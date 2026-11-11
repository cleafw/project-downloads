# NeuralNote · MuScriptor v1 模型

这是独立于 NeuralNote 安装包的备用下载。选一种模型即可，文件适用于支持 MuScriptor GGUF v1 的 NeuralNote。

| 模型 | 备用下载 |
| --- | --- |
| 小型，约 209 MB | [GGUF](https://github.com/cleafw/project-downloads/releases/download/neuralnote-muscriptor-v1/muscriptor-small-f16.gguf) |
| 中型，约 618 MB | [GGUF](https://github.com/cleafw/project-downloads/releases/download/neuralnote-muscriptor-v1/muscriptor-medium-f16.gguf) |
| 大型，约 2.74 GB | [第 1 片](https://github.com/cleafw/project-downloads/releases/download/neuralnote-muscriptor-v1/muscriptor-large-f16.gguf.part01) · [第 2 片](https://github.com/cleafw/project-downloads/releases/download/neuralnote-muscriptor-v1/muscriptor-large-f16.gguf.part02) |

支持备用下载的 NeuralNote 可在模型下载窗口选择 **从 GitHub 下载**，并自动合并和校验。手动下载时，大型模型的两片要放在同一个文件夹，再运行以下任一命令：

```bat
copy /b muscriptor-large-f16.gguf.part01+muscriptor-large-f16.gguf.part02 muscriptor-large-f16.gguf
```

```sh
cat muscriptor-large-f16.gguf.part01 muscriptor-large-f16.gguf.part02 > muscriptor-large-f16.gguf
```

第一条在 Windows 命令提示符运行，第二条在 macOS/Linux 终端运行。核对最终文件的 [SHA-256](SHA256SUMS.txt)，再将完整 GGUF 放入对应模型的使用目录，保持原文件名。分片不是可加载的模型。

## 来源和许可

- 原模型：**MuScriptor**，由 **Mirelo 和 Kyutai** 制作。见 [原始权重](https://huggingface.co/MuScriptor)、[代码](https://github.com/muscriptor/muscriptor)。
- GGUF 由 **Damien Ronssin** 转换，使用其 [固定版本](https://huggingface.co/DamRsn/muscriptor-gguf/tree/d7045f94e8b19427f4ff9542975035e66596e51c)；详见 [上游署名及使用说明](NOTICE.md)。
- 权重许可为 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，限非商业用途。本镜像不修改权重；大型模型只做字节分片。此镜像不代表原作者背书。
