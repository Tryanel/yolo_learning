# YOLO Model Textbook

Version date: 2026-05-22

This textbook is the reading companion for YOLO Learning Lab. It is written for a learner with no prior model experience and assumes a weak local computer. The course path is therefore local-light and cloud-heavy: learn, organize, inspect, and write locally; train and host on cloud resources when needed.

## Table of Contents

- Chapter 0: How to Use This Book
- Chapter 1: The Computer Vision Problem
- Chapter 2: Bounding Boxes and Detection Geometry
- Chapter 3: What YOLO Is Really Doing
- Chapter 4: Running Pretrained Prediction
- Chapter 5: Building a YOLO Dataset
- Chapter 6: Training in the Cloud
- Chapter 7: Validation and Error Analysis
- Chapter 8: Export and Deployment
- Chapter 9: Project Engineering
- Chapter 10: Final Project Checklist
- Appendix A: Formulas
- Appendix B: Command Reference
- Appendix C: Glossary
- Appendix D: References

---

## Chapter 0: How to Use This Book

YOLO is easiest to learn when you stop treating it as a mysterious neural network and start treating it as a system:

1. Images enter the system.
2. Labels describe objects in those images.
3. A model predicts boxes and classes.
4. Metrics summarize performance.
5. Error cases tell you what data to collect next.
6. Deployment constraints decide how the model is used.

This book follows that system order. Each chapter maps to a lab:

| Chapter | Lab | Main Skill |
| --- | --- | --- |
| 1 | `lab00` | Set up local environment and course tools |
| 2 | `lab01` | Understand boxes, IoU, and NMS |
| 3-4 | `lab02` | Run pretrained prediction |
| 5 | `lab03` | Build and audit a dataset |
| 6 | `lab04` | Train in the cloud |
| 7 | `lab05` | Evaluate and improve |
| 8 | `lab06`, `lab07` | Export and deploy |
| 9-10 | `lab08` | Build a reproducible final project |

The most important habit is recording evidence. When something fails, write down:

- command run
- input paths
- output paths
- error message
- what you changed next

That habit is what turns random experimentation into engineering.

---

## Chapter 1: The Computer Vision Problem

Computer vision models turn pixels into structured information. For this course, the important task types are:

| Task | Question | Output |
| --- | --- | --- |
| Image classification | What is the main thing in this image? | One or more labels |
| Object detection | What objects are present, and where are they? | Boxes, classes, confidence scores |
| Instance segmentation | Which pixels belong to each object instance? | Masks per object |
| Semantic segmentation | Which class does each pixel belong to? | Class map |
| Pose estimation | Where are keypoints? | Points and skeletons |

YOLO is most famous for object detection. In object detection, the model must solve two problems at the same time:

- Classification: what is the object?
- Localization: where is the object?

This is why detection is harder than classification. A classifier can be right with one label. A detector must be right about class and position for every visible object.

### What Counts as an Object?

An object should be visually definable. "Cup" is usually a good class. "Useful cup" is not, because usefulness is not directly visible. "Worker wearing helmet" may be too composite for a first dataset; "helmet" is cleaner.

Good beginner classes have:

- visible boundaries
- enough examples
- limited ambiguity
- real use value

Poor beginner classes often have:

- tiny objects
- transparent or reflective surfaces
- severe occlusion
- class differences based on text or subtle texture
- concepts that require context rather than appearance

### Local-Light Strategy

Training can be expensive. This course assumes your local computer may be weak, so you should split work:

- Local: code, notes, sample prediction, dataset organization.
- Cloud: training, heavy validation, hosted demo.

The goal is not to avoid compute. The goal is to spend compute only after your data and commands are clear.

---

## Chapter 2: Bounding Boxes and Detection Geometry

An object detector predicts rectangular boxes. A box is usually represented in one of two formats:

| Format | Meaning |
| --- | --- |
| `xyxy` | left, top, right, bottom |
| `xywh` | center x, center y, width, height |

YOLO label files use normalized `xywh`:

```text
class_id x_center y_center width height
```

All four numbers are ratios from 0 to 1. If an image is 1000 px wide and the box center is at x=500 px, normalized `x_center` is `0.5`.

### Intersection over Union

IoU measures how much two boxes overlap:

```text
IoU = area(intersection) / area(union)
```

If two boxes do not overlap, IoU is 0. If they are identical, IoU is 1.

IoU is used for:

- deciding whether a prediction matches a ground-truth box
- evaluating box quality
- removing duplicate predictions during NMS

