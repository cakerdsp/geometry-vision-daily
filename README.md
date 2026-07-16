# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：54
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 21
  - Neural Scene Representations & Rendering: 14
  - Embodied / Robotics / AR Applications: 11
  - Dynamic / 4D Reconstruction: 5
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的中文科研趋势综合分析。

#### 今日主要趋势

1.  **从“表征”到“交互”：物理与语义的深度耦合成为新焦点**
    本日论文清晰地展示了计算机视觉与三维重建研究正从单纯追求视觉质量的“静态表征”，转向服务于具身智能和机器人操作的“动态交互”领域。多篇论文致力于填补“感知”与“行动”之间的鸿沟，例如通过解耦语义与空间流（**S-squared-VLA**）提升自动驾驶控制精度，或为3D资产自动赋予物理语义（**UniPhysGen**），使其可用于仿真。此外，物理引导的残差动力学（**PGRD**）和基于单次演示合成大规模训练数据（**WANDA**）的工作，都旨在为机器人策略学习提供更真实、更高效的数据与环境。这一趋势表明，让模型“理解”并“适应”物理世界规则，比单纯“看懂”更为重要。

2.  **3D高斯泼溅（3DGS）进入“高速、高质量、高保真”应用深化阶段**
    3DGS依然是本日最活跃的研究方向之一，但重点已从架构创新转向特定场景下的性能优化与应用拓展。技术上，出现了追求极致渲染速度（**Bake It Till You Make It**），实现高达5倍加速和4K 60 FPS输出；追求高质量外推，如结合扩散模型增强内窥镜视图外推（**ExtraGS**）；以及为无线VR场景设计结合通信约束的几何感知跨层框架（**GeoFovea-GS**）。此外，3DGS还作为高效的世界基底，用于合成机器人操作训练数据（**WANDA**）。这显示出3DGS正在从实验室基准走向解决特定领域（如手术、VR、机器人模拟）的工程难题。

3.  **联合逆渲染：物理模型与神经网络的融合走向精细化**
    从图像中恢复场景的材质、光照和几何属性（逆渲染）正朝着更物理精准、更通用的方向发展。本日的几篇工作不再依赖端到端的黑盒学习，而是巧妙地融合了经典物理模型与神经网络。例如，**Volumetric Inverse Rendering** 直接将辐射传输方程（RTE）的微分形式作为残差目标，指导神经场优化；**Differentiable Polarized Path Tracing** 则通过引入偏振信息，在可微渲染框架中解决了传统梯度估计的数值不稳定问题；**FreeLit** 则用物理先验引导扩散模型，实现了无需配对数据的高控制性重打光。这种做法在保留了物理模型的解释性和约束能力的同时，利用了神经网络的强大拟合能力。

4.  **数据效率革命：从“大规模标注”到“单样本学习”与“零样本自博弈”**
    针对监督学习对大规模、高质量数据（尤其是配对数据或人工标注）的依赖，本日论文展示了多种数据效率极高的解决方案。**Human4K** 这类传统大规模数据集依然重要（提供高分辨率、高精度标注），但更引人注目的是 **WANDA** 提出的“单次演示”引擎，通过程序化合成和轨迹重排，从一次人类演示生成海量训练数据。同时，**TerraZero** 通过程序化生成的模拟器和完全基于强化学习的自博弈方法，在零人类演示和零后备规划器的情况下，从头训练出达到顶尖安全性的自动驾驶策略。这表明，利用物理或几何先验进行数据合成，是打破数据瓶颈的关键路径。

#### 技术路线观察

-   **几何基础模型**：本日仅**X-Lens**属于此类。其技术路线是构建紧凑的、**几何感知**的前馈网络，通过**可学习校准令牌**和**雅可比畸变偏置**等创新模块，解决异构相机（鱼眼+针孔）的实时度量深度估计问题，强调**跨相机泛化能力**。
-   **3D/4D重建**：这一方向呈现出两大分支。一是**主动式**（**COLMAR**），通过强化学习优化多机器人协同的视点规划，目标是在有限预算下最大化重建质量。二是**从稀疏/不完整数据中补全**，例如从稀疏触觉重建可变形物体网格（**Topology-Agnostic Mesh...**）和用视觉几何先验补全遮挡区域的体占用（**GPOcc++**）。**CASA-SDF** 则代表了隐式神经表示向**空间自适应**的演进，通过课程学习和曲率指导处理室内场景的几何异质性。
-   **神经场景表示与渲染**：这是本日论文数量最多的方向，技术路线多元化。
    - **速度优化**：**Bake It Till You Make It** 通过将高频纹理烘焙到纹理图集，并采用2D曲面元素（Surfels）和稀疏化优化，大幅提升了渲染速度。
    - **物理/偏振扩展**：**Differentiable Polarized Path Tracing** 和 **Volumetric Inverse Rendering** 分别向可微渲染中引入了偏振和体辐射传输方程，提升了逆渲染的物理准确性。
    - **跨领域应用**：**ExtraGS** 和 **GeoFovea-GS** 代表了3DGS向医学（内窥镜）和通信（无线VR）领域的应用探索，各自设计了针对领域问题的解决方案（如扩散引导外推、几何感知跨层优化）。
    - **混合仿真**：**PGRD** 采用了“可优化物理模拟器 + 神经网络残差校正”的混合路线，是物理模型与数据驱动结合的典型案例。
-   **机器人/AR应用**：这个方向的论文更侧重于**闭环系统**和**数据生成**。
    - **端到端控制**：**S-squared-VLA** 关注如何在VLA模型中保持空间信息，以生成精确轨迹。
    - **仿真数据生成**：**WANDA** 和 **TerraZero** 代表了两种数据生成范式：前者从单次演示中合成多样化数据，后者在程序化模拟器中通过自博弈产生数据。
    - **物理属性附加**：**UniPhysGen** 致力于为现有3D资产附加统一的物理语义，使其可直接用于机器人仿真。
    - **AR辅助**：**Marker-free deformable registration...** 解决了手术中标记点从标本到病灶床的准确映射，代表了AR在精准医疗中的应用。

#### 值得优先阅读的论文

1.  **S-squared-VLA**：作为“Embodied/Robotics”方向的核心论文，它深刻剖析了当前VLA模型的根本缺陷（空间表征崩溃），并提出了一个极具可解释性的解耦方案。不仅适用于自动驾驶，其思想对整个具身智能领域都有启发。
2.  **Bake It Till You Make It**：这篇论文代表了当前3DGS在渲染速度上的极致追求，其“烘焙-纹理图集”的加速思路非常具有工程价值。对于任何从事实时或交互式渲染的研究者来说，都是必读之作。
3.  **UniPhysGen**：该工作直击了“仿真就绪3D资产”这一核心痛点，为具身AI和机器人研究提供了一个关键基础设施。其提出的自动化框架、大规模数据集和联合推理模型，使得这项工作既有方法论贡献，也有实用价值。
4.  **WANDA**：这篇论文在数据效率方面的突破令人瞩目。其“单次演示合成海量数据”的路线，为破解机器人学习中的数据瓶颈问题提供了一个极具潜力的范式，对整个社区的训练数据生成策略有重要参考意义。
5.  **Differentiable Polarized Path Tracing**：该工作将偏振信息引入可微渲染，直接挑战了一个长期存在的数值稳定性难题。为逆渲染领域开辟了一个新的提升维度（利用偏振先验），对于从事材质和光照估计的研究者是必读文献。

#### 可能的研究机会

1.  **“物理引导的3D/4D表示”的泛化与自动化**：
    - **机会**：**PGRD** 和 **Volumetric Inverse Rendering** 等工作展示了物理模型与神经表示结合的优势。一个有趣的方向是，能否开发一种通用框架，自动为不同场景（如布料、流体、刚体）选择和参数化物理先验，并将其无缝嵌入到神经隐式或显式表示（如3DGS）的优化中，从而无需人工设计特定混合模型。
    - **组合**：将 **B

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-16T10:20:18-04:00
**Total number of papers:** 54
**Number of papers added in the latest update:** 15
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

#### 2026-07-12 - MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction

