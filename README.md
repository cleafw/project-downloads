# Project Downloads · 项目附件备用下载

这是 cleafw 各项目共用的公开附件仓库。代码仓库继续负责源码和软件版本；这里的 [Releases](https://github.com/cleafw/project-downloads/releases) 只存放可公开再分发的附件。

| 项目 | 内容 | 版本 |
| --- | --- | --- |
| NeuralNote | MuScriptor GGUF 转录模型 | [v1 下载与校验](projects/neuralnote/muscriptor-v1/README.md) |

## 归档约定

- `projects/<项目>/<附件版本>/`：来源、许可证、校验值、安装说明，提交到 Git。
- `artifacts/<项目>/<附件版本>/originals/` 和 `release/`：本地原始文件和待上传附件，不提交到 Git。
- GitHub Release 标签：`<项目>-<附件版本>`。使用固定标签链接，不使用全仓库的「最新版本」。
- 单个附件必须小于 2 GiB。原文件超限时按字节拆分，记录顺序与 SHA-256；不覆盖已公开的版本，内容变更时使用新标签。
- 发布前检查文件的分发许可，从公开链接重新下载并核对校验值。不要上传私人文件、密钥或无权再分发的材料。

准备附件时，可运行 `python tools/split_asset.py <原文件> <release目录> <原文件的SHA-256>`。低于上限的文件原样保留；超过或达到上限的文件拆为从 `part01` 开始的分片。确认完整文件和分片校验值后，先上传到 Release 草稿，附件齐全再公开。
