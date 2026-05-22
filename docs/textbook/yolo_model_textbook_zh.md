# YOLO 模型教材

版本日期：2026-05-22

这是 YOLO Learning Lab 的中文教材。它面向没有模型经验的学习者，默认你本地电脑配置一般，因此课程采用 **本地轻量学习 + 云端训练/部署** 的路线：本地负责写代码、整理数据、记录实验；云端负责训练、批量评估和在线演示。

英文版教材保留在 [yolo_model_textbook.md](yolo_model_textbook.md)。两份教材内容目标一致，但中文版会更贴近本课程的中文 lab 说明。

## 目录

- 第 0 章：如何使用这本教材
- 第 1 章：计算机视觉与目标检测
- 第 2 章：检测框、IoU 与 NMS
- 第 3 章：YOLO 模型到底在做什么
- 第 4 章：运行预训练模型预测
- 第 5 章：构建 YOLO 数据集
- 第 6 章：云端训练
- 第 7 章：验证、指标与错误分析
- 第 8 章：导出与部署
- 第 9 章：工程化一个 YOLO 项目
- 第 10 章：最终项目要求
- 附录 A：常用公式
- 附录 B：命令速查
- 附录 C：术语表
- 附录 D：参考资料

---

## 第 0 章：如何使用这本教材

学习 YOLO 最容易踩的坑，是一上来就问“模型结构是什么”“论文怎么读”“怎么调参”。这些当然重要，但对初学者来说，更可靠的路线是先把 YOLO 当成一个完整系统：

```text
图片 -> 标注 -> 数据集配置 -> 模型训练 -> 预测结果 -> 指标 -> 错误案例 -> 数据改进 -> 部署
```

这本教材按这个顺序展开。每一章都对应一个或多个实验：

| 教材章节 | 对应实验 | 主要能力 |
| --- | --- | --- |
| 第 1 章 | `lab00` | 搭建本地环境和课程工具 |
| 第 2 章 | `lab01` | 理解检测框、IoU、NMS |
| 第 3-4 章 | `lab02` | 用预训练模型做预测 |
| 第 5 章 | `lab03` | 构建和检查 YOLO 数据集 |
| 第 6 章 | `lab04` | 在云端训练自定义模型 |
| 第 7 章 | `lab05` | 验证模型并分析错误 |
| 第 8 章 | `lab06`、`lab07` | 导出、推理和部署 |
| 第 9-10 章 | `lab08` | 完成最终项目 |

### 这门课的学习方式

它更像实验课，而不是视频课。每个 lab 都要求你：

1. 阅读教材。
2. 打开 `labs/labXX/README.md`。
3. 完成 `submissions/labXX/` 里的提交模板。
4. 运行 `python tools/course.py grade labXX`。
5. 修改直到通过。
6. 运行 `python tools/course.py handin labXX` 打包。

轻量 grader 不会判断你的模型是否“真的好”，它只检查结构、必填项和明显占位符。真正的质量判断来自你的错误分析和复盘。

### 最重要的习惯

记录证据。

每次运行实验，都记录：

- 运行了什么命令
- 输入文件在哪里
- 输出文件在哪里
- 报错是什么
- 指标是多少
- 哪些图片失败了
- 下一步要改什么

这就是从“我试了一下”变成“我做了一个可复现实验”的分界线。

---

## 第 1 章：计算机视觉与目标检测

计算机视觉的目标，是让程序从图像或视频中提取结构化信息。常见任务包括：

| 任务 | 问题 | 输出 |
| --- | --- | --- |
| 图像分类 | 这张图主要是什么？ | 一个或多个类别 |
| 目标检测 | 图里有哪些物体，它们在哪里？ | 检测框、类别、置信度 |
| 实例分割 | 每个物体具体占哪些像素？ | 每个实例的 mask |
| 语义分割 | 每个像素属于哪个类别？ | 像素级类别图 |
| 姿态估计 | 人体或物体关键点在哪里？ | 点和骨架 |

YOLO 最常用于 **目标检测**。目标检测比分类更难，因为它同时要解决两个问题：

- 分类：这个物体是什么？
- 定位：这个物体在哪里？

一张图里可能有多个物体，所以检测模型还要处理“有几个”“每个在哪里”“是否重复框出同一个物体”等问题。

### 什么适合作为检测类别

好的初学者类别应该满足：

