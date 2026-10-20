# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：73
- 分类分布：
  - Neural Scene Representations & Rendering: 25
  - Embodied / Robotics / AR Applications: 23
  - 3D Reconstruction & Multi-view Geometry: 18
  - Dynamic / 4D Reconstruction: 5
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“几何基础模型 + 分辨率/规模解耦”成为多视图重建的新主线。**
   ReDT 直接指出高分辨率输入下帧内注意力与编码器注意力开销未被解决，提出用固定大小基元 token 空间做对应计算；SpaRV 则从机器人数据出发，用稀疏辐射体素 + LiDAR 监督解决几何约束不足与显存随场景增长的问题。两者共同反映：重建模型正在从“堆叠视图/分辨率”转向“把几何推理与输入规模解耦”。

2. **前馈式 4D/动态重建与生成式视频模型加速合流。**
   Drive2Gauss 把联合生成的 RGB、度量深度、动态流前馈转换为 4D 高斯，避免逐序列优化；Holo4D 把前馈 4D 重建得到的 3D 轨迹投影到目标视角，作为视频扩散模型的几何控制。两者都体现“重建提供几何骨架、生成补全未观测区域”的分工模式，动态 4D 重建正从优化型管线转向可复用前馈表示。

3. **稀疏视角/受限观测下的表示正则化被系统化重述。**
   稀疏视角 3DGS 论文把高斯基元当神经元、以少样本学习视角统一数据监督增强与训练正则化；MCSplat 用规范外观空间解耦几何与相机外观，并用 Fisher 信息不确定性加权几何自监督。这说明 3DGS 社区的关注点正从“表示能力”转向“在弱监督、跨相机不一致条件下如何防止几何退化”。

4. **机器人操作正在从单一策略转向“触觉/形态条件化 + 仿真到真实适配 + 未知物体可用性”。**
   LEAP Hand 论文比较拟人化与对称式手指布局在完整触觉、二值接触、仅本体感觉下的表现，把手部几何与触觉反馈作为可分析变量；农业 VLA 论文用 MuJoCo 演示适配 Octo 与 π₀.₅ 并在真实 Franka 上微调；OV-PEAR 面向未知工业物体做观测验证的位姿-尺度估计与重建。共同趋势是：不再假设物体已知或工作单元稳定，而是强调对未见物体的适应与多模态反馈的作用量化。

5. **具身智能评测开始从“问答/静态任务”转向“主动探索与地图式推理”。**
   SpatialScout 要求 VLM 智能体在有限交互预算下主动控制相机、完成对象级 3D 度量建图；ForagerSim 提供可独立调节感知、尺度、拓扑、动态的任务平台，并指出地图式推理可能是瓶颈。这反映评测设计正在向“主动获取证据 + 构建一致空间表示”迁移，而非仅考查单帧识别或空间问答。

#### 技术路线观察

- **几何基础模型方向**：ReDT 的路线是“内部表示与输入分辨率解耦”，以固定大小基元空间承载对应计算；PnP-Transformer 则把位姿求解本身神经化、可微化，试图替代 PnP-RANSAC 的迭代流程。两者分别从“特征侧”和“求解侧”推进几何基础能力，但 PnP-Transformer 摘要中 EPnP-RANSAC 替换后反超的结果提示：神经求解器的收益可能高度依赖对应场质量与训练/集成方式。

- **3D/4D 重建方向**：Drive2Gauss 与 Holo4D 都采用“多模态生成/重建 → 显式 4D 表示 → 下游渲染或条件控制”的前馈路线；MCSplat 与 ReDT 则更关注多视图一致性、分辨率和几何监督可靠性。整体上，4D 重建正从“每场景优化”转向“前馈 + 可组合表示”，但跨相机光度一致性、动态流可靠性和大场景扩展仍是共同难点。

- **神经场景表示与渲染方向**：RxGS 把风格化从 RGB 外观转移到 BRDF 分解后的漫反射反照率场，使风格化结果可重光照；SpaRV 用稀疏体素替代稠密辐射场以控制显存；稀疏视角 3DGS 论文用少样本学习框架统一监督增强与正则化。三条路线分别对应“物理可分解”“内存可扩展”“监督可正则化”，显示 3DGS/辐射场研究正在向可编辑、可扩展、抗退化三个维度分化。

- **机器人/AR 应用方向**：LEAP Hand 论文把触觉观测条件作为消融变量，量化完整触觉相对本体感觉的提升（拟人化 94.8%、对称 66.9%）；农业 VLA 论文强调仿真演示降低真实采集成本；OV-PEAR 强调观测验证抑制生成幻觉；CAOS-SLAM 强调无需预定义类别的动态物体过滤。共同技术侧重点是“在真实部署约束（成本、未知物体、动态环境、传感器噪声）下保持可用性”，而非追求单一基准分数。

- **交叉趋势**：单目 MAV 飞行论文用跨模态蒸馏把深度专家的规划特征迁移到 RGB 规划器，并借助 3DGS 模拟器做数据生成；这与 Drive2Gauss、Holo4D 形成呼应：3DGS/4D 表示不仅用于渲染，也越来越多地充当机器人学习的仿真数据与几何监督来源。

#### 值得优先阅读的论文

1. **ReDT: Resolution-Decoupled Visual Geometry Transformer**（2610.25517）
   理由：直接处理视觉几何 Transformer 在高分辨率下的计算扩展问题，提出“基元 token 空间”这一可复用的架构思路。对多视图重建、几何基础模型和 HD 输入落地都有直接参考价值，且属于方法层面的结构性改进。

2. **Drive2Gauss**（2610.26585）与 **Holo4D**（2610.25276）可对照阅读
   理由：两篇分别代表“生成多模态 → 前馈 4D 高斯”和“前馈 4D 重建 → 条件化视频扩散”两种互补路线。对照阅读能看清 4D 重建与生成模型的分工边界、几何控制信号的形式，以及哪些区域交给生成先验。

3. **SpatialScout**（2610.26659）
   理由：把 VLM 智能体的评测从空间问答推进到主动探索与对象级度量建图，任务定义（视角选择、跨视角关联、几何估计、地图修正、有限交互预算）清晰，适合作为具身空间智能评测设计的参考基准。

4. **Tactile In-Hand Object Rotation**（2610.26759）
   理由：以手部形态与触觉观测条件为控制变量，给出仿真与硬件对照的量化结果（完整触觉相对本体感觉提升 94.8%/66.9%），对触觉操作、低成本硬件和强化学习框架的可复现实验设计有较高参考价值。

5. **OV-PEAR**（2610.25840）
   理由：面向未知工业物体的位姿-尺度估计与重建，强调观测验证抑制生成幻觉并产出可复用物体模型，贴近工业操作落地中的“无 CAD、无物体专用训练数据”场景，方法三阶段流程较完整。

#### 可能的研究机会

- **分辨率解耦思想向 4D/动态重建迁移**：ReDT 的基元 token 空间主要用于多视图静态重建；若把时间维度纳入固定大小基元表示，可能缓解 Drive2Gauss/Holo4D 在长序列或高分辨率驾驶视频上的计算压力。可探索“时空基元 token + 动态流关联”的前馈 4D 架构。

- **触觉条件化与手部形态的联合优化**：LEAP Hand 论文把形态作为固定变量比较；一个自然空白是“形态-触觉-策略”联合设计或形态参数化搜索，并验证仿真中触觉收益在硬件多朝向条件下是否保持。可与农业 VLA 的仿真到真实适配流程结合，形成跨任务的触觉策略迁移评估。

- **未知物体重建中的观测验证与不确定性量化**：OV-PEAR 用体素占用验证抑制幻觉，MCSplat 用 Fisher 信息不确定性加权几何监督。两者可组合为“生成假设

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-20T12:59:56-04:00
**Total number of papers:** 73
**Number of papers added in the latest update:** 26
**Categories tracked:** cs.CV, cs.GR, cs.RO, eess.IV

Paper metadata is collected from the public arXiv API and stored as structured JSON. PDF files are not mirrored or redistributed; full-text analysis only downloads PDFs temporarily during the workflow run and deletes them afterward.

Rolling 7-day structured archive: [data/papers.json](data/papers.json)

## Table of Contents

- [Geometry Foundation Models](#geometry-foundation-models)
- [Dynamic / 4D Reconstruction](#dynamic-4d-reconstruction)
- [3D Reconstruction & Multi-view Geometry](#3d-reconstruction-multi-view-geometry)
- [Neural Scene Representations & Rendering](#neural-scene-representations-rendering)
- [Embodied / Robotics / AR Applications](#embodied-robotics-ar-applications)

## How It Works

1. GitHub Actions runs the update workflow every day.
2. The update script searches candidate papers from the latest configured lookback window.
3. A deterministic rule-based classifier filters and categorizes papers.
4. Papers are deduplicated by normalized arXiv ID.
5. README displays papers from the latest 7 days.
6. The rolling 7-day archive is kept in data/papers.json.
7. PDF files are never stored in this repository.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
python scripts/update_papers.py
```

Windows PowerShell activation:

```powershell
.venv\Scripts\Activate.ps1
```

## Configuration

Users can edit config.yaml to adjust arXiv categories, include keywords, exclude keywords, category priority, lookback days, README display days, request interval, and classification thresholds.

## Manual Update

Use the Actions tab on GitHub and run the workflow_dispatch trigger manually.

## Geometry Foundation Models

### 2026-10

#### 2026-10-18 - ReDT: Resolution-Decoupled Visual Geometry Transformer

**Authors:** Abteen Arab, Guile Wu, Dongfeng Bai
**Links:** [abs](https://arxiv.org/abs/2610.25517) - [pdf](https://arxiv.org/pdf/2610.25517)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, multi-view reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReDT: Resolution-Decoupled Visual Geometry Transformer
- 作者：Abteen Arab, Guile Wu, Dongfeng Bai
- 出版日期：2026-10-18T20:17:29Z
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.25517) / [PDF](https://arxiv.org/pdf/2610.25517) / [项目网站](https://redt.github.io)

### 一句话总结
ReDT 是一种前馈视觉几何 Transformer，通过将多视图重建的内部注意力表示与输入分辨率解耦，使高分辨率（HD/2K）多视图重建在质量和计算效率上均优于现有方法。

### 研究问题
现有视觉几何 Transformer 通常在固定标准定义（SD）分辨率上训练，面对高输入分辨率时重建质量下降、计算扩展性差。已有高效架构主要降低帧间注意力复杂度，但帧内注意力与编码器注意力的高昂开销仍未解决，导致 HD 重建在现有架构下不切实际。

### 核心思路/方法
ReDT 的核心是分辨率解耦：先将每个视图映射为固定大小的基元 token 集合，在这个紧凑、恒定大小的基元空间中计算对应关系，再将输出投影回原始分辨率进行稠密预测。由于注意力阶段的内部表示与输入分辨率解耦，高分辨率 3D 重建的计算成本大幅降低，同时模型在各分辨率下的性能得到改善。

### 主要贡献
- 提出 ReDT，一种面向高分辨率输入扩展的前馈视觉几何 Transformer。
- 通过固定大小基元 token 空间进行对应计算，解耦内部表示与输入分辨率，缓解帧内与编码器注意力的高开销。
- 在 SD 到 FHD（2K）的多个数据集上取得优于现有视觉几何 Transformer 的重建质量与计算效率。
- 摘要给出的具体结果：在 ETH3D（2K）上相对 VGGT-$Ω$ 实现 $16\times$ 加速、峰值 GPU 内存降低 $34\%$、chamfer distance 降低 $33\%$。

### 局限性
摘要未提供足够信息。未说明方法在极低分辨率、稀疏视图、动态场景或训练数据分布外场景下的表现；未提供消融实验细节、失败案例或计算成本的具体测量条件。

### 阅读优先级
高。理由：该工作直接针对视觉几何 Transformer 在高分辨率多视图重建中的计算瓶颈，提出分辨率解耦的架构思路，并在摘要中给出明确的效率与精度改进数据，与 3D 重建和多视图几何方向高度相关。

</details>

<details>
<summary>Abstract</summary>

We introduce ReDT, a feed-forward visual geometry transformer designed to scale multi-view reconstruction to high-definition (HD) inputs. Existing visual geometry transformers are typically trained at fixed, standard definition (SD) resolutions and exhibit degraded reconstruction quality and poor computational scaling to high input resolutions. While recent efficient architectures reduce the complexity of inter-frame attention, expensive intra-frame and encoder attention remain largely unaddressed, making HD reconstruction impractical with existing architectures. ReDT addresses both limitations with a resolution-aware architecture designed to scale to high-resolution inputs. The key idea of ReDT is to first map each view to a fixed-size set of basis tokens, compute correspondences in this compact constant-size basis space, and then project the outputs back to the original resolution for dense prediction. By decoupling the internal representation from input resolution during attention, ReDT substantially reduces the computational cost of high-resolution 3D reconstruction and improves model performance at all resolutions. Extensive experiments on multiple datasets spanning SD to FHD (2K) show that ReDT outperforms state-of-the-art visual geometry transformers in both reconstruction quality and computational efficiency. For instance, on the ETH3D (2K) dataset, ReDT achieves a $16\times$ speedup, a $34\%$ reduction in peak GPU memory usage, and a $33\%$ reduction in chamfer distance over VGGT-$Ω$. \href{https://redt.github.io}{Project Website.}

</details>

#### 2026-10-15 - Motion- and Gravity-Aware Feedforward 3D Reconstruction

**Authors:** Shiyao Qian, Yuan Ren, Dongfeng Bai
**Links:** [abs](https://arxiv.org/abs/2610.22177) - [pdf](https://arxiv.org/pdf/2610.22177)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Motion- and Gravity-Aware Feedforward 3D Reconstruction
- 作者：Shiyao Qian, Yuan Ren, Dongfeng Bai
- 出版日期：2026-10-15T16:34:04Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.22177 ；PDF https://arxiv.org/pdf/2610.22177

### 一句话总结
该论文在 LUPI（Learning Using Privileged Information）框架下，将残差光流和重力方向作为训练期的特权信号注入前馈 Transformer，以提升多视角 3D 重建在动态场景和弱几何线索下的精度与鲁棒性，且不增加推理阶段复杂度。

### 研究问题
前馈 Transformer 在多视角 3D 重建中表现良好，但主要依赖基于外观的注意力机制，在存在动态物体、几何线索薄弱等情形时仍面临困难。论文关注的问题是：如何在不增加测试时复杂度的前提下，把运动信息与物理先验（重力）引入前馈重建模型，以改善动态场景与困难相机运动下的重建表现。

### 核心思路/方法
- 采用 LUPI 范式：训练阶段额外提供残差光流和重力方向作为特权信号，用于指导几何表示学习；推理阶段仅使用标准视觉输入。
- 将这些先验以轻量级结构改动集成到 Transformer 骨干中，保持前馈效率。
- 考察不同注入阶段的影响，发现最优注入阶段依赖骨干网络：对 VGGT 通常中间层集成更优，对 π3 则后期集成更有效。

### 主要贡献
- 提出运动与重力感知的前馈 3D 重建框架，在 LUPI 范式下引入残差光流与重力方向作为训练期特权信号。
- 通过轻量级架构改动将上述先验注入 Transformer 骨干，保持前馈推理效率，不增加测试时复杂度。
- 在标准基准上取得重建精度与鲁棒性的一致提升，尤其在动态物体、结构歧义和挑战性相机运动场景中。
- 分析表明先验注入的最优阶段与骨干相关：VGGT 偏好中间层，π3 偏好后期阶段，为 LUPI 在前馈 3D 重建中的实际应用提供了参考。

### 局限性
- 摘要未提供足够信息说明具体数据集、评价指标、定量提升幅度及消融实验的详细设置。
- 摘要未提供足够信息说明模型规模、训练成本、推理速度或对特权信号质量的敏感度。
- 摘要未提供足够信息说明该方法在非动态或强几何线索场景中的表现，以及是否对特定骨干存在依赖性限制。
- 摘要未提供足够信息说明重力方向与残差光流的具体获取方式及其在真实部署中的可行性。

### 阅读优先级
中。理由：该论文面向多视角 3D 重建中的动态场景与弱几何线索问题，提出的 LUPI 训练期特权信息注入思路具有明确的问题针对性，且强调不增加推理复杂度，对前馈 3D 重建与几何基础模型方向有参考价值；但摘要未给出定量结果与实验细节，是否值得深入阅读需结合具体基准表现和实现细节进一步判断。

</details>

<details>
<summary>Abstract</summary>

Feed-forward transformer models have recently achieved strong performance in multi-view 3D reconstruction, but they still rely primarily on appearance-based attention and often struggle in dynamic scenes with weak geometric cues. In this work, we introduce a motion- and gravity-aware framework under the Learning Using Privileged Information (LUPI) paradigm. During training, residual optical flow and gravity direction are provided as privileged signals to guide geometric representation learning; during inference, the model uses standard visual inputs only. We integrate these priors into transformer backbones with lightweight architectural changes, preserving feed-forward efficiency. Experiments on standard benchmarks show consistent gains in reconstruction accuracy and robustness, especially in scenes with dynamic objects, ambiguous structure, and challenging camera motion. Our analysis further shows that the optimal injection stage is backbone-dependent: middle-layer integration is generally preferable for VGGT, while late-stage integration is more effective for π3. These results suggest that LUPI offers a practical way to inject motion and physical priors into feed-forward 3D reconstruction without increasing test-time complexity.

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-19 - Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos

**Authors:** Tong Zhao, Zhiyuan Han, Lin Chen, Bowen Xie, Yunxi Qiao, Bohan Li, Weiqing Xiao, Gen Li, Shu Han, Xuyang Dai, Cheng Bi, Hao Zhao, Chaojian Li
**Links:** [abs](https://arxiv.org/abs/2610.26585) - [pdf](https://arxiv.org/pdf/2610.26585)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** metric depth, dynamic 4D, 4D Gaussian, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos
- 作者：Tong Zhao, Zhiyuan Han, Lin Chen, Bowen Xie, Yunxi Qiao, Bohan Li, Weiqing Xiao, Gen Li, Shu Han, Xuyang Dai, Cheng Bi, Hao Zhao, Chaojian Li
- 出版日期：2026-10-19T15:34:28Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.26585；PDF https://arxiv.org/pdf/2610.26585

### 一句话总结
Drive2Gauss 提出一种前馈框架，将从参考多视角图像与未来控制信号联合生成的 RGB、度量深度和动态流转换为动态 4D 高斯场景，从而避免逐序列优化。

### 研究问题
生成可复用的驾驶环境需要：既可控制未来观测，又要有支持不同视角渲染的显式表示。然而现有方法仍需针对每条生成 RGB 视频逐序列优化来恢复显式场景，效率与可复用性受限。论文即针对这一“生成视频到显式动态场景”的重建问题展开。

### 核心思路/方法
方法由两部分构成：
1. **多模态视频生成器**：从参考多视角图像和未来控制信号预测 RGB、度量深度和动态流三种模态；
2. **高斯查询解码器**：用深度初始化稀疏 3D 查询，用动态流在时间维度关联查询，并通过时空特征聚合与迭代查询细化融合外观信息。

重建阶段以单次前馈完成，无需针对每个场景做优化。

### 主要贡献
- 提出 Drive2Gauss 前馈框架，把联合生成的 RGB、度量深度与动态流转换为动态 4D 高斯场景。
- 设计高斯查询解码器，利用深度初始化稀疏 3D 查询、利用动态流建立跨时间关联，并结合时空特征聚合与迭代细化。
- 重建不再依赖逐场景优化，实现单次前馈推理。
- 在 nuScenes 上报告：未来 RGB 生成 FID 6.38、FVD 12.43；重建其生成观测的 PSNR 为 29.91 dB；并支持横向相机偏移下的直接渲染与下游视频修复。

### 局限性
摘要未提供足够信息。摘要未说明方法在更多数据集上的泛化性、失败案例、计算开销、对生成模态质量的敏感性，也未给出与逐序列优化方法的系统性对比细节。

### 阅读优先级
**中**。理由：该工作与“生成式驾驶视频驱动的 4D 重建”直接相关，核心思路（多模态生成 + 前馈高斯查询解码）清晰，且有 nuScenes 上的量化结果；若关注动态 4D 重建或驾驶场景生成，值得阅读。但摘要未提供与优化式方法的对比细节和泛化性证据，且兴趣方向未额外指定，因此不列为高优先级。

</details>

<details>
<summary>Abstract</summary>

Generating reusable driving environments requires both controllable future observations and an explicit representation that supports rendering from different viewpoints, yet existing methods still recover explicit scenes from generated RGB videos through optimization for each sequence. To overcome these limitations, we present Drive2Gauss, a feedforward framework that converts jointly generated RGB, metric depth, and dynamic flow into dynamic 4D Gaussian scenes. A Multimodal Video Generator predicts the three modalities from reference multiview images and future control signals. Furthermore, we introduce a Gaussian Query Decoder that uses depth to initialize sparse 3D queries and flow to associate the queries across time, and integrates appearance information through spatiotemporal feature aggregation and iterative query refinement. The reconstruction stage operates in a single feedforward pass without optimization for each scene. Extensive results on nuScenes demonstrate that our approach attains an FID of 6.38 and an FVD of 12.43 for future RGB generation, a PSNR of 29.91 dB when reconstructing its generated observations, and supports both direct rendering under lateral camera shifts and downstream video fixing. Code and more visualizations are available at https://zttt04. github.io/Drive2Gauss_page/.

</details>

#### 2026-10-18 - Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion

**Authors:** Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
**Links:** [abs](https://arxiv.org/abs/2610.25276) - [pdf](https://arxiv.org/pdf/2610.25276)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion
- 作者：Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
- 出版日期：2026-10-18T13:47:01Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.25276)｜[PDF](https://arxiv.org/pdf/2610.25276)

### 一句话总结
Holo4D 将前馈 4D 重建得到的 3D 轨迹投影到目标视角，作为几何与外观的条件引导预训练视频扩散模型，实现单目视频的新相机轨迹重拍。

### 研究问题
从新相机轨迹合成单目视频，需要同时保持已观测场景的几何与运动，并补全新变为可见的区域。前馈 4D 重建器能恢复观测场景结构，视频扩散模型提供生成先验；论文关注如何将两者结合，以重建立足生成、以生成补全未观测区域。

### 核心思路/方法
提出名为 Holo4D 的视频重拍框架：将重建的 3D 轨迹作为整体性的源视角 4D 脚手架（scaffold）；把这些轨迹投影到请求的目标视角，并编码其几何与源外观，用于引导预训练视频扩散模型。结合源视频与目标相机，脚手架使生成以重建观测为依据，而未支持区域交由生成先验补全。框架可适配不同的 4D 重建器，无需重新训练视频生成器。

### 主要贡献
- 提出以重建 3D 轨迹作为整体源视角 4D 脚手架来条件化视频扩散模型的视频重拍框架。
- 将轨迹投影到目标视角并编码几何与源外观，以引导预训练视频扩散模型。
- 实验表明基于轨迹的条件化对相机控制和新视角合成具有价值。
- 框架可容纳不同 4D 重建器且无需重训视频生成器，从而有望受益于源重建的后续进展。

### 局限性
摘要未提供足够信息（未给出失败情形、计算开销、重建器依赖程度或评测细节等具体局限）。

### 阅读优先级
高。理由：论文聚焦 4D 重建与视频扩散的结合，以重建轨迹作为几何控制，且强调无需重训生成器即可适配不同重建器；对动态/4D 重建与神经场景表示渲染方向具有直接相关性。

</details>

<details>
<summary>Abstract</summary>

Synthesizing a monocular video from a new camera trajectory requires preserving the observed scene geometry and motion while completing regions that become newly visible. Feed-forward 4D reconstructors recover the structure of the observed scene, whereas video diffusion models provide a generative prior for completing unseen content. We introduce Holo4D, a video reshooting framework that uses reconstructed 3D trajectories as a holistic source-view 4D scaffold. We project these trajectories into the requested views and encode their geometry and source appearance to guide a pretrained video diffusion model. Together with the source video and target cameras, the scaffold grounds generation in reconstructed observations while leaving unsupported regions to the generative prior. Experiments demonstrate the value of trajectory-based conditioning for camera control and novel-view synthesis. The framework accommodates different 4D reconstructors without retraining the video generator, allowing it to benefit from future advances in source reconstruction. More details can be found in our project page.

</details>

#### 2026-10-14 - DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning

**Authors:** Qihang Cao, Haoyuan Li, Zihan Guo, Sensen Gao, Zihui Gao, Huixin Zhang, Fan He, Jianhua Han, Hang Xu, Xiaodan Liang, Jia-Wang Bian
**Links:** [abs](https://arxiv.org/abs/2610.20598) - [pdf](https://arxiv.org/pdf/2610.20598)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 4D, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning
- 作者：Qihang Cao, Haoyuan Li, Zihan Guo, Sensen Gao, Zihui Gao, Huixin Zhang, Fan He, Jianhua Han, Hang Xu, Xiaodan Liang, Jia-Wang Bian
- 出版日期：2026-10-14T17:59:31Z
- 分类：主分类 Dynamic / 4D Reconstruction；二级分类未提供
- 链接：摘要链接 https://arxiv.org/abs/2610.20598 ；PDF 链接 https://arxiv.org/pdf/2610.20598

### 一句话总结
DynThinker 提出统一框架，通过 D-EMA 与 Spatial-Dynamic Fusion 缓解静态 3D 与动态 4D 空间推理之间的相互干扰，从而在同一个模型中同时增强两类空间推理能力。

### 研究问题
论文关注的问题是：实现通用空间智能需要同时理解静态 3D 与动态 4D，但现有模型难以在两者上都表现优异。摘要指出，3D 后训练可能削弱动态理解，而 4D 专用模型往往缺乏强静态 3D 推理能力。作者进一步分析认为，这种“空间—动态干扰”在不同参数组之间高度不均匀，静态与动态能力之间的平衡对后层 MLP 的变化尤其敏感。

### 核心思路/方法
针对上述干扰，论文提出统一框架 DynThinker，用于联合增强静态与动态空间推理。方法包含两个核心组件：
1. **Decoupled Exponential Moving Average (D-EMA)**：对参数进行可配置的分组平均，以约束对干扰敏感的预训练参数发生漂移，同时保留能力增强的灵活性。
2. **Spatial-Dynamic Fusion (SDF)**：在语义引导下，选择性地将动态几何编码器中的空间先验和时间先验整合进 VLM 的中间表示，与 D-EMA 形成互补。

### 主要贡献
- 发现并指出静态 3D 与动态 4D 空间推理之间存在非均匀的“空间—动态干扰”，且该平衡对后层 MLP 变化尤为敏感。
- 提出 DynThinker 统一框架，联合增强静态 3D 与动态 4D 空间推理。
- 提出 D-EMA，用于约束干扰敏感预训练参数的漂移。
- 提出 SDF，在语义引导下将动态几何编码器的空间与时间先验选择性融合进 VLM 中间表示。
- 在覆盖九个静态 3D 与动态 4D 基准的十个指标上，DynThinker 取得所有评估模型中的最高平均分；并在 ReVSI、DSR-Bench、DSI-Bench 的 sample-wise 与 group-wise 评测协议上分别取得 56.0、67.2、51.2 和 40.1，在统一模型下于这四项评测中刷新所比较开源模型的最优结果。

### 局限性
摘要未提供足够信息说明 DynThinker 的局限性，例如失败场景、计算开销、对特定基准或数据分布的依赖、消融实验的完整结果，以及 D-EMA 与 SDF 各自贡献的详细定量分析，均未在摘要中给出。

### 阅读优先级
高。理由：该论文直接针对静态 3D 与动态 4D 空间推理之间的干扰问题，提出统一框架，并在摘要中报告了跨九个基准、十个指标的领先平均成绩，以及四项评测中的开源模型最优结果，主题明确且结果陈述集中，适合优先阅读以了解统一空间推理方法的设计思路。

</details>

<details>
<summary>Abstract</summary>

Achieving general spatial intelligence requires a unified understanding of both static 3D and dynamic 4D. However, we find that existing models struggle to excel at both: 3D post-training can weaken dynamic understanding, while 4D-specialized models often lack strong static 3D reasoning. Our analysis reveals that this spatial--dynamic interference is highly non-uniform across parameter groups, with the balance between static and dynamic capabilities particularly sensitive to changes in late-layer MLPs. To address this interference, we propose DynThinker, a unified framework for jointly strengthening static and dynamic spatial reasoning. Decoupled Exponential Moving Average (D-EMA) applies configurable group-wise averaging to constrain drift in interference-sensitive pretrained parameters while preserving flexibility for capability enhancement. Spatial-Dynamic Fusion (SDF) complements D-EMA by selectively integrating spatial and temporal priors from a dynamic geometry encoder into intermediate VLM representations under semantic guidance. Across ten metrics spanning nine static 3D and dynamic 4D benchmarks, DynThinker achieves the highest average score among all evaluated models. Notably, DynThinker achieves 56.0 on ReVSI, 67.2 on DSR-Bench, and 51.2 and 40.1 under the sample-wise and group-wise evaluation protocols of DSI-Bench, respectively, setting new state-of-the-art results among the compared open-source models across all four evaluations within a unified model.

</details>

#### 2026-10-14 - DD-GBP: Anytime Multi-Arm Planning and Continuous Execution via Distributed Dynamic Gaussian Belief Propagation

**Authors:** Zhao Jin, Fengyi Dai, Yuetong Yin, Yunan Wang, Wenjie Chen, Chuxiong Hu
**Links:** [abs](https://arxiv.org/abs/2610.20460) - [pdf](https://arxiv.org/pdf/2610.20460)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DD-GBP: Anytime Multi-Arm Planning and Continuous Execution via Distributed Dynamic Gaussian Belief Propagation
- 作者：Zhao Jin, Fengyi Dai, Yuetong Yin, Yunan Wang, Wenjie Chen, Chuxiong Hu
- 出版日期：2026-10-14T16:43:32Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：abstract_url: https://arxiv.org/abs/2610.20460；pdf_url: https://arxiv.org/pdf/2610.20460

### 一句话总结
论文提出分布式动态高斯信念传播（DD-GBP）方法，通过并行的局部推断直接规划多机械臂的关节空间轨迹，以在复杂动态环境中实现长时程多臂规划与连续执行。

### 研究问题
在复杂动态环境中，安全地在线执行长时程多臂任务仍然具有挑战性。论文关注的问题是如何在线完成长时程多臂规划，并在动态障碍与通信受限条件下保持安全与连续执行。

### 核心思路/方法
- 提出分布式动态高斯信念传播（DD-GBP），通过并行局部推断直接规划关节空间轨迹。
- 使用统一的高斯过程（GP）参数化，将自适应规划时域、插值时间因子和连续执行连接起来。
- 每个机器人维护局部树结构因子图，并在活跃的臂间链路上异步交换消息。
- 通过动态子网重建和事件触发更新，降低通信与推断成本，同时响应移动障碍物。
- 提供关于局部推断精度、anytime 早停、触发重规划一致性和 GP 一致执行的理论分析。

### 主要贡献
- 提出 DD-GBP 方法，用于在线长时程多臂规划与连续执行。
- 给出局部推断精度、anytime 早停、触发重规划一致性及 GP 一致执行的理论分析。
- 在 50 个长时程、多目标、含移动障碍的四臂场景中，DD-GBP 实现 92.5% 的无碰撞全目标完成率，并在六个代表性基线中取得最高成功率。
- 场景消融显示长时程安全性与对通信损伤和极端条件的鲁棒性；在 90% 丢包下成功率仍为 86.0%。
- 执行结果显示，相对于 Syn-GBP，显著抑制了极端速度与加速度峰值。
- 在一个工作站上，30 个共存臂的无障碍测试保持 99.87% 成功率，平均热求解时间为 15.80 ms，超过 60 Hz，并在可扩展性上优于对比方法。
- 动态干扰下的双臂运输实验展示了在线响应与实际部署能力。

### 局限性
摘要未提供足够信息。摘要未说明方法在更一般场景、不同机器人构型、真实硬件长期运行或计算资源受限条件下的具体局限。

### 阅读优先级
中。理由：论文主题涉及多臂在线规划、分布式推断与动态环境执行，并声称在成功率、通信鲁棒性和可扩展性上取得较强结果；但主分类为 Dynamic / 4D Reconstruction，与机器人规划任务存在分类上的错位，且摘要未提供足够信息说明方法细节与局限。若关注多臂规划、信念传播或在线连续执行，可优先阅读；若仅关注 4D 重建或神经场景表示，则相关性可能较低。

</details>

<details>
<summary>Abstract</summary>

Safely executing long-horizon multi-arm tasks online in complex dynamic environments remains challenging. We propose a new distributed dynamic Gaussian belief propagation (DD-GBP) method that directly plans joint-space trajectories through parallel local inference. A unified Gaussian-process (GP) parameterization connects adaptive planning horizons, interpolation-time factors, and continuous execution. Each robot maintains a local tree-structured factor graph and exchanges messages asynchronously over active inter-arm links. Dynamic subnet reconstruction and event-triggered updates reduce communication and inference costs while responding to moving obstacles. We also provide theoretical analyses of local inference accuracy, anytime early stopping, triggered-replanning consistency, and GP-consistent execution. In 50 long-horizon, multi-target four-arm scenes with moving obstacles, DD-GBP achieves $92.5\%$ collision-free all-target completion and the highest success rate among six representative baselines. Scenario ablations demonstrate long-horizon safety and robustness to communication impairment and extreme conditions; success remains $86.0\%$ under $90\%$ packet loss. Execution results further show substantially suppressed extreme velocity and acceleration peaks relative to Syn-GBP. On one workstation, obstacle-free tests with 30 coexisting arms retain $99.87\%$ success and a $15.80$ ms mean warm solve, exceeding 60 Hz and outperforming the compared methods in scalability. Dual-arm transport experiments under dynamic interference demonstrate online response and practical deployability. To the best of our knowledge, these results establish a new state of the art for online long-horizon multi-arm planning in dynamic scenes.

</details>

#### 2026-10-13 - Perceptual Characterization of Scan-induced Artifacts in Dynamic 3D Meshes

**Authors:** Huong Hoang, Truong Nguyen, Pamela Cosman
**Links:** [abs](https://arxiv.org/abs/2610.19173) - [pdf](https://arxiv.org/pdf/2610.19173)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Perceptual Characterization of Scan-induced Artifacts in Dynamic 3D Meshes
- 作者：Huong Hoang, Truong Nguyen, Pamela Cosman
- 出版日期：2026-10-13T20:39:45Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.19173 ；PDF https://arxiv.org/pdf/2610.19173

### 一句话总结
本文针对真实场景重建的动态网格中由扫描引起的表面抖动与孔洞等伪影，开展系统可控的感知研究，并提出一种紧凑的无参考质量评估框架。

### 研究问题
从真实世界场景重建的动态网格常出现表面抖动和几何缺失等扫描伪影，显著影响视觉质量感知。但由于缺乏无伪影的参考真值，且对伪影之间交互作用的感知理解有限，客观质量评估仍然困难。本文关注的是：如何系统研究表面抖动与孔洞这两类扫描伪影的感知特性，以及如何基于感知机制构建无参考质量评估方法。

### 核心思路/方法
- 开展针对动态网格中扫描伪影的系统、可控感知研究，聚焦表面抖动与孔洞。
- 提出一个具有物理基础的伪影合成框架：孔洞基于多视图几何导出的重建不确定性模型进行合成。
- 通过该受控研究揭示伪影间的非对称交叉交互、非加性整合以及运动依赖的时间掩蔽现象。
- 基于上述发现，提出一个紧凑、具有感知基础的无参考质量评估框架，用于编码所观察到的感知机制。

### 主要贡献
- 针对动态网格中扫描引起的伪影（表面抖动与孔洞）提供了系统且可控的感知研究。
- 提出物理基础的伪影合成框架，其中孔洞由多视图几何推导的重建不确定性模型合成，以支持系统分析。
- 揭示了非对称跨伪影交互、非加性整合和运动依赖的时间掩蔽等感知规律。
- 基于这些发现提出紧凑的无参考质量评估框架，将观察到的感知机制编码其中。

### 局限性
摘要未提供足够信息。摘要未说明研究使用的数据集规模、受试者数量、具体实验设置、所提框架的定量性能以及与其他方法的对比结果，也未给出方法的适用边界与失败情形。

### 阅读优先级
中。理由：该工作聚焦动态 3D 网格扫描伪影的感知建模与无参考质量评估，问题定位清晰，且提出物理基础的合成框架和基于感知机制的评估框架，对动态/4D 重建与感知质量评估方向有参考价值；但摘要未提供实验规模与定量验证信息，实际影响力需阅读全文后判断。

</details>

<details>
<summary>Abstract</summary>

Dynamic meshes reconstructed from real-world scenes often exhibit scan-induced artifacts such as surface jitter and missing geometry, which strongly impact perceived visual quality. Objective assessment remains challenging due to the absence of artifact-free ground truth and limited perceptual understanding of artifact interactions. This paper presents a systematic and controlled perceptual study of scan-induced artifacts in dynamic meshes, focusing on surface jitter and holes. To enable systematic analysis, we introduce a physically grounded artifact synthesis framework in which holes are synthesized using a reconstruction uncertainty model derived from multi-view geometry. The study reveals asymmetric cross-artifact interactions, non-additive integration, and motion-dependent temporal masking. Based on these findings, we propose a compact, perceptually grounded no-reference quality assessment framework that encodes the observed perceptual mechanisms.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-19 - SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?

**Authors:** Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li
**Links:** [abs](https://arxiv.org/abs/2610.26659) - [pdf](https://arxiv.org/pdf/2610.26659)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D mapping, camera calibration, mapping, localization, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?
- 作者：Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li
- 出版日期：2026-10-19T16:17:48Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.26659) / [PDF](https://arxiv.org/pdf/2610.26659) / [代码](https://github.com/JesseZZZZZ/SpatialScout)

### 一句话总结
论文提出 SpatialScout 基准，用于评估视觉语言模型（VLM）智能体在主动探索室内场景时构建对象级三维度量地图的能力，并揭示当前前沿模型在精确定位与目标覆盖上的显著不足。

### 研究问题
摘要指出，空间智能要求智能体主动获取视觉证据，并将观测整合为对三维世界的一致表示；然而，现有的空间问答任务难以充分证明模型能否通过自主探索构建准确的度量地图。论文因此关注：VLM 智能体能否在有限交互预算下主动探索场景，并在统一坐标系中估计目标物体中心，从而完成对象级三维建图。

### 核心思路/方法
- 构建 SpatialScout 基准，包含 80 个多样室内场景和 3,140 个目标物体。
- 任务输入包括目标物体清单、RGB 观测、相机标定和相机位姿；智能体控制相机探索场景，并估计各目标物体中心在共享坐标系中的位置。
- 任务要求智能体协调视角选择、跨视角关联、几何估计和地图修正，且交互预算有限。
- 评估同时衡量定位精度与目标覆盖度，采用对象尺度重叠分数并对遗漏预测进行惩罚。
- 论文对前沿 VLM 进行实验评估。

### 主要贡献
- 提出面向主动对象级三维建图的 VLM 智能体基准 SpatialScout，强调通过自主探索构建度量地图，而非仅回答空间问题。
- 设计了结合定位精度与目标覆盖度的评估方式，使用对象尺度重叠分数并惩罚遗漏预测。
- 通过实验揭示当前前沿 VLM 的明显局限：最强评估模型 Claude Opus 5.5 的平均重叠分数为 41.71%，仅 47.23% 的目标超过 IoU 0.5，超过 IoU 0.9 的目标仅 3.25%。
- 指出模型在恢复粗略物体布局与构建完整、精确度量地图之间存在显著差距，并提供可量化测试平台与代码链接。

### 局限性
- 摘要未提供足够信息说明基准场景的具体来源、数据采集方式及场景多样性细节。
- 摘要未提供足够信息说明交互预算的具体数值、相机控制接口或动作空间设计。
- 摘要未提供足够信息说明除 Claude Opus 5.5 外参与评估的完整模型列表及各自详细结果。
- 摘要未提供足够信息说明失败模式分析、消融实验或方法改进建议。
- 摘要未提供足够信息说明评估指标的具体计算细节及与真实标注的匹配方式。

### 阅读优先级
高。理由：该论文直接针对 VLM 智能体主动三维感知与建图能力提出新基准，任务定义和评估指标明确，且摘要给出了量化结果与显著能力差距；对三维重建、多视角几何、具身智能和机器人应用方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploration. We introduce SpatialScout, a benchmark for evaluating vision-language model (VLM) agents on active object-level 3D mapping. SpatialScout comprises 80 diverse indoor scenes containing 3,140 target objects. Given an object inventory, RGB observations, camera calibration, and camera poses, agents control a camera to explore each scene and estimate object centers in a shared coordinate frame. The task requires coordinating viewpoint selection, cross-view association, geometric estimation, and map revision under bounded interaction budgets. Evaluation jointly measures localization accuracy and target coverage through object-scale overlap scores that penalize missing predictions. Experiments with frontier VLMs reveal substantial limitations: the strongest evaluated model, Claude Opus 5.5, achieves a mean overlap score of 41.71%, with 47.23% of targets exceeding an intersection-over-union (IoU) threshold of 0.5 and only 3.25% exceeding 0.9. These results reveal a substantial gap between recovering coarse object layouts and constructing complete, precise metric maps. SpatialScout provides a quantitative testbed for developing agents that build reliable 3D spatial representations through active perception. Code is available at https://github.com/JesseZZZZZ/SpatialScout.

</details>

#### 2026-10-19 - EgoRayFormer: Ray-Space Stereo Refinement for Egocentric 3D Human Pose Estimation

**Authors:** Haozhe Wang, Songyuan Wu, Jihai Xu, Jie Zhao
**Links:** [abs](https://arxiv.org/abs/2610.26641) - [pdf](https://arxiv.org/pdf/2610.26641)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoRayFormer: Ray-Space Stereo Refinement for Egocentric 3D Human Pose Estimation
- 作者：Haozhe Wang, Songyuan Wu, Jihai Xu, Jie Zhao
- 出版日期：2026-10-19T16:03:20Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；未提供二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.26641) / [PDF](https://arxiv.org/pdf/2610.26641)

### 一句话总结
EgoRayFormer 面向头戴式双目鱼眼相机下的第一人称 3D 人体姿态估计，在射线空间中耦合双目特征采样与几何细化，以引入显式双目约束，并在几何约束较弱时保留学习式更新的灵活性。

### 研究问题
头戴式双目鱼眼相机能提供穿戴者身体的紧凑视角，但强畸变、部分可见性和短基线使 3D 姿态估计困难。摘要指出现有细化解码器在各视图中独立采样图像特征，不要求这些采样对应共同的 3D 假设，因而缺少显式双目几何约束。论文即针对这一问题提出改进。

### 核心思路/方法
论文提出因果姿态估计器 EgoRayFormer，将双目特征采样与几何细化耦合在射线空间中。对每个关节，解码器沿其视线射线并在射线周围，把共享的 3D 假设投影到两幅图像中；随后几何分支校正投影后的关节位置，并对所得射线进行相交；一个学习到的门控将几何估计与学习到的姿态更新融合。该形式化方法引入显式双目约束，同时在射线提供弱深度约束时保留灵活性。

### 主要贡献
- 提出 EgoRayFormer，在射线空间中耦合双目特征采样与几何细化，用于第一人称 3D 人体姿态估计。
- 通过将共享 3D 假设沿/绕观测射线投影到双视图，并对校正后的射线求交，引入显式双目约束；再用学习门控融合几何估计与学习姿态更新。
- 摘要报告在官方设备相对测试划分上的本地评估结果：UnrealEgo2 上三随机种子平均 MPJPE 为 17.64 mm，UnrealEgo-RW 上为 49.55 mm，使用 UnrealEgo2 预训练后提升至 47.57 mm。
- 配对验证消融显示，在两种输入分辨率下移除几何分支均使三个随机种子的 MPJPE 增加。
- 在相同 ResNet-18 编码器和输入分辨率下，相较设备相对的 EgoPoseFormer 基线，将 RW 测试 MPJPE 降低 9.09 mm。
- 另有一项协议分析量化设备相对评估与 oracle-root 评估之间的差异。

### 局限性
摘要未提供足够信息说明方法在真实场景泛化、计算开销、对极端遮挡或强畸变的失败模式等方面的局限；也未提供跨数据集以外的完整实验细节。仅从摘要可知，部分结果来自本地评估与特定测试划分，且预训练依赖 UnrealEgo2。

### 阅读优先级
中。理由：该论文聚焦第一人称双目鱼眼 3D 人体姿态估计中的显式双目几何约束与射线空间细化，问题定义和方法动机较清晰，并报告了 MPJPE 改进与消融结果；但摘要未提供真实场景验证、计算成本及更广泛失败模式的信息，是否高优先级取决于读者对第一人称姿态估计或多视图几何细化的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Head-mounted stereo fisheye cameras provide a compact view of the wearer's body, but strong distortion, partial visibility and a short baseline make 3D pose estimation difficult. Existing refinement decoders sample image features independently in each view, without requiring the samples to correspond to a common 3D hypothesis. We introduce EgoRayFormer, a causal pose estimator that couples stereo feature sampling and geometric refinement in ray space. For each joint, the decoder projects shared 3D hypotheses along and around its viewing ray into both images. A geometric branch then corrects the projected joint locations and intersects the resulting rays; a learned gate blends this geometric estimate with a learned pose update. This formulation introduces an explicit stereo constraint while retaining flexibility when the rays provide weak depth constraints. In local evaluations on the official device-relative test splits, EgoRayFormer achieves three-seed mean MPJPEs of 17.64 mm on UnrealEgo2 and 49.55 mm on UnrealEgo-RW, improving to 47.57 mm with UnrealEgo2 pre-training. In paired validation ablations, removing the geometric branch increases MPJPE in all three seeds at both input resolutions. With a common ResNet-18 encoder and input resolution, our system reduces RW test MPJPE by 9.09 mm relative to the device-relative EgoPoseFormer baseline. A separate protocol analysis quantifies the difference between device-relative and oracle-root evaluation.

</details>

#### 2026-10-19 - CAOS-SLAM: Class-Agnostic Object-Aware Real-Time vSLAM for Dynamic Environments

**Authors:** Gaia Borghi, João Carlos Virgolino Soares, Angelo Bratta, Shahab Heshmati-Alamdari, Claudio Semini
**Links:** [abs](https://arxiv.org/abs/2610.26633) - [pdf](https://arxiv.org/pdf/2610.26633)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CAOS-SLAM: Class-Agnostic Object-Aware Real-Time vSLAM for Dynamic Environments
- 作者：Gaia Borghi, João Carlos Virgolino Soares, Angelo Bratta, Shahab Heshmati-Alamdari, Claudio Semini
- 出版日期：2026-10-19T16:00:00Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.26633) | [PDF](https://arxiv.org/pdf/2610.26633)

### 一句话总结
CAOS-SLAM 在 ORB-SLAM3 基础上引入混合感知流程，实时检测、跟踪并过滤语义已知与未见过的运动物体，以减少动态特征对定位与建图的干扰。

### 研究问题
动态环境中的运动物体会引入错误观测，破坏地图重建并降低定位精度。现有 vSLAM 方法常依赖预定义语义类别或昂贵的逐像素分类，限制了其在真实场景中的鲁棒性或适用性。论文旨在解决对语义已知和此前未见运动物体的实时检测、跟踪与动态特征剔除问题。

### 核心思路/方法
论文提出 CAOS-SLAM，一个动态 vSLAM 框架，扩展 ORB-SLAM3 并加入混合感知流程，用于实时检测、跟踪和过滤语义已知及此前未见过的运动物体。方法包括：按需执行全景分割用于物体发现；通过未分类区域的深度聚类实例化候选未知物体；在全景分割更新之间，利用可用的轻量检测或基于世界坐标系 Kalman 预测、深度一致性和外观相似性的时序掩码传播来更新持续物体轨迹；随后利用估计的物体运动从 SLAM 流程中剔除动态特征。

### 主要贡献
- 提出 CAOS-SLAM 动态 vSLAM 框架，扩展 ORB-SLAM3，支持对语义已知和未见运动物体的实时检测、跟踪与过滤。
- 设计混合感知流程：按需全景分割、基于深度聚类的未知物体实例化，以及结合轻量检测或时序掩码传播的持续物体跟踪。
- 利用估计的物体运动剔除动态特征，提升动态环境下的定位表现。
- 摘要称在多个动态 RGB-D 数据集和真实实验上优于现有动态 vSLAM 方法：未知动态物体场景定位误差最高降低 59%，严重遮挡场景最高降低 88%，在笔记本电脑上达到 30 FPS 的中位处理速率。
- 跟踪模块提供物体轨迹和速度估计，摘要称可支持动态环境下感知、导航和运动规划等潜在应用。

### 局限性
摘要未提供足够信息说明方法在极端场景、计算资源受限平台、长期运行稳定性或失败模式方面的局限。摘要提到代码和数据集将在接收后发布，但未提供具体实验细节、数据集名称或消融结果。

### 阅读优先级
高。理由：该论文直接针对动态环境下 vSLAM 的鲁棒性与实时性问题，提出类无关物体感知与动态特征剔除框架，并给出定位误差降低和 30 FPS 的摘要级结果；对动态 SLAM、机器人感知与导航相关研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Robust visual Simultaneous Localization and Mapping (vSLAM) in dynamic environments faces challenges due to the presence of moving objects that may introduce erroneous observations, corrupt the map reconstruction and overall degrade localization accuracy. Existing vSLAM approaches often rely on predefined semantic classes or costly pixel-wise classification, limiting their robustness or applicability in real-world scenarios. This paper presents CAOS-SLAM, a dynamic vSLAM framework that extends ORB-SLAM3 with a hybrid perception pipeline to detect, track, and filter both semantically known and previously unseen moving objects in real-time. On-demand panoptic segmentation is performed for object discovery, with candidate unknown objects instantiated through depth-based clustering of unclassified regions. Between panoptic updates, persistent object tracks are updated using lightweight detection when available or temporal mask propagation based on world-frame Kalman prediction, depth consistency, and appearance similarity. The estimated object motion is then used to reject dynamic features from the SLAM pipeline. Experimental results on multiple dynamic RGB-D datasets and real-world experiments demonstrate improved localization accuracy over state-of-the-art dynamic vSLAM approaches, achieving up to 59% lower localization error in scenes characterized by unknown dynamic objects and up to 88% lower error in heavily occluded scenes, while achieving a median processing rate of 30 FPS on a laptop. Furthermore, the tracking module provides estimates of object trajectories and velocities, supporting potential future applications in perception, navigation, and motion-planning tasks in dynamic environments. Code and dataset will be released upon acceptance.

</details>

#### 2026-10-19 - PnP-Transformer: A Neural Pose Solver for 6D Object Pose Estimation

**Authors:** Emirkan Burak Yilmaz, Yakup Genc
**Links:** [abs](https://arxiv.org/abs/2610.26096) - [pdf](https://arxiv.org/pdf/2610.26096)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, mapping, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PnP-Transformer: A Neural Pose Solver for 6D Object Pose Estimation
- 作者：Emirkan Burak Yilmaz, Yakup Genc
- 出版日期：2026-10-19T09:57:44Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次分类
- 链接：[摘要](https://arxiv.org/abs/2610.26096) / [PDF](https://arxiv.org/pdf/2610.26096)

### 一句话总结
论文提出 PnP-Transformer，一种无需迭代、可微的神经位姿求解器，用来替代经典 PnP-RANSAC，并在零样本 6D 物体位姿估计流程中评估其精度与延迟表现。

### 研究问题
论文关注 6D 物体位姿估计中的位姿求解环节：如何以无需迭代、可微的方式，从预测的半稠密 2D-3D 对应场及置信度分数中回归 6D 物体位姿，作为经典 PnP-RANSAC 的替代方案，并考察其在实际零样本流程中的精度和延迟权衡。

### 核心思路/方法
- 设计 PnP-Transformer 作为神经位姿求解器，输入为预测的半稠密 2D-3D 对应场及置信度分数。
- 将几何输入映射到连续潜空间，并直接回归 6D 物体位姿。
- 定位为无需迭代、可微的经典 PnP-RANSAC 替代方案。
- 将其集成到零样本 6D 位姿估计流程中，对应模块与位姿求解器分开训练。
- 与 EPnP-RANSAC 替换实验对比，分析精度与延迟的权衡。

### 主要贡献
- 提出 PnP-Transformer 神经位姿求解器，作为经典 PnP-RANSAC 的无需迭代、可微替代方案。
- 在七个核心 BOP 基准数据集上取得 41.2% 平均 AR，延迟为 0.46 s/obj；摘要称其超过除 Co-op（58.4% AR）之外的所有先前基线，例如 RayPose（39.1% AR）。
- 通过零样本 6D 位姿估计流程的集成评估，展示了求解器的实际可用性。
- 通过替换为 EPnP-RANSAC 的对照，揭示了精度-延迟权衡：RANSAC 替代方案在七个数据集中的六个上更优，平均 AR 达 52.2%，但每物体额外增加 60 ms。
- 摘要提供代码与预训练模型链接。

### 局限性
- 摘要未提供足够信息说明方法在大规模场景、遮挡、对称物体或不同对应质量下的具体鲁棒性细节。
- 摘要未提供足够信息说明训练数据规模、网络结构细节、推理硬件条件及延迟测量环境。
- 摘要未提供足够信息解释 PnP-Transformer 与 EPnP-RANSAC 精度差距的具体原因。
- 摘要未提供足够信息说明在七个 BOP 数据集上的逐数据集完整结果与失败案例分析。

### 阅读优先级
中。理由：论文主题集中在 6D 位姿估计的位姿求解环节，涉及经典 PnP-RANSAC 的可微神经替代与精度-延迟权衡，对相关方向有参考价值；但摘要已明确显示其平均 AR 低于同流程下的 EPnP-RANSAC 替代方案，且摘要未提供足够信息判断其更广泛适用性，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

We present PnP-Transformer, a neural pose solver designed as an iterative-free, differentiable alternative to classical PnP-RANSAC algorithms. PnP-Transformer regresses the 6D object pose by processing predicted semi-dense 2D-3D correspondence fields alongside confidence scores, while mapping geometric inputs into a continuous latent space. To evaluate its practical utility, we integrate PnP-Transformer into a zero-shot 6D pose estimation pipeline, where the correspondence module and pose solver are trained separately. PnP-Transformer achieves a 41.2% mean AR score with low latency (0.46 s/obj) on seven core BOP benchmark datasets, surpassing all prior baselines (such as RayPose with 39.1% AR) but one (Co-op with 58.4% AR). When the pose solver is replaced with EPnP-RANSAC (similar to Co-op) while keeping the correspondence module unchanged, the RANSAC alternative outperforms PnP-Transformer on six of the seven datasets by reaching 52.2% mean AR at a cost of an additional 60 ms per object, revealing an accuracy-latency trade-off. Code and pretrained models are available: https://github.com/ebylmz/pnp-transformer

</details>

#### 2026-10-19 - OV-PEAR: Observation-Verified Pose-Scale Estimation and Reconstruction for Unknown Industrial Manipulation Objects

**Authors:** Guoqin Tang, Qingxuan Jia, Yichen Tan, Zihang Lv, Ruiquan Wang, Zeyuan Huang, Gang Chen
**Links:** [abs](https://arxiv.org/abs/2610.25840) - [pdf](https://arxiv.org/pdf/2610.25840)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, pose estimation, manipulation, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OV-PEAR: Observation-Verified Pose-Scale Estimation and Reconstruction for Unknown Industrial Manipulation Objects
- 作者：Guoqin Tang, Qingxuan Jia, Yichen Tan, Zihang Lv, Ruiquan Wang, Zeyuan Huang, Gang Chen
- 出版日期：2026-10-19T05:51:41Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要页](https://arxiv.org/abs/2610.25840)｜[PDF](https://arxiv.org/pdf/2610.25840)

### 一句话总结
OV-PEAR 面向未知工业操作物体，提出一个经观测验证的三阶段框架，同时完成物体级 3D 重建和位姿-尺度估计，以摆脱对 CAD 模型、物体专用训练数据或稳定工作单元的依赖。

### 研究问题
精细工业机器人操作需要 6D 位姿、尺度以及可直接用于操作的 3D 模型。摘要指出，现有工业位姿估计依赖 CAD 模型、物体专用训练数据或稳定工作单元，因此难以用于未见物体；零样本方法则受单视角遮挡、生成偏差和尺度不确定性影响。论文要解决的问题是：对未知工业物体，如何在不依赖上述先验或假设的情况下，获得可用的 3D 模型以及位姿和尺度估计。

### 核心思路/方法
论文提出 OV-PEAR，一个以物体为中心、包含三个阶段并经观测验证的流水线：

1. 分割 RGB-D 实例，并生成物体级 3D 假设；
2. 通过外观感知的视角检索、显式尺度搜索和可见性敏感配准，将假设锚定到机器人坐标系；
3. 将多视角 RGB-D 证据反投影到物体规范坐标系，验证体素占用、抑制幻觉，并生成可复用的可信物体模型。

摘要还提到，模型库和位姿-尺度日志支持短期的物体级状态维护。

### 主要贡献
- 提出 OV-PEAR 框架，用于未知工业物体的 3D 重建与位姿-尺度估计，并以观测验证作为核心机制。
- 设计三阶段物体中心流水线，涵盖实例分割与 3D 假设生成、机器人坐标系锚定、多视角体素占用验证与可信模型生成。
- 在 BOP-Industrial 上报告平均 AR 为 0.657，并在真实场景中改善位姿与体素级几何一致性。
- 在真实机器人连接器装配任务中报告 99.67% 抓取成功率和 84.00% 装配成功率。
- 模型库与位姿-尺度日志支持短期的物体级状态维护，报告速度为 0.02 ms/frame。

### 局限性
- 摘要未提供足够信息说明方法对极端遮挡、严重传感器噪声或高度透明/反光工业物体的具体表现。
- 摘要未提供足够信息说明三阶段各模块的消融实验、失败案例和计算资源需求。
- 摘要未提供足够信息说明 BOP-Industrial 上的评测协议细节、对比方法完整列表，以及真实场景实验规模。
- 摘要未提供足够信息说明“短期物体级状态维护”的时间范围、适用边界与长期稳定性。
- 摘要未提供足够信息说明方法对机器人坐标系标定误差、视角检索失败或尺度搜索失败的鲁棒性。

### 阅读优先级
中。理由：该论文与未知物体 6D 位姿、尺度估计、机器人操作和 3D 重建直接相关，且摘要给出了量化结果和真实机器人验证；但摘要未展开方法细节、消融与失败分析。若关注零样本工业物体位姿估计、观测验证式重建或机器人装配，优先级可提高至高；若仅关心通用 6D 位姿跟踪或大规模场景重建，则优先级为中等。

</details>

<details>
<summary>Abstract</summary>

Fine industrial robotic manipulation requires 6D pose, scale, and an operation-ready 3D model. Existing industrial pose estimation relies on CAD models, object-specific training data, or stable workcells, limiting use with unseen objects; zero-shot methods suffer from single-view occlusion, generative bias, and scale uncertainty. We present OV-PEAR, an observation-verified framework for 3D reconstruction and pose-scale estimation of unknown industrial objects. Its three-stage object-centric pipeline: (1) segments RGB-D instances and generates object-level 3D hypotheses; (2) anchors them to the robot frame via appearance-aware view retrieval, explicit scale search, and visibility-sensitive registration; (3) back-projects multi-view RGB-D evidence into the object-canonical frame to verify voxel occupancy, suppress hallucinations, and produce reusable trusted object models. On BOP-Industrial, OV-PEAR achieves 0.657 average AR and improves pose and voxel-level geometric consistency in real scenes; real-robot connector assembly reaches 99.67% grasp and 84.00% assembly success. The model library and pose-scale log enable short-term object-level state maintenance at 0.02 ms/frame.

</details>

#### 2026-10-19 - Recurrent Vision Transformers for Event-Based Spacecraft Pose Estimation Under Slow Relative Motions

**Authors:** Sofia McLeod, Mohsi Jawaid, Carl Seubert, Tat-Jun Chin
**Links:** [abs](https://arxiv.org/abs/2610.25622) - [pdf](https://arxiv.org/pdf/2610.25622)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Recurrent Vision Transformers for Event-Based Spacecraft Pose Estimation Under Slow Relative Motions
- 作者：Sofia McLeod, Mohsi Jawaid, Carl Seubert, Tat-Jun Chin
- 出版日期：2026-10-19T00:52:34Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.25622 ；PDF https://arxiv.org/pdf/2610.25622

### 一句话总结
论文提出用循环视觉 Transformer（RVT）处理慢速相对运动下事件相机航天器位姿估计中事件率低、信噪比差的问题，并在真实慢速运动事件数据上验证了位姿估计精度与稳定性优于逐事件帧或固定时间窗方法。

### 研究问题
基于视觉的航天器位姿估计对交会与近距离操作（RPO）很重要，事件相机因高动态范围在轨道强光照条件下具有鲁棒性。但基于事件的航天器位姿估计（EBSPE）在追踪器与目标相对运动很慢时表现变差：事件率显著下降，数据信噪比低；而真实 RPO 轨迹出于安全常包含慢速相对运动，例如低至 1 mm/s；低照度还会加剧该问题。因此，如何处理慢速相对运动是提升 EBSPE 实用性的关键。

### 核心思路/方法
论文提出将循环视觉 Transformer（RVT）用于 EBSPE。核心思想是利用循环记忆在稀疏事件流中捕捉更长时程信息，并从完整轨迹中学习时间注意力跨度，而不是固定时间窗口。作者开发了一个基于 RVT 的热图回归器，用于产生位姿估计所需的 2D-3D 对应关系，并在代表 RPO 轨迹的慢速相对运动条件下采集的真实事件数据上进行验证。

### 主要贡献
- 针对慢速相对运动导致事件率低、信噪比差的问题，提出使用 RVT 进行基于事件的航天器位姿估计。
- 利用循环记忆捕捉稀疏事件流中的长期信息，并学习时间注意力跨度而非固定时间窗。
- 构建基于 RVT 的热图回归器以生成 2D-3D 对应关系用于位姿估计。
- 在慢速相对运动的真实事件数据上验证，结果显示相较此前逐事件帧或固定时间窗的 EBSPE 方法，位姿估计精度和稳定性更优。

### 局限性
摘要未提供足够信息。仅能看出验证基于真实事件数据，但具体数据集规模、轨迹范围、光照条件覆盖、计算开销、实时性、失败案例等均未在摘要中说明；也未给出定量指标数值和与基线方法的详细对比设置。

### 阅读优先级
高。理由：该论文直接针对 EBSPE 在真实 RPO 慢速运动场景下的关键失效模式，问题定义明确且具有实际应用背景；方法上引入 RVT 的循环记忆与可学习时间注意力跨度，针对稀疏事件流的时程建模；摘要声称在真实慢速运动事件数据上优于逐事件帧和固定时间窗方法。若关注事件相机位姿估计、航天器 RPO 或稀疏事件流时序建模，该论文值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Vision-based object pose estimation is vital for conducting spacecraft rendezvous and proximity operations (RPO). Recent research has demonstrated the robustness of event cameras against the harsh lighting conditions that often occur in orbit, thanks to the extremely high dynamic range of event sensors. However, event-based spacecraft pose estimation (EBSPE) suffers when the relative motion between the chaser and target is slow, since the event rate drops significantly, leading to data with low signal-to-noise ratio. Unfortunately, for safety reasons, real RPO trajectories often involve slow relative motions (e.g., down to 1 mm/s), and operating under low illumination exacerbates the problem. Addressing slow relative motions is thus crucial to raise the practicality of EBSPE. To this end, we propose using recurrent vision transformers (RVT) for EBSPE. The key idea is to exploit recurrent memory to capture longer-term information across sparse event streams, and to learn the temporal attention span from full trajectories rather than fixing the time window. We developed an RVT-based heatmap regressor to produce 2D-3D correspondences for pose estimation, which was validated on real event data collected under slow relative motions representative of RPO trajectories. Results indicate the superior pose estimation accuracy and stability of our RVT-based method, relative to previous per-event-frame-based or fixed-time-window EBSPE methods.

</details>

#### 2026-10-15 - Gen4P: Video Generators are 4D Perceivers

**Authors:** Yitong Xia, Zeren Jiang, Chuanxia Zheng
**Links:** [abs](https://arxiv.org/abs/2610.22371) - [pdf](https://arxiv.org/pdf/2610.22371)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gen4P: Video Generators are 4D Perceivers
- 作者：Yitong Xia, Zeren Jiang, Chuanxia Zheng
- 出版日期：2026-10-15T17:59:48Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.22371

### 一句话总结
Gen4P 提出将预训练视频生成器改造为无需迭代去噪的前馈式 4D 感知器，从单目视频中统一恢复 4D 几何与运动。

### 研究问题
如何从单目视频中恢复 4D 几何与运动，并利用预训练视频生成器的能力实现统一、前馈式的 4D 感知，而非依赖迭代去噪过程。

### 核心思路/方法
- 将预训练视频生成器重新利用为前馈式 4D 感知器，无需迭代去噪。
- 基于按需查询（on-demand querying），Gen4P 在单次编码器前向中处理干净的视频 latent，并通过轻量级 cross-attention 解码器预测所请求的 4D 属性。
- 按需查询形式支持灵活的空间采样；提出的连续时间查询进一步提供时间灵活性。
- 为增强几何知识，提出一种简单的插件式方案：将预训练的视频-深度 LoRA 作为冻结的几何先验引入，在不增加额外可训练参数的情况下提升整体性能。

### 主要贡献
- 提出 Gen4P，一个从单目视频恢复 4D 几何与运动的统一框架。
- 展示预训练视频生成器可被改造为前馈式 4D 感知器，且无需迭代去噪。
- 通过按需查询与连续时间查询，分别实现灵活的空间采样与时间灵活性。
- 提出将预训练视频-深度 LoRA 作为冻结几何先验的插件式方案，在不增加可训练参数的情况下提升性能。
- 在 3D 点跟踪、视频深度和相机位姿估计任务上取得 state-of-the-art 或具竞争力的性能；在野外视频上的定性结果展示其跟踪复杂运动并保持精细结构的能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作将视频生成预训练与统一 4D 感知结合，涉及 3D 点跟踪、视频深度和相机位姿估计等多任务，并声称达到 state-of-the-art 或具竞争力性能，对 3D 重建与多视图几何方向有参考价值；但摘要未给出具体实验细节、量化结果与失败情形，需进一步阅读原文确认适用范围与局限。

</details>

<details>
<summary>Abstract</summary>

We introduce Gen4P, a unified framework for recovering 4D geometry and motion from monocular video. We show that a pretrained video generator can be repurposed into a feed-forward 4D perceiver without iterative denoising. Building on on-demand querying, Gen4P processes clean video latents in a single encoder pass and predicts the requested 4D attributes through a lightweight cross-attention decoder. The on-demand query formulation enables flexible spatial sampling, and our proposed continuous-time queries further provide temporal flexibility. To strengthen geometric knowledge, we propose a straightforward plug-in solution by incorporating a pretrained video-depth LoRA as a frozen geometry prior, improving overall performance without adding extra trainable parameters. Gen4P achieves state-of-the-art or competitive performance on tasks of 3D point tracking, video depth and camera pose estimation. Qualitative results on in-the-wild videos illustrate its capability of tracking complex motion while maintaining the delicate structure. Together, these results demonstrate the potential of video generative pretraining for unified 4D perception. See https://gen4p.github.io for more visual results.

</details>

#### 2026-10-15 - GeoPano: Towards Geometrically Accurate 3D Reconstruction from a Single Panorama

**Authors:** Jing OU, Zidong Cao, Liaoyuan Fan, Zhuoxiao Li, Shuai Zhang, Yinrui Ren, Dongli Wu, Haoang Li, Hui Xiong, Wufan Zhao
**Links:** [abs](https://arxiv.org/abs/2610.21297) - [pdf](https://arxiv.org/pdf/2610.21297)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoPano: Towards Geometrically Accurate 3D Reconstruction from a Single Panorama
- 作者：Jing OU, Zidong Cao, Liaoyuan Fan, Zhuoxiao Li, Shuai Zhang, Yinrui Ren, Dongli Wu, Haoang Li, Hui Xiong, Wufan Zhao
- 出版日期：2026-10-15T05:42:59Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.21297) / [PDF](https://arxiv.org/pdf/2610.21297)

### 一句话总结
GeoPano 是一个面向单张全景图的馈送式（feed-forward）3D 重建框架，通过全景感知注意力聚合与混合监督策略，从单张全景图中恢复几何准确且一致的点云。

### 研究问题
从全景图（ERP 图像）直接估计几何会受到球面畸变的固有限制。常见做法是将全景图分解为无畸变的透视视图，但独立处理这些视图往往引入跨视图的几何不一致。论文旨在解决单张全景图三维重建中的球面投影畸变与跨视图几何一致性问题。

### 核心思路/方法
论文提出 GeoPano，一个单视图全景 3D 重建的馈送式框架，从单张全景图恢复几何准确且一致的点云。其方法由两项关键创新驱动：
1. **全景感知注意力聚合器**：采用精简的注意力架构，配备新颖的 Pano-Attention 机制，显式利用全景图内在的球面几何来引导跨视图交互，从而抑制几何不一致。
2. **混合监督策略**：联合在透视空间中约束细粒度局部细节，并在球面空间中约束全局结构一致性。

### 主要贡献
- 提出 GeoPano，一个用于单视图全景 3D 重建的馈送式框架，可从单张全景图恢复几何准确且一致的点云。
- 提出全景感知注意力聚合器，包含 Pano-Attention 机制，显式利用全景球面几何引导跨视图交互，以抑制几何不一致。
- 提出混合监督策略，在透视空间与球面空间中联合约束局部细节与全局结构一致性。
- 摘要称实验表明该方法在重建精度、几何一致性和视觉保真度上显著优于此前的 SOTA 方法。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集、评价指标数值、失败案例或方法适用边界等细节，因此无法基于摘要判断其局限性。

### 阅读优先级
高。理由：该论文聚焦单张全景图 3D 重建中的球面畸变与跨视图一致性这两个核心难点，提出明确的注意力机制与混合监督设计，且摘要声称在重建精度、几何一致性和视觉保真度上显著优于此前 SOTA；对 3D 重建、多视图几何以及机器人 / AR/VR 应用方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Panoramic 3D reconstruction enables the holistic recovery of complete 360 $^\circ$ scene geometry, offering significant benefits for robotics and AR/VR applications. However, directly estimating geometry from ERP images is inherently challenged by spherical distortions. To reduce spherical projection distortions, a common strategy is to decompose panoramas into distortion-free perspective views, but independently processing these views often introduces cross-view geometric inconsistencies. To address these challenges, we introduce GeoPano, a feed-forward framework for single-view panoramic 3D reconstruction that recovers a geometrically accurate and consistent point cloud from a single panorama. Our approach is driven by two key innovations: First, we propose a panoramic-aware attention aggregator, featuring a streamlined attention architecture equipped with a novel Pano-Attention mechanism, which explicitly exploits the intrinsic spherical geometry of the panorama to guide cross-view interactions, thereby suppressing geometric inconsistencies. Furthermore, we formulate a hybrid supervision strategy to jointly enforce fine-grained local details in perspective space and global structural coherence in spherical space. Experiments demonstrate that our method significantly outperforms previous SOTA approaches in reconstruction accuracy, geometric consistency, and visual fidelity.

</details>

#### 2026-10-15 - LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

**Authors:** Shiqi Che, Yijie Liu, Shuo Wang, Wenxin Liu
**Links:** [abs](https://arxiv.org/abs/2610.21199) - [pdf](https://arxiv.org/pdf/2610.21199)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation
- 作者：Shiqi Che, Yijie Liu, Shuo Wang, Wenxin Liu
- 出版日期：2026-10-15T03:58:47Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.21199) / [PDF](https://arxiv.org/pdf/2610.21199)

### 一句话总结
LIN-SLAM 将高频几何 LiDAR--惯性估计与神经隐式跟踪、持续建图和全局优化相耦合，在保持实时性的同时提升定位精度。

### 研究问题
论文指出，几何 LiDAR--惯性 SLAM 虽然状态估计高效，但缺乏神经隐式 SLAM 所具备的连续地图表示和全局优化能力；而神经隐式方法通常计算开销较大，难以兼顾实时机载运行。

### 核心思路/方法
提出一种混合方法 LIN-SLAM：将高频几何 LiDAR--惯性估计与神经隐式跟踪、持续建图以及全局优化耦合，用于准确且实时的机载 SLAM。

### 主要贡献
- 在三个数据集、覆盖 32、64、128 通道 LiDAR 配置的十二个代表性序列上，LIN-SLAM 在所评估的几何与神经隐式最先进方法中取得最低总体平均绝对轨迹误差（ATE），同时相较现有神经隐式 SLAM 方法显著降低运行时间。
- 在搭载 NVIDIA Jetson Orin NX 和 16 通道 LiDAR 的 Unitree Go2 上，LIN-SLAM 在 1.47 km 室内轨迹、具有挑战性的重复走廊环境中持续进行实时定位和神经建图，端点闭合误差仅为 0.141 m。
- 据作者所述，LIN-SLAM 是首个在移动机器人平台上实现实时在线运行、并保持最先进定位精度的神经隐式后端 LiDAR--惯性 SLAM 系统。
- 代码将在接收后发布。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、传感器退化条件、不同平台泛化能力、长期运行稳定性或计算资源下限等方面的具体限制。

### 阅读优先级
高。理由：该论文提出轻量级 LiDAR--惯性神经 SLAM，直接面向实时机载导航；摘要报告了多数据集、多种 LiDAR 通道配置下的精度与运行时间对比，以及真实机器人平台上的长轨迹实时运行结果，并声称是首个实现实时在线运行的神经隐式后端 LiDAR--惯性 SLAM 系统，具有较强的问题针对性和工程应用价值。

</details>

<details>
<summary>Abstract</summary>

Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LIN-SLAM), a hybrid method that couples high-rate geometric LiDAR--inertial estimation with neural implicit tracking, continual mapping, and global refinement for accurate real-time onboard SLAM. Experiments on twelve representative sequences from three datasets spanning 32-, 64-, and 128-channel LiDAR configurations show that LIN-SLAM achieves the lowest overall mean absolute trajectory error (ATE) among the evaluated state-of-the-art geometric and neural implicit methods, while substantially reducing runtime compared with existing neural implicit SLAM methods. On a Unitree Go2 equipped with an NVIDIA Jetson Orin NX and a 16-channel LiDAR, LIN-SLAM sustains real-time localization and neural mapping over a 1.47-km indoor trajectory through challenging repetitive corridor environments, with an endpoint closure error of only 0.141~m. To the best of our knowledge, LIN-SLAM is the first LiDAR--inertial SLAM system with a neural implicit backend to achieve real-time online operation on a mobile robotic platform while maintaining state-of-the-art localization accuracy. The code will be released upon acceptance.

</details>

#### 2026-10-15 - RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching

**Authors:** Liangjing Shao, Wanhao Liu, Zhiwei Fang, Rulin Zhou, Quanlu Zhang, Changjing Liu, Beilei Cui, Yiming Huang, Hongliang Ren
**Links:** [abs](https://arxiv.org/abs/2610.21086) - [pdf](https://arxiv.org/pdf/2610.21086)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, rendering, robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching
- 作者：Liangjing Shao, Wanhao Liu, Zhiwei Fang, Rulin Zhou, Quanlu Zhang, Changjing Liu, Beilei Cui, Yiming Huang, Hongliang Ren
- 出版日期：2026-10-15T01:40:49Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.21086，https://arxiv.org/pdf/2610.21086

### 一句话总结
RoPE-Flow 提出一种基于流匹配的端到端单目相机到机器人位姿估计框架，利用 2D 关键点热图构造图条件并生成 3D 位姿，同时通过拓扑与尺度相关损失提升不同机器人上的位姿估计表现。

### 研究问题
从单目图像估计相机到机器人的位姿对基于视觉的机器人导航与控制具有重要意义，但从 2D 观测恢复 3D 结构特征仍然困难。现有方法要么依赖耗时的迭代渲染，要么涉及复杂的 2D-3D 配准，并面临投影歧义、远端关节误差累积以及不同关节学习不均衡等问题。

### 核心思路/方法
论文提出 RoPE-Flow，一个端到端的、基于流匹配的相机到机器人位姿估计框架。方法从预测的 2D 热图出发，使用 Keypoint-centered Feature Extractor 从关键点为中心的多尺度图像块中获取位置特征与上下文表示；引入 Graph-guided Condition Generator，通过可学习邻接图，基于关键点之间的相关性为流匹配生成条件；并引入 Bone Length Loss 与 Ray-Depth Loss，用于拓扑一致性和尺度稳定性，同时采用逐关节加权以缓解不同关节预测难度不一致的问题。

### 主要贡献
- 提出 RoPE-Flow，一个端到端的基于流匹配的相机到机器人位姿估计框架。
- 设计 Keypoint-centered Feature Extractor，从预测的 2D 热图中提取关键点为中心的多尺度位置特征与上下文表示。
- 引入 Graph-guided Condition Generator，使用可学习邻接图，根据关键点相关性为流匹配生成条件。
- 引入 Bone Length Loss 和 Ray-Depth Loss，以增强拓扑一致性与尺度稳定性，并通过逐关节加权处理不同关节预测难度差异。
- 摘要称该方法在多类机器人和多相机设置下优于现有位姿估计方法，并建立了新的跨场景基准，展示零样本跨场景机器人位姿估计性能。

### 局限性
摘要未提供足够信息。摘要未提供足够信息说明方法的具体失败场景、计算开销、对特定机器人结构或相机设置的依赖程度，也未给出定量实验结果、数据集细节和与基线方法的完整比较。

### 阅读优先级
高。理由：该论文面向单目机器人位姿估计这一重要问题，提出流匹配与图条件结合的端到端框架，并声称在多类机器人、多相机以及零样本跨场景设定下取得优于现有方法的表现；若关注单目 3D 位姿估计、机器人视觉或流匹配应用，该论文具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Camera-to-robot pose estimation from a monocular image is significant for vision-based robot navigation and control. However, recovering 3D structural features from 2D observations remains a challenging task. Existing camera-to-robot pose estimation methods either rely on time-consuming iterative rendering or involve sophisticated 2D-3D registration which suffers from projection ambiguity, accumulated errors for distal joints and imbalanced learning for different joints. In this work, we propose RoPE-Flow, an end-to-end flow matching-based framework for camera-to-robot pose estimation. From the predicted 2D heatmaps, we propose a Keypoint-centered Feature Extractor to obtain positional features along with contextual representations from keypoints-centered multi-scale patches. Moreover, we introduce Graph-guided Condition Generator, which embeds a learnable adjacency map to generate condition for flow matching based on correlation among keypoints. Besides, we introduce Bone Length Loss and Ray-Depth Loss for topological consistency and scale stability, with joint-wise weighting to mitigate varied prediction difficulty across joints. The proposed method outperforms state-of-the-art methods for pose estimation across different types of robots with mutiple cameras. Besides, we establish a novel cross-scene benchmark to demonstrate the outstanding performance of RoPE-Flow on zero-shot cross-scene robot pose estimation. Meanwhile, animated visualizations are shown on the website: ropeflow.netlify.app

</details>

#### 2026-10-14 - Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

**Authors:** Dara Molloy, Terry Wu, Wonju Lee, Abhilash Nand Kumar, David Adley, Conor Ferguson, Hesam Rabeti
**Links:** [abs](https://arxiv.org/abs/2610.20958) - [pdf](https://arxiv.org/pdf/2610.20958)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments
- 作者：Dara Molloy, Terry Wu, Wonju Lee, Abhilash Nand Kumar, David Adley, Conor Ferguson, Hesam Rabeti
- 出版日期：2026-10-14T21:29:40Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.20958 ；https://arxiv.org/pdf/2610.20958

### 一句话总结
该论文在 CUDA 加速的视觉 SLAM 系统 cuVSLAM 中引入线特征扩展，以提升仓库、生产设施等低纹理环境下的视觉里程计鲁棒性。

### 研究问题
仓库和生产设施中的自主移动机器人常处于缺乏点特征的环境，例如无特征通道、均匀墙面、重复货架和镜面地板，这些环境会使基于点特征的视觉里程计失效。论文关注的核心问题是：在点特征稀缺的低纹理环境下，如何利用环境中丰富的直线边缘结构来提升视觉里程计的鲁棒性与精度。

### 核心思路/方法
论文提出对 cuVSLAM 的线特征扩展，以恢复低纹理环境中直线边缘所提供的信号。方法要点包括：
- 线段使用 Plücker 坐标进行几何传输，并使用 Bartoli 和 Sturm 的最小 4-DOF 正交表示进行优化。
- 将 Cauchy 鲁棒的点到线残差及其解析雅可比直接融入 cuVSLAM 的逐帧 Gauss-Newton 位姿求解。
- 在 Schur 补滑动窗口 bundle adjustment 中联合优化相同的线状态。
- 使用自适应信息权重，使线特征在点特征变得稀缺时承担更多估计任务。
- 该扩展通过向现有求解器添加残差块实现，而不是引入第二个估计器；关闭时完全退化为未修改的点特征管线。

### 主要贡献
- 提出一种面向 cuVSLAM 的线特征扩展，用于低纹理环境下的鲁棒视觉里程计。
- 将 Plücker 坐标、Bartoli-Sturm 最小 4-DOF 表示、Cauchy 鲁棒点到线残差及解析雅可比集成到 cuVSLAM 的位姿求解与滑动窗口 bundle adjustment 中。
- 设计自适应信息权重，使线特征在点特征稀缺时承担更多估计负担。
- 在 RGB-D 模式下，使用 SE(3) Umeyama 对齐且无尺度校正进行评估，线特征在 TUM RGB-D Freiburg3 的 22 个序列上将平均绝对轨迹误差降低 38.5%，在 8 个 Replica 房间和办公室序列上降低 30.1%；其中中位平移误差降低 38.9%，中位旋转误差降低 66.4%，所有测试配置中零跟踪失败。
- 该扩展以添加残差块的方式实现，不引入第二估计器，关闭时完全退化为原始点特征管线。

### 局限性
摘要未提供足够信息。摘要未说明方法的计算开销、实时性能、内存占用、不同硬件平台上的表现、失败案例、参数敏感性、与其它线特征 SLAM 方法的对比细节，也未说明在非 RGB-D 模式或真实室外环境中的泛化能力。

### 阅读优先级
高。理由：该论文针对低纹理环境下点特征视觉里程计失效这一明确且实际的问题，提出了与 CUDA 加速 cuVSLAM 集成的线特征扩展，并给出了在 TUM RGB-D 与 Replica 数据集上的量化提升和零跟踪失败结果；对于关注视觉 SLAM、视觉里程计、低纹理鲁棒性和机器人导航的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present high-contrast linear edges stable across wide viewpoint changes. A line-feature extension to cuVSLAM, a CUDA-accelerated visual-SLAM system, is presented that recovers this signal. Lines are parameterised as Plücker coordinates for geometric transport and as the minimal 4-DOF orthonormal representation of Bartoli and Sturm for optimisation; a Cauchy-robust point-to-line residual with analytic Jacobians is folded directly into cuVSLAM's per-frame Gauss-Newton pose solve, and the same line state is jointly refined in the Schur-complement sliding-window bundle adjustment. An adaptive information weight causes lines to assume more of the estimation burden exactly as point features become scarce, and the extension adds residual blocks to existing solvers rather than introducing a second estimator, reducing exactly to the unmodified point pipeline when disabled. Evaluated in RGB-D mode under SE(3) Umeyama alignment with no scale correction, line features reduce mean absolute trajectory error by 38.5% over the 22 sequences of the TUM RGB-D Freiburg3 collection and by 30.1% over the 8 Replica room and office sequences, where median translation error falls by 38.9% and median rotation error by 66.4%, with zero tracking failures in any configuration tested.

</details>

#### 2026-10-14 - Smart Fusion for Adaptive Visual-IMU Weighting in cuVSLAM Sparse Bundle Adjustment

**Authors:** Wonju Lee, Dara Molloy, Abhilash Nand Kumar, Onias Castelo, Petar Trslic, David Adley, Conor Ferguson, Hesam Rabeti
**Links:** [abs](https://arxiv.org/abs/2610.20226) - [pdf](https://arxiv.org/pdf/2610.20226)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Smart Fusion for Adaptive Visual-IMU Weighting in cuVSLAM Sparse Bundle Adjustment
- 作者：Wonju Lee, Dara Molloy, Abhilash Nand Kumar, Onias Castelo, Petar Trslic, David Adley, Conor Ferguson, Hesam Rabeti
- 出版日期：2026-10-14T14:09:42Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.20226 ；PDF: https://arxiv.org/pdf/2610.20226

### 一句话总结
本文针对 cuVSLAM 稀疏束调整中视觉与 IMU 权重固定、无法运行时自适应的问题，引入标量 α 调节视觉信息矩阵相对 IMU 预积分约束的权重，并训练一个轻量级视觉质量估计器（VQE）来预测每个 SBA 应采用的权重区间。

### 研究问题
在 cuVSLAM 中，视觉与 IMU 残差在稀疏束调整（SBA）中融合，但权重由预先标定的噪声协方差固定，缺乏在运行时自适应调整视觉-惯性平衡的机制。论文要解决的核心问题是：如何根据运行时视觉质量动态调整视觉与 IMU 的相对权重，以改善轨迹精度。

### 核心思路/方法
- 引入一个标量 α ≥ 1，用于放大视觉信息矩阵相对于 IMU 预积分约束的权重。
- 在候选集合 {1.0, 2.0, 5.0, 10.0, 20.0} 上观察轨迹表现，形成两个经验性能区间：
  - IMU-TRUST 区间：α ∈ {1, 2}，接近标定基线；
  - VISION-TRUST 区间：α ∈ {10, 20}；
  - α = 5 被视为过渡情况。
- 区间内差异相对区间间差异较小，因此将 α 选择简化为二值决策。
- 训练一个轻量级 Visual Quality Estimator（VQE），实现为多层感知机，含 914 个可训练参数；输入为 tracker 已维护的统计量构成的 10 维视觉质量特征向量，输出为每个 SBA 的区间预测。

### 主要贡献
- 提出一种在 cuVSLAM SBA 中运行时自适应调整视觉-IMU 权重的方法。
- 通过 α 候选集实验观察到两个经验性能区间，并据此将 α 选择简化为二值决策。
- 设计轻量级 VQE（MLP，914 个可训练参数），基于现有 tracker 统计量进行每个 SBA 的区间预测。
- 在 EuRoC MAV 和 TUM-VI Room 上，所提方法分别将平均 RMSE APE 降低 27.7%，在 LOOCV 下降低 14.9%。

### 局限性
摘要未提供足够信息。摘要未说明 VQE 的推理开销、对不同场景或传感器的泛化能力、α 候选集之外的行为、区间划分是否依赖特定数据集，以及失败案例或消融实验细节。摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对视觉-惯性 SLAM 中固定权重这一具体问题提出轻量自适应方案，并在标准数据集上报告了明确的误差下降；但摘要仅给出高层方法和两个数据集上的汇总结果，未展开实验细节与泛化验证。若关注 VSLAM、稀疏束调整或视觉-惯性融合权重自适应，值得阅读；若需要完整方法对比或工程部署细节，需进一步查看正文。

</details>

<details>
<summary>Abstract</summary>

In cuVSLAM, visual and inertial measurement unit (IMU) residuals are fused in sparse bundle adjustment (SBA) with a weighting fixed by pre-calibrated noise covariances, leaving no mechanism to adapt the visual-inertial balance at runtime. We introduce a scalar $α\geq1$ that upscales the visual information matrix relative to the IMU preintegration constraint. Across the candidate set $\{1.0,2.0,5.0,10.0,20.0\}$, the resulting trajectories form two empirical performance regimes. The IMU-TRUST regime contains $α\in\{1,2\}$ near the calibrated baseline, while the VISION-TRUST regime contains $α\in\{10,20\}$. The intermediate value $α=5$ is treated as a transition case. Differences within each regime are small relative to those observed between the regimes. This structure motivates reducing $α$-selection to a binary decision. We train a lightweight Visual Quality Estimator (VQE), implemented as a multilayer perceptron with 914 trainable parameters. It maps a 10-dimensional visual quality feature vector assembled from statistics already maintained by the tracker to a per-SBA regime prediction. The proposed method reduces mean RMSE APE by $27.7\%$ and by $14.9\%$ under leave-one-out cross-validation (LOOCV) on EuRoC MAV and TUM-VI Room, respectively.

</details>

#### 2026-10-14 - Why 3D Reconstruction Breaks Down on Under-Ice AUV Video, and How to Predict It

**Authors:** Ana-Ştefania Kogălniceanu, Klára Orbán, Ashwin Nedungadi, Stefan Lüdtke, Kuderna-Iulian Benţa
**Links:** [abs](https://arxiv.org/abs/2610.19993) - [pdf](https://arxiv.org/pdf/2610.19993)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, SfM, feature matching, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Why 3D Reconstruction Breaks Down on Under-Ice AUV Video, and How to Predict It
- 作者：Ana-Ştefania Kogălniceanu, Klára Orbán, Ashwin Nedungadi, Stefan Lüdtke, Kuderna-Iulian Benţa
- 出版日期：2026-10-14T11:10:03Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.19993) / [PDF](https://arxiv.org/pdf/2610.19993)

### 一句话总结
论文在相同的南极冰下 AUV 视频上测试四类 3D 重建方法并观察到它们均失败，且失败方式各异，作者将这些失败统一归因于同一采集条件——相机基线与场景深度之比过小，并提出可在数分钟内标记此类失败的检测系统。

### 研究问题
冰下 AUV 视频的 3D 结构重建结果不准确，但尚不确定原因在于重建方法的缺陷，还是采集系统本身的固有限制。论文试图回答：不同类别的重建方法在同一冰下 AUV 视频上会如何失败，这些失败是否可由共同的采集条件解释，以及能否提前预测这种失败。

### 核心思路/方法
- 数据：使用同一段南极冰下 AUV 视频（Icefin，Kamb Ice Stream）。
- 对比四类重建模型：
  1. 经典特征匹配 SfM；
  2. 可微光度 splatting；
  3. 体深度融合（volumetric depth fusion）；
  4. 无位姿（pose-free）前馈基础模型。
- 观察并记录每种方法各自不同的失败模式。
- 分析表明四种失败均与同一采集条件一致：较小的“相机基线—场景深度比”。
- 基于该分析，提出一个检测系统，用于在数分钟内标记此类失败，避免数小时的计算浪费。

### 主要贡献
- 在同一冰下 AUV 视频上系统比较了四类重建模型，报告它们全部失败。
- 刻画了四类失败的具体表现：几乎完全配准失败、几乎无结构；光度指标健康但几何破碎；持续存在的覆盖伪影；跨块尺度不稳定。
- 提出四种失败与同一采集条件（小相机基线—场景深度比）一致的解释。
- 提出一个可在数分钟内标记该类失败的检测系统，以减少无效计算开销。

### 局限性
- 实验仅基于摘要所述的一段南极冰下 AUV 视频（Icefin，Kamb Ice Stream），样本量与场景多样性有限。
- 摘要未提供四类方法的实现细节、参数设置、定量评价指标数值与对比基准。
- 摘要未提供检测系统的具体设计、阈值、验证方式与性能数据。
- 摘要未提供“小相机基线—场景深度比”的量化定义或取值范围。
- 摘要未说明该解释是否在其他冰下或非冰下数据上得到验证。
- 摘要未提供足够信息说明代码、数据或模型是否公开。

### 阅读优先级
中。理由：该工作聚焦冰下 AUV 视频 3D 重建的系统性失败诊断，并强调失败与采集条件的关联以及提前检测，对从事水下/极端环境视觉与 3D 重建的研究者有直接参考价值；但摘要未给出定量结果与检测系统细节，若关注具体方法性能或可复现性，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Reconstruction of 3D structures using under-ice AUV video footage has been inaccurate, although it is not certain whether this is due to shortcomings in the methods or an inherent deficiency of the capture system. We test four different models for reconstruction on the same Antarctic under-ice AUV video (Icefin, Kamb Ice Stream): classical feature matching SfM, differentiable photometric splatting, volumetric depth fusion, and a pose-free feed-forward foundation model. All four fail, each in a distinct way: near-total registration yielding almost no structure, geometrically broken output despite healthy photometric metrics, a persistent coverage artifact, and unstable cross-chunk scale. We show that all four are consistent with the same capture regime, a small camera-baseline-to-scene-depth ratio. Following our analysis, we propose a detection system that flags this type of failure in minutes, rather than hours of wasted compute.

</details>

#### 2026-10-14 - MicroSDF: Microfacet-Driven Hybrid Neural SDFs for Mixed-Reflectance Surface Reconstruction

**Authors:** Lejia Ye, Yuhua Xu, Yulan Guo, Lian Xu, Xiaohu Zhang
**Links:** [abs](https://arxiv.org/abs/2610.19681) - [pdf](https://arxiv.org/pdf/2610.19681)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction, NeRF

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MicroSDF: Microfacet-Driven Hybrid Neural SDFs for Mixed-Reflectance Surface Reconstruction
- 作者：Lejia Ye, Yuhua Xu, Yulan Guo, Lian Xu, Xiaohu Zhang
- 出版日期：2026-10-14T07:05:54Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.19681) / [PDF](https://arxiv.org/pdf/2610.19681)

### 一句话总结
MicroSDF 提出了一种基于微表面理论的神经隐式框架，将反射与非反射表面的几何与反射率建模统一起来，以提升混合反射场景下的重建鲁棒性与物理合理性。

### 研究问题
真实环境中反射表面与非反射表面共存，二者对建模的需求不同。现有方法通常将这两类表面分开处理，导致泛化能力受限，物理合理性不足。论文旨在通过统一的神经隐式框架同时建模几何与反射率，弥合这一差距。

### 核心思路/方法
论文提出 MicroSDF，利用微表面理论驱动几何与反射率建模，包含三项核心设计：
1. **微表面引导的几何模型**：从符号距离场（SDF）中提取多尺度表面法线，包括宏观法线与微表面法线，并引入微表面法线一致性损失进行正则化，以约束物理合理的表面朝向。
2. **增强的双分支颜色模型**：镜面分支利用微表面法线建模高频反射；普通分支不同于先前工作，使用反射方向（而非观察方向）来更好地建模漫反射与低频镜面成分。
3. **检测引导的颜色混合策略**：基于反射先验自适应融合颜色输出，相比隐式学习的混合权重更具物理直观性。

此外，论文结合定制的多阶段优化方案，以提升混合反射表面的重建质量。

### 主要贡献
- 提出 MicroSDF，一个通过微表面理论统一几何与反射率建模的神经隐式框架。
- 引入微表面引导的几何模型，提取多尺度表面法线并用法线一致性损失进行正则化。
- 设计增强的双分支颜色模型，其中普通分支采用反射方向建模漫反射与低频镜面。
- 提出检测引导的颜色混合策略，基于反射先验自适应融合颜色输出。
- 在 DTU、Shiny Blender、Ref-NeRF 和 DeepVoxels 数据集上进行大量实验，摘要声称取得 state-of-the-art 性能。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法的具体失败场景、计算开销、对特定反射类型的适用边界或数据集覆盖范围之外的泛化限制。

### 阅读优先级
高。理由：该论文针对混合反射表面重建这一具有挑战性的问题，提出了结构清晰的三项创新，并在多个常用数据集上声称达到 state-of-the-art，且涉及神经隐式 SDF 与微表面理论的结合，对 3D 重建与多视图几何方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate 3D reconstruction in real-world environments remains a significant challenge due to the coexistence of reflective and non-reflective surfaces, which pose distinct modeling demands. Existing methods often treat these surface types separately, limiting their generalizability and physical plausibility. To bridge this gap, we propose MicroSDF, a novel neural implicit framework that facilitates geometry and reflectance modeling through microfacet theory. Our approach incorporates three core innovations: (i) a microfacet-guided geometry model that extracts multi-scale surface normals (macroscopic and microfacet) from a signed distance field (SDF), regularized by a proposed microfacet normal consistency loss to enforce physically plausible surface orientations; (ii) an enhanced dual-branch color model, where the specular branch leverages the microfacet normals to model high-frequency reflectance, and the vanilla branch, unlike prior works, uses reflection direction (instead of viewing direction) to better model diffuse and low-frequency specular components; and (iii) a detection-guided color blending strategy that adaptively fuses the color outputs based on reflection priors, providing more physically intuitive blending than implicitly learned blending weights. Combined with a tailored multi-stage optimization scheme, the proposed MicroSDF achieves robust and high-fidelity reconstruction across reflective and non-reflective surfaces. Extensive experiments on DTU, Shiny Blender, Ref-NeRF, and DeepVoxels datasets demonstrate state-of-the-art performance, establishing a new direction for physically grounded neural reconstruction.

</details>

#### 2026-10-14 - Remember, Revisit, Revise: Scaffold Memory for Long-Horizon 3D Geometry

**Authors:** Soumick Sarker, Mengmi Zhang
**Links:** [abs](https://arxiv.org/abs/2610.19674) - [pdf](https://arxiv.org/pdf/2610.19674)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, simultaneous localization and mapping, SLAM, camera pose estimation, pose estimation, depth estimation, point cloud reconstruction, novel view synthesis, view synthesis, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Remember, Revisit, Revise: Scaffold Memory for Long-Horizon 3D Geometry
- 作者：Soumick Sarker, Mengmi Zhang
- 出版日期：2026-10-14T06:50:28Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.19674) | [PDF](https://arxiv.org/pdf/2610.19674)

### 一句话总结
论文提出 SMORE，为冻结的几何基础模型配备可修订的外部记忆，以缓解长时序视频中位姿与三维重建误差累积、且难以回溯修正的问题。

### 研究问题
论文关注长时序视频序列下的几何基础模型推理问题。摘要指出两类现有方法的不足：
1. 前馈模型将长序列按独立、固定长度的帧窗口处理再对齐预测，导致位姿与重建误差跨窗口累积；
2. 流式模型虽保留过去帧信息以辅助未来预测，但当后续观察揭示先前估计存在错误时，无法修订早先估计。

因此核心问题是：如何让几何基础模型在长时序推理中既能利用历史信息，又能根据新证据修正已有估计。

### 核心思路/方法
论文提出 Scaffold MemOry for Revision（SMORE）框架，为冻结的几何基础模型配备可修订的外部记忆，用于长时序推理。

其设计受生物大脑海马体联想记忆启发：海马体将空间情境与感官体验关联。SMORE 据此将“观察者所在位置”与“其观察到的内容”相关联，使过去观察能够被存储、检索、与新证据核验，并在检测到不一致时进行修订。

摘要强调该框架不改变冻结的几何基础模型，而是以外部记忆作为接口扩展其长时序推理能力。

### 主要贡献
摘要中列出的贡献包括：
1. 提出 SMORE，一个为冻结几何基础模型提供可修订外部记忆的长时序推理框架。
2. 在 8 个具竞争力的几何模型、5 个数据集上评估 SMORE，任务覆盖相机位姿估计、多视角深度估计、三维点云重建、SLAM 和新视角合成。
3. 在所有被评估模型上，SMORE 一致提升长序列位姿估计。
4. 多视角深度误差最多降低 58%。
5. 三维点云重建的 Chamfer 距离最多降低 43%。
6. 长时序 SLAM 中平均轨迹误差低至 2.9 cm。
7. 通过保留修正后的位姿与观察，进一步提升大规模三维场景重建的保真度与空间一致性。
8. 结论上，将可修订外部记忆确立为一种灵活接口，使预训练几何模型从固定上下文预测走向长视觉序列上的迭代、纠错式推理。

### 局限性
摘要未提供足够信息。论文摘要未说明 SMORE 的计算开销、记忆容量上限、对超参数或数据集特性的敏感性、失败案例，也未给出与更多基线在全部任务上的逐项对比细节；这些方面的局限性无法仅凭摘要判断。

### 阅读优先级
高。理由：该论文针对长时序三维几何中的误差累积与不可修订问题提出通用框架，并在 8 个模型、5 个数据集、5 类任务上报告一致改进，且覆盖位姿、深度、点云、SLAM 与新视角合成，问题重要性与结论覆盖面都较强；若关注长序列三维重建、SLAM 或几何基础模型的外部记忆扩展，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Geometry foundation models estimate camera poses and 3D scene structure from video sequences, but maintaining consistent reconstructions over long horizons remains challenging. Feed-forward models process long sequences as independent, fixed-length frame windows and align their predictions, causing pose and reconstruction errors to accumulate across windows. Streaming models retain information from past frames to inform future predictions, but cannot revise earlier estimates when later observations reveal errors. To address this, we introduce Scaffold MemOry for Revision (SMORE), a framework equipping frozen geometry foundation models with a revisable external memory for long-horizon inference. Inspired by hippocampal associative memory in biological brains, which links spatial context with sensory experience, SMORE associates where an observer is with what it observes, enabling past observations to be stored, retrieved, verified against new evidence, and revised when inconsistencies are detected. We evaluate SMORE with eight competitive geometry models on five datasets spanning camera pose estimation, multi-view depth estimation, 3D point-cloud reconstruction, simultaneous localization and mapping (SLAM), and novel view synthesis. Across all evaluated models, SMORE consistently improves long-sequence pose estimation, reduces multi-view depth error by up to 58%, reduces Chamfer distance for 3D point-cloud reconstruction by up to 43%, and achieves average trajectory error as low as 2.9 cm in long-horizon SLAM. By retaining corrected poses and observations, SMORE further improves the fidelity and spatial consistency of large-scale 3D scene reconstruction. These results establish revisable external memory as a flexible interface for extending pretrained geometry models beyond fixed-context prediction toward iterative, error-correcting inference over long visual sequences.

</details>

#### 2026-10-14 - Robust Real-Time Monocular Human Pose Estimation with Insole-Based Sensor Fusion

**Authors:** Liang Yu, Tao Zhu, Xiangqing Lu, Wenjian Luo, Liming Chen
**Links:** [abs](https://arxiv.org/abs/2610.19494) - [pdf](https://arxiv.org/pdf/2610.19494)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robust Real-Time Monocular Human Pose Estimation with Insole-Based Sensor Fusion
- 作者：Liang Yu, Tao Zhu, Xiangqing Lu, Wenjian Luo, Liming Chen
- 出版日期：2026-10-14T03:14:34Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类；无二级分类）
- 链接：https://arxiv.org/abs/2610.19494 ；PDF：https://arxiv.org/pdf/2610.19494

### 一句话总结
该论文提出一种基于鞋垫传感器与单目视觉融合的部件解耦时序融合框架，旨在缓解下半身遮挡或短暂出画时纯视觉人体姿态估计的困难。

### 研究问题
论文关注实时单目人体姿态估计在视觉观测不完整时面临的挑战，特别是下半身遮挡或短暂出画间隔下，纯视觉系统难以重建物理合理的下肢运动并可靠估计足地接触。作者希望探究简单的足底压力与加速度传感器是否能有效解决这些由视觉局限引发的问题。

### 核心思路/方法
论文首先采集了一个同步多模态数据集，然后提出一种部件解耦的时序融合框架。该模型将足部传感特征融合进下半身分支，以补偿不完整的视觉证据；同时使用一个轻量级协调器在上半身与下半身时序表示之间交换信息，以维持全身一致性。框架在三种代表性实时视觉骨干上进行评估，这些骨干分别基于 2D 关键点、3D landmarks 和 SMPL-based human mesh recovery。

### 主要贡献
- 采集了一个同步多模态数据集。
- 提出部件解耦时序融合框架，将足部传感特征融合进下半身分支，并利用轻量级协调器维持上下半身时序表示的全身一致性。
- 在基于 2D 关键点、3D landmarks 和 SMPL-based human mesh recovery 的三种代表性实时视觉骨干上评估该框架。
- 定量实验表明，引入简单足部传感器相比纯视觉基线，能持续提升姿态精度、运动平滑度和步态相关测量指标；在遮挡和短暂视觉丢失条件下增益最显著。
- 结果表明，在相机观测暂时不可用时，非侵入式足部传感可提供重要且互补的物理可观测性。

### 局限性
摘要未提供足够信息，无法确定具体局限性，例如数据集规模、传感器佩戴舒适性、泛化能力、计算开销、失败案例或与更多基线方法的比较细节。摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对单目人体姿态估计中遮挡与短暂出画这一常见且困难的问题，提出鞋垫传感与视觉融合的明确技术路线，并声明在多个实时视觉骨干上验证了持续改进，主题与 3D 重建及多视图几何相关，且强调实时性与物理可观测性，具有较高的潜在参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-time monocular human pose estimation is an important sensing component for human-centered intelligent systems. While recent camera-based methods have achieved impressive accuracy, fundamental challenges persist, particularly when visual observations are incomplete, such as during lower-body occlusion or short out-of-frame intervals. In these challenging but common scenarios, vision-only systems often struggle to reconstruct physically plausible lower-limb motion and reliable foot-ground contact. Due to the highly unobtrusive and wearable nature of smart insoles, this paper investigates whether simple plantar pressure and acceleration sensors can effectively resolve these visually induced limitations. To systematically investigate this, we first collect a synchronized multimodal dataset and then propose a part-decoupled temporal fusion framework. The proposed model fuses foot-sensing features into the lower-body branch to compensate for incomplete visual evidence, while a lightweight coordinator exchanges information between the upper- and lower-body temporal representations to maintain whole-body consistency. The framework is evaluated with three representative real-time visual backbones based on 2D keypoints, 3D landmarks, and SMPL-based human mesh recovery. We evaluate our framework on three representative real-time visual backbones. Quantitative experiments demonstrate that incorporating simple foot sensors consistently improves pose accuracy, motion smoothness, and gait-related measurements over vision-only baselines, with the most significant gains observed under occlusion and short visual-dropout conditions. Ultimately, our results demonstrate that unobtrusive foot sensing provides vital and complementary physical observability when camera observations are temporarily unavailable.

</details>

#### 2026-10-13 - Benchmarking 3D Reconstruction for Under-Ice Robotic Perception in Arctic Environments

**Authors:** Klára Orbán, Ashwin Nedungadi, Ana-Ştefania Kogălniceanu, Bianca-Marcela Sava, Bastian Cieply, Raul-Alexandru Simon, Kuderna-Iulian Benţa, Stefan Lüdtke
**Links:** [abs](https://arxiv.org/abs/2610.19097) - [pdf](https://arxiv.org/pdf/2610.19097)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, SfM, depth estimation, monocular depth, robotics, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Benchmarking 3D Reconstruction for Under-Ice Robotic Perception in Arctic Environments
- 作者：Klára Orbán, Ashwin Nedungadi, Ana-Ştefania Kogălniceanu, Bianca-Marcela Sava, Bastian Cieply, Raul-Alexandru Simon, Kuderna-Iulian Benţa, Stefan Lüdtke
- 出版日期：2026-10-13T19:34:55Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类；次要分类未提供）
- 链接：摘要页 https://arxiv.org/abs/2610.19097 ；PDF https://arxiv.org/pdf/2610.19097

### 一句话总结
论文提出了一个面向北极冰下机器人感知的视觉三维重建基准，结合 MOSAiC 真实数据与 Unreal Engine 水下机器人模拟器合成数据，评估 SfM 与单目深度估计，并通过与向上观测多波束声呐的跨模态配准实现定量比较。

### 研究问题
北极向季节性无冰状态转变的背景下，获取水下海冰复杂形态对 ocean-ice-atmosphere 热交换建模与冰下栖息地监测至关重要。当前冰下冰面测绘主要依赖多波束声呐等声学传感器，其可提供稳健的大尺度几何，但缺乏记录精细形态特征所需的光谱与高分辨率纹理信息。冰下环境视觉特征稀疏、感知条件退化，给捕捉详细结构与光学表面属性带来挑战。论文关注的是：在这一困难环境下，如何对基于视觉的冰下三维重建方法进行基准评测。

### 核心思路/方法
- 构建一个基于视觉的冰下三维重建基准。
- 数据来源包括两类：MOSAiC 考察的真实世界数据，以及基于 Unreal Engine 的水下机器人模拟器生成的合成数据。
- 评测对象为 Structure-From-Motion（SfM）与单目深度估计。
- 通过跨模态配准到向上观测多波束声呐，实现定量比较。

### 主要贡献
- 提出面向北极冰下机器人感知的视觉三维重建基准。
- 汇集真实（MOSAiC）与合成（Unreal Engine 水下机器人模拟器）两类数据。
- 对 SfM 和单目深度估计进行评估。
- 借助与向上观测多波束声呐的跨模态配准，建立定量比较手段。

### 局限性
- 摘要未提供足够信息说明具体数据集规模、场景数量、评估指标细节及定量结果。
- 摘要未提供足够信息说明 SfM 与单目深度估计各方法的具体配置、对比基线或消融实验。
- 摘要未提供足够信息说明跨模态配准的具体实现方式、精度与误差来源。
- 摘要未提供足够信息说明合成数据与真实数据之间的域差异处理及泛化性验证。
- 摘要未提供足够信息说明该基准在机器人实际部署中的实时性或计算约束。

### 阅读优先级
中。理由：该工作聚焦北极冰下机器人感知与视觉三维重建基准，问题背景明确，且结合真实 MOSAiC 数据、合成模拟数据与声呐跨模态配准，对冰下视觉感知与多模态评测方向有参考价值；但摘要未给出具体实验结果、指标与数据规模，若需判断其方法有效性或直接复现，还需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

As the Arctic transitions toward a seasonally ice-free state, capturing the complex morphology of submerged sea ice is crucial for advancing models of ocean-ice-atmosphere heat exchange and monitoring under-ice habitats. Currently, sub-surface ice mapping is predominantly achieved through acoustic sensors such as multibeam sonar. While sonar provides robust large-scale geometry, it lacks spectral and high-resolution textural information required to record fine morphological features - a critical limitation in under-ice environments, where sparse visual features and degraded sensing conditions challenge the capture of detailed structural and optical surface properties. We present a benchmark for vision-based under-ice 3D reconstruction using real-world data from the MOSAiC expedition and synthetic data generated in an Unreal Engine-based underwater robotics simulator. The benchmark evaluates Structure-From-Motion (SfM) and monocular depth estimation, with quantitative comparison enabled through cross-modal registration to upward-looking multibeam sonar.

</details>

#### 2026-10-13 - WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World

**Authors:** Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
**Links:** [abs](https://arxiv.org/abs/2610.18846) - [pdf](https://arxiv.org/pdf/2610.18846)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, mesh reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World
- 作者：Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
- 出版日期：2026-10-13T17:57:58Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；次要分类：摘要未提供足够信息
- 链接：摘要链接 https://arxiv.org/abs/2610.18846 ；PDF 链接 https://arxiv.org/pdf/2610.18846 ；项目页 https://kszpxxzmc.github.io/WorldRecon-website/

### 一句话总结
WorldRecon 是一个面向大规模场景的生成式多视角网格重建框架，利用由输入图像估计出的粗糙全局点云与相机位姿作为全局支架，并通过分块生成与邻域感知的因果式世界生成流程，从无位姿 RGB 图像中恢复完整、连贯的大规模三维场景网格。

### 研究问题
论文关注的任务是：从**无位姿（unposed）多视角 RGB 图像**中重建大规模场景的**完整、高质量网格**。该任务的核心难点在于，既要保持可靠的几何 grounding，又需要合理地补全未被观测或仅被稀疏捕获的表面。摘要指出，这需要在几何忠实性与生成补全能力之间取得平衡，并将多视角生成式重建扩展到大规模场景。

### 核心思路/方法
- 整体框架：WorldRecon 是一个生成式多视角重建框架，用于从无位姿 RGB 图像恢复完整的大规模三维场景网格。
- 全局支架：使用由重建模型从输入图像估计出的**粗糙、带噪声的全局点云和相机位姿**作为整个场景生成的全局支架，并将其划分为**重叠的空间块（overlapping spatial blocks）**。
- 条件生成架构：为稳健利用这些不完美的几何先验，作者为原生三维生成模型 **TRELLIS.2** 配备了专门基于重建的条件架构，使每个块能够基于其**局部点云裁剪（local point-cloud crop）** 和**与该块相关的图像观测**进行生成，产出稀疏结构、详细几何以及 PBR 材质。
- 场景级一致性：为保持场景级连贯性，提出**邻域感知的 latent inpainting** 以及**因果式世界生成流程（causal world-generation procedure）**，在重叠块之间传播结构、几何与材质上下文。
- 效果定位：上述设计共同将多视角生成式重建扩展到大规模场景，得到连贯、统一的网格。

### 主要贡献
- 提出 WorldRecon，一个从无位姿 RGB 图像恢复完整、大规模三维场景网格的生成式多视角重建框架。
- 设计以粗糙噪声全局点云与相机位姿作为全局支架、并划分重叠空间块的大规模生成策略。
- 为 TRELLIS.2 引入专门基于重建的条件架构，使每个块可利用局部点云裁剪与块相关图像观测生成稀疏结构、细节几何和 PBR 材质。
- 引入邻域感知 latent inpainting 与因果式世界生成流程，跨重叠块传播结构、几何与材质上下文，以维持场景级一致性。
- 摘要报告实验显示其达到 state-of-the-art 重建性能：在合成与真实室内场景上，相较最强基线，Chamfer distance 分别降低 14.9% 与 43.1%，F-score 分别提升 17.3% 与 12.0%，并展现出较强的 sim-to-real 泛化能力。

### 局限性
- 摘要未提供足够信息说明方法在极端稀疏视角、严重遮挡或动态场景下的具体失效情形。
- 摘要未提供足够信息说明对初始粗糙点云与相机位姿估计误差的敏感程度及失败边界。
- 摘要未提供足够信息说明计算开销、运行时间、显存需求或可扩展场景规模上限。
- 摘要未提供足够信息说明真实世界实验的完整设置、评价协议与消融细节。
- 摘要未提供足够信息说明 PBR 材质生成的质量评估方式及其局限性。

### 阅读优先级
高。理由：该论文面向无位姿多视角大规模场景网格重建这一重要且困难的问题，提出结合全局支架、分块生成、邻域感知 latent inpainting 与因果式世界生成的完整框架，并在摘要中报告了相对最强基线的定量提升与 sim-to-real 泛化结果，对三维重建、多视角几何与生成式三维建模方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing complete, high-quality meshes of large-scale scenes from unposed multi-view images requires faithful geometric grounding while plausibly completing surfaces that are unobserved or only sparsely captured. We present WorldRecon, a generative multi-view reconstruction framework for recovering complete, large-scale 3D scene meshes from unposed RGB images. WorldRecon uses a coarse, noisy global point cloud and camera poses estimated from the input images by a reconstruction model as a global scaffold for whole-scene generation and partitions it into overlapping spatial blocks. To robustly leverage these imperfect geometric priors, we equip the native 3D generative model TRELLIS.2 with a dedicated reconstruction-based conditioning architecture that generates each block from its local point-cloud crop and block-relevant image observations, producing sparse structure, detailed geometry, and PBR materials. To maintain scene-level coherence, we introduce neighbour-aware latent inpainting and a causal world-generation procedure that propagates structural, geometric, and material context across overlapping blocks. Together, these designs scale multi-view generative reconstruction to large-scale scenes, yielding coherent, unified meshes. Extensive experiments demonstrate that WorldRecon achieves state-of-the-art reconstruction performance, reducing Chamfer distance by 14.9% and 43.1% while improving F-score by 17.3% and 12.0% over the strongest baselines on synthetic and real-world indoor scenes, respectively, thereby demonstrating faithful and complete generative reconstruction as well as strong sim-to-real generalization. Project page: https://kszpxxzmc.github.io/WorldRecon-website/.

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-19 - Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision

**Authors:** Wencan Feng, Bailing Tian, Yulin Hui, Zhiyu Li, Junjie Lu
**Links:** [abs](https://arxiv.org/abs/2610.26508) - [pdf](https://arxiv.org/pdf/2610.26508)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision
- 作者：Wencan Feng, Bailing Tian, Yulin Hui, Zhiyu Li, Junjie Lu
- 出版日期：2026-10-19T14:44:16Z
- 分类：主分类 Neural Scene Representations & Rendering；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.26508) / [PDF](https://arxiv.org/pdf/2610.26508)

### 一句话总结
该论文提出一种面向单目 MAV 飞行的几何感知规划框架，通过将深度专家学习到的规划相关特征跨模态蒸馏到 RGB 规划器中，在不显式重建深度的前提下实现避障规划，并声称在仿真中训练后可零微调迁移到真实环境。

### 研究问题
现有 MAV 高速导航系统多依赖深度相机、立体视觉或 LiDAR 获取显式几何信息，而单目相机更轻量、低成本。但单目飞行仍面临挑战：RGB 图像不提供直接度量线索，且视觉外观在不同环境中变化显著。论文旨在解决如何让单目 RGB 规划器获得与规划相关的几何信息，从而支持避障飞行的问题。

### 核心思路/方法
论文提出一个几何感知的单目视觉规划框架，输入为两帧图像、它们的相对位姿以及 MAV 状态，输出轨迹。方法不显式重建深度，而是通过跨模态蒸馏，将特权深度专家学习到的、与规划相关的表示迁移到 RGB 规划器，以特征级几何监督补充下游规划目标。框架训练流程为：首先训练基于深度的几何专家；然后利用成对 RGB-D 观测，将其规划特征蒸馏到单目分支；最后使规划器适配下游轨迹规划目标。该设计促使策略学习与规划相关的几何特征，从而支持避障。数据收集、成对 RGB-D 监督和仿真评估使用 3D Gaussian Splatting（3DGS）模拟器渲染视觉观测。仿真中训练的规划器随后部署到真实环境，无需真实世界微调，并声称实现最高 6.5 m/s 速度下的避障。

### 主要贡献
- 提出一种几何感知单目视觉规划框架，从两帧图像、相对位姿和 MAV 状态预测轨迹，不显式重建深度。
- 引入跨模态蒸馏：先训练深度几何专家，再将其规划相关特征通过成对 RGB-D 观测蒸馏到单目分支，最后适配下游轨迹规划目标。
- 使用 3DGS 模拟器进行视觉观测渲染、数据收集、成对 RGB-D 监督和仿真评估。
- 声称仿真训练的规划器可零真实世界微调部署，并在最高 6.5 m/s 速度下实现避障。

### 局限性
摘要未提供足够信息说明方法在真实环境中的泛化边界、失败案例、计算开销、对不同场景或光照条件的敏感性，以及定量评估指标和对比基线细节。摘要未提供足够信息说明 3DGS 模拟器与真实环境之间域差异的具体影响。摘要未提供足够信息说明蒸馏过程中特征对齐的假设与限制。

### 阅读优先级
中。理由：该论文关注单目 MAV 高速避障与跨模态蒸馏规划表示，问题明确且方法路线清晰，并声称零微调真实部署；但摘要未给出定量结果、对比基线和详细实验设置，是否值得深入阅读需结合全文实验部分判断。

</details>

<details>
<summary>Abstract</summary>

Existing high-speed navigation systems for micro aerial vehicles (MAVs) commonly rely on depth cameras, stereo vision, or LiDAR to obtain explicit geometric information, while monocular cameras offer a lighter and lower-cost alternative. However, monocular flight remains challenging because RGB images offer no direct metric cues and visual appearance varies considerably across environments. We propose a geometry-aware monocular visual planning framework that predicts trajectories from two image frames, their relative pose, and the MAV state. Without explicitly reconstructing depth, the proposed method complements the downstream planning objective with feature-level geometric supervision by transferring the planning-relevant representation learned by a privileged depth expert to the RGB planner through cross-modal distillation. The framework first trains a depth-based geometric expert, then distills its planning features into a monocular branch using paired RGB-D observations, and finally adapts the planner to the downstream trajectory planning objective. This design encourages the policy to learn planning-relevant geometric features, enabling collision avoidance. We further use a 3D Gaussian Splatting (3DGS) simulator to render visual observations for data collection, paired RGB-D supervision, and simulation evaluation. The planner trained in simulation is then deployed in real-world environments without real-world fine-tuning, achieving obstacle avoidance at speeds of up to 6.5 m/s.

</details>

#### 2026-10-19 - Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention

**Authors:** Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang
**Links:** [abs](https://arxiv.org/abs/2610.25887) - [pdf](https://arxiv.org/pdf/2610.25887)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, novel view synthesis, view synthesis, splatting, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention
- 作者：Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang
- 出版日期：2026-10-19T06:44:19Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页面 https://arxiv.org/abs/2610.25887 ；PDF https://arxiv.org/pdf/2610.25887

### 一句话总结
论文将稀疏视角 3D Gaussian Splatting 重新建模为少样本学习问题，把每个高斯基元视为神经元，并借助深度学习正则化思路，从数据监督增强与训练时正则化两方面抑制过拟合。

### 研究问题
稀疏视角新视角合成在 AR/VR 与实时通信中很重要，但从有限视角重建 3D 场景仍然困难。3DGS 在稠密视角下表现好，在稀疏输入下却容易出现 overfitting 与 geometry degradation。现有方法多从局部入手，分别处理数据质量或训练正则化，缺少统一且可解释的系统改进框架。

### 核心思路/方法
论文提出新的视角：从 few-shot learning 出发重新审视稀疏视角 3DGS，把每个 Gaussian primitive 当作 neuron，并利用深度学习正则化技术。在该统一框架下，通过两种策略从稀少观测中生成更有效的监督：
1. 数据相关监督增强：optical flow-guided pseudo-view synthesis 与 joint camera-scene optimization；
2. 训练时正则化：motion-aware dropout 与 early stopping，用于抑制过拟合并保持动态场景稳定性。

### 主要贡献
- 提出将稀疏视角 3DGS 视为少样本学习问题的新视角，并把高斯基元类比为神经元，借助深度学习正则化形成统一框架。
- 设计数据相关监督增强策略：optical flow-guided pseudo-view synthesis 与 joint camera-scene optimization。
- 设计训练时正则化策略：motion-aware dropout 与 early stopping，以抑制过拟合并保持动态场景稳定性。
- 在 SIGGRAPH Asia 2025 volumetric video challenge sparse-view dataset 上取得显著改进，作者称系统在该挑战赛 sparse-view track 中获得第一名。

### 局限性
摘要未提供足够信息。摘要未给出具体失败场景、计算开销、对光流质量或相机优化的敏感性、消融实验细节、与各基线的定量差距，也未说明方法在非挑战数据或更极端稀疏条件下的泛化表现。

### 阅读优先级
高。理由：该工作针对稀疏视角 3DGS 的过拟合问题提出统一且可解释的少样本学习框架，并声称在 SIGGRAPH Asia 2025 相关挑战赛稀疏视角赛道获得第一，问题重要且结果信号较强；但摘要未提供实验细节，阅读全文时需重点核查方法假设、消融与泛化证据。

</details>

<details>
<summary>Abstract</summary>

Sparse-view novel view synthesis (NVS) is essential for AR/VR and real-time communication applications, yet remains challenging when reconstructing 3D scenes from limited viewpoints. While 3D Gaussian Splatting (3DGS) excels in dense-view scenarios, it suffers from overfitting and geometry degradation under sparse inputs. Current approaches often tackle these problems from a local perspective, addressing either data quality or training regularization individually, lacking a unified and interpretable framework for systematic improvement. We introduce a new perspective that reframes sparse-view 3DGS from a few-shot learning viewpoint, treating each Gaussian primitive as a neuron and leveraging deep learning regularization techniques. Under this unified framework, our approach generates more effective supervision from scarce observations through two strategies: (1) data-related supervision enrichment via optical flow-guided pseudo-view synthesis and joint camera-scene optimization; and (2) training-time regularization via motion-aware dropout and early stopping, which suppress overfitting while preserving dynamic-scene stability. Extensive experiments on the SIGGRAPH Asia 2025 volumetric video challenge sparse-view dataset demonstrate significant improvements over state-of-the-art optimization-based and feed-forward baselines. Our system won first place in the sparse-view track of the SIGGRAPH Asia 2025 challenge.

</details>

#### 2026-10-19 - RxGS: Relightable Gaussian Stylization via BRDF Decomposition

**Authors:** Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li
**Links:** [abs](https://arxiv.org/abs/2610.25681) - [pdf](https://arxiv.org/pdf/2610.25681)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feature matching, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, inverse rendering, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RxGS: Relightable Gaussian Stylization via BRDF Decomposition
- 作者：Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li
- 出版日期：2026-10-19T02:31:17Z
- 分类：主分类为 Neural Scene Representations & Rendering；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.25681 ；PDF https://arxiv.org/pdf/2610.25681

### 一句话总结
RxGS 提出一种基于 BRDF 感知 3D 高斯表示的可重光照 3D 场景风格化框架，通过仅优化逆渲染得到的漫反射反照率场，使风格化后的场景仍可在不同光照条件下重新渲染。

### 研究问题
论文关注基于参考图像的 3D 场景风格化问题：将参考图像的外观迁移到重建的 3D 场景上，同时保持场景几何。现有方法通常优化 NeRF 或 3DGS 等神经场景模型的 RGB 外观表示，而单点颜色混合了材质反射率、环境光照、着色效果以及观察方向等因素。当风格化修改这种混合颜色时，风格化过程中的光照效果会被“烘焙”进存储的外观中，导致风格化场景无法在不同光照下重新渲染。论文旨在解决这一限制。

### 核心思路/方法
RxGS 构建在 BRDF 感知的 3D 高斯表示之上，而不是修改逐点 RGB 颜色。方法仅优化通过逆渲染恢复的漫反射反照率场，同时保持粗糙度、金属度、表面法线以及估计的环境光照不变。这样，风格化场景除被编辑的反照率外，仍保留基于物理渲染器所需的其他组件，因此仍可重光照。在优化反照率场时，RxGS 使用最近邻特征匹配损失，并对高斯中心施加空间平滑先验。评估方面，论文采用基于光流扭曲误差的 Geometry Consistency Cost（GCC）。

### 主要贡献
- 提出 RxGS，一个可重光照的 3D 场景风格化框架，基于 BRDF 感知的 3D 高斯表示。
- 与修改逐点 RGB 颜色的做法不同，仅优化逆渲染得到的漫反射反照率场，保留粗糙度、金属度、表面法线和估计环境光照不变，从而支持风格化后的重光照。
- 使用最近邻特征匹配损失与高斯中心上的空间平滑先验优化反照率场。
- 采用基于光流扭曲误差的 GCC 进行评估；摘要称 RxGS 在所有评估的 NeRF-Synthetic 场景上取得最低 GCC，并在真实拍摄场景上保持竞争力，同时支持现有基于参考的 3D 场景风格化方法不具备的可重光照风格化能力。

### 局限性
摘要未提供足够信息。仅从摘要无法确定方法在计算开销、训练时间、对逆渲染质量的依赖、真实场景泛化能力、重光照一致性的定量评估以及失败案例等方面的具体局限。

### 阅读优先级
中。理由：论文聚焦 3D 场景风格化与可重光照表示的交叉问题，提出通过 BRDF 分解仅编辑反照率以保留重光照能力的思路，对神经场景表示与渲染方向具有相关性；但摘要未提供充分的实验细节、定量重光照评估和局限性信息，是否需要优先精读取决于读者对 3DGS、逆渲染或可重光照风格化的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Reference-based 3D scene stylization transfers the appearance of a reference image onto a reconstructed 3D scene while preserving scene geometry. Recent methods perform this transfer by optimizing the appearance representation of neural scene models including Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). These methods optimize an RGB appearance representation, in which a single per-point colour combines the effects of material reflectance, environment illumination, together with the shading it produces, and the viewing direction. When stylization modifies this combined colour, the illumination effects present during stylization are baked into the stored appearance, so the stylized scene cannot be rendered under different illumination. To address this limitation, we present RxGS, a relightable 3D scene stylization framework built on a Bidirectional Reflectance Distribution Function (BRDF)-aware 3D Gaussian representation. Rather than modifying a per-point RGB colour, RxGS optimizes only the diffuse albedo field recovered by inverse rendering, while leaving roughness, metallicity, surface normals, and the estimated environment lighting unchanged. As a result, the stylized scene keeps all the components a physically-based renderer needs other than the edited albedo, and can therefore still be relit. RxGS optimizes the albedo field using a nearest-neighbour feature matching loss together with a spatial smoothness prior over Gaussian centres. We evaluate the method using a Geometry Consistency Cost (GCC) based on optical-flow warping error. RxGS achieves the lowest GCC on all evaluated NeRF-Synthetic scenes and remains competitive on real-captured scenes, while additionally supporting relightable stylization, which existing reference-based 3D scene stylization methods do not provide.

</details>

#### 2026-10-19 - SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering

**Authors:** Jianheng Liu, Yunfei Wan, Fangming Cheng, Xiangyu Hong, Zuhao Zou, Haotian Li, Longji Yin, Chunran Zheng, Jiarong Lin, Fu Zhang
**Links:** [abs](https://arxiv.org/abs/2610.25665) - [pdf](https://arxiv.org/pdf/2610.25665)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** rendering, radiance, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering
- 作者：Jianheng Liu, Yunfei Wan, Fangming Cheng, Xiangyu Hong, Zuhao Zou, Haotian Li, Longji Yin, Chunran Zheng, Jiarong Lin, Fu Zhang
- 出版日期：2026-10-19T02:12:26Z
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2610.25665；PDF https://arxiv.org/pdf/2610.25665

### 一句话总结
SpaRV 是一种稀疏辐射体素地图，通过可微光线步进进行渲染，并用不规则 LiDAR 扫描与图像共同监督，以在机器人采集数据条件下实现几何一致、可扩展的 LiDAR-视觉建图与渲染。

### 研究问题
论文针对从机器人数据构建辐射场时面临的三个挑战：1）机器人轨迹服务于任务而非重建，少量视角导致几何约束不足；2）相机位姿与内参的残余误差使地图模糊；3）地图的 GPU 内存随场景规模增长，限制大场景中的细节水平。目标是同时获得照片级真实感和几何准确的地图，并支持大规模场景。

### 核心思路/方法
- 使用稀疏辐射体素地图，并以可微光线步进进行渲染。
- 让不规则 LiDAR 扫描与图像共同监督该地图；LiDAR 深度和占据信息用于锚定约束不足的几何，法向与平滑正则项用于保持 LiDAR 点之间的平滑性。
- 为校正相机误差，SpaRV 交替进行地图训练与对相机位姿和焦距的光度优化。
- 为限制训练和渲染中的 GPU 内存，SpaRV 同时仅以一个子图保持全分辨率，其余子图保持在较粗的八叉树层级。

### 主要贡献
- 提出 SpaRV：稀疏辐射体素地图，结合可微光线步进渲染，并利用不规则 LiDAR 扫描与图像共同监督。
- 利用 LiDAR 深度与占据锚定几何，并用正则项保持 LiDAR 点间平滑。
- 通过交替地图训练与相机位姿、焦距的光度优化来校正相机误差。
- 通过“一个子图全分辨率、其余子图粗八叉树层级”的策略约束 GPU 内存。
- 摘要报告：SpaRV 在远离采集轨迹处保持几何一致，并通过优化相机参数锐化纹理；在单张 24 GB GPU 上重建了由 63,582 张图像捕获的大学校园，并模拟其他相机和 LiDAR。

### 局限性
摘要未提供足够信息。摘要未给出定量精度、运行时间、内存占用对比、失败案例或与其他方法的系统比较等细节。

### 阅读优先级
中。理由：该工作面向机器人建图与渲染中的几何一致性、相机参数优化和大场景内存可扩展性问题，与 Neural Scene Representations & Rendering 及机器人应用相关；摘要给出了明确的问题、方法要点和大规模重建结果，但未提供定量实验细节。是否优先精读取决于读者对 LiDAR-视觉联合辐射场、可扩展建图或机器人仿真/导航/巡检应用的兴趣；仅就摘要信息而言，定为中。

</details>

<details>
<summary>Abstract</summary>

Robotic simulation, navigation, and inspection need photorealistic and geometrically accurate maps. Radiance fields achieve photorealism, but building them from robot data raises three challenges. A robot's trajectory serves its task, not reconstruction, so images from few viewpoints leave the geometry under-constrained. Residual errors in camera poses and intrinsics blur the map. The map's GPU memory grows with scene size, which limits its level of detail in large scenes. We present \textbf{SpaRV}, a \textbf{Spa}rse \textbf{R}adiance \textbf{V}oxel map rendered by differentiable ray marching, which lets irregular LiDAR scans supervise it alongside images. LiDAR depth and occupancy anchor the under-constrained geometry, and normal and smoothness regularizers keep it smooth between LiDAR points. To correct camera errors, SpaRV alternates map training with photometric optimization of the camera poses and focal lengths. To bound GPU memory in training and rendering, SpaRV holds one submap at a time at full resolution and the rest at coarser octree levels. Experiments show that SpaRV keeps the geometry consistent away from the captured trajectory and sharpens textures by optimizing the camera parameters. On one 24\,GB GPU, SpaRV reconstructs a university campus captured in 63{,}582 images and simulates other cameras and LiDARs. Our code will be released at \url{https://github.com/hku-mars/SpaRV}.

</details>

#### 2026-10-18 - MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes

**Authors:** Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao
**Links:** [abs](https://arxiv.org/abs/2610.25345) - [pdf](https://arxiv.org/pdf/2610.25345)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, splatting, driving scene

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes
- 作者：Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao
- 出版日期：2026-10-18T15:40:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.25345) / [PDF](https://arxiv.org/pdf/2610.25345)

### 一句话总结
MCSplat 是一个面向驾驶场景的前馈高斯泼溅框架，通过构建规范外观空间解耦几何与相机外观，并用基于 Fisher 信息的不确定性自适应加权几何自监督，以提升多视角光度一致性与几何可靠性。

### 研究问题
论文针对稀疏多视角图像前馈高斯泼溅重建驾驶场景中的两个挑战：
1. **跨相机光度不一致**：曝光、ISP 和光照变化导致的多相机光度差异，可能被错误地吸收进高斯几何中。
2. **局部几何监督不可靠**：在深度不连续区域附近，基于法向的约束提供的局部几何监督不可靠。

### 核心思路/方法
- 从深度引导的多相机对应关系构建**规范外观空间**，将几何学习与相机特定外观解耦。
- 提出**多尺度双边网格 Transformer**，从规范渲染结果恢复原始相机外观，从而在光度监督时不污染高斯几何。
- 从光度敏感性估计**基于 Fisher 信息的不确定性**，并用其自适应加权面向表面的自监督，以提升局部几何可靠性。

### 主要贡献
- 提出 MCSplat：一个多视角一致的前馈高斯泼溅框架，面向驾驶场景。
- 构建规范外观空间以解耦几何学习与相机特定外观，缓解跨相机光度不一致对几何的污染。
- 设计多尺度双边网格 Transformer 恢复原始相机外观，支持不污染几何的光度监督。
- 引入基于 Fisher 信息的不确定性，自适应加权表面朝向自监督，改善局部几何可靠性。
- 摘要称实验显示重建质量和跨驾驶数据集泛化性提升，几何评估显示跨视角深度一致性和局部表面法向一致性增强，定性结果显示几何伪影更少、重叠视角结构更连贯。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集名称、实验设置、计算开销、实时性、失败案例或定量指标细节。

### 阅读优先级
**中**。理由：该论文聚焦驾驶场景稀疏多视角前馈高斯泼溅中的光度一致性与几何监督可靠性，问题定义清晰且方法组合有针对性；但摘要未提供具体实验细节与量化结果，是否适合优先精读取决于读者对驾驶场景重建、前馈高斯泼溅或多相机光度一致性方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors. First, cross-camera photometric inconsistency, caused by variations in exposure, ISP, and illumination, can be incorrectly absorbed into Gaussian geometry. Second, unreliable local geometric supervision arises from normal-based constraints near depth discontinuities. To address these issues, we present \textbf{MCSplat}, a multi-view consistent feed-forward Gaussian splatting framework for driving scenes. MCSplat constructs a canonical appearance space from depth-guided multi-camera correspondences to decouple geometry learning from camera-specific appearance. A multi-scale Bilateral Grid Transformer restores raw camera appearance from canonical renderings, enabling photometric supervision without contaminating Gaussian geometry. To improve local geometric reliability, we estimate Fisher-information-based uncertainty from photometric sensitivity and use it to adaptively weight surface-oriented self-supervision. Extensive experiments demonstrate improved reconstruction quality and generalization across driving datasets. Geometry-oriented evaluations further reveal enhanced cross-view depth consistency and local surface-normal agreement, while qualitative results show fewer geometric artifacts and more coherent structures across overlapping views.

</details>

#### 2026-10-18 - GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation

**Authors:** Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger
**Links:** [abs](https://arxiv.org/abs/2610.25261) - [pdf](https://arxiv.org/pdf/2610.25261)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, splatting, robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation
- 作者：Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger
- 出版日期：2026-10-18T13:31:50Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25261 ；PDF https://arxiv.org/pdf/2610.25261 ；代码 https://github.com/Bennnoo/GOFusion ；补充视频 https://youtu.be/pLQKbxQvb6I

### 一句话总结
GOFusion 是一种面向自主机器人导航的实时视觉建图系统，将 3D 高斯原语锚定到局部占据地图上，并利用栅格化集成的 Fisher 近似实现在线敏感度量化，以支持高斯剪枝和下一最佳视角规划。

### 研究问题
论文关注自主机器人导航中的实时视觉建图问题：如何同时提供用于路径规划的空间感知能力与高保真外观信息，并在位姿校正、GPU 内存受限和大规模场景下保持几何与视觉一致性。摘要还指出需要一种在线不确定性/敏感度度量，作为信息驱动的高斯剪枝与下一最佳视角规划启发式。

### 核心思路/方法
- 从视觉-惯性 SLAM 获得的位姿估计与局部占据地图构建 3D 高斯地图，并将高斯原语锚定到局部占据地图。
- 支持位姿校正，以维持几何与视觉一致性。
- 将 3D Gaussian Splatting 优化限制在活跃子图（active submaps）内，以约束 GPU 内存使用。
- 提出栅格化集成的 Fisher 近似，在线量化每个高斯原语的敏感度，并将其作为信息驱动启发式用于高斯剪枝和下一最佳视角规划。
- 在公共数据集和真实无人机飞行中进行评估，并展示利用 Fisher 启发式的全自主无人机探索以细化高斯地图。

### 主要贡献
- 提出 GOFusion 实时视觉建图系统，将高斯原语锚定到局部占据地图，兼顾路径规划所需的空间感知与高保真外观。
- 设计基于活跃子图的 3D Gaussian Splatting 优化，以限制 GPU 内存占用。
- 引入栅格化集成的 Fisher 近似，在线量化逐原语敏感度，并用于高斯剪枝与下一最佳视角规划。
- 摘要称其在建图质量上优于若干基线，并实现实时、高保真、不确定性感知的大规模建图。
- 展示使用 Fisher 信息启发式的全自主无人机探索与高斯地图细化。

### 局限性
摘要未提供足够信息。摘要未给出具体失败场景、计算开销细节、对 SLAM 位姿质量的依赖程度、不同数据集上的定量局限，也未说明 Fisher 近似在何种条件下可能失效。

### 阅读优先级
高。理由：该论文直接面向自主机器人导航中的实时建图、内存约束、不确定性感知与主动探索规划，且提供代码与补充视频；摘要明确声称在公共数据集和真实无人机飞行中验证，并展示全自主无人机探索，适合关注神经场景表示与机器人/具身应用交叉方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

In this letter, we present GOFusion, a real-time visual mapping system for autonomous robot navigation that anchors Gaussian primitives to local occupancy maps, providing both spatial awareness for path planning and high-fidelity appearance that enables information-driven robot navigation. GOFusion builds 3D Gaussian maps from pose estimates and local occupancy maps obtained via visual-inertial SLAM and enables pose corrections to maintain both geometric and visual consistency. Furthermore, it restricts the 3D Gaussian Splatting optimization to active submaps to bound GPU memory usage. Building on the appearance-rich Gaussian map, we introduce a rasterizer-integrated Fisher approximation that quantifies per-primitive sensitivity online, serving as an information-driven heuristic for Gaussian pruning and next-best-view planning. We evaluate GOFusion on public datasets and in real-world drone flights. It not only outperforms several baselines in mapping quality, but also achieves real-time, high-fidelity and uncertainty-aware mapping at scale. Finally, we demonstrate fully autonomous drone exploration for Gaussian map refinement using the proposed Fisher-informed heuristic. Code is available at https://github.com/Bennnoo/GOFusion. We provide a supplementary video demonstration at https://youtu.be/pLQKbxQvb6I.

</details>

#### 2026-10-18 - GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation

**Authors:** Yuchen Xi, Yuhan Guo, Chenwei Hou, Zixu Liu, Jin Fang, Jason Liu, Ruigang Yang
**Links:** [abs](https://arxiv.org/abs/2610.25245) - [pdf](https://arxiv.org/pdf/2610.25245)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, autonomous driving, driving scene, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation
- 作者：Yuchen Xi, Yuhan Guo, Chenwei Hou, Zixu Liu, Jin Fang, Jason Liu, Ruigang Yang
- 出版日期：2026-10-18T13:05:08Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25245 ；PDF https://arxiv.org/pdf/2610.25245 ；项目页 https://xiyuche.github.io/GeoV2V/

### 一句话总结
GeoV2V 是一个以几何为约束的视频到视频扩散框架，旨在沿新轨迹合成时序一致的驾驶场景视频，并配套提出 Para4D 合成数据集以提供跨车道变换的同步多轨迹监督。

### 研究问题
论文关注轨迹变化下的新视角合成，尤其是外推到车道偏移等未见视角时，现有方法难以生成一致视频的问题。摘要指出两类现有方法存在不足：基于重建的方法几何一致但在大视角变化下视觉质量下降；先重建后修复的方法帧视觉上看似合理，但存在几何与时序不一致。核心挑战在于真实数据集缺乏同步多轨迹监督，使跨车道变换学习困难。

### 核心思路/方法
GeoV2V 被描述为一个几何锚定的视频到视频扩散框架：它将 LiDAR 与深度导出的几何先验，与 Wan 2.1 骨干中的全视频条件相结合，用于沿新轨迹合成时序一致的驾驶视频。为缓解跨车道变换监督不足，论文引入 Para4D 合成数据集，捕获动态场景中同步的多车道驾驶视频，为车道偏移生成提供显式监督，并作为几何一致视角合成的训练先验。

### 主要贡献
- 提出 GeoV2V：几何锚定的视频到视频扩散框架，在 Wan 2.1 骨干中融合 LiDAR 和深度几何先验与全视频条件，面向新轨迹驾驶视频生成。
- 识别并针对真实数据缺乏同步多轨迹监督的问题，提出 Para4D 合成数据集，提供车道偏移生成的显式监督。
- 摘要称在 Waymo、nuScenes 和 Para4D 上的实验显示出在视觉质量、几何一致性以及大轨迹偏移下复杂光照动态鲁棒性方面的最先进性能。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、计算成本、对 LiDAR/深度先验质量的依赖程度、Para4D 与真实数据分布差异的量化影响，也未提供各数据集上的详细指标与消融结果。

### 阅读优先级
中。理由：该论文聚焦自动驾驶仿真中的新轨迹视角合成，问题定义清晰，且同时提出方法与大轨迹偏移监督数据集；摘要声称在 Waymo、nuScenes 与 Para4D 上取得最先进表现。但仅凭摘要无法判断实验细节、复现难度与实际部署成本，因此优先级定为中，适合关注驾驶场景生成、几何一致视频扩散与仿真数据构建的读者进一步阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis under trajectory changes is essential for autonomous driving simulation, yet existing methods struggle to generate consistent videos when extrapolating to unseen viewpoints such as lane shifts. Reconstruction-based approaches maintain geometric consistency but degrade in visual quality under large viewpoint changes, while reconstruct-then-restore methods often produce visually plausible frames yet suffer from geometric and temporal inconsistencies. We present GeoV2V, a geometry-grounded video-to-video diffusion framework that synthesizes temporally coherent driving videos along novel trajectories by integrating LiDAR and depth-derived geometric priors with full-video conditioning in the Wan 2.1 backbone. A key challenge in learning cross-lane transformations is the lack of synchronized multi-trajectory supervision in real-world datasets. To address this, we also introduce Para4D, a synthetic dataset capturing synchronized multi-lane driving videos within dynamic scenes, which provides explicit supervision for lane-shift generation and serves as a strong training prior for geometry-consistent view synthesis. Experiments on Waymo, nuScenes, and Para4D demonstrate state-of-the-art performance in visual quality, geometric consistency, and robustness to complex lighting dynamics under large trajectory shifts. Project page: https://xiyuche.github.io/GeoV2V/

</details>

#### 2026-10-18 - Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots

**Authors:** Que Haohua, Mingkai Liu, Handong Yao
**Links:** [abs](https://arxiv.org/abs/2610.25068) - [pdf](https://arxiv.org/pdf/2610.25068)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** SfM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots
- 作者：Que Haohua, Mingkai Liu, Handong Yao
- 出版日期：2026-10-18T07:18:24Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.25068) / [PDF](https://arxiv.org/pdf/2610.25068)

### 一句话总结
LENS 在 AMD KR260 低功耗 FPGA/ARM 平台上协同设计 SCR 定位加速器与定点 3DGS 渲染器，将 ACEsplat 风格场景记忆工作负载带到边缘设备。

### 研究问题
资源受限的机器人与自动驾驶车辆需要能在无桌面 GPU 条件下定位相机并渲染附近视图的场景记忆。SCR 与 3DGS 因无需 SfM 阶段而适用，但 ACEsplat 风格流水线以 GPU 为中心，迁移到边缘 FPGA 存在困难：SCR 对位姿敏感，3DGS 渲染不规则且对容量敏感。

### 核心思路/方法
论文提出 LENS，一个运行于 AMD KR260 的边缘场景记忆加速系统，将 ACEsplat 风格工作负载带到低功耗 FPGA/ARM 平台。作者不提出新的场景模型，而是将两个主导内核与板级数据通路协同设计：一是保持位姿精度的 INT16 SCR 加速器；二是位精确定点有序 3DGS 渲染器，将 alpha 透射率改写为 log-sum-exp 递推，并剔除可证明无用的流式高斯。摘要称所有 LENS 延迟、功耗与质量结果均为板级实测。

### 主要贡献
- 提出 LENS 边缘场景记忆加速系统，在 AMD KR260 上实现 ACEsplat 风格工作负载。
- 设计 INT16 SCR 加速器，保持 DSAC* 定位精度，延迟为 25.42 ms。
- 设计位精确定点有序 3DGS 渲染器，采用 log-sum-exp 递推表达 alpha 透射率，并移除可证明无用的流式高斯。
- 板载渲染器在 Cambridge 上达到 34.11 dB，高于 ACEsplat 的 33.20；RealEstate10K 新视图合成达到 27.84 dB，高于 26.11；全部十个 Wayspots 场景达到 ACEsplat 渲染目标。
- 与 Jetson Orin NX 相比，LENS 在每个部署任务上性能功耗比更优，提升 1.9x 至 5.7x，功耗约为其四分之一，并在定位与 Wayspots 渲染上绝对延迟更快。
- 设备端训练达到 ACEsplat 级质量，但未达到 GPU 的时间或能耗水平，作者将其标记为未来训练加速器的剩余边界。

### 局限性
- 设备端训练在时间或能耗上未达到 GPU 水平，摘要未提供具体差距数值。
- 摘要未提供功耗绝对值、FPGA 资源占用、散热或部署环境细节。
- 摘要未提供失败案例、泛化范围或更多数据集的定量结果。
- 摘要未提供与除 Jetson Orin NX 外其他边缘平台的比较。
- 摘要未提供训练加速器设计或时间表。

### 阅读优先级
中。理由：该论文聚焦边缘 FPGA 上的场景记忆加速，涉及 SCR 定位与 3DGS 渲染的协同设计，对机器人、AR 与边缘视觉系统读者有参考价值；摘要给出了板级实测的延迟、质量与性能功耗比结果，但未提供功耗绝对值、资源占用与训练差距细节，是否高优先级取决于读者对 FPGA 部署与 3DGS 边缘加速的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Resource-constrained robots and autonomous vehicles need scene memories that localize a camera and render nearby views without a desktop GPU. Scene-coordinate regression (SCR) and 3D Gaussian splatting (3DGS) fit because they avoid an SfM stage, but ACEsplat-style pipelines are GPU-centered, and moving them to an edge FPGA is hard because SCR is pose-sensitive and 3DGS rendering is irregular and capacity-sensitive. We present LENS, an edge scene-memory acceleration system on the AMD KR260 that brings an ACEsplat-style workload to a low-power FPGA/ARM platform. Rather than proposing a new scene model, LENS co-designs the two dominant kernels with the board data path: an INT16 SCR accelerator that preserves pose accuracy, and a bit-exact fixed-point ordered 3DGS renderer that rewrites alpha transmittance as a log-sum-exp recurrence and removes provably useless streamed Gaussians. All LENS latency, power, and quality results are board-measured. The SCR engine preserves DSAC* localization accuracy at 25.42 ms, the on-board renderer reaches 34.11 dB on Cambridge against ACEsplat's 33.20, novel-view synthesis on RealEstate10K reaches 27.84 dB against 26.11, and all ten Wayspots scenes reach the ACEsplat rendering target. LENS wins performance per watt over a Jetson Orin NX on every deployment task, by 1.9x to 5.7x at about a quarter of the power, and is faster in absolute latency on localization and Wayspots rendering. On-device training reaches ACEsplat-level quality but not the GPU's time or energy, marking the remaining boundary for a future training accelerator.

</details>

#### 2026-10-18 - FineSplat: Fine Patches, Local Groups, Detailed Splats

**Authors:** Hyebin Kim, Hwasik Jeong, Joonhyuk Park, Gyeongjin Kang, Jungwoo Kim, Younghyun Kim, Eunbyung Park
**Links:** [abs](https://arxiv.org/abs/2610.25011) - [pdf](https://arxiv.org/pdf/2610.25011)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FineSplat: Fine Patches, Local Groups, Detailed Splats
- 作者：Hyebin Kim, Hwasik Jeong, Joonhyuk Park, Gyeongjin Kang, Jungwoo Kim, Younghyun Kim, Eunbyung Park
- 出版日期：2026-10-18T04:44:10Z
- 分类：Neural Scene Representations & Rendering（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2610.25011) / [PDF](https://arxiv.org/pdf/2610.25011)

### 一句话总结
FineSplat 是一个围绕细粒度图像块构建的前馈式 3D Gaussian Splatting 框架，通过双重分组策略、重建误差反馈和紧凑高斯生成，在保持效率与紧凑性的同时恢复更丰富的几何与外观细节。

### 研究问题
前馈式 3D Gaussian Splatting 虽然有望实现即时场景重建与高质量新视角合成，但在细粒度几何和外观的恢复上仍然困难。作者因此重新审视前馈模型如何表示、聚合与精炼细节视觉信息。具体而言，当图像块分辨率很高、token 数量很大时，全局多视图注意力代价过高，需要更高效的局部交互机制；同时，单次前馈预测在细节恢复上存在局限。

### 核心思路/方法
论文提出 FineSplat，其核心设计包括：
1. **以细粒度图像块为基础**：框架围绕 fine-grained image patches 构建，以提升细节表达能力。
2. **双重分组策略**：由于高 token 分辨率下全局多视图注意力过于昂贵，方法结合两种互补的局部性——按视图分组（view-wise grouping）使邻近视图间高效交互；3D 空间分组则将几何相关的 token 提升到 3D 场景空间中重新连接，这些 token 在视图分组下可能从未交互。
3. **重建误差作为直接反馈**：利用重建误差提供显式的、基于渲染的信号，以恢复细粒度结构和外观，从而克服单次前馈预测的限制。
4. **紧凑高斯生成方案**：在享受细粒度特征收益的同时，避免不必要地增加高斯基元数量。

### 主要贡献
- 提出 FineSplat 前馈式 3DGS 框架，围绕细粒度图像块进行细节表示与聚合。
- 设计双重分组策略，在视图局部性与 3D 空间局部性之间互补，缓解高分辨率 token 下全局注意力的开销问题。
- 引入基于重建误差的显式渲染反馈，弥补单次前馈预测在细粒度结构恢复上的不足。
- 提出紧凑高斯生成方案，在不显著增加基元数量的前提下保留细粒度特征优势。
- 摘要声称在相同或更小的高斯预算下，以较大幅度取得 state-of-the-art 结果，同时保持效率与紧凑性。

### 局限性
- 摘要未提供足够信息说明方法的具体失败场景或适用范围限制。
- 摘要未提供足够信息说明双重分组策略在不同场景规模、视图数量或分辨率下的敏感性。
- 摘要未提供足够信息说明重建误差反馈的具体计算方式、训练成本或收敛行为。
- 摘要未提供足够信息说明“state-of-the-art by a substantial margin”所对应的数据集、指标与定量结果。
- 摘要未提供足够信息说明紧凑高斯生成方案对基元数量的具体控制机制与压缩程度。

### 阅读优先级
**高**。理由：该论文聚焦前馈式 3DGS 中细粒度几何与外观恢复这一明确难题，提出的双重分组、渲染误差反馈与紧凑高斯生成均属于方法层面的实质性设计；且摘要声称在相同或更小高斯预算下显著优于现有方法。若关注前馈 3D 重建、3D Gaussian Splatting 的效率与细节平衡，该论文具有较高阅读价值。但需注意，摘要未给出实验细节，定量结论需查阅正文验证。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) promises instant scene reconstruction with high-quality novel-view synthesis. Yet, fine-grained geometry and appearance remain difficult to recover, motivating us to revisit how feed-forward models represent, aggregate, and refine detailed visual information. We introduce FineSplat, a feed-forward 3DGS framework built around fine-grained image patches. Since global multi-view attention becomes prohibitively expensive at such high token resolutions, we develop a dual-grouping strategy that combines two complementary forms of locality: view-wise grouping enables efficient interaction among neighboring views, while 3D spatial grouping reconnects geometrically related tokens that may never have interacted under view-wise grouping by lifting them into the 3D scene space. We further leverage reconstruction error as direct feedback, providing an explicit rendering-based signal to recover fine-grained structures and appearance, thereby overcoming the limitations of one-pass feed-forward prediction. Finally, a compact Gaussian generation scheme preserves the benefits of fine-grained features without unnecessarily increasing the number of primitives. Together, these designs enable FineSplat to recover richer geometry and appearance while remaining efficient and compact, achieving state-of-the-art results by a substantial margin, under the same or smaller Gaussian budgets than existing methods.

</details>

#### 2026-10-17 - SwitchSplat: Learning Discrete Object States from Casually Captured Scenes

**Authors:** Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi
**Links:** [abs](https://arxiv.org/abs/2610.24812) - [pdf](https://arxiv.org/pdf/2610.24812)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SwitchSplat: Learning Discrete Object States from Casually Captured Scenes
- 作者：Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi
- 出版日期：2026-10-17T18:35:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.24812) | [PDF](https://arxiv.org/pdf/2610.24812)

### 一句话总结
SwitchSplat 提出一种基于 3D Gaussian Splatting 的“基础 + 槽位”分解表示，用于从随性拍摄视频中学习可交互物体的离散二值状态，并支持在推理时自由组合状态进行新视角渲染。

### 研究问题
现有 3D Gaussian Splatting 表示假设世界是静态的，无法建模随性拍摄中用户与环境交互（如开门、拨动开关、移动物体）带来的离散状态变化。时间条件动态方法（如 4DGS）将“状态被观察到的时间”与“场景处于何种状态”混为一谈，只能回放已见序列，难以组合任意物体配置。

### 核心思路/方法
论文提出 base+slot 分解：一个共享的静态 base 捕捉不变场景，每个可交互物体对应一个 slot，独立持有该物体的两种二值状态（on/off）。由于高斯到 slot 的分配完全可微，模型可直接从视频中发现各状态的几何，无需人工标注。推理时用户可自由组合各 slot 状态，并从任意视角渲染结果场景。

### 主要贡献
- 提出 SwitchSplat，据摘要称为首个通过 base+slot 分解处理离散物体状态变化的 3DGS 表示。
- 实现无需人工标注的可微状态几何发现。
- 支持推理时自由组合 slot 状态，渲染捕捉时从未见过的状态组合。
- 在新随性拍摄数据集上验证，并在新视角合成质量上优于静态与动态基线。

### 局限性
摘要未提供足够信息（未说明方法对非二值状态、复杂拓扑变化、遮挡或大规模场景的适用性，也未给出计算开销、数据集规模与失败案例等细节）。

### 阅读优先级
中。理由：该工作针对 3DGS 静态假设与动态表示状态混淆的问题，提出可组合离散状态的表示，问题定义清晰且与可交互场景重建相关；但摘要未提供定量结果、数据集细节与局限分析，需阅读全文后才能判断其实际效果与适用范围。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has made high-fidelity 3D reconstruction fast and accessible, yet existing representations assume a static world. This assumption breaks down in casual captures, where a user naturally interacts with the environment -- opening doors, toggling switches, or moving objects -- introducing discrete state changes that no current framework can model. Time-conditioned dynamic methods such as 4DGS conflate when a state was observed with what state the scene is in, limiting them to replaying seen sequences rather than composing arbitrary object configurations. We present SwitchSplat, the first 3DGS representation to address this gap via a base+slot decomposition: a shared static base captures the invariant scene, while each slot independently holds the two binary states (on/off) of one interactable object. Because the assignment of Gaussians to slots is fully differentiable, the model discovers the geometry of each state directly from video, without manual annotation. At inference, the user can freely combine slot states and render the resulting scene from any viewpoint. We validate SwitchSplat on a new casual-capture dataset and show that it outperforms static and dynamic baselines in novel-view synthesis quality, while uniquely supporting rendering of state combinations never seen during capture. Project page: https://switchsplat.github.io

</details>

#### 2026-10-17 - Directionally Factorized Illumination with Spherical Harmonic Rotation

**Authors:** Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer
**Links:** [abs](https://arxiv.org/abs/2610.24811) - [pdf](https://arxiv.org/pdf/2610.24811)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, neural rendering, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Directionally Factorized Illumination with Spherical Harmonic Rotation
- 作者：Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer
- 出版日期：2026-10-17T18:35:02Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.24811) / [PDF](https://arxiv.org/pdf/2610.24811)

### 一句话总结
论文提出可插入任意新视角合成管线的 DaFISH，将逐点发射颜色分解为表面反照率与球谐表示的光照因子，以缓解相机与光源刚性同装导致的姿态相关光照问题。

### 研究问题
许多真实采集场景中，主动光源（如相机闪光灯、水下载具灯、内窥镜或腹腔镜光源）与相机刚性连接；相机移动时光源随之移动，造成每个表面点的光照方向随视角变化。NeRF、Gaussian Splatting 等神经渲染方法会把这种姿态相关光照编码为表面颜色，从而产生外观不一致，并增加恢复底层场景的难度。

### 核心思路/方法
- 提出 **DaFISH**，可插入任意新视角合成（NVS）管线（如 NeRF）。
- 将逐点发射颜色分解为**表面反照率**与**球谐（SH）表示的光照因子**。
- 训练时直接评估 SH 光照，从而稳定地联合优化反照率、光照与几何。
- 基于闭式 SH 到辐照度的转换，训练流程从 SH 评估到体渲染完全可微。
- 提供解析式光照泛化到任意相机姿态的能力，无需重新训练。

### 主要贡献
- 针对相机同装主动光源导致的姿态相关光照问题，提出可插拔的光照分解方案 DaFISH。
- 将反照率与 SH 光照因子分解，并实现从 SH 评估到体渲染的完全可微训练。
- 支持对任意相机姿态的解析式光照泛化，无需重训练。
- 摘要在五个场景的留出帧上报告：DaFISH 在所有对比方法中取得最佳平均 PSNR（38.91 dB）、SSIM（0.9613）与 LPIPS（0.0582），并优于最强的 splatting 基线及最接近的 NeRF 基线；相较先前方法能跨视角更一致地恢复场景。

### 局限性
- 摘要未提供足够信息说明方法在非刚性光源、多光源或复杂全局光照条件下的适用性。
- 摘要未提供足够信息说明计算开销、训练时间与显存需求。
- 摘要未提供足够信息说明五个场景的具体构成、数据规模及基线方法的完整列表。
- 摘要未提供足够信息说明对极端相机姿态或稀疏视角的鲁棒性。

### 阅读优先级
**中**。理由：该工作针对相机同装主动光源这一明确且具有实际采集意义的场景，方法可插入现有 NVS 管线，并给出定量指标；但摘要仅概述核心分解与结果，未展开实验细节与适用边界，适合作为该方向的方法参考而非必须优先精读的综述性文献。

</details>

<details>
<summary>Abstract</summary>

Many real-world capture scenarios involve an active light source rigidly attached to the camera: camera flashes for dark-environment imaging, underwater vehicle lights, and endoscopic/laparoscopic medical procedures. As the camera moves, the co-mounted light moves with it, causing the illumination direction at each surface point to change across views. Neural rendering methods (NeRF, Gaussian Splatting) encode this pose-dependent illumination as surface coloration, producing appearance inconsistencies and making it harder to recover the underlying scene. We present \textbf{DaFISH}, which can be plugged into any novel-view synthesis (NVS) pipeline such as NeRF. It factorizes per-point emitted color into surface albedo and a spherical harmonic (SH)-represented illumination factor. During training, the SH illumination is evaluated directly, enabling stable joint optimization of albedo, lighting, and geometry. \textbf{DaFISH} provides analytical generalization of illumination to arbitrary camera poses without retraining. Building on the closed-form SH-to-irradiance conversion, the training pipeline is fully differentiable from SH evaluation through volume rendering. Averaged over the held-out frames of the five scenes, \textbf{DaFISH} attains the best mean PSNR (38.91\,dB), SSIM (0.9613), and LPIPS (0.0582) among all compared methods. It improves over the strongest splatting baseline as well as the closest NeRF-based baseline, while recovering the scene consistently across views compared to prior methods.

</details>

#### 2026-10-15 - CF-Splat: Closed-Form Triangle Splatting with Mesh Priors

**Authors:** Yixin Fang, Liang Zhao
**Links:** [abs](https://arxiv.org/abs/2610.22108) - [pdf](https://arxiv.org/pdf/2610.22108)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, 3DGS, novel view synthesis, view synthesis, radiance, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CF-Splat: Closed-Form Triangle Splatting with Mesh Priors
- 作者：Yixin Fang, Liang Zhao
- 出版日期：2026-10-15T15:49:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.22108

### 一句话总结
CF-Splat 提出一种基于已知网格先验的闭式三角 splatting 框架，将多视图外观估计转化为全局线性最小二乘问题，从而避免迭代非线性优化，在保持竞争性或更优新视角合成质量的同时大幅降低计算时间与显存占用。

### 研究问题
现有基于 splatting 的辐射场表示通常依赖迭代非线性优化，需要联合优化数百万个相互耦合的图元参数，导致计算时间长、峰值 GPU 显存消耗大，并且容易陷入局部极小值。论文关注的问题是如何在已知网格几何与已标定相机的条件下，高效地估计场景外观，避免上述迭代非线性优化带来的代价与不稳定性。

### 核心思路/方法
论文的关键洞察是：在给定网格几何和标定相机的条件下，通过适当形式化问题，渲染像素颜色可以表示为关于每个顶点球谐（SH）系数的线性函数。因此，多视图场景外观估计可被建模为一个全局线性最小二乘（LLS）问题，无需迭代非线性优化。为保证在多视图观测覆盖不均匀时解仍适定，作者引入自适应 SH 正则化，约束支持不足的高阶 SH 系数，从而得到唯一的全局极小值。为扩展到大规模场景，作者开发了三角形结构的无矩阵预条件共轭梯度求解器，避免显式构造大型稀疏法方程系统，同时产生与 LLS 相同的解。

### 主要贡献
- 提出 CF-Splat，一种面向已知网格（预先存在或由上游建图/重建流程提供）的闭式三角 splatting 框架，用于高效场景外观估计。
- 将多视图外观估计形式化为关于每顶点 SH 系数的全局线性最小二乘问题，避免迭代非线性优化。
- 引入自适应 SH 正则化，以在观测覆盖不均匀时保证适定性并得到唯一全局极小值。
- 开发三角形结构的无矩阵预条件共轭梯度求解器，避免显式构造大型稀疏法方程系统，提升大规模场景可扩展性。
- 在多种真实世界数据集上的实验表明，与最先进 splatting 方法相比，CF-Splat 达到竞争性或更优的 NVS 质量；在不同规模场景下，相比 3DGS 在消费级笔记本上平均减少约 27.5–378.0 倍计算时间，峰值 GPU 显存平均降低约 1.8 倍。

### 局限性
摘要未提供足够信息。摘要未说明该方法是否依赖高质量网格先验、对网格误差或缺失的鲁棒性、在无网格或网格质量较差场景下的适用性，以及具体数据集、评价指标和消融实验细节。

### 阅读优先级
中。理由：该论文聚焦于基于网格先验的闭式 splatting 外观估计，针对迭代优化耗时长、显存高、易陷局部极小值的问题提出线性最小二乘与无矩阵求解方案，并报告了显著效率提升，对神经渲染与机器人感知中的高效 NVS 有潜在价值。但摘要未提供网格先验依赖程度、鲁棒性边界和实验细节，且方法前提是已知网格几何，适用场景相对受限，因此优先级为中等而非高。

</details>

<details>
<summary>Abstract</summary>

Splatting-based radiance-field representations have recently gained popularity in robotic perception, enabling high-quality novel-view synthesis (NVS) through explicit scene primitives. However, existing splatting methods typically rely on iterative nonlinear optimization that jointly optimizes millions of coupled primitive parameters, resulting in substantial computation time, peak GPU memory consumption, and susceptibility to local minima. In this paper, we propose CF-Splat, a novel closed-form triangle-splatting framework for efficient scene appearance estimation over a known mesh either pre-existing or provided by upstream mapping or reconstruction pipelines. Our key insight is that, by properly formulating the problem over the given mesh geometry and calibrated cameras, the rendered pixel colors can be expressed linearly with respect to the per-vertex spherical harmonics (SH) coefficients, allowing multi-view scene appearance estimation to be formulated as a global linear least-squares (LLS) problem without the need of iterative nonlinear optimization. To guarantee a well-posed solution under uneven multi-view observation coverage, we introduce adaptive SH regularization that constrains insufficiently supported high-order SH coefficients and yields a unique global minimizer. To ensure the scalability to large-scale scenes, we develop a triangle-structured matrix-free preconditioned conjugate-gradient solver that avoids explicitly constructing the large sparse normal system while producing the same LLS solution. Experiments on diverse real-world datasets demonstrate that CF-Splat achieves competitive or superior NVS quality compared with state-of-the-art splatting methods. While, CF-Splat requires approximately 27.5-378.0 times less computation time and 1.8 times lower peak GPU memory on average than 3DGS across scenes of different scales on a consumer-grade laptop.

</details>

#### 2026-10-15 - Edit4D: Editable 4D Scene Generation with Textual Control

**Authors:** Chanwoo Kim, Tackgeun You, Hwasup Lim
**Links:** [abs](https://arxiv.org/abs/2610.21668) - [pdf](https://arxiv.org/pdf/2610.21668)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Edit4D: Editable 4D Scene Generation with Textual Control
- 作者：Chanwoo Kim, Tackgeun You, Hwasup Lim
- 出版日期：2026-10-15T10:52:22Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.21668 ；PDF：https://arxiv.org/pdf/2610.21668 ；项目页：https://chanwo0kim.github.io/Edit4D/

### 一句话总结
Edit4D 是一个可编辑的文本到 4D 场景生成框架，通过将背景与动态角色分开表示并分阶段生成，以支持相机控制和对象级编辑。

### 研究问题
摘要指出，现有文本驱动动态场景生成方法通常生成整体场景视频，背景与动态角色相互耦合，因此难以进行对象级编辑和灵活的相机控制；同时可编辑 4D 场景生成还需在编辑时保持空间几何与时间动态，这仍是挑战。

### 核心思路/方法
- 采用阶段特定（stage-specific）的生成流程，将 4D 场景拆分为背景与动态角色两个独立表示。
- 给定用户指令后，先将其分解为背景、动态角色、场景-角色合成对应的阶段提示。
- 使用文本到图像与相机条件生成先验合成多视角场景图像，并重建背景的 3D Gaussian splatting 表示。
- 生成角色图像，用图像条件视频先验进行动画化，重建 4D mesh，并绑定 Gaussian primitives 得到角色表示。
- 通过文本引导分割与接触感知优化将两部分组合，再进行全局场景细化以提升协调性与渲染一致性。

### 主要贡献
- 提出 Edit4D，一个可编辑的文本到 4D 场景生成框架，从分离的背景与动态角色表示构建 4D 场景。
- 通过阶段特定提示分解与分阶段生成流程，缓解背景与角色耦合带来的编辑和相机控制困难。
- 整合阶段特定组件后，支持可控相机运动、灵活的对象级编辑，以及可编辑 4D 场景的实际构建。

### 局限性
摘要未提供足够信息。摘要未给出定量或定性实验细节、失败案例、计算成本、编辑类型覆盖范围、评估指标或用户研究结果。

### 阅读优先级
中。理由：该工作聚焦文本到 4D 场景生成中的可编辑性与对象级编辑，问题定位明确，方法流程具有结构性；但摘要未提供实验验证细节，是否显著优于现有方法、适用边界与实际可用性尚无法仅凭摘要判断。

</details>

<details>
<summary>Abstract</summary>

We introduce Edit4D, an editable text-to-4D scene generation framework that constructs 4D scenes from separate background and dynamic character representations. Recent advances in generative models have enabled text-driven dynamic scene synthesis, but editable 4D scene generation remains challenging due to the need to preserve spatial geometry and temporal dynamics. Existing approaches typically generate holistic scene videos, where the background and dynamic characters are coupled, making object-level editing and flexible camera control difficult. Edit4D addresses these limitations through a stage-specific generation pipeline. Given a user instruction, Edit4D first decomposes it into stage-specific prompts for background, dynamic character, and scene-character composition. Using these prompts, we synthesize multi-view scene images with text-to-image and camera-conditioned generative priors and reconstruct a background 3D Gaussian splatting representation. We then generate a character image, animate it with an image-conditioned video prior, reconstruct a 4D mesh, and bind Gaussian primitives to obtain a character representation. Finally, both components are composed through text-guided segmentation and contact-aware optimization. A global scene refinement is then performed to improve harmonization and rendering consistency. By integrating stage-specific components, Edit4D enables controllable camera motion, flexible object-level editing, and the practical construction of editable 4D scenes. Project page: https://chanwo0kim.github.io/Edit4D/

</details>

#### 2026-10-15 - Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation

**Authors:** Sheng Ye, Jiangke Lin, Fudong Wang, Yi Yuan, Zhen-Hui Dong, Yong-Jin Liu
**Links:** [abs](https://arxiv.org/abs/2610.21634) - [pdf](https://arxiv.org/pdf/2610.21634)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation
- 作者：Sheng Ye, Jiangke Lin, Fudong Wang, Yi Yuan, Zhen-Hui Dong, Yong-Jin Liu
- 出版日期：2026-10-15T10:18:41Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.21634) / [PDF](https://arxiv.org/pdf/2610.21634)

### 一句话总结
Anchor3DGS 提出一种无位姿、前馈式的 3D 高斯泼溅框架，用基于信息熵放置的紧凑 3D 锚点表示替代逐像素预测范式，在大幅减少高斯原语数量的同时提升新视角合成质量。

### 研究问题
现有前馈式 3DGS 方法多采用“像素对齐”范式，即每个输入像素预测一个高斯原语。这带来两个问题：
1. 高斯原语数量与输入分辨率及视角数量直接耦合，难以灵活控制表示规模；
2. 在无纹理区域产生冗余原语，而在几何复杂区域覆盖不足。

### 核心思路/方法
- 用**紧凑的锚点表示**替代像素对齐预测：在场景中放置一组 3D 锚点，由信息熵引导，将锚点集中在视觉复杂度较高的区域，同时保持较广的空间覆盖。
- 每个锚点执行**遮挡感知的多视角图像特征聚合**，并与其他锚点进行信息交换，随后被解码为一组局部高斯原语。
- 引入**轻量级特征增强模块**，对高斯泼溅输出的粗略 RGB 结果进行细化，以提升渲染保真度。
- 整体为**无位姿（pose-free）前馈框架**。

### 主要贡献
- 提出 Anchor3DGS，以基于锚点的紧凑表示取代逐像素预测范式，使高斯原语数量与输入分辨率/视角数解耦。
- 利用信息熵引导锚点放置，缓解无纹理区域冗余与几何复杂区域覆盖不足的问题。
- 设计锚点间的遮挡感知聚合与信息交换机制，以及轻量级特征增强模块以改善渲染质量。
- 在多个基准数据集上的实验表明，方法在达到当前最优新视角合成质量的同时，仅使用约一个数量级更少的高斯原语。

### 局限性
摘要未提供足够信息（未提及失败案例、计算开销、锚点数量上限、对特定场景类型的适用性限制等）。

### 阅读优先级
**高**。理由：该工作针对前馈式 3DGS 中“原语数量与输入耦合”这一明确痛点，提出信息熵引导的锚点表示，并声称在显著减少高斯原语数量的同时达到 SOTA 新视角合成质量；若结论成立，对高效 3D 重建与渲染方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent feed-forward 3D Gaussian Splatting (3DGS) methods have enabled effective multi-view 3D reconstruction by predicting Gaussian primitives in a single forward pass. However, existing approaches predominantly adopt a pixel-aligned paradigm that predicts one Gaussian per input pixel, coupling the Gaussian count to the input resolution and number of views. This also leads to redundant primitives in textureless regions and insufficient coverage in geometrically complex areas. We present Anchor3DGS, a pose-free feed-forward 3DGS framework that replaces pixel-aligned prediction with a compact anchor-based representation. Guided by information entropy, our method places a set of 3D anchors in the scene, concentrating them in regions of higher visual complexity while maintaining broad spatial coverage. Each anchor performs occlusion-aware aggregation of multi-view image features, exchanges information with other anchors, and is decoded into a set of local Gaussians. A lightweight feature enhancement module further refines the coarse RGB output from Gaussian splatting and improves rendering fidelity. Extensive experiments on diverse benchmark datasets demonstrate that our Anchor3DGS achieves state-of-the-art novel view synthesis quality while only using an order of magnitude fewer Gaussian primitives.

</details>

#### 2026-10-15 - Training-Free Target-Aware Refinement of 3D Gaussian Language Map

**Authors:** Sibaek Lee, Kyeongsu Kang, Seongbo Ha, Yewon Jeon, Joonyeol Choi, Daegeol Ko, Jaehyuk Hur, Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo, Hyeonwoo Yu
**Links:** [abs](https://arxiv.org/abs/2610.21619) - [pdf](https://arxiv.org/pdf/2610.21619)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, robotics, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Training-Free Target-Aware Refinement of 3D Gaussian Language Map
- 作者：Sibaek Lee, Kyeongsu Kang, Seongbo Ha, Yewon Jeon, Joonyeol Choi, Daegeol Ko, Jaehyuk Hur, Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo, Hyeonwoo Yu
- 出版日期：2026-10-15T10:00:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.21619 ；PDF：https://arxiv.org/pdf/2610.21619

### 一句话总结
提出一种无需训练、面向指定目标的三维高斯语言地图精修方法，在保留开放词汇查询能力的同时，提高用户指定目标的定位与分割可靠性。

### 研究问题
将视觉—语言特征蒸馏到 3D Gaussian Splatting 后可得到可用任意文本查询的语言地图，但在实际部署中，当前蒸馏地图往往难以可靠定位一小部分用户指定目标，同时又必须保持对其他词的开放词汇查询能力。因此，问题在于：如何在不重新训练、且不破坏通用查询能力的前提下，对已蒸馏语言地图进行目标感知精修。

### 核心思路/方法
方法是对已蒸馏语言地图进行无需训练的目标感知精修。由可文本提示的分割器引导，在每个检测到的目标区域内，将视觉嵌入与目标文本嵌入进行混合，采用凸组合，其系数决定注入先验的强度；非目标区域保持不变。由于注入过多会覆盖外观线索并影响通用查询能力，方法为每个目标寻找仍能使其“胜出”的最小系数，并以闭式解获得所有系数，从而无需调参。作者还指出语言目标定位中的一种注入失败模式：文本嵌入共享共同分量，注入后会使标准余弦读出变得与查询无关，而在读出中加入中心化步骤可消除该问题。

### 主要贡献
- 提出一种无需训练、目标感知的三维高斯语言地图精修方法。
- 通过凸组合将目标文本嵌入注入检测到的目标区域，并为每个目标以闭式解求取最小注入系数，避免超参数调优。
- 识别出注入文本嵌入导致语言目标定位中标准余弦读出与查询无关的失败模式，并通过读出中的中心化步骤解决。
- 在三个基准上持续提升开放词汇分割，在 Replica 上约为基线 mIoU 的两倍，并比基础地图更可靠地定位语言目标。
- 该方法可作为插件迁移到现成的基于场和对象级的语言地图，并支持四足机器人导航到自然语言目标的真实世界演示。

### 局限性
摘要未提供足够信息。摘要未说明方法在哪些具体场景下会失效、对分割器质量的依赖程度、计算开销、基准细节、失败案例范围以及真实世界演示的具体限制。

### 阅读优先级
中。理由：论文关注 3D Gaussian Splatting 语言地图在部署中的目标定位可靠性，提出无需训练、无超参数的精修方案，并涉及开放词汇分割与机器人导航演示，方向具有实用性；但摘要未提供足够实验细节与局限分析，是否值得深入阅读取决于读者对 3D 语言地图、开放词汇查询或机器人导航的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Distilling vision-language features into 3D Gaussian Splatting yields a language map that can be queried with arbitrary text. In deployment, however, a small set of user-specified targets must be reliably located, which current distilled maps often miss, while open-vocabulary queryability for other words must remain intact. We propose a training-free, target-aware refinement of an already-distilled language map. Guided by a text-promptable segmenter, the visual embedding inside each detected target region is blended with the target text embedding, a convex combination whose coefficient sets the amount of injected prior, while non-target regions are left untouched. Injecting too much overwrites appearance cues and general queryability, so we seek, for each target, the smallest coefficient that still lets it win, and we obtain every coefficient in closed form, leaving no hyperparameters to tune. We further identify a failure mode of injection in language-goal localization. Text embeddings share a common component, and injecting them makes the standard cosine read-out query-agnostic, which a centering step in the read-out removes. Across three benchmarks, the refinement consistently improves open-vocabulary segmentation, roughly doubling the base mIoU on Replica, and localizes language goals more reliably than the base map. It also transfers as a plug-in to off-the-shelf field-based and object-level language maps and supports a real-world demonstration in which a legged robot navigates to natural-language goals. Project page and code: https://lab-of-ai-and-robotics.github.io/target-aware-langmap/

</details>

#### 2026-10-15 - ResStreamGS: Residual-Sensitive Dual-Stream Gaussian Splatting for Mobile Volumetric Video Streaming

**Authors:** Haoran Liu, Di Wu, Wang Luo, Hengyuan Na, Miao Hu, Guocong Quan
**Links:** [abs](https://arxiv.org/abs/2610.21121) - [pdf](https://arxiv.org/pdf/2610.21121)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ResStreamGS: Residual-Sensitive Dual-Stream Gaussian Splatting for Mobile Volumetric Video Streaming
- 作者：Haoran Liu, Di Wu, Wang Luo, Hengyuan Na, Miao Hu, Guocong Quan
- 出版日期：2026-10-15T02:25:39Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.21121 ；PDF：https://arxiv.org/pdf/2610.21121

### 一句话总结
ResStreamGS 针对移动体积视频流中“所有高斯点都按帧变化编码”不适配全场景内容的问题，提出按高斯点时间行为分流的双流框架，将稳定高斯点按 GOP 复用、仅对残差敏感高斯点进行逐帧视频编码传输。

### 研究问题
实时移动体积视频需要沉浸式自由视角体验，但在带宽和计算受限条件下高质量 3D 内容传输仍然困难。现有 3D Gaussian Splatting 流式系统（如 V³）通过视频编解码器与硬件解码传输随时间变化的高斯属性，但将全部高斯点都视为逐帧变化信号，不适合包含大量时间稳定区域的全场景内容。摘要指出，逐帧适配并编码所有高斯点会导致复杂全场景内容的质量退化，尤其是在时间稳定区域。

### 核心思路/方法
- 根据高斯点的时间行为进行处理，提出残差敏感的双流框架。
- 通过轻量级探针适配识别残差敏感基元。
- 在每个 Group of Pictures（GOP）内复用稳定高斯点。
- 稳定高斯点每个 GOP 只传输一次。
- 仅残差敏感高斯点保留在逐帧、可硬件解码的视频流中。

### 主要贡献
- 提出 ResStreamGS，一种残差敏感双流高斯泼溅框架，用于移动体积视频流。
- 通过轻量级探针适配识别残差敏感基元，并在 GOP 内复用稳定高斯点。
- 将传输拆分为 GOP 级稳定高斯点与逐帧硬件可解码的残差敏感高斯点视频流。
- 在复杂全场景体积视频实验中，相比受控的 V³ 风格全高斯基线，编码后 PSNR 提升 7.51–8.35 dB，摊销负载最多降低 56.5%，并在 Qualcomm Snapdragon 778G 平台上达到 30.883 FPS。

### 局限性
摘要未提供足够信息。摘要未说明探针适配的具体开销、不同场景类型下的泛化性、在更高移动性或动态内容中的表现、端到端延迟与能耗细节，也未提供与更多现有方法的完整对比。

### 阅读优先级
高。理由：该工作直接面向移动体积视频流的关键瓶颈，提出明确的双流传输机制，并在摘要中报告了显著的 PSNR、负载和端侧帧率指标；对 3DGS 流式传输、移动端实时渲染与体积视频编码方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Real-time mobile volumetric video enables immersive free-viewpoint experiences, but delivering high-quality 3D content under constrained bandwidth and computation remains challenging. Recent 3D Gaussian Splatting (3DGS) systems, such as V$^3$, enable efficient mobile streaming by encoding time-varying Gaussian attributes with commodity video codecs and hardware decoding. However, existing pipelines treat all Gaussians as frame-varying signals, which is poorly suited to full-scene content where large portions remain temporally stable. Our empirical study shows that frame-wise adaptation and video coding of all Gaussians cause quality degradation in complex full-scene content, particularly in temporally stable regions. To address this issue, we propose ResStreamGS, a residual-sensitive dual-stream framework that processes Gaussians according to their temporal behavior. ResStreamGS identifies residual-sensitive primitives through lightweight probe adaptation and reuses stable Gaussians within each Group of Pictures (GOP). Stable Gaussians are transmitted once per GOP, while only residual-sensitive Gaussians remain in the frame-wise hardware-decodable video stream. Experiments on complex full-scene volumetric videos show that ResStreamGS improves post-codec PSNR by 7.51--8.35~dB over a controlled V$^3$-style all-Gaussians baseline, reduces amortized payload by up to 56.5%, and achieves 30.883~FPS on a Qualcomm Snapdragon 778G platform.

</details>

#### 2026-10-14 - Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting

**Authors:** Seungmi Choi, Ji-Hyoun Choi, Suhyun Jo, Tae-Gwon Park, Hui Yong Kim
**Links:** [abs](https://arxiv.org/abs/2610.20590) - [pdf](https://arxiv.org/pdf/2610.20590)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting
- 作者：Seungmi Choi, Ji-Hyoun Choi, Suhyun Jo, Tae-Gwon Park, Hui Yong Kim
- 出版日期：2026-10-14T17:58:28Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.20590

### 一句话总结
本文提出 MFGS，一种端到端前馈的多视角特征编码框架，通过直接编码多视角特征而非显式高斯表示，联合表示几何与外观，从而提升 3DGS 场景编码的率失真性能并降低计算开销。

### 研究问题
现有前馈 3DGS 场景编码流程通常先“生成完整高斯表示”，再分别编码其几何与外观属性，往往包含不可微操作。这种“先生成后压缩”的管道需要复杂的属性专用编解码器设计，并且由于限制了跨属性冗余的利用，率失真性能受到制约。论文旨在解决这一编码流程复杂、性能受限的问题。

### 核心思路/方法
MFGS 不再压缩显式高斯表示，而是从输入图像中提取多视角特征，并将其编码为紧凑比特流。通过端到端的率失真训练，MFGS 学习能够联合表示几何与外观的紧凑多视角特征，接收端则从解码后的特征预测高斯属性。此外，论文引入重要性引导的高斯选择，以适应不同渲染预算，使接收端能够从同一比特流中调整用于渲染的高斯数量。

### 主要贡献
- 提出 MFGS，一种端到端前馈的场景编码框架，直接编码多视角特征而非显式高斯表示。
- 通过端到端率失真训练，学习联合表示几何与外观的紧凑多视角特征，接收端可据此预测高斯属性。
- 引入重要性引导的高斯选择，支持从同一比特流调整渲染所需高斯数量，以适应不同渲染预算。
- 在 RE10K、ACID 和 DL3DV 上，按 BD-rate 衡量，相比“先生成后压缩”管道实现 99.76–99.86% 的比特率节省，同时总 GMACs 降低 52–55%，并提供约 12 倍的端到端加速。

### 局限性
摘要未提供足够信息。摘要未说明方法在特定场景类型、极端稀疏视角、训练数据规模或泛化能力方面的限制，也未提供失败案例或消融实验的负面结果。

### 阅读优先级
高。理由：该论文针对前馈 3DGS 场景编码中“先生成后压缩”管道的关键瓶颈提出端到端替代方案，报告了显著的比特率节省、计算量降低和速度提升，且涉及跨属性冗余利用与可变渲染预算，属于神经场景表示与渲染方向中较有潜力的工作。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) methods enable efficient reconstruction of 3D scenes from sparse multi-view images in a single forward pass, without scene-specific optimization. However, existing feed-forward scene-coding pipelines first generate a complete Gaussian representation and then encode its geometry and appearance attributes separately, often involving non-differentiable operations. The resulting 'generate-then-compress' pipeline requires complex attribute-specific codec designs and limits rate-distortion performance by restricting the exploitation of cross-attribute redundancy. We propose multi-view feature coding for Gaussian splatting (MFGS), an end-to-end feed-forward framework for scene coding. Instead of compressing an explicit Gaussian representation, MFGS extracts multi-view features from the input images and encodes them into a compact bitstream. Through end-to-end rate-distortion training, MFGS learns compact multi-view features that jointly represent geometry and appearance, enabling the receiver to predict Gaussian attributes from the decoded features. We further introduce importance-guided Gaussian selection to accommodate different rendering budgets, allowing the receiver to adjust the number of Gaussians used for rendering from the same bitstream. Across RE10K, ACID, and DL3DV, MFGS achieves 99.76-99.86% bitrate savings over the generate-then-compress pipeline, as measured by BD-rate, while reducing total GMACs by 52-55% and providing an approximately 12 times end-to-end speedup.

</details>

#### 2026-10-14 - Where Should the Gaussians Go? Reusable Label-Aware Allocation for Budget-Constrained Gaussian Splatting of Cinematic CT

**Authors:** Bowen Xiang, Dingjie Su, Jon S. Heiselman, Michael I. Miga
**Links:** [abs](https://arxiv.org/abs/2610.20397) - [pdf](https://arxiv.org/pdf/2610.20397)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Where Should the Gaussians Go? Reusable Label-Aware Allocation for Budget-Constrained Gaussian Splatting of Cinematic CT
- 作者：Bowen Xiang, Dingjie Su, Jon S. Heiselman, Michael I. Miga
- 出版日期：2026-10-14T16:01:38Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.20397) / [PDF](https://arxiv.org/pdf/2610.20397)

### 一句话总结
该论文针对电影级 CT 渲染中固定高斯数量预算下的位置分配问题，提出可复用的、标签感知的高斯放置前端，使固定预算 B 个高斯的位置无需逐患者优化即可确定。

### 研究问题
在电影级 CT 的 3D 高斯溅射渲染中，解剖标签有助于保留血管结构，但场景表示仍需逐患者优化，其中致密化过程决定高斯的位置，而实时显示又会限制高斯数量。论文聚焦于其中一个环节：在固定 B 个高斯预算下，应把这些高斯放置在哪里。

### 核心思路/方法
论文提出一种可复用、标签感知的分配前端，将患者的 CT、标签和传递函数映射到 2mm 单元上的密度分布，并从中抽取恰好 B 个位置，且无需逐患者优化；其他高斯属性仍逐患者拟合。该前端从逐患者优化场景中一次性学习，并以两种形式实现：群体训练的神经先验，以及可解释的七参数可见性感知闭式解（VACF）。

### 主要贡献
- 提出可复用的标签感知高斯位置分配前端，用于固定预算 B 下的高斯放置，避免逐患者位置优化。
- 实现两种形式：群体训练的神经先验和可解释的七参数可见性感知闭式解（VACF）。
- 在 20 名留出患者、10K–100K 高斯预算下，相较均匀分配，血管掩膜 PSNR 提升 4.5–7.1dB；相较剪枝后的稠密体素对齐模型提升 1.6–3.3dB。
- 神经先验在各预算下与逐患者优化分配无显著差异；VACF 在血管上与其相差不超过 0.6dB；在 19 名外部患者上，神经先验同样在血管上匹配该分配，VACF 相差不超过 0.7dB。
- 作为位置优化初始化时，VACF 分配在 10K 高斯下血管表现优于逐患者致密化；在 25K 下，优化 118s 后的血管 PSNR 高于致密化优化 248s 的结果。
- 在渲染预设改变时，VACF 可迁移到新颜色和光照，但不能迁移到无标签传递函数；神经先验则呈现相反模式。

### 局限性
摘要未提供足够信息说明神经先验与 VACF 的失败边界、对标签质量或传递函数设计的依赖程度、计算成本细节、外部患者规模之外的泛化性，以及除血管外其他解剖结构的表现。

### 阅读优先级
高。理由：该论文直接处理固定高斯预算下的位置分配这一关键瓶颈，提出可复用前端并报告了跨患者、跨预算和外部患者的定量结果，同时给出神经先验与可解释闭式解两种实现，对高斯溅射在医学 CT 渲染中的实际部署具有明确参考价值。

</details>

<details>
<summary>Abstract</summary>

Anatomical labels help 3D Gaussian splatting preserve vessels in cinematic renderings of CT, but the representation is still found by optimising each patient's scene, where densification decides where Gaussians go, while real-time displays cap their number. We address one part of this process: deciding where a fixed budget of B Gaussians should be placed. We propose a reusable, labelaware allocation front end that maps a patient's CT, labels and transfer function to a density over 2mm cells and draws exactly B positions from it without per-patient optimisation; the other Gaussian attributes are still fitted per patient. The front end is learned once from per-patient optimised scenes and implemented as a population-trained neural prior and an interpretable seven-parameter visibility-aware closed form (VACF). With identical attribute fitting on 20 held-out patients at 10K-100K Gaussians, both raise vessel-masked PSNR over uniform allocation by 4.5-7.1dB and over pruning a dense voxel-aligned model by 1.6-3.3dB. The neural prior does not differ significantly from per-patient optimised allocation at any budget, and VACF is within 0.6dB of it on vessels; on 19 external patients the neural prior again matches it on vessels and VACF is within 0.7dB. As an initialisation for position optimisation, VACF allocation beats per-patient densification on vessels at 10K Gaussians and, at 25K, reaches a higher vessel PSNR after 118s of optimisation than densification after 248s. Under altered rendering presets, VACF transfers to new colours and lighting but not to a label-free transfer function, whereas the neural prior shows the opposite pattern.

</details>

#### 2026-10-14 - GLoD-LVSM: Learning Geometry-Grounded Continuous-LoD Scene Representations for Large View Synthesis Models

**Authors:** Weikai Lin, Nicholas Milef, Carl S Marshall, Grant Kaijuin Yang, Todd Keeler, Yuhao Zhu
**Links:** [abs](https://arxiv.org/abs/2610.20254) - [pdf](https://arxiv.org/pdf/2610.20254)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** view synthesis, scene representation, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GLoD-LVSM: Learning Geometry-Grounded Continuous-LoD Scene Representations for Large View Synthesis Models
- 作者：Weikai Lin, Nicholas Milef, Carl S Marshall, Grant Kaijuin Yang, Todd Keeler, Yuhao Zhu
- 出版日期：2026-10-14T14:25:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.20254) | [PDF](https://arxiv.org/pdf/2610.20254)

### 一句话总结
GLoD-LVSM 为大视图合成模型提出一种紧凑的、几何接地的连续细节层次场景表示，用于缓解 token 冗余带来的存储与渲染开销。

### 研究问题
大视图合成模型（LVSMs）能从稀疏视图快速重建场景并渲染新视图，但存在 token 冗余，导致不必要的存储和渲染成本。论文关注的问题是如何在 LVSMs 中构建更紧凑的场景表示，以减少场景 token 数量并加速渲染，同时尽量保持渲染质量。

### 核心思路/方法
- 不学习固定的一组场景锚点初始化，而是学习一个连续场，用于初始化数量灵活的锚点，以匹配期望的预算。
- 使用一个 condenser 将场景信息聚合到这些锚点中，连续场与 condenser 端到端训练。
- condenser 推断 reference-token 和锚点几何，通过 geometry-grounded attention 指导压缩，从而提升渲染质量，并在解码阶段支持视锥剔除（frustum culling）。

### 主要贡献
- 提出 GLoD-LVSM，一种面向 LVSMs 的紧凑、几何接地、具有连续细节层次的场景表示。
- 与现有 LVSM 场景压缩基线相比，在渲染质量与场景 token 数量的权衡上取得最佳表现。
- 与未压缩基础模型相比，在无质量损失的情况下将场景 token 数量减少 33.4%，渲染加速 1.23×。
- 在放宽质量损失预算时，场景 token 数量减少可达 85.5%，渲染加速 3.00×。
- 分析显示，视图合成监督带来了涌现的场景深度和自组织锚点：锚点与表面对齐，并能根据局部纹理复杂度调整密度。
- 该场景表示除渲染外还支持场景语义理解，显示其更广泛下游任务的潜力。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、适用范围限制、对特定数据集或硬件条件的依赖。摘要未提供足够信息说明其语义理解能力的具体评测范围与上限。摘要未提供足够信息说明连续场训练成本、condenser 结构细节及与基线相比在极端稀疏视图下的表现。

### 阅读优先级
高。理由：该论文直接针对 LVSMs 的 token 冗余与渲染效率问题，提出了明确的场景表示设计，并给出量化压缩与加速结果；同时涉及涌现深度、自组织锚点与语义理解等扩展能力，对神经场景表示与渲染方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Large view synthesis models (LVSMs) reconstruct scenes from sparse views and render novel views quickly, but they incur unnecessary storage and rendering costs due to token redundancy. We present GLoD-LVSM, a compact, geometry-grounded scene representation for LVSMs with continuous levels of detail. First, instead of learning a fixed set of scene anchor initializations, GLoD-LVSM learns a continuous field that initializes a flexible number of anchors to match the desired budget. A condenser then aggregates scene information into these anchors, with both the field and condenser trained end-to-end. Second, the condenser infers reference-token and anchor geometry to guide compression through geometry-grounded attention, improving rendering quality and enabling frustum culling during decoding. Compared with existing LVSM scene-compression baselines, GLoD-LVSM achieves the best trade-off between rendering quality and scene token count. Compared with the uncompressed base model, GLoD-LVSM reduces the scene-token count by 33.4% and accelerates rendering by $1.23\times$ with no quality loss. Under a relaxed quality-loss budget, the reduction increases to 85.5%, with $3.00\times$ rendering speedup. Further analysis reveals that view-synthesis supervision yields emergent scene depth and self-organized anchors that align with surfaces and adapt their density to local texture complexity. Beyond rendering, we further show that our scene representation also supports scene-semantic understanding, highlighting its potential for broader downstream tasks.

</details>

#### 2026-10-14 - VisibilitySplat: Ray-Traced Occlusion for Relighting with 3D Gaussian Splatting

**Authors:** Sven Kluge, Oliver Staadt
**Links:** [abs](https://arxiv.org/abs/2610.19847) - [pdf](https://arxiv.org/pdf/2610.19847)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, inverse rendering, relighting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VisibilitySplat: Ray-Traced Occlusion for Relighting with 3D Gaussian Splatting
- 作者：Sven Kluge, Oliver Staadt
- 出版日期：2026-10-14T09:17:40Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.19847) / [PDF](https://arxiv.org/pdf/2610.19847)

### 一句话总结
该论文在 3D Gaussian Splatting 逆渲染流程中引入稀疏的、基于 BVH 加速点光线追踪的可见性查询模块，以显式建模遮挡，从而改进重光照与材质-光照分解。

### 研究问题
论文关注 3D Gaussian Splatting（3DGS）下的逆渲染问题，即在重光照以及材质与光照分解中，如何显式建模可见性/遮挡。摘要指出，该方法旨在解决标准 3DGS 光栅化流程中缺乏显式可见性建模的问题，并将其用于提升重光照和材质-光照解耦效果。

### 核心思路/方法
- 在标准光栅化 3DGS 流程基础上，增加一个“稀疏可见性 oracle”。
- 该 oracle 从采样光照方向估计高斯原语的透射率加权遮挡。
- 实现方式为基于点的光线追踪，并使用包围体层次结构（BVH）加速。
- 在逆渲染目标中稀疏查询该可见性 oracle，同时保留原始 3DGS 循环，以维持训练效率、交互式可视化和工具兼容性。
- 着色采用基于物理的渲染（PBR）公式，包含 principled microfacet BRDF 和低分辨率 HDR 环境贴图。
- 在 TensoIR 合成数据集上，与基于 NeRF、张量表示和 3DGS 的基线方法进行比较。

### 主要贡献
- 为 3DGS 逆渲染引入显式可见性建模，通过稀疏点式光线追踪查询估计透射率加权遮挡。
- 将可见性 oracle 与标准光栅化 3DGS 流程结合，在保留 3DGS 训练效率和生态兼容性的同时支持重光照与材质/光照分解。
- 采用 PBR 着色框架，结合 microfacet BRDF 与 HDR 环境贴图。
- 在 TensoIR 合成数据集上评估新视角合成、反照率重建和重光照，结果显示具有竞争力的性能，并在若干指标上优于早期基线。
- 消融实验表明，显式可见性建模对重光照和材质-光照解耦有重要贡献，而纯 PBR 监督可能更有利于新视角合成中的外观拟合。

### 局限性
- 摘要未提供足够信息说明方法在真实场景、非合成数据或复杂光照条件下的泛化能力。
- 摘要未提供足够信息说明计算开销、训练时间或推理速度的具体影响。
- 摘要未提供足够信息说明对透明、半透明、镜面或强各向异性材质的处理能力。
- 摘要未提供足够信息说明与所有基线方法的完整定量比较细节及失败案例。
- 摘要未提供足够信息说明 BVH 构建、稀疏查询策略或超参数选择的敏感性。

### 阅读优先级
中。理由：该论文聚焦 3DGS 逆渲染与重光照中的可见性建模，方法思路清晰，且保留 3DGS 生态兼容性，对神经渲染、逆渲染和可重光照表示方向的研究者有参考价值；但摘要仅给出 TensoIR 合成数据集上的结果，且未提供充分实验细节与局限性讨论，因此若关注具体性能、真实场景适用性或工程开销，需要进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

We address inverse rendering with 3D Gaussian Splatting (3DGS) by introducing explicit visibility modeling for relighting as well as material and light decomposition. Our approach augments the standard rasterized 3DGS pipeline with a sparse visibility oracle that estimates transmittance-weighted occlusion for Gaussian primitives from sampled lighting directions. This oracle is implemented using a point-based ray tracer accelerated by a bounding volume hierarchy (BVH) and queried sparsely within the inverse-rendering objectives, while the original 3DGS loop is retained for training efficiency, interactive visualization, and tooling compatibility. Shading follows a physically based rendering (PBR) formulation with a principled microfacet bidirectional reflectance distribution function (BRDF) and low-resolution high-dynamic-range (HDR) environment maps. We evaluate our method on the TensoIR synthetic dataset against baselines based on neural radiance fields (NeRFs), tensor representations, and 3DGS. The results show competitive performance and improvements over several earlier baselines for novel-view synthesis (NVS), albedo reconstruction, and relighting. Ablations indicate that explicit visibility modeling is an important contributor to relighting and material-illumination disentanglement, while pure PBR supervision can favor appearance fitting in NVS. Overall, the findings suggest that sparse, point-based visibility queries effectively complement rasterized splatting for inverse rendering while preserving the practical advantages of the 3DGS ecosystem.

</details>

#### 2026-10-14 - HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration

**Authors:** Annie Bhalla, Dennis Rotondi, Riccardo Giubilato, Kai O. Arras, Wolfgang Stuerzl
**Links:** [abs](https://arxiv.org/abs/2610.19742) - [pdf](https://arxiv.org/pdf/2610.19742)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration
- 作者：Annie Bhalla, Dennis Rotondi, Riccardo Giubilato, Kai O. Arras, Wolfgang Stuerzl
- 出版日期：2026-10-14T08:04:06Z
- 分类：Neural Scene Representations & Rendering（主类）；3D Reconstruction & Multi-view Geometry（次类）
- 链接：https://arxiv.org/abs/2610.19742 ；PDF：https://arxiv.org/pdf/2610.19742

### 一句话总结
论文提出 HyperLoop，将高光谱成像引入基于 3DGS 的 SLAM 回环检测模块，并发现所用传感器 Red-NIR（600–860 nm）波段对岩石地形的区分能力有限，融合高光谱未带来显著精度提升。

### 研究问题
行星漫游车自主导航面临视觉重复、缺乏特征的地形挑战。基于 3D 高斯泼溅（3DGS）的 SLAM 系统虽能稠密建图，但其依赖的 RGB 外观描述子在感知混叠下会退化——在地外环境中，物理上不同的位置可能视觉上完全相同，这是常见失效模式。论文试图解决该场景下的回环检测问题。

### 核心思路/方法
- 提出 HyperLoop，据摘要称为首个将高光谱成像（HSI）集成到基于 3DGS 的 SLAM 系统回环检测模块的框架。
- 高光谱描述子编码材料级光谱签名，用于补充 RGB 特征，以增强对光照变化和视觉重复性的鲁棒性。
- 引入两类 HSI 描述子：
  - Bag-of-Spectral-Words（BoSW）：通过 TF-IDF 加权直方图编码光谱材料分布。
  - PCA-K VLAD（PCAK-VLAD）：捕捉 PCA 压缩光谱签名的一阶残差统计量。
- 在 Strict-AND 与 Weighted 两种融合策略下，将上述 HSI 描述子与 SIFT-VLAD、NetVLAD 两种 RGB 描述子进行组合评估。
- 使用 DLR 的 Moon-Mars Outdoor Test Site（MMOTS）自建数据集，包含四条行星模拟行进路线（共 65.5 m）的同步 RGB-D 与高光谱序列。

### 主要贡献
- 提出 HyperLoop 框架，将 HSI 集成进 3DGS-based SLAM 的回环检测模块。
- 提出两类高光谱描述子 BoSW 与 PCAK-VLAD。
- 在 MMOTS 数据集上系统评估 HSI 描述子与 RGB 描述子（SIFT-VLAD、NetVLAD）在两种融合策略下的表现。
- 给出关键发现：传感器 Red-NIR 范围（600–860 nm）对岩石地形区分能力有限；最佳 HSI 融合（SIFT-VLAD + BoSW，Strict-AND）达到 5.04 cm ATE RMSE，与单独 SIFT-VLAD（4.95 cm）相差在 1.8% 以内；相对 NetVLAD（8.81 cm）的增益归因于 SIFT-VLAD，而非 HSI 融合。
- 由此提出未来在行星 SLAM 任务中采用可捕获诊断性矿物吸收特征的 SWIR 传感器的动机。

### 局限性
- 摘要明确指出当前传感器 Red-NIR 范围（600–860 nm）对岩石地形区分能力有限，HSI 融合未带来显著精度提升。
- 最佳融合结果与单独 SIFT-VLAD 差距仅 1.8%，且相对 NetVLAD 的提升并非来自 HSI 融合。
- 实验仅在 DLR MMOTS 自建数据集、四条模拟路线（共 65.5 m）上进行，摘要未提供更大规模或其他场景的验证信息。
- 摘要未提供关于计算开销、实时性、3DGS 建图质量、失败案例等细节；摘要未提供足够信息。
- 摘要未提供 SWIR 传感器方案的实际实验验证；摘要未提供足够信息。

### 阅读优先级
中。理由：论文主题（行星探索 SLAM 回环检测、高光谱与 3DGS 结合）具有明确的新颖性与领域价值，且其负向/有限增益的实证结论对未来传感器选型有参考意义；但摘要显示核心方法未带来显著性能提升，实验规模较小（65.5 m），若读者关注的是行星 SLAM 或高光谱辅助感知方向，值得阅读以了解失败模式与传感器波段限制；若仅关注通用 3DGS-SLAM 性能提升，则优先级相对较低。

</details>

<details>
<summary>Abstract</summary>

Autonomous navigation of planetary rovers is challenged by visually repetitive, featureless terrain. SLAM systems based on 3D Gaussian Splatting (3DGS) offer dense mapping but rely on RGB appearance descriptors that degrade under perceptual aliasing - a common failure mode in extraterrestrial environments where physically distinct locations appear visually identical. This paper presents HyperLoop, the first framework integrating hyperspectral imaging (HSI) into the loop closure module of a 3DGS-based SLAM system. Hyperspectral descriptors encode material-level spectral signatures complementing RGB features, providing robustness to illumination changes and visual repetitiveness. Two HSI descriptor families are introduced: Bag-of-Spectral-Words (BoSW), encoding spectral material distributions via TF-IDF weighted histograms, and PCA-K VLAD (PCAK-VLAD), capturing first-order residual statistics of PCA-compressed spectral signatures. Both are evaluated with SIFT-VLAD and NetVLAD RGB descriptors under Strict-AND and Weighted fusion strategies on a custom dataset from the Moon-Mars Outdoor Test Site (MMOTS) at DLR, comprising synchronized RGB-D and hyperspectral sequences across four planetary analog traverses (65.5 m total). A key finding is that the sensor's Red-NIR range (600-860 nm) provides limited discriminability for rock terrain: the best HSI fusion (SIFT-VLAD + BoSW, Strict-AND) achieves 5.04 cm ATE RMSE, within 1.8% of SIFT-VLAD alone (4.95 cm). The gain over NetVLAD (8.81 cm) is attributable to SIFT-VLAD, not HSI fusion. This motivates future adoption of SWIR sensors capturing diagnostic mineral absorption features absent from the 600-860 nm range for planetary SLAM missions.

</details>

#### 2026-10-14 - GS-PRM: Gaussian Visual Roadmap for Image-Goal Navigation

**Authors:** Ashraf Siddique, Kyung Min Han, Young J. Kim
**Links:** [abs](https://arxiv.org/abs/2610.19541) - [pdf](https://arxiv.org/pdf/2610.19541)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-PRM: Gaussian Visual Roadmap for Image-Goal Navigation
- 作者：Ashraf Siddique, Kyung Min Han, Young J. Kim
- 出版日期：2026-10-14T03:58:13Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.19541 ；PDF：https://arxiv.org/pdf/2610.19541

### 一句话总结
GS-PRM 提出一种基于 3D Gaussian Splatting 渲染直接构建的“高斯视觉路线图”，用于图像目标导航中的全局规划，并在仿真与真实环境中验证了其长时程导航表现。

### 研究问题
图像目标导航需要全局规划器连接视觉指定的端点，并提供局部策略可跟随的观测。3D Gaussian Splatting 虽能提供地图配准的 RGB、不透明度和深度渲染，但不显式编码可导航拓扑。论文关注如何在不构建占据栅格或符号距离场的情况下，从 3DGS 渲染中直接获得可导航的路线图结构。

### 核心思路/方法
论文提出 GS-PRM：一种高斯视觉路线图，其里程碑、局部连接和视觉参考直接通过 3DGS 渲染构建，而不依赖占据栅格或符号距离场。方法定义了基于渲染的无碰撞配置与路径（RC-free）。全景深度用于为里程碑验证和自适应覆盖提供保守间隙，边缘对齐的正交渲染用于测试机器人的扫掠体积。论文还建立了 GS-PRM 的条件健全性，以及确定性查询完备性和概率性构建完备性的充分条件。

### 主要贡献
- 提出 GS-PRM，一种直接通过 3DGS 渲染构建里程碑、局部连接和视觉参考的高斯视觉路线图，不导出占据栅格或符号距离场。
- 定义 render-based collision-free（RC-free）配置与路径。
- 使用全景深度提供保守间隙以支持里程碑验证和自适应覆盖，并使用边缘对齐正交渲染测试机器人扫掠体积。
- 建立条件健全性，以及确定性查询完备性和概率性构建完备性的充分条件。
- 在仿真和真实环境中实验，展示由 GS-PRM 引导的目标条件策略实现长时程导航；与一个先进的基于 3DGS 的导航系统相比，GS-PRM 导航系统平均成功率最高提升至两倍，并在两者均完成任务时最多减少 57.2% 的旅行时间。

### 局限性
摘要未提供足够信息。摘要未说明方法在何种场景条件下会失效、对 3DGS 重建质量的依赖程度、计算开销、实时性、传感器配置假设，以及仿真与真实实验的具体规模与指标细节。

### 阅读优先级
中。理由：该工作面向图像目标导航与 3DGS 场景表示交叉方向，提出不依赖占据栅格或符号距离场的视觉路线图，并给出完备性条件与仿真/真实实验对比；但摘要未提供足够信息说明其失效条件、计算成本与实验细节，是否优先精读取决于读者对 3DGS 导航、视觉路线图或图像目标导航的具体需求。

</details>

<details>
<summary>Abstract</summary>

Image-goal navigation requires a global planner that connects visually specified endpoints while providing observations that a local policy can follow. Three-dimensional Gaussian Splatting (3DGS) provides map-registered RGB, opacity, and depth renderings, but does not explicitly encode navigable topology. We introduce GS-PRM, a Gaussian visual roadmap whose milestones, local connections, and visual references are constructed directly through 3DGS rendering without deriving an occupancy grid or signed distance field. We define render-based collision-free (RC-free) configurations and paths. Panoramic depth supplies conservative clearance for milestone validation and adaptive coverage, while edge-aligned orthographic rendering tests the robot's swept volume. We establish conditional soundness and sufficient conditions for deterministic query completeness and probabilistic construction completeness of GS-PRM. To validate the performance of GS-PRM, we conduct experiments in both simulated and real-world environments, demonstrating long-horizon navigation using goal-conditioned policies guided by GS-PRM. Compared with a state-of-the-art 3DGS-based navigation system, our GS-PRM-based navigation system achieves up to a twice higher average success rate and reduces travel time by up to 57.2% when both systems complete the navigation task.

</details>

#### 2026-10-14 - RDCompGS: Rate-Distortion Optimization for Compression of 3D Gaussian Splatting with Image Codecs

**Authors:** Huiping Ren, Shuai Wan, Luqian Bai, Zhang Chen, Fuzheng Yang
**Links:** [abs](https://arxiv.org/abs/2610.19538) - [pdf](https://arxiv.org/pdf/2610.19538)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RDCompGS: Rate-Distortion Optimization for Compression of 3D Gaussian Splatting with Image Codecs
- 作者：Huiping Ren, Shuai Wan, Luqian Bai, Zhang Chen, Fuzheng Yang
- 出版日期：2026-10-14T03:55:12Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.19538 ；PDF：https://arxiv.org/pdf/2610.19538

### 一句话总结
RDCompGS 通过在 3D 高斯表示的优化中引入可微的编码码率估计，并与渲染失真共同进行率失真优化，以提升后续图像编解码器压缩后的率失真性能。

### 研究问题
3D Gaussian Splatting（3DGS）能够实现高质量、实时的新视角合成，但需要大量存储与传输资源。将高斯属性映射到 2D 表示可以利用成熟图像编解码器进行高效压缩。然而，具有相近渲染质量的高斯表示在优化过程中通常被同等对待，尽管它们的编码码率存在显著差异，这导致压缩后的率失真（R-D）性能受限。

### 核心思路/方法
论文提出 RDCompGS，一种面向后续编码的 3DGS 压缩方法，目标是实现高斯表示的整体率失真优化。具体做法包括：将编码码率的可微估计引入率失真优化，并与渲染失真共同考虑；此外，使用码率约束调整模型来调节不同压缩条件下的率失真权衡。

### 主要贡献
- 提出 RDCompGS，使高斯表示能够针对后续编码进行整体率失真优化。
- 在率失真优化中引入可微的编码码率估计，并与渲染失真结合。
- 设计码率约束调整模型，用于在不同压缩条件下调节率失真权衡。
- 在三个基准数据集上的实验表明，RDCompGS 在 H.265/HEVC 和 JPEG XL 下分别取得平均 Bjøntegaard Delta Rate 降低 37.84% 和 49.31%。
- 估计码率在不同压缩条件下与实际比特率表现出强相关性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该论文聚焦 3DGS 压缩与率失真优化，并给出明确的 BD-Rate 改进结果，对关注 3DGS 存储传输效率、图像编解码器结合以及率失真优化方向的研究者有较高参考价值；但摘要未展开方法细节、实验设置与局限性，是否具备广泛适用性仍需阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables high-quality, real-time novel view synthesis but requires significant storage and transmission resources. Mapping Gaussian attributes to 2D representations enables efficient compression using mature image codecs. However, Gaussian representations that achieve comparable rendering quality are generally treated similarly during optimization, despite substantial differences in coding rate, leading to limited rate-distortion (R-D) performance after compression. To address this limitation, we propose RDCompGS, a 3DGS compression method that enables overall R-D optimization of Gaussian representations with respect to subsequent coding. A differentiable estimate of the coding rate is incorporated into the R-D optimization with rendering distortion. The rate constraint adjustment model further regulates the R-D trade-off across different compression conditions. Extensive experiments on three benchmark datasets demonstrate that RDCompGS achieves average Bjøntegaard Delta Rate reductions of 37.84% and 49.31% with H.265/HEVC and JPEG XL, respectively. The estimated rate also shows a strong correlation with the actual bit-rate under different compression conditions.

</details>

#### 2026-10-14 - Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence

**Authors:** Yuanyuan Gao, Zhirui Liu, Yuning Gong, Yifei Liu, Yifan Zhan, Kuixuan Jiao, Xiaolong Zhou, Yifan Yang, Hongjie Zhang, Xue Yang, Dan Xu, Zhihang Zhong
**Links:** [abs](https://arxiv.org/abs/2610.19502) - [pdf](https://arxiv.org/pdf/2610.19502)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence
- 作者：Yuanyuan Gao, Zhirui Liu, Yuning Gong, Yifei Liu, Yifan Zhan, Kuixuan Jiao, Xiaolong Zhou, Yifan Yang, Hongjie Zhang, Xue Yang, Dan Xu, Zhihang Zhong
- 出版日期：2026-10-14T03:21:09Z
- 分类：Neural Scene Representations & Rendering（secondary_categories：摘要未提供足够信息）
- 链接：https://arxiv.org/abs/2610.19502 ；PDF: https://arxiv.org/pdf/2610.19502

### 一句话总结
针对稀疏全景与弱纹理条件下多房间室内重建严重欠约束的问题，提出生成式重建与数据整理框架 Holi-Spatial 360，将在线房源全景转换为可渲染、可标注的多房间 3D 环境，并配套数据集与评测基准以提升 VLM 空间理解能力。

### 研究问题
- 空间智能需要可扩展、照片级真实且具备语义基础的 3D 环境，但现有室内数据集以房间尺度采集为主，且依赖昂贵的 LiDAR 获取。
- 在线房地产平台虽提供大量多房间住宅全景，但存在视点稀疏、纹理贫乏区域等问题，导致重建严重欠约束。
- 重建质量会限制后续生成与语义标注的上限。

### 核心思路/方法
- 提出 Holi-Spatial 360，一个生成式重建与数据整理框架，用于将全景转换为带标注的多房间 3D 环境。
- 采用 Correspondence-Guided Geometric Optimization（对应引导的几何优化），将前馈重建先验转化为可靠的跨视角约束，并构建连贯的 3D Gaussian Splatting 表示作为 3D 空间记忆。
- 在此基础上适配单图像与视频先验，恢复外观并补全连续轨迹，同时保留已观测内容。
- 重建场景支持任意 RGB-D 渲染，并配套自动化整理流程，结合端到端 3D grounding 与基于 VLM 的验证。
- 构建 Holi360 数据集与 Holi360 基准，用于评估 VLM 在真实多房间室内环境中的空间理解。

### 主要贡献
- 提出 Holi-Spatial 360 生成式重建与数据整理框架，面向稀疏全景输入的多房间室内 3D 重建。
- 提出 Correspondence-Guided Geometric Optimization，将前馈重建先验转为跨视角约束，并建立 3D Gaussian Splatting 空间记忆。
- 结合单图与视频先验进行外观恢复与连续轨迹补全，并保留观测内容，支持任意 RGB-D 渲染。
- 构建自动化整理管线，融合端到端 3D grounding 与 VLM 验证。
- 发布 Holi360：超过 1K 多房间 3DGS 场景、超过 100K 实例标注、2M 空间问答对。
- 提出 Holi360 基准，用于评测 VLM 在真实多房间室内环境中的空间理解；实验表明在稀疏全景输入下重建与整理质量更优，且在该数据集上微调 VLM 可显著提升空间推理能力。

### 局限性
- 摘要未提供足够信息（未给出具体失败案例、计算成本、对特定场景类型或传感器条件的依赖、数据偏差与评测覆盖范围等细节）。

### 阅读优先级
高。理由：该工作同时涉及稀疏全景重建、3D Gaussian Splatting、生成式补全、数据整理与 VLM 空间推理评测，并发布了规模较大的数据集与基准（1K+ 场景、100K+ 实例标注、2M 空间问答对），对神经场景表示、3D 空间智能与多模态评测方向均具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires scalable 3D environments that are both photorealistic and semantically grounded, yet existing indoor datasets are dominated by room-scale captures and costly LiDAR acquisition. Online real-estate platforms offer abundant panoramas of diverse multi-room homes, but sparse viewpoints and texture-poor regions make reconstruction severely under-constrained. We introduce Holi-Spatial 360, a generative reconstruction and data curation framework for converting these panoramas into annotated multi-room 3D environments. Because reconstruction quality bounds subsequent generation, our Correspondence-Guided Geometric Optimization converts feed-forward reconstruction priors into reliable cross-view constraints and builds a coherent 3D Gaussian Splatting representation as 3D spatial memory. Adapted single-image and video priors then restore appearance and complete continuous trajectories while preserving observed content. The reconstructed scenes support arbitrary RGB-D rendering and an automated curation pipeline that combines end-to-end 3D grounding with VLM-based verification. Holi360 contains over 1K multi-room 3DGS scenes, more than 100K instance annotations, and 2M spatial question-answer pairs. We also introduce the Holi360 benchmark to evaluate the spatial understanding of VLMs in real-world, multi-room indoor environments. Experiments demonstrate superior reconstruction and curation quality under sparse panoramic inputs, while fine-tuning VLMs on Holi360 substantially improves spatial reasoning capabilities.

</details>

#### 2026-10-13 - DoReMe: Dual optimization of Reconstruction and Motion estimation for self-navigated free-breathing abdominal MRI using Gaussian Splatting

**Authors:** Majd Helo, Dominik Nickel, Thomas Kuestner
**Links:** [abs](https://arxiv.org/abs/2610.19120) - [pdf](https://arxiv.org/pdf/2610.19120)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DoReMe: Dual optimization of Reconstruction and Motion estimation for self-navigated free-breathing abdominal MRI using Gaussian Splatting
- 作者：Majd Helo, Dominik Nickel, Thomas Kuestner
- 出版日期：2026-10-13T19:54:43Z
- 分类：Neural Scene Representations & Rendering（主分类）；次要分类：未提供
- 链接：摘要页 https://arxiv.org/abs/2610.19120 ；PDF https://arxiv.org/pdf/2610.19120

### 一句话总结
该论文提出一种耦合的重建-运动估计算法，用高斯图元表示呼吸运动并在迭代重建中与图像联合优化，在自由呼吸腹部 MRI 的自导航采集上实现了优于压缩感知重建的视觉图像质量。

### 研究问题
自由呼吸腹部 MRI 受呼吸运动限制，会产生图像伪影和 k 空间不一致。现有重建方法通常依赖预先估计的运动场或外部呼吸替代信号。论文关注如何在自导航自由呼吸采集下，不依赖预估计运动场或外部替代信号，实现重建与运动估计的联合优化。

### 核心思路/方法
论文提出一种迭代重建方法，在数据一致性更新与运动建模之间交替进行。呼吸运动使用高斯图元（Gaussian primitives）表示，并将高斯泼溅（Gaussian splatting）集成到重建算法中。方法在四名健康志愿者的自导航自由呼吸笛卡尔梯度回波（GRE）采集上评估，包括回顾性扫描缩短实验，并与正则化压缩感知（CS）重建进行比较。

### 主要贡献
- 提出耦合的重建-运动估计算法，面向自导航自由呼吸采集，运动由紧凑高斯图元表示，并在迭代重建中与图像估计联合细化。
- 将高斯泼溅集成到重建算法中，用于表示非刚性呼吸运动。
- 在四名健康志愿者的自导航自由呼吸 Cartesian GRE 采集上进行了评估，包含回顾性扫描缩短实验，并与正则化压缩感知重建对比。
- 结果显示呼吸运动状态重建约需 1.5 分钟；与 CS 相比，所提方法改善了视觉图像质量，尤其在冠状位肝脏视图，并在回顾性缩短采集下更好地保留解剖结构。
- 结论认为该工作为所提方法提供了概念验证，高斯图元为不可见呼吸运动提供了紧凑且足够灵活的表示，并具有实用运行时间，支持进一步扫描仪集成与更大规模队列验证。

### 局限性
- 摘要未提供足够信息说明样本量以外的更大队列验证结果；仅提到在四名健康志愿者上评估，并指出支持进一步在更大队列中验证。
- 摘要未提供足够信息说明方法的泛化性、对不同病理或不同采集协议的适用性。
- 摘要未提供足够信息说明与 CS 对比之外的定量指标细节、统计显著性或盲评结果。
- 摘要未提供足够信息说明运动估计的准确度定量评估、失败案例或超参数敏感性。
- 摘要未提供足够信息说明临床部署、扫描仪集成或实时性的具体限制；仅提到“支持进一步扫描仪集成和验证”。

### 阅读优先级
中。理由：该工作面向自由呼吸腹部 MRI 的运动伪影问题，提出将高斯泼溅与迭代重建耦合的概念验证方法，并在健康志愿者上显示优于 CS 的视觉质量与回顾性扫描缩短下的结构保留，且报告约 1.5 分钟的运动状态重建时间。对神经场景表示与医学 MRI 重建交叉方向的研究者有参考价值；但摘要仅提供四名健康志愿者的初步结果，尚缺更大队列与定量细节，因此优先级为中而非高。

</details>

<details>
<summary>Abstract</summary>

Purpose: Free-breathing abdominal MRI is limited by respiratory motion, which introduces image artifacts and k-space inconsistencies. Existing reconstruction approaches often depend on pre-estimated motion fields or external respiratory surrogate signals. We propose a coupled reconstruction-motion estimation algorithm for self-navigated free-breathing acquisition, in which motion is represented by compact Gaussian primitives and jointly refined with the image estimates during iterative reconstruction. Methods: An iterative reconstruction that alternates between data consistency updates and motion modelling was proposed. Respiratory motion was represented using Gaussian primitives. A Gaussian splatting was integrated into the reconstruction algorithm. The method was evaluated on self-navigated free-breathing Cartesian gradient-echo (GRE) acquisition in four healthy volunteers, including retrospective scan shortening experiments, and was compared with regularized compressed sensing (CS) reconstruction. Results: Respiratory motion states were reconstructed in approximately 1.5 min. Compared with CS, the proposed method improved visual image quality, particularly in coronal liver views, and better preserved anatomical structures in retrospectively shortened acquisitions. These findings provide proof of concept for the proposed method. Conclusion: The proposed coupled reconstruction-motion estimation algorithm improved visual image quality compared with CS alone. Gaussian primitives provided a compact and sufficiently flexible representation of nonrigid respiratory motion with practical runtime, supporting further scanner integration and validation in larger cohorts.

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-19 - Tactile In-Hand Object Rotation: A Comparative Study of Hand Morphology in Simulation and Hardware

**Authors:** Wenhao He, Max Yang, Chenghua Lu, Yijiong Lin, David A. W. Barton, Nathan F. Lepora
**Links:** [abs](https://arxiv.org/abs/2610.26759) - [pdf](https://arxiv.org/pdf/2610.26759)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tactile In-Hand Object Rotation: A Comparative Study of Hand Morphology in Simulation and Hardware
- 作者：Wenhao He, Max Yang, Chenghua Lu, Yijiong Lin, David A. W. Barton, Nathan F. Lepora
- 出版日期：2026-10-19T17:18:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.26759 ；PDF https://arxiv.org/pdf/2610.26759

### 一句话总结
该论文比较两种低成本 LEAP Hand 手指布局（拟人化与对称式）在配备 TacTip 视触觉传感器、共享强化学习框架下的在手物体连续旋转表现，并结合仿真与硬件实验分析触觉信息、手指参与度和指尖载荷之间的关系。

### 研究问题
论文关注连续在手旋转中接触维持与接触更新如何协调，并探究手部几何结构（手指排布）与触觉反馈分别如何影响操作表现。具体比较拟人化与对称式手指布局在旋转进展、手指参与和指尖载荷上的差异，同时考察不同触觉观测条件对仿真任务表现的影响。

### 核心思路/方法
- 使用两种版本的 LEAP Hand：拟人化手指布局与对称式手指布局。
- 两种手均集成 TacTip 视触觉传感器，并采用共享的强化学习框架。
- 仿真中在 12 个未见物体上评估三种观测条件：完整触觉、二值接触、仅本体感觉。
- 硬件实验中在 10 个物体、多种手部朝向下评估完整触觉策略。
- 分析指标包括旋转进展、手指参与度、指尖载荷与操作持续时间；硬件中还记录接触测量与力数据。

### 主要贡献
- 在仿真中显示，完整触觉观测相比仅本体感觉可提高每回合平均归一化旋转量：拟人化手提高 94.8%，对称手提高 66.9%，同时平均回合持续时间更长、平均总指尖载荷更低。
- 硬件接触测量显示，拟人化手的手指参与更差异化，而对称手各手指的累积载荷分布更均匀。
- 报告对称手取得更高的平均旋转次数（高 32.0%）、更高的总体旋转速率（高 25.8%）以及更长操作持续时间。
- 额外硬件力记录显示，该对称布局的平均总指尖载荷低 19.9%。
- 将手指排布与接触组织、载荷分担联系起来，并表明更丰富的触觉信息在两种仿真本体上均支持更大的任务进展与更低的平均载荷。

### 局限性
- 摘要未提供足够信息说明仿真中不同触觉观测条件在硬件上的对应验证范围；硬件实验主要评估完整触觉策略。
- 摘要未提供足够信息说明 12 个未见物体与 10 个硬件物体的具体类别、形状分布或难度划分。
- 摘要未提供足够信息说明强化学习框架的网络结构、训练细节、奖励设计及统计显著性检验。
- 摘要未提供足够信息说明 TacTip 传感器的具体配置、校准方式及硬件力测量的完整实验协议。
- 摘要未提供足够信息说明不同手部朝向对结果的单独影响，以及仿真与硬件结果差异的系统性原因。

### 阅读优先级
中。理由：该论文涉及触觉感知、手部形态与强化学习在手内旋转中的比较研究，主题对具身操作与触觉机器人研究者有参考价值；摘要给出了明确的定量比较结果，但未提供实验细节与统计信息。若关注低成本触觉手、手指布局设计或仿真到硬件比较，可优先阅读；若仅需一般性了解，摘要已覆盖主要结论。

</details>

<details>
<summary>Abstract</summary>

Continuous in-hand rotation requires coordinated contact maintenance and renewal, linking manipulation performance to both hand geometry and tactile feedback. We investigate these relationships through rotational progress, finger participation, and fingertip loading on two versions of the low-cost LEAP Hand with anthropomorphic and symmetric finger arrangements. Both hands are integrated with TacTip vision-based tactile sensors and use a shared reinforcement learning framework. Simulation evaluates full tactile, binary touch, and proprioception-only observations on 12 unseen objects; hardware experiments evaluate full tactile policies on ten objects under multiple hand orientations. In simulation, full tactile observations increase mean normalized rotation per episode over proprioception alone by 94.8% for the anthropomorphic hand and 66.9% for the symmetric hand, with longer mean episode durations and lower mean total fingertip loads. Hardware contact measurements reveal more differentiated finger participation in the anthropomorphic hand, while cumulative loading is more evenly distributed across the symmetric hand's fingers. Overall, the symmetric hand achieves a 32.0% higher mean rotation count and a 25.8% higher aggregate rotation rate, together with longer manipulation duration. Additional hardware force recordings show a 19.9% lower mean total fingertip load for this layout. These findings relate finger arrangement to contact organization and load sharing, and show that richer tactile information supports greater task progress at lower mean loading in both simulated embodiments.

</details>

#### 2026-10-19 - Robot Learning with Vision-Language-Action Models for Agricultural Manipulation

**Authors:** Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi
**Links:** [abs](https://arxiv.org/abs/2610.26717) - [pdf](https://arxiv.org/pdf/2610.26717)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robot Learning with Vision-Language-Action Models for Agricultural Manipulation
- 作者：Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi
- 出版日期：2026-10-19T16:49:17Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.26717) / [PDF](https://arxiv.org/pdf/2610.26717)

### 一句话总结
该论文构建了一个面向农业到达与抓取任务的仿真到真实机器人学习框架，先在基于 MuJoCo 的农业仿真环境中采集专家演示，并对 Octo 与 π_{0.5} 两个预训练通用机器人策略进行适配，随后在真实 Franka Research 3 机械臂上进一步微调与评估。

### 研究问题
论文关注农业机器人操作中的困难：植物几何结构变化、遮挡以及相机视角变化。预训练视觉-语言-动作（VLA）模型和通用机器人策略有望通过多模态观测与语言指令学习操作行为来应对这些挑战，但将其适配到农业任务需要领域特定演示，而在真实机器人上采集这些演示成本高、耗时长。因此，论文研究如何通过仿真到真实的机器人学习框架，将预训练通用策略适配到农业到达与抓取任务。

### 核心思路/方法
论文提出一个面向农业到达与抓取的仿真到真实机器人学习框架，整合任务特定演示采集与预训练策略适配。具体包括：
- 构建基于 MuJoCo 的农业环境，包含多样化的番茄植株结构，用于支持演示采集与受控评估；
- 通过操纵杆遥操作采集专家演示，并使用低层控制器执行机器人动作；
- 使用仿真演示对两个预训练通用机器人策略 Octo 和 π_{0.5} 进行适配；
- 随后在真实 Franka Research 3 机械臂上使用真实机器人演示进一步微调；
- 在仿真中评估适配策略在分布内、视角/空间偏移和分布外条件下的表现，并进行真实机器人实验；
- 还研究了本体感知信息对策略性能的影响。

### 主要贡献
- 提出了一个用于农业到达与抓取的仿真到真实机器人学习框架，结合任务特定演示采集与预训练策略适配；
- 开发了基于 MuJoCo 的农业环境，包含多样化番茄植株结构，支持演示采集与受控评估；
- 将 Octo 和 π_{0.5} 两个预训练通用机器人策略适配到农业操作任务，并在仿真与真实 Franka Research 3 机械臂上进行评估；
- 比较了两种策略在分布内、视角/空间偏移和分布外条件下的表现，并考察了本体感知信息对策略性能的影响；
- 摘要报告的结果显示，π_{0.5} 的任务性能得分高于 Octo，且在分布偏移下退化更小。

### 局限性
- 摘要仅提到在仿真中评估分布内、视角/空间偏移和分布外条件，并进行了真实机器人实验，但未提供真实机器人实验的具体规模、任务数量或统计细节；
- 摘要未提供演示采集数量、训练时长、硬件配置、评估指标定义等实验细节；
- 摘要未说明该方法在更广泛农业任务、不同作物或更复杂自然环境中的泛化能力；
- 摘要未提供失败案例分析或方法在真实农业场景中部署的限制；
- 摘要未提供足够信息说明仿真环境与真实环境之间的差距及其对结果的具体影响；
- 其他未在摘要中提及的实验细节、消融设置和定量结果：摘要未提供足够信息。

### 阅读优先级
中。理由：该论文聚焦于 VLA/通用机器人策略在农业操作中的仿真到真实适配，问题明确且与农业机器人操作相关；摘要给出了框架、策略比较和主要结果，但未提供详细实验数据与真实部署规模。对于关注机器人学习、VLA 策略适配和农业操作的研究者具有参考价值；若需要具体实验细节或复现信息，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation in agricultural environments remains challenging due to variations in plant geometry, occlusion, and camera viewpoints. Pretrained vision-language-action (VLA) and generalist robot policies offer a promising approach to addressing these challenges by learning manipulation behaviors from multimodal observations and language instructions. However, adapting these policies to agricultural tasks requires domain-specific demonstrations, which are costly and time-consuming to collect on physical robots. In this work, we develop a simulation-to-real robot-learning framework for agricultural reaching and grasping that integrates task-specific demonstration collection and pretrained policy adaptation. A MuJoCo-based agricultural environment is developed with diverse tomato plant structures to support demonstration collection and controlled evaluation. Expert demonstrations are collected through joystick teleoperation, with a low-level controller used to execute robot actions. Two pretrained generalist robot policies, Octo and $π_{0.5}$, are adapted using simulated demonstrations, followed by further fine-tuning on a physical Franka Research 3 manipulator using real-robot demonstrations. The adapted policies are evaluated under in-distribution, viewpoint/spatial-shift, and out-of-distribution conditions in simulation, followed by physical-robot experiments. The influence of proprioceptive information on policy performance is also investigated. Results show that $π_{0.5}$ achieves higher task-performance scores than Octo and exhibits less degradation under distribution shifts. These findings demonstrate the potential of integrating pretrained generalist policies with task-specific demonstration learning for agricultural manipulation.

</details>

#### 2026-10-19 - ForagerSim: Evaluating Embodied Map-Based Reasoning in Large-Scale Dynamic Worlds

**Authors:** Tomáš Musil, Martin Kotík, Michal Vavrečka, Karla Štěpánová, Sebastian Scherer, Martin Saska
**Links:** [abs](https://arxiv.org/abs/2610.26395) - [pdf](https://arxiv.org/pdf/2610.26395)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ForagerSim: Evaluating Embodied Map-Based Reasoning in Large-Scale Dynamic Worlds
- 作者：Tomáš Musil, Martin Kotík, Michal Vavrečka, Karla Štěpánová, Sebastian Scherer, Martin Saska
- 出版日期：2026-10-19T13:40:47Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.26395

### 一句话总结
论文提出 ForagerSim，一个用于评估具身智能体在大规模动态世界中进行“基于地图的推理”的跨学科仿真平台，并通过对比强化学习基线、工程化机器人栈和人类玩家，指出复杂场景中地图式推理可能是性能瓶颈。

### 研究问题
当前具身 AI 系统要么依赖手工设计的建图流程（在未建模动态下易失效且局限于度量空间），要么依赖很少形成地图式表示的学习策略；同时，缺少真正要求“基于地图推理”的具身 AI 基准，导致难以发展能像动物一样灵活构建和使用地图式表示的架构。论文试图提供这样的评估环境。

### 核心思路/方法
ForagerSim 是一个高度模块化的研究平台与仿真环境，聚焦需要地图式推理的具身任务，场景覆盖移动机器人搜救、复杂迷宫与广阔甚至可能无限的开放区域中的动物觅食等。平台允许独立调节多个难度轴：感知（从抽象 2D 感知到完整 RGB 或 LiDAR）、尺度（房间级到多公里级）、拓扑（开放场地到复杂迷宫）、动态（烟雾、碎片、感知运动故障等）以及任务（从简单 2D 覆盖到受觅食启发的井交替任务）。论文在 8 个示例世界上比较了强化学习基线、简单工程化机器人栈和人类玩家，以观察不同难度轴对现有方法的影响。

### 主要贡献
- 提出 ForagerSim：一个面向“基于地图推理”的具身任务仿真平台，具有跨学科定位。
- 提供多维度可独立调节的难度设计，涵盖感知、尺度、拓扑、动态和任务。
- 在 8 个示例世界上对比强化学习基线、工程化机器人栈与人类玩家，分析不同难度轴对方法表现的影响。
- 报告发现：当感知简化为 2D 时，学习策略在简单拓扑中的多目标搜索和井交替任务上表现 surprisingly well，但在更大或拓扑更复杂的环境中低于人类表现，而基于地图的基线表现良好，提示地图式推理是这些场景的瓶颈。

### 局限性
摘要未提供足够信息说明具体实验规模、统计显著性、各难度轴的系统消融细节、工程化机器人栈与人类玩家的具体配置，以及平台在真实机器人上的部署验证情况。摘要也未提供足够信息说明 ForagerSim 的开源许可、计算开销与可复现性细节。

### 阅读优先级
中。理由：该工作与具身 AI、机器人导航和地图式表示学习评估直接相关，且明确指出现有学习策略在复杂拓扑和大尺度场景中的瓶颈，对基准设计有参考价值；但摘要仅给出 8 个示例世界的对比结果，缺少更细的实验与可复现信息，需阅读全文后才能判断其方法深度与结论稳健性。

</details>

<details>
<summary>Abstract</summary>

Animals build cognitive maps of vast environments, use them to perform map-based navigation, and might even be reusing the same circuitry used in spatial reasoning for creating and using maps of arbitrary task-spaces. In contrast, current embodied AI systems either rely on hand-engineered mapping pipelines, which break in the presence of unmodeled dynamics and are restricted to metric space, or on learned policies that rarely form map-like representations at all. Developing architectures that could learn to build and use map-like representations as flexibly as animals is, however, difficult because few embodied AI benchmarks actually require map-based reasoning. To address this, we present ForagerSim --- an interdisciplinary research platform and simulation environment focused on embodied tasks that require map-based reasoning, with scenarios ranging from mobile-robot search and rescue to animal foraging in both complex mazes and vast, potentially infinite open areas. ForagerSim is highly modular and allows modifying independent axes of difficulty related to perception (abstract 2D sensing to full RGB or LiDAR), scale (room-scale to multi-km scale), topology (open-fields to complex mazes), dynamics (smoke, debris, sensorimotor failures and others) and tasks (from simple 2D coverage to foraging-inspired well-alternation tasks). We compare reinforcement learning baselines with a simple engineered robotics stack and a human player on 8 example worlds which show how different difficulty axes affect existing methods. Our results show that, when sensing is simplified to 2D, learned policies can perform multi-object search and well-alternation tasks surprisingly well in simple topologies, but they fall short of human performance in larger or more complex-topology environments where map-based baselines perform well, suggesting that map-based reasoning is the bottleneck in these scenarios.

</details>

#### 2026-10-19 - Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving

**Authors:** Jie Wang, Guang Li, Zhijian Huang, Jinlong Li, Chenxu Dang, Hangjun Ye, Yahong Han, Long Chen
**Links:** [abs](https://arxiv.org/abs/2610.25734) - [pdf](https://arxiv.org/pdf/2610.25734)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving
- 作者：Jie Wang, Guang Li, Zhijian Huang, Jinlong Li, Chenxu Dang, Hangjun Ye, Yahong Han, Long Chen
- 出版日期：2026-10-19T03:37:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25734 ；PDF https://arxiv.org/pdf/2610.25734

### 一句话总结
论文提出“Think Densely, Act Sparsely”的驾驶智能范式及 LECDrive 框架，通过在 VLA 模型内嵌入由任务特定潜在 token 承载的渐进式“潜在专家认知链”，让模型在保持高效推理的同时内化稠密视觉、语义与几何知识。

### 研究问题
现有 Vision-Language-Action（VLA）自动驾驶模型通常以稀疏监督（如语言指令或轨迹信号）训练，而自动驾驶本质上需要稠密理解视觉、语义和几何信息。摘要指出，从稠密视觉观察到稀疏表示的直接映射会迫使模型压缩甚至丢弃对安全驾驶至关重要的场景信息。作者认为该限制并非源于模型容量不足，而是缺乏显式机制来鼓励在潜在空间中形成稠密世界表示。

### 核心思路/方法
论文提出“Think Densely, Act Sparsely”范式，并实例化为 LECDrive 框架。其核心是模仿人类分层感知过程，在 VLA 模型中嵌入一条渐进式的潜在专家认知链。具体而言，方法注入一小组任务特定的潜在 token 作为载体，使模型能够从基础视觉模型内化稠密知识，包括视觉表示（DINOv3）、语义结构（SAM3）和空间几何（DepthAnything3），同时保持高效推理。该相互依赖的认知链遵循课程学习原则，监督信号从表示到语义再到几何逐步结构化。

### 主要贡献
- 提出“Think Densely, Act Sparsely”的驾驶智能范式，主张通过显式机制在潜在空间中构建稠密世界表示，而非仅依赖稀疏监督的直接映射。
- 提出 LECDrive 框架，将渐进式潜在专家认知链嵌入 VLA 模型，并以任务特定潜在 token 作为载体，内化来自 DINOv3、SAM3、DepthAnything3 的视觉、语义和几何知识。
- 设计遵循课程学习原则的监督结构，使认知链从表示到语义再到几何逐步组织，并强调保持高效推理。
- 摘要称大量实验表明 LECDrive 在多个自动驾驶基准上持续提升基础 VLM 的性能，覆盖物体感知、状态预测和轨迹规划等关键任务。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集规模、基线细节和定量结果。
- 摘要未提供足够信息说明潜在 token 的数量选择、课程学习各阶段的具体监督形式及训练成本。
- 摘要未提供足够信息说明“高效推理”的具体效率指标或与其它方法的计算开销对比。
- 摘要未提供足够信息说明方法在不同基础 VLM 或不同驾驶场景下的泛化边界与失败案例。

### 阅读优先级
中。理由：该论文针对 VLA 自动驾驶中“稠密感知与稀疏监督”的矛盾提出明确范式，方法思路清晰，且涉及视觉、语义、几何三类基础模型知识的潜在空间整合，与具身智能/机器人视觉语言动作方向相关。但当前仅依据摘要，缺少实验细节与定量证据，是否值得深入精读需结合全文的实验充分性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Autonomous driving fundamentally demands dense understanding of visual, semantic, and geometric information, yet existing Vision-Language-Action (VLA) models are typically trained with sparse supervision such as language instructions or trajectory signals. This direct mapping from dense visual observations to sparse representations forces the model to compress or even discard critical scene information essential for safe driving. We argue that this limitation does not stem from insufficient model capacity, but from the lack of explicit mechanisms that encourage the formation of dense world representations in the latent space. In this spirit, we propose a novel paradigm for driving intelligence, Think Densely, Act Sparsely, and instantiate it with an efficient and interpretable framework, LECDrive (Latent Expert Cognitive Chains for Vision-Language-Action autonomous Driving). The core idea is to mimic the hierarchical perception process of humans by embedding a progressive chain of latent expert cognition within the VLA model. Concretely, we inject a compact set of task-specific latent tokens as carriers, enabling the model to internalize dense knowledge from foundational vision models, including visual representations (DINOv3), semantic structures (SAM3), and spatial geometry (DepthAnything3), while maintaining efficient inference. This interdependent cognitive chain follows a curriculum learning principle, where supervision is progressively structured from representation to semantics and geometry. Extensive experiments demonstrate that LECDrive consistently improves the performance of base VLMs across multiple autonomous driving benchmarks, covering key tasks such as object perception, state prediction, and trajectory planning. These findings suggest that constructing dense world models through structured latent expert chains is a promising direction for VLA-based autonomous driving.

</details>

#### 2026-10-18 - Preserving the Manifold: Frozen Expert Alignment for Label-Efficient SAR Scene Understanding

**Authors:** Eli A. Underwood, I. Taylor McKechnie, Leslie M. Collins
**Links:** [abs](https://arxiv.org/abs/2610.25429) - [pdf](https://arxiv.org/pdf/2610.25429)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Preserving the Manifold: Frozen Expert Alignment for Label-Efficient SAR Scene Understanding
- 作者：Eli A. Underwood, I. Taylor McKechnie, Leslie M. Collins
- 出版日期：2026-10-18T17:43:57Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次级分类
- 链接：[摘要](https://arxiv.org/abs/2610.25429)｜[PDF](https://arxiv.org/pdf/2610.25429)

### 一句话总结
该论文提出一种“冻结专家”框架：保持 SAR 编码器与 CLIP 文本编码器均冻结，只学习一个轻量、受约束且保持结构的残差桥接模块，以缓解 SAR—文本跨模态对齐中的模态失配与“物理遗忘”，并在标签高效设定下提升零样本 SAR 场景分类表现。

### 研究问题
论文指出 SAR 图像与自然语言跨模态对齐面临两类失败：
1. **模态失配**：在光学图像上预训练的文本编码器（如 CLIP）难以高效迁移到 SAR；主动微波后向散射与被动光学反射在物理上不兼容，且现有 SAR 描述数据集规模比所需小几个数量级，难以在不显著破坏已学语义流形的情况下弥合差距。
2. **物理遗忘**：在大规模自监督目标上预训练的 SAR 编码器编码了雷达物理特性，但在有限描述数据上为文本对齐而微调编码器时，这些特性会被逐步抹除。

### 核心思路/方法
- **单一设计原则**：保持两个编码器冻结，仅学习一个受约束、保持结构的桥接模块。
- **Frozen Expert 框架**：将冻结的 CROMA SAR 编码器与冻结的 CLIP 文本编码器通过轻量级“受约束残差桥”对齐。
- **物理遗忘的形式化**：通过 Procrustes disparity 定义物理遗忘，并报告其桥接方法比微调更好地保持 SAR 几何（disparity：0.210 对 0.351）。
- **泛化验证**：摘要称在多种 SAR 骨干与文本编码器上验证了通用性。

### 主要贡献
- 提出冻结双专家、仅学习受约束残差桥的 SAR—文本对齐框架。
- 用 Procrustes disparity 形式化“物理遗忘”，并给出桥接优于微调的几何保持证据。
- 在零样本 SAR 场景分类上，以最多少 8 倍训练数据超过微调基线：
  - DFC2020：+10.3% R@1，+15.5% mAP
  - EuroSAT-SAR：+15.7% R@1，+12.2% mAP
  - BigEarthNet-MM：+14.7% R@1
- 将“冻结流形对齐”定位为高差异跨模态设定下相对微调的原则性、数据高效替代方案。

### 局限性
- 摘要未提供足够信息说明桥接模块的具体结构、参数量与训练细节。
- 摘要未提供足够信息说明各数据集的划分、训练数据规模绝对值、基线配置与统计显著性。
- 摘要未提供足够信息说明方法在非分类任务（如检索、描述生成、分割）上的表现。
- 摘要未提供足够信息说明失败案例、计算开销或对 SAR 成像条件变化的鲁棒性。
- 摘要未提供足够信息说明“物理遗忘”Procrustes disparity 的完整定义与计算协议。

### 阅读优先级
**中**。理由：论文聚焦 SAR—文本跨模态对齐中的模态失配与物理遗忘，提出冻结双编码器加轻量桥接的数据高效方案，并给出零样本分类的量化提升，问题定义清晰、方法原则简洁；但摘要未展开桥接结构、训练细节与更广泛任务验证，是否适合精读取决于读者对 SAR 跨模态对齐、冻结骨干适配或标签高效场景理解的兴趣。

</details>

<details>
<summary>Abstract</summary>

Cross-modal alignment of synthetic aperture radar (SAR) imagery to natural language is constrained by two distinct failures. The first is modality mismatch: text encoders pre-trained on optical imagery, such as CLIP, cannot be efficiently fine-tuned on SAR, because active microwave backscatter is physically incompatible with passive optical reflectance and the available SAR caption datasets are orders of magnitude too small to bridge this gap without substantially degrading the learned semantic manifold. The second is physical forgetting: SAR encoders pre-trained on large-scale self-supervised objectives encode radar physics that are progressively erased when the encoder is fine-tuned for text alignment on limited caption data. A single design principle addresses both failures: keep both encoders frozen and learn only a constrained, structure-preserving bridge. Our Frozen Expert framework aligns a frozen CROMA SAR encoder with a frozen CLIP text encoder via a lightweight constrained residual bridge. We formally define physical forgetting via Procrustes disparity and show our bridge preserves SAR geometry significantly better than fine-tuning (disparity: 0.210 vs. 0.351). We validate generality across multiple SAR backbones and text encoders. On zero-shot SAR scene classification, our approach outperforms fine-tuned baselines using up to 8x less training data: DFC2020 (+10.3% R@1, +15.5% mAP), EuroSAT-SAR (+15.7% R@1, +12.2% mAP), BigEarthNet-MM (+14.7% R@1). These results establish frozen manifold alignment as a principled, data-efficient alternative to fine-tuning in high-disparity cross-modal settings.

</details>

#### 2026-10-18 - Learning Lane-Structured Conditioning Fields for Online HD Mapping

**Authors:** Andrea Bertogalli, Anthony Dell'Eva, Marcello Ceresini, Federico Pirazzoli, Lorenzo Cipelli, Filippo D'Addeo, Nicola Marinello, Massimo Bertozzi
**Links:** [abs](https://arxiv.org/abs/2610.25284) - [pdf](https://arxiv.org/pdf/2610.25284)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Lane-Structured Conditioning Fields for Online HD Mapping
- 作者：Andrea Bertogalli, Anthony Dell'Eva, Marcello Ceresini, Federico Pirazzoli, Lorenzo Cipelli, Filippo D'Addeo, Nicola Marinello, Massimo Bertozzi
- 出版日期：2026-10-18T14:04:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.25284) / [PDF](https://arxiv.org/pdf/2610.25284)

### 一句话总结
论文提出一种与 BEV 对齐的密集“Lane Field”表示来编码局部车道结构，并基于该表示构建即插即用框架，通过 BEV 特征调制和可变形注意力引导来提升在线高清地图构建。

### 研究问题
在线高清地图构建中，现有方法常依赖外部先验来提升精度与鲁棒性，但先验表示存在权衡：密集栅格易集成却忽略某些地图几何属性；稀疏向量保留几何结构却需要专用编码器、难以接入现有架构。此外，外部先验可能不准确、获取成本高或难以维护。论文希望找到一种既能提供几何引导、又可学习且广泛适用的结构表示。

### 核心思路/方法
论文提出 Lane Field：一种密集的、与 BEV 对齐的几何表示，在每个空间位置编码局部车道结构，并可由车载观测预测，或由外部地图先验构建。在此基础上，作者设计了一个即插即用框架，通过两种互补机制增强在线高清地图构建：
1. BEV 特征调制：将车道结构线索注入潜在 BEV 特征；
2. 可变形注意力引导：将查询采样引导至底层车道几何。

论文主要在 OpenLane-V2 上评估，摘要称该方法能持续改进现有方法，并在车道段感知上达到 state-of-the-art。

### 主要贡献
- 提出 Lane Field，一种密集 BEV 对齐的局部车道结构表示，可由观测预测或由外部地图先验构建。
- 提出基于 Lane Field 的即插即用框架，通过 BEV 特征调制和可变形注意力引导增强在线高清地图构建。
- 在 OpenLane-V2 上评估，摘要报告其方法持续改进现有方法，并在车道段感知上取得 state-of-the-art 性能。

### 局限性
摘要未提供足够信息说明计算开销、实时性、不同数据集上的泛化能力、对不准确外部先验的鲁棒性，以及失败案例或消融实验细节。摘要也未提供足够信息说明该框架在非车道类地图元素上的适用性。

### 阅读优先级
中。理由：该论文关注在线高清地图构建中的先验表示与即插即用增强，问题定义清晰，且摘要声称在 OpenLane-V2 上取得 state-of-the-art；但摘要未提供足够实验细节与局限性信息。是否优先阅读取决于读者对 BEV 表示、车道段感知或可变形注意力引导的兴趣。

</details>

<details>
<summary>Abstract</summary>

High-definition maps provide critical structural information for downstream autonomous driving tasks. Recent methods increasingly rely on external priors to improve prediction accuracy and robustness. Yet, existing prior representations expose a trade-off: dense rasters are easy to integrate but ignore certain map geometric properties, while sparse vectors preserve geometric structure but require dedicated encoders and are difficult to plug into existing architectures. Moreover, external priors can be inaccurate, costly to acquire, or difficult to maintain, motivating a structural representation that can provide geometric guidance while remaining learnable and broadly applicable. We address this limitation with the Lane Field, a dense BEV-aligned geometric representation that encodes local lane structure at each spatial location and can be either predicted from onboard observations or constructed from external map priors. Building on this representation, we introduce a plug-and-play framework that enhances online HD mapping through two complementary mechanisms: BEV feature modulation, which injects lane-structured cues into latent BEV features, and deformable attention guidance, which steers query sampling toward the underlying lane geometry. We primarily evaluate our method on OpenLane-V2, showing that conditioning BEV features and guiding deformable attention with local lane geometry enables our framework to consistently improve existing methods and achieve state-of-the-art performance on lane segment perception. Project page: https://andberto.github.io/LaneField/

</details>

#### 2026-10-15 - GeoState: Learning View-Decoupled Geometry States for 3D World Modeling

**Authors:** Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
**Links:** [abs](https://arxiv.org/abs/2610.22343) - [pdf](https://arxiv.org/pdf/2610.22343)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoState: Learning View-Decoupled Geometry States for 3D World Modeling
- 作者：Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
- 出版日期：2026-10-15T17:56:18Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.22343 ；PDF：https://arxiv.org/pdf/2610.22343 ；项目页：https://hongchang-liu.github.io/GeoState-project-page/

### 一句话总结
GeoState 提出一种视角解耦的几何表示，将场景状态演化与相机相关观测分离，以提升预测式 3D 世界建模的稳定性与跨视角查询一致性。

### 研究问题
现有 3D 世界模型常将几何基础模型（GFM）的特征作为预测用的世界状态，但这些特征具有视角依赖性，会把场景动态与相机引起的变化纠缠在一起，使状态演化更难预测。论文试图解决由此带来的视角依赖与预测困难问题。

### 核心思路/方法
GeoState 将场景状态演化与相机相关观测分离。具体而言，一个场景 tokenizer 将多视角 GFM 特征聚合为视角解耦的场景状态；一个几何解码器使用相机射线对该状态进行查询；随后，一个自回归世界模型预测未来场景状态，而相机运动被单独建模。预测出的状态可以在预测相机或外部指定相机下解码，并在整个 rollout 中保持来自单一上下文的尺度，无需逐帧尺度对齐。

### 主要贡献
- 提出 GeoState，一种用于预测式 3D 世界建模的视角解耦几何表示，将场景状态演化与相机相关观测分离。
- 设计场景 tokenizer 聚合多视角 GFM 特征为视角解耦场景状态，并用相机射线通过几何解码器查询。
- 采用自回归世界模型预测未来场景状态，同时单独建模相机运动。
- 支持在预测或外部指定相机下解码预测状态，并在 rollout 中保持单一上下文尺度，无需逐帧尺度对齐。
- 实验表明 GeoState 在 Waymo 上优于先前 3D 世界模型，支持几何一致的跨视角查询，并零样本泛化到 KITTI 和 nuScenes。

### 局限性
摘要未提供足够信息。摘要未提供关于失败案例、计算开销、具体限制条件或方法适用范围之外不足的详细信息。

### 阅读优先级
高。理由：该论文针对 3D 世界模型中视角依赖导致状态预测困难的关键问题，提出明确的解耦建模思路，并在 Waymo 上报告优于先前方法、支持跨视角查询且零样本泛化到 KITTI 和 nuScenes；若关注 3D 世界模型、具身智能或自动驾驶场景建模，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent 3D world models increasingly use features from geometry foundation models (GFMs) as predictive world states, benefiting from their rich geometric priors. However, the view dependence of these features entangles scene dynamics with camera-induced variation, making the resulting state evolution harder to predict. We propose GeoState, a view-decoupled geometry representation for predictive 3D world modeling that separates scene-state evolution from camera-dependent observation. Specifically, a scene tokenizer aggregates multi-view GFM features into a view-decoupled scene state, which a geometry decoder queries using camera rays. An autoregressive world model then predicts future scene states, while camera motion is modeled separately. The predicted states can therefore be decoded under either predicted or externally specified cameras, while retaining a single context-derived scale throughout the rollout without per-frame scale alignment. Experiments show that GeoState outperforms prior 3D world models on Waymo, supports geometrically consistent cross-view querying, and generalizes zero-shot to KITTI and nuScenes. Project page: https://hongchang-liu.github.io/GeoState-project-page/

</details>

#### 2026-10-15 - Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

**Authors:** Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye, Chenze Yu, Wenxuan Zhu, Eric J. Chen, Yan Qin, Yue Chen, Tongyu Wu, Junhao Gong, Kai-Chong Lei, Jiahao Zhang, Kailun Su, Qiwei Liang, Renjing Xu, Ping Luo, Wenbo Ding
**Links:** [abs](https://arxiv.org/abs/2610.22342) - [pdf](https://arxiv.org/pdf/2610.22342)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation
- 作者：Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye, Chenze Yu, Wenxuan Zhu, Eric J. Chen, Yan Qin, Yue Chen, Tongyu Wu, Junhao Gong, Kai-Chong Lei, Jiahao Zhang, Kailun Su, Qiwei Liang, Renjing Xu, Ping Luo, Wenbo Ding
- 出版日期：2026-10-15T17:56:17Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接 https://arxiv.org/abs/2610.22342 ；PDF 链接 https://arxiv.org/pdf/2610.22342 ；项目网站 https://xsparkai.com/Spark-0

### 一句话总结
Spark-0 提出一种空间对齐的视觉-触觉-语言-动作（VTLA）模型，将触觉既作为预训练监督信号又作为策略输入，用于提升机器人在接触密集的灵巧操作任务中的表现。

### 研究问题
通用机器人策略从大规模视觉预训练中获益，但在接触密集的灵巧操作中往往表现不佳，因为力、柔顺性和早期滑动难以仅从图像中观测。论文关注的核心问题是：如何利用触觉信息，既改善视觉运动预训练，又作为部署时的策略条件，从而提升灵巧操作能力。

### 核心思路/方法
Spark-0 以两种互补方式使用触觉：
1. **预训练阶段**：由触觉手套导出的图像空间接触图（image-space contact maps）与冻结的 3D 几何教师（frozen 3D geometry teacher）特征共同监督视觉 token；这些监督目标在推理阶段被移除。
2. **并行触觉通路**：编码区域力历史（regional force histories）与 3D taxel 状态，用于条件化动作专家（action expert）。
因此，单个检查点（single checkpoint）可同时支持纯视觉部署和触觉条件化部署。

为扩展这种监督，论文构建了 **HumanTouch**：一个 1,000 小时的全手触觉人类操作数据集，并将 Spark-0 与自我中心视频、机器人数据、仿真数据一起预训练。论文还发布了 **SparkArena**，在同一灵巧本体（one dexterous embodiment）上配对纯视觉仿真任务与触觉条件化真实机器人任务。

### 主要贡献
- 提出 Spark-0，一种空间对齐的 VTLA 模型，将触觉同时用作可扩展的预训练监督信号和部署时的策略输入。
- 构建 HumanTouch，1,000 小时全手触觉人类操作数据集，用于规模化触觉预训练。
- 发布 SparkArena，在同一灵巧本体上配对纯视觉仿真任务与触觉条件化真实机器人任务。
- 实验结果表明：Spark-0 在 SparkArena 两个赛道上均取得最高平均成功率，并在 Ego Humanoid Manipulation Benchmark 的全部八项聚合指标上排名第一。
- 关键对比：在相同数据与计算量下，相比丢弃触觉的纯视觉预训练，保留 1,000 小时 HumanTouch 触觉使 Ego Humanoid 上的纯视觉成功率从 52.5% 提升至 71.7%，使 SparkArena-Real（部署时也使用触觉）成功率从 44.0% 提升至 52.0%，说明触觉不仅是策略输入，也是灵巧视觉运动预训练的可扩展监督。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败案例、计算成本细节、触觉硬件泛化性、仿真到真实迁移的具体限制，也未提供与更多基线方法的全面对比或消融实验细节。

### 阅读优先级
**高**。理由：该工作同时涉及触觉预训练规模化、VTLA 模型、大规模数据集（1,000 小时 HumanTouch）与基准（SparkArena），并给出触觉监督显著提升视觉运动预训练效果的定量证据，对灵巧操作、多模态机器人策略和触觉学习方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, image-space contact maps derived from tactile gloves, together with features from a frozen 3D geometry teacher, supervise the visual tokens; these objectives are removed at inference. In parallel, a tactile pathway encodes regional force histories and 3D taxel states to condition the action expert. A single checkpoint therefore supports both vision-only and tactile-conditioned deployment. To scale this supervision, we build HumanTouch, a 1,000-hour dataset of full-hand tactile human manipulation, and pretrain Spark-0 on it together with egocentric video, robot data, and simulation. We also release SparkArena, which pairs vision-only simulated tasks with tactile-conditioned real-robot tasks on one dexterous embodiment. Spark-0 achieves the highest mean success rate on both SparkArena tracks and ranks first on all eight aggregate metrics of the Ego Humanoid Manipulation Benchmark. Compared with vision-only pretraining on the same data and compute with touch discarded, retaining the touch of 1,000 hours of HumanTouch raises vision-only success on Ego Humanoid from 52.5% to 71.7%, and success on SparkArena-Real, where touch is also used at deployment, from 44.0% to 52.0%, indicating that touch serves not only as a policy input but also as scalable supervision for dexterous visuomotor pretraining. The Website is available at: https://xsparkai.com/Spark-0.

</details>

#### 2026-10-15 - VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models

**Authors:** Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen, Zhe Liu, Hengshuang Zhao
**Links:** [abs](https://arxiv.org/abs/2610.21985) - [pdf](https://arxiv.org/pdf/2610.21985)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models
- 作者：Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen, Zhe Liu, Hengshuang Zhao
- 出版日期：2026-10-15T14:34:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.21985

### 一句话总结
针对基于流的 VLA 策略在测试时只执行单一噪声样本、缺乏质量评估的问题，提出一种免训练的两轴触发机制，并在触发时用基于 JEPA 的潜在世界模型对候选动作块进行排序，在真实与仿真任务中提升完成度与成功率。

### 研究问题
基于流的 Vision-Language-Action（VLA）策略本质上是随机的：同一观测下，不同噪声种子会生成质量不一的动作块。但测试时策略通常只提交单一采样，且没有对其质量的显式估计。在细粒度操作任务中，执行次优动作可能不可逆地破坏任务进程并导致失败。因此需要解决：如何在测试时利用策略的随机性，检测关键状态并选择更优的动作块。

### 核心思路/方法
- 引入一个免训练的两轴触发机制，使用两个初始样本，分别测量块内时间变化与跨样本方差，用以检测关键状态。
- 一旦触发，使用基于 JEPA 的潜在世界模型对候选动作块进行排序。
- 排序依据是预测动作条件下的未来潜在状态以及相应的任务进展变化。
- 由于在潜在空间中操作，验证器避免了像素重建，从而实现高效且更准确的排序。

### 主要贡献
- 提出免训练的两轴触发机制，利用两个初始样本的块内时间变化与跨样本方差检测关键状态。
- 提出基于 JEPA 的潜在世界模型验证器，在潜在空间中对候选动作块按预测的未来潜在状态与任务进展变化排序，避免像素重建。
- 在三个真实任务（钢笔插入、移液、苹果放置）上，将平均完成分数从 50.8% 提升至 65.5%，在单张 RTX 4090 上每个触发决策增加 326 ms 的采样与验证时间。
- 在仿真中取得一致增益：RoboTwin 2.0 干净设置下平均成功率从 66.4% 升至 73.6%，随机化设置下从 62.8% 升至 69.6%，LIBERO 上从 96.9% 升至 97.6%。

### 局限性
摘要未提供足够信息。摘要未说明方法在未触发状态下的表现、触发机制的误判率、不同任务对 326 ms 额外延迟的容忍度、候选动作块数量与验证开销的关系，也未提供失败案例或与其他验证方法的对比。真实任务仅列出三个，泛化性边界未在摘要中说明。

### 阅读优先级
高。理由：该工作针对基于流的 VLA 测试时随机性与次优动作执行的现实问题，提出免训练触发与潜在世界模型验证的组合方案，并在真实任务与多个仿真基准上报告了明确提升；若关注机器人操作策略的测试时验证与潜在世界模型应用，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation. At test time, however, the policy typically commits to a single sample without an explicit estimate of its quality. In fine-grained manipulation, executing a suboptimal action can irreversibly disrupt task progress and lead to failure. To exploit policy stochasticity, we introduce a training-free two-axis trigger that uses two initial samples to measure within-chunk temporal variation and cross-sample variance, detecting the critical states. Once triggered, a JEPA-based latent world model ranks candidate action chunks by predicting action-conditioned future latent states and the corresponding changes in task progress. By operating in latent space, the verifier avoids pixel reconstruction and enables efficient and more accurate ranking. Across three real-world tasks, $\textit{i.e.,}$ pen insertion, pipetting, and apple placement), our method raises the average completion score from 50.8% to 65.5%, while adding 326 ms for sampling and verification per triggered decision on a single RTX 4090. Consistent gains are also observed in simulation, where the average success rate rises from 66.4% to 73.6% in the clean setting of RoboTwin 2.0, from 62.8% to 69.6% in its randomized setting, and from 96.9% to 97.6% on LIBERO.

</details>

#### 2026-10-15 - Anvil: Scaling Embodied Spatial Intelligence through Knowledge Recirculation

**Authors:** Weilin Ruan, Bohan Zhou, Jinghao Li, Yangkai Wei, Wenqian Li, Peiran Dong, Yingjie Xu, Leyi Wu, Haojian Huang, Binghui Xie, Han Yang, Kaiwen Zhou, Yinchuan Li, Ying-Cong Chen, James Cheng
**Links:** [abs](https://arxiv.org/abs/2610.21882) - [pdf](https://arxiv.org/pdf/2610.21882)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Anvil: Scaling Embodied Spatial Intelligence through Knowledge Recirculation
- 作者：Weilin Ruan, Bohan Zhou, Jinghao Li, Yangkai Wei, Wenqian Li, Peiran Dong, Yingjie Xu, Leyi Wu, Haojian Huang, Binghui Xie, Han Yang, Kaiwen Zhou, Yinchuan Li, Ying-Cong Chen, James Cheng
- 出版日期：2026-10-15T13:47:08Z
- 分类：Embodied / Robotics / AR Applications（二级分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2610.21882 ；PDF https://arxiv.org/pdf/2610.21882

### 一句话总结
论文提出 Anvil 统一框架，通过数据生成、训练与评测三个组件，将具身空间智能中的异构空间知识进行循环整合，并以 9B 学生模型 Anvil-MOPD 在七个公开基准上取得相对基线约 9–11 个百分点的平均提升。

### 研究问题
具身空间智能要求模型不仅做视觉识别，还需定位实体、推理实体间关系，并以动作相关形式表达这些知识。然而不同阶段所需的监督信号分散在互不兼容的几何与语义输出形式中，联合训练会将这些阶段所需知识混为一谈。论文关注的问题是：如何在数据生成、训练与评测层面统一处理这种异构性，使模型能够学习多样化的具身空间能力，并区分阶段能力不足与错误传播。

### 核心思路/方法
论文提出 Anvil 统一框架，包含三个部分：
1. Anvil-Gen：异构数据飞轮，结合形式特定生成、跨阶段一致性校验和失败驱动的回采，覆盖 11 种 Ground–Relation–Act 形式。
2. Anvil-Ben：提供场景对齐的监督，用于学习多样的具身空间能力；并提供场景关联的评测，以区分阶段能力与错误传播。
3. Anvil-MOPD：一个 9B 学生模型，通过从专家教师蒸馏来整合异构空间知识；其中“语义优先故障路由”将教师监督对准学生最早的决定性失败，“阶段归一化”用于控制不同长度原生输出的损失尺度。

数据方面，论文构建了 5.8M 条基于来源的记录，覆盖 160K 张图像，其中 580K 条空间记录留作留出评测，其余 5.22M 条用于训练。

### 主要贡献
- 提出 Anvil 统一框架，覆盖具身空间智能的数据生成、训练与评测。
- 提出 Anvil-Gen 异构数据飞轮，覆盖 11 种 Ground–Relation–Act 形式，并包含跨阶段一致性验证与失败驱动回采。
- 提出 Anvil-Ben，用于场景对齐监督与区分阶段能力和错误传播的评测。
- 提出 Anvil-MOPD 9B 学生模型，结合语义优先故障路由与阶段归一化，从专家教师蒸馏异构空间知识。
- 构建 5.8M 条来源可溯记录（160K 图像），并划分 580K 留出评测与 5.22M 训练记录。
- 在七个公开基准上，Anvil-MOPD 平均分别超过 Qwen3.5-9B 和 RynnBrain-8B 9.29 与 11.03 个百分点，并在 VABench-Point 上达到 80.67%。
- 通过受控研究支持“定向覆盖”“选择性迁移”“反馈引导修复”作为互补框架组件。

### 局限性
- 论文的具体实验设置、基线配置、消融细节、数据构建流程细节、教师模型构成、训练成本、推理开销等，摘要未提供足够信息。
- 七个公开基准的具体名称与逐项结果，除 VABench-Point 的 80.67% 外，摘要未提供足够信息。
- “定向覆盖”“选择性迁移”“反馈引导修复”的受控研究具体设计与量化结论，摘要未提供足够信息。
- 框架在真实机器人或 AR 场景中的部署验证、泛化边界与失败案例分析，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文面向具身空间智能这一核心方向，同时提出数据生成、训练方法和评测基准三方面统一框架，并给出 9B 模型在七个公开基准上的平均提升与具体指标。对关注具身空间推理、多阶段监督异构性、知识蒸馏与数据飞轮的研究者具有较高参考价值。但需注意，摘要未提供实验细节与局限性讨论，深入评估需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Embodied spatial intelligence requires more than visual recognition: models must localize entities, reason about their relations, and express this knowledge in action-relevant forms. Yet joint training can conflate the knowledge needed at different stages because supervision is fragmented across incompatible geometric and semantic outputs. We introduce Anvil, a unified framework for data generation, training, and benchmarking for embodied spatial intelligence. (1) Anvil-Gen is a heterogeneous data flywheel that combines form-specific generation, cross-stage consistency verification, and failure-driven recollection across 11 Ground--Relation--Act forms. (2) Anvil-Ben provides scene-aligned supervision for learning diverse embodied spatial capabilities and scene-linked assessments that distinguish stage competence from error propagation. (3) Anvil-MOPD is a 9B student that consolidates heterogeneous spatial knowledge through distillation from specialist teachers. Semantic-first-fault routing targets teacher supervision to the student's earliest decisive failure, while stage normalization controls the loss scale across native outputs of different lengths. We construct 5.8M source-grounded records spanning 160K images, reserving 580K spatial records for held-out evaluation and using the remaining 5.22M records for training. On average across seven public benchmarks, Anvil-MOPD outperforms Qwen3.5-9B and RynnBrain-8B by 9.29 and 11.03 percentage points, respectively, while reaching 80.67% on VABench-Point. Controlled studies support targeted coverage, selective transfer, and feedback-guided repair as complementary framework components.

</details>

#### 2026-10-15 - CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation

**Authors:** Yanchen Ding, Jiayi Chen, Jianfeng Xu, Wei Zhao, Li Yi, He Wang
**Links:** [abs](https://arxiv.org/abs/2610.21349) - [pdf](https://arxiv.org/pdf/2610.21349)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation
- 作者：Yanchen Ding, Jiayi Chen, Jianfeng Xu, Wei Zhao, Li Yi, He Wang
- 出版日期：2026-10-15T06:30:20Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.21349) / [PDF](https://arxiv.org/pdf/2610.21349)

### 一句话总结
论文提出 CQDC-Warp，一个面向批量模型预测控制的 GPU 加速可微准动态仿真器，用于研究接触引导的轨迹优化，并在多项接触丰富操作任务上报告了成功率和速度优势。

### 研究问题
论文关注接触丰富操作轨迹的高效合成问题。摘要指出，基于梯度的规划是有前景的方向，但联合优化运动与接触决策仍然困难；同时，许多现有规划器运行在 CPU 上，吞吐量有限。

### 核心思路/方法
论文提出 CQDC-Warp，一个用于批量模型预测控制的 GPU 加速可微准动态仿真器。其核心设定是接触引导的轨迹优化：在规划前指定期望的机器人与物体接触，并通过软代价鼓励这些接触；接触几何与摩擦响应由仿真动力学决定，而不依赖预先规定的接触模式调度。

### 主要贡献
- 提出 CQDC-Warp：面向批量 MPC 的 GPU 加速可微准动态仿真器。
- 将其用于接触引导的轨迹优化：接触意图预先指定并由软代价鼓励，接触几何和摩擦响应由仿真动力学决定，无需预设接触模式调度。
- 在 17 物体 Allegro 手内旋转基准上进行 17,408 次试验，报告成功率为 79.8%，高于 CFree 的 73.7% 和 IMPACT 的 65.2%；平均轨迹生成时间分别缩短为后两者的 1/27.0 和 1/50.2。
- 在单张 NVIDIA RTX 4090 上使用 2,048 个并行世界，前向与反向吞吐分别达到 2.06×10^5 和 2.25×10^5 world-steps per second。
- 进一步实验涵盖 LEAP 和 Shadow 手操作、环境接触利用、双臂操作、全身控制，以及在 Sharpa 手上的真实世界轨迹回放。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、泛化边界、仿真到现实差距的定量评估、消融实验细节、计算资源之外的扩展性限制，以及真实世界回放的成功率或误差指标。摘要仅报告了部分基准结果和任务覆盖范围，未提供完整局限性讨论。

### 阅读优先级
高。理由：该工作直接针对接触丰富操作中运动与接触联合优化的难题，并同时报告了基准成功率、相对基线提升、GPU 吞吐和多种任务扩展；对机器人学习、接触规划、可微仿真和批量 MPC 方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Efficient synthesis of contact-rich manipulation trajectories is essential for downstream robot learning. Gradient-based planning offers a promising approach, but jointly optimizing motion and contact decisions remains challenging. Meanwhile, many existing planners run on CPUs with limited throughput. We present CQDC-Warp, a GPU-accelerated differentiable quasi-dynamic simulator for batched model predictive control (MPC). We use it to study contact-guided trajectory optimization, in which intended robot--object contacts are specified before planning and encouraged through soft costs, while the simulated dynamics determine contact geometry and frictional response without a prescribed contact-mode schedule. Across $17{,}408$ trials on the $17$-object Allegro in-hand rotation benchmark, our framework achieves $79.8\%$ success, compared with $73.7\%$ for CFree and $65.2\%$ for IMPACT, and reduces mean trajectory-generation time by factors of $27.0$ and $50.2$, respectively. On a single NVIDIA RTX 4090 with $2{,}048$ parallel worlds, forward and backward throughput reach $2.06\times10^5$ and $2.25\times10^5$ world-steps per second, respectively. Further experiments cover manipulation with LEAP and Shadow hands, environmental contact exploitation, bimanual manipulation, whole-body control, and real-world trajectory replay on a Sharpa hand.

</details>

#### 2026-10-14 - EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos

**Authors:** Meng Cao, Can Zhao, Jinjie Wei, Haonan Zhao, Yulong Zhang, Duo Han, Xiaofan Li, Ziwu Song, Rongtao Xu, Ruyi Gan, Hao Wang, Qian Wang, Daolin Ma, Ian Reid, Xiaodan Liang
**Links:** [abs](https://arxiv.org/abs/2610.20904) - [pdf](https://arxiv.org/pdf/2610.20904)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos
- 作者：Meng Cao, Can Zhao, Jinjie Wei, Haonan Zhao, Yulong Zhang, Duo Han, Xiaofan Li, Ziwu Song, Rongtao Xu, Ruyi Gan, Hao Wang, Qian Wang, Daolin Ma, Ian Reid, Xiaodan Liang
- 出版日期：2026-10-14T20:34:18Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.20904 ；PDF：https://arxiv.org/pdf/2610.20904

### 一句话总结
EgoJEPA 提出一个三阶段框架，试图绕开基于规则的人到机器人重定向，从第一视角人类视频中学习与具体机器人本体无关的表征，用于灵巧操作。

### 研究问题
第一视角人类视频可为机器人演示提供可扩展替代方案，但如何把其中的操作先验迁移到机器人控制仍是挑战。常见做法是基于重定向：通过手工设计的几何映射，将人类手腕和手指姿态转换为特定本体的动作命令。摘要指出这种映射存在两个问题：一是跨不同本体时需要细致重新校准；二是可能把手势跟踪误差传播到下游机器人控制流程中。

### 核心思路/方法
论文提出 EgoJEPA，一个三阶段框架，目标是在不依赖基于规则的人到机器人重定向的情况下，从第一视角人类视频中学习本体无关表征：

1. 人类动作预训练：通过 JEPA 风格的视觉预测，并以手部运动差异为条件，学习具有效果感知的潜在动作。
2. 基于潜在动作的世界建模：联合预测未来视觉动态和潜在动作，从而将人类先验预训练与机器人特定的控制参数化解耦。
3. 本体特定调优：通过轻量级动作适配器，将预训练模型适配到不同机器人。

### 主要贡献
- 提出 EgoJEPA 三阶段框架，用于从第一视角人类视频学习本体无关表征，避免基于规则的人到机器人重定向。
- 将人类动作预训练、潜在动作世界建模与本体特定调优结合，以解耦人类先验预训练和机器人特定控制参数化。
- 摘要报告在三个机器人本体、五个真实世界操作任务上验证了有效性和效率：域外评估平均成功率为 74%，重定向基线为 65%；跨本体累计挂钟成本降低 47.2%，从 743.2 小时降至 392.7 小时。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、适用边界、任务难度分布、机器人本体类型、是否存在仿真到现实差距、对外观或视角变化的鲁棒性、以及轻量级动作适配器的具体结构与训练成本。摘要未提供足够信息说明其与更多基线或更广泛任务集的比较结果。摘要未提供足够信息说明手部跟踪质量对方法的影响。摘要未提供足够信息说明其方法在非第一视角视频或非灵巧操作任务上的泛化能力。

### 阅读优先级
高。理由：该论文直接针对第一视角人类视频到机器人灵巧操作迁移中的重定向瓶颈，提出替代性表征学习框架，并在摘要中给出跨三个机器人本体、五个真实任务的量化结果与成本对比；若关注机器人学习、第一视角视频利用、跨本体迁移或 JEPA 类方法在具身控制中的应用，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Egocentric human videos offer a scalable alternative to costly robot demonstra- tions, yet transferring their manipulation priors to robot control remains chal- lenging. The commonly adopted retargeting-based approaches convert human wrist and finger poses into embodiment-specific action commands through hand- crafted geometric mappings. However, such mappings require meticulous recal- ibration across different embodiments and risk propagating hand-tracking errors into downstream robot control pipelines. To this end, we propose EgoJEPA, a three-stage framework that learns embodiment-agnostic representations from ego- centric human videos without rule-based human-to-robot retargeting: 1) Human- action pre-training learns effect-aware latent actions through JEPA-style visual prediction conditioned on hand-motion differences; 2) Latent-action-based world modeling jointly predicts future visual dynamics and latent actions, which decou- ples human prior pre-training from robot-specific control parameterizations; 3) Embodiment-specific tuning adapts the pretrained model to diverse robots through lightweight action adapters. Experiments on five real-world manipulation tasks across three robot embodiments demonstrate the effectiveness and efficiency of EgoJEPA. It achieves a 74% average success rate under the out-of-domain evalu- ation, compared with 65% for the retargeting baseline, while reducing cumulative cross-embodiment wall-clock cost by 47.2%, from 743.2 to 392.7 hours.

</details>

#### 2026-10-14 - BubbleCBF: Constructive Safety for Second-Order Systems and Application to Autonomous Robot Navigation in Unknown Environments

**Authors:** Mani Amani, Mohammed Alyaseen, Zhirui Dai, Ki Myung Brian Lee, Nikolay Atanasov, Jorge Cortes
**Links:** [abs](https://arxiv.org/abs/2610.20895) - [pdf](https://arxiv.org/pdf/2610.20895)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BubbleCBF: Constructive Safety for Second-Order Systems and Application to Autonomous Robot Navigation in Unknown Environments
- 作者：Mani Amani, Mohammed Alyaseen, Zhirui Dai, Ki Myung Brian Lee, Nikolay Atanasov, Jorge Cortes
- 出版日期：2026-10-14T20:24:47Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.20895

### 一句话总结
该论文提出 BubbleCBF，一种针对二阶控制仿射系统的构造性安全约束设计方法，通过从有符号距离函数（SDF）构造位置空间中的无碰撞球（bubble），并利用其二次几何与重叠关系构建速度相关安全约束，以二次规划安全滤波器实现，并应用于差分驱动机器人在未知环境中的自主导航。

### 研究问题
二阶动力学系统的安全约束满足具有挑战性，因为位置约束可能要求不可行的减速度。高阶控制屏障函数（CBF）可用于表达此类系统的安全条件，但其可行性依赖于系统动力学和可用控制权限。论文旨在为二阶控制仿射系统构造可行的安全约束。

### 核心思路/方法
- 从有符号距离函数（SDF）出发，在位置空间中构造无碰撞球（bubble）。
- 利用这些球的二次几何及重叠关系，构造速度相关的安全约束。
- 将相关安全集表示为若干交集组成的并集，并通过二次规划安全滤波器进行约束执行。
- 在关于动力学、球重叠和设计参数的温和假设下，证明基于二次规划的控制器是良定义的、关于系统状态连续，并使该集合前向不变。
- 推导有界输入下的可行性充分条件。
- 将 BubbleCBF 应用于差分驱动机器人，展示在未知环境中的安全自主导航。

### 主要贡献
- 提出面向二阶控制仿射系统的构造性可行安全约束设计方法。
- 基于 SDF 构造位置空间中的无碰撞球，并利用其二次几何与重叠建立速度相关安全约束。
- 将安全集表示为交集之并，并通过二次规划安全滤波器实现。
- 在温和假设下证明控制器的良定义性、状态连续性和集合前向不变性。
- 推导有界输入下的可行性充分条件。
- 在差分驱动机器人上验证 BubbleCBF 用于未知环境安全自主导航。

### 局限性
摘要未提供足够信息。摘要未说明实验规模、环境复杂度、与基线方法的定量对比、计算开销、假设在实际系统中的满足程度，以及除差分驱动机器人外的泛化验证情况。

### 阅读优先级
高。理由：该论文聚焦二阶系统安全约束的可行构造与理论保证，并直接应用于未知环境下的机器人导航，主题明确且兼具理论证明与机器人验证；但具体实验细节和对比结果需查阅原文，摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Satisfying safety constraints for systems with second-order dynamics is challenging because a position constraint may require infeasible deceleration. Higher-order control barrier functions (CBFs) provide an approach for expressing safety conditions for such systems but feasibility depends on the system dynamics and available control authority. We develop a constructive approach for designing feasible safety constraints for second-order control-affine systems. Starting from a signed distance function (SDF), we construct collision-free spheres, i.e., bubbles, in position space, and use their quadratic geometry and overlap to construct a velocity-dependent safety constraint. The associated safe set is represented as a union of intersections and enforced through a quadratic-program safety filter. Under mild assumptions on the dynamics, bubble overlap, and design parameters, we prove that the quadratic-program-based controller is well defined, continuous in the system state, and renders the set forward invariant. We also derive sufficient conditions for feasibility under bounded inputs. We demonstrate that our BubbleCBF, applied to a differential-drive robot, achieves safe autonomous navigation in unknown environments. Videos and results are available at: https://existentialrobotics.org/bubblecbf/.

</details>

#### 2026-10-14 - GeoThinker-$F$: Endogenous Predictive World Representations for Fast Spatial Intelligence

**Authors:** Haoyuan Li, Qihang Cao, Huanyuan Zhou, Xin Hu, Sijia Chen, Zihan Guo, Kun Xiang, Yunshuang Nie, Tao Tang, Xinlong Zheng, Jia-Wang Bian, Xianming Liu, Xiaodan Liang
**Links:** [abs](https://arxiv.org/abs/2610.20592) - [pdf](https://arxiv.org/pdf/2610.20592)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoThinker-$F$: Endogenous Predictive World Representations for Fast Spatial Intelligence
- 作者：Haoyuan Li, Qihang Cao, Huanyuan Zhou, Xin Hu, Sijia Chen, Zihan Guo, Kun Xiang, Yunshuang Nie, Tao Tang, Xinlong Zheng, Jia-Wang Bian, Xianming Liu, Xiaodan Liang
- 出版日期：2026-10-14T17:59:03Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.20592 ；PDF: https://arxiv.org/pdf/2610.20592

### 一句话总结
GeoThinker-$F$ 通过将因果 MLLM 隐状态转化为预测性潜在世界表示，在移除推理阶段外部 3D 几何编码器依赖的同时，保持有竞争力的空间智能表现并显著加速推理。

### 研究问题
现有几何感知多模态大语言模型（MLLMs） increasingly 依赖外部 3D 编码器提供结构先验，但在推理时执行这些额外编码器路径会带来显著的延迟和计算开销。论文关注的问题是：能否在不依赖外部 3D 编码器的情况下，让 MLLM 自身内化时空感知能力，从而兼顾空间智能性能与推理效率。

### 核心思路/方法
论文提出 GeoThinker-$F$，核心洞察是中间语义表示已包含足够信息来预测当前几何的有用表示和未来语义表示，而不需要精确复现专用 3D 编码器的特征。方法采用解耦的两阶段训练策略：
- 第一阶段：冻结 MLLM 主干，轻量级 Latent Frame Prediction (LFP) 头从离线 3D 几何专家和下一帧语义目标中学习。
- 第二阶段：移除外部专家，通过专门的 Spatial-Grounded Temporal (SGT) Fusion 模块，联合优化模型以生成并选择性整合其自预测先验。

### 主要贡献
- 提出 GeoThinker-$F$ 框架，通过将因果 MLLM 隐状态转化为预测性潜在世界表示，内化时空感知。
- 采用解耦两阶段训练策略，先由 LFP 头学习离线 3D 几何专家与下一帧语义目标，再移除外部专家并通过 SGT Fusion 模块联合优化自预测先验的生成与选择性整合。
- 实验评估显示，GeoThinker-$F$ 消除了运行时对外部 3D 几何编码器的依赖，同时在多样空间智能基准上保持有竞争力的性能。
- 实现最高 $3.6\times$ 推理加速，将延迟从 $1.45\,\mathrm{s}$ 降至 $0.40\,\mathrm{s}$，并保留较强的空间推理性能。

### 局限性
摘要未提供足够信息。摘要未说明具体基准名称、数据集规模、失败案例、方法在哪些场景下可能退化、训练成本细节、LFP 头与 SGT Fusion 模块的具体结构，以及与其他方法逐项对比的完整结果。

### 阅读优先级
高。理由：该论文针对几何感知 MLLM 推理效率这一明确痛点，提出去除外部 3D 编码器依赖的内生预测表示方案，并报告了最高 $3.6\times$ 推理加速与延迟从 $1.45\,\mathrm{s}$ 降至 $0.40\,\mathrm{s}$ 的量化结果；若关注具身智能、机器人、AR 中的实时空间推理，该工作具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing geometry-aware Multimodal Large Language Models (MLLMs) increasingly rely on external 3D encoders to provide structural priors, but executing these additional encoder paths at inference introduces substantial latency and computational overhead. We propose GeoThinker-$F$, an efficient framework that internalizes spatiotemporal perception by transforming causal MLLM hidden states into predictive latent world representations. Our key insight is that intermediate semantic representations contain sufficient information to predict useful representations of current geometry and future semantics, without requiring an exact reproduction of features from a dedicated 3D encoder. To realize this idea, GeoThinker-$F$ adopts a decoupled two-stage training strategy. In the first stage, the MLLM backbone is frozen while lightweight Latent Frame Prediction (LFP) heads learn from an offline 3D geometry expert and next-frame semantic targets. In the second stage, the external expert is removed, and the model is jointly optimized to generate and selectively integrate its self-predicted priors through a specialized Spatial-Grounded Temporal (SGT) Fusion module. Extensive evaluations show that GeoThinker-$F$ eliminates runtime dependence on external 3D geometry encoders while maintaining competitive performance across diverse spatial intelligence benchmarks. It achieves up to a $3.6\times$ inference speedup, reducing latency from $1.45\,\mathrm{s}$ to $0.40\,\mathrm{s}$ while retaining strong spatial reasoning performance.

</details>

#### 2026-10-14 - Feasibility of a Patient-Specific Digital Twin for Ventriculoperitoneal Shunt Trajectory Planning

**Authors:** Kritsanavis Chongsrid, Vich Yindeedej, Supaporn Konmun, Xulei Yang, Si Yong Yeo
**Links:** [abs](https://arxiv.org/abs/2610.20074) - [pdf](https://arxiv.org/pdf/2610.20074)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Feasibility of a Patient-Specific Digital Twin for Ventriculoperitoneal Shunt Trajectory Planning
- 作者：Kritsanavis Chongsrid, Vich Yindeedej, Supaporn Konmun, Xulei Yang, Si Yong Yeo
- 出版日期：2026-10-14T12:12:56Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.20074

### 一句话总结
该研究构建了一个基于术前 CT 的患者特异性数字孪生，用于搜索 Keen 点周围满足安全约束、且脑室内长度最长的垂直穿刺轨迹，并在 11 例连续成人中验证了徒手执行该方案的可行性与定位精度。

### 研究问题
脑室腹腔分流失败的最常见原因是导管阻塞；在 Keen 点徒手置入时，仅约十分之一的病例导管尖端能自由位于脑脊液中。因此，研究关注的是：能否通过患者特异性数字孪生优化穿刺入口与深度，从而在不改变手术技术的前提下提高导管在脑室内的放置质量。

### 核心思路/方法
方法上，作者从术前 CT 中通过确定性几何重建颅骨、头皮、耳和脑室，在 Keen 点周围搜索所有入口，寻找在安全约束下具有最长脑室内长度的垂直轨迹，并将计划以两项耳部标尺测量和两个深度值的形式返回。该方案在 11 名连续成人中徒手执行，属于 IDEAL Stage 2a。

### 主要贡献
- 提出并实现了一个患者特异性数字孪生，用于脑室腹腔分流轨迹规划，输出可操作的耳部标尺测量值和深度值。
- 在 11 例连续成人徒手执行中，10/11 达到 Hayhurst Grade 1 放置，而历史对照为 22/213（p = 9 x 10^-9）。
- 报告中位入口偏差 2.5 mm、角度偏差 5.9 度，脑室内导管比 Keen 点多 1.4 cm，且无术中并发症。
- 强调技术本身未改变，增益来自按患者选择入口和深度；并指出是否降低翻修率是下一阶段的假设。

### 局限性
摘要未提供足够信息说明该研究的样本量代表性、长期随访结果、是否降低翻修率、不同术者间的一致性、数字孪生重建或搜索算法的误差来源，以及更广泛人群中的适用性。摘要明确指出“是否降低翻修率是下一阶段的假设”，因此当前证据仅支持可行性与短期定位质量。

### 阅读优先级
中。理由：该研究将患者特异性数字孪生用于神经外科穿刺规划，并在小样本前瞻性可行性研究中报告了显著优于历史对照的定位结果，对手术规划、AR/机器人辅助和数字孪生应用有参考价值；但样本量仅 11 例，主要终点为可行性而非翻修率，且分类偏应用工程，理论或方法创新深度需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

Catheter obstruction is the commonest cause of shunt failure; freehand insertion at Keen's point leaves the tip free in cerebrospinal fluid in only one case in ten. We built a digital twin that reconstructs skull, scalp, ear and ventricles from preoperative CT by deterministic geometry, searches every entry around Keen's point for the perpendicular trajectory with the longest intraventricular length under safety constraints, and returns the plan as two ruler measurements from the ear and two depths. Executed freehand in 11 consecutive adults (IDEAL Stage 2a), it achieved Hayhurst Grade 1 placement in 10 of 11 against 22 of 213 historically (p = 9 x 10^-9), median entry and angular deviations 2.5 mm and 5.9 degrees, 1.4 cm more intraventricular catheter than Keen's point, and no intraoperative complication. The technique was unchanged; the gain came from choosing entry and depth per patient. Whether it lowers revision is the next stage's hypothesis.

</details>

#### 2026-10-14 - FOMI: A Force-Feedback Manipulation Interface for Teaching Contact-Rich Manipulation

**Authors:** Yishu Shen, Yiming Luo, Ruilin Wang, Bowen Yang, Shuai Yang, Fangyi Xu, Yujun Shen, Fu Zhang, Boyu Zhou, Yinghao Xu
**Links:** [abs](https://arxiv.org/abs/2610.19839) - [pdf](https://arxiv.org/pdf/2610.19839)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FOMI: A Force-Feedback Manipulation Interface for Teaching Contact-Rich Manipulation
- 作者：Yishu Shen, Yiming Luo, Ruilin Wang, Bowen Yang, Shuai Yang, Fangyi Xu, Yujun Shen, Fu Zhang, Boyu Zhou, Yinghao Xu
- 出版日期：2026-10-14T09:10:24Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.19839 ；PDF：https://arxiv.org/pdf/2610.19839

### 一句话总结
FOMI 是一种基于剪刀式机构、无需力传感器即可向操作者双手传递交互力的手持力反馈操作接口，用于提升接触丰富任务中无机器人示教采集与遥操作的效率与策略学习效果。

### 研究问题
现有手持式接口在无机器人示教采集中虽然具备可扩展性，但往往缺乏直观的力反馈，导致人类操作者在采集接触丰富演示时面临困难。论文旨在解决如何在无机器人采集与遥操作场景中提供直观力反馈，以支持接触丰富任务的示教与实时动作调整。

### 核心思路/方法
论文提出 FOMI，一种采用剪刀形机构的手持力反馈操作接口。其核心特点是：通过传动连杆将物体交互力直接传递到操作者手上，而无需力传感器，从而提供直观力反馈，支持在无机器人采集接触丰富演示过程中进行实时动作调整。围绕 FOMI，作者构建了包含传感器标定、数据采集与同步的演示采集系统，用于无机器人采集。系统还将 FOMI 的位姿变化与夹爪开合映射为机器人末端执行器位姿与夹爪指令，因此也支持遥操作。

### 主要贡献
- 提出 FOMI，一种剪刀式、无力传感器、可向操作者双手直接传递交互力的手持力反馈操作接口。
- 构建围绕 FOMI 的演示采集系统，集成传感器标定、数据采集与同步，支持无机器人采集。
- 通过将 FOMI 位姿变化和夹爪开合映射到机器人末端执行器位姿与夹爪命令，使系统同时支持遥操作。
- 在四个接触丰富任务上，FOMI 在无机器人采集和遥操作中分别比最佳基线提升约 29% 和 18% 的采集效率；两种模式下采集的演示可使策略以较高成功率完成挑战性接触丰富操作任务。

### 局限性
摘要未提供足够信息，无法确定具体局限性；例如未说明力反馈精度、可扩展性、任务范围、失败案例、硬件成本与长期稳定性等方面的限制。

### 阅读优先级
高。理由：该论文直接针对接触丰富操作示教中力反馈不足这一关键问题，提出无需力传感器的手持力反馈接口，并同时覆盖无机器人采集与遥操作两种模式；摘要还报告了明确的效率提升与策略成功率结果，对具身智能、机器人示教与遥操作方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Robot-free collection with handheld interfaces enables scalable acquisition of human demonstrations for policy learning. However, existing handheld interfaces often provide limited intuitive force feedback, making contact-rich demonstration collection challenging for human operators. To address this, we present FOMI, a force-feedback manipulation interface with a scissor-shaped mechanism, which transmits object interaction forces directly to the operator's hands through actuation links without force sensors. This intuitive force feedback supports real-time action adjustment during robot-free collection of contact-rich demonstrations. Around FOMI, we build a demonstration collection system that integrates sensor calibration, data acquisition, and synchronization for robot-free collection. By further mapping pose changes and gripper opening of FOMI to robot end-effector poses and gripper commands, the system also supports teleoperation. Across four contact-rich tasks, FOMI improves collection efficiency by approximately 29% and 18% over the best baselines in robot-free collection and teleoperation, respectively. Demonstrations collected with FOMI in both modes enable policies to perform challenging contact-rich manipulation tasks with high success rates.

</details>

#### 2026-10-14 - What Matters for World Modeling in Vision-Language-Action Models?

**Authors:** Qisen Ma, Yixiang Chen, Yuan Xu, Peiyan Li, Jiabing Yang, Kai Wang, Jianhua Yang, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang
**Links:** [abs](https://arxiv.org/abs/2610.19825) - [pdf](https://arxiv.org/pdf/2610.19825)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：What Matters for World Modeling in Vision-Language-Action Models?
- 作者：Qisen Ma, Yixiang Chen, Yuan Xu, Peiyan Li, Jiabing Yang, Kai Wang, Jianhua Yang, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang
- 出版日期：2026-10-14T09:01:30Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.19825

### 一句话总结
该论文通过统一的框架系统比较了四种将世界模型整合进视觉-语言-动作（VLA）模型的范式，并分析了世界表示、整合范式和策略骨干等因素对世界建模效果的影响。

### 研究问题
现有将世界模型整合进 VLA 模型的方法在世界表示、整合范式和策略骨干上各不相同，导致难以判断究竟哪些因素对有效的世界模型整合真正重要。论文试图解耦这些因素，回答“在 VLA 中进行世界建模，什么才是关键”这一问题。

### 核心思路/方法
论文将现有工作归纳为四种代表性范式：Implicit Future Alignment、Explicit Future Query、MoT Future Expert 和 External World Predictor。作者在一个统一框架内实例化每种范式，并使用多样的世界表示和策略骨干，在域内、域外、长时程、动态、少样本及真实世界等设置下进行系统评估。

### 主要贡献
论文报告了四项主要发现：1）世界表示的有效性依赖于范式，而 2D 语义表示能提供稳健的跨范式增益；2）没有单一范式具有普遍最优性，但解耦的 MoT Future Expert 具有有竞争力的整体性能，尤其在域外鲁棒性方面；3）世界建模对基于标准 VLM 的策略 consistently 有益，而解耦设计对预训练 VLA 表现出更好的兼容性；4）世界建模在多种设置下优于仅动作基线，在长时程和动态任务上增益显著。

### 局限性
摘要未提供足够信息说明具体实验规模、计算成本、真实世界实验的具体条件、各范式的失败案例或超参数敏感性等细节。

### 阅读优先级
高。理由：该论文针对 VLA 中世界模型整合的关键因素进行了系统性解耦与比较，结论对理解该方向的设计选择具有直接参考价值，且涵盖多种评估设置，适合关注具身智能与机器人学习的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Integrating world models into Vision-Language-Action models (VLAs) has emerged as a promising direction, enabling policies to anticipate future dynamics beyond reactive observation-to-action mapping. However, existing approaches vary simultaneously in their world representations, integration paradigms, and policy backbones, making it difficult to determine what truly matters for effective world model integration. To disentangle these factors, we categorize existing efforts into four representative paradigms, namely Implicit Future Alignment, Explicit Future Query, MoT Future Expert, and External World Predictor. We instantiate each within a unified framework and systematically evaluate these paradigms with diverse world representations and policy backbones across in-domain, out-of-domain, long-horizon, dynamic, few-shot, and real-world settings. Our study yields four main findings: 1) world representation effectiveness is paradigm-dependent, whereas 2D semantic representations offer robust, cross-paradigm gains; 2) no single paradigm is universally optimal, yet the decoupled MoT Future Expert offers competitive overall performance, particularly in OOD robustness; 3) world modeling consistently benefits policies built on standard VLMs, while decoupled designs exhibit greater compatibility with pretrained VLAs; and 4) world modeling improves performance over action-only baselines across multiple settings, with notable gains on long-horizon and dynamic tasks. Project page and video demonstrations are available at https://dylanmqs.github.io/WM-in-VLAs/.

</details>

#### 2026-10-14 - FPV-CRASH: A Dataset for Offline Crash Moment Localization in Drone First-Person-View Videos

**Authors:** Jifan Zhang, Tingyu Wang, Qian Liu, Zhedong Zheng
**Links:** [abs](https://arxiv.org/abs/2610.19785) - [pdf](https://arxiv.org/pdf/2610.19785)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FPV-CRASH: A Dataset for Offline Crash Moment Localization in Drone First-Person-View Videos
- 作者：Jifan Zhang, Tingyu Wang, Qian Liu, Zhedong Zheng
- 出版日期：2026-10-14T08:32:57Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.19785) / [PDF](https://arxiv.org/pdf/2610.19785)

### 一句话总结
该论文提出了 FPV-CRASH，一个面向无人机第一人称视角（FPV）视频的离线“坠机时刻定位”数据集与固定协议参考评测，并给出一个基于热力图的参考模型，显著优于固定时间先验基线。

### 研究问题
论文关注的问题是：在无人机机载 FPV 视频中，定位中断受控飞行的主要物理冲击时刻（Crash Moment），从而为航空机器人领域的事后坠机分析提供时间参考。摘要指出，已有坠机视频数据集主要面向监控或行车记录仪画面，其标注方案与任务形式并非为无人机机载 FPV 视频中主要物理冲击的时间定位而设计。因此，该研究试图填补这一空白。

### 核心思路/方法
- 构建 FPV-CRASH 数据集：包含 1,052 个无人机 FPV 视频片段，其中 526 个为 Crash 片段、526 个为 Normal 片段。
- 标注方式：每个 Crash 片段对 Crash Moment 提供单帧参考标注；Normal 片段不携带时间戳目标，用于训练时的背景监督。
- 字幕辅助：每个片段配有四条英文描述，由采样帧和已知的 Crash/Normal 标签自动生成；这些描述支持一个辅助的“文本到视频检索”任务，但定位推理仍然是纯视频任务。
- 评测协议：提供固定的、非源分离（non-source-disjoint）的片段级协议。
- 参考模型：提出一个基于热力图的参考模型，从稀疏采样帧中估计连续的 Crash Moment 时间戳。

### 主要贡献
- 提出 FPV-CRASH 数据集，用于无人机 FPV 视频中的离线 Crash Moment Localization。
- 提供固定协议的参考评测，并包含 526 个 Crash 与 526 个 Normal 片段的平衡数据组成。
- 提供 Crash Moment 的单帧参考标注，以及自动生成的四条英文描述，支持辅助 Text-to-Video Retrieval 任务，同时保持定位推理为视频输入。
- 提出基于热力图的参考模型，在固定、非源分离的片段级协议下，将 MAE 从最强固定时间先验基线的 1.12 秒降低到 0.56 秒（相对降低 50%），MedAE 达到 0.33 秒；0.5 秒内定位成功的片段比例从 37.14% 提升到 65.71%。
- 发布内容包括标注、可用的源视频标识与 URL、片段元数据、固定划分列表和预处理代码，使得可报告部分可在不重新分发源视频的情况下重建。摘要提到，提交时所有源汇编 URL 仍可访问。

### 局限性
摘要未提供足够信息。摘要未说明参考模型的计算开销、泛化能力、对稀疏采样率的敏感性、跨数据集迁移表现，也未提供源分离协议下的结果或数据偏置分析。此外，摘要未提供完整实验细节、消融研究或失败案例分析。

### 阅读优先级
中。理由：该工作面向无人机 FPV 坠机时刻定位这一相对专门的任务，提出了新数据集、固定评测协议和参考模型，并报告了明确的定量提升，对航空机器人、视频时间定位和坠机分析相关研究者有直接价值。但摘要未提供足够信息说明其方法通用性、跨域泛化和实际部署限制；若研究兴趣不在无人机 FPV、视频时间定位或机器人安全分析方向，优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Crash Moment Localization aims to localize the major physical impact that interrupts controlled flight in an onboard first-person-view (FPV) video recorded by a drone, thereby providing a temporal reference for retrospective crash analysis in aerial robotics. However, existing crash-video datasets predominantly target surveillance or dash-camera footage, and their annotation schemes and task formulations are not designed for temporal localization of the major physical impact in UAV onboard FPV videos. To address this gap, we present FPV-CRASH, a dataset and fixed-protocol reference evaluation for offline Crash Moment Localization in drone FPV videos. FPV-CRASH contains 1,052 drone FPV clips (526 Crash and 526 Normal); each Crash clip has a single-frame reference annotation for the Crash Moment, and every clip is paired with four English captions automatically generated from sampled frames and the known Crash/Normal label. Normal clips carry no timestamp target and provide training-time background supervision. The captions support an auxiliary Text-to-Video Retrieval task, whereas localization inference remains video-only. We further provide a heatmap-based reference model that estimates a continuous Crash Moment timestamp from sparsely sampled frames. Under the fixed, non-source-disjoint clip-level protocol, the reference model reduces MAE from 1.12 s for the strongest fixed timing-prior baseline to 0.56 s (a 50% relative reduction) and achieves a median absolute error (MedAE) of 0.33 s; the fraction of clips localized within 0.5 s rises from 37.14% to 65.71%. The release includes annotations, available source video identifiers and URLs, clipping metadata, fixed split lists, and preprocessing code so that the reportable portion can be reconstructed without redistributing source footage. At submission time, all source-compilation URLs remained accessible.

</details>

#### 2026-10-14 - $S^3$-Nav: Structured Spatial-Semantic Decision Making for Language-Guided Robot Navigation

**Authors:** Chaemin Lee, Hae Min Cho
**Links:** [abs](https://arxiv.org/abs/2610.19431) - [pdf](https://arxiv.org/pdf/2610.19431)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：$S^3$-Nav: Structured Spatial-Semantic Decision Making for Language-Guided Robot Navigation
- 作者：Chaemin Lee, Hae Min Cho
- 出版日期：2026-10-14T02:25:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.19431 ；PDF https://arxiv.org/pdf/2610.19431

### 一句话总结
$S^3$-Nav 是一个面向部分可观测条件下语言引导机器人导航的结构化空间—语义决策框架，通过分离持久状态、面向决策的证据与执行权限，在降低策略推理成本的同时提升闭环导航可靠性。

### 研究问题
论文关注的是部分可观测条件下的语言引导机器人导航：如何在不预先假设完整环境表示的前提下，让机器人边执行边构建空间—语义状态，并让高层策略只访问受容量控制、由任务条件化后的信息视图。核心难点在于，机器人需要保留的证据与策略当前需要检查的内容并不相同，若不加区分，决策复杂度与后续推理、验证所需的落地证据之间会产生矛盾。

### 核心思路/方法
摘要给出的方法要点包括：
1. 不假设预先拥有完整环境表示，而是增量构建持久化的空间—语义状态。
2. 对高层策略只暴露一个容量受控、任务条件化的视图，从而把“机器人必须保留什么”与“策略需要检查什么”解耦。
3. 高层导航输出保持为暂定结果，在物理执行或任务终止之前，需独立地依据持久语义证据与当前几何观测进行落地和验证。
4. 整体上形成持久状态、面向决策的证据、执行权限三者分离的决策结构。

### 主要贡献
摘要明确提到的贡献为：
- 提出 $S^3$-Nav 这一结构化空间—语义决策框架，用于部分可观测下的语言引导机器人导航。
- 通过分离持久状态、面向决策的证据与执行权限，在多个环境和物体目标、关系目标任务上评测，显示可提升闭环导航可靠性并降低策略推理成本。
- 强调高层导航输出在被验证之前只是暂定结果，从而在执行前保留落地与验证环节。

### 局限性
摘要未提供足够信息说明具体失败场景、性能上界、对传感器或环境结构的依赖、计算开销的量化边界、消融实验细节、真实机器人部署范围等。摘要仅说明在多个环境与两类任务上进行了评测，未给出数据集、基线、指标、参数量或安全性分析的细节。

### 阅读优先级
高。理由：该论文的问题设定明确，聚焦部分可观测下的语言引导导航，并提出“持久状态—决策视图—执行权限”分离这一结构化设计；摘要已给出跨环境与物体、关系目标任务的评测结论，且涉及闭环可靠性与推理成本两个关键指标。若关注具身导航、机器人决策架构或语言条件任务，该文值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

This paper presents $S^3$-Nav, a structured spatial-semantic decision-making framework for language-guided robot navigation under partial observability. Rather than assuming a complete environment representation in advance, $S^3$-Nav incrementally constructs persistent spatial-semantic state while exposing only a capacity-controlled, task-conditioned view to the high-level policy. This separation decouples what the robot must retain from what the policy needs to inspect, allowing decision complexity to be controlled without discarding grounded evidence required for subsequent reasoning and validation. High-level navigation outputs remain provisional and are independently grounded and validated against persistent semantic evidence and current geometric observations before physical execution or task termination. Evaluations across multiple environments and object- and relation-goal tasks demonstrate that separating persistent state, decision-facing evidence, and execution authority improves closed-loop navigation reliability while reducing policy reasoning cost.

</details>

#### 2026-10-14 - A VR Training System for Robot-Assisted Vascular Intervention with Dual-Mode Control and Model-Based Interaction Response

**Authors:** Yining Shang, Shuxiang Guo, Sheng Cao, Pengcheng Li, Bin Wang, Mingchao Ding
**Links:** [abs](https://arxiv.org/abs/2610.19413) - [pdf](https://arxiv.org/pdf/2610.19413)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A VR Training System for Robot-Assisted Vascular Intervention with Dual-Mode Control and Model-Based Interaction Response
- 作者：Yining Shang, Shuxiang Guo, Sheng Cao, Pengcheng Li, Bin Wang, Mingchao Ding
- 出版日期：2026-10-14T01:59:33Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.19413

### 一句话总结
该论文提出一个用于机器人辅助血管介入的虚拟现实训练系统，结合异步双模式命令映射与无传感器交互估计，并在初步研究中观察到受训新手在物理体模任务上的表现提升。

### 研究问题
机器人辅助血管介入的虚拟现实训练需要准确的机器人控制和有效的导丝—血管交互反馈。论文关注如何在一个 VR 训练系统中同时支持不同操作模式，并对导丝与血管之间的交互强度进行响应估计，以用于训练与术后回顾。

### 核心思路/方法
系统结合异步双模式命令映射与无传感器交互估计，支持速度控制导航和位置驱动的增量操作。方法上将导丝形变与 Hunt–Crossley 类型接触响应结合，并进行时间滤波以估计交互强度；同时基于轨迹的可视化支持术后回顾。测试涵盖三种速度档位与位置模式下的命令分发模式，并在混合场景导航中观察估计响应。轨迹分析给出模型导出的 normalized units 下累计创伤功（CTW）值为 15.166，并定位交互升高区域。初步研究纳入 15 名新手。

### 主要贡献
- 提出一个 VR 训练系统，支持异步双模式控制：速度控制导航与位置驱动增量操作。
- 将导丝形变与 Hunt–Crossley 类型接触响应结合，并经时间滤波估计交互强度。
- 提供基于轨迹的可视化以支持术后回顾，并给出模型导出的 CTW 值及交互升高区域。
- 初步研究显示，15 名新手在 VR 训练后，物理体模任务成功率由 53.3% 提升至 93.3%，平均完成时间由 132.4 s 降至 96.7 s。

### 局限性
摘要未提供足够信息说明样本规模之外的受试者特征、对照组设置、统计显著性、长期保留效果、系统延迟或真实临床转化验证等细节。摘要未提供足够信息说明 CTW 计算模型的具体参数与验证方式。摘要未提供足够信息说明系统在更复杂血管模型或不同操作者水平下的泛化表现。

### 阅读优先级
中。理由：该论文涉及机器人辅助血管介入的 VR 训练、双模式控制与交互响应估计，且给出了新手初步研究结果，对相关方向有参考价值；但摘要仅提供初步结果，未给出完整实验设计、统计分析和临床验证信息，因此不适合作为最高优先级精读，除非读者特别关注该训练系统或 CTW 类交互估计方法。

</details>

<details>
<summary>Abstract</summary>

Virtual reality training for robot-assisted vascular intervention requires accurate robotic control and effective feedback on guidewire--vessel interactions. This paper presents a VR training system combining asynchronous dual-mode command mapping with sensorless interaction estimation. The system supports velocity-controlled navigation and position-driven incremental manipulation. Guidewire deformation and a Hunt--Crossley-type contact response are combined and temporally filtered to estimate interaction intensity, while trajectory-based visualization supports post-procedure review. Tests confirmed distinct command-dispatch patterns across three velocity gears and the position mode. During hybrid-scene navigation, the estimated response remained low during straight insertion and increased as the guidewire bent within the vascular model. Trajectory analysis yielded a model-derived cumulative trauma work (CTW) value of 15.166 in normalized units and localized regions of elevated interaction. In a preliminary study with 15 novices, physical-phantom task success increased from 53.3% to 93.3% after VR training, while mean completion time decreased from 132.4 s to 96.7 s. These results demonstrate the system's dual-mode operation, deformation-sensitive feedback, and potential to improve subsequent physical-phantom task performance.

</details>

#### 2026-10-13 - Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors

**Authors:** Henry Che, Xuanchi Ren, Sanja Fidler, Shenlong Wang, Laura Leal-Taixé, Shengyu Huang
**Links:** [abs](https://arxiv.org/abs/2610.19201) - [pdf](https://arxiv.org/pdf/2610.19201)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors
- 作者：Henry Che, Xuanchi Ren, Sanja Fidler, Shenlong Wang, Laura Leal-Taixé, Shengyu Huang
- 出版日期：2026-10-13T21:11:28Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2610.19201) / [PDF](https://arxiv.org/pdf/2610.19201)

### 一句话总结
LidarVerse 提出一个实时统一的 LiDAR 世界模型，将重建式与生成式两种范式整合进同一条件生成框架，实现跨任务、跨传感器的传感器仿真。

### 研究问题
现有 LiDAR 仿真器主要沿两条互补范式展开：重建式方法能保留所捕获场景的几何结构，但需要针对每个场景进行耗时优化；生成式方法可跨数据摊销学习，但缺乏长时程 rollout 所需的一致性。论文试图解决如何将两者统一到单一模型中，并同时兼顾长时程一致性与实时推理。

### 核心思路/方法
- 提出统一的条件生成框架 LidarVerse，把重建式与生成式范式结合到一个模型中。
- 使用通用 tokenizer 将 LiDAR 距离序列映射到共享潜在空间。
- 在该潜在空间中，一个双向 teacher 学习统一的条件接口，可条件于 LiDAR 前缀、HD-Map、持久化空间缓存，并可选地条件于文本。
- 通过改变可用的场景证据，同一个模型可分别充当新世界的生成器、点云预测器，或对已观测场景的可泛化重仿真器，且无需逐场景优化。
- 将 teacher 蒸馏为四步自回归因果 student，并维护滚动时间 K/V 缓存与世界对齐的空间缓存，从而支持持久长时程 rollout。
- 在单张 H100 GPU 上实现 11 FPS 的实时推理。

### 主要贡献
- 提出 LidarVerse，将生成式与重建式 LiDAR 仿真统一在一个模型中，为未来闭环传感器仿真提供核心能力。
- 通过通用 tokenizer 支持 32、64、128 束 LiDAR，并能泛化到未见过的扫描模式。
- 在全部三种评估协议中的多数报告指标上取得 state-of-the-art 性能。
- 实现实时推理（单张 H100 GPU 上 11 FPS）与持久长时程 rollout。

### 局限性
- 具体的计算资源需求、训练数据规模与训练成本：摘要未提供足够信息。
- 三种评估协议的具体内容、基线方法与详细指标数值：摘要未提供足够信息。
- 文本条件的具体形式与效果：摘要未提供足够信息。
- 蒸馏带来的性能损失、四步自回归的具体设计细节：摘要未提供足够信息。
- 在真实闭环仿真或下游任务中的验证情况：摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对 LiDAR 仿真中重建式与生成式范式的核心矛盾提出统一框架，同时覆盖跨任务、跨传感器、长时程一致性与实时推理等关键能力，并声称在多数指标上达到 state-of-the-art，对自动驾驶、机器人感知与闭环传感器仿真方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors. Existing LiDAR simulators largely follow one of two complementary paradigms: reconstruction-based methods preserve the geometry of a captured scene but require lengthy per-scene optimization, whereas generative methods amortize learning across data but lack the consistency needed for long-horizon rollouts. LidarVerse brings both paradigms into a single, unified conditional generative framework. A universal tokenizer maps LiDAR range sequences into a shared latent space, where a bidirectional teacher learns a common interface for conditioning on a LiDAR prefix, an HD-Map, a persistent spatial cache, and optionally, text. Varying the available scene evidence turns the same model into a generator of new worlds, a point-cloud forecaster, or a generalizable resimulator of observed scenes without per-scene optimization. We distill the teacher into a four-step autoregressive causal student and maintain both a rolling temporal K/V cache and a world-aligned spatial cache, enabling persistent long-horizon rollouts with real-time inference at 11 FPS on a single H100 GPU. LidarVerse achieves state-of-the-art performance on most reported metrics across all three evaluation protocols, while its tokenizer supports 32-, 64-, and 128-beam LiDAR and generalizes to an unseen scanning pattern. These results demonstrate that generative and reconstruction-grounded LiDAR simulation can be realized within one model, providing the core capabilities for future closed-loop sensor simulation.

</details>

#### 2026-10-13 - EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

**Authors:** Yunsong Zhou, Xuekun Jiang, Haiqi Shen, Hangxu Liu, Chaojian Shi, Yujie Liu, Jingyuan Li, Haoran Yang, Jiafei Cao, Dongzhan Zhou, Dong Wang, Yao Mu, Chunhua Shen, Weinan Zhang
**Links:** [abs](https://arxiv.org/abs/2610.18872) - [pdf](https://arxiv.org/pdf/2610.18872)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ
- 作者：Yunsong Zhou, Xuekun Jiang, Haiqi Shen, Hangxu Liu, Chaojian Shi, Yujie Liu, Jingyuan Li, Haoran Yang, Jiafei Cao, Dongzhan Zhou, Dong Wang, Yao Mu, Chunhua Shen, Weinan Zhang
- 出版日期：2026-10-13T17:59:55Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.18872) / [PDF](https://arxiv.org/pdf/2610.18872)

### 一句话总结
本文提出 EgoExplorer——一个基于可穿戴系统、时长 100 小时的视觉—运动—触觉人类 loco-manipulation 观测数据集，并配套提出 Calibrate-Complete-Constrain 流程，以在稀疏体感条件下重建全身运动与手部精细动作。

### 研究问题
- 从人类演示中学习人形机器人的 loco-manipulation，需要观察移动、姿态与物体交互如何随任务展开而共同演化。
- 要在多种环境中扩大采集规模，需要轻量、便携的采集系统。
- 摘要指出，现有数据集只能提供这种协调过程的部分视图，缺乏对上述多模态协同的完整覆盖。

### 核心思路/方法
- 构建 EgoExplorer：一个 100 小时的视觉—运动—触觉人类 loco-manipulation 观测系统，采用可穿戴系统采集，侧重专业活动场景。
- 数据内容：连续记录将第一视角视频与重建的全身运动、细粒度手指关节动作、触觉观测对齐，并附有 step-level（步骤级）描述。
- 针对稀疏体感条件下的覆盖问题，提出 Calibrate-Complete-Constrain 流程：
  - 可复用标定：在运动推断前固定参与者几何结构与传感器佩戴方式，从而将安装偏移与关节动作解耦。
  - 时间先验：补全未观测的关节运动。
  - 分层约束：促进测量一致性、时间连续性与几何一致性——摘要指出这些性质仅靠运动合理性并不能保证。
- 初步研究探索了多模态生成与条件化，以及在仿真中结合全身控制的人形重定向。

### 主要贡献
- 提出 EgoExplorer，一个 100 小时、以专业活动为重点、基于可穿戴系统的视觉—运动—触觉人类 loco-manipulation 观测数据集，将第一视角视频与全身运动、手指精细动作、触觉观测及步骤级描述对齐。
- 提出 Calibrate-Complete-Constrain 流程，用于在稀疏体感条件下实现上述覆盖。
- 实验结果表明：相较于最强基线，该方法在身体点误差上降低 71.9%（以 tracker 拟合结果为参考）；匹配评估还显示手部稳定性与接触估计有所提升。
- 初步研究探索了多模态生成与条件化，以及仿真中结合全身控制的人形重定向。

### 局限性
- 摘要未提供足够信息说明数据集的具体规模分布、参与者数量、场景多样性及任务类型覆盖范围。
- 摘要未提供足够信息说明标定方法对传感器配置变化的敏感性与泛化能力。
- 摘要未提供足够信息说明手部稳定性与接触估计提升的具体数值与评估协议。
- 摘要未提供足够信息说明多模态生成、条件化与人形重定向初步研究的定量结果。
- 摘要未提供足够信息说明可穿戴系统在真实采集中的舒适性、遮挡与长时间佩戴带来的影响。

### 阅读优先级
- 优先级：中
- 理由：该工作面向人形机器人从人类演示中学习 loco-manipulation 的数据瓶颈，提出的 100 小时多模态数据集与稀疏体感重建流程具有一定针对性，且摘要给出了身体点误差降低 71.9% 的量化结果。但摘要未披露数据集规模细节、评估协议与初步研究的定量验证，是否与具体研究需求匹配需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer, a 100-hour vision-motion-touch observatory of human loco-manipulation built with a wearable system. With an emphasis on professional activities, its continuous recordings align egocentric video with reconstructed whole-body motion, fine-grained finger articulation, and tactile observations, accompanied by step-level descriptions. To achieve this coverage with sparse body sensing, we develop the Calibrate-Complete-Constrain pipeline. Concretely, reusable calibration fixes participant geometry and sensor attachments before motion inference to disentangle mounting offsets from articulation. A temporal prior then completes unobserved joint motion, while layered constraints promote measurement agreement, temporal continuity, and geometric consistency, properties that motion plausibility alone does not guarantee. Against tracker-fitted references, the method reduces body-point error by 71.9% relative to the strongest baseline; matched evaluations also show gains in hand stability and contact estimation. Preliminary studies explore multimodal generation and conditioning alongside humanoid retargeting with whole-body control in simulation.

</details>

#### 2026-10-13 - ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation

**Authors:** Zijun Xu, Wendi Chen, Xinkai Wang, Jiachen Zou, Hongjin Chen, Hairuo Liu, Bokai Lin, Shihao Ma, Ke Ma, Zhiwei Zhang, Zhuohao Yan, Ke Wu, Haoming Song, Xueqi Li, Chuan Wen, Jieru Zhao, Wenchao Ding, Cewu Lu, Lixin Yang
**Links:** [abs](https://arxiv.org/abs/2610.18852) - [pdf](https://arxiv.org/pdf/2610.18852)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation
- 作者：Zijun Xu, Wendi Chen, Xinkai Wang, Jiachen Zou, Hongjin Chen, Hairuo Liu, Bokai Lin, Shihao Ma, Ke Ma, Zhiwei Zhang, Zhuohao Yan, Ke Wu, Haoming Song, Xueqi Li, Chuan Wen, Jieru Zhao, Wenchao Ding, Cewu Lu, Lixin Yang
- 出版日期：2026-10-13T17:58:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.18852) / [PDF](https://arxiv.org/pdf/2610.18852)

### 一句话总结
ForceWAM 将“任务兼容的交互结果预测”与“局部动作如何改变接触”这两类知识解耦，分别通过世界模型和逆动力学模型从示范数据与任务无关的 play 数据中学习，以提升接触丰富操作的成功率。

### 研究问题
接触丰富任务中，专家示范能展示如何完成任务，但对“不同动作下交互力如何响应”的覆盖有限；任务无关的 play 数据虽包含更广泛的接触动力学经验，却不指定任务目标。论文关注如何同时利用这两类数据，以支撑接触丰富操作中的力调节执行。

### 核心思路/方法
论文提出 ForceWAM，一种 force world action model，将知识拆分为两部分：
1. 世界模型从成功示范中学习，联合预测未来视频与六轴力/力矩轨迹；这些未来共同描述任务中运动与接触的预期演化。
2. 独立的逆动力学模型（IDM）从任务数据与 play 数据中学习，将当前观测和记录的视觉-力/力矩未来映射为对应机器人动作；play 数据由此提供面向目标执行的力响应知识。
部署时，IDM 反应式地将生成的未来转化为动作，并在世界模型更新之间结合新鲜力/力矩反馈复用这些未来。

### 主要贡献
- 提出 ForceWAM，将任务兼容的交互结果知识与局部动作改变接触的知识进行解耦。
- 设计世界模型从成功示范中联合预测未来视频与六轴力/力矩轨迹。
- 设计独立 IDM，同时从任务与 play 数据中学习，使 play 数据提供力响应知识以服务目标导向执行。
- 在真实机器人力调节滑动、有/无扰动的盒子翻转以及圆环放置任务中，报告 85%–95% 平均成功率，超过世界建模与反应式基线。
- 实验显示，加入任务无关 play 数据可将成功率提升 15–45 个百分点，体现其对学习接触丰富执行的价值。

### 局限性
摘要未提供足够信息。摘要未给出失败模式、方法假设、计算开销、泛化边界或 play 数据质量影响等细节。

### 阅读优先级
高。理由：该论文直接处理接触丰富操作中示范数据覆盖不足与任务无关 play 数据利用的问题，提出解耦式世界模型与逆动力学框架，并在多个真实机器人任务上报告了明确的成功率提升；对机器人力控制、世界模型和机器人学习方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Expert demonstrations show how to complete contact-rich tasks, but provide limited coverage of how interaction forces respond to different actions. Task-agnostic play provides broader experience of contact dynamics without specifying task goals. To fully leverage these two types of data, we introduce ForceWAM, a force world action model that decouples knowledge of task-compatible interaction outcomes from knowledge of how local actions change contact. A world model learns from successful demonstrations to jointly predict future video and six-axis force/torque trajectories. Together, these futures describe the expected evolution of motion and contact during the task. A separate inverse dynamics model (IDM) learns from both task and play, mapping current observations and recorded visual-wrench futures to their associated robot actions. Play data thus provide knowledge of force responses for goal-directed execution. At deployment, the IDM reactively translates generated futures into actions, reusing them with fresh wrench feedback between world-model updates. Across real-robot force-regulated sliding, box flipping with and without disturbances, and ring placement, ForceWAM achieves $85$-$95\%$ mean success, surpassing world-modeling and reactive baselines. Our experiments further show that adding task-agnostic play data improves success by $15$-$45$ percentage points, demonstrating its value for learning contact-rich execution. Project page and code are available at https://force-wam.github.io/.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
