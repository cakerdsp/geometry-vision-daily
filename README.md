# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：39
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 15
  - Embodied / Robotics / AR Applications: 10
  - Neural Scene Representations & Rendering: 10
  - Geometry Foundation Models: 2
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的今日科研趋势综合分析。

---

#### 今日主要趋势

本日论文列表揭示了以下几个主要趋势：

1.  **前馈式方法与基础模型主导的3D重建**：大量工作致力于摆脱传统的逐场景优化范式，转向更可扩展的前馈式框架。这体现在利用几何基础模型（如VGGT-类方法）直接从多视图输入预测场景表示（如3D高斯），并在道路表面重建（`RoadVGGT`）、结构光深度估计（`NSL-SLAM`）和物体操作（`KAI`）中展现出潜力。同时，文本到图像扩散模型的先验知识被重新用于解决特定难题，如透明表面感知（`SILICA`）。

2.  **以SLAM为核心的智能体协同与AR整合**：SLAM系统正从单一任务扩展到更复杂的多智能体协同和人机协作场景。焦点从单纯提高精度，转向平衡不同智能体（如机器人 vs. AR用户）的差异化延迟需求（`SHARE`），并通过融合高保真深度传感（`NSL-SLAM`）和利用大尺度场景的空间分解策略（`GLAM-SLAM`）来提升鲁棒性和实用性。

3.  **动态场景建模的深化与“未来”预测**：动态场景重建正从简单的渲染向更准确的物理运动建模演变。这体现在对头发动力学（`DynHair`）、运动解耦（`GrainGS`）的精细建模，以及对未来时域几何的预测需求（`FutureSurf`基准）。研究者开始关注模型是否真正理解了运动的物理规律，而不仅仅是拟合观测数据。

4.  **数据效率与弱/自监督学习的持续崛起**：为了降低对昂贵人工标注的依赖，利用弱监督、自监督和跨模态学习成为核心策略。这包括从视频中自监督分离相机与物体运动（`SDM`），利用RGB-D追踪器自监督LiDAR人体姿态估计（`Factorized Spatio-Temporal Convolutions`），以及通过多教师蒸馏和雷达融合提升恶劣天气下的自监督深度估计（`Boosting Robustness`）。

#### 技术路线观察

-   **几何基础模型与3D/4D重建**：本类论文（如`NSL-SLAM`, `RoadVGGT`, `MSVS-VAE`）的技术路线明显偏向于**前馈式网络**。它们倾向于将特定领域先验（如道路结构、运动学）或预训练基础模型（如VGGT, 扩散模型）集成到网络中，以实现对单/多视图输入的快速、一致推理。`FutureSurf`则开辟了一个全新的评估路线，提出了一个验证动态模型是否理解物理规律的诊断基准。

-   **神经场景表示与渲染**：本类（`GenSplatCodec`, `DynHair`, `GrainGS`）技术路线核心是**3D高斯泼溅（3DGS）** 的扩展与优化。它们致力于解决3DGS在处理压缩（`GenSplatCodec`）、动态（`DynHair`, `GrainGS`）和大尺度场景（`GLAM-SLAM`）时的局限性。其中，动态场景的解决方案出现分歧：有的采用**锚定+每高斯形变**的混合架构（`GrainGS`），有的则结合**显式发丝表示与时间网络**（`DynHair`）。

-   **具身/机器人/AR应用**：本类（`KAI`, `HGeo-TopoMap`, `SHARE`, `DAP-Pose`）的技术路线更侧重于**系统集成**与**任务特定设计**。例如，`KAI`通过设计运动学感知的中间表征来提升样本效率；`SHARE`通过用户中心的调度策略整合边缘计算和实时性；`DAP-Pose`则设计深度时序对齐模块来解决多传感器异步问题。这些工作通常不会单独提出全新的3D表示，而是巧妙地将现有技术（Implicit Representation, SLAM, 传感器融合）组合并适配于特定任务。

#### 值得优先阅读的论文

1.  **NSL-SLAM** - 理由：代表了一个**高精度深度传感器+SLAM**的可行范式。其“强深度使你SLAM管道可以变简单”的理念具有很强的启发性，且实验证明了在当前sota方法基础上依然能获得显著提升（深度精度提升35%）。对于研究实用型SLAM和AR的学者，这是必读。
2.  **SILICA** - 理由：巧妙地**重新利用预训练扩散模型的先验知识**来解决“透明表面”这一公认的难题，完全绕过了真实数据的稀缺性。其零样本迁移能力和20%的显著性能提升，展示了通用视觉先验的另一种有效应用路径。
3.  **MSVS-VAE** - 理由：直接挑战并**弥合了基于集合的VAE与性能更优的基于体素的VAE之间的保真度差距**。这对于基于潜在扩散的3D生成模型至关重要。其分层稠密化和局部聚合算子（AVS-Conv）的设计思路，为解决3D VAE的瓶颈提供了清晰有效的方案。
4.  **FutureSurf** - 理由：提出了一个新颖且关键的评估问题：“动态重建模型是否真的理解了物理规律？” 通过构建基准和证伪控制，揭示了现有sota方法在预测未来表面时存在严重误差，且渲染质量与未来曲面准确性解耦。这为动态场景建模的研究方向设立了新的评估标准。
5.  **SDM** - 理由：针对**从视频中分离相机运动与物体运动**这一基础且未充分解决的问题，提出了一种只需弱监督的解决方案。其表现与强监督方法（VGGT）相当，证明了自监督+弱监督范式在此类解耦任务上的巨大潜力。

#### 可能的研究机会

1.  **未来表面预测的专用架构**：`FutureSurf` 的基准表明现有方法（DG-Mesh, Deform-3DGS）在预测未来时表现不佳。一个清晰的机会是开发**专门用于时域外推的动态表面重建模型**，该模型需要显式地融入物理运动模型（如轨迹预测、波动方程）而非仅仅依赖隐式变形。
2.  **前馈式4D重建与压缩**：`RoadVGGT` 和 `GenSplatCodec` 分别展示了前馈式3D重建与压缩的潜力。将它们结合，可以尝试开发一个**端到端的前馈式动态（4D）场景编解码器**，直接从视频流预测紧凑的、可驱动的动态场景表示，并支持高效的存储和传输。
3.  **跨任务的知识蒸馏与统一表示**：`SILCA` 和 `Boosting Robustness` 都利用了多教师蒸馏。另一个机会是探索**如何为一个复杂的多模态任务（如人机协作导航）构建一个统一的基础模型**，使其能同时进行玻璃分割、深度估计、运动预测和规划，并利用自监督信号从大量无标注数据中学习。
4.  **针对异构智能体的协同SLAM**：`SHARE` 的工作启发了一个方向，即**设计能够感知和适应不同任务需求的异构智能体SLAM系统**。例如，为一个由高速无人机、精准操作机械臂和头戴AR设备组成的团队，优化其之间的地图共享与计算调度策略。

#### 风险和不确定性

-   **结论的泛化性需全文验证**：许多论文的优越性能是在特定数据集或环境下报告的。例如，`NSL-SLAM` 的深度提升（35%）和`SILICA` 的性能提升（~20%）是否泛化到更多样、更具挑战性的真实场景，需要阅读全文以了解其对数据集构成和测试条件的详细描述。
-   **因果解释的可靠性**：`KAI` 声称仅用一半数据即可达到相似性能，`SDM` 声称实现了有效解耦。这些结论依赖于精心设计的实验和消融研究。读者需要检查全文中是否排除了其他可能的影响因素（如网络容量、数据随机性），以确认观察到的提升确实源于提出的核心组件，而非偶然。
-   **实际部署的可行性**：`GLAM-SLAM` 和 `DAP-Pose` 强调了实时性，`Factorized Spatio-Temporal Convolutions`

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-28T10:34:30-04:00
**Total number of papers:** 39
**Number of papers added in the latest update:** 12
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

#### 2026-07-21 - IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer

