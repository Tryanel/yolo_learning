# Week 07 Assignment - Demo 与导出

## 作业目标

把模型从训练结果变成可以演示的东西。

## 任务

1. 选择一种 demo：

- 图片批量预测
- 视频预测
- 摄像头实时预测

2. 导出 ONNX：

```powershell
python scripts/export_model.py --model outputs/train/exp/weights/best.pt --format onnx
```

3. 记录推理速度。
4. 写下部署问题清单。

## 通过标准

- 有一个可运行 demo。
- 至少成功导出一种格式，或记录了导出失败原因。
- 能解释训练和推理的区别。

