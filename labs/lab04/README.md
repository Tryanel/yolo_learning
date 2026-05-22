# Lab 04: Cloud Training and Experiment Logging

## Goal

Train your first custom model in the cloud and keep a reproducible experiment log.

## Background

Training is the first compute-heavy lab. If your local machine is weak, use Google Colab, Ultralytics Cloud Training, Kaggle, or another GPU-backed notebook. The important artifact is not only `best.pt`; it is the record of exactly what produced it.

## Tasks

1. Upload or mount your dataset in a cloud notebook.
2. Install Ultralytics in the notebook.
3. Run a short smoke training run of 5-10 epochs.
4. Fix dataset errors if the smoke run fails.
5. Run a real training attempt.
6. Record model name, epochs, image size, batch size, metrics, and output path.
7. Fill in `submissions/lab04/cloud_training_log.md`.
8. Record time spent in `submissions/lab04/time.txt`.

## Hints

- Start with nano weights.
- Save a copy of `best.pt` outside the temporary notebook runtime.
- A failed training run is useful if you document the exact failure.

## Grade

```powershell
python tools/course.py grade lab04
```

## Submit

```powershell
python tools/course.py handin lab04
```

