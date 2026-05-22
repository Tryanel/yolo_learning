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


def main() -> None:
    build_lab_workflow()
    build_yolo_pipeline()
    build_box_iou_nms()
    build_dataset_layout()
    build_local_cloud_workflow()
    build_error_matrix()
    print(f"Wrote teaching assets to {ASSET_DIR}")


if __name__ == "__main__":
    main()

