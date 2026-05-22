# Lab 04: Cloud Training and Experiment Logging

## Goal

Train your first custom model in the cloud and keep a reproducible experiment log.

## Background

Training is the first compute-heavy lab. If your local machine is weak, use Google Colab, Ultralytics Cloud Training, Kaggle, or another GPU-backed notebook. The important artifact is not only `best.pt`; it is the record of exactly what produced it.

![Local-light and cloud-heavy workflow](../../docs/assets/local_cloud_workflow.svg)

For the default path, use Google Colab:

```text
https://colab.research.google.com/
```

Read Chapter 6 of the textbook before starting. It includes account setup notes, GPU runtime setup, Drive mounting, zip-based dataset upload, smoke training, full training, and result backup.

## Tasks

1. Create or open a Google Colab notebook.
2. Switch runtime hardware accelerator to GPU and run `!nvidia-smi`.
3. Install Ultralytics in the notebook.
4. Mount Google Drive.
5. Copy your zipped dataset from Drive to `/content` and unzip it locally.
6. Run a short smoke training run of 3-5 epochs.
7. Fix dataset errors if the smoke run fails.
8. Run a real training attempt.
9. Copy the full training output back to Google Drive.
10. Record model name, epochs, image size, batch size, metrics, notebook name, dataset path, and output path.
11. Fill in `submissions/lab04/cloud_training_log.md`.
12. Record time spent in `submissions/lab04/time.txt`.

## Hints

- Start with nano weights.
- Save a copy of `best.pt` outside the temporary notebook runtime.
- A failed training run is useful if you document the exact failure.
- If Drive is slow, train from files copied into `/content`, not directly from thousands of Drive files.
- If Colab cannot allocate GPU, record the blocker and either wait, use CPU for a smoke run, or switch to another cloud GPU.

## Grade

```powershell
python tools/course.py grade lab04
```

## Submit

```powershell
python tools/course.py handin lab04
```
