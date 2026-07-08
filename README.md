# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：69
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 24
  - Embodied / Robotics / AR Applications: 19
  - Neural Scene Representations & Rendering: 17
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的今日论文列表生成的中文科研趋势综合分析。

#### 今日主要趋势

1.  **从静态重建到动态、具身场景的统一理解**：趋势明确从单一对象的静态重建，转向对包含动态物体（如人体、手术器械）和智能体（如机器人、车辆）的复杂场景进行统一、动态的4D理解与重建。代表性论文包括：
    *   `GUSH3R`：直接从单目视频同时重建动态人体和静态场景。
    *   `DeGenseGS`：在4D高斯泼溅中独立建模语义演变与几何形变，用于动态手术场景。
    *   `CRISP`：通过预测未来点云预训练时空主干网络，用于自动驾驶场景理解。
    *   `TGRIP`：将语义先验注入BEV空间进行动态车辆实例预测。

2.  **前馈式方法成为主流，并解决其核心缺陷（冗余与退化）**：前馈式（Feedforward）方法因其高效率在3D重建中占据主导，但今日论文集中关注并解决其两个核心问题：**表示冗余**（如 `AdaptiveSplat` 的纹理感知剪枝）和**长序列状态退化**（如 `ReCal3R` 的可靠性校准学习率）。同时，前馈方法正被扩展到更具挑战性的“野生”场景（`WildSplat`）和非刚性动态场景（`GUSH3R`）。

3.  **几何与语义/外观的显式解耦**：为了提升鲁棒性和泛化能力，众多工作抛弃了隐式绑定，转而设计架构将**几何与外观**（`WildSplat`, `FocusGS`）、**几何与语义**（`DeGenseGS`）、**几何与时间**（`FocusGS`）显式解耦。这一趋势使得模型能更专注地处理各自领域的挑战（如光照变化、运动模糊、类别多样性），并互相补充。

4.  **基础模型与记忆/先验的深度融合**：大型预训练基础模型（如视觉-语言模型VLM、视频世界模型）不再只是简单调用，而是被深度集成到任务框架中，提供**语义先验**（`TGRIP`）、**运动学交互线索**（`KAM-WM`）或**几何先验**（`MemPose`的类别级记忆）。这体现了从“特征提取”到“知识注入”的范式转变，以解决小样本、零样本或开放词汇等难题。

#### 技术路线观察

| 方向 | 论文/领域 | 技术侧重点 |
| :--- | :--- | :--- |
| **几何基础模型** | `RIC-Loc`, `AdaptiveSplat` | **场景无训练**与**零样本泛化**是核心目标。`RIC-Loc`依赖前馈模型`VGGT`和假设共识，`AdaptiveSplat`则探索了基于纹理信息的自适应高斯分配范式，旨在减少冗余，提高前馈重建的效率和紧凑性。 |
| **3D/4D 重建** | `ReCal3R`, `GUSH3R`, `FocusGS`, `HeartVolMesh`, `NeLD-BA` | 技术路线分化明显：**流式重建**关注状态维护（`ReCal3R`）；**动态场景**追求前馈式、统一的人-物重建（`GUSH3R`）；**稀疏输入**转向靶向计算与几何模糊区域补全（`FocusGS`）；**领域特定**（如心脏、LiDAR）则强调**隐式表示（如NeRF）与显式先验/物理约束结合**（`HeartVolMesh`, `NeLD-BA`）。 |
| **神经场景表示与渲染** | `WildSplat`, `DeGenseGS`, `AdaptiveSplat` | 3D/4D高斯泼溅（3DGS/4DGS）是其共同基础。趋势在于将3DGS与**可控制性**结合：`WildSplat`解耦几何与外观以支持外观编辑，`DeGenseGS`解耦几何与语义以支持语义理解，`AdaptiveSplat`则控制高斯数量以提升效率。 |
| **机器人/AR 应用** | `TGRIP`, `CRISP`, `KAM-WM`, `ACE`, `RCT-AD` | 大量工作聚焦于**自动驾驶**和**机械臂操作**。技术共性在于：1）利用**预测式表征学习**（世界模型）作为预训练目标 (`CRISP`)；2）引入**语义/语言先验**指导决策 (`TGRIP`, `KAM-WM`)；3）设计**可靠性感知**与**闭环控制**机制，以应对现实世界的不确定性 (`RCT-AD`, `ACE`)。 |

#### 值得优先阅读的论文

1.  **【阅读优先级：最高】WildSplat (2607.05347)**
    *   **理由**：首次将前馈3D高斯泼溅成功应用于光照变化剧烈的“野生”场景，解决了该领域长期存在的挑战。其双分支解耦架构和多参考训练策略设计精巧，代表了神经渲染向实用化、鲁棒化迈进的重要一步。

2.  **【阅读优先级：最高】GUSH3R (2607.05243)**
    *   **理由**：将前馈式重建从静态场景扩展到包含动态人体的复杂场景，且是首个一次前向传播输出3DGS基元的框架。这直接关系到AR、数字人等热门应用，并为动态场景重建开辟了新范式。

3.  **【阅读优先级：高】ReCal3R (2607.05356)**
    *   **理由**：直接指出了流式3D重建的“阿克琉斯之踵”——状态退化，并提出一个简单、训练无关且有效的解决方案。对于任何从事长序列重建（如SLAM、视频重建）的研究者，其思路（可靠性校准）具有重要参考价值。

4.  **【阅读优先级：高】DeGenseGS (2607.04761)**
    *   **理由**：解决了4D重建中几何与语义严重错位这一普遍问题，其核心思想——解耦——具有跨领域通用性。结合手术导航这一关键应用场景，其方法和实验设计（与VLM的集成）对该领域有显著启发。

5.  **【阅读优先级：高】FocusGS (2607.04661)**
    *   **理由**：针对自动驾驶中稀疏视图重建效率低下的痛点，提出了一个清晰且高效的范式转变（从全局稠密化到靶向补全）。其性能提升（高斯数减少74%）非常亮眼，展示了将计算资源聚焦于“不确定区域”的正确性。

#### 可能的研究机会

1.  **面向动态、交互式场景的“基础世界模型”**：当前工作（`CRISP`, `KAM-WM`, `ACE`）分别利用预测、交互先验或工作流推理。一个明确的机会是结合三者，构建一个统一的、能同时预测运动、提供交互建议并执行闭环控制的零样本通用操纵/驾驶基础模型。

2.  **“可靠性”评估的泛化与理论化**：`ReCal3R`和`RCT-AD`等工作提出了基于状态或感知特征的可靠性度量。如何将这些概念**泛化**到其他任务（如定位`RIC-Loc`已给出），并建立一套更**理论化、通用化的“场景特征可靠性”评估框架**，是一个值得深入的方向。

3.  **记忆增强与高效场景理解的结合**：`MemPose`利用外部记忆存储类别优先级结构，而`AdaptiveSplat`和`FocusGS`则关注降低表示冗余。一个自然的组合是：**将记忆机制引入紧凑、自适应的3D表示**，使模型既能高效地表示场景，又能从历史经验中按需提取结构化知识（如物体类别、关系、潜在运动方式），从而在资源受限的机器人或AR设备上实现更智能、持久的场景理解。

4.  **面向4D语义/实例级编辑的解耦表示**：`DeGenseGS`和`WildSplat`分别解耦了语义-几何和外观-几何。未来机会在于**将两者（以及实例信息）统一整合到一个解耦的

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-08T10:39:56-04:00
**Total number of papers:** 67
**Number of papers added in the latest update:** 16
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

#### 2026-07-07 - TRIG: Trajectory-Rig Decoupled Metric Geometry Learning

