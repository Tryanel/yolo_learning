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
- Appendix D: Study Questions
- Appendix E: References

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

![Lab-driven learning loop](../assets/lab_workflow.svg)

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

### Where to Slow Down

You do not need to understand every neural-network layer on day one. You do need three practical instincts.

First, build input-output instinct. Know what files the model reads, what files it writes, and what each number in the output means.

Second, build data instinct. Learn to see whether classes are visually clear, labels are consistent, and validation images resemble the real use case.

Third, build experiment instinct. When a result changes, you should be able to explain what likely caused it. If you change the dataset, model size, image size, epoch count, and confidence threshold all at once, the result may improve but you will not know why.

Whenever you run a command, ask:

- What is the input?
- Where will the output be written?
- If the result is bad, should I inspect data, parameters, or deployment environment first?

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

### From Pixels to Structured Output

An image is a grid of numbers. A color image usually has red, green, and blue channels. Humans see cups, screens, reflections, and shadows; the model starts with numeric intensity values.

A vision network gradually turns low-level signals into higher-level clues:

```text
pixel values -> edges/colors -> texture -> parts -> objects -> class and location
```

Object detection output is not a sentence. It is closer to a table:

| class | confidence | x_center | y_center | width | height |
| --- | --- | --- | --- | --- | --- |
| cup | 0.91 | 0.52 | 0.48 | 0.18 | 0.31 |
| phone | 0.77 | 0.71 | 0.62 | 0.20 | 0.12 |

Each row is a candidate object. Confidence filtering, NMS, and metrics all operate on these candidate rows.

### Classification, Detection, and Segmentation

If your question is "is there a helmet in this image?", classification may be enough.

If your question is "where is each helmet, and who is missing one?", detection is the right first tool.

If your question is "which exact pixels belong to the helmet?", segmentation is more appropriate.

YOLO family models can support multiple vision tasks. This course starts with detection because it exposes the full engineering loop: annotation, training, validation, error analysis, export, and deployment.

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

![Local-light and cloud-heavy workflow](../assets/local_cloud_workflow.svg)

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

### Pixel-to-YOLO Example

Assume an image is `1280 x 720`. A cup has this pixel box:

```text
top-left = (384, 180)
bottom-right = (640, 540)
```

First compute center and size in pixels:

```text
x_center_px = (384 + 640) / 2 = 512
y_center_px = (180 + 540) / 2 = 360
width_px = 640 - 384 = 256
height_px = 540 - 180 = 360
```

Then divide by image width and height:

```text
x_center = 512 / 1280 = 0.400
y_center = 360 / 720 = 0.500
width = 256 / 1280 = 0.200
height = 360 / 720 = 0.500
```

If the cup class id is `1`, the YOLO label line is:

```text
1 0.400 0.500 0.200 0.500
```

Many beginner dataset bugs come from mixing `xyxy` with `xywh`, forgetting normalization, or swapping image width and height.

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

### A Numeric IoU Example

Suppose two boxes each have area `100`, and their overlap area is `60`. The union is not `200`, because the overlap was counted twice:

```text
union = 100 + 100 - 60 = 140
IoU = 60 / 140 = 0.429
```

So two boxes can look meaningfully overlapped while still having IoU below `0.5`. When you see `mAP50` or an `IoU=0.5` matching rule, it is asking whether the predicted box overlaps the true box by at least that threshold.

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

![Bounding boxes, IoU, and NMS](../assets/box_iou_nms.svg)

### Understanding Thresholds

YOLO prediction commonly exposes a confidence threshold and an IoU threshold.

`conf` decides whether a candidate is confident enough to keep. Raise it and the model reports fewer boxes. Lower it and the model reports more boxes.

The NMS IoU threshold decides how much overlap counts as a duplicate. If it is too low, two nearby real objects may collapse into one. If it is too high, duplicate boxes may remain.

Treat thresholds as application choices, not magic constants:

