from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import yaml


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect a YOLO detection dataset.")
    parser.add_argument("--data", required=True, help="Path to dataset.yaml.")
    return parser.parse_args()


def resolve_split(root: Path, split_value: str) -> Path:
    split_path = Path(split_value)
    return split_path if split_path.is_absolute() else root / split_path


def list_images(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return sorted(p for p in path.rglob("*") if p.suffix.lower() in IMAGE_EXTENSIONS)


def inspect_label(label_path: Path, class_count: int) -> list[str]:
    errors: list[str] = []
    if not label_path.exists():
        return [f"missing label: {label_path}"]

    lines = [line.strip() for line in label_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    for index, line in enumerate(lines, start=1):
        parts = line.split()
        if len(parts) != 5:
            errors.append(f"{label_path}:{index} expected 5 values, got {len(parts)}")
            continue
        try:
            class_id = int(parts[0])
            values = [float(value) for value in parts[1:]]
        except ValueError:
            errors.append(f"{label_path}:{index} contains non-numeric values")
            continue
        if class_id < 0 or class_id >= class_count:
            errors.append(f"{label_path}:{index} class id {class_id} outside 0..{class_count - 1}")
        if any(value < 0 or value > 1 for value in values):
            errors.append(f"{label_path}:{index} box values must be normalized into 0..1")
    return errors


def main() -> None:
    args = parse_args()
    data_path = Path(args.data)
    config = yaml.safe_load(data_path.read_text(encoding="utf-8"))

    root = Path(config.get("path", data_path.parent))
    if not root.is_absolute():
        root = data_path.parent / root if not (data_path.parent / root).exists() else data_path.parent / root
        if not root.exists():
            root = Path(config.get("path", "."))

    names = config.get("names", {})
    if isinstance(names, list):
        class_count = len(names)
    elif isinstance(names, dict):
        class_count = len(names)
    else:
        raise ValueError("dataset.yaml field 'names' must be a list or dict")

    print(f"Dataset config: {data_path}")
    print(f"Dataset root: {root.resolve()}")
    print(f"Classes: {class_count} -> {names}")
    print()

    total_images = 0
    total_errors: list[str] = []
    split_counts: Counter[str] = Counter()

    for split in ["train", "val", "test"]:
        if split not in config:
            continue
        image_dir = resolve_split(root, config[split])
        images = list_images(image_dir)
        split_counts[split] = len(images)
        total_images += len(images)
        print(f"{split}: {len(images)} images at {image_dir}")

        label_dir = Path(str(image_dir).replace(f"{Path.sep}images{Path.sep}", f"{Path.sep}labels{Path.sep}"))
        for image_path in images:
            label_path = label_dir / f"{image_path.stem}.txt"
            total_errors.extend(inspect_label(label_path, class_count))

    print()
    print(f"Total images: {total_images}")
    print(f"Split counts: {dict(split_counts)}")

    if total_errors:
        print()
        print("Potential label issues:")
        for error in total_errors[:50]:
            print(f"- {error}")
        if len(total_errors) > 50:
            print(f"... and {len(total_errors) - 50} more")
        raise SystemExit(1)

    print("Dataset inspection passed.")


if __name__ == "__main__":
    main()

