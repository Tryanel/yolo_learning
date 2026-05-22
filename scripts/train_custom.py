from __future__ import annotations

import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a custom YOLO detection model.")
    parser.add_argument("--data", required=True, help="Path to dataset.yaml.")
    parser.add_argument("--model", default="yolo11n.pt", help="Base model weight path or official model name.")
    parser.add_argument("--epochs", type=int, default=50, help="Training epochs.")
    parser.add_argument("--imgsz", type=int, default=640, help="Training image size.")
    parser.add_argument("--batch", type=int, default=-1, help="Batch size. Use -1 for auto batch when supported.")
    parser.add_argument("--device", default=None, help="Device, for example 'cpu', '0', or leave empty for auto.")
    parser.add_argument("--project", default="outputs/train", help="Output project folder.")
    parser.add_argument("--name", default="custom_yolo", help="Output run name.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    Path(args.project).mkdir(parents=True, exist_ok=True)

    model = YOLO(args.model)
    results = model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
        project=args.project,
        name=args.name,
    )

    print("Training finished.")
    print(f"Results: {results}")
    print(f"Check weights under: {Path(args.project) / args.name / 'weights'}")


if __name__ == "__main__":
    main()

