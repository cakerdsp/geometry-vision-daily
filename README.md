# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：74
- 分类分布：
  - Neural Scene Representations & Rendering: 25
  - 3D Reconstruction & Multi-view Geometry: 21
  - Embodied / Robotics / AR Applications: 20
  - Geometry Foundation Models: 4
  - Dynamic / 4D Reconstruction: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，以下是根据您提供的论文列表生成的中文科研趋势综合分析。

---

#### 今日主要趋势

1.  **多模态与几何先验深度融合，提升稀疏/退化场景下的鲁棒性**：传统方法在稀疏输入、弱光或无纹理场景下容易失效。今日多篇论文通过引入非传统传感器模态（如热红外、声纳）或显式几何先验（如LiDAR平面、亚特兰大世界假设、可见域约束）来克服这一难题。例如，`LIT-GS` 融合热成像，`VisDom` 引入可见域几何约束，`MMD-SLAM` 利用亚特兰大世界假设引导场景结构，展示了将“非视觉”信息或强几何假设注入神经表达是提升系统鲁棒性的核心路径。

2.  **世界模型与智能体向“具身空间智能”演进，强调结构与对称性**：世界模型已不满足于单纯的视频生成，而是朝可控、具备空间推理能力的智能体方向发展。`Holo-World` 实现了对相机、物体和天气的联合控制；`S-Agent` 将空间推理建模为证据累积过程；`SWAP` 则通过编码对称等变性来提升机器人运动策略的效率。这表明研究焦点从生成静态或动态画面，转向构建能理解、推理并与三维世界交互的“空间大脑”。

3.  **高斯泼溅（3DGS）成为多模态感知与任务执行的“统一坐标系”**：3DGS已超越新视角合成的范畴，成为连接不同传感器和任务的几何代理。`LIT-GS` 利用LiDAR平面正则化GS；`Geometry-Preserving in 3DGS` 专为LiDAR-相机标定保留GS的度量几何；`One Demo` 利用GS为机器人数据增广；`Building Drift` 则用GS记录建筑现场变形。3DGS正从一个渲染工具演变为一个可微、灵活、能承载多源信息的核心“几何基座”，其高保真度与可编辑性使其在标定、建图、仿真、文档化等下游任务中展现出巨大潜力。

4.  **视觉语言模型（VLM）的3D感知路径更趋“轻量”与“无感”**：为避免将3D几何编码器强耦合进VLM，新方法倾向于从2D图像中隐式地或通过简单变换构建3D感知。`Occ-VLM` 仅用RGB图和2D编码器，通过重建3D占用作为几何先验；`OneCanvas` 则将多视图特征投影到全景画布，使得预训练VLM能直接像处理2D图像一样理解3D空间。这种“去3D编码器”的趋势，旨在以最小代价让语言模型获得3D理解能力，降低了部署门槛。

5.  **从“合成数据”到“真实数据”，并关注高保真物理仿真**：多个工作强调了在真实数据上训练或使用真实物理原理计算的重要性。`TIDY` 在真实热红外数据对而非合成噪声上训练去噪网络；`TaCauchy` 从第一性原理计算触觉力，而非经验估计；`CalTennis` 提供了带有动作捕捉级真值的大规模真实多视角数据集。这反映了社区对“仿真到真实”鸿沟的清醒认识，并积极通过真实数据和物理仿真来提高模型的可信度与泛化能力。

#### 技术路线观察

| 技术方向 | 侧重点 | 代表论文 |
| :--- | :--- | :--- |
| **3D 重建与多视图几何** | **鲁棒性与大规模基准**：侧重解决大尺度、稀疏、多模态、非固定结构（如水下洞穴、植物分支）场景的稳定重建，并提供大规模真实运动数据集用于基准测试。 | `CalTennis`， `Towards 3D karst`， `MMD-SLAM`， `TIDY`， `Modeling Branches`， `Hardware-...Maritime` |
| **神经场景表示与渲染** | **结构与约束**：重点在于向NeRF和3DGS中注入强几何约束（如平面、可见域）或可编辑的结构信息（如网格、潜粒子），以解决稀疏视图、漂移和编辑问题，使其从“表现”走向“理解”和“可控”。 | `VisDom`， `LIT-GS`， `Geometry-Preserving`，`MMD-SLAM`， `3D-DLP`， `NeuMesh++`， `One Demo`， `Building Drift` |
| **具身/机器人/AR应用** | **智能体与交互**：核心是构建能进行空间推理、精细操作、并适应动态环境的智能体。技术路线包括：赋予VLM空间认知能力的轻量级架构、利用对称性和材料参数等先验的运动规划、用于仿真和训练的高保真物理和视觉仿真框架。 | `S-Agent`， `Holo-World`， `SWAP`， `TaCauchy`， `Occ-VLM`， `OneCanvas`， `Modeling Branches` |
| **几何基础模型** | **应用迁移**：该类别下的工作较少，主要是将传统或经典的几何特征（如SIFT）应用于新领域（如艺术技能评估）。 | `Evaluation of Image Matching` |

**整体来看，今日论文的技术路线呈现“融合”与“解耦”的并行趋势。** “融合”指将不同模态（热、声纳、力、惯性）和多源信息（点线特征、几何先验）与神经表达（NeRF/3DGS）结合；“解耦”指在神经表达中分离几何、纹理、语义、运动等属性，或让VLM的3D感知能力与2D预训练解耦，从而提升可控性和训练效率。

#### 值得优先阅读的论文

1.  **`LIT-GS`**：**优先原因**：它代表了一种极具前景的鲁棒建图范式——用热红外替代或补充可见光，并用LiDAR平面几何作为锚点，解决了黑暗、低纹理场景下的核心痛点。对于从事自动驾驶、机器人巡检或任何在非理想光照条件下工作的研究者，该方法论具有启发性，且将LiDAR几何约束引入GS优化过程的设计精巧。
2.  **`S-Agent`**：**优先原因**：它从根本上重构了“空间智能”问题，将其视为一个多步、证据累积的推理过程，而非一次性预测。这种“推理而非识别”的范式转变，对于希望让VLM具备真正空间理解能力的研究者和工程师极具价值。生成的S-300K轨迹数据集本身也是一个重要贡献。
3.  **`SWAP`**：**优先原因**：它在四足机器人领域取得了破纪录的实证成果，并提出“对称等变性”这一简洁而强大的结构先验。该思想不仅对机器人学有价值，对任何需要从数据中高效学习几何规律（如3D重建、场景理解）的领域都有借鉴意义。
4.  **`OneCanvas`**：**优先原因**：它在“让VLM理解3D”的难题中，提供了一个优雅、低成本的解决方案。不去修改庞大而复杂的VLM，而是通过全景画布投影和3D位置编码，巧妙地让VLM在既有的2D能力基础上“无感”地获得了3D空间感。其简洁性和有效性使其具有很强的可复制和推广潜力。
5.  **`VisDom`**：**优先原因**：它提出一个通用、无需学习的几何约束（可见域）。这个约束简单到可以用几句话解释，却能在稀疏新视角合成中显著提升几何一致性。它是一个高性能、零学习成本的“插件”，对于任何需要处理稀疏输入的管线（如NeRF、3DGS、SLAM）都是宝贵的补充。

#### 可能的研究机会

1.  **多模态几何先验的通用框架**：`VisDom`（可见域）和`LIT-GS`（LiDAR平面）分别使用了不同的几何先验。一个潜在的通用框架是将多种此类“弱几何约束”模块化，并让系统自动选择或加权它们，从而适用于各种退化场景（如水下声纳+LiDAR+热成像联合建图）。
2.  **“物理启发的” 3DGS 用于机器人交互**：`TaCauchy` 将

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-19T11:41:11-04:00
**Total number of papers:** 74
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

### 2026-06

#### 2026-06-18 - Evaluation of Image Matching for Art Skills Assessment