### Confidence

A detection result usually has a confidence score. In practice, a higher confidence threshold means:

- fewer predictions
- fewer false positives
- more risk of missed objects

A lower confidence threshold means:

- more predictions
- more false positives
- fewer missed low-confidence objects

There is no universal best threshold. You choose based on the application. For safety inspection, recall may matter more. For auto-counting inventory, false positives may be expensive.

### Non-Maximum Suppression

Models often predict multiple boxes around the same object. NMS keeps the strongest box and suppresses overlapping duplicates.

The rough logic is:

1. Sort boxes by confidence.
2. Keep the highest-confidence box.
3. Remove lower-confidence boxes with high IoU against the kept box.
4. Repeat.

NMS helps with duplicates, but it cannot fix a bad class definition or missing training data.

---

## Chapter 3: What YOLO Is Really Doing

YOLO means "You Only Look Once." The original idea was to frame detection as a single pass through the network rather than a multi-stage proposal pipeline.

Modern YOLO implementations differ from the original paper, but the practical interface remains similar:

```text
image -> model -> boxes + classes + scores
```

### The Model as a Pipeline

A YOLO model has several conceptual parts:

- Backbone: extracts visual features from the image.
- Neck: mixes features across scales.
- Head: predicts boxes, classes, and objectness/confidence.
- Post-processing: filters predictions, applies NMS, formats results.

You do not need to implement these parts in this beginner course. You do need to know where errors can come from.

If small objects are missed, the issue may involve feature scale, input resolution, training data, or annotation quality. If classes are confused, the issue may be class definitions, label noise, or insufficient examples.

### Pretrained Weights

Training from scratch is usually wasteful for beginners. Pretrained weights already understand many visual primitives:

- edges
- textures
- object parts
- common object layouts

Fine-tuning starts from this useful prior and adapts it to your dataset.

### Model Size

YOLO models often come in sizes such as nano, small, medium, large, or extra-large. Larger models can be more accurate, but they require more compute and can be slower.

Beginner rule:

1. Start with nano.
2. Fix data and labels.
3. Only then try a larger model.

---

## Chapter 4: Running Pretrained Prediction

Prediction is the safest first interaction with YOLO because no training is required.

The key parameters are:

| Parameter | Meaning |
| --- | --- |
| `model` | weight file or official model name |
| `source` | image, folder, video, URL, webcam index |
| `conf` | confidence threshold |
| `imgsz` | input image size |
| `save` | whether to save visual output |

Example:

```powershell
python scripts/predict_image.py --source data/samples --model yolo11n.pt --imgsz 320 --conf 0.25
```

If your machine is weak:

- use a nano model
- set `imgsz` to 320 or 416
- predict on still images first
- avoid webcam demos until later

### Reading Prediction Output

A prediction image is not enough. For each result, ask:

- Did it find all visible target objects?
- Did it hallucinate objects in the background?
- Are boxes too loose or too tight?
- Are small objects missed?
- Does confidence match visual certainty?

The model is not a judge. You are the judge.

### Common First Observations

You will probably see:

- common COCO objects detected well
- domain-specific objects missed
- small objects missed
- reflective or blurry objects misread
- confidence threshold changing the number of boxes

That is normal. It tells you why custom data matters.

---

## Chapter 5: Building a YOLO Dataset

A YOLO dataset has images, label text files, and a YAML config.

Typical structure:

```text
data/yolo_dataset/
  images/
    train/
    val/
    test/
  labels/
    train/
    val/
    test/
  dataset.yaml
```

Example `dataset.yaml`:

```yaml
path: data/yolo_dataset
train: images/train
val: images/val
test: images/test

names:
  0: phone
  1: cup
  2: mouse
```

Label file example:

```text
0 0.512 0.433 0.210 0.315
2 0.721 0.602 0.180 0.140
```

Each line means:

```text
class_id x_center y_center width height
```

### Train / Val / Test Split

Training set teaches the model. Validation set helps you monitor generalization. Test set is held for final evaluation.

Beginner split:

- train: 70-80%
- val: 10-20%
- test: 10%

If the dataset is very small, keep a validation set but do not over-interpret metrics. Visual error analysis will matter more.

### Annotation Quality

Bad labels create bad models. Common label problems:

- missing objects
- boxes too loose
- boxes too tight
- inconsistent class choice
- wrong class id
- normalized coordinates outside 0-1
- duplicate labels for one object

Annotation rules should be written down. For example:

