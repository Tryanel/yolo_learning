const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const outDir = path.join(__dirname, "..", "slides");
fs.mkdirSync(outDir, { recursive: true });

const pptx = new pptxgen();
pptx.layout = "LAYOUT_16x9";
pptx.author = "Codex";
pptx.company = "YOLO Learning Lab";
pptx.subject = "第一周学习计划：本地轻量环境";
pptx.title = "YOLO 第一周学习计划";
pptx.lang = "zh-CN";
pptx.theme = {
  headFontFace: "Microsoft YaHei UI",
  bodyFontFace: "Microsoft YaHei",
  lang: "zh-CN",
};
pptx.defineLayout({ name: "CUSTOM_WIDE", width: 13.333, height: 7.5 });
pptx.layout = "CUSTOM_WIDE";
pptx.margin = 0;

const C = {
  ink: "172026",
  ink2: "334155",
  muted: "667085",
  paper: "F7F3EA",
  paper2: "FFFDF7",
  mint: "2BAE9E",
  mintDark: "0F766E",
  coral: "F36F45",
  gold: "F4B942",
  navy: "16324F",
  line: "D8CDB8",
  white: "FFFFFF",
  codeBg: "10202A",
  codeText: "C7F9CC",
};

const W = 13.333;
const H = 7.5;
const fontH = "Microsoft YaHei UI";
const fontB = "Microsoft YaHei";

function addBg(slide, color = C.paper) {
  slide.background = { color };
}

function addPage(slide, n) {
  slide.addText(String(n).padStart(2, "0"), {
    x: 12.2,
    y: 6.92,
    w: 0.55,
    h: 0.2,
    fontFace: fontB,
    fontSize: 9,
    color: C.muted,
    margin: 0,
    align: "right",
  });
}

function addKicker(slide, text, x = 0.72, y = 0.45, color = C.mintDark) {
  slide.addText(text, {
    x,
    y,
    w: 5.8,
    h: 0.25,
    fontFace: fontH,
    fontSize: 10,
    bold: true,
    color,
    charSpacing: 1.8,
    margin: 0,
  });
}

function addTitle(slide, title, subtitle, n) {
  addKicker(slide, "YOLO LEARNING LAB / WEEK 01");
  slide.addText(title, {
    x: 0.72,
    y: 0.82,
    w: 9.2,
    h: 0.58,
    fontFace: fontH,
    fontSize: 27,
    bold: true,
    color: C.ink,
    margin: 0,
    fit: "shrink",
    breakLine: false,
  });
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.74,
      y: 1.48,
      w: 8.6,
      h: 0.3,
      fontFace: fontB,
      fontSize: 12.5,
      color: C.muted,
      margin: 0,
      fit: "shrink",
    });
  }
  addPage(slide, n);
}

function addRule(slide, x, y, w, color = C.line, width = 1) {
  slide.addShape(pptx.ShapeType.line, {
    x,
    y,
    w,
    h: 0,
    line: { color, width },
  });
}

function terminal(slide, x, y, w, h, lines, title = "PowerShell") {
  slide.addShape(pptx.ShapeType.roundRect, {
    x,
    y,
    w,
    h,
    rectRadius: 0.08,
    fill: { color: C.codeBg },
    line: { color: "243844", width: 1 },
  });
  slide.addShape(pptx.ShapeType.rect, {
    x,
    y,
    w,
    h: 0.35,
    fill: { color: "172B35" },
    line: { color: "172B35", transparency: 100 },
  });
  slide.addText(title, {
    x: x + 0.24,
    y: y + 0.11,
    w: w - 0.5,
    h: 0.15,
    fontFace: "Consolas",
    fontSize: 8.5,
    color: "A7F3D0",
    margin: 0,
  });
  slide.addText(lines.join("\n"), {
    x: x + 0.26,
    y: y + 0.55,
    w: w - 0.5,
    h: h - 0.75,
    fontFace: "Consolas",
    fontSize: 11,
    color: C.codeText,
    breakLine: false,
    fit: "shrink",
    margin: 0,
    breakLine: false,
  });
}

function dot(slide, x, y, color, size = 0.13) {
  slide.addShape(pptx.ShapeType.ellipse, {
    x,
    y,
    w: size,
    h: size,
    fill: { color },
    line: { color, transparency: 100 },
  });
}

