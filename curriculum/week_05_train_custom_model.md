# Week 05 - 训练第一个自定义模型

## 本周目标

用自己的数据微调一个 YOLO 模型，并得到 `best.pt`。

## 推荐命令

```powershell
python scripts/train_custom.py --data data/yolo_dataset/dataset.yaml --model yolo11n.pt --epochs 50 --imgsz 640
```

训练完成后，权重通常在：

```text
outputs/train/<run_name>/weights/best.pt
```

## 必做任务

1. 跑通一次 10-20 epoch 的短训练，确认流程没问题。
2. 再跑一次 50 epoch 训练。
3. 保存训练结果图和 `best.pt` 路径。
4. 用自己的模型跑 10 张新图片。

## 检查点

你能解释：

- 为什么从预训练模型开始，而不是从零训练？
- `epochs`、`batch`、`imgsz` 大概影响什么？
- 为什么训练集效果好，验证集效果差，可能说明过拟合？

