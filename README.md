# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：68
- 分类分布：
  - Neural Scene Representations & Rendering: 27
  - 3D Reconstruction & Multi-view Geometry: 21
  - Embodied / Robotics / AR Applications: 12
  - Geometry Foundation Models: 4
  - Dynamic / 4D Reconstruction: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，基于今日提供的论文列表，以下是中文科研趋势综合分析。

#### 今日主要趋势

1.  **场景理解从静态迈向动态与环境感知**：多篇论文不再满足于静态场景的重建，而是深入探讨动态环境下的鲁棒性问题。这体现在两个层面：一是场景本身包含运动物体，如 `OCD SLAM` 和 `DL-SLAM` 致力于在动态环境中实现稳定的SLAM和高质量地图构建；二是模型需要应对动态变化的输入质量，如 `LLM-Empowered Multimodal Fusion Framework` 处理动态变化的传感器噪声和遮挡。这反映出研究正从受控环境向真实世界、非结构化场景迁移。

2.  **前馈式（Feed-Forward）与训练免费（Training-Free）方法成为效率提升主流**：为了摆脱传统优化方法（如COLMAP）或逐场景微调的低效，大量工作探索前馈式预测或零训练推理。`InvSplat` 提出了前馈式逆渲染框架，`NeoMap` 通过流形优化实现免训练的新视角合成，`The Turning Point of 3D Plant Phenotyping` 用3D基础模型实现了秒级跨作物重建，而 `Diversity-aware View Partitioning for Scalable VGGT` 也是无需训练的即插即用框架。这种追求效率的趋势在3D重建、新视角合成和具身智能等计算密集型领域尤为突出。

3.  **大模型与基础模型的深度融合与知识蒸馏**：大语言模型（LLM）和基础模型正被系统地引入视觉和3D任务，作为强大的先验知识来源。例如，`FoundDP` 融合单目深度基础模型以弥补双像素深度估计的不足，`ICDepth` 驯服预训练的视频扩散模型用于深度估计。同时，这些大型模型的高昂成本也催生了知识蒸馏的需求，`Geometric Foundation Model Distillation for Efficient Lunar 3D Reconstruction` 直接研究了如何将复杂基础模型压缩为轻量级学生模型，以适应资源受限的部署场景（如太空探索）。

4.  **3D高斯泼溅（3DGS）的持续演进：从渲染走向综合场景表示与动态处理**：3DGS已经从单纯的新视角渲染工具，演变为集几何、语义、动态于一体的综合场景表示核心。`InvSplat` 用带材质属性的3DGS实现逆渲染，`Bridging 3D Gaussians and Semantic Occupancy` 将其与语义占用场耦合。`DL-SLAM` 和 `Structure-Aware Gaussian Splatting` 则分别针对动态场景和大规模静态场景进行优化，展示了3DGS在不同应用场景下的适应性和潜力。

5.  **面向特定领域应用的工程化系统集成**：除了核心算法创新，将多种模型整合成端到端的实用系统也成为趋势。`VisionAId` 将单目深度、实例分割、人脸识别等6个端侧模型打包成一个面向视障人士的安卓应用，而 `OCD SLAM` 和 `PhysMani` 等则将感知、预测和决策模块耦合，以实现完整的机器人系统。这表明研究重心正从单一模型性能优化转向系统级的鲁棒性和实用性。

#### 技术路线观察

-   **几何基础模型**：主要趋势是 **简化与高效**。`PointDiT` 挑战了复杂架构的必要性，提出极简的像素空间扩散模型；而 `Diversity-aware View Partitioning for Scalable VGGT` 和 `Geometric Foundation Model Distillation` 则从推理和部署的角度，分别通过视图组织和知识蒸馏来解决大模型的可扩展性瓶颈。技术侧重点从“如何构建更强大的模型”转向“如何更聪明地使用和压缩现有强大模型”。
-   **3D/4D 重建 & 神经场景表示**：呈现 **多模态融合、物理感知、应用驱动** 的趋势。`InvSplat` 和 `Learning Spectral and Polarimetric Clues` 展示了将传统RGB建模拓展到材质属性（粗糙度、金属度等）及非常规模态（红外、偏振）的融合。`PhysMani` 强调物理先验（无散度速度场）在预测动态中的重要性。`Structure-Aware Gaussian Splatting` 关注大规模应用的效率问题，`Personalized 4D Whole-Heart Mesh Reconstruction` 则直接服务于医疗数字化转型。技术侧重点是从“生成照片级真实感图像”扩展到“生成可用于仿真、分析和交互的物理或语义世界模型”。
-   **具身智能/机器人/AR应用**：**鲁棒性、安全性与传感器融合** 是核心关切。`Comprehensive Robustness Analysis of LiDAR-based 3D Object Detection` 和 `Towards Robustness against Typographic Attack` 系统地分析了现有模型在对抗攻击下的脆弱性，并提出全面的评估框架和防御手段。`LLM-Empowered Multimodal Fusion Framework` 和 `PhysMani` 分别从高层语义推理和物理规律预测两个角度，提升机器人在复杂、动态、不确定性环境中的决策可靠性。技术侧重点是从“功能实现”向“可靠实现”转变，关注边缘情况（corner cases）和系统容错。

#### 值得优先阅读的论文

1.  **PointDiT** (ID: 2607.02515)
    -   **理由**：该论文挑战了领域内“隐空间扩散+复杂架构”的惯性思维，以极简的像素空间扩散方法在单目几何估计任务上超越复杂模型。其“少即是多”的思路可能启发多个相关方向的架构简化研究，是挑战现有范式的关键工作。

2.  **NeoMap** (ID: 2607.01962)
    -   **理由**：提出了一种全新且优雅的研究视角——将新视角合成问题转化为预训练模型内部流形上的优化问题，并实现了免训练、高质量的结果。该工作揭示了预训练模型内在的潜力，其流形交替投影方法可能被广泛应用于其他“从外部条件生成”的图像/视频任务。

3.  **InvSplat** (ID: 2607.02301)
    -   **理由**：该工作是3DGS向前馈式、可解释场景表示演进的重要一步。它不仅实现了前馈逆渲染，还将材质属性（albedo, roughness, metallic）编码进高斯基元中，这对实现场景重光照、材质编辑等下游应用至关重要，代表了3DGS从“渲染工具”向“场景理解框架”的发展方向。

4.  **Bridging 3D Gaussians and Semantic Occupancy** (ID: 2607.01633)
    -   **理由**：该工作将渲染性3DGS与可空间推理的占用场结合起来，实现了“一鱼多吃”（新视角合成+开放词汇语义+占用预测），且无需相机位姿。完美地解决了3DGS在未观测区域缺乏约束的固有问题，为无位姿、稀疏视图下的综合场景理解提供了一个高质量基线。

5.  **PhysMani** (ID: 2607.01938)
    -   **理由**：该工作是“物理知识”与“3D世界模型”结合的优秀实例，它通过在线优化一个无散度高斯速度场，实现了对动态目标的物理合理预测。其构建的Benchmark和未来感知的动作策略模型，对具身智能中动态物体操控这一难题提供了非常有价值的技术路线。

#### 可能的研究机会

1.  **“极简范式”的推广**：`PointDiT` 和 `NeoMap` 的成功暗示，在设计3D/场景理解的神经网络时，或许应该优先考虑“能否利用现有模型或简化架构解决问题”，而不是默认构建更复杂的系统。研究者可以探索将这种“像素空间扩散”或“流形优化”的思想应用到手部姿态估计、人体重建、4D场景流估计等更多任务中。

2.  **“3DGS + 物理/语义”的深度融合**：当前的工作要么是3DGS+材质属性（`InvSplat`），要么是3DGS+语义占用（`COVScene`），或是3DGS+动态预测（`DL-SLAM`, `PhysMani`）。一个明显的机会是**将三者或更多要素整合进一个统一的3DGS框架**，实现一个能够同时表示几何、外观、语义、材质和物理属性的通用世界模型

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-07T11:12:40-04:00
**Total number of papers:** 69
**Number of papers added in the latest update:** 24
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

#### 2026-07-06 - Reference-Induced Consensus for Selective Posed-Reference Visual Localization