| Setting | Typical effect | Useful when |
| --- | --- | --- |
| Lower `conf` | More detections, more false positives | Missing objects is expensive |
| Higher `conf` | Fewer detections, more conservative | False positives are expensive |
| Lower NMS `iou` | Fewer duplicate boxes, possible merging | Objects are sparse |
| Higher NMS `iou` | Nearby objects are preserved, duplicates may remain | Objects are dense |

---

## Chapter 3: What YOLO Is Really Doing

YOLO means "You Only Look Once." The original idea was to frame detection as a single pass through the network rather than a multi-stage proposal pipeline.

Modern YOLO implementations differ from the original paper, but the practical interface remains similar:

```text
image -> model -> boxes + classes + scores
```

![YOLO object detection pipeline](../assets/yolo_pipeline.svg)

### The Model as a Pipeline

A YOLO model has several conceptual parts:

- Backbone: extracts visual features from the image.
- Neck: mixes features across scales.
- Head: predicts boxes, classes, and objectness/confidence.
- Post-processing: filters predictions, applies NMS, formats results.

You do not need to implement these parts in this beginner course. You do need to know where errors can come from.

If small objects are missed, the issue may involve feature scale, input resolution, training data, or annotation quality. If classes are confused, the issue may be class definitions, label noise, or insufficient examples.

### Feature Map Intuition

The model does not judge every original pixel independently. It converts the image into smaller, more abstract feature maps. You can think of feature maps as clue maps: some respond to edges, some to texture, and some to shape combinations.

![Feature maps and multi-scale detection](../assets/feature_pyramid.svg)

Large objects can often be recognized on low-resolution, semantic features. Small objects need more fine detail. Multi-scale fusion connects those two needs:

```text
small objects need detail; large objects need semantics; multi-scale fusion joins them
```

### What the Detection Head Outputs

The detection head does not directly output a rendered image. It first creates many candidate detections. A useful mental model is:

```text
candidate box + class scores + object quality / confidence
```

![Detection head candidate outputs](../assets/detection_head_outputs.svg)

The model produces candidates across multiple feature scales. Post-processing turns them into human-readable detections:

1. Remove candidates below the confidence threshold.
2. Convert coordinates back to the original image scale.
3. Use NMS to remove duplicates.
4. Return final `class, confidence, box` results.

Different YOLO implementations compute object quality, class score, and box regression details differently. For this course, keep the abstraction: the model produces many candidates, then filters them.

### What Training Learns

Training is not simply memorizing images. The model repeatedly adjusts parameters so its predictions become closer to the labels. A training example contributes several kinds of error:

- Class error: the object category is wrong.
- Box error: the predicted box does not overlap the true box enough.
- Confidence error: the model is too confident where no object exists, or not confident enough where one does.

![YOLO loss components](../assets/loss_components.svg)

These errors become a training loss. A lower loss usually means the model fits the training data better, but it does not guarantee generalization. That is why validation metrics and error cases matter.

More mechanically, training repeats four steps:

1. Forward pass: the model predicts using current parameters.
2. Loss calculation: predictions are compared to labels.
3. Backpropagation: the optimizer computes useful parameter directions.
4. Parameter update: the next prediction should move closer to the labels.

Loss is not a mysterious grade. It is an optimizable expression of how far predictions are from labels. In detection, it usually cares about box quality, class prediction, and object confidence or quality.

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

### Do Not Over-Optimize the Version Question

YOLO is a family, not one fixed file. Implementations differ in layers, training recipes, export support, and naming. At the beginner stage, chasing the newest version is less important than mastering the workflow:

```text
define data -> label -> train -> validate -> analyze errors -> export -> deploy
```

Once that workflow is clear, switching implementations is a manageable engineering task rather than a restart.

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

Read the command in pieces:

- `--source data/samples`: where to read images from.
- `--model yolo11n.pt`: which pretrained weights to use.
- `--imgsz 320 --conf 0.25`: how large the input should be and how confident a detection must be to remain.

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

### Reading the Output Folder

A prediction run usually produces:

- rendered images with boxes, useful for human inspection
- labels or JSON, useful for downstream code
- logs, useful for model, image size, speed, and output path

