# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：58
- 分类分布：
  - Embodied / Robotics / AR Applications: 22
  - 3D Reconstruction & Multi-view Geometry: 19
  - Neural Scene Representations & Rendering: 9
  - Geometry Foundation Models: 7
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，基于你提供的论文列表，以下是中文科研趋势综合分析。

---

#### 今日主要趋势

基于今日的论文，可以归纳出以下几条显著趋势：

1.  **从“通用模型”走向“物理一致性”与“可交互仿真”**：许多工作不再仅仅追求重建的视觉保真度，而是强调生成内容与物理世界规律的一致性。这体现在：
    -   **自动驾驶仿真**：`CARLA-GS` 提出解耦视觉、推理与物理仿真，专为生成物理可行的边缘案例。
    -   **机器人交互**：`RoboSnap` 和 `OrchardBench` 专注于将真实场景转化为可交互、有物理属性的仿真环境。`OrchardBench` 甚至精确模拟了树枝的力学特性（断裂、弹性）和苹果果梗的拉力。
    -   **重建鲁棒性**：`NoDrift3R` 直接针对长序列重建中的位姿漂移，该问题本质上是几何一致性（而非外观一致性）的退化。
    -   **水下机器人**：`Disturbance-aware Motion Planning` 从“执行器扰动”这一物理层面出发优化重建质量，是感知与执行物理耦合的直接体现。

2.  **“本体感觉-环境感知”的深度融合**：机器人领域论文正试图打破本体状态（Proprioception）与环境视觉感知（Vision）之间的隔阂，通过显式的几何映射或统一的世界模型来提升策略性能。
    -   `GeoProp` 直接将机器人关节状态投影到图像平面采样特征，构建显式的视觉-本体对应关系。
    -   `RynnWorld-4D` 提出 RGB-DF（RGB+深度+光流）四维世界模型，认为这种多模态协同的表征更接近机器人末端的动作空间，从而缩小预测与规划之间的鸿沟。
    -   `TouchWorld` 则从另一个维度切入，将触觉信号作为关键变量，通过层级架构将高层规划、触觉世界模型预测与触觉反馈精化进行分离，实现了触觉的预测性与反应性的统一。

3.  **“生成式”与“判别式”任务的界限进一步模糊**：传统上认为生成模型（如扩散模型）擅长渲染，而判别模型（如分类器）擅长理解。现在的趋势是利用生成模型的内部表征来直接服务理解任务。
    -   `Gen4U` 是这一趋势的直接体现。它系统地分析了视频扩散模型的中间表征，发现其在低层几何（如深度、位姿）和高层语义（如分类）上都极具潜力，从而通过单次前向传播的方式，在不进行微调的情况下，实现了生成与理解的统一。
    -   `ProxyPose` 则将 6-DoF 姿态跟踪这种典型的3D理解任务，转化为“视频到视频”的生成任务（生成一个代理多面体视频），然后从代理视频中解析姿态。这本质上是将复杂理解任务“外包”给强大的生成模型。

4.  **对“场景理解”维度的扩展：从单场景、静态到跨场景、动态和4D**。
    -   **跨场景推理**：`CAIRN` 专门针对多房间、有拓扑结构的3D场景理解。它不再将每个房间独立处理，而是建模房间间的连接关系。
    -   **城市级尺度**：`WildCity` 挑战了城市尺度的重建与空间智能，将场景理解推向了与人类认知相当的规模。
    -   **时间与交互维度**：`RynnWorld-4D` 和 `Point as Skeleton` 将预测扩展到了未来时间步，不仅理解“现在是什么”，还要预测“下一步会变成什么样”。这在自动驾驶和机器人操作中尤为关键。

#### 技术路线观察

| 技术方向 | 论文/方法 | 技术侧重点 |
| :--- | :--- | :--- |
| **几何基础模型** | `NoDrift3R` | 聚焦于无位姿前馈重建的**几何漂移**问题。核心创新不在于建模方法本身，而在于通过“几何-外观”显式耦合（Raymap）和课程式训练策略解决长序列下的几何退化。 |
| **3D/4D 重建与表示** | `CARLA-GS`, `GeoGS-SLAM`, `WildCity`, `Disturbance-aware Motion Planning` | 呈现**多元化**发展：<br> - **与仿真深度绑定** (`CARLA-GS`, `WildCity`)：重建服务于仿真，强调 **可编辑性** 和 **物理属性**。<br> - **极简表征** (`GeoGS-SLAM`)：专为下游任务优化，舍弃外观参数，只保留 **纯几何** 的高斯泼溅，显著压缩存储和计算。<br> - **与环境感知耦合** (`Disturbance-aware Motion Planning`)：重建质量被作为下游优化目标，而非上游独立任务。 |
| **神经场景表示与渲染** | `SoccerNet 2026`, `RoboSnap`, `Gen4U`, `ProxyPose` | **应用驱动**特征明显：<br> - **体育分析** (`SoccerNet 2026`)：新视角渲染是任务之一，更关注其作为体育视频理解基准的一部分。<br> - **机器人仿真** (`RoboSnap`)：使用3DGS作为 **视觉背景层**，以分离物理交互区域，展示了3DGS作为模块化工具的价值。<br> - **模型表征复用** (`Gen4U`, `ProxyPose`)：不再将扩散模型/渲染模型视为最终输出，而是将其内部表征和解码能力作为 **分析工具或预处理步骤**。 |
| **机器人/AR应用** | `HumAIN`, `TouchWorld`, `GeoProp`, `RynnWorld-4D`, `CAIRN`, `OrchardBench` | **多层次、多模态融合**是核心主线：<br> - **社会线索融合** (`HumAIN`)：将隐式人体骨架 cues 融入导航规划。<br> - **触觉与视觉分层融合** (`TouchWorld`)：层次化架构，解耦不同信号的时间尺度和功能。<br> - **本体与视觉几何融合** (`GeoProp`)：显式几何投影，轻量高效。<br> - **4D动态融合** (`RynnWorld-4D`)：未来状态预测，在时间维度上扩展感知。<br> - **拓扑与语义融合** (`CAIRN`)：3D-LLM 中加入房间拓扑信息。<br> - **专用物理仿真** (`OrchardBench`)：为特定任务（农业采摘）构建高保真物理仿真，强调域随机化和可重复性。 |

#### 值得优先阅读的论文

1.  **`NoDrift3R`**：
    -   **理由**：该工作直接针对当前无位姿前馈3D重建（如DUSt3R系列）的 **核心瓶颈——长序列漂移** 提出解决方案。`Raymap-Guided Coupling` 模块和双频率训练策略的设计思路，对于理解如何稳定大规模、端到端的3D重建模型具有重要的方法论意义。

2.  **`TouchWorld`**：
    -   **理由**：它提出了一种 **层次化** 的多模态基础模型架构，将“高层语义规划”、“预测性世界模型”和“反应式反馈控制”分离。这种架构设计思路非常清晰，为解决具身智能中“慢思考”与“快反应”的矛盾提供了可操作的范式，且触觉信号的引入是处理精细操作的关键。

3.  **`RynnWorld-4D`**：
    -   **理由**：它提出了 **RGB-DF（RGB + 深度 + 光流）** 这一物理上更接地气的世界模型表征。从问题定义、模型设计到大规模数据集，论文工作非常完整。对于研究“如何让世界模型真正服务于机器人控制”的读者，此工作是必读的参考基准。

4.  **`GeoProp`**：
    -   **理由**：看似简单，却直击当前视觉-语言-动作模型（VLA）中一个 **普遍被忽视的痛点**——本体感觉与视觉的对齐。其“几何投影+特征采样”的方案极其轻量、即插即用且有效。这不仅是技术贡献，更是对社区研究方向的有力提醒。

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-10T10:50:07-04:00
**Total number of papers:** 68
**Number of papers added in the latest update:** 14
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

#### 2026-07-08 - NoDrift3R: Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction

