# Week 04 Assignment - 制作最小数据集

## 作业目标

完成一个能被 YOLO 训练脚本读取的数据集。

## 任务

1. 选择 1-3 个类别。
2. 收集至少 50 张图片。
3. 完成标注并导出 YOLO 格式。
4. 把文件放到 `data/yolo_dataset/`。
5. 复制 `data/dataset.yaml.example` 为 `data/yolo_dataset/dataset.yaml` 并修改类别名。
6. 运行：

```powershell
python scripts/inspect_dataset.py --data data/yolo_dataset/dataset.yaml
```

## 通过标准

- 图片和标签数量大致匹配。
- `dataset.yaml` 能被脚本读取。
- 没有明显越界或格式错误标签。

