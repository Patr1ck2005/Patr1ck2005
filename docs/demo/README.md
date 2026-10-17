# Three-minute tool tour / 三分钟工具导览

[MP4](research-tools-tour.mp4) · [Local player / 本地播放器](index.html) · [Sources and SHA-256 / 来源与校验](manifest.json) · [Visual guide / 功能图导览](../visual-guide.md)

A **180-second, silent, bilingual captioned walkthrough** of computed synthetic results and an attributed public software frame. It covers input audits, numerical tracking, plotting, combined workflows, scalar optics, GDS and interactive waves. These are result views, not a recording of manual operation or a benchmark. The frames preserve each image's full aspect ratio, axes and legends.

这是 **180 秒、无声、双语字幕的结果导览**，展示实际合成计算和保留来源的公开程序画面，覆盖输入审计、数值追踪、绘图、组合工作流、标量光学、GDS 与互动波场。它不是手工操作录屏或性能测试；图像比例、坐标与图例完整保留。

The manifest pins each public image URL, source hash and chapter duration. The MP4 contains 2,160 frames at 12 fps, 1280 × 960, encoded with PyAV/libx264. The chapter PNGs are editable presentation inputs. No unpublished research or private runtime is included.

Manifest 固定每张公开图片的 URL、源哈希和章节时长。MP4 为 1280 × 960、12 fps、2,160 帧，使用 PyAV/libx264 编码；各章节 PNG 可继续用于演示。不包含未发表研究或私人运行信息。

To rebuild, download the exact source images recorded in `manifest.json`, give each record a local `path` in an input JSON, and run with Pillow, PyAV and PyMuPDF available:

复现时下载 `manifest.json` 记录的精确源图，在输入 JSON 的各条记录中补上本地 `path`，并使用已具备 Pillow、PyAV 和 PyMuPDF 的环境运行：

```bash
python scripts/build_tour.py --inputs tour-inputs.json --font /path/to/a/CJK-font.ttf --out docs/demo
```

Input keys / 输入字段：`path`, `title`, `zh`, `en`, `seconds`, `source_url`, `kind`. Durations must sum to 180 seconds / 时长之和必须为 180 秒。The font must cover Latin and simplified Chinese / 字体需支持英文和简体中文。