Inspect in this order:

1. Confirm the command read the intended images.
2. Confirm the output folder was created.
3. Open 5-10 rendered predictions.
4. Only then decide whether to change `conf`, `imgsz`, or model size.

If the source path is wrong, the rest of the result is noise.

### A Small Parameter Experiment

Run the same images three ways:

```powershell
python scripts/predict_image.py --source data/samples --model yolo11n.pt --imgsz 320 --conf 0.15
python scripts/predict_image.py --source data/samples --model yolo11n.pt --imgsz 320 --conf 0.50
python scripts/predict_image.py --source data/samples --model yolo11n.pt --imgsz 640 --conf 0.25
```

Then compare:

- Did lower `conf` add false positives?
- Did higher `conf` miss objects?
- Did larger `imgsz` help small objects while slowing prediction?

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

![YOLO dataset folder structure](../assets/dataset_layout.svg)

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

### How Images and Labels Match

YOLO pairs images and labels by matching filenames:

```text
images/train/desk_001.jpg
labels/train/desk_001.txt
```

For an image with no target objects, an empty `.txt` file is often the clearest signal: this image was checked and intentionally has no boxes.

If a label filename is misspelled, the model cannot infer your intent. Many training problems are file relationship problems, not model problems.

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

### Annotation Boundary Details

A useful rule is: box the visible outer rectangle of the target, include as little background as possible, and do not cut off visible target pixels.

| Scene | Recommendation |
| --- | --- |
| Occluded object | Box the visible part unless your project defines otherwise |
| Shadow | Do not include the shadow |
| Transparent object | Box the visible contour and document the rule |
| Tiny object | Skip below your threshold, but be consistent |
| Cut-off object | Keep it if the real use case includes cut-off views |

Consistency matters more than making one individual image perfect. The model learns statistical patterns across the dataset.

### How Much Data Is Enough?

There is no universal number, but phases help:

| Phase | Image count | Goal |
| --- | --- | --- |
| Smoke dataset | 10-30 | Prove training can run and paths are correct |
| First dataset | 100-300 | See whether the model learns the basic pattern |
| Iteration dataset | 300-1000+ | Add difficult cases and improve generalization |

If you have many classes, each class needs enough examples. A first project with 2-3 clear classes is usually better than a first project with 20 vague classes.

### What Data Augmentation Does

Training often uses augmentations such as scaling, cropping, rotation, color jitter, and Mosaic.

![Data augmentation examples](../assets/augmentation_panel.svg)

Augmentation does not create truly new real-world evidence. It helps the model see reasonable variations:

- the same object farther or closer
- slightly tilted camera angles
- brighter or darker lighting
- partially cropped objects
- backgrounds not identical to the original images

Augmentation cannot replace real data. If the target scene is night surveillance and the dataset only contains daytime photos, brightness changes are usually not enough. Collect real night examples.

Do not make augmentation too extreme. Strong augmentation can create unnatural images and teach patterns that will not appear in deployment. Start with framework defaults, then adjust after error analysis.

### Dataset Versioning

Do not keep changing data without naming versions. Use a simple convention:

```text
dataset_v0_smoke
dataset_v1_initial
dataset_v2_more_low_light
dataset_v3_fixed_labels
```

Your model report should always say which dataset version it used.

### Pre-Training Dataset Checklist

Before training, check:

- `dataset.yaml` paths can be read by scripts.
- `names` covers every class id used by labels.
- Every image has the intended label file.
- Label coordinates are between 0 and 1.
- Train and validation sets do not contain accidental duplicates.
- Validation images resemble the target use case.
- There are no obvious missing labels or duplicate labels.

If data quality is unstable, longer training usually just learns the mistakes more confidently.

---

## Chapter 6: Training in the Cloud

Training adjusts model weights so predictions fit your dataset. Cloud training is recommended when local hardware is weak.

![Local-light and cloud-heavy workflow](../assets/local_cloud_workflow.svg)

### Google Colab Example

Google Colab entry point:

