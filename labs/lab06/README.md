# Lab 06: Export and Lightweight Inference

## Goal

Export or benchmark your trained model and decide what is realistic on weak local hardware.

## Background

Deployment is a set of tradeoffs: accuracy, latency, model size, runtime, hardware, and licensing. Export formats such as ONNX or OpenVINO can help CPU inference, but they add their own compatibility surface.

## Tasks

1. Try exporting to ONNX:

```powershell
python scripts/export_model.py --model outputs/best.pt --format onnx
```

2. If local export fails, run the export in Colab and record the issue.
3. Measure or estimate local prediction latency on a few images.
4. Compare `.pt` inference and exported inference if possible.
5. Fill in `submissions/lab06/export_report.md`.
6. Record time spent in `submissions/lab06/time.txt`.

## Hints

- Export is not the same as deployment.
- A slower but reliable cloud demo may be better than a fragile local webcam demo.
- Keep your report honest about what was measured and what was estimated.

## Grade

```powershell
python tools/course.py grade lab06
```

## Submit

```powershell
python tools/course.py handin lab06
```

