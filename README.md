# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：39
- 分类分布：
  - Neural Scene Representations & Rendering: 14
  - 3D Reconstruction & Multi-view Geometry: 12
  - Embodied / Robotics / AR Applications: 9
  - Dynamic / 4D Reconstruction: 2
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **生成式重建从“能生成”转向“可查询、可评测、可控制”**
   - 前馈生成式重建开始强调下游可用性：LucidLyra 把几何、外观、开放词汇语义与实例线索统一到同一次前馈推断中，目标是让生成场景可直接被机器人和物理 AI 查询。
   - 评测侧同步出现反思：Aligning Misaligned Benchmarks 指出单视图新视角合成的评测因参考系与真值位姿对齐方式不同而不公平，并改用传统 2D-2D/2D-3D 匹配对齐三维重建、只在共视区域评测。
   - COGS 则针对 3DGS 感知建立属性诊断基准，追问“哪些高斯属性真正有用”，说明社区开始从“堆属性”转向“理解属性”。

2. **4D/动态场景建模开始纳入声音、语义与稠密感知等多模态维度**
   - SonoWorld4D 把“单视频→可探索 4D 视听场景”定义为新任务，在视觉之外补上空间音频与声源运动。
   - GenSight 把未来视频生成与深度、分割、光流等稠密 4D 感知统一在同一视频扩散 Transformer 中。
   - 两者共同指向：世界模型不再只追求画面逼真，而要求几何、语义、运动乃至听觉结构的一致。

3. **3DGS 的密度控制与效率成为独立且活跃的技术战场**
   - ACD-GS 用二阶深度响应对克隆/分裂做非对称调控，抑制冗余高斯。
   - BudSplat 在有限基元预算下做重要性评分与质量感知剪枝，面向密集多视角输入的渲染效率瓶颈。
   - GradSplat 在前向传播内部用学习到的梯度步骤自细化高斯形状，缩小前馈预测与逐场景优化之间的差距。
   - 三条路线分别从“何时致密”“保留多少”“如何自我修正”切入，说明 3DGS 正从表示创新转向训练动力学与预算约束下的工程化。

4. **几何基础模型与扩散先验加速向“退化/极端/稀疏观测”场景渗透**
   - MLLM-GS 用冻结 MLLM 视觉先验增强退化视图，并用轻量校正网络抑制像素错位与颜色偏差。
   - RoSAMDepth 借 SAM 的对象级先验改善自监督深度在不利条件下的对象内偏离与模糊。
   - 极端稀疏视角 CT 论文在“训练稀疏、推理稀疏”设定下学习姿态感知扩散先验。
   - 共性技术路线是：冻结大模型提供先验，轻量模块负责对齐/校正/物理一致性，避免为每种退化单独训练模型。

5. **机器人/具身应用侧的论文更强调“部署约束”与“决策层指标”**
   - SKiD-SLAM 以行星任务的通信与计算预算为约束选择模块，并完成模拟场址实地部署。
   - DEED 用演示扩展与执行设计把预训练 VLA 策略适配到细粒度操作任务，强调逆运动学、夹爪映射与闭环重规划。
   - 单目 RGB 人体跟踪论文提出决策级 Shapley 归因，把“安全规则”与“感知误差”对停止/继续决策的贡献分开。
   - 月球单目深度评估则直接检验分布外泛化。整体看，机器人方向更关注资源预算、决策后果与真实部署验证，而非单纯刷精度。

#### 技术路线观察

- **几何基础模型方向**：PhysInsert 把 VGGT 几何流与图像、文本流耦合，用于参考物体插入的位姿与光照适配；LucidLyra 从相机控制视频扩散模型与冻结 2D 基础模型蒸馏几何与语义。两者都体现“几何先验 + 多模态条件”的融合思路，但前者面向编辑式插入，后者面向前馈场景理解与查询。
- **3D/4D 重建方向**：SonoWorld4D 与 GenSight 都把扩散模型作为时空生成骨干，区别在于前者强调视听一致与声场物理性，后者强调生成与稠密感知共享同一预测空间。极端稀疏 CT 论文则展示扩散先验在医学断层重建中的“训练稀疏”变体，说明扩散先验正从自然图像扩展到物理成像。
- **神经场景表示方向**：3DGS 相关论文形成明显分层——ACD-GS 改致密化判据，BudSplat 改前馈预算控制，GradSplat 改前向自细化，COGS 改感知评测，GOFish 改鱼眼全视场与网格提取。技术侧重点从“表示能力”转向“训练效率、几何准确性、下游可用性与传感器适配”。
- **机器人/AR 应用方向**：SKiD-SLAM、DEED、粒子滤波定位、单目人体跟踪决策评估、KITScenes Aerial 分别对应多机 SLAM、操作策略适配、无外部定位、安全决策评测与空中辅助驾驶基准。路线差异大，但共同点是评测指标向任务后果靠拢，而非仅用几何或渲染精度。
- **评测与数据侧**：今日多篇论文以数据集/基准为主要贡献（KITScenes Aerial、COGS、Insert World、PhysInsert-Bench、Aligning Misaligned Benchmarks），说明该领域正处在“方法快于评测”的阶段，基准建设本身成为趋势信号。

#### 值得优先阅读的论文

1. **LucidLyra（2610.40495）**：把前馈生成式重建与开放词汇语义、实例线索统一，直接对应机器人与物理 AI 对“可查询生成场景”的需求。若关注生成式重建的下游落地，这是今日最直接的一篇。
2. **GenSight（2610.39232）**：统一视频生成与稠密 4D 感知，且共享 DiT 骨干与预测空间，代表具身世界模型“生成即感知”的路线。对理解 4D 感知与视频扩散的耦合方式有参考价值。
3. **ACD-GS（2610.39399）**：从二阶深度响应重新定义 3DGS 致密化判据，思路清晰、问题明确。若关注 3DGS 训练动力学与几何质量，这篇比单纯压缩类工作更具方法启发性。
4. **SonoWorld4D（2610.40640）**：提出新任务 Video-to-4DAVScene，把声音纳入 4D 场景生成。虽然任务较新、成熟度待验证，但“视听同步的 4D 场景”是较少被覆盖的方向，适合作为选题参考。
5. **Aligning Misaligned Benchmarks（2610.38349）**：不提出新生成方法，而是指出单视图新视角合成评测的系统性偏差。对正在做 NVS 实验或复现对比的人，这篇可能直接影响实验设计与结论可信度。

#### 可能的研究机会

- **生成式重建的“可查询性”标准化**：LucidLyra 展示前馈语义查询，但今日尚无统一指标衡量生成场景的语义/实例查询质量。可跟进“生成式 3D 场景的下游任务基准”，把重建、分割、抓取或导航成功率纳入同一评测。
- **4D 视听场景的物理一致性验证**：SonoWorld4D 提出空间音频渲染，但摘要未给出声场物理正确性的量化协议。可探索将声学仿真、材质属性与视觉几何联合约束的评测方法。
- **3DGS 致密化与预算控制的联合设计**：ACD-GS 管“何时分裂”，BudSplat 管“保留多少”，GradSplat 管“如何修正”。三者目前独立，存在组合空间：例如在有限基元预算下用曲率先验指导剪枝，或用前向梯度细化后的形状反馈致密化决策。
- **冻结大模型先验的轻量对齐模块复用**：MLLM-GS 的轻量校正网络、RoSAMDepth 的对象级可靠性估计、PhysInsert 的几何引导适配，都在解决“大模型输出与三维一致性之间的错位”。可提炼通用的跨先验对齐范式，减少

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-03T15:06:14-05:00
**Total number of papers:** 55
**Number of papers added in the latest update:** 36
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

### 2026-11

#### 2026-11-01 - Lie Routing Vision Language Models for View-Robust 3D Understanding

**Authors:** Jingjun Yi, Chen Hu, Qi Bi, Hao Zheng, Huimin Huang, Yongkang, Wei Ji, Yawen Huang, Xian Wu, Yefeng Zheng
**Links:** [abs](https://arxiv.org/abs/2611.02306) - [pdf](https://arxiv.org/pdf/2611.02306)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, scene understanding

<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) have made substantial progress in 3D scene understanding from multi-view RGB observations. Yet a fixed object and query can elicit inconsistent target-related responses across camera viewpoints, a phenomenon we characterize as viewpoint-induced semantic drift. We introduce LieVLM, a Lie routing framework for view-robust 3D understanding. Motivated by the rotational component of viewpoint change, Lie routing adapts visual representations by applying local $\mathrm{SO}(3)$ transformations to projected features within learned three-dimensional subspaces. Geometry tokens extracted by VGGT predict local rotation parameters and channel-wise routing coefficients. A closed-form Padé--Cayley map transforms projected visual features, whose identity-relative corrections are projected back and gated into the original visual and geometry features. This design retains the pretrained semantic and direct spatial context while learning view-dependent feature adjustments. Experiments on 3D captioning, grounding, detection, and spatial reasoning show consistent improvements over additive fusion across training scales and backbones. Controlled ablations examine the roles of geometric conditioning and transformation structure. Viewpoint analyses further reveal systematic variation in the predicted routing states alongside more localized target responses and stronger task performance across viewpoint changes.

</details>

### 2026-10

#### 2026-10-29 - PhysInsert: Physically Plausible Object Insertion with Geometric Priors and Bidirectional Object-Scene Interactions

