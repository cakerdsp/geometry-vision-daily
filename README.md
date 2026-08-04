# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：58
- 分类分布：
  - Neural Scene Representations & Rendering: 18
  - 3D Reconstruction & Multi-view Geometry: 15
  - Embodied / Robotics / AR Applications: 13
  - Dynamic / 4D Reconstruction: 8
  - Geometry Foundation Models: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**1. 从"像素对齐"到"表面对齐/几何锚定"的表示范式迁移**
昨日多篇论文共同指向一个核心转变：在3D高斯泼溅（3DGS）体系中，固定图像网格的像素对齐预测正被更贴合场景几何结构的表示取代。InfiniSplat（2608.02437）直接提出从像素对齐转向表面对齐，用几何引导采样放置支撑点；StreamSplat（2608.01659）通过体素对齐因果缓存和深度锚定维护几何接地状态；GIFT（2608.02068）则利用非朗伯表面几何不变的先验进行无标签微调。这一趋势表明，几何结构正从前馈重建的隐式副产品变为显式约束与锚定来源。

**2. 前馈3DGS从"多视图"走向"在线流式"与"稀疏/退化输入"**
前馈3DGS正在突破固定多视图输入的假设。StreamSplat（2608.01659）实现了因果流式场景更新，内存随场景几何而非流长度增长；DerainSplat（2608.02191）面对稀疏雨景输入，通过天气因子预测实现干净三维重建；D²-4DGS（2608.01588）在稀疏相机动态重建中融合双源深度先验；UniqueSplat（2608.02145）则按查询视角动态调整高斯分布。这些工作把前馈重建的适用边界推向在线、稀疏和带噪的真实采集条件。

**3. 4D动态重建中的运动建模从"单一多项式"转向"频域分解"**
动态场景的运动建模在过去多依赖单一多项式或简单MLP。FAST-GS（2608.01958）提出傅里叶运动建模，将运动分解为频率正弦分量，分别捕获低频全局轨迹与高频局部细节；ASTRA（2608.02006）则用2D轨迹对齐作为显式与纹理无关的监督，替代弱时间线索的光度匹配。两者均将运动解析视为动态重建的核心复杂度来源，而非配准后的次要问题。

**4. 3DGS加速器/系统层面的"解耦"与"可扩展"设计成为研究重点**
3DGS的渲染管线与数据流正在被重新审视。DeGS（2608.02099）识别出"边检查边混合"数据流是并行扩展瓶颈，将其解耦为解析-重组-混合三阶段，实现高分辨率下的高PE利用率；DecoupleGS（2608.01761）则在自动驾驶测试场景中将场景分解为静态背景与可操控动态智能体。系统层与场景层的"解耦"策略并进，反映3DGS生态正从算法验证走向工程化与规模化部署。

**5. 世界模型/具身智能的"无解码器"趋势与天气条件可控合成**
DF³（2608.02428）在自动驾驶世界建模中完全移除解码器，直接在冻结视觉基础模型末端注入查询以预测未来状态表征；SG-WAM（2608.01397）在策略派生表征空间中学习几何感知动力学。同时，GSRAIN（2608.02177）与DerainSplat（2608.02191）均针对降雨场景，前者强调物理可控性（0–13 mm/h）与多视角一致性，后者聚焦稀疏雨景的前馈去雨重建。具身/自动驾驶场景对"物理可控+几何感知+计算高效"的综合需求正在显性化。


#### 技术路线观察

**几何基础模型层面**：GIFT（2608.02068）利用"外观变化、几何不变"的观测构建无标签监督信号，是几何先验用于模型微调的代表；DF³（2608.02428）直接将冻结视觉基础模型用作特征预测主干，不训练解码器，表征复用思路激进。

**3D/4D重建层面**：三维前馈重建沿三条路线分化——表面对齐（InfiniSplat）、流式增量（StreamSplat）、视图条件化（UniqueSplat）；四维重建则聚焦运动建模的频域解析（FAST-GS）与轨迹监督（ASTRA）。稀疏输入下的深度先验融合（D²-4DGS）与天气退化输入（DerainSplat）进一步丰富了输入模态边界。

**神经场景表示层面**：3DGS在表示结构上进入精细化阶段，如CHOW-SLAM（2608.01914）提出参数化哈希混合表示以构建紧凑空间约束；G-Skin（2608.01726）为3DGS资产学习蒙皮绑定权重；GaussianSelector（2608.01492）直接在高斯原语上做图割选择，无需训练。表示从"建模工具"走向"可操作资产"。

**机器人/AR应用层面**：世界模型向"动作相关+几何感知"的潜空间联合建模推进（SG-WAM），自动驾驶测试向解耦式可交互3DGS场景靠拢（DecoupleGS），雨景可控合成（GSRAIN）为鲁棒性测试提供物理校准数据。

**标定与系统层面**：CalibBEV（2608.02309）以BEV对齐替代传统点对像素标定，跨模态标定的范式在向统一空间表征归并；DeGS（2608.02099）则是少见的3DGS专用硬件架构设计，聚焦数据流解耦。


#### 值得优先阅读的论文

1. **StreamSplat（2608.01659）** —— 打开了前馈3DGS从未覆盖的在线流式场景，VACC内存机制与几何锚定设计兼具理论新意与工程价值，对机器人、自动驾驶等实时增量建图场景影响直接。仅依赖摘要无法判断其在实际视频流上的漂移问题。

2. **InfiniSplat（2608.02437）** —— 表面对齐vs像素对齐之争直指前馈3DGS表示的核心局限，其几何引导采样+隐式解码的组合可能成为后续前馈重建的通用组件，值得跟进其跨数据集泛化表现。

3. **DF³（2608.02428）** —— "完全无解码器"的世界模型在架构层面足够大胆，若能验证其在多样化下游任务上的通用性，可能改变自动驾驶世界模型的计算预算分布。但摘要未报告与带解码器方法的性能差异细节，需全文确认。

4. **FAST-GS（2608.01958）** —— 傅里叶运动建模是针对4DGS运动表达能力不足的直观补强，方法简洁、动机清晰，其频率分解思路可能迁移到其他动态表示。摘要未给出定量对比结果，需谨慎评估其真实增益。

5. **DeGS（2608.02099）** —— 3DGS专用硬件加速器架构属于稀缺方向，其解耦数据流分析从底层揭示了3DGS并行渲染瓶颈，对系统研究者或部署诉求强烈团队有独特参考价值。


#### 可能的研究机会

1. **表面对齐+流式更新的组合**：InfiniSplat的表面对齐表示尚未与StreamSplat的流式因果缓存结合。将几何引导采样引入流式框架，可能解决长流重建中的漂移与几何不一致问题。

2. **无解码器世界模型与几何感知的结合**：DF³的无解码器范式与SG-WAM的几何感知策略空间可以互补——在冻结基础模型中直接注入几何查询，可能实现既免解码又几何可控的未来状态预测。

3. **非朗伯表面先验在小样本/在线场景中的迁移**：GIFT依赖受控外观变化采集，若将其"几何不变"思想迁移到无受控采样的在线场景（如自动驾驶中的玻璃/镜面），与深度基础模型推理时修正结合，是实用化方向。

4. **退化天气下的可控数据集与重建闭环**：GSRAIN强调物理可控降雨合成，DerainSplat强调稀疏雨景前馈去雨重建，但两者未打通——用GSRAIN生成多视角雨景数据训练/评测DerainSplat类前馈去雨重建，或将形成完整闭环。

5. **3DGS交互标注与图优化的扩展**：GaussianSelector将用户涂鸦提升到3D并以图割求解，但其超点粗化在动态场景或拓扑复杂物体上的表现未知。结合CHOW-SLAM的紧凑混合表示

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-04T10:37:43-04:00
**Total number of papers:** 58
**Number of papers added in the latest update:** 28
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

### 2026-08

#### 2026-08-02 - Sparse Meets Dense: Correspondence Guided Robotic Manipulation with Rigid-Deformable Interactions

