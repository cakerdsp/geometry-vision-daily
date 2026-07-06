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

**Last updated:** 2026-07-03T10:30:48-04:00
**Total number of papers:** 68
**Number of papers added in the latest update:** 25
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

### 2026-06

#### 2026-06-30 - AnyMatch: Supercharging Universal Multi-Modal Image Matching with Large-Scale Single-View Images

**Authors:** Meng Yang, Zizhuo Li, Linfeng Tang, Fan Fan, Jiayi Ma
**Links:** [abs](https://arxiv.org/abs/2606.31077) - [pdf](https://arxiv.org/pdf/2606.31077)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** image matching, MVS, SfM, depth estimation, monocular depth, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnyMatch: Supercharging Universal Multi-Modal Image Matching with Large-Scale Single-View Images
- 作者：Meng Yang, Zizhuo Li, Linfeng Tang, Fan Fan, Jiayi Ma
- 出版日期：2026-06-30T03:06:58Z
- 分类：Geometry Foundation Models（主类别），3D Reconstruction & Multi-view Geometry（次类别）
- 链接：https://arxiv.org/abs/2606.31077

### 一句话总结
本文提出AnyMatch，一种利用大量单视角图像合成高质量多模态训练数据的方法，以克服多模态图像匹配中真实数据获取成本高、场景多样性不足和3D几何一致性难以保证的问题。

### 研究问题
多模态图像匹配面临训练数据稀缺的困境：真实世界数据集存在采集成本高、场景多样性有限以及SfM-MVS管线误差累积等问题；合成数据方法则难以同时保证3D几何一致性与逼真外观。

### 核心思路/方法
AnyMatch整合单目深度估计、3D重投影、基于扩散模型的图像修复以及跨模态图像翻译，从大量易获取的单视角图像出发，合成多视角、多模态的图像对，并通过显式3D重投影提供严格几何一致性的标注，避免SfM-MVS误差。其框架可通过调节输入和相机参数实现可控的场景多样性与标注难度。

### 主要贡献
1. 提出AnyMatch框架，利用廉价单视图图像生成具有3D几何保证的多模态训练样本。
2. 构建大规模合成数据集Any-syn，用于多模态图像匹配训练。
3. 实验表明，在Any-syn上微调的匹配网络（如LoFTR、EDM、RoMa）在多模态基准上性能显著提升，泛化性和鲁棒性优于现有数据训练模型。

### 局限性
摘要未提供足够信息。文中未明确讨论AnyMatch在复杂现实场景（如动态物体、光照剧烈变化）中的适用性或可能引入的深度估计误差。

### 阅读优先级
高。理由：该工作针对多模态匹配领域数据匮乏的关键瓶颈，提出创新且可扩展的数据生成方案，实验验证有效，符合当前视觉定位和多传感器融合研究的热点需求。

</details>

<details>
<summary>Abstract</summary>

Multi-modal image matching is essential for visual localization and multi-sensor fusion, but it is hindered by the scarcity of large-scale training data with precise geometric annotations. Existing real-world datasets suffer from prohibitive costs, limited scene diversity, and errors in SfM-MVS pipelines, while synthetic methods struggle to maintain 3D geometric consistency or achieve photorealistic appearance. To address this, we propose AnyMatch, a novel framework that leverages abundant, easily accessible single-view images at minimal cost to generate rich multi-modal training data. AnyMatch integrates monocular depth estimation, 3D reprojection, diffusion-based inpainting, and crossmodal image translation to synthesize multi-view, multi-modal image pairs with 3D geometric fidelity. Crucially, our method provides annotations that strictly adhere to 3D geometric consistency through explicit 3D reprojection, avoiding SfM-MVS error accumulation. Furthermore, AnyMatch offers strong scalability, enabling controllable scene diversity and annotation difficulty via adjustable input and camera parameters. We construct Any-syn, a large-scale synthetic multi-modal dataset using AnyMatch. Experimental results show that matching networks (e.g., LoFTR, EDM, RoMa) fine-tuned on Any-syn achieve substantial performance gains on multi-modal benchmarks, exhibiting superior generalization and robustness compared to models trained on existing data.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

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

### 2026-06

#### 2026-06-30 - One Video, One World: Turning Monocular Video into Physical 4D Scenes

**Authors:** Junhao Chen, Boran Zhang, Mingjin Chen, Henghaofan Zhang, Saining Zhang, Congcong Zhu, Hao Zhao, Ruqi Huang, Zhihao Li, Yufei Wang
**Links:** [abs](https://arxiv.org/abs/2606.31388) - [pdf](https://arxiv.org/pdf/2606.31388)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, video-to-4D, rendering, embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Video, One World: Turning Monocular Video into Physical 4D Scenes
- 作者：Junhao Chen, Boran Zhang, Mingjin Chen, Henghaofan Zhang, Saining Zhang, Congcong Zhu, Hao Zhao, Ruqi Huang, Zhihao Li, Yufei Wang
- 出版日期：2026-06-30
- 分类：Dynamic / 4D Reconstruction；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.31388

### 一句话总结
提出首个无需训练的OVOW系统，从单目视频重建出带有实例分离、水密网格且可物理模拟的4D场景。

### 研究问题
如何从单目视频生成具备实例级分离、水密拓扑和物理接口的4D网格场景，以用于物理模拟和具身AI。

### 核心思路/方法
采用四阶段流水线：① 视觉-语言模型对实例进行发现、标注及运动分类；② 类别感知重建：刚性物体生成每实例网格，非刚性物体生成拓扑一致的网格序列；③ 迭代渲染-匹配-优化恢复公制尺度和6自由度位姿轨迹；④ 基于物理的组装施加地面接触和物体间支撑约束。所有运动（刚性和非刚性）通过直接顶点变形建模，无需类别先验或骨架绑定。

### 主要贡献
1. 首个无需训练的、从单目视频到仿真就绪的4D实例级网格场景系统。
2. 建立了首个结构化视频到4D评估基准，涵盖几何正确性、实例分离和物理合理性等指标。
3. 在合成基准上取得最佳布局与几何精度、最低光度与语义误差；单目视频运行速度比基线快1-2个数量级；下游物理模拟验证了其稳定性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接解决了4D重建与物理模拟/具身AI之间的接口空缺，方法新颖（训练自由、实例级水密网格），并建立了首个结构化评估基准，对动态场景重建和机器人应用领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce \textbf{OVOW}, the first training-free system that reconstructs \emph{instance-level, simulation-ready} 4D mesh scenes from a single monocular video. Recent 4D reconstruction achieves impressive rendering quality, but its outputs (\eg, implicit fields, Gaussian primitives, or point clouds) lack the watertight topology, instance separation, and standardized physical interfaces required by physics simulators and embodied AI. OVOW closes this gap with a four-stage pipeline: a vision-language model discovers, labels, and motion-classifies all instances; category-aware reconstruction yields per-instance meshes for rigid objects and topology-consistent mesh sequences for deformable ones; an iterative render-match-optimize procedure recovers metric scale and 6-DoF pose trajectories; and physics-grounded assembly enforces ground contact and inter-object support. Crucially, we model all motion, rigid and non-rigid, through direct vertex deformation without category-specific priors or skeleton rigging, producing watertight mesh scenes ready for downstream physics simulation and editing. We further establish the first benchmark for \emph{structured Video-to-4D} evaluation, with metrics for geometric correctness, instance separation, and physical plausibility beyond visual fidelity; the same pipeline doubles as a scalable engine for \emph{synthesizing} paired video-to-4D simulation data for future 4D world models and embodied AI. Across two synthetic benchmarks (static and 4D), OVOW attains the best overall layout and geometry accuracy and the lowest photometric and semantic error among all baselines, and on monocular video runs one to two orders of magnitude faster than the baselines, while downstream physics simulation confirms its physical stability.

</details>

#### 2026-06-30 - JacobianAvatar: Temporally Consistent Semi-rigid Avatar Reconstruction from a Monocular Video

**Authors:** Changyeon Won, Min-Gyu Park, Seonghwan Park, Ju Hong Yoon, Hae-Gon Jeon
**Links:** [abs](https://arxiv.org/abs/2606.31115) - [pdf](https://arxiv.org/pdf/2606.31115)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** avatar reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JacobianAvatar: Temporally Consistent Semi-rigid Avatar Reconstruction from a Monocular Video
- 作者：Changyeon Won, Min-Gyu Park, Seonghwan Park, Ju Hong Yoon, Hae-Gon Jeon
- 出版日期：2026-06-30
- 分类：动态/4D重建
- 链接：摘要URL: https://arxiv.org/abs/2606.31115；PDF: https://arxiv.org/pdf/2606.31115

### 一句话总结
提出一种利用神经雅可比场（NJF）从单目视频重建半刚性人体化身的方法，通过自监督学习预测雅可比矩阵并解泊松方程，同时引入三项关键组件以处理单目输入中的自遮挡和不可见区域，实现时间稳定且几何一致的动态人体重建。

### 研究问题
如何从单目视频中重建具有复杂运动（如衣物动态）的真实感人体化身，并保持时间一致性，尤其解决自遮挡区域和不可见表面的建模困难。

### 核心思路/方法
1. **核心表示**：采用神经雅可比场（NJF）表示半刚性变形，通过自监督神经网络预测与姿态相关的雅可比矩阵，再求解泊松方程得到变形场。
2. **三个关键组件**：
   - 约束泊松求解器（constrained Poisson solver）：消除边界伪影。
   - 基于符号距离的雅可比正则化（signed distance-based Jacobian regularization）：恢复频繁被遮挡的区域（如腋窝、大腿）。
   - 变形引导的残差光流损失（deformation-guided residual flow loss）：强制运动过程中的时间一致性。

### 主要贡献
- 首次将神经雅可比场应用于单目视频的半刚性化身重建，有效建模全局与局部变形。
- 提出三项针对性设计（约束泊松求解器、符号距离正则化、残差光流损失），解决单目设置中自遮挡、不可见表面及时间不稳定问题。
- 在基准和野外视频上实验表明，生成结果在时间稳定性和几何一致性上优于现有方法。

### 局限性
摘要未提供足够信息，未说明方法对极端姿态、快速运动或复杂遮挡场景的鲁棒性，也未提及计算开销或训练数据要求。

### 阅读优先级
**中**。理由：该方法针对动态人体化身重建这一热门领域提出了创新技术（神经雅可比场与三个组件的结合），实验证据表明其优于现有方法。但摘要未展示详细定量结果或消融实验，且未讨论处理失败的案例，故兴趣程度中等。若读者关注单目动态重建或基于泊松方程的变形建模，则优先级可提高。

</details>

<details>
<summary>Abstract</summary>

Generating realistic human avatars in complex motions--such as clothing dynamics--requires modeling of global and local deformations which remains challenging in monocular settings. We address this problem by leveraging neural Jacobian fields (NJFs) for representing semi-rigid deformations. We train self-supervised neural networks for predicting Jacobian matrices that give the pose-dependent deformations, by solving a Poisson equation. However, monocular input presents several difficulties such as self-occluded regions and invisible surfaces. To address these issues, we introduce three key components: a constrained Poisson solver, signed distance-based Jacobian regularization, and a deformation-guided residual flow loss, which together suppress boundary artifacts, recover frequently occluded regions such as armpits and thighs, and enforce temporal consistency during motion. Experiments on benchmark and in-the-wild videos demonstrate that our method generates temporally stable and geometrically coherent avatars, outperforming state-of-the-art approaches.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

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

#### 2026-06-30 - DrivingDepth: Sparse-Prompted Pixel-wise Scale Correction for Driving Depth Estimation

**Authors:** Chi Huang, Wenhao Zhang, Hang Yin, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Liang Wang
**Links:** [abs](https://arxiv.org/abs/2606.31488) - [pdf](https://arxiv.org/pdf/2606.31488)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DrivingDepth: Sparse-Prompted Pixel-wise Scale Correction for Driving Depth Estimation
- 作者：Chi Huang, Wenhao Zhang, Hang Yin, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Liang Wang
- 出版日期：2026-06-30T11:07:23Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类），Embodied / Robotics / AR Applications（次分类）
- 链接：摘要: https://arxiv.org/abs/2606.31488 | PDF: https://arxiv.org/pdf/2606.31488

### 一句话总结
论文提出DrivingDepth方法，通过稀疏激光雷达作为几何提示，对预训练的深度基础模型进行逐像素尺度校正，从而在保持几何一致性的同时实现高精度度量深度估计。

### 研究问题
自动驾驶中密集深度估计存在几何-尺度冲突：深度基础模型能提供像素对齐的密集视觉几何但缺乏可靠度量尺度，而投影激光雷达能提供度量锚点却稀疏、有噪声且与图像结构不对齐。

### 核心思路/方法
核心思路是：基础模型已捕获几何一致的相对深度，无需额外学习表面结构，只需将相对几何映射到度量坐标的逐像素尺度因子。具体方法上，DrivingDepth将稀疏激光雷达视为几何提示，通过残差逐像素尺度校正局部校准冻结的基础先验，从而在结构上保持密集视觉几何。

### 主要贡献
- 提出基于稀疏提示的逐像素尺度校正方法，解决深度基础模型与激光雷达之间的尺度冲突。
- 在保持冻结基础模型密集视觉几何的同时，实现度量精度提升，无需重新生成深度。
- 在nuScenes数据集（4帧环视输入）上，AbsRel达到11.19，EdgeCR达到5.741，在度量精度和几何一致性上均优于MapAnything（11.99/1.914）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该方法针对自动驾驶密集深度估计中的尺度校正问题，在nuScenes上取得了优于现有方法的结果，思路有创新性（利用冻结基础模型加残差校正）。但缺少对算法复杂度、泛化性及失败案例的讨论，且仅基于摘要无法评估实验完备性。适合对深度估计或自动驾驶感知有兴趣的读者进一步阅读。

</details>

<details>
<summary>Abstract</summary>

Dense depth estimation for autonomous driving faces a geometry-scale conflict: depth foundation models deliver pixel-aligned dense visual geometry without reliable metric scale, while projected LiDAR provides metric anchors that are sparse, noisy, and misaligned with image structures. Existing sparse-prompted methods incorporate LiDAR by regenerating depth from scratch, overriding the foundation model's coherent geometry and producing structural artifacts on visually continuous surfaces. Our key insight is that foundation models already capture geometrically coherent relative depth; no additional surface structure learning is required-only a per-pixel scale factor mapping relative geometry to metric coordinates. Based on this, we propose DrivingDepth, which treats sparse LiDAR as geometric prompts that locally calibrate a frozen foundation prior through residual pixel-wise scale correction, preserving dense visual geometry by construction. On nuScenes with 4-frame surround-view input, DrivingDepth achieves an AbsRel of 11.19 and an EdgeCR of 5.741, outperforming MapAnything (11.99/1.914) by simultaneously delivering SOTA metric accuracy and geometric consistency.

</details>

#### 2026-06-30 - CasaMaestro: Multi-View Panoramas for House-Scale 3D Reconstruction

**Authors:** Yuzhou Ji, Xiaotian Yang, Zhipeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.31086) - [pdf](https://arxiv.org/pdf/2606.31086)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, 3D reconstruction, point cloud reconstruction, embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CasaMaestro: Multi-View Panoramas for House-Scale 3D Reconstruction
- 作者：Yuzhou Ji, Xiaotian Yang, Zhipeng Zhang
- 出版日期：2026-06-30
- 分类：3D Reconstruction & Multi-view Geometry（主）、Embodied / Robotics / AR Applications（副）
- 链接：摘要：https://arxiv.org/abs/2606.31086；PDF：https://arxiv.org/pdf/2606.31086

### 一句话总结
CasaMaestro是一个前馈模型，仅用20至50张稀疏的多视角室内全景图即可直接预测度量深度和相机位姿，实现全屋覆盖的快速点云重建。

### 研究问题
现有针孔相机3D重建管线视场角有限，在大规模室内场景（如多房间住宅）中需要数千张图像才能实现全覆盖，且长序列增量配准容易产生漂移。如何用少量输入高效、度量化地重建住宅尺度3D场景。

### 核心思路/方法
将输入从传统针孔图像替换为**多视角室内全景图**（20至50张），并设计一个**前馈模型**直接端到端预测度量深度和相机位姿，从而避免长序列增量对齐带来的漂移，实现房屋尺度的快速点云重建。

### 主要贡献
- 首个支持**房屋尺度重建**的多视角全景图模型。
- 仅需稀疏全景输入（20~50张）即可获得全屋覆盖的度量深度与位姿，实现快速点云重建。
- 在真实场景和合成场景中均取得高质量结果，可为闭环仿真中的房屋级3D室内资产获取提供基础。

### 局限性
摘要未提供足够信息，无法判断模型在极端光照、镜面反射、大尺度空洞等挑战场景下的表现，以及深度与位姿预测的定量精度指标。

### 阅读优先级
**高**  
理由：该工作直接回应了家庭部署具身智能系统对快速、度量级住宅3D重建的迫切需求，且首次将全景图用于房屋尺度重建，方法简洁且效果已在实景和合成数据上验证，对同领域研究有较强参考价值和启发性。

</details>

<details>
<summary>Abstract</summary>

The rise of home-deployed embodied AI systems is driving a growing need for fast, metric 3D reconstruction of residential spaces to support navigation, interaction, and long-horizon task execution. However, the commonly used pinhole-camera 3D reconstruction pipelines struggle to model large indoor residences efficiently due to their limited field of view, to which achieving full coverage across multiple rooms often requires thousands of images and incurs drift from long chains of incremental alignment. In this work, we present CasaMaestro (Spanish words meaning ``house'' and ``master''), a feedforward model that can take only twenty to fifty sparse multi-view indoor panoramas as input and directly predicts metric depth along with camera poses, allowing fast point-cloud reconstruction of the entire house with full coverage. CasaMaestro is the first model that supports house-scale reconstruction with multi-view panoramas. Experiments show that CasaMaestro can robustly provide high quality results in both real-world and synthetic scenes, which can serve as a strong foundation for acquiring house-scale 3D indoor assets to be applied in close-loop simulation.

</details>

#### 2026-06-29 - Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation

**Authors:** Siddhant Bansal, Zhifan Zhu, Shashank Tripathi, Jiahe Zhao, Michael J. Black, Dima Damen
**Links:** [abs](https://arxiv.org/abs/2606.30598) - [pdf](https://arxiv.org/pdf/2606.30598)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation
- 作者：Siddhant Bansal, Zhifan Zhu, Shashank Tripathi, Jiahe Zhao, Michael J. Black, Dima Damen
- 出版日期：2026-06-29
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.30598

### 一句话总结
本文针对野外第一人称视角下的手-物体3D姿态估计难题，构建了带有密集3D接触标注的野外数据集EPIC-Contact，并提出端到端Transformer模型HOPformer，显著提升了估计成功率并降低了接触误差。

### 研究问题
如何从野外第一人称视角的RGB图像中准确估计手与物体的3D姿态，解决现有方法因严重遮挡和接触歧义而泛化性差、监督数据稀缺的问题。

### 核心思路/方法
1. **数据集构建**：提出EPIC-Contact野外数据集，包含2.3K个片段（62.3K帧），带有密集、双射的3D手-物体接触对应关系及姿态网格模型。
2. **模型设计**：提出HOPformer，一种端到端Transformer架构，单次前向传播即可联合预测双手和物体的3D姿态。其交叉注意力解码器利用手部先验信息调节物体特征，从而实现鲁棒的姿态估计。

### 主要贡献
1. 发布了EPIC-Contact数据集，为野外场景提供了密集的3D手-物体接触标注。
2. 提出了HOPformer模型，在ARCTIC室内数据集上达到82.4%的成功率（超越当前最优方法6.2个百分点）。
3. 在EPIC-Contact数据集上，HOPformer将成功率提升近一倍，同时将接触偏差减少75%。

### 局限性
摘要未提供足够信息。例如，未提及模型的计算成本、对极端光照或快速运动场景的鲁棒性，以及EPIC-Contact数据集的标注多样性或偏差分析。

### 阅读优先级
高。理由：该论文同时贡献了核心数据集和高效模型，在ARCTIC和自建野外数据集上均取得显著提升，且代码和模型已开源，对从事第一人称手-物体交互、3D姿态估计的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Estimating accurate 3D hand-object pose from in-the-wild egocentric RGB remains challenging due to severe occlusions and ambiguous contact. Existing learning-based methods often struggle to generalise to in-the-wild scenes and are limited by the scarcity of supervision. We address these issues with two contributions. First, we introduce EPIC-Contact, an in-the-wild egocentric dataset of 2.3K clips (62.3K frames) with dense, bijective 3D hand-object contact correspondences and posed meshes. Second, we propose HOPformer, an end-to-end transformer that jointly predicts bi-manual hand and object pose in a single forward pass. A cross-attention decoder conditions object features on hand priors, producing robust pose estimation. We test HOPformer on the in-lab 3D dataset, ARCTIC, as well as our newly introduced EPIC-Contact dataset. HOPformer reaches 82.4% success rate on ARCTIC (+6.2 pts over current SOTA). On EPIC-Contact, it nearly doubles the success rate while reducing contact deviation by 75%. EPIC-Contact, HOPformer code and checkpoints are released: https://sid2697.github.io/epic-contact.

</details>

#### 2026-06-29 - StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors

**Authors:** Wenhao Yuan, Yiyuan Ge, Deli Cai
**Links:** [abs](https://arxiv.org/abs/2606.30545) - [pdf](https://arxiv.org/pdf/2606.30545)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** depth estimation, monocular depth, stereo depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors
- 作者：Wenhao Yuan, Yiyuan Ge, Deli Cai
- 出版日期：2026-06-29
- 分类：3D Reconstruction & Multi-view Geometry (主要); Neural Scene Representations & Rendering (次要)
- 链接：摘要链接: https://arxiv.org/abs/2606.30545; PDF链接: https://arxiv.org/pdf/2606.30545

### 一句话总结
本文提出 StereoGS，一种在稀疏视图条件下通过引入立体先验（Stereo Priors）来增强3D高斯泼溅（3DGS）几何一致性的新框架，实现了无需额外推理开销的先进稀疏视图新视角合成性能。

### 研究问题
3D高斯泼溅（3DGS）在稀疏视图设置下因几何约束不足而严重过拟合，现有引入单目深度先验的方法存在尺度模糊和跨视图不一致性，导致几何缺陷。

### 核心思路/方法
1. **立体深度正则化（Stereo Depth Regularization）**：在优化过程中构造虚拟立体对，利用基础立体模型强制施加绝对尺度和双目一致的结构约束，替代传统的尺度不可知单目约束。
2. **梯度感知不透明度衰减（Gradient-Aware Opacity Decay）**：根据高斯原语的相对梯度幅度动态惩罚高斯体，以抑制过拟合并消除冗余原语。
3. **一致性感知密集初始化（Consistency-Aware Dense Initialization）**：使用零样本多视图深度估计方法，将高斯原语有效地锚定到准确的场景表面。

### 主要贡献
- 提出StereoGS框架，首次将立体先验系统性地整合到稀疏视图3DGS中，解决了单目先验的尺度模糊和跨视图不一致问题。
- 设计了立体深度正则化、梯度感知不透明度衰减和一致性感知密集初始化三项关键技术，分别用于建立可靠双目一致性、抑制过拟合和优化初始几何。
- 在LLFF、DTU、Mip-NeRF360和Blender四个数据集上取得稀疏视图下的最先进性能，且不增加额外推理开销。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对3DGS在稀疏视图下的核心难题（几何约束不足）提出了新颖的立体先验框架，方法设计系统且实验结果覆盖多个标准数据集。对于从事3D重建、新视角合成和神经渲染领域的研究者，该工作具有直接的应用价值与启发性。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has achieved remarkable success in real-time novel view synthesis, yet it suffers from severe overfitting under sparse-view settings due to insufficient geometric constraints. While recent methods introduce monocular depth priors to mitigate this, they inherently struggle with scale ambiguity and cross-view inconsistency, leading to defective geometry. In this paper, we propose StereoGS, a novel sparse-view 3DGS framework that integrates stereo priors to establish reliable binocular consistency. Unlike scale-agnostic monocular constraints, StereoGS introduces a Stereo Depth Regularization by constructing virtual stereo pairs during optimization and leveraging a foundation stereo model to enforce absolute scale and binocular-consistent structures. To further suppress overfitting and eliminate redundant primitives, we design a Gradient-Aware Opacity Decay strategy that dynamically penalizes Gaussians based on their relative opacity gradient magnitudes. Combined with a Consistency-Aware Dense Initialization using zero-shot multi-view depth estimation, StereoGS effectively anchors primitives to accurate scene surfaces. Extensive experiments on LLFF, DTU, Mip-NeRF360, and Blender datasets demonstrate that StereoGS achieves state-of-the-art performance in sparse-view settings without incurring any additional inference overhead. Project Page: https://stringerywh00.github.io/StereoGS_project_page/

</details>

## Neural Scene Representations & Rendering

### 2026-07

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

#### 2026-06-30 - NURBS Splatting: A Unified Differentiable Rendering Framework for Vector Graphics

**Authors:** Jingye Qiu, Shizhe Zhou
**Links:** [abs](https://arxiv.org/abs/2606.31764) - [pdf](https://arxiv.org/pdf/2606.31764)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NURBS Splatting: A Unified Differentiable Rendering Framework for Vector Graphics
- 作者：Jingye Qiu, Shizhe Zhou
- 出版日期：2026-06-30
- 分类：神经场景表示与渲染
- 链接：[摘要页](https://arxiv.org/abs/2606.31764) | [PDF](https://arxiv.org/pdf/2606.31764)

### 一句话总结
本文提出NURBS Splatting，一种通过将平面有理曲线表示为连续高斯场，进而实现稳定可微渲染的统一框架。

### 研究问题
现有可微向量渲染器主要针对贝塞尔曲线且依赖解析光栅化，在处理有理样条曲线时存在梯度不稳定、灵活性不足的问题。本文旨在解决平面有理样条的可微渲染挑战。

### 核心思路/方法
将平面有理曲线（NURBS）表示为连续高斯场：通过在曲线参数域和封闭区域内部采样高斯分布，将渲染过程重新表述为平滑的累积过程，从而获得稳定梯度。该方法自然支持长样条、有理权重、非均匀节点和封闭区域填充。

### 主要贡献
- 提出了NURBS Splatting统一框架，实现平面有理曲线的可微渲染。
- 通过高斯场采样重写渲染过程，解决梯度不稳定问题。
- 在书法重建、矢量化框架和长样条图像抽象任务中展示了优于现有方法的重建质量和稳定性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法聚焦于图形学中细分领域（有理样条可微渲染），对于从事矢量化、草图重建或可微渲染的研究者有一定参考价值；但论文尚未提供完整的实验细节（如定量指标、对比基线等），需要阅读全文评估实际效果。

</details>

<details>
<summary>Abstract</summary>

Differentiable rendering of planar rational splines remains largely underexplored, despite their widespread use in vector graphics and design. Existing differentiable vector renderers primarily focus on Bézier curves and rely on analytic rasterization, which can suffer from gradient instability and limited flexibility. We propose NURBS Splatting, a unified framework that represents planar rational curves as continuous Gaussian fields. By sampling Gaussians along the curve parameter domain and inside closed regions, rendering is reformulated as a smooth accumulation process with stable gradients. Our method naturally supports long splines, rational weights, non-uniform knots, and closed-region filling. We demonstrate its effectiveness in calligraphy reconstruction, vectorization frameworks, and long-spline image abstraction, showing improved stability and reconstruction quality over existing approaches.

</details>

#### 2026-06-30 - Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera

**Authors:** Kristof Overdulve, Lode Jorissen, Nick Michiels
**Links:** [abs](https://arxiv.org/abs/2606.31679) - [pdf](https://arxiv.org/pdf/2606.31679)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera
- 作者：Kristof Overdulve, Lode Jorissen, Nick Michiels
- 出版日期：2026-06-30T13:56:26Z
- 分类：Neural Scene Representations & Rendering
- 链接：arxiv.org/abs/2606.31679

### 一句话总结
本文提出了一套完整的管线，用于将针插蝴蝶标本转化为可从任意视角查看的逼真3D模型，解决了微距拍摄景深极浅和腹面不可见两大难题。

### 研究问题
如何高效、高保真地实现针插蝴蝶标本的新视角合成，特别是克服微距镜头景深极浅以及标本腹面难以拍摄的问题。

### 核心思路/方法
提出端到端管线，融合三个关键组件：
1. 手持式焦点堆叠（handheld focus stacking）——无需三脚架即可获得全焦微距图像；
2. 非接触式第一表面镜系统（non-contact first-surface mirror system）——在不触碰标本的前提下露出腹面；
3. 无分割、镜像感知的3D高斯泼溅扩展（segmentation-free, mirror-aware 3D Gaussian Splatting extension）——支持从镜面反射区域进行渲染。

### 主要贡献
- 首次实现针插蝴蝶标本的全方位、逼真新视角合成。
- 提出一种结合焦点堆叠与镜面辅助的实用3D采集与渲染管线。
- 在四个不同标本上验证了重建效果的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：针对自然历史标本数字化这一具体应用场景，该工作提供了可实际部署的完整解决方案，且融合了经典摄影技术与前沿3D高斯泼溅方法，对该方向研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Mounted butterflies are among the most striking objects in natural history collections. However, their beauty is notoriously hard to digitize in 3D: they are small and fragile, with microscopic hairs and vein structures. Capturing them in sufficient detail, therefore, requires a macro lens, which has a very limited Depth of Field (DoF). Moreover, a camera body cannot be maneuvered beneath a pinned specimen to photograph its ventral surface (the underside of the wings). We introduce an end-to-end pipeline that resolves these challenges to turn such specimens into photo-realistic 3D models viewable from every direction. It combines three ingredients: handheld focus stacking for all-in-focus macro capture without a tripod, a non-contact first-surface mirror system that exposes the ventral surface without touching the specimen, and a segmentation-free, mirror-aware 3D Gaussian Splatting extension. We validate the reconstructions on four diverse specimens.

</details>

#### 2026-06-30 - Intrinsic decomposition and editing of 3D Gaussian splats

**Authors:** Alexandre Lanvin, Jeffrey Hu, Simon Lucas, Adrien Bousseau, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2606.31637) - [pdf](https://arxiv.org/pdf/2606.31637)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Intrinsic decomposition and editing of 3D Gaussian splats
- 作者：Alexandre Lanvin, Jeffrey Hu, Simon Lucas, Adrien Bousseau, George Drettakis
- 出版日期：2026-06-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.31637

### 一句话总结
本文提出一种将3D高斯泼溅表示的辐射场分解为固有成分（漫反射反照率和着色）的方法，并支持通过编辑二维图像中的反照率来对平面纹理进行编辑后重新渲染。

### 研究问题
如何对以3D高斯泼溅表示的辐射场进行固有分解，从而支持用户直接修改物体颜色和纹理而不改变光照，并实现多视角下的重新渲染。

### 核心思路/方法
1. 将固有分解建模为独立的高斯基元集，使每个集自适应其所代表层的特征。
2. 采用由数据驱动预测引导的优化过程，将多视角照片分解为反照率和着色等固有成分。
3. 设计一个编辑工作流：用户只需在单张图像中修改平面的反照率，即可将编辑捕获到固有辐射场中，并在任意视角下重新渲染出具有合理光照的场景。

### 主要贡献
- 扩展了固有分解到高斯泼溅辐射场，提出以独立高斯基元集建模各成分的方案。
- 提出了一个结合数据驱动预测的多视角优化方法来分离反照率和着色。
- 提供了一种基于单张图像反照率编辑的平面纹理修改工作流，支持编辑后场景在任意视角下的重渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法将经典的图像固有分解技术扩展到3D高斯泼溅这一新型辐射场表示中，并提供了实用的编辑工作流，对神经场景表示与渲染领域的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Intrinsic decomposition which expresses image colors as the product of diffuse albedo and shading, possibly augmented with view-dependent residuals has a long history in image editing as it enables the modification of object colors and textures without altering lighting. We extend intrinsic decomposition to radiance fields represented with Gaussian splatting by proposing solutions to three key aspects of such decomposition. First, we describe how to model the intrinsic decomposition as independent sets of Gaussian primitives, which allows each set to adapt to the characteristics of the layer it represents. Second, we present an optimization procedure guided by data-driven predictions to disentangle multi-view photographs of a scene into the aforementioned intrinsic sets. Finally, we provide an editing workflow where users modify the texture of planar surfaces simply by modifying the albedo of that surface in one image. Capturing this edit within the intrinsic radiance field allows re-rendering of the edited scene with plausible lighting under arbitrary viewpoints.

</details>

#### 2026-06-30 - DPPE: Rethinking Camera-Based Positional Encoding for Scaling Multi-View Transformers

**Authors:** Shun Kenney, Teppei Suzuki
**Links:** [abs](https://arxiv.org/abs/2606.31585) - [pdf](https://arxiv.org/pdf/2606.31585)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DPPE: Rethinking Camera-Based Positional Encoding for Scaling Multi-View Transformers
- 作者：Shun Kenney, Teppei Suzuki
- 出版日期：2026-06-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.31585

### 一句话总结
本文提出一种解耦式相机位姿位置编码（DPPE），以解决现有基于相机的位置编码在大规模训练后期性能停滞的问题。

### 研究问题
当使用基于相机参数（如外参或投影矩阵）作为相对位置编码来缩放新视图合成（NVS）模型的训练时，模型性能在训练后期出现停滞瓶颈。本文探究了这一瓶颈的成因。

### 核心思路/方法
1. **问题分析**：作者发现，将位置编码中的旋转（rotation）和平移（translation）信息存储在值向量（value vector）的相同维度中，会导致两者无法独立识别（indeterminacy），从而限制了训练的可扩展性。
2. **方法提出**：提出解耦式位姿位置编码（Decoupled Pose Positional Encoding, DPPE），明确将旋转和平移分量进行解耦，以消除识别的模糊性。

### 主要贡献
- 揭示并分析了基于相机的位置编码在缩放训练时性能停滞的根本原因：旋转与平移在同一维度中的混合导致识别不确定性。
- 提出DPPE编码方法，通过显式解耦旋转和平移，使得多视图Transformer能够在放大的训练设置下实现稳定的长期训练。
- 在NVS任务上的实验表明，DPPE在泛化设置（如处理更多视角和缩放场景）中展现出优越的性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：针对多视图Transformer缩放训练的关键瓶颈提出明确解决方案，且在新视图合成任务上验证了稳定训练与泛化优势，对神经场景表示与渲染领域具有直接推动作用。

</details>

<details>
<summary>Abstract</summary>

The remarkable scalability of Transformers has expanded their application to 3D computer vision, where camera-aware positional encoding is crucial for providing spatial cues in multi-view geometry. Recent advancements have established the practice of using camera parameters -- such as extrinsics or projection matrices -- as relative positional encoding into the query, key, and value vectors of the attention mechanism. However, when scaling up the training recipe of novel view synthesis (NVS) models with the camera-based positional encoding, we observe a significant issue: model performance stagnates in the late stages of training. In this paper, we investigate the cause of the performance bottleneck when scaling up and demonstrate that storing rotation and translation given by the positional encoding in the same dimensions of the value vector causes indeterminacy in their independent identification, hindering training scalability. To address this, we propose Decoupled Pose Positional Encoding (DPPE), a novel camera-based positional encoding that explicitly decouples rotation and translation. Extensive evaluations on NVS tasks demonstrate that DPPE enables stable long-term training even in scaled-up training setup. Furthermore, it exhibits superior generalization performance in extrapolation settings, such as handling an increased number of viewpoints and zoom-in scenarios.

</details>

#### 2026-06-30 - AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings

**Authors:** Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno
**Links:** [abs](https://arxiv.org/abs/2606.31556) - [pdf](https://arxiv.org/pdf/2606.31556)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, radiance field, Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings
- 作者：Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno
- 出版日期：2026-06-30T12:12:21Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.31556

### 一句话总结
AugSplat 利用神经辐射场合成新视角图像，为稀疏视图下的高斯泼溅优化提供辅助监督，从而在不牺牲实时渲染速度的前提下提升新视角合成质量。

### 研究问题
在稀疏视图场景中，标准高斯泼溅（Gaussian Splatting）因对初始几何质量高度敏感，易产生不完整或噪声点云，导致重建质量不佳。而神经辐射场虽能从有限观测恢复稳健几何，但计算成本高、推理慢。现有方法难以同时满足高重建质量和实时渲染。

### 核心思路/方法
1. **阶段一（视图扩充）**：先在稀疏输入视图上训练一个神经辐射场（radiance field），并利用它从附近的虚拟视角合成额外图像，以增加有效视角覆盖范围。
2. **阶段二（辅助监督）**：将合成视图作为辅助监督信号，用于高斯泼溅优化过程。提出了两种变体：
   - **Staged AugSplat**：先仅使用合成视图进行初始优化阶段，然后切换到真实图像继续优化。
   - **Dual AugSplat**：在训练全程同时使用真实图像和合成视图，并对合成视图的损失权重进行衰减。

### 主要贡献
1. 提出一种简单框架，利用辐射场合成的视图来增强高斯泼溅在稀疏视图下的优化效果，无需修改基础高斯泼溅管线。
2. 设计了两种互补的优化策略（分阶段训练与联合训练），并在稀疏视图的 mip-NeRF 360 场景上验证了有效性。
3. 在提升重建质量的同时，推理时仍保持实时渲染速度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法针对稀疏视图场景下的高斯泼溅优化问题提出了一个实用且简洁的增强策略（辐射场视图增强），思路清晰且实验初步显示有效。但由于摘要未提供详细的定量对比、消融实验或与最新基线的比较，对于需要深入了解其实际性能效益的读者可能不够充分。适合对稀疏视图渲染或高斯泼溅加速感兴趣的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Generating high-quality novel views at real-time frame rates remains a central challenge in 3D vision, particularly in sparse-view scenarios. Neural radiance fields have demonstrated robust reconstruction from limited observations, but their reliance on volumetric rendering leads to high computational cost and slow inference. In contrast, Gaussian Splatting methods achieve real-time rendering through rasterization, but their optimization is highly sensitive to the quality of the initial geometry. This sensitivity becomes especially problematic in sparse-view settings, where limited observations often lead to incomplete or noisy point-cloud reconstructions. In this work, we present AugSplat, a simple framework for improving Gaussian Splatting in sparse-view regimes using radiance-field-based view augmentation. We first train a radiance field on the sparse input views and use it to synthesize additional images from nearby novel viewpoints, increasing the effective view-space coverage available for supervision. These synthetic views are then used as auxiliary supervision during Gaussian Splatting optimization. We study two variants: Staged AugSplat, which uses synthetic views for an initial optimization phase before switching to real images, and Dual AugSplat, which jointly trains on real and synthetic views with a decaying synthetic loss weight. Experiments on sparse-view mip-NeRF 360 scenes show that AugSplat improves reconstruction quality over standard Gaussian Splatting. Staged AugSplat achieves the strongest average performance, while Dual AugSplat provides a closely performing formulation that keeps real-image supervision active throughout training, and both variants preserve real-time rendering at inference.

</details>

#### 2026-06-30 - WarpHammer: Densifying Scene Warps with 3D Object Priors for Extreme View Synthesis

**Authors:** Michael Green, Gavriel Habib, Dvir Samuel, Tal Berkovitz Shalev, Issar Tzachor, Rami Ben-Ari, Or Litany
**Links:** [abs](https://arxiv.org/abs/2606.31258) - [pdf](https://arxiv.org/pdf/2606.31258)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** geometry foundation model, 3D reconstruction, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WarpHammer: 通过3D物体先验稠密化场景扭曲以实现极端视角合成
- 作者：Michael Green, Gavriel Habib, Dvir Samuel, Tal Berkovitz Shalev, Issar Tzachor, Rami Ben-Ari, Or Litany
- 出版日期：2026-06-30
- 分类：神经场景表示与渲染
- 链接：https://arxiv.org/abs/2606.31258

### 一句话总结
WarpHammer是一个无需训练的框架，通过使用3D生成先验（如SAM3D）对场景扭曲进行显式3D物体重建增强，解决了极端视角下投影条件新视角合成（NVS）的稀疏和伪影问题，并能融合来自外部源的辅助物体视图。

### 研究问题
如何解决投影条件新视角合成（NVS）在大视角轨道运动下的失效模式，即扭曲变得稀疏、隐藏表面占据主导、出现镜面伪影，导致生成器丢失像素内容和隐式相机线索。

### 核心思路/方法
- 核心方法：在现有NVS管线基础上，通过一个本原的3D生成先验（如SAM3D）获得待观察物体的显式3D重建，然后用该重建物体增强扭曲场景：为前景添加缺失表面，并遮挡那些在新视角下不应可见的背景点。
- 辅助视图融合：使用预训练的多视图几何基础模型，将参考图像和外部辅助图像（如汽车快照与同车型厂商摄影图）联合处理，预测统一点云并融合到物体3D重建中，从而获得比单图像重建更精确的几何，且无需用户提供辅助视图的相机位姿。
- 该框架无需微调基础模型，完全无训练。

### 主要贡献
1. 提出WarpHammer，一种无需训练的方法，通过显式3D物体重建增强扭曲场景，有效解决极端视角下NVS在物体周围的稀疏和伪影问题，恢复外观和相机线索。
2. 首次实现场景级NVS方法自然融合来自外部源且位姿未知的辅助物体视图，显著提升几何保真度。
3. 在五个基准评测中，WarpHammer在强基线方法失效的大视角偏差下仍能生成稳定新视角。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对现有NVS在极端视角下的核心故障模式提出创新性解决方案，并实现了无需训练的外部多视图融合，在方法上具有显著突破性，且实验验证于多个基准，对神经渲染和视角合成领域的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Projection-conditioned novel view synthesis (NVS) warps an explicit 3D reconstruction of the input view into the target camera and conditions a generator on the warped rendering. This works well for small viewpoint changes but degrades sharply under large orbital motion: the warp becomes sparse around the orbited object, where hidden surfaces dominate the new view and mirror-like artifacts emerge, causing the generator to lose both pixel content and the implicit camera cue carried by the warp. We introduce WarpHammer, a training-free framework that resolves this failure mode by augmenting the warped scene with an explicit 3D reconstruction of the object obtained from a native 3D generative prior (e.g., SAM3D). The reconstructed object adds missing foreground surfaces and occludes background points that should no longer be visible, restoring both appearance and camera cues without fine-tuning the base model. The same explicit object representation further unlocks a capability current NVS pipelines do not support: incorporating auxiliary views of the object from sources outside the target scene, for example, a casual snapshot of a car paired with a manufacturer studio shot of the same model. We process the reference and auxiliary images jointly with a pretrained multi-view geometry foundation model, which predicts a unified point cloud that we fuse into the 3D object reconstruction. This yields substantially more faithful geometry than single-image reconstruction, without requiring user-provided camera poses for the auxiliary views. On five benchmarks, WarpHammer produces stable novel views at viewpoint deviations where strong baselines collapse, and is the first scene-level NVS method that can naturally fuse auxiliary, pose-unknown object views from an external source.

</details>

#### 2026-06-30 - Diffusion-Based Material Regularization for Physics-Based Inverse Rendering

**Authors:** Jingwang Ling, Lifan Wu, Feng Xu, Shuang Zhao
**Links:** [abs](https://arxiv.org/abs/2606.31065) - [pdf](https://arxiv.org/pdf/2606.31065)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Diffusion-Based Material Regularization for Physics-Based Inverse Rendering
- 作者：Jingwang Ling, Lifan Wu, Feng Xu, Shuang Zhao
- 出版日期：2026-06-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.31065

### 一句话总结
本文提出一种将扩散模型输出作为相似性核、约束优化材料参数的损失函数，以弥补物理逆渲染与数据驱动方法之间的差距，实现高质量几何、材质和光照联合重建。

### 研究问题
如何将物理精确的逆渲染与数据驱动的扩散先验有效结合，解决物理逆渲染中因缺乏强先验而导致的材质与光照耦合、泛化性差的问题。

### 核心思路/方法
核心思想是将扩散模型预测值视为一个相似性核（similarity kernel）：当扩散模型对表面某区域的预测结果近似恒定时，引入正则化损失，惩罚优化材质偏离该恒定值；而在其他区域，优化过程可自由匹配输入图像。通过该正则化器，构建端到端管线联合重建几何、材质和光照。

### 主要贡献
1. 提出一种新型正则化损失，将扩散模型输出用作相似性核，而非直接作为目标材质值，从而平衡了物理逼真度与数据先验。
2. 构建完整的端到端重建管线，能够联合输出可在标准渲染管线中直接使用、并支持可信重新光照的3D资产。
3. 在Synthetic4Relight、Stanford-ORB和DTC-Synthetic三个数据集上，重建精度和重光照质量均显著优于现有基线方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对物理逆渲染长期存在的欠约束问题提出了创新性解法，在多个基准上实现显著提升，且应用场景（3D资产重建与重光照）在计算机图形学和视觉领域具有高度实用性。摘要表述清晰，方法动机明确，实验结果积极，值得深入阅读。

</details>

<details>
<summary>Abstract</summary>

Reconstructing physics-based 3D assets -- geometry, materials, and illumination -- from multi-view images is a core problem in computer graphics and vision, and a prerequisite for realistic relighting and editing. Physics-based inverse rendering offers an accurate image-formation model, but is severely underconstrained: without strong priors, illumination is baked into materials, and reconstructions generalize poorly to novel views and lighting. Data-driven diffusion models, in contrast, predict visually plausible materials, yet their predictions rarely satisfy the rendering equation and are not directly usable for physics-based rendering. We bridge these two paradigms rather than replacing either. Our key idea is to treat the predictions of a state-of-the-art diffusion model not as target material values but as a similarity kernel for optimization: we introduce a regularization loss that penalizes deviations in the optimized material over surface regions where the diffusion predictions are near-constant, while leaving the optimization free to match the input images. Built on this regularizer, our end-to-end pipeline jointly reconstructs geometry, materials, and illumination, yielding high-quality assets that drop into standard rendering pipelines and relight faithfully. On the Synthetic4Relight, Stanford-ORB, and DTC-Synthetic datasets, our method significantly outperforms state-of-the-art baselines in both reconstruction accuracy and relighting quality.

</details>

#### 2026-06-30 - Learning Video Dynamics with Predictive Differentiable Rendering

**Authors:** Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun
**Links:** [abs](https://arxiv.org/abs/2606.31050) - [pdf](https://arxiv.org/pdf/2606.31050)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Video Dynamics with Predictive Differentiable Rendering
- 作者：Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun
- 出版日期：2026-06-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.31050

### 一句话总结
该论文提出一种名为预测可微渲染（PDR）的视频预测新范式，通过将离散像素空间预测转化为连续高斯表示，并引入轻量级适配器和加速渲染器，显著提升了预测的细节保真度和视觉质量。

### 研究问题
现有确定性视频预测模型在离散像素空间操作，使用均方误差（MSE）损失会导致预测结果过度平滑、缺乏精细的视觉细节，即如何精准预测高保真未来世界的问题。

### 核心思路/方法
1. 提出PredGS，一种基于2D高斯表示的轻量级即插即用适配器，可无缝集成到现有像素空间预测器中，在极低计算开销下保留空间细节。
2. 开发predgsplat，一种支持任意通道的CUDA加速可微2D高斯渲染器，每个高斯由5+C个可学习参数定义，渲染速度比基线快10倍。
3. 采用L1和SSIM联合损失替代传统MSE损失，克服模糊倾向，提升预测性能。

### 主要贡献
- 提出预测可微渲染（PDR），一种连接离散和连续表示的新型端到端视频预测范式。
- 设计PredGS适配器和predgsplat加速渲染器，实现高效的细节保留与快速渲染。
- 在TaxiBJ、WeatherBench、KTH、Human3.6M等多个真实世界基准上，PDR在细节保留、视觉保真度和预测精度上一致超越现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该论文提出了一种全新的预测范式，结合3D高斯溅射的进展和可微渲染，在多个基准上取得显著提升，且方法具有轻量级和即插即用的特性，对视频预测和神经渲染领域有较强的创新性和实用性。

</details>

<details>
<summary>Abstract</summary>

How to accurately predict a high-fidelity future world? While the visual world is inherently continuous, existing deterministic video prediction models operate in discrete pixel space and are mainly optimized with pixel-wise mean squared error (MSE), which often leads to over-smoothed predictions and a lack of fine-grained visual details. To address these limitations, we propose Predictive Differentiable Rendering (PDR), a novel end-to-end video prediction paradigm that bridges the gap between discrete and continuous representations. Inspired by recent progress in 3D reconstruction with 3D Gaussian Splatting, we introduce PredGS, a lightweight and plug-and-play adapter based on 2D Gaussian representation, which could be seamlessly integrated with existing pixel space predictors, significantly improving spatial detail preservation with negligible computational overhead. Furthermore, we develop predgsplat, a CUDA-accelerated differentiable 2D Gaussian renderer supporting arbitrary channels. Each Gaussian is defined by 5 + C learnable parameters (position, scale, rotation, and C channel amplitudes) and achieves up to 10x faster rendering than the baseline. Optimized by a combined L1 and SSIM loss, PDR overcomes the inherent blurring tendencies of MSE Loss, significantly enhancing the prediction performance. Extensive experiments on diverse real-world benchmarks, including TaxiBJ, WeatherBench, KTH, and Human3.6M, demonstrate that PDR consistently surpasses existing methods, delivering superior detail preservation, visual fidelity, and predictive accuracy.

</details>

#### 2026-06-29 - GRay: Ray Tracing 3D Gaussians Near the Speed of Splats

**Authors:** Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2606.30869) - [pdf](https://arxiv.org/pdf/2606.30869)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GRay: Ray Tracing 3D Gaussians Near the Speed of Splats
- 作者：Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis
- 出版日期：2026-06-29
- 分类：神经场景表示与渲染
- 链接：[摘要](https://arxiv.org/abs/2606.30869) | [PDF](https://arxiv.org/pdf/2606.30869)

### 一句话总结
GRay提出一种基于光线追踪的3D高斯渲染方法，通过利用算法差异和密集初始化优势，大幅缩短优化时间，在速度上接近主流光栅化方法3DGS。

### 研究问题
如何解决3D高斯光线追踪（3DGRT）优化速度慢（比光栅化方法3DGS慢近一个数量级）的问题，使其在保持质量的同时达到与光栅化相当的渲染与优化速度。

### 核心思路/方法
- 利用光线追踪与光栅化的算法差异：光线追踪只评估被光线“实际相交”的高斯，在基元数量上具有对数级缩放潜力，而非光栅化的线性缩放。
- 发现并利用“密集初始化”效应：密集初始化会生成大量小高斯，这会拖慢光栅化渲染，但反而能加速光线追踪；GRay专门设计来利用这一特性。
- 实现快速渲染与优化：相比3DGRT，GRay渲染速度提升近4倍，优化速度提升近10倍；与3DGS速度竞争，但质量略低。

### 主要贡献
1. 提出GRay，一种快速3D高斯光线追踪器，显著缩小了与3DGS光栅化渲染的速度差距。
2. 揭示了光线追踪在密集高斯场景下的对数级缩放优势，以及密集初始化对光栅化与光线追踪速度的相反影响。
3. 实验表明GRay在几乎相同的质量下，渲染速度比3DGRT快4倍，优化速度快10倍。

### 局限性
摘要未提供足够信息。摘要未讨论方法的缺点或限制，也未说明在哪些场景下质量可能下降。

### 阅读优先级
**高**  
理由：该研究直接针对神经渲染领域的关键效率问题（3DGS光栅化速度与光线追踪质量间的权衡），提出了有效加速方案，代码已开源，对从事场景表示、实时渲染及相关应用的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) is a popular representation for radiance field reconstruction, distinguished by the rendering speed of its rasterization-based renderer. While 3D Gaussians can also be ray traced, this approach has so far been slower, with 3D Gaussian Ray Tracing (3DGRT) taking nearly one order of magnitude longer to optimize. To address this, we present GRay, a fast ray tracer for 3D Gaussians designed to close this performance gap and match 3DGS's speed. Our method leverages the algorithmic difference between both approaches: unlike rasterization, ray tracing evaluates only Gaussians that are actually intersected by a ray, leading to potentially logarithmic--rather than linear--scaling in the number of primitives. This property allows ray tracing to better exploit dense scenes composed of numerous tiny Gaussians, a configuration which has largely been overlooked. Notably, we show that dense initialization--which creates many small Gaussians--slows down rasterization, but instead speeds up ray tracing. Designed to leverage this effect, GRay renders nearly 4x faster and optimizes nearly 10x faster than 3DGRT while maintaining similar quality, and has competitive speed with 3DGS albeit at somewhat lower quality. Code is available at https://repo-sam.inria.fr/nerphys/gray.

</details>

#### 2026-06-29 - Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields

**Authors:** Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2606.30861) - [pdf](https://arxiv.org/pdf/2606.30861)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, scene representation, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields
- 作者：Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis
- 出版日期：2026-06-29
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.30861

### 一句话总结
提出一种基于光线追踪高斯溅射的辐射场方法，通过分离漫反射与镜面反射组件，实现对捕捉场景中镜面反射的实时编辑（如多弹射反射、粗糙度调整等）。

### 研究问题
如何正确重建反射器与被反射物体的几何与材质，使辐射场中的镜面反射具有物理一致性并可编辑，而非仅用“虚假”反射几何模拟。

### 核心思路/方法
1. 利用基于学习的方法从输入照片中提取漫反射与镜面反射缓冲，以及几何和BRDF缓冲。
2. 优化场景的漫反射版本，并通过路径追踪高效生成基于物理的镜面反射。
3. 设计专门的训练方法确保上述过程收敛。
4. 提出针对3D高斯基元的快速光线追踪算法，实现高效的多弹射反射。

### 主要贡献
- 提出一种可编辑的物理基镜面反射表示方法，重建反射器与反射物体（包括输入图像中未见的物体）。
- 支持实时、一致地编辑捕捉场景的镜面反射，包括多弹射效果和粗糙度变化。
- 在合成场景中使用真值缓冲展示主要结果，并在真实场景中展示基于当前不完美学习缓冲的初步结果。

### 局限性
摘要未明确说明局限性，但提及在真实场景中仅展示了初步结果，且依赖的学习缓冲目前尚不完美。此外，实验细节（如性能指标、基准对比等）未在摘要中提供。

### 阅读优先级
高。理由：辐射场中真实反射的可编辑是计算机视觉与图形学的关键挑战，该方法提出了结合物理基渲染与实时编辑的新思路，且代码已公开，对相关领域研究人员具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Radiance fields such as 3D Gaussian Splatting allow real-time rendering of scenes captured from photos. They also reconstruct most specular reflections with high visual quality, but typically model them with "fake" reflected geometry, using primitives behind the reflector. Our goal is to correctly reconstruct the reflector and the reflected objects such as to make specular reflections editable. We present a proof of concept which exploits promising learning-based methods to extract diffuse and specular buffers from photos, as well as geometry and BRDF buffers. Our method builds on three key components. First, by using diffuse and specular buffers of input training views, we optimize a diffuse version of the scene and use path tracing to efficiently generate physically based specular reflections. Second, we present a specialized training method that allows this process to converge. Finally, we present a fast ray tracing algorithm for 3D Gaussian primitives that enables efficient multi-bounce reflections. Our method reconstructs reflectors and reflected objects, including those not seen in the input images, in a unique scene representation. Our solution allows real-time, consistent editing of captured scenes with specular reflections, including multi-bounce effects, changing roughness, and more. We mainly show results using ground truth buffers from synthetic scenes, and also preliminary results in real scenes with currently imperfect learning-based buffers. Code and data are available at: https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections/

</details>

#### 2026-06-29 - GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping

**Authors:** Annika Thomas, Mason Peterson, Jonathan P. How
**Links:** [abs](https://arxiv.org/abs/2606.30809) - [pdf](https://arxiv.org/pdf/2606.30809)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussLite: 用于实时机器人建图的任务条件化在线3D高斯泼溅
- 作者：Annika Thomas, Mason Peterson, Jonathan P. How
- 出版日期：2026-06-29
- 分类：神经场景表示与渲染；具身/机器人/AR应用
- 链接：https://arxiv.org/abs/2606.30809

### 一句话总结
GaussLite提出了一种任务驱动的3D高斯泼溅（3DGS）建图系统，根据自然语言任务描述动态分配表示资源，在有限计算资源下实现实时建图，并在感兴趣区域（ROI）质量上显著超越基线。

### 研究问题
如何让3D高斯泼溅建图系统根据机器人下游任务（如抓取物体）的需求，在线动态分配表示容量，避免对无关场景区域的浪费，从而在实时性和计算资源受限的条件下提升任务相关区域的建图质量。

### 核心思路/方法
1.  **任务解析与语义接地**：利用一次性大语言模型（LLM）解析器从自然语言任务（如“准备捡起桌子上的物体”）中提取目标物体和参考物体。
2.  **在线兴趣区域生成**：通过开放词汇检测器对每一帧RGB-D图像进行检测和分割，生成逐像素的任务相关性掩码，实现实时兴趣区域确定。
3.  **基于任务相关性的资源分配**：建图器根据任务相关性掩码，动态控制高斯原语的播种密度、梯度流动和缩放参数，使得计算资源集中在任务关键区域。
4.  **多智能体地图融合**：通过逐体素的活跃优化计数投票，在实时条件下将多个任务特化智能体的地图融合为单一共享地图，优于简单拼接。

### 主要贡献
- 提出了一种任务条件化的在线3DGS建图框架，能够根据自然语言指令动态分配表示容量。
- 在Replica数据集和真实硬件演示（室内外场景）中，在相同高斯预算和实时建图（4Hz）条件下，任务区域PSNR分别比基线平均高+2.72 dB和+2.23 dB。
- 实现了多智能体地图的实时融合策略，通过体素投票共享仅7.08%的地图，融合后PSNR比简单拼接高+3.42 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
**理由**：该工作针对机器人实时建图的实际需求，创新性地将3DGS与任务驱动语义结合，解决了计算资源分配的关键瓶颈。实验结果（ROI PSNR提升2-3 dB）和实时性（4 Hz）在资源受限硬件上表现突出，且提供了多智能体融合方案，对具身智能和机器人应用方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing 3D Gaussian Splatting (3DGS) systems distribute representation capacity uniformly across a scene, ignoring the fact that many downstream robotic tasks engage only a fraction of the reconstructed geometry. This causes valuable onboard compute to be allocated towards optimizing irrelevant parts of the scene, either limiting online capacity or under-optimizing the most relevant parts of the scene. We introduce GaussLite, a task-driven 3DGS mapping system that conditions its representation density on a natural-language task specification. Given a posed RGB-D stream and a task such as "prepare to pick up the object on the desk," GaussLite uses a one-shot LLM parser to extract target and anchor objects, which are grounded per-frame by an open-vocabulary detector and segmented to produce per-pixel relevance masks in real time. The mapper allocates seeding density, gradient flow and scaling by task relevance. At matched Gaussian budget and real-time mapping at 4 Hz on resource-constrained hardware, GaussLite outperforms baselines on ROI PSNR on the Replica Dataset by an average +2.72 dB and on a real-hardware demonstration in indoor and outdoor settings by +2.23 dB. We further show that two task-specialized agents' maps can be fused into a single shared map via per-voxel voting on active-optimization counts in real time, outperforming concatenation by +3.42 dB while only sharing an average 7.08% of the map.

</details>

#### 2026-06-29 - VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes

**Authors:** Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu
**Links:** [abs](https://arxiv.org/abs/2606.30645) - [pdf](https://arxiv.org/pdf/2606.30645)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes
- 作者：Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu
- 出版日期：2026-06-29T17:59:55Z
- 分类：神经场景表示与渲染；具身/机器人/AR应用
- 链接：摘要URL: https://arxiv.org/abs/2606.30645；PDF: https://arxiv.org/pdf/2606.30645

### 一句话总结
该论文提出一个通过合成交互数据来训练人形机器人全身运动策略的框架，利用三维高斯喷溅重建场景，生成视觉-语言-运动学配对数据，并在真实机器人上验证其有效性。

### 研究问题
如何获取大规模、同步的自我中心视觉、语言指令和机器人兼容运动学轨迹数据，以训练感知驱动的人形机器人全身定位-操作策略。

### 核心思路/方法
1. **数据生成流水线**：使用三维高斯喷溅技术重建公制尺度室内场景；利用场景特权信息合成导航和物体交互轨迹；事后渲染配对的自我中心观察。该流水线无需人工干预生成48,000个配对轨迹。
2. **策略训练**：训练一个视觉-语言-运动学策略，预测短时程的全身运动学轨迹。
3. **执行与迁移**：通过全身轨迹跟踪器将预测转化为真实人形机器人的动作，并最终在物理Unitree G1机器人上进行评估。

### 主要贡献
- 提出一个无需人工干预的合成数据生成流水线，利用重建场景构建视觉-语言-运动学配对数据，解决了数据瓶颈问题。
- 在物理Unitree G1机器人上成功展示了基于视觉的导航和单物体运输任务，证明了合成交互数据对基于感知的仿真到现实人形定位-操作的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。
理由：该论文针对人形机器人感知控制中的数据稀缺这一关键瓶颈，提出一个创新性的合成数据生成框架，并结合完整的训练与真实部署验证流程。研究内容对机器人和神经渲染交叉领域具有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Perception-based humanoid loco-manipulation requires connecting egocentric observations and task instructions to whole-body motion. Learning this mapping requires synchronized egocentric images, language commands, and robot-compatible kinematic trajectories, yet no existing data source provides this complete tuple at scale. We address this bottleneck by generating vision-language-kinematics (VLK) supervision synthetically in reconstructed scenes. Our pipeline leverages 3D Gaussian Splatting to reconstruct metric-scale indoor environments, synthesizes navigation and object-interaction trajectories using privileged scene information, and renders paired egocentric observations after the fact. We produce 48,000 paired trajectories with no human intervention and train a VLK policy that predicts short-horizon whole-body kinematic trajectories. A whole-body tracker converts these predictions into actions on the physical humanoid. We evaluate on the physical Unitree G1 performing navigation and single-object transport, demonstrating that synthesized interactions in reconstructed scenes provide effective supervision for sim-to-real perception-based humanoid loco-manipulation. Project Website: https://vision-language-kinematics.github.io/

</details>

#### 2026-06-29 - Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors

**Authors:** Jameel Hassan, Yasiru Ranasinghe, Vishal Patel
**Links:** [abs](https://arxiv.org/abs/2606.30638) - [pdf](https://arxiv.org/pdf/2606.30638)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, rendering, splatting, embodied AI

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors
- 作者：Jameel Hassan, Yasiru Ranasinghe, Vishal Patel
- 出版日期：2026-06-29
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.30638

### 一句话总结
本文提出GaussDet方法，利用开放词汇的2D目标检测器为3D高斯场景实现零样本的开放词汇分割和指代表达式定位，避免了传统方法对稠密CLIP特征的依赖。

### 研究问题
现有基于3D高斯泼溅的开放词汇理解方法存在两个问题：1) 实例分组机制需要预定义实例数量或受噪声影响；2) 依赖CLIP特征限制了语义理解，无法处理复杂的指代表达式地面定位。

### 核心思路/方法
1. 利用具备指代表达能力、开放词汇的2D目标检测器，替代传统的稠密CLIP特征蒸馏。
2. 为每个3D高斯学习实例特征，从而将场景分解为3D实例组。
3. 渲染这些实例组，并从多视角2D检测结果中聚合语义投票，为每个3D实例生成视图聚合语义标签分布（VASD）。该分布作为强正则化器，抑制低质量实例分组带来的虚假标签。

### 主要贡献
1. 提出GaussDet方法，实现了从简单语言查询到复杂指代表达式定位的零样本扩展。
2. 在开放词汇分割（LeRF-OVS、ScanNet数据集）和指代表达式地面定位（Ref-LeRF数据集）两个任务上，均取得优于现有方法的一致性改进。
3. 在严格的零样本设置下，指代表达式定位的mIoU提升达16.7%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法针对特定任务（3D高斯场景的开放词汇与指代分割）有显著性能提升，且关键设计（利用2D检测器替代CLIP）具有启发性。但该方法不涉及通用计算机视觉或新范式突破，适合该方向的从业者阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their bottom-up grouping strategies. Furthermore, the reliance on CLIP restricts semantic understanding to simple noun phrases, preventing complex spatial reasoning and referential expression grounding. We present GaussDet, a method that circumvents the need for dense CLIP features by leveraging discrete, open-vocabulary 2D object detectors with referring expression capabilities. We learn instance features for individual Gaussians to decompose the scene into 3D instance groups. By rendering these groups and aggregating semantic votes from multi-view 2D detections, we generate a robust View-Aggregated Semantic Label Distribution (VASD) for each 3D instance. This view-aggregation strategy acts as a strong regularizer, attenuating spurious labels caused by low-quality instance grouping. Our approach enables a straightforward, zero-shot extension from simple language queries to complex referential grounding. Extensive evaluations across two key tasks -- open-vocabulary segmentation (LeRF-OVS, ScanNet) and referring expression grounding (Ref-LeRF) -- demonstrate that GaussDet achieves consistent improvements over existing methods. Most notably, we achieve a substantial 16.7% mIoU improvement in referential grounding within a strict zero-shot setting.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

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

#### 2026-06-30 - MV-GEL: Language-Driven Multi-View Geometric Entity Localization on Meshes

**Authors:** Kartik Bali, Roland Aydin
**Links:** [abs](https://arxiv.org/abs/2606.31533) - [pdf](https://arxiv.org/pdf/2606.31533)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MV-GEL: Language-Driven Multi-View Geometric Entity Localization on Meshes
- 作者：Kartik Bali, Roland Aydin
- 出版日期：2026-06-30
- 分类：Embodied / Robotics / AR Applications
- 链接：[Abstract](https://arxiv.org/abs/2606.31533) / [PDF](https://arxiv.org/pdf/2606.31533)

### 一句话总结
MV-GEL提出一个多视角框架，通过语言查询在三维多边形网格上定位细粒度几何实体（如面、边），核心是使用一个提示条件化的视图排名模块选择最能清晰呈现目标实体的视角。

### 研究问题
如何从自然语言查询中，在三维多边形网格上准确、鲁棒地定位精细的几何实体（例如边、平面区域、曲面），解决单视角下因遮挡或透视导致的观测不充分问题。

### 核心思路/方法
1. **GELviews排名模块**：基于语言提示，对候选视图进行评估，优先选择能使查询实体最大可观测的视角。
2. **VLM推理分割**：对选出的最佳视图，使用视觉语言模型（VLM）进行推理，生成二维分割掩码。
3. **几何感知光线投射**：将二维掩码通过光线投射映射回三维网格，获得目标实体在网格上的定位。

### 主要贡献
- 提出MV-GEL框架，实现从自然语言到三维网格几何实体的定位。
- 引入GELviews模块，利用语言提示主动选择最优观测视角，提升定位可靠性。
- 在面级IoU上提升高达1.7倍，边级F1上提升超过4.5倍，显著优于CLIP和随机视角基线，尤其对薄、视角敏感的结构有效。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作解决了语言驱动三维几何实体定位这一新兴且具挑战性的问题，方法创新（视角排名模块），性能提升显著（边级F1超4.5倍），并开源了代码和模型，对计算机辅助设计、机器人操控等领域有直接应用价值。

</details>

<details>
<summary>Abstract</summary>

Identifying and grounding precise geometric entities, such as edges, planar regions, and curved surfaces within 3D objects, is foundational to computer-aided design (CAD), robotic manipulation, and scientific simulation. Although modern Vision Language Models (VLMs) have advanced referring segmentation (RIS) in the image domain, extending such language-driven localization to structured 3D geometry is substantially harder. The 3D object appearance is highly sensitive to viewpoints; a single perspective may render a target entity clearly observable, while another may suffer from severe occlusion or foreshortening. In this work, we attempt to solve these challenges with MV-GEL (Multi-View Geometric Entity Localization), a framework for localizing fine-grained geometric entities on polygon meshes from natural language queries. Our key insight is that reliable CAD entity (i.e., faces, edges or solids) localization depends on selecting views that make the queried entity maximally interpretable. We introduce GELviews, a prompt-conditioned ranking module that prioritizes viewpoints based on language prompted observability of geometric CAD entities. Selected views are processed by a VLM-based reasoning segmentation backbone, and predicted masks are lifted to the corresponding meshes via geometry-aware ray casting. Our framework is completely CAD agnostic and relies only on 3D meshes. Experiments show up to a 1.7X improvement in face-level IoU and over 4.5X gains in edge-level F1 compared to vanilla baselines, substantially outperforming CLIP-based and random view sampling, particularly for thin and view-sensitive structures.The dataset, code and trained checkpoints are available at https://github.com/kbali1297/MV-GEL.

</details>

#### 2026-06-29 - Knowledge-Driven Dimension Estimation from a Single Image -3D Asset Generation Technology for Digital Twin Construction

**Authors:** Hidenori Sakaniwa, Akihito Akai, Akihiko Hyodo
**Links:** [abs](https://arxiv.org/abs/2606.30896) - [pdf](https://arxiv.org/pdf/2606.30896)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Knowledge-Driven Dimension Estimation from a Single Image -3D Asset Generation Technology for Digital Twin Construction
- 作者：Hidenori Sakaniwa, Akihito Akai, Akihiko Hyodo
- 出版日期：2026-06-29T20:35:54Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接: https://arxiv.org/abs/2606.30896；PDF链接: https://arxiv.org/pdf/2606.30896

### 一句话总结
本文提出一种知识驱动的单目图像尺度估计方法，通过分解物体结构并集成设计规则等外部知识，估计各组件尺寸并生成3D资产，以提升自动驾驶虚拟验证中摄像机识别性能。

### 研究问题
如何从单目图像准确估计高空交通标志等难以通过LiDAR或立体相机测距的物体的真实尺度，以减少虚拟与真实环境间物体尺度差异导致的摄像机识别性能下降。

### 核心思路/方法
1. **结构分解**：将目标物体分解为多个结构元素。
2. **知识集成**：融入设计规则、几何关系及常规尺寸等外部知识。
3. **尺寸估计**：从单目图像检测每个组件，结合结构关系和周围元素的尺寸一致性，估算各组件尺寸。
4. **3D资产生成**：利用估计的组件重建物体3D资产，使其尺度逼近真实环境，并部署至数字孪生空间。

### 主要贡献
- 提出一种基于外部知识驱动的单目图像尺度估计方法，解决了高空交通标志等物体的尺寸估算难题。
- 方法可生成尺度与真实环境近似的3D资产，服务于数字孪生构建。
- 有望提升自动驾驶虚拟环境中车载摄像头的验证准确性。

### 局限性
摘要未提供足够信息。未提及方法的失败案例、对复杂物体的适用性、计算开销或对特定知识库的依赖程度等局限性。

### 阅读优先级
高。理由：该方法直接针对自动驾驶虚拟验证中的关键尺度不一致问题，结合知识驱动与单目估计，具有实际应用潜力；摘要清晰阐述了问题、方法与应用场景，且发表于较新日期（2026年），对从事数字孪生、自动驾驶仿真或三维重建的研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

In the verification of in-vehicle cameras, simulation technology using virtual spaces has advanced, enabling pre-evaluation of false detections and missed detections in various scenarios. However, discrepancies in the scale of the object being verified between the virtual and real environments can lead to a decrease in camera recognition performance. For traffic signs installed at high altitudes, distance measurement using LiDAR or stereo cameras is difficult, requiring size estimation from monocular images. This paper proposes a method for estimating the scale of an object by decomposing it into multiple structural elements and integrating external knowledge regarding design rules, geometric relationships, and conventional dimensions. Specifically, this method detects each component from a monocular image and estimates the size of each component by considering its structural relationships and dimensional consistency with surrounding elements. Furthermore, it generates a 3D asset of the object by reconstructing the estimated components. This method makes it possible to place 3D assets with a scale approximating the real environment within a digital twin space and is expected to contribute to improving the verification accuracy of in-vehicle cameras for autonomous driving in virtual environments.

</details>

#### 2026-06-29 - UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image

**Authors:** Mohamed el Amine Boudjoghra, Ivan Laptev, Angela Dai
**Links:** [abs](https://arxiv.org/abs/2606.30608) - [pdf](https://arxiv.org/pdf/2606.30608)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image
- 作者：Mohamed el Amine Boudjoghra, Ivan Laptev, Angela Dai
- 出版日期：2026-06-29
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.30608

### 一句话总结
本文提出一种基于辩论驱动的智能体方法，利用视觉-语言和视频模型的先验知识，从文本或单张图像零样本恢复完整的铰接式3D物体的几何、内部结构和运动状态。

### 研究问题
如何从稀疏的观察（如文本或单张图像）中，在没有监督数据或先验的情况下，可靠地重建铰接式3D物体的结构、运动以及被遮挡的内部几何。

### 核心思路/方法
该方法采用“辩论驱动”的多智能体框架：
1. **高层智能体**：利用视觉-语言模型和视频模型推理物体的语义和运动。
2. **低层智能体**：估计铰接参数和交互点。
3. **两轮结构化辩论**：第一轮利用全局-局部不一致性进行辩论；第二轮将智能体的推理锚定在自由生成的视频中。
4. **视频先验驱动**：基于达成一致的铰接结果，利用视频生成先验驱动每个部件运动，从而暴露单张静态视图无法推断的遮挡内部和几何结构。

### 主要贡献
- 首次提出辩论驱动的方法，从文本或图像输入实现铰接式3D物体的零样本重建。
- 通过结合智能体推理与视频生成先验，联合推断铰接关系并重建完整的3D物体，包括高保真几何、内部结构和运动一致的状态。
- 方法不依赖监督数据，能够恢复超出直接观测表面的隐藏几何信息。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法在零样本、无监督条件下解决了铰接式3D重建的核心难题（遮挡、内部结构推断），且创新性地引入了辩论机制和视频先验，对具身AI、机器人、虚拟现实领域的研究有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging. Existing approaches remain largely constrained by lack of supervised data or lack the priors needed to reliably recover articulation, hidden geometry, and internal object structure. We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry revealed under articulation. High-level agents reason about object semantics and motion using knowledge from vision-language and video models, while low-level agents estimate articulation parameters and interaction points; together, they engage in a two-round structured debate that first exploits global--local disagreement and then grounds the agents in freely generated video. The same video prior, conditioned on the agreed articulation, then drives each part through its motion to expose occluded interiors and geometry that cannot be inferred from a single static view. By combining agentic reasoning with a video generative prior, our approach jointly infers articulation and reconstructs complete 3D articulated objects, producing high-fidelity geometry, internal structure, and motion-consistent states beyond directly observed surfaces.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
