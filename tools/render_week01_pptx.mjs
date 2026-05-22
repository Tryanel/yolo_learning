import { FileBlob, PresentationFile } from "file:///C:/Users/Cat/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";
import fs from "node:fs/promises";
import path from "node:path";

const deckPath = path.resolve("slides/week_01_yolo_learning_plan.pptx");
const outDir = path.resolve("slides/previews/week_01");
await fs.mkdir(outDir, { recursive: true });

const deckBlob = await FileBlob.load(deckPath);
const presentation = await PresentationFile.importPptx(deckBlob);

const layoutReport = [];
for (let i = 0; i < presentation.slides.count; i += 1) {
  const slide = presentation.slides.getItem(i);
  const png = await slide.export({ format: "png", scale: 1 });
  const pngPath = path.join(outDir, `slide_${String(i + 1).padStart(2, "0")}.png`);
  await fs.writeFile(pngPath, Buffer.from(await png.arrayBuffer()));

  const layout = await slide.export({ format: "layout" });
  layoutReport.push({ slide: i + 1, layout });
}

await fs.writeFile(
  path.join(outDir, "layout_report.json"),
  JSON.stringify(layoutReport, null, 2),
  "utf8",
);

console.log(`Rendered ${presentation.slides.count} slides to ${outDir}`);
