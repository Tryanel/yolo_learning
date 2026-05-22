# YOLO Learning Lab

一个仿 MIT 6.S081 实验课组织方式的 YOLO 目标检测教学仓库。

这不是单纯的资料集合，而是一门可执行的小课：有教材、有 schedule、有 lab、有提交区、有轻量 grader，也有 hand-in 打包命令。默认学习路线是 **本地轻量学习 + 云端训练/部署**，适合本地电脑配置一般但想完整学会 YOLO 项目流程的人。

## Quick Start

```powershell
cd "D:\Cat\Documents\New project 6\yolo-learning-lab"
python tools/course.py list
python tools/course.py show lab00
python tools/course.py grade lab00
```

如果你要初始化环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
python scripts/check_environment.py
```

## Course Map

- [course/schedule.md](course/schedule.md): 课程日程
- [course/policies.md](course/policies.md): 提交、数据、模型和许可规则
- [docs/teaching_model.md](docs/teaching_model.md): 仓库教学模式说明
- [docs/textbook/yolo_model_textbook_zh.md](docs/textbook/yolo_model_textbook_zh.md): 完整 YOLO 中文教材
- [docs/textbook/yolo_model_textbook.md](docs/textbook/yolo_model_textbook.md): English textbook
- [labs/](labs): 每个实验的说明
- [submissions/](submissions): 每个实验的提交模板
- [scripts/](scripts): YOLO 预测、训练、评估、导出和数据检查脚本

## Labs

| Lab | Topic | Command |
| --- | --- | --- |
| `lab00` | 本地环境与课程工具 | `python tools/course.py grade lab00` |
| `lab01` | 框、IoU、NMS | `python tools/course.py grade lab01` |
| `lab02` | 本地轻量预训练预测 | `python tools/course.py grade lab02` |
| `lab03` | YOLO 数据集构建与审计 | `python tools/course.py grade lab03` |
| `lab04` | 云端训练与实验日志 | `python tools/course.py grade lab04` |
| `lab05` | 验证、错误分析、数据迭代 | `python tools/course.py grade lab05` |
| `lab06` | 导出与轻量推理 | `python tools/course.py grade lab06` |
| `lab07` | 托管 demo 与部署取舍 | `python tools/course.py grade lab07` |
| `lab08` | 最终项目 | `python tools/course.py grade lab08` |

## Course Commands

```powershell
python tools/course.py list
python tools/course.py status
python tools/course.py show lab03
python tools/course.py grade lab03
python tools/course.py grade all
python tools/course.py handin lab03
```

如果你的环境有 `make`，也可以用：

```powershell
make list
make grade LAB=lab00
make handin LAB=lab00
```

## Repository Structure

```text
yolo-learning-lab/
  course/           # schedule, policies, lab manifest
  docs/             # teaching model and textbook
  labs/             # lab handouts
  submissions/      # student answers and time.txt files
  data/             # dataset templates and local ignored data
  scripts/          # helper scripts for YOLO workflows
  tools/            # course CLI and slide builders
  slides/           # generated teaching slides
  handin/           # generated lab tarballs
```

## Learning Philosophy

像 6.S081 那样学：不要只看视频或笔记，要跑命令、改文件、检查输出、提交证据。

对 YOLO 来说，真正重要的不是“我训练出了一个模型”，而是：

- 我知道数据集怎么定义。
- 我知道模型为什么漏检或误检。
- 我知道本地电脑做什么，云端资源做什么。
- 我能复现训练命令和结果。
- 我能诚实说明模型当前不能做什么。

## First Lab

从 `lab00` 开始：

```powershell
python tools/course.py show lab00
```

然后填写：

```text
submissions/lab00/environment.md
submissions/lab00/time.txt
```

再运行：

```powershell
python tools/course.py grade lab00
```
