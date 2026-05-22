from __future__ import annotations

from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "docs" / "assets"


def write_svg(name: str, body: str) -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    (ASSET_DIR / name).write_text(dedent(body).strip() + "\n", encoding="utf-8")


def build_lab_workflow() -> None:
    write_svg(
        "lab_workflow.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="520" viewBox="0 0 1200 520" role="img" aria-labelledby="title desc">
          <title id="title">YOLO Learning Lab workflow</title>
          <desc id="desc">A lab workflow from reading, doing tasks, grading, hand-in, and reflection.</desc>
          <defs>
            <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
              <path d="M2,2 L10,6 L2,10 Z" fill="#0f766e"/>
            </marker>
            <style>
              .bg{fill:#f7f3ea}.ink{fill:#172026}.muted{fill:#667085}.teal{fill:#0f766e}.mint{fill:#e8f5f1}.coral{fill:#f36f45}.gold{fill:#f4b942}
              .card{fill:#fffdf7;stroke:#d8cdb8;stroke-width:2}.num{font:700 30px 'Microsoft YaHei',Arial,sans-serif;fill:#fff}
              .title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.label{font:700 24px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}
              .body{font:18px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.code{font:18px Consolas,monospace;fill:#0f766e}
              .arrow{stroke:#0f766e;stroke-width:4;fill:none;marker-end:url(#arrow)}
            </style>
          </defs>
          <rect class="bg" width="1200" height="520"/>
          <text x="70" y="70" class="title">实验驱动学习闭环</text>
          <text x="70" y="106" class="body">每个 lab 都产生可检查的证据，而不是只留下“我看过了”。</text>
          <g transform="translate(70,165)">
            <rect class="card" x="0" y="0" width="180" height="180" rx="18"/>
            <circle cx="38" cy="42" r="24" class="teal"/><text x="29" y="52" class="num">1</text>
            <text x="28" y="100" class="label">阅读</text>
            <text x="28" y="135" class="body">教材章节</text>
            <text x="28" y="162" class="code">docs/textbook</text>
          </g>
          <path class="arrow" d="M270 255 H340"/>
          <g transform="translate(360,165)">
            <rect class="card" x="0" y="0" width="180" height="180" rx="18"/>
            <circle cx="38" cy="42" r="24" class="coral"/><text x="29" y="52" class="num">2</text>
            <text x="28" y="100" class="label">实验</text>
            <text x="28" y="135" class="body">运行命令</text>
            <text x="28" y="162" class="code">labs/labXX</text>
          </g>
          <path class="arrow" d="M560 255 H630"/>
          <g transform="translate(650,165)">
            <rect class="card" x="0" y="0" width="180" height="180" rx="18"/>
            <circle cx="38" cy="42" r="24" class="gold"/><text x="29" y="52" class="num">3</text>
            <text x="28" y="100" class="label">检查</text>
            <text x="28" y="135" class="body">自动评分</text>
            <text x="28" y="162" class="code">grade labXX</text>
          </g>
          <path class="arrow" d="M850 255 H920"/>
          <g transform="translate(940,165)">
            <rect class="card" x="0" y="0" width="180" height="180" rx="18"/>
            <circle cx="38" cy="42" r="24" class="teal"/><text x="29" y="52" class="num">4</text>
            <text x="28" y="100" class="label">提交</text>
            <text x="28" y="135" class="body">打包证据</text>
            <text x="28" y="162" class="code">handin labXX</text>
          </g>
          <path d="M1030 365 C870 455 300 455 160 365" stroke="#f36f45" stroke-width="4" fill="none" marker-end="url(#arrow)"/>
          <text x="455" y="447" class="body">复盘失败案例，进入下一轮数据和模型改进</text>
        </svg>
        """,
    )


def build_yolo_pipeline() -> None:
    write_svg(
        "yolo_pipeline.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="560" viewBox="0 0 1200 560" role="img" aria-labelledby="title desc">
          <title id="title">YOLO detection pipeline</title>
          <desc id="desc">Image enters the model, features are extracted, predictions are post-processed, and final boxes are produced.</desc>
          <defs>
            <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M2,2 L10,6 L2,10 Z" fill="#16324f"/></marker>
            <style>
              .bg{fill:#fffdf7}.ink{fill:#172026}.muted{fill:#667085}.navy{fill:#16324f}.teal{fill:#0f766e}.mint{fill:#e8f5f1}.orange{fill:#fff1e8;stroke:#f4c5a9;stroke-width:2}
              .card{fill:#f7f3ea;stroke:#d8cdb8;stroke-width:2}.title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}
              .label{font:700 22px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.body{font:17px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}
              .small{font:14px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.arrow{stroke:#16324f;stroke-width:4;fill:none;marker-end:url(#arrow)}
            </style>
          </defs>
          <rect class="bg" width="1200" height="560"/>
          <text x="70" y="72" class="title">YOLO 目标检测流水线</text>
          <text x="70" y="108" class="body">把模型看成一个系统：输入图片，输出带类别和置信度的检测框。</text>
          <g transform="translate(70,175)">
            <rect class="card" width="180" height="230" rx="18"/>
            <rect x="35" y="42" width="110" height="82" rx="10" fill="#dbeafe" stroke="#93c5fd" stroke-width="2"/>
            <circle cx="72" cy="76" r="16" fill="#f59e0b"/><rect x="96" y="88" width="32" height="24" fill="#0f766e"/>
            <text x="34" y="165" class="label">Image</text>
            <text x="34" y="195" class="small">原始图片或视频帧</text>
          </g>
          <path class="arrow" d="M270 290 H330"/>
          <g transform="translate(350,175)">
            <rect class="card" width="190" height="230" rx="18"/>
            <rect x="36" y="38" width="118" height="35" rx="8" fill="#e8f5f1"/>
            <rect x="52" y="82" width="86" height="35" rx="8" fill="#cdeee7"/>
            <rect x="66" y="126" width="58" height="35" rx="8" fill="#9de0d3"/>
            <text x="34" y="182" class="label">Backbone</text>
            <text x="34" y="210" class="small">提取边缘、纹理、形状</text>
          </g>
          <path class="arrow" d="M560 290 H620"/>
          <g transform="translate(640,175)">
            <rect class="card" width="190" height="230" rx="18"/>
            <path d="M48 55 H142 M48 95 H142 M48 135 H142" stroke="#0f766e" stroke-width="8" stroke-linecap="round"/>
            <path d="M64 55 C95 72 104 82 128 95 M64 135 C95 118 104 108 128 95" stroke="#f36f45" stroke-width="5" fill="none"/>
            <text x="34" y="182" class="label">Neck</text>
            <text x="34" y="210" class="small">融合不同尺度特征</text>
          </g>
          <path class="arrow" d="M850 290 H910"/>
          <g transform="translate(930,175)">
            <rect class="orange" width="200" height="230" rx="18"/>
            <rect x="36" y="46" width="126" height="78" fill="none" stroke="#f36f45" stroke-width="5"/>
            <text x="43" y="42" class="small">cup 0.91</text>
            <rect x="72" y="84" width="76" height="50" fill="none" stroke="#0f766e" stroke-width="5"/>
            <text x="76" y="157" class="small">phone 0.84</text>
            <text x="34" y="190" class="label">Head + NMS</text>
            <text x="34" y="216" class="small">框、类别、置信度</text>
          </g>
        </svg>
        """,
    )


def build_box_iou_nms() -> None:
    write_svg(
        "box_iou_nms.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="620" viewBox="0 0 1200 620" role="img" aria-labelledby="title desc">
          <title id="title">Bounding box, IoU and NMS</title>
          <desc id="desc">A visual explanation of YOLO normalized boxes, intersection over union, and duplicate suppression.</desc>
          <style>
            .bg{fill:#f7f3ea}.ink{fill:#172026}.muted{fill:#667085}.teal{stroke:#0f766e}.coral{stroke:#f36f45}.gold{fill:#f4b942}
            .title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.label{font:700 22px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}
            .body{font:17px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.code{font:18px Consolas,monospace;fill:#16324f}
            .panel{fill:#fffdf7;stroke:#d8cdb8;stroke-width:2}.box{fill:none;stroke-width:5}.thin{stroke:#d8cdb8;stroke-width:2}
          </style>
          <rect class="bg" width="1200" height="620"/>
          <text x="70" y="70" class="title">检测框、IoU 与 NMS</text>
          <text x="70" y="106" class="body">YOLO 的结果不是一个标签，而是一组几何对象。</text>
          <g transform="translate(70,155)">
            <rect class="panel" width="320" height="360" rx="18"/>
            <text x="28" y="45" class="label">1. YOLO 标签格式</text>
            <rect x="62" y="90" width="190" height="145" fill="#dbeafe" stroke="#93c5fd" stroke-width="2"/>
            <rect x="112" y="125" width="92" height="70" class="box teal"/>
            <circle cx="158" cy="160" r="6" fill="#f36f45"/>
            <line x1="158" y1="160" x2="158" y2="250" class="thin"/><line x1="158" y1="160" x2="272" y2="160" class="thin"/>
            <text x="36" y="280" class="code">class x y w h</text>
            <text x="36" y="314" class="body">坐标是 0 到 1 的比例</text>
          </g>
          <g transform="translate(440,155)">
            <rect class="panel" width="320" height="360" rx="18"/>
            <text x="28" y="45" class="label">2. IoU 衡量重叠</text>
            <rect x="80" y="105" width="130" height="110" class="box teal"/>
            <rect x="130" y="145" width="130" height="110" class="box coral"/>
            <rect x="130" y="145" width="80" height="70" fill="#f4b942" fill-opacity="0.55"/>
            <text x="60" y="290" class="code">IoU = intersection / union</text>
            <text x="52" y="324" class="body">越接近 1，两个框越一致</text>
          </g>
          <g transform="translate(810,155)">
            <rect class="panel" width="320" height="360" rx="18"/>
            <text x="28" y="45" class="label">3. NMS 去重</text>
            <rect x="72" y="110" width="150" height="105" class="box teal"/>
            <rect x="93" y="128" width="150" height="105" class="box coral" opacity="0.55"/>
            <rect x="112" y="146" width="150" height="105" class="box coral" opacity="0.32"/>
            <text x="55" y="295" class="body">保留最高置信度框</text>
            <text x="55" y="326" class="body">删除高度重叠的重复框</text>
          </g>
        </svg>
        """,
    )


def build_dataset_layout() -> None:
    write_svg(
        "dataset_layout.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="640" viewBox="0 0 1200 640" role="img" aria-labelledby="title desc">
          <title id="title">YOLO dataset layout</title>
          <desc id="desc">A folder tree showing image folders, label folders, and dataset.yaml.</desc>
          <style>
            .bg{fill:#fffdf7}.ink{fill:#172026}.muted{fill:#667085}.teal{fill:#0f766e}.mint{fill:#e8f5f1}.orange{fill:#fff1e8}.line{stroke:#d8cdb8;stroke-width:2}
            .title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.label{font:700 22px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}
            .body{font:17px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.code{font:18px Consolas,monospace;fill:#16324f}
            .folder{fill:#f7f3ea;stroke:#d8cdb8;stroke-width:2}.yaml{fill:#e8f5f1;stroke:#9de0d3;stroke-width:2}
          </style>
          <rect class="bg" width="1200" height="640"/>
          <text x="70" y="70" class="title">YOLO 数据集结构</text>
          <text x="70" y="106" class="body">图片和标签必须成对组织，dataset.yaml 是训练入口。</text>
          <g transform="translate(90,160)">
            <rect class="folder" x="0" y="0" width="450" height="390" rx="18"/>
            <text x="32" y="48" class="label">data/yolo_dataset/</text>
            <line x1="58" y1="80" x2="58" y2="330" class="line"/>
            <text x="88" y="102" class="code">images/</text>
            <text x="128" y="142" class="code">train/</text>
            <text x="128" y="182" class="code">val/</text>
            <text x="128" y="222" class="code">test/</text>
            <text x="88" y="282" class="code">labels/</text>
            <text x="128" y="322" class="code">train/ val/ test/</text>
          </g>
          <g transform="translate(640,160)">
            <rect class="yaml" width="430" height="390" rx="18"/>
            <text x="32" y="48" class="label">dataset.yaml</text>
            <text x="38" y="98" class="code">path: data/yolo_dataset</text>
            <text x="38" y="138" class="code">train: images/train</text>
            <text x="38" y="178" class="code">val: images/val</text>
            <text x="38" y="218" class="code">test: images/test</text>
            <text x="38" y="278" class="code">names:</text>
            <text x="72" y="318" class="code">0: phone</text>
            <text x="72" y="358" class="code">1: cup</text>
          </g>
          <path d="M550 350 C585 350 600 350 630 350" stroke="#f36f45" stroke-width="5" fill="none"/>
          <polygon points="630,350 612,340 612,360" fill="#f36f45"/>
        </svg>
        """,
    )


def build_local_cloud_workflow() -> None:
    write_svg(
        "local_cloud_workflow.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="580" viewBox="0 0 1200 580" role="img" aria-labelledby="title desc">
          <title id="title">Local-light and cloud-heavy YOLO workflow</title>
          <desc id="desc">A split workflow showing local repo, dataset work, cloud training, and hosted demo.</desc>
          <style>
            .bg{fill:#f7f3ea}.ink{fill:#172026}.muted{fill:#667085}.teal{fill:#0f766e}.coral{fill:#f36f45}.gold{fill:#f4b942}
            .local{fill:#e8f5f1;stroke:#9de0d3;stroke-width:2}.cloud{fill:#fff1e8;stroke:#f4c5a9;stroke-width:2}
            .title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.label{font:700 25px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}
            .body{font:18px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.item{font:700 19px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}
            .arrow{stroke:#16324f;stroke-width:4;fill:none}
          </style>
          <rect class="bg" width="1200" height="580"/>
          <text x="70" y="70" class="title">本地轻量 + 云端训练/部署</text>
          <text x="70" y="106" class="body">弱电脑也能完整学习 YOLO：把算力任务放到云端，把可复现工作留在本地。</text>
          <rect x="80" y="165" width="465" height="300" rx="22" class="local"/>
          <text x="120" y="218" class="label">本地电脑</text>
          <circle cx="130" cy="265" r="7" class="teal"/><text x="155" y="272" class="item">写代码与笔记</text>
          <circle cx="130" cy="315" r="7" class="teal"/><text x="155" y="322" class="item">整理 dataset.yaml</text>
          <circle cx="130" cy="365" r="7" class="teal"/><text x="155" y="372" class="item">少量图片预测</text>
          <circle cx="130" cy="415" r="7" class="teal"/><text x="155" y="422" class="item">记录错误案例</text>
          <rect x="655" y="165" width="465" height="300" rx="22" class="cloud"/>
          <text x="695" y="218" class="label">云端资源</text>
          <circle cx="705" cy="265" r="7" class="coral"/><text x="730" y="272" class="item">GPU 训练</text>
          <circle cx="705" cy="315" r="7" class="coral"/><text x="730" y="322" class="item">批量验证</text>
          <circle cx="705" cy="365" r="7" class="coral"/><text x="730" y="372" class="item">在线 Demo</text>
          <circle cx="705" cy="415" r="7" class="coral"/><text x="730" y="422" class="item">托管 API</text>
          <path d="M560 300 H640" class="arrow"/><polygon points="640,300 620,289 620,311" fill="#16324f"/>
          <path d="M640 350 H560" class="arrow"/><polygon points="560,350 580,339 580,361" fill="#16324f"/>
          <text x="515" y="270" class="body">数据上传</text>
          <text x="505" y="395" class="body">权重下载</text>
        </svg>
        """,
    )


def build_error_matrix() -> None:
    write_svg(
        "error_analysis_matrix.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="680" viewBox="0 0 1200 680" role="img" aria-labelledby="title desc">
          <title id="title">YOLO error analysis matrix</title>
          <desc id="desc">A matrix of common detection errors and recommended dataset actions.</desc>
          <style>
            .bg{fill:#fffdf7}.ink{fill:#172026}.muted{fill:#667085}.teal{fill:#0f766e}.coral{fill:#f36f45}.gold{fill:#f4b942}
            .title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.body{font:17px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}
            .head{font:700 21px 'Microsoft YaHei',Arial,sans-serif;fill:#fff}.celltitle{font:700 20px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}
            .cellbody{font:16px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.grid{stroke:#d8cdb8;stroke-width:2}.cell{fill:#f7f3ea}
          </style>
          <rect class="bg" width="1200" height="680"/>
          <text x="70" y="70" class="title">错误案例分析矩阵</text>
          <text x="70" y="106" class="body">不要只看 mAP。把错误分桶，才能知道下一轮该补什么数据。</text>
          <g transform="translate(80,160)">
            <rect x="0" y="0" width="1040" height="58" fill="#16324f"/>
            <text x="35" y="38" class="head">错误类型</text>
            <text x="355" y="38" class="head">常见现象</text>
            <text x="720" y="38" class="head">下一步动作</text>
            <g transform="translate(0,58)">
              <rect class="cell grid" width="1040" height="72"/><text x="35" y="43" class="celltitle">漏检</text><text x="355" y="43" class="cellbody">目标存在但没有框</text><text x="720" y="43" class="cellbody">补相似样本，检查阈值</text>
              <rect class="cell grid" y="72" width="1040" height="72"/><text x="35" y="115" class="celltitle">误检</text><text x="355" y="115" class="cellbody">背景被当成目标</text><text x="720" y="115" class="cellbody">添加 hard negative</text>
              <rect class="cell grid" y="144" width="1040" height="72"/><text x="35" y="187" class="celltitle">框不准</text><text x="355" y="187" class="cellbody">类别对，位置差</text><text x="720" y="187" class="cellbody">修标签，增加分辨率</text>
              <rect class="cell grid" y="216" width="1040" height="72"/><text x="35" y="259" class="celltitle">类别错</text><text x="355" y="259" class="cellbody">A 被识别成 B</text><text x="720" y="259" class="cellbody">澄清类别定义，补样本</text>
              <rect class="cell grid" y="288" width="1040" height="72"/><text x="35" y="331" class="celltitle">域偏移</text><text x="355" y="331" class="cellbody">新场景整体变差</text><text x="720" y="331" class="cellbody">采集目标场景数据</text>
            </g>
          </g>
        </svg>
        """,
    )


def build_feature_pyramid() -> None:
    write_svg(
        "feature_pyramid.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="650" viewBox="0 0 1200 650" role="img" aria-labelledby="title desc">
          <title id="title">Feature pyramid and multi-scale detection</title>
          <desc id="desc">An input image becomes feature maps at multiple scales for small, medium, and large object detection.</desc>
          <defs>
            <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M2,2 L10,6 L2,10 Z" fill="#16324f"/></marker>
            <style>
              .bg{fill:#fffdf7}.title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.body{font:18px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}
              .label{font:700 22px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.small{font:16px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}
              .panel{fill:#f7f3ea;stroke:#d8cdb8;stroke-width:2}.map{fill:#e8f5f1;stroke:#0f766e;stroke-width:3}.grid{stroke:#9de0d3;stroke-width:1}
              .arrow{stroke:#16324f;stroke-width:4;fill:none;marker-end:url(#arrow)}
            </style>
          </defs>
          <rect class="bg" width="1200" height="650"/>
          <text x="70" y="72" class="title">特征图与多尺度检测</text>
          <text x="70" y="108" class="body">图片经过主干网络后变成不同大小的特征图：高分辨率保留细节，低分辨率语义更强。</text>
          <g transform="translate(80,170)">
            <rect class="panel" width="260" height="310" rx="18"/>
            <rect x="48" y="56" width="164" height="120" rx="8" fill="#dbeafe" stroke="#93c5fd" stroke-width="2"/>
            <circle cx="92" cy="96" r="18" fill="#f4b942"/>
            <rect x="130" y="118" width="50" height="34" fill="#0f766e"/>
            <text x="45" y="225" class="label">输入图片</text>
            <text x="45" y="260" class="small">像素级信息最多</text>
          </g>
          <path class="arrow" d="M360 325 H455"/>
          <g transform="translate(485,145)">
            <rect class="panel" width="610" height="370" rx="22"/>
            <text x="38" y="52" class="label">Feature Pyramid</text>
            <text x="38" y="86" class="small">同一张图片被压缩成多种尺度的线索地图</text>
            <g transform="translate(60,125)">
              <rect class="map" width="170" height="170" rx="8"/>
              <path class="grid" d="M34 0 V170 M68 0 V170 M102 0 V170 M136 0 V170 M0 34 H170 M0 68 H170 M0 102 H170 M0 136 H170"/>
              <text x="18" y="215" class="label">P3 细节多</text>
              <text x="18" y="245" class="small">适合小目标</text>
            </g>
            <g transform="translate(270,150)">
              <rect class="map" width="130" height="130" rx="8"/>
              <path class="grid" d="M32 0 V130 M64 0 V130 M96 0 V130 M0 32 H130 M0 64 H130 M0 96 H130"/>
              <text x="0" y="190" class="label">P4 平衡</text>
              <text x="0" y="220" class="small">适合中等目标</text>
            </g>
            <g transform="translate(455,175)">
              <rect class="map" width="90" height="90" rx="8"/>
              <path class="grid" d="M30 0 V90 M60 0 V90 M0 30 H90 M0 60 H90"/>
              <text x="-8" y="165" class="label">P5 语义强</text>
              <text x="-8" y="195" class="small">适合大目标</text>
            </g>
          </g>
        </svg>
        """,
    )


def build_detection_head_outputs() -> None:
    write_svg(
        "detection_head_outputs.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="660" viewBox="0 0 1200 660" role="img" aria-labelledby="title desc">
          <title id="title">Detection head outputs</title>
          <desc id="desc">Feature map locations produce candidate boxes with class scores and confidence, then thresholds and NMS produce final detections.</desc>
          <defs>
            <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M2,2 L10,6 L2,10 Z" fill="#16324f"/></marker>
            <style>
              .bg{fill:#f7f3ea}.title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.body{font:18px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}
              .label{font:700 22px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.small{font:16px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.code{font:18px Consolas,monospace;fill:#16324f}
              .panel{fill:#fffdf7;stroke:#d8cdb8;stroke-width:2}.grid{fill:#e8f5f1;stroke:#0f766e;stroke-width:3}.line{stroke:#9de0d3;stroke-width:1}.arrow{stroke:#16324f;stroke-width:4;fill:none;marker-end:url(#arrow)}
              .chip{fill:#fff1e8;stroke:#f4c5a9;stroke-width:2}
            </style>
          </defs>
          <rect class="bg" width="1200" height="660"/>
          <text x="70" y="72" class="title">检测头输出到底是什么</text>
          <text x="70" y="108" class="body">检测头把特征图上的位置变成候选框，再经过阈值和 NMS 筛选成最终结果。</text>
          <g transform="translate(80,170)">
            <rect class="panel" width="280" height="330" rx="18"/>
            <text x="34" y="48" class="label">特征图位置</text>
            <rect x="58" y="88" width="164" height="164" rx="8" class="grid"/>
            <path class="line" d="M99 88 V252 M140 88 V252 M181 88 V252 M58 129 H222 M58 170 H222 M58 211 H222"/>
            <circle cx="140" cy="170" r="11" fill="#f36f45"/>
            <text x="50" y="292" class="small">每个位置预测若干候选信息</text>
          </g>
          <path class="arrow" d="M380 335 H455"/>
          <g transform="translate(485,170)">
            <rect class="panel" width="300" height="330" rx="18"/>
            <text x="34" y="48" class="label">候选输出</text>
            <rect x="38" y="82" width="225" height="48" rx="10" class="chip"/><text x="58" y="113" class="code">box: x y w h</text>
            <rect x="38" y="150" width="225" height="48" rx="10" class="chip"/><text x="58" y="181" class="code">class scores</text>
            <rect x="38" y="218" width="225" height="48" rx="10" class="chip"/><text x="58" y="249" class="code">confidence</text>
            <text x="38" y="304" class="small">不同实现的细节会变，核心都是“位置 + 类别 + 质量”。</text>
          </g>
          <path class="arrow" d="M805 335 H880"/>
          <g transform="translate(910,170)">
            <rect class="panel" width="230" height="330" rx="18"/>
            <text x="30" y="48" class="label">筛选后结果</text>
            <rect x="42" y="84" width="132" height="82" fill="none" stroke="#f36f45" stroke-width="5"/>
            <text x="47" y="77" class="small">cup 0.91</text>
            <rect x="70" y="142" width="95" height="62" fill="none" stroke="#0f766e" stroke-width="5"/>
            <text x="74" y="229" class="small">phone 0.84</text>
            <text x="34" y="284" class="small">conf 过滤 + NMS 去重</text>
          </g>
        </svg>
        """,
    )


def build_loss_components() -> None:
    write_svg(
        "loss_components.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="640" viewBox="0 0 1200 640" role="img" aria-labelledby="title desc">
          <title id="title">YOLO loss components</title>
          <desc id="desc">Training loss combines box quality, class prediction, and confidence or objectness quality, then updates model weights.</desc>
          <defs>
            <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M2,2 L10,6 L2,10 Z" fill="#16324f"/></marker>
            <style>
              .bg{fill:#fffdf7}.title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.body{font:18px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}
              .label{font:700 22px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.small{font:16px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.code{font:19px Consolas,monospace;fill:#16324f}
              .panel{fill:#f7f3ea;stroke:#d8cdb8;stroke-width:2}.box{fill:none;stroke-width:5}.pred{stroke:#f36f45}.gt{stroke:#0f766e}.arrow{stroke:#16324f;stroke-width:4;fill:none;marker-end:url(#arrow)}
              .barbg{fill:#e8f5f1}.bar1{fill:#0f766e}.bar2{fill:#f36f45}.bar3{fill:#f4b942}
            </style>
          </defs>
          <rect class="bg" width="1200" height="640"/>
          <text x="70" y="72" class="title">损失函数如何推动学习</text>
          <text x="70" y="108" class="body">训练时模型比较“预测”和“标签”的差距，把差距转成 loss，再反向更新参数。</text>
          <g transform="translate(80,175)">
            <rect class="panel" width="270" height="300" rx="18"/>
            <text x="34" y="48" class="label">预测 vs 标签</text>
            <rect x="70" y="95" width="125" height="92" class="box gt"/>
            <rect x="98" y="123" width="125" height="92" class="box pred"/>
            <text x="45" y="248" class="small">绿色：真实框</text>
            <text x="45" y="278" class="small">橙色：预测框</text>
          </g>
          <path class="arrow" d="M370 325 H445"/>
          <g transform="translate(475,175)">
            <rect class="panel" width="300" height="300" rx="18"/>
            <text x="34" y="48" class="label">Loss 组成</text>
            <text x="36" y="98" class="small">框位置 / IoU 质量</text>
            <rect x="36" y="112" width="210" height="20" rx="10" class="barbg"/><rect x="36" y="112" width="150" height="20" rx="10" class="bar1"/>
            <text x="36" y="162" class="small">类别预测</text>
            <rect x="36" y="176" width="210" height="20" rx="10" class="barbg"/><rect x="36" y="176" width="95" height="20" rx="10" class="bar2"/>
            <text x="36" y="226" class="small">置信度 / 目标质量</text>
            <rect x="36" y="240" width="210" height="20" rx="10" class="barbg"/><rect x="36" y="240" width="125" height="20" rx="10" class="bar3"/>
          </g>
          <path class="arrow" d="M795 325 H870"/>
          <g transform="translate(900,175)">
            <rect class="panel" width="230" height="300" rx="18"/>
            <text x="30" y="58" class="label">反向传播</text>
            <text x="30" y="112" class="code">loss ↓</text>
            <text x="30" y="156" class="small">调整模型参数</text>
            <text x="30" y="198" class="small">下一轮预测更接近标签</text>
            <path d="M64 246 C122 205 157 230 168 168" stroke="#0f766e" stroke-width="6" fill="none"/>
            <polygon points="168,168 153,183 174,190" fill="#0f766e"/>
          </g>
        </svg>
        """,
    )


def build_precision_recall_curve() -> None:
    write_svg(
        "precision_recall_curve.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="640" viewBox="0 0 1200 640" role="img" aria-labelledby="title desc">
          <title id="title">Precision-recall curve</title>
          <desc id="desc">A precision-recall curve shows the tradeoff between conservative and permissive confidence thresholds.</desc>
          <style>
            .bg{fill:#f7f3ea}.title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.body{font:18px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}
            .label{font:700 22px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.small{font:16px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.axis{stroke:#172026;stroke-width:3}.grid{stroke:#d8cdb8;stroke-width:1}
            .curve{stroke:#0f766e;stroke-width:7;fill:none}.area{fill:#9de0d3;fill-opacity:.32}.dot{fill:#f36f45}
          </style>
          <rect class="bg" width="1200" height="640"/>
          <text x="70" y="72" class="title">Precision-Recall 曲线</text>
          <text x="70" y="108" class="body">调节置信度阈值，会在“少误检”和“少漏检”之间移动。AP 是曲线下方的综合面积。</text>
          <g transform="translate(120,160)">
            <line x1="0" y1="360" x2="760" y2="360" class="axis"/>
            <line x1="0" y1="360" x2="0" y2="0" class="axis"/>
            <path class="grid" d="M0 288 H760 M0 216 H760 M0 144 H760 M0 72 H760 M152 0 V360 M304 0 V360 M456 0 V360 M608 0 V360"/>
            <path class="area" d="M0 40 C110 48 190 80 280 125 C385 178 470 240 600 300 C675 332 725 346 760 354 L760 360 L0 360 Z"/>
            <path class="curve" d="M0 40 C110 48 190 80 280 125 C385 178 470 240 600 300 C675 332 725 346 760 354"/>
            <circle cx="155" cy="66" r="9" class="dot"/><text x="174" y="62" class="small">高 conf：误检少，召回低</text>
            <circle cx="560" cy="282" r="9" class="dot"/><text x="580" y="280" class="small">低 conf：找得多，误检多</text>
            <text x="333" y="410" class="label">Recall</text>
            <text x="-80" y="185" class="label" transform="rotate(-90 -80 185)">Precision</text>
          </g>
          <g transform="translate(930,215)">
            <text x="0" y="0" class="label">读图方法</text>
            <text x="0" y="45" class="small">曲线越靠右上越好</text>
            <text x="0" y="85" class="small">AP 约等于曲线下面积</text>
            <text x="0" y="125" class="small">不同阈值对应不同点</text>
            <text x="0" y="165" class="small">真实项目要结合误检成本</text>
          </g>
        </svg>
        """,
    )


def build_augmentation_panel() -> None:
    write_svg(
        "augmentation_panel.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="640" viewBox="0 0 1200 640" role="img" aria-labelledby="title desc">
          <title id="title">Data augmentation examples</title>
          <desc id="desc">Common image augmentations used to improve YOLO robustness.</desc>
          <style>
            .bg{fill:#fffdf7}.title{font:700 34px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.body{font:18px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}
            .label{font:700 22px 'Microsoft YaHei',Arial,sans-serif;fill:#172026}.small{font:16px 'Microsoft YaHei',Arial,sans-serif;fill:#667085}.panel{fill:#f7f3ea;stroke:#d8cdb8;stroke-width:2}
            .img{fill:#dbeafe;stroke:#93c5fd;stroke-width:2}.box{fill:none;stroke:#f36f45;stroke-width:5}
          </style>
          <rect class="bg" width="1200" height="640"/>
          <text x="70" y="72" class="title">数据增强在训练中做什么</text>
          <text x="70" y="108" class="body">增强不是凭空创造新类别，而是让模型见到更多光照、尺度、裁剪和组合变化。</text>
          <g transform="translate(80,165)">
            <rect class="panel" width="230" height="310" rx="18"/>
            <rect x="45" y="55" width="140" height="105" rx="8" class="img"/>
            <rect x="80" y="88" width="65" height="48" class="box"/>
            <text x="45" y="215" class="label">原图</text>
            <text x="45" y="250" class="small">真实标注保持不变</text>
          </g>
          <g transform="translate(345,165)">
            <rect class="panel" width="230" height="310" rx="18"/>
            <rect x="45" y="55" width="140" height="105" rx="8" class="img" transform="rotate(-8 115 107)"/>
            <rect x="79" y="86" width="65" height="48" class="box" transform="rotate(-8 111 110)"/>
            <text x="45" y="215" class="label">旋转/缩放</text>
            <text x="45" y="250" class="small">适应角度和距离变化</text>
          </g>
          <g transform="translate(610,165)">
            <rect class="panel" width="230" height="310" rx="18"/>
            <rect x="55" y="52" width="120" height="120" rx="8" fill="#fef3c7" stroke="#f4b942" stroke-width="2"/>
            <line x1="115" y1="52" x2="115" y2="172" stroke="#fffdf7" stroke-width="5"/>
            <line x1="55" y1="112" x2="175" y2="112" stroke="#fffdf7" stroke-width="5"/>
            <rect x="78" y="75" width="42" height="35" class="box"/>
            <text x="45" y="215" class="label">Mosaic</text>
            <text x="45" y="250" class="small">组合多个场景</text>
          </g>
          <g transform="translate(875,165)">
            <rect class="panel" width="230" height="310" rx="18"/>
            <rect x="45" y="55" width="140" height="105" rx="8" fill="#e0f2fe" stroke="#93c5fd" stroke-width="2"/>
            <rect x="80" y="88" width="65" height="48" class="box"/>
            <rect x="45" y="55" width="140" height="105" rx="8" fill="#f36f45" opacity=".18"/>
            <text x="45" y="215" class="label">颜色/亮度</text>
            <text x="45" y="250" class="small">适应光照变化</text>
          </g>
        </svg>
        """,
    )


def main() -> None:
    build_lab_workflow()
    build_yolo_pipeline()
    build_box_iou_nms()
    build_dataset_layout()
    build_local_cloud_workflow()
    build_error_matrix()
    build_feature_pyramid()
    build_detection_head_outputs()
    build_loss_components()
    build_precision_recall_curve()
    build_augmentation_panel()
    print(f"Wrote teaching assets to {ASSET_DIR}")


if __name__ == "__main__":
    main()