- 视觉边界清楚
- 容易用矩形框标注
- 类别之间差异明显
- 样本容易收集
- 真实使用场景明确

例如：

- 手机
- 杯子
- 鼠标
- 安全帽
- 车辆
- 某种水果

不适合初学者的类别通常有：

- 概念太抽象，如“危险物品”
- 需要上下文判断，如“有用的工具”
- 目标太小
- 边界模糊
- 类别差别只体现在文字或极细纹理上

### 本地轻量 + 云端训练

如果你的本地电脑配置不强，不要强行本地训练。合理分工是：

| 环节 | 推荐位置 |
| --- | --- |
| 写代码 | 本地 |
| 写笔记 | 本地 |
| 数据整理 | 本地 |
| 少量图片预测 | 本地或 Colab |
| 模型训练 | Colab / Kaggle / 云 GPU |
| 批量验证 | 云端 |
| 在线 demo | Hugging Face Spaces / Roboflow / 云端 |

学习 YOLO 的重点不是让本地电脑跑满，而是理解完整流程。

---

## 第 2 章：检测框、IoU 与 NMS

目标检测模型输出的是一组矩形框。每个框通常包含：

- 类别 class
- 位置 box
- 置信度 confidence

### 检测框格式

常见框格式有两种：

| 格式 | 含义 |
| --- | --- |
| `xyxy` | 左上角 x、左上角 y、右下角 x、右下角 y |
| `xywh` | 中心点 x、中心点 y、宽度、高度 |

YOLO 标签文件使用的是归一化后的 `xywh`：

```text
class_id x_center y_center width height
```

例子：

```text
0 0.500 0.420 0.200 0.300
```

意思是：

- 类别 id 是 `0`
- 框中心在图片宽度 50% 处
- 框中心在图片高度 42% 处
- 框宽度是图片宽度的 20%
- 框高度是图片高度的 30%

归一化的好处是标签不依赖具体图片尺寸。

### IoU：交并比

IoU 全称是 Intersection over Union，中文常叫交并比。

公式：

```text
IoU = 两个框的交集面积 / 两个框的并集面积
```

如果两个框完全不重叠，IoU = 0。  
如果两个框完全一致，IoU = 1。

IoU 用在三个地方：

- 判断预测框是否匹配真实框
- 衡量框的位置质量
- 在 NMS 中去掉重复框

### 置信度 confidence

置信度是模型对一个检测结果的信心。注意：

> 高置信度不等于框一定准。

一个检测可以类别很自信，但框很松。也可以框住了目标，但类别错了。

提高 `conf` 阈值通常会：

- 减少预测框
- 减少误检
- 增加漏检风险

降低 `conf` 阈值通常会：

- 增加预测框
- 找到更多低置信度目标
- 增加误检

### NMS：非极大值抑制

模型可能对同一个物体输出多个重叠框。NMS 的作用是保留最强的框，去掉重复框。

简化过程：

1. 按置信度从高到低排序。
2. 保留最高置信度框。
3. 删除与它高度重叠的低置信度框。
4. 对剩余框重复这个过程。

NMS 解决的是“重复框”问题，不解决“类别定义不清楚”或“训练数据不足”的问题。

---

## 第 3 章：YOLO 模型到底在做什么

YOLO 是 You Only Look Once 的缩写。它的核心思想是：模型只看一遍整张图，就同时预测物体类别和位置。

实际工程中，你可以把 YOLO 理解成：

```text
输入图片 -> 特征提取 -> 多尺度融合 -> 检测头预测 -> 后处理 -> 输出框
```

### Backbone、Neck、Head

虽然你不需要从零实现 YOLO，但需要知道三个概念：

Backbone：主干网络，用来提取图像特征，例如边缘、纹理、形状、部件。

Neck：特征融合部分，用来结合不同尺度的信息。小目标和大目标依赖的特征尺度不同。

Head：检测头，输出类别、框位置和置信度。

后处理：包括阈值过滤、NMS、结果格式化等。

### 为什么用预训练模型

从零训练模型需要大量数据和算力。初学者通常不这么做。

预训练模型已经从大数据集中学到很多通用视觉能力，例如：

- 边缘
- 角点
- 纹理
- 常见物体部件
- 场景布局

你在自定义数据集上训练时，通常是在预训练模型基础上微调。

### 模型大小

YOLO 模型常见大小包括 nano、small、medium、large、xlarge。一般规律是：