- Box the visible part only, not the imagined hidden part.
- Label a cup even if partially occluded, if at least 30% is visible.
- Do not label objects smaller than 12 pixels unless the project requires tiny objects.

### Dataset Versioning

Do not keep changing data without naming versions. Use a simple convention:

```text
dataset_v0_smoke
dataset_v1_initial
dataset_v2_more_low_light
dataset_v3_fixed_labels
```

Your model report should always say which dataset version it used.

---

## Chapter 6: Training in the Cloud

Training adjusts model weights so predictions fit your dataset. Cloud training is recommended when local hardware is weak.

The typical training call is:

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
model.train(
    data="/content/yolo_dataset/dataset.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    project="/content/outputs/train",
    name="custom_yolo",
)
```

### Smoke Run First

Before spending time on full training, run a short smoke test:

```python
model.train(data="dataset.yaml", epochs=3, imgsz=320)
```

This catches:

- wrong paths
- malformed labels
- missing images
- class id mismatch
- unavailable GPU

If the smoke run fails, do not tune hyperparameters. Fix the data path or label issue.

### Important Training Parameters

| Parameter | Effect |
| --- | --- |
| `epochs` | how many times the model sees the training set |
| `imgsz` | input resolution; larger may help small objects but costs compute |
| `batch` | images per training step; too high can exceed memory |
| `model` | starting weights and model size |
| `patience` | early stopping patience in some training configs |

### What to Save

At the end of a training lab, save:

- `best.pt`
- training command
- dataset version
- key metrics
- confusion matrix or result plots if available
- example predictions
- notebook link or exported notebook

Do not trust memory. Future you will not remember which model came from which dataset.

---

## Chapter 7: Validation and Error Analysis

Validation gives metrics. Error analysis gives direction.

Common detection metrics:

- Precision: of predicted detections, how many are correct?
- Recall: of true objects, how many were found?
- AP: area under the precision-recall curve for a class.
- mAP: mean AP across classes.
- mAP50: mAP at IoU threshold 0.50.
- mAP50-95: average mAP over multiple IoU thresholds.

### How to Read Metrics

High precision, low recall:

- The model is conservative.
- It avoids false positives but misses objects.
- Lower confidence threshold or collect hard positives.

Low precision, high recall:

- The model finds many objects but also hallucinates.
- Raise threshold or collect confusing negative/background examples.

Low mAP for one class:

- That class may have fewer examples.
- Labels may be inconsistent.
- The class may be visually similar to another class.

### Error Buckets

Create a table with these buckets:

| Bucket | Meaning | Likely next action |
| --- | --- | --- |
| False negative | object missed | add similar examples, lower threshold |
| False positive | background detected as object | add hard negatives, adjust threshold |
| Bad box | class right, box poor | fix labels, increase resolution |
| Class confusion | wrong class | clarify labels, merge classes, add examples |
| Duplicate boxes | multiple boxes on same object | inspect NMS/conf settings |
| Domain shift | new scene fails | collect data from target scene |

### One-Variable Iteration

Change one major thing at a time:

- dataset version
- label rules
- image size
- model size
- training duration

If you change everything at once, you will not know why results changed.

---

## Chapter 8: Export and Deployment

Training creates a model file. Deployment makes it usable.

Common routes:

| Route | Good for | Risk |
| --- | --- | --- |
| `.pt` with Ultralytics | Python demos, notebooks | needs Python and PyTorch |
| ONNX | cross-runtime inference | post-processing details |
| OpenVINO | CPU acceleration | hardware/runtime-specific setup |
| TensorRT | NVIDIA GPU deployment | environment complexity |
| Hosted API | easy demo | cost, privacy, latency |
| Hugging Face Spaces | portfolio demo | cold starts, resource limits |

Export example:

```powershell
python scripts/export_model.py --model outputs/best.pt --format onnx
```

### Deployment Questions

Before deploying, answer:

- Who uploads the image?
- Where is the image stored?
- How fast must prediction be?
- What happens when the model is wrong?
- What hardware is available?
- What license applies?
- Can the model process sensitive data?

### Weak Local Machine Strategy

If local deployment is too slow:

- keep local as a client only
- run inference in a hosted notebook
- use a hosted API
- export to CPU-friendly runtime
- reduce image size
- process every Nth video frame

Do not let "webcam real-time" become a blocker. A reliable image upload demo is already a valid first deployment.

---

## Chapter 9: Project Engineering

A YOLO project is more than a model. It needs structure.

Recommended final project layout:

```text
project/
  README.md
  data_card.md
  model_card.md
  train.py
  predict.py
  dataset.yaml
  examples/
  reports/