function labeledStep(slide, idx, title, body, x, y, color) {
  const textX = x + 0.72;
  const safeW = Math.max(2.1, Math.min(3.95, 12.1 - textX));
  slide.addShape(pptx.ShapeType.ellipse, {
    x,
    y,
    w: 0.54,
    h: 0.54,
    fill: { color },
    line: { color, transparency: 100 },
  });
  slide.addText(String(idx), {
    x,
    y: y + 0.11,
    w: 0.54,
    h: 0.18,
    fontFace: fontH,
    fontSize: 13,
    bold: true,
    color: C.white,
    align: "center",
    margin: 0,
  });
  slide.addText(title, {
    x: textX,
    y: y - 0.02,
    w: safeW,
    h: 0.28,
    fontFace: fontH,
    fontSize: 14,
    bold: true,
    color: C.ink,
    margin: 0,
    fit: "shrink",
  });
  slide.addText(body, {
    x: textX,
    y: y + 0.36,
    w: safeW,
    h: 0.48,
    fontFace: fontB,
    fontSize: 10.5,
    color: C.muted,
    margin: 0,
    fit: "shrink",
    breakLine: false,
  });
}

function addChip(slide, text, x, y, w, color) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x,
    y,
    w,
    h: 0.36,
    rectRadius: 0.06,
    fill: { color },
    line: { color, transparency: 100 },
  });
  slide.addText(text, {
    x,
    y: y + 0.095,
    w,
    h: 0.12,
    align: "center",
    fontFace: fontH,
    fontSize: 8.5,
    bold: true,
    color: C.white,
    margin: 0,
    fit: "shrink",
  });
}

// Slide 1
{
  const s = pptx.addSlide();
  addBg(s, C.navy);
  s.addShape(pptx.ShapeType.rect, {
    x: 8.85,
    y: 0,
    w: 4.48,
    h: H,
    fill: { color: C.mint },
    line: { color: C.mint, transparency: 100 },
  });
  s.addShape(pptx.ShapeType.arc, {
    x: 7.55,
    y: 0.85,
    w: 4.9,
    h: 4.9,
    adjustPoint: 0.28,
    line: { color: "F9D271", width: 8, transparency: 8 },
    rotate: 15,
  });
  s.addText("WEEK 01", {
    x: 0.75,
    y: 0.62,
    w: 2.4,
    h: 0.28,
    fontFace: fontH,
    fontSize: 11,
    bold: true,
    color: "9DEAD8",
    charSpacing: 2,
    margin: 0,
  });
  s.addText("YOLO 第一周学习计划", {
    x: 0.75,
    y: 1.32,
    w: 7.4,
    h: 0.75,
    fontFace: fontH,
    fontSize: 34,
    bold: true,
    color: C.white,
    margin: 0,
    fit: "shrink",
  });
  s.addText("本地轻量环境：先把工具链跑稳，再把训练交给云端", {
    x: 0.78,
    y: 2.25,
    w: 6.9,
    h: 0.38,
    fontFace: fontB,
    fontSize: 15,
    color: "D7EDE8",
    margin: 0,
    fit: "shrink",
  });
  terminal(s, 0.82, 3.32, 5.75, 2.32, [
    "cd yolo-learning-lab",
    "python -m venv .venv",
    ".\\.venv\\Scripts\\Activate.ps1",
    "python scripts/check_environment.py",
  ], "week01.local");
  s.addText("目标不是训练模型\n而是让学习仓库、Python 环境\n和检查脚本进入可控状态", {
    x: 8.97,
    y: 5.05,
    w: 3.62,
    h: 1.05,
    fontFace: fontH,
    fontSize: 17,
    bold: true,
    color: C.navy,
    margin: 0,
    fit: "shrink",
  });
  s.addText("每天 45-60 分钟", {
    x: 8.98,
    y: 6.22,
    w: 2.05,
    h: 0.25,
    fontFace: fontH,
    fontSize: 10,
    bold: true,
    color: C.white,
    margin: 0,
  });
  s.addText("2026", {
    x: 11.4,
    y: 6.95,
    w: 0.75,
    h: 0.16,
    fontFace: fontB,
    fontSize: 8.5,
    color: C.navy,
    margin: 0,
  });
}