```text
https://colab.research.google.com/
```

Colab is a browser-based cloud Jupyter Notebook environment. It is useful for this course because your local machine only needs a browser while training runs on a cloud runtime. You can save notebooks in Google Drive and use a GPU when one is available.

Important boundaries:

- Colab requires a Google Account.
- Free compute is not guaranteed or unlimited.
- GPU/TPU availability and type can change.
- Idle notebooks can disconnect, and runtimes can be recycled.
- Files under `/content` belong to the current runtime and may disappear.
- Save important notebooks, datasets, and outputs to Google Drive or GitHub.

#### Account and Registration Notes

If you can sign in to Gmail, Google Drive, or YouTube, you usually already have a Google Account that can be used with Colab.

If not, create one from:

```text
https://accounts.google.com/signup
```

Use a personal account if a school or company account blocks Colab, Drive mounting, or external sharing. Add recovery information so you do not lose access to training files. Do not use multiple accounts to bypass Colab usage limits, and do not upload sensitive images unless you understand the privacy and compliance requirements.

#### Create a Training Notebook

1. Open `https://colab.research.google.com/` and sign in.
2. Create a new notebook.
3. Rename it, for example `yolo_lab04_training.ipynb`.
4. Choose `Runtime -> Change runtime type`.
5. Set `Hardware accelerator` to `GPU`.
6. Run a quick hardware check:

```python
!nvidia-smi

import torch
print("cuda available:", torch.cuda.is_available())
print("device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")
```

If `nvidia-smi` fails, GPU was not attached or is temporarily unavailable. You can do a tiny CPU smoke test, but real training should wait for GPU or move to another cloud option.

#### Install Ultralytics

Colab runtimes are temporary, so keep dependency installation as the first notebook cell:

```python
!pip -q install ultralytics

from ultralytics import YOLO
```

Then verify:

```python
import ultralytics
ultralytics.checks()
```

#### Prepare Data with Drive and Zip Files

For many small files, do not train directly from Google Drive. A more stable pattern is:

1. Zip the dataset locally as `dataset_v1.zip`.
2. Upload it to Drive, for example:

```text
MyDrive/yolo_learning/dataset_v1.zip
```

3. Mount Drive:

```python
from google.colab import drive
drive.mount("/content/drive")
```

4. Copy and unzip into the local runtime:

```python
!mkdir -p /content/yolo_learning
!cp "/content/drive/MyDrive/yolo_learning/dataset_v1.zip" /content/yolo_learning/
!unzip -q /content/yolo_learning/dataset_v1.zip -d /content/yolo_learning/dataset_v1
```

5. Check the dataset YAML:

```python
from pathlib import Path

data_yaml = Path("/content/yolo_learning/dataset_v1/dataset.yaml")
print(data_yaml.exists(), data_yaml)
```

If this prints `False`, inspect the extracted tree before training.

#### Colab Smoke Run

Run a short training job first:

```python
model = YOLO("yolo11n.pt")
model.train(
    data=str(data_yaml),
    epochs=3,
    imgsz=320,
    batch=4,
    project="/content/yolo_runs",
    name="smoke_v1",
)
```

Fix path, label, class id, dependency, or GPU problems here before spending time on a full run.

#### Full Training Run

After the smoke run passes:

```python
model = YOLO("yolo11n.pt")
model.train(
    data=str(data_yaml),
    epochs=50,
    imgsz=640,
    batch=8,
    project="/content/yolo_runs",
    name="custom_yolo_v1",
)
```

If you hit GPU memory errors, lower `batch`, then lower `imgsz`, and stay with nano weights.

#### Save Results Back to Drive

Copy outputs immediately after training:

```python
!mkdir -p "/content/drive/MyDrive/yolo_learning/runs"
!cp -r /content/yolo_runs/custom_yolo_v1 "/content/drive/MyDrive/yolo_learning/runs/"
```

Confirm that Drive contains:

- `weights/best.pt`
- `weights/last.pt`
- `results.csv`
- `args.yaml`
- training plots or prediction examples

