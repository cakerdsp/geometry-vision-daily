# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：59
- 分类分布：
  - Neural Scene Representations & Rendering: 18
  - 3D Reconstruction & Multi-view Geometry: 17
  - Embodied / Robotics / AR Applications: 16
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的中文科研趋势综合分析。

---

#### 今日主要趋势

1.  **几何基础模型向“度量”与“微型化”演进**：单目几何估计（深度、法向、点云）不再仅追求视觉上合理的预测，而是越来越强调**度量尺度（Metric Scale）** 的准确性。这一趋势体现在多个工作中：
    - `VIDAR` 通过耦合视觉-惯性里程计（VIO）与基础模型（Depth Anything 3），为稠密预测提供“度量锚点”，解决了单目模型的尺度模糊问题。
    - `DROID-ANCHOR` 则将里程计信号直接集成到SLAM系统的迭代优化中，学习时变的不确定性以平衡视觉与度量信息。
    - `DepthART` 关注模型的落地部署，通过抗偏置采样和相机条件微调，首次将基础模型的泛化能力成功压缩至微型模型，使其能在低算力设备上实现快速、有尺度的深度估计。

2.  **3D高斯泼溅（3DGS）进入“精细化瓶颈探索”与“鲁棒工程化”阶段**：随着3DGS的普及，研究焦点从基本的渲染质量转向解决其内在缺陷和实际部署难题。
    - **鲁棒性**：`Exploration Matters...` 从数学上识别了3DGS优化中的“模糊陷阱”问题，并提出极简的随机探索策略来跳出局部次优解，这在理论层面是重要补充。
    - **效率与鲁棒传输**：`CaT-GS` 系统分析了大规模场景下的渲染效率瓶颈（冗余预处理、负载不均），并设计帧间缓存机制实现10倍加速。`Packet-Loss Robust 3D Gaussian Compression...` 则首次针对网络流媒体场景，设计了原子锚点打包和GNN错误隐藏机制，抵御网络丢包。
    - **复杂输入**：`Splat-based 3D Scene Reconstruction with Extreme Motion-blur` 直面低光照、快速运动等极端场景，将模糊输入下的位姿估计与场景重建联合优化。

3.  **多模态融合与协同，从“视觉为主”到“几何+语义+传感”**：为了克服单一模态（如纯2D视觉）的局限性，论文普遍采用多模态融合策略，并探索不同模态间的协同计算。
    - **视觉+3D几何**：`When 2D Cues Fail` 认识到纯2D线索在图像篡改定位中的不足，主动引入深度和法向等3D几何先验，并设计了可靠性估计模块以应对几何噪声。
    - **视觉+惯性/里程计**：`VIDAR` 和 `DROID-ANCHOR` 均将里程计信号作为关键度量锚点，与视觉信息深度融合，解决了单目SLAM和深度估计的尺度漂移问题。
    - **视觉+语义+几何**：`Robust Multimodal Dynamic Object Segmentation` 整合了2D点轨迹、3D重建和语义信息，通过 Transformer 和特征聚类，实现了更鲁棒的动态物体分割。
    - **多视图协同**：`MuViSeg` 通过联合自注意力机制，直接在实例分割层面建立多视图对应关系，弥补了传统点/像素匹配与物体级应用之间的鸿沟。

#### 技术路线观察

| 技术方向 | 论文示例 | 技术侧重点 |
| :--- | :--- | :--- |
| **几何基础模型** | `VIDAR`, `DROID-ANCHOR`, `DepthART` | 聚焦于**度量校准**（注入高频里程计、学习不确定性）和**模型小型化**；倾向于将基础模型作为特征提取或深度补全的“插件”，再与经典SLAM架构或轻量级模型结合。 |
| **3D/4D 重建** | `Plenoptic Condensation`, `Splat-based...` | 侧重**特定挑战下的鲁棒重建**（如运动模糊）和**新重建范式探索**（如“汤状”元素自适应凝聚），追求更高的空间可变表示能力和细节保真度。 |
| **神经场景表示（3DGS）** | `Exploration Matters...`, `CaT-GS`, `Packet-Loss Robust...`, `QIRF` | 从**渲染/重构性能瓶颈**（优化陷阱、效率、存储）出发，进行理论分析（模糊陷阱）和工程优化（缓存、压缩、错误隐藏）；方法更具**系统性和鲁棒性**，关注从训练到传输的全链条。 |
| **机器人/AR 应用** | `GeoWorldAD`, `UMCP`, `Lifelong Localization`, `BIM-enabled...` | 强调**实用化**和**特定任务驱动**。例如，自动驾驶需要显式的几何推理和未来预测；室内机器人需要结合BIM进行知识驱动的导航；无人机检测需要针对小目标进行优化。模型设计更注重实时性、低成本和环境适应性。 |

#### 值得优先阅读的论文

1.  **`DROID-ANCHOR`**：它直接回应了单目SLAM领域长期存在的“尺度模糊”问题，并且方法设计精妙（LSTM编码里程计、不确定性感知后端）。阅读全文可以了解如何优雅地将非视觉传感器（里程计）与循环神经架构深度融合，对从事视觉SLAM、多传感器融合的研究者价值最高。

2.  **`Exploration Matters for Escaping the Blur Trap in 3DGS`**：这篇论文的价值在于**理论贡献**。它首次形式化了3DGS优化中的一个根本性缺陷（模糊陷阱），并通过极简方法（随机播种/分裂）有效缓解。理解其背后的数学分析和问题洞察，对于改进3DGS系列算法极具启发性。

3.  **`Robust Multimodal Dynamic Object Segmentation`**：该文试图解决一个公认的难题（动态物体分割），而且解决方案（融合点轨迹、3D重建和语义）全面且具有代表性。其创新的“自适应模态主导”机制和“点查询SAM”后处理，都是值得深入研究的点。它对视觉分割、场景理解乃至3D重建都有参考价值。

4.  **`DepthART`**：该工作解答了一个现实问题：“如何在微型设备上实现强大的单目深度估计？”它识别并解决了小模型过拟合和度量不稳定的瓶颈，方法（相机条件微调）简洁有效。适合关注模型落地和低算力部署的研究者。

5.  **`Packett-Loss Robust 3D Gaussian Compression via Atomic Packaging...`**：这篇论文开辟了3DGS研究的一个**新方向**：网络传输鲁棒性。随着3DGS在云渲染、VR/AR中的普及，这个问题将愈发关键。原子打包和GNN修复的思路很有启发性。

#### 可能的研究机会

1.  **融合几何与语义的“鲁棒度量”SLAM**：现有的度量SLAM（如`DROID-ANCHOR`）依赖惯性或轮速计。一个开放问题是：**能否从纯视觉信号中学习到更鲁棒的度量线索？** 例如，结合语义信息（已知尺寸的物体）或几何先验（平面、直线结构）来直接约束尺度，从而摆脱对特定传感器的依赖。

2.  **面向“实时光线追踪”的高效3DGS渲染**：`CaT-GS`解决了传统光栅化的效率问题。但**将3DGS与更真实的物理渲染（如光线追踪）结合时，将面临全新的计算瓶颈**。探索如何利用3DGS的显式表示进行高效的近似光线追踪，或设计新的加速结构，是一个前沿趋势。

3.  **多模态动态场景的联合优化与泛化**：`Robust Multimodal Dynamic Object Segmentation` 展示了多种模态融合的力量。机会在于：**将此框架推广到更一般的动态场景理解任务**，如动态场景下的4D重建、动态物体的属性（材质、运动）估计。同时，研究如何使模型**从有限或质量不佳的模态输入中泛化**，例如当某种传感器故障时的自适应降级。

4.  **基础模型在“不可靠”数据下的应用**：`When 2D Cues Fail` 和 `Splat-based...` 都显示，基础模型在面对噪声或模糊数据时性能会下降。一个重要的机会是：**

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-21T10:19:48-04:00
**Total number of papers:** 59
**Number of papers added in the latest update:** 22
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

#### 2026-07-20 - Fine-Detail Monocular Geometry Estimation with Self-Guided Sparse Volumetric Refinement