// Slide 2
{
  const s = pptx.addSlide();
  addBg(s);
  addTitle(s, "这一周只解决一件事：本地能稳定学习", "不把弱电脑变成训练服务器，只让它成为清晰、可复现的学习工作台。", 2);
  addRule(s, 0.75, 2.15, 11.85);
  labeledStep(s, 1, "装对 Python", "确认不是 Windows Store 占位入口，能看到真实版本号。", 0.92, 2.65, C.coral);
  labeledStep(s, 2, "建虚拟环境", "把 YOLO 学习依赖和系统环境隔离，方便重装和排错。", 5.08, 2.65, C.mintDark);
  labeledStep(s, 3, "跑检查脚本", "记录版本、库和硬件状态。", 9.25, 2.65, C.gold);
  s.addShape(pptx.ShapeType.line, { x: 1.46, y: 2.92, w: 3.35, h: 0, line: { color: C.line, width: 2 } });
  s.addShape(pptx.ShapeType.line, { x: 5.62, y: 2.92, w: 3.35, h: 0, line: { color: C.line, width: 2 } });
  s.addText("本周不追求：训练自定义模型、实时摄像头推理、部署在线服务。", {
    x: 1.06,
    y: 4.78,
    w: 10.3,
    h: 0.4,
    fontFace: fontH,
    fontSize: 17,
    bold: true,
    color: C.ink,
    margin: 0,
    fit: "shrink",
  });
  s.addText("这些会从第 4 周开始逐步交给 Colab、Ultralytics Platform 或 Hugging Face Spaces。", {
    x: 1.08,
    y: 5.38,
    w: 9.8,
    h: 0.3,
    fontFace: fontB,
    fontSize: 12,
    color: C.muted,
    margin: 0,
    fit: "shrink",
  });
}

// Slide 3
{
  const s = pptx.addSlide();
  addBg(s, C.paper2);
  addTitle(s, "本地与云端的分工", "第一周先把左侧做好，右侧只需要知道未来会用到。", 3);
  s.addText("本地电脑", {
    x: 1.0,
    y: 2.08,
    w: 2.2,
    h: 0.3,
    fontFace: fontH,
    fontSize: 18,
    bold: true,
    color: C.ink,
    margin: 0,
  });
  s.addText("云端资源", {
    x: 7.58,
    y: 2.08,
    w: 2.2,
    h: 0.3,
    fontFace: fontH,
    fontSize: 18,
    bold: true,
    color: C.ink,
    margin: 0,
  });
  s.addShape(pptx.ShapeType.rect, {
    x: 0.9,
    y: 2.58,
    w: 5.15,
    h: 3.35,
    fill: { color: "E8F5F1" },
    line: { color: "B6DDD3", width: 1 },
  });
  s.addShape(pptx.ShapeType.rect, {
    x: 7.25,
    y: 2.58,
    w: 5.15,
    h: 3.35,
    fill: { color: "FFF1E8" },
    line: { color: "F4C5A9", width: 1 },
  });
  const left = [
    ["仓库管理", "README、notes、assignments"],
    ["轻量预测", "少量图片、nano 模型"],
    ["数据整理", "图片归档、dataset.yaml"],
    ["复盘记录", "错误案例、环境日志"],
  ];
  const right = [
    ["模型训练", "Colab / Ultralytics Cloud"],
    ["批量评估", "验证集、mAP、错误案例"],
    ["在线 Demo", "Hugging Face Spaces / Roboflow"],
    ["模型导出", "ONNX、API 或托管推理"],
  ];
  left.forEach(([a, b], i) => {
    const y = 2.95 + i * 0.68;
    dot(s, 1.25, y + 0.06, C.mintDark, 0.14);
    s.addText(a, { x: 1.55, y, w: 1.45, h: 0.2, fontFace: fontH, fontSize: 12.2, bold: true, color: C.ink, margin: 0 });
    s.addText(b, { x: 3.05, y, w: 2.3, h: 0.2, fontFace: fontB, fontSize: 10.8, color: C.muted, margin: 0, fit: "shrink" });
  });
  right.forEach(([a, b], i) => {
    const y = 2.95 + i * 0.68;
    dot(s, 7.6, y + 0.06, C.coral, 0.14);
    s.addText(a, { x: 7.9, y, w: 1.45, h: 0.2, fontFace: fontH, fontSize: 12.2, bold: true, color: C.ink, margin: 0 });
    s.addText(b, { x: 9.4, y, w: 2.55, h: 0.2, fontFace: fontB, fontSize: 10.8, color: C.muted, margin: 0, fit: "shrink" });
  });
  s.addShape(pptx.ShapeType.chevron, {
    x: 6.2,
    y: 3.5,
    w: 0.8,
    h: 0.75,
    fill: { color: C.gold },
    line: { color: C.gold, transparency: 100 },
  });
  s.addText("Week 01", {
    x: 1.0,
    y: 6.25,
    w: 1.2,
    h: 0.22,
    fontFace: fontH,
    fontSize: 10,
    bold: true,
    color: C.mintDark,
    margin: 0,
  });
  s.addText("先完成本地侧闭环；训练与部署不用在这一周硬做。", {
    x: 2.05,
    y: 6.24,
    w: 7.1,
    h: 0.25,
    fontFace: fontB,
    fontSize: 11.2,
    color: C.muted,
    margin: 0,
  });
}

