# Glossary

## YOLO

You Only Look Once，一类实时目标检测模型。它一次看完整张图，直接预测目标类别和位置框。

## Object Detection

目标检测。任务是判断图片里有哪些目标，以及每个目标在哪里。

## Bounding Box

目标框。通常用矩形框表示目标位置。

## Class

类别。例如 `person`、`car`、`cup`。

## Confidence

置信度。模型认为某个检测结果可信的程度。

## IoU

Intersection over Union，交并比。衡量预测框和真实框重合程度。

## Precision

查准率。检测出来的结果里，有多少是真的。

## Recall

查全率。真实存在的目标里，有多少被检测出来。

## mAP

mean Average Precision，目标检测常用综合指标。常见写法包括 `mAP50` 和 `mAP50-95`。

## Epoch

训练轮数。模型完整看过训练集一次叫一个 epoch。

## Batch Size

每次送进模型训练的一批图片数量。太大可能显存不够，太小训练会慢或不稳定。

## Image Size

训练或预测时输入模型的图片尺寸，常见值是 640。

## Overfitting

过拟合。模型在训练集表现很好，但在新图片或验证集表现差。

