# Week 06 - 评估与改进

## 本周目标

不只看分数，还要知道模型错在哪里，并做一次有根据的改进。

## 推荐命令

```powershell
python scripts/evaluate_model.py --model outputs/train/exp/weights/best.pt --data data/yolo_dataset/dataset.yaml
```

## 错误类型

- 漏检：真实目标没有被框出来。
- 误检：背景或其他物体被当成目标。
- 框不准：目标被检测到了，但框的位置不好。
- 类别错：A 类被识别成 B 类。
- 重复框：同一个物体被框了多次。

## 必做任务

1. 收集至少 20 个错误案例。
2. 把错误案例写到 [notes/error_cases.md](../notes/error_cases.md)。
3. 判断主要问题是数据、标注、模型大小还是训练配置。
4. 做一次改进并重新训练。
5. 对比改进前后的结果。

## 检查点

你能解释：

- 为什么加数据比盲目调参更常见也更有效？
- 什么样的错误说明类别定义不清楚？
- 如何判断是否需要更大的模型？