// Slide 4
{
  const s = pptx.addSlide();
  addBg(s);
  addTitle(s, "7 天安排：每天一个小闭环", "每天只留一个主任务，结束时都要有一个可保存的证据。", 4);
  const days = [
    ["D1", "确认 Python", "版本号、安装路径"],
    ["D2", "创建虚拟环境", ".venv 可激活"],
    ["D3", "安装依赖", "requirements 跑完"],
    ["D4", "跑环境检查", "保存输出记录"],
    ["D5", "认识仓库结构", "知道文件放哪里"],
    ["D6", "补最小 Python", "变量、函数、路径"],
    ["D7", "复盘与排错", "写 week_01.md"],
  ];
  addRule(s, 0.95, 3.18, 11.38, "CFC3AC", 1.5);
  days.forEach(([d, title, proof], i) => {
    const x = 0.95 + i * 1.64;
    const color = i < 4 ? C.mintDark : i < 6 ? C.gold : C.coral;
    s.addShape(pptx.ShapeType.ellipse, {
      x,
      y: 2.87,
      w: 0.62,
      h: 0.62,
      fill: { color },
      line: { color, transparency: 100 },
    });
    s.addText(d, {
      x,
      y: 3.05,
      w: 0.62,
      h: 0.12,
      fontFace: fontH,
      fontSize: 8,
      bold: true,
      color: C.white,
      align: "center",
      margin: 0,
    });
    s.addText(title, {
      x: x - 0.12,
      y: 3.78,
      w: 1.28,
      h: 0.3,
      fontFace: fontH,
      fontSize: 11,
      bold: true,
      color: C.ink,
      align: "center",
      margin: 0,
      fit: "shrink",
    });
    s.addText(proof, {
      x: x - 0.22,
      y: 4.32,
      w: 1.48,
      h: 0.34,
      fontFace: fontB,
      fontSize: 9.4,
      color: C.muted,
      align: "center",
      margin: 0,
      fit: "shrink",
    });
  });
  s.addText("节奏建议", {
    x: 1.0,
    y: 5.62,
    w: 1.05,
    h: 0.22,
    fontFace: fontH,
    fontSize: 12,
    bold: true,
    color: C.coral,
    margin: 0,
  });
  s.addText("每天 45-60 分钟。遇到安装问题时，先记录现象和命令输出，不急着跳到训练。", {
    x: 2.12,
    y: 5.62,
    w: 8.45,
    h: 0.25,
    fontFace: fontB,
    fontSize: 11.3,
    color: C.ink2,
    margin: 0,
    fit: "shrink",
  });
}

