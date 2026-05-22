# Week 01 - 环境与最小 Python 基础

## 本周目标

- 安装 Python 和虚拟环境
- 安装 YOLO 学习需要的依赖
- 会运行一个 Python 脚本
- 知道图片路径、模型路径、输出路径分别是什么

## 必做任务

1. 创建虚拟环境并安装依赖。
2. 运行 `python scripts/check_environment.py`。
3. 截图或记录 Python、PyTorch、Ultralytics 版本。
4. 新建 `notes/week_01.md`，写下遇到的环境问题。

## 够用的 Python 知识

- 变量：`model_path = "yolo11n.pt"`
- 函数：`def main():`
- 列表：`classes = ["phone", "cup"]`
- 字典：`metrics = {"map50": 0.72}`
- 文件路径：Windows 下建议用 `/` 或 `pathlib.Path`
- 命令行参数：用 `argparse` 改变脚本输入

## 检查点

你能用一句话回答：

- 什么是虚拟环境？
- `pip install -r requirements.txt` 做了什么？
- 为什么输出目录不应该提交到 Git？

