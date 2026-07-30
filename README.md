# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：39
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 17
  - Embodied / Robotics / AR Applications: 10
  - Neural Scene Representations & Rendering: 8
  - Geometry Foundation Models: 2
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，以下是基于今日论文列表的中文科研趋势综合分析。

---

#### 今日主要趋势

##### 1. 3D 高斯泼溅（3DGS）全面走向“高效与可部署”
3DGS 系列论文不再满足于简单的新视角合成，而是全面转向解决实际部署中的痛点：模型压缩、场景级/物体级存储与流传输、以及动态场景的适应性传输。具体体现在：
- **压缩与紧凑性**：如 `3DGBGS` 引入颗粒球（Granular Ball）进行自适应锚点初始化，在减少模型存储的同时保持渲染质量；`AtlasLC` 针对物体级 3DGS 提出了高效、无需重训练的直接压缩管线，服务于 XR 应用。
- **流传输与可伸缩性**：`SplatStream` 提出质量/分辨率分层和层间预测编码，实现了动态 3D 场景的细粒度、自适应流传输，直接面向带宽波动环境下的渲染应用。
- **新应用拓展**：`CORF-GS` 将 3DGS 从视觉信号拓展到射频（RF）信号，用于实时无线信道建模。`PanoLess` 利用 3DGS 和反射线索从反射面局部视图重建完整环境，`StructureGS` 则针对铰接物体，将结构先验嵌入 3DGS 优化中。

##### 2. 视频与场景理解的“世界模型化”与“交互化”
研究重心从“感知”向“预测和交互”迁移，视频模型不再仅是生成工具，而成为可探索的世界模型。
- **交互式世界模型**：`Wonder` 构建了一个实时、相机可控的“可玩”世界模型，支持用户交互式导航。`Genie Sim PanoWorld` 将全景图生成和 3D 重建桥接，通过可控轨迹生成可直接用于具身 AI 模拟的 3D 场景。
- **视频中的时序结构利用**：`VidMap` 强调利用视频的时序结构来弥补传统 SfM 和 SLAM 的不足。`DVPSFormer` 则通过在线、流式的深度感知全景分割，服务于自动驾驶中的实时 4D 场景理解。
- **面向规划的世界模型**：`Temporal-Distance JEPA` 专门针对基于潜空间世界模型的规划问题，通过挖掘离线轨迹中的时间成本来优化表示学习，使模型更适用于长程规划。

##### 3. 多模态融合的“精细化”与“可解释性”
多模态（特别是视觉-语言模型）在 3D 理解和机器人领域的应用，正在从“能不能做”转向“做得好不好”和“为什么这么做”。
- **精细化空间推理**：`ByDeWay-V2` 针对多模态大语言模型在精细空间关系（如“左边”、“内部”）上的不足，通过注入显式的、结构化的空间谓词和深度线索，提升了推理准确性和可审计性。
- **多模态质量评估**：`SpatialQ` 从简单的 2D 图像质量评估转向 3D 场景质量评估，引入了多视图几何特征和多模态大语言模型（Qwen）进行有依据的质量推理，增加了评估的可解释性。
- **机器人操作中的模态融合**：`S2A2` 在机器人模仿学习中融合了听觉空间信息，拓展了多模态在操作性任务中的应用范围。`HiFi-UMI` 则从数据采集端出发，系统性地提升了无机器人 UMI 数据（视觉 + 动作轨迹）的保真度。

---

#### 技术路线观察

- **几何基础模型与 3D 重建**：该领域的论文（如 `JEPADepth`， `WHTMix`， `HOME`）更侧重于**效率**和**鲁棒性**。它们普遍尝试使用计算复杂度更低的算子（如 Walsh-Hadamard 变换、霍夫空间变换）或更优的预训练策略（如 JEPA）来替代计算密集型组件。同时，针对纹理稀少和结构主导的场景（如 `HOME`），提出了鲁棒的匹配方案。

- **3D/4D 重建与神经场景表示**：**3DGS** 及其变体是绝对的主流。技术路线集中在：1) **提升结构感知能力**（如 `StructureGS` 的空间一致性和结构连通性约束）；2) **提升可部署性**（如 `3DGBGS` 的模型压缩，`AtlasLC` 的无需重训练压缩，`SplatStream` 的可伸缩编码）。此外，`PanoLess` 展示了利用反射线索重建环境的独特路径。`CORF-GS` 则将 3DGS 的“神经渲染”理念“超模”到了物理层（RF 信号），显示出该方法论强大的迁移能力。

- **机器人 / AR 应用**：技术路线呈现高度**系统化**和**数据驱动**。一方面，研究者构建大一统的系统（如 `DVPSFormer` 尝试用一个网络完成深度、语义、实例跟踪）。另一方面，数据本身的重要性被极度强调：从 `HiFi-UMI` 对数据采集保真度的系统化设计，到 `S2A2` 对模态缺失（听觉）的弥补，再到 `Genie Sim PanoWorld` 对模拟数据生成的全流程设计，都体现了数据质量和可用性对下游策略学习的决定性影响。

---

#### 值得优先阅读的论文

1.  **`Wonder: Video World Model Done Better`** (arXiv: 2607.26037)
    - **优先级：最高**
    - **理由**：这项工作在视频生成、世界模型、交互控制和长期记忆四个前沿领域交汇点上取得了突破，且性能指标（16 FPS 实时生成分钟级连贯视频）极具震撼力。其提出的密集坐标场和稀疏注意力记忆机制是重要的技术贡献，对视频理解、模拟和机器人规划领域有深远影响。

2.  **`SpatialQ: Understanding 3D Gaussian Splatting Scene Quality via Visual-based MLLM`** (arXiv: 2607.26595)
    - **优先级：高**
    - **理由**：它解决了一个被长期忽视但关键的问题——**3D 场景的质量评估**。传统 2D 指标无法反映空间结构和跨视图一致性，而本文的方法首次引入多模态大语言模型（MLLM）为 3D 场景质量提供有依据的推理。这为 3DGS 重建技术的工程化、生产化和自动化提供了一种全新的评价范式，具有重要的学术和产业价值。

3.  **`Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation`** (arXiv: 2607.26646)
    - **优先级：高**
    - **理由**：它为解决具身 AI 和机器人模拟中的“数据饥渴”问题提供了一个极具吸引力的方案。从单张全景图出发，端到端地生成高质量、可自由导航的 3D 场景作为训练资产，这种“生成 + 重建”的流水线思路在效率、成本和泛化能力上都优于传统手工构建或逐场景优化的方法，是通往大规模模拟训练的关键步骤。

4.  **`VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion`** (arXiv: 2607.27194)
    - **优先级：中高**
    - **理由**：这是一篇“系统级”的整合工作，试图解决视觉定位和 3D 重建领域 SLAM 与 SfM 之间的经典矛盾。其“取其精华，去其糟粕”的设计思路清晰，且实验验证了在极端场景（视觉对称、极端运动、任意长视频）下的鲁棒性。对于研究视觉导航、SLAM 和 SfM 的读者而言，这是一项值得关注的方法论进步。

5.  **`CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting`** (arXiv: 2607.25569)
    - **优先级：中高**
    - **理由**：这是一项典型的“跨模态”迁移创新。将视觉 3DGS 的成功经验迁移到无线信道建模，解决了该领域实时性差的问题（重建时间降低 6.4 倍）。其提出的耦合优化策略（应对光与无线电

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-30T10:29:35-04:00
**Total number of papers:** 39
**Number of papers added in the latest update:** 11
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

### 2026-07

#### 2026-07-29 - SpatialQ: Understanding 3D Gaussian Splatting Scene Quality via Visual-based MLLM