// Slide 5
{
  const s = pptx.addSlide();
  addBg(s, C.paper2);
  addTitle(s, "环境搭建命令：一行一行跑", "先确认 Python 入口，再创建隔离环境，最后运行检查脚本。", 5);
  terminal(s, 0.88, 2.06, 6.15, 3.88, [
    "python --version",
    "where.exe python",
    "",
    "python -m venv .venv",
    ".\\.venv\\Scripts\\Activate.ps1",
    "python -m pip install -U pip",
    "pip install -r requirements.txt",
    "python scripts/check_environment.py",
  ], "PowerShell");
  const notes = [
    ["看见版本号", "如果只有 WindowsApps 路径，多半是商店占位入口。"],
    ["激活 .venv", "命令行前面出现 (.venv) 后再安装依赖。"],
    ["保存输出", "把检查结果放进 notes/week_01.md。"],
  ];
  notes.forEach(([a, b], i) => {
    const y = 2.18 + i * 1.15;
    s.addShape(pptx.ShapeType.line, { x: 7.48, y: y + 0.13, w: 0.55, h: 0, line: { color: C.gold, width: 2.5 } });
    s.addText(a, { x: 8.18, y, w: 2.2, h: 0.25, fontFace: fontH, fontSize: 14, bold: true, color: C.ink, margin: 0 });
    s.addText(b, { x: 8.18, y: y + 0.42, w: 3.35, h: 0.38, fontFace: fontB, fontSize: 10.6, color: C.muted, margin: 0, fit: "shrink" });
  });
  s.addText("本页是第一周最重要的操作页。跑不通也没关系，问题记录本身就是本周产物。", {
    x: 7.48,
    y: 5.82,
    w: 4.35,
    h: 0.38,
    fontFace: fontH,
    fontSize: 13.2,
    bold: true,
    color: C.mintDark,
    margin: 0,
    fit: "shrink",
  });
}

// Slide 6
{
  const s = pptx.addSlide();
  addBg(s);
  addTitle(s, "够用的 Python：只学会读懂脚本入口", "第一周不学算法，只补能运行脚本、改参数、看路径的能力。", 6);
  const items = [
    ["变量", 'model_path = "yolo11n.pt"'],
    ["函数", "def main():"],
    ["列表", 'classes = ["phone", "cup"]'],
    ["字典", 'metrics = {"map50": 0.72}'],
    ["路径", "Path('data/samples')"],
    ["参数", "argparse.ArgumentParser()"],
  ];
  items.forEach(([label, code], i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = col === 0 ? 1.0 : 6.9;
    const y = 2.08 + row * 1.15;
    addChip(s, label, x, y, 0.9, col === 0 ? C.mintDark : C.coral);
    s.addText(code, {
      x: x + 1.18,
      y: y + 0.03,
      w: 4.45,
      h: 0.26,
      fontFace: "Consolas",
      fontSize: 13,
      color: C.ink,
      margin: 0,
      fit: "shrink",
    });
    addRule(s, x + 1.18, y + 0.52, 4.4, "E1D6C1", 0.8);
  });
  s.addText("检查自己是否够用", {
    x: 1.0,
    y: 6.05,
    w: 1.65,
    h: 0.23,
    fontFace: fontH,
    fontSize: 12.2,
    bold: true,
    color: C.ink,
    margin: 0,
  });
  s.addText("能打开 `scripts/check_environment.py`，大概说出每一段在检查什么，就达标了。", {
    x: 2.9,
    y: 6.05,
    w: 7.7,
    h: 0.25,
    fontFace: fontB,
    fontSize: 11.2,
    color: C.muted,
    margin: 0,
    fit: "shrink",
  });
}

// Slide 7
{
  const s = pptx.addSlide();
  addBg(s, C.paper2);
  addTitle(s, "本周作业：交付环境证据", "不交模型文件，交一份能复盘的环境记录。", 7);
  const rows = [
    ["1", "运行环境检查", "python scripts/check_environment.py"],
    ["2", "保存关键输出", "Python / Torch / Ultralytics / CUDA"],
    ["3", "写学习复盘", "notes/week_01.md"],
    ["4", "列出阻塞问题", "错误信息、已尝试命令、下一步"],
  ];
  rows.forEach(([num, a, b], i) => {
    const y = 2.02 + i * 0.82;
    s.addText(num, {
      x: 1.0,
      y,
      w: 0.35,
      h: 0.24,
      fontFace: fontH,
      fontSize: 12,
      bold: true,
      color: i === 3 ? C.coral : C.mintDark,
      margin: 0,
      align: "center",
    });
    s.addShape(pptx.ShapeType.line, { x: 1.52, y: y + 0.11, w: 9.9, h: 0, line: { color: "E0D5BF", width: 0.8 } });
    s.addText(a, { x: 1.72, y, w: 2.6, h: 0.24, fontFace: fontH, fontSize: 13, bold: true, color: C.ink, margin: 0 });
    s.addText(b, { x: 4.45, y, w: 5.8, h: 0.24, fontFace: fontB, fontSize: 11.2, color: C.muted, margin: 0, fit: "shrink" });
  });
  s.addShape(pptx.ShapeType.rect, {
    x: 1.0,
    y: 5.68,
    w: 10.2,
    h: 0.72,
    fill: { color: "E8F5F1" },
    line: { color: "B6DDD3", width: 1 },
  });
  s.addText("通过标准", {
    x: 1.28,
    y: 5.91,
    w: 1.1,
    h: 0.2,
    fontFace: fontH,
    fontSize: 11,
    bold: true,
    color: C.mintDark,
    margin: 0,
  });
  s.addText("你能解释虚拟环境的作用，也知道当前电脑适合本地轻量测试还是需要云端训练。", {
    x: 2.48,
    y: 5.91,
    w: 7.8,
    h: 0.2,
    fontFace: fontB,
    fontSize: 10.8,
    color: C.ink2,
    margin: 0,
    fit: "shrink",
  });
}