- 越小越快，越适合弱设备
- 越大可能越准，但更吃显存和算力

初学者建议：

1. 先用 nano。
2. 先修数据和标注。
3. 数据质量稳定后再尝试更大模型。

---

## 第 4 章：运行预训练模型预测

预测是最安全的第一步，因为它不需要训练。

常用参数：

| 参数 | 含义 |
| --- | --- |
| `model` | 权重文件或官方模型名 |
| `source` | 图片、文件夹、视频、URL、摄像头编号 |
| `conf` | 置信度阈值 |
| `imgsz` | 输入图片尺寸 |
| `save` | 是否保存可视化结果 |

本课程提供脚本：

```powershell
python scripts/predict_image.py --source data/samples --model yolo11n.pt --imgsz 320 --conf 0.25
```

如果本地电脑较弱：

- 使用 nano 模型
- `imgsz` 先用 320 或 416
- 先测图片，不测视频
- 不急着跑摄像头实时检测

### 如何观察预测结果

不要只看“框出来了没有”。你应该问：

- 该出现的目标是否都出现了？
- 有没有把背景误认为目标？
- 框是否太松或太紧？
- 小目标是否漏掉？
- 同一个物体是否被重复框出？
- 置信度和肉眼判断是否一致？

### 预训练模型的局限

预训练模型通常对 COCO 等常见类别效果不错，但对你的自定义场景未必有效。例如：

- 工业零件
- 特定品牌包装
- 小缺陷
- 屏幕 UI 元素
- 非常特殊的摄像头角度

这就是为什么需要自定义数据集。

---

## 第 5 章：构建 YOLO 数据集

YOLO 数据集由三部分组成：

- 图片
- 标签 `.txt`
- 数据集配置 `dataset.yaml`

推荐结构：

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

`dataset.yaml` 示例：

```yaml
path: data/yolo_dataset
train: images/train
val: images/val
test: images/test

names:
  0: phone
  1: cup
  2: mouse
```

标签文件示例：

```text
0 0.512 0.433 0.210 0.315
2 0.721 0.602 0.180 0.140
```

每一行代表一个目标。

### 数据集划分

训练集用于学习。验证集用于观察泛化能力。测试集用于最终评估。

初学者可以用：

- 训练集：70%-80%
- 验证集：10%-20%
- 测试集：10%

如果数据很少，也要保留验证集，但不要过度迷信指标。小数据集上，错误案例分析更重要。

### 标注规则

标注前要写规则。没有规则，标签会越来越乱。

例子：

- 只框可见部分，不框被遮挡但想象中存在的部分。
- 目标至少可见 30% 才标注。
- 小于 12 像素的目标暂不标注。
- 同一类物体统一使用同一个 class id。
- 反光、模糊、遮挡样本要保留一部分，因为真实场景会出现。

### 常见数据错误

- 图片有标签，标签文件名不匹配
- 标签坐标不是 0 到 1
- class id 超出 `names` 范围
- 漏标目标
- 同一个目标重复标注
- 框太松
- 框太紧
- 训练集和验证集来自完全不同分布

本课程提供检查脚本：

```powershell
python scripts/inspect_dataset.py --data data/yolo_dataset/dataset.yaml
```

### 数据版本

不要不断覆盖数据集。建议命名：

```text
dataset_v0_smoke
dataset_v1_initial
dataset_v2_more_low_light
dataset_v3_fixed_labels
```

每个训练结果都应该能对应到一个数据版本。

---

## 第 6 章：云端训练

训练是最吃算力的环节。如果本地电脑弱，直接用云端。

常见选择：

- Google Colab
- Kaggle Notebook
- Ultralytics Cloud Training
- 云服务器 GPU