**Authors:** Asaad Alghamdi, Michael Poor, Trung-Nghia Le, Tam V. Nguyen
**Links:** [abs](https://arxiv.org/abs/2606.20199) - [pdf](https://arxiv.org/pdf/2606.20199)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** image matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evaluation of Image Matching for Art Skills Assessment
- 作者：Asaad Alghamdi, Michael Poor, Trung-Nghia Le, Tam V. Nguyen
- 出版日期：2026-06-18
- 分类：Geometry Foundation Models (主要) / 3D Reconstruction & Multi-view Geometry (次要)
- 链接：https://arxiv.org/abs/2606.20199

### 一句话总结
本文提出通过图像匹配（SIFT特征与孪生网络）来评估手绘与模板之间的相似度，以衡量绘画技能水平。

### 研究问题
如何利用计算机视觉技术，通过比较手绘图像与原始模板的相似度，客观、高效地评估绘画技能。

### 核心思路/方法
1.  将手绘图像与原始模板进行匹配。
2.  实现并对比两种图像相似度度量方法：基于SIFT特征的关键点匹配，以及基于孪生网络的方法。
3.  通过分析特征匹配结果来推断绘画技能水平。

### 主要贡献
1.  提出了一种基于图像匹配的绘画技能评估方法，旨在简化传统繁琐的评估流程。
2.  实验比较了SIFT特征与孪生网络在衡量手绘与模板图像相似度上的表现。
3.  实验结果表明，SIFT特征的关键点匹配在检测绘画技能方面更为有效，从而验证了该方法评估艺术技能水平的可行性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：方法具有实际应用价值，且比较了经典（SIFT）与前沿（孪生网络）技术，但摘要未提供具体实验结果、评估指标、数据集规模等关键细节，且发表于未来时间，需谨慎核实。

</details>

<details>
<summary>Abstract</summary>

While some individuals possess a natural talent for drawing, mastering this skill requires dedicated training and practice. Determining one's skill in the art of drawing requires proper comprehensive assessment. In this paper, we propose a method to measure drawing skill by by matching the hand-drawn image with the original template. Existing techniques often involve complex processes. However, advancements in computer vision allow us to train computers to perform these comparisons at a human-like level, thereby resolving the tedious and overwhelming traditional process. Using computer vision applications, determining image similarity involves identifying the level of similarities in an image with a reference image. We have implemented and analyzed the SIFT feature and Siamese network to measure image similarity. Our results indicate that it is feasible to assess art skill levels. Through feature analysis, we found that SIFT-based key point matching provides a more effective means of detecting drawing skills.

</details>

#### 2026-06-16 - RegimeVGGT: Layer-Wise Spatially Preserving Redundancy Removal for Visual Geometry Grounded Transformer

**Authors:** Jinhao You, Shuo Lyu, Zhuohang Lyu, Tanxuan Li, Zibo Zhao, Jiaxiang Hu, Kai Tang, Yichen Guo
**Links:** [abs](https://arxiv.org/abs/2606.18439) - [pdf](https://arxiv.org/pdf/2606.18439)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** visual geometry grounded transformer, VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RegimeVGGT: Layer-Wise Spatially Preserving Redundancy Removal for Visual Geometry Grounded Transformer
- 作者：Jinhao You, Shuo Lyu, Zhuohang Lyu, Tanxuan Li, Zibo Zhao, Jiaxiang Hu, Kai Tang, Yichen Guo
- 出版日期：2026-06-16
- 分类：Geometry Foundation Models
- 链接：摘要：https://arxiv.org/abs/2606.18439；PDF：https://arxiv.org/pdf/2606.18439

### 一句话总结
RegimeVGGT 提出一种无训练的分层加速方法，通过识别 VGGT 网络中三层不同的冗余模式并对其进行修剪，实现了6.7倍加速且不降低重建质量。

### 研究问题
如何在不经过额外训练的前提下，减少 VGGT 中二次交叉帧注意力的计算开销，同时保持多视图场景三维重建的准确性？

### 核心思路/方法
1. **诊断性分析**：通过频谱、探针和因果分析，发现 VGGT 网络中存在三种不同的层级行为模式（regime）——浅层缺乏跨视图结构、中层驱动跨视图对齐、深层对密集几何冗余但对姿态重要。
2. **分轴压缩**：沿两层维度（token 空间和特征通道/时序维度）应用层级的 U 形压缩策略：
   - **Saliency-Guided Banded Merging**：保护几何和边缘显著 token 的完整性。
   - **Selectively Protected K/V Downsampling**：通过相位偏移空间网格、参考帧锚点和未压缩的相机/注册 token，保留跨帧空间覆盖和姿态关键路径。

### 主要贡献
- 揭示了 VGGT 网络中跨层冗余的非均匀分布，识别出三种不同的冗余处理机制。
- 提出无训练、分层的 U 形压缩方法，同时沿两个轴线（token 和 K/V）进行选择性保留与压缩。
- 实验表明，在匹配原始 VGGT* 重建质量的条件下，实现 6.7 倍速度提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法针对当前视觉几何基础模型（VGGT）的核心效率瓶颈提出解决方案，且无需重新训练，实用性较强；分层冗余分析视角具有理论启发性。对关注点云重建、多视图几何或高效 Transformer 部署的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Visual Geometry Grounded Transformer (VGGT) recovers dense 3D scene structure from multi-view images in one forward pass, but quadratic cross-frame attention limits its scalability. Existing training-free accelerators reduce computation uniformly along one axis, missing layer heterogeneity. Our spectral, probing, and causal analyses reveal three regimes: shallow layers lack cross-view structure, middle layers drive cross-view alignment, and deep layers are redundant for dense geometry yet their cross-frame attention remains essential for pose. RegimeVGGT applies layer-wise U-shaped compression along two axes: Saliency-Guided Banded Merging protects geometry- and edge-salient tokens, while Selectively Protected K/V Downsampling preserves cross-frame spatial coverage and the pose-critical path through a phase-shifted spatial grid, a reference-frame anchor, and uncompressed camera/register tokens. Training-free, RegimeVGGT achieves a 6.7x speedup over VGGT* at matched reconstruction quality.

</details>

#### 2026-06-15 - SurroundNEXO: Ego-Centric Metric Bridging for Spatially Consistent Geometry in Autonomous Driving

**Authors:** Shuai Yuan, Runxi Tang, Yuzhou Ji, Fudong Ge, Hanshi Wang, Yifei Wang, Xianming Zeng, Jianyun Xu, Xingliang Liu, Yanfeng Wang, Zhipeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.16960) - [pdf](https://arxiv.org/pdf/2606.16960)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth prediction, metric depth, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SurroundNEXO: Ego-Centric Metric Bridging for Spatially Consistent Geometry in Autonomous Driving
- 作者：Shuai Yuan, Runxi Tang, Yuzhou Ji, Fudong Ge, Hanshi Wang, Yifei Wang, Xianming Zeng, Jianyun Xu, Xingliang Liu, Yanfeng Wang, Zhipeng Zhang
- 出版日期：2026-06-15T17:00:32Z
- 分类：Geometry Foundation Models (主要); Embodied / Robotics / AR Applications (次要)
- 链接：摘要: https://arxiv.org/abs/2606.16960, PDF: https://arxiv.org/pdf/2606.16960

### 一句话总结
SurroundNEXO通过利用自车视角几何信息（Ego-Ray位置编码）和稀疏LiDAR度量锚点，解决了自动驾驶中多相机低重叠场景下的深度预测与空间一致性问题，相比现有方法在多项指标上取得了显著提升。

### 研究问题
如何在不依赖密集视觉对应的情况下，实现自动驾驶多相机（低重叠环视系统）的可靠度量级深度预测，以提升三维空间一致性？

### 核心思路/方法
1.  **Ego-Ray位置编码**：将图像令牌赋予全局可比较的自车视角方向，奠定跨视图几何推理基础，而非进行早期全局特征融合。
2.  **稀疏度量锚点**：使用稀疏LiDAR测量值作为度量锚点，向深度预测中传播绝对尺度信息。
3.  **渐进式特征交互**：特征交互按照从视图内部建模、到分解的时空推理、再到全局集成的顺序逐步扩展。

### 主要贡献
- 提出了SurroundNEXO，一种面向低重叠多相机系统的度量深度框架，以自车几何替代密集视觉对应。
- 在NuScenes、Waymo、DDAD三个自动驾驶基准上，单视图误差降低33.2%，跨视图一致性提升10.5%，度量重建质量提升25.6%。
- 在极稀疏深度提示下保持鲁棒性，并对未见过的相机布局展现出强大的零样本泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作明确提出并解决了自动驾驶感知域中环视相机低重叠带来的实际难题，并基于摘要报告了在NuScenes、Waymo、DDAD等主流数据集上全面且显著的性能提升，同时方法设计新颖（引入Ego-Ray位置编码和渐进式交互）。对于从事自动驾驶环境感知、多视图几何或度量深度估计的研究者而言，具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Modern autonomous driving depends on accurate metric 3D understanding for perception, reconstruction, and planning, which in turn requires reliable multi-camera depth prediction. However, the outward-facing nature of vehicle-mounted surround-view camera rigs inherently limits visual overlap across views, challenging the correspondence-based assumptions that underpin conventional multi-view geometry. To bridge this gap, we present SurroundNEXO, named after the Spanish word nexo for a geometric link, a low-overlap multi-camera metric depth framework that grounds cross-view reasoning in ego-centric geometry rather than dense visual correspondences. Instead of directly enforcing early global fusion, SurroundNEXO first assigns image tokens globally comparable ego-frame viewing directions through Ego-Ray Positional Encoding, then uses sparse LiDAR measurements as metric anchors to propagate absolute scale cues, and finally expands feature interaction progressively from view-local modeling to decomposed spatio-temporal reasoning and global integration. This design enables metric-scale depth prediction with improved spatial consistency across weakly overlapping cameras. Across low-overlap autonomous driving benchmarks, including NuScenes, Waymo and DDAD, SurroundNEXO reduces single-view error by 33.2%, improves cross-view consistency by 10.5%, and enhances metric reconstruction quality by 25.6% compared with SOTA methods. It further remains robust under extremely sparse depth prompts and exhibits strong zero-shot generalization to unseen camera layouts.

</details>

#### 2026-06-15 - Uncertainty Quality of VGGT: An Analysis on the DTU Benchmark Dataset

**Authors:** Markus Hillemann, Robert Langendörfer, Steven Landgraf, Markus Ulrich
**Links:** [abs](https://arxiv.org/abs/2606.16479) - [pdf](https://arxiv.org/pdf/2606.16479)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** visual geometry grounded transformer, VGGT, DUSt3R, MASt3R, 3D reconstruction, bundle adjustment, photogrammetry, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Uncertainty Quality of VGGT: An Analysis on the DTU Benchmark Dataset
- 作者：Markus Hillemann, Robert Langendörfer, Steven Landgraf, Markus Ulrich
- 出版日期：2026-06-15T09:49:00Z
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（副分类）
- 链接：https://arxiv.org/abs/2606.16479

### 一句话总结
本文分析了VGGT模型在DTU基准数据集上输出的不确定性质量，发现存在一个有效的置信度阈值可用于过滤原始输出，并指出提升不确定性质量对改善VGGT三维重建精度有显著潜力。

### 研究问题
如何评估VGGT模型所预测的不确定性质量？具体包括：是否存在可用的置信度阈值来过滤VGGT的原始输出？不确定性质量的提升能否提高三维重建的准确性？

### 核心思路/方法
基于DTU基准数据集，对VGGT模型输出的不确定性进行定量分析，通过设定置信度阈值对原始输出进行过滤，并评估该过滤操作对三维重建精度的影响。

### 主要贡献
1. 识别出VGGT在DTU数据集上预测不确定性时存在一个有效的置信度阈值，可用于过滤其原始输出。
2. 通过实验证明，提升不确定性质量（例如通过该阈值过滤）有望显著提高VGGT的三维重建精度。

### 局限性
摘要未提供足够信息。具体局限性（如分析仅针对DTU数据集、未讨论其他场景或基线对比等）超出摘要范围。

### 阅读优先级
**高**。理由：VGGT因获得CVPR-2025最佳论文奖而广受关注，本文聚焦于其不确定性质量这一关键但常被忽视的方面，对可靠使用该模型进行三维重建具有重要意义。分析结果可直接指导实际应用中的输出后处理，且发表于2026年（当前时间点之后），属于前沿研究。

</details>

<details>
<summary>Abstract</summary>

Visual Geometry Grounded Transformer (VGGT) has already attracted a great deal of attention in a short period of time, not least due to the Best Paper Award at CVPR-2025. Similar to DUSt3R and MASt3R, VGGT aims to bring about a paradigm shift by replacing established methods like bundle adjustment and feature matching with a simple, unified, feed-forward neural network that predicts camera poses, depth maps, and dense 3D structure directly from multiple images of a scene in a few seconds. A key aspect is its ability to process an arbitrary number of views consistently in a single forward pass without any post-processing or iterative optimization. For photogrammetry, this opens new possibilities for real-time, scalable, and accessible 3D reconstruction. In this context, not only high reconstruction accuracy but also high-quality uncertainty estimates are crucial, as they foster trust and enable robust quality assurance. This paper therefore investigates the quality of VGGT's uncertainty predictions. The analysis identifies an effective confidence threshold for filtering VGGT's raw output and demonstrates that enhancing uncertainty quality holds strong potential for improving the accuracy of its 3D reconstructions.

</details>

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-17 - Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos

**Authors:** Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon
**Links:** [abs](https://arxiv.org/abs/2606.19156) - [pdf](https://arxiv.org/pdf/2606.19156)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic 4D, Gaussian Splatting, 3D Gaussian Splatting, splatting, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos
- 作者：Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon
- 出版日期：2026-06-17
- 分类：Dynamic / 4D Reconstruction, Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.19156, PDF: https://arxiv.org/pdf/2606.19156

### 一句话总结
本文提出Hand-4DGS，首个从第一人称视频中实现前馈式动态4D手部重建的框架，通过网格引导表示和时间卷积，在无需3D标注的情况下达到约60 FPS的推理速度与强泛化能力。

### 研究问题
从第一人称视频中重建动态4D手部，现有方法面临头部快速运动、手部剧烈动态、严重遮挡以及单视角观测固有的歧义性等挑战。

### 核心思路/方法
1. 采用前馈式（feed-forward）3D高斯泼溅（Gaussian Splatting）框架，直接从输入视频重建动态4D手部。
2. 引入网格引导（mesh-guided）表示来提供结构先验，增强几何准确性。
3. 使用时间卷积（temporal convolutions）建模手部的动态运动，处理时序变化。
4. 利用高斯泼溅的可微渲染实现2D图像监督，从而避免依赖昂贵的3D手部姿态真值标注。

### 主要贡献
1. 首个前馈式动态4D手部重建框架，支持从第一人称视频中快速（~60 FPS）且泛化性强的推理。
2. 提出网格引导表示与时间卷积相结合的方法，有效应对遮挡和动态歧义。
3. 在H2O和ARCTIC两个挑战性数据集上取得优于基线的显著改进。

### 局限性
摘要未提供足够信息来明确指出方法的具体局限性。

### 阅读优先级
高  
理由：该方法解决了第一人称视频中动态手部重建这一关键难题，同时实现了实时推理速度和良好泛化性，且无需3D标注，对AR/VR和AI眼镜等应用具有重要参考价值。论文发表在知名团队工作（含Marc Pollefeys）上，方法新颖且实效性经过数据集验证。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D hand reconstruction from egocentric videos is essential for next-generation computing platforms such as AR/VR and AI glasses. Despite its importance, most prior works focus either on multi-view 3D hand reconstruction or on 4D human body reconstruction. Egocentric 4D hand reconstruction remains challenging due to fast head motion, rapid hand dynamics, severe occlusions, and inherent ambiguity from single-view observations. To address these challenges, we introduce Hand-4DGS, the first feed-forward framework for reconstructing dynamic 4D hands directly from egocentric videos, enabling both fast (~60 FPS) inference and strong generalization. Our approach incorporates a mesh-guided representation for structural priors and temporal convolutions to model dynamic motion. We evaluate our framework on two challenging egocentric datasets, H2O and ARCTIC, and demonstrate significant improvements over baselines. Our method benefits from the generalization capability of feed-forward networks and effective 2D image supervision through Gaussian splatting, without requiring expensive 3D hand pose ground-truth annotations.

</details>

#### 2026-06-17 - Intrinsic 4D Gaussian Segmentation from Scene Cues

**Authors:** Hasan Yazar, Mohamed Rayan Barhdadi, Erchin Serpedin, Mehmet Tuncel, Hasan Kurban
**Links:** [abs](https://arxiv.org/abs/2606.18623) - [pdf](https://arxiv.org/pdf/2606.18623)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic 4D, 4D Gaussian, Gaussian Splatting, rendering, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Intrinsic 4D Gaussian Segmentation from Scene Cues
- 作者：Hasan Yazar, Mohamed Rayan Barhdadi, Erchin Serpedin, Mehmet Tuncel, Hasan Kurban
- 出版日期：2026-06-17
- 分类：动态/4D重建；神经场景表示与渲染
- 链接：摘要页 https://arxiv.org/abs/2606.18623；PDF https://arxiv.org/pdf/2606.18623

### 一句话总结
本文提出Intrinsic-GS，一种无需训练和掩码监督的动态4D高斯分割方法，仅从高斯原语自身的外观、方向、尺度、变形轨迹和渲染边界线索构建稀疏亲和图，通过社区划分实现对象分割。

### 研究问题
如何在无需外部基础模型（如SAM）生成的2D掩码的情况下，仅从4D高斯表示本身恢复场景中的对象级结构，实现高效、鲁棒的动态场景分割。

### 核心思路/方法
1. 从4D高斯原语中提取五种内在线索：外观、方向、尺度、变形轨迹和非学习的渲染边界。
2. 基于这些线索构建稀疏亲和图，将高斯原语之间的相似性编码为图边权重。
3. 应用Leiden社区检测算法对图进行划分，得到对象分组。
4. 整个过程无需任何掩码监督或学习特征场，是训练无关、掩码无关的。

### 主要贡献
- 提出了Intrinsic-GS，首个不依赖外部掩码或特征场的学习的动态4D高斯分割方法。
- 在Neu3D基准上以仅几何线索的变体达到0.902 mIoU，与受SAM监督的TRASE方法持平；在HyperNeRF上达到0.575 mIoU。
- 在HyperNeRF上比基于掩码监督的管线快12.5倍，显著降低了计算开销。
- 证明了4D高斯表示本身已编码了大量分割信号，为高效、鲁棒的动态分割提供了新方向。

### 局限性
摘要未提供足够信息（如对复杂运动或遮挡场景的适应性、社区检测参数敏感性、分割细粒度上限等）。

### 阅读优先级
高。理由：本文提出了一种新颖的无监督/无掩码的动态3D分割方法，在保持较高准确性的同时大幅提升效率（12.5倍加速），对计算机视觉中动态场景理解、编辑、运动分析等领域具有重要参考价值，且方法简洁、可复现性强。

</details>

<details>
<summary>Abstract</summary>

Dynamic 4D Gaussian Splatting reconstructs deforming scenes with high fidelity and is increasingly adopted as a representation for dynamic 3D scenes. Putting such a scene to use, for editing, manipulation or motion analysis, first requires segmenting it: grouping the Gaussian primitives into coherent objects. Current pipelines obtain this grouping by importing 2D masks from foundation models such as SAM and lifting or distilling them into the Gaussian representation. In dynamic scenes these masks must be generated across many frames and views, which is costly, and the resulting segmentation can depend strongly on the quality and consistency of those external masks. We ask how much object-level structure can instead be recovered from the Gaussians themselves, and propose Intrinsic-GS, a training-free, mask-free method that builds a sparse affinity graph over Gaussian primitives from appearance, orientation, scale, deformation-trajectory and non-learned rendered-boundary cues. The graph is partitioned with Leiden community detection, requiring no foundation model and no learned feature field. On the standard 4D Gaussian segmentation benchmarks, Neu3D and HyperNeRF, Intrinsic-GS recovers substantial object structure without mask supervision, reaching 0.746 mIoU on Neu3D and 0.575 on HyperNeRF; on Neu3D, a geometry-only variant reaches 0.902 mIoU, matching SAM-supervised TRASE. On HyperNeRF, Intrinsic-GS runs 12.5x faster than the mask-generation and feature-rendering stages used by mask-supervised pipelines. These results suggest that much of the segmentation signal is already encoded in the Gaussians themselves, offering a fast, mask-free direction for 3D and 4D Gaussian segmentation that may also point toward more generalizable, robust segmentation in settings where external masks are unreliable or expensive.

</details>

#### 2026-06-16 - Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion

**Authors:** Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab, Federico Tombari, Stefano Gasperini
**Links:** [abs](https://arxiv.org/abs/2606.18250) - [pdf](https://arxiv.org/pdf/2606.18250)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** dynamic 3D, 3D reconstruction, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion
- 作者：Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab, Federico Tombari, Stefano Gasperini
- 出版日期：2026-06-16
- 分类：Dynamic / 4D Reconstruction, 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.18250

### 一句话总结
本文提出FR3D，一种将场景3D演化与智能体运动解耦的世界模型，用于从单目观测进行未来动态3D重建，可在2秒后保持几何一致性。

### 研究问题
如何从单目视频预测动态环境的未来演化，同时解决2D视频合成中因自运动与世界运动混淆导致的物体变形或消失等物理不一致性问题，并实现长期几何一致性。

### 核心思路/方法
1. **解耦建模**：显式地将场景的3D演化与智能体轨迹分离，将推断的自我运动作为潜在的动作代理，从而消除自运动与世界运动之间的歧义。
2. **教师-学生蒸馏**：利用现成基础模型的空间“常识”（如深度、尺寸等）进行蒸馏，以增强模型在未见场景上的零样本泛化能力。
3. **持久3D潜在表示**：维护一个持续更新的潜在3D表示，用于预测未来动态场景，而非仅依赖逐帧图像特征。

### 主要贡献
- 提出FR3D，首个实现未来动态3D重建（即使2秒后）并保持几何一致性的世界模型。
- 通过解耦自我运动和场景运动，解决了传统基于图像特征的预测方法中存在的物理不一致问题。
- 引入教师-学生蒸馏策略，利用基础模型的空间知识提升零样本泛化性能。
- 在多个数据集上的实验证明了该方法对未来动态3D重建的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该工作聚焦于动态3D重建与未来预测，方法新颖（解耦自运动与世界运动），对自主智能体相关研究有参考价值。但摘要未提供量化性能数据或与现有方法的具体对比，读者需进一步阅读论文正文以评估实际效果。若研究领域为3D/4D重建或具身智能，则优先级可提升至高。

</details>

<details>
<summary>Abstract</summary>

Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. Unlike prior works that treat the world as a sequence of image-based features, FR3D explicitly decouples the 3D evolution of the scene from the agent's trajectory, treating the inferred ego-motion as a latent proxy for action. This disentanglement resolves the ambiguities between self-motion and world-motion, ensuring geometric consistency into the future. Furthermore, we introduce a teacher-student distillation strategy that leverages the spatial "common sense" of off-the-shelf foundation models, leading to robust zero-shot generalization. Extensive experiments demonstrate FR3D's strong performance for future dynamic 3D reconstruction from monocular observations across multiple datasets, even 2 seconds into the future. Project page: https://fr3d-wm.github.io.

</details>

#### 2026-06-15 - Renderable Partial Representations for Dynamic Gaussian Splatting under Incomplete Delivery

**Authors:** Faruk Alpay, Levent Sarioglu, Yaser Hadri
**Links:** [abs](https://arxiv.org/abs/2606.17212) - [pdf](https://arxiv.org/pdf/2606.17212)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, NeRF, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Renderable Partial Representations for Dynamic Gaussian Splatting under Incomplete Delivery
- 作者：Faruk Alpay, Levent Sarioglu, Yaser Hadri
- 出版日期：2026-06-15
- 分类：动态/4D重建；神经场景表示与渲染
- 链接：摘要: https://arxiv.org/abs/2606.17212, PDF: https://arxiv.org/pdf/2606.17212

### 一句话总结
本文提出一种面向动态高斯泼溅（Dynamic Gaussian Splatting）的渲染可用的部分表示方法，通过优化图像空间中的退化度，使不完整传输状态下的场景仍可直接渲染，并以反事实效用层指导自适应调度。

### 研究问题
在动态高斯压缩中，交互式渲染常面临部分表示：部分时空区域存在、部分缺失，且后期精炼无法影响已显示帧。本文研究如何在网络传输不完整时，使高斯表示状态仍然直接可渲染，并优化其图像空间退化。

### 核心思路/方法
1. 将高斯图元组织成可独立寻址的时空聚类，包含一个基础层和三个精炼层。
2. 训练时采样部分依赖图，在一个GPU批次中渲染多个反事实状态。
3. 优化目标包括：期望失真、尾部失真、时间不一致性、码率和前缀回归。
4. 引入反事实效用层，测量每个完成组在不同接收方上下文中的边际渲染贡献。
5. 具体传输实现基于MTU限制的熵编码块、截止时间感知调度和接收方依赖闭包。

### 主要贡献
1. 提出一种动态高斯表示，其不完整交付状态仍可渲染，且退化在图像空间优化。
2. 建立反事实效用层，定量评估各完成组的渲染贡献，超越了标称精炼层顺序。
3. 实验证明：在多个动态场景（D-NeRF、HyperNeRF）中，精细精炼层的边际效用为负；基于效用的顺序可在匹配字节预算下消除PSNR回归（broom2）或提升PSNR达3.03 dB（chicken）。

### 局限性
摘要未提供足够信息关于方法的计算开销、实时性能、对极端缺失率的鲁棒性或与其他动态高斯压缩方法的系统比较。

### 阅读优先级：高
**理由**：该工作直接针对交互式渲染中动态高斯表示的传输与渲染退化问题，提出反事实效用这一新颖思路，实验验证了标称层顺序的不足并带来显著性能提升（如3.03 dB）。方法紧密结合网络交付的分布视角，为动态场景的实时渲染优化提供重要方向。

</details>

<details>
<summary>Abstract</summary>

Dynamic Gaussian compression is normally optimized for complete files or complete progressive prefixes, but interactive rendering encounters partial representations: some spatiotemporal regions are present, others missing, and late refinements cannot affect the displayed frame. We study dynamic Gaussian representations whose incomplete delivery states remain directly renderable and whose degradation is optimized in image space. Gaussian primitives are organized into independently addressable spatiotemporal clusters with a base level and three refinements; training samples partial dependency graphs, renders many counterfactual states in one GPU batch, and minimizes expected distortion, tail distortion, temporal inconsistency, rate, and prefix regressions. A counterfactual utility layer measures the marginal render contribution of each completion group across valid receiver contexts. The same graph admits a concrete delivery realization with MTU-bounded entropy-coded chunks, deadline-aware scheduling, and receiver-side dependency closure. On held-out views, the finest refinement has negative mean marginal utility in 3/32 D-NeRF bouncingballs, 49/64 HyperNeRF broom2, and 28/64 HyperNeRF chicken clusters; its lower-tail utility is negative in 21/32, 61/64, and 42/64 clusters, respectively. On broom2, render-utility ordering removes both PSNR regressions produced by nominal layer order at matched byte budgets; on chicken, utilities measured on disjoint training cameras improve held-out PSNR by 3.03 dB at the lowest matched budget. These scoped results show why nominal refinement order cannot substitute for render-conditioned utility: the formulation treats network delivery as a distribution over renderable scene states rather than as an external wrapper around a graphics codec.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

#### 2026-06-18 - CalTennis: Large Multi-View Tennis Video Dataset and Benchmark of Monocular-to-3D Pose Estimation

**Authors:** Ilona Demler, Xinran Xie, Blake Werner, Anna Szczuka, Pietro Perona
**Links:** [abs](https://arxiv.org/abs/2606.20542) - [pdf](https://arxiv.org/pdf/2606.20542)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CalTennis: Large Multi-View Tennis Video Dataset and Benchmark of Monocular-to-3D Pose Estimation
- 作者：Ilona Demler, Xinran Xie, Blake Werner, Anna Szczuka, Pietro Perona
- 出版日期：2026-06-18
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.20542

### 一句话总结
CalTennis是一个大规模、多视角网球视频数据集与基准，用于评估野外从单目到三维的人体姿态估计，提供了比现有数据集大数倍的数据量，并揭示了模型在深度和足部接触方面的持续缺陷。

### 研究问题
如何构建一个大规模、低成本、可标准化的多视角视频基准，以评估和揭示单目到三维姿态估计方法在真实运动场景中的表现与不足。

### 核心思路/方法
- 收集超过1100万帧（51小时）的网球训练与比赛视频，覆盖40名选手，使用2-6台同步相机以60 Hz拍摄。
- 提出简单标准化的数据采集协议，无需专用设备或专业知识，并实现全自动视频标定与同步。
- 利用多视角设置实现低成本、无标签的评估，对比当前最先进的单目到三维姿态方法。
- 引入两个新性能指标（footwork和stability），并从定性的身体形状不一致性角度分析失败模式。

### 主要贡献
1. 发布大规模多视角网球视频数据集CalTennis，比现有野外人体运动视频数据集大10倍，比有动作捕捉真值的数据集大3倍。
2. 提供首个大规模同步多视角记录专业运动员动作的基准。
3. 通过基准测试发现当前模型在深度估计和足部接触一致性方面普遍存在困难。
4. 提出新的评估指标（footwork和stability），揭示之前未被充分探索的失败模式。

### 局限性
摘要未提供足够信息，无法明确描述该研究的具体局限性。

### 阅读优先级
高。理由：该工作贡献了显著超越现有规模的数据集和基准，针对单目到三维姿态估计这一活跃领域，揭示了现有模型的通用弱点并提出新评估指标，对后续研究和算法改进有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

The Caltech Tennis Dataset (CalTennis) is a large-scale video benchmark for evaluating monocular-to-3D pose estimation in the wild. CalTennis comprises over 11 million frames (51 hours) of tennis practice and match play from 40 players, captured with 2-6 synchronized cameras at 60 Hz. It is 10 times larger than existing in-the-wild human motion video datasets and 3 times larger than existing MOCAP-ground-truthed datasets, and it is the first large-scale benchmark to provide synchronized multi-view recordings of expert athletic motion. The multi-view setup enables inexpensive, label-free evaluation of monocular-to-3D pose estimation algorithms. We describe a simple, standardized protocol that enables data collection without specialized equipment or expertise, along with fully automated video calibration and synchronization. Benchmarking state-of-the-art monocular-to-3D pose methods on CalTennis, we find that while 3D joint angle recovery is now quite accurate, all models struggle to estimate depth and foot contact consistently. We further propose two novel performance metrics, footwork and stability, as well as qualitatively study body shape inconsistency. These metrics expose previously underexplored failure modes and point to concrete opportunities for improvement in pose estimation and action analysis.

</details>

#### 2026-06-18 - Towards 3D karst underwater scene reconstruction from rotating sonar data

**Authors:** Georgios Evangelos Margaritis, Lionel Lapierre, Simon Rohou, Zhi Yan, Andreas Nüchter, François Goulette
**Links:** [abs](https://arxiv.org/abs/2606.20322) - [pdf](https://arxiv.org/pdf/2606.20322)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, scene reconstruction, SLAM, surface reconstruction, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards 3D karst underwater scene reconstruction from rotating sonar data  
- 作者：Georgios Evangelos Margaritis, Lionel Lapierre, Simon Rohou, Zhi Yan, Andreas Nüchter, François Goulette  
- 出版日期：2026-06-18  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：摘要 https://arxiv.org/abs/2606.20322 | PDF https://arxiv.org/pdf/2606.20322  

### 一句话总结
本文提出了一套从旋转声纳数据重建水下岩溶三维场景的流水线，结合连续时间SLAM校正轨迹漂移与两阶段深度学习方法生成可漫游的3D网格。

### 研究问题
如何从稀疏、有噪声的声纳数据以及存在漂移的导航估计中，重建复杂且结构未知的水下岩溶管道的三维几何。

### 核心思路/方法
1. **轨迹校正**：采用连续时间SLAM方法纠正声纳探测过程中的轨迹漂移。  
2. **表面重建**：提出一种新颖的两阶段深度学习方法，从校正后的稀疏点云生成沉浸式、可导航的3D网格。  

### 主要贡献
- 构建了一套完整的水下岩溶场景重建流水线，将SLAM与深度学习表面重建相结合。  
- 提出两阶段深度学习方法，专门用于从稀疏声纳数据生成可用的3D网格。  

### 局限性
摘要未提供足够信息（例如：未说明方法在极端噪声或大规模场景下的表现，未提及与现有方法的定量对比结果，未分析实时性要求或计算成本）。

### 阅读优先级
**中**  
理由：该方法针对特定应用场景（水下岩溶探测）具有实际价值，且结合了SLAM与深度学习，技术上具有一定创新性。但摘要未提供实验对比与量化指标，缺乏对方法性能的直接评估，故优先级适中。

</details>

<details>
<summary>Abstract</summary>

Karst aquifers provide critical freshwater resources but pose significant hazards due to their complex and poorly understood subsurface geometry. Mapping these environments is challenging because sonar data from underwater exploration is sparse and noisy, while navigation estimates suffer from drift limiting standard 3D reconstruction methods. We present a pipeline for reconstructing underwater karst conduits from a sonar profiler. We combine a continuous-time SLAM approach to correct trajectory drift with a novel two-stage deep learning method for surface reconstruction, producing an immersive and navigable 3D mesh for hydrogeological analysis.

</details>

#### 2026-06-18 - MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM

**Authors:** Fan Zhu, Ziyu Chen, Peichen Liu, Yifan Zhao, Zhisong Xu, Hui Zhu, Hongxing Zhou, Sixun Liu, Chunmao Jiang
**Links:** [abs](https://arxiv.org/abs/2606.19874) - [pdf](https://arxiv.org/pdf/2606.19874)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, simultaneous localization and mapping, SLAM, visual SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM
- 作者：Fan Zhu, Ziyu Chen, Peichen Liu, Yifan Zhao, Zhisong Xu, Hui Zhu, Hongxing Zhou, Sixun Liu, Chunmao Jiang
- 出版日期：2026-06-18
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.19874 ; PDF: https://arxiv.org/pdf/2606.19874

### 一句话总结
MMD-SLAM 是一种基于 3D 高斯泼溅的结构增强视觉 SLAM 框架，通过引入亚特兰大世界假设与多元高斯表征，在跟踪精度和建图质量上超越了现有方法（如 MonoGS）。

### 研究问题
现有 3DGS 驱动的视觉 SLAM 系统未能充分利用场景底层结构信息，导致渲染质量受限且建图结果不一致。

### 核心思路/方法
1. 采用亚特兰大世界假设，提取场景中的主导方向作为结构先验。
2. 设计多元高斯表征，显式编码结构先验。
3. 引入点-线融合策略进行位姿优化，利用 3D 线段提升跟踪鲁棒性并提供映射约束。
4. 提出高斯演化策略，使高斯体适应场景几何，并将结构线索融入全局优化。

### 主要贡献
- 提出点-线融合策略，增强位姿优化与映射约束。
- 设计基于亚特兰大世界假设的多元高斯表征，显式编码结构先验。
- 提出高斯演化策略，动态适应场景几何并参与全局优化。
- 在 ScanNet 上 ATE RMSE 降低 48.56%，在 Replica 上 PSNR 提升 5.71%，达到 SOTA 性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：论文在视觉 SLAM 与神经渲染交叉方向有明确创新点（结构增强与多高斯表征），且在公开数据集上取得显著性能提升。适合对该方向感兴趣的读者跟进，但对纯 SLAM 或纯渲染从业者而言，需进一步阅读原文评估方法的普适性。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has significantly boosted novel view synthesis and high-fidelity scene reconstruction, expanding the potential of 3DGS-based Visual Simultaneous Localization and Mapping (SLAM) methods. However, most existing systems fail to fully exploit the underlying structural information, which limits rendering quality and often leads to inconsistent maps. To address these limitations, we propose MMD-SLAM, a structure-enhanced Visual SLAM framework that leverages the Atlanta World (AW) assumption to guide a Multi-Meta Gaussian representation for photorealistic mapping. First, we introduce a point-line fusion strategy for pose optimization, where 3D line segments are incorporated to improve tracking robustness and provide additional constraints for mapping. Second, we design a Multi-Meta Gaussian representation with dominant directions, explicitly encoding structural priors from the AW hypothesis. Finally, we propose a Gaussian evolution strategy that adapts to scene geometry and incorporates structural cues into global optimization. Extensive experiments demonstrate that these innovations enable MMD-SLAM to achieve state-of-the-art performance in both tracking accuracy and mapping quality. e.g., our method achieves a 48.56% reduction in ATE RMSE on ScanNet and a 5.71% improvement in PSNR on Replica, compared with MonoGS.

</details>

#### 2026-06-18 - TIDY: Thermal Infrared Image Denoising via Wavelet Domain Entropy and Directional Stripe Index

**Authors:** Tai Hyoung Rhee, Dong-Guw Lee, Ayoung Kim
**Links:** [abs](https://arxiv.org/abs/2606.19813) - [pdf](https://arxiv.org/pdf/2606.19813)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TIDY: Thermal Infrared Image Denoising via Wavelet Domain Entropy and Directional Stripe Index
- 作者：Tai Hyoung Rhee, Dong-Guw Lee, Ayoung Kim
- 出版日期：2026-06-18T05:42:50Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2606.19813 ，PDF: https://arxiv.org/pdf/2606.19813

### 一句话总结
TIDY是一种轻量级的小波域热红外图像去噪方法，通过在真实数据上训练并引入小波熵和方向条纹指数作为损失项，在保持高推理速度（约34Hz）的同时实现了鲁棒的去噪效果，并提升了下游机器人任务（如热惯性里程计和单目深度估计）的性能。

### 研究问题
现有的热红外图像去噪方法存在精度与效率的权衡问题：要么因速度慢而无法满足机器人任务的在线部署需求，要么对严重噪声（尤其室内低热对比度下）鲁棒性不足，且通常依赖合成噪声进行训练。

### 核心思路/方法
1. 设计轻量级小波域去噪网络，在小波域中显式地将噪声与结构内容分离，从而降低空间复杂度并提升推理速度。
2. 提出两个新的度量指标**小波熵**（Wavelet Entropy）和**小波方向条纹指数**（Wavelet Directional Stripe Index）作为互补的损失项，分别用于抑制随机噪声和条纹伪影。
3. 使用真实的热红外清洁-配对数据（而非合成噪声）进行训练，并在室内严重退化场景与零样本设置下评估鲁棒性。

### 主要贡献
1. 提出轻量级小波域去噪器TIDY，在真实TIR数据上训练，推理速度达约34Hz，适合在线部署。
2. 引入小波熵和方向条纹指数作为损失项，实现针对随机噪声和条纹噪声的显式抑制。
3. 在室内严重退化及零样本场景下，验证了TIDY在下游机器人任务（热惯性里程计、单目深度估计）中的一致性提升。
4. 开源了代码和数据集。

### 局限性
摘要未提供足够信息，例如在极端噪声水平、不同传感器类型或更长序列上的表现；也未提及对计算资源的具体需求或潜在的泛化限制。

### 阅读优先级
中。理由：该方法针对热红外图像去噪在机器人应用中的效率与鲁棒性瓶颈，提出了轻量级且创新的小波域解决方案，但摘要未提供与现有方法的详细数值对比，且作为2026年发表的工作，当前时效性一般。若读者关注机器人感知或热红外成像，可阅读；若对去噪通用方法更感兴趣，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Thermal infrared (TIR) imaging has been a popular choice for field robotics due to its robust perception capability under low light visual degradation, but it suffers from severe stochastic and fixed-pattern noise that breaks downstream estimation. This noise is intensified indoors due to low thermal contrast and uniform temperature distributions, contributing to the relative lack of indoor TIR deployments. Existing TIR denoising methods exhibit a poor accuracy-efficiency tradeoff, either too slow for online deployment required in robotics or insufficiently robust to severe degradation, while typically being trained on synthetic noise. Addressing these problems, we propose TIDY, a lightweight wavelet-domain denoiser trained on real clean-noisy TIR data. By reformulating TIR denoising in the wavelet domain, TIDY explicitly disentangles noise from structural content, enabling targeted suppression with reduced spatial complexity, significantly improving inference speed over prior methods (~34Hz). TIDY introduces two new metrics, Wavelet Entropy and Wavelet Directional Stripe Index, as complementary loss terms to explicitly suppress stochastic noise and stripe artifacts. Across severe indoor corruption and zero-shot settings, TIDY improves robustness and yields consistent gains in downstream robotics tasks including thermal inertial odometry and monocular depth estimation. Code and dataset is available at: https://github.com/williamrheeth/TIDY

</details>

#### 2026-06-17 - Hardware- and Vision-in-the-Loop Validation of Deep Monocular Pose Estimation for Autonomous Maritime UAV Flight

**Authors:** Maneesha Wickramasuriya, Beomyeol Yu, Jaden Shin, Mason Huslig, Taeyoung Lee, Murray Snyder
**Links:** [abs](https://arxiv.org/abs/2606.19176) - [pdf](https://arxiv.org/pdf/2606.19176)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hardware- and Vision-in-the-Loop Validation of Deep Monocular Pose Estimation for Autonomous Maritime UAV Flight
- 作者：Maneesha Wickramasuriya, Beomyeol Yu, Jaden Shin, Mason Huslig, Taeyoung Lee, Murray Snyder
- 出版日期：2026-06-17T15:18:11Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.19176

### 一句话总结
本文提出一个硬件与视觉在环的验证框架，将逼真海事渲染视图输入深度单目位姿估计器，并结合延迟卡尔曼滤波与IMU数据融合，实现了面向自主海航UAV飞行的闭环室内测试。

### 研究问题
在船舶甲板上执行自主无人机起降时，如何规避高成本、受天气影响且风险大的实海验证，通过硬件在环手段可靠地测试基于视觉的相对位姿估计及闭环控制性能。

### 核心思路/方法
1. **硬件与视觉在环框架**：搭建全自主室内飞行环境，同时生成逼真（photorealistic）海事背景的渲染视图。
2. **深度单目位姿估计**：在无人机上运行基于Transformer架构的单目位姿估计器，处理渲染视图。
3. **延迟融合与控制**：利用延迟卡尔曼滤波器将滞后的视觉测量与高频IMU数据融合，为几何控制提供一致的状态估计。
4. **实验验证**：开展自主起飞、轨迹跟踪与着陆实验，展示稳定闭环飞行。

### 主要贡献
- 提出了一个兼顾硬件与视觉在环的验证框架，能捕捉纯仿真中缺失的感知延迟、异步更新和计算约束等嵌入式效应。
- 为发展海事UAV自主性提供了安全且硬件真实的中间测试阶段，降低了实际舰载部署前的验证风险。

### 局限性
摘要未提供关于方法在非海事场景或更复杂气象条件下的泛化能力、估计器精度量化、以及具体计算资源开销等信息。

### 阅读优先级
**中**。  
理由：该方法面向特定场景（海事UAV）的软硬件联合验证，创新在于验证框架而非核心算法本身。若研究领域涉及无人机自主着陆、硬件在环仿真或视觉-惯性融合，则有参考价值；否则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Autonomous UAV operations on ships require reliable vision-based relative pose estimation, yet at-sea validation is costly, weather-dependent, and risky. This paper presents a hardware-validated vision-in-the-loop framework that enables fully autonomous indoor flight while emulating photorealistic maritime environments. Rendered maritime views are processed onboard by a deep transformer-based monocular pose estimator. Delayed vision measurements are fused with high-rate IMU data using a delayed Kalman filter to provide consistent state estimates for geometric control. The system captures critical embedded effects, including perception latency, asynchronous updates, and computational constraints, that are absent in pure simulation. Autonomous takeoff, trajectory tracking, and landing experiments demonstrate stable closed-loop flight. The results establish a safe and hardware-realistic intermediate stage for developing maritime UAV autonomy prior to shipboard deployment.

</details>

#### 2026-06-17 - Sensor Configuration Matters: A Systematic Evaluation of Multimodal SLAM on Quadruped Robots

**Authors:** Roberto Corlito, Fabian Schmidt, Nils Seibert, Markus Enzweiler, Abhinav Valada, Arne Roennau
**Links:** [abs](https://arxiv.org/abs/2606.19067) - [pdf](https://arxiv.org/pdf/2606.19067)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sensor Configuration Matters: A Systematic Evaluation of Multimodal SLAM on Quadruped Robots
- 作者：Roberto Corlito, Fabian Schmidt, Nils Seibert, Markus Enzweiler, Abhinav Valada, Arne Roennau
- 出版日期：2026-06-17
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.19067

### 一句话总结
本文系统评估了不同硬件传感器配置（摄像头类型、快门技术、惯性传感器等级）对四足机器人多模态SLAM性能的影响，发现立体配置优于单目和RGB-D，全局快门优于卷帘快门，且标准惯性集成在激烈足式运动下反而可能降低视觉SLAM性能。

### 研究问题
四足机器人在激烈运动（如足部冲击震动、高频机械振动、快速角旋转）带来的独特传感器挑战下，硬件级别的传感器配置如何影响视觉、视觉-惯性及LiDAR-视觉-惯性SLAM方法的定位精度、算法鲁棒性和计算资源利用？

### 核心思路/方法
利用ANYmal D四足机器人上录制的GrandTour数据集，对不同状态最先进的视觉、视觉-惯性和LiDAR-视觉-惯性SLAM方法进行系统评估。通过隔离和量化摄像头模态（单目、立体、RGB-D）、快门技术（全局快门、卷帘快门）以及惯性传感器等级的影响，分析它们在定位精度、算法鲁棒性和计算资源利用方面的权衡。

### 主要贡献
1. 首次针对四足机器人激进运动动力学引发的传感器挑战，系统评估硬件传感器配置对多模态SLAM性能的影响。
2. 实验揭示：立体配置显著优于单目和RGB-D；全局快门相机显著减少运动引发的跟踪失败；标准的惯性集成在激烈足式运动下可能降低基于视觉系统的性能。
3. 为在敏捷四足系统上设计定制传感器负载以实现可靠感知，提供了具体的设计指南。

### 局限性
摘要未提供足够信息。摘要未提及实验范围之外的局限，例如是否在多种地形上验证、是否考虑不同四足机器人型号、是否存在计算资源或传感器成本方面的约束等。

### 阅读优先级
高。理由：该研究针对四足机器人领域的SLAM关键实际问题——传感器硬件配置对性能的影响进行系统评估，结果具有直接工程应用价值，可为实际机器人系统设计提供具体指导。

</details>

<details>
<summary>Abstract</summary>

Autonomous navigation of quadrupedal robots in diverse environments fundamentally relies on resilient Simultaneous Localization and Mapping (SLAM). While visual-inertial SLAM has matured across wheeled, handheld, and aerial platforms, a critical evaluation gap remains regarding how hardware-level sensor configurations affect performance under the aggressive dynamics of legged locomotion. Quadrupeds introduce distinct embodiment-induced sensory challenges, including foot-impact shocks, high-frequency mechanical vibrations, and rapid angular rotations, which degrade standard perception pipelines. To address this gap, we present a systematic evaluation of state-of-the-art visual, visual-inertial, and LiDAR-visual-inertial SLAM methods using the GrandTour dataset recorded on an ANYmal D quadruped. We isolate and quantify the impacts of camera modalities, shutter techniques, and inertial sensor tiers, analyzing their trade-offs across localization accuracy, algorithmic robustness, and computational resource utilization. Our empirical findings demonstrate that hardware selection has substantial influence on system resilience: stereo configurations consistently outperform monocular and RGB-D modalities, global shutter cameras significantly mitigate motion-induced tracking failures compared to rolling shutter cameras, and, crucially, standard inertial integration can degrade the performance of primarily vision-based frameworks under harsh legged locomotion. These insights additionally offer concrete design guidelines for tailoring custom sensor payloads to achieve dependable perception on agile legged systems.

</details>

#### 2026-06-17 - TactSpace: Learning a Physics-enriched Shared Latent Space for Tactile Sim-to-Real Transfer

**Authors:** Arunim Joarder, Arjun Bhardwaj, René Zurbrügg, Mayank Mittal, Florin Püntener, Sira Bielefeldt, Cosmin Roman, Vaishakh Patil, Marco Hutter
**Links:** [abs](https://arxiv.org/abs/2606.18959) - [pdf](https://arxiv.org/pdf/2606.18959)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** shape reconstruction, geometric reconstruction, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TactSpace: Learning a Physics-enriched Shared Latent Space for Tactile Sim-to-Real Transfer
- 作者：Arunim Joarder, Arjun Bhardwaj, René Zurbrügg, Mayank Mittal, Florin Püntener, Sira Bielefeldt, Cosmin Roman, Vaishakh Patil, Marco Hutter
- 出版日期：2026-06-17
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.18959

### 一句话总结
本文提出一个多模态表示学习框架，通过对齐模拟与真实触觉信号（如模拟穿透深度和真实电容）到一个共享潜在空间，实现零样本触觉模拟到真实迁移，并显著降低力预测和形状重建误差。

### 研究问题
当前模拟器无法精确建模触觉传感器的复杂形变和传导机制，阻碍了机器人学习中的触觉模拟到真实迁移。

### 核心思路/方法
构建一个多模态表示学习框架，使用模态特定编码器将异质触觉观测（如模拟穿透深度、真实电容）投影到一个共享潜在空间。训练时结合自重建、交叉重建目标和对比对齐，鼓励生成模态不变且信息丰富的表示。

### 主要贡献
1. 提出一种无需精确原始信号模拟的触觉模拟到真实迁移方法，仅需对齐共享潜在空间。
2. 在压头形状识别、力预测和几何重建任务上实现了零样本模拟到真实迁移。
3. 相比基线，力预测误差降低16.7%，形状重建误差降低45.8%。
4. 发布一个基于Warp的、适用于Isaac Lab的惩罚性触觉模拟模型，支持可扩展触觉数据生成。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文提出了一种解决触觉模拟到真实迁移瓶颈的新框架，具有明确的跨模态对齐策略和显著的性能提升（如力预测和形状重建误差降低），且附带开源模拟工具，对机器人操控和触觉学习领域有实际应用价值。

</details>

<details>
<summary>Abstract</summary>

Tactile sensing provides direct measurements of contact interactions that are essential for robotic manipulation. However, current simulators lack the fidelity to faithfully model the complex deformation and transduction mechanics of tactile sensors, severely hindering sim-to-real transfer in robot learning pipelines. To address this challenge, we propose a multi-modal representation learning framework that aligns heterogeneous tactile modalities within a shared latent space, eliminating the need for accurate raw-signal simulation while preserving relevant contact information. Our approach employs modality-specific encoders to project diverse tactile observations, such as simulated penetration depth and real-world capacitance, into a common embedding space. The model is trained using self- and cross-reconstruction objectives alongside contrastive alignment, encouraging modality-invariant yet information-rich representations. We evaluate the learned embeddings on indenter shape identification, force prediction, and geometric reconstruction tasks, training exclusively in simulation and testing directly on real sensor measurements. Our results demonstrate zero-shot sim-to-real transfer across physically dissimilar representations. Furthermore, incorporating multi-physics simulation modalities yields more informative embeddings that transfer across diverse downstream tasks, demonstrating a 16.7% reduction in force prediction error and a 45.8% reduction in shape reconstruction error. Finally, we release an efficient Warp-based implementation of a penalty-based tactile simulation model for Isaac Lab, enabling scalable tactile data generation.

</details>

#### 2026-06-17 - Learned Radius Estimation for UDF-Based Point Cloud Reconstruction

**Authors:** Eito Ogawa, Hiroshi Watanabe
**Links:** [abs](https://arxiv.org/abs/2606.18787) - [pdf](https://arxiv.org/pdf/2606.18787)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** point cloud reconstruction, surface reconstruction, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learned Radius Estimation for UDF-Based Point Cloud Reconstruction
- 作者：Eito Ogawa, Hiroshi Watanabe
- 出版日期：2026-06-17
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.18787

### 一句话总结
提出一个基于学习的逐查询点支持半径选择器，用于提升局部补片无符号距离场（UDF）方法在点云重建中的精度。

### 研究问题
局部补片UDF方法依赖“支持半径”来定义每个点的局部邻域范围，传统上该半径为固定值或通过一维曲率启发式选取，无法适应局部几何变化，导致重建精度受限。

### 核心思路/方法
提出一个可学习的逐查询点半径选择器，该选择器预测连续的支持半径，并作为插件接入冻结的LoSF-UDF骨干网络。训练时，通过抛物线插值缓存UDF误差曲线，获取离网格的目标半径作为监督信号。

### 主要贡献
- 首次针对UDF点云重建提出可学习的支持半径估计方法。
- 设计了一个可插拔的半径选择器，无需重新训练骨干网络。
- 提出基于抛物线插值的离网格监督方式，从缓存UDF误差曲线获得目标半径。
- 实验证明该方法在提高精细尺度重建精度方面的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该工作聚焦于UDF重建中的具体参数（支持半径）优化，属于技术改进型研究，对从事点云重建或隐式表面学习的读者有一定参考价值；但摘要未给出定量实验对比或消融结果，需进一步阅读全文评估实际增益。

</details>

<details>
<summary>Abstract</summary>

Surface reconstruction from point clouds is important for consumer-grade 3D capture, including AR/VR and indoor scanning. Local-patch Unsigned Distance Field (UDF) methods are lightweight and generalizable, but their accuracy depends on the support radius, traditionally fixed or selected by a one-dimensional curvature heuristic that cannot capture heterogeneous local geometry. We propose a learned per-query radius selector that predicts a continuous support radius and plugs into a frozen LoSF-UDF backbone. The selector is trained using off-grid target radii obtained by parabolic interpolation of cached UDF error curves. Experiments show improved fine-scale reconstruction accuracy.

</details>

#### 2026-06-17 - Splaxel: Efficient Distributed Training of 3D Gaussian Splatting for Large-scale Scene Reconstruction via Pixel-level Communication

**Authors:** Wenqi Jia, Zhewen Hu, Ying Huang, Yu Gong, Stavros Kalafatis, Yuke Wang, Wei Niu, Chengming Zhang, Ang Li, Sheng Di, Yuede Ji, Bo Fang, Miao Yin
**Links:** [abs](https://arxiv.org/abs/2606.18588) - [pdf](https://arxiv.org/pdf/2606.18588)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Splaxel: Efficient Distributed Training of 3D Gaussian Splatting for Large-scale Scene Reconstruction via Pixel-level Communication
- 作者：Wenqi Jia, Zhewen Hu, Ying Huang, Yu Gong, Stavros Kalafatis, Yuke Wang, Wei Niu, Chengming Zhang, Ang Li, Sheng Di, Yuede Ji, Bo Fang, Miao Yin
- 出版日期：2026-06-17
- 分类：3D Reconstruction & Multi-view Geometry（主分类）; Neural Scene Representations & Rendering（次分类）
- 链接：摘要页 https://arxiv.org/abs/2606.18588 ；PDF https://arxiv.org/pdf/2606.18588

### 一句话总结
Splaxel 提出基于像素级通信的分布式3D高斯泼溅（3DGS）训练框架，通过局部渲染与全局合成避免高斯同步，在百万级高斯规模场景下实现最高7.6倍加速，同时保持高重建质量。

### 研究问题
现有分布式3DGS训练方法存在两大难题：要么将场景分割为孤立区域导致全局不一致，要么依赖全局高斯级交换导致通信量随场景规模急剧增长，迭代时间被通信主导。如何实现通信高效且数学一致的分布式大规模场景3DGS训练？

### 核心思路/方法
- **像素级局部渲染与全局合成**：每个GPU渲染自己负责的局部高斯子集，仅交换部分像素值，而非同步高斯参数。
- **通信成本稳定**：该机制使得通信开销不随场景中高斯数量增加而增长。
- **冗余减少策略**：通过几何与透射可见性预测（geometric and transmittance visibility prediction）降低像素级冗余。
- **冲突避免的相机视角合并**：采用conflict-free camera-view consolidation提升GPU利用率。

### 主要贡献
1. 首次提出基于像素级通信的分布式3DGS训练框架Splaxel，避免高斯级同步带来的通信瓶颈。
2. 在数学一致性的前提下，保持通信成本与场景规模无关，实现了可扩展的分布式训练。
3. 融合可见性预测与视角合并的优化，进一步减少像素冗余并提升GPU利用效率。
4. 在包含多达1.2亿个高斯的大规模数据集上，相比现有最优分布式3DGS框架获得最高7.6倍加速，且重建质量接近。

### 局限性
摘要未提供足够信息，未说明该方法在哪些场景或条件下效果不佳、内存消耗、收敛稳定性或对相机数量/视角分布的敏感性。

### 阅读优先级
**高**  
理由：该工作直接针对分布式3DGS训练的关键瓶颈——通信效率，提出新颖的像素级通信范式，实验显示显著加速，适用于大规模场景重建，对相关领域研究者和工程人员具有明确参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables high-fidelity and real-time 3D scene reconstruction, but scaling training to large-scale scenes requires optimizing hundreds of millions of Gaussians across multiple GPUs. Existing distributed approaches either partition scenes into isolated regions, causing global inconsistency, or rely on global Gaussian-level exchanges, which lead to substantial growth in inter-GPU communication and quickly dominate iteration time. We propose Splaxel, a communication-efficient distributed 3DGS training framework based on pixel-level local rendering and global composition. Instead of synchronizing Gaussians, each GPU renders its local subset and exchanges only partial pixel values, maintaining mathematical consistency while keeping communication cost stable as the scene size increases. Splaxel further reduces pixel-level redundancy through geometric and transmittance visibility prediction and improves GPU utilization via conflict-free camera-view consolidation. Evaluated on large-scale datasets with up to 120M Gaussians, Splaxel achieves up to 7.6$\times$ speedup over the state-of-the-art distributed 3DGS framework while preserving high reconstruction quality.

</details>

#### 2026-06-16 - SP-TransientBench: A Real-Captured Single Photon Perception Benchmark

**Authors:** Hongzhou Dong, Zili Zhang, Ziting Wen, Yiheng Qiang, Runrong Deng, Wenle Dong, Ziwen Jiang, Xinyang Li, Rui Lu, Shuoyao Sun, Wenyu Wang, Ziyi Xia, Haitao Zheng, Guodong Shi, Xiaoqiang Ren
**Links:** [abs](https://arxiv.org/abs/2606.18952) - [pdf](https://arxiv.org/pdf/2606.18952)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, depth estimation, geometric reconstruction, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SP-TransientBench: A Real-Captured Single Photon Perception Benchmark
- 作者：Hongzhou Dong, Zili Zhang, Ziting Wen, Yiheng Qiang, Runrong Deng, Wenle Dong, Ziwen Jiang, Xinyang Li, Rui Lu, Shuoyao Sun, Wenyu Wang, Ziyi Xia, Haitao Zheng, Guodong Shi, Xiaoqiang Ren
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.18952

### 一句话总结
本文提出了一个名为SP-TransientBench的真实拍摄单光子感知多任务基准测试集，包含10个场景、10297个视图，并提供了完整的飞行时间直方图、校准相机位姿和3D语义标注，旨在系统评估单光子LiDAR在深度估计、多视图重建和3D语义理解等难题上的性能。

### 研究问题
现有单光子感知研究多基于模拟数据或小规模受控采集，缺乏对真实世界单光子感知（包括深度估计、多视图重建和3D语义理解）的系统性评估基准。

### 核心思路/方法
构建一个真实采集的多任务基准测试集：
1. 使用固态单光子LiDAR（分辨率为256×192）采集10个多样化场景，共10297个视图。
2. 为每个视图提供包含多返回行为的完整飞行时间直方图、标准化元数据以及用于多视图评估的校准相机位姿。
3. 为选定场景提供13类3D语义标注。
4. 针对每个任务提供专用数据划分和评估协议，以实现可复现的基准测试。

### 主要贡献
1. 提出了第一个真实采集、面向多任务（深度估计、多视图重建、3D语义理解）的单光子感知基准测试集。
2. 提供了覆盖10个场景、10297个视图的完整飞行时间直方图和多返回行为数据。
3. 提供了校准相机位姿和13类3D语义标注，支持标准化和可复现的评估。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该基准测试直接填补了单光子感知领域缺乏真实世界系统性评估基准的空白，提供了大规模、多任务、标注完整的数据集，对从事单光子LiDAR、3D重建和语义理解的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-photon LiDAR (SPL) based on single-photon avalanche diode (SPAD) sensing enables time-resolved photon measurements with extreme sensitivity, offering unique potential for active 3D perception in photon-starved scenarios.However, real-world single photon perception remains fundamentally challenging due to unique measurement noise and complex multi-return transient phenomena, which jointly complicate geometric reconstruction and semantic scene understanding. Despite growing interest in SPAD-based sensing, existing studies are largely limited to simulated data or small-scale controlled captures. As a result, systematic evaluation of real-world single photon perception across depth estimation, multi-view reconstruction, and 3D semantic understanding remains underexplored. To bridge this gap, we introduce SP-TransientBench (STB), a real-captured multi-task benchmark for single photon perception. SP-TransientBenc comprises 10 diverse scenes and 10,297 views captured using a solid-state single-photon LiDAR at $256\times192$ resolution. Each view provides full time-of-flight histograms with multi-return behavior,standardized metadata, and calibrated camera poses for multi-view evaluation. We further provide 13-class 3D semantic annotations for selected scenes. By providing dedicated data splits and evaluation protocols for each task, STB enables consistent and reproducible benchmarking of real-world single photon perception across multiple 3D vision problems. The dataset and code will be released upon acceptance.

</details>

#### 2026-06-16 - Neural Tree Reconstruction for the Open Forest Observatory

**Authors:** Marissa Ramirez de Chanlatte, Arjun Rewari, Trevor Darrell, Derek J. N. Young
**Links:** [abs](https://arxiv.org/abs/2606.18153) - [pdf](https://arxiv.org/pdf/2606.18153)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, NeRF, radiance, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Neural Tree Reconstruction for the Open Forest Observatory  
- 作者：Marissa Ramirez de Chanlatte, Arjun Rewari, Trevor Darrell, Derek J. N. Young  
- 出版日期：2026-06-16  
- 分类：3D 重建与多视角几何  
- 链接：摘要：https://arxiv.org/abs/2606.18153；PDF：https://arxiv.org/pdf/2606.18153  

### 一句话总结
本文探索将神经辐射场（NeRF）引入开放森林观测站（OFO）数据集，以提升森林三维地图的重建质量，并指出其对气候应用的重要性。

### 研究问题
如何克服现有基于运动恢复结构（SfM）方法在森林三维重建中产生的伪影、细节缺失及林下可见性受限等问题，从而提升 OFO 数据集的质量。

### 核心思路/方法
利用神经辐射场（NeRF）等先进三维重建技术替代经典 SfM 方法，因其能够产生更高质量、更鲁棒的重建结果，并对稀疏视图和先验知识有更好的支持。

### 主要贡献
- 提出了将 NeRF 整合到 OFO 数据集中的探索性思路。
- 概述了未来支持更先进三维视觉模型的工作方向。
- 强调了高质量三维重建对于林业应用（如再造林优先、野火隐患减少、碳汇监测）的重要性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
低。理由：本文目前仅停留在“探索思路”和“未来工作展望”阶段，未给出具体实验或定量结果，缺乏实质性技术贡献。对于关注成熟方法的读者而言，参考价值有限。

</details>

<details>
<summary>Abstract</summary>

The Open Forest Observatory (OFO) is a collaboration across universities and other partners to make low-cost forest mapping accessible to ecologists, land managers, and the general public. The OFO is building both a database of geospatial forest data as well as open-source methods and tools for forest mapping by uncrewed aerial vehicle. Such data are useful for a variety of climate applications including prioritizing reforestation efforts, informing wildfire hazard reduction, and monitoring carbon sequestration. In the current iteration of the OFO's forest map database, 3D tree maps are created using classical structure-from-motion techniques. This approach is prone to artifacts, lacks detail, and has particular difficulty on the forest floor where the input data (overhead imagery) has limited visibility. These reconstruction errors can potentially propagate to the downstream scientific tasks (e.g. a wildfire simulation.) Advances in 3D reconstruction, including methods like Neural Radiance Fields (NeRF), produce higher quality results that are more robust to sparse views and support data-driven priors. We explore ways to incorporate NeRFs into the OFO dataset, outline future work to support even more state-of-the-art 3D vision models, and describe the importance of high-quality 3D reconstructions for forestry applications.

</details>

#### 2026-06-16 - SPARK: Low Latency Single-Camera 3D Pose Estimation for Autonomous Racing using Keypoints

**Authors:** Dominic Ebner, Markus Lienkamp
**Links:** [abs](https://arxiv.org/abs/2606.17936) - [pdf](https://arxiv.org/pdf/2606.17936)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SPARK: Low Latency Single-Camera 3D Pose Estimation for Autonomous Racing using Keypoints
- 作者：Dominic Ebner, Markus Lienkamp
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2606.17936；PDF: https://arxiv.org/pdf/2606.17936

### 一句话总结
本文提出SPARK，一种基于关键点检测的单目相机3D位姿估计算法，专为自动驾驶赛车设计，在实现高精度远程检测的同时保持低延迟和低资源消耗。

### 研究问题
如何在自动驾驶赛车场景中，利用单目相机快速、准确地检测其他非合作参与者的3D位姿，以支持安全、无碰撞的轨迹规划，并克服LiDAR方法延迟高、边缘部署困难的问题。

### 核心思路/方法
- 采用YOLO模型进行关键点检测，利用自动驾驶赛车环境中固定的几何结构（如赛车尺寸一致性）来提升检测精度与速度。
- 整体框架为端到端单目3D位姿估计，旨在降低延迟并减少计算资源占用。
- 在真实世界的自动驾驶赛车数据上评估，并与当前最先进的LiDAR和相机检测算法进行对比。

### 主要贡献
- 提出SPARK算法，在远程检测中达到高精度，性能超越现有最先进的单目相机检测算法。
- 实现低延迟和低资源消耗，适合边缘设备部署。
- 公开发布源代码，便于复现与进一步研究。

### 局限性
摘要未提供足够信息（未说明算法在极端光照、遮挡条件下的表现，也未提及多目标场景下的具体性能瓶颈）。

### 阅读优先级
高。理由：本文针对自动驾驶赛车这一实时性要求极高的场景，提出了在精度和延迟上优于现有方法的单目解决方案，且代码开源，对相关领域有直接参考价值和复现潜力。

</details>

<details>
<summary>Abstract</summary>

In autonomous racing, fast detection of other participants' movements is required to plan safe, collision-free trajectories with non-cooperative opponents. LiDAR detection is inherently slower and harder to deploy on edge devices than vision methods, causing delayed detections that limit object tracking performance during high-dynamic maneuvering. Utilizing monocular 3D detection enables an easy-to-deploy, low-latency detection of other participants on the racetrack. We present SPARK, a single-camera pose-estimation algorithm for autonomous racing using keypoint detection. It achieves long-range detection with high accuracy, exceeding the performance of state-of-the-art monocular camera detection algorithms while maintaining lower latency. By employing well-optimized YOLO models and leveraging the fixed geometry in the autonomous racing domain, the algorithm also exhibits low latency and resource usage. We evaluate the performance of our approach on real-world autonomous racing data and compare it to state-of-the-art LiDAR and camera detection algorithms. The source code is available at: https://github.com/TUMFTM/SPARK-camera-det

</details>

#### 2026-06-16 - MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization

**Authors:** Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian
**Links:** [abs](https://arxiv.org/abs/2606.17935) - [pdf](https://arxiv.org/pdf/2606.17935)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization
- 作者：Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2606.17935

### 一句话总结
MoonSplat 提出一种集成全局 Sim(3) 优化的在线体素化 3DGS 框架，实现了单目图像序列下的稳健相机追踪与高效全局闭环，并引入颜色残差学习以加速收敛。

### 研究问题
现存在线 3DGS 方法面临两个关键挑战：因缺乏全局优化导致的相机姿态估计脆弱，以及大规模/长序列场景下的优化效率低下。

### 核心思路/方法
1. 提出在线体素化 3DGS 重建框架，并集成全局 **Sim(3)** 优化（即同时优化尺度、旋转和平移），实现相机追踪与全局闭环对相机姿态和体素化 3DGS 的一致性修正。
2. 引入**颜色残差学习**策略，加速体素化 3DGS 的收敛，并提升渲染质量。

### 主要贡献
1. 提出结合全局 Sim(3) 优化的在线体素化 3DGS 系统，显著提升单目序列下相机姿态估计的稳健性和大场景优化效率。
2. 引入颜色残差学习策略，兼顾优化速度与渲染质量。
3. 在多种室内外数据集上，方法在相机姿态估计精度和渲染质量上达到当前最优（SOTA），并保持实时性。
4. 基于该方法开发并部署了真实的无人机主动重建系统，验证了其实用鲁棒性与泛化性。

### 局限性
摘要未提供足够信息。未提及方法在极端动态场景、遮挡、或计算资源约束下的具体表现，也未讨论可能存在的失败模式或假设限制。

### 阅读优先级
**高**  
理由：该工作直击在线 3DGS 的主要痛点（姿态估计不稳定、大场景效率低），提出了具有理论新颖性的 Sim(3) 全局优化与颜色残差学习；实验涵盖多类数据集，并落地到无人机实际系统，对机器人、AR/VR 等应用有直接启发价值。

</details>

<details>
<summary>Abstract</summary>

Online 3D reconstruction from monocular image sequences is a challenging and ongoing research topic. 3D Gaussian Splatting (3DGS), leveraging its high-quality real-time rendering capability, empowers online 3D reconstruction to represent dense scenes with enhanced expressiveness, and thus holds great promise for a wide range of applications such as robotics and AR/VR. However, existing online 3DGS methods still suffer from some key challenges: fragile camera pose estimation due to the lack of global optimization, and low optimization efficiency in large-scale or long-sequence scenarios. To address these issues, we propose a robust and efficient online voxelized 3DGS reconstruction framework integrated with global $\text{Sim}(3)$ optimization, which enables reliable camera tracking and efficient global loop closure for both camera poses and voxelized 3DGS. To accelerate the convergence of the voxelized 3DGS, we further introduce a color residual learning strategy, which not only boosts optimization speed but also enhances rendering quality. Extensive experiments on diverse indoor and outdoor datasets demonstrate that our method achieves state-of-the-art performance in both camera pose estimation accuracy and rendering quality, while retaining real-time efficiency. Additionally, we develop and deploy a real-world UAV-based active reconstruction system grounded on our proposed method, validating its robustness and generalizability for practical online 3D reconstruction tasks. Our code and data are available at https://github.com/TrickyGo/MoonSplat.

</details>

#### 2026-06-16 - High-Fidelity 3D Geometric Reconstruction of Pelvic Organs from MRI: A Hybrid Deep Learning and Iterative Optimization Approach

**Authors:** Hui Wang, Xiaowei Li, Chenxin Zhang, Yifan Feng, Jianwei Zuo, Yumeng Tang, Xiuli Sun, Jianliu Wang, Bing Xie, Jiajia Luo
**Links:** [abs](https://arxiv.org/abs/2606.17836) - [pdf](https://arxiv.org/pdf/2606.17836)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, geometric reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：High-Fidelity 3D Geometric Reconstruction of Pelvic Organs from MRI: A Hybrid Deep Learning and Iterative Optimization Approach  
- 作者：Hui Wang, Xiaowei Li, Chenxin Zhang, Yifan Feng, Jianwei Zuo, Yumeng Tang, Xiuli Sun, Jianliu Wang, Bing Xie, Jiajia Luo  
- 出版日期：2026-06-16  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：摘要页 https://arxiv.org/abs/2606.17836；PDF https://arxiv.org/pdf/2606.17836  

### 一句话总结  
本文提出一种混合深度学习与迭代优化的框架，用于从 MRI 数据中高保真重建盆腔器官（膀胱、子宫、直肠）的 3D 几何结构，在几何精度与网格质量上优于现有主流方法。

### 研究问题  
现有盆腔器官 3D 重建方法要么聚焦分割，要么侧重下游模型应用，缺乏标准化的高保真几何重建流程，导致劳动密集型且保真度不足。

### 核心思路/方法  
提出混合可变形形状建模框架，包含三个核心组件：  
1. **几何感知多层深度学习架构**：保持盆腔器官的拓扑一致性；  
2. **两阶段摊销优化训练策略**：先捕捉全局形状，后优化局部表面；  
3. **全局协同机制**：训练时迭代优化为深度学习提供监督，推理时深度学习快速预测全局形态，再经迭代优化精修局部表面与网格质量。

### 主要贡献  
- 首个集成深度学习预测与迭代优化的盆腔器官高保真重建框架；  
- 在几何保真度上显著优于主流深度学习重建模型（膀胱、直肠、子宫的 Chamfer Distance 更低，Dice 相似系数更高）；  
- 在保持高计算效率的同时，获得更好的整体体网格质量；  
- 在患者级别，框架在最小元素质量指标（minSICN 和 minSIGE）上超过传统几何后处理算法。

### 局限性  
摘要未提供足够信息。

### 阅读优先级  
**高**  
理由：该研究针对医学图像重建中实际问题（盆腔器官高保真几何重建），提出新的混合框架并取得性能提升，适用于需要高精度 3D 模型的下游分析任务；方法结构清晰，有明确的应用价值，对于从事医学图像处理、3D 重建或盆腔建模的研究者具有参考意义。

</details>

<details>
<summary>Abstract</summary>

Patient-specific 3D reconstruction of pelvic organ geometry from MRI is important for pelvic floor modeling and downstream patient-specific analysis. However, while previous studies have focused primarily on either image segmentation or downstream use of 3D models, the reconstruction of high-fidelity, high-quality geometries remains labor-intensive and poorly standardized. The study introduced a hybrid deformable shape modeling framework that integrates deep learning prediction with iterative optimization for the reconstruction of the bladder, uterus, and rectum. The framework consists of three core components: a geometry-aware multi-level deep learning architecture that preserves topological consistency of pelvic organs; a two-stage amortized optimization training strategy that balances global shape capture and local surface refinement; and a holistic synergy mechanism--where iterative optimization provides supervision for deep learning during the training phase, and during inference, deep learning rapidly predicts the global organ morphology, followed by iterative optimization to refine local surfaces and mesh quality. This framework demonstrated marked superiority in geometric fidelity than current mainstream deep learning-based organ reconstruction models. For individual anatomical structures, the reconstructed 3D geometries for the bladder, rectum, and uterus achieved significantly lower Chamfer Distance values and higher Dice Similarity Coefficient scores. In addition, while maintaining high computational efficiency, the proposed architecture yielded superior overall volumetric mesh quality. At the patient level, the framework achieved higher mean values for the 10 worst elements for both minSICN and minSIGE compared to traditional geometric post-processing algorithms.

</details>

#### 2026-06-16 - RICH-SLAM: Radar SLAM with Incremental and Continuous Hilbert Mapping

**Authors:** Bingbing Zhang, Huan Yin, Yang Xu, Shuo Liu, Shaojie Shen, Fumin Zhang, Wen Xu
**Links:** [abs](https://arxiv.org/abs/2606.17534) - [pdf](https://arxiv.org/pdf/2606.17534)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, pose estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RICH-SLAM: Radar SLAM with Incremental and Continuous Hilbert Mapping
- 作者：Bingbing Zhang, Huan Yin, Yang Xu, Shuo Liu, Shaojie Shen, Fumin Zhang, Wen Xu
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry; Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.17534

### 一句话总结
RICH-SLAM 是一种基于雷达的 SLAM 框架，通过增量希尔伯特空间高斯过程建图和后验加权粒子滤波，实现从稀疏噪声雷达测量中构建连续占用地图并支持不确定性感知规划。

### 研究问题
如何克服雷达测量数据稀疏、噪声大的固有缺陷，以实现密集、连续且一致的 SLAM 地图表示。

### 核心思路/方法
- 后端采用 Rao-Blackwellized 粒子滤波器，粒子滤波用于位姿估计，卡尔曼滤波用于地图更新。
- 提出增量希尔伯特空间降秩高斯过程建图策略（Incremental Hilbert-space reduced-rank Gaussian process mapping），能根据稀疏雷达输入生成连续且感知不确定性的地图表示。
- 引入后验感知的粒子加权方案（posterior-aware particle weighting scheme），利用地图参数的完整后验分布进行更鲁棒的似然评估。

### 主要贡献
1. 提出了 RICH-SLAM，一个为雷达传感器设计的完整 SLAM 框架。
2. 设计了增量希尔伯特空间降秩高斯过程映射方法，实现稀疏输入下的连续与不确定性建模。
3. 提出基于后验分布的粒子加权机制，提升似然估计的鲁棒性。
4. 在自采集数据集和公开 ColoRadar 数据集上验证了该方法能从稀疏雷达测量构建连续占用地图，并支持移动机器人的不确定性感知规划。

### 局限性
摘要未提供足够信息，未明确指出本方法的计算复杂度、实时性限制、对雷达硬件或环境的特定约束。

### 阅读优先级
**中**
理由：该方法针对雷达 SLAM 中稀疏、噪声数据导致的建图连续性难题，提出了基于希尔伯特空间高斯过程的创新解决方案，在理论和新颖性方面有亮点，对从事雷达 SLAM 或不确定性感知建图的研究人员有一定参考价值。但摘要未涉及详细实验对比或性能指标，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Simultaneous localization and mapping using radar sensors has gained increasing attention due to radar's inherent robustness to adverse weather and lighting conditions. However, radar measurements are characteristically sparse and noisy compared to LiDAR and visual data, posing significant challenges in achieving dense, continuous, and consistent map representations. In this paper, we present RICH-SLAM, a radar SLAM framework designed to address these challenges. Our approach features a Rao-Blackwellized particle filter-based back end that employs particle filtering for pose estimation and Kalman filtering for map updates. We propose an incremental Hilbert-space reduced-rank Gaussian process mapping strategy that enables continuous and uncertainty-aware map representations given sparse radar inputs. We further introduce a posterior-aware particle weighting scheme that leverages the full posterior distribution of map parameters for more robust likelihood evaluation. Experiments on self-collected and public ColoRadar datasets show that RICH-SLAM constructs continuous occupancy maps from sparse radar measurements and supports uncertainty-aware planning for mobile robots.

</details>

#### 2026-06-16 - Impact of Hand Impairment and Occlusions on Hand Pose Estimation Accuracy in Augmented Reality Applications

**Authors:** Damian M. Manzone, Mathew Szymanowski, Olga Taran, Shuo Cai, Melissa Marquez-Chin, Tammy Zeng, Hardeep Singh, Cesar Marquez-Chin, José Zariffa
**Links:** [abs](https://arxiv.org/abs/2606.17427) - [pdf](https://arxiv.org/pdf/2606.17427)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, AR, augmented reality, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Impact of Hand Impairment and Occlusions on Hand Pose Estimation Accuracy in Augmented Reality Applications
- 作者：Damian M. Manzone, Mathew Szymanowski, Olga Taran, Shuo Cai, Melissa Marquez-Chin, Tammy Zeng, Hardeep Singh, Cesar Marquez-Chin, José Zariffa
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry（主要），Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2606.17427

### 一句话总结
本研究评估了HoloLens 2头戴显示器和多种手部姿态估计算法（WiLoR、HaMeR、WildHands、MediaPipe）在手部受损人群（颈髓损伤患者）与无损伤对照组中，以及与透明和遮挡物体交互时的姿态估计准确性。

### 研究问题
手部损伤和来自真实物体交互的遮挡对增强现实中手部姿态估计准确性的影响，以及AR头戴显示器与现有最先进姿态估计算法的比较。

### 核心思路/方法
- 被试：13名颈髓损伤患者（神经损伤水平C3-C6；ASIA等级A-D）和15名无损伤对照。
- 任务：与透明和不透明物体交互。
- 设备/算法：HoloLens 2 HMD + 4种最先进姿态估计算法（WiLoR, HaMeR, WildHands, MediaPipe）。
- 评估方式：通过多摄像机三角测量生成3D关节位置的真实值，比较预测准确性。

### 主要贡献
1. 首次系统评估手部损伤和物体遮挡对AR HMD及多种姿态估计算法准确性的影响。
2. 发现HoloLens 2和姿态估计算法的预测在受损与无损伤群体间准确性无显著差异，表明这些方法可推广至手部受损人群。
3. 透明物体相比不透明物体提供了微小精度优势（约0.1 mm），WiLoR和HaMeR比HoloLens 2略准确（约2 mm）。
4. 生成的数据库可用于改进针对手部受损人群的姿态估计方法。

### 局限性
摘要未提供足够信息，例如：缺乏具体实验设置（如摄像机数量、光照条件）、不同物体交互类型的详细分析、算法在特定遮挡模式下的表现差异，以及样本量对统计效力的影响等。

### 阅读优先级
高。理由：研究直接针对AR手部康复应用中的核心挑战（手部损伤与遮挡），并提供了主流算法与商业设备（HoloLens 2）的定量比较，对相关领域的研究者和从业者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Mixed reality applications can be designed for hand rehabilitation. Augmented reality (AR) head mounted displays (HMDs) specifically allow for ecologically valid tasks because individuals can see their real environment and interact with real objects while receiving additional cues on the HMD. While these applications rely on accurate hand pose estimation, there is a gap in investigating the influence of hand impairment or occlusion from real-object interactions on pose estimation accuracy. Further, comparisons between AR HMD predictions and state-of-the-art pose estimation methods have not been established. The current study assessed pose estimation accuracy of the HoloLens 2 HMD and state-of-the-art pose estimation algorithms (WiLoR, HaMeR, WildHands, and MediaPipe) while individuals with cervical spinal cord injury (cSCI; n = 13, Neurological Level of Injury: C3-C6; American Spinal Injury Association Impairment Scale: A-D) and 15 uninjured controls interacted with clear and opaque objects. Ground truth estimates of 3D joint positions were generated via triangulation from a multi-camera setup. Pose estimation accuracy did not differ between the cSCI and uninjured control groups suggesting that 3D joint predictions from the HoloLens 2 and pose estimation algorithms can generalize to populations with hand impairment. Further, clear objects provided a small accuracy advantage over opaque objects (0.1 mm) and predictions from both WiLoR and HaMeR were slightly more accurate than the HoloLens 2 (2 mm). Overall, these results suggest that the HoloLens 2 may be viable for hand rehabilitation applications and the dataset generated can be used to refine pose estimation methods for hand-impaired populations.

</details>

#### 2026-06-15 - SGM-SLAM: Scene Graph Matching for Data-Efficient Distributed SLAM

**Authors:** Yewei Huang, Tixiao Shan, Abhinav Rajvanshi, Niluthpol Chowdhury Mithun, Yaxuan Li, Brendan Englot, Han-Pang Chiu
**Links:** [abs](https://arxiv.org/abs/2606.16881) - [pdf](https://arxiv.org/pdf/2606.16881)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SGM-SLAM: Scene Graph Matching for Data-Efficient Distributed SLAM
- 作者：Yewei Huang, Tixiao Shan, Abhinav Rajvanshi, Niluthpol Chowdhury Mithun, Yaxuan Li, Brendan Englot, Han-Pang Chiu
- 出版日期：2026-06-15
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：摘要： https://arxiv.org/abs/2606.16881 ；PDF： https://arxiv.org/pdf/2606.16881

### 一句话总结
提出一种基于场景图匹配的数据高效分布式SLAM框架，通过仅使用对象标签和质心进行匹配，实现多机器人间的协作定位与建图。

### 研究问题
如何高效地在多机器人分布式SLAM系统中，利用场景图匹配识别机器人间的测量约束，同时降低通信和数据交换成本。

### 核心思路/方法
1. 构建场景图：利用融合的RGB-LiDAR点云生成语义分割点云层和离散有界对象层，并辅以估计的机器人轨迹。
2. 场景图匹配：仅使用对象标签和质心（而非传统特征级匹配）进行协作匹配，通过多步数据交换与优化过程最大化通信效率。
3. 框架集成：将场景图匹配作为分布式SLAM的约束机制，支持装备激光雷达、相机和惯性传感器的机器人团队。

### 主要贡献
- 首次提出仅依赖对象标签和质心的场景图匹配方法，用于分布式SLAM中的机器人间约束识别。
- 设计了多步数据交换与优化流程，显著提升通信效率。
- 通过仿真和真实世界（四足机器人）数据集验证了框架在室内外环境中的有效性与高效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。
理由：该工作聚焦分布式SLAM中的数据效率和场景图匹配，属于技术设计完善的应用型研究，但未提供与现有方法的定量对比或极致性能提升证据，适合对多机器人SLAM或语义建图感兴趣的读者参考。

</details>

<details>
<summary>Abstract</summary>

We introduce a data-efficient distributed Simultaneous Localization and Mapping (SLAM) framework designed for a team of robots equipped with LiDAR, cameras, and inertial sensors. Our framework uses scene graph matching to identify inter-robot measurement constraints. Unlike prior approaches that rely on feature-level matching, our framework is the first to perform scene graph matching using only object labels and centroids. Our approach constructs a scene graph by using fused RGB-LiDAR point clouds to generate both a semantically segmented point cloud layer, and a layer of discrete bounded objects, to accompany estimated robot trajectories. Scene graph matching is performed collaboratively through exchanging and matching object data with neighboring robots. To maximize communication efficiency, we utilize a multi-step data exchange and optimization process. We demonstrate the effectiveness and efficiency of our approach using both simulation and real-world datasets collected by legged robots in indoor and outdoor environments.

</details>

#### 2026-06-15 - MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods

**Authors:** Robert Langendörfer, Markus Hillemann, Markus Ulrich
**Links:** [abs](https://arxiv.org/abs/2606.16638) - [pdf](https://arxiv.org/pdf/2606.16638)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** visual geometry grounded transformer, 3D reconstruction, multi-view stereo, structure from motion, camera pose estimation, pose estimation, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods
- 作者：Robert Langendörfer, Markus Hillemann, Markus Ulrich
- 出版日期：2026-06-15T12:26:47Z
- 分类：3D Reconstruction & Multi-view Geometry (主要), Neural Scene Representations & Rendering (次要)
- 链接：摘要链接: https://arxiv.org/abs/2606.16638, PDF链接: https://arxiv.org/pdf/2606.16638

### 一句话总结
本文提出了一个名为MVM-IOD的工业物体中心基准数据集，用于评估3D重建方法，并基于该数据集对当前多种SOTA方法（如SfM、MVS、前馈网络等）进行了实验。

### 研究问题
现有的3D重建和相机位姿估计数据集大多未描绘真实的工业场景，而工业应用中的高成本和时间限制使得该任务极具挑战性。

### 核心思路/方法
1.  **构建数据集 (MVM-IOD)**：通过将工业机器人臂末端执行器上的相机沿半球轨迹系统性地移动，采集典型工业物体的RGB图像、参考相机位姿和参考3D点云。数据集包含9个物体和2种背景选择，共18个场景。
2.  **定义基准评估**：基于该数据集，对多种当前SOTA方法（包括传统方法如Structure from Motion、Multi-View Stereo，以及前馈方法如Visual Geometry Grounded Transformer、π3，还有2D Gaussian Splatting）进行广泛评估，报告基线结果。

### 主要贡献
1.  **引入MVM-IOD数据集**：该数据集专门针对真实工业场景中的3D重建和相机位姿评估，提供参考位姿和点云。
2.  **揭示前馈方法的局限性**：实验表明，数据集中的捕获设置（半球轨迹）为前馈方法生成了分布外图像，导致次优的点云和位姿。
3.  **提出改进路径**：发现通过应用简单的预处理步骤，可以将分布外图像向训练分布偏移，从而改善前馈方法性能，并提示在特定工业应用中应谨慎使用这些方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：论文提出了一个针对特定工业场景的基准数据集（MVM-IOD），并基于该数据集对比了传统与前沿（如前馈网络）3D重建方法，为评估该类方法提供了标准。但数据集的具体细节（如物体种类、数量、场景复杂性）及实验结果的量化指标在摘要中未展示，需要阅读全文才能获得更深入的见解。

</details>

<details>
<summary>Abstract</summary>

3D object reconstruction, and camera pose estimation in industrial applications are challenging tasks, as errors are costly while the computation time is often limited. The complexity of typical industrial objects further complicates these tasks. Most of the existing datasets in this context do not depict realistic industrial scenarios. Therefore, we introduce the Machine Vision Metrology Industrial Object Dataset (MVM-IOD). Images of typical industrial objects are captured systematically, by moving a camera, mounted at the end effector of an industrial robot arm, on a hemisphere around the objects. MVM-IOD contains reference camera poses and reference 3D point clouds, the acquired RGB images of 9 objects and 2 background choices resulting in 18 scenes, which allows evaluation of all image based methods that compute a 3D reconstruction, camera poses, or novel views of a scene. Based on MVM-IOD, we extensively evaluate current SOTA 3D reconstruction and camera pose estimation methods, such as Structure from Motion, Multi-View Stereo, recent feed forward methods (Visual Geometry Grounded Transformer, π3), and 2D Gaussian Splatting and report our findings as a baseline for future research. The experiments show that capture setups like ours generate out-of distribution images for feed forward methods, leading to suboptimal point clouds and camera poses. However, these out-of-distribution images can be shifted closer to the training distribution by applying simple preprocessing steps. Consequently, in certain industrial applications, feed forward methods should be used with caution.

</details>

#### 2026-06-15 - Rotational Symmetry based Object Pose Estimation from Point Clouds in the Absence of Known 3D Models

**Authors:** Weichen Dai, Ruixun Yu, Yangjie Tang, Yifan Du, Yiyang Zhang, Donglei Sun, Hua Zhang
**Links:** [abs](https://arxiv.org/abs/2606.16593) - [pdf](https://arxiv.org/pdf/2606.16593)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rotational Symmetry based Object Pose Estimation from Point Clouds in the Absence of Known 3D Models
- 作者：Weichen Dai, Ruixun Yu, Yangjie Tang, Yifan Du, Yiyang Zhang, Donglei Sun, Hua Zhang
- 出版日期：2026-06-15
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：abstract: https://arxiv.org/abs/2606.16593 ; pdf: https://arxiv.org/pdf/2606.16593

### 一句话总结
提出一种在无已知3D模型情况下，利用物体旋转对称性先验信息，通过迭代优化同时估计点云姿态并细化点云的方法。

### 研究问题
如何在没有已知高质量3D模型（例如因保密限制无法获取）的条件下，仅依据点云数据实现工业物体的姿态估计。

### 核心思路/方法
1. **利用旋转对称性**：将工业物体常见的旋转对称性作为先验信息，替代缺失的3D模型。
2. **迭代优化过程**：姿态估计与点云细化联合进行。
3. **旋转对称约束损失**：
   - 根据当前估计的姿态旋转每个3D点。
   - 利用旋转对称性，通过最近邻搜索为每个点找到多个对应点。
   - 基于这些对应关系计算旋转对称约束损失，用于迭代更新姿态和点云。

### 主要贡献
- 提出一种不依赖已知3D模型，仅靠旋转对称性先验实现点云姿态估计的方法。
- 通过显式将旋转对称性融入优化过程，方法在多种物体类型上表现出鲁棒性和良好的泛化能力。
- 在自建数据集（含四类合成物体和一类真实轮毂）上，性能与依赖已知3D模型的方法相当。

### 局限性
摘要未提供足够信息。例如，未说明方法在非对称物体上的表现、对强噪声或遮挡的处理能力，也未提及计算效率或依赖的具体对称性条件（如仅轴向对称还是多类对称）。

### 阅读优先级
**中**
理由：研究问题（无模型姿态估计）具有实际应用价值，且方法思路清晰（利用旋转对称性+迭代优化）。但需注意其适用场景局限在有旋转对称性的工业零件上，且摘要未提供详细定量对比结果，需阅读全文评估实际效果和泛化性。

</details>

<details>
<summary>Abstract</summary>

Object pose estimation is crucial to many industrial applications, with one example being automated spray painting using a robot. However, confidentiality concerns often limit access to high-quality 3D models, posing a significant challenge for point-cloud-based pose estimation. In such scenarios, rotational symmetry, a readily accessible characteristic of many industrial objects, can provide valuable prior information to facilitate pose estimation.In this paper, we propose a method that leverages the rotational symmetry commonly found in industrial objects to address the challenge caused by the absence of 3D models. The object pose is jointly estimated with point cloud refinement through an iterative optimization process. This optimization relies on a rotational symmetry constraint loss. To construct this loss, each 3D point is rotated according to the currently estimated pose, and multiple correspondences are identified using nearest-neighbor search by exploiting the rotational symmetry property. These correspondences are then used to compute the rotational symmetry constraint loss, which iteratively refines both the pose and the point cloud.By explicitly incorporating rotational symmetry into the optimization process, the proposed method achieves robust pose estimation and generalizes well across diverse object types. The proposed method is evaluated on a dataset specifically created for point clouds without known 3D models, consisting of four categories of synthetic objects and one real wheel hub collected from a production line. Experimental results demonstrate that the proposed method achieves performance comparable to methods that rely on known 3D models.

</details>

#### 2026-06-15 - Instance-Aware Knowledge Distillation for Semi-Supervised Learning of an On-Board Multi-Task Dense Prediction Model for Collision Avoidance System

**Authors:** Gyutae Hwang, Sang Jun Lee
**Links:** [abs](https://arxiv.org/abs/2606.16414) - [pdf](https://arxiv.org/pdf/2606.16414)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, monocular depth, driving scene, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Instance-Aware Knowledge Distillation for Semi-Supervised Learning of an On-Board Multi-Task Dense Prediction Model for Collision Avoidance System
- 作者：Gyutae Hwang, Sang Jun Lee
- 出版日期：2026-06-15T08:51:06Z
- 分类：3D Reconstruction & Multi-view Geometry（主类）；Embodied / Robotics / AR Applications（次类）
- 链接：摘要：https://arxiv.org/abs/2606.16414 | PDF：https://arxiv.org/pdf/2606.16414

### 一句话总结
本文提出一种实例感知知识蒸馏框架，用于半监督学习轻量级多任务密集预测模型，并部署于低算力边缘设备的碰撞避免系统，在目标域（乡村俱乐部数据集）上实现学生模型性能超越大教师模型，计算量大幅降低。

### 研究问题
如何在有限计算资源和标注成本下，为碰撞避免系统训练一个轻量级、多任务密集预测模型，并部署到边缘设备上。

### 核心思路/方法
1. **实例感知知识蒸馏框架**：结合教师模型的域先验和基础模型的实例中心知识，生成伪标签以缓解教师偏差。  
2. **半监督学习**：利用伪标签进行训练，降低对大规模标注数据集的依赖。  
3. **多任务密集预测**：学生模型同时执行前向障碍物检测和单目深度估计。  
4. **系统部署**：将学生模型部署到低算力边缘设备，实时将障碍物空间信息编码为CAN消息，用于自动导引车操作。  
5. **数据集构建与验证**：构建大型乡村俱乐部数据集，并进行实地验证。

### 主要贡献
1. 提出基于实例感知知识蒸馏的半监督学习框架，有效缓解教师偏差。  
2. 学生模型在实例分割任务上超越教师模型，并在单目深度估计中保持性能稳定。  
3. 与教师模型相比，学生模型FLOPs降低22.68倍，参数量减少14.33倍，在低算力边缘设备上达到6.46 FPS。  
4. 构建了大型乡村俱乐部数据集，并完成多任务密集预测碰撞避免系统的实地验证。

### 局限性
摘要未提供足够信息：未提及伪标签生成的具体失败案例、框架对不同数据域（非乡村俱乐部场景）的泛化能力、深度估计性能下降的具体数值、系统在极端场景（如夜间、恶劣天气）下的表现，以及半监督学习所需的未标注数据量等。

### 阅读优先级
**高**  
理由：  
- 提出新颖的实例感知知识蒸馏框架，结合半监督学习，有效解决边缘部署中的算力和标注瓶颈。  
- 实验结果显著（学生模型参数量和FLOPs大幅降低，部分任务性能超越教师），具有实际应用价值。  
- 涉及当前热门方向（多任务密集预测、边缘AI、自动导引车安全），对计算机视觉和机器人交叉领域的研究者有参考意义。

</details>

<details>
<summary>Abstract</summary>

Collision avoidance systems have evolved toward camera-based deep learning approaches for driving scene understanding. However, deployment in edge environments such as country clubs is constrained by limited computational resources and unreliable communication infrastructure. Moreover, constructing large-scale datasets for the target domain involves substantial annotation cost. To address these limitations, we propose an instance-aware knowledge distillation framework for semi-supervised learning. Specifically, we generate pseudo labels that mitigate teacher bias by leveraging domain priors from the teacher and instance-centric knowledge from foundation models. The trained lightweight student is deployed in the proposed collision avoidance system and performs multiple dense prediction tasks in real-time. The system detects frontal obstacles and encodes their spatial information into controller area network messages for automated guided vehicle operation. To achieve this, we construct a large-scale country club dataset and perform field validation of the proposed system. Experimental results demonstrate that the student outperforms the large teacher in instance segmentation while mitigating performance degradation in monocular depth estimation. Compared with the teacher, the student reduces FLOPs by 22.68$\times$ and parameters by 14.33$\times$, achieving 6.46 FPS on a low-cost edge device.

</details>

#### 2026-06-12 - StereoGeo: an end-to-end stereo camera calibration method

**Authors:** Imane Meddour, Andréa Macario Barros, Cédric Gouy-Pailler
**Links:** [abs](https://arxiv.org/abs/2606.14619) - [pdf](https://arxiv.org/pdf/2606.14619)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StereoGeo: an end-to-end stereo camera calibration method
- 作者：Imane Meddour, Andréa Macario Barros, Cédric Gouy-Pailler
- 出版日期：2026-06-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.14619

### 一句话总结
本文提出了一种基于端到端网络的立体相机标定方法StereoGeo，能够同时估计左右相机的焦距、重力方向以及两者之间的相对外参。

### 研究问题
如何设计一种端到端的方法，在无需结构化环境中的标定图案、且不局限于单目或多视角设置的情况下，同时完成立体相机的内参（焦距、重力方向）和外参（相对位姿）标定。

### 核心思路/方法
扩展GeoCalib算法，将深度神经网络的特征提取与可微分优化器相结合，构建一个端到端的网络架构，用于立体相机标定。

### 主要贡献
1. 提出了StereoGeo，首个端到端的立体相机标定网络，同时估计左右相机的焦距、重力方向及相对外参。
2. 在真实世界基准数据集上，该方法在内参标定上达到有竞争力表现，并在立体外参估计上准确度优于现有的单目方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法聚焦于立体相机标定这一专业子领域，解决了现有方法在端到端联合标定上的不足，但论文公开的摘要篇幅有限，缺乏对方法架构细节、实验设置和量化结果的深入描述，适合对该方向有特定需求的读者作为参考。

</details>

<details>
<summary>Abstract</summary>

In this work, we propose StereoGeo, an end-to-end network-based approach for stereo camera calibration. Our method estimates the focal lengths and gravity directions of the left and right cameras, as well as the relative extrinsic transformation relating them. Existing methods often rely on calibration patterns in structured environments or address only a single camera configuration, being limited to either intrinsic or extrinsic estimation, and depending on a multi-view setups. StereoGeo extends the GeoCalib algorithm, integrating deep neural network feature extraction with a differentiable optimizer. Extensive experiments on real-world benchmarks demonstrate that StereoGeo achieves competitive performance for intrinsic calibration and provides accurate stereo extrinsic estimation, outperforming existing methods that are limited to monocular settings. The dataset used in this work is partially publicly available at https://github.com/meddourimane/StereoGeo-dataset.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-18 - VisDom: Sparse Novel View Synthesis with Visible Domain Constraint

**Authors:** Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers
**Links:** [abs](https://arxiv.org/abs/2606.20531) - [pdf](https://arxiv.org/pdf/2606.20531)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VisDom: Sparse Novel View Synthesis with Visible Domain Constraint
- 作者：Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers
- 出版日期：2026-06-18
- 分类：Neural Scene Representations & Rendering
- 链接：论文摘要 https://arxiv.org/abs/2606.20531 | PDF https://arxiv.org/pdf/2606.20531

### 一句话总结
VisDom 提出一种无需学习的几何约束（可见域约束），通过最小多视图可见性要求，从稀疏输入中改进新视角合成的几何一致性。

### 研究问题
稀疏新视角合成（NVS）中，从少量输入视图恢复3D几何存在模糊性，现有NeRF和Gaussian Splatting方法在稀疏设置下易过拟合，产生漂浮伪影和不一致几何；仅使用轮廓一致性作为正则化仍不足够，因为轮廓一致区域可能超出真实物体几何。

### 核心思路/方法
- 定义“可见域”为至少被K个视图观测到的3D子空间，并将其作为额外过滤标准，叠加在标准基于轮廓的重建之上，以提供更强的空间先验。
- 将VisDom集成到隐式（NeRF）和显式（GS）管线中，通过限制体素采样和指导高斯点优化时的放置。
- 该方法无需学习参数，仅需轮廓图，作为简单补充组件。

### 主要贡献
1. 提出一种无学习的几何约束（可见域），增强经典视觉外壳重建，有效缓解稀疏视图下的几何模糊。
2. 展示VisDom可无缝集成到NeRF和Gaussian Splatting两类管线中，提升稀疏NVS质量。
3. 在三个挑战性数据集上，从仅4张输入图像实现高质量物体中心重建，并能在GaussianObject之上以22倍更低训练成本达到或超越其性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法简洁（无学习参数、仅需轮廓图）且效果显著（在多个数据集和两种主流管线中稳定提升性能），对从事稀疏视图3D重建和新视角合成的研究者具有较高的实用参考价值。

</details>

<details>
<summary>Abstract</summary>

Sparse novel view synthesis (NVS) remains challenging due to the ambiguity of recovering 3D geometry from few input views. While NeRF- and Gaussian Splatting (GS)-based methods perform well with dense supervision, they often overfit in sparse settings, producing floating artifacts and inconsistent geometry. Silhouette consistency is commonly used as a regularizer, but it remains insufficient, as silhouette-consistent regions can extend beyond the true object geometry. We introduce VisDom, a learning-free geometric constraint that augments classical carving-based visual hull reconstruction by enforcing a minimum multi-view visibility requirement. Specifically, we define a visible domain as the subset of 3D space observed by at least $K$ views and use it as an additional filtering criterion on top of standard silhouette-based reconstruction. This provides a stronger spatial prior in sparse-view settings. We integrate VisDom into both implicit (NeRF) and explicit (GS) pipelines by restricting volumetric sampling and guiding Gaussian placement during optimization. Experiments on three challenging datasets show consistent improvements in sparse-view NVS, enabling high-quality object-centric reconstruction from as few as four input images. Our method is domain-agnostic, requires only silhouettes, and introduces no learned parameters, making it a simple complement to existing approaches. Applying VisDom on top of GaussianObject further improves performance on Omni3D and MipNeRF360, while matching or surpassing it at 22 $\times$ lower training cost.

</details>

#### 2026-06-18 - LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping

**Authors:** Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui
**Links:** [abs](https://arxiv.org/abs/2606.20424) - [pdf](https://arxiv.org/pdf/2606.20424)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** bundle adjustment, Gaussian Splatting, neural rendering, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping
- 作者：Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui
- 出版日期：2026-06-18
- 分类：Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2606.20424；PDF：https://arxiv.org/pdf/2606.20424

### 一句话总结
LIT-GS 提出一种融合 LiDAR、惯性和热成像数据的高斯泼溅建图框架，通过注入 LiDAR 平面几何约束来克服光照变化和低纹理场景下的结构漂移与渲染退化问题。

### 研究问题
现有的 LiDAR-惯性-视觉（LIV）高斯建图方法依赖 RGB 光度线索，在光照变化大或纹理缺乏的环境中脆弱易失效。本文旨在利用热成像通道替代视觉信息，解决弱光/无纹理条件下的几何精度和渲染质量下降问题。

### 核心思路/方法
1. **跨模态锚定**：将 LIV 视觉地图点作为置信度感知的跨模态锚点，建立可靠的热成像-LiDAR 关联。
2. **联合光束法平差**：在弱热监督下，将加权 LiDAR 点到平面残差加入光束法平差中，联合优化相机位姿和 3D 点。
3. **LiDAR 平面正则化渲染**：在优化后的结构基础上，引入 LiDAR 平面正则化的可微泼溅目标，约束渲染出的 3D 点与局部观测平面对齐，减少低对比度热成像中的表面增厚和结构漂移。

### 主要贡献
- 提出首个融合 LiDAR、惯性、热成像的高斯泼溅建图框架，增强对光照变化的鲁棒性。
- 设计置信度感知的跨模态热成像-LiDAR 关联机制及 LiDAR 平面正则化的可微约束。
- 在自有序列和公开数据集上，相比现有 LIV 高斯泼溅基线，在几何精度和渲染质量上取得一致提升，尤其在高挑战光照条件下表现突出。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对现有 LIV 高斯泼溅方法在弱光和低纹理场景下的关键瓶颈提出了创新性融合方案，实验证明了显著提升，对机器人、自动驾驶及 AR 领域的视觉建图与渲染具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has enabled real-time neural rendering, yet existing LiDAR-inertial-visual (LIV) Gaussian mapping pipelines remain fragile under illumination changes and texture-deficient scenes due to their reliance on RGB photometric cues. We present LIT-GS, a LiDAR-inertial-thermal Gaussian Splatting framework that injects LiDAR-derived plane geometry as an explicit constraint in both pose/structure refinement and Gaussian optimization. Specifically, we exploit LIV visual map points as confidence-aware cross-modal anchors to establish reliable thermal-LiDAR associations, and incorporate weighted LiDAR point-to-plane residuals into bundle adjustment to jointly refine camera poses and 3D points under weak thermal supervision. Building on the refined structure, we further introduce a LiDAR-plane-regularized differentiable splatting objective that constrains rendered 3D points to align with locally observed planes, mitigating surface thickening and structural drift in low-contrast thermal imagery. Experiments on proprietary sequences and public datasets demonstrate that LIT-GS consistently improves geometric accuracy and rendering quality over state-of-the-art LIV-based Gaussian Splatting baselines, particularly in challenging lighting conditions.

</details>

#### 2026-06-18 - Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration

**Authors:** Kyoleen Kwak, Daeho Kim, Jeong Woon Lee, Hyoseok Hwang
**Links:** [abs](https://arxiv.org/abs/2606.20103) - [pdf](https://arxiv.org/pdf/2606.20103)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** camera calibration, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration
- 作者：Kyoleen Kwak, Daeho Kim, Jeong Woon Lee, Hyoseok Hwang
- 出版日期：2026-06-18
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.20103

### 一句话总结
本文提出一种在3D高斯溅射框架中保留度量几何信息的方法，通过密集深度监督和阻止光度梯度更新高斯空间参数，提升了激光雷达与相机的外参标定精度。

### 研究问题
现有基于3D高斯溅射（3DGS）的激光雷达-相机无目标外参标定方法中，由于3DGS本身是为新视角合成设计的，代理几何结构容易偏离真实的激光雷达度量结构，导致标定精度受限。

### 核心思路/方法
1. 通过聚合多视角激光雷达观测数据，提供密集的深度监督，以保持高斯代理的度量几何一致性。
2. 阻断来自光度（图像）重建的梯度对高斯空间参数的更新，从而防止渲染质量优先导致的几何漂移。

### 主要贡献
- 提出一种几何保持框架，确保3D高斯代理的度量结构与真实激光雷达结构一致。
- 在公开驾驶数据集上，所提方法在标定精度上持续优于现有无目标标定方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦于自动驾驶中多模态传感器的标定问题，对从事激光雷达-相机融合感知的研究者具有直接参考价值；但需要读者对3D高斯溅射和标定框架有一定基础，非通用视觉论文。

</details>

<details>
<summary>Abstract</summary>

Accurate LiDAR-camera calibration is essential for robust multi-modal perception. Targetless approaches avoid manual setup but remain limited by the scarcity of discriminative cross-modal features. Recent methods address this by reconstructing the scene within a differentiable model, enabling extrinsic optimization through dense photometric supervision. Among these, 3D Gaussian Splatting (3DGS) has been widely adopted as a geometric proxy that bridges LiDAR and camera within a single differentiable framework. However, since 3DGS was originally designed for novel view synthesis, existing methods tend to prioritize rendering quality, causing the proxy geometry to drift from the true LiDAR structure. We propose a framework that preserves the metric geometry of the Gaussian proxy by aggregating multi-view LiDAR observations for dense depth supervision and blocking photometric gradients from updating the Gaussian spatial parameters. We validate our method on public driving datasets, where it consistently outperforms existing targetless methods in calibration accuracy.

</details>

#### 2026-06-17 - Building Drift: Documenting On-Site Construction Adaptations Across Material Lifecycles

**Authors:** Ritik Batra, Martin Tamke, Tom Svilans, Jan Hüls, Amritansh Kwatra, Steven J. Jackson, Thijs Roumen, Mette Ramsgaard Thomsen
**Links:** [abs](https://arxiv.org/abs/2606.19609) - [pdf](https://arxiv.org/pdf/2606.19609)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Building Drift: Documenting On-Site Construction Adaptations Across Material Lifecycles
- 作者：Ritik Batra, Martin Tamke, Tom Svilans, Jan Hüls, Amritansh Kwatra, Steven J. Jackson, Thijs Roumen, Mette Ramsgaard Thomsen
- 出版日期：2026-06-17
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：摘要: https://arxiv.org/abs/2606.19609 | PDF: https://arxiv.org/pdf/2606.19609

### 一句话总结
本文提出“建筑漂移”（building drift）概念，描述回收材料建筑在现场施工中物理状态与数字模型的偏差，并开发了基于视频和3D高斯泼溅的文档工具Pentimento，用于记录和呈现现场适应过程以支持材料循环利用。

### 研究问题
如何系统性地记录、表征和传递回收材料建筑在现场施工中因不可预测性产生的物理适配（即“建筑漂移”），从而为材料在多个生命周期中的评估、传承和再利用提供必要信息。

### 核心思路/方法
1. **案例研究**：通过回收木材展馆ReShelter的建造实践，归纳出现场适应的分类法（Tending the Site, Foraging for Fit, Interpreting the Material, Marking Measurements, Coordinating Across Communities）。
2. **工具开发**：提出名为Pentimento的文档工具，利用视频文档和3D高斯泼溅技术，在空间、时间和语义三个维度上，将现场适应与设计模型相关联，使各利益相关方能导航材料历史。

### 主要贡献
1. 提出“建筑漂移”概念，系统刻画回收材料建筑在生命周期中的物理状态与数字模型间的集体偏差。
2. 建立建筑漂移的分类法，涵盖现场适应、材料解读、社区协调等五个关键类别。
3. 开发Pentimento工具，将视频与3D高斯泼溅结合，实现现场适应的空间、时间与语义化记录，降低材料再利用障碍。

### 局限性
摘要未提及方法在规模扩展性、计算效率、不同材料类型或建筑场景下的适用性评估；也未说明工具对协作流程的量化影响或用户验证结果。

### 阅读优先级
**中**  
理由：该工作聚焦可持续建筑中的材料记录与数字孪生，核心创新在于将计算机视觉技术（3D高斯泼溅）应用于建筑现场适应的文档化。若对循环经济、建筑信息建模或现场施工协作感兴趣，该文具有启发价值；但若需具体技术实现细节或实验评估，摘要内容有限。

</details>

<details>
<summary>Abstract</summary>

In a circular economy for construction, reclaimed materials carry prior lives of use and go on to have post-lives in future buildings. Yet working with such materials introduces unpredictability that requires on-site improvisation, making their reuse challenging to document and scale across building lifetimes. Without documentation, the on-site adaptations that make construction with reclaimed materials possible leave collaborators, evaluators, and inheritors without the information they need to continue, assess, and reuse materials. We call the collective deviation of the physical state from the digital model through these adaptations "building drift." Through a case study, ReShelter, a reclaimed timber pavilion constructed in the forest, we develop a taxonomy for building drift that characterizes the collective deviation across building lifetimes: Tending the Site, Foraging for Fit, Interpreting the Material, Marking Measurements, and Coordinating Across Communities. To put our taxonomy for building drift into practice, we present Pentimento, a documentation tool that leverages video documentation and 3D Gaussian Splatting to spatially, temporally, and semantically represent on-site adaptations in relation to the designed model. Pentimento enables each stakeholder to navigate material histories in ways that reduce barriers to material reuse. Together, these contributions open pathways towards computational tools that support the on-site improvisation essential to construction with reclaimed materials, enabling more sustainable cycles of recovery, repair, and reuse.

</details>

#### 2026-06-17 - One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies

**Authors:** Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song
**Links:** [abs](https://arxiv.org/abs/2606.19586) - [pdf](https://arxiv.org/pdf/2606.19586)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies
- 作者：Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song
- 出版日期：2026-06-17T20:41:13Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.19586

### 一句话总结
本文提出一种数据增强框架，通过生成逼真的鱼眼图像序列和物理可行的动作轨迹，提升视觉运动策略在操作任务中的成功率和泛化能力。

### 研究问题
如何利用少量真实世界演示数据，生成增强的视觉和动作数据，以减轻视觉运动策略对初始配置和未见过障碍物的分布外失败问题。

### 核心思路/方法
1. 使用便携式平行夹爪和单个鱼眼相机捕获真实世界“眼在手”演示。
2. 引入适用于大视场鱼眼相机的新型高斯溅射公式，重建并编辑包含未见过物体的3D场景。
3. 通过轨迹优化生成平滑、无碰撞、利于视图渲染的动作轨迹，并从对应新视角渲染视觉观察。

### 主要贡献
提出一种有效的数据增强框架，无需大量数据收集，通过生成视觉真实的鱼眼图像序列和对应物理可行的动作轨迹，改善了同一场景和包含障碍物的增强场景下多种操作任务的成功率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该工作针对视觉运动策略的分布外泛化问题提出了一种数据增强方法，创新性较强，但摘要未详述实验设置、基线对比和优势量化，因此适合对数据增强或场景理解方向感兴趣的读者进一步参考，但优先级中等。

</details>

<details>
<summary>Abstract</summary>

Visuomotor policies for manipulation have demonstrated remarkable potential in modeling complex robotic behaviors, yet minor alterations in the robot's initial configuration and unseen obstacles easily lead to out-of-distribution observations. Without extensive data collection effort, these result in catastrophic execution failures. In this work, we introduce an effective data augmentation framework that generates visually realistic fisheye image sequences and corresponding physically feasible action trajectories from real-world eye-in-hand demonstrations, captured with a portable parallel gripper with a single fisheye camera. We introduce a novel Gaussian Splatting formulation, adapted to wide FoV fisheye cameras, to reconstruct and edit the 3D scene with unseen objects. We utilize trajectory optimization to generate smooth, collision-free, view-rendering-friendly action trajectories and render visual observations from corresponding novel views. Comprehensive experiments in simulation and the real world show that our augmentation framework improves the success rate for various manipulation tasks in both the same scene and the augmented scene with obstacles requiring collision avoidance.

</details>

#### 2026-06-17 - 3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning

**Authors:** Ellina Zhang, Madhaven Iyengar, Amir Zadeh, Chuan Li, Deepak Pathak, David Held, Tal Daniel
**Links:** [abs](https://arxiv.org/abs/2606.19451) - [pdf](https://arxiv.org/pdf/2606.19451)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning
- 作者：Ellina Zhang, Madhaven Iyengar, Amir Zadeh, Chuan Li, Deepak Pathak, David Held, Tal Daniel
- 出版日期：2026-06-17T18:00:08Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.19451

### 一句话总结
本文提出3D-DLP模型，是一种自监督的3D以物体为中心的场景表示学习方法，通过将RGB-D或体素观测分解为可解释的3D潜粒子，实现场景重构和下游操控任务性能提升。

### 研究问题
如何从3D场景观测（RGB-D或体素）中学习一种以物体为中心、可解释且可控的潜表示，同时避免对密集3D输入的高内存消耗，并提升下游机器人操控任务的表现。

### 核心思路/方法
基于Deep Latent Particles (DLP)框架扩展至3D，将场景级RGB-D或体素观测分解为一组3D潜粒子。每个粒子编码解耦的属性，包括3D关键点位置、包围框尺寸和外观特征，代表场景中的一个不同实体。模型通过端到端的自监督重构目标学习每个粒子的可解释分割图。

### 主要贡献
1. 提出3D-DLP，一种自监督的3D以物体为中心的场景表示学习模型，能够将场景解耦为一组3D潜粒子。
2. 每个潜粒子编码解耦的3D属性（位置、尺寸、外观），并学习可解释的逐粒子分割图。
3. 在模拟和真实数据集上证明，通过操纵粒子位置和重构可生成新场景配置。
4. 将紧凑的3D潜粒子用于下游机器人操控任务，性能优于缺乏明确3D信息或使用无物体结构密集3D输入的基线方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作结合了自监督学习、3D场景表示和机器人操控，但摘要中实验细节和量化结果（如具体性能提升幅度）未披露，仅通过定性描述展示优势。若读者对物体中心表示或自监督3D理解感兴趣，值得阅读；若需严格对比基线，需查阅全文。

</details>

<details>
<summary>Abstract</summary>

We introduce 3D-DLP, a self-supervised object-centric representation learning model that decomposes scene-level RGB-D or voxel observations into a set of 3D latent particles. Building on the Deep Latent Particles (DLP) framework, each particle encodes disentangled attributes, including 3D keypoint position, bounding box dimensions, and appearance features, and represents a distinct entity in the scene. The model learns interpretable per-particle segmentation maps through an end-to-end self-supervised reconstruction objective. We demonstrate on both simulated and real-world datasets that the learned latent space is interpretable and controllable: by manipulating particle positions and decoding, we can generate novel scene configurations. Furthermore, we show that leveraging these compact 3D latent particles for downstream robotic manipulation improves performance over baselines that either lack explicit 3D information or rely on memory-intensive dense 3D inputs without object-centric structure. Code and videos are available at https://eubooks3003.github.io/3d-dlp.

</details>

#### 2026-06-17 - NeuMesh++: Towards Versatile and Efficient Volumetric Editing with Disentangled Neural Mesh-based Implicit Field

**Authors:** Chong Bao, Yuan Li, Bangbang Yang, Yujun Shen, Hujun Bao, Zhaopeng Cui, Yinda Zhang, Guofeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.19316) - [pdf](https://arxiv.org/pdf/2606.19316)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, neural radiance field, radiance field, neural rendering, novel view synthesis, view synthesis, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NeuMesh++: Towards Versatile and Efficient Volumetric Editing with Disentangled Neural Mesh-based Implicit Field
- 作者：Chong Bao, Yuan Li, Bangbang Yang, Yujun Shen, Hujun Bao, Zhaopeng Cui, Yinda Zhang, Guofeng Zhang
- 出版日期：2026-06-17T17:39:21Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.19316

### 一句话总结
本文提出一种基于网格顶点的解耦神经隐式场表示（NeuMesh++），通过在网格顶点上编码几何、纹理和语义信息，实现多种高效的体积编辑功能。

### 研究问题
现有神经渲染方法在编辑方面功能有限（如仅支持刚性变换或类别特定编辑），缺乏支持几何、纹理语义等综合且高效编辑的统一表示。

### 核心思路/方法
1. **表示设计**：在网格顶点上解耦编码神经辐射场的几何、纹理和语义代码。
2. **关键技术**：
   - 局部空间参数化：提升渲染质量和训练稳定性。
   - 顶点可学习修改颜色：改善纹理编辑的真实感。
   - 空间感知优化策略：实现精确纹理编辑。
   - 语义辅助区域选择：简化隐式场编辑所需的人工标注。
3. **编辑功能**：支持网格引导的几何编辑、指定纹理编辑（纹理交换、填充和涂绘）以及语义引导的编辑。

### 主要贡献
1. 提出一种新的基于网格的表示，将几何、纹理和语义解耦编码在网格顶点上，支持多种编辑操作。
2. 开发了多种专用技术（局部空间参数化、可学习修改颜色、空间感知优化、语义辅助区域选择）以增强编辑效果与效率。
3. 在真实与合成数据集上展示了该方法在表示质量和编辑能力上的优越性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法面向神经隐式场编辑这一重要应用场景，提出了一种解耦表示并实现了多种高效编辑功能，且附带多技术改进。对于关注3D场景编辑、神经渲染应用的读者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recently neural implicit rendering techniques have evolved rapidly and demonstrated significant advantages in novel view synthesis and 3D scene reconstruction. However, existing neural rendering methods for editing purposes offer limited functionalities, e.g., rigid transformation and category-specific editing. In this paper, we present a novel mesh-based representation by encoding the neural radiance field with disentangled geometry, texture, and semantic codes on mesh vertices, which empowers a set of efficient and comprehensive editing functionalities, including mesh-guided geometry editing, designated texture editing with texture swapping, filling and painting operations, and semantic-guided editing. To this end, we develop several techniques including a novel local space parameterization to enhance rendering quality and training stability, a learnable modification color on vertex to improve the fidelity of texture editing, a spatial-aware optimization strategy to realize precise texture editing, and a semantic-aided region selection to ease the laborious annotation of implicit field editing. Extensive experiments and editing examples on both real and synthetic datasets demonstrate the superiority of our method on representation quality and editing ability. Project page: https://zju3dv.github.io/neumeshplusplus/

</details>

#### 2026-06-17 - FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity

**Authors:** Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer
**Links:** [abs](https://arxiv.org/abs/2606.19019) - [pdf](https://arxiv.org/pdf/2606.19019)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity
- 作者：Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer
- 出版日期：2026-06-17T12:42:09Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.19019

### 一句话总结
FlowObject提出了一种无训练引导框架，通过双空间引导策略和3D高斯泼溅（3DGS）优化，融合流匹配模型的生成先验与观测一致性，实现了从稀疏视角图像到完整3D对象的高质量重建。

### 研究问题
如何从少量随意拍摄的图像中恢复完整的3D物体表示，同时平衡生成先验（用于补全未见区域）与重建保真度（保持与真实观测一致）之间的矛盾。

### 核心思路/方法
1. 将稀疏视角3D重建重新定义为无训练的引导逆问题，通过双空间引导策略控制流匹配模型的常微分方程（ODE）轨迹。
2. 利用生成先验补全被遮挡或未观测的区域，同时强制输出与真实观测严格一致。
3. 引入3DGS精炼阶段，减少生成输出的“合成感”，弥合生成结果与逼真重建之间的差距。

### 主要贡献
- 提出首个将稀疏视角重建作为训练-free引导逆问题的框架，有效融合生成先验与观测一致性。
- 引入双空间引导策略，在几何完整性和外观保真度之间取得平衡。
- 在合成和真实数据集上，显著优于现有生成模型和优化方法，尤其在严重遮挡场景下表现更优。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：针对稀疏视角3D重建的核心难题（生成先验与观测一致性冲突）提出了新颖的引导框架，方法简洁且性能显著优于现有方法，对计算机视觉领域的3D表征与渲染方向具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering complete 3D representations of objects from few casual image captures remains a significant challenge. Recent 3D generative models, particularly those based on Flow-Matching (FM), can synthesize high-quality textured assets; however, they often suffer from ''synthetic bias'' where learned priors override observational evidence, alongside a lack of alignment with the observed instance. Conversely, optimization-based methods like 3D Gaussian Splatting (3DGS) provide high fidelity on visible surfaces but fail to reason about unobserved geometry. In this paper, we present FlowObject, a framework that reformulates sparse-view 3D reconstruction as a training-free, guided inverse problem. Our approach applies a dual-space guidance strategy to steer the Ordinary Differential Equation (ODE) trajectory of a flow-matching model, enabling the completion of unseen regions through learned generative priors while enforcing strict consistency with real-world observations. By integrating a 3DGS refinement stage, FlowObject further bridges the gap between ''synthetic-looking'' generative outputs and photorealistic reconstructions. Comprehensive benchmarks on synthetic and real-world datasets demonstrate that current state-of-the-art methods often struggle to achieve geometric completeness and observational consistency simultaneously, especially under severe occlusions. In contrast, our method significantly outperforms state-of-the-art generative models and optimization-based frameworks in both geometric completeness and view-dependent appearance fidelity.

</details>

#### 2026-06-17 - EDoF-NeRF: extended depth-of-field neural radiance fields using a coded aperture camera

**Authors:** Yoshiyuki Shirasaki, Ryoichi Horisaki
**Links:** [abs](https://arxiv.org/abs/2606.18826) - [pdf](https://arxiv.org/pdf/2606.18826)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EDoF-NeRF: extended depth-of-field neural radiance fields using a coded aperture camera
- 作者：Yoshiyuki Shirasaki, Ryoichi Horisaki
- 出版日期：2026-06-17
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.18826

### 一句话总结
本文提出EDoF-NeRF方法，通过在相机瞳孔处放置编码光圈来扩展景深，从而构建高保真的神经辐射场。

### 研究问题
传统相机在采集NeRF所需的多视角图像时，存在景深与光通量之间的固有矛盾，导致NeRF渲染的视图在景深外区域保真度下降。

### 核心思路/方法
1. 在相机瞳孔处引入编码光圈，以在散焦条件下保留空间频率成分。
2. 设计一种将编码光圈纳入NeRF的相机模型，使编码图像可直接输入网络。
3. 通过该模型，网络能够从编码图像中学习并生成具有扩展景深的新视图。

### 主要贡献
1. 提出EDoF-NeRF，首次将编码光圈与NeRF结合以扩展景深。
2. 开发了兼容编码图像的相机模型，直接处理编码图像输入。
3. 通过仿真和实验验证，EDoF-NeRF在扩展景深的新视图渲染上优于传统光圈相机。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。
理由：该方法从硬件（编码光圈）和模型（相机模型）两方面优化NeRF的景深问题，具有一定新颖性；但摘要未提供具体性能指标或典型场景对比，需要查看全文评估实际效果与复杂度。

</details>

<details>
<summary>Abstract</summary>

We propose a method for extending the depth-of-field (DoF) to construct high-fidelity neural radiance fields (NeRF) -- an emerging technique for rendering photorealistic novel views from a dataset of images captured at different viewpoints, based on implicit neural representations. The trade-off between DoF and light quantity is inherent not only in conventional cameras but also in NeRF, since the datasets used by NeRF are captured by these cameras. To address this issue, we introduce a coded aperture placed at the camera pupil, preserving spatial frequency components under defocused conditions. We develop a camera model incorporating coded apertures into NeRF, allowing direct input of coded images and enabling the generation of novel views with an extended DoF. We validate the proposed method, termed extended DoF-NeRF (EDoF-NeRF), through simulations and experiments, demonstrating its superior performance compared to conventional aperture cameras.

</details>

#### 2026-06-16 - AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement

**Authors:** Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.17998) - [pdf](https://arxiv.org/pdf/2606.17998)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement
- 作者：Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-16
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.17998

### 一句话总结
AIGS-Net是一种超轻量级网络，通过输入自适应的2D高斯点照明场模型，仅用约40个可学习参数即可实现快速、高质量的低光照图像增强。

### 研究问题
现有低光照图像增强方法在光照场建模的表达能力与计算复杂度之间难以平衡，导致细节恢复和色彩保真度不足。

### 核心思路/方法
1. 构建输入自适应的2D高斯点照明场，其高斯基函数的不透明度由输入图像相对亮度统计动态调节，并通过有序Alpha合成渲染空间变化的照明补偿。
2. 引入零参数非线性多尺度上下文编码模块，无需额外卷积权重即可提取低频结构和局部对比度线索。
3. 集成噪声掩膜估计、锁定单通道Gamma映射、跨通道一致性正则化及目标颜色对齐约束，抑制噪声放大和传感器导致的色彩偏差。

### 主要贡献
1. 提出超轻量级AIGS-Net架构，仅需约40个可学习参数。
2. 设计了输入自适应的2D高斯点照明场，实现高效光照建模与补偿。
3. 在LOL和LSRW基准上实现细节恢复与色彩保真度的提升，同时保持极快的推理速度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作专注于低光照图像增强领域的实际效率问题，方法新颖（结合2D高斯点与极轻量设计），且实验结果明确。但摘要未提供与其他方法的定量对比细节或开源信息，其实际可复现性和规模效应尚需进一步评估。若对超轻量级网络或照明场建模感兴趣，则值得一读。

</details>

<details>
<summary>Abstract</summary>

Existing low-light image enhancement methods often face a bottleneck between the representation capacity of illumination-field modeling and computational complexity. To address this issue, this paper proposes an Adaptive Illumination Gaussian Splatting Network (AIGS-Net), an ultra-lightweight architecture for fast low-light enhancement. Unlike conventional static priors, AIGS-Net constructs an input-adaptive 2D Gaussian Splatting illumination field. The opacity of Gaussian basis functions is dynamically modulated by relative luminance statistics of the input image, and spatially varying illumination compensation is rendered through ordered alpha compositing. To guide adaptive illumination compensation efficiently, a zero-parameter nonlinear multiscale contextual encoding module is introduced to extract low-frequency structures and local contrast cues without additional convolutional weights. To suppress noise amplification and sensor-induced color bias, AIGS-Net integrates noise-mask estimation, locked single-channel Gamma mapping, cross-channel consistency regularization, and target color-alignment constraints. Experiments on LOL and LSRW benchmarks show that AIGS-Net improves detail recovery and color fidelity while requiring only approximately 40 learnable parameters, achieving an effective trade-off between enhancement quality and extreme inference efficiency.

</details>

#### 2026-06-16 - Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement

**Authors:** Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, Ying Fang, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.17985) - [pdf](https://arxiv.org/pdf/2606.17985)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement
- 作者：Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, Ying Fang, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-16T14:37:08Z
- 分类：Neural Scene Representations & Rendering
- 链接：论文摘要 https://arxiv.org/abs/2606.17985 | PDF https://arxiv.org/pdf/2606.17985

### 一句话总结
本文提出GLFS，一种将高斯光场飞溅的连续物理光照模型集成到Vision Transformer中，用于无监督低光图像增强的方法。

### 研究问题
现有无监督低光图像增强方法在复杂非均匀光照下容易出现局部曝光失衡和颜色失真，且大多数Vision Transformer缺乏显式建模光照退化物理先验的机制。

### 核心思路/方法
1. 将场景光照表示为各向异性高斯基函数的叠加，实现连续物理光照建模。
2. 在自注意力机制中引入物理引导偏差，自适应推断空间增益场，以实现复杂光照下的准确均匀恢复。
3. 开发颜色矢量角度损失和亮度-边缘损失，分别用于减少增强过程中的色偏和结构退化，保持色调一致性并提高局部细节的结构保真度。

### 主要贡献
1. 提出了GLFS，一种基于高斯光场飞溅的Vision Transformer，将连续物理光照建模引入Transformer架构。
2. 通过物理指导的偏差机制，使自注意力能够自适应地推断空间增益场，改善非均匀光照下的恢复效果。
3. 设计了颜色矢量角度损失和亮度-边缘损失，有效抑制色偏并提升细节结构保真度。
4. 消融研究和定量评估表明，GLFS在光照校正和细节保留方面具有明显优势，达到当前最优性能，并为低光图像增强提供了新的表示范式。

### 局限性
摘要未提供足够信息（例如模型计算复杂度、对极端暗光场景的鲁棒性、是否依赖特定数据集或超参数设置等）。

### 阅读优先级
**高**。
理由：该工作针对低光图像增强中的核心痛点（非均匀光照、颜色失真）提出了物理先验驱动的Transformer结构，并设计了专用损失函数。论文表示达到SOTA性能并提供新表示范式，属于方法创新度较高的文章，对相关领域研究者有较强借鉴意义。

</details>

<details>
<summary>Abstract</summary>

Existing unsupervised low-light image enhancement methods often encounter local exposure imbalance and color distortion under complex non-uniform illumination. In addition, most Vision Transformers lack an explicit mechanism for modeling the physical priors of illumination degradation. To address these limitations, we propose GLFS, a Gaussian light field splatting-based Vision Transformer that integrates continuous physical illumination modeling from Gaussian splatting into the Transformer architecture. In GLFS, scene illumination is represented by a superposition of anisotropic Gaussian basis functions. Physics-guided biases are introduced into self-attention to adaptively infer a spatial gain field, enabling accurate and uniform restoration under complex illumination. To reduce color bias and structural degradation during enhancement, a color-vector angular loss and a luminance-edge loss are further developed. These losses enforce hue consistency and improve the structural fidelity of local details. Extensive ablation studies and quantitative evaluations show that GLFS provides clear advantages in illumination correction and detail preservation. It achieves state-of-the-art performance and offers a new representation paradigm for low-light image enhancement.

</details>

#### 2026-06-16 - GSPan: A Continuous Gaussian Primitive Representation for Arbitrary-Scale Pansharpening

**Authors:** Fangyi Li, Xiaoyuan Yang, Yixiao Li, Zongyang Sui, Kangqing Shen, Gemine Vivone
**Links:** [abs](https://arxiv.org/abs/2606.17722) - [pdf](https://arxiv.org/pdf/2606.17722)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, Gaussian primitive, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GSPan: A Continuous Gaussian Primitive Representation for Arbitrary-Scale Pansharpening
- 作者：Fangyi Li, Xiaoyuan Yang, Yixiao Li, Zongyang Sui, Kangqing Shen, Gemine Vivone
- 出版日期：2026-06-16T09:36:36Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.17722

### 一句话总结
GSPan 提出用连续二维高斯基元表示残差细节，实现任意尺度的全色锐化融合。

### 研究问题
现有全色锐化深度学习方法局限于固定网格预测，无法灵活适应不同缩放比例。

### 核心思路/方法
- 将每个波段上的残差细节建模为连续且可学习的二维高斯基元。
- 设计双流分层交互（DSHI）架构和空间-光谱交互注意力（SSIA）模块，从PAN和MS观测中估计这些基元。
- 将预测的基元渲染为残差细节场，注入上采样后的MS图像。
- 提出尺度解耦非对称推理（SDAI）策略：先以较低分辨率估计基元，再在目标分辨率下渲染融合图像。

### 主要贡献
- 首次将二维高斯泼溅引入全色锐化，实现任意缩放网格上的连续融合。
- 提出双流分层交互与空间-光谱交互注意力机制，用于从互补数据中估计高斯基元。
- 设计尺度解耦推理策略，可降低大场景推理的计算成本。
- 在QuickBird、GaoFen-2、WorldView-3及WorldView-3-4K数据集上实现最先进的融合性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。该工作创新性地用连续表示替代固定网格预测，解决了全色锐化中的尺度适应问题，并支持高效推理，方法论新颖且实验基准覆盖多个卫星数据集。

</details>

<details>
<summary>Abstract</summary>

Pansharpening aims to generate high-resolution multispectral (HRMS) images by fusing low-resolution multispectral (LRMS) and panchromatic (PAN) observations. Most existing deep learning methods treat pansharpening as fixed-grid prediction, which limits scale adaptation. To address this, we propose GSPan, a framework that introduces 2D Gaussian Splatting (GS) into pansharpening. Instead of directly predicting pixels, GSPan represents band-wise residual details as continuous and learnable 2D Gaussian primitives. We design a Dual-Stream Hierarchical Interaction (DSHI) architecture with a Spatial-Spectral Interactive Attention (SSIA) module to estimate these primitives from complementary PAN and MS observations. The predicted primitives are rendered as a residual detail field and injected into the upsampled MS image. This continuous representation allows GSPan to render fused images on arbitrary target sampling grids without scale-specific retraining. It further enables a Scale-Decoupled Asymmetric Inference (SDAI) strategy, which estimates primitives at a reduced resolution and renders the fused image at the target resolution for efficient large-scene pansharpening. Experiments on QuickBird, GaoFen-2, WorldView-3, and WorldView-3-4K datasets show that GSPan delivers state-of-the-art fusion performance. Moreover, SDAI markedly accelerates inference, achieving a favorable trade-off between computational efficiency and fusion quality. Our results demonstrate the potential of continuous Gaussian residual representations as a flexible and scale-decoupled alternative to fixed-grid prediction.

</details>

#### 2026-06-16 - GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments

**Authors:** Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.17520) - [pdf](https://arxiv.org/pdf/2606.17520)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GASE: 基于高斯泼溅的自动化系统用于重建具身仿真环境  
- 作者：Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang  
- 出版日期：2026-06-16T05:00:42Z  
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）  
- 链接：摘要 https://arxiv.org/abs/2606.17520 ；PDF https://arxiv.org/pdf/2606.17520  

### 一句话总结  
GASE 是一个基于高斯泼溅的高度自动化系统，利用全景相机阵列快速扫描环境，并采用相机位姿引导的前景提取与高质量修复策略，独立重建前景物体与静态背景，以实现逼真的仿真场景构建，有效缩小 sim-to-real 差距。

### 研究问题  
如何高效、自动化地重建高保真仿真场景，以减小模拟环境与真实环境之间的 sim-to-real 差距，用于机器人具身智能体的策略训练。

### 核心思路/方法  
1. **高效数据采集**：采用全景相机阵列的多视角视频流，实现快速环境扫描。  
2. **前景-背景分离与修复**：引入基于相机位姿的策略，在2D域内鲁棒地跨帧提取前景物体；对背景进行高保真场景修复。  
3. **独立重建与导入**：前景物体与静态背景分别使用3D高斯泼溅等方法独立重建，并无缝导入物理仿真器用于策略训练。

### 主要贡献  
- 提出了一个高度自动化的仿真场景构建系统 GASE，显著简化了现有工作流中的数据采集与前景提取步骤。  
- 在分割精度上超越现有3D高斯方法超过10%，同时实现了最先进的修复质量。  
- 在真实机器人操作与导航任务中，与纯真实世界数据训练的策略相比，性能差距维持在10%以内，验证了系统在弥合 sim-to-real 差距上的有效性。  
- 将开源代码以促进可复现性。

### 局限性  
摘要未提供足够信息。

### 阅读优先级  
**高**  
**理由**：该系统在分割精度和修复质量上取得显著提升（分别超过10%和最先进水平），且在真实机器人部署中保持了较小的性能差距（<10%），直接解决了仿真环境构建的关键瓶颈。对于从事机器人学习、具身智能或神经渲染的研究者具有高参考价值。

</details>

<details>
<summary>Abstract</summary>

Training embodied agents in the real world requires skilled operators and expensive hardware. Simulation environments offer a compelling alternative by enabling large-scale, cost-effective data augmentation. Consequently, rapidly constructing high-fidelity simulation scenes with a minimal sim-to-real gap has become a critical objective in robot learning. While reconstruction-based methods provide superior visual quality, current workflows are hindered by inefficient data acquisition and subpar foreground object extraction. We thus propose GASE, a highly automated system for simulation scene construction. GASE leverages multi-view video streams from panoramic camera arrays to enable rapid environment scanning. To ensure high-quality asset generation, our pipeline introduces a camera-pose-based strategy that robustly extracts objects across frames in the 2D domain, followed by high-fidelity scene inpainting. Foreground objects and the static background are then reconstructed independently and seamlessly imported into physics simulators for policy training. Extensive experiments demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation accuracy by over 10\% while achieving state-of-the-art inpainting quality. Furthermore, real-robot deployments across manipulation and navigation tasks maintains a performance gap of less than 10\% compared to policies trained purely on real-world data. These results confirm that GASE provides an efficient and highly effective solution for bridging the sim-to-real gap. Code will be released.

</details>

#### 2026-06-16 - Edit3DGS: Unified Framework for Dynamic Head Editing via 2D Instruction-Guided Diffusion and 3D Gaussian Splatting

**Authors:** Duy-Dat Tran, Trung-Nghia Le
**Links:** [abs](https://arxiv.org/abs/2606.17432) - [pdf](https://arxiv.org/pdf/2606.17432)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic 3D, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Edit3DGS: Unified Framework for Dynamic Head Editing via 2D Instruction-Guided Diffusion and 3D Gaussian Splatting
- 作者：Duy-Dat Tran, Trung-Nghia Le
- 出版日期：2026-06-16
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.17432

### 一句话总结
Edit3DGS是一个将2D指令引导扩散模型与3D高斯泼溅技术结合的统一框架，用于对动态三维头部进行语义可控、时序连贯的编辑。

### 研究问题
如何实现动态3D头部的高保真编辑，使其既能通过文本指令进行语义控制，又能保持身份、运动动态和时间一致性，同时避免帧间伪影。

### 核心思路/方法
1. 利用文本条件扩散模型对视频中可编辑面部区域进行掩码和修改，支持表情变换、属性修改和外观精修等精细操作。
2. 将编辑后的帧通过3D高斯泼溅聚合为连贯、高保真的动态头像。
3. 引入多视角批量编辑和轻量级修复策略，以恢复跨时间步长丢失的表情，增强时空一致性。

### 主要贡献
- 提出一个统一框架，整合了2D指令驱动的语义控制与3D高斯泼溅的逼真重建。
- 实现了无伪影、时序平滑的动态头部编辑，支持多种编辑操作（表情、属性、外观）。
- 框架可应用于虚拟化身、沉浸式通信、电影制作和交互媒体等场景。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文提出的方法在动态3D头部编辑领域兼具语义可控性与时序一致性，且应用场景广泛；方法整合了当前热门的扩散模型与3D高斯泼溅技术，技术新颖性高。

</details>

<details>
<summary>Abstract</summary>

We present Edit3DGS, a unified framework for dynamic 3D head editing that integrates 2D instruction-guided diffusion with 3D Gaussian splatting. Unlike prior approaches that separately address frame-based edits or static 3D reconstruction, our method couples semantic controllability in the image domain with photorealistic, temporally consistent 3D representations. Given an input video, editable facial regions are masked and modified using a text-conditioned diffusion model to support fine-grained operations such as expression transformation, attribute modification, and appearance refinement. The edited frames are then aggregated through 3D Gaussian splatting to produce a coherent, high-fidelity avatar that preserves both identity and motion dynamics. To enforce consistency, Edit3DGS incorporates multi-view batch editing and lightweight inpainting strategies that recover lost expressions across timesteps. Experimental results demonstrate that our framework enables controllable, artifact-free head editing with smooth temporal transitions, offering practical applications in virtual avatars, immersive communication, film production, and interactive media.

</details>

#### 2026-06-16 - TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations

**Authors:** Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan
**Links:** [abs](https://arxiv.org/abs/2606.17386) - [pdf](https://arxiv.org/pdf/2606.17386)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations
- 作者：Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan
- 出版日期：2026-06-16
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.17386；PDF: https://arxiv.org/pdf/2606.17386

### 一句话总结
本文提出TerraTransfer方法，通过在向量化模拟器中自博弈训练策略，再将其与预训练视觉骨干网络对齐，实现了无需专家示范的端到端驾驶。

### 研究问题
如何在不依赖昂贵的人工标注和专家演示数据的情况下，高效训练端到端自动驾驶策略，并降低训练成本（包括数据收集和闭环强化学习的计算开销）。

### 核心思路/方法
将“学习驾驶”与“学习视觉”解耦：1）在向量化模拟器中进行快速自博弈（self-play）训练，生成包含碰撞、近碰撞和恢复等丰富状态分布的驾驶策略；2）通过动作KL散度和批量关系低秩结构损失，将自博弈策略的潜在空间与预训练视觉骨干网络对齐，仅需配对（图像，场景状态）数据，无需专家轨迹监督。

### 主要贡献
1. 提出利用向量化模拟器的低成本自博弈替代昂贵实车数据采集和闭环图像RL训练。
2. 设计了一种对齐机制，使自博弈学习的驾驶策略能迁移到视觉输入上，无需专家示范。
3. 在基于3D高斯溅射的逼真闭环场景中，端到端策略获得了匹配或超越现有方法的性能。

### 局限性
摘要未提供足够信息，例如：在真实世界或复杂动态场景下的泛化能力、对齐过程的收敛性保证、以及未与大规模实际路测结果的对比。

### 阅读优先级
中。理由：该方法在降低端到端自动驾驶训练成本（无需专家演示）方面提出了新颖的解耦思路，对关注训练效率和数据成本的读者有参考价值；但摘要未提供充分的实验对比和泛化性分析，需进一步阅读全文评估实用性。

</details>

<details>
<summary>Abstract</summary>

End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all stages: collecting and labeling millions of driving frames is costly, and closed-loop RL on images is bottlenecked by the per-step cost of photorealistic rendering plus a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: millions of rollout steps per second, and a state distribution naturally rich in collisions, near-misses, and recoveries that no driving log contains. Our approach exploits this asymmetry by decoupling learning to drive from learning to see. We pretrain a single policy by self-play, then align its latent space with a pretrained vision backbone, through the action KL divergence and a batch-relational low-rank structural loss. The action target comes from the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. On photorealistic 3D Gaussian splatting closed-loop scenarios, the resulting end-to-end policy matches or exceeds prior end-to-end methods.

</details>

#### 2026-06-15 - BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering

**Authors:** Yi-Ruei Liu, Jie-Ying Lee, Zheng-Hui Huang, Yu-Lun Liu, Chih-Hao Lin
**Links:** [abs](https://arxiv.org/abs/2606.17049) - [pdf](https://arxiv.org/pdf/2606.17049)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** inverse rendering, relighting, rendering, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering
- 作者：Yi-Ruei Liu, Jie-Ying Lee, Zheng-Hui Huang, Yu-Lun Liu, Chih-Hao Lin
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering (主)；Embodied / Robotics / AR Applications (次)
- 链接：摘要页 [https://arxiv.org/abs/2606.17049](https://arxiv.org/abs/2606.17049) | PDF [https://arxiv.org/pdf/2606.17049](https://arxiv.org/pdf/2606.17049)

### 一句话总结
BRDFusion 将物理渲染（PBR）与生成式模型融合，实现高质量、可控的城市场景逆向渲染与正向渲染，支持重光照、夜间模拟和动态物体编辑。

### 研究问题
如何解决物理渲染方法在城市场景逆向渲染中存在的重建与渲染伪影，同时克服生成模型一致性和可控性不足的问题，以实现高质量且可控的视频生成。

### 核心思路/方法
提出一个统一框架，结合两种互补模型：
1. **逆向渲染阶段**：使用物理建模恢复显式、一致的场景属性（如材质、光照），并利用生成先验缓解优化歧义。
2. **正向渲染阶段**：物理模型从场景配置提供可控渲染，生成模型负责去噪和修复伪影。二者协同工作，实现高保真视频输出。

### 主要贡献
- 将物理渲染与生成模型有机结合，取长补短。
- 在真实与合成场景中获得了优于基线方法的视频质量。
- 支持新颖视角重光照、夜间模拟、动态物体插入/编辑等高级功能。

### 局限性
摘要未提供关于方法计算开销、对训练数据规模要求、失败案例（如极端光照或复杂几何）等局限性信息。

### 阅读优先级
**中**
理由：该工作解决了城市场景逆向渲染中的实用问题，方法巧妙结合物理与生成范式，但摘要未展示定量实验结果或具体实施细节，且2026年的论文相对较新，需谨慎评估其可比性与可复现性。如果对可编辑渲染或城市仿真感兴趣，则值得深入原文阅读。

</details>

<details>
<summary>Abstract</summary>

Inverse rendering of urban scenes from captured videos enables numerous applications, including content creation and autonomous driving simulation. Physically-based rendering methods follow and control lighting physics, but suffer from reconstruction and rendering artifacts. While generative models produce realistic videos, they offer limited consistency and controllability. We present BRDFusion, a unified framework that combines two complementary models for inverse and forward rendering. Specifically, BRDFusion recovers explicit, consistent scene properties with physical modeling and alleviates optimization ambiguity with generative priors. During forward rendering, the physical model provides controllable rendering from the scene configuration, and the generative model denoises and fixes artifacts. Therefore, our method produces high-quality videos while allowing precise control, outperforming baselines in real and synthetic scenes. Moreover, BRDFusion supports novel-view relighting, night simulation, and dynamic object insertion/editing. Project page: https://shigon255.github.io/brdfusion-page/

</details>

#### 2026-06-15 - Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence

**Authors:** Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu
**Links:** [abs](https://arxiv.org/abs/2606.16566) - [pdf](https://arxiv.org/pdf/2606.16566)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence
- 作者：Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2606.16566; PDF: https://arxiv.org/pdf/2606.16566

### 一句话总结
Local-GS 通过针对SIMT执行边界的瓦片级warp一致性优化，显著加速了3D高斯泼溅的渲染过程。

### 研究问题
如何解决3D高斯泼溅中因高斯原语不规则空间分布导致的GPU利用率低下、warp发散和冗余计算问题，以提升渲染效率。

### 核心思路/方法
提出一种warp一致的渲染范式，将高斯原语组织为与SIMT执行边界对齐的形式，而非依赖场景几何。具体包括三个warp一致的阶段：
1. **提升阶段（hoisting stage）**：在瓦片级别预计算共享参数。
2. **剔除阶段（culling stage）**：丢弃无贡献的warp。
3. **混合阶段（blending stage）**：将逐像素分支替换为统一指令流。

### 主要贡献
- 提出Local-GS，一种通过瓦片级warp一致性加速3DGS的即插即用优化方法。
- 在多个数据集的基准测试中，在不牺牲质量的前提下提升了效率。
- 在所有测试基线上均带来额外性能增益，例如在Deep Blending场景上实现7.76倍加速。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法针对3DGS渲染效率这一具体工程优化问题，提出创新性的warp一致性策略，对于从事神经渲染或GPU优化的研究者具有参考价值，但未涉及算法理论突破，可结合具体场景决定是否深入阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has significantly advanced real-time novel view synthesis by representing scenes as dense collections of anisotropic 3D Gaussian primitives. However, the irregular spatial distribution of Gaussians often leads to poor GPU utilization, as warp divergence and redundant computation degrade rendering performance. To address this, we present Local-GS, a warp-coherent rendering paradigm that, organizes Gaussian primitives with respect to SIMT (Single Instruction, Multiple Threads) execution boundaries rather than scene geometry. Specifically, we propose three warp-coherent stages: a hoisting stage that precomputes shared parameters at tile level, a culling stage that discards warps with no contribution, and a blending stage that replaces per-pixel branching with a uniform instruction stream. Across extensive benchmarks on multiple datasets, Local-GS improves efficiency without compromising quality. As a plug-and-play optimization, it provides additional performance gains to all tested baselines, culminating in a $7.76\times$ speedup on Deep Blending scenes.

</details>

#### 2026-06-15 - RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos

**Authors:** Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li
**Links:** [abs](https://arxiv.org/abs/2606.16278) - [pdf](https://arxiv.org/pdf/2606.16278)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos
- 作者：Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2606.16278

### 一句话总结
提出RealityBridge框架，用于修复和增强可编辑3D高斯泼溅（3DGS）仿真驾驶视频，弥合其与真实世界视频之间的Sim-to-Real差距。

### 研究问题
如何修复可编辑3DGS驾驶仿真视频中存在的渲染伪影、前景资产退化、光照不一致和时序闪烁等Sim-to-Real差距，同时保持结构完整性和资产一致性。

### 核心思路/方法
1. 采用多模态控制输入（渲染视频、前景掩码、边缘图、语义掩码）作为条件。
2. 引入轻量级GateNet模块，实现自适应条件分配到骨干网络各层。
3. 构建针对性训练数据，并采用自回归长视频训练策略。
4. 使用奖励引导的后训练（reward-guided post-training）来提升修复质量、时间稳定性和幻觉抑制。

### 主要贡献
1. 提出首个结构保持且资产感知的Sim-to-Real框架，专用于编辑后的3DGS驾驶视频。
2. 设计多模态控制与自适应条件分配机制（GateNet），有效处理多种伪影和光照问题。
3. 通过自回归长视频训练和奖励引导后训练，显著提升时序一致性和视觉真实性。
4. 在内部和公开驾驶数据集上的实验表明，该方法在伪影去除、光照和谐化及长序列时序一致性上优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。
理由：该工作针对自动驾驶安全关键的稀有场景仿真问题，提出了结合3DGS编辑与视频修复的新框架，方法设计具有创新性（多模态控制+自回归训练+奖励引导），涉及当前热门的3DGS与Sim-to-Real交叉领域，且实验结果明确优于现有方法，对自动驾驶和神经渲染方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Long-tail hazardous scenarios are essential for safety-oriented autonomous driving, yet they are difficult to collect and reproduce at scale. Editable 3D Gaussian Splatting (3DGS) simulation offers a promising alternative by reconstructing real driving scenes and supporting controllable scene editing. However, edited 3DGS-rendered videos still suffer from a significant Sim-to-Real gap, including rendering artifacts, degraded foreground assets, inconsistent illumination, and temporal flickering. Existing restoration and video generation methods are insufficient for this task, as they often fail to jointly repair 3DGS-specific artifacts, improve visual realism, and ensure temporal consistency. To fill this gap, we propose RealityBridge, a structure-preserving and asset-aware Sim-to-Real framework for edited 3DGS driving videos. RealityBridge uses multimodal controls, including rendered videos, foreground masks, edge maps, and semantic masks, together with a lightweight GateNet for adaptive condition allocation across backbone layers. We further construct targeted training data and introduce autoregressive long-video training with reward-guided post-training to improve restoration quality, temporal stability, and hallucination suppression. Extensive experiments on internal and public driving datasets show that RealityBridge outperforms existing methods in artifact removal, illumination harmonization, and long-sequence temporal consistency.

</details>

#### 2026-06-15 - PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation

**Authors:** Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou
**Links:** [abs](https://arxiv.org/abs/2606.16232) - [pdf](https://arxiv.org/pdf/2606.16232)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation  
- 作者：Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou  
- 出版日期：2026-06-15  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2606.16232  

### 一句话总结  
该工作提出PolyMerge方法，将高保真3D高斯泼溅场景模型转换为轻量级凸多面体覆盖表示，在资源受限的无人机上实现可证明安全的实时避障导航。

### 研究问题  
如何压缩大容量、高计算量的3DGS场景模型，使其能在计算资源严重受限的嵌入式平台上实时生成安全轨迹，同时保证碰撞避免的数学可证性。

### 核心思路/方法  
- 将原始3DGS模型中的所有障碍物用一组凸多面体的并集进行可证明的过近似覆盖（即每个多面体完全包含障碍物，且并集不遗漏任何障碍）。  
- 通过调节凸多面体的数量来权衡保守程度（覆盖精度）与计算代价。  
- 与控制障碍函数（CBF）集成，以该多面体覆盖作为约束条件，规划出无碰撞路径。

### 主要贡献  
1. 提出PolyMerge：一种将3DGS场景压缩为可证明覆盖所有障碍的凸多面体表示的方法。  
2. 该方法能灵活控制多面体数量，在安全保守性与计算需求之间做权衡。  
3. 在Crazyflie微型无人机上实现实时轨迹规划与跟踪，在严苛机载计算约束下保证碰撞安全，且速度快于基线方法。  
4. 提供了模拟和硬件实验验证，并公开代码与演示视频。

### 局限性  
摘要未提供足够信息，无法判断具体局限性（如多面体覆盖的保守性程度对路径可行性的影响、是否依赖特定场景结构、3DGS模型精度损失等）。

### 阅读优先级  
高  
理由：该工作直接解决了3DGS在高动态、资源受限机器人（如微型无人机）上应用的瓶颈问题，结合了可证明安全（CBF）与实时性，与神经场景表示在机器人导航中的落地紧密相关，具有明显的实际应用与理论价值。

</details>

<details>
<summary>Abstract</summary>

Obstacle avoidance is essential for safe navigation and motion planning. Recent radiance field reconstruction methods enable object detection and modeling with high fidelity, but remain too memory- and compute-intensive for on-board perception-based path planning. To address these limitations, we propose PolyMerge to convert a large, photorealistic 3D Gaussian Splatting (3DGS) model of a scene into a lightweight representation of convex polytopes whose union provably over-approximates all obstacles in the original 3DGS model. PolyMerge tunes the polytope count to trade off conservativeness and compute cost, and integrates with control barrier functions (CBFs) to plan collision-free paths. We showcase PolyMerge in simulation and hardware experiments on a Crazyflie drone, which uses PolyMerge to compute and follow safe trajectories in real time under severe onboard compute constraints, outperforming baselines in speed while guaranteeing safety. For our code and videos, visit https://athlon76.github.io/PolyMerge-website/.

</details>

#### 2026-06-15 - Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing

**Authors:** Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Kunyang Huang, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.16168) - [pdf](https://arxiv.org/pdf/2606.16168)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing
- 作者：Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Kunyang Huang, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.16168；PDF：https://arxiv.org/pdf/2606.16168

### 一句话总结
本文提出了一种频率感知的隐式高斯泼溅网络（Fi-Gaussian），通过频域解耦和物理散射重归一化机制，提升单张图像去雾的细节恢复效果。

### 研究问题
单张图像去雾任务中，高频细节丢失以及准确的物理散射建模困难。

### 核心思路/方法
1. 采用隐式高斯泼溅（Implicit Gaussian Splatting）在2D特征空间中连续表示清晰图像的潜在分布，替代显式3D点云渲染。
2. 设计频率感知隐式高斯泼溅模块，在频域中解耦低频结构信息和高频纹理信息，并使用复数值权重进行自适应高斯聚合，以恢复精细细节。
3. 引入物理驱动的散射重归一化机制，在隐式高斯先验指导下估计透射图和大气光。

### 主要贡献
1. 提出Fi-Gaussian网络，首次将隐式高斯泼溅应用于单张图像去雾，验证了其在低级视觉任务中的有效性。
2. 通过频率感知解耦和复数值高斯聚合，显著提升高频纹理的恢复质量。
3. 结合物理散射重归一化机制，在多个基准数据集上取得最优定量性能，并生成视觉上更优的去雾结果。

### 局限性
摘要未提供足够信息，例如模型的计算复杂度、对极端雾霾场景的鲁棒性、不同数据集上的具体性能差异、与现有方法的详细对比数值等。

### 阅读优先级
中。理由：该方法在去雾任务中引入了频域感知与隐式高斯泼溅的新颖结合，对关注低级视觉和神经渲染的读者有参考价值，但内容相对专精且发表于2026年，若非直接相关领域，优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Single image dehazing continues to be hindered by the loss of high-frequency details and the difficulty of accurate physical scattering modeling. To address these issues, we propose Fi-Gaussian, a frequency-aware implicit Gaussian splatting network for single image dehazing. Unlike explicit rendering methods that rely on 3D point clouds, our method employs implicit Gaussian splatting to adaptively model the underlying distribution of clear images as a continuous representation in 2D feature space. The core of the network is a frequency-aware implicit Gaussian splatting module, which decouples low-frequency structural information and high-frequency texture information in the frequency domain and then performs adaptive Gaussian aggregation with complex-valued weights to recover fine details. In addition, a physics-driven scattering renormalization mechanism is introduced to estimate the transmission map and atmospheric light under the guidance of implicit Gaussian priors. Extensive experiments on multiple benchmark datasets demonstrate that Fi-Gaussian achieves state-of-the-art quantitative performance and produces visually superior dehazed results, validating the effectiveness of implicit Gaussian splatting for low-level vision tasks.

</details>

#### 2026-06-15 - Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation

**Authors:** Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.16163) - [pdf](https://arxiv.org/pdf/2606.16163)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation
- 作者：Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-15
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：[摘要](https://arxiv.org/abs/2606.16163) | [PDF](https://arxiv.org/pdf/2606.16163)

### 一句话总结
本文提出首个将2D高斯泼溅（2DGS）引入图像去雾领域的零样本框架Dehaze-GaussianImage，通过可演化的各向异性高斯场建模雾图，并以无监督方式实现物理可解释的高效去雾。

### 研究问题
现有单图像去雾方法在像素级优化中存在计算冗余，且隐式神经网络缺乏物理可解释性，导致表示效率与重建保真度难以平衡。本文旨在突破传统像素网格处理范式，提升去雾的表示效率和重建质量。

### 核心思路/方法
- 将雾图建模为连续且动态可演化的各向异性高斯场，取代传统CNN或Transformer的静态网格处理。
- 提出一种新颖的重建-解耦零样本学习策略，将大气散射模型嵌入高斯参数空间，驱动高斯基元在优化过程中自适应地分裂、克隆和剪枝，从而实现传输介质与清晰纹理的几何级解耦。
- 引入显式结构保持约束，抑制传统物理先验常见的伪影。

### 主要贡献
- 首次将2D高斯泼溅引入图像去雾领域，提出零样本去雾框架Dehaze-GaussianImage，打破了像素网格处理范式。
- 提出重建-解耦零样本学习策略，将大气散射模型融入高斯参数空间，实现几何级解耦。
- 实验表明，该方法在完全无监督、参数极少的条件下达到最先进（SOTA）性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法在零样本去雾领域提出新颖的高斯表示范式，具有较好的创新性和理论价值；但摘要缺乏定量实验对比细节，也未说明泛化到其他视觉任务或真实场景的挑战，因此属于中等优先级的参考阅读。

</details>

<details>
<summary>Abstract</summary>

Existing single image dehazing methods are often constrained by computational redundancy in pixel-level optimization and the lack of physical interpretability in implicit neural networks. These limitations hinder the balance between representation efficiency and reconstruction fidelity. To address these issues, we propose Dehaze-GaussianImage, the first zero-shot framework that introduces 2D Gaussian Splatting (2DGS) into the image dehazing domain to break the traditional pixel-grid processing paradigm. Distinct from static convolutional neural networks (CNNs) or Transformers, our approach models hazy images as continuous and dynamically evolvable anisotropic Gaussian fields. Specifically, we propose a novel reconstruction-decoupling zero-shot learning strategy that embeds the atmospheric scattering model into the Gaussian parameter space. This strategy drives Gaussian primitives to adaptively split, clone, and prune during optimization, achieving geometric-level decoupling of the transmission medium and clear textures. Furthermore, explicit structure-preserving constraints are introduced to suppress artifacts commonly caused by traditional physical priors. Experimental results demonstrate that the proposed method achieves state-of-the-art (SOTA) performance in a fully unsupervised manner with minimal parameters, highlighting the potential of explicit Gaussian representation for low-level vision tasks.

</details>

#### 2026-06-15 - Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement

**Authors:** Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.16159) - [pdf](https://arxiv.org/pdf/2606.16159)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement
- 作者：Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.16159

### 一句话总结
提出首个基于显式-隐式联合建模的低光图像增强框架CGS-Retinex，通过连续高斯泼溅估计全局光照分布，并利用隐式神经表示独立建模反射率，以解决低光增强中的颜色失真和结构伪影问题。

### 研究问题
低光图像增强中，现有方法难以在全局平滑光照调整与局部高频细节恢复之间取得平衡，常导致颜色失真和结构伪影。

### 核心思路/方法
1. **连续高斯渲染器**：将图像网格表示为连续参数场，用于估计空间连续的全局光照分布，从而消除离散高斯采样导致的网格伪影。
2. **隐式反射率建模**：引入隐式神经表示独立建模反射率，利用浅层高频特征指导网络准确重建退化纹理细节。
3. **Retinex框架约束**：在Retinex理论框架中，引入物理启发的亮度一致性约束和光照平滑正则化，使显式光照和隐式反射率能保持恰当曝光，并高保真恢复高频结构与颜色。

### 主要贡献
- 首次将连续高斯泼溅与Retinex理论深度结合，建立显式-隐式联合建模的低光增强框架。
- 提出连续高斯渲染器消除离散采样伪影，并通过隐式神经表示独立恢复高频纹理。
- 实验表明该方法能显著抑制暗区噪声和过曝，实现优异的高频结构保真度和颜色恢复。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作为低光图像增强引入了全新的连续物理表示范式（连续高斯泼溅+隐式神经表示），方法具有创新性，且针对颜色失真和结构伪影等核心难题提出了系统性解决方案，适合关注图像增强、神经渲染及Retinex理论的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Low-light image enhancement aims to recover clear images from low-illumination observations and is crucial for high-level downstream vision tasks. However, existing methods frequently encounter color distortion and structural artifacts when balancing global smooth illumination adjustment and local high-frequency detail recovery. To address these issues, we propose CGS-Retinex as the first low-light image enhancement framework based on explicit-implicit joint modeling. Our framework deeply integrates continuous Gaussian splatting with Retinex theory. Specifically, we represent the image grid as a continuous parameter field and propose a continuous Gaussian renderer to estimate the spatially continuous global illumination distribution. This approach fundamentally eliminates grid artifacts caused by discrete Gaussian sampling. Furthermore, we introduce an implicit neural representation to model reflectance independently. We leverage shallow high-frequency features to guide the network in accurately reconstructing degraded texture details. Within the Retinex framework, we incorporate physics-inspired brightness consistency constraints and illumination smoothness regularization to enable explicit illumination and implicit reflectance to maintain proper exposure and achieve high-fidelity recovery of high-frequency structures and colors. Extensive experiments demonstrate that CGS-Retinex significantly suppresses dark-region noise and overexposure while achieving exceptional high-frequency structural fidelity and color restoration by precisely decoupling illumination and texture. This work establishes a novel continuous physical representation paradigm for low-light image enhancement.

</details>

#### 2026-06-14 - TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization

**Authors:** Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu
**Links:** [abs](https://arxiv.org/abs/2606.15924) - [pdf](https://arxiv.org/pdf/2606.15924)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization
- 作者：Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu
- 出版日期：2026-06-14T16:59:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.15924；PDF：https://arxiv.org/pdf/2606.15924

### 一句话总结
TurboGS 是一个通过错误引导的稀疏像素采样和优化来加速 3D 高斯泼溅（3DGS）训练的训练框架，能够在单张 RTX 5090 GPU 上 100 秒内实现与原始 3DGS 相当或更优的新视角渲染质量，训练速度提升高达 10 倍。

### 研究问题
如何在保持高保真渲染质量的前提下，加速 3D 高斯泼溅（3DGS）的训练优化过程，以减少处理冗余像素和牺牲细节的问题。

### 核心思路/方法
TurboGS 基于四个核心组件构建：
1.  **基于块的稀疏像素采样**：利用训练过程中的多视图重建误差，优先处理困难区域（挑战区域），跳过已良好重建的区域，避免冗余梯度计算。
2.  **基于块的结构感知损失与稀疏归一化互相关（NCC）**：提供稀疏但有效的监督信号，以保留精细细节并稳定训练。
3.  **错误驱动的密度控制策略**：动态分配模型容量，移除冗余的高斯原语，控制模型复杂度。
4.  **定制化混合优化器**：结合 Hessian 引导的更新与 Adam 动量衰减，在稀疏监督下稳定并改善收敛。

### 主要贡献
- 提出了 TurboGS，一个基于错误引导稀疏像素采样和优化的 3DGS 加速训练框架。
- 通过四大核心组件（稀疏采样、结构感知损失、密度控制、混合优化器）协同工作，显著减少计算冗余。
- 实验证明，在单张 RTX 5090 GPU 上，TurboGS 能在 100 秒内取得与原始 3DGS 相当或更优的渲染质量，实现高达 10 倍的训练加速。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作直接针对 3DGS 的训练效率瓶颈，提出了一个端到端的加速框架，在保持质量的同时实现了数量级的速度提升（10倍），且发表在 2026 年，具有很强的时效性和实用性，尤其适合关注高效神经渲染和实时应用的读者。

</details>

<details>
<summary>Abstract</summary>

Consumer-level applications require fast optimization of 3D Gaussian Splatting (3DGS) with high-fidelity novel view rendering. However, existing 3DGS acceleration approaches still incur substantial computation on redundant pixels while sacrificing fine details. In this paper, we present TurboGS, an error-guided training framework that accelerates 3DGS by concentrating optimization on perceptually informative pixels. TurboGS is built upon four core components: (1) a tile-wise sparse pixel sampling, which, driven by multi-view reconstruction errors during training, prioritizes challenging regions and skips well-reconstructed ones to avoid redundant gradient computation; (2) a tile-wise structure-aware loss with sparse Normalized Cross-Correlation, which provides sparse yet effective supervision to preserve fine details and stabilize training; (3) an error-driven Gaussian density control strategy, which dynamically allocates model capacity and removes redundant primitives; and (4) a tailored hybrid optimizer that couples Hessian-informed updates with Adam moment damping to stabilize and improve convergence under sparse supervision. Experiments on standard benchmarks demonstrate that TurboGS can deliver on par or superior rendering quality within 100 seconds on a single RTX 5090 GPU card (up to 10x training speedup over vanilla 3DGS).

</details>

#### 2026-06-14 - EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units

**Authors:** Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen
**Links:** [abs](https://arxiv.org/abs/2606.15848) - [pdf](https://arxiv.org/pdf/2606.15848)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units
- 作者：Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen
- 出版日期：2026-06-14
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.15848

### 一句话总结
本文提出EmoZone-Talker框架，通过区域语义控制和面部动作单元（AU），解决音频驱动3DGS说话头在表情控制中的空间纠缠和时间不稳定问题，实现精细、可解释的面部动画。

### 研究问题
如何在高保真音频驱动的3DGS说话头合成中，实现精细、可编辑且时空稳定的面部表情控制，克服语音驱动动态与显式表情信号之间的内在冲突。

### 核心思路/方法
1. 提出 **Synergy Zones with Prioritized Attention Bias (SZ-PAB)**，利用解剖先验约束区域级模态贡献，显式解耦音频和表情信号的贡献。
2. 提出 **Channel-Independent Temporal AU Encoder (CIT-AE)**，对动作单元（AU）的时序动态进行独立通道建模，保证时间一致性。
3. 将上述解耦的区域AU表示集成到3D高斯变形中，实现精确、可解释的面部表情控制。

### 主要贡献
- 将音频驱动面部动画重新构造为跨模态冲突下的结构化时空协调问题。
- 提出SZ-PAB和CIT-AE两种模块，实现显式的空间解耦和时序动态建模。
- 实验表明，该方法在表情可控性、真实感、上脸精确度和时间一致性上均有提升，同时保持高渲染质量和准确唇同步。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对3DGS说话头合成中的关键问题（表情控制的可解释性与时空稳定性），提出了结构化的新框架，实验效果显著，且代码将开源，对领域研究和应用有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has shown strong potential for high-fidelity talking head synthesis. However, enabling fine-grained, interpretable, and editable facial expression control remains fundamentally challenging due to intrinsic conflicts between speech-driven facial dynamics and explicit expression signals. Existing methods rely on implicit multimodal fusion, leading to spatial entanglement and temporal instability. We present EmoZone-Talker, a novel framework that reformulates audio-driven facial animation as a structured spatial-temporal coordination problem under cross-modal conflicts. Our approach introduces an explicit spatial disentanglement and temporal dynamics modeling of facial motion. Specifically, we propose Synergy Zones with Prioritized Attention Bias (SZ-PAB) to explicitly decouple modality contributions via region-wise constraints guided by anatomical priors, and a Channel-Independent Temporal AU Encoder (CIT-AE) to model temporally coherent AU dynamics. By integrating these representations into 3D Gaussian deformation, EmoZone-Talker enables precise and interpretable control over facial expressions. Extensive experiments demonstrate that our method improves expression controllability and realism, with notable gains in upper-face accuracy and temporal coherence, while preserving high rendering quality and accurate lip synchronization. Code will be publicly released to facilitate reproducibility and further research.

</details>

#### 2026-06-14 - SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction

**Authors:** Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao
**Links:** [abs](https://arxiv.org/abs/2606.15659) - [pdf](https://arxiv.org/pdf/2606.15659)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction
- 作者：Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao
- 出版日期：2026-06-14T07:55:57Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.15659

### 一句话总结
本文提出SpatialAvatar-0，一种基于FLAME网格绑定高斯表示的多阶段重建框架，通过前馈生成器和布局保持的逐主体精炼，实现高质量4D头部虚拟形象重建，并在多个基准上取得领先性能。

### 研究问题
如何从单张或少数源肖像出发，高效重建高质量4D头部虚拟形象，并弥合前馈预测器（可泛化）和逐主体精炼器（需大量迭代）两种范式之间的鸿沟。

### 核心思路/方法
1. **共享的FLAME网格绑定高斯表示**：将3D高斯绑定到FLAME网格上，使前馈生成和逐主体精炼共用同一表示，避免表示不兼容。
2. **前馈生成器**：使用参数自由的K源均值池化（parameter-free K-source mean-pool）处理可变数量的输入源，并采用单目时间到多视角空间的两阶段调度策略（monocular-temporal to multi-view-spatial two-phase schedule），防止身份先验在小规模多视图集上坍塌。
3. **布局保持的逐主体精炼**：仅需10K次迭代的精炼流程，冻结FLAME绑定和高斯数量，用三分量抗尖峰正则化（three-component anti-spike regularization）替代传统的自适应稠密化，从而保留前馈阶段的高斯布局。

### 主要贡献
1. 提出了前馈生成与逐主体精炼共享同一FLAME网格绑定高斯表示的框架，首次实现两种范式的端到端兼容。
2. 设计了一种参数自由的K源均值池化机制，支持可变数量的输入源，减少对固定源数训练数据的依赖。
3. 引入10K次迭代的布局保持精炼流程，相比传统300K-600K迭代方法显著降低计算成本，同时提升指标（如超过GeoAvatar +1.3 dB PSNR）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作在4D虚拟形象重建这一活跃方向上提出了统一前馈与精炼的新思路，性能提升显著（PSNR+1.3~1.5 dB），且训练效率提升高达60倍，对AR/VR和数字人领域的实践有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

High-quality 4D head avatars from one or a few source portraits are central to telepresence, AR/VR, and digital-human interaction. 3D Gaussian Splatting (3DGS) has emerged as the dominant representation, with two complementary regimes (generalizable feed-forward predictors and per-subject refiners) maturing in parallel. However, existing feed-forward predictors are trained on a single dataset family with a hard-coded source count, inheriting the corresponding domain bias. Per-subject refiners require 300K--600K iterations and rely on adaptive densification that destroys upstream Gaussian layouts, preventing the two regimes from sharing a representation end-to-end. To bridge both regimes we propose SpatialAvatar-0 on a shared FLAME-mesh-bound Gaussian representation: a feed-forward generator with a parameter-free K-source mean-pool and a monocular-temporal to multi-view-spatial two-phase schedule that anchors against identity-prior collapse onto the smaller multi-view set. We further introduce a 10K-iter layout-preserving per-subject refinement loop that freezes the FLAME-binding and Gaussian count and replaces densification with a three-component anti-spike regularization. On VFHQ/HDTF cross-domain zero-shot we surpass the in-domain leader GAGAvatar by +1.5 dB PSNR despite never training on either test domain, and on the SplattingAvatar monocular benchmark we lead every reported metric, surpassing the 300K-iter GeoAvatar by +1.3 dB PSNR at up to 60x shorter per-subject schedule than common SOTA baselines. Website: https://spatialwalk.github.io/SpatialAvatar-0.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-18 - S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence

**Authors:** Yalun Dai, Hao Li, Shulin Tian, Runmao Yao, Yuhao Dong, Fangzhou Hong, Zhaoxi Chen, Fangfu Liu, Baoliang Tian, Dingwen Zhang, Tao Wang, Kim-Hui Yap, Ziwei Liu
**Links:** [abs](https://arxiv.org/abs/2606.20515) - [pdf](https://arxiv.org/pdf/2606.20515)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence
- 作者：Yalun Dai, Hao Li, Shulin Tian, Runmao Yao, Yuhao Dong, Fangzhou Hong, Zhaoxi Chen, Fangfu Liu, Baoliang Tian, Dingwen Zhang, Tao Wang, Kim-Hui Yap, Ziwei Liu
- 出版日期：2026-06-18
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2606.20515) | [PDF](https://arxiv.org/pdf/2606.20515)

### 一句话总结
本文提出 **S-Agent**，一种空间工具使用智能体范式，将空间推理建模为时空证据累积过程，通过层次化工具和记忆机制显著提升多视图和视频空间推理性能，并基于其生成的轨迹微调出紧凑型空间智能体S-Agent-8B。

### 研究问题
现有视觉语言模型(VLM)和工具增强智能体大多依赖静态、无状态推理，无法对持续演进的3D世界进行空间推理。本文试图解决如何实现连续多视图图像和视频中的空间智能问题。

### 核心思路/方法
1. **任务重定义**：将空间推理从孤立帧级预测重塑为**时空证据累积**的场景级理解。
2. **语义规划与工具层级**：VLM作为语义规划器决定需何种证据；层次化空间工具和专家将2D对象提升为3D几何证据，并聚合为高级空间知识（如计数、测量、朝向、相对位置）。
3. **时间记忆机制**：包括**场景记忆**（维护持续演进的场景状态）和**智能体记忆**（累积推理上下文），以跨帧和推理步骤整合证据。
4. **训练与微调**：无训练地增强开源和闭源VLM；进一步对S-Agent生成的空间轨迹（S-300K）进行监督微调，得到紧凑模型S-Agent-8B。

### 主要贡献
1. 提出 **S-Agent** 范式，将空间推理转化为证据累积过程，突破静态推理限制。
2. 引入层次化空间工具和双记忆机制（场景记忆+智能体记忆），实现跨时空证据整合。
3. 在多项多视图和视频空间推理基准上，无需额外训练即可一致提升开源/闭源VLM性能。
4. 通过微调S-Agent生成的轨迹，得到紧凑模型 **S-Agent-8B**，性能超越同尺度基线（如Qwen3-VL-8B），媲美先进闭源模型（如GPT-5.4、Gemini 3）。

### 局限性
摘要未提供足够信息，无法评估具体局限性（如计算开销、泛化边界、失败案例等）。

### 阅读优先级
**高**
理由：该工作聚焦空间推理这一具身智能/机器人领域核心挑战，提出新颖的“证据累积+工具层级+记忆”范式，实验结果表明其既能无训练增强现有模型，又能通过微调获得紧凑高效模型，实用性和创新性均显著，对从事空间感知、VLM增强和多模态推理的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-world spatial intelligence requires reasoning over a continuous and evolving 3D world, yet existing VLMs and tool-augmented agents largely remain tied to static, stateless inference from isolated visual observations. We introduce \textbf{\textsc{S-Agent}}, a spatial tool-use agentic paradigm for understanding and reasoning over continuous multi-view images and videos. By formulating spatial reasoning as spatio-temporal evidence accumulation rather than isolated frame-level prediction, \textsc{S-Agent} reshapes spatial perception into scene-centric understanding beyond frame-centric recognition. Specifically, \textsc{S-Agent} casts the VLM as a semantic planner that decides what evidence is needed, while a hierarchy of spatial tools and experts grounds objects in 2D, lifts them into 3D geometric evidence, and aggregates this evidence into high-level spatial knowledge (\textit{e.g.}, counting, measurement, orientation, and relative position). Additionally, a temporal memory mechanism, including Scene Memory for maintaining the evolving scene state and Agent Memory for accumulating reasoning context, enables evidence integration across frames and reasoning steps. Comprehensive experiments on multi-view and video spatial reasoning benchmarks show that \textsc{S-Agent} consistently improves both open-source and closed-source VLMs in a training-free manner. Beyond inference-time augmentation, supervised fine-tuning (SFT) on \textsc{S-Agent}-generated spatial trajectories \textsc{S-300K} yields \textsc{S-Agent-8B}, a compact spatial agent that significantly surpasses similar-scale baselines (e.g., Qwen3-VL-8B) and performs comparably to advanced closed-source models (e.g., GPT-5.4 and Gemini 3).

</details>

#### 2026-06-18 - TaCauchy: An Extensible FEM Framework for Vision-Based Tactile Simulation

**Authors:** Hengfei Zhao, Yifan Xie, Junhao Gong, Yue Sun, Kai Zhu, Weihua He, Shoujie Li, Haohuan Fu, Wenbo Ding
**Links:** [abs](https://arxiv.org/abs/2606.20426) - [pdf](https://arxiv.org/pdf/2606.20426)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TaCauchy: An Extensible FEM Framework for Vision-Based Tactile Simulation
- 作者：Hengfei Zhao, Yifan Xie, Junhao Gong, Yue Sun, Kai Zhu, Weihua He, Shoujie Li, Haohuan Fu, Wenbo Ding
- 出版日期：2026-06-18
- 分类：具身/机器人/增强现实应用（Embodied / Robotics / AR Applications）
- 链接：https://arxiv.org/abs/2606.20426

### 一句话总结
TaCauchy是一个基于有限元法（FEM）的视觉触觉仿真框架，通过集成到Isaac Sim平台中，从第一性原理直接计算柯西应力张量以提供精准的力学场，并支持多种触觉传感器的快速集成。

### 研究问题
如何在高性能GPU加速的机器人仿真平台（如Isaac Sim）中，提供准确且物理一致的机械应力场，以支持基于视觉的触觉传感器的高保真仿真和强化学习任务。

### 核心思路/方法
- 基于统一增量势能接触（UIPC）求解器，利用超弹性本构定律直接计算柯西应力张量。
- 将应力张量投影至接触表面，从而获取接触力矢量与压力分布，避免依赖经验估计。
- 实现自动化网格生成（含几何感知自适应细化）和模块化传感器接口，支持GelSight Mini、DIGIT、9DTact等多种触觉传感器的快速扩展与配置。

### 主要贡献
1. 提出TaCauchy框架，首次将基于物理的有限元力计算无缝集成到Isaac Sim中，提供第一性原理的力学真值。
2. 在单环境仿真中达到33.40 FPS，60个并行环境聚合吞吐量达555 FPS，且应力提取开销低于1毫秒，验证了实时性与可扩展性。
3. 物理验证实验显示，在1.2556 N至4.7332 N的力范围内，模拟与真实触觉响应的结构相似性指数（SSIM）高于0.93，证明框架能够为下游机器人操作任务提供准确、物理基础的力监督信号。

### 局限性
摘要未提供足够信息。具体实验局限性（如特定材料模型的适用范围、网格细化对复杂几何的误差、或对超弹性本构参数的敏感度等）未在摘要中提及。

### 阅读优先级
高  
理由：该工作解决了视觉触觉仿真中力学场准确性这一关键瓶颈，且提供了可直接部署在主流机器人仿真平台（Isaac Sim）上的开源自适应框架，对从事触觉传感、机器人操作和仿真到现实迁移的研究者具有较高的实用价值和参考意义。

</details>

<details>
<summary>Abstract</summary>

Vision-based tactile sensors require high-fidelity simulation for reinforcement learning, yet existing approaches struggle to provide accurate mechanical stress fields within GPU-accelerated robotics platforms. We present TaCauchy, an extensible Finite Element Method (FEM) framework that integrates rigorous physics-based force computation into Isaac Sim. Built on the Unified Incremental Potential Contact (UIPC) solver, TaCauchy directly computes Cauchy stress tensors from hyperelastic constitutive laws and projects them onto contact surfaces to obtain traction forces and pressure distributions, providing mechanical ground truth from first principles rather than empirical estimation. Our framework features automatic mesh generation with geometry-aware adaptive refinement and a modular sensor interface enabling rapid integration of diverse sensors (GelSight Mini, DIGIT, 9DTact) with minimal configuration. Performance benchmarks demonstrate 33.40 FPS for single environments and 555 FPS aggregate throughput across 60 parallel environments, with stress extraction overhead under 1 ms. Physical validation experiments show strong agreement between simulated and real tactile responses across force ranges from 1.2556 N to 4.7332 N, achieving SSIM above 0.93, confirming the framework's capability to provide accurate, physically-grounded force supervision for downstream robotic manipulation tasks.

</details>

#### 2026-06-18 - Holo-World: Unified Camera, Object and Weather Control for Video World Model

**Authors:** Xiangchen Yin, Wenzhang Sun, Jiahui Yuan, Zijie Liu, Yinda Chen, Wei Li, Dachun Kai, Chunfeng Wang, Xiaoyan Sun
**Links:** [abs](https://arxiv.org/abs/2606.20083) - [pdf](https://arxiv.org/pdf/2606.20083)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Holo-World: Unified Camera, Object and Weather Control for Video World Model
- 作者：Xiangchen Yin, Wenzhang Sun, Jiahui Yuan, Zijie Liu, Yinda Chen, Wei Li, Dachun Kai, Chunfeng Wang, Xiaoyan Sun
- 出版日期：2026-06-18T11:01:34Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.20083

### 一句话总结
Holo-World 提出了一种统一的视频世界模型，能够从单张图像出发，通过相机、物体控制和天气指令，生成保持世界状态或转换到目标天气状态的视频。

### 研究问题
如何从单张图像出发，实现统一的相机、物体和天气控制，并能够根据指令生成保持原始世界或转移到目标天气状态的视频。

### 核心思路/方法
1. 构建 HoloStateData 数据集：将多样的视频转换为统一的控制样本，提供相机、物体和天气的监督信号。
2. 设计 Holo-World 模型：包含统一的场景适配器（Unified Scene Adapter），将世界保持和天气转移分解为不同的参数子空间，利用渲染背景、几何缓冲区和物体控制来维持场景结构，同时建模天气相关的表观和粒子效果。
3. 提出 Scene-Weather Decomposed CFG：分别引导场景和天气残差，增强目标天气效果而不过度放大整个条件。

### 主要贡献
1. 提出首个从单张图像出发、支持相机、物体和天气统一控制的视频世界模型 Holo-World。
2. 构建了 HoloStateData 数据集，用于大规模监督学习。
3. 在保持精确相机和物体控制及场景结构的同时，能够将场景转移到多样目标天气状态，在天气状态生成上优于视频到视频的天气编辑基线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该工作聚焦于视频世界模型在统一控制（相机、物体、天气）方面的创新，对于研究可控视频生成、世界模型或多模态控制的研究者有一定参考价值。但摘要未提供详尽的实验对比结果和具体性能数据，实用性评估需进一步阅读原文。

</details>

<details>
<summary>Abstract</summary>

Video world models are moving toward preserving an observed world under controllable camera and object motion while allowing its environmental state to change. Yet these controls remain isolated, and weather generation typically relies on a source video or reconstructed scene that already specifies future structure. We study a first-frame-anchored source-to-state setting, where the model starts from a single image and follows explicit camera and object controls and an optional weather instruction, then generates a video that either preserves the source world or transfers it to a target weather state. To address these challenges, we first build HoloStateData, a state video dataset that turns diverse videos into unified control samples for camera, object, and weather supervision. Second, we introduce Holo-World, a unified controllable video world model that jointly controls scene from a single image. Its Unified Scene Adapter factorizes world preservation and weather transfer into distinct parameter subspaces, using rendered background, geometry buffers, and object controls to maintain controlled scene structure while modeling weather-dependent appearance and particle effects. Additionally, Scene-Weather Decomposed CFG guides scene and weather residuals separately, strengthening target weather effects without over-amplifying the full condition. Quantitative and qualitative experiments demonstrate that Holo-World maintains precise camera and object control with consistent scene structure while transferring scenes into diverse target weather state, outperforming video-to-video weather editing baselines on weather-state generation. Our project page is available at \url{https://xiangchenyin.github.io/Holo-World/}.

</details>

#### 2026-06-18 - SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour

**Authors:** Kaixin Lan, Ze Wang, Hongyi Li, Lei Jiang, Chaojie Fu, Chengkai Su, Choi Lam Wong, Yongbin Jin, Hongtao Wang
**Links:** [abs](https://arxiv.org/abs/2606.19928) - [pdf](https://arxiv.org/pdf/2606.19928)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour
- 作者：Kaixin Lan, Ze Wang, Hongyi Li, Lei Jiang, Chaojie Fu, Chengkai Su, Choi Lam Wong, Yongbin Jin, Hongtao Wang
- 出版日期：2026-06-18
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.19928

### 一句话总结
本文提出一种内置对称等变性的端到端世界模型框架SWAP，使四足机器人在真实世界中完成破纪录的2.13米跨越和1.63米攀爬，并展现了良好的几何泛化和零样本迁移能力。

### 研究问题
如何通过结构先验（对称等变性）减少纯数据驱动潜世界模型在极端跑酷中冗余学习左右对称交互模式的负担，提升潜空间效率并增强下游策略的几何泛化能力。

### 核心思路/方法
将对称等变性直接嵌入世界模型和演员-评论家网络中。通过在模型架构层面显式编码左右对称的几何结构约束，使模型不必独立学习对称模式，从而更高效地捕获几何规律。在真实世界四足机器人跑酷任务上进行验证。

### 主要贡献
1. 提出SWAP框架，将对称等变性嵌入端到端的潜世界模型和策略网络。
2. 在真实世界测试中，机器人实现跨越2.13米间隙和攀爬1.63米平台，创造四足机器人跑酷纪录。
3. 展示了对未见镜像地形的强几何泛化能力，以及在多样化户外环境中的优异零样本迁移能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该论文在四足机器人跑酷任务上取得了显著的实证突破（破纪录性能），并引入对称等变形作为结构先验，思路具有一定的启发性。但摘要未涉及方法细节、训练流程、实验设置等，需要阅读全文才能评估其技术贡献的完整性和可复现性。如果您关注机器人运动控制中的几何先验应用，可优先阅读。

</details>

<details>
<summary>Abstract</summary>

While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns. This inflates the learning burden and hinders the capture of geometric regularities, restricting the latent space's efficiency for downstream policies. To address this, we propose SWAP, an end-to-end equivariant symmetric world model. This framework embeds symmetry directly into both the world model and the actor-critic networks. In real-world tests, the robot leaps across a 2.13 m gap and climbs a 1.63 m platform, breaking records for quadruped parkour. Furthermore, the framework exhibits robust geometric generalization to unseen mirrored terrains and exceptional zero-shot transferability across diverse outdoor environments. These results demonstrate that symmetry equivariance is an effective structural prior for pushing the physical boundaries of learned legged locomotion.

</details>

#### 2026-06-18 - Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding

**Authors:** Jianing Li, Zhou Fang, Yijiang Liu, Li Du
**Links:** [abs](https://arxiv.org/abs/2606.19776) - [pdf](https://arxiv.org/pdf/2606.19776)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding
- 作者：Jianing Li, Zhou Fang, Yijiang Liu, Li Du
- 出版日期：2026-06-18
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2606.19776) | [PDF](https://arxiv.org/pdf/2606.19776)

### 一句话总结
Occ-VLM提出了一种仅依赖RGB图像和单个2D视觉编码器的3D场景理解框架，通过重建3D占用作为几何先验，实现无需显式3D输入的视觉-语言联合推理。

### 研究问题
现有3D视觉语言模型往往需显式3D输入（如点云、RGB-D序列）或引入额外的3D几何编码器，导致3D几何感知与2D视觉语言预训练之间的结构性解耦，阻碍了统一的3D视觉语言表示。本文旨在仅用2D图像实现3D场景的几何感知与语言推理的融合。

### 核心思路/方法
1. **输入**：仅使用带位姿的RGB图像，并采用单一2D视觉编码器。
2. **3D占用重建**：作为辅助几何先验，从2D图像中重建3D场景占用信息。
3. **空间关联**：利用3D占用将前景2D标记与3D空间进行空间关联。
4. **语言解码**：关联后的标记由大语言模型（LLM）解码，实现统一的场景理解任务。

### 主要贡献
- 提出Occ-VLM，仅用2D图像输入即可实现3D几何感知与视觉语言推理的统一框架。
- 在多视图占用预测任务上达到当前最优性能。
- 在3D视觉问答（VQA）和3D密集描述基准上，性能与采用3D输入的VLM持平。

### 局限性
摘要未提供足够信息：未提及在极端遮挡、大尺度场景或实时推理能力上的局限性，也未讨论对训练数据规模或标注成本的要求。

### 阅读优先级
**中**。理由：该工作聚焦于3D室内场景理解，在仅用2D图像的情况下实现了与3D输入VLM相当的性能，且在多视图占用预测上达到SOTA，对嵌入式智能和机器人视觉领域有参考价值。但摘要未提供详细的实验设置和消融分析，约束了对其实际效果的全面评估。

</details>

<details>
<summary>Abstract</summary>

Recently, vision-language models (VLMs) have made significant progress in 3D scene understanding, driving advances in applications such as embodied intelligence and robotic vision. However, existing approaches typically either rely directly on explicit 3D inputs (e.g., point clouds or RGB-D sequences), or introduce an additional 3D geometry encoder to derive 3D-aware visual tokens from 2D images. Such designs structurally decouple 3D geometric perception from the rich 2D semantics learned via vision-language pre-training, hindering the development of a unified 3D vision-language representation. In this work, we propose Occ-VLM, a novel framework for 3D scene understanding that operates purely on posed RGB images and employs a single 2D vision encoder. Specifically, Occ-VLM reconstructs 3D scene occupancy as an auxiliary geometric prior, which is utilized to spatially associate foreground 2D tokens with 3D space. These tokens are then decoded by a Large Language Model (LLM) for unified scene understanding. Extensive experiments demonstrate that Occ-VLM achieves both accurate geometric perception and robust vision-language reasoning: it attains state-of-the-art performance on multi-view occupancy prediction, while performing on par with 3D-input VLMs on 3D Visual Question Answering (VQA) and 3D dense captioning benchmarks.

</details>

#### 2026-06-17 - Modeling Branches for Active Manipulation using Iterative Parameter Estimation

**Authors:** Madhav Rijal, Rashik Shrestha, Trevor Smith, Yu Gu
**Links:** [abs](https://arxiv.org/abs/2606.19314) - [pdf](https://arxiv.org/pdf/2606.19314)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Modeling Branches for Active Manipulation using Iterative Parameter Estimation
- 作者：Madhav Rijal, Rashik Shrestha, Trevor Smith, Yu Gu
- 出版日期：2026-06-17
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.19314

### 一句话总结
本文提出一种通过迭代估计材料参数来建模植物分支的方法，以支持精细的分支操作；实验表明，该方法在路径长度略有增加的情况下，显著减少了形变能量。

### 研究问题
如何对形态各异的植物分支进行精确建模，以支持农业机器人中精细、低损伤的分支操作（如重定位、稳定、清除视觉障碍）。

### 核心思路/方法
1. **分支建模**：从点云数据构建四面体分支模型，并利用有限元方法模拟其行为。
2. **参数估计**：基于真实观测的形变数据，通过迭代估计分支的材料参数。
3. **运动规划**：结合形变感知的运动规划器，计算最优路径以移动并稳定分支，使分支处于另一机器人的视野内。

### 主要贡献
- 提出了一种结合点云建模、有限元仿真和迭代参数估计的植物分支建模方法。
- 通过30次不同几何和材料属性的分支试验验证：该方法平均减少形变能量35.69%，同时平均增加路径长度8.10%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法针对农业机器人中精细分支操作这一具体场景，结合了建模、仿真与规划，结果量化且有效。但该方法仅基于摘要无法判断其泛化能力或实现复杂度，对机器人操作领域研究者有一定参考价值；若对植物建模或软体操作不感兴趣，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

This study presents a method for modeling diverse plant branches by iteratively estimating material parameters to support delicate branch manipulation. Branch manipulation is necessary in agricultural robotics for plant repositioning, stabilizing, and clearing visual obstructions in dense foliage. The proposed method builds a tetrahedral branch model from point-cloud data and simulates its behavior using the finite element method. Using real observed deformation data, it iteratively estimates branch parameters and then computes an optimal path with a deformation-aware motion planner to move and stabilize branches within another robot's field of view. Across 30 trials on branches with varying geometries and material properties, the proposed method reduced the deformation energy by 35.69% while increasing the path length by 8.10% on average.

</details>

#### 2026-06-17 - OneCanvas: 3D Scene Understanding via Panoramic Reprojection

**Authors:** Bartłomiej Baranowski, Dave Zhenyu Chen, Matthias Nießner
**Links:** [abs](https://arxiv.org/abs/2606.19253) - [pdf](https://arxiv.org/pdf/2606.19253)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OneCanvas: 3D Scene Understanding via Panoramic Reprojection
- 作者：Bartłomiej Baranowski, Dave Zhenyu Chen, Matthias Nießner
- 出版日期：2026-06-17
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.19253

### 一句话总结
OneCanvas 提出一种全景画布表示方法，将所有视角的图像块特征投影到单一等距柱面画布上，使预训练视觉语言模型无需复杂几何编码器即可直接理解3D场景，并在多个基准上取得最优结果。

### 研究问题
如何在不依赖复杂几何编码器和大量训练预算的情况下，让视觉语言模型（VLM）具备对3D场景的空间推理能力，同时支持从特定视角进行情境化推理（如机器人和具身AI所需）。

### 核心思路/方法
- **全景画布投影**：将每个视角的图像块特征，利用其深度和相机姿态反投影到3D世界坐标，再根据画布原点观察该点的连续经纬度放置到等距柱面画布上，不进行光栅化或跨视图特征聚合。
- **3D位置嵌入**：在每个图像块特征中加入其度量坐标的3D位置嵌入，以恢复将世界坐标压缩到角度坐标时丢失的深度信息。
- **无需模型修改**：所有帧的块特征共享同一个空间坐标系，无需对VLM骨干网络进行融合或重大架构修改，预训练VLM直接将其作为普通图像处理。
- **空间预训练课程**：在空画布上从真实图像中提取物体块特征，程序化地放置在选定的3D世界位置，生成覆盖多种空间推理任务的即时监督，并控制答案分布以减少空间推理捷径。

### 主要贡献
1. 提出一种无需复杂几何编码器或大量训练修改的3D场景表示方法，使VLM能像处理普通图像一样理解3D场景。
2. 引入空间预训练课程，通过程序化生成多样化的空间推理训练样本，减少推理捷径。
3. 在SQA3D、VSI-Bench和SPBench上达到最先进精度，且训练计算量比最强竞争对手低一个数量级。

### 局限性
摘要未提供足够信息（如方法在动态场景或复杂光照下的表现、对深度和姿态精度的依赖程度、画布分辨率与场景规模的可扩展性等）。

### 阅读优先级
**高**
理由：该方法在保持较高空间推理精度的同时显著降低了训练计算成本，且直接兼容现有预训练VLM，对具身智能、机器人等领域的3D场景理解具有重要实用价值。摘要中提到的创新性全景画布表示和预训练课程设计新颖，实验结果（SOTA）具有说服力。

</details>

<details>
<summary>Abstract</summary>

Existing approaches to 3D scene understanding in Vision-Language Models (VLMs) either rely on complex, model-specific geometry encoders or large training budgets in pursuit of spatial reasoning. Instead, OneCanvas aggregates patch features from all views onto a single equirectangular panoramic canvas. Namely, each patch is unprojected to a 3D world coordinate using its depth and camera pose, then placed on the canvas at the continuous longitude and latitude of that point as seen from the canvas origin, with no rasterization or aggregation across overlapping views. A 3D position embedding of the patch's metric coordinates is added to its feature, restoring the depth lost when collapsing the world position to an angular canvas coordinate. Patches from all frames thus share one spatial coordinate system with no fusion or major architectural modifications of the backbone. The pretrained VLM consumes this representation as if it were an ordinary image. Because the canvas can be centered on any pose of interest, the same representation directly supports situated reasoning from a specific viewpoint, a common requirement in robotics and embodied AI. Thanks to this representation, we can also introduce a spatial pretraining curriculum: by procedurally placing patch features of objects, drawn from real images, at chosen 3D world positions on an otherwise empty canvas, we generate on-the-fly supervision spanning a broad range of spatial reasoning tasks, with answer distributions controlled to reduce spatial reasoning shortcuts. OneCanvas achieves state-of-the-art accuracy on SQA3D and VSI-Bench, and generalizes to out-of-distribution data on SPBench, using an order of magnitude less training compute than the strongest competing methods.

</details>

#### 2026-06-17 - Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation

**Authors:** Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, Weiming Li, Dong Wang, Huchuan Lu, Xu Jia
**Links:** [abs](https://arxiv.org/abs/2606.18960) - [pdf](https://arxiv.org/pdf/2606.18960)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, manipulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation
- 作者：Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, Weiming Li, Dong Wang, Huchuan Lu, Xu Jia
- 出版日期：2026-06-17
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2606.18960, PDF: https://arxiv.org/pdf/2606.18960

### 一句话总结
提出记忆增强的世界模型 Mem-World，通过4D腕部视角表面元索引记忆（W-VMem）解决机器人持续操作任务中场景细节遗忘和幻觉问题，提升长时程预测与策略评估性能。

### 研究问题
在持续操作世界中模型的预测中，末端执行器频繁遮挡和腕部相机快速运动导致当前观测不足以预测未来视角，模型容易遗忘或幻觉先前帧的场景细节，而现有记忆检索策略难以在动态操作场景中识别信息丰富的历史帧。

### 核心思路/方法
提出 Mem-World，核心组件为 W-VMem——一种以腕部视角为中心的4D表面元索引记忆结构，将历史观测锚定到随时间演变的表面元素上。通过显式建模场景元素被观测的时间与空间位置，基于未来动作条件进行几何感知的历史帧检索。生成时，利用表面元渲染与评分策略选择信息丰富且不冗余的历史帧作为预测上下文。

### 主要贡献
1. 提出 Mem-World，一种记忆增强的多视图动作条件世界模型，实现复杂操作场景的持续预测。
2. 提出 W-VMem，一种4D腕部视角表面元索引记忆，支持几何感知的历史帧检索。
3. 实验表明：相比 Ctrl-World，Mem-World 在长短时程任务中生成更可靠的持续 rollout，策略评估的 Pearson 相关系数提升14.5%；通过合成数据增强，长时程任务成功率从58%提升至72%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对机器人操作中世界模型预测的持续性问题（遮挡与运动导致的遗忘/幻觉），提出创新的4D记忆结构，在策略评估和策略改进任务上均有显著量化提升（相关系数增长14.5%，成功率提升14个百分点），对具身智能领域有较大借鉴价值。

</details>

<details>
<summary>Abstract</summary>

Action-conditioned world models have emerged as a promising paradigm for robot learning, offering a scalable alternative to costly real-world experimentation by generating action-consistent video rollouts. However, persistent world modeling remains challenging in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the current observation insufficient for predicting future views, causing models to forget or hallucinate scene details seen in earlier frames. Existing memory retrieval strategies often fail to identify informative history in dynamic manipulation scenarios. To address this limitation, we propose Mem-World, a memory-augmented multi-view action-conditioned world model. At its core, we present W-VMem, a 4D wrist-view-centered surfel-indexed memory that anchors historical observations to temporally evolving surface elements. By explicitly modeling when and where scene elements are observed, W-VMem enables geometry-aware retrieval of relevant history frames conditioned on future actions. During generation, relevant history frames are selected via surfel-based rendering and scoring, providing informative and non-redundant context for prediction. Extensive experiments show that Mem-World generates persistent rollouts in complex manipulation scenarios, enables more reliable policy evaluation than Ctrl-World, improving the Pearson correlation with real-world performance by 14.5\%, and supports effective policy improvement through synthetic data generation, increasing success rates from 58\% to 72\% on long-horizon tasks.

</details>

#### 2026-06-17 - A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks

**Authors:** Kui Yang, Xianlei Long, Haoxuan Li, Yan Ding, Chao Chen
**Links:** [abs](https://arxiv.org/abs/2606.18646) - [pdf](https://arxiv.org/pdf/2606.18646)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks  
- 作者：Kui Yang, Xianlei Long, Haoxuan Li, Yan Ding, Chao Chen  
- 出版日期：2026-06-17  
- 分类：具身智能 / 机器人学 / AR应用  
- 链接：https://arxiv.org/abs/2606.18646  

### 一句话总结
本文提出了BestMan，一个可扩展的“真实-仿真-真实”具身智能平台，通过自动化场景生成、仿真引导的任务形式化与技能学习架构、以及硬件无关的统一中间件，解决家庭移动操作任务在真实与仿真环境之间无缝迁移的关键挑战。

### 研究问题
如何在非结构化的家庭环境中，实现真实到仿真再到真实的低成本、高保真、可兼容的无缝迁移，从而高效开发、集成和部署移动操作策略。

### 核心思路/方法
1. **自动化场景生成模块**：从真实观测自动重建高保真仿真场景。  
2. **仿真引导的任务形式化与技能学习架构**：支持在仿真中灵活集成和规模化评估混合技能策略。  
3. **硬件无关的统一中间件**：确保跨异构移动操作机器人的兼容性，实现仿真到真实的无缝迁移。

### 主要贡献
- 提出BestMan平台，首次在真实-仿真-真实全周期中实现可扩展的无缝迁移。  
- 设计自动化场景生成模块，降低仿真场景重建成本。  
- 提出仿真引导的任务形式化与技能学习架构，支持混合策略的灵活集成与大规模评估。  
- 开发硬件无关的统一中间件，提升真实部署的可扩展性与兼容性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该研究直面具身智能领域“真实-仿真-真实”迁移的核心瓶颈，提出的三大模块（自动化场景生成、仿真引导学习、硬件无关中间件）具有明确的工程创新和实用价值，且实验证明其在标准基准测试中表现优异。适合关注具身智能、机器人仿真迁移及家庭操作任务的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Mobile manipulation is a fundamental capability in embodied intelligence robotics. The growing demand for robust and generalizable manipulation in unstructured household environments has driven rapid progress in embodied intelligence platforms. However, achieving a seamless transfer across the real-to-sim-to-real cycle faces three key challenges, including costly high-fidelity simulation scenes reconstruction, the complexity of systematic strategy evaluation in simulation, and incompatible real-world deployments. To address these challenges, we develop BestMan, a scalable and seamless real-to-sim-to-real platform that bridges the gap between the simulation and the real world, enabling effective strategy development, integration, and deployment for household mobile manipulation. Specifically, we design a novel Automated Scene Generation (ASG) module to reconstruct realistic simulations from real observations. Then, we propose a simulation-guided task formalization and skill learning architecture that supports the flexible integration and large-scale evaluations of hybrid skill strategies in simulation. Finally, to enhance the real-world scalability, we develop a Hardware-agnostic and Unified Middleware (HUM) to ensure seamless and compatible sim-to-real transfer across heterogeneous mobile manipulators for real deployments. Experimental results demonstrate the superior performance of our proposed platform in establishing standardized benchmarks and facilitating promising research in the field of mobile manipulation.

</details>

#### 2026-06-16 - OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation

**Authors:** Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang
**Links:** [abs](https://arxiv.org/abs/2606.17536) - [pdf](https://arxiv.org/pdf/2606.17536)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation
- 作者：Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang
- 出版日期：2026-06-16T05:25:55Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.17536

### 一句话总结
本文提出名为DRIVE-CHOREO的LLM编排多智能体世界模型，通过统一潜在共压缩机制解决多视角驾驶视频生成中异构控制注入和后处理跨视角融合问题，在nuScenes上取得新SOTA。

### 研究问题
自主驾驶生成式世界模型面临两个未解决冲突：1）异构控制注入——自然语言、高清地图、轨迹、相机位姿等表征空间不兼容；2）后处理跨视角融合——每个相机的潜在编码无法编码全局3D几何。

### 核心思路/方法
核心思想是将可控多视角视频生成重新定义为潜在编排（latent choreography），使用三个Qwen2.5-VL智能体协作：
- **Director**（导演）：将用户意图解析为结构化WorldScript。
- **Cartographer**（制图师）：将WorldScript转化为空间锚定的布局标记。
- **Auditor**（审核员）：提供跨视角反馈作为辅助监督。
三个智能体共同生成一个位置感知的标记序列，该序列通过视图-时间排列与多视角视频共压缩，在3D VAE的卷积感受野中强制实现相机间几何一致性。

### 主要贡献
1. 提出DRIVE-CHOREO方法，将LLM编排与多智能体世界模型结合，统一处理语言、几何和像素的潜在对齐。
2. 在nuScenes数据集上，多视角一致性和BEV mAP达到新SOTA（21.6），FVD为45.7。
3. 纯用合成数据训练的检测器在真实验证集上获得+2.4 NDS提升，验证了下游实用性。

### 局限性
摘要未提供不足够信息：未提及计算开销、对异常场景的鲁棒性、模型在不同天气/光照条件下的泛化能力，以及智能体协作的具体失败案例分析。

### 阅读优先级
**中**。该工作结合LLM与生成式世界模型，在自动驾驶视频生成和多视角一致性问题上有显著改进，但属于较专业的分支领域。若研究方向与多模态视频生成、world model、自动驾驶仿真相关，则阅读优先级可提升。

</details>

<details>
<summary>Abstract</summary>

Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-choreographed multi-agent world model that recasts controllable multi-view video generation as latent choreography. Three Qwen2.5-VL agents - a Director parsing user intent into a structured WorldScript, a Cartographer grounding it into spatially-anchored layout tokens, and an Auditor feeding cross-view critiques back as auxiliary supervision - jointly author a single position-aware token sequence. This sequence is co-compressed with the multi-view video via a view-time permutation that enforces inter-camera geometry within the convolutional receptive field of a 3-D VAE. On nuScenes, DRIVE-CHOREO sets new state-of-the-art multi-view consistency and BEV mAP (21.6) with competitive FVD (45.7); a detector trained purely on our synthetic data gains +2.4 NDS on the real validation split, validating downstream utility.

</details>

#### 2026-06-16 - AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation

**Authors:** Haoran Lu, Mutian Shen, Shuyang Yu, Yu Xiao, Songling Liu, Jianshu Zhang, Shang Wu, Yue Chen, Guo Ye, Jiayi Wang, Zhaoran Wang, Han Liu
**Links:** [abs](https://arxiv.org/abs/2606.17446) - [pdf](https://arxiv.org/pdf/2606.17446)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation
- 作者：Haoran Lu, Mutian Shen, Shuyang Yu, Yu Xiao, Songling Liu, Jianshu Zhang, Shang Wu, Yue Chen, Guo Ye, Jiayi Wang, Zhaoran Wang, Han Liu
- 出版日期：2026-06-16
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.17446

### 一句话总结
AnnotateAnything 是一个通用自动标注框架，能将仅有几何结构的3D资产转换为附带语义、交互和物理操控标签的资产，支持机器人仿真数据收集。

### 研究问题
如何为机器人仿真中的原始3D资产自动生成结构化、多样化且可执行的操控标签（如抓取姿态、灵巧接触点、关节运动路径等），以替代仅依赖几何信息的被动资产。

### 核心思路/方法
构建两条互补的标注流水线：
1. **统一视觉-语言标注流水线**：利用视觉语言推理推断物体语义、交互约束和3D线索，提供人类先验指导以识别有意义的交互区域。
2. **全自动大规模并行物理标注流水线**：在视觉语言先验的基础上，通过候选生成、几何优化和轨迹生成，将先验信息与每个资产的几何及物理约束结合，生成多样化可执行的动作注释。

此外，基于生成的注释构建异步并行仿真数据收集系统，支持多种物体、任务和机器人形态。

### 主要贡献
- 提出了一个通用自动标注框架，将被动3D资产转化为“操控就绪”的资产。
- 设计了两条互补的标注流水线（视觉-语言推理管线 + 物理标注管线），兼顾语义先验和物理可执行性。
- 实验表明，该框架在标注效率、数据收集效率和任务成功率上均优于现有标注和数据生成流水线。
- 支持下游任务如功能区域检测、机器人视觉问答和视觉指令微调。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接面向机器人操作领域的核心瓶颈（3D资产缺乏交互语义标签），提出了通用自动化解决方案，并展现了跨多任务和机器人形态的实用性。摘要明确提供了与现有方法的性能对比，且计划开源代码和基准，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Simulation enables scalable robot data collection, but raw 3D assets provide only geometry, lacking the semantic, interactive, and physical knowledge needed to specify where and how robots should act. In this work, we present AnnotateAnything, a general automatic annotation framework that converts passive 3D assets into manipulation-ready assets with structured, diverse, and executable manipulation labels. AnnotateAnything is built around two complementary pipelines. First, a unified visual-language annotation pipeline using vision-language reasoning to infer object semantics, interaction constraints, and 3D-grounded cues, providing human-prior guidance for identifying meaningful interaction regions. Second, a fully automatic and massively parallel physics annotation pipeline grounds these priors in each asset's geometry and physical constraints through candidate generation, geometry optimization and trajectory generation. This pipeline produces diverse and executable action annotations, including grasp poses, dexterous contacts, articulation waypoints, insertion directions, hanging affordances, and navigation targets. Using the generated annotations, we further build an asynchronous parallel simulation data-collection system across diverse objects, tasks, and robot embodiments. Experiments demonstrate that AnnotateAnything achieves superior annotation efficiency, data-collection efficiency, and task success rates over existing annotation and data-generation pipelines, while also supporting downstream tasks such as affordance detection, robotic VQA, and visual instruction finetuning. We provide project materials on the project page and plan to release the full code, annotations, and benchmark to facilitate future research. Videos, code, demo assets, and annotations are provided in supplementary materials Project page: https://tourmaline-caramel-169490.netlify.app.

</details>

#### 2026-06-15 - Geometric Action Model for Robot Policy Learning

**Authors:** Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
**Links:** [abs](https://arxiv.org/abs/2606.17046) - [pdf](https://arxiv.org/pdf/2606.17046)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric foundation model, manipulation, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometric Action Model for Robot Policy Learning  
- 作者：Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong  
- 出版日期：2026-06-15  
- 分类：Embodied / Robotics / AR Applications  
- 链接：[摘要](https://arxiv.org/abs/2606.17046) | [PDF](https://arxiv.org/pdf/2606.17046)  

### 一句话总结  
本文提出**几何动作模型（GAM）**，通过复用预训练几何基础模型（GFM）作为共享骨干，实现语言条件下的机器人操作策略学习，在仿真和真实实验中表现优于现有方法。

### 研究问题  
如何让机器人策略在遵循语言指令时，有效利用3D几何信息处理接触丰富的操作任务，而不依赖传统2D图像或2D衍生潜空间。

### 核心思路/方法  
1. **模型结构**：将预训练的几何基础模型（GFM）在中间层拆分——浅层作为观测编码器，插入因果未来预测器以预测语言、本体感知和动作历史条件下的未来潜在token；深层GFM模块则用于特征传播和动作解码，最终同时输出未来几何和动作。  
2. **设计特点**：通过最小架构修改赋予GFM语言条件化的时序世界建模能力，同时保留其丰富的几何先验。

### 主要贡献  
1. 提出GAM，直接复用GFM作为感知、时序预测和动作解码的统一基座。  
2. 通过拆分GFM并插入因果预测器，实现语言条件化的时序世界建模，无需大幅改动模型结构。  
3. 在多个仿真和真实机器人操作基准上，GAM在精确度、鲁棒性、速度和模型轻量化方面均超越当前基础模型规模的基线方法。

### 局限性  
摘要未提供实验的失败案例、泛化边界或计算资源要求等具体局限性信息。

### 阅读优先级  
**高**  
理由：该工作针对机器人操作中的3D几何建模这一核心难题，提出了创新且高效的轻量化解决方案，实验涵盖仿真和真实场景，结果全面优于基线，对具身智能及机器人学习领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world. Recent vision-language-action models (VLAs) and video world-action models (WAMs) inherit strong semantic or temporal priors from large-scale foundation models, but they still operate primarily on 2D image frames or 2D-derived latent spaces, leaving implicit the 3D geometry required for contact-rich manipulation. We propose the Geometric Action Model (GAM), a language-conditioned manipulation policy that directly repurposes a pretrained geometric foundation model (GFM) as a shared substrate for perception, temporal prediction, and action decoding. GAM splits the GFM at an intermediate layer: the shallow layers serve as an observation encoder, and a causal future predictor inserted at the split layer forecasts future latent tokens conditioned on language, proprioception, and action history. The predicted future tokens are then routed through the remaining GFM blocks for feature propagation and decoding, allowing a single backbone to produce both future geometry and actions. This design equips the GFM with language-conditioned temporal world modeling through minimal architectural modification while preserving its rich geometric priors. Across a broad suite of simulation and real-robot manipulation benchmarks, GAM is more accurate, more robust, faster, and lighter than current foundation-model-scale baselines.

</details>

#### 2026-06-15 - R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies

**Authors:** Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu
**Links:** [abs](https://arxiv.org/abs/2606.17040) - [pdf](https://arxiv.org/pdf/2606.17040)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies
- 作者：Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.17040

### 一句话总结
R2RDreamer 提出一种真实到真实的数据增强框架，通过结合轻量级3D编辑和2D视频补全，在不引入模拟-真实差距的前提下，提升基于RGB的2D操控策略的空间泛化能力。

### 研究问题
如何从少量真实演示中通过数据增强，使基于RGB的2D操控策略（如扩散策略和视觉-语言-动作策略）在目标物体姿态、机器人配置和相机视角发生空间偏移时仍能保持泛化能力？

### 核心思路/方法
R2RDreamer 采用两阶段策略：首先，在共享3D空间中执行轻量级3D增强，包括编辑不完整的物体点云和末端执行器轨迹；然后，利用遮挡感知推理将编辑后的场景投影为带掩码的图像空间控制视频，并通过一个稠密控制的图像到视频模型，补全出时间上连贯的RGB观测。整个过程无需强3D场景解析或完整的几何补全，且直接生成适用于2D RGB策略的数据。

### 主要贡献
1. 提出首个面向2D RGB策略的真实到真实数据增强框架，兼顾3D动作-观测的几何一致性与2D视频空间的可视化完整性。
2. 设计了一种结合轻量级3D编辑、遮挡感知投影和稠密控制视频补全的流水线，避免复杂环境配置和模拟-真实鸿沟。
3. 在空间偏移操控任务上，通过扩散策略和视觉-语言-动作策略验证了该方法能显著提升空间泛化能力，并分别分析了3D编辑、遮挡感知投影和视频补全三个模块的贡献。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对2D RGB策略的数据增强问题提出实用方案，结合3D和2D优势，避免模拟-真实差距，且在两种主流策略（扩散策略和视觉-语言-动作策略）上进行了验证，对从事机器人操控、模仿学习及数据增广的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial generalization is critical for imitation-learned manipulation policies, but achieving it typically requires scaling demonstrations across diverse object poses, robot configurations, and camera viewpoints. Data augmentation from a few source demonstrations offers a practical alternative to costly real-world collection. Simulation-based augmentation can create controllable variation, but requires complex environment and object setup and may introduce a sim-to-real gap. Recent real-to-real methods avoid these issues by jointly editing 3D observations and action trajectories from real demonstrations, yet they still rely on strong 3D scene parsing and geometry completion, and often produce observations tailored to 3D pointcloud policies rather than RGB-based 2D policies. We propose R2RDreamer, a real-to-real demonstration augmentation framework that preserves the geometric consistency of 3D action-observation editing while moving visual completion to 2D video space. Specifically, R2RDreamer first performs lightweight 3D augmentation by editing incomplete object pointclouds and end-effector trajectories in a shared 3D frame; it then projects the edited scene into masked image-space control videos with occlusion-aware reasoning and uses a dense-control image-to-video model to complete temporally coherent RGB observations. Experiments on spatially shifted manipulation tasks with both 2D diffusion-style policies and vision-language-action policies show that R2RDreamer improves spatial generalization from limited source demonstrations, with analyses validating the contributions of 3D editing, occlusion-aware projection, and video completion.

</details>

#### 2026-06-15 - Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation

**Authors:** Jie Zhang, Xiaoyue Chen, Anzhe Chen, Dayiheng Liu, Deqing Li, Gengze Zhou, Hale Yin, Haoqi Yuan, Haoyang Li, Jiahao Li, Jiazhao Zhang, Jingren Zhou, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Pei Lin, Qihang Peng, Shengming Yin, Tianhe Wu, Tianyi Yan, Xiao Xu, Yan Shu, Yanran Zhang, Ye Wang, Yi Wang, Yilei Chen, Yixian Xu, Yiyang Huang, Yuxiang Chen, Zekai Zhang, Zhendong Wang, Zixing Lei, Zhixuan Liang, Zihao Liu, Zikai Zhou, Chenxu Lv, Xiong-Hui Chen, Chenfei Wu
**Links:** [abs](https://arxiv.org/abs/2606.17030) - [pdf](https://arxiv.org/pdf/2606.17030)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, autonomous driving, mapping, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation
- 作者：Jie Zhang, Xiaoyue Chen, 等（共37位作者）
- 出版日期：2026-06-15
- 分类：具身智能/机器人/增强现实应用
- 链接：摘要: https://arxiv.org/abs/2606.17030 ；PDF: https://arxiv.org/pdf/2606.17030

### 一句话总结
本文提出Qwen-RobotWorld，一个以自然语言为统一接口的语言条件视频世界模型，用于预测多种具身任务（如机器人操作、自动驾驶等）的未来视觉轨迹。

### 研究问题
如何构建一个统一的、语言条件驱动的具身世界模型，使其能够在多种具身场景（机器人操作、自动驾驶、室内导航、人机转移）中生成物理上合理的未来视觉预测，并支持策略训练、策略评估和下游控制等应用。

### 核心思路/方法
论文提出三部分设计：
1. **双流MMDiT与多模态大语言模型动作编码**：使用60层双流扩散Transformer，通过逐层联合注意力机制融合Qwen2.5-VL（冻结）的语义信息和视频-VAE的潜在表示。
2. **具身世界知识库（Embodied World Knowledge, EWK）**：包含860万视频-文本对（超过2亿帧）的大规模语料库，覆盖20多种具身形态和500多个动作类别，并具有动作-语言映射。
3. **通用+专家渐进课程（General+Expert Progressive Curriculum）**：两阶段训练策略，先学习通用视觉先验，再通过共享语言接口注入具身专业知识。

### 主要贡献
- 提出了统一的语言条件视频世界模型，在多个具身任务中表现优异。
- 构建了大规模具身世界知识库（EWK），支持多形态多动作。
- 在多个基准上取得领先结果：EWMBench和DreamGen Bench排名第一，WorldModelBench和PBench上优于所有开源模型，RoboTwin-IF上的零样本分析也展示了强大的泛化能力和多视角一致性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作提出了一个统一的具身世界模型框架，在多个重要基准上取得了SOTA结果，且包含大规模数据构建和渐进训练策略，对具身智能、视频生成和世界模型方向的学者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge (EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+ embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a two-stage training strategy that first learns general visual priors and then injects embodied specialization under a shared language interface. Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-IF benchmark further support robust generalization and multi-view consistency.

</details>

#### 2026-06-15 - DreamX-World 1.0: A General-Purpose Interactive World Model

**Authors:** DreamX Team, Yancheng Bai, Rui Chen, Xiangxiang Chu, Rujing Dang, Hao Dou, Bingjie Gao, Qiwen Gu, Siyu Hong, Jiachen Lei, Geng Li, Jifan Li, Ruimin Lin, Qingfeng Shi, Bingze Song, Lei Sun, Jing Tang, Ruitian Tian, Jun Wang, Jiahong Wu, Pengfei Zhang, Shen Zhang, Jiashu Zhu
**Links:** [abs](https://arxiv.org/abs/2606.16993) - [pdf](https://arxiv.org/pdf/2606.16993)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DreamX-World 1.0: A General-Purpose Interactive World Model
- 作者：DreamX Team, Yancheng Bai, Rui Chen, Xiangxiang Chu, Rujing Dang, Hao Dou, Bingjie Gao, Qiwen Gu, Siyu Hong, Jiachen Lei, Geng Li, Jifan Li, Ruimin Lin, Qingfeng Shi, Bingze Song, Lei Sun, Jing Tang, Ruitian Tian, Jun Wang, Jiahong Wu, Pengfei Zhang, Shen Zhang, Jiashu Zhu
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.16993

### 一句话总结
DreamX-World 1.0是一个通用的交互式文本/图像到视频世界模型，支持可控的长时序生成，在5秒基础评测中总体得分84.76，优于HY-WorldPlay 1.5和LingBot-World。

### 研究问题
如何构建一个通用、可控、支持长时序交互的世界模型，同时实现相机导航、事件控制、多域生成（逼真、游戏风格、风格化）和高帧率推理。

### 核心思路/方法
1. **数据引擎**：结合相机精确的Unreal Engine渲染、动作丰富的游戏录像和恢复相机几何的真实世界视频。
2. **相机控制**：提出E-PRoPE，一种轻量级投影位置编码变体，在保持PRoPE投影几何的同时进行相机感知注意力。
3. **自回归世界模型**：通过因果强制、DMD风格蒸馏和长序列训练，将双向视频生成器转化为几步自回归世界模型。
4. **记忆条件场景持久性**：通过基于相机几何的检索恢复早期视图，减少跨自回归块的颜色漂移。
5. **事件指令微调**：添加可组合的事件控制；强化学习对齐恢复蒸馏后的相机控制和视觉质量。
6. **高效推理**：混合精度DiT、残差重用、75%剪枝VAE解码和异步流水线并行，在8块RTX 5090上达到16 FPS。

### 主要贡献
- 提出通用交互式世界模型，支持长时序、相机控制和事件指令。
- 引入E-PRoPE编码和记忆条件场景持久性机制，提升长时序生成稳定性。
- 通过训练和推理优化（蒸馏、残差重用、剪枝等）实现16 FPS实时推理。
- 在5秒评测中取得84.76总分，优于对比方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作针对世界模型的可控生成和高效推理有明确技术贡献，适合关注交互式视频生成、世界模型或实时推理的读者；但摘要未列出具体实验设置和基线对比细节，作为应用方向的论文，重要程度中等。

</details>

<details>
<summary>Abstract</summary>

DreamX-World 1.0 is a general-purpose interactive text/image-to-video world model for controllable long-horizon generation. It supports camera navigation, revisits to previously observed regions, and promptable events across photorealistic, game-style, and stylized domains. Our data engine combines camera-accurate Unreal Engine rendering, action-rich gameplay recordings, and real-world videos with recovered camera geometry. For camera control, we introduce E-PRoPE, a lightweight variant of projective positional encoding that retains PRoPE's projective camera geometry while applying camera-aware attention to spatially reduced tokens. We convert a bidirectional video generator into a few-step autoregressive world model using causal forcing, DMD-style distillation, and long-rollout training. Training on self-generated long-horizon contexts exposes the model to its own generated history and reduces the style and color drift that accumulates across autoregressive chunks. Memory-Conditioned Scene Persistence retrieves earlier views through camera-geometry-based retrieval, while residual recycling makes the conditioning path less sensitive to imperfect memory latents. Event Instruction Tuning adds composable event control, and reinforcement learning alignment recovers camera control and visual quality after distillation. With mixed-precision DiT execution, residual reuse, 75\%-pruned VAE decoding, and asynchronous pipeline parallelism, DreamX-World 1.0 reaches up to 16\,FPS on eight RTX\,5090 GPUs. On our 5-second basic evaluation, DreamX-World 1.0 achieves a camera-control score of 73.75 and an overall score of 84.76, outperforming HY-WorldPlay 1.5 and LingBot-World in overall score, which achieve 80.79 and 80.45, respectively.

</details>

#### 2026-06-15 - Latent Space Reinforcement Learning for Inverse Material Estimation in Food Fracture Simulation

**Authors:** Adrian Ramlal, Yuhao Chen, John S. Zelek
**Links:** [abs](https://arxiv.org/abs/2606.16870) - [pdf](https://arxiv.org/pdf/2606.16870)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Latent Space Reinforcement Learning for Inverse Material Estimation in Food Fracture Simulation
- 作者：Adrian Ramlal, Yuhao Chen, John S. Zelek
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.16870

### 一句话总结
本文提出了一个基于潜空间强化学习的框架，通过目标条件策略在不可微的食品断裂模拟器中高效估计材料参数，以橘子剥皮为例，验证了方法的有效性。

### 研究问题
如何从目标断裂行为描述中，反向估计非均匀食品材料（如橘子）的不可微材料参数，并实现任意目标无需重训练的通用逆映射。

### 核心思路/方法
1. 在不可微的连续损伤力学模拟器上，训练一个神经网络代理（使用2000次前向模拟）。
2. 比较CMA-ES（无梯度进化优化器）与PPO（强化学习算法）在原始9维参数空间和两个学习到的4维潜空间上的表现。
3. 训练一个目标条件的PPO策略，学习通用逆映射：给定任意目标剥皮行为描述，该策略可在单次前向传递（约10ms，8次代理评估）中输出材料参数估计。
4. 使用归一化流潜空间与共享代理评估器，并引入热启动扩展（从策略输出初始化CMA-ES细化）进一步提升恢复精度。

### 主要贡献
- 提出了一种基于潜空间强化学习的逆材料估计框架，能在不可微模拟器中高效运行。
- 目标条件PPO策略在模拟器验证中实现0.642的实际恢复率，比原始参数空间提升23%。
- 热启动CMA-ES细化将恢复率提升至0.828（使用540次评估），为食品物理逆向问题提供了实用方案。

### 局限性
摘要未提供足够信息：未讨论方法在非食品场景或不同断裂类型上的泛化性、对噪声或观测误差的鲁棒性、以及计算资源需求等局限性。

### 阅读优先级
高  
理由：该工作将强化学习与潜空间表示结合，解决了食品模拟中不可微逆参数估计的实际问题，方法清晰且有量化性能提升（23%），对机器人、食品科学和计算机视觉领域的交叉研究有参考价值。

</details>

<details>
<summary>Abstract</summary>

Realistic visual simulation of food manipulation requires accurate material parameters, yet these are difficult to measure directly and vary across the heterogeneous regions of a single food item. We address the inverse problem of estimating material parameters from a target description of fracture behavior in a non-differentiable continuum damage mechanics simulator. Using orange peeling as a test case, we train a neural surrogate on 2,000 forward simulations and compare Covariance Matrix Adaptation Evolution Strategy (CMA-ES, a gradient-free evolutionary optimizer) with Proximal Policy Optimization (PPO, a reinforcement learning algorithm) across the original 9-dimensional parameter space and two learned 4-dimensional latent representations. Since different oranges have different material properties, a practical inverse system must handle arbitrary targets without retraining. We train a goal-conditioned PPO policy that learns a general inverse mapping: given any target description of peeling behavior, the policy produces a material parameter estimate in a single forward pass (8 surrogate evaluations, approximately 10ms). Operating in a normalizing flow latent space with a shared surrogate evaluator, the goal-conditioned policy achieves 0.642 actual recovery when validated through the simulator, outperforming the original parameter space by 23%. A warm-start extension that initializes CMA-ES refinement from the policy's output further improves recovery to 0.828 with 540 evaluations. These findings provide a practical framework for inverse food physics and lay groundwork for vision-driven material identification from video observations of food manipulation.

</details>

#### 2026-06-15 - Automated Digital Twin Construction for Highway Scenarios Using LiDAR Point Clouds and OpenStreetMap

**Authors:** Yongqi Zhao, Dong Bi, Paul Kovacevic, Tomislav Mihalj, Martin Schabauer, Johannes Betz, Arno Eichberger
**Links:** [abs](https://arxiv.org/abs/2606.16570) - [pdf](https://arxiv.org/pdf/2606.16570)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Automated Digital Twin Construction for Highway Scenarios Using LiDAR Point Clouds and OpenStreetMap
- 作者：Yongqi Zhao, Dong Bi, Paul Kovacevic, Tomislav Mihalj, Martin Schabauer, Johannes Betz, Arno Eichberger
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.16570

### 一句话总结
提出一种自动化工作流，融合LiDAR点云与OpenStreetMap数据，生成符合ASAM OpenDRIVE标准的高速公路数字孪生地图，减少了手动干预需求。

### 研究问题
如何高效、低成本地从真实传感器数据（LiDAR点云）和开源地图（OSM）中自动构建高速公路场景的标准化道路地图（ASAM OpenDRIVE格式），以支持自动驾驶系统的仿真与验证。

### 核心思路/方法
1. 利用移动测绘LiDAR点云精确提取车道级几何信息，但仅覆盖扫描路径范围。  
2. 结合OpenStreetMap提供的广泛道路网络拓扑，弥补LiDAR在未覆盖区域（如匝道）的几何缺失。  
3. 自动化管道中：从LiDAR测量重建主线路段；从OSM道路图推断匝道几何与拓扑结构，从而完整建模高速公路立交，无需全面传感器覆盖。  
4. 最终生成地理参考的ASAM OpenDRIVE地图。

### 主要贡献
- 提出融合LiDAR精确几何与OSM拓扑的自动化数字孪生构建管道，仅需最小手动干预。  
- 实验证明平均横向均方根误差（RMSE）为0.740米，且生成地图可直接用于主流仿真平台（IPG CarMaker和Esmini）。  
- 提供了开源代码（GitHub仓库）。

### 局限性
摘要未提供足够信息，无法确定具体局限性（如对特定道路类型的适用性、计算效率、大场景扩展性等），需要阅读全文。

### 阅读优先级
- 优先级：中  
- 理由：该工作针对自动驾驶仿真中的地图生成问题，提出实用的传感器融合方案（LiDAR+OSM），结果有定量误差指标和仿真验证，且代码开源。适合对数字孪生、地图自动化构建或自动驾驶仿真感兴趣的读者。但摘要未披露与纯LiDAR方法或纯OSM方法的全面对比，以及局限性细节，故优先级设为中等。

</details>

<details>
<summary>Abstract</summary>

Accurate road environment modeling is fundamental to the simulation and validation of automated driving systems. However, constructing road maps in standardized formats such as ASAM OpenDRIVE from real-world sensor data remains a time-consuming and costly process. Mobile mapping LiDAR captures accurate lane-level geometry but is confined to the driven corridor, while OpenStreetMap (OSM) provides broad road network topology but lacks geometric precision at the lane level. To address this, an automated workflow is proposed to fuse LiDAR point clouds with OSM data to generate georeferenced ASAM OpenDRIVE maps of highway environments, requiring minimal manual intervention. The pipeline reconstructs mainline roads from LiDAR-derived measurements and infers ramp geometry and topology from the OSM road graph, enabling complete highway interchange modeling without full sensor coverage. Experiments demonstrate a mean lateral RMSE of 0.740 m, and the generated maps are directly usable in mainstream simulation platforms including IPG CarMaker and Esmini. These results validate the effectiveness of combining measurement-derived geometry with map-derived topology for automated OpenDRIVE digital twin generation. The project code is available at https://github.com/ftgTUGraz/opendrive-digital-twin-generator

</details>

#### 2026-06-15 - PROSE: Training-Free Egocentric Scene Registration with Vision-Language Models

**Authors:** Zhiang Chen, Nahyuk Lee, Boyang Sun, Taein Kwon, Marc Pollefeys, Zuria Bauer, Sunghwan Hong
**Links:** [abs](https://arxiv.org/abs/2606.16569) - [pdf](https://arxiv.org/pdf/2606.16569)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** AR, digital twin, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PROSE: Training-Free Egocentric Scene Registration with Vision-Language Models
- 作者：Zhiang Chen, Nahyuk Lee, Boyang Sun, Taein Kwon, Marc Pollefeys, Zuria Bauer, Sunghwan Hong
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications (具身智能/机器人/增强现实应用)
- 链接：https://arxiv.org/abs/2606.16569

### 一句话总结
PROSE 是一种无需训练、仅依赖 RGB 视觉语言模型的自我中心场景配准方法，通过将视频序列转化为对象级 3D 场景图并利用 VLM 进行跨扫描匹配，在无需深度传感器或注释的情况下实现优于传统几何和深度学习方法的效果。

### 研究问题
如何仅通过 RGB 图像对两个不同时间拍摄的自我中心室内场景进行鲁棒且可扩展的配准，而无需深度传感器、预训练匹配器或标注的场景图。

### 核心思路/方法
1.  **场景图生成**：利用现成的几何、分割和语言基础模型，将每个 RGB 序列提升为对象级 3D 场景图。
2.  **跨序列匹配**：使用同一个预训练的视觉语言模型（VLM）来匹配两个 RGB 序列中的对象实例。具体通过对象高度作为先验来缩小匹配范围，并通过成对的相同/不同查询来验证匹配提案。
3.  **刚性变换估计**：为每个匹配对象假设一个候选变换，并选择几何一致性最强的变换作为最终结果。整个过程无需添加任何可学习参数，也不需要深度传感器、训练或标注图。

### 主要贡献
- 提出了一种全新的、完全无需训练的RGB-only自我中心场景配准范式，避开了传统方法对稀疏几何或预训练图匹配的依赖。
- 有效利用预训练VLM的跨扫描匹配能力，结合对象高度先验和配对验证查询，使匹配过程变得可靠。
- 在Aria Digital Twin和Aria Everyday Activities基准测试中，该方法在配准精度上优于几何基线和基于学习场景图的方法，且生成的场景图可直接用于下游任务。

### 局限性
摘要未提供足够信息。例如，未讨论该方法对VLM性能的依赖性、在极端遮挡或光照变化下的鲁棒性、计算成本，以及是否在所有场景中都优于基线方法。

### 阅读优先级
高。理由：该工作提出了一种新颖的、轻量级（无训练）的自我中心场景配准方案，直接针对该领域的关键挑战（无深度、无标注、视图模糊）给出了独特的解决路径，并在多个基准上取得了领先性能。对于从事机器人空间记忆、AR系统以及具身智能的研究者具有重要参考价值。即使摘要未提供全部细节，其核心思路的创新性和实用性已经足够突出。

</details>

<details>
<summary>Abstract</summary>

Registering two captures of the same indoor space taken at different times underpins persistent spatial memory for robots and AR systems, yet the realistic version of this task is egocentric and its most scalable form is RGB-only. Head-mounted cameras yield blurry, fast-moving, partially overlapping views from which dense geometry is hard to recover. Classical registration leans on exactly the clean point clouds this setting lacks, while learned scene-graph methods require a pre-built or annotated graph and a trained matcher that we find brittle under egocentric data. We take a different route, using a pretrained vision-language model as the source of both scene understanding and cross-scan matching. Our method, PROSE (Prompted Scene rEgistration), lifts each RGB sequence into an object-level 3D scene graph using off-the-shelf foundation models for geometry, segmentation, and language, then prompts the same VLM to match object instances across the two RGB sequences. To make this matching tractable and reliable, we leverage object heights as a prior and verify each proposed match with a paired same/different query, then solve for the rigid transform by hypothesizing a candidate per matched object and selecting the one with the strongest geometric consensus. PROSE adds no learned parameters and requires no depth sensor, training, or annotated graph. On the egocentric Aria Digital Twin and Aria Everyday Activities benchmarks, it outperforms both geometric and learned scene-graph baselines in registration accuracy, on ground-truth and RGB-reconstructed point clouds alike, and the scene graph it produces transfers directly to downstream tasks.

</details>

#### 2026-06-15 - EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video

**Authors:** Hyunjin Kim, Ri-Zhao Qiu, Guangqi Jiang, Xiaolong Wang
**Links:** [abs](https://arxiv.org/abs/2606.16202) - [pdf](https://arxiv.org/pdf/2606.16202)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video
- 作者：Hyunjin Kim, Ri-Zhao Qiu, Guangqi Jiang, Xiaolong Wang
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.16202

### 一句话总结
本文提出EgoPhys框架，能够从第一人称RGB视频中，利用可泛化的先验知识构建可变形物体的物理数字孪生，并支持零样本泛化到未见物体。

### 研究问题
如何仅通过第一人称RGB视频，构建可变形物体（如弹性材料、织物）的物理数字孪生，并实现准确的物理动力学预测与零样本泛化？

### 核心思路/方法
1. **蒸馏逆物理解**：将每个物体的逆物理求解结果蒸馏到紧凑的码本（codebook）中，避免测试时对每个弹簧刚度进行逐点优化。
2. **可泛化先验训练**：利用包含多种可变形物体、场景和操作风格的自我中心交互数据集，训练模型以学习通用先验。
3. **预测密度场**：对未见物体，直接预测密集的弹簧刚度场，实现零样本泛化。
4. **机器人部署验证**：以单个第一人称人类操作视频初始化数字孪生，作为内部世界表征辅助可变形物体规划（在真实xArm6机器人上演示）。

### 主要贡献
- 提出首个能从自我中心RGB视频构建可变形物理数字孪生的框架EgoPhys。
- 通过码本蒸馏与可泛化先验，实现无需测试时优化的零样本泛化。
- 在重建、未来预测和零样本泛化任务上优于基线方法。
- 构建了包含多样化可变形物体、场景和操作风格的自我中心交互数据集。
- 在真实机器人上验证了单次人类操作视频初始化的数字孪生可作为世界模型辅助规划。

### 局限性
摘要未提供足够信息，无法从文本中推断具体局限性。例如，未说明对视频质量、物体种类或光照条件的潜在限制，也未提及计算成本或失败案例。

### 阅读优先级
**高**
理由：该工作将自我中心RGB视频直接用于可变形物体物理建模，结合零样本泛化与机器人规划验证，在具身智能和机器人领域具有明确的应用潜力和创新性。摘要清晰展示了从数据、方法到实际部署的完整链条，对于关注物理仿真、数字孪生或机器人操作的读者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Humans naturally understand object physics through everyday interactions, but faithfully predicting complex deformable dynamics, such as elastic materials and fabrics, remains a major challenge for computer vision and robotics. We present EgoPhys, a framework that constructs deformable physical digital twins from egocentric RGB-only video using generalizable priors. EgoPhys overcomes the limitations of existing methods to enable controllable deformable digital twin generation from egocentric videos by distilling per-object inverse-physics solutions into a compact codebook, enabling prediction of dense spring stiffness fields for unseen objects without per-spring test-time optimization. Trained with generalizable priors from diverse egocentric interactions, EgoPhys outperforms baselines in reconstruction, future prediction, and zero-shot generalization. To support training and evaluation, we curate an egocentric interaction dataset covering diverse deformable objects, scenes, and manipulation styles. We deploy EgoPhys on a real xArm6 robot, demonstrating that a digital twin initialized from a single egocentric human play video can serve as an internal world representation to aid in deformable-object planning, highlighting egocentric RGB observations as a scalable path toward real-to-sim pipelines.

</details>

#### 2026-06-14 - FlashNav: Ultra-Fast Policy Training for Robot Navigation within 20 Seconds

**Authors:** Shanze Wang, Yiwei Qian, Xinming Zhang, Jun Xue, Siwei Cheng, Xianghui Wang, Qingyuan Hu, Xiaoyu Shen, Wei Zhang
**Links:** [abs](https://arxiv.org/abs/2606.15846) - [pdf](https://arxiv.org/pdf/2606.15846)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FlashNav: Ultra-Fast Policy Training for Robot Navigation within 20 Seconds
- 作者：Shanze Wang, Yiwei Qian, Xinming Zhang, Jun Xue, Siwei Cheng, Xianghui Wang, Qingyuan Hu, Xiaoyu Shen, Wei Zhang
- 出版日期：2026-06-14
- 分类：Embodied / Robotics / AR Applications
- 链接：论文摘要 | 论文PDF

### 一句话总结
FlashNav提出一种GPU优先的深度强化学习导航训练框架，将策略训练时间缩短至20秒以内，并能在真实轮式和足式机器人上部署。

### 研究问题
如何大幅降低基于深度强化学习的机器人导航策略的训练时间（从数小时/天缩短至秒级），同时保持策略的可部署性和避障性能。

### 核心思路/方法
核心思路是让仿真环境紧密对齐导航马尔可夫决策过程（MDP），剥离不必要的渲染和高保真物理细节，只保留速度级导航必需组件（占据几何、范围传感、目标条件控制、机器人运动动力学、碰撞处理、终止和重置）。具体实现上，基于批量化位图仿真器和全GPU驻留训练流水线（FastDSAC学习器），完全在GPU上生成大规模并行导航转移样本。

### 主要贡献
1. 提出首个将基于DRL的机器人导航策略训练时间降至秒级的框架，最快部署策略训练时间少于20秒。
2. 通过实验在TurtleBot2和Unitree Go2上展示：在RTX 5090上20秒内达到100%成功率；在多个桌面GPU上训练时间保持在几十秒内。
3. 验证了学得的策略可直接迁移到物理轮式和足式机器人上，在静态和动态室内场景中均有效。

### 局限性
摘要未提供关于方法在复杂动态场景、多障碍物环境或不同传感器配置下的泛化能力；也未提及与其他基线方法的详细对比指标或失败案例。摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作显著降低了机器人导航中深度强化学习的训练时间瓶颈（从小时级到秒级），且进行了真实机器人部署验证，对机器人应用领域具有较强实用价值和启发性。

</details>

<details>
<summary>Abstract</summary>

Deep reinforcement learning has shown strong potential for robot navigation, but its practical deployment is still limited by the long wall-clock cost of policy training. This paper presents FlashNav, a GPU-first framework for ultra-fast range-based robot navigation training. To the best of our knowledge, FlashNav is the first DRL-based robot navigation framework that reaches seconds-level policy training, with the fastest deployable policy trained in less than 20 seconds. The key idea is to align simulation with the navigation MDP: FlashNav preserves the essential components for velocity-level navigation, including occupancy geometry, range sensing, goal-conditioned control, robot motion dynamics, collision handling, termination, and reset, while removing unnecessary rendering and high-fidelity physical details from the training loop. Built on a batched bitmap simulator and a fully GPU-resident training pipeline with our FastDSAC learner, FlashNav generates massive parallel navigation transitions entirely on GPU. Experiments on TurtleBot2 and Unitree Go2 show that FlashNav achieves a 100\% success-rate below 20 seconds on an RTX 5090 and remains within tens of seconds across desktop GPUs. The learned policies further transfer to physical wheeled and legged robots in static and dynamic indoor scenes, demonstrating that DRL-based navigation can be trained at seconds-level speed while preserving deployable obstacle-avoidance behavior.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
