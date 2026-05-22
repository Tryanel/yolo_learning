from __future__ import annotations

import argparse

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a YOLO model to a deployment format.")
    parser.add_argument("--model", required=True, help="Path to trained weights, for example best.pt.")
    parser.add_argument("--format", default="onnx", help="Export format, for example onnx, torchscript, engine.")
    parser.add_argument("--imgsz", type=int, default=640, help="Export image size.")
    parser.add_argument("--device", default=None, help="Device, for example 'cpu', '0', or leave empty for auto.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = YOLO(args.model)
    exported = model.export(format=args.format, imgsz=args.imgsz, device=args.device)
    print(f"Export finished: {exported}")


if __name__ == "__main__":
    main()