**Authors:** Ziyu Zhu, Yue Chen, Xirui Liang, Hojin Bae, Yuran Wang, Zhen Yuan, Ruihai Wu, Hao Dong
**Links:** [abs](https://arxiv.org/abs/2608.01083) - [pdf](https://arxiv.org/pdf/2608.01083)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** dense correspondence, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sparse Meets Dense: Correspondence Guided Robotic Manipulation with Rigid-Deformable Interactions
- 作者：Ziyu Zhu, Yue Chen, Xirui Liang, Hojin Bae, Yuran Wang, Zhen Yuan, Ruihai Wu, Hao Dong
- 出版日期：2026-08-02T08:33:24Z
- 分类：Geometry Foundation Models（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.01083

### 一句话总结
该论文提出一种混合稀疏-稠密对应关系表示方法，通过结合任务感知的稀疏关键点与稠密对应关系，实现刚体-可变形体交互的机器人精细操作。

### 研究问题
如何解决刚体与可变形体交互场景（如挂衣服、穿衣）中的机器人操作难题，特别是在多点多接触和复杂动力学条件下，现有基于单一物体的表示（如6D位姿或结构点）缺乏任务信息，难以支持此类交互。

### 核心思路/方法
1. 设计**结构、任务与交互感知的稀疏关键点**：基于刚体和可变形体的全局结构生成关键点，并通过局部交互接触进行筛选，以捕获精细交互信息。
2. 构建可变形体上的**稠密对应关系**：用于在整个操作过程中精确跟踪稀疏关键点，应对可变形体高维动力学带来的追踪困难。
3. 融合两种表示的优点：稀疏关键点编码任务特定信息以实现细粒度操作，稠密对应关系保证追踪效率并泛化到新变形、形状和场景，支持少量演示下的一次性任务迁移。

### 主要贡献
- 提出面向刚体-可变形体交互的混合对应关系表示，兼顾任务信息编码与动态跟踪。
- 引入三层感知（结构、任务、交互）的稀疏关键点生成机制。
- 利用稠密对应关系解决稀疏关键点的鲁棒跟踪问题，实现对新场景的泛化。
- 实验验证了该方法在多种任务上的有效性和广泛适用性。

### 局限性
摘要未提供足够信息，无法获知具体的实验设置、失败案例或方法局限。

### 阅读优先级
**中**。该工作针对机器人操作中刚体-可变形体交互这一特定且具挑战性的方向提出混合表示策略，思路上有一定新颖性；但摘要未提供定量实验对比或具体性能数据，读者需进一步阅读全文评估方法有效性。若研究方向与机器人操作、可变形物体建模相关，则值得深入阅读。

</details>

<details>
<summary>Abstract</summary>

Manipulation involving rigid-deformable interactions, such as hanging clothes or dressing humans, is common in daily life, making it essential for household robots. Compared to single-object manipulation or interactions between rigid bodies, these tasks are particularly challenging due to the rich multi-point contacts and the complex dynamics of the deformable bodies during interaction. Therefore, object-centric representations such as 6D poses or structural points without task-specific information become insufficient for these interactions. In this work, we propose a hybrid correspondence-based representation tailored for rigid-deformable interactions. First, to capture intricate interaction information, we introduce structure-, task-, and interaction-aware sparse keypoints. The keypoints are generated based on the global structures of both rigid and deformable objects, and filtered by their local interaction contacts. However, tracking these sparse keypoints through the interaction remains difficult due to the high-dimensional dynamics of deformable objects. Therefore, we further construct dense correspondences on the deformable objects for accurate keypoint tracking throughout the manipulation. This hybrid design combines the advantages of both representations: sparse keypoints encode rich, task-specific information for fine-grained manipulation, while dense correspondences ensure efficient tracking and generalization to novel deformations, shapes, and scenarios. Together, they enable one-shot transfer to new tasks with minimal demonstrations. Extensive experiments demonstrate the effectiveness and broad applicability of our method.

</details>

#### 2026-08-02 - OC-VLA++: Monocular Geometry-Guided Cross-View Consistency for Viewpoint-Robust Robotic Manipulation

**Authors:** Tianyi Zhang, Ziyang Gong, Zhenjie Yang, Zhe Qian, Haonan Duan
**Links:** [abs](https://arxiv.org/abs/2608.01066) - [pdf](https://arxiv.org/pdf/2608.01066)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** monocular geometry, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OC-VLA++: Monocular Geometry-Guided Cross-View Consistency for Viewpoint-Robust Robotic Manipulation
- 作者：Tianyi Zhang, Ziyang Gong, Zhenjie Yang, Zhe Qian, Haonan Duan
- 出版日期：2026-08-02
- 分类：Geometry Foundation Models（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：https://arxiv.org/abs/2608.01066

### 一句话总结
OC-VLA++ 通过在 OC-VLA 基础上引入几何引导的跨视角监督与显式的跨视角动作等变目标，提升了机器人在有限相机覆盖下对未见视角的泛化能力。

### 研究问题
在相机覆盖受限的情况下，如何提升机器人在未见视角下的操作泛化性能，克服仅依赖图像级增强或相机坐标空间监督导致的视角过拟合问题。

### 核心思路/方法
- 在 OC-VLA 的相机坐标空间动作监督基础上，引入几何引导的配对视角监督（paired-view supervision）。
- 利用来自几何相关视角的同一操作场景的配对观测，训练模型使其相机空间预测对应到相同的机器人坐标系动作，从而显式监督动作预测在跨视角间的变换方式，而非仅依赖图像级增强。

### 主要贡献
- 提出 OC-VLA++，作为 OC-VLA 的扩展，专门针对有限相机覆盖下的视角泛化问题。
- 引入显式的跨视角动作等变目标，作为观察中心动作接地（observation-centric action grounding）的有效补充。
- 实验表明，在有限相机覆盖下，未见视角泛化性能显著提升，且相机位移增大时性能下降更平缓，展示了更稳健的实际部署潜力。

### 局限性
摘要未提供足够信息，关于具体实验设置、数据集、对比基线、失败案例或计算开销等细节均未在摘要中说明。

### 阅读优先级
**中**。理由：该工作聚焦机器人操作中的视角泛化问题，方法在抽象层面有明确创新点（跨视角动作等变监督），且实验结果摘要中有正面结论；但摘要未给出具体的定量提升幅度、实验场景规模或与现有方法的直接对比细节，因此重要性评估受到信息限制。若读者关注机器人操作与跨视角一致性方向，值得阅读；若关注纯视觉几何基础模型，优先级可下调。

</details>

<details>
<summary>Abstract</summary>

We propose OC-VLA++, an extension of OC-VLA for viewpoint generalization under limited camera coverage. While OC-VLA grounds robot actions in the camera coordinate system to align action supervision with visual observations, camera-space grounding alone can still overfit to the few viewpoints observed during training. OC-VLA++ addresses this limitation by introducing geometry-guided paired-view supervision and an explicit cross-view action-equivariance objective. Given paired observations of the same manipulation scene from geometrically related viewpoints, the model is trained such that their camera-space predictions correspond to the same robot-frame action. This objective explicitly supervises how action predictions should transform across viewpoints, rather than relying solely on image-level augmentation. Experiments demonstrate substantial improvements in unseen-view generalization under limited camera coverage, with performance degrading more gracefully under increasing camera displacement. These results establish cross-view action equivariance as an effective complement to observation-centric action grounding for robust real-world deployment.

</details>

### 2026-07

#### 2026-07-30 - JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles

**Authors:** Shawn Li, Wei Yang, Jike Zhong, Jiate Li, Jiawei Yang, You Qin, Ryan Rossi, Franck Dernoncourt, Roger Zimmermann, Yue Wang, Zhengzhong Tu, Vicente Ordonez, Mohit Bansal, Yue Zhao
**Links:** [abs](https://arxiv.org/abs/2607.27670) - [pdf](https://arxiv.org/pdf/2607.27670)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** geometric reasoning

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles
- 作者：Shawn Li, Wei Yang, Jike Zhong, Jiate Li, Jiawei Yang, You Qin, Ryan Rossi, Franck Dernoncourt, Roger Zimmermann, Yue Wang, Zhengzhong Tu, Vicente Ordonez, Mohit Bansal, Yue Zhao
- 出版日期：2026-07-30T04:34:27Z
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.27670

### 一句话总结
本文提出一个基于榫卯拼图的全新基准JigShape，用于评估视觉语言模型（VLMs）的视觉-几何推理能力，发现在更高密度拼图中所有模型均出现性能崩塌的“缩放悬崖”现象。

### 研究问题
现有拼图基准采用矩形切割，在纹理重复区域会产生模糊的ground truth，无法有效衡量VLM的几何推理能力。本文旨在通过引入具有强局部兼容性约束的榫卯咬合拼图，评估VLM在视觉内容与几何约束联合推理上的真实表现，并探索其在不同规模拼图下的能力边界。

### 核心思路/方法
构建JigShape基准，使用“榫+槽”（tab-and-blank）互锁拼图片段，使几何约束提供强局部兼容性要求，与视觉内容结合后产生无歧义的ground truth。基准包含95K个实例，覆盖4×4至16×16四种网格密度。评估方法包括：对前沿VLM进行零样本测试，以及对模型进行监督微调（SFT）后测试，观察不同网格规模下的性能变化。

### 主要贡献
1. 提出JigShape基准，通过榫卯互锁设计解决了传统矩形拼图ground truth模糊的问题，提供无歧义的几何-视觉联合推理评估。
2. 建立包含95K实例、四种网格密度的大规模评测集，系统评估VLM的视觉几何推理能力。
3. 揭示零样本VLM在几何推理上的显著短板：仅GPT-5.5在4×4上超过随机基线，其余模型均处于随机水平。
4. 发现“缩放悬崖”现象：监督微调在4×4上可达到>97%准确率，但所有模型在更大网格（8×8、12×12）上性能急剧下降，表明现有架构无法在拼图数量增加时维持一致的约束满足能力。

### 局限性
摘要未提供足够信息。摘要仅提及性能下降现象（“scaling cliff”）及其对架构能力的暗示，但未明确讨论基准本身的局限性（如可能的偏差、计算成本、泛化范围等）。此外，摘要未提供关于实验设置的具体细节、模型部署方式或误差分析的深入讨论。

### 阅读优先级
**高**
理由：该论文针对VLM几何推理这一关键短板，提出了设计新颖的基准（榫卯拼图），并揭示了系统的“缩放悬崖”现象，这对当前VLM能力边界评估和未来架构改进具有重要参考价值。尽管摘要中未给出完整实验细节，但问题定义清晰，发现的现象具有跨模型的一般性，适合计算机视觉与多模态推理方向的研究者重点关注。

</details>

<details>
<summary>Abstract</summary>

Jigsaw puzzle solving requires jointly reasoning about visual content and geometric constraints, yet existing benchmarks use rectangular cuts that create ambiguous ground truth in texture-repeated regions. We introduce \textit{\ours{}}, a benchmark with tab-and-blank interlocking pieces where geometric constraints provide strong local compatibility requirements that, combined with visual content, yield unambiguous ground truth. Across 95K instances at four grid densities (4$\times$4 to 16$\times$16), we find that \textbf{zero-shot VLMs largely lack geometric reasoning}: only one of five frontier models (GPT-5.5) exceeds random baseline on 4$\times$4 puzzles, while all others perform at chance level. While supervised fine-tuning achieves $>$97\% on 4$\times$4, \textbf{all models collapse on larger grids}: GPT-5.5 drops from 70\% to near-random on 8$\times$8, and even fine-tuned models fall below 5\% on 12$\times$12. This ``scaling cliff'' suggests current architectures cannot maintain consistent constraint satisfaction as the number of pieces increases. \ours{} establishes scalable geometric reasoning as an open challenge for vision-language models.

</details>

#### 2026-07-29 - SpatialQ: Understanding 3D Gaussian Splatting Scene Quality via Visual-based MLLM

**Authors:** Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao
**Links:** [abs](https://arxiv.org/abs/2607.26595) - [pdf](https://arxiv.org/pdf/2607.26595)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialQ: 基于视觉多模态大语言模型的3D高斯泼溅场景质量理解
- 作者：Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao
- 出版日期：2026-07-29（需注意该日期可能与实际发布时间存在偏差，系原文提供）
- 分类：Geometry Foundation Models（主分类）；Neural Scene Representations & Rendering（次分类）
- 链接：[摘要页](https://arxiv.org/abs/2607.26595) | [PDF](https://arxiv.org/pdf/2607.26595)

### 一句话总结
本文提出SpatialQ，一个针对3D高斯泼溅（3DGS）场景质量评估的多模态框架，通过融合多视图几何特征与视觉大语言模型，解决了传统2D质量指标难以捕捉空间结构和跨视图一致性的问题。

### 研究问题
如何对3D高斯泼溅重建的3D场景进行可靠的质量评估，使其不仅能衡量渲染视图的感知保真度，还能反映空间结构、跨视图一致性等场景级因素。

### 核心思路/方法
1. **3D感知质量表示学习**：基于VGGT编码器增加专用质量预测头，将多视图图像编码为视图特定特征并聚合，捕捉跨视图一致性。同时通过联合建模深度和点云结构信息，融入几何线索，学习超越外观特征的结构感知质量表示。
2. **基于多模态大语言模型的推理机制**：将原始图像、深度图、点云渲染图和相机参数共同输入Qwen模型（一种多模态大语言模型），实现有依据的多模态质量推理。

### 主要贡献
- 提出首个专门针对3DGS场景的多模态质量评估框架，整合3D感知质量表示与多模态大语言模型推理。
- 引入结构感知的质量学习策略，融合深度和点云几何信息，弥补传统2D质量指标在空间结构方面的不足。
- 构建了基于Qwen的多模态推理机制，将视觉与几何数据联合输入，增强对3D场景质量的解释能力。

### 局限性
- 摘要未提供实验具体结果，无法定量评估方法性能（如与其他IQA或MLLM方法的对比结果）。
- 摘要未讨论模型的计算复杂度、推理速度或对多视图数量依赖性的分析。
- 未提及是否在多种3DGS渲染场景（如大规模场景、稀疏视图等）下验证鲁棒性。

### 阅读优先级：中
**理由**：该工作针对3DGS场景质量评估这一新兴且实用的方向，方法设计合理（结合几何线索与MLLM）。但由于摘要未提供关键性能数据（如准确率、与主流方法的对比），且发布日期标注为2026年（可能存疑），建议在获取完整实验细节或验证有效性后再决定是否深入阅读。对于从事3D场景重建与质量评估研究的读者，优先级可适度提高。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as an effective representation for novel view synthesis and 3D scene reconstruction, creating an increasing demand for reliable quality assessment. Unlike conventional image quality assessment (IQA), the quality of a 3DGS scene depends not only on the perceptual fidelity of rendered views, but also on scene-level factors such as spatial structure and cross-view consistency. Existing IQA methods are limited by their reliance on 2D perceptual cues, whereas general multimodal large language models (MLLMs) are not designed for stable quality regression and may produce unreliable judgments. To address these limitations, a multimodal quality assessment framework is developed for 3DGS scene understanding. First, a 3D-aware quality representation learning framework is introduced by augmenting a VGGT-based encoder with a dedicated quality head. Multi-view images are encoded into view-specific features and aggregated to capture cross-view consistency, while geometric cues are incorporated through joint modeling of depth and point-cloud-related structural information, enabling the learning of structure-aware quality representations beyond appearance-driven features. Second, a grounded multimodal reasoning mechanism is constructed by jointly feeding original images, depth maps, point cloud renderings, and camera parameters into a Qwen-based MLLM.

</details>

## Dynamic / 4D Reconstruction

### 2026-08

#### 2026-08-03 - ASTRA: Asynchronous Spatio-Temporal Reconstruction via Trajectory Alignment

**Authors:** Junyu Zhu, Hao Zhu, Xinzhuo Zhang, Hongdong Li, Zhan Ma, Xun Cao
**Links:** [abs](https://arxiv.org/abs/2608.02006) - [pdf](https://arxiv.org/pdf/2608.02006)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, dynamic 3D, spatio-temporal reconstruction, temporal reconstruction, motion trajectories, dynamic Gaussian, scene reconstruction, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ASTRA: Asynchronous Spatio-Temporal Reconstruction via Trajectory Alignment
- 作者：Junyu Zhu, Hao Zhu, Xinzhuo Zhang, Hongdong Li, Zhan Ma, Xun Cao
- 出版日期：2026-08-03T10:06:45Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02006

### 一句话总结
ASTRA 提出利用 2D 运动轨迹作为显式、与纹理无关的监督信号，通过轨迹对齐联合优化时间偏移与动态 3D 表示，以解决多相机异步动态场景重建中的运动模糊与几何伪影问题。

### 研究问题
在真实场景中，多相机采集设备之间存在时间异步，导致动态 3D 场景重建出现严重运动模糊与几何伪影。现有异步重建方法依赖光度监督估计时间偏移，但在大偏移和复杂运动下，外观匹配提供的时间线索很弱，其瓶颈包括：低纹理区域的“纹理诱导坍缩”（对齐信号近乎消失）以及“变形诱导耦合”（时间误差被吸收进扭曲的几何或运动而非被显式纠正）。

### 核心思路/方法
ASTRA 以 2D 运动轨迹作为显式的、纹理无关的监督信号，替代仅依赖渲染颜色残差进行相机同步的做法。具体地，它将重建 3D 点投影后的运动与观测到的 2D 轨迹进行对齐，联合优化时间偏移和动态 3D 表示；同时使用动态与确定性掩码（dynamic and certainty masking）抑制不可靠的轨迹约束。

### 主要贡献
- 提出 ASTRA 框架，将 2D 运动轨迹引入异步动态重建作为显式监督，缓解纹理缺失和大偏移下的同步困难。
- 在多个动态 Gaussian Splatting 骨干网络上验证了方法的通用性。
- 实验表明：在高达 25 帧偏移的严重异步下，ASTRA 保持高频空间细节和强鲁棒性，PSNR 提升约 1.4 dB，时间偏移 MAE 降低 54.0%，同步成功率提升近 4 倍。

### 局限性
摘要未提供足够信息（未提及方法在极端遮挡、轨迹长度不足、计算开销或失败案例等方面的局限）。

### 阅读优先级
**高**  
理由：该工作针对动态重建中实际且棘手的时间异步问题，提出了新的监督范式（轨迹对齐），在多个骨干上取得显著提升（PSNR、MAE、成功率均有量化改善），对 4D 重建、神经表示与渲染方向的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D scene reconstruction has achieved remarkable success under the assumption of strictly synchronized multi-camera inputs. However, in real-world scenarios, temporal asynchrony among capturing devices remains a critical challenge, leading to severe motion blur and geometric artifacts. Existing asynchronous reconstruction methods typically estimate temporal offsets through photometric supervision, but appearance matching provides weak temporal cues under large offsets and complex motions. We attribute this limitation to two major bottlenecks: texture-induced collapse, where low-texture regions provide nearly vanishing alignment signals, and deformation-induced coupling, where temporal errors are absorbed into distorted geometry or motion rather than being explicitly corrected. To address these issues, we propose ASTRA (Asynchronous Spatio-Temporal Reconstruction via Trajectory Alignment), a framework that introduces 2D motion trajectories as explicit, texture-agnostic supervision for asynchronous dynamic reconstruction. Instead of synchronizing cameras solely through rendered color residuals, ASTRA jointly optimizes temporal offsets and dynamic 3D representations by aligning the projected motion of reconstructed 3D points with observed 2D trajectories, while using dynamic and certainty masking to suppress unreliable trajectory constraints. Extensive experiments on different dynamic Gaussian Splatting backbones show that ASTRA preserves high-frequency spatial details and sustains strong robustness even under severe asynchrony with up to 25-frame offsets, achieving approximately 1.4 dB PSNR improvement, reducing temporal-offset MAE by 54.0\%, and nearly quadrupling the synchronization success rate.

</details>

#### 2026-08-03 - FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis

**Authors:** Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma
**Links:** [abs](https://arxiv.org/abs/2608.01958) - [pdf](https://arxiv.org/pdf/2608.01958)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, 4D Gaussian, 3D reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis
- 作者：Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma
- 出版日期：2026-08-03
- 分类：Dynamic / 4D Reconstruction（主）；Neural Scene Representations & Rendering（次）
- 链接：https://arxiv.org/abs/2608.01958

### 一句话总结
本文提出一种基于傅里叶运动建模的频率感知时空高斯泼溅方法（FAST-GS），通过将运动分解为频域正弦分量，同时捕捉低频全局轨迹与高频局部细节，以提升动态场景重建的复杂运动拟合精度与长期时间一致性。

### 研究问题
现有4D高斯泼溅（4DGS）方法使用单一多项式建模运动，在含高频运动分量的复杂动态场景中性能受限，且因累积轨迹漂移难以保证长期稳定性。

### 核心思路/方法
- 提出**傅里叶运动建模模块**：将运动分解为基于频率的正弦分量，分别捕捉低频全局轨迹和高频局部细节，以准确建模复杂运动模式，同时保持4DGS的实时渲染能力。
- 在损失函数中集成**运动感知正则化策略**：使用与频率相关的权重抑制高频抖动，同时保持低频运动的连贯性。

### 主要贡献
- 提出傅里叶运动建模范式，改进复杂运动拟合能力与长期时序一致性。
- 引入频率相关的运动感知正则化，在抑制高频噪声的同时维持低频运动连贯性。
- 在N3V和Google Immersive数据集的多场景实验中验证了方法有效性。

### 局限性
摘要未提供足够信息（如具体数值结果、与基线方法的定量对比细节、失败案例或计算开销等均未说明）。

### 阅读优先级
**高**。理由：该工作直接针对4DGS在复杂动态场景中的核心瓶颈（运动建模能力不足与轨迹漂移）提出新颖的频域分解方案，属于动态新视角合成方向的重要方法论改进；且实验覆盖多个公开数据集，若该方向与读者兴趣相关，值得精读。

</details>

<details>
<summary>Abstract</summary>

4D Gaussian Splatting (4DGS) excels in dynamic 3D reconstruction and real-time novel view synthesis via efficient 4D Gaussian representations and parallelizable rendering. However, existing 4DGS approaches rely on a single polynomial to model motion, which limits performance in complex dynamic scenes where high-frequency motion components are prevalent, and fails to ensure long-term stability due to cumulative trajectory drift. To address these issues, we propose a Fourier Motion Modeling module: this paradigm decomposes motion into frequency-based sinusoidal components, capturing both low-frequency global trajectories and high-frequency local details to model complex motion patterns accurately. It retains the real-time rendering capability of 4DGS while improving complex motion fitting and long-term coherence. Additionally, we integrate a motion-aware regularization strategy into the loss function: it uses frequency-dependent weights to suppress high-frequency jitter while preserving low-frequency motion coherence. Extensive experiments on N3V and Google Immersive datasets from multiple scenarios demonstrate the effectiveness of our method.

</details>

#### 2026-08-03 - D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting

**Authors:** Jijian Zhao
**Links:** [abs](https://arxiv.org/abs/2608.01588) - [pdf](https://arxiv.org/pdf/2608.01588)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, 4D Gaussian, monocular depth, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting
- 作者：Jijian Zhao
- 出版日期：2026-08-03
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01588

### 一句话总结
本文提出一种基于双源深度先验引导的稀疏相机动态4D高斯泼溅方法，通过融合单目深度与多视角几何深度，在减少输入视角的同时提升动态场景重建的质量与一致性。

### 研究问题
如何在稀疏相机输入下，缓解动态4D高斯泼溅因几何监督不足而导致的结构缺失和漂浮高斯伪影问题。

### 核心思路/方法
- 利用双源深度先验（单目深度与多视角几何深度）的互补性：单目深度提供稠密但尺度模糊、局部有偏的结构；多视角几何深度提供与重建坐标系一致但不完整的锚点。
- 将单目深度估计与有效的多视角几何深度对齐，并通过一致性验证筛选出可靠的几何锚点。
- 可靠锚点用于一致性感知剪枝和深度监督；经验证的几何深度和对齐后的单目深度共同为欠重建区域提供候选几何，以支持稠密化。
- 采用RGB-D联合优化，在稀疏视角监督下提升外观保真度与几何一致性。

### 主要贡献
- 提出D^2-4DGS框架，首次在稀疏相机动态4D高斯泼溅中系统性地融合双源深度先验。
- 设计基于一致性验证的几何锚点筛选机制，有效支持剪枝、深度监督和稠密化。
- 通过RGB-D联合优化，在稀疏视角下同时改善外观质量与几何一致性。
- 在全部9个数据集-视角设置中取得最高PSNR，平均较各设置最佳对比方法提升1.33 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法针对稀疏相机动态重建这一具体问题，提出了双源深度融合的可行方案，并在量化指标上有明显提升，对从事动态场景重建或高斯泼溅相关研究的读者有参考价值；但摘要未给出方法复杂度、运行效率或失败案例分析，尚不足以判断其在实际应用中的普适性。

</details>

<details>
<summary>Abstract</summary>

Dynamic 4D Gaussian Splatting has emerged as an efficient representation for dynamic novel view synthesis through explicit scene modeling and real-time rendering. However, existing methods typically require dense multi-view videos for sufficient geometric constraints, making capture expensive and limiting sparse-camera deployment. Reducing input views lowers acquisition cost but weakens geometry supervision, often causing missing structures and floating Gaussians. Depth priors provide geometric cues, yet no single source offers both dense coverage and reliable geometry. Monocular depth provides dense structure but is scale-ambiguous and locally biased, whereas multi-view geometric depth provides incomplete anchors consistent with the reconstruction coordinate system. To exploit their complementarity, we propose D$^2$-4DGS, a sparse-camera dynamic 4D Gaussian Splatting framework guided by dual-source depth priors. We align monocular estimates with valid multi-view geometric depths and verify their consistency to identify reliable geometric anchors. These verified anchors support consistency-aware pruning and depth supervision, while verified geometric depths and aligned mono-only estimates provide candidate geometry for densification in under-reconstructed regions. Finally, RGB-D joint optimization improves appearance fidelity and geometric consistency under sparse-view supervision. Across all nine dataset--view settings, D$^2$-4DGS achieves the highest PSNR, improving by 1.33 dB on average over the best competing method in each setting.

</details>

#### 2026-08-02 - DynActiveGS: Active Gaussian Splatting for Dynamic Scene Reconstruction

**Authors:** Hongbo Duan, Pengting Luo, Chengzhi Zhao, Yuanhao Chiang, Fangming Liu, Xueqian Wang
**Links:** [abs](https://arxiv.org/abs/2608.01178) - [pdf](https://arxiv.org/pdf/2608.01178)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DynActiveGS: Active Gaussian Splatting for Dynamic Scene Reconstruction
- 作者：Hongbo Duan, Pengting Luo, Chengzhi Zhao, Yuanhao Chiang, Fangming Liu, Xueqian Wang
- 出版日期：2026-08-02
- 分类：Dynamic / 4D Reconstruction（次级：3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.01178

### 一句话总结
本文提出一种基于3D高斯泼溅的动态感知主动重建框架，通过显式区分结构不确定性与运动诱导不确定性，实现动态环境下鲁棒的主动探索与场景重建。

### 研究问题
如何在包含动态物体的环境中，实现主动（自主探索）的3D高斯场景重建，并避免运动物体对重建质量造成的干扰。

### 核心思路/方法
- 基于3DGS框架，在线增量重建高斯场景表示。
- 通过在线不确定性预测与不确定性加权的高斯优化，抑制被运动干扰的观测。
- 核心创新：将不确定性显式分解为**结构不确定性**（对应未充分重建的静态区域）与**运动诱导不确定性**（对应动态不可靠区域）。
- 基于两类不确定性，进行**动态感知视角选择**与**动态约束路径规划**，在探索中优先选择信息丰富且稳定的观测。
- 整体形成统一的闭环主动重建流程。

### 主要贡献
- 提出首个面向动态场景的主动3DGS重建框架（DynActiveGS）。
- 显式分解不确定性为结构性与运动诱导两类，使系统能区分欠重建静态区域与动态不可靠区域。
- 设计动态感知的视角选择与路径规划策略，实现闭环主动重建。
- 在动态基准上，相比现有主动重建基线，在重建精度、完整性、渲染质量与探索效率上均取得一致性提升。

### 局限性
摘要未提供足够信息。具体局限性（如对极端动态场景的鲁棒性、计算开销、实验范围限制等）摘要未提及。

### 阅读优先级
**高**。理由：该工作将主动重建扩展至动态场景，且结合3DGS这一当前热点表示，提出新颖的不确定性分解机制，在方法设计与系统完整性上均具一定创新性；适用于4D重建、主动探索与机器人感知方向的读者。

</details>

<details>
<summary>Abstract</summary>

We present DynActiveGS, a dynamic-aware active reconstruction framework based on 3D Gaussian Splatting (3DGS) for autonomous exploration in dynamic environments. The framework incrementally reconstructs a 3D Gaussian scene representation while suppressing motion-corrupted observations through online uncertainty prediction and uncertainty-weighted Gaussian optimization. A key component of DynActiveGS is the explicit decomposition of uncertainty into structural uncertainty and motion-induced uncertainty, which enables the system to distinguish under-reconstructed static regions from dynamically unreliable areas. Based on these uncertainty fields, DynActiveGS performs dynamic-aware viewpoint selection and dynamic-constrained path planning to favor informative yet stable observations during exploration. The resulting system forms a unified closed-loop pipeline for robust active reconstruction in dynamic scenes. Extensive experiments on challenging dynamic benchmarks demonstrate consistent improvements over existing active reconstruction baselines in reconstruction accuracy, completeness, rendering quality, and exploration efficiency.

</details>

### 2026-07

#### 2026-07-31 - OASIS: Occlusion-aware Single-image Hand Avatar Reconstruction via 3D Gaussian Splatting

**Authors:** Zhisheng Han, Shiyao Wu, Jiayan Qiu, Yakun Ju, Lu Liu, Le Zhang, Pengfei Feng, Huiyu Zhou, Zheheng Jiang
**Links:** [abs](https://arxiv.org/abs/2607.29633) - [pdf](https://arxiv.org/pdf/2607.29633)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** avatar reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OASIS: Occlusion-aware Single-image Hand Avatar Reconstruction via 3D Gaussian Splatting
- 作者：Zhisheng Han, Shiyao Wu, Jiayan Qiu, Yakun Ju, Lu Liu, Le Zhang, Pengfei Feng, Huiyu Zhou, Zheheng Jiang
- 出版日期：2026-07-31
- 分类：主分类：Dynamic / 4D Reconstruction；次分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.29633

### 一句话总结
提出了一种基于3D高斯泼溅的遮挡感知单图手部化身重建框架OASIS，通过可见性条件注意力与特征网格表征实现高保真重建。

### 研究问题
从单张图像重建3D手部化身，核心难点在于：严重自遮挡导致的视觉证据有限，以及高度关节化手部的复杂姿态依赖形变。现有基于隐式神经辐射场（NeRF）的方法计算开销大且难以保留精细手部细节。

### 核心思路/方法
1. **几何对齐视觉证据令牌**：将输入图像观测与3D手部几何显式对齐，并通过上下文自适应令牌化编码稀疏的图像外观信息。
2. **可见性条件点-图像注意力**：由于自遮挡使图像证据可靠性依赖可见性，引入该机制将视觉证据可靠传递至几何令牌，生成遮挡感知的高斯特征。
3. **网格上特征（Feature-on-Mesh）表征**：使高斯形变由局部表面拉伸引导，捕获手部的非刚性形变。
4. **一次性适应方案**：先从多身份训练数据学习共享手部先验，再拟合到目标图像实现目标专属重建。

### 主要贡献
- 提出首个针对单图手部化身重建的定制3D高斯泼溅框架，在视觉保真度和效率上优于现有基线。
- 设计了几何对齐视觉证据令牌与可见性条件注意力机制，缓解自遮挡带来的信息缺失问题。
- 引入Feature-on-Mesh表征，使高斯形变能由局部表面拉伸引导，提升对非刚性形变的建模能力。
- 采用一次性适应方案，支持跨身份先验学习与目标图像适配，并展示了在文本到化身生成和纹理编辑等下游任务中的适用性。

### 局限性
摘要未提供足够信息，未明确讨论该方法的失败案例、计算资源需求、对极端遮挡或复杂背景的鲁棒性边界，也未提及与现有方法在定量指标上的具体差距。

### 阅读优先级
**高**。理由：该工作针对单图手部重建这一长期存在的病态问题，提出基于3D高斯泼溅的新框架，同时解决遮挡感知和姿态形变两个核心挑战，在效率和保真度上均表现出优势，且展示了多场景下游应用的潜力，对关注手部重建、3D视觉或动态重建的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-image 3D hand avatar reconstruction is fundamentally ill-posed and particularly challenging due to limited visual evidence under severe self-occlusion and the complex pose-dependent deformation of highly articulated hands. Existing methods predominantly rely on implicit NeRF-style representations, whose volumetric fitting is computationally expensive and often struggles to preserve fine-grained hand details. In this work, we present OASIS, a tailored 3D Gaussian Splatting framework for single-image hand avatar reconstruction. To faithfully encode sparse image-specific appearance cues in single-view reconstruction, we construct geometry-aligned visual evidence tokens by explicitly aligning input image observations with 3D hand geometry and context-adaptively tokenizing the resulting visual evidence. Since severe self-occlusion makes the reliability of image evidence inherently visibility-dependent, we introduce a visibility-conditioned point-image attention to reliably transfer visual evidence to geometric tokens, yielding occlusion-aware Gaussian features for faithful and robust reconstruction. To further capture non-rigid deformation of articulated hands, we introduce a Feature-on-Mesh representation to enable Gaussian deformation to be guided by local surface stretching. Under this framework, we adopt a one-shot adaptation scheme that learns a shared hand prior from multi-identity training data and then fits it to a target image for target-specific reconstruction. Extensive experiments show that OASIS outperforms existing baselines in both visual fidelity and efficiency across challenging poses and in-the-wild scenarios, and further demonstrates strong versatility in downstream applications such as text-to-avatar generation and texture editing.

</details>

#### 2026-07-30 - AdaAnchor4D: Anchor-Conditioned Spatiotemporal Feature Aggregation for Monocular UAV 4D Reconstruction

**Authors:** Peiyi Xu, Junpeng Zhang, Guanbin Li, Ronghua Shang, Mingtao Feng, Le Dong, Weisheng Dong, Guangming Shi, Jie Feng
**Links:** [abs](https://arxiv.org/abs/2607.28320) - [pdf](https://arxiv.org/pdf/2607.28320)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic scene reconstruction, dynamic reconstruction, dynamic Gaussian, scene reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AdaAnchor4D: Anchor-Conditioned Spatiotemporal Feature Aggregation for Monocular UAV 4D Reconstruction
- 作者：Peiyi Xu, Junpeng Zhang, Guanbin Li, Ronghua Shang, Mingtao Feng, Le Dong, Weisheng Dong, Guangming Shi, Jie Feng
- 出版日期：2026-07-30
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.28320

### 一句话总结
本文提出AdaAnchor4D，一种面向单目无人机视频动态场景重建的自适应锚点变形框架，通过锚点条件化的时空特征聚合提升复杂城市动态场景的渲染质量并保持实时性能。

### 研究问题
单目无人机视频中的复杂城市场景具有显著的时空异构性，不同区域遵循不同时间活动模式，且部分动态区域的运动状态随时间演变。现有基于分解共享时空特征场的动态高斯方法采用固定平面特征组合机制，难以适应此类异构局部动态，导致重影伪影和动态细节模糊。

### 核心思路/方法
- **Anchor-Conditioned Feature Aggregation (ACFA)**：利用锚点特有的聚合嵌入和时间信息，自适应聚合共享时空特征，使不同局部单元获得匹配自身局部状态和时间状态的动态表示。
- **Decoupled Local Geometry Deformation (DLGD)**：将锚点状态变形与局部高斯几何变形解耦。
- **Density-Adaptive Coordinate Warping (DACW)**：根据轴向上的锚点分布重新参数化特征查询坐标，缓解非均匀几何采样与均匀网格参数化之间的不匹配。

### 主要贡献
- 提出AdaAnchor4D，一种针对单目无人机动态场景重建的自适应锚点变形框架。
- 设计ACFA机制，实现锚点条件化的自适应时空特征聚合，适应场景异构局部动态。
- 提出DLGD与DACW，分别解耦几何变形并缓解采样与参数化不匹配问题。
- 在UAV-Arc4D、VisDrone和UAVDT数据集上实验表明，AdaAnchor4D在保持实时渲染性能的同时，相比代表性动态高斯方法取得了更高的渲染质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目无人机动态场景重建中时空异构性这一具体挑战，提出了三项机制创新（ACFA、DLGD、DACW），并在多个UAV基准上验证了渲染质量提升和实时性保留。结合所属动态/4D重建及神经场景渲染领域，对从事动态场景建模、无人机视觉和实时神经渲染研究的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular UAV videos provide valuable observations for dynamic reconstruction of complex urban scenes. However, such scenes exhibit pronounced spatiotemporal heterogeneity: different regions follow distinct temporal activity patterns, while the motion states of some dynamic regions may further evolve over time. Although dynamic Gaussian methods based on decomposed shared spatiotemporal feature fields have achieved efficient and accurate reconstruction in object-centric or relatively compact scenes, their commonly adopted fixed plane-wise feature combination mechanisms are less suited to the heterogeneous local dynamics of UAV scenes, often leading to ghosting artifacts and blurred dynamic details. To address this challenge, we propose AdaAnchor4D, an adaptive anchor deformation framework for monocular UAV dynamic scene reconstruction. At its core, Anchor-Conditioned Feature Aggregation (ACFA) adaptively aggregates shared spatiotemporal features using anchor-specific aggregation embeddings and temporal information, allowing different local units to obtain dynamic representations tailored to their local and temporal states. Decoupled Local Geometry Deformation (DLGD) separates anchor-state deformation from local Gaussian geometry deformation, while Density-Adaptive Coordinate Warping (DACW) reparameterizes feature-query coordinates according to the axis-wise anchor distributions, alleviating the mismatch between non-uniform geometric sampling and uniform grid parameterization. Experiments on UAV-Arc4D, VisDrone, and UAVDT show that AdaAnchor4D achieves higher rendering quality than representative dynamic Gaussian methods while maintaining real-time rendering performance. The code will be made publicly available.

</details>

#### 2026-07-30 - S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image

**Authors:** Hail Song, Seokhwan Yang, Jiwon Yang, Woojin Cho, Woontack Woo
**Links:** [abs](https://arxiv.org/abs/2607.28164) - [pdf](https://arxiv.org/pdf/2607.28164)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** dynamic 3D, avatar reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, AR, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image
- 作者：Hail Song, Seokhwan Yang, Jiwon Yang, Woojin Cho, Woontack Woo
- 出版日期：2026-07-30
- 分类：Dynamic / 4D Reconstruction；子分类：Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.28164

### 一句话总结
S-Avatar 提出一种从单张图像生成逼真 3D 头部虚拟形象的方法，通过扩散引导的 3D 高斯生成和 FLAME 参数模型驱动，实现动态渲染与新视角、表情下的高一致性。

### 研究问题
如何从单张图像重建头部 3D 虚拟形象，并解决现有方法在未见视角下 3D 一致性不足的问题，同时支持实时动态驱动。

### 核心思路/方法
采用三阶段流程：
1. 利用基于扩散的高斯生成模块，从单张图像直接合成高分辨率 3D 高斯溅射（3DGS）。
2. 将参数化头部模型 FLAME 与生成的 3DGS 对齐，通过优化其参数和空间变换实现匹配。
3. 构建绑定模板（binding template），编码初始高斯溅射与 FLAME 之间的空间关系，从而将 3DGS 适配至 FLAME 的变化，实现实时动态形变与渲染。

### 主要贡献
- 提出扩散引导的单图 3DGS 生成模块，结合 FLAME 控制实现高质量头部虚拟形象构建。
- 引入绑定模板策略，使 3DGS 能适应 FLAME 参数变化，支持实时动态渲染。
- 公开数据集上的评估显示，该方法在新视角和表情生成任务上优于现有最先进方法，具备更高真实感和一致性。
- 为 VR/AR 等应用提供了高效且易访问的虚拟形象创建途径。

### 局限性
摘要未提供足够信息，未详细说明方法在极端姿态、遮挡、非正面光照或训练数据依赖等方面的潜在限制，也未给出定量误差或失败案例分析。

### 阅读优先级
**高**  
理由：论文聚焦单图头部虚拟形象重建这一热门且具有实际应用价值的方向，结合扩散模型与 3DGS，方法新颖且宣称优于现有技术，并支持实时动态渲染，适合关注 3D 重建、神经渲染及 VR/AR 应用的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

We propose S-Avatar, a novel method for generating photorealistic 3D head avatars from a single image using a diffusion-guided 3D model generation module and strategies for animating 3D Gaussian Splatting (3DGS). While single-image head avatar reconstruction is crucial for lifelike Virtual Reality (VR) applications, existing approaches often struggle to preserve 3D consistency under unseen viewpoints. S-Avatar addresses this limitation through a three-stage pipeline. First, a high-resolution 3DGS is synthesized directly from a single image using a diffusion-based Gaussian splat generation module. Next, the parametric head model FLAME is aligned with the generated 3DGS by optimizing its parameters and spatial transformations. Finally, to adapt the 3DGS to FLAME variations, we construct a binding template that encodes the spatial relationship between the initial splats and FLAME. The dynamic 3D head avatar can then be rendered in real time by deforming the 3DGS with the binding template. By combining diffusion-guided canonical 3DGS generation with FLAME-based control, our method achieves efficient and accurate reconstruction with enhanced 3D consistency. Evaluations on public datasets demonstrate that S-Avatar outperforms state-of-the-art methods in novel-view and expression generation, achieving superior realism and consistency. Consequently, our approach represents a significant advance in accessible avatar creation, applicable to a wide range of VR/AR applications. The project page is available at https://github.com/hailsong/savatar.

</details>

#### 2026-07-28 - SplatStream: Fine Granular Scalable Gaussian Splatting for Adaptive 3D Scene Streaming

**Authors:** Muhammad Talha, William Gordon, Sajid Umair, Zhu Li, Anique Akhtar, Joel Jung
**Links:** [abs](https://arxiv.org/abs/2607.25971) - [pdf](https://arxiv.org/pdf/2607.25971)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic Gaussian, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatStream: Fine Granular Scalable Gaussian Splatting for Adaptive 3D Scene Streaming
- 作者：Muhammad Talha, William Gordon, Sajid Umair, Zhu Li, Anique Akhtar, Joel Jung
- 出版日期：2026-07-28
- 分类：Dynamic / 4D Reconstruction（主分类）；Neural Scene Representations & Rendering（副分类）
- 链接：摘要：https://arxiv.org/abs/2607.25971 ；PDF：https://arxiv.org/pdf/2607.25971

### 一句话总结
提出一个名为 SplatStream 的细粒度可伸缩高斯泼溅框架，用于动态3D场景的适应性流传输，通过质量/分辨率分层、层间预测编码、B帧时域扩展及体积-不透明度重要性度量，实现低延迟、带宽自适应的流媒体传输。

### 研究问题
动态3D高斯泼溅（GS）表征尺寸大、帧间冗余高，导致其在适应性流传输场景下（如带宽波动环境）面临显著挑战。

### 核心思路/方法
1. **空间可伸缩性**：将GS场景分解为质量层和分辨率层，引入层间预测编码实现可伸缩性。
2. **时域可伸缩性**：引入B帧以提供时域质量可伸缩性。
3. **预测机制**：使用轻量级基于跨层Transformer的预测器，用于跨层和时域预测。
4. **重要性分组**：基于体积-不透明度度量对高斯原语进行细粒度打包，优先传输视觉重要性高的原语，实现渐进式细化。
5. **流传输适配**：将可伸缩GS比特流映射为兼容MPEG-DASH的子表示结构，支持细粒度自适应、低延迟传输。

### 主要贡献
1. 提出一种细粒度可伸缩的高斯泼溅框架，支持动态3D场景的适应性流传输。
2. 引入跨层预测编码和B帧机制，实现空间与时域的可伸缩性。
3. 利用体积-不透明度重要性度量进行高斯原语分组与优先传输，提升渐进式反馈质量。
4. 将可伸缩比特流与MPEG-DASH流媒体标准对接，实现在带宽波动下的低延迟自适应传输。

### 局限性
摘要未提供足够信息。该部分需阅读全文后分析。

### 阅读优先级
**高**。理由：该工作针对动态高斯泼溅在流传输中的核心难点——表征冗余与带宽适配——提出了完整的可伸缩方案，并涉及层间预测、Transformer、MPEG-DASH标准对接等多个技术点，对NeRF/3D GS领域及多媒体流传输研究均有参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (GS) enables high quality real-time rendering for immersive media, but its large representation size and frame-wise redundancy create significant challenges for adaptive streaming. This paper presents SplatStream, a fine granular scalable Gaussian splatting framework for dynamic 3D scene delivery. The proposed method decompose the GS scenes into quality and resolution layers, and introduces inter-layer predictive coding to achieve scalability. For temporal direction, B-frames are introduced to have temporal quality scalability. A lightweight cross-layer transformer based predictor is utilized for both cross layer and temporal predictions. In addition, a volume-opacity based importance measure is used for fine-grained Gaussian packetization, allowing visually important primitives to be transmitted earlier for progressive refinement. Finally, the scalable GS bitstream is mapped to an MPEG-DASH compatible sub-representation structure, enabling fine granular adaptive, low-latency delivery of dynamic Gaussian splatting content under bandwidth-varying conditions.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-08

#### 2026-08-03 - CalibBEV: LiDAR-Camera Calibration via BEV Alignment

**Authors:** Filippo D'Addeo, Lorenzo Cipelli, Adriano Cardace, Emanuele Ghelfi, Andrea Zinelli, Massimo Bertozzi
**Links:** [abs](https://arxiv.org/abs/2608.02309) - [pdf](https://arxiv.org/pdf/2608.02309)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CalibBEV: LiDAR-Camera Calibration via BEV Alignment
- 作者：Filippo D'Addeo, Lorenzo Cipelli, Adriano Cardace, Emanuele Ghelfi, Andrea Zinelli, Massimo Bertozzi
- 出版日期：2026-08-03
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.02309

### 一句话总结
CalibBEV 提出了一种基于鸟瞰图（BEV）特征对齐的两步式 LiDAR-相机标定方法，通过隐式粗对齐和显式精对齐实现高效、鲁棒的跨模态标定，在 KITTI 和 nuScenes 数据集上显著优于现有方法。

### 研究问题
如何利用 BEV 空间的统一表征，实现 LiDAR 与相机之间高精度、鲁棒的自动标定，从而替代传统的点对像素匹配方法。

### 核心思路/方法
1. **统一空间表征**：将 LiDAR 和相机数据分别映射到共享的 3D BEV 空间中，提取各自的 BEV 特征。
2. **两步对齐流程**：
   - **隐式对齐（第一步）**：直接从 BEV 特征回归一个粗标定矩阵。
   - **显式对齐（第二步）**：利用 BEV 公式将一种模态的特征与另一种模态对齐，细化粗估计为精准的标定矩阵。
3. **语义一致性约束**：引入受 CLIP 启发的对比损失，迫使两个模态的 BEV 特征在空间中语义一致，引导网络学习统一特征空间。

### 主要贡献
- 提出新颖的 BEV 对齐标定框架，统一了 LiDAR 与相机的空间表征。
- 设计两步对齐机制（隐式+显式），兼顾粗定位与精细化。
- 采用对比损失实现跨模态语义一致性，提升特征融合质量。
- 在 KITTI 和 nuScenes 基准上大幅超越先前方法：RRE 分别降低 51% 和 68%，RTE 分别降低 80% 和 91%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法在标定精度上取得了大幅度提升（RRE/RTE 相对降低 51%~91%），且采用两步对齐+对比学习的思路具有创新性，对多传感器融合与自动驾驶领域有重要参考价值。摘要提供了清晰的性能对比，展示了显著优势。

</details>

<details>
<summary>Abstract</summary>

We present CalibBEV, a novel Bird's Eye View (BEV) alignment approach for LiDAR-camera calibration. Our method unifies LiDAR and camera data into a shared 3D spatial representation, enabling accurate and robust cross-modal calibration. CalibBEV extracts sensor-wise BEV features from each modality using domain-specific architectures and estimates the calibration matrix through a two-step alignment process. First, we perform an implicit alignment by regressing a coarse calibration matrix directly from the BEV features. To ease this alignment, we enforce semantic consistency between BEV representations across modalities using a contrastive loss inspired by CLIP, guiding both networks toward a unified feature space. In the second step, we leverage our BEV formulation to explicitly align the features of one modality with the other, refining the initial coarse estimate into a final, more accurate calibration matrix. CalibBEV significantly outperforms prior point-to-pixel matching methods, achieving state-of-the-art calibration accuracy. On the KITTI and nuScenes benchmarks, our method reduces the Relative Rotation Error (RRE) by 51% and 68%, and the Relative Translation Error (RTE) by 80% and 91%, respectively, compared to previous methods.

</details>

#### 2026-08-03 - TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction

**Authors:** Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang
**Links:** [abs](https://arxiv.org/abs/2608.02304) - [pdf](https://arxiv.org/pdf/2608.02304)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction
- 作者：Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang
- 出版日期：2026-08-03T14:30:20Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02304

### 一句话总结
本文提出将主动场景重建视为遍历覆盖问题，通过核遍历水平规划器在线生成与当前地图信息分布匹配的传感器轨迹，以替代贪婪的逐次最优视点选择。

### 研究问题
现有基于高斯泼溅地图的主动重建系统采用贪心策略，每步仅优化单个下一个最佳视角（NBV），并用短视路径连接已选视角。这种贪婪解耦方式忽略场景信息的全局结构，产生低效轨迹，在视角之间浪费感知能力。因此，研究问题是如何设计考虑全局信息分布的轨迹优化方法。

### 核心思路/方法
- 将主动重建形式化为遍历覆盖问题：要求传感器轨迹的时间平均空间统计量匹配由当前地图导出的目标信息分布。
- 目标信息分布在线由不确定性和可见性推导得到。
- 通过核遍历水平规划器（kernel-ergodic horizon planner）计算遍历轨迹，结合梯度流和足迹耗尽（footprint depletion）机制。
- 在映射与轨迹优化之间形成闭环。

### 主要贡献
- 提出新的主动重建范式：从贪心NBV转向全局遍历轨迹优化。
- 设计在线推导目标信息分布的方法（基于不确定性和可见性）。
- 开发核遍历水平规划器，带有梯度流与足迹耗尽机制，实现映射与轨迹优化的闭环集成。
- 在Replica数据集上相较于NBV基线，将PSNR提升1.5 dB。

### 局限性
摘要未提供足够信息（未提及计算开销、对动态环境适应能力、真实场景测试结果、与更多基线对比的细节、算法收敛性保证等）。

### 阅读优先级
**高**。理由：该工作针对主动重建中贪心策略效率低下的核心问题，提出全局遍历优化的新视角，方法上有闭环设计，并在公开基准上取得定量提升（PSNR +1.5 dB），对该领域研究者具有参考价值。此外提供了开源代码，便于复现和扩展。

</details>

<details>
<summary>Abstract</summary>

Existing active reconstruction systems with Gaussian-splatting maps select observations greedily, optimizing a single next-best-view (NBV) at each step and connecting the chosen views by short-horizon path planning. This greedy decoupling disregards the global structure of scene information, producing inefficient trajectories that waste sensing capacity in transit between selected views. In this work, we study active reconstruction as an ergodic coverage problem: the time-averaged spatial statistics of the sensor trajectory should match a target information distribution induced by the current map. Our approach derives this target distribution online from uncertainty and visibility, and calculates ergodic trajectories via a kernel-ergodic horizon planner with gradient flow and footprint depletion, closing the loop between mapping and trajectory optimization. We thoroughly evaluate TRACE on the Replica dataset against the Next-Best-View (NBV) baselines, improving PSNR by 1.5 dB. Code: https://github.com/spikelab-jhu/trace-active-reconstruction.

</details>

#### 2026-08-03 - UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction

**Authors:** Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan
**Links:** [abs](https://arxiv.org/abs/2608.02145) - [pdf](https://arxiv.org/pdf/2608.02145)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction
- 作者：Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan
- 出版日期：2026-08-03T12:31:12Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02145

### 一句话总结
UniqueSplat提出一种基于视图条件的三维高斯泼溅前馈模型，通过动态调整高斯分布来适应不同查询视角，提升通用三维重建的精度与泛化能力。

### 研究问题
现有前馈三维重建方法（如pixelSplat和MVSplat）为每个场景生成固定的三维高斯表示，无法根据目标视角动态调整，导致对特定视点的适应能力不足。研究问题是如何将目标视角信息融入高斯预测过程，实现视图自适应的三维重建。

### 核心思路/方法
提出一种双分支视图条件超网络（view-conditioned hyperNetwork），同时学习视图无关的嵌入表示（共享知识）和视图特定的知识（适应具体视角），将目标视角信息作为先验注入网络参数，使高斯分布能随查询视角动态调整，从而在测试时为不同视图定制化重建辐射场。

### 主要贡献
- 提出UniqueSplat，一种视图条件的前馈三维高斯泼溅模型，支持按查询视角动态生成高斯表示。
- 设计双分支视图条件超网络，同时建模视图共享与视图特定信息。
- 在RealEstate10K、ACID和DTU数据集上超越现有最先进方法，并在跨数据集评估中表现出更强的泛化能力。

### 局限性
摘要未提供足够信息（未提及计算开销、推理速度、对输入视图数量的敏感性、失败案例或潜在限制）。

### 阅读优先级
**高**。理由：针对三维高斯泼溅前馈重建中的视角自适应问题提出了新的解决方案，创新性明确，并在多个主流数据集及跨数据集评估中验证了性能提升，对从事通用三维重建和神经场景表示研究的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

In this paper, we propose UniqueSplat, a view-conditioned feed-forward 3D Gaussian Splatting model to reconstruct customized 3D radiance fields for each view query. Existing feed-forward methods such as pixelSplat and MVSplat aim to generate fixed Gaussians across all views of each scene by minimizing the error between rendered views and ground-truth images. However, such fixed Gaussians generally render images from all views and lack the ability to adapt to specific viewpoints, as they do not incorporate target view information when predicting Gaussians. To address this, our UniqueSplat learns the view-conditioned information as a prior and incorporates this knowledge into network parameters, so that Gaussians are dynamically adjusted in accordance with different views. Specifically, we propose a two-branch view-conditioned hyperNetwork to simultaneously learn view-agnostic embeddings and view-specific knowledge, which not only explores the shareable knowledge from various views, but also adapts the model to specific views at test time. Extensive experiments on widely-used datasets including RealEstate10K, ACID and DTU demonstrate the superiority of UniqueSplat over the state-of-the-art methods. Moreover, UniqueSplat encouragingly outperforms existing methods in cross-dataset evaluation, showing its notable generalization ability.

</details>

#### 2026-08-03 - GIFT: Geometry-Invariant Fine-Tuning for Non-Lambertian Monocular Depth Estimation

**Authors:** Xianghui Fan, Zhaoyu Chen, Bingqian Wu, Dayu Li, Xin Zeng, Huanran Cui, Guangzhen Xu, Xiangru Huang, Hang Yang
**Links:** [abs](https://arxiv.org/abs/2608.02068) - [pdf](https://arxiv.org/pdf/2608.02068)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GIFT: Geometry-Invariant Fine-Tuning for Non-Lambertian Monocular Depth Estimation（GIFT：面向非朗伯单目深度估计的几何不变微调）
- 作者：Xianghui Fan, Zhaoyu Chen, Bingqian Wu, Dayu Li, Xin Zeng, Huanran Cui, Guangzhen Xu, Xiangru Huang, Hang Yang
- 出版日期：2026-08-03
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.02068

### 一句话总结
GIFT 提出一种无需深度标签的参数高效微调框架，利用非朗伯表面在表观变化下几何不变的特性，抑制单目深度基础模型在镜面和透明物体上的深度幻觉。

### 研究问题
单目深度基础模型在非朗伯表面（如镜子、玻璃）上会产生深度幻觉——估计的是反射或透射内容的位置，而非物理表面的实际深度。由于传统深度传感器在此类区域同样不可靠，如何在不依赖实测深度标签的情况下，适应真实世界非朗伯场景成为难题。

### 核心思路/方法
- **关键观察**：非朗伯表面的外观会随反射或透射环境变化，但其底层几何（物理表面位置）保持不变。
- **方法框架**：在保持相机与目标几何固定的条件下，采集多组受控外观变化的 RGB 图像；利用这些观测之间的几何不变性作为监督信号，进行参数高效的模型微调（后训练阶段），从而抑制非朗伯深度幻觉，同时保持基础模型泛化能力。
- **评测方式**：构建受控基准，评估非朗伯深度恢复、外观变化鲁棒性，以及在其余区域的性能保持情况。

### 主要贡献
1. 提出基于几何不变性的无标签微调框架（GIFT），用于非朗伯场景深度估计，无需实测深度标签。
2. 设计受控的数据采集方案（外观变化、几何固定）以利用几何不变性。
3. 构建专门的非朗伯深度恢复基准，涵盖深度恢复质量、外观变化鲁棒性及性能保留三个维度。
4. 在基准和独立真实数据集上验证，GIFT 能改善镜面与透明物体深度预测，同时大体保持基础模型原有性能。

### 局限性
摘要未提供足够信息（如方法对极端表观变化、复杂多非朗伯物体共存场景的处理能力、微调计算成本具体数值、失效边界等均未提及）。

### 阅读优先级
**中**
理由：该工作针对单目深度估计中非朗伯表面这一明确痛点，思路新颖（利用几何不变性替代深度标签），且提供了低成本、实用的解决方案，对从事深度估计、三维重建的研究者有参考价值。但当前摘要未给出量化性能对比细节，若需判断方法优越性，还需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Monocular depth foundation models, benefiting from large-scale synthetic training data, have demonstrated strong generalization. However, they often hallucinate depth on non-Lambertian surfaces, estimating reflected content in mirrors or transmitted content behind glass rather than the physical surface itself. Adapting these models with real-world data is challenging because conventional depth sensors are also unreliable in such regions. We observe that while the appearance of a non-Lambertian surface varies with its reflected or transmitted environment, its underlying geometry remains unchanged. Based on this observation, we propose GIFT (Geometry-Invariant Fine-Tuning), a parameter-efficient post-training framework that requires no measured depth labels. We collect groups of RGB images under controlled appearance changes while keeping the camera and target geometry fixed. GIFT exploits geometric invariance across these observations to suppress non-Lambertian depth hallucinations while retaining general depth estimation capability. We further construct a controlled benchmark that evaluates non-Lambertian depth recovery, robustness to appearance changes, and performance retention in other regions. Experiments on our benchmark and an independent real-world dataset demonstrate that GIFT improves depth prediction for mirrors and transparent objects while largely preserving the base model's performance, providing a practical and low-cost approach for adapting monocular depth foundation models to non-Lambertian scenes.

</details>

#### 2026-08-03 - CHOW-SLAM: Compact Hybrid Representation with Complementary Overlap Window Optimization for RGB-D SLAM

**Authors:** Wenxuan Ji, Jin Xiao, Xiaoguang Hu, Jiaqi Shi, Zichong Jia, Baochang Zhang
**Links:** [abs](https://arxiv.org/abs/2608.01914) - [pdf](https://arxiv.org/pdf/2608.01914)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, simultaneous localization and mapping, SLAM, pose estimation, bundle adjustment, NeRF, neural rendering, rendering, radiance, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CHOW-SLAM: Compact Hybrid Representation with Complementary Overlap Window Optimization for RGB-D SLAM
- 作者：Wenxuan Ji, Jin Xiao, Xiaoguang Hu, Jiaqi Shi, Zichong Jia, Baochang Zhang
- 出版日期：2026-08-03
- 分类：3D Reconstruction & Multi-view Geometry（次要分类：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.01914

### 一句话总结
本文提出CHOW-SLAM，一种通过紧凑混合场景表示与互补重叠窗口优化策略，同时构建空间和时间约束，以提升RGB-D神经SLAM系统重建质量与跟踪精度的方法。

### 研究问题
现有基于NeRF的SLAM系统在有限在线资源下，难以同时构建两类约束：来自场景表示的紧凑且可区分的空间约束，以及来自历史观测的持续时间约束。如何平衡并有效利用这两类约束是本文要解决的核心问题。

### 核心思路/方法
- **空间约束**：提出紧凑的参数化哈希（P-H）混合表示，基于平面和网格在不同尺度上组织P与H分支组件；使用统一多输出解码器对齐TSDF与密度诱导的射线终止分布，在紧凑参数预算下保持几何和外观。
- **时间约束**：提出互补重叠窗口策略，在固定预算内保留近期帧、选择高重叠局部帧，并引入时间分布的历史关键帧，避免优化被短期重叠或弱相关历史观测主导。
- **优化调度**：采用损失感知的关键帧插入和捆绑调整调度，使优化适应跟踪质量。
- **位姿初始化**：使用ORB特征跟踪和几何位姿估计进行初始化，随后通过神经渲染优化提升跟踪稳定性。

### 主要贡献
1. 提出显式构建互补空间与时间约束的密集RGB-D SLAM框架CHOW-SLAM。
2. 设计紧凑的参数化哈希混合表示，结合统一多输出解码器，在紧凑参数下保持重建质量。
3. 提出互补重叠窗口策略及损失感知的调度机制，提升优化稳定性与效率。
4. 在多个数据集上验证，重建质量和跟踪精度均优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对神经SLAM中空间与时间约束难以兼顾的关键挑战，提出了兼具表示创新（P-H混合表示）和优化策略创新（互补重叠窗口）的完整框架，实验结果在重建质量和跟踪精度上均优于SOTA，且提供了开源代码，对RGB-D神经SLAM方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Simultaneous localization and mapping (SLAM) based on Neural Radiance Fields (NeRF) enables dense, continuous scene reconstruction. However, existing systems operating with limited online resources struggle to simultaneously construct two types of constraints, namely, compact yet discriminative spatial constraints derived from scene representations and persistent temporal constraints derived from historical observations. To address this challenge, we propose CHOW-SLAM, a dense RGB-D SLAM framework that explicitly constructs these complementary spatial and temporal constraints. Spatially, we propose a compact parametric-hash (P-H) hybrid representation that organizes components based on planes and grids across scales in P and H branches. A unified multi-output decoder further aligns the ray termination distributions induced by TSDF and density, preserving geometry and appearance under a compact parameter budget. Temporally, we propose a complementary overlap-window strategy to prevent optimization from being dominated by short-term overlap or weakly related historical observations. Within a fixed budget, the strategy retains recent frames, selects high-overlap local frames, and introduces temporally distributed historical keyframes. Loss-aware keyframe insertion and bundle adjustment scheduling further adapt optimization to tracking quality. In addition, ORB-based tracking and geometric pose estimation are used for pose initialization, followed by neural rendering optimization to improve tracking stability. Extensive evaluations on multiple datasets demonstrate that CHOW-SLAM outperforms state-of-the-art methods in both scene reconstruction quality and camera tracking accuracy. The source code is available at https://github.com/jinjidexiaohuoban/CHOW-SLAM.

</details>

#### 2026-08-02 - FeDepth: Federated Learning for Depth Estimation under Robot Heterogeneity

**Authors:** Ganghyeon Lee, Inha Lee, Junhee Lee, Jeongeon Lee, Sung Whan Yoon, Kyungdon Joo
**Links:** [abs](https://arxiv.org/abs/2608.01129) - [pdf](https://arxiv.org/pdf/2608.01129)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, robot perception

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FeDepth: Federated Learning for Depth Estimation under Robot Heterogeneity
- 作者：Ganghyeon Lee, Inha Lee, Junhee Lee, Jeongeon Lee, Sung Whan Yoon, Kyungdon Joo
- 出版日期：2026-08-02T10:11:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.01129

### 一句话总结
本文提出 FeDepth，一个基于描述符的软聚类联邦学习框架，用于在机器人平台异构性导致的非独立同分布（non-IID）场景下提升深度估计的鲁棒性。

### 研究问题
在机器人异构性（平台、环境、深度分布差异）导致的联邦学习域偏移下，如何在不假设客户端域可清晰分离的情况下，有效提升深度估计性能？

### 核心思路/方法
- 提出两个新的、贴近实际机器人部署的 non-IID 场景，反映平台、环境和深度分布层面的异构性。
- 提出 FeDepth，一种基于描述符（descriptor-based）的聚类联邦学习框架，采用软聚类方式建模客户端关系。
- 与硬聚类方法不同，FeDepth 允许客户端同时隶属于多个聚类簇，以捕捉机器人环境中连续且模糊的域过渡。

### 主要贡献
- 揭示了机器人感知（尤其是深度估计）中现有聚类联邦学习对“客户端域清晰可分离”假设的失效问题。
- 引入两个真实且未被探索的非 IID 场景，涵盖平台、环境和深度分布异构性。
- 提出 FeDepth 软聚类联邦学习框架，在多种深度估计架构上相比标准联邦学习和聚类联邦学习基线，持续提升鲁棒性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对联邦学习在机器人深度估计中的实际异构性问题提出了新的场景定义和软聚类方法，实验部分显示在多个架构上均有提升，且属于较新的研究方向。摘要指出其解决了已有聚类联邦学习的假设局限，对研究联邦学习在机器人感知领域的应用有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Although recent robot perception research emphasizes training on data from diverse environments to improve generalization, most existing methods still rely on centralized learning, which is inefficient and difficult to scale across heterogeneous robot platforms. Federated learning (FL) offers an alternative by enabling distributed training without raw data transfer, but it suffers from severe performance degradation under domain shifts caused by heterogeneity across clients. In real robotic deployments, data distributions often overlap across platforms, environments, and sensing conditions, making it difficult to partition clients into clearly separated domains. However, this characteristic breaks the assumption of clearly separable client domains commonly used in clustered FL. To address this gap in robot perception, particularly in depth estimation, we introduce two realistic and unexplored non-IID scenarios that reflect heterogeneity in terms of platform, environment, and depth distribution. We then propose FeDepth, a descriptor-based clustered FL framework that models client relationships through soft clustering. Unlike hard clustering methods that assume clearly separated clusters, FeDepth allows clients to participate in multiple clusters, capturing continuous and ambiguous domain transitions commonly observed in robotic environments. Extensive experiments demonstrate that FeDepth consistently improves robustness over standard FL and clustered FL baselines across multiple depth estimation architectures, providing a practical and effective solution for federated robot perception. Our project page is available at https://vision3d-lab.github.io/fedepth/.

</details>

#### 2026-08-02 - Swimm3R: Splatting with Medium-aware SfM for Underwater 3D Reconstruction

**Authors:** Minseong Kweon, Junaed Sattar
**Links:** [abs](https://arxiv.org/abs/2608.00950) - [pdf](https://arxiv.org/pdf/2608.00950)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, structure from motion, SfM, Gaussian Splatting, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Swimm3R: Splatting with Medium-aware SfM for Underwater 3D Reconstruction
- 作者：Minseong Kweon, Junaed Sattar
- 出版日期：2026-08-02
- 分类：3D Reconstruction & Multi-view Geometry；次要分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.00950

### 一句话总结
Swimm3R 是一个结合介质感知运动恢复结构（SfM）与水下 Beta 泼溅（Splatting）的统一框架，旨在克服水下散射与衰减引起的三维重建失败问题。

### 研究问题
水下三维重建中，由于水的散射与光衰减效应导致的几何重建不稳定、点云质量差以及渲染精度下降的问题。

### 核心思路/方法
- 将空气中的几何先验蒸馏（distill）到一个前馈骨干网络（feed-forward backbone）中。
- 使用一个物理头（physics head）回归水下图像形成参数、相机位姿以及恢复后的点云。
- 提出 Underwater Beta Splatting，扩展高斯泼溅，使用 Beta 基元（Beta primitives）和散射感知的几何梯度，以实现稳定的水下几何表示。
- 建立了巴巴多斯水下视频数据集（Barbados underwater video dataset），用于在真实挑战性水下环境中验证方法。

### 主要贡献
1. 提出 Swimm3R，一个将介质感知 SfM 与水下 Beta 泼溅结合的统一三维重建框架。
2. 引入 Underwater Beta Splatting，用 Beta 基元替代传统高斯基元并加入散射感知梯度。
3. 建立巴巴多斯水下视频数据集。
4. 实验表明，相较于 WaterSplatting，平均 PSNR 提升 1.47 dB；下游定位任务中 RRA@15 和 RTA@15 分别提升 2.0 和 2.4 个百分点。

### 局限性
摘要未提供足够信息，未提及该方法的计算开销、对特定水质/深度范围的依赖、泛化到其他水下环境的限制，或失败案例等。

### 阅读优先级
**高**。理由：该工作针对水下三维重建这一高难度且应用价值明确的场景提出新框架，融合了 SfM 与泼溅渲染，并配有新数据集与定量提升（PSNR、定位精度），对 3D 重建、水下视觉及神经渲染方向均有参考意义；发表时间较新，属于当前热点交叉方向。

</details>

<details>
<summary>Abstract</summary>

We propose Swimm3R, a unified framework that combines medium-aware structure-from-motion (SfM) with Underwater Beta Splatting to address scattering- and attenuation-induced failures in underwater 3D reconstruction. Swimm3R distills in-air geometric priors into a feed-forward backbone and uses a physics head to regress underwater image-formation parameters, camera poses, and restored point clouds. Additionally, we introduce Underwater Beta Splatting, which extends Gaussian splatting with Beta primitives and scattering-aware geometric gradients for stable underwater geometry representation. We further establish the Barbados underwater video dataset to demonstrate the effectiveness of our method in challenging underwater environments. On this dataset, Swimm3R robustly recovers underwater scene structure under challenging scattering conditions, yielding coherent seafloor geometry. Using these predicted point clouds, the proposed Underwater Beta Splatting improves average PSNR by $1.47$ dB over WaterSplatting while increasing downstream localization performance by $2.0$ and $2.4$ percentage points in RRA@15 and RTA@15, respectively.

</details>

#### 2026-08-02 - Stipple: Real-Time Incremental Gaussian Splatting with Visual-Inertial Tracking

**Authors:** Kilian Northoff, Mateo de Mayo, Daniel Cremers
**Links:** [abs](https://arxiv.org/abs/2608.00931) - [pdf](https://arxiv.org/pdf/2608.00931)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, simultaneous localization and mapping, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, robotics, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stipple: Real-Time Incremental Gaussian Splatting with Visual-Inertial Tracking
- 作者：Kilian Northoff, Mateo de Mayo, Daniel Cremers
- 出版日期：2026-08-02
- 分类：3D Reconstruction & Multi-view Geometry；次级分类：Neural Scene Representations & Rendering、Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.00931

### 一句话总结
本文提出一种将视觉惯性跟踪系统与3D高斯泼溅相结合的实时增量重建方法，替代传统3DGS的繁重预处理和训练流程。

### 研究问题
如何在实时场景（如机器人或XR应用）中，高效利用视觉惯性跟踪提供的信息，实现3D高斯泼溅的在线增量训练与即时重建，克服传统3DGS预处理和训练开销大的问题。

### 核心思路/方法
- 基于Basalt的视觉惯性跟踪系统提供高效率的定位信息。
- 在Brush（一个基于Rust、硬件厂商无关的高效3DGS实现）之上构建新型增量训练方法。
- 利用视觉惯性跟踪系统产生的信息，替代传统3DGS的大量预处理与训练步骤，转为更高效的增量训练策略。
- 提出并组合多项实际工程改进，提升训练管线效率，使其能与跟踪线程并行、实时运行。

### 主要贡献
- 提出一套实时同时进行跟踪与重建的完整方法，融合视觉惯性里程计与增量式3DGS。
- 论证了3DGS的重预处理和训练步骤可被基于VIO信息的增量策略有效替代。
- 展示了SLAM与3DGS互补结合在实时3D重建中的潜力。

### 局限性
摘要未提供足够信息，无法得知具体精度、速度指标、场景类型限制、内存开销或与现有方法的定量对比结果。

### 阅读优先级
**中**。理由：该工作面向实时重建的应用方向（机器人/XR），具有明确的系统集成创新性，但摘要未给出定量实验结果和详细性能评估，需进一步阅读全文判断实际效果与工程价值。若非该领域研究者，可先关注摘要中的技术框架即可。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) provides efficient rendering of photo-realistic scenes, but its heavy preprocessing and training steps make it a poor fit for applications that require real-time reconstruction in robotics or XR. This capability is important since it allows immediate feedback and interaction with new environments. Visual-inertial odometry (VIO) and simultaneous localization and mapping (VI-SLAM) systems, on the other hand, specifically target these real-time applications, which makes them a good choice for integration with 3DGS. We propose a new method that tracks and reconstructs simultaneously in real-time by leveraging an efficient visual-inertial tracking system based on Basalt together with a novel incremental method built on top of Brush, an efficient Rust-based GPU-vendor-agnostic implementation of 3D Gaussian Splatting. We show that many of the heavy preprocessing and training steps of 3DGS can be replaced with a more efficient incremental training strategy that has direct access to the information generated by the visual-inertial tracking system. Furthermore, we propose and combine multiple practical improvements to increase the efficiency of the training pipeline and adapt it to run in real-time, parallel to the tracking thread. This work highlights the value of exploiting the complementary nature of SLAM and 3DGS, and how that can lead to promising results for real-time 3D reconstruction.

</details>

### 2026-07

#### 2026-07-30 - Beyond Visual Ambiguity: Guiding Robust Monocular Depth Estimation in Challenging Scenarios via Detailed Long Captions

**Authors:** Junrui Zhang, Jiaqi Li, Yiran Wang, Liao Shen, Zhiguo Cao
**Links:** [abs](https://arxiv.org/abs/2607.28285) - [pdf](https://arxiv.org/pdf/2607.28285)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Visual Ambiguity: Guiding Robust Monocular Depth Estimation in Challenging Scenarios via Detailed Long Captions
- 作者：Junrui Zhang, Jiaqi Li, Yiran Wang, Liao Shen, Zhiguo Cao
- 出版日期：2026-07-30T14:32:02Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.28285

### 一句话总结
本文提出CapDepth框架，利用详细长文本描述作为语言引导，以缓解单目深度估计在非朗伯表面和恶劣天气等挑战场景中的视觉歧义问题。

### 研究问题
单目深度估计（MDE）在非朗伯表面和恶劣天气条件下，由于单张图像信息有限导致视觉歧义，现有方法通常孤立地通过图像修复或增强处理这些场景，鲁棒性提升有限。基于此，本文研究如何借助语言模态的详细长描述能力，有效引导深度估计模型应对这些挑战场景。

### 核心思路/方法
本文提出CapDepth框架，核心包括三个设计：
1. **详细长描述输入模板**：显式编码多个原子句子之间的丰富空间关系，为模型提供更全面的场景信息。
2. **动态描述编码器**：通过渐进式掩码注意力机制，从长描述中提取细粒度的、与深度相关的文本特征。
3. **文本自适应解码器**：利用稳定的自适应层归一化，用文本特征引导增强的深度解码过程。

### 主要贡献
- 提出CapDepth框架，首次将详细长描述系统地用于引导单目深度估计，缓解挑战场景中的视觉歧义。
- 设计详细长描述输入模板、动态描述编码器和文本自适应解码器三个组件，分别解决先前语言集成MDE方法中文本信息有限、全局文本特征粗糙、深度解码阶段语言引导不足的问题。
- 在实验中，CapDepth在非朗伯表面场景深度误差降低25.0%，恶劣天气条件下降低22.0%，优于现有最先进方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目深度估计中具有实际挑战性的场景（非朗伯表面、恶劣天气）提出了创新性的语言引导框架，报告的性能提升幅度较大（误差降低超过20%），且研究问题明确、方法设计有针对性，对视觉-语言模型与深度估计交叉方向具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation (MDE) faces challenges with non-Lambertian surfaces and adverse weather conditions due to the visual ambiguities inherent in single-image limited information. Existing works address them in isolation via image inpainting or augmentation, yielding limited robustness gains. Language, as a powerful complementary modality to vision, is demonstrated to enhance the visual perception capabilities of vision-language models (VLMs) via detailed long captions. However, prior language-integrated MDE methods fail to fully harness this potential due to short text input with limited information, coarse global text feature learning, and limited language guidance during depth decoding. To address these limitations, we propose CapDepth, a novel framework for robust MDE that leverages guidance from detailed long captions to alleviate visual ambiguities in both challenging scenarios. First, we design a detailed long caption input template that explicitly conveys rich spatial relationships among multiple atom sentences. Second, a dynamic caption encoder is introduced to extract fine-grained depth-relevant text features via progressive masked attention. Finally, we propose a text-adaptive decoder that guides enhanced depth decoding with text features via stable adaptive layer normalization. Extensive experiments validate the efficacy of CapDepth, which outperforms state-of-the-art methods, achieving depth error reductions of 25.0% on non-Lambertian surfaces and 22.0% under adverse weather conditions.

</details>

#### 2026-07-30 - Convolutional Neural Shading for High-Quality 3D Reconstruction from Multi-View Images

**Authors:** Juheon Hwang, Taewan Kim, Heeseok Oh, Jiwoo Kang
**Links:** [abs](https://arxiv.org/abs/2607.28132) - [pdf](https://arxiv.org/pdf/2607.28132)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, differentiable rendering, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Convolutional Neural Shading for High-Quality 3D Reconstruction from Multi-View Images
- 作者：Juheon Hwang, Taewan Kim, Heeseok Oh, Jiwoo Kang
- 出版日期：2026-07-30
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.28132

### 一句话总结
本文提出一种名为卷积神经着色（CNS）的新管线，通过引入卷积神经着色器和细粒度位移网络，从多视图图像重建更高质量的3D形状。

### 研究问题
如何克服现有神经可微渲染方法中仅使用单点几何信息（如表面位置和法线）导致的局部几何细节缺失问题，特别是在暗区和无纹理区域，以及图像边界处的表面不规则性。

### 核心思路/方法
- 采用**卷积神经着色器（convolutional neural shader）**替代单点着色模型，利用卷积操作捕捉表面邻域信息，从而在暗区和无纹理区域也能捕获几何变化，提升几何预测精度。
- 引入**细粒度位移网络（fine-detail displacement network）**，利用表面几何的空间信息，在渲染坐标中关联相邻值以学习精细位移细节，从而缓解图像边界处的表面不规则问题。

### 主要贡献
- 提出一种新的CNS管线，将卷积神经着色用于多视图3D重建，有效克服单点信息局限。
- 设计细粒度位移网络，改善图像边界处的表面质量。
- 实验表明，与当前最先进方法相比，重建形状和渲染图像质量均有显著提升。

### 局限性
摘要未提供足够信息；摘要中未提及方法在极端几何、大规模场景、计算开销、训练时间或泛化性等方面的潜在限制。

### 阅读优先级
**高**。理由：该工作针对神经辐射场/神经渲染在几何细节重建中的核心瓶颈提出新思路，且实验显示质量提升显著，属于近期多视图重建与神经渲染方向的前沿方法，适合该领域研究者跟进。

</details>

<details>
<summary>Abstract</summary>

We propose a convolutional neural shading (CNS), a novel pipeline to reconstruct high-quality 3D shapes from multi-view images. Several recent studies have used neural radiance fields and other neural differentiable rendering methods to understand 3D geometry. However, these approaches rely on single-point geometric information, such as positions and normals of the surface, leading to a lack of detailed local geometry. Our approach addresses the inherent limitations of single-point information by leveraging a neural shader to capture variations even in dark and textureless regions with a convolutional neural shader, resulting in far more accurate geometry predictions. Additionally, our method mitigates surface irregularities at image boundaries by introducing a fine-detail displacement network, which utilizes spatial information of surface geometry and learns fine displacement details by correlating neighboring values in the rendering coordinates. Through extensive experiments, our proposed method has demonstrated significant quality improvements in the reconstructed shapes and rendered images over current state-of-the-art methods.

</details>

#### 2026-07-30 - Endo-NeRF++: Uncertainty-Aware Neural Rendering with Multi-Resolution Hash Encoding for Dynamic Surgical Scene Reconstruction

**Authors:** Gousia Habib, Laura Ruotsalainen
**Links:** [abs](https://arxiv.org/abs/2607.27825) - [pdf](https://arxiv.org/pdf/2607.27825)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, NeRF, neural rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Endo-NeRF++: Uncertainty-Aware Neural Rendering with Multi-Resolution Hash Encoding for Dynamic Surgical Scene Reconstruction
- 作者：Gousia Habib, Laura Ruotsalainen
- 出版日期：2026-07-30
- 分类：3D Reconstruction & Multi-view Geometry（次要分类：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2607.27825

### 一句话总结
Endo-NeRF++是一种面向动态手术场景的神经渲染框架，通过多分辨率哈希编码、时空特征融合与不确定性引导的自适应采样，在变形内镜场景中提升了重建精度和时间一致性。

### 研究问题
如何在存在组织变形、遮挡、镜面反射和受限视角的动态手术场景中，实现高精度且时间连贯的神经渲染重建。

### 核心思路/方法
在EndoNeRF基础上扩展，引入三项关键机制：
1. 多分辨率哈希网格编码，同时捕捉粗粒度和细粒度的解剖细节；
2. 时间特征融合，在组织变形和手术工具遮挡期间维持稳定的重建；
3. 不确定性引导的自适应采样，将更多采样点分配到不确定性高的区域，从而提升渲染质量和几何连贯性。

### 主要贡献
- 提出Endo-NeRF++框架，将不确定性估计引入动态手术场景的神经渲染；
- 结合多分辨率哈希编码和时序特征融合，有效处理形变与遮挡；
- 不确定性驱动的自适应采样机制，在机器人手术视频序列上较EndoNeRF基线取得显著提升：PSNR最高提升1.22 dB（4.3%），SSIM最高提升5.3%，LPIPS最高降低55.1%。

### 局限性
摘要未提供足够信息，无法获知该方法在计算开销、泛化能力、不同手术类型或更长视频序列上的表现，也未提及与除EndoNeRF外其他方法的比较或失败案例。

### 阅读优先级
**中**  
理由：该工作针对手术场景重建这一特定领域，方法上有明确创新（不确定性引导采样+多分辨率哈希编码），并与基线取得了可观提升，适合关注神经渲染或医学影像重建的读者；但摘要未提供实验设置细节和更广泛对比，普适性和方法局限尚不明朗，可不作为紧急必读。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic surgical scenes is crucial for robot-assisted minimally invasive surgery; however, it continues to be difficult because of tissue deformation, occlusions, specular reflections, and restricted viewpoints. In this study, we introduce Endo-NeRF++, a neural rendering framework that accounts for uncertainty in the reconstruction of dynamic surgical scenes. Expanding on EndoNeRF, the suggested approach incorporates multi-resolution hash-grid encoding, temporal feature merging, and uncertainty-informed adaptive sampling to enhance reconstruction accuracy and temporal coherence in deformable endoscopic scenes.The multi-resolution hash-grid representation within the framework effectively captures both coarse and fine anatomical details, while temporal feature blending ensures stable reconstruction during tissue deformation and surgical tool occlusions. Additionally, uncertainty-driven adaptive sampling assigns more samples to uncertain areas to enhance rendering quality and geometric coherence. Experiments on robotic surgical video sequences demonstrate that the proposed uncertainty-guided adaptive sampling improves PSNR by up to 1.22\,dB (4.3\%), increases SSIM by up to 5.3\%, and reduces LPIPS by up to 55.1\% compared with the EndoNeRF baseline.

</details>

#### 2026-07-30 - EgoGVAE: Ego-body Mesh Reconstruction via Guided Variational Autoencoder

**Authors:** Jaehun Jung, Wonjun Kim
**Links:** [abs](https://arxiv.org/abs/2607.27755) - [pdf](https://arxiv.org/pdf/2607.27755)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoGVAE: Ego-body Mesh Reconstruction via Guided Variational Autoencoder
- 作者：Jaehun Jung, Wonjun Kim
- 出版日期：2026-07-30
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.27755

### 一句话总结
本文提出一种基于引导变分自编码器的单步推理方法，仅利用头部姿态即可快速重建全身网格，推理速度比扩散式方法快50倍以上。

### 研究问题
如何仅从头部姿态（单一关节轨迹）恢复未观察到的全身姿态与网格，同时避免扩散模型迭代过程带来的高计算成本和时间开销。

### 核心思路/方法
- 构建一个以全身姿态为输入的引导网络（变分自编码器），学习全身姿态的潜在分布。
- 设计一个头到运动的网络（head-to-motion network），使其学习到的潜在分布与引导网络的分布对齐。
- 推理时从头姿态采样的“引导分布”潜在特征可直接解码为自然的全身姿态，仅需单步采样即可完成重建，无需迭代。

### 主要贡献
- 提出一种简洁新颖的引导变分自编码器框架，利用潜在空间对齐实现高效全身网格重建。
- 相比扩散式方法，推理速度提升超过50倍（单步采样）。
- 在基准数据集上验证了该方法在ego-body网格重建任务中的有效性和性能提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法在保证全套姿重建质量的同时，将推理速度提升至扩散模型的50倍以上，对头戴设备/智能眼镜等实时应用具有重要意义；且方法简洁，潜在空间对齐思路具有可扩展性，适合关注高效人体重建与生成模型的读者。

</details>

<details>
<summary>Abstract</summary>

We address the problem of recovering the full-body mesh from only the head pose. This task has become essential for various applications based on head-mounted devices or smart glasses. The challenge of this task lies in estimating the pose information of unobserved body parts based solely on a single joint (i.e., head) trajectory. Several studies have begun to adopt head-conditioned generative models, however, such previous methods are costly and time-consuming due to the diffusion-based iterative process. As an alternative, we propose a simple yet novel method that leverages the latent space of the guidance network, which is designed as a variational autoencoder taking full-body poses as inputs. By enforcing latent distributions of this guidance network and our head-to-motion network to be similar, latent features sampled from the 'guided' distribution, i.e., distribution learned in our head-to-motion network, can be reliably decoded for natural representations of full-body poses even only with the head pose. One important advantage of the proposed method is that one-step sampling scheme achieves remarkably fast inference (more than 50 times faster) compared to diffusion-based approaches. Experimental results on benchmark datasets show that the proposed method efficiently improves the performance of ego-body mesh reconstruction.

</details>

#### 2026-07-29 - VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion

**Authors:** Zador Pataki, Paul-Edouard Sarlin, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2607.27194) - [pdf](https://arxiv.org/pdf/2607.27194)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** image matching, structure from motion, SfM, simultaneous localization and mapping, SLAM, monocular depth, camera calibration, mapping, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion
- 作者：Zador Pataki, Paul-Edouard Sarlin, Marc Pollefeys
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2607.27194

### 一句话总结
本文提出VidMap系统，通过融合SLAM的时序约束与离线SfM的全局优化能力，实现了任意未校准长视频的度量重建。

### 研究问题
现有视频位姿恢复方法存在局限：SLAM依赖初始化、对瞬态故障敏感且需已知相机校准；SfM忽略图像顺序，在视觉对称和极端运动场景下鲁棒性不足。因此，该文致力于解决如何结合两种方法的优势，实现鲁棒且准确的视频度量重建。

### 核心思路/方法
- 结合SLAM的强时序约束与SfM的全局优化灵活性，将时间顺序作为闭环检测的关键信息。
- 利用近期宽基线密集图像匹配的进展提升匹配质量。
- 使用度量单目深度先验增强全局优化过程。

### 主要贡献
- 提出一种新系统，融合SLAM时序约束与离线SfM全局优化，支持未校准视频的度量重建。
- 将时序信息作为闭环检测的“一等公民”，提升可靠性。
- 在包含极端运动和视觉对称的多样困难数据集上，比现有经典/学习的SLAM和SfM方法（无论是否已知校准）更鲁棒、更准确。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该文针对视频重建领域SLAM与SfM的矛盾提出融合方案，技术思路清晰且实验验证鲁棒性优势，适合对3D重建、视觉SLAM或机器人导航感兴趣的读者；但摘要未提及具体性能指标与消融实验细节，需进一步阅读正文判断方法可复现性和实际效果。

</details>

<details>
<summary>Abstract</summary>

Accurately recovering the camera's calibration and metric poses for any unconstrained video would unlock large-scale training data for navigation and scene understanding. The dominant approaches to this problem are severely limited: Simultaneous Localization and Mapping (SLAM) is sensitive to initialization and transient failures due to its causal, incremental nature; it is often over-optimized for real-time operation and generally requires known camera calibration; while Structure-from-Motion (SfM) typically forgoes any image ordering, enabling optimal initialization and global optimization, but lacks robustness to visual symmetries and extreme motions. To bridge this gap, we introduce a system that combines the strong sequential constraints of SLAM with the flexibility and global optimization of offline SfM, enabling the metric reconstruction of arbitrary, long, uncalibrated videos. This system leverages recent advances in wide-baseline dense image matching, treats temporal ordering as a first-class citizen for reliable loop closure, and augments global optimization with metric monocular depth priors. As a result, thorough evaluations on diverse, challenging datasets that exhibit extreme motion and visual symmetries reveal that our approach is significantly more robust and accurate than both state-of-the-art SLAM and SfM, classical or learned, with given or unknown camera calibration. The code is publicly available at https://github.com/cvg/vidmap.

</details>

#### 2026-07-29 - Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for Decision-Critical Applications

**Authors:** Piyush Jain, Kousik Dasgupta, Rajarshi Roy, Subarna Tripathi
**Links:** [abs](https://arxiv.org/abs/2607.27145) - [pdf](https://arxiv.org/pdf/2607.27145)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, monocular depth, embodied AI, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for Decision-Critical Applications
- 作者：Piyush Jain, Kousik Dasgupta, Rajarshi Roy, Subarna Tripathi
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry; Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.27145

### 一句话总结
本文提出ByDeWay-V2框架，通过向多模态大语言模型（MLLM）的提示中注入显式的空间关系谓词和深度线索，在无需训练的情况下提升了空间推理的准确性和可审计性，尤其适合资源受限的实时决策场景。

### 研究问题
多模态大语言模型在关键决策应用（如机器人、具身AI）中，其空间判断不透明且存在细粒度空间理解不足和物体幻觉问题；现有方法（如ByDeWay的LDP）在处理同一几何平面内物体间的投影和拓扑空间关系时表现不足。

### 核心思路/方法
- 采用开放词汇物体检测器（YOLO-World-L）计算图像中检测到的物体之间的成对几何关系。
- 将这些关系转化为人类可读的结构化空间谓词（如“left of”、“inside”等），并将其与深度线索（来自单目深度估计）一起注入MLLM的提示中。
- 整个流程无需训练，将3D场景深度与2D空间语义桥接，同时提供可审计的证据以支持下游决策。

### 主要贡献
1. 提出了ByDeWay-V2框架，通过显式空间关系谓词增强MLLM的空间推理能力，同时保持可解释性。
2. 在VSR和BLINK空间推理子集上，该框架显著提升了多个MLLM的性能：例如在BLINK空间子集上，对于Qwen2.5-VL，相对于LDP方法F1分数相对提升46%；将BLIP-Base在VSR上的近乎随机性能恢复至F1=0.53。
3. 提供轻量级配置（在CPU上仅需40个token上下文预算），证明了框架在资源受限实时决策场景中的适用性。

### 局限性
摘要未提供足够信息（如具体失败案例、对其他任务或更大模型的影响、深度估计误差的影响等）。

### 阅读优先级
中
- 理由：该工作专注于视觉空间推理这一具体方向，并提出了实用的轻量级改进方法（无需训练）。对于从事具身AI、机器人及可解释AI的研究者有一定参考价值，但对于广义的计算机视觉或语言模型研究者，其方法限定性较强。

</details>

<details>
<summary>Abstract</summary>

As Multimodal Large Language Models (MLLMs) are increasingly deployed in decision-critical pipelines such as robotics, embodied AI, and safety monitoring, the opacity of their spatial judgments limits operator trust and auditability. MLLMs demonstrate strong reasoning but often struggle with fine-grained spatial understanding and object hallucination. Prior work, ByDeWay, introduced Layered-Depth-Based Prompting (LDP), a training-free framework that mitigates hallucinations by structuring prompts using monocular depth estimation. However, coarse depth layering falls short in resolving object-to-object spatial relationships within the same geometric plane, such as projective ("left of", "above") and topological ("inside", "touching") relations. We propose ByDeWay-V2, which integrates explicit spatial relational context alongside depth cues, expressed as human-readable predicates that serve as auditable evidence for downstream decision support. Using an open-vocabulary object detector (YOLO-World-L), our framework computes pairwise geometric relations between detected objects and injects them as structured spatial predicates into the MLLM prompt, bridging 3D scene depth and 2D spatial semantics without any training. We evaluate ByDeWay-V2 on the Visual Spatial Reasoning (VSR) and BLINK benchmarks across multiple MLLMs, with hallucination grounding assessed via POPE. On the BLINK spatial subset, ByDeWay-V2 achieves a 46 percent relative F1 improvement over LDP for Qwen2.5-VL, and recovers BLIP-Base's spatial reasoning on VSR from near-random performance to a competitive F1 of 0.53. Our lightest configuration operates under a strict 40-token context budget on CPU, showing the framework's suitability for resource-constrained, real-time decision-support settings.

</details>

#### 2026-07-29 - JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation

**Authors:** Ionuţ Grigore, Călin-Adrian Popa
**Links:** [abs](https://arxiv.org/abs/2607.26600) - [pdf](https://arxiv.org/pdf/2607.26600)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation
- 作者：Ionuţ Grigore, Călin-Adrian Popa
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.26600

### 一句话总结
JEPADepth 提出一种自监督单目深度估计方法，在标准光度损失基础上，引入基于I-JEPA的掩码预测表示学习损失，以提升模型性能，且在推理时不增加额外开销。

### 研究问题
如何通过引入掩码预测表示学习来增强自监督单目深度估计中基于光度重建损失的训练效果，同时不改变推理时的模型结构。

### 核心思路/方法
1. 在标准光度重建流程上，增加一个基于预训练DINOv3 Vision Transformer编码器的掩码预测损失（JEPA目标）。
2. 该损失在表示空间中计算：一个预测器根据可见上下文区域的嵌入，推断被掩码的目标区域嵌入；目标编码器和预测器仅在训练阶段使用，推理时丢弃。
3. 整体框架在KITTI上训练，与同一DINOv3光度基线对比，性能有提升。

### 主要贡献
摘要未提供足够信息以提取独立贡献列表。从摘要可推断：提出了一种结合I-JEPA的掩码预测损失与光度损失的深度估计框架，在三个公开基准（KITTI、Make3D、Cityscapes）上取得有竞争力的结果，尤其在零样本迁移场景下达到最佳或接近最佳性能。

### 局限性
摘要未提供关于局限性、失败案例或计算成本等信息，因此无法进行分析。

### 阅读优先级
中  
理由：该方法在自监督深度估计领域表现出竞争力，零样本迁移性能突出，但创新点主要是将现有I-JEPA损失嫁接到光度框架上，且实验细节未深入给出。如关注自监督表示学习与深度估计结合，可阅读；若需理论突破或详尽实验分析，优先级较低。

</details>

<details>
<summary>Abstract</summary>

Self-supervised monocular depth estimation typically relies on photometric reconstruction losses that couple depth, pose, and appearance assumptions. In this paper, we propose JEPADepth, a self-supervised monocular depth framework that incorporates a complementary training objective inspired by Image Joint-Embedding Predictive Architectures (I-JEPA) for self-supervised depth learning. Our method augments a standard photometric pipeline with a masked prediction loss computed in the representation space of a pretrained DINOv3 Vision Transformer encoder. A predictor infers target-region embeddings from visible context-region embeddings under structured masking, and is discarded along with the target encoder at inference time, adding no deployment cost. On KITTI, adding the JEPA objective consistently improves performance over the same DINOv3-based photometric baseline, without changing the inference-time architecture. Compared to prior monocular self-supervised methods, JEPADepth is competitive with state-of-the-art transformer-based approaches and outperforms strong CNN-based baselines on the standard benchmark. In zero-shot transfer (trained on KITTI and evaluated without fine-tuning), JEPADepth achieves the best or near-best performance among the compared methods on both Make3D and Cityscapes across multiple metrics.

</details>

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-03 - InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthesis

**Authors:** Jiawei Wang, Hao Yu, Yongzhen Hu, Xinyi Yang, Tao Ni, Xin Zhan, Junbo Chen, Xiaowei Zhou, Ruizhen Hu, Sida Peng
**Links:** [abs](https://arxiv.org/abs/2608.02437) - [pdf](https://arxiv.org/pdf/2608.02437)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, view synthesis, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthesis
- 作者：Jiawei Wang, Hao Yu, Yongzhen Hu, Xinyi Yang, Tao Ni, Xin Zhan, Junbo Chen, Xiaowei Zhou, Ruizhen Hu, Sida Peng
- 出版日期：2026-08-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02437

### 一句话总结
InfiniSplat 提出了一种从单张图像前馈生成 3D 高斯泼溅（3DGS）的框架，通过将像素对齐的高斯表示改为表面对齐表示，以提升大基线视角变化下的新视角合成质量。

### 研究问题
现有单图像前馈 3DGS 方法通常采用像素对齐表示，即从固定图像网格位置预测高斯属性。这种表示在近距离视角时效果较好，但高斯与场景表面弱耦合，在大视角变化下难以保持结构一致性，导致新视角渲染质量下降。本研究旨在解决这一问题，实现大基线单目视图合成。

### 核心思路/方法
InfiniSplat 的核心是从像素对齐表示转向表面对齐表示，具体包括两步：
1. **几何引导采样**：根据深度诱导的局部表面结构放置二维支撑点（2D supports），使支撑点贴合场景表面；
2. **查询条件隐式解码器**：在这些支撑点处查询图像特征，并通过隐式解码器预测高斯属性。

通过将支撑点定位在几何结构上，并将高斯预测与固定像素中心解耦，该方法生成的 3DGS 布局能更好地贴合场景表面，减少因网格离散化造成的分散基元。

### 主要贡献
- 提出 InfiniSplat，一种前馈单图像 3DGS 框架，采用表面对齐表示替代像素对齐表示；
- 设计了几何引导采样 + 查询条件隐式解码的组合方式，使高斯布局更贴合场景表面；
- 在多个跨数据集新视角合成评测中，相比其他单图像前馈基线方法取得最优性能；
- 展示从 Hypersim 室内合成数据训练到复杂开放世界场景的零样本泛化能力。

### 局限性
摘要未提供足够信息。摘要未明确讨论局限性，如方法对深度估计误差的敏感性、推理效率、训练数据需求、极端视角下的性能边界等细节均未提及。

### 阅读优先级
**高**。理由：该方法针对单图像 3DGS 中关键的表示对齐问题提出了新思路，并在跨数据集评测和零样本泛化上表现突出；且论文来自多个知名机构，发表于较新的时间点，对神经场景表示与渲染方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-image feed-forward 3D Gaussian Splatting (3DGS) aims to directly generate a renderable 3D scene representation from one input image, avoiding the cost of multi-view capture and per-scene optimization. However, existing methods are often constrained by a pixel-aligned representation, where Gaussians are predicted from fixed image-grid locations. Such pixel-aligned primitives can produce promising nearby-view renderings, but they remain weakly coupled to underlying scene surfaces and struggle to preserve coherent structures under large viewpoint shifts. We present InfiniSplat, a feed-forward single-image 3DGS framework that moves from a pixel-aligned representation toward a surface-aligned representation. InfiniSplat constructs this representation by first using geometry-guided sampling to place 2D supports according to depth-induced local surface structure, and then applying a query-conditioned implicit decoder to predict Gaussian attributes from the image features queried at these supports.By grounding support locations in geometry while decoupling Gaussian prediction from fixed pixel centers, InfiniSplat produces Gaussian layouts that better follow scene surfaces and reduce scattered primitives caused by grid discretization.Across multiple cross-dataset NVS evaluations, InfiniSplat achieves state-of-the-art performance compared with single-image feed-forward baselines, and demonstrates zero-shot generalization from Hypersim indoor synthetic training to complex open-world scenes.Project page: https://zju3dv.github.io/InfiniSplat.

</details>

#### 2026-08-03 - CLEAR: Conflict-aware Learning via Evidence-guided Adaptive Routing for Unified Sparse-View 3D Gaussian Super-Resolution

**Authors:** Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan
**Links:** [abs](https://arxiv.org/abs/2608.02206) - [pdf](https://arxiv.org/pdf/2608.02206)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CLEAR: Conflict-aware Learning via Evidence-guided Adaptive Routing for Unified Sparse-View 3D Gaussian Super-Resolution
- 作者：Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan
- 出版日期：2026-08-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02206

### 一句话总结
CLEAR 提出首个统一单阶段稀疏视角 3D 高斯超分框架，通过冲突感知优化与证据引导路由机制，在单一高斯表示中联合优化低分辨率观测与高分辨率先验，显著提升渲染质量和几何保真度。

### 研究问题
稀疏视角 3D 高斯泼溅超分面临的核心挑战：稀疏且低分辨率的输入缺乏足够的几何与高频信息，现有两阶段管线（先低分辨率重建、再高分辨率细化）会引入阶段间高斯迁移与重建误差累积。论文旨在解决如何在一个统一框架中避免误差累积并同时恢复高频细节。

### 核心思路/方法
- 提出统一单阶段框架 CLEAR，在单个高斯表示中联合优化真实低分辨率观测与外部高分辨率先验。
- **高斯级冲突感知优化策略**：将低分辨率梯度视为可靠锚点，仅对严重高分辨率冲突施加基于证据条件的软校正，以缓解稀疏监督带来的梯度冲突。
- **证据引导的 Patch-to-Gaussian 路由机制**：估计 patch 可靠性与细节需求，将其提升至高斯空间，并选择性路由高频梯度与致密化操作。
- 采用共享高斯丢弃（shared Gaussian dropout）与分离的中途训练锚定（detached mid-training anchoring）增强训练鲁棒性。

### 主要贡献
- 首次提出稀疏视角 3D 高斯泼溅超分的统一单阶段框架，避免两阶段误差累积。
- 提出高斯级冲突感知优化策略，以低分辨率梯度为锚进行条件性软校正。
- 设计证据引导的 Patch-to-Gaussian 路由机制，针对性恢复高频细节。
- 在合成与真实世界 4× 超分基准上达到最先进渲染质量与几何保真度。

### 局限性
摘要未提供足够信息。具体局限性（如计算开销、对不同稀疏程度输入的敏感性、失败案例等）在摘要中未提及。

### 阅读优先级
**高**
理由：该工作面向稀疏视角 3D 超分这一活跃方向，提出单阶段统一框架替代传统两阶段管线，思路具有创新性；同时涉及冲突感知优化与证据引导路由等机制，对神经渲染与 3D 重建研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Sparse-view 3D Gaussian Splatting Super-resolution is highly challenging since the sparse and low-resolution (LR) inputs lack sufficient geometric and high-frequency information for accurate reconstruction. To achieve high-quality reconstruction, existing sparse-view super-resolution methods adhere to two-stage pipeline that performs LR Gaussian reconstruction and then high-resolution (HR) Gaussian refinement, which directly results in stage-wise Gaussian transfer and reconstruction error accumulation. To this end, we propose CLEAR, a Conflict-aware Learning via Evidence-guided Adaptive Routing, as the first unified single-stage framework for Sparse-view 3D Gaussian Splatting Super-resolution. Specifically, CLEAR performs joint the optimization of authentic LR observations and external HR priors within a unified Gaussian representation. To mitigate the gradient conflicts introduced by sparse supervision during training, we propose a Gaussian-wise conflict-aware optimization strategy that regards the LR gradient as a reliable anchor and applies evidence-conditioned soft correction only to severe HR conflicts. Moreover, to recover high-frequency details, we introduce an evidence-guided Patch-to-Gaussian routing mechanism which estimates patch reliability and detail demand, lifts them into Gaussian space, and selectively routes high-frequency gradients and densification. Finally, we employ shared Gaussian dropout and a detached mid-training anchoring to enhance the robustness of training framework. Extensive experiments on both synthetic and real-world $4\times$ super-resolution benchmarks demonstrate that CLEAR consistently achieves state-of-the-art rendering quality and superior geometric fidelity.

</details>

#### 2026-08-03 - DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views

**Authors:** Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen
**Links:** [abs](https://arxiv.org/abs/2608.02191) - [pdf](https://arxiv.org/pdf/2608.02191)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting, embodied AI, autonomous driving, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views
- 作者：Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen
- 出版日期：2026-08-03
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.02191

### 一句话总结
DerainSplat 提出了一种前馈式 3D 高斯泼溅框架，能够仅从少量雨景视角直接重建干净的 3D 场景，并通过预测天气因子实现去雨与几何增强。

### 研究问题
如何从稀疏的雨景多视图输入中，以前馈方式重建干净的 3D 场景，以解决现有前馈 3DGS 方法在雨景条件下性能崩溃的问题。

### 核心思路/方法
- 构建大规模多视角去雨数据集：通过四阶段合成流程依次建模阴天光照、深度相关雾霾、雨条纹和镜头雨滴，生成带特权天气因子的数据。
- 引入天气网络：从雨景上下文中预测天气因子，并生成两种支持图（场景支持与辐射支持）。
- 场景支持：用于调制跨视图代价体匹配，增强几何估计。
- 辐射支持：用于驱动深度对齐的外观融合，填补被雨损坏的像素。
- 几何证据调节：利用推导出的几何证据衰减高斯不透明度，减少虚假结构。
- 雨景循环一致性：使用预测的天气因子重渲染干净视图，并与雨景输入对齐，形成自监督约束。

### 主要贡献
- 提出首个面向稀疏雨景输入的前馈式干净 3D 场景重建框架 DerainSplat。
- 构建了大规模多视角去雨数据集，包含分层天气建模的合成管线。
- 设计天气网络与双支持图机制，分别作用于几何匹配和外观融合。
- 引入雨景循环一致性损失，增强去雨重建的一致性。
- 在多个数据集（RealEstate10K、ACID、Mip-NeRF360）及真实雨景场景上验证了优于现有方法的表现，并具备跨数据集泛化能力。

### 局限性
摘要未提供足够信息。未提及具体失败场景、对极端雨况的鲁棒性边界、计算开销、实时性要求或对非雨景输入的退化表现等。

### 阅读优先级
**高**。理由：该工作针对空间智能应用（如具身 AI 和自动驾驶）中稀疏雨景 3D 重建这一关键痛点，提出了完整的前馈框架、数据集与自监督机制，兼具方法创新与实际应用价值，且跨数据集验证了泛化性，值得重点阅读。

</details>

<details>
<summary>Abstract</summary>

Although image deraining has advanced substantially, existing methods mainly focus on 2D image restoration. As spatial intelligence applications such as embodied AI and autonomous driving continue to emerge, reconstructing clean 3D scenes from sparse rainy views in a feed-forward manner becomes increasingly important. Existing feed-forward 3D Gaussian Splatting (3DGS) methods often assume clean inputs and collapse under rainy conditions. To this end, we present \textbf{\textit{DerainSplat}}, a feed-forward framework that reconstructs clean 3D scenes from only a few rainy views. To support this task, we build a large-scale multi-view derain dataset through a four-stage synthesis pipeline that sequentially models overcast illumination, depth-dependent haze, rain streaks, and lens raindrops, producing privileged weather factors. We introduce a weather net that predicts the weather factors from rainy context and yields two support maps. Scene support modulates cross-view cost-volume matching, while radiance support drives depth-aligned appearance fusion to fill corrupted pixels. The derived geometry evidence further attenuates Gaussian opacity to reduce spurious structures. A rainy cycle consistency re-renders clean views using the predicted factors and aligns them with rainy inputs. Extensive experiments show that \textbf{\textit{DerainSplat}} outperforms existing methods on various datasets, including RealEstate10K, ACID, Mip-NeRF360, and real-world rainy scenes, with strong cross-dataset generalization.

</details>

#### 2026-08-03 - GSRAIN: Physically Calibrated High-/Low-Frequency Rainfall Synthesis for 3D Gaussian Driving Scenes

**Authors:** Fanyu Wang, Longgao Zhang, Junyi Chen
**Links:** [abs](https://arxiv.org/abs/2608.02177) - [pdf](https://arxiv.org/pdf/2608.02177)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GSRAIN: Physically Calibrated High-/Low-Frequency Rainfall Synthesis for 3D Gaussian Driving Scenes
- 作者：Fanyu Wang, Longgao Zhang, Junyi Chen
- 出版日期：2026-08-03T12:57:44Z
- 分类：Neural Scene Representations & Rendering（次要：Embodied / Robotics / AR Applications）
- 链接：https://arxiv.org/abs/2608.02177

### 一句话总结
GSRAIN 提出一种基于 3D 高斯泼溅（3DGS）的高/低频降雨合成方法，通过融合物理校准的雨滴模型与扩散模型生成的雨景外观，实现对自动驾驶场景降雨强度的可控渲染。

### 研究问题
现有面向自动驾驶的降雨仿真方法在物理可控性和多视角一致性方面存在局限，缺乏能够支持可控降雨强度且与闭环测试兼容的场景生成手段。

### 核心思路/方法
- 构建高频雨滴模型：基于实测降雨数据生成高频雨滴效果。
- 生成低频降雨外观：使用几何感知的单步扩散模型生成低频雨景外观。
- 统一融合：将高、低频两种效果融合到统一的 3DGS 场景中，实现 0–13 mm/h 范围的降雨强度控制。

### 主要贡献
- 提出 GSRAIN 方法，实现物理校准的高/低频降雨合成，兼顾可控性与多视角一致性。
- 在 3DGS 驾驶场景中支持降雨强度的连续控制（0–13 mm/h）。
- 定量评估：FID 达到 149.09，优于 CycleGAN-Turbo（155.71）和 WeatherEdit（157.94）。
- 目标检测与闭环驾驶实验表明，生成的场景能暴露算法在可控降雨下的场景相关性能变化，证明其可用于构建物理可控、可重复且闭环兼容的雨景测试场景。

### 局限性
摘要未提供足够信息，未提及方法在极端降雨强度、真实感上限、计算开销、泛化到其他天气类型或场景外推等方面的局限性。

### 阅读优先级
**高**
理由：该工作针对自动驾驶仿真中的物理可控降雨生成问题，提出基于 3DGS 的新方法，在定量指标上优于现有方法，并验证了其在闭环测试中的实用性。对于从事神经场景渲染、自动驾驶仿真或鲁棒性测试的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing rainfall simulation methods for autonomous driving remain limited in physical controllability and multi-view consistency. This paper presents GSRAIN, a high-/low-frequency rainfall synthesis method for 3D Gaussian Splatting (3DGS) driving scenes. GSRAIN constructs a high-frequency raindrop model from measured rainfall data and generates low-frequency rainy appearance using a geometry-aware single-step diffusion model. The two effects are then fused in a unified 3DGS scene, enabling rainfall-intensity control over the range of 0--13~mm/h. The proposed method achieves a Fréchet Inception Distance (FID) of 149.09, outperforming CycleGAN-Turbo (155.71) and WeatherEdit (157.94). Object-detection and closed-loop driving experiments further show that the generated scenes expose scene-dependent performance changes of the evaluated algorithms under controllable rainfall. These results indicate that GSRAIN provides an effective approach for constructing physically controllable, repeatable, and closed-loop-compatible rainy-weather test scenes for autonomous driving.

</details>

#### 2026-08-03 - DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization

**Authors:** Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng
**Links:** [abs](https://arxiv.org/abs/2608.02099) - [pdf](https://arxiv.org/pdf/2608.02099)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization
- 作者：Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng
- 出版日期：2026-08-03T11:59:51Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02099

### 一句话总结
DeGS提出一种解耦工作负载解析与重组的可扩展3DGS硬件架构，通过将传统渲染中耦合的检查与混合流程分离，显著提升并行处理单元利用率与吞吐量。

### 研究问题
现有3DGS加速器存在架构可扩展性差的问题：增加处理单元（PE）数量时渲染性能提升有限。根因是“边检查边混合”（checking-while-blending）的紧耦合数据流，导致不规则的Gaussian覆盖（空间冗余）和异步像素终止（时间冗余）下PE利用率低下。

### 核心思路/方法
- 将标准渲染过程中耦合的α检查、透射率检查和α混合操作解耦，重构为三个连续阶段：工作负载解析（parsing）、重组（reorganization）和混合（blending）。
- 在混合之前将碎片化、长度可变且依赖时序的工作负载重组为紧凑、无冲突且密集的工作负载，从而提高并行混合阶段的PE利用率。
- 在28nm工艺下实现，并与现有最先进加速器（GSCore、GBU、GCC）对比。

### 主要贡献
- 提出解耦数据流设计，系统性消除渲染固有的空间和时间冗余。
- 实现高可扩展性：从16扩展到1024个PE时，在高分辨率下维持超过80%的PE利用率。
- 在多样场景和分辨率（720p至8K）下，相比现有加速器获得2.36倍–7.25倍吞吐量、1.82倍–6.02倍端到端加速，以及1.59倍–4.42倍能效提升。

### 局限性
摘要未提供足够信息，例如具体功耗/面积开销、对不同场景类型的泛化失败案例、与传统GPU的对比结果等。

### 阅读优先级
**高**。理由：该工作直接针对3DGS硬件加速的核心可扩展性瓶颈，提出结构化的解耦方案，具有明确的性能与能效数据支撑，且覆盖从720p到8K的多种分辨率，对实时渲染和神经渲染硬件设计领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as a leading technique for real-time novel view synthesis, yet existing 3DGS accelerators suffer from poor architectural scalability: increasing the number of PEs leads to marginal performance improvement during rendering. We identify that the root cause is the tightly coupled ``checking-while-blending'' dataflow, which exacerbates PE underutilization caused by spatial redundancy from irregular Gaussian coverage and temporal redundancy from asynchronous pixel-wise termination under parallel execution. To address this issue, we propose DeGS, a scalable architecture for efficient 3DGS inference. To systematically eliminate the redundancies inherent in rendering, DeGS exploits a decoupled dataflow, restructuring the coupled $α$-checking, transmittance checking, and $α$-blending of the standard rendering process into consecutive workload parsing, reorganization, and blending stages. This allows the fragmented, length-variable, and temporal-dependent workloads to be reorganized into compact, conflict-free, and dense workloads prior to blending, thereby significantly improving PE utilization during parallel blending. Implemented in 28 nm technology, DeGS achieves 2.36$\times$--7.25$\times$ throughput, 1.82$\times$--6.02$\times$ end-to-end speedup, and 1.59$\times$--4.42$\times$ energy efficiency over state-of-the-art 3DGS accelerators (GSCore, GBU, GCC) across diverse scenes and resolutions (720p to 8K). Moreover, scaling from 16 to 1024 PEs, DeGS maintains over 80\% PE utilization at high resolutions, significantly outperforming existing accelerators.

</details>

#### 2026-08-03 - LiveLight: Real-time Streaming Video Relighting with Interactive Control

**Authors:** Yue Ma, Jiangming Wang, Yucheng Wang, Xilai Wang, Zhiyuan Li, Xinyu Wang, Hongyu Liu, Ruofan Liang, Songchun Zhang, Yuxuan Xue, Qifeng Chen
**Links:** [abs](https://arxiv.org/abs/2608.01771) - [pdf](https://arxiv.org/pdf/2608.01771)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic 3D, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LiveLight: Real-time Streaming Video Relighting with Interactive Control
- 作者：Yue Ma, Jiangming Wang, Yucheng Wang, Xilai Wang, Zhiyuan Li, Xinyu Wang, Hongyu Liu, Ruofan Liang, Songchun Zhang, Yuxuan Xue, Qifeng Chen
- 出版日期：2026-08-03T06:45:00Z
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：https://arxiv.org/abs/2608.01771

### 一句话总结
LiveLight 是首个基于扩散模型的实时流式视频重照明框架，支持交互式 3D 光照控制，在极低推理步数下实现高质量、时间稳定的重照明效果。

### 研究问题
如何构建一个既能实时处理流式视频、又支持交互式 3D 光照控制，同时保持高保真重照明质量的扩散模型框架？具体需要解决三个关键挑战：有效注入动态 3D 光照信息、在极低 NFE（函数评估次数）预算下维持生成质量以达成实时速度、以及支持任意长度视频的连续流式交互控制。

### 核心思路/方法
论文提出三项核心设计：
1. **光照注入**：设计一个轻量级适配器，将多平面光辐照度（MPLI）条件——即编码 3D 光照几何的深度感知辐照度图——直接送入扩散主干网络。
2. **低 NFE 质量保持**：引入几何引导反馈分支，在训练时使用冻结的几何估计器强制深度与法线一致的重照明，确保几何合理的着色效果，且不增加推理开销。
3. **流式交互**：开发渐进式滚动窗口策略，维护不同噪声水平的潜变量块去噪阶梯，通过传播中间状态保证时间一致性，支持任意长度视频重照明及逐帧参考刷新。

### 主要贡献
- 首次提出面向实时流式视频重照明的扩散框架，支持交互式 3D 光照控制。
- 提出轻量适配器实现 MPLI 条件的高效光照注入。
- 提出几何引导反馈分支，在极低 NFE 下保持几何一致的渲染质量。
- 设计渐进式滚动窗口策略，实现时间一致的无限长度流式重照明。
- 在真实与合成基准上达到最先进的重照明质量，同时实现实时速度；在时间稳定性、光照可控性和用户偏好上显著优于离线基线。
- 将公开模型、训练数据及合成数据生成器以促进相关研究。

### 局限性
摘要未提供足够信息，未讨论方法的失败案例、计算资源需求、对输入视频质量的依赖、光照控制的范围限制，或与其他方法的定量对比细节等潜在局限性。

### 阅读优先级
**高**。理由：该工作针对视频重照明这一活跃研究方向，首次将扩散模型、实时速度与交互式 3D 光照控制结合起来，具有较强的创新性和实用价值；同时作者计划开源模型与数据，便于复现和后续研究，值得高优先级关注。

</details>

<details>
<summary>Abstract</summary>

We present LiveLight, the first diffusion-based framework for real-time streaming video relighting with interactive 3D lighting control. Achieving this is non-trivial, as it requires overcoming three critical challenges: effectively injecting dynamic 3D lighting into a diffusion model, maintaining high-fidelity generation under an extremely low NFE (Number of Function Evaluations) budget for real-time speed, and facilitating continuous streaming for interactive control. To address these pain points, we propose three key designs. First, for accurate lighting injection, we propose a lightweight adapter that feeds Multi-Plane Light Irradiance (MPLI) conditions-depth-aware irradiance maps encoding 3D lighting geometry-directly into the diffusion backbone. Second, to prevent rendering quality degradation at low NFEs towards real-time distillation, we introduce a geometry-guided feedback branch. This training-time constraint leverages a frozen geometry estimator to enforce depth- and normal-consistent relighting, ensuring geometrically plausible shading without adding inference overhead. Finally, to enable streaming interaction, we develop a progressive rolling-window strategy that maintains a denoising ladder of latent chunks at varying noise levels. By propagating intermediate states, this strategy guarantees temporal coherence and supports arbitrarily long video relighting with per-frame reference refresh. Extensive experiments on real-world and synthetic benchmarks demonstrate that LiveLight achieves state-of-the-art relighting quality while running at real-time speed, significantly outperforming offline baselines in temporal stability, lighting controllability, and user preference. To foster real-time interactive relighting research, we will publicly release our models, training data, and synthetic data generator.

</details>

#### 2026-08-03 - DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing

**Authors:** Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi
**Links:** [abs](https://arxiv.org/abs/2608.01761) - [pdf](https://arxiv.org/pdf/2608.01761)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, relighting, rendering, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing
- 作者：Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi
- 出版日期：2026-08-03
- 分类：神经场景表示与渲染（主）；具身/机器人/AR应用（次）
- 链接：https://arxiv.org/abs/2608.01761

### 一句话总结
本文提出一种解耦式3D高斯泼溅（3DGS）框架，将大场景拆分为静态背景与可操控动态智能体，以支持端到端自动驾驶算法的高保真、可交互、实时的闭环测试。

### 研究问题
现有端到端自动驾驶测试环境（游戏引擎或静态神经渲染方法）难以同时兼顾高视觉保真度、强交互性与实时性能，尤其在动态场景组合方面存在不足，无法满足大规模闭环评估需求。

### 核心思路/方法
采用基于对象中心的规范表示（object-centric canonical representation），从根本上将场景分解为：
- 高保真静态背景；
- 可操控的动态智能体。

为解决分解带来的表征冲突，引入三个针对性模块：
1. **资产压缩**：通过感知剪枝和向量量化（vector quantization）实现实时交通渲染；
2. **地图引导的几何配准**：利用语义拓扑严格对齐轨迹；
3. **代理式重光照**：迁移环境光照以实现无缝的光度合成。

### 主要贡献
- 提出面向大规模端到端自动驾驶评估的解耦式3DGS框架；
- 设计三个模块解决静态背景与动态智能体分解后的表征冲突；
- 实验表明该方法在保真度与效率之间取得平衡，提升了指标一致性和光度一致性；
- 构建了实用的闭环传感器仿真平台，用于端到端自动驾驶评估。

### 局限性
摘要未提供足够信息。摘要未提及对极端天气、遮挡处理、大规模场景内存占用、计算资源需求等具体局限性，也未提供详细实验对比数据。

### 阅读优先级
**中**

理由：该工作面向自动驾驶闭环测试这一特定应用场景，技术上结合了3DGS、神经渲染与仿真，对相关领域研究者有一定参考价值。但摘要未提供足够定量实验细节，难以判断其相对既有方法的实际优势幅度，建议根据是否需要3DGS仿真框架来决定是否精读原文。

</details>

<details>
<summary>Abstract</summary>

End-to-end (E2E) autonomous driving algorithms require rigorous closed-loop validation in simulation environments offering high visual fidelity, strong interactivity, and real-time performance. Existing approaches, from game engines to static neural rendering, inherently trade off these requirements and struggle with the dynamic scene composition essential for E2E testing. To bridge this gap, we propose a novel decoupled 3D Gaussian Splatting (3DGS) framework tailored for large-scale E2E evaluation. We fundamentally decompose scenes into a high-fidelity static background and manipulable dynamic agents using an object-centric canonical representation. To resolve resulting representational conflicts, we introduce three targeted modules: (1) asset compression via perceptual pruning and vector quantization for real-time traffic rendering; (2) map-guided geometric registration leveraging semantic topology to strictly align trajectories; and (3) proxy-based relighting transferring ambient illumination for seamless photometric integration. Extensive experiments demonstrate that DecoupleGS achieves a balanced fidelity-efficiency trade-off, improves metric and photometric consistency, and provides a practical closed-loop sensor simulation platform for E2E autonomous driving evaluation.

</details>

#### 2026-08-03 - G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors

**Authors:** Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou
**Links:** [abs](https://arxiv.org/abs/2608.01726) - [pdf](https://arxiv.org/pdf/2608.01726)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors
- 作者：Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou
- 出版日期：2026-08-03（注：该日期异常，建议核实）
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01726

### 一句话总结
G-Skin 提出一种生成式蒙皮框架，利用2D视觉基础模型蒸馏运动先验作为伪引导，为3D高斯表示学习拓扑无关的蒙皮权重，实现高保真动画化。

### 研究问题
如何在没有高质量3D高斯蒙皮数据集的情况下，为任意骨架拓扑的3D高斯资产实现灵活且高保真的蒙皮绑定，同时克服前馈方法缺乏训练数据、以及基于网格迁移方法泛化性差的问题。

### 核心思路/方法
1. 利用骨架可控的图像生成模型，借助2D视觉基础模型，将强大的运动先验蒸馏为伪引导（pseudo-guidance），以缓解3D数据稀缺问题。
2. 在该伪引导下，设计包含几何感知正则化的优化管线，以稳定学习过程并确保蒙皮权重平滑且结构连贯。
3. 框架可灵活扩展到3D高斯表示的增强变体，用于缓解动画引起的渲染伪影。

### 主要贡献
- 提出G-Skin，一种面向3D高斯表示的新型生成式蒙皮框架，支持表达丰富、高保真的动画。
- 引入基于2D视觉基础模型的骨架可控图像生成方案，为解决3D蒙皮数据稀缺提供了新途径。
- 设计了结合几何感知正则化的优化流程，保证蒙皮权重的平滑性和结构一致性。
- 通过大量实验验证了方法有效性，并表明相对于现有最先进方法具有明显优势。

### 局限性
摘要未提供足够信息，无法得知该方法在极端拓扑、实时性能、多物体交互、以及蒙皮权重质量量化指标等方面的具体限制。

### 阅读优先级
**高**。理由：3D高斯泼溅是当前神经渲染与动态场景建模的热点方向，而蒙皮绑定是其动画化的关键瓶颈；该工作提出了一种绕开昂贵3D数据采集的生成式方案，思路新颖且声称超越现有方法，对从事3D内容生成与动画渲染的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has achieved remarkable success in photorealistic and efficient rendering, leading to a rapid increase in 3D assets represented by 3D Gaussian primitives. Directly rigging these assets with arbitrary skeleton topologies is highly desirable. However, training a feed-forward skinning framework is infeasible due to the lack of high-quality 3D Gaussian rigging datasets. An alternative solution is to transfer mesh-based techniques to 3D Gaussian-based representation, but 3D Gaussian primitives are not restricted to the surface and lack explicit topological connectivity. Moreover, this kind of method suffers from poor generalization to unseen data due to its strong dependence on training data, while acquiring high-quality rigging data is prohibitively expensive. To address this challenging problem, we propose G-Skin, a novel generative skinning framework designed for expressive and high-fidelity animation with 3D Gaussian representation. To overcome this 3D data scarcity, we introduce a skeleton-controllable image generation model leveraging 2D vision foundation models to distill powerful motion priors into pseudo-guidance. Guided by these priors, we formulate an optimization pipeline incorporating geometry-aware regularizations, which stabilizes the learning process and ensures smooth, structurally coherent skinning weights. G-Skin also generalizes flexibly to the augmented variants of 3D Gaussian representation designed to mitigate animation-induced rendering artifacts. Extensive experiments validate the effectiveness of our approach, demonstrating clear advantages over state-of-the-art methods. Project page: https://yaoyx689.github.io/GSkin.html.

</details>

#### 2026-08-03 - StreamSplat: Streaming Feed-Forward 3D Gaussian Splatting

**Authors:** Changhao Song, Yuxuan Wang, Qibiao Li, Youcheng Cai, Ligang Liu
**Links:** [abs](https://arxiv.org/abs/2608.01659) - [pdf](https://arxiv.org/pdf/2608.01659)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StreamSplat: Streaming Feed-Forward 3D Gaussian Splatting
- 作者：Changhao Song, Yuxuan Wang, Qibiao Li, Youcheng Cai, Ligang Liu
- 出版日期：2026-08-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01659

### 一句话总结
StreamSplat 提出了一种流式前馈 3D 高斯泼溅框架，通过体素对齐的因果缓存和几何锚定机制，实现在线顺序输入场景下的增量式新视角合成，并支持超长输入流。

### 研究问题
现有前馈 3D 高斯泼溅方法通常假设一组固定的上下文视图并联合处理，无法适应校准视图按顺序到达、场景需因果更新的在线场景；且固定视图方法在长输入流中会内存溢出。本文旨在解决流式环境下高效、稳定地进行新视角合成的问题。

### 核心思路/方法
- 提出 StreamSplat，一个流式前馈 3DGS 框架，增量维护一个持续的、基于几何的场景状态，并在每个输入块后解码为可渲染的 3D 高斯。
- 核心组件为 **Voxel-Aligned Causal Cache (VACC)**：在内存有界的体素结构中存储历史 3D token，使内存随探索的场景几何增长而非流长度增长。
- 引入 **History-Projected Depth Anchoring (HPDA)**：将缓存几何投影为当前代价体估计的深度引导。
- 引入 **Cache-Guided Feature Injection (CGFI)**：将缓存中的潜在证据注入高斯 token 回归过程。

### 主要贡献
- 提出首个面向流式输入的前馈 3DGS 框架，支持因果更新而不依赖未来视图或全场景上下文。
- 设计 VACC 缓存机制，使内存消耗与场景几何规模相关而非输入流长度。
- 通过 HPDA 和 CGFI 有效复用历史信息，实现在稀疏因果输入下与 SOTA 方法竞争力相当的性能。
- 在 DL3DV、RealEstate10K 和 ScanNet 上验证，能够扩展至 256、512、1024 视图的长流输入，且新视角质量随观测增多持续提升。

### 局限性
摘要未提供足够信息（如具体失败场景、计算开销、对高度动态场景的适用性、实际运行时效率等均未提及）。

### 阅读优先级
**高**
理由：该工作针对在线/流式新视角合成这一实际需求，解决了现有前馈 3DGS 方法无法处理长序列和因果更新的关键瓶颈；提出的缓存机制与几何锚定方法具有较强通用性，且实验覆盖多个数据集和超长输入规模，对从事实时三维重建、机器人感知、流媒体渲染等方向的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting enables efficient novel-view synthesis without per-scene optimization, but most existing methods assume a fixed set of context views and process them jointly. This limits their applicability to online scenarios where calibrated views arrive sequentially and the scene must be updated causally. We present \emph{StreamSplat}, a streaming feed-forward 3DGS framework that incrementally maintains a persistent geometry-grounded scene state and decodes it into renderable 3D Gaussians after each input chunk. StreamSplat centers on a \textbf{Voxel-Aligned Causal Cache (VACC)}, which stores historical 3D tokens in a memory-bounded voxel structure so that memory grows with explored scene geometry rather than stream length. To better reuse history during causal prediction, we introduce \textbf{History-Projected Depth Anchoring (HPDA)} to project cached geometry as depth guidance for current cost-volume estimation, and \textbf{Cache-Guided Feature Injection (CGFI)} to inject cached latent evidence into Gaussian-token regression. Experiments on DL3DV, RealEstate10K, and ScanNet show that StreamSplat remains competitive with state-of-the-art feed-forward 3DGS methods under sparse causal inputs, despite not using future views or full-scene context. More importantly, it scales to long input streams with 256, 512, and 1024 views where fixed-view baselines run out of memory, yielding sustained improvements in novel-view synthesis quality as more observations arrive. The code will be made publicly available upon acceptance.

</details>

#### 2026-08-02 - GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization

**Authors:** Baihan Yang, Tiexin Li, Yuheng Liu, Xin Lin, Xinke Li, Xiaohui Xie, Truong Nguyen
**Links:** [abs](https://arxiv.org/abs/2608.01492) - [pdf](https://arxiv.org/pdf/2608.01492)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization
- 作者：Baihan Yang, Tiexin Li, Yuheng Liu, Xin Lin, Xinke Li, Xiaohui Xie, Truong Nguyen
- 出版日期：2026-08-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01492

### 一句话总结

提出一种无需训练的3D高斯泼溅交互式物体选择框架，利用稀疏视角和稀疏涂鸦，通过图优化实现轻量级的高质量物体分割。

### 研究问题

在3D场景编辑和具身交互中，如何以最小用户交互成本，从重建的3D高斯场景中准确选择完整物体，同时降低对密集视角和大量计算资源的依赖。

### 核心思路/方法

- 直接在原生3D高斯原语上操作，无需重新训练或标注嵌入。
- 将密集高斯体粗化为几何一致的超点，并利用外观和空间信息构建带连续性权重的图。
- 将稀疏用户涂鸦通过可见性感知的透射率覆盖提升至3D空间。
- 将物体选择建模为全局图割能量最小化问题，传播稀疏标注以覆盖完整3D物体。
- 支持多轮交互式细化，用户可从额外视角迭代纠正选择结果。

### 主要贡献

- 提出训练免费的交互式3D物体选择框架，支持稀疏视角输入和稀疏涂鸦引导。
- 引入基于超点和连续性权重图的图割优化方法，有效传播稀疏用户证据。
- 设计了可见性感知的透射率覆盖机制，将2D涂鸦准确提升到3D空间。
- 天然支持多轮细化交互，逐步提升选择质量。
- 实验表明在较少交互视角和大幅降低计算开销的条件下，达到与基于多视角SAM方法相当的选择质量。

### 局限性

摘要未提供足够信息，无法得知在极端稀疏视角下的性能边界、对不同场景类型的适应能力、与SAM方法的具体质量差异数值、以及用户交互轮次对性能的详细影响。摘要也未提及方法在复杂拓扑物体或遮挡严重场景下的表现。

### 阅读优先级

**高**

理由：该方法针对3DGS物体选择中计算开销大、依赖密集视角的实际痛点，提出无需训练的轻量级解决方案，兼具实用性和创新性。而且其交互式多轮细化设计贴合真实部署场景，对3D场景编辑和资产提取方向的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Selecting a complete 3D object from a reconstructed scene with minimal user effort is essential for practical scene editing and embodied interaction. Existing 3DGS-based methods either retrain the Gaussian representation to embed per-object labels, or build dense multi-view SAM observations, both requiring heavy computation and dense viewpoint coverage that is rarely available in practice. We present GaussianSelector, a training-free framework for interactive 3D object selection from sparse views and sparse scribble guidance. Operating directly on native Gaussian primitives, we coarsen dense Gaussians into geometrically coherent superpoints and construct a continuity-weighted graph using appearance and spatial cues. Sparse user scribbles are lifted into 3D via visibility-aware transmittance coverage, and selection is solved as a global graph-cut energy minimization that propagates sparse evidence to a complete 3D object. This design naturally supports multi-round refinement, where users iteratively correct the selection from additional viewpoints to progressively improve the result. Experiments demonstrate that GaussianSelector achieves competitive selection quality against state-of-the-art multi-view SAM-based methods, while requiring significantly fewer interaction views and substantially lower computational overhead. These properties make it well suited for human-in-the-loop 3D scene editing and 3D asset extraction in real-world deployment scenarios.

</details>

#### 2026-08-02 - QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction

**Authors:** Yinglong Li, Donghui Shen, Xiaoyu Zhang, Zhichao Ye, Hongyu Wu, Aimin Hao, Guofeng Zhang, Haomin Liu
**Links:** [abs](https://arxiv.org/abs/2608.01186) - [pdf](https://arxiv.org/pdf/2608.01186)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction
- 作者：Yinglong Li, Donghui Shen, Xiaoyu Zhang, Zhichao Ye, Hongyu Wu, Aimin Hao, Guofeng Zhang, Haomin Liu
- 出版日期：2026-08-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01186

### 一句话总结
QuerySplat 提出一种基于几何先验与显式外观解耦的前馈 3D 高斯泼溅框架，在无需位姿的情况下实现高保真新视角合成，并在 DL3DV 基准上取得最优性能。

### 研究问题
现有多视角前馈 3D 高斯泼溅（3DGS）重建方法在渲染保真度上仍存在不足：像素级对齐方法受限于空间灵活性差且结构冗余多；基于查询的方法缺乏 3D 先验，且将几何与外观耦合，导致结果模糊且依赖视角姿态。

### 核心思路/方法
设计了一个双分支查询式解码器：
- **几何分支**：利用预训练的视觉几何模型提供空间理解，使模型天然具备无位姿建模能力；
- **外观分支**：通过与几何属性回归分离的专用通道，恢复高频细节；
两个分支相互解耦，避免几何-外观信息纠缠，从而缓解早期查询式模型渲染模糊的问题。

### 主要贡献
1. 提出 QuerySplat，一种由几何先验驱动且显式解耦外观的前馈 3DGS 框架；
2. 设计双分支查询式解码器，实现几何与外观表示的解耦；
3. 在 DL3DV 基准上取得新视角合成的最优性能，相比最佳无位姿基线平均 PSNR 提升 2.30 dB，相比最佳需位姿基线提升 1.04 dB。

### 局限性
摘要未提供足够信息，例如模型的计算开销、对遮挡或复杂场景的鲁棒性、以及与其他方法在更多基准上的对比等均未提及。

### 阅读优先级
**高**。理由：该方法在无需位姿条件下大幅提升渲染保真度（PSNR 提升 2.30 dB），且同时优于需位姿方法，对前馈 3D 重建领域具有明确改进价值；双分支解耦设计思路简洁且具启发性，值得关注。

</details>

<details>
<summary>Abstract</summary>

While feed-forward 3D Gaussian Splatting (3DGS) enables efficient 3D reconstruction, achieving high-fidelity rendering remains challenging. Existing pixel-aligned approaches suffer from spatial inflexibility and massive structural redundancy, whereas query-based methods lack 3D priors and entangle geometry with appearance, yielding blurry, pose-dependent results. To overcome these deficiencies, we propose \textbf{QuerySplat}, a feed-forward 3DGS framework driven by geometric priors and explicit appearance decoupling. Specifically, we design a dual-branch query-based decoder: the geometry branch leverages a pretrained Vision Geometric Model for spatial understanding, which intrinsically endows QuerySplat with pose-free modeling capabilities, while the appearance branch recovers high-frequency details through a dedicated pathway separated from geometric attribute regression. Extensive experiments demonstrate that QuerySplat mitigates the blurry rendering issues of early query-based models and consistently outperforms pixel-aligned approaches in rendering fidelity. On the challenging DL3DV benchmark, it achieves state-of-the-art novel view synthesis performance, with average PSNR gains of 2.30 dB and 1.04 dB over the best pose-free and pose-required baselines, respectively. Project Page: https://inspatio.github.io/querysplat.

</details>

#### 2026-08-02 - Struct-GStream: Towards Efficient Free-Viewpoint Video Streaming at Low-Bitrates with Structured 3D Gaussians

**Authors:** Han Jiao, Jiakai Sun, Lei Zhao, Wei Xing, Huaizhong Lin, Zhanjie Zhang, Ao Ma
**Links:** [abs](https://arxiv.org/abs/2608.01053) - [pdf](https://arxiv.org/pdf/2608.01053)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3DGS, neural rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Struct-GStream: Towards Efficient Free-Viewpoint Video Streaming at Low-Bitrates with Structured 3D Gaussians
- 作者：Han Jiao, Jiakai Sun, Lei Zhao, Wei Xing, Huaizhong Lin, Zhanjie Zhang, Ao Ma
- 出版日期：2026-08-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01053

### 一句话总结
本文提出Struct-GStream，一种基于结构化3D高斯的方法，用于在低比特率下高效流式传输自由视角视频，兼顾快速训练、低存储与高渲染质量。

### 研究问题
如何在不牺牲渲染质量的前提下，解决现有在线训练的神经网络渲染方法在自由视角视频（FVV）构建中存储开销大、训练时间长的问题，从而实现低比特率下的高效流式传输。

### 核心思路/方法
- 引入动态锚点（dynamic anchor points）生成结构化3D高斯（structured 3DGs），用于构建基础场景。
- 基于物体运动的局部刚性假设，建模场景的近似运动。
- 提出全局自由3D高斯修补策略，包含自由3D高斯的生成、剪枝与优化，用于修补缺失区域及建模新出现的物体。

### 主要贡献
- 提出Struct-GStream框架，首次将结构化3D高斯应用于低比特率下的高效FVV流式传输。
- 在低比特率下实现快速训练，同时保持高质量渲染。
- 实验表明，在训练时间、存储和渲染质量上显著优于现有在线训练FVV方法，并保持有竞争力的渲染速度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法针对FVV流式传输的实际应用瓶颈（训练速度与存储）提出新框架，实验结果指标明确优于现有方法，但论文发表于2026年且摘要未提供具体数据或方法细节，若读者关注3D高斯实时渲染或视频流方向值得阅读；若对创新性要求极高，建议先查看完整实验部分以评估实际增益。

</details>

<details>
<summary>Abstract</summary>

Constructing photorealistic Free-Viewpoint Videos (FVVs) of dynamic scenes from a set of posed 2D images has been an intriguing yet challenging task in computer vision. Methods based on neural rendering achieve high-fidelity image quality in FVV construction. However, most of these methods are unable to achieve real-time rendering and often require complete video sequences to train. Despite the existence of some online training methods capable of rendering FVVs in real time, they struggle to meet the requirements for storage and training time for downstream applications. To overcome this problem, we propose Struct-GStream, which can achieve efficient FVV streaming using structured 3D Gaussians (3DGs). Specifically, we introduce dynamic anchor points to generate structured 3DGs to construct basic scenes and model approximate scene movements based on the assumption of local rigidity in object motion. Besides, we introduce a global free 3DGs patching strategy involving free 3DGs' generation, pruning, and optimization to patch and model deficient areas and emerging objects. Our method achieves fast training at low bitrates while maintaining high rendering quality. Extensive experiments demonstrate that Struct-GStream significantly outperforms existing online training methods for FVV construction in terms of training time, storage, and rendering quality while maintaining competitive rendering speed.

</details>

### 2026-07

#### 2026-07-30 - TSOG: A Format For Temporally And Spatially Ordered Gaussians

**Authors:** Shady Gmira, Evangelos Alexiou, Emmanouil Potetsianakis, Emmanuel Thomas
**Links:** [abs](https://arxiv.org/abs/2607.28049) - [pdf](https://arxiv.org/pdf/2607.28049)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TSOG: A Format For Temporally And Spatially Ordered Gaussians
- 作者：Shady Gmira, Evangelos Alexiou, Emmanouil Potetsianakis, Emmanuel Thomas
- 出版日期：2026-07-30T11:28:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.28049

### 一句话总结
提出了一种名为TSOG的4D高斯泼溅高效表示格式，通过时间域扩展的空间有序高斯框架，实现超过90%的文件体积缩减且质量损失极小。

### 研究问题
如何高效表示、存储和传输动态场景的4D高斯泼溅（4DGS）内容，以解决现有4DGS表示中文件体积过大的问题。

### 核心思路/方法
- 在空间有序高斯（SOG）框架基础上引入**时间线属性**，并对几何与外观属性进行**时间参数化**，从而将SOG扩展到时间域。
- 与SOG一致，TSOG是一种有损格式，为每个高斯分配唯一索引，并将属性值编码为与索引对齐的图像数据。
- 该格式是**模型无关**、**可扩展**的，兼容离散和连续两种4DGS表示。
- 评估采用PLYs序列作为基础基线、FreeTimeGS作为最先进的4DGS表示基线进行对比。

### 主要贡献
- 提出TSOG格式，首次将空间有序高斯框架系统性地扩展到时间域。
- 实现文件体积缩减超过90%，同时PSNR差异仅为-0.42至+0.85 dB，显示以极小质量代价换取显著存储节省。
- 格式设计具备模型无关性和扩展性，适用于不同4DGS表示类型，为下一代4D内容的表示、存储和传输提供了可行方案。

### 局限性
摘要未提供足够信息——关于计算开销、编码解码效率、对极端动态场景的鲁棒性、以及其他质量指标（如SSIM或LPIPS）方面的表现，摘要未提及。

### 阅读优先级
**高**
理由：该工作针对4DGS文件体积极大的痛点，提出了通用且兼容性强的压缩表示格式，节省超过90%的存储空间且质量损失小，对动态场景内容的高效存储和传输具有直接且重要的应用价值，适合关注神经渲染、3D/4D内容压缩的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

We propose Temporally and Spatially Ordered Gaussians (TSOG), a format for efficient representation of 4D Gaussian Splatting (4DGS) content. TSOG extends the Spatially Ordered Gaussians (SOG) framework to the temporal domain by introducing a timeline attribute and temporal parameterization of geometry and appearance attributes. Similar to SOG, TSOG is a lossy format that assigns each Gaussian a unique index and encodes attribute values as index-aligned image data. TSOG is model-agnostic, extensible, and compatible with both discrete and continuous 4DGS representations. Evaluation using a PLYs sequence and FreeTimeGS as baselines, serving as simplistic and state-of-the-art 4DGS representations respectively, shows file size reductions exceeding 90%, with PSNR differences ranging between -0.42 and +0.85 dB. These results demonstrate substantial file size savings with minimal quality degradation, enabling efficient representation, storage, and delivery of dynamic scenes for next-generation 4D content.

</details>

#### 2026-07-30 - Split and Drive: Dual-Axis Disentanglement for Real-Time Gaussian Head Avatars

**Authors:** MD Wahiduzzaman Khan, Mingshan Jia, Xiaolin Zhang, En Yu, Kaska Musial-Gabrys
**Links:** [abs](https://arxiv.org/abs/2607.28032) - [pdf](https://arxiv.org/pdf/2607.28032)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Split and Drive: Dual-Axis Disentanglement for Real-Time Gaussian Head Avatars
- 作者：MD Wahiduzzaman Khan, Mingshan Jia, Xiaolin Zhang, En Yu, Kaska Musial-Gabrys
- 出版日期：2026-07-30
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：https://arxiv.org/abs/2607.28032

### 一句话总结
提出一个基于双轴解耦的单图高斯头部虚拟形象框架 SpiD，通过内化逐帧驱动和分解面部特征分支，在包含完整驱动流程的情况下实现了最快推理速度。

### 研究问题
如何从单张图像生成照片级真实感、可动画化的头部虚拟形象，同时消除推理阶段对外部跟踪管线的依赖，并解决统一表示中不同几何面部区域相互纠缠导致的表达力与渲染保真度受限问题。

### 核心思路/方法
提出“双轴解耦”（Dual-Axis Disentanglement）设计：
1. **计算轴（Compute Axis）**：将逐帧驱动过程内化为模型自身计算的一部分，从而在推理时不再依赖外部跟踪管线。
2. **特征轴（Feature Axis）**：将头部虚拟形象分解为三个专用高斯分支，每个分支分别建模一个几何上不同的面部区域（具体区域划分摘要未详细说明）。

### 主要贡献
- 提出 SpiD 框架，首次在单图高斯头部虚拟形象中同时实现计算轴与特征轴的双重解耦。
- 消除推理阶段的外部跟踪依赖，使得实测推理速度包含完整驱动流程，更贴近真实应用场景。
- 在多个对比实验中，性能持续优于现有最先进方法，并且是所比较方法中推理速度最快的。

### 局限性
- 摘要未提供三个高斯分支具体对应的面部区域划分细节。
- 摘要未提及方法在极端表情、遮挡、非正面视角或不同光照条件下的表现。
- 摘要未提供定量实验数据（如具体 FPS、PSNR/SSIM 数值）或与其他方法的详细性能差距。
- 摘要未说明训练所需数据规模、计算资源要求及泛化能力测试情况。

### 阅读优先级
**中**
理由：该工作针对单图头部虚拟形象生成的实时性瓶颈，提出了具有实用价值的双轴解耦架构，且强调包含完整驱动管道的推理速度优势，对数字人合成与实时渲染领域有一定参考意义。然而，摘要中缺乏具体实验数据（如量化指标、可视化结果），且未提供实现细节与消融分析，难以直接评估其技术效果的显著程度，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Creating photorealistic animatable head avatars from a single image remains a fundamental challenge in digital human synthesis. While recent 3D Gaussian Splatting methods have achieved promising results, they rely on external tracking pipelines whose latency is excluded from inference measurements. Furthermore, they adopt unified representations that entangle geometrically distinct facial regions, limiting both expressiveness and rendering fidelity. We propose SpiD (Split and Drive), a single-image Gaussian head avatar framework built on two disentanglement axes. The compute axis internalizes per-frame driving, eliminating external tracking dependency at inference. The feature axis decomposes the avatar into three specialized Gaussian branches, each modeling a geometrically distinct facial domain. Extensive experiments demonstrate consistently strong performance against state-of-the-art methods while achieving the fastest inference speed among all compared methods on a single GPU with the complete driving pipeline included.

</details>

#### 2026-07-30 - 4DHumanDiff: Direct Text-to-4DGS Generation for Consistent 360-Degree Dynamic Humans

**Authors:** Renlong Wu, Haoran Chen, Yuxiang Wei, Xiaowei Jin, Wangmeng Zuo, Hui Li
**Links:** [abs](https://arxiv.org/abs/2607.27634) - [pdf](https://arxiv.org/pdf/2607.27634)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, scene reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4DHumanDiff: Direct Text-to-4DGS Generation for Consistent 360-Degree Dynamic Humans
- 作者：Renlong Wu, Haoran Chen, Yuxiang Wei, Xiaowei Jin, Wangmeng Zuo, Hui Li
- 出版日期：2026-07-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.27634 ；PDF: https://arxiv.org/pdf/2607.27634

### 一句话总结
本文提出4DHumanDiff，一个直接从文本提示端到端生成由4D高斯泼溅（4DGS）表示的动态人体模型的扩散框架，可在约一分钟内生成360度一致动态人体，推理时间较现有方法降低10倍以上。

### 研究问题
现有文本生成动态人体资产的方法通常先合成单目或多视角视频，再拟合4D表示，该流程成本高且容易出现几何不完整或视角不一致的渲染结果。本文旨在解决如何在文本提示下直接、高效、一致地生成完整360度动态人体资产的问题。

### 核心思路/方法
- 直接建模结构化的4D表示空间，端到端生成4DGS动态人体，避免视频预生成和逐场景重建。
- 采用3D U-Net骨干网络并引入时间注意力机制，实现运动感知的生成。
- 构建大规模text-to-4DGS数据集（60,000个高质量文本-4DGS对）。
- 引入2D正则化提升渲染质量，并提出免训练的4D插值方法增强运动平滑性。

### 主要贡献
- 提出首个直接从文本生成4DGS动态人体的扩散框架，免去视频中间步骤和逐场景重建。
- 构建60,000对的大规模text-to-4DGS训练数据集。
- 通过2D正则化和免训练4D插值，提升渲染质量与运动平滑度。
- 实验显示所提方法能在一分钟内生成一致的360度动态人体，获得更好的时间一致性和多视角一致性，并将推理时间降低10倍以上。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法直接针对文本到动态3D资产生成这一热点方向，绕开了传统多阶段流程，在效率（10倍以上提速）和一致性（360度、时间与多视角）上均有明显提升，并附带大规模数据集，对神经场景表示、内容生成和渲染领域的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Generating high-quality 360-degree dynamic human assets from text prompts is challenging. Existing methods usually synthesize monocular or multi-view videos first and then fit a 4D representation, which is expensive and often causes incomplete geometry or view-inconsistent renderings. We present 4DHumanDiff, a diffusion framework that directly generates dynamic humans represented by 4D Gaussian Splatting (4DGS) from text prompts. By modeling the structured 4D representation space end-to-end, 4DHumanDiff avoids video pre-generation and per-scene reconstruction, making it better suited for view-consistent and temporally coherent asset generation. The model uses a 3D U-Net backbone with temporal attention for motion-aware generation. We further construct a large-scale text-to-4DGS dataset with 60,000 high-quality pairs, and introduce 2D regularization and training-free 4D interpolation to improve rendering quality and motion smoothness. Experiments show that 4DHumanDiff generates consistent 360-degree dynamic humans within one minute, achieves better temporal and multi-view consistency, and reduces inference time by more than 10x.

</details>

#### 2026-07-29 - StructureGS: Structure-aware Gaussian Splatting for Articulated Object Reconstruction

**Authors:** Gahye Lee, Gyoonseo Kim, Wonjong Jang, Jooeun Son, Seungyong Lee
**Links:** [abs](https://arxiv.org/abs/2607.26889) - [pdf](https://arxiv.org/pdf/2607.26889)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StructureGS: Structure-aware Gaussian Splatting for Articulated Object Reconstruction
- 作者：Gahye Lee, Gyoonseo Kim, Wonjong Jang, Jooeun Son, Seungyong Lee
- 出版日期：2026-07-29
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：摘要页: https://arxiv.org/abs/2607.26889 ; PDF: https://arxiv.org/pdf/2607.26889

### 一句话总结
本文提出StructureGS，一种将结构感知约束（如空间一致性和结构连通性）集成到3D高斯溅射框架中的方法，用于重建具有清晰部件几何与边界的铰接物体。

### 研究问题
如何解决铰接物体（含多个可动部件）重建中由于几何、外观和运动参数相互纠缠，导致部件分解模糊、边界不清和几何伪影的问题。

### 核心思路/方法
- 基础框架：基于3D Gaussian Splatting进行铰接物体重建。
- 关键创新：引入结构化导向信息，具体利用物体部件的有向包围盒来施加两类结构约束：
  - 空间一致性：约束每个部件的几何在其指定区域内保持紧凑且空间连贯。
  - 结构连通性：强制相邻部件之间保持物理上合理的接触关系。
- 实现手段：通过结构感知损失函数，将显式结构约束注入优化过程。

### 主要贡献
1. 提出了StructureGS，一个集成了结构感知导向的铰接物体重建框架，有效改善了部件分解质量。
2. 设计了基于有向包围盒的空间一致性和结构连通性约束，为优化提供显式结构先验。
3. 实验表明，该方法在铰接物体重建任务上达到了最先进性能，生成了部件几何清晰的高质量结果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**

理由：本文方法专注于铰接物体的3D重建这一具体问题，利用结构先验改进部件分解。对于从事神经渲染、物体重建或机器人操作等领域的读者，该方法结合了经典几何约束与现代场景表示，具有参考价值。但如果读者主要关注通用场景渲染或无铰接结构的静态重建，则相关性较低。摘要未提供消融实验或失败案例等细节，因此初步判断为中等优先级。

</details>

<details>
<summary>Abstract</summary>

Reconstructing articulated objects with multiple movable parts is essential for understanding object structure and enabling physical interaction. However, this reconstruction task poses significant challenges due to the entanglement of geometry, appearance, and motion parameters during optimization. Existing methods rely primarily on photometric supervision, which commonly fails to disentangle these interdependent components, resulting in poor part decomposition with blurred boundaries and geometric artifacts. To address this limitation, we introduce StructureGS, a reconstruction framework for articulated objects that integrates structure-aware guidance into 3D Gaussian Splatting. Our approach leverages oriented bounding boxes of object parts to enforce two key structural properties: spatial coherence, which constrains each part's geometry to remain compact and spatially coherent within its designated region, and structural connectivity, which enforces physically plausible contact relationships between adjacent parts. These properties are realized through structure-aware losses that inject explicit structural constraints into the optimization process. Extensive experiments demonstrate that our method achieves state-of-the-art performance in articulated object reconstruction, producing high-quality results with well-defined part geometries.

</details>

#### 2026-07-29 - 3DGBGS: 3D Granular Ball Gaussian Splatting for Compact Novel View Synthesis

**Authors:** Meng Yang, Shuyin Xia, Dawei Dai, YiWang
**Links:** [abs](https://arxiv.org/abs/2607.26578) - [pdf](https://arxiv.org/pdf/2607.26578)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** SfM, Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3DGBGS: 3D Granular Ball Gaussian Splatting for Compact Novel View Synthesis
- 作者：Meng Yang, Shuyin Xia, Dawei Dai, YiWang
- 出版日期：2026-07-29
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2607.26578，PDF: https://arxiv.org/pdf/2607.26578

### 一句话总结
3DGBGS 是一种基于颗粒球（Granular Ball）思想的紧凑型3D高斯溅射框架，通过自适应划分点云并初始化锚点，在减少模型存储的同时保持新视角合成质量。

### 研究问题
现有基于锚点的3D高斯溅射方法通常使用固定体素化从稀疏SfM点云构建锚点，无法充分适应空间非均匀点分布，导致锚点数量、模型紧凑性和渲染质量之间存在权衡。该研究旨在解决这一问题。

### 核心思路/方法
提出3DGBGS框架，核心步骤包括：
- **自适应颗粒球划分**：将SfM点云自适应划分为3D颗粒球，大球紧凑表示平滑冗余区域，小球保留复杂几何和局部细节。
- **颗粒球锚点初始化（GBAI）**：利用颗粒球中心初始化紧凑锚点位置。
- **颗粒球尺度先验（GBSP）**：利用颗粒球半径提供局部尺度先验，用于高斯生成。

### 主要贡献
基于摘要，主要贡献包括：
- 提出了结合颗粒球计算（GBC）与锚点型3DGS的紧凑框架。
- 通过GBAI和GBSP模块，实现自适应、紧凑的锚点初始化与尺度指导。
- 在四个基准数据集上，平均减少初始锚点37.1%、最终锚点10.0%，模型存储降低9.8%，同时保持可比的渲染质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。
理由：该方法针对3DGS模型紧凑性提出了新颖的颗粒球自适应策略，实验改进了锚点数量与存储效率，适合对3D场景渲染紧凑性有兴趣的读者。但未与更多最新方法对比或讨论实时性等关键细节，优先级中等。

</details>

<details>
<summary>Abstract</summary>

Three-dimensional Gaussian Splatting (3DGS) enables high-quality real-time novel-view synthesis through explicit Gaussian primitives and differentiable rasterization. 3DGS and Granular Ball Computing (GBC), proposed in 2019, share a natural compatibility in adaptive representation. The efficiency of 3DGS partly stems from a coarse-to-fine and on-demand refinement process that draws on the generation principle of GBC. This connection motivates us to further introduce adaptive granular ball organization into anchor-based 3DGS. Existing anchor-based methods typically construct anchors from sparse SfM point clouds through fixed voxelization, which cannot adequately adapt to spatially non-uniform point distributions and leads to a trade-off among anchor count, model compactness, and rendering quality. To address this issue, we propose 3DGBGS (3D Granular Ball Gaussian Splatting), a compact anchor-based framework for novel-view synthesis. 3DGBGS adaptively partitions SfM point clouds into 3D granular balls, using larger balls to compactly represent smooth and redundant regions and smaller balls to preserve complex geometry and local details. Based on this representation, Granular Ball Anchor Initialization (GBAI) uses granular ball centers to initialize compact anchor positions, while the Granular Ball Scale Prior (GBSP) exploits granular ball radii to provide local scale priors for Gaussian generation. Experiments on four benchmarks show that 3DGBGS reduces initial and final anchors by 37.1% and 10.0%, respectively, and model storage by 9.8% on average, while maintaining comparable rendering quality.

</details>

#### 2026-07-29 - AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting

**Authors:** ByungHyun Kim, Jinwoo Jeon, Woontack Woo
**Links:** [abs](https://arxiv.org/abs/2607.26525) - [pdf](https://arxiv.org/pdf/2607.26525)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting
- 作者：ByungHyun Kim, Jinwoo Jeon, Woontack Woo
- 出版日期：2026-07-29T06:43:17Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.26525

### 一句话总结
AtlasLC 是一种无需原始源数据、无需训练、直接对已发布的物体级3D高斯泼溅资产进行快速压缩的管线，通过局部竞争剪枝和确定性地图打包技术，在减少压缩时间的同时维持可比的几何与感知质量。

### 研究问题
现有3DGS压缩方法主要针对场景级捕获设计，依赖繁重的布局生成或激进的全域剪枝，不适用于语义集中的前景物体；在XR实际管线中，物体级资产需要反复打包、传输、解码和实例化，因此现有方法在资产准备成本、编解码兼容性、解码延迟以及深度和轮廓线索保留方面表现不佳。本文旨在解决如何针对物体级3DGS实现快速、编解码器就绪且部署友好的压缩。

### 核心思路/方法
AtlasLC 结合了局部竞争剪枝与确定性地图打包，直接操作已发布的3DGS资产（无需原始图像、相机位姿或逐资产优化）。具体地：
- **局部竞争剪枝**：在保持物体前景整体支撑的前提下，去除冗余高斯点。
- **单次排序条件传输**：作为轻量级、单遍的共享坐标骨干，连接剪枝与打包阶段，避免映射/重映射瓶颈。
- **确定性地图打包**：无需额外布局生成，直接打包高斯点，减少预处理时间。

### 主要贡献
1. 提出一种无需源数据、无需训练的直接压缩管线，适用于已发布的物体级3DGS资产。
2. 将地图准备时间降低最高25倍，端到端压缩时间降低最高5倍。
3. 在相似压缩尺寸下，比特数比紧凑结构化基线减少约6%~8%，同时保持可比的感知和几何质量。
4. 提供更优的部署感知平衡：兼顾有效载荷、解码延迟、运行时FPS和3D几何保真度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接针对XR实际部署中的物体级3DGS资产压缩瓶颈，提出了无需原始数据、无需训练的快速方案，且显著降低压缩时间和比特率。对于关注3DGS在XR/移动设备落地或编解码器优化的研究者与工程师，具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic novel-view synthesis with real-time rendering, but deploying compressed object-centric 3DGS in XR requires more than image-space rate-distortion. In practical XR asset pipelines, reusable objects are repeatedly packaged, transmitted, decoded, and instantiated, making asset-preparation cost, codec compatibility, decoding latency, and preservation of depth and silhouette cues first-class concerns. Existing 3DGS compression methods are largely developed for scene-scale captures and often rely on heavy layout generation or aggressive global pruning, assumptions that transfer poorly to semantically concentrated foreground objects. We present AtlasLC, a source-free, training-free compression pipeline for object-centric 3DGS that operates directly on released Gaussian assets, without original images, camera poses, or per-asset optimization. AtlasLC couples local-competition pruning with deterministic atlas packing to remove the mapping/remapping bottleneck while preserving object-wide foreground support; a lightweight single-pass sort-based conditional transport is used as a shared coordinate backbone for these stages. Across the evaluated assets, AtlasLC reduces atlas-preparation time by up to a factor of 25 and end-to-end compression time by up to a factor of 5, while offering a favorable deployment-aware balance of payload, decode latency, runtime FPS, and 3D geometry relative to the evaluated compressed baselines. Relative to similarly compact structured baselines, it uses about 6 to 8 percent fewer bits while maintaining comparable perceptual and geometric quality. These results show that object-centric 3DGS compression should be optimized for a deployment-aware operating point enabling scalable XR asset libraries.

</details>

## Embodied / Robotics / AR Applications

### 2026-08

#### 2026-08-03 - DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation

**Authors:** Jiaming Chen, Guoan Xu, Aoshen Huang, Haozhuo Zhang, Yang Li, Wei Pan
**Links:** [abs](https://arxiv.org/abs/2608.02428) - [pdf](https://arxiv.org/pdf/2608.02428)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DF³: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation
- 作者：Jiaming Chen, Guoan Xu, Aoshen Huang, Haozhuo Zhang, Yang Li, Wei Pan
- 出版日期：2026-08-03T16:08:59Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.02428

### 一句话总结
本文提出一种完全在潜空间内进行未来状态预测、无需解码器的世界建模框架 DF³，面向自动驾驶中的感知与控制任务，实现高效率和灵活部署。

### 研究问题
如何在不依赖像素级生成或解码器的情况下，高效预测视频序列中的未来状态，并将其直接用于自动驾驶中的下游任务（如感知与控制），以降低计算开销并提升系统灵活性。

### 核心思路/方法
- 提出 Decoder-Free Feature Forecasting（DF³）框架，完全在潜空间内建模世界演化，直接生成任务输出，彻底移除了解码器。
- 具体做法：向冻结的视觉基础模型的末端模块注入可学习的空间查询（spatial queries），直接提取未来状态表征。
- 设计轻量化的 Motion-Aware Context Fusion（MACF）机制，将粗粒度光流扭曲与细粒度潜空间互相关相结合，使查询与历史 token 表示交互，显式对齐并预测下一帧的特征。
- 随后使用一组专门的任务查询（task queries）对这些预测特征进行探测，以支撑下游任务。

### 主要贡献
- 首次提出完全无解码器的未来特征预测框架，消除解码器带来的计算瓶颈。
- 设计了可学习的空间查询与轻量级运动感知上下文融合机制，实现高效且准确的未来状态表征预测。
- 在公开基准和机器人模拟器的零样本部署实验中，表明该方法在达到与最先进方法相当性能的同时，具备更优的效率和灵活性，适用于集成感知与控制系统。

### 局限性
摘要未提供足够信息。摘要中未明确讨论方法的失败场景、潜在的信息丢失问题、对冻结视觉基础模型的依赖限制、亦未给出定量对比的细节或消融研究。

### 阅读优先级
**中**。理由：该工作针对自动驾驶中世界建模的计算瓶颈提出了一种新颖的去解码器思路，方法设计具有创新性，且强调效率与灵活性，可能与具身智能与机器人方向相关；但如果读者不关注潜空间预测或无解码器架构，则优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

Forecasting future states from video sequences is a critical challenge for autonomous robotic systems and a fundamental objective of world modeling. Prior generative methods operating at the pixel level inevitably overemphasize task-irrelevant details, leading to prohibitive computational overhead. While latent-based approaches attempt to mitigate this by predicting features directly, the persistent reliance on heavy decoders for state-to-task mapping remains a computational bottleneck. In this work, we propose Decoder-Free Feature Forecasting (DF$^3$), a novel framework that models world evolution entirely within the latent space and directly derives task outputs, completely eliminating the need for a decoder. Specifically, DF$^3$ injects learnable spatial queries into the terminal blocks of a frozen vision foundation model to extract future state representations directly. By employing a lightweight, unified Motion-Aware Context Fusion (MACF) mechanism that seamlessly integrates coarse flow warping with fine-grained latent cross-correlation, these queries interact with historical token representations to explicitly align and forecast the feature of the next frame. Subsequently, a specialized set of task queries probes these forecasted features for the downstream task. Extensive experiments on public benchmarks and zero-shot deployment in a robotic simulator demonstrate that DF$^3$ achieves performance comparable to state-of-the-art methods while offering superior efficiency and flexibility for integrated perception and control.

</details>

#### 2026-08-02 - SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space

**Authors:** Ruiteng Zhao, Zhengshen Zhang, Yue Su, Wenshuo Wang, Jiahui Li, Zhiyuan Yang, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu
**Links:** [abs](https://arxiv.org/abs/2608.01397) - [pdf](https://arxiv.org/pdf/2608.01397)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space
- 作者：Ruiteng Zhao, Zhengshen Zhang, Yue Su, Wenshuo Wang, Jiahui Li, Zhiyuan Yang, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu
- 出版日期：2026-08-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.01397

### 一句话总结
本文提出 SG-WAM，一种在策略派生的表征空间中自监督学习几何感知的动作条件动力学模型，通过联合优化潜在未来预测、几何约束和流匹配动作生成，在 LIBERO 基准上取得 98.5% 平均成功率。

### 研究问题
现有世界动作模型（WAM）在动作生成中耦合未来状态预测，但对未来动力学的建模空间存在不足：要么使用感知密集的观测空间目标，要么使用辅助潜在空间，难以同时满足动作相关性和几何感知性。本文旨在解决如何构建一个既与动作生成对齐又具备几何感知的未来建模空间这一问题。

### 核心思路/方法
- 提出 SG-WAM 框架，在策略派生的表征空间中直接学习几何感知、动作条件的动力学模型。
- 引入可学习的动力学令牌（learnable dynamics tokens）和自引导世界预测器（Self-Guided World Predictor），在机器人动作干预下预测这些令牌的未来潜在状态。
- 预测目标由同一策略骨干网络（policy backbone）的指数移动平均（EMA）副本生成，为动作专家所使用的表征族提供稳定监督。
- 通过几何监督（geometric supervision）对策略图像令牌表征进行结构化，为动力学令牌提供空间上有依据的上下文，从而构建一个既动作相关又几何感知的未来对齐空间。
- 将潜在未来预测、几何接地和流匹配动作生成在统一框架中端到端联合优化。

### 主要贡献
- 提出 SG-WAM，一种自引导世界建模框架，在策略表征空间中联合学习几何感知的动作条件动力学。
- 采用 EMA 副本作为预测目标来源，实现在动作专家表征族内的稳定自监督。
- 通过几何监督强化图像令牌表征的空间结构，使未来对齐空间兼具动作相关性与几何感知性。
- 基于 0.9B 参数模型（无大规模具身预训练），在 LIBERO 上达到 98.5% 平均成功率、LIBERO-Plus 上达到 73%，并在分布内和分布外的真实世界评估中优于强基线方法。

### 局限性
摘要未提供足够信息，无法获知该方法的失败场景、计算开销、泛化边界或伦理影响等局限性细节。

### 阅读优先级
**高**。理由：该方法在 LIBERO 基准上取得接近完美的成功率（98.5%），且在分布外真实世界评估中优于强基线，同时模型规模仅 0.9B 且无需大规模具身预训练，对于机器人操作领域的世界建模与动作生成研究具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

World Action Models (WAMs) couple action generation with prediction of future states. Their effectiveness depends on whether future dynamics are modeled in a space that is both aligned with action generation and sufficiently geometry-aware to capture where and how actions change the scene. Existing WAMs typically satisfy only part of this requirement, relying on either perceptually heavy observation-space targets or auxiliary latent spaces that are not jointly structured for action relevance and geometry. We propose SG-WAM, a self-guided framework that learns geometry-aware action-conditioned dynamics directly in the policy-derived representation space. SG-WAM introduces learnable dynamics tokens and a Self-Guided World Predictor that forecasts their future latent states conditioned on intervening robot actions. Prediction targets are generated by an exponential moving average copy of the same policy backbone, providing stable supervision within the representation family used by the action expert. Geometric supervision further structures the policy image-token representations, providing spatially grounded context for the dynamics tokens and yielding a future-alignment space that is both action-relevant and geometry-aware. Latent future prediction, geometric grounding, and flow-matching action generation are jointly optimized end-to-end in a unified framework. Built on a 0.9B model without large-scale embodied pretraining, SG-WAM achieves 98.5% average success on LIBERO and 73% on LIBERO-Plus, while outperforming strong baselines in both in-distribution and out-of-distribution real-world evaluations.

</details>

### 2026-07

#### 2026-07-30 - When Robots Exchange Meaning: A Demo of Goal-Oriented Semantic Communications for Collaborative Robotics

**Authors:** Peizheng Li, Xinyi Lin, Sajida Gufran, Adnan Aijaz
**Links:** [abs](https://arxiv.org/abs/2607.28256) - [pdf](https://arxiv.org/pdf/2607.28256)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D mapping, embodied AI, robotics, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：When Robots Exchange Meaning: A Demo of Goal-Oriented Semantic Communications for Collaborative Robotics
- 作者：Peizheng Li, Xinyi Lin, Sajida Gufran, Adnan Aijaz
- 出版日期：2026-07-30
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.28256

### 一句话总结
本文演示了一个面向协作机器人的机器人-边缘语义通信测试平台，通过VQ-VAE令牌传输实现RGB图像的42.67倍压缩，并重建为语义地图以支撑任务级机器人应用。

### 研究问题
在面向6G的任务导向型协作机器人场景中，通信质量应体现于任务执行与环境理解，而非仅以数据包传递来衡量；本文旨在构建一个从语义视觉传输到对象级地图交互的完整演示平台。

### 核心思路/方法
- 搭建机器人-边缘语义通信测试平台，包括机器人端视觉压缩、边缘端语义建图以及基于浏览器的任务交互界面。
- 机器人端配备RGB-D传感器与LiDAR，运行ROS 2；边缘节点使用Jetson Orin进行重建、RTAB-Map建图、语义对象处理及可视化。
- 具体实现：机器人端通过ONNX Runtime编码器将RGB帧编码为VQ-VAE令牌，边缘端使用PyTorch解码器重建图像。
- 320×240图像被表示为80×60令牌网格，打包负载为5400字节，相较模型输入RGB字节实现42.67倍压缩。
- 重建后的视觉流与深度、位姿和3D建图信息关联，生成语义地图供下游机器人应用使用。

### 主要贡献
- 构建了完整的机器人-边缘语义通信演示路径，覆盖从语义视觉传输到对象级地图交互。
- 提供了一个结合语义通信、具身AI与物理AI的实用测试平台，用于未来任务感知6G网络研究。
- 给出了初步的压缩效率验证（42.67倍缩减）以及实际演示视频链接。

### 局限性
摘要未提供足够信息，具体包括：未说明VQ-VAE训练数据集与训练细节，未报告重建图像质量指标（如PSNR/SSIM）或语义建图精度评估结果，也未讨论不同网络条件或任务场景下的系统性性能对比。

### 阅读优先级
**中**。理由：该文为演示论文，侧重于系统集成与概念验证，而非深度方法创新或完整实验评估。对于关注语义通信与机器人结合的研究者有一定参考价值，但如需深入了解性能与算法细节，摘要提供的信息有限，建议结合视频或其他扩展材料阅读。

</details>

<details>
<summary>Abstract</summary>

Collaborative robotics is a representative task-oriented 6G use-case, where communication quality should be reflected in mission execution, environment understanding, and closed-loop operation rather than packet delivery alone. This demo paper presents a robot-edge semantic communication (SemCom) testbed integrating robot-side visual compression, edge-side semantic mapping, and dashboard-based mission interaction. A mobile robot equipped with RGB-D sensing and LiDAR runs ROS 2, while a Jetson Orin edge node performs reconstruction, RTAB-Map mapping, semantic object handling, and browserbased visualization. As an initial proof of concept, RGB frames are encoded on the robot into VQ-VAE tokens using an ONNX Runtime encoder and reconstructed on the edge using a PyTorch decoder. A 320 X 240 image is represented by an 80 X 60 token grid with a packed payload of 5400 bytes, corresponding to a 42.67X reduction relative to model-input RGB bytes. The reconstructed visual stream is further associated with depth, pose, and 3D mapping information to generate a semantic map for downstream robotic applications. The demo exposes the full path from semantic visual transport to object-level map interaction, and provides a practical platform for future task-aware 6G networking studies at the intersection of SemCom, embodied AI, and physical AI-enabled robotics. A video of the demo is available at https://tinyurl.com/Tos09

</details>

#### 2026-07-30 - mmRadarTwin: A Measurement-Calibrated Signal-Level Digital Twin Platform for Indoor mmWave Radar

**Authors:** Jianyi Zhou, Chenghao Zhang, Yanli Li, Dong Yuan
**Links:** [abs](https://arxiv.org/abs/2607.28108) - [pdf](https://arxiv.org/pdf/2607.28108)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：mmRadarTwin: A Measurement-Calibrated Signal-Level Digital Twin Platform for Indoor mmWave Radar
- 作者：Jianyi Zhou, Chenghao Zhang, Yanli Li, Dong Yuan
- 出版日期：2026-07-30
- 分类：Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：https://arxiv.org/abs/2607.28108

### 一句话总结
mmRadarTwin是一个面向室内毫米波雷达的、信号级且带路径归因的数字孪生平台，通过共享接收通道和距离-角度处理接口将真实雷达测量与虚幻引擎场景仿真连接，实现同域比较与诊断。

### 研究问题
室内毫米波雷达感知难以复现，因为测量的距离-角度响应受场景几何、材料响应、多径、硬件约定和信号处理等多种因素影响；现有光线追踪和数字孪生工具多暴露渲染、信道或路径级量，而雷达感知需要能在与真实FMCW测量相同域中处理和比较的复杂信号产品。

### 核心思路/方法
- 构建信号级、路径归因的数字孪生平台，包含两条分支：真实雷达测量分支 与 虚幻引擎场景仿真分支，二者通过共享的接收通道和距离-角度处理接口对接。
- 仿真器输出复数多通道接收网格，并导出每条路径的贡献记录，标识模拟返回的参与者（actor）、材料标签、传播事件和输出bin支持。
- 在办公室部署中使用商用单站毫米波雷达和移动场景采集硬件进行评估。

### 主要贡献
- 提出mmRadarTwin平台，实现信号级（非路径级或渲染级）的室内毫米波雷达数字孪生仿真。
- 建立测量与仿真共享的接收通道和距离-角度处理接口，支持同域比较。
- 提供每路径贡献记录，可识别参与者、材料、传播事件及输出位置，便于诊断仿真与实测差异。
- 在真实办公环境、154个测量位姿、22个雷达位置上进行评估，召回率70.8%，展示了实用的系统工作流。

### 局限性
摘要未提供足够信息，但根据摘要可明确：作者并不声称实现完整的雷达图重建或跨房间泛化；平台当前性能受限于弱/缺失路径支持、响应偏移、不支持锚点及缺失物理机制导致的残差。其他实验细节（如精度、运行时间、各类型残差的具体量化等）摘要未提供。

### 阅读优先级
**中**

理由：该工作提供了一个可工作的信号级室内毫米波雷达数字孪生平台，且已通过真实测量验证（70.8%召回率），对从事毫米波雷达仿真或室内感知的研究者有一定参考价值。但根据摘要，作者明确表示未实现完整重建或跨房间泛化，且未展示对下游任务的提升效果；若读者关注高精度重建或通用泛化，本工作的实用性可能有限。因此建议按需阅读，不必优先。

</details>

<details>
<summary>Abstract</summary>

Indoor mmWave radar perception is difficult to reproduce because measured range-angle responses depend on scene geometry, material response, multipath, hardware conventions, and signal processing. Existing ray-tracing and digital-twin tools often expose rendering, channel, or path-level quantities, while radar sensing requires complex signal products that can be processed and compared in the same domain as real FMCW measurements. We present mmRadarTwin, a signal-level and path-attributed digital-twin platform for indoor mmWave radar. mmRadarTwin links a real radar measurement branch with an Unreal Engine scene-simulation branch through a shared receive-channel and range-angle processing interface. The simulator writes complex multi-channel receive grids and exports per-path contribution records that identify the actor, material tag, propagation event, and output-bin support of each simulated return. We evaluate mmRadarTwin in an office deployment using a commodity monostatic mmWave radar and mobile scene-capture hardware. Across 154 measured poses spanning 22 radar locations, the current physics-only path-basis simulator recalls 70.8% of measurement-active geometry-supported response regions in the central usable field of view while exposing residuals caused by weak or missing path support, shifted responses, unsupported anchors, and missing physical mechanisms. Rather than claiming complete radar-map reconstruction or cross-room generalization, mmRadarTwin establishes a practical systems workflow for constructing, comparing, and diagnosing indoor radar digital twins.

</details>

#### 2026-07-30 - ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow

**Authors:** Dongxiu Liu, Haoyi Niu, Peng Cheng, Yuan Gao, Xirui Kang, Sangli Teng, Koushil Sreenath, Xianyuan Zhan
**Links:** [abs](https://arxiv.org/abs/2607.27924) - [pdf](https://arxiv.org/pdf/2607.27924)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow
- 作者：Dongxiu Liu, Haoyi Niu, Peng Cheng, Yuan Gao, Xirui Kang, Sangli Teng, Koushil Sreenath, Xianyuan Zhan
- 出版日期：2026-07-30T09:37:30Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.27924

### 一句话总结
ODEWorld 是一种基于物理时间连续流的潜空间世界模型，通过 ODE 参数化连续动力学，支持任意时间分辨率预测、反向预测并缓解表征坍缩问题。

### 研究问题
现有世界建模方法主要局限于离散时间预测，难以高效捕捉物理世界中空间与时间的连续动态特性。作者试图构建一个连续时间潜变量世界模型，以更自然地建模物理世界动态。

### 核心思路/方法
- 提出 Physical-Time Flow（PT-Flow）：在结构化表示空间中学习一个连续的潜速度场，并用常微分方程（ODE）参数化时序数据的底层动态。
- 未来预测被重构为在压缩潜空间中对 ODE 进行时间积分。
- 基于 PT-Flow 构建 ODEWorld，提取时变特征，并在动力学表示空间和潜速度场上施加 ODE 约束，以解决潜世界模型中的表征坍缩问题。
- 由于模型本质连续，支持任意时间分辨率预测和反向预测。

### 主要贡献
- 提出 PT-Flow 连续潜动力学学习方法，并用 ODE 参数化物理时间动态。
- 构建 ODEWorld 连续时间潜世界模型，兼具效率与通用性，并解决潜世界模型长期存在的表征坍缩问题。
- 在长时程预测后仍能实现高质量图像重建。
- 支持任意时间分辨率预测与反向预测，突破了离散时间模型的能力边界。
- 可提供丰富的规划导向信息，促进下游策略学习。
- 实验表明 ODEWorld 在视频生成和机器人控制任务中均表现出色，兼顾规划导向的动力学抽象与视觉真实感。

### 局限性
摘要未提供足够信息。摘要中未明确讨论该方法的潜在局限性，例如计算开销、ODE 求解器的数值稳定性、对高维复杂场景的扩展性、训练数据需求等均未提及。

### 阅读优先级
**高**
理由：该工作提出了一个新颖的连续时间潜世界模型范式，直接挑战主流离散时间世界模型，且研究目标跨足视频生成与机器人控制，在具身智能和连续动力学建模方向具有较高的学术价值与潜在应用前景。摘要中实验覆盖两类任务且宣称性能优越，值得关注。

</details>

<details>
<summary>Abstract</summary>

In the physical world we inhabit, space and time are fundamentally continuous. However, existing machine learning paradigms for world modeling are largely confined to discrete-time prediction, thereby exhibiting significant inefficiency in capturing the dynamics of physical world. We introduce Physical-Time Flow (\textbf{PT-Flow}), a novel approach that learns a continuous latent velocity field operating in physical time. Crucially, the underlying dynamics of sequential data are parameterized by an ordinary differential equation (ODE) embedded in a well-structured representation space. Under this paradigm, the prediction of future can be recast as temporal integration via an ODE solver in the compressed latent space. Building upon PT-Flow, we construct \textbf{ODEWorld}, a continuous-time latent world model that is both efficient and versatile. By extracting time-variant features and enforcing ODE properties on both the dynamical representation space and the latent velocity field, ODEWorld effectively addresses the long-standing representation collapse issue in latent world model literature. This also enables high-quality image reconstruction even after long-horizon prediction. Moreover, its continuous nature allows for arbitrary temporal resolution and even backward prediction, which is impossible for most discrete-time models. Lastly, ODEWorld can provide rich planning-oriented information to facilitate downstream policy learning. Comprehensive experiments demonstrate that ODEWorld successfully reconciles planning-conducive dynamics abstraction with visual realism, excelling in both video generation and robotic control. \href{https://dstate.github.io/odeworld_website/}{Project Website}.

</details>

#### 2026-07-30 - Write-Safe Flow Field Mapping under Ambiguous Onboard Sensing and Localization Drift

**Authors:** Linhao Jin, Qimin Feng, Peter Gunnarson, Qiang Zhong
**Links:** [abs](https://arxiv.org/abs/2607.27713) - [pdf](https://arxiv.org/pdf/2607.27713)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Write-Safe Flow Field Mapping under Ambiguous Onboard Sensing and Localization Drift
- 作者：Linhao Jin, Qimin Feng, Peter Gunnarson, Qiang Zhong
- 出版日期：2026-07-30
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.27713

### 一句话总结
本文提出一种地图参考感知的保守融合框架，通过预测“写安全分数”来抑制移动机器人流场建图中因观测模糊和定位漂移导致的鬼影结构污染。

### 研究问题
移动机器人在依赖机载感知推断局部流场结构时，局部估计虽然局部看似合理，但直接写入全局地图可能不安全——相似的流场结构会产生模糊观测，而定位漂移会导致预测块被写入错误位置，重复的错误配准更新会积累成持久的鬼影结构。论文针对这一失效模式，研究如何在模糊感知和定位漂移下安全地进行流场地图写入。

### 核心思路/方法
提出一种地图参考感知的保守融合框架：
- 模型预测局部速度块（velocity patch）以及一个学习得到的写安全分数（write-safety score）。
- 该分数会持续衰减不确定的地图更新，同时在没有可靠地图参考时允许初始化。
- 通过这种门控机制，避免将不可靠的局部估计写入全局地图，从而减少鬼影污染。

### 主要贡献
- 提出地图参考感知的保守融合框架，引入学习式写安全分数。
- 在合成射流和横流环境中，该方法相比无门控融合将平均鬼影污染减少42%。
- 在真实推力器尾流数据上的零样本硬件回放中，鬼影污染减少39%，同时保留81%的地图覆盖率。
- 实验结果表明，在模糊感知和定位漂移条件下，安全地图写入对流场建图至关重要。

### 局限性
摘要未提供足够信息，未提及方法在复杂真实环境下的泛化能力、计算开销、对安全分数阈值的敏感性，或与现有方法的定量对比细节。

### 阅读优先级
**中**。理由：该工作针对移动机器人流场建图中的实际失效模式（感知模糊与定位漂移导致的鬼影污染），提出了有明确创新点的保守融合框架，且实验验证了有效性。但其主要面向流场建图这一特定下游任务，若读者关注机器人建图安全性或流场感知，则有较高参考价值；否则可作为一般性感知-建图融合问题的参考。

</details>

<details>
<summary>Abstract</summary>

Mobile robots can infer local flow structure from onboard sensing, but a locally plausible estimate is not always safe to write into a global map. Similar flow structures may produce ambiguous observations, while localization drift causes predicted patches to be written at incorrect locations. Repeated misregistered updates then accumulate into persistent ghost structures. We address this failure mode with a map-reference-aware conservative fusion framework. The model predicts a local velocity patch and a learned write-safety score that continuously attenuates uncertain map updates while permitting initialization when no reliable map reference is available. Across synthetic jet and crossflow environments, the proposed method reduces average ghost contamination by 42% relative to ungated fusion. A zero-shot hardware replay using real pressure and optical-flow measurements from a thruster wake further reduces ghost contamination by 39% while retaining 81% map coverage. These results show that safe map writing is critical for flow mapping under ambiguous sensing and localization drift.

</details>

#### 2026-07-29 - Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation

**Authors:** Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, Maoqing Yao
**Links:** [abs](https://arxiv.org/abs/2607.26646) - [pdf](https://arxiv.org/pdf/2607.26646)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation  
- 作者：Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, Maoqing Yao  
- 出版日期：2026-07-29  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.26646  

### 一句话总结  
该论文提出一个两阶段的前馈流水线，仅从单张360°全景图生成高质量、可自由探索的室内3D场景，无需逐场景优化或多视角输入，支持零样本泛化。

### 研究问题  
如何从单张360°全景图重建高质量、可自由导航的3D场景，同时解决现有方法缺乏度量轨迹控制、在大范围相机运动下处理大面积遮挡困难以及需要高端多GPU服务器的问题。

### 核心思路/方法  
- **第一阶段：全景视频生成**  
  - 使用NavMesh规划的SE(3)漫游轨迹，通过密集几何扭曲条件注入潜在视频扩散模型。  
  - 采用长-短轨迹混合训练和基于快捷模型的自一致性目标，在无无分类器引导的四步去噪中生成高保真全景视频。  
- **第二阶段：3D重建**  
  - 利用前馈式全景重建器将生成的视频提升为高保真3D高斯场景，支持实时自由视角漫游，可直接作为具身AI模拟资产。

### 主要贡献  
1. 提出一种两阶段流水线，将生成与重建通过显式、轨迹可控的全景视频桥接。  
2. 引入NavMesh规划轨迹注入、长短轨迹混合训练和基于快捷模型的自一致性目标，实现高效高质量视频生成。  
3. 在生成全景视频和下游3D重建任务上均优于几何条件基线，且零样本泛化到未见室内场景。

### 局限性  
摘要未提供足够信息。

### 阅读优先级  
**高**  
理由：该工作解决了具身AI中的关键问题（从单全景图到可导航3D场景的生成），方法创新性强（两阶段桥接生成与重建、快捷模型加速推理），实验证明性能优越且具备零样本泛化能力，对室内3D场景理解和模拟领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We address the problem of reconstructing a high-fidelity, freely navigable 3D scene from a single $360^\circ$ panorama, without per-scene optimization or multi-view capture. Existing methods either lack metric trajectory control, which hinders reliable downstream 3D reconstruction, or struggle with large disocclusions under long-range camera motion while requiring high-end multi-GPU servers.We present Genie Sim PanoWorld, a two-stage feed-forward pipeline that bridges generation and reconstruction via an explicit, trajectory-controllable panoramic video. A NavMesh-planned $\mathrm{SE}(3)$ roaming trajectory is injected into a latent video diffusion model through dense geometry-warped conditioning; long--short trajectory mixed training and a self-consistency objective based on shortcut models together yield high-fidelity video in four CFG-free denoising steps. A feed-forward panoramic reconstructor then lifts the generated video into a high-fidelity 3D Gaussian scene that supports real-time, free-viewpoint roaming and can be directly used as a simulation-ready asset for embodied AI applications. Experiments show that Genie Sim PanoWorld outperforms geometry-conditioned baselines in both panoramic video generation and downstream 3D reconstruction, while generalizing zero-shot to unseen indoor scenes.

</details>

#### 2026-07-28 - Spline-Based Boundary Representations for Sparse View Reconstruction and Simulation Using Isogeometric Analysis

**Authors:** Davor Dobrota, Vsevolod Skorokhodov, Chenghao Xu, Olga Fink, Malcolm Mielle
**Links:** [abs](https://arxiv.org/abs/2607.26234) - [pdf](https://arxiv.org/pdf/2607.26234)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spline-Based Boundary Representations for Sparse View Reconstruction and Simulation Using Isogeometric Analysis
- 作者：Davor Dobrota, Vsevolod Skorokhodov, Chenghao Xu, Olga Fink, Malcolm Mielle
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26234

### 一句话总结
本文提出FORGE-SIM方法，通过优化B样条边界表示，直接从稀疏RGB图像重建紧凑、光滑、水密的几何模型，并同步支持计算机辅助设计和数值仿真。

### 研究问题
如何从稀疏视角的RGB图像直接重建出既适合可视化、又满足数值仿真（如热仿真、模态分析）要求的显式、水密、光滑的几何模型，以消除计算机视觉与数值分析之间的表示鸿沟。

### 核心思路/方法
1. **直接优化样条表示**：不依赖传统网格或隐式表面，而是将多片B样条边界表示作为可优化参数，从稀疏图像中直接回归出几何。
2. **仿真兼容性设计**：重建的几何自动满足水密性和光滑性，原生兼容计算机辅助设计和等几何分析流程。
3. **场投影策略**：将观测得到的场（如热状态、语义信息）以相同样条基函数投影到重建模型上，使模型可直接用于仿真。

### 主要贡献
- 提出了FORGE-SIM，一种无需人工干预、从稀疏RGB图像直接重建多片B样条边界表示的方法。
- 重建的几何紧凑、光滑、水密，同时兼容设计软件与仿真工作流。
- 实现了将观测场（热、语义等）映射到同一样条基上，支持即时仿真应用。
- 模型质量足以支撑热仿真与模态分析，统一了图像重建与仿真建模的优化框架。

### 局限性
摘要未提供足够信息，无法得知具体性能指标、对比方法、失败案例或计算开销等局限性。

### 阅读优先级
**高**  
理由：该方法解决了计算机视觉与数值仿真之间的长期表示不兼容问题，对于数字孪生、仿真驱动设计等跨领域应用有重要启发意义。摘要提供的技术路径清晰、创新点明确，且实验（热仿真、模态分析）初步验证了可行性。建议优先阅读以评估方法细节。

</details>

<details>
<summary>Abstract</summary>

Image-based reconstruction aims to recover three-dimensional geometry from images. Recent advances have enabled the recovery of visually detailed models, yet their representations are not well-suited for numerical simulation. Simulation frameworks typically require explicit, watertight, and smooth geometries to ensure numerical robustness and accuracy, properties that surfaces extracted from image-based reconstructions lack. We propose FORGE-SIM, a method to directly reconstruct a multi-patch B-spline boundary representation from sparse posed RGB images without manual intervention. By optimizing the spline representation itself, our approach produces compact, smooth, and watertight geometries that are natively compatible with both Computer Aided Design and simulation workflows. Additionally, we introduce a strategy to project observation-derived fields, such as a thermal state and semantic information, onto the reconstructed models in the same spline basis, enabling immediate use in simulation. We demonstrate that the obtained models are of sufficiently high quality to enable thermal simulation and modal analysis. By unifying image-based reconstruction and simulation-ready modeling within a single optimization framework, this work removes a long-standing barrier between computer vision and numerical analysis. We anticipate that it will enable new workflows for simulation-driven design, inspection, and digital twin applications.

</details>

#### 2026-07-28 - BG-REAL: A Public Real-Data Anchored Benchmark for Background Manipulation Detection and Localization

**Authors:** Bugra Alperen Uluirmak, Rifat Kurban
**Links:** [abs](https://arxiv.org/abs/2607.26232) - [pdf](https://arxiv.org/pdf/2607.26232)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BG-REAL: A Public Real-Data Anchored Benchmark for Background Manipulation Detection and Localization
- 作者：Bugra Alperen Uluirmak, Rifat Kurban
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.26232，PDF: https://arxiv.org/pdf/2607.26232

### 一句话总结
本文提出BG-REAL，一个专注于背景操作检测与定位的公开真实数据锚定基准测试包，包含7000个处理样本、六种编辑类型，并揭示了现有基线模型因重编码伪影而产生的高误报率问题。

### 研究问题
背景操作是一种实用但定义不够清晰的图像取证场景：操纵证据可能位于显著性前景物体之外，而许多现有评估强调以物体为中心的复制-移动、拼接或通用合成编辑。因此，需要针对背景操作检测与定位的专用基准。

### 核心思路/方法
构建基于Open Images V7实例分割源的真实数据锚定基准测试包BG-REAL。包含7000个样本（6000个公共数据锚定样本+1000个合成对照样本），覆盖六种编辑家族、匹配的真实对照、源组划分、掩码与泄露质量保证、599条人工辅助质量控制行。采用匹配真实对照诊断方法，评估三种完整外部基线（TruFor、MVSS-Net、HiFi-Net）在固定阈值下的误报率。

### 主要贡献
1. 提出了首个公开的、基于真实数据锚定的背景操作检测与定位基准BG-REAL。
2. 提供了完整的构建流程、评估协议、可直接使用的图表和复现文档。
3. 通过匹配真实对照诊断，发现基线模型存在重编码伪影导致的共同捷径风险（误报率0.57至1.00），而非某一特定模型的问题。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。
理由：该工作专注于图像取证中一个特定且实用的子问题——背景操作，并提供了真实的基准数据集和诊断结果，对从事图像篡改检测、特别是背景相关研究的学者有直接参考价值。但论文尚未提出新的检测算法，且摘要未展示在背景操作场景下的具体性能提升，因此优先级适中。

</details>

<details>
<summary>Abstract</summary>

Background manipulation is a practical but under-specified image-forensics setting: the manipulated evidence can sit outside the salient foreground object, while many evaluations emphasize object-centric copy-move, splicing, or generic synthetic edits. We introduce BG-REAL, a public real-data anchored benchmark package for background manipulation detection and localization. The current release is built from Open Images V7 instance-segmentation sources and contains 7,000 processed samples over 1,200 source groups, including 6,000 public-data anchored samples and 1,000 synthetic control samples. BG-REAL covers six edit families, matched authentic controls, source-group splits, mask and leakage QA, 599 human-assisted quality-control rows, three completed external baselines (TruFor, MVSS-Net, and HiFi-Net), and five-seed model evaluation. Beyond aggregate accuracy, we use matched-authentic-control diagnostics to measure how often baselines misclassify re-encoded authentic images as manipulated at a threshold fixed on held-out validation data; false-positive rates range from 0.57 (TruFor, the lowest) to 1.00 (several weak or mask-informed baselines), indicating that re-encoding artifacts are a shared shortcut risk across baselines rather than a problem specific to any one model. The release provides the construction pipeline, evaluation protocol, paper-ready figures, and reproduction documentation. We frame BG-REAL as a background-manipulation-focused complement to general image-manipulation-localization benchmarks, not as a fully real-only or general-purpose benchmark.

</details>

#### 2026-07-28 - DVPSFormer: Efficient Online Depth-aware Video Panoptic Segmentation for Autonomous Driving

**Authors:** Yung-Hsu Yang, Luigi Piccinelli, Siyuan Li, Mattia Segu, Lei Ke, Martin Danelljan, Yuqian Fu, Zuria Bauer, Fisher Yu, Hermann Blum, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2607.26165) - [pdf](https://arxiv.org/pdf/2607.26165)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, rendering, autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DVPSFormer: Efficient Online Depth-aware Video Panoptic Segmentation for Autonomous Driving
- 作者：Yung-Hsu Yang, Luigi Piccinelli, Siyuan Li, Mattia Segu, Lei Ke, Martin Danelljan, Yuqian Fu, Zuria Bauer, Fisher Yu, Hermann Blum, Marc Pollefeys
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2607.26165；PDF：https://arxiv.org/pdf/2607.26165

### 一句话总结
提出一种面向自动驾驶的高效在线深度感知视频全景分割架构DVPSFormer，通过显式场景离散化和在线多数投票机制，在降低延迟的同时在Cityscapes-DVPS和SemKITTI-DVPS基准上达到新SOTA。

### 研究问题
现有深度感知视频全景分割（DVPS）方法依赖多阶段流水线或离线跟踪，计算成本高且不适合实时决策，无法满足自动驾驶对在线、高效4D场景理解的需求。

### 核心思路/方法
1. **显式场景离散化（ESD）**：利用分割查询（segmentation queries）表示前景和背景区域，配合离散到连续（D2C）深度头在单次前向中解码度量深度，紧密耦合语义与几何学习，减少延迟。
2. **在线多数投票机制（OMV）**：利用时间一致性在实例跟踪过程中对分类结果进行修正，提升稳定性。
3. 整体架构为统一在线设计，无需多阶段或离线步骤。

### 主要贡献
- 提出DVPSFormer，首个高效在线的统一架构用于深度感知视频全景分割。
- 设计ESD机制，实现语义与深度学习的紧耦合，显著降低延迟。
- 提出OMV机制，利用时间一致性提升跟踪中的分类效果。
- 在Cityscapes-DVPS和SemKITTI-DVPS基准上取得新SOTA结果。

### 局限性
摘要未提供足够信息，未提及计算资源要求、在极端驾驶场景下的表现、或对标注数据的依赖等具体局限性。

### 阅读优先级
**高**。理由：该论文针对自动驾驶中实时4D场景理解的迫切需求，提出了兼具效率和性能的在线解决方案，并在多个基准上刷新SOTA，方法新颖（ESD和OMV），且提供开源代码和模型，对从事环境感知、机器人导航的从业者和研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Safe autonomous navigation requires a holistic understanding of dynamic environments, necessitating the simultaneous estimation of metric depth, semantic segmentation, and instance trajectories. While depth-aware video panoptic segmentation (DVPS) unifies these tasks, existing approaches often rely on computationally expensive, multi-stage pipelines or offline tracking, rendering them unsuitable for real-time decision-making. To address this, we propose DVPSFormer, a unified online architecture designed for efficient 4D scene understanding. Central to our approach is explicit scene discretization (ESD), a novel mechanism that leverages segmentation queries to represent foreground and background regions, enabling a discrete-to-continuous (D2C) depth head to decode metric depth in a single pass. This tightly couples semantic and geometric learning while significantly reducing latency. Furthermore, we propose an online majority voting (OMV) mechanism that exploits temporal consistency to refine classification during instance tracking. DVPSFormer establishes a new state-of-the-art on the Cityscapes-DVPS and SemKITTI-DVPS benchmarks, offering a streamlined solution for online robotic perception. Code and models are available at https://royyang0714.github.io/DVPSFormer.

</details>

#### 2026-07-28 - S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information

**Authors:** Kaneyoshi Hiratsuka, Benjamin Yen, Ryosuke Kojima
**Links:** [abs](https://arxiv.org/abs/2607.26047) - [pdf](https://arxiv.org/pdf/2607.26047)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information
- 作者：Kaneyoshi Hiratsuka, Benjamin Yen, Ryosuke Kojima
- 出版日期：2026-07-28T17:56:07Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26047

### 一句话总结
本文提出一个将听觉空间信息与视觉特征融合的多模态模仿学习框架S2A2，用于机器人操作任务中的声源定位与识别，并通过仿真和真实机器人实验验证其有效性。

### 研究问题
如何在机器人模仿学习操作任务中，有效利用物体位置、材质及接触/运动引起的声学信息，实现主动声源定位与识别，并完成声学感知驱动的操作目标。

### 核心思路/方法
1. 设计一系列新的“声学感知操作任务”，要求机器人依赖听觉线索（如声音位置、音色）来确定操作目标。
2. 提出多模态模仿学习框架S2A2（Spatial-Spectral Audio Action），该框架将视觉特征与声学空间信息（空间+谱）整合，用于声学感知操作任务。
3. 将ACT、Diffusion Policy、VQ-BeT和π₀等策略集成到S2A2框架中，并通过仿真实验和真实机器人实验进行评估。

### 主要贡献
- 引入了一组新的声学感知操作任务，用于模仿学习，强调机器人通过听觉线索进行主动探索。
- 提出了S2A2框架，该框架能够将视觉特征与声学空间-谱信息进行多模态融合。
- 仿真实验表明，所提方法在同时需要位置和音色信息的任务中效果最佳。
- 真实机器人实验验证了所提任务和框架在真实世界操作中的可行性。

### 局限性
摘要未提供足够信息，无法明确列出本文实验的量化局限性（如失败案例、计算资源需求或任务泛化能力等）。

### 阅读优先级
**中**  
理由：该工作创新性地将听觉空间信息引入机器人操作中的模仿学习，解决了传统方法忽视声音线索的问题，对于多模态机器人学习领域有参考价值。但由于未详细说明方法具体结构、基线对比差异或实验量化结果，目前仅适用于概念验证和领域入门阅读，尚需后续完整论文评估细节。

</details>

<details>
<summary>Abstract</summary>

Acoustic information provides rich cues about object location, material properties, and changes caused by contact or motion. This paper introduces a new set of acoustic-aware manipulation tasks for imitation learning, in which robots must use auditory cues to determine manipulation targets. These tasks require sound source localization and identification for active exploration in robotic manipulation. Also, we propose a multimodal imitation learning framework, Spatial-Spectral Audio Action (S2A2), that integrates visual features with acoustic spatial and acoustic signal information for the acoustic-aware manipulation tasks. We implemented S2A2 models that integrates policies such as ACT, Diffusion Policy, VQ-BeT, and $π_0$, into our framework. Simulation experiments showed that the proposed method is the most effective for tasks requiring both position and timbre. Furthermore, real-robot experiments confirm the applicability of the proposed tasks and framework to real-world manipulation.

</details>

#### 2026-07-28 - Wonder: Video World Model Done Better

**Authors:** Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei
**Links:** [abs](https://arxiv.org/abs/2607.26037) - [pdf](https://arxiv.org/pdf/2607.26037)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wonder: Video World Model Done Better
- 作者：Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei
- 出版日期：2026-07-28T17:45:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26037

### 一句话总结
本文提出一个名为Wonder的通用的视频世界模型，支持实时、可控制摄像头的交互式世界探索，用户可通过移动摄像头在长时程中导航并发现新区域。

### 研究问题
如何构建一个通用的视频世界模型，使其能够实时响应摄像头控制指令，在保持长期连贯性的同时支持用户交互式探索（如移动摄像头、发现和重访区域）。

### 核心思路/方法
1. **摄像头控制**：引入密集坐标场的摄像头条件化方法，通过渲染提供空间对齐的运动和方向线索，使模型直接将摄像头运动视为视觉证据。
2. **记忆机制**：提出高效的基于稀疏注意力的记忆机制，在推理时选择性地关注少量相关上下文标记，不受实际上下文长度限制，实现快速精确的记忆检索。
3. **训练策略**：开发了多种技术来纠正自强制样式的蒸馏流程，提升学生模型对控制信号的遵从性，同时保持教师模型的多样化生成模式和长期记忆能力。

### 主要贡献
- 提出了一个支持实时、长时程、摄像头可控交互的视频世界模型Wonder。
- 设计了基于密集坐标场的摄像头条件化方法和稀疏注意力记忆机制。
- 改进了蒸馏训练流程，平衡了控制信号响应、生成多样性及长期记忆保持。
- 模型能以16 FPS合成多样化的分钟级视频，在长卷中保持连贯的几何、外观和动态。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法涉及视频生成、世界模型、交互控制与长期记忆等前沿交叉领域，且声称实现了实时长时程的可控探索，对机器人仿真、AR/VR及具身智能应用具有潜在重要影响。

</details>

<details>
<summary>Abstract</summary>

We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy. We introduce a novel camera conditioning with a dense coordinate field whose renderings provide spatially aligned motion and orientation cues, allowing the model to interpret camera motion directly as visual evidence. To support fast and precise memory retrieval over a growing generation context, we propose an efficient sparse attention-based memory mechanism, enabling the model to selectively attend to a small set of relevant context tokens at inference time, regardless of actual context length. We further develop several techniques to rectify the self-forcing-style distillation pipeline, improving the student model's ability to respect control signals, as well as maintaining diverse generation modes and long-term memory from the teacher. Together, these components enable Wonder to synthesize diverse, minute-scale videos at 16 FPS while preserving coherent geometry, appearance, and dynamics across long rollouts. Beyond image-to-video generation, Wonder naturally supports video-conditioned generation, allowing existing dynamic scenes to be re-shot in real time.

</details>

#### 2026-07-28 - HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone

**Authors:** Simple AI, :, Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, Yushen Zuo, Ke Rui, Minglei Li, Jinhao Zhang, Zhikang Pan, Xiang Wang, Haoran Jia, Huan Du, Zicheng Zeng, Jun Ma, Guiyu Qin, Di Zhang, Xiaofei Li
**Links:** [abs](https://arxiv.org/abs/2607.25895) - [pdf](https://arxiv.org/pdf/2607.25895)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone
- 作者：Simple AI, :, Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, Yushen Zuo, Ke Rui, Minglei Li, Jinhao Zhang, Zhikang Pan, Xiang Wang, Haoran Jia, Huan Du, Zicheng Zeng, Jun Ma, Guiyu Qin, Di Zhang, Xiaofei Li
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：arxiv.org/abs/2607.25895

### 一句话总结
本文提出HiFi-UMI数据生产系统，通过提升无机器人UMI数据的采集保真度，使得仅用该数据微调的策略能直接部署到真实机器人上，无需任何后训练阶段的真实机器人数据。

### 研究问题
机器人操作策略学习受限于同时具备高保真度和可扩展性的数据匮乏问题：真实遥操作数据精准但成本高、难以规模化；无机器人UMI数据容易采集但保真度低，通常只能用于预训练，仍需少量真实机器人数据作为后训练的“锚点”。本文核心问题是：能否仅通过提高无机器人UMI数据的保真度，完全去除后训练中的真实机器人数据环节。

### 核心思路/方法
本文从四个维度协同设计了一套便携式UMI数据生产系统（HiFi-UMI）以提升数据保真度：
1. **轨迹精度**：采用头戴式离线立体惯性SLAM。
2. **夹爪间相对姿态**：使用原生而非重建的相对姿态估计。
3. **同步性**：利用共享微秒级GPIO触发信号。
4. **视野**：每只手配备两个广角相机，覆盖约200度视野。
该系统在无外部定位基础设施下，可实现3毫米工作空间局部末端执行器精度。基于此系统采集的高保真数据，策略后训练阶段完全使用HiFi-UMI演示数据，无需任何真实机器人轨迹。

### 主要贡献
1. 提出HiFi-UMI数据生产系统，通过提升无机器人UMI数据的保真度，实现了零机器人后训练：仅用HiFi-UMI演示数据微调的策略可直接在真实机器人上部署，并在三个不同架构（视觉-语言-动作族与世界-动作模型族）的基线上，与评估场景内采集的遥操作基线相比，成功率差异仅为-2.5、+3.1和-0.6个百分点。
2. 最强策略在精密插入任务上达到85%成功率，尽管HiFi-UMI轨迹未在该评估场景采集。
3. 在相同语料库上预训练4000小时，将十个未见任务的动作误差降低41%，并使基于StarVLA-QwenPI的真实机器人成功率再提升18.1个百分点。
4. 开源HiFi-UMI-2K数据集：2000小时微秒同步、超宽视角演示数据，每条数据均通过仿真回放自动重建与验证。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：本文针对机器人操作学习的数据瓶颈，提出了一种系统性的数据生产方案，在不依赖昂贵真实机器人数据的情况下实现了高性能策略学习，并提供了大规模开源数据集，对具身智能领域的研究有重要参考价值。实验覆盖多种主流策略架构并报告了量化成功率和动作误差，结果详实。

</details>

<details>
<summary>Abstract</summary>

Learning deployable manipulation policies is bottlenecked by the scarcity of data that is both high-fidelity and scalable. Real-robot teleoperation is accurate but costly to scale; robot-free UMI capture scales readily, and current practice uses the resulting data mainly for pre-training, adding a small real-robot "anchor" at post-training. We ask whether raising the fidelity of robot-free UMI data, rather than shrinking the real-robot fraction, can remove that anchor. We present HiFi-UMI, a portable UMI data-production system co-designed for trajectory accuracy, inter-gripper relative pose, synchronization, and field of view: head-mounted offline stereo-inertial SLAM, native rather than reconstructed relative pose, a shared microsecond GPIO trigger, and two wide-angle cameras per hand covering ~200 degrees. It reaches 3 mm workspace-local end-effector accuracy without external tracking infrastructure. Using this corpus, we demonstrate zero-robot post-training: a policy post-trained solely on HiFi-UMI demonstrations deploys directly on a real robot and matches in-domain teleoperation across three backbones spanning the vision-language-action and world-action-model families, with success-rate differences of -2.5, +3.1, and -0.6 percentage points on StarVLA-QwenPI, OpenPI-pi_0.5, and LingBot-VA; the strongest policy reaches 85% on a precision insertion task, even though the teleoperation baseline is collected in the evaluation scene and no HiFi-UMI trajectory is. Pre-training on 4,000 hours from the same corpus lowers action error on ten unseen tasks by 41% and, on StarVLA-QwenPI, raises real-robot success by a further 18.1 percentage points. We open-source HiFi-UMI-2K, 2,000 hours of microsecond-synchronized, ultra-wide-FoV demonstrations, each automatically reconstructed and validated through simulation replay, as a large-scale, high-fidelity resource for the robot-learning community.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