**Authors:** Zhengyu Zou, Hao Li, Kuixuan Jiao, Liu Liu, Tingyang Xiao, Xiaolin Zhou, Fangzhou Hong, Zhizhong Su, Dingwen Zhang, Ziwei Liu
**Links:** [abs](https://arxiv.org/abs/2607.19228) - [pdf](https://arxiv.org/pdf/2607.19228)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** feed-forward reconstruction, feed-forward 3D reconstruction, 3D reconstruction, pose estimation, scene understanding, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer
- 作者：Zhengyu Zou, Hao Li, Kuixuan Jiao, Liu Liu, Tingyang Xiao, Xiaolin Zhou, Fangzhou Hong, Zhizhong Su, Dingwen Zhang, Ziwei Liu
- 出版日期：2026-07-21
- 分类：Geometry Foundation Models（主要），3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications（次要）
- 链接：摘要: https://arxiv.org/abs/2607.19228 ; PDF: https://arxiv.org/pdf/2607.19228

### 一句话总结
提出一种流式实例-几何融合的Transformer（IGGT4D），能够在线处理视频序列，实现动态场景中几何与实例一致性的4D理解与重建。

### 研究问题
现有流式3D重构方法偏重于几何信息，缺乏时间一致的物体级别理解；而语义重建与3D视觉-语言方法多依赖外部2D语义线索或松散耦合的几何输入，无法在长时间动态场景中实现统一的几何-实例学习。因此，需要一种能在流式视频中同时保持几何和实例一致性的在线4D场景理解方法。

### 核心思路/方法
1. **流式架构**：顺序处理视频帧，通过因果时空建模复用历史上下文，增量更新包含相机运动、几何和物体标识的统一表示。
2. **数据集构建**：为解决高质量4D监督数据缺乏的问题，构造了包含真实/合成、静态/动态场景的大型数据集InsScene4D-147K，并采用自动化几何引导标注流程生成时间一致的实例掩码。
3. **前馈重建**：支持长序列的前馈式重建，在动态环境中保持几何-实例一致性。

### 主要贡献
1. 提出IGGT4D，一个流式实例-几何融合的Transformer，实现在线4D场景理解。
2. 构建大规模数据集InsScene4D-147K，涵盖多种场景类型及时间一致的实例标注。
3. 在3D重建、位姿估计、实例空间追踪和开放词汇分割任务中，IGGT4D优于现有流式基线方法，同时保持对长动态序列的可扩展在线推理能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对流式动态场景的4D理解与重建任务，在方法上融合了几何与实例学习，并提供了新的数据集，对从事3D/4D场景理解、空间智能的相关方向有参考价值。但摘要未透露关键设计细节（如Transformer结构、因果建模的具体机制），需进一步阅读正文评估创新深度。

</details>

<details>
<summary>Abstract</summary>

Real-world spatial intelligence requires agents to understand scenes from continuous video streams, where objects move, persist, disappear, and reappear over time. While recent spatial foundation models have enabled generalizable feed-forward 3D reconstruction, most streaming methods remain geometry-centric and lack temporally consistent object-level understanding. Meanwhile, existing semantic reconstruction and 3D-aware vision-language methods largely rely on externally extracted 2D semantic cues or loosely coupled geometry inputs, limiting unified geometry-instance learning in long dynamic scenes. In this paper, we propose IGGT4D, a streaming instance-grounded geometry Transformer for online 4D scene understanding. IGGT4D processes video frames sequentially, reuses historical context through causal spatial-temporal modeling, and incrementally updates a unified representation of camera motion, geometry, and object identity. This enables long-sequence feed-forward reconstruction with geometry-instance consistency in dynamic environments. To address the lack of high-quality 4D supervision, we further construct InsScene4D-147K, a large-scale dataset spanning real/synthetic and static/dynamic scenes, with RGB images, depth, poses, and temporally consistent instance masks generated by an automated geometry-guided annotation pipeline. Experiments on 3D reconstruction, pose estimation, instance spatial tracking, and open-vocabulary segmentation demonstrate that IGGT4D outperforms existing streaming baselines while maintaining scalable online inference for long dynamic sequences.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

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

#### 2026-07-23 - FA-LAM: Focus-Aware Large Avatar Model for One-Shot 4D Animatable Gaussian Head

**Authors:** Yingdong Hu, Yisheng He, Yiming Jiang, Zehong Lin, Steven Hoi, Jun Zhang
**Links:** [abs](https://arxiv.org/abs/2607.20922) - [pdf](https://arxiv.org/pdf/2607.20922)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, dynamic 4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FA-LAM: Focus-Aware Large Avatar Model for One-Shot 4D Animatable Gaussian Head
- 作者：Yingdong Hu, Yisheng He, Yiming Jiang, Zehong Lin, Steven Hoi, Jun Zhang
- 出版日期：2026-07-23
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2607.20922

### 一句话总结
FA-LAM 是一个用于单次生成可动画化高斯头部模型的焦点感知大模型，通过分析注意力机制与训练任务冲突，改进了3D/4D头部重建质量。

### 研究问题
如何解决现有方法在单次可动画化高斯头部生成中存在的两个问题：(1) 注意力激活不正确且带有噪声；(2) 重建任务与动画任务之间的目标冲突。

### 核心思路/方法
1. **对称语义注意力正则化**：利用人头的语义和结构对称性，对注意力激活进行正则化。
2. **双阶段训练流水线**：将大视角幻觉能力与动画能力解耦至不同模块，分别优化。
3. **核心自回归修改与可见性感知令牌融合**：支持多视角和流式4D重建，提高效率与内存友好性。

### 主要贡献
- 指出了现有方法在3D全头生成质量低下的两个根本原因（注意力问题与任务冲突）。
- 提出了对称语义注意力正则化策略，改善注意力激活质量。
- 设计了双阶段训练流水线，消除重建与动画任务间的冲突。
- 增强了模型对多视角和流式4D重建的支持，并保持内存高效。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对可动画化高斯头部生成中的核心瓶颈（注意力噪声与任务冲突）提出了系统性解决方案，并支持4D流式重建，对动态3D人脸/头部建模领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We propose FA-LAM, a Focus-Aware Large Avatar Model for one-shot animatable Gaussian head creation, while simultaneously enabling static 3D and dynamic 4D full-head recovery. The core of our method lies in a thorough analysis of the attention mechanisms and the entangled reconstruction and animation training pipeline adopted by prior state-of-the-art approaches. Our analysis identifies two main factors that compromise the quality of 3D full-head generation: (1) incorrect and noisy attention activations, and (2) conflicts between the tasks of reconstruction and animation. To address the first issue, we introduce a symmetric and semantic attention regularization strategy that leverages the inherent semantics and structural symmetry of human heads. To disentangle the objectives of reconstruction and animation, we develop a novel dual-phase training pipeline that separates the model's capabilities for large-view hallucination and animation into distinct modules. Moreover, we enhance our model to support multi-view and streaming 4D reconstruction in an efficient and memory-friendly manner through a core autoregressive modification with tailored visibility-aware token fusion. Collectively, these innovations enable FA-LAM to reconstruct animatable Gaussian full heads with superior quality, particularly in fine facial regions and large viewing angles.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

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

#### 2026-07-23 - Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar

**Authors:** Simone Arreghini, Mirko Nava, Nicholas Carlotti, Antonio Paolillo, Alessandro Giusti
**Links:** [abs](https://arxiv.org/abs/2607.21309) - [pdf](https://arxiv.org/pdf/2607.21309)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar
- 作者：Simone Arreghini, Mirko Nava, Nicholas Carlotti, Antonio Paolillo, Alessandro Giusti
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.21309

### 一句话总结
本文提出一种基于时空分离卷积的轻量级网络，利用平面LiDAR序列实现服务机器人的全向人体检测与二维姿态估计，通过跨模态自监督训练减少人工标注需求。

### 研究问题
如何利用计算资源受限的服务机器人上常见的全向平面LiDAR传感器，实现高效、精确的人体检测、距离估计和朝向识别。

### 核心思路/方法
设计基于“时空块”的轻量级网络，将沿扫描射线的空间处理与跨扫描帧的时间聚合显式分离；训练阶段使用RGB-D人体追踪器在传感器重叠区域提供跨模态自监督信号，避免手动标注LiDAR数据。

### 主要贡献
1. 提出显式分离空间与时间处理的轻量级网络结构，适配平面LiDAR序列。
2. 采用跨模态自监督训练方法，消除对LiDAR人工标注的依赖。
3. 在定量实验中，相比参数匹配的基线模型，在距离误差（-38%）、位置误差（-28%）和朝向误差（-15%）上均有显著改善。
4. 在FROG公开数据集上验证性能，并在真实服务机器人上实现实时CPU推理和现场演示。

### 局限性
摘要未提供足够信息。例如未讨论在极端光照、动态遮挡或复杂多人场景下的性能退化情况，也未说明跨模态自监督对RGB-D追踪器精度有多少依赖。

### 阅读优先级
**高**
理由：本文直接针对服务机器人最常见的低算力平面LiDAR场景，提出兼具轻量级、低标注成本和高精度的解决方案，对社交机器人导航与人机交互具有直接应用价值。实验数据具体（误差降低百分比）且涵盖公开数据集与真实部署，适合相关领域研究者阅读。

</details>

<details>
<summary>Abstract</summary>

Localizing nearby humans and estimating their facing direction are key capabilities for safe navigation and socially aware human-robot interaction. Many pose-estimation pipelines target cameras and 3D LiDAR or assume GPU-class compute, whereas service robots are often equipped only with omnidirectional planar LiDARs and modest onboard processors. We address omnidirectional human detection and relative 2D pose estimation from planar LiDAR sequences with a lightweight network based on Space-Time Blocks, which explicitly separate spatial processing along scan rays from temporal aggregation across scans. Our network processes 360° LiDAR sequences to output per-ray human presence, distance, and relative orientation. We train it via cross-modal self-supervision from a narrow RGB-D body tracker in the sensors' overlap region, removing the need for manual LiDAR labels. Quantitative experiments show that our approach consistently outperforms a parameter-matched baseline model, reducing errors in distance (-38%), position (-28%), and orientation (-15%). We further benchmark on the public FROG dataset, report real-time CPU inference on a service robot, and validate with in-field demonstrations, supporting its suitability for spatial perception on computationally constrained service robots.

</details>

#### 2026-07-23 - TransBiolab: A Real-World Multi-View Dataset of Cluttered Transparent Biomedical Objects

**Authors:** Ke Ma, Yifei Wang, Meng Wang, Tian Xia
**Links:** [abs](https://arxiv.org/abs/2607.21071) - [pdf](https://arxiv.org/pdf/2607.21071)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, depth estimation, camera calibration, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TransBiolab: 杂乱透明生物医学物体的真实多视角数据集
- 作者：Ke Ma、Yifei Wang、Meng Wang、Tian Xia
- 出版日期：2026-07-23
- 分类：3D重建与多视角几何
- 链接：https://arxiv.org/abs/2607.21071

### 一句话总结
提出一个针对杂乱透明生物医学物体的真实世界RGB-D多视角数据集TransBiolab，包含大量标注帧和多种任务基准，旨在推动自动化实验室操作中的视觉感知研究。

### 研究问题
现有透明物体数据集通常不评估真实实验室操作场景中的多物体杂乱、遮挡和标定多视角捕获的组合设置，导致该领域缺乏高质量的真实世界数据。

### 核心思路/方法
1. 构建真实世界RGB-D数据集，包含98个场景共161,315帧，覆盖15种实验室物体类型，提供1.03M实例标注。
2. 数据集沿三个难度轴组织：物体类别、帧中物体总数、相机视角。
3. 定义以数据集为中心的基准任务：分割、深度估计与补全、6D姿态估计。
4. 通过释放的标注和标定执行系统级机器人操作评估。

### 主要贡献
1. 提供首个面向杂乱透明生物医学物体的标定多视角真实世界数据集。
2. 数据集包含6D姿态、全掩码与可见掩码、深度和逐帧相机标定等丰富标注。
3. 定义了多种视觉任务的基准并报告了机器人操作评估结果。
4. 聚焦重复透明实例、杂乱场景和实验室多视角捕获，补充现有数据集的空白。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该数据集针对透明生物医学物体这一特殊场景，填补了现有数据集的空白，同时涵盖多视角、杂乱、遮挡等实际挑战，对自动化实验室视觉感知领域有直接推动作用；且提供了多种基准任务和机器人操作评估，具有较高实用价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous biomedical laboratories increasingly rely on visual perception to recognize, localize, and manipulate transparent plasticware, yet high-quality real-world datasets for this setting remain limited. The scarcity of domain-relevant data is particularly restrictive in cluttered multi-object scenes, where mutual occlusion and view-dependent appearance changes remain challenging even for contemporary visual foundation models. Existing transparent-object datasets have advanced segmentation, depth, and pose estimation, but they usually do not evaluate the combined setting of multi-object clutter, occlusion, and calibrated multi-view capture that characterizes real laboratory manipulation scenes. To address this gap, we present TrainsBiolab, a real-world RGB-D dataset of cluttered transparent biomedical objects captured as calibrated multi-view sequences. TrainsBiolab contains 161,315 frames from 98 scenes and 1.03M instance annotations over 15 laboratory object types, including 6D poses, full and visible masks, depth, and per-frame camera calibration. The dataset is organized along three axes that reflect operational difficulty: object category, the total number of objects in a frame, and camera viewpoint. We further define dataset-centric benchmarks for segmentation, depth estimation and completion, and 6D pose estimation, and report a system-level robot manipulation evaluation enabled by the released annotations and calibrations. By focusing on repeated transparent instances, clutter, and multi-view laboratory capture, TrainsBiolab provides a resource for segmentation, depth estimation, 6D pose estimation, and multi-view reasoning in autonomous laboratory manipulation. Project page: https://dualtransparency.github.io/TransBiolab/.

</details>

#### 2026-07-23 - WAT3R: Feedforward Underwater 3D Reconstruction

**Authors:** Jiayi Xu, Jiahao Lu, Ziqiang Zheng, Yihao Tan, Yaolong Zhu, Yuan Liu, Sai-Kit Yeung
**Links:** [abs](https://arxiv.org/abs/2607.21023) - [pdf](https://arxiv.org/pdf/2607.21023)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, multi-view reconstruction, camera pose estimation, pose estimation, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WAT3R: Feedforward Underwater 3D Reconstruction
- 作者：Jiayi Xu, Jiahao Lu, Ziqiang Zheng, Yihao Tan, Yaolong Zhu, Yuan Liu, Sai-Kit Yeung
- 出版日期：2026-07-23T08:07:43Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.21023

### 一句话总结
提出了一种前馈式框架WAT3R，通过轻量级神经适配模块处理水下光照衰减和背向散射，直接从水下图像高效重建高质量3D场景。

### 研究问题
水下图像因光线衰减和背向散射导致视觉质量下降、跨视角特征不一致，使得前馈式3D重建难以获得准确的多视图几何结构。

### 核心思路/方法
将水下成像退化视为一种受几何约束的过程，集成一个轻量级神经适配模块来灵活建模成像效应，从而在单个前向传播中从水下视频直接输出像素对齐的3D点图与相机位姿。

### 主要贡献
1. 提出了WAT3R，一个前馈式水下3D重建框架，无需迭代优化即可高效重建。
2. 设计退化适配模块，将水下成像效应作为几何约束过程处理，改善多视图重建质量。
3. 在FLSea、SQUID和USOD10K数据集上，该方法在多视图/单目深度估计与相机位姿估计任务上均超越现有最先进方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对水下环境这一特定场景提出前馈式3D重建方案，并在公开数据集上取得显著提升，方法具有实用性；但未涉及泛化性分析或极端退化案例，且摘要未提供实验细节，适合对水下视觉或前馈式3D重建感兴趣的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Reliable feedforward underwater 3D reconstruction remains challenging due to severe light attenuation and backscattering, which degrade visual quality and disrupt feature consistency across views, leading to inaccurate multi-view geometry. To address this issue, we propose WAT3R, a feed-forward framework for reconstructing 3D scenes directly from underwater images. By leveraging degradation adaptation as a geometry-constrained process, WAT3R integrates a lightweight neural adaptation module to flexibly account for these underwater imaging effects, thereby improving multi-view reconstruction quality. Implemented in a single forward pass, WAT3R directly and efficiently outputs pixel-aligned 3D point maps and camera poses from underwater videos, allowing a high-quality underwater 3D reconstruction. Experiments conducted on the FLSea, SQUID, and USOD10K datasets show that our method consistently outperforms state-of-the-art approaches on 3D reconstruction tasks, including multi-view/monocular depth estimation and camera pose estimation.

</details>

## Neural Scene Representations & Rendering

### 2026-07

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

#### 2026-07-23 - SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization

**Authors:** Jiun Lee, Jaekwang Kim, Sangmin Lee
**Links:** [abs](https://arxiv.org/abs/2607.20813) - [pdf](https://arxiv.org/pdf/2607.20813)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization
- 作者：Jiun Lee, Jaekwang Kim, Sangmin Lee
- 出版日期：2026-07-23
- 分类：Neural Scene Representations & Rendering (神经场景表征与渲染)
- 链接：摘要: https://arxiv.org/abs/2607.20813 | PDF: https://arxiv.org/pdf/2607.20813

### 一句话总结
SubSplat 提出了一种亚像素高斯重参数化方法（SPGR），通过将低分辨率特征中的主高斯分解为细粒度基元，在保持低计算成本的同时实现了高分辨率、像素对齐的逼真新视角合成。

### 研究问题
像素对齐的高斯泼溅在渲染高分辨率图像时面临两难困境：提高输入分辨率可改善细节但使网络计算成本呈二次方增长；而保持低分辨率输入虽能稳定计算成本，却导致高斯密度不足并产生视觉伪影。SubSplat 旨在解决这一计算效率与渲染保真度之间的权衡问题。

### 核心思路/方法
核心思路是引入 **Sub-pixel Gaussian Reparameterizer (SPGR)**，直接从低分辨率特征中恢复高斯密度。具体做法是：将原始（初级）高斯体细分为更精细的基元（fine-grained primitives），从而在不依赖高分辨率输入的情况下重现必要的结构细节。此外，通过 **特征聚合（feature aggregation）** 增强重参数化质量，该机制能有效地从多视角捕捉高频细节。

### 主要贡献
1. 提出 SubSplat 框架，成功解决了像素对齐高斯泼溅中重参数化保真度与网络计算成本之间的固有矛盾。
2. 引入 SPGR，在低计算成本下从低分辨率特征重建高密度高斯基元，实现高效的高分辨率渲染。
3. 通过多视图特征聚合增强重参数化效果，提升高频细节的捕获能力。
4. 在 RealEstate10K 和 ACID 数据集上验证了该方法在渲染质量和效率上的优越性。

### 局限性
摘要未提供足够信息，例如在特定场景（如非朗伯表面或极稀疏视图）下的表现、对视频/动态场景的适用性，或计算资源需求的具体量化指标。

### 阅读优先级
**高**。理由：该工作直接针对像素对齐高斯泼溅在多分辨率下的核心计算瓶颈（二次方增长 vs. 密度不足），并提出了一种新颖的重参数化解法。结合其在标准数据集（RealEstate10K, ACID）上的验证，对关注高效神经渲染和 3D 高斯泼溅优化的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Pixel-aligned Gaussian splatting enables efficient and generalizable novel-view synthesis. However, high-resolution rendering faces a critical trade-off where increasing input resolution improves detail at the expense of quadratically rising network computational cost. Conversely, maintaining low-resolution inputs stabilizes this cost but results in insufficient Gaussian density and artifacts. To address this, we propose SubSplat, which introduces Sub-pixel Gaussian Reparameterizer(SPGR) to subdivide primary Gaussians into fine-grained primitives, restoring structural density directly from low-resolution features. We further enhance the reparameterization quality through feature aggregation, which effectively captures high-frequency details across multiple views. Experiments on RealEstate10K and ACID demonstrate that SubSplat achieves high-fidelity rendering with superior efficiency. Our results validate that the proposed framework successfully resolves the trade-off between reparameterization fidelity and network computational cost inherent in pixel-aligned Gaussian Splatting.

</details>

#### 2026-07-22 - 3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch

**Authors:** Xuening Tian, Dieter Schmalstieg, Shohei Mori
**Links:** [abs](https://arxiv.org/abs/2607.20789) - [pdf](https://arxiv.org/pdf/2607.20789)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch
- 作者：Xuening Tian, Dieter Schmalstieg, Shohei Mori
- 出版日期：2026-07-22
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.20789

### 一句话总结
本文提出3D-GIMP方法，通过一次生成式修补结合3D-aware PatchMatch传播，高效实现3D高斯泼溅场景中的高保真物体移除，避免了逐帧扩散的高成本与多视图不一致问题。

### 研究问题
如何在3D高斯泼溅场景中高效、高保真地去除物体，同时保持渲染速度、视图一致性和高频细节，避免逐帧扩散带来的计算瓶颈和“幻觉漂移”导致的视图不一致与结构伪影。

### 核心思路/方法
1. **单参考视图生成**：仅对单个关键参考视图进行一次生成式修补，将其作为外观先验。
2. **3D-aware PatchMatch传播**：设计三维感知的PatchMatch算法，通过对应匹配将参考纹理传播至所有剩余视图，避免逐帧扩散的随机性。
3. **重建一致性优先**：优先保证重建数学一致性而非迭代生成，从而在不同分辨率下维持高频细节，确保三维重建在数学上一致。

### 主要贡献
- 提出一种新的混合范式3D-GIMP，将单次生成修补与3D-aware PatchMatch结合，用于3D高斯泼溅中的高保真物体移除。
- 实验表明，3D-GIMP在修补质量上与使用多视图扩散的先前方法竞争力相当，同时在渲染速度和视图一致性上超越这些方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接针对3D场景编辑中的核心痛点（计算效率、视图一致性、细节保留），提出一种轻量且有效的混合方案；实验表明其性能在渲染速度和一致性上优于主流的多视图扩散方法，对实际应用具有重要潜力。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D scene editing have leveraged iterative diffusion models to update input views. However, this process is computationally expensive and struggles to produce sharp details. Meanwhile, ``hallucination drift'' frequently introduces multi-view inconsistencies, leading to structural artifacts when rendering novel viewpoints. To address this problem, we present 3D-GIMP (3D Gaussian Inpainting Meets Patch Matching), a novel hybrid paradigm designed for high-fidelity object removal in 3D Gaussian Splatting. Instead of diffusing every view, 3D-GIMP performs a single generative inpainting on a key reference view, which serves as an appearance prior. We then introduce a 3D-aware PatchMatch algorithm to propagate these reference textures across all remaining views via correspondence matching, effectively bypassing the stochastic nature of frame-by-frame diffusion. By prioritizing reconstructive consistency over iterative generation, 3D-GIMP maintains high-frequency details across arbitrary resolutions while ensuring a mathematically consistent 3D reconstruction. Our experiments demonstrate that 3D-GIMP not only achieves competitive inpainting quality as previous methods using diffusion in multiple views, but also outperforms these methods in rendering speed and view consistency.

</details>

#### 2026-07-22 - RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring

**Authors:** Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue
**Links:** [abs](https://arxiv.org/abs/2607.20628) - [pdf](https://arxiv.org/pdf/2607.20628)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring
- 作者：Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue
- 出版日期：2026-07-22（需注意该日期晚于当前时间，可能为未来论文或笔误）
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：摘要URL: https://arxiv.org/abs/2607.20628；PDF URL: https://arxiv.org/pdf/2607.20628

### 一句话总结
本文提出RealVDeblur，一个基于单步扩散模型的视频去模糊框架，通过物理驱动的模糊合成管道和高效推理设计，实现在真实世界多样条件下的鲁棒复原。

### 研究问题
真实世界视频去模糊面临运动模式多样化、退化复杂以及真实训练数据稀缺的挑战，且需为下游任务（如移动成像、3D重建）提供稳健的复原结果。

### 核心思路/方法
1. **模糊合成管道**：利用场景级3D高斯泼溅（3DGS）资产和高帧率视频构建大规模、物理逼真的模糊合成管道，生成包含相机运动模糊和物体运动模糊的训练数据。
2. **视频扩散先验**：采用视频扩散模型作为复原先验，为适应帧间模糊变化，禁用VAE中的时间压缩并改用逐帧编码方案。
3. **高效推理**：将扩散模型的多步采样蒸馏为单步生成器，并引入无需训练的“时间窗口掩码”方法，在训练时长外稳定推理且保持内存恒定。

### 主要贡献
- 提出一个从3DGS和高帧率视频出发的物理驱动模糊合成管线，用于生成丰富多样的真实模糊训练数据。
- 设计了适配帧间模糊变化的视频扩散复原框架，并通过蒸馏实现高效单步生成。
- 开发了一种无需训练的时间窗口掩码技术，支持长视频推理且内存占用恒定。
- 在多个真实世界基准上展示了出色的感知质量、语义保真度、时间一致性，以及在下游3D重建任务中对严重运动模糊的鲁棒性提升。

### 局限性
摘要未提供足够信息。未讨论方法的计算资源需求、模型规模或对特定模糊类型（如极端低光）的适用性。

### 阅读优先级
**高**。理由：本文针对真实世界视频去模糊这一实际难题，提出了一个包含数据合成、扩散模型适配和高效率推理的完整框架，且在下游任务（3D重建）上验证了鲁棒性，对计算机视觉与神经渲染领域有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-world video deblurring remains challenging due to diverse motion patterns, complex degradations, and the scarcity of realistic training data, yet robust restoration is critical for downstream pipelines such as mobile imaging and 3D reconstruction. This work presents \textbf{RealVDeblur}, an efficient generative framework designed to improve in-the-wild robustness under diverse real capture conditions. First, a large-scale, physically grounded blur synthesis pipeline is constructed from scene-level 3D Gaussian Splatting (3DGS) assets and high-frame-rate videos, providing realistic training data covering both camera-induced and object-motion blur. Second, a video diffusion prior is leveraged for restoration; to better accommodate frame-dependent blur variations, temporal compression in the VAE is disabled and a frame-wise encoding scheme is adopted. For practical deployment on long videos, multi-step diffusion sampling is distilled into an efficient one-step generator, and a training-free Temporal Window Mask stabilizes inference beyond the training horizon with constant memory usage. Extensive experiments on diverse real-world benchmarks demonstrate strong perceptual quality, semantic fidelity, and temporal consistency on unseen videos, as well as improved robustness in downstream 3D reconstruction under severe motion blur. Project page: https://rbjin.github.io/RealVDeblur

</details>

#### 2026-07-22 - ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion

**Authors:** Cho In, Jeonghwan Cho, Mijin Yoo, Gim Hee Lee, Seon Joo Kim
**Links:** [abs](https://arxiv.org/abs/2607.20417) - [pdf](https://arxiv.org/pdf/2607.20417)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- **标题**：ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion
- **作者**：Cho In, Jeonghwan Cho, Mijin Yoo, Gim Hee Lee, Seon Joo Kim
- **出版日期**：2026-07-22
- **分类**：Neural Scene Representations & Rendering
- **链接**：https://arxiv.org/abs/2607.20417

### 一句话总结
ATSplat 提出了一种自适应令牌扩展的前馈式 3D 高斯泼溅方法，通过稀疏锚点令牌和自适应扩展机制，在保持紧凑表示的同时实现了高质量的新视角合成。

### 研究问题
现有的前馈式 3D 高斯泼溅（3DGS）方法通常将高斯体素固定到输入像素并沿射线提升，导致高斯体素的数量和位置依赖图像分辨率而非场景复杂度，产生密集且冗余的高斯集，丧失了 3DGS 优化中的自适应容量分配能力。

### 核心思路/方法
1. **稀疏锚点令牌生成**：先利用粗粒度的图像块深度和相机线索，在 3D 空间中生成稀疏的锚点令牌，形成场景的紧凑骨架。
2. **局部高斯回归**：每个令牌通过学习到的 3D 偏移量回归出局部高斯体素，使体素放置与输入图像网格解耦。
3. **自适应令牌扩展**：通过预测令牌维度的不确定性分数（由渲染误差图监督），选择性地利用可学习扩展层对高不确定性令牌进行扩展，从而在挑战区域集中更多高斯体素，同时保持整体表示紧凑。

### 主要贡献
1. 提出了一种前馈式 3DGS 框架 ATSplat，恢复了 3DGS 优化中的自适应分配能力。
2. 通过稀疏锚点令牌和自适应令牌扩展机制，将高斯体素的数量减少至密集前馈方法（如 5.7 倍）的同时，获得更优或相当的渲染质量。
3. 在 RealEstate10K 和 DL3DV 数据集上达到最先进的渲染质量，且推理速度快：12 张 512×960 输入图像，在单 GPU 上完成重建不到 1 秒，渲染 1136 FPS（512×960），仅用 311K 个高斯体素。

### 局限性
摘要未提供足够信息，无法判断该方法的局限性，例如对输入图像数量、场景动态性、光照变化的鲁棒性等。

### 阅读优先级
**高**
理由：该方法有效解决了前馈式 3DGS 中高斯体素冗余的核心问题，在保持高质量渲染的同时实现显著压缩和高速推理，对实时场景重建与渲染有重要实践价值；实验结果在多个指标上表现突出，且方法设计新颖（自适应令牌扩展），适合关注 3D 场景表示、新视角合成和高效渲染的读者。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves high-quality novel-view synthesis by optimizing freely placed primitives in 3D and adaptively densifying them in under-reconstructed regions. However, this scene-adaptive capacity allocation is largely lost in existing feed-forward 3DGS methods, which commonly regress Gaussians at input pixels and lift them along camera rays. Such pixel-aligned formulations make the number and placement of primitives depend on image resolution and input viewpoints rather than scene complexity, resulting in dense and often redundant Gaussian sets. We present ATSplat, a feed-forward 3DGS framework that restores the adaptive allocation capability of 3DGS optimization through Adaptive 3D Tokens. ATSplat first lifts coarse patch-level depth and camera cues into sparse 3D anchor tokens, forming a compact scaffold of the scene. Each token is then regressed into local Gaussians with learnable 3D offsets, decoupling primitive placement from input image grids. An Adaptive Token Expansion module predicts a token-level uncertainty score, supervised by rendering error maps, and selectively expands high-uncertainty tokens through learnable expansion layers. This sparse-to-adaptive formulation enables ATSplat to concentrate primitives in challenging regions while maintaining a compact representation. Experiments on two representative datasets, RealEstate10K and DL3DV, show that ATSplat achieves state-of-the-art rendering quality while reducing the number of Gaussians by more than $5.7\times$ compared with dense feed-forward 3DGS methods. From 12 input images at $512 \times 960$ resolution, ATSplat completes reconstruction in less than a second using a single commercial GPU, and renders high-quality novel views at 1136 FPS ($512 \times 960$) with only 311K Gaussians.

</details>

#### 2026-07-22 - MR-Compare: A Mixed-Reality Framework for Spatially Grounded Visual Comparison of 3D Gaussian Splatting and Mesh Reconstructions with the Physical Environment

**Authors:** Changrui Zhu, Ernst Kruijff, Pengju Zhang, Simon Julier
**Links:** [abs](https://arxiv.org/abs/2607.20325) - [pdf](https://arxiv.org/pdf/2607.20325)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MR-Compare: 一种用于三维高斯泼溅和网格重建与物理环境空间锚定视觉比较的混合现实框架
- 作者：Changrui Zhu, Ernst Kruijff, Pengju Zhang, Simon Julier
- 出版日期：2026年7月22日
- 分类：神经场景表示与渲染 / 具身/机器人/增强现实应用
- 链接：摘要URL：https://arxiv.org/abs/2607.20325；PDF：https://arxiv.org/pdf/2607.20325

### 一句话总结
本文提出了一个名为MR-Compare的混合现实框架，通过视频透视技术实现三维高斯泼溅和网格重建与物理环境的空间对齐视觉比较，并在两个室内房间中通过用户研究验证了其可行性。

### 研究问题
如何在混合现实中实现三维高斯泼溅（3DGS）和网格重建与真实物理环境的精确空间对齐和直观视觉对比？

### 核心思路/方法
1. 基于PC连接的Meta Quest 3头显，构建一个混合现实框架，包含一个两阶段配准流程和一个用于跨媒体比较的3D滑块。
2. 通过一个包含30名用户的探索性用户研究，在静态室内房间中评估了五种典型的桌面和移动端重建工作流，着重测量配准误差和视觉一致性。
3. 提出了一种各向异性滤波器，作为一种零样本模块，利用高斯泼溅的各向异性特性来改进3DGS在MR-Compare中的配准性能，并通过控制Replica阈值扫描发现适度修剪可提升鲁棒性并降低残差。

### 主要贡献
1. 提出了MR-Compare框架，实现了厘米级的翻译误差和较高的感知可用性、低工作负荷。
2. 系统评估显示桌面端3DGS工作流（尤其是3DGS-MCMC）在配准误差和VST参考视觉一致性上表现最佳。
3. 提出的各向异性滤波器在零样本条件下可提升3DGS配准的鲁棒性，且适度修剪能减少残差误差。

### 局限性
1. 摘要明确指出这些结果“建立了在测试场景下的系统级可行性，而非任务级有效性或独立部署”，因此缺乏对实际任务完成效果和独立使用场景的验证。
2. 评估仅在两个静态室内房间中进行，场景多样性和动态环境适应性未涉及。
3. 摘要未提供具体用户研究任务细节、错误率的定量比较，以及各向异性滤波器在不同工作流下的普适性验证。

### 阅读优先级
中  
理由：该工作在场景重建与混合现实的交叉领域提出了一个实用框架和评价方法，对从事AR/VR场景可视化或三维重建比较的研究者有参考价值。但由于摘要明确其验证限于系统可行性而非任务级效果，且缺乏对动态场景或通用性部署的讨论，对追求算法性能提升或应用落地的读者吸引力有限。

</details>

<details>
<summary>Abstract</summary>

We introduce MR-Compare, a mixed reality framework for spatially grounded visual comparison between 3D Gaussian splatting and mesh reconstructions with live video see-through (VST). Implemented on a PC-tethered Meta Quest~3, it combines a two-stage registration pipeline with a 3D Slider for cross-media comparison. We evaluated five representative desktop and mobile reconstruction workflows through a real-world benchmark with an exploratory user study ($n=30$) in two static indoor rooms. MR-Compare achieved centimetre-level translation error across all workflows. The two desktop 3DGS workflows showed the strongest overall pattern, with 3DGS-MCMC yielding the lowest registration error and strongest VST-referenced visual consistency. Room-session measures indicated high perceived usability and low workload. We further propose an anisotropy filter, a zero-shot module that leverages Gaussian anisotropies to improve 3DGS registration in MR-Compare. A controlled Replica threshold sweep shows that moderate pruning can improve robustness and reduce residual errors. These results establish system-level feasibility in the tested setting rather than task-level effectiveness or standalone deployment. The project is available at https://github.com/changruizhu96/MR-Compare.

</details>

#### 2026-07-22 - Look Before You Edit: Attention-Guided Camera Placement and Multi-View Alignment for 3D Gaussian Splatting Editing

**Authors:** Jaeyeon Park, Taeho Kang, Youngki Lee
**Links:** [abs](https://arxiv.org/abs/2607.19777) - [pdf](https://arxiv.org/pdf/2607.19777)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Look Before You Edit: Attention-Guided Camera Placement and Multi-View Alignment for 3D Gaussian Splatting Editing
- 作者：Jaeyeon Park, Taeho Kang, Youngki Lee
- 出版日期：2026-07-22
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.19777

### 一句话总结
本文提出LB-Edit框架，通过注意力引导的编辑相机放置和多视图对齐技术，解决了基于3D高斯泼溅（3DGS）的文本驱动场景编辑中编辑范围受限和多视图不一致的问题。

### 研究问题
现有文本驱动的3DGS编辑方法使用固定训练相机视角，导致编辑空间覆盖有限，且难以对复杂场景中的特定对象进行局部编辑，同时多个视角的编辑结果不一致，影响3D场景的全局一致性。

### 核心思路/方法
1. **注意力引导的编辑相机放置（ACP）**：在多个候选相机距离下探测扩散模型的自注意力和交叉注意力，找到注意力在感兴趣区域内高度集中的最优距离，然后在该距离处放置一组紧凑且几何多样的编辑相机。
2. **多视图注意力对齐（MAA）**：通过两条轴对齐多视图编辑：一是通过令牌级对应共享自注意力特征来对齐外观；二是将交叉注意力图提升到3D高斯上作为共享的3D注意力场，对齐空间位置，从而抑制外观和空间漂移。

### 主要贡献
- 提出ACP方法，能够自动选择最优编辑相机位置和距离，实现局部、紧凑的编辑。
- 提出MAA方法，通过注意力机制在多个视图间对齐编辑的外观和空间位置，提升3D一致性。
- 实验表明，该方法仅需5个编辑视图，在指令保真度、多视图一致性和编辑局部性上达到最高用户偏好，且延迟比现有方法降低最多7倍。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文针对3DGS编辑中的关键难题（局部编辑受限与多视图不一致）提出创新性框架，实验效果显著，效率提升明显，且属于神经场景表示与渲染领域的前沿工作，对相关研究和应用具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Text-driven 3D scene editing with 3D Gaussian Splatting (3DGS) typically applies a 2D diffusion editor to views rendered from fixed training cameras, limiting both the spatial coverage of edits and the user's freedom to target specific objects in complex scenes. We present LB-Edit, a framework that addresses two coupled problems: where to place editing cameras for localized edits, and how to make per-view edits agree with one another so that the 3D scene remains consistent after fine-tuning. First, Attention-Guided Editing Camera Placement (ACP) probes the diffusion model's self- and cross-attention at multiple candidate camera distances to find where attention is well-contained in the region of interest, then places a compact, geometrically diverse editing camera set at that attention-optimal distance. Second, Multi-view Attention Alignment (MAA) steers the editor toward the same edit across views along two axes: it aligns appearance by sharing self-attention features via token-level correspondence, and aligns spatial location by lifting cross-attention maps onto the 3D Gaussians as a shared 3D attention field, suppressing both appearance and spatial drift. Experiments on multi-object and single-object scenes show that our method achieves the highest user preference in instruction fidelity, multi-view consistency, and editing locality, using as few as 5 editing views and reducing latency by up to 7x over existing methods.

</details>

#### 2026-07-22 - Extending a Large View Synthesis Model for Multi-view Panoptic Segmentation

**Authors:** Kwonyoung Ryu, In-Jae Lee, Jonghyun Jin, Hyunjee Lee, Jongmin Lee, Jaesik Park
**Links:** [abs](https://arxiv.org/abs/2607.19765) - [pdf](https://arxiv.org/pdf/2607.19765)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, novel view synthesis, view synthesis, rendering, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Extending a Large View Synthesis Model for Multi-view Panoptic Segmentation
- 作者：Kwonyoung Ryu, In-Jae Lee, Jonghyun Jin, Hyunjee Lee, Jongmin Lee, Jaesik Park
- 出版日期：2026-07-22
- 分类：神经场景表示与渲染
- 链接：[摘要](https://arxiv.org/abs/2607.19765) | [PDF](https://arxiv.org/pdf/2607.19765)

### 一句话总结
本文提出首个将大规模视图合成模型扩展至3D场景理解的工作，利用冻结的视图合成模型直接将输入视图中的全景标签传播到新视角，无需3D重建或针对分割的额外训练。

### 研究问题
如何在不进行3D重建或专门训练的情况下，利用大型视图合成模型的跨视图对应能力，实现多视图全景分割？

### 核心思路/方法
1. **观察基础**：发现视图合成模型从RGB监督中学到的空间对应关系可以泛化到非真实感信号（如双编码的全景标签），使得标签传播后仍保持一致的空间结构。
2. **标签编码与传播**：将输入视图的全景标签编码为二进制通道表示，然后直接通过预训练且冻结的视图合成模型，生成目标视图的分割结果。
3. **无需额外训练**：视图合成模型不进行任何分割相关的微调或训练，仅利用其已有的跨视图注意力机制。

### 主要贡献
1. 首个将大规模视图合成模型扩展到外观渲染之外，应用于3D场景理解的工作。
2. 提出一种无需3D重建或分割训练的全景分割管线，仅依靠输入标签传播。
3. 在ScanNet上，分割质量与需要显式3D重建的高斯方法相当，且在视图合成任务上PSNR高出7 dB以上。
4. 标签传播具有跨数据集迁移能力，无需微调即可在Replica数据集上超越对比方法。

### 局限性
- 摘要未提供足够信息：未讨论方法在复杂遮挡、标签噪声或大规模场景下的性能表现。
- 摘要未提供足够信息：未提及标签编码的具体实现细节（如二进制通道的构造方式）或计算开销。
- 摘要未提供足够信息：未分析模型对输入标签准确性的依赖程度或误差传播问题。

### 阅读优先级
**高**
- **理由**：该文提出的方法创新性强——首次将视图合成模型的能力从RGB渲染扩展到语义理解，且无需3D重建或额外训练，具有潜在的实用价值。实验结果在分割精度和视图合成质量上均有显著优势，并展现了跨数据集泛化能力，适合关注神经渲染、场景理解或无监督域迁移的研究者参考。

</details>

<details>
<summary>Abstract</summary>

Large view synthesis models synthesize novel views through cross-view attention without explicit 3D representations, and recent studies have shown that they learn accurate spatial correspondence from RGB supervision alone. We observe that this correspondence generalizes beyond appearance. When non-photorealistic signals such as binary encoded panoptic labels are passed through the model, they are propagated to novel views with consistent spatial structure. These results indicate that the correspondence learned for RGB view synthesis can also propagate view-independent per-pixel labels. From this observation, we present the first work to extend large view synthesis models beyond appearance rendering to 3D scene understanding. We propose a panoptic segmentation pipeline that reuses a frozen view synthesis model to propagate panoptic labels from input views to novel views, without 3D reconstruction or any segmentation-specific training of the view synthesis model. Given panoptic labels on the input views, we encode them into binary channel representations and pass them through the same model to render target-view segmentation. On ScanNet, our method achieves segmentation quality on par with Gaussian based approaches requiring explicit 3D reconstruction, while outperforming them in novel view synthesis by more than 7 dB. The label propagation also transfers across datasets, surpassing these approaches on Replica without any fine-tuning.

</details>

#### 2026-07-22 - Fast Wave-optics Rendering of Multiplane Images for 3D Holographic Displays

**Authors:** Brian Chao, Dario Seyb, Nathan Matsuda, Oliver Cossairt, Yang Zhou, Douglas Lanman, Gordon Wetzstein, Grace Kuo, Changwon Jang
**Links:** [abs](https://arxiv.org/abs/2607.19731) - [pdf](https://arxiv.org/pdf/2607.19731)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, neural rendering, novel view synthesis, view synthesis, rendering, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fast Wave-optics Rendering of Multiplane Images for 3D Holographic Displays
- 作者：Brian Chao, Dario Seyb, Nathan Matsuda, Oliver Cossairt, Yang Zhou, Douglas Lanman, Gordon Wetzstein, Grace Kuo, Changwon Jang
- 出版日期：2026-07-22
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.19731

### 一句话总结
本文提出一种基于多平面图像（MPI）的波动光学渲染管线，用于高效合成高质量全息图，相比现有方法在速度上提升高达25万倍，同时保持可比的图像质量。

### 研究问题
如何将基于神经渲染生成的3D场景表示（如MPI）高效转换为与全息显示兼容的格式，以实现高保真、高沉浸感的3D全息显示？

### 核心思路/方法
提出一种基于多平面图像（MPI）的波动光学渲染管线，用于计算机生成全息术（CGH）。该方法利用MPI的层状结构，通过优化的波动光学计算，直接合成全息图。

### 主要贡献
- 提出一种基于MPI的全息图合成算法，在运行时间上显著超越最先进的基元类CGH算法（速度提升高达25万倍），且图像质量可比。
- 在图像质量上显著优于传统基于分层的CGH算法。
- 在多种3D场景数据集上，通过仿真和实验验证了该方法在3D焦点堆栈和4D光场重建中的出色性能，且不牺牲效率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文针对全息显示这一新兴领域提出了高效解决方案，实现了数量级的速度提升，且实验结果涵盖仿真与实物验证，方法具有实际应用潜力，适合对全息显示、神经渲染或3D重建感兴趣的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent advances in neural rendering have unlocked unprecedented capabilities in 3D reconstruction and novel view synthesis, giving rise to applications such as virtual fly-throughs of a 3D scene reconstructed from a set of sparse, casually captured images. However, these renderings are viewed on a computer screen or conventional VR headsets as 2D images, greatly limiting the perceptual realism and immersiveness of such experiences. The rapid development in novel 3D scene representations calls for dedicated rendering algorithms that convert these readily-available 3D contents into formats that are compatible with emerging 3D display technologies, such as holographic displays. In this paper, we propose a wave-optics rendering pipeline that works with multiplane images (MPIs) for efficient and high-quality hologram synthesis. Our MPI-based computer-generated holography algorithm greatly outperforms state-of-the-art primitive-based CGH algorithms in terms of runtime, achieving speedups up to 250,000x while achieving comparable image quality, and significantly outperforms conventional layer-based CGH algorithms in terms of image quality. We validate our method extensively on a wide variety of 3D scene datasets both in simulation and through experimentally captured results, showing exceptional 3D focal stack and 4D light field reconstruction performance without sacrificing efficiency.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

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

#### 2026-07-23 - HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors

**Authors:** Siyu Li, Kunyu Peng, Di Wen, Beiping Hou, Zhiyong Li, Kailun Yang
**Links:** [abs](https://arxiv.org/abs/2607.21281) - [pdf](https://arxiv.org/pdf/2607.21281)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors
- 作者：Siyu Li, Kunyu Peng, Di Wen, Beiping Hou, Zhiyong Li, Kailun Yang
- 出版日期：2026-07-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.21281

### 一句话总结
本文提出HGeo-TopoMap方法，通过显式先验地图与隐式空间关系分层提升自动驾驶拓扑地图构建的精度与鲁棒性，尤其解决了中心线检测难题。

### 研究问题
拓扑地图需要检测中心线等实例及其连接关系，但由于真实环境中中心线缺乏明确标注，中心线实例的检测仍是一个重大挑战。

### 核心思路/方法
1. **几何自适应学习模块**：针对逆透视变换得到的道路结构图，离散编码语义和空间特征，并用先验掩码注意力机制聚焦信息区域。
2. **几何一致性学习模块**：利用中心线的几何特性与空间关系，在几何感知解码器中通过对齐具有相同几何朝向的中心线特征来强制空间一致性。

### 主要贡献
1. 提出HGeo-TopoMap，使用显式先验地图与隐式空间关系分层提升拓扑地图构建。
2. 设计几何自适应学习与几何一致性学习两个模块，分别处理道路结构图与中心线空间一致性。
3. 在OpenLane-V2数据集上，方法在中心线、车道段及鲁棒性基准测试中均显著提升拓扑地图准确性，并在标准与挑战条件下稳定优于基线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中等**。理由：该方法聚焦于自动驾驶拓扑地图构建中中心线检测的具体痛点，属于计算机视觉与机器人领域的专项技术。如果研究方向涉及拓扑映射、鲁棒性感知或自动驾驶感知系统，则具有较高参考价值；否则对通用视觉任务研究者而言优先级一般。

</details>

<details>
<summary>Abstract</summary>

Topological maps are key outputs of autonomous driving perception systems, delivering essential road information for path planning. They identify instances such as centerlines and traffic signs, along with their connectivity relationships. Due to the lack of explicit markings for centerlines in real-world environments, the detection of centerline instances remains a significant challenge. To tackle this problem, we propose HGeo-TopoMap, which leverages an explicit prior map and implicit spatial relations to hierarchically boost topological mapping. First, a geometric adaptive learning module is designed for the road structure map obtained via inverse perspective mapping. This module discretely encodes semantic and spatial features from the map, followed by a prior-mask attention mechanism that selectively focuses on informative regions. Then, a geometric consistency learning module is devised, which leverages the geometric properties and spatial relationships of centerlines. Built on the geometry-aware decoder, it enforces spatial consistency by aligning features of centerline instances with identical geometric orientations. The proposed method is evaluated on the OpenLane-V2 dataset across the centerline, lane segment, and robustness benchmarks. Beyond substantial improvements in topological mapping accuracy, the proposed method offers the benefit of enhanced robustness, consistently outperforming baselines under both standard and challenging conditions. The source code and model weights will be made publicly available at https://github.com/lynn-yu/HGeo-TopoMap.

</details>

#### 2026-07-23 - A Real-Time Generalized Nash Equilibrium Framework for Interaction-Aware Autonomous Driving in Mixed Traffic

**Authors:** Nouhed Naidja, Mohamed-Cherif Rahal, Steve Pechberti, Stéphane Font, Guillaume Sandou, Marc Revilloud
**Links:** [abs](https://arxiv.org/abs/2607.21043) - [pdf](https://arxiv.org/pdf/2607.21043)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Real-Time Generalized Nash Equilibrium Framework for Interaction-Aware Autonomous Driving in Mixed Traffic
- 作者：Nouhed Naidja, Mohamed-Cherif Rahal, Steve Pechberti, Stéphane Font, Guillaume Sandou, Marc Revilloud
- 出版日期：2026-07-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.21043

### 一句话总结
本文提出了一个基于广义纳什均衡问题的实时决策框架，用于混合交通中自动驾驶汽车与人驾驶车辆的交互，并在真实测试轨道上验证了其有效性。

### 研究问题
如何在混合交通环境中，通过显式建模自动驾驶车辆与人驾驶车辆之间的共享约束（安全性、几何约束），实现实时、安全且自然的交互决策。

### 核心思路/方法
将驾驶交互形式化为一个广义纳什均衡问题（GNEP），以此显式建模自动驾驶策略与对手动作之间的动态可行性关联；为解决该非凸问题的实时性，采用基于粒子群优化（PSO）的专用求解器。

### 主要贡献
1. 提出了一个将驾驶交互建模为GNEP的决策框架，与解耦优化方法不同，该框架显式考虑了共享安全与几何约束。
2. 设计了一个基于PSO的实时求解器，在真实测试中实现了低于50毫秒的收敛时间。
3. 使用真实的雷诺Zoé自动驾驶车辆与人类驾驶员在测试轨道上进行了实验验证，表明系统能生成舒适、类人的轨迹。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由是：该工作聚焦于自动驾驶中交互决策的具体技术路线（GNEP+PSO），并在真实车辆上验证了实时性能，对从事运动规划与交互建模的研究者有参考价值；但摘要未提供与现有方法的定量对比或失败案例，创新性程度需结合全文评估，因此优先级为中等。

</details>

<details>
<summary>Abstract</summary>

Safe and efficient navigation in mixed-traffic environments remains a critical challenge for Autonomous Vehicles (AVs), primarily due to the complex interdependence between the AV's decisions and the unpredictable reactions of human drivers. This paper introduces a comprehensive decision-making framework that formulates the driving interaction as a Generalized Nash Equilibrium Problem (GNEP). Unlike decoupled optimization approaches, this framework explicitly models shared safety and geometric constraints, ensuring that the feasibility of the AV's strategy is dynamically linked to the opponent's actions. To solve this non-convex problem in real-time, we propose a dedicated solver based on Particle Swarm Optimization (PSO). The complete architecture was validated on a test track using a real autonomous Renault Zoé interacting with a human driver. Experimental results demonstrate the system's ability to handle critical scenarios by generating comfortable, human-like trajectories. Benchmarks confirm the solver's operational feasibility, achieving convergence in under 50 ms.

</details>

#### 2026-07-23 - TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation

**Authors:** Boyuan Wang, Yue Zhang, Xutao Xue, Xueyu Song, Yu Sun
**Links:** [abs](https://arxiv.org/abs/2607.21017) - [pdf](https://arxiv.org/pdf/2607.21017)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation
- 作者：Boyuan Wang, Yue Zhang, Xutao Xue, Xueyu Song, Yu Sun
- 出版日期：2026-07-23
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.21017；PDF: https://arxiv.org/pdf/2607.21017

### 一句话总结
本文提出TableVerse，一个全自动的Real2Sim pipeline，通过从非结构化互联网图像中确定性重建物理可信的桌面场景，构建了包含10万个独特环境与交互轨迹的大规模数据集TableVerse-100K，旨在推动通用机器人操作策略的研究。

### 研究问题
如何克服现有自动化数据合成方法生成的场景数据物理不真实、难以反映真实环境复杂杂乱布局的问题，从而为通用机器人操作提供大规模、高保真的数据基础。

### 核心思路/方法
- 提出全自动的**Real2Sim pipeline**：从现实生活图像数据（如互联网媒体）中确定性地重建桌面环境，而非依赖文本生成或程序化生成的“想象布局”。
- 该pipeline能够输出具有**精确度量尺度、真实拓扑结构和已验证机械稳定性**的高保真仿真环境。
- 集成**自动化任务条件轨迹生成框架**，为每个环境合成高质量、无碰撞的抓取与放置演示轨迹。
- 利用该流程构建**TableVerse-100K**数据集：包含10万个物理一致的独特环境及对应的交互轨迹。

### 主要贡献
- 提出将范式从“想象布局生成”转向“从非结构化图像数据中确定性重建”的TableVerse自动化流程。
- 构建了大规模、高保真的TableVerse-100K数据集，包含10万个物理一致的环境与交互演示，具有真实的资产组成和空间分布。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对通用机器人操作中数据规模与保真度不足的核心瓶颈，提出了一种新颖的确定性重建范式，并提供了大规模公开数据集（10万环境），对Embodied AI和机器人学习领域具有显著价值。

</details>

<details>
<summary>Abstract</summary>

The development of generalizable robotic manipulation policies is inherently bounded by the availability of large-scale, high-fidelity scene data. While recent automated synthesis methods attempt to bridge this gap via text-to-layout hallucination or simplified procedural generation, they frequently suffer from physical implausibility and fail to capture the complex, dense clutter of actual human environments. In this paper, we introduce TableVerse, a fully automated Real2Sim pipeline that shifts the paradigm from imaginative layout generation to deterministic reconstruction from unstructured, in-the-wild image data. Our framework seamlessly processes unscripted internet media into high-fidelity, simulation-ready tabletop environments with accurate metric scales, authentic topologies, and verified mechanical stability. Furthermore, an automated task-conditioned trajectory generation framework is integrated to synthesize high-quality, collision-free pick-and-place demonstrations. Leveraging this complete pipeline, we construct the TableVerse-100K Dataset, a large-scale corpus comprising 100,000 unique, physically consistent environments paired with interactive manipulation trajectories. By capturing diverse asset compositions, realistic spatial distributions, and high-quality demonstrations, TableVerse-100K establishes a highly scalable and high-fidelity data foundation, providing significant value to facilitate future research in generalizable robotic manipulation tasks.

</details>

#### 2026-07-22 - PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving

**Authors:** Yushan Liu, Tianxiong Lv, Bohua Wang, Hangqi Fan, Chenxu Zhao, He Zheng, Xuchang Zhong, Yifan Xie, Congyang Zhao, Zhihao Liao, Leigang Luo, Yang Cai, Xiao-Ping Zhang, Wenbo Ding
**Links:** [abs](https://arxiv.org/abs/2607.20175) - [pdf](https://arxiv.org/pdf/2607.20175)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving
- 作者：Yushan Liu, Tianxiong Lv, Bohua Wang, Hangqi Fan, Chenxu Zhao, He Zheng, Xuchang Zhong, Yifan Xie, Congyang Zhao, Zhihao Liao, Leigang Luo, Yang Cai, Xiao-Ping Zhang, Wenbo Ding
- 出版日期：2026-07-22T14:09:15Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.20175

### 一句话总结
PerceptDrive提出了一种自适应专家路由的感知先验世界-动作建模框架，在不使用测试时候选选择的情况下，仅依赖单目前视相机，实现了端到端自动驾驶的规划性能提升。

### 研究问题
如何将冻结的感知基础模型编码的丰富先验知识（几何、语义、动态）有效地转化为规划动作，解决窄条件化接口导致的任务相关线索衰减以及静态融合无法适应不同场景专家贡献的问题。

### 核心思路/方法
1. **感知先验世界-动作建模框架**：将来自冻结、驾驶自适应提供者的教师蒸馏先验，与来自冻结自监督视频编码器的密集观测潜变量，输入到可训练的专家路由世界-动作模型中。
2. **自适应专家路由**：利用专家特定查询分支处理信号，并通过先验保留目标将每个分支锚定到其先验。一个路由器从共享场景表示中预测软门控，组合专家条件后再进行轨迹生成。
3. **训练与推理**：训练时，使用特权规则驱动的子度量估计为分支特定轨迹草稿提供软门控蒸馏目标；推理时，移除特权组件，仅用单目前视相机生成单条轨迹，无测试时评分或重排序。

### 主要贡献
- 提出了PerceptDrive框架，将感知先验知识以自适应专家路由方式融入世界-动作建模，改善了端到端规划。
- 在NAVSIM v1和v2上实现了先进性能（PDMS 90.4 / EPDMS 90.2），无需测试时候选选择。
- 消融实验证实先验保留和场景条件化路由的互补增益，以及三个先验的差异化依赖。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：论文在主流自动驾驶基准（NAVSIM）上取得领先性能，且方法新颖（自适应专家路由与先验保留），对端到端规划领域的隐私感知和动作生成有直接参考价值。出版日期为2026年，属于较新研究，适合关注前沿方法的读者。

</details>

<details>
<summary>Abstract</summary>

Frozen perception foundation models encode rich geometric, semantic, and dynamic knowledge. Yet narrow conditioning interfaces may attenuate task-relevant cues, while static fusion cannot adjust expert contributions to each scene. We cast this challenge as the prior-to-plan transfer problem and introduce PerceptDrive, a perception prior world-action modeling framework with adaptive expert routing. PerceptDrive feeds teacher-distilled priors from a frozen, driving-adapted provider and dense observation latents from a frozen self-supervised video encoder into a trainable expert-routed world-action model. Expert-specific query branches process these signals, while a prior-retention objective anchors each branch to its prior. A router predicts soft gates from a shared scene representation and combines the expert conditions before trajectory generation. During training, privileged rule-based sub-metric estimates for branch-specific trajectory drafts provide soft-gate distillation targets. The predicted action-free future latent conditions a flow-matching actor. At inference, privileged components are absent; with one front-facing camera, PerceptDrive generates one trajectory per planning step without test-time scoring, reranking, or search. Experiments show that PerceptDrive achieves state-of-the-art performance with 90.4 PDMS on NAVSIM v1 and 90.2 EPDMS on NAVSIM v2, outperforming existing methods. Ablations confirm complementary gains from prior retention and scene-conditioned routing, alongside differential reliance on the three priors. These results demonstrate that preserving and adaptively routing perception priors improves direct planning without test-time candidate selection.

</details>

#### 2026-07-22 - KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding

**Authors:** Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai, Xuelong Li
**Links:** [abs](https://arxiv.org/abs/2607.19876) - [pdf](https://arxiv.org/pdf/2607.19876)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding
- 作者：Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai, Xuelong Li
- 出版日期：2026-07-22
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2607.19876) | [PDF](https://arxiv.org/pdf/2607.19876)

### 一句话总结
本文提出KineBench，一种不依赖逆动力学模型（IDM-free）的闭环基准测试，通过显式运动学接地直接提取6D末端执行器姿态，用于评估具身世界模型的物理一致性。

### 研究问题
现有评估具身世界模型物理一致性的闭环方法严重依赖逆动力学模型（IDM），但IDM在像素-运动学映射中存在分布外脆弱性，导致无法区分世界模型误差与提取器误差。如何减少这种归因模糊性？

### 核心思路/方法
提出KineBench，其核心是显式运动学接地管道：对生成视频逐帧使用级联视觉基础模型直接提取6D末端执行器姿态，随后在物理模拟器中执行以进行闭环验证。它还引入两个经典3D运动学指标（频谱弧长SPARC和Maruyama可操作性指数）以描述轨迹平滑度和运动学可行性，并基于ManiSkill3中的20个多样化操作任务构建四个递进评估套件（基础执行、任务迁移、视觉分布外泛化、复杂度条件缩放）。

### 主要贡献
1. 提出IDM-free闭环基准KineBench，消除IDM引入的归因模糊性。
2. 采用显式运动学接地管道，结合级联视觉基础模型和物理模拟器验证。
3. 引入机器人视角的运动学指标（SPARC、可操作性指数）用于更精细的评估。
4. 通过前沿模型评估揭示了具身视频生成中任务复杂度界定的非线性缩放行为，为数据扩展策略提供经验指导。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作专注于具身世界模型的评估基准构建，对设计可验证的物理一致性评估方法有方法论贡献。但如果读者当前不涉及具身世界模型、运动学接地或仿真评估框架，则优先度较低。摘要显示了清晰的方法论创新和实证发现，但未提供具体性能对比或失败案例，因此优先级中等。

</details>

<details>
<summary>Abstract</summary>

Evaluating the physical consistency of embodied world models(EWMs) is a critical open challenge. While closed-loop evaluation via simulator rollouts offers a more faithful assessment of physical plausibility than open-loop alternatives, existing frameworks almost exclusively rely on Inverse Dynamics Models(IDMs) for action extraction. Due to the intricate mapping from 2D pixel space to 3D kinematic space, the learned IDMs can be brittle to data outside their training distribution, resulting in unreliable action extraction from the generated videos with novel objects and scenarios. This creates an unavoidable attribution ambiguity between world model inaccuracies and extractor errors. To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for EWMs, built upon an explicit kinematic grounding pipeline. Given a generated video, KineBench employs cascaded visual foundation models to directly extract 6D end-effector poses from individual frames, which are then executed in a physics simulator for closed-loop validation. Beyond execution-based task success, KineBench incorporates two classical 3D kinematic metrics--Spectral Arc Length (SPARC) and the Maruyama Manipulability Index--to characterize trajectory smoothness and kinematic feasibility from a robot-centric perspective. Built on 20 diverse manipulation tasks in ManiSkill3, KineBench evaluates EWMs across four progressive suites: basic execution, task transfer, visual out-of-distribution generalization, and complexity-conditioned scaling. Evaluation across frontier models reveals task-complexity-bounded nonlinear scaling in embodied video generation, providing empirical guidance for future data-scaling strategies.

</details>

#### 2026-07-22 - SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving

**Authors:** Jiangfan Liu, Zexuan Cui, Tianyuan Zhang, Zonglei Jing, Zonghao Ying, Yaoyuan Zhang, Jiakai Wang, Xiaoqi Jiang, Aishan Liu, Xianglong Liu
**Links:** [abs](https://arxiv.org/abs/2607.19701) - [pdf](https://arxiv.org/pdf/2607.19701)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving
- 作者：Jiangfan Liu, Zexuan Cui, Tianyuan Zhang, Zonglei Jing, Zonghao Ying, Yaoyuan Zhang, Jiakai Wang, Xiaoqi Jiang, Aishan Liu, Xianglong Liu
- 出版日期：2026-07-22
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.19701，PDF: https://arxiv.org/pdf/2607.19701

### 一句话总结
SafeGen提出了一种基于目标条件的视频扩散框架，用于生成安全关键场景（如危险的人车交互），以测试和提升基于视觉语言模型（VLM）的自动驾驶系统的安全性。

### 研究问题
如何生成真实、多样且具有不可预见性的人-车交互安全关键场景，以有效评估基于VLM的自动驾驶系统（VLMAD）的安全性，并克服现有基于模拟器方法存在的“模拟到现实”差距（sim-to-real gap）。

### 核心思路/方法
- 核心公式：将场景生成建模为**目标条件扩散过程（goal-conditioned diffusion process）**——预设的灾难性最终状态（catastrophic end-state）作为强监督信号，引导生成时间上连贯的视频轨迹，使其自然演化到安全关键结局。
- 两步流程：
  1. **Context Grounded End State Reasoning**：利用VLM分析正常的驾驶上下文，推断人-车交互中的潜在脆弱性，生成结构化的最终状态规格（end-state specifications），从而诱发高风险场景。
  2. **End State Conditioned Video Evolution**：将语义威胁落地为物理上合理的视觉动态。具体包括：通过深度感知几何投影（depth-aware geometric projection）在场景中实例化高风险代理，再通过边界条件扩散（boundary-conditioned diffusion）生成中间帧，确保运动模式一致和时间连贯性。

### 主要贡献
- 提出了SafeGen框架，将安全关键场景生成转化为目标条件扩散过程，克服了模拟器方法的局限性。
- 引入了“Context Grounded End State Reasoning”，利用VLM自动从良性驾驶上下文中推断出潜在风险，生成结构化目标。
- 设计了“End State Conditioned Video Evolution”机制，将语义威胁转化为符合物理规律的视觉动态。
- 实验表明，在3个VLMAD上，SafeGen将评估VLMAD理解与决策的“Judge Overall Score”平均提升24.25%（对比当前最优方法），且基于其生成的场景微调VLMAD后，在真实驾驶场景中的性能平均提升15.9%。

### 局限性
摘要未提供足够信息来讨论该方法的局限性，例如计算成本、对VLM推理的依赖程度、生成场景的多样性边界或在不同天气/光照条件下的鲁棒性等。

### 阅读优先级
**高**。理由：该工作针对自动驾驶安全评估这一核心难题，提出了一种基于扩散模型的新颖框架，直接解决了模拟器方法的关键弱点（sim-to-real gap）。实验指标提升显著（24.25%和15.9%），且方法结合了VLM推理与视频生成，体现了前沿技术融合趋势，对于从事自动驾驶安全、VLM评估或视频生成的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

VLMs are increasingly deployed in AD systems, creating an urgent need for rigorous safety evaluation under rare yet safety-critical scenarios. Among these, interactions with vulnerable road users represent a major source of real-world failures. However, existing safety-critical scenario generation methods predominantly rely on simulator-based pipelines, which suffer from a substantial sim-to-real gap and often fail to capture realistic, diverse, and unforeseen human-vehicle interaction dynamics. We present SafeGen, a goal-conditioned diffusion framework for safety-critical scenario generation in VLMADs. Our key insight is to formulate scenario generation as a goal-conditioned diffusion process, where a predefined catastrophic end-state serves as a strong supervisory signal, guiding the generation of temporally coherent video trajectories that naturally evolve toward safety-critical outcomes. Building on this formulation, we introduce Context Grounded End State Reasoning, which leverages VLMs to analyze benign driving contexts and infer latent vulnerabilities in human-vehicle interactions, producing structured end-state specifications that induce high-risk scenarios. Conditioned on these targets, we further propose End State Conditioned Video Evolution, which grounds semantic threats into physically plausible visual dynamics. Specifically, we instantiate high-risk agents within the scene via depth-aware geometric projection, followed by boundary-conditioned diffusion to generate intermediate frames with consistent motion patterns and temporal coherence. Extensive experiments across 3 VLMADs demonstrate that SafeGen increases the Judge Overall Score, a metric using a VLM judge to evaluate VLMADs' understanding and decision-making, by 24.25% on average compared to SoTA baselines. Furthermore, fine-tuning a VLMAD improves performance in real-world driving scenes by an average of 15.9%.

</details>

#### 2026-07-21 - LowPowAR: Power-Constrained Tone Mapping for Augmented Reality

**Authors:** Weikai Lin, Sheng Zhao, Ian Ross, Carl Marshall, Sushant Kondguli, Yuhao Zhu
**Links:** [abs](https://arxiv.org/abs/2607.19509) - [pdf](https://arxiv.org/pdf/2607.19509)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LowPowAR: Power-Constrained Tone Mapping for Augmented Reality
- 作者：Weikai Lin, Sheng Zhao, Ian Ross, Carl Marshall, Sushant Kondguli, Yuhao Zhu
- 出版日期：2026-07-21T18:48:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2607.19509，PDF https://arxiv.org/pdf/2607.19509

### 一句话总结
本文提出一种受功率约束的色调映射框架，将增强现实眼镜的显示功耗优化问题转化为在给定功率预算下最大化感知质量的色调映射问题，并通过学习的方法实现实时部署。

### 研究问题
如何在全天候穿戴式增强现实眼镜的严格功率限制下，优化显示功耗以在有限功耗预算内最大化视觉感知质量。

### 核心思路/方法
将显示功率优化形式化为功率约束的色调映射问题，提出一种基于人类视觉感知的学习框架。具体包括：设计一种优化友好的色调映射算子参数化方法，并采用渐进式优化策略来权衡质量与功耗；将迭代优化过程蒸馏为一个轻量级的前馈神经网络，以实现实时推理。

### 主要贡献
1. 将AR显示功耗优化重新定义为功率约束的色调映射问题。
2. 提出一种基于人类视觉、可学习的框架，在给定功耗预算下最大化感知质量。
3. 引入优化友好的色调映射参数化方案和渐进式优化策略。
4. 通过蒸馏迭代优化为轻量级神经网络实现实时部署。
5. 主观实验表明在同等功耗预算下，该方法比先前工作具有更好的感知质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工作聚焦于AR显示功耗优化的具体技术问题，方法新颖且具有实际部署潜力。但摘要中未提供明确的数值对比或详细实验设置，对于追求技术深度细节的读者可能需要查阅全文。对于从事AR硬件优化或低功耗视觉计算的从业者而言具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Everyday-wearable Augmented Reality (AR) glasses must meet strict power limits, making displays a key target for optimization. We cast display power optimization as a power-constrained tone-mapping problem and propose a human-vision-grounded, learning-based framework that maximizes perceptual quality under a given power budget. We introduce an optimization-friendly tone-mapping operator (TMO) parameterization along with a progressive optimization strategy to effectively navigate the quality-vs-power landscape. We distill the iterative optimization into a lightweight feed-forward neural network for real-time deployment. Subjective experiments show that our method yields better perceptual quality than prior work at the same power budget. Project page: https://horizon-lab.org/lowpowar/.

</details>

#### 2026-07-21 - Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents

**Authors:** Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen
**Links:** [abs](https://arxiv.org/abs/2607.19190) - [pdf](https://arxiv.org/pdf/2607.19190)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents
- 作者：Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen
- 出版日期：2026-07-21
- 分类：具身/机器人/AR应用
- 链接：https://arxiv.org/abs/2607.19190

### 一句话总结
该工作提出一个基于视觉-语言智能体的框架，能将真实世界的物体-机器人交互记录自动转换为可运行的物理仿真场景（即“数字孪生”），在多个领域实现统一且低成本的现实到仿真转换。

### 研究问题
如何将真实世界中的物体-机器人交互过程，自动转化为可直接用于物理仿真运行的“数字孪生”场景，并克服现有流程依赖手动调参、网格清理、坐标系对齐等繁琐步骤的局限。

### 核心思路/方法
提出**Agentic Real2Sim**框架，利用视觉-语言智能体（VLM）驱动决策，自动完成真实场景的几何重建、物体状态恢复、物理参数推断，并组装参与者（机器人）、物体、相机、位姿和运动轨迹，形成可运行的物理仿真孪生体。智能体决策可由开源VLM后端驱动，成本仅为前沿模型的零头。

### 主要贡献
1. 提出首个统一框架，可处理刚体操作、可变形物体交互和类人运动场景的Real2Sim转换（传统上这些场景需不同管道）。
2. 框架由视觉-语言智能体自动完成繁琐的工程步骤，无需人工干预。
3. 证明智能体决策可使用低成本开源VLM后端，仍能达到与前沿模型相当的成功率。
4. 生成的仿真孪生体与真实世界对齐，可用于下游机器人策略学习与评估。

### 局限性
摘要未提供关于实验失败案例、场景复杂性上限、物理精度量化对比、计算资源消耗等具体局限性的信息。摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作瞄准机器人仿真中关键且困难的“真实到仿真”自动转换问题，提出的多场景统一框架具有实用潜力，且采用低成本VLM的方案降低了门槛。对于从事具身智能、机器人策略迁移或物理仿真研究的读者，有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-to-sim conversion for robotic interaction with objects remains labor-intensive because it requires more than visual reconstruction: a streamlined real2sim process must recover scene geometries and object states, infer physical parameters, and assemble actors, objects, cameras, poses, and trajectories into a runnable physical simulation. Today this process still depends on manual tuning of visual foundation models, mesh cleanup, coordinate-frame alignment, and brittle workflow glue across visual perception tools and simulators. We introduce \textit{Agentic Real2Sim}, a framework for generalized physical world modeling with vision-language agents, converting a real-world recording of object-robot interaction into a simulatable episodic twin which preserves observations, geometries, robot interactions, and object states. We evaluate Agentic Real2Sim on rigid-object manipulation, deformable-object interaction, and humanoid motion scenes, spanning domains that are usually handled by separate Real2Sim pipelines, marking a first step toward scalable conversion. The framework's agentic decisions can be driven by an open-weight VLM backend at a small fraction of the cost of frontier models, while attaining comparable conversion success rate. We aim to use the resulting real-world-aligned twins for downstream robotics tasks, specifically policy learning and evaluation. The project site is available at https://agentic-real2sim.github.io/.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
