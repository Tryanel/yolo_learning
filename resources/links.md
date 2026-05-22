# Resources

这些链接作为学习入口。工具和版本会变化，真正使用时以官方文档为准。

## YOLO / Ultralytics

- Ultralytics Docs: https://docs.ultralytics.com/
- Quickstart: https://docs.ultralytics.com/quickstart/
- Python Usage: https://docs.ultralytics.com/usage/python/
- Train Mode: https://docs.ultralytics.com/modes/train/
- Predict Mode: https://docs.ultralytics.com/modes/predict/
- Object Detection Datasets: https://docs.ultralytics.com/datasets/detect/
- Command Line Interface: https://docs.ultralytics.com/usage/cli/

## Course Design References

- MIT 6.S081 schedule: https://pdos.csail.mit.edu/6.S081/2020/schedule.html
- MIT 6.S081 sample lab hand-in convention: https://pdos.csail.mit.edu/6.S081/2020/labs/util.html

## Papers

- YOLO original paper: https://arxiv.org/abs/1506.02640

## 数据标注

- Roboflow Annotate: https://docs.roboflow.com/annotate/annotation-tools
- CVAT: https://www.cvat.ai/
- Label Studio: https://labelstud.io/

## 基础概念

- Object Detection Overview: https://en.wikipedia.org/wiki/Object_detection
- Intersection over Union: https://en.wikipedia.org/wiki/Jaccard_index

## 实践建议

- 先用官方预训练权重跑通预测。
- 自定义训练前，先用很小的数据集跑 1-2 个 epoch 检查数据格式。
- 每次改进只改一个主要因素：数据、标注、模型大小、训练轮数、图片尺寸。