Your experiment log should include platform, notebook name, dataset zip path, `dataset.yaml` path, model, epochs, image size, batch size, and output path.

#### Colab Troubleshooting

| Problem | Likely cause | Fix |
| --- | --- | --- |
| No GPU | runtime not set or free GPU unavailable | set GPU runtime, wait, or use Kaggle/paid cloud GPU |
| Training interrupted | idle timeout, network, runtime recycling | save to Drive often and copy outputs immediately |
| Drive reads slowly | many small files read from Drive | copy a zip to `/content` and unzip locally |
| `No such file` | extracted tree differs from `dataset.yaml` | inspect with `find` and fix paths |
| CUDA out of memory | batch/imgsz too large | reduce `batch`, then `imgsz` |
| Metrics look wrong | labels or class definitions are bad | return to dataset audit |

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

### Cloud Training Package

Prepare cloud work as a small package:

```text
cloud_train_package/
  dataset/
    images/
    labels/
    dataset.yaml
  train_notebook.ipynb
  requirements.txt
  README_cloud.md
```

`README_cloud.md` should say:

- dataset version
- entry notebook
- expected training time
- output directory
- files to download after training

Cloud runtimes can reset. A clear package lets you recover quickly.

### Important Training Parameters

| Parameter | Effect |
| --- | --- |
| `epochs` | how many times the model sees the training set |
| `imgsz` | input resolution; larger may help small objects but costs compute |
| `batch` | images per training step; too high can exceed memory |
| `model` | starting weights and model size |
| `patience` | early stopping patience in some training configs |

### Reading Training Logs

During training, do not only wait for `best.pt`. Watch:

- whether loss generally decreases
- whether validation metrics stay flat
- whether precision and recall are badly imbalanced
- whether GPU memory is near the limit
- whether each epoch takes unusually long

If training loss decreases but validation metrics do not improve, possible causes include overfitting, a tiny validation set, inconsistent labels, or train/validation distribution mismatch.

### Underfitting and Overfitting

Underfitting means the model cannot even learn the training set well. Common causes are too few epochs, too small a model, too low an image size, or noisy labels.

Overfitting means the model looks good on training data but fails on validation or real data. Common causes are too little data, narrow scenes, too much training, or a validation set that exposes different conditions.

| Symptom | Possible issue | Next step |
| --- | --- | --- |
| Train poor, validation poor | underfitting or data errors | inspect labels, train longer, try a slightly larger model |
| Train good, validation poor | overfitting or domain shift | add diverse data, analyze errors |
| Both good, real scene poor | target scene mismatch | collect real-scene data |

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

![Error analysis matrix](../assets/error_analysis_matrix.svg)

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

### TP, FP, and FN

Detection evaluation checks both category and location.

- True positive: the model predicted an object with the right class and enough box overlap.
- False positive: the model predicted an object where no matching true object exists.
- False negative: a real object was missed.

Precision is sensitive to false positives. Recall is sensitive to false negatives. Lowering the confidence threshold often improves recall but may hurt precision; raising it often does the opposite.

### Precision-Recall Curve and AP

The same model produces different precision and recall values at different confidence thresholds. Connecting those points gives the precision-recall curve.

![Precision-recall curve](../assets/precision_recall_curve.svg)

With a high confidence threshold, the model keeps only its strongest detections. Precision often rises, but recall may fall.

With a low confidence threshold, the model keeps more candidates. Recall may rise, but false positives can increase and precision may fall.

AP is roughly the area under the precision-recall curve. A curve closer to the top-right is better. mAP averages AP across classes.

In real projects, do not chase only one mAP number. Inspect per-class curves and error cases. A class can have a decent overall score while still failing in a critical scene.

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

### How Detailed Should Error Analysis Be?

After a training run, choose at least 20 failed images and write a table:

| image | error_type | observed | likely_reason | next_action |
| --- | --- | --- | --- | --- |
| val_003.jpg | false negative | low-light cup missed | not enough low-light cups | collect low-light cup images |
| val_014.jpg | false positive | reflection detected as phone | missing hard negatives | add reflective desk negatives |
| val_021.jpg | bad box | box includes too much background | loose labels | revise label rules and audit |