```

### Data Card

A data card should include:

- classes
- image count
- source
- collection conditions
- annotation rules
- known bias
- train/val/test split
- privacy concerns

### Model Card

A model card should include:

- base model
- dataset version
- training command
- metrics
- intended use
- out-of-scope use
- known failure modes
- license notes

### Reproducibility

Every result should be traceable:

```text
dataset version + code commit + training command + model artifact = experiment
```

This is the heart of the course. A mediocre but reproducible model is easier to improve than an impressive result you cannot recreate.

---

## Chapter 10: Final Project Checklist

Your final project should answer six questions:

1. What problem does the model solve?
2. What data did it learn from?
3. How was it trained?
4. How well does it work?
5. Where does it fail?
6. How can someone run or inspect it?

Minimum final deliverables:

- problem statement
- dataset description
- training command
- metrics
- five example predictions
- error analysis
- deployment or demo plan
- next data iteration plan

### Good Final Project Example

"Detect cups and phones on my desk" is a good beginner project if it includes:

- clear class definitions
- 100-300 labeled images
- varied lighting and angles
- documented training run
- examples of missed reflections or occlusions
- a simple upload-image demo

### Weak Final Project Example

"Detect all dangerous things" is weak because:

- classes are unclear
- object boundaries are ambiguous
- data collection is huge
- failure costs are high
- evaluation is underspecified

Start narrow. Earn complexity later.

---

## Appendix A: Formulas

### Convert Pixel Box to YOLO Format

Given:

```text
image_width = W
image_height = H
left = x1
top = y1
right = x2
bottom = y2
```

Then:

```text
x_center = ((x1 + x2) / 2) / W
y_center = ((y1 + y2) / 2) / H
width = (x2 - x1) / W
height = (y2 - y1) / H
```

### IoU

```text
intersection_width = max(0, min(x2_a, x2_b) - max(x1_a, x1_b))
intersection_height = max(0, min(y2_a, y2_b) - max(y1_a, y1_b))
intersection_area = intersection_width * intersection_height
union_area = area_a + area_b - intersection_area
IoU = intersection_area / union_area
```

### Precision and Recall

```text
precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)
```

---

## Appendix B: Command Reference

Course commands:

```powershell
python tools/course.py list
python tools/course.py show lab00
python tools/course.py grade lab00
python tools/course.py status
python tools/course.py handin lab00
```

Environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
python scripts/check_environment.py
```

Prediction:

```powershell
python scripts/predict_image.py --source data/samples --model yolo11n.pt --imgsz 320 --conf 0.25
```

Dataset inspection:

```powershell
python scripts/inspect_dataset.py --data data/yolo_dataset/dataset.yaml
```

Training:

```powershell
python scripts/train_custom.py --data data/yolo_dataset/dataset.yaml --model yolo11n.pt --epochs 50 --imgsz 640
```

Validation:

```powershell
python scripts/evaluate_model.py --model outputs/train/custom_yolo/weights/best.pt --data data/yolo_dataset/dataset.yaml
```

Export:

```powershell
python scripts/export_model.py --model outputs/train/custom_yolo/weights/best.pt --format onnx
```

---

## Appendix C: Glossary

AP: Average Precision for one class.

Backbone: neural network layers that extract visual features.

Bounding box: rectangle around an object.

Class: object category.

Confidence: model score for a detection.

Dataset YAML: config file that tells YOLO where images, labels, and class names are.

Epoch: one pass through the training set.

False negative: a real object that the model missed.

False positive: a predicted object that is not really there.

IoU: intersection over union, a box overlap score.

mAP: mean Average Precision across classes.

NMS: non-maximum suppression, duplicate-box filtering.

ONNX: model exchange format used by multiple runtimes.

Pretrained weights: model weights learned from a previous dataset.

Recall: fraction of real objects found.

Validation set: held-out data used to evaluate generalization during development.

YOLO: You Only Look Once, a family of real-time object detection models.

---

## Appendix D: References

- Ultralytics Python Usage: https://docs.ultralytics.com/usage/python
- Ultralytics Object Detection Dataset Format: https://docs.ultralytics.com/datasets/detect
- Ultralytics CLI Usage: https://docs.ultralytics.com/usage/cli
- Original YOLO paper: https://arxiv.org/abs/1506.02640
- Lab-based course design pattern: reading, lab handout, grading command, and hand-in artifact