训练示例：

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
model.train(
    data="/content/yolo_dataset/dataset.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    project="/content/outputs/train",
    name="custom_yolo",
)
```

### 先做 smoke run

不要一上来跑 100 epoch。先跑短训练：

```python
model.train(data="dataset.yaml", epochs=3, imgsz=320)
```

短训练用来发现：

- 路径错误
- 标签格式错误
- 图片缺失
- class id 错误
- GPU 不可用
- 依赖安装失败

如果 smoke run 失败，不要调参。先修数据和路径。

### 常见训练参数

| 参数 | 含义 |
| --- | --- |
| `epochs` | 训练轮数 |
| `imgsz` | 输入分辨率 |
| `batch` | 每批图片数量 |
| `model` | 初始权重和模型大小 |
| `project` | 输出目录 |
| `name` | 本次实验名称 |

### 训练结束后保存什么

至少保存：

- `best.pt`
- 训练命令
- 数据集版本
- 关键指标
- 训练曲线或结果图
- 示例预测结果
- notebook 链接或导出的 notebook

如果你只保存 `best.pt`，以后很难复现。

---

## 第 7 章：验证、指标与错误分析

训练完成后，要验证模型。

常见指标：

| 指标 | 含义 |
| --- | --- |
| Precision | 预测出来的目标中，有多少是真的 |
| Recall | 真实目标中，有多少被找到了 |
| AP | 某个类别的平均精度 |
| mAP | 多个类别 AP 的平均值 |
| mAP50 | IoU=0.50 下的 mAP |
| mAP50-95 | 多个 IoU 阈值平均后的 mAP |

### 怎么读 precision 和 recall

高 precision、低 recall：

- 模型比较保守
- 误检少
- 漏检多
- 可以考虑降低 conf 或补充难样本

低 precision、高 recall：

- 模型框得很多
- 漏检少
- 误检多
- 可以考虑提高 conf 或添加 hard negatives

某一类 mAP 很低：

- 该类样本少
- 标注不一致
- 类别之间太像
- 图像质量差

### 错误案例比总分更重要

你应该建立错误表：

| 错误类型 | 现象 | 下一步 |
| --- | --- | --- |
| 漏检 | 真实目标没框出来 | 补相似样本，检查阈值 |
| 误检 | 背景被当成目标 | 添加 hard negative |
| 框不准 | 类别对但位置差 | 修标签，增大分辨率 |
| 类别错 | A 被识别成 B | 澄清类别定义 |
| 重复框 | 同一物体多个框 | 检查 NMS/阈值 |
| 域偏移 | 新场景效果差 | 收集目标场景数据 |

### 一次只改一个大变量

不要同时改：

- 数据集
- 模型大小
- 图片尺寸
- epoch
- batch
- 阈值

如果同时改，结果变好也不知道原因。

推荐迭代：

```text
训练 v1 -> 错误分析 -> 数据 v2 -> 训练 v2 -> 对比
```

---

## 第 8 章：导出与部署

训练得到模型文件，不等于完成部署。部署要考虑运行环境、速度、隐私、成本和许可。

常见路线：

| 路线 | 适合 | 风险 |
| --- | --- | --- |
| `.pt` + Ultralytics | Python demo、notebook | 依赖 PyTorch |
| ONNX | 跨平台推理 | 后处理细节 |
| OpenVINO | CPU 加速 | 环境配置 |
| TensorRT | NVIDIA GPU | 配置复杂 |
| Roboflow Hosted API | 快速托管 | 成本和隐私 |
| Hugging Face Spaces | 作品展示 | 冷启动和资源限制 |

导出示例：

```powershell
python scripts/export_model.py --model outputs/best.pt --format onnx
```

### 部署前要回答的问题

- 谁上传图片？
- 图片是否包含隐私信息？
- 图片会不会被保存？
- 推理需要多快？
- 模型错了会造成什么后果？
- 运行在 CPU 还是 GPU？
- 是否需要离线运行？
- 许可证是否允许当前用途？

### 弱电脑部署策略

如果本地跑不动：

- 本地只做客户端
- 云端运行推理
- 使用 Hosted API
- 降低 `imgsz`
- 使用 nano 模型
- 视频隔帧处理
- 做图片上传 demo，而不是实时摄像头 demo

一个稳定的图片上传 demo，比一个卡顿的实时 demo 更适合作为第一版项目。

---

## 第 9 章：工程化一个 YOLO 项目

一个合格的 YOLO 项目不只是模型权重。它至少包括：

```text
project/
  README.md
  data_card.md
  model_card.md
  train.py
  predict.py
  dataset.yaml
  examples/
  reports/