// Slide 8
{
  const s = pptx.addSlide();
  addBg(s, C.navy);
  s.addText("完成定义", {
    x: 0.86,
    y: 0.72,
    w: 2.05,
    h: 0.3,
    fontFace: fontH,
    fontSize: 16,
    bold: true,
    color: C.gold,
    margin: 0,
  });
  s.addText("第一周结束时，你不需要有模型成果。", {
    x: 0.86,
    y: 1.45,
    w: 8.4,
    h: 0.55,
    fontFace: fontH,
    fontSize: 28,
    bold: true,
    color: C.white,
    margin: 0,
    fit: "shrink",
  });
  s.addText("你只需要有一个可复现的学习环境、一份环境记录，以及继续进入第 2 周的信心。", {
    x: 0.9,
    y: 2.38,
    w: 7.2,
    h: 0.42,
    fontFace: fontB,
    fontSize: 15,
    color: "D7EDE8",
    margin: 0,
    fit: "shrink",
  });
  const checks = [
    "Python 入口正确",
    ".venv 可激活",
    "依赖安装有记录",
    "check_environment.py 已运行",
    "notes/week_01.md 已写",
  ];
  checks.forEach((text, i) => {
    const y = 3.5 + i * 0.47;
    dot(s, 0.98, y + 0.03, C.mint, 0.12);
    s.addText(text, {
      x: 1.25,
      y,
      w: 3.8,
      h: 0.22,
      fontFace: fontB,
      fontSize: 12,
      color: C.white,
      margin: 0,
    });
  });
  s.addShape(pptx.ShapeType.rect, {
    x: 8.7,
    y: 1.2,
    w: 3.45,
    h: 4.8,
    fill: { color: C.paper },
    line: { color: C.paper, transparency: 100 },
  });
  s.addText("下一周", {
    x: 9.12,
    y: 1.72,
    w: 1.2,
    h: 0.22,
    fontFace: fontH,
    fontSize: 12,
    bold: true,
    color: C.coral,
    margin: 0,
  });
  s.addText("目标检测基础", {
    x: 9.12,
    y: 2.12,
    w: 2.55,
    h: 0.4,
    fontFace: fontH,
    fontSize: 21,
    bold: true,
    color: C.ink,
    margin: 0,
    fit: "shrink",
  });
  s.addText("开始理解 bounding box、confidence、IoU、mAP，以及模型为什么会漏检或误检。", {
    x: 9.14,
    y: 2.95,
    w: 2.52,
    h: 1.0,
    fontFace: fontB,
    fontSize: 12,
    color: C.ink2,
    margin: 0,
    fit: "shrink",
    breakLine: false,
  });
  addChip(s, "READY FOR WEEK 02", 9.14, 4.9, 2.2, C.mintDark);
  s.addText("08", {
    x: 11.45,
    y: 6.72,
    w: 0.45,
    h: 0.18,
    fontFace: fontB,
    fontSize: 8.5,
    color: C.paper,
    margin: 0,
  });
}

pptx
  .writeFile({ fileName: path.join(outDir, "week_01_yolo_learning_plan.pptx") })
  .then(() => {
    console.log(path.join(outDir, "week_01_yolo_learning_plan.pptx"));
  });
