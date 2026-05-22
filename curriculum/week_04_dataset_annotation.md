# Week 04 - 数据集与标注

## 本周目标

做出一个最小可训练的 YOLO 格式数据集。

## 数据集结构

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

每张图片对应一个同名 `.txt` 标注文件。YOLO 检测标注格式：

```text
class_id x_center y_center width height
```

其中坐标都是 0 到 1 之间的归一化比例。

## 必做任务

1. 选择 1-3 个类别。
2. 收集至少 50 张图片，越接近真实使用场景越好。
3. 使用 Roboflow、CVAT、Label Studio 或其他工具画框。
4. 导出 YOLO 格式数据集。
5. 运行 `python scripts/inspect_dataset.py --data data/yolo_dataset/dataset.yaml`。

## 检查点

你能解释：

- 为什么训练集和验证集要分开？
- 为什么标注框太松或太紧都会影响模型？
- 为什么同一个类别需要不同角度、背景、光照的图片？

