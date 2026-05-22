# Week 05 Assignment - 第一次训练

## 作业目标

训练出自己的第一个 YOLO 权重文件。

## 任务

1. 先短训：

```powershell
python scripts/train_custom.py --data data/yolo_dataset/dataset.yaml --epochs 10
```

2. 确认没有数据路径和标签错误。
3. 再训练 50 epoch：

```powershell
python scripts/train_custom.py --data data/yolo_dataset/dataset.yaml --epochs 50
```

4. 用 `best.pt` 对新图片做预测。
5. 记录训练结果路径和关键指标。

## 通过标准

- 得到 `best.pt`。
- 能用 `best.pt` 做预测。
- 能解释训练集和验证集的作用。

