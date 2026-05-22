from __future__ import annotations

import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run YOLO prediction on images or a folder.")
    parser.add_argument("--source", required=True, help="Image path, folder path, URL, or glob pattern.")
    parser.add_argument("--model", default="yolo11n.pt", help="Model weight path or official model name.")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold.")
    parser.add_argument("--imgsz", type=int, default=640, help="Inference image size.")
    parser.add_argument("--project", default="outputs/predict", help="Output project folder.")
    parser.add_argument("--name", default="images", help="Output run name.")
    parser.add_argument("--show", action="store_true", help="Show prediction window.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    Path(args.project).mkdir(parents=True, exist_ok=True)

    model = YOLO(args.model)
    results = model.predict(
        source=args.source,
        conf=args.conf,
        imgsz=args.imgsz,
        project=args.project,
        name=args.name,
        save=True,
        show=args.show,
    )

    print(f"Predictions finished. Images processed: {len(results)}")
    print(f"Output folder: {Path(args.project) / args.name}")


if __name__ == "__main__":
    main()

