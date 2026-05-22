# Lab 07: Hosted Demo and Deployment Tradeoffs

## Goal

Turn your model into a small demo that another person can try, or write a concrete deployment plan if hosting is blocked.

## Background

For weak local machines, hosted demos are often the easiest path. Hugging Face Spaces, Roboflow Hosted API, or a notebook-based demo can show the model without asking your laptop to be a server.

## Tasks

1. Choose a deployment route: Hugging Face Spaces, Roboflow, Colab demo, or local script.
2. Build the smallest demo that accepts an image and returns a detection result.
3. Record setup steps, limitations, costs, and licensing concerns.
4. Fill in `submissions/lab07/deployment_report.md`.
5. Record time spent in `submissions/lab07/time.txt`.

## Hints

- A URL is nice but not mandatory if hosting is blocked.
- If you cannot host, write a runbook that someone else could follow.
- Include a privacy note if images might contain people or sensitive scenes.

## Grade

```powershell
python tools/course.py grade lab07
```

## Submit

```powershell
python tools/course.py handin lab07
```

