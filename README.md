# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：36
- 分类分布：
  - Neural Scene Representations & Rendering: 14
  - 3D Reconstruction & Multi-view Geometry: 12
  - Embodied / Robotics / AR Applications: 6
  - Geometry Foundation Models: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**1. 3DGS 从"表征工具"走向"多角色复用与场景理解中枢"**
多篇论文不再将 3DGS 仅视为渲染表征，而是将其作为集几何、可见性、语义、语言于一体的多模态场景表示。SplatGuide 复用同一 3DGS 场景产生渲染图像、逐高斯可见性投票图和重建 token 三种信号；GaussianDWM++ 将 Qwen/SigLIP 视觉语言特征直接蒸馏进 3D 高斯基元，构建开放词汇语义场；QAGaussian 在 3DGS 上做查询自适应的结构化推理（而非相似性匹配）；Gaussian-JEPA 则在 3DGS token 上进行潜空间自监督预测。这种"单一表示、多角色复用"的趋势显著。

**2. 几何基础模型（Video/Image-based Reconstruction Models）向任务专用化与下游适配演进**
VGGT 风格的重建基础模型正被适配到特定场景。VGGT-Align 针对长序列重建的尺度漂移问题，提出场景几何不变量锚定（SGIA），将 Sim(3) 对齐退化为刚体变换；GeoUP 则将 VGGT 重建导向潜表示适配到流式多相机驾驶场景，支撑度量深度、3D 检测和语义占用三个任务。这表明几何基础模型正从"通用重建"走向"下游任务级适配"。

**3. 视觉-语言-3D 融合走向结构化推理与细粒度对齐**
从简单的文本-区域全局相似性匹配，转向基于关系图的逻辑推理和细粒度特征对齐。QAGaussian 直接批判全局相似性匹配的弱点，提出多尺度高斯槽 + 关系感知槽图推理；GaussianDWM++ 强调文本与 3D 结构细粒度对齐的必要性，采用 KL 对齐将高斯世界 token 与基础图像 token 对齐。

**4. 物理交互与交互式仿真成为神经场景表示的新延伸**
LaGSplat 将低维潜状态同时作为耗散拉格朗日动力学广义坐标和 3DGS 解码器条件变量，支持用户对物体施加训练未见过的外力。这是"重建 + 物理"融合方向的一个典型代表，结合了可微物理与神经渲染的归纳偏置。

**5. 效率优化与边缘化部署成为显式研究维度**
TinyDETR-Pose 面向资源受限硬件做端到端 6DoF 位姿估计；RoofGS 通过 Roofline 分析差异化优化 3DGS 渲染瓶颈；BinRVR 用二值化网络实现约 96% 的参数量和计算量缩减。这与"大规模基础模型"的趋势并行，构成另一条清晰的优化路径。

---

#### 技术路线观察

| 方向 | 技术侧重 | 代表论文 |
|------|----------|----------|
| **几何基础模型** | 主要聚焦如何校准尺度漂移（Sim(3)→SE(3) 降自由度退化）、如何将重建潜表示适配到下游感知任务（因子化注意力 + 标定感知射线图） | VGGT-Align、GeoUP |
| **3D/4D 重建与神经场景表示** | 3DGS 成为绝对主导表示；强调从单一场景中复用多种信号（渲染、可见性、token、语义）或引入物理可解释潜状态；自监督方向探索 JEPA 式潜空间预测 | SplatGuide、Gaussian-JEPA、LaGSplat、GS²CI |
| **视觉-语言-3D 交叉** | 从"相似性匹配"转向"结构化推理"；采用槽式候选 + 图推理（语言条件边权重）+ 粒度自适应路由；或利用基础特征蒸馏实现开放词汇语义场 | QAGaussian、GaussianDWM++ |
| **机器人/AR 应用** | 强调低成本遥操作硬件 + 触觉反馈提升接触关键任务示教质量；动作条件世界模型（注入 SE(3) 几何编码、深度分支 + SAM3 掩码）；语义辐射场作为模拟器提供几何和语义接地 | ViHaTeleop、DreamX-Phi 1.0、Semantic Radiance Fields as Simulators |
| **效率优化与低资源** | Roofline 模型驱动的瓶颈特定优化；二值化网络 + 分布感知量化；轻量级 Transformer 单阶段端到端位姿回归 | RoofGS、BinRVR、TinyDETR-Pose |

值得注意的横向特征：多个工作（VGGT-Align、GeoUP、GaussianDWM++、SplatGuide）都共享一种"将大模型/基础模型的特征或潜表示嵌入 3D 表示中"的范式，差异在于嵌入的层次（逐高斯 vs. 场景级 token）和用途（重建、感知、编辑）。

---

#### 值得优先阅读的论文

**1. SplatGuide（2608.16863）**
将同一 3DGS 场景复用于三种互补信号，直接解决"信息断开"问题，且无额外计算开销。对 3DGS 前馈重建 + 扩散的管线设计具有较强的方法论启发价值。

**2. VGGT-Align（2608.15260）**
聚焦长序列 3D 重建核心痛点——尺度漂移，提出即插即用框架（SGIA + 测试时自适应），无需重训即可直接挂载到现有 VGGT 类管线，实用性和增量贡献明显。

**3. QAGaussian（2608.16103）**
明确指出现有 3DGS 指代分割基于全局相似性匹配的不足，提出系统的结构化推理框架（多尺度槽 + 图推理 + 粒度路由）。对"语言-3D"交互方向有较强的范式意义。

**4. Gaussian-JEPA（2608.15651）**
首次将 JEPA 潜空间预测范式引入 3DGS 表示学习，解决高斯原语耦合属性与异质空间支撑的难题。对 3D 自监督预训练方向有前瞻性价值，可能影响后续 3D 基础模型的预训练方式。

**5. LaGSplat（2608.16324）**
将物理可解释的拉格朗日动力学与 3DGS 解码器结合，实现用户可在推理时交互施力。这是"可交互物理 + 神经渲染"的跨域创新，值得跟踪其后续扩展。

---

#### 可能的研究机会

**1. 3DGS 的多角色统一复用 + 下游任务联合学习**
SplatGuide 展示了同一 3DGS 场景可产生几何、可见性、特征三种信号，GaussianDWM++ 则展示了语言语义蒸馏的可行性。将这两种思路结合，探索"一个 3DGS 表示同时服务重建、理解、编辑、交互"的统一框架，是一个明确的空白。

**2. 3DGS 的 JEPA 式预训练 + 下游任务微调**
Gaussian-JEPA 刚提出潜空间预测范式，但下游验证还限于部件分割和物体分类。将其扩展到语言引导的指代分割（QAGaussian）、场景理解（GaussianDWM++）、乃至驾驶场景，是一个自然的延伸方向。

**3. 尺度/位姿一致性的跨任务复用**
VGGT-Align 的 SGIA 利用了驾驶场景的几何不变量，GeoUP 则适配了 VGGT 潜表示到多相机驾驶感知。两者核心都是"利用场景结构约束重建/感知一致性"，但尚未被统一。可探索一个通用的"几何不变量约束模块"，跨数据集、跨任务复用。

**4. 物理交互合成数据的生成与自监督**
LaGSplat 从单目视频推断物理交互，DreamX-Phi 1.0 是动作条件视频世界模型，SRF 则用语义辐射场做模拟器。三者的共性都是"用可交互/可查询的神经场景表示生成训练数据"。探索用物理可解释的 3DGS 场景生成机器人操作或空间推理的训练数据，是一个有潜力的组合方向。

**5. 高频感知（SCI / 压缩成像）与几何基础模型的结合**
GS²CI 已证明快照压缩成像 + 3DGS + 视觉基础模型先验的可行性。但

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-19T09:06:53-04:00
**Total number of papers:** 42
**Number of papers added in the latest update:** 15
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

### 2026-08

#### 2026-08-15 - VGGT-Align: Bridging Local Reconstruction and Global Consistency for Long-Sequence 3D Reconstruction

