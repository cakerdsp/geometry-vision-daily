# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：44
- 分类分布：
  - Neural Scene Representations & Rendering: 14
  - Embodied / Robotics / AR Applications: 13
  - 3D Reconstruction & Multi-view Geometry: 12
  - Dynamic / 4D Reconstruction: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，根据您提供的今日论文列表，以下是针对计算机视觉和三维重建领域的科研趋势综合分析。

#### 今日主要趋势

1.  **物理与动力学知识深度融入神经场景表示**：一个非常显著的趋势是将物理仿真（刚体动力学、重力）、人类运动动力学等先验知识嵌入到3D/4D重建和世界模型的训练与推理过程中。不再是简单的后处理修正，而是作为“物理在环”的诊断器（如SimuScene）或可微物理层（如PersistGS），以及在惯导里程计中引入人体运动学先验（如MARIO）。这表明领域正从追求视觉保真度转向追求物理与几何的联合一致性。

2.  **从离线重建迈向在线、流式、交互式“世界模型”**：研究重心正从对静态/离散场景的离线重建，转向对动态、流式输入的在线处理，并服务于具身决策。GN0和OmniDreams代表了构建统一“数据-仿真-学习”闭环的宏大叙事；FreeStreamGS则聚焦于具体的在线前馈3DGS技术。这类工作致力于让模型像智能体一样实时感知和理解不断变化的动态环境。

3.  **为实时性与部署效率对3D高斯泼溅（3DGS）进行系统化压缩与加速**：3DGS虽好，但高昂的存储和计算成本成为其实际部署的瓶颈。SparseStreet针对街景场景提出高达80%的压缩率，而BA-T则通过精巧的迭代设计，显著降低了解码器参数。同时，PixVOD从硬件层面提出了分布式的像素级计算范式。这反映了3DGS从“能做”到“高效实用”的转变，是走向机器人、自动驾驶等实时应用的关键一步。

4.  **推动3D场景从“感知”走向“可编辑与交互”**：单纯的重建已不能满足需求，对重建结果的语义理解和可控编辑成为热点。MLP Splatting和TASE都致力于实现物体级别的场景分解和可控编辑。前者通过物体中心神经基元实现自然分解，后者通过截断感知的嵌入空间实现文本驱动的灵活编辑。这标志着3D场景表示正从静态地图演变为可交互、可操作的智能资产。

5.  **多模态与空间智能基准的精细化与挑战性提升**：随着多模态大模型（MLLM）和具身智能的发展，对模型空间推理能力的评估需求日益迫切。OVO-S-Bench构建了专注于流式空间智能的层次化基准，揭示了当前最佳模型与人类专家之间的巨大差距（27分）。同时，3DGS的安全性（如Poison-3DGS）和非结构化场景（如UnsOcc）等特定挑战也开始被系统化地研究和评估，体现了研究的成熟度提升。

#### 技术路线观察

| 技术方向 | 论文代表 | 侧重点比较 |
| :--- | :--- | :--- |
| **几何基础模型** | SAMatcher, BA-T, PixVOD, Multi-Robot Bearing-only | 本方向热衷于“更鲁棒”和“更特殊”的几何求解。SAMatcher利用基础模型（SAM）进行显式的共可见性建模，提升特征匹配鲁棒性；BA-T试图用轻量级Transformer模拟经典BA算法，注重参数效率；PixVOD和Multi-Robot Bearing-only则探索了极端场景下的分布式计算与弱拓扑条件几何求解，更具理论前沿性。 |
| **3D/4D 重建** | SimuScene, PersistGS, FreeStreamGS | 本方向的核心挑战是“动态”与“遮挡”。SimuScene解决单图静态场景的物理稳定性；PersistGS应对4D动态场景中的物体完全遮挡问题；FreeStreamGS则处理流式动态输入的无序性问题。三者技术路线不同：物理仿真、可微动力学、在线前馈，但都瞄准了传统方法在动态/复杂条件下的失效点。 |
| **神经场景表示与渲染** | SparseStreet, MLP Splatting, KC-3DGS | 本方向在3DGS框架下并行探索三大优化方向：**效率**（SparseStreet剪枝压缩）、**表达能力**（MLP Splatting用MLP基元替代高斯基元以支持场景分解）、**感知质量**（KC-3DGS引入小波域统计约束提升视觉感知保真度）。这构成了一个完整的“高效-灵活-高质量”三角，显示出3DGS生态的日益成熟。 |
| **机器人/AR 应用与世界模型** | GN0, OmniDreams, GeoSem-WAM, MARIO, UnsOcc, OVO-S-Bench | 本方向最活跃，体现了从“视觉感知”到“具身决策”的明确转向。世界模型成为核心叙事：OmniDreams擅长生成极端场景，GeoSem-WAM强调结构化潜在表征，前者是生成式，后者是辅助监督式。GN0则提供了一个包含数据、仿真、基准、算法的完整生态闭环。MARIO和UnsOcc分别聚焦于AR人体跟踪与自动驾驶无名场景的具体难题，而OVO-S-Bench则为此类应用提供精准的测试工具。 |

#### 值得优先阅读的论文

1.  **PersistGS（arXiv 2606.03479）**：优先阅读。该文创造性地将**可微刚体物理**与流行的**4D高斯泼溅**结合，解决了动态场景中物体被遮挡后的“物体恒存性”这一根本性问题。其“物理先验补偿视觉缺失”的思路，是未来动态场景理解的重要方向。

2.  **SimuScene（arXiv 2606.03994）**：优先阅读。其提出的“物理在环（Physics-in-the-Loop）”思想颠覆了以往将物理作为后处理的惯例，将物理引擎作为生成过程中的诊断工具。这种将物理约束从“修正”提升为“指导”的范式，对构建仿真就绪的数字孪生具有普适意义。

3.  **BA-T（arXiv 2606.03287）**：优先阅读。该文用简洁的迭代Transformer结构模拟了束调整（BA）这一传统几何优化过程，并以极少的参数达到了顶尖的精度。它展示了**融合经典几何理论与现代深度学习**的简洁而强大的力量，对设计高效3D重建网络极具启发。

4.  **GN0（arXiv 2606.03682）**：建议阅读。该文并非单一算法创新，而是一个庞大的统一框架（数据生成-高保真仿真-强化学习基础模型），代表了视觉语言导航领域从“算法竞赛”向“系统构建”的宏大趋势。理解其整体架构，有助于把握领域发展的前沿方向。

5.  **KC-3DGS（arXiv 2606.03120）**：建议阅读。该文直击3DGS在自然图像统计上的软肋，通过引入小波域的自然图像先验（峰度约束等）来提升感知质量。其理论分析（像素损失存在小波域不可区分扰动）具有启发性，代表了从“像素对齐”走向“感知对齐”的精细化优化方向。

#### 可能的研究机会

1.  **“物理+视觉”联合优化框架**：将SimuScene的“物理在环”与PersistGS的“可微物理”思想结合，建立一个统一的、可微的多物体动态场景物理-视觉联合优化管线，可能是4D重建领域的下一个突破点。

2.  **3DGS的隐私与安全性研究**：Poison-3DGS开启了3DGS安全领域的大门。可以借鉴传统图像/视频中的投毒和对抗攻击与防御方法，针对3DGS独特的可微渲染管线、高斯参数空间等特性，设计更隐蔽的攻击和更强的防御机制。

3.  **面向具身智能的在线、交互式3DGS世界模型**：FreeStreamGS展示了在线GS的可能性，GN0和OmniDreams展示了世界模型的巨大潜力。将两者结合，构建一个**基于在线3DGS的、可交互的、用于策略学习的世界模型**，是一个非常有前景的空缺。例如，在FreeStreamGS的流式GS之上，加入动作条件预测能力。

4.  **几何与语义先验辅助的3D场景编辑**：TASE和MLP Splatting都展示了场景编辑能力，但编辑的物理合理性（如移除支撑物后物体应

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-03T01:30:19-04:00
**Total number of papers:** 44
**Number of papers added in the latest update:** 44
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

No papers in the current README window.

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-02 - PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting

**Authors:** Adrian Ramlal, John S. Zelek
**Links:** [abs](https://arxiv.org/abs/2606.03479) - [pdf](https://arxiv.org/pdf/2606.03479)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, 4D Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting
- 作者：Adrian Ramlal, John S. Zelek
- 出版日期：2026-06-02
- 分类：Dynamic / 4D Reconstruction（主要），Neural Scene Representations & Rendering（次要）
- 链接：摘要页 https://arxiv.org/abs/2606.03479 | PDF https://arxiv.org/pdf/2606.03479

### 一句话总结
PersistGS 通过将可微刚体动力学仿真与3D高斯泼溅相结合，在物体完全被遮挡期间恢复其持久性，从而提升动态场景重建的物理保真度。

### 研究问题
动态3D高斯泼溅方法在运动物体被多相机视频完全遮挡时，物体对应的3D高斯失去光度监督梯度信号，导致高斯退化，无法正确重建物体的动态行为。如何在没有视觉信号的遮挡期间，保持物体的持久性并生成物理上准确的轨迹？

### 核心思路/方法
1. **场景分解**：将场景分解为每个物体的高斯表示和碰撞网格。
2. **可微物理仿真**：从观测到的遮挡前轨迹中，通过可微仿真估计摩擦系数和速度。
3. **轨迹预测**：利用可微刚体动力学方程预测遮挡期间的SE(3)轨迹，该轨迹能够捕捉弹跳、摩擦减速和方向变化等接触事件。
4. **损失函数**：引入质心轮廓损失，将位置梯度与外观噪声分离，使轨迹误差比光度监督降低40%。
5. **评估方式**：使用留出的、观察到物体遮挡过程的相机进行测试。

### 主要贡献
1. 提出PersistGS方法，首次将可微刚体物理仿真与3D高斯泼溅结合，解决了遮挡下的物体持久性问题。
2. 通过可微仿真预测的轨迹满足刚体动力学方程，能够建模运动学外推无法模拟的接触事件（如弹跳、摩擦减速）。
3. 在合成场景实验中，PersistGS相较于匀速外推在PSNR上提升+2.46dB，且与真实轨迹上界仅差0.19dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法针对动态场景重建中遮挡这一关键难题，提出了将物理仿真与神经渲染结合的新范式，且实验指标提升显著（+2.46dB PSASNR），并接近理想上界。对于关注4D重建、物理感知渲染的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (3DGS) methods reconstruct time-varying scenes from synchronized multi-camera video using photometric supervision. When a moving object becomes fully occluded from all training cameras, this supervision vanishes: the Gaussians representing it receive no gradient signal and degrade. Existing approaches to incomplete observations in neural reconstruction rely on learned generative priors that prioritize visual plausibility over physical correctness. We propose $\textbf{PersistGS}$, a method that restores object permanence during occlusion by coupling differentiable rigid body simulation with 3D Gaussian Splatting. Our approach decomposes the scene into per-object Gaussians and collision meshes, estimates friction and velocity from the observed pre-occlusion trajectory via differentiable simulation, and uses the resulting SE(3) trajectory to position object Gaussians throughout the occlusion period. Because the predicted trajectory satisfies the governing equations of rigid body dynamics, it faithfully captures contact events (bounces, friction-based deceleration, direction changes) that kinematic extrapolation cannot model. We introduce a centroid silhouette loss that isolates positional gradients from appearance noise, yielding 40% lower trajectory error than photometric supervision. We evaluate using cameras withheld from training that observe the object during its occlusion. Experiments on synthetic scenes show that PersistGS outperforms constant velocity extrapolation by +2.46dB PSNR and comes within 0.19dB of a ground-truth trajectory upper bound.

</details>

#### 2026-06-01 - TROPHIES: Temporal Reconstruction of Places, Humans, and Cameras from Multi-view Videos

**Authors:** Jinpeng Liu, Yukang Xu, Yutong Li, Xingyu Liu
**Links:** [abs](https://arxiv.org/abs/2606.02350) - [pdf](https://arxiv.org/pdf/2606.02350)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** temporal reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TROPHIES: Temporal Reconstruction of Places, Humans, and Cameras from Multi-view Videos
- 作者：Jinpeng Liu, Yukang Xu, Yutong Li, Xingyu Liu
- 出版日期：2026-06-01T15:00:18Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要地址 https://arxiv.org/abs/2606.02350 | PDF地址 https://arxiv.org/pdf/2606.02350

### 一句话总结
本文提出TROPHIES框架，从多视角视频中联合重建动态人体、静态场景和相机位姿，并在全局坐标系中实现几何、运动和轨迹的一致性。

### 研究问题
如何从多视角视频中实现人体、场景与相机位姿的全局一致4D重建，以克服现有单视角或解耦方法无法获得连贯几何、稳定运动和物理对齐轨迹的局限。

### 核心思路/方法
- 提出统一框架TROPHIES，包含一个人体分支（Human Branch）和场景分支（Scene Branch）。
- 人体分支：通过时间与空间推理对人体进行建模。
- 场景分支：引入人类感知注意力机制重建静态场景几何。
- 全局对齐与优化模块：通过尺度一致性、接触先验和跨视角时间一致性约束，将两个分支耦合。

### 主要贡献
- 提出新任务：多视角视频中统一的人类-场景-相机重建。
- 设计TROPHIES框架，能恢复全局对齐、物理合理的4D重建。
- 在EgoHuman和EgoExo4D数据集上验证，在全局保真度和人-场景一致性上始终优于现有范式。

### 局限性
摘要未提供足够信息（未提及方法的计算开销、对多视角数量的依赖、或特定失败场景）。

### 阅读优先级
高。理由：该工作针对4D重建中未被很好解决的问题（解耦导致的不一致性），提出了统一框架，并在公开基准上取得明显改进，对动态场景感知与重建方向具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing humans and their surrounding environments in a globally consistent 4D space is essential for comprehensive perception. However, prior works typically assume single-view inputs or decouple humans, scenes, and cameras, making them unable to recover coherent geometry, stable motion, and physically aligned trajectories. These limitations motivate us to introduce a new task: unified human-scene-camera reconstruction from multi-view videos, which aims to jointly estimate dynamic humans, static scenes, and camera poses in one global coordinate frame. We propose TROPHIES--Temporal Reconstruction of Places, Humans, and Cameras from Multi-view Videos-a unified framework tailored for this task. TROPHIES features a Human Branch that models humans through temporal and spatial reasoning, and a Scene Branch that reconstructs static geometry with human-aware attention. A global alignment and optimization module couples both branches by enforcing scale consistency, contact priors, and cross-view temporal coherence. Experiments on EgoHuman and EgoExo4D demonstrate that TROPHIES achieves globally aligned, physically plausible 4D reconstructions and consistently outperforms existing paradigms in both global fidelity and human-scene consistency.

</details>

#### 2026-06-01 - WebSpline: Structure-Informed Splines for Real-Time 3D Gaussians from Monocular Videos

**Authors:** Jongmin Park, Jeonghwan Yun, Minh-Quan Viet Bui, Munchurl Kim
**Links:** [abs](https://arxiv.org/abs/2606.02096) - [pdf](https://arxiv.org/pdf/2606.02096)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, dynamic Gaussian, scene reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WebSpline: Structure-Informed Splines for Real-Time 3D Gaussians from Monocular Videos
- 作者：Jongmin Park, Jeonghwan Yun, Minh-Quan Viet Bui, Munchurl Kim
- 出版日期：2026-06-01T11:28:17Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：摘要 URL: https://arxiv.org/abs/2606.02096；PDF URL: https://arxiv.org/pdf/2606.02096

### 一句话总结
WebSpline 提出了一种结构信息样条 (SIS) 表示法，用于从单目视频中实时、高质量地重建动态 3D 高斯场景，在保持全局结构一致性的同时实现了快速渲染。

### 研究问题
从单目视频进行动态场景重建时，如何同时平衡全局结构连贯性和局部细粒度细节，并在有限的多视角线索下实现快速渲染？

### 核心思路/方法
1. **表示学习**：提出结构信息样条 (SIS) 表示，每个动态高斯的轨迹由可学习的三次埃尔米特样条建模。
2. **结构组织**：引入辅助结构代理图 (SPG)，用于在运动中组织各个高斯轨迹的结构关系。
3. **两阶段优化**：
   - 第一阶段：从 2D 点轨迹初始化 SPG，并通过时间刚性正则化进行精细化，以建立序列中运动物体的结构连贯性。
   - 第二阶段：从精细化后的 SPG 初始化 SIS 表示，并在空间和结构邻域约束下优化。
4. **推理**：仅通过评估学习到的 SIS 即可获得高斯运动，从而实现快速渲染。

### 主要贡献
- 提出 WebSpline 框架，实现了从单目视频中进行结构连贯且高保真的动态场景重建。
- 设计了 SIS 表示法和 SPG 结构，有效融合了全局结构信息与局部运动细节。
- 在 iPhone 和 NVIDIA 基准上达到最先进的渲染质量，且在 iPhone 数据集上渲染速度比第二名方法 WorldTree 快 10 倍以上。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法在动态场景重建中同时实现了高渲染质量和实时性能，解决了该领域的核心平衡问题，且在两大数据集上达到 SOTA，对 4D 重建和实时渲染方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic scene reconstruction from monocular videos remains highly challenging, as existing methods often struggle to balance global structural coherence and local fine-grained details under limited multi-view cues. To address this challenge, we propose WebSpline, a novel dynamic 3D Gaussian framework that enables structurally coherent and high-fidelity reconstruction from monocular videos with fast rendering. The core of WebSpline is the Structure-Informed Spline (SIS) representation, which models each dynamic Gaussian trajectory using a learnable cubic Hermite spline whose motion is structurally organized with an auxiliary Structural Proxy Graph (SPG). The proposed framework is optimized in two stages: (i) in the first stage, the SPG is initialized from 2D point tracks and refined with temporal rigidity regularization to establish structural coherence for moving objects across the sequence; and (ii) in the second stage, the SIS representation is initialized from the refined SPG and optimized under both spatial and structural neighborhood constraints. At inference, Gaussian motion is obtained solely by evaluating the learned SIS, enabling fast rendering. Extensive experiments on the challenging monocular dynamic scene benchmarks, iPhone and NVIDIA, demonstrate that our WebSpline achieves state-of-the-art rendering quality while rendering over 10 times faster than WorldTree, the second-best method on the iPhone dataset.

</details>

#### 2026-06-01 - TIDES: Time-Derivative Event Simulation via Deformable Reconstruction

**Authors:** Christopher Thirgood, Dipon Kumar Ghosh, Simon Hadfield
**Links:** [abs](https://arxiv.org/abs/2606.02058) - [pdf](https://arxiv.org/pdf/2606.02058)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** deformable reconstruction, dynamic Gaussian, Gaussian Splatting, scene representation, rendering, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TIDES: Time-Derivative Event Simulation via Deformable Reconstruction
- 作者：Christopher Thirgood, Dipon Kumar Ghosh, Simon Hadfield
- 出版日期：2026-06-01
- 分类：Dynamic / 4D Reconstruction（主类别）；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次类别）
- 链接：摘要链接：https://arxiv.org/abs/2606.02058；PDF链接：https://arxiv.org/pdf/2606.02058

### 一句话总结
提出一个基于动态高斯泼溅的连续时间事件模拟器TIDES，通过三维场景显式重建解决现有模拟器在快速运动与遮挡下的时间戳批处理缺陷。

### 研究问题
现有事件相机模拟器从帧序列推断事件时间戳，导致许多阈值交叉事件共享少量离散时间（称为时间戳批处理），尤其在快速运动和遮挡场景下加剧；如何更精确地模拟连续时间事件流。

### 核心思路/方法
1. 采用动态高斯泼溅构建显式三维场景表征，学习几何与运动，从而直接从场景推导每像素强度变化率，而非通过渲染帧差分。
2. 利用同一三维场景模型感知部分遮挡区域，指导自适应时间步长，仅在遮挡动态使亮度变化模型不可靠的区域集中计算。
3. 通过瓦片级仲裁器建模有限传感器带宽，模拟吞吐量、抖动和事件丢失等现实传感器伪影。

### 主要贡献
- 提出基于三维场景显式表示的连续时间事件模拟方法，支持每渲染步的多次阈值交叉预测，无需时间上采样或帧插值。
- 利用场景遮挡信息实现自适应时间步进，减少非必要计算。
- 建模传感器带宽有限性产生的伪影，提升仿真真实性。
- 在配对RGB-事件基准上达到最先进的事件流保真度，且模拟事件在真实下游任务中迁移效果优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法针对事件模拟中的关键缺陷（时间戳批处理）提出创新解决方案，同时结合显式三维表征和传感器建模，实验验证了保真度提升和下游任务迁移有效性。对动态场景重建、事件相机仿真和机器人/AR应用领域的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Event cameras emit asynchronous events in response to environmental appearance changes. The scarcity of real-world event datasets makes simulation essential. However, most simulators infer event timestamps from frame sequences, forcing many threshold crossings to share a small set of discrete times; a failure mode we term timestamp batching that worsens under fast motion and occlusion. We present TIDES, a continuous-time event simulator built on dynamic Gaussian splatting. Because TIDES operates on an explicit 3D scene representation with learnt geometry and motion, it can derive per-pixel intensity dynamics directly from the scene, rather than by differencing rendered frames. This enables accurate threshold-crossing prediction, including multiple crossings per rendering step, without temporal upsampling or frame interpolation. The same 3D scene model reveals where objects partially occlude one another; TIDES uses this to guide adaptive time stepping, concentrating computation only in regions where occlusion dynamics make simple models of brightness change unreliable. Finally, we model finite sensor bandwidth using a tile-level arbiter whose throughput, jitter, and event drops reproduce realistic sensor artifacts. Across paired RGB-event benchmarks, TIDES attains state-of-the-art event-stream fidelity. We also show that events simulated by TIDES transfer more effectively to real downstream tasks than competitors'.

</details>

#### 2026-06-01 - DisFlow: Scene Flow from Distance Field for Object Pose, Velocity Tracking, and Dynamic Object Reconstruction

**Authors:** Lan Wu, Sheila Sutjipto, Jennifer Wakulicz, Teresa Vidal-Calleja
**Links:** [abs](https://arxiv.org/abs/2606.01824) - [pdf](https://arxiv.org/pdf/2606.01824)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** scene flow, pose estimation, surface reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DisFlow: Scene Flow from Distance Field for Object Pose, Velocity Tracking, and Dynamic Object Reconstruction
- 作者：Lan Wu, Sheila Sutjipto, Jennifer Wakulicz, Teresa Vidal-Calleja
- 出版日期：2026-06-01
- 分类：Dynamic / 4D Reconstruction (主), 3D Reconstruction & Multi-view Geometry (次)
- 链接：[摘要](https://arxiv.org/abs/2606.01824) | [PDF](https://arxiv.org/pdf/2606.01824)

### 一句话总结
提出基于距离场的场景流框架DisFlow，通过高斯过程隐式曲面（GPIS）表示和对象坐标系中的概率融合，实现实时6DoF物体姿态跟踪、运动估计与动态表面重建。

### 研究问题
如何在在线场景中，同时从动态物体的距离场中估计场景流、物体姿态、速度并重建物体表面，且保持几何一致性。

### 核心思路/方法
1. **场景表示**：用高斯过程隐式曲面（GPIS）表示场景，加入表面法向量作为导数约束，以计算近表面的有符号距离和带不确定性的梯度。
2. **场景流计算**：基于上述距离场计算场景流，描述连续帧间表面点的时空运输。
3. **姿态与运动估计**：通过闭合形式优化，将新观测的点云增量式注册，从而估计物体位姿和运动。
4. **概率融合**：直接在“对象坐标系”中进行概率融合，使物体在时间上保持几何一致，而非在相机或世界坐标系中操作。

### 主要贡献
- 提出DisFlow框架，将场景流、物体姿态速度跟踪与动态表面重建紧密耦合，并在对象坐标系中实现概率融合。
- 利用GPIS的导数约束实现精确有符号距离与梯度查询，支持实时运行。
- 在动态物体序列上验证了该方法能同时实现准确的姿态运动跟踪与高质量表面重建，并公开了代码。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：文章解决了动态场景中姿态估计、跟踪与表面重建的联合实时问题，方法新颖（对象坐标系概率融合+GPIS场景流），且已公开代码，具备较强实用性和可复现性。

</details>

<details>
<summary>Abstract</summary>

We present \emph{DisFlow}, a novel framework for online scene flow estimation from distance field that enables \emph{6DoF dynamic object pose estimation}, \emph{motion tracking}, and \emph{surface reconstruction}. The scene is represented by Gaussian Process Implicit Surfaces (GPIS), with surface normals serving as derivative constraints, enabling accurate signed distance computations near the surface and gradient queries with uncertainty. With this representation as a foundation, we compute a scene flow from the distance field that describes how surface points are transported over time in consecutive frames. Through our flow, we can estimate an object's pose and motion by incrementally registering a new observed point cloud via an elegant closed-form optimisation. Unlike prior methods that operate in the camera or world frame, our approach performs probabilistic fusion directly in the \emph{object frame}, where the object remains geometrically consistent over time. The tight coupling of the DisFlow method in space and time yields dense geometry, surface normals, object pose trajectories, velocities, and uncertainty, all at real-time rates. We evaluate DisFlow on dynamic object sequences and demonstrate that it achieves accurate pose and motion tracking while simultaneously reconstructing high-quality object surfaces. Code publicly available at \href{https://github.com/LanWu076/disflow_ros2}{https://github.com/LanWu076/disflow\_ros2}

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

#### 2026-06-02 - SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image

**Authors:** Inhee Lee, Sangwon Baik, Sungjoo Kim, Hyeonwoo Kim, Hyunsoo Cha, Hanbyul Joo
**Links:** [abs](https://arxiv.org/abs/2606.03994) - [pdf](https://arxiv.org/pdf/2606.03994)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, scene reconstruction, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image
- 作者：Inhee Lee, Sangwon Baik, Sungjoo Kim, Hyeonwoo Kim, Hyunsoo Cha, Hanbyul Joo
- 出版日期：2026-06-02
- 分类：3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2606.03994

### 一句话总结
提出SimuScene，一种从单张图像重建物理稳定的组合式3D场景的管道，其核心创新在于利用物理仿真引擎作为诊断工具，在生成过程中反馈修正形状与布局误差，而非仅作为后处理。

### 研究问题
如何从单张图像重建出可直接用于物理仿真（无穿透、悬空、下沉等物理不稳定现象）的组合式3D场景，克服现有单图提升方法在生成后因形状和布局误差导致的仿真崩溃问题。

### 核心思路/方法
1. **物理在环（Physics-in-the-Loop）**：将物理引擎（如重力仿真）用于生成过程中的诊断，而非仅仅作为后处理布局修正。
2. **诊断性仿真**：对重建的物体施加重力进行仿真，将穿透和支撑失效等物理不稳定现象量化为校正信号。
3. **迭代反馈**：基于校正信号驱动重力轴上的拉伸和全图（amodal）形状重采样，从而在形状和布局估计阶段纳入物理约束，减少累积误差，最终输出稳定的仿真就绪场景。

### 主要贡献
1. 提出一种新的组合式3D重建方法，在形状和布局估计中融入物理约束（而非仅后处理）。
2. 利用物理引擎作为诊断测量工具，将物理不稳定转化为定量信号指导生成过程。
3. 在物理稳定性和几何对齐基准上达到最先进性能，并通过人形控制和机械臂操作任务展示了实际应用价值。

### 局限性
摘要未提供关于方法局限性的信息，例如对物体类别、输入图像质量、计算复杂度或极端物理场景（如复杂关节或可变形物体）的适应性等细节。

### 阅读优先级
高。理由：该工作针对机器人操作和物理仿真中的关键瓶颈（单图场景重建的物理稳定性），提出了创新的“物理在环”反馈框架，方法新颖且实验验证了在稳定性基准和具体任务上的有效性，对3D重建与具身智能交叉领域有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing interactive, simulation-ready 3D scenes from a single image is a critical bottleneck for robotic manipulation. While recent single-image lifters recover plausible per-object shapes, composing them yields scenes that collapse under physical simulation due to interpenetrating, hovering, or sinking objects. Existing physics-aware methods address this strictly as a post-hoc layout correction, leaving the underlying geometric errors unresolved. To address this, we introduce SimuScene, a compositional 3D reconstruction pipeline that puts physics in the loop of shape and layout estimation. Rather than using physics merely for layout cleanup, we utilize the physics engine as a diagnostic measurement tool during the generative process itself. By diagnostically simulating reconstructed objects under gravity, we convert penetration and support failures into quantitative correction signals that drive gravity-axis stretching and amodal shape resampling. This physics-informed feedback loop mitigates accumulated reconstruction errors and produces a stable, simulation-ready compositional 3D scene. Extensive experiments demonstrate state-of-the-art performance on physical stability and geometric alignment benchmarks. We further highlight SimuScene's utility by deploying reconstructed environments in humanoid control and robot-arm manipulation tasks.

</details>

#### 2026-06-02 - PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation

**Authors:** Shinjeong Kim, Ignacio Alzugaray, Callum Rhodes, Paul H. J. Kelly, Andrew J. Davison
**Links:** [abs](https://arxiv.org/abs/2606.03989) - [pdf](https://arxiv.org/pdf/2606.03989)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation
- 作者：Shinjeong Kim, Ignacio Alzugaray, Callum Rhodes, Paul H. J. Kelly, Andrew J. Davison
- 出版日期：2026-06-02T17:59:22Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2606.03989；PDF: https://arxiv.org/pdf/2606.03989；项目页面: https://www.shinjeongkim.com/pixvod/

### 一句话总结
本文提出一种完全可并行化的像素级视觉里程计与深度估计方法PixVOD，通过高斯置信传播（GBP）在传感器像素间分布式计算，并引入关键帧锚定机制以保证优化稳定性。

### 研究问题
如何设计一种可在传感器像素间完全并行化运行的视觉里程计与深度估计方法，以降低从传感器传输冗余像素数据的开销，并利用像素级计算为高层视觉任务提供更丰富的输入。

### 核心思路/方法
- 提出完全可并行化的视觉里程计和深度估计范式，使传感器处理器中的每个像素都能独立参与计算。
- 采用高斯置信传播（GBP）在像素间交换信息，以协同估计相机运动，并从每个像素的光度观测和表面法线先验中推断深度。
- 引入类似关键帧的锚定机制，调节帧间有效基线，从而在优化过程中保持几何稳定性，实现一致的相机运动与深度更新。

### 主要贡献
1. 提出首个基于GBP的像素级分布式视觉里程计与深度估计框架。
2. 设计了关键帧锚定机制，有效维持了像素级分布式优化中的几何稳定性。
3. 在真实数据集上验证了该方法在传感器处理器上实现分布式计算的可行性。

### 局限性
摘要未提供足够信息（未提及量化误差分析、计算复杂度、对传感器硬件的具体依赖或失败案例等）。

### 阅读优先级
中。理由：该方法在传感器计算和分布式视觉领域具有新颖性，适合对焦平面处理或片上视觉系统感兴趣的读者；但摘要未展示与传统方法的定量对比性能，实验细节有限，可能对需要直接对比方法的读者价值中等。

</details>

<details>
<summary>Abstract</summary>

Images composed of 2D pixel arrays are the standard input to computer vision algorithms, yet many underlying computations can be distributed across pixels. Transmitting raw, redundant, and noisy pixel data off the sensor remains inefficient, motivating a shift toward focal-plane sensor-processors that perform a significant part of the computation directly within each pixel. We envision pixels synthesizing higher-level signals locally, reducing downstream load, and providing richer inputs for higher-level vision tasks. We propose a fully parallelizable form of visual odometry and depth estimation across pixels, where sensor-processors exchange information through Gaussian Belief Propagation (GBP) to achieve consensus about camera motion and infer depth from per-pixel photometric observations and a surface normal prior. To maintain geometric stability during optimization, we introduce a keyframe-like anchoring mechanism that regulates the effective baseline between frames, enabling consistent motion and depth updates. Our method is evaluated on realistic datasets, demonstrating the feasibility of GBP-based pixel-level distributed odometry and depth estimation with keyframe anchoring on-sensor. Project Page: https://www.shinjeongkim.com/pixvod/

</details>

#### 2026-06-02 - Multi-Robot Bearing-only Pose Estimation via Angle Rigidity

**Authors:** J. Francisco Presenza, Leonardo J. Colombo, Ignacio Mas, Juan I. Giribet
**Links:** [abs](https://arxiv.org/abs/2606.03931) - [pdf](https://arxiv.org/pdf/2606.03931)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-Robot Bearing-only Pose Estimation via Angle Rigidity
- 作者：J. Francisco Presenza, Leonardo J. Colombo, Ignacio Mas, Juan I. Giribet
- 出版日期：2026-06-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.03931

### 一句话总结
本文提出了一种基于角度刚性的分布式方位仅位姿估计方法，仅利用机器人间的方位测量和更弱的拓扑条件（角度刚性），可实现时变多机器人系统的位置和方向估计。

### 研究问题
如何在没有方向信息且拓扑条件更弱的分布式多机器人系统中，仅利用方位测量来估计机器人的三维位置和方向。

### 核心思路/方法
- 利用机器人本体坐标系中的方位角计算出的角度，估计机器人在 \(\mathbb{R}^3\) 中的位置。
- 从估计位置、方位及其导数恢复出机器人在 \(\mathrm{SO}(3)\) 中的方向。
- 要求感知拓扑满足“角度刚性”条件，该条件弱于常用的方位刚性。
- 在部分机器人的运动持续激励假设下，建立了观测器的局部一致指数稳定性。

### 主要贡献
1. 提出了一种新的分布式方位仅姿态估计器，适用于时变多机器人系统。
2. 将所需的拓扑条件从传统方位刚性放宽为更弱的“角度刚性”。
3. 通过理论分析证明了观测器的局部一致指数稳定性。
4. 通过仿真验证了方案的有效性和实用性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**
理由：该论文在分布式机器人状态估计领域提出了新的理论条件（角度刚性），并给出了稳定性证明，对相关方向的研究者有一定参考价值。但由于未提供与现有方法的定量对比结果，且缺乏实验细节，实用性评估有限。建议有具体兴趣的读者进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

This letter proposes a novel distributed bearing-based pose estimator for time-varying multi-robot systems. The method uses angles computed from body-frame bearings to estimate the robots' positions in $\mathbb{R}^3$ without knowledge of their orientations. The orientations in $\mathrm{SO}(3)$ are recovered from the estimated positions, the bearings, and the bearing derivatives. The proposed observer only requires the (directed) sensing topology to be \textit{angle-rigid}, a weaker condition than the commonly used ones like bearing rigidity. Local uniform exponential stability of the proposed observer is established under the assumption of persistently exciting motions for a subset of robots. Simulations are presented and discussed to evaluate the scheme's effectiveness and practicality.

</details>

#### 2026-06-02 - SAMatcher: Co-Visibility Modeling with Segment Anything for Robust Feature Matching

**Authors:** Xu Pan, Qiyuan Ma, Mingyue Dong, He Chen, Wei Ji, Xianwei Zheng
**Links:** [abs](https://arxiv.org/abs/2606.03406) - [pdf](https://arxiv.org/pdf/2606.03406)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** image matching, structure from motion, feature matching, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAMatcher: Co-Visibility Modeling with Segment Anything for Robust Feature Matching
- 作者：Xu Pan, Qiyuan Ma, Mingyue Dong, He Chen, Wei Ji, Xianwei Zheng
- 出版日期：2026-06-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2606.03406；PDF: https://arxiv.org/pdf/2606.03406

### 一句话总结
SAMatcher提出了一种基于“共同可见性建模”的特征匹配框架，利用Segment Anything Model（SAM）通过预测跨视图的共可见区域掩码和边界框作为结构先验，来提升大视角和尺度变化下的鲁棒特征匹配性能。

### 研究问题
如何通过显式建模跨视图的“共同可见区域”来改进特征匹配的鲁棒性，尤其是在大视角和尺度变化较大的场景下。

### 核心思路/方法
1.  **共可见性建模**：不直接进行局部特征匹配，而是先预测跨视图共同可见区域的掩码（mask）和边界框（bounding box），作为后续匹配的结构先验。
2.  **基于SAM的交互机制**：内置对称的跨视图交互机制，实现双向特征交换和跨视图语义对齐。
3.  **统一监督方案**：联合优化掩码预测、边界框回归以及掩码-边界框一致性约束三个目标。

### 主要贡献
1.  提出了SAMatcher，一个通过共可见性建模来估计对应关系的特征匹配框架。
2.  展示了原本用于单目分割的基础模型（SAM）可以通过显式的共可见性建模，扩展应用于多视图对应关系推理。
3.  在多个挑战性基准上，方法在存在大视角和尺度变化的情况下，显著优于现有匹配管道。

### 局限性
摘要未提供足够信息。摘要中未提及任何关于计算复杂度、失败案例或具体应用场景限制的局限性讨论。

### 阅读优先级
**高**
理由：该工作首次系统地将SAM大模型引入特征匹配任务，通过显式共可见性建模提供了一个新的解决思路，并且实验证明在大视角变化场景下具有显著优势。这对于三维重建、视觉定位等下游应用具有重要潜在价值，属于将基础模型拓展到新任务领域的创新性工作。

</details>

<details>
<summary>Abstract</summary>

Reliable correspondence estimation is a fundamental problem in image processing, underpinning applications such as Structure from Motion, visual localization, and image registration. Existing learning-based methods have significantly improved local feature representations, yet most still operate at the pixel or patch level and lack explicit modeling of regions that are jointly visible across views. We propose SAMatcher, a feature matching framework that formulates correspondence estimation through co-visibility modeling. Instead of directly matching local features, SAMatcher first predicts co-visible region masks and bounding boxes as structured priors for correspondence estimation. Built upon the Segment Anything Model (SAM), it introduces a symmetric cross-view interaction mechanism that enables bidirectional feature exchange and cross-view semantic alignment. We further develop a unified supervision scheme that jointly optimizes mask prediction and box localization through mask learning, box regression, and mask-box consistency constraints. Extensive experiments on challenging benchmarks demonstrate substantial improvements over existing matching pipelines, particularly under large viewpoint and scale variations. Our results show that foundation models originally designed for monocular segmentation can be effectively extended to multi-view correspondence reasoning through explicit co-visibility modeling, offering a new perspective on structured representation learning for image matching. Code and project page: https://xupan.top/Projects/samatcher

</details>

#### 2026-06-02 - BA-T: An Iterative Transformer for Two-View Bundle Adjustment

**Authors:** Ganlin Zhang, Weirong Chen, Daniel Cremers, Xi Wang
**Links:** [abs](https://arxiv.org/abs/2606.03287) - [pdf](https://arxiv.org/pdf/2606.03287)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BA-T: An Iterative Transformer for Two-View Bundle Adjustment
- 作者：Ganlin Zhang, Weirong Chen, Daniel Cremers, Xi Wang
- 出版日期：2026-06-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.03287

### 一句话总结
BA-T 提出一种基于迭代Transformer的轻量级网络，通过模拟经典束调整（BA）的结构化更新过程，在隐式token空间内逐步优化双视图位姿与几何重建，以较小的解码器参数量实现媲美大模型的精度。

### 研究问题
现有前馈3D重建模型依赖深层交叉注意力解码器进行信息交换，但缺乏几何精化机制，导致多视图一致性差。如何设计一种轻量、结构化的迭代方法来替代深度解码器堆叠，同时提升位姿和重建精度？

### 核心思路/方法
- 将经典束调整（BA）视为位姿与局部几何之间迭代信息传播的过程，并将其抽象为隐式token空间中的可重复层（repeatable layer）。
- 提出BA-T：一个迭代Transformer，每一层利用潜在残差（latent residual）执行类似BA的结构化更新，而非依赖深层注意力堆叠。
- 采用单一轻量级层代替深度解码器，通过多次迭代逐步精化预测结果。

### 主要贡献
1. 提出BA-T，一种将束调整风格的结构化更新引入Transformer迭代框架的方法，实现隐式特征空间的几何精化。
2. 在仅使用传统模型16%解码器参数的情况下，达到或超越更大规模模型的性能，展现极佳的参数效率。
3. 实验证明BA-T能随迭代次数稳步提升位姿与重建精度，并增强跨视图一致性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对多视图几何与3D重建中的一个核心瓶颈（解码器深度与多视图一致性），提出了一种结构紧凑的迭代方案，具有显著参数效率提升，且公开代码。对于关注轻量级、高效Transformer在几何任务中应用的读者，有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward models for 3D reconstruction have achieved strong performance using deep cross-view attention to exchange information across images. However, these approaches often depend on heavy decoder stacks and lack a structured mechanism for geometry refinement, resulting in poor multi-view consistency. We address this by drawing inspiration from classical bundle adjustment (BA), which can be viewed as an iterative information propagation process between poses and local geometry. Inspired by BA, we propose BA-T, an iterative Transformer that implements BA-style structured updates as a repeatable layer in implicit token space. Instead of relying on deep attention stacks, BA-T refines predictions based on latent residual by a single lightweight layer. Experiments demonstrate that BA-T progressively improves pose and reconstruction accuracy across iterations, achieves stronger cross-view consistency than conventional decoders, and matches or surpasses substantially larger models while using only 16% of their decoder parameters. BA-T provides a compact, efficient, and structural alternative to depth-heavy attention, enabling accurate 3D reconstruction within a lightweight architecture. The code will be made publicly at https://github.com/zhangganlin/BA-T.

</details>

#### 2026-06-01 - BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting

**Authors:** Yanchen Wang, Lenny Aharon, Wangshu Zhu, Kyle Daruwalla, Linghua Zhang, Jiaru Zou, Selmaan Chettih, Helen Hou, Liam Paninski, Matthew R Whiteway
**Links:** [abs](https://arxiv.org/abs/2606.02937) - [pdf](https://arxiv.org/pdf/2606.02937)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, pose estimation, Gaussian Splatting, novel view synthesis, view synthesis, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting
- 作者：Yanchen Wang, Lenny Aharon, Wangshu Zhu, Kyle Daruwalla, Linghua Zhang, Jiaru Zou, Selmaan Chettih, Helen Hou, Liam Paninski, Matthew R Whiteway
- 出版日期：2026-06-01T22:34:14Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：摘要页 https://arxiv.org/abs/2606.02937 ；PDF https://arxiv.org/pdf/2606.02937

### 一句话总结
BEAST3D是一个自监督预训练框架，通过可微渲染预测3D高斯溅射（Gaussian splats）从无标签多视角视频中学习3D视觉表示，并用于动物行为分析与神经编码。

### 研究问题
如何从实验室场景中的稀疏多视角视频（仅4个视角）中，无需人工标注即可提取丰富的3D动物行为表示，并有效应用于下游任务（新视角合成、姿态估计、神经编码）。

### 核心思路/方法
- 采用自监督预训练框架：在未标记的、标定过的多视角视频上训练。
- 使用视觉Transformer预测3D高斯溅射，并通过可微渲染重建被遮蔽的视角（held-out views）。
- 在训练过程中同时分割动物与背景。
- 直接利用已知相机参数实现稀疏视角（最少4个视角）下的3D结构重建，避免像通用模型那样需依赖密集重叠视角来估计相机几何。

### 主要贡献
1. 提出BEAST3D自监督框架，可从无标签多视角视频中学习视角不变的3D表示。
2. 实现了在稀疏视角（如4个视角）下的3D结构重建，解决了通用模型在实验室场景中因视角不足而失效的问题。
3. 在四个物种的数据集上展示框架的有效性，涵盖三个下游任务：新视角合成（验证3D表示质量）、多视角姿态估计（提供稀疏关键点轨迹）、以及神经编码（将3D行为特征与神经活动关联）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：本工作面向动物行为分析与神经编码领域，方法上融合了自监督学习、3D高斯溅射和多视角几何，对于从事计算神经科学、动物行为量化或3D场景理解的研究者有一定参考价值。但若读者不涉及该领域，或更关注通用3D重建方法，则阅读优先级较低。

</details>

<details>
<summary>Abstract</summary>

Multi-view video recordings are increasingly used to capture the 3D movements of animals in experimental settings, yet extracting rich 3D representations from these recordings remains challenging. Supervised pose estimation requires extensive manual annotation, while general-purpose 3D reconstruction models trained on generic scene datasets fail on the specialized imagery and sparse-view setting of laboratory experiments. We address these limitations with BEAST3D, a self-supervised pretraining framework that learns 3D visual representations from unlabeled, calibrated multi-view video. BEAST3D uses a vision transformer to predict 3D Gaussian splats that reconstruct held-out views through differentiable rendering, while simultaneously segmenting the animal from the background. BEAST3D reconstructs 3D structure with as few as four views by conditioning directly on known camera parameters--unlike general-purpose models, which must estimate camera geometry from dense overlapping viewpoints that are seldom available in lab settings. Through comprehensive evaluation across four species, we demonstrate that BEAST3D produces rich, viewpoint-invariant features that transfer effectively to three downstream tasks: novel view synthesis, which validates the quality of the learned 3D representations; multi-view pose estimation, which provides the sparse keypoint trajectories widely used in behavioral analysis; and neural encoding, which relates 3D behavioral features to simultaneously recorded neural activity. BEAST3D thus establishes a versatile framework for behavioral analysis that leverages 3D structure in modern multi-view laboratory recordings.

</details>

#### 2026-06-01 - Modeling Depth Ambiguity: A Mixture-Density Representation for Flying-Point-Free Depth Estimation

**Authors:** Siyuan Bian, Congrong Xu, Jun Gao
**Links:** [abs](https://arxiv.org/abs/2606.02552) - [pdf](https://arxiv.org/pdf/2606.02552)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Modeling Depth Ambiguity: A Mixture-Density Representation for Flying-Point-Free Depth Estimation
- 作者：Siyuan Bian, Congrong Xu, Jun Gao
- 出版日期：2026-06-01T17:50:28Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要链接：https://arxiv.org/abs/2606.02552；PDF链接：https://arxiv.org/pdf/2606.02552

### 一句话总结
本文提出一种混合密度表示法（MDA），让模型为每个像素预测多个深度假设及其概率，从而消除深度估计中物体边界处的“飞点”伪影。

### 研究问题
深度估计模型在物体边界处常产生“飞点”（flying points），即在空空间中预测虚假的3D点。原因是标准做法为每个像素只分配单个深度假设，导致边界像素的深度被拉向前景和背景之间的中间值，而非任何真实表面。

### 核心思路/方法
采用混合密度表示（Mixture-Density Representation, MDA），使模型为每个像素预测多个深度假设及其关联概率。在边界处，不同假设可与不同表面对齐，解码时从这些假设中选择一个深度，而非在空空间中插值。该方法还自然扩展到透明物体（预测多个深度层）和天空区域（用专用组件分离无限远天空与有限深度区域）。

### 主要贡献
- 指出“飞点”伪影源于单深度假设建模，并分析其成因。
- 提出MDA混合密度表示法，通过多假设预测消除边界飞点。
- 实验证实该方法在不同骨干网络上显著改善边界重建，在强烈输入模糊下仍有效去除飞点，且运行时开销可忽略不计。
- 展示该框架可扩展至透明物体和天空区域，实现无飞点的天际线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作解决了深度估计中一个持久且关键的失败模式（飞点伪影），方法直接且验证有效，同时关注了透明物体和天空等实际挑战，对3D场景理解和重建领域具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Despite advances in depth estimation, flying points remain a persistent failure mode: near object boundaries, depth estimators often predict spurious 3D points in the empty space between foreground and background surfaces. We trace this artifact to a standard modeling choice: assigning each pixel a single depth hypothesis. At boundaries, a pixel can straddle a foreground and a background surface, so its true depth is ambiguous between the two. A model that predicts a single depth cannot keep both possibilities, so training instead pulls the prediction toward an intermediate depth that lies on neither surface. We address this with MDA, a mixture-density representation that lets the model predict multiple depth hypotheses and their associated probabilities for each pixel. Near boundaries, different hypotheses can align with different surfaces, and the decoded depth is selected from one of these hypotheses rather than placed in the empty space between them. Across different backbones, MDA substantially improves boundary reconstruction and largely removes flying-point artifacts even under severe input blur, while adding negligible runtime overhead. The same mixture-density framework naturally extends to transparent objects, where it predicts multiple depth layers at transparent pixels, and to sky regions, where a dedicated component separates the unbounded sky from finite-depth regions, producing flying-point-free skylines. Project Page: https://biansy000.github.io/mda-site/.

</details>

#### 2026-06-01 - Symmetry-Aware 9D Pose Estimation with Sim(3)-Consistent Feature and Spherical Inception Convolution

**Authors:** Panfei Cheng, Hongshan Yu, Wenrui Chen, Xiaojun Tang, Jian Liu, Naveed Akhtar
**Links:** [abs](https://arxiv.org/abs/2606.02219) - [pdf](https://arxiv.org/pdf/2606.02219)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Symmetry-Aware 9D Pose Estimation with Sim(3)-Consistent Feature and Spherical Inception Convolution
- 作者：Panfei Cheng, Hongshan Yu, Wenrui Chen, Xiaojun Tang, Jian Liu, Naveed Akhtar
- 出版日期：2026-06-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[https://arxiv.org/abs/2606.02219](https://arxiv.org/abs/2606.02219)

### 一句话总结
本文提出了一种用于类别级物体9D姿态估计的方法，通过对称性感知模块和球面大核初始卷积融合特征，在基准和真实场景中达到最佳性能。

### 研究问题
现有实例级姿态估计方法难以泛化到未见物体，而类别级方法受限于非线性的Sim(3)空间学习复杂性和类内变化。如何更有效地进行类别级物体姿态估计？

### 核心思路/方法
1. **平移/尺度估计器**：利用大视觉模型（LVM）的语义通用性，通过对称性感知模块推断对称点，无需形状先验即可准确估计平移和尺寸。该结果作为旋转估计的预计算线索，降低Sim(3)空间学习难度。
2. **特征融合模块**：基于提出的球面大核初始卷积，融合LVM的语义特征与系统计算的几何特征，无需过大计算成本即可建模长距离依赖，提取类内变化中的关键姿态特征。

### 主要贡献
- 提出对称性感知的平移/尺度估计器，利用LVM消除形状先验需求。
- 设计球面大核初始卷积模块，实现高效的特征融合与长距离依赖建模。
- 在基准和真实场景中达到最佳性能，并开发了处理多样化物体的鲁棒机器人抓取系统。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：本文聚焦于机器人抓取中关键的姿态估计问题，提出了基于大视觉模型和新型卷积的方法，达到当前最佳性能。对于从事姿态估计、机器人操控或3D视觉的研究者具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Object pose estimation is a fundamental problem for an agent system to perceive or manipulate objects in images or videos. However, current instance-level methods struggle with generalization to unseen objects. Category-level methods seek to address this, but remain constrained by the complexities of learning in the non-linear Sim(3) space and intra-class variations. To address these challenges, We propose an effective method for category-level object pose estimation with two key innovations: (1) A translation/size estimator, featuring a semantic-guided symmetry-aware module that leverages robust generalization capabilities of a large vision model (LVM) to infer symmetry points, resulting in accurate translation and size without shape priors. This result serves as a precomputed cue for rotation estimation, thereby reducing the difficulty of learning in the non-linear Sim(3) space and laying a robust foundation for tackling the inherently more challenging rotation estimation. (2) A feature fusion module, based on our proposed spherical large-kernel inception convolution, fuses semantic features from the LVM with systematically computed geometric features to extract essential pose features from intra-class variations by modeling long-range dependencies without excessive computational cost. Built on these innovations, we achieve SOTA on benchmarks and real-world scenes, while developing a robust robotic picking system capable of handling diverse objects. Our code will be available at the project page: {\hypersetup{urlcolor=blue}https://panfei-cheng.github.io/SSH-Pose}.

</details>

#### 2026-06-01 - PerBite: A Curated Diagnostic Workflow for Bite-Aware Food Volume Estimation

**Authors:** Ahmad AlMughrabi, Farid Al-Areqi, David Fernández Gómez, Umair Haroon, Marc Bolaños, Ricardo Marques, Petia Radeva
**Links:** [abs](https://arxiv.org/abs/2606.02021) - [pdf](https://arxiv.org/pdf/2606.02021)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PerBite: A Curated Diagnostic Workflow for Bite-Aware Food Volume Estimation
- 作者：Ahmad AlMughrabi, Farid Al-Areqi, David Fernández Gómez, Umair Haroon, Marc Bolaños, Ricardo Marques, Petia Radeva
- 出版日期：2026-06-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.02021

### 一句话总结
提出一个基于前-后餐状态配对、结合分割与3D重建的完整工作流，在MetaFood挑战中取得第一，用于估计食物体积。

### 研究问题
能否信任视觉上合理的食物网格来估计已消耗食物的体积？即如何设计一个可靠的工作流来从用餐前后图像对中准确计算食物消耗体积。

### 核心思路/方法
1. 从MetaFood挑战中选取配对的餐前和餐后状态图像。
2. 使用SAM~3分割食物和盘子区域。
3. 用Hunyuan3D/SAM~3D生成无量纲食物网格。
4. 用盘子直径提供公制尺度；在Blender中移除盘子几何；对剩余网格进行孔洞填充、水密化并积分以估计体积。
5. MoGe-2仅在直接测量盘子不确定时作为初始盘直径估计的辅助线索，不作为主要尺度来源。

### 主要贡献
1. 在MetaFood CVPR 2026挑战中取得第一名，平均Chamfer距离8.31（34个网格，刚性ICP无尺度校正）。
2. 在17对餐前-餐后数据上，状态级体积MAPE为33.87%，消耗体积MAPE为53.74%，零单调性违规。
3. 提出应分别评估表面重建、公制尺度、受控网格清理、水密体积积分和物理消耗一致性等环节对膳食评估的影响。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：专注于特定饮食评估挑战（MetaFood）的工程方案，方法细节较多但实验样本量较小（34个网格，17对餐），主要适用于3D重建在饮食监控领域的应用研究者；对一般计算机视觉读者兴趣有限。

</details>

<details>
<summary>Abstract</summary>

Can a visually plausible food mesh be trusted to estimate the volume of consumed food? \method investigates this question using selected paired before- and after-consumption states from the MetaFood CVPR 2026 Continuous 3D Reconstruction While Eating Challenge. The submitted workflow follows a curated reconstruction protocol: SAM~3 segments the food and plate regions; Hunyuan3D/SAM~3D generates a dimensionless food mesh; the plate diameter provides the metric scale; the plate geometry is removed in Blender; and the remaining mesh is hole-filled, made watertight, and integrated to estimate volume. MoGe-2 is used only as an auxiliary cue for initial dish-diameter estimation when direct plate measurement is uncertain; it is not the primary scale source for the reported challenge result. \method ranks first, with an average Chamfer distance of 8.31 across 34 meshes using rigid ICP without scale correction. On 17 before- and after-pairs, it achieves 33.87\% state-level volume MAPE and zero monotonicity violations, while consumed-volume MAPE remains 53.74\%. The results show that surface reconstruction, metric scale, controlled mesh cleanup, watertight volume integration, and physical depletion consistency should be evaluated separately for dietary assessment. Source code and evaluation scripts will be available at \href{https://github.com/GCVCG/PerBite-CVPR-MetaFood-2026}{github.com/GCVCG/PerBite-CVPR-MetaFood-2026}.

</details>

#### 2026-06-01 - Closed-Form Pose Estimation of Endoluminal Medical Devices via Gradiometer-Based Electromagnetic Localization System

**Authors:** Zhiwei Wu, Jiahao Luo, Yubo Pu, Siyi Wei, Yuankai Chen, Jinhui Zhang
**Links:** [abs](https://arxiv.org/abs/2606.01946) - [pdf](https://arxiv.org/pdf/2606.01946)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Closed-Form Pose Estimation of Endoluminal Medical Devices via Gradiometer-Based Electromagnetic Localization System
- 作者：Zhiwei Wu, Jiahao Luo, Yubo Pu, Siyi Wei, Yuankai Chen, Jinhui Zhang
- 出版日期：2026-06-01
- 分类：3D Reconstruction & Multi-view Geometry; Embodied / Robotics / AR Applications
- 链接：arXiv: https://arxiv.org/abs/2606.01946

### 一句话总结
本文提出了一种基于梯度计的电磁定位系统（GELS），利用紧凑磁力计阵列作为准梯度计，通过闭式解析方法实现腔内医疗器械的六自由度位姿估计，无需预校准场图或初始猜测。

### 研究问题
如何在不依赖预校准工作空间场图、初始位姿猜测或校准激励源矩的条件下，通过嵌入式磁跟踪实现腔内医疗器械的实时、高精度六自由度位姿估计？

### 核心思路/方法
- 使用紧凑磁力计阵列作为嵌入式准梯度计，测量局部磁场和梯度张量。
- 利用欧拉齐次关系将测量量映射为源与阵列之间的位移，再通过多源Procrustes配准（至少三个非共线源）恢复阵列的朝向和位置。
- 算法仅需已知源位置和阵列几何结构，无需预校准场图、初始猜测或校准源矩。
- 恢复的位姿可作为移动磁参考框架，用于子级偶极子定位任务的概念验证。

### 主要贡献
1. 提出了GELS闭式跟踪框架，无需预校准场图或迭代优化，实现快速位姿估计。
2. 通过多源Procrustes配准方法，利用至少三个非共线源完成六自由度位姿恢复，降低了对源矩校准的依赖。
3. 在台架实验中展示了序列平均位置误差为10.80 mm–15.57 mm，最快更新率14.49 Hz，中位求解器运行时间172.00 μs。
4. 通过基于扰动的误差传播分析，揭示了传感器间不一致性和偶极子模型失配是主要精度限制因素，为未来传感器阵列和磁源设计提供了指导。

### 局限性
- 摘要未提供关于传感器阵列规模、实验环境多样性、活体实验验证、复杂运动场景下的鲁棒性等具体局限性信息。
- 方法目前仅通过台架实验验证，未提及人体或动物体内实验。摘要未明确给出所有误差来源的量化对比。

### 阅读优先级
**中**
理由：该工作针对腔内医疗器械的电磁定位提出了一种新颖的闭式解析方法，规避了传统方法中预校准或迭代优化的需求，具有理论创新和实际应用潜力。但由于摘要中实验规模有限（误差范围较大，更新率中等），且未提供与现有方法的对比，更适合对磁定位技术或医疗机器人领域有直接兴趣的读者深入阅读，而非紧急推荐给所有计算机视觉研究者。

</details>

<details>
<summary>Abstract</summary>

Embedded magnetic tracking holds highly attractive prospects for remote navigation of endoluminal medical devices. However, existing six-degree-of-freedom pose recovery approaches often require pre-calibrated workspace field maps or iterative nonlinear optimization. This letter presents a Gradiometer-Based Electromagnetic Localization System (GELS), a closed-form tracking framework that uses a compact magnetometer array as an embedded quasi-gradiometer to estimate local magnetic fields and gradient tensors. These quantities are mapped by the Euler homogeneous relation to displacements between source and array, from which multi-source Procrustes registration recovers the array orientation and position using at least three non-collinear sources. The algorithm requires known source positions and array geometry, but no pre-calibrated workspace field maps, initial pose guesses, or calibrated excitation-source moments. The recovered pose also enables a proof-of-concept sub-level dipole localization task by serving as a mobile magnetic reference frame. Benchtop experiments across sensor-array configurations and excitation modes demonstrate sequence-averaged position errors of \SI{10.80}{\milli\meter}--\SI{15.57}{\milli\meter}, a fastest update rate of \SI{14.49}{\hertz}, and a median solver runtime of \SI{172.00}{\micro\second}. A perturbation-based error propagation analysis further identifies inter-sensor inconsistency and dipole-model mismatch as the dominant accuracy limits, thereby informing future sensor array and magnetic source design for further reducing pose-estimation error.

</details>

#### 2026-06-01 - SCAPO: Self-Supervised Category-Level Articulated Pose Estimation from a Single 3D Observation

**Authors:** Can Zhang, Gim Hee Lee
**Links:** [abs](https://arxiv.org/abs/2606.01940) - [pdf](https://arxiv.org/pdf/2606.01940)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SCAPO: Self-Supervised Category-Level Articulated Pose Estimation from a Single 3D Observation
- 作者：Can Zhang, Gim Hee Lee
- 出版日期：2026-06-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.01940

### 一句话总结
提出一种名为SCAPO的自监督框架，仅凭单张RGB-D观测即可估计类别的铰接物体几何、部件分割及关节参数，无需真实标签或类别特定模型。

### 研究问题
如何从单次3D观测中，无需标注数据和类别模型，自监督地估计类别级别铰接物体的几何结构、刚性部件分割以及关节枢轴、轴线和铰接状态。

### 核心思路/方法
1.  **全局位姿解耦**：使用SE(3)等变的矢量神经元自编码器，将不同实例的全局位姿分离，并将它们对齐到一个共享的规范空间。
2.  **部件运动建模**：在对齐的形状上，设计一个关节感知的混合蒙皮模块来建模部件运动。
3.  **自监督学习**：通过观测形状与规范形状之间的循环重建，以及使用可学习规范模板（解耦共享类别几何与实例特定残差形状）的跨空间对齐来学习该表示。

### 主要贡献
- 提出了一个完全自监督的框架SCAPO，能从单次3D观测中恢复铰接类别物体的部件结构和精确关节参数。
- 设计了SE(3)等变自编码器用于姿势解耦与规范对齐，以及关节感知混合蒙皮模块用于运动建模。
- 在合成和真实铰接物体数据集上，该方法在部件结构和关节参数恢复上超越了所有自监督基线。

### 局限性
摘要未提供关于局限性的信息。

### 阅读优先级
**高**
理由：该工作关注“单张3D观测”、“自监督”、“铰接物体”这几个关键且具有挑战性的组合，并取得了超越自监督基线的结果。思路清晰，结合了等变网络与蒙皮模型的创新，且发布于2026年，在3D感知与机器人操作领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing methods for category-level object articulation from a single 3D observation often rely on dense supervision, multi-frame inputs, or CAD templates, and still struggle to disentangle geometry from articulation or to recover explicit joint parameters. We propose SCAPO, a self-supervised framework that estimates canonical geometry, rigid part segmentation, and joint pivots, axes, and articulation states from a single RGB-D observation without ground-truth labels or category-specific models. Our SCAPO first uses an SE(3)-equivariant vector-neuron autoencoder to factor out global pose and align diverse instances into a shared canonical space. On this aligned shape, a joint-aware blend-skinning module is then designed to model part motion. We learn this representation through cycle reconstruction between observed and canonical shapes and cross-space alignment with a learnable canonical template that decouples shared category geometry from instance-specific residual shape. Experiments on synthetic and real articulated-object datasets show that our SCAPO recovers consistent part structure and accurate articulation parameters and outperforms all self-supervised baselines.

</details>

### 2026-05

#### 2026-05-31 - ActMVS: Active Scene Reconstruction with Monocular Multi-View Stereo

**Authors:** Guo Pu, Yixuan Han, Zhouhui Lian
**Links:** [abs](https://arxiv.org/abs/2606.01367) - [pdf](https://arxiv.org/pdf/2606.01367)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, scene reconstruction, multi-view stereo, stereo depth, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ActMVS: Active Scene Reconstruction with Monocular Multi-View Stereo
- 作者：Guo Pu, Yixuan Han, Zhouhui Lian
- 出版日期：2026-05-31
- 分类：3D Reconstruction & Multi-view Geometry（三维重建与多视图几何）
- 链接：抽象页: https://arxiv.org/abs/2606.01367 ; PDF: https://arxiv.org/pdf/2606.01367

### 一句话总结
本文提出ActMVS，**首个面向单目主动场景重建的框架**，通过集成视图因子图构建与全局深度优化，实现在线生成全局一致的高质量密集深度图，使单目机器人/UAV能在导航中维持可靠的占据地图。

### 研究问题
主动场景重建中，如何**仅使用单目视觉（而非深度传感器）**实现实时、全局一致的密集深度估计，以支持机器人/UAV的自主轨迹规划与碰撞安全导航。

### 核心思路/方法
1. **视图因子图构建**：在线构建因子图，利用多视图几何约束引导稠密深度预测（Multi-View Stereo）。
2. **全局深度优化**：对预测的深度图进行全局优化，确保跨帧一致性。
3. **集成流程**：将上述两步结合，使单目平台能**实时**生成高质量密集深度图，并据此更新占据地图用于轨迹规划。

### 主要贡献
- 提出**首个单目主动重建框架**ActMVS，摆脱对深度传感器的依赖。
- 解决现有单目方法只能离线、无法提供高速全局一致深度的问题。
- 在Replica数据集上，**性能可媲美RGB-D方法**（具体指标摘要未提供）。

### 局限性
摘要未提供足够信息。例如：未提及在真实机器人或UAV平台上的实时性能、计算资源需求、对光照或纹理条件的鲁棒性，以及与其他单目方法的详细对比结果。

### 阅读优先级
**高**  
理由：该工作填补了“单目主动场景重建”领域的方法空白，且声称性能与RGB-D方法竞争，对降低机器人/UAV硬件成本、推动视觉智能有重要意义。摘要虽未提供完整实验细节，但问题定义和方法创新性明确，值得深入阅读。

</details>

<details>
<summary>Abstract</summary>

Active scene reconstruction enables robots/UAVs to autonomously plan trajectories and reconstruct environments without costly manual data acquisition. Unlike passive methods, active reconstruction requires real-time construction of high-confidence occupancy maps for collision-free navigation. Existing approaches rely on depth sensors for occupancy map updates, increasing platform cost and weight. To advance spatial intelligence, we aim for a vision-only monocular solution. However, current monocular scene reconstruction methods operate offline and fail to deliver globally consistent dense depth at the frame rates required for robots/UAVs navigation. To bridge this gap, we introduce ActMVS, the first framework for monocular active reconstruction. Our framework integrates a view factor graph construction for informed Multi-View Stereo depth prediction, along with a global depth optimization, to enable the online generation of high-quality, globally consistent dense depth maps. This enables monocular robots/UAVs to maintain reliable occupancy maps for safe trajectory planning during reconstruction. Experiments on Replica datasets demonstrate performance competitive with RGB-D methods. Our code and data are available at https://github.com/TrickyGo/ActMVS.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-02 - SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation

**Authors:** Qingpo Wuwu, Xiaobao Wei, Peng Chen, Nan Huang, Zhongyu Zhao, Hao Wang, Ming Lu, Ningning Ma, Shanghang Zhang
**Links:** [abs](https://arxiv.org/abs/2606.03909) - [pdf](https://arxiv.org/pdf/2606.03909)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic scene reconstruction, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, scene representation, rendering, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation
- 作者：Qingpo Wuwu, Xiaobao Wei, Peng Chen, Nan Huang, Zhongyu Zhao, Hao Wang, Ming Lu, Ningning Ma, Shanghang Zhang
- 出版日期：2026-06-02T17:06:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.03909；PDF：https://arxiv.org/pdf/2606.03909

### 一句话总结
SparseStreet提出一种针对街景的3D高斯溅射压缩框架，通过可学习的节点剪枝和背景压缩，在几乎不降低质量的前提下实现高达80%的压缩率，并保持动态物体高保真度。

### 研究问题
现有3D高斯溅射在街景重建中需要使用大量高斯元来捕捉细节，导致存储成本高和渲染速度慢，需要一种能够减少冗余、提升效率的方法。

### 核心思路/方法
1. **节点可学习剪枝策略**：系统性地移除贡献度低的高斯元，同时保留视觉关键区域。
2. **背景压缩**：在场景表示稳定后，进一步减少静态区域的冗余。
3. 核心目标是保留动态物体（如车辆、行人）的几何和外观，同时显著降低高斯元总数。

### 主要贡献
- 提出一种专为街景设计的通用压缩框架SparseStreet。
- 在Waymo和nuScenes数据集上实现高达80%的压缩率，且质量退化极小。
- 实现资源高效、高保真的动态场景重建。

### 局限性
摘要未提供足够信息：未讨论方法在极端场景（如大量快速运动物体或复杂光照）下的表现，也未提及与现有方法在计算时间上的对比细节。

### 阅读优先级
**高**。理由：该工作针对街景实时仿真的实际部署需求，提出显著的压缩效率（80%），且已在两个主流数据集验证；如果读者关注自动驾驶、场景重建或实时渲染的资源优化，该论文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting has shown promising results in street scene reconstruction, existing methods require massive numbers of Gaussian primitives to capture fine details, leading to prohibitive storage costs and slow rendering speeds. We observe that dynamic objects (e.g., vehicles and pedestrians) demand high-fidelity representations to maintain temporal consistency, while static background regions often contain substantial redundancy. Motivated by this, we propose SparseStreet, a general compression framework specifically designed for street scenes. First, we introduce a node-based learnable pruning strategy that systematically removes low-contributing Gaussian primitives while preserving visually critical regions. Second, after the scene representation stabilizes, we apply background compression, further reducing redundancy in static regions. Our method effectively preserves the geometry and appearance of dynamic objects while significantly reducing the total number of Gaussian primitives. Extensive experiments on the Waymo and nuScenes demonstrate that SparseStreet achieves up to 80% compression ratio with minimal quality degradation, enabling resource-efficient, high-fidelity dynamic scene reconstruction. Project website: https://sparsestreet.github.io/.

</details>

#### 2026-06-02 - MLP Splatting: Object-Centric Neural Fields

**Authors:** Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison
**Links:** [abs](https://arxiv.org/abs/2606.03877) - [pdf](https://arxiv.org/pdf/2606.03877)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MLP Splatting: Object-Centric Neural Fields
- 作者：Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison
- 出版日期：2026-06-02T16:46:16Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03877

### 一句话总结
MLP-Splatting提出用多个紧凑的局部MLP作为“神经基元”来替代传统高斯基元或全局辐射场，实现物体级别可分解的、快速的逼真新视图合成。

### 研究问题
现有3D表示方法（如3D高斯泼溅和NeRF）在实现逼真合成的同时难以自然分解场景中的物体，通常需要额外的分割或分组才能进行物体级操作。

### 核心思路/方法
该方法将每个场景基元建模为一个独立的紧凑MLP，该MLP具有局部的空间支持，能够预测辐射度和不透明度。渲染时通过稀疏的体素合成（沿射线与基元的交互）高效进行。基元仅通过RGB监督即可学习，自动对应于局部场景区域（通常为物体或物体部件），从而无需分割掩码即可通过选择少量基元实现交互式物体级编辑。

### 主要贡献
1. 提出MLP-Splatting，使用少量表达力强的神经基元实现场景分解，同时保持逼真的新视图合成。
2. 相比底层高斯基元或单个全局辐射场，神经基元在保持局部性的同时提供更强的表达能力。
3. 通过可选的语义特征蒸馏，支持开放词汇的场景交互和开放集实例分割。
4. 实验表明，与语义3DGS方法相比，内存使用量显著降低（1/15×），渲染速度提升（3×）。

### 局限性
摘要未提供足够信息。未提及该方法在基元数量、训练效率、复杂场景鲁棒性等方面的具体局限。

### 阅读优先级
**高**。理由：该方法在基于神经辐射场的物体级分解与高效渲染方面提出了创新方案，与当前热门的3D高斯泼溅和NeRF范式直接相关，且展示了明显的性能优势（内存和速度）。同时支持开放词汇交互，具有广泛的应用前景。

</details>

<details>
<summary>Abstract</summary>

3D representations are fundamental to scene rendering, understanding, and interaction. Recent approaches, such as 3D Gaussian Splatting and Neural Radiance Fields, achieve impressive photorealistic novel-view synthesis, but lack the ability to easily decompose scene elements into a few primitives, requiring additional segmentation or grouping for object-level manipulation. We present MLP-Splatting, a method that enables scene decomposition via a few expressive light-field primitives while providing photorealistic novel-view synthesis. MLP-Splatting models each primitive as an independent compact MLP with localized spatial support that predicts radiance and opacity. In contrast to low-level Gaussian primitives or a single global radiance field, our neural primitives provide greater expressive capacity while remaining spatially localized. Rendering is performed through efficient sparse volumetric compositing over ray-primitive interactions. Our primitives are supervised using RGB supervision alone, which yields primitives that represent local scene regions often corresponding to objects or object parts, enabling interactive object-level editing without segmentation masks by selecting a handful of primitives. Our method, augmented with optional semantic feature distillation, enables open-vocabulary scene interaction and open-set instant segmentation. Compared to state-of-the-art methods, we achieve substantially lower memory usage (1/15$\times$) and faster rendering (3$\times$), as we show in our experiments compared to semantic 3DGS methods. Project Page: https://shinjeongkim.com/mlp-splatting

</details>

#### 2026-06-02 - GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation

**Authors:** Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li
**Links:** [abs](https://arxiv.org/abs/2606.03682) - [pdf](https://arxiv.org/pdf/2606.03682)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation
- 作者：Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03682

### 一句话总结
本文提出GN0，一个统一的数据、模拟与学习框架，通过大规模数据集、高保真仿真平台和强化学习驱动的导航基础模型，在视觉语言导航任务上达到超越现有方法的性能。

### 研究问题
视觉语言导航（VLN）系统中，导航数据的可用性和质量有限，导致模型的泛化能力和长程任务执行能力不足。

### 核心思路/方法
1. **数据生成**：策展多样化3D场景，并开发自动化管线，构建大规模GN-Matrix数据集。
2. **仿真平台**：基于3D高斯泼溅（3DGS）引擎，搭建支持交互漫游和碰撞感知导航的高保真模拟平台。
3. **基准评估**：提出首个基于鸟瞰图（BEV）的基准GN-Bench，集成动态3DGS虚拟角色用于人机交互评估。
4. **模型训练**：采用强化学习驱动的导航基础模型BAE（Break and Establish）。先进行监督学习，再通过DAgger算法让模型接触 rollout 状态，打破狭窄的专家分布，并支持下游RL探索。
5. **表示学习**：GN-BAE将高保真3DGS渲染的BEV表示作为紧凑记忆，以解锁视觉语言模型中的潜在空间推理。

### 主要贡献
1. 提出GN-Matrix数据集，涵盖大规模多样化3D场景和自动化的导航数据生成管线。
2. 构建高保真仿真平台，支持交互式漫游和碰撞感知导航。
3. 引入首个基于BEV的基准GN-Bench，具备动态3DGS虚拟角色的人机交互评估能力。
4. 开发RL驱动的导航基础模型BAE，通过监督学习与DAgger算法结合，提升模型在分布外状态下的探索能力。
5. 统一了基于地图和无地图的任务（如指令跟随、人跟随、目标导航），并在GN-Bench和VLN-CE上达到超越现有最优方法的表现。

### 局限性
摘要未提供足够信息。摘要未提及模型的计算开销、对特定场景或任务的失败案例、数据集的潜在偏差、仿真到真实场景的迁移效果，以及动态3DGS虚拟角色的真实性局限。

### 阅读优先级
中  
理由：该工作提出了一个涵盖数据、仿真、评估和学习的统一框架，在VLN领域具有系统性的创新，适合对具身智能、导航和强化学习感兴趣的研究者阅读。但摘要未提供详细的定量实验结果或深入的方法消融分析，优先程度中等。

</details>

<details>
<summary>Abstract</summary>

Embodied navigation connects intelligent agents with the physical world and is fundamental for general robotic intelligence. Limited availability and quality of navigation data have constrained Vision-and-Language Navigation (VLN) systems' generalization and long-horizon capabilities. To address this, we curate diverse 3D scenes and develop an automated pipeline for large-scale navigation data, resulting in the GN-Matrix dataset. Building on a 3D Gaussian Splatting (3DGS) engine, we introduce a high-fidelity simulation platform supporting interactive roaming and collision-aware navigation. We further propose GN-Bench, the first BEV-based benchmark incorporating dynamic 3DGS avatars for human-robot interaction evaluation. To leverage the simulator, we develop an RL-driven navigation foundation model, Break and Establish (BAE). After supervised learning, DAgger exposes the model to rollout-induced states, breaking narrow expert-centric distributions and enabling downstream RL exploration. This unified VLN paradigm integrates map-based and map-free tasks, including instruction following, human following, and goal navigation. GN-BAE formalizes high-fidelity 3DGS-rendered Bird's Eye View representations as compact memory, unlocking latent spatial reasoning in VLMs. Extensive evaluations on GN-Bench and VLN-CE show that GN0 outperforms state-of-the-art VLN methods. Overall, GN-Matrix offers a unified framework spanning data, simulation, and learning, advancing embodied navigation in research and industrial applications.

</details>

#### 2026-06-02 - UnsOcc: 3D Semantic Occupancy Prediction in Unstructured Scene via Rendering Fusion

**Authors:** Ye Wu, Ruiqi Song, Baiyong Ding, Nanxin Zeng, Junjie Cheng, Yunfeng Ai
**Links:** [abs](https://arxiv.org/abs/2606.03581) - [pdf](https://arxiv.org/pdf/2606.03581)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UnsOcc: 3D Semantic Occupancy Prediction in Unstructured Scene via Rendering Fusion
- 作者：Ye Wu, Ruiqi Song, Baiyong Ding, Nanxin Zeng, Junjie Cheng, Yunfeng Ai
- 出版日期：2026-06-02T12:50:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03581

### 一句话总结
本文提出UnsOcc，一种针对非结构化场景（如露天矿场）的多模态3D语义占用预测框架，通过渲染融合模块和基于高斯泼溅的细节感知辅助监督，提升模型在稀疏场景下的预测鲁棒性。

### 研究问题
非结构化场景（如不规则障碍物、稀疏布局）中，直接应用3D语义占用预测时面临两个困难：场景稀疏性阻碍有效的跨模态融合，以及长尾分布问题导致预测性能下降。

### 核心思路/方法
- 构建一个专用的露天矿场非结构化场景数据集。
- 提出渲染融合模块（RenderFusion），通过双向渲染监督增强跨模态特征对齐。
- 提出细节感知辅助监督方法（GSRefinement），基于高斯泼溅（Gaussian Splatting）将稀疏3D占用预测投影为密集2D语义分割图，从而对长尾类别进行有效监督。

### 主要贡献
- 提出UnsOcc，一个针对非结构化场景的多模态3D语义占用预测框架。
- 引入RenderFusion模块，通过双向渲染监督改进跨模态融合。
- 提出GSRefinement方法，利用高斯泼溅生成密集2D语义图以辅助长尾类别监督。
- 在露天矿场数据集和nuScenes数据集上，所提方法显著优于现有最先进方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对自动驾驶中非结构化场景这一有挑战性的实际应用问题（如矿场），提出了新颖的渲染融合与高斯泼溅辅助监督方法，并在两个数据集上验证了有效性。目标读者若关注多模态融合、3D语义占用预测或非标准场景处理，则该论文具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Unstructured scenes present unique challenges for autonomous driving, as irregular obstacles and sparse scene layouts undermine the effectiveness of traditional perception methods such as 3D object detection. 3D semantic occupancy prediction has emerged as a prominent focus due to its ability to provide dense spatial representations by assigning semantic labels to individual voxels in 3D space. However, directly applying 3D semantic occupancy prediction to unstructured scenes remains challenging because scene sparsity hinders effective cross-modal fusion and the more severe long-tail distribution in these scenarios further degrades prediction performance. To validate the effectiveness of our approach, we construct a dedicated dataset of unstructured scenes collected from open-pit mines. Based on this, we propose UnsOcc, a multi-modal 3D semantic occupancy prediction framework that improves robustness in unstructured environments. At its core, we introduce a rendering-based fusion module, RenderFusion, which enhances cross-modal feature alignment through bidirectional rendering supervision. Furthermore, we propose GSRefinement, a detail-aware auxiliary supervision method based on Gaussian Splatting that projects sparse 3D occupancy predictions into dense 2D semantic segmentation maps, enabling effective supervision for long-tail categories. Extensive experiments on both the open-pit mine dataset and the nuScenes dataset demonstrate that our method significantly outperforms existing state-of-the-art approaches.

</details>

#### 2026-06-02 - Characterizing Detectability in 3DGS Poisoning: A Stage-wise Benchmark

**Authors:** Quoc-Anh Bui-Huynh, Thanh Duc Ngo, Xue Geng, Kaixin Xu, Wang Zhe, Xulei Yang, Ngai-Man Cheung
**Links:** [abs](https://arxiv.org/abs/2606.03499) - [pdf](https://arxiv.org/pdf/2606.03499)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Characterizing Detectability in 3DGS Poisoning: A Stage-wise Benchmark
- 作者：Quoc-Anh Bui-Huynh, Thanh Duc Ngo, Xue Geng, Kaixin Xu, Wang Zhe, Xulei Yang, Ngai-Man Cheung
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03499

### 一句话总结
本文提出了Poison-3DGS基准，系统地研究了3DGS重建管线中不同阶段对攻击痕迹的可检测性差异。

### 研究问题
在3DGS面临多种投毒攻击（如幻影物体注入、计算成本放大、后验水印）的背景下，如何从检测角度理解不同攻击在不同重建阶段（多视图图像、几何、训练动态、高斯参数）留下的可检测信号特性？

### 核心思路/方法
1. 构建Poison-3DGS基准：涵盖多种场景和攻击类型，收集并利用多阶段中间表示（多视图图像、几何、训练动态、高斯参数）作为检测特征。
2. 进行系统性的阶段依赖性可检测性分析：比较不同攻击在不同阶段留下的取证信号强度，评估检测效果随阶段变化的情况。

### 主要贡献
- 提出了首个用于阶段化检测特性分析的标准基准Poison-3DGS。
- 揭示了可检测性在不同阶段存在显著变化，且没有一个阶段在所有攻击类型中始终最优。
- 指出后期阶段（如训练动态、高斯参数统计）能提供早期阶段无法捕获的强检测线索。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦于3DGS安全防御中的检测问题，针对性强，但属于基准构建与特性分析类研究，适合对3DGS安全或可解释性感兴趣的专业研究者阅读；对一般读者或应用导向需求者优先级不高。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has rapidly emerged as a leading representation for real-time novel view synthesis, but recent work shows it is vulnerable to diverse poisoning attacks, including illusory object injection, computation cost amplification, and post hoc model watermarking. Despite this expanding threat surface, existing studies focus mainly on attack success, while defense and detection remain underexplored. From a detection perspective, a key challenge and opportunity arise from the multi-stage nature of the 3DGS reconstruction pipeline, which produces heterogeneous intermediate representations. Forensic signals for detecting poisoning are inherently stage dependent: an attack introduced at one stage may produce signals that emerge only at later stages. This motivates a stage-wise view of detectability that goes beyond single-stage evaluation. We introduce Poison-3DGS, a benchmark for stage-wise characterization of poisoning detection in 3DGS. It exposes stage-specific artifacts, including multi-view images, geometry, training dynamics, and Gaussian parameters, across a diverse set of scenes and attacks. Using it, we conduct a systematic study of detectability across pipeline stages. Our analysis reveals several insights. First, detectability varies significantly across stages, and no single stage consistently dominates across attack types. Second, different attacks exhibit distinct stage-specific forensic signals, so detection effectiveness depends critically on where signals are observed. Third, later-stage signals such as training dynamics and Gaussian parameter statistics provide strong cues not observable at earlier stages. Overall, our work provides a principled benchmark and the first systematic characterization of stage-dependent detectability in 3DGS, offering a foundation for future research on robust and reliable 3DGS systems.

</details>

#### 2026-06-02 - FreeStreamGS: Online Feed-forward 3D Gaussian Splatting from Unposed Streaming Inputs

**Authors:** Ruiyang Chen, Feiran Li, Chu Zhou, Zonglin Li, Zhanyu Ma, Heng Guo
**Links:** [abs](https://arxiv.org/abs/2606.03254) - [pdf](https://arxiv.org/pdf/2606.03254)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FreeStreamGS: Online Feed-forward 3D Gaussian Splatting from Unposed Streaming Inputs
- 作者：Ruiyang Chen, Feiran Li, Chu Zhou, Zonglin Li, Zhanyu Ma, Heng Guo
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03254

### 一句话总结
该论文提出一种名为FreeStreamGS的在线前馈框架，能够在无位姿的流式输入下实现高效、高质量的新视角合成（NVS），其渲染质量可与依赖未来帧的离线前馈3DGS方法相媲美。

### 研究问题
如何从无位姿的流式图像输入中，在线进行高效、高质量的新视角合成，克服传统前馈3DGS方法在流式场景下因多视图一致性要求而出现的渲染退化问题。

### 核心思路/方法
1. 提出一个在线前馈框架，不依赖未来帧信息。
2. 引入**解耦内参恢复头**：用于消除累积的相机内参偏置，防止长时间流式处理中的场景尺度抖动。
3. 引入**动态点细化偏移策略**：通过放松刚性反投影约束，来修正耦合的位姿-深度漂移。

### 主要贡献
1. 首次提出了一个健壮的在线前馈框架，用于从无位姿流式输入中高效、高质量地实现新视角合成。
2. 设计了解耦内参恢复头和动态点细化偏移机制，分别解决了内参累积偏置与位姿-深度耦合漂移问题。
3. 实验表明，该方法能获得与最先进离线前馈3DGS方法竞争的渲染质量，且无需访问未来帧。

### 局限性
摘要未提供足够信息，未提及该方法在极端快速运动、严重遮挡、低纹理区域或计算资源受限条件下的具体表现。

### 阅读优先级
**高**  
理由：该工作针对在线流式新视角合成这一实际应用场景中的核心难点（多视图一致性退化），提出了明确且创新的解决方案，并能与离线方法竞争，对3DGS实时应用具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) allows efficient and high-fidelity novel view synthesis (NVS) from an offline recorded image sequence. However, achieving online NVS from streaming and unposed image inputs remains challenging. Although online feed-forward geometric estimation methods have been proposed for streaming depth and point cloud recovery, they cannot be adapted to NVS due to severe rendering artifacts. This is because NVS demands stricter multi-view consistency in Gaussian scales and pose-geometry alignment; even minor deviations would accumulate over time and visibly degrade rendering quality. To this end, we propose FreeStreamGS, a robust online feed-forward framework for efficient and high-quality NVS. We introduce two key mechanisms: a Decoupled Intrinsic Recovery Head that removes cumulative camera intrinsic bias and prevents scene scale jitter during long-term streaming, and a Dynamic Point Refinement Offset strategy that relaxes rigid unprojection to correct coupled pose-depth drift. Extensive experiments show that FreeStreamGS achieves rendering quality competitive with state-of-the-art offline feed-forward 3DGS methods, despite operating without access to future frames.

</details>

#### 2026-06-02 - KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis

**Authors:** Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy
**Links:** [abs](https://arxiv.org/abs/2606.03120) - [pdf](https://arxiv.org/pdf/2606.03120)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis
- 作者：Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03120

### 一句话总结
本文提出KC-3DGS，通过在3DGS训练中引入基于小波域的自然图像统计约束（峰度、跨频带协方差等），改善视角合成的感知质量，尤其在稀疏视图场景下缓解过平滑和结构伪影。

### 研究问题
标准3DGS使用像素空间损失（L1、SSIM）仅约束整体重建误差，导致误差在不同频率尺度上重新分布，造成过平滑和结构伪影，在稀疏视图设置中尤为严重。本文旨在解决这一频率细节缺失问题。

### 核心思路/方法
提出KC-3DGS，在3DGS的可微渲染管道中增加三个小波域约束：
1. 多尺度小波系数对齐损失：显式惩罚缺失的高频细节。
2. 有监督峰度集中损失：鼓励渲染图像匹配真实图像的重尾频率统计特性。
3. 跨频带协方差惩罚：促进频率特化。
理论分析表明，像素空间损失允许一类在小波重分布下不可区分的扰动，而联合目标函数排除了退化解。

### 主要贡献
- 提出结合自然图像统计的小波域监督，增强3DGS的感知保真度。
- 理论证明像素损失存在小波重分布下的不可区分扰动，并验证联合目标可排除退化解。
- 实验在MipNeRF360、Tanks&Temples、MVImgNet、DeepBlending及WRIVA-ULTRRA等数据集上展示了一致的感知质量提升。在WRIVA-ULTRRA上DreamSim提升9.48%，同时在PSNR、SSIM、LPIPS上也有改进。稀疏视图（12张训练图像）下PSNR提升至0.5 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法作为即插即用正则化策略，可直接集成到现有3DGS管线中，显著提升感知质量，并在稀疏视图等困难场景中表现优异。对于从事神经渲染、视角合成或3D场景重建的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel view synthesis by representing scenes as collections of anisotropic Gaussians optimized via differentiable rasterization. However, standard pixel-space losses (L1, SSIM) constrain only aggregate reconstruction error, permitting the optimization to redistribute error across frequency scales. This leads to oversmoothing and structural artifacts, particularly in sparse-view settings where supervision is limited. We propose KC-3DGS, which augments 3DGS training with wavelet-domain supervision based on natural image statistics. Our method combines three components: (1) a multi-scale wavelet coefficient alignment loss that explicitly penalizes missing high-frequency detail, (2) a supervised kurtosis concentration loss that encourages rendered images to match the heavy-tailed frequency statistics of ground-truth images, and (3) a cross-band covariance penalty that promotes frequency specialization. We provide theoretical analysis showing that pixel-space losses admit a family of indistinguishable perturbations under wavelet redistribution, and that our joint objective excludes degenerate solutions. Experiments across MipNeRF360, Tanks&Temples, MVImgNet, DeepBlending, and WRIVA-ULTRRA demonstrate consistent improvements in perceptual quality. On the challenging WRIVA-ULTRRA outdoor dataset, KC-3DGS achieves a 9.48% improvement in DreamSim while also improving PSNR, SSIM, and LPIPS. In sparse-view settings with only 12 training images, our method improves PSNR by up to 0.5 dB on MipNeRF360 while maintaining perceptual quality. The approach integrates seamlessly into existing 3DGS pipelines as a plug-and-play regularization strategy.

</details>

#### 2026-06-01 - The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset

**Authors:** Richard Schwarzkopf, Fabian Immel, Alexander Blumberg, Jonas Merkert, Nils Rack, Kaiwen Wang, Fabian Konstantinidis, Julian Truetsch, Carlos Fernandez, Annika Bätz, Kevin Rösch, Marlon Steiner, Willi Poh, Yinzhe Shen, Royden Wagner, Felix Hauser, Dominik Strutz, Jaime Villa, Gleb Stepanov, Holger Caesar, Ömer Şahin Taş, Frank Bieder, Jan-Hendrik Pauls, Christoph Stiller
**Links:** [abs](https://arxiv.org/abs/2606.02956) - [pdf](https://arxiv.org/pdf/2606.02956)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, novel view synthesis, view synthesis, embodied AI, autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset  
- 作者：Richard Schwarzkopf, Fabian Immel, Alexander Blumberg, Jonas Merkert, Nils Rack, Kaiwen Wang, Fabian Konstantinidis, Julian Truetsch, Carlos Fernandez, Annika Bätz, Kevin Rösch, Marlon Steiner, Willi Poh, Yinzhe Shen, Royden Wagner, Felix Hauser, Dominik Strutz, Jaime Villa, Gleb Stepanov, Holger Caesar, Ömer Şahin Taş, Frank Bieder, Jan-Hendrik Pauls, Christoph Stiller  
- 出版日期：2026-06-01  
- 分类：神经场景表示与渲染（主要），具身/机器人/AR应用（次要）  
- 链接：abstract: https://arxiv.org/abs/2606.02956; pdf: https://arxiv.org/pdf/2606.02956  

### 一句话总结  
KITScenes Multimodal 是一个高保真、多模态的欧洲自动驾驶数据集，提供首个公开的完整3D交通元素HD地图，并引入四项空间学习基准。

### 研究问题  
现有自动驾驶数据集在传感器精度、地图完整性和地理多样性方面存在不足，限制了场景理解与空间学习的发展。

### 核心思路/方法  
- 构建一套完全同步的高保真传感器套件，包括高分辨率全局快门相机、超过400米探测距离的激光雷达、4D成像雷达和冗余GNSS/INS定位系统。  
- 制作目前公开传感器数据集中最完整的HD地图：首次将所有驾驶相关交通元素（如交通灯）以3D形式映射，达到重投影精确级别，并包含完整拓扑连接。  
- 数据集在街道布局不规则和混合交通模式的城市中采集，以补充现有数据集的地理多样性。  
- 提出四个基准任务：在线HD地图构建、远距离深度估计、新颖视角合成和端到端驾驶，旨在推进具身AI的空间学习。

### 主要贡献  
- 提供了一个高保真、多模态的自动驾驶数据集，传感器性能优于现有数据集。  
- 公开了首个具备完整3D交通元素和拓扑连接的高清地图。  
- 通过采集欧洲不规则街道布局的城市数据，增强了地理多样性。  
- 引入四个促进空间学习的基准任务，覆盖建图、深度估计、视图合成和驾驶控制。

### 局限性  
摘要未提供足够信息：未提及数据集规模（如样本数、序列长度）、具体传感器规格、标注成本、潜在偏差（如天气或光照条件覆盖）或与现有数据集的定量对比结果。

### 阅读优先级  
**高**  
理由：该数据集在传感器精度、地图完整性和基准多样性方面具有显著创新，尤其适用于研究高保真场景理解、空间学习及端到端自动驾驶的学者和工程师。

</details>

<details>
<summary>Abstract</summary>

Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity. We present KITScenes Multimodal, a European dataset built around high-fidelity sensors and maps. Our fully synchronized sensor suite combines high-resolution global-shutter cameras, long-range lidar beyond 400m, 4D imaging radar, and redundant GNSS/INS localization. Our HD maps are, to our knowledge, the most complete of any sensor dataset, validated through autonomous driving trials on open-source software. For the first time in a public dataset, all driving-relevant traffic elements, such as traffic lights, are mapped in 3D to a reprojection-accurate level with full topological connectivity. Recorded in cities with irregular street layouts and mixed traffic modes, our dataset complements existing datasets by broadening the available geographic diversity. We also introduce four benchmarks, each advancing spatial learning for embodied AI: online HD map construction, long-range depth estimation, novel view synthesis, and end-to-end driving. Project page: https://kitscenes.com/

</details>

#### 2026-06-01 - VEDAL: Variational Error-Driven Asynchronous Learning for 3D Gaussian Splatting Pruning

**Authors:** Aoduo Li, Jiancheng Li, Huan Ye, Hongjian Xu, Shiting Wu, Xiujun Zhang, Zimeng Li, Xuhang Chen
**Links:** [abs](https://arxiv.org/abs/2606.02346) - [pdf](https://arxiv.org/pdf/2606.02346)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VEDAL: Variational Error-Driven Asynchronous Learning for 3D Gaussian Splatting Pruning
- 作者：Aoduo Li, Jiancheng Li, Huan Ye, Hongjian Xu, Shiting Wu, Xiujun Zhang, Zimeng Li, Xuhang Chen
- 出版日期：2026-06-01
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：摘要: https://arxiv.org/abs/2606.02346 ；PDF: https://arxiv.org/pdf/2606.02346

### 一句话总结
VEDAL提出了一种基于变分自由能最小化的3D高斯剪枝框架，通过异步激活的预测误差门控机制和可学习先验的变分不确定性头，在保持实时渲染速度（185 FPS）的同时实现了5.2倍压缩，PSNR仅下降0.31 dB。

### 研究问题
3D高斯溅射（3DGS）虽然实现了高质量的新视角合成和实时渲染，但由于需要数百万个高斯原语，导致内存消耗过大。现有的剪枝方法依赖启发式重要性分数或同步批量更新，导致压缩效果次优且训练不稳定。

### 核心思路/方法
- 将高斯剪枝问题形式化为**变分自由能最小化**，在信息论视角下平衡重建保真度与模型复杂度。
- 提出（1）**预测-误差门控机制**：基于每个高斯的重建不确定性，异步触发剪枝操作；（2）**变分不确定性头**：将剪枝决策建模为具有可学习先验的潜变量。

### 主要贡献
1. 首次将3D高斯剪枝与变分自由能最小化结合，提供理论上的信息论解释。
2. 设计异步激活的门控机制，避免传统同步批量更新的训练不稳定性。
3. 在Mip-NeRF 360、Tanks&Temples和Deep Blending数据集上，以5.2倍压缩实现PSNR仅下降0.31 dB，在更高压缩比下性能优于PUP 3D-GS和LightGaussian，并保持185 FPS的实时渲染速度。

### 局限性
摘要未提供足够信息，例如该方法在极端压缩率下的视觉质量退化上限、对不同场景类型的鲁棒性差异、或计算开销（如变分不确定性头的训练成本）。

### 阅读优先级
**高**
理由：该工作针对3DGS内存消耗大这一核心工程痛点，提出了具有理论背景（变分自由能）的创新方法，且在多个基准数据集上实现了显著压缩比与保真度之间的平衡，同时维持实时渲染性能（185 FPS）。对于从事神经渲染、3D场景压缩或实时图形学的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves remarkable novel view synthesis quality with real-time rendering, yet suffers from excessive memory consumption due to millions of Gaussian primitives. Existing pruning methods rely on heuristic importance scores or synchronous batch updates, leading to suboptimal compression and training instability. We propose VEDAL, a principled framework that formulates Gaussian pruning as variational free energy minimization. Our approach introduces (1) a prediction-error gating mechanism that asynchronously activates pruning based on per-Gaussian reconstruction uncertainty, and (2) a variational uncertainty head that models pruning decisions as latent variables with learnable priors. The free energy objective naturally balances reconstruction fidelity against model complexity through an information-theoretic lens. Extensive experiments on Mip-NeRF 360, Tanks&Temples, and Deep Blending demonstrate that VEDAL achieves 5.2x compression with only 0.31 dB PSNR drop, outperforming PUP 3D-GS by +0.05 dB at a higher compression ratio and LightGaussian by +0.35 dB at comparable quality, while maintaining real-time rendering at 185 FPS.

</details>

#### 2026-06-01 - Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image

**Authors:** Kaidi Zhang, Guanxu Zhu
**Links:** [abs](https://arxiv.org/abs/2606.02068) - [pdf](https://arxiv.org/pdf/2606.02068)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image
- 作者：Kaidi Zhang, Guanxu Zhu
- 出版日期：2026-06-01T10:57:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.02068

### 一句话总结
本文通过可微分的多平面图像（MPI）表示，结合视觉基础模型预测的点图初始化与一步扩散优化，实现了快速、轻量级且在前视角场景下质量可观的新视角合成。

### 研究问题
针对NeRF和3DGS等主流方法在渲染速度与模型大小之间难以平衡、优化训练耗时、稀疏视角下效果不佳，以及前馈式重建方法在移动端部署受限于高斯数量过大的问题，提出一种更高效的新视角合成方法。

### 核心思路/方法
1. **重新使用多平面图像（MPI）表示**：用紧凑的平面层集合表示场景。
2. **可靠几何初始化**：利用视觉基础模型预测的点图进行几何初始化。
3. **可微优化**：在初始化后进行可微优化。
4. **一步扩散参与**：将一步扩散引入两个环节：MPI的可微优化过程、渲染结果的后处理，以解决稀疏初始化导致的空洞和伪影问题。

### 主要贡献
- 提出一种基于可微MPI的快速、轻量级新视角合成方法。
- 利用视觉基础模型预测点图实现可靠的几何初始化。
- 引入一步扩散同时用于MPI优化与渲染后处理，解决稀疏初始化缺陷。
- 实验表明，相比代表性的基于GS的方法，本方法速度快30.7%，模型大小仅为其14.8%，在前视角场景下达到竞争性的合成质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法在渲染速度、模型大小和稀疏视角适应性方面针对现有主流方法（NeRF、3DGS）有明显改进，且实验结果量化了增益，具有一定参考价值；但仅声称“前视角场景”效果良好，且未提供更多对比实验细节（如其他场景类型表现），故优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Recently, novel view synthesis has witnessed remarkable progress, with mainstream methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) delivering impressive results. However, these approaches often struggle to balance rendering speed and model size, and their optimization-based training can be highly time-consuming. Furthermore, they typically rely on dense observations, often failing to produce satisfactory results under sparse-view conditions. Although feed-forward reconstruction significantly reduces the optimization time of 3DGS, its pixel-aligned formulation generates millions of Gaussians from a single image, severely limiting its practical deployment on mobile devices. To address these limitations, we revisit the Multiplane Image(MPI) representation, which represents scenes using a compact set of planar layers for efficient novel view synthesis. Leveraging recent advances in visual foundation models, we utilize predicted point maps for reliable geometric initialization, followed by differentiable optimization. To address the issues of holes and artifacts in sparsely initialized MPI, we introduce one-step diffusion, which participates in both the differentiable optimization of MPI and the postprocessing of rendering results. Compared with a representative GS-based method, our approach is 30.7% faster and uses only 14.8% of its model size, while achieving competitive synthesis quality on front-view scenarios

</details>

#### 2026-06-01 - Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects

**Authors:** Jens U. Kreber, Lukas Mack, Joerg Stueckler
**Links:** [abs](https://arxiv.org/abs/2606.01950) - [pdf](https://arxiv.org/pdf/2606.01950)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, splatting, manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects
- 作者：Jens U. Kreber, Lukas Mack, Joerg Stueckler
- 出版日期：2026-06-01
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）；Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：https://arxiv.org/abs/2606.01950

### 一句话总结
提出一种基于物体为中心的高斯泼溅的世界模型（MRO-GWM），通过时空变换器预测刚体物体的运动轨迹，并应用于非抓取操作中的模型预测控制。

### 研究问题
如何学习刚体物体在三维空间中受动作影响的条件动力学，并处理多物体场景中的部分遮挡和物体形状多样性。

### 核心思路/方法
1. 用物体为中心的高斯泼溅表示场景，每个物体以规范坐标系下的高斯集合建模，运动描述为刚体变换。
2. 设计一种新颖的时空变换器架构，从当前和历史的物体高斯状态与未来动作序列中，预测出物体的刚体运动。
3. 模型通过多视角重建数据训练，强制模型处理物体因遮挡产生的部分观测问题。

### 主要贡献
- 提出MRO-GWM，一种学习物体为中心、动作条件化的刚体动力学世界模型。
- 利用规范坐标系下的高斯表示，统一处理任意形状物体与多物体场景。
- 在包含典型家居物体的合成数据集上验证了预测性能，并通过模拟仿真展示了其在非抓取操作中模型预测控制的应用。

### 局限性
摘要未提供足够信息，无法分析模型在真实世界数据、计算效率、遮挡处理极限或泛化能力上的具体局限。

### 阅读优先级
中
理由：该方法结合了高斯泼溅与变换器预测刚体动力学，创新性明确且面向机器人操作应用，但验证仅基于合成数据，缺乏真实场景及实验细节，适合对场景表示与运动预测交叉领域感兴趣的读者快速了解。

</details>

<details>
<summary>Abstract</summary>

World models enable intelligent agents to predict the consequences of their actions on the environment. In this paper, we propose Multi Rigid Object Gaussian World Model (MRO-GWM), a novel model that learns action-conditional dynamics of rigid objects in 3D. By representing the scene by object-centric Gaussians, we can represent arbitrary object shapes and multi-object scenes. We develop a novel spatio-temporal transformer architecture that predicts future rigid body motion from a history of object Gaussians and future actions. Objects are represented by their Gaussians in a canonical frame, which allows for describing object motion as rigid body transformation. Our model is trained on reconstructions from multiple viewpoints, which requires the model to handle partial observations of objects due to occlusions. We analyze prediction performance of our approach on synthetic datasets composed of typical household objects with multi-object dynamics and interactions by a robot end effector. We also evaluate our model in model-predictive control for non-prehensile manipulation in simulation.

</details>

#### 2026-06-01 - Effective Multi-sensor Conditioning for Street-view Novel-view Synthesis

**Authors:** Zhengfei Kuang, Adam Sun, Liyuan Zhu, Tong Wu, Shengqu Cai, Jonathan Tremblay, Iro Armeni, Ehsan Adeli, Lior Yariv, Gordon Wetzstein
**Links:** [abs](https://arxiv.org/abs/2606.01590) - [pdf](https://arxiv.org/pdf/2606.01590)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** metric depth, novel view synthesis, view synthesis, rendering, driving scene

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Effective Multi-sensor Conditioning for Street-view Novel-view Synthesis
- 作者：Zhengfei Kuang, Adam Sun, Liyuan Zhu, Tong Wu, Shengqu Cai, Jonathan Tremblay, Iro Armeni, Ehsan Adeli, Lior Yariv, Gordon Wetzstein
- 出版日期：2026-06-01
- 分类：Neural Scene Representations & Rendering
- 链接：论文摘要：https://arxiv.org/abs/2606.01590；PDF：https://arxiv.org/pdf/2606.01590；项目主页：https://streetnvs.github.io

### 一句话总结
本文提出StreetNVS，一种基于视频扩散模型的街景新视角合成框架，通过同时利用LiDAR、环绕视图参考图像和相机位姿进行多传感器条件控制，有效提升了稀疏LiDAR下的合成质量，并支持极端轨迹路径。

### 研究问题
现有街景新视角合成方法仅利用部分传感器信号（如仅用图像或位姿），导致当目标轨迹偏离原始行车路径时，合成质量显著下降。因此，本文旨在解决如何有效融合多传感器信息（稀疏LiDAR点云、环绕视图参考图像、相机位姿）以提升街景视角合成对偏离轨迹的鲁棒性。

### 核心思路/方法
1. **多传感器条件设计**：将稀疏LiDAR提供的精确但不完整的度量几何、环绕视图参考图像提供的密集外观、以及相机位姿提供的跨视图关联三信号联合作为扩散模型的条件输入。
2. **Reference-Enhanced Camera Attention模块**：基于相对光线级别的位姿编码（relative ray-level positional encoding），增强模型对参考图像与目标视图之间几何关系的建模能力。
3. **两阶段课程训练策略**：第一阶段使用密集LiDAR预训练，第二阶段逐渐暴露模型到更稀疏的LiDAR数据，以避免稀疏输入导致的信息稀缺问题，提升泛化性。

### 主要贡献
1. 提出StreetNVS，一个同时利用三种传感器信号（LiDAR、图像、位姿）的视频扩散框架，用于街景新视角合成。
2. 设计基于相对光线级别位姿编码的Reference-Enhanced Camera Attention模块，实现跨视图注意力机制的细粒度控制。
3. 引入两阶段课程训练策略，使模型能在极稀疏LiDAR（甚至1/10～1/100于现有方法的密度）下仍取得优异效果。
4. 在Waymo Open Dataset上，StreetNVS在稀疏LiDAR条件下大幅超越现有基线，并展示了沿极端轨迹（如高度变化、车道偏移、拉回、旋转）合成连贯视频的能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。
理由：该工作系统性地解决了多传感器融合在街景视频新视角合成中的核心问题，提出实用的注意力机制和训练策略，并在公开数据集上展现了显著优于基线的性能。对于从事自动驾驶、三维重建、视频生成的研究者，具有明确的启发和应用价值。

</details>

<details>
<summary>Abstract</summary>

Modern vehicle platforms are equipped with a rich sensor suite, including LiDAR, calibrated multi-camera rigs, and accurate ego-motion, that in principle offers strong signal for re-rendering a driving scene from novel viewpoints. A growing line of recent work leverages video diffusion models for this task, using their generative priors to synthesize plausible novel views from sparse vehicle observations. In practice, however, existing methods exploit only a fragment of this signal, and their quality tends to degrade as the target trajectory departs from the recorded driving path. We argue that this is fundamentally a multi-sensor fusion problem: sparse LiDAR reprojections supply accurate but incomplete metric geometry, surround-view reference imagery supplies dense appearance but no metric depth, and camera poses tie the two together across views. We introduce StreetNVS, a video diffusion framework that jointly conditions on all three signals through a Reference-Enhanced Camera Attention module based on a relative ray-level positional encoding. We develop a two-stage curriculum training strategy that gradually exposes the model to increasingly sparse LiDAR. On the Waymo Open Dataset, StreetNVS substantially outperforms state-of-the-art baselines under sparse LiDAR conditioning, matches methods that rely on 10-100 times denser point clouds. We further show capabilities of synthesizing coherent videos along extreme out-of-trajectory paths such as elevation, lane-shift, pullback, and rotation. Our website: https://streetnvs.github.io

</details>

### 2026-05

#### 2026-05-31 - LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World

**Authors:** Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang, Mac Schwager
**Links:** [abs](https://arxiv.org/abs/2606.01458) - [pdf](https://arxiv.org/pdf/2606.01458)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World
- 作者：Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang, Mac Schwager
- 出版日期：2026-05-31T21:36:02Z
- 分类：Neural Scene Representations & Rendering（主要），Embodied / Robotics / AR Applications（次要）
- 链接：[https://arxiv.org/abs/2606.01458](https://arxiv.org/abs/2606.01458)

### 一句话总结
LEGS 提出一种混合模拟器，通过3D高斯泼溅重建真实场景背景、结合网格前景与程序化运动生成器，无需人类遥操作即可为类人机器人生成大量训练数据，使VLA策略性能超过或匹配遥操作基线。

### 研究问题
如何在不依赖昂贵人类遥操作示范的情况下，高效微调视觉-语言-动作（VLA）策略，使其能够泛化至类人机器人的全身移动操作任务。

### 核心思路/方法
1. **混合模拟器**：将网格前景（机器人、物体、道具）合成到从手持扫描重建的3D高斯泼溅（3DGS）照片级真实背景之上。
2. **无遥操作数据合成**：使用程序化运动基元生成器自动生成带标注的示范，无需真人操作。
3. **色彩校准**：确定性的两阶段色彩校准，将渲染的3DGS图像对齐到机器人的部署相机。
4. **背景-运动解耦**：人体运动记录与场景外观独立，可利用一组自动生成的示范在多种新背景和物体网格下重新渲染，实现低成本数据增强。

### 主要贡献
1. 首次展示基于合成数据训练的策略在类人机器人移动操作任务上达到或超越基于人类遥操作示范的策略性能。
2. 通过消融实验证明，照片级真实渲染（3DGS背景）是合成数据成功迁移的关键因素。
3. 提出数据增强方法（LEGS-AUG），仅需遥操作15倍以下的成本即可覆盖新场景，且在物体-场景联合外观偏移下仍能保持任务成功率，而遥操作基线完全失败。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接解决了类人机器人VLA训练中遥操作成本高昂的核心瓶颈，提出了完整的数据合成、渲染校准与泛化方案，并在多任务、多骨干网络上验证了有效性，对移动操作、合成数据仿真和机器人视觉表征领域均有参考价值。

</details>

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) policies for humanoid loco-manipulation is constrained by the high cost and complexity of collecting human teleoperation demonstrations. VLA policies fine-tuned in simulators have, until now, failed to transfer effectively in humanoid loco-manipulation tasks. We present LEGS (Loco-manipulation via Embodied Gaussian Splatting), a hybrid simulator that composites a mesh foreground (robot, objects, props) over a photorealistic 3D Gaussian Splatting (3DGS) background reconstructed from a handheld scene capture. LEGS uses a procedural motion-primitive generator to synthesize labeled demonstrations at scale without human teleoperation, and a deterministic two-stage color calibration to align the rendered 3DGS image to the robot's deployment camera. On a Unitree G1 humanoid robot, across three pick-and-place tasks of increasing whole-body difficulty and three VLA backbones (psi_0, pi_0.5, GR00T N1.6), a policy trained purely on LEGS data matches or exceeds one trained on human teleoperation demos on every experiment. It also outperforms a mesh-only simulation baseline that ablates the effect of the 3DGS background, showing that photorealistic rendering is a key enabler for synthetic data transfer. Humanoid motion is recorded independently of scene appearance in LEGS, allowing the same auto-generated demonstrations to be re-rendered under new backgrounds and object meshes--covering a new scene at more than 15x lower cost than teleoperation--to augment training data for robustness to scene variations. Under combined object-and-scene appearance shift, the policy trained on re-rendered LEGS-AUG data maintains task success while the baseline trained on teleoperation data fails entirely. Our project page is located at https://legsvla.github.io/.

</details>

#### 2026-05-31 - RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation

**Authors:** Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang
**Links:** [abs](https://arxiv.org/abs/2606.01261) - [pdf](https://arxiv.org/pdf/2606.01261)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation  
- 作者：Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
- 出版日期：2026-05-31  
- 分类：Neural Scene Representations & Rendering（主要），Embodied / Robotics / AR Applications（次要）  
- 链接：https://arxiv.org/abs/2606.01261  

### 一句话总结
提出一种基于RGB图像和LiDAR点云的射频数字孪生场景构建工作流，用于28 GHz室内射线追踪信道仿真，能有效减少有效路径数量并保持主路径幅度不变。

### 研究问题
如何高效构建射频可计算的室内三维几何模型，并在28 GHz射线追踪仿真中准确绑定电磁材料属性，以克服手动建模效率低、视觉重建网格射频适应性差以及材料绑定缺失的问题。

### 核心思路/方法
1. 使用Jetson Orin平台搭载LiDAR和GMSL摄像头采集室内视频和点云。  
2. 通过COLMAP、3D Gaussian Splatting和SuGaR生成初始三角形网格。  
3. 在Blender中利用LiDAR点云提供几何和尺度参考，进行射频导向的网格正则化（包括对齐、墙面固化、门窗开口构建和拓扑修复）。  
4. 使用OpenScene语义分割将主要室内结构映射到混凝土、玻璃、木材和金属四种材料。  
5. 利用Sionna RT执行28 GHz射线追踪仿真，并输出信道冲激响应（CIR）、信道频率响应（CFR）和无线电地图。

### 主要贡献
- 开发了一套完整的RF数字孪生场景构建工作流（RFDT-Channel），自动将RGB图像和LiDAR点云转换为射频可计算的室内几何模型。  
- 通过材料绑定，显著改变了弱反射、透射和散射路径，将有效路径数量从约742条减少到约52条，同时保持主导路径幅度几乎不变。  
- 实现了高效、自动化的室内毫米波信道仿真场景构建。

### 局限性
摘要未提供足够信息（例如：未提及方法在复杂场景下的泛化能力、计算开销、实验对比基线、或对动态环境的适用性）。

### 阅读优先级
**中**  
理由：论文聚焦于射频数字孪生与信道仿真这一相对小众的交叉领域，方法结合了视觉重建、语义分割和射线追踪，技术创新点明确且应用场景具体。若读者从事毫米波通信、数字孪生或室内定位相关研究，则值得一读；若主要关注通用计算机视觉或机器人领域，则相关性较低。

</details>

<details>
<summary>Abstract</summary>

Real-scene indoor millimeter-wave simulation requires efficient modeling of radio frequency (RF)-computable geometry and electromagnetic material properties. To address the low efficiency of manual scene modeling, the limited RF adaptability of visually reconstructed meshes, and the lack of material binding in 28 GHz ray-tracing simulation, RFDT-Channel is developed as an RF digital twin scene construction workflow based on red-green-blue (RGB) images and light detection and ranging (LiDAR) point clouds. Indoor videos and point clouds are collected by a Jetson Orin platform with LiDAR and GMSL cameras. An initial triangular mesh is generated through COLMAP, 3D Gaussian Splatting, and SuGaR. The LiDAR point cloud then provides geometric and scale references for RF-oriented regularization in Blender, including alignment, wall solidification, door/window opening construction, and topology repair. OpenScene semantic segmentation maps major indoor structures to concrete, glass, wood, and metal materials, and Sionna RT performs 28 GHz ray tracing. Under a fixed transmitter-receiver deployment, the generated channel impulse response (CIR), channel frequency response (CFR), and Radio Map results show that material binding mainly changes weak reflection, transmission, and scattering paths, reducing the number of effective paths from about 742 to about 52 while keeping the dominant path amplitude nearly unchanged.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-02 - OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs

**Authors:** Yifei Li, Pengyiang Liu, Yuhang Zang, Zhongyue Shi, Qi Fu, Hongye Hao, Jiwen Lu
**Links:** [abs](https://arxiv.org/abs/2606.03890) - [pdf](https://arxiv.org/pdf/2606.03890)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, autonomous driving, mapping, AR, simulation, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs
- 作者：Yifei Li, Pengyiang Liu, Yuhang Zang, Zhongyue Shi, Qi Fu, Hongye Hao, Jiwen Lu
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications
- 链接：abstract: https://arxiv.org/abs/2606.03890, pdf: https://arxiv.org/pdf/2606.03890

### 一句话总结
本文提出一个名为 OVO-S-Bench 的层次化基准，用于评估多模态大语言模型在连续自我中心视频流中实时推理空间结构的能力。

### 研究问题
现有基准要么在完整视频上离线评估，要么针对事件而非空间结构；缺乏专为流式空间智能设计的测试。本文旨在填补这一空白，系统评估多模态大语言模型在仅看到查询时间点之前视频前缀的条件下，对空间布局和关系的实时推理能力。

### 核心思路/方法
- 构建包含 1,680 道题目、348 个源视频的完全人工标注基准。标注过程涉及 12 名训练有素的标注员，每人同时担任盲审交叉审阅者，总耗时约 804 人小时进行多轮质量保证。
- 每个问题附带一个查询时间戳和一个证据区间，评估时模型只能看到查询点之前的视频前缀。
- 问题分为四个抽象层次：瞬时自我中心感知、时空上下文追踪、空间模拟与推理，以及异中心映射。
- 在 38 个专有和开源多模态大语言模型上进行评估，并与人类专家表现对比。

### 主要贡献
- 引入 OVO-S-Bench，一个专注于流式空间智能的完全人工标注基准，包含多层次问题。
- 评估结果表明，最佳模型 Gemini-3.1-Pro 得分为 59.2，与人类专家的 86.6 分仍有 27 分的差距，其中异中心映射是主要瓶颈。
- 发现流式与空间微调的多模态大语言模型表现甚至不如其基础模型。
- 发现链式思维推理在缺乏流式空间依据时会放大空间错误。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文直面多模态智能体在机器人、增强现实和自动驾驶中的核心挑战——流式空间推理，并构建了首个专用层次化基准，揭示了现有模型与人类专家的显著差距，对相关领域的研究和实践具有重要指导意义。

</details>

<details>
<summary>Abstract</summary>

Multimodal agents in robotics, AR, and autonomous driving must reason about places and layouts from continuous egocentric streams, often using evidence outside the current view. Existing benchmarks either evaluate offline over full videos or target events rather than spatial structure. We introduce OVO-S-Bench, a fully human-annotated benchmark for streaming spatial intelligence, comprising 1,680 questions over 348 source videos. Annotation involves 12 trained annotators, each also serving as a blind cross-reviewer, across roughly 804 person-hours of multi-round quality assurance. Each question carries a query timestamp and an evidence interval, and at evaluation, the model sees only the prefix preceding the query. Questions span four levels of increasing abstraction: instantaneous egocentric perception, spatiotemporal context tracking, spatial simulation and reasoning, and allocentric mapping. Across 38 proprietary and open-source MLLMs, Gemini-3.1-Pro trails human experts by 27 points, 59.2 vs. 86.6, with allocentric mapping as the dominant bottleneck. Notably, streaming and spatially fine-tuned MLLMs underperform their own backbones. We further find that chain-of-thought reasoning amplifies spatial errors when ungrounded in the stream. By exposing these limitations, OVO-S-Bench establishes a demanding testbed for next-generation streaming spatial MLLMs.

</details>

#### 2026-06-02 - A 3D Isovist World Model -- Revealing a City's Unseen Geometry and Its Emergent Cross-City Signature

**Authors:** Xuhui Lin, Stephen Law, Nanjiang Chen, Kunyao Li, Tao Yang
**Links:** [abs](https://arxiv.org/abs/2606.03609) - [pdf](https://arxiv.org/pdf/2606.03609)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A 3D Isovist World Model – Revealing a City’s Unseen Geometry and Its Emergent Cross-City Signature
- 作者：Xuhui Lin, Stephen Law, Nanjiang Chen, Kunyao Li, Tao Yang
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03609

### 一句话总结
本文提出一种以3D isovist（球面可见深度图）为预测目标的世界模型，仅通过几何信息学习城市可导航空间动态，并发现该模型在训练于多个城市时能自发产生可区分城市身份的时空特征。

### 研究问题
现有具身智能体的世界模型通常预测场景外观（如RGB图像）或简化的俯视占用网格，忽略了三维空间中的可导航几何结构（如架空层、多层空间），难以准确建模智能体实际移动的负空间（建筑物之间的开放体积）。研究目标是：如何仅基于几何信息、无需外观特征，预测智能体在移动中周围可导航空间的变化。

### 核心思路/方法
1. **预测目标设计**：将3D isovist（球面可见深度图）作为世界模型的预测目标，记录每个方向上到最近表面的距离，从而编码开放体积的几何结构。
2. **预测机制**：模型基于短历史isovist序列和当前动作，预测下一个isovist的深度残差（使解码器保留建筑边缘锐利性）。
3. **训练策略**：采用自展开调度采样（self-rollout scheduled sampling），在训练中向模型提供带有几何流形扰动的上下文，使其适应预测偏差。
4. **持久空间记忆**：引入隐式俯视鸟瞰空间图（persistent latent BEV spatial map），实现跨路径的一致性保持。
5. **跨城市实验**：在曼哈顿和巴黎两个城市数据上训练单一模型，并测试其在不同城市路径上的表现。

### 主要贡献
- 提出一种不依赖外观信息、仅基于三维几何的轻量级世界模型预测框架（3D isovist）。
- 发现跨城市空间特征：单一模型在不同城市中产生线形可解码的城市身份信号，且该信号存在于学习到的动态中而非单帧外观中。
- 提供了开放数据集和可复现的流水线，可用于具身AI、机器人导航和城市分析。

### 局限性
摘要未提供足够信息：未提及模型在复杂城市环境（如非网格状道路、密集植被遮挡）中的鲁棒性、对传感器噪声的容忍度、多源数据集下的泛化边界，以及与现有外观预测基线的量化对比实验细节。

### 阅读优先级
**高**  
理由：本文提出了一种新颖的几何世界模型范式，聚焦于智能体导航中“可走空间”而非“场景外观”，方向具有实用价值；且发现的跨城市空间特征具有启发性。摘要结构清晰、方法描述完整，适合对具身智能、城市空间分析感兴趣的读者深入阅读。

</details>

<details>
<summary>Abstract</summary>

Embodied agents that navigate cities rely on world models that predict how their surroundings will change as they move. But for navigation, what matters is not what the buildings look like; it is where the agent can go. Most world models nonetheless predict appearance, learning how a scene looks rather than the space an agent can move through. Those that do target geometry, such as bird's-eye-view occupancy grids, flatten the three-dimensional environment onto a ground plane, discarding the above-ground and multi-level structure that shapes real navigation. What is missing is a predictive target that captures the navigable geometry an agent actually traverses, without photometric entanglement and without collapsing the third dimension. Our key idea is to model the open volume between buildings, the negative space, encoded as a 3D isovist: a spherical visibility-depth map recording the distance to the nearest surface in every direction. We introduce an embodied world model that predicts the next isovist from a short history of past isovists and a movement action. The prediction is formulated as a depth residual so the decoder inherits sharp building edges, trained with self-rollout scheduled sampling to keep corrupted context on the geometry manifold, and equipped with a persistent latent bird's-eye-view spatial map for cross-path consistency. Our central finding is emergent and unexpected: a single city-blind model trained on Manhattan and Paris develops a cross-city spatial signature, with city identity linearly decodable from its temporal latents far above single-frame baselines, so the signature lives in the learned dynamics rather than in appearance. The representation is lightweight, interpretable, and reproducible, offering a geometric substrate for spatial reasoning in embodied AI, robotics, and urban analysis, released with an open dataset and pipeline.

</details>

#### 2026-06-02 - TASE: Truncation-Aware Semantic Embeddings for 3D Scene Understanding and Editing

**Authors:** Tim-Felix Faasch, Jochen Kall, Lucas Nunes, Jens Behley, Cyrill Stachniss
**Links:** [abs](https://arxiv.org/abs/2606.03314) - [pdf](https://arxiv.org/pdf/2606.03314)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, autonomous driving, simulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TASE: Truncation-Aware Semantic Embeddings for 3D Scene Understanding and Editing
- 作者：Tim-Felix Faasch, Jochen Kall, Lucas Nunes, Jens Behley, Cyrill Stachniss
- 出版日期：2026-06-02T08:25:53Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03314

### 一句话总结
TASE 提出一种通过截断感知嵌入空间实现灵活可控的3D场景编辑方法，支持文本驱动编辑并可调节编辑强度。

### 研究问题
如何实现高保真、可编辑且具备可控性的3D语义场景表征，以支持大规模几何修改的文本驱动编辑。

### 核心思路/方法
1. 将预训练的2D语义特征投影到截断感知的嵌入空间，并显式优化该特征空间：减少特征通道数时产出更抽象的语义表示，保留更多通道则保留细粒度细节。
2. 利用尺度和平移等变性损失提高特征的多视图一致性。
3. 编辑时可通过截断策略控制修改与原始场景内容的贴合程度，实现比现有方法更强的大规模修改。
4. 对编辑扩散模型进行微调，以缓解几何变化带来的伪影。

### 主要贡献
- 提出截断感知嵌入空间，实现特征通道数控制下的语义抽象粒度调节。
- 通过尺度和平移等变性损失提升多视图特征一致性。
- 实现文本驱动的3D场景编辑，支持显式控制编辑强度，尤其在大几何修改任务上显著优于现有方法。

### 局限性
摘要未提供足够信息，无法明确提及具体局限性，如方法在不同场景下的泛化能力、计算开销或对特定编辑任务的适用边界等。

### 阅读优先级
高。理由：该方法在3D场景编辑任务上实现了优于现有技术的大几何修改能力，且具备可控性，适用于机器人、自动驾驶、仿真等前沿应用场景，摘要所示方法设计（截断感知嵌入）具有创新性。

</details>

<details>
<summary>Abstract</summary>

High-fidelity semantic 3D scene representations are crucial for numerous applications, including robotics, autonomous driving, and simulation. Beyond this, the ability to edit such representations enables developers to adapt these applications more easily to specific target scenarios. Current approaches provide limited support for controllable editing. We introduce TASE, a method that projects pretrained 2D semantic features into a truncation-aware embedding space to enable flexible 3D scene editing. Our method explicitly optimizes a feature space in which progressively reducing feature channels yields increasingly abstract semantic representations, while retaining more channels preserves fine-grained detail. Additionally, we improve multi-view consistency of the features using a scale- and translation-equivariance loss. The resulting truncation-aware embedding space enables text-driven edits to 3D scenes, providing explicit control over how strongly edits adhere to the original scene content and allowing more substantial modifications than prior methods. Moreover, we propose a finetuning stage for the editing diffusion model to mitigate artifacts caused by geometric changes. Experimental results demonstrate competitive performance in 3D scene editing, substantially outperforming prior methods on edits involving large geometric modifications.

</details>

#### 2026-06-02 - GeoSem-WAM: Geometry- and Semantic-Aware World Action Models

**Authors:** Fulong Ma, Daojie Peng, Wenjun Yue, Jiahang Cao, Bintao Wang, Qiang Zhang, Jun Ma
**Links:** [abs](https://arxiv.org/abs/2606.03188) - [pdf](https://arxiv.org/pdf/2606.03188)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoSem-WAM: Geometry- and Semantic-Aware World Action Models
- 作者：Fulong Ma, Daojie Peng, Wenjun Yue, Jiahang Cao, Bintao Wang, Qiang Zhang, Jun Ma
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03188

### 一句话总结
该论文提出一种结构化世界建模框架GeoSem-WAM，通过在RGB未来预测之外引入几何与语义辅助预测分支，增强世界动作模型的潜在表征，从而在不依赖显式测试时推演的前提下提升具身决策中的动作预测准确性和场景理解鲁棒性。

### 研究问题
现有世界动作模型（WAM）主要依赖基于RGB的未来预测，缺乏对复杂环境的结构和空间理解；此外，其有效性究竟源于显式未来想象还是表征学习尚不明确。论文试图通过结构化监督来增强潜在表征，以解决上述结构性与语义理解不足的问题。

### 核心思路/方法
提出GeoSem-WAM框架，在现有WAM的RGB未来预测主干基础上，增加两个辅助预测分支：未来几何表征分支和未来语义表征分支。通过联合优化这三个分支，模型在统一的潜在空间中同时捕获场景动态、空间几何与语义上下文。推理时避免了显式的未来展开或视频生成，保持高效。

### 主要贡献
1. 提出一种结合几何与语义监督的结构化世界建模框架，用于增强WAM的潜在表征。
2. 引入两个辅助预测分支（几何与语义），在训练中提供结构化世界监督，而测试时不增加额外计算开销。
3. 实验表明结构化世界监督一致地提升了动作预测准确性、场景理解能力和在挑战性具身场景下的鲁棒性。

### 局限性
摘要未提供足够信息，包括对潜在表征可解释性、计算开销对比、未覆盖的场景类型或失败案例的讨论。

### 阅读优先级
中  
理由：该工作针对具身智能中世界模型的结构化表征问题提出了明确的改进方向，方法设计清晰且实验展示了收益，适合对具身决策、世界模型或结构化表示学习感兴趣的读者。但摘要未包含对基线方法的详细对比或消融实验的具体数据，且发表年份较远（2026年），可能需要结合完整论文评估其实际效果与创新程度。

</details>

<details>
<summary>Abstract</summary>

Recent World Action Models (WAMs) have demonstrated impressive capabilities in embodied decision-making. However, whether their effectiveness stems from explicit future imagination during inference or representation learning induced by predictive training remains an open question. Emerging evidence suggests the primary advantage lies in learning robust latent representations rather than generating future observations at test time. Nevertheless, existing WAMs mainly rely on RGB-based future prediction, which provides limited structural and spatial understanding of complex environments. To address this, we propose a structured world modeling framework that enhances latent representations through geometric and semantic supervision. Alongside future RGB prediction, our model introduces two auxiliary prediction branches for future geometry and semantic representations, enabling it to jointly capture scene dynamics, spatial geometry, and semantic context within a unified latent space. Crucially, our approach preserves efficient inference by avoiding explicit future rollout or video generation at test time. Extensive experiments show that incorporating structured world supervision consistently improves action prediction accuracy, scene understanding, and robustness under challenging embodied scenarios, highlighting its potential for advancing scalable and efficient WAMs.

</details>

#### 2026-06-02 - NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation

**Authors:** NVIDIA, :, Aarti Basant, Amlan Kar, Despoina Paschalidou, Fangyin Wei, Francesco Ferroni, Guillermo Garcia Cobo, Haithem Turki, Huan Ling, Jaewoo Seo, James Lucas, Jay Zhangjie Wu, Jialiang Wang, Jonathan Lorraine, Jun Gao, Kai He, Katarina Tothova, Kevin Xie, Michał Tyszkiewicz, Qi Wu, Riccardo de Lutio, Ruilong Li, Sanja Fidler, Seung Wook Kim, Tianchang Shen, Tianshi Cao, Tobias Pfaff, William Lew, Xindi Wu, Xuanchi Ren, Yifan Lu, Yuxuan Zhang, Zan Gojcic, Zian Wang
**Links:** [abs](https://arxiv.org/abs/2606.03159) - [pdf](https://arxiv.org/pdf/2606.03159)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation
- 作者：NVIDIA, :, Aarti Basant, Amlan Kar, Despoina Paschalidou, Fangyin Wei, Francesco Ferroni, Guillermo Garcia Cobo, Haithem Turki, Huan Ling, Jaewoo Seo, James Lucas, Jay Zhangjie Wu, Jialiang Wang, Jonathan Lorraine, Jun Gao, Kai He, Katarina Tothova, Kevin Xie, Michał Tyszkiewicz, Qi Wu, Riccardo de Lutio, Ruilong Li, Sanja Fidler, Seung Wook Kim, Tianchang Shen, Tianshi Cao, Tobias Pfaff, William Lew, Xindi Wu, Xuanchi Ren, Yifan Lu, Yuxuan Zhang, Zan Gojcic, Zian Wang
- 出版日期：2026-06-02T05:11:05Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03159

### 一句话总结
OmniDreams是一个基于Cosmos扩散模型进行中训练和后训练的实时生成式世界模型，用于在闭环自动驾驶仿真中根据驾驶动作自回归生成动作条件化视频，以模拟极端天气等长尾场景。

### 研究问题
如何在闭环自动驾驶仿真中克服传统重建式神经模拟器对初始捕获数据的依赖，并生成难以捕捉的动态或新颖场景（如极端天气和不可预测的智能体行为），以实现安全、全面的驾驶策略评估。

### 核心思路/方法
- 从Cosmos扩散模型出发，利用其丰富的视觉先验，对OmniDreams进行中训练和后训练（使用21k小时驾驶场景数据）。
- 模型自回归地将过去帧、当前模拟器状态和即时驾驶动作作为条件，生成逼真的传感器观测视频。
- 在闭环系统中与Alpamayo 1策略模型和AlpaSim编排器集成，使OmniDreams作为响应式的环境。
- 额外验证了世界-动作模型（WAM）在NuRec数据集上超越VLA基线的潜力。

### 主要贡献
1. 提出了OmniDreams，一个能够实时自回归生成动作条件化视频的生成式世界模型。
2. 通过中训练和后训练，使模型能够合成传统模拟器难以捕捉的复杂、未观测现象（如极端天气和动态智能体行为）。
3. 展示了在闭环自动驾驶仿真中作为响应式环境的部署效果。
4. 初步结果表明，基于OmniDreams后训练的世界-动作模型（WAM）在NuRec数据集上优于VLA-based Alpamayo 1.5政策模型，且参数量仅为其1/5。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该工作针对自动驾驶仿真中长尾场景生成这一关键瓶颈，提出了基于扩散模型的实时生成式世界模型，方法新颖且具有实际应用价值。初步实验显示出参数效率优势，适合关注自动驾驶仿真与世界模型的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck. In closed-loop simulation, the driving policy model actively interacts with the environment, where its actions dynamically update the simulator state and directly influence the next set of generated sensor observations. While recent reconstruction-based neural simulators offer photorealism, they are fundamentally constrained by their initial captured data and struggle to generalize to highly dynamic or novel scenes. To overcome these limitations, we introduce OmniDreams, a foundation generative world model mid- and post-trained from the Cosmos diffusion model to autoregressively generate action-conditioned videos in real time. By leveraging the rich visual priors of Cosmos and mid- and post-training on 21k hours of driving scenarios, OmniDreams synthesizes complex, unobserved phenomena that are hard for traditional simulators to capture, such as extreme weather and unpredictable dynamic agent behaviors. Crucially, it autoregressively conditions its photorealistic sensor generation on past frames, the current simulator state, and immediate driving actions. Deployed in a closed-loop system with the Alpamayo 1 policy model and AlpaSim orchestrator, OmniDreams acts as a highly responsive, reactive environment, providing a scalable and comprehensive solution for training and evaluating next-generation autonomous driving policies. We additionally show preliminary results indicating that a world-action model (WAM) post-trained from OmniDreams achieves strong performance on the Physical AI Autonomous Vehicles NuRec dataset, surpassing the VLA-based Alpamayo 1.5 research policy model while using only 1/5 the total parameters. These results highlight the potential for a real-time world model like OmniDreams to also serve as a backbone for policy architectures.

</details>

#### 2026-06-02 - MARIO: Motion-Augmented Real-Time Multi-Sensor Inertial Odometry

**Authors:** Yiquan Li, Taeyoung Yeon, Chenfeng Gao, Vasco Xu, Xuanyou Liu, Karan Ahuja
**Links:** [abs](https://arxiv.org/abs/2606.02996) - [pdf](https://arxiv.org/pdf/2606.02996)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MARIO: Motion-Augmented Real-Time Multi-Sensor Inertial Odometry
- 作者：Yiquan Li, Taeyoung Yeon, Chenfeng Gao, Vasco Xu, Xuanyou Liu, Karan Ahuja
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications（体现/机器人/AR应用）
- 链接：摘要链接（https://arxiv.org/abs/2606.02996）| PDF链接（https://arxiv.org/pdf/2606.02996）

### 一句话总结
本文提出MARIO，一种通过学习IMU推断的姿势先验并结合多传感器融合（磁力计、气压计、辅助IMU）来提升惯性里程计位置漂移性能的方法，在Nymeria数据集上漂移降低高达42%。

### 研究问题
惯性里程计（仅使用IMU）在人体运动跟踪中仍然存在漂移和噪声问题，尤其是当应用于日常活动数据集（如Nymeria）时，现有学习方法未能显式捕捉人体运动动力学。

### 核心思路/方法
1. 先验姿势学习：通过学习一个IMU推断的姿势先验，将惯性里程计建立在人体运动学基础上，提供物理一致的运动约束。
2. 集成到现有IO架构：将姿势先验集成到现有的惯性里程计架构中，在Nymeria数据集上将位置漂移降低高达36%。
3. 多传感器融合框架：进一步融合商用AR眼镜已有的轻量传感器（磁力计、气压计、辅助IMU），将位置漂移降低高达42%，提升不同运动条件下的鲁棒性和泛化性。

### 主要贡献
1. 引入基于人体运动学的IMU推断姿势先验，提升惯性里程计的物理一致性。
2. 在挑战性Nymeria数据集（比以往工作大5倍）上减少位置漂移最高36%。
3. 提出多传感器融合框架，利用商用AR眼镜现有传感器进一步减少漂移最高42%。
4. 为无相机的精确人体跟踪设立了新基准。

### 局限性
摘要未提供足够信息。未讨论方法在计算开销、实时性限制、不同传感器失效场景下的表现，也未提及数据隐私或传感器校准等潜在问题。

### 阅读优先级
中。理由：该工作针对AR/可穿戴设备中的惯性定位漂移问题提出了一个有明确改进的方案（姿势先验+多传感器融合），在较大数据集上取得了显著效果，适合对IMU跟踪、人机交互或多传感器融合方向的研究者参考。但具体技术细节（如模型架构、训练流程、实时性验证等）需要阅读全文才能判断其可复现性和实际价值。

</details>

<details>
<summary>Abstract</summary>

Inertial odometry (IO) using only Inertial Measurement Units (IMUs) provides a lightweight solution for human motion tracking in augmented reality (AR) and wearable devices. Recent learning-based IO methods have improved the generalizability of inertial localization through large-scale pretraining on human motion datasets. However, these approaches remain prone to drift and noise because they do not explicitly capture human motion dynamics, especially on daily activity datasets such as Nymeria. In this work, we propose to ground inertial odometry in human kinematics through a learned IMU-inferred pose prior, which promotes physically consistent motion constraints. We integrate this pose prior into existing IO architectures and reduce positional drift by up to 36% on the challenging Nymeria dataset, which is 5x larger than datasets used in prior work. We further improve long-term performance with a sensor-fusion framework that incorporates auxiliary signals from lightweight sensors already available on commercial AR glasses, including magnetometers, barometers, and secondary IMUs. With this fusion strategy, positional drift is reduced by up to 42%, improving robustness and generalization across diverse motion conditions. Together, our results introduce a new paradigm for inertial and lightweight odometry by unifying human motion kinematics with multimodal sensing, setting a new benchmark for accurate and robust camera-less human tracking. Our website is available at https://spice-lab.org/projects/MARIO/.

</details>

#### 2026-06-02 - Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion

**Authors:** Oskar Natan, Jun Miura
**Links:** [abs](https://arxiv.org/abs/2606.02979) - [pdf](https://arxiv.org/pdf/2606.02979)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth estimation, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion
- 作者：Oskar Natan, Jun Miura
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications
- 链接：论文摘要 https://arxiv.org/abs/2606.02979 ; PDF https://arxiv.org/pdf/2606.02979

### 一句话总结
提出一个紧凑型多任务深度学习模型，通过自适应损失加权和中间传感器融合，在单次前向传播中同时处理语义分割、深度估计、激光雷达分割和鸟瞰图投影等多种自动驾驶感知任务，且参数量更少、推理更快。

### 研究问题
如何处理自动驾驶中多种感知任务（如语义分割、深度估计、激光雷达分割、鸟瞰图投影）的联合学习，并解决多任务训练中因任务数量过多导致的学习不平衡问题，同时融合RGB相机、动态视觉传感器（DVS）和激光雷达等多模态输入。

### 核心思路/方法
1. **紧凑型多任务学习模型**：设计一个单一的深度学习模型，无需其他模型支持，即可在单次前向传播中完成多种视图的感知任务（语义分割、深度估计、激光雷达分割、鸟瞰图投影）。
2. **自适应损失加权算法**：针对多个任务造成的学习不平衡问题，提出一种自动调整各任务损失权重的算法，以平衡训练过程。
3. **数据预处理与中间传感器融合**：通过对RGB相机、DVS和激光雷达的数据进行预处理和中间层融合，使模型能处理并合并多种输入模态，实现多位置传感器的信息整合。

### 主要贡献
1. 提出了一种紧凑型多任务感知模型，能以更少参数保持或提升性能，推理速度更快，GPU内存占用更低。
2. 设计自适应损失加权算法，缓解多任务学习中的不平衡问题。
3. 通过数据预处理和中间传感器融合技术，实现了RGB相机、DVS和激光雷达多模态输入的有效整合。
4. 在3个CARLA仿真数据集和1个真实世界nuScenes-lidarseg数据集上取得了稳定一致的表现，并公开代码以支持后续研究。

### 局限性
摘要中未明确提及模型的局限性（如复杂环境下的可靠性、计算资源需求、未测试的场景等）。此外，所有实验均在仿真和单一真实数据集进行，摘要未提供足够信息说明在更复杂真实场景下的泛化能力。

### 阅读优先级
**高**  
理由：该研究针对自动驾驶感知中的多任务学习和传感器融合核心问题，提出了紧凑且高效的解决方案，并显著减少了参数量和计算资源消耗，符合当前自动驾驶系统对实时性和节能的需求。同时，实验结果在多个数据集上表现一致，代码公开，适合相关领域研究人员快速验证和借鉴。

</details>

<details>
<summary>Abstract</summary>

We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass. The model performs multiple views of semantic segmentation, depth estimation, light detection and ranging (LiDAR) segmentation, and bird's eye view projection simultaneously without being supported by other models. We also provide an adaptive loss weighting algorithm to tackle the imbalanced learning issue that occurred due to plenty of given tasks. Through data pre-processing and intermediate sensor fusion techniques, the model can process and combine multiple input modalities retrieved from RGB cameras, dynamic vision sensors (DVS), and LiDAR placed at several positions on the ego vehicle. Therefore, a better understanding of a dynamically changing environment can be achieved. Based on the ablation study, the model variant trained with our proposed method achieves a better performance. Furthermore, a comparative study is also conducted to clarify its performance and effectiveness against the combination of some recent models. As a result, our model maintains better performance even with much fewer parameters. Hence, the model can inference faster with less GPU memory utilization. Moreover, the result tends to be consistent in 3 different CARLA simulation datasets and 1 real-world nuScenes-lidarseg dataset. To support future research, we share codes and other files publicly at https://github.com/oskarnatan/compact-perception.

</details>

#### 2026-06-01 - MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data

**Authors:** Teng Hu, Mingchun Lu, Yating Wang, Jiangning Zhang, Jinkun Hao, Ye Pan, Ran Yi, Lizhuang Ma, Dacheng Tao
**Links:** [abs](https://arxiv.org/abs/2606.02753) - [pdf](https://arxiv.org/pdf/2606.02753)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, simulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data
- 作者：Teng Hu, Mingchun Lu, Yating Wang, Jiangning Zhang, Jinkun Hao, Ye Pan, Ran Yi, Lizhuang Ma, Dacheng Tao
- 出版日期：2026-06-01
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2606.02753；PDF: https://arxiv.org/pdf/2606.02753

### 一句话总结
MetaWorld 提出了一种从单视角视频数据扩展至多智能体视频世界模型的新框架，通过单目世界状态展开、智能体感知生成器和世界状态对齐技术，解决了多视角数据稀缺和跨视角状态一致性两大问题。

### 研究问题
如何从大规模单视角视频（而非昂贵的多视角录制数据）中构建多智能体视频世界模型，并保证不同视角生成的视频流在共享物理环境和事件演化上具有一致性。

### 核心思路/方法
1. **Monocular World-State Unrolling (MWSU)**：将单目视频显式分解为相机操作者的自运动和可见主体的空间轨迹，从单个视角中提取同步的多智能体运动数据，绕过多相机配置需求。
2. **Subject-Aware World Generator**：基于每智能体身份图像进行外观驱动的模拟，实现对视频中特定主体的视觉控制。
3. **World-State Alignment (WSA)**：在视频DiT的每个Transformer层中插入帧间跨分支交叉注意力机制，联合同步去噪过程，同时保证静态几何一致性和动态运动一致性。

### 主要贡献
1. 提出了从单视角视频扩展至多智能体视频世界模型的框架，解决了数据可扩展性问题。
2. 设计了单目世界状态展开方法，无需多相机设置即可获得同步的多智能体运动数据。
3. 引入世界状态对齐机制，确保不同视角的视频流在共享物理环境和事件演化上保持一致。
4. 实验证明MetaWorld在跨视角一致性和身份保真度上优于现有方法。

### 局限性
摘要未提供足够信息（未讨论可能的失败案例、对复杂场景的适用边界、计算开销或对视频数据质量的依赖等）。

### 阅读优先级
**高**  
理由：该工作针对多智能体视频世界模型的核心瓶颈（数据获取困难和跨视角对齐）提出了新颖且可扩展的解决方案，方法设计完整（包含分解、生成、对齐三个关键模块），涉及重要应用场景（具身AI、元宇宙），且论文发表于2026年，具有方向引导性。

</details>

<details>
<summary>Abstract</summary>

Video world models are a foundational generative technology for embodied AI and the Metaverse, yet existing approaches are inherently limited to a single agent observing from a single perspective. Extending these models to multi-agent settings introduces two critical challenges: data scarcity (coordinated multi-view recordings are prohibitively expensive to collect for general open-domain scenarios) and world state alignment (independently generated video streams cannot ensure that shared physical environments and events evolve consistently across views). To address these challenges, we propose MetaWorld, a novel framework that scales multi-agent video world models to open-domain environments directly from single-view videos. First, we introduce Monocular World-State Unrolling (MWSU) to explicitly decompose monocular footage into the camera operator's ego-motion and the visible subject's spatial trajectory. This camera-trajectory decomposition naturally extracts synchronized multi-agent motion data within a shared 3D space, completely bypassing the need for multi-camera setups. Second, for precise visual control, we develop the Subject-Aware World Generator to enable appearance-driven simulation conditioned on per-agent identity images. Finally, to ensure both views are grounded in the identical physical reality, we propose World-State Alignment, a per-frame inter-branch cross-attention mechanism inserted at every transformer layer of the video DiT. By jointly synchronizing the denoising process, WSA enforces both static geometric consistency and dynamic motion consistency, encouraging that the shared 3D environment and physical events remain well-aligned across both egocentric views. Extensive experiments demonstrate that MetaWorld achieves superior cross-view consistency and identity fidelity, establishing a highly scalable, physics-driven paradigm for multi-agent video world modeling.

</details>

#### 2026-06-01 - MASER: Modality-Adaptive Specialist Routing for Embodied 3D Spatial Intelligence

**Authors:** Hilton Raj, Vishnuram AV
**Links:** [abs](https://arxiv.org/abs/2606.02463) - [pdf](https://arxiv.org/pdf/2606.02463)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MASER: Modality-Adaptive Specialist Routing for Embodied 3D Spatial Intelligence
- 作者：Hilton Raj, Vishnuram AV
- 出版日期：2026-06-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.02463

### 一句话总结
MASER提出一种轻量化框架，通过训练五个模态适配器并学习基于问题语义进行路由的策略，解决具身3D智能中单一模态忽略问题语义的问题。

### 研究问题
具身3D智能中，现有视觉-语言模型仅针对单一模态微调，忽略了问题本身的语义可能导致不同模态（如点云、RGB图像等）更适合不同场景，无法自适应选择最优模态。

### 核心思路/方法
1. **五模态适配器**：在共享VLM骨干上训练五个独立的模态适配器（分别处理自然语言、RGB图像、点云、深度图和相机位姿）。
2. **神经路由策略**：使用冻结的句子编码器将问题编码为嵌入，通过一个小型多层感知机（MLP）根据问题选择最优适配器。该MLP在oracle适配器-准确率标签上训练。
3. **推理高效**：每次推理只需调用一次适配器，避免多模态全量计算。

### 主要贡献
1. 首次在具身3D VQA中引入模态自适应路由，使模型根据问题动态选择最佳模态。
2. 通过轻量框架（单个MLP）实现接近oracle水平的路由（51.3% oracle一致性），优于随机森林基线（43.5%）。
3. 实验证实无单一模态普遍最优（点云在51.5%情况下最佳），验证了自适应路由的必要性。

### 局限性
摘要未提供足够信息：未提及跨领域泛化能力、对噪声或多模态缺失情况的鲁棒性、以及更复杂场景下的路由延迟分析。

### 阅读优先级
**高**
理由：该方法针对具身3D智能中模态选择的核心瓶颈，提出实用轻量框架，且实验指标明确（oracle一致性、适配器仅调用一次），对多模态理解与智能体决策领域有参考价值。

</details>

<details>
<summary>Abstract</summary>

In 3D environments, Embodied Agents answer spatially relevant questions through reasoning from a mixture of modalities including natural language, RGB images, point clouds, depth maps and camera poses. Existing Vision-Language models (VLMs) are fine-tuned over a single modality. This completely ignores the question semantics which may favor a different modality than the finetuned modality. To address this, we propose MASER (Modality-Adaptive SpEcialist Routing), a lightweight framework that trains five different modality adapters of a shared VLM backbone and learns a neural routing policy that selects the best adapter based on the question during inference. We encode each question with a frozen sentence transformer and pass the embedding through a small Multi-layer Perceptron (MLP) trained on oracle adapter-accuracy labels. We evaluate our methodology over the Open3D-VQA benchmark and our evaluations show that no single modality is universally optimal -- point-cloud answers are best in 51.5% of cases. MASER routes with 51.3% oracle agreement, outperforming a Random-Forest ablation (43.5%), with only a single adapter call per question.

</details>

#### 2026-06-01 - SAVMap: Structure-Aided Visual Mapping of Large-Scale 2.5D Manhattan Wireframes from Panoramic Video

**Authors:** Howard Huang, Bharath Surianarayanan, Keifer Lee, Chenyu Wang, Chen Feng
**Links:** [abs](https://arxiv.org/abs/2606.01939) - [pdf](https://arxiv.org/pdf/2606.01939)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** structure from motion, mapping, localization, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAVMap: Structure-Aided Visual Mapping of Large-Scale 2.5D Manhattan Wireframes from Panoramic Video
- 作者：Howard Huang, Bharath Surianarayanan, Keifer Lee, Chenyu Wang, Chen Feng
- 出版日期：2026-06-01
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2606.01939，PDF：https://arxiv.org/pdf/2606.01939

### 一句话总结
SAVMap是一种利用全景视频生成仓库货架与灯光结构语义线框地图的方法，通过语义分割、特征点跟踪和曼哈顿网格约束的运动恢复结构实现高精度大规模建图。

### 研究问题
如何仅使用全景视频摄像头作为传感器输入，为大规模工业环境（如仓库）生成精确的语义线框地图，以支持机器人定位和数字孪生等任务。

### 核心思路/方法
1. 从沿仓库通道采集的全景视频中提取经过矫正的货架和天花板视角图像序列。
2. 利用语义分割网络前端，从每帧图像中提取稀疏的语义结构特征点（如货架角点、灯光中心）。
3. 跨序列跟踪这些特征点，并利用现实中的几何关系（如曼哈顿网格）作为约束，通过结构-运动算法计算3D点，最终形成线框地图。

### 主要贡献
- 提出一种仅依赖全景视频的线框地图生成方法，无需传统传感器（如激光雷达）。
- 结合曼哈顿网格约束提升运动恢复结构的准确性和稳定性。
- 在包含46排货架、每排跨度55米×7米的仓库中验证，从一小时全景视频生成超过5000个货架元素的线框地图，整体平均绝对误差为4.8厘米（相对于真值）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法针对工业环境中的大规模建图任务，仅使用低成本全景视频实现厘米级精度，对机器人定位和数字孪生应用具有直接价值，且实验规模大、误差指标清晰。

</details>

<details>
<summary>Abstract</summary>

Precise 3D representations of industrial environments enable tasks such as robot localization and digital twin generation. We propose SAVMap, a method for generating a semantic wireframe map of warehouse shelf and light structures using only a panoramic video camera as the sensor input. Sequences of rectified images with shelf and ceiling-facing views are extracted from a panoramic video captured along the warehouse aisles. Using a semantic segmentation network front end, a set of sparse, semantic structure feature points (e.g., corners of shelf structures, centers of lights) are extracted from each image and tracked across the sequences. By accounting for real-world geometric relationships among the points such as Manhattan grids, a constrained structure-from-motion algorithm yields the 3D points that form a wireframe map. We demonstrate the scalability and accuracy of our proposal in a warehouse with 46 shelving rows, each with faces spanning 55\,m by 7\,m. From an hour of panoramic video content, we create wireframe maps for over 5000 shelf elements across the rows, achieving an aggregate mean absolute error of 4.8\,cm with respect to ground-truth.

</details>

#### 2026-06-01 - Unified Driving Tokens: Representation- and Geometry-Guided Discrete Tokenizer for Driving World Models and Planning

**Authors:** Ziyang Yao, Zeyu Zhu, YunCheng Jiang, Zibin Guo, Huijing Zhao
**Links:** [abs](https://arxiv.org/abs/2606.01935) - [pdf](https://arxiv.org/pdf/2606.01935)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Unified Driving Tokens: Representation- and Geometry-Guided Discrete Tokenizer for Driving World Models and Planning
- 作者：Ziyang Yao, Zeyu Zhu, YunCheng Jiang, Zibin Guo, Huijing Zhao
- 出版日期：2026-06-01T09:02:32Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.01935

### 一句话总结
本文提出一种受表征和几何引导的离散分词器，通过联合监督学习紧凑的驾驶令牌，用于驾驶世界模型和规划任务，并实验验证了其重构保真度、表征一致性和生成质量。

### 研究问题
现有离散视觉分词器主要针对图像生成优化，侧重于像素重构，可能有损于驾驶决策所需的有效解码，需要弥合“易生成”与“对决策有用”之间的鸿沟。

### 核心思路/方法
1. 设计一种表征引导和几何增强的分词器，在联合监督下学习离散令牌。
2. 通过特征解码将其离散瓶颈与冻结的DINO特征空间对齐。
3. 结合感知损失和对抗损失保留外观（RGB重构）。
4. 注入几何状态提示：在训练中加入相邻帧深度和相对姿态监督。
5. 使用多码本量化稳定联合目标。
6. 评估环节：采用轻量规划读出器和GPT风格的下一令牌世界模型，检验同一套学习令牌。

### 主要贡献
- 提出一种统一的分词器，同时利用表征引导和几何增强来学习离散令牌。
- 在NAVSIM实验上展示了改进的重构保真度和表征一致性。
- 在固定解码器下取得有竞争力的规划性能，以及匹配设置下更好的生成质量。

### 局限性
摘要未提供足够信息，如：未讨论在不同驾驶场景或复杂环境下的鲁棒性，也未提及计算开销或与现有方法的具体对比数字。

### 阅读优先级
中  
理由：论文聚焦自动驾驶中的分词器设计，方法有明确创新点（结合表征引导和几何监督），并给出了多项任务评估。但摘要未详细披露对比基线或消融实验的具体结果，且未讨论实际部署限制，适合相关领域研究者关注，对一般读者优先级中等。

</details>

<details>
<summary>Abstract</summary>

Discrete visual tokens should provide a compact representation for both token-based world modeling and planning in autonomous driving. However, most tokenizers are inherited from image generation and are optimized mainly for pixel reconstruction, which may leave a gap between what is easy to generate and what is useful to decode for driving decisions. We present a representation-guided and geometry-enhanced tokenizer that learns discrete tokens under joint supervision. The tokenizer aligns its discrete bottleneck with a frozen DINO feature space through feature decoding, while preserving appearance via RGB reconstruction with perceptual and adversarial losses. To inject geometric state-related cues, we add adjacent-frame depth and relative-pose supervision during training and stabilize joint objectives with multi-codebook quantization. We evaluate the same learned tokens with a lightweight planning readout and a GPT-style next-token world model. Experiments on NAVSIM show improved reconstruction fidelity and representation consistency, competitive planning performance under a fixed decoder, and better generative quality under matched settings.

</details>

#### 2026-06-01 - Trans2Occ: Voxel Occupancy Estimation and Grasp for Transparent Objects from Simulation to Reality

**Authors:** Yixuan Yang, Sha Zhang, Rui Li, Zhenfei Yin, Xinzhu Ma, Yiran Qin, Lei Bai, Xudong Xu, Shilin Shan, Wangmeng Zuo, Yanyong Zhang, Wanli Ouyang, Feng Zheng, Shixiang Tang, Dongzhan Zhou
**Links:** [abs](https://arxiv.org/abs/2606.01777) - [pdf](https://arxiv.org/pdf/2606.01777)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, robotics, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Trans2Occ: Voxel Occupancy Estimation and Grasp for Transparent Objects from Simulation to Reality
- 作者：Yixuan Yang, Sha Zhang, Rui Li, Zhenfei Yin, Xinzhu Ma, Yiran Qin, Lei Bai, Xudong Xu, Shilin Shan, Wangmeng Zuo, Yanyong Zhang, Wanli Ouyang, Feng Zheng, Shixiang Tang, Dongzhan Zhou
- 出版日期：2026-06-01
- 分类：Embodied / Robotics / AR Applications
- 链接：arXiv:2606.01777

### 一句话总结
提出一种基于单视图RGB输入的透明物体体素占用预测框架，通过仿真数据训练后可直接迁移到真实机器人抓取场景，无需微调。

### 研究问题
透明物体因折射和反射导致深度传感不可靠，现有依赖多视图重建或深度补全的方法难以在真实机器人系统中规模化部署。

### 核心思路/方法
1. 输入：单视图RGB图像。
2. 方法：直接从单张RGB图像预测体素空间占用（voxel-space occupancy），形成几何感知表示。
3. 训练数据：构建仿真管线，在不同材质和光照条件下生成配对的RGB图像和体素占用标注。
4. 迁移策略：预测的占用表示对域偏移鲁棒，从仿真迁移到真实场景无需微调。
5. 下游任务：基于占用的简单规则抓取策略实现可靠抓取。

### 主要贡献
1. 提出基于单视图RGB的透明物体体素占用预测框架，无需深度信息或多视图。
2. 构建仿真数据生成管线，支持大规模训练。
3. 在仿真和真实环境中验证了占用量化表示的域迁移能力及抓取性能。

### 局限性
摘要未提供足够信息。未讨论模型在极端光照、复杂背景或遮挡场景下的失败情况，也未提及计算效率或实时性评估。

### 阅读优先级
中
理由：方向聚焦于透明物体感知与抓取，属于移动机器人和操作领域的特定难题，方法（单视图体素占用+仿真迁移）有实用价值，但创新点较为常规，建议对该子领域有直接兴趣的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Transparent objects remain challenging for robotic perception due to unreliable depth sensing caused by refraction and reflection. While prior approaches rely on multi-view reconstruction or depth completion, they are often difficult to scale or deploy in real-world robotic systems. In this paper, we present a practical framework for transparent object perception and manipulation based on single-view RGB input. Our approach predicts voxel-space occupancy directly from a single image, providing a geometry-aware representation that supports downstream robotic grasping. To enable large-scale training, we construct a simulation pipeline that generates paired RGB images and voxel occupancy annotations under diverse materials and lighting conditions. We demonstrate that the predicted occupancy representation is robust to domain shifts and transfers effectively from simulation to real-world robotic setups without fine-tuning. A simple rule-based grasping strategy built on top of the occupancy further achieves reliable grasp performance on transparent objects. Extensive experiments in both simulation and real-world environments show that our framework provides accurate 3D understanding and enables practical manipulation of transparent objects. These results suggest that single-view occupancy prediction offers a scalable and effective solution for transparent object perception in robotics.

</details>

#### 2026-06-01 - Hierarchical Object Representation for Spatial Robot Perception: Points, Meshes, and Superquadrics

**Authors:** Ceng Zhang, Wan Su, Mohamed Samshad, Gregory S. Chirikjian, Rajat Talak
**Links:** [abs](https://arxiv.org/abs/2606.01545) - [pdf](https://arxiv.org/pdf/2606.01545)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, robot perception, robot navigation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hierarchical Object Representation for Spatial Robot Perception: Points, Meshes, and Superquadrics
- 作者：Ceng Zhang, Wan Su, Mohamed Samshad, Gregory S. Chirikjian, Rajat Talak
- 出版日期：2026-06-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.01545

### 一句话总结
本文提出一种分层物体表示方法，包含点云、网格和超二次曲面多层次抽象，旨在提升机器人长时自主中的物体级重建、地图对齐和碰撞检测性能。

### 研究问题
如何为3D场景图（3DSG）中的物体设计一种分层几何表示，以同时支持高保真重建、鲁棒重定位和高效碰撞检测，并克服现有方法仅使用部分点云或3D边界框的局限性。

### 核心思路/方法
- 构建包含四个层次的分层物体表示：从原始传感器数据逐渐抽象为密集3D网格，再到超二次曲面等分析几何基元。
- 开发从RGB-D图像流生成该分层表示的流程，并在真实室内外开放集物体场景中验证。
- 在HOPE、ReplicaCAD、Kimera-Multi及使用Unitree B2机器人收集的NUS Campus数据集上评估性能，重点比较基于超二次曲面的地图对齐方法与现有方法ROMAN。

### 主要贡献
- 提出一种面向空间机器人感知的分层物体表示结构，兼顾保真度与稀疏性。
- 构建完整pipeline，能从机器人采集的RGB-D流实时生成该表示。
- 实验验证其在室内外多数据集上的有效性，且超二次曲面地图对齐方法优于当前最优的基于物体的地图对齐方法ROMAN。

### 局限性
摘要未提供足够信息，例如未提及该方法在极端动态场景或感知失效下的鲁棒性，也未讨论计算实时性限制或不同物体类别下的性能差异。

### 阅读优先级
**高**。理由：该工作针对3DSG中物体几何表示这一被忽视的问题提出创新方案，采用四层分层结构兼顾抽象效率与几何保真度，并在多个公开数据集和实际机器人实验中取得优于SOTA对齐方法的结果。对于从事机器人感知、SLAM或空间智能的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Hierarchical 3D Scene Graphs (3DSG) have emerged as an actionable and scalable representation for long-term autonomy incorporating metric, semantic, and topological information in the scene. However, the question of geometric representation of objects in 3DSG has been overlooked as most methods use simplified geometric models such as partial point clouds or 3D bounding boxes. In this work, we introduce a hierarchical object representation that can be leveraged for high-fidelity object-level reconstruction, object-based robust re-localization or map alignment, and efficient and analytical collision checking for safe robot navigation planning in dense and cluttered environments. The representation is structurally organized into four distinct layers, progressively abstracting the scene from raw sensor data to dense 3D meshes to analytical primitives such as superquadrics, which provide a sparse and analytical representation for object geometry. We develop a pipeline that builds the hierarchical object representation from RGB-D image stream captured by a robot, and demonstrate its working in real-world open-set object scenes in both indoor and outdoor environments. Extensive experiments across diverse datasets including HOPE, ReplicaCAD, Kimera-Multi, and NUS Campus Dataset collected using Unitree B2 Robot validate our pipeline in both indoor and outdoor environments. We show that our superquadric-based map alignment method outperforms the current state-of-the-art object based map alignment method ROMAN. Our code can be found at https://github.com/perceptica-robotics/Hickory.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