The purpose is to turn "the model is bad" into an actionable data task.

### Do Not Worship One Score

`mAP50-95` is useful, but project success also depends on:

- whether critical classes work
- whether high-risk errors are acceptable
- whether inference speed is usable
- whether deployment is stable
- whether failures can be improved with the next data round

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

### Inference Is More Than a Model File

Deployment includes pre-processing and post-processing:

```text
read image -> resize/letterbox -> model inference -> parse output -> NMS -> restore coordinates -> draw boxes or return JSON
```

If you export to ONNX or another runtime, confirm that coordinates map back to the original image, class order is unchanged, and NMS behavior is understood.

### Deployment Acceptance Checklist

Before calling a deployment done, check:

- the same test image gives similar results locally and in deployment
- class names display correctly
- large images, small images, empty images, and wrong formats receive reasonable responses
- inference time is acceptable
- model version and dataset version are recorded
- image privacy and storage behavior are documented

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

### Reproducible Experiment Notes

Weak note:

```text
Trained today. Looks okay.
```

Useful note:

```text
run_id: 2026-05-22-cup-phone-v2-yolo11n
dataset: dataset_v2_more_low_light
base_model: yolo11n.pt
command: python scripts/train_custom.py --data data/yolo_dataset/dataset.yaml --model yolo11n.pt --epochs 50 --imgsz 640
result: best.pt, mAP50=0.82, recall=0.74
main_errors: low-light cups missed, phone reflections false positive
next_step: add 60 low-light cup images and 30 reflective-desk hard negatives
```

This is the difference between a memory and an experiment.

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

### Final Project Rubric

Use this table to self-check:

| Area | Passing | Strong |
| --- | --- | --- |
| Problem | classes and scene are clear | intended and out-of-scope use are explicit |
| Data | train/val/test and label rules exist | data card, versions, and bias notes exist |
| Training | experiment command is reproducible | smoke run, full run, and comparison run are documented |
| Evaluation | metrics and prediction images exist | error buckets and next data plan exist |
| Deployment | demo or export runs | acceptance checks, speed, and privacy are documented |
| Documentation | README runs the basic flow | a new reader can reproduce the experiment |

The final project is not proof that the model is perfect. It is proof that you can turn a vision problem into a reproducible engineering project.

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

## Appendix D: Study Questions

After each chapter, use these questions to check yourself.

Chapter 1:

- Does your task really need detection, or would classification be enough?
- Can every class be identified visually?
- Which work belongs locally, and which work belongs in the cloud?

Chapter 2:

- Can you convert a pixel box into a YOLO label by hand?
- What do `conf` and NMS `iou` control?
- Why can a high-confidence prediction still be a bad box?

Chapter 3:

- What do backbone, neck, and head each do?
- Why do small objects depend on higher-resolution detail?
- Why do pretrained weights help small custom datasets?

Chapter 5:

- Do images and labels match one-to-one?
- Are annotation rules written down and consistent?
- Does the validation set resemble the target use case?

Chapter 7:

- What is the model's biggest error bucket?
- Should the next iteration collect data, fix labels, tune thresholds, or change deployment?
- If the score improved, can you explain why?

---

## Appendix E: References

- Ultralytics Python Usage: https://docs.ultralytics.com/usage/python
- Ultralytics Object Detection Dataset Format: https://docs.ultralytics.com/datasets/detect
- Ultralytics CLI Usage: https://docs.ultralytics.com/usage/cli
- Google Colab: https://colab.research.google.com/
- Google Colab FAQ: https://research.google.com/colaboratory/faq.html
- Create a Google Account: https://support.google.com/accounts/answer/27441
- Ultralytics Google Colab Integration: https://docs.ultralytics.com/integrations/google-colab/
- Original YOLO paper: https://arxiv.org/abs/1506.02640
- Lab-based course design pattern: reading, lab handout, grading command, and hand-in artifact
