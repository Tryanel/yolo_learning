# Week 07 - 部署与 Demo

## 本周目标

把训练出的模型用在一个小 demo 中，理解模型导出和推理速度。

## 推荐命令

导出 ONNX：

```powershell
python scripts/export_model.py --model outputs/train/exp/weights/best.pt --format onnx
```

实时摄像头预测：

```powershell
python scripts/predict_video.py --source 0 --model outputs/train/exp/weights/best.pt
```

## 必做任务

1. 至少完成一种 demo：图片批量预测、视频预测或摄像头预测。
2. 记录 CPU/GPU 推理速度差异。
3. 尝试导出 ONNX。
4. 写下部署时最容易踩坑的 3 个问题。

## 检查点

你能解释：

- 训练和推理有什么区别？
- 为什么模型越大通常越慢？
- 为什么导出格式会影响部署环境？

