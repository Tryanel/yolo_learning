# PPTX Outline: week_01_yolo_learning_plan.pptx

- Source: `D:\Cat\Documents\New project 6\yolo-learning-lab\slides\week_01_yolo_learning_plan.pptx`
- Slides: 8

## Slide 1: WEEK 01

- Part: `ppt/slides/slide1.xml`
- Image/media count: 0

### Visible text
- WEEK 01
- YOLO 第一周学习计划
- 本地轻量环境：先把工具链跑稳，再把训练交给云端
- week01.local
- cd yolo-learning-lab
- python -m venv .venv
- .\.venv\Scripts\Activate.ps1
- python scripts/check_environment.py
- 目标不是训练模型
- 而是让学习仓库、Python 环境
- 和检查脚本进入可控状态
- 每天 45-60 分钟
- 2026

### Existing notes
- 1

## Slide 2: YOLO LEARNING LAB / WEEK 01

- Part: `ppt/slides/slide2.xml`
- Image/media count: 0

### Visible text
- YOLO LEARNING LAB / WEEK 01
- 这一周只解决一件事：本地能稳定学习
- 不把弱电脑变成训练服务器，只让它成为清晰、可复现的学习工作台。
- 02
- 1
- 装对 Python
- 确认不是 Windows Store 占位入口，能看到真实版本号。
- 2
- 建虚拟环境
- 把 YOLO 学习依赖和系统环境隔离，方便重装和排错。
- 3
- 跑检查脚本
- 记录版本、库和硬件状态。
- 本周不追求：训练自定义模型、实时摄像头推理、部署在线服务。
- 这些会从第 4 周开始逐步交给 Colab、Ultralytics Platform 或 Hugging Face Spaces。

### Existing notes
- 2

## Slide 3: YOLO LEARNING LAB / WEEK 01

- Part: `ppt/slides/slide3.xml`
- Image/media count: 0

### Visible text
- YOLO LEARNING LAB / WEEK 01
- 本地与云端的分工
- 第一周先把左侧做好，右侧只需要知道未来会用到。
- 03
- 本地电脑
- 云端资源
- 仓库管理
- README、notes、assignments
- 轻量预测
- 少量图片、nano 模型
- 数据整理
- 图片归档、dataset.yaml
- 复盘记录
- 错误案例、环境日志
- 模型训练
- Colab / Ultralytics Cloud
- 批量评估
- 验证集、mAP、错误案例
- 在线 Demo
- Hugging Face Spaces / Roboflow
- 模型导出
- ONNX、API 或托管推理
- Week 01
- 先完成本地侧闭环；训练与部署不用在这一周硬做。

### Existing notes
- 3

## Slide 4: YOLO LEARNING LAB / WEEK 01

- Part: `ppt/slides/slide4.xml`
- Image/media count: 0

### Visible text
- YOLO LEARNING LAB / WEEK 01
- 7 天安排：每天一个小闭环
- 每天只留一个主任务，结束时都要有一个可保存的证据。
- 04
- D1
- 确认 Python
- 版本号、安装路径
- D2
- 创建虚拟环境
- .venv 可激活
- D3
- 安装依赖
- requirements 跑完
- D4
- 跑环境检查
- 保存输出记录
- D5
- 认识仓库结构
- 知道文件放哪里
- D6
- 补最小 Python
- 变量、函数、路径
- D7
- 复盘与排错
- 写 week_01.md
- 节奏建议
- 每天 45-60 分钟。遇到安装问题时，先记录现象和命令输出，不急着跳到训练。

### Existing notes
- 4

## Slide 5: YOLO LEARNING LAB / WEEK 01

- Part: `ppt/slides/slide5.xml`
- Image/media count: 0

### Visible text
- YOLO LEARNING LAB / WEEK 01
- 环境搭建命令：一行一行跑
- 先确认 Python 入口，再创建隔离环境，最后运行检查脚本。
- 05
- PowerShell
- python --version
- where.exe python
- python -m venv .venv
- .\.venv\Scripts\Activate.ps1
- python -m pip install -U pip
- pip install -r requirements.txt
- python scripts/check_environment.py
- 看见版本号
- 如果只有 WindowsApps 路径，多半是商店占位入口。
- 激活 .venv
- 命令行前面出现 (.venv) 后再安装依赖。
- 保存输出
- 把检查结果放进 notes/week_01.md。
- 本页是第一周最重要的操作页。跑不通也没关系，问题记录本身就是本周产物。

### Existing notes
- 5

## Slide 6: YOLO LEARNING LAB / WEEK 01

- Part: `ppt/slides/slide6.xml`
- Image/media count: 0

### Visible text
- YOLO LEARNING LAB / WEEK 01
- 够用的 Python：只学会读懂脚本入口
- 第一周不学算法，只补能运行脚本、改参数、看路径的能力。
- 06
- 变量
- model_path = "yolo11n.pt"
- 函数
- def main():
- 列表
- classes = ["phone", "cup"]
- 字典
- metrics = {"map50": 0.72}
- 路径
- Path('data/samples')
- 参数
- argparse.ArgumentParser()
- 检查自己是否够用
- 能打开 `scripts/check_environment.py`，大概说出每一段在检查什么，就达标了。

### Existing notes
- 6

## Slide 7: YOLO LEARNING LAB / WEEK 01

- Part: `ppt/slides/slide7.xml`
- Image/media count: 0

### Visible text
- YOLO LEARNING LAB / WEEK 01
- 本周作业：交付环境证据
- 不交模型文件，交一份能复盘的环境记录。
- 07
- 1
- 运行环境检查
- python scripts/check_environment.py
- 2
- 保存关键输出
- Python / Torch / Ultralytics / CUDA
- 3
- 写学习复盘
- notes/week_01.md
- 4
- 列出阻塞问题
- 错误信息、已尝试命令、下一步
- 通过标准
- 你能解释虚拟环境的作用，也知道当前电脑适合本地轻量测试还是需要云端训练。

### Existing notes
- 7

## Slide 8: 完成定义

- Part: `ppt/slides/slide8.xml`
- Image/media count: 0

### Visible text
- 完成定义
- 第一周结束时，你不需要有模型成果。
- 你只需要有一个可复现的学习环境、一份环境记录，以及继续进入第 2 周的信心。
- Python 入口正确
- .venv 可激活
- 依赖安装有记录
- check_environment.py 已运行
- notes/week_01.md 已写
- 下一周
- 目标检测基础
- 开始理解 bounding box、confidence、IoU、mAP，以及模型为什么会漏检或误检。
- READY FOR WEEK 02
- 08

### Existing notes
- 8