**Authors:** Wei Zhang, Yihang Wu, Songhua Li, Qi Wang
**Links:** [abs](https://arxiv.org/abs/2608.15260) - [pdf](https://arxiv.org/pdf/2608.15260)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VGGT-Align: Bridging Local Reconstruction and Global Consistency for Long-Sequence 3D Reconstruction
- 作者：Wei Zhang, Yihang Wu, Songhua Li, Qi Wang
- 出版日期：2026-08-15
- 分类：Geometry Foundation Models（次要分类：3D Reconstruction & Multi-view Geometry）
- 链接：https://arxiv.org/abs/2608.15260

### 一句话总结
本文提出一种即插即用的尺度一致性增强框架（含SGIA与测试时自适应策略），通过约束块间尺度漂移来提升长序列三维重建的全局几何一致性。

### 研究问题
长序列三维重建中全局几何一致性难以保持，核心故障模式是尺度漂移——在基于分块（chunk-based）的推断流程中，逐块Sim(3)对齐的尺度自由度未被约束，导致估计误差乘法式累积，扭曲全局轨迹与点云几何。

### 核心思路/方法
- 关键洞察：在驾驶场景等结构化环境中，环境规则性衍生的几何量在时间片段间本质不变，其逐块测量差异可直接暴露块间尺度漂移。
- **Scene Geometric Invariant Anchoring (SGIA)**：从每块预测点云中通过粗到细的鲁棒估计提取主导几何不变量，利用跨块一致性建立独立于点云配准的尺度约束，将7自由度Sim(3)对齐显式退化为6自由度刚体变换，从源头切断链式尺度误差传播。
- **测试时自适应策略**：通过多目标自监督仅微调归一化层参数，沿序列渐进改善块内预测。
- 两个模块均为即插即用，无需离线重训练。

### 主要贡献
- 提出SGIA方法，利用场景几何不变量约束尺度漂移，将Sim(3)对齐退化为刚体变换。
- 提出轻量级测试时自适应策略（仅微调归一化层参数）。
- 两项模块均即插即用，无需离线重训练。
- 在多个长序列基准上达到最先进性能，绝对轨迹误差最多降低32%，轨迹稳定性与重建质量显著提升。
- 开源代码。

### 局限性
摘要未提供足够信息（如对非结构化场景的泛化能力、计算开销细节、失败案例分析等均未提及）。

### 阅读优先级
**高**
理由：该方法针对长序列三维重建中常见的尺度漂移问题提出了无需重训练的即插即用解决方案，在多个基准上误差降低显著（最高32%），且代码已开源，对从事三维重建、几何基础模型相关研究的读者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Maintaining global geometric consistency is a central challenge in long-sequence 3D reconstruction, with scale drift being the most critical failure mode. In chunk-based inference pipelines, the scale degree of freedom in sequential Sim(3) alignment is left unconstrained, causing estimation errors to compound multiplicatively and distort global trajectories and point cloud geometry. We present a scale-consistency enhancement framework built on a key insight: in structured environments such as driving scenes, geometric quantities arising from environmental regularity remain inherently invariant across temporal segments, and discrepancies in their per-chunk measurements directly expose inter-chunk scale drift. We propose Scene Geometric Invariant Anchoring (SGIA), which extracts dominant geometric invariants from each chunk's predicted point cloud via coarse-to-fine robust estimation and exploits their cross-chunk consistency to establish scale constraints independent of point cloud registration, explicitly degenerating 7-DoF Sim(3) alignment into 6-DoF rigid-body transformation and severing chain-wise scale error propagation at its source. We further introduce a lightweight test-time adaptation strategy that fine-tunes only normalization-layer parameters via multi-objective self-supervision, progressively improving intra-chunk predictions along the sequence. Both modules are plug-and-play and require no offline retraining. Experiments on multiple long-sequence benchmarks demonstrate state-of-the-art performance, reducing absolute trajectory error by up to 32% with significant gains in trajectory stability and reconstruction quality. Code: https://github.com/WZ-CS/VGGT-Align

</details>

#### 2026-08-13 - Geometry-Grounded Unified 3D Perception for Autonomous Driving

**Authors:** Longfei Xu, Xiaohui Wang, Zehao Huang, Han Li, Ya Yang, Naiyan Wang, Si Liu
**Links:** [abs](https://arxiv.org/abs/2608.13147) - [pdf](https://arxiv.org/pdf/2608.13147)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, metric depth, depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry-Grounded Unified 3D Perception for Autonomous Driving
- 作者：Longfei Xu, Xiaohui Wang, Zehao Huang, Han Li, Ya Yang, Naiyan Wang, Si Liu
- 出版日期：2026-08-13
- 分类：Geometry Foundation Models（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.13147

### 一句话总结
本文提出GeoUP框架，将基于几何基础模型的重建导向潜表示适配到多相机驾驶场景，通过因子化跨图像注意力和校准感知的射线图编码，实现度量深度估计、3D目标检测和语义占用预测的统一3D感知。

### 研究问题
现有基于相机的自动驾驶感知框架通常使用为语义识别预训练的骨干网络，并通过下游任务特定模块引入3D几何，导致其共享表示难以保留显式的度量几何和一致的3D场景结构。本文旨在构建一种能够保持度量3D结构的统一共享表示，以支持多种3D感知任务。

### 核心思路/方法
- 将重建导向的VGGT潜表示适配到经过标定的、流式的多相机驾驶场景中。
- 将跨图像交互分解为自注意力、时间注意力和视图注意力，以分别捕获结构上不同的时间和跨视图对应关系。
- 注入校准感知的射线图编码，以提供度量尺度和相机几何信息。
- 将几何基础的潜表示解码为度量深度估计、3D目标检测和语义占用预测，分别对应同一3D场景的表面级、实例级和体素级读取。
- 通过多任务和多数据集联合训练，利用异构标注并泛化到不同的传感器配置和感知范围。

### 主要贡献
- 提出GeoUP框架，将几何基础模型的潜表示引入统一的3D驾驶感知。
- 设计因子化的自/时间/视图注意力结构，以捕获时间和跨视图的结构性对应关系。
- 引入校准感知的射线图编码，提供度量尺度和相机几何。
- 在nuScenes、Argoverse 2、Waymo、KITTI和DDAD等多个数据集上实现检测、占用和深度估计的SOTA性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶统一3D感知中的核心瓶颈——共享表示的度量几何保持问题，提出了基于几何基础模型的全新方案，并在五个公开数据集上取得SOTA结果，方法思路新颖且实验覆盖广泛，对从事多相机3D感知、几何基础模型及应用的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera-based autonomous driving perception requires a shared representation that preserves metric 3D structure across synchronized multi-camera streams. However, existing image-based frameworks often rely on backbones pretrained for semantic recognition, and introduce 3D geometry through downstream task-specific modules. As a result, their shared representations may fail to preserve explicit metric geometry and consistent 3D scene structure. In this paper, we present a Geometry-grounded Unified 3D Perception (GeoUP) framework that adapts the reconstruction-oriented latent of VGGT to calibrated, streaming multi-camera driving scenes. GeoUP factorizes cross-image interaction into self, temporal, and view attention to capture structurally distinct temporal and cross-view correspondences. It further injects calibration-aware raymap encodings to provide metric scale and camera geometry. The resulting geometry-grounded latent is decoded for metric depth estimation, 3D object detection, and semantic occupancy prediction, corresponding to surface-, instance-, and volume-level readouts of the same 3D scene. Through joint multi-task and multi-dataset training, GeoUP effectively leverages heterogeneous annotations and generalizes across diverse sensor configurations and perception ranges. Extensive experiments on nuScenes, Argoverse 2, Waymo, KITTI, and DDAD demonstrate that GeoUP achieves SOTA performance across detection, occupancy, and depth estimation. These results validate the effectiveness of geometry-grounded representations for unified 3D driving perception.

</details>

#### 2026-08-13 - RbFT-Net: Rectify-Before-Fuse Temporal Radar Anchors for 4D Radar-Camera Depth Completion

**Authors:** Wentao Zhao, Shouxuan Wu, Yongtao Cen, Tianchen Deng, Yuyang Zhang, Jingchuan Wang
**Links:** [abs](https://arxiv.org/abs/2608.13102) - [pdf](https://arxiv.org/pdf/2608.13102)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** depth prediction, metric depth, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RbFT-Net: Rectify-Before-Fuse Temporal Radar Anchors for 4D Radar-Camera Depth Completion
- 作者：Wentao Zhao, Shouxuan Wu, Yongtao Cen, Tianchen Deng, Yuyang Zhang, Jingchuan Wang
- 出版日期：2026-08-13
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2608.13102

### 一句话总结
RbFT-Net提出了一种“先矫正后融合”的端到端框架，通过对多帧4D雷达点进行图像条件化矫正与可靠性估计，再选择性传播锚点，以提升雷达-相机深度补全的精度与鲁棒性。

### 研究问题
多帧雷达-相机深度补全中，聚合后的雷达测量虽能提供更密的度量提示，但存在时间错位、动态物体干扰、杂波和多径反射等问题，直接传播不可靠测量会污染大范围深度预测区域。

### 核心思路/方法
- 将累积的雷达返回视为带有噪声的时序锚点候选，而非直接视为准确测量。
- 设计图像条件化矫正模块，联合修正锚点在图像平面上的位置和度量深度，并同时估计逐点可靠性。
- 经矫正后的锚点在高层多模态融合之前进行选择性传播，以抑制不可靠测量的影响。
- 整体采用“先矫正后融合”（rectify-before-fuse）的端到端训练框架。

### 主要贡献
- 提出RbFT-Net，一个端到端的“先矫正后融合”多帧4D雷达-相机深度补全框架。
- 不再假设累积雷达返回准确，而是将其建模为带噪声的时序锚点候选，并引入图像条件化矫正与可靠性估计。
- 在ZJU-4DRadarCam及新采集的4D雷达-相机-激光雷达数据集上，持续优于所评估的独立雷达-相机方法，并与使用辅助单目深度模型的插件式方案保持竞争力。
- 跨平台评估和组件分析验证了所提矫正与可靠性感知传播策略的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向自动驾驶中的雷达-相机深度补全，方法设计合理且有跨数据集验证，但摘要未给出具体数值性能或与最先进方法的详细对比，若读者关注多模态深度补全或雷达感知可进一步阅读全文，否则优先度一般。

</details>

<details>
<summary>Abstract</summary>

Dense metric depth prediction from cameras and millimeter-wave radar offers a cost-effective sensing solution for autonomous systems. However, radar measurements are inherently sparse and susceptible to clutter, multipath reflections, and projection errors. While aggregating multiple radar frames provides denser metric cues, it also introduces temporal misalignment and dynamic-object interference. Directly propagating such unreliable measurements can therefore corrupt large regions of the predicted depth map. To address this issue, we propose RbFT-Net, an end-to-end rectify-before-fuse framework for multi-frame 4D radar-camera depth completion. Rather than assuming accumulated radar returns to be accurate, RbFT-Net treats them as noisy temporal anchor candidates. An image-conditioned rectification module jointly corrects their image-plane locations and metric depths while estimating pointwise reliability. The rectified anchors are then selectively propagated before high-level multi-modal fusion, suppressing the influence of unreliable measurements. Experiments on ZJU-4DRadarCam and a newly collected 4D radar-camera-LiDAR dataset show that RbFT-Net consistently outperforms the evaluated independent radar-camera methods and remains competitive with plug-in pipelines using auxiliary monocular depth models. Cross-platform evaluation and component analyses further support the effectiveness of the proposed rectification and reliability-aware propagation strategy.

</details>

#### 2026-08-12 - Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs

**Authors:** Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò, Sunghwan Hong, Denis Rozumny, Johannes Schönberger, Zuria Bauer, Hermann Blum, Peter Kontschieder, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2608.12179) - [pdf](https://arxiv.org/pdf/2608.12179)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs
- 作者：Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò, Sunghwan Hong, Denis Rozumny, Johannes Schönberger, Zuria Bauer, Hermann Blum, Peter Kontschieder, Marc Pollefeys
- 出版日期：2026-08-12
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.12179

### 一句话总结
Map-Det3D 将前馈式度量 3D 重建模型作为几何骨干，将多视角 3D 物体检测直接引入重建出的度量 3D 空间中，从而从单目视频流中实现稳定的度量级 3D 检测。

### 研究问题
如何在缺乏深度传感器的情况下，从单目视频流中实现可靠的度量级 3D 物体检测，尤其是克服单张图像中深度和绝对尺度欠约束带来的检测不稳定性，以及在相机、运动或环境发生域偏移时的泛化问题。

### 核心思路/方法
- 设计在线多视角 3D 检测模型 Map-Det3D，将短时间窗口内的多视图映射为输入，使用前馈度量 3D 重建模型作为几何骨干，并调整其面向物体的能力。
- 直接在重建出的度量 3D 空间中预测 3D 检测框，绕过常用的 2D 检测后提升至 3D（2D-to-3D lifting）的范式。
- 在多个基准上验证了在线性能和鲁棒的跨域迁移能力。

### 主要贡献
- 提出 Map-Det3D，将检测直接融入从 RGB 重建的 3D 空间中，避免 2D 到 3D 提升的脆弱性。
- 展示了将重建先验训练用于检测是获得单目视频稳定度量 3D 检测的实用路径。
- 验证了该设计在多个基准上的强在线性能及无需适应的鲁棒迁移能力，并开源代码与模型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目 3D 检测中尺度欠约束的核心难题，提出了一种新颖的“重建-检测”一体化范式，且实验显示跨域迁移能力强，对面向具身智能的视觉感知研究具有较高参考价值。摘要中虽未给出定量结果细节，但问题动机清晰、方法路径创新，建议优先精读。

</details>

<details>
<summary>Abstract</summary>

Metric 3D object detection is a core capability for embodied agents, yet most reliable systems lean on depth sensors, trading away cost, power, and integration simplicity. This motivates monocular 3D detection, which avoids additional constraints, yet it faces a major obstacle: from a single image, depth, and especially absolute scale, are underconstrained. As a result, the prevailing pattern of detecting in 2D and then predicting 3D attributes is often brittle, since modest range errors can dominate 3D localization, and the learned scale prior can fail when cameras, motion, or environments undergo domain shifts. To address this, we propose Map-Det3D, an online multi-view 3D object detection model that brings detection directly into a 3D space reconstructed from RGB. We map a short temporal window into multiple views and repurpose a feed-forward metric 3D reconstruction model as our geometric backbone while tuning its object-aware capabilities. Building on this representation, Map-Det3D directly predicts boxes in metric 3D space, without the widely used 2D-to-3D lifting. Experiments across different benchmarks show that this design supports strong online performance and robust transfer without adaptation, suggesting that training reconstruction priors for detection is a practical route to stable metric 3D detection from monocular video. Code and models are available at https://royyang0714.github.io/Map-Det3D.

</details>

## Dynamic / 4D Reconstruction

### 2026-08

#### 2026-08-18 - UniQuery4R: Unified 4D Scene Reconstruction from a Single Query

**Authors:** Tiancheng Chen, Sheng Tang, Wenhua Jin, Weiqi Zhang, Juntong Fang, Junsheng Zhou, Zesong Li
**Links:** [abs](https://arxiv.org/abs/2608.17283) - [pdf](https://arxiv.org/pdf/2608.17283)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** dynamic 4D, scene flow, scene reconstruction, dense reconstruction

<details>
<summary>Abstract</summary>

Reconstructing dynamic 4D scenes requires jointly estimating correspondence, geometry, object motion, and camera motion. Existing feed-forward methods typically predict dense task-specific maps or independently process source-target pairs, leading to unnecessary computation for sparse queries and limited feature reuse across different frame pairs. We present UniQuery4R, a query-conditioned framework that encodes a multi-frame clip once and selects the source view, target view, and continuous source-image coordinate only at decoding time via source-to-target cross-attention. Each query jointly predicts target correspondence, target-time 3D position, and scene flow, along with source depth, while camera parameters are estimated per view. This design allows the encoded clip to be reused across arbitrary source-target selections and supports both sparse inference and dense reconstruction through batched queries, without learned temporal embeddings tied to a fixed clip length. We further introduce a direction-magnitude parameterization of scene flow with separate supervision for moving and static points. Among the evaluated methods, UniQuery4R achieves the best macro-average results on WorldTrack for both scene-flow estimation and dynamic-point reconstruction.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-08

#### 2026-08-18 - Initialization-Free Bundle Adjustment Revisited: A Controlled Experimental Study

**Authors:** Simon Weber, Mateo de Mayo, Je Hyeong Hong, Carl Olsson, Daniel Cremers, Ronald Clark
**Links:** [abs](https://arxiv.org/abs/2608.18028) - [pdf](https://arxiv.org/pdf/2608.18028)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, bundle adjustment

<details>
<summary>Abstract</summary>

Initialization-free bundle adjustment (InitFree BA) aims to recover camera poses and scene structure directly from image observations, avoiding the geometric initialization stages of conventional structure-from-motion pipelines. Recent methods based on Object-Space Error (OSE) formulations and Variable Projection (VarPro) show encouraging optimization behavior from random camera configurations. However, existing evaluations primarily measure optimization success, leaving unclear whether a low OSE objective yields a valid metric 3D reconstruction. We revisit InitFree BA experimentally through a unified evaluation framework combining a C++ implementation of existing OSE formulations with a Blender-based dataset generator providing exact ground truth and controlled camera configurations and observation densities. Our experiments reveal a previously overlooked optimization--reconstruction gap: projective solutions with similarly low OSE values can lead to substantially different Euclidean reconstructions after metric upgrade. We identify initialization priors, landmark observation density, and metric-upgrade stability as key factors governing reconstruction success. Overall, our results suggest that the main challenge of InitFree BA is not merely minimizing OSE objectives, but obtaining projective reconstructions that admit reliable metric upgrade. We believe that the proposed benchmark, implementation, and analysis establish stronger experimental foundations for future research on initialization-free bundle adjustment, a problem largely unexplored within the computer vision community. Project page is available at https://github.com/simonwebertum/InitFreeBA.git.

</details>

#### 2026-08-18 - Scalix: Uncertainty-Aware Scale-Consistent Monocular SLAM

**Authors:** Sebastian Barbas Laina, Tianyi Zhang, Panagiotis Petropoulakis, Simon Schaefer, Simon Boche, Jaehyung Jung, Cedric Le Gentil, Stefan Leutenegger
**Links:** [abs](https://arxiv.org/abs/2608.17553) - [pdf](https://arxiv.org/pdf/2608.17553)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, monocular depth, robotics

<details>
<summary>Abstract</summary>

Cameras are ubiquitous sensors in robotics due to their compact form factor and the perceptual richness captured through visual information. Monocular SLAM enables robots to understand the environment with a minimum setup, however, it inherently suffers from scale ambiguity. A common solution is to provide multi-modal sensor configurations, such as visual-inertial systems, where scale is observable unless the robot navigates under a constant-velocity motion, a common scenario in mobile robotics. With the advent of deep-learning, geometric foundation models have been used to address this problem, but the depths maps are often noisy and scale-inconsistent across frames. In this paper, we propose Scalix, a real-time monocular SLAM framework that achieves metric-scale state estimation by integrating learned depth cues into a probabilistic factor-graph formulation. By augmenting existing monocular depth models with both per-pixel depth uncertainty and per-frame scale uncertainty, Scalix treats scale predictions as independent measurements within its optimization, leading to improved scale consistency through multi-view data associations. Experiments in large-scale outdoor and indoor environments demonstrate state-of-the-art performance on both metric and up-to-scale benchmarks while maintaining real-time operation and generalization.

</details>

#### 2026-08-18 - GeoWeaver: Accurate Long-Sequence 3D Reconstruction via Hierarchical Geometric Assembly

**Authors:** Tinghao Jiang, Sheng Tang, Shengzhe Wei, Juntong Fang, Weiqi Zhang, Junsheng Zhou, Zesong Li
**Links:** [abs](https://arxiv.org/abs/2608.17389) - [pdf](https://arxiv.org/pdf/2608.17389)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>Abstract</summary>

Long-sequence 3D reconstruction from RGB videos requires both accurate local geometry and globally consistent camera motion. Feed-forward models provide strong depth and pose predictions, but their memory cost prevents joint inference over long sequences. Chunk-wise processing improves scalability, yet independently predicted chunks often exhibit scale drift, pose errors, and point-cloud misalignment. We present GeoWeaver, a unified framework comprising a Geometric Prior Model (GPM) and Test-Time Adaptation (TTA). The GPM predicts chunk-wise depth, confidence, and camera parameters as adjustable geometric priors. TTA then performs sequential initialization, global chunk-level Sim(3) alignment, and coarse-to-fine refinement of camera poses, affine depth corrections, and intrinsics. Dense correspondences provide adjacent, cross-chunk, and long-range constraints, while a robust CDF-style objective jointly optimizes weighted 2D reprojection and 3D consistency residuals. This design preserves local geometric accuracy while correcting accumulated pose, scale, depth, and calibration errors. Experiments across diverse long-sequence benchmarks demonstrate improved camera accuracy, global consistency, and point-cloud quality. Ablations verify the contribution of each adaptation stage, and applying the same TTA procedure to different geometric prior models consistently improves their trajectory estimates, demonstrating that GeoWeaver is not tied to a specific GPM.

</details>

#### 2026-08-17 - PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation

**Authors:** Zhiyuan Yuan, Guanying Chen, Lingteng Qiu, Ruimao Zhang, Shuguang Cui, Xiaochun Cao
**Links:** [abs](https://arxiv.org/abs/2608.16984) - [pdf](https://arxiv.org/pdf/2608.16984)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, depth estimation, monocular depth

<details>
<summary>Abstract</summary>

Recent monocular depth estimators achieve strong zero-shot generalization, yet often struggle to preserve fine-grained structures and object boundaries. We attribute this limitation to the prevalent combination of large-patch ViT encoders and convolutional decoders, as coarse tokenization can weaken pixel-level cues that upsampling cannot fully recover. To address this issue, we propose PXDepth, a discriminative monocular depth model that separates global context modeling from pixel-level depth prediction. Specifically, a large-patch ViT captures global scene context, while a pixel-space predictor composed of Context-Modulated Pixel Transformer blocks maintains high-resolution spatial representations throughout depth estimation. This design preserves fine structures and sharp boundaries without sacrificing global depth consistency. Across diverse zero-shot benchmarks, PXDepth combines faithful local geometry with competitive global depth accuracy while remaining efficient at inference. Our code and model are available at https://yuanzhy29.github.io/PXDepth-Page/.

</details>

#### 2026-08-17 - Binarized High-Efficiency RAW Video Restoration and Beyond

**Authors:** Tianyu Zhu, Ying Fu, Hesong Li, Gengchen Zhang, Xin Yuan, Yulun Zhang
**Links:** [abs](https://arxiv.org/abs/2608.16756) - [pdf](https://arxiv.org/pdf/2608.16756)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Binarized High-Efficiency RAW Video Restoration and Beyond
- 作者：Tianyu Zhu, Ying Fu, Hesong Li, Gengchen Zhang, Xin Yuan, Yulun Zhang
- 出版日期：2026-08-17T16:03:50Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.16756

### 一句话总结
本文提出BinRVR，一种面向RAW视频恢复的二值化神经网络框架，在降低约96%计算量和参数量的同时，仅带来约4%的性能损失，并支持多比特量化以实现精度与效率的灵活权衡。

### 研究问题
二值化神经网络（BNNs）虽能实现轻量级高效部署，但在视频场景下对时序连贯性和激活值分布的建模能力不足，导致RAW视频恢复任务中性能受限。

### 核心思路/方法
- 提出二值化信息交互模块（BIIM），以统一且高效的方式联合建模空间与时间信息。
- 开发分布感知二值化卷积（DAB-Conv），利用全精度激活值的统计信息来缓解量化误差。
- 框架支持多比特量化，可在不同硬件约束下灵活调整精度与效率。

### 主要贡献
- 首次提出针对RAW视频恢复的二值化框架BinRVR，大幅降低计算与参数量（约96%）的同时仅损失约4%性能。
- 设计BIIM模块，有效解决二值化模型在视频场景中的时序建模问题。
- 提出DAB-Conv，利用激活值分布统计信息减少量化误差。
- 支持多比特量化，提供精度-效率的灵活权衡。
- 在低光增强、去噪、去模糊和超分辨率等多个RAW视频恢复任务上验证了方法的有效性，并探索了在下游任务（目标检测、单目深度估计）上的潜力。

### 局限性
摘要未提供足够信息，例如：未提及与其他非二值化方法的具体性能对比细节、未给出不同比特量化下的具体精度/效率数值、未讨论方法的训练成本或推理速度实测数据。

### 阅读优先级
**高**
理由：该工作针对RAW视频恢复这一基础性重要任务，提出高压缩率的二值化方案，同时兼顾性能与效率，且覆盖多种恢复任务及下游应用，对于关注轻量化视频处理和模型部署的研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

RAW video restoration is fundamental to high-quality low-level perception and serves as the basis for a wide range of downstream vision applications. While binary neural networks (BNNs) enable efficient lightweight deployment for image enhancement, their deficiencies in modeling temporal coherence and activation value distributions hinder their effectiveness when applied to video scenarios. In this paper, we propose BinRVR, a binarized RAW video restoration framework that reduces computation and parameters by approximately 96% while incurring only about 4% performance degradation. Specifically, we present a Binarized Information Interaction Module (BIIM) to jointly model spatial and temporal information in an efficient and unified manner. Moreover, we develop a Distribution-Aware Binarized Convolution (DAB-Conv) that leverages the statistics of full-precision activations to mitigate quantization errors. The proposed framework further supports multi-bit quantization, enabling flexible accuracy-efficiency trade-offs across different hardware constraints. Extensive experiments demonstrate that our BinRVR achieves competitive performance compared with state-of-the-art binarized methods on RAW video restoration tasks, including low-light enhancement, denoising, deblurring, and super-resolution. We further explore the potential of our method on downstream video applications, including object detection and monocular depth estimation.

</details>

#### 2026-08-15 - TinyDETR-Pose: Towards End-to-End Real-Time Single-Stage 6DoF Object Pose Estimation with Lightweight Transformers

**Authors:** Paul Julius Kühn, Duc Anh Nguyen, Saptarshi Neil Sinha, Michael Weinmann, Arjan Kuijper
**Links:** [abs](https://arxiv.org/abs/2608.15297) - [pdf](https://arxiv.org/pdf/2608.15297)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TinyDETR-Pose: Towards End-to-End Real-Time Single-Stage 6DoF Object Pose Estimation with Lightweight Transformers
- 作者：Paul Julius Kühn, Duc Anh Nguyen, Saptarshi Neil Sinha, Michael Weinmann, Arjan Kuijper
- 出版日期：2026-08-15
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.15297

### 一句话总结
本文提出TinyDETR-Pose，一种基于轻量级Transformer的端到端单阶段6DoF物体位姿估计框架，在边缘设备上实现了实时推理与准确预测的平衡。

### 研究问题
如何在资源受限的硬件上实现实时且准确的6DoF物体位姿估计，同时避免依赖非可微的PnP/RANSAC、迭代精化或高成本的基础模型推理。

### 核心思路/方法
- 基于高效LW-DETR架构，将检测与位姿估计建模为集合预测问题，单次前向传播同时完成物体检测和6D位姿回归。
- 为每个解码器查询附加专用MLP头，分别回归旋转、单目深度和投影物体中心，无需PnP、NMS或迭代精化。
- 使用ADD-S损失统一处理所有物体的对称性，无需针对物体特定损失调度或额外的测地线/ADD监督。
- 采用基于类别和2D空间线索的对称安全匈牙利匹配器进行预测与真值分配，在对称性和深度模糊情况下保持稳定匹配。

### 主要贡献
- 提出轻量级端到端单阶段6DoF位姿估计框架TinyDETR-Pose，无需PnP、NMS和迭代精化。
- 在YCB-V数据集上达到85.9的ADD-S AUC，与现有方法相当。
- 相比其他基于DETR的单阶段位姿估计方法，参数量最多减少72.7%。
- 在NVIDIA Jetson Nano上使用TensorRT实现约4.5毫秒/帧的推理延迟，证明Transformer-based位姿估计可在边缘设备实时运行。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法的失败模式、对遮挡或纹理缺失物体的鲁棒性、多物体场景下的性能、训练数据需求或与其他非DETR基线方法的详细对比。

### 阅读优先级
**高**。理由：该工作针对资源受限边缘设备上的实时6DoF位姿估计这一实际痛点，提出无需PnP/NMS的精简端到端Transformer方案，在准确率与效率之间取得良好平衡，并给出了具体硬件上的延迟验证，对部署导向研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-time 6DoF object pose estimation on resource-constrained hardware remains challenging, as accurate correspondence-based and refinement pipelines typically rely on non-differentiable PnP/RANSAC stages or costly iterative refinement, while recent foundation-model-based approaches incur inference costs that are prohibitive for edge deployment. We present TinyDETR-Pose, a lightweight, end-to-end, single-stage framework that jointly detects objects and regresses their full 6D pose in a single forward pass. Built on the efficient LW-DETR architecture, TinyDETR-Pose formulates detection and pose estimation as a set-prediction problem and attaches dedicated MLP heads for rotation, monocular depth, and projected object center regression to each decoder query, eliminating the need for PnP, NMS (non-maximum suppression), or iterative pose refinement. Object symmetries are handled through a ADD-S loss applied uniformly to all objects, without the need for object-specific loss schedules or separate geodesic/ADD supervision. In addition, predictions are assigned to ground truth using a symmetry-safe Hungarian matcher based on class and 2D spatial cues, yielding stable assignment under symmetry and depth ambiguity. On YCB-V, TinyDETR-Pose achieves a comparable ADD-S AUC of 85.9, while requiring up to 72.7% fewer parameters than other DETR-based single-stage pose-estimation approaches. Due to its compact design, TinyDETR-Pose runs in real time and achieves an inference latency of only ~4.5 ms per frame on an NVIDIA Jetson Nano using TensorRT, demonstrating that accurate end-to-end transformer-based 6D pose estimation can be made practical for edge deployment.

</details>

#### 2026-08-15 - Robust structure from motion for aerial-ground images via detector-free feature matching and multi-view track refinement

**Authors:** San Jiang, Hui Wang, Xing Zhang, Zhongwen Hu, Zhijun Wang, Ruisheng Wang, Wanshou Jiang, Qingquan Li
**Links:** [abs](https://arxiv.org/abs/2608.15251) - [pdf](https://arxiv.org/pdf/2608.15251)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robust structure from motion for aerial-ground images via detector-free feature matching and multi-view track refinement
- 作者：San Jiang, Hui Wang, Xing Zhang, Zhongwen Hu, Zhijun Wang, Ruisheng Wang, Wanshou Jiang, Qingquan Li
- 出版日期：2026-08-15
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.15251

### 一句话总结
本文提出一种结合旋转变换鲁棒的免检测器特征匹配网络与多视角轨迹优化的增量式运动恢复结构（ISfM）方法，用于提升空地影像集成三维重建的精度。

### 研究问题
空地影像因视点、尺度和旋转差异显著，导致特征匹配困难，进而影响运动恢复结构（SfM）的鲁棒性和重建精度。本文旨在解决这一条件下的特征匹配与多视角轨迹稳定性问题。

### 核心思路/方法
本文提出一个包含四个关键模块的ISfM工作流：
1. **旋转感知特征提取**：用全向状态空间块（OSS Block）替代传统卷积，在八个对称方向上进行选择性扫描，以建模长程空间依赖并生成旋转不变特征图。
2. **多尺度注意力变换**：利用四叉树注意力构建层次化令牌金字塔，隔离高关联令牌区域并丢弃无关区域，以线性计算复杂度捕获长程上下文。
3. **双向特征匹配**：执行对称的从粗到细匹配方案，粗对齐阶段在互近邻约束下计算双向Softmax置信度矩阵，细对齐阶段用多层感知机回归亚像素坐标偏移。
4. **多视角轨迹优化**：采用集成索引结构评估局部空间邻近性，将不相交的子轨迹连接到最高置信度锚点，确保特征在ISfM管线中的稳定可重复性。

### 主要贡献
- 提出旋转鲁棒的免检测器匹配网络，整合了旋转感知特征提取、多尺度注意力变换与双向粗到细匹配机制。
- 引入多视角轨迹优化模块，提升ISfM中特征轨迹的稳定性。
- 在真实空地影像数据集上，与LoFTR相比，该方法在5°位姿误差下的AUC提升了93.9%，并在ISfM重建中取得最高精度，精度提升范围为27.6%至32.7%。

### 局限性
摘要未提供足够信息（例如计算成本、对极端场景的适应能力、失败案例分析等均未提及）。

### 阅读优先级
**高**。理由：该工作针对空地影像集成三维重建中的核心难点（视角、尺度、旋转变化）提出系统性解决方案，并在公开数据集上取得显著精度提升；其旋转鲁棒匹配与轨迹优化思路对SfM和三维重建方向研究者具有直接参考价值，且发表在arXiv近期论文中，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Integrated 3D reconstruction from aerial-ground images is essential for generating high-precision urban 3D models, yet severe variations in viewpoint, scale, and rotation make robust feature matching highly challenging. To address these limitations, this study introduces a rotation-robust detector-free matching network coupled with multi-view track refinement for incremental Structure from Motion (ISfM). The proposed workflow features four key modules. First, rotation-aware feature extraction replaces traditional convolutions with an Omnidirectional State Space Block (OSS Block) that selectively scans across eight symmetrical directions to model long-range spatial dependencies and synthesize rotation-invariant feature maps. Second, multi-scale attention transformation utilizes quadtree attention to build a hierarchical token pyramid that isolates high-association token regions and discards irrelevant areas, capturing long-range context with linear computational complexity. Third, bi-directional feature matching executes a symmetric coarse-to-fine matching scheme where coarse alignment computes dual-direction Softmax confidence matrices under mutual nearest neighbor constraints, and fine alignment uses a multi-layer perceptron to regress sub-pixel coordinate offsets. Finally, multi-view track refinement employs an integrated indexing structure to evaluate localized spatial proximity and link disjoint sub-tracks to the highest-confidence anchor point, ensuring stable feature repeatability across the ISfM pipeline. By using real aerial-ground datasets, experimental results demonstrate that the proposed method improves AUC at 5° pose error by 93.9% compared with LoFTR and achieves the highest precision in ISfM reconstruction, with the improved accuracy ranging from 27.6% to 32.7%. The proposed method provides a reliable solution for integrated 3D reconstruction of aerial-ground images.

</details>

#### 2026-08-13 - A Controlled Study of Self-Supervised Image and Video Pretraining under Limited Resources

**Authors:** Brunó B. Englert, Gijs Dubbelman
**Links:** [abs](https://arxiv.org/abs/2608.13183) - [pdf](https://arxiv.org/pdf/2608.13183)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Controlled Study of Self-Supervised Image and Video Pretraining under Limited Resources
- 作者：Brunó B. Englert、Gijs Dubbelman
- 出版日期：2026-08-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.13183

### 一句话总结
本文在受控资源条件下对比了多种图像与视频自监督学习目标，发现DINOv2风格预训练综合表现最佳，且将其与视频目标（如VideoMAE）结合会在语义任务上带来提升、但在几何任务上造成退化。

### 研究问题
在资源受限（数据、架构、计算预算均匹配）的情况下，图像与视频自监督学习（SSL）目标如何表现？不同SSL目标（对比、重建、特征预测、扩散）之间是否存在性能差异？联合训练图像-视频SSL目标是否能产生优于单一目标的效果？

### 核心思路/方法
作者在匹配的数据、架构和计算预算条件下，对图像与视频SSL目标进行受控对照研究。比较了对比学习（contrastive）、重建（reconstruction）、特征预测（feature-prediction）和扩散（diffusion）四类目标，并评估了单独训练以及联合训练的图像-视频SSL组合，在一系列图像与视频理解任务上进行评测。

### 主要贡献
- 在受控资源条件下系统对比了多种图像和视频SSL目标，填补了该场景下的比较空白。
- 发现DINOv2风格预训练在有限资源下综合性能最优。
- 揭示图像SSL（DINOv2）与视频SSL（如VideoMAE）联合训练可提升图像分类和分割性能，但会损害视频跟踪和相机位姿估计性能，表明语义表示与几何表示学习之间存在权衡。

### 局限性
摘要未提供足够信息，如具体数据集、模型规模、训练时长、评测任务细节及定量结果等均未给出。

### 阅读优先级
**中**。理由：该研究针对资源受限场景下的SSL目标比较具有实用价值，且揭示了联合训练带来的语义-几何权衡这一有意义的发现；但作者未提供定量实验细节，结论的普适性和可复现性无法从摘要评估，适合对SSL预训练策略感兴趣的读者阅读原文获取具体数据。

</details>

<details>
<summary>Abstract</summary>

Visual foundation models are a cornerstone of image and video understanding but typically require large amounts of data and computation. The current scale required for pretraining visual foundation models may be unsustainable or unnecessary, and significant benefits arise when effective models can be obtained with fewer resources. To better understand how self-supervised learning (SSL) objectives behave under resource constraints, we conduct a controlled study of image and video SSL objectives under matched data, architecture, and compute budgets. We compare contrastive, reconstruction, feature-prediction, and diffusion objectives and evaluate both standalone and jointly trained image-video SSL formulations across a diverse set of image and video understanding tasks. Our results show that DINOv2-style pretraining consistently provides the strongest overall performance under limited resources. Furthermore, combining DINOv2 with video SSL objectives such as VideoMAE substantially improves image classification and segmentation performance, but degrades video tracking and camera-pose estimation performance, revealing an important tradeoff between semantic and geometric representation learning. These findings suggest that combining image and video SSL objectives can be beneficial in resource-limited settings, while highlighting the need for improved methods that better balance semantic, temporal, and geometric supervision.

</details>

#### 2026-08-13 - Fast Iterative Five point Relative Pose Estimation

**Authors:** Johan Hedborg, Michael Felsberg
**Links:** [abs](https://arxiv.org/abs/2608.13114) - [pdf](https://arxiv.org/pdf/2608.13114)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fast Iterative Five point Relative Pose Estimation
- 作者：Johan Hedborg, Michael Felsberg
- 出版日期：2026-08-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.13114

### 一句话总结
本文提出一种基于Powell's Dog Leg算法的快速迭代式五点相对位姿估计方法，在精度与Nister算法相当的情况下，速度约为其两倍。

### 研究问题
如何加速五点法相对位姿估计，同时保持与当前最先进方法相当的精度，并使其易于扩展至多于五个点的情形。

### 核心思路/方法
- 提出一种新的迭代方法，基于Powell's Dog Leg算法（一种非线性优化方法）。
- 该方法在RANSAC框架下使用，具备与Nister五点法相同的精度，但速度约为其两倍。
- 方法易于扩展到多于五个点的情况，同时保持高效的误差度量，因此也适合作为细化（refinement）步骤。
- 在三种具有已知真值的数据集上进行了系统评估。

### 主要贡献
1. 提出一种新的快速迭代式五点相对位姿估计算法。
2. 在精度不降低的前提下，速度约为Nister算法的两倍。
3. 算法可自然扩展至超过五个点，适合作为位姿细化步骤。
4. 在三种已知真值的数据集上进行了系统评估，验证了方法的有效性。

### 局限性
摘要未提供足够信息（例如：未提及方法对噪声、离群点的具体鲁棒性表现，未给出具体数据集类型与规模，也未说明与Nister算法以外的其他方法（如七点法、八点法）的比较情况）。

### 阅读优先级
**中**
理由：该工作针对经典五点相对位姿估计问题提出性能改进，方向明确且速度提升显著，对从事三维重建、多视图几何的读者有一定参考价值。但摘要仅提供了性能对比的高层结论，缺乏具体的实验数值和评估细节，适合作为速读参考，而非必读精读文献。

</details>

<details>
<summary>Abstract</summary>

Robust estimation of the relative pose between two cameras is a fundamental part of Structure and Motion methods. For calibrated cameras, the five point method together with a robust estimator such as RANSAC gives the best result in most cases. The current state-of-the-art method for solving the relative pose problem from five points is due to Nister [9], because it is faster than other methods and in the RANSAC scheme one can improve precision by increasing the number of iterations. In this paper, we propose a new iterative method, which is based on Powell's Dog Leg algorithm. The new method has the same precision and is approximately twice as fast as Nister's algorithm. The proposed method is easily extended to more than five points while retaining a efficient error metrics. This makes it also very suitable as an refinement step. The proposed algorithm is systematically evaluated on three types of datasets with known ground truth.

</details>

#### 2026-08-13 - Topology-Unified 2D Pose Estimation across Intact, Residual and Prosthetic Limbs

**Authors:** Tianye Qi, Tengyue Zhang, Jiaying Ying, Tianqing Zhu, Xin Yu
**Links:** [abs](https://arxiv.org/abs/2608.13047) - [pdf](https://arxiv.org/pdf/2608.13047)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Topology-Unified 2D Pose Estimation across Intact, Residual and Prosthetic Limbs
- 作者：Tianye Qi, Tengyue Zhang, Jiaying Ying, Tianqing Zhu, Xin Yu
- 出版日期：2026-08-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.13047

### 一句话总结
本文提出统一拓扑表示的ProPose基准和结构感知的ProLoss损失函数，以改善包含健全肢体、义肢和残肢的人体姿态估计性能。

### 研究问题
现有主流人体姿态估计数据集存在严重的表示偏差，主要面向健全人，对义肢（如跑步刀片）和未安装假肢的残肢缺乏统一的标注协议，导致模型在这些多样化肢体形态上难以泛化，且长尾分布下关节分类精度不足。

### 核心思路/方法
1. 提出**ProPose**基准：设计一种新型标注协议，在单一框架内统一生物学肢体、多种义肢和物理缺失肢体的拓扑表示。
2. 设计**Real-to-Synthetic数据扩充管道**：针对真实义肢图像稀缺且呈极端长尾分布的问题，显式合成并扩充该类样本。
3. 提出**ProLoss**损失函数：结构感知目标函数，强制同一肢体内部关键点之间的依赖关系，防止模型在机械结构上幻觉出不存在的关节。

### 主要贡献
- 引入大规模基准ProPose，首次在统一拓扑框架下覆盖健全、残肢与义肢场景。
- 提出Real-to-Synthetic数据扩充策略，缓解义肢数据的极端长尾问题。
- 设计ProLoss结构感知损失，约束关键点间依赖关系，避免不真实预测。
- 实验表明，在不损失坐标定位精度的前提下，长尾义肢关节分类准确率提升2%至6%。

### 局限性
摘要未提供足够信息。具体而言，关于ProPose数据集的规模与构成细节、各方法的消融实验对比、具体实验设置（如backbone、训练配置）以及在不同下游任务上的泛化验证等均未在摘要中提及。

### 阅读优先级
**中**。理由：该工作面向人体姿态估计中的包容性/公平性研究，属于较细分的进阶方向，当前可能不是通用姿态估计领域的主流热点；但问题定义清晰、方法具有工程创新性，且摘要中的量化提升明确，适合研究义肢场景或关注数据长尾问题的读者参考。

</details>

<details>
<summary>Abstract</summary>

Driven by the availability of large-scale datasets, Human Pose Estimation (HPE) plays a critical role in numerous downstream tasks. However, mainstream benchmarks exhibit severe representation bias, predominantly featuring able-bodied individuals. While a few pioneering datasets have attempted to address limb differences, their annotation protocols fail to generalize, struggling to represent specialized mechanical structures like running blades or unprosthetized residual limbs. To bridge this gap, we introduce ProPose, a large-scale benchmark featuring a novel annotation protocol that unifies the topological representation of biological limbs, diverse prostheses, and physical absences within a single framework. Because real-world prosthetic images are inherently scarce and exhibit extreme long-tail distributions, we design a Real-to-Synthetic data expansion pipeline to explicitly synthesize and expand the underrepresented cases. However, simply training existing models on this enriched dataset often leads to suboptimal solutions, as they estimate each keypoint independently and might hallucinate non-existent joints on mechanical structures. To resolve this, we propose ProLoss, a structure-aware objective that enforces keypoint dependencies within a single limb to prevent unrealistic limb predictions. Extensive experiments demonstrate that our approach improves the classification accuracy of long-tail prosthetic joints by 2% to 6% without compromising spatial coordinate localization performance. This work sets a foundation for inclusive pose estimation, unlocking new possibilities for understanding the interactions between human bodies and assistive devices.

</details>

#### 2026-08-13 - AMR-Pose: An Active LED Marker-Based Relative Pose Estimation Framework With Probabilistic Switching PnP for Cooperative AUVs

**Authors:** Zeyu Sha, Xiaorui Wang, Mingyang Yang, Feitian Zhang
**Links:** [abs](https://arxiv.org/abs/2608.12866) - [pdf](https://arxiv.org/pdf/2608.12866)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, robotics, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AMR-Pose: An Active LED Marker-Based Relative Pose Estimation Framework With Probabilistic Switching PnP for Cooperative AUVs
- 作者：Zeyu Sha, Xiaorui Wang, Mingyang Yang, Feitian Zhang
- 出版日期：2026-08-13T06:29:43Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.12866

### 一句话总结
本文提出AMR-Pose，一种基于主动LED标记与概率切换PnP的水下自主机器人（AUV）相对位姿估计框架，通过紧凑标记模块与自适应估计机制在复杂水下环境中实现稳健的六自由度相对定位。

### 研究问题
如何在存在浑浊、光照变化、反射和间歇性特征遮挡等严重光学退化条件下，实现合作AUV之间可靠、鲁棒的基于视觉的相对位姿估计。

### 核心思路/方法
- 设计一个紧凑的主动LED标记模块，包含一个红色中心LED和三个蓝色外围LED，安装在领航AUV上，以在复杂水下条件下提供独特的视觉特征。
- 基于检测到的标记观测，开发概率切换PnP估计器（PSwPnP），结合SE(3)上的李群位姿传播、概率标记关联和可见性自适应测量融合。
- 框架根据标记可见性动态调整估计过程，在部分观测和可见性切换期间保持几何一致性和时间稳定性。

### 主要贡献
- 提出AMR-Pose框架，基于主动LED标记实现水下合作AUV的相对位姿估计。
- 开发紧凑的LED标记模块，提供水下复杂环境中可辨识的视觉特征。
- 设计概率切换PnP估计器（PSwPnP），融合李群位姿传播、概率关联与自适应融合。
- 通过水槽实验（运动捕捉系统提供真值）验证了框架在挑战性水下条件下的准确性、平滑性和鲁棒性。
- 闭环领航-跟随实验证明其在合作水下机器人实时相对位姿反馈中的可行性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作面向水下多机器人协作中的关键难题（光学退化下的相对定位），提出了结合主动标记设计与概率切换PnP的完整解决方案，并通过水槽真值实验和闭环实验验证了实用性。对于从事水下机器人、视觉定位或多机器人协同的研究人员具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Reliable relative pose estimation between autonomous underwater vehicles (AUVs) is critical for cooperative ocean exploration, sampling, and multi-robot coordination. However, achieving robust vision-based relative localization in underwater environments remains challenging due to severe optical degradation, including turbidity, illumination variations, reflections, and intermittent feature occlusions. This paper presents AMR-Pose, an active LED marker-based relative pose estimation framework for cooperative AUVs. A compact marker module consisting of one red central LED and three blue peripheral LEDs is developed and integrated onto the leader AUV to provide distinctive visual features under complex underwater conditions. Building upon the detected marker observations, a probabilistic switching Perspective-n-Point estimator (PSwPnP) is developed by combining Lie-group pose propagation on $SE(3)$, probabilistic marker association, and visibility-adaptive measurement fusion for robust six-degree-of-freedom relative pose estimation. The proposed framework dynamically adapts the estimation process according to marker visibility, maintaining geometric consistency and temporal stability during partial observations and visibility transitions. Extensive water-tank experiments with motion-capture ground truth validate that AMR-Pose achieves accurate, smooth, and robust relative pose estimation under challenging underwater conditions. Closed-loop leader-follower experiments further demonstrate its feasibility for real-time relative pose feedback in cooperative underwater robotics.

</details>

#### 2026-08-12 - MV2: Multi-View Multi-Vehicle Driving Dataset for Novel View Synthesis

**Authors:** Sanjay Bhargav Dharavath, Hanvitha Saraswathi Mukkamala, Faizan Farooq Khan, Ioannis Kakogeorgiou, Aditya Arun, C V Jawahar, Zakaria Laskar
**Links:** [abs](https://arxiv.org/abs/2608.12442) - [pdf](https://arxiv.org/pdf/2608.12442)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, camera pose estimation, pose estimation, novel view synthesis, view synthesis, differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MV2: Multi-View Multi-Vehicle Driving Dataset for Novel View Synthesis
- 作者：Sanjay Bhargav Dharavath, Hanvitha Saraswathi Mukkamala, Faizan Farooq Khan, Ioannis Kakogeorgiou, Aditya Arun, C V Jawahar, Zakaria Laskar
- 出版日期：2026-08-12T16:02:32Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：https://arxiv.org/abs/2608.12442

### 一句话总结
本文提出MV2数据集与基准，通过多车辆（汽车、摩托车、无人机）同步轨迹拍摄，评估新视角合成方法在动态城市场景中大幅视点变化下的性能。

### 研究问题
新视角合成在真实驾驶场景中因稀疏采集视角、动态物体和有限的多轨迹数据而难以应用，现有数据集多为单一轨迹，难以评估视点大幅变化下的模型表现。

### 核心思路/方法
构建MV2数据集：使用汽车、摩托车和无人机三台设备同步采集，各自沿不同但同步的轨迹行驶；训练时使用某一车辆的相机流，测试时换用另一车辆的相机流，从而引入大幅视点变化。所有序列通过Structure-from-Motion配准，并使用手动像素级对应标注验证相机位姿，最终得到50个高质量场景、12000张图像。在此基础上，对近期NVS方法和相机位姿估计方法进行基准测试。

### 主要贡献
- 提出MV2数据集，包含50个高质量场景、12000张图像，支持动态城市场景下大幅视点变化的NVS评估。
- 设计多车辆交叉轨迹的基准协议，使训练和测试视点差异显著大于现有单轨迹数据集。
- 通过基准测试发现：NVS性能随视点差异增大而下降；前馈位姿估计器明显落后于优化方法，验证了MV2作为驾驶NVS测试床的严格性。
- 公开数据集、基准协议及项目资源。

### 局限性
摘要未提供足够信息：未说明数据集在场景多样性（如天气、光照、交通密度）上的覆盖范围，也未提及与现有驾驶数据集的定量对比，或方法失败的典型案例分析。

### 阅读优先级
**中**。理由：该工作主要贡献在于新数据集与基准，对从事驾驶场景新视角合成或位姿估计的研究者有一定参考价值，但属于资源型工作而非新方法提出；若不在该领域，则关联度有限。

</details>

<details>
<summary>Abstract</summary>

Differentiable rendering has advanced novel view synthesis (NVS), yet applying it to real-world driving remains difficult due to sparse capture viewpoints, dynamic objects, and limited multi-trajectory data. We introduce the Multi-View Multi-Vehicle (MV2) dataset and benchmark for evaluating NVS models under large viewpoint changes in dynamic urban scenes. MV2 features synchronized captures from a car, scooter, and drone, each following distinct yet synchronized trajectories. Training NVS methods on one vehicle's camera stream and testing on another enables evaluation under substantially larger viewpoint variations than existing single-trajectory datasets. All sequences are registered via Structure-from-Motion and camera poses verified using manual pixel-level correspondence annotations, yielding 50 high-quality scenes with 12000 images. Benchmarking recent NVS and camera pose estimation methods shows that NVS performance degrades with increasing viewpoint disparity, and that feed-forward pose estimators notably lag behind optimization-based approaches, highlighting MV2 as a rigorous testbed for NVS in driving. The dataset, benchmark protocol, and project resources are available at https://mv2-dataset.github.io/.

</details>

#### 2026-08-12 - HSTGFormer: Hyper Spatial-Temporal Graph Transformer for 3D Human Pose Estimation

**Authors:** Ruochen Li, Shuang Chen, Wenke E, Farshad Arvin, Amir Atapour-Abarghouei
**Links:** [abs](https://arxiv.org/abs/2608.12187) - [pdf](https://arxiv.org/pdf/2608.12187)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HSTGFormer: Hyper Spatial-Temporal Graph Transformer for 3D Human Pose Estimation
- 作者：Ruochen Li, Shuang Chen, Wenke E, Farshad Arvin, Amir Atapour-Abarghouei
- 出版日期：2026-08-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.12187

### 一句话总结
本文提出一种图增强的Transformer框架HSTGFormer，通过超时空图将空间与时间推理耦合成局部图聚合，实现高效且精度高的单目3D人体姿态估计。

### 研究问题
现有基于Transformer的3D人体姿态估计方法通常将空间和时间推理分为两个独立阶段，这可能导致对动作中固有的统一时空依赖建模不足，并在时间建模之前压缩了帧级结构信息。本文旨在解决这一问题，构建更统一的时空关联推理方式。

### 核心思路/方法
- 提出**Hyper Spatial-Temporal Graph (HSTG)**：将每帧的骨架图扩展到时间邻域，将全局时空推理分解为围绕每个“关节点-时间”节点的局部时空感受野，实现结构感知的耦合推理，同时保留局部结构运动信息。
- 引入**Adaptive Dual-Scale Temporal Graph (ADSTG)**：在互补的短窗口和长窗口内捕获关节点特定的时间依赖。
- 设计轻量级的**节点级融合模块**：自适应地整合两种图表示，用于每个“关节点-时间”节点。

### 主要贡献
- 提出将时空推理重新表述为“关节点-时间”节点上的局部耦合图聚合，替代传统分离式时空建模。
- 设计HSTG实现局部结构感知的耦合时空推理，并保留局部结构运动信息。
- 引入ADSTG与节点级融合模块，增强跨尺度时间依赖建模。
- 在Human3.6M和MPI-INF-3DHP数据集上验证了强精度与高计算效率（摘要提供实验范围，具体数值未给出）。

### 局限性
摘要未提供足够信息，具体局限性（如对遮挡、极端姿态的鲁棒性、长序列效率等）未在摘要中说明。

### 阅读优先级
**高**  
理由：该工作针对3D人体姿态估计中时空建模分离的核心问题提出了统一的耦合图推理框架，并声称在主要基准上取得强精度与高效率，方法设计具有新意，对关注人体姿态估计和时空建模的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Transformer-based methods have achieved strong performance in monocular 3D human pose estimation, but most existing approaches organise spatial and temporal reasoning as separate stages, which may weaken unified spatial-temporal interdependencies inherent in human motion and compress frame-level structural information before temporal modelling. In this paper, we propose HSTGFormer, a graph-enhanced Transformer framework that reformulates spatial-temporal reasoning as localised coupled graph aggregation over joint-time nodes. Specifically, HSTGFormer introduces a Hyper Spatial-Temporal Graph (HSTG), which decomposes global spatial-temporal reasoning into local spatial-temporal receptive fields around individual joint-time nodes by extending per-frame skeleton graphs into temporal neighbourhoods, thereby enabling structure-aware coupled reasoning while preserving local structural motion information. It further incorporates an Adaptive Dual-Scale Temporal Graph (ADSTG) to capture joint-specific temporal dependencies over complementary short- and long-range windows. A lightweight node-wise fusion module further adaptively integrates the two graph representations for each joint-time node. Experiments on Human3.6M and MPI-INF-3DHP show that HSTGFormer achieves strong accuracy with high computational efficiency.

</details>

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-18 - GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation

**Authors:** Ming Qian, Zijian Wang, Minchao Sun, Jincheng Xiong, Hang Zhang, Mu Xu, Chi Wang, Baoquan Chen
**Links:** [abs](https://arxiv.org/abs/2608.17988) - [pdf](https://arxiv.org/pdf/2608.17988)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Many scalable latent 3D generators operate on structured tensors, whereas pre-optimized 3D Gaussian Splatting (3DGS) reconstructions are unordered, spatially irregular, and vary widely in primitive count. We present GS-Voxel, a fitting-free structured latent framework, and evaluate it for large-scale aerial 3D Gaussian scene generation. GS-Voxel deterministically converts a compatible pre-optimized 3DGS reconstruction into sparse active voxels without additional per-scene optimization, retaining the sub-voxel positions and rendering attributes of the selected primitives. A GS-specific factorized VAE then separately encodes voxel geometry and local Gaussian attributes into sparse 3D latents whose size grows with the number of occupied voxels rather than being limited by a fixed scene-wide primitive count. We train image-conditioned flow models in the GS-Voxel latent space to generate aerial 3DGS scenes. A key application enabled by GS-Voxel is large-area scene generation: overlap-aware tiled inference extends synthesis beyond a single training crop conditioned on satellite-view images. Our results show that GS-Voxel provides structured latents for pre-optimized aerial 3DGS reconstructions, with latent capacity that grows with the number of occupied voxels.

</details>

#### 2026-08-18 - MetaSapiens v2: Advancing Real-Time Foveated Neural Rendering via Foveation-Aware Pruning and Stereo Warping

**Authors:** Weikai Lin, Yu Feng
**Links:** [abs](https://arxiv.org/abs/2608.17969) - [pdf](https://arxiv.org/pdf/2608.17969)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural rendering, rendering, AR, VR

<details>
<summary>Abstract</summary>

Point-Based Neural Rendering (PBNR) is emerging as a promising class of rendering techniques, which are permeating all aspects of society, driven by a growing demand for real-time, photorealistic rendering in AR/VR and digital twins. However, achieving real-time PBNR on VR/AR devices is challenging. This paper proposes MetaSapiens v2, a PBNR system that delivers real-time neural rendering on VR/AR devices while maintaining human visual quality. MetaSapiens v2 combines four techniques. First, we present an efficiency-aware pruning technique to optimize rendering speed. Second, we introduce a Foveated Rendering (FR) method with an efficient primitive for PBNR, leveraging humans' low visual acuity in peripheral regions to relax rendering quality and improve rendering speed. Third, we leverage the redundancy between the two eyes and propose a selective warping method to further reduce the computation overhead in AR/VR binocular rendering. Finally, we propose an accelerator design for binocular FR, addressing the load imbalance issue in (FR-based) PBNR and supporting warping for efficient binocular rendering. Our evaluation shows that MetaSapiens v2 achieves an order of magnitude speedup over existing PBNR models while maintaining the visual quality.

</details>

#### 2026-08-18 - GenRec: Knowing Where to Reconstruct and Where to Generate

**Authors:** Ata Çelen, Jaewoo Jung, Federico Tombari, Marc Pollefeys, Sunghwan Hong, Michael Niemeyer, Daniel Barath
**Links:** [abs](https://arxiv.org/abs/2608.17832) - [pdf](https://arxiv.org/pdf/2608.17832)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** monocular depth, NeRF, novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Generative novel view synthesis from sparse input images is rarely all reconstruction or all generation: pixels visible in some source view have a unique correct value modulated only by view-dependent shading, while pixels in disocclusions or beyond the captured volume admit a distribution of plausible completions. Existing generative novel-view-synthesis methods conflate these regimes under a single uniform loss, blurring the line between geometric fidelity and creative hallucinations even when scene geometry is injected through warped point clouds or projected depth. We introduce GenRec, a multi-view flow matching model that builds the reconstruction--generation split directly into its architecture, supervision, and gradient flow. Guided by an observation mask derived from the source cameras and a monocular depth estimator, a flow matching backbone jointly denoises RGB and scene-coordinate maps across all target views, while a pixel-space refinement stage restores high-frequency detail on observed pixels; the same mask gates supervision so regression signals do not contaminate the generative prior. Across RealEstate10K, DL3DV-10K, and Mip-NeRF~360, in both single-view extrapolation and two-view interpolation, GenRec attains the best reconstruction fidelity in observed regions while also surpassing purely generative baselines on perceptual quality in unobserved ones, showing the effectiveness of our approach.

</details>

#### 2026-08-18 - Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds

**Authors:** Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl
**Links:** [abs](https://arxiv.org/abs/2608.17682) - [pdf](https://arxiv.org/pdf/2608.17682)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, scene representation, rendering, splatting

<details>
<summary>Abstract</summary>

Real-time novel view synthesis is dominated by rasterized explicit primitives. These projection-based pipelines provide high throughput but require specialized extensions for non-pinhole effects such as distortion, rolling shutter, and depth of field. Ray-based rendering expresses these effects naturally but is generally assumed too slow for competitive real-time rendering. We analyze the factors governing throughput in differentiable Voronoi ray tracing and identify traversal length, per-cell work, and memory locality as principal determinants. Guided by this, we introduce VoroTracing, which co-designs the scene representation, optimization, and GPU execution to reduce these costs. Compact octahedral appearance textures reduce memory traffic, while surface-concentrated opacity promotes early termination. The fixed-budget representation is optimized without pruning or densification and rendered with a GPU implementation designed for coherent traversal. On Mip-NeRF 360, VoroTracing renders at 623 FPS on an RTX 5090, providing $3.2\times$ the throughput of the fastest prior ray-based method and $2.8\times$ that of 3D Gaussian Splatting, while maintaining competitive reconstruction quality. Our renderer supports fisheye, rolling-shutter, motion-blur, and depth-of-field effects through ray generation and sampling, requiring no specialized rasterization. These results show that real-time throughput can be achieved with the flexibility of ray-based rendering. We release our source code, see https://research.zenseact.com/publications/vorotracing

</details>

#### 2026-08-18 - GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting

**Authors:** Qijian Tian, Zimeng Wu, Xuhong Wang, Lizhuang Ma, Xin Tan
**Links:** [abs](https://arxiv.org/abs/2608.17535) - [pdf](https://arxiv.org/pdf/2608.17535)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Simultaneously reconstructing and understanding 3D environments is essential for embodied agents. Toward this goal, feed-forward semantic 3D Gaussian Splatting (3DGS) efficiently constructs semantic scene representations from sparse multi-view observations. However, existing methods lack explicit instance discrimination and mainly support category- or phrase-based semantic queries. To this end, we propose GroupForward, an instance-grouped feed-forward Gaussian splatting model that reconstructs geometry, appearance, instance structure, and semantics from sparse, unposed, and uncalibrated multi-view images. Unlike existing methods that attach high-dimensional semantic features to each Gaussian, GroupForward learns compact instance embeddings that group Gaussians into cross-view consistent 3D instances, reformulating feed-forward semantic 3DGS from per-Gaussian semantic feature rendering to instance-level semantic aggregation and propagation. Building on these instance groups, we further propose a Referential Scene Reasoning Framework (RSRF) for complex 3D referring segmentation. RSRF constructs an instance-grouped 3D scene graph and retrieves candidate instances for a given referring expression. A vision-language model then reasons over structured instance evidence and multi-view observations to identify the referred instance among the candidates. RSRF thereby extends language interaction from simple semantic querying to complex referential scene reasoning. Experiments on semantic reconstruction and referential reasoning demonstrate the effectiveness of our instance-grouped reconstruction and reasoning framework.

</details>

#### 2026-08-18 - NGS-Marker: Robust Native Watermarking for 3D Gaussian Splatting

**Authors:** Hao Qin, Yukai Sun, Luyuan Chen, Mengxu Lu, Feng Zhang, Ming Kong, Zhenhong Du, Qiang Zhu
**Links:** [abs](https://arxiv.org/abs/2608.17447) - [pdf](https://arxiv.org/pdf/2608.17447)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

With the rapid development and adoption of 3D Gaussian Splatting (3DGS), the need for effective copyright protection has become increasingly critical. Existing watermarking techniques for 3DGS mainly focus on protecting rendered images via pre-trained decoders, leaving the underlying 3D Gaussian primitives vulnerable to misuse. In particular, they are ineffective against Partial Infringement, where an adversary extracts and reuses only a subset of Gaussians. In this paper, we propose NGS-Marker, a novel native watermarking framework for 3DGS. It integrates a jointly trained watermark injector and message decoder, and employs a gradientbased progressive injection strategy to ensure full-scene coverage. This enables robust ownership decoding from any local region. We further extend NGS-Marker with hybrid protection (combining native and indirect watermarks) and support for multimodal watermarking. Extensive experiments demonstrate that NGS-Marker effectively defends against partial infringement while offering practical flexibility for real-world deployment.

</details>

#### 2026-08-18 - SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering

**Authors:** Gen Li, Shu Han, Yun Xi Qiao, Hua Chen, Xuyang Dai, Bohan Li, Hao Zhao, Chaojian Li
**Links:** [abs](https://arxiv.org/abs/2608.17420) - [pdf](https://arxiv.org/pdf/2608.17420)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving, driving scene, simulation

<details>
<summary>Abstract</summary>

Driving scene reconstruction and rendering, especially with 3D Gaussian Splatting, has become an important component of autonomous driving simulation. However, rendered views often degrade under extrapolated ego trajectories and scene edits, producing blurry structures, temporal flicker, and foreground-background misalignment. Existing refinement methods are commonly designed for a specific setting, such as image-level novel-view repair or object-editing correction. In this paper, we introduce SPVC, a structured and panoptic video fixing framework for cross-dataset driving scene rendering. The name summarizes four design principles. (1) Structured fixing denotes the use of explicit spatial conditions, including camera pose, 3D bounding boxes, and HD maps, to guide the repair process and reduce uncontrolled hallucination. (2) Panoptic fixing refers to correcting both background rendering artifacts, such as distorted roads, buildings, and lanes, and foreground vehicle artifacts introduced by scene editing, such as inconsistent object appearance. (3) Video fixing means that the model operates on driving sequences rather than isolated frames, allowing temporal cues to be used during artifact correction. (4) Cross-dataset fixing means that a single shared network is trained and applied across multiple driving datasets, reducing the need for dataset-specific or scene-specific fixers. Concretely, we construct paired degraded-clean training data by simulating under-constrained 3DGS rendering and foreground vehicle insertion artifacts, and train a two-stage controllable video diffusion model that first addresses video-level appearance and then refines scene layout with structured controls.

</details>

#### 2026-08-18 - Scanline-Aware Animatable Gaussian Avatars from Rolling-Shutter Videos

**Authors:** Youxiang Wang
**Links:** [abs](https://arxiv.org/abs/2608.17314) - [pdf](https://arxiv.org/pdf/2608.17314)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Animatable human avatars are routinely reconstructed from multi-view video under a silent assumption: that every pixel of a frame observes the same instant of the body's motion. Rolling-shutter (RS) sensors expose image rows sequentially, so within one frame the head and the feet of a moving person are separated by tens of milliseconds of articulated motion, and every scanline sees a different pose. Feeding such video to a state-of-the-art avatar bakes the distortion into the canonical representation, where it survives as shear and wobble under novel views and novel poses. Worse, every camera in a rig follows its own readout schedule, so the multi-view consistency that drives the reconstruction is violated even when the geometry is correct. We present RS-Avatar, which reconstructs a sharp, undistorted, animatable 3D Gaussian avatar directly from RS video. The formulation is minimal: a motion-aware avatar already renders the body at several sub-frame instants, and where a blur model averages those renderings, a rolling-shutter model composites them scanline by scanline. Changing that operator is the only modification required. On RS-ZJU, a benchmark we build from ZJU-MoCap, this improves novel-view synthesis over training as if the frames were instantaneous, on every subject. A motion-aware blur model built on the same sub-frame machinery does not transfer, and in fact falls below the shutter-oblivious baseline: the machinery is reusable, the operator is not.

</details>

#### 2026-08-18 - 3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation

**Authors:** Laurent Vit, Oliver Batchelor, Richard Green
**Links:** [abs](https://arxiv.org/abs/2608.17298) - [pdf](https://arxiv.org/pdf/2608.17298)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has made Gaussian primitives a highly efficient representation for real-time novel view synthesis, but its rasterisation-based formulation relies on screen-space approximations that limit accurate view-dependent ordering and the integration of secondary ray effects such as reflections, refractions, and shadows. Gaussian ray tracing addresses these limitations by evaluating explicit ray-primitive intersections, yet it remains costly to train. We observe that the main bottleneck is not ray traversal alone, but the pixel-centric backward propagation, where many threads concurrently accumulate gradients into the same primitive parameters, causing severe atomic contention and thread serialisation. We present 3DGART, a practical training framework for ray-traced Gaussian rendering. Our key idea is to reorganise backward propagation around primitives rather than pixels. Using conservative perspective-correct screen-space bounds, we build a compact intermediate buffer and a tile-primitive mapping that allows each thread to accumulate the contribution of one primitive over its covered pixels within a tile. This transforms gradient computation from a contention-heavy scatter operation into a structured gather-like process. On Mip-NeRF 360, 3DGART achieves an $\approx 3-3.5\times$ raw training speedup over per-pixel baseline and $\approx4 \times$ over 3DGRT on Mip-NeRF 360 while improving quality. More importantly, 3DGART makes fully ray-traced Gaussian training practical, reaching runtimes competitive with rasterisation-based pipelines while preserving benefits of ray tracing.

</details>

#### 2026-08-17 - SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis

**Authors:** Yejun Zhang, Zihan Wang, Xu Ji, Yihao Wang, Yuxin Hou, Junyuan Fang, Juho-Matti Kilpeläinen, Arno Solin, Hamed Rezazadegan Tavakoli, Esa Rahtu, Juho Kannala
**Links:** [abs](https://arxiv.org/abs/2608.16863) - [pdf](https://arxiv.org/pdf/2608.16863)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, 3DGS, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis
- 作者：Yejun Zhang, Zihan Wang, Xu Ji, Yihao Wang, Yuxin Hou, Junyuan Fang, Juho-Matti Kilpeläinen, Arno Solin, Hamed Rezazadegan Tavakoli, Esa Rahtu, Juho Kannala
- 出版日期：2026-08-17
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.16863

### 一句话总结
SplatGuide 通过将单个 3D 高斯场景复用于三种互补信号（渲染图像、逐高斯可见性投票图、重建 token），弥合了前馈 3DGS 重建与多视角扩散之间的信息断层，实现了无需位姿的最新视图合成。

### 研究问题
如何在不使用相机位姿的情况下，利用 3D 高斯重建中的几何先验（包括可渲染几何、可见性线索和学到的特征）来提升新视图合成的质量，特别是解决现有管线仅提取单一信号而忽略其他信号的问题。

### 核心思路/方法
- 核心策略：在一个前馈 3DGS 重建过程中，同时复用同一场景产生三种信号：
  1. **渲染图像**：提供像素对齐的几何条件。
  2. **逐高斯源视角索引投票图**：渲染到目标视图，用于遮挡感知的参考视图选择。
  3. **重建 token**：通过交叉注意力提供特征级引导。
- 所有三种信号均来自同一次重建前向传播，无需额外计算开销。
- 与多视角扩散模型结合，实现从无位姿图像生成逼真新视图。

### 主要贡献
- 指出并解决现有管线中“信息断开”问题（即重建的几何、可见性信息和特征未被充分利用）。
- 提出 SplatGuide 方法，将单个 3DGS 场景用于三种互补角色，系统性提取几何先验。
- 在 RealEstate10K、DL3DV、Tanks-and-Temples 和 Mip-NeRF 360 上实现最先进的无需位姿新视图合成性能。
- 在 RealEstate10K 上，使用中等数量输入视图时，超越了使用真实位姿的基线方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该方法提出了明确的创新点（复用 3DGS 场景产生三种互补信号），针对无位姿新视图合成这一重要问题，在多个基准上达到最先进效果，甚至超越有真值位姿的基线，对神经场景表示与渲染领域具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Generating photorealistic novel views from unposed images requires both 3D geometric understanding and the ability to synthesize unseen content. A natural strategy combines feed-forward 3DGS reconstruction with multi-view diffusion. Yet prior pipelines extract at most one signal from the reconstruction, either pixel rendering or learned features, while none exploits per-Gaussian visibility for occlusion-aware reference selection. This *information disconnect* leaves renderable geometry, visibility cues, and learned features unused. SplatGuide closes this disconnect by reusing a single 3DGS scene across three complementary roles. Rendered images provide pixel-aligned geometric conditioning. Per-Gaussian source-view indices are rendered into a target-view voting map for occlusion-aware reference selection. Reconstruction tokens supply feature-level guidance via cross-attention. All three signals derive from the same reconstruction forward pass. Across RealEstate10K, DL3DV, Tanks-and-Temples, and Mip-NeRF 360, SplatGuide achieves state-of-the-art pose-free novel view synthesis. On RealEstate10K, with a moderate number of input views, it surpasses the ground-truth-pose baseline.

</details>

#### 2026-08-17 - LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting

**Authors:** Louen Pottier
**Links:** [abs](https://arxiv.org/abs/2608.16324) - [pdf](https://arxiv.org/pdf/2608.16324)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting
- 作者：Louen Pottier
- 出版日期：2026-08-17T09:29:12Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.16324

### 一句话总结
本文提出LaGSplat框架，利用隐式拉格朗日力学与高斯泼溅解码器，从单目视频中推断物理驱动的交互式动态仿真，允许用户在推理时对物体施加训练中未见过的外力。

### 研究问题
如何从单目视频中学习具有物理可解释性的动态场景模型，使得在推理阶段用户可以对真实物体施加任意大小和方向的外部力，并获得实时、合理的物理响应。

### 核心思路/方法
- 引入低维隐状态 $\mathbf{q} \in \mathbb{R}^d$，同时担任两个角色：其一是学习到的耗散拉格朗日动力学方程的广义坐标，其二是高斯泼溅解码器的条件变量。
- 高斯泼溅解码器的基元是显式点 $\mu_i(\mathbf{q})$，它们随物体运动；这种归纳偏置使得图像平面施加的力 $f$ 可以回拉为隐式广义力 $J(\mathbf{q})^\top f$，并进入运动方程，从而支持外部交互力。像素空间CNN或神经场（NeRF）解码器不具备此能力。
- 通过在耗散欧拉-拉格朗日方程上做假设，对未见外力产生有界且合理的响应，而非约束的预测器则会发散。

### 主要贡献
- 提出一种从单目视频（一个或少数几个）推断物理控制交互仿真的框架。
- 设计双重角色的隐状态表示，将广义坐标与高斯泼溅条件变量统一，实现物理力与图像空间交互的耦合。
- 在从刚体到可变形、从自主运动到受迫真实系统的递增难度测试案例上验证了方法，结合单目视频与传感器测量。
- 支持交互式使用：任意大小和方向的外力可作用于重建物体，并在2D或3D实时渲染其响应。

### 局限性
摘要未提供足够信息（未明确讨论方法的失败案例、计算开销、对相机位姿或物体纹理的依赖、时间泛化能力等具体局限）。

### 阅读优先级
**高**
理由：该工作将经典力学（拉格朗日动力学）与神经渲染（3D高斯泼溅）结合，解决了单目视频中物理交互仿真的关键难题，方法新颖且具有实用交互性，对动态场景重建与物理推理领域有较显著的启示意义。

</details>

<details>
<summary>Abstract</summary>

We present LaGSplat (Latent Lagrangian Gaussian Splatting), a framework that infers interactive, physics-governed dynamics from one or a few monocular videos. At inference it lets a user push on the filmed object, rigid or deformable, with an external force that was never measured, annotated, or seen during training. This is possible because a low-dimensional latent state $\mathbf{q} \in \mathbb{R}^d$ plays two roles at once: it is the generalised coordinate of a learned dissipative Lagrangian and the conditioning variable of a Gaussian Splatting decoder. The inductive bias of this decoder, whose primitives are explicit points $μ_i(\mathbf{q})$ that move with the object, is what lets a force $f$ applied in the image pull back into a latent generalised force $J(\mathbf{q})^\top f$ and enter the equations of motion, which pixel-space (CNN) or neural-field (NeRF) decoders cannot do. We validate LaGSplat on test cases of increasing difficulty, from rigid to deformable and from autonomous to forced real systems, combining monocular video and sensor measurements. We further demonstrate interactive use: forces of arbitrary magnitude and direction can be applied to the reconstructed object at any time, its response rendered in real time, in 2D or 3D. Assuming a dissipative Euler-Lagrange equation over a few generalised coordinates trades generality for a bounded, plausible response to unseen forces, where an unconstrained predictor diverges.

</details>

#### 2026-08-17 - Beyond Similarity Matching: Structured Reasoning for Open-Vocabulary Referring Segmentation in 3DGS

**Authors:** Yizhao Wang, Xinfa Wang, Jingbo Wang, Jingbo Wang, Guantao Zhang, Yafeng Han, Guohong Gao, Yuhe Xia
**Links:** [abs](https://arxiv.org/abs/2608.16103) - [pdf](https://arxiv.org/pdf/2608.16103)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Similarity Matching: Structured Reasoning for Open-Vocabulary Referring Segmentation in 3DGS
- 作者：Yizhao Wang, Xinfa Wang, Jingbo Wang, Jingbo Wang, Guantao Zhang, Yafeng Han, Guohong Gao, Yuhe Xia
- 出版日期：2026-08-17T04:48:02Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.16103

### 一句话总结
本文提出QAGaussian，一种基于查询自适应神经推理的3D高斯泼溅（3DGS）开放词汇指代分割框架，通过多尺度高斯槽学习、关系感知图推理和自适应路由机制，超越了传统的全局文本-区域相似性匹配方法。

### 研究问题
现有3DGS开放词汇指代分割方法依赖全局文本-区域相似性，难以处理涉及属性、参照对象、空间关系和细粒度部件的查询，导致目标-参照混淆、粒度不匹配、部分-整体泄漏和关系违背等问题。本文旨在解决这些结构化推理难题。

### 核心思路/方法
QAGaussian框架包含三个关键组件：
1. **查询条件多尺度高斯槽学习**：学习查询条件化的多尺度高斯槽作为可微分候选，其感受野由输入表达式塑造。
2. **关系感知槽图推理**：构建语言条件边权重的关系感知槽图，传播目标-参照、属性、部分-整体和上下文证据。
3. **粒度自适应路由与细化**：软性组合区域级、对象级、部分级、属性感知和关系感知掩码分支，并通过关系约束细化保证空间、部分-整体、属性和几何一致性。

模型仅在Mosaic3D-5.6M上预训练用于高斯-文本对齐，在独立基准上评估时不进行目标数据集微调。

### 主要贡献
1. 提出QAGaussian，一个查询自适应的神经推理框架，专为语言引导的高斯原语选择设计。
2. 引入查询条件多尺度高斯槽学习、关系感知图推理和自适应路由的联合建模策略。
3. 在独立基准上实现47.2 Avg. mIoU和63.2 Avg. F1，超过最强3DGS指代基线2.7 mIoU点和2.9 F1点。
4. 显著改进Part-mIoU（从38.6到43.4）和Rel-mIoU（从44.4到50.8），并将目标-参照混淆从10.8降至7.4。
5. 开源代码：https://github.com/zqeslwyz/QAGaussian

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对3DGS开放词汇指代分割中的结构化推理难题，提出了完整的神经推理框架，在多个评估指标上取得显著提升（mIoU、F1、Part-mIoU、Rel-mIoU），且不依赖目标数据集微调，具有较强泛化性。同时开源代码，便于复现和后续研究。对从事3D场景理解、指代分割和高斯泼溅相关研究的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Open-vocabulary referring segmentation in 3D Gaussian Splatting (3DGS) requires a neural model to select Gaussian primitives according to free-form language expressions. Existing 3DGS-based methods usually rely on global text-region similarity, which is weak for queries involving attributes, reference objects, spatial relations, and fine-grained parts. This often causes target-reference confusion, granularity mismatch, part-whole leakage, and relation violations. We propose QAGaussian, a query-adaptive neural reasoning framework for language-guided Gaussian primitive selection. QAGaussian first learns query-conditioned multi-scale Gaussian slots as differentiable candidates whose receptive fields are shaped by the input expression. It then builds a relation-aware slot graph with language-conditioned edge weighting to propagate target-reference, attribute, part-whole, and contextual evidence. A granularity-adaptive router softly combines region-level, object-level, part-level, attribute-aware, and relation-aware mask branches, followed by relation-constrained refinement for spatial, part-whole, attribute, and geometric consistency. QAGaussian is pretrained only on Mosaic3D-5.6M for Gaussian-text alignment and evaluated on independent benchmarks without target-dataset fine-tuning. It achieves 47.2 Avg. mIoU and 63.2 Avg. F1, outperforming the strongest 3DGS referring baseline by 2.7 mIoU points and 2.9 F1 points. It also improves Part-mIoU from 38.6 to 43.4, Rel-mIoU from 44.4 to 50.8, and reduces target-reference confusion from 10.8 to 7.4. These results demonstrate that query-conditioned slot learning, relation-aware graph reasoning, and adaptive routing provide an effective neural modeling strategy for open-vocabulary referring segmentation in 3DGS. The code is available at https://github.com/zqeslwyz/QAGaussian.

</details>

#### 2026-08-16 - RoofGS: Roofline-Guided End-to-End Acceleration of 3D Gaussian Splatting

**Authors:** Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao
**Links:** [abs](https://arxiv.org/abs/2608.15785) - [pdf](https://arxiv.org/pdf/2608.15785)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoofGS: Roofline-Guided End-to-End Acceleration of 3D Gaussian Splatting
- 作者：Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao
- 出版日期：2026-08-16
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.15785

### 一句话总结
RoofGS 通过基于 Roofline 模型的分阶段瓶颈分析，对 3D Gaussian Splatting 的前端（内存受限）和光栅化（指令吞吐受限）分别设计针对性优化，在 4K 分辨率下实现 10.1 倍端到端加速且仅损失 0.028 dB PSNR。

### 研究问题
3D Gaussian Splatting（3DGS）在 GPU 高分辨率渲染场景下存在性能瓶颈，需要识别并消除不同渲染阶段的硬件瓶颈以实现加速。

### 核心思路/方法
1. 通过分阶段 Roofline 特征分析，识别出两个不同的硬件瓶颈：
   - 前端（front end）：全局内存流量受限
   - 光栅化（rasterization）：指令吞吐量受限
2. 针对内存受限的前端，设计分辨率自适应的量化深度排序键，将每个键压缩至 32 位。
3. 针对计算受限的光栅化器，提出范围感知的位级快速指数近似，利用不透明度剔除后的有界指数范围，并推导出逐像素误差界。
4. 辅以额外优化：内核融合、紧凑属性存储、剔除、双像素评估，以进一步减少内存流量并提升指令级并行度。

### 主要贡献
- 识别出 3DGS 在不同渲染阶段具有不同的硬件瓶颈（内存 vs 指令吞吐），而非统一的性能限制因素。
- 提出面向内存瓶颈的量化为 32 位的深度排序键方案。
- 提出面向计算瓶颈的、具有明确误差界的快速指数近似方法。
- 集成多项辅助优化，实现端到端加速：在 RTX 4090 上 4K 分辨率下从 61 FPS 提升至 616 FPS（10.1 倍），PSNR 仅下降 0.028 dB。

### 局限性
摘要未提供足够信息（例如：在不同分辨率、不同 GPU 平台上的表现，对非 4K 场景的适应性，误差界对视觉质量的实际影响，内存开销变化等均未提及）。

### 阅读优先级
**高**  
理由：该方法在不显著损失质量的前提下实现了 10 倍以上的端到端加速，针对不同瓶颈采用差异化优化而非通用内核加速，设计思路有较强的可借鉴性；且实验数据明确，适合关注 3DGS 高效渲染、硬件感知优化的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel-view synthesis but remains limited on GPUs at high resolutions. Through a stage-wise Roofline characterization, we identify two distinct hardware bottlenecks: global memory traffic dominates the front end, whereas instruction throughput limits rasterization. Guided by this analysis, we develop RoofGS, a rendering framework that applies bottleneck-specific optimizations rather than generic kernel acceleration. For the memory-bound front end, we design a resolution-adaptive quantized depth sorting key that compresses each key to 32 bits. For the compute-bound rasterizer, we introduce a range-aware bit-level fast exponential approximation tailored to the bounded exponent range after opacity culling, with a derived per-pixel error bound. These two core techniques are complemented by additional optimizations (kernel fusion, compact attribute storage, culling, dual-pixel evaluation) that additionally reduce memory traffic and improve instruction-level parallelism. Experiments show that RoofGS achieves a 10.1$\times$ end-to-end speedup over 3DGS at 4K on an RTX 4090, increasing throughput from 61 to 616 FPS, with only a 0.028 dB PSNR loss.

</details>

#### 2026-08-16 - Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats

**Authors:** Bin Ren, Qi Ma, Yue Li, Zongyan Han, Yidi Li, Yuqian Fu, Rao Muhammad Anwer, Theo Gevers, Fahad Shahbaz Khan, Salman Khan
**Links:** [abs](https://arxiv.org/abs/2608.15651) - [pdf](https://arxiv.org/pdf/2608.15651)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats
- 作者：Bin Ren, Qi Ma, Yue Li, Zongyan Han, Yidi Li, Yuqian Fu, Rao Muhammad Anwer, Theo Gevers, Fahad Shahbaz Khan, Salman Khan
- 出版日期：2026-08-16
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.15651

### 一句话总结
本文提出Gaussian-JEPA，一种基于联合嵌入预测学习（JEPA）范式的自监督方法，用于从3D高斯溅射（3DGS）表示中学习可复用的特征表示，无需重建被掩蔽的高斯属性。

### 研究问题
在3DGS表示中，自监督预训练面临两个核心挑战：同一物体可能通过不同的高斯原语（primitive）实现被观测，而现有方法将监督信号绑定在单次采样实现上并依赖输入空间解码器进行属性重建。本文旨在探索是否可以通过潜空间预测（latent prediction）为高斯token学习更统一、可复用的表示。

### 核心思路/方法
- 采用联合嵌入预测架构：在线编码器处理可见的高斯token块，共享权重的指数移动平均（EMA）编码器为掩蔽的token块提供多尺度目标特征。
- 引入互补目标投影（complementary target projections）和特征空间接地（feature-space grounding）机制，在潜空间提供监督信号，避免重建高斯属性。
- 评估场景包括高斯重采样、部分观测、可渲染形状补全，以及迁移到部件分割和物体分类任务。

### 主要贡献
- 提出Gaussian-JEPA，首次将潜空间预测范式应用于3DGS表示学习，适应高斯原语耦合属性与异质空间支撑的特点。
- 设计了基于EMA编码器和互补投影的多尺度目标生成方案，无需重建输入属性。
- 通过实验证明，与匹配的重建式预训练相比，Gaussian-JEPA在重采样输入下特征更一致，部分观测时保留更多实例信息，并为高斯补全提供更强的冻结特征。

### 局限性
摘要未提供足够信息（未提及计算开销、对超参数敏感性、在大规模场景上的扩展性、对下游任务的全面评测或失败案例等）。

### 阅读优先级
**中**
理由：该方法针对3DGS自监督学习提出了一种新颖的JEPA式范式，在特征一致性、部分观测鲁棒性和补全性能上相对于重建式预训练具有明确优势，且代码已公开，对从事神经场景表示、3D表示学习的研究者有参考价值。但摘要未提供底层实现细节和大规模实验验证，且该研究方向相对细分，若读者不涉及3DGS或自监督预训练，则优先级可下调。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) represents 3D content with anisotropic primitives that jointly encode geometry and appearance. Fixed-budget encoders consume sampled observations of Gaussian assets, so the same object may be observed through different primitive realizations. Existing self-supervised methods mainly reconstruct masked Gaussian attributes, tying supervision to one sampled realization and requiring an input-space decoder. Latent prediction offers an alternative, but its application to Gaussian tokens requires targets that accommodate coupled attributes and heterogeneous spatial support. We introduce Gaussian-JEPA, which predicts representations of held-out Gaussian token blocks from visible context. An online encoder processes the context, while a shared exponential-moving-average encoder supplies stop-gradient features for multi-scale targets. Complementary target projections and feature-space grounding provide latent supervision without reconstructing Gaussian attributes. We evaluate the features under Gaussian resampling, partial observations, and renderable shape completion, together with transfer to part segmentation and object classification. Compared with matched reconstruction pretraining, Gaussian-JEPA is more consistent across resampled inputs, retains more instance information under partial observations, and provides stronger frozen features for Gaussian completion. These results support latent prediction as an effective objective for reusable 3D Gaussian representations. Code is on the project page (https://amazingren.github.io/Gaussian-JEPA/).

</details>

#### 2026-08-15 - HistReNeRF: Historic Image Relocalisation within Contemporary Neural Radiance Field Reconstructions

**Authors:** Benjamin T. Hughes, Stuart James
**Links:** [abs](https://arxiv.org/abs/2608.15420) - [pdf](https://arxiv.org/pdf/2608.15420)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HistReNeRF: Historic Image Relocalisation within Contemporary Neural Radiance Field Reconstructions
- 作者：Benjamin T. Hughes, Stuart James
- 出版日期：2026-08-15
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.15420

### 一句话总结
本文提出 HistReNeRF 框架，通过匹配历史照片的 DINOv2 特征与当代 NeRF 重建中的候选射线，实现对历史照片的 6-DoF 位姿重定位。

### 研究问题
如何将历史档案照片在当代场景模型中进行可靠重定位，以应对历史与现代视图在摄影外观、可见物体和空间布局上的显著差异。

### 核心思路/方法
利用 NeRF 的连续场景表示作为可查询接口，从当代重建中采样候选射线；将历史照片与当代图像的特征通过域适应直接对齐到 DINOv2 特征空间中，避免在像素空间进行操作，从而减少跨时间外观偏移。研究对比了嵌入空间域适应与像素空间方法。

### 主要贡献
- 提出 HistReNeRF，一个基于 NeRF 和 DINOv2 特征匹配的历史图像重定位框架。
- 构建了一个新的跨时间数据集，包含 10,545 张当代街景图像和 230 张来自三个欧洲地标的历史档案照片。
- 实验表明，嵌入空间域适应相比像素空间方法，在三个场景中平均降低平移误差 11%、旋转误差 16%。

### 局限性
摘要未提供足够信息，未明确讨论方法的失败情况、运行效率、对 NeRF 重建质量的依赖程度、数据集覆盖范围局限或潜在泛化能力限制。

### 阅读优先级
**中**。该工作聚焦于历史图像重定位这一较细分方向，方法结合了 NeRF 与 DINOv2 特征，具有一定新颖性，并提供了公开数据集和代码。但摘要未展示与主流视觉定位基准的对比或更广泛适用性，若研究兴趣集中在跨时间视觉定位或 NeRF 应用，可优先阅读；若为通用视觉重定位领域，可暂缓精读。

</details>

<details>
<summary>Abstract</summary>

Relocalising archival photographs within a contemporary scene model is challenging because historic and modern views can differ in photographic appearance, visible objects, and spatial layout. Therefore, we present HistReNeRF, a framework that estimates the 6-DoF pose of a historic photograph by matching adapted DINOv2 patch features to candidate rays sampled from a contemporary Neural Radiance Field (NeRF) reconstruction. The continuous representation of a NeRF provides a queryable scene interface from which candidate rays can be sampled and matched, enabling domain adaptation between historic photography and contemporary images directly in the feature representation used for localisation. We evaluate embedding-space-based domain adaptation against pixel-space methods on a new cross-temporal dataset comprising 10,545 contemporary street-level images and 230 archival photographs from three European landmarks. Embedding-space adaptation reduces translation and rotation errors by an average of 11% and 16%, respectively, across the three scenes. These results show that neural scene relocalisation provides a natural interface for feature-space adaptation, reducing cross-temporal appearance shift without modifying the query image. Code and dataset at https://github.com/ARTUROLab/HistReNeRF.

</details>

#### 2026-08-13 - GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors

**Authors:** Yanming Yang, Chenxi Song, Ping Wang, Xin Yuan, Chi Zhang
**Links:** [abs](https://arxiv.org/abs/2608.13502) - [pdf](https://arxiv.org/pdf/2608.13502)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS²CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors
- 作者：Yanming Yang, Chenxi Song, Ping Wang, Xin Yuan, Chi Zhang
- 出版日期：2026-08-13
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.13502

### 一句话总结
该论文提出一种新框架，利用3D高斯溅射与大规模视觉基础模型先验，从单次快照压缩成像测量中重建高质量3D场景，并通过专用稠密化策略提升重建鲁棒性与效率。

### 研究问题
如何从单一快照压缩成像（SCI）测量中高效、高质量地重建3D场景，克服信息损失、视点多样性有限以及3D表示与相机位姿联合优化的计算负担等挑战。

### 核心思路/方法
- 主重建阶段：将测量数据与3D视觉基础模型（VFM）初始化结合，进行SCI感知的高斯优化。
- 辅助细化阶段：在粗阶段收敛后，引入2D视觉基础模型在合成视点处提供伪视图监督，用于局部外观细化。
- 专用稠密化策略（OSGR）：包括基于局部不透明度统计扩展分裂候选、通过平均不透明度正则抑制损失补偿性的不透明度膨胀，以及用显式候选比例和高斯数量约束限制表示增长，以应对SCI监督模糊导致的不稳定性。

### 主要贡献
- 提出首个结合3DGS与大规模视觉基础模型先验的SCI单测量3D重建框架。
- 设计SCI专用的不透明度引导分裂与增长调节（OSGR）稠密化策略。
- 在多个基准上实现最佳综合性能，兼顾领先的重建质量、对视点变化的鲁棒性以及竞争力的计算效率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作将快照压缩成像与3D高斯溅射及视觉基础模型结合，属于多领域交叉创新，面向3D重建的前沿方向。其提出的稠密化策略针对SCI特有监督模糊问题，具有明确的方法贡献和广泛的实验验证（摘要提及多基准），适合关注3D表示学习、压缩感知或高效重建的研究者深入阅读。

</details>

<details>
<summary>Abstract</summary>

Snapshot Compressive Imaging (SCI) offers an efficient solution for high-speed video acquisition and, under exposure-time camera--scene relative motion, multi-view scene capture by compressing temporal or spatial information into a single 2D measurement. While recent studies have explored SCI for 3D scene reconstruction, existing methods struggle with significant challenges due to information loss, limited viewpoint diversity, and the computational burden of jointly optimizing 3D representations and camera poses. In this work, we propose a novel framework that reconstructs high-quality 3D scenes from a single SCI measurement by leveraging 3D Gaussian Splatting (3DGS) and the powerful priors of large-scale vision foundation models (VFMs). Our primary reconstruction combines measurement-derived 3D VFM initialization with SCI-aware Gaussian optimization. After coarse-stage convergence, an auxiliary 2D VFM provides pseudo-view supervision at synthesized viewpoints for local appearance refinement. To further address the instability caused by ambiguous SCI supervision during 3DGS optimization, we introduce Opacity-Guided Splitting and Growth Regulation (OSGR), an SCI-specific densification strategy that augments split candidates using local opacity statistics, discourages loss-compensating opacity inflation through mean-opacity regulation, and bounds representation growth with explicit candidate-ratio and Gaussian-count constraints. Extensive experiments across multiple benchmarks demonstrate that our method achieves the strongest overall performance, combining leading reconstruction quality and robustness to viewpoint variation with competitive computational efficiency.

</details>

#### 2026-08-13 - Semantic Radiance Fields as Simulators for Spatial Reasoning in Real-World Scenes

**Authors:** Nico Heider, Michał Jan Włodarczyk, Katarzyna Wasielewska-Michniewska, Przemysław Hołda, Martin Schieck, Marcin Paprzycki, Maria Ganzha, Bogdan Franczyk
**Links:** [abs](https://arxiv.org/abs/2608.13095) - [pdf](https://arxiv.org/pdf/2608.13095)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, novel view synthesis, view synthesis, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Semantic Radiance Fields as Simulators for Spatial Reasoning in Real-World Scenes
- 作者：Nico Heider, Michał Jan Włodarczyk, Katarzyna Wasielewska-Michniewska, Przemysław Hołda, Martin Schieck, Marcin Paprzycki, Maria Ganzha, Bogdan Franczyk
- 出版日期：2026-08-13T11:01:09Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.13095

### 一句话总结
本文提出将语义辐射场（SRF）作为真实场景中空间推理智能体的模拟器，通过联合编码几何、外观和逐类语义身份，实现真实感与语义标注的统一。

### 研究问题
如何为空间推理智能体的训练与评估提供既具备几何真实性又可语义查询的多样化环境？现有合成模拟器虽提供真值语义但缺乏真实感，而基于真实场景重建的模拟器虽外观真实却默认缺少语义真值。

### 核心思路/方法
使用语义辐射场（SRF）作为模拟器：将预训练视觉模型产生的2D语义分割提升到3D辐射场中，使辐射场联合编码几何、外观和逐类语义身份。该表示从真实场景的有姿态RGB图像重建，支持新视角合成、语义查询和自由空间查询，并可将这些能力提供给物理引擎使用。

### 主要贡献
- 提出将SRF用作空间推理智能体的模拟器，统一了真实感与语义真值。
- SRF从真实场景重建，同时支持新视角渲染、语义查询和自由空间查询，形成单一三维接地表示。
- 能够高效生成多样化的真实世界环境，用于训练和评估空间推理模型。
- 以果园苹果抓取任务为例，展示了SRF驱动模拟器的应用流程（相机渲染、语义真值、占用查询供物理引擎使用）。

### 局限性
摘要未提供足够信息。摘要中仅以果园苹果抓取任务作为示例应用，未讨论方法在场景规模、动态物体、语义类别覆盖、计算开销或泛化能力等方面的潜在限制。

### 阅读优先级
**中**。理由：该方法对空间推理或神经场景表示领域有一定新颖性，且提出的SRF模拟器思路清晰，具有应用潜力；但摘要未涉及实验验证和量化结果，属于概念性方案论述，若读者关注该交叉方向可进一步阅读，若仅需成熟方法则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Training and evaluating spatial reasoning in embodied agents requires diverse environments that are both geometrically faithful and semantically queryable. Synthetic simulators offer ground truth semantics but sacrifice realism; simulators based on reconstructions of real-world environments have realistic appearance but lack ground truth semantics by default. We propose using Semantic Radiance Fields (SRF) as simulators for spatial reasoning agents. SRFs are a representation that unifies these requirements by lifting 2D semantic segmentations from pretrained vision models into a 3D radiance field that jointly encodes geometry, appearance, and per-class semantic identity. The resulting fields are reconstructed from posed RGB captures of real scenes and support novel-view synthesis, semantic and free-space queries within a single grounded representation. This enables the efficient generation of diverse real-world environments to train and evaluate spatial reasoning models. As an example application, we outline an SRF-driven simulator for an orchard apple-reaching task, in which the radiance field supplies camera rendering, semantic ground truth, and occupancy queries to a physics engine.

</details>

#### 2026-08-13 - HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments

**Authors:** Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao, Tuyen P. Le, Truong Nguyen, Quan Nguyen
**Links:** [abs](https://arxiv.org/abs/2608.12860) - [pdf](https://arxiv.org/pdf/2608.12860)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments
- 作者：Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao, Tuyen P. Le, Truong Nguyen, Quan Nguyen
- 出版日期：2026-08-13T06:16:05Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.12860

### 一句话总结
本文提出了HumanoidVLN，一个基于物理的仿真器与基准，用于评估跨多种人形机器人的视觉-语言导航任务，并验证了其仿真到现实迁移的有效性。

### 研究问题
现有视觉-语言导航（VLN）基准未考虑人形机器人特有的物理约束（如双足运动限制）、多平台形态差异以及步态导致的视觉相机动态畸变，本文旨在填补这一空白，提出面向人形机器人形态多样性的VLN仿真环境与评测基准。

### 核心思路/方法
- 基于NVIDIA Isaac Sim构建物理仿真平台，支持可扩展的人形机器人配置，涵盖4种机器人（Unitree G1、H1、Internal-A、Internal-B），身高1.17m至1.80m，下肢自由度10–12。
- 采用分层控制栈：强化学习运动策略结合可替换的PD或MPC路径跟踪器。
- 环境来源包括艺术家设计场景与3D高斯泼溅重建，筛选可通行面积超过100平方米的区域。
- 指令生成采用“生成器-评审器-释义器”多智能体流水线并有人类在环验证，产出933条冲突感知参考片段，每条含1条细粒度指令和3种风格变体（正式、自然、随意）。
- 兼容性验证：支持NaVILA、DualVLN、StreamVLN、JanusVLN等VLN模型。
- 仿真到现实迁移：使用DualVLN和Unitree G1进行20片段试点实验。

### 主要贡献
- 提出了首个面向多种人形机器人形态的物理仿真VLN基准（HumanoidVLN）。
- 构建了可扩展的仿真平台，支持新机器人和新VLN模型的低成本集成。
- 发布了包含933条高质量参考片段的多粒度指令数据集。
- 在4个模型和4种机器人上进行了系统评估，其中JanusVLN获得最高平均成功率43.55%和nDTW 48.38。
- 通过20片段实机实验验证了仿真到现实的强相关性（r=0.935），平均绝对误差0.68m，平均轨迹相似度0.782 nDTW（±0.188）。

### 局限性
摘要未提供足够信息。摘要未明确讨论该方法在计算开销、仿真多样性覆盖范围、不同指令风格对性能的影响分析、以及内部机器人（Internal-A/B）的实机验证情况等方面的局限性。

### 阅读优先级
**高**。
理由：该工作针对人形机器人VLN这一前沿且实际约束突出的问题，提供了完整的仿真-数据-基准-实机验证闭环，实验结果（含sim-to-real强相关性）具有较强说服力，对从事VLN、机器人导航和人形机器人研究的读者有直接参考价值，且代码和数据承诺开放。

</details>

<details>
<summary>Abstract</summary>

Vision-Language Navigation (VLN) for humanoid robots poses challenges existing benchmarks fail to address: bipedal locomotion imposes physical constraints absent from wheeled agents, humanoid morphologies vary across platforms, and egocentric observations are distorted by locomotion-induced camera dynamics. We present HumanoidVLN, a physics-grounded simulator and benchmark for VLN across diverse humanoid embodiments. Built on NVIDIA Isaac Sim, our platform supports an extensible set of humanoid configurations, demonstrated on four robots (Unitree G1, Unitree H1, Internal-A, Internal-B) spanning 10-12 lower-body DoF and heights from 1.17m to 1.80m, via a hierarchical control stack combining a reinforcement learning locomotion policy with interchangeable PD or MPC path trackers. New robots and VLN models integrate with minimal effort; we demonstrate compatibility with NaVILA, DualVLN, StreamVLN, and JanusVLN. Environments are drawn from artist-designed scenes and 3D Gaussian Splatting reconstructions, filtered for navigable areas exceeding 100 square meters. Instructions are generated by a dual generator-reviewer plus paraphraser multi-agent pipeline with human-in-the-loop verification, yielding 933 collision-aware reference episodes, each paired with one fine-grained instruction and three coarse-grained stylistic variants (formal, natural, casual). Across four models and four embodiments, JanusVLN achieves the highest mean success rate of 43.55% and nDTW of 48.38. In a 20-episode sim-to-real pilot with DualVLN and the Unitree G1, navigation errors correlate strongly (r=0.935), with a mean absolute difference of 0.68m and mean trajectory similarity of 0.782 (+/-0.188) nDTW. These results highlight the interaction between VLN models, controllers, and humanoid embodiments under physical execution. Code, benchmark, and data will be released upon acceptance at https://humanoid-vln.github.io/.

</details>

#### 2026-08-13 - LocusGS: Spatially Grounded Tokens for Feed-Forward 3D Gaussian Splatting

**Authors:** Wenyu Li, Sidun Liu, Tongrui Hu, Peng Qiao, Yong Dou
**Links:** [abs](https://arxiv.org/abs/2608.12825) - [pdf](https://arxiv.org/pdf/2608.12825)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LocusGS: Spatially Grounded Tokens for Feed-Forward 3D Gaussian Splatting
- 作者：Wenyu Li, Sidun Liu, Tongrui Hu, Peng Qiao, Yong Dou
- 出版日期：2026-08-13
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.12825

### 一句话总结
LocusGS 通过为查询式前馈 3D 高斯泼溅中的每个高斯查询引入显式的 3D 锚点状态（中心+支撑半径），改善查询的空间连贯性，从而提升渲染质量。

### 研究问题
现有查询式前馈 3DGS 方法中，从同一查询解码出的高斯常常散布在场景中相距较远的区域，导致查询级别的空间连贯性弱、与场景结构对齐差。作者将这一问题归因于现有高斯查询所采用纯隐式表示，缺乏显式空间约束。

### 核心思路/方法
LocusGS 为每个高斯查询增加一个 3D 锚点状态，包含中心位置和支撑半径。锚点状态在解码器各层中逐步细化，并在查询交互、多视图特征聚合和高斯生成三个环节中统一使用。具体包括：
1. 锚点-射线几何偏置：引导查询只关注与其锚点空间相关的图像观测。
2. 锚点中心解码：将查询生成的 Gaussians 限制在锚点周围的局部区域内。

### 主要贡献
1. 提出 LocusGS 方法，通过显式 3D 锚点状态增强高斯查询的空间定位能力。
2. 在相同高斯预算下，较查询式高斯 token 基线方法在新型视图合成基准上取得更好的渲染质量。
3. 实验分析表明，学习到的锚点形成连贯的空间布局，高斯分布更加结构化，证明显式锚点状态改善了空间组织性。

### 局限性
摘要未提供足够信息，无法得知该方法在计算开销、对遮挡或复杂场景的鲁棒性、以及与大场景或动态场景的适配性等方面的局限性。

### 阅读优先级
**中**。该工作针对查询式前馈 3DGS 的空间连贯性问题提出了明确改进，方法设计清晰、实验验证充分，适合关注 3D 场景表示与神经渲染的研究者阅读。但摘要未展示与更多当前主流方法（如非查询式方法）的全面对比，也未涉及多尺度或大规模场景的扩展讨论，因此作为方向性参考价值较高，而非必须优先精读的突破性工作。

</details>

<details>
<summary>Abstract</summary>

Recent query-based feed-forward 3DGS methods represent a scene using learnable queries, each aggregating multi-view evidence and decoding a group of Gaussians. Ideally, different queries should specialize in coherent local regions of the scene. However, we observe that Gaussians decoded from the same query often scatter across distant scene regions, resulting in weak query-level spatial coherence and poor alignment with the scene structure. We attribute this behavior to the purely latent representation of existing Gaussian queries. To address this limitation, we introduce LocusGS, which augments each Gaussian query with a 3D anchor state consisting of a center and a support radius. The anchor state is progressively refined across decoder layers and is used throughout query interaction, multi-view feature aggregation, and Gaussian generation. Specifically, an anchor-to-ray geometric bias guides each query toward spatially relevant image observations, while anchor-centered decoding organizes its Gaussians within a local region. Experiments on novel view synthesis benchmarks show that LocusGS improves rendering quality over query-based Gaussian token baselines under the same Gaussian budget. Further analysis shows that the learned anchors form coherent spatial layouts and lead to more structured Gaussian distributions, demonstrating that explicit anchor states improve the spatial organization. Our project page: https://leo-frank.github.io/LocusGS_viewer.

</details>

## Embodied / Robotics / AR Applications

### 2026-08

#### 2026-08-17 - Mask What Matters: Saliency-Guided Video Self-Supervised Learning for Autonomous Driving

**Authors:** Christopher Lang, Alexander Braun, Abhinav Valada
**Links:** [abs](https://arxiv.org/abs/2608.17178) - [pdf](https://arxiv.org/pdf/2608.17178)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth estimation, autonomous driving

<details>
<summary>Abstract</summary>

Video self-supervised learning through masked spatiotemporal prediction has emerged as a promising paradigm for learning feature representations from unlabeled data. However, existing methods typically rely on random masking, which indiscriminately removes regions irrespective of their semantic or temporal relevance. In ego-centric driving videos, this can weaken the pretext signal since safety-critical cues such as pedestrians, vehicles, lane boundaries, and dynamic interactions often occupy only a small portion of the frame, yet are central to downstream perception. We introduce V-JEPA4A, a domain-specialized variant of V-JEPA for autonomous driving that is pre-trained on publicly available driving videos with a novel saliency-driven masking policy. It accounts for semantically and temporally relevant context. The proposed policy preserves and predicts context according to semantic importance and temporal relevance, yielding more informative representation learning while retaining the efficiency of masked prediction. We evaluate the resulting encoders on four driving benchmarks spanning tracking, semantic segmentation, and depth estimation. The results demonstrate that V-JEPA4A reduces identity switches on BDD100k MOT by 25% over V-JEPA with random masking, achieves 73.2 mIoU on Cityscapes, and 3.75 RMSE on KITTI-2015 depth, while incurring only ~14% additional pre-training iteration overhead.

</details>

#### 2026-08-17 - ViHaTeleop: A Low-Cost, Lightweight Visual-Haptic Teleoperation System for Dexterous Manipulation Learning

**Authors:** Fucai Zhu, Yanhou Lai, Paul Maestre, Koichi Hashimoto
**Links:** [abs](https://arxiv.org/abs/2608.16572) - [pdf](https://arxiv.org/pdf/2608.16572)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ViHaTeleop: A Low-Cost, Lightweight Visual-Haptic Teleoperation System for Dexterous Manipulation Learning
- 作者：Fucai Zhu, Yanhou Lai, Paul Maestre, Koichi Hashimoto
- 出版日期：2026-08-17
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.16572

### 一句话总结
本文提出了一种低成本、轻量级的视觉-触觉遥操作系统 ViHaTeleop，通过引入指级振动触觉反馈，显著提升了接触关键型灵巧操作任务的示教质量与成功率。

### 研究问题
如何以低成本硬件实现高质量的接触关键型灵巧操作示教数据采集，即解决低成本遥操作硬件难以采集接触关键演示数据的问题。

### 核心思路/方法
- 构建轻量（0.7 kg）低成本（$550）的视觉-触觉遥操作系统，融合 SLAM 腕部追踪、相机手部追踪以及基于线性谐振致动器（LRA）的指级振动触觉反馈。
- 引入若干设计选择：LED 照明、鱼眼手部相机、触觉感知重定向约束。
- 在真实环境（Franka + LEAP Hand + 9DTact）与仿真环境（Isaac Sim）中部署系统，并集成基于深度相机的轻量触觉代理，实现从多模态示教采集到视觉-触觉策略训练的完整流程。

### 主要贡献
- 首次提出结合低成本视觉追踪与指级振动触觉反馈的遥操作系统，并通过消融实验验证触觉反馈的有效性。
- 在六项接触关键任务、九名参与者的匹配实验中，触觉反馈使所有任务的成功率提升（+2.2～+15.6 个百分点），主观评分在触觉清晰度和抓取信心方面有显著提升（Wilcoxon 符号秩检验，p<0.05）。
- 提供从多模态示教采集到视觉-触觉策略训练的完整管线，初步下游验证表明触觉线索对接触关键子任务（如插销入孔）有显著增益（相较纯视觉提升 +17 个百分点）。

### 局限性
摘要未提供足够信息；未报告硬件耐久性、系统延迟、大规模任务泛化能力、参与者多样性等细节。

### 阅读优先级
**高**。理由：该工作直击灵巧操作示教学习中接触关键数据采集困难的核心痛点，系统成本低、重量轻，且提供了真实与仿真环境下的多任务验证以及消融实验，对遥操作硬件设计和触觉反馈在人机交互中的价值均有明确的数据支撑，适合机器人操作、示教学习与人机交互方向的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

Learning from demonstration is a promising approach for dexterous manipulation, but collecting high-quality contact-critical demonstrations remains difficult with low-cost teleoperation hardware. We present ViHaTeleop, a lightweight (0.7 kg), low-cost (\$550) visual-haptic teleoperation system with SLAM-based wrist tracking, camera-based hand tracking, and finger-wise vibrotactile feedback through Linear Resonant Actuators (LRA). The system includes several design choices (LED illumination, fisheye hand camera, and tactile-aware retargeting constraints) and is deployed on Franka + LEAP Hand + 9DTact in both real and simulated environments. Under matched with/without-haptic conditions with nine participants across six contact-critical tasks, haptics improved success rates across all tasks (+2.2 to +15.6 percentage points), while completion-time effects were task-dependent. Subjective ratings showed significant gains in contact clarity and grasp confidence in both simulation and real-world settings (Wilcoxon signed-rank, $p<0.05$). We also integrate a lightweight depth-camera-based tactile proxy in Isaac Sim, enabling a full pipeline from multi-modal demonstration collection to visual-tactile policy training. Preliminary downstream validation by training visual-tactile policies from collected demonstrations shows tactile cues benefit contact-critical subtasks (peg-in-hole: +17 percentage points over vision-only).

</details>

#### 2026-08-17 - GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation

**Authors:** Tianchen Deng, Xuefeng Chen, Shuang Wu, Qu Chen, Jiajun Zhu, Bo Dai, Jianfei Yang, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2608.16234) - [pdf](https://arxiv.org/pdf/2608.16234)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, scene understanding, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation
- 作者：Tianchen Deng, Xuefeng Chen, Shuang Wu, Qu Chen, Jiajun Zhu, Bo Dai, Jianfei Yang, Hesheng Wang
- 出版日期：2026-08-17
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.16234

### 一句话总结
本文提出一个基于3D高斯的基础特征驾驶世界模型，统一了场景理解、语言推理、可控4D编辑与多模态生成任务。

### 研究问题
现有驾驶世界模型主要聚焦条件场景生成，缺乏显式3D场景理解、语言接地推理与可控4D编辑能力；此外，点云、占用或BEV表示难以实现文本信息与3D场景结构的细粒度对齐。

### 核心思路/方法
- 提出基础特征高斯分词器（foundation-feature Gaussian tokenizer），将Qwen/SigLIP的视觉语言特征直接蒸馏至3D高斯基元，构建紧凑的开词汇高斯语义场。
- 设计几何感知高斯适配器（geometry-aware Gaussian adapter），结合重要性感知层次选择与文本条件Perceiver式交叉注意力，将稠密高斯基元聚合成紧凑世界令牌。
- 引入基于KL的高斯-图像分布对齐目标，使高斯世界令牌与基础图像令牌对齐。
- 在对齐的高斯表示基础上，支持指令可控场景编辑（如天气条件生成、动态车辆操作）。

### 主要贡献
- 提出统一框架，同时支持场景理解、语言接地推理、可控4D编辑与多模态生成。
- 提出基础特征高斯分词器，实现开放词汇的3D语义场构建。
- 设计几何感知适配器与KL对齐目标，提升表示兼容性。
- 在多个驾驶基准上，于场景理解、视觉接地、规划推理和可控4D生成任务中取得先进性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作将3D高斯表示与视觉语言基础模型结合，面向驾驶场景提出统一框架，覆盖理解、编辑与生成多类任务，与当前3D生成式世界模型和语言接地研究方向高度相关，且宣称在多个基准上取得SOTA，值得进一步精读其技术细节与实验设计。

</details>

<details>
<summary>Abstract</summary>

Driving World Models (DWMs) have recently advanced rapidly with generative models, yet most existing methods mainly focus on conditional scene generation and lack explicit 3D scene understanding, language-grounded reasoning, and controllable 4D editing capabilities. Moreover, commonly used point cloud, occupancy, or BEV representations make it difficult to achieve fine-grained alignment between textual information and the underlying 3D scene structure. To address these limitations, we propose a foundation-feature Gaussian driving world model that unifies scene understanding, language-grounded reasoning, controllable 4D editing, and multi-modal generation within a single framework. Specifically, we introduce a foundation-feature Gaussian tokenizer that directly distills Qwen/SigLIP visual-language features into 3D Gaussian primitives, building a compact open-vocabulary Gaussian semantic field. We further design a geometry-aware Gaussian adapter that combines importance-aware hierarchical selection with text-conditioned Perceiver-style cross-attention to aggregate dense Gaussian primitives into compact world tokens. To improve representation compatibility, we introduce a KL-based Gaussian--image distribution alignment objective that aligns Gaussian world tokens with foundation image tokens. Based on the aligned Gaussian representation, our framework further supports instruction-controllable scene editing, including weather-conditioned generation and dynamic vehicle manipulation. Extensive experiments on broader driving benchmarks demonstrate that our method achieves state-of-the-art performance across scene understanding, visual grounding, planning-oriented reasoning, and controllable 4D generation tasks. We will release the code and datasets publicly on Github.

</details>

#### 2026-08-13 - DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation

**Authors:** DreamX Team, Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li, Qingfeng Shi, Datao Tang, Jing Tang, Jun Wang, Pengfei Zhang
**Links:** [abs](https://arxiv.org/abs/2608.13489) - [pdf](https://arxiv.org/pdf/2608.13489)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation
- 作者：DreamX Team, Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li, Qingfeng Shi, Datao Tang, Jing Tang, Jun Wang, Pengfei Zhang
- 出版日期：2026-08-13
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.13489

### 一句话总结
DreamX-Phi 1.0 是一个动作条件下的视频世界模型，通过几何编码、深度分支和物体一致性保持等技术，实现机器人操作中的高质量未来帧预测，并在 WorldArena 2.0 挑战赛中取得优异成绩。

### 研究问题
如何构建一个既具备视觉真实感、又能严格遵循动作指令且保持物体一致性的机器人操作视频世界模型，以准确预测给定动作序列下的未来观测。

### 核心思路/方法
- 以当前观测帧、语言指令和末端执行器位姿及夹爪状态序列为条件，预测未来观测视频。
- 采用 **PRoPE-style 几何编码**：将每只手臂的 SE(3) 变换注入注意力机制，保持手臂身份与刚体运动结构，确保预测遵循各臂指令路径。
- 引入轻量 **深度分支** 建模场景级几何信息。
- 利用 **SAM3 掩码** 与冻结的 **V-JEPA teacher** 维持抓取过程中小物体的语义一致性。
- 通过 **分布匹配蒸馏** 将多步生成器压缩为少步学生模型，提升部署效率。

### 主要贡献
- 提出动作条件视频世界模型 DreamX-Phi 1.0，兼顾视觉真实感与动作/物体级忠实性。
- 创新性引入 PRoPE-style 几何编码实现手臂级 SE(3) 约束。
- 结合深度分支与 SAM3+V-JEPA 教师机制，解决场景几何与物体演化建模难题。
- 通过分布匹配蒸馏实现高效生成推理。
- 在 WorldArena 2.0 挑战赛中获得 Track 1 第一名、Track 2 第二名。

### 局限性
摘要未提供足够信息：论文未在摘要中报告量化实验误差、模型参数量、训练数据规模、推理速度或具体蒸馏加速比等细节，也未说明当前方法在哪些场景下可能失效或存在何种限制。

### 阅读优先级
**高**

理由：该工作面向机器人操作中的视频世界建模这一前沿方向，方法整合了几何编码、深度估计、物体分割与蒸馏技术，设计较为系统，且已在公开挑战赛中验证效果，对从事具身智能、视频预测和机器人控制的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mathrm{SE}(3)$ transformations into attention via \textbf{PRoPE-style geometric encoding}, preserving arm identity and rigid-motion structure. Action control alone does not fully constrain scene geometry or the evolution of small manipulated objects. We therefore add a lightweight \textbf{depth branch} for scene-level geometry and use \textbf{SAM3 masks} with a frozen \textbf{V-JEPA teacher} to maintain object consistency throughout grasping. We further distill the multi-step generator into a few-step student via distribution-matching distillation for efficient deployment. At the time of writing, \model{} achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge. Our model and code will be publicly available.

</details>

#### 2026-08-12 - Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations

**Authors:** AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini, AmirMohsen Eshghi, Siavash Arjomand Bigdel
**Links:** [abs](https://arxiv.org/abs/2608.12299) - [pdf](https://arxiv.org/pdf/2608.12299)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations
- 作者：AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini, AmirMohsen Eshghi, Siavash Arjomand Bigdel
- 出版日期：2026-08-12T17:45:03Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.12299

### 一句话总结
本文对2016年以来57篇以方法为中心的类激活映射（CAM）相关论文进行系统综述，提出了按归因机制、架构依赖和评估目标划分的分类法，总结了该领域从单一CNN层向多层、概率化、令牌感知及基础模型感知解释的演进趋势。

### 研究问题
类激活映射（CAM）作为可解释人工智能中广泛使用的视觉解释方法家族，其研究现状和发展趋势如何？具体包括：不同CAM方法如何归类和区分、各方法的主要贡献与遗留问题是什么，以及当前评估协议是否统一。

### 核心思路/方法
作者严格筛选了2016年以来57篇以方法为中心的论文，构建了一个分类法，从三个维度对CAM方法进行划分：（1）归因机制（gradient-based vs. gradient-free vs. hybrid）；（2）架构依赖（CNN、Transformer、基础模型等）；（3）评估目标（忠实性、定位、鲁棒性、计算成本、人类信任等）。在此基础上，分三类综述了梯度式CAM、近期与混合CAM风格方法，以及基于模型或架构感知的方法，并检视了每种方法留下的未解决缺口及后续方法的补足尝试。

### 主要贡献
1. 提供了一个严格的、以方法为中心的57篇论文综述语料库。
2. 构建了新的CAM分类法，按归因机制、架构依赖和评估目标实现多维划分。
3. 系统梳理了CAM从经典CNN场景到Transformer、基础模型时代的演进路径。
4. 明确指出评估协议碎片化问题，并分析了各方法在忠实性、定位、鲁棒性、成本和人类信任等维度上的贡献与缺口。

### 局限性
摘要未提供足够信息：未提及关于语料库选择的具体排除/纳入标准、各方法的定量对比结果、以及评估协议碎片化的具体表现或标准化建议。摘要也未报告综述过程中的偏倚控制方法或对未来研究方向的详细建议。

### 阅读优先级
**中**。理由：该文是一篇综述论文，对所涉领域（可解释视觉、CAM方法）有系统梳理价值，适合该方向研究者了解宏观脉络和分类框架。但由于其分类为“Embodied / Robotics / AR Applications”，与纯计算机视觉方向略有距离，且摘要未提供具体的实证对比结论，对于追求具体方法细节或实验复现的读者优先级略低。若读者正从事视觉可解释性研究或需要CAM方向的全景认知，则值得一读。

</details>

<details>
<summary>Abstract</summary>

Class activation mapping (CAM) is one of the most widely used visual explanation families in explainable artificial intelligence. Its purpose is intuitive: it converts internal model evidence into a heatmap that highlights the image regions, convolutional channels, tokens, or patches that support a target class or concept. Since the first CAM formulation in 2016, the field has moved far beyond global-average-pooled CNN classifiers. CAM-style methods now include gradient-based post-hoc explanations, gradient-free score and ablation methods, high-resolution upscaling, weakly supervised localization and segmentation, transformer token attribution, causal and debiasing methods, and foundation-model-era approaches that use CLIP, DINO, SAM, or feature-distribution comparisons. This review synthesizes a strict corpus of 57 method-centered papers published from 2016 onward. The paper develops a taxonomy that separates methods by attribution mechanism, architectural dependence, and evaluation objective. It then reviews gradient-based CAMs, recent and hybrid CAM-style methods, and model-based or architecture-aware methods. Across the corpus, the main trend is clear: the field is shifting from explaining one class score in one low-resolution CNN layer toward comparative, multi-layer, probabilistic, token-aware, and foundation-model-aware explanations. At the same time, evaluation remains fragmented. Faithfulness, localization, robustness, computational cost, and human trust are often measured with different protocols. The review therefore emphasizes not only what each method contributes, but also which gap it leaves open and which later methods attempt to close that gap.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