**Authors:** Xiangyu Sun, Liu Liu, Seungkwon Yang, Jingbing Han, Seungtae Nam, Zhizhong Su, Eunbyung Park
**Links:** [abs](https://arxiv.org/abs/2607.07168) - [pdf](https://arxiv.org/pdf/2607.07168)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, scene reconstruction, SfM, camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NoDrift3R: Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction
- 作者：Xiangyu Sun, Liu Liu, Seungkwon Yang, Jingbing Han, Seungtae Nam, Zhizhong Su, Eunbyung Park
- 出版日期：2026-07-08
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering（次要）
- 链接：摘要：https://arxiv.org/abs/2607.07168 ；PDF：https://arxiv.org/pdf/2607.07168

### 一句话总结
本文提出NoDrift3R，通过显式耦合几何与外观的Raymap导向模块（RGC）和双频率视点调度策略，解决了无位姿前馈3D重建在长序列中的累积漂移问题。

### 研究问题
如何提高无位姿前馈3D高斯泼溅（3DGS）在长图像序列中的重建稳定性，消除因累积相机位姿估计漂移导致的渲染质量下降。

### 核心思路/方法
1. **识别瓶颈**：指出长序列下位姿漂移是限制重建质量的主要因素，而SfM伪真值引入传感器噪声、纯渲染监督则导致优化不稳定。
2. **Raymap导向耦合法（RGC）**：将高斯中心锚定到raymap生成的几何上，统一优化RGB重建、raymap一致性和相机正则化，形成几何与外观的双向反馈循环。
3. **双频率视点调度策略**：结合“从易到难”区间扩展与短间隔对回放，稳定大时间跨度的学习过程。

### 主要贡献
1. 首次揭示并针对性解决无位姿前馈3DGS在长序列中的漂移问题。
2. 提出RGC模块，实现几何与外观的显式协同，通过统一目标函数优化形成双向反馈。
3. 引入双频率视点调度策略，稳定宽时间范围下的学习。
4. 在域内和跨域数据集上验证了渲染和位姿估计的一致提升，尤其在长序列上鲁棒性显著增强。

### 局限性
摘要未提供实验的失败案例或具体局限性分析，例如对极端长度序列或复杂光照条件的表现未明确说明。

### 阅读优先级
**高**
理由：该工作针对无位姿3D重建中长期存在的漂移这一核心难点，提出了系统性的解决方案（RGC耦合+调度策略），并在多个数据集上验证了有效性，对3D重建、几何基础模型领域的研究者和工程师具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Pose-Free Feed-forward 3D Gaussian Splatting (3DGS) has recently emerged as a powerful paradigm for fast scene reconstruction. However, its performance degrades significantly in long image sequences due to cumulative camera pose estimation drift, which propagates errors into geometric modeling and severely limits rendering fidelity. In this work, we revisit the long-sequence bottleneck and identify pose drift as the primary factor restricting reconstruction quality. Furthermore, while SfM-based pseudo ground-truth poses introduce sensor noise, purely rendering-based supervision often leads to optimization instability and local minima due to the entangled optimization of geometry and pose. To address the challenges, we propose a synergistic pose-free framework that explicitly couples geometry and appearance via a Raymap-Guided Coupling Module (RGC). Concretely, we anchor Gaussian centers to raymap-induced geometry and jointly optimize RGB reconstruction, raymap consistency, and camera regularization under a unified objective, yielding a bidirectional feedback loop: stronger geometry improves rendering, and appearance supervision in turn refines geometry and pose. To further stabilize learning across wide temporal ranges, we introduce a Dual-Frequency Viewpoint Scheduling strategy that combines easy-to-hard interval expansion with replay of short-interval pairs. Extensive experiments across in-domain and cross-domain datasets show consistent gains in both rendering and pose estimation, with notably improved robustness on long sequences. Ablation studies validate our central insight: explicitly designed geometry-appearance synergy is the key to scalable and drift-robust pose-free feed-forward 3D reconstruction.

</details>

#### 2026-07-07 - TRIG: Trajectory-Rig Decoupled Metric Geometry Learning

**Authors:** Lizhou Liao, Wentao Xu, Handong Wang, Lirong Yang, Shuai Yang, Weiwei Liu, Chang Huang
**Links:** [abs](https://arxiv.org/abs/2607.05801) - [pdf](https://arxiv.org/pdf/2607.05801)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** depth prediction, geometric reasoning, metric depth, 3D reconstruction, pose estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRIG: Trajectory-Rig Decoupled Metric Geometry Learning
- 作者：Lizhou Liao, Wentao Xu, Handong Wang, Lirong Yang, Shuai Yang, Weiwei Liu, Chang Huang
- 出版日期：2026-07-07
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.05801；PDF: https://arxiv.org/pdf/2607.05801

### 一句话总结
本文提出TRIG，一种将相机位姿分解为自车轨迹和相机刚体拓扑的几何感知框架，用于提升自动驾驶中位姿估计、深度预测和3D重建的度量一致性。

### 研究问题
现有视觉几何模型在处理刚性多相机驾驶系统时，将相机位姿编码为纠缠表示，无法分离时变的自我运动与静态的相机刚体几何，从而限制了车辆侧几何先验的利用。

### 核心思路/方法
TRIG框架将相机位姿因子化为自我轨迹和相机刚体两部分，实现自运动与静态多相机拓扑的分别建模。具体引入解耦的位姿编码与监督，分别约束轨迹演化与刚体几何以实现度量一致学习；同时采用稀疏时空注意力，将跨相机交互与时间聚合分离，在保持几何推理能力的同时降低全局注意力计算成本。

### 主要贡献
1. 提出轨迹-刚体解耦指标几何学习框架（TRIG），专门用于自动驾驶场景。
2. 引入解耦的位姿编码与监督，实现轨迹与刚体几何的独立度量约束。
3. 设计稀疏时空注意力机制，分离跨相机交互与时间聚合，提升效率。
4. 在五个自动驾驶基准上，TRIG在姿态估计、度量深度预测和3D重建方面达到最先进水平。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中等。理由：该工作聚焦自动驾驶中多相机几何建模的特定问题，对基于视觉的自动驾驶感知方向有实际改进。但若读者不对车辆运动学分解或多相机范式特别感兴趣，则创新点针对性较强。

</details>

<details>
<summary>Abstract</summary>

Vision-centric autonomous driving requires accurate metric geometry and ego-motion estimation from synchronized multi-camera observations. Recent visual geometry models show strong performance in pose estimation, depth prediction, and 3D reconstruction, but are not tailored to rigid multi-camera driving systems. They often encode camera poses as entangled representations, in which time-varying ego-motion and static camera-rig geometry are jointly modeled, limiting the utilization of vehicle-side geometric priors. We propose Trajectory-Rig Decoupled Metric Geometry Learning (TRIG), a geometry perception framework for autonomous driving. TRIG factorizes camera poses into ego-trajectory and camera-rig components, enabling separate modeling of ego-motion and static multi-camera topology. We introduce decoupled pose encoding and supervision, which separately constrain trajectory evolution and rig geometry for metric-consistent learning. Moreover, sparse Temporal--Spatial attention separates cross-camera interaction from temporal aggregation, reducing global attention cost while preserving geometric reasoning. Experiments on five autonomous driving benchmarks show that TRIG achieves state-of-the-art performance in pose estimation, metric depth prediction, and 3D reconstruction.

</details>

#### 2026-07-06 - Learning 4D Geometric Priors for Inference-Efficient World Action Models

**Authors:** Jianjun Zhang, Jian Zhu, Taiyi Su, Chong Ma, Zitai Huang, Yi Xu, Hanli Wang
**Links:** [abs](https://arxiv.org/abs/2607.05468) - [pdf](https://arxiv.org/pdf/2607.05468)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning 4D Geometric Priors for Inference-Efficient World Action Models
- 作者：Jianjun Zhang, Jian Zhu, Taiyi Su, Chong Ma, Zitai Huang, Yi Xu, Hanli Wang
- 出版日期：2026-07-06
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.05468

### 一句话总结
本文提出MECo-WAM，通过在训练时引入4D几何先验知识提升世界动作模型的操控性能，且推理时不增加计算开销。

### 研究问题
现有视频-动作联合训练方法主要优化面向外观的视频潜在表示，未能充分捕获随时间演化的几何信息，导致机器人精确操控能力受限。

### 核心思路/方法
1. **多专家协同训练**：在训练阶段，结合视频专家、动作专家和轻量级4D专家（受冻结VGGT编码器的关系目标监督），通过非对称专家可见性防止辅助几何信息产生非因果捷径。
2. **衰减式4D读-掩码注意力**：在训练早期提供受限的当前帧几何引导，并逐步移除该依赖，以将几何知识迁移到视频-动作主通路中。
3. **动作感知时序几何蒸馏**：对齐帧内几何关系及其时序演化，同时强调与机器人动作最相关的视觉区域。
4. **部署时无额外开销**：所有辅助4D组件在部署时被移除，保持原有轻量推理图。

### 主要贡献
- 提出注入动作相关4D几何先验的训练框架，提升视频-动作表示质量。
- 设计衰减式4D读-掩码注意力和动作感知时序几何蒸馏，实现知识迁移且不引入非因果偏差。
- 在LIBERO（98.2%）、RoboTwin 2.0（92.6%）及真实世界操控任务上验证了性能提升，且推理成本不变。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法聚焦于机器人操控的视觉-动作建模，属于几何先验与强化学习/模仿学习的交叉方向，对相关领域研究者有参考价值；但摘要未提供方法在复杂场景下的泛化性或失败案例分析，限制了对全面性的评估。

</details>

<details>
<summary>Abstract</summary>

World Action Models (WAMs) have shown strong potential for robotic manipulation by jointly modeling visual future dynamics and executable action sequences. However, existing video-action co-training methods primarily optimize appearance-oriented video latents, which may insufficiently capture the temporally evolving geometry required for precise manipulation. We propose MECo-WAM, a Multi-Expert Co-Training World Action Model that injects action-relevant 4D geometric priors into video-action representations while preserving the original lightweight inference graph. During training, MECo-WAM combines video and action experts with a lightweight 4D expert supervised by relational targets from a frozen VGGT encoder. Asymmetric expert visibility prevents non-causal shortcuts from auxiliary geometry to action generation. To transfer geometric knowledge into the deployed video-action pathway, we introduce decayed 4D read-mask attention, which provides restricted current-frame geometric guidance early in training and progressively removes this dependency. We further propose action-aware temporal geometric distillation, which aligns within-frame geometric relations and their temporal evolution while emphasizing visual regions most relevant to robot actions. At deployment, all auxiliary 4D components are removed. Experiments on LIBERO (98.2%), RoboTwin 2.0 (92.6%), and challenging real-world manipulation tasks show that MECo-WAM improves manipulation performance without increasing inference cost.

</details>

#### 2026-07-06 - Reference-Induced Consensus for Selective Posed-Reference Visual Localization

**Authors:** Wonseok Kang, Jaehyun Kim, Jeongmin Lee, Tae-Wan Kim
**Links:** [abs](https://arxiv.org/abs/2607.04722) - [pdf](https://arxiv.org/pdf/2607.04722)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, point map, SfM, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reference-Induced Consensus for Selective Posed-Reference Visual Localization
- 作者：Wonseok Kang, Jaehyun Kim, Jeongmin Lee, Tae-Wan Kim
- 出版日期：2026-07-06
- 分类：Geometry Foundation Models（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：https://arxiv.org/abs/2607.04722

### 一句话总结
本文提出RIC-Loc，一种无需场景训练、不依赖SfM点云的定位方法，通过参考姿态诱导的假设共识估计查询位姿，并利用假设结构输出可靠性得分实现选择性地故障检测。

### 研究问题
如何在不使用SfM地图点、无需场景训练的前提下，仅利用参考姿态（而非预计算3D点）实现精确的视觉定位，并可靠地检测定位失败。

### 核心思路/方法
1. 使用冻结的VGGT网络预测查询图像与所选参考图像的局部相机姿态、深度以及查询-参考对应轨迹。
2. 每对参考诱导一个地图坐标系下的SE(3)查询位姿假设，通过鲁棒共识估计最终位姿。
3. 保留假设结构，从中推导两个可靠性分数：空间离散度（spatial dispersion）和轨迹条件协方差分数（track-conditioned covariance score）。
4. 在协方差可计算的子集上，联合使用两个分数在室内、室外及大规模低纹理基准上进行免真值的故障检测。

### 主要贡献
- 提出一种无SfM地图点、无场景训练的定位器，主估计器仅依赖参考姿态。
- 引入基于假设结构的两个可靠性分数（空间离散度与轨迹条件协方差），在各类场景中一致性优于标准的检索分数差距和随机排序。
- 无需每场景训练，共识估计器在室内达到与基于结构的方法相当的精度，并优于可比的纯前馈基线。
- 在低纹理场景中，协方差分数表现最强；在纹理场景中，联合策略最有效。

### 局限性
摘要未提供足够信息。论文未明确说明在高动态变化场景中的性能、计算开销细节或对参考姿态数量的敏感性。

### 阅读优先级
高  
理由：该方法解决了传统定位中依赖SfM点云和场景训练的痛点，且通过假设结构实现了可靠的故障检测，对几何基础模型和机器人/AR应用领域有直接参考价值，实验结果覆盖多种复杂场景。

</details>

<details>
<summary>Abstract</summary>

We present RIC-Loc (Reference-Induced Consensus localization), a scene-training-free posed-reference localizer that is SfM-point-map-free in its main estimator: it uses known reference poses, but not precomputed SfM 3D map points, query-to-map 2D-3D matches, or query-to-map PnP. A frozen VGGT pass predicts local camera poses, depth, and query-reference tracks for a query and selected references. Each reference induces one map-frame SE(3) query-pose hypothesis, robust consensus estimates the pose, and the preserved hypothesis structure yields two reliability scores: spatial dispersion and a track-conditioned covariance score. On the covariance-eligible set, the two scores are complementary for held-out, ground-truth-free failure detection across indoor, outdoor, and large-scale low-texture benchmarks: the joint policy is strongest in textured scenes and the covariance score in the low-texture regime, and the hypothesis-derived scores consistently outperform the standard retrieval-score gap and random rankings. Without per-scene training the consensus estimator remains accurate -- competitive with structure-based localization indoors and improving over a comparable feed-forward baseline -- giving an effective selective operating regime for posed-reference localization. Code is available at https://github.com/SNU-DLLAB/ric_loc.

</details>

#### 2026-07-05 - AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction

**Authors:** Badrinath Singhal, Srihari K G, Sreehari Iyer, Ankit Dhiman, Venkatesh Babu Radhakrishnan
**Links:** [abs](https://arxiv.org/abs/2607.04256) - [pdf](https://arxiv.org/pdf/2607.04256)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction
- 作者：Badrinath Singhal, Srihari K G, Sreehari Iyer, Ankit Dhiman, Venkatesh Babu Radhakrishnan
- 出版日期：2026-07-05
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.04256

### 一句话总结
本文提出一种基于纹理感知的前馈式3D高斯分配方法，通过自适应剪枝低纹理区域的冗余高斯原语，在不破坏前馈范式的前提下减少表示冗余。

### 研究问题
当前前馈式3D重建方法预测像素对齐的高斯原语，导致高度冗余的表示。如何在不引入伪影且保持前馈范式的情况下，有效去除冗余高斯原语？

### 核心思路/方法
方法基于观察：高频区域需要更多高斯原语，低频区域可用更少原语表示。通过三个关键组件实现：
1. **纹理估计**：捕捉场景细节的空间变化；
2. **纹理感知剪枝**：从低频区域移除冗余高斯原语；
3. **自适应高斯头**：预测保留原语的修正属性，不破坏前馈范式。

### 主要贡献
- 提出显式利用局部纹理信息控制高斯原语数量的新方法；
- 设计纹理感知剪枝策略，避免前馈推理时产生严重伪影；
- 在多个数据集（RE10K, ACID, DL3DV, Tanks and Temples, DTU）上验证有效性，并通过消融实验确认各组件的贡献。

### 局限性
摘要未提供足够信息。具体局限性如：未讨论剪枝后对极端复杂场景的鲁棒性、计算开销变化、或对未见纹理分布的泛化能力。

### 阅读优先级：中
理由：该方法针对前馈式3D重建中的冗余表示问题提出实用改进，在多个数据集上验证了有效性。但论文核心思路（纹理感知剪枝）属于对现有技术的优化整合，创新性有限，适合对3D高斯泼溅或实时重建感兴趣的研究者参考。

</details>

<details>
<summary>Abstract</summary>

Current feed-forward 3D reconstruction methods predict pixel aligned Gaussian primitives, resulting in highly redundant representations. A natural solution is to prune the redundant Gaussians, but naive pruning introduces severe artifacts and often requires inference time fine-tuning, breaking the feed-forward paradigm. Based on previous works, high frequency regions require more Gaussian primitives, while low frequency regions can be represented with significantly fewer primitives. Motivated by this, we propose a novel approach to explicitly control the number of Gaussians by leveraging local texture information. Our approach achieves this through three key components: (1) texture estimation to capture spatial variation in scene detail, (2) texture-aware pruning that removes redundant Gaussians from low frequency regions, and (3) an adaptive Gaussian head that predicts the modified attributes of the retained primitives without breaking the feed-forward paradigm. Experiments on RE10K, ACID, DL3DV, Tanks and Temples, and DTU demonstrate the effectiveness of our approach, while ablation studies validate the contributions of its key components.

</details>

#### 2026-07-05 - The Multipath Blind Spot: $K$-Agnostic Robust Calibration for Sparse-Anchor Metric Depth from Frozen Foundations

**Authors:** Sohag Roy, Rajesh Misra, Swami Shastravidyananda, Tamal Maharaj
**Links:** [abs](https://arxiv.org/abs/2607.04101) - [pdf](https://arxiv.org/pdf/2607.04101)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** metric depth, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Multipath Blind Spot: $K$-Agnostic Robust Calibration for Sparse-Anchor Metric Depth from Frozen Foundations
- 作者：Sohag Roy, Rajesh Misra, Swami Shastravidyananda, Tamal Maharaj
- 出版日期：2026-07-05T03:42:21Z
- 分类：Geometry Foundation Models
- 链接：论文摘要链接：https://arxiv.org/abs/2607.04101；PDF链接：https://arxiv.org/pdf/2607.04101

### 一句话总结
本文针对稀疏锚点深度校准中实际传感器产生的多路径异常值问题，提出一种无参数、推理时有效的鲁棒校准方法MRAC，通过基于基础模型一致性的锚点筛选机制显著提升性能，并在多个基准上超越现有方法。

### 研究问题
现有的稀疏锚点度量深度校准方法假设锚点是无噪声的，但真实传感器（如ToF）的异常值以错误数值形式存在（时间飞行多路径、混合像素），导致基于残差在CFA上的校准方法失效。最强的公开部署方法VI-Depth存在结构性多路径盲点：对缺失锚点鲁棒，但在锚点存在但错误时表现不佳。本文旨在解决这一问题。

### 核心思路/方法
提出Multipath-Robust Anchor Calibration（MRAC），一个无参数、推理时运行的包装器。核心步骤：
1. **锚点筛选**：在调用校准头之前，先用Theil-Sen拟合和中位数绝对偏差（MAD）检验，根据基础模型自身的相对深度顺序一致性来筛选锚点。
2. **应用**：筛选后的锚点直接喂入校准头，无需额外训练或学习参数。
3. **效率**：筛选过程在CPU上约需50微秒，且支持从单个检查点处理锚点数量K∈[5,200]的预算。

### 主要贡献
1. 揭示了现有稀疏锚点校准方法在多路径异常值下的结构性问题，并识别VI-Depth的盲点。
2. 提出MRAC，一种无参数、推理时、高效的鲁棒校准方法，无需重训练即可实现状态压缩（从相同骨干和架构的控制实验看，在320个单元的基准中，MRAC在84%的单元上严格获胜）。
3. 在12个受损多路径单元和16个KITTI单元上全面超越VI-Depth，在KITTI多路径绝对相对误差（AbsRel）上降低3.2倍（从0.489到0.151）。

### 局限性
摘要未提供具体局限性信息。

### 阅读优先级
**高**。
理由：本文直接针对实际传感器噪声这一关键工程问题（多路径异常值），提出了一种简单高效（无参数、推理时快）、显著提升性能的方法（在多数据集和异常值族上全面超越基线），尤其适合关注度量深度估算鲁棒性、传感器融合或自动驾驶/机器人的研究者。

</details>

<details>
<summary>Abstract</summary>

Monocular depth foundations predict domain-general relative depth but lack absolute scale; a handful of sparse metric anchors from a range sensor can calibrate them to metric depth, an attractive alternative to metric-supervised training. Existing sparse-anchor calibration methods, however, assume the anchors are clean, whereas real sensors produce outliers that are present with the wrong value -- time-of-flight multipath, mixed pixels -- not merely missing. We show that the established residual-on-CFA calibration recipe collapses under such outliers, and that the strongest publicly deployed method, VI-Depth, has a structural multipath blind spot: robust to missing anchors, it falls behind an unprotected baseline on three of four datasets when anchors are present but wrong. We propose Multipath-Robust Anchor Calibration (MRAC), a parameter-free, inference-time wrapper that gates anchors by foundation consistency -- a Theil--Sen fit and a median-absolute-deviation test against the foundation's own relative-depth ordering -- before a single call to the calibration head. MRAC adds no learned parameters, runs its selection in $\approx 50\,μ$s on CPU, and serves anchor budgets $K \in [5,200]$ from one checkpoint. On a $320$-cell benchmark with a same-backbone, same-architecture control, MRAC strictly wins $84\%$ of same-backbone cells across all four outlier families and, against VI-Depth, wins all twelve corrupted multipath cells and all sixteen KITTI cells, reducing KITTI multipath AbsRel by $3.2\times$ ($0.489$ to $0.151$) at zero retraining.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

#### 2026-07-09 - LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models

**Authors:** Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, Yu-Lun Liu
**Links:** [abs](https://arxiv.org/abs/2607.08770) - [pdf](https://arxiv.org/pdf/2607.08770)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>Abstract</summary>

Recovering high-quality video from sparse event streams is a challenging task. Regression methods often blur textures, while existing generative models struggle with long-term stability. We propose LongE2V, a novel approach that leverages pre-trained video diffusion priors to jointly handle event-based video reconstruction, prediction, and frame interpolation. By fine-tuning a foundational video model, our approach achieves high data efficiency and superior perceptual quality. We introduce Autoregressive Unrolling and Adaptive Context Switching to mitigate temporal drift in extremely long sequences. We also propose Reencoding Alignment with Cross Residual Correction to ensure precise bidirectional consistency during frame interpolation. Furthermore, Event Voxel Density Augmentation ensures robustness across varying sensor resolutions. Extensive experiments on real-world benchmarks demonstrate that LongE2V outperforms state-of-the-art methods across all three tasks, exhibiting exceptional temporal coherence and zero-shot generalization. Project page: https://cdfan0627.github.io/LongE2V-page/

</details>

#### 2026-07-09 - On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting

**Authors:** In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong
**Links:** [abs](https://arxiv.org/abs/2607.08250) - [pdf](https://arxiv.org/pdf/2607.08250)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

Dynamic scene reconstruction remains challenging due to the heterogeneous and spatially varying nature of real-world motion. Although recent 3D Gaussian Splatting methods have introduced diverse deformation formulations for dynamic novel view synthesis, each method typically relies on a single deformation model within its representation, which limits robustness across diverse dynamic scenarios. In this work, we study a fundamental problem-multi-deformation modeling for dynamic 3D Gaussian representations-under two distinct integration constraints that differ in when and how multiple deformation experts interact during training. From a Mixture-of-Experts (MoE) perspective, we view multi-deformation modeling as the problem of combining multiple specialized deformation models within a unified 3D representation. We first introduce Mixture of Deformation Experts (MoDE), which integrates multiple deformation experts directly into the deformable Gaussian Splatting pipeline through joint optimization. In MoDE, experts operate on a shared canonical Gaussian representation, enabling multi-deformation modeling without introducing additional training stages or modifying the original optimization schedule. In contrast, we further present Mixture of Experts for Dynamic Gaussian Splatting (MoE-GS) under a different integration constraint, where deformation experts are optimized independently and combined through a separate routing stage. As a result, expert interaction occurs over non-canonical Gaussian representations after individual optimization. Together, these two approaches provide alternative strategies for multi-deformation modeling, clarifying how integration constraints shape the design and behavior of deformation experts in dynamic 3D Gaussian representations. Our code is available at: https://github.com/cvsp-lab/MoE-GS-studio.

</details>

#### 2026-07-06 - DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting

**Authors:** Yimo Wang, Bin Kang, Shuojue Yang, Yueming Jin
**Links:** [abs](https://arxiv.org/abs/2607.04761) - [pdf](https://arxiv.org/pdf/2607.04761)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, 4D Gaussian, Gaussian Splatting, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting
- 作者：Yimo Wang, Bin Kang, Shuojue Yang, Yueming Jin
- 出版日期：2026-07-06T07:56:17Z
- 分类：动态/4D重建（主分类），神经场景表征与渲染、具身/机器人/AR应用（副分类）
- 链接：摘要：https://arxiv.org/abs/2607.04761，PDF：https://arxiv.org/pdf/2607.04761

### 一句话总结
提出一种几何与语义解耦的4D高斯泼溅框架，通过独立建模语义演变与几何形变，实现手术场景中文本提示下的实时、高保真重建与分割。

### 研究问题
现有将视觉-语言模型集成到可变形场的方法采用刚性耦合方案，将语义特征与几何扭曲紧密绑定，导致语义含义与物理解剖结构之间存在严重错位。

### 核心思路/方法
1. **HexPlane时空纠缠模块**：利用共享运动学潜在变量，在同步语义变化与场景动态的同时，显式地将语义更新与几何形变解耦。
2. **光栅化原生语义提取机制**：从拓扑连续的特征图中推断语义，以增强对重建伪影的鲁棒性。
3. **角度对齐优化策略**：符合原生超球面潜在空间，防止语义失真。

### 主要贡献
1. 提出语义与几何解耦的4D重建框架，实现更鲁棒的语义-解剖对齐。
2. 在CholecSeg8k和EndoVis18数据集上取得最优性能，增强几何完整性与连续分割能力，能应对剧烈组织形变与拓扑变化。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**
理由：该工作针对手术场景下的动态4D语义理解提出清晰的解耦思路，方法设计具有创新性。但摘要未提供消融实验或定量对比结果细节，且分类偏向医学图像与机器人应用，对通用4D重建领域参考价值有限。若读者关注手术导航或可变形场景语义分割，可优先阅读。

</details>

<details>
<summary>Abstract</summary>

Real-time, text-promptable 4D reconstruction is indispensable for autonomous surgical interaction. Severe misalignment between semantic meaning and physical anatomy still persists, largely because existing solutions integrate Vision-Language Models into deformable fields via a rigid coupling scheme that tightly binds semantic features to geometric warping. In this paper, we propose DeGenseGS, Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting, a novel framework that independently models semantic evolution and geometric deformation. Specifically, we propose a HexPlane-based spatiotemporal entanglement module that uses shared kinematic latents to synchronize semantic mutations with scene dynamics, while explicitly disentangling semantic updates from geometric deformation. To further ensure robustness against reconstruction artifacts, we devise a Rasterization-Native Semantic Extraction mechanism that infers semantics from topologically continuous feature maps. Additionally, we incorporate an angular-aligned optimization strategy that conforms to the native hyperspherical latent space, thereby preventing semantic distortion. Extensive evaluations on the CholecSeg8k and EndoVis18 datasets demonstrate that DeGenseGS achieves state-of-the-art performance. Our framework yields enhanced geometric completeness and robust semantic-anatomic alignment, enabling spatially continuous segmentation despite drastic tissue deformation and topological transitions.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-09 - Wat3R: Underwater 3D Geometry Learning without Annotations

**Authors:** Jiangwei Ren, Xingyu Jiang, Zijie Song, Wei Xu, Hongkai Lin, Dingkang Liang, Xiang Bai
**Links:** [abs](https://arxiv.org/abs/2607.08772) - [pdf](https://arxiv.org/pdf/2607.08772)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, depth estimation, point cloud reconstruction

<details>
<summary>Abstract</summary>

Estimating 3D geometry in underwater environments presents unique challenges due to light attenuation, scattering, and the absence of large-scale, high-quality 3D annotations. Pioneering methods rely on massive dense annotations that are impractical in underwater settings. In this paper, we propose Wat3R, a cross-domain semi-supervised learning framework designed to adapt feed-forward 3D reconstruction models from air to underwater scenes. Uniquely, our method eliminates the need for any annotated underwater data following a teacher-student architecture, that learns robust geometry representations merely on abundant unlabeled real underwater video footage. We also design a cross-view consistency loss that leverages geometric cues from other views to compensate for the information degradation in the current view caused by water attenuation and scattering. Furthermore, considering the lack of comprehensive evaluation benchmarks, we construct Water3D, a diverse dataset covering various water bodies and underwater scenarios, designed for geometric task evaluation. Experimental results demonstrate that Wat3R outperforms current state-of-the-art methods in underwater multi-view depth estimation and point cloud reconstruction. The dataset and code are available at https://github.com/LSXI7/Wat3R .

</details>

#### 2026-07-09 - ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device

**Authors:** Fabio Tosi, Luca Bartolomei, Matteo Poggi, Stefano Mattoccia
**Links:** [abs](https://arxiv.org/abs/2607.08771) - [pdf](https://arxiv.org/pdf/2607.08771)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>Abstract</summary>

Monocular depth estimation has seen remarkable progress through foundation models achieving robust zero-shot generalization, yet their computational demands place them far beyond the reach of embedded and mobile platforms. Lightweight alternatives exist, but have been developed almost exclusively within single-domain, self-supervised paradigms, failing silently under domain shift. We present ZipDepth, a compact monocular depth network that bridges this gap by combining an efficient reparameterizable encoder-decoder with large-scale knowledge distillation from a foundation model over a large multi-domain training set. Comprising just 6.1M parameters, ZipDepth runs at real-time rates from server GPUs to power-constrained devices, achieving the best trade-off between zero-shot accuracy and deployment efficiency among lightweight models across five benchmarks, taking a significant step towards the accuracy of foundation models with 50x more parameters.

</details>

#### 2026-07-09 - Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction

**Authors:** Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi
**Links:** [abs](https://arxiv.org/abs/2607.08769) - [pdf](https://arxiv.org/pdf/2607.08769)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, monocular depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Scaling 3D Gaussian Splatting (3DGS) to large outdoor scenes is costly in both data acquisition and computation. Adopting panoramic images with equirectangular projection (ERP) can reduce capture effort via their full $360^{\circ}$ field of view, yet the resulting omnipresent visibility invalidates existing partitioning strategies that rely on local camera frustums, causing block-wise optimization to degenerate into global training. Thus, we propose PanoLOG, a two-stage coarse-to-fine framework equipped with a Geometry and Gradient-based Partitioning Strategy tailored for large-scale panoramic 3DGS reconstruction. In the global coarse stage, PanoLOG leverages sky-sphere modeling and panoramic monocular depth supervision for reliable geometry, while in the refinement stage, G$^2$PS builds adaptive bounding volumes via parallax-driven uncertainty and assigns cameras via gradient-based importance scoring. Furthermore, we construct Pano360, the first benchmark on large-scale panoramic dataset for outdoor scene reconstruction. Extensive experiments demonstrate that G$^2$PS achieves state-of-the-art rendering quality while maintaining scalable, block-parallel training. Our models, training code, and dataset are publicly available.

</details>

#### 2026-07-09 - LTM: Large-scale Terrain Model for Wildfire-prone Landscapes

**Authors:** Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan
**Links:** [abs](https://arxiv.org/abs/2607.08711) - [pdf](https://arxiv.org/pdf/2607.08711)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, feature matching

<details>
<summary>Abstract</summary>

Accurate 3D terrain maps are essential for emergency response when assessing wildfire hazards. However, wildfire-prone regions often span vast areas where conventional reconstruction methods underperform. Airborne LiDAR systems provide high-resolution terrain data, but they are expensive and infrequently updated. Image-based methods offer a lower-cost alternative, but struggle due to sparse visual features and limited image overlap. We propose a multi-modal reconstruction framework leveraging outdated Digital Elevation Models (DEMs) as geometric priors for image-based 3D reconstruction. Our key innovation is physics-based pixel-pixel alignment between images and DEM data, dramatically reducing computational complexity by eliminating expensive feature matching procedures. To validate our approach, we developed a large-terrain simulator based on a real wildfire-prone area, generating realistic images enabling a comprehensive evaluation. Given posed images and legacy DEMs, our method produces high-fidelity depth maps while maintaining real-time performance. We find significant improvements in reconstruction accuracy and computational efficiency over existing techniques, offering a scalable solution for wildfire response.

</details>

#### 2026-07-09 - HoloTetSphere: Unified TetSphere Mesh Reconstruction for Physical Simulations

**Authors:** YaQiao Dai, Renjiao Yi, Zhirui Gao, Wei Chen, Kai Xu, Chenyang Zhu
**Links:** [abs](https://arxiv.org/abs/2607.08398) - [pdf](https://arxiv.org/pdf/2607.08398)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mesh reconstruction, rendering, splatting, simulation

<details>
<summary>Abstract</summary>

Standard pipelines for physics-ready 3D reconstruction rely on a decoupled two-stage paradigm: extracting surface geometry followed by an error-prone tetrahedralization process. While recent Lagrangian methods like TetSphere Splatting attempt to bypass this by directly optimizing volumetric primitives, their homeomorphic constraints prevent topology-adaptive optimization. Consequently, they produce disjoint tetrahedra rather than a single connected mesh, rendering the structures unsuitable for further physical simulations. To address this, we propose a topology-adaptive framework for holistic tetrahedral mesh reconstruction through end-to-end topological and geometric optimization. First, by coupling Gaussian spheres to tetrahedral elements and leveraging edge connections, we estimate a continuous opacity field for differentiable element pruning. Next, jointly minimizing mesh smoothing energy and multi-view Gaussian rendering error drives alternating geometric refinement while preserving topological adaptivity. Consequently, our approach effectively constructs a unified and topologically coherent tetrahedral mesh. Extensive experiments demonstrate that our method outperforms state-of-the-art techniques by achieving superior geometric accuracy and producing coherent, single-connected tetrahedral meshes, thereby effectively bypassing the error-prone conventional tetrahedralization step for reconstructed surface meshes and streamlining downstream physical simulation.

</details>

#### 2026-07-08 - 3D Reconstruction of deciduous Trees using low-cost UAV- and Crane-based Photogrammetry for Monitoring Shoot Elongation across entire Canopies

**Authors:** Stephan Nebiker, Micha Tschanz, Nando Amport, Frederik Baumgarten
**Links:** [abs](https://arxiv.org/abs/2607.07905) - [pdf](https://arxiv.org/pdf/2607.07905)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, photogrammetry

<details>
<summary>Abstract</summary>

Tree growth determines how much CO2 is sequestered from the atmosphere and temporarily stored in woody biomass. At the same time tree growth is affected by increasing temperatures, more frequent drought periods, late frosts and other extreme events associated with climate change. While continuous measurements of radial (secondary) tree growth using dendrometers are well established, monitoring of shoot elongation (primary growth) has largely been neglected because suitable measurement techniques are lacking. As a result, the effects of climate change on primary tree growth remain insufficiently understood. This work aims at reconstructing native deciduous trees in 3D as a basis for measuring and monitoring shoot elongation over entire tree canopies. Here we explored the use of low-cost UAV photogrammetry and of a multi-camera CraneCam system under real-world conditions. Data were collected in two study areas over an entire growing season. We present sensor evaluations, photogrammetric data acquisition and processing strategies. A special focus is placed on the analysis of the resulting photogrammetric 3D point clouds in terms of accuracy, resolution and completeness. Results demonstrate 3D point accuracies of 5-6 mm for entire trees using consumer-grade UAVs weighing less than 250 g and a 3D reconstruction completeness between 92% and 98% depending on the UAV type. The paper introduces a novel 3Dprinted ground-truth branch to evaluate the capability to reconstructing fine-detail structures such as thin tree shoots. Finally, we discuss operational challenges and initial experiments towards a skeletonization of entire trees based on photogrammetric point clouds.

</details>

#### 2026-07-08 - Monocular Vision Based Control Framework for Grasping

**Authors:** Shail Jadav, Dongheui Lee
**Links:** [abs](https://arxiv.org/abs/2607.07897) - [pdf](https://arxiv.org/pdf/2607.07897)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, manipulation

<details>
<summary>Abstract</summary>

Grasping in unstructured environments requires handling objects with widely different mechanical properties, from soft and deformable items to rigid everyday objects. Most existing approaches address these categories separately and often rely on tactile sensing, object-specific models, or specialized grippers. In this paper, we present a unified monocular vision-based grasping framework that targets both soft and rigid objects within a single control pipeline, using only RGB input and a position-controlled gripper. The proposed system combines open-vocabulary object detection, image segmentation, boundary-aware point assignment, real-time point tracking, and monocular depth estimation to recover object motion and geometry from visual observations. A key component of the framework is a language-based stiffness estimation model that infers an object's expected compliance from its semantic description and provides an object-level prior for selecting the grasping strategy before contact. For deformable objects, grasp adaptation is governed by a Procrustes-based dissimilarity measure computed from tracked keypoints, which acts as a visual proxy for deformation. For rigid objects, the gripper width is regulated through the scaling of tracked point distances. We validate the proposed method in real-world pick-and-place experiments on a Franka Emika Research 3 arm using objects with substantially different mechanical properties, including lettuce, fresh mozzarella cheese, croissants, paper towels, and hard plastic bottles. Results demonstrate that the framework achieves stable grasping across both soft and rigid objects using visual feedback alone, highlighting a practical, sensor-efficient, and generalizable approach for food handling and household manipulation.

</details>

#### 2026-07-08 - Time-to-Collision Based Dynamic Obstacle Avoidance Using Pretrained Vision Models for Robots in Unstructured Environments

**Authors:** Erik Jagnandan, Mulugeta Haile, Gregory Barber, Pratik Chaudhari
**Links:** [abs](https://arxiv.org/abs/2607.07885) - [pdf](https://arxiv.org/pdf/2607.07885)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** bundle adjustment, depth estimation, monocular depth, simulation

<details>
<summary>Abstract</summary>

Dynamic obstacle avoidance in unstructured outdoor environments remains a critical challenge for autonomous mobile robots, particularly when large-scale robot-specific training data and simulation-based policies are impractical. We present a data-efficient, interpretable method for vision-based dynamic obstacle avoidance that operates entirely on real-world data, avoiding the sim-to-real transfer problem inherent in simulation-trained policies. Our approach leverages UniDepth, a large pretrained monocular depth estimation model, to produce dense depth maps from RGB video without requiring stereo cameras or LiDAR at inference time. Dynamic obstacle avoidance is achieved by extending the SuperPoint and SuperGlue feature correspondence pipeline to track keypoints across long frame sequences, projecting their 2D pixel-space positions into 3D using camera intrinsics and predicted depth, running bundle adjustment initialized from these 3D keypoints, and computing per-keypoint time-to-collision (TTC). A 2D motion primitive in the ground plane is then selected to move the robot away from the closest point of approach of the minimum-TTC keypoint. Evaluated on real-world data from the M3ED dataset, our pipeline achieves a precision of 0.49 and a recall of 0.38 in identifying frames with a ground truth TTC below 1 second, and correctly generates the evasive motion direction in 84\% of true positive detections. Crucially, it detects at least one frame with TTC less than 1 second for 20 out of 22 unique physical obstacles present in our test sequences. Unlike end-to-end learned methods that demand thousands of hours of robot-specific training data, our approach eliminates model training entirely, requiring only 74 seconds of data for hyperparameter tuning. This demonstrates exceptional data efficiency while preserving interpretable and generalizable behavior across diverse obstacle types.

</details>

#### 2026-07-08 - GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

**Authors:** Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang
**Links:** [abs](https://arxiv.org/abs/2607.07452) - [pdf](https://arxiv.org/pdf/2607.07452)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, SLAM, visual SLAM, geometric reconstruction, Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, robotics, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM
- 作者：Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang
- 出版日期：2026-07-08T14:22:05Z
- 分类：3D Reconstruction & Multi-view Geometry (主要), Neural Scene Representations & Rendering (次要)
- 链接：https://arxiv.org/abs/2607.07452

### 一句话总结
本文提出了一种仅利用高斯分布的空间参数进行纯几何重建的SLAM方法GeoGS-SLAM，通过简化表征和配套的优化框架，在在线建图效率和几何重建质量上优于现有方法。

### 研究问题
现有基于3D高斯泼溅的密集SLAM框架同时关注外观和几何建模，但SLAM下游任务（如导航、避障）更依赖于精确的几何信息而非逼真渲染。因此，研究问题为：**是否可能仅通过3D高斯泼溅进行场景几何重建，而不进行外观建模？**

### 核心思路/方法
1. **纯几何高斯泼溅（GeoGS）**：仅保留高斯原语的空间参数（如位置、协方差等），完全舍弃颜色等外观参数，将每个原语的参数数量降低超过80%。
2. **训练框架**：通过单视图和多视图的几何与光度监督来优化高斯原语，并利用**局部平面驱动初始化**使原语更好地对齐局部结构，加速几何收敛。
3. **地图更新策略**：针对回环检测，提出一种全局变换高斯地图的策略，使其与校正后的位姿估计对齐，避免因视角不一致的位姿校正导致的地图撕裂。

### 主要贡献
1. 提出纯几何高斯泼溅表征（GeoGS），显著减少原语参数数量并提高几何收敛速度。
2. 构建基于该表征的密集单目SLAM系统GeoGS-SLAM，并设计有效的单/多视图几何-光度监督训练框架。
3. 提出一种回环地图更新策略，解决现有方法中的地图撕裂问题。
4. 在合成和真实世界基准上，证明该方法在在线建图效率和几何重建质量方面均优于当前最先进方法。

### 局限性
摘要未提供足够信息。文中未提及该方法的潜在局限性，例如对动态场景的鲁棒性、计算资源需求或在大规模场景下的扩展性。

### 阅读优先级
**高**。
理由：该工作针对SLAM领域核心的几何建图需求，提出了一种简化但高效的高斯泼溅变体，实验表明在效率和精度上均有提升。对于从事密集SLAM或3D高斯泼溅应用的研究者有较强参考价值，且方法创新点清晰。

</details>

<details>
<summary>Abstract</summary>

Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoidance, rely primarily on accurate spatial geometry rather than photorealistic rendering. This observation raises a natural question: Is it feasible for 3DGS to perform 3D reconstruction without scene appearance modeling? Motivated by this, we propose Geometry-only Gaussian Splatting (GeoGS), which directly reconstructs scene geometry, and further present GeoGS-SLAM, a dense visual SLAM system built upon this representation. Specifically, GeoGS retains only spatial parameters to reduce the number of per-primitive parameters by over 80%. In contrast to existing 3DGS methods, GeoGS focuses solely on geometric reconstruction, which significantly reduces the number of Gaussian primitives, accelerates geometric convergence, and enhances robustness to illumination variations. In addition, we present an effective training framework that optimizes the Gaussian primitives via single-view and multi-view geometric and photometric supervision, and speeds up geometry convergence with a local-plane driven initialization that better aligns primitives with local structures. Furthermore, we introduce a map update strategy for loop closure that globally transforms the Gaussian map to align it with the corrected pose estimates, thereby preventing map tearing caused by inconsistent per-viewpoint pose corrections in existing methods. Extensive experiments on synthetic and real-world benchmarks demonstrate that our method outperforms SOTA methods in terms of online mapping efficiency and geometric reconstruction quality.

</details>

#### 2026-07-08 - PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments

**Authors:** Seunghun Lee, Jihun Nam, Dong-Uk Seo, Hyun Myung
**Links:** [abs](https://arxiv.org/abs/2607.07374) - [pdf](https://arxiv.org/pdf/2607.07374)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments
- 作者：Seunghun Lee, Jihun Nam, Dong-Uk Seo, Hyun Myung
- 出版日期：2026-07-08T13:06:13Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.07374

### 一句话总结
本文提出一种基于事件相机的单目视觉惯性SLAM系统PLED-VINS，通过融合点、线特征的时间与几何可靠性估计，在动态环境中实现鲁棒的状态估计。

### 研究问题
动态环境（如移动物体和快速运动）导致视觉SLAM中的观测不可靠，传统基于事件相机的SLAM框架仍假设静态场景，缺乏对特征可靠性的评估方法。

### 核心思路/方法
1. 提出“熵-新近度得分图”基于事件时间统计量表征点、线特征的时间可靠性。
2. 通过统一点-线鲁棒捆绑调整估计特征的几何可靠性。
3. 设计自适应加权策略融合时间与几何可靠性，包括针对线特征的运动条件可靠性建模，以抑制不可靠观测。

### 主要贡献
- 首次提出结合时间与几何可靠性的点-线事件视觉惯性SLAM框架，专门面向动态环境。
- 提出基于事件时间统计的熵-新近度得分图与统一点-线鲁棒捆绑调整，分别刻画特征的时间与几何可靠性。
- 实验表明在包含移动物体的动态序列上提升了状态估计精度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。该工作聚焦于动态场景下事件相机的SLAM方法，对研究鲁棒视觉里程计或事件相机应用的人有参考价值，但若需完整实验细节或与其他方法对比，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Dynamic environments remain a fundamental challenge for visual SLAM, where unreliable observations from moving objects and rapid motion degrade state estimation accuracy. Although event cameras preserve fine-grained spatio-temporal information, most existing event-based SLAM frameworks still assume static scenes and lack approaches to estimate the reliability of features. To this end, we propose PLED-VINS, a monocular event camera-based visual-inertial SLAM framework that enables robust state estimation in dynamic environments. We propose an entropy-recency score map to characterize the temporal reliability of both point and line features based on event temporal statistics. Concurrently, geometric reliability is estimated via a unified point-line robust bundle adjustment. Building upon these, we design an adaptive weighting strategy that fuses temporal and geometric reliability, including motion-conditioned reliability modeling for line features, to suppress unreliable observations. Experimental results demonstrate that PLED-VINS improves state estimation on the evaluated dynamic sequences with moving objects.

</details>

#### 2026-07-08 - Disturbance-aware Motion Planning for Over-actuated Underwater Vehicles Exploiting Actuation Redundancy for High-fidelity 3D Reconstruction

**Authors:** Yuer Gao, Tongqing Xu, Qingyang Liu, Yi Cai
**Links:** [abs](https://arxiv.org/abs/2607.07139) - [pdf](https://arxiv.org/pdf/2607.07139)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Disturbance-aware Motion Planning for Over-actuated Underwater Vehicles Exploiting Actuation Redundancy for High-fidelity 3D Reconstruction
- 作者：Yuer Gao, Tongqing Xu, Qingyang Liu, Yi Cai
- 出版日期：2026-07-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.07139

### 一句话总结
本文提出一种利用过驱动水下机器人的冗余推进能力，通过优化推进器分配以最小化目标区域扰动，从而提升水下三维重建质量的方法。

### 研究问题
传统水下机器人控制器仅优化自身运动（如跟踪、稳定性），忽略推进器产生的扰动（如沉积物再悬浮、湍流）对感知任务（如三维重建图像质量）的负面影响。本文旨在解决这种“执行-感知”耦合问题。

### 核心思路/方法
1. **利用冗余空闲空间**：对于配备八个推进器的ROV，多种推进力分配方案可产生相同运动；通过在零空间中搜索，在满足运动约束的前提下，最小化任务相关目标区域的预测扰动。
2. **扰动建模**：基于执行器盘理论并引入方向衰减，建立控制导向的推进器尾流代理模型，使用PIV（粒子图像测速）验证（近轴区域 \(R^2=0.99\)，主尾流区域 \(R^2>0.82\)）。
3. **实时分配器**：实现一个10Hz（每45毫秒求解一次）的实时冗余解析分配器，在线求解最优分配。

### 主要贡献
1. 提出一种扰动感知的过驱动水下机器人运动规划方法，利用执行器冗余来解耦执行与感知的冲突。
2. 提出一个计算高效的尾流代理模型（基于执行器盘理论），可实时预测扰动。
3. 实验验证：在440次试验中，目标区域粒子速度降低67%（\(p<0.001\)），三维重建RMSE从 \(4.3 \pm 1.8\) mm（未考虑扰动基线）降至 \(1.9 \pm 0.4\) mm（降低55%），重建成功率98.5%。支持自动扫描与操作员辅助两种模式。

### 局限性
- 摘要未提供关于方法在非过驱动或尾流模型失效场景（如高海流、复杂地形）下的推广性讨论。
- 摘要未提供关于实时分配器在不同计算硬件上的性能边界分析。
- 摘要未提供关于尾流模型在远场或与多种传感器（如声纳）耦合时的精度验证信息。

### 阅读优先级
**高**  
理由：该方法直接解决了水下机器人实际应用中的关键瓶颈（推进扰动导致成像退化），实验数据详实（含统计显著性检验、大样本试验），并实现了实时能力（10Hz），对水下三维重建和机器人运动规划领域具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Underwater robots often operate near delicate targets where high-power thrusters resuspend sediments and induce turbulence, degrading image quality at the sensor input. Conventional controllers optimize vehicle-centric objectives, such as tracking and stability, without accounting for the impact of actuation on sensing. We address this actuation-to-perception coupling by exploiting redundancy in over-actuated platforms. For an eight-thruster ROV, multiple thrust allocations can yield the same motion; we search this null space to minimize predicted disturbance in a task-relevant target region while enforcing motion constraints. Our method uses a control-oriented thruster-wake proxy derived from actuator-disk theory with directional attenuation and validated by PIV ($R^2 = 0.99$ near the wake axis; $R^2 > 0.82$ in the primary wake region), together with a real-time redundancy-resolving allocator running at 10 Hz (45 ms/solve). Across 440 trials, the approach reduces target-region particle velocity by 67% ($p < 0.001$), improves 3D reconstruction RMSE by 55% versus a disturbance-unaware baseline ($1.9 \pm 0.4$ mm vs. $4.3 \pm 1.8$ mm), and achieves a 98.5% reconstruction success rate. The framework supports autonomous scanning, which is quantitatively evaluated, and operator-assisted inspection, which is demonstrated in the supplementary materials.

</details>

#### 2026-07-07 - Gen4U: Unifying Video Generation and Understanding via Diffusion

**Authors:** Michael King, Aravindh Mahendran, Matthew Koichi Grimes, Fedor Kitashov, Adham Elarabawy, Pedro Velez, Maks Ovsjanikov, Viorica Pătrăucean
**Links:** [abs](https://arxiv.org/abs/2607.06856) - [pdf](https://arxiv.org/pdf/2607.06856)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gen4U: Unifying Video Generation and Understanding via Diffusion
- 作者：Michael King, Aravindh Mahendran, Matthew Koichi Grimes, Fedor Kitashov, Adham Elarabawy, Pedro Velez, Maks Ovsjanikov, Viorica Pătrăucean
- 出版日期：2026-07-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.06856

### 一句话总结
本文提出Gen4U框架，利用无需微调的冻结视频扩散模型的中间表征，同时实现高水平的视频生成与多种理解任务。

### 研究问题
如何利用视频扩散模型的中间表征来统一视频生成和理解，并验证其在低层几何与高层语义任务上的能力。

### 核心思路/方法
1. 通过系统性探针实验（使用互k近邻对齐指标）分析先进视频扩散模型的中间激活，发现隐空间具有高度结构化特征：中等噪声水平对应线性可分的全局语义，低噪声水平保留细粒度细节但空间分散，需注意力机制解码。
2. 基于这些观察，提出Gen4U框架，以单次前向传播方式复用生成表征，无需微调。
3. 实验证明冻结的大规模视频扩散模型可充当强视频编码器，适用于视频分类、深度估计、相机位姿估计、图像及视频描述等任务。

### 主要贡献
1. 揭示视频扩散模型中间表征的结构化特性及其与噪声水平的关联。
2. 提出Gen4U框架，实现生成与理解的统一，无需微调即可在语义和非语义任务上达到强感知性能。
3. 保留模型生成高质量视频的原始能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法在统一生成与理解上具有创新性，且实验覆盖任务广泛；但缺乏具体性能指标和对比细节，实用性验证需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Prior work suggests that diffusion representations capture low-level geometry but struggle with high-level semantics. We demonstrate that state-of-the-art video diffusion models overcome this limitation. By systematically probing their intermediate activations using recent mutual-kNN alignment metrics, we reveal a highly structured latent space where visual representations evolve across both network depth and noise levels. We show that while moderate noise levels yield linearly separable global semantics, fine-grained details persist at lower noise levels but become spatially scattered, requiring attention mechanisms to decode. Building on these insights, we introduce Gen4U (Generation for Understanding), a framework that repurposes these generative representations with a single forward pass. Our experiments establish that frozen, large-scale video diffusion models function as highly competitive video encoders across a wide spectrum of tasks, spanning semantic and non-semantic objectives (video classification, depth estimation, camera pose estimation, image and video captioning). Bypassing fine-tuning, Gen4U unifies the generation and understanding paradigms, achieving strong perception performance while fully preserving the model's ability to generate high-quality video.

</details>

#### 2026-07-07 - CILC: Cryptographically-secure Inter-agent Loop Closure Candidate Detection for Multi-Agent Collaborative SLAM

**Authors:** Andrew Fishberg, Yixuan Jia, Jonathan P. How
**Links:** [abs](https://arxiv.org/abs/2607.06700) - [pdf](https://arxiv.org/pdf/2607.06700)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CILC: Cryptographically-secure Inter-agent Loop Closure Candidate Detection for Multi-Agent Collaborative SLAM
- 作者：Andrew Fishberg, Yixuan Jia, Jonathan P. How
- 出版日期：2026-07-07T18:20:09Z
- 分类：3D Reconstruction & Multi-view Geometry (主要)；Embodied / Robotics / AR Applications (次要)
- 链接：摘要页 https://arxiv.org/abs/2607.06700；PDF https://arxiv.org/pdf/2607.06700

### 一句话总结
本文提出CILC，首个利用安全多方计算（SMPC）实现多机器人协同SLAM中无需明文交换全局描述符的隐私保护闭环候选检测方法。

### 研究问题
多机器人协同SLAM（CSLAM）中，即使使用加密无线电通信，被攻破的内部机器人仍可通过监听公开的全局描述符（GDs）重建其他诚实机器人的图像和轨迹信息，如何在不泄露隐私的前提下安全检测闭环候选？

### 核心思路/方法
- 不保护整个CSLAM流水线，仅将SMPC应用于“闭环候选检测”这一隐私敏感且计算轻量的环节，即对全局描述符（视觉和LiDAR模态）的相似度比较进行加密计算。
- 通过SMPC技术，使机器人能在不公开原始GD的情况下计算彼此描述符的相似度，从而检测闭环候选，同时将信息泄漏最小化。

### 主要贡献
- 揭示现有CSLAM系统中GD广播的隐私漏洞——被攻破的个体可重构诚实个体图像和轨迹。
- 提出CILC，首个将SMPC用于多机器人闭环候选检测的方案，在不暴露明文GD的情况下实现安全比较。
- 在仿真和硬件实验中验证CILC在多模态GD（视觉和LiDAR）下仍能保持实时性和通信可行性，并有效缓解信息泄漏。

### 局限性
摘要未提供足够信息，未明确讨论计算开销的具体数值、对闭环检测召回率的影响、SMPC引入的延迟是否会限制大规模多机器人系统，以及攻击模型的边界假设。

### 阅读优先级
**高**。理由：针对多机器人协同SLAM中实际存在的内部隐私威胁（而非传统外部窃听），提出首个基于SMPC的解决方案，同时兼顾隐私-开销权衡，且通过了实物验证，对隐私敏感型协作机器人系统具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Multi-agent Simultaneous Localization and Mapping (SLAM) and collaborative SLAM (CSLAM) require robots to continuously exchange global descriptors (GDs) to detect inter-agent loop closures (ILCs). While encrypted radios protect this traffic from external eavesdroppers, they offer no protection against a compromised swarm member. We show this threat is concrete by demonstrating how a corrupted agent can reconstruct approximations of an honest agent's imagery and trajectory from its public GD broadcasts. To address this, we propose CILC (Cryptographically-secure Inter-agent Loop Closure candidate detection), a first-of-its-kind system leveraging Secure Multi-Party Computation (SMPC) to detect ILC candidates without exchanging GDs in the clear. Rather than securing the entire CSLAM pipeline, we apply SMPC only to ILC candidate detection (i.e., GD similarity comparison), a privacy-sensitive yet computationally lightweight step, yielding an advantageous privacy-to-overhead trade-off. We validate in both simulation and hardware experiments that CILC remains real-time and communication-feasible across multimodal GDs (visual and LiDAR), while mitigating information leakage to a compromised swarm agent.

</details>

#### 2026-07-07 - Vision as Unified Multimodal Generation

**Authors:** Xiaoyang Han, Jianhua Li, Kewang Deng, Zukai Chen, Xuanke Shi, Sihan Wang, Boxuan Li, Linyan Wang, Siyi Xie, Xin You, Jinsheng Quan, Zhongang Cai, Haiwen Diao, Ziwei Liu, Lei Yang, Dahua Lin, Quan Wang
**Links:** [abs](https://arxiv.org/abs/2607.06560) - [pdf](https://arxiv.org/pdf/2607.06560)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Vision as Unified Multimodal Generation
- 作者：Xiaoyang Han, Jianhua Li, Kewang Deng, Zukai Chen, Xuanke Shi, Sihan Wang, Boxuan Li, Linyan Wang, Siyi Xie, Xin You, Jinsheng Quan, Zhongang Cai, Haiwen Diao, Ziwei Liu, Lei Yang, Dahua Lin, Quan Wang
- 出版日期：2026-07-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.06560

### 一句话总结
本文提出将计算机视觉任务统一表述为多模态生成问题，通过一个无需任务特定架构的统一模型（SenseNova-Vision）在文本和图像生成空间中完成检测、分割、深度估计等多种视觉任务。

### 研究问题
如何将异构的计算机视觉任务（如检测、分割、深度估计等）整合到一个统一的多模态生成框架中，避免为每个任务设计专门的模型架构或预测头。

### 核心思路/方法
1. **重新定义任务形式**：将不同的视觉任务统一表示为“文本+可选的视觉提示”作为输入，输出可以是纯文本（符号输出）、纯图像（稠密空间预测）或文本与图像的混合（组合任务），从而在统一的文本和图像生成空间中表达。
2. **构建专用语料库**：将多样化的计算机视觉标注转换为符合上述生成空间的指令-响应示例，形成名为“SenseNova-Vision Corpus”的大规模语料库。
3. **模型训练**：基于现成的多模态预训练模型，主要在此语料库上训练（辅以少量多模态数据以保持模型能力），不添加任务特定的预测头或修改模型架构。

### 主要贡献
- 提出“视觉即统一多模态生成”的新公式，将多种视觉任务（检测、OCR、关键点估计、分割、深度估计、表面法线预测、点图、相机位姿估计）整合到单一模型中。
- 构建并公开了 SenseNova-Vision Corpus，这是一个覆盖文本、图像和混合目标的视觉指令-响应语料库。
- 实验表明，单个统一模型能够在结构化视觉理解、稠密几何预测、分割和多视角视觉几何等任务上与专有任务模型性能持平。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作提出了一种统一的视觉任务框架，能够在不修改模型架构的情况下处理多种竞争性任务，且实验表明性能与专用模型相当。对于关注通用基础模型与计算机视觉集成、多模态生成范式的研究者具有重要参考价值。论文和语料库均已公开，便于复现与深入探索。

</details>

<details>
<summary>Abstract</summary>

We formulate computer vision as unified multimodal generation, where heterogeneous visual tasks are expressed in the native text and image generation spaces of a unified multimodal model, without task-specific architectures. Under this formulation, SenseNova-Vision uses natural-language instructions and optional visual prompts to specify tasks, target regions or views, and decoding conventions, and generates responses as text for symbolic outputs, images for dense spatial predictions, or mixed text-and-image outputs for compositional tasks. To support large-scale training, we convert diverse computer vision annotations into instruction-response examples compatible with these generation spaces, resulting in the SenseNova-Vision Corpus, a computer-vision instruction-response corpus spanning text, image, and mixed targets. Starting from an off-the-shelf pretrained unified multimodal model, SenseNova-Vision is trained primarily on this corpus, with auxiliary multimodal data used as a capability-preserving mixture, and requires no task-specific prediction heads or architectural modifications. The resulting model covers a broad range of vision tasks, including detection, OCR, keypoint estimation, segmentation, depth estimation, surface normal prediction, point maps, and camera pose estimation, while supporting language-defined variants that combine category, color, region, and other visual cues. Experiments show that a single unified model can match leading task-specialized systems across structured visual understanding, dense geometric prediction, segmentation, and multi-view visual geometry. These results suggest unified multimodal generation as a scalable route for integrating computer vision capabilities into general-purpose foundation models. The model and corpus are publicly available.

</details>

#### 2026-07-07 - ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation

**Authors:** Ruihang Zhang, Felix Taubner, Pooja Ravi, Kiriakos N. Kutulakos, David B. Lindell
**Links:** [abs](https://arxiv.org/abs/2607.06555) - [pdf](https://arxiv.org/pdf/2607.06555)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation
- 作者：Ruihang Zhang, Felix Taubner, Pooja Ravi, Kiriakos N. Kutulakos, David B. Lindell
- 出版日期：2026-07-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要链接](https://arxiv.org/abs/2607.06555) | [PDF链接](https://arxiv.org/pdf/2607.06555)

### 一句话总结
ProxyPose 将单目视频中的 6-DoF 姿态跟踪问题转化为视频到视频的翻译任务，通过微调的视频扩散模型生成合成“代理视频”，进而使用经典方法恢复姿态，无需 3D 模型、深度图等额外输入。

### 研究问题
如何仅从单目视频中跟踪物体或表面的六自由度（6-DoF）姿态，且无需 3D 模型、深度图、对象掩码或任务特定特征等额外输入，尤其针对无纹理、透明、反射或可变形表面等困难材质。

### 核心思路/方法
- 将姿态跟踪重新定义为视频到视频的翻译问题。
- 输入仅为一个视频和第一帧中的一个标记像素。
- 使用微调的视频扩散模型，将输入视频翻译为一个“代理视频”：即一个彩色多面体（polyhedron）的合成视频，该多面体与被标记像素处的表面区域经历相同的局部刚体运动。
- 由于代理视频的几何和外观是已知的，因此恢复其完整的 6-DoF 轨迹可简化为使用现成求解器进行经典姿态估计。
- 该方法利用大规模视频预训练，将姿态跟踪中处理困难材质、遮挡和形变的复杂部分吸收到翻译步骤中，而在像素级别工作，无需假设物体身份、边界或全局刚性。

### 主要贡献
1. 提出 ProxyPose，一种新颖的 6-DoF 姿态跟踪范式，将问题简化为视频到视频的翻译。
2. 在仅使用合成数据微调视频模型后，实现了最先进的 6-DoF 姿态跟踪精度，且无需竞争方法所需的额外输入。
3. 展示了该方法可扩展至面部跟踪、相机姿态估计以及现有方法无法处理的挑战性野外场景。

### 局限性
摘要未提供足够信息。论文未在摘要中讨论方法在特定场景下的失败案例、计算成本、对标记像素质量的依赖性或实时性等局限性。

### 阅读优先级
**高**。理由：该论文提出了一种创新的姿态跟踪范式，从根本上改变了传统方法对额外输入的依赖，并在困难材质（无纹理、透明、反射等）上展示了优势。对于从事 3D 视觉、姿态估计或视频理解的研究者来说，这一全新思路具有较高的参考价值和启发性。

</details>

<details>
<summary>Abstract</summary>

Tracking the six-degree-of-freedom (6-DoF) pose of objects and surfaces from monocular video is a long-standing problem in computer vision. To tackle this problem, existing methods require inputs beyond the video itself-such as 3D models, depth maps, object masks, or task-specific learned features-and they struggle with textureless, transparent, reflective, or deformable surfaces. Here, we introduce ProxyPose, which recasts 6-DoF pose tracking as video-to-video translation. Given only a video and a single marked pixel in the first frame, a fine-tuned video diffusion model translates the input into a proxy video-a synthetic video depicting a colored polyhedron undergoing the same local rigid-body motion as the surface region at the marked pixel. Because the proxy's geometry and appearance are known by construction, recovering its full 6-DoF trajectory reduces to classical pose estimation with off-the-shelf solvers. This formulation leverages large-scale video pre-training to absorb the hardest aspects of pose tracking-handling challenging materials, occlusions, and deformations-into the translation step, while operating at the pixel level with no assumptions about object identity, boundaries, or global rigidity. ProxyPose achieves state-of-the-art 6-DoF pose tracking accuracy without the additional inputs required by competing methods and after fine-tuning the video model only on synthetic data. We further demonstrate that ProxyPose extends to face tracking, camera pose estimation, and challenging in-the-wild scenes that are beyond the reach of existing approaches. Project page: https://ruihangzhang97.github.io/proxypose/.

</details>

#### 2026-07-07 - Hilti-Trimble-Oxford Dataset: 360 Visual-Inertial Benchmark with Floor Plan Priors for SLAM and Localization

**Authors:** Samuele Centanni, Yuhao Zhang, Yifu Tao, Julien Kindle, Frank Neuhaus, Tilman Koß, Aryaman Patel, Michael Helmberger, Emilia Szymańska, Torben Gräber, Maurice Fallon
**Links:** [abs](https://arxiv.org/abs/2607.06464) - [pdf](https://arxiv.org/pdf/2607.06464)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, visual SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hilti-Trimble-Oxford Dataset: 360 Visual-Inertial Benchmark with Floor Plan Priors for SLAM and Localization
- 作者：Samuele Centanni, Yuhao Zhang, Yifu Tao, Julien Kindle, Frank Neuhaus, Tilman Koß, Aryaman Patel, Michael Helmberger, Emilia Szymańska, Torben Gräber, Maurice Fallon
- 出版日期：2026-07-07
- 分类：3D Reconstruction & Multi-view Geometry (主), Embodied / Robotics / AR Applications (次)
- 链接：https://arxiv.org/abs/2607.06464

### 一句话总结
本文介绍了一个在真实建筑工地采集的360度视觉-惯性数据集，旨在为SLAM和基于楼层平面图先验的定位提供基准，并报告了相关公开挑战赛的结果。

### 研究问题
如何利用低成本360度相机和惯性测量单元（IMU），在复杂多变的建筑工地环境中实现高精度的视觉SLAM和基于楼层平面图的定位，以支持自动化施工进度监测。

### 核心思路/方法
作者在一个正在施工的建筑工地中，历时八个月、跨越七个楼层，采集了30个视觉-惯性序列。数据集使用高精度LiDAR-惯性SLAM系统提供真值轨迹，并组织了一场开放研究挑战赛，邀请全球团队在SLAM和基于楼层平面图的定位两个任务上评估其系统性能。

### 主要贡献
1. 提供了真实建筑工地环境下的高质量视觉-惯性数据集，包含光照变化、工人移动、快速运动和重复结构等现实挑战。
2. 构建了基于楼层平面图先验的定位基准，并作为公开挑战赛的评测平台。
3. 通过挑战赛结果分析了SLAM和定位任务的现状：SLAM参与度更高（62个团队）且相对成熟，而定位任务误差更大、更具挑战性（22个团队），说明该领域仍需进一步研究。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文贡献了低成本视觉定位在复杂真实场景（建筑工地）中的稀缺数据集和公开基准，对从事SLAM、视觉-惯性导航和建筑自动化研究的学者具有直接参考价值。挑战赛结果揭示了SLAM与定位任务的成熟度差异，有助于明确后续研究方向。

</details>

<details>
<summary>Abstract</summary>

Automated progress monitoring on construction sites is an active area of research and development. Robot and human-carried mapping systems have been developed to build 3D maps of building and infrastructure projects. While LiDAR-based mapping systems achieve high accuracy, the cost of LiDAR can be prohibitive. Consumer-grade cameras with wide field of view ("360 cameras") combined with embedded inertial measurement units (IMUs) provide a cost-effective alternative. To support change detection and progress monitoring, highly accurate visual Simultaneous Localization and Mapping (SLAM) and floor plan-referenced localization systems are required. In this paper we present a high-quality dataset collected at an active construction site, which captures realistic challenges such as variable lighting conditions, moving workers, fast motions, and repetitive structures. The dataset offers thirty visual-inertial sequences recorded across seven floors over an eight-month period of the construction project. Ground truth trajectories were collected using a high quality LiDAR-inertial SLAM system rigidly attached to the 360 camera. Additionally, we report the results of an open research challenge evaluating the best visual SLAM and localization systems from around the world. The Challenge attracted substantially higher participation in SLAM, with 62 teams compared to 22 in floor-plan-referenced localization, reflecting the broader maturity of SLAM methods. The higher errors in localization further highlight the difficulty of this task in construction and point to the need for continued research, which this dataset is intended to support. The dataset and the benchmark are publicly available at: https://hilti-trimble-challenge.com/dataset-2026.

</details>

#### 2026-07-07 - Why does Deep Learning Improve Visual SLAM?

**Authors:** Giovanni Cioffi, Davide Scaramuzza
**Links:** [abs](https://arxiv.org/abs/2607.06023) - [pdf](https://arxiv.org/pdf/2607.06023)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Why does Deep Learning Improve Visual SLAM?
- 作者：Giovanni Cioffi, Davide Scaramuzza
- 出版日期：2026-07-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2607.06023) | [PDF](https://arxiv.org/pdf/2607.06023)

### 一句话总结
本文通过控制实验发现，深度学习提升视觉SLAM性能的核心原因是学习到的2D数据关联和不确定性，而非循环网络架构本身。

### 研究问题
深度学习视觉SLAM系统优于传统几何方法，但其成功究竟归因于哪个核心组件？是学习到的2D数据关联、结合不确定性的2D数据关联，还是循环网络架构？

### 核心思路/方法
采用控制变量法进行实证研究，即通过逐步消融或替换不同组件（如固定2D数据关联、移除不确定性表示、改变循环架构等），观察对视觉SLAM性能的影响，从而确定各组件的关键性。

### 主要贡献
1. 明确揭示深度学习视觉SLAM成功的关键驱动因素：学习到的2D数据关联和不确定性，而非循环网络架构。
2. 强调学习范式对于视觉SLAM中数据关联和不确定性设计的必要性。
3. 摘要未提供额外贡献信息。

### 局限性
摘要未提供足够信息，包括实验设置、数据集、对比方法、具体性能指标、以及“控制实验”的详细构造等细节。

### 阅读优先级
**高**
理由：本文直指深度学习视觉SLAM领域一个根本性的理论问题，通过实证回答“成功究竟来自哪里”而非“做得更好”，对指导未来系统设计（如是否应关注架构创新还是数据关联模块）具有重要启示。适合从事视觉SLAM、深度学习与几何结合方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combining learned 2D data association and uncertainty with differentiable geometric optimization in recurrent architectures. Still, it remains unclear exactly which components are fundamentally responsible for this success. In this paper, we ask: Is the superior performance of deep learning-based systems driven primarily by learned 2D data association, the combination of learned 2D data association and uncertainty, or the recurrent architecture itself? We investigate this question empirically by conducting a controlled study. Our findings reveal that the success of DL-based V-SLAM systems hinges on learned 2D data association and uncertainty rather than their recurrent architecture, underscoring the necessity of learning-based paradigms for the design of these components. Upon acceptance, the code will be released as open source.

</details>

#### 2026-07-07 - MiLSD: A Micro Line-Segment Detector for Resource-Constrained Devices

**Authors:** Parsa Hassani Shariat Panahi, Amir Hossein Jalilvand, M. Hassan Najafi
**Links:** [abs](https://arxiv.org/abs/2607.06600) - [pdf](https://arxiv.org/pdf/2607.06600)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, SLAM, visual SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MiLSD: A Micro Line-Segment Detector for Resource-Constrained Devices
- 作者：Parsa Hassani Shariat Panahi, Amir Hossein Jalilvand, M. Hassan Najafi
- 出版日期：2026-07-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.06600

### 一句话总结
本文提出MiLSD，一种专为资源受限设备（如低功耗MCU）设计的亚兆字节级线检测器，通过紧凑架构、8位量化和推理增强，在1 MB激活预算下将sAP10从0.25 MB的10.6提升至24.1。

### 研究问题
如何在内存预算小于1 MB（适配MCU）的条件下，最大化线检测任务的精度？

### 核心思路/方法
1. 设计紧凑的全卷积骨干网络，比较三种输出表示（其中F-Clip中心-长度-角度表示在小模型下学习效果最佳）。
2. 探索量化方案：8位量化保持全精度性能，4位量化导致严重退化（尤其角度回归），量化感知训练仅能部分恢复。
3. 在1 MB激活预算下集成推理增强：亚像素解码、测试时数据增强、轻量验证器，提升最终检测精度。

### 主要贡献
- 提出MiLSD，首个面向亚兆字节内存约束的微线段检测器。
- 系统比较了三种输出表示在小骨干网络下的有效性，明确F-Clip表示最优。
- 揭示了位宽量化对线检测精度的具体影响（8位无损，4位有显著角度误差）。
- 在1 MB激活预算下，将ShanghaiTech Wireframe数据集上的sAP10从0.25 MB的10.6提升至24.1。

### 局限性
摘要未提供信息（如：未讨论模型在真实MCU上的具体部署延迟、功耗实测、其他数据集泛化能力、量化后精度下降的详细原因分析、与更多轻量方法的对比等）。

### 阅读优先级
高
理由：该工作聚焦于嵌入式设备和MCU场景的线检测，填补了深度学习线检测模型在极端小内存约束下的空白，所涉及的量化、紧凑表示、后处理策略对低功耗计算机视觉应用有明确参考价值，且提供了清晰的精度-内存权衡图谱。

</details>

<details>
<summary>Abstract</summary>

Line segment detection is a key building block in visual SLAM, 3D reconstruction, and industrial inspection. Recent deep learning methods have greatly improved accuracy, yet even the smallest models require several megabytes of memory, exceeding low-cost MCU capacity. This work investigates the maximum achievable accuracy under a sub-megabyte budget. We propose MiLSD, a detector tailored for MCU-level constraints, and systematically compare three output representations within a compact fully-convolutional backbone. Our study shows that the proposed F-Clip center-with-length-and-angle formulation learns most effectively at small model sizes. We find that 8-bit quantization preserves full-precision performance, while 4-bit quantization causes significant degradation, particularly in angle regression, with quantization-aware training recovering only part of the loss. With a one-megabyte activation budget and inference enhancements including sub-pixel decoding, test-time augmentation, and a lightweight verifier, MiLSD improves sAP10 on ShanghaiTech Wireframe from 10.6 (25k parameters, 0.25 MB) to 24.1 within 1 MB. Rather than competing with GPU-scale parsers, we map the accuracy memory trade-off across representations, bit-widths, capacities, and post-processing strategies for embedded vision systems.

</details>

#### 2026-07-06 - ReCal3R: Reliability-Calibrated Learning Rates for Streaming 3D Reconstruction

**Authors:** Xinze Li, Yiyuan Wang, Pengxu Chen, Wentao Fan, Weifeng Su, Weisi Lin, Wentao Cheng
**Links:** [abs](https://arxiv.org/abs/2607.05356) - [pdf](https://arxiv.org/pdf/2607.05356)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReCal3R: Reliability-Calibrated Learning Rates for Streaming 3D Reconstruction
- 作者：Xinze Li, Yiyuan Wang, Pengxu Chen, Wentao Fan, Weifeng Su, Weisi Lin, Wentao Cheng
- 出版日期：2026-07-06
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.05356

### 一句话总结
ReCal3R提出一种基于可靠性校准的学习率方法，用于流式3D重建，通过为每个状态令牌动态调整更新步长，抑制对不可靠信息的过激更新，从而提升长序列重建的精度。

### 研究问题
流式3D重建中，随着图像序列持续输入，循环场景状态会因重复更新而逐渐被噪声或模糊观测污染，导致可靠的历史信息被覆盖。如何在不增复杂度的情况下防止状态退化、保持重建质量？

### 核心思路/方法
方法核心是“可靠性校准的学习率”。具体流程：
1. 从当前场景状态中估计每个状态令牌的可靠性。
2. 基于令牌对齐、状态重建残差和近期更新压力，计算一个候选学习率。
3. 将候选学习率与保守基础率进行插值，得到令牌级的学习率。对于可靠性低的令牌，插值更偏向保守基础率，抑制过激更新；对可靠性高的令牌则允许较大更新以适配新信息。
该规则被作为训练无关的校准模块应用于CUT3R模型中。

### 主要贡献
- 提出可靠性校准的学习率机制，有效抑制流式3D重建中的状态退化问题。
- 该方法是训练无关的即插即用规则，可直接应用于现有模型（如CUT3R）。
- 在长序列重建任务中，姿态、深度和重建质量显著提升，平均平移误差（ATE）降低3.7倍，且运行时间和内存开销与基线相当。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对流式3D重建中状态退化的关键问题，提出了简单有效的学习率校准方法，且性能提升显著（ATE降低3.7倍），具有实际应用价值；代码开源，便于复现和扩展。如果研究领域涉及动态3D重建、增量式SLAM或长时间序列处理，值得深入阅读。

</details>

<details>
<summary>Abstract</summary>

Streaming 3D reconstruction relies on a compact recurrent scene state to process long image streams in linear time and bounded memory. However, repeated updates can gradually corrupt this state, causing reliable historical information to be overwritten by noisy or ambiguous observations. We introduce ReCal3R, a reliability-calibrated learning rate method for recurrent 3D reconstruction. Instead of directly applying a candidate learning rate, our method estimates state token reliability from the maintained scene state and uses it to calibrate a candidate learning rate derived from token alignment, state reconstruction residual, and recent update pressure. The resulting token-wise learning rate interpolates between a conservative base rate and the candidate rate, suppressing aggressive updates on unreliable tokens while preserving adaptation to informative frames. Applied to CUT3R as a training-free calibration rule, ReCal3R reaches strong performance on long sequences in pose, depth, and reconstruction quality, including a 3.7$\times$ reduction in ATE, with comparable runtime and memory. Code is available at: https://github.com/Powertony102/ReCal3R.

</details>

#### 2026-07-06 - GUSH3R: Everyone Everywhere All at Once as Gaussians

**Authors:** Keito Abe, Kaede Shiohara, Takashi Otonari, Toshihiko Yamasaki
**Links:** [abs](https://arxiv.org/abs/2607.05243) - [pdf](https://arxiv.org/pdf/2607.05243)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GUSH3R: Everyone Everywhere All at Once as Gaussians
- 作者：Keito Abe, Kaede Shiohara, Takashi Otonari, Toshihiko Yamasaki
- 出版日期：2026-07-06
- 分类：3D Reconstruction & Multi-view Geometry（主分类），Neural Scene Representations & Rendering（次分类）
- 链接：摘要链接：https://arxiv.org/abs/2607.05243；PDF链接：https://arxiv.org/pdf/2607.05243

### 一句话总结
GUSH3R是一个前馈式框架，能从单目视频中一次性同时重建动态人体和静态场景，并将其表示为3D高斯泼溅（3DGS）基元，支持几何一致的新视角合成。

### 研究问题
从单目视频中重建动态人体-场景环境，难点在于需要联合建模场景几何、相机运动和人体柔性动力学，同时实现照片级渲染。现有前馈方法或无法处理非刚性物体（如动态人体），或仅能生成非照片级真实感表示（如点云、网格）。

### 核心思路/方法
提出前馈式框架（GUSH3R），将动态人体（everyone）和静态场景（everywhere）统一在一个前向传播中（all at once），直接输出3D高斯泼溅（3DGS）基元，实现几何一致且可支持新视角合成的表示。该方法无需逐帧优化，而是通过一次推理完成重建。

### 主要贡献
- 首次提出前馈式框架同时重建动态人体和静态场景，并以3DGS基元形式输出。
- 在单目人体-场景数据集上，新视角合成质量具有竞争力，且推理效率显著优于基于优化的方法。

### 局限性
摘要未提供足够信息：未明确说明在复杂遮挡、快速运动或大范围场景下的表现，也未提及训练数据需求或对相机运动的鲁棒性限制。

### 阅读优先级
**高**。
理由：该工作针对单目动态人体-场景重建这一难题，提出了创新的前馈式方案（取代慢速优化），并实现了有竞争力的合成质量与高效推理。方法新颖且实用性强，适合关注3D重建、动态场景理解或新视角合成方向的读者。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic human-scene environments from monocular videos is a challenging problem that requires jointly modeling scene geometry, camera motion, and non-rigid human dynamics while enabling photorealistic rendering. Recent feed-forward methods can efficiently predict geometry, but they are often limited to non-photorealistic representations such as point clouds and meshes, or they fail to handle non-rigid objects, particularly dynamic humans. To fill this gap, we present GUSH3R (Gaussian-Unified Scene Human 3D Reconstruction), a feed-forward framework for online dynamic human-scene reconstruction. From a monocular human-scene video, our method reconstructs dynamic humans (everyone) and static scenes (everywhere) in a single forward pass (all at once) as 3D Gaussian Splatting (3DGS) primitives (as gaussians), which are geometrically consistent and capable of novel view synthesis. Experiments on monocular human-scene datasets demonstrate that our approach achieves competitive novel view synthesis quality while significantly improving inference efficiency compared to optimization-based methods.

</details>

#### 2026-07-06 - MemPose: Category-level Object Pose Estimation with Memory

**Authors:** Xiao Lin, Minghao Zhu, Yun Peng, Liuyi Wang, Qiyi Wang, Chengju Liu, Qijun Chen
**Links:** [abs](https://arxiv.org/abs/2607.04930) - [pdf](https://arxiv.org/pdf/2607.04930)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MemPose: Category-level Object Pose Estimation with Memory  
- 作者：Xiao Lin, Minghao Zhu, Yun Peng, Liuyi Wang, Qiyi Wang, Chengju Liu, Qijun Chen  
- 出版日期：2026-07-06  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：摘要页 https://arxiv.org/abs/2607.04930 / PDF https://arxiv.org/pdf/2607.04930  

### 一句话总结
MemPose 提出一种基于记忆增强的类别级物体位姿估计框架，通过显式引入并动态更新类别级几何记忆，在四个基准数据集上达到了领先性能。

### 研究问题
现有类别级物体位姿估计方法大多采用参数化形式（如固定形状先验或静态参数权重），将类别模式编码为固定表示，难以泛化到高度多样化的实例。如何提升大规模实例下的鲁棒性和可泛化性？

### 核心思路/方法
从记忆为中心的角度，设计一个外部记忆缓冲区，用于存储和动态更新从先前观察实例中提取的结构化几何表示，从而使模型能够利用累积经验辅助当前位姿估计。

### 主要贡献
1. 提出 MemPose 框架，将类别级几何记忆显式集成到位姿估计流程中。  
2. 引入外部记忆缓冲区及其动态更新机制，使模型能够积累并复用实例结构知识。  
3. 在 REAL275、CAMERA25、Housecat6D 和 Wild6D 四个挑战性基准上验证了方法优于此前最优方法。

### 局限性
摘要未提供足够信息。未提及计算开销、记忆容量限制、对新类别的零样本泛化能力，或在特定场景下的失败案例。

### 阅读优先级
高 — 理由：该工作针对类别级位姿估计的泛化瓶颈提出了新颖的记忆增强范式，实验覆盖多个标准及跨域数据集并取得 SOTA，对从事 3D 视觉、机器人操作或增强现实的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

In the pursuit of robust and generalizable category-level object pose estimation, most existing methods adopt parametric formulations that learn effective representations from data, yet they primarily encode category-level patterns into fixed shape priors or static parameter weights, which limits their scalability to highly diverse instances. In this paper, we rethink category-level pose estimation from a memory-centric perspective and present MemPose, a memory-augmented framework that explicitly incorporates category-level geometric memory into the pose estimation pipeline. We introduce an external memory buffer that stores and dynamically updates structural representations from previously observed instances, enabling the model to leverage accumulated experience to support current perception. Extensive experiments on four challenging benchmarks (REAL275, CAMERA25, Housecat6D and Wild6D) demonstrate the superiority of our proposed method over previous state-of-the-art approaches.

</details>

#### 2026-07-06 - Hybrid Deep Learning for Traceability and Classification of Industrial Slate Tiles

**Authors:** Soren Antebi, Stefan Eickeler, Sandra Halscheidt, Rene Schmitz, Michael Muellers, Dirk Hecker, Rafet Sifa
**Links:** [abs](https://arxiv.org/abs/2607.04811) - [pdf](https://arxiv.org/pdf/2607.04811)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** image matching, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hybrid Deep Learning for Traceability and Classification of Industrial Slate Tiles
- 作者：Soren Antebi, Stefan Eickeler, Sandra Halscheidt, Rene Schmitz, Michael Muellers, Dirk Hecker, Rafet Sifa
- 出版日期：2026-07-06
- 分类：3D Reconstruction & Multi-view Geometry（主要类别）
- 链接：https://arxiv.org/abs/2607.04811

### 一句话总结
本文提出了一种轻量级混合深度学习框架，结合图像匹配与分类分支，用于工业板岩瓷砖的实例级可追溯性与开采场地分类，在自建工业数据集上分别实现了+15.4% AUC的匹配提升和+10.9%精度的分类提升。

### 研究问题
如何利用深度学习对天然材料（板岩瓷砖）进行高效、准确的实例级再识别（traceability）和开采场地分类（extraction site classification），以提升工业生产线中的质量控制和效率。

### 核心思路/方法
设计并实现了一个轻量级混合深度学习系统，将图像匹配与分类整合在同一框架中：
- 特征匹配分支：基于XFeat特征提取器，并搭配LightGlue匹配头部，专门用于实例匹配。
- 分类分支：基于MobileNetV3网络。
- 特征融合：两个分支的骨干网络特征被共享并融合，用于辅助分类任务。
- 评估：在包含2,610张板岩瓷砖图像（来自六个开采场地）的新建工业数据集上进行实验。

### 主要贡献
1. 提出了一个轻量级混合深度学习框架，同时支持板岩瓷砖的实例级匹配和开采场地分类。
2. 通过XFeat+LightGlue的组合，在实例匹配任务上取得了+15.4% AUC的性能提升。
3. 通过特征共享与融合，分类准确率比标准MobileNetV3提高了+10.9%。
4. 在自行构建的工业板岩瓷砖数据集上验证了方法的有效性。

### 局限性
摘要未提供足够信息。例如：未说明模型推理速度、对不同光照或角度变化的鲁棒性、数据集是否平衡、方法是否存在特定失败案例以及是否与纯分类方法进行对比等。

### 阅读优先级
中。理由：该工作针对板岩瓷砖生产的工业场景，提出了轻量化的混合方法并取得明显提升，对工业应用开发有参考价值。但未提供下游部署细节或与其他先进方法的广泛对比，且摘要信息较为基础，适合作为领域入门或特定任务参考。

</details>

<details>
<summary>Abstract</summary>

Applying deep learning to instance-aware reidentification of slate tiles and extraction site classification can improve production efficiency and quality control in the slate tile industry. These tasks are particularly important for handling natural materials where visual variability can make manual inspection costly and error-prone. We present a lightweight, hybrid deep learning approach that combines image matching and classification within a single framework. The system integrates a feature-matching branch based on XFeat with a MobileNetV3- based classification branch. The XFeat branch, combined with a LightGlue matching head, improves instance matching performance by +15.4% AUC. For classification, features from both backbones are shared and fused, resulting in a +10.9% accuracy improvement over a standard MobileNetV3 model. Our approach is evaluated on a newly created industrial dataset consisting of 2,610 slate tile images from six extraction sites. The results demonstrate the effectiveness of the proposed approach for object re-identification and classification in an industrial setting.

</details>

#### 2026-07-06 - A Task-Driven Evaluation of UAV Detection and Tracking under Synthetic Fog

**Authors:** Amir Pouladi, Vesal Ahsani, Haijun Li, Homayoun Najjaran, Afzal Suleman
**Links:** [abs](https://arxiv.org/abs/2607.05467) - [pdf](https://arxiv.org/pdf/2607.05467)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Task-Driven Evaluation of UAV Detection and Tracking under Synthetic Fog
- 作者：Amir Pouladi, Vesal Ahsani, Haijun Li, Homayoun Najjaran, Afzal Suleman
- 出版日期：2026-07-06
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.05467

### 一句话总结
本文提出一个任务驱动的评估框架，通过合成雾气、图像恢复、目标检测与跟踪的流水线，分析雾气对无人机检测与跟踪性能的影响，并发现雾气主要增加漏检，雾气训练比测试时恢复更有效。

### 研究问题
雾气如何影响小型无人机在远距离天空主导图像中的检测与跟踪性能，以及图像恢复和训练策略对下游感知任务的真实增益。

### 核心思路/方法
1. 利用单目深度估计和大气散射模型，从真实晴朗天气图像合成逼真的雾气图像。
2. 比较经典、CNN和Transformer三类恢复方法，选出代表模型集成到下游感知流水线。
3. 在“仅干净图像训练”和“雾气加入训练”两种模式下评估多种检测器，并在干净、雾气和恢复后的视频序列上评估基于检测的跟踪。
4. 不仅评估图像级恢复指标，还评估雾气与恢复对检测鲁棒性和跟踪性能的实际影响。

### 主要贡献
1. 提出了一个将深度感知雾气合成、图像恢复、目标检测与跟踪统一起来的任务驱动评估框架。
2. 揭示了雾气主要通过增加漏检率显著降低检测和跟踪性能。
3. 发现雾气包含训练是提升鲁棒性最一致的方法，而测试时恢复仅在检测器仅用干净图像训练时才有明显帮助。
4. 证明恢复质量不必然转化为下游感知性能的等比例增益，需与检测和跟踪联合评估。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该研究直接解决“雾气下无人机检测跟踪”这一实际难题，提出了从合成数据生成到下游评估的完整流水线，实验设计清晰，结论（恢复质量≠感知增益、雾气训练优于测试恢复）对实际部署具有重要指导意义，适合从事无人机视觉、目标检测与跟踪以及恶劣环境感知的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

Fog severely degrades the visibility of small unmanned aerial vehicles (UAVs) in skydominant, long-range imagery, reducing the reliability of downstream detection and tracking. This paper presents a task-driven evaluation framework that links depth-aware synthetic fog generation, image restoration, object detection, and tracking within a unified pipeline. Given the practical difficulty of collecting and annotating foggy UAV scenes, synthetic fog is generated from real clear-weather outdoor images containing UAV targets using monocular depth estimation and the atmospheric scattering model. Representative restoration methods from classical, convolutional neural network (CNN)-based, and transformer-based families are first compared, after which the selected restoration model is integrated into the downstream perception pipeline. Detection is evaluated under both clean-only and fog-inclusive training regimes using multiple detector variants, while tracking-by-detection is assessed on clean, foggy, and restored video sequences. Beyond image-level restoration metrics, the study evaluates how fog and restoration affect detection robustness and tracking performance. The results show that fog substantially degrades both detection and tracking, primarily through increased missed detections. Fog-inclusive training provides the most consistent improvement in robustness, whereas test-time restoration is most beneficial when the detector has been trained only on clean imagery. These findings show that restoration quality does not necessarily translate into proportional gains in downstream perception and therefore should be evaluated jointly with detection and tracking performance.

</details>

#### 2026-07-06 - Targeted Structure Completion for Sparse-View 3D Reconstruction in Autonomous Driving

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, Liping Hou, Chao Ma
**Links:** [abs](https://arxiv.org/abs/2607.04661) - [pdf](https://arxiv.org/pdf/2607.04661)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, rendering, autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Targeted Structure Completion for Sparse-View 3D Reconstruction in Autonomous Driving
- 作者：Guoqing Wang, Pin Tang, Xiangxuan Ren, Liping Hou, Chao Ma
- 出版日期：2026-07-06
- 分类：3D Reconstruction & Multi-view Geometry; Embodied / Robotics / AR Applications
- 链接：arXiv:2607.04661

### 一句话总结
本文提出FocusGS框架，通过将3D重建的计算集中在几何模糊区域而非全局稠密化，实现了在自动驾驶稀疏视图场景下效率与质量的更优平衡。

### 研究问题
如何从稀疏、低重叠的观测数据中高效且完整地重建自动驾驶场景的三维结构，克服现有体素高斯方法计算冗余的问题。

### 核心思路/方法
- 从全局稠密化转向**针对性结构补全**：将结构补全过程与确定性区域解耦，仅对存在几何模糊的区域进行重点计算。
- 通过**3D几何模糊流形**精确定位易遮挡、高几何不确定性的局部区域。
- 设计**轻量级针对性结构补全模块**，在该非结构化的稀疏拓扑子空间内选择性实例化并优化连续高斯查询。

### 主要贡献
1. 提出FocusGS框架，首次实现从全局稠密化到靶向结构补全的范式转变。
2. 通过3D几何模糊流形有效定位几何不确定区域，并设计轻量模块进行针对性补全。
3. 在自动驾驶基准数据集上实现更优的效率-质量权衡，高斯数量减少约74%，渲染时间降低约34%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶中稀疏视图三维重建这一关键问题，提出了具有明确效率优势的新范式，实验数据显著且量化。对于关注自动驾驶感知、高效三维建模的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing 3D scene structures from sparse, low-overlap observations remains a fundamental challenge in autonomous driving. Recent state-of-the-art frameworks achieve promising results by incorporating voxel-based Gaussians, but incur substantial computational redundancy due to a uniform volumetric processing strategy. To bridge the gap between the efficiency of pixel-based Gaussian methods and the structural completeness of voxel-based Gaussian approaches, we propose FocusGS, a simple yet effective framework that shifts the paradigm from global densification to targeted structural completion. Our central insight is that structural completion should be decoupled from deterministic regions, with computation concentrated exclusively on areas exhibiting geometric ambiguity. Specifically, FocusGS addresses the localization challenge by deriving a 3D Geometric Ambiguity Manifold to accurately isolate localized areas prone to occlusion and high geometric uncertainty. To overcome the subsequent manifold completion challenge, we design a lightweight targeted structure completion module that selectively instantiates and optimizes continuous Gaussian queries strictly within this unstructured, sparse topological subspace. Extensive experiments demonstrate that FocusGS achieves a superior efficiency-quality trade-off, advancing state-of-the-art performance on driving-centric benchmarks while naturally reducing the total number of Gaussians by ~74% and decreasing rendering time by ~34%.

</details>

#### 2026-07-05 - HeartVolMesh: Cardiac Volumetric Mesh Reconstruction via Covariance-Guided Graph Deformation

**Authors:** Fengming Lin, Arezoo Zakeri, Haoran Dou, Zherui Zhou, Shaokun Lan, Jinming Duan, Alejandro Frangi
**Links:** [abs](https://arxiv.org/abs/2607.04243) - [pdf](https://arxiv.org/pdf/2607.04243)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HeartVolMesh: Cardiac Volumetric Mesh Reconstruction via Covariance-Guided Graph Deformation  
- 作者：Fengming Lin, Arezoo Zakeri, Haoran Dou, Zherui Zhou, Shaokun Lan, Jinming Duan, Alejandro Frangi  
- 出版日期：2026-07-05  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：abstract: https://arxiv.org/abs/2607.04243 ; pdf: https://arxiv.org/pdf/2607.04243  

### 一句话总结
HeartVolMesh 提出一种协方差引导的图变形方法，直接从体图像重建各向异性高斯核表示的患者特异性四面体心脏网格，避免传统分割-建模流程的薄壁模糊问题，并保持跨案例对应性。

### 研究问题
如何从体图像准确重建具有跨案例拓扑对应性的患者特异性四面体心脏网格，同时克服传统分割后建模流程中薄壁结构模糊的缺陷。

### 核心思路/方法
1. **表示与预测**：将模板顶点提升为各向异性高斯核，使用3D CNN-GNN 联合预测每个顶点的位移和Cholesky参数化的协方差矩阵。  
2. **训练损失**：采用协方差感知的负对数似然损失，并辅以轻量级网格正则化。  
3. **体积网格生成**：将固定四面体模板通过分阶段对齐、非刚性配准和变形传播映射到重建表面，通过模板密度控制分辨率，自动保持网格连接性和跨案例对应。

### 主要贡献
1. 提出HeartVolMesh，实现直接从体图像到四面体心脏网格的端到端重建，无需中间分割步骤。  
2. 引入协方差引导的图变形机制，通过各向异性高斯核和Cholesky参数化提升重建精度。  
3. 实验表明，相比基于变形的基线方法，在表面网格精度和体积网格保真度上均取得一致提升。

### 局限性
摘要未提供足够信息（如：未说明模型在不同心脏结构（如心房/心室）、极端病理案例或小规模训练数据下的表现，也未提及计算效率或临床验证结果）。

### 阅读优先级
**高**  
理由：该方法针对心脏体积网格重建中的关键痛点（薄壁模糊、对应性缺失）提出了创新性的协方差引导变形框架，实验性能优于基线，且发布于2026年，对于从事计算心脏病学、医学图像重建及有限元仿真的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate patient-specific tetrahedral cardiac meshes are essential for in-silico trials, yet common segmentation-then-modelling pipelines can blur thin-wall anatomy and offer limited cross-case correspondence. We propose HeartVolMesh, which lifts each template vertex to an anisotropic Gaussian kernel and uses a 3D CNN-GNN to predict per-vertex displacements and Cholesky-parameterized covariances from volumetric images. Training is guided by a covariance-aware negative log-likelihood loss with lightweight mesh regularization. For volumetric meshing, we warp a fixed tetrahedral template to the reconstructed surface via staged alignment, non-rigid registration, and deformation propagation, preserving connectivity and correspondence by construction, with resolution controlled by template density. Experiments show consistent gains over deformation-based baselines in surface mesh accuracy and volumetric mesh fidelity.

</details>

#### 2026-07-05 - Neural LiDAR Bundle Adjustment

**Authors:** Chin Yung Anson Hon, Kaicheng Zhang, Sen Wang
**Links:** [abs](https://arxiv.org/abs/2607.04169) - [pdf](https://arxiv.org/pdf/2607.04169)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, bundle adjustment, 3D mapping, NeRF, neural radiance field, radiance field, rendering, radiance, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Neural LiDAR Bundle Adjustment
- 作者：Chin Yung Anson Hon, Kaicheng Zhang, Sen Wang
- 出版日期：2026-07-05
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2607.04169；PDF: https://arxiv.org/pdf/2607.04169

### 一句话总结
本文发现LiDAR NeRF中体素采样密度对性能影响显著，并据此提出一种基于LiDAR光线高效采样的神经光束调整算法NeLD-BA，用于联合优化LiDAR地图与姿态。

### 研究问题
现有RGB NeRF与LiDAR NeRF之间存在关键设计差异（特别是体素采样原理），如何利用这一差异改进LiDAR场景的联合地图构建与姿态优化？

### 核心思路/方法
- 理论及实证证明：LiDAR NeRF中体积采样的密度起重要作用。
- 基于上述发现，设计Neural LiDAR Bundle Adjustment (NeLD-BA)算法，核心是对LiDAR光线采用高效体积采样策略，以实现LiDAR地图与相机位姿的联合优化。

### 主要贡献
- 首次从理论和实证角度阐明体积采样密度在LiDAR NeRF中的关键作用。
- 提出NeLD-BA算法，在Newer College和FusionPortable数据集上实现多视点云配准与3D建图的先进性能（state-of-the-art）。
- 承诺开源代码。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由是：该工作直接回应了RGB NeRF与LiDAR NeRF设计差异未被充分探索的问题，提出的NeLD-BA方法在公开数据集上达到SOTA，且具有理论分析支持，对神经隐式表达与激光雷达SLAM交叉领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent research has achieved remarkable novel view rendering and scene reconstruction results with Neural Radiance Field (NeRF), including extensions to the LiDAR modality. Few studies have, however, explored the key design differences between RGB NeRFs and LiDAR NeRFs, particularly considering their underlying working principles. In this work, we provide both theoretical and empirical evidence suggesting that the density of volume sampling plays a significant role in LiDAR NeRF. Based on this finding, we propose a novel Neural LiDAR Bundle Adjustment (NeLD-BA) algorithm, which is tailored using efficient volume sampling of LiDAR rays for joint optimization of LiDAR map and poses. Extensive experiments are performed using the Newer College and FusionPortable datasets to demonstrate the proposed NeLD-BA's state-of-the-art performance in multi-view point cloud registration and 3D mapping. We will open-source our code for the community.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-09 - Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery

**Authors:** Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos
**Links:** [abs](https://arxiv.org/abs/2607.08408) - [pdf](https://arxiv.org/pdf/2607.08408)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, scene representation, splatting, mapping

<details>
<summary>Abstract</summary>

Gaussian splatting is the current state-of-the-art for dense, deformable 3D anatomy reconstruction in robot-assisted minimally invasive surgery (RAMIS); however, most pipelines are offline and depend on accurate camera trajectory priors (often from robotic kinematics), limiting applicability when priors are missing or noisy. To address these limitations, we propose Track2Map, an online 3D Gaussian Splatting pipeline that jointly optimizes camera trajectory and 3D deformable scene representation directly from surgical video. Track2Map is therefore capable of robust 3D reconstructions when camera trajectory priors are either absent or noisy, and due to its online nature it effectively works as a Simultaneous Localisation and Mapping (SLAM) method. To stabilize optimization in the presence of tissue motion and ambiguous visual cues, we introduce a track-anchored deformation initialization using dense 2D point tracks. Track statistics are further utilized to disentangle camera motion from scene deformation by detecting static camera periods and reducing drift during incremental mapping. Experiments on StereoMIS show improved reconstruction quality and camera trajectory against competing SLAM methods, as well as compared to non-SLAM methods that utilize camera trajectory priors. The code is available at https://track2map.github.io/.

</details>

#### 2026-07-09 - LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting

**Authors:** Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan
**Links:** [abs](https://arxiv.org/abs/2607.08016) - [pdf](https://arxiv.org/pdf/2607.08016)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>Abstract</summary>

Video relighting requires balancing long-form temporal consistency with a physically grounded understanding of light transport, which depends on accurate estimation of intrinsic scene properties such as materials, geometry, and illumination. Existing methods follow two paradigms: (1) reconstruct a video's photometric properties via inverse rendering and relight them to a target illumination via forward rendering, using physically-based rendering (PBR) or a neural renderer; these suffer from noisy reconstructions and struggle with hard-to-model effects such as global illumination. (2) Frame the task as generative video-to-video translation conditioned on relighting targets (a target environment map or text); this limits relighting control and temporal stability, since diffusion models struggle to translate long-form videos, and is constrained by the availability of input/relit training pairs. We propose LightCrafter, a hybrid pipeline that reformulates video relighting as video translation of a proxy video: rather than translating the input video directly to the target, we translate a PBR rendering of the input under the target illumination to the final target. This bakes illumination targets into the PBR proxy, removing the need to teach the diffusion model illumination concepts like environment maps, and enables more intricate lighting control while naturally providing long-form temporal consistency. We show PBR renders alone already outperform some prior art but struggle with effects like global illumination; to capture these, we leverage photometric priors in video generation models by post-training CogVideoX on synthetic video pairs and real-world unpaired videos. We outperform prior state-of-the-art on existing real-world relighting benchmarks and contribute a synthetic benchmark for further analysis. We will release our dataset, benchmark, metrics, and code.

</details>

#### 2026-07-08 - SoccerNet 2026 Challenges Results

**Authors:** Anthony Cioppa, Silvio Giancola, Håkan Ardö, Mohamad Dalal, Jan Held, Jérémie Ochin, Jiayuan Rao, Karen Sanchez, Renaud Vandeghen, Artur Xarles, Olivier Barnich, Albert Clapés, Mathieu Delvaux, Sergio Escalera, Bernard Ghanem, Cédric Hons, Antoine Houet, Sotiris Manitsaris, Tom Michel, Pierre Miralles, Thomas B. Moeslund, Mikael Nilsson, Bogdan Stanciulescu, Marc Van Droogenbroeck, Yanfeng Wang, Weidi Xie, Faisal Altawijri, Mohamed Atef, Semen Budennyy, Vasiliy Chelpanov, Puhua Chen, Yixin Chen, Lechao Cheng, Jianling Chu, Ju-Seong Do, Oleg Durygin, Omar Fetouh, Mirco Fuchs, Youssef Ghallab, Falguni Ghosh, Wonjun Heo, Yufeng Hu, Weixuan Huang, Phuong-Linh Huynh-Ha, Matvey Isupov, Yangguang Ji, Siyuan Jiang, Zhenxiang Jiang, Wonyong Jo, Ho-Young Jung, SeongHeon Kang, MinJae Kim, Youngseon Kim, Jakub Komosa, Artem Konshin, Trung-Hoang Le, Jongmin Lee, Lingling Li, Litao Li, Vadim Linkov, Fang Liu, Haoxuan Ma, Shun Makino, Ismail Mathkour, Konstantin Mitin, Mikhail Moiseev, Takumi Nagaya, Yuki Nakamura, Thanh-Khoi Nguyen, Hoang-Phuc Nguyen, Trong-Thuan Nguyen, Christian Orduz, Kwanyong Park, Fabian Perez, Parthsarthi Rawat, SuHyun Rim, Hoover Rueda-Chacón, Atom Scott, Minori Sugimura, Yuyang Sun, Shengeng Tang, Minh-Triet Tran, Ikuma Uchida, Juan Vanegas, Thanh-Nhan Vo, Jiangtao Wang, Yaxiong Wang, Xiaogang Wang, Ruifeng Wang, Rio Watanabe, Jiali Wen, Yongliang Wu, Di Yang, Xu Yang, Zhuo Yang, Xinyu Ye, Yibo Yu, Zihan Zhai, Yu Zhang, Zhenyu Zhao, Zhun Zhong, Yixi Zhou, Xingyu Zhu, Wenbo Zhu, Julian Ziegler
**Links:** [abs](https://arxiv.org/abs/2607.07320) - [pdf](https://arxiv.org/pdf/2607.07320)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SoccerNet 2026 Challenges Results
- 作者：Anthony Cioppa, Silvio Giancola, Håkan Ardö 等（共88位作者）
- 出版日期：2026-07-08
- 分类：场景表征与渲染（Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2607.07320

### 一句话总结
本文是SoccerNet 2026挑战赛的结果报告，记录了五个计算机视觉任务的设置、评估协议、排行榜以及最佳提交方案。

### 研究问题
如何通过标准化基准和公开竞赛推动体育视频理解领域的计算机视觉研究，具体涵盖球动作预测、球员定位、新视角合成、场地区域定位以及视觉问答五个任务。

### 核心思路/方法
组织方为每个任务提供了标注数据、统一评估协议和公开基线，邀请全球团队提交算法结果。最终427支队伍提交了1129份参赛作品，28支队伍贡献了经评审的技术报告。本文汇总了各任务的评价设置及领先方案。

### 主要贡献
1. 组织了第六届SoccerNet年度挑战赛，涵盖五个视觉任务。
2. 发布了各任务的排行榜和领先方法总结。
3. 提供了一个在保留测试数据上评估当前技术水平的公开记录。

### 局限性
摘要未提供足够信息，未说明各任务的具体性能指标、基线方法的缺陷、数据规模或竞赛中暴露的普遍未解决问题。

### 阅读优先级
低。本文是竞赛结果汇总，适合需要了解体育视频分析领域多个任务最新进展的读者，但对具体技术细节和深度分析无帮助。

</details>

<details>
<summary>Abstract</summary>

The SoccerNet 2026 Challenges constitute the sixth annual edition of the SoccerNet open benchmarking effort, dedicated to advancing computer vision research in sports video understanding. This year's challenges span five vision-based tasks: (1) Ball Action Anticipation, predicting the timing and class of ball-related actions within a short future window from a preceding observation window; (2) Player-Centric Ball Action Spotting, temporally localizing and classifying ball-related actions while assigning each action to the acting player through team affiliation and jersey number; (3) Novel View Synthesis, rendering images from unobserved camera poses in multi-view football scenes; (4) Spiideo SoccerNet Synloc, localizing athletes in real-world pitch coordinates from a single calibrated static-camera image; and (5) Visual Question Answering, answering multiple-choice questions about football broadcasts across text, image, and video inputs. For each task, participants were provided with annotated data, a unified evaluation protocol, and a public baseline. This edition saw broad participation, with 427 teams submitting 1,129 entries across the five tasks and 28 teams contributing reviewed technical reports. This paper describes each task and its evaluation protocol, presents the challenge leaderboards, and summarizes the leading submissions, with the aim of documenting the current state of each task as measured on held-out challenge data.

</details>

#### 2026-07-07 - RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation

**Authors:** Shujie Zhang, Jingkun Yi, Weipeng Zhong, Zirui Zhou, Yangkun Zhu, Hanqing Wang, Xudong Xu, Weinan Zhang, Chunhua Shen
**Links:** [abs](https://arxiv.org/abs/2607.06699) - [pdf](https://arxiv.org/pdf/2607.06699)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation
- 作者：Shujie Zhang, Jingkun Yi, Weipeng Zhong, Zirui Zhou, Yangkun Zhu, Hanqing Wang, Xudong Xu, Weinan Zhang, Chunhua Shen
- 出版日期：2026-07-07
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2607.06699, PDF: https://arxiv.org/pdf/2607.06699

### 一句话总结
RoboSnap 是一种能从单张 RGB 图像快速生成可用于机器人交互与策略评估的仿真场景的实时方法，通过分层设计分离物理交互区域与视觉背景。

### 研究问题
如何将真实世界场景高效地转换为既物理稳定又视觉保真的交互式仿真环境，以支持通用机器人学习和可重复策略评估。

### 核心思路/方法
- 采用分层设计（layered design）：将物理关键交互区域与周围视觉背景分离。
- 针对交互区域：使用碰撞感知的前景资产，经细化处理以支持稳定机器人交互。
- 针对背景：使用 3D 高斯泼溅视觉层，在新视角下保留逼真的背景外观。
- 整体流程：输入单张 RGB 图像 → 输出可立即用于仿真的场景。

### 主要贡献
1. 提出 RoboSnap：一个仅需单张 RGB 图像即可生成仿真就绪场景的实时转换框架。
2. 提出分层设计：分离物理关键区域与视觉背景，兼顾交互稳定性与视觉保真度。
3. 引入 DROID-Sim 数据集：基于 DROID 中 564 个真实场景构建的配套实景-仿真数据集，推动该领域研究。
4. 实验表明 RoboSnap 在恢复场景中能可靠重放轨迹，支持策略训练的任务特定合成数据生成，并产生有意义的仿真-真实相关性。

### 局限性
摘要未提供足够信息以评估 RoboSnap 的具体局限性，例如对复杂光照、遮挡或动态物体的处理能力等均未提及。

### 阅读优先级
**中**  
理由：该方法在机器人学习与仿真领域具有明确创新性（单图生成、分层设计），但来自单一团队且未在摘要中展开实验细节或失败案例，适合对该方向有基础兴趣的读者作为技术入门，但对追求深入技术对比或性能验证的读者可能信息不足。

</details>

<details>
<summary>Abstract</summary>

Recovering real-world scenes as interactive simulation environments can enable generalizable robot learning and reproducible policy evaluation. However, constructing scenes that are both physically stable and visually faithful remains slow and expensive. In this work, we present RoboSnap, a real-to-sim framework that turns a single RGB image into a simulation-ready scene. The key idea is a layered design that separates the physics-critical interaction area from the surrounding visual context: collision-aware foreground assets are refined for stable robot interaction, while a 3D Gaussian splatting visual layer preserves faithful background appearance under novel views. Experiments on DROID scenes and real-robot tasks show that RoboSnap achieves reliable trajectory replay in the recovered scenes, supports task-specific synthetic data generation for policy training, and yields meaningful sim-real correlation for policy evaluation. To further support real-to-sim research, we introduce DROID-Sim, a real-to-sim companion dataset constructed from 564 real-world scenes in DROID. Extensive experiments suggest that the value of real-to-sim methods lies not only in high-fidelity visual reconstruction, but in turning real environments into reusable infrastructure for robot learning and evaluation.

</details>

#### 2026-07-07 - GaussFusion: Towards Multimodal 3D Gaussian Pretraining

**Authors:** Zhixuan You, Jihua Zhu, Yiding Sun, Zihao Guo, Haozhe Cheng, Dongxu Zhang, Lin Chen, Hainan Luo
**Links:** [abs](https://arxiv.org/abs/2607.05906) - [pdf](https://arxiv.org/pdf/2607.05906)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussFusion: Towards Multimodal 3D Gaussian Pretraining
- 作者：Zhixuan You, Jihua Zhu, Yiding Sun, Zihao Guo, Haozhe Cheng, Dongxu Zhang, Lin Chen, Hainan Luo
- 出版日期：2026-07-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.05906

### 一句话总结
GaussFusion 提出一种多模态3D高斯预训练框架，通过融合图像与文本监督信号提升高斯表示的可迁移性，在分类下游任务中优于现有方法。

### 研究问题
如何设计预训练任务，使3D高斯表示不仅捕获局部几何和外观结构，还能学习视觉和语言级别的语义信息，从而提升其可迁移性。

### 核心思路/方法
1. **多模态预训练框架**：将图像和文本监督信号集成到掩码高斯建模中，通过跨模态语义对齐，使高斯编码器学习跨模态语义。
2. **高斯显著性引导的多尺度空洞掩码（GSHM）**：针对高斯原始分布不均匀的特点，基于高斯显著性构造空间连续掩码区域，并在多尺度上应用空洞掩码，强制编码器同时学习细粒度局部模式和更广泛的上下文依赖。

### 主要贡献
1. 提出了第一个融合图像与文本监督的多模态3D高斯预训练框架（GaussFusion）。
2. 设计了高斯显著性引导的多尺度空洞掩码（GSHM），适应非均匀的高斯分布，增强掩码建模的效果。
3. 实验表明GaussFusion在ModelNet40与ScanObjectNN（PB-T50-RS）上分别比高斯-掩码自动编码器（Gaussian-MAE）绝对提升0.61%和3.85%。

### 局限性
摘要未提供足够信息，未提及方法在泛化性、计算效率或极端场景下的局限性。

### 阅读优先级
**中**。理由：该工作专注于3D高斯表示学习的预训练阶段，创新点（多模态融合与自适应掩码）明确，且定量提升具体；但当前未提供更多下游任务（如分割、渲染）结果，也未讨论局限性，适合对3D表示学习有兴趣的读者跟踪进展。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting provides an explicit representation that jointly models geometry and appearance, serving as a scalable foundation for 3D representation learning. Existing pre-training methods for Gaussian representations, such as masked Gaussian reconstruction, primarily capture local structures but offer limited semantic supervision. In this paper, we propose GaussFusion, a multimodal pre-training framework for 3D Gaussian representations. GaussFusion integrates image and text supervision into masked Gaussian modeling through cross-modal semantic alignment, enabling the Gaussian encoder to learn both visual and language-level semantic information during pre-training. To better adapt masked modeling to the non-uniform distribution of Gaussian primitives, we further propose Gaussian Salience-guided Multi-scale Hole Masking (GSHM). GSHM constructs spatially continuous masked regions based on Gaussian salience. By applying hole masks at multiple scales, GSHM encourages the encoder to capture both fine-grained local patterns and broader structural dependencies. Extensive experiments on downstream tasks demonstrate that GaussFusion improves the transferability of Gaussian representations. Notably, GaussFusion outperforms Gaussian-MAE on ModelNet40 and ScanObjectNN (PB-T50-RS) by 0.61\% and 3.85\%, respectively.

</details>

#### 2026-07-06 - SSA-3DGS: Unsupervised Removal of Screen-Space Artifacts for 3D Gaussian Splatting

**Authors:** Kristof Overdulve, Lode Jorissen, Nick Michiels
**Links:** [abs](https://arxiv.org/abs/2607.05598) - [pdf](https://arxiv.org/pdf/2607.05598)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SSA-3DGS: Unsupervised Removal of Screen-Space Artifacts for 3D Gaussian Splatting
- 作者：Kristof Overdulve, Lode Jorissen, Nick Michiels
- 出版日期：2026-07-06
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.05598

### 一句话总结
提出无监督框架SSA-3DGS，联合优化3D场景与可学习2D覆盖层，从多视角输入中去除屏幕空间伪影，恢复干净3D场景。

### 研究问题
如何在不使用监督信号或人工标注的情况下，从包含静态二维固定伪影（如传感器缺陷、遮挡物、数字叠加层等）的多视角输入图像中，恢复干净的3D场景表示，同时分离出这些伪影。

### 核心思路/方法
- 利用视图间的几何一致性，设计一个无监督框架。
- 联合优化：同时优化一个3D高斯场景表示和一个可学习的2D覆盖层（overlay）。
- 通过2D覆盖层捕获固定在图像平面上的屏幕空间伪影，而3D场景部分则专注于一致性的3D几何信息，从而实现两者的分离。

### 主要贡献
- 提出SSA-3DGS，首个无需监督或人工干预即可从3D高斯泼溅重建中去除屏幕空间伪影的无监督方法。
- 在多种合成伪影和真实捕获数据集上，该方法相比直接使用带噪输入训练的3DGS，PSNR提升最高达9 dB，同时能忠实保留伪影本身（作为分离出的2D覆盖层）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法针对3DGS在实际应用中（如自动驾驶、移动设备捕获）鲁棒性不足的关键问题，提出了一个简洁、无监督的解决方案，且实验效果提升显著（PSNR最高提升9 dB）。对于关注3D场景表示实用化和鲁棒性的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Novel View Synthesis (NVS) methods, such as 3D Gaussian Splatting (3DGS), rely heavily on the assumption of clean, multi-view consistent, posed input images. Real-world captures can violate this assumption due to screen-space artifacts-static occlusions fixed to the 2D image plane rather than to the 3D world. Common examples include physical sensor defects, environmental obstructions (such as rain or mud on the lens enclosure), capture obstructions (such as a thumb over the camera sensor or a dashboard visible in dashcam footage), and digital overlays (such as watermarks or UI elements). When present, they are erroneously baked into the 3D geometry as "floaters" or near-camera artifacts, degrading the quality of novel-view rendering. In this work, we propose SSA-3DGS, an unsupervised framework that jointly optimizes a 3D scene and a learnable 2D overlay to recover a clean 3D scene and the corrupting artifacts. By exploiting geometric consensus across views, our method effectively disentangles static artifacts from the 3D scene geometry without supervision or manual input. Across diverse synthetic corruptions and a self-captured real-world dataset, SSA-3DGS improves reconstruction fidelity by up to 9 dB PSNR over 3DGS trained on the same corrupted inputs, while faithfully preserving the corrupting artifact.

</details>

#### 2026-07-06 - Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control

**Authors:** Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang
**Links:** [abs](https://arxiv.org/abs/2607.05522) - [pdf](https://arxiv.org/pdf/2607.05522)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control
- 作者：Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang
- 出版日期：2026-07-06
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.05522

### 一句话总结
提出一个渲染感知的贝叶斯3D高斯泼溅框架，通过引入正态逆威沙特后验和狄利克雷过程扩展，实现原生不确定性和自适应复杂度控制，并在主动视角选择等任务中显著优于标准基线。

### 研究问题
标准3D高斯泼溅训练依赖点估计和手工启发式规则，缺乏原生不确定性估计和自适应的复杂度控制，这限制了其在稀疏视角或固定采集预算场景下的表现，例如模型无法识别弱支持的几何结构或选择信息量最大的视角。

### 核心思路/方法
1. 使用正态逆威沙特（NIW）后验来追踪高斯几何的均值和协方差，其中后验的构成利用渲染器导出的替代摘要（surrogate summaries）计算。
2. 引入可选狄利克雷过程扩展，提供概率性的组件使用信号（component-usage signal），使复杂度控制具有适应性。
3. 训练调度明确了闭式与近似推断的边界。通过重新渲染后验几何样本，获得原生预测不确定性，用于区间校准和主动视角选择。

### 主要贡献
1. 提出渲染感知贝叶斯3DGS框架，原生支持不确定性估计和复杂度控制。
2. 在固定预算（16到32）的主动视角选择任务中，NIW主动采集在PSNR上提升0.453 dB、LPIPS降低0.0146，优于3成员标准集成基线（在29/39场景-种子对和10/13场景均值上获胜）。
3. NIW原生区间的95%覆盖误差较共享代理（proxy）方法降低约17倍（0.046 vs. 0.796），较3成员深度集成降低约10倍（0.047 vs. 0.454），且训练成本约为后者的三分之一。
4. 作为重建兼容性验证，NIW在39个场景-种子运行上平均提升0.030 dB PSNR，仅增加1.6%训练时间。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法将贝叶斯推断引入3DGS，解决了稀疏视角下不确定性估计和复杂度控制的关键问题，实验效果显著且训练成本非常低，对于从事神经渲染、主动视角选择或可靠性需求高的场景重建的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian splatting (3DGS) is a strong representation for real-time novel-view synthesis, but its standard training pipeline relies on point estimates and hand-tuned heuristics, providing no native uncertainty or principled complexity control. This is most limiting under sparse views or fixed acquisition budgets, where a model must identify weakly supported geometry and select informative views. We introduce a rendering-aware Bayesian 3DGS framework that tracks Gaussian geometry with a Normal-Inverse-Wishart posterior over means and covariances using renderer-derived surrogate summaries. An optional Dirichlet-process extension adds a probabilistic component-usage signal, and the training schedule makes the closed-form versus approximate inference boundary explicit. Re-rendering posterior geometry samples yields native predictive uncertainty for interval calibration and active view selection. In a fixed-budget 16-to-32 active-view task, native NIW acquisition improves PSNR by +0.453 dB and LPIPS by -0.0146 over a scoring-only 3-member standard-ensemble baseline, winning 29/39 scene-seed pairs and 10/13 scene means; it also improves over PPU-style (+0.355 dB) and NIW-proxy (+0.401 dB) acquisition. NIW native intervals reduce 95% coverage error by about 17x relative to a shared proxy (0.046 vs. 0.796) and are about 10x closer to nominal coverage than a 3-member deep ensemble (0.047 vs. 0.454) at roughly one-third the training cost. As a reconstruction compatibility check, paired NIW-vs-standard analysis over 39 scene-seed runs yields +0.030 dB PSNR with 1.6% additional training time. These results position Bayesian 3DGS as a practical probabilistic scene representation for decision-facing tasks such as active view selection.

</details>

#### 2026-07-06 - WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images

**Authors:** Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan
**Links:** [abs](https://arxiv.org/abs/2607.05347) - [pdf](https://arxiv.org/pdf/2607.05347)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images
- 作者：Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan
- 出版日期：2026-07-06
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.05347

### 一句话总结
WildSplat 是首个基于前馈3D高斯溅射的框架，能够从无姿态的“野生”图像（光照变化剧烈）中，实现外观自适应的新视角合成。

### 研究问题
现有的前馈3D重建方法在光照条件变化的“野生”场景（in-the-wild images）中表现不佳，无法从无相机姿态的稀疏输入图像中高效、鲁棒地合成新视角。

### 核心思路/方法
1.  **双分支架构**：显式解耦几何与外观。几何分支提取光照不变的3D结构，并联合估计相机姿态；外观分支通过全局预调制交叉注意力机制，将目标外观线索注入内容特征，从而控制渲染外观。
2.  **联合多参考训练策略**：通过稳定训练过程，进一步防止几何与外观特征的纠缠。

### 主要贡献
1.  首次提出面向“野生”图像的前馈3D高斯溅射框架，支持外观条件新视角合成。
2.  提出显式解耦几何与外型的双分支架构，并设计预调制交叉注意力机制注入外观信息。
3.  引入联合多参考训练策略以稳定训练并防止特征纠缠。
4.  在“野生”新视角合成和外观编辑任务中，以单次前向传播超越现有基于优化和前馈的方法，达到最先进水平。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作解决了前馈3D重建在光照变化剧烈场景下的长期难点，首次将3D高斯溅射引入“野生”图领域，设计新颖且实验性能大幅超越基线。对神经渲染、新视角合成及场景外观编辑方向的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

While feedforward 3D reconstruction excels at efficient novel view synthesis, it typically falters when faced with scenes under varying illumination. To this end, we introduce WildSplat, the first feedforward 3D Gaussian Splatting framework capable of appearance-conditioned novel-view synthesis for unposed in-the-wild images. To handle inconsistent photometric conditions, we propose a dual-branch architecture that explicitly decouples geometry from appearance. The geometry branch extracts an appearance-invariant 3D structure and jointly predicts camera poses. To govern the rendering appearance, the appearance branch injects target appearance cues into the content features via a globally pre-modulated cross-attention mechanism. To further prevent feature entanglement, we introduce a joint multi-reference training strategy that stabilizes the training process. Extensive experiments show that WildSplat surpasses existing optimization-based and feedforward methods, achieving state-of-the-art performance in in-the-wild novel view synthesis and appearance editing from sparse inputs in a single forward pass.

</details>

#### 2026-07-05 - Semantic-Guided Progressive Object Removal with Gaussian Splatting

**Authors:** Xianliang Huang, Chen Xiao, Yuanxiang Ni, Guanming Liu, Mingkai Liu, Dikai Fan, Xiao Liu, Hao Zhang
**Links:** [abs](https://arxiv.org/abs/2607.04144) - [pdf](https://arxiv.org/pdf/2607.04144)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, Gaussian Splatting, splatting, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Semantic-Guided Progressive Object Removal with Gaussian Splatting  
- 作者：Xianliang Huang, Chen Xiao, Yuanxiang Ni, Guanming Liu, Mingkai Liu, Dikai Fan, Xiao Liu, Hao Zhang  
- 出版日期：2026-07-05  
- 分类：主类别：神经场景表示与渲染；次类别：具身/机器人/AR应用  
- 链接：摘要 https://arxiv.org/abs/2607.04144 | PDF https://arxiv.org/pdf/2607.04144  

### 一句话总结
本文提出一种基于语义引导和渐进式区域精化的3D物体去除框架，利用DINOv2编码多视角语义信息，并结合高斯点渲染实现高质量、跨视图一致的物体移除。

### 研究问题
如何在高斯点渲染框架下，利用多视角语义信息，高质量地去除重建3D场景中的目标物体并填补缺失区域。

### 核心思路/方法
1. **语义引导的块匹配（SBM）**：使用DINOv2从多视图观测中编码语义引导，解码最佳匹配块以在目标视图中补全缺失区域，同时保持跨视图一致性。  
2. **渐进式区域精化（RPR）**：将目标掩码分割为多个子区域，仅选择视觉质量较差的子区域进行迭代优化，提升效率与质量。  
3. **基于高斯点渲染**：整个框架构建在高斯点渲染之上，保证重建高保真度和计算高效性。

### 主要贡献
- 首次将语义引导（DINOv2编码）与块匹配相结合用于3D物体移除，提升复杂几何与纹理的处理能力。  
- 提出渐进式区域精化策略，避免一次性处理整个掩码区域，提高修复质量和效率。  
- 实验表明，该方法在感知质量和3D物体移除的一致性上优于现有基于高斯的同类方法。

### 局限性
摘要未提供足够信息，无法判断该方法的局限性（如对复杂场景的鲁棒性、计算开销的具体范围等）。

### 阅读优先级
- **中**  
- **理由**：该方法针对3D物体去除任务提出了新颖的语义引导与渐进式优化策略，对于从事AR/VR、机器人及数字内容创作的研究者具有参考价值；但摘要未提供定量实验结果或对比细节，需进一步阅读全文评估其性能上限与适用场景。

</details>

<details>
<summary>Abstract</summary>

Removing unwanted objects from reconstructed 3D scenes is an important task in computer vision, supporting applications in AR/VR, robotics, and digital content creation. Existing methods typically complete the entire masked region in a single step and without effectively utilizing semantic information from other views, leading to difficulties in handling complex geometric details and textures. In this work, we propose a novel framework that integrates Semantic-guided Block Matching (SBM) and Region-Wise Progressive Refinement (RPR) for high-quality 3D object removal. First, we leverage DINOv2 to encode semantic guidance from multi-view observations, and the best match tokens are decoded to complete missing regions in the target view while maintaining cross-view consistency. Second, we introduce a RPR strategy that segments the target mask into multiple subregions and selectively refines those with poor visual quality. Our method is built upon Gaussian Splatting, ensuring high-fidelity scene reconstruction with efficient computation. Experimental results demonstrate that our approach outperforms existing Gaussian-based methods in terms of perceptual quality and coherence in 3D object removal.

</details>

#### 2026-07-05 - Real-Time LiDAR Gaussian Splatting SLAM

**Authors:** Seungjun Tak, Yewon Jeon, Jaeik Hwang, SukMin Hwang, Seongbo Ha, Hyeonwoo Yu
**Links:** [abs](https://arxiv.org/abs/2607.04127) - [pdf](https://arxiv.org/pdf/2607.04127)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-Time LiDAR Gaussian Splatting SLAM  
- 作者：Seungjun Tak, Yewon Jeon, Jaeik Hwang, SukMin Hwang, Seongbo Ha, Hyeonwoo Yu  
- 出版日期：2026-07-05  
- 分类：Neural Scene Representations & Rendering; 3D Reconstruction & Multi-view Geometry  
- 链接：抽象页 https://arxiv.org/abs/2607.04127 | PDF https://arxiv.org/pdf/2607.04127  

### 一句话总结
该论文提出一种基于LiDAR的实时高斯泼溅SLAM框架，通过紧耦合G-ICP配准与球面光栅化稠密建图，实现大规模序列上的高效同步定位与高质量地图表示。

### 研究问题
如何利用LiDAR几何信息（而非外观）构建实时、可扩展且几何精确的高斯泼溅SLAM系统，以克服传统方法在大规模场景中的速度与精度瓶颈。

### 核心思路/方法
1. **紧耦合前端**：将快速G-ICP配准与球面光栅化稠密建图紧密结合，实现实时处理。  
2. **几何初始化**：重用跟踪阶段估计的局部协方差，初始化高斯体，使其具有距离感知尺度，并导出表面法向以进行几何感知地图优化。  
3. **自适应优化**：引入基于协方差的几何分数，衡量局部复杂度，从而在平面区域进行剪枝，在结构丰富区域选择性加密。  
4. **闭环反馈**：将优化后的高斯体与LiDAR特定的置信度线索反馈至跟踪模块，提升鲁棒性。

### 主要贡献
1. 首个实时LiDAR高斯泼溅SLAM框架，在Newer College数据集上达到86.78% F-score，运行速度超过20 FPS。  
2. 提出利用协方差初始化、几何分数驱动的自适应剪枝/加密策略，以及基于置信度的跟踪增强机制。  
3. 在多个数据集上验证了方法的稳定性和可扩展性。

### 局限性
摘要未提供足够信息。未提及显式局限性，如对动态场景的处理、内存消耗或极端环境中的退化情况等。

### 阅读优先级
**高**  
理由：该方法将高斯泼溅与LiDAR SLAM结合，首次在纯线上轨迹下实现实时高精度建图（F-score 86.78%），对实时3D重建与机器人定位领域具有重要参考价值。摘要中方法创新完整，实验指标明确，适合对该方向感兴趣的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

We present a real-time LiDAR-based framework for Gaussian Splatting SLAM that tightly couples fast G-ICP registration with spherical rasterization-based dense mapping for large-scale sequences. Leveraging LiDAR geometry rather than appearance, we reuse tracking-estimated local covariances to initialize Gaussians with range-aware scales and to derive surface normals for geometry-aware map optimization. We further introduce a covariance-derived geometry score that measures local complexity and drives pruning in planar regions and selective densification in structurally rich areas, while optimized Gaussians and LiDAR-specific confidence cues are fed back to improve tracking robustness. On the Newer College dataset, our method achieves an F-score of 86.78\% using purely online trajectories at real-time speed ($>$20 FPS), and additional experiments on other datasets confirm its stability and scalability.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-09 - DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

**Authors:** Yunchao Yao, Zhuxiu Xu, Tianqi Zhang, Zixian Liu, Sikai Li, Zhenyu Wei, Feng Chen, Dihong Huang, Kechang Wan, Chenyang Ma, Shuqi Zhao, Shenghua Gao, Masayoshi Tomizuka, Yi Ma, Mingyu Ding
**Links:** [abs](https://arxiv.org/abs/2607.08751) - [pdf](https://arxiv.org/pdf/2607.08751)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, VR

<details>
<summary>Abstract</summary>

Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering studies of cross-task and cross-embodiment generalization. We present DexVerse, a large-scale and modular benchmark for dexterous manipulation. DexVerse includes 100 tasks spanning a broad range of manipulation skills, including object grasping and relocation, articulated-object interaction, functional tool use, bimanual coordination, non-prehensile control, contact-rich behaviors, multi-goal execution, and long-horizon multi-stage task completion. It supports 3 robot arms and 6 dexterous hands, and is extensible to new tasks, assets, and embodiments. To evaluate visuomotor generalization, DexVerse provides configurable visual variations in textures, background, lighting, and camera viewpoints. We further provide a VR-based teleoperation interface and 3,180 demonstrations with synchronized proprioceptive, RGB, depth, point-cloud, and state observations. We benchmark representative methods, including Diffusion Policy, DP3, OpenVLA, and $π_{0.5}$, across 19 tasks. Results reveal substantial challenges in task generalization and visuomotor robustness, establishing DexVerse as a promising testbed for general-purpose dexterous manipulation. Project page: https://ycyao216.github.io/DexVerse.site

</details>

#### 2026-07-09 - WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving

**Authors:** Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, Jia Hu, Binyang Song
**Links:** [abs](https://arxiv.org/abs/2607.08375) - [pdf](https://arxiv.org/pdf/2607.08375)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, autonomous driving, world model

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-VLA unifies world cognition and reasoning by incorporating 3D spatial perception and injecting agent tokens to capture the world dynamics, while concurrently enabling Game-theoretic Chain-of-Thought (Game-CoT) reasoning. At the generative level, we introduce the Aligned Decoupled Diffusion Transformer (ADDT) as a powerful generative world model that synthesizes physically-plausible joint multi-agent trajectories. Through scene representation alignment, ADDT reduces the number of denoising steps required and thus significantly accelerates inference. To facilitate strategic reasoning, we further construct a large-scale dataset featuring 85k Game-CoT annotations. Extensive experiments on the NAVSIM benchmark demonstrate that WCog-VLA achieves a State-Of-The-Art (SOTA) PDMS score of 92.9.

</details>

#### 2026-07-08 - CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis

**Authors:** Kaicong Huang, Meng Ma, Ruimin Ke
**Links:** [abs](https://arxiv.org/abs/2607.07601) - [pdf](https://arxiv.org/pdf/2607.07601)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis
- 作者：Kaicong Huang, Meng Ma, Ruimin Ke
- 出版日期：2026-07-08T16:20:19Z（摘要标注日期）
- 分类：Embodied / Robotics / AR Applications（主要分类）
- 链接：https://arxiv.org/abs/2607.07601（PDF: https://arxiv.org/pdf/2607.07601）

### 一句话总结
本文提出CARLA-GS，一个模块化的自动驾驶边缘案例合成框架，通过解耦视觉表示、语义推理与物理执行，并利用多智能体LLM和CARLA仿真器，生成逼真、时空一致且物理可行的极端场景视频。

### 研究问题
如何在统一的框架中生成自动驾驶中的罕见、安全关键型边缘案例（corner cases），同时确保视觉逼真度、时空一致性以及物理运动可行性？现有方法或孤立处理场景/轨迹组件，或端到端生成但难以兼顾一致性。

### 核心思路/方法
提出CARLA-GS模块化流水线，具体包括：
1. **视觉表示**：从真实驾驶数据重建可编辑的3D高斯场景，并增加几何一致性约束。
2. **语义推理**：使用多智能体大语言模型（LLM）进行场景级推理，识别危险交互并生成意图级航点轨迹。
3. **物理执行**：将低层运动控制委托给CARLA仿真器，利用PID控制器确保运动学与动力学可行性。
4. **渲染输出**：将模拟的车辆状态重新投影到高斯场景中，生成以自我为中心的逼真视频。

### 主要贡献
- 提出了一个解耦的模块化管线，统一了视觉表示、语义推理与物理仿真。
- 实现了可控的边缘案例生成，生成视频在逼真度、时空一致性与物理可行性上表现良好（在Waymo Open Dataset上经定量和定性验证）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文针对自动驾驶安全评估中的核心挑战——边缘案例合成，提出了将LLM推理、物理仿真与3D场景重建相结合的创新模块化方案，且在Waymo数据集上验证了效果。对于关注自动驾驶安全验证、仿真生成及多模态融合的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Safety evaluation for autonomous driving is dominated by rare, safety-critical interactions, motivating simulators that can deliberately synthesize corner cases with photorealistic observations. Corner-case generation is inherently a multi-source problem spanning visual representation, scene reasoning, and vehicle trajectory generation and control. Prior knowledge- and model-based approaches typically focus on scene or trajectory components in isolation, while diffusion-based methods attempt end-to-end generation but still struggle to ensure spatiotemporal consistency and physical realism. To unify these aspects within a single framework, we propose CARLA-GS, a modular corner-case synthesis pipeline that decouples visual representation, semantic reasoning, and physics-based execution while maintaining tight cross-module coupling. Starting from real driving data, we reconstruct an editable gaussian scene with additional geometry-consistent constraints. A multi-agent LLM then performs scene-level reasoning to identify risky interactions and generate intent-level waypoint trajectories, while the low-level motion control is delegated to CARLA, where a PID controller ensures kinematic and dynamic feasibility. The simulated vehicle states are finally re-projected into the gaussian scene for ego-centric rendering. This design enables high-level semantic reasoning, low-level physically executable motion, and photorealistic corner-case generation within a unified pipeline. Experiments on the Waymo Open Dataset show, both quantitatively and qualitatively, that our framework enables controllable corner-case generation and produces photorealistic, spatiotemporally consistent videos aligned with semantic intent and physically feasible motion.

</details>

#### 2026-07-08 - HumAIN: Human-Aware Implicit Social Robot Navigation

**Authors:** Daeun Song, Nhat Le, Jeffrey Chen, Mohammad Nazeri, Amirreza Payandeh, Rohan Chandra, Reuth Mirsky, Ross Mead, Ling Xiao, Xuesu Xiao
**Links:** [abs](https://arxiv.org/abs/2607.07357) - [pdf](https://arxiv.org/pdf/2607.07357)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HumAIN: Human-Aware Implicit Social Robot Navigation  
- 作者：Daeun Song, Nhat Le, Jeffrey Chen, Mohammad Nazeri, Amirreza Payandeh, Rohan Chandra, Reuth Mirsky, Ross Mead, Ling Xiao, Xuesu Xiao  
- 出版日期：2026-07-08  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.07357  

### 一句话总结
本文提出一种名为 HumAIN 的社交机器人导航框架，通过知识蒸馏将隐式人体社会线索（如步态、朝向）融入规划环路，实现高效且社会合规的导航。

### 研究问题
如何让机器人在资源受限平台上，利用隐式、全身的人体行为线索（如骨架关键点）进行社会感知的导航规划，同时保持实时性。

### 核心思路/方法
1. **教师模型**：基于Transformer架构，融合多模态输入（历史图像、骨架关键点、机器人状态、目标），学习鲁棒的人体感知轨迹表示。  
2. **学生模型**：通过知识蒸馏，从教师模型中蒸馏出轻量级模型，仅使用最小输入，同时优化轨迹重建和潜在特征对齐，以推断复杂社会动态。  
3. **规划-预测集成**：将隐式社会线索直接嵌入规划循环，弥补预测与规划之间的差距。

### 主要贡献
- 提出HumAIN框架，首次将隐式全身社会线索（如步态、朝向）通过知识蒸馏直接融入机器人导航规划。  
- 通过轻量级蒸馏架构实现实时部署，使资源受限平台也能具备社会感知能力。  
- 实验表明，与最先进基线相比，轨迹预测指标平均提升29.8%。

### 局限性
摘要未提供足够信息：未讨论在极端遮挡、多人密集场景或不同机器人平台上的泛化表现，也未提及计算资源的具体需求或失败案例。

### 阅读优先级
**高**  
理由：该工作直接针对社交机器人导航中的实时性与社会感知矛盾，提出了结合知识蒸馏与多模态隐式线索的实用方案，性能提升显著（29.8%），且主题与当前具身智能与机器人应用趋势紧密相关。摘要逻辑完整，方法新颖，适合对机器人导航、人机交互和知识蒸馏感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

Effective social robot navigation requires sensitivity to human behavior, often revealed through subtle skeletal cues like gait and orientation. We present Human-Aware Implicit Social Robot Navigation (HumAIN), a novel framework that fuses implicit social cues directly into the planning loop via knowledge distillation. We first employ a transformer-based teacher model that fuses rich multi-modal inputs, including historic images, skeletal keypoints, robot state, and a robot's target goal, to learn robust, human-aware representations for the robot's future trajectory planning. To enable real-time deployment, we then distill this knowledge into a lightweight student model. By optimizing for both trajectory reconstruction and latent feature alignment with the teacher, the student learns to infer complex social dynamics from minimal inputs. Bridging the prediction-planning gap with an efficient distilled architecture, our method enables robots to reason about human behavior in a manner that is adaptive, robust, and socially compliant. We validate HumAIN through extensive experiments, where it improves trajectory prediction metrics by an average of 29.8% across all metrics compared to state-of-the-art baselines. These results highlight the benefit of using implicit, whole-body cues to achieve human-like navigation awareness on resource-constrained platforms.

</details>

#### 2026-07-08 - TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation

**Authors:** Jianyi Zhou, Feiyang Hong, Yunhao Li, Yicheng Zhao, Yongjue Cen, Zirui Liu, Jiakang Huang, Zirui Chen, Ruiyang Zhang, Weizhuo Zhu, Xuhua Song, Shuo Yang
**Links:** [abs](https://arxiv.org/abs/2607.07287) - [pdf](https://arxiv.org/pdf/2607.07287)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation
- 作者：Jianyi Zhou, Feiyang Hong, Yunhao Li, Yicheng Zhao, Yongjue Cen, Zirui Liu, Jiakang Huang, Zirui Chen, Ruiyang Zhang, Weizhuo Zhu, Xuhua Song, Shuo Yang
- 出版日期：2026-07-08
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.07287，PDF: https://arxiv.org/pdf/2607.07287

### 一句话总结
TouchWorld 提出一种层次化触觉基础模型，通过分离高层规划、触觉世界模型预测、视觉-触觉目标条件动作生成和触觉残差精化，同时实现触觉的预测性与反应性，显著提升了灵巧操作在无扰动和人为扰动下的成功率。

### 研究问题
现有灵巧操作策略将触觉仅作为低频观测输入，与任务推理、动作生成耦合在单一循环中，导致局部接触错误（如滑动、力不匹配）难以被快速修正。如何让触觉同时提供预测性接触参考和快速反馈信号，以实现语义泛化与局部接触适应的统一？

### 核心思路/方法
- **层次化策略架构**：将操作过程解耦为四个阶段：
  1. **高层规划层**：基于视觉-语言进行子任务规划，并预测触觉子目标。
  2. **视觉-触觉目标条件策略**：生成标称动作块。
  3. **触觉条件精化策略**：利用近期触觉和本体感受反馈进行在线残差修正。
- **触觉双重角色**：触觉既作为预测性参考（世界模型预测），又作为反应性校正信号（高频残差精化），保持视觉-语言-动作策略的语义泛化能力。

### 主要贡献
- 提出 TouchWorld 模型，首次将触觉同时作为预测性参考和反应性反馈，解决灵巧操作中局部接触适应问题。
- 设计层次化策略框架，分离慢速任务推理、动作生成与快速触觉反馈。
- 在6项长时域、高接触的灵巧操作任务中，于无扰动环境达到65.0%成功率，在人为扰动下达到53.7%成功率，分别领先最强基线15.7和18.5个百分点。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文针对灵巧操作中触觉反馈的瓶颈问题，提出了兼具预测性与反应性的层次化架构，在多个复杂任务上取得了显著优于基线的结果（成功率提升超15个百分点），对具身机器人、触觉感知与灵巧操作方向的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-frequency observation stream within a monolithic action model, coupling slow task reasoning, action generation, and fast contact feedback in a single loop. We introduce TouchWorld, a predictive-and-reactive tactile foundation model for dexterous manipulation. TouchWorld uses a hierarchical policy that separates vision-language subtask planning, tactile world-model prediction, visuo-tactile goal-conditioned action generation, and high-frequency tactile residual refinement. A High-Level Planning Layer produces executable subtasks and predicts tactile subgoals; a Visuo-Tactile Goal-Conditioned Policy generates nominal action chunks; and a Tactile-Conditioned Refinement Policy performs online residual correction using recent tactile and proprioceptive feedback. By using touch as both a predictive contact reference and a fast feedback signal, TouchWorld preserves the semantic generalization of vision-language-action policies while improving local contact adaptation. Across six long-horizon and contact-rich dexterous manipulation tasks, TouchWorld achieves 65.0% success in the clean setting and 53.7% success under human perturbations, outperforming the strongest baseline by 15.7 and 18.5 percentage points, respectively.

</details>

#### 2026-07-08 - GeoProp: Grounding Robot State in Vision for Generalist Manipulation

**Authors:** Guoyang Zhao, Quanhao Qian, Gongjie Zhang, Wenhao Li, Jiuniu Wang, Xiaowei Lu, Deli Zhao, Ran Xu
**Links:** [abs](https://arxiv.org/abs/2607.07101) - [pdf](https://arxiv.org/pdf/2607.07101)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoProp: Grounding Robot State in Vision for Generalist Manipulation
- 作者：Guoyang Zhao, Quanhao Qian, Gongjie Zhang, Wenhao Li, Jiuniu Wang, Xiaowei Lu, Deli Zhao, Ran Xu
- 出版日期：2026-07-08
- 分类：具身智能 / 机器人 / AR应用
- 链接：摘要：https://arxiv.org/abs/2607.07101，PDF：https://arxiv.org/pdf/2607.07101

### 一句话总结
GeoProp提出了一种轻量级的即插即用适配器，通过将机器人本体状态显式几何投影到视觉特征图上并采样空间特征，来对齐视觉与本体感觉，从而显著提升通用操作策略的性能。

### 研究问题
机器人操作中，标准的多模态融合方法通常将本体感觉视为独立向量，缺乏与视觉特征的显式对齐。这种3D运动学与2D特征图之间的对应缺失，导致策略难以在场景中“接地”机器人状态，甚至不如纯视觉基线。因此，研究问题是如何有效建立本体感觉与视觉之间的空间对应关系。

### 核心思路/方法
GeoProp通过以下三步实现视觉-本体感觉对齐：
1. **显式几何接地**：将机器人状态（如关节角度）投影到图像平面，在该投影位置采样局部视觉特征，构建一个“接地状态token”。
2. **空间先验注入**：利用FiLM（特征线性调制）机制，将状态导出的空间先验信息注入到对应的视觉特征中。
3. **运动意图捕获**：基于近期运动学预测一个短时间范围内的未来坐标，在该位置额外采样特征，为策略提供前瞻性的视觉上下文。

该方法可作为一个轻量适配器（仅增加2-3%参数量）插入现有策略（如Diffusion Policy和π₀）中。

### 主要贡献
1. 提出了GeoProp，一种即插即用的轻量适配器，通过几何投影和空间特征采样对齐本体感觉与视觉。
2. 在63个仿真任务上，将Diffusion Policy提升8.7%；在RoboTwin子集上，将π₀提升4.0%。
3. 在真实世界实验中，在两个策略族上获得平均10.6%的性能增益。
4. 仅增加2-3%的参数量，即可成为通用具身策略的有效归纳偏置。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对机器人操作中本体感觉-视觉对齐的核心难题，提出了简单有效的几何接地方案，并在大规模任务（67个）和两种主流策略（Diffusion Policy和π₀）上验证了显著提升，同时参数量增加极小，具有高实用性和迁移潜力。适合对具身智能、机器人操作和视觉-运动融合感兴趣的研究者。

</details>

<details>
<summary>Abstract</summary>

Proprioception is fundamental to robotic manipulation, yet standard fusion methods often treat it as an isolated vector lacking explicit alignment with visual tokens. Without a direct correspondence between 3D kinematics and 2D feature maps, manipulation policies struggle to ground the robot's state within the scene, frequently underperforming even vision-only baselines. To address this, we introduce GeoProp, a lightweight, plug-and-play adapter that aligns proprioception with vision through explicit geometric grounding and spatial feature sampling. GeoProp projects the robot state onto the image plane to sample localized visual features, constructing a grounded state token. It then injects state-derived spatial priors into the corresponding visual features via FiLM modulation. To capture motion intent, GeoProp further samples features at a short-horizon predicted coordinate derived from recent kinematics, providing look-ahead visual context. Across 67 tasks, GeoProp improves Diffusion Policy by 8.7% on 63 simulation tasks and pi_0 by 4.0% on the RoboTwin subset, and yields a 10.6% average gain across both policy families in the real world, while adding only 2-3% to the parameter count. These results demonstrate that GeoProp is a simple yet high-impact inductive bias for generalist embodied policies. Project page: https://alibaba-damo-academy.github.io/GeoProp/.

</details>

#### 2026-07-07 - WildCity: A Real-World City-Scale Testbed for Rendering, Simulation, and Spatial Intelligence

**Authors:** Xiangyu Han, Mengyu Yang, Jiaqi Li, Bowen Chang, Ziyu Chen, Hexu Zhao, Rahul Kumar Agrawal, Anthony Rodriguez, Fiona Hua, Marco Pavone, Chen Feng, Yiming Li
**Links:** [abs](https://arxiv.org/abs/2607.06838) - [pdf](https://arxiv.org/pdf/2607.06838)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, rendering, simulation, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WildCity: A Real-World City-Scale Testbed for Rendering, Simulation, and Spatial Intelligence
- 作者：Xiangyu Han, Mengyu Yang, Jiaqi Li, Bowen Chang, Ziyu Chen, Hexu Zhao, Rahul Kumar Agrawal, Anthony Rodriguez, Fiona Hua, Marco Pavone, Chen Feng, Yiming Li
- 出版日期：2026-07-07
- 分类：Embodied / Robotics / AR Applications（主要），Neural Scene Representations & Rendering（次要）
- 链接：arXiv 摘要页 https://arxiv.org/abs/2607.06838

### 一句话总结
WildCity 是一个真实世界城市尺度的多模态数据集，包含18条平均长度83.7公里的轨迹，并配套了城市级重建基线和闭环模拟器，旨在推动城市规模渲染、仿真和空间智能的研究。

### 研究问题
现有场景重建和具身智能方法难以扩展到整个城市尺度，主要原因是缺乏城市规模的真实数据。论文旨在填补这一空白，推动AI在感知、记忆和空间推理方面达到人类认知尺度。

### 核心思路/方法
1. **数据收集**：利用自动驾驶车队在复杂城市环境中采集多模态数据，涵盖18条长轨迹（平均83.7公里），保留动态物体、光照变化和不完美相机位姿等野外感知挑战。
2. **重建基线**：建立面向城市场景的定制化重建基线，将重建环境转换为闭环仿真器。
3. **系统分析**：在通往仿真就绪的城市数字孪生道路上，系统分析可扩展性、外推能力和不确定性等关键挑战。

### 主要贡献
- 发布了首个真实世界城市规模的多模态数据集，轨迹总长达到近百公里级别。
- 提供了针对城市环境定制的重建基线和闭环仿真器。
- 系统性地揭示了城市级场景理解与仿真面临的核心挑战（可扩展性、外推、不确定性）。

### 局限性
摘要未提供实验细节，无法评估基线方法性能、数据多样性或仿真器逼真度。具体局限性（如数据覆盖城市类型、轨迹密度、标注情况等）摘要未提及。

### 阅读优先级
**高**  
理由：该工作针对城市规模三维重建与仿真的数据稀缺问题，提供了大规模真实数据集和配套基线，对神经渲染、具身智能、数字孪生等方向有重要推动作用。

</details>

<details>
<summary>Abstract</summary>

Humans can navigate an unfamiliar city and gradually form a coherent spatial mental map spanning tens of square kilometers. Can AI build spatial representations at a comparable scale? Although recent foundation models have advanced scene reconstruction and embodied intelligence, scaling to entire cities remains an open challenge, primarily due to the lack of city-scale data. To bridge the gap, we introduce WildCity, a real-world multimodal dataset collected by autonomous fleets traversing complex urban environments. Our dataset includes 18 trajectories, each averaging 83.7 kilometers in length, and preserves the core challenges of in-the-wild perception, e.g., dynamic objects, lighting variations, and imperfect camera poses. We further establish an urban-tailored reconstruction baseline and convert the reconstructed environments into a closed-loop simulator. Beyond the dataset and baseline, we systematically analyze the key challenges on the path to simulation-ready urban digital twins: scalability, extrapolation, and uncertainty. Ultimately, WildCity aims to catalyze progress not only in city-scale rendering, but more broadly in the pursuit of AI that can perceive, remember, and reason across space at a scale comparable to human cognition. Project page: https://han-xiangyu.github.io/Wild-City/

</details>

#### 2026-07-07 - RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation

**Authors:** Haoyu Zhao, Xingyue Zhao, Siteng Huang, Xin Li, Deli Zhao, Zhongyu Li
**Links:** [abs](https://arxiv.org/abs/2607.06559) - [pdf](https://arxiv.org/pdf/2607.06559)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation
- 作者：Haoyu Zhao, Xingyue Zhao, Siteng Huang, Xin Li, Deli Zhao, Zhongyu Li
- 出版日期：2026-07-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.06559

### 一句话总结
提出一个名为 RynnWorld-4D 的生成式世界模型，能够从单张RGB-D图像和语言指令联合预测未来的RGB帧、深度图与光流，并基于其内部表征实现闭环机器人操作策略。

### 研究问题
如何构建4D世界模型，使机器人能够预测场景在交互下的3D结构运动，并生成与机器人低级末端执行器动作更匹配的表征，从而缩小世界预测与策略学习之间的差距。

### 核心思路/方法
- 核心表征：联合使用RGB、深度和光流（RGB-DF）作为物理基础表征，以捕捉场景的4D动态（外观、几何与运动）。
- 模型架构：采用三分支架构的生成式扩散模型，整合跨模态注意力与帧级3D旋转位置编码（3D RoPE），在统一扩散过程中联合生成未来的RGB帧、深度图和光流。
- 训练数据：构建大规模数据集 Rynn4DDataset 1.0，包含超过2.544亿帧的自我中心人类和机器人操作视频，并通过伪标签获取深度和光流标注。
- 策略集成：提出 RynnWorld-4D-Policy，一个逆动力学头，通过单次前向传播直接消费模型内部4D表征，避免多步去噪计算，实现闭环动作输出。

### 主要贡献
1. 提出RGB-DF联合表征，将视觉外观、几何结构和时间运动对齐，降低世界预测与策略学习之间的差距。
2. 构建RynnWorld-4D生成模型，支持从单张RGB-D图像和语言指令联合预测多模态未来帧。
3. 发布大规模数据集Rynn4DDataset 1.0，为4D世界模型训练提供高质量伪标签数据。
4. 提出RynnWorld-4D-Policy，在真实世界灵巧双手操作任务上达到最新性能，尤其在需空间精度和时间协调的任务中表现突出。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该工作聚焦于机器人操作中的4D世界模型构建，方法创新（RGB-DF联合表征、三分支扩散架构）且实验表现优异（真实任务SOTA），但摘要未披露细节如模型参数、消融实验或与其他方法的定量对比，作为论文分析尚可，但并不迫切适用于非机器人的视觉任务。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation in the open world requires not only recognizing what a scene looks like, but also anticipating how its 3D structure moves under interaction. We argue that synchronized RGB, depth, and optical flow, namely RGB-DF, provide a physically grounded representation that captures the underlying 4D dynamics of a scene. Compared to 2D pixel videos, this multi-modal synergy aligns visual appearance with geometric structure and temporal motion, creating a representation space significantly closer to the low-level end-effector actions demanded by robotic systems, thereby narrowing the gap between world prediction and policy learning. Building on this insight, we introduce RynnWorld-4D, a generative model that co-produces future RGB frames, depth maps, and optical flow from a single RGB-D image and a language instruction within one unified diffusion process. This 4D world model features a tri-branch architecture that integrates cross-modal attention with frame-wise 3D RoPE, ensuring that appearance, geometry, and motion evolve consistently. To supply training data at scale, we curate Rynn4DDataset 1.0, a massive dataset of over 254.4 million frames across egocentric human and robotic manipulation videos with high-quality pseudo-labels for depth and optical flow. We further propose RynnWorld-4D-Policy, an inverse dynamics head that consumes the internal 4D representations of RynnWorld-4D in a single forward pass, bypassing expensive multi-step denoising, to output robot actions in a closed-loop manner. Experiments show that RynnWorld-4D produces temporally and spatially coherent 4D predictions, and that RynnWorld-4D-Policy achieves state-of-the-art performance on real-world dexterous bimanual manipulation tasks, particularly excelling in tasks demanding spatial precision and temporal coordination.

</details>

#### 2026-07-07 - CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models

**Authors:** He Liang, Chenyang Ma, Yiming Zhang, Sangyun Shin, Andrew Markham, Niki Trigoni, Yuhang He
**Links:** [abs](https://arxiv.org/abs/2607.06534) - [pdf](https://arxiv.org/pdf/2607.06534)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models
- 作者：He Liang, Chenyang Ma, Yiming Zhang, Sangyun Shin, Andrew Markham, Niki Trigoni, Yuhang He
- 出版日期：2026-07-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.06534

### 一句话总结
CAIRN 是一个能感知房间拓扑结构的大语言模型，用于对包含多个相连房间的3D场景进行理解、推理和问答。

### 研究问题
现有3D场景基础大语言模型（3D-LLMs）仅限于简化单房间场景，无法处理真实家庭环境中多房间互联、物体种类多样的情况。本研究旨在解决跨房间3D场景理解问题。

### 核心思路/方法
- 将对场景层次结构的感知融入Transformer注意力机制，使模型显式感知物体层面的关系和房间层面的连通性。
- 通过图神经网络增强物体令牌，融入房间内的局部关系上下文；引入可学习的房间令牌实现房间级抽象。
- 应用带有几何偏置的分层注意力掩码，根据场景拓扑结构路由信息。
- 同时引入了新基准CAIRN-MR（基于HM3D数据集），用于评估多房间3D场景理解，包含指代定位、字幕生成和四种问答任务。

### 主要贡献
1. 提出了CAIRN，首个具备拓扑感知能力的跨房间3D场景理解大语言模型。
2. 构建了CAIRN-MR基准，覆盖从室内感知到跨房间推理的多种任务。
3. 实验表明，CAIRN在CAIRN-MR全部任务上大幅优于先前3D-LLMs，并在五个单房间基准上保持竞争力。

### 局限性
摘要未提供足够信息。摘要未提及模型的计算开销、对复杂拓扑结构的鲁棒性、在真实机器人平台上的部署情况，或跨房间场景在异构布局下的泛化能力。

### 阅读优先级
**高**
理由：该论文针对多房间3D场景理解这一实际但研究不足的挑战，提出了新模型和新基准，且在多项任务上取得显著提升。对于从事具身智能、机器人导航或3D视觉语言理解的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing 3D scene-grounded Large Language Models (3D-LLMs) focus on answering questions grounded in simplified single-room 3D scenes, lacking the ability to reason over real-world household environments containing multiple interconnected rooms and diverse object categories. We introduce CAIRN, a topology-aware 3D-LLM for multi-room 3D scene understanding. CAIRN aligns transformer attention with scene hierarchy, giving the model explicit awareness of object-level relations and room-level connectivity. It enriches object tokens with room-local relational context via a graph neural network, introduces learned room tokens for room-level abstraction, and applies a hierarchical attention mask with geometric bias to route information according to scene topology. CAIRN is developed on CAIRN-MR, a benchmark we introduce on HM3D for multi-room 3D scene understanding, covering grounding, captioning, and four question-answering tasks that progressively evaluate from intra-room perception to cross-room reasoning. Experiments show that CAIRN outperforms prior 3D-LLMs by a large margin across all CAIRN-MR tasks while remaining competitive on five single-room benchmarks.

</details>

#### 2026-07-07 - Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation

**Authors:** Songbur Wong, Xiaosong Jia, Junqi You, Bo Zhang, Pei Xu, Renqiu Xia, Yuping Qiu, Shaofeng Zhang, Zelin Zhao, Xuechao Yan, Yuchen Zhou, Yurui Chen, Wen Guo, Hang Xu, Junchi Yan
**Links:** [abs](https://arxiv.org/abs/2607.06516) - [pdf](https://arxiv.org/pdf/2607.06516)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation
- 作者：Songbur Wong, Xiaosong Jia, Junqi You, Bo Zhang, Pei Xu, Renqiu Xia, Yuping Qiu, Shaofeng Zhang, Zelin Zhao, Xuechao Yan, Yuchen Zhou, Yurui Chen, Wen Guo, Hang Xu, Junchi Yan
- 出版日期：2026-07-07
- 分类：具身智能/机器人/AR应用
- 链接：[摘要](https://arxiv.org/abs/2607.06516) | [PDF](https://arxiv.org/pdf/2607.06516)

### 一句话总结
本文提出一种基于累积点云骨架的自回归生成框架，用于在闭环驾驶仿真中生成视觉逼真且状态可更新的驾驶视频。

### 研究问题
如何同时提升闭环自动驾驶仿真的交互性（如CARLA）和真实世界视觉保真度（如nuScenes），并解决自回归滚动生成过程中的误差积累。

### 核心思路/方法
1. 提出“点云骨架”（Point as Skeleton）作为条件输入，将前景和背景资产解耦，并投影到相机视角的涂色点和模板深度条件中，提供外观和几何线索。
2. 设计“Reset-and-Roll”机制，将滚动扩散推理适配到仿真中，防止未来条件潜伏状态跨仿真步骤提交。
3. 构建基于nuPlan的渲染级闭环生成接口，用于评估自车偏离原日志轨迹时的生成质量。
4. 使用自回归生成器，根据逐步更新的自车状态、参与者状态、场景地图和点云骨架条件，合成视觉观测。

### 主要贡献
1. 提出一种生成式传感器仿真框架，结合点云骨架和自回归生成，实现状态更新的闭环驾驶视频生成。
2. 通过“点云骨架”解耦前后景，稳定自回归滚动过程中的误差累积。
3. 在nuScenes和nuPlan数据集上的实验表明，该方法提升了闭环滚动过程中自回归生成的质量。

### 局限性
摘要未提供关于计算开销、实时性、对不同天气/光照条件的鲁棒性、或与现有方法相比的详细量化对比等信息。实验细节仅提及在nuScenes和nuPlan上评估，未提供具体指标值。

### 阅读优先级
高。
理由：该工作针对闭环自动驾驶仿真中交互性与视觉保真度的矛盾，提出了新颖的点云骨架条件和Reset-and-Roll机制，对于从事生成式仿真、端到端自动驾驶评测的研究人员具有较高参考价值。同时提供了代码开源链接，便于复现。

</details>

<details>
<summary>Abstract</summary>

Evaluating end-to-end autonomous driving (E2E-AD) remains challenging, as existing driving simulation methods often trade off closed-loop interactivity (e.g., CARLA) and real-world visual fidelity (e.g., nuScenes). We present \textbf{\emph{Point as Skeleton}}, a generative sensor simulation framework for state-updated autoregressive driving video generation, in which an autoregressive generator synthesizes visual observations from step-wise updated ego states, actor states, scene maps, and point-cloud skeleton conditions. To support closed-loop rollout, we introduce Reset-and-Roll, which adapts rolling diffusion inference to simulation by preventing future-conditioned latent states from being committed across simulation steps. To stabilize error accumulation during step-wise autoregressive rollout, we introduce point-cloud skeletons that decouple foreground and background assets and project them into camera-view painted-point and template-depth conditions, providing appearance and geometric cues. We further implement a nuPlan-based renderer-level closed-loop generative interface for evaluating generation under ego deviations from the original log. Experiments on nuScenes and nuPlan show that \textit{Point as Skeleton} improves autoregressive generation quality during closed-loop rollout, demonstrating its potential for visually faithful closed-loop driving simulation. The code is available at https://github.com/krauwu/point-as-skeleton.

</details>

#### 2026-07-07 - OrchardBench: A Physically-Grounded, GPU-Parallel Apple-Orchard Simulation Benchmark for Agricultural Robotics

**Authors:** Humphrey Munn
**Links:** [abs](https://arxiv.org/abs/2607.06337) - [pdf](https://arxiv.org/pdf/2607.06337)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OrchardBench: A Physically-Grounded, GPU-Parallel Apple-Orchard Simulation Benchmark for Agricultural Robotics  
- 作者：Humphrey Munn  
- 出版日期：2026-07-07  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.06337  

### 一句话总结
OrchardBench 是一个基于物理的、GPU 并行的苹果园仿真基准，用于农业机器人研究，通过模拟真实树木的生物学和力学特性，支持可重复的田野实验。

### 研究问题
农业机器人中的树果采摘研究受限于田野实验的高成本、不可重复性（如果园仅在特定季节可用、每棵树不同、控制错误可能造成永久损害）。现有仿真要么缺乏物理交互性，要么缺乏合理的树木模型，导致算法验证困难。

### 核心思路/方法
- 使用随机 L-system 生长树木，并实例化为全刚体系统。  
- 树枝建模为符合欧拉-伯努利梁理论的扭转弹簧-阻尼器，可断裂后成为自由铰链。  
- 苹果通过茎绳独立连接，拉力达到文献基础时脱落，拉动时对树枝施加载荷。  
- 可移动的、密度可控的叶片层模拟真实遮挡效果。  
- 所有物理参数均基于已发表文献。  
- 引入环境域随机化，每个批次世界均为不同的树。  
- 使用腕部深度相机的移动机械手闭环实现几何果实感知和自主采摘基线。  
- 通过求解器和模型的精细工程，可在笔记本电脑 GPU 上以交互速率运行多个并行环境。

### 主要贡献
- 提出了一个可交互、可并行的苹果园物理仿真基准，填补了现有仿真在农业机器人领域的空白。  
- 定义了覆盖采摘完整性、吞吐量和植物损伤（含冠层区域细分）的指标集及任务。  
- 提供了包含叶片、果实负载、地形、冠层区域和并行性的基线结果，显示基线方法仅成功采摘约40%的检测果实、收获约1/8的可达果实，为算法改进留出空间。

### 局限性
- 摘要未提供实验的具体统计结果（如不同环境参数下的具体性能差异）、与其他基线方法的定量比较细节。  
- 未讨论仿真与实际田野环境之间的差距（sim-to-real gap）。  
- 未提及系统的运行时间下限或极端情况下的性能限制。

### 阅读优先级
**高**  
理由：该工作提出了一个新颖的、专门针对农业机器人采摘的物理仿真基准，解决了当前该领域缺乏可重复、低成本实验平台的关键瓶颈。基线结果显示当前方法仍有显著改进空间，对从事农业自动化、机器人操作和物理仿真的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Robotic tree-fruit harvesting is a flagship problem for agricultural automation, but progress is bottlenecked by the cost and irreproducibility of field experiments: an orchard is available only weeks a year, every tree is different, and a control error can permanently damage the crop or the plant. The tree models used in graphics and agronomy are geometrically detailed but physically inert, while the GPU-parallel simulators used in robot learning contain no plausible trees. We present OrchardBench, a physically-grounded, GPU-parallel simulation of apple-orchard trees on the Newton engine. Each tree is grown by a stochastic L-system and instantiated as a fully articulated body: branches are compliant torsional spring-dampers whose stiffness follows Euler-Bernoulli beam theory, they break at a wood modulus of rupture and fall as free hinges, and apples are independent bodies on stem tethers that detach at literature-grounded pull forces and load the branch when pulled. A moving, density-controllable foliage layer occludes the canopy as real leaves do. Every physical parameter is tied to a published source. Per-environment domain randomization makes each batched world a distinct tree, and a mobile manipulator with a wrist depth camera closes the loop with geometric fruit perception and an autonomous harvesting baseline. Careful engineering of the solver and the model lets OrchardBench run many parallel environments at interactive rates on a laptop GPU. We define the tasks and a metric suite spanning harvest completeness, throughput, and plant damage (with a per-canopy-zone breakdown), and report baseline results across foliage, fruit load, terrain, canopy zone, and parallelism. The analytic baseline succeeds on about 40% of the fruit it detects and harvests only about an eighth of the reachable fruit on a tree, leaving clear headroom for novel autonomy approaches.

</details>

#### 2026-07-07 - APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment

**Authors:** Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung
**Links:** [abs](https://arxiv.org/abs/2607.06222) - [pdf](https://arxiv.org/pdf/2607.06222)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment
- 作者：Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung
- 出版日期：2026-07-07
- 分类：Embodied / Robotics / AR Applications (主要)；3D Reconstruction & Multi-view Geometry (次要)
- 链接：摘要：https://arxiv.org/abs/2607.06222；PDF：https://arxiv.org/pdf/2607.06222

### 一句话总结
APVI-SLAM是一个能够在水下视觉失效时，通过声学/压力传感器可靠性重加权和滑动窗口冻结策略实现鲁棒定位，并结合四叉树引导的3D高斯映射进行实时逼真重建的多传感器融合SLAM系统。

### 研究问题
如何在水下复杂环境中，解决视觉惯性SLAM因特征退化和估计器发散导致的定位问题，并在间歇性视觉失效条件下实现鲁棒的实时多传感器融合定位与高保真度地图重建。

### 核心思路/方法
1. **可靠性感知定位框架**：引入动态重加权机制，根据传感器（DVL、压力计等）的可靠性调整估计器权重；采用滑动窗口冻结策略，从跟踪失败中恢复，增强系统鲁棒性。
2. **四叉树引导的增量映射模块**：高效管理场景重建过程，实现增量式水下介质建模和3D高斯优化，以生成逼真的地图。
3. **数据集贡献**：提供一个带有同步多模态数据的珊瑚礁调查数据集，用于水下重建评估的基准测试。

### 主要贡献
- 提出了APVI-SLAM系统，在复杂水下环境中实现了实时、高精度的定位与逼真地图重建。
- 设计了可靠性感知定位框架和滑动窗口冻结策略，显著提升了视觉失效时的系统鲁棒性。
- 开发了基于四叉树的增量映射模块，支持高效水下介质建模和3D高斯优化。
- 贡献了首个用于水下重建评估的同步多模态珊瑚礁数据集。

### 局限性
摘要未提供具体局限性。摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该工作专注于水下SLAM的工程解决方案，涉及多传感器融合、鲁棒定位和重建。若您关注水下/退化环境下的SLAM系统设计、多模态传感器可靠性融合或实时逼真重建，建议阅读；若您更关注纯视觉SLAM或通用SLAM理论，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Extreme subsea environments often cause severe feature de-gradation and estimator divergence in underwater visual-inertial SLAM. Although sensors like Doppler Velocity Logs (DVL) and pressure gauges provide auxiliary constraints, robust multi-sensor fusion during intermittent visual failure remains challenging. To address this, we present APVI-SLAM, a real-time multi-sensor fusion SLAM system that achieves both accurate underwater localization and photorealistic mapping. Our approach introduces a reliability-aware localization framework that dynamically reweights sensor estimators and employs a sliding-window freezing strategy to recover from tracking failures, substantially enhancing system robustness. Furthermore, for high-fidelity scenes reconstruction, we propose an efficient quadtree-guided mapping module that facilitates incremental water-medium modeling and 3D Gaussian optimization. Recognizing the lack of benchmark for underwater mapping evaluation, we also contribute a coral reef surveying dataset with synchronized multi-modality data. Extensive experiments on public and our proposed benchmarks demonstrate that APVI-SLAM achieves state-of-the-art localization and reconstruction quality at real-time speeds.

</details>

#### 2026-07-06 - Harnessing Generative Image Models for Training-Free Primitive Shape Abstraction

**Authors:** Gregor Kobsik, Tim Elsner, Leif Kobbelt
**Links:** [abs](https://arxiv.org/abs/2607.05568) - [pdf](https://arxiv.org/pdf/2607.05568)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, simulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Harnessing Generative Image Models for Training-Free Primitive Shape Abstraction
- 作者：Gregor Kobsik, Tim Elsner, Leif Kobbelt
- 出版日期：2026-07-06
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.05568

### 一句话总结
本文提出一种无需额外训练的方法，通过直接利用预训练的生成式图像模型和视觉语言模型，将3D物体抽象为紧凑的几何基元（超二次曲面）。

### 研究问题
如何在不进行任务特定微调的情况下，利用预训练的生成式图像模型实现无类别、无方向的3D形状基元抽象？

### 核心思路/方法
1. **多视图渲染**：对3D物体渲染多视角图像。
2. **语义分析**：使用视觉语言模型分析渲染图像中的语义部件。
3. **分割掩码生成**：利用生成式图像模型为每个部件生成彩色编码的分割掩码。
4. **几何重投影**：将2D分割掩码重投影回3D几何表面。
5. **基元拟合**：通过参数优化为每个部件拟合超二次曲面基元。
整个流程不含任何学习参数，完全依赖预训练模型的零样本能力。

### 主要贡献
1. 提出首个无需训练的基元抽象方法，消除了对任务特定数据和微调的依赖。
2. 方法具有类别无关性和方向不变性，克服了先前基于学习方法的局限性。
3. 在HumanPrim和Toys4K数据集上，以每对象平均5-9个基元的紧凑性，取得了所有评估方法中最低的Chamfer距离。
4. 通过真值分割实验揭示：当前精度瓶颈在于部件分割，而非基元拟合，且性能可随生成式模型进步自动提升。

### 局限性
摘要未提供方法的失败案例、计算效率分析或对复杂拓扑的适应能力等局限性信息。

### 阅读优先级
中
- 理由：该方法在基元抽象任务上展现出无需训练的优势，并在两个基准上取得最优结果，对机器人、仿真等领域的3D形状理解有参考价值。但方法依赖现有生成式模型的成熟度，且摘要未提供与更多传统方法的比较细节或鲁棒性分析，适合对无训练方法感兴趣的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Representing 3D shapes as compact sets of geometric primitives is fundamental to robotics, simulation, and scene understanding. Generative image models trained at scale have recently emerged as generalist visual learners that can identify and segment object parts directly in the image domain, across arbitrary categories and without task-specific training. Adapting such models to downstream tasks typically requires fine-tuning; we ask whether their pretrained capability can instead be harnessed directly, without any training, and answer affirmatively with a training-free harness. Our pipeline renders multi-view images of a 3D object, uses a vision-language model to analyze its semantic parts, prompts a generative image model to paint a color-coded part segmentation mask, reprojects it onto the geometry, and fits a superquadric primitive to each part via parameter optimization. The approach contains no learned parameters: it is category-agnostic and orientation-invariant, properties that previous learning-based models struggled with. Its accuracy ceiling rises with future generative-model improvements, which we confirm with a ground-truth segmentation study showing that part segmentation, not primitive fitting, is the current accuracy bottleneck. On HumanPrim and Toys4K, our method achieves the lowest Chamfer distance among all evaluated methods, using 5--9 primitives per object on average.

</details>

#### 2026-07-06 - Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis

**Authors:** Xianhao Chen, Jiarui Hu, Yuanbo Yang, Xiyu Zhang, Tengyue Wang, Hujun Bao, Guofeng Zhang, Zhaopeng Cui
**Links:** [abs](https://arxiv.org/abs/2607.05348) - [pdf](https://arxiv.org/pdf/2607.05348)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis
- 作者：Xianhao Chen, Jiarui Hu, Yuanbo Yang, Xiyu Zhang, Tengyue Wang, Hujun Bao, Guofeng Zhang, Zhaopeng Cui
- 出版日期：2026-07-06 (UTC)
- 分类：具身/机器人/AR应用 (Embodied / Robotics / AR Applications)
- 链接：https://arxiv.org/abs/2607.05348

### 一句话总结
本文提出 RelGraphOV，一种利用 3D 场景图关系推理来增强开放词汇 3D 场景理解的方法，通过自适应门控双流图神经网络融合几何与语义特征，并在多个基准上展示了泛化能力。

### 研究问题
现有开放词汇 3D 场景理解方法通常只依赖上下文无关的语义特征，忽略了物体间的关系信息，导致缺乏场景级别的上下文语义细化。如何利用物体关系提升模型对开放词汇场景的理解能力是核心问题。

### 核心思路/方法
1. **构建关系场景图**：利用视觉-语言推理从多视角观测中推断物体关系，并剪除几何上不合理的关系边，整个过程无需人工关系标注。
2. **自适应门控双流上下文图注意力网络 (Adaptive Gated Dual-Stream Contextual GAT)**：该网络将密集几何特征与语义 CLIP 嵌入分开处理，进行边引导的消息传递，然后通过门控机制自适应地融合互补语义信息，避免特征干扰。
3. **层次化对比学习目标**：设计对比学习损失，同时促进实例级别的一致性（同一物体不同视图）和类别级别的区分性（不同类别物体）。

### 主要贡献
1. 提出 RelGraphOV，一种结合 3D 场景图分析的关系感知开放词汇场景理解框架。
2. 引入无需人工标注的自动化关系场景图构建流程，并设计专门的特征聚合与融合策略（自适应门控双流 GAT）来利用关系上下文。
3. 提出层次化对比学习目标，兼顾实例一致性和类别区分性。
4. 在 ScanNetV2、ScanNet200、ScanNet$++$ 和 Replica 数据集上验证了强性能和泛化能力。

### 局限性
摘要中未提供关于模型计算复杂度、推理速度、在遮挡或动态场景下的表现、具体失败案例分析或对关系标注噪声的敏感性等信息。因此无法补充实验细节。

### 阅读优先级
- 中
- 理由：该工作针对开放词汇 3D 场景理解这一前沿任务，创新性地结合了场景图关系与开放词汇学习，并设计了专门的特征融合架构，方法具有启发性。但对机器人、AR应用领域之外的研究者而言，其直接相关性有限；且摘要未提供具体的性能数值对比，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Open-vocabulary 3D scene understanding aims to segment 3D scenes beyond predefined categories by transferring semantic knowledge from vision-language models. Existing methods have advanced this task by lifting language-aligned 2D features into 3D, yet they often rely on context-independent semantic representations, leaving object relationships underexplored for contextual refinement. We propose RelGraphOV, a relationship-aware framework that uses 3D scene graphs to enhance open-vocabulary 3D understanding. Our method constructs relational scene graphs from multi-view observations by leveraging vision-language reasoning to infer object relationships and prune geometrically implausible connections, without manual relationship annotations. To aggregate relational context while avoiding feature interference, we introduce an Adaptive Gated Dual-Stream Contextual GAT that separates dense geometric features and semantic CLIP embeddings, performs edge-guided message passing, and adaptively fuses complementary semantics. A hierarchical contrastive objective further promotes instance-level consistency and category-level discrimination. Experiments on ScanNetV2, ScanNet200, ScanNet$++$, and Replica demonstrate strong performance and generalization ability. Project Page: https://cxavireh.github.io/relgraphov-projectpage

</details>

#### 2026-07-06 - Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation

**Authors:** Zhe Zhao, Zhibin Li, Yilin Ou, Mengshi Qi
**Links:** [abs](https://arxiv.org/abs/2607.04940) - [pdf](https://arxiv.org/pdf/2607.04940)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation
- 作者：Zhe Zhao, Zhibin Li, Yilin Ou, Mengshi Qi
- 出版日期：2026-07-06
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.04940

### 一句话总结
本文提出一种基于仿真到现实（sim-to-real）的强化学习方法，无需真实硬件微调即可零样本部署至五指灵巧手，实现可控抓握力跟踪和物体重新定向操作。

### 研究问题
如何克服灵巧手在接触动力学和驱动不完美等方面的现实差距，使完全在仿真中训练的控制策略能够零样本部署到真实硬件上，并完成力控抓取和操作任务。

### 核心思路/方法
1. **仿真环境与观测设计**：结合密集触觉反馈和关节力矩传感，通过并行正向运动学快速计算虚拟触觉单元与物体间的距离，提供高频率、高分辨率的触觉信号。
2. **电流-力矩校准**：利用电机电流映射关节力矩，避免在灵巧手上额外安装力矩传感器。
3. **执行器动力学建模与随机化**：建模执行器非理想力矩-速度效应，并通过随机化弥合驱动差距。
4. **训练与部署**：采用非对称演员-评论家PPO（Asymmetric Actor-Critic PPO）管线，在仿真中训策略后直接部署至五指机器人手，展示可控抓握力跟踪和物体重新定向。

### 主要贡献
- 提出结合触觉和力矩观测输入（通过可扩展的传感仿真和驱动建模）的sim-to-real框架，首次实现在多指灵巧手上完全由仿真训练、零样本迁移到硬件并执行可控抓握和重新定向。
- 引入快速触觉仿真方法（基于并行正向运动学的距离计算）和电流-力矩校准技术，简化了真实部署所需的硬件需求。
- 实验证明，策略无需额外微调即可鲁棒执行两种类人操作技能：基于指令的可控抓握力跟踪和手持物体重新定向。

### 局限性
摘要未提供足够信息：具体实验设置（如触觉传感器的具体类型、物体种类与数量）、成功率、迁移中出现的失败案例、计算效率对比、与基线方法的量化对比等细节均未提及。

### 阅读优先级
高  
理由：本文针对灵巧手零样本部署这一机器人操作领域的核心难题，提出了实用且系统的方法（触觉仿真、电流-力矩校准、执行器建模），且声称首次在仿真训练后成功迁移至真实硬件。对从事灵巧操作、sim-to-real迁移或强化学习在机器人应用的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

</details>

#### 2026-07-06 - TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving

**Authors:** Miguel Antunes-García, Santiago Montiel-Marín, Fabio Sánchez-García, Rodrigo Gutiérrez-Moreno, Rafael Barea, Luis M. Bergasa
**Links:** [abs](https://arxiv.org/abs/2607.04812) - [pdf](https://arxiv.org/pdf/2607.04812)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving
- 作者：Miguel Antunes-García, Santiago Montiel-Marín, Fabio Sánchez-García, Rodrigo Gutiérrez-Moreno, Rafael Barea, Luis M. Bergasa
- 出版日期：2026-07-06
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.04812

### 一句话总结
本文提出TGRIP框架，通过教师-学生结构和视觉-语言基础模型，将语义先验注入鸟瞰视角（BEV）实例预测任务，在nuScenes数据集上超越了现有最先进模型。

### 研究问题
现有BEV端到端实例预测方法主要依赖几何监督（如占位回归和光流），将场景中的智能体视为通用移动障碍，缺乏显式语义意识，导致在复杂场景（如超车、交叉口）中难以解决歧义。

### 核心思路/方法
提出教师-学生流水线：教师模型利用视觉-语言基础模型从多摄像头图像生成稠密、语义增强的BEV地图；这些地图作为辅助监督信号指导学生网络训练，使其学习兼具几何一致性和语义判别性的时空表征。

### 主要贡献
1. 首次将语义引导与未来的实例预测时间任务统一起来。
2. 提出TGRIP框架，通过注入丰富的语义先验提升实例预测性能。
3. 在nuScenes数据集上验证了语义增强对鲁棒端到端运动预测的重要性。

### 局限性
摘要未提供实验局限性或失败案例分析。

### 阅读优先级
**高**。理由：该工作首次将语义引导与未来实例预测结合，在nuScenes数据集上超越当前最先进模型，且提供了开源代码，对自动驾驶感知领域的语义-几何融合研究具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Bird's-Eye View (BEV) end-to-end instance prediction has emerged as a robust paradigm for autonomous driving perception, effectively mitigating the error propagation inherent in traditional modular pipelines. However, current state-of-the-art approaches rely predominantly on geometric supervision, such as occupancy regression and optical flow, effectively treating scene agents as generic moving obstacles. This absence of explicit semantic awareness imposes limitations on the capacity of the model to solve ambiguities in complex scenarios, particularly those where object-specific behavior is essential for accurate forecasting (e.g. overtaking, intersections). In this paper, we introduce Text-Guided Representation for Instance Prediction (TGRIP), a novel framework that bridges this gap by injecting rich semantic priors into the instance prediction loop. The proposed teacher-student pipeline employs Vision-Language Foundation Models to generate dense, semantic-enhanced BEV maps from multi-camera images. These maps serve as auxiliary supervision during training, guiding the network to learn spatio-temporal representations that are not only geometrically consistent but also semantically discriminative. To the best of our knowledge, this represents the first attempt to unify semantic guidance with the temporal task of future instance prediction. The experimental results demonstrate that TGRIP surpasses existing state-of-the-art models in nuScenes, validating the hypothesis that semantic enrichment is a fundamental element for robust, end-to-end motion prediction. Code is available on https://github.com/miguelag99/TGRIP.

</details>

#### 2026-07-06 - A Reliable Context-Aware and Temporal Planning Framework for Autonomous Driving

**Authors:** Argho Dey, Yunfei Yin, Swachha Ray, Md Minhazul Islam, Zheng Yuan, Sijing Xiong, Hongyu Liu, Zhiqiu Huang
**Links:** [abs](https://arxiv.org/abs/2607.04689) - [pdf](https://arxiv.org/pdf/2607.04689)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Reliable Context-Aware and Temporal Planning Framework for Autonomous Driving
- 作者：Argho Dey, Yunfei Yin, Swachha Ray, Md Minhazul Islam, Zheng Yuan, Sijing Xiong, Hongyu Liu, Zhiqiu Huang
- 出版日期：2026-07-06
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2607.04689，PDF：https://arxiv.org/pdf/2607.04689

### 一句话总结
本文提出一种名为RCT-AD的自动驾驶规划框架，通过显式建模每帧感知特征的质量和时序一致性，在传感器退化（如遮挡、模糊）条件下提升轨迹规划的鲁棒性和安全性。

### 研究问题
在密集城市交通中，车载摄像头观测常因遮挡、运动模糊、光照变化和传感器噪声而退化，若不加区分地聚合降质观测，会导致轨迹规划不稳定，增加自车与周围道路使用者的碰撞风险。

### 核心思路/方法
1. **可靠上下文感知模块**：为每帧特征计算可靠性分数，通过质量门控的先进先出（FILO）记忆机制，选择性保留可信特征，利用可靠历史上下文重建退化观测，避免损坏输入破坏场景表示。
2. **时序轨迹规划器**：捕捉长期依赖和多智能体交互，生成更平滑且安全感知的轨迹。
3. **联合检测-分割头**：将语义和运动线索注入共享的鸟瞰图（BEV）空间，增强场景理解。

### 主要贡献
- 提出RCT-AD框架，在感知退化时仍能维持规划稳定性。
- 设计了基于质量门控的FILO记忆机制，选择性利用可靠历史上下文。
- 在nuScenes基准上，与近期端到端基线相比，提升了感知精度（61.5 NDS、52.9 mAP、52.3 mIoU）、运动预测和规划鲁棒性，同时保持适合实时部署的计算效率。

### 局限性
摘要未提供足够信息：未讨论该方法在极端退化场景（如完全无观测）下的表现，也未分析其在不同传感器配置或硬件平台上的泛化性。

### 阅读优先级
**高**  
理由：该工作直接针对自动驾驶中常见但关键的问题——感知退化下的规划可靠性，提出了新颖的显式质量建模机制，且在主流基准上取得了明确的性能提升。对于从事端到端自动驾驶、鲁棒规划或BEV感知的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Safe operation of autonomous vehicles in dense urban traffic depends on perception and planning that remain reliable when onboard sensing is degraded. In real driving conditions, camera observations are frequently corrupted by occlusion, motion blur, illumination change, and sensor noise, and when such degraded observations are aggregated indiscriminately over time, trajectory planning becomes unstable and collision risk rises for both the ego vehicle and surrounding road users. Recent Bird's-Eye-View (BEV) approaches unify perception and planning through a shared spatial representation, but most fuse temporal information across frames without assessing the reliability of the underlying observations. We present a Reliable Context-Aware and Temporal Planning framework for Autonomous Driving (RCT-AD) that explicitly models feature quality and temporal consistency to support safer, more consistent planning. A Reliable Context Awareness module scores per-frame reliability and selectively retains trustworthy features through a quality-gated First-In-Last-Out (FILO) memory mechanism, reconstructing degraded observations from reliable historical context so that corrupted inputs do not destabilize the scene representation. A Temporal Trajectory Planner captures long-term dependencies and multi-agent interactions to produce smoother, safety-aware trajectories, while a joint detection-and-segmentation head injects semantic and motion cues into the shared BEV space to strengthen scene understanding. Experiments on the nuScenes autonomous driving benchmark show that RCT-AD improves perception accuracy, motion prediction, and planning robustness over recent end-to-end baselines, achieving 61.5 nuScenes Detection Score, 52.9 mean Average Precision, and 52.3 mean Intersection over Union, while maintaining competitive computational efficiency suitable for real-time deployment.

</details>

#### 2026-07-06 - KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation

**Authors:** Xinyu Shao, Keru Zhou, Guowei Huang, Yajun Gao, Tongtong Cao, Xiu Li
**Links:** [abs](https://arxiv.org/abs/2607.04652) - [pdf](https://arxiv.org/pdf/2607.04652)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation
- 作者：Xinyu Shao, Keru Zhou, Guowei Huang, Yajun Gao, Tongtong Cao, Xiu Li
- 出版日期：2026-07-06
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.04652

### 一句话总结
本文提出 KAM-WM 框架，利用冻结的潜在视频世界模型提取运动学可供性图（KAM），为机器人操控提供粗略的方向性交互线索，从而提升少样本学习下的操作成功率。

### 研究问题
如何从少量演示中学习机器人操控，不仅获取交互区域（“在哪里互动”），还能捕获交互的起始运动方向（“如何开始互动”），从而避免仅依赖静态先验（如分割掩码）带来的信息不足。

### 核心思路/方法
1. **利用冻结的潜在视频世界模型**：从预训练的视频模型（Flow Matching 图像到视频骨干）中，通过单次查询获取单步潜在速度，无需展开或微调世界模型。
2. **生成运动学可供性图（KAM）**：将该潜在速度解释为 KAM，提供任务相关的交互区域和粗略的运动结构（方向信息）。
3. **轻量级条件扩散策略**：使用 Perceiver 架构将 KAM 压缩为 tokens，与 RGB 观测和本体感受一起输入扩散策略，生成控制指令。

### 主要贡献
- 提出 KAM-WM 框架，首次在无需世界模型展开或微调的情况下，从冻结的潜在视频模型中提取方向性交互先验（KAM）。
- 在 LIBERO 和 RoboTwin2.0 基准上取得可观性能：LIBERO 平均成功率 90.6%，RoboTwin2.0 简单设置 65.7%、困难设置 22.4%。
- 通过对比零阶掩码先验，验证了方向信息（超越空间定位）对性能提升有贡献。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作聚焦机器人操控中的少样本学习，提出新颖的“方向性交互先验”生成方法，且公开了跨不同基准的明确成功率对比，对操控前沿领域有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

</details>

#### 2026-07-05 - CRISP: A Spatiotemporal Camera-Radar Backbone for Driving via Forecasting-Based World-Model Pretraining

**Authors:** Jingyu Song, Yi Liu, Katherine A. Skinner
**Links:** [abs](https://arxiv.org/abs/2607.04541) - [pdf](https://arxiv.org/pdf/2607.04541)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, autonomous driving, mapping, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CRISP: A Spatiotemporal Camera-Radar Backbone for Driving via Forecasting-Based World-Model Pretraining
- 作者：Jingyu Song, Yi Liu, Katherine A. Skinner
- 出版日期：2026-07-05
- 分类：具身智能/机器人/AR应用（Embodied / Robotics / AR Applications）
- 链接：https://arxiv.org/abs/2607.04541

### 一句话总结
CRISP提出了一种基于预测式世界模型预训练的时空相机-雷达主干网络，通过预测未来LiDAR点云来学习统一的鸟瞰图表示，并在预训练后仅依赖相机和雷达进行部署。

### 研究问题
如何利用预测式表征学习（以未来LiDAR点云为监督信号）来预训练一个鲁棒的、可迁移的相机-雷达融合时空主干网络，从而在无需任务特定监督的情况下学习可复用的驾驶场景表示。

### 核心思路/方法
1. **预训练范式**：使用历史多视角图像和雷达扫描（sweeps）作为输入，预测未来的LiDAR点云；LiDAR仅在预训练阶段作为特权监督信号，部署时仅使用相机和雷达。
2. **模型组件**：
   - **增强型雷达编码器**：提取雷达的测距和速度（Doppler）线索。
   - **雷达增强的时间自注意力机制**：将雷达线索注入到鸟瞰图（BEV）的时间传播中。
   - **多模态特征渲染与模态创新门控**：允许BEV令牌有选择性地吸收相机和雷达的证据。

### 主要贡献
1. 提出了CRISP，首个通过预测式世界模型预训练构建的时空相机-雷达融合主干网络。
2. 设计了多种专门组件（雷达编码器、时间自注意力、特征渲染门控）来使预测式预训练有效服务于相机-雷达融合。
3. 在nuScenes数据集上验证，CRISP不仅提升了长时序点云预测性能，还能有效迁移到3D检测、跟踪、在线地图、运动预测、未来占用预测和规划等多个下游任务。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作聚焦于自动驾驶中实用的相机-雷达传感器配置，提出了一种无需任务特定监督的预训练方法，并在多个关键下游任务（检测、跟踪、规划等）上展示了迁移能力。研究思路新颖（利用LiDAR作为预训练特权信号），具有较好的实用价值和启发性，适合关注自动驾驶感知、多模态融合、自监督/预测式学习的读者。

</details>

<details>
<summary>Abstract</summary>

Camera-radar (CR) fusion is a practical sensing configuration for autonomous driving, but existing models are typically trained with task-specific supervision, limiting reusable representation learning. We present CRISP, a spatiotemporal CR backbone pretrained through forecasting-based representation learning. Given historical multi-view images and radar sweeps, CRISP learns a unified bird's-eye-view (BEV) representation by predicting future LiDAR point clouds. LiDAR is used only as privileged supervision during pretraining; the deployed model requires only camera and radar. To make forecasting-based pretraining effective for CR fusion, CRISP introduces an enhanced radar encoder, radar-enhanced temporal self-attention, and multimodal feature rendering with modality innovation gating. These components inject radar range and Doppler cues into BEV temporal propagation and allow BEV tokens to selectively incorporate camera and radar evidence. Experiments on nuScenes show that CRISP improves long-horizon point cloud forecasting and transfers effectively to downstream tasks, including 3D detection, tracking, online mapping, motion forecasting, future occupancy prediction, and planning, suggesting that predictive CR pretraining is a promising path toward scalable driving representations under practical sensor configurations. The project website is https://umfieldrobotics.github.io/CRISP.

</details>

#### 2026-07-05 - UniSkip-Mamba: A Frequency-Aware State Space Model for Audio-Visual Temporal Forgery Localization

**Authors:** Cangjin Qiu, Quan Zhang, Dan Jiang, Ke Zhang
**Links:** [abs](https://arxiv.org/abs/2607.04498) - [pdf](https://arxiv.org/pdf/2607.04498)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniSkip-Mamba: A Frequency-Aware State Space Model for Audio-Visual Temporal Forgery Localization
- 作者：Cangjin Qiu, Quan Zhang, Dan Jiang, Ke Zhang
- 出版日期：2026-07-05
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.04498

### 一句话总结
本文提出UniSkip-Mamba，一种频率感知的状态空间模型，通过分析伪造区域主要集中于低中频成分，利用跳过扫描机制提升视听时序伪造定位的性能和鲁棒性。

### 研究问题
如何更准确地定位音视频中的时序伪造区域，同时避免对高频噪声的过拟合，提升模型在真实退化数据下的鲁棒性。

### 核心思路/方法
1. **频域分析发现**：通过系统频域分析发现，伪造判别模式主要集中于归一化频率0-0.15的低中频范围，而高频成分主要引入噪声，去除高频成分甚至可使检测性能提升+1.4%。
2. **统一多模态序列融合**：引入Unified Multimodal Sequence Fusion，保留跨模态相位关系。
3. **Skip-Scanning Mamba块**：通过新颖的Group-Scan-Merge机制实现频率感知正则化，自然地将学习偏向于具有判别性的低中频模式（0-0.15），同时保持表征完整性。

### 主要贡献
1. 从信号处理视角提供了频域分析的理论依据，证明跳过扫描（skip-scanning）本质上有助于提升准确性和鲁棒性。
2. 提出了UniSkip-Mamba框架，在LAV-DF上达到63.4% AP@0.95（提升+9.8%），在AV-Deepfake1M上达到63.58% mAP（提升+14.32%），且推理速度快6倍。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对时序伪造定位这一重要安全问题，提出了新频率分析视角和有效方法，结果有显著提升且推理速度快，适合研究者快速了解前沿进展。

</details>

<details>
<summary>Abstract</summary>

With the proliferation of AI-generated content, sophisticated multimedia manipulation has raised critical concerns about malicious applications such as opinion manipulation and evidence fabrication, making Audio-Visual Temporal Forgery Localization (AV-TFL) an urgent research frontier. Existing TFL methods have progressed along two main paradigms: Transformer-based temporal modeling and channel-wise multimodal fusion. While these approaches capture temporal dependencies and cross-modal correlations, they process all frequency components indiscriminately, leading to overfitting on high-frequency noise and limited robustness under real-world data degradation. Through systematic frequency domain analysis, we find that forgery-discriminative patterns concentrate in the low/mid-frequency range (normalized frequency 0-0.15), while high-frequency components primarily introduce noise, removing them even improves detection performance by +1.4%. Based on this phenomenon, we propose UniSkip-Mamba, a frequency-aware State Space Model framework that incorporates Unified Multimodal Sequence Fusion to preserve cross-modal phase relationships, and Skip-Scanning Mamba Blocks that implement frequency-aware regularization through a novel Group-Scan-Merge mechanism, naturally biasing learning toward discriminative low/mid-frequency patterns (0-0.15) while maintaining representational completeness. We achieve state-of-the-art (SOTA) performance: 63.4% AP@0.95 on LAV-DF (+9.8% improvement) and 63.58% mAP on AV-Deepfake1M (+14.32% improvement), with 6x faster inference. Our frequency-domain analysis provides theoretical justification from a signal processing perspective for why skip-scanning inherently improves both accuracy and robustness.

</details>

#### 2026-07-05 - Framework and Multi-modal Dataset for Roadwork Zone Detection and Geo-localization

**Authors:** Zhiran Yan, Yutong Xin, S Shyam Shenoi, Rui Song, Gordon Elger
**Links:** [abs](https://arxiv.org/abs/2607.04330) - [pdf](https://arxiv.org/pdf/2607.04330)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Framework and Multi-modal Dataset for Roadwork Zone Detection and Geo-localization
- 作者：Zhiran Yan, Yutong Xin, S Shyam Shenoi, Rui Song, Gordon Elger
- 出版日期：2026-07-05
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.04330

### 一句话总结
本文提出了一个用于自动驾驶中道路施工区域检测与地理定位的多模态数据集（RZDG），并基于AB3DMOT设计了一个跟踪式管道，实验表明该方法在真实和模拟数据上均达到较高召回率。

### 研究问题
自动驾驶车辆依赖高清地图导航，但地图更新频率低，缺乏临时施工区域这类半静态信息，现有公开数据集缺失导致难以评估相关检测与地理定位模型。

### 核心思路/方法
1. **数据集（RZDG）**：包含模拟数据和真实数据，提供多模态传感器输入及全面标注，支持图像语义分割、3D目标检测和物体地理定位等任务。  
2. **检测与定位管道（RZDG pipeline）**：基于AB3DMOT的扩展，用于将物体从局部坐标系转换到全局坐标系，实现准确的施工区域地理定位。  
3. **评估标准**：以预测位置与真值距离小于1米视为真阳性（TP）。

### 主要贡献
- 公开了一个多模态道路施工区域检测与地理定位数据集（RZDG），填补了该领域的空白。  
- 提出一个基于AB3DMOT的跟踪式管道，实现施工区域检测与全局坐标定位。  
- 在真实和模拟数据上进行了基准测试，精度分别为0.565（真实）和0.615（模拟），召回率分别为0.898和0.809，F1-score分别为0.597和0.665。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文切中自动驾驶中高清地图更新慢、缺乏半静态施工区域标注数据的实际痛点，提出了首个相关多模态数据集和基准管道，实验显示召回率较高（超过0.8），对自动驾驶安全性和地图动态更新有直接应用价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous vehicles often rely on high-definition (HD) maps for navigation; however, these maps are not frequently updated and often lack semi-static information, such as temporary roadwork zones, which can significantly alter the road network. This limitation underscores the urgent need for an accurate global position of roadwork zones. However, the absence of publicly available datasets for evaluating roadwork zone detection and geo-localization models has hindered the development of reliable autonomous driving systems. To address this challenge, we propose the Roadwork Zone Detection and Geo-localization (RZDG) dataset, which includes both simulated and real-world data, providing multimodal sensor inputs along with comprehensive annotations. The dataset supports multiple perception tasks, including image semantic segmentation, 3D object detection, and object geo-localization. In addition, we introduce a tracker-based roadwork zone detection and geo-localization (RZDG) pipeline, an extension of AB3DMOT, for accurate object geo-localization in roadwork zones. We benchmark our approach on the RZDG dataset, demonstrating its effectiveness in detecting roadwork zones and transforming object positions from the local coordinate system to the global coordinate system. A prediction is considered a true positive (TP) if its estimated position falls within one meter of the ground truth. Our experimental results show that our approach achieves high accuracy on both real and simulated data. Specifically, we report: Precision: 0.565 (real) / 0.615 (simulated) Recall: 0.898 (real) / 0.809 (simulated) F1-score: 0.597 (real) / 0.665 (simulated).

</details>

#### 2026-07-05 - ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning

**Authors:** Iok Tong Lei, QianZhi Li, Ying Jie Yap, Yujie Zhang, Rui Zhong, Haichao Gui, Xiaolong Liu, Zhidong Deng
**Links:** [abs](https://arxiv.org/abs/2607.04162) - [pdf](https://arxiv.org/pdf/2607.04162)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning
- 作者：Iok Tong Lei, QianZhi Li, Ying Jie Yap, Yujie Zhang, Rui Zhong, Haichao Gui, Xiaolong Liu, Zhidong Deng
- 出版日期：2026-07-05T08:07:42Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.04162

### 一句话总结
该论文提出了一种名为ACE的零样本工作流推理框架，用于桌面拾放操作任务，通过将语义推理与掩码介导的视觉动作接口结合，实现了在长时域、逻辑复杂任务中的零样本泛化和闭环自适应。

### 研究问题
如何让机器人代理在桌面操作任务中，仅通过自然语言指令，无需任务特定重训练，就能在动态环境和执行失败的情况下进行零样本泛化并稳健完成长时域、逻辑复杂的操作。

### 核心思路/方法
ACE采用零样本工作流推理框架，将高级语义推理与两个可执行底层技能（视觉接地位接口和可复用拾放原语）相结合。具体方法包括：通过掩码介导的视觉-动作接口将主动子目标接地，该掩码统一指定目标对象和目的地，并随时间跟踪；系统以闭环方式运行，并支持多时间尺度记忆，在执行动作后自动验证子目标是否成功，并根据结果推进、重试、修复或重新规划，从而实现在线适应。

### 主要贡献
1. 提出了ACE，一个零样本工作流推理框架，能够在桌面拾放操作中实现任务级零样本泛化，无需任务特定重训练。
2. 设计了一种掩码介导的视觉-动作接口，用于桥接语义推理与物理控制，支持目标追踪和人工验证。
3. 实现了基于多时间尺度记忆的闭环控制，支持在线适应（如用户更正、场景变化和物理失败）。
4. 在逻辑复杂、长时域的任务（如多步等号形成和约束检索）上，相比端到端基线方法，ACE取得了显著更高的成功率（等号形成为50%，约束检索为70%）。

### 局限性
摘要未提供足够信息，无法确定该方法的具体局限性（例如对掩码质量或工作流推理精度的依赖、未测试的任务类型或场景、计算资源需求等）。

### 阅读优先级
**高**  
理由：该论文针对具身操作中零样本泛化和闭环自适应这一前沿挑战，提出了新颖的代理工作流推理框架，并在长时域、逻辑复杂的任务上展示了显著优于标准基线的性能。对于从事机器人操作、零样本学习或语义推理与物理控制交叉领域的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Open-ended tabletop manipulation requires agents to not only understand natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for Embodied Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language. Rather than relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing executable skills: a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning and physical control, the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask specifies the target object and destination, is tracked over time, exposed for human verification, and ultimately passed to a task-agnostic downstream policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale memory. After an action is executed, the system automatically verifies whether the intended sub-goal succeeded, using the outcome to advance, retry, repair, or replan. This enables online adaptation to user corrections, scene changes, and physical failures. We evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation formation with number cubes and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization on novel semantic constraints and randomized tabletop scenes without task-specific retraining. Specifically, while standard end-to-end baselines struggle to complete these logically demanding tasks, ACE achieves a 50% success rate in equation formation and a 70% success rate in constraint retrieval. This contrast demonstrates that explicit workflow reasoning and mask-mediated control offer a robust, practical route toward adaptable robotic manipulation.

</details>

#### 2026-07-04 - WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control

**Authors:** Jiahao Jiang, Jianing Zhang, Zhenhan Yin, Ruidong Chen, Sen Wang, Zhaoshu Yu, Pengpeng Zeng, Xiaofeng Cao, Xuanhan Wang, Jingkuan Song, Heng Tao Shen
**Links:** [abs](https://arxiv.org/abs/2607.03941) - [pdf](https://arxiv.org/pdf/2607.03941)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, manipulation, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WSA₁: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control
- 作者：Jiahao Jiang, Jianing Zhang, Zhenhan Yin, Ruidong Chen, Sen Wang, Zhaoshu Yu, Pengpeng Zeng, Xiaofeng Cao, Xuanhan Wang, Jingkuan Song, Heng Tao Shen
- 出版日期：2026-07-04
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.03941

### 一句话总结
本文提出WSA₁，一种基于3D中心的世界-空间-动作联合建模的机器人基础模型，通过在预训练中融入3D世界意识与因果推理，以少量真实数据实现了竞争性的泛化操控性能。

### 研究问题
当前的机器人基础模型因依赖2D视觉感知而缺乏对物理动力学及行为在3D世界中的因果效应推理能力，导致在现实任务中的泛化能力受限。研究旨在解决2D视觉与3D具身交互之间的根本性不匹配问题。

### 核心思路/方法
提出3D中心的世界-空间-动作建模范式，构建WSA₁模型。该模型不仅学习对未来机器人行为的3D世界感知视觉思维，还显式建模3D世界状态转移与机器人动作之间的相互约束关系，从而增强行为泛化。预训练使用6000小时的专家演示数据（其中仅1000小时来自真实机器人）。

### 主要贡献
1. 提出一种3D中心的世界-空间-动作建模范式，赋予机器人基础模型3D世界意识与因果推理能力。
2. 在RoboTwin2.0仿真基准上以93%的成功率取得有竞争力的操控性能。
3. 在真实机器人控制任务上，相比现有最优机器人基础模型平均性能提升+20%。
4. 展示了结合3D中心联合建模后，无需大规模真实机器人数据即可实现可泛化的机器人基础模型。

### 局限性
摘要未提供足够信息，无法分析具体局限性（如模型复杂度、计算成本、未讨论失败案例或特定场景下的性能退化等）。

### 阅读优先级
**高**
理由：该工作针对机器人领域核心痛点（2D-3D不匹配），提出新颖的3D中心联合建模范式，在仿真和真实场景中均取得显著性能提升（+20%），且数据效率较高，对具身智能与机器人泛化研究具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks.To address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm. It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between 3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical and affordable pathway to generalist robotic systems.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