```

### README 应该写什么

- 项目目标
- 检测类别
- 如何安装
- 如何预测
- 如何训练
- 示例结果
- 已知问题

### Data Card

数据卡记录：

- 类别
- 图片数量
- 数据来源
- 采集场景
- 标注规则
- 数据偏差
- train/val/test 划分
- 隐私风险

### Model Card

模型卡记录：

- 基础模型
- 数据集版本
- 训练命令
- 指标
- 适用场景
- 不适用场景
- 已知失败模式
- 许可说明

### 可复现性公式

```text
数据版本 + 代码版本 + 训练命令 + 模型文件 = 一次实验
```

没有这个公式，项目很快会变成一堆无法解释的 `best.pt`。

---

## 第 10 章：最终项目要求

最终项目要回答六个问题：

1. 这个模型解决什么问题？
2. 它从什么数据学来？
3. 它是怎么训练的？
4. 它效果如何？
5. 它在哪里失败？
6. 其他人如何运行或检查它？

最低交付物：

- 问题定义
- 数据集说明
- 训练命令
- 评估指标
- 至少 5 张预测示例
- 错误案例分析
- 部署或 demo 方案
- 下一轮数据改进计划

### 好的初学者项目

“检测桌面上的手机、杯子和鼠标”是一个好项目，如果它包含：

- 清晰类别定义
- 100-300 张图片
- 不同光照和角度
- 完整训练记录
- 漏检/误检案例
- 简单图片上传 demo

### 不好的初学者项目

“检测所有危险物品”不适合第一版，因为：

- 类别不清楚
- 边界模糊
- 数据需求巨大
- 误判代价高
- 评估方式不明确

初学者应该从窄问题开始。

---

## 附录 A：常用公式

### 像素框转 YOLO 格式

已知：

```text
图片宽度 = W
图片高度 = H
左上角 = (x1, y1)
右下角 = (x2, y2)
```

则：

```text
x_center = ((x1 + x2) / 2) / W
y_center = ((y1 + y2) / 2) / H
width = (x2 - x1) / W
height = (y2 - y1) / H
```

### IoU

```text
intersection_width = max(0, min(x2_a, x2_b) - max(x1_a, x1_b))
intersection_height = max(0, min(y2_a, y2_b) - max(y1_a, y1_b))
intersection_area = intersection_width * intersection_height
union_area = area_a + area_b - intersection_area
IoU = intersection_area / union_area
```

### Precision 和 Recall

```text
precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)
```

---

## 附录 B：命令速查

课程命令：

```powershell
python tools/course.py list
python tools/course.py show lab00
python tools/course.py grade lab00
python tools/course.py status
python tools/course.py handin lab00
```

环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
python scripts/check_environment.py
```

预测：

```powershell
python scripts/predict_image.py --source data/samples --model yolo11n.pt --imgsz 320 --conf 0.25
```

数据检查：

```powershell
python scripts/inspect_dataset.py --data data/yolo_dataset/dataset.yaml
```

训练：

```powershell
python scripts/train_custom.py --data data/yolo_dataset/dataset.yaml --model yolo11n.pt --epochs 50 --imgsz 640
```

验证：

```powershell
python scripts/evaluate_model.py --model outputs/train/custom_yolo/weights/best.pt --data data/yolo_dataset/dataset.yaml
```

导出：

```powershell
python scripts/export_model.py --model outputs/train/custom_yolo/weights/best.pt --format onnx
```

---

## 附录 C：术语表

AP：Average Precision，单个类别的平均精度。

Backbone：主干网络，用于提取图像特征。

Batch：每次训练送入模型的一批图片。

Bounding box：检测框，框住目标的矩形。

Class：类别。

Confidence：置信度。

Dataset YAML：数据集配置文件。

Epoch：模型完整看过训练集一次。

False negative：漏检。

False positive：误检。

IoU：交并比。

mAP：多个类别 AP 的平均值。

NMS：非极大值抑制，用于去掉重复框。

ONNX：模型交换格式。

Pretrained weights：预训练权重。

Recall：召回率。

Validation set：验证集。

YOLO：You Only Look Once，一类实时目标检测模型。

---

## 附录 D：参考资料

- Ultralytics Python Usage: https://docs.ultralytics.com/usage/python
- Ultralytics Object Detection Dataset Format: https://docs.ultralytics.com/datasets/detect
- Ultralytics CLI Usage: https://docs.ultralytics.com/usage/cli
- Original YOLO paper: https://arxiv.org/abs/1506.02640
- MIT 6.S081 schedule and lab style reference: https://pdos.csail.mit.edu/6.S081/2020/schedule.html
- MIT 6.S081 sample lab hand-in convention: https://pdos.csail.mit.edu/6.S081/2020/labs/util.html