**Authors:** Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao
**Links:** [abs](https://arxiv.org/abs/2607.26595) - [pdf](https://arxiv.org/pdf/2607.26595)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialQ: 基于视觉多模态大语言模型的3D高斯泼溅场景质量理解
- 作者：Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao
- 出版日期：2026-07-29（需注意该日期可能与实际发布时间存在偏差，系原文提供）
- 分类：Geometry Foundation Models（主分类）；Neural Scene Representations & Rendering（次分类）
- 链接：[摘要页](https://arxiv.org/abs/2607.26595) | [PDF](https://arxiv.org/pdf/2607.26595)

### 一句话总结
本文提出SpatialQ，一个针对3D高斯泼溅（3DGS）场景质量评估的多模态框架，通过融合多视图几何特征与视觉大语言模型，解决了传统2D质量指标难以捕捉空间结构和跨视图一致性的问题。

### 研究问题
如何对3D高斯泼溅重建的3D场景进行可靠的质量评估，使其不仅能衡量渲染视图的感知保真度，还能反映空间结构、跨视图一致性等场景级因素。

### 核心思路/方法
1. **3D感知质量表示学习**：基于VGGT编码器增加专用质量预测头，将多视图图像编码为视图特定特征并聚合，捕捉跨视图一致性。同时通过联合建模深度和点云结构信息，融入几何线索，学习超越外观特征的结构感知质量表示。
2. **基于多模态大语言模型的推理机制**：将原始图像、深度图、点云渲染图和相机参数共同输入Qwen模型（一种多模态大语言模型），实现有依据的多模态质量推理。

### 主要贡献
- 提出首个专门针对3DGS场景的多模态质量评估框架，整合3D感知质量表示与多模态大语言模型推理。
- 引入结构感知的质量学习策略，融合深度和点云几何信息，弥补传统2D质量指标在空间结构方面的不足。
- 构建了基于Qwen的多模态推理机制，将视觉与几何数据联合输入，增强对3D场景质量的解释能力。

### 局限性
- 摘要未提供实验具体结果，无法定量评估方法性能（如与其他IQA或MLLM方法的对比结果）。
- 摘要未讨论模型的计算复杂度、推理速度或对多视图数量依赖性的分析。
- 未提及是否在多种3DGS渲染场景（如大规模场景、稀疏视图等）下验证鲁棒性。

### 阅读优先级：中
**理由**：该工作针对3DGS场景质量评估这一新兴且实用的方向，方法设计合理（结合几何线索与MLLM）。但由于摘要未提供关键性能数据（如准确率、与主流方法的对比），且发布日期标注为2026年（可能存疑），建议在获取完整实验细节或验证有效性后再决定是否深入阅读。对于从事3D场景重建与质量评估研究的读者，优先级可适度提高。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as an effective representation for novel view synthesis and 3D scene reconstruction, creating an increasing demand for reliable quality assessment. Unlike conventional image quality assessment (IQA), the quality of a 3DGS scene depends not only on the perceptual fidelity of rendered views, but also on scene-level factors such as spatial structure and cross-view consistency. Existing IQA methods are limited by their reliance on 2D perceptual cues, whereas general multimodal large language models (MLLMs) are not designed for stable quality regression and may produce unreliable judgments. To address these limitations, a multimodal quality assessment framework is developed for 3DGS scene understanding. First, a 3D-aware quality representation learning framework is introduced by augmenting a VGGT-based encoder with a dedicated quality head. Multi-view images are encoded into view-specific features and aggregated to capture cross-view consistency, while geometric cues are incorporated through joint modeling of depth and point-cloud-related structural information, enabling the learning of structure-aware quality representations beyond appearance-driven features. Second, a grounded multimodal reasoning mechanism is constructed by jointly feeding original images, depth maps, point cloud renderings, and camera parameters into a Qwen-based MLLM.

</details>

#### 2026-07-23 - Self-Supervised Learning of Structured Dynamics from Videos

**Authors:** Lukas Knobel, Andrew Zisserman, Yuki M. Asano
**Links:** [abs](https://arxiv.org/abs/2607.21576) - [pdf](https://arxiv.org/pdf/2607.21576)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Self-Supervised Learning of Structured Dynamics from Videos
- 作者：Lukas Knobel, Andrew Zisserman, Yuki M. Asano
- 出版日期：2026-07-23
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.21576

### 一句话总结
本文提出了一种结构化动力学模型（SDM），通过结合自监督学习与弱监督，从预训练图像模型的视频特征中分解出相机运动和物体运动两种动态来源。

### 研究问题
如何从视频中恢复结构化的运动表征，将相机运动与物体运动分离开，以学习更稳健的动力学表示。

### 核心思路/方法
1. 利用预训练图像视觉Transformer的冻结特征。
2. 提出结构化动力学模型（SDM），通过未来帧特征预测，显式分离主导时间变化与残差动力学。
3. 训练结合了真实视频的自监督学习和合成Kubric数据上场景动力学的弱监督。
4. 在ProbeMotion评估套件上进行测试，该套件涵盖合成与真实视频中的相机运动、物体运动及混合动态。

### 主要贡献
1. 提出SDM模型，能够从预训练图像模型特征中提取结构化视频动力学表征。
2. 在自监督框架下实现相机运动与物体运动的分离，无需强监督。
3. 在ProbeMotion评测中，SDM优于使用全局CLS或平均池化特征的基线，并与强监督VGGT方法相比表现相当，但使用更弱的监督。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：本文针对视频理解中相机运动与物体运动解耦这一重要且未充分探索的问题，提出了结合自监督与弱监督的结构化动力学模型，在较弱的监督下取得了与强监督方法相当的效果，对运动表征学习研究具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Understanding motion in video is a fundamental challenge for visual learning, as frame-to-frame change entangles two sources of dynamics: camera motion and object motion. This decomposition has remained underexplored in representation learning, partly because these factors are tightly coupled in natural videos and difficult to supervise separately. Yet recovering it is important for learning robust motion representations that separate meaningful object dynamics from camera-induced variation. We study whether such structured motion representations can be recovered from frozen features of a pretrained image vision transformer. We propose the Structured Dynamics Model (SDM), which explicitly separates the dominant source of temporal change from residual dynamics through future-feature prediction, rather than representing video change with a single entangled latent or with unstructured, spatially dense transition tokens. Training combines self-supervised learning on real video with weak supervision of scene dynamics on synthetic Kubric data. We evaluate SDM on ProbeMotion, a new evaluation suite spanning synthetic and real videos with camera motion, object motion, and combined dynamics. SDM outperforms backbone baselines using global CLS or average-pooled features, and compares favorably to strongly supervised representations such as VGGT on several probes, despite using substantially weaker supervision. These results suggest that pretrained image models can be readily repurposed into structured video-dynamics representations, providing a useful inductive bias for learning and analyzing latent video dynamics.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

#### 2026-07-28 - SplatStream: Fine Granular Scalable Gaussian Splatting for Adaptive 3D Scene Streaming

**Authors:** Muhammad Talha, William Gordon, Sajid Umair, Zhu Li, Anique Akhtar, Joel Jung
**Links:** [abs](https://arxiv.org/abs/2607.25971) - [pdf](https://arxiv.org/pdf/2607.25971)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic Gaussian, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatStream: Fine Granular Scalable Gaussian Splatting for Adaptive 3D Scene Streaming
- 作者：Muhammad Talha, William Gordon, Sajid Umair, Zhu Li, Anique Akhtar, Joel Jung
- 出版日期：2026-07-28
- 分类：Dynamic / 4D Reconstruction（主分类）；Neural Scene Representations & Rendering（副分类）
- 链接：摘要：https://arxiv.org/abs/2607.25971 ；PDF：https://arxiv.org/pdf/2607.25971

### 一句话总结
提出一个名为 SplatStream 的细粒度可伸缩高斯泼溅框架，用于动态3D场景的适应性流传输，通过质量/分辨率分层、层间预测编码、B帧时域扩展及体积-不透明度重要性度量，实现低延迟、带宽自适应的流媒体传输。

### 研究问题
动态3D高斯泼溅（GS）表征尺寸大、帧间冗余高，导致其在适应性流传输场景下（如带宽波动环境）面临显著挑战。

### 核心思路/方法
1. **空间可伸缩性**：将GS场景分解为质量层和分辨率层，引入层间预测编码实现可伸缩性。
2. **时域可伸缩性**：引入B帧以提供时域质量可伸缩性。
3. **预测机制**：使用轻量级基于跨层Transformer的预测器，用于跨层和时域预测。
4. **重要性分组**：基于体积-不透明度度量对高斯原语进行细粒度打包，优先传输视觉重要性高的原语，实现渐进式细化。
5. **流传输适配**：将可伸缩GS比特流映射为兼容MPEG-DASH的子表示结构，支持细粒度自适应、低延迟传输。

### 主要贡献
1. 提出一种细粒度可伸缩的高斯泼溅框架，支持动态3D场景的适应性流传输。
2. 引入跨层预测编码和B帧机制，实现空间与时域的可伸缩性。
3. 利用体积-不透明度重要性度量进行高斯原语分组与优先传输，提升渐进式反馈质量。
4. 将可伸缩比特流与MPEG-DASH流媒体标准对接，实现在带宽波动下的低延迟自适应传输。

### 局限性
摘要未提供足够信息。该部分需阅读全文后分析。

### 阅读优先级
**高**。理由：该工作针对动态高斯泼溅在流传输中的核心难点——表征冗余与带宽适配——提出了完整的可伸缩方案，并涉及层间预测、Transformer、MPEG-DASH标准对接等多个技术点，对NeRF/3D GS领域及多媒体流传输研究均有参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (GS) enables high quality real-time rendering for immersive media, but its large representation size and frame-wise redundancy create significant challenges for adaptive streaming. This paper presents SplatStream, a fine granular scalable Gaussian splatting framework for dynamic 3D scene delivery. The proposed method decompose the GS scenes into quality and resolution layers, and introduces inter-layer predictive coding to achieve scalability. For temporal direction, B-frames are introduced to have temporal quality scalability. A lightweight cross-layer transformer based predictor is utilized for both cross layer and temporal predictions. In addition, a volume-opacity based importance measure is used for fine-grained Gaussian packetization, allowing visually important primitives to be transmitted earlier for progressive refinement. Finally, the scalable GS bitstream is mapped to an MPEG-DASH compatible sub-representation structure, enabling fine granular adaptive, low-latency delivery of dynamic Gaussian splatting content under bandwidth-varying conditions.

</details>

#### 2026-07-23 - GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis

**Authors:** Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian
**Links:** [abs](https://arxiv.org/abs/2607.21448) - [pdf](https://arxiv.org/pdf/2607.21448)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis
- 作者：Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian
- 出版日期：2026-07-23
- 分类：Dynamic / 4D Reconstruction; Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2607.21448; PDF: https://arxiv.org/pdf/2607.21448

### 一句话总结
GrainGS 提出了一种结合层级锚定结构与每高斯形变的动态框架，通过梯度解耦、静态预热和规范残差外观分解，实现了动态场景的高质量、实时与紧凑的渲染。

### 研究问题
如何平衡动态场景重建中对细微运动建模、结构稳定性和紧凑表示的需求，避免现有方法（如每基元方法导致冗余增长、锚定方法抑制局部运动）的不足。

### 核心思路/方法
1. **层级锚定+每高斯形变**：结合层级锚定支架（anchor scaffold）与每个高斯独立的形变能力，实现结构约束下的局部运动建模。
2. **静态预热阶段**：在所有时间戳观测数据上建立一个时间不变的规范表示。
3. **梯度解耦操作**：在联合训练中，使用 stop-gradient 操作阻断通过形变传递到规范位置的梯度路径，同时保留通过重建目标对规范位置的直接优化。
4. **规范-残差外观分解**：将帧依赖的光度变化建模为规范残差，而非强制纳入几何形变。

### 主要贡献
1. 提出了 GrainGS 框架，实现了高重建质量、实时新视角合成和紧凑存储。
2. 在合成单目和真实多视图基准上，达到平均峰值信噪比36.98分贝、渲染速度435.6帧每秒、存储需求4.67兆字节。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对动态场景重建中的关键权衡问题（运动建模、稳定性、紧凑性）提出了创新性框架，且实验指标突出（36.98 dB PSNR、435.6 FPS、4.67 MB存储），在动态/4D重建和神经渲染领域具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic scene reconstruction with 3D Gaussian Splatting requires a balance between fine-grained motion modeling, structural stability, and compact representation. Existing per-primitive methods provide flexible local deformation but often suffer from redundant primitive growth, while anchor-based methods improve spatial regularity at the cost of suppressing locally varying motion. To address these issues, we present GrainGS, a dynamic Gaussian framework that combines a hierarchical anchor scaffold with per-Gaussian deformation. A static warm-up stage first establishes a time-invariant canonical representation from observations across all timestamps. During joint training, a stop-gradient operation blocks the deformation-mediated gradient pathway to the canonical positions while preserving their direct refinement through the reconstruction objective. Each Gaussian then predicts independent temporal offsets for position, rotation, and scale, enabling detailed local motion within a structurally constrained scaffold. A canonical-residual appearance decomposition further models frame-dependent photometric changes without forcing them into geometric deformation. Experiments on synthetic monocular and real-world multiview benchmarks show that GrainGS achieves high reconstruction quality, real-time novel view synthesis, and compact storage. Under the synthetic benchmark setting, it reaches an average peak signal-to-noise ratio of 36.98 decibels, renders at 435.6 frames per second, and requires 4.67 megabytes of storage.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-29 - VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion

**Authors:** Zador Pataki, Paul-Edouard Sarlin, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2607.27194) - [pdf](https://arxiv.org/pdf/2607.27194)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** image matching, structure from motion, SfM, simultaneous localization and mapping, SLAM, monocular depth, camera calibration, mapping, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion
- 作者：Zador Pataki, Paul-Edouard Sarlin, Marc Pollefeys
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2607.27194

### 一句话总结
本文提出VidMap系统，通过融合SLAM的时序约束与离线SfM的全局优化能力，实现了任意未校准长视频的度量重建。

### 研究问题
现有视频位姿恢复方法存在局限：SLAM依赖初始化、对瞬态故障敏感且需已知相机校准；SfM忽略图像顺序，在视觉对称和极端运动场景下鲁棒性不足。因此，该文致力于解决如何结合两种方法的优势，实现鲁棒且准确的视频度量重建。

### 核心思路/方法
- 结合SLAM的强时序约束与SfM的全局优化灵活性，将时间顺序作为闭环检测的关键信息。
- 利用近期宽基线密集图像匹配的进展提升匹配质量。
- 使用度量单目深度先验增强全局优化过程。

### 主要贡献
- 提出一种新系统，融合SLAM时序约束与离线SfM全局优化，支持未校准视频的度量重建。
- 将时序信息作为闭环检测的“一等公民”，提升可靠性。
- 在包含极端运动和视觉对称的多样困难数据集上，比现有经典/学习的SLAM和SfM方法（无论是否已知校准）更鲁棒、更准确。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该文针对视频重建领域SLAM与SfM的矛盾提出融合方案，技术思路清晰且实验验证鲁棒性优势，适合对3D重建、视觉SLAM或机器人导航感兴趣的读者；但摘要未提及具体性能指标与消融实验细节，需进一步阅读正文判断方法可复现性和实际效果。

</details>

<details>
<summary>Abstract</summary>

Accurately recovering the camera's calibration and metric poses for any unconstrained video would unlock large-scale training data for navigation and scene understanding. The dominant approaches to this problem are severely limited: Simultaneous Localization and Mapping (SLAM) is sensitive to initialization and transient failures due to its causal, incremental nature; it is often over-optimized for real-time operation and generally requires known camera calibration; while Structure-from-Motion (SfM) typically forgoes any image ordering, enabling optimal initialization and global optimization, but lacks robustness to visual symmetries and extreme motions. To bridge this gap, we introduce a system that combines the strong sequential constraints of SLAM with the flexibility and global optimization of offline SfM, enabling the metric reconstruction of arbitrary, long, uncalibrated videos. This system leverages recent advances in wide-baseline dense image matching, treats temporal ordering as a first-class citizen for reliable loop closure, and augments global optimization with metric monocular depth priors. As a result, thorough evaluations on diverse, challenging datasets that exhibit extreme motion and visual symmetries reveal that our approach is significantly more robust and accurate than both state-of-the-art SLAM and SfM, classical or learned, with given or unknown camera calibration. The code is publicly available at https://github.com/cvg/vidmap.

</details>

#### 2026-07-29 - Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for Decision-Critical Applications

**Authors:** Piyush Jain, Kousik Dasgupta, Rajarshi Roy, Subarna Tripathi
**Links:** [abs](https://arxiv.org/abs/2607.27145) - [pdf](https://arxiv.org/pdf/2607.27145)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, monocular depth, embodied AI, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for Decision-Critical Applications
- 作者：Piyush Jain, Kousik Dasgupta, Rajarshi Roy, Subarna Tripathi
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry; Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.27145

### 一句话总结
本文提出ByDeWay-V2框架，通过向多模态大语言模型（MLLM）的提示中注入显式的空间关系谓词和深度线索，在无需训练的情况下提升了空间推理的准确性和可审计性，尤其适合资源受限的实时决策场景。

### 研究问题
多模态大语言模型在关键决策应用（如机器人、具身AI）中，其空间判断不透明且存在细粒度空间理解不足和物体幻觉问题；现有方法（如ByDeWay的LDP）在处理同一几何平面内物体间的投影和拓扑空间关系时表现不足。

### 核心思路/方法
- 采用开放词汇物体检测器（YOLO-World-L）计算图像中检测到的物体之间的成对几何关系。
- 将这些关系转化为人类可读的结构化空间谓词（如“left of”、“inside”等），并将其与深度线索（来自单目深度估计）一起注入MLLM的提示中。
- 整个流程无需训练，将3D场景深度与2D空间语义桥接，同时提供可审计的证据以支持下游决策。

### 主要贡献
1. 提出了ByDeWay-V2框架，通过显式空间关系谓词增强MLLM的空间推理能力，同时保持可解释性。
2. 在VSR和BLINK空间推理子集上，该框架显著提升了多个MLLM的性能：例如在BLINK空间子集上，对于Qwen2.5-VL，相对于LDP方法F1分数相对提升46%；将BLIP-Base在VSR上的近乎随机性能恢复至F1=0.53。
3. 提供轻量级配置（在CPU上仅需40个token上下文预算），证明了框架在资源受限实时决策场景中的适用性。

### 局限性
摘要未提供足够信息（如具体失败案例、对其他任务或更大模型的影响、深度估计误差的影响等）。

### 阅读优先级
中
- 理由：该工作专注于视觉空间推理这一具体方向，并提出了实用的轻量级改进方法（无需训练）。对于从事具身AI、机器人及可解释AI的研究者有一定参考价值，但对于广义的计算机视觉或语言模型研究者，其方法限定性较强。

</details>

<details>
<summary>Abstract</summary>

As Multimodal Large Language Models (MLLMs) are increasingly deployed in decision-critical pipelines such as robotics, embodied AI, and safety monitoring, the opacity of their spatial judgments limits operator trust and auditability. MLLMs demonstrate strong reasoning but often struggle with fine-grained spatial understanding and object hallucination. Prior work, ByDeWay, introduced Layered-Depth-Based Prompting (LDP), a training-free framework that mitigates hallucinations by structuring prompts using monocular depth estimation. However, coarse depth layering falls short in resolving object-to-object spatial relationships within the same geometric plane, such as projective ("left of", "above") and topological ("inside", "touching") relations. We propose ByDeWay-V2, which integrates explicit spatial relational context alongside depth cues, expressed as human-readable predicates that serve as auditable evidence for downstream decision support. Using an open-vocabulary object detector (YOLO-World-L), our framework computes pairwise geometric relations between detected objects and injects them as structured spatial predicates into the MLLM prompt, bridging 3D scene depth and 2D spatial semantics without any training. We evaluate ByDeWay-V2 on the Visual Spatial Reasoning (VSR) and BLINK benchmarks across multiple MLLMs, with hallucination grounding assessed via POPE. On the BLINK spatial subset, ByDeWay-V2 achieves a 46 percent relative F1 improvement over LDP for Qwen2.5-VL, and recovers BLIP-Base's spatial reasoning on VSR from near-random performance to a competitive F1 of 0.53. Our lightest configuration operates under a strict 40-token context budget on CPU, showing the framework's suitability for resource-constrained, real-time decision-support settings.

</details>

#### 2026-07-29 - JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation

**Authors:** Ionuţ Grigore, Călin-Adrian Popa
**Links:** [abs](https://arxiv.org/abs/2607.26600) - [pdf](https://arxiv.org/pdf/2607.26600)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation
- 作者：Ionuţ Grigore, Călin-Adrian Popa
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.26600

### 一句话总结
JEPADepth 提出一种自监督单目深度估计方法，在标准光度损失基础上，引入基于I-JEPA的掩码预测表示学习损失，以提升模型性能，且在推理时不增加额外开销。

### 研究问题
如何通过引入掩码预测表示学习来增强自监督单目深度估计中基于光度重建损失的训练效果，同时不改变推理时的模型结构。

### 核心思路/方法
1. 在标准光度重建流程上，增加一个基于预训练DINOv3 Vision Transformer编码器的掩码预测损失（JEPA目标）。
2. 该损失在表示空间中计算：一个预测器根据可见上下文区域的嵌入，推断被掩码的目标区域嵌入；目标编码器和预测器仅在训练阶段使用，推理时丢弃。
3. 整体框架在KITTI上训练，与同一DINOv3光度基线对比，性能有提升。

### 主要贡献
摘要未提供足够信息以提取独立贡献列表。从摘要可推断：提出了一种结合I-JEPA的掩码预测损失与光度损失的深度估计框架，在三个公开基准（KITTI、Make3D、Cityscapes）上取得有竞争力的结果，尤其在零样本迁移场景下达到最佳或接近最佳性能。

### 局限性
摘要未提供关于局限性、失败案例或计算成本等信息，因此无法进行分析。

### 阅读优先级
中  
理由：该方法在自监督深度估计领域表现出竞争力，零样本迁移性能突出，但创新点主要是将现有I-JEPA损失嫁接到光度框架上，且实验细节未深入给出。如关注自监督表示学习与深度估计结合，可阅读；若需理论突破或详尽实验分析，优先级较低。

</details>

<details>
<summary>Abstract</summary>

Self-supervised monocular depth estimation typically relies on photometric reconstruction losses that couple depth, pose, and appearance assumptions. In this paper, we propose JEPADepth, a self-supervised monocular depth framework that incorporates a complementary training objective inspired by Image Joint-Embedding Predictive Architectures (I-JEPA) for self-supervised depth learning. Our method augments a standard photometric pipeline with a masked prediction loss computed in the representation space of a pretrained DINOv3 Vision Transformer encoder. A predictor infers target-region embeddings from visible context-region embeddings under structured masking, and is discarded along with the target encoder at inference time, adding no deployment cost. On KITTI, adding the JEPA objective consistently improves performance over the same DINOv3-based photometric baseline, without changing the inference-time architecture. Compared to prior monocular self-supervised methods, JEPADepth is competitive with state-of-the-art transformer-based approaches and outperforms strong CNN-based baselines on the standard benchmark. In zero-shot transfer (trained on KITTI and evaluated without fine-tuning), JEPADepth achieves the best or near-best performance among the compared methods on both Make3D and Cityscapes across multiple metrics.

</details>

#### 2026-07-28 - HOME: Robust Hough-space Matching Method for Structured and Textureless Videos

**Authors:** Masaki Satoh
**Links:** [abs](https://arxiv.org/abs/2607.25389) - [pdf](https://arxiv.org/pdf/2607.25389)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, pose estimation, feature matching, robotics, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HOME: Robust Hough-space Matching Method for Structured and Textureless Videos  
- 作者：Masaki Satoh  
- 出版日期：2026-07-28  
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications  
- 链接：摘要：https://arxiv.org/abs/2607.25389 ；PDF：https://arxiv.org/pdf/2607.25389  

### 一句话总结
提出一种基于霍夫空间的超轻量、免训练特征匹配框架HOME，通过将图像中的全局线性结构映射为稳定局部极值，将复杂线条匹配简化为高效的一维点匹配，在结构化和无纹理场景中实现鲁棒且快速的单应性估计。

### 研究问题
如何在计算资源有限的边缘设备上，针对结构化环境（强线性结构）或无纹理表面，实现高效、鲁棒的视觉特征匹配，从而解决现有基于点特征（如ORB）在这些场景中频繁失败、而基于线条的SLAM方法计算量过大的瓶颈问题。

### 核心思路/方法
1. **霍夫空间变换**：将输入图像转换到霍夫空间，把全局线性结构映射为稳定的局部极值，并将这些极值作为关键点。  
2. **一维点匹配**：将复杂的线条匹配问题重构成高效的一维点匹配任务。  
3. **一维径向描述子**：设计具有数学保证的旋转和平移不变性的描述子，无需显式估计方向，降低计算开销。  
4. **验证方式**：以单应性估计作为概念验证，评估匹配精度和效率。

### 主要贡献
- 提出HOME框架，首次将线条匹配通过霍夫空间转换为轻量级的一维点匹配，避免了传统线条提取与描述的昂贵计算。  
- 数学上保证了一维径向描述子的旋转和平移不变性，无需方向估计步骤。  
- 实验表明：在基于点特征方法失败的结构化/无纹理场景中，HOME仍能实现鲁棒配准，且运行速度远快于现有基于线条的方法。

### 局限性
- 摘要仅说明本文聚焦于单应性估计作为概念验证，未提供全3D位姿估计的实验细节。  
- 摘要未提供任何关于算法实时性定量数据、与其他方法的具体速度对比数值、以及在更多场景下的鲁棒性测试结果。  
- 摘要明确提及“将稳健匹配引擎扩展到全3D位姿估计仍是未来方向”，表明当前工作尚未覆盖3D位姿估计。  

### 阅读优先级
**高**  
理由：该方法针对边缘计算中的实时匹配瓶颈提出新颖且轻量的思路，在结构化和无纹理场景中具有显著优势。尽管当前验证限于2D单应性估计，但其基础框架对机器人、AR等实时应用具有潜在价值，适合对轻量化特征匹配感兴趣的研究者。

</details>

<details>
<summary>Abstract</summary>

Visual front-ends for robotic localization typically rely on point-based features such as Oriented FAST and Rotated BRIEF (ORB), which frequently fail in structured environments dominated by strong linear structures or textureless surfaces. While line-based Simultaneous Localization and Mapping (SLAM) systems mitigate this by utilizing line segments, conventional line extraction and description algorithms are computationally prohibitive for real-time edge robotics. To address this fundamental bottleneck, we propose HOME (Hough-space One-dimensional Matching of Extrema), an ultra-lightweight, training-free feature matching framework. HOME transforms images into Hough space, mapping global linear structures to stable local extrema, which serve as keypoints, thereby reformulating complex line matching into highly efficient one-dimensional point matching. The proposed 1D radial descriptor mathematically guarantees rotational and translational invariance without the overhead of explicit orientation estimation. As a proof of concept to validate the matching accuracy and efficiency of HOME, this paper focuses on homography estimation. Extensive evaluations demonstrate that HOME achieves robust registration in challenging scenarios where point-based methods fail, operating at a much faster speed than existing line-based methods. Extending this robust matching engine to full 3D pose estimation remains a highly promising future direction.

</details>

#### 2026-07-28 - WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing

**Authors:** Prathyush Sajith, Emadeldeen Hamdan, Ahmet Enis Cetin
**Links:** [abs](https://arxiv.org/abs/2607.25234) - [pdf](https://arxiv.org/pdf/2607.25234)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, stereo depth, robotics, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing
- 作者：Prathyush Sajith, Emadeldeen Hamdan, Ahmet Enis Cetin
- 出版日期：2026-07-28
- 分类：3D Reconstruction & Multi-view Geometry（主要），Embodied / Robotics / AR Applications（次要）
- 链接：摘要：https://arxiv.org/abs/2607.25234；PDF：https://arxiv.org/pdf/2607.25234

### 一句话总结
本文提出用数据无关的Walsh-Hadamard token mixer替代立体深度估计Transformer中的全局自注意力，在对数线性复杂度下保持精度，并引入混合对数视差损失以提升远距离物体估计性能。

### 研究问题
立体深度估计算法（用于驾驶、机器人和增强现实）需在高分辨率下快速运行，而基于Transformer的立体匹配器中，全局自注意力的计算复杂度随像素数平方增长，成为推理延迟的主要瓶颈。

### 核心思路/方法
1. 将立体Transformer中的联合自注意力阶段替换为数据无关的Walsh-Hadamard token mixer，该混频器在变换域以对数线性成本全局混合token，而保留数据相关的交叉注意力用于左右视图对应。
2. 引入混合对数视差损失函数，对代表远距离物体的小视差像素赋予更高权重，以提升远处物体估计精度且不增加额外计算开销。

### 主要贡献
- 提出Walsh-Hadamard token mixer替代全局自注意力，在合成驾驶数据上将模型计算量降低2.46倍，单图像推理延迟降低2.65倍，且端点误差与注意力基线持平。
- 通过复杂度分析揭示该方法优势受序列长度与通道宽度比值主导，解释了其在高分辨率立体匹配中的适用性及在分类Transformer中的不适用性，并在非立体长序列基准上验证了这种token-通道缩放规律。
- 引入混合对数视差损失，在不增加计算开销的前提下减少远距离物体的误差。

### 局限性
摘要未提供足够信息。摘要未讨论模型在真实驾驶/机器人数据上的鲁棒性、泛化能力、硬件部署细节，也未对比其他高效注意力变体或提供消融实验的量化误差率。

### 阅读优先级
高  
理由：该工作直接针对立体深度估计的实时性核心瓶颈，提供了理论清晰（复杂度分析）、实验验证（计算和延迟大幅下降，精度持平）且实用（损失函数提升远距离物体性能）的解决方案，对高分辨率实时应用场景具有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Stereo depth estimation for driving, robotics and augmented reality must run at high resolution under tight latency budgets, yet in transformer-based matchers the global self-attention that aggregates scene context grows quadratically with the number of pixels and comes to dominate runtime. We show that the joint self-attention stage of a stereo transformer, whose role is to spread context across both views, can be replaced by a data-independent Walsh-Hadamard token mixer that mixes tokens globally in the transform domain at log-linear cost, while the data-dependent cross-attention that performs left-right correspondence is retained. On synthetic driving data the mixer matches the attention baseline in end-point error while reducing model compute by a factor of 2.46 and single-image inference latency by a factor of 2.65. A complexity analysis shows the benefit is governed by the ratio of sequence length to channel width, which explains why high-resolution stereo matching is a particularly favorable setting and why classification transformers are not; we confirm this token-to-channel scaling on non-stereo long-sequence benchmarks. Furthermore, we introduce a hybrid log-disparity loss function designed to up-weight small-disparity pixels corresponding to long-range objects. This approach reduces the error on distant objects without incurring any additional computational overhead.

</details>

#### 2026-07-27 - NSL-SLAM: High-Fidelity Neural Structured-Light Depth for Practical SLAM and Reconstruction

**Authors:** Jiaheng Li, Binsheng Zhang, Xinhai Chang, Wenzheng Chen
**Links:** [abs](https://arxiv.org/abs/2607.24495) - [pdf](https://arxiv.org/pdf/2607.24495)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NSL-SLAM: High-Fidelity Neural Structured-Light Depth for Practical SLAM and Reconstruction
- 作者：Jiaheng Li, Binsheng Zhang, Xinhai Chang, Wenzheng Chen
- 出版日期：2026-07-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.24495

### 一句话总结
本文提出了一种针对高保真结构光深度定制的SLAM系统NSL-SLAM，通过融合单目深度先验增强深度估计精度，并设计以深度为中心的SLAM管线，实现了高精度、鲁棒且实时的SLAM与重建。

### 研究问题
如何利用高保真结构光深度传感器提升SLAM系统的跟踪精度和重建质量，并使其在实际应用中做到鲁棒、高效且实时运行。

### 核心思路/方法
1. **增强深度估计**：在已有神经结构光（NSL）方法基础上，融入强单目深度先验，用于结构光立体解码，将深度的RMSE降低35%（在Replica-SL上）。
2. **深度为中心的SLAM管道**：由于结构光几何具有密集且度量准确的特点，将其作为主跟踪信号；仅在几何退化情况下使用稀疏视觉对应点，并通过轻量级束调整来处理远程漂移。
3. **深度估计与SLAM协同**：更精确的深度使得简单的SLAM管线有效，而深度为中心的管线确保这种优势传递到下游重建中。

### 主要贡献
- 提出了NSL-SLAM，首个针对高保真结构光深度设计的实用SLAM系统。
- 通过融合单目深度先验，显著改进了神经结构光深度估计的精度。
- 设计了一个以深度为核心、兼顾稀疏视觉点和轻量级优化的SLAM管线。
- 在合成Replica-SL基准上达到最佳跟踪精度，并将重建F-score提升1.6个点（与SOTA基线相比，在共享深度协议下）。
- 在真实8个挑战性场景的基准上，是唯一在所有序列上避免灾难性失败的方法，同时轨迹偏差比所选基线低43.3%。
- 系统能以20.9 FPS在线运行，实现了实用、鲁棒的SLAM。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法在合成和真实基准上均取得显著性能提升（重建F-score提升1.6点，轨迹偏差降低43.3%），且实现了实时在线运行（20.9 FPS）；设计思路清晰（深度优先、协同强化），对SLAM与深度感知交叉领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Structured-light (SL) cameras power depth sensing in millions of devices, and recent neural SL decoding methods have substantially improved their depth quality. SLAM systems can benefit greatly from such strong depth sensing, where reliable geometry enables stable tracking and faithful reconstruction. In this work, we present NSL-SLAM, a practical SLAM system tailored for high-fidelity structured-light depth. We first strengthen SL depth sensing: inspired by the neural structured-light (NSL) method, we further incorporate strong monocular depth priors into the SL stereo decoding, reducing depth RMSE by 35% on Replica-SL compared to NSL. We then build a depth-centric SLAM pipeline with this stronger depth: because structured-light geometry is dense and metrically accurate, we keep it as the primary tracking signal, and add only sparse visual correspondences for geometrically degenerate cases and lightweight bundle adjustment for long-range drift. Our depth estimator and SLAM design reinforce each other: stronger depth makes a simple SLAM pipeline effective, and the depth-centric pipeline ensures this advantage transfers to downstream reconstruction. Experimentally, on the synthetic Replica-SL benchmark, NSL-SLAM achieves the best tracking accuracy and improves reconstruction F-score by 1.6 points over the SOTA baseline under a shared-depth protocol. On a real benchmark of 8 challenging scenes, it is the only method that avoids catastrophic failure on all sequences while achieving 43.3% lower trajectory deviation than selected baselines. The SLAM system runs online at 20.9 FPS, demonstrating that stronger structured-light depth and depth-centric system design together enable practical, robust SLAM.

</details>

#### 2026-07-27 - MSVS-VAE: Multi-Scale Anchored VecSet for High-Fidelity 3D Reconstruction

**Authors:** Dehao Hao, Kaiyi Zhang, Tanghui Jia, Xiangjun Gao, Dongyu Yan, Weikai Chen, Zeyu Hu, Lingting Zhu, Yingda Yin, Runze Zhang, Li Yuan, Xin Wang, Long Quan
**Links:** [abs](https://arxiv.org/abs/2607.24436) - [pdf](https://arxiv.org/pdf/2607.24436)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MSVS-VAE: Multi-Scale Anchored VecSet for High-Fidelity 3D Reconstruction
- 作者：Dehao Hao, Kaiyi Zhang, Tanghui Jia, Xiangjun Gao, Dongyu Yan, Weikai Chen, Zeyu Hu, Lingting Zhu, Yingda Yin, Runze Zhang, Li Yuan, Xin Wang, Long Quan
- 出版日期：2026-07-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.24436

### 一句话总结
MSVS-VAE 提出了一种基于分层集合的 VAE，通过渐进式稠密化、局部聚合算子和多尺度查询解码，在保持紧凑性的同时实现了高保真 3D 重建，显著优于现有基于体素和集合的方法。

### 研究问题
现有 3D 生成建模中，潜在扩散范式的重建质量受限于底层 3D VAE。基于稀疏体素的方法重建质量好但计算开销大，基于集合的方法紧凑但保真度低，主要原因是潜在表示稀疏且全局过于平滑。

### 核心思路/方法
1. **分层点洗牌上采样**：通过分层渐进式稠密化锚定 VecSet 潜在表示，增加空间容量以支持细粒度几何建模。
2. **AVS-Conv 局部聚合算子**：用几何感知的局部邻域聚合替代全局交叉注意力，实现高效解码。
3. **多尺度查询解码**：融合粗细尺度特征，粗尺度提供稳定全局上下文，细尺度细化局部几何，减少局部感受野造成的伪影。

### 主要贡献
- 提出 MSVS-VAE，一种分层集合 VAE，在不牺牲紧凑性的前提下弥合了保真度差距。
- 引入 AVS-Conv 局部聚合算子，替代全局注意力的计算瓶颈，显著加速解码（约 10 倍于先前集合方法）。
- 在 Objaverse、ABO 和野外基准上，MSVS-VAE 一致优于先前集合和体素 VAE，紧凑性约为体素基线方法的 10 倍。

### 局限性
摘要未提供足够信息（如对特定类型输入或遮挡的处理效果、计算资源消耗、潜在失败模式等）。仅从摘要看，未讨论泛化性、鲁棒性或负样本。

### 阅读优先级
**高**  
理由：该工作针对 3D 生成建模中的关键瓶颈（VAE 重建质量与紧凑性权衡）提出了新颖且高效的分层集合方案，实验在多个基准上取得显著优势，且解码速度提升明显，对从事 3D 重建、生成模型的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

High-fidelity 3D generative modeling increasingly relies on the latent diffusion paradigm, where the reconstruction quality of the underlying 3D VAE becomes a primary bottleneck. Existing approaches largely follow two paradigms: sparse voxel-based representations achieve strong reconstruction quality but incur significant memory and computational overhead, while set-based representations are compact and continuous yet typically lag in fidelity due to latent sparsity and excessive global smoothness. We propose MSVS-VAE, a hierarchical set-based VAE that closes this fidelity gap without sacrificing compactness. Our key idea is to progressively densify anchored VecSet latents via hierarchical point-shuffle upsampling, increasing spatial capacity for fine-grained geometry modeling. To efficiently decode from the densified hierarchy, we replace global cross-attention with AVS-Conv, a geometry-aware local aggregation operator operating within local neighborhoods rather than the exhaustive latent set. We further introduce multi-scale query decoding to fuse coarse-to-fine latent features, where coarse scales provide stable global context, and fine scales refine localized geometry, reducing artifacts from overly local receptive fields. Extensive experiments on Objaverse, ABO, and in-the-wild benchmarks demonstrate that MSVS-VAE consistently outperforms prior set-based and voxel-based VAEs, delivering approximately 10x faster decoding than prior set-based methods and approximately 10x higher compactness than voxel-based baselines.

</details>

#### 2026-07-27 - Accuracy potential of visual localization exploiting high-end street-level imagery

**Authors:** Jonas Meyer, Stephan Nebiker, Pascal Theiler, Norbert Haala
**Links:** [abs](https://arxiv.org/abs/2607.24409) - [pdf](https://arxiv.org/pdf/2607.24409)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** motion reconstruction, structure from motion, pose estimation, scene representation, robotics, mapping, localization, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：基于高端街道级影像的视觉定位精度潜力
- 作者：Jonas Meyer, Stephan Nebiker, Pascal Theiler, Norbert Haala
- 出版日期：2026-07-27
- 分类：3D重建与多视图几何；具身/机器人/AR应用
- 链接：摘要原文：https://arxiv.org/abs/2607.24409；PDF：https://arxiv.org/pdf/2607.24409；数据集：https://fhnw-muttenz-vl-dataset.github.io/

### 一句话总结
本文提出一种使用高精度地理参考街道影像的可扩展视觉定位流程，并发布了包含亚厘米级真值位姿的户外数据集，实验表明其定位精度可达1–5厘米平移和0.05–0.1°旋转，可满足测量级GNSS的互补需求。

### 研究问题
视觉定位能否达到测量级（survey-grade）精度要求，尤其是在缺乏大规模、亚厘米级真值姿态的公开户外数据集的情况下。

### 核心思路/方法
1. **流程设计**：构建一个可扩展的视觉定位管线，直接使用精确地理参考的高分辨率街道级影像作为场景表示；包含先验引导的参考候选选择、即时局部运动恢复结构（SfM）重建和基于PnP的位姿估计。
2. **数据集构建**：发布FHNW Muttenz数据集——覆盖10公里连续街道网络，通过两次移动测绘（间隔约1.5年）采集；包含高分辨率参考影像和来自四台不同相机的查询序列，所有图像均精确配准，提供亚厘米级6自由度真值位姿。
3. **实验评估**：在该数据集上评估视觉定位精度，获得中位平移精度1–5厘米、旋转精度0.05–0.1°，有利条件下可达1厘米和0.03°。

### 主要贡献
1. 提出了一种利用高端街道级影像的可扩展视觉定位流程，无需传统3D地图即可实现高精度定位。
2. 发布了一个公开可用的户外数据集（FHNW Muttenz），包含亚厘米级真值位姿，填补了现有大型数据集在测量级精度评估方面的空白。
3. 通过系统实验证明了视觉定位可以达到与测量级GNSS互补的精度水平，为消费级设备获取3D地理空间数据和全自动地理参考方法铺平道路。

### 局限性
摘要未提供足够信息，例如方法对光照或季节变化的鲁棒性、实时性、计算成本，以及数据集规模或场景多样性方面的潜在限制。

### 阅读优先级
**高**。理由：该论文直接针对视觉定位在测量级应用中的精度潜力这一关键问题，提供了开创性的评估方法和首个亚厘米级真值户外数据集，对自动驾驶、机器人、AR及地理空间数据采集领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate and reliable pose information with respect to a reference frame is increasingly demanded across applications such as autonomous navigation, surveying, robotics, and augmented and mixed reality. Visual localization can serve as a complementary positioning modality to GNSS, whose applicability and accuracy are often limited. Yet, the accuracy potential of visual localization has not been systematically investigated against survey-grade demands. This is mainly due to the lack of publicly available, large-scale outdoor datasets with ground-truth poses in the sub-centimeter range. In this work, we address both gaps. We introduce a scalable visual localization pipeline that employs precisely georeferenced, high-resolution street-level imagery directly as the scene representation. It combines prior-guided reference candidate selection with on-the-fly local Structure-from-Motion reconstruction and PnP-based pose estimation. We further present the FHNW Muttenz dataset, a real-world dataset covering a contiguous 10 km street network mapped in two mobile mapping campaigns approximately 1.5 years apart. It consists of high-resolution reference imagery and query sequences acquired by four different cameras across five representative scenes. All images are precisely co-registered, yielding 6-DoF ground-truth poses in the sub-centimeter range. Using this dataset, we evaluate the accuracy potential of visual localization. Our experiments demonstrate median pose accuracies in the range of 1-5 cm for translation and 0.05-0.1° for rotation, reaching as low as 1 cm and 0.03° under favorable conditions. These results show that visual localization can complement survey-grade GNSS positioning, paving the way for 3D geospatial data acquisition using consumer devices and fully automated georeferencing approaches. The dataset is publicly available at: https://fhnw-muttenz-vl-dataset.github.io/.

</details>

#### 2026-07-27 - SILICA: Repurposing Diffusion Priors for Joint Glass Segmentation and Depth Estimation

**Authors:** Tarun R, Anuj Verma, Laksh Nanwani, Sourav Garg, K. Madhava Krishna
**Links:** [abs](https://arxiv.org/abs/2607.24249) - [pdf](https://arxiv.org/pdf/2607.24249)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, 3D mapping, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SILICA: Repurposing Diffusion Priors for Joint Glass Segmentation and Depth Estimation
- 作者：Tarun R, Anuj Verma, Laksh Nanwani, Sourav Garg, K. Madhava Krishna
- 出版日期：2026-07-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2607.24249) | [PDF](https://arxiv.org/pdf/2607.24249)

### 一句话总结
提出统一框架SILICA，利用文本到图像扩散模型先验，联合完成玻璃分割与深度估计，无需真实玻璃深度标注，并实现零样本迁移。

### 研究问题
标准深度传感器在透明玻璃表面系统性地失效，导致3D地图错误和导航风险；现有的玻璃感知单目深度估计方法因真实世界玻璃深度标注极度稀缺，难以零样本泛化到新场景。

### 核心思路/方法
- 重新利用文本到图像扩散模型中蕴含的丰富先验知识，构建统一管道SILICA。
- 同时预测玻璃分割掩码和玻璃感知深度，通过两种任务间的互信息交换建立鲁棒的视觉空间层次。
- 完全摆脱对配对真实玻璃深度标注的依赖。
- 利用预测的分割掩码从标准深度传感器中显式过滤错误的玻璃深度点，恢复精确的度量玻璃深度。

### 主要贡献
1. 提出SILICA框架，首次将扩散模型先验用于联合玻璃分割与深度估计。
2. 无需真实配对玻璃深度标注，实现零样本迁移至各类未见环境。
3. 在多种新场景中，性能超越现有最好方法近20%，为透明表面感知设立新基准。
4. 引入辅助数据集Mirage 18k。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法直接针对现有深度感知系统的关键短板（透明表面失败），利用扩散模型先验绕开了数据标注瓶颈，并在零样本迁移上取得显著提升（20%以上），理论创新和应用价值均较强，对3D重建、机器人导航等领域研究者有重要参考意义。

</details>

<details>
<summary>Abstract</summary>

Standard depth sensors systematically fail on transparent surfaces, creating corrupted 3D maps and severe navigation hazards. While specialized hardware sensors can detect glass, they lack modularity and have extensive hardware dependencies. Consequently, learning-based monocular depth estimation has emerged as a compelling alternative. However, domain-specific glass-aware monocular depth estimators struggle with unfamiliar indoor layouts; restricted by the severe scarcity of real-world glass depth annotations, they fail to generalize zero-shot to new settings. This motivates us to explore whether the extensive priors of text-to-image diffusion models can enable generalizable perception of transparent surfaces. We introduce SILICA, a unified pipeline leveraging these priors to jointly predict glass segmentation and glass-aware depth. This mutual information exchange establishes a robust spatial hierarchy, entirely eliminating the need for paired real-world glass depth annotations. Subsequently, we use the predicted segmentation mask to explicitly filter incorrect glass depth points from standard sensors, recovering accurate metric glass depth for downstream 3D mapping and autonomous collision avoidance. Supported by our novel Mirage 18k dataset, extensive experiments demonstrate that SILICA achieves remarkable zero-shot transfer across diverse, unseen environments, outperforming state-of-the-art models by almost 20% and setting a new benchmark for transparent surface perception.

</details>

#### 2026-07-27 - Quality-Adaptive Multi-UAV 3D Reconstruction with Sparse Workload Redistribution

**Authors:** Benjamin Sportich, Kenza Boubakri, Olivier Simonin, Alessandro Renzaglia
**Links:** [abs](https://arxiv.org/abs/2607.24233) - [pdf](https://arxiv.org/pdf/2607.24233)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, robotics, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Quality-Adaptive Multi-UAV 3D Reconstruction with Sparse Workload Redistribution
- 作者：Benjamin Sportich, Kenza Boubakri, Olivier Simonin, Alessandro Renzaglia
- 出版日期：2026-07-27T10:10:31Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.24233

### 一句话总结
本文提出一种质量自适应的多无人机协同3D重建策略，通过结合TSDF置信度准则和两级协调机制（局部分散与全局负载重平衡），在用户定义保真度目标下提升路径效率与重建精度。

### 研究问题
多无人机在未知环境进行3D重建时，如何通过在线协调实现高效路径规划，同时满足用户定义的3D地图保真度要求，并克服计算和能量限制带来的挑战。

### 核心思路/方法
1. **质量导向的视点生成与信息增益估计**：将基于TSDF置信度的质量准则集成到视点评估中，使生成视点与用户指定的保真度目标一致。
2. **两级协调机制**：
   - 局部层面：在视点评价中引入惩罚因子，鼓励无人机之间分散探索。
   - 全局层面：基于正则化聚类和最优任务分配的全局不平衡校正机制，仅当检测到无人机配置相对于高信息区域失衡时触发。
3. **整体流程**：采用去中心化的决策策略，在重建过程中动态调整无人机行为，依靠协调机制优化整体探索与重建质量。

### 主要贡献
1. 提出质量自适应的去中心化决策策略，支持用户自定义3D重建保真度。
2. 设计两级协调机制（局部分散+全局负载重平衡），在不平衡时通过正则化聚类与最优任务分配进行纠正。
3. 仿真实验表明，该方法在路径效率、重建覆盖率和精度上均优于现有最先进的多无人机探索方法，并公开代码。

### 局限性
摘要未提供足够信息。根据摘要，未明确说明方法的局限性，如对动态环境适应性、计算开销或真实无人机平台的验证情况等。

### 阅读优先级
**高**  
理由：该研究针对多无人机3D重建中核心的在线协调和质量控制问题，提出了可量化的解决方案（TSDF置信度与两级协调），并且综合性能（路径效率+重建精度）在仿真中优于现有方法。若用户关注无人机集群3D重建或自适应探索策略，此文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D reconstruction of unknown environments is a key application in robotics but is severely limited by the computational and energy capabilities of current aerial platforms. Deploying multiple UAVs and providing efficient and scalable path planning strategies are common approaches, but effective online coordination among UAVs remains a significant challenge. To address this problem, we propose a quality-adaptive decentralized decision-making strategy to build a 3D map with user-defined degrees of fidelity. The approach integrates a quality-oriented criterion based on TSDF confidence into view generation and information gain estimation to produce viewpoints consistent with the desired fidelity target. Additionally, we employ two levels of coordination: a penalty factor in the viewpoint evaluation to encourage local dispersion among the UAVs and a global imbalance correction mechanism. The latter, based on regularized clustering and optimal task assignment, is only triggered when an unbalanced configuration relative to high-information regions is detected. Simulation results demonstrate that the proposed method improves path efficiency compared to state-of-the-art multi-UAV exploration approaches, while also achieving higher-fidelity reconstructions in terms of coverage and accuracy. We make our code publicly available to the community.

</details>

#### 2026-07-27 - SHARE: Towards Head-Mounted AR with User-Centric SLAM in Shared Human-Robot Workspaces

**Authors:** Tianyuan Du, Tianyi Hu, Hanting Ye, Maria Gorlatova
**Links:** [abs](https://arxiv.org/abs/2607.23901) - [pdf](https://arxiv.org/pdf/2607.23901)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, manipulation, mapping, localization, AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SHARE: Towards Head-Mounted AR with User-Centric SLAM in Shared Human-Robot Workspaces
- 作者：Tianyuan Du, Tianyi Hu, Hanting Ye, Maria Gorlatova
- 出版日期：2026-07-27T00:21:39Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Embodied / Robotics / AR Applications（副分类）
- 链接：摘要页 https://arxiv.org/abs/2607.23901，PDF https://arxiv.org/pdf/2607.23901

### 一句话总结
本文提出一种以用户为中心的SLAM系统SHARE，通过优先保障AR用户低延迟需求并利用特征冗余减少边缘计算开销，在共享人机协作空间中实现了AR用户平均13.22 ms延迟和亚厘米级跟踪精度。

### 研究问题
现有边缘驱动的多智能体SLAM系统对所有智能体（如机器人和头戴AR用户）采取统一资源分配，忽略了AR用户对低延迟的严格要求，导致用户操作高延迟。

### 核心思路/方法
1. 构建首个面向人机协作智能体的体验模型（experience model）。  
2. 根据体验模型自适应调整传输优先级，优先响应用户端的AR延迟需求。  
3. 利用共享工作空间中各智能体获取视觉特征的重叠性，减少边缘处理的计算时间，降低端到端延迟。

### 主要贡献
1. 设计并实现了SHARE，一个用户中心的SLAM系统，在维护机器人跟踪精度的同时优先保障AR用户体验。  
2. 提出首个针对人机协作智能体的体验模型，用于自适应优先级调度。  
3. 利用特征冗余减少边缘计算，使AR用户平均延迟降低43.3%（至13.22 ms），机器人跟踪精度保持在2厘米以内。  
4. 用户研究显示用户感知有统计学显著改善。

### 局限性
摘要未提供足够信息：未提及系统在极端场景（如高动态环境、大量智能体并发）下的表现、对计算资源的具体要求，以及长时运行稳定性。

### 阅读优先级
**高**  
理由：该工作关注共享人机协作空间中AR用户面临的实际延迟瓶颈，提出了具体且经过物理部署验证的优化方案（平均延迟降低43.3%），属于3D重建、机器人学与AR跨领域应用，对有此方向需求的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Human-Robot Collaboration (HRC) in shared physical spaces using Augmented Reality (AR) interfaces is powered by Simultaneous Localization and Mapping (SLAM). Existing multi-agent SLAM systems rely on an edge server to combine visual findings of multiple resource-constrained agents, perform computation, and schedule updates to their local maps. However, the edge treats all agents uniformly and ignores the fundamentally different latency requirements of heterogeneous HRC agents: robots and head-mounted AR users. This uniform resource allocation often results in high lag for user manipulation, as it does not meet the stringent latency requirements of AR. In this work, we design, implement, and evaluate SHARE, a user-centric SLAM system that strategically prioritizes AR user experience while maintaining accurate tracking performance for robots. SHARE builds a first-of-its-kind experience model for HRC agents and adaptively adjusts transmission priorities to match it. To reduce end-to-end latency, SHARE leverages the redundancy of visual features acquired by agents in shared human-robot workspaces to reduce computation time induced by edge-based processing. Real-world deployment with commercial AR headsets and a ground robot achieves 13.22 ms average latency for AR users (43.3% reduction from baseline) while maintaining sub-2-centimeter tracking accuracy. User studies further reveal statistically significant improvements in user perception.

</details>

#### 2026-07-26 - RoadVGGT: Road-Structure-Aware Feed-Forward Road Surface Reconstruction

**Authors:** Han Jiao, Chen Liu, Jiakai Sun, Zhanjie Zhang, Mengyuan Yang, Yimeng Li, Mofan Zhou, Kun Zhan, Lei Zhao
**Links:** [abs](https://arxiv.org/abs/2607.23758) - [pdf](https://arxiv.org/pdf/2607.23758)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** geometric foundation model, surface reconstruction, novel view synthesis, view synthesis, autonomous driving, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoadVGGT: Road-Structure-Aware Feed-Forward Road Surface Reconstruction
- 作者：Han Jiao, Chen Liu, Jiakai Sun, Zhanjie Zhang, Mengyuan Yang, Yimeng Li, Mofan Zhou, Kun Zhan, Lei Zhao
- 出版日期：2026-07-26
- 分类：3D Reconstruction & Multi-view Geometry（主要），Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次要）
- 链接：摘要: https://arxiv.org/abs/2607.23758，PDF: https://arxiv.org/pdf/2607.23758

### 一句话总结
RoadVGGT 提出了一种无需逐场景优化的前馈式道路表面重建框架，利用几何基础模型从多视图图像中预测高斯属性，并通过类别感知融合生成紧凑的道路高斯表示。

### 研究问题
现有道路专用优化方法虽能生成高质量道路表示，但通常需要对每个场景进行单独训练并围绕行驶轨迹设计场景依赖的覆盖方案，限制了在新采集道路上的可扩展重建。研究旨在解决这一局限性，实现可扩展的前馈式道路表面重建。

### 核心思路/方法
1. **几何基础模型**：利用多视图图像、提供的位姿和深度观测，通过学习的 Gaussian 头预测密集的像素对齐 Gaussian 属性。
2. **坐标系对齐与融合**：将密集预测转换到一致的度量世界坐标系，并在道路对齐的 XY 平面上通过置信度加权网格融合冗余 Gaussian。
3. **类别感知分组与保护**：通过类别感知分组和道路-人行道交界处保护，在脆弱道路结构周围控制融合。
4. **输出表示**：生成紧凑的 Gaussian 道路表面，支持 RGB 和语义鸟瞰图、高程估计和新视角合成。

### 主要贡献
- 消除了 prior 方法中所需的逐场景优化，实现测试时无需训练的前馈重建。
- 以紧凑 Gaussian 表示重建完整道路表面，改善了图像质量、语义映射和高程精度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法针对自动驾驶和高精地图中的实际难题（可扩展道路重建），提供了无需逐场景优化的前馈式解决方案，且实验表明质量提升。对从事 3D 重建、自动驾驶感知和神经渲染的研究人员具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Large-scale road surface reconstruction supports high-definition mapping, autonomous-driving perception, annotation, and simulation. Existing road-specialized optimization methods can produce high-quality road representations, but they typically require per-scene training and scene-dependent coverage design around the driving trajectory, limiting scalable reconstruction over newly collected roads. To address these limitations, we introduce RoadVGGT, a road-structure-aware feed-forward framework that reconstructs compact Gaussian road surfaces without test-time per-scene optimization. RoadVGGT uses a geometric foundation model to exploit multi-view images together with provided pose and depth observations, and predicts dense pixel-aligned Gaussian attributes through a learned Gaussian head. To make these dense predictions usable for large road surfaces, we align them into a consistent metric world coordinate system and fuse redundant Gaussians on the road-aligned XY plane through confidence-weighted grid fusion. Category-aware grouping and road--sidewalk junction protection further control fusion around vulnerable road structures. The resulting representation supports RGB and semantic bird's-eye-view maps, elevation estimation, and novel view synthesis. RoadVGGT eliminates the need for per-scene optimization in prior methods, reconstructs complete road surfaces with a compact Gaussian representation, and improves image quality, semantic mapping, and elevation accuracy. Extensive experiments demonstrate the potential of geometric foundation models for scalable feed-forward road surface reconstruction.

</details>

#### 2026-07-26 - DAP-Pose: Deep Temporal Alignment and Physics-aware Cross-modal Sensor Fusion for Robust Pose Estimation

**Authors:** Jianhan Lin, Yuchu Qin, Jiateng Yuan, Wenbo Zhang, Shuai Gao
**Links:** [abs](https://arxiv.org/abs/2607.23755) - [pdf](https://arxiv.org/pdf/2607.23755)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DAP-Pose: Deep Temporal Alignment and Physics-aware Cross-modal Sensor Fusion for Robust Pose Estimation
- 作者：Jianhan Lin, Yuchu Qin, Jiateng Yuan, Wenbo Zhang, Shuai Gao
- 出版日期：2026-07-26
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.23755 ; PDF: https://arxiv.org/pdf/2607.23755

### 一句话总结
DAP-Pose是一个端到端的多模态位姿估计模型，通过深度时序对齐和物理感知跨模态融合，在KITTI基准上取得了最先进的性能（平移误差1.31%，旋转误差0.46°）。

### 研究问题
如何在多模态传感器（视觉、惯性、GNSS）存在异步时间偏移的情况下，实现鲁棒且准确的位姿估计？

### 核心思路/方法
1. **Bi-level Cross-modal Fusion (BCF)**：从视觉、惯性和GNSS测量中捕获互补的语义和几何运动线索。
2. **Deep Temporal Alignment (DTA)**：在隐空间中对齐异步流，实现无需严格硬件同步的连贯运动建模。
3. **物理感知约束**：利用流形几何和GNSS引导的绝对度量尺度，强制执行运动一致性并抑制漂移。

### 主要贡献
1. 提出了一个统一端到端模型DAP-Pose，用于鲁棒多模态位姿估计。
2. 设计了BCF模块和DTA模块，分别解决模态融合和时序异步问题。
3. 引入物理感知约束（流形几何、GNSS度量尺度）增强运动一致性。
4. 在KITTI数据集上，DAP-Pose实现了最低的平移误差（1.31%）和旋转误差（0.46°），并在严重人工注入时间错位下仍保持鲁棒性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作发表于权威应用场景（自动驾驶/机器人），在多模态融合和时序对齐方面提出了新颖模块，并在公开基准KITTI上取得了当时最佳结果，对位姿估计、传感融合领域的研究者有直接参考价值。摘要中实验设置清晰，性能指标明确，但未说明消融实验或局限性，建议结合全文评估实际适用场景。

</details>

<details>
<summary>Abstract</summary>

Robust and accurate pose estimation with multi-modal sensors is fundamental for autonomous vehicles and mobile robotic systems in complex environments. In this paper, we propose DAP-Pose, a unified end-to-end model for robust multi-modal pose estimation. DAP-Pose introduces a Bi-level Cross-modal Fusion (BCF) module that captures complementary semantic and geometric motion cues from visual, inertial, and GNSS measurements. To handle temporal offsets, we designed a Deep Temporal Alignment (DTA) module that explicitly aligns asynchronous streams in latent space, enabling coherent motion modeling without strict hardware synchronization. Furthermore, we incorporate physics-aware constraints via manifold geometry and GNSS-guided absolute metric scale, enforcing motion consistency and mitigating drift. Experiments upon the public KITTI benchmark dataset were conducted to evaluate the performance of DAP-Pose against existing methods. DAP-Pose achieved the state-of-the-art performance, with the lowest average translation error ($t_{rel}$) of 1.31% and rotation error ($r_{rel}$) of 0.46$^{\circ}$. Furthermore, it accurately estimates poses and maintains robust performance under severe artificially injected temporal misalignment.

</details>

#### 2026-07-23 - Boosting Robustness for All-Weather Self-Supervised Depth Estimation in Autonomous Driving

**Authors:** Mengshi Qi, Xiaoyang Bi, Xianlin Zhang, Huadong Ma
**Links:** [abs](https://arxiv.org/abs/2607.21526) - [pdf](https://arxiv.org/pdf/2607.21526)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Boosting Robustness for All-Weather Self-Supervised Depth Estimation in Autonomous Driving
- 作者：Mengshi Qi, Xiaoyang Bi, Xianlin Zhang, Huadong Ma
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2607.21526 | PDF https://arxiv.org/pdf/2607.21526

### 一句话总结
本文提出一种自训练框架，通过多教师蒸馏和鲁棒的雷达融合方法，提升自动驾驶在恶劣天气下自监督深度估计的鲁棒性，并在全天候数据集上达到最优性能。

### 研究问题
恶劣天气条件下（如雨、雾等）自监督深度估计的鲁棒性问题。具体包括两个子问题：
1. 恶劣天气会扭曲像素对应关系，违反自监督损失函数假设，导致深度预测错误；
2. 雷达传感器虽常见于恶劣天气，但其点云在相机视角（POV）中分布稀疏，使得自监督融合困难。

### 核心思路/方法
1. **不确定性感知的多教师蒸馏（Uncertainty-Aware Multi-Teacher Distillation）**：使用不同恶劣天气条件输入生成多个教师模型，再通过不确定性建模对知识蒸馏损失进行加权。
2. **POV-BEV雷达融合（POV-BEV Radar Fusion）**：利用相机像素射线约束，建立POV（相机视角）与雷达BEV（鸟瞰视角）之间的联系，从而利用更稠密的雷达点，同时捕捉两种视角的互补信息。

### 主要贡献
- 提出了针对全天候自监督深度估计的鲁棒自训练框架，结合多教师蒸馏与雷达融合。
- 设计了POV-BEV雷达融合方法，有效利用稠密雷达点以增强恶劣天气下的深度预测。
- 在全天候数据集上的定性和定量实验均展示了鲁棒性，实现了当时最优性能。

### 局限性
摘要未提供足够信息。未提及方法在特定天气条件下的失败案例、计算开销或对传感器硬件的要求。

### 阅读优先级
**高**
理由：该工作直接针对自动驾驶在恶劣天气下的关键安全挑战，提出了融合多教师蒸馏与雷达的创新方案，并达到SOTA性能，对相关领域研究者和工程师具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Self-supervised depth estimation is challenging for safe autonomous driving under various adverse weather conditions due to sensor perception degradation. These challenges arise from two main aspects. Firstly, adverse conditions can distort pixel correspondences and violate the assumptions embedded in the self-supervised loss function, leading to erroneous depth predictions. Secondly, while radar is a widely adopted sensor in adverse weather conditions, the sparse distribution of radar points in the Point of View (POV) poses challenges for self-supervised fusion. To address these issues, we introduce a novel self-training pipeline using unpaired real all-weather data through multi-teacher distillation and robust radar fusion. We propose the Uncertainty-Aware Multi-Teacher Distillation method to generate diverse teacher models with different adverse condition inputs, and then employ uncertainty modeling to weigh the knowledge distillation loss. Additionally, we design the POV-BEV Radar Fusion approach, which leverages camera-pixel ray constraints to establish connections between the camera's Point of View (POV) and the radar's Bird's-Eye View (BEV). This approach enables the utilization of denser radar points, effectively capturing the complementary perspectives of both POV and BEV. Extensive quantitative and qualitative experiments demonstrate the robustness of our proposed method on all-weather datasets, achieving state-of-the-art performance. Our code and models are available at https://github.com/MICLAB-BUPT/RobustDepth.

</details>

#### 2026-07-23 - Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window

**Authors:** Yukun Shi, Minglun Gong
**Links:** [abs](https://arxiv.org/abs/2607.21471) - [pdf](https://arxiv.org/pdf/2607.21471)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, scene reconstruction, surface reconstruction, 3DGS, novel view synthesis, view synthesis, rendering, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Future Rendering ≠ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window
- 作者：Yukun Shi, Minglun Gong
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.21471

### 一句话总结
本文提出了一个名为FutureSurf的基准测试和数据集，用于评估动态场景中超出观测时间窗口的几何表面重建（未来表面）的准确性。

### 研究问题
当前动态场景重建方法几乎只在观测时间窗口内评估，但实际应用（如AR覆盖、机器人交互）需要预测未来时刻的表面几何形状。问题在于：**没有标准基准来衡量未来表面重建的准确性**。

### 核心思路/方法
1.  **基准定义**：要求方法训练于序列的前75%观测数据，然后在保留的未来数据上评估每帧的表面几何（使用Chamfer距离）。主要分数为绝对未来CD，诊断指标为未来/观测误差差距。
2.  **数据集**：包含8个解析定义的受控运动，其中3个为证伪控制（用于检验方法是否正确忽略不影响表面的变化）。提供每帧精确的ground truth网格。
3.  **基线实验**：在受控运动上测试了DG-Mesh和Deformable-3DGS两个骨干方法，发现未来表面误差显著（2.0-6.6×差距），且未来渲染质量与未来表面准确性统计上解耦。

### 主要贡献
1.  **提出FutureSurf基准与数据集**：首个专门用于评估动态场景未来时间点表面重建的受控诊断基准，包含精确地面真值和证伪控制。
2.  **揭示现有方法局限**：即使对于原则可预测的未来运动，现有方法（DG-Mesh, Deformable-3DGS）仍存在显著未来表面误差（2.0-6.6×），且渲染质量指标无法反映几何误差。
3.  **提供工具与资源**：公开了分割文件、评分代码、基准卡片、Croissant元数据及数据集，便于社区复现和比较。
4.  **建立未来表面与渲染的差异**：通过统计证明新视角合成指标与未来几何准确性无关，未来误差主要集中于表面移动区域。

### 局限性
摘要未提供关于局限性的信息，例如数据集只有8个受控运动（场景多样性有限）以及基线方法类型有限（仅使用DG-Mesh和Deformable-3DGS）等限制。

### 阅读优先级
**高**
- **理由**：该工作填补了动态重建领域的一个明确空白——缺乏未来表面预测的标准评估，提出的基准和数据集具有开创性。实验揭示了现有方法（包括流行的DG-Mesh和Deformable-3DGS）在预测未来几何时的系统性不足，并指出渲染质量无法替代几何准确性，这对从事动态场景重建、AR/VR和机器人交互的研究者具有重要警示和参考价值。资源已公开，便于直接复现和使用。

</details>

<details>
<summary>Abstract</summary>

Dynamic-scene reconstruction is almost always evaluated inside the observed time window, yet deployment settings such as AR overlays, robot interaction, and anticipatory planning need the future surface: the geometry at times beyond those captured. No standard benchmark measures this. We introduce FutureSurf, a controlled diagnostic benchmark and dataset for future-time surface reconstruction that trades scene diversity for exact future ground truth and falsification controls. A method trains on the observed first 75% of a sequence; we score its extracted per-frame surface on the held-out future by Chamfer distance, reporting absolute future CD as the primary score and the future/observed gap as a diagnostic. The dataset contains eight analytically defined controlled motions, including three falsification controls, with exact per-frame ground-truth meshes. We also provide a ground-truth-side recoverability oracle. The release includes split files, scoring code, a benchmark card, and Croissant metadata. On the controlled motions, the DG-Mesh backbone leaves a 2.7-4.1$\times$ gap even for futures predictable in principle (four of five recoverable from observed motion by a fixed rule), while the falsification controls behave as designed (the surface-invariant motion shows no gap). Beyond the contributed dataset, the gap persists across six animated DG-Mesh asset scenes and a second backbone, Deformable-3DGS (2.0-6.6$\times$; both share a deformation-MLP temporal model). The benchmark also shows that future rendering quality and future-surface accuracy are statistically decoupled, so the novel-view-synthesis metrics the field reports do not track future geometry. The future error is structured, concentrating where the surface moves. The dataset, evaluation toolkit, and scoring code are available on Hugging Face and GitHub (https://github.com/Ricky-S/futuresurf).

</details>

#### 2026-07-23 - DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV

**Authors:** Tong Ling, Wenhui Diao, Yingchao Feng, Hanbo Bi, Zhongyan Hou, Xian Sun
**Links:** [abs](https://arxiv.org/abs/2607.21438) - [pdf](https://arxiv.org/pdf/2607.21438)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, camera pose estimation, pose estimation, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV
- 作者：Tong Ling, Wenhui Diao, Yingchao Feng, Hanbo Bi, Zhongyan Hou, Xian Sun
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：arXiv:2607.21438

### 一句话总结
该论文提出了DAPM，一种针对无人机航拍图像的单目深度估计框架，能够在高度、俯仰角、翻滚角与视场角持续变化下联合估计相机姿态与深度，并达到最优性能。

### 研究问题
无人机在动态变化的高度、俯仰角、翻滚角和视场角下进行单目深度估计时，现有方法难以泛化到这些多样视角以及航拍场景中深度分布的大尺度范围。

### 核心思路/方法
1. 通过理论分析建立无人机视角与视距的几何对应关系，并以此为观测基准。
2. 提出理想地面深度（IGD）模块，利用推导出的几何关系实现密集相机姿态监督并增强深度特征。
3. 设计粗到细的渐进量化箱（PQB）模块，通过渐进监督与层次量化箱实现复杂航拍图像中的鲁棒估计。
4. 构建UAPD数据集，涵盖全面且连续的姿态参数分布，用于评估框架。

### 主要贡献
- 第一个针对无人机航拍图像、在连续变化视角下联合估计相机姿态与深度的单目框架（DAPM）。
- 提出IGD模块，利用几何关系实现密集相机姿态监督与深度特征增强。
- 提出PQB模块，通过渐进式监督与层次量化箱提升复杂航拍场景的估计鲁棒性。
- 创建UAPD数据集，包含连续分布的姿态参数，并在该数据集上达到深度与相机姿态估计指标的最优性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：本文针对无人机实际部署中高度动态视角下的核心难题提出了首个专用框架，理论分析严谨，方法设计（IGD与PQB）具有明确创新性，并开源代码与数据集，对3D重建、自主导航等领域有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation is a fundamental prerequisite for 3D reconstruction and autonomous navigation in Unmanned Aerial Vehicles (UAVs). In practical deployments, UAVs operate under highly dynamic camera poses characterized by continuous variations in height, pitch, roll, and field of view (FOV). Existing monocular depth estimation methods frequently fail to generalize across such diverse perspectives and the expansive scale of depth distributions inherent in aerial scenes. To address these challenges, we establish a quantitative representation of UAV viewing angles through rigorous theoretical analysis, deriving the geometric correspondence between viewing angles and view distances using the ground plane as a reference for observation. Building upon this, we propose Depth Estimation for Any Perspectives Model (DAPM), representing the first monocular framework specifically designed for UAV aerial imagery to jointly estimate camera pose and depth under continuously varying viewpoints. Specifically, we introduce an Ideal Ground Depth (IGD) module that leverages the derived geometric relationships between UAV perspectives and view distances to implement dense camera-pose supervision and enhance depth features. And we further develop a coarse-to-fine Progressive Quantization Bins (PQB) module. By incorporating progressive supervision and hierarchical quantization bins, the PQB module enables robust estimation in complex UAV aerial imagery. To evaluate the proposed framework, we present the UAV Any Perspectives Depth (UAPD) dataset, featuring comprehensive and continuous distributions of pose parameters. Experimental results on UAPD demonstrate that DAPM achieves state-of-the-art performance across both depth and camera-pose estimation metrics. The source code and datasets are available at: https://github.com/ThisIsLT/DAPM.

</details>

#### 2026-07-23 - GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition

**Authors:** Panagiotis Mermigkas, Argyris Manetas, Petros Maragos
**Links:** [abs](https://arxiv.org/abs/2607.21416) - [pdf](https://arxiv.org/pdf/2607.21416)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition
- 作者：Panagiotis Mermigkas, Argyris Manetas, Petros Maragos
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要 https://arxiv.org/abs/2607.21416；PDF https://arxiv.org/pdf/2607.21416

### 一句话总结
GLAM-SLAM 提出一种实时、解耦的高斯泼溅SLAM系统，通过流致密化锚定策略和场景空间分解，实现大规模室外场景的长序列建图与定位。

### 研究问题
现有基于高斯泼溅的单目SLAM系统在处理长序列、大规模室外场景时，存在实时性差、GPU内存需求过高的问题，限制了其在真实长时任务中的应用。

### 核心思路/方法
1. **轻量追踪**：采用基于特征鲁棒的SLAM前端进行轻量化位姿估计。
2. **稀疏锚点网格表示**：采用结构化的稀疏锚点网格进行建图，保证大规模操作的可扩展性和场景一致性。
3. **几何流致密化锚定策略**：基于对极几何约束，通过流致密化满足3D高斯泼溅（3DGS）的密集初始化需求。
4. **场景分割策略**：将建图视为多场景问题，通过MLP初始化引入强空间归纳偏置，生成局部化高斯体。

### 主要贡献
- 提出首个实时、解耦的高斯泼溅SLAM系统，专为大规模室外长序列场景设计。
- 引入几何流致密化锚定策略，解决3DGS密集初始化的需求。
- 提出基于场景分割的空间分解方法，借助MLP初始化实现局部高斯化。
- 在KITTI Odometry、Oxford RobotCar和Málaga数据集上，重建质量相比次优方法提升15%，同时保持实时性和长序列扩展能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：论文针对高斯泼溅SLAM在真实长序列大规模场景中的实际瓶颈（实时性、内存、扩展性）提出系统级解决方案，方法新颖（流致密化、场景分解），并在多个挑战性基准上取得显著提升。对该领域（3D重建、SLAM、机器人、AR）的研究者和工程师具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing Gaussian-splatting-based monocular Simultaneous Localization and Mapping (SLAM) systems are either tailored to short sequences, are not real-time, or suffer from prohibitive GPU memory requirements, limiting their applicability in realistic, long-horizon scenarios. To address this, we present GLAM-SLAM, a real-time, decoupled Gaussian-splatting SLAM system designed for large-scale outdoor scenes. We ensure lightweight tracking using a robust, feature-based SLAM frontend, while for mapping, we adopt a structured, sparse anchor grid representation that ensures scalable operation and maintains scene coherence across long-term sequences. To satisfy the dense initialization requirements of 3D Gaussian Splatting (3DGS), we introduce a geometry-based flow-densification anchoring strategy using epipolar constraints. Furthermore, by treating mapping as a multi-scene problem, we propose a scene-partitioning strategy that introduces a strong spatial inductive bias via MLP initializations to generate localized Gaussians. We evaluate our system on the challenging, long-sequence KITTI Odometry, Oxford RobotCar, and M'alaga datasets. Extensive ablations and comparisons demonstrate a 15% improvement in reconstruction quality over the second-best performer, while maintaining real-time performance and the ability to scale to longer sequences. Code is publicly available for the benefit of the community.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-29 - StructureGS: Structure-aware Gaussian Splatting for Articulated Object Reconstruction

**Authors:** Gahye Lee, Gyoonseo Kim, Wonjong Jang, Jooeun Son, Seungyong Lee
**Links:** [abs](https://arxiv.org/abs/2607.26889) - [pdf](https://arxiv.org/pdf/2607.26889)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StructureGS: Structure-aware Gaussian Splatting for Articulated Object Reconstruction
- 作者：Gahye Lee, Gyoonseo Kim, Wonjong Jang, Jooeun Son, Seungyong Lee
- 出版日期：2026-07-29
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：摘要页: https://arxiv.org/abs/2607.26889 ; PDF: https://arxiv.org/pdf/2607.26889

### 一句话总结
本文提出StructureGS，一种将结构感知约束（如空间一致性和结构连通性）集成到3D高斯溅射框架中的方法，用于重建具有清晰部件几何与边界的铰接物体。

### 研究问题
如何解决铰接物体（含多个可动部件）重建中由于几何、外观和运动参数相互纠缠，导致部件分解模糊、边界不清和几何伪影的问题。

### 核心思路/方法
- 基础框架：基于3D Gaussian Splatting进行铰接物体重建。
- 关键创新：引入结构化导向信息，具体利用物体部件的有向包围盒来施加两类结构约束：
  - 空间一致性：约束每个部件的几何在其指定区域内保持紧凑且空间连贯。
  - 结构连通性：强制相邻部件之间保持物理上合理的接触关系。
- 实现手段：通过结构感知损失函数，将显式结构约束注入优化过程。

### 主要贡献
1. 提出了StructureGS，一个集成了结构感知导向的铰接物体重建框架，有效改善了部件分解质量。
2. 设计了基于有向包围盒的空间一致性和结构连通性约束，为优化提供显式结构先验。
3. 实验表明，该方法在铰接物体重建任务上达到了最先进性能，生成了部件几何清晰的高质量结果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**

理由：本文方法专注于铰接物体的3D重建这一具体问题，利用结构先验改进部件分解。对于从事神经渲染、物体重建或机器人操作等领域的读者，该方法结合了经典几何约束与现代场景表示，具有参考价值。但如果读者主要关注通用场景渲染或无铰接结构的静态重建，则相关性较低。摘要未提供消融实验或失败案例等细节，因此初步判断为中等优先级。

</details>

<details>
<summary>Abstract</summary>

Reconstructing articulated objects with multiple movable parts is essential for understanding object structure and enabling physical interaction. However, this reconstruction task poses significant challenges due to the entanglement of geometry, appearance, and motion parameters during optimization. Existing methods rely primarily on photometric supervision, which commonly fails to disentangle these interdependent components, resulting in poor part decomposition with blurred boundaries and geometric artifacts. To address this limitation, we introduce StructureGS, a reconstruction framework for articulated objects that integrates structure-aware guidance into 3D Gaussian Splatting. Our approach leverages oriented bounding boxes of object parts to enforce two key structural properties: spatial coherence, which constrains each part's geometry to remain compact and spatially coherent within its designated region, and structural connectivity, which enforces physically plausible contact relationships between adjacent parts. These properties are realized through structure-aware losses that inject explicit structural constraints into the optimization process. Extensive experiments demonstrate that our method achieves state-of-the-art performance in articulated object reconstruction, producing high-quality results with well-defined part geometries.

</details>

#### 2026-07-29 - 3DGBGS: 3D Granular Ball Gaussian Splatting for Compact Novel View Synthesis

**Authors:** Meng Yang, Shuyin Xia, Dawei Dai, YiWang
**Links:** [abs](https://arxiv.org/abs/2607.26578) - [pdf](https://arxiv.org/pdf/2607.26578)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** SfM, Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3DGBGS: 3D Granular Ball Gaussian Splatting for Compact Novel View Synthesis
- 作者：Meng Yang, Shuyin Xia, Dawei Dai, YiWang
- 出版日期：2026-07-29
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2607.26578，PDF: https://arxiv.org/pdf/2607.26578

### 一句话总结
3DGBGS 是一种基于颗粒球（Granular Ball）思想的紧凑型3D高斯溅射框架，通过自适应划分点云并初始化锚点，在减少模型存储的同时保持新视角合成质量。

### 研究问题
现有基于锚点的3D高斯溅射方法通常使用固定体素化从稀疏SfM点云构建锚点，无法充分适应空间非均匀点分布，导致锚点数量、模型紧凑性和渲染质量之间存在权衡。该研究旨在解决这一问题。

### 核心思路/方法
提出3DGBGS框架，核心步骤包括：
- **自适应颗粒球划分**：将SfM点云自适应划分为3D颗粒球，大球紧凑表示平滑冗余区域，小球保留复杂几何和局部细节。
- **颗粒球锚点初始化（GBAI）**：利用颗粒球中心初始化紧凑锚点位置。
- **颗粒球尺度先验（GBSP）**：利用颗粒球半径提供局部尺度先验，用于高斯生成。

### 主要贡献
基于摘要，主要贡献包括：
- 提出了结合颗粒球计算（GBC）与锚点型3DGS的紧凑框架。
- 通过GBAI和GBSP模块，实现自适应、紧凑的锚点初始化与尺度指导。
- 在四个基准数据集上，平均减少初始锚点37.1%、最终锚点10.0%，模型存储降低9.8%，同时保持可比的渲染质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。
理由：该方法针对3DGS模型紧凑性提出了新颖的颗粒球自适应策略，实验改进了锚点数量与存储效率，适合对3D场景渲染紧凑性有兴趣的读者。但未与更多最新方法对比或讨论实时性等关键细节，优先级中等。

</details>

<details>
<summary>Abstract</summary>

Three-dimensional Gaussian Splatting (3DGS) enables high-quality real-time novel-view synthesis through explicit Gaussian primitives and differentiable rasterization. 3DGS and Granular Ball Computing (GBC), proposed in 2019, share a natural compatibility in adaptive representation. The efficiency of 3DGS partly stems from a coarse-to-fine and on-demand refinement process that draws on the generation principle of GBC. This connection motivates us to further introduce adaptive granular ball organization into anchor-based 3DGS. Existing anchor-based methods typically construct anchors from sparse SfM point clouds through fixed voxelization, which cannot adequately adapt to spatially non-uniform point distributions and leads to a trade-off among anchor count, model compactness, and rendering quality. To address this issue, we propose 3DGBGS (3D Granular Ball Gaussian Splatting), a compact anchor-based framework for novel-view synthesis. 3DGBGS adaptively partitions SfM point clouds into 3D granular balls, using larger balls to compactly represent smooth and redundant regions and smaller balls to preserve complex geometry and local details. Based on this representation, Granular Ball Anchor Initialization (GBAI) uses granular ball centers to initialize compact anchor positions, while the Granular Ball Scale Prior (GBSP) exploits granular ball radii to provide local scale priors for Gaussian generation. Experiments on four benchmarks show that 3DGBGS reduces initial and final anchors by 37.1% and 10.0%, respectively, and model storage by 9.8% on average, while maintaining comparable rendering quality.

</details>

#### 2026-07-29 - AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting

**Authors:** ByungHyun Kim, Jinwoo Jeon, Woontack Woo
**Links:** [abs](https://arxiv.org/abs/2607.26525) - [pdf](https://arxiv.org/pdf/2607.26525)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting
- 作者：ByungHyun Kim, Jinwoo Jeon, Woontack Woo
- 出版日期：2026-07-29T06:43:17Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.26525

### 一句话总结
AtlasLC 是一种无需原始源数据、无需训练、直接对已发布的物体级3D高斯泼溅资产进行快速压缩的管线，通过局部竞争剪枝和确定性地图打包技术，在减少压缩时间的同时维持可比的几何与感知质量。

### 研究问题
现有3DGS压缩方法主要针对场景级捕获设计，依赖繁重的布局生成或激进的全域剪枝，不适用于语义集中的前景物体；在XR实际管线中，物体级资产需要反复打包、传输、解码和实例化，因此现有方法在资产准备成本、编解码兼容性、解码延迟以及深度和轮廓线索保留方面表现不佳。本文旨在解决如何针对物体级3DGS实现快速、编解码器就绪且部署友好的压缩。

### 核心思路/方法
AtlasLC 结合了局部竞争剪枝与确定性地图打包，直接操作已发布的3DGS资产（无需原始图像、相机位姿或逐资产优化）。具体地：
- **局部竞争剪枝**：在保持物体前景整体支撑的前提下，去除冗余高斯点。
- **单次排序条件传输**：作为轻量级、单遍的共享坐标骨干，连接剪枝与打包阶段，避免映射/重映射瓶颈。
- **确定性地图打包**：无需额外布局生成，直接打包高斯点，减少预处理时间。

### 主要贡献
1. 提出一种无需源数据、无需训练的直接压缩管线，适用于已发布的物体级3DGS资产。
2. 将地图准备时间降低最高25倍，端到端压缩时间降低最高5倍。
3. 在相似压缩尺寸下，比特数比紧凑结构化基线减少约6%~8%，同时保持可比的感知和几何质量。
4. 提供更优的部署感知平衡：兼顾有效载荷、解码延迟、运行时FPS和3D几何保真度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接针对XR实际部署中的物体级3DGS资产压缩瓶颈，提出了无需原始数据、无需训练的快速方案，且显著降低压缩时间和比特率。对于关注3DGS在XR/移动设备落地或编解码器优化的研究者与工程师，具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic novel-view synthesis with real-time rendering, but deploying compressed object-centric 3DGS in XR requires more than image-space rate-distortion. In practical XR asset pipelines, reusable objects are repeatedly packaged, transmitted, decoded, and instantiated, making asset-preparation cost, codec compatibility, decoding latency, and preservation of depth and silhouette cues first-class concerns. Existing 3DGS compression methods are largely developed for scene-scale captures and often rely on heavy layout generation or aggressive global pruning, assumptions that transfer poorly to semantically concentrated foreground objects. We present AtlasLC, a source-free, training-free compression pipeline for object-centric 3DGS that operates directly on released Gaussian assets, without original images, camera poses, or per-asset optimization. AtlasLC couples local-competition pruning with deterministic atlas packing to remove the mapping/remapping bottleneck while preserving object-wide foreground support; a lightweight single-pass sort-based conditional transport is used as a shared coordinate backbone for these stages. Across the evaluated assets, AtlasLC reduces atlas-preparation time by up to a factor of 25 and end-to-end compression time by up to a factor of 5, while offering a favorable deployment-aware balance of payload, decode latency, runtime FPS, and 3D geometry relative to the evaluated compressed baselines. Relative to similarly compact structured baselines, it uses about 6 to 8 percent fewer bits while maintaining comparable perceptual and geometric quality. These results show that object-centric 3DGS compression should be optimized for a deployment-aware operating point enabling scalable XR asset libraries.

</details>

#### 2026-07-28 - CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting

**Authors:** Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin
**Links:** [abs](https://arxiv.org/abs/2607.25569) - [pdf](https://arxiv.org/pdf/2607.25569)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting
- 作者：Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin
- 出版日期：2026-07-28
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.25569

### 一句话总结
CORF-GS提出一种基于耦合光学-射频3D高斯泼溅的实时无线辐射场重建框架，通过光学引导和联合优化实现高效在线信道建模。

### 研究问题
现有无线辐射场重建方法依赖预采集观测数据和离线优化，无法提供实时信道知识，如何实现基于序贯输入数据的实时无线信道重建。

### 核心思路/方法
1. 构建光学与射频的统一高斯表征：共享几何结构，分别学习模态特定的外观属性。
2. 光学引导高斯采样：在新关键帧到达时，利用高分辨率光学图像为重建不足区域补充高斯点。
3. 耦合光学-射频联合优化：针对光与无线电波对物体表面响应的波长失配问题，同时优化共享高斯，使其适应光学结构和射频功率分布，避免被动适应冻结的光学几何。

### 主要贡献
- 提出首个基于3DGS的实时无线辐射场重建框架CORF-GS。
- 设计光学引导采样与耦合优化策略，解决跨模态信源感知差异。
- 仿真结果表明CORF-GS在RF频谱合成质量上达到最先进水平，重建时间相比现有方法减少6.4倍。

### 局限性
摘要未提供足够信息：未报告方法在真实场景、动态环境或不同频段下的性能表现，亦未分析计算资源需求或模型可扩展性。

### 阅读优先级
**高**
理由：该工作首次将在线、实时特性引入无线辐射场重建领域，且提出耦合光学-射频联合优化方案解决跨模态感知差异问题，性能提升显著（重建时间降低6.4倍），对动态无线信道建模有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D Gaussian Splatting (3DGS)-based wireless radiance field (WRF) reconstruction provide an efficient solution for wireless channel modeling. However, existing WRF reconstruction methods rely on pre-collected observations and offline optimization, and thus struggle to provide real-time channel knowledge. To bridge this gap, we propose CORF-GS, a real-time WRF reconstruction framework that processes sequential optical and radio frequency (RF) keyframes. Specifically, CORF-GS constructs a unified Gaussian representation for optical and RF with shared geometry and modality-specific appearance, allowing high-resolution optical images to provide structural priors for WRF reconstruction. When a new keyframe arrives, CORF-GS first employs optical-guided Gaussian sampling to densify the WRF in under-represented regions. Since light and radio waves may respond differently to the same object surfaces due to wavelength mismatch, relying solely on optical guidance may neglect RF-informative areas. Therefore, CORF-GS performs coupled optical-RF optimization to jointly refine the shared Gaussians. Compared with the existing two-stage training pipelines, this prevents WRF from passively adapting to a frozen optical geometry and encourages the shared Gaussians to adapt to both optical structures and RF power distributions. Simulations show that CORF-GS achieves state-of-the-art RF spectrum synthesis quality and reduces the reconstruction time by $6.4\times$ compared with existing WRF methods.

</details>

#### 2026-07-28 - PanoLess: Environment Reconstruction from Partial Reflective Views

**Authors:** Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan
**Links:** [abs](https://arxiv.org/abs/2607.25362) - [pdf](https://arxiv.org/pdf/2607.25362)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, inverse rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PanoLess: Environment Reconstruction from Partial Reflective Views
- 作者：Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan
- 出版日期：2026-07-28
- 分类：Neural Scene Representations & Rendering
- 链接：摘要地址 https://arxiv.org/abs/2607.25362，PDF地址 https://arxiv.org/pdf/2607.25362

### 一句话总结
PanoLess 提出一种基于高斯溅射的框架，仅通过反射表面（如玻璃）的部分视角图像，就能重构出完整的环境照明图，并输出环境支持区域的可见性图。

### 研究问题
如何在仅从反射表面一侧获取的局部视角图像中，重建出具有几何一致性的周围环境照明图（远场 illumination map），以克服传统方法需要 360 度全覆盖数据的限制。

### 核心思路/方法
1. 使用表面对齐的 2D 高斯溅射与延迟着色技术，从部分反射视图中恢复精确的逐像素法线及反射线索。
2. 将这些线索融合到一个神经立方体贴图表示中，用以编码环境照明信息。
3. 额外生成一个可见性图，显式标记环境中的哪些区域得到了部分反射观测的支持。

### 主要贡献
- 提出可在仅利用反射表面一侧图像的情况下重建环境照明的新框架。
- 与需要全 360 度覆盖的现有逆渲染和反射感知高斯溅射方法不同，本方法能够在局部视图输入下实现一致、有物理依据的照明估计。
- 在自建合成基准和公开数据集上超越反射感知基线，并展示出对真实世界反射捕获数据的泛化能力。

### 局限性
摘要未提供足够信息，未提及该方法在特定复杂场景（如非朗伯反射表面、强遮挡或动态环境）下的表现或限制，也未讨论重建计算开销或对输入图像质量的要求。

### 阅读优先级
高。该工作针对部分反射视图这一实用场景提出新的解决方案，在技术路径（高斯溅射+神经立方体贴图）和任务设定上均有新意，且展示了较好的实验结果和泛化性，适合关注环境重建、反射感知渲染的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Reflections from shiny objects and glass facades naturally extend the field of view of a camera, capturing the surrounding environment without the need to pan the camera or acquire a full panorama. We propose PanoLess, a Gaussian-splat-based framework that reconstructs the surrounding environment as a distant illumination map from images captured on only one side of a reflective surface. PanoLess leverages surface-aligned 2D Gaussian splats with deferred shading to recover accurate per-pixel normals and reflection cues, which are fused into a neural cubemap representation of the environment. In addition, PanoLess produces a visibility map that explicitly denotes which regions of the environment are supported by the partial reflective observations. Unlike existing inverse-rendering and reflection-aware Gaussian-splatting approaches, which typically require full 360-degree coverage and struggle under incomplete views, PanoLess enables consistent, physically grounded illumination estimation from partial-view input. We show that PanoLess achieves high-fidelity and geometrically consistent environment reconstruction, outperforming reflection-aware baselines on a new custom synthetic benchmark and publicly available datasets, and demonstrating generalization to real-world reflective captures.

</details>

#### 2026-07-28 - SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation

**Authors:** Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang
**Links:** [abs](https://arxiv.org/abs/2607.25219) - [pdf](https://arxiv.org/pdf/2607.25219)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation
- 作者：Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang
- 出版日期：2026-07-28T02:51:24Z
- 分类：Neural Scene Representations & Rendering（主要），Embodied / Robotics / AR Applications（次要）
- 链接：摘要：https://arxiv.org/abs/2607.25219，PDF：https://arxiv.org/pdf/2607.25219

### 一句话总结
提出一个基于3D高斯泼溅（3DGS）的社交导航仿真平台SONG，结合大语言模型驱动行人轨迹和全身运动合成，并提供基准数据集SONG-Bench与多维评估指标，用于支持视觉感知的社交导航研究。

### 研究问题
现有社交导航仿真平台缺乏视觉观测、移动人物化身或真实感外观与行人行为，无法支持基于视觉的社交导航研究。本文旨在构建一个高保真、可真实模拟视觉感知环境的仿真平台。

### 核心思路/方法
- 采用3D高斯泼溅（3DGS）对场景和人物化身进行真实感表示。
- 使用大语言模型生成语义合理的行人移动轨迹。
- 通过轨迹驱动的全身运动生成器合成连续、自然的肢体运动。
- 构建SONG-Bench，按难度分层的评估任务序列。
- 提出涵盖有效性、安全性、社会合规性的多维评估指标集。

### 主要贡献
1. 提出SONG平台，首个利用3DGS实现场景和人物高保真表示的社交导航仿真平台。
2. 构建SONG-Bench，提供分层难度的评估任务与多维评价指标。
3. 系统评估表明：基于视觉的社交导航远未解决；安全性缺陷先于社交礼节问题；真实世界数据比模型规模更重要。
4. 验证了在平台生成数据上微调可有效提升真实环境下的成功率。

### 局限性
摘要未提供足够信息。例如未说明平台的可扩展性、计算开销、跨场景泛化能力或对人类行为多样性的覆盖程度。

### 阅读优先级
高  
理由：该平台直接针对视觉社交导航模拟的空白，采用3DGS+大语言模型的新技术组合，提供了系统评估与真实场景迁移验证，对从事仿真、机器人导航与具身智能的研究者有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Social navigation has progressed from simplified 2D environments toward a more general vision-based setting, in which a robot needs to achieve socially compliant behavior purely from onboard visual observations. Yet supporting simulation platforms have not kept pace: existing options either lack visual observations, lack moving human avatars, or fall short of real-world fidelity in appearance and pedestrian behavior, offering limited support for advancing vision-based social navigation. We introduce SONG, a SOcial Navigation platform powered by 3D Gaussian splatting (3DGS). It leverages 3DGS for both scene and avatar representations, drives pedestrians using semantically grounded trajectories generated by a large language model, and synthesizes their full-body motion with a trajectory-conditioned generator to produce continuous, natural movement. On top of the platform, we curate SONG-Bench, a set of evaluation episodes stratified by difficulty, and propose a multi-dimensional metric suite covering effectiveness, safety, and social compliance. A systematic evaluation of representative navigation baselines reveals three findings: (a) vision-based social navigation is far from solved; (b) a critical safety deficit precedes social etiquette; (c) real-world data matters more than model scale. Crucially, we demonstrate that fine-tuning on our curated data effectively improves the success rate in real-world environments. We hope our platform provides a faithful and rigorous testbed for the next generation of vision-based social navigation research.

</details>

#### 2026-07-27 - GenSplatCodec: Feed-Forward Gaussian Splatting Compression via One-Step Diffusion

**Authors:** Qiang Hu, Zhenlong Wu, Lei Huang, Zihan Zheng, Xiaoyun Zhang, Wenjun Zhang
**Links:** [abs](https://arxiv.org/abs/2607.24403) - [pdf](https://arxiv.org/pdf/2607.24403)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GenSplatCodec: Feed-Forward Gaussian Splatting Compression via One-Step Diffusion
- 作者：Qiang Hu, Zhenlong Wu, Lei Huang, Zihan Zheng, Xiaoyun Zhang, Wenjun Zhang
- 出版日期：2026-07-27
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.24403

### 一句话总结
本文提出了一个统一的**前馈式高斯泼溅编解码器**，通过**几何引导的一步扩散生成式解码**，在低码率下实现高保真和视图一致的新视角合成。

### 研究问题
现有的前馈式高斯泼溅压缩方法在低码率下，当丢弃高频纹理和视图相关外观信息时，确定性表示恢复解码效果不佳。虽然生成模型作为后处理可以弥补，但会破坏跨视图一致性。因此，本文旨在解决**低码率下高斯泼溅压缩的保真度与视图一致性难以兼顾**的问题。

### 核心思路/方法
1.  **双流编码方案**：提出一种细节感知的前馈式高斯编码，将紧凑的**高斯结构流**与轻量的**参考外观流**相结合，形成双流表示。
2.  **几何引导的解码**：引入几何引导的一步扩散生成式解码方法，联合利用解码后的结构和外观线索，通过**分层几何控制**重建高保真且视图一致的新视图。
3.  **三阶段优化策略**：设计三阶段优化策略，稳定统一编解码器的学习，并使生成式解码器适应来自编解码器的结构和外观线索。

### 主要贡献
- 提出了GenSplatCodec，一种统一的前馈式高斯编解码器，将低码率高斯压缩重新定义为**几何引导的生成式解码**问题。
- 设计了**双流编码方案**和**几何引导的一步扩散解码**方法，有效结合了结构信息与生成能力。
- 提出了**三阶段优化策略**，确保编解码器和生成模型的稳定训练与适配。
- 在多个数据集上，GenSplatCodec在**率失真性能**上持续优于现有方法。

### 局限性
摘要未提供足够信息。摘要仅提及实验表明性能优于现有方法，但未描述具体的失败案例或局限性，例如模型复杂度、推理速度或对特定场景的适应性等问题。

### 阅读优先级
**高**
理由：该论文针对前馈式3D高斯泼溅压缩这一前沿方向，提出了结合扩散生成模型的创新思路（几何引导的生成式解码），并提供了完整的方案设计和性能验证。该方向是神经渲染与压缩领域的交叉热点，对于从事场景表示压缩、视点合成或生成式重建的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) enables scalable scene reconstruction without per-scene optimization, yet produces dense Gaussians that are costly to store and transmit. Existing feed-forward Gaussian compression methods formulate decoding as deterministic representation recovery, which becomes inadequate at low bitrates when high-frequency textures and view-dependent appearance are discarded. Although generative models offer a promising alternative, using them as standalone post-processing decouples generation from the transmitted scene structure, thereby compromising cross-view consistency. To address these limitations, we propose GenSplatCodec, a unified feed-forward Gaussian codec that reformulates low-bitrate Gaussian compression as geometry-guided generative decoding. We present a detail-aware feed-forward Gaussian coding scheme within a dual-stream formulation, where the resulting compact Gaussian structural stream is complemented by a lightweight reference appearance stream. We further introduce a geometry-guided one-step generative decoding approach that jointly exploits decoded structural and appearance cues through hierarchical geometry control to reconstruct high-fidelity and view-consistent novel views. Finally, we develop a three-stage optimization strategy that stabilizes the learning of the unified codec and adapts the generative decoder to codec-derived structural and appearance cues. Extensive experiments across multiple datasets demonstrate that GenSplatCodec consistently achieves superior rate-distortion (RD) performance over existing methods.

</details>

#### 2026-07-26 - Head Avatars with Dynamic Explicit Hair

**Authors:** Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies
**Links:** [abs](https://arxiv.org/abs/2607.23861) - [pdf](https://arxiv.org/pdf/2607.23861)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Head Avatars with Dynamic Explicit Hair
- 作者：Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies
- 出版日期：2026-07-26
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.23861

### 一句话总结
提出一种名为 DynHair 的方法，通过结合基于显式发丝的表示与结构化 3D 高斯溅射，从视频输入中重建具有动态头发运动的可驱动头部虚拟形象。

### 研究问题
如何从视频输入中重建带有动态头发运动（如物理形变）的人体头部虚拟形象，使头发能够像真实场景中一样响应头部运动和重力。

### 核心思路/方法
1. 使用结构化 3D 高斯溅射（3D Gaussian Splatting）表示头发，采用显式发丝（explicit strand-based）结构。
2. 提出一个时间网络（temporal network）来建模头发动态形变：该网络以头部角速度、加速度和相对重力为条件，通过 LSTM 编码运动历史，利用 FiLM 调制（Feature-wise Linear Modulation）调节每根发丝的特征点，再通过 MLP 产生物理上合理的位移，将规范发型形变到当前姿态。
3. 联合优化头发运动和外观表示，以及基于 3DGS 的面部区域表示，通过可微高斯溅射进行监督，损失函数包含光度、几何和物理约束。

### 主要贡献
- 提出 DynHair 方法，实现显式发丝级别的动态头发跟踪与建模，用于可驱动的头部虚拟形象。
- 引入基于 LSTM 和 FiLM 的条件时间网络，使头发形变能由头部运动参数（角速度、加速度、重力）驱动，产生物理合理的效果。
- 在头发动态效果、时间一致性和跨主体泛化方面达到当前最优性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该方法专注于头部虚拟形象中的动态头发建模，属于特定子领域（神经场景表示与渲染）的前沿工作，但未涉及突破性的架构创新或广泛适用的通用方法，适合对该子方向感兴趣的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

We present DynHair, a novel method for tracking and modeling dynamic hair for human head avatars. From video input, we reconstruct a dynamic head avatar with an explicit strand-based hair representation using structured 3D Gaussian Splatting. In contrast to the face region of human head avatars, which can be modeled with 3D Gaussians that are attached or generated with respect to some expressive 3D head model, hair is particularly challenging as it exhibits dynamic motion effects. Therefore, we present a novel method that models the dynamic deformations of the hair strands using a temporal network that is conditioned on angular velocity and acceleration of the head, as well as relative gravity. Specifically, an LSTM encodes the motion history and modulates per-point strand features via FiLM conditioning which further used by MLP to produce physically plausible displacements to canonical hairstyle. We jointly optimize this motion and appearance representation of the hair, with a 3DGS-based representation of the face-region, via differentiable Gaussian splatting with photometric, geometric, and physics-based supervision. As a result of our method, we retrieve hair tracking of the training video data and an animatable head avatar with controllable hair dynamics. In our experiments, we demonstrate state-of-the-art performance in terms of hair dynamics, temporal consistency, and generalization across subjects.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-29 - Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation

**Authors:** Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, Maoqing Yao
**Links:** [abs](https://arxiv.org/abs/2607.26646) - [pdf](https://arxiv.org/pdf/2607.26646)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation  
- 作者：Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, Maoqing Yao  
- 出版日期：2026-07-29  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.26646  

### 一句话总结  
该论文提出一个两阶段的前馈流水线，仅从单张360°全景图生成高质量、可自由探索的室内3D场景，无需逐场景优化或多视角输入，支持零样本泛化。

### 研究问题  
如何从单张360°全景图重建高质量、可自由导航的3D场景，同时解决现有方法缺乏度量轨迹控制、在大范围相机运动下处理大面积遮挡困难以及需要高端多GPU服务器的问题。

### 核心思路/方法  
- **第一阶段：全景视频生成**  
  - 使用NavMesh规划的SE(3)漫游轨迹，通过密集几何扭曲条件注入潜在视频扩散模型。  
  - 采用长-短轨迹混合训练和基于快捷模型的自一致性目标，在无无分类器引导的四步去噪中生成高保真全景视频。  
- **第二阶段：3D重建**  
  - 利用前馈式全景重建器将生成的视频提升为高保真3D高斯场景，支持实时自由视角漫游，可直接作为具身AI模拟资产。

### 主要贡献  
1. 提出一种两阶段流水线，将生成与重建通过显式、轨迹可控的全景视频桥接。  
2. 引入NavMesh规划轨迹注入、长短轨迹混合训练和基于快捷模型的自一致性目标，实现高效高质量视频生成。  
3. 在生成全景视频和下游3D重建任务上均优于几何条件基线，且零样本泛化到未见室内场景。

### 局限性  
摘要未提供足够信息。

### 阅读优先级  
**高**  
理由：该工作解决了具身AI中的关键问题（从单全景图到可导航3D场景的生成），方法创新性强（两阶段桥接生成与重建、快捷模型加速推理），实验证明性能优越且具备零样本泛化能力，对室内3D场景理解和模拟领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We address the problem of reconstructing a high-fidelity, freely navigable 3D scene from a single $360^\circ$ panorama, without per-scene optimization or multi-view capture. Existing methods either lack metric trajectory control, which hinders reliable downstream 3D reconstruction, or struggle with large disocclusions under long-range camera motion while requiring high-end multi-GPU servers.We present Genie Sim PanoWorld, a two-stage feed-forward pipeline that bridges generation and reconstruction via an explicit, trajectory-controllable panoramic video. A NavMesh-planned $\mathrm{SE}(3)$ roaming trajectory is injected into a latent video diffusion model through dense geometry-warped conditioning; long--short trajectory mixed training and a self-consistency objective based on shortcut models together yield high-fidelity video in four CFG-free denoising steps. A feed-forward panoramic reconstructor then lifts the generated video into a high-fidelity 3D Gaussian scene that supports real-time, free-viewpoint roaming and can be directly used as a simulation-ready asset for embodied AI applications. Experiments show that Genie Sim PanoWorld outperforms geometry-conditioned baselines in both panoramic video generation and downstream 3D reconstruction, while generalizing zero-shot to unseen indoor scenes.

</details>

#### 2026-07-28 - Spline-Based Boundary Representations for Sparse View Reconstruction and Simulation Using Isogeometric Analysis

**Authors:** Davor Dobrota, Vsevolod Skorokhodov, Chenghao Xu, Olga Fink, Malcolm Mielle
**Links:** [abs](https://arxiv.org/abs/2607.26234) - [pdf](https://arxiv.org/pdf/2607.26234)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spline-Based Boundary Representations for Sparse View Reconstruction and Simulation Using Isogeometric Analysis
- 作者：Davor Dobrota, Vsevolod Skorokhodov, Chenghao Xu, Olga Fink, Malcolm Mielle
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26234

### 一句话总结
本文提出FORGE-SIM方法，通过优化B样条边界表示，直接从稀疏RGB图像重建紧凑、光滑、水密的几何模型，并同步支持计算机辅助设计和数值仿真。

### 研究问题
如何从稀疏视角的RGB图像直接重建出既适合可视化、又满足数值仿真（如热仿真、模态分析）要求的显式、水密、光滑的几何模型，以消除计算机视觉与数值分析之间的表示鸿沟。

### 核心思路/方法
1. **直接优化样条表示**：不依赖传统网格或隐式表面，而是将多片B样条边界表示作为可优化参数，从稀疏图像中直接回归出几何。
2. **仿真兼容性设计**：重建的几何自动满足水密性和光滑性，原生兼容计算机辅助设计和等几何分析流程。
3. **场投影策略**：将观测得到的场（如热状态、语义信息）以相同样条基函数投影到重建模型上，使模型可直接用于仿真。

### 主要贡献
- 提出了FORGE-SIM，一种无需人工干预、从稀疏RGB图像直接重建多片B样条边界表示的方法。
- 重建的几何紧凑、光滑、水密，同时兼容设计软件与仿真工作流。
- 实现了将观测场（热、语义等）映射到同一样条基上，支持即时仿真应用。
- 模型质量足以支撑热仿真与模态分析，统一了图像重建与仿真建模的优化框架。

### 局限性
摘要未提供足够信息，无法得知具体性能指标、对比方法、失败案例或计算开销等局限性。

### 阅读优先级
**高**  
理由：该方法解决了计算机视觉与数值仿真之间的长期表示不兼容问题，对于数字孪生、仿真驱动设计等跨领域应用有重要启发意义。摘要提供的技术路径清晰、创新点明确，且实验（热仿真、模态分析）初步验证了可行性。建议优先阅读以评估方法细节。

</details>

<details>
<summary>Abstract</summary>

Image-based reconstruction aims to recover three-dimensional geometry from images. Recent advances have enabled the recovery of visually detailed models, yet their representations are not well-suited for numerical simulation. Simulation frameworks typically require explicit, watertight, and smooth geometries to ensure numerical robustness and accuracy, properties that surfaces extracted from image-based reconstructions lack. We propose FORGE-SIM, a method to directly reconstruct a multi-patch B-spline boundary representation from sparse posed RGB images without manual intervention. By optimizing the spline representation itself, our approach produces compact, smooth, and watertight geometries that are natively compatible with both Computer Aided Design and simulation workflows. Additionally, we introduce a strategy to project observation-derived fields, such as a thermal state and semantic information, onto the reconstructed models in the same spline basis, enabling immediate use in simulation. We demonstrate that the obtained models are of sufficiently high quality to enable thermal simulation and modal analysis. By unifying image-based reconstruction and simulation-ready modeling within a single optimization framework, this work removes a long-standing barrier between computer vision and numerical analysis. We anticipate that it will enable new workflows for simulation-driven design, inspection, and digital twin applications.

</details>

#### 2026-07-28 - BG-REAL: A Public Real-Data Anchored Benchmark for Background Manipulation Detection and Localization

**Authors:** Bugra Alperen Uluirmak, Rifat Kurban
**Links:** [abs](https://arxiv.org/abs/2607.26232) - [pdf](https://arxiv.org/pdf/2607.26232)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BG-REAL: A Public Real-Data Anchored Benchmark for Background Manipulation Detection and Localization
- 作者：Bugra Alperen Uluirmak, Rifat Kurban
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.26232，PDF: https://arxiv.org/pdf/2607.26232

### 一句话总结
本文提出BG-REAL，一个专注于背景操作检测与定位的公开真实数据锚定基准测试包，包含7000个处理样本、六种编辑类型，并揭示了现有基线模型因重编码伪影而产生的高误报率问题。

### 研究问题
背景操作是一种实用但定义不够清晰的图像取证场景：操纵证据可能位于显著性前景物体之外，而许多现有评估强调以物体为中心的复制-移动、拼接或通用合成编辑。因此，需要针对背景操作检测与定位的专用基准。

### 核心思路/方法
构建基于Open Images V7实例分割源的真实数据锚定基准测试包BG-REAL。包含7000个样本（6000个公共数据锚定样本+1000个合成对照样本），覆盖六种编辑家族、匹配的真实对照、源组划分、掩码与泄露质量保证、599条人工辅助质量控制行。采用匹配真实对照诊断方法，评估三种完整外部基线（TruFor、MVSS-Net、HiFi-Net）在固定阈值下的误报率。

### 主要贡献
1. 提出了首个公开的、基于真实数据锚定的背景操作检测与定位基准BG-REAL。
2. 提供了完整的构建流程、评估协议、可直接使用的图表和复现文档。
3. 通过匹配真实对照诊断，发现基线模型存在重编码伪影导致的共同捷径风险（误报率0.57至1.00），而非某一特定模型的问题。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。
理由：该工作专注于图像取证中一个特定且实用的子问题——背景操作，并提供了真实的基准数据集和诊断结果，对从事图像篡改检测、特别是背景相关研究的学者有直接参考价值。但论文尚未提出新的检测算法，且摘要未展示在背景操作场景下的具体性能提升，因此优先级适中。

</details>

<details>
<summary>Abstract</summary>

Background manipulation is a practical but under-specified image-forensics setting: the manipulated evidence can sit outside the salient foreground object, while many evaluations emphasize object-centric copy-move, splicing, or generic synthetic edits. We introduce BG-REAL, a public real-data anchored benchmark package for background manipulation detection and localization. The current release is built from Open Images V7 instance-segmentation sources and contains 7,000 processed samples over 1,200 source groups, including 6,000 public-data anchored samples and 1,000 synthetic control samples. BG-REAL covers six edit families, matched authentic controls, source-group splits, mask and leakage QA, 599 human-assisted quality-control rows, three completed external baselines (TruFor, MVSS-Net, and HiFi-Net), and five-seed model evaluation. Beyond aggregate accuracy, we use matched-authentic-control diagnostics to measure how often baselines misclassify re-encoded authentic images as manipulated at a threshold fixed on held-out validation data; false-positive rates range from 0.57 (TruFor, the lowest) to 1.00 (several weak or mask-informed baselines), indicating that re-encoding artifacts are a shared shortcut risk across baselines rather than a problem specific to any one model. The release provides the construction pipeline, evaluation protocol, paper-ready figures, and reproduction documentation. We frame BG-REAL as a background-manipulation-focused complement to general image-manipulation-localization benchmarks, not as a fully real-only or general-purpose benchmark.

</details>

#### 2026-07-28 - DVPSFormer: Efficient Online Depth-aware Video Panoptic Segmentation for Autonomous Driving

**Authors:** Yung-Hsu Yang, Luigi Piccinelli, Siyuan Li, Mattia Segu, Lei Ke, Martin Danelljan, Yuqian Fu, Zuria Bauer, Fisher Yu, Hermann Blum, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2607.26165) - [pdf](https://arxiv.org/pdf/2607.26165)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, rendering, autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DVPSFormer: Efficient Online Depth-aware Video Panoptic Segmentation for Autonomous Driving
- 作者：Yung-Hsu Yang, Luigi Piccinelli, Siyuan Li, Mattia Segu, Lei Ke, Martin Danelljan, Yuqian Fu, Zuria Bauer, Fisher Yu, Hermann Blum, Marc Pollefeys
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2607.26165；PDF：https://arxiv.org/pdf/2607.26165

### 一句话总结
提出一种面向自动驾驶的高效在线深度感知视频全景分割架构DVPSFormer，通过显式场景离散化和在线多数投票机制，在降低延迟的同时在Cityscapes-DVPS和SemKITTI-DVPS基准上达到新SOTA。

### 研究问题
现有深度感知视频全景分割（DVPS）方法依赖多阶段流水线或离线跟踪，计算成本高且不适合实时决策，无法满足自动驾驶对在线、高效4D场景理解的需求。

### 核心思路/方法
1. **显式场景离散化（ESD）**：利用分割查询（segmentation queries）表示前景和背景区域，配合离散到连续（D2C）深度头在单次前向中解码度量深度，紧密耦合语义与几何学习，减少延迟。
2. **在线多数投票机制（OMV）**：利用时间一致性在实例跟踪过程中对分类结果进行修正，提升稳定性。
3. 整体架构为统一在线设计，无需多阶段或离线步骤。

### 主要贡献
- 提出DVPSFormer，首个高效在线的统一架构用于深度感知视频全景分割。
- 设计ESD机制，实现语义与深度学习的紧耦合，显著降低延迟。
- 提出OMV机制，利用时间一致性提升跟踪中的分类效果。
- 在Cityscapes-DVPS和SemKITTI-DVPS基准上取得新SOTA结果。

### 局限性
摘要未提供足够信息，未提及计算资源要求、在极端驾驶场景下的表现、或对标注数据的依赖等具体局限性。

### 阅读优先级
**高**。理由：该论文针对自动驾驶中实时4D场景理解的迫切需求，提出了兼具效率和性能的在线解决方案，并在多个基准上刷新SOTA，方法新颖（ESD和OMV），且提供开源代码和模型，对从事环境感知、机器人导航的从业者和研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Safe autonomous navigation requires a holistic understanding of dynamic environments, necessitating the simultaneous estimation of metric depth, semantic segmentation, and instance trajectories. While depth-aware video panoptic segmentation (DVPS) unifies these tasks, existing approaches often rely on computationally expensive, multi-stage pipelines or offline tracking, rendering them unsuitable for real-time decision-making. To address this, we propose DVPSFormer, a unified online architecture designed for efficient 4D scene understanding. Central to our approach is explicit scene discretization (ESD), a novel mechanism that leverages segmentation queries to represent foreground and background regions, enabling a discrete-to-continuous (D2C) depth head to decode metric depth in a single pass. This tightly couples semantic and geometric learning while significantly reducing latency. Furthermore, we propose an online majority voting (OMV) mechanism that exploits temporal consistency to refine classification during instance tracking. DVPSFormer establishes a new state-of-the-art on the Cityscapes-DVPS and SemKITTI-DVPS benchmarks, offering a streamlined solution for online robotic perception. Code and models are available at https://royyang0714.github.io/DVPSFormer.

</details>

#### 2026-07-28 - S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information

**Authors:** Kaneyoshi Hiratsuka, Benjamin Yen, Ryosuke Kojima
**Links:** [abs](https://arxiv.org/abs/2607.26047) - [pdf](https://arxiv.org/pdf/2607.26047)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information
- 作者：Kaneyoshi Hiratsuka, Benjamin Yen, Ryosuke Kojima
- 出版日期：2026-07-28T17:56:07Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26047

### 一句话总结
本文提出一个将听觉空间信息与视觉特征融合的多模态模仿学习框架S2A2，用于机器人操作任务中的声源定位与识别，并通过仿真和真实机器人实验验证其有效性。

### 研究问题
如何在机器人模仿学习操作任务中，有效利用物体位置、材质及接触/运动引起的声学信息，实现主动声源定位与识别，并完成声学感知驱动的操作目标。

### 核心思路/方法
1. 设计一系列新的“声学感知操作任务”，要求机器人依赖听觉线索（如声音位置、音色）来确定操作目标。
2. 提出多模态模仿学习框架S2A2（Spatial-Spectral Audio Action），该框架将视觉特征与声学空间信息（空间+谱）整合，用于声学感知操作任务。
3. 将ACT、Diffusion Policy、VQ-BeT和π₀等策略集成到S2A2框架中，并通过仿真实验和真实机器人实验进行评估。

### 主要贡献
- 引入了一组新的声学感知操作任务，用于模仿学习，强调机器人通过听觉线索进行主动探索。
- 提出了S2A2框架，该框架能够将视觉特征与声学空间-谱信息进行多模态融合。
- 仿真实验表明，所提方法在同时需要位置和音色信息的任务中效果最佳。
- 真实机器人实验验证了所提任务和框架在真实世界操作中的可行性。

### 局限性
摘要未提供足够信息，无法明确列出本文实验的量化局限性（如失败案例、计算资源需求或任务泛化能力等）。

### 阅读优先级
**中**  
理由：该工作创新性地将听觉空间信息引入机器人操作中的模仿学习，解决了传统方法忽视声音线索的问题，对于多模态机器人学习领域有参考价值。但由于未详细说明方法具体结构、基线对比差异或实验量化结果，目前仅适用于概念验证和领域入门阅读，尚需后续完整论文评估细节。

</details>

<details>
<summary>Abstract</summary>

Acoustic information provides rich cues about object location, material properties, and changes caused by contact or motion. This paper introduces a new set of acoustic-aware manipulation tasks for imitation learning, in which robots must use auditory cues to determine manipulation targets. These tasks require sound source localization and identification for active exploration in robotic manipulation. Also, we propose a multimodal imitation learning framework, Spatial-Spectral Audio Action (S2A2), that integrates visual features with acoustic spatial and acoustic signal information for the acoustic-aware manipulation tasks. We implemented S2A2 models that integrates policies such as ACT, Diffusion Policy, VQ-BeT, and $π_0$, into our framework. Simulation experiments showed that the proposed method is the most effective for tasks requiring both position and timbre. Furthermore, real-robot experiments confirm the applicability of the proposed tasks and framework to real-world manipulation.

</details>

#### 2026-07-28 - Wonder: Video World Model Done Better

**Authors:** Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei
**Links:** [abs](https://arxiv.org/abs/2607.26037) - [pdf](https://arxiv.org/pdf/2607.26037)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wonder: Video World Model Done Better
- 作者：Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei
- 出版日期：2026-07-28T17:45:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26037

### 一句话总结
本文提出一个名为Wonder的通用的视频世界模型，支持实时、可控制摄像头的交互式世界探索，用户可通过移动摄像头在长时程中导航并发现新区域。

### 研究问题
如何构建一个通用的视频世界模型，使其能够实时响应摄像头控制指令，在保持长期连贯性的同时支持用户交互式探索（如移动摄像头、发现和重访区域）。

### 核心思路/方法
1. **摄像头控制**：引入密集坐标场的摄像头条件化方法，通过渲染提供空间对齐的运动和方向线索，使模型直接将摄像头运动视为视觉证据。
2. **记忆机制**：提出高效的基于稀疏注意力的记忆机制，在推理时选择性地关注少量相关上下文标记，不受实际上下文长度限制，实现快速精确的记忆检索。
3. **训练策略**：开发了多种技术来纠正自强制样式的蒸馏流程，提升学生模型对控制信号的遵从性，同时保持教师模型的多样化生成模式和长期记忆能力。

### 主要贡献
- 提出了一个支持实时、长时程、摄像头可控交互的视频世界模型Wonder。
- 设计了基于密集坐标场的摄像头条件化方法和稀疏注意力记忆机制。
- 改进了蒸馏训练流程，平衡了控制信号响应、生成多样性及长期记忆保持。
- 模型能以16 FPS合成多样化的分钟级视频，在长卷中保持连贯的几何、外观和动态。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法涉及视频生成、世界模型、交互控制与长期记忆等前沿交叉领域，且声称实现了实时长时程的可控探索，对机器人仿真、AR/VR及具身智能应用具有潜在重要影响。

</details>

<details>
<summary>Abstract</summary>

We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy. We introduce a novel camera conditioning with a dense coordinate field whose renderings provide spatially aligned motion and orientation cues, allowing the model to interpret camera motion directly as visual evidence. To support fast and precise memory retrieval over a growing generation context, we propose an efficient sparse attention-based memory mechanism, enabling the model to selectively attend to a small set of relevant context tokens at inference time, regardless of actual context length. We further develop several techniques to rectify the self-forcing-style distillation pipeline, improving the student model's ability to respect control signals, as well as maintaining diverse generation modes and long-term memory from the teacher. Together, these components enable Wonder to synthesize diverse, minute-scale videos at 16 FPS while preserving coherent geometry, appearance, and dynamics across long rollouts. Beyond image-to-video generation, Wonder naturally supports video-conditioned generation, allowing existing dynamic scenes to be re-shot in real time.

</details>

#### 2026-07-28 - HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone

**Authors:** Simple AI, :, Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, Yushen Zuo, Ke Rui, Minglei Li, Jinhao Zhang, Zhikang Pan, Xiang Wang, Haoran Jia, Huan Du, Zicheng Zeng, Jun Ma, Guiyu Qin, Di Zhang, Xiaofei Li
**Links:** [abs](https://arxiv.org/abs/2607.25895) - [pdf](https://arxiv.org/pdf/2607.25895)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone
- 作者：Simple AI, :, Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, Yushen Zuo, Ke Rui, Minglei Li, Jinhao Zhang, Zhikang Pan, Xiang Wang, Haoran Jia, Huan Du, Zicheng Zeng, Jun Ma, Guiyu Qin, Di Zhang, Xiaofei Li
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：arxiv.org/abs/2607.25895

### 一句话总结
本文提出HiFi-UMI数据生产系统，通过提升无机器人UMI数据的采集保真度，使得仅用该数据微调的策略能直接部署到真实机器人上，无需任何后训练阶段的真实机器人数据。

### 研究问题
机器人操作策略学习受限于同时具备高保真度和可扩展性的数据匮乏问题：真实遥操作数据精准但成本高、难以规模化；无机器人UMI数据容易采集但保真度低，通常只能用于预训练，仍需少量真实机器人数据作为后训练的“锚点”。本文核心问题是：能否仅通过提高无机器人UMI数据的保真度，完全去除后训练中的真实机器人数据环节。

### 核心思路/方法
本文从四个维度协同设计了一套便携式UMI数据生产系统（HiFi-UMI）以提升数据保真度：
1. **轨迹精度**：采用头戴式离线立体惯性SLAM。
2. **夹爪间相对姿态**：使用原生而非重建的相对姿态估计。
3. **同步性**：利用共享微秒级GPIO触发信号。
4. **视野**：每只手配备两个广角相机，覆盖约200度视野。
该系统在无外部定位基础设施下，可实现3毫米工作空间局部末端执行器精度。基于此系统采集的高保真数据，策略后训练阶段完全使用HiFi-UMI演示数据，无需任何真实机器人轨迹。

### 主要贡献
1. 提出HiFi-UMI数据生产系统，通过提升无机器人UMI数据的保真度，实现了零机器人后训练：仅用HiFi-UMI演示数据微调的策略可直接在真实机器人上部署，并在三个不同架构（视觉-语言-动作族与世界-动作模型族）的基线上，与评估场景内采集的遥操作基线相比，成功率差异仅为-2.5、+3.1和-0.6个百分点。
2. 最强策略在精密插入任务上达到85%成功率，尽管HiFi-UMI轨迹未在该评估场景采集。
3. 在相同语料库上预训练4000小时，将十个未见任务的动作误差降低41%，并使基于StarVLA-QwenPI的真实机器人成功率再提升18.1个百分点。
4. 开源HiFi-UMI-2K数据集：2000小时微秒同步、超宽视角演示数据，每条数据均通过仿真回放自动重建与验证。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：本文针对机器人操作学习的数据瓶颈，提出了一种系统性的数据生产方案，在不依赖昂贵真实机器人数据的情况下实现了高性能策略学习，并提供了大规模开源数据集，对具身智能领域的研究有重要参考价值。实验覆盖多种主流策略架构并报告了量化成功率和动作误差，结果详实。

</details>

<details>
<summary>Abstract</summary>

Learning deployable manipulation policies is bottlenecked by the scarcity of data that is both high-fidelity and scalable. Real-robot teleoperation is accurate but costly to scale; robot-free UMI capture scales readily, and current practice uses the resulting data mainly for pre-training, adding a small real-robot "anchor" at post-training. We ask whether raising the fidelity of robot-free UMI data, rather than shrinking the real-robot fraction, can remove that anchor. We present HiFi-UMI, a portable UMI data-production system co-designed for trajectory accuracy, inter-gripper relative pose, synchronization, and field of view: head-mounted offline stereo-inertial SLAM, native rather than reconstructed relative pose, a shared microsecond GPIO trigger, and two wide-angle cameras per hand covering ~200 degrees. It reaches 3 mm workspace-local end-effector accuracy without external tracking infrastructure. Using this corpus, we demonstrate zero-robot post-training: a policy post-trained solely on HiFi-UMI demonstrations deploys directly on a real robot and matches in-domain teleoperation across three backbones spanning the vision-language-action and world-action-model families, with success-rate differences of -2.5, +3.1, and -0.6 percentage points on StarVLA-QwenPI, OpenPI-pi_0.5, and LingBot-VA; the strongest policy reaches 85% on a precision insertion task, even though the teleoperation baseline is collected in the evaluation scene and no HiFi-UMI trajectory is. Pre-training on 4,000 hours from the same corpus lowers action error on ten unseen tasks by 41% and, on StarVLA-QwenPI, raises real-robot success by a further 18.1 percentage points. We open-source HiFi-UMI-2K, 2,000 hours of microsecond-synchronized, ultra-wide-FoV demonstrations, each automatically reconstructed and validated through simulation replay, as a large-scale, high-fidelity resource for the robot-learning community.

</details>

#### 2026-07-28 - Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control

**Authors:** Jiaxin Bai, Jiaxuan Xiong
**Links:** [abs](https://arxiv.org/abs/2607.25337) - [pdf](https://arxiv.org/pdf/2607.25337)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control
- 作者：Jiaxin Bai, Jiaxuan Xiong
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.25337

### 一句话总结
本文提出Temporal-Distance JEPA，通过从离线轨迹中挖掘有向时间距离成本来训练JEPA世界模型，使潜在模型预测控制的表现优于现有方法。

### 研究问题
如何让JEPA世界模型规划器在离线演示日志中获取真正的进度成本，而非依赖潜空间欧氏距离这种非设计用于规划的信号，从而缩小训练与规划之间的差距。

### 核心思路/方法
1. 保留LeWM的编码器-预测器主干，并从无奖励轨迹中挖掘有向时间成本。
2. 使用同轨迹步序作为正样本，跨轨迹对作为启发性负样本，并加入滚动一致性项匹配规划器视野。
3. 挖掘得到的监督同时作为规划成本和表示信号：拓扑进度时直接部署成本，接触几何主导时通过改进表示提升欧氏规划。

### 主要贡献
1. 提出Temporal-Distance JEPA，能自主从离线轨迹中提取时间进度结构用于规划。
2. 在锁评估下，部署挖掘成本使Two-Room成功率达到100.0%（LeWM为97.4%），共享欧氏规划使OGB-Cube提升14.2分，并改善Push-T。
3. 与LeWM和RC-aux基线对比，在多个环境上匹配或超过两者表现。
4. 消融实验验证了有向头、跨轨迹负样本和滚动一致性各自的贡献。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。该工作针对具体规划场景（JEPA世界模型控制）有明确改进，但需要读者熟悉JEPA和潜在模型预测控制背景，且未提供局限性细节，适合相关方向研究者快速了解方案。

</details>

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space rather than reconstructing pixels, making them a natural backbone for latent model predictive control from offline demonstration logs. JEPA-style training optimizes short-horizon latent prediction, whereas planning requires a multi-step ranking of imagined futures by goal progress. Prior JEPA planners often inherit that ranking from embedding geometry, typically latent Euclidean distance, which arises as a byproduct of representation learning rather than as a progress cost mined from the logs. We propose Temporal-Distance-JEPA, which retains the LeWM encoder--predictor backbone and mines a directed temporal cost from reward-free trajectories: same-trajectory step order supplies positive targets, cross-trajectory pairs act as heuristic negatives, and a rollout-consistency term matches the planner horizon. The mined supervision serves two roles: as the deployed planning cost when progress is topological, and as a representation signal that improves Euclidean planning when contact geometry dominates. Under locked evaluation, deploying the mined cost raises Two-Room success to 100.0% versus LeWM's 97.4%, while shared Euclidean planning on the same temporally trained checkpoint raises OGB-Cube by 14.2 points over LeWM and improves Push-T. Against LeWM and the concurrent RC-aux baseline under locked evaluation, Temporal-Distance-JEPA matches or exceeds both methods on every environment. Ablations show that the directed head, cross-trajectory negatives, and rollout consistency each contribute. Temporal-Distance-JEPA narrows the train--plan gap for JEPA world-model planners by discovering temporal progress structure in offline logs and co-designing cost form with plan-time deployment. Code is available at https://github.com/HKBU-KnowComp/Temporal-Distance-JEPA.

</details>

#### 2026-07-27 - A Smooth Explicit Elastoplastic--Damage Update for Graphics Simulation

**Authors:** Yu Ren, Shuangjiu Xiao, Deli Dong
**Links:** [abs](https://arxiv.org/abs/2607.24509) - [pdf](https://arxiv.org/pdf/2607.24509)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Smooth Explicit Elastoplastic–Damage Update for Graphics Simulation
- 作者：Yu Ren, Shuangjiu Xiao, Deli Dong
- 出版日期：2026-07-27T14:49:08Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.24509

### 一句话总结
本文提出了一种用于图形模拟的显式弹塑性-损伤更新方法，通过光滑激活函数和闭式评估避免局部牛顿迭代，但仅适用于各向同性、比例或接近比例加载场景。

### 研究问题
如何在图形模拟中实现一种兼顾光滑性、可向量化、且保持不可逆变形与渐进退化特性的弹塑性-损伤更新方法，同时避免复杂的局部求解。

### 核心思路/方法
1. **平滑激活与闭式评估**：使用 softplus 函数生成候选等效塑性应变，通过最大历史投影保证不可逆性，并由偏斜塑性应变张量保留残余方向。
2. **损伤驱动**：利用存储历史驱动指数型标量退化变量，主动和冻结分支通过单个响应能量解析评估，无需局部牛顿迭代。
3. **验证实验**：通过一维循环拉伸、二维悬臂弯曲、三维压缩及环面模拟验证了残余变形、单调内变量、梯度一致性和网格敏感性。

### 主要贡献
1. 提出一种紧凑、可向量化的弹塑性-损伤更新方法，显式图形模拟中实现光滑激活与闭式评估。
2. 对比 J2 径向返回基线，方法在速度上略慢（内核 1.51–3.08 倍、结构更新 1.69 倍），但优势在于光滑性和实现简洁性。
3. 定量明确了该方法在比例加载下误差为 1.53%，但在固定幅度 90° 转向时误差达 49.39%，清晰划定了适用边界。

### 局限性
1. 该方法仅适用于各向同性、比例或接近比例加载；不适用于一般返回映射、各向异性损伤或相场断裂场景。
2. 摘要未提供足够信息：未讨论收敛性证明、不同材料参数的鲁棒性、或与现有非线性历史相关方法的全面对比。

### 阅读优先级
**中**  
理由：该方法在图形模拟领域提出了一种平衡光滑性与计算效率的新思路，且实验验证较充分；但其应用范围有限（仅限比例加载），且速度并非优势，适合对显式弹塑性模拟中实现简洁度有需求的研究者参考。若用户更关注高速非线性力学或通用弹塑性算法，则优先级较低。

</details>

<details>
<summary>Abstract</summary>

History-dependent solids require material updates that preserve irreversible deformation and progressive degradation during loading, unloading, and reloading. We present a compact, vectorizable elastoplastic-damage update for explicit graphics simulation, designed for smooth activation and closed-form evaluation rather than exact yield-surface enforcement. A softplus function generates a candidate equivalent plastic strain, a maximum-history projection enforces irreversibility, and a deviatoric plastic-strain tensor retains the residual direction. An exponential scalar degradation variable is driven by the stored history. The active and frozen branches are evaluated analytically from one response energy without a local Newton solve. We evaluate the method using one-dimensional cyclic tension, two-dimensional cantilever bending, controlled three-dimensional platen compression, and a genus-one torus. The results verify residual deformation, monotone internal variables, branchwise energy-gradient agreement, and mesh-resolution sensitivity. An analytical J2 radial-return baseline is compared both as a vectorized kernel and within the same structural solver. The baseline is 1.51--3.08 times faster as a kernel and 1.69 times faster in the structural material update, showing that our contribution is smoothness and implementation simplicity rather than raw speed. A path-direction sweep gives 1.53% normalized equivalent-stress error under proportional loading but 49.39% for a fixed-magnitude 90-degree turn. This quantifies the method's intended restriction to isotropic, proportional or nearly proportional loading; it is not a replacement for general return mapping, anisotropic damage, or phase-field fracture.

</details>

#### 2026-07-27 - KAI: A Kinematic-Aware Interface for Data-Efficient Articulated Object Manipulation

**Authors:** Yaping Li, Zhaxizhuoma, Qiaojun Yu, Jia Zeng, Dahua Lin, Jiangmiao Pang
**Links:** [abs](https://arxiv.org/abs/2607.24493) - [pdf](https://arxiv.org/pdf/2607.24493)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KAI: A Kinematic-Aware Interface for Data-Efficient Articulated Object Manipulation  
- 作者：Yaping Li, Zhaxizhuoma, Qiaojun Yu, Jia Zeng, Dahua Lin, Jiangmiao Pang  
- 出版日期：2026-07-27  
- 分类：具身/机器人/AR应用  
- 链接：arXiv:2607.24493  

### 一句话总结
论文提出一种名为KAI的结构化中间表征，通过嵌入运动学先验来提高关节物体操作策略的样本效率，仅用一半演示数据即可达到或超越基线性能，并展现出良好的鲁棒性和泛化能力。

### 研究问题
如何提升机器人操作关节物体时的样本效率，并使其在低数据场景和复杂视觉环境下仍能保持高性能。

### 核心思路/方法
设计一种名为**KAI (Kinematic-Aware Articulation Interface)**的结构化中间表征，该表征将可解释的几何与运动学先验嵌入策略学习过程，提供与关节物体运动结构对齐的强归纳偏置，从而减少对大量机器人演示数据的依赖。

### 主要贡献
1. 提出KAI这一新的中间表征，有效提升关节物体操作策略的样本效率，尤其在低数据场景下表现突出（平均成功率82.9%，仅用半数演示数据）。  
2. 方法在六项仿真任务中成功迁移至具有未见背景和视觉干扰物的真实场景，展现了良好的泛化性。  
3. KAI的动作无关设计允许与人类交互视频进行协同训练，在多种视觉干扰下仍能达到超过70%的平均成功率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接针对机器人操作中样本效率低和泛化性差的常见痛点，提出了一种简洁且有效的结构化表征方案，实验数据（一半数据、82.9%成功率、70%+视频协同效果）具有较强的说服力，对关注具身智能、操作学习或数据高效策略的研究者具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Articulated object manipulation requires an understanding of kinematic structure that is difficult and costly to learn from robot demonstrations alone. We introduce the Kinematic-Aware Articulation Interface (KAI), a structured intermediate representation that captures the kinematic structure of articulated objects. By embedding interpretable geometric and kinematic priors into policy learning, KAI provides a strong inductive bias aligned with the underlying structure of articulated motion. This design effectively improves sample efficiency, with gains particularly pronounced in low-data regimes: across six simulation tasks, our method achieves an average success rate of 82.9%, matching or surpassing baseline performance while using only half the demonstration data. Our method also exhibits robust generalization to unseen backgrounds and visual distractors, transferring from a single clean training environment to cluttered real-world scenes. KAI's action-agnostic design further enables co-training with human interaction videos to enhance real-world robustness: under diverse visual distractions, our method with video co-training achieves over 70% average success rate.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