**Authors:** Wonseok Kang, Jaehyun Kim, Jeongmin Lee, Tae-Wan Kim
**Links:** [abs](https://arxiv.org/abs/2607.04722) - [pdf](https://arxiv.org/pdf/2607.04722)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, point map, SfM, localization

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

#### 2026-07-06 - ReCal3R: Reliability-Calibrated Learning Rates for Streaming 3D Reconstruction

**Authors:** Xinze Li, Yiyuan Wang, Pengxu Chen, Wentao Fan, Weifeng Su, Weisi Lin, Wentao Cheng
**Links:** [abs](https://arxiv.org/abs/2607.05356) - [pdf](https://arxiv.org/pdf/2607.05356)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

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
<summary>Abstract</summary>

Applying deep learning to instance-aware reidentification of slate tiles and extraction site classification can improve production efficiency and quality control in the slate tile industry. These tasks are particularly important for handling natural materials where visual variability can make manual inspection costly and error-prone. We present a lightweight, hybrid deep learning approach that combines image matching and classification within a single framework. The system integrates a feature-matching branch based on XFeat with a MobileNetV3- based classification branch. The XFeat branch, combined with a LightGlue matching head, improves instance matching performance by +15.4% AUC. For classification, features from both backbones are shared and fused, resulting in a +10.9% accuracy improvement over a standard MobileNetV3 model. Our approach is evaluated on a newly created industrial dataset consisting of 2,610 slate tile images from six extraction sites. The results demonstrate the effectiveness of the proposed approach for object re-identification and classification in an industrial setting.

</details>

#### 2026-07-06 - Targeted Structure Completion for Sparse-View 3D Reconstruction in Autonomous Driving

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, Liping Hou, Chao Ma
**Links:** [abs](https://arxiv.org/abs/2607.04661) - [pdf](https://arxiv.org/pdf/2607.04661)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, rendering, autonomous driving, localization

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

#### 2026-07-01 - Towards Robust Driving Perception: A Flexible Scale-Driven Family for Self-Supervised Monocular Depth Estimation

**Authors:** Zhaowen Zhu, Li Zhang, Yujie Chen, Tian Zhang, Yingjie Wang, Mingxia Zhan
**Links:** [abs](https://arxiv.org/abs/2607.00736) - [pdf](https://arxiv.org/pdf/2607.00736)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Robust Driving Perception: A Flexible Scale-Driven Family for Self-Supervised Monocular Depth Estimation
- 作者：Zhaowen Zhu, Li Zhang, Yujie Chen, Tian Zhang, Yingjie Wang, Mingxia Zhan
- 出版日期：2026-07-01T10:18:32Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2607.00736， PDF URL: https://arxiv.org/pdf/2607.00736

### 一句话总结
本文提出FlexDepth，一个面向复杂驾驶场景的自监督单目深度估计模型家族，通过静态-动态解耦训练和尺度驱动的解码器，在任意尺度下以极低计算开销实现最先进性能。

### 研究问题
现有自监督单目深度估计模型在复杂驾驶环境中性能显著下降，且针对动态交通参与者的专用网络过于复杂，难以部署在资源受限的车载边缘设备上。

### 核心思路/方法
- 提出**两阶段静态-动态解耦训练策略**，分别评估静态背景和动态道路物体的置信度。
- 设计**尺度驱动解码器（SDD）**，根据尺度大小动态选择组件，实现高效特征融合并输出高精度深度图。
- 通过上述方法构建FlexDepth模型家族，无需任何辅助信息即可在任意尺度下达到最优性能。

### 主要贡献
1. 提出FlexDepth，一个尺度驱动的自监督MDE模型家族，专为具有挑战性的道路场景设计。
2. 提出静态-动态解耦训练策略和尺度驱动解码器（SDD），实现高效的深度估计。
3. 在标准驾驶基准上达到最先进性能，且计算开销极小：最小模型Flex-Nano仅需0.7 GFLOPs，在移动平台上达到37.6 FPS，并具备优秀的零样本泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶感知中的关键问题（复杂环境下的深度估计），提出了轻量化且性能先进的解决方案，实验指标（如0.7 GFLOPs和37.6 FPS）表明其具有实际部署价值。对于关注自监督深度估计、边缘端部署或鲁棒驾驶感知的研究者而言，具有较高的参考意义。

</details>

<details>
<summary>Abstract</summary>

Self-Supervised Monocular Depth Estimation (MDE) has garnered attention in recent years due to its independence from ground truth. However, most existing models are limited to a single scale and exhibit considerable performance degradation in complex driving environments. Networks specifically designed to handle dynamic traffic participants tend to be overly complex, hindering their deployment on resource-constrained automotive edge devices. To address these limitations and move towards robust driving perception, we propose FlexDepth, a scale-driven and flexible family of self-supervised MDE models tailored for challenging road scenarios. FlexDepth employs a two-stage static-dynamic decoupled training strategy, enabling the independent assessment of confidence for both static backgrounds and dynamic road objects. Furthermore, it introduces a meticulously designed Scale-Driven Decoder (SDD) to dynamically select components based on scale size, facilitating efficient feature fusion and the output of high-precision depth maps. Extensive experiments on standard driving benchmarks demonstrate that without any auxiliary information, our model achieves state-of-the-art performance across arbitrary scales with minimal computational overhead. Our smallest model, Flex-Nano, requires only 0.7 GFLOPs and achieves 37.6 FPS on mobile platforms, ensuring reliable real-time perception while maintaining excellent zero-shot generalization. Our source code is avalible: https://github.com/startnew/flexdepth

</details>

#### 2026-07-01 - Active Spatial Guidance: Eliminating Injected Positional Mechanisms in Vision Transformers

**Authors:** Cong Liu, Xiaofang Li, Simon X. Yang
**Links:** [abs](https://arxiv.org/abs/2607.00580) - [pdf](https://arxiv.org/pdf/2607.00580)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Active Spatial Guidance: Eliminating Injected Positional Mechanisms in Vision Transformers
- 作者：Cong Liu, Xiaofang Li, Simon X. Yang
- 出版日期：2026-07-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.00580

### 一句话总结
本文提出一种训练时使用的辅助目标（Active Spatial Guidance），在视觉Transformer中无需注入位置编码，通过坐标回归损失隐式地将空间归纳偏置引入模型，并在多个视觉任务中超越了传统位置注入方法。

### 研究问题
视觉Transformer（ViT）通常需要显式注入位置编码来打破自注意力的排列不变性，但自然图像本身带有空间规律性；本文研究是否可以通过训练过程而非架构设计来诱导空间组织性。

### 核心思路/方法
提出Active Spatial Guidance（简称Guidance），该方法在训练时禁用所有位置编码机制，并在最后一层patch token上施加一个额外的2D坐标回归损失（guidance head），该head仅在训练阶段使用，推理时移除；部署模型由无位置注入的ViT编码器与任务专用预测模块组成。

### 主要贡献
1. 提出一种仅用于训练阶段的辅助目标，无需在ViT架构中注入任何位置编码。
2. 在ImageNet-100分类、ADE20K语义分割和Hypersim单目深度估计任务上，基于DINOv3 ViT骨干网络，该方法一致优于学习型绝对位置编码和旋转位置编码等强基线。
3. 在ImageNet-100上，与多种常见位置编码设计对比，进一步验证Guidance的有效性。
4. 该方法在分辨率迁移下表现更鲁棒，且多分辨率训练可进一步提升不同输入尺寸下的准确性。

### 局限性
摘要未提供足够信息（如Guidance在更大规模数据集或极端低分辨率下的表现、训练收敛速度、对预训练模型的迁移性等）。

### 阅读优先级
**中**  
理由：该工作验证了训练监督可替代架构位置注入的观点，方法简洁且结果正面；但实验仅基于DINOv3和中等规模数据集，目前摘要未展示与SOTA复杂位置机制的全面对比或大规模验证，适合对ViT位置编码设计感兴趣的研究者参考。

</details>

<details>
<summary>Abstract</summary>

Vision Transformers (ViTs) commonly rely on injected positional mechanisms to address self-attention's permutation invariance. Motivated by the spatial regularities of natural images, we ask whether spatial organization can be induced from data rather than explicitly injected. Under controlled, matched from-scratch training, we propose Active Spatial Guidance (Guidance), a training-only objective that disables positional injection and applies an auxiliary 2D coordinate-regression loss to the final-layer patch tokens. The guidance head is used only during training and removed for inference; the deployed model consists of a positional-injection-free ViT encoder and the task-specific prediction module. Using DINOv3 ViT backbones, Guidance consistently improves performance on ImageNet-100 classification, ADE20K semantic segmentation, and Hypersim monocular depth estimation, outperforming strong injected baselines such as learned absolute positional embeddings and rotary positional embeddings under identical training protocols. On ImageNet-100, broader comparisons against representative injected positional designs further support Guidance's effectiveness. Guidance also improves robustness under resolution transfer, and multi-resolution training further strengthens accuracy across input sizes. Overall, our results suggest that spatial inductive bias in ViTs need not be architecturally injected, but can be shaped through training-time supervision. The code used for training and evaluation is publicly available in https://github.com/cloudlc/asg.

</details>

#### 2026-07-01 - EPO: Boosting 3D Foundation Models with Edge-based Pose Optimization

**Authors:** Mattia D'Urso, Christian Sormann, Mattia Rossi, Friedrich Fraundorfer
**Links:** [abs](https://arxiv.org/abs/2607.00579) - [pdf](https://arxiv.org/pdf/2607.00579)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EPO: Boosting 3D Foundation Models with Edge-based Pose Optimization
- 作者：Mattia D'Urso, Christian Sormann, Mattia Rossi, Friedrich Fraundorfer
- 出版日期：2026-07-01T08:02:17Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要：https://arxiv.org/abs/2607.00579，PDF：https://arxiv.org/pdf/2607.00579

### 一句话总结
本文提出了一种名为边缘位姿优化（EPO）的框架，通过无需特征跟踪的边缘图对齐，在低内存和低运行时条件下，显著提升3D基础模型的运动恢复结构（SfM）几何精度。

### 研究问题
3D基础模型在快速推理时，几何精度低于传统SfM管线；而使用传统的捆绑调整（Bundle Adjustment）后处理来提升精度需要重新提取特征轨迹，从而丧失了速度优势。本文旨在解决如何在避免特征提取和轨道构建的前提下，提升3D基础模型的几何重建精度。

### 核心思路/方法
提出完全可微的**边缘位姿优化（EPO）**框架，使用**边缘图对齐**作为几何优化的代理指标，完全避免了显式特征提取和特征轨迹的构建。该方法不需要像捆绑调整那样建立3D点与多图像之间的对应关系（即轨道），而是通过优化边缘图的一致性来改善位姿和重建质量。

### 主要贡献
1. 提出了EPO，一种无需轨道、完全可微的几何优化框架，专为提升3D基础模型的SfM重建质量而设计。
2. 在多个数据集和任务上的实验表明，EPO在匹配或超越传统捆绑调整方法的精度的同时，显著降低了运行时和内存需求。
3. 由于内存占用量小，EPO能够在消费级硬件上运行，而其他竞争的精化方法则无法在此类硬件上执行。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法专门针对当前3D基础模型几何精度不足且后处理复杂的痛点，提出了一个轻量级、可微且无需特征提取的优化方案。实验数据扎实（多个数据集、任务），且展示了在消费级硬件上的可用性，对实际部署具有重要价值。属于三维重建与基础模型交叉方向的新颖技术。

</details>

<details>
<summary>Abstract</summary>

We introduce \textbf{Edge-based Pose Optimization (EPO)}, a trackless geometric optimization framework specifically designed to boost the Structure-from-Motion reconstructions generated by 3D Foundation Models. These models achieve rapid inference by bypassing the time-consuming feature extraction and matching stages of traditional pipelines, where explicit correspondences between each 3D point and multiple images, referred to as tracks, are established. However, their geometric accuracy currently falls short of traditional pipelines. While this can be addressed in a post-processing step via Bundle Adjustment-like refinement, doing so requires extracting feature tracks, thus defeating the original speed advantage. Instead, our fully differentiable framework uses edge map alignment as a proxy for geometric optimization, avoiding feature extraction and track construction entirely. Through extensive evaluation across multiple datasets and tasks, we demonstrate that EPO matches or outperforms Bundle Adjustment-like methods while requiring significantly lower runtime and memory. Notably, its reduced memory footprint makes EPO suitable for consumer-grade hardware, where competing refinement methods cannot run.

</details>

#### 2026-07-01 - LIST3R: Long-sequence Instance-aware 3D Reconstruction

**Authors:** Jing Gao, Wei Wang, Feiran Wang, Yan Yan
**Links:** [abs](https://arxiv.org/abs/2607.00375) - [pdf](https://arxiv.org/pdf/2607.00375)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LIST3R: Long-sequence Instance-aware 3D Reconstruction
- 作者：Jing Gao, Wei Wang, Feiran Wang, Yan Yan
- 出版日期：2026-07-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页: https://arxiv.org/abs/2607.00375，PDF: https://arxiv.org/pdf/2607.00375

### 一句话总结
本文提出一种名为 LIST3R 的实例感知框架，通过将长序列视频分解为子序列，并利用持久化的实例锚点（instance anchors）来匹配与对齐碎片化子序列，从而生成连贯的全局3D场景。

### 研究问题
如何针对长视频序列，在缺乏全局视觉锚点的情况下，实现准确且稳定的 3D 重建，特别是处理子序列碎片间的匹配与对齐问题。

### 核心思路/方法
受人类空间记忆组织方式启发，LIST3R 通过以下步骤进行长序列重建：
1.  **视频分割**：将长视频切分成有重叠的子序列。
2.  **局部重建与实例库构建**：对每个子序列进行部分重建，并构建结构化的局部实例库，库中包含具有语义和几何证据的持久化可追踪锚点。
3.  **跨子序列锚点匹配**：在不同子序列的锚点间进行匹配，以识别被重复扫描的区域。
4.  **对象感知约束对齐**：利用匹配的锚点提供对象感知约束，将碎片化子序列对齐，消除漂移。
5.  **全局实例库整合**：在迭代过程中，随着几何证据的更新，逐步将局部实例库整合为统一的全局实例库。

### 主要贡献
- 提出了一种实例感知的长序列 3D 重建框架，利用实例锚点来组织全局场景。
- 通过持久化锚点在子序列间进行匹配，有效恢复被重复扫描的区域，并为碎片对齐提供对象感知约束。
- 在长序列基准测试上的实验表明，该方法能生成更准确的相机轨迹和更高质量的3D重建。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。
理由：该方法直接针对长视频序列3D重建中常见的漂移和碎片化对齐难题，提出了一个新颖的实例感知组织方案（持久化锚点匹配）。实验在标准长序列基准上取得了更优结果，具有明确的实用价值和启发性。代码已开源，便于复现和进一步研究。

</details>

<details>
<summary>Abstract</summary>

We present LIST3R, an instance-aware framework for long-sequence 3D reconstruction inspired by the way humans organize spatial memory around stable and recognizable objects. LIST3R organizes long-sequence reconstruction around instance anchors, using them to reconnect fragmented subsequences and consolidate local observations into a coherent global 3D scene. Given a long video, our approach partitions it into overlapping subsequences and builds a structured local instance library for each partial reconstruction, maintaining persistent trackable anchors with semantic and geometric evidence. These anchors are matched across subsequences to recover revisited regions and provide object-aware constraints for fragment alignment, producing a consistent global reconstruction. During this process, the evolving geometric evidence updates the local instance libraries and progressively organizes them into a unified global 3D instance library. Experiments on long-sequence benchmarks show that our method produces more accurate trajectories and higher-quality 3D reconstructions, highlighting the effectiveness of persistent instance anchors for organizing long-horizon 3D reconstruction. Our code is available on the project page: https://yixn965.github.io/LIST3R/.

</details>

### 2026-06

#### 2026-06-30 - VOCA: Visual Odometry with Codec Awareness

**Authors:** Nouri Alexander Hilscher, Mateo de Mayo, Dominik Muhle, Christoph Otten genannt Hermes, Daniel Cremers
**Links:** [abs](https://arxiv.org/abs/2607.00189) - [pdf](https://arxiv.org/pdf/2607.00189)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, camera pose estimation, pose estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VOCA: Visual Odometry with Codec Awareness
- 作者：Nouri Alexander Hilscher, Mateo de Mayo, Dominik Muhle, Christoph Otten genannt Hermes, Daniel Cremers
- 出版日期：2026-06-30
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.00189

### 一句话总结
VOCA是一种利用视频编解码信息提升压缩视频流中立体视觉里程计跟踪性能的方法，在因果视觉里程计任务上达到了最先进水平。

### 研究问题
如何利用广泛可用的视频编解码信息，减少视频压缩带来的视觉伪影对传统视觉里程计系统（尤其是立体视觉里程计）性能的影响。

### 核心思路/方法
提出一种因果（causal）立体视觉里程计方法，该方法显式地利用视频流中的编解码信息（codec information），从而在压缩视频流中提高跟踪性能。

### 主要贡献
- 首次利用了视频编解码信息来改进压缩视频流中的视觉里程计跟踪。
- 在因果视觉里程计任务上，针对相对轨迹误差、效率和绝对轨迹误差指标均达到了最先进性能。
- 展示了利用广泛可用的视频编解码信息在视觉任务中的潜力。

### 局限性
摘要未提供局限性信息。

### 阅读优先级
**高**
理由：该工作针对实际系统中广泛存在的视频压缩问题，提出了一种新颖的利用编解码信息的方法，并在多个指标上取得最优结果。对于关注视觉里程计、同时定位与建图以及硬件效率的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera pose estimation from image streams is a critical component of spatial world models that integrate perception into planning and decision-making. Nearly all Visual Odometry (VO) and Simultaneous Localization and Mapping (V-SLAM) systems have focused on datasets containing raw, uncompressed videos. Many working systems instead use ubiquitous hardware units to efficiently compress and decode video streams, saving orders of magnitude in storage and bandwidth. However, this lossy compression introduces visual artifacts that hinder the performance of traditional tracking systems. We present VOCA, a causal stereo visual-odometry method that exploits codec information to improve tracking performance. We achieve state-of-the-art performance on causal VO for relative trajectory error, efficiency, and absolute trajectory error on compressed streams. This work highlights the potential of leveraging widely available video codec information for vision tasks.

</details>

#### 2026-06-30 - PRISM-VO: Scale-Aware Visual Odometry Using Photometric Plenoptic Bundle Adjustment

**Authors:** Aymeric Fleith, Julian Zirbel, Daniel Cremers, Niclas Zeller
**Links:** [abs](https://arxiv.org/abs/2607.00176) - [pdf](https://arxiv.org/pdf/2607.00176)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PRISM-VO: Scale-Aware Visual Odometry Using Photometric Plenoptic Bundle Adjustment
- 作者：Aymeric Fleith, Julian Zirbel, Daniel Cremers, Niclas Zeller
- 出版日期：2026-06-30
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：abstract: https://arxiv.org/abs/2607.00176 ; pdf: https://arxiv.org/pdf/2607.00176

### 一句话总结
本文提出了一种基于纯优化的稀疏光度全向视觉里程计框架PRISM-VO，通过联合优化相机位姿与逆深度，实现了尺度感知且抗漂移的位姿估计。

### 研究问题
如何在仅使用单个全向传感器的情况下，克服单目SLAM的尺度模糊性，并获得准确、抗漂移的视觉里程计结果。

### 核心思路/方法
核心是提出了一种新颖的光度全向光束法平差方法，在滑动窗口内联合优化相机位姿和点的逆深度。该方法利用全向相机单次成像能直接计算几何深度先验的特性，结合时间域多视图约束，从而显式建模全向投影并恢复公制尺度，避免复杂初始化。

### 主要贡献
1. 提出了PRISM-VO，一种纯优化的稀疏光度视觉里程计框架，专为聚焦全向相机设计。
2. 提出了新颖的光度全向光束法平差方法，实现尺度感知的位姿和深度联合优化。
3. 仅依赖单一全向传感器，无需复杂初始化，通过直接计算深度先验解决单目SLAM的尺度模糊问题。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法在室内外场景中均超越了当前最先进的全向视觉里程计方法，并与其他基于优化和学习的方案相媲美，同时确切恢复公制尺度，对3D重建与多视图几何领域具有显著的实际意义。

</details>

<details>
<summary>Abstract</summary>

We introduce PRISM-VO, a novel pure optimization-based sparse photometric visual odometry framework for focused plenoptic cameras. The core of PRISM-VO is a novel photometric plenoptic bundle adjustment which jointly optimizes camera poses and inverse depth values of points in a sliding window. By combining geometric depth from a single plenoptic image with temporal multi-view constraints, PRISM-VO achieves accurate and drift-resilient motion estimation. Through explicit modeling of the plenoptic projection, PRISM-VO provides reliable metric-scale reconstructions, overcoming the scale ambiguity of monocular SLAM algorithms. Importantly, our approach relies solely on a single plenoptic sensor and avoids complex initialization, as depth priors are computed directly from plenoptic imaging. Experiments show that PRISM-VO outperforms the current state-of-the-art plenoptic visual odometry method on indoor and outdoor scenes. The proposed approach rivals other optimization- and learning-based methods while accurately and reliably recovering a metric scale of the scene. Project page: https://prism-vo.github.io/

</details>

#### 2026-06-30 - Planar-SfM: Camera Pose Estimation via Homography Graph Embeddings

**Authors:** Gabi Pragier, Matan Karklinsky, David Ungarish, Avi Ben-Cohen
**Links:** [abs](https://arxiv.org/abs/2606.31979) - [pdf](https://arxiv.org/pdf/2606.31979)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Planar-SfM: Camera Pose Estimation via Homography Graph Embeddings
- 作者：Gabi Pragier, Matan Karklinsky, David Ungarish, Avi Ben-Cohen
- 出版日期：2026-06-30
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2606.31979 | PDF: https://arxiv.org/pdf/2606.31979

### 一句话总结
本文提出一种利用平面场景中的单应性几何约束进行相机位姿估计的新型SfM框架，通过构建单应性位姿图并采用谱嵌入滤波来鲁棒恢复位姿。

### 研究问题
传统基于对极几何的SfM方法在平面场景中会退化失效，如何将平面表面从限制条件转化为几何约束来源，以在高度平面化场景中鲁棒地恢复相机位姿。

### 核心思路/方法
1. 将多视图中共视的每个平面视为独立的相对位姿估计源，通过单应性分解得到位姿候选。
2. 构建基于单应性估计的位姿图，并采用谱嵌入方法将位姿估计映射到实线上，依据几何与视觉一致性识别并过滤不可靠边。
3. 从过滤后的图中提取最大一致生成树用于最终位姿恢复，统一处理高度平面场景（如室内体育馆）与一般3D环境。

### 主要贡献
1. 提出将平面表面作为几何约束源而非障碍的统—框架。
2. 引入基于谱嵌入的图方法，自动筛选单应性位姿估计中的不可靠边。
3. 在传统方法失效的篮球场图像上展现优越性能，并在IMC Phototourism无约束户外场景基准上匹配或超越现有最佳结果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该工作直接挑战传统SfM在平面场景中的退化问题，提出新颖的图嵌入过滤机制，并在特定场景（体育馆）和公开基准上均有可验证的改进，对多视图几何与3D重建领域具有理论与实践价值。

</details>

<details>
<summary>Abstract</summary>

Structure from Motion (SfM) systems traditionally struggle with planar scenes, where standard epipolar geometry-based methods become degenerate. Rather than viewing planar surfaces as a limitation, we propose a unified framework that leverages them as a source of geometric constraints. Our key insight is that each planar surface visible across multiple views provides an independent estimate of relative camera poses through homography decomposition. By aggregating estimates from multiple planes or even from a single dominant plane we achieve robust pose recovery in scenarios where traditional methods fail. We introduce a novel graph-based approach that constructs a pose-graph from homography estimates and employs spectral embedding to identify and filter unreliable edges. Our method maps homography-based pose estimates onto the real line based on their geometric and visual consistency, enabling efficient extraction of a maximally consistent spanning tree for pose recovery. This approach naturally handles both highly planar scenes, such as indoor sports arenas, and general $3$D environments. We demonstrate superior performance on basketball court imagery where existing methods struggle, while matching or exceeding state-of-the-art results on unconstrained outdoor scenes from the IMC Phototourism benchmark.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-06 - WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images

**Authors:** Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan
**Links:** [abs](https://arxiv.org/abs/2607.05347) - [pdf](https://arxiv.org/pdf/2607.05347)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

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

#### 2026-07-01 - GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting

**Authors:** Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang
**Links:** [abs](https://arxiv.org/abs/2607.00959) - [pdf](https://arxiv.org/pdf/2607.00959)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting
- 作者：Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang
- 出版日期：2026-07-01
- 分类：神经场景表示与渲染
- 链接：https://arxiv.org/abs/2607.00959

### 一句话总结
本文提出GaussianEmoTalker，一种基于3D高斯泼溅的实时音频驱动的情绪化说话头合成框架，通过将情绪动画建模为中性与情绪之间的残差变形问题，实现了可控的情绪表达和实时渲染。

### 研究问题
如何在实时约束下，从语音中合成具有可控情绪强度、高唇同步精度和逼真视觉质量的说话头表情动画？

### 核心思路/方法
1. 使用高斯混合形变模型构建身份特定的中性说话空间，提供高保真高斯属性和音素同步的中性运动。
2. 将情绪动画形式化为中性到情绪的残差变形问题，结合网格位移线索、音频特征、情绪类别和强度编码，预测情绪条件化的残差变形。
3. 引入空间-音频-情绪注意力模块，融合异构信号，估计高斯属性的偏移量，实现富有表现力和时间稳定的渲染。

### 主要贡献
- 提出一种基于3D高斯泼溅的实时情绪化说话头合成框架GaussianEmoTalker。
- 将情绪动画建模为中性到情绪的残差变形问题，而非直接预测最终情绪化头像。
- 设计空间-音频-情绪注意力模块，有效融合音频、情绪和强度等多源信息。
- 在视频质量、唇同步、可控情绪表达和实时渲染方面，相比近期方法取得了有竞争力的结果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该工作针对实时情绪化说话头合成这一具有挑战性的任务，提出了新颖的残差变形建模思路和特征融合模块，在情绪可控性和实时性方面具有明显亮点，适合对音频驱动虚拟人、3D高斯渲染及情绪动画感兴趣的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Audio-driven talking head synthesis has achieved impressive progress in lip synchronization and visual quality, yet generating expressive emotional avatars with controllable intensity remains challenging, especially under real-time constraints. In this paper, we present GaussianEmoTalker, an audio-driven framework for real-time emotional talking head synthesis based on 3D Gaussian Splatting. Instead of directly predicting the final emotional avatar from speech, we formulate emotional animation as a neutral-to-emotional residual deformation problem. GaussianEmoTalker first constructs an identity-specific neutral talking space with GaussianBlendshapes, which provides high-fidelity Gaussian attributes and phoneme-synchronized neutral motion. It then predicts an emotion-conditioned residual deformation by combining mesh displacement cues, audio features, emotion categories, and intensity encodings. To fuse these heterogeneous signals, we introduce a spatial-audio-emotion attention module that estimates the offsets of Gaussian attributes for expressive and temporally stable rendering. Extensive experiments demonstrate that GaussianEmoTalker achieves competitive video quality, accurate lip synchronization, controllable emotional expression, and real-time rendering compared with recent emotional talking head methods. Our project page is available at https://njust-yang.github.io/GaussianEmoTalker.github.io/

</details>

#### 2026-07-01 - Improving Sparse-View 3DGS Generalization via Flat Minima Optimization

**Authors:** Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo
**Links:** [abs](https://arxiv.org/abs/2607.00885) - [pdf](https://arxiv.org/pdf/2607.00885)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Improving Sparse-View 3DGS Generalization via Flat Minima Optimization
- 作者：Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo
- 出版日期：2026-07-01T12:52:57Z
- 分类：Neural Scene Representations & Rendering
- 链接：abstract: https://arxiv.org/abs/2607.00885, pdf: https://arxiv.org/pdf/2607.00885

### 一句话总结
本文提出通过平坦极小值优化（Flat Minima Optimization）和周期性重初始化方法，改善3D高斯溅射（3DGS）在稀疏视角输入下的泛化能力，无需修改模型架构即可提升新视角合成质量。

### 研究问题
当3DGS模型的监督仅来自稀疏视角图像时，模型容易对观测图像过拟合，导致对未见过视角的泛化性能差。如何在不改变算法架构的前提下提升稀疏视角下的泛化能力？

### 核心思路/方法
1. **平坦极小值优化**：将高斯参数视为可训练权重，引入适应各向异性高斯几何和训练动态的受控扰动，使优化解更稳定，保留细节的同时缓解过拟合。
2. **周期性重初始化**：在训练过程中短期地将非位置参数重置回初始状态，以进一步稳定平坦极小值优化过程。
3. 方法可无缝集成到现有3DGS流水线中，无需架构改动。

### 主要贡献
- 将平坦极小值优化概念首次适配到3DGS模型，专门处理稀疏视角过拟合问题。
- 提出周期性重初始化技术，增强优化稳定性。
- 在LLFF和Mip-NeRF360数据集上，方法在稀疏视角监督下实现了更优的量化指标和感知质量，生成更清晰、稳定且泛化更好的新视角重建。

### 局限性
摘要未提供足够信息。例如未讨论对不同稀疏程度的量化敏感性、计算开销、对噪声的鲁棒性或对特定场景类型的适用性。

### 阅读优先级
**高**。理由：该工作针对3DGS在少样本场景下的关键技术瓶颈（过拟合与泛化差），提出了与架构解耦的轻量级优化策略，实验提升明显，且方法通用性强。对该方向感兴趣的读者可快速获取潜在改进思路。

</details>

<details>
<summary>Abstract</summary>

Recent advances in neural rendering have established 3D Gaussian Splatting (3DGS) as a highly efficient representation for novel view synthesis, enabling fast training and real-time rendering with strong fidelity. However, when supervision is limited to sparse input views, 3DGS tends to overfit to the observed images and generalize poorly to unseen viewpoints. We address this challenge from the perspective of flat minima (FM) optimization, which seeks solutions that remain stable under small parameter perturbations. Viewing Gaussian parameters as trainable weights, we adapt FM principles to the geometric and dynamic nature of 3DGS with a lightweight training framework. Our method regularizes optimization with controlled Gaussian perturbations that account for each Gaussian's anisotropy and the training progress, preserving fine details while improving robustness to sparse-view overfitting. To further stabilize this flat minima optimization process, we introduce periodic reinitialization, which temporarily returns non-positional parameters to their initial states for a short window. Together, these techniques integrate seamlessly into existing 3DGS pipelines without architectural changes. Experiments on LLFF and Mip-NeRF360 datasets demonstrate improved quantitative metrics and perceptual quality under sparse-view supervision, producing reconstructions that are sharper, more stable, and better generalized to novel viewpoints.

</details>

#### 2026-07-01 - AnchorSplat: Fast and Structure Consistent Detail Synthesis for Gaussian Splatting

**Authors:** Dexu Zhu, Jiangnan Shao, Xiaofeng Wang, Junxian Duan, Jie Cao, Zheng Zhu, Huaibo Huang
**Links:** [abs](https://arxiv.org/abs/2607.01290) - [pdf](https://arxiv.org/pdf/2607.01290)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnchorSplat: Fast and Structure Consistent Detail Synthesis for Gaussian Splatting
- 作者：Dexu Zhu, Jiangnan Shao, Xiaofeng Wang, Junxian Duan, Jie Cao, Zheng Zhu, Huaibo Huang
- 出版日期：2026-07-01
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.01290

### 一句话总结
AnchorSplat 提出一种无需原始多视角图像的3D原生深度网络，通过点锚机制实现高效的几何一致性细节合成，且速度比优化方法快约10^5倍。

### 研究问题
如何在不借助原始多视角图像、避免多视图不一致和高计算成本的前提下，为3D高斯泼溅（3DGS）资产增强细节并减少纹理噪声。

### 核心思路/方法
1. **3D原生端到端网络**：直接在3D结构上运行，避免传统的3D-2D-3D优化管线。
2. **点锚机制（Point Anchor Mechanism）**：通过局部偏移约束强制几何一致性，缓解不良映射和梯度混淆问题。
3. **单次乘法机制**：替代迭代式密度化，实现单步细节生成。
4. **数据与基准**：构建了首个大规模基准数据集3DGS-SR。

### 主要贡献
- 提出 AnchorSplat，一种严格无源（无需原始多视图图像）的3D原生细节合成方法。
- 引入点锚机制以保持几何一致性，并采用单次乘法替换迭代密度化。
- 构建了3DGS-SR，该任务首个大规模基准数据集。
- 在3DGS-SR上取得最先进效果，吞吐量比优化方法快约10^5倍。
- 展现出对包括生成模型输出和真实扫描在内的多样化数据分布的鲁棒零样本泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法在速度上有数量级提升（10^5倍），且无需原始多视图图像，具备零样本泛化能力，对3DGS质量改善领域具有显著实用价值和推广潜力。摘要提供了清晰的思路、实验基准和性能数据，适合快速跟进研读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as a powerful representation for high-fidelity rendering. However, existing assets often suffer from quality bottlenecks such as missing details and texture noise. Prior attempts to enhance these assets via 2D image processing introduce multi-view inconsistencies and high computational costs. In this paper, we propose a novel 3D-native refinement paradigm named AnchorSplat. AnchorSplat is an end-to-end deep network operating directly on 3D structures, avoiding the expensive optimization overhead of traditional 3D-2D-3D pipelines. Crucially, AnchorSplat is a strictly source-free solution requiring no original multi-view images. Central to the proposed method is the Point Anchor Mechanism, which enforces geometric consistency via local offset constraints, mitigating ill-posed mapping and gradient confounding. Furthermore, AnchorSplat replaces iterative densification with a single-pass multiplication mechanism. To facilitate research, we construct 3DGS-SR, the first large-scale benchmark for this task. Experiments demonstrate state-of-the-art results on the 3DGS-SR dataset, with throughput up to $10^5$ times faster than optimization methods. Notably, AnchorSplat exhibits robust zero-shot generalization across diverse data distributions, including generative model outputs and real-world scans.

</details>

#### 2026-07-01 - Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences

**Authors:** Zhenjia Li, Jinrang Jia, Yifeng Shi
**Links:** [abs](https://arxiv.org/abs/2607.00832) - [pdf](https://arxiv.org/pdf/2607.00832)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences
- 作者：Zhenjia Li, Jinrang Jia, Yifeng Shi
- 出版日期：2026-07-01T11:54:02Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.00832

### 一句话总结
Pano2World提出一种端到端方法，以单张室内全景图为输入，直接生成可探索的3D高斯场景，利用全景扩散模型和视角感知注意力路由实现多视图一致性，并通过潜在特征适配器避免信息损失。

### 研究问题
如何从单张室内全景图直接生成可自由探索的3D场景，以克服现有迭代方法（误差累积、流程繁琐）和视频生成模型（轨迹约束、限制多方向覆盖）的局限性。

### 核心思路/方法
1. **粗3D高斯代理重建**：从单张全景图重建初始3D高斯代理，并在自适应采样的邻近视角渲染出几何对齐的引导全景图。
2. **全景扩散模型+视角感知注意力路由**：所有目标视图通过视角感知注意力路由联合去噪，每个目标视图同时接收引导全景图的几何约束和源全景图的全局语义引导，强制跨视图一致性。
3. **潜在特征适配器**：设计几何感知桥梁模块，将联合去噪过程中形成的多视图隐藏特征直接蒸馏为场景潜在表示，避免通过VAE解码回像素域造成的信息损失，最终解码为3D高斯场景。

### 主要贡献
- 提出端到端框架Pano2World，从单张全景图直接输出可探索的3D高斯场景，无需迭代多步流程。
- 引入视角感知注意力路由，在联合去噪中同时利用几何与语义约束，增强跨视图一致性。
- 设计潜在特征适配器，减少多视图隐藏特征解码过程中的信息损失。

### 局限性
摘要未提供关于方法局限性（如复杂度、泛化性、潜在假设等）的讨论。

### 阅读优先级
**高**  
理由：该工作针对单张全景图到3D场景生成这一前沿问题，方法具有创新性（结合扩散模型、注意力路由与特征适配器），并在基准测试中显著超越现有方法，对神经场景表示和3D生成领域研究者有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

A single panorama captures the full visual sphere from one camera center, yet confines users to looking around in place without enabling true scene exploration. Converting a single panorama into a persistent, renderable 3D representation for free-viewpoint navigation has attracted growing interest; existing methods either adopt iterative per-view completion that propagates inpainting results to update the underlying geometry, leading to progressive error accumulation and cumbersome multi-step pipelines, or leverage the temporal consistency priors of video generation models, yet the continuous-trajectory constraint intrinsic to such models limits their flexibility in covering scenes from multiple directions simultaneously. We present Pano2World, which takes a single indoor panorama as input and directly outputs a persistent, explorable 3D Gaussian scene. Given the source panorama, Pano2World first reconstructs a coarse 3D Gaussian proxy and renders it at adaptively sampled nearby poses to obtain geometrically aligned guidance panoramas; a panoramic diffusion model then jointly denoises all target views via View-Aware Attention Routing, where each target view simultaneously receives geometric constraints from its corresponding guidance panorama and global semantic guidance from the source panorama, naturally enforcing cross-view consistency. To avoid the information loss incurred by decoding the multi-view hidden features formed during joint denoising back to the pixel domain via VAE, we introduce Latent Feature Adapter, a geometry-aware bridge module that directly distills these hidden features into a scene latent, subsequently decoded into the final 3D Gaussian scene. Experiments demonstrate that Pano2World significantly outperforms existing methods on the multi-position panoramic novel-view synthesis benchmark.

</details>

#### 2026-07-01 - GADA: Geometry-Aware Deformable Aggregation for Image-Based Gaussian Splatting

**Authors:** Siwoo Lim, Sunjae Yoon, Gwanhyeong Koo, Chang D. Yoo
**Links:** [abs](https://arxiv.org/abs/2607.00595) - [pdf](https://arxiv.org/pdf/2607.00595)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GADA: Geometry-Aware Deformable Aggregation for Image-Based Gaussian Splatting
- 作者：Siwoo Lim, Sunjae Yoon, Gwanhyeong Koo, Chang D. Yoo
- 出版日期：2026-07-01
- 分类：Neural Scene Representations & Rendering
- 链接：arXiv:2607.00595

### 一句话总结
针对基于扭曲（warping）的高斯泼溅方法中因几何不确定性导致像素级空间错位的问题，提出几何感知可变形聚合模块（GADA），通过可变形偏移迭代校正错位并融合隐式置信权重，在保持高频细节质量的同时实现2.13倍速度提升。

### 研究问题
现有基于扭曲的高斯泼溅方法在像素级精度上存在空间错位，尤其是薄结构和高频细节区域，导致残差学习和校正效果受限。

### 核心思路/方法
1. 提出迭代精炼模块，利用可变形偏移（deformable offsets）主动校正扭曲图像中的空间错位，恢复位移后丢失的视觉线索。
2. 引入隐式置信度加权机制，替代标准流程中基于阈值裁剪的可见性检查和简单均值融合，自适应抑制不可靠的证据。

### 主要贡献
1. 首次将可变形聚合与隐式置信度加权引入基于图像的高斯泼溅，主动解决几何不确定性引起的空间错位问题。
2. 在保持高频质量的前提下，实现2.13倍于先前扭曲类高斯泼溅方法的FPS，兼顾精度与效率。

### 局限性
摘要未提供足够信息。例如未讨论方法在复杂遮挡场景、大规模场景或不同光照条件下的表现，也未提及其计算开销或存储需求。

### 阅读优先级
高  
理由：该论文针对高斯泼溅领域中的几何错位痛点提出新方法，在性能（高频细节保持）和效率（2.13倍加速）上均有显著改进，且方法模块设计具有启发性，适合关注神经渲染或可变形对齐的研究者。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has achieved significant improvements by incorporating warping-based techniques. However, such methods suffer from pixel-level inaccuracies due to uncertain geometry. This uncertainty leads to spatial misalignments in the warped images, which disrupt residual learning used in warping-based methods and fundamentally limit the gains of correction, particularly on thin structures and high-frequency details. Driven by our insight that useful visual cues are not lost but locally preserved under slight displacement, we propose Geometry-Aware Deformable Aggregation (GADA). This method introduces an iterative refinement module with deformable offsets to actively correct spatial misalignments and recover these displaced cues. Furthermore, to address the limitations of standard pipelines where visibility checks (i.e., thresholding) often discard valid pixels and multi-view warped image fusion relies on naive mean aggregation, our module is coupled with an implicit confidence weighting mechanism that selectively suppresses unreliable evidence. Consequently, our approach outperforms prior warping-based Gaussian Splatting, preserving high-frequency quality while achieving 2.13 times faster FPS.

</details>

### 2026-06

#### 2026-06-30 - Progressive Pose-Guided 4D Animal Reconstruction from Monocular Video

**Authors:** Siyuan Li, Weiying Chen, Yilin Wang, Xinxin Zuo, Xingyu Li, Li Cheng
**Links:** [abs](https://arxiv.org/abs/2607.00157) - [pdf](https://arxiv.org/pdf/2607.00157)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Progressive Pose-Guided 4D Animal Reconstruction from Monocular Video
- 作者：Siyuan Li, Weiying Chen, Yilin Wang, Xinxin Zuo, Xingyu Li, Li Cheng
- 出版日期：2026-06-30T20:32:29Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2607.00157) | [PDF](https://arxiv.org/pdf/2607.00157)

### 一句话总结
本文提出了一种基于3D高斯泼溅的渐进式测试时优化框架，用于从单目视频中高质量重建4D动物，通过解耦关节点位姿与非刚性形变，实现了跨物种的稳健泛化。

### 研究问题
如何从单目视频中实现对不同物种、复杂姿态的动物进行高保真4D重建，同时避免依赖严格的类别先验或牺牲输入保真度。

### 核心思路/方法
- 采用**渐进式测试时优化**框架，基于3D高斯泼溅实现重建。
- 核心思想：**粗糙的形状先验**结合渐进策略，将**关节点位姿**与**非刚性形变**解耦。
- 具体机制：
  - **对称感知的时间编码**：利用双边线索，同时吸收相机估计漂移。
  - **条件形变机制**：基于可学习的**部位锚点**和**蒙皮场**引导。

### 主要贡献
- 提出一种无需严格类别先验的4D动物重建方法，仅需单目视频。
- 通过解耦策略和对称感知编码，有效处理物种间差异、复杂关节运动和非刚性形变。
- 实验表明，本方法在几何精度、时间一致性和视觉保真度上优于现有基线，即使在先验严重不匹配时也能鲁棒泛化。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对单目视频4D动物重建这一挑战性问题，提出了一种新颖的渐进式优化框架，在泛化性和保真度方面有显著提升，适合对神经场景表示、动物模型重建或测试时优化感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

Reconstructing 4D animals from monocular videos is challenging due to large inter-species variation, complex articulations, and the lack of reliable templates. Existing approaches typically rely on either strict category-specific priors that restrict generalization, or unconstrained generative models that sacrifice input fidelity. To bridge this gap, we present a progressive test-time optimization framework built on 3D Gaussian Splatting for high-fidelity 4D animal reconstruction from a single video. Our key insight is that a coarse shape prior suffices when coupled with a progressive strategy that disentangles articulated pose from non-rigid deformation. Specifically, we employ a symmetry-aware temporal encoding that exploits bilateral cues while absorbing camera estimation drift and a part-conditioned deformation mechanism guided by learnable part anchors and a learnable skinning field. Extensive experiments demonstrate that our approach generalizes robustly across diverse species, achieving superior geometric accuracy, temporal consistency, and visual fidelity compared to existing baselines, even under severe prior mismatch.

</details>

#### 2026-06-30 - PointSplat: Compact Gaussian Splatting via Human-Centric Prediction

**Authors:** Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou
**Links:** [abs](https://arxiv.org/abs/2606.32036) - [pdf](https://arxiv.org/pdf/2606.32036)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PointSplat: Compact Gaussian Splatting via Human-Centric Prediction
- 作者：Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou
- 出版日期：2026-06-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.32036

### 一句话总结
PointSplat提出一种面向人体的前馈式三维高斯溅射方法，通过在3D空间直接预测高斯属性，减少跨视图冗余，从而在保持高渲染质量的同时显著压缩模型表示。

### 研究问题
如何从输入视图实时生成紧凑且高质量的三维人体表示，以克服现有前馈重建方法中因多视图重复编码导致的视图间冗余问题。

### 核心思路/方法
1. 先估计粗略几何代理（coarse geometric proxy），并通过光线投射（ray casting）剔除冗余点，建立显式的2D-3D对应关系。
2. 设计“点-图像变换器”（Point-Image Transformer）融合外观与几何特征，在单次前向传播中预测高斯属性（如位置、形状、颜色等）。
3. 预测仅聚焦于前景感兴趣区域，从而大幅减少高斯原语数量，同时提升新视角渲染质量。

### 主要贡献
- 提出在3D空间直接预测高斯属性的范式，避免多视图间对同一内容的重复编码，降低视图间冗余。
- 设计Point-Image Transformer结构，有效融合2D图像外观与3D几何特征。
- 在多个数据集上实验证明，PointSplat在渲染效率与质量上均优于现有方法，且对视图数量、图像分辨率变化展现出强鲁棒性。

### 局限性
摘要未提供足够信息，未明确讨论方法的局限性，如对复杂人体姿态、遮挡场景或大规模动态环境下的适应性。

### 阅读优先级
**高**  
理由：该方法直击沉浸式直播系统中实时性、紧凑性与高保真的核心矛盾，提出“在3D空间直接预测”的创新思路，且已在多数据集上验证其高效性与鲁棒性，对本领域（神经场景表示与渲染）具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our key insight is to perform predictions directly in 3D space, enabling the network to learn and produce a highly compact representation. To this end, we propose PointSplat, a novel human-centric approach that directly infers Gaussian primitives from an input point set. The proposed method first estimates a coarse geometric proxy and performs ray casting to prune redundant points and establish explicit 2D--3D correspondences. Subsequently, it employs a Point-Image Transformer to fuse appearance and geometry features, predicting Gaussian attributes in a single forward pass. This design restricts predictions to foreground regions of interest, substantially reducing the total number of Gaussians while improving novel-view rendering quality. Extensive experiments demonstrate that PointSplat achieves higher efficiency and quality while exhibiting strong robustness to variations in view count and image resolution across multiple datasets.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-06 - Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis

**Authors:** Xianhao Chen, Jiarui Hu, Yuanbo Yang, Xiyu Zhang, Tengyue Wang, Hujun Bao, Guofeng Zhang, Zhaopeng Cui
**Links:** [abs](https://arxiv.org/abs/2607.05348) - [pdf](https://arxiv.org/pdf/2607.05348)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

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

#### 2026-07-01 - DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors

**Authors:** Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin, Benjamin Busam, Woontack Woo
**Links:** [abs](https://arxiv.org/abs/2607.00889) - [pdf](https://arxiv.org/pdf/2607.00889)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, AR, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors
- 作者：Seok-Young Kim, Abdelrahman Elkhawky, Taewook Ha, Dooyoung Kim, Eunjae Shin, Benjamin Busam, Woontack Woo
- 出版日期：2026-07-01T12:55:09Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.00889

### 一句话总结
本文提出DeWorldSG框架，利用深度引导滤波与世界模型先验，从RGB-D序列中生成时空鲁棒的3D语义场景图，在3DSSG和ReplicaSSG数据集上达到最先进水平。

### 研究问题
现有3D语义场景图生成方法因不稳定的3D对象表示和帧级推理导致的缺失关系，难以构建可靠的3D场景图。

### 核心思路/方法
1. 通过深度引导滤波估计实例级几何3D高斯分布，将每个对象表示为概率3D节点，而非单个投影点，以提升对象表示稳定性。
2. 跨对象对聚合时空证据，并利用世界模型（V-JEPA 2）导出的上下文先验来细化关系，缓解帧级推理带来的关系稀疏性。

### 主要贡献
1. 提出DeWorldSG框架，在3DSSG和ReplicaSSG数据集上，对象和谓词预测均达到最先进性能，并生成时间一致性的场景结构。
2. 相比先前最先进方法，三元组召回率提升77.4%，谓词召回率提升23.2%，适用于机器人操作和AR应用。
3. 代码和模型开源。

### 局限性
摘要未提供足够信息来明确本文方法的局限性，例如计算复杂度、对特定场景的依赖性或潜在失败案例。

### 阅读优先级
**高**
理由：该工作在新兴的3D语义场景图生成任务上取得了显著的性能提升（三元组召回率提升77.4%），并且直接面向机器人操作和AR等具体应用，同时开源代码，对从事相关领域的研究者和工程师具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-level geometric 3D Gaussian distributions through depth-guided filtering and representing each object as a probabilistic 3D node rather than a single projected point. To mitigate relational sparsity from frame-wise inference, our framework further aggregates spatiotemporal evidence across object pairs and refines relations using contextual priors derived from a world model (V-JEPA 2). Experiments on the 3DSSG and ReplicaSSG datasets demonstrate state-of-the-art (SoTA) performance in both object and predicate prediction, while producing temporally consistent scene structures. In particular, our method improves triplet recall by 77.4% and predicate recall by 23.2% over prior SoTA approaches, making it suitable for robotic manipulation and AR applications. Our code and models are open-sourced.

</details>

#### 2026-07-01 - OmniView-Space: Reinforcing Spatial Reasoning via Multi-Perspective Spatial Mapping

**Authors:** Xudong Li, Mengdan Zhang, Peixian Chen, Jiaxi Tan, Zihao Huang, Jingyuan Zheng, Yan Zhang, Xiawu Zheng, Xing Sun, Rongrong Ji
**Links:** [abs](https://arxiv.org/abs/2607.00881) - [pdf](https://arxiv.org/pdf/2607.00881)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mapping, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniView-Space: Reinforcing Spatial Reasoning via Multi-Perspective Spatial Mapping
- 作者：Xudong Li, Mengdan Zhang, Peixian Chen, Jiaxi Tan, Zihao Huang, Jingyuan Zheng, Yan Zhang, Xiawu Zheng, Xing Sun, Rongrong Ji
- 出版日期：2026-07-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.00881

### 一句话总结
本文提出OmniView-Space框架，通过多视角空间映射和工具引导的自我中心推理，增强多模态大语言模型在空间推理中的一致性，并利用认知地图蒸馏减少对外部几何管线的依赖。

### 研究问题
多模态大语言模型在空间推理任务中，难以维持连贯的场景表示，尤其在多步推理中无法动态地将证据重新锚定到查询所需的视角（如相机中心、物体中心或方向中心）。

### 核心思路/方法
1. **多视角空间映射（MPSM）**：将重建的几何信息重新锚定到查询对齐的视觉认知地图和文本空间图。
2. **工具引导的自我中心推理**：训练一个交错策略，主动选择查询所需的自我锚点，并请求对应的MPSM证据。
3. **认知地图蒸馏**：利用MPSM生成的轨迹和自我帧奖励，训练模型使用自生成的认知地图进行推理，减少对外部几何管线依赖。

### 主要贡献
1. 提出OmniView-Space框架，在单图和多图空间推理基准上达到最先进性能。
2. 通过认知地图蒸馏，在保持性能的同时降低对外部几何管线的依赖。
3. 设计了多视角空间映射与工具引导推理机制，提升了多步空间推理的动态锚定能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对多模态大语言模型在空间推理中的核心难点（多视角锚定与一致性）提出系统框架，并展示了性能提升与管线简化，对于从事空间智能、具身智能或多模态推理的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence remains a persistent challenge for Multimodal Large Language Models (MLLMs), as it requires coherent spatial scene representations beyond basic object recognition. Existing methods typically build such representations through textual reasoning or 3D reconstruction. However, they often falter during multi-step reasoning, particularly when required to dynamically re-anchor evidence to the specific camera-, object-, or direction-centric reference frames demanded by complex queries. To address this, we propose OmniView-Space, a framework designed to maintain spatial consistency through multimodal egocentric evidence. Our approach consists of three core components: (1) Multi-Perspective Spatial Mapping (MPSM), which re-anchors reconstructed geometry into a query-aligned visual cognitive map and a textual spatial graph; (2) Tool-Guided Egocentric Reasoning, an interleaved policy trained to actively select the ego anchor required by the query and request the corresponding MPSM evidence; and (3) Cognitive-Map Distillation, which uses MPSM-generated trajectories and ego-frame rewards to train the model to reason with self-generated cognitive maps. Experiments on single- and multi-image spatial reasoning benchmarks show that OmniView-Space achieves state-of-the-art performance. Furthermore, the distilled model maintains this performance while reducing reliance on external geometry pipelines.

</details>

#### 2026-07-01 - DriveVer: Lightweight Trajectory Evaluator as Test-Time Verifier for Autonomous Driving

**Authors:** Chong He, Yuechen Luo, Fang Li, Shaoqing Xu, Fuxi Wen
**Links:** [abs](https://arxiv.org/abs/2607.00399) - [pdf](https://arxiv.org/pdf/2607.00399)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DriveVer: Lightweight Trajectory Evaluator as Test-Time Verifier for Autonomous Driving
- 作者：Chong He, Yuechen Luo, Fang Li, Shaoqing Xu, Fuxi Wen
- 出版日期：2026-07-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.00399

### 一句话总结
DriveVer 是一个轻量级、即插即用的测试时验证器，通过双头架构融合轨迹与感知特征，在推理阶段对自动驾驶轨迹进行安全评分和几何修正，以较小计算开销提升基线规划器性能。

### 研究问题
端到端自动驾驶模型在训练时存在计算成本高、边际收益递减的问题，且现有规划器采用一次生成范式，缺乏推理阶段的二次验证与主动修正机制，导致无法检测和修正次优或不安全的轨迹。

### 核心思路/方法
1. 构建专用轨迹数据集：基于 NAVSIM 基准，通过条件驱动聚类和依据自车状态与导航指令的平衡采样方法生成。
2. 双头架构：融合候选轨迹与多视图视觉表示、自车运动学特征，同时预测安全置信度分数和绝对几何修正向量（从而同时实现轨迹评估与修正）。
3. 测试时缩放（Test-Time Scaling）范式：在不依赖大量且昂贵训练的前提下，通过推理阶段验证与精炼轨迹来提升性能。

### 主要贡献
1. 提出 DriveVer，一种轻量级（仅34M参数）、即插即用的测试时验证器，用于自动驾驶轨迹的后验证与修正。
2. 设计了基于条件驱动聚类与平衡采样的专用轨迹数据集构建方法。
3. 在 NAVSIM 基准上的实验表明，DriveVer 能以极小的计算开销显著提升基线规划模型性能，同时保持实时推理效率。

### 局限性
摘要未提供足够信息。具体局限性（如可能存在的泛化性、对特定场景的失败案例、计算资源要求等）未在摘要中说明。

### 阅读优先级
高。理由：该方法针对自动驾驶中轨迹验证的实用问题提出了一种轻量级且高效的解决方案，双头架构设计新颖，实验在公开基准上展示了性能提升与实时性，对部署场景有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

End-to-end autonomous driving models often encounter performance bottlenecks, as training-time scaling leads to high computational costs and diminishing marginal returns. Existing planners typically adopt a one-shot generation paradigm, lacking secondary validation and active correction mechanisms to detect and revise suboptimal or unsafe trajectories during inference. To address this issue, we propose DriveVer, a lightweight, plug-and-play Test-Time Verifier that leverages the test-time scaling paradigm to enable autonomous driving systems to validate and refine trajectories without costly and heavy training. We construct a dedicated trajectory dataset based on the NAVSIM benchmark through condition-driven clustering and balanced sampling according to ego-vehicle states and navigation commands. Employing a dual-head architecture, DriveVer efficiently fuses candidate trajectories with multi-view visual representations and ego-vehicle kinematic features to simultaneously predict a safety confidence score and an absolute geometric refinement vector. Extensive experiments on the NAVSIM benchmark show that DriveVer significantly improves the performance of base planning models. Notably, as an extremely compact model with only 34M parameters, DriveVer introduces minimal computational overhead, achieving competitive results while maintaining real-time inference efficiency.

</details>

### 2026-06

#### 2026-06-30 - DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation

**Authors:** Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang
**Links:** [abs](https://arxiv.org/abs/2606.31918) - [pdf](https://arxiv.org/pdf/2606.31918)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, autonomous driving, driving scene, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation
- 作者：Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang
- 出版日期：2026-06-30T16:23:32Z
- 分类：Embodied / Robotics / AR Applications（主类别）
- 链接：摘要：https://arxiv.org/abs/2606.31918；PDF：https://arxiv.org/pdf/2606.31918

### 一句话总结
DriveWeaver提出了一种基于点云条件视频修复的框架，用于在自动驾驶仿真中可控地插入前景车辆，解决了现有方法依赖预建3D资产导致的视觉不一致和泛化性差的问题。

### 研究问题
如何在自动驾驶仿真中高效、可控地插入具有预定轨迹的前景车辆，同时确保其视觉真实感（与背景无缝融合）和几何一致性，并支持大规模场景增强。

### 核心思路/方法
- 方法：采用**点云条件视频修复**（Point-Conditioned Video Inpainting）框架，在目标插入区域的掩码上进行视频修复，生成高质量、时间一致的车辆。
- 关键设计：
  - **全局到局部层次化修复策略**（global-to-local hierarchical inpainting strategy），以支持长期生成并保持插入车辆的ID和外观一致。
  - 通过**城市重建管线**提取插入车辆的显式3D高斯表示（explicit 3D Gaussian representations），实现自动驾驶仿真中的实时渲染。

### 主要贡献
1. 提出了DriveWeaver，一种新颖的可控车辆插入框架，利用点云条件视频修复替代传统3D资产依赖方法。
2. 设计了全局到局部的层次化修复策略，确保长序列生成中车辆的视觉一致性。
3. 将修复结果转化为3D高斯表示，实现实时渲染，适用于自动驾驶仿真场景。
4. 在多数据集上实验表明，该方法在视觉真实感和几何一致性上优于现有基线。

### 局限性
摘要未提供关于方法在极端场景（如严重遮挡、复杂光照变化）下的性能表现、计算资源消耗、以及修复失败案例的明确分析。此外，摘要未说明不同数据集规模或车辆类型对性能的影响。

### 阅读优先级
**高**  
理由：论文针对自动驾驶仿真中的关键问题（可扩展的场景增强和视觉真实性）提出创新性方法，结合视频修复与点云条件，并支持实时渲染，与当前自动驾驶仿真和计算机视觉领域的研究热点高度相关。摘要提供了清晰的方法论和实验结果总结，适合优先深入阅读。

</details>

<details>
<summary>Abstract</summary>

A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes. This process enhances scene diversity and facilitates the creation of various corner cases for testing and improving autonomous driving models. However, existing methods often rely on pre-reconstructed 3D assets, which frequently lead to lighting inconsistencies between the inserted foreground and the background. Moreover, the reliance on limited, manually-curated 3D assets hinders large-scale deployment. To address these challenges, we propose DriveWeaver, a novel framework for controllable vehicle insertion in autonomous driving simulation. Specifically, for a masked target insertion area, DriveWeaver performs video inpainting conditioned on vehicle point clouds to generate high-quality, temporally consistent vehicles. This video-inpainting-based approach ensures seamless blending between the foreground and background, while the readily available point cloud conditions enable superior generalization. To support long-term generation, we further design a global-to-local hierarchical inpainting strategy, ensuring the consistent identity and appearance of the inserted vehicles. Meanwhile, we extract explicit 3D Gaussian representations of the inserted vehicles through an urban reconstruction pipeline to enable real-time rendering for autonomous driving simulation. Extensive experiments across diverse datasets demonstrate that our method outperforms existing baselines in visual realism and geometric consistency, providing a robust tool for scalable autonomous driving scene augmentation.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
