# Teaching Model

This repository is designed as a lab course, not a loose collection of notes.

It borrows the useful habits of rigorous lab-based systems courses:

- A schedule that pairs reading with a lab.
- A lab README with goals, background, tasks, hints, grading, and submission.
- A student submission folder for each lab.
- A lightweight grading command.
- A hand-in command that packages only the relevant artifacts.
- A course textbook that explains the concepts in the same order as the labs.

## What This Course Teaches

This course asks you to build a small computer vision system. The learning posture is practical: run real commands, inspect outputs, write down failures, and make each lab reproducible.

## Course Commands

```powershell
python tools/course.py list
python tools/course.py show lab00
python tools/course.py grade lab00
python tools/course.py status
python tools/course.py handin lab00
```

If `make` is available:

```powershell
make list
make grade LAB=lab00
make handin LAB=lab00
```

## Grader Philosophy

The grader checks structure, completeness, and obvious placeholders. It is intentionally not a full model-quality judge. A high-quality YOLO project still requires human review of dataset definitions, error cases, and deployment constraints.

## Instructor Notes

For a classroom:

- Release one lab at a time.
- Require `time.txt` to keep workload honest.
- Ask students to demo failure cases, not only success cases.
- Use Lab 08 as a portfolio artifact.
