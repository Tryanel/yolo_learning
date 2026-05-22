from __future__ import annotations

import argparse

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate a trained YOLO model.")
    parser.add_argument("--model", required=True, help="Path to trained weights, for example best.pt.")
    parser.add_argument("--data", required=True, help="Path to dataset.yaml.")
    parser.add_argument("--imgsz", type=int, default=640, help="Validation image size.")
    parser.add_argument("--conf", type=float, default=0.001, help="Confidence threshold for validation.")
    parser.add_argument("--device", default=None, help="Device, for example 'cpu', '0', or leave empty for auto.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = YOLO(args.model)
    metrics = model.val(data=args.data, imgsz=args.imgsz, conf=args.conf, device=args.device)

    print("Validation finished.")
    box = getattr(metrics, "box", None)
    if box is not None:
        print(f"mAP50: {box.map50:.4f}")
        print(f"mAP50-95: {box.map:.4f}")
        print(f"Precision mean: {box.mp:.4f}")
        print(f"Recall mean: {box.mr:.4f}")
    else:
        print(metrics)


if __name__ == "__main__":
    main()

