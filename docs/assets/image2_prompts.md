# Optional GPT Image 2 Prompt Bank

The repository uses deterministic SVG diagrams by default. If you later want richer bitmap illustrations, these prompts can be used with GPT Image 2 or another image generation tool. Keep generated outputs under `docs/assets/generated/` and review text carefully before committing.

## YOLO Pipeline Poster

Prompt:

```text
Create a clean educational diagram for a beginner YOLO object detection course. Landscape 16:9. Show the pipeline from image input to backbone feature extraction, multi-scale neck, detection head, NMS, and final bounding boxes. Use a warm paper background, teal and coral accents, minimal labels, no logos, no brand names, crisp vector-like style, readable Chinese labels: 输入图片, 特征提取, 多尺度融合, 检测头, NMS, 输出检测框.
```

## Dataset Anatomy

Prompt:

```text
Create a modern textbook-style diagram explaining YOLO dataset structure. Landscape 16:9. Show folders images/train, images/val, labels/train, labels/val, plus dataset.yaml. Include a small example label line "0 0.52 0.43 0.21 0.31". Warm neutral background, teal highlights, no photorealistic people, no logos, crisp readable Chinese text.
```

## Error Analysis Board

Prompt:

```text
Create an educational visual board for YOLO error analysis. Landscape 16:9. Show five error buckets: 漏检, 误检, 框不准, 类别错, 域偏移. For each, include a small simple icon-like example and a short next action. Clean classroom handout style, high contrast, no external brand logos, readable Chinese text.
```

