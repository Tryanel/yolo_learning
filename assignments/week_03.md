# Week 03 Assignment - 预训练预测实验

## 作业目标

用预训练 YOLO 模型完成一次可复现的预测实验。

## 任务

1. 放 5 张测试图片到 `data/samples/`。
2. 分别运行：

```powershell
python scripts/predict_image.py --source data/samples --conf 0.25
python scripts/predict_image.py --source data/samples --conf 0.50
```

3. 比较两次输出。
4. 记录至少 3 个模型错误案例。

## 通过标准

- `outputs/predict/` 里有预测结果。
- 能解释 `conf` 变化带来的影响。
- 有一份实验记录。

