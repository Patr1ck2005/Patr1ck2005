# Verified downloads / 已核验下载

[Project directory / 作品目录](../README.md) · [Visual guide / 功能图](visual-guide.md)

These GitHub Releases contain wheels built from the recorded public commits, standalone synthetic-example ZIPs, public provenance and SHA-256 checksums. All 16 uploaded assets were downloaded again and checked. The `showcase-2026-10-17` tags identify the exact showcase source; runtime package versions remain unchanged. This is not a PyPI release.

这些 GitHub Release 提供从明确公开提交构建的 wheel、独立合成示例 ZIP、公开来源和 SHA-256 校验。16 个上传附件均已重新下载核对。`showcase-2026-10-17` 标签标识展示源码，运行时包版本保持不变；没有发布到 PyPI。

| Package / 包 | Version / 版本 | Release and files / 下载 |
|---|---|---|
| eigenmode-analysis | 0.2.10 | [Release](https://github.com/Patr1ck2005/eigenmode-analysis/releases/tag/showcase-2026-10-17) |
| campaign-data | 0.2.0 | [Release](https://github.com/Patr1ck2005/campaign-data/releases/tag/showcase-2026-10-17) |
| plot-foundation | 0.1.13 | [Release](https://github.com/Patr1ck2005/plot-foundation/releases/tag/showcase-2026-10-17) |
| plot-workflows | 0.1.7 | [Release](https://github.com/Patr1ck2005/plot-workflows/releases/tag/showcase-2026-10-17) |

Download the four wheels into one directory. Use Python 3.10+ in a fresh environment, activate it for your shell, then run:

将四个 wheel 下载到同一目录。使用 Python 3.10+ 新建环境，按所用终端激活后运行：

```bash
python -m venv .venv
# Activate the environment before the next command / 先激活环境
python -m pip install "matplotlib==3.10.9" ./eigenmode_analysis-0.2.10-py3-none-any.whl ./campaign_data-0.2.0-py3-none-any.whl ./plot_foundation-0.1.13-py3-none-any.whl "./plot_workflows-0.1.7-py3-none-any.whl[multislice]"
python -m pip check
```

Unpack the Plot Workflows synthetic-showcase ZIP. From its example root, run `python examples/synthetic_end_to_end.py --out output`. The example creates its own inputs, checks them and writes the gallery. Each ZIP includes reproduction instructions and the source identity. Verify `SHA256SUMS.txt` before use, for example `Get-FileHash <file> -Algorithm SHA256` in PowerShell.

解压 Plot Workflows 的 synthetic-showcase ZIP，从示例根目录运行 `python examples/synthetic_end_to_end.py --out output`。示例自行生成并检查输入，随后写出图集。各 ZIP 都包含复现说明和源码身份。使用前核对 `SHA256SUMS.txt`，例如在 PowerShell 中运行 `Get-FileHash <文件> -Algorithm SHA256`。

**Compatibility / 兼容：** Workflows 0.1.7 multislice currently requires Matplotlib **3.10.9**; 3.11 removed an API it uses. Campaign Data 0.2.0 is an independent file-audit stage: do not request `plot-workflows[campaign]`, which declares `<0.2`. Eigenmode 0.3.1 grouping uses a **separate environment** and is described on its public feature branch. No daily research environment needs to change.

Workflows 0.1.7 的切片接口当前需固定 Matplotlib **3.10.9**，3.11 已移除其使用的接口。Campaign Data 0.2.0 作为独立文件审计阶段接入，不使用要求 `<0.2` 的 `plot-workflows[campaign]`。Eigenmode 0.3.1 分组使用**单独环境**，详见其公开 feature 分支。无需改变日常科研环境。

The first releases intentionally distribute the audited wheels and example bundles. Full public source remains in GitHub at each tag. Locally built sdists are not release attachments.

首轮附件限定为已审计的 wheel 与示例包；完整公开源码位于各 GitHub 标签。本地构建的 sdist 未作为发行附件。