**Authors:** Lingyu Kong, Ruicheng Li, Ruicheng Wang, Sicheng Xu, Chengtang Yao, Jianfeng Xiang, Jiaolong Yang
**Links:** [abs](https://arxiv.org/abs/2607.17967) - [pdf](https://arxiv.org/pdf/2607.17967)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** point map, monocular geometry

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fine-Detail Monocular Geometry Estimation with Self-Guided Sparse Volumetric Refinement
- 作者：Lingyu Kong, Ruicheng Li, Ruicheng Wang, Sicheng Xu, Chengtang Yao, Jianfeng Xiang, Jiaolong Yang
- 出版日期：2026-07-20
- 分类：Geometry Foundation Models
- 链接：摘要URL: https://arxiv.org/abs/2607.17967 ; PDF: https://arxiv.org/pdf/2607.17967

### 一句话总结
本文提出一种自引导稀疏体素精化（SSR）方法，通过将单目几何估计从2D图像空间提升到3D空间，显著提升细粒度几何（如薄结构和小物体）的重建保真度。

### 研究问题
现有单目几何估计模型在局部3D结构（尤其是细粒度细节，如薄结构和小物体）上存在显著畸变，原因在于大多数模型在2D参数化下解码3D几何，特征交互受图像平面邻近性而非真实3D空间关系主导，导致来自几何上距离较远表面的特征混合，产生过度平滑的几何。

### 核心思路/方法
1. 从基础模型中提取粗尺度的度量点云图。
2. 将该粗点云图提升到稀疏体素壳（sparse voxel shell）上。
3. 通过自引导稀疏体素精化（SSR）模块进行精化。该模块采用基于3D空间局部性的稀疏卷积聚合特征，避免深度不连续处的特征混合，从而生成高保真的度量尺度点图。

### 主要贡献
1. 明确了现有单目几何估计模型在细粒度结构上性能受限的关键原因：2D参数化导致的特征混合问题。
2. 提出了SSR方法，将单目几何建模从2D图像空间提升到3D空间，通过稀疏体素精化实现高保真度量点图。
3. 在多个数据集上的实验表明，该方法在定量指标和定性可视化上均显著优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
- 优先级：高
- 理由：该方法针对单目几何估计中长期存在的细粒度细节畸变问题，提出了新颖的3D稀疏体素精化范式，且实验证明了显著改进。对于从事3D视觉、几何重建、单目深度估计等方向的研究者具有重要参考价值。方法思路清晰，问题定义明确，具备较高实用与学术价值。

</details>

<details>
<summary>Abstract</summary>

Monocular geometry estimation has recently achieved impressive performance across diverse scenes. However, state-of-the-art models still face notable distortion in local 3D structure, especially in fine details, like thin structures and small objects. We attribute this limitation to an architectural mismatch: most current models decode 3D geometry within a 2D parameterization, where feature interactions are governed by image-plane proximity rather than true 3D spatial relationships. This inadvertently mixes features from geometrically distant surfaces, resulting in over-smoothed geometry particularly around thin or elongated structure. In this paper, we propose a fine-detail monocular geometry estimation with Self-Guided Sparse 3D Refinement (SSR) that lifts monocular geometry modeling from 2D image space to 3D space for high-fidelity metric-scale point maps. Our model lifts the coarse point map from a foundation base model onto a sparse voxel shell and refines it via SSR. The SSR employs sparse convolutions that aggregate features based on 3D spatial locality, avoiding feature mixing across depth discontinuities. Extensive experiments on diverse datasets demonstrate that our method significantly outperforms existing approaches in recovering fine detailed 3D geometry across both quantitative metrics and qualitative visualizations.

</details>

#### 2026-07-20 - MuViSeg: Multi-View Segment Correspondences from Dense Geometry Priors

**Authors:** Denis Fatykhoph, Timur Akhtyamov, Konstantin Pakulev, German Devchich, Gonzalo Ferrer
**Links:** [abs](https://arxiv.org/abs/2607.17938) - [pdf](https://arxiv.org/pdf/2607.17938)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, MASt3R, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MuViSeg: Multi-View Segment Correspondences from Dense Geometry Priors
- 作者：Denis Fatykhoph, Timur Akhtyamov, Konstantin Pakulev, German Devchich, Gonzalo Ferrer
- 出版日期：2026-07-20
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.17938

### 一句话总结
本文提出MuViSeg方法，通过三种匹配头（LightGlue风格、DPT风格和多视图联合自注意力）在实例分割层面建立多视图对应关系，并在零样本评估中提升了拓扑导航性能。

### 研究问题
如何从密集几何先验出发，建立多视角图像之间的实例分割级别对应关系，以弥补传统像素/关键点匹配与物体级消费系统（如物体级建图、拓扑导航）之间的鸿沟。

### 核心思路/方法
1. **基础框架**：采用类无关分割器每张图生成实例分割，然后从大型3D基础模型（MASt3R、VGGT）中池化特征作为分段描述符。
2. **三个学习的匹配头**：
   - **LightGlue风格注意力头**：基于冻结的MASt3R描述符，采用DoubleSoftmax评分进行段级匹配。
   - **DPT风格多尺度融合模块**：在VGGT基础模型中池化前，暴露层次化空间细节。
   - **多视图扩展头（主要贡献）**：同时对多个视图中的段进行联合自注意力，恢复严格成对匹配器无法获得的传递性对应关系。

### 主要贡献
1. 提出了一个多视图实例段对应框架，包含两个新的单视图匹配头和一个多视图扩展头。
2. 在Replica和Virtual KITTI 2的零样本协议下，LightGlue风格头相比无参数Sinkhorn匹配器，AUPRC分别提升+4.85和+25.9。
3. 将多视图变体集成到RoboHop拓扑导航流水线（Habitat-Matterport 3D基准）中，无需重新训练即实现成功率从50%提升至70%，LightGlue风格头使SPL从45.7提升至59.1。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文提出了一种新颖的多视图实例段对应方法，并通过零样本评估在经典导航基准上取得了显著提升，对物体级对应和拓扑导航领域有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Classical image correspondence is solved at the level of sparse keypoints or dense pixels, but the systems that consume these matches - object-level mapping, topological navigation, scene-graph maintenance - reason about whole objects. Recent work narrows this gap by matchng directly at the level of instance segments: a class-agnostic segmenter partitions each image, and per-segment descriptors are obtained by pooling features from large 3D foundation models over the masks. We build on this segment-level matching paradigm and propose three learned matching heads: a LightGlue-style attention head with DoubleSoftmax scoring on frozen MASt3R descriptors; a DPT-style multi-scale fusion module that exposes layered spatial detail from the VGGT foundation model before pooling; and - as our main contribution - a multi-view extension that performs joint self-attention over segments drawn from several views at once, recovering transitive correspondences that strictly pairwise matchers cannot reach. Under a stratified zero-shot protocol on Replica and Virtual KITTI 2 with controlled viewpoint baselines from 0 deg to 180 deg, the LightGlue-style head improves over a parameter-free Sinkhorn matcher on the same MASt3R backbone by +4.85 AUPRC on Replica and +25.9 AUPRC on Virtual KITTI 2. Dropped into the RoboHop topological navigation pipeline on the Habitat-Matterport 3D (HM3D) Instance Image Navigation benchmark without retraining, our multi-view variant raises success rate from 50% to 70%, and our LightGlue-style head raises SPL from 45.7 to 59.1.

</details>

#### 2026-07-19 - VIDAR: Visual-Inertial Dense Alignment and Reconstruction via a Geometric Foundation Model

**Authors:** Diyari Mohammed Salih, Lingxiang Hu, Naima AitOufroukh-Mammar, Fabien Bonardi
**Links:** [abs](https://arxiv.org/abs/2607.17171) - [pdf](https://arxiv.org/pdf/2607.17171)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** geometric foundation model, dense reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VIDAR: Visual-Inertial Dense Alignment and Reconstruction via a Geometric Foundation Model
- 作者：Diyari Mohammed Salih, Lingxiang Hu, Naima AitOufroukh-Mammar, Fabien Bonardi
- 出版日期：2026-07-19
- 分类：Geometry Foundation Models
- 链接：[Abstract](https://arxiv.org/abs/2607.17171) | [PDF](https://arxiv.org/pdf/2607.17171)

### 一句话总结
VIDAR 是一种视觉惯性密集重建框架，通过将视觉惯性里程计（SVO+IMU）与基础模型 Depth Anything 3 耦合，利用度量锚点（metric anchor）对齐单目基础模型的稠密几何预测，实现稳定尺度的稠密重建。

### 研究问题
如何解决单目基础模型（如 Depth Anything 3）在稠密几何预测中缺乏稳定度量尺度（metric scale）的问题，从而实现实用的度量稠密单目重建。

### 核心思路/方法
- 使用视觉惯性前端（SVO+IMU）作为度量锚点，提供相机位姿、尺度以及一致的世界坐标系，用于对齐跨时间的基础模型稠密预测。
- 基础模型贡献局部精细几何细节，并通过融合策略整合到全局重建中。
- 研究了两种对齐策略：1）位姿条件化的深度预测（pose-conditioned DA3）；2）解耦对齐策略（decoupled alignment）。

### 主要贡献
- 提出 VIDAR 框架，将视觉惯性度量约束与基础模型稠密几何能力结合，实现了鲁棒的度量稠密重建。
- 展示两种对齐策略效果：在 EuRoC 数据集上，位姿注入使尺度误差降至约 1%，F@0.10 均值达 0.463；解耦混合策略在无真值位姿时提升至 0.676。
- 在 EuRoC 和 TUM RGB-D 数据集上的实验表明，该方法为度量稠密单目重建提供了实用方案。

### 局限性
摘要未提供足够信息。未说明失败案例、计算开销、对光照或纹理的敏感性，也未提及与其他方法的全面对比。

### 阅读优先级
**中**  
理由：提出了一种将传统视觉惯性里程计与新兴几何基础模型结合的实用框架，对于从事单目深度估计或 SLAM 的研究者有一定参考价值。但方法明确依赖 Depth Anything 3 和特定惯性前端，通用性待评估；且摘要未提供完整消融实验和局限性，创新性主要体现为架构组合而非全新理论。

</details>

<details>
<summary>Abstract</summary>

Monocular foundation models provide dense geometry but usually lack a stable metric scale. This paper presents VIDAR, a visual-inertial dense reconstruction framework that couples SVO+IMU odometry with Depth Anything 3. VIDAR uses the visual-inertial front end as a metric anchor: it provides camera poses, scale, and a consistent world frame for aligning dense foundation-model predictions across time. The foundation model then contributes detailed local geometry that is fused into a global reconstruction. We study both pose-conditioned DA3 and a decoupled alignment strategy. On EuRoC, pose injection reduces scale error to about 1\% and reaches 0.463 mean F@0.10; the decoupled hybrid improves this to 0.676 without ground-truth poses. Results on EuRoC and TUM RGB-D show that VIDAR is a practical route to metric dense monocular reconstruction.

</details>

#### 2026-07-19 - DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation

**Authors:** Yuxuan Chen, Brook Du
**Links:** [abs](https://arxiv.org/abs/2607.17058) - [pdf](https://arxiv.org/pdf/2607.17058)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, SLAM, visual SLAM, depth estimation, robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation
- 作者：Yuxuan Chen, Brook Du
- 出版日期：2026-07-19
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要：https://arxiv.org/abs/2607.17058 ；PDF：https://arxiv.org/pdf/2607.17058

### 一句话总结
提出一种名为 Metric-DROID 的端到端递归架构，通过集成本体感受里程计作为几何锚点，解决单目视觉SLAM系统的尺度模糊和漂移问题，实现精确的公尺度深度估计。

### 研究问题
摘要未提供足够信息，但根据背景描述，研究问题为：单目系统固有的尺度模糊与尺度漂移问题，如何使基于递归光流的SLAM系统恢复公尺度度量，以实现自主机器人导航所需的高精度深度估计。

### 核心思路/方法
1. 设计一个**LSTM更新算子**，将高频里程计序列编码为空间特征图，为迭代优化提供持续的度量偏置。
2. 提出**不确定性感知度量后端（$BA_{odom}$）**：将里程计视为几何锚点，并学习其异方差协方差；通过回归时变度量不确定性$\Sigma_{o}$，智能平衡视觉重投影误差与度量平移残差，从而减轻轮滑与传感器噪声的影响。
3. 采用**选择性残差微调策略**，在保护预训练几何先验的同时，实现零样本的度量对齐。

### 主要贡献
1. 提出一种端到端递归架构Metric-DROID，集成里程计锚定视觉SLAM到物理现实。
2. 引入LSTM更新算子编码高频里程计序列。
3. 设计不确定性感知度量后端（$BA_{odom}$）并学习时变度量不确定性。
4. 提出选择性残差微调策略，保留预训练先验的同时实现零样本度量对齐。

### 局限性
摘要未提供足够信息。根据摘要，方法涉及轮滑和传感器噪声的缓解，但未明确讨论系统的实时性、实际部署局限、对特定里程计类型的依赖程度、或失败边界条件。

### 阅读优先级
**高**  
理由：该工作直接面向视觉SLAM中的关键尺度问题，提出结合里程计与不确定性的创新框架，结构设计清晰（LSTM编码、度量后端、残差微调），且包含零样本对齐能力，对自主机器人导航领域的研究者和工程师具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture that anchors visual SLAM to physical reality by integrating proprioceptive odometry. Our framework introduces the following innovations: (1) A LSTM Update Operator that encodes high-frequency odometry sequences into spatial feature maps, providing a persistent metric bias for iterative refinement. (2) An Uncertainty-Aware Metric Backend ($BA_{odom}$) that treats odometry as a geometric anchor with learned heteroscedastic covariance. By regressing a time-varying metric uncertainty $Σ_{o}$, our system intelligently balances visual re-projection and metric translation residuals, effectively mitigating the impact of wheel-slip and sensor noise. (3) We further propose a selective residual fine-tuning strategy to preserve pre-trained geometric priors while enabling zero-shot metric alignment.

</details>

#### 2026-07-16 - MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos

**Authors:** Ziren Gong, Xiaohan Li, Fabio Tosi, Ninghui Xu, Stefano Mattoccia, Jianfei Cai, Matteo Poggi
**Links:** [abs](https://arxiv.org/abs/2607.15211) - [pdf](https://arxiv.org/pdf/2607.15211)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** point map, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos
- 作者：Ziren Gong, Xiaohan Li, Fabio Tosi, Ninghui Xu, Stefano Mattoccia, Jianfei Cai, Matteo Poggi
- 出版日期：2026-07-16
- 分类：Geometry Foundation Models（主分类），3D Reconstruction & Multi-view Geometry（副分类）
- 链接：摘要页 https://arxiv.org/abs/2607.15211 | PDF https://arxiv.org/pdf/2607.15211

### 一句话总结
本文提出MAGiSt3R，一个基于多智能体（multi-agent）前馈流水线的单目RGB视频三维重建框架，能以接近10 FPS的速度同时完成重建和相机跟踪。

### 研究问题
如何从单目RGB视频中高效、准确地进行前馈式三维重建和相机跟踪，尤其是解决前馈流水线中累积的相机漂移问题？

### 核心思路/方法
1.  **基础模块**：采用来自3R系列的前馈模型处理RGB视频并回归局部点图（local point maps）。
2.  **融合模型**：提出MAGMA，在智能体内（intra-agent）和智能体间（inter-agent）两个层级上融合局部点图，以生成最终全局点图。
3.  **优化策略**：进行姿态图优化（pose graph optimization），以减轻前馈流水线中累积的相机漂移。

### 主要贡献
- 提出了一个多智能体前馈三维重建框架，实现了从单目RGB视频到全局点图的快速重建（近10 FPS）。
- 设计了MAGMA融合模型，能有效合并多智能体生成的局部点图。
- 通过姿态图优化缓解了前馈流水线中的累积相机漂移问题。
- 在合成和真实数据集上均取得了优于现有技术的重建和相机跟踪精度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  

**理由**：本文提出了一个新颖的多智能体前馈式三维重建框架，在效率（近10 FPS）和精度上均有提升，且方法思路清晰。但摘要未提供具体实验量化对比、局限性及方法细节（如智能体数量、网络结构等），因此对于需要深度复现或评估方法普适性的读者，阅读优先级可定为中等。若用户仅需了解该方向的最新进展，可考虑阅读。

</details>

<details>
<summary>Abstract</summary>

This paper presents MAGiSt3R, a multi-agent 3D reconstruction framework performing reconstruction and camera tracking for monocular RGB videos at almost 10 FPS. MAGiSt3R relies on a feed-forward model from the 3R family to process RGB videos and regress local point maps, and on a merging model, MAGMA, that combines local maps at both intra-agent and inter-agent levels to obtain the final global point map. Furthermore, MAGiSt3R performs pose graph optimization to mitigate cumulative camera drift occurring along the feed-forward pipeline. We evaluate MAGiSt3R on both synthetic and real-world datasets, demonstrating its superior reconstruction and camera tracking accuracy compared to state-of-the-art approaches.

</details>

#### 2026-07-14 - X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras

**Authors:** Heng Zhou, Shuhong Liu, Yonghao He, Bohao Zhang, Fa Fu, Chenhui Hou, Xianbao Hou, Lijun Han, Wei Sui
**Links:** [abs](https://arxiv.org/abs/2607.12993) - [pdf](https://arxiv.org/pdf/2607.12993)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras
- 作者：Heng Zhou, Shuhong Liu, Yonghao He, Bohao Zhang, Fa Fu, Chenhui Hou, Xianbao Hou, Lijun Han, Wei Sui
- 出版日期：2026-07-14
- 分类：Geometry Foundation Models（基础几何模型）; 3D Reconstruction & Multi-view Geometry（三维重建与多视图几何）
- 链接：https://arxiv.org/abs/2607.12993

### 一句话总结
X-Lens 是一个紧凑的前馈模型，通过几何感知的异构相机公式（可学习校准令牌和雅可比参数化的畸变偏置），从可变数量的鱼眼和针孔视图实时估计度量深度，在极低参数量下实现高帧率与高精度。

### 研究问题
如何从不同类型的相机（鱼眼和针孔）混合配置中实时估计度量深度，同时保证跨相机一致性和全局度量尺度。

### 核心思路/方法
1. **几何感知的异构相机公式**：包含两个关键组件。
   - **可学习校准令牌**：在鱼眼和针孔投影空间之间提供粗略对齐。
   - **雅可比参数化的畸变偏置**：注入交叉注意力中，对局部投影变化建模，促进跨相机一致性。
2. **紧凑前馈架构**：模型仅0.04B参数，运行速度高达41 FPS。
3. **端到端度量深度预测**：直接输出稠密深度及全局度量尺度，避免使用辅助重建目标造成计算和优化负担。
4. **大规模训练数据**：在多个公共数据集以及自研的OmniScene（约266K同步六视图帧、1.7M单张图像、103个室内外场景）上训练，实现跨相机泛化。

### 主要贡献
- 提出X-Lens，首个支持实时、异构相机混合输入的度量深度估计模型。
- 提出可学习校准令牌和雅可比参数化畸变偏置，有效处理鱼眼与针孔视图的几何差异。
- 在OmniScene-Full上相比最强基线将AbsRel降低25.4%，同时参数减少88.9%。
- 在常规鱼眼/针孔单设置上也达到竞争性性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作聚焦于实用且具有挑战性的异构相机混合场景（鱼眼+针孔），在保持极低参数量和实时性（41 FPS）的同时显著提升度量深度精度，并公开大规模合成数据集，对多相机感知系统研发具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We present X-lens, a compact feed-forward model for metric depth estimation from a variable number of calibrated fisheye and pinhole views. To support real-time downstream perception, X-lens is built around a geometry-aware heterogeneous camera formulation with two key components. Learnable calibration tokens provide a coarse alignment between fisheye and pinhole projective spaces, while a Jacobian-parameterized distortion bias injected into cross-attention models local projection changes and promotes cross-camera consistency, enabling robust generalization with only 0.04B parameters and up to 41 FPS. The model predicts dense depth together with a global metric scale, avoiding auxiliary reconstruction targets that increase computation and optimization complexity. To learn such cross-camera generalization at scale and depth, X-lens is trained on multiple public datasets and OmniScene, our newly released large-scale synthetic dataset containing approximately 266K synchronized six-view frames, 1.7M individual images, and 103 indoor and outdoor scenes. Extensive experiments on both real-world and synthetic indoor and outdoor datasets demonstrate superior heterogeneous-camera metric depth accuracy, reducing AbsRel by 25.4\% on OmniScene-Full over the strongest baseline while using 88.9\% fewer parameters, with competitive performance on conventional fisheye-only and pinhole-only settings.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

#### 2026-07-17 - MotionForesight: Re-purposing Video Models for Future 3D Scene-Flow Prediction

**Authors:** Homanga Bharadhwaj, Yash Jangir
**Links:** [abs](https://arxiv.org/abs/2607.16192) - [pdf](https://arxiv.org/pdf/2607.16192)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** scene flow

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MotionForesight: Re-purposing Video Models for Future 3D Scene-Flow Prediction
- 作者：Homanga Bharadhwaj, Yash Jangir
- 出版日期：2026-07-17
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2607.16192

### 一句话总结
本文提出MotionForesight方法，通过重新利用视频预测模型中的先验知识，仅从观察到的单目视频帧预测未来物体在3D空间中的轨迹流，无需语言或物体属性假设。

### 研究问题
如何从普通的单目人类-物体交互视频中，学习预测被操作物体上点的未来3D运动轨迹？

### 核心思路/方法
1. 利用预训练视频模型中的密集3D跟踪器，从完整视频片段生成伪真实轨迹。
2. 仅使用观察到的帧，训练一个轻量适配器，将回溯式跟踪表示转换为前向预测，同时冻结视频和跟踪组件。
3. 通过学习掩码潜变量替代未来的RGB和几何信息，实现从像素预测到未来3D场景流的重定向。

### 主要贡献
1. 提出了一种从被动视频观察中预测未来3D物体运动轨迹的方法，无需物体属性假设。
2. 证明了视频预测模型中的先验知识可被高效重用于3D运动预测，仅需4万个人类视频即可训练。
3. 该模型对分布外的物体、环境、视角和交互具有泛化能力，且性能优于使用百万级视频训练的更大模型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法在少量数据下实现了跨领域泛化，且直接输出3D轨迹预测，对机器人学、具身智能等领域的互动规划具有潜在价值；方法设计简洁，重用预训练模型，实用性强。

</details>

<details>
<summary>Abstract</summary>

Humans can infer how objects are likely to move from passive observation: a cup may be lifted, a drawer may slide, and a lid may rotate shut. Such predictions expose the physical consequences of interaction needed to act in the real world. We study how to learn this anticipation from ordinary monocular videos of human-object interaction. Given a short observed video context, MotionForesight predicts future 3D trajectories for points on the manipulated object. This casts interaction prediction as object-centered 3D motion forecasting without any assumptions on the object properties. Our key insight is that video prediction models already encode rich priors about how objects move during human interactions. We redirect these priors from pixel prediction toward future 3D scene flow. We start from a dense 3D tracker built on a pretrained video model, generate pseudo-ground-truth tracks from complete clips, and train the forecaster using only the observed frames. We replace future RGB and geometry with learned mask latents and train a lightweight adapter to turn the retrospective tracking representation into a forward predictor, while freezing the large video and tracking components. Using just 40k human videos and no auxiliary inputs such as language, MotionForesight generalizes across diverse out-of-distribution objects, environments, viewpoints, and interactions. It also outperforms substantially larger models that use over a million training videos. These results show that we can efficiently re-purpose video priors into explicit geometric forecasts for embodied intelligence. https://motionforesight.github.io/

</details>

#### 2026-07-15 - Human4K: A Large-Scale 4K Multi-View Mocap Dataset for Whole-Body 3D Human Reconstruction

**Authors:** Tianshun Han, Ziyu Shi, Lijian Liu, Ajian Liu, Benjia Zhou, Hugo Jair Escalante, Yanyan Liang, Sergio Escalera, Zhen Lei, Jun Wan
**Links:** [abs](https://arxiv.org/abs/2607.13646) - [pdf](https://arxiv.org/pdf/2607.13646)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** human reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Human4K: A Large-Scale 4K Multi-View Mocap Dataset for Whole-Body 3D Human Reconstruction
- 作者：Tianshun Han, Ziyu Shi, Lijian Liu, Ajian Liu, Benjia Zhou, Hugo Jair Escalante, Yanyan Liang, Sergio Escalera, Zhen Lei, Jun Wan
- 出版日期：2026-07-15
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2607.13646

### 一句话总结
本文提出了Human4K，一个包含超600万张4K多视角图像、配备动作捕捉精确SMPL-X标注的大规模全身人体重建数据集，旨在提升复杂真实场景下的3D人体重建鲁棒性。

### 研究问题
现有3D人体重建模型在最具挑战性的真实场景（如深度模糊、自遮挡、肢体关节复杂动作）中表现不佳，关键原因在于已有数据集缺乏高分辨率图像、高精度标注和多样化全身动作的组合。

### 核心思路/方法
1. **数据集构建**：使用八视角高分辨率相机系统配合专业Vicon动作捕捉设备，采集11位受试者执行复杂、高度关节化且强自遮挡的全身运动，获得超600万张4K图像。
2. **标注处理**：通过“动作重定向与精炼模块”（MRRM）处理所有序列，确保全身及四肢的精确定位。
3. **实验验证**：在标准基准上使用Human4K进行训练，结果显示全身重建性能持续提升，尤其在手、脚和深度模糊肢体构型方面表现显著。

### 主要贡献
- 提供了首个大规模、4K分辨率、多视角、带动作捕捉精确SMPX-X标注的全身人体重建数据集（Human4K），覆盖复杂全身运动。
- 使用MRRM模块实现高质量动作标注对齐。
- 实验证明该数据集能有效提升标准基准上的全身重建质量，尤其改善手脚及深度模糊肢体构型的重建效果。

### 局限性
摘要未提供足够信息。未提及数据集的潜在偏差、是否涵盖不同体型或运动模式，以及模型在旋转或极端光照下的表现等。

### 阅读优先级
**高**  
理由：该数据集直接针对当前3D人体重建中的关键瓶颈（复杂真实场景下的不稳定几何与肢体关节不精确），且提供了大规模、高分辨率、高精度标注的资源，对提升相关模型性能具有重要实践价值，适合从事人体重建、动作捕捉或多视角三维视觉的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D human reconstruction have improved overall performance, yet current models still fail in the most challenging real-world scenarios. They often produce unstable geometry, inaccurate limb articulation and unreliable predictions under depth ambiguity or self-occlusion. A key reason is that existing datasets still lack the combination of high-resolution images, high-precision annotations and diverse whole-body motions required to support robust reconstruction. To address this gap, we present Human4K, a large-scale 4K multi-view whole-body human reconstruction dataset with mocap-accurate SMPL-X annotations. Human4K contains over six million 4K images captured by an eight-view high-resolution camera system synchronized with a professional Vicon motion capture setup, covering 11 subjects performing complex, highly articulated and strongly self-occluded full-body motions. All sequences are processed by a Motion-Retargeting and Refinement Module (MRRM) to ensure precise alignment for the full body and extremities. Experimental results show that training with Human4K consistently improves whole-body reconstruction on standard benchmarks, with particularly large gains for hands, feet and depth-ambiguous limb configurations.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-20 - Robust Multimodal Dynamic Object Segmentation

**Authors:** Zhe Xin, Hanzhi Chang, Penghui Huang, Yinian Mao, Guoquan Huang
**Links:** [abs](https://arxiv.org/abs/2607.18153) - [pdf](https://arxiv.org/pdf/2607.18153)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robust Multimodal Dynamic Object Segmentation  
- 作者：Zhe Xin, Hanzhi Chang, Penghui Huang, Yinian Mao, Guoquan Huang  
- 出版日期：2026-07-20  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2607.18153  

### 一句话总结  
提出一种融合2D点轨迹、3D重建和语义信息的多模态动态物体分割框架，通过Transformer与特征聚类聚合模块实现精确且完整的动态掩膜生成。  

### 研究问题  
现有基于光流的方法无法保证物体边界的静态/动态分割一致性，而基于3D重建的方法对重建误差高度敏感。如何实现鲁棒且精确的动态物体分割？  

### 核心思路/方法  
1. 设计融合Transformer和特征聚类聚合模块的网络，对多模态特征轨迹进行静态/动态分类。  
2. 模型能够根据场景特征自适应决定主导模态，并缓解特征退化问题。  
3. 引入基于点查询的SAM后处理方法，可处理单个掩膜内的多个物体。  

### 主要贡献  
- 提出整合2D点轨迹、3D重建和语义信息的多模态动态分割框架。  
- 设计自适应模态主导机制与特征退化缓解策略。  
- 提出点查询SAM后处理，支持单掩膜多物体处理。  
- 实验表明在动态物体分割与静态场景重建任务中达到最佳性能。  

### 局限性  
摘要未提供足够信息。  

### 阅读优先级  
**高**  
理由：该文在动态分割领域提出融合多种模态（2D轨迹、3D重建、语义）的新框架，并明确指出了现有方法的缺陷（边界不一致、对重建误差敏感），方法设计具有创新性（自适应模态选择、点查询SAM），同时宣称在两项任务上达到SOTA，适合对视觉分割、3D场景理解感兴趣的读者优先关注。

</details>

<details>
<summary>Abstract</summary>

Dynamic object segmentation plays a critical role in many visual applications such as static scene reconstruction from dynamic videos. However, existing optical flow-based methods fail to ensure consistent static/dynamic segmentation along object boundaries, while 3D reconstruction-based approaches are highly sensitive to reconstruction errors. To address these limitations, we present a dynamic object segmentation framework that can generate both precise and complete dynamic masks by integrating multimodal cues including 2D point tracks, 3D reconstruction, and semantic information. We design a network combining Transformer architectures with feature clustering aggregation modules to perform static/dynamic classification of multimodal feature trajectories. It enables the model to adaptively determine which type of feature should dominate based on the characteristics of each scene, while also mitigating the impact of feature degradation. Additionally, we introduce a novel point-query-based SAM post-processing method capable of handling multiple objects within a single mask. Extensive experiments demonstrate that our approach achieves state-of-the-art performance in both dynamic object segmentation and static scene reconstruction tasks.

</details>

#### 2026-07-20 - Plenoptic Condensation: A Novel Approach to Generalized Scene Reconstruction

**Authors:** Brevin Tilmon, Alex DeJournett, John Leffingwell, Scott Ackerson
**Links:** [abs](https://arxiv.org/abs/2607.18151) - [pdf](https://arxiv.org/pdf/2607.18151)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, rendering, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Plenoptic Condensation: A Novel Approach to Generalized Scene Reconstruction
- 作者：Brevin Tilmon, Alex DeJournett, John Leffingwell, Scott Ackerson
- 出版日期：2026-07-20
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.18151

### 一句话总结
本文提出一种名为“全光凝聚”（Plenoptic Condensation, PCon）的新型通用场景重建方法，通过多阶段重建管道将图像转化为可自适应凝聚的结构化元素，实现了高保真渲染与精细损伤测量。

### 研究问题
如何实现通用场景重建（Generalized Scene Reconstruction, GSR），在保持高保真渲染与测量精度的同时，自适应地处理不同区域（如锐利边缘、光滑反射面）的表示能力需求？

### 核心思路/方法
PCon采用多阶段重建管道：
1. **初始转化**：将输入图像转换为低表示能力的“汤状”场景元素（soupy scene elements）。
2. **自适应凝聚**：将“汤状”元素自适应地凝聚为高表示能力的“结构化”元素，从而高效表示复杂特征（如锐利边缘、光滑反射面）。
3. **输出模型**：生成的场景模型称为“实相模型”（Reality Models, Relms），具有空间可变的表示能力，支持高保真渲染、测量和场景理解。

### 主要贡献
1. 提出了PCon这一GSR新方法，通过多阶段凝聚机制实现空间可变的表示能力。
2. 展示了使用消费级手机和无人机拍摄的野外场景重建效果（包括“Damaged Fiat”案例）。
3. 在“Damaged Fiat”案例中，PCon在重建汽车发动机盖时精度是SOTA方法（NeRO和RT-Splatting）的两倍以上，且局部损伤剖面误差仅为35微米（0.035毫米），而对比方法基本无法测量损伤。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法提出了一种新颖的多阶段凝聚范式，在消费级设备上实现了远超SOTA的重建精度（尤其在高精度局部测量任务中），对3D重建与多视图几何领域具有潜在重要影响。

</details>

<details>
<summary>Abstract</summary>

We present a novel Generalized Scene Reconstruction (GSR) approach called Plenoptic Condensation (PCon). PCon uses a multi-stage reconstruction pipeline, initially converting images into "soupy" scene elements with low (representational) power, then adaptively condensing the "soup" into "structured" elements of higher power capable of efficiently representing, for example, sharp edges and smooth reflective surfaces. PCon scene models called Reality Models (Relms) enable spatially varying representational power, which is essential for high-fidelity rendering, measurement, and scene understanding. We showcase several in-the-wild PCon reconstructions captured with consumer phone cameras and drones. In one case called "Damaged Fiat", PCon is benchmarked against two state-of-the-art (SOTA) GSR methods: NeRO and RT-Splatting. Referring to Figure 1 below, PCon reconstructs the car hood more than twice as accurately as the SOTA methods. But more importantly, the local damage profile error for PCon is 35 um (0.035 mm), whereas the two other SOTA methods are essentially unable to measure the damage at all. Our project website is available at https://quidient.github.io/pcon-2026.html.

</details>

#### 2026-07-20 - UMCP: A Unified Multi-Task Collaborative Perception Network for Luggage Trolley Pose Estimation

**Authors:** Zhirui Sun, Zhihao Jiang, Yao Wang, Jianwei Peng, Jiankun Wang
**Links:** [abs](https://arxiv.org/abs/2607.17950) - [pdf](https://arxiv.org/pdf/2607.17950)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UMCP: A Unified Multi-Task Collaborative Perception Network for Luggage Trolley Pose Estimation
- 作者：Zhirui Sun, Zhihao Jiang, Yao Wang, Jianwei Peng, Jiankun Wang
- 出版日期：2026-07-20T13:51:01Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2607.17950；PDF: https://arxiv.org/pdf/2607.17950

### 一句话总结
本文提出一个名为UMCP的统一多任务协作感知网络，用于同时进行行李车检测、关键点检测和朝向估计，在保持竞争精度的同时显著降低模型复杂度和计算成本。

### 研究问题
在机器人自动收集行李车的任务中，如何实现高精度且实时的视觉感知，以避免现有级联多模型推理导致的推理延迟增加和部署成本过高的问题。

### 核心思路/方法
基于YOLOv12架构，将关键点特征与朝向特征融合，并送入朝向特征增强模块（OFEM）以提升朝向估计精度；此外，采用圆形概率分布建模和KL散度损失进一步优化朝向估计。

### 主要贡献
1. 提出统一的单阶段多任务协作网络UMCP，同时实现检测、关键点检测和朝向估计。
2. 设计朝向特征增强模块（OFEM），通过融合关键点特征增强朝向估计。
3. 引入圆形概率分布建模与KL散度损失，提升朝向估计精度。
4. 实验表明，该方法在保持竞争精度的同时，显著降低了模型复杂度和计算成本。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法针对行李车姿态估计这一特定应用场景，虽有一定通用性（多任务协作），但核心创新点（YOLOv12架构基础上的特征融合与概率建模）属于工程优化，理论贡献有限；且摘要未提供具体精度与速度数值，需要阅读全文才能评估实际效果。

</details>

<details>
<summary>Abstract</summary>

In robotic autonomous luggage trolley collection, robots must continuously localize scattered luggage trolleys in cluttered and dynamic environments. This requires the vision system to achieve both high accuracy and real-time performance. However, existing visual perception approaches for luggage trolleys often rely on cascaded multi-model inference, leading to increased inference latency and high deployment costs. To address these limitations, this article presents a unified multi-task collaborative perception network (UMCP) that simultaneously performs luggage trolley detection, keypoint detection and orientation estimation. Based on the YOLOv12 architecture, keypoint features are fused with orientation features and then fed into an orientation feature enhancement module (OFEM), thereby improving orientation estimation accuracy. In addition, circular probability distribution modeling with a Kullback-Leibler (KL) divergence loss is adopted to enhance orientation estimation accuracy further. Experimental results demonstrate that the proposed method achieves competitive overall accuracy while substantially reducing model complexity and computational cost compared with existing methods. A website about this work is available at https://sites.google.com/view/robot-umcp.

</details>

#### 2026-07-20 - SLAM in Low-Light Environments: Project Report

**Authors:** Oleh Basystyi, Anna Stasyshyn, Oleksandr Kosovan, Yaroslav Prytula
**Links:** [abs](https://arxiv.org/abs/2607.17699) - [pdf](https://arxiv.org/pdf/2607.17699)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, feature matching, robotics, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SLAM in Low-Light Environments: Project Report  
- 作者：Oleh Basystyi, Anna Stasyshyn, Oleksandr Kosovan, Yaroslav Prytula  
- 出版日期：2026-07-20  
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.17699  

### 一句话总结
该报告在低光照环境下基准测试了六种SLAM系统，发现仅惯性融合与全局优化并存的系统（Kimera-VIO）能稳定完成全部序列，而纯RGB方法在高难度低光照序列中普遍失效。

### 研究问题
低光照环境下，仅使用标准RGB摄像头的SLAM系统能达到何种跟踪精度与鲁棒性？当前主流方法的局限性及潜在改进方向是什么？

### 核心思路/方法
在LaMARia数据集的五个不同难度与光照水平序列上，对六种SLAM系统（ORB-SLAM3、DSO、Kimera-VIO、OpenVINS、DPVO、DPV-SLAM）进行基准测试，使用绝对姿态误差、相对姿态误差以及控制点召回率作为评价指标。

### 主要贡献
1. 系统性地评估了六种SLAM范式（特征法、直接法、滤波法、学习法）在低光照环境下的表现。  
2. 发现仅Kimera-VIO（同时包含惯性融合与全局优化）能成功跟踪全部五条序列，且相对姿态误差最低，但绝对误差因无闭环修正而持续增长。  
3. 指出学习型方法（DPVO、DPV-SLAM）虽不丢失跟踪，但在低光照下绝对误差可达约100米；经典单目及滤波方法在大多数困难低光照序列上彻底失败或发散。

### 局限性
- 摘要未提及实验的具体扫描环境、序列长度或计算资源开销。  
- 摘要未说明Kimera-VIO为何比其他系统更优的具体机制。  
- 摘要未提供各方法的完整定量误差值，仅给出了定性结论。  

### 阅读优先级
中  
理由：该工作针对低光照SLAM这一实际工程难点进行了系统基准测试，结论具有参考价值；但摘要未提供详细实验数据，且问题叙述较为通用，适合关注SLAM鲁棒性评估的读者，而非寻求新算法或创新方法的读者。

</details>

<details>
<summary>Abstract</summary>

Simultaneous localization and mapping (SLAM) is one of the fundamental problems in robotics, as it enables autonomous operations in real-world scenarios. Under low illumination, reduced contrast, sensor noise, and motion blur degrade both feature extraction and feature matching, while compensating with LiDAR, depth, or thermal sensors raises cost, power draw, and integration complexity. Existing benchmarks remain dominated by well-lit indoor or daylight sequences, leaving open how far SLAM with standard RGB cameras can be pushed in the dark. We benchmark six systems spanning the feature-based, direct, filter-based, and learning-based paradigms - ORB-SLAM3, DSO, Kimera-VIO, OpenVINS, DPVO, and DPV-SLAM - on five LaMARia sequences of varying difficulty and illumination, reporting absolute and relative pose error alongside control-point recall. Kimera-VIO is the only system to track all five sequences to completion, combining the lowest relative pose error with steadily growing absolute error due to the absence of loop closure; DPVO and DPV-SLAM never lose tracking but incur absolute errors of roughly 100 m under low light; and the classical monocular pipelines (ORB-SLAM3, DSO) together with the filter-based OpenVINS fail outright or diverge on most of the harder and low-light sequences. The results suggest that RGB-only SLAM maintains stable low-light tracking only when both inertial fusion and global optimization are present. Closing the remaining gap will likely require low-light-specific learned front-ends or a return to complementary sensing.

</details>

#### 2026-07-19 - DepthART: Scaling Foundation Monocular Depth to Tiny Models

**Authors:** Feng Xue, Wu Chen, Mingshuai Zhao, Guofeng Zhong, Anlong Ming, Haozhe Wang, Dianqiao Lei, Zhaowen Lin, Haiyang Zhang, Nicu Sebe
**Links:** [abs](https://arxiv.org/abs/2607.17099) - [pdf](https://arxiv.org/pdf/2607.17099)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DepthART: Scaling Foundation Monocular Depth to Tiny Models
- 作者：Feng Xue, Wu Chen, Mingshuai Zhao, Guofeng Zhong, Anlong Ming, Haozhe Wang, Dianqiao Lei, Zhaowen Lin, Haiyang Zhang, Nicu Sebe
- 出版日期：2026-07-19
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.17099

### 一句话总结
本文提出DepthART，一种针对小型模型设计的紧凑型单目深度估计模型，通过抗偏置数据采样与相机条件微调两项策略，在保持低计算量的同时显著提升了零样本泛化能力和度量精度。

### 研究问题
如何将先进的几何基础模型（如Metric3D、Depth Anything）在单目深度估计中的跨场景泛化与度量预测能力，有效迁移至资源受限的微型模型上，解决微型模型因容量不足而导致的过拟合和度量不稳定问题。

### 核心思路/方法
1. **识别瓶颈**：发现微型模型存在两个关键瓶颈：一是过度拟合数据集特定的分布偏置；二是在相机参数变化时度量尺度调整不稳定，全参数微调会破坏可迁移的几何知识。
2. **抗偏置数据采样**：设计一种数据采样方案，在相同训练预算下减少分布偏置的影响。
3. **相机条件微调协议**：冻结蒸馏后的编码器，仅根据相机内参条件调整度量尺度，从而保留跨数据集的泛化能力。

### 主要贡献
- 提出DepthART模型，首次将基础模型的深度估计优势成功扩展到微型模型，适合设备端部署。
- 识别并解决了微型模型在深度估计中的两个关键容量瓶颈。
- 提供可扩展的模型家族，DepthART-S在RTX A6000上达到347/245 FPS（FP32），在Jetson Nano 4GB上超过15 FPS。
- 在多个数据集上超越先前微型基线，例如在NYUD v2上零样本δ₁=0.964，部分结果接近大型模型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。
理由：该工作聚焦于将基础模型压缩至微型设备，对边缘计算和实时应用有实际意义；方法明确且性能提升显著。但若读者不关注模型部署或微型模型压缩，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Recent geometric foundation models (e.g., Metric3D, Depth Anything and UniDepth) have substantially improved monocular depth estimation (MDE) in both cross-scene generalization and metric-scale prediction, yet these gains have not translated to tiny models. We bridge this gap with DepthART (Depth Anything Rethought for Tiny Models), which is a compact MDE model for on-device deployment across diverse scenes. We first identify two capacity-driven bottlenecks in tiny models: (i) overfitting to dataset-specific distribution bias and (ii) unstable metric adaptation under camera shift, where full fine-tuning easily damages transferable geometry. Accordingly, DepthART combines two simple but effective strategies: a bias-resistant data sampling scheme to reduce distribution bias under the same training budget, and a camera-conditioned fine-tuning protocol that freezes the distilled encoder and adjusts metric scale conditioned on intrinsics while better preserving cross-dataset generalization. Across datasets, DepthART consistently surpasses previous tiny baselines in both zero-shot generalization and metric accuracy (e.g., zero-shot $δ_1$=0.964 for DepthART-S on NYUD v2), and in some cases approaches heavy models. We further provide a scalable model family, with DepthART-S reaching 347/245 FPS (strict FP32) on an RTX A6000 at $224^2/448^2$, 102 FPS (TF32) on a Orin NX 8GB, and over 15 FPS (FP32) on a Jetson Nano 4GB.

</details>

#### 2026-07-18 - Splat-based 3D Scene Reconstruction with Extreme Motion-blur

**Authors:** Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim
**Links:** [abs](https://arxiv.org/abs/2607.16926) - [pdf](https://arxiv.org/pdf/2607.16926)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, scene reconstruction, camera pose estimation, pose estimation, 3D mapping, Gaussian Splatting, scene representation, radiance, splatting, robotics, mapping, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Splat-based 3D Scene Reconstruction with Extreme Motion-blur
- 作者：Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim
- 出版日期：2026-07-18
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2607.16926) | [PDF](https://arxiv.org/pdf/2607.16926)

### 一句话总结
本文提出一种基于高斯溅射的RGB-D三维场景重建方法，通过联合相机位姿估计与图像去模糊，有效应对极端运动模糊场景下的重建挑战。

### 研究问题
在低光照或快速运动条件下，RGB图像常因长时间曝光产生严重运动模糊，导致传统相机位姿估计方法（如COLMAP）和三维重建技术（如NeRF、Gaussian Splatting）失效；同时，深度传感器的视野限制和快速相机运动减少了点云重叠，降低了ICP算法位姿估计的效果。如何在此极端条件下实现高质量三维重建是核心问题。

### 核心思路/方法
1. **输入与数据对齐**：利用光流和ICP算法初步对齐连续RGB-D帧。
2. **位姿与几何优化**：通过调整高斯位置以实现最佳深度对齐，从而细化相机位姿和三维几何。
3. **运动模糊处理**：在曝光时间内建模相机运动，通过比较输入图像与一系列清晰渲染帧实现去模糊。
4. **框架基础**：基于高斯溅射框架，结合三维高斯溅射和深度输入增强场景表示。

### 主要贡献
- 提出一种结合相机位姿估计与图像去模糊的高斯溅射方法，专门应对极端运动模糊。
- 通过建模曝光期间的相机运动，实现从模糊输入恢复清晰场景。
- 构建了一个新的极端运动模糊RGB-D数据集，并公开代码与数据集。
- 实验表明，该方法在挑战条件下优于现有技术，对机器人、自动驾驶和增强现实等三维映射应用有重要意义。

### 局限性
摘要未提供足够信息。例如，未提及方法在非运动模糊场景下的性能、计算开销、对深度传感器噪声的敏感性，或与无深度输入方法的对比。

### 阅读优先级
**高**。理由：该工作针对低光照和快速运动这一实际难题提出了新的解决方案，结合了去模糊与高斯溅射框架，且公开了代码与数据集，对从事三维重建、机器人感知、AR/VR的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We propose a splat-based 3D scene reconstruction method from RGB-D input that effectively handles extreme motion blur, a frequent challenge in low-light environments. Under dim illumination, RGB frames often suffer from severe motion blur due to extended exposure times, causing traditional camera pose estimation methods, such as COLMAP, to fail. This results in inaccurate camera pose and blurry color input, compromising the quality of 3D reconstructions. Although recent 3D reconstruction techniques like Neural Radiance Fields and Gaussian Splatting have demonstrated impressive results, they rely on accurate camera trajectory estimation, which becomes challenging under fast motion or poor lighting conditions. Furthermore, rapid camera movement and the limited field of view of depth sensors reduce point cloud overlap, limiting the effectiveness of pose estimation with the ICP algorithm. To address these issues, we introduce a method that combines camera pose estimation and image deblurring using a Gaussian Splatting framework, leveraging both 3D Gaussian splats and depth inputs for enhanced scene representation. Our method first aligns consecutive RGB-D frames through optical flow and ICP, then refines camera poses and 3D geometry by adjusting Gaussian positions for optimal depth alignment. To handle motion blur, we model camera movement during exposure and deblur images by comparing the input with a series of sharp, rendered frames. Experiments on a new RGB-D dataset with extreme motion blur show that our method outperforms existing approaches, enabling high-quality reconstructions even in challenging conditions. This approach has broad implications for 3D mapping applications in robotics, autonomous navigation, and augmented reality. Both code and dataset are publicly available on https://github.com/KAIST-VCLAB/gs-extreme-motion-blur.

</details>

#### 2026-07-18 - GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

**Authors:** Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
**Links:** [abs](https://arxiv.org/abs/2607.16897) - [pdf](https://arxiv.org/pdf/2607.16897)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM
- 作者：Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- 出版日期：2026-07-18
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.16897

### 一句话总结
本文提出GLidE-SLAM，一种面向嵌入式设备的单目混合间接-直接SLAM框架，通过将GPU加速的直接跟踪与CPU间接管线分离，在资源受限硬件上实现了高达9倍的帧率提升。

### 研究问题
如何在嵌入式设备上部署Visual SLAM时，在保持高跟踪帧率的同时，为地图扩展和维护保留足够的计算资源。

### 核心思路/方法
采用架构分离策略：系统使用OpenGL ES 3.1 compute shaders（独立于CUDA）在中间帧上进行GPU加速的直接跟踪（仅位姿估计，无需深度优化或地图点创建），而将完整的间接管线（用于地图扩展和全局一致性）保留给CPU处理。这种设计将适合高度并行的图像对齐操作卸载到GPU，从而释放CPU资源用于后端任务。

### 主要贡献
1. 提出首个在嵌入式设备上通过compute shaders实现完整直接光度位姿估计的SLAM系统。
2. 通过GPU-CPU架构分离，在目标平台上实现比仅CPU基线高达9倍的帧率提升，同时保持轨迹精度。
3. 采用vendor-agnostic的OpenGL ES 3.1标准，使系统可在更广泛的商用嵌入式平台上部署，无需CUDA支持。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该方法针对嵌入式设备上的SLAM性能优化，提出了创新的GPU加速直接跟踪方案，实验显示显著帧率提升。若读者关注资源受限硬件上的高效V-SLAM，则值得阅读；若对SLAM算法精度或通用框架设计更感兴趣，则优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

With the growing demand for robotics, autonomous drones, and wearable extended reality systems, the deployment of Visual SLAM on embedded devices remains challenging. Tracking must sustain high frame rates while preserving compute resources for map extension and maintenance. This paper presents GLidE-SLAM, a monocular hybrid indirect-direct framework that addresses this by architectural separation: the system performs GPU-accelerated direct tracking on intermediate frames, while reserving the full indirect pipeline for map extension and global consistency. We leverage highly parallel image-alignment operations for pose-only estimation without depth optimization or map point creation, making the workload suitable for GPU offloading and freeing CPU resources for backend tasks. We implement the direct tracker using vendor-agnostic OpenGL ES~3.1 compute shaders, enabling deployment across a broader range of commodity embedded platforms without requiring CUDA support. To our knowledge, this is the first complete direct photometric pose estimator realized via compute shaders for embedded-class devices. Experiments on target platforms demonstrate up to 9$\times$ higher frame rates than the CPU-only baseline while maintaining trajectory accuracy and improving practical deployment across commodity resource-constrained hardware.

</details>

#### 2026-07-17 - Toward Semantic Communication for Real-time Mobile 3D Reconstruction

**Authors:** Fangzhou Zhao, Yao Sun, Xuesong Liu, Runze Cheng, Shang Kai, Yi Sun
**Links:** [abs](https://arxiv.org/abs/2607.16128) - [pdf](https://arxiv.org/pdf/2607.16128)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, pose estimation, bundle adjustment, rendering, digital twin, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Toward Semantic Communication for Real-time Mobile 3D Reconstruction
- 作者：Fangzhou Zhao, Yao Sun, Xuesong Liu, Runze Cheng, Shang Kai, Yi Sun
- 出版日期：2026-07-17T17:07:40Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类），Embodied / Robotics / AR Applications（次分类）
- 链接：摘要链接：https://arxiv.org/abs/2607.16128；PDF链接：https://arxiv.org/pdf/2607.16128

### 一句话总结
本文提出一种针对实时移动3D重建的语义通信框架，通过传输语义信息并输出像素级置信度地图，指导几何估计，从而在噪声信道下提升位姿估计精度和3D结构一致性。

### 研究问题
如何在实时移动3D重建场景中，利用语义通信（SemCom）缓解通信引起的图像失真对几何估计（如位姿计算和场景结构重建）的敏感性影响。

### 核心思路/方法
- 设计一个语义收发机（semantic transceiver），能够输出重建图像以及每个像素的置信度地图（pixel-wise confidence map），量化各区域的重建可靠性。
- 提出置信度引导的几何估计方法：在基于RANSAC的位姿初始化和集束调整（bundle adjustment）中融入置信度信息，减少不可靠区域的影响，从而增强在噪声信道下的鲁棒性。

### 主要贡献
- 首次将语义通信框架应用于实时移动3D重建，支持任务相关的可靠传输。
- 提出包含像素级置信度地图的语义收发机，为几何估计提供明确的可靠性信息。
- 设计置信度引导的几何估计流程，改进传统RANSAC和集束调整，显著提升位姿估计准确性和3D结构一致性（通过模拟实验验证）。

### 局限性
摘要未提供足够信息。例如，未讨论框架的计算复杂度对移动平台实时性的影响、置信度地图的生成机制细节、实际硬件实现中的延迟或功耗，以及除模拟外是否在真实移动平台上进行测试。

### 阅读优先级
**中**。
理由：该工作融合了语义通信与3D重建两个方向，对于从事实时移动3D重建、无线通信与计算机视觉交叉领域的研究者有参考价值。但由于摘要未提供实验细节和具体数值比较，且属于较新发表的论文（2026年），若需评估其实际效果和可复现性，需进一步阅读全文。对于仅关注传统3D重建或通信的读者，优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

Real-time mobile 3D reconstruction is fundamental to many emerging applications such as autonomous navigation and digital twin construction, where a moving platform continuously captures an image stream and transmit to a computing server for scene understanding. Unlike offline reconstruction, camera poses and scene geometry are estimated on-the-fly during acquisition, making multi-view consistency a real-time requirement and rendering geometric estimation highly sensitive to communication-induced distortions. Semantic communication (SemCom) transmits compact semantic information, offering a promising way to preserve task-critical data over unreliable links. However, existing designs are optimized at the image or single-view level and without providing explicit reliability information for geometric estimation, limiting their applicability to real-time mobile 3D reconstruction. In this context, we propose a SemCom framework for real-time mobile 3D reconstruction. The framework includes a semantic transceiver that outputs a reconstructed image alongside a pixel-wise confidence map, quantifying the reliability of each region. We further introduce a confidence-guided geometric estimation method, incorporating confidence into RANSAC-based pose initialization and bundle adjustment to reduce the influence of unreliable regions and enhance robustness under noisy channels. Simulations show that, compared to existing SemCom and traditional seperate source and channel coding, our framework maintains high image quality while significantly improving pose estimation accuracy and 3D structural consistency.

</details>

#### 2026-07-17 - BayesContact: Uncertain Pose Estimation via Visuo-Tactile Proposals and Simulation-based Inference

**Authors:** Aditya Kamireddypalli, Matias Mattamala, Joao Moura, Russell Buchanan, Sethu Vijayakumar, Subramanian Ramamoorthy
**Links:** [abs](https://arxiv.org/abs/2607.16123) - [pdf](https://arxiv.org/pdf/2607.16123)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BayesContact: Uncertain Pose Estimation via Visuo-Tactile Proposals and Simulation-based Inference
- 作者：Aditya Kamireddypalli, Matias Mattamala, Joao Moura, Russell Buchanan, Sethu Vijayakumar, Subramanian Ramamoorthy
- 出版日期：2026-07-17
- 分类：3D Reconstruction & Multi-view Geometry (主要)；Embodied / Robotics / AR Applications (次要)
- 链接：https://arxiv.org/abs/2607.16123

### 一句话总结
本文提出BayesContact，一种基于仿真的推理框架，通过融合视觉和触觉信息，实现对插销-孔装配任务中物体姿态的不确定性估计，相比纯视觉方法将插装成功率提升了30%。

### 研究问题
如何在接触密集型操作中，利用模拟驱动的视觉-触觉融合方法，无需离线训练，准确估计物体姿态并处理不确定性。

### 核心思路/方法
1. **粒子滤波信念**：使用一系列粒子维持对物体姿态的后验信念。
2. **仿真前向模型**：对每个姿态假设，渲染器预测深度测量值，物理仿真器在防护探测动作下预测接触结果。
3. **多模态融合**：将真实深度观测和力/力矩接触证据，与仿真预测结果进行评分对比，在线更新粒子信念。
4. **主动探测**：基于信息增益选择探测动作，主动消除姿态歧义。

### 主要贡献
1. 提出一个无需离线训练的视觉-触觉姿态估计框架，适用于新环境和新几何形状。
2. 利用仿真前向模型近似观测似然，融合深度与力/力矩信息。
3. 在模拟和真实机器人实验中，相比纯视觉推理，姿态可观测性和插装成功率提升30%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。
理由：该方法针对特定装配任务（插销-孔插入），提出了新颖的在线推理思路，无离线训练负担。实验效果有明确提升（30%），但属于领域专用方法，若您的兴趣不在接触密集型操作或机器人装配，则可降为低优先级。

</details>

<details>
<summary>Abstract</summary>

Contact-rich manipulation requires pose estimates that are often more accurate than what depth-only sensing provides. Existing methods, relying on vision and contact, employ costly offline training procedures that need to be retrained for new environments and geometries. We propose BayesContact, a Simulation-Based Inference framework for visuo-tactile pose estimation in peg-in-hole insertion. BayesContact maintains a particle belief over object pose and fuses depth observations with force/torque-derived contact evidence. We employ simulation based forward models to approximate these observation likelihoods. For each pose hypothesis, a renderer predicts depth measurements and a physics simulator predicts contact outcomes under guarded probing actions; both are scored against real observations to update the belief. The resulting multimodal belief also enables information-gain-based probing for active disambiguation. Across simulated geometries and real-robot experiments, BayesContact improves pose observability and insertion success over vision-only inference by 30%

</details>

#### 2026-07-17 - Adaptive Contrast Enhancement and Optimised Feature Matching for RootSIFT-Based Palm-Vein Recognition

**Authors:** Kaveen Perera, Fouad Khelifi, Ammar Belatreche
**Links:** [abs](https://arxiv.org/abs/2607.16077) - [pdf](https://arxiv.org/pdf/2607.16077)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Adaptive Contrast Enhancement and Optimised Feature Matching for RootSIFT-Based Palm-Vein Recognition
- 作者：Kaveen Perera, Fouad Khelifi, Ammar Belatreche
- 出版日期：2026-07-17
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.16077

### 一句话总结
本文提出一种名为ILACS-BGOT的自适应对比度增强方法，并结合RootSIFT特征与优化匹配策略，显著提升了掌静脉识别性能。

### 研究问题
掌静脉图像因近红外光散射和传感器限制导致的低对比度问题，影响识别准确率。

### 核心思路/方法
1. 提出ILACS-BGOT方法，在原有ILACS-LGOT基础上，用双向高斯加权重叠分块（BGOT）来减轻分块伪影，实现局部对比度自适应增强。
2. 将RootSIFT特征与KNN+RT（一种匹配策略）结合，并引入先前提出的MMD（均值与中值距离）滤波器。
3. 在CASIA、PolyU、PUT三个基准数据集上，使用42种MMD阈值与RT值的组合进行系统评估，分析参数变化对识别性能的影响。

### 主要贡献
1. 提出ILACS-BGOT增强算法，有效改善低对比度掌静脉图像质量。
2. 将RootSIFT与KNN+RT及MMD滤波器整合，并系统分析了参数变化对性能的影响。
3. 在三个公开数据集上取得更优的等错误率（EER）和准确率，证明方法具有良好的泛化能力。
4. 指出ILACS-BGOT机制可能适用于其他低对比度图像增强任务（如指静脉、掌纹识别）。

### 局限性
摘要未提供足够信息。未讨论方法的计算复杂度、实时性、对极端低质量图像的鲁棒性，以及与其他深度学习方法的直接对比。

### 阅读优先级
中。理由：方法在掌静脉识别领域有明确创新（对比度增强+特征匹配优化），实验结果在多个数据集上表现优异，但未涉及与当前主流深度学习方法的对比，且应用场景相对专一，适合对该方向有具体需求的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Palm-vein recognition is a highly secure biometric modality due to the uniqueness and subcutaneous nature of vein patterns. However, low contrast in palm-vein images, caused by NIR light scattering and sensor limitations, remains a significant challenge. To address this, we propose the Intensity-Limited Adaptive Contrast Stretching with Bidirectional Gaussian-weighted Overlapping Tiles (ILACS-BGOT) method, an enhancement of the previously developed ILACS with Layered Gaussian-weighted Overlapping Tiles (ILACS-LGOT) technique. ILACS enhances local contrast, while BGOT mitigates blocky artefacts. This study further integrates RootSIFT features with KNN+RT and incorporates the previously introduced Mean and Median Distance (MMD) filter to investigate the parameter variations of both MMD and RT, and their impact on recognition performance. A comprehensive analysis was conducted across three benchmark datasets (CASIA, PolyU, and PUT), using 42 combinations of MMD filter thresholds and RT values. Results were evaluated using EER and Accuracy. Findings reveal that higher template sizes improve performance, while varying MMD thresholds reflect dataset-specific rotational variations. The proposed system demonstrates superior generalisability, achieving significant improvements in both EER and Accuracy over existing methods. Furthermore, the underlying ILACS-BGOT mechanism suggests potential applicability beyond palm vein recognition to other biometric modalities such as finger vein and palmprint recognition, and more generally to low-contrast image enhancement across computer vision applications.

</details>

#### 2026-07-17 - PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects

**Authors:** Leon Jungemeyer, Alejandro Magaña, Gautham Mohan, Matthias Karl, Daniel Werdehausen
**Links:** [abs](https://arxiv.org/abs/2607.16015) - [pdf](https://arxiv.org/pdf/2607.16015)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects
- 作者：Leon Jungemeyer, Alejandro Magaña, Gautham Mohan, Matthias Karl, Daniel Werdehausen
- 出版日期：2026-07-17
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要链接：https://arxiv.org/abs/2607.16015；PDF链接：https://arxiv.org/pdf/2607.16015

### 一句话总结
PIXIE是一个零样本的6D位姿估计框架，仅使用无纹理3D模型和RGB图像，通过几何一致性实现对未见物体（含装配缺陷）的鲁棒位姿估计。

### 研究问题
如何在仅有未纹理3D模型且物体存在几何偏差（如损伤或装配缺陷）的情况下，零样本地从RGB图像估计物体的6D位姿，同时克服光照和纹理变化的影响。

### 核心思路/方法
1. 从采样参考视角渲染物体的合成深度图与法线图。
2. 利用预训练的跨模态特征匹配器，将查询RGB图像的特征与合成深度/法线图进行匹配。
3. 将匹配的关键点反投影到3D空间，获得2D-3D对应关系。
4. 通过Perspective-n-Point (PnP) 算法求解6D位姿。
5. 引入对应关系过滤机制，处理模型与物理物体之间的几何偏差。

### 主要贡献
- 提出PIXIE，一种零样本、纹理无关的6D位姿估计方法，仅需无纹理3D模型。
- 通过仅依赖几何信息，实现对照明和纹理变化的内在鲁棒性。
- 在公开基准上对无纹理物体取得当时最优结果（无需物体特定训练）。
- 提出一个包含装配缺陷、纹理变化和遮挡的新数据集，展示实际应用能力。

### 局限性
摘要未提供足够信息说明具体局限性，例如计算效率、对极端几何偏差的鲁棒性边界或未测试物体的类别范围等。

### 阅读优先级
高。理由：该方法针对工业场景下纹理缺失、几何缺陷和零样本需求等实际挑战，提出了简洁高效的解决方案，并在标准基准上取得最优结果，对机器人和计算机视觉领域有直接应用价值。

</details>

<details>
<summary>Abstract</summary>

6D pose estimation remains a key challenge in robotics and computer vision, particularly in industrial environments. The deployment of currently available data-driven methods is often limited by resource-intensive data pipelines, reliance on textured 3D models, and sensitivity to geometric deviations caused by damages or assembly defects. We present PIXIE, a zero-shot framework that estimates the 6D pose of an object from an RGB image using only an untextured 3D model. Synthetic depth and normal maps are rendered from sampled reference viewpoints and matched to the query image via a pretrained cross-modality feature matcher. Matched keypoints are back-projected to obtain 2D--3D correspondences for PnP-based pose estimation. Relying exclusively on geometry makes the method inherently robust to lighting and texture variation, while correspondence filtering handles geometric deviations between the model and physical object. We evaluate on widely-used public benchmarks, reporting state-of-the-art results on texture-less objects without object-specific training, and introduce a novel dataset with assembly defects, texture variations, and occlusion to demonstrate real-world applicability.

</details>

#### 2026-07-16 - Communication-Efficient Relative Pose Estimation with Vision Foundation Models for Ephemeral Collaborative Perception

**Authors:** Qihang Li, Jo-Hao Huang, Jiewen Liu, Suyoung Kang, Hao Zhang, Peng Gao
**Links:** [abs](https://arxiv.org/abs/2607.14539) - [pdf](https://arxiv.org/pdf/2607.14539)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Communication-Efficient Relative Pose Estimation with Vision Foundation Models for Ephemeral Collaborative Perception
- 作者：Qihang Li, Jo-Hao Huang, Jiewen Liu, Suyoung Kang, Hao Zhang, Peng Gao
- 出版日期：2026-07-16
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.14539 | PDF: https://arxiv.org/pdf/2607.14539

### 一句话总结
提出CERPE系统框架，利用视觉基础模型实现通信高效的相对位姿估计，专为短暂协作感知场景设计。

### 研究问题
如何解决多机器人系统在短暂相遇、有限带宽、间歇性或缺失视觉重叠条件下的通信高效相对位姿估计问题。

### 核心思路/方法
1. 使用连续共享的固定大小描述符（而非原始观测数据）进行事件触发式的原始图像请求，减少通信冗余。
2. 针对无视觉重叠场景，通过度量的尺度化自运动传播机器人间相对位姿，维持估计连续性。
3. 整体框架协调视觉基础模型，联合估计自运动与机器人间相对位姿。

### 主要贡献
1. 提出CERPE系统框架，在短暂协作感知中显著降通信开销。
2. 设计独立于位姿估计的固定大小描述符门控机制，实现事件触发的原始图像传输。
3. 通过自运动传播处理非重叠相遇场景，保持相对位姿估计稳定性。
4. 仿真与真实机器人实验表明CERPE在6-DoF相对位姿估计上优于所选基线方法。

### 局限性
摘要未提供实验细节，因此无法分析具体局限性，如是否依赖特定视觉基础模型、对极端遮挡或快速运动的鲁棒性、实际通信带宽节省比例等。（摘要未提供足够信息）

### 阅读优先级
高
理由：该研究针对多机器人协作感知中的通信与视觉重叠瓶颈，提出实用框架，且结合了视觉基础模型的近期进展；实验涵盖仿真与真实场景，具有应用潜力。对于从事多机器人系统或协作感知的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Relative pose estimation is a fundamental capability for collaborative perception and coordination in multi-robot systems. However, robots encountering each other in real-world environments often operate in short interaction windows and must operate under limited communication bandwidth with intermittent or missing visual overlap caused by occlusions or limited fields of view. Existing approaches typically rely on global reference frames, assume sustained view overlap, or incur prohibitive communication costs, thereby limiting their applicability to ephemeral collaborative perception. To address these challenges, we introduce communication-efficient relative pose estimation (CERPE), a system-level framework that coordinates vision foundation models to jointly estimate ego-motion and inter-robot relative pose. CERPE reduces unnecessary raw-observation exchange by using continuously shared fixed-size descriptors to gate event-triggered raw-image requests independently of pose estimation. Non-overlapping encounters are handled by propagating inter-robot relative poses through metrically scaled ego-motion, thus maintaining relative pose estimates even in the absence of visual overlap. Experiments in simulation and real-world robots show that CERPE improves 6-DoF relative pose estimation over selected baselines in ephemeral collaborative perception.

</details>

#### 2026-07-16 - G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction

**Authors:** Dasong Gao, Vivienne Sze, Sertac Karaman
**Links:** [abs](https://arxiv.org/abs/2607.14470) - [pdf](https://arxiv.org/pdf/2607.14470)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G²SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction
- 作者：Dasong Gao, Vivienne Sze, Sertac Karaman
- 出版日期：2026-07-16
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.14470

### 一句话总结
G²SR提出一种结合轻量级神经网络前端与解析几何后端的混合方法，用于从少量视角的RGB图像中快速、内存高效地进行高斯散点表面重建，在多个数据集上达到或超越现有方法精度，并大幅降低计算开销。

### 研究问题
如何从少量视角的RGB图像中，实现快速、几何精确且内存占用小的3D高斯散点表面重建，以减少“浮动伪影”并提升在线移动平台的适用性。

### 核心思路/方法
该方法将任务分解为两步：1）使用轻量级神经网络前端检测并跟踪图像平面上的2D高斯散点对应关系；2）利用解析几何后端，基于多视角几何原理将这些2D对应点三角化重建为公制尺度的3D高斯散点。整个流程避免了传统端到端方法中大型Transformer网络的使用。

### 主要贡献
1. 提出G²SR框架，利用多视角几何中的解析关系从2D对应点直接推得3D散点，降低了问题的病态性。
2. 在ScanNet、Replica和DTU数据集上，几何精度匹配或超越当前最先进的端到端方法。
3. 在2-3视角、384×512分辨率输入下，实现每秒69-89次重建速度，且GPU内存仅需203 MB（较对比方法低5-107倍），显著提升内存效率和速度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该论文针对少视角表面重建中的实时性和内存限制问题，提出了一种混合几何与轻量学习的创新方案，实验效率指标突出（速度提升与内存降低数十倍），且与现有方法精度相当，对移动机器人在线3D重建具有实际参考价值。

</details>

<details>
<summary>Abstract</summary>

Few-view surface reconstruction recovers the visible surfaces of a scene from a few posed RGB images, providing the 3D models that robots need to explore and interact online. On mobile platforms, the reconstruction must be fast and geometrically accurate while keeping a small memory footprint to ensure safe and efficient operation. 3D Gaussian Splatting (3DGS) offers a high-fidelity scene representation, but building it from a few views is ill-posed, as many distinct surfaces reproduce the same images, making traditional photometric methods prone to "floater" artifacts. End-to-end methods resolve the ambiguity by regressing splats with large, usually Transformer-based, networks that require heavy compute and memory while generalizing poorly to new scenes. We propose G2SR, which exploits a well-posed core of the task: given cross-view 2D splat correspondences, 3D splats follow analytically from multi-view geometry. G2SR employs a lightweight neural frontend to detect and track 2D Gaussian splats on the image plane and an analytic backend to triangulate each into a metric-scale 3D splat. On ScanNet, Replica, and DTU, G2SR matches or exceeds the geometric accuracy of state-of-the-art end-to-end methods while running at 69-89 reconstructions per second within 203 MB of GPU memory (5-107x less) for 2- and 3-view inputs at 384 x 512 resolution, offering a practical path to online Gaussian-based surface reconstruction.

</details>

#### 2026-07-15 - COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction

**Authors:** Phu Pham, Damon Conover, Aniket Bera
**Links:** [abs](https://arxiv.org/abs/2607.13524) - [pdf](https://arxiv.org/pdf/2607.13524)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction
- 作者：Phu Pham, Damon Conover, Aniket Bera
- 出版日期：2026-07-15
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2607.13524) | [PDF](https://arxiv.org/pdf/2607.13524)

### 一句话总结
本文提出COLMAR，一个基于共享策略学习的多智能体协同视点规划框架，通过重建感知目标优化主动三维重建的质量与覆盖。

### 研究问题
多智能体主动三维重建中，因协调不足（如冗余观测、空间聚类）导致重建质量下降，如何设计有效的协同视点政策以在有限传感预算下提升重建精度与覆盖。

### 核心思路/方法
1. 将视点分配建模为基于地图中心观测的**共享策略优化**问题。
2. 引入**重建感知目标函数**，包含重叠感知覆盖、团队级新区域发现、碰撞安全探索三项指标。
3. 利用增量重建更新生成密集反馈，将探索行为与下游几何质量对齐。
4. 采用参数共享的**近端策略优化（PPO）**训练策略，部署时各智能体独立执行动作，基于融合团队地图决策，无需智能体间消息传递。
5. 选定视点通过**3D高斯泼溅（3DGS）**重建，实现高保真光度评估。

### 主要贡献
- 提出多智能体协同视点学习框架COLMAR，通过重建感知目标优化协调策略。
- 设计无需在线通信的共享策略机制，降低部署复杂度。
- 在GLEAM和Replica数据集上，相比启发式和非协同基线，在相同传感预算下实现高达**54%的重建精度提升**和**49%的覆盖增加**。

### 局限性
摘要未提供足够信息（如失败场景、计算开销、泛化至复杂场景的瓶颈等）。

### 阅读优先级
**高**  
理由：该工作针对多智能体主动三维重建中的关键协调难题，提出了结合强化学习与3DGS的新框架，实验提升显著（精度/覆盖均超50%），且属于近期的前沿方向（2026年发表）。适合关注多机器人重建、视点规划及神经渲染的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Active 3D reconstruction requires selecting informative viewpoints under limited sensing budgets. In multi-agent settings, coordination inefficiencies such as redundant observations and spatial clustering can significantly reduce reconstruction quality. We present COLMAR, a cooperative view policy learning framework for multi-agent active 3D reconstruction. COLMAR formulates viewpoint allocation as a shared policy optimization over map-centric observations and introduces a reconstruction-aware objective that promotes overlap-aware coverage, team-level discovery, and collision-safe exploration. Dense feedback derived from incremental reconstruction updates aligns exploration behavior with downstream geometric quality. The policy is trained using parameter-sharing Proximal Policy Optimization (PPO) with independent per-agent action selection at deployment, conditioned on a fused team map and without inter-agent message passing for decision making. Selected viewpoints are then reconstructed with 3D Gaussian Splatting (3DGS) for high-fidelity photometric evaluation. Experiments on GLEAM and Replica demonstrate consistent improvements over heuristic and non-cooperative baselines, achieving up to 54% higher reconstruction accuracy and 49% greater coverage under matched sensing budgets.

</details>

#### 2026-07-15 - CASA-SDF: Curriculum-Aware Spatial Adaptation with Curvature-Guided Density for Neural Implicit Surface Reconstruction

**Authors:** Lei Yang, Weiqing Li, Zhiyong Su, Liang Xiao
**Links:** [abs](https://arxiv.org/abs/2607.13492) - [pdf](https://arxiv.org/pdf/2607.13492)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CASA-SDF: Curriculum-Aware Spatial Adaptation with Curvature-Guided Density for Neural Implicit Surface Reconstruction
- 作者：Lei Yang, Weiqing Li, Zhiyong Su, Liang Xiao
- 出版日期：2026-07-15
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.13492 | PDF: https://arxiv.org/pdf/2607.13492

### 一句话总结
本文提出CASA-SDF框架，通过课程感知的空间自适应监督和曲率引导的密度变换，同时提升室内场景中平面区域的平滑性和薄结构的细节重建精度。

### 研究问题
室内场景由于几何异质性（大面积无纹理平面与精细薄结构并存），现有隐式神经表示方法难以同时实现平面平滑（避免高频伪影）和薄结构细节保留（克服MLP的光谱偏置），通常导致过平滑或伪影。

### 核心思路/方法
1. **混合空间自适应不确定度退火（SAUA）**：融合语义和光度不确定度，构建像素级课程，在训练初期抑制不可靠的单目先验监督，保留可靠区域的正则化，后期允许数据驱动的光度优化。
2. **曲率感知局部自适应密度变换（CALADT）**：通过曲率代理逐步调节SDF到密度的映射锐度，增强对薄结构的表示能力，同时不破坏平面稳定性。

### 主要贡献
- 提出了统一框架CASA-SDF，通过监督和表示能力的空间自适应互补适配，解决室内重建中几何异质性的挑战。
- 设计SAUA策略，基于像素级不确定度实现单目先验的课程式监督，平衡可靠性和灵活性。
- 设计CALADT机制，利用曲率代理动态调整密度变换锐度，改善高频结构的表示。
- 在基准室内数据集上验证，相比现有方法提高了表面完整性和高频结构细节恢复，且未牺牲平面稳定性。

### 局限性
摘要未提供足够信息，例如对极端噪声/缺失区域的鲁棒性、计算开销或与其他方法的定量对比细节。

### 阅读优先级
高
- 理由：该工作直接针对室内场景重建中的核心难点（平面与薄结构平衡），提出创新的监督和表示适应机制（SAUA和CALADT），实验证明有显著提升。对于从事3D重建、隐式表示或室内场景理解的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Neural implicit representations have emerged as a powerful paradigm for 3D reconstruction. However, high-fidelity indoor surface reconstruction remains a significant challenge, primarily due to the pronounced \emph{geometric heterogeneity} of indoor scenes. Large texture-less planar regions typically require stronger regularization to suppress high-frequency artifacts, while thin structures demand sharper, more adaptive representations to mitigate the spectral bias of multi-layer perceptrons (MLPs) and prevent over-smoothing. Existing approaches often rely on spatially indiscriminate prior supervision and a scene-global SDF-to-density transformation, which constrains their ability to balance planar smoothness and detail preservation. In this paper, we propose CASA-SDF (Curriculum-Aware Spatial Adaptation for SDF), a unified framework that addresses this challenge via complementary adaptations of supervision and representation capacity. Specifically, Hybrid Spatially-Adaptive Uncertainty Annealing (SAUA) fuses semantic and photometric uncertainties to construct a pixel-wise curriculum for monocular prior supervision. This strategy maintains regularization in reliable regions while attenuating unreliable supervision early in training to enable data-driven photometric refinement. Meanwhile, Curvature-Aware Locally Adaptive Density Transformation (CALADT) progressively modulates the sharpness of the SDF-to-density mapping via a curvature proxy to enhance the representation of thin structures. Extensive experiments on benchmark indoor datasets demonstrate that CASA-SDF improves surface completeness and detail recovery on high-frequency structures, without compromising the stability of planar surfaces.

</details>

#### 2026-07-15 - Topology-Agnostic Mesh Reconstruction of Deformable Objects from Sparse Touch

**Authors:** Everest Yang
**Links:** [abs](https://arxiv.org/abs/2607.13479) - [pdf](https://arxiv.org/pdf/2607.13479)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Topology-Agnostic Mesh Reconstruction of Deformable Objects from Sparse Touch
- 作者：Everest Yang
- 出版日期：2026-07-15T06:17:35Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.13479

### 一句话总结
论文提出一种拓扑无关的单一估计器，仅通过少量触觉信号（无视觉）即可重建可变形物体的完整网格，并利用深度集成不确定性指导触觉采样位置以降低重建误差。

### 研究问题
如何在无视觉条件下（如黑暗、遮挡等场景），仅依赖稀疏的触觉接触点重建可变形物体的完整三维网格形状，并优化触觉采样策略以提升重建精度。

### 核心思路/方法
- 使用**单一置换不变交叉注意力架构**，统一处理1D绳索、2D布料和3D体积软体三种拓扑结构，无需针对不同拓扑分别设计模型。
- 训练**深度集成估计器**，从少量触觉输入直接输出物体完整网格，并产生不确定性估计。
- 利用不确定性估计指导下一次触觉采样位置（主动触觉策略），在给定触觉预算下降低误差。

### 主要贡献
- 提出第一个拓扑无关的稀疏触觉网格重建方法，单一架构适用于绳索、布料、体积软体。
- 相比非学习的几何网格补全和高斯过程曲面基线，重建误差降低约三分之二。
- 基于深度集成的不确定性主动采样策略在低预算下优于随机触摸和高斯过程主动基线，尤其在自遮挡和误差尾部分表现更明显。
- 当视觉可用时，触觉采样位置影响不大，凸显无视觉场景的研究价值。

### 局限性
摘要未提供足够信息（如对高度自变形、多物体交互或真实物理接触数据的测试结果，以及计算复杂度等）。

### 阅读优先级
**中**：该工作针对无视觉环境下的可变形物体重建问题，方法新颖（拓扑无关、主动触觉），但领域较为专精，适合从事触觉感知、机器人操作或非刚性重建的研究者阅读。对于通用3D重建社区，参考价值相对有限。

</details>

<details>
<summary>Abstract</summary>

Estimating the full shape of a deformable object is especially challenging when vision is unavailable: in the dark, inside an opaque bag, behind the manipulating hand, or under heavy self-occlusion. Touch is the natural sensor in these settings, but touches are sparse and local. We present a single topology-agnostic estimator that reconstructs the full mesh of a deformable object from only a few touches and no vision, using one permutation-invariant cross-attention architecture that handles a 1D rope, a 2D cloth, and a 3D volumetric soft body. The learned estimator reduces reconstruction error by roughly two-thirds relative to non-learned geometric mesh completion and a Gaussian-process surface baseline, and it outperforms a simpler global-pool set encoder, with the gap growing as more touches are observed. We then show that the estimator's deep-ensemble uncertainty can be used to learn where to touch next, which lowers error further and beats both random touching and a Gaussian-process active baseline at sparse budgets. This gain is modest on average but grows with self-occlusion and on the error tail. When vision is also available, where to touch barely matters, motivating the vision-free setting we study.

</details>

#### 2026-07-15 - DreamSat-Pose: Spacecraft Pose Estimation from Single-View 3D Reconstructions and Learned 2D-3D Feature Matching

**Authors:** Josiane Uwumukiza, Jocelyn Zhao, Giovanni Lavezzi, Giacomo Battaglia, Paolo Panicucci, Minduli C. Wijayatunga, Victor Rodriguez-Fernandez, Richard Linares
**Links:** [abs](https://arxiv.org/abs/2607.13449) - [pdf](https://arxiv.org/pdf/2607.13449)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DreamSat-Pose: Spacecraft Pose Estimation from Single-View 3D Reconstructions and Learned 2D-3D Feature Matching
- 作者：Josiane Uwumukiza, Jocelyn Zhao, Giovanni Lavezzi, Giacomo Battaglia, Paolo Panicucci, Minduli C. Wijayatunga, Victor Rodriguez-Fernandez, Richard Linares
- 出版日期：2026-07-15T05:12:48Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.13449

### 一句话总结
本文提出DreamSat-Pose框架，通过单张图像重建未知航天器的3D形状模型并学习2D-3D对应关系，实现6自由度姿态估计，在SPE3R数据集上达到0.157度的平均指向误差。

### 研究问题
如何在未知目标航天器的情况下，通过单张图像同时实现目标三维形状重建和准确的6自由度姿态估计。

### 核心思路/方法
1. **单视图三维重建**：首先从单张输入图像重建目标的3D形状模型（点云）。  
2. **特征提取与匹配**：使用冻结的DINOv3视觉Transformer提取图像特征，用可训练的动态图卷积神经网络（DGCNN）编码器从重建点云中提取几何特征。  
3. **双流Transformer匹配器**：通过交替自注意力和交叉注意力机制精炼描述符，生成软对应关系。  
4. **姿态恢复**：将软对应关系输入Perspective-n-Point求解器，计算最终6自由度姿态。

### 主要贡献
1. 提出一个端到端框架，联合实现未知航天器的单视图三维重建与6自由度姿态估计。  
2. 设计双流Transformer匹配器，通过交替注意力机制实现2D-3D特征匹配。  
3. 在SPE3R数据集上验证了有效性，仅使用单张图像和重建几何即可达到0.157度平均指向误差，展现了良好的泛化能力。

### 局限性
摘要未提供足够信息：未提及具体失败案例、计算复杂度、对遮挡或光照变化的鲁棒性分析，以及重建几何质量对姿态估计精度的直接影响。

### 阅读优先级
**高**。理由：该研究针对航天器自主交会中的关键问题（未知目标形状与姿态联合估计），方法设计新颖（融合视觉Transformer、图神经网络和双流匹配器），且实验指标（0.157度指向误差）具有吸引力，对3D重建与姿态估计领域具有参考价值。

</details>

<details>
<summary>Abstract</summary>

6-DoF pose estimation is a critical task in autonomous rendezvous and proximity operations. In the case of an unknown target, this task becomes challenging as it shall be paired with the reconstruction of the target shape model. In this article, we propose a novel framework for single-shot shape and pose estimation of unknown spacecraft objects. Given a single image, we first reconstruct a 3D shape model of the target, then estimate the relative six-degrees-of-freedom pose by learning dense 2D-3D correspondences. The image features are extracted using a frozen DINOv3 vision transformer, while the geometric features are computed from the reconstructed point cloud using a trainable dynamic graph convolutional neural network encoder. A dual-stream transformer matcher refines descriptors through alternating self- and cross-attention, producing soft correspondences that are passed to a Perspective-$n$-Point solver for pose recovery. We evaluate the method on the SPE3R dataset and consider FoundationPose as a representative baseline for current state-of-the-art capabilities. Results show reliable pose estimates achieving 0.157 degrees mean pointing error using only a single image and reconstructed geometry, demonstrating strong generalization to unseen spacecraft.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-20 - QIRF Quantum-Inspired Non-Orthogonal Function-Space Compression for 3D Gaussian Splatting

**Authors:** Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang
**Links:** [abs](https://arxiv.org/abs/2607.18067) - [pdf](https://arxiv.org/pdf/2607.18067)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：QIRF: 量子启发的非正交函数空间压缩方法用于3D高斯泼溅
- 作者：Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang
- 出版日期：2026-07-20
- 分类：神经场景表示与渲染
- 链接：摘要: https://arxiv.org/abs/2607.18067 / PDF: https://arxiv.org/pdf/2607.18067

### 一句话总结
本文提出QIRF方法，通过量子启发的非正交函数空间压缩技术，在保持重建质量的同时大幅减少3D高斯泼溅中的高斯原语数量与存储成本。

### 研究问题
如何有效压缩3D高斯泼溅模型中因高斯基函数强重叠和非正交性导致的冗余，从而降低存储和渲染开销。

### 核心思路/方法
1. 将相邻高斯原语建模为局部非正交基，并将原语减少问题转化为子空间感知的选择问题。
2. 构建解析高斯重叠矩阵和辐射响应密度矩阵，分别表征功能冗余和渲染相关性。
3. 利用广义特征分解识别主导局部子空间，并选择代表性高斯原语。
4. 基于RRDM的响应模型和细节感知保护机制，在激进剪枝下保留视觉重要的高频结构。

### 主要贡献
1. 提出QIRF，一种量子启发的非正交函数空间压缩方法，首次系统探索高斯基函数非正交性导致的冗余。
2. 在13个场景（Mip-NeRF 360、Tanks and Temples、Deep Blending）上，平均高斯数量减少71.7%，原始PLY存储压缩约3.54倍。
3. 重建质量与3DGS相当，平均PSNR提升0.10 dB，平均渲染速度相比3DGS提升34.3%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该方法针对3D高斯泼溅中的非正交基冗余这一未充分探索的问题提出创新压缩框架，实验在多个基准数据集上取得显著压缩率和渲染速度提升，且质量保持良好，对场景表示与渲染领域的实际应用有重要价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves high-quality real-time rendering by representing a scene with a large collection of anisotropic Gaussian primitives. However, complex scenes often require millions of Gaussians, resulting in substantial storage and rendering costs. Existing compression methods mainly reduce redundancy through primitive-wise pruning, attribute quantization, clustering, or neural coding, while redundancy caused by strongly overlapping and non-orthogonal Gaussian basis functions remains largely unexplored. We present QIRF, a quantum-inspired non-orthogonal function-space compression method for 3D Gaussian Splatting. QIRF models neighboring Gaussian primitives as a local non-orthogonal basis and formulates primitive reduction as a subspace-aware selection problem. Specifically, an analytic Gaussian overlap matrix and a radiance-response density matrix are constructed to characterize functional redundancy and rendering relevance. Generalized eigendecomposition is then used to identify the dominant local subspace and select representative Gaussian primitives. An RRDM-based response model and detail-aware safeguarding further preserve visually important high-frequency structures under aggressive pruning. Experiments on 13 scenes from Mip-NeRF 360, Tanks and Temples, and Deep Blending show that QIRF reduces the Gaussian count and raw PLY storage by 71.7 percent on average, corresponding to approximately 3.54 times compression, while maintaining reconstruction quality comparable to 3DGS and achieving a marginal average PSNR improvement of 0.10 dB. QIRF also improves the average rendering speed over 3DGS by 34.3 percent. These results suggest that non-orthogonal function-space redundancy is an important yet underexplored source of representational redundancy in explicit Gaussian radiance fields.

</details>

#### 2026-07-20 - Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting

**Authors:** Chengbo Wang, Guozheng Ma, Jinhong Wu, Tie Ji, Yizhen Lao
**Links:** [abs](https://arxiv.org/abs/2607.17965) - [pdf](https://arxiv.org/pdf/2607.17965)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting
- 作者：Chengbo Wang, Guozheng Ma, Jinhong Wu, Tie Ji, Yizhen Lao
- 出版日期：2026-07-20
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.17965

### 一句话总结
本文发现3D高斯泼溅优化中存在一种称为“模糊陷阱”的梯度偏差，并通过引入随机播种和随机分裂两种简单探索策略来克服该陷阱，从而提升渲染质量。

### 研究问题
3D高斯泼溅的显式建模在优化过程中会产生梯度偏差，导致非凸优化容易收敛到局部次优解（即“模糊陷阱”），如何解决这一根本性局限？

### 核心思路/方法
1. 通过数学分析将模糊陷阱分为两种子类型：远侧模糊陷阱和近侧模糊陷阱。
2. 提出两种简单的探索策略：随机播种用于缓解远侧模糊陷阱，随机分裂用于缓解近侧模糊陷阱。

### 主要贡献
1. 首次识别并形式化了3D高斯泼溅优化中的“模糊陷阱”问题，并将其分为两类。
2. 提出了两种极简的探索操作（随机播种和随机分裂），互补性地有效克服了该陷阱。
3. 实验证明这些探索机制在多个数据集上实现了高质量渲染性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文针对3D高斯泼溅这一当前热门渲染方法的根本优化缺陷提出了新的解决思路，问题明确、方法简单有效，对从事神经渲染或场景重建的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) employs Gaussian primitives for explicit scene representation, facilitating real-time, high-fidelity reconstruction and novel view synthesis of complex scenes. However, the explicit modeling inherent in 3DGS introduces a gradient bias during optimization, rendering its non-convex optimization process highly susceptible to convergence toward local suboptimal solutions. This constitutes a fundamental limitation in 3DGS optimization, which we term the Blur Trap. To address this limitation, we integrate simple explicit exploration into the 3DGS optimization framework. First, through rigorous mathematical analysis of the 3DGS optimization formulation, we identify the underlying optimization bias responsible for the Blur Trap and categorize it into two distinct subtypes: the Far-Side Blur Trap and the Near-Side Blur Trap. Subsequently, we propose two highly straightforward exploration strategies (Random Seeding and Random Splitting) to mitigate the far-side and near-side blur traps, respectively. Experimental validation demonstrates that the incorporation of these exploration operators effectively and complementarily overcome the Blur Trap, achieving high-quality rendering performance across multiple datasets. Project page: https://chengbo-wang.github.io/ExploreGS/

</details>

#### 2026-07-20 - Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based Error Concealment

**Authors:** Yuxuan Tao, Xuerui Ma, Hao Zhang, Chunhua Peng
**Links:** [abs](https://arxiv.org/abs/2607.17916) - [pdf](https://arxiv.org/pdf/2607.17916)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based Error Concealment
- 作者：Yuxuan Tao, Xuerui Ma, Hao Zhang, Chunhua Peng
- 出版日期：2026-07-20
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.17916

### 一句话总结
本文提出了一种针对3D高斯溅射（3DGS）压缩流在丢包网络传输中的鲁棒性增强框架，通过原子锚点打包和基于图神经网络的错误隐藏机制，显著减少渲染失真。

### 研究问题
现有3DGS压缩方案（如HAC++）的比特流在网络传输时对丢包敏感，丢包会导致锚点属性不一致、渲染出现严重伪影，影响实时神经渲染的可靠性。

### 核心思路/方法
- **编码端**：采用原子锚点级别打包，将每个锚点的所有属性联合封装，使丢包从属性损坏变为干净的锚点缺失；配合分层随机分组，将丢包在空间上分散，避免连续大空洞。
- **解码端**：将恢复视为先验感知的属性修复。提出上下文感知残差插值分支（CARI），利用哈希网格先验预测和邻域残差构建鲁棒基线；轻量双层图神经网络（GNN）通过交叉注意力机制在哈希网格先验上细化高频属性残差；引入属性级置信度控制，当学习到的预测不可靠时回退至插值。

### 主要贡献
- 提出首个针对3DGS压缩流在丢包网络传输的鲁棒框架，并集成原子打包与分层分组策略。
- 设计结合哈希网格先验、残差插值及图神经网络的错误隐藏方法，实现先验感知的属性修复。
- 在三种基准数据集（BungeeNeRF, Mip-NeRF 360, Tanks and Temples）上，20%随机丢包条件下，相比无隐藏方案显著提升，将平均PSNR退化限制在约3 dB以内（相对于无损HAC++参考）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接解决3DGS压缩在实时网络传输中的实际鲁棒性问题，方法结合了原子打包、GNN和先验感知修复，实验验证效果显著；针对新兴的3DGS应用场景具有明确价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) and recent compression schemes such as HAC++ enable high-fidelity real-time neural rendering, but their bitstreams are fragile under packet loss during network streaming. Existing compression methods often separate correlated anchor attributes into independent streams, so losing one packet can create attribute-inconsistent broken anchors and severe rendering artifacts. We propose a packet-loss robust 3DGS transmission and error concealment framework. On the encoder side, anchor-level atomic packaging jointly encapsulates all attributes of each anchor, converting corrupted-attribute failures into clean missing-anchor erasures. Stratified random grouping further disperses packet losses across the spatial domain to avoid large contiguous voids. On the decoder side, we formulate recovery as prior-aware attribute inpainting. A Context-Aware Residual Interpolation (CARI) branch uses hash-grid prior predictions and neighboring residuals to build a robust baseline, while a lightweight two-layer graph neural network with cross-attention over hash-grid priors refines high-frequency attribute residuals. Attribute-wise confidence control falls back to interpolation when learned predictions are unreliable. Experiments under 20 percent random packet loss on BungeeNeRF, Mip-NeRF 360, and Tanks and Temples show that the proposed method substantially improves over no-concealment transmission and limits average PSNR degradation to about 3 dB relative to the lossless HAC++ reference.

</details>

#### 2026-07-20 - CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling

**Authors:** Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen
**Links:** [abs](https://arxiv.org/abs/2607.17842) - [pdf](https://arxiv.org/pdf/2607.17842)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling
- 作者：Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen
- 出版日期：2026-07-20T11:33:51Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.17842

### 一句话总结
CaT-GS 通过帧间缓存、预计算和分块调度优化，大幅提升大场景3D高斯泼溅（3DGS）渲染效率，实现最高10倍加速。

### 研究问题
大场景下3DGS渲染存在冗余预处理、视角相关的遮挡冗余以及分块级负载不均问题，导致GPU利用率低、性能下降。

### 核心思路/方法
提出三项关键技术：1）投机性多帧预处理方法，消除连续帧间的冗余计算；2）帧间缓存机制，消除视角冗余渲染阶段；3）专用内核重构光栅化任务，缓解分块负载不均衡，提升GPU利用率。

### 主要贡献
- 识别并系统分析大场景3DGS渲染中的三大效率瓶颈。
- 提出CaT-GS，一种高效的新型3DGS渲染管线，包含帧间缓存与分块调度策略。
- 实验表明，相比原始3DGS实现最高10倍加速，相比此前最先进方法提升最高70%，为大场景高保真实时渲染设立新基准。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：针对3DGS在大规模场景下的实际部署瓶颈，提出了系统性的工程优化方案，加速比显著且方法新颖，对实时神经渲染应用有直接指导价值。

</details>

<details>
<summary>Abstract</summary>

Recent breakthroughs in 3D Gaussian Splatting (3DGS) have advanced neural rendering with high fidelity and speed. However, its performance degrades significantly in large-scale scenes due to the computational burden of tile-based rasterization. Existing optimization efforts either require costly scene re-training or focus on narrow aspects of the pipeline, overlooking critical inefficiencies in real-world deployments. Through a comprehensive analysis, we identify three primary sources of redundancy and low GPU utilization: redundant inter-frame pre-processing, viewpoint-based occlusion redundancy, and severe tile-level load imbalance. To address these issues, we propose CaT-GS, a novel and efficient 3DGS rendering pipeline. CaT-GS introduces a speculative multi-frame preprocessing method to eliminate redundant computations across consecutive frames, and an inter-frame caching mechanism to eliminate viewpoint redundant rendering stages. Furthermore, it refactors rasterization tasks with a dedicated kernel to mitigate tile load imbalance, significantly boosting GPU utilization. Extensive experiments demonstrate that CaT-GS achieves a speedup of up to 10 times over the original 3DGS and up to 70% over previous state-of-the-art methods, establishing a new benchmark for high-fidelity, real-time rendering of large-scale scenes.

</details>

#### 2026-07-20 - FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System

**Authors:** Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang
**Links:** [abs](https://arxiv.org/abs/2607.17803) - [pdf](https://arxiv.org/pdf/2607.17803)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, Gaussian Splatting, inverse rendering, rendering, splatting, manipulation, mapping, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System
- 作者：Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang
- 出版日期：2026-07-20
- 分类：Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.17803, PDF: https://arxiv.org/pdf/2607.17803

### 一句话总结
本文提出FF-ProCams，一种前馈式3D高斯逆渲染框架，用于投影-相机系统，在保持高保真结果的同时实现实时重建（0.13秒），显著速度提升并支持未知投影模式和视角。

### 研究问题
如何解决投影-相机系统中传统逆渲染方法耗时优化（每场景优化）与前馈方法无法适应空间可变投影照明之间的矛盾，实现精度与效率的平衡。

### 核心思路/方法
1. **前馈框架设计**：采用混合Mamba2-Transformer编码器，从稀疏多视角观测中聚合跨视角几何和光度线索，并通过轻量级头部一次性预测可重照明的3D高斯表示。
2. **投影感知渲染器**：设计可微渲染器，合成任意主动照明和投影-相机姿态下的相机观测图像。
3. **大规模合成数据集**：构建覆盖多样物体几何和表面材质的合成ProCams数据集，用于前馈训练。

### 主要贡献
1. 提出了首个前馈式3D高斯逆渲染框架FF-ProCams，用于投影-相机系统，无需每场景优化。
2. 设计了投影感知的可微渲染器，支持任意主动照明和姿态下的图像合成。
3. 构建了大规模合成ProCams数据集，支持前馈训练。
4. 实验表明：仅用8个输入视图，性能优于使用297视图的优化基线，并将测试时重建速度降至0.13秒（三个到五个数量级加速）。

### 局限性
摘要未提供足够信息（如对复杂光照、极端材质或真实场景的泛化能力，以及大规模合成数据与真实世界性能的固有差异均未提及）。

### 阅读优先级
**高**
理由：该工作以极快的速度（0.13秒）重建高保真投影-相机系统结果，克服了传统优化方法耗时的缺点，且代码和数据集已开源。对于从事增强现实、投影映射、逆渲染等方向的读者，具有很强的实用参考价值和复现吸引力。

</details>

<details>
<summary>Abstract</summary>

Projector-camera (ProCams) systems achieve active scene perception and controllable appearance manipulation via structured illumination, serving as a core infrastructure for spatial augmented reality, projection mapping, and surface reflectance acquisition. Existing inverse-rendering methods for ProCams deliver high-fidelity results but rely on time-consuming per-scene optimization, while mainstream feed-forward 3D reconstruction models produce baked appearance that cannot adapt to spatially varying projector illumination. To resolve this accuracy-efficiency trade-off, we propose FF-ProCams, a Feed-Forward 3D Gaussian inverse-rendering framework for ProCams. A hybrid Mamba2-Transformer encoder aggregates cross-view geometric and photometric cues from sparse multi-view observations, and lightweight heads predict a relightable Gaussian representation in a single forward pass. We further design a projector-aware differentiable renderer to synthesize camera observations under arbitrary active illumination and ProCams poses. To enable feed-forward training, we construct a large-scale synthetic ProCams dataset covering diverse object geometries and surface materials. Experiments show FF-ProCams achieves high-fidelity projector-aware rendering, generalizes to unseen patterns, and supports novel projector-camera poses. Using only 8 input views, it outperforms optimization-based baselines with 297 views while reducing test-time reconstruction to 0.13 seconds (a three-to-five-order-of-magnitude speedup). The code and data are available at https://github.com/CPREgroup/FF-ProCams/.

</details>

#### 2026-07-18 - TopoGS: Planar Reconstruction via Topology-aware 3D Gaussian Splatting

**Authors:** Shanshan Pan, Jiale Chen, Yilin Liu, Hui Huang
**Links:** [abs](https://arxiv.org/abs/2607.16838) - [pdf](https://arxiv.org/pdf/2607.16838)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** geometric reasoning, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TopoGS: 基于拓扑感知的3D高斯泼溅的平面重建
- 作者：Shanshan Pan, Jiale Chen, Yilin Liu, Hui Huang
- 出版日期：2026-07-18T14:27:49Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2607.16838) | [PDF](https://arxiv.org/pdf/2607.16838)

### 一句话总结
TopoGS通过显式集成平面约束和拓扑约束，解决了现有3D高斯泼溅方法中平面重建碎片化和边界不对齐的问题，在ScanNet++数据集上实现了最先进的性能。

### 研究问题
如何从原始图像中提取结构化的、参数化的3D平面重建，并克服现有方法因缺乏拓扑连接性导致的碎片化重建和边界不对齐问题。

### 核心思路/方法
1. 从多视图图像分割中提取全局2D拓扑关系。
2. 将高斯基元锚定到这些拓扑结构元素上，实现平面参数、渲染保真度和拓扑邻接性的联合优化。
3. 强制执行多视图一致性并结合拓扑约束，从而减少几何不对齐，产生连贯的结构化3D模型。

### 主要贡献
1. 提出首个在3D高斯泼溅框架中显式集成平面和拓扑约束的方法（TopoGS），用于连贯的3D重建。
2. 通过全局2D拓扑关系提取和锚定，实现了平面参数、渲染和拓扑的联合优化。
3. 在ScanNet++数据集上达到最先进性能，生成精确、拓扑正确且视觉保真的场景表示。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法针对3D高斯泼溅中平面重建拓扑缺失这一关键问题，提出了显式的拓扑约束联合优化方案，在主流数据集上取得SOTA，对结构化三维重建和场景编辑领域具有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Extracting structured, parametric 3D representations from raw images remains a fundamental challenge in computer vision and graphics. While recent advancements in the 3D Gaussian Splatting (3DGS) pipeline integrate planar primitives to yield compact and editable geometry, these approaches typically treat planes as isolated, discrete sets. This lack of topological connectivity hinders robust geometric reasoning, leading to fragmented reconstructions and misaligned boundaries that fall short of the precision for rigorous spatial analysis and professional design workflows. To address this, we introduce TopoGS, the first 3DGS framework to explicitly integrate both planar and topological constraints for coherent 3D reconstruction. Specifically, we extract global 2D topological relationships from multi-view image segmentations and anchor Gaussian primitives to these structural elements. This formulation enables the joint optimization of plane parameters, rendering fidelity, and topological adjacency. By enforcing strict multi-view consistency alongside these topological constraints, our method significantly mitigates geometric misalignments and produces connected, structured 3D models. Extensive evaluations on the ScanNet++ dataset demonstrate that TopoGS achieves state-of-the-art performance, providing a highly robust solution for generating accurate, topologically sound, and visually faithful scene representations.

</details>

#### 2026-07-16 - Online Neural Space Time Memory for Dynamic Novel View Synthesis

**Authors:** Baback Elmieh, Lynn Tsai, Zeman Li, Srinivas Kaza, Tiancheng Sun, Gabor Csapo, Ali Behrouz, Yuan Deng, Stephen Lombardi, Steven M. Seitz, Xuan Luo
**Links:** [abs](https://arxiv.org/abs/2607.15271) - [pdf](https://arxiv.org/pdf/2607.15271)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Online Neural Space Time Memory for Dynamic Novel View Synthesis
- 作者：Baback Elmieh, Lynn Tsai, Zeman Li, Srinivas Kaza, Tiancheng Sun, Gabor Csapo, Ali Behrouz, Yuan Deng, Stephen Lombardi, Steven M. Seitz, Xuan Luo
- 出版日期：2026-07-16
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2607.15271 | PDF：https://arxiv.org/pdf/2607.15271

### 一句话总结
本文提出了一种在线神经时空记忆方法，通过解耦记忆更新与应用的频率，并引入记忆损失和缓存策略，实现了动态场景的实时新颖视角合成。

### 研究问题
在线新颖视角合成中存在持久记忆（用于重建暂时遮挡区域）与实时约束之间的根本权衡：传统测试时训练模型需在每帧进行梯度更新，计算成本高且长上下文不稳定。

### 核心思路/方法
- 将记忆更新与记忆应用解耦：周期性更新记忆，但每帧都应用当前记忆。
- 应用记忆时使用跨视角注意力处理上一记忆状态与当前帧之间的形变。
- 引入两个关键机制：辅助记忆损失（强制内化场景历史）和记忆缓存策略（正则化当前权重，防止灾难性漂移）。

### 主要贡献
- 提出了解耦记忆更新频率的方法，使得在实时条件下仍能维持长期记忆。
- 设计了记忆损失和记忆缓存两种机制以锁定历史上下文。
- 在动态人体运动场景和分钟级记忆任务上实现了实时且当前最优的性能。

### 局限性
摘要未提供足够信息。未说明方法在极快速运动或严重遮挡场景下的性能边界，也未提及与其他非实时方法的定量比较细节。

### 阅读优先级
高。理由：该论文解决了动态场景在线新颖视角合成中的核心实时性难题，方法设计新颖（解耦更新与应用、双重记忆约束），且声称达到实时和SOTA性能，对新视角渲染领域的研究者具有较强的参考价值。

</details>

<details>
<summary>Abstract</summary>

Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes. The computational cost of heavy memory updates precludes real-time application and can lead to instability over long contexts. Given that memory updates are more demanding than memory application and video content is largely redundant, we propose to decouple the frequencies of these two processes. Our approach performs periodic memory updates while applying the memory on a per-frame basis, using cross-view attention to manage deformations between the prior memory state and the current frame. To lock in the historical context, we introduce two critical mechanisms: an auxiliary Memory Loss that forces persistent internalization of the scene, and a Memory Caching strategy that regularizes active weights against catastrophic drift. Our method demonstrates real-time, state-of-the-art performance on scenes with dynamic human motion as well as minute-scale online memorization.

</details>

#### 2026-07-16 - AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight

**Authors:** Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang
**Links:** [abs](https://arxiv.org/abs/2607.14997) - [pdf](https://arxiv.org/pdf/2607.14997)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight
- 作者：Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang
- 出版日期：2026-07-16T13:46:00Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.14997

### 一句话总结
AeroAct 是首个在真实世界四旋翼飞行中实例化的世界-动作模型，通过视频扩散Transformer预测动作轨迹，并在语言指令下实现平滑、动态可行的飞行控制。

### 研究问题
如何为语言控制的四旋翼飞行设计一个模型，使其能利用未来视觉信息作为密集监督信号，输出平滑且动态可行的控制参考，并解决现有方法（如离散动作或瞬时速度指令）对未来观测变化监督不足的问题。

### 核心思路/方法
- 提出行动中心的世界-动作模型（WAM），基于预训练视频扩散Transformer，从第一人称视觉历史、本体感知和语言指令中预测局部轨迹-动作块。
- 训练时使用未来第一人称帧作为密集后果监督；推理时直接解码动作，不生成未来视频。
- 构建基于DiffAero的数据生成管道，结合Isaac Lab和3D高斯泼溅渲染器，获取对齐的视觉、状态、语言和动态可行动作数据。
- 引入低成本手持采集设备，耦合相机观测与运动估计以重建飞行式第一人称轨迹，并通过自引导程序改善重叠轨迹块的时间一致性。

### 主要贡献
1. 首个在真实世界四旋翼飞行中实例化并演示的世界-动作模型（WAM）。
2. 提出利用未来视频帧作为密集监督信号的新训练范式，同时保持推理时无视频生成的高效性。
3. 开发了完整的数据管道（DiffAero、仿真渲染器和手持采集设备），支持大规模对齐数据获取。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工作聚焦于四旋翼飞行与语言指令结合的具体应用场景，创新点在于首次将WAM引入实际飞行任务，并解决了数据获取和训练监督问题。如果读者关注具身智能、无人机导航或视觉语言动作模型，则具有较高参考价值；但如果领域关联不紧密，则优先级可降为中。

</details>

<details>
<summary>Abstract</summary>

Language-conditioned quadrotor flight requires a policy to ground semantic goals, anticipate the visual consequences of ego-motion, and output control references that remain smooth and dynamically executable under rapidly changing first-person views. Existing aerial vision-language navigation and vision-language-action methods commonly use discrete actions, high-level waypoints, or instantaneous velocity commands, which provide limited supervision about how flight actions change future observations. We present AeroAct, an action-centered world-action model (WAM) for quadrotor navigation. To the best of our knowledge, AeroAct is the first WAM instantiated and demonstrated for real-world aerial flight. The model adapts a pretrained video diffusion Transformer to predict local trajectory-action chunks from egocentric visual history, proprioception, and language. Future first-person frames are used during training as dense consequence supervision, while deployment directly decodes actions without generating future video. To obtain aligned visual, state, language, and dynamically feasible action data, we build a DiffAero-based pipeline with complementary Isaac Lab and 3D Gaussian splatting renderers. We further introduce a low-cost handheld collection device that couples camera observations with motion estimates to recreate flight-like egocentric trajectories, and a self-guidance procedure that improves temporal consistency across overlapping trajectory chunks. Closed-loop simulation and real-world experiments show that temporal visual context improves target tracking and object-search performance, and that WAM-based policies can be executed on a physical quadrotor.

</details>

#### 2026-07-16 - JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting

**Authors:** Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao
**Links:** [abs](https://arxiv.org/abs/2607.14990) - [pdf](https://arxiv.org/pdf/2607.14990)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting
- 作者：Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao
- 出版日期：2026-07-16
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页：https://arxiv.org/abs/2607.14990；PDF：https://arxiv.org/pdf/2607.14990

### 一句话总结
JADE-GS通过事件相机提供的微秒级运动信号，在3D高斯泼溅框架中实现联合交替去模糊，并借助双向闭环机制将二维图像恢复器转化为几何感知预测器。

### 研究问题
快速相机运动导致的曝光期间模糊破坏了三维模型所需的清晰场景信息，而事件相机虽能捕获精确运动信号，但其在三维监督中存在两个障碍：1）物理先验和网络先验各有缺陷（漂移积累或边界失真）；2）现有流水线为单向，导致事件噪声或固定伪标签误差直接传递到几何重建中。

### 核心思路/方法
1. **像素自适应路由门**：融合互补的物理事件积分先验（保留边缘但漂移）和学习网络先验（恢复纹理但边界失真）。  
2. **双向闭环耦合**：将二维图像恢复器与3D高斯泼溅学生模型连接，通过解耦的多视角一致渲染图和基于物理的重模糊约束来正则化恢复器，将固定预处理器变为几何感知预测器。

### 主要贡献
1. 提出一种自适应门控机制，有效结合事件驱动的物理先验和深度学习先验进行去模糊。  
2. 设计双向闭环训练策略，使2D恢复器受3D几何约束，避免噪声与偏置单向传递。  
3. 在合成和真实基准上取得最佳感知质量（LPIPS和CLIP-IQA领先），PSNR和SSIM具有竞争力，训练时间约1小时、显存低于5 GB，且支持实时渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法解决了事件引导的3D场景重建中的核心缺陷（先验矛盾与单向误差），并在通用基准上获得感知质量领先，同时在单GPU上实现高效训练和实时渲染，对从事神经渲染、事件视觉或多传感器融合的研究者具有明显参考价值。

</details>

<details>
<summary>Abstract</summary>

When a camera moves fast during exposure, blur destroys the intra-exposure motion a 3D model needs to recover the sharp scene, while event cameras capture exactly this signal at microsecond resolution. Turning them into reliable 3D supervision faces two obstacles. First, the two restoration priors fail in opposite ways: physics-based event-integration priors preserve edges but accumulate drift; learned networks recover texture but distort boundaries. Second, existing pipelines run in one direction only, so raw event noise or the biases of fixed 2D pseudo-labels pass uncorrected into the geometry. JADE-GS addresses both: a pixel-adaptive routing gate fuses the complementary priors, and the resulting 2D restorer is coupled to a 3D Gaussian Splatting student in a bidirectional loop, where detached, multi-view-consistent renders and a physics-based reblurring constraint regularize the restorer, turning a fixed preprocessor into a geometry-aware predictor. Across synthetic and real benchmarks, JADE-GS attains the best perceptual quality, leading LPIPS and CLIP-IQA on both benchmarks with competitive PSNR and SSIM, and trainsin about one hour under 5 GB on a single consumer GPU while preserving real-time rendering.

</details>

#### 2026-07-16 - Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding

**Authors:** Amir Said, Randall Rauwendaal
**Links:** [abs](https://arxiv.org/abs/2607.14513) - [pdf](https://arxiv.org/pdf/2607.14513)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding
- 作者：Amir Said, Randall Rauwendaal
- 出版日期：2026-07-16
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2607.14513；PDF：https://arxiv.org/pdf/2607.14513

### 一句话总结
本文提出利用GPU硬件加速的纹理压缩方案（如BC1和BC7）来高效压缩3D高斯泼溅中的球谐系数，并通过局部分组与重排序提升压缩效率，同时保持并行解码与随机访问能力。

### 研究问题
如何在不牺牲GPU并行渲染性能的前提下，有效压缩3D高斯泼溅（3DGS）中由大量球谐系数导致的大内存占用问题。

### 核心思路/方法
- 利用专门设计用于GPU并行解码且具备硬件加速的纹理压缩格式（BC1、BC7），对3DGS的球谐颜色系数进行压缩。
- 通过将基元按颜色局部分组和重排序，使纹理压缩比直接应用于2D纹理更高效。
- 引入一种比特率控制策略，保留随机访问能力，从而支持大规模并行化而不影响渲染性能。

### 主要贡献
- 提出一种将GPU友好纹理压缩方案应用于3DGS球谐系数压缩的方法，利用硬件加速实现高效并行解码。
- 通过局部基元分组和重排序，显著提升纹理压缩效率。
- 设计比特率控制策略，在保持随机访问和并行化的前提下，实现可忽略或不可察觉的渲染质量损失（基于BC1和BC7格式的实验验证）。

### 局限性
摘要未提供足够信息。未说明不同场景下的压缩率范围、与其它3DGS压缩方法的定量比较，以及解码速度的具体指标。

### 阅读优先级
**高**  
理由：3DGS是当前新颖视图合成的前沿方法，其内存瓶颈是实际部署的关键问题。本文提出的利用GPU原生纹理压缩的思路具备高效、硬件兼容的实用潜力，且实验表明视觉质量损失可忽略，对实时应用和系统优化有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Techniques for modeling 3D scenes from image collections, such as 3D Gaussian Splatting (3DGS), are capable of generating high-quality novel views by leveraging graphics primitives with view-dependent appearance. In 3DGS, spherical harmonic (SH) are employed to model view-dependent color, resulting in a large number of SH coefficients per primitive and large memory requirements. While compression approaches have been proposed to mitigate this problem, they do not exploit the capabilities of modern Graphics Processing Units (GPUs) for parallel decoding and rendering. In this paper, we propose a method for compressing SH color coefficients using texture compression schemes specifically designed for efficient parallel GPU decoding and supported by dedicated hardware acceleration. It is shown that those methods can compress color coefficients more effectively than 2D textures by exploiting the fact that primitives can be locally grouped and reordered according to color. Furthermore, we introduce a bit-rate control strategy that preserves random access, enabling large-scale parallelization without compromising rendering performance. Experimental results using BC1 and BC7 texture compression formats show that GPU-based decompression can be achieved with negligible or imperceptible degradation in the visual quality of rendered 3DGS scenes.

</details>

#### 2026-07-16 - Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency

**Authors:** Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2607.14481) - [pdf](https://arxiv.org/pdf/2607.14481)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** structure from motion, SLAM, radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency
- 作者：Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis
- 出版日期：2026-07-16
- 分类：Neural Scene Representations & Rendering；3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.14481，PDF: https://arxiv.org/pdf/2607.14481

### 一句话总结
本文提出首个能够处理无序输入图像序列、提供即时反馈且保持全局一致性的3D高斯泼溅（3DGS）重建方法。

### 研究问题
如何在无序（非连续）图像捕获场景中，实现即时（无需等待全部输入）的3DGS重建，同时保证全局一致性。

### 核心思路/方法
1. **快速无序匹配**：利用视觉地点识别模型和共可见性图，实现无序图像序列的快速匹配，并高效找到高关联关键帧。
2. **局部快速重建**：结合GPU优化和精细的高斯基元放置，在辐射场重建中实现快速局部重建。
3. **基于聚类的闭环**：再次利用共可见性图，提出无需序列输入的聚类闭环方法，保证全局一致性。
4. **渐进式层级结构**：为处理大规模场景，设计渐进式层级方案，使方法可扩展至大型环境。

### 主要贡献
1. 首个为辐射场捕获提供即时反馈且保持全局一致性的方案。
2. 提出针对无序序列的快速匹配方法（重新利用视觉地点识别模型和共可见性图）。
3. 提出基于共可见性图的高效聚类闭环方法，无需依赖顺序输入。
4. 引入渐进式层级结构，使方法能够扩展到包含数千张图像的大场景。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作解决了3DGS实践中常见的无序输入与即时重建的核心矛盾，提出了完整的解决方案（匹配、闭环、可扩展性），且实验结果表明在多种数据集上达到良好视觉质量，对实时3D场景重建具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become the method of choice for reconstructing and real-time rendering of captured scenes. To capture a scene with good visual quality, continuous image sequences are usually combined with out-of-order shots for better scene coverage. Structure from motion can reconstruct such captures, but only after they are all available and often with high computational cost. Incremental reconstruction methods -- often derived from SLAM solutions -- provide immediate feedback, but cannot handle the out-of-order capture we require. We provide the first immediate feedback solution for such radiance field capture that provides global consistency. We first introduce a method for fast matching in out-of-order sequences, by repurposing visual place recognition models and a covisibility graph, and provide an efficient way to find highly connected keyframes, improving quality even for ordered sequences. We show how these steps -- together with GPU optimization and careful Gaussian primitive placement -- provide fast local reconstruction, in our challenging radiance field reconstruction case. We then introduce a novel cluster-based method, again using the covisibility graph, to provide efficient loop closure that does not require sequential input. Finally, to handle large scenes in our context, we introduce a progressive hierarchy that allows our method to scale to large environments, without compromising efficiency. Our results show we provide immediate feedback 3DGS reconstruction with good visual quality in several datasets, with up to thousands of input images.

</details>

#### 2026-07-15 - Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation

**Authors:** NVIDIA, :, Jiahui Huang, Jiawei Ren, Michal Tyszkiewicz, Bjoern Haefner, Michael Shelley, Xin Kang, Seung Wook Kim, Ning Xu, Qi Wu, Janick Martinez Esturo, Shengyu Huang, Nick Schneider, Laura Leal-Taixe, Zan Gojcic, Sanja Fidler
**Links:** [abs](https://arxiv.org/abs/2607.14203) - [pdf](https://arxiv.org/pdf/2607.14203)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, autonomous driving, driving scene, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation
- 作者：NVIDIA, Jiahui Huang, Jiawei Ren, Michal Tyszkiewicz, Bjoern Haefner, Michael Shelley, Xin Kang, Seung Wook Kim, Ning Xu, Qi Wu, Janick Martinez Esturo, Shengyu Huang, Nick Schneider, Laura Leal-Taixe, Zan Gojcic, Sanja Fidler
- 出版日期：2026-07-15
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）；Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：摘要链接 - https://arxiv.org/abs/2607.14203；PDF链接 - https://arxiv.org/pdf/2607.14203

### 一句话总结
Instant NuRec是一种前馈式神经网络重建模型，能够将短时多视角驾驶日志通过单次前向传播快速转化为可模拟的3D高斯场景。

### 研究问题
如何加速神经驾驶场景模拟的3D重建过程，避免现有方法（如NuRec）所需的逐场景调优和较慢的重建速度。

### 核心思路/方法
- 采用前馈式（feed-forward）神经网络架构，直接从校准的多视角相机输入中，一次前向生成包含静态与动态3D高斯层、天空立方体贴图以及每相机ISP校正的分层输出。
- 通过3DGUT原生支持非针孔相机模型。
- 模型深度集成于NuRec框架中，并兼容AlpaSim闭环仿真系统。

### 主要贡献
1. 提出Instant NuRec，实现驾驶场景的快速3D高斯重建（10-20秒多相机场景约1.5秒完成）。
2. 在Waymo Open Dataset上，PSNR比最强基线方法高出2.01 dB。
3. 支持非针孔相机模型，并输出分层场景表示（静态/动态层、天空、ISP校正）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该方法在自动驾驶仿真领域实现了显著的速度提升（单次前向传播）和性能增益（PSNR提升2.01 dB），且解决了现有方法需逐场景调优的痛点，对于从事神经重建、自动驾驶仿真的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

3D simulation platforms are critical for autonomous driving because they enable end-to-end policy evaluation, thereby reducing development costs and improving safety. In recent years, neural simulation has become predominant, with methods such as NuRec playing a central role; however, these methods remain relatively slow and typically require per-scene tuning. In this work, we present Instant NuRec, a feed-forward neural reconstruction model that turns a short multi-view driving log into a fully simulatable 3D Gaussian Splatting (3DGS) world in a single forward pass. The model accepts multi-view input from a calibrated camera rig and emits a layered output consisting of static and dynamic 3DGS layers, a sky cubemap, and per-camera ISP corrections, while providing native support for non-pinhole camera models via 3DGUT. It reconstructs a 10-20-second multi-camera scene in roughly 1.5 seconds and achieves a PSNR on the Waymo Open Dataset that is 2.01 dB above the strongest evaluated baseline. Instant NuRec is deeply integrated into NuRec and is compatible with AlpaSim for closed-loop simulation.

</details>

#### 2026-07-15 - Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting

**Authors:** Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann
**Links:** [abs](https://arxiv.org/abs/2607.13808) - [pdf](https://arxiv.org/pdf/2607.13808)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting
- 作者：Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann
- 出版日期：2026-07-15T13:12:31Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.13808

### 一句话总结
本文提出一种将高频纹理烘焙到紧凑纹理图集的快速渲染方法，通过解耦低频几何与高频外观，在保持高视觉保真度的同时将3DGS渲染速度提升至5倍，并支持60 FPS的4K实时渲染。

### 研究问题
如何克服3D高斯泼溅（3DGS）在基于哈希网格的外观参数化中片段渲染阶段的高计算开销，同时保持高频纹理细节和实时渲染速度。

### 核心思路/方法
1. 采用解耦的辐射表示：用2D surfels建模低频几何和视角相关外观特征，通过视角无关的空间哈希网格表示高频纹理。
2. 将空间哈希网格“烘焙”成一个紧凑的纹理图集（texture atlas）。
3. 引入稀疏性增强优化：惩罚半透明度和每个原语的衰减，从而激进地剪枝不重要的surfels，实现比先前工作更快、更稀疏的重建。
4. 利用几何稀疏性和高效GPU纹理映射来加速渲染。

### 主要贡献
- 提出一种解耦辐射表示，分离低频几何/视角相关外观与高频纹理，并采用烘焙纹理图集技术。
- 通过稀疏性增强优化显著减少surfels数量，实现更快的重建和更稀疏的表示。
- 相比3DGS获得高达5倍的渲染速度提升，同时保持最先进的视觉保真度，在消费级硬件上实现60 FPS的4K实时渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：论文显著提升了3DGS的渲染速度（最高5倍），且直接展示了4K 60 FPS的实时性能，在神经渲染领域具有实际应用潜力；方法结构清晰（解耦表示+烘焙纹理图集+稀疏优化），是近期工作方向中针对效率瓶颈的直观改进，值得深入参考。

</details>

<details>
<summary>Abstract</summary>

Recent extensions of 3D Gaussian Splatting (3DGS) capture fine color details using hash-grid-based appearance parameterization but incur high computational cost during fragment rendering. We introduce a decoupled radiance representation that models low-frequency geometry and view dependent appearance features with 2D surfels while representing high-frequency textures via a view-independent spatial hash grid that is baked into a compact texture atlas. By including sparsity-enhancing optimizations that penalize semi-transparency and per-primitive falloff, our method aggressively prunes insignificant surfels and achieves significantly faster and sparser reconstructions than prior work. Exploiting geometric sparsity and efficient GPU texture mapping, our approach achieves up to a fivefold speedup over 3DGS while preserving state-of-the-art visual fidelity, enabling real-time 4K rendering at 60 FPS on consumer hardware.

</details>

#### 2026-07-15 - Volumetric Inverse Rendering via Neural Radiative Transfer

**Authors:** Ntumba Elie Nsampi, Adarsh Djeacoumar, Hans-Peter Seidel, Tobias Ritschel, Thomas Leimkühler
**Links:** [abs](https://arxiv.org/abs/2607.13695) - [pdf](https://arxiv.org/pdf/2607.13695)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Volumetric Inverse Rendering via Neural Radiative Transfer  
- 作者：Ntumba Elie Nsampi, Adarsh Djeacoumar, Hans-Peter Seidel, Tobias Ritschel, Thomas Leimkühler  
- 出版日期：2026-07-15  
- 分类：Neural Scene Representations & Rendering  
- 链接：arXiv:2607.13695 (摘要: https://arxiv.org/abs/2607.13695, 论文: https://arxiv.org/pdf/2607.13695)

### 一句话总结
本文提出一种基于神经辐射传输的体积逆渲染方法，通过联合优化神经网络场表示的光学属性和光场，并利用辐射传输方程的局部微分形式作为残差目标来强制执行全局光照，从而实现从多视图图像中重建参与介质的散射、吸收和相位函数参数。

### 研究问题
如何从多视图图像中高效且准确地恢复参与介质的体光学属性（如散射、吸收和相位函数），同时兼顾物理完整的全局光照建模与通用神经优化的简便性。

### 核心思路/方法
- 将介质的光学属性和完整光场表示为**神经场**（neural fields）。  
- 通过**联合优化过程**同时估计光学参数和光场。  
- 利用**辐射传输方程（RTE）的局部微分形式**构建残差目标，以强制模型满足全局光照约束。  
- 沿主视角光线添加**体渲染项**以缓解低频偏差。  
- 最终从多视图图像中重建**空间变化、颜色分辨的散射、吸收和相位函数参数**。

### 主要贡献
- 提出一种**兼顾物理完整性与通用神经优化的体逆渲染框架**，无需依赖可微分随机光传输模拟的复杂算法。  
- 通过微分形式的RTE残差目标**实现全局光照建模**，同时利用体渲染项抑制低频偏差。  
- 支持从多视图图像重建**空间变化的散射、吸收和相位函数**，并可用于学习具有物理光学属性的生成模型。

### 局限性
摘要未提供任何关于实验局限性的信息。

### 阅读优先级
**中**。理由：该工作聚焦于体渲染中的逆问题，方法上结合了神经场与辐射传输方程，对从事神经渲染、体积光学属性重建或物理仿真领域的研究者有参考价值；但由于摘要未提供实验对比或性能数据，且属于较新的预印本（出版于2026年），实用性尚待验证。非相关领域读者可暂缓阅读。

</details>

<details>
<summary>Abstract</summary>

Volumetric inverse rendering seeks to recover the optical properties of participating media from images. Existing approaches either rely on differentiable stochastic light transport simulation, which require substantial algorithmic effort, or use simplified models that fail to capture global illumination. We propose a formulation that reconciles physically complete light transport with general-purpose neural optimization. The optical properties of the medium and the full light field are represented as neural fields and estimated through a joint optimization process. Global illumination is enforced via a residual objective derived from the Radiative Transfer Equation in local differential form, complemented by a volume rendering term along primary viewing rays to mitigate \rev{low-frequency} bias. We demonstrate reconstruction of spatially varying, color-resolved scattering, absorption, and phase function parameters from multi-view images. Beyond reconstruction, the same framework supports learning generative models of participating media with physical optical properties under global illumination.

</details>

#### 2026-07-15 - FreeLit: Paired-Free Indoor Relighting via Physics-Guided Diffusion

**Authors:** Chi-En Yen, Duy-Khanh Ngo, Wen-Wei Tang, Huu-Phu Do, Wen-Hsiao Peng, Ching-Chun Huang
**Links:** [abs](https://arxiv.org/abs/2607.13656) - [pdf](https://arxiv.org/pdf/2607.13656)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FreeLit: Paired-Free Indoor Relighting via Physics-Guided Diffusion
- 作者：Chi-En Yen, Duy-Khanh Ngo, Wen-Wei Tang, Huu-Phu Do, Wen-Hsiao Peng, Ching-Chun Huang
- 出版日期：2026-07-15
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2607.13656 | PDF: https://arxiv.org/pdf/2607.13656

### 一句话总结
FreeLit 提出了一种无需配对训练数据的室内场景重打光框架，通过物理引导的扩散模型和内在稳定性策略，实现对光源位置、颜色和强度的可控调整，尤其在低照度场景中表现鲁棒。

### 研究问题
如何在不依赖昂贵的配对多光照数据集的情况下，实现对室内场景的可控重打光（包括光源位置、颜色和强度的显式操控），并提升在低照度等挑战条件中的稳定性和物理一致性。

### 核心思路/方法
1. **无配对框架**：利用物理先验构建照明先验，从内在场景属性生成结构化的光照图（lightmap）和伪重打光图像。
2. **物理引导扩散**：以上述光照图和伪图像作为引导信号，驱动扩散模型合成最终重打光结果。
3. **重打光引导的内在稳定性策略**：针对内在属性估计在低光场景中的不稳定性，通过结构感知蒸馏和一致性约束，强制保持反射率在光照变化下的不变性。
4. **可控制性评估指标**：提出新的评价指标，量化重打光结果与用户指定光照颜色和强度的对齐程度。

### 主要贡献
- 提出了无需配对监督的可控室内重打光框架 FreeLit。
- 设计了物理引导的扩散合成流程，利用内在属性构建照明先验。
- 提出重打光引导的内在稳定化策略，提升低光场景下内在估计的鲁棒性。
- 引入面向可控性的评估指标，用以衡量与用户光照参数的一致性。

### 局限性
摘要未提供足够信息，因此未说明实验中的具体局限性（如计算开销、对极端几何的适应性等）。

### 阅读优先级
中  
理由：该方法针对室内重打光中配对数据稀缺和低光鲁棒性问题，提出了一套无监督且物理约束的解决方案，对从事图像合成、神经渲染或照明估计的研究者有一定参考价值。但摘要未详细介绍与现有方法的定量对比或消融实验细节，需阅读全文验证其有效性。若您关注扩散模型与物理先验结合的重打光方向，可优先阅读。

</details>

<details>
<summary>Abstract</summary>

Image-based indoor scene relighting remains challenging due to the complex interplay between cluttered geometry and local illumination, requiring precise modeling of light position, color, and intensity. Existing data-driven methods implicitly learn this relationship via paired multi-illumination datasets. Nevertheless, this data is costly and fails to scale, which is essential for accurate light-source-level control. Conversely, inverse-rendering methods reduce the data dependency by incorporating physical priors; however, they lack the robustness of intrinsic estimation in challenging conditions. In this paper, we present FreeLit, a paired-free framework for controllable indoor relighting that explicitly manipulates light-source location, color, and intensity. Instead of relying on paired supervision, we construct a physics-guided illumination prior from intrinsic scene properties, generating a structured lightmap along with a pseudo-relit image to guide diffusion-based synthesis. To address instability in intrinsic estimation, especially in low-light scenes, we introduce a relighting-guided intrinsic stabilization strategy that enforces illumination-invariant reflectance through structure-aware distillation and consistency constraints. Furthermore, we propose controllability-oriented evaluation metrics to quantify alignment with user-specified illumination color and intensity. Experimental results demonstrate that FreeLit achieves stable, physically consistent, and controllable relighting, with improved robustness in low-light indoor scenes, without requiring paired supervision.

</details>

#### 2026-07-15 - Learning Physics-Guided Residual Dynamics for Deformable Object Simulation

**Authors:** Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali, Svetlana Lazebnik, Yunzhu Li
**Links:** [abs](https://arxiv.org/abs/2607.13451) - [pdf](https://arxiv.org/pdf/2607.13451)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Physics-Guided Residual Dynamics for Deformable Object Simulation
- 作者：Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali, Svetlana Lazebnik, Yunzhu Li
- 出版日期：2026-07-15T05:15:43Z
- 分类：主要类别：神经场景表示与渲染；次要类别：具身/机器人/AR应用
- 链接：摘要：https://arxiv.org/abs/2607.13451 ；PDF：https://arxiv.org/pdf/2607.13451

### 一句话总结
提出物理引导残差动力学（PGRD）混合框架，将可优化的弹簧-质点物理模拟器与学习残差校正的神经网络结合，在真实世界可变形物体模拟中取得比纯物理或纯学习方法更准确的结果。

### 研究问题
如何准确模拟可变形物体的动力学行为，克服纯物理方法精度不足和纯学习方法泛化性弱的局限。

### 核心思路/方法
1. **混合框架**：以可优化的弹簧-质点模拟器作为基础物理骨干，叠加一个学习残差校正的神经网络。
2. **速度基础公式**：采用基于速度的公式确保模拟稳定性。
3. **滑动窗口Transformer**：使用滑动窗口Transformer架构捕捉时间依赖性。
4. **应用扩展**：将PGRD用于基于模型预测控制的操控规划（包括语言条件设置下的目标图像生成），以及通过3D高斯喷溅进行动作条件视频预测的交互式模拟。

### 主要贡献
- 提出了PGRD混合模拟框架，融合物理模拟与学习残差校正。
- 在多种真实世界可变形物体上展示了优于纯物理和纯学习方法的准确性。
- 展示了PGRD在操控规划（含语言条件）和交互式模拟两个应用中的实用价值。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对机器人操控中可变形物体模拟这一关键难题，提出了新颖且实用的混合方法，并在真实数据上验证了有效性，同时展示了在语言条件操控等前沿应用场景的潜力。

</details>

<details>
<summary>Abstract</summary>

Simulating deformable objects is essential for a wide range of robotic manipulation applications, yet accurately predicting their dynamics remains challenging. We propose Physics-Guided Residual Dynamics (PGRD), a hybrid simulation framework that combines the advantages of physics-based and learning-based approaches. Specifically, PGRD combines an optimizable spring-mass simulator as a backbone with a learned neural network that predicts residual corrections to the physics-based predictions. We adopt a velocity-based formulation to ensure stable simulation and a sliding-window transformer architecture to capture temporal dependencies. We show that PGRD produces more accurate results than both purely physics-based and learning-based methods on a set of diverse real-world deformable objects. We further demonstrate the utility of PGRD in two applications: manipulation planning via Model Predictive Control, including a language-conditioned setting with a generated goal image; and interactive simulation via action-conditioned video prediction by 3D Gaussian Splatting.

</details>

#### 2026-07-14 - Differentiable Polarized Path Tracing

**Authors:** Pramod Rao, Jérémy Riviere, Xilong Zhou, Abhijeet Ghosh, Abhimitra Meka, Thabo Beeler, Marc Habermann, Christian Theobalt, Delio Vicini
**Links:** [abs](https://arxiv.org/abs/2607.13265) - [pdf](https://arxiv.org/pdf/2607.13265)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, inverse rendering, differentiable rendering, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Differentiable Polarized Path Tracing  
- 作者：Pramod Rao, Jérémy Riviere, Xilong Zhou, Abhijeet Ghosh, Abhimitra Meka, Thabo Beeler, Marc Habermann, Christian Theobalt, Delio Vicini  
- 出版日期：2026-07-14  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2607.13265  

### 一句话总结  
本文提出一种基于偏振感知的可微分路径追踪方法，通过结合路径回放与局部缓存估计无偏梯度，解决了偏振算子导致的数值不稳定问题，从而支持复杂场景下的材质与光照逆渲染。

### 研究问题  
现有基于物理的可微分渲染方法大多忽略偏振信息，而偏振线索能约束场景几何与材质属性，但偏振算子（如线性偏振器、漫反射）的秩亏特性破坏了标准梯度估计器（如路径回放反向传播）的可逆性假设，导致数值不稳定。

### 核心思路/方法  
- 采用基于Mueller-Stokes微分的偏振光前向仿真方法。  
- 在反向传播中，通过路径回放与局部缓存相结合的方案估计无偏梯度，避免偏振算子秩亏导致的算法失效，实现稳定优化。

### 主要贡献  
1. 提出一种鲁棒、偏振感知的可微分路径追踪算法。  
2. 解决了偏振光反向扩散中梯度估计的数值不稳定问题。  
3. 扩展了基于物理的逆渲染在复杂材质与光照优化中的适用性。

### 局限性  
摘要未提供足够信息（如实验设置、计算开销、对场景或偏振类型的限制等）。

### 阅读优先级  
**高**。理由：该工作填补了可微分渲染中偏振信息利用的空白，针对关键数值稳定性问题提出新方案，对逆渲染领域（如3D重建、材质估计）具有潜在实用价值，且方法描述清晰。

</details>

<details>
<summary>Abstract</summary>

Physically based differentiable rendering has proven to be a powerful tool for inverse rendering problems (e.g., 3D reconstruction, reflectance estimation, lighting estimation). However, most existing methods operate solely on radiometric intensity, discarding valuable polarization cues that constrain scene geometry and material properties. While forward simulation of polarized light is well-defined via Mueller-Stokes calculus, extending reverse-mode differentiation to this domain presents significant challenges. The rank-deficient nature of common polarimetric operators, such as linear polarizers and diffuse reflections, violates the invertibility assumptions of standard gradient estimators like path replay backpropagation and results in numerical instability. We address this by proposing a robust, polarization-aware differentiable path tracing method. Our approach estimates unbiased gradients through a combination of path replay and local caching. This formulation enables efficient and stable optimization of material and lighting parameters in complex scenes, broadening the applicability of physically based inverse rendering. Project page: https://vcai.mpi-inf.mpg.de/projects/DPPT/

</details>

#### 2026-07-14 - Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation

**Authors:** Lingxiao Guo, Huanyu Li, Guanya Shi
**Links:** [abs](https://arxiv.org/abs/2607.13154) - [pdf](https://arxiv.org/pdf/2607.13154)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation
- 作者：Lingxiao Guo, Huanyu Li, Guanya Shi
- 出版日期：2026-07-14
- 分类：Neural Scene Representations & Rendering (主要), Embodied / Robotics / AR Applications (次要)
- 链接：摘要: https://arxiv.org/abs/2607.13154 ; PDF: https://arxiv.org/pdf/2607.13154

### 一句话总结
本文提出WANDA，一个从单次人类演示中合成大规模训练数据的数据引擎，通过重建场景与轨迹、重排交互片段、纠正状态扩展和跨环境合成，使机器人能从一次演示学习具备空间泛化、长时程鲁棒性和跨环境泛化的开放世界移动操作策略。

### 研究问题
如何用最少的人类演示数据（单次演示）为开放世界移动操作策略提供足够量的训练数据，以实现空间泛化、长时程鲁棒性和跨场景泛化，同时避免传统遥操作和UMI方法的高人力成本。

### 核心思路/方法
1. **场景与轨迹重建**：从单次RGBD观测中重建背景高斯溅射（Gaussian splats）和机器人-物体交互轨迹，作为后续规划和渲染的世界基质。
2. **轨迹重排与扩展**：将交互片段按多种空间配置重新排列，利用全身运动规划将它们连接成新轨迹；并通过纠正状态扩展（Corrective State Expansion）增加机器人和物体在不同移动操作阶段的状态多样性。
3. **跨环境合成**：基于日常照片生成多样化的3D世界，在此类世界中合成新轨迹，解锁跨环境泛化能力。
4. **观测合成**：通过将渲染的机器人/物体网格与高斯溅射背景合成，生成逼真的观测数据。

### 主要贡献
1. 提出WANDA数据引擎，仅需一次人类演示即可大规模合成训练数据，显著降低数据收集成本。
2. 方法在仿真和真实任务中验证，使策略达到长时程鲁棒性、广泛空间泛化和跨环境泛化。
3. 自然支持跨形态数据生成，通过零样本部署到不同形态的移动操作机器人得到验证。

### 局限性
摘要未提供足够信息。例如：未说明在不同场景中的具体性能指标、真实世界实验的失败案例、计算开销或与基线方法的量化对比等。

### 阅读优先级
**高**
理由：该论文针对开放世界移动操作中的数据瓶颈问题，提出从单次演示合成大量数据的创新方法，同时涉及神经场景表示、机器人学习和跨场景泛化等前沿领域，对低数据驱动机器人研究具有重要启发。结果在仿真和真实任务中均得到验证，且展示了跨形态迁移能力，实用性较强。

</details>

<details>
<summary>Abstract</summary>

Learning open-world mobile manipulation policies requires vast data to achieve spatial generalization, long-horizon robustness, and scene generalization. Current prevailing data collection paradigms, teleoperation and UMI, demand prohibitive human effort and cost at scale. To scale beyond the limits of manual data collection, we seek to maximize the value of each human demonstration by scalable data generation. To this end, we introduce WANDA: learning open-World mobile mANipulation from one demonstration via a synthetic DAta engine. WANDA first reconstructs background Gaussian splats and robot-object interaction trajectories from source RGBD observations, as a world substrate for later planning and rendering. It then rearranges contact-rich robot-object interaction segments into extensive spatial configurations, utilizing whole-body motion planning to chain them into new trajectories. To enhance long-horizon robustness, it applies Corrective State Expansion to increase the robot and object state diversity at different stages of mobile manipulation. To unlock cross-environment generalization, trajectories are synthesized on diverse generated 3D worlds from everyday photos. Furthermore, we synthesize photo-realistic observations by compositing rendered robot and object meshes with Gaussian splatting backgrounds. We evaluate our approach on extensive simulation and real-world tasks in various scenes. Experiments show that policies trained with WANDA achieve long-horizon robustness, broad spatial generalization and cross-environment generalization from one real demonstration. Moreover, WANDA naturally supports cross-embodiment data generation, validated by zero-shot deployment on another mobile manipulator with a distinct morphology.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-20 - When 2D Cues Fail: Improving Image Manipulation Localization with Reliable 3D Geometry

**Authors:** Guofeng Yu, Zhiqing Guo, Dan Ma, Gaobo Yang
**Links:** [abs](https://arxiv.org/abs/2607.18040) - [pdf](https://arxiv.org/pdf/2607.18040)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reasoning, manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：When 2D Cues Fail: Improving Image Manipulation Localization with Reliable 3D Geometry
- 作者：Guofeng Yu, Zhiqing Guo, Dan Ma, Gaobo Yang
- 出版日期：2026-07-20
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.18040

### 一句话总结
本文提出一种利用可靠3D几何线索（深度、表面法向）来增强图像篡改定位性能的框架GFrame，以解决纯2D线索在篡改区域与外观高度融合时失效的问题。

### 研究问题
当篡改区域在2D外观上与周围环境高度一致时，传统基于低层伪影、噪声痕迹、语义不一致等2D取证线索的图像篡改定位方法判别能力下降，需要引入几何推理来提供互补证据。

### 核心思路/方法
1. 利用单目重建提取辅助几何线索：深度图和表面法向图。
2. 考虑到被篡改图像中重建的几何信息天然带有噪声，直接作为证据不可靠，因此先估计这些几何线索的可靠性，再选择性使用。
3. 设计一个几何感知框架GFrame，将可靠的几何线索与RGB特征融合，并进行跨尺度传播以改善细粒度定位。

### 主要贡献
1. 指出纯2D线索在篡改区域外观融合良好时的局限，并引入可靠3D几何线索作为互补取证证据。
2. 提出GFrame框架，通过估计并选择性利用深度和表面法向的可靠性，实现更鲁棒的篡改定位。
3. 在有限预算下实现优秀性能，并计划公开代码。

### 局限性
摘要未提供足够信息，无法确认方法在复杂场景、计算成本、不同篡改类型上的具体表现或失败模式。

### 阅读优先级
中
理由：该方法属于图像取证领域的实用创新，思路明确（引入3D几何推理），但摘要未给出详尽的实验对比或代码开源时间，建议在需要解决2D线索失败场景时再深入阅读。

</details>

<details>
<summary>Abstract</summary>

Existing image manipulation localization (IML) methods rely heavily on 2D forensic cues, such as low-level artifacts, noise traces, and semantic inconsistencies in the manipulated image. While effective in many cases, these cues become much less discriminative when manipulated regions are well blended with their surrounding context in appearance. In such cases, a manipulated region may remain locally appearance-consistent, but still violate the geometric structure of the surrounding scene. This limitation motivates us to go beyond purely 2D evidence and introduce geometric reasoning into IML. To this end, we leverage monocular reconstruction to obtain auxiliary geometric cues, including depth and surface normals. However, a key challenge lies in the fact that reconstructed geometry on manipulated images is inherently noisy and cannot be used naively. Rather than treating depth and normals as direct evidence, we estimate their reliability and exploit them selectively for localization. Based on this principle, we design a geometry-aware framework (GFrame) that fuses reliable geometric cues with RGB features and propagates them across scales to improve fine-grained localization. Extensive experiments show that the proposed method achieves excellent performance under limited budget constraints. These results indicate that reliable 3D geometry provides complementary forensic evidence beyond traditional 2D cues for IML. Related code will be released.

</details>

#### 2026-07-20 - Lifelong Localization in Dynamic Indoor Environments Combining Odometry with Sparse Distance Sampling

**Authors:** Michael M. Bilevich, Tomer Buber, Dan Halperin
**Links:** [abs](https://arxiv.org/abs/2607.17852) - [pdf](https://arxiv.org/pdf/2607.17852)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, rendering, robot navigation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lifelong Localization in Dynamic Indoor Environments Combining Odometry with Sparse Distance Sampling
- 作者：Michael M. Bilevich, Tomer Buber, Dan Halperin
- 出版日期：2026-07-20T11:46:57Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.17852

### 一句话总结
论文提出了一种结合里程计与稀疏距离采样的鲁棒终身定位框架，可在动态室内环境中实现高效、可证明收敛的机器人定位，仅需少量距离样本即可达到类似SLAM的定位效果。

### 研究问题
如何在动态室内环境中实现机器人终身鲁棒定位，尤其是在预建地图因动态障碍物变得不准确，以及机器人可能被“绑架”（kidnapped robot problem）的情况下。

### 核心思路/方法
1. **稀疏距离采样提供鲁棒先验**：利用机器人获取的稀疏距离样本（如仅16个距离值）作为初始位置先验，可实时解决机器人绑架问题（存在对称性歧义时除外）。
2. **融合里程计与先验**：随时间将距离采样提供的先验与里程计数据融合，逐步收敛到机器人真实位姿。
3. **应对动态障碍**：基于真实世界记录数据的洞察，设计方法处理动态障碍物对定位的影响。
4. **理论基础**：证明在静态环境中方法可确保收敛到真实位姿；在动态环境中，若变化规律被正确学习，同样可保证收敛。

### 主要贡献
1. 提出一种终身定位框架，仅需稀疏距离采样（而非完整LiDAR范围），在传感器成本、隐私、存储和传输带宽方面具有优势。
2. 方法可实时解决机器人绑架问题，并在动态环境中保持鲁棒性。
3. 通过理论证明和真实世界实验验证，该方法在静态和动态环境中均能收敛到真实位姿，定位效果与SLAM相当。

### 局限性
摘要未提供具体局限性信息，但可推断：
- 动态环境中的收敛保证依赖于“变化规律被正确学习”，即需要准确建模动态障碍物的行为模式，这在实际应用中可能存在挑战。
- 绑架问题仅能“up to symmetries”（即对称性歧义可能无法完全消除），摘要未明确说明如何解决对称性场景。
- 实验仅在特定真实室内环境中验证，未提及跨场景泛化性。

### 阅读优先级
**高**
理由：该工作提出了新颖的稀疏距离采样定位方法，兼具理论收敛保证和实际应用优势（低传感器成本、隐私友好），且解决了动态环境下的终身定位难题，对机器人领域研究人员具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Localization is a key task in robot navigation, and many techniques exist for it. In many plausible scenarios, a robot might face unforeseen, dynamic obstacles, rendering any pre-determined map inaccurate for localization. In this work, we propose a robust lifelong localization framework in dynamic planar indoor environments, using the robot's odometry and sparse distance sampling. We demonstrate how distance samples can be used to provide a robust prior on the robot's location. This technique can solve the kidnapped robot problem in real time, up to symmetries. Based on insights from real-world recorded data, we also account for dynamic obstacles. We then fuse this prior, over time, with the odometry to converge to the robot's location. A central property of our method is that it provably converges to the robot's ground truth pose even in large indoor environments when the environment is static. We further show that this guarantee also holds in dynamic environments, as long as the nature of those changes has been correctly learned. We demonstrate the effectiveness of our approach in different real-world indoor environments. In particular, we achieve a localization comparable to SLAM with merely a few (sixteen) distance samples, as opposed to the full LiDAR range. Sufficing with only sparse distance sampling is advantageous in terms of sensor cost, privacy, storage space, and transmission bandwidth.

</details>

#### 2026-07-20 - Attention from Above: A Multimodal Model for Drone-Based Object Localization

**Authors:** Hyun-Ki Jung
**Links:** [abs](https://arxiv.org/abs/2607.17669) - [pdf](https://arxiv.org/pdf/2607.17669)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Attention from Above: A Multimodal Model for Drone-Based Object Localization（来自上方的注意力：面向无人机目标定位的多模态模型）
- 作者：Hyun-Ki Jung
- 出版日期：2026-07-20
- 分类：Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：论文摘要链接: https://arxiv.org/abs/2607.17669 ；PDF链接: https://arxiv.org/pdf/2607.17669

### 一句话总结
本文基于YOLO-World框架，通过引入注意力机制的A2C2f层替换原有C2f层，提出了一种改进的多模态无人机目标检测模型，在VisDrone数据集上显著提升了检测精度，尤其是对小目标的检测性能。

### 研究问题
如何改进基于多模态（文本提示+视觉）的无人机目标检测模型，以提升对小目标或边界清晰目标的检测准确性。

### 核心思路/方法
1. **基础框架**：采用YOLO-World作为基线多模态检测模型。
2. **关键改进**：将YOLOv8骨干网络中的C2f层替换为基于注意力机制的A2C2f层。
3. **设计目标**：通过注意力机制和并行处理结构，增强模型对局部特征的表示能力，特别针对小目标或具有清晰边界的对象。
4. **验证实验**：在VisDrone数据集上进行对比实验，与原始YOLO-World模型比较。

### 主要贡献
1. 提出了一种基于注意力机制的新型模块A2C2f，有效提升了多模态检测模型对局部特征的捕捉能力。
2. 在VisDrone数据集上验证了所提模型的有效性：相比原始YOLO-World，检测精度（precision）从43.0%提升至45.1%，召回率（recall）从32.8%升至35.0%，F1分数从37.2%升至39.4%，mAP@0.5从32.5%升至35.2%，mAP@0.5-0.95从18.5%升至19.9%。
3. 为基于无人机的图像和视频目标检测应用提供了一种更精确的解决方案。

### 局限性
摘要未提供足够信息。具体局限性（如模型的计算成本、推理速度、对复杂场景的泛化能力、多模态融合的失败案例等）未在摘要中说明。

### 阅读优先级
**高**
理由：该论文针对无人机场景下小目标检测这一实际且具有挑战性的问题，在近期主流模型YOLO-World基础上进行了明确的可量化改进（所有评估指标均有提升），且实验基于公开数据集VisDrone。方向契合无人机、机器人和多模态应用领域，对于关注轻量化或嵌入式检测的研究者具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Drone-based object detection technology has advanced rapidly, becoming increasingly sophisticated and efficient. Recently, research trends have expanded beyond the detection of predefined objects toward the identification of specified target objects. For example, desired targets can be specified through textual prompts, enabling accurate detection of objects of interest. To address this demand, this paper proposes an efficient multimodal-based object detection model aimed at improving small object detection performance. The proposed method is built upon the YOLO-World framework and replaces the C2f layers used in the YOLOv8 backbone with attention-based A2C2f layers. This modification enables more precise representation of local features, particularly for small objects or objects with well-defined boundaries. In addition, the incorporation of attention mechanisms and parallel processing structures significantly enhances the model's computational accuracy. Comparative experiments conducted on the VisDrone dataset demonstrate that the proposed model outperforms the original YOLO-World model. Specifically, precision increases from 43.0% to 45.1%, recall from 32.8% to 35.0%, the F1 score from 37.2% to 39.4%, mAP@0.5 from 32.5% to 35.2%, and mAP@0.5-0.95 from 18.5% to 19.9%, confirming a substantial improvement in detection accuracy. These results verify that the proposed approach provides an effective and highly accurate solution for object detection in drone-based image and video application environments.

</details>

#### 2026-07-20 - GeoWorldAD: Geometry World Action Model for Autonomous Driving

**Authors:** Songyan Zhang, Jinyuan Tian, Hanbing Li, Daqi Liu, Hao Chen, Wenhui Huang, Fang Li, Guang Chen, Hangjun Ye, Long Chen, Kuiyuan Yang, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2607.17521) - [pdf](https://arxiv.org/pdf/2607.17521)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** dynamic 3D, autonomous driving, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoWorldAD: Geometry World Action Model for Autonomous Driving  
- 作者：Songyan Zhang, Jinyuan Tian, Hanbing Li, Daqi Liu, Hao Chen, Wenhui Huang, Fang Li, Guang Chen, Hangjun Ye, Long Chen, Kuiyuan Yang, Chen Lv  
- 出版日期：2026-07-20T03:56:07Z  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.17521  

### 一句话总结
GeoWorldAD提出了一种基于几何世界建模的自动驾驶动作模型，通过引入自车对齐的3D几何线索和潜在未来几何令牌，实现更安全、更高效的轨迹规划。

### 研究问题
自动驾驶在动态3D环境中需要兼顾安全与效率的规划决策。现有视觉/视频动作模型往往缺乏显式的几何基础和未来感知的空间引导，难以在避免碰撞与保持行驶进度之间取得平衡。

### 核心思路/方法
- **显式几何锚定**：将轨迹规划嵌入到自车对齐的3D空间中，利用当前几何信息提供空间约束。  
- **潜在未来几何建模**：通过隐式未来几何令牌预测短时场景演化，包括周围代理和自车自由空间的变化，以减少过于保守的决策。  
- **渐进式轨迹优化**：利用多尺度的当前几何和潜在未来几何，通过迭代细化逐步优化轨迹。

### 主要贡献
- 提出了GeoWorldAD框架，将显式3D几何基础与未来几何世界建模相结合。  
- 在NAVSIM v1和v2基准上取得了最先进的性能，验证了该方法对安全与效率的平衡效果。  
- 强调了利用几何线索（当前与未来）对于自动驾驶规划的重要性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：论文提出了一种新颖的几何世界动作模型，在自动驾驶规划中同时考虑当前与未来几何线索，并在标准基准上取得领先性能，对安全性提升和决策保守问题具有明确贡献。尽管实验细节有限，其方法思路对相关领域研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous driving requires both safe and efficient planning decisions in dynamic 3D environments. Although recent Vision/Video-Action models learn policies directly from visual observations and scale well with advances in vision transformers and large-scale training data, they often lack explicit geometric grounding and future-aware spatial guidance, limiting their ability to balance collision avoidance and driving progress. In this work, we propose GeoWorldAD, a geometry world action model that grounds trajectory planning in ego-aligned 3D space and anticipates short-horizon scene evolution with latent future geometry tokens. Present geometry provides essential spatial constraints for safe planning, while future geometry reveals how surrounding agents and ego-centric free space may evolve, reducing overly conservative decisions without sacrificing safety. To efficiently exploit these geometric cues, GeoWorldAD progressively aggregates multi-scale present geometry and latent future geometry through iterative trajectory refinement. Experiments on NAVSIM v1 and v2 demonstrate state-of-the-art performance, highlighting the effectiveness of explicit 3D geometry grounding and future geometry world modeling for safe and efficient autonomous driving.

</details>

#### 2026-07-18 - A BIM-enabled, Agent-based Discrete-event Simulation Platform for Robotic Studies: A Method based on Graph Theory

**Authors:** Ping Xu, Xinghua Gao
**Links:** [abs](https://arxiv.org/abs/2607.16920) - [pdf](https://arxiv.org/pdf/2607.16920)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** simultaneous localization and mapping, SLAM, robot navigation, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A BIM-enabled, Agent-based Discrete-event Simulation Platform for Robotic Studies: A Method based on Graph Theory
- 作者：Ping Xu, Xinghua Gao
- 出版日期：2026-07-18
- 分类：Embodied / Robotics / AR Applications；3D Reconstruction & Multi-view Geometry
- 链接：摘要：https://arxiv.org/abs/2607.16920；PDF：https://arxiv.org/pdf/2607.16920

### 一句话总结
该研究提出一个基于BIM、基于图论的智能体离散事件仿真平台，用于支持室内机器人进行知识驱动的导航与操作规划，通过将环境离散化为网格并映射为图节点，利用图论算法实现高效无碰撞导航。

### 研究问题
如何利用建筑信息模型（BIM）的丰富语义和几何信息，弥补现有导航方法对室内环境理解不足的问题，从而实现室内机器人在复杂设施管理任务（如定位和维修泄漏管道）中的知识驱动导航与操作规划。

### 核心思路/方法
1. 将室内环境离散化为网格单元，并将这些单元映射为图节点。
2. 根据与建筑元素的空间关系，将节点分类为目标节点、障碍节点或常规节点。
3. 为连接相邻节点的边分配遍历成本，使图论算法能够计算高效且无碰撞的导航路径。
4. 采用基于智能体的离散事件仿真框架，集成BIM信息，支持虚拟评估。

### 主要贡献
- 提出一种BIM赋能的、基于图论的室内机器人仿真平台，将BIM信息与机器人导航和操作规划结合。
- 通过网格离散化和图节点分类方法，实现了高效且无碰撞的导航。
- 识别并缓解了粗糙离散化造成的目标占用单元与障碍占用单元重叠的问题，通过网格细化提高了空间精度和路径可行性。
- 支持在部署前对机器人操作进行虚拟评估，为BIM赋能的设施管理机器人系统奠定基础。

### 局限性
- 摘要指出关键局限：粗糙离散化会导致目标占用单元与障碍占用单元重叠问题，虽通过网格细化缓解，但该处理可能带来计算或精度上的折中，摘要未提供具体权衡细节。
- 摘要未提供场景规模、计算效率、实验对比等具体信息。

### 阅读优先级
中。理由：该研究针对室内机器人复杂任务场景，提出BIM与图论结合的方法，思路清晰且有仿真验证，对建筑机器人应用有一定参考价值。但摘要未提供详细实验数据和性能指标，且方法本身的创新性（网格+图）较为常规，需阅读全文评估实际效果和局限性。

</details>

<details>
<summary>Abstract</summary>

Indoor robots are increasingly employed for facility management tasks such as cleaning and inspection. These applications primarily rely on navigation and can be effectively supported by predefined routes or perception-driven Simultaneous Localization and Mapping (SLAM) techniques. However, more complex tasks, such as locating and repairing leaking pipes, require not only navigation but also access to building information, including the location, geometry, material, and operational attributes of components. Existing navigation approaches provide only limited environmental understanding and cannot readily supply such information. In contrast, Building Information Modeling (BIM) contains rich geometric, semantic, and operational information that remains largely underutilized in robotic applications. This study proposes a BIM-enabled, agent-based simulation platform for knowledge-driven indoor robot navigation and operation planning. Within the framework, indoor environments are discretized into grid cells that are mapped to graph nodes and classified as target, obstacle, or regular nodes according to their spatial relationships with building elements. Traversal costs are assigned to edges connecting neighboring nodes, enabling graph-theoretic algorithms to compute efficient and collision-free navigation paths while avoiding obstacles. Simulation results demonstrate that the proposed graph representation enables efficient and collision-free navigation. A key limitation associated with coarse discretization, namely overlap between target-occupied and obstacle-occupied cells, is identified and mitigated through grid refinement, improving spatial accuracy and path feasibility. The proposed platform supports virtual evaluation of robotic operations prior to deployment and provides a foundation for BIM-informed robotic systems in facility management.

</details>

#### 2026-07-17 - VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds

**Authors:** Zhiyuan Wu, Zhuo Chen, Shan Luo
**Links:** [abs](https://arxiv.org/abs/2607.16146) - [pdf](https://arxiv.org/pdf/2607.16146)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds
- 作者：Zhiyuan Wu, Zhuo Chen, Shan Luo
- 出版日期：2026-07-17T17:27:08Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2607.16146) | [PDF](https://arxiv.org/pdf/2607.16146)

### 一句话总结
本文提出VTLoc，一种利用视觉点云和触觉读数进行接触点定位的视觉-触觉融合框架。

### 研究问题
如何将触觉数据与视觉几何进行精确的空间对齐，以实现从触觉读数预测接触点在物体表面位置的任务（接触定位）。

### 核心思路/方法
1.  提出VTLoc框架，以3D点云作为视觉输入，结合触觉读数进行接触点定位。
2.  引入**几何多模态对齐模块**：从融合的视觉-触觉特征中重建伪点云，并将此伪点云与原始视觉点云对齐，以强制跨模态的空间一致性。
3.  引入**迭代定位更新器**：利用融合的视觉-触觉特征，通过迭代方式不断优化预测的接触点位置。

### 主要贡献
- 提出VTLoc，一种新颖的视觉-触觉框架，用于从触觉读数和3D点云中定位接触点。
- 设计了两个关键组件：几何多模态对齐模块和迭代定位更新器，以解决跨模态空间对齐问题。
- 在包含100个真实物体的新基准上评估，表明VTLoc通过减少局部到全局的对应歧义，提升了单次触觉接触定位性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。该论文提供了一个有明确评估基准的视觉-触觉定位方法，对于从事机器人抓取、对象感知或多模态融合方向的研究者有一定参考价值。但它发表于近期（2026年），尚未有广泛的讨论或复现验证，且摘要未提供与现有具体方法的性能对比数值，其实际效果需进一步查看完整论文。

</details>

<details>
<summary>Abstract</summary>

Vision and touch are complementary modalities essential for robotic perception and manipulation. While vision provides global object context, touch offers precise local information at contact points. Integrating these modalities for contact localization, i.e., predicting the location of touch on an object's surface, poses significant challenges due to the need for accurate spatial alignment between tactile data and visual geometry. To address this challenge, we propose VTLoc, a novel visual-tactile framework that localizes contact points from tactile readings using a 3D point cloud as visual input. VTLoc introduces two key components: a geometric multi-modal alignment module, which reconstructs a pseudo-point cloud from fused visual-tactile features and aligns it with the visual point cloud to enforce spatial consistencies across modalities; and an iterative localizing updater, which iteratively refines the predicted contact location using fused visual-tactile features. Evaluated on a new benchmark of 100 real-world objects, VTLoc improves single-touch contact localization by reducing local-to-global correspondence ambiguity.

</details>

#### 2026-07-16 - RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping

**Authors:** Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2607.15048) - [pdf](https://arxiv.org/pdf/2607.15048)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** surface reconstruction, autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping
- 作者：Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang
- 出版日期：2026-07-16
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.15048

### 一句话总结
该论文提出一种基于自适应网格高斯表示的鲁棒大规模道路表面建图框架ROADGS-T，通过将2D高斯曲面片布置在网格上，并结合道路结构感知的自适应策略和轨迹一致性姿态优化，提升重建质量和效率。

### 研究问题
如何在大规模驾驶场景下，克服现有基于网格的道路表面重建方法存在的重建质量有限和优化成本高的问题，实现高精度、高效的道路表面建图。

### 核心思路/方法
1. **网格高斯表示**：将2D高斯曲面片（surfels）放置于网格上，每个曲面片显式存储颜色、语义和几何信息，相比于传统网格表示和3D高斯基元，更匹配道路薄表面特性，减少冗余基元和重叠。
2. **道路结构感知自适应网格策略**：对几何或语义复杂区域（如车道标记、道路边界、高度变化处）分配更密的高斯曲面片，在平坦区域保持紧凑表示。
3. **轨迹一致性引导的姿态鲁棒优化**：不依赖单一最近车辆姿态，而是从多个邻近姿态估计局部表面先验，并根据几何一致性自适应加权姿态引导的高度正则化。

### 主要贡献
1. 提出基于自适应网格高斯的道路表面建图框架ROADGS-T。
2. 设计网格高斯表示，兼顾道路的薄表面属性和存储效率。
3. 开发道路结构感知自适应网格分配策略，提升复杂区域重建保真度。
4. 提出轨迹一致性引导的姿态鲁棒优化，减少对单一姿态的依赖。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶中道路建图这一关键方向，提出结合自适应网格和高斯表示的新方法，并解决了大规模场景下的效率与质量权衡问题，方法新颖且实用性强。

</details>

<details>
<summary>Abstract</summary>

Road surface mapping plays a crucial role in autonomous driving, supporting high-definition map generation, lane-level perception, and automatic road annotation. Recent mesh-based road surface reconstruction methods have shown promising results, but they still suffer from limited reconstruction quality and high optimization cost, especially in large-scale driving scenarios. To address these limitations, we propose ROADGS-T, a robust and efficient large-scale road surface mapping framework based on adaptive meshgrid Gaussian representation. Specifically, we model the road surface by placing 2D Gaussian surfels on a meshgrid, where each surfel explicitly stores color, semantic, and geometric information. Compared with conventional mesh-based representations and 3D Gaussian primitives, the proposed meshgrid Gaussian representation better matches the thin-surface property of roads while significantly reducing redundant primitives and overlap during optimization. To further improve representation efficiency and structural fidelity, we introduce a road-structure-aware adaptive meshgrid strategy, which allocates denser Gaussian surfels to geometrically or semantically complex regions, such as lane markings, road boundaries, and height discontinuities, while maintaining a compact representation in flat road areas. Moreover, instead of relying on a single nearest vehicle pose, we design a trajectory-consistency-guided pose-robust refinement strategy, which estimates local surface priors from multiple neighboring poses and adaptively weights pose-guided height regularization according to their geometric consistency.

</details>

#### 2026-07-16 - Rotational Motion-Induced Error Compensation for Phase-Shifting Profilometry-Based Eye Reconstruction

**Authors:** Seong-Jin An, Sanghoon Jeon, Yatong An, Jae-Sang Hyun
**Links:** [abs](https://arxiv.org/abs/2607.14876) - [pdf](https://arxiv.org/pdf/2607.14876)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** dynamic 3D, surface reconstruction, AR, augmented reality, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rotational Motion-Induced Error Compensation for Phase-Shifting Profilometry-Based Eye Reconstruction  
- 作者：Seong-Jin An, Sanghoon Jeon, Yatong An, Jae-Sang Hyun  
- 出版日期：2026-07-16  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.14876  

### 一句话总结
本文提出了一种基于旋转运动补偿的框架，用于消除相位偏折轮廓术（PSP）在动态人眼重建中因眼球旋转导致的测量误差。

### 研究问题
如何补偿眼球旋转引起的帧间运动误差，从而提高基于PSP的动态三维眼部重建的准确性和稳定性。

### 核心思路/方法
1. **运动估计**：从图像运动线索中，利用用户特定的三维眼球模型在球坐标系下估计相对眼球旋转。  
2. **误差补偿**：根据估计的运动，补偿因帧间旋转导致的相机像素错位和相位偏移误差。  
3. **区域优化**：引入分区域优化策略，对不同眼部区域独立调整补偿强度，以减少残余伪影。

### 主要贡献
- 提出了一种专门针对眼球旋转运动误差的补偿框架，显著抑制了运动引起的变形，提升了重建精度。  
- 通过旋转假眼实验验证了方法的有效性，并在非球形刚体实验中表明补偿原理不局限于球形眼球几何结构。  
- 为未来沉浸式环境中的高精度动态眼动追踪提供了实用基础。

### 局限性
摘要未提供足够信息。具体局限性包括：实验仅使用旋转假眼和非球形刚体，未提及真实人眼测试结果；未说明计算效率或实时性要求；未讨论不同旋转速度或复杂运动模式下的性能边界。

### 阅读优先级
**高**  
理由：该工作直接面向VR/AR中的高精度眼动追踪需求，针对动态三维重建中的核心运动误差问题提出了创新性解决方案，且通过实验验证了有效性。对于从事沉浸式显示、计算机视觉或精密测量领域的研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

With the proliferation of immersive Head-Mounted Displays (HMDs) for Virtual and Augmented Reality (VR/AR), reliable and high-precision eye tracking has become increasingly important. Conventional 2D image-based methods offer low system complexity but remain limited in stability, accuracy, and robustness. Three-dimensional ocular surface reconstruction can provide richer geomet-ric information, and structured light profilometry is particularly attractive because it enables dense and accurate surface measurement. However, Phase-Shifting Profilometry (PSP), which estimates phase from sequentially acquired fringe images, is highly susceptible to motion-induced errors when the eye rotates between frames. This study proposes a rotational motion compensation framework for PSP-based dynamic 3D eye reconstruction. Relative eye rotation is estimated from image-based motion cues using a user-specific 3D eye model in a spherical-coordinate domain. The estimated motion is then used to compensate for camera-pixel mismatch and phase-shift errors caused by inter-frame rotation. A region-wise optimization strategy is further introduced to reduce residual artifacts by inde-pendently refining the compensation strength in different ocular regions. Experiments with a rotating fake eye under non-uniform motion demonstrate that the proposed method substantially suppresses motion-induced deformation and improves reconstruction accuracy. An additional experiment with a non-spherical rigid object indicates that the compensation principle is not restricted to spherical eye geometry. These results establish a practical basis for stable PSP-based dynamic 3D eye reconstruction toward future high-precision eye tracking in immersive environments.

</details>

#### 2026-07-16 - Variational Inference for Bird's Eye View Segmentation in Autonomous Driving

**Authors:** Jingyue Shi, Huaicheng Li, Junhui Zhao, Yanxiang Jiang
**Links:** [abs](https://arxiv.org/abs/2607.14710) - [pdf](https://arxiv.org/pdf/2607.14710)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Variational Inference for Bird‘s Eye View Segmentation in Autonomous Driving
- 作者：Jingyue Shi, Huaicheng Li, Junhui Zhao, Yanxiang Jiang
- 出版日期：2026-07-16
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.14710

### 一句话总结
该论文提出了一种基于变分推理和Transformer的鸟瞰图分割网络TVB，通过条件变分自编码器和归一化流来生成多个候选BEV地图，并利用注意力机制进行融合，在nuScenes和OPV2V数据集上取得了优越性能。

### 研究问题
如何有效融合多相机传感器数据，解决自动驾驶中复杂外部环境下鸟瞰图分割的难题。

### 核心思路/方法
1. 将BEV分割问题重构成变分推理框架。
2. 提出Transformer-based变分流变换网络（TVB），以条件变分自编码器（CVAE）为骨干网络，利用后验BEV监督隐式学习多相机视图到统一BEV地图的映射。
3. 在BEV地图生成过程中集成归一化流，以构建更复杂、更具表达力的概率分布，增强生成地图的真实性。
4. 设计BEV-注意力融合（BAF）模块，利用注意力机制自适应地融合多个候选BEV地图。

### 主要贡献
- 首次将变分推理框架引入BEV分割任务。
- 提出了TVB网络，结合CVAE、归一化流和注意力融合机制。
- 在nuScenes和OPV2V两个数据集上的实验表明，该方法在多相机BEV分割和车道环境感知中达到了优越性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由是：该工作针对自动驾驶中的BEV分割这一重要问题提出了新颖的变分推理框架，方法涉及CVAE、归一化流和注意力融合，具有技术亮点，且实验在两个数据集上验证。但由于摘要未提供详细定量对比结果，且缺乏对局限性、计算开销等关键信息的描述，因此优先级别设为中等，适合对BEV分割或变分方法感兴趣的读者进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

The bird's eye view (BEV) has emerged as a pivotal approach for environmental perception in autonomous driving, providing a unified spatial representation for vehicles. Nevertheless, despite BEV's significance in addressing the challenges inherent to autonomous driving, effectively fusing data from multiple camera sensors and operating in complex external driving environments remains a considerable challenge. To mitigate this issue, we recast the BEV segmentation problem within a variational inference framework. In this paper, we propose a novel transformer-based variational flow transformation network for BEV segmentation, denoted as TVB. Our architecture implicitly learns the mapping from multiple camera views to a unified canonical BEV map during training by exploiting posterior BEV supervision. TVB employs a conditional variational auto encoder (CVAE) as its backbone and produces multiple BEV map candidates. To augment the realism of the generated BEV maps, we integrate normalizing flows into the map generation process, enabling the construction of more complex and expressive probability distributions. Furthermore, we design a BEV-attention fusion (BAF) module that harnesses attention mechanisms to adaptively integrate the multiple candidate BEV maps. Experimental results, evaluated on both the nuScenes and OPV2Vdatasets, demonstrate that our proposed method achieves superior performance in multi-camera view BEV segmentation and lane environment perception.

</details>

#### 2026-07-15 - Dynamic Manipulation Hypergraphs for HAR: Beyond Pairwise Relations: Dynamic Manipulation Hypergraphs for Vision-Based Human Activity Recognition

**Authors:** Fatemeh Ziaeetabar
**Links:** [abs](https://arxiv.org/abs/2607.14350) - [pdf](https://arxiv.org/pdf/2607.14350)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dynamic Manipulation Hypergraphs for HAR: Beyond Pairwise Relations: Dynamic Manipulation Hypergraphs for Vision-Based Human Activity Recognition  
- 作者：Fatemeh Ziaeetabar  
- 出版日期：2026-07-15  
- 分类：Embodied / Robotics / AR Applications  
- 链接：摘要: https://arxiv.org/abs/2607.14350 ; PDF: https://arxiv.org/pdf/2607.14350  

### 一句话总结
本文提出一种动态操作超图框架，将人手、物体、工具和支撑面等多实体交互建模为高阶关系单元，通过超图推理网络和时序注意力机制，在细粒度操作识别任务上显著超越传统成对图或静态超图方法。

### 研究问题
如何通过建模随时间变化的多实体高阶关系（而非仅成对边），提升基于视觉的细粒度人机操作活动识别（如手与物体、工具、支撑面的交互）性能。

### 核心思路/方法
1. **超图构建**：在每个时间步，将实体（手、物体、工具、支撑面）用外观、空间、运动和语义角色特征编码，并基于邻近性、接触和运动耦合谓词生成候选超边，通过排序得到高阶关系单元。  
2. **超图推理网络**：执行节点到超边以及超边到节点的消息传递，捕捉多实体间的结构化交互。  
3. **时序注意力**：对演化的交互结构施加时序注意力机制，聚焦关键时间区间。  
4. **评估协议**：在EPIC-KITCHENS-100/VISOR和Assembly101上使用注释辅助的实体定位协议，并与视频/实体基线、成对图、静态超图进行对照。  
5. **定性分析**：在ARCTIC数据集上展示高排名超边与接触密集操作区间的对应关系。

### 主要贡献
1. 提出动态操作超图框架，将多实体交互表示为随时间变化的高阶关系单元，替代传统成对图。  
2. 在EPIC-KITCHENS-100/VISOR上，HO-F1指标比配对的成对图提升6.9个百分点，比静态超图提升4.4个百分点；在Assembly101上分别提升9.5和5.8个百分点。  
3. 提供类无关的超边重要性分数，可识别模型强调的实体配置和时间区间，但不作为因果解释。  
4. 在ARCTIC上的定性分析验证了高阶关系与接触密集操作间的对应性。

### 局限性
摘要未提供足够信息，如计算复杂度、对实体检测或注释的依赖程度、在无注释条件下的性能、或对噪声实体识别的鲁棒性等。

### 阅读优先级
**高**  
理由：该工作针对细粒度人机操作识别的关键难点（多实体动态高阶关系），提出有结构创新的超图框架，在多个数据集上取得显著性能提升（6.9-9.5个百分点），且定性分析直观。对从事活动识别、人机交互、具身智能研究的读者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Fine-grained manipulation recognition requires modeling evolving relations among hands, objects, tools, and supporting surfaces. Conventional graph-based methods use pairwise edges that can fragment a coordinated event into disconnected binary relations. We propose a dynamic manipulation hypergraph framework that represents multi-entity configurations as higher-order relational units. At each temporal step, relevant entities are encoded using appearance, spatial, motion, and semantic-role features. Hyperedge candidates are instantiated and ranked using proximity, contact, and motion-coupling predicates. A hypergraph reasoning network performs node-to-hyperedge and hyperedge-to-node message passing, followed by temporal attention over the evolving interaction structure. The framework provides class-agnostic hyperedge-importance scores that identify entity configurations and temporal intervals emphasized by the model without treating them as causal explanations. Quantitative evaluation is conducted on EPIC-KITCHENS-100/VISOR and Assembly101 under an annotation-assisted entity-localization protocol. Video-only and entity-based methods provide contextual comparisons, while a matched pairwise graph and a static hypergraph serve as the principal controlled baselines because they use identical entity inputs and comparable relational settings. The proposed method improves HO-F1 over the matched pairwise graph by 6.9 percentage points on EPIC-KITCHENS-100/VISOR and 9.5 points on Assembly101, and exceeds the static hypergraph by 4.4 and 5.8 points, respectively. Qualitative analysis on ARCTIC further shows correspondence between highly ranked hyperedges and contact-rich manipulation intervals. These results demonstrate the value of time-varying higher-order relational modeling for fine-grained manipulation activity recognition.

</details>

#### 2026-07-15 - S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving

**Authors:** Jianguo Yu, Rukang Wang, Duanfeng Chu, Chen Wang, Renju Feng, Liping Lu
**Links:** [abs](https://arxiv.org/abs/2607.13926) - [pdf](https://arxiv.org/pdf/2607.13926)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving
- 作者：Jianguo Yu, Rukang Wang, Duanfeng Chu, Chen Wang, Renju Feng, Liping Lu
- 出版日期：2026-07-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.13926

### 一句话总结
本文提出S-squared-VLA框架，通过解耦视觉-语言-动作模型中的语义流与空间流，缓解了传统VLA模型因空间表征崩溃导致的低层级控制精度不足问题，在NAVSIM闭环基准上取得新最优性能。

### 研究问题
传统视觉-语言-动作（VLA）模型在自动驾驶中因离散语言标记与连续轨迹规划之间的语义-物理鸿沟，导致空间表征崩溃，从而难以生成精确的低层级控制动作。如何有效解耦语义与空间信息流，提升VLA模型的细粒度空间感知与轨迹规划能力。

### 核心思路/方法
1. **双流解耦架构**：显式分离语义流与空间流。
   - 语义流：采用层级桥接提取多尺度VLM特征，用于鲁棒的意图推理。
   - 空间流：独立绕过自回归语言瓶颈，直接保留来自视觉编码器的未压缩空间特征，并引入辅助感知监督以增强几何先验。
2. **双流规划适配器**：通过级联注意力机制融合高层语义意图与精确空间约束，生成最终控制动作。

### 主要贡献
- 提出S-squared-VLA，首次在VLA模型中显式解耦语义与空间流，解决空间表征崩溃问题。
- 在NAVSIM闭环基准上，S-squared-VLA在纯监督微调（SFT）设置下达到PDMS 87.1，创下VLA模型新最优；No Collision（NC）率达到98.4，超越所有评估方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文直面自动驾驶VLA模型的关键瓶颈（空间表征崩溃），提出新颖的显式解耦架构，并在标准闭环基准上取得显著领先性能。对于从事自动驾驶、视觉-语言动作模型或多模态控制的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action (VLA) architectures attempt to bridge this gap by unifying perception and control into a single policy, this entanglement creates a new bottleneck. Standard VLAs experience a severe spatial representation collapse, which irreversibly degrades the fine-grained spatial and geometric priors essential for safe, boundary-aware navigation. To address this limitation, we propose the S-squared-VLA, which explicitly decouples the semantic and spatial streams in Vision-Language-Action models. The semantic stream leverages hierarchical bridging to extract multi-scale VLM features for robust intent reasoning. In parallel, an independent spatial stream bypasses the autoregressive language bottleneck, directly preserving uncompressed spatial features from the visual encoder. By integrating auxiliary perception supervision, this stream explicitly equips the model with rich spatial and geometric priors. Finally, a dual-stream planning adapter fuses high-level semantic intent with precise spatial constraints via cascaded attention mechanisms. Evaluations on the NAVSIM closed-loop benchmark show that S-squared-VLA achieves a Predictive Driver Model Score (PDMS) of 87.1, establishing a new state-of-the-art for VLA models under a purely supervised fine-tuning (SFT) setting. By mitigating the spatial representation collapse of traditional VLMs, our framework significantly outperforms baselines, achieving the highest No Collision (NC) rate of 98.4 among all evaluated methods.

</details>

#### 2026-07-15 - Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning

**Authors:** Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen, Qingze Guan, Zhengxing Wu, Wanke Zhan, Yang Sun, Zhiyi Huang, Zitong Shan, Zhenchao Jin, Jiadong Hong, Taowen Wang, Yushi Feng, You Liu, Yibo Wang, Yifan Yang, Zhaowen Zhou, Man Luo, Hao Cheng, Bo Zhang, Jianshu Li, Jiansheng Cai, Guocai Yao, Jize Zhang, Chenhao Lin, Renjing Xu, Lequan Yu, Chao Shen, Chunhua Shen, Zhe Li
**Links:** [abs](https://arxiv.org/abs/2607.14183) - [pdf](https://arxiv.org/pdf/2607.14183)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning
- 作者：Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen, Qingze Guan, Zhengxing Wu, Wanke Zhan, Yang Sun, Zhiyi Huang, Zitong Shan, Zhenchao Jin, Jiadong Hong, Taowen Wang, Yushi Feng, You Liu, Yibo Wang, Yifan Yang, Zhaowen Zhou, Man Luo, Hao Cheng, Bo Zhang, Jianshu Li, Jiansheng Cai, Guocai Yao, Jize Zhang, Chenhao Lin, Renjing Xu, Lequan Yu, Chao Shen, Chunhua Shen, Zhe Li
- 出版日期：2026-07-15
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2607.14183 | PDF：https://arxiv.org/pdf/2607.14183

### 一句话总结
Open-AoE是一个面向具身学习的开放、社区导向的自我中心操作数据集与工具链，包含约2000小时的自然环境人体操作视频及从数据采集到模型训练的完整流水线。

### 研究问题
当前缺乏一种结合低成本连续采集、操作级结构化标注和可复用工具的具身智能资源，以支持从人类视频到机器人学习的高效转化。

### 核心思路/方法
1. **数据集构建**：利用500+名贡献者使用400+部智能手机在自然环境中采集约2000小时的自我中心操作视频。
2. **结构化标注**：为视频提供文本描述、基于MANO的手部姿态、相机轨迹以及时间上局域化的原子动作标注。
3. **数据处理流水线**：包含时间动作分割、语义标注、手部重建和相机轨迹重建，将原始录像转化为结构化样本。
4. **下游工具链**：支持可视化、跨本体重新定位、特定模型数据转换，并提供VLA策略、WAMs和世界模型的训练方案。

### 主要贡献
1. 提供了一个大规模（约2000小时）、低成本、由社区贡献的自我中心操作数据集。
2. 建立了一套从智能手机采集到模型训练、具有完整标注和工具链的开放基础设施。
3. 整合了可扩展数据采集、结构化处理和下游适应，降低了数据贡献与复用的门槛。

### 局限性
摘要未提供足够信息。未提及数据集的具体覆盖动作类型、标注质量验证、训练模型性能评估结果或与现有数据集的对比分析细节。

### 阅读优先级
高。该工作为具身学习领域提供了大规模、开放且实用的基础设施，并结合了从数据到模型训练的全流程工具链，对需要低成本数据资源的研究者或从事人机迁移、世界模型研究的团队具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning. We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training. Its first release contains approximately 2,000 hours of manipulation video collected in natural environments by 500+ contributors using 400+ smartphones. The dataset provides text annotations, MANO-based hand poses, camera trajectories, and temporally localized atomic actions. Open-AoE further includes a data processing pipeline that transforms raw recordings into structured samples through temporal action segmentation, semantic annotation, hand reconstruction, and camera trajectory reconstruction. Meanwhile, we provide a separate downstream toolchain supports visualization, cross-embodiment retargeting, model-specific data conversion, and training recipes for VLA policies, WAMs, and World Models. By integrating scalable capture, structured processing, and downstream adaptation, Open-AoE reduces the barriers to both data contribution and reuse, providing practical open infrastructure for embodied model training, human-to-robot transfer, and world modeling.

</details>

#### 2026-07-15 - UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets

**Authors:** Xian Li, Rong Wei, Lujie Yang, Haolin Huang, Junyuan Fang, Siliang Tang, Jun Xiao, Rui Tang, Juncheng Li
**Links:** [abs](https://arxiv.org/abs/2607.13586) - [pdf](https://arxiv.org/pdf/2607.13586)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets
- 作者：Xian Li, Rong Wei, Lujie Yang, Haolin Huang, Junyuan Fang, Siliang Tang, Jun Xiao, Rui Tang, Juncheng Li
- 出版日期：2026-07-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.13586

### 一句话总结
本文提出UniPhysGen框架，利用UniPhys方法自动将原始3D资产转换为具备统一物理语义（关节语义与内在物理属性）的仿真就绪资产，并构建了大规模数据集与基准。

### 研究问题
如何使现有3D资产自动获得统一的物理语义（包括关节语义和内在物理属性），从而支持具身AI与机器人仿真中的真实交互。

### 核心思路/方法
- 提出UniPhys，一个可扩展的框架，用于自动将原始3D资产转换为具有统一物理语义的仿真就绪资产。
- 基于UniPhys构建了大规模物理语义数据集UniPhys-40K和验证基准UniPhys-Bench。
- 引入UniPhysGen模型，联合推理关节语义和内在物理属性。
- 通过几何鲁棒的关节语义推理，减轻异质部件分解下的几何捷径偏差。

### 主要贡献
1. 提出UniPhys框架，自动化将原始3D资产转换为具备统一物理语义的仿真就绪资产。
2. 构建大规模物理语义数据集UniPhys-40K及验证基准UniPhys-Bench。
3. 提出UniPhysGen模型，在关节语义推理和内在物理属性估计任务上达到最优性能，所得资产可直接部署在机器人仿真环境中。

### 局限性
摘要未提供有关局限性或失败案例的足够信息。

### 阅读优先级
高  
理由：该工作针对具身AI和机器人仿真中3D资产物理语义缺失的关键问题，提供了自动化、可扩展的解决方案，并构建了大规模数据集与基准，实验性能达到最优。对于从事仿真、机器人学或3D场景理解的读者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Physically grounded 3D assets are increasingly important for embodied AI and robotic simulation. However, most existing 3D assets lack unified physical semantics, including articulation semantics and intrinsic physical properties, required for realistic interaction. Current approaches either treat these semantics independently or rely on canonicalized object structures, limiting robustness across heterogeneous 3D assets. We present UniPhys, a scalable framework for automatically transforming raw 3D assets into simulation-ready assets with unified physical semantics. Based on UniPhys, we construct UniPhys-40K, a large-scale physically grounded dataset, together with UniPhys-Bench, a carefully verified benchmark for unified physical grounding evaluation. We further introduce UniPhysGen, a unified physical grounding model that jointly reasons over articulation semantics and intrinsic physical properties. UniPhysGen incorporates geometry-robust articulation grounding to mitigate geometric shortcut bias under heterogeneous part decompositions. Extensive experiments demonstrate state-of-the-art performance across articulation grounding and intrinsic physical property estimation tasks, while the resulting assets can be directly deployed in robotic simulation environments for realistic physical interaction. Our code and dataset will be available at https://github.com/breezexian/UniPhysGen.

</details>

#### 2026-07-15 - GPOcc++: Unified Sparse Gaussian Occupancy Prediction with Visual Geometry Priors

**Authors:** Changqing Zhou, Yueru Luo, Yulan Guo, Bing Wang, Jie Qin, Changhao Chen
**Links:** [abs](https://arxiv.org/abs/2607.13481) - [pdf](https://arxiv.org/pdf/2607.13481)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GPOcc++: Unified Sparse Gaussian Occupancy Prediction with Visual Geometry Priors
- 作者：Changqing Zhou, Yueru Luo, Yulan Guo, Bing Wang, Jie Qin, Changhao Chen
- 出版日期：2026-07-15
- 分类：Embodied / Robotics / AR Applications
- 链接：abstract: https://arxiv.org/abs/2607.13481, pdf: https://arxiv.org/pdf/2607.13481

### 一句话总结
GPOcc++提出一种统一稀疏高斯占用预测框架，利用视觉几何先验，将表面中心输出转化为体素占用感知表示，并在室内外场景中实现高效、泛化强的占用预测。

### 研究问题
如何利用视觉几何先验（其输出本质是表面中心）来补全视觉观测中遮挡和未观察区域的3D占用（需要推理体素内部和自由空间），实现准确的3D场景理解。

### 核心思路/方法
- **GPOcc基础**：将视觉几何先验转换为占用感知的稀疏高斯表示，用于高效表达体场景建模。
- **GPOcc++扩展**：将多视角观测和时间序列以统一框架建模，使用相同表示处理空间和时间证据。
- **场景延伸**：从室内场景扩展至室外占用预测。
- **验证**：在室内外基准上对多视角和时间设置进行实验，验证性能、效率和泛化性。

### 主要贡献
1. 引入GPOcc，将视觉几何先验转化为占用感知的稀疏高斯表示，弥合表面中心输出与体占用推理之间的差距。
2. 提出GPOcc++，在多视角和时间序列设置下实现统一框架，支持空间和时间证据的同表示处理。
3. 将方法从室内扩展到室外占用预测，并在多个基准上展示一致强性能、效率和泛化性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文研究了3D占用预测中的关键挑战（从表面到体积的转换），并提出统一、高效的框架，适用于室内外场景，且实验显示跨设置一致性表现。对于致力于3D场景理解、自动驾驶和具身智能的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate 3D scene understanding is fundamental to embodied intelligence and autonomous driving, where 3D occupancy provides a unified representation of objects, structures, and free space. However, recovering such a complete volumetric representation from visual observations remains challenging, particularly in occluded and unobserved regions. Visual geometry priors offer strong and generalizable geometric cues for addressing this challenge, but their outputs are inherently surface-centric, whereas occupancy prediction requires reasoning about volumetric interiors and free space. To bridge this gap, we introduce GPOcc, which transforms visual geometry priors into occupancy-aware sparse Gaussian representations for efficient and expressive volumetric scene modeling. Building on GPOcc, GPOcc++ models multi-view observations and temporal sequences within a unified framework, allowing spatial and temporal evidence to be handled through the same representation. We further extend GPOcc++ from indoor scenes to outdoor occupancy prediction. Extensive experiments on both indoor and outdoor benchmarks demonstrate consistently strong performance across both multi-view and temporal settings, together with favorable efficiency and generalization. Code will be released at https://github.com/JuIvyy/GPOcc.

</details>

#### 2026-07-15 - Marker-free deformable registration and fusion for augmented reality-guided positive margin localization during tumor resection surgery

**Authors:** Yue Yang, Annie Benson, Matthieu Chabanas, Jason Slagle, Thomas Myles, Matthew B. Weinger, Jon S. Heiselman, Michael I. Miga, Michael Topf, Jie Ying Wu
**Links:** [abs](https://arxiv.org/abs/2607.13343) - [pdf](https://arxiv.org/pdf/2607.13343)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization, AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Marker-free deformable registration and fusion for augmented reality-guided positive margin localization during tumor resection surgery
- 作者：Yue Yang, Annie Benson, Matthieu Chabanas, Jason Slagle, Thomas Myles, Matthew B. Weinger, Jon S. Heiselman, Michael I. Miga, Michael Topf, Jie Ying Wu
- 出版日期：2026-07-15T00:06:52Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.13343

### 一句话总结
本文提出了一种无标记增强现实(AR)工作流，用于在头颈肿瘤切除手术中，将样本切片的阳性边缘定位映射到患者切除床，并在尸体实验中展示了比传统口头指导更低的定位误差。

### 研究问题
如何在没有外部标记物的情况下，将标本病理切片上的阳性边缘标记准确映射到手术切除床，并配合AR显示减小定位误差，改善头颈肿瘤手术中阴阳性边缘的定位精度。

### 核心思路/方法
该方法结合了多个步骤：
1. 对切除后的三维标本扫描进行轮廓约束变形。
2. 将变形后的标本与切除床的深度扫描进行残差对齐。
3. 通过无标记表面配准将信息融合到头戴显示器中。
4. 目标投影到重建的切除床上。利用缝合线对应点估计标本变形；患者与显示器的融合不依赖外部标记。
5. 在尸体实验中将本方法与口头指导、口头指导加标本检查进行对比，评估变形误差、融合误差和端到端边缘定位误差。

### 主要贡献
- 提出并验证了一个无标记的AR工作流，成功将阳性边缘从标本扫描映射到患者切除床。
- 在尸体实验中，端到端边缘定位误差从口头指导的21.40 mm和标本检查的16.09 mm显著降低至AR指导的6.19 mm（p < 0.001）。
- 无标记融合误差为2.15 ± 0.87 mm，与有标记方法无显著差异；在线融合仅需5.23秒。
- 展示了该工作流在更精确肿瘤切除方面的临床潜力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。
理由：该方法直接解决临床头颈肿瘤手术中阳性边缘定位的痛点，实验结果（误差降低至6.19 mm）显示出显著改进，且无标记设计增强了临床应用便利性。属于应用导向的优质工作，对于从事AR手术导航、医学图像配准和肿瘤外科研究的读者具有高参考价值。

</details>

<details>
<summary>Abstract</summary>

Positive margins in head and neck oncologic surgery require mapping specimen-side pathology findings to the patient resection bed. This is challenging because pathologists identify the positive margin on slices of the resected, deformed specimen, while surgeons must relocate the corresponding site on the resection bed using only verbal descriptions and no visual guidance. We present a marker-free augmented reality (AR) workflow for mapping a margin label from a three-dimensional specimen scan to the resection bed. The method combines contour-constrained deformation, residual alignment to a depth scan, surface-based fusion to a head-mounted display, and target projection onto the reconstructed bed. Bead-suture correspondences estimate specimen deformation, whereas patient-to-display fusion does not require external fiducial markers. Following formative experiments, five residents and surgeons performed cadaveric cheek and scalp re-resection tasks under verbal guidance, verbal guidance with specimen examination, and AR guidance. Deformation target errors were $7.63 \pm 3.74$ mm for the cheek and $3.72 \pm 1.02$ mm for the scalp; residual specimen-to-bed distances were $2.43 \pm 2.15$ mm and $2.19 \pm 1.06$ mm, respectively. Fusion error did not differ significantly between marker-free and marker-based methods on either cadaver; overall marker-free fusion error was $2.15 \pm 0.87$ mm. End-to-end margin localization error decreased from $21.40 \pm 3.84$ mm with verbal guidance and $16.09 \pm 4.30$ mm with specimen examination to $6.19 \pm 1.79$ mm with AR guidance ($p < 0.001$). Online fusion required $5.23 \pm 0.34$ s. These results demonstrate effective marker-free AR guidance for positive-margin localization and support more precise tumor resection.

</details>

#### 2026-07-14 - TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

**Authors:** Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee, Tim Wang, Wei Zhan
**Links:** [abs](https://arxiv.org/abs/2607.13028) - [pdf](https://arxiv.org/pdf/2607.13028)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale
- 作者：Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee, Tim Wang, Wei Zhan
- 出版日期：2026-07-14
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.13028

### 一句话总结
TerraZero 是一个程序化生成驾驶场景的模拟器及自博弈训练框架，能在无人类示范和无后备规划器的情况下，从头训练出直接部署到多城市数据集、并在长尾和常规驾驶基准上达到顶尖安全表现的完全学习型驾驶策略。

### 研究问题
如何构建一个模拟器，使其兼具大规模强化学习所需的运行速度、基于真实地图结构的保真度，以及能覆盖安全关键长尾场景的多样性，从而训练出零人类示范、零后备规划器的鲁棒自动驾驶策略。

### 核心思路/方法
- **模拟器设计**：采用基于 C 引擎的配置式架构，在 CPU 上运行仿真，通过零拷贝路径在 GPU 上执行策略推理，实现每秒 130 万代理步长的速度。同时保持高保真度（异质代理、多种动力学模型、完整交通规则）。
- **场景生成**：仅利用日志数据提供真实世界地图几何信息，每个地图上随机生成基于规则的交通参与者、信号控制器，并随机化代理动力学、奖励和尺寸，从而每张地图产生无限多样化场景。
- **训练范式**：通过仅依赖强化学习的自博弈配方，在多个 GPU 上从零开始训练策略，全程无人类示范和推理时的后备规划器。

### 主要贡献
- 提出首个完全学习型策略 TerraZero，在 InterPlan 长尾基准上超越更大规模学习规划器，位列第一。
- 在常规驾驶基准 val14 上，此策略在碰撞及碰撞时间指标上取得最佳成绩，被认为最安全。
- 在 Waymo Open Sim Agents 真实性评估中，该配方优于其他无示范方法，并与最强的参考锚定自博弈方法竞争。
- 策略展现出零样本跨城市和数据集泛化能力，包括在无显式监督下涌现左侧行驶能力。
- 同一框架可同时训练驾驶策略（支持不同动力学的小车和卡车）和模拟代理（控制车辆、行人、自行车手）。

### 局限性
摘要未提供足够信息来描述该方法的局限性，例如在哪些极端场景下可能失效、计算资源需求、或与传统基于规则的模拟器在特定任务上的对比失败案例。

### 阅读优先级
**高**  
理由：该工作提出了一个在速度和多样性上都有显著提升的驾驶模拟器，并在长尾和常规基准上取得了领先的性能和安全性，同时展现了零样本泛化能力，对自动驾驶领域的大规模强化学习研究具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per second on a single server-grade GPU, far faster than existing object-level simulators, while keeping fidelity lighter single-agent systems omit: heterogeneous agents, multiple dynamics models, and full traffic-rule enforcement. TerraZero treats logged data only as a source of real-world map geometry, populating each map with randomized rule-based road users and signal controllers and randomizing agent dynamics, rewards, and sizes per episode, so a map yields an unbounded set of scenarios. Every reported policy trains from scratch by reinforcement learning alone on a compute-efficient self-play recipe across GPUs, with zero human demonstrations and no fallback planner at inference. Policies generalize zero-shot across cities and datasets, including emergent left-hand-traffic driving without explicit supervision. As an ego policy, TerraZero is the first fully learned policy to top the InterPlan long-tail benchmark, ahead of larger learned planners; on routine-driving val14 it ranks among the best approaches and is the safest, posting the best collision and time-to-collision scores. On Waymo Open Sim Agents realism the same recipe outperforms other demonstration-free methods and is competitive with the strongest reference-anchored self-play method. One stack serves both roles: driving policies across dynamics for cars and trucks, and sim agents that jointly control vehicles, pedestrians, and cyclists.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
