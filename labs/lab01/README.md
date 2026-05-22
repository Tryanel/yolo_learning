# Lab 01: Detection Geometry - Boxes, IoU, and NMS

## Goal

Understand the geometry behind object detection before trusting model output. You will reason about bounding boxes, confidence thresholds, IoU, and non-maximum suppression.

## Background

YOLO returns boxes. A useful practitioner must know whether a box is good, duplicated, too loose, too tight, or just confidently wrong. IoU and NMS are the small pieces of math that make this visible.

## Tasks

1. Draw at least five example boxes by hand on images of your choice.
2. For two pairs of boxes, estimate IoU by reasoning about overlap and union.
3. Explain what happens when the confidence threshold is too low or too high.
4. Explain what NMS is trying to remove.
5. Fill in `submissions/lab01/iou_exercises.md`.
6. Record time spent in `submissions/lab01/time.txt`.

## Hints

- A high-confidence prediction can still have a poor box.
- A low-confidence prediction can still reveal a useful hard case.
- NMS suppresses duplicate boxes; it does not magically fix incorrect classes.

## Grade

```powershell
python tools/course.py grade lab01
```

## Submit

```powershell
python tools/course.py handin lab01
```

