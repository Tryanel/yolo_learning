# Course Schedule

This course follows a lab-first style: each week has a reading target, a concrete lab, a grading command, and a small hand-in artifact. The habit is simple: learn by making a real system behave.

Primary Chinese reading: [docs/textbook/yolo_model_textbook_zh.md](../docs/textbook/yolo_model_textbook_zh.md)  
English reference: [docs/textbook/yolo_model_textbook.md](../docs/textbook/yolo_model_textbook.md)

| Week | Reading | Lab | Main Artifact |
| --- | --- | --- | --- |
| 1 | Textbook Ch. 0-1 | `lab00` Local environment | `submissions/lab00/environment.md` |
| 2 | Textbook Ch. 2-3 | `lab01` Boxes, IoU, NMS | `submissions/lab01/iou_exercises.md` |
| 3 | Textbook Ch. 4 | `lab02` Pretrained prediction | `submissions/lab02/predict_report.md` |
| 4 | Textbook Ch. 5 | `lab03` Dataset construction | `data/yolo_dataset/dataset.yaml` |
| 5 | Textbook Ch. 6 | `lab04` Cloud training | `submissions/lab04/cloud_training_log.md` |
| 6 | Textbook Ch. 7 | `lab05` Evaluation and error analysis | `submissions/lab05/error_analysis.md` |
| 7 | Textbook Ch. 8 | `lab06` Export and lightweight inference | `submissions/lab06/export_report.md` |
| 8 | Textbook Ch. 9 | `lab07` Hosted demo | `submissions/lab07/deployment_report.md` |
| 9 | Textbook Ch. 10 | `lab08` Final project | `submissions/lab08/final_project.md` |

## Weekly Rhythm

1. Read the assigned textbook chapter.
2. Open the lab README under `labs/labXX/`.
3. Work in the matching `submissions/labXX/` folder.
4. Run `python tools/course.py grade labXX`.
5. When satisfied, run `python tools/course.py handin labXX`.

The grader is intentionally lightweight. It checks structure, required files, and obvious placeholders. It does not judge whether your model is good; your error analysis and final project write-up do that.
