# Lab 05: Validation, Error Analysis, and Dataset Iteration

## Goal

Move from "I trained a model" to "I know what my model gets wrong and what data it needs next."

## Background

Validation metrics are useful, but they are not a substitute for looking at mistakes. Good detection projects improve through error buckets: false positives, false negatives, class confusion, box quality, small objects, occlusion, and domain shift.

## Tasks

1. Run validation on the model from Lab 04.
2. Predict on 20-50 images not used for training.
3. Collect at least 20 error cases.
4. Categorize each error.
5. Decide the next dataset change.
6. Fill in `submissions/lab05/error_analysis.md`.
7. Record time spent in `submissions/lab05/time.txt`.

## Hints

- Do not tune ten knobs at once.
- If errors cluster around one scene type, collect more of that scene.
- If class confusion is frequent, your class definitions may be too subtle.

## Grade

```powershell
python tools/course.py grade lab05
```

## Submit

```powershell
python tools/course.py handin lab05
```

