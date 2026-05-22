from __future__ import annotations

import argparse
import datetime as dt
import json
import tarfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "course" / "labs.json"
PLACEHOLDERS = ("TODO", "<TODO>", "待填写", "TBD")


@dataclass
class CheckResult:
    ok: bool
    points: int
    message: str


def load_manifest() -> dict[str, Any]:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def labs() -> list[dict[str, Any]]:
    return load_manifest()["labs"]


def find_lab(lab_id: str) -> dict[str, Any]:
    for lab in labs():
        if lab["id"] == lab_id:
            return lab
    known = ", ".join(lab["id"] for lab in labs())
    raise SystemExit(f"Unknown lab '{lab_id}'. Known labs: {known}")


def rel(path: str | Path) -> Path:
    return ROOT / Path(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has_placeholder(text: str) -> bool:
    upper = text.upper()
    return any(token.upper() in upper for token in PLACEHOLDERS)


def check_required_file(path: str) -> CheckResult:
    file_path = rel(path)
    if not file_path.exists():
        return CheckResult(False, 0, f"missing required file: {path}")
    if file_path.is_dir():
        return CheckResult(False, 0, f"required path is a directory, expected file: {path}")
    if file_path.stat().st_size == 0:
        return CheckResult(False, 0, f"required file is empty: {path}")
    return CheckResult(True, 1, f"found: {path}")


def check_no_placeholder(path: str) -> CheckResult:
    file_path = rel(path)
    if not file_path.exists():
        return CheckResult(False, 0, f"cannot inspect missing file: {path}")
    text = read_text(file_path)
    if has_placeholder(text):
        return CheckResult(False, 0, f"replace TODO placeholders in: {path}")
    if len(text.strip()) < 80:
        return CheckResult(False, 0, f"write a more complete response in: {path}")
    return CheckResult(True, 1, f"no placeholders: {path}")


def check_integer_hours(path: str) -> CheckResult:
    file_path = rel(path)
    if not file_path.exists():
        return CheckResult(False, 0, f"missing time file: {path}")
    value = read_text(file_path).strip()
    if has_placeholder(value):
        return CheckResult(False, 0, f"replace TODO with an integer hour count: {path}")
    try:
        hours = int(value)
    except ValueError:
        return CheckResult(False, 0, f"time file must contain one integer: {path}")
    if hours < 0:
        return CheckResult(False, 0, f"time cannot be negative: {path}")
    return CheckResult(True, 1, f"time recorded: {hours} hour(s)")


def check_contains_any(path: str, needles: list[str]) -> CheckResult:
    file_path = rel(path)
    if not file_path.exists():
        return CheckResult(False, 0, f"cannot inspect missing file: {path}")
    raw = read_text(file_path)
    if has_placeholder(raw):
        return CheckResult(False, 0, f"replace TODO placeholders before vocabulary check: {path}")
    text = raw.lower()
    if any(needle.lower() in text for needle in needles):
        return CheckResult(True, 1, f"contains expected lab vocabulary: {path}")
    joined = ", ".join(needles)
    return CheckResult(False, 0, f"expected at least one of [{joined}] in: {path}")


def check_contains_all(path: str, needles: list[str]) -> CheckResult:
    file_path = rel(path)
    if not file_path.exists():
        return CheckResult(False, 0, f"cannot inspect missing file: {path}")
    raw = read_text(file_path)
    if has_placeholder(raw):
        return CheckResult(False, 0, f"replace TODO placeholders before section check: {path}")
    text = raw.lower()
    missing = [needle for needle in needles if needle.lower() not in text]
    if missing:
        return CheckResult(False, 0, f"missing required section words {missing} in: {path}")
    return CheckResult(True, 1, f"contains required section words: {path}")


def check_dataset_yaml(path: str) -> CheckResult:
    file_path = rel(path)
    if not file_path.exists():
        return CheckResult(False, 0, f"missing dataset YAML: {path}")
    text = read_text(file_path)
    if has_placeholder(text):
        return CheckResult(False, 0, f"replace placeholders in dataset YAML: {path}")

    required_keys = ["path:", "train:", "val:", "names:"]
    missing = [key for key in required_keys if key not in text]
    if missing:
        return CheckResult(False, 0, f"dataset YAML missing keys {missing}: {path}")

    names_index = text.find("names:")
    names_block = text[names_index:]
    has_class = any(line.strip().startswith("0:") or line.strip().startswith("- ") for line in names_block.splitlines()[1:10])
    if not has_class:
        return CheckResult(False, 0, f"dataset YAML needs at least class 0 under names: {path}")
    return CheckResult(True, 1, f"dataset YAML structure looks usable: {path}")


def run_special_check(check: dict[str, Any]) -> CheckResult:
    kind = check["type"]
    path = check.get("path", "")
    if kind == "no_placeholder":
        return check_no_placeholder(path)
    if kind == "integer_hours":
        return check_integer_hours(path)
    if kind == "contains_any":
        return check_contains_any(path, check["needles"])
    if kind == "contains_all":
        return check_contains_all(path, check["needles"])
    if kind == "dataset_yaml":
        return check_dataset_yaml(path)
    return CheckResult(False, 0, f"unknown check type: {kind}")


def grade_lab(lab_id: str, quiet: bool = False) -> tuple[int, list[CheckResult]]:
    lab = find_lab(lab_id)
    results: list[CheckResult] = []
    for path in lab.get("required_files", []):
        results.append(check_required_file(path))
    for check in lab.get("checks", []):
        results.append(run_special_check(check))

    if not results:
        score = 0
    else:
        score = round(100 * sum(1 for result in results if result.ok) / len(results))

    if not quiet:
        print(f"{lab['id']}: {lab['title']}")
        for result in results:
            mark = "PASS" if result.ok else "FAIL"
            print(f"  [{mark}] {result.message}")
        print(f"score: {score}/100")
    return score, results


def cmd_list(_: argparse.Namespace) -> None:
    for lab in labs():
        print(f"{lab['id']}  week {lab['week']}  {lab['title']}")


def cmd_show(args: argparse.Namespace) -> None:
    lab = find_lab(args.lab)
    readme = ROOT / "labs" / lab["id"] / "README.md"
    print(f"{lab['id']}: {lab['title']}")
    print(f"README: {readme}")
    print()
    if readme.exists():
        print(read_text(readme))
    else:
        print("No README found for this lab.")


def cmd_grade(args: argparse.Namespace) -> None:
    if args.lab == "all":
        total = 0
        for lab in labs():
            score, _ = grade_lab(lab["id"], quiet=True)
            total += score
            print(f"{lab['id']}: {score}/100")
        print(f"average: {round(total / len(labs()))}/100")
        return
    grade_lab(args.lab)


def cmd_status(_: argparse.Namespace) -> None:
    for lab in labs():
        score, _ = grade_lab(lab["id"], quiet=True)
        state = "done" if score == 100 else "template" if score <= 50 else "in-progress"
        print(f"{lab['id']:<6} {score:>3}/100  {state:<12} {lab['title']}")


def cmd_handin(args: argparse.Namespace) -> None:
    lab = find_lab(args.lab)
    score, results = grade_lab(args.lab, quiet=True)
    if score < 100 and not args.force:
        print(f"{args.lab} is not passing yet ({score}/100). Use --force to package anyway.")
        for result in results:
            if not result.ok:
                print(f"  FAIL: {result.message}")
        raise SystemExit(1)

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = ROOT / "handin"
    out_dir.mkdir(exist_ok=True)
    tar_path = out_dir / f"{args.lab}_{timestamp}.tar.gz"

    paths: list[Path] = []
    paths.append(ROOT / "labs" / lab["id"] / "README.md")
    for item in lab.get("required_files", []):
        candidate = rel(item)
        if candidate.exists():
            paths.append(candidate)

    with tarfile.open(tar_path, "w:gz") as tar:
        for path in paths:
            tar.add(path, arcname=path.relative_to(ROOT))

    print(f"created: {tar_path}")
    print(f"score packaged: {score}/100")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Course helper for YOLO Learning Lab.")
    sub = parser.add_subparsers(required=True)

    list_parser = sub.add_parser("list", help="List labs.")
    list_parser.set_defaults(func=cmd_list)

    status_parser = sub.add_parser("status", help="Show grading status for all labs.")
    status_parser.set_defaults(func=cmd_status)

    show_parser = sub.add_parser("show", help="Print a lab README.")
    show_parser.add_argument("lab", help="Lab id, for example lab00.")
    show_parser.set_defaults(func=cmd_show)

    grade_parser = sub.add_parser("grade", help="Grade a lab or all labs.")
    grade_parser.add_argument("lab", help="Lab id, or 'all'.")
    grade_parser.set_defaults(func=cmd_grade)

    handin_parser = sub.add_parser("handin", help="Create a hand-in tarball for a lab.")
    handin_parser.add_argument("lab", help="Lab id, for example lab00.")
    handin_parser.add_argument("--force", action="store_true", help="Package even if the lab does not pass.")
    handin_parser.set_defaults(func=cmd_handin)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
