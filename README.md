# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：48
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 21
  - Embodied / Robotics / AR Applications: 14
  - Neural Scene Representations & Rendering: 8
  - Geometry Foundation Models: 3
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，作为您的计算机视觉和三维重建方向科研趋势分析助手，以下是根据您今日提供的论文列表生成的科研趋势综合分析。

---

#### 今日主要趋势

1.  **基础模型深度赋能与轻量化部署并行**：几何基础模型（如VGGT、3DGS相关）的隐式能力被深入挖掘，同时大型基础模型（如扩散模型、单目深度估计模型）正向轻量、高效、可实时运行的方向迅猛发展，两者共同推动技术从“能否做”向“在哪做”转变。代表论文：`What VGGT Knows About Overlap`、`ZipDepth`、`LongE2V`、`Time-to-Collision`。

2.  **从“静态世界”走向“动态与可形变场景”**：研究热点明显从静态场景重建，转向更具挑战性的动态场景、可形变物体（手术、抓取）以及长时间视频处理。这包括对运动先验、时间一致性、物理真实性的极致追求。代表论文：`LongE2V`、`Track2Map`、`On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting`、`LightCrafter`。

3.  **低资源与特定领域重建的范式创新**：在标注数据稀缺或领域特性显著（如水下、野火、手术、树木生长）的场景下，研究工作不再依赖大规模标注，而是转向利用先验知识、自/半监督学习、跨域适应等创新范式，并同时构建配套的评估基准。代表论文：`Wat3R`、`LTM`、`Track2Map`、`3D Reconstruction of deciduous Trees`。

4.  **SLAM与机器人应用的鲁棒性与社会性融合**：SLAM和机器人抓取/导航正从理想环境走向动态、非结构化的真实世界。研究不仅关注定位与建图的鲁棒性（如对抗动态物体、大尺度、弱纹理），还开始融合语义、人体社会线索等高层认知信息，以提升系统的智能性和社会适应性。代表论文：`PLED-VINS`、`Track2Map`、`HumAIN`、`Monocular Vision Based Control Framework for Grasping`、`Time-to-Collision`、`WCog-VLA`、`CARLA-GS`。

#### 技术路线观察

| 技术方向 | 核心关注点 | 代表论文 | 技术侧重点 |
| :--- | :--- | :--- | :--- |
| **几何基础模型** | 模型内部表征与能力挖掘、知识蒸馏 | `What VGGT Knows About Overlap` | 通过探针实验和轻量级训练头发掘预训练模型（VGGT）的隐式能力（共可见性），理解模型行为。 |
| **3D/4D 重建** | 尺度感知、动态/形变、拓扑、大规模场景 | `DGSfM`、`On the Design of MoE for Dynamic GS`、`HoloTetSphere`、`PanoLOG`、`LTM` | **DGSfM** 侧重利用先验（深度图）提升鲁棒性；**MoE** 探索多专家模型处理复杂动态；**HoloTetSphere** 突破拓扑限制；**PanoLOG** 解决全景图大规模场景分区问题；**LTM** 利用多模态先验（DEM）降低计算成本。 |
| **神经场景表示与渲染** | 视频时间一致性、物理真实感、几何优先 | `LightCrafter`、`LongE2V`、`GeoGS-SLAM` | **LightCrafter** 和 **LongE2V** 侧重于生成式模型（扩散模型）在视频上的时间一致性与控制性；**GeoGS-SLAM** 则反其道而行，抛弃外观重建，专攻纯几何的SLAM，强调效率与实用性。 |
| **机器人/AR应用** | 动态环境、隐性社会线索、端到端驾驶 | `PLED-VINS`、`HumAIN`、`WCog-VLA`、`Time-to-Collision`、`DexVerse`、`CARLA-GS` | **PLED-VINS** 和 **Time-to-Collision** 关注系统鲁棒性与数据效率；**HumAIN** 引入社会维度（人）；**WCog-VLA** 和 **CARLA-GS** 构建更高级的认知和仿真框架（世界模型、大模型、物理仿真），实现主动驾驶和复杂场景生成。 |

#### 值得优先阅读的论文

1.  **`ZipDepth`** - **优先理由**：高度务实，直击“模型部署到边缘设备”这一核心产业痛点。它展示了如何通过知识蒸馏，将笨重的零样本深度估计模型压缩到一个仅6.1M参数、可实时运行的小模型上。这对于关注落地和工程化的研究者极具参考价值。

2.  **`LightCrafter`** - **优先理由**：视频重光照是一个高难度、高应用价值的任务。该工作巧妙地结合了基于物理渲染（PBR）的“确定性”优势与基于扩散模型的“生成式”优势，提出了一种混合流水线，在保持物理真实感的同时，实现了长视频的时间一致性。其设计思路对类似问题（如视频编辑、增强现实）有很强的借鉴意义。

3.  **`HoloTetSphere`** - **优先理由**：这项工作直接挑战了传统的“重建+四面体化”两步走范式。通过端到端的可微分拓扑与几何优化，直接生成可用于物理仿真的连贯四面体网格。这为计算机图形学、VR/AR和科学计算中的物理仿真工作流带来了革新的可能性。

4.  **`Wat3R`** - **优先理由**：水下3D重建是典型的标注匮乏领域。`Wat3R`提出的无标注跨域半监督学习方法（教师-学生架构加上精巧的跨视图一致性损失）是一种强大且通用的方法论。任何面临类似数据瓶颈（如医疗、遥感）的研究者都能从中获得启发。

5.  **`On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting`** - **优先理由**：该工作不是提出一个具体的SOTA方法，而是从“混合专家”（MoE）的角度，系统性地研究了动态3DGS中多变形建模的设计空间。它提供了两种互补的集成策略和深入的分析，具有很高的理论价值，为后续设计更鲁棒的动态3DGS方法奠定了基础。

#### 可能的研究机会

1.  **动态场景中的“几何+外观”解耦重建与高效渲染**：`GeoGS-SLAM` 证明了纯几何GS的可行性，`LightCrafter` 尝试将物理与生成结合。未来是否可在4D重建中，将动态物体的几何、刚性与非刚性运动、外观纹理解耦，分别用最高效的方式表示，并通过一个统一的框架整合？

2.  **通用“共可见性”先验的SLAM与重建**：`What VGGT Knows About Overlap` 证明了从基础模型中提取共可见性先验的可行性。这可以作为一个通用的“智能”视图选择器或初始化模块，提升现有全局SfM或基于学习的SLAM系统在大规模、弱纹理场景下的性能和鲁棒性。

3.  **知识蒸馏与特定领域重建的结合**：`ZipDepth` 和 `HumAIN` 都采用了知识蒸馏。这一思路可以推广。例如，将大仿真模型（如`DexVerse`、`CARLA-GS`）中习得的、针对特定任务（如灵巧操作、边缘案例）的“世界知识”，蒸馏到一个轻量级的感知-控制模型中，实现高效部署。

4.  **基于物理先验的可微渲染与重建**：`LTM` 利用DEM作为几何先验，`HoloTetSphere` 是可微四面体网格。可进一步研究将其他物理先验（如光照模型、材料属性、流体动力学）直接引入可微渲染管线，实现从稀疏观测中重建出物理上更准确、更可编辑的3D场景。

#### 风险和不确定性

*   **通用性与局限性**：许多论文的“贡献”和“性能”在摘要中通常被概括为“超越了SOTA”。但摘要很少提及方法的**失败案例、计算开销、对超参数的敏感性**以及在极端退化

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-14T10:11:38-04:00
**Total number of papers:** 56
**Number of papers added in the latest update:** 20
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

#### 2026-07-12 - MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction

**Authors:** Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia
**Links:** [abs](https://arxiv.org/abs/2607.10792) - [pdf](https://arxiv.org/pdf/2607.10792)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** MASt3R, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>Abstract</summary>

Reconstructing high-fidelity 3D scenes from sparse-views remains a central problem in generalizable neural rendering. Existing generalizable 3D Gaussian Splatting (3DGS) methods often exhibit geometric artifacts in sparse-view settings, since supervision based solely on 2D photometric losses cannot resolve depth and correspondence ambiguities. To address this issue, we propose MAC-Splat, a training framework built around direct 3D consistency supervision. MAC-Splat builds on the MASt3R geometric backbone and a frozen DINOv3 encoder to obtain semantically informed 2D correspondences, which serve as geometric anchors for 3D supervision. Using these anchors, we define the Multi-Attribute Consistency (MAC) loss. This objective jointly regularizes the 3D attributes of matched Gaussians, including their position, shape, and appearance, by enforcing agreement in a common world coordinate frame. The formulation is robust to outliers and respects the geometry of covariance matrices, which leads to stable training under sparse-view conditions. Experiments on ScanNet++ show that MAC-Splat outperforms strong baselines, with particularly large gains under different overlap regimes. In particular, it improves average PSNR over Splatt3R by more than 4.5 dB, reduces LPIPS, and maintains performance as the camera pose gap increases. These results indicate that a direct, multi-attribute 3D consistency objective, when combined with high-quality correspondences, is effective for addressing the ill-posed sparse-view reconstruction problem.

</details>

#### 2026-07-10 - What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility

**Authors:** Filippo Ziliotto, Luciano Serafini, Lamberto Ballan, Tommaso Campari
**Links:** [abs](https://arxiv.org/abs/2607.09503) - [pdf](https://arxiv.org/pdf/2607.09503)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, SfM, SLAM, scene representation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility  
- 作者：Filippo Ziliotto, Luciano Serafini, Lamberto Ballan, Tommaso Campari  
- 出版日期：2026-07-10  
- 分类：Geometry Foundation Models（主），3D Reconstruction & Multi-view Geometry（次）  
- 链接：摘要 https://arxiv.org/abs/2607.09503 | PDF https://arxiv.org/pdf/2607.09503  

### 一句话总结
本文发现VGGT内部表征隐式编码了共可见性（co-visibility），并通过引入轻量级逐层混合专家头（Co-VGGT）在Co-VisiON基准上超越人类标注基线，性能提升超过25%。

### 研究问题
如何利用几何基础模型VGGT的内部表征，在没有显式监督的情况下，判断图像对之间是否存在共可见重叠区域（尤其在低重叠场景中）？

### 核心思路/方法
1. 通过探针实验揭示VGGT的层级结构：早期层构建3D感知场景表征，晚期层（特别是L17层）充当共可见性推理器，且层L17对非共可见对具有一致路由行为。  
2. 提出Co-VGGT：冻结VGGT，仅训练一个小于7.5M参数的逐层混合专家头（layer-wise MoE），将每层视为一个专家，根据输入对自适应加权每层的几何抽象，以便从单张RGB图像中分类共可见性。  
3. 在Co-VisiON基准上评估，并与先前方法及人类标注基线对比。

### 主要贡献
1. 首次证明VGGT能够隐式编码共可见性，其内部表征呈现类似LLM的层级结构，且存在问题导向的层级专化证据（负锚点层L17）。  
2. 提出Co-VGGT方法，仅训练轻量级MoE头，以分类RGB图像对的共可见性。  
3. 在Co-VisiON基准上，Co-VGGT的成对预测和多重视图预测分别超越先前最佳方法25%以上和10%，并且超过人类标注基线。  
4. 成对预测校准良好（ECE=0.030），可直接作为可见性图的边权重用于下游SfM和SLAM流水线，无需后处理纠正。

### 局限性
摘要未提供足够信息，例如方法在极端场景下的性能、对错误预测的鲁棒性、计算效率的详细分析，以及是否依赖特定训练数据集等。

### 阅读优先级：高  
理由：该工作首次揭示VGGT的共可见性推理能力，基于此设计的轻量头方法显著超越现有技术和人类基线，性能提升幅度大（>25%）。方法直接服务于3D重建与SLAM的实际下游任务，且提供代码和数据，实用性强。

</details>

<details>
<summary>Abstract</summary>

A fundamental challenge in 3D reconstruction and robotic localization is co-visibility: determining which image pairs share overlapping visible surfaces, particularly in scenarios with minimal overlap. We demonstrate that VGGT implicitly encodes co-visibility as an emergent behavior: without any supervision for this task, its internal representations exhibit a clear hierarchical structure mirroring that of large language models, i.e. early layers build a 3D-aware scene representation, while late layers act as dedicated co-visibility reasoners. In particular, we identify layer L17 as a negative anchor that consistently routes non-co-visible pairs for this backbone, regardless of the evaluation setting, providing task-grounded evidence of layer specialization in a geometry-grounded foundation model. Building on this, we introduce Co-VGGT, which freezes VGGT and trains only a lightweight layer-wise mixture-of-experts head (less than 7.5M parameters) to classify co-visibility from RGB alone, treating each layer as a specialized expert whose geometric abstraction is adaptively weighted per input pair. On the Co-VisiON benchmark, Co-VGGT surpasses the human annotation baseline and improves over prior work by more than 25% pairwise and 10% multiview. Pairwise predictions are well-calibrated (ECE=0.030), enabling direct use as edge weights in visibility graphs for downstream SfM and SLAM pipelines without post-hoc correction. Code and data are available.

</details>

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

## Dynamic / 4D Reconstruction

### 2026-07

#### 2026-07-12 - OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields

**Authors:** Yanqin Jiang, Tengfei Wang, Zhengwei Wang, Chenjie Cao, Junta Wu, Wenhan Luo, Weiming Hu, Jin Gao, Chunchao Guo
**Links:** [abs](https://arxiv.org/abs/2607.10840) - [pdf](https://arxiv.org/pdf/2607.10840)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 4D reconstruction, camera pose estimation, pose estimation, depth estimation

<details>
<summary>Abstract</summary>

Previous feed-forward 4D reconstruction methods either predict per-frame static point clouds, ignoring foreground motion, or estimate point cloud trajectories while being limited to small camera motions. This restricts their ability to aggregate observations over time and reconstruct complete dynamic scenes under large viewpoint changes. To address this limitation, we propose OmniX, a feed-forward 4D reconstruction framework that predicts dense 3D point trajectories for every pixel from videos with large camera motion. OmniX decouples dynamic motion modeling from static geometry prediction and represents motion using a compact set of dynamic tokens. By leveraging the sparse and low-rank structure of 3D motion, these tokens generate trajectory fields for all pixels across all images while efficiently preserving global interactions. To facilitate training, we further build an automatic UE5-based 4D data engine and introduce a large-scale dataset containing 80K scenes and 1.28M multi-view videos with full geometric annotations. OmniX achieves state-of-the-art performance on dense 3D point trajectory prediction and 3D point tracking, while also demonstrating competitive results on video depth estimation and camera pose estimation.

</details>

#### 2026-07-11 - Grassmannian Splatting I: Moving rank-2 Spacetime Surfels for Dynamic Scene Rendering

**Authors:** Aaron Maurice Berman, Shantanu Dave
**Links:** [abs](https://arxiv.org/abs/2607.10489) - [pdf](https://arxiv.org/pdf/2607.10489)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene representation, 4D Gaussian, Gaussian Splatting, 3DGS, scene representation, rendering, splatting

<details>
<summary>Abstract</summary>

We introduce Grassmannian splatting, a dynamic scene representation whose primitives are Gaussians supported on 3-planes in spacetime $\R^4$: generically, spatial 2-planes in uniform translation along their normals. Each primitive carries a unit normal $n \in \mathbb S^3/\{\pm 1\} \cong \mathrm{Gr}(3,4)$ and an unconstrained factor $L \in \mathbb R^{4 \times 3}$, with covariance \[ Σ_{4\mathrm{D}} = (P_n L)(P_n L)^T, \qquad P_n = I - n n^T. \] For generic $L$ and $n \neq \pm e_0$, conditioning on time returns a rank-2 surfel at every frame. The normal of the disk and its velocity along that normal are read off from $n$; the disk shape and the tangential drift of its center are set by $L$. Existing native 4D Gaussian splatting methods [\it{Yang et. al. 2023,Duan et. al. 2024}] slice full-rank spacetime covariances, so their per-frame primitive is a volumetric ellipsoid; since conditioning lowers rank by exactly one, a rank-2 surfel in the slice requires a rank-3 spacetime covariance, and the parameterization above realizes exactly these. The motion model is closed form, i.e. no deformation field is learned, and no custom CUDA is required: the conditioned disk feeds a standard 3DGS rasterizer through its precomputed-covariance interface. A soft clamp in the Schur denominator regularizes the static orientation and continuously bridges rank-3 static and rank-2 dynamic behavior, so static and moving primitives form a single continuous family. On the 17 HyperNeRF scenes of MonoDyGauBench, training is fastest among all compared methods (4.9 to 5.6 times faster than the strongest quality baselines), while ranking second in PSNR, MS-SSIM, and LPIPS. Code: https://github.com/PaulCelanCoding/grassmannian-splatting

</details>

#### 2026-07-09 - LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models

**Authors:** Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, Yu-Lun Liu
**Links:** [abs](https://arxiv.org/abs/2607.08770) - [pdf](https://arxiv.org/pdf/2607.08770)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models
- 作者：Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, Yu-Lun Liu
- 出版日期：2026-07-09
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2607.08770

### 一句话总结
本文提出LongE2V，利用预训练视频扩散模型，通过自回归展开、自适应上下文切换和重编码对齐等技术，统一实现事件数据的高质量视频重建、预测和帧插值，尤其在长时序列中保持稳定性。

### 研究问题
如何从稀疏事件流中恢复高质量、长时稳定的视频，并同时解决重建、预测和帧插值三个任务中的纹理模糊、时间漂移和双向一致性问题。

### 核心思路/方法
1. **预训练视频扩散先验**：微调基础视频模型，利用其生成先验实现高数据效率和优越感知质量。
2. **自回归展开与自适应上下文切换**：通过逐步展开生成并动态切换上下文，缓解极长序列中的时间漂移。
3. **重编码对齐与交叉残差校正**：在帧插值任务中，通过对齐隐空间编码和残差校正，确保精确的双向一致性。
4. **事件体素密度增强**：增强对不同传感器分辨率的鲁棒性。

### 主要贡献
- 首个统一处理事件视频重建、预测和帧插值的扩散方法，实现三任务协同。
- 提出自回归展开和自适应上下文切换，解决长序列时间漂移问题。
- 提出重编码对齐与交叉残差校正，提升帧插值的双向一致性。
- 提出事件体素密度增强，提高模型对不同传感器分辨率的泛化性。
- 在真实世界基准上，三个任务均超越现有方法，表现出优异的时间一致性和零样本泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作首次将视频扩散模型统一应用于三个关键事件视觉任务，且重点解决了长时序列稳定性这一核心挑战，方法设计系统（多个原创模块），实验结果全面，理论基础与工程实践价值均较高，适合关注事件相机、视频生成和时序建模的研究者优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting
- 作者：In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong
- 出版日期：2026-07-09
- 分类：Dynamic / 4D Reconstruction（主要）、Neural Scene Representations & Rendering（次要）
- 链接：摘要页 https://arxiv.org/abs/2607.08250 ；PDF https://arxiv.org/pdf/2607.08250

### 一句话总结
本文从混合专家（MoE）视角出发，研究了动态3D高斯表示中多变形建模的设计问题，提出了两种不同集成约束下的变形专家组合策略：MoDE（联合优化）和MoE-GS（独立优化后经路由组合）。

### 研究问题
如何有效设计多变形模型，以提升动态3D高斯表示在多样化动态场景下的鲁棒性和泛化能力。

### 核心思路/方法
- 基于混合专家（MoE）框架，将多变形建模视为在统一3D表示中组合多个专用变形专家。
- 提出两种方案：
    - **MoDE（Mixture of Deformation Experts）**：多个变形专家与可变形高斯泼溅管线联合优化，作用于共享的规范高斯表示，不引入额外训练阶段。
    - **MoE-GS**：变形专家独立优化，通过独立的路由阶段进行组合，专家交互发生在非规范高斯表示上。
- 两种方案对比揭示了不同集成约束如何塑造动态3D表示中变形专家的设计与行为。

### 主要贡献
- 从MoE视角系统研究了动态3D高斯表示中的多变形建模问题。
- 提出两种互补的集成策略（MoDE和MoE-GS），分别对应不同的专家交互时机与表示形式。
- 为动态场景重建中如何灵活部署多变形模型提供了设计空间分析。

### 局限性
摘要未提供足够信息，无法判断具体实验局限性（如计算成本、场景规模限制等）。

### 阅读优先级
**高**
- **理由**：
    - 主题前沿：动态场景重建和3D高斯泼溅是当前热门的视觉研究方向。
    - 方法新颖：将MoE思想系统性地引入多变形建模，并明确提出两种差异化设计方案，具有方法论贡献。
    - 作者团队公布了代码，便于复现与扩展。

</details>

<details>
<summary>Abstract</summary>

Dynamic scene reconstruction remains challenging due to the heterogeneous and spatially varying nature of real-world motion. Although recent 3D Gaussian Splatting methods have introduced diverse deformation formulations for dynamic novel view synthesis, each method typically relies on a single deformation model within its representation, which limits robustness across diverse dynamic scenarios. In this work, we study a fundamental problem-multi-deformation modeling for dynamic 3D Gaussian representations-under two distinct integration constraints that differ in when and how multiple deformation experts interact during training. From a Mixture-of-Experts (MoE) perspective, we view multi-deformation modeling as the problem of combining multiple specialized deformation models within a unified 3D representation. We first introduce Mixture of Deformation Experts (MoDE), which integrates multiple deformation experts directly into the deformable Gaussian Splatting pipeline through joint optimization. In MoDE, experts operate on a shared canonical Gaussian representation, enabling multi-deformation modeling without introducing additional training stages or modifying the original optimization schedule. In contrast, we further present Mixture of Experts for Dynamic Gaussian Splatting (MoE-GS) under a different integration constraint, where deformation experts are optimized independently and combined through a separate routing stage. As a result, expert interaction occurs over non-canonical Gaussian representations after individual optimization. Together, these two approaches provide alternative strategies for multi-deformation modeling, clarifying how integration constraints shape the design and behavior of deformation experts in dynamic 3D Gaussian representations. Our code is available at: https://github.com/cvsp-lab/MoE-GS-studio.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-13 - IBPA: Real-time Free-form Manifold Mesh Reconstruction via Incremental Ball Pivoting with Integrated Hole Detection

**Authors:** Mauhing Yip, Mohit Singh, Kostas Alexis, Christian Schellewald, Annette Stahl
**Links:** [abs](https://arxiv.org/abs/2607.11627) - [pdf](https://arxiv.org/pdf/2607.11627)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction, surface reconstruction

<details>
<summary>Abstract</summary>

Both Remotely Operated underwater Vehicles (ROVs) and Autonomous Underwater Vehicles (AUVs) are frequently deployed to acquire geometric bathymetric data. However, it is often discovered post-survey that the acquired data coverage is incomplete. Given the high operational cost associated with underwater deployments, it is essential to incrementally visualize surface coverage in real-time to support informed decision-making by both the operators of ROVs and the AUVs during data collection. In addition, traditional incremental surface reconstruction methods, such as Digital Terrain Models (DTMs), are inherently limited in expressiveness: they represent surfaces as height fields, allows only one elevation value per $(x, y)$ coordinate and thus cannot capture overhangs or vertical structures. To overcome these limitations, we adapt the original Ball Pivoting Algorithm (BPA) into an incremental, real-time, and free-form surface reconstruction method, referred to as Incremental BPA (IBPA). Our method incrementally constructs an orientable, manifold mesh from streaming point cloud data without imposing assumptions regarding point cloud overlap or spatial distribution. Furthermore, we introduce a hole detection mechanism that identifies and highlights incomplete mesh regions. Compared to existing approaches, our method supports more complex surface topologies without prior structural assumptions. The source code of our reference implementation is available: https://github.com/Mauhing/Incremental-BPA

</details>

#### 2026-07-13 - SalientGS: Unified SfM-to-3DGS with Importance-Guided MCMC Gaussian Allocation

**Authors:** Tianyu Xiong, Rui Li, Suning Ge, Jiaqi Yang
**Links:** [abs](https://arxiv.org/abs/2607.11285) - [pdf](https://arxiv.org/pdf/2607.11285)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, SfM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

Reconstructing 3D scenes from unordered images remains bottlenecked by expensive Structure-from-Motion (SfM) preprocessing and frozen pose interfaces. We present SalientGS, a unified SfM-to-3D Gaussian Splatting (3DGS) pipeline. Its central contribution is importance-guided Markov Chain Monte Carlo (MCMC) Gaussian allocation, which aggregates multi-view residuals into per-Gaussian underfit and redundancy signals. These signals define a smooth importance-weighted sampling distribution that biases both birth and relocation toward underfit regions. This reallocates capacity from well-fit areas without altering the underlying stochastic gradient Langevin dynamics (SGLD). SalientGS achieves end-to-end reconstruction in 15 minutes with state-of-the-art perceptual quality. The supplementary material provides dedicated sections for Per-Scene Qualitative Comparisons and Per-Image Learned Perceptual Image Patch Similarity (LPIPS) Analysis, including failure cases. Code and evaluation scripts are available at https://github.com/Six-Bit-TX/SalientGS.

</details>

#### 2026-07-13 - GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors

**Authors:** Ruilan Gao, Letian Jin, Yu Zhang
**Links:** [abs](https://arxiv.org/abs/2607.11184) - [pdf](https://arxiv.org/pdf/2607.11184)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** SLAM, dense reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping

<details>
<summary>Abstract</summary>

SLAM methods based on 3D Gaussian Splatting (3DGS) have demonstrated impressive tracking and mapping performance, but typically require additional geometric information from external depth sensors. Meanwhile, recent SLAM systems that leverage geometric priors from pre-trained feed-forward models enable real-time dense reconstruction, yet often discard original RGB information during optimization, thus degrading overall reconstruction quality. We present GeoGS-SLAM, an online monocular dense reconstruction system that combines the 3DGS-based map representation with learned geometric priors. Given uncalibrated RGB input, we first employ a feed-forward visual geometry model to predict camera and scene priors. The Gaussian scene map is then expanded by directly sampling Gaussian primitives from both RGB input and geometric priors. Camera poses and the scene map are jointly optimized through a coarse-to-fine strategy that minimizes both photometric and geometric losses. To ensure global consistency, we further incorporate online loop closure detection and pose graph optimization. Extensive experiments across indoor and outdoor benchmarks demonstrate that GeoGS-SLAM achieves superior rendering quality and tracking accuracy compared to state-of-the-art methods while maintaining online real-time performance. Project page: https://rlgao.github.io/geogs_slam.

</details>

#### 2026-07-13 - GHOST: Geometry-Guided Hallucination of Opaque Surface Textures

**Authors:** Langxu Zhao, Zuan Gu, Tianhan Gao
**Links:** [abs](https://arxiv.org/abs/2607.11118) - [pdf](https://arxiv.org/pdf/2607.11118)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, depth estimation

<details>
<summary>Abstract</summary>

Transparent objects pose a fundamental challenge for depth estimation and 3D reconstruction due to their violation of Lambertian assumptions, leading to severe geometry degradation in downstream tasks. To address this, we propose a novel geometry-guided preprocessing framework \textbf{GHOST} that leverages visual foundation models to transform transparent regions into opaque, structurally consistent representations without requiring downstream model retraining. Specifically, our pipeline utilizes (1) \textbf{TransDINO} and (2) \textbf{TransDecomp} to disentangle masks and transparency physical properties, while (3) \textbf{DAF-Net} recovers surface normal priors to encode geometric curvature. Subsequently, (4) \textbf{GeoSemTransNet} integrates these multi-modal cues to synthesize a texture-rich opaque RGB image that preserves the transparent object's 3D structure. Extensive experiments demonstrate that our method significantly enhances the accuracy of state-of-the-art depth estimation and reconstruction models on transparent objects by restoring essential photometric cues.

</details>

#### 2026-07-13 - Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems

**Authors:** Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
**Links:** [abs](https://arxiv.org/abs/2607.11099) - [pdf](https://arxiv.org/pdf/2607.11099)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, camera pose estimation, pose estimation

<details>
<summary>Abstract</summary>

Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically require replacing the extraction-and-matching pipeline and introduce substantial computational overhead. Descriptor enhancement offers a compromise by refining existing descriptors within their original format, yet current methods rely on simplified attention mechanisms whose limited contextual modeling constrains the achievable matching quality. To resolve this trade-off between contextual expressiveness and efficiency, we propose Desc++, a lightweight enhancement module that jointly encodes descriptor representations and keypoint geometry and aggregates spatial context through a hybrid architecture that combines order-agnostic global attention with geometry-aware sequential modeling in linear time. The enhanced descriptors retain their original dimensionality and matching interface, enabling integration into deployed V-SLAM systems without modifying the pipeline. Experiments across descriptor matching, correspondence analysis, and system-level benchmarks with four different V-SLAM systems demonstrate that Desc++ improves matching accuracy over the state-of-the-art enhancement method, translates these gains into more accurate and stable trajectory estimation, and achieves a favorable balance between accuracy and efficiency for practical integration into existing real-time V-SLAM pipelines.

</details>

#### 2026-07-13 - WiFi-JEPA: Self-supervised Learning for WiFi-CSI 3D Human Pose Estimation

**Authors:** Doeon Kim, Jungyoon Lee, Seongsin Kim, Seong-heum Kim
**Links:** [abs](https://arxiv.org/abs/2607.11064) - [pdf](https://arxiv.org/pdf/2607.11064)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, simulation

<details>
<summary>Abstract</summary>

WiFi Channel State Information (CSI) enables privacy-preserving human pose sensing in camera-denied environments, but existing WiFi-based pose estimators often fail under environment shifts and rely on costly camera-based annotation pipelines that limit scale. We propose WiFi-JEPA, a self-supervised framework that learns CSI-native representations by predicting masked latent embeddings instead of reconstructing raw CSI signals that may contain hardware-specific artifacts. WiFi-JEPA makes three contributions: (i) CSI-specific tokenization and link masking tailored to the CSI tensor over channel, time, and link (C,T,L); masking entire Tx-Rx antenna links forces the model to predict one spatial link view from others, capturing cross-link correlations informative of 3D spatial structure. (ii) A ray-tracing CSI simulation pipeline that generates diverse unlabeled CSI from randomized geometric primitives, providing scalable pre-training data without pose annotations. (iii) State-of-the-art results on Person-in-WiFi-3D: WiFi-JEPA outperforms prior WiFi-CSI baselines on both single- and multi-person 3D pose estimation under the same evaluation protocol. We also show that simulated CSI provides complementary pre-training signal to real CSI, and that four vision-native SSL objectives degrade performance below training from scratch, whereas WiFi-JEPA consistently improves downstream pose estimation.

</details>

#### 2026-07-12 - Mapping Pamir: Multi-Session Visual-Inertial SLAM and 3D Reconstruction of an Underwater Shipwreck

**Authors:** Michalis Chatzispyrou, Luke Horgan, Hyunkil Hwang, Harish Sathishchandra, Chinmay Burgul, Monika Roznere, Alberto Quattrini Li, Philippos Mordohai, Ioannis Rekleitis
**Links:** [abs](https://arxiv.org/abs/2607.10925) - [pdf](https://arxiv.org/pdf/2607.10925)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, structure from motion, SfM, SLAM, dense reconstruction, sparse reconstruction, mapping

<details>
<summary>Abstract</summary>

This paper presents a framework for multi-session mapping of underwater environments utilizing an affordable action camera. The Visual-Inertial data are augmented by water depth recordings from a dive computer. SVIn2, an open-source VI-SLAM framework, is utilized to generate a trajectory and a sparse reconstruction for each session. Utilizing the keyframes extracted from SVIn2 and the estimated camera poses, a Structure-from-Motion (SfM) framework, COLMAP, is employed for global optimization and to produce a dense reconstruction of the target environment. The presence of calibration targets at fixed locations, when available, is used to estimate the coordinate transformation between different data collection sessions, thus transforming the different sessions into the same coordinate frame. The proposed pipeline is employed for the mapping of a shipwreck off the coast of Barbados. For the first time, both the exterior and the accessible interior parts of the wreck were mapped in two sessions, while a third session employed two cameras with different fields of view.

</details>

#### 2026-07-12 - TriCons-Pose: Triangle-Invariant Geometric Consistency Learning for Category-Level Object Pose Estimation

**Authors:** Zuzhi Yang, Shuai Wang, Mounir Kaaniche, Ziwei Li, Zhiming Cheng, Zhidong Zhao, Chenggang Yan
**Links:** [abs](https://arxiv.org/abs/2607.10754) - [pdf](https://arxiv.org/pdf/2607.10754)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, mapping

<details>
<summary>Abstract</summary>

Category-level object pose estimation is a crucial yet challenging task in both academia and industry, and has achieved remarkable success by leveraging keypoint-based correspondence paradigms. However, most existing methods increasingly rely on stronger feature learning while overlooking whether the established correspondences are geometrically stable across diverse perturbations. This often results in fragile pose recovery under intra-class shape variations and occlusions. To tackle this challenge, we develop a novel Triangle-Invariant Geometric Consistency Learning for Category-Level Object Pose Estimation (TriCons-Pose) to anchor stable keypoints and aggregate pose-invariant cues, yielding reliable canonical mapping and accurate pose estimation. Specifically, a Structure-Consistent Keypoint Detector (SCKD) is designed to identify robust keypoints by enforcing cross-view structural consistency via normalized pairwise distance matching. Moreover, we propose a Pose-Invariant Geometric Aggregator (PIGA) to augment keypoint representations by injecting triangle-based pose-invariant descriptors into a local-to-global attention mechanism. The proposed framework is optimized using standard objective functions while incorporating an additional geometry consistency loss. Extensive experiments on REAL275, CAMERA25, and HouseCat6D datasets demonstrate the effectiveness of the proposed approach.

</details>

#### 2026-07-12 - Incremental Online Scene Reconstruction by 3D Gaussian Triangulation

**Authors:** Yanjin Zhu, Shaofan Liu, Jianke Zhu
**Links:** [abs](https://arxiv.org/abs/2607.10690) - [pdf](https://arxiv.org/pdf/2607.10690)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Incremental scene reconstruction is essential for real-world applications. Although 3D Gaussian Splatting shows strong potential, most existing approaches require offline conversion of the optimized Gaussians into an intermediate implicit field for explicit mesh extraction, which hinders seamless integration with downstream tasks. To address this limitation, we propose a novel online framework that incrementally reconstructs and updates high-fidelity explicit meshes by directly triangulating a dense geometric Gaussian representation, which supports both high-quality rendering and incremental surface reconstruction. Moreover, we present a direct meshing algorithm that efficiently extracts and updates the mesh from the Gaussian set. To ensure mesh accuracy, we enforce a plane-based pulling constraint that dynamically aligns 3D Gaussian primitives to the approximated local surface. Furthermore, our framework significantly reduces memory and computational overhead during long-sequence processing by dynamically freezing fully optimized historical regions. Experiments on public datasets demonstrate that our method outperforms conventional Gaussian-based methods on both rendering quality and reconstruction accuracy.

</details>

#### 2026-07-11 - CSI-Assisted Edge SLAM Testbed Platform for 5G Connected Unmanned Autonomous Vehicles

**Authors:** Boris Radovanovic, Sasa Talosi, Srdjan Sobot, Dejan Vukobratovic
**Links:** [abs](https://arxiv.org/abs/2607.10394) - [pdf](https://arxiv.org/pdf/2607.10394)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, robotics, mapping, localization

<details>
<summary>Abstract</summary>

The evolution from 5G towards 6G reinforces interest in connected robotics, where mobile robots offload compute-intensive tasks to edge servers over ultra-reliable low-latency communication (URLLC) links. Simultaneous localization and mapping (SLAM), a fundamental yet demanding robotics function, is increasingly considered for edge deployment within mobile edge computing (MEC) frameworks. In parallel, integrated sensing and communications (ISAC) enables the use of radio channel information, such as channel state information (CSI), as an additional sensing modality in radio-based SLAM. In this paper, we design and implement a CSI-assisted Edge SLAM testbed integrating a custom unmanned ground vehicle (UGV), a ROS2-based SLAM framework, and a 5G Open Radio Access Network (O-RAN) system. The proposed architecture provides an end-to-end, cross-layer view of ROS2 sensor data streaming over 5G, explicitly enabling CSI exposure and integration into the SLAM pipeline. We analyze ROS2 DDS communication, RTPS packetization, and 5G user-plane transport, and discuss mechanisms for CSI extraction and delivery via O-RAN components. The platform enables realistic experimentation with communication-aware SLAM and reveals key challenges related to latency, data streaming, synchronization, and cross-system integration, providing insights for future 6G-enabled robotic platforms.

</details>

#### 2026-07-10 - DGSfM: Depth-Guided Scale-Aware Global Structure-from-Motion

**Authors:** Sithu Aung, Viktor Kocur, Yaqing Ding, Torsten Sattler, Zuzana Kukelova
**Links:** [abs](https://arxiv.org/abs/2607.09507) - [pdf](https://arxiv.org/pdf/2607.09507)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM, bundle adjustment, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DGSfM: Depth-Guided Scale-Aware Global Structure-from-Motion
- 作者：Sithu Aung, Viktor Kocur, Yaqing Ding, Torsten Sattler, Zuzana Kukelova
- 出版日期：2026-07-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.09507

### 一句话总结
DGSfM 是一种深度感知的全局运动恢复结构（SfM）流水线，通过引入单目深度图作为先验，将传统尺度模糊的对极几何约束转换为尺度感知的约束，并结合视图图过滤与深度一致性剪枝，显著提升了位姿精度。

### 研究问题
全局 SfM 方法依赖尺度模糊的对极几何，易受噪声基线估计和弱视图图约束的影响，同时视觉模糊对之间的假边会降低重建质量。本文旨在解决这些鲁棒性和尺度模糊性问题。

### 核心思路/方法
1. **深度感知相对位姿求解器**：对每对图像，利用深度图将尺度模糊的对极约束转换为尺度感知的相对位姿约束。
2. **视图图过滤与深度一致性剪枝**：通过视图图过滤和基于深度一致性的对应点剪枝，抑制仅在对极几何下看似合理的假边和误匹配。
3. **全局尺度平均与深度引导初始化**：进行全局尺度平均，并用深度引导的位姿-点初始化将单目深度图对齐到公共重建尺度，为全局位姿估计和光束法平差提供稳定初始化。

### 主要贡献
- 提出一种深度感知的全局 SfM 流水线 DGSfM，利用单目深度图作为可扩展先验，同时保持显式多视图优化。
- 通过深度引导的位姿求解、视图图过滤和对应剪枝，在稀疏和稠密匹配前端均显著提升位姿精度。
- 在 ETH3D 和 IMC2021 数据集上，优于强全局 SfM 基线方法。

### 局限性
摘要未提供足够信息。摘要未提及模型对深度图质量的敏感度、计算开销、在极端场景（如纹理缺失或动态场景）下的表现等局限性。

### 阅读优先级
**高**。理由：该工作针对全局 SfM 中的核心尺度模糊和鲁棒性问题，提出了简洁有效的深度引导方案，在标准数据集上取得了明显改进，且代码已开源。对于从事 3D 重建、多视图几何研究的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Global Structure-from-Motion (SfM) is an efficient paradigm for recovering camera poses and sparse 3D structure from unordered images. However, its reliance on scale-ambiguous epipolar geometry makes global positioning sensitive to noisy baseline estimates and weak view-graph constraints, while false edges from visually ambiguous pairs can further degrade reconstruction. We propose DGSfM, a depth-aware global SfM pipeline that uses monocular depth maps as a scalable prior while preserving explicit multi-view optimization. For each image pair, we use a depth-aware relative pose solver to convert scale-ambiguous epipolar constraints into scale-aware relative pose constraints. We further improve robustness through view-graph filtering and depth-consistency-based correspondence pruning, which suppress false edges and matches that remain plausible under epipolar geometry alone. Finally, global scale averaging and depth-guided pose-point initialization align monocular depth maps into a common reconstruction scale and provide stable initialization for global positioning and bundle adjustment. Experiments on ETH3D and IMC2021 show that DGSfM consistently improves over strong global SfM baselines across sparse and dense matching front-ends, achieving substantial gains in pose accuracy. Code is available at https://github.com/sithu31296/DGSfM.

</details>

#### 2026-07-09 - Wat3R: Underwater 3D Geometry Learning without Annotations

**Authors:** Jiangwei Ren, Xingyu Jiang, Zijie Song, Wei Xu, Hongkai Lin, Dingkang Liang, Xiang Bai
**Links:** [abs](https://arxiv.org/abs/2607.08772) - [pdf](https://arxiv.org/pdf/2607.08772)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, depth estimation, point cloud reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wat3R: 无标注水下3D几何学习
- 作者：Jiangwei Ren, Xingyu Jiang, Zijie Song, Wei Xu, Hongkai Lin, Dingkang Liang, Xiang Bai
- 出版日期：2026-07-09
- 分类：3D重建与多视图几何
- 链接：arXiv:2607.08772

### 一句话总结
本文提出一个名为Wat3R的半监督学习框架，无需任何水下标注数据，仅利用无标注水下视频，通过教师-学生架构适应空气到水下场景的前馈3D重建模型。

### 研究问题
如何在水下环境（存在光衰减、散射及缺少大规模高质量3D标注）中，有效估计3D几何结构。

### 核心思路/方法
1. 构建一个交叉域半监督学习框架，采用教师-学生架构，无需任何标注水下数据。
2. 利用大量无标注真实水下视频，让模型学习鲁棒的几何表示。
3. 设计跨视图一致性损失函数：从其他视图提取几何线索，补偿当前视图因水衰减和散射导致的信息退化。
4. 构建了用于几何评估的Water3D数据集，涵盖多样水体与水下场景。

### 主要贡献
1. 提出了首个无需水下标注数据的交叉域半监督3D重建方法（Wat3R）。
2. 设计了跨视图一致性损失，有效缓解水下信息退化问题。
3. 构建了Water3D数据集，填补水下几何评估基准的空白。
4. 在水下多视图深度估计和点云重建任务上，Wat3R超越了当前最优方法。

### 局限性
- 摘要未提供具体局限性信息（如对极暗水体、强浑浊环境的鲁棒性，或训练计算成本等）。

### 阅读优先级
**高**。理由：该工作解决了水下3D重建中标注数据稀缺的关键痛点，提出的无标注半监督学习思路具有较强创新性和实用性，且包含了新构建的评估基准数据集。若您关注水下视觉、无监督/半监督3D重建领域，该论文有重要参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device
- 作者：Fabio Tosi, Luca Bartolomei, Matteo Poggi, Stefano Mattoccia
- 出版日期：2026-07-09
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.08771

### 一句话总结
ZipDepth是一种仅6.1M参数、可在各类设备上实时运行的轻量级零样本单目深度估计网络，通过高效编码器-解码器与大规模知识蒸馏，在零样本精度与部署效率间取得了最佳平衡。

### 研究问题
如何构建一种轻量级、能在嵌入式和移动平台上实时运行，同时具备零样本泛化能力（即应对跨领域场景）的单目深度估计模型。

### 核心思路/方法
- 设计一个可重参数化的高效编码器-解码器架构。
- 利用大规模多域训练集，从基础模型（foundation model）中执行大规模知识蒸馏，将庞大模型的知识迁移至紧凑网络。

### 主要贡献
- 提出了ZipDepth网络，仅包含6.1M参数，可在从服务器GPU到功耗受限设备上以实时速率运行。
- 在五个基准测试上，ZipDepth在轻量级模型中实现了零样本准确度与部署效率之间的最佳权衡。
- 显著缩小了与参数多50倍的基础模型在精度上的差距。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高 — 该工作直接面向嵌入式/移动设备上的实时零样本深度估计，具有明确的部署价值，且方法简洁有效，适合关注轻量级计算机视觉和移动端部署的研究者。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction
- 作者：Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi
- 出版日期：2026-07-09
- 分类：3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.08769

### 一句话总结
本工作提出了PanoLOG，一个结合几何与梯度启发的分区策略（G²PS），专门用于基于全景图像的大规模室外场景3D高斯溅射重建，在保证渲染质量的同时实现可扩展的块并行训练。

### 研究问题
如何高效地将3D高斯溅射（3DGS）扩展到大型室外场景重建，特别是当使用全景图像（ERP格式）时，解决其全向可见性导致现有局部相机视锥分区策略失效、块优化退化为全局训练的问题。

### 核心思路/方法
提出一个两阶段粗到细框架PanoLOG：1）全局粗阶段：利用天球建模和全景单目深度监督获得可靠的初始几何。2）细化阶段：采用G²PS分区策略，通过视差驱动的不确定性构建自适应包围体，并基于梯度的重要性评分分配相机，从而实现块并行优化。

### 主要贡献
1. 提出了PanoLOG，首个针对大规模全景室外场景3DGS重建的两阶段框架。
2. 设计了G²PS分区策略，解决了全景图像全向可见性带来的分区困难。
3. 构建了Pano360，第一个大规模室外场景重建的全景数据集。
4. 实验表明G²PS在保持可扩展块并行训练的同时，取得了最先进的渲染质量；代码、模型和数据集已公开。

### 局限性
摘要未提供足够信息。未提及计算资源需求、对极端光照或动态物体的处理能力、以及分割边界处的伪影或一致性评价等。

### 阅读优先级
高。理由：该工作针对全景图像在大规模室外重建中的关键挑战（分区退化）提出了原创性方法，并贡献了首个专用数据集，方法在渲染质量和可扩展性上均表现优异，对全景3D重建领域有重要推进意义。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：LTM: Large-scale Terrain Model for Wildfire-prone Landscapes
- 作者：Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan
- 出版日期：2026-07-09
- 分类：3D Reconstruction & Multi-view Geometry（3D重建与多视图几何）
- 链接：摘要页 https://arxiv.org/abs/2607.08711 | PDF https://arxiv.org/pdf/2607.08711

### 一句话总结
该文提出一种多模态重建框架，利用过时数字高程模型（DEM）作为几何先验，通过物理驱动的像素-像素对齐，实现野火易发区域大尺度地形的低成本、高保真三维重建。

### 研究问题
如何利用低成本的图像数据，并结合过时的数字高程模型，高效准确地重建野火易发区域的大尺度三维地形，以克服传统方法成本高、更新慢或视觉特征稀疏的问题。

### 核心思路/方法
提出一种多模态重建框架，核心创新在于：采用物理驱动的像素-像素对齐方法，将图像与数字高程模型（DEM）数据直接对齐，从而跳过昂贵且易失败的图像间特征匹配步骤，大幅降低计算复杂度。该框架以DEM作为几何先验，为基于图像的三维重建提供约束，最终生成高保真深度图。

### 主要贡献
1. 提出了一种基于多模态（图像+DEM）的框架，用于大尺度野火易发地形的高效重建。
2. 创新性地引入物理驱动的像素-像素对齐，无需显式特征匹配，显著降低计算开销。
3. 构建了一个基于真实野火区域的大尺度地形仿真器，用于生成包含真实场景的图像数据，支撑算法评估。
4. 实验表明，在给定有姿态图像和过时DEM的情况下，方法在重建精度和计算效率上均显著优于现有技术，且支持实时性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作面向野火应急场景下的大规模地形重建，具有明确的应用价值。核心方法（物理驱动像素对齐替代特征匹配）在计算效率和精度上展现出优势，且通过仿真器进行了系统验证。对于从事3D重建、遥感与应急响应研究的读者，具有直接参考意义。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：HoloTetSphere: Unified TetSphere Mesh Reconstruction for Physical Simulations
- 作者：YaQiao Dai, Renjiao Yi, Zhirui Gao, Wei Chen, Kai Xu, Chenyang Zhu
- 出版日期：2026-07-09
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.08398

### 一句话总结
本文提出HoloTetSphere，一种通过端到端拓扑与几何优化直接构建统一且拓扑连贯的四面体网格的方法，旨在替代传统易出错的表面重建加四面体化流程，以支持物理仿真。

### 研究问题
现有物理仿真就绪的三维重建方法主要依赖分离的两阶段范式（先提取表面几何，再进行易出错的四面体化），而近期Lagrangian方法如TetSphere Splatting虽尝试直接优化体积基元，但其同胚约束限制了拓扑自适应优化，导致生成不连贯的离散四面体，无法用于进一步的物理仿真。本文致力于解决如何直接重建拓扑连贯、统一的四面体网格，且适用于物理仿真的问题。

### 核心思路/方法
1. **拓扑自适应优化框架**：通过端到端的拓扑和几何优化实现整体四面体网格重建。
2. **可微分元素剪枝**：将高斯球与四面体元素耦合，并利用边连接关系估计连续不透明度场，以实现可微分的元素剪枝。
3. **交替几何细化**：联合最小化网格平滑能量与多视图高斯渲染误差，驱动交替的几何细化，同时保持拓扑自适应性。
4. **输出**：构建统一的、拓扑连贯的四面体网格，绕过传统表面网格四面体化步骤。

### 主要贡献
- 提出了一种拓扑自适应的框架，直接从多视图输入重建四面体网格，克服了传统方法拓扑固定且产生离散元素的问题。
- 通过可微元素剪枝与交替几何优化，在保持拓扑适应性的同时实现了几何精度提升。
- 实验表明，该方法在几何精度上超越现有技术，并生成连贯、单一连接的四面体网格，从而简化下游物理仿真流程。

### 局限性
摘要未提供足够信息。摘要中未讨论方法在复杂拓扑、计算效率、鲁棒性或在极端稀疏视图条件下的表现，也未提及任何失败的案例或潜在的应用限制。

### 阅读优先级
**高**  
理由：该方法直接解决三维重建到物理仿真流程中的关键瓶颈（传统四面体化易出错、Lagrangian方法拓扑不连贯），且通过端到端优化实现了拓扑自适应的四面体网格重建，在几何精度和网格连贯性上超越现有技术，对计算机图形学与物理仿真领域具有重要潜在价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：3D Reconstruction of deciduous Trees using low-cost UAV- and Crane-based Photogrammetry for Monitoring Shoot Elongation across entire Canopies  
- 作者：Stephan Nebiker, Micha Tschanz, Nando Amport, Frederik Baumgarten  
- 出版日期：2026-07-08  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2607.07905  

### 一句话总结
本文探索利用低成本无人机（UAV）和吊车多相机系统进行摄影测量，以重建落叶乔木三维模型，从而监测整个树冠的枝条伸长（初级生长）。

### 研究问题
如何通过低成本摄影测量技术（UAV与CraneCam）在真实条件下获取落叶乔木高精度、高完整性的三维点云，以支持整个生长季内枝条伸长的连续监测。

### 核心思路/方法
1. 使用重量不足250g的消费级UAV和一套多相机CraneCam系统，在整个生长季内采集两个研究区的数据。  
2. 采用摄影测量数据采集与处理策略，重点分析三维点云的精度、分辨率和完整性。  
3. 引入一种创新的3D打印“地面真值”枝条，用于评估重建细部结构（如细枝条）的能力。  

### 主要贡献
1. 证明了消费级UAV（<250g）即可实现整棵树5-6 mm的点云精度。  
2. 不同无人机型号的三维重建完整性达到92%至98%。  
3. 提出了利用3D打印人造枝条作为基准，评估对细薄枝条等精细结构的重建效果。  
4. 探讨了基于摄影测量点云进行整树骨架化的初步实验与操作挑战。  

### 局限性
摘要未提供足够信息，无法明确说明该方法的适用场景限制、无法重建的枝条类型、不同天气或季节的影响，以及与其他传感器（如激光雷达）的对比结果。

### 阅读优先级
中  
**理由**：该研究针对树木初级生长监测这一特定生态学需求，方法上具有创新性（低成本、轻量化设备、高精度），并展示了实用结果。但摘要未涉及算法细节、实验对比或后续骨架化方法的具体效果，对于非生态遥感领域或无硬件部署计划的研究者可能参考价值有限。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Monocular Vision Based Control Framework for Grasping
- 作者：Shail Jadav, Dongheui Lee
- 出版日期：2026-07-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[论文摘要页](https://arxiv.org/abs/2607.07897) | [PDF](https://arxiv.org/pdf/2607.07897)

### 一句话总结
本文提出一种仅使用单目RGB视觉和位置控制夹爪的统一抓取框架，通过语言估计物体刚度并适应性地抓取软硬物体，在真实实验中验证了对多种食品及家庭物品的稳定抓取。

### 研究问题
如何在非结构化环境中，仅依靠单目视觉（无需触觉、物体模型或专用夹爪）实现对软性（可变形）和刚性物体的统一抓取控制。

### 核心思路/方法
框架融合多项计算机视觉技术：开放词汇目标检测、图像分割、边界感知点分配、实时点跟踪、单目深度估计，以及一个基于语言描述的刚度估计模型。该模型利用物体的语义信息预判其柔顺性，从而在接触前选择抓取策略。对于可变形物体，使用Procrustes距离（基于跟踪关键点）作为形变视觉代理来调整抓取；对于刚性物体，则通过跟踪点距离的缩放调节夹爪宽度。全部控制仅依赖RGB输入和位置控制夹爪。

### 主要贡献
1. 提出一个统一的单目视觉抓取框架，能同时处理软性（可变形）和刚性物体，无需专用传感器或物体模型。
2. 引入语言基础刚度估计模型，从物体语义推断其预期柔顺性，提供接触前的抓取策略先验。
3. 针对可变形物体设计基于Procrustes度量的抓取自适应方法，作为形变的视觉代理信号。
4. 在真实Franka Emika Research 3臂上，用多种软硬物体（生菜、马苏里拉奶酪、牛角包、纸巾、硬塑料瓶）验证了框架的有效性和泛化性。

### 局限性
摘要未提供足够信息评估局限性，例如在极端光照、遮挡、高速运动或完全透明物体上的表现。

### 阅读优先级
中  
理由：该方法将视觉与语言结合实现软硬物体统一抓取，具有传感器高效性和实际应用潜力，尤其适合食品处理等场景。但实验物体种类有限，且未评估极端情况下的鲁棒性，对于追求工程落地的读者可能有参考价值，理论创新性为中等。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Time-to-Collision Based Dynamic Obstacle Avoidance Using Pretrained Vision Models for Robots in Unstructured Environments
- 作者：Erik Jagnandan, Mulugeta Haile, Gregory Barber, Pratik Chaudhari
- 出版日期：2026-07-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.07885

### 一句话总结
本文提出一种基于碰撞时间（TTC）的视觉动态避障方法，利用预训练深度估计和特征匹配模型，无需训练即可实现非结构化环境中的机器人避障，并在真实数据集上验证了数据高效性和可解释性。

### 研究问题
如何在非结构化户外环境中实现动态障碍物避障，同时避免大规模机器人专用训练数据和仿真策略带来的数据效率低、仿真到现实迁移困难等问题。

### 核心思路/方法
- 利用预训练单目深度估计模型 UniDepth 从 RGB 视频生成稠密深度图，无需立体相机或激光雷达。
- 扩展 SuperPoint 和 SuperGlue 特征匹配管线，在长帧序列中跟踪关键点，并通过相机内参和预测深度将2D像素投影到3D。
- 对3D关键点进行束调整（bundle adjustment）以优化位姿，计算每个关键点的碰撞时间（TTC）。
- 在地平面选择2D运动基元，使机器人远离最小TTC关键点的最近接近点。

### 主要贡献
1. 提出一种完全基于真实世界数据、无需模型训练的视觉动态避障方法，避免了仿真到现实的迁移问题。
2. 利用预训练模型（UniDepth、SuperPoint、SuperGlue）实现数据高效性，仅需74秒数据用于超参数调优，无需数千小时训练数据。
3. 在M3ED数据集上验证性能：识别TTC<1秒帧的精确率0.49、召回率0.38；正确避障方向生成率为84%；对22个物理障碍中的20个检测到至少一个TTC<1秒的帧。
4. 方法保持可解释性和泛化性，适用于多种障碍物类型。

### 局限性
摘要未提供足够信息。未提及方法在复杂场景（如密集障碍物、高速运动）下的鲁棒性、实时性表现，或对光照、纹理等环境因素的敏感性。

### 阅读优先级
**高**
理由：本文针对动态避障这一机器人领域核心难题，提出了一种无需训练、数据高效的解决方案，并使用了预训练视觉模型，具有较强的实用价值和可迁移性。实验结果在真实数据集上表现合理，且方法可解释性强，适合关注自主导航、避障与计算机视觉交叉研究的读者。

</details>

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

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-13 - ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space

**Authors:** Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan
**Links:** [abs](https://arxiv.org/abs/2607.11673) - [pdf](https://arxiv.org/pdf/2607.11673)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** video reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, world model

<details>
<summary>Abstract</summary>

We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds. At the heart of our framework is a unified Spatial Generative Primitive (SGP), a compact tuple of a high-quality panorama and a spatial point cloud that delivers an efficient description of any 3D space. Multimodal inputs are first lifted into this primitive; a 3D-consistent panoramic video generator then explores the primitive along a planned trajectory; finally, our panoramic video reconstruction engine converts the generated video into a clean, photorealistic 3D Gaussian Splatting (3DGS) world. This pipeline covers two regimes: rich inputs (multi-view sets, casual video) are lifted into the SGP through a geometry-rigorous recovery that mirrors the observed scene, while a single image or sentence is completed generatively into a creative world. The result is one low-barrier engine for general 3D content creation that further anchors generated worlds to geographic points of interest, enabling map-native spatial exploration at consumer scale. Experiments show that ABot-3DWorld 0 sets the state of the art among open-source methods and demonstrates stronger scene fidelity than Marble under rich multimodal inputs.

</details>

#### 2026-07-13 - HyperGS: Fast and Generalizable Gaussian Video Representation

**Authors:** Fatimah Zohra, Chen Zhao, Shuming Liu, Yahya Al Malallah, Bernard Ghanem
**Links:** [abs](https://arxiv.org/abs/2607.11500) - [pdf](https://arxiv.org/pdf/2607.11500)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Gaussian Splatting has emerged as an effective representation for video, but existing methods rely on per-video optimization. This leads to slow encoding and limits generalization across videos. To amortize this optimization, we propose HyperGS, a feedforward, optimization-free approach that directly predicts Gaussian representations from any video in a single forward pass, speeding up encoding and decoding by orders of magnitude while generalizing to out-of-distribution videos at higher resolutions. In HyperGS, we design a factorized spatiotemporal Transformer to extract tokens from video, and a learnable query-based Transformer to obtain 8-parameter Gaussian representations for each video frame. We find that naively predicting Gaussians across diverse videos induces a needle-like degeneration that collapses training, and address this with a rank-based geometric regularizer whose strength adapts dynamically to stabilize optimization. HyperGS achieves encoding at $10^4$--$10^5\times$ the speed of per-video Gaussian optimization at matched reconstruction quality while generalizing zero-shot to $720p$ video, enabling higher-resolution rendering without re-encoding. HyperGS improves PSNR by +2.9--3.1 dB over the prior video encoders on K400, SSv2, and UCF101 at a smaller video representation size. By predicting explicit 2D Gaussians in a single forward pass, HyperGS combines the fast, flexible rendering of Gaussian Splatting with the speed and generalization of feedforward prediction, advancing Gaussians as a practical direction for fast and generalizable video representation.

</details>

#### 2026-07-13 - AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling

**Authors:** Yingji Zhong, Dave Zhenyu Chen, Fuzhao Ou, Youyu Chen, Zhihao Li, Lanqing Hong, Dan Xu
**Links:** [abs](https://arxiv.org/abs/2607.10995) - [pdf](https://arxiv.org/pdf/2607.10995)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

Recent generalizable 3D Gaussian Splatting models have advanced long-sequence novel view synthesis (NVS), but at the cost of substantial redundant computation. We identify that the redundancy can be mitigated based on two observations: (i) high-precision geometry is not strictly required for high-quality NVS; (ii) appearance learning is generally easier than geometry recovery. Motivated by these insights, we propose an asymmetric architecture that decouples geometry and appearance modeling. The geometry branch processes coarse-grained tokens with most of the parameters for multi-view reconstruction, while the appearance branch operates on fine-grained tokens to capture details using significantly fewer parameters. The two branches interact through bilateral connections, enabling mutual guidance for their respective tasks. This task-aware asymmetry reduces the computational redundancy and allocates the computation more judiciously, thereby increasing parameter efficiency and enabling smaller models to achieve strong performance. On 32-view 960P inputs, our model matches optimization-based methods while delivering nearly 800x speedup, and surpasses the zero-shot performance of state-of-the-art generalizable models with markedly fewer parameters and reduced training/inference overhead, achieving an overall efficiency improvement.

</details>

#### 2026-07-12 - DP-Splat: Bayesian Nonparametric Complexity Control for Gaussian Splatting

**Authors:** Aqi Dong
**Links:** [abs](https://arxiv.org/abs/2607.10912) - [pdf](https://arxiv.org/pdf/2607.10912)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting represents scenes as finite mixtures of anisotropic Gaussians whose number of components $K$ is set by heuristic density control or user caps. Variational Bayes Gaussian Splatting (VBGS) recast splat fitting as conjugate variational inference, but $K$ remains fixed. We replace the finite symmetric Dirichlet over mixture weights with a truncated stick-breaking Dirichlet-process prior -- and, as a theory-backed alternative, a sparse overfitted finite Dirichlet -- so that the number of occupied components adapts to the data while every update remains a closed-form coordinate-ascent step; a natural-gradient stochastic variant makes the per-step cost independent of the number of points. We give an exact monotonicity guarantee, a rigorous truncation-error bound correcting an anti-conservative large-$α$ approximation in common use, and an honest account of what the fitted number of components estimates. Empirically: (i) the effective complexity $\hat{K}$ adapts to scene complexity and recovers the true $K$ within $\pm 1$ on well-separated synthetic data with regime-appropriate concentration; (ii) a deconfounded comparison shows the DP prior's contribution is complexity selection, not per-component efficiency -- converged DP fits exceed single-pass fixed-$K$ VBGS by +2.7 dB at matched budgets yet tie an equally converged fixed-$K$ baseline, and on 3D scenes DP-Splat matches or exceeds VBGS's held-out color prediction with 5.9-7.6x fewer components; (iii) the posterior-predictive color variance is well calibrated on model-matched synthetic data; and (iv) the ordering suggested by exact-posterior asymptotics reverses under mean-field coordinate ascent: the DP prior resists over-splitting while the sparse finite mixture saturates its truncation, a gap between variational practice and posterior asymptotics documented across three orders of magnitude in $N$.

</details>

#### 2026-07-09 - Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery

**Authors:** Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos
**Links:** [abs](https://arxiv.org/abs/2607.08408) - [pdf](https://arxiv.org/pdf/2607.08408)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, scene representation, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery
- 作者：Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos
- 出版日期：2026-07-09
- 分类：Neural Scene Representations & Rendering；3D Reconstruction & Multi-view Geometry
- 链接：摘要：https://arxiv.org/abs/2607.08408 ；PDF：https://arxiv.org/pdf/2607.08408

### 一句话总结
Track2Map是一种在线、可变形3D高斯溅射SLAM管线，能够从手术视频中联合优化相机轨迹与三维可变形场景，无需依赖机器人运动学先验。

### 研究问题
如何在机器人辅助微创手术（RAMIS）中，从手术视频在线进行稠密、可变形三维解剖重建，并在缺少或带有噪声的相机轨迹先验下实现鲁棒的定位与建图（SLAM）。

### 核心思路/方法
1. **在线联合优化**：构建一个在线3D高斯溅射管线，同时优化相机轨迹和三维可变形场景。
2. **轨迹锚定变形初始化**：使用密集的二维点轨迹进行变形初始化，以稳定存在组织运动和模糊视觉线索时的优化过程。
3. **运动感知位姿优化**：利用点轨迹统计信息，通过检测静态相机时期来分离相机运动与场景变形，并在增量建图过程中减少漂移。

### 主要贡献
- 提出Track2Map，一种在线的可变形SLAM方法，能直接从未知或带噪的相机轨迹先验的术中视频中联合优化相机位姿和场景。
- 引入轨迹锚定变形初始化策略，利用密集2D点轨迹稳定优化。
- 利用点轨迹统计实现运动感知位姿优化，有效分离相机运动与组织变形，减少漂移。
- 在StereoMIS数据集上的实验表明，Track2Map在重建质量和相机轨迹估计上优于现有SLAM方法，甚至可与使用轨迹先验的非SLAM方法竞争。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对手术机器人视觉中的核心问题（缺少相机先验时的在线可变形SLAM）提出了新颖的联合优化管线，并展示了优于现有方法的实验性能。对于从事手术机器人、SLAM或可变形场景重建的研究者具有直接参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting
- 作者：Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan
- 出版日期：2026-07-09
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.08016

### 一句话总结
LightCrafter 提出一种混合流水线，通过将视频重光照转化为对基于物理渲染（PBR）代理视频的翻译，利用视频扩散模型精细调整以实现可控且时间一致的重光照。

### 研究问题
如何在长视频中实现既保持时间一致性、又符合物理光照规律（如全局光照）的可控重光照，同时克服传统逆渲染方法噪声大、生成式方法控制受限的缺陷。

### 核心思路/方法
核心思路是构建一个混合流水线：不为直接从输入视频翻译到目标光照下的视频，而是先通过逆渲染和PBR生成输入视频在目标光照下的代理渲染视频，然后使用经过合成视频对和真实无配对视频微调的CogVideoX扩散模型，将该PBR代理视频翻译为最终的重光照结果。这样，光照目标已被“烘培”进PBR代理中，扩散模型无需学习环境映射等光照概念，从而提升控制精度和长时一致性。

### 主要贡献
1. 提出LightCrafter混合流水线，结合PBR渲染和视频扩散模型，实现可控且一致的重光照。
2. 通过将光照目标嵌入PBR代理，简化扩散模型的输入空间，增强光照控制灵活性并自然保持长时间一致性。
3. 在现有真实世界重光照基准上超越此前最优方法，并贡献了用于进一步分析的合成基准。
4. 将公开发布数据集、基准、评估指标和代码。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对视频重光照中的关键难题（时间一致性与物理真实性）提出了新颖的混合方法，在基准上取得超越结果，且涉及当前热门的扩散模型与物理渲染结合，方法具有实用潜力。

</details>

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

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-13 - Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model

**Authors:** Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li
**Links:** [abs](https://arxiv.org/abs/2607.11643) - [pdf](https://arxiv.org/pdf/2607.11643)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation

<details>
<summary>Abstract</summary>

Recent foundation image and video generation models offer strong generalization and controllability, but their direct application to embodied scenarios is limited by requirements for multi-view consistency, geometric coherence, and robot embodiment constraints. Existing methods typically adapt foundation models with limited robot data, often sacrificing visual knowledge acquired during large-scale pre-training. We present Xiaomi-Robotics-U0, a 38-billion-parameter multimodal autoregressive model for unified embodied synthesis. It treats embodied generation as an extension of foundation image and video generation and jointly optimizes text-to-image generation, image editing, embodied scene generation, embodied transfer, and embodied video generation. This unified framework preserves the generalization of the pre-trained world foundation model while adapting it to embodied settings. Xiaomi-Robotics-U0 is the first model to support high-quality multi-view scene generation across multiple robot embodiments and to introduce structured, controllable embodied transfer for fine-grained editing while preserving multi-view consistency and interaction dynamics. It achieves state-of-the-art results on single-step and sequential generation tasks, outperforming GPT-Image-2.0 in human evaluations of embodied scene generation and transfer, ranking first on World Arena for embodied video generation, and improving the out-of-distribution success rate of pi_0.5 from 36.9% to 63.2% on challenging real-world manipulation tasks. These results show that foundation world models can serve both as embodied world models and scalable data engines for embodied intelligence. Code and checkpoints are available at https://robotics.xiaomi.com/xiaomi-robotics-u0.html.

</details>

#### 2026-07-13 - SegDiff: Segmented Trajectory Diffusion for Consistent and Adaptive Robot Manipulation

**Authors:** Haidong Cao, Wenjun Cao, Quanhao Li, Sicheng Xie, Zhiying Du, Jiaqi Leng, Zuxuan Wu, Yu-Gang Jiang
**Links:** [abs](https://arxiv.org/abs/2607.11027) - [pdf](https://arxiv.org/pdf/2607.11027)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>Abstract</summary>

Imitation learning enables robots to acquire manipulation skills from demonstrations by mapping observations to actions. Existing approaches predict either short-horizon continuous action sequences or discrete keyposes. However, continuous prediction methods suffer from compounding errors due to short prediction horizons and struggle with multi-modal action distributions, whereas keypose-based methods necessitate an external planner, constraining real-time applicability. To address these challenges, we introduce SegDiff, a closed-loop visuomotor policy that integrates the strengths of both paradigms. SegDiff decomposes demonstrations into motion segments between keyposes and learns to predict the continuous trajectory from the current state to the next keypose, enabling long-horizon prediction with real-time refinement. Furthermore, we leverage the capability of diffusion models and DDIM inversion to propose a Dynamic Temporal Ensembling mechanism, which allows the policy to efficiently respond to dynamic environments and mitigate discontinuities caused by inconsistent multi-modal sampling. SegDiff demonstrates significant performance gains over existing approaches across various simulated and real-world scenarios, indicating its strong ability to reason over extended temporal dependencies while maintaining real-time adaptability and control stability.

</details>

#### 2026-07-11 - PrismAD: Decoupled Planning via Semantic Mixture-of-Planners for End-to-End Autonomous Driving

**Authors:** Kang Ding, Zhigui Lin, Hongsong Wang, Jie Gui, Qi Liu, Zhe Wang, Luqi Tang, Lei He
**Links:** [abs](https://arxiv.org/abs/2607.10336) - [pdf](https://arxiv.org/pdf/2607.10336)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

This letter presents PrismAD, a decoupled end-to-end autonomous driving framework based on a Semantic Mixture-of-Planners. Existing planners usually aggregate heterogeneous scene tokens into a coupled representation space, forcing a single planning branch to jointly model agent interaction, road geometry, and driving intention. Such coupling may weaken factor-specific reasoning and obscure the contribution of different planning cues. To address this limitation, PrismAD partitions scene tokens into interaction, geometry, and intent groups, and assigns them to independent planning experts with the same architecture but separate parameters. Each expert learns a specialized motion-planning representation, while a semantics-aware router adaptively aggregates expert predictions with separate routing weights for motion prediction and ego planning. Sparse top-$K$ activation with noisy gating is further introduced to improve routing robustness and reduce unnecessary expert computation. Extensive experiments on the nuScenes open-loop dataset and NeuroNCAP closed-loop benchmark demonstrate that PrismAD exhibits competitive performance. Our code will be released soon.

</details>

#### 2026-07-09 - DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

**Authors:** Yunchao Yao, Zhuxiu Xu, Tianqi Zhang, Zixian Liu, Sikai Li, Zhenyu Wei, Feng Chen, Dihong Huang, Kechang Wan, Chenyang Ma, Shuqi Zhao, Shenghua Gao, Masayoshi Tomizuka, Yi Ma, Mingyu Ding
**Links:** [abs](https://arxiv.org/abs/2607.08751) - [pdf](https://arxiv.org/pdf/2607.08751)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation
- 作者：Yunchao Yao, Zhuxiu Xu, Tianqi Zhang, Zixian Liu, Sikai Li, Zhenyu Wei, Feng Chen, Dihong Huang, Kechang Wan, Chenyang Ma, Shuqi Zhao, Shenghua Gao, Masayoshi Tomizuka, Yi Ma, Mingyu Ding
- 出版日期：2026-07-09
- 分类：具身智能/机器人/AR应用
- 链接：https://arxiv.org/abs/2607.08751

### 一句话总结
该论文提出了DexVerse，一个大规模模块化灵巧操作基准，包含100项任务、多种机器人构型、可配置视觉变化和3,180条演示数据，并评测了多种代表性方法，揭示了任务泛化和视觉运动鲁棒性方面的显著挑战。

### 研究问题
现有灵巧操作基准在任务多样性、数据覆盖范围、机器人构型支持以及可控视觉变化方面存在局限，难以系统性地评估策略在跨任务和跨构型下的泛化能力。

### 核心思路/方法
构建一个模块化基准，具体包括：
1. 集成100项涵盖抓取、重定位、交互式物体操作、工具使用、双手协调、非抓取控制、接触丰富行为、多目标执行以及长时多阶段任务等多种技能的任务。
2. 支持3种机器人臂和6种灵巧手，并具备可扩展性。
3. 提供可配置的纹理、背景、光照和相机视角等视觉变化，用于评估视觉运动泛化。
4. 提供一个基于VR的遥操作接口，并收集3,180条包含本体感受、RGB、深度、点云和状态观测的同步演示数据。
5. 选取Diffusion Policy、DP3、OpenVLA和π₀.₅四种代表性方法在19项任务上进行基准测试。

### 主要贡献
1. 提出了一个大规模、模块化的灵巧操作基准DexVerse，包含丰富的任务、构型及视觉变化。
2. 提供了3,180条多模态同步演示数据及VR遥操作接口，便于获取高质量演示。
3. 在19项任务上对多种代表性方法进行了系统基准测试，揭示了跨任务泛化与视觉运动鲁棒性方面的显著挑战，验证了DexVerse作为通用灵巧操作测试平台的价值。

### 局限性
摘要未提供关于DexVerse基准在真实机器人部署、计算成本、任务难度分布、数据收集成本以及所测试方法在其他任务上的性能上限等具体实验细节或局限性信息。

### 阅读优先级
中
理由：该论文提供了一个综合性的基准和评测结果，对于研究灵巧操作泛化问题、需要多任务多构型评估资源的领域具有直接参考价值；但摘要未深入分析算法性能差异或具体实验结果，故优先级设为中等。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving
- 作者：Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, Jia Hu, Binyang Song
- 出版日期：2026-07-09
- 分类：Embodied / Robotics / AR Applications（主要类别）；未提供次要类别
- 链接：摘要链接: https://arxiv.org/abs/2607.08375；PDF链接: https://arxiv.org/pdf/2607.08375

### 一句话总结
本文提出WCog-VLA，一种双层次世界认知视觉-语言-动作模型，通过结合语义世界预测与生成世界演化，在NAVSIM基准上实现PDMS评分92.9的领先性能，推动端到端自动驾驶从被动驾驶向主动驾驶转变。

### 研究问题
现有视觉-语言-动作（VLA）模型在端到端自动驾驶中缺乏全面的世界认知，或存在碎片化的世界预见能力，导致模型只能进行被动驾驶（reactive driving），无法实现主动驾驶（proactive driving）。

### 核心思路/方法
- **双层次世界认知框架（Dual-Level World-Cognitive）**：
  - **语义层次**：通过集成3D空间感知和注入代理令牌（agent tokens）来捕捉世界动态，并实现面向博弈论链式思考（Game-theoretic Chain-of-Thought, Game-CoT）推理，统一世界认知与推理。
  - **生成层次**：引入对齐的解耦扩散Transformer（Aligned Decoupled Diffusion Transformer, ADDT）作为生成世界模型，合成物理上合理的多智能体联合轨迹；通过场景表示对齐减少去噪步骤，显著加速推理。
- **数据集构建**：创建包含85,000个Game-CoT注释的大规模数据集，支持策略推理训练。
- **实验验证**：在NAVSIM基准上进行了广泛实验，结果达到SOTA（PDMS评分92.9）。

### 主要贡献
1. 提出WCog-VLA，首个将语义世界预测与生成世界演化结合的双层次世界认知VLA框架，实现主动驾驶。
2. 提出Game-CoT推理机制，将博弈论思想融入视觉-语言推理链。
3. 提出ADDT生成模型，通过场景表示对齐减少去噪步骤，加速推理。
4. 构建包含85k Game-CoT注释的大规模数据集，促进策略推理研究。
5. 在NAVSIM基准上取得SOTA性能（PDMS评分92.9）。

### 局限性
摘要未提供足够信息（例如未提及模型的计算开销、在不同场景下的泛化能力、对异常或边缘情况的鲁棒性等）。

### 阅读优先级
**高**  
理由：该论文针对自动驾驶中VLA模型缺乏世界认知的核心问题，提出了兼具语义推理与生成预测的双层次框架，并在权威基准上取得SOTA结果。方法创新性较强（如Game-CoT、ADDT对齐策略），且附带大规模数据集，对主动驾驶和端到端自动驾驶领域具有重要参考价值。

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
