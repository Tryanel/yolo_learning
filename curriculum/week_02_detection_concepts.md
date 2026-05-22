# Week 02 - 目标检测核心概念

## 本周目标

理解 YOLO 结果图里的每个元素：框、类别、置信度，以及为什么有些物体会漏检或误检。

## 核心概念

- Classification：只判断整张图是什么。
- Object Detection：判断图里有什么，以及在哪里。
- Bounding box：包住目标的矩形框。
- Class：目标类别。
- Confidence：模型对检测结果的信心。
- IoU：两个框的重叠程度。
- Precision：检测出来的结果有多少是真的。
- Recall：真实目标有多少被检测出来。
- mAP：综合评价检测模型效果的指标。

## 必做任务

1. 找 5 张图，手动画出你认为合理的目标框。
2. 对每张图写出可能的难点：小目标、遮挡、反光、背景相似、角度特殊。
3. 读 [resources/glossary.md](../resources/glossary.md)。
4. 完成 [assignments/week_02.md](../assignments/week_02.md)。

## 检查点

你能解释：

- 为什么 confidence 高不一定代表框很准？
- 为什么只看 accuracy 不适合目标检测？
- 漏检和误检分别应该怎么分析？

