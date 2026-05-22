# Data Folder

这里放学习用数据。大型数据、训练权重和生成输出默认不会提交到 Git。

## 推荐结构

```text
data/
  samples/          # 第 3 周预测用样例图片/视频
  raw/              # 原始未整理数据
  yolo_dataset/     # 自定义 YOLO 数据集
```

## YOLO 数据集结构

```text
data/yolo_dataset/
  images/
    train/
    val/
    test/
  labels/
    train/
    val/
    test/
  dataset.yaml
```

## 标签格式

每张图片对应一个同名 `.txt` 文件。每行一个目标：

```text
class_id x_center y_center width height
```

所有坐标都是归一化比例，范围应在 0 到 1。