**Authors:** Yue Gong, Le Zhang, Rui Chen, Song Chang, Xiaochao Qu, Luoqi Liu, Ting Liu, Yebin Liu
**Links:** [abs](https://arxiv.org/abs/2610.40453) - [pdf](https://arxiv.org/pdf/2610.40453)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PhysInsert: Physically Plausible Object Insertion with Geometric Priors and Bidirectional Object-Scene Interactions
- 作者：Yue Gong, Le Zhang, Rui Chen, Song Chang, Xiaochao Qu, Luoqi Liu, Ting Liu, Yebin Liu
- 出版日期：2026-10-29T17:01:13Z
- 分类：主分类为 Geometry Foundation Models；次分类摘要未提供。
- 链接：摘要页 https://arxiv.org/abs/2610.40453；PDF https://arxiv.org/pdf/2610.40453

### 一句话总结
PhysInsert 提出一个基于参考图像、联合调整物体与周围场景的物理合理物体插入框架，并通过新数据集、几何引导适配、2D 空间监督和新基准来提升位姿与光照适配及双向物体—场景交互。

### 研究问题
论文关注参考图像驱动的物体插入任务，要求插入结果在物理上合理，并同时适配物体的位姿与光照以及周围场景。摘要指出，现有方法常依赖掩码输入、生成式配对数据，或视角变化有限的训练配对，导致位姿与光照适配以及双向物体—场景交互约束不足。

### 核心思路/方法
- 构建 Insert World 数据集：使用 Blender 渲染严格对齐的反事实配对，并包含跨视角与光照条件的物体参考。
- 提出 Geometry-Guided Adaptation：将 VGGT 几何流与图像流、文本流结合，在目标场景特征监督下引导空间一致的插入。
- 引入 2D Object-Scene Spatial Supervision：联合监督物体占据与环境变化，并通过图像—文本注意力将空间指令 grounding 到物体区域。
- 提出 PhysInsert-Bench：包含跨环境和跨视角案例，要求模型进行光照与位姿适配，而不仅是外观复制。

### 主要贡献
- 指出现有物体插入方法在位姿与光照适配、双向物体—场景交互约束方面的不足。
- 构建 Insert World 数据集，提供严格对齐的 Blender 渲染反事实配对及跨视角、光照条件的物体参考。
- 提出结合几何先验的 Geometry-Guided Adaptation 和 2D Object-Scene Spatial Supervision。
- 提出 PhysInsert-Bench，用于评估跨环境与跨视角下需要光照和位姿适配的插入能力。
- 摘要称在 PhysInsert-Bench 和 DreamBooth 上实验显示图像保真度提升；用户研究显示放置更准确，光照整合、透视和位姿合理性更好。

### 局限性
摘要未提供足够信息。摘要未给出具体实验数值、失败案例分析、计算成本、数据集规模与多样性细节，也未说明方法在更广泛场景或真实复杂环境中的泛化边界。

### 阅读优先级
中。理由：该论文涉及参考驱动的物体插入、几何先验和物体—场景双向交互，并配套新数据集与基准，问题定义和方法组合较明确；但摘要仅给出高层方法与有限实验结果描述，是否值得深入阅读需结合全文的实验细节、基线对比和局限性分析再判断。

</details>

<details>
<summary>Abstract</summary>

We present PhysInsert, a framework for physically plausible reference-based object insertion that jointly adapts objects and their surrounding scenes. Existing methods often rely on masked inputs, generation-based pairs, or training pairs with limited viewpoint variation, leaving pose and illumination adaptation and bidirectional object-scene interactions insufficiently constrained. We construct the Insert World dataset with strictly aligned Blender-rendered counterfactual pairs and object references across viewpoints and lighting conditions. Building on these data, Geometry-Guided Adaptation couples a VGGT geometry stream with image and text streams under target-scene feature supervision to guide spatially consistent insertion. Complementary 2D Object-Scene Spatial Supervision jointly supervises object occupancy and environmental changes while grounding spatial instructions in object regions through image-text attention. We introduce PhysInsert-Bench with dedicated cross-environment and cross-view cases requiring illumination and pose adaptation beyond appearance copying. Experiments on PhysInsert-Bench and DreamBooth demonstrate improved image fidelity; a user study further shows more accurate placement and improved lighting integration, perspective, and pose plausibility.

</details>

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-02 - HIVE-Diff: High Frame Rate HDR Video Reconstruction from a Single LDR Frame and Events

**Authors:** Caixin Wang, Qingrui Wang, Jie Zhang, Ralph Etienne-Cummings
**Links:** [abs](https://arxiv.org/abs/2611.03465) - [pdf](https://arxiv.org/pdf/2611.03465)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction, autonomous driving

<details>
<summary>Abstract</summary>

High frame rate HDR video is important in applications such as autonomous driving and scientific imaging, where rapid motion and extreme illumination often occur simultaneously. Conventional frame cameras face a trade-off between temporal resolution and dynamic range, while event cameras provide complementary high-speed brightness-change measurements over a wide illumination range. These properties have motivated event-based HDR reconstruction, with existing methods broadly following event-only and hybrid event-frame paradigms. Event-only HDR reconstruction, however, suffers from brightness and color drift due to the lack of absolute intensity references. Hybrid event-frame methods alleviate this ambiguity using low-dynamic-range (LDR) frames as anchors, but most perform one-to-one HDR reconstruction at available LDR timestamps. In this work, we investigate single-reference HDR temporal expansion, reconstructing N HDR frames from one LDR reference and events instead of N aligned LDR observations. We develop HIVE-Diff, an event-conditioned video diffusion framework that decomposes the task into event-guided temporal generation and HDR content completion. Because paired real HDR-event data are scarce, we train on synthetic data and adapt the model to real event domains using LDR-event sequences as proxy supervision with teacher-student distillation. Experiments on synthetic and multiple real-world datasets demonstrate strong reconstruction quality and robust real-data adaptation.

</details>

#### 2026-11-02 - The DynaCell Evaluation Suite for Dynamic 3D Virtual Staining of Live Cells

**Authors:** Alexandr A. Kalinin, Dihan Zheng, Taylla Milena Theodoro, Ivan Ivanov, Eduardo Hirata-Miyasaki, See-Chi Lee, Aofei Liu, Sricharan Reddy Varra, Talon Chandler, Soorya Pradeep, Chad Liu, Manuel D. Leonetti, Carolina Arias, Bo Huang, Shalin B. Mehta
**Links:** [abs](https://arxiv.org/abs/2611.02324) - [pdf](https://arxiv.org/pdf/2611.02324)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D, localization

<details>
<summary>Abstract</summary>

Understanding how cells respond to perturbations over time is central to cell biology and drug discovery. Live-cell imaging captures the dynamics of perturbation-induced phenotypes in individual cells. While fluorescence imaging can visualize specific molecular phenotypes, labeling and repeated illumination often affect cell health. Virtual staining offers an alternative by predicting these fluorescence images from images acquired without fluorescent labels. Although many virtual staining models have been developed, their performance on volumetric time-lapse data remains poorly characterized. We address this gap with an evaluation suite for 3D time-lapse virtual staining of live cells. The suite combines paired 3D time-lapse images acquired with and without fluorescent labels, a set of baseline models, and three metric tiers measuring pixel-level fidelity, organelle segmentation performance, and single-cell phenotype similarity. Using this evaluation suite, we study metric and model behavior across 3 cell types, 2 microscopes, 4 organelles, and 3 perturbation states. We find that regression baselines better predict the spatial localization of target organelles, whereas the generative baseline better captures the distribution of phenotypes across cells. These differences expose trade-offs between structural and phenotypic fidelity that are obscured by single-metric evaluation and suggest how virtual staining models can be developed for diverse downstream tasks such as localization, segmentation, tracking, and phenotypic profiling. We release the curated datasets, baseline checkpoints, and evaluation code as part of DynaCell, a broader framework for image-based profiling of cell-state dynamics.

</details>

#### 2026-11-01 - 4D Triangle Splatting Reconstruction of Dynamic Endoscopic Scenes from Monocular Videos

**Authors:** Laura Salort-Benejam, Stamatia Giannarou, Antonio Agudo
**Links:** [abs](https://arxiv.org/abs/2611.02034) - [pdf](https://arxiv.org/pdf/2611.02034)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic reconstruction, scene reconstruction, splatting

<details>
<summary>Abstract</summary>

Robust 4D reconstruction of deformable endoscopic scenes from monocular videos remains challenging due to non-rigid tissue deformation, illumination changes, occlusions, and unknown camera trajectories. Reliable dynamic reconstruction of endoscopies could significantly enhance visualization, diagnostic accuracy and intraoperative guidance of minimally invasive procedures. We propose SurgicalTS, a self-supervised triangle-splatting framework for dynamic endoscopic scene reconstruction from static monocular cameras. The scene is represented by a canonical set of triangles jointly optimized with a deformation network. We introduce a quaternion-based deformation model, an improved color parametrization, spatio-temporal priors, and a redefined initialization strategy that improves completeness under occlusions. Extensive evaluation on challenging in-vivo endoscopy videos from diverse procedures shows that SurgicalTS successfully models soft-tissue deformations and tool-tissue interactions over time, while consistently outperforming state-of-the-art methods. Our method also reduces training times while maintaining competitive geometric and photometric accuracy results, highlighting the effectiveness of quaternion-based deformation modelling with physical consistency for robust and efficient 4D reconstruction of endoscopic scenes.

</details>

### 2026-10

#### 2026-10-29 - SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization

**Authors:** Derong Jin, Xiyi Chen, Ming C. Lin, Ruohan Gao
**Links:** [abs](https://arxiv.org/abs/2610.40640) - [pdf](https://arxiv.org/pdf/2610.40640)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 4D, motion trajectories, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization
- 作者：Derong Jin, Xiyi Chen, Ming C. Lin, Ruohan Gao
- 出版日期：2026-10-29T17:58:45Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要 https://arxiv.org/abs/2610.40640 ；PDF https://arxiv.org/pdf/2610.40640

### 一句话总结
该论文提出从单段单目视频生成可探索、随时间变化的 4D 视听场景的任务与 SonoWorld4D 框架，重点补足以往 4D 场景生成中未被建模的声音维度。

### 研究问题
论文关注的是：如何从极少的输入（单段单目视频）生成动态 4D 场景，并且把与动态对象和事件内在耦合的声音纳入场景建模。摘要指出，已有视觉场景生成工作虽已从静态 3D 扩展到动态 4D，但声音在先前工作中“基本未被建模”。

### 核心思路/方法
摘要给出的方法要点包括：
1. 定义新任务 Video-to-4DAVScene：把一段视频转化为可探索、时变的 4D 视听场景；
2. 给定单目视频，生成 360 度静态背景；
3. 重建动态、发声前景对象的显式运动轨迹；
4. 通过“双空间音频扩散同步”合成跨多个声源、物理 grounded 且一致的声音场；
5. 生成的 4D 场景支持实时新视角视觉渲染与空间音频渲染。

### 主要贡献
摘要明确陈述的贡献为：
1. 提出新任务 Video-to-4DAVScene，将单视频转为可探索的时变 4D 视听场景；
2. 提出 SonoWorld4D 框架，联合生成 360 度静态背景、动态发声前景对象的显式运动轨迹，以及多声源一致的声音场；
3. 通过双空间音频扩散同步实现物理 grounded 的声音合成；
4. 在真实世界动态场景上的评估与用户研究表明，该方法生成的 4D 视听场景具有感知上真实、与场景几何和视觉内容一致的空间音频。

### 局限性
- 摘要未提供足够信息说明方法在何种输入条件下会失败，或对视频质量、场景类型、声源类型有何限制。
- 摘要未提供足够信息说明评估规模、定量指标、用户研究细节及与基线方法的完整比较。
- 摘要未提供足够信息说明计算开销、实时渲染的具体硬件条件或运行效率。
- 摘要未提供足够信息说明“物理 grounded”的具体判定标准与验证方式。

### 阅读优先级
高。理由：该论文提出明确的新任务（Video-to-4DAVScene），并针对 4D 场景生成中声音建模缺失的问题给出框架；摘要同时声称支持实时新视角视觉与空间音频渲染，并有真实场景评估与用户研究。对于关注动态 4D 重建、视听场景生成与空间音频的研究方向，具有直接相关性。但摘要未给出定量结果与实现细节，需阅读全文进一步核验。

</details>

<details>
<summary>Abstract</summary>

Recent progress in visual scene generation has extended beyond static 3D scenes toward the more challenging problem of generating dynamic 4D scenes from minimal input. However, sound, despite being intrinsically coupled with dynamic objects and events, remains largely unmodeled in prior work. We introduce Video-to-4DAVScene, a new task that turns a video into an explorable, time-varying 4D audio-visual scene, and present the SonoWorld4D framework for this task. Given a monocular video, our method generates a 360 static background, reconstructs explicit motion trajectories of dynamic, sound-emitting foreground objects, and synthesizes a physically-grounded sound field consistent across multiple sources through dual-space audio diffusion synchronization. The resulting 4D scene supports real-time novel-view visual and spatial audio rendering. Evaluation on real-world dynamic scenes and a user study demonstrates SonoWorld4D generates 4D audio-visual scenes with perceptually realistic, physically grounded spatial audio consistent with scene geometry and visual content.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-02 - ReVA-HPE: Relative 6DoF Head Pose Estimation with Synthetic Pose Supervision and Personalized Virtual Anchors

**Authors:** Vasiliki Vasileiou, Panagiotis P. Filntisis, Petros Maragos, Kostas Daniilidis
**Links:** [abs](https://arxiv.org/abs/2611.03283) - [pdf](https://arxiv.org/pdf/2611.03283)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Monocular head pose estimation is usually formulated as absolute regression from a single face crop, yet many applications observe the same person over time and can supply an explicit anchor image. Recently, relative head pose estimation was proposed, which casts the problem as estimation of the relative geometric change between an anchor and a query image. However, existing methods still require the anchor image pose to be known at inference, significantly limiting their practical use. We first extend relative head pose estimation to full 6DoF by additionally predicting a depth-normalized relative translation, which composes with the anchor to recover metric query pose in the camera frame. To eliminate the need for a ground-truth anchor pose, we reconstruct a personalized avatar from a single unlabeled enrollment image and render a bank of virtual anchors with known poses. The bank provides robust rotation hypotheses through multi-anchor consensus, while the real enrollment image serves as the real anchor in the translation branch via landmark PnP. We also introduce an efficient variant that amortizes the bank cost once at enrollment, after which each query requires a single real-to-real relative prediction, with limited accuracy sacrifice. The relative pose estimator is trained exclusively on synthetic face renderings, without real pose supervision, pseudo-labels, domain adaptation, or fine-tuning on the evaluation sets. On real 6DoF benchmarks, ReVA-HPE achieves state-of-the-art rotation accuracy on BIWI and, given a near-frontal enrollment image, on FaMoS, while remaining competitive in metric translation despite relying solely on synthetic pose supervision. Project page and code: https://vasilikivas.github.io/ReVA-HPE/

</details>

#### 2026-11-02 - A Tightly Coupled Magnetic-Inertial SLAM System for Field Robots

**Authors:** Chuan Huang, Tongxing Peng
**Links:** [abs](https://arxiv.org/abs/2611.03106) - [pdf](https://arxiv.org/pdf/2611.03106)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>Abstract</summary>

Field robots operating in mines, tunnels, and disaster areas require reliable localization despite GNSS denial and degraded camera and LiDAR measurements caused by dust, smoke, or poor illumination. Missions involving both ground and aerial robots further motivate complementary sensing modalities that do not depend on visibility, preinstalled infrastructure, or wheel contact. This letter presents MISLAM, a tightly coupled magnetic-inertial simultaneous localization and mapping system using an IMU and a nine-magnetometer array, without relying on external odometry or platform-specific motion assumptions. The system combines the inertial navigation model with local polynomial magnetic-field models for short-term motion estimation and a global Gaussian process model for drift correction using an error-state Kalman filter. Offline evaluation on three indoor datasets collected with a handheld rig shows reductions in total endpoint closure error of 45.7% - 78.0% relative to magnetic-inertial odometry. Under poor illumination, MISLAM maintains tracking after visual-inertial odometry fails, achieving a horizontal closure error of 0.332 m, although vertical drift remains a limitation. These results support magnetic-inertial SLAM as a complementary localization modality for robotic sensor suites operating under degraded visual conditions.

</details>

#### 2026-11-02 - MuCHMDPoser: Multiview RGB-Camera Full-Body Pose Tracking for Virtual Reality

**Authors:** Antoine Maiorca, George Fletcher, Thierry Ravet, Thierry Dutoit
**Links:** [abs](https://arxiv.org/abs/2611.03062) - [pdf](https://arxiv.org/pdf/2611.03062)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, camera calibration, VR, virtual reality

<details>
<summary>Abstract</summary>

Accurate full-body tracking in Virtual Reality (VR) is heavily underconstrained when relying solely on consumer-grade sparse sensors, such as Head-Mounted Displays (HMDs) and handheld controllers. Indeed, the self-avatar full-body pose must be inferred based on the 3 available upper-body joints tracked by these devices. This leads to significant tracking error, especially in lower-body pose. To overcome this issue, we propose to extend the tracking setup with external multiview RGB cameras. We show that integrating RGB-based pose estimation this framework is able to significantly decrease lower-body tracking errors, even under common artifacts in RGB-based estimates. Additionally, we evaluate a only-once HMD-camera calibration procedure that does not require any physical markers. We finally propose an implementation of the overall framework, achieving an end-to-end animation at 60 FPS on a Nvidia RTX3080 GPU. Codes are available at https://github.com/antmaio/MuCHMDPoser.

</details>

#### 2026-11-02 - GPU-Native Real-Time Textured Mesh Reconstruction with Seam-Aware Multi-View Radiometric Correction

**Authors:** Hiroyuki Sato
**Links:** [abs](https://arxiv.org/abs/2611.03033) - [pdf](https://arxiv.org/pdf/2611.03033)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction, rendering, mapping

<details>
<summary>Abstract</summary>

We present a GPU-native volumetric-video system for real-time reconstruction of graphics-compatible textured triangle meshes from multiple RGB-D sensors. Existing TSDF systems accelerate fusion and mesh extraction, but extending them to per-frame textured meshing adds CPU mesh processing, CPU-side texturing work, or extra CPU-GPU transfers between stages. After input staging, our method keeps the reconstruction and texturing stages (TSDF fusion, Marching Cubes, connected-component noise removal, view-based texture mapping, inpainting, and radiometric seam correction) resident on the GPU; no intermediate mesh or image data returns to the host between these stages. A fixed-size-array representation of mesh topology gives constant-time neighbor access on the GPU and makes the downstream mesh-level operations data-parallel. Because we texture each face from a single camera, exposure seams that vary smoothly across each image remain; we estimate a per-camera low-frequency gain field and bake it into the atlas on the GPU. On the CMU Panoptic dataset, our method is faster than the baselines at every tested voxel resolution and number of sensors, achieves peak speedups of more than an order of magnitude over CUDA-accelerated nvblox and CPU-based Open3D, and approaches an offline textured-meshing baseline in perceptual re-rendering quality.

</details>

#### 2026-11-02 - Comprehensive Evaluation of Monocular and Multi-view 3D Human Pose Estimation Models for Fitness Exercise Analysis

**Authors:** Néstor Ortega, Agustín Salgado, Javier Sánchez
**Links:** [abs](https://arxiv.org/abs/2611.02929) - [pdf](https://arxiv.org/pdf/2611.02929)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Three-dimensional human pose estimation has become a fundamental component of computer vision systems for sports analytics, rehabilitation, and motion understanding. Although recent deep learning approaches have achieved remarkable accuracy on standard benchmarks, their performance under realistic sports scenarios remains insufficiently studied. Furthermore, the trade-offs between recent monocular and multi-view approaches, as well as the benefits of post-processing techniques for improving temporal consistency, have not been systematically evaluated on fitness-oriented datasets. This paper evaluates recent state-of-the-art 3D human pose estimation methods on Fit3D, a dataset of synchronized multi-view recordings of a wide variety of fitness exercises with accurate ground-truth annotations. We study two recent monocular lifting approaches, TCPFormer and PoseMamba-L, and a multi-view model, MVGFormer, under a unified evaluation protocol. To investigate the influence of the input data, monocular methods are evaluated using ground-truth keypoints and detections generated by recent 2D pose estimators, RTMPose and YOLO-Pose. Additionally, we analyze the effectiveness of three temporal filters for reducing prediction jitter while preserving motion dynamics. Experimental results provide a detailed comparison of accuracy, temporal consistency, and robustness to imperfect 2D detections across the evaluated methods. Our analysis highlights the impact of detector quality on lifting-based approaches, compares transformer- and state-space-based temporal architectures, and discusses the practical trade-offs between monocular and multi-view systems for fitness motion analysis. Our results show that 2D detection quality, temporal modeling, and post-processing must be considered jointly in pose estimation pipelines for exercise analysis.

</details>

#### 2026-11-02 - AnchorHEC: Targetless Hand-Eye Calibration of Wrist and Fixed Cameras

**Authors:** Guebin Hwang, Taeyeop Lee, Yeonseo Lee, Hyosup Shin, Sungho Jo
**Links:** [abs](https://arxiv.org/abs/2611.02884) - [pdf](https://arxiv.org/pdf/2611.02884)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, bundle adjustment, simulation

<details>
<summary>Abstract</summary>

Recent robot systems combine wrist and fixed cameras, requiring camera-to-robot transforms for both. Most hand-eye calibration methods rely on targets or robot-body observations. Scene-based methods using 3D reconstruction require neither but address only wrist cameras. We introduce AnchorHEC, a targetless hand-eye calibration framework for wrist and fixed cameras in a single procedure using RGB images, forward kinematics (FK), and known camera intrinsics. We initialize both camera types using FK and a shared 3D foundation model reconstruction. FK-constrained wrist-image bundle adjustment reduces the impact of reconstructed pose and scale errors. If this refinement fails or retains too few inliers, we relax the constraints on potentially inaccurate FK poses and lens parameters. We use the refined wrist transform and FK to triangulate metric points and estimate fixed-camera poses. Across three backbones, calibration errors in simulation decrease by 86.4% in translation and 71.6% in rotation, averaged over both camera types, relative to reconstruction-based baselines. We also validate AnchorHEC on a physical robot. Project page: https://hwanggb.github.io/AnchorHEC/

</details>

#### 2026-11-02 - OctreeSplat: Hierarchical Octree-Guided Feed-Forward Gaussian Splatting

**Authors:** Yibin Zhao, Yihan Pan, Wenli Yang, Jun Nan, Jianjun Yi
**Links:** [abs](https://arxiv.org/abs/2611.02658) - [pdf](https://arxiv.org/pdf/2611.02658)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has shown considerable potential for novel view synthesis (NVS) and 3D reconstruction. Feed-forward methods avoid costly per-scene optimization, but fixed image or spatial resolutions limit their ability to allocate primitives according to local complexity. We present OctreeSplat, a hierarchical octree-guided feed-forward Gaussian splatting. OctreeSplat extracts multi-view features and geometric priors from a frozen visual foundation model (VFM), constructs a hierarchical octree, and predicts densification scores. The resulting representation allocates Gaussian primitives at spatially varying densities according to local complexity. Stochastic solids volume rendering improves depth rendering, strengthens geometric supervision, and supports surface reconstruction. When camera parameters are available, an optional test-time optimization (TTO) module improves agreement between predicted and ground-truth parameters. Training updates only 76 million additional parameters and requires 35 GPU-hours. Experiments on Replica, TUM, Tanks and Temples, and DTU demonstrate competitive RGB view synthesis, depth synthesis, and surface reconstruction. OctreeSplat reduces the number of Gaussian primitives while maintaining high reconstruction quality.

</details>

#### 2026-11-01 - Depth Anyviewpoint? Evaluating Monocular Depth Over Viewpoint Sequences

**Authors:** Theo Rode, Rui Zhang, Ryan Aubrey, Olivia Li, Jessica Huang, Liv Chu, Healani Dowd, Calden Wloka
**Links:** [abs](https://arxiv.org/abs/2611.02203) - [pdf](https://arxiv.org/pdf/2611.02203)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, structure from motion, depth estimation, monocular depth

<details>
<summary>Abstract</summary>

Monocular depth estimation aims to predict depth maps from single RGB images (forgoing the need for stereo camera pairs) and has seen impressive leaps in performance in recent work due to the introduction of affine-invariant losses and the use of foundation model features. These monocular depth models predict affine-invariant depth, which describes the relative positions of objects in the scene instead of absolute depth. While these models demonstrate strong performance on single image benchmarks and qualitatively consistent predictions in video, their effectiveness at preserving consistent spatial structure has been less thoroughly explored. Many potential real-world applications, such as handling video streams as input, rely on coherent three dimensional consistency in scenes. Further, anchoring relative depth predictions to a metric reference for a given scene is a key challenge for applying monocular depth models to real-world situations. We develop a novel evaluation protocol for monocular depth models using video sequences with moving camera positions to test the consistency of prediction across variation in viewpoint. We demonstrate this methodology over diverse, real-world video sequences where we are able to anchor depth model output to metric depth values using structure from motion. Our work demonstrates open challenges in the development of broadly applicable monocular depth foundation models, particularly with their ability to provide temporal consistency over long time frames. We also identify challenges in the straightforward adoption of structure-from-motion as a metric grounding tool for monocular depth estimation models.

</details>

#### 2026-11-01 - UniGS-SLAM: Monocular Gaussian SLAM with Enhanced Geometry and Open-Vocabulary Semantics

**Authors:** Xingyuan Ding, Sicheng Yu, Kaiyong Zhao, Hao Wang
**Links:** [abs](https://arxiv.org/abs/2611.02051) - [pdf](https://arxiv.org/pdf/2611.02051)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, pose estimation, monocular depth, geometric reconstruction, rendering, mapping

<details>
<summary>Abstract</summary>

Monocular semantic SLAM aims to reconstruct scene geometry and build semantic maps from RGB observations. Existing Gaussian-based methods often attach semantic labels or features to evolving Gaussian primitives, making semantic fusion difficult to maintain and increasing reconstruction overhead. Hybrid Gaussian--voxel representations provide more stable semantic support, but often rely on RGB-D input or known poses and do not revise historical semantic evidence after geometry updates. We present UniGS-SLAM, an RGB-only framework that decouples open-vocabulary semantics from Gaussian reconstruction while preserving bidirectional interaction. Foundation priors enhance monocular depth and pose estimation, while semantic observations are fused into an independent sparse voxel map with observation provenance, enabling historical contributions to be revised as reconstruction evolves. The fused semantics further guide Gaussian filtering and local surface refinement. Experiments on Replica, ScanNet, and KITTI-360 show leading tracking, rendering, and geometric reconstruction performance among representative RGB-only methods, together with strong open-set semantic mapping on Replica and ScanNet. We also achieve a 2.37-fold reconstruction speedup over the fastest compared semantic SLAM baseline. Project page: https://3dagentworld.github.io/UniGS-SLAM/.

</details>

#### 2026-11-01 - Spade-SLAM: Sparse Correspondence Anchors for Dense Self-Supervised Visual SLAM

**Authors:** Julian Philipp Schmitt, Weirong Chen, Ganlin Zhang, Felix Wimbauer, Daniel Cremers
**Links:** [abs](https://arxiv.org/abs/2611.01937) - [pdf](https://arxiv.org/pdf/2611.01937)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM

<details>
<summary>Abstract</summary>

We introduce Spade-SLAM, a self-supervised dense visual SLAM framework that substantially narrows the long-standing performance gap to supervised methods in a zero-shot setting. By demonstrating that high-fidelity tracking can be achieved without explicit ground-truth pose and depth labels, our approach offers a highly effective and label-efficient alternative to fully supervised pretraining. Our core contribution is a complementary sparse-to-dense training regime: While a warping-based photometric loss provides a dense training signal, we stabilize the optimization and suppress drift in ambiguous regions using a sparse correspondence loss derived from image feature matches. Extensive experiments demonstrate that Spade-SLAM significantly improves robustness and accuracy compared to existing self-supervised baselines, closely rivaling SLAM systems trained with explicit pose and depth supervision. The code will be made publicly available at https://github.com/JulianPSchmitt/Spade-SLAM.

</details>

#### 2026-11-01 - Teleoperation System for Service Robots using Virtual Reality Headset and Pose Estimation

**Authors:** Eduardo Fernandes, Tiago Ribeiro, Antonio Ribeiro, Carolina Lopes, Gil Lopes, Fernando Ribeiro
**Links:** [abs](https://arxiv.org/abs/2611.01759) - [pdf](https://arxiv.org/pdf/2611.01759)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, manipulation, mapping, VR, virtual reality

<details>
<summary>Abstract</summary>

This paper presents a teleoperation system for service robots that integrates human pose estimation with virtual reality (VR) to enable intuitive remote control. By using the Mediapipe framework for 2D pose detection and extending it with RGB-D data from the Intel RealSense D455 camera, a comprehensive 3D human pose estimation is achieved. This data is then mapped to the robot's kinematics, allowing the operator to control the robot's movements naturally. A VR interface was developed to provide an immersive perspective, enhancing the operator's situational awareness. Real-world experiments were conducted using the CHARMIE service robot to validate the system's effectiveness in tasks involving object manipulation. While the current system successfully demonstrates the potential of VR-based teleoperation, challenges remain in accurately capturing certain joint angles (e.g., wrist yaw) and ensuring precise mapping between human and robot movements. Future work includes the integration of inertial measurement units (IMUs) for improved rotational tracking and the implementation of more advanced control algorithms. Overall, this research contributes to the development of more intuitive and effective teleoperation systems for service robots, facilitating their deployment in complex and dynamic environments. This work further introduces a novel approach to teleoperation by combining RGB-D sensing with an innovative algorithm for real-time joint angle computation using Mediapipe, enhancing the precision of human-robot motion mapping and enabling immersive control through a VR interface. These contributions represent significant advancements in the field of human-robot interaction, particularly for service robot applications.

</details>

#### 2026-11-01 - EgoMo3R: Joint Egocentric Motion and Scene Reconstruction

**Authors:** Chaitanya Patel, Yusuke Kato, Rin Takahira, Kazuki Kozuka, Juan Carlos Niebles, Ehsan Adeli
**Links:** [abs](https://arxiv.org/abs/2611.01627) - [pdf](https://arxiv.org/pdf/2611.01627)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** motion reconstruction, scene reconstruction, monocular depth, robotics, AR, VR

<details>
<summary>Abstract</summary>

Understanding holistic 3D human motion and the surrounding environment from egocentric video is fundamental for applications in AR/VR and robotics. Although these tasks are inherently coupled, existing methods treat them separately. In particular, egocentric motion reconstruction methods typically assume access to metric, gravity-aligned camera trajectories from specialized inertial sensors. Recovering such trajectories from monocular egocentric video remains a significant challenge due to rapid head movements and motion blur. We present EgoMo3R, a joint optimization framework that simultaneously reconstructs 3D human motion and scene geometry from casual egocentric video. It leverages the robustness of low-level visuo-geometric primitives, including monocular depth, optical flow, and point tracks, integrated with a diffusion-based human motion prior via first-order optimization. We propose an alternating optimization scheme that establishes a synergistic feedback loop: scene reconstruction provides physical grounding and trajectory conditioning for the motion prior, while the motion prior regularizes the camera trajectory and anchors the scene in a metric, gravity-aligned world frame. We evaluate EgoMo3R on the highly dynamic sequences of the EgoExo4D and Nymeria datasets and show that it outperforms specialized baselines in both 3D scene reconstruction and egocentric motion estimation.

</details>

#### 2026-11-01 - Detecting Generated-Depth Injection Attacks on RGB-D Place Authentication

**Authors:** Seigo Kawachi, Satoshi Matsuura
**Links:** [abs](https://arxiv.org/abs/2611.01550) - [pdf](https://arxiv.org/pdf/2611.01550)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>Abstract</summary>

Advances in monocular depth estimation (MDE) now let an attacker generate depth from publicly available RGB images and submit forged RGB-D queries. Such attacks break a core assumption of RGB-D place authentication: that depth comes from a sensor. We study a presentation attack detection (PAD) classifier that uses geometric consistency between the enrollment and query views, as a software-layer defense. A three-stage evaluation shows how far this classifier detects software-injected depth, depending on how accurately the attacker knows the camera intrinsics. In the first stage, the attacker has only an estimate of the intrinsics, and the PAD classifier separates forgeries generated by all three MDE models with a validation area under the receiver operating characteristic curve (AUC) of 0.997-0.999. In the second stage, the attacker obtains the exact intrinsics, and the original PAD classifier falls to near chance (AUC 0.54-0.61); a retrained PAD classifier, however, still has the registration residual between enrollment and query as a cue. In the third stage, an oracle evaluation, in which the evaluator fits warps using the ground-truth 3D geometry, shows that detection falls to near chance only in its strongest case, where every valid query keypoint is given its ground-truth 3D coordinate. Of the detection cues, the reprojection error captures the attacker's misestimate of the intrinsics, whereas the registration residual remains even when the attacker knows the exact intrinsics.

</details>

#### 2026-11-01 - RadPose: ISAC-based RF 3D Human Pose Estimation

**Authors:** Geo Jie Zhou, Kunzhe Song, Ruxin Lin, Huacheng Zeng
**Links:** [abs](https://arxiv.org/abs/2611.01400) - [pdf](https://arxiv.org/pdf/2611.01400)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Human pose estimation under adverse lighting and occlusion conditions remains challenging for camera- and LiDAR-based systems. Although mmWave radars provide robustness to illumination and occlusion, they rely on dedicated hardware and licensed spectrum, limiting scalability. In this paper, we present RadPose, a learning-based monostatic integrated sensing and communication (ISAC) framework that enables mmWave communication devices to perform 3D human pose estimation. Unlike specialized radars, RadPose leverages monostatic full-duplex operation to extract channel impulse responses (CIRs) directly from standard OFDM communication signals, generating 3D radio point clouds without additional sensing hardware. To address the sparsity and noise of RF observations, RadPose employs a cross-frame transformer-based pose inference network with semantic-guided spatial attention and target-driven temporal attention for robust spatio-temporal aggregation. It further adopts a joint-aware inverse kinematics refinement module based on graph convolution to enforce skeletal topology, bone-length consistency, and anatomical plausibility. Extensive experiments demonstrate RadPose achieves competitive accuracy compared to state-of-the-art radar-based approaches while maintaining robust performance in unseen and occluded scenarios. The dataset and source code are available at https://github.com/Geo-Chou/RadPose.

</details>

### 2026-10

#### 2026-10-29 - LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation

**Authors:** Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé
**Links:** [abs](https://arxiv.org/abs/2610.40495) - [pdf](https://arxiv.org/pdf/2610.40495)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** dynamic 3D, 3D reconstruction, scene reconstruction, 3DGS, rendering, robotics, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation
- 作者：Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé
- 出版日期：2026-10-29T17:18:51Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.40495 ；PDF https://arxiv.org/pdf/2610.40495

### 一句话总结
LucidLyra 提出一种前馈框架，从视频潜变量生成可直接查询语义与实例信息的三维场景，并通过多任务蒸馏统一重建与理解。

### 研究问题
生成式三维重建可以从单张图像合成虚拟环境，但机器人与物理 AI 等下游应用不仅需要视觉真实感，还需要获取场景语义和物体身份。现有三维理解方法通常依赖已采集的多视角场景、泛化能力有限，或需要昂贵的逐场景处理与优化。论文旨在弥合生成式三维重建与三维理解之间的差距。

### 核心思路/方法
方法从相机控制的视频扩散模型和冻结的 2D 视觉基础模型中蒸馏互补知识，形成一个统一模型，以联合推断编码几何、外观、开放词汇语义和类别无关实例线索的三维高斯。所得场景支持新视角渲染、开放词汇分割和物体分组，且无需逐场景优化。训练不需要人工三维标注，也不需要采集多视角数据。论文还指出其潜变量形式可自然扩展到单目视频，重建跨时间的结构化动态三维场景。

### 主要贡献
- 提出 LucidLyra 框架，使生成式重建的三维场景能够以前馈方式直接查询语义和实例信息。
- 通过从视频扩散模型与冻结 2D 视觉基础模型进行多任务蒸馏，统一推断几何、外观、开放词汇语义和类别无关实例线索的三维高斯。
- 生成场景支持新视角渲染、开放词汇分割和物体分组，且无需逐场景优化。
- 训练既不需要人工三维标注，也不需要采集多视角数据。
- 在摘要所述精选的合成与真实图像条件基准上，优于将先进 3DGS 分割方法与生成式三维场景重建结合的基线，同时保持重建质量。
- 潜变量形式可扩展到单目视频，重建跨时间的结构化动态三维场景。
- 摘要称可支持三维场景编辑、三维资产挖掘和机器人仿真等下游应用。

### 局限性
- 摘要未提供足够信息说明方法在真实复杂场景中的泛化边界、失败案例或对视频扩散模型与 2D 基础模型质量的依赖程度。
- 摘要未提供足够信息说明动态三维场景扩展的定量结果、时序一致性评估细节和计算开销。
- 摘要未提供足够信息说明基准规模、评价指标、消融实验及与基线对比的具体数值。
- 摘要未提供足够信息说明训练数据来源、蒸馏损失设计细节和开放词汇语义的具体覆盖范围。

### 阅读优先级
高。理由：论文聚焦生成式三维重建与三维理解的联合建模，强调前馈、免逐场景优化、免人工三维标注和免采集多视角数据，并覆盖开放词汇分割、实例分组、动态场景扩展及机器人仿真等下游应用；若关注三维场景理解、3DGS 分割或多任务蒸馏，该工作与这些方向直接相关。但需注意摘要未给出实验细节，阅读全文时应重点核查基准设置、定量结果和局限性。

</details>

<details>
<summary>Abstract</summary>

We present LucidLyra, a framework that makes generatively reconstructed 3D scenes directly queryable for semantics and instances in a feed-forward manner from video latents. While generative 3D reconstruction can synthesize virtual environments from a single image, downstream applications in robotics and physical AI require not only visual realism but also access to scene semantics and object identities. Existing 3D understanding approaches, however, require captured multi-view scenes, have limited generalization capabilities, or rely on expensive per-scene processing and optimization. To bridge this gap, our method distills complementary knowledge from a camera-controlled video diffusion model and frozen 2D vision foundation models into a unified model to jointly infer 3D Gaussians encoding geometry, appearance, open-vocabulary semantics, and class-agnostic instance cues. The resulting scenes support novel-view rendering, open-vocabulary segmentation, and object grouping without per-scene optimization, while training requires neither manual 3D annotations nor captured multi-view data. Our method outperforms baselines combining state-of-the-art 3DGS segmentation approaches with generative 3D scene reconstruction on curated synthetic and real-image-conditioned benchmarks, while preserving reconstruction quality. Furthermore, our latent formulation naturally extends to monocular video, reconstructing structured dynamic 3D scenes across time. By turning renderable but unstructured outputs into queryable 3D worlds, LucidLyra enables downstream applications including 3D scene editing, 3D asset mining, and robotic simulation.

</details>

#### 2026-10-29 - MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments

**Authors:** Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang
**Links:** [abs](https://arxiv.org/abs/2610.39936) - [pdf](https://arxiv.org/pdf/2610.39936)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, scene reconstruction, 3DGS, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments
- 作者：Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang
- 出版日期：2026-10-29T12:36:54Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.39936) | [PDF](https://arxiv.org/pdf/2610.39936) | [项目页](https://wzlwlm13.github.io/MLLM-GS)

### 一句话总结
论文提出 MLLM-GS：利用冻结的多模态大语言模型（MLLM）的视觉先验增强退化视图，并结合快速 3D 场景重建分支，面向极端环境下的新视角合成。

### 研究问题
论文关注退化场景中的新视角合成（NVS）：从受多种退化影响的多视角观测中重建 3D 场景，并在未见视角生成清晰、逼真的图像。摘要指出，现有方法往往依赖针对特定退化类型的模型，跨多样极端环境的泛化能力受限；生成模型虽能提供丰富视觉先验，但其输出存在像素错位和颜色偏差，并可能传播到重建的 3D 场景中，损害重建质量；此外，3D 重建的高计算与内存开销也阻碍了 NVS 在极端环境中的实际应用。

### 核心思路/方法
MLLM-GS 包含两个分支：
1. **MLLM 先验引导的视图增强**：利用冻结 MLLM 的丰富视觉先验，增强在不同严重退化下的视图；引入轻量级校正网络，以减少 MLLM 输出中的像素偏移和颜色失真。该分支仅需少量配对清晰视图作为监督，为所有退化观测生成可靠的增强视图，为后续 3D 重建提供伪 GT 视图。
2. **快速 3D 场景重建**：通过优化光栅化、高斯内存布局和参数更新，降低冗余计算、内存访问开销和优化成本，以提升 3DGS 效率。

### 主要贡献
- 提出 MLLM-GS，一个由 MLLM 先验引导的极端环境下快速 NVS 框架，包含视图增强与快速 3D 场景重建两个分支。
- 利用冻结 MLLM 的视觉先验处理不同严重退化，并通过轻量校正网络缓解 MLLM 输出的像素错位与颜色偏差；仅需少量配对清晰视图监督即可为退化观测生成增强视图和伪 GT。
- 通过优化光栅化、高斯内存布局与参数更新提升 3DGS 效率，减少冗余计算、内存访问和优化成本。
- 摘要称在多个退化场景上的实验表明，MLLM-GS 能有效处理多种严重退化，并以显著更低的 reconstruction time 和内存消耗实现高质量 NVS。

### 局限性
- 摘要未提供足够信息说明具体退化类型、数据集规模、对比基线、评价指标及消融实验的完整细节。
- 摘要未提供足够信息说明轻量校正网络的结构、训练细节，以及“少量配对清晰视图”的具体数量与获取方式。
- 摘要未提供足够信息说明快速 3D 重建分支各优化措施的具体实现与单独贡献。
- 摘要未提供足够信息说明方法在非退化场景或极端退化边界条件下的表现与失败案例。
- 摘要未提供足够信息说明 MLLM 先验引入的额外推理成本及其与 3DGS 加速之间的总体开销权衡。

### 阅读优先级
**中**。理由：该论文聚焦退化场景下 NVS 的泛化性与效率问题，结合冻结 MLLM 先验与 3DGS 加速，主题与 3D 重建及多视角几何方向相关；但当前仅有摘要，缺少实验细节与定量结果，是否值得深入阅读需结合对 MLLM 先验用于 3D 重建、极端环境鲁棒性及 3DGS 效率优化的具体兴趣判断。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis (NVS) in degraded scenes aims to reconstruct 3D scenes from multi-view observations affected by various degradations, and to generate clear and photorealistic images at unseen viewpoints. Despite recent advances, existing methods often rely on degradation-specific models, limiting their generalization across diverse extreme environments. Generative models provide rich visual priors, but their outputs often suffer from pixel misalignment and color deviations, which can propagate into the reconstructed 3D scene and compromise reconstruction quality. Furthermore, the high computational and memory costs of 3D reconstruction hinder the practical application of NVS in extreme environments. To this end, we propose MLLM-GS, a multimodal large language model (MLLM) prior-guided framework for fast NVS in extreme environments. MLLM-GS consists of two branches: MLLM prior-guided view enhancement and fast 3D scene reconstruction. The former leverages the rich visual priors of a frozen MLLM to enhance views under different severe degradations and introduces a lightweight correction network to reduce pixel shifts and color distortions in MLLM outputs. With supervision from only a few paired clean views, this branch produces reliable enhanced views for all degraded observations, providing pseudo-GT views for subsequent 3D reconstruction. The latter improves 3DGS efficiency by optimizing rasterization, Gaussian memory layout, and parameter updates, reducing redundant computation, memory-access overhead, and optimization costs. Extensive experiments on multiple degraded scenes demonstrate that MLLM-GS effectively handles various severe degradations and achieves high-quality NVS with significantly lower reconstruction time and memory consumption. Project Page: https://wzlwlm13.github.io/MLLM-GS

</details>

#### 2026-10-28 - RoSAMDepth: Robust Self-supervised Depth Estimation Leveraging Segment Anything Model

**Authors:** Xuanang Gao, Zhiwei Ning, Gengming Zhang, Jiaxi Cao, Runze Yang, Zhonglong Zheng, Jie Yang, Rong Xiao, Wei Liu
**Links:** [abs](https://arxiv.org/abs/2610.38587) - [pdf](https://arxiv.org/pdf/2610.38587)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoSAMDepth: Robust Self-supervised Depth Estimation Leveraging Segment Anything Model
- 作者：Xuanang Gao, Zhiwei Ning, Gengming Zhang, Jiaxi Cao, Runze Yang, Zhonglong Zheng, Jie Yang, Rong Xiao, Wei Liu
- 出版日期：2026-10-28T10:16:49Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.38587 ；PDF https://arxiv.org/pdf/2610.38587

### 一句话总结
论文提出 RoSAMDepth，利用 Segment Anything Model（SAM）提供的对象级先验，从特征表示、区域深度平滑和对象级可靠性估计三方面增强自监督深度估计的鲁棒性。

### 研究问题
论文关注鲁棒深度估计问题，即希望在多样条件下保持高质量深度。摘要指出，现有方法大多在估计深度时未考虑对象级信息，因此预测深度容易在对象内部发生偏离，并在不利条件下变得模糊。论文试图弥补这一弱点。

### 核心思路/方法
论文提出 RoSAMDepth 框架，借助 SAM 的丰富且多样的对象级先验辅助鲁棒自监督深度估计。摘要说明其从三个关键方面引入对象级信息：
1. 分割引导的表示对比方法（segment-guided representation contrasting method），将对象级感知注入特征表示空间；
2. 自适应区域离群值掩码策略（adaptive regional outlier masking strategy），结合区域高斯似然损失（regional Gaussian likelihood loss），以增强区域深度平滑性；
3. 对象级可靠性估计策略（object-level reliability estimation strategy），用于减轻不可靠监督的影响。

### 主要贡献
- 提出 RoSAMDepth 框架，将 SAM 的对象级先验用于鲁棒自监督深度估计。
- 设计分割引导的表示对比方法，在特征表示空间中注入对象级感知。
- 提出自适应区域离群值掩码策略与区域高斯似然损失，以约束区域深度平滑性。
- 提出对象级可靠性估计策略，以缓解不可靠监督的影响。
- 摘要称在多个数据集和多样天气条件下进行了广泛实验，结果表明该方法能产生更清晰、更准确的深度预测，并持续优于现有最先进方法。具体实验设置、对比方法和数值结果摘要未提供足够信息。

### 局限性
摘要未提供足够信息说明方法局限性。例如，对 SAM 的依赖程度、计算开销、失败场景、对象级先验错误时的鲁棒性、具体数据集与天气条件的覆盖范围等，摘要均未提供足够信息。

### 阅读优先级
中。理由：论文主题属于鲁棒自监督深度估计，并明确结合 SAM 的对象级先验，问题动机和方法要点在摘要中较清晰，适合关注自监督深度估计与基础模型结合的研究者阅读；但摘要未给出具体实验细节、定量结果和局限性分析，是否优先精读需结合读者对 SAM 辅助深度估计方向的兴趣判断。

</details>

<details>
<summary>Abstract</summary>

Robust depth estimation aims to maintain high-quality depths across diverse conditions. However, most existing methods estimate depth without taking into account the object-level information. As a result, the predicted depth may easily deviate within objects and become blurred under adverse conditions. To overcome this weakness, we propose RoSAMDepth, a novel framework that can assist robust self-supervised depth estimation in leveraging rich and diverse object-level priors from the Segment Anything Model (SAM). We focus on incorporating object-level information across three key aspects: a segment-guided representation contrasting method that injects object-level awareness into the feature representation space; an adaptive regional outlier masking strategy combined with a regional Gaussian likelihood loss that enforces regional depth smoothness; and an object-level reliability estimation strategy that mitigates the influence of unreliable supervision. Extensive experiments across multiple datasets and diverse weather conditions demonstrate that our method produces sharper, more accurate depth predictions, consistently outperforming state-of-the-art methods. Our code is available at https://github.com/xagao/RoSAMDepth.

</details>

#### 2026-10-28 - SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites

**Authors:** Hogyun Kim, Juwon Kim, Dongjin Cho, Jiwon Choi, Geonmo Yang, Seokhwan Jeong, Jiyun Lee, Miryeong Park, Hyungtae Lim, Younggun Cho
**Links:** [abs](https://arxiv.org/abs/2610.38141) - [pdf](https://arxiv.org/pdf/2610.38141)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, pose estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites
- 作者：Hogyun Kim, Juwon Kim, Dongjin Cho, Jiwon Choi, Geonmo Yang, Seokhwan Jeong, Jiyun Lee, Miryeong Park, Hyungtae Lim, Younggun Cho
- 出版日期：2026-10-28T01:24:37Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2610.38141 ；PDF https://arxiv.org/pdf/2610.38141

### 一句话总结
本文提出面向行星任务的资源感知分布式多机器人 LiDAR SLAM 系统 SKiD-SLAM，并在韩国两处模拟场址的洞穴与行星表面场景中完成实地部署验证。

### 研究问题
未来行星探索任务需要机器人团队在严重通信受限、星载计算资源受限且没有中心基础设施的条件下协同建图。论文关注如何在这种通信与计算预算下实现多机器人 LiDAR SLAM，并报告其在洞穴探索与科学表面探索两类任务概念中的部署情况。

### 核心思路/方法
论文首先调研实际行星任务的通信与计算预算，并据此选择适合这些预算的模块，用于机器人间地点识别、相对位姿估计和分布式轨迹融合。在实地部署前，系统在类似行星环境的公开数据集以及基于 NASA JPL Open Source Rover 构建的仿真器中进行了验证。随后在韩国开展实地部署：轮式漫游车团队探索济州岛 Majang 熔岩管洞穴，四足机器人团队在韩国建设技术研究院（KICT）涟川的行星模拟地形上执行陨石坑与岩石科学场景。部署中，SKiD-SLAM 在 250 kbps 的机器人间通信预算内可靠完成了分布式多机器人 LiDAR SLAM。

### 主要贡献
- 提出 SKiD-SLAM，一个面向行星探索任务的资源感知分布式多机器人 LiDAR SLAM 系统。
- 调研实际行星任务的通信与计算预算，并据此选择机器人间地点识别、相对位姿估计与分布式轨迹融合模块。
- 在类似行星环境的公开数据集和基于 NASA JPL Open Source Rover 的仿真器中验证组装系统。
- 在韩国济州岛熔岩管洞穴与 KICT 涟川行星模拟地形完成两类任务概念的实地部署，并在 250 kbps 通信预算内验证系统可行性。
- 摘要提到补充材料（含代码与实地数据）可在项目页面获取。

### 局限性
- 摘要未提供足够信息说明系统在更大规模机器人团队、更长任务时长或更复杂通信条件下的表现。
- 摘要未提供足够信息给出定量精度、鲁棒性对比或失败案例分析。
- 摘要未提供足够信息说明计算资源具体配置、模块详细设计及与其它 SLAM 系统的对比结果。
- 摘要未提供足够信息说明公开数据集与仿真验证的具体指标。

### 阅读优先级
中。理由：该论文聚焦行星任务下通信与计算受限的分布式多机器人 LiDAR SLAM，并包含两类实地部署，问题设定和现场验证具有较强应用价值；但摘要未给出定量结果与详细方法对比，是否优先精读取决于读者对行星机器人、分布式 SLAM 或资源受限系统的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Future planetary exploration missions require teams of robots to collaboratively map unknown environments under severe communication limits, constrained onboard computation, and no central infrastructure. In this field report, we present SKiD-SLAM, a distributed multi-robot LiDAR simultaneous localization and mapping (SLAM) system for such environments, and report its deployment across two mission concepts: cave exploration and scientific surface exploration. We survey the communication and computation budgets of actual planetary missions and select modules that fit these budgets for inter-robot place recognition, relative pose estimation, and distributed trajectory fusion. Before field deployment, we verify the assembled system on public datasets resembling planetary environments and in a simulator built on NASA JPL's Open Source Rover. We then validate SKiD-SLAM through field deployments in South Korea: a team of wheeled rovers explores the Majang lava-tube cave on Jeju Island, and quadruped robots carry out a crater-and-rock science scenario on a planetary analog terrain at the Korea Institute of Civil Engineering and Building Technology (KICT) in Yeoncheon. Across both deployments, SKiD-SLAM reliably performed distributed multi-robot LiDAR SLAM within a 250 kbps inter-robot communication budget, demonstrating its feasibility under challenging field conditions. Supplementary materials, including code and field data, are available at https://sparolab.github.io/research/skid_slam/.

</details>

#### 2026-10-27 - Efficacy of Monocular Depth Estimation in Lunar Environments

**Authors:** Michael W. Lanighan, Kenji Brameld, Seth Gee
**Links:** [abs](https://arxiv.org/abs/2610.38080) - [pdf](https://arxiv.org/pdf/2610.38080)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Efficacy of Monocular Depth Estimation in Lunar Environments
- 作者：Michael W. Lanighan, Kenji Brameld, Seth Gee
- 出版日期：2026-10-27T23:52:45Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.38080 ；PDF https://arxiv.org/pdf/2610.38080

### 一句话总结
该研究评估多种先进单目深度估计方法在分布外月球环境中的重建效果，并借助 POLAR 立体数据集与 Apollo 17 表面影像构建从模拟到现场的验证流程。

### 研究问题
现有单目深度估计方法虽在分布内陆地场景中能实现高精度三维重建，但其在分布外月球环境中的有效性尚不明确；论文关注这些方法能否泛化到非结构化月球表面，并产出高保真相对三维重建。

### 核心思路/方法
论文使用 NASA Ames Polar Optical Lunar Analog Reconstruction（POLAR）立体数据集和 Apollo 17 表面影像，建立“模拟到现场”的验证流程：在定量层面，以真实物理模拟物为基准评估若干最先进方法的性能；在定性层面，与历史现场数据进行对比评估。摘要未提供具体方法名称、网络结构、训练策略或评价指标的细节。

### 主要贡献
- 针对分布外月球环境，评估多种最先进单目深度估计方法的有效性。
- 构建基于 POLAR 立体数据集与 Apollo 17 影像的模拟到现场验证流程。
- 结合定量（对照真实物理模拟物）与定性（对照历史现场数据）两类评估。
- 结果表明，部分最先进技术能够成功泛化，生成非结构化月球表面的高保真相对三维重建。

### 局限性
摘要未提供足够信息说明具体方法清单、数据集规模与采集条件、定量指标及其数值、失败案例、计算成本、绝对尺度精度，以及相对三维重建与绝对度量之间的差异等细节。

### 阅读优先级
中。理由：该论文聚焦单目深度估计在月球分布外环境中的泛化与验证流程，对行星探测视觉与三维重建方向具有参考价值；但摘要仅给出总体结论，未披露具体方法、指标和实验细节，是否精读需结合对月球探测或单目深度估计泛化问题的具体兴趣再判断。

</details>

<details>
<summary>Abstract</summary>

Recent advances in monocular depth estimation have demonstrated highly accurate 3D reconstructions within in-distribution terrestrial domains. This study investigates the efficacy of several state-of-the-art approaches to reconstruct out-of-distribution lunar environments using the NASA Ames Polar Optical Lunar Analog Reconstruction (POLAR) stereo dataset and Apollo 17 surface imagery. By leveraging these datasets, we establish a robust analog-to-field validation pipeline that evaluates quantitative performance against ground-truth physical analogs and qualitative performance against historical field data. Our results indicate that select state-of-the-art techniques can successfully generalize to produce high-fidelity relative 3D reconstructions of the unstructured lunar surface.

</details>

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-02 - 3D Gaussian Splatting within Self-Learned Neural View-Dependent Color Fields

**Authors:** Yixiao Yang, Yu-Shen Liu, Zhizhong Han
**Links:** [abs](https://arxiv.org/abs/2611.03114) - [pdf](https://arxiv.org/pdf/2611.03114)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, radiance, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become a vital tool in novel view synthesis. 3D Gaussian functions with attributes like color, opacity, and scale are stacked together to explicitly model a radiance field. However, discrete 3D Gaussians usually produce poor depth with few geometry details but lots of floaters, which hinders the effective modeling of smooth radiance fields. To address this issue, we propose to learn a radiance field within a continuous view-dependent color field parameterized by neural networks. With continuous constraints in color, the bias on low-frequency signals of neural networks can highly encourage the geometry modeling to contribute to high-frequency color variations on images, getting rid of solely relying on the color attribute itself. Moreover, we impose a constraint to improve the Lipschitz continuity of the neural color field, making large changes of each Gaussian's color also match with large changes of its position in terms of a ratio. To this end, we additionally introduce novel self-learning strategies to improve the learning of the neural view-dependent color field without any external knowledge or priors, aiming for better generalization on unseen scenes. Our numerical and visual comparisons on widely used benchmarks justify our idea and show better ability of high fidelity geometry recovery in 3DGS. Project page: https://github.com/yangyixi21/Neural-Color-Fields-3DGS.

</details>

#### 2026-11-02 - SyncHeC: Markerless Spatio-Temporal Hand-Eye Calibration via Differentiable Rendering and Continuous-Time Joint Optimization

**Authors:** Zhengdong Hong
**Links:** [abs](https://arxiv.org/abs/2611.02999) - [pdf](https://arxiv.org/pdf/2611.02999)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** metric depth, camera calibration, differentiable rendering, rendering

<details>
<summary>Abstract</summary>

Markerless hand-eye calibration under continuous motion requires jointly resolving camera geometry and the time offset between images and joint states. We present SyncHeC (Synchronized Hand-Eye Calibration), a dense differentiable-rendering framework that estimates both from a single robot trajectory. Continuous-time forward kinematics makes latency differentiable, metric depth complements mask contours, and an offline planner combines spatial sensitivity with temporal excitation. Alternating updates support Eye-to-Hand, Eye-in-Hand, and multi-camera calibration. On a 7-DoF arm, one $6.5$\,s motion yields $0.21$\,cm translation error against a marker-board reference, $0.34$\,cm touch-test error, and $2.7$\,ms latency error relative to an $87$\,ms reference with $95\%$ uncertainty of $\pm1.5$\,ms. Against CM-Calib on matched recordings, translation and nominal latency errors improve by $3.7\times$ and $2.3\times$. Experiments span seven arms and four depth sensors. Compensating the recovered offset during policy training and deployment increases success by $8.1$ percentage points across six families and six tasks ($1{,}800$ matched pairs; paired $95\%$ confidence interval $[6.3,9.9]$ points).

</details>

#### 2026-11-02 - GaussFlaw: Fine-Grained Perceptual Diagnosis for 3D Gaussian Splatting

**Authors:** Shaocheng Shen, Zihan Zheng, Kejin Li, Lu Liu, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang
**Links:** [abs](https://arxiv.org/abs/2611.02767) - [pdf](https://arxiv.org/pdf/2611.02767)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic novel- view synthesis with real-time rendering, yet fine-grained di- agnosis of its rendering artifacts remains challenging. These artifacts are typically spatially localized and exhibit diverse degradation patterns, making them difficult to character- ize using global quality metrics and image-level assessment benchmarks, which provide no explicit indication of where they occur or what types of artifacts they represent. To ad- dress this limitation, we introduce GaussFlaw-80K, the first large-scale dataset for fine-grained perceptual diagnosis in 3DGS. Constructed through a model-assisted human-in-the- loop pipeline, GaussFlaw-80K contains 80,049 artifact re- gions across 14,289 rendered images, each annotated with a pixel-level mask and one of eight flaw labels spanning ge- ometric, blending, and photometric degradations. These an- notations turn 3DGS artifact diagnosis into an explicit and measurable task. Building on this dataset, we propose Ge- oCritic, a geometry-guided multi-task model that integrates RGB appearance with depth-derived cues to jointly localize artifacts and classify their flaw types. Beyond evaluation, we further demonstrate the downstream benefits of fine-grained diagnosis through three complementary targeted operations: Gaussian densification, attribute correction, and outlier prun- ing. Experiments show that GeoCritic achieves an AUC-J of 0.9507 and an Acc@1 of 80.08%, while diagnosis-guided re- finement improves all reported global and crop-level metrics across diverse datasets and 3DGS backbones.

</details>

#### 2026-11-02 - UniCross3D: Unified Cross-View and Cross-Domain Diffusion for Consistent Single-Image 3D Generation

**Authors:** U-Chae Jun, Jaeeun Ko, Jiwoo Kang
**Links:** [abs](https://arxiv.org/abs/2611.02631) - [pdf](https://arxiv.org/pdf/2611.02631)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Reconstructing detailed geometry and realistic appearance from a single RGB image is essential yet fundamentally challenging due to inherent ambiguities such as occlusion, lighting variations, and texture-geometry entanglement. While recent diffusion-based generative models have significantly improved novel view synthesis, existing approaches suffer from two critical limitations: lack of cross-view geometric consistency and insufficient cross-domain semantic alignment. To address these issues, we introduce UniCross3D, a unified cross-view and cross-domain diffusion framework designed explicitly for consistent and physically coherent 3D generation. UniCross3D features two novel contributions: (1) a cross-view latent regularization that enforces cross-view geometric consistency across synthesized viewpoints by penalizing latent variance, and (2) a cross-domain mutual information objective grounded in the physics of image formation, explicitly aligning synthesized color and normal maps. Extensive experiments demonstrate that UniCross3D achieves significantly improved view consistency and semantic alignment over state-of-the-art methods and yields higher-fidelity reconstructions, particularly under challenging textures and ambiguous viewpoints.

</details>

#### 2026-11-01 - Unified Loss-Aware Density Control for 3D Gaussian Splatting

**Authors:** Tae-Young Kim, Jiwoo Chung, Jae-Pil Heo
**Links:** [abs](https://arxiv.org/abs/2611.02044) - [pdf](https://arxiv.org/pdf/2611.02044)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

The efficiency and fidelity of 3D Gaussian Splatting critically depend on adaptive density control, which grows and suppresses Gaussian primitives throughout optimization. However, the standard pipeline still relies on heuristic view-space gradients, scale thresholds, and global opacity resets, rather than explicitly assessing the loss-reducing effect of each split, clone, or opacity update. This mismatch can allocate primitives to already-sufficient regions, miss under-reconstructed structures, and destabilize training through blanket opacity changes. In this work, we recast adaptive density control as a collection of local loss-reduction decisions. We derive efficient Taylor-based per-Gaussian surrogates that predict the objective change caused by three primitive-level operations: splitting, cloning, and opacity decay. This yields a unified loss-aware framework with three components. First, we extend second-order splitting to a normalized joint position-scale space, enabling children to adapt not only their locations but also their anisotropic extents. Second, we formulate duplicate cloning as a surrogate minimization problem, selecting only Gaussians whose duplicated contribution is predicted to improve reconstruction and assigning each child a principled opacity. Third, we replace global opacity reset with selective soft opacity decay that weakens harmful primitives while preserving useful ones. Across standard 3DGS benchmarks, our method produces more targeted primitive allocation and achieves improved rendering quality with comparable or smaller Gaussian budgets compared to baselines.

</details>

#### 2026-11-01 - VLSplat: Vision-Language Guided Object-Centric 3D Gaussian Splatting via Scene Graph

**Authors:** Yuntae Jeon, Younho Jeon, Sujin Jin, Sungho Jo, Seunghee Park
**Links:** [abs](https://arxiv.org/abs/2611.01939) - [pdf](https://arxiv.org/pdf/2611.01939)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, scene understanding

<details>
<summary>Abstract</summary>

Learning semantic representations for 3D Gaussian Splatting has recently emerged as a promising direction for 3D scene understanding. However, existing 2D-to-3D semantic lifting approaches rely primarily on 2D segmentation supervision and lack object-level priors, causing the learned representation to be driven by local mask evidence rather than holistic object structure. In this paper, we present VLSplat, a vision-language guided approach for object-centric semantic lifting in 3D Gaussian Splatting. Our method augments mask-based lifting with object-level semantic priors derived from vision-language models and refines Gaussian representations using an object-group scene graph. The refinement is performed through two language-guided modules: intra-group refinement suppresses semantic noise within object groups, while inter-group acquisition expands object support regions by incorporating structurally relevant candidates from neighboring groups. Extensive experiments on indoor scene datasets demonstrate that VLSplat improves the semantic consistency and structural completeness of object-level categories. Our code and models are available at https://vlsplat.github.io/.

</details>

#### 2026-11-01 - AbacusGS: Gaussian Splatting without Per-Splat Sorting

**Authors:** Jiacheng Ding, Yanliang Qi, Cong Guo, Peihua Mai
**Links:** [abs](https://arxiv.org/abs/2611.01534) - [pdf](https://arxiv.org/pdf/2611.01534)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting sorts every splat by depth in every frame. Viewers that draw splats with the hardware rasterizer and sort them on the CPU, as most web and mobile viewers do, spend most of the frame time in this sort. We present AbacusGS, which stores the blending order of a 3DGS scene in the scene layout. AbacusGS groups the splats into octree boxes of at most 128 splats and stores each box in order along an axis chosen at write time. In each frame, AbacusGS sorts only the visible boxes, and one dot product per box decides whether the box is read forward or backward. A short order-aware fine-tuning converts an existing 3DGS model, and the over operator of 3DGS stays unchanged. On 13 standard scenes, AbacusGS loses 0.13 dB PSNR on average against an equally fine-tuned 3DGS model. In an OpenGL viewer that orders splats on the CPU, AbacusGS renders frames 4.5 times faster than per-splat sorting. We also present a compact format of 17 bytes per splat and a CUDA tile renderer that use the same order. The code will be released.

</details>

### 2026-10

#### 2026-10-29 - ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting

**Authors:** Houqiang Zhong, Tianchi Zhu, Qiang Hu, Xiaoyun Zhang, Li Song, Wenjun Zhang
**Links:** [abs](https://arxiv.org/abs/2610.39399) - [pdf](https://arxiv.org/pdf/2610.39399)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** geometric reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting
- 作者：Houqiang Zhong, Tianchi Zhu, Qiang Hu, Xiaoyun Zhang, Li Song, Wenjun Zhang
- 出版日期：2026-10-29T05:34:55Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.39399) / [PDF](https://arxiv.org/pdf/2610.39399) / [项目页](https://waveviewer.github.io/ACD-GS/)

### 一句话总结
论文提出 ACD-GS，一种利用二阶深度响应作为结构先验、对克隆与分裂进行非对称调控的 3D Gaussian Splatting 致密化框架，旨在训练阶段直接抑制冗余高斯生成，获得更紧凑且几何感知的表示。

### 研究问题
摘要指出，3DGS 的训练期致密化仍以启发式为主，常导致高斯冗余增殖与几何重建不准确。现有方法主要依赖一阶屏幕空间梯度触发克隆与分裂，难以区分真实几何不连续与高频纹理或噪声残差。论文关注的正是这一密度控制判据的可靠性问题。

### 核心思路/方法
- 核心洞察：二阶深度响应可为密度控制提供更可靠的结构先验。
- 基于该先验，对克隆与分裂实施**非对称调控**，以更好捕捉几何不连续。
- 引入**多视角光度一致性约束**，抑制瞬时的单视角误差。
- 引入**容量感知的自适应调控策略**，在训练中平衡致密化与剪枝。
- 与事后压缩或量化方法不同，该方法在训练过程中直接防止冗余高斯生成。

### 主要贡献
- 提出 ACD-GS，一个面向紧凑与几何感知 3D 高斯优化的非对称曲率感知致密化框架。
- 将二阶深度响应用于密度控制，并据此非对称调节克隆与分裂。
- 结合多视角光度一致性约束与容量感知自适应调控策略。
- 摘要称实验中将高斯数量与存储减少近 60%，同时保持有竞争力的渲染保真度，并在多个数据集上持续优于现有方法。

### 局限性
- 摘要未提供足够信息说明二阶深度响应的具体计算方式、非对称调控的阈值设定与实现细节。
- 摘要未提供足够信息说明多视角光度一致性约束的具体形式与视角采样策略。
- 摘要未提供足够信息说明容量感知策略中超参数设置及对训练开销的影响。
- 摘要未提供足够信息列出所用数据集、对比方法与完整定量结果，仅给出约 60% 的缩减幅度与总体结论。
- 摘要未提供足够信息讨论方法在弱纹理、透明或反射等困难场景下的表现与失败情形。

### 阅读优先级
**高**。理由：该工作针对 3DGS 致密化这一训练效率与表示紧凑性的核心环节，提出可替代一阶梯度判据的二阶结构先验，并声称在显著减少高斯数量与存储的同时保持渲染保真度；对关注 3DGS 表示紧凑化、几何重建质量与训练期密度控制的研究者具有直接参考价值。具体收益幅度与适用边界仍需查阅全文实验部分确认。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as a powerful paradigm for real-time photorealistic novel view synthesis. However, its training-time densification remains largely heuristic, often resulting in redundant Gaussian proliferation and inaccurate geometric reconstruction. Existing methods predominantly rely on first-order screen-space gradients to trigger cloning and splitting, which fail to distinguish true geometric discontinuities from high-frequency textures or noisy residuals. To address this limitation, we propose ACD-GS, an Asymmetric Curvature-aware Densification framework for compact and geometry-aware 3D Gaussian optimization. Our key insight is that second-order depth responses provide a more reliable structural prior for density control, enabling asymmetric regulation of cloning and splitting to better capture geometric discontinuities. Building on this, we introduce a multi-view photometric consistency constraint to suppress transient single-view errors, together with a capacity-aware adaptive regulation strategy that balances densification and pruning during training. Unlike post-hoc compression or quantization-based approaches, ACD-GS directly prevents redundant Gaussian generation during training, yielding inherently compact representations. Extensive experiments demonstrate that our method reduces nearly 60% of Gaussian count and storage while maintaining competitive rendering fidelity, consistently outperforming existing methods across multiple datasets. Our code is available in https://waveviewer.github.io/ACD-GS/.

</details>

#### 2026-10-29 - COGS: A Diagnostic Benchmark for Attribute-Aware Object-Level 3D Gaussian Splatting Perception

**Authors:** Zheng Xiao, Yifan Liu, Weijian Deng, Jiashu Li, Ziqin Liu, Zhenjun Han, Jianbin Jiao
**Links:** [abs](https://arxiv.org/abs/2610.39201) - [pdf](https://arxiv.org/pdf/2610.39201)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：COGS: A Diagnostic Benchmark for Attribute-Aware Object-Level 3D Gaussian Splatting Perception
- 作者：Zheng Xiao, Yifan Liu, Weijian Deng, Jiashu Li, Ziqin Liu, Zhenjun Han, Jianbin Jiao
- 出版日期：2026-10-29T02:23:23Z
- 分类：Neural Scene Representations & Rendering（主分类）；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.39201 ；PDF https://arxiv.org/pdf/2610.39201

### 一句话总结
论文提出面向对象级 3D Gaussian Splatting 感知的属性诊断基准 COGS（含数据集与 COGS-Bench），揭示不同高斯属性子集对分类的影响并不一致，并提供保留属性角色信息的参考模型 HALO。

### 研究问题
3D Gaussian Splatting 正被探索用作 3D 感知的输入表示，但当前 3D 架构如何利用异构的高斯属性仍不清楚，导致准确率难以解释，也限制了面向 3DGS 感知的原则化架构设计。现有对象级 3DGS 数据集缺乏外观变化或伪影控制，难以进行系统的属性级分析。

### 核心思路/方法
- 构建大规模 3DGS 数据集 COGS，包含 40 个类别、15,675 个经过伪影过滤且外观丰富的对象。
- 基于 COGS 建立 COGS-Bench，用于对象分类与属性使用诊断，并辅以外部验证。
- 通过基准分析高斯属性的作用，发现属性并非一致有益：部分属性子集可优于完整属性集，且外观、不透明度及协方差相关属性组合的效果在不同架构间差异显著。
- 提出参考模型 HALO，在层级聚合之前保留属性特定证据，以研究属性角色保持的组织方式。

### 主要贡献
- 提出 COGS：大规模、经伪影过滤、外观丰富的对象级 3DGS 数据集，覆盖 40 类、15,675 个对象。
- 建立 COGS-Bench，支持对象分类和属性使用诊断，并包含外部验证。
- 给出诊断性发现：高斯属性并非均匀有益，属性子集可能优于全集，不同属性组合的效果随架构显著变化。
- 提出 HALO 参考模型，强调角色保持的属性组织价值；在 COGS-Bench 与外部 3DGS 数据集上的实验表明 COGS 支持系统的 3DGS 属性使用诊断。
- 公开数据集链接。

### 局限性
- 摘要未提供足够信息说明数据集构建的具体流程、伪影过滤标准与类别平衡细节。
- 摘要未提供足够信息说明 COGS-Bench 的具体评价指标、基线架构清单与定量结果。
- 摘要未提供足够信息说明 HALO 的网络结构细节、训练配置与计算开销。
- 摘要未提供足够信息说明外部验证所用数据集、外部 3DGS 数据集实验设置及统计显著性。
- 摘要未提供足够信息说明属性子集优于全集的具体条件与适用范围。

### 阅读优先级
高。理由：该工作直接针对 3DGS 感知中“属性如何被利用”这一可解释性与架构设计问题，提供专用诊断基准与参考模型，并公开数据集；对研究 3DGS 表示、3D 感知架构分析与基准构建的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) is increasingly explored as an input representation for 3D perception. Yet it remains unclear how current 3D architectures exploit heterogeneous Gaussian attributes. This ambiguity makes accuracy hard to interpret and limits principled architecture design for 3DGS perception. However, existing object-level 3DGS datasets lack the appearance variation or artifact control needed for systematic attribute-level analysis. We introduce COGS, a large-scale 3DGS dataset with 15,675 artifact-filtered and appearance-rich objects across 40 categories. Built on COGS, we establish COGS-Bench for object classification and attribute-usage diagnosis, complemented by external validation. Our benchmark shows that Gaussian attributes are not uniformly beneficial: selected subsets can outperform the full attribute set, and the effects of appearance, opacity, and covariance-related attribute combinations vary substantially across architectures. We further study this finding with HALO, a reference model that preserves attribute-specific evidence before hierarchical aggregation. Experiments on COGS-Bench and external 3DGS datasets demonstrate that COGS supports systematic diagnosis of 3DGS attribute usage, while HALO highlights the value of role-preserving attribute organization. Our dataset is available at https://huggingface.co/datasets/XiaoZhengCV/COGS.

</details>

#### 2026-10-28 - GradSplat: Gradients Inside the Forward Pass for Feed-Forward 3D Gaussian Splatting

**Authors:** Jingong Chen, Linlian Jiang, Guangyuan Li, Xinxin Zuo, Yang Wang, Chulwoo Pack, Kyle Gao, Kwanghee Won
**Links:** [abs](https://arxiv.org/abs/2610.38951) - [pdf](https://arxiv.org/pdf/2610.38951)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GradSplat: Gradients Inside the Forward Pass for Feed-Forward 3D Gaussian Splatting
- 作者：Jingong Chen, Linlian Jiang, Guangyuan Li, Xinxin Zuo, Yang Wang, Chulwoo Pack, Kyle Gao, Kwanghee Won
- 出版日期：2026-10-28T21:36:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.38951) / [PDF](https://arxiv.org/pdf/2610.38951)

### 一句话总结
GradSplat 在前向传播内部用学习到的梯度步骤，对前馈预测出的 3D 高斯做自细化，缩小前馈预测的 3D 高斯与逐场景优化的 3D 高斯之间的精度差距。

### 研究问题
前馈 3D Gaussian Splatting 能从少量图像预测场景，但其精度低于在同一批图像上逐场景优化的 Gaussian。摘要指出这一差距主要体现在高斯的形状（尺度与旋转）上，因为仅优化形状就几乎能恢复全部差距，而不透明度和颜色能恢复的部分较少。因此，论文关注的是：如何让前馈模型自身缓解这一高斯形状的精度差距。

### 核心思路/方法
- 观察到对输入视图做梯度步骤可以纠正高斯形状，并且模型在推理时仍可保留这些输入视图。
- 提出 Log-anisotropy correction：在对数空间中、保持体积不变的情况下改变每个高斯的轴比。
- 提出 in-forward gradient refinement：将高斯渲染到输入视图，应用光度损失的梯度，并通过学习到的循环更新进行细化；更新顺序为先处理不透明度和颜色，再处理形状。
- GradSplat 是一个前馈模型，在其前向传播内部通过学到的梯度步骤细化自身生成的高斯，且不使用目标视图。

### 主要贡献
- 提出在前向传播内部进行学习式梯度细化，使前馈 3D Gaussian Splatting 模型能够自我纠正高斯形状。
- 引入 Log-anisotropy correction，在对数空间、恒定体积下调整高斯轴比。
- 在 RealEstate10K 的两个完整六视图协议上，于九种方法中取得最佳 PSNR 和 SSIM，并在 6 到 42 个输入视图范围内保持精度。
- 未经微调，在 DL3DV 上最准确，在 ScanNet++ 上取得最佳 PSNR 和 SSIM。
- 代码将发布于 https://github.com/Jingong-Chen/GradSplat/。

### 局限性
摘要未提供足够信息来系统说明局限性。仅能看出：方法依赖推理时保留输入视图，并在前向传播中执行梯度细化；其计算开销、对输入视图数量的极端变化、失败场景等，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作直接针对前馈 3D Gaussian Splatting 中“预测高斯不如逐场景优化高斯”的关键精度差距，并给出前向内部梯度细化的明确方案；摘要报告了多个数据集和协议上的领先结果，对神经场景表示与渲染方向有参考价值。但摘要未提供实现细节、计算成本与局限分析，是否精读需结合全文实验与效率信息再判断。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting predicts a scene from a few images, but our predictor is less accurate than its own Gaussians optimized per scene on those images. This gap lies mostly in the shape of the Gaussians, their scale and rotation, since optimizing the shape alone recovers almost all of it and opacity and color recover less. Gradient steps on the input views correct this shape, and the model holds these views at inference. Log-anisotropy correction changes the axis ratios of each Gaussian in log space at constant volume, and in-forward gradient refinement renders the Gaussians into the input views and applies the gradient of the photometric loss with a learned recurrent update, first to opacity and color and then to the shape. GradSplat is a feed-forward model that refines its own Gaussians by learned gradient steps inside its forward pass, with no target view. On both complete six-view RealEstate10K protocols, it has the best PSNR and SSIM among nine methods and keeps its accuracy from $6$ to $42$ input views. Without fine-tuning, it is the most accurate on DL3DV and has the best PSNR and SSIM on ScanNet++. The code will be released at https://github.com/Jingong-Chen/GradSplat/.

</details>

#### 2026-10-28 - Aligning Misaligned Benchmarks for Single-View Novel View Synthesis

**Authors:** Yang-Che Tseng, Erqun Dong, Jeong-gi Kwak, Gopal Sharma, Shakiba Kheradmand, Stephan Garbin, Hossam Isack, Kwang Moo Yi
**Links:** [abs](https://arxiv.org/abs/2610.38349) - [pdf](https://arxiv.org/pdf/2610.38349)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** image matching, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Aligning Misaligned Benchmarks for Single-View Novel View Synthesis
- 作者：Yang-Che Tseng, Erqun Dong, Jeong-gi Kwak, Gopal Sharma, Shakiba Kheradmand, Stephan Garbin, Hossam Isack, Kwang Moo Yi
- 出版日期：2026-10-28T06:49:44Z
- 分类：主分类为 Neural Scene Representations & Rendering；无副分类
- 链接：[摘要](https://arxiv.org/abs/2610.38349)｜[PDF](https://arxiv.org/pdf/2610.38349)

### 一句话总结
论文指出单视图新视角合成评测中“方法自身参考系与真值位姿对齐”这一关键问题会造成不公平比较，并提出使用传统 2D-to-2D 与 2D-to-3D 图像匹配来对齐三维重建、仅在共视区域内评测的改进方案。

### 研究问题
单视图新视角合成方法近年来性能显著提升，但如何量化其性能尚未标准化。作者认为一个重要因素在于：每种方法自身的参考系如何与所谓“真值位姿”对齐。现有方法常依赖在测试时对目标位姿进行优化来完成对齐，但由于相机位姿与渲染精度之间的优化 landscape 复杂，该问题本质上是病态的（ill-posed），导致方法可能在任意局部最优处被评估。部分工作意识到这一局限，转而使用训练与测试视图对整个场景做三维重建来对齐位姿，但这可能不可行。因此，论文聚焦于如何更合理地完成坐标对齐并定义有效评测区域。

### 核心思路/方法
- 不使用测试时目标位姿优化，也不依赖包含训练与测试视图的全场景三维重建来对齐位姿。
- 提出使用传统 2D-to-2D 和 2D-to-3D 图像匹配技术来对齐三维重建。
- 评测仅在视图之间的共视区域（co-visible regions）内进行，作者认为这是唯一可以定义“正确”真值的地方。
- 提供一个简单基线：直接使用现成的视频生成器与前馈几何估计器，且不做任何任务特定训练。

### 主要贡献
- 揭示单视图新视角合成评测中参考系与真值位姿对齐问题的重要性，并指出测试时位姿优化与全场景三维重建对齐方式的局限。
- 提出基于传统 2D-to-2D 与 2D-to-3D 图像匹配的三维重建对齐方案，并限定在共视区域内评测。
- 基于该评测发现：使用显式三维高斯的新视角合成方法在正确坐标对齐后达到 state of the art，尽管此前文献报告其被纯图像式二维方法超越。
- 提供一个无需任务特定训练的简单基线（现成视频生成器 + 前馈几何估计器），其性能已可与专门为新视角合成训练的最先进方法相比。

### 局限性
- 摘要未提供足够信息说明所提对齐方法在不同场景、不同基线方法上的具体误差或鲁棒性表现。
- 摘要未提供足够信息说明共视区域评测在多大程度上改变已有 benchmark 的排名，以及除“显式三维高斯方法”外的其他方法类别的重评结果。
- 摘要未提供足够信息说明简单基线的具体实现细节、运行成本与失败情形。
- 摘要未提供足够信息说明该方法对 2D-to-2D / 2D-to-3D 匹配失败或匹配质量不佳时的处理方式。

### 阅读优先级
高。理由：该论文直接针对单视图新视角合成的评测标准化问题，指出已有评测中的坐标对齐缺陷，并给出可能改变方法排名结论的重评结果；对关注该任务评测公平性、三维高斯方法与图像式方法比较的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

While single-view novel view synthesis methods have been dramatically enhanced recently, how to quantify their performance has yet to be standardized. In this work, we demonstrate that an important factor lies in how each method's own reference frame is aligned with the so-called ground-truth pose. Existing methods often rely on test-time optimization of target poses for this alignment, which inherently is ill-posed due to the complexity of the optimization landscape of camera poses vs render accuracy, leading to methods being evaluated at an arbitrary local optimum. Some recognize this limitation and thus rely on 3D reconstructions of entire scenes using training and test views to align poses, which may be infeasible. In this work, instead, we propose to use traditional 2D-to-2D and 2D-to-3D image matching techniques to align 3D reconstructions. We also evaluate only within co-visible regions, between different views, which is the only place where a `correct' ground truth can be defined. Our evaluations show that with proper coordinate alignment, novel-view synthesis methods that use explicit 3D Gaussians achieve the state of the art, despite being previously reported in the literature to be outperformed by pure image-based 2D methods. We further provide a simple baseline that directly utilizes an off-the-shelf video generator and a feed-forward geometry estimator. Our simple baseline is already comparable to state-of-the-art methods specifically trained for novel-view synthesis, without any task-specific training.

</details>

#### 2026-10-28 - Extremely Sparse-View Computed Tomography from 2D Projections via Pose-Aware Diffusion Priors

**Authors:** Linrui Dai, Jinxiu Liang, Chu Zhou, Mae Yamaguchi, Ryuya Takahashi, Imari Sato
**Links:** [abs](https://arxiv.org/abs/2610.38319) - [pdf](https://arxiv.org/pdf/2610.38319)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Extremely Sparse-View Computed Tomography from 2D Projections via Pose-Aware Diffusion Priors
- 作者：Linrui Dai, Jinxiu Liang, Chu Zhou, Mae Yamaguchi, Ryuya Takahashi, Imari Sato
- 出版日期：2026-10-28T06:08:39Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.38319) / [PDF](https://arxiv.org/pdf/2610.38319)

### 一句话总结
本文针对一种“训练稀疏、推理稀疏”的极端稀疏视角 CT（xSV-CT）场景，提出从每训练样本仅一张 2D 投影中学习姿态感知扩散先验，并在扩散采样中结合测量视图保真、共享体积重投影和投影物理一致性来重建 CT。

### 研究问题
极端稀疏视角 CT（xSV-CT）在扫描时间、运动或辐射耐受限制每次扫描仅能获取少量投影时非常重要。但同一采集限制也约束数据集构建，使得来自密集扫描的预重建 3D 体积不可用。现有稀疏视角方法存在空白：基于优化的方法直接使用稀疏测量但缺乏数据驱动先验抑制伪影；基于学习的方法有强先验但通常需要密集扫描训练体积，而这些训练体积是在 xSV-CT 场景之外采集的。论文聚焦“train-sparse / infer-sparse”设定。

### 核心思路/方法
- 从每训练样本一张 2D 投影中学习姿态感知扩散先验。
- 在扩散采样过程中引入三类引导：
  - 测量视图保真（measured-view fidelity）
  - 共享体积重投影（shared-volume reprojection）
  - 投影物理一致性（projection-physics consistency）
- 用于断层重建。

### 主要贡献
- 明确提出并研究“train-sparse / infer-sparse”的 xSV-CT 设定：不依赖密集扫描 3D 体积监督。
- 提出从单张 2D 投影学习姿态感知扩散先验，并结合重建引导进行 CT 重建。
- 在两个公开 CT 数据集、1/4/8 视角设置下，报告了最佳新视角合成分数，以及与使用密集体积监督的基线相比最佳或具有竞争力的重建质量。

### 局限性
- 摘要未提供足够信息说明具体网络结构、训练细节、推理耗时和参数敏感性。
- 摘要未提供足够信息说明失败案例、极端视角条件下的性能边界及临床/真实采集验证情况。
- 摘要未提供足够信息说明“投影物理一致性”的具体建模假设与适用范围。

### 阅读优先级
中。理由：该工作与稀疏视角 CT、扩散先验和神经场景表示直接相关，且明确针对“训练数据也稀疏”的实际约束，具有方法参考价值；但摘要仅给出高层方法与总体结果，具体实验细节、实现与泛化证据需阅读全文进一步确认。

</details>

<details>
<summary>Abstract</summary>

Extremely sparse-view computed tomography (xSV-CT) is critical when scanning time, motion, or radiation tolerance limits each scan to only a few projections. In many such scenarios, the same acquisition limits also constrain dataset construction, making pre-reconstructed 3D volumes from dense scans unavailable. This exposes a gap in current sparse-view approaches: Optimization-based methods, which use the sparse measurements directly but lack data-driven priors to suppress artifacts, and learning-based methods, which use strong priors but usually require densely scanned training volumes acquired outside the xSV-CT regime. We study this train-sparse / infer-sparse setting by learning a pose-aware diffusion prior from one 2D projection per training sample, then guiding diffusion sampling with measured-view fidelity, shared-volume reprojection, and projection-physics consistency for tomographic reconstruction. On two public CT datasets across 1-, 4-, and 8-view settings, the proposed method achieves the best novel-view synthesis scores and best or competitive reconstruction quality compared with baselines that use dense-volume supervision.

</details>

#### 2026-10-28 - BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget

**Authors:** Muyu Xu, Fangneng Zhan, Yu Wei, Ling Shao, Shijian Lu
**Links:** [abs](https://arxiv.org/abs/2610.38278) - [pdf](https://arxiv.org/pdf/2610.38278)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget
- 作者：Muyu Xu, Fangneng Zhan, Yu Wei, Ling Shao, Shijian Lu
- 出版日期：2026-10-28T05:00:22Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.38278) | [PDF](https://arxiv.org/pdf/2610.38278)

### 一句话总结
BudSplat 提出一种紧凑的前馈 3D Gaussian Splatting 框架，在有限 Gaussian 基元数量约束下学习保留最有价值的基元，以缓解多视角输入扩展带来的渲染效率瓶颈。

### 研究问题
前馈 3D Gaussian Splatting 能从输入图像直接预测 Gaussian 基元，实现快速新视角合成，但在从稀疏多视角扩展到密集多视角输入时面临渲染效率瓶颈：密集输入提供更多几何约束，却会产生快速增长的候选 Gaussian 集合。现有方案无法可靠区分冗余基元，导致反复观测区域产生大量冗余基元，渲染成本上升而视觉质量收益有限。论文关注的核心问题是：如何在有限基元数量下保留最有价值的 Gaussian，从而在渲染质量与效率之间取得更好权衡。

### 核心思路/方法
论文提出 BudSplat，一个紧凑的前馈 3DGS 框架，其目标是在受限基元数量下学习保留最有价值的 Gaussians。方法包含两个新设计：

1. **细节感知重要性分数**：从多级视觉 token 中提取细节感知重要性分数，为“剪枝可能损害感知质量”的区域提供显式线索。该分数可注入体素融合过程，在多视角聚合时保留高价值局部贡献者。
2. **质量感知 Gaussian 剪枝**：联合考虑渲染贡献与细节重要性，选择紧凑的基元集合。该剪枝支持局部配额重分配，有助于避免将过多基元分配给大面积冗余区域。

### 主要贡献
- 提出 BudSplat 紧凑前馈 3DGS 框架，面向有限基元数量下的渲染预算约束。
- 设计细节感知重要性分数，从多级视觉 token 中提取显式线索，并可注入体素融合以保留高价值局部贡献者。
- 设计质量感知 Gaussian 剪枝，联合考虑渲染贡献与细节重要性，并支持局部配额重分配以抑制冗余区域过度分配基元。
- 在 RE10K、DL3DV 和 ACID 上的实验表明，BudSplat 在渲染质量与效率之间取得了有利权衡（摘要仅给出结论性描述，具体实验细节未提供）。

### 局限性
摘要未提供足够信息。论文摘要未说明方法的具体计算开销、对不同输入密度或场景类型的敏感性、失败案例，以及实验中的定量指标和消融细节。

### 阅读优先级
**中**。理由：该论文聚焦前馈 3DGS 在多视角密集输入下的渲染效率瓶颈，问题定义清晰，两个设计点（细节感知重要性分数与质量感知剪枝）与“渲染预算”主题直接相关；摘要提到在 RE10K、DL3DV、ACID 上取得质量与效率的有利权衡，但未给出具体定量结果。若读者关注前馈 3DGS 的冗余基元控制与效率优化，本文具有较高相关性；若需要依据充分实验细节判断方法有效性，则需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting has recently emerged as a promising alternative to per-scene optimization, enabling fast novel view synthesis by predicting Gaussian primitives directly from input images. However, it quickly faces a bottleneck of rendering efficiency while scaling from sparse to dense multi-view inputs, which offer more geometric constraints but produce a rapidly growing set of candidate Gaussians. Existing solutions cannot reliably distinguish redundant primitives, leading to many redundant primitives from repeatedly observed regions and increased rendering cost without much gain in visual quality. We propose BudSplat, a compact feed-forward 3DGS framework that learns to keep the most valuable Gaussians under a limited primitive count. BudSplat has two novel designs. The first is a detail-aware importance score that is extracted from multi-level visual tokens, providing an explicit cue for regions where pruning is likely to harm perceptual quality. The score can be injected into voxel fusion to preserve high-value local contributors during multi-view aggregation. The second is quality-aware Gaussian pruning that selects a compact set of primitives by jointly considering rendering contribution and detail importance. The quality-aware pruning enables local quota redistribution that helps avoid over-allocating primitives to large redundant regions. Experiments on RE10K, DL3DV, and ACID show that BudSplat achieves a favorable trade-off among rendering quality and efficiency.

</details>

#### 2026-10-27 - Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation

**Authors:** Kaihua Chen, Yiming Gong, Deva Ramanan, Tarasha Khurana
**Links:** [abs](https://arxiv.org/abs/2610.37983) - [pdf](https://arxiv.org/pdf/2610.37983)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation
- 作者：Kaihua Chen, Yiming Gong, Deva Ramanan, Tarasha Khurana
- 出版日期：2026-10-27T21:28:33Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37983) / [PDF](https://arxiv.org/pdf/2610.37983)

### 一句话总结
论文提出将自回归生成（WanAR）与分层长上下文去噪（FixAR）结合的轻量框架，用于从单张图像生成相机可控的长视频，以缓解误差累积和相机控制歧义问题。

### 研究问题
论文面向“从单张图像进行长视频、相机可控生成”的任务。摘要指出主流的自回归范式存在两项关键限制：
1. 误差随时间累积：远处帧以先前生成的输出而非真实数据为条件，导致漂移；
2. 如何融入相机控制存在歧义。
摘要还指出，针对这两点的常见方案（如 self-forcing 与以显式 6-DOF 位姿为条件）要么带来显著计算开销，要么随时间产生场景几何漂移。

### 核心思路/方法
- 提出一个简单且轻量的框架，将自回归生成（WanAR）与分层长上下文去噪（FixAR）结合。
- 为使场景几何与输入相机保持一致，借鉴前馈式新视角合成，将视频生成重新表述为“变形加修复”（warping-and-inpainting）问题。
- 为缓解漂移，引入分层去噪策略，让不同阶段以不同的时间历史为条件：
  - 首先生成以紧邻过去为条件的帧；
  - 再用第二个去噪器，以时间上降采样的长程历史为条件进行细化，以增强全局一致性。
- 该由细到粗（fine-to-coarse）的方案使每个生成帧能够有效利用完整时间上下文，同时避免过高成本。

### 主要贡献
- 提出 WanAR+FixAR 的轻量框架，用于相机可控的长视频自回归生成。
- 将视频生成重构为 warping-and-inpainting 问题，以约束场景几何与输入相机一致。
- 引入分层去噪策略：先基于紧邻过去生成，再基于时间降采样的长程历史细化，以在可控成本下利用完整时间上下文。
- 摘要称在 RealEstate10k 与 DL3DV 上，WanAR+FixAR 优于先前相机可控长视频生成方法，结果在时间上稳定且与输入相机轨迹一致。

### 局限性
- 摘要仅给出方法概述与数据集层面的实验结论，未提供具体量化指标、消融实验、失败案例或计算开销的详细数据；这些细节“摘要未提供足够信息”。
- 摘要未说明方法在极端相机轨迹、复杂动态场景或更长视频长度下的表现；“摘要未提供足够信息”。
- 摘要未给出与基线方法的具体比较数值和实现细节；“摘要未提供足够信息”。

### 阅读优先级
中。理由：该论文针对相机可控长视频生成中的误差累积与相机控制歧义提出较清晰的轻量方案，并在两个常用数据集上给出优于先前方法的摘要性结论；但摘要未提供定量结果、消融与失败分析，需阅读全文才能判断方法有效性与适用范围。

</details>

<details>
<summary>Abstract</summary>

We address the task of long-video, camera-controlled generation from a single image. The dominant autoregressive paradigm suffers from two key limitations: (1) error accumulation over time, as distant frames are conditioned on previously generated outputs rather than ground truth, leading to drift; and (2) ambiguity in how to incorporate camera control. Standard solutions to both--such as self-forcing and conditioning on explicit 6-DOF poses--either incur significant computational overhead or produce drifting scene geometries over time. We propose a simple and lightweight framework that combines autoregressive generation (WanAR) with hierarchical long-context denoising (FixAR). To enforce scene geometry remains consistent with input cameras, we draw from feed-forward novel-view synthesis and reformulate video generation as a warping-and-inpainting problem. To mitigate drift, we introduce a hierarchical denoising strategy in which different stages condition on different temporal histories. Specifically, we first generate frames conditioned on the immediate past, and then refine them using a second denoiser conditioned on a temporally subsampled long-range history to enforce global consistency. This fine-to-coarse scheme enables each generated frame to effectively condition on the full temporal context without incurring a prohibitive cost. Experiments on RealEstate10k and DL3DV demonstrate that WanAR+FixAR outperforms prior methods for camera-controlled long-video generation, producing results that are both temporally stable and consistent with input camera trajectories.

</details>

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-02 - MoSoLoco: Monocular 3D Human Localization through Visual Latent Features and Social Context

**Authors:** Yasamin Borhani, Javad Khoramdel, Yang Gao, Po-Chien Luan, Alexandre Alahi
**Links:** [abs](https://arxiv.org/abs/2611.03189) - [pdf](https://arxiv.org/pdf/2611.03189)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, localization

<details>
<summary>Abstract</summary>

Estimating the metric 3D position of people from a monocular camera is important for robot navigation and motion prediction. Lightweight pose-based localizers are attractive for robotic hardware with limited computational resources because they operate on compact 2D keypoints. However, they typically discard the richer visual representations computed by the pose estimator. We introduce MoSoLoco, a per-frame monocular 3D human localizer that combines the pose detector's internal visual features with the detected 2D skeleton, without requiring an additional RGB or depth encoder. MoSoLoco can further incorporate sparse same-frame multi-person context to refine individual position estimates. Experiments on JRDB and NuScenes show that reusing pose-detector representations improves localization, reducing the best JRDB error by approximately 23 percent relative to the strongest evaluated keypoint-based baseline. A sparse social-interaction module incorporates nearby detections from the same image for further refinement. Controlled trajectory-forecasting experiments show downstream benefits, while the complete pipeline remains suitable for efficient Jetson AGX Xavier inference.

</details>

#### 2026-11-02 - ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation

**Authors:** Zhongkai Gu, Yang Liu, Wei Zhu, Mitsuhiro Hayashibe
**Links:** [abs](https://arxiv.org/abs/2611.02968) - [pdf](https://arxiv.org/pdf/2611.02968)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Contact transitions allow humanoid robots to redistribute object support across the whole body, enabling manipulation beyond hand-only grasps. Human videos provide a scalable source of such transitions for robots to learn from. However, body occlusion disrupts object pose tracking and corrupts retargeted motion. Moreover, accurately reproducing the object trajectory does not ensure that the robot applies stabilizing forces at the intended contacts, risking slips or drops in later phases. To address these challenges, we propose ReContact, which reconstructs and retargets human-object interactions through an object-centric contact plan. The plan specifies contact phases, contact pairs, anchors, pressing directions, and sticking or sliding modes. Contact priors stabilize object pose reconstruction through occlusion. A residual policy over a frozen whole-body tracker is rewarded for making contact at planned anchors with forces aligned to the specified directions. In simulation, on a thigh-supported regrasp task, ReContact achieves the planned two-palm bottom hold in 83.5 of episodes over three training seeds, versus 0.16% for the best adapted baseline. One policy trained on 247 references re-solved for new placements raises in-workspace tube-transfer success from 20.4% (source reference only) to 97.8%. On a real Unitree G1, policies execute seven contact-rich manipulation and two loco-manipulation tasks.

</details>

#### 2026-11-02 - Scaling Action-Free Video Latent Prediction for Transferable Representations in End-to-End Autonomous Driving

**Authors:** Xingtai Gui, Xubin Zhou, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan, Jianbing Shen
**Links:** [abs](https://arxiv.org/abs/2611.02853) - [pdf](https://arxiv.org/pdf/2611.02853)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

End-to-end autonomous driving policies require effective visual representations that capture both spatial scene structure and temporal dynamics. Video latent prediction has emerged as an effective paradigm for learning spatiotemporal visual representations, yet it remains unclear whether scaling this objective with action-free driving videos can yield representations that benefit end-to-end planning. We study action-free video latent prediction as a scalable pretraining objective and introduce ScaleDrive, a driving-oriented framework pretrained exclusively on large-scale internet open-world driving videos, without action annotations or benchmark-specific data. We keep the pretrained video encoder frozen during downstream end-to-end planning training to isolate the transferability of representations learned from internet driving videos. Ego-motion and depth probes show that scaling action-free video pretraining progressively strengthens the temporal and geometric information encoded in the frozen representation. We systematically study the visual representation transfer across different end-to-end driving policies and closed-loop benchmarks, where ScaleDrive consistently improves downstream performance and demonstrates that scaling action-free video latent prediction yields representations that generalize across both planning policy architectures and evaluation scenarios and protocols.

</details>

#### 2026-11-02 - HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation

**Authors:** Gyeonghun Kim, Donghoon Kim, Minsoo Choi, Suyun Lee
**Links:** [abs](https://arxiv.org/abs/2611.02660) - [pdf](https://arxiv.org/pdf/2611.02660)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>Abstract</summary>

Recent advances in Vision-Language-Action (VLA) models have enabled fine manipulation capabilities, yet performing tasks that require working memory remains a key challenge. Most existing VLA architectures operate under a Markovian assumption, mapping only the current observation to an action, which leads to failure in non-Markovian environments. Inspired by the human 'inner monologue', we propose Hierarchical Explicit Language Memory (HeLM), a hierarchical VLA framework that maintains task-relevant history in explicit language through factorized event detection and event-triggered memory updates. We evaluate HeLM across 10 non-Markovian real-world tasks with 56 variants, including five newly formulated inter-episode tasks that require persistent context across task boundaries. HeLM improves intra-episode success by 12.8 percentage points over the strongest baseline and achieves 78% subtask success on compositional generalization tasks, while using up to 4.5x less memory and running 2.5x faster than the keyframe baseline at long horizons.

</details>

#### 2026-11-02 - Interactive 3D Cutaway Visualization for Subsurface Target Localization in Robot-Assisted Surgery

**Authors:** Yuxin Chen, Wenxuan Wang, Wanwen Chen, Qi Zeng, Septimiu E. Salcudean
**Links:** [abs](https://arxiv.org/abs/2611.02537) - [pdf](https://arxiv.org/pdf/2611.02537)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, AR, augmented reality

<details>
<summary>Abstract</summary>

Purpose: Blended augmented reality (AR) overlays can provide ambiguous depth cues in which subsurface anatomy floats above the tissue surface. We investigate whether an interactive 3D cutaway visualization can improve robot-assisted target localization. Methods: We propose Virtual Box, an interactive 3D cutaway interface that allows users to independently manipulate the viewing perspective to inspect subsurface targets. In a controlled, counterbalanced within-subject tissue phantom study, 15 engineering students used Virtual Box and a depth-enhanced blended AR overlay to position a da Vinci instrument at virtual targets in a water tank. We used registered 3D transrectal ultrasound to measure 3D localization error and depth error. We also collected completion time and subjective ratings. Results: Virtual Box reduced mean 3D error from 12.92 to 4.96 mm (61.6% reduction) and depth error from 9.48 to 2.07 mm (78.2% reduction; both p < 0.001). Spatial understanding, depth perception, and confidence ratings were higher (all unadjusted p < 0.001), but completion time increased from 21.64 to 32.58 s (p = 0.008). Overall workload did not differ significantly. Conclusion: Virtual Box improved localization accuracy and perceived spatial understanding in this controlled task, with additional completion time, supporting further evaluation for surgical navigation.

</details>

#### 2026-11-02 - AgiWorld: An Agentic Video World Model for Building Persistent Worlds

**Authors:** Shaoheng Fang, Yiqun Mei, Hanwen Jiang, Xin Sun, Haitian Zheng, Hao Tan, Kalyan Sunkavalli, Georgios Pavlakos, Qixing Huang, Yiwei Hu
**Links:** [abs](https://arxiv.org/abs/2611.02341) - [pdf](https://arxiv.org/pdf/2611.02341)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>Abstract</summary>

Recent interactive video world models generate visually compelling videos from a single image, following user-provided camera motion and text prompts. However, such low-level control demands substantial user effort to realize a high-level intent, and the generated world struggles to remain persistent as the exploration proceeds. In this work, we present AgiWorld, an agentic video world model that explores and builds a persistent world from a single image and a free-form instruction. For high-level planning, our agent AgiWorld-Agent designs the world and the journey through it in a world state and directs the exploration. For low-level realization, our video world model AgiWorld-WM generates the video chunk by chunk and stores it with its geometry in a spatial memory, from which the agent updates its world state. This closed loop keeps the world faithful to the user's intent and keeps the agent's world state consistent with the generated content throughout the exploration. We co-design the two levels around the shared spatial memory and an interface of metric camera trajectories and structured prompts. In AgiWorld-WM, to handle occlusion and accumulated geometric errors in the spatial memory over long rollouts, we propose occlusion-aware history selection, which retrieves past views by surface visibility, and reliability-based memory maintenance, which prefers reliable geometry and earlier observations. AgiWorld-WM achieves state-of-the-art overall performance on world revisiting and exploration benchmarks, and qualitative results and ablations show that AgiWorld builds persistent worlds from free-form instructions over minute-long journeys. Persistence thus arises not from the video model alone but from its closed loop with the agent.

</details>

#### 2026-11-01 - GoalDex: Learning Image-Goal-Conditioned Policies for Dexterous In-Hand Manipulation

**Authors:** Arjun Bhardwaj, Mayank Mittal, Maximum Wilder-Smith, Vaishakh Patil, Marco Hutter
**Links:** [abs](https://arxiv.org/abs/2611.02171) - [pdf](https://arxiv.org/pdf/2611.02171)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation, simulation

<details>
<summary>Abstract</summary>

Dexterous in-hand manipulation is commonly formulated around explicit object pose estimation, yet reliable pose tracking is challenging under severe hand-object occlusions and often requires object-specific supervision. This dependence creates a bottleneck between perception and control that can limit robustness and scalability. We present an end-to-end visuomotor framework for dexterous in-hand reorientation that operates on RGB observations and proprioception without intermediate pose estimation. Our approach jointly learns visual representations and control policies through behavior distillation from privileged state teachers and auxiliary reconstruction objectives. Furthermore, we introduce image-goal-conditioned reorientation, allowing desired object configurations to be specified directly through images rather than canonical pose representations. We evaluate our approach across a diverse set of object geometries and instances in simulation, where it consistently outperforms pose-based methods and policies built on pretrained visual encoders. Finally, we demonstrate direct sim-to-real transfer of a single image-goal-conditioned policy across five real-world objects, showing that accurate dexterous reorientation can be achieved without explicit pose estimation. For videos and code release, please refer to the project website: https://rffr.leggedrobotics.com/works/goaldex/

</details>

#### 2026-11-01 - Reconstruction as Spatial Evaluation: Diagnosing Cross-View Spatial Intelligence in Large Vision-Language Models

**Authors:** Junfei Wu, Qiuyue Wang, Xuhong Huang, Qihang Peng, Mingsheng Li, Jian Guan, Qiang Liu, Shu Wu, Liang Wang, Shuai Bai, Tieniu Tan
**Links:** [abs](https://arxiv.org/abs/2611.02026) - [pdf](https://arxiv.org/pdf/2611.02026)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, spatial intelligence

<details>
<summary>Abstract</summary>

The spatial intelligence of large vision-language models (LVLMs) requires the ability to combine local visual observations into a geometrically consistent representation of the physical world. Many static benchmarks assess isolated spatial judgments, such as relative direction or distance, while interactive embodied evaluations combine perception with exploration, planning, control, and simulator-specific execution. To bridge this gap, we introduce RECONSPATIAL, a benchmark centered on multi-view 3D scene reconstruction across indoor, tabletop, and outdoor environments. Given real multi-view images and target-object queries, LVLMs are required to jointly predict oriented 3D bounding boxes in a shared, camera-anchored metric coordinate frame. Reconstructions are evaluated along two complementary axes: Structure for relative layout and Metric for physical scale and camera-anchored placement. Nine atomic spatial QA tasks, grouped into Geometric Perception and Spatial Relations, probe spatial capabilities involved in joint reconstruction. Offline navigation extends evaluation to path planning. Evaluation of 18 frontier LVLMs reveals a consistent gap between relative scene structure and metric reconstruction; even GPT-6-Astra scores 81.4% on Structure but only 58.7% on Metric. Tracing this gap, diagnostic analyses link atomic spatial capabilities to reconstruction quality and show that relational consistency alone does not ensure metric accuracy. Experiments with 3D map injection further separate scene construction from path planning, revealing how these geometric errors limit navigation success. Finally, spatial fine-tuning yields broad transfer across both spatial and general vision-language benchmarks.

</details>

#### 2026-11-01 - OCBI: Order-Sensitive Cross-Branch Interaction for Image Manipulation Localization

**Authors:** Zhouli Yu
**Links:** [abs](https://arxiv.org/abs/2611.01783) - [pdf](https://arxiv.org/pdf/2611.01783)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>Abstract</summary>

Image manipulation localization combines semantic structure with forensic traces to identify modified pixels. Within-branch spatial mixing and RGB-guided cross-branch mixing can produce different messages when composed in opposite orders. We propose OCBI, an extension of Co-Transformers that models the discrepancy between these two composition orders for localization. A local cross-branch fusion module uses the commutator of RGB-guided cross-attention and forensic self-attention to add a learnable signed correction to feature transfer. Pixelwise adaptive multiscale aggregation then combines spatial contexts before prediction. OCBI uses the Co-Transformers backbone and supervision. We compare OCBI with retrained Co-Transformers using CASIA-only task training, a 50-epoch budget, and final-epoch evaluation. Across five clean test datasets, OCBI achieves a macro PixelF1 of 0.5773, exceeding the baseline by 0.43 percentage points. Under JPEG compression, Gaussian blur, and resizing on three datasets, its average PixelF1 over 21 dataset-transformation conditions exceeds the baseline by 0.95 percentage points.

</details>

#### 2026-11-01 - SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts

**Authors:** Amir Hossain Raj, Xuesu Xiao
**Links:** [abs](https://arxiv.org/abs/2611.01600) - [pdf](https://arxiv.org/pdf/2611.01600)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, manipulation, world model

<details>
<summary>Abstract</summary>

Robots manipulating in cluttered spaces must often plan from partial views where foreground objects occlude the target, surrounding geometry, and usable free space. Reactive policies often miss these hidden constraints, while exhaustive search becomes computationally prohibitive in dense clutter. We present SCOUT, an occlusion-aware planning framework that bridges high-level deliberation with grounded physical rollouts. SCOUT leverages an object-centric scene representation to reconstruct hidden geometry and derive a relational planning state capturing blocker hierarchies and accessibility corridors. To navigate the vast action space in clutter, an LLM proposes structured action candidates which are then rigorously evaluated via Monte Carlo Tree Search (MCTS) using a learned action-conditioned world model. Evaluations on 'Reveal' and 'Placement' tasks show that SCOUT outperforms Vision-Language-Action (VLA) policies, embodied agents, and 3D world models, with significant gains in long-horizon tasks requiring reasoning over occluded geometry. We further validate the framework's robustness through real-world robotic manipulation in a cluttered shelf environment.

</details>

### 2026-10

#### 2026-10-31 - Shades of Success: Evaluating Manipulation Quality from Object-Centric Constraints

**Authors:** Lorena Maria Genua, Sarvesh Prajapati, Ananya Trivedi, Taskin Padir
**Links:** [abs](https://arxiv.org/abs/2611.01250) - [pdf](https://arxiv.org/pdf/2611.01250)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

As learned manipulation policies become increasingly capable of solving practical manipulation tasks, assessing how well a task is performed becomes a fundamental challenge. While binary labels confirm task success, they cannot distinguish successful executions with different levels of geometric precision. To address this, we introduce SPECTRA, an object-centric framework for quantifying execution quality in manipulation of rigid objects. From a small set of oracle demonstrations generated in simulation, SPECTRA represents object interactions through progress-aligned relative poses. SPECTRA identifies which relative-pose directions are constrained and their admissible variations from demonstrations. These constraints establish a reference for evaluating robotic manipulation tasks. To score an unseen execution, deviations beyond the admissible variation are summarized by a Task Quality Index Q in [0,1]. Across seven simulated tasks, SPECTRA recovers constraints with 94% accuracy using 30 demonstrations per task. On rollouts from three learned policies, its scores achieve pooled Spearman correlations with human judgments of p=0.81 over all rollouts and p=0.61 among successful rollouts, exceeding all baselines in both subsets. Using the task reference learned in simulation, we use SPECTRA to select the highest-scoring demonstrations for training a diffusion policy on hardware. Exploratory results show higher success rate than training on randomly selected demonstrations.

</details>

#### 2026-10-29 - A Unified Benchmark for Aerial-Enhanced Autonomous Driving: The KITScenes Aerial Dataset

**Authors:** Daniel Lengerer, Richard Schwarzkopf, Jonas Merkert, Fabian Immel, Rupert Polley, Frank Bieder, Jan-Hendrik Pauls, J. Marius Zöllner, Klaus Bogenberger, Christoph Stiller, Carsten Markgraf
**Links:** [abs](https://arxiv.org/abs/2610.40455) - [pdf](https://arxiv.org/pdf/2610.40455)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** feature matching, autonomous driving, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Unified Benchmark for Aerial-Enhanced Autonomous Driving: The KITScenes Aerial Dataset
- 作者：Daniel Lengerer, Richard Schwarzkopf, Jonas Merkert, Fabian Immel, Rupert Polley, Frank Bieder, Jan-Hendrik Pauls, J. Marius Zöllner, Klaus Bogenberger, Christoph Stiller, Carsten Markgraf
- 出版日期：2026-10-29T17:01:30Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.40455) / [PDF](https://arxiv.org/pdf/2610.40455)

### 一句话总结
论文提出 KITScenes Aerial 数据集，在 KITScenes 多模态数据基础上增加空间关联的航空影像与更高分辨率神经表征，为空中辅助建图与跨视角定位等任务提供统一基准。

### 研究问题
摘要指出，航空影像能够提供车载传感器感知范围之外的道路结构信息，但基于航空影像的地图构建、空中辅助在线 HD 建图以及跨视角定位通常分别在独立的数据与基准上研究，缺乏统一的数据基础与评测平台。

### 核心思路/方法
KITScenes Aerial 作为 KITScenes Multimodal 数据集的扩展，将同步车载传感器数据、车辆位姿和 Lanelet2 地图标注与空间关联的航空影像及更高分辨率神经表征结合，形成面向多种研究任务的共同基础。建图评测覆盖全部 53 个 KITScenes 地图类别，并在不同模型设计、空间范围与航空影像分辨率下评估，同时保持与常用三类设置的兼容性。跨视角定位在地理上不重叠的条件下评估，并使用经适配的细粒度特征匹配基线。

### 主要贡献
- 构建 KITScenes Aerial，将航空影像与车载多模态数据、位姿及 Lanelet2 地图标注进行空间关联，并提供更高分辨率神经表征。
- 建立覆盖 53 类地图要素的统一建图评测，兼容三类设置，并考察模型设计、空间范围和航空分辨率的影响。
- 基线结果显示，航空上下文对细粒度与扩展范围建图尤其有益，在更大建图范围下 53 类 mAP 提升超过一倍；更高分辨率航空影像进一步带来 4.3 mAP（+24%）提升，增益扩展到交通灯等困难地图要素。
- 在地理不重叠条件下评估跨视角定位，适配的细粒度特征匹配基线取得 5.13 m 平均平移误差。

### 局限性
摘要未提供足够信息说明数据集规模、采集区域数量、传感器配置细节、基线模型完整列表、计算成本、失败案例或方法在真实部署中的限制。

### 阅读优先级
高。理由：该工作面向航空辅助自动驾驶的统一基准，直接涉及建图与跨视角定位两类关键任务，并给出明确的定量基线结果；若关注空中—地面跨视角感知、HD 地图构建或相关基准建设，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Aerial imagery provides complementary spatial context for autonomous driving by exposing road structure beyond the immediate perception range of onboard sensors. Yet map construction from aerial imagery, aerial-assisted online HD mapping, and cross-view localization are typically studied on separate data and benchmarks. We introduce KITScenes Aerial, an extension of the KITScenes Multimodal dataset that augments synchronized onboard sensor data, vehicle poses, and rich Lanelet2 map annotations with spatially associated aerial imagery and higher-resolution neural representations, providing a common basis for a variety of research tasks. Our mapping evaluation focuses on all 53 KITScenes map classes across different model designs, spatial ranges, and aerial resolutions, while retaining compatibility with the widely used three-class setting. Representative baselines show that aerial context is particularly beneficial for fine-grained and extended-range mapping, more than doubling 53-class mAP at the larger mapping extent. Higher-resolution aerial imagery yields a further 4.3 mAP (+24 %) improvement, with gains extending to challenging map elements such as traffic lights. We additionally evaluate cross-view localization under geographically disjoint conditions, where an adapted fine-grained feature-matching baseline achieves a mean translation error of 5.13 m. KITScenes Aerial thus enables unified study of aerial and ground-level information across complementary mapping and localization tasks. Project page: https://kitscenes.com/aerial

</details>

#### 2026-10-29 - Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design

**Authors:** Jingxu Gu, Dongze Lian
**Links:** [abs](https://arxiv.org/abs/2610.40430) - [pdf](https://arxiv.org/pdf/2610.40430)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design
- 作者：Jingxu Gu, Dongze Lian
- 出版日期：2026-10-29T16:51:45Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.40430

### 一句话总结
DEED 通过结构化演示扩展与执行设计，将预训练视觉-语言-动作策略适配到 MetaFine 的五个细粒度操作任务，官方 Overall 得分为 85.55%。

### 研究问题
细粒度操作要求机器人策略既能遵循指令，又对视觉变化保持稳健，并能把预测动作转化为精确的机器人控制。论文关注如何将预训练视觉-语言-动作策略适配到 MetaFine 的五个任务，以提升细粒度操作表现。

### 核心思路/方法
DEED 包含两部分：演示扩展与执行设计。演示扩展方面，DEED 针对同一初始场景下不同指令生成演示，并在保持原始状态与动作目标不变的前提下，用不同相机位置和光照条件渲染每条物理轨迹；在监督适配过程中采用分层采样策略，平衡指令、轨迹和视觉条件。执行设计方面，部署时将预测的动作块通过逆运动学、按任务选择的夹爪映射以及闭环重规划转换为机器人命令。

### 主要贡献
- 提出 DEED 框架，通过结构化演示扩展和执行设计，将预训练视觉-语言-动作策略适配到 MetaFine 的五个细粒度操作任务。
- 演示扩展在同一初始场景下覆盖不同指令，并对同一物理轨迹进行多相机位置与多光照条件渲染，同时保持原始状态和动作目标不变。
- 采用分层采样策略在监督适配中平衡指令、轨迹与视觉条件。
- 部署阶段结合逆运动学、任务特定夹爪映射和闭环重规划，将预测动作块转换为机器人命令。
- 官方 Overall 得分为 85.55%；固定策略评估显示性能随执行时域、去噪预算和夹爪映射变化。

### 局限性
摘要未提供足够信息。摘要未说明各任务的分项得分、消融实验细节、计算成本、失败案例、与基线方法的完整对比，以及固定策略评估中执行时域、去噪预算和夹爪映射变化的具体幅度与最优设置。

### 阅读优先级
中。理由：论文给出明确的框架组成和官方 Overall 得分，且涉及预训练视觉-语言-动作策略的演示扩展与部署执行设计，对细粒度机器人操作方向有参考价值；但摘要未提供分项结果、消融细节和失败分析，需阅读全文后才能判断方法增益来源与泛化边界。

</details>

<details>
<summary>Abstract</summary>

Fine-grained manipulation requires a robot policy to follow instructions, remain robust to visual variations, and translate predicted actions into precise robot control. We present Demonstration Expansion and Execution Design (DEED), a framework for adapting a pretrained vision-language-action policy to the five MetaFine tasks through structured demonstration expansion and execution design. DEED generates demonstrations for different instructions from the same initial scene and renders each physical trajectory under different camera positions and lighting conditions while preserving its original states and action targets. A hierarchical sampling strategy balances instructions, trajectories, and visual conditions during supervised adaptation. At deployment, DEED converts predicted action chunks into robot commands using inverse kinematics, gripper mappings selected for each task, and closed-loop replanning. DEED achieves an official Overall score of 85.55%. Fixed-policy evaluations show that performance varies with execution horizon, denoising budget, and gripper mapping.

</details>

#### 2026-10-29 - Decision-Level Error Attribution and Depth-Aware Safety Evaluation of Monocular RGB Human Tracking for Autonomous Robot Navigation

**Authors:** Abdulahi Taiwo, Chijioke Cyriacus Ekechi
**Links:** [abs](https://arxiv.org/abs/2610.40199) - [pdf](https://arxiv.org/pdf/2610.40199)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Decision-Level Error Attribution and Depth-Aware Safety Evaluation of Monocular RGB Human Tracking for Autonomous Robot Navigation
- 作者：Abdulahi Taiwo, Chijioke Cyriacus Ekechi
- 出版日期：2026-10-29T14:52:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.40199；PDF https://arxiv.org/pdf/2610.40199

### 一句话总结
论文针对单目 RGB 人体跟踪在自主机器人靠近人时的停止/继续决策，提出决策级误差归因与深度感知安全评估，分离安全规则与感知误差对漏检危险和多余停止的贡献。

### 研究问题
单目 RGB 跟踪对靠近人的机器人有用，但感知误差对二元停止/继续决策的影响，无法被几何精度指标充分刻画。论文要回答：决策错误中有多少来自安全规则本身、多少来自感知；并进一步区分漏检与定位误差的作用。摘要还指出，仅使用横向距离的规则在位置准确时不会漏掉平面距离规则能识别的危险，但会产生不必要的停止。

### 核心思路/方法
- 证明仅横向距离是平面距离的下界：位置准确时不会漏掉平面规则识别的危险，但会带来多余停止。
- 提出双因素 Shapley 归因，将规则贡献与感知贡献分开，并进一步区分漏检与定位错误。
- 实验使用 ETH 与 UCY 行人视频、模拟静止机器人、互不重叠的标定与评估行人、时间块 bootstrap 区间。
- 在 RGB 感知部分，比较标定后的地平面定位与几何基线、以及标定的 Depth Anything V2；并评估检测召回与安全裕量对决策的影响。

### 主要贡献
- 给出横向距离规则相对平面距离规则的下界性质，说明其安全性与多余停止之间的取舍。
- 引入双因素 Shapley 归因，用于在决策层分离安全规则与感知误差的贡献，并区分漏检与定位误差。
- 在 898 名行人、三个场景上报告：横向规则在标注位置上未漏掉危险，但停止精确率仅 5.6–31.9%。
- 在两个场景的 RGB 感知中，标定地平面定位的平面 RMSE 为 0.59 m 和 0.51 m；几何基线为 1.72 m 和 1.39 m；标定 Depth Anything V2 为 0.81 m 和 0.68 m。
- 检测召回 0.43 和 0.26，使漏检成为漏掉危险的主要来源。
- 使用两倍标准差安全裕量配合地平面定位，在全部八个场景-阈值设置中漏危率匹配或优于横向规则，并在七个设置中减少多余停止。

### 局限性
- 摘要明确说明所有机器人交互均为模拟，结果是离线决策分类，并非碰撞避免的演示。
- 实验范围为 ETH 与 UCY 行人视频、三个场景、模拟静止机器人；摘要未提供更多场景、机器人运动或真实部署信息。
- 摘要未提供检测器类型、跟踪方法细节、阈值设置的具体数值、计算成本或实时性信息。
- 摘要未提供与其他决策级归因方法的对比细节。
- 摘要未提供关于 Depth Anything V2 标定流程、失败案例或不同光照/遮挡条件的充分信息。
- 摘要未提供足够信息说明方法在非行人目标、动态机器人平台或不同安全规则下的泛化能力。

### 阅读优先级
中。理由：论文聚焦决策级误差归因与安全评估，对单目 RGB 人体跟踪在机器人导航中的安全规则与感知误差分离有明确方法贡献，并给出定量结果；但摘要显示实验为离线模拟决策分类、场景数量有限，且未提供真实机器人部署或碰撞避免演示。若关注机器人近人安全决策与感知误差归因，值得阅读；若需要真实系统验证或完整实验细节，需进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

Monocular RGB tracking is useful for robots operating near people, but perception errors affect binary stop/proceed decisions in ways that geometric accuracy metrics do not capture. We examine how much decision error arises from the safety rule versus perception. We prove that lateral-only distance is a lower bound on planar distance: with accurate positions, it cannot miss dangers identified by the planar rule, but it produces unnecessary stops. We introduce a two-factor Shapley attribution separating rule and perception contributions, and further distinguish missed detections from localization errors. Experiments use ETH and UCY pedestrian videos with simulated stationary robots, disjoint calibration and evaluation pedestrians, and time-block bootstrap intervals. Across 898 pedestrians in three scenes, the lateral rule missed no dangers on annotated positions but achieved only 5.6-31.9% stop precision. In two scenes with RGB perception, calibrated ground-plane localization achieved 0.59 m and 0.51 m planar RMSE, compared with 1.72 m and 1.39 m for a geometric baseline and 0.81 m and 0.68 m for calibrated Depth Anything V2. Detection recall of 0.43 and 0.26 made missed detections the leading source of missed danger. A two-standard-deviation safety margin with ground-plane localization matched or improved on the lateral rule's missed-danger rate in all eight scene-threshold settings and reduced unnecessary stops in seven. All robot interactions are simulated, and outcomes are offline decision classifications, not demonstrations of collision avoidance.

</details>

#### 2026-10-29 - AFast Robot Localization Method Based on Monte Carlo Sampling

**Authors:** He Zhaoqing, Hang Li, Xian Pu, Li Wang
**Links:** [abs](https://arxiv.org/abs/2610.39708) - [pdf](https://arxiv.org/pdf/2610.39708)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AFast Robot Localization Method Based on Monte Carlo Sampling
- 作者：He Zhaoqing, Hang Li, Xian Pu, Li Wang
- 出版日期：2026-10-29T09:44:11Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.39708) / [PDF](https://arxiv.org/pdf/2610.39708)

### 一句话总结
该论文提出一种基于蒙特卡洛采样的在线粒子滤波定位方法，仅依靠机器人前、后、左、右四个测距传感器，在无外部定位系统且不使用航向信息的迷宫环境中实现移动机器人定位。

### 研究问题
论文关注的问题：在真实世界的受限环境中，机器人往往无法依赖外部定位系统；因此需要一种不依赖外部定位基础设施的机器人自主定位方法。论文将方法应用于迷宫环境中的移动机器人定位。

### 核心思路/方法
- 采用基于蒙特卡洛采样的在线粒子滤波定位方法。
- 仅使用安装在车体前、后、左、右四个方向的测距传感器。
- 不需要任何航向信息（heading information）。
- 应用场景为迷宫环境中的移动机器人定位。
- 通过仿真实验验证方法效果。

### 主要贡献
- 提出一种面向受限环境的在线粒子滤波机器人定位方法。
- 展示仅靠四个测距传感器、无需航向信息即可进行定位的可行性。
- 摘要称仿真实验表明，即使在局部区域高度相似的迷宫中，车辆仍能实现相对准确的定位，为复杂环境中的机器人定位提供快速有效的方法。

### 局限性
- 论文输入仅提供摘要，未提供具体实验设置、传感器参数、粒子数、定位精度指标、对比方法等信息；这些内容“摘要未提供足够信息”。
- 验证仅提及仿真实验，真实机器人实验情况“摘要未提供足够信息”。
- 方法在局部区域高度相似迷宫中的具体失败情形、计算开销和实时性量化结果“摘要未提供足够信息”。
- 仅使用四个测距传感器且不使用航向信息，在更复杂或动态环境中的泛化能力“摘要未提供足够信息”。

### 阅读优先级
**中**。理由：该论文主题属于机器人自主定位与粒子滤波的实用方向，且约束条件明确（四向测距、无航向信息、迷宫环境），对受限环境定位研究有参考价值；但当前仅有摘要，缺少实验细节和量化结果，需阅读全文后才能判断其方法新颖性与实际效果。

</details>

<details>
<summary>Abstract</summary>

Localization is an essential capability of intelligent robots. However, in real-world constrained environments, robots often cannot rely on external localization systems. Therefore, this paper proposes an online particle-filter localization method based on Monte Carlo sampling. The method is applied to the localization of a mobile robot in a maze environment and requires only four range sensors mounted on the front, rear, left, and right sides of the vehicle, without the need for any heading information. Simulation experiments demonstrate that even in a maze where local regions are highly similar, the vehicle can still achieve relatively accurate localization, thereby providing a fast and effective approach for robot localization in complex environments.

</details>

#### 2026-10-29 - Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling

**Authors:** Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li, Chengzhi Zhao, Hexiang Wei, Lin Shao
**Links:** [abs](https://arxiv.org/abs/2610.39232) - [pdf](https://arxiv.org/pdf/2610.39232)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling
- 作者：Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li, Chengzhi Zhao, Hexiang Wei, Lin Shao
- 出版日期：2026-10-29T02:50:17Z
- 分类：Embodied / Robotics / AR Applications（无二级分类信息）
- 链接：[摘要](https://arxiv.org/abs/2610.39232) / [PDF](https://arxiv.org/pdf/2610.39232)

### 一句话总结
GenSight 将未来视频生成与稠密 4D 感知统一到同一个预训练视频扩散 Transformer 中，用共享的时空表示和预测空间联合建模外观、几何、语义与运动。

### 研究问题
具身世界模型不仅需要“想象”合理的未来，还需要“感知”演化世界中的几何、语义和运动结构。论文关注如何避免为视频生成与多种稠密感知任务分别构建模态专用流水线，并在统一表示中耦合这些能力。

### 核心思路/方法
- 构建统一具身世界模型 GenSight，基于单一预训练视频扩散 Transformer（DiT）骨干。
- 采用统一的时空表示覆盖视频、深度、具身分割和相对首帧的 2D 光流。
- 在共享 DiT 骨干上使用轻量任务调制，在同一架构内预测所有模态。
- 所有任务在统一的速度预测空间中联合优化。
- 推理支持两种互补模式：多步未来视频生成并输出对齐的稠密预测；从观测视频进行单步稠密感知。
- 通过统一模态表示、模型架构和预测空间，促进跨模态一致性，并使稠密感知受益于视频生成学习到的时空先验。
- 训练数据为涵盖多种机器人具身与人类手部交互的具身操作数据。

### 主要贡献
- 提出统一的具身世界模型，将未来视频生成与稠密 4D 感知整合进同一预训练视频扩散 Transformer。
- 以统一时空表示、轻量任务调制和统一速度预测空间，替代模态专用流水线。
- 支持多步未来生成与单步稠密感知两种推理模式。
- 摘要称其在视频生成和稠密 4D 感知上均表现良好，体现“看与想象统一”的有效性。

### 局限性
摘要未提供足够信息。未给出具体实验指标、失败案例、计算成本、推理效率、数据规模、泛化到未见具身或场景的评估，以及各任务之间的潜在冲突分析。

### 阅读优先级
中。理由：论文主题与具身世界模型、视频生成和 4D 感知的统一建模直接相关，方法思路清晰；但当前仅有摘要与元数据，缺少定量结果和实验细节，需阅读全文后才能判断其实际效果与可复现性。

</details>

<details>
<summary>Abstract</summary>

Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world. We present GenSight, a unified embodied world model that brings future video generation and dense perception into a single pretrained video diffusion transformer. GenSight uses a unified spatiotemporal representation for video, depth, embodiment segmentation, and first-frame-relative 2D flow. Built on a shared DiT backbone, GenSight uses lightweight task modulation to predict all modalities within the same architecture. All tasks are jointly optimized within a unified velocity prediction space. At inference, GenSight supports two complementary modes: multi-step future video generation with aligned dense predictions and single-step dense perception from an observed video. By unifying modality representation, model architecture, and prediction space, GenSight avoids separate modality-specific pipelines and couples appearance, geometry, semantics, and motion in a shared representation. It promotes cross-modal consistency and allows dense perception to benefit from the spatiotemporal priors learned through video generation. Trained on embodied manipulation data spanning multiple robot embodiments and human-hand interactions, GenSight demonstrates strong performance in both video generation and dense 4D perception, highlighting the effectiveness of unifying seeing and imagining for embodied world modeling.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
