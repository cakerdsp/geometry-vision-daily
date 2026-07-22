# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：43
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 13
  - Neural Scene Representations & Rendering: 12
  - Embodied / Robotics / AR Applications: 12
  - Geometry Foundation Models: 5
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

## 今日科研趋势综合分析（2026-07-20）

### 今日主要趋势

#### 1. 几何基础模型从“大而全”向“小而精”与“多模态对齐”演进
一系列论文（如 **DepthART**、**VIDAR**、**DROID-ANCHOR**、**MuViSeg**）显示出几何基础模型研究的两个新方向：**一是将大模型的泛化能力迁移到轻量化设备端**，**二是利用里程计、IMU等模态为缺乏尺度感的基础模型提供“度量锚点”**。这表明该领域正在从追求更大的模型和更强的泛化，转向解决**实际部署中的尺度一致性、模型效率和多视角几何一致性**问题。

#### 2. 3D高斯泼溅（3DGS）进入“鲁棒性与效率”的系统优化阶段
多篇3DGS相关论文（如 **QIRF**、**CaT-GS**、**Blur Trap**、**Atomic Packaging**、**FF-ProCams**）不再只关注渲染质量本身，而是集中于解决3DGS在实际应用中的**根本性缺陷**，如：
- **优化陷阱**：识别并解决收敛到局部次优解的问题（Blur Trap）。
- **存储与传输压缩**：利用非正交性冗余（QIRF）和网络丢包鲁棒性（Atomic Packaging）。
- **大规模场景渲染效率**：帧间缓存与负载均衡（CaT-GS）。
- **稀疏输入下的实时前馈推理**：FF-ProCams 将优化从每场景几分钟降至0.13秒。

这表明3DGS正在从学术演示向**工程化、稳健化**的工业级系统演进。

#### 3. 多模态融合成为动态场景理解与自主系统核心范式
多篇论文（如 **Robust Dynamic Segmentation**、**GeoWorldAD**、**UMCP**、**Attention from Above**）将**2D+3D+语义/文本+时序**等多种模态进行深度耦合。其核心逻辑是：单一模态（如纯2D外观或纯几何）在复杂动态场景中会失效，而融合不同模态（如点轨迹+3D重建、当前几何+未来几何预测、关键点+朝向）可以实现鲁棒的感知与推理。这反映出从“感知”到“理解”的范式转变。

#### 4. 低光照/动态挑战下的“稳健感知”成为新热点
**SLAM in Low-Light**、**Splat-based Extreme Motion-blur** 等论文直面现实世界的恶劣条件（如夜间、快速运动），系统性评估或提出解决方案。这表明社区不再满足于实验室理想场景，而是将**光照不足、运动模糊、动态障碍**视为必须攻克的核心挑战。

### 技术路线观察

| 研究方向 | 技术侧重点 | 代表性论文 |
| :--- | :--- | :--- |
| **几何基础模型** | 轻量化部署、度量尺度锚定（IMU/Odom联合）、多视图实例级对应 | DepthART、VIDAR、DROID-ANCHOR、MuViSeg |
| **3D/4D 重建** | 结合去模糊与位姿估计的端到端重建、融合BIM语义的导航 | Splat-based (Motion-blur)、BIM-enabled Simulation |
| **神经场景表示/渲染 (3DGS)** | 优化陷阱克服、功能性压缩、传输鲁棒性、大规模高效渲染、前馈逆渲染 | QIRF、CaT-GS、Blur Trap、Atomic Packaging、FF-ProCams |
| **机器人/AR 应用** | 多任务统一网络、几何世界模型、激光测距+里程计融合、低光照SLAM | UMCP、GeoWorldAD、Lifelong Localization、SLAM Low-light |
| **图像取证/分割** | 引入3D几何作为新线索、多模态动态分割 | GFrame (IML)、Robust Dynamic Segmentation |

