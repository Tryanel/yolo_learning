# Week 03 - 用预训练 YOLO 做预测

## 本周目标

用现成权重检测图片、视频或摄像头画面，并看懂输出结果。

## 推荐命令

检测图片：

```powershell
python scripts/predict_image.py --source data/samples/demo.jpg --model yolo11n.pt
```

检测视频：

```powershell
python scripts/predict_video.py --source data/samples/demo.mp4 --model yolo11n.pt
```

调整置信度阈值：

```powershell
python scripts/predict_image.py --source data/samples/demo.jpg --conf 0.5
```

## 必做任务

1. 准备 5 张不同场景的图片。
2. 分别用 `conf=0.25`、`conf=0.5` 跑预测。
3. 记录哪些目标漏掉了，哪些目标误检了。
4. 把最有代表性的结果写入实验记录。

## 检查点

你能解释：

- `conf` 调高以后会发生什么？
- `imgsz` 变大可能带来什么影响？
- 为什么 nano 模型快但可能不够准？