**Authors:** Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia
**Links:** [abs](https://arxiv.org/abs/2607.10792) - [pdf](https://arxiv.org/pdf/2607.10792)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** MASt3R, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction
- 作者：Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia
- 出版日期：2026-07-12
- 分类：Geometry Foundation Models (主); Neural Scene Representations & Rendering (辅)
- 链接：摘要链接 https://arxiv.org/abs/2607.10792；PDF链接 https://arxiv.org/pdf/2607.10792

### 一句话总结
MAC-Splat 提出一种基于多属性一致性损失（MAC loss）的训练框架，通过引入高质量3D对应关系作为几何锚点，显式正则化匹配高斯的空间位置、形状和外观，以解决稀疏视角重建中的几何伪影问题。

### 研究问题
从稀疏视角重建高保真3D场景时，现有可泛化3D高斯泼溅（3DGS）方法仅依赖2D光度损失监督，无法解决深度与对应关系歧义，导致几何伪影。

### 核心思路/方法
1. **骨干网络**：采用MASt3R几何骨干网络和冻结的DINOv3编码器，获取语义引导的2D对应关系，作为3D监督的几何锚点。
2. **多属性一致性损失（MAC loss）**：基于上述锚点，强制匹配高斯体在公共世界坐标系下对齐其位置、形状和外观三种属性，以正则化3D高斯属性。
3. **鲁棒性设计**：损失函数对异常值具有鲁棒性，并尊重协方差矩阵的几何结构，从而在稀疏视角条件下实现稳定训练。

### 主要贡献
- 提出直接面向3D属性一致性监督的训练框架MAC-Splat，可有效缓解稀疏视角下的几何伪影。
- 设计多属性一致性损失（MAC loss），联合正则化匹配高斯的空间、形状和外观属性。
- 在ScanNet++数据集上，MAC-Splat在重叠率等变化场景下均显著超越基线（如相较于Splatt3R，PSNR提升超4.5 dB，LPIPS降低），且在相机姿态间距增大时仍保持性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对稀疏视角下3D重建的核心难题（几何伪影），提出创新的直接3D一致性监督方法，并在公开基准上取得大幅性能提升（PSNR超4.5 dB），方法清晰且实验结果突出，对神经渲染和3DGS领域具有显著参考价值。

</details>

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

## Dynamic / 4D Reconstruction

### 2026-07

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

#### 2026-07-14 - Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements

**Authors:** Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun
**Links:** [abs](https://arxiv.org/abs/2607.12362) - [pdf](https://arxiv.org/pdf/2607.12362)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements
- 作者：Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun
- 出版日期：2026-07-14
- 分类：Dynamic / 4D Reconstruction（主分类），Neural Scene Representations & Rendering（副分类）
- 链接：摘要页 https://arxiv.org/abs/2607.12362；PDF https://arxiv.org/pdf/2607.12362

### 一句话总结
本文提出 SPIN-4DGS，通过时空位置隐式网络从显式收集的时空位置学习高斯属性，解决了现有4DGS方法在帧间大位移快速运动场景下重建失败的问题。

### 研究问题
现有4D高斯泼溅（4DGS）方法在处理快速运动且帧间位移较大的场景时，高斯属性的训练效果差，常导致快速运动物体在重建中丢失。

### 核心思路/方法
核心思路是用显式收集的时空位置替代对时间位移的建模，以避免因位移大导致的训练困难。具体方法：
1. 构建一个轻量级前馈网络，该网络从所有时空位置显式收集的输入中预测高斯属性，而非直接优化每个位置。
2. 网络基于光栅化重建损失训练，从而学习所有高斯点间的共享表征，捕获时空一致性。
3. 这避免了显式优化所有时空位置带来的巨大内存开销，同时提升了快速运动下的稳定性和质量。

### 主要贡献
1. 提出了 SPIN-4DGS 框架，能在大帧间位移的快速运动中实现更忠实的高斯泼溅。
2. 通过轻量级前馈网络预测高斯属性，降低了内存开销并保持了时空一致性。
3. 在 CMU Panoptic 数据集的高难度体育场景上，SPIN-4DGS 在 PSNR 和 SSIM 上显著优于现有方法，例如在 Basketball 场景中比最强基线 D3DGS 高出 +1.83 PSNR。

### 局限性
摘要未提供足够信息。例如，文中未讨论该方法在极端复杂场景（如严重遮挡、光照剧变）下的表现，也未提及计算开销或推理速度等具体局限性。

### 阅读优先级
高  
理由：该工作针对4D重建中快速运动这一实际痛点，提出了新颖的隐式网络方法，且在公开数据集的体育场景上取得了明显量化提升（如PSNR提升+1.83），属于动态场景重建方向的前沿进展，对相关领域研究有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent 4D Gaussian Splatting (4DGS) methods often fail under fast motion with large inter-frame displacements, where Gaussian attributes are poorly learned during training, and fast-moving objects are often lost from the reconstruction. In this work, we introduce Spatiotemporal Position Implicit Network for 4DGS, coined SPIN-4DGS, which learns Gaussian attributes from explicitly collected spatiotemporal positions rather than modeling temporal displacements, thereby enabling more faithful splatting under fast motions with large inter-frame displacements. To avoid the heavy memory overhead of explicitly optimizing attributes across all spatiotemporal positions, we instead predict them with a lightweight feed-forward network trained under a rasterization-based reconstruction loss. Consequently, SPIN-4DGS learns shared representations across Gaussians, effectively capturing spatiotemporal consistency and enabling stable high-quality Gaussian splatting even under challenging motions. Across extensive experiments, SPIN-4DGS consistently achieves higher fidelity under large displacements, with clear improvements in PSNR and SSIM on challenging sports scenes from the CMU Panoptic dataset. For example, SPIN-4DGS notably outperforms the strongest baseline, D3DGS, by achieving +1.83 higher PSNR on the Basketball scene.

</details>

#### 2026-07-12 - OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields

**Authors:** Yanqin Jiang, Tengfei Wang, Zhengwei Wang, Chenjie Cao, Junta Wu, Wenhan Luo, Weiming Hu, Jin Gao, Chunchao Guo
**Links:** [abs](https://arxiv.org/abs/2607.10840) - [pdf](https://arxiv.org/pdf/2607.10840)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 4D reconstruction, camera pose estimation, pose estimation, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields
- 作者：Yanqin Jiang, Tengfei Wang, Zhengwei Wang, Chenjie Cao, Junta Wu, Wenhan Luo, Weiming Hu, Jin Gao, Chunchao Guo
- 出版日期：2026-07-12
- 分类：Dynamic / 4D Reconstruction（主分类），3D Reconstruction & Multi-view Geometry（次分类）
- 链接：摘要页 https://arxiv.org/abs/2607.10840，PDF https://arxiv.org/pdf/2607.10840

### 一句话总结
本文提出OmniX，一种前馈式4D重建框架，通过预测稠密3D点轨迹，在大视角变化视频中实现任意视角和任意时间的动态场景重建。

### 研究问题
现有前馈式4D重建方法存在两个主要限制：一是按帧预测静态点云，忽略了前景运动；二是估计点云轨迹时仅支持小相机运动，无法在大视角变化下聚合时间观测，难以重建完整的动态场景。

### 核心思路/方法
1. **解耦动态运动建模与静态几何预测**：将运动表示从静态几何中分离，用一组紧凑的动态令牌（dynamic tokens）编码运动。
2. **利用3D运动的稀疏和低秩结构**：通过动态令牌为所有图像的所有像素生成轨迹场，同时高效保持全局交互。
3. **自动数据引擎与大规模数据集**：构建基于UE5的自动4D数据生成引擎，产出包含80K场景和1.28M多视角视频的全几何标注数据集，用于训练。

### 主要贡献
- 提出OmniX框架，能够从大相机运动视频中预测稠密3D点轨迹，实现任意视角和任意时间的4D重建。
- 提出解耦的动态运动建模方法，利用稀疏和低秩运动结构生成轨迹场。
- 构建了大规模自动生成的4D数据集（80K场景，1.28M多视角视频），带有完整几何标注。
- 在稠密3D点轨迹预测和3D点跟踪任务上达到当前最优性能，在视频深度估计和相机位姿估计上也获得有竞争力的结果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对前馈式4D重建在大视角变化下的核心局限提出解决方案，并构建了大规模训练数据，在多项任务上取得最优或接近最优性能。对于关注动态3D重建、4D场景理解及新视角合成的研究者具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Grassmannian Splatting I: Moving rank-2 Spacetime Surfels for Dynamic Scene Rendering
- 作者：Aaron Maurice Berman, Shantanu Dave
- 出版日期：2026-07-11
- 分类：Dynamic / 4D Reconstruction; Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2607.10489 ; PDF: https://arxiv.org/pdf/2607.10489

### 一句话总结
该论文提出一种基于时序-空间四维Grassmannian splatting的动态场景表示方法，利用秩-2时空surfels实现无需变形场的高效动态渲染，在HyperNeRF数据集上训练速度最快且质量排名第二。

### 研究问题
如何用一种简洁、封闭形式的运动表示，替代现有4D Gaussian splatting方法中通过学习变形场或使用全秩四维协方差来渲染动态场景的方式，从而降低训练开销并保持高质量渲染。

### 核心思路/方法
1. 表示设计：每个图元是一个在四维时空中由高斯函数支持的三维平面（即均匀运动的二维空间表面），其协方差矩阵由单位法向量\(n\)和自由矩阵\(L\)参数化，保证在时间切片后得到秩-2的surfel（带速度信息）。
2. 运动建模：封闭形式，无需学习变形场；运动参数（法线方向、沿法线速度、磁盘形状和中心切向漂移）直接从参数中读出。
3. 硬件兼容：秩-2磁盘通过预计算协方差接口直接输入标准3DGS光栅化器，无需自定义CUDA。
4. 静态-动态统一：使用软夹钳（Schur分母中的正则化）使静态秩-3图元和动态秩-2图元连续，形成统一参数族。

### 主要贡献
- 提出一种新型动态场景图元（Grassmannian splatting），在四维时空上实现秩-2 surfel，每个图元对应一个均匀运动的二维空间表面。
- 运动模型是封闭形式的，无需变形场或额外网络，降低了训练复杂度。
- 不需要自定义CUDA内核，可直接利用预计算协方差接口和标准3DGS光栅化器。
- 在MonoDyGauBench的17个HyperNeRF场景上，训练速度比最优质基线快4.9–5.6倍，并在PSNR、MS-SSIM和LPIPS上排名第二。

### 局限性
摘要未提供足够信息：未提及多视角处理、动态场景中复杂遮挡或拓扑变化、以及在大规模场景或非HyperNeRF类数据集上的表现。

### 阅读优先级
**高**  
理由：该方法在动态场景渲染领域实现了显著的训练速度提升（4.9–5.6倍），同时保持了顶级质量（第二），且避免了自定义CUDA和变形场，工程实现简洁；摘要显示其发布在2026年（即使时间戳存疑），但内容新颖，对关注动态辐射场高效表示的读者有较高价值。

</details>

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

## 3D Reconstruction & Multi-view Geometry

### 2026-07

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

#### 2026-07-14 - ARDepth: Auto-regressive Monocular Depth Estimation with Progressive Visual Conditioning

**Authors:** Zijie Wang, Wei Zhang, Weiming Zhang, Xiao Tan, Weikai Chen, Xiaoxu Li, Guanbin Li
**Links:** [abs](https://arxiv.org/abs/2607.12433) - [pdf](https://arxiv.org/pdf/2607.12433)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ARDepth: Auto-regressive Monocular Depth Estimation with Progressive Visual Conditioning
- 作者：Zijie Wang, Wei Zhang, Weiming Zhang, Xiao Tan, Weikai Chen, Xiaoxu Li, Guanbin Li
- 出版日期：2026-07-14
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[Abstract](https://arxiv.org/abs/2607.12433) | [PDF](https://arxiv.org/pdf/2607.12433)

### 一句话总结
提出ARDepth方法，将单目深度估计重构为一种跨空间尺度的自回归生成过程，通过渐进式视觉条件注入和语义引导，在保持全局结构一致性的同时捕捉细粒度局部细节。

### 研究问题
现有扩散模型进行单目深度估计时，通常假设深度可通过全局迭代去噪恢复为平滑场，但这种方法未能显式建模场景几何的逐段平滑性和跨尺度的层次化组织特性。

### 核心思路/方法
1. 将深度估计建模为结构化自回归生成：随着空间分辨率增加，逐步构建深度表示，而非通过全局细化恢复深度。
2. Scale-Progressive Conditioning (SPC)：在每一个生成阶段注入多尺度视觉特征。
3. Semantic-Aware Guidance (SAG)：提供场景级语义先验，增强全局结构一致性。

### 主要贡献
1. 提出ARDepth，一种将单目深度估计形式化为结构化的自回归生成的新范式。
2. 设计渐进式视觉条件注入机制（SPC）和语义感知引导机制（SAG），分别用于多尺度特征融合和全局结构约束。
3. 实验表明该方法在保持跨尺度结构一致的深度预测方面具有强性能，验证了自回归生成作为几何建模替代范式的潜力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作提出了单目深度估计的新范式（自回归生成替代扩散模型），并设计了针对性的条件注入和引导模块，对几何建模方法创新有参考价值。

</details>

<details>
<summary>Abstract</summary>

Diffusion models have recently become the dominant paradigm for monocular depth estimation (MDE). However, they implicitly assume that depth can be recovered as a globally smooth field through iterative denoising, which does not explicitly reflect the piecewise and scale-dependent organization of scene geometry. In practice, geometric structure emerges progressively across spatial scales, where coarse layout, surfaces, and boundaries are constructed in a hierarchical manner. Motivated by this observation, we introduce ARDepth, which formulates depth estimation as structured auto-regressive generation. Instead of recovering depth through global refinement, ARDepth progressively constructs depth representations as spatial resolution increases. To support this generative process, we introduce Scale-Progressive Conditioning (SPC) to inject multi-scale visual features at each generation stage, and Semantic-Aware Guidance (SAG) to provide scene-level semantic priors that enhance global structural consistency. Together, these designs enable the model to capture fine-grained local details while maintaining coherent global geometry. Empirical results demonstrate that our approach achieves strong performance and produces structurally consistent depth predictions across scales, validating auto-regressive generation as a promising alternative paradigm for geometric modeling.

</details>

#### 2026-07-14 - DiffRadar: Differentiable Physics-Aware Radar SLAM with Gaussian Fields

**Authors:** Gaurav Bagwe, Xiaoyong Yuan, Yongji Wu, Lan Zhang
**Links:** [abs](https://arxiv.org/abs/2607.12265) - [pdf](https://arxiv.org/pdf/2607.12265)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, pose estimation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DiffRadar: Differentiable Physics-Aware Radar SLAM with Gaussian Fields
- 作者：Gaurav Bagwe, Xiaoyong Yuan, Yongji Wu, Lan Zhang
- 出版日期：2026-07-14
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.12265

### 一句话总结
DiffRadar 是一种利用可微分高斯场建模雷达观测的实时SLAM系统，通过联合优化位姿与场景结构，在多种恶劣条件下实现了比传统方法更稳定、更一致的轨迹和地图重建。

### 研究问题
现有雷达SLAM系统通常对离散化的雷达热图进行扫描匹配，破坏了几何连续性且无法捕捉关键的雷达感知特性（如多普勒效应），导致在特征匮乏或动态环境中位姿估计不稳定、地图质量下降。

### 核心思路/方法
- 使用各向异性高斯基元表示场景，并通过可微分的雷达前向模型在距离-方位角和多普勒-方位角空间渲染雷达测量值。
- 将雷达观测建模为可微分的、物理感知的高斯场，而非离散扫描，从而实现对机器人位姿和场景结构的联合优化。

### 主要贡献
- 提出了一种将雷达观测直接建模为可微分高斯场的SLAM方法，避免了离散化带来的几何断裂。
- 在商用FMCW雷达硬件上实现，并在Radarize基准测试和自建压力测试集上验证。
- 在基准测试中大幅降低了轨迹误差（尤其在特征匮乏的走廊运动中），地图一致性提升超过一倍，同时保持实时性能（70 FPS）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。
理由：该方法在雷达SLAM这一实际应用方向（无人车、移动机器人）中提出了新颖的可微分高斯场建模思路，且在极端场景下显著提升了鲁棒性和一致性，同时保持了实时性，具有较高的技术价值和潜在影响力。

</details>

<details>
<summary>Abstract</summary>

Radar sensing is increasingly used in mobile systems because it operates reliably under poor lighting, adverse weather, and privacy-sensitive settings where cameras and LiDAR often fail. However, most existing radar SLAM systems estimate motion through scan matching on discretized radar heatmaps, which breaks geometric continuity and fails to capture key radar sensing properties, often leading to unstable pose estimation and degraded mapping in regenerate or dynamically changing environments. We present DiffRadar, a real-time radar SLAM system that models radar observations as a differentiable, physics-aware Gaussian field rather than discrete scans. DiffRadar represents the scene as anisotropic Gaussian primitives and renders radar measurements in range-azimuth and Doppler-azimuth spaces through a differentiable radar forward model, enabling joint optimization of robot pose and scene structure directly from radar measurements. We implement DiffRadar on commodity FMCW radar hardware and evaluate it on both the public Radarize benchmark and a controlled stress-test suite that targets common radar SLAM failure modes, including corridor degeneracy, motion regime transitions, dynamic clutter, and long-horizon loop closures. DiffRadar achieves substantial reductions in trajectory error on the benchmark, with especially large gains under feature-poor corridor motion, while more than doubling map consistency and maintaining real-time performance at 70 FPS. These results show that modeling radar observations directly in the signal domain enables substantially more robust and consistent radar-only SLAM for mobile platforms.

</details>

#### 2026-07-13 - IBPA: Real-time Free-form Manifold Mesh Reconstruction via Incremental Ball Pivoting with Integrated Hole Detection

**Authors:** Mauhing Yip, Mohit Singh, Kostas Alexis, Christian Schellewald, Annette Stahl
**Links:** [abs](https://arxiv.org/abs/2607.11627) - [pdf](https://arxiv.org/pdf/2607.11627)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction, surface reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IBPA: Real-time Free-form Manifold Mesh Reconstruction via Incremental Ball Pivoting with Integrated Hole Detection
- 作者：Mauhing Yip, Mohit Singh, Kostas Alexis, Christian Schellewald, Annette Stahl
- 出版日期：2026-07-13T14:45:46Z
- 分类：3D Reconstruction & Multi-view Geometry（主要类别）
- 链接：[摘要](https://arxiv.org/abs/2607.11627) | [PDF](https://arxiv.org/pdf/2607.11627)

### 一句话总结
本文提出增量式球体旋转算法（IBPA），一种能够在水下机器人实时获取点云数据时，逐步构建无需预定义结构假设的自由形式流形网格，并集成孔洞检测功能的方法。

### 研究问题
针对水下机器人（ROV/AUV）作业中，传统方法（如数字地形模型DTM）无法表达悬垂、垂直结构等复杂拓扑，且现有增量重建方法（如DTM）表达能力有限的问题，文中提出了如何实时、增量地重建自由形式流形网格并检测不完整区域的研究问题。

### 核心思路/方法
- 将原始球体旋转算法（BPA）改造为增量版本（IBPA），使其能实时处理流式点云数据，无需依赖点云重叠或分布假设。
- 方法逐块构建可定向流形网格，并集成孔洞检测机制，以识别并高亮显示未完全重建的网格区域。

### 主要贡献
1. 提出IBPA算法，实现从流式点云中增量式构建自由形式流形网格，支持复杂表面拓扑（如悬垂、垂直结构）。
2. 集成孔洞检测机制，可视化标识不完整网格区域，帮助操作者实时感知覆盖质量。
3. 提供了参考实现的源代码（开源链接见摘要），便于复现和比较。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：论文针对水下机器人实时3D重建的实际工程问题，提出了一个增量式的自由形式网格重建方法，并集成了孔洞检测功能。方法新颖（改进经典BPA），且开源实现，对于从事实时3D重建、水下导航测绘或点云处理的研究者具有直接参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：SalientGS: Unified SfM-to-3DGS with Importance-Guided MCMC Gaussian Allocation
- 作者：Tianyu Xiong, Rui Li, Suning Ge, Jiaqi Yang
- 出版日期：2026-07-13
- 分类：3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
- 链接：摘要URL (https://arxiv.org/abs/2607.11285), PDF (https://arxiv.org/pdf/2607.11285)

### 一句话总结
SalientGS 提出了一种基于重要性引导的马尔可夫链蒙特卡洛（MCMC）高斯分布分配方法，将传统的结构运动恢复（SfM）和3D高斯泼溅（3DGS）过程统一为端到端管道，在15分钟内实现高质量3D场景重建。

### 研究问题
从无序图像进行3D场景重建时，传统方法受限于昂贵的SfM预处理和冻结的位姿接口，导致流程割裂且效率低下。本文旨在解决这一瓶颈，实现SfM与3DGS的端到端统一。

### 核心思路/方法
核心方法是重要性引导的MCMC高斯分布分配。其流程为：
1. **聚合多视图残差**：计算每个高斯体的欠拟合和冗余信号。
2. **定义重要性加权采样分布**：基于上述信号，构建平滑的重要性采样分布，倾向于引导高斯体的新生（birth）和重定位（relocation）到欠拟合区域。
3. **重新分配容量**：在保持随机梯度朗之万动力学（SGLD）不变的前提下，将高斯体从拟合良好的区域重新分配至需要更多细节的区域。

### 主要贡献
1. 提出了**统一的SfM-to-3DGS端到端管道**，简化了3D重建流程。
2. 设计了**重要性引导的MCMC高斯分配机制**，通过聚合多视图残差自动识别并修复欠拟合区域，同时减少冗余高斯体。
3. 实验表明，该方法能够在**15分钟内**完成端到端重建，并达到**最先进的感知质量**（通过LPIPS等指标验证）。

### 局限性
摘要未提供充分信息，仅提到附录中包含了失败案例的分析，但未在摘要中明确列出具体的局限性或失败模式。

### 阅读优先级
**高**  
理由：该方法提出了一个创新的统一框架（融合SfM和3DGS），并引入了一种新的重要性引导分配机制，直接解决了该领域内由SfM预处理造成的效率瓶颈。实验在感知质量上达到先进水平，且代码已开源，对从事3D重建、神经渲染的研究者具有直接参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors
- 作者：Ruilan Gao, Letian Jin, Yu Zhang
- 出版日期：2026-07-13
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：abstract_url: https://arxiv.org/abs/2607.11184; pdf_url: https://arxiv.org/pdf/2607.11184

### 一句话总结
GeoGS-SLAM提出一种结合3D高斯溅射（3DGS）与学习几何先验的单目在线稠密重建系统，通过从RGB输入和几何先验中采样高斯基元、联合优化光度与几何损失，以及引入闭环检测，实现了优于现有方法的渲染质量和跟踪精度。

### 研究问题
如何在不依赖外部深度传感器的情况下，利用单目RGB输入实现高精度的在线稠密SLAM重建，同时避免因丢弃RGB信息导致的重建质量下降。

### 核心思路/方法
1. 使用前馈视觉几何模型从未标定RGB输入预测相机和场景几何先验。
2. 通过直接从RGB输入和几何先验中采样高斯基元来扩展高斯场景图。
3. 采用从粗到细的策略联合优化相机位姿和场景图，最小化光度损失和几何损失。
4. 引入在线闭环检测与位姿图优化以保持全局一致性。

### 主要贡献
1. 提出一种结合3DGS地图表示与学习几何先验的单目稠密重建SLAM系统。
2. 通过从RGB和几何先验中采样高斯基元的方式，避免优化过程中丢失RGB信息。
3. 在室内外基准测试中，实现了优于现有方法的渲染质量与跟踪精度，且保持在线实时性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法在单目SLAM和稠密重建领域提出了整合几何先验与3DGS的实用方案，性能有提升，但属于对现有范式的改进而非颠覆性创新；适合对SLAM或神经渲染方向有基础了解的读者参考。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GHOST: Geometry-Guided Hallucination of Opaque Surface Textures  
- 作者：Langxu Zhao, Zuan Gu, Tianhan Gao  
- 出版日期：2026-07-13  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：[摘要](https://arxiv.org/abs/2607.11118) | [PDF](https://arxiv.org/pdf/2607.11118)

### 一句话总结
提出一个几何引导的预处理框架GHOST，通过视觉基础模型将透明物体表面转化为不透明、结构一致的RGB纹理，以提升现有深度估计与3D重建模型的精度。

### 研究问题
透明物体因违反朗伯体假设，导致深度估计和3D重建中的几何退化问题。

### 核心思路/方法
提出一个预处理流水线，包含四个模块：  
1. **TransDINO** 和 **TransDecomp**：分别用于解耦透明区域的掩膜和透明度物理属性。  
2. **DAF-Net**：恢复表面法线先验以编码几何曲率。  
3. **GeoSemTransNet**：整合上述多模态线索，合成为保持3D结构的不透明RGB纹理图像。  
该方法无需重新训练下游模型即可直接增强其输入质量。

### 主要贡献
1. 提出一种新框架，通过几何引导的纹理生成解决透明物体的几何恢复难题。  
2. 设计了四个专用模块（TransDINO、TransDecomp、DAF-Net、GeoSemTransNet）协同工作。  
3. 实验表明，该方法能显著提升现有深度估计和重建模型在透明物体上的精度。

### 局限性
摘要未提供足够信息：未提及计算开销、对极端透明或复杂光照场景的鲁棒性，以及是否依赖大量标注数据。

### 阅读优先级
**高**。理由：该文针对3D重建中的透明物体难题提供了新颖的预处理思路，且不依赖下游模型重训练，具有较强实用价值；同时发表于2026年，内容前沿。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems
- 作者：Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
- 出版日期：2026-07-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.11099, PDF: https://arxiv.org/pdf/2607.11099

### 一句话总结
提出一种轻量级描述符增强模块Desc++，在保持原始维度与匹配接口的前提下，通过混合全局注意力与几何感知序列建模提升现有视觉SLAM系统的数据关联性能。

### 研究问题
现有视觉SLAM系统中，手工描述符在光照与视角变化下性能下降，而基于学习的替换前端计算开销大；当前描述符增强方法受限于简化注意力机制，上下文建模能力不足，导致匹配质量受限。

### 核心思路/方法
提出Desc++模块，该模块联合编码描述符表示与关键点几何信息，并通过混合架构聚合空间上下文：结合顺序无关的全局注意力与几何感知的序列建模，在线性时间内实现高效增强。增强后的描述符保留原始维度和匹配接口，可直接集成到现有SLAM系统的管线上。

### 主要贡献
- 提出Desc++，一种轻量级描述符增强模块，在保持原始格式的前提下提升匹配精度。
- 引入混合架构，融合全局注意力与几何感知建模，提高上下文表达效率。
- 在描述符匹配、对应关系分析及四个不同SLAM系统的系统级基准上，验证了相比现有增强方法在匹配精度与轨迹估计稳定性上的提升，并实现了精度与效率的平衡。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工作聚焦于提升现有视觉SLAM系统的数据关联鲁棒性，提供了一种不修改管线即可集成的轻量级方案，对工程落地有较好参考价值。但摘要未披露具体性能数值或对比细节，需要进一步阅读全文评估实际提升幅度。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：WiFi-JEPA: Self-supervised Learning for WiFi-CSI 3D Human Pose Estimation
- 作者：Doeon Kim, Jungyoon Lee, Seongsin Kim, Seong-heum Kim
- 出版日期：2026-07-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.11064 ; PDF: https://arxiv.org/pdf/2607.11064

### 一句话总结
WiFi-JEPA 是一个自监督学习框架，通过预测掩码潜在嵌入而非重建原始CSI信号，并在无标注的射线追踪仿真数据上预训练，从而提升WiFi-CSI 3D人体姿态估计在环境变化下的鲁棒性与性能。

### 研究问题
现有基于WiFi的3D人体姿态估计方法在环境变化时容易失效，且严重依赖昂贵的相机标注数据来训练，限制了其规模化应用。如何设计一种无需人工标注、能泛化至新环境的WiFi-CSI姿态估计方法？

### 核心思路/方法
1. **自监督预训练目标**：采用掩码潜在嵌入预测（类似JEPA），而不是重建原始CSI信号，以避免学习硬件相关的噪声和伪影。
2. **CSI特定的结构化掩码**：针对信道、时间、链路（C,T,L）三维张量，提出CSI tokenization和链路掩码——通过掩码整个发射-接收天线链路，迫使模型从其他链路预测该链路的嵌入，从而学习跨链路相关性和3D空间结构。
3. **仿真数据生成**：使用射线追踪模拟，从随机几何体生成多样化的无标注CSI数据，无需任何姿态标注即可提供大规模预训练素材。

### 主要贡献
1. 提出了CSI特定的tokenization和链路掩码策略，有效捕获空间结构信息。
2. 构建了射线追踪CSI仿真管道，可规模化生成无标注预训练数据。
3. 在Person-in-WiFi-3D数据集上，WiFi-JEPA在单人和多人3D姿态估计任务上均超越了以往WiFi-CSI基线方法；仿真数据与真实数据的结合能互补预训练信号；而四种视觉原生自监督目标在CSI任务上性能下降甚至不如从头训练，WiFi-JEPA则持续提升下游姿态估计效果。

### 局限性
摘要未提供足够信息。例如：未讨论模型在不同环境之间的具体迁移效果、对遮挡或极端姿态的鲁棒性、仿真与真实数据之间的域差异程度、训练计算成本或推理速度等。

### 阅读优先级
**高**。理由：该工作提出了在难以标注的模态（WiFi-CSI）中结合仿真数据与自监督学习的有效方案，在3D姿态估计任务上取得了SOTA结果，且对视觉SSL方法不适用WiFi模态的现象给出了直接对比，对同类无监督跨模态感知研究具有参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Mapping Pamir: Multi-Session Visual-Inertial SLAM and 3D Reconstruction of an Underwater Shipwreck
- 作者：Michalis Chatzispyrou, Luke Horgan, Hyunkil Hwang, Harish Sathishchandra, Chinmay Burgul, Monika Roznere, Alberto Quattrini Li, Philippos Mordohai, Ioannis Rekleitis
- 出版日期：2026-07-12
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2607.10925) | [PDF](https://arxiv.org/pdf/2607.10925)

### 一句话总结
本文提出一个利用低成本运动相机和开源框架的多会话水下环境映射管线，成功实现了对巴巴多斯海域一艘沉船外部和内部首次联合的3D重建。

### 研究问题
如何利用低成本设备和开源框架，实现水下沉船的多会话视觉-惯性SLAM与稠密三维重建。

### 核心思路/方法
1. 使用低成本运动相机采集视觉-惯性数据，并辅以潜水电脑的水深记录。
2. 采用开源VI-SLAM框架SVIn2为每个数据会话生成轨迹和稀疏重建。
3. 从SVIn2提取关键帧与估计的相机位姿，再使用SfM框架COLMAP进行全局优化，并生成目标环境的稠密重建。
4. 当存在固定位置的标定目标时，利用其估计不同会话之间的坐标变换，将所有会话统一到同一坐标系下。
5. 通过三个会话对沉船进行映射：两个会话覆盖沉船外部和内部，第三个会话使用两个不同视场的相机。

### 主要贡献
- 提出一个多会话水下环境映射管线，结合了VI-SLAM和SfM，仅使用低成本运动相机和开源软件。
- 首次实现了对巴巴多斯海域沉船“Pamir”外部与可进入内部的联合三维映射。
- 展示了多会话数据融合及利用标定目标实现坐标对齐的实用性。

### 局限性
摘要未提供足够信息。未提及系统在缺乏标定目标时的对齐精度、光照条件对重建质量的影响、计算资源需求或大规模环境下的可扩展性。

### 阅读优先级
中
**理由**：本文针对水下沉船场景提出了一种实际可行的多会话映射方案，技术路线清晰且结合了低成本硬件与开源工具，对水下机器人或考古应用有参考价值。但方法创新主要集中在流程整合与应用演示，而非算法理论突破，优先级中等。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：TriCons-Pose: Triangle-Invariant Geometric Consistency Learning for Category-Level Object Pose Estimation
- 作者：Zuzhi Yang, Shuai Wang, Mounir Kaaniche, Ziwei Li, Zhiming Cheng, Zhidong Zhao, Chenggang Yan
- 出版日期：2026-07-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.10754

### 一句话总结
本文提出了一种基于三角形不变几何一致性学习的类别级物体姿态估计方法，通过检测结构一致的关键点并聚合姿态不变特征，在REAL275、CAMERA25和HouseCat6D数据集上验证了有效性。

### 研究问题
现有基于关键点对应范式的类别级物体姿态估计方法，往往依赖更强的特征学习，却忽视了所建立对应关系在不同扰动下的几何稳定性，导致在类内形状变化和遮挡场景下姿态恢复不稳健。

### 核心思路/方法
- 提出三角形不变几何一致性学习框架。
- 设计结构一致关键点检测器（SCKD），通过归一化成对距离匹配强制跨视角结构一致性，以定位稳健关键点。
- 提出姿态不变几何聚合器（PIGA），通过将基于三角形的姿态不变描述子注入局部到全局注意力机制，增强关键点表示。
- 在标准目标函数基础上，额外引入几何一致性损失进行训练。

### 主要贡献
- 开发了TriCons-Pose框架，通过三角形不变几何一致性学习获得可靠的关键点和姿态不变线索，从而实现精确的规范映射和姿态估计。
- 提出SCKD和PIGA两个核心模块，分别用于稳定关键点检测和姿态不变特征聚合。
- 在REAL275、CAMERA25和HouseCat6D三个数据集上进行实验，证明了方法的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对类别级物体姿态估计中的几何稳定性问题，方法设计具有明确的理论动机（三角形不变性），且在多个基准数据集上验证了性能。适合从事3D视觉、姿态估计相关领域的研究者阅读，但对于不涉及该方向的研究者则优先级不高。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Incremental Online Scene Reconstruction by 3D Gaussian Triangulation  
- 作者：Yanjin Zhu, Shaofan Liu, Jianke Zhu  
- 出版日期：2026-07-12  
- 分类：3D Reconstruction & Multi-view Geometry / Neural Scene Representations & Rendering  
- 链接：[摘要](https://arxiv.org/abs/2607.10690) | [PDF](https://arxiv.org/pdf/2607.10690)

### 一句话总结
本文提出一种在线增量式重建框架，直接对三维高斯点集进行三角化，以同时实现高质量渲染和增量式表面网格重建。

### 研究问题
现有的三维高斯泼溅方法多依赖离线将优化后的高斯转化为隐式场来提取网格，无法与下游任务无缝集成。本文旨在解决如何在线、增量地重建并更新高保真显式网格的问题。

### 核心思路/方法
- 设计一种密集几何高斯表示，通过直接三角化该表示来重建显式网格，支持增量更新与高质量渲染。
- 提出一种直接网格化算法，从高斯集中高效提取并更新网格。
- 引入基于平面的牵引约束，动态将三维高斯基元对齐到近似局部表面，以提高网格精度。
- 通过动态冻结已充分优化的历史区域，降低长序列处理中的内存与计算开销。

### 主要贡献
- 提出一种新颖的在线框架，能增量重建并更新高保真显式网格，避免离线隐式转换。
- 实现直接网格化算法，从高斯表示中高效提取和更新网格。
- 引入平面牵引约束以保证网格准确性。
- 在公共数据集上，该方法在渲染质量和重建精度上均优于传统基于高斯的方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对3D高斯泼溅在在线增量重建中的关键瓶颈（必须离线转换隐式场）提出了直接三角化显式网格的新思路，方法创新性较强，且公开实验结果显示性能领先，对实时场景重建和下游任务集成有潜在应用价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：CSI-Assisted Edge SLAM Testbed Platform for 5G Connected Unmanned Autonomous Vehicles
- 作者：Boris Radovanovic, Sasa Talosi, Srdjan Sobot, Dejan Vukobratovic
- 出版日期：2026-07-11
- 分类：3D Reconstruction & Multi-view Geometry (主要), Embodied / Robotics / AR Applications (次要)
- 链接：arXiv:2607.10394

### 一句话总结
本文设计并实现了一个集成5G O-RAN、CSI辅助的Edge SLAM测试平台，用于评估面向6G的机器人系统在通信与感知融合中的性能与挑战。

### 研究问题
如何构建一个端到端的、支持CSI（信道状态信息）数据暴露与融合的Edge SLAM测试平台，以在5G URLLC环境下实现通信感知协同，并揭示其在延迟、同步和系统集成方面的关键难题。

### 核心思路/方法
- 构建一个集成的测试平台：包含自定义无人地面车（UGV）、基于ROS2的SLAM框架，以及5G O-RAN（开放无线接入网）系统。
- 提供端到端的跨层视图，让ROS2传感器数据流经5G网络传输，并明确将CSI作为额外感知模态暴露并集成到SLAM流水线中。
- 分析ROS2 DDS（数据分发服务）通信、RTPS（实时发布订阅协议）分包及5G用户面传输，探讨通过O-RAN组件提取和交付CSI的机制。

### 主要贡献
- 设计并实现了首个整合UGV、ROS2 SLAM与5G O-RAN的CSI辅助Edge SLAM测试平台。
- 提供了完整的端到端、跨层数据流分析，涵盖从ROS2层到5G用户面的传输细节。
- 揭示了通信感知SLAM在实际系统中的关键挑战，包括延迟、数据流、同步及跨系统集成，为未来6G机器人平台提供了实验洞察。

### 局限性
摘要未提供足够信息（例如未讨论测试规模、具体性能指标或是否存在试验结果中的失败案例）。

### 阅读优先级
中
理由：该论文侧重于系统架构设计与平台实现，核心价值在于工程整合与实验观察，而非提出全新算法。对于关注5G/6G与机器人SLAM交叉领域、需要构建类似测试平台的读者具有直接参考意义，但对纯算法或理论研究者价值相对有限。

</details>

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

## Neural Scene Representations & Rendering

### 2026-07

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

#### 2026-07-14 - ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting

**Authors:** Cheng-Tai Hsieh, Jiwei Shan, Han Fang, Jianshu Hu, Tao Ni, Lijun Han, Yutong Ban, Shing Shin Cheng, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2607.12785) - [pdf](https://arxiv.org/pdf/2607.12785)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, neural rendering, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting  
- 作者：Cheng-Tai Hsieh, Jiwei Shan, Han Fang, Jianshu Hu, Tao Ni, Lijun Han, Yutong Ban, Shing Shin Cheng, Hesheng Wang  
- 出版日期：2026-07-14  
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）  
- 链接：[arXiv:2607.12785](https://arxiv.org/abs/2607.12785)  

### 一句话总结
ExtraGS 通过引导扩散模型生成伪观测数据并采用置信度加权微调，增强了基于 3D 高斯溅射的内窥镜视图外推能力，显著减少了外推伪影。

### 研究问题
如何在机器人辅助微创手术中，利用有限的观察数据（内窥镜视频）实现高质量的视图外推（extrapolation），即合成训练轨迹之外的新视角，并减少伪影。

### 核心思路/方法
1. **初始重建**：使用 3D 高斯溅射（3D Gaussian Splatting）从内窥镜视频进行初始场景重建。  
2. **不确定性引导的虚拟相机采样**：主动探索观察盲区，最大化信息增益，生成可能包含未知区域的虚拟视角。  
3. **扩散模型细化**：使用扩散模型对虚拟视角的渲染结果进行精细化，恢复合理的解剖结构，产生“伪观测”数据。  
4. **置信度加权微调**：在将伪观测数据融入优化时，采用置信度加权策略，避免生成内容退化已有可靠区域。

### 主要贡献
- 提出了 ExtraGS 框架，结合 3D 高斯溅射与扩散模型，用于增强内窥镜视图外推。  
- 设计了不确定性引导的虚拟相机采样策略，以主动探索盲区。  
- 实现了置信度加权的微调策略，在引入伪观测时保持可靠区域的质量。  
- 在多个公开内窥镜数据集上达到了最先进的新视图合成性能，显著减少了外推伪影。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作聚焦于手术机器人内窥镜感知这一实际医疗应用，提出了一种结合 3D 高斯溅射与扩散模型的创新思路，增强了视图外推能力。摘要明确展示了问题定义、方法设计和实验验证，且实现了 state-of-the-art 性能，对手术场景中的神经渲染研究有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of the surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating beyond the training trajectory. In this work, we propose ExtraGS, a framework for enhancing endoscopic view extrapolation through diffusion-guided 3D Gaussian Splatting. Starting from an initial reconstruction, we introduce an uncertainty-guided virtual camera sampling strategy to actively explore blind spots and maximize information gain. The rendered views from these sampled locations are refined using a diffusion model to recover plausible anatomical structures, producing pseudo-observations that guide further optimization. To prevent the generated content from degrading reliable regions, we adopt a confidence-weighted fine-tuning strategy when incorporating these pseudo-observations. Extensive experiments on multiple public endoscopic datasets demonstrate that ExtraGS significantly reduces extrapolation artifacts and achieves state-of-the-art performance in endoscopic novel view synthesis.

</details>

#### 2026-07-14 - GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR

**Authors:** Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu
**Links:** [abs](https://arxiv.org/abs/2607.12641) - [pdf](https://arxiv.org/pdf/2607.12641)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR
- 作者：Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu
- 出版日期：2026-07-14T11:19:16Z
- 分类：主要：Neural Scene Representations & Rendering；次要：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2607.12641；PDF：https://arxiv.org/pdf/2607.12641

### 一句话总结
提出一个面向无线空中VR的几何感知跨层框架GeoFovea-GS，通过联合优化3DGS渲染与通信资源分配，在传输成本大幅降低的同时提升沉浸式渲染质量。

### 研究问题
现有无线空中VR在带宽、延迟和功率受限下难以生成高质量视图，且3DGS的几何误差会导致VR质量严重下降；此外，现有信道感知或像素级资源分配方案无法捕捉几何敏感的失真，因此需要一种能兼顾几何误差与通信效率的跨层优化方法。

### 核心思路/方法
1. 开发了一种**注视点几何感知失真度量**，统一表征光度渲染误差、几何不一致性和视图依赖的感知重要性。
2. 基于该度量，将纯姿态3DGS渲染与图像/瓦片纠正传输的联合选择，表述为**无线约束下的跨层优化问题**。
3. 设计了一个**轻量级信息价值调度器**，将通信资源优先分配给既几何关键又感知重要的区域。

### 主要贡献
- 提出了首个几何感知的跨层框架GeoFovea-GS，用于通信高效的无线空中VR。
- 设计了统一形式的注视点几何感知失真度量，联合考虑光度、几何和感知因素。
- 实现了在真实3DGS场景中，以显著降低的传输成本获得更优的沉浸式渲染质量。

### 局限性
摘要未提供关于框架在实时性、计算开销、不同场景泛化能力或与现有系统集成方面的局限性信息。

### 阅读优先级
**高**  
理由：该工作针对无线VR中渲染与通信的联合优化这一实际瓶颈，提出了新颖的几何感知跨层方法，且实验在真实3DGS场景上取得显著效果。对于从事神经渲染、VR通信、无线资源分配方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Wireless aerial virtual reality (VR) aims to provide immersive access to large-scale scenes, but high-resolution view generation and delivery are jointly constrained by limited bandwidth, latency, and power. 3D Gaussian Splatting (3DGS) can reduce the payload by rendering views from compact pose information, yet its geometry errors may cause severe VR quality degradation. Existing channel-aware or pixel-level resource allocation schemes fail to capture such geometry-sensitive distortion. To address this issue, this paper proposes GeoFovea-GS as a geometry-aware cross-layer framework for communication-efficient wireless aerial VR. A foveated geometry-aware distortion metric is developed to characterize photometric rendering error, geometric inconsistency, and view-dependent perceptual importance in a unified form. Based on this metric, the joint selection of pose-only 3DGS rendering and image/tile correction transmission is formulated as a cross-layer optimization problem under wireless constraints. A lightweight value-of-information scheduler is further developed to allocate communication resources to regions that are both geometry-critical and perceptually important. Experiments on real-world 3DGS scenes demonstrate that GeoFovea-GS achieves superior immersive rendering quality with substantially reduced transmission cost.

</details>

#### 2026-07-14 - Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots

**Authors:** Yanghe Hao, Martin Huber, Christos Bergeles, Tom Vercauteren
**Links:** [abs](https://arxiv.org/abs/2607.12604) - [pdf](https://arxiv.org/pdf/2607.12604)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** pose estimation, differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots
- 作者：Yanghe Hao, Martin Huber, Christos Bergeles, Tom Vercauteren
- 出版日期：2026-07-14
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.12604

### 一句话总结
本文通过优化立体可微渲染框架，实现了无标记、实时的外科手术机器人跟踪，速度达30 fps，精度与基于标记的方法相当。

### 研究问题
如何在无标记条件下，实现手术机器人实时、高精度的三维位姿跟踪，以克服传统基于标记的方法在杂乱手术室中易被遮挡的缺点。

### 核心思路/方法
在标记无关位姿估计框架roboreg基础上，引入两项改进：
1. 序列优化：通过运动自适应超参数调优，在帧间传播位姿估计。
2. CUDA流并行化：并行执行分割与优化，并用CUDA-graph加速分割过程。
最终实现立体可微渲染的在线动态跟踪。

### 主要贡献
- 实现了实时1080p、30 fps的跟踪速度（原框架仅14 fps），与相机帧率匹配。
- 静态精度达1.7 cm / 0.6度（与静态真值对比），动态参考下平均3D误差为1.2 cm（27,460帧）。
- 在遮挡场景下（1,242帧）平均误差为1.53 cm。
- 相比FoundationPose基线，动态估计提升11%（遮挡下提升63%），静态估计提升250%，且推理速度快6倍。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法解决了手术机器人无标记跟踪中的实时性与精度权衡问题，性能显著优于已有基线，且速度达到实际应用要求，对机器人辅助手术领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Purpose: Marker-based tracking of surgical robots is occlusion-prone in cluttered operating rooms. We evaluate stereo differentiable rendering for marker-free, real-time robot pose tracking, potentially improving safety, reducing setup time, and enabling multi-robot interaction. Methods: We extend the markerless pose estimation framework roboreg to online dynamic tracking via (i) sequential optimisation that propagates pose estimates across frames with motion-adaptive hyperparameter tuning, and (ii) CUDA stream parallelisation of segmentation and optimisation, combined with CUDA-graph accelerated segmentation. We evaluate on 38 unobstructed and 5 occluded displacement sequences with static start/end ground-truth calibrations and dynamic marker-based reference tracking. Results: We achieve real-time 1080p tracking at 30 fps (up from 14 fps for vanilla roboreg), matching the camera frame rate. Accuracy reaches 1.7 cm / 0.6 deg against static ground truth and 1.2 cm mean 3D error over 27,460 frames against the marker-based reference (1.53 cm over 1,242 occluded frames). Our method outperforms FoundationPose by 11% in dynamic estimation (63% under occlusion) and 250% in static estimation, with 6x faster inference. Conclusions: Stereo differentiable rendering enables real-time, high-resolution marker-free surgical robot tracking, on par with marker-based approaches and surpassing foundation-model baselines.

</details>

#### 2026-07-13 - MetaView: Monocular Novel View Synthesis with Scale-Aware Implicit Geometry Priors

**Authors:** Yufei Cai, Xuesong Niu, Hao Lu, Kun Gai, Kai Wu, Guosheng Lin
**Links:** [abs](https://arxiv.org/abs/2607.12000) - [pdf](https://arxiv.org/pdf/2607.12000)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** metric depth, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MetaView: Monocular Novel View Synthesis with Scale-Aware Implicit Geometry Priors  
- 作者：Yufei Cai, Xuesong Niu, Hao Lu, Kun Gai, Kai Wu, Guosheng Lin  
- 出版日期：2026-07-13  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2607.12000  

### 一句话总结
本文提出MetaView，一种基于扩散模型的单目新视角合成框架，通过结合隐式几何先验和度量深度线索，在保持几何一致性的同时实现大幅视点变化下的可控渲染。

### 研究问题
如何在单张图像输入下，实现大幅视角变化下的新视角合成，同时兼顾几何一致性、精确相机控制和高泛化能力。

### 核心思路/方法
- 引入隐式几何先验：利用前馈几何感知网络提取结构化约束，不依赖显式的重建管线。  
- 显式度量深度锚定：将生成过程锚定到度量尺度，增强精确控制能力。  
- 整体设计：融合隐式几何建模与最小必要的显式3D线索，在扩散框架下实现灵活性与约束的平衡。

### 主要贡献
- 提出了MetaView框架，在单目大幅视角变化下显著优于现有方法。  
- 展示出优越的泛化性能（摘要未提供具体数值或实验细节）。  
- 代码开源。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对视觉生成中空间结构感知这一关键问题提出创新解决方案，结合隐式几何先验与度量深度，方法设计合理且有明显性能提升，开源代码便于复现，适合对神经场景表示和生成式新视角合成感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

Current visual generation models are capable of producing high-quality content, yet they lack a coherent perception of the spatial structure. Existing generative novel view synthesis methods typically introduce explicit geometry priors, which enforce spatial consistency but inherently restrict generalization in large view changes. In contrast, recent interactive generative methods favor implicit scene modeling, offering greater flexibility at the cost of precise camera control and geometry consistency. In this paper, we propose MetaView, a diffusion-based monocular novel view synthesis framework that enables rendering under large view changes from a single image. Our key insight is to combine implicit geometry modeling with minimal yet essential explicit 3D cues: we incorporate implicit geometry priors from a feed-forward geometry perception network to regularize structure without imposing restrictive reconstruction pipelines, while leveraging metric depth to anchor the generation to a metric scale. This design allows MetaView to achieve both geometry consistency and precise controllability. Extensive experiments demonstrate that, under challenging monocular large viewpoint changes, MetaView significantly outperforms existing methods and exhibits superior generalization. Our code is publicly available at https://github.com/KlingAIResearch/MetaView.

</details>

#### 2026-07-13 - ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space

**Authors:** Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan
**Links:** [abs](https://arxiv.org/abs/2607.11673) - [pdf](https://arxiv.org/pdf/2607.11673)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** video reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space
- 作者：Mingchao Sun, Luyang Tang, Yu Liu 等34位作者
- 出版日期：2026-07-13
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）；具身/机器人/增强现实应用（Embodied / Robotics / AR Applications）
- 链接：[摘要](https://arxiv.org/abs/2607.11673) | [PDF](https://arxiv.org/pdf/2607.11673)

### 一句话总结
提出一个通用多模态3D世界模型，将文本、图像、视频输入转化为高保真、可探索的3D场景，并通过统一的空间生成基元（SGP）实现高效的3D空间描述。

### 研究问题
如何将多种输入模态（文本、图像、视频）转化为一致、高保真的可探索3D世界，并支持从稀疏输入（单张图片或句子）到丰富输入（多视图集、随意视频）的通用构建。

### 核心思路/方法
核心是“空间生成基元（SGP）”——一个包含高质量全景图与空间点云的紧凑元组。流程分三步：
1. **输入提升**：将多模态输入映射为SGP。丰富输入通过几何严格恢复实现场景重建；单图像或句子则通过生成式方法创造新世界。
2. **3D一致全景视频生成**：沿规划轨迹探索SGP，生成连续的3D一致全景视频。
3. **全景视频重建引擎**：将生成视频转换为清晰的逼真3D高斯泼溅（3DGS）世界。此外，支持将生成的世界锚定到地理兴趣点，实现地图原生的空间探索。

### 主要贡献
1. 提出通用多模态3D世界模型，统一处理文本、图像、视频输入。
2. 引入紧凑的空间生成基元（SGP），高效描述任意3D空间。
3. 在高质量全景图与点云基础上，通过全景视频生成与3DGS重建，实现高保真场景。
4. 在稀疏输入（单图像/句子）上支持创造性生成，在丰富输入上实现几何严格恢复。
5. 将生成世界锚定到地理兴趣点，具备消费级地图原生探索能力。
6. 实验表明，在丰富多模态输入下，该方法在开源方法中达到最优，场景保真度优于Marble。

### 局限性
摘要未提供充分信息。例如未讨论多视图一致性、生成速度、对复杂场景的鲁棒性、训练数据依赖或失败模式。

### 阅读优先级
中  
理由：该方法在3D场景生成领域具有新颖性，提出统一的SGP基元并支持地理锚定，适合关注多模态3D内容创作的研究者。但由于发布时间为2026年，方法细节和实验仅基于摘要概要，可先阅读全文评估实用性与局限性。对纯应用或工程导向的读者优先级可降低。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：HyperGS: Fast and Generalizable Gaussian Video Representation
- 作者：Fatimah Zohra, Chen Zhao, Shuming Liu, Yahya Al Malallah, Bernard Ghanem
- 出版日期：2026-07-13
- 分类：Neural Scene Representations & Rendering
- 链接：abstract: https://arxiv.org/abs/2607.11500, pdf: https://arxiv.org/pdf/2607.11500

### 一句话总结
HyperGS 提出一种前馈式、免优化的高斯视频表示方法，通过因子化时空Transformer和可学习查询Transformer直接从视频预测高斯参数，实现极快编码与跨视频的零样本泛化。

### 研究问题
现有基于高斯泼溅的视频表示方法依赖逐视频优化，导致编码速度慢且难以跨视频泛化。HyperGS 旨在解决如何在不执行逐视频优化的前提下，快速生成可泛化的高斯视频表示。

### 核心思路/方法
1. **前馈预测架构**：设计一个因子化时空Transformer从输入视频提取token，再通过一个基于可学习查询的Transformer为每一帧预测8参数的高斯表示。
2. **秩几何正则化**：针对直接预测时出现的“针状退化”导致训练崩溃的问题，提出一种自适应强度动态调整的秩基几何正则化器，稳定优化过程。
3. **零样本高分辨率渲染**：模型能直接泛化到未见过的分布及720p视频，无需重新编码即可进行更高分辨率渲染。

### 主要贡献
- 提出第一个前馈式、免优化高斯视频表示方法，实现编码速度相比逐视频优化提升4到5个数量级（10^4–10^5×），同时保持匹配的重建质量。
- 在K400、SSv2、UCF101等基准上，以更小的视频表示尺寸，将PSNR提升+2.9–3.1 dB（相比此前视频编码器）。
- 展示了高斯泼溅在前馈预测下的泛化能力，结合了快速灵活渲染与前馈预测的速度和通用性。

### 局限性
摘要未提供关于模型在处理超长视频、内存消耗、或对复杂动态场景（如剧烈遮挡、快速运动）的具体表现细节。摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法显著加快了高斯视频表示的编码速度（数个数量级），并通过零样本泛化支持高分辨率视频，性能在多个基准上大幅优于此前方法，对于追求实时或可泛化视频表示的研究与应用有重要参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling
- 作者：Yingji Zhong, Dave Zhenyu Chen, Fuzhao Ou, Youyu Chen, Zhihao Li, Lanqing Hong, Dan Xu
- 出版日期：2026-07-13
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.10995

### 一句话总结
本文提出一种非对称的3D高斯泼溅架构，通过分离几何与外观建模来减少计算冗余，在长序列新视角合成任务中实现效率大幅提升。

### 研究问题
如何减少现有可泛化3D高斯泼溅模型在长序列新视角合成中的冗余计算，同时保持或提升渲染质量。

### 核心思路/方法
基于两个观察：（i）高质量NVS不严格要求高精度几何；（ii）外观学习通常比几何恢复更容易。因此设计非对称架构，将几何建模和外观建模解耦：
- 几何分支：使用粗粒度token和大部分参数进行多视图重建。
- 外观分支：使用细粒度token和显著更少的参数捕捉细节。
- 两个分支通过双边连接交互，实现任务间的相互指导。

### 主要贡献
1. 提出任务感知的非对称架构，有效减少计算冗余并更合理地分配计算资源。
2. 在32视图960P输入下，模型匹配优化方法的质量，同时实现近800倍加速。
3. 超越现有可泛化模型的零样本性能，参数更少、训练/推理开销更低，整体效率提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该工作针对长序列场景建模中计算冗余的关键问题，提出了清晰且新颖的非对称架构设计，在效率（800倍加速）和性能（匹配优化方法）上均有显著突破，对NeRF/3D高斯泼溅领域的研究者和实践者有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：DP-Splat: Bayesian Nonparametric Complexity Control for Gaussian Splatting
- 作者：Aqi Dong
- 出版日期：2026-07-12
- 分类：神经场景表示与渲染
- 链接：https://arxiv.org/abs/2607.10912

### 一句话总结
本文提出DP-Splat，通过引入截断狄利克雷过程先验（截断stick-breaking）和稀疏过拟合有限狄利克雷先验，使3D高斯溅射中高斯成分的数量能够自适应场景复杂度，同时保持闭式坐标上升更新。

### 研究问题
3D高斯溅射中，高斯成分数量K通常由启发式的密度控制或用户上限设定，缺乏基于数据自适应调整的理论基础。现有变分贝叶斯方法（如VBGS）虽将溅射拟合转为共轭变分推断，但K仍固定不变。

### 核心思路/方法
1. 将有限对称狄利克雷先验替换为截断stick-breaking狄利克雷过程先验，以及作为理论替代的稀疏过拟合有限狄利克雷先验，使被占用的成分数量自适应数据。
2. 所有更新保持闭式坐标上升步骤；提出自然梯度随机变体，使得每步计算成本与数据点数无关。
3. 给出了精确单调性保证、严格的截断误差界（纠正了常见大α近似中过于保守的问题），并对拟合的成分数量估计含义进行诚实分析。

### 主要贡献
1. 理论贡献：提供了精确单调性证明、严格的截断误差界，并区分了变分实践与后验渐近理论之间的差距（在N三个数量级范围内证实）。
2. 实验贡献：
   - 有效复杂度K^自适应场景复杂度，在分离良好的合成数据上恢复真实K（误差±1）。
   - 在解混淆比较中，DP先验的贡献主要来自复杂度选择而非逐成分效率：在匹配预算下，收敛的DP拟合超过单次固定K的VBGS +2.7 dB，而与同样收敛的固定K基线持平；在3D场景中，DP-Splat以5.9-7.6倍更少的成分达到或超过VBGS的保留颜色预测。
   - 后验预测颜色方差在模型匹配的合成数据上校准良好。
   - 在均场坐标上升下，DP先验抵抗过度分裂而稀疏有限混合达到截断饱和，揭示了变分实践与后验渐近之间的差异。

### 局限性
摘要未提供任何关于方法局限性、潜在失败场景或计算资源需求的信息。

### 阅读优先级
高。
理由：该方法从贝叶斯非参数角度解决了高斯溅射中成分数量自动选择的核心问题，具有理论保证（单调性、截断误差界）和明确的实验优势（成分数量减少5.9-7.6倍且性能匹配/超越基线）。对神经场景表示和变分推断领域均有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting represents scenes as finite mixtures of anisotropic Gaussians whose number of components $K$ is set by heuristic density control or user caps. Variational Bayes Gaussian Splatting (VBGS) recast splat fitting as conjugate variational inference, but $K$ remains fixed. We replace the finite symmetric Dirichlet over mixture weights with a truncated stick-breaking Dirichlet-process prior -- and, as a theory-backed alternative, a sparse overfitted finite Dirichlet -- so that the number of occupied components adapts to the data while every update remains a closed-form coordinate-ascent step; a natural-gradient stochastic variant makes the per-step cost independent of the number of points. We give an exact monotonicity guarantee, a rigorous truncation-error bound correcting an anti-conservative large-$α$ approximation in common use, and an honest account of what the fitted number of components estimates. Empirically: (i) the effective complexity $\hat{K}$ adapts to scene complexity and recovers the true $K$ within $\pm 1$ on well-separated synthetic data with regime-appropriate concentration; (ii) a deconfounded comparison shows the DP prior's contribution is complexity selection, not per-component efficiency -- converged DP fits exceed single-pass fixed-$K$ VBGS by +2.7 dB at matched budgets yet tie an equally converged fixed-$K$ baseline, and on 3D scenes DP-Splat matches or exceeds VBGS's held-out color prediction with 5.9-7.6x fewer components; (iii) the posterior-predictive color variance is well calibrated on model-matched synthetic data; and (iv) the ordering suggested by exact-posterior asymptotics reverses under mean-field coordinate ascent: the DP prior resists over-splitting while the sparse finite mixture saturates its truncation, a gap between variational practice and posterior asymptotics documented across three orders of magnitude in $N$.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

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

#### 2026-07-14 - More Than Where You Are: Learning Semantics, Structure, and Geometry from Cross-View Localization

**Authors:** Mao Chen, Xiangkai Zhang, Zhiyong Liu, Chuankai Liu, Xu Yang
**Links:** [abs](https://arxiv.org/abs/2607.12429) - [pdf](https://arxiv.org/pdf/2607.12429)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reasoning, pose estimation, localization, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：More Than Where You Are: Learning Semantics, Structure, and Geometry from Cross-View Localization
- 作者：Mao Chen, Xiangkai Zhang, Zhiyong Liu, Chuankai Liu, Xu Yang
- 出版日期：2026-07-14
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.12429

### 一句话总结
本文提出CROSS框架，将跨视角定位问题重新定义为不仅仅是位姿估计，而是学习跨极端视角变化的稳定语义、可靠结构和可迁移几何。

### 研究问题
如何克服现有跨视角定位方法在极端视角变化下缺乏3D基础、依赖严格点匹配削弱语义一致性、以及绝对目标对几何推理指导有限等局限性，以建立一致的跨视角理解能力。

### 核心思路/方法
提出CROSS统一框架，通过三个关键组件来解决上述局限性：
1. **3D基础对齐（3D-grounded alignment）**：引入明确的3D基础，使结构学习成为内在需求。
2. **结构感知匹配（structure-aware matching）**：替代严格点匹配，鼓励语义表示保持稳定。
3. **假设排序（hypothesis ranking）**：提供更灵活的几何推理指导，使模型获得可迁移的几何能力。

### 主要贡献
1. 重新定义了跨视角定位的目标，即学习跨视角的稳定语义、可靠结构和可迁移几何，而不仅是位姿估计。
2. 识别并克服了现有方法的三大关键局限性。
3. 提出CROSS框架，在KITTI和VIGOR数据集上达到跨视角定位的最新性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文直接回应了跨视角定位在极端视角变化下的核心挑战，提出统一框架并在多个数据集取得最优结果，对空间智能、机器人及增强现实应用具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Consistent cross-view understanding under extreme viewpoint changes is essential for spatial intelligence, as it enables models to recognize the same scene across extreme viewpoint gaps. Cross-view localization naturally provides a promising pathway toward this ability, as it requires a model to align ground-view imagery with geo-referenced satellite-view imagery despite drastic appearance changes to estimate camera poses. Recent visual foundation models have made this long-standing localization problem increasingly feasible by providing rich 2D representations for cross-view matching. However, we argue that cross-view localization should not be viewed merely as 2D matching or pose estimation. In this work, we revisit cross-view localization as more than pose estimation and investigate how it can help the model develop consistent cross-view understanding under extreme viewpoint changes, including stable semantics, reliable structure, and transferable geometry. We identify three key limitations of existing methods that prevent them from achieving this. They usually lack explicit 3D grounding, rely on strict point-wise matching that can weaken semantic consistency, and learn from an absolute objective that provides limited guidance for geometric reasoning. To address these limitations, we propose CROSS, a unified cross-view localization framework built upon 3D-grounded alignment, structure-aware matching, and hypothesis ranking. This formulation makes structure learning an intrinsic requirement, encourages semantic representations to remain stable, and enables the model to acquire transferable geometry. Extensive experiments on the KITTI and VIGOR datasets show that CROSS achieves state-of-the-art performance in cross-view localization. More importantly, CROSS effectively learns stable semantics, reliable structure, and transferable geometry across extremely different viewpoints.

</details>

#### 2026-07-14 - VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation

**Authors:** Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang
**Links:** [abs](https://arxiv.org/abs/2607.12356) - [pdf](https://arxiv.org/pdf/2607.12356)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation
- 作者：Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang
- 出版日期：2026-07-14
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.12356

### 一句话总结
VistaVLA提出一种两阶段框架，通过将多视图视觉-语言特征提升为3D高斯基元并压缩为紧凑语义令牌，使VLA模型获得几何与语义感知的3D认知表示，显著提升机器人操作任务的成功率。

### 研究问题
现有的视觉-语言-动作（VLA）模型缺乏显式的场景级3D表示，难以对空间布局和几何约束进行推理；仅引入深度图或点云等方法虽增强了几何感知，但缺少3D空间中的高层语义信息，限制了机器人与物理世界的交互认知能力。

### 核心思路/方法
1. **3D高斯基元构建**：将多视图视觉-语言特征投影到3D高斯基元中，形成几何锚定的语义令牌，建立与视图一致的3D空间映射与2D视觉特征空间的联系。
2. **Merge-then-Query（MtQ）令牌压缩**：设计一种令牌摘要机制，将密集的3D高斯基元压缩为一组高度紧凑的空间信息令牌，实现99%的令牌缩减，同时保留与动作相关的3D布局和语义上下文。
3. **两阶段框架**：第一阶段构建几何与语义感知的3D认知表示，第二阶段将该表示作为紧凑的上下文令牌输入VLA策略学习网络。

### 主要贡献
- 提出首个构建几何与语义感知3D认知表示的VLA框架，用于机器人操作任务。
- 设计MtQ机制，实现密集3D高斯基元到紧凑令牌的高效压缩，显著降低计算开销。
- 在仿真和真实世界环境中验证有效性：真实场景下，在7个任务上平均成功率提升22.8%，在分布外任务上比VLA-Adapter基线提升30.0%。

### 局限性
摘要未提供关于模型泛化能力、计算复杂度、失败模式分析或更多实验设置（如训练数据规模、实时性）的详细信息。

### 阅读优先级
**高**  
理由：该工作在VLA模型领域引入了创新的3D认知表示方法，并结合高效的令牌压缩技术，在真实环境中取得了明显的性能提升，对机器人操作与具身智能研究具有较强的参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions. However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints. While recent efforts incorporate explicit 3D cues, such as depth maps or point clouds, to improve geometric awareness, they primarily capture low-level structures and lack high-level semantic grounding in 3D space. In human cognition, interaction with the physical world relies on a 3D semantic cognitive map - an internal mental model that integrates spatial layouts with semantic context to enable persistent, viewpoint-invariant reasoning. In light of this, we present VistaVLA, a novel two-stage framework that constructs a geometry- and semantics-aware 3D cognitive representation from 3D Gaussian primitives and grounds it as compact context tokens for VLA policy learning. Specifically, VistaVLA lifts multi-view vision-language features into 3D Gaussian primitives, forming geometry-anchored semantic tokens that align view-consistent spatial grounding with 2D visual feature spaces. To make this 3D representation computationally tractable for effective VLA control, we introduce Merge-then-Query (MtQ), a token summarization mechanism. MtQ compresses dense Gaussian primitives into a highly compact set of spatially informative tokens, achieving a 99% token reduction while preserving action-relevant 3D layouts and semantic context. Extensive evaluations in both simulated and real-world environments demonstrate the effectiveness of VistaVLA. Notably, in real-world scenarios, VistaVLA improves success rates by 22.8% across seven real-world tasks and by 30.0% over the VLA-Adapter baseline on challenging out-of-distribution tasks.

</details>

#### 2026-07-13 - Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model

**Authors:** Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li
**Links:** [abs](https://arxiv.org/abs/2607.11643) - [pdf](https://arxiv.org/pdf/2607.11643)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model
- 作者：Xinghang Li, Jun Guo, Qiwei Li 等
- 出版日期：2026-07-13
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.11643

### 一句话总结
本文介绍了一个380亿参数的多模态自回归模型，将基础图像/视频生成统一扩展到具身场景生成、具身迁移和具身视频生成，在单步与序列生成任务上达到最先进效果，并在真实世界操作任务中显著提升了策略的成功率。

### 研究问题
如何将大规模预训练的基础图像与视频生成模型的泛化能力和可控性，有效地迁移到具身场景中，同时满足多视角一致性、几何连贯性和机器人本体约束。

### 核心思路/方法
- 构建一个380亿参数的多模态自回归模型（Xiaomi-Robotics-U0）。
- 将具身生成视为基础图像与视频生成的扩展，统一优化文本到图像生成、图像编辑、具身场景生成、具身迁移和具身视频生成五个任务。
- 采用统一框架，在保留预训练世界基础模型泛化能力的同时，使其适应具身设定。
- 支持跨多种机器人本体的高质量多视角场景生成，并引入结构化、可控的具身迁移，实现细粒度编辑并保持多视角一致性与交互动态。

### 主要贡献
- 第一个支持多种机器人本体的高质量多视角场景生成的模型。
- 引入结构化、可控的具身迁移，实现细粒度编辑并保持多视角一致性。
- 在单步和序列生成任务上达到最先进结果：人类评估中在具身场景生成与迁移上优于GPT-Image-2.0；具身视频生成在World Arena排名第一；在真实世界操作任务中将 pi_0.5 的分布外成功率从36.9%提升至63.2%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作在具身智能建模中首次实现了多任务统一的巨大参数模型，并在多个任务上取得了显著的性能提升和实际部署验证，对具身场景生成、机器人数据引擎构建有重要参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：SegDiff: Segmented Trajectory Diffusion for Consistent and Adaptive Robot Manipulation
- 作者：Haidong Cao, Wenjun Cao, Quanhao Li, Sicheng Xie, Zhiying Du, Jiaqi Leng, Zuxuan Wu, Yu-Gang Jiang
- 出版日期：2026-07-13
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页面 https://arxiv.org/abs/2607.11027 | PDF https://arxiv.org/pdf/2607.11027

### 一句话总结
本文提出SegDiff，一种结合连续轨迹预测与关键位姿预测优点的闭环视觉运动策略，利用扩散模型和DDIM反演实现长时间范围内的稳定、自适应的机器人操作。

### 研究问题
现有模仿学习方法分为两类：预测短视界连续动作序列（易累积误差且难以处理多模态动作分布）和预测离散关键位姿（需外部规划器，限制实时性）。本文旨在解决这两类方法各自的局限，实现既能长期预测又能实时自适应、控制稳定的操作策略。

### 核心思路/方法
1. **分段轨迹扩散**：将演示分解为关键位姿之间的运动片段，学习从当前状态到下一个关键位姿的连续轨迹预测，从而实现长视界预测并支持实时精化。
2. **动态时间集成机制**：利用扩散模型和DDIM反演的能力，提出一种机制，使策略能够高效响应动态环境，同时缓解因多模态采样不一致导致的轨迹不连续问题。整体策略为闭环视觉运动策略。

### 主要贡献
1. 提出SegDiff框架，集成连续轨迹与关键位姿两种范式的优势，提升长时依赖推理与实时适应性。
2. 引入动态时间集成机制，借助扩散模型与DDIM反演，增强对动态环境的响应能力并减少轨迹不连续性。
3. 在多个模拟和真实场景中，SegDiff相比现有方法取得了显著性能提升，验证了其在长期时间依赖推理、实时适应性和控制稳定性方面的优势。

### 局限性
摘要未提供足够信息：未明确讨论实验的失败案例、对特定任务/场景的局限性、计算成本、模型泛化边界或与其他方法的详细对比数据。

### 阅读优先级
**高**：理由：该论文针对机器人模仿学习中的核心矛盾（长视界预测与实时性、连续/离散预测的权衡）提出了创新性的融合方案，且方法在模拟和真实场景中均验证有效，对具身智能和机器人操作领域的研究具有潜在重要参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：PrismAD: Decoupled Planning via Semantic Mixture-of-Planners for End-to-End Autonomous Driving
- 作者：Kang Ding, Zhigui Lin, Hongsong Wang, Jie Gui, Qi Liu, Zhe Wang, Luqi Tang, Lei He
- 出版日期：2026-07-11
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.10336

### 一句话总结
PrismAD 提出一种基于语义混合规划器的解耦式端到端自动驾驶框架，通过将场景token按语义分组并分配给独立专家，提升运动规划和自我规划效果。

### 研究问题
现有端到端规划器将异构场景token聚合到耦合表示空间，迫使单一规划分支联合建模智能体交互、道路几何和驾驶意图，这削弱了各因素具体推理能力，并模糊了不同规划线索的贡献。

### 核心思路/方法
- 将场景token划分为交互、几何、意图三组，分别分配给参数独立但架构相同的专家。
- 每个专家学习特定规划子任务（运动预测或自我规划）的表示。
- 引入语义感知路由器，自适应地为运动预测和自我规划分配不同的路由权重，聚合专家预测。
- 采用稀疏Top-K激活和噪声门控，提升路由鲁棒性并减少不必要的专家计算。

### 主要贡献
- 提出解耦规划范式，通过语义分组和独立专家增强各规划线索的专用推理。
- 设计混合专家路由机制，在运动预测和自我规划间动态分配权重，实现自适应聚合。
- 在nuScenes开放循环数据集和NeuroNCAP闭合循环基准上展示出竞争性能。

### 局限性
摘要未提供关于模型局限性、失败案例或计算复杂度的具体信息。

### 阅读优先级
中。理由：该工作聚焦端到端自动驾驶规划中的表示解耦问题，方法设计清晰（混合专家架构），但性能仅描述为“竞争性”，未给出量化对比细节；同时摘要长度较短，缺少充分的实验验证说明，适合对解耦规划范式感兴趣的读者初步了解，但需阅读全文才能评估实际效果优势。

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