**关键观察**：两个方向出现“交叉融合”趋势。例如，**几何基础模型**被用于为图像篡改定位（GFrame）提供3D线索，也被用于帮助视觉惯性SLAM（VIDAR、DROID-ANCHOR）捕捉局部细节。3DGS则开始被用于解决机器人规划中的逆渲染问题（FF-ProCams）。

### 值得优先阅读的论文

#### 1. **Fine-Detail Monocular Geometry Estimation with Self-Guided Sparse Volumetric Refinement** (arXiv:2607.17967)
- **理由**：该文直击当前单目几何估计的核心瓶颈——**2D参数化导致的细粒度结构平滑**。提出的**3D空间精化**策略具有普适性，可能启发后续深度估计、法向估计等任务放弃纯2D解码，转向稀疏3D空间操作。

#### 2. **Plenoptic Condensation: A Novel Approach to Generalized Scene Reconstruction** (arXiv:2607.18151)
- **理由**：提出全新的“全光凝聚”（PCon）多阶段重建范式，与传统NeRF/Splatting路径不同。其在“Damaged Fiat”案例中展示了**超越SOTA两倍以上精度**，并支持消费级设备，可能开辟“先粗后精”的通用重建新路线。

#### 3. **Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting** (arXiv:2607.17965)
- **理由**：该文首次**形式化定义了3DGS优化中的根本缺陷——“模糊陷阱”**，并提出了极其简单的解决方案（随机播种/分裂）。这不仅是一个新的理论贡献，也为后续所有3DGS优化工作提供了必须避免的“坑”。

#### 4. **DepthART: Scaling Foundation Monocular Depth to Tiny Models** (arXiv:2607.17099)
- **理由**：该文解决了“基础模型如何在设备端落地”这一实际痛点。识别出的**容量瓶颈（过拟合、度量不稳定）** 和提出的抗偏置采样+相机条件微调策略，对希望将任何大型基础模型迁移到嵌入式系统的研究人员具有直接借鉴价值。

#### 5. **MuViSeg: Multi-View Segment Correspondences from Dense Geometry Priors** (arXiv:2607.17938)
- **理由**：在物体级建图、拓扑导航等应用日益重要的背景下，该文提出从**多视图场景获取段级对应**。其多视图注意力头是**解决“传递性对应”** 的核心创新，直接与SLAM中“数据关联”这一核心问题相关。

### 可能的研究机会

- **“轻量化+度量对齐”的组合**：DepthART 提供了轻量化方向，VIDAR/DROID-ANCHOR 提供了度量对齐方向。**将两者结合**，即训练一个极小的、能同时输出度量尺度并保持泛化的单目深度模型，是一个明显的空白。
- **动态场景下3DGS的在线优化**：当前3DGS主要针对静态或准静态场景。**利用多模态动态分割（Robust Segmentation）的结果指导3DGS去掉动态物体，并在动态物体移动后如何“修补”被遮挡背景**，是一个直接的工程与算法结合机会。
- **将“几何世界模型”应用于更广泛的机器人任务**：GeoWorldAD 将当前+未来几何用于规划。**将该范式扩展到机械臂抓取、人机交互**等任务中，利用几何先验预测未来交互空间的变化，是一个有潜力的通用化方向。
- **构建“去模糊+SLAM+3DGS”的统一流水线**：极端运动模糊下的重建（Splat-based Motion-blur）展示了联合优化的威力。**将该思想与轻量化3DGS（CaT-GS, QIRF）结合形成一个端到端的、高效的“稳健感知”流水线**，可用于低光照、快速运动的机器人导航。

### 风险和不确定性

- **缺少真实场景消融和失败案例**：许多论文（如 **PCon**、**QIRF**、**Robust Segmentation**）的摘要仅给出了最佳性能，未阐述在**极端输入（如极度稀疏视角、极度模糊）下的退化行为**或**失败案例**。结论在复杂真实场景中的鲁棒性需要全文数据证明。
- **部分改进的泛化性存疑**：
  - **DepthART** 的方法高度依赖于“蒸馏后的

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-21T10:19:48-04:00
**Total number of papers:** 43
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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