**Authors:** Lizhou Liao, Wentao Xu, Handong Wang, Lirong Yang, Shuai Yang, Weiwei Liu, Chang Huang
**Links:** [abs](https://arxiv.org/abs/2607.05801) - [pdf](https://arxiv.org/pdf/2607.05801)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** depth prediction, geometric reasoning, metric depth, 3D reconstruction, pose estimation, autonomous driving

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

#### 2026-07-02 - PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

**Authors:** Haofei Xu, Rundi Wu, Philipp Henzler, Nikolai Kalischek, Michael Oechsle, Fabian Manhardt, Marc Pollefeys, Andreas Geiger, Federico Tombari, Michael Niemeyer
**Links:** [abs](https://arxiv.org/abs/2607.02515) - [pdf](https://arxiv.org/pdf/2607.02515)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** point map, monocular geometry, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation
- 作者：Haofei Xu, Rundi Wu, Philipp Henzler, Nikolai Kalischek, Michael Oechsle, Fabian Manhardt, Marc Pollefeys, Andreas Geiger, Federico Tombari, Michael Niemeyer
- 出版日期：2026-07-02
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.02515

### 一句话总结
本论文提出一个简化到极致的像素空间扩散模型（PointDiT），直接用原始3D点图块对单张图像进行几何估计，无需复杂架构、损失函数或点图分词器。

### 研究问题
单目图像中几何估计的方法往往依赖复杂的混合架构和损失函数，或将几何压缩到隐空间以利用预训练隐扩散模型。作者认为这些架构开销和复杂损失设计并非必要，因此探索能否用极简的纯像素空间扩散方法完成任务。

### 核心思路/方法
- 构建一个基于普通ViT（Vision Transformer）的像素空间扩散Transformer（PointDiT），直接对原始3D点图块（raw 3D point map patches）进行操作。
- 通过预训练的DINOv3提取图像特征（image tokens）作为条件。
- 与传统隐扩散方法不同，该扩散主干从头训练，无需点图分词器。
- 整个方法在架构和损失设计上力求最小化，不采用混合架构或复杂损失函数。

### 主要贡献
- 证明单目几何估计可以通过极简的像素空间扩散方法实现，无需隐空间压缩或混合架构。
- PointDiT在性能上超越复杂的隐扩散模型，同时比混合替代方案显著更简单。
- 生成的几何结构更锐利，在透明物体等高度歧义区域更具鲁棒性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法在架构简化上有明显创新，且展示了更好的性能与鲁棒性，适合对扩散模型和单目几何估计感兴趣的读者。但由于摘要未提供定量实验细节，需要进一步阅读全文评估其实际收益。

</details>

<details>
<summary>Abstract</summary>

State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained latent diffusion models. In this work, we show that such architectural overhead and intricate loss formulations are unnecessary. We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on image tokens from a pre-trained DINOv3. Unlike existing latent diffusion approaches, we train our diffusion backbone entirely from scratch, eliminating the need for point map tokenizers. Despite its simplicity, our approach surpasses complex latent-based diffusion models while remaining significantly simpler than hybrid alternatives. Notably, it produces sharper geometric structure and is more robust in highly ambiguous regions, such as transparent objects.

</details>

#### 2026-07-02 - Diversity-aware View Partitioning for Scalable VGGT

**Authors:** Jinsoo Park, Donggyu Choi, Ahyun Seo, Minsu cho, Jeany Son
**Links:** [abs](https://arxiv.org/abs/2607.01885) - [pdf](https://arxiv.org/pdf/2607.01885)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, depth prediction, 3D reconstruction, multi-view reconstruction, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Diversity-aware View Partitioning for Scalable VGGT
- 作者：Jinsoo Park, Donggyu Choi, Ahyun Seo, Minsu cho, Jeany Son
- 出版日期：2026-07-02
- 分类：Geometry Foundation Models (主要), 3D Reconstruction & Multi-view Geometry (次要)
- 链接：[摘要](https://arxiv.org/abs/2607.01885) | [PDF](https://arxiv.org/pdf/2607.01885)

### 一句话总结
本文提出一个无需训练、即插即用的VGGT推理框架，通过基于视觉差异和空间离散度的图划分，将视图组织成多样性感知的均衡块，以减少冗余注意力交互并提升大视图集合下的重建质量与效率。

### 研究问题
如何解决VGGT等几何变换器在扩展到大量视图时存在的注意力二次成本问题，以及冗余视图稀释有效几何信号导致的性能退化问题。

### 核心思路/方法
1. **观测驱动**：发现VGGT的性能对视图分布敏感，冗余视图会引入高度相似的token，稀释注意力机制中的有效几何信号。  
2. **多样性感知分块**：提出无需训练、即插即用的推理框架，将视图划分为多样性感知的均衡块。块通过基于**视觉不相似性**和**空间离散度**的组合图划分构建，使注意力聚焦于几何信息丰富的视图。  
3. **软姿态传播**：为近似空间离散度而不依赖完整姿态估计，采用基于种子帧视觉相似性的软姿态传播策略，推理视图间的空间关系。

### 主要贡献
- 揭示了视图多样性对VGGT重建质量的关键影响，以及冗余视图导致性能下降的现象。  
- 提出一种无需训练、即插即用的视图组织框架，通过图划分实现注意力聚焦。  
- 在相机姿态估计、多视图深度预测和3D重建任务上取得改进，同时降低内存占用和推理延迟。  
- 该框架可补充现有VGGT变体，实现可扩展的多视图重建而不损失几何保真度。

### 局限性
摘要未提供关于方法对特定场景（如极端视图数量、低纹理区域或动态场景）的鲁棒性分析，也未讨论软姿态传播可能存在的误差上限。摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该工作聚焦于几何基础模型的实用扩展（减少计算、提升可扩展性），方法具有即插即用特性，对从事多视图重建与效率优化的研究者有实际参考价值。但问题本身较为工程导向，且依赖VGGT预训练模型，并非理论突破，故优先级适中。

</details>

<details>
<summary>Abstract</summary>

Geometry transformers such as VGGT achieve strong performance by jointly reasoning over multiple views with global attention. However, scaling them to large view collections remains challenging due to the quadratic cost of attention. Moreover, our empirical analysis reveals that the reconstruction quality in VGGT is sensitive to the distribution of viewpoints. Simply increasing the number of views without sufficient viewpoint diversity can even degrade performance, as redundant views introduce highly similar tokens that dilute informative geometric signals in the attention mechanism. Motivated by this observation, we propose a training-free and plug-and-play VGGT inference framework that organizes views into diversity-aware balanced chunks. The chunks are constructed through combinatorial graph partitioning over visual dissimilarity and spatial dispersion. This view organization allows the transformer to focus attention on geometrically informative views while reducing redundant attention interactions. To estimate spatial dispersion without full pose estimation, we approximate spatial relationships via a soft pose propagation strategy based on visual similarity from a small set of seed frames. Extensive experiments demonstrate improved performance in camera pose estimation, multi-view depth prediction, and 3D reconstruction while reducing memory usage and inference latency. Our framework also complements existing VGGT variants, enabling scalable multi-view reconstruction without sacrificing geometric fidelity.

</details>

#### 2026-07-02 - Geometric Foundation Model Distillation for Efficient Lunar 3D Reconstruction

**Authors:** Clémentine Grethen, Florient Chouteau, Géraldine Morin, Simone Gasparini
**Links:** [abs](https://arxiv.org/abs/2607.01851) - [pdf](https://arxiv.org/pdf/2607.01851)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** geometric foundation model, MASt3R, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometric Foundation Model Distillation for Efficient Lunar 3D Reconstruction
- 作者：Clémentine Grethen, Florient Chouteau, Géraldine Morin, Simone Gasparini
- 出版日期：2026-07-02
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要页 https://arxiv.org/abs/2607.01851 ；PDF https://arxiv.org/pdf/2607.01851

### 一句话总结
本文研究如何通过知识蒸馏将大型3D基础模型（MASt3R）压缩为轻量级学生模型，在月球立体重建任务中实现模型规模缩小7倍而精度损失很小。

### 研究问题
在计算资源严重受限的星载部署环境下（如行星探测），如何高效压缩大型3D基础模型（尤其是MASt3R），使其在保持重建精度的同时显著降低模型参数量与计算需求。

### 核心思路/方法
以在月表图像上微调过的688M参数MASt3R模型作为教师，蒸馏其密集几何预测结果给一组轻量级学生模型。学生模型探索了不同编码器类型（CNN vs ViT）、解码器宽度/深度及训练策略。为解决师生解码器维度不匹配问题，提出了基于SVD的结构化初始化方法，将教师解码器权重投影至学生更小的隐空间，作为训练起点以改善收敛和最终性能。

### 主要贡献
1. 在月球立体重建任务上验证了知识蒸馏可将模型压缩7倍，且学生模型保留大部分重建精度，甚至优于直接使用稀疏真值监督训练的基线。
2. 提出基于SVD的解码器初始值映射方法，有效提升蒸馏训练稳定性与收敛效果。
3. 揭示几何基础模型蒸馏的关键原则：卷积编码器性能不如Transformer（但预训练可用性为混淆因素）；保留编码器容量比维持大解码器更重要；特征级蒸馏始终优于仅输出层监督；SVD初始化可改善优化稳定性。

### 局限性
摘要未提供足够信息。未讨论蒸馏学生模型在非月球场景或更广泛3D任务上的泛化能力，也未涉及实际硬件部署的推理延迟或能耗对比。

### 阅读优先级
高  
理由：针对资源受限环境（如星载计算）下的3D模型压缩问题提出了系统性的蒸馏方案与实用准则，且方法在具体任务上实现了7倍压缩；对从事边缘部署3D重建或基础模型轻量化的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Large 3D foundation models such as MASt3R achieve state-of-the-art stereo reconstruction but are computationally demanding for deployment under strict hardware constraints -- a critical limitation in domains such as planetary exploration, where onboard computing is severely restricted. We study how far such models can be compressed through knowledge distillation, using lunar stereo reconstruction as a challenging and practically relevant case study. Starting from a 688M-parameter MASt3R teacher fine-tuned on lunar imagery, we distill its dense geometric predictions into a family of lightweight students spanning different encoder types (CNN vs ViT), decoder widths and depths, and training strategies. To bridge the dimensional mismatch between teacher and student, we propose a structured SVD-based initialization that projects the teacher's decoder weights into the student's smaller latent space, yielding a warm start that significantly improves convergence and final performance. Based on our results on lunar data, we can obtain a distilled student that retains most of teacher's reconstruction accuracy while reducing the model size up to 7 times, and even outperforms a baseline trained directly with sparse ground-truth annotations. Beyond compression, our study highlights both principles and practical insights for distilling geometric foundation models: a convolutional encoder underperforms transformer-based alternatives (though pretraining availability remains a confounding factor), preserving encoder capacity is more critical than maintaining a large decoder, feature-level distillation consistently outperforms output-only supervision, and SVD-based initialization improves optimisation stability. These findings provide practical guidelines for deploying 3D reconstruction models in resource-constrained environments.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

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

#### 2026-07-02 - MVFusion-GS: Motion-Variance Guided Temporal Attention for High-Quality Dynamic Gaussian Splatting

**Authors:** Jianwei Hu, Tingxuan Huang, Hengyu Zhou, Ningna Wang, Xiaohu Guo Jinshan Lai, Bin Wang
**Links:** [abs](https://arxiv.org/abs/2607.01578) - [pdf](https://arxiv.org/pdf/2607.01578)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MVFusion-GS: Motion-Variance Guided Temporal Attention for High-Quality Dynamic Gaussian Splatting
- 作者：Jianwei Hu, Tingxuan Huang, Hengyu Zhou, Ningna Wang, Xiaohu Guo, Jinshan Lai, Bin Wang
- 出版日期：2026-07-02
- 分类：Dynamic / 4D Reconstruction, Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.01578

### 一句话总结
本文提出MVFusion-GS，通过两种互补的运动感知机制（运动方差引导的细化与运动先验时间注意力）增强变形网络，提升了动态场景三维高斯泼溅（3DGS）的重建质量，并在动态与去干扰重建基准上达到最先进性能。

### 研究问题
现有基于变形场的动态3DGS方法缺乏显式运动意识：既不能捕捉长期运动强度，也不能利用短期时间连贯性，导致前景变形不准确和背景出现伪静态残留。

### 核心思路/方法
1. **运动方差引导的细化（Motion-Variance Guided Refinement）**：跨时间聚合每个高斯的变形统计量，估计运动方差，并利用该方差在变形预测中指导动态-静态分离。
2. **运动先验时间注意力模块（MotionFormer Temporal Attention）**：对相邻时间步应用Transformer自注意力，建模局部运动依赖性，提升时间一致性。

### 主要贡献
- 提出了MVFusion-GS方法，通过显式运动感知机制增强变形网络。
- 设计了两种互补模块：运动方差引导的细化与运动先验时间注意力，分别解决长期运动强度与短期时间连贯性问题。
- 在动态场景重建和去干扰重建两个基准上取得了最先进性能，显式运动意识同时改善了前景运动建模和静态背景重建。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法针对动态3DGS中变形网络缺乏运动意识的核心瓶颈，提出了新颖且互补的双机制方案，并在多个基准上验证了SOTA性能。若研究方向涉及动态场景重建、4D重建或神经渲染，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel view synthesis for static scenes. Extending it to dynamic scenes via deformation fields has recently attracted significant attention, particularly for dynamic scene reconstructionband distractor-free. However, existing deformation networks lack explicit motion awareness: they neither capture long-term motion intensity nor exploit short-term temporal coherence, leading to inaccurate foreground deformation and pseudo-static residuals in the background. We present MVFusion-GS, a method that enhances deformation networks with two complementary motion-aware mechanisms. The Motion-Variance Guided Refinement aggregates per-Gaussian deformation statistics across time to estimate motion variance and uses it to guide dynamic-static separation during deformation prediction. The MotionFormer Temporal Attention module applies Transformer self-attention over neighboring timesteps to model local motion dependencies and improve temporal consistency. Extensive experiments on both dynamic scene reconstruction and distractor-free reconstruction benchmarks demonstrate state-of-the-art performance, showing that explicit motion awareness improves both foreground motion modeling and static background reconstruction.

</details>

#### 2026-07-01 - World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video

**Authors:** Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, Tianye Li, Zan Gojcic, Gordon Wetzstein, Iro Armeni, Shalini De Mello, Alex Trevithick
**Links:** [abs](https://arxiv.org/abs/2607.01202) - [pdf](https://arxiv.org/pdf/2607.01202)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic 3D, dynamic Gaussian, 3DGS, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video
- 作者：Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, Tianye Li, Zan Gojcic, Gordon Wetzstein, Iro Armeni, Shalini De Mello, Alex Trevithick
- 出版日期：2026-07-01
- 分类：Dynamic / 4D Reconstruction (主), Neural Scene Representations & Rendering (副)
- 链接：摘要: https://arxiv.org/abs/2607.01202 ; PDF: https://arxiv.org/pdf/2607.01202

### 一句话总结
本文提出一种从单目视频生成可自由渲染的动态3D高斯表征的方法，通过将视频模型条件化在密集、像素对齐的渲染结果上，修正初始重建的伪影并填补缺失区域，在4D重建任务上达到了新SOTA。

### 研究问题
如何从单目视频中重建高质量的动态3D高斯表征，以解决初始重建中出现的渲染伪影和缺失区域问题，并同时提升新视角合成与底层3D运动质量。

### 核心思路/方法
1.  **条件视频模型**：将视频模型条件化在密集、像素对齐的渲染结果上，这些渲染结果编码了外观、几何和3D场景运动，覆盖输入和目标相机轨迹。
2.  **数据集构建**：构建一个由对齐的多视角视频对和动态3DGS表征组成的训练数据集，并模拟单目重建特有的伪影。
3.  **测试时蒸馏**：在测试阶段，将模型生成的包含新观测区域和运动的结果，蒸馏回一个单一、一致且高质量的动态3DGS中，从而同时改进新视角合成和底层3D运动。

### 主要贡献
1.  提出了一种从单目视频生成自由可渲染的动态3D高斯表征的新方法。
2.  构建了包含对齐多视角视频对和模拟伪影的数据集，以训练条件视频模型。
3.  在4D重建任务上达到了新的最优性能（SOTA），并能够无缝泛化到具有大视角变化和动态运动的野外视频。

### 局限性
摘要未提供关于局限性的具体信息。

### 阅读优先级
**高**
理由：该方法在4D重建任务上声称达到新SOTA，并且能够处理具有大视角变化的野外动态视频，这对于从单目视频进行动态场景重建这一重要研究方向具有显著价值。方法设计包含条件视频模型、模拟伪影和蒸馏流程，结构完整且新颖。

</details>

<details>
<summary>Abstract</summary>

We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderings that encode appearance, geometry, and 3D scene motion along both input and target camera trajectories to correct rendering artifacts and fill in missing regions from an initial reconstruction. To train this model, we construct a dataset of aligned multiview video pairs and dynamic 3DGS representations, with simulated artifacts characteristic of monocular reconstruction. At test time, we distill the model's generations, including newly observed regions and motions, back into a single consistent, high-quality dynamic 3DGS, improving both novel-view synthesis and the underlying 3D motion. Our method sets a new state of the art in 4D reconstruction and seamlessly generalizes to in-the-wild videos with large viewpoint changes and dynamic motions.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-07 - Vision as Unified Multimodal Generation

**Authors:** Xiaoyang Han, Jianhua Li, Kewang Deng, Zukai Chen, Xuanke Shi, Sihan Wang, Boxuan Li, Linyan Wang, Siyi Xie, Xin You, Jinsheng Quan, Zhongang Cai, Haiwen Diao, Ziwei Liu, Lei Yang, Dahua Lin, Quan Wang
**Links:** [abs](https://arxiv.org/abs/2607.06560) - [pdf](https://arxiv.org/pdf/2607.06560)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation, depth estimation

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
<summary>Abstract</summary>

Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combining learned 2D data association and uncertainty with differentiable geometric optimization in recurrent architectures. Still, it remains unclear exactly which components are fundamentally responsible for this success. In this paper, we ask: Is the superior performance of deep learning-based systems driven primarily by learned 2D data association, the combination of learned 2D data association and uncertainty, or the recurrent architecture itself? We investigate this question empirically by conducting a controlled study. Our findings reveal that the success of DL-based V-SLAM systems hinges on learned 2D data association and uncertainty rather than their recurrent architecture, underscoring the necessity of learning-based paradigms for the design of these components. Upon acceptance, the code will be released as open source.

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

#### 2026-07-02 - VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval

**Authors:** Cristian-Gabriel Florea, Stelian Spînu
**Links:** [abs](https://arxiv.org/abs/2607.02371) - [pdf](https://arxiv.org/pdf/2607.02371)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation, monocular depth, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval
- 作者：Cristian-Gabriel Florea, Stelian Spînu
- 出版日期：2026-07-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.02371

### 一句话总结
VisionAId 是一个离线优先的安卓视觉助手，通过六个端侧深度学习模型和可选的云大语言模型，为视障人士提供实时障碍规避、物品检索、人脸识别和货币检测等多模态辅助功能。

### 研究问题
如何利用普通智能手机的端侧计算能力，为视障人士提供实时、离线优先、多模态的视觉辅助，尤其是实现个性化物品的精准检索与引导。

### 核心思路/方法
1. **硬件与运行时**：在普通安卓手机上部署六个端侧深度学习模型，完全通过 ONNX Runtime 运行，同时可选云大语言模型（Google Gemini Flash）用于场景描述和自动标签化。
2. **核心模型**：集成公制单目深度估计、实例分割、视觉/人脸嵌入、人脸检测和定制纸币检测器。
3. **个性化物品检索**：提出少样本流水线——用户从多角度拍摄物品照片，系统后后续环境中定位该特定实例，并通过增强现实标记、空间音频和距离比例触觉反馈引导用户。
4. **多模态反馈**：使用罗马尼亚语语音合成、语音指令和振动反馈。

### 主要贡献
1. 提出一个完全离线优先的安卓视觉辅助系统，整合六种深度模型，利用 ONNX Runtime 实时运行。
2. 设计并实现面向视障人士的个性化物体少样本检索流水线，支持实时定位与多模态引导。
3. 通过 INT8 量化将深度估计延迟从约1200毫秒降至约491毫秒；定制纸币检测器达到 mAP@50 为 0.986；在3米内公制深度误差低于1厘米。

### 局限性
摘要未提供足够信息以判断系统的局限性，如个性化检索在不同环境光照下的稳定性、用户测试结果、电池消耗等。

### 阅读优先级
**高**。理由：论文提出了一个完整且实用的离线端侧多模态辅助系统，针对视障人士的实际需求（个性化检索），在手机上实现了低延迟、高精度的深度估计和检测，对移动端计算机视觉和人机交互领域有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Over 285 million people worldwide live with a visual impairment, for whom everyday tasks such as avoiding obstacles, locating personal belongings, recognizing familiar faces, or handling cash remain persistent obstacles to personal autonomy. Existing assistive applications are typically limited to recognizing predefined categories, depend heavily on cloud connectivity, or require dedicated hardware. We present VisionAId, an Android application that turns a commodity smartphone into a real-time visual assistant. The system integrates six on-device deep learning models (metric monocular depth estimation, instance segmentation, visual and facial embeddings, face detection, and a custom banknote detector) running entirely through ONNX Runtime, with an optional cloud large language model (Google Gemini Flash) used only for narrative scene description and automatic object labeling. A distinctive contribution is a few-shot pipeline for personal objects: the user photographs an object from several angles, and the system later locates that specific instance in the environment, guiding the user toward it with augmented-reality markers, spatial audio, and distance-proportional haptics. All feedback is multimodal (Romanian speech synthesis, voice commands, vibration). On a reference device (Samsung Galaxy S21 Ultra), INT8 quantization reduces depth latency from ~1200 ms to ~491 ms, the custom banknote detector reaches an mAP@50 of 0.986, and metric depth is calibrated to below 1 cm of error within 3 m.

</details>

#### 2026-07-02 - InvSplat: Inverse Feed-Forward Scene Splatting

**Authors:** Polina Karpikova, Wenjing Bian, Haofei Xu, Hendrik Lensch, Andreas Geiger
**Links:** [abs](https://arxiv.org/abs/2607.02301) - [pdf](https://arxiv.org/pdf/2607.02301)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** feed-forward reconstruction, 3D reconstruction, multi-view reconstruction, Gaussian primitive, novel view synthesis, view synthesis, scene representation, inverse rendering, relighting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InvSplat: Inverse Feed-Forward Scene Splatting
- 作者：Polina Karpikova, Wenjing Bian, Haofei Xu, Hendrik Lensch, Andreas Geiger
- 出版日期：2026-07-02
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：论文摘要：https://arxiv.org/abs/2607.02301；PDF：https://arxiv.org/pdf/2607.02301

### 一句话总结
本文提出一种前馈多视图逆渲染框架，通过直接预测具有材质属性的结构化3D高斯表示，实现几何、反射率和光照的联合重建。

### 研究问题
现有逆渲染方法中，基于优化的方法虽精度高但需要每场景单独适配，而基于图像空间的学习方法存在多视图不一致、缺乏显式3D表示导致新视角渲染不稳定等问题。本文旨在设计一种前馈式多视图重建方法，在单次前向传播中同时预测几何与物理材质属性。

### 核心思路/方法
1. 采用前馈式多视图重建框架，直接预测结构化的3D高斯表示，每个高斯基元参数化为均值、法线、不透明度、旋转、尺度、反照率、金属度和粗糙度。
2. 将材质估计网络的先验知识与多视图3D重建主干网络结合，实现联合预测几何和反射率参数。
3. 该表示支持可分离的、基于物理的场景表达，从而支持物理渲染和视图依赖效果建模。

### 主要贡献
- 提出前馈式逆渲染框架，可直接预测带有内在材质属性的3D高斯表示。
- 在合成与真实数据集上，相比2D基线方法改善了多视图一致性，可实现准确的材质恢复和稳定的新视角渲染。
- 相比现有基于RGB的前馈重建方法，本表示能更忠实地建模视图依赖效果，并支持基于物理的光照重绘。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦于逆渲染中的前馈式重建，提出将材质属性与几何属性集成到高斯表示中，属于结合神经场景表示与可微渲染的交叉方向。若研究方向涉及新视角合成、材质重建或可重光照，则值得阅读。但摘要未给出定量实验对比或消融分析细节，无法判断实际性能提升幅度。

</details>

<details>
<summary>Abstract</summary>

Inverse rendering aims to recover both 3D geometry and physically meaningful material properties from images, enabling applications such as relighting and novel view synthesis. Optimization-based methods achieve high fidelity but require costly per-scene fitting, while image-space learning-based approaches often suffer from multi-view inconsistencies and lack an explicit 3D representation for stable novel view rendering. We present a feed-forward multi-view reconstruction framework for inverse rendering that directly predicts a structured 3D Gaussian representation with intrinsic material attributes. Each Gaussian primitive is parameterized by mean, normal, opacity, rotation, scale, albedo, metallic, and roughness, enabling a disentangled and physically grounded scene representation. Our model integrates priors from a material estimation network with a multi-view 3D reconstruction backbone, allowing joint prediction of geometry and reflectance parameters in a single forward pass. Experiments on synthetic and real-world datasets demonstrate improved multi-view consistency compared to 2D baselines, accurate material recovery, and stable novel view rendering. Our representation further supports physically-based relighting and more faithful modeling of view-dependent effects compared to existing RGB-based feed-forward reconstruction methods. Our project webpage is: $\href{https://poliik.github.io/invsplat/}{\text{https://poliik.github.io/invsplat/}}$.

</details>

#### 2026-07-02 - A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity

**Authors:** Sujan Kumar Dhali, Bhaskar Dasgupta
**Links:** [abs](https://arxiv.org/abs/2607.02005) - [pdf](https://arxiv.org/pdf/2607.02005)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, pose estimation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity  
- 作者：Sujan Kumar Dhali, Bhaskar Dasgupta  
- 出版日期：2026-07-02  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：摘要：https://arxiv.org/abs/2607.02005；PDF：https://arxiv.org/pdf/2607.02005  

### 一句话总结
本文提出OCD SLAM，一种动态立体视觉SLAM框架，通过结合几何交叉视差滤波与三维目标跟踪，在动态场景中显著提升轨迹精度。

### 研究问题
现有视觉SLAM系统在动态环境中因假设静态世界而容易失效，无法准确处理运动物体对位姿估计和地图构建的影响。

### 核心思路/方法
1. 提出“交叉视差”（cross disparity）概念，利用时间与立体不一致性识别动态特征点。  
2. 集成三维目标检测模块SMOKE与基于卡尔曼滤波的目标跟踪，实现目标级运动分类。  
3. 兼顾特征级（交叉视差）与目标级（3D检测+跟踪）运动分析，分离静态与动态元素，优化位姿估计。

### 主要贡献
1. 提出结合交叉视差的几何动态特征滤波方法，能检测三维目标检测漏检的动点。  
2. 构建融合特征级与目标级运动估计的立体SLAM系统，在KITTI数据集上轨迹精度优于ORB-SLAM2及多个动态SLAM方法。  
3. 通过消融实验验证交叉视差模块的有效性。

### 局限性
摘要未提供足够信息。例如，未提及计算开销、对极度动态场景的鲁棒性、是否依赖特定传感器或数据集条件等具体局限性。

### 阅读优先级
高  
理由：该方法在动态SLAM领域提出了新颖的几何交叉视差概念，实验表明较ORB-SLAM2有明显提升，且消融验证了模块必要性，对动态环境下的SLAM研究有参考价值。

</details>

<details>
<summary>Abstract</summary>

This paper presents OCD SLAM, a dynamic stereo visual SLAM framework that extends ORB-SLAM2 by jointly addressing dynamic objects and dynamic features in the scene. Usual visual SLAM systems operating in dynamic environments often fail in the presence of moving objects, due to the static-world assumption used in pose estimation and mapping. To address this predicament, we introduce a novel geometric approach based on the discrepancy between disparity and a newly proposed notion called ``cross disparity'', which exploits both temporal and stereo inconsistency to identify dynamic feature points. Complementary to this feature-level motion analysis, OCD SLAM integrates a 3D object detection module (SMOKE) with Kalman filter-based object tracking to perform object-level motion classification, enabling robust separation of static and dynamic scene elements for accurate pose estimation. The proposed approach has been evaluated on various sequences from the KITTI Odometry and KITTI Raw datasets. Results demonstrate that OCD SLAM achieves significant improvement in trajectory accuracy compared to ORB-SLAM2 and several state-of-the-art dynamic SLAM methods. Ablation studies further demonstrate the effectiveness of the cross disparity module in the KITTI Raw dataset and show that this method is able to detect dynamic features that are missed by the 3D object detection scheme alone.

</details>

#### 2026-07-02 - Personalized 4D Whole-Heart Mesh Reconstruction from Cine MRI via Multi-Scale Temporal Modeling and Differentiable Contour Rendering

**Authors:** Xiaoyue Liu, Dongcheng Cang, Xiaohan Yuan, Mark YY Chan, Ching-Hui Sia, Lei Li
**Links:** [abs](https://arxiv.org/abs/2607.01952) - [pdf](https://arxiv.org/pdf/2607.01952)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction, rendering, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Personalized 4D Whole-Heart Mesh Reconstruction from Cine MRI via Multi-Scale Temporal Modeling and Differentiable Contour Rendering
- 作者：Xiaoyue Liu, Dongcheng Cang, Xiaohan Yuan, Mark YY Chan, Ching-Hui Sia, Lei Li
- 出版日期：2026-07-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.01952

### 一句话总结
本文提出了一种端到端框架，通过多尺度时间建模和可微分轮廓渲染，从稀疏电影MRI重建个性化的4D全心网格，在低误差和高运动平滑度上优于现有方法。

### 研究问题
如何从稀疏的2D电影MRI切片中准确重建出具有时间分辨率的4D全心网格，以捕捉完整心腔的动态变化和生理合理的运动轨迹。

### 核心思路/方法
1. **端到端图像到网格映射**：直接学习从多视角2D MRI序列到3D+t网格的映射，避免中间轮廓拟合步骤。
2. **可微分轮廓渲染器**：基于比尔-朗伯衰减原理设计，通过轮廓投影损失对3D+t网格形变进行解剖感知监督。
3. **多尺度时间建模模块**：集成全局周期级动态和局部帧间一致性，生成平滑且生理合理的网格轨迹。

### 主要贡献
1. 提出了首个端到端重建时空分辨全心网格的框架，能捕获全心腔动态。
2. 引入了基于比尔-朗伯原理的可微分轮廓渲染器，实现解剖感知的监督。
3. 设计了多尺度时间建模模块，提升了时间一致性和运动平滑度。
4. 实验显示全心的平均绝对误差为1.68 ± 0.31 mm，运动抖动为0.77 ± 0.17 mm/帧³，并改进了2D轮廓对齐，支持下游电生理仿真。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该研究聚焦于医学成像中的4D全心重建，提出了新颖的端到端框架和微分渲染技术，在定量指标和下游应用上均有显著改进，对计算机视觉与医学交叉领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate 4D whole-heart mesh reconstruction from sparse cine MRI is critical for creating cardiac digital twins, but remains challenging due to limited 2D slice coverage and the complex coupling between cardiac shape and motion. Existing methods often rely on intermediate contour fitting and typically reconstruct static, single-phase, or partial cardiac geometries, limiting their ability to capture full-chamber dynamics. We propose a novel end-to-end framework for reconstructing temporally resolved whole-heart meshes from multi-view 2D cine MRI sequences by learning an image-to-mesh mapping. The framework incorporates a differentiable contour renderer inspired by the Beer-Lambert attenuation principle, enabling anatomy-aware supervision of 3D+t mesh deformation through contour-based projection losses. To improve temporal consistency across the cardiac cycle, we further introduce a multi-scale temporal modeling module that integrates global cycle-level dynamics with local inter-frame coherence to generate smooth and physiologically plausible mesh trajectories. The proposed method achieved a whole-heart mean absolute error of 1.68 $\pm$ 0.31 mm and a motion jitter of 0.77 $\pm$ 0.17 $\mathrm{mm}/\mathrm{frame}^{3}$, outperforming existing methods with lower reconstruction error and substantially improved motion smoothness. It also improved 2D contour alignment across multiple cine MRI views and supported downstream proof-of-concept electrophysiological simulation. The code will be released publicly upon acceptance of the manuscript for publication.

</details>

#### 2026-07-02 - FoundDP: Revisiting Weak Disparity Observability in Dual-Pixel Depth Estimation

**Authors:** Fengchen He, Hao Xu, Dayang Zhao, Tingwei Quan, Shaoqun Zeng
**Links:** [abs](https://arxiv.org/abs/2607.01900) - [pdf](https://arxiv.org/pdf/2607.01900)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FoundDP: Revisiting Weak Disparity Observability in Dual-Pixel Depth Estimation
- 作者：Fengchen He, Hao Xu, Dayang Zhao, Tingwei Quan, Shaoqun Zeng
- 出版日期：2026-07-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.01900

### 一句话总结
本文提出FoundDP框架，通过融合双像素（DP）深度与单目深度基础模型的全局结构先验，解决了DP成像中弱视差可观测性导致的深度估计退化问题。

### 研究问题
双像素成像中极小的有效基线限制了视差可观测性，导致在纹理缺失、低对比度或下采样区域出现结构退化与深度失败。现有基于局部视差线索的方法在弱视差信号下不可靠。

### 核心思路/方法
1. 构建统一框架，将具有度量尺度的DP深度与单目深度基础模型的全局结构先验结合。
2. 利用DP深度维持度量尺度，并借助Vision Transformer（ViT）特征恢复弱视差区域的结构一致性。
3. 识别并缓解DP离焦模糊导致的ViT表征退化问题，通过ViT特征对齐实现稳定的度量引导深度估计。

### 主要贡献
- 提出了整合DP度量深度与单目全局先验的统一框架FoundDP，有效处理弱视差条件下的深度估计难题。
- 揭示了DP离焦模糊对ViT表征的负面影响，并设计了特征对齐策略以消除该退化。
- 在合成与真实DP基准上验证了方法的优越性，尤其是在结构保真度和度量精度上获得一致提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦于双像素深度估计中的特殊难点（弱视差可观测性），属于图像传感器与深度估计的交叉方向。若读者从事计算摄影、3D重建或传感器融合相关研究，可优先阅读。但该方法高度依赖DP成像硬件和预训练的ViT模型，通用性范围有限。

</details>

<details>
<summary>Abstract</summary>

Dual-pixel (DP) imaging enables metric depth estimation from a single camera using sub-aperture disparity. However, the extremely small effective baseline limits disparity observability, leading to structural degradation and depth failure in textureless, low-contrast, or downsampled regions. Existing DP-based methods rely primarily on local disparity cues and therefore become unreliable when disparity signals are weak or ambiguous. To address this limitation, we propose \emph{FoundDP}, a unified framework that integrates metric DP depth with global structural priors from a monocular depth foundation model. Our method preserves metric scale through DP-derived depth and leverages Vision Transformer (ViT) features to restore structural consistency in weak-disparity regions. To ensure reliable metric guidance under DP imaging conditions, we identify and mitigate ViT representation degradation induced by DP defocus blur via ViT feature alignment, enabling stable metric-guided depth estimation. Extensive experiments on synthetic and real-world DP benchmarks show that FoundDP delivers superior performance, with consistent gains in structural fidelity and metric accuracy, especially under reduced disparity observability. Code will be available at: https://github.com/EchoLighting/FoundDP

</details>

#### 2026-07-02 - DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability

**Authors:** Ziheng Xu, Qingfeng Li, Xuefeng Liu, Chen Chen, Jianwei Niu
**Links:** [abs](https://arxiv.org/abs/2607.01860) - [pdf](https://arxiv.org/pdf/2607.01860)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** simultaneous localization and mapping, SLAM, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability
- 作者：Ziheng Xu, Qingfeng Li, Xuefeng Liu, Chen Chen, Jianwei Niu
- 出版日期：2026-07-02T08:18:23Z
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：arXiv 摘要：https://arxiv.org/abs/2607.01860；PDF：https://arxiv.org/pdf/2607.01860

### 一句话总结
提出一种基于双层概率框架的单目高斯溅射SLAM系统DL-SLAM，通过融合语义与几何信息计算动态概率，实现高质量静态地图构建与精确鲁棒的相机追踪。

### 研究问题
现有基于3D高斯溅射的稠密动态SLAM方法在处理动态物体时，要么直接丢弃静态物体（忽略其几何约束价值），要么使用逐像素不确定性地图导致瞬态静态物体被错误融入静态地图产生伪影，且纯几何信息的边界模糊。

### 核心思路/方法
1. 构建双层概率框架：先结合语义和几何信息生成逐像素动态概率图。
2. 将像素级概率提升至3D并聚合，为每个实例计算物体级动态概率。
3. 基于物体级概率对动态高斯体进行分类剪枝，获得无伪影的静态地图。
4. 利用静态地图提供的几何一致性指导，反过来优化逐像素概率，形成闭环反馈。

### 主要贡献
- 提出DL-SLAM，一种在动态场景下实现高保真高斯溅射SLAM的新方法。
- 创新性地设计双层概率机制，同时利用瞬态静态物体的几何约束并避免静态地图伪影。
- 实验证明相比现有方法，追踪精度最高提升13%，并生成高保真语义地图。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法有效解决了动态SLAM中瞬态物体利用与静态地图保真性的关键矛盾，且在跟踪精度上有显著提升（13%），对从事动态场景3D重建或SLAM的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D Gaussian Splatting (3DGS) have enabled significant progress in dense dynamic Simultaneous Localization And Mapping (SLAM). Prevailing methods typically discard predefined dynamic objects, ignoring that transiently static objects offer valuable geometric constraints for pose estimation. A recent work attempts to leverage this potential by employing per-pixel uncertainty maps to quantify the magnitude of motion. While this approach enables transiently static objects to enhance pose estimation, it erroneously integrates these objects into the static map, resulting in persistent artifacts. Moreover, its reliance on purely geometric information leads to ambiguous object boundaries in the uncertainty maps. To overcome these limitations, we present DL-SLAM, a monocular Gaussian Splatting SLAM system built upon a novel dual-level probabilistic framework. Our method computes dynamic probability maps by combining semantic and geometric information. These pixel-level probabilities are lifted to 3D and aggregated to derive an object-level dynamic probability for each instance. Object-level probability enables the categorical pruning of dynamic Gaussians, resulting in an artifact-free static map. The static map, in turn, provides a geometrically consistent guidance to refine the pixel-wise probabilities, enhancing their reliability. Experimental results demonstrate that DL-SLAM outperforms existing approaches, improving tracking accuracy by up to 13\% while generating high-fidelity semantic maps.

</details>

#### 2026-07-02 - The Turning Point of 3D Plant Phenotyping: 3D Foundation Models Enable Minute-to-Second Cross-Crop Reconstruction and Beyond

**Authors:** Hanyue Jia, Wei Zhou, Wenbo Zhou, Yanan Li, Hao Lu, Tingting Wu
**Links:** [abs](https://arxiv.org/abs/2607.01753) - [pdf](https://arxiv.org/pdf/2607.01753)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, dense reconstruction, Gaussian Splatting, 3D Gaussian Splatting, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Turning Point of 3D Plant Phenotyping: 3D Foundation Models Enable Minute-to-Second Cross-Crop Reconstruction and Beyond
- 作者：Hanyue Jia, Wei Zhou, Wenbo Zhou, Yanan Li, Hao Lu, Tingting Wu
- 出版日期：2026-07-02
- 分类：3D Reconstruction & Multi-view Geometry (主要); Neural Scene Representations & Rendering (次要)
- 链接：arXiv:2607.01753 (摘要: https://arxiv.org/abs/2607.01753, PDF: https://arxiv.org/pdf/2607.01753)

### 一句话总结
本文提出一个基于3D基础模型(3DFMs)的跨作物3D表型分析框架，将传统耗时数分钟的重建流程压缩至1.58秒，在保持高精度前提下实现高通量植物表型重建。

### 研究问题
如何利用3D基础模型简化传统3D植物表型分析中繁琐、低通量的重建流程，使其在低成本数据采集（如手机视频、稀疏多视角图像）条件下也能实现快速、准确的重建和表型提取。

### 核心思路/方法
1. **用3DFM替换COLMAP初始化**：采用基于3D基础模型的馈送式几何恢复替代传统COLMAP的稀疏初始化步骤。
2. **几何约束的3D高斯泼溅**：结合几何约束进行密集重建。
3. **少视角重建策略**：通过迭代视图合成与精炼实现仅用少量视图即可重建。
4. **2D到3D语义迁移**：利用2D语义信息完成度量尺度恢复和器官实例分离，将重建几何转化为可测量的器官。
5. **构建跨作物数据集**：包含手机采集的图像、多种植物形态及人工标注，用于分割和表型评估。

### 主要贡献
1. 提出首个结合3D基础模型的跨作物3D表型分析框架，显著简化传统重建管线。
2. 将平均重建时间从6.52分钟降至1.58秒（加速约247倍），同时保持高质量重建和表型精度。
3. 在26个植物序列上验证了从低成本图像采集到快速重建、感知、尺度恢复和表型测量的完整技术路线。

### 局限性
摘要未提供足够信息（未讨论框架在极端遮挡、复杂背景或不同光照条件下的鲁棒性，也未提及计算资源消耗或失败案例）。

### 阅读优先级
**高**  
**理由**：该工作提出将3D基础模型应用于植物表型领域，实现了数量级的速度提升，且方法具有跨作物通用性，对高通量植物表型研究有显著启发意义。摘要报告了具体量化指标（时间、序列数），结果可信度高，适合重点关注。

</details>

<details>
<summary>Abstract</summary>

3D plant phenotyping is notoriously known to be procedure-complicated and of low throughput due to the extensive multi-view imaging, the fragile 3D reconstruction pipeline, and the additional cost from reconstructed geometry to phenotypic extraction. These limitations are further amplified in low-cost data acquisition, where smartphone videos or sparsely sampled multi-view images provide limited view overlap and self-occlusion. In this work, we show that the conventional 3D plant phenotyping pipeline could be streamlined and significantly accelerated with 3D Foundation Models (3DFMs), and particularly, present one of the first cross-crop 3D phenotyping frameworks powered by 3DFMs. The framework replaces COLMAP-style sparse initialization with 3DFM-based feed-forward geometric recovery, combines geometry-constrained 3D Gaussian Splatting for dense reconstruction, enables few-view reconstruction through iterative view synthesis and refinement, and converts reconstructed geometry into measurable organs through 2D-to-3D semantic transfer, metric scale recovery, and organ instance separation. We further construct a cross-crop dataset with smartphone-based image acquisition, diverse plant morphologies, and manual annotations for segmentation and phenotypic evaluation. Experiments across 26 plant sequences show that 3D Foundation Models reduce the average reconstruction time from 6.52 minutes to 1.58 seconds while maintaining high reconstruction quality and phenotyping accuracy. These results suggest a fresh technical route for high-throughput 3D plant phenotyping, from low-cost image acquisition to fast reconstruction, perception, scale recovery, and phenotypic measurement.

</details>

#### 2026-07-02 - Structure-Aware Gaussian Splatting for Large-Scale Scene Reconstruction

**Authors:** Weiyi Xue, Fan Lu, Chi Zhang, Tianhang Wang, Sanqing Qu, Zehan Zheng, Boyuan Zheng, Junqiao Zhao, Guang Chen
**Links:** [abs](https://arxiv.org/abs/2607.01698) - [pdf](https://arxiv.org/pdf/2607.01698)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Structure-Aware Gaussian Splatting for Large-Scale Scene Reconstruction
- 作者：Weiyi Xue, Fan Lu, Chi Zhang, Tianhang Wang, Sanqing Qu, Zehan Zheng, Boyuan Zheng, Junqiao Zhao, Guang Chen
- 出版日期：2026-07-02
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.01698

### 一句话总结
本文针对3D高斯泼溅在大规模场景重建中因稀疏观测区域导致冗余原语和效率下降的问题，提出了一种信号结构感知调度策略SIG和球面约束高斯，以实现频率一致、几何感知且无漂浮物的训练，在大规模场景中显著提升了效率与渲染质量。

### 研究问题
如何解决3D高斯泼溅方法在大规模场景中因初始点过于稀疏，导致高斯原语不受控制的稠密化和冗余，进而降低重建效率与质量的问题。

### 核心思路/方法
- 从信号结构恢复的角度重新定义场景重建问题，提出SIG调度器，通过推导3D表示的采样频率和带宽，根据场景频率收敛情况动态调节训练图像分辨率和高斯稠密化过程。
- 引入Sphere-Constrained Gaussians（球面约束高斯），利用初始化点云的空间先验来约束高斯优化，抑制漂浮物产生。
- 整体框架确保频率一致、几何感知且无漂浮物训练，兼顾效率与渲染质量。

### 主要贡献
- 重新分析并指出稀疏观测区域中低频初始化点与高频图像监督之间的不匹配是效率和质量下降的关键原因。
- 提出SIG调度器，实现图像监督频率与高斯频率的同步调节，避免硬编码调度策略的局限性。
- 引入球面约束高斯，利用点云空间先验控制优化过程。
- 在大规模场景重建任务中，相比现有方法在效率和渲染质量方面均取得显著提升。

### 局限性
摘要未提供足够信息。原文未讨论方法的潜在局限性，例如对不同类型场景（如极端稀疏或动态场景）的适应性、计算资源消耗等具体细节。

### 阅读优先级
高  
理由：该论文针对3D高斯泼溅在大规模场景中实际部署的关键瓶颈（稀疏区域冗余与效率低下）提出原创性解决方案，思路新颖（信号结构恢复视角+自适应调度），能够大幅提升大规模重建的实用性与质量，且论文给出了开源代码，对从事3D重建和渲染方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has demonstrated remarkable potential in novel view synthesis. In contrast to small-scale scenes, large-scale scenes inevitably contain sparsely observed regions with excessively sparse initial points. In this case, supervising Gaussians initialized from low-frequency sparse points with high-frequency images often induces uncontrolled densification and redundant primitives, degrading both efficiency and quality. Intuitively, this issue can be mitigated with scheduling strategies, which can be categorized into two paradigms: modulating target signal frequency via densification and modulating sampling frequency via image resolution. However, previous scheduling strategies are primarily hardcoded, failing to perceive the convergence behavior of scene frequency. To address this, we reframe the scene reconstruction problem from the perspective of signal structure recovery and propose SIG, a novel scheduler that synchronizes image supervision with Gaussian frequencies. Specifically, we derive the average sampling frequency and bandwidth of 3D representations, and then regulate the training image resolution and the Gaussian densification process based on scene frequency convergence. Furthermore, we introduce Sphere-Constrained Gaussians, which leverage the spatial prior of initialized point clouds to control Gaussian optimization. Our framework enables frequency-consistent, geometry-aware, and floater-free training, achieving state-of-the-art performance by a substantial margin in both efficiency and rendering quality in large-scale scenes. The code is available at: https://github.com/weiyixue999/Signal_Structure_Aware_Gaussian

</details>

#### 2026-07-02 - ICDepth: Taming Video Diffusion Models for Video Depth Estimation via In-Context Conditioning

**Authors:** Xuanhua He, Jiaxin Xie, Mingzhe Zheng, Qifeng Chen
**Links:** [abs](https://arxiv.org/abs/2607.01677) - [pdf](https://arxiv.org/pdf/2607.01677)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ICDepth: Taming Video Diffusion Models for Video Depth Estimation via In-Context Conditioning
- 作者：Xuanhua He, Jiaxin Xie, Mingzhe Zheng, Qifeng Chen
- 出版日期：2026-07-02T04:05:17Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.01677

### 一句话总结
本文提出ICDepth框架，通过将预训练文本到视频扩散模型适配为视频深度估计器，利用上下文条件（In-Context Conditioning）和两项关键技术，在仅使用80万帧数据训练的情况下，达到了多基准测试的领先性能和强零样本泛化能力。

### 研究问题
现有单目视频深度估计方法难以同时实现时序一致性、几何精度和跨场景泛化：判别式模型虽逐帧精度高但易出现时序漂移，生成式模型虽一致性强但需超1000万样本训练且几何精度不足。因此，研究如何利用视频扩散模型固有的时空先验，以高效数据实现高性能深度估计。

### 核心思路/方法
1. **整体框架**：将预训练文本到视频扩散变换器（Video Diffusion Transformers）改造为深度估计模型，采用**上下文条件（In-Context Conditioning, ICC）** 机制，直接复用扩散模型丰富的时空先验。
2. **SAND-Attention**：通过共享旋转位置编码（RoPE）保证精确时空对齐，并施加单向注意力以防止噪声污染。
3. **SRFM**：注入DINOv2的语义和分辨率先验，以增强几何精度。

### 主要贡献
- 首次将上下文条件（ICC）从生成任务迁移到密集预测型视频深度估计，并解决迁移中的关键挑战。
- 设计SAND-Attention实现时空精确对齐并防御噪声干扰，SRFM模块提升几何精度。
- 仅用80万帧（0.8M）训练数据（是竞争生成式方法的1/6至1/13），即在多个基准上达到领先性能，并展现强大的零样本跨域泛化能力。

### 局限性
摘要未提供足够信息。摘要中未讨论方法存在的具体限制或失败案例。

### 阅读优先级
**高**  
理由：方法创新性较强（迁移视频扩散模型至密集预测任务），数据效率显著优于现有生成式方法，且性能领先多个基准；适用于关注视频深度估计、扩散模型应用或高效训练的研究者。技术细节（SAND-Attention、SRFM）具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular video depth estimation requires temporal consistency, geometric accuracy, and generalization across diverse scenarios, yet existing methods struggle to achieve all three simultaneously. Discriminative models excel at per-frame accuracy but suffer from temporal drift due to limited context windows, while generative methods improve consistency and generalization at the cost of extensive training data (10M+ samples) and lack of geometric precision. In response to these issues, we introduce \textbf{ICDepth}, a framework that adapts pre-trained text-to-video diffusion transformers for video depth estimation via In-Context Conditioning (ICC), leveraging their rich spatial-temporal priors. To address key challenges in transferring ICC from generation to dense prediction, we propose: (1)~\textbf{SAND-Attention}, which ensures precise spatial-temporal alignment via shared RoPE and enforces unidirectional attention to prevent noise contamination; (2)~\textbf{SRFM}, which injects DINOv2 semantic and resolution priors to enhance geometric precision. ICDepth achieves state-of-the-art results on multiple benchmarks with remarkable data efficiency, trained on only 0.8M frames ($6$--$13\times$ less than competing generative methods), while demonstrating strong zero-shot generalization to diverse domains.

</details>

#### 2026-07-02 - Multi-THuMBS: Multi-person Tracking of 3D Human Meshes Beyond Video Shots

**Authors:** Jeongwan On, Muhammad Salman Ali, Muneeb A. Khan, Sunwoo Park, Inwoong Moon, Hyung Jin Chang, Jaekwang Kim, Seong Jong Ha, Seungryul Baek
**Links:** [abs](https://arxiv.org/abs/2607.01626) - [pdf](https://arxiv.org/pdf/2607.01626)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** motion reconstruction, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-THuMBS: Multi-person Tracking of 3D Human Meshes Beyond Video Shots
- 作者：Jeongwan On, Muhammad Salman Ali, Muneeb A. Khan, Sunwoo Park, Inwoong Moon, Hyung Jin Chang, Jaekwang Kim, Seong Jong Ha, Seungryul Baek
- 出版日期：2026-07-02T02:48:43Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.01626

### 一句话总结
提出了一种名为Multi-THuMBS的方法，利用3D场景先验在视频镜头切换处重建共享3D空间中的边界帧，从而在多人场景下实现跨镜头的一致身份跟踪和3D人体网格恢复。

### 研究问题
现有3D人体网格跟踪方法在应对现实视频中频繁的镜头切换（shot changes）时，容易丢失人体身份信息且无法重建时间上连贯的轨迹；同时，已有的跨镜头跟踪工作仅限于单人场景，不适用于多人交互的真实视频。

### 核心思路/方法
利用最先进的3D场景先验（3D scene prior），将镜头切换处的两个边界帧（boundary frames）重建到同一共享3D空间中；然后在该共享空间内注册所有人体网格，从而保持每个人的身份一致性和跨镜头的运动连贯性。

### 主要贡献
- 针对视频镜头切换下的多人3D人体网格跟踪问题，提出了Multi-THuMBS方法。
- 通过共享3D空间重建和人体网格注册，实现了跨镜头的身份跟踪与运动一致性保持。
- 实验表明，该方法在3D人体网格恢复、相机位姿估计和身份跟踪方面均优于现有方法，确保了高保真的运动重建和身份一致性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作聚焦于视频镜头切换这一具体场景下的多人3D人体跟踪问题，方法新颖且实验效果显著改善。对于从事视频人体分析、3D重建或多目标跟踪的研究者具有参考价值，但若研究兴趣不涉及跨镜头场景，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Tracking multi-person 3D human meshes from in-the-wild videos is a highly challenging problem due to complex interactions, frequent occlusions, and severe truncation inherent in unconstrained environments. While recent approaches have improved robustness against these issues, they largely overlook the critical challenge prevalent in real-world footage: frequent shot changes. These abrupt transitions in camera viewpoints often cause existing methods to lose track of human identities and fail in reconstructing temporally coherent trajectories. Although several recent works have explored 3D human mesh tracking under shot changes, they are still limited to single-person scenarios, making them inadequate for real-world videos where multiple people interact and appear simultaneously. To address this limitation, we propose Multi-THuMBS (Multi-person Tracking of 3D Human Meshes Beyond Video Shots) that leverages a state-of-the-art 3D scene prior to reconstruct the two boundary frames in a single shared 3D space. Human meshes are then registered within the shared 3D space, maintaining per-person identity and motion consistency across shot changes. Extensive experiments demonstrate that our approach yields significant improvements in 3D human mesh recovery, camera pose estimation, and identity tracking, thereby ensuring high-fidelity motion reconstruction with consistent identity preservation across shots compared to previous state-of-the-art methods.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-07 - GaussFusion: Towards Multimodal 3D Gaussian Pretraining

**Authors:** Zhixuan You, Jihua Zhu, Yiding Sun, Zihao Guo, Haozhe Cheng, Dongxu Zhang, Lin Chen, Hainan Luo
**Links:** [abs](https://arxiv.org/abs/2607.05906) - [pdf](https://arxiv.org/pdf/2607.05906)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

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

#### 2026-07-02 - Learning Spectral and Polarimetric Clues for One-to-Multimodal Novel View Synthesis

**Authors:** Federico Lincetto, Gianluca Agresti, Mattia Rossi, Piergiorgio Sartor, Pietro Zanuttigh
**Links:** [abs](https://arxiv.org/abs/2607.02372) - [pdf](https://arxiv.org/pdf/2607.02372)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural rendering, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Spectral and Polarimetric Clues for One-to-Multimodal Novel View Synthesis
- 作者：Federico Lincetto, Gianluca Agresti, Mattia Rossi, Piergiorgio Sartor, Pietro Zanuttigh
- 出版日期：2026-07-02
- 分类：Neural Scene Representations & Rendering
- 链接：arXiv:2607.02372

### 一句话总结
本文提出了一种名为SPoILeR的方法，在仅需少量或无需非常规模态（如红外、偏振、多光谱）输入的情况下，通过多模态预训练学习模态间的相关性，并由RGB图像监督微调，实现对多模态场景的新视图合成。

### 研究问题
如何在没有或仅有极少数非常规成像模态（红外、偏振、多光谱）样本的场景中，实现对这些模态的多视角一致渲染。

### 核心思路/方法
1.  **多模态预训练阶段**：模型学习不同成像模态（如RGB与红外、偏振、多光谱）之间的相互关联性。
2.  **微调阶段**：在仅由RGB图像监督的条件下，利用预训练获得的相关性知识，预测并渲染出其他非常规模态的准确图像。

### 主要贡献
- 提出了SPoILeR方法，能够在仅依赖RGB帧或极少额外模态数据的情况下，生成多模态视图一致的渲染结果。
- 通过多模态预训练，模型学会了模态间的共性与相关性，从而在微调阶段无需昂贵传感器捕获的完整多模态样本即可工作。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：方法解决了多模态神经渲染中数据采集成本高的实际问题，具有较强的应用潜力。但摘要未提供实验的具体量化指标（如PSNR/SSIM对比），也未讨论方法在复杂场景下的性能边界和失败情况，因此暂不列为最高优先级。

</details>

<details>
<summary>Abstract</summary>

Neural rendering techniques allow for accurate reconstruction of the geometry and color appearance of 3D scenes. Some methods have extended their use to additional imaging modalities, such as multispectral, infrared, or polarimetric data. However, all of these approaches require expensive sensors and calibrated setups to capture new multimodal frames for each new scene. We propose Spectral and Polarimetric Implicit Learned Representation (SPoILeR), a novel method to obtain multi-view consistent renderings of unconventional modalities for scenes where either only RGB frames or very few of the additional modalities are available. Thanks to a multimodal pre-training phase, the model learns the mutual correlation between different modalities. This step allows predicting accurate renderings of unconventional modalities during a fine-tuning phase supervised only by RGB images. Experimental results show that the approach can accurately render infrared, polarimetric, and multispectral frames for scenes where no input sample captured by these types of sensors is provided.

</details>

#### 2026-07-02 - NeoMap: Training-free Novel-View Synthesis from Single Images and Videos

**Authors:** Jinxi Li, Tianyi Zhang, Yafei Yang, Zihui Zhang, Peng Huang, Koon Wing Macgyver Lin, Bo Yang
**Links:** [abs](https://arxiv.org/abs/2607.01962) - [pdf](https://arxiv.org/pdf/2607.01962)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NeoMap: Training-free Novel-View Synthesis from Single Images and Videos
- 作者：Jinxi Li, Tianyi Zhang, Yafei Yang, Zihui Zhang, Peng Huang, Koon Wing Macgyver Lin, Bo Yang
- 出版日期：2026-07-02
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2607.01962；PDF：https://arxiv.org/pdf/2607.01962

### 一句话总结
NeoMap提出一种免训练框架，通过流形交替投影迭代从预训练视频模型中定位高保真、视图一致的新视角合成结果。

### 研究问题
如何从单张图像或单目视频中，无需微调或条件对齐，实现高质量且全局一致的新视角视频合成。

### 核心思路/方法
核心思路是：预训练视频模型本身已编码了新视角解在自然视频数据流形中的分布，关键仅在于定位最优解。方法采用**收敛流形交替投影迭代**（核心机制）优化初始噪声，从而直接利用预训练模型生成新视角。

### 主要贡献
1. 提出NeoMap，首个免训练的新视角合成框架，无需相机条件、微调或逐帧硬去噪引导。
2. 揭示预训练视频模型内在具备新视角生成能力，并将问题转化为流形优化。
3. 在Tanks-and-Temples、LLFF和DAVIS三个标准基准上，取得领先生成保真度和视图一致性。

### 局限性
摘要未提供足够信息。未讨论方法的失败案例、计算开销或对输入视频/图像质量的敏感性。

### 阅读优先级
**高**。理由：该工作提出一种免训练方法，直接利用预训练视频模型的主流技术路线，在多个标准基准上取得领先性能，且方法论（流形优化）具有通用性，适合关注新视角合成、视频生成的研究者快速跟进。

</details>

<details>
<summary>Abstract</summary>

We study the challenging problem of novel view video synthesis from single images or monocular videos. Existing methods, which operate under the assumption that pre-trained video models lack native novel view synthesis capability and enforce view alignment via camera conditioning, task-specific fine-tuning, or stepwise hard denoising guidance, often suffer from artifacts and compromised global scene consistency. In this paper, we introduce NeoMap, a novel training-free framework designed to locate high-fidelity, view-consistent novel view solutions from general pre-trained video models. The key to our approach is the core insight that promising novel view solutions are inherently encoded within the natural video data manifold learned by pre-trained models, and the core challenge is simply to locate this optimal solution. We solve this via our core mechanism: convergent manifold alternating projection iterations that optimize the initial noise. Extensive experiments demonstrate that NeoMap significantly outperforms all existing methods across 3 standard novel view synthesis benchmarks, including the challenging Tanks-and-Temples, LLFF and DAVIS datasets, achieving state-of-the-art generation fidelity and top-tier view consistency.

</details>

#### 2026-07-02 - Consistent Scene Understanding in 3D Gaussian Splatting via Multi-Cue Mask Refinement

**Authors:** Hyunjoon Park, Donghyeon Cho
**Links:** [abs](https://arxiv.org/abs/2607.01708) - [pdf](https://arxiv.org/pdf/2607.01708)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Consistent Scene Understanding in 3D Gaussian Splatting via Multi-Cue Mask Refinement
- 作者：Hyunjoon Park, Donghyeon Cho
- 出版日期：2026-07-02
- 分类：Neural Scene Representations & Rendering (主), Embodied / Robotics / AR Applications (辅)
- 链接：https://arxiv.org/abs/2607.01708

### 一句话总结
本文提出一个多线索掩码精炼框架，用于在3D高斯泼溅(3DGS)中生成跨视图一致的2D实例掩码，从而提升3D场景理解的稳定性和一致性。

### 研究问题
当前的基于2D基础分割模型的场景理解方法在3D高斯泼溅中会产生碎片化的掩码和跨视图不一致的预测，如何实现跨视图一致的实例级场景理解？

### 核心思路/方法
提出一个三阶段框架：1) 多线索提取：从输入图像中生成协同的语义、几何和结构先验；2) 多线索引导的掩码合并：利用由语义、深度和边缘线索导出的复合合并分数，整合碎片化掩码；3) 跨视图掩码匹配：在所有视角间建立全局一致的身份分配，并将视角特定的片段转化为连贯的3D图元，从而稳定3D实例分割和下游编辑任务。

### 主要贡献
1. 提出了一个多线索掩码精炼框架，解决了2D分割模型在3DGS中跨视图不一致和碎片化问题。
2. 设计了多线索引导的掩码合并策略，有效整合碎片化掩码。
3. 通过跨视图掩码匹配实现全局一致的身份分配，显著提升了跨视图一致性和分割稳定性，同时保持了高保真光度重建。

### 局限性
摘要未提供足够信息。未提及实验中的具体失败案例、场景限制（如动态物体、光照变化）、计算开销或对某些类型场景的适用性边界。

### 阅读优先级
中。理由：该工作针对3DGS中实例分割一致性的具体问题提出新框架，方法新颖且实验表明有效。但对摘要中未披露的细节（如具体性能数值、与更多方法的对比、鲁棒性测试等）缺乏了解，因此暂不列为高优先级。若您正从事3D场景理解或3DGS相关工作，可进一步阅读。

</details>

<details>
<summary>Abstract</summary>

Reliable instance-level scene understanding is a fundamental prerequisite for object-level interactions and high-fidelity 3D representations. While current methods often leverage 2D foundation segmentation models to obtain these priors, their 2D-centric design typically yields fragmented masks and inconsistent predictions across different views. To address these issues, we propose a novel framework that produces consistent 2D instance masks to guide the optimization of 3D Gaussian Splatting (3DGS) feature fields. Our framework consists of three main stages. (1) Multi-Cue Extraction that generates synergistic semantic, geometric, and structural priors from input images. (2) Multi-Cue-Guided Mask Merging process that consolidates fragmented masks using a composite merge score derived from semantic, depth, and edge cues. (3) Cross-View Mask Matching that establishes globally consistent identity assignments across all viewpoints. By transforming viewpoint-specific segments into coherent 3D primitives, our approach enables stable 3D instance segmentation and effective downstream editing tasks. Experiments demonstrate that our method significantly improves cross-view consistency and segmentation stability over existing baselines while maintaining high-fidelity photometric reconstruction.

</details>

#### 2026-07-02 - Bridging 3D Gaussians and Semantic Occupancy for Comprehensive Open-Vocabulary Scene Understanding from Unposed Images

**Authors:** Hu Zhu, Bohan Li, Xianda Guo, Yanlun Peng, Zheng Zhu, Xin Jin, Wenjun Zeng, Chang Wen Chen
**Links:** [abs](https://arxiv.org/abs/2607.01633) - [pdf](https://arxiv.org/pdf/2607.01633)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** camera calibration, novel view synthesis, view synthesis, rendering, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- **标题**：Bridging 3D Gaussians and Semantic Occupancy for Comprehensive Open-Vocabulary Scene Understanding from Unposed Images
- **作者**：Hu Zhu, Bohan Li, Xianda Guo, Yanlun Peng, Zheng Zhu, Xin Jin, Wenjun Zeng, Chang Wen Chen
- **出版日期**：2026-07-02
- **分类**：Neural Scene Representations & Rendering（主类别）；Embodied / Robotics / AR Applications（副类别）
- **链接**：Abstract: https://arxiv.org/abs/2607.01633 , PDF: https://arxiv.org/pdf/2607.01633

### 一句话总结
该论文提出COVScene，一个无需相机位姿的语义高斯框架，将可渲染的高斯基元与稠密语义占用场通过可微分体素提升过程耦合，实现从稀疏、无位姿图像中恢复可渲染几何、开放词汇语义和占用空间。

### 研究问题
如何从稀疏且无外参标定的图像中，实现包含可渲染几何、开放词汇语义以及自由/占用三维空间的综合场景理解。

### 核心思路/方法
1. **耦合高斯与占用场**：通过可微分体素提升（volumetric lifting），在训练计算图中将预测的语义高斯基元提升为稠密语义占用场，使体素正则化能直接为高斯的不透明度、几何和语义特征提供梯度。
2. **多任务架构**：包含语义感知的几何Transformer、多任务高斯解码、几何基础模型蒸馏以及占用熵正则化。
3. **单一表示支持多个任务**：在单个表示中同时支持新视角合成、开放词汇语义查询和语义占用预测。

### 主要贡献
- 提出COVScene，首个将可渲染高斯基元与稠密语义占用场紧密结合的无位姿语义高斯框架。
- 引入可微分体素提升机制，在训练中对高斯参数施加体积正则化，提升未观测区域约束。
- 通过实验（ScanNet和ScanNet++）表明：在保持竞争力渲染质量的同时，提升了开放词汇分割性能，并在无直接体素监督下实现了更强的语义占用预测。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该方法聚焦于无位姿场景理解中的高斯-占用耦合技术，对NeRF/Gaussian Splatting及开放词汇语义领域有参考价值，但实验仅与自监督基线对比，且缺乏与现有最先进方法的详细比较，创新性中等。适合相关方向研究者阅读，非核心领域可暂缓。

</details>

<details>
<summary>Abstract</summary>

Comprehensive 3D scene understanding from sparse, unposed images requires a model to recover renderable geometry, open-vocabulary semantics, and free/occupied 3D space without relying on external camera calibration. Recent feed-forward Gaussian methods improve pose-free reconstruction and semantic rendering, but their Gaussian primitives are mainly optimized through image-space objectives and remain weakly constrained in unobserved regions. We propose \textit{COVScene}, a pose-free semantic Gaussian framework that couples renderable Gaussian primitives with a dense semantic occupancy field through differentiable volumetric lifting. Instead of converting Gaussians to voxels only at evaluation time, COVScene lifts the predicted semantic Gaussians inside the training computation graph, so volumetric regularization provides gradients to Gaussian opacity, geometry, and semantic features. The framework combines a semantic-aware Geometry Transformer, multi-task Gaussian decoding, geometric foundation distillation, and occupancy entropy regularization to support novel view synthesis, open-vocabulary semantic querying, and semantic occupancy prediction within a single representation. Experiments on ScanNet and ScanNet++ show that COVScene maintains competitive rendering quality, improves open-vocabulary segmentation, and achieves stronger semantic occupancy prediction than the self-supervised baseline without direct voxel-level supervision.

</details>

#### 2026-07-02 - Online Segment 3D Gaussians via Launching Virtual Drones

**Authors:** Liwei Liao, Rongjie Wang, Ronggang Wang
**Links:** [abs](https://arxiv.org/abs/2607.01628) - [pdf](https://arxiv.org/pdf/2607.01628)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Online Segment 3D Gaussians via Launching Virtual Drones  
- 作者：Liwei Liao, Rongjie Wang, Ronggang Wang  
- 出版日期：2026-07-02  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2607.01628  

### 一句话总结
提出SAGO框架，通过虚拟无人机将3D分割问题转化为在线Next-Best-View规划任务，首次实现无需预设置的亚秒级交互式3D高斯分割。

### 研究问题
如何消除现有交互式3D高斯分割（3DGS）方法中耗时的预设置阶段（如多视角掩码准备、掩码提升、特征蒸馏），同时保持在线分割的实时性（亚秒级）。

### 核心思路/方法
1. **零预设置设计**：完全去除分割前的场景特定准备步骤，直接对原始3DGS场景进行交互分割。  
2. **虚拟无人机引入**：将3D分割问题重新定义为马尔可夫过程中的在线Next-Best-View（NBV）规划任务，通过虚拟无人机动态选择最佳视角。  
3. **在线处理**：在用户交互后，以亚秒级延迟直接提取干净的3D资产，无需离线阶段。

### 主要贡献
1. 首次提出无需预设置的交互式3DGS分割框架，突破现有方法“预设置分钟级+交互秒级”的瓶颈。  
2. 将3D分割与NBV规划结合，利用虚拟无人机高效在线提取3D资产。  
3. 在多种下游任务（目标操作、场景编辑）中验证有效性，且相比先前无预设置方法实现超50倍加速。

### 局限性
摘要未提供足够信息，无法分析具体局限性，如对复杂场景的鲁棒性、虚拟无人机规划的计算开销或分割精度边界。

### 阅读优先级
**高**  
理由：该方法解决了3DGS交互分割中预设置耗时的核心痛点，提出新颖的虚拟无人机NBV规划策略，且加速比显著（>50x），对实时3D场景编辑与操作有重要应用价值。

</details>

<details>
<summary>Abstract</summary>

Interactive segmentation of 3D Gaussians offers a compelling opportunity for real-time manipulation of 3D scenes, thanks to the real-time rendering capability of 3D Gaussian Splatting (3DGS). However, existing methods require a time-consuming per-scene setup - typically tens of seconds or even minutes - before interactive segmentation can begin on a raw 3DGS scene. This setup involves multi-view mask preparation, mask lifting, and feature distillation, creating a major bottleneck for online applications. To address this limitation, we aim to completely eliminate the setup stage for interactive 3DGS segmentation while keeping the segmentation time practical (under 1 second). In this work, we present SAGO (Segment Any Gaussians Online), a novel setup-free framework for interactive 3DGS segmentation. By introducing virtual drones, our method reframes the 3D segmentation problem as an online Next-Best-View (NBV) planning task formulated within a Markov process. Extensive experiments demonstrate that SAGO can extract clean 3D assets directly from 3D Gaussians with sub-second latency, thereby enabling a broad range of downstream applications such as object manipulation and scene editing. Moreover, our method achieves over a 50x speedup compared to the previous setup-free 3DGS segmentation frameworks.

</details>

#### 2026-07-02 - Mind the Gap: Standard 3DGS Evaluation Primarily Measures Near-Trajectory Interpolation

**Authors:** Gaoxiang Jia, Vikram Appia
**Links:** [abs](https://arxiv.org/abs/2607.01556) - [pdf](https://arxiv.org/pdf/2607.01556)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mind the Gap: Standard 3DGS Evaluation Primarily Measures Near-Trajectory Interpolation
- 作者：Gaoxiang Jia, Vikram Appia
- 出版日期：2026-07-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.01556

### 一句话总结
论文发现标准3DGS评估（隔帧留出）实际上测量的是近轨迹插值性能，而非空间泛化能力，并通过一种匹配计数协议量化了一个显著的插值-外推差距（3~12 dB），该差距跨多种表示方法存在且足以改变方法排名。

### 研究问题
标准MipNeRF360风格的3DGS评估（每隔N帧留出一帧作为测试集）是否真正衡量了模型对未见空间区域的泛化能力，还是仅仅衡量了相邻训练帧之间的插值性能？

### 核心思路/方法
作者提出了一个“匹配计数”（matched-count）对比协议：让两种评估方案使用相同数量的训练图像，唯一区别在于留出帧的分布方式：
- 插值方案：留出帧均匀分布于整个轨迹（即标准隔帧留出）。
- 外推方案：留出帧形成一个连续的空间扇区（即模型需要外推到未见过的空间区域）。
通过比较两种方案下的性能差异（插值-外推差距），作者量化了标准评估中混入的插值分量。

### 主要贡献
1. 首次结合了匹配计数配对留出、跨表示量化（含非高斯体素神经辐射场）和诊断分析，揭示了标准3DGS评估中的系统偏差。
2. 发现一个一致的插值-外推差距（3~12 dB），该差距远大于典型的方法间性能差异，并在多随机种子验证下足以改变方法排名。
3. 诊断出该差距主要由扩散/几何代理分量主导，并与每个视图到最近训练视图的角距离相关，这一零成本信号可用于捕获规划。
4. 准备发布一个包含16个场景的标准化空间留出基准工具包（含划分和基线）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作系统性地揭示了当前3DGS评估范式中的一个根本性缺陷（将插值误读为泛化），发现的结果数量级（差距3~12 dB）远超常见方法改进，对研究社区正确解读实验结果具有广泛指导意义。论文还提供了跨表示验证和诊断分析，并计划开源基准工具包，实用性和影响力均较高。

</details>

<details>
<summary>Abstract</summary>

Standard MipNeRF360-style 3D Gaussian Splatting (3DGS) evaluation holds out every N-th frame -- but these frames have trained neighbors on both sides, so the metric measures near-trajectory interpolation rather than spatial generalization. We introduce a fair matched-count protocol that isolates this effect: both arms train on the same number of images and differ only in whether the holdout is spread evenly (interpolation) or forms a contiguous spatial sector (extrapolation). Our primary finding is a large, consistent interpolation-extrapolation gap of 3~12dB -- several times the differences typically reported between competing methods. The gap is robust to training noise, is in two cases large enough to flip a method ranking under multi-seed confirmation, and -- crucially -- persists across three representation families, including a non-Gaussian volumetric neural radiance field (NeRF), so it reflects spatial coverage rather than any one representation. Diagnostically, it is dominated by a diffuse/geometry-proxy component and tracks each view's angular distance to its nearest training view, a zero-cost signal that also guides capture planning; loss-side regularization yields only marginal gains. Standard holdouts remain useful for near-trajectory rendering but should not, alone, be read as evidence of spatial generalization. Prior work notes protocol sensitivity; ours is, to our knowledge, the first to combine matched-count paired holdout, cross-representation quantification, and a diagnostic analysis Table 1. We describe a spatial-holdout benchmark toolkit with standardized splits and baselines for 16 scenes, which we are preparing for public release.

</details>

#### 2026-07-01 - FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight

**Authors:** Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian
**Links:** [abs](https://arxiv.org/abs/2607.01200) - [pdf](https://arxiv.org/pdf/2607.01200)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight
- 作者：Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian
- 出版日期：2026-07-01T17:33:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.01200

### 一句话总结
本文提出了一种基于全四旋翼动力学、考虑执行器约束的非线性安全滤波器（FastBridge），用于在3D高斯泼溅（3DGS）场景表示下实现快速、低抖动且计算高效的避障飞行。

### 研究问题
现有基于3DGS的安全滤波器采用简化模型（如单/双积分器），忽略执行器极限和加速度实时性，导致实际飞行中存在模型误差和抖动问题。

### 核心思路/方法
1. 基于3DGS的解析碰撞锥障碍物模型，引入非线性、考虑执行器的安全滤波器，并整合全四旋翼动力学。
2. 推导高相对度碰撞锥指数型控制障碍函数（CBF）以及备份CBF，利用前向模拟的备份策略在输入约束下保持二次规划（QP）可行性。
3. 通过仿真和硬件实验，在杂乱、感知衍生的环境中进行实时导航验证。

### 主要贡献
1. 提出了首个结合全四旋翼动力学的3DGS安全滤波器，弥合了模型简化带来的现实差距。
2. 在相同场景下，与最先进的3DGS安全滤波器相比，轨迹抖动降低47%，运行速度提升2.25倍。
3. 在仿真和真实硬件上验证了方法的实时性与有效性。

### 局限性
摘要未提供关于方法在极端环境（如高速、高动态干扰）下的鲁棒性、对3DGS重建质量的依赖程度以及计算资源需求的具体信息。

### 阅读优先级
高  
理由：该方法直接解决了3DGS安全滤波器在现实部署中的模型不匹配和性能瓶颈（抖动大、计算慢），实验增益显著（抖动降47%，快2.25倍），对视觉导向的无人机自主飞行和神经场景表示应用有明确实用价值。

</details>

<details>
<summary>Abstract</summary>

Fast quadrotor flight requires safe obstacle avoidance under tight onboard compute limits. While 3D Gaussian Splatting (3DGS) provides a continuous, geometry-aware scene representation for perception-driven navigation, existing 3DGS safety filters use reduced-order models such as single- and double-integrators that ignore actuator limits and assume commanded accelerations are realized instantaneously. Building on an analytic collision cone barrier for 3DGS, we introduce a nonlinear, actuator-aware safety filter enforced through the full quadrotor dynamics. We derive a high-relative-degree collision cone exponential CBF and a backup CBF that preserves QP feasibility under input constraints using a forward-simulated backup policy. Compared with a state-of-the-art 3DGS safety filter, our approach reduces trajectory jerk by 47% and runs 2.25 times faster. We validate the method in simulation and on hardware for real-time navigation in cluttered, perception-derived environments.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-07 - RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation

**Authors:** Haoyu Zhao, Xingyue Zhao, Siteng Huang, Xin Li, Deli Zhao, Zhongyu Li
**Links:** [abs](https://arxiv.org/abs/2607.06559) - [pdf](https://arxiv.org/pdf/2607.06559)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

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

#### 2026-07-02 - Towards Robustness against Typographic Attack with Training-free Concept Localization

**Authors:** Bohan Liu, Wenqian Ye, Guangzhi Xiong, Zhenghao He, Sanchit Sinha, Aidong Zhang
**Links:** [abs](https://arxiv.org/abs/2607.02494) - [pdf](https://arxiv.org/pdf/2607.02494)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Robustness against Typographic Attack with Training-free Concept Localization  
- 作者：Bohan Liu, Wenqian Ye, Guangzhi Xiong, Zhenghao He, Sanchit Sinha, Aidong Zhang  
- 出版日期：2026-07-02  
- 分类：具身机器人/增强现实应用  
- 链接：摘要URL: https://arxiv.org/abs/2607.02494 ; PDF: https://arxiv.org/pdf/2607.02494  

### 一句话总结  
本文提出一种无需训练的可解释性方法，通过定位和调整CLIP视觉Transformer中过度编码词汇信息的注意力头，有效提升模型对文字攻击的鲁棒性。

### 研究问题  
CLIP模型在面对图像中无关文本时的脆弱性（文字攻击），导致视觉表征偏向词汇含义而非真实视觉语义，威胁安全关键应用（如自动驾驶）。

### 核心思路/方法  
1. 提出一种基于采样的隐状态表示解释方法，定量分析每个注意力头对语义与词汇信息的关注程度。  
2. 通过概率分析和电路挖掘，隔离视觉Transformer中过度编码词汇信息的组件（即文字攻击的机制根源）。  
3. 对识别出的电路施加简单干预（如选择性调整注意力权重），无需额外训练即可提升分类鲁棒性。  
4. 将该干预应用于多个大型视觉语言模型的视觉编码器，验证其在RIO-Bench上的泛化性。

### 主要贡献  
1. 首次将文字攻击的脆弱性归因到特定注意力头，并揭示其机制来源。  
2. 提出一种无需训练的可解释性防御方法，优于现有监督和无训练防御。  
3. 方法在多个模型上验证有效，并提升了视觉问答准确率。

### 局限性  
摘要未提供足够信息（如计算开销、对合法文本的误判影响、干预后整体性能变化等）。

### 阅读优先级  
高  
理由：该工作针对CLIP模型关键漏洞（文字攻击），提出无需训练的因果解释与防御方法，方法新颖且实验验证了有效性及泛化性，对理解与提升大视觉语言模型安全性具有显著价值。

</details>

<details>
<summary>Abstract</summary>

Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP models exhibit a critical yet underexplored failure mode: irrelevant text appearing within images confounds visual representations, biasing them toward lexical meaning rather than true visual semantics. This robustness issue, commonly described as a Typographic Attack (TA), exposes a vulnerability that poses a significant risk to safety-critical applications such as autonomous driving. To achieve interpretable and effective robustness against TA, we propose a novel, training-free mechanistic interpretability method. Our method provides sampling-based interpretations of hidden state representations and quantitatively attributes semantic versus lexical focus to individual attention heads. Through probabilistic analysis and circuit mining, we isolate specific Vision Transformer (ViT) components that disproportionately encode lexical information, thereby identifying the mechanistic source of TA. We further show that simple interventions applied directly to the identified circuits, without any additional training, can substantially improve robustness against Typographic Attacks in object classification. These interventions, such as selective adjustment of attention weights, also outperform both supervised and training-free defense methods. Our experiments demonstrate that applying the proposed intervention to the vision encoders of several state-of-the-art LVLMs yields substantial gains in Visual Question Answering accuracy under Typographic Attack interference on RIO-Bench. These results confirm both the efficacy and the generalizability of our mechanistic approach. Code is released at https://github.com/Liu-524/SamplingTAR.

</details>

#### 2026-07-02 - Comprehensive Robustness Analysis of LiDAR-based 3D Object Detection in Autonomous Driving

**Authors:** Adwait Chandorkar, Kai Krink, Yerdana Maulenbay, Hasan Tercan, Tobias Meisen
**Links:** [abs](https://arxiv.org/abs/2607.02074) - [pdf](https://arxiv.org/pdf/2607.02074)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Comprehensive Robustness Analysis of LiDAR-based 3D Object Detection in Autonomous Driving
- 作者：Adwait Chandorkar, Kai Krink, Yerdana Maulenbay, Hasan Tercan, Tobias Meisen
- 出版日期：2026-07-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.02074

### 一句话总结
本文提出一个用于评估LiDAR3D目标检测模型对抗鲁棒性的全面框架，并通过对新旧SOTA模型的实证分析，发现高容量体素检测器比柱状检测器更易受结构化坐标扰动，且近期模型和早期模型同样脆弱。

### 研究问题
现有针对LiDAR-only 3D目标检测的对抗鲁棒性研究不足，且评估框架仅依赖mAP，忽略了结构和预测因素。本文旨在填补这一空白，提出一个综合考虑结构因素（点云密度、点云定位）和预测因素（误分类、定位误差、自车距离）的评估框架。

### 核心思路/方法
1.  **提出评估框架**：定义五个评估维度——两个结构因素（点云密度、点云定位）和三个预测因素（误分类、定位误差、自车距离）。
2.  **实证研究**：使用专门针对LiDAR模型的对抗攻击方法，对近期和历史上的SOTA模型进行实验。
3.  **关键对比**：比较体素检测器与柱状检测器、基于锚点的检测器与非锚点检测器的鲁棒性差异。

### 主要贡献
- 提出了一个比单一mAP更全面的对抗鲁棒性评估框架。
- 发现高容量、基于体素的检测器比柱状检测器更易受结构化坐标扰动。
- 发现非锚点检测器对抗鲁棒性较差，暗示需要重新思考训练方法。
- 论证了近期模型与早期模型一样容易受到对抗攻击，强调需改进评估基准以同时奖励检测精度和鲁棒性。

### 局限性
摘要未提供足够信息来阐明具体局限性，例如未提及实验评估的模型数量、攻击方法种类、数据集规模，也未讨论框架的计算成本或对某些场景的适用性。

### 阅读优先级
**中**
理由：该工作针对自动驾驶中LiDAR检测模型的对抗鲁棒性这一关键安全性问题，提出了系统性评估框架。对于从事自动驾驶安全或LiDAR感知研究的读者具有参考价值。但由于摘要仅提供了定性结论和框架概述，未展示具体实验数据和模型表现，阅读优先级评为“中”。

</details>

<details>
<summary>Abstract</summary>

Recent advancements in LiDAR-only 3D object detection have demonstrated improved detection accuracy over benchmark datasets. However, the adversarial robustness of these models remains untested. Very few adversarial robustness studies exist for LiDAR-only 3D object detection and unfortunately, even they are limited to legacy models. Moreover, there is a systemic gap in the existing evaluation frameworks that rely simply on mAP ignoring other structural and predictive factors. To fill this gap, we propose a holistic framework that evaluates adversarial robustness using two structural factors (point cloud density and point cloud localization) and three predictive factors (misclassification, localization error, distance from ego). Using this framework, we perform an empirical study and critical analysis on recent and legacy state-of-the-art models using adversarial attacks specifically designed for LiDAR-based models. Our key finding is that high-capacity, voxel-based detectors are more susceptible to structured coordinate perturbations than pillar-based detectors. Additionally, non-anchor-based detectors demonstrate poor adversarial robustness, which necessitates rethinking model training techniques. Overall, our results demonstrate that recent models are as vulnerable to adversarial attacks as their predecessors. Therefore, we argue that there is a need to improve the evaluation benchmarks for 3D object detection that not only reward architectural modifications for improving detection accuracy, but also evaluate whether the design choices improve adversarial robustness.

</details>

#### 2026-07-02 - PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation

**Authors:** Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang, Bo Yang
**Links:** [abs](https://arxiv.org/abs/2607.01938) - [pdf](https://arxiv.org/pdf/2607.01938)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation
- 作者：Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang, Bo Yang
- 出版日期：2026-07-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.01938

### 一句话总结
PhysMani 提出了一种结合物理原理的3D高斯世界模型与未来感知动作策略模型的框架，用于在非结构化环境中操控快速动态目标，并在仿真和真实机器人实验中取得了优于强基线的成功率。

### 研究问题
如何在非结构化3D环境中，对快速运动的目标进行准确且物理可行的动态预测，并据此制定有效的操控动作策略。

### 核心思路/方法
1. **物理原理的3D高斯世界模型**：通过在线优化学习一个无散度（divergence-free）的高斯速度场，实现对未来动态的快速、物理驱动的预测。
2. **未来感知动作策略模型**：采用基于可学习标记（learnable token）的交叉注意力模块，将世界模型预测的3D场景未来动态整合到动作决策中。
3. **基准测试**：构建了包含16个任务的动态操控基准（PhysMani-Bench）用于评估。

### 主要贡献
1. 提出了一种物理原理驱动的3D高斯世界模型，能够在线优化并预测无散度的速度场，保证未来动态预测的物理合理性。
2. 设计了未来感知动作策略模型，通过可学习标记的交叉注意力机制融合预测的动态信息，提升操控性能。
3. 发布了包含16个任务的动态操控基准PhysMani-Bench，并在仿真和真实机器人实验中验证了方法相对于强基线的优越成功率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对具身智能中动态目标操控这一难题，提出了结合物理原理的3D世界模型与动作策略的新框架，并在仿真和真实场景中均取得优于基线方法的性能。对于关注具身AI、机器人操控、3D场景理解与动态预测的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Manipulating fast and dynamically moving targets in unstructured 3D environments remains challenging for embodied AI. Existing visual-language-action models and world models struggle with accurate 3D geometry and physically meaningful forecasting. We propose PhysMani, a framework that couples a physics-principled 3D Gaussian world model with a future-aware action policy model. The world model learns a divergence-free Gaussian velocity field via online optimization for fast and physically grounded future dynamics prediction. The policy model integrates the predicted 3D scene future dynamics through a learnable token based cross-attention module. We introduce PhysMani-Bench, a dynamic manipulation benchmark with 16 tasks, and demonstrate a superior success rate over strong baselines in both simulation and real-world robot experiments.

</details>

#### 2026-07-02 - LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design

**Authors:** Wen Wang, Yaping Sun, Yejun He, Hao Chen, Zhiyong Chen, Xiaodong Xu, Nan Ma, Shuguang Cui
**Links:** [abs](https://arxiv.org/abs/2607.01772) - [pdf](https://arxiv.org/pdf/2607.01772)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design
- 作者：Wen Wang, Yaping Sun, Yejun He, Hao Chen, Zhiyong Chen, Xiaodong Xu, Nan Ma, Shuguang Cui
- 出版日期：2026-07-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.01772

### 一句话总结
本文提出一个以大语言模型（LLM）为核心的视觉-雷达融合框架LM-SCIP，通过通道自适应语义模块动态调整外部雷达特征，实现了在不同信噪比下从降级回退到协同融合的鲁棒感知。

### 研究问题
实际自动驾驶中视觉-雷达融合质量受遮挡、恶劣天气及信道噪声影响而动态变化，现有静态数据融合方法无法适应这种输入质量的波动。

### 核心思路/方法
1. 将问题从静态数据融合重新定义为通道感知语义推理，构建以大语言模型（LLM）为中心推理核心的LM-SCIP框架。
2. 设计层次化雷达-视觉编码器，并引入通道自适应语义模块（CASM），将链路指标映射为“通道提示”，用于动态门控外部雷达特征。
3. 使用参数高效的LoRA微调LLM，结合异构混合专家（H-MoE），协调本地视觉线索与通道条件化的雷达上下文。
4. 采用解耦多任务解码器输出定位、轨迹预测和图像重建。

### 主要贡献
- 提出了以LLM为核心的通道感知语义融合框架LM-SCIP，解决了视觉-雷达融合中动态输入质量问题。
- 设计了CASM模块，利用链路指标生成提示实现雷达特征的自适应门控。
- 在nuScenes数据集上，控制雷达输入切换时，LM-SCIP相较纯视觉基线将定位RMSE降低40.0%。
- 在VIRAT数据集上达到0.214m定位RMSE和0.179m最小最终位移误差（minFDE，k=1），验证了低信噪比下的稳健降级回退与高信噪比下的协同融合。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作将LLM融入自动驾驶多模态融合，提出新颖的通道自适应设计，有效解决了实际场景中动态输入质量问题，定量结果显著（RMSE降低40%），对自动驾驶感知鲁棒性研究有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-radar fusion is central to robust autonomous driving, combining dense visual semantics with precise range and velocity measurements from radar. However, real-world fusion quality is fundamentally challenged by dynamically varying input quality, stemming from occlusion, adverse weather, and channel noise. To address this, we re-frame the problem from static data fusion to channel-aware semantic reasoning and propose a Large Language Model-centric Semantic-layer Channel-aware Integrated Perception (LM-SCIP) framework. It places a Large Language Model (LLM) as a central reasoning core to fuse a local visual stream with a quality-varying external radar stream used to cover perception-blind spots. Concretely, LM-SCIP couples a hierarchical radar-vision encoder with a Channel-Adaptive Semantic Module (CASM) that maps link indicators into a "Channel Prompt" to dynamically gate external radar features. A parameter-efficient, LoRA-tuned LLM, in conjunction with a heterogeneous Mixture-of-Experts (H-MoE), then arbitrates between local visual cues and the channel-conditioned radar context. Finally, a decoupled multi-task decoder outputs localization, trajectory forecasting, and image reconstruction. Experiments on nuScenes and VIRAT validate our approach. On nuScenes, under a controlled toggle of radar input, LM-SCIP reduces localization RMSE by 40.0% versus a vision-only baseline. On VIRAT, the model attains a 0.214m localization RMSE and 0.179m minFDE (k=1). These results reveal that the proposed LM-SCIP enables a robust vision-dominant fallback at low SNR and synergistic fusion at high SNR.

</details>

#### 2026-07-01 - Structured 4D Latent Predictive Model for Robot Planning

**Authors:** Zhiyi Li, Peilin Wu, Xiaoshen Han, Ruojin Cai, Yilun Du
**Links:** [abs](https://arxiv.org/abs/2607.01166) - [pdf](https://arxiv.org/pdf/2607.01166)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Structured 4D Latent Predictive Model for Robot Planning
- 作者：Zhiyi Li, Peilin Wu, Xiaoshen Han, Ruojin Cai, Yilun Du
- 出版日期：2026-07-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.01166

### 一句话总结
本文提出一种结构化的4D潜在预测模型，用于机器人规划，该模型在结构化潜空间中预测场景3D结构的演化，从而生成具有强3D一致性的未来场景，并最终通过逆动力学模块转化为执行动作。

### 研究问题
现有基于2D视频的预测模型缺乏3D几何理解，难以进行精确的空间推理和保持物理一致性，因此需要一种能够生成3D一致未来场景的预测模型以提升机器人规划性能。

### 核心思路/方法
1. 构建一种结构化的4D潜在预测模型，在结构化潜空间中预测场景3D结构的演化，该表示以观测和文本指令为条件。
2. 该表示可解码为多种3D格式，实现完整且3D一致的场景理解。
3. 模型作为规划器生成未来场景，再通过目标条件的逆动力学模块将这些场景转化为可执行动作。

### 主要贡献
- 提出结构化4D潜在预测模型，能预测场景3D结构演化，并解码为多种3D格式。
- 生成具有强视觉质量、显著优于现有基于视频规划器的3D一致性和多视角连贯性的未来场景。
- 在复杂操作任务上取得优异表现，展现出对新型视觉条件的鲁棒泛化能力，并在真实机器人平台上验证有效性。

### 局限性
摘要未提供关于模型计算复杂度、训练数据需求、失败案例或与现有方法在更广泛场景下对比的具体信息，因此局限性无法从摘要中得出。

### 阅读优先级
优先级：**中**
理由：该工作在机器人规划中引入结构化4D潜在空间表示，在3D一致性和多视角连贯性上相比2D视频方法有明确提升，且提供了真实机器人实验验证，值得关注。但摘要未深入说明方法的具体实现细节或定量对比，需阅读全文以评估其工程实用性和可复现性。

</details>

<details>
<summary>Abstract</summary>

Video predictive models are emerging as a powerful paradigm in robotics, offering a promising path toward task generalization, long-horizon planning, and flexible decision-making. However, prevailing approaches often operate on 2D video sequences, inherently lacking the 3D geometric understanding necessary for precise spatial reasoning and physical consistency. We introduce a Structured 4D Latent Predictive Model, which predicts the evolution of a scene's 3D structure in a structured latent space conditioned on observations and textual instructions. Our representation encodes the scene holistically and can be decoded into diverse 3D formats, enabling a more complete and 3D consistent scene understanding. This structured 4D latent predictive model serves as a planner, generating future scenes that are translated into executable actions by a goal-conditioned inverse dynamics module. Experiments demonstrate that our model generates futures with strong visual quality, substantially better 3D consistency and multi-view coherence compared to state-of-the-art video-based planners. Consequently, our full planning pipeline achieves superior performance on complex manipulation tasks, exhibits robust generalization to novel visual conditions, and proves effective on real-world robotic platforms. Our website is available at https://structured-4d-model.github.io/.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
