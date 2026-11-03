# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：55
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 19
  - Embodied / Robotics / AR Applications: 16
  - Neural Scene Representations & Rendering: 14
  - Dynamic / 4D Reconstruction: 4
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“事件/多传感器补偿帧相机物理极限”成为动态重建主线。** HIVE-Diff 用事件流弥补单帧 LDR 在时间分辨率与动态范围上的不足，MISLAM 用磁-惯性替代在粉尘、烟尘、低照度下退化的视觉/激光，GPU-Native 系统用多路 RGB-D 做实时带纹理网格化。三者共同反映：当单一模态受物理约束（曝光、能见度、计算带宽）时，研究重心转向**跨模态互补与紧耦合融合**，而非单模态精度堆叠。

2. **3DGS 从“能渲染”走向“可诊断、可约束、可前馈”。** GaussFlaw 构建首个 3DGS 细粒度伪影数据集与标签体系，Neural-Color-Fields-3DGS 用连续神经颜色场与 Lipschitz 约束抑制漂浮物、改善深度，OctreeSplat 用八叉树引导前馈高斯原语按局部复杂度分配密度。方向从“提升 PSNR”转向**伪影可解释性、几何正则化与前馈化**三条并行的工程化路线。

3. **无靶标、无标注的标定与位姿估计集中出现。** SyncHeC（免标记手眼标定 + 可微渲染 + 连续时间联合优化）、AnchorHEC（腕部 + 固定相机统一无靶标标定）、ReVA-HPE（单张无标注注册图重建虚拟锚点，摆脱锚点真值姿态依赖）三篇同日出现，说明**“用可微渲染/生成先验替代物理靶标与人工标注”**正在成为机器人视觉标定的主流替代范式。

4. **视频/世界模型开始承担“表征预训练 + 长时一致性”双重角色。** ScaleDrive 验证无动作视频潜变量预测规模化后可为端到端自动驾驶提供可迁移表征（冻结编码器做隔离验证）；AgiWorld 用智能体规划 + 视频世界模型 + 空间记忆闭环，从单图与自由指令构建持久世界。二者分别从**表征可迁移性**与**世界持久性**切入，指向视频生成模型作为具身智能基础设施的趋势。

5. **人体/操作类任务从“关节回归”转向“接触、上下文与轻量化部署”。** ReContact 以物体为中心接触计划（接触阶段、接触对、按压方向、粘滑模式）驱动人形机器人重定向；HeLM 用显式语言记忆突破 VLA 的马尔可夫假设；MoSoLoco 复用姿态检测器内部视觉特征做轻量 3D 人体定位（JRDB 误差降约 23%）；MuCHMDPoser 用外部多视角 RGB 补足 VR 稀疏传感器欠约束。共性是**显式结构化先验（接触、记忆、特征复用、多视角）替代纯端到端黑箱**。

#### 技术路线观察

- **几何基础模型：从“特征提取器”升级为“可微几何先验供应商”。** OctreeSplat 冻结 VFM 提取多视角特征与几何先验做八叉树致密化；LieVLM 用 VGGT 几何 token 预测 SO(3) 局部旋转与路由系数，缓解视角诱导语义漂移；AnchorHEC 用共享 3D 基础模型重建初始化两类相机。VFM 正从下游模块的“输入”变为**标定、稠密化与视角鲁棒性的约束源**。

- **3D/4D 重建：动态与静态两条线分化明显。** 动态侧（HIVE-Diff 单参考 HDR 时间扩展、DynaCell 3D 时间序列虚拟染色评估）强调**时间维度上的监督稀缺**——前者靠合成数据 + 教师-学生蒸馏迁移到真实事件域，后者暴露体积时序虚拟染色缺乏统一评测的问题。静态侧（GPU-Native、OctreeSplat、Neural-Color-Fields-3DGS）则聚焦**实时性、几何细节与伪影可控**，路线从 TSDF 全 GPU 常驻到前馈高斯再到连续颜色场约束，呈现“工程管线优化”与“表示学习正则化”并进。

- **神经场景表示：约束设计比表征形式更受关注。** 同日三篇 3DGS 相关工作分别从数据（GaussFlaw-80K 的像素级掩码 + 八类缺陷标签）、连续性（Lipschitz 约束神经颜色场）、空间自适应（八叉树致密化分数）三个正交维度施加约束，说明 3DGS 的表征红利趋于饱和，**约束与诊断工具**成为新的贡献点。

- **机器人/AR 应用：标定与交互接口成为瓶颈环节。** SyncHeC 把延迟作为可微变量联合优化（7-DoF 臂 6.5 s 运动达 0.21 cm 平移误差、2.7 ms 延迟误差）；AnchorHEC 统一腕部与固定相机；MuCHMDPoser 用一次性无标记 HMD-相机标定 + 多视角 RGB 达到 60 FPS；Interactive 3D Cutaway 用可交互剖切把 3D 定位误差从 12.92 mm 降至 4.96 mm。这些工作共同表明：**部署侧误差的主要来源正从感知模型精度转移到时空标定与可视化接口设计**。

- **数据与评测缺口被显式提出。** GaussFlaw-80K（80,049 个伪影区域）、DynaCell（3 种细胞、2 种显微镜、4 种细胞器、3 种扰动）、以及 Fitness 姿态评测（TCPFormer、PoseMamba-L、MVGFormer 在 Fit3D 上统一对比），反映社区开始**为细分场景建立可复现的评测基线**，而非继续在通用 benchmark 上刷点。

#### 值得优先阅读的论文

1. **HIVE-Diff（2611.03465）**——提出“单参考 HDR 时间扩展”这一新任务定义，且给出合成训练 + 教师-学生蒸馏应对真实 HDR-事件配对稀缺的完整方案，对事件相机 + 生成模型交叉方向有直接参考价值。
2. **OctreeSplat（2611.02658）**——前馈 3DGS 的空间自适应原语分配是当前 3DGS 工程化的关键问题，其“冻结 VFM + 八叉树 + 随机实体体积渲染 + 可选 TTO”的组合对该方向研究者信息密度高。
3. **SyncHeC（2611.02999）**——把时间延迟作为可微变量与相机几何联合估计，并用离线规划器平衡空间敏感性与时间激励，方法论可迁移到其他时空标定问题。
4. **GaussFlaw（2611.02767）**——首个 3DGS 细粒度伪影数据集与八类缺陷标签，配合 GeoCritic 做几何引导多任务诊断，适合作为 3DGS 质量评估与下游细化的起点。
5. **HeLM（2611.02660）**——显式语言记忆 + 事件触发更新直击 VLA 的马尔可夫假设缺陷，回合内成功率提升 12.8 个百分点、长时程内存少 4.5 倍，对具身智能长程任务研究者优先级高。

#### 可能的研究机会

- **事件/多模态融合与 3DGS 的结合**：HIVE-Diff 的事件条件扩散与 3DGS 场景表示尚未交汇，可探索“事件流驱动的高斯致密化与时间一致性约束”。
- **标定与重建的联合优化**：SyncHeC 的可微延迟与 AnchorHEC 的 FK 约束 bundle adjustment 提示“几何标定与稠密重建共享优化变量”的路径，尤其在多相机 + 机械臂系统中。
- **前馈 3DGS 的伪影可诊断性**：把 GaussFlaw 的八类缺陷标签作为 OctreeSplat 类前馈方法的训练信号或评估维度，形成“诊断-致密化-修正”闭环。
- **视频世界模型与具身策略的可迁移表征**：

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
<summary>AI 简析</summary>

### Metadata
- 标题：Lie Routing Vision Language Models for View-Robust 3D Understanding
- 作者：Jingjun Yi, Chen Hu, Qi Bi, Hao Zheng, Huimin Huang, Yongkang, Wei Ji, Yawen Huang, Xian Wu, Yefeng Zheng
- 出版日期：2026-11-01T23:56:37Z
- 分类：Geometry Foundation Models（主分类；二级分类：摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2611.02306) / [PDF](https://arxiv.org/pdf/2611.02306)

### 一句话总结
论文提出 LieVLM，一种基于李路由（Lie routing）的框架，通过在多视角 RGB 观测下对投影视觉特征施加局部 SO(3) 变换，缓解多模态大语言模型在 3D 场景理解中由视角变化引起的语义漂移，从而提升视角鲁棒性。

### 研究问题
多模态大语言模型在多视角 RGB 观测的 3D 场景理解中已取得进展，但同一固定物体和查询在不同相机视角下会产生不一致的目标相关回答，作者将这一现象称为“视角诱导的语义漂移”（viewpoint-induced semantic drift）。论文关注的问题是：如何使 MLLM 的 3D 理解在面对视角变化时保持更一致、更稳健的表现。

### 核心思路/方法
- 以视角变化的旋转分量作为动机，提出 Lie routing 框架，在学习到的三维子空间中对投影特征施加局部 SO(3) 变换，以适配视觉表示。
- 由 VGGT 提取的 geometry tokens 预测局部旋转参数和通道级路由系数。
- 使用闭式 Padé–Cayley 映射对投影视觉特征进行变换；将相对于恒等变换的修正投影回原空间，并通过门控方式融入原始视觉特征与几何特征。
- 该设计旨在保留预训练模型的语义信息和直接空间上下文，同时学习依赖视角的特征调整。
- 摘要提到在 3D captioning、grounding、detection 和 spatial reasoning 任务上进行实验，并与 additive fusion 进行比较。

### 主要贡献
- 识别并刻画了多视角 3D 理解中的“视角诱导语义漂移”现象。
- 提出 LieVLM，即一种基于李路由的视角鲁棒 3D 理解框架，利用局部 SO(3) 变换和 Padé–Cayley 映射进行特征适配。
- 设计了几何条件驱动的旋转参数与通道路由系数预测机制，并通过门控修正保留预训练语义与空间上下文。
- 摘要称在 3D captioning、grounding、detection 和 spatial reasoning 上相较 additive fusion 在多种训练规模和骨干网络下取得一致提升；并通过受控消融考察几何条件与变换结构的作用，通过视角分析观察预测路由状态与任务表现的变化。

### 局限性
- 摘要未提供足够信息说明方法在非多视角 RGB 输入、其他模态或真实部署场景中的适用性。
- 摘要未提供足够信息说明计算开销、推理效率或模型规模方面的限制。
- 摘要未提供足够信息说明实验数据集的规模、多样性以及是否存在特定基准偏差。
- 摘要未提供足够信息说明失败案例、极端视角变化或遮挡条件下的表现。
- 摘要未提供足够信息说明与更多基线方法的完整比较细节。

### 阅读优先级
中。理由：论文针对多视角 3D 理解中的视角一致性问题提出明确的几何驱动路由方法，问题定义清晰，方法结合 SO(3) 变换与 MLLM 特征适配，具有一定新颖性；摘要显示覆盖多类 3D 任务与消融分析，适合关注 3D 视觉语言模型和视角鲁棒性的读者进一步阅读。但摘要未提供具体实验数值、效率分析和失败案例等关键细节，因此优先级定为中而非高。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：HIVE-Diff: High Frame Rate HDR Video Reconstruction from a Single LDR Frame and Events
- 作者：Caixin Wang, Qingrui Wang, Jie Zhang, Ralph Etienne-Cummings
- 出版日期：2026-11-02T17:08:05Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.03465) / [PDF](https://arxiv.org/pdf/2611.03465)

### 一句话总结
论文提出 HIVE-Diff，一个以事件相机数据为条件的视频扩散框架，目标是从单个 LDR 参考帧和事件流重建 N 帧高帧率 HDR 视频，而非依赖 N 个对齐的 LDR 观测。

### 研究问题
高帧率 HDR 视频在自动驾驶和科学成像等场景中很重要，这些场景常同时存在快速运动和极端光照。传统帧相机在时间分辨率与动态范围之间存在权衡；事件相机可提供宽光照范围内的高速亮度变化测量，因此被用于 HDR 重建。现有方法大致分为纯事件方法和事件-帧混合方法：纯事件方法因缺少绝对强度参考而存在亮度和颜色漂移；混合方法虽用 LDR 帧作为锚点缓解歧义，但多数只在已有 LDR 时间戳上做一对一 HDR 重建。本文研究单参考 HDR 时间扩展问题：从一个 LDR 参考帧和事件中重建 N 个 HDR 帧。

### 核心思路/方法
HIVE-Diff 是一个事件条件视频扩散框架，将任务分解为事件引导的时间生成和 HDR 内容补全。由于成对的真实 HDR-事件数据稀缺，模型先在合成数据上训练，再通过以 LDR-事件序列作为代理监督的教师-学生蒸馏，将模型适配到真实事件域。

### 主要贡献
- 提出单参考 HDR 时间扩展任务：从 1 个 LDR 参考帧和事件重建 N 个 HDR 帧，而非依赖 N 个对齐 LDR 观测。
- 提出 HIVE-Diff，将任务分解为事件引导的时间生成与 HDR 内容补全的事件条件视频扩散框架。
- 针对真实 HDR-事件配对数据稀缺，采用合成数据训练加教师-学生蒸馏、以 LDR-事件序列为代理监督的真实域适配策略。
- 摘要称在合成数据和多个真实世界数据集上的实验展示了较强的重建质量和稳健的真实数据适配能力。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算成本、推理速度、对事件噪声或运动极端程度的敏感性，也未给出定量指标和消融实验细节。真实域适配依赖 LDR-事件代理监督与教师-学生蒸馏，其误差传播或域间隙影响在摘要中未展开。

### 阅读优先级
中。理由：该论文针对高帧率 HDR 视频重建中的单参考时间扩展问题，任务设定和“扩散模型 + 事件条件 + 合成到真实蒸馏”的方法组合具有明确的研究价值；但摘要未提供定量结果、对比细节和局限性分析，是否值得深入阅读取决于读者对事件相机 HDR 重建或视频扩散应用的兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：The DynaCell Evaluation Suite for Dynamic 3D Virtual Staining of Live Cells
- 作者：Alexandr A. Kalinin, Dihan Zheng, Taylla Milena Theodoro, Ivan Ivanov, Eduardo Hirata-Miyasaki, See-Chi Lee, Aofei Liu, Sricharan Reddy Varra, Talon Chandler, Soorya Pradeep, Chad Liu, Manuel D. Leonetti, Carolina Arias, Bo Huang, Shalin B. Mehta
- 出版日期：2026-11-02T00:16:20Z
- 分类：Dynamic / 4D Reconstruction（主分类）；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.02324 ；PDF https://arxiv.org/pdf/2611.02324

### 一句话总结
论文提出 DynaCell 评估套件，用于系统评测活细胞动态 3D 虚拟染色模型，并发现回归基线与生成基线在结构保真与表型分布刻画上存在取舍。

### 研究问题
活细胞成像可记录扰动诱导的表型动态，但荧光成像的标记与重复光照常影响细胞健康；虚拟染色可从无荧光标记图像预测荧光图像，然而现有虚拟染色模型在体积时间序列数据上的表现仍缺乏充分刻画。论文聚焦于如何评估 3D 时间序列活细胞虚拟染色模型，并揭示不同模型在像素、分割与单细胞表型层面的行为差异。

### 核心思路/方法
论文构建一个面向活细胞 3D 时间序列虚拟染色的评估套件，包含三部分：配对采集的带荧光标记与无荧光标记的 3D 时间序列图像、一组基线模型，以及三层评价指标——像素级保真度、细胞器分割性能、单细胞表型相似度。基于该套件，论文在 3 种细胞类型、2 种显微镜、4 种细胞器和 3 种扰动状态下研究指标与模型行为。

### 主要贡献
- 提出 DynaCell 评估套件，用于 3D 时间序列活细胞虚拟染色的系统评测。
- 汇总配对 3D 时间序列图像、基线模型与三层评价指标。
- 在 3 种细胞类型、2 种显微镜、4 种细胞器和 3 种扰动状态下分析指标与模型行为。
- 发现回归基线更能预测目标细胞器的空间定位，而生成基线更能刻画跨细胞表型分布；这一差异揭示了结构保真与表型保真之间的取舍，而单指标评估会掩盖这种取舍。
- 指出该评估有助于面向定位、分割、追踪和表型分析等下游任务开发虚拟染色模型。
- 作为 DynaCell 框架的一部分，发布整理后的数据集、基线检查点和评估代码。

### 局限性
- 摘要未提供足够信息说明数据集规模、样本量及具体采集参数。
- 摘要未提供足够信息说明各基线模型的具体架构与训练细节。
- 摘要未提供足够信息说明三层指标的具体计算方式与数值结果。
- 摘要未提供足够信息说明评估在 3 种细胞类型、2 种显微镜、4 种细胞器和 3 种扰动状态上的完整组合覆盖情况。
- 摘要未提供足够信息说明计算成本、推理速度或实际部署限制。

### 阅读优先级
高。理由：该论文直接针对 3D 时间序列活细胞虚拟染色的评估空白，提供配对数据、基线、分层指标与多条件分析，并明确指出结构保真与表型保真之间的取舍；对关注动态 4D 重建、虚拟染色及基于图像的表型分析的研究者具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：4D Triangle Splatting Reconstruction of Dynamic Endoscopic Scenes from Monocular Videos
- 作者：Laura Salort-Benejam, Stamatia Giannarou, Antonio Agudo
- 出版日期：2026-11-01T16:29:57Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.02034) / [PDF](https://arxiv.org/pdf/2611.02034)

### 一句话总结
提出 SurgicalTS，一种面向单目内窥镜视频的自监督三角面片泼溅（triangle-splatting）框架，用于动态内窥镜场景的 4D 重建。

### 研究问题
从单目视频对可形变内窥镜场景进行稳健的 4D 重建仍具挑战性，主要困难包括非刚性组织形变、光照变化、遮挡以及未知相机轨迹。摘要指出，可靠的动态内窥镜重建有望提升微创手术的可视化、诊断准确性和术中引导。

### 核心思路/方法
- 采用自监督的 triangle-splatting 框架，从静态单目相机视频重建动态内窥镜场景。
- 场景由一组规范化（canonical）三角形表示，并与形变网络联合优化。
- 引入基于四元数的形变模型、改进的颜色参数化、时空先验，以及重新定义的初始化策略，以提升遮挡条件下的完整性。
- 在多种术式的活体内窥镜视频上进行评估。

### 主要贡献
- 提出 SurgicalTS 自监督 triangle-splatting 框架，用于单目动态内窥镜场景重建。
- 引入四元数形变模型、改进颜色参数化、时空先验和新的初始化策略。
- 摘要称其在挑战性活体内窥镜视频上能建模软组织形变与工具-组织交互，并持续优于现有最先进方法。
- 摘要称其在保持有竞争力的几何与光度精度的同时减少训练时间，体现基于四元数且具物理一致性的形变建模在稳健高效 4D 重建中的有效性。

### 局限性
- 摘要未提供足够信息说明具体数据集规模、评价指标数值、消融实验细节及失败案例。
- 摘要未提供足够信息说明方法在极端遮挡、快速运动或未知相机轨迹下的具体表现边界。
- 摘要未提供足够信息说明临床部署可行性、实时性上限或泛化到未见术式的程度。

### 阅读优先级
中。理由：该论文聚焦内窥镜动态 4D 重建这一明确且具临床应用指向的问题，方法要素（triangle splatting、四元数形变、自监督）与任务匹配度较高，摘要也声称在活体视频上优于现有方法并降低训练时间；但摘要未给出定量结果、数据集细节与消融证据，需阅读全文后才能判断其实际性能与泛化能力。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：ReVA-HPE: Relative 6DoF Head Pose Estimation with Synthetic Pose Supervision and Personalized Virtual Anchors
- 作者：Vasiliki Vasileiou, Panagiotis P. Filntisis, Petros Maragos, Kostas Daniilidis
- 出版日期：2026-11-02T15:24:53Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类；无副分类信息）
- 链接：[摘要](https://arxiv.org/abs/2611.03283) / [PDF](https://arxiv.org/pdf/2611.03283) / [项目页](https://vasilikivas.github.io/ReVA-HPE/)

### 一句话总结
该论文将相对头部姿态估计扩展到完整 6DoF，并通过单张无标注注册图像重建个性化虚拟形象、渲染一组虚拟锚点，从而摆脱推理时对锚点真实姿态的依赖。

### 研究问题
- 单目头部姿态估计通常被建模为从单张人脸裁剪图像进行绝对回归。
- 许多应用会随时间观察同一人，并可提供显式锚点图像；已有相对头部姿态估计方法将问题转化为锚点图像与查询图像之间的相对几何变化估计。
- 摘要指出，现有相对方法在推理时仍需要已知锚点图像姿态，这显著限制了实际使用。
- 论文需要解决的问题是：在不需要锚点真实姿态标注的前提下，实现完整 6DoF 的相对头部姿态估计，并尽量保持旋转与度量平移的精度。

### 核心思路/方法
- 将相对头部姿态估计扩展到完整 6DoF：除相对旋转外，额外预测深度归一化的相对平移，并与锚点组合，以恢复查询图像在相机坐标系下的度量姿态。
- 为消除对真实锚点姿态的需求，从单张无标注注册图像重建个性化虚拟形象，并渲染一组具有已知姿态的虚拟锚点。
- 该虚拟锚点库通过多锚点共识提供稳健的旋转假设；在平移分支中，真实注册图像通过 landmark PnP 作为真实锚点使用。
- 提出一种高效变体：在注册阶段一次性分摊虚拟锚点库的成本，之后每个查询只需进行一次真实图像到真实图像的相对预测，但会带来有限精度损失。
- 相对姿态估计器仅使用合成人脸渲染训练，不使用真实姿态监督、伪标签、域适应或在评估集上微调。

### 主要贡献
- 将相对头部姿态估计扩展为完整 6DoF，并引入深度归一化相对平移预测，用于恢复查询图像的度量姿态。
- 通过单张无标注注册图像构建个性化虚拟形象和已知姿态的虚拟锚点库，避免推理时依赖真实锚点姿态。
- 设计多锚点共识用于旋转假设，并结合 landmark PnP 使用真实注册图像处理平移分支。
- 提出注册阶段一次性分摊成本的高效变体，使后续查询仅需单次真实到真实相对预测。
- 仅使用合成人脸渲染训练相对姿态估计器，不使用真实姿态监督、伪标签、域适应或评估集微调。
- 摘要报告：在真实 6DoF 基准上，ReVA-HPE 在 BIWI 上取得最先进旋转精度；在提供近正面注册图像的 FaMoS 上也取得最先进旋转精度；尽管仅依赖合成姿态监督，在度量平移方面仍具竞争力。

### 局限性
- 摘要未提供足够信息说明方法在非近正面注册图像、跨域场景或遮挡等条件下的具体表现。
- 摘要未提供足够信息说明高效变体的具体精度下降幅度。
- 摘要未提供足够信息说明虚拟形象重建失败或注册图像质量较差时的影响。
- 摘要未提供足够信息给出完整实验设置、数据集划分、运行时间与资源消耗等细节。

### 阅读优先级
中。理由：该论文针对相对头部姿态估计中“推理需已知锚点姿态”的实际限制，提出 6DoF 扩展、虚拟锚点与仅合成监督的训练方案，问题定义和应用动机清晰；摘要报告了 BIWI 与 FaMoS 上的旋转精度结果。但摘要未提供足够信息展示完整实验细节、失败情形与高效变体的精度代价，是否优先精读取决于读者对 6DoF 头部姿态估计、合成监督和个性化虚拟锚点方向的兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：A Tightly Coupled Magnetic-Inertial SLAM System for Field Robots
- 作者：Chuan Huang, Tongxing Peng
- 出版日期：2026-11-02T13:23:39Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次要分类
- 链接：摘要页 https://arxiv.org/abs/2611.03106 ；PDF https://arxiv.org/pdf/2611.03106

### 一句话总结
本文提出紧耦合的磁-惯性 SLAM 系统 MISLAM，仅依靠 IMU 与九磁力计阵列，在 GNSS 拒止及视觉/激光退化条件下为地面与空中野外机器人提供不依赖外部里程计或平台运动假设的定位与建图。

### 研究问题
矿山、隧道和灾区等场景中的野外机器人常面临 GNSS 拒止，以及粉尘、烟雾或低照度导致的相机与 LiDAR 测量退化；同时涉及地面与空中机器人的任务需要不依赖可见性、预设基础设施或轮式接触的互补感知模态。论文旨在验证磁-惯性 SLAM 能否作为此类退化视觉条件下的补充定位手段。

### 核心思路/方法
MISLAM 使用 IMU 与九磁力计阵列进行紧耦合磁-惯性 SLAM，不依赖外部里程计或平台特定运动假设。系统将惯性导航模型与局部多项式磁场模型结合用于短期运动估计，并利用全局高斯过程模型通过误差状态卡尔曼滤波器进行漂移校正。

### 主要贡献
- 提出紧耦合磁-惯性 SLAM 系统 MISLAM，使用 IMU 与九磁力计阵列，不依赖外部里程计或平台特定运动假设。
- 将惯性导航模型、局部多项式磁场模型（短期运动估计）与全局高斯过程模型（基于误差状态卡尔曼滤波的漂移校正）相结合。
- 在三个室内手持装置采集数据集上进行离线评估，总端点闭环误差相对磁-惯性里程计降低 45.7%–78.0%。
- 在低照度条件下，视觉-惯性里程计失败后 MISLAM 仍保持跟踪，水平闭环误差为 0.332 m。

### 局限性
- 垂直漂移仍然是限制，摘要明确提及。
- 评估仅基于三个室内手持装置采集的数据集，且为离线评估；摘要未提供更多现场机器人平台或真实野外场景的实验信息。
- 摘要未提供计算开销、实时性、磁干扰鲁棒性、磁力计阵列标定需求等方面的信息。
- 摘要未提供与更多基线方法的全面对比细节；摘要未提供足够信息。

### 阅读优先级
中。理由：论文针对 GNSS 拒止与视觉退化场景提出不依赖可见性的磁-惯性互补定位方案，问题定位清晰，且有定量误差降低与视觉-惯性失效后的跟踪结果；但摘要显示评估限于三个室内手持数据集和离线实验，且存在垂直漂移限制，是否适用于真实野外机器人仍需进一步阅读全文验证。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MuCHMDPoser: Multiview RGB-Camera Full-Body Pose Tracking for Virtual Reality
- 作者：Antoine Maiorca, George Fletcher, Thierry Ravet, Thierry Dutoit
- 出版日期：2026-11-02T12:51:00Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.03062) | [PDF](https://arxiv.org/pdf/2611.03062)

### 一句话总结
论文提出在仅依赖头显与手柄的 VR 全身姿态跟踪中引入外部多视角 RGB 相机，以降低下半身跟踪误差，并给出无需物理标记的一次性 HMD-相机标定流程及 60 FPS 的端到端实现。

### 研究问题
仅使用消费级稀疏传感器（头显和手持控制器）进行 VR 全身跟踪时，系统只能获得 3 个上半身关节，导致全身姿态推断高度欠约束，尤其下半身姿态存在显著跟踪误差。论文旨在解决这一稀疏传感条件下的全身姿态跟踪精度问题。

### 核心思路/方法
在原有头显与手柄的稀疏跟踪设置基础上，扩展外部多视角 RGB 相机，将基于 RGB 的姿态估计整合进该框架，以改善全身尤其是下半身的姿态推断；同时评估一种仅需执行一次、无需任何物理标记的 HMD-相机标定流程；并给出整体框架的实现，在 Nvidia RTX3080 GPU 上达到 60 FPS 的端到端动画。

### 主要贡献
- 提出以外部多视角 RGB 相机扩展 VR 稀疏传感器跟踪设置，并表明整合基于 RGB 的姿态估计可显著降低下半身跟踪误差，即使在 RGB 估计存在常见伪影的情况下亦然。
- 评估了一种仅执行一次、无需物理标记的 HMD-相机标定流程。
- 提出整体框架的实现，在 Nvidia RTX3080 GPU 上实现 60 FPS 的端到端动画，并公开代码。

### 局限性
摘要未提供足够信息。摘要未给出具体误差指标、数据集规模、参与者数量、RGB 伪影类型与程度的定量分析、标定精度的定量结果，也未说明方法在不同场景或硬件条件下的泛化表现。

### 阅读优先级
中。理由：论文聚焦 VR 全身姿态跟踪中稀疏传感器欠约束这一明确问题，提出多视角 RGB 扩展、免标记标定与实时实现，并公开代码，对多视角几何与 VR/AR 应用方向具有参考价值；但摘要未提供定量实验细节与充分局限性说明，需阅读全文才能判断其实际效果与适用范围。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GPU-Native Real-Time Textured Mesh Reconstruction with Seam-Aware Multi-View Radiometric Correction
- 作者：Hiroyuki Sato
- 出版日期：2026-11-02T12:30:21Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.03033 ；PDF https://arxiv.org/pdf/2611.03033

### 一句话总结
提出一种完全驻留 GPU 的体素视频系统，从多路 RGB-D 传感器实时重建带纹理的三角网格，并在 GPU 上完成接缝感知的辐射校正。

### 研究问题
现有 TSDF 系统虽已加速融合与网格提取，但扩展到逐帧带纹理网格化时，会引入 CPU 网格处理、CPU 侧纹理化工作，或阶段间额外的 CPU-GPU 数据传输，影响实时性与端到端效率。此外，逐面从单一相机取纹理会留下随图像平滑变化的曝光接缝。

### 核心思路/方法
- 输入暂存后，将重建与纹理化各阶段（TSDF 融合、Marching Cubes、连通分量噪声去除、基于视角的纹理映射、图像修补、辐射接缝校正）全部保持在 GPU 上，中间网格或图像数据不返回主机。
- 用固定大小数组表示网格拓扑，在 GPU 上实现常数时间邻域访问，并使下游网格级操作数据并行化。
- 由于每个面仅从单一相机取纹理，仍存在平滑变化的曝光接缝；方法估计每相机低频增益场，并在 GPU 上烘焙进纹理图集。

### 主要贡献
- 提出 GPU 原生的实时带纹理三角网格重建系统，避免阶段间回传主机。
- 设计固定大小数组的网格拓扑表示，支持 GPU 常数时间邻域访问与数据并行网格操作。
- 提出接缝感知的多视角辐射校正：估计每相机低频增益场并烘焙到图集。
- 在 CMU Panoptic 数据集上，所有测试体素分辨率与传感器数量下均快于基线；相对 CUDA 加速的 nvblox 与基于 CPU 的 Open3D 取得超过一个数量级的峰值加速；感知重渲染质量接近离线带纹理网格化基线。

### 局限性
摘要未提供足够信息。摘要未说明方法在非 CMU Panoptic 场景、动态场景、传感器标定误差、增益场估计失败情形下的表现，也未给出内存占用、延迟分布或定量重渲染指标等细节。

### 阅读优先级
中。理由：与实时多传感器带纹理网格重建、GPU 端到端管线及辐射接缝校正直接相关；摘要给出了明确的速度与质量结论，但缺乏定量指标与更广泛场景验证，需阅读全文确认适用边界。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Comprehensive Evaluation of Monocular and Multi-view 3D Human Pose Estimation Models for Fitness Exercise Analysis
- 作者：Néstor Ortega, Agustín Salgado, Javier Sánchez
- 出版日期：2026-11-02T10:56:19Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要链接 https://arxiv.org/abs/2611.02929 ；PDF 链接 https://arxiv.org/pdf/2611.02929

### 一句话总结
该论文在 Fit3D 健身动作多视角数据集上统一评测两种单目 3D 人体姿态估计方法与一种多视角方法，并分析 2D 检测质量与时间滤波后处理对精度、时间一致性和鲁棒性的影响。

### 研究问题
论文关注的问题是：尽管近期深度学习方法在标准基准上取得较高精度，但它们在真实体育场景下的表现仍缺乏充分研究；同时，单目与多视角方法之间的权衡，以及提升时间一致性的后处理技术在健身类数据集上的效果，尚未被系统评估。

### 核心思路/方法
论文在 Fit3D 数据集上采用统一评测协议，评估两种近期单目提升方法 TCPFormer 和 PoseMamba-L，以及一种多视角模型 MVGFormer。为研究输入数据的影响，单目方法分别使用真实关键点和由近期 2D 姿态估计器 RTMPose、YOLO-Pose 生成的检测结果进行评测。此外，论文分析三种时间滤波器在减少预测抖动的同时保留运动动态方面的有效性。

### 主要贡献
- 在 Fit3D 健身动作多视角同步录制数据集上，对单目与多视角 3D 人体姿态估计方法进行统一评测。
- 对比 TCPFormer、PoseMamba-L 与 MVGFormer 在精度、时间一致性和对不完美 2D 检测鲁棒性方面的表现。
- 分析 2D 检测器质量对基于提升的单目方法的影响，并比较基于 Transformer 与基于状态空间的时间架构。
- 讨论单目与多视角系统在健身运动分析中的实际权衡。
- 分析三种时间滤波器在减少预测抖动与保留运动动态之间的效果。

### 局限性
摘要未提供足够信息说明具体的定量实验结果、各方法的具体精度数值、时间滤波器的详细参数与实现细节，以及评测协议的具体构成。论文也未在摘要中给出对更多数据集或更多模型的泛化验证信息。

### 阅读优先级
中。理由：该论文属于系统评测与实证分析类工作，聚焦健身场景下的 3D 人体姿态估计方法对比，对关注体育分析、单目与多视角权衡、2D 检测质量影响及时间后处理的研究者有参考价值；但摘要未提供具体实验数值和显著新方法，若读者更关注新模型架构或定量结论，需进一步阅读全文。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：AnchorHEC: Targetless Hand-Eye Calibration of Wrist and Fixed Cameras
- 作者：Guebin Hwang, Taeyeop Lee, Yeonseo Lee, Hyosup Shin, Sungho Jo
- 出版日期：2026-11-02T10:19:26Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.02884；PDF https://arxiv.org/pdf/2611.02884；项目页 https://hwanggb.github.io/AnchorHEC/

### 一句话总结
论文提出 AnchorHEC，一种仅使用 RGB 图像、前向运动学（FK）和已知相机内参、无需标定靶标或机器人本体观测的统一手眼标定框架，可同时标定腕部相机与固定相机。

### 研究问题
近期机器人系统同时使用腕部相机和固定相机，因此需要分别获得两类相机到机器人的变换。多数手眼标定方法依赖标定靶标或机器人本体观测；基于场景的三维重建方法虽不需这些，但只处理腕部相机。论文要解决的是：如何在无标定靶标条件下，用统一流程同时完成腕部相机与固定相机的手眼标定。

### 核心思路/方法
AnchorHEC 使用 RGB 图像、前向运动学（FK）和已知相机内参，在单一过程中完成两类相机标定。方法先用 FK 和共享的三维基础模型重建初始化两类相机；随后通过 FK 约束的腕部图像 bundle adjustment 降低重建位姿与尺度误差的影响。若该细化失败或保留的内点过少，则放松对可能不准确 FK 位姿和镜头参数的约束。最后利用细化后的腕部变换与 FK 三角化度量点，并估计固定相机位姿。

### 主要贡献
- 提出 AnchorHEC：面向腕部相机与固定相机的无靶标手眼标定框架，在单一流程中完成两类相机标定，且不需要标定靶标或机器人本体观测。
- 给出结合 FK、共享三维基础模型重建、FK 约束腕部图像 bundle adjustment 以及后续三角化与固定相机位姿估计的方法流程。
- 在三种骨干网络上，仿真标定误差相对基于重建的基线平均在平移上降低 86.4%、旋转上降低 71.6%（两类相机平均）；并在实体机器人上验证了 AnchorHEC。
- 提供项目页面用于结果展示。

### 局限性
- 摘要仅说明在仿真中与基于重建的基线比较，并在实体机器人上验证，但未提供实体实验的定量结果、误差指标或统计细节：摘要未提供足够信息。
- 未说明方法对 FK 精度、相机内参误差、三维基础模型质量、场景纹理与动态物体等因素的敏感性：摘要未提供足够信息。
- 未给出运行时间、计算资源需求、失败案例比例或与更多类型基线的系统比较：摘要未提供足够信息。
- 摘要未说明代码或数据是否公开，仅提供项目页面链接：摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对腕部与固定相机联合手眼标定的实际问题，提出无靶标、单流程方法，并在仿真中报告相对基线的显著误差下降，且包含实体机器人验证，具有一定参考价值；但摘要未提供实体实验定量细节、鲁棒性分析与计算成本信息，是否优先精读取决于读者对无靶标多相机手眼标定或三维基础模型用于机器人标定的兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：OctreeSplat: Hierarchical Octree-Guided Feed-Forward Gaussian Splatting
- 作者：Yibin Zhao, Yihan Pan, Wenli Yang, Jun Nan, Jianjun Yi
- 出版日期：2026-11-02T07:17:04Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.02658；PDF https://arxiv.org/pdf/2611.02658

### 一句话总结
OctreeSplat 提出一种由分层八叉树引导的前馈高斯泼溅方法，根据局部复杂度在空间上自适应分配高斯原语，并结合随机实体体积渲染与可选测试时优化，以较少原语完成新视角合成、深度合成与表面重建。

### 研究问题
3D Gaussian Splatting 在新视角合成与三维重建中具有潜力，前馈方法虽避免了昂贵的逐场景优化，但固定图像或空间分辨率限制了其按局部复杂度分配原语的能力。论文关注如何在前馈框架下实现空间自适应的高斯原语密度分配，并提升深度渲染、几何监督与表面重建效果。

### 核心思路/方法
方法从冻结的视觉基础模型（VFM）中提取多视角特征与几何先验，构建分层八叉树并预测致密化分数，从而按局部复杂度在不同空间位置分配不同密度的高斯原语。渲染方面采用随机实体体积渲染，以改善深度渲染、加强几何监督并支持表面重建。当相机参数可用时，提供可选的测试时优化（TTO）模块，以提升预测参数与真实参数的一致性。训练仅更新 7600 万个额外参数，需要 35 GPU 小时。

### 主要贡献
- 提出 OctreeSplat，一种分层八叉树引导的前馈高斯泼溅框架，实现按局部复杂度变化的空间密度分配。
- 利用冻结 VFM 提取多视角特征与几何先验，并通过八叉树结构预测致密化分数。
- 引入随机实体体积渲染，改善深度渲染、几何监督与表面重建。
- 提供可选 TTO 模块，在相机参数可用时提升预测参数与真实参数的一致性。
- 在 Replica、TUM、Tanks and Temples 和 DTU 上报告了有竞争力的 RGB 视角合成、深度合成与表面重建结果，并在保持高重建质量的同时减少高斯原语数量。
- 摘要给出训练开销：仅更新 7600 万额外参数，需要 35 GPU 小时。

### 局限性
摘要未提供足够信息说明方法在不同场景规模、相机参数缺失条件、极端稀疏视角或动态场景下的表现；也未提供失败案例、计算资源需求之外的具体效率对比或消融细节。摘要未提供足够信息。

### 阅读优先级
中。理由：论文聚焦前馈 3DGS 中“按局部复杂度自适应分配原语”这一明确问题，并给出多数据集上的 RGB、深度与表面重建结果，且训练参数与 GPU 小时数较具体，对关注前馈高斯泼溅、八叉树结构引导和表面重建的研究者有参考价值；但摘要未展开关键实验细节与局限性，需阅读全文后才能判断其相对现有方法的实际增益与适用范围。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Depth Anyviewpoint? Evaluating Monocular Depth Over Viewpoint Sequences
- 作者：Theo Rode, Rui Zhang, Ryan Aubrey, Olivia Li, Jessica Huang, Liv Chu, Healani Dowd, Calden Wloka
- 出版日期：2026-11-01T21:01:53Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.02203) | [PDF](https://arxiv.org/pdf/2611.02203)

### 一句话总结
论文提出一种基于移动相机视频序列的单目深度模型评测协议，用于检验模型在视角变化下是否保持空间结构一致，并评估借助 structure from motion 将预测锚定到度量深度的可行性。

### 研究问题
单目深度模型预测的是仿射不变深度（相对深度），在单图像基准上表现良好，在视频中定性上也较为一致，但其在视角变化下能否保持连贯的三维空间结构尚缺乏充分检验。许多现实应用（如视频流输入）依赖场景的三维一致性；同时，如何将相对深度预测锚定到特定场景的度量参考，也是单目深度模型落地应用的关键挑战。

### 核心思路/方法
作者设计了一种新的单目深度模型评测协议：使用相机位置移动的视频序列，测试模型预测在视角变化下的一致性。该方法在多样的真实世界视频序列上进行验证，并利用 structure from motion 将深度模型输出锚定到度量深度值，从而在真实视频上检验模型的跨视角一致性与度量锚定效果。

### 主要贡献
- 提出面向视角序列的单目深度模型评测协议，用于检验预测在视角变化下的一致性。
- 在多样的真实世界视频序列上演示该评测方法。
- 利用 structure from motion 将深度模型输出锚定到度量深度值。
- 揭示广泛适用的单目深度基础模型仍存在的开放挑战，尤其是在长时段内提供时间一致性的能力。
- 指出将 structure from motion 作为单目深度度量锚定工具时直接采用所面临的挑战。

### 局限性
- 摘要未提供足够信息说明具体数据集规模、模型清单、定量指标与误差数值。
- 摘要未提供足够信息说明评测协议的具体实现细节与参数设置。
- 摘要未提供足够信息说明 structure from motion 锚定失败或偏差的具体原因与量化程度。
- 摘要未提供足够信息说明方法的适用范围边界（如场景类型、视频长度、相机运动模式等）。

### 阅读优先级
中。理由：该论文关注单目深度模型在视角序列上的空间/时间一致性与度量锚定问题，属于三维重建与多视图几何方向的评测类工作，对视频深度应用和基础模型评估有参考价值；但摘要未给出具体实验规模与定量结果，是否值得深入阅读取决于读者对“评测协议”和“structure from motion 锚定”这一具体问题的兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：UniGS-SLAM: Monocular Gaussian SLAM with Enhanced Geometry and Open-Vocabulary Semantics
- 作者：Xingyuan Ding, Sicheng Yu, Kaiyong Zhao, Hao Wang
- 出版日期：2026-11-01T16:56:02Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.02051)｜[PDF](https://arxiv.org/pdf/2611.02051)｜[项目页](https://3dagentworld.github.io/UniGS-SLAM/)

### 一句话总结
UniGS-SLAM 是一个仅依赖 RGB 输入的单目高斯 SLAM 框架，将开放词汇语义与高斯重建解耦，并通过独立稀疏体素语义地图支持历史语义证据随几何更新而修订。

### 研究问题
论文针对单目语义 SLAM 中场景几何重建与语义地图构建的问题。摘要指出，现有基于高斯的方法通常把语义标签或特征附加到演化中的高斯基元上，导致语义融合难以维护且增加重建开销；混合高斯—体素表示虽提供更稳定的语义支撑，但往往依赖 RGB-D 输入或已知位姿，并且在高斯几何更新后不会修订历史语义证据。

### 核心思路/方法
- 提出仅 RGB 输入的 UniGS-SLAM 框架，将开放词汇语义与高斯重建解耦，同时保留二者的双向交互。
- 使用基础模型先验增强单目深度与位姿估计。
- 将语义观测融合进独立的稀疏体素地图，并记录观测来源（observation provenance），使历史贡献可随重建演化被修订。
- 融合后的语义进一步用于引导高斯过滤与局部表面细化。

### 主要贡献
- 提出 RGB-only 的单目高斯 SLAM 框架，实现开放词汇语义与高斯重建的解耦及双向交互。
- 设计带观测来源的独立稀疏体素语义地图，使历史语义证据可在几何更新后被修订。
- 利用融合语义反向引导高斯过滤和局部表面细化。
- 摘要报告在 Replica、ScanNet 和 KITTI-360 上，于代表性 RGB-only 方法中取得领先的跟踪、渲染和几何重建性能，并在 Replica 与 ScanNet 上展现较强的开放集语义建图能力。
- 摘要报告相比最快的对比语义 SLAM 基线实现 2.37 倍重建加速。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、计算资源需求、实时性上限、对基础模型先验的依赖程度，也未提供各数据集上的具体量化指标与消融细节。

### 阅读优先级
中。理由：该论文与单目 RGB-only 高斯 SLAM、开放词汇语义建图和重建效率直接相关，且摘要给出了明确的方法差异点与多数据集性能声明；但摘要未提供具体实验数值、消融和局限性信息，是否精读需结合全文实验细节进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Spade-SLAM: Sparse Correspondence Anchors for Dense Self-Supervised Visual SLAM
- 作者：Julian Philipp Schmitt, Weirong Chen, Ganlin Zhang, Felix Wimbauer, Daniel Cremers
- 出版日期：2026-11-01T14:14:01Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.01937 ；PDF https://arxiv.org/pdf/2611.01937 ；代码 https://github.com/JulianPSchmitt/Spade-SLAM

### 一句话总结
Spade-SLAM 提出面向稠密自监督视觉 SLAM 的“稀疏对应锚点”训练机制，在无真值位姿与深度标签的零样本设定下缩小与监督方法的性能差距。

### 研究问题
论文关注稠密视觉 SLAM 中长期存在的自监督方法与监督方法之间的性能差距，尤其是在零样本设置下。目标是证明不依赖显式真值位姿和深度标签也能实现高保真跟踪，从而提供一种高效、标签友好的替代方案，减少对全监督预训练的依赖。

### 核心思路/方法
核心是一种“稀疏到稠密”的互补训练机制：
- 稠密训练信号：基于 warping 的光度损失，提供稠密监督。
- 稀疏稳定信号：由图像特征匹配得到的稀疏对应损失，用于稳定优化并抑制歧义区域的漂移。
两者结合构成互补的稀疏到稠密训练范式。

### 主要贡献
- 提出 Spade-SLAM 自监督稠密视觉 SLAM 框架，在零样本设置下显著缩小与监督方法的性能差距。
- 提出互补的稀疏到稠密训练机制：以光度损失提供稠密信号，以特征匹配导出的稀疏对应损失稳定优化、抑制歧义区域漂移。
- 摘要称大量实验表明，相较于现有自监督基线，方法在鲁棒性和精度上显著提升，并接近使用显式位姿与深度监督训练的 SLAM 系统。
- 承诺公开代码。

### 局限性
- 具体实验数据集、评价指标、定量结果和消融细节：摘要未提供足够信息。
- 稀疏对应损失的实现细节、特征匹配方式及超参数设置：摘要未提供足够信息。
- 计算开销、实时性、在不同场景下的失效条件：摘要未提供足够信息。
- 与监督方法的具体差距数值及“closely rivaling”的量化依据：摘要未提供足够信息。

### 阅读优先级
高。理由：论文直接针对自监督稠密视觉 SLAM 与监督方法之间的性能差距，提出明确的稀疏到稠密训练机制，且摘要声称在零样本设置下显著提升鲁棒性与精度并接近监督系统；若关注标签高效 SLAM、自监督稠密跟踪或稀疏对应约束在 SLAM 训练中的作用，该工作具有较高阅读价值。但需注意摘要未给出定量实验细节，阅读全文前应保留对结论强度的审慎判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Teleoperation System for Service Robots using Virtual Reality Headset and Pose Estimation
- 作者：Eduardo Fernandes, Tiago Ribeiro, Antonio Ribeiro, Carolina Lopes, Gil Lopes, Fernando Ribeiro
- 出版日期：2026-11-01T10:05:56Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.01759)｜[PDF](https://arxiv.org/pdf/2611.01759)

### 一句话总结
论文提出一种面向服务机器人的遥操作系统，将基于 Mediapipe 与 RGB-D 数据的人体三维姿态估计映射到机器人运动学，并通过 VR 头显提供沉浸式视角，用 CHARMIE 服务机器人进行了真实环境物体操作任务验证。

### 研究问题
如何让服务机器人的远程操作更直观、更自然：利用人体姿态估计获取操作者的动作，并将其映射为机器人的运动，同时通过 VR 界面提升操作者的情境感知能力。摘要指出，系统仍需应对某些关节角度（如手腕偏航）的准确捕捉，以及人与机器人运动之间精确映射的挑战。

### 核心思路/方法
- 使用 Mediapipe 框架做 2D 姿态检测，并借助 Intel RealSense D455 相机的 RGB-D 数据扩展为较完整的三维人体姿态估计。
- 将估计得到的人体姿态数据映射到机器人运动学，使操作者能以自然动作控制机器人运动。
- 开发 VR 界面，为操作者提供沉浸式视角，以增强情境感知。
- 摘要还提到一种用于实时关节角计算的创新算法，结合 RGB-D 感知以提升人机运动映射精度，并支持通过 VR 界面进行沉浸式控制。
- 使用 CHARMIE 服务机器人开展真实世界实验，验证系统在涉及物体操作任务中的有效性。

### 主要贡献
- 提出并实现了一个融合人体姿态估计与 VR 的服务机器人遥操作系统。
- 将 Mediapipe 的 2D 姿态检测与 RealSense D455 的 RGB-D 数据结合，形成三维人体姿态估计并映射至机器人运动学。
- 引入结合 RGB-D 感知与实时关节角计算算法的遥操作新方法，旨在提升人机运动映射精度并实现 VR 沉浸式控制。
- 通过 CHARMIE 服务机器人的真实环境实验，展示了 VR 遥操作在物体操作任务中的潜力。
- 摘要声称这些工作对人机交互领域、尤其是服务机器人应用具有推进意义。

### 局限性
- 摘要明确承认：系统在准确捕捉某些关节角度方面仍存在困难，例如手腕偏航（wrist yaw）。
- 摘要明确承认：确保人与机器人运动之间的精确映射仍是挑战。
- 未来工作包括引入惯性测量单元（IMU）以改善旋转跟踪，以及实现更先进的控制算法。
- 除上述内容外，摘要未提供足够信息说明实验规模、定量指标、对比基线、失败率或用户研究结果等细节。

### 阅读优先级
**中**。理由：该工作与 VR 遥操作、人体姿态估计和 service robot 人机交互直接相关，且提供了 RealSense + Mediapipe 与机器人运动学映射的系统思路，对相关方向有参考价值；但摘要显示系统仍受关节角捕捉和精确映射问题限制，且摘要未提供定量实验细节与对比结果，因此不适合作为仅凭摘要即可高置信度采纳结论的高优先级文献，建议在需要了解 VR 遥操作实现路线时阅读全文进一步核实。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：EgoMo3R: Joint Egocentric Motion and Scene Reconstruction
- 作者：Chaitanya Patel, Yusuke Kato, Rin Takahira, Kazuki Kozuka, Juan Carlos Niebles, Ehsan Adeli
- 出版日期：2026-11-01T06:20:11Z
- 分类：3D Reconstruction & Multi-view Geometry（主）；Embodied / Robotics / AR Applications（次）
- 链接：摘要页 https://arxiv.org/abs/2611.01627 ；PDF https://arxiv.org/pdf/2611.01627

### 一句话总结
EgoMo3R 提出一种联合优化框架，从日常第一人称单目视频中同时重建 3D 人体运动与场景几何，并借助人体运动先验将相机轨迹锚定到度量、重力对齐的世界坐标系。

### 研究问题
论文关注第一人称（egocentric）视频中整体 3D 人体运动与周围环境的理解。摘要指出，这两项任务本质上是耦合的，但现有方法将它们分开处理；第一人称运动重建方法通常依赖专用惯性传感器提供的度量、重力对齐相机轨迹，而仅从单目第一人称视频恢复此类轨迹仍因快速头部运动和运动模糊而具有显著挑战。

### 核心思路/方法
- 构建联合优化框架，同时重建 3D 人体运动与场景几何。
- 利用低层视觉几何基元的鲁棒性，包括单目深度、光流和点轨迹。
- 将上述基元与基于扩散的人体运动先验通过一阶优化进行整合。
- 提出交替优化方案，形成协同反馈回路：
  - 场景重建为运动先验提供物理 grounding（物理约束/支撑）与轨迹条件；
  - 运动先验反过来正则化相机轨迹，并将场景锚定到度量、重力对齐的世界坐标系。

### 主要贡献
- 提出 EgoMo3R 联合优化框架，从随意拍摄的第一人称视频中同时重建 3D 人体运动与场景几何。
- 将低层视几何基元（单目深度、光流、点轨迹）与扩散式人体运动先验结合，并通过一阶优化求解。
- 设计交替优化机制，使场景重建与运动先验相互约束，尤其是利用运动先验恢复度量、重力对齐的相机轨迹并锚定场景。
- 在 EgoExo4D 与 Nymeria 数据集的高动态序列上评估，摘要称其在 3D 场景重建与第一人称运动估计上均优于专门的基线方法。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、计算成本、对特定场景或数据条件的敏感性分析，也未说明方法在非高动态或极端运动模糊条件下的表现。

### 阅读优先级
高。理由：该论文直接针对第一人称视频中运动与场景联合重建这一耦合问题，且摘要明确声称在 EgoExo4D 与 Nymeria 高动态序列上优于专门基线；主题同时涉及 3D 重建、AR/VR 与机器人应用，方法思路（视几何基元 + 扩散运动先验 + 交替优化）具有较强参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Detecting Generated-Depth Injection Attacks on RGB-D Place Authentication
- 作者：Seigo Kawachi, Satoshi Matsuura
- 出版日期：2026-11-01T04:21:48Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.01550) / [PDF](https://arxiv.org/pdf/2611.01550)

### 一句话总结
论文研究一种基于注册视图与查询视图之间几何一致性的软件层 PAD 分类器，用于检测攻击者用单目深度估计（MDE）从公开 RGB 图像生成深度并提交的伪造 RGB-D 查询，并评估检测效果随攻击者对相机内参掌握程度的变化。

### 研究问题
RGB-D 地点认证默认深度来自传感器；但 MDE 的进步使攻击者可从公开 RGB 图像生成深度，提交伪造 RGB-D 查询，从而破坏该假设。论文关注：此类“软件注入深度”攻击能否被基于几何一致性的 PAD 分类器检测，以及检测能力如何取决于攻击者对相机内参的准确程度。

### 核心思路/方法
- 采用 PAD 分类器，利用注册视图与查询视图之间的几何一致性作为软件层防御。
- 设计三阶段评估：
  1. 攻击者仅估计内参；
  2. 攻击者获得精确内参；
  3. oracle 评估，评估者用真实 3D 几何拟合 warp。
- 分析两类检测线索：重投影误差（reprojection error）捕捉攻击者对内参的误估；注册残差（registration residual）在攻击者知道精确内参时仍然存在。

### 主要贡献
- 提出并评估一种针对“生成深度注入攻击”的软件层 PAD 防御思路。
- 通过三阶段评估刻画检测性能随攻击者内参知识增长而退化的程度。
- 识别重投影误差与注册残差两类线索的不同作用：前者反映内参误估，后者在内参精确时仍可作为线索。
- 具体实验设置、数据集与实现细节：摘要未提供足够信息。

### 局限性
- 摘要仅给出三阶段评估的 AUC 范围与定性结论，未提供数据集规模、攻击场景覆盖、计算开销等细节：摘要未提供足够信息。
- 第三阶段为 oracle 评估，其结论与实际攻击者能力之间的差距：摘要未提供足够信息。
- 防御在真实部署条件下的鲁棒性与泛化性：摘要未提供足够信息。

### 阅读优先级
中。理由：论文针对 RGB-D 地点认证中的生成深度注入攻击，问题新颖且与 3D 几何一致性检测直接相关；三阶段评估设计清晰，并给出可量化的 AUC 变化。但摘要未提供数据集、实现与部署细节，是否值得深入阅读取决于读者对 PAD、MDE 攻击面或地点认证安全的兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：RadPose: ISAC-based RF 3D Human Pose Estimation
- 作者：Geo Jie Zhou, Kunzhe Song, Ruxin Lin, Huacheng Zeng
- 出版日期：2026-11-01T01:08:32Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.01400)｜[PDF](https://arxiv.org/pdf/2611.01400)｜[代码与数据集](https://github.com/Geo-Chou/RadPose)

### 一句话总结
RadPose 提出一种基于单基地全双工 ISAC 的学习框架，利用标准 OFDM 通信信号提取 CIR 并生成 3D 射频点云，从而实现无需专用雷达硬件的 3D 人体姿态估计。

### 研究问题
在不利光照和遮挡条件下，基于相机和 LiDAR 的人体姿态估计仍具挑战性。mmWave 雷达虽对光照和遮挡更稳健，但依赖专用硬件与许可频谱，可扩展性受限。论文关注的问题是：能否利用 mmWave 通信设备本身完成 3D 人体姿态估计，并应对射频观测的稀疏性与噪声。

### 核心思路/方法
- 采用学习式单基地 ISAC 框架，通过单基地全双工操作从标准 OFDM 通信信号中提取信道冲激响应（CIR），生成 3D 射频点云，而不依赖额外感知硬件。
- 针对 RF 观测稀疏和噪声问题，使用跨帧 Transformer 姿态推断网络，并引入语义引导的空间注意力和目标驱动的时间注意力，进行稳健的时空聚合。
- 进一步采用基于图卷积的关节感知逆运动学细化模块，约束骨架拓扑、骨长一致性和解剖合理性。

### 主要贡献
- 提出 RadPose，使 mmWave 通信设备能够执行 3D 人体姿态估计，避免专用雷达硬件与许可频谱依赖。
- 设计跨帧 Transformer 姿态推断网络，结合语义引导空间注意力与目标驱动时间注意力。
- 引入基于图卷积的关节感知逆运动学细化模块，以增强骨架结构约束。
- 摘要称大量实验表明，RadPose 与最先进的基于雷达的方法相比具有有竞争力的精度，并在未见场景和遮挡场景中保持稳健性能；数据集和源代码已公开。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集规模、评价指标、对比方法细节及定量结果。
- 摘要未提供足够信息说明方法在功耗、实时性、通信兼容性、不同人体尺度或复杂多目标场景下的表现。
- 摘要未提供足够信息说明单基地全双工 ISAC 的硬件假设、适用频段及实际部署限制。

### 阅读优先级
高。理由：该论文将 ISAC 与 3D 人体姿态估计结合，问题定位明确，方法涵盖射频点云生成、跨帧 Transformer 与时序空间注意力、逆运动学细化，且作者公开数据集与代码；对射频感知、无线通信辅助感知和遮挡鲁棒姿态估计方向具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：3D Gaussian Splatting within Self-Learned Neural View-Dependent Color Fields
- 作者：Yixiao Yang, Yu-Shen Liu, Zhizhong Han
- 出版日期：2026-11-02T13:32:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.03114) / [PDF](https://arxiv.org/pdf/2611.03114) / [项目页](https://github.com/yangyixi21/Neural-Color-Fields-3DGS)

### 一句话总结
论文提出以神经网络参数化的连续视角相关颜色场来约束 3D Gaussian Splatting，以缓解离散高斯导致的深度质量差、几何细节不足和漂浮物问题。

### 研究问题
3D Gaussian Splatting 通过堆叠带颜色、不透明度、尺度等属性的 3D 高斯显式建模辐射场，但离散 3D 高斯通常产生较差的深度，几何细节少且漂浮物多，阻碍平滑辐射场的有效建模。摘要未提供具体量化问题定义或失败案例的详细实验分析。

### 核心思路/方法
- 在由神经网络参数化的连续视角相关颜色场中学习辐射场，以颜色上的连续约束替代仅依赖高斯的颜色属性。
- 利用神经网络对低频信号的偏置，鼓励几何建模去贡献图像中的高频颜色变化，从而不再单纯依赖颜色属性本身。
- 对神经颜色场施加约束以提升其 Lipschitz 连续性，使每个高斯颜色的较大变化与其位置变化按比例匹配。
- 引入新的自学习策略改进神经视角相关颜色场的学习，不依赖外部知识或先验，目标是提升对未见场景的泛化能力。

### 主要贡献
- 提出在自学习的神经视角相关颜色场内进行 3D Gaussian Splatting 的框架。
- 通过连续颜色约束与 Lipschitz 连续性约束，改善 3DGS 的几何建模与高频颜色变化建模。
- 引入无需外部知识或先验的自学习策略，面向未见场景的泛化。
- 在广泛使用的基准上进行了数值与视觉比较，摘要称其展示了 3DGS 中更高保真几何恢复的能力。

### 局限性
摘要未提供足够信息。摘要未给出具体基准名称、评价指标、定量结果、运行开销、失败场景或消融实验细节，因此无法基于所提供内容判断方法的适用范围与局限。

### 阅读优先级
中。理由：该工作针对 3DGS 中离散高斯导致的深度与几何质量问题，思路明确且与神经颜色场、Lipschitz 约束和自学习策略相关；但摘要未提供具体实验设置与定量证据，是否值得优先精读取决于读者对 3DGS 几何保真度与泛化改进的关注程度。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：SyncHeC: Markerless Spatio-Temporal Hand-Eye Calibration via Differentiable Rendering and Continuous-Time Joint Optimization
- 作者：Zhengdong Hong
- 出版日期：2026-11-02T12:03:20Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.02999 ；PDF https://arxiv.org/pdf/2611.02999

### 一句话总结
SyncHeC 是一个基于稠密可微渲染的免标记手眼标定框架，用单条机器人轨迹同时估计相机几何与图像—关节状态之间的时间偏移，并报告了精度、对比实验和策略部署收益。

### 研究问题
连续运动下的免标记手眼标定，需要同时解决相机几何与图像和关节状态之间的时间偏移问题。摘要指出，这一联合估计是该方法要处理的核心困难。

### 核心思路/方法
- 采用稠密可微渲染框架，从单条机器人轨迹中估计相机几何和时间偏移。
- 使用连续时间前向运动学，使延迟（latency）可微。
- 以度量深度补充掩码轮廓信息。
- 使用离线规划器，将空间敏感性与时间激励结合起来。
- 通过交替更新，支持 Eye-to-Hand、Eye-in-Hand 和多相机标定。

### 主要贡献
- 提出 SyncHeC，在连续运动下联合估计相机几何与时间偏移，并兼容多种手眼配置。
- 在 7-DoF 机械臂上，一次 6.5 s 运动得到 0.21 cm 平移误差（相对标记板参考）、0.34 cm 触摸测试误差，以及相对 87 ms 参考的 2.7 ms 延迟误差（95% 不确定性 ±1.5 ms）。
- 在匹配录制上对比 CM-Calib，平移误差和标称延迟误差分别改善 3.7 倍和 2.3 倍。
- 实验覆盖七种机械臂和四种深度传感器；在策略训练与部署中补偿恢复的偏移，跨六个家族和六项任务将成功率提高 8.1 个百分点（1,800 对匹配样本；配对 95% 置信区间 [6.3, 9.9] 个百分点）。

### 局限性
- 摘要未提供足够信息说明方法在更复杂场景、不同运动模式或失败条件下的表现。
- 摘要未提供足够信息说明对规划器设计、参数敏感性或计算成本的详细分析。
- 摘要未提供足够信息说明七种机械臂和四种深度传感器的具体型号、实验设置及统计细节。
- 摘要未提供足够信息说明与更多基线方法的系统比较。

### 阅读优先级
高。理由：摘要给出了明确的问题定义、统一框架、定量精度、与基线的对比，以及下游策略部署收益；对关注机器人手眼标定、可微渲染和连续时间优化的读者具有较强相关性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GaussFlaw: Fine-Grained Perceptual Diagnosis for 3D Gaussian Splatting
- 作者：Shaocheng Shen, Zihan Zheng, Kejin Li, Lu Liu, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang
- 出版日期：2026-11-02T08:46:50Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.02767 ；PDF https://arxiv.org/pdf/2611.02767

### 一句话总结
论文提出面向 3D Gaussian Splatting 细粒度伪影诊断的数据集 GaussFlaw-80K 与几何引导多任务模型 GeoCritic，并展示诊断结果可用于引导后续细化操作。

### 研究问题
3DGS 虽能实现高质量新视角合成与实时渲染，但其渲染伪影通常空间局部化且退化模式多样，全局质量指标和图像级评估基准难以说明伪影出现位置及其类型，因此缺乏细粒度的伪影诊断手段。

### 核心思路/方法
- 构建 GaussFlaw-80K：首个面向 3DGS 细粒度感知诊断的大规模数据集，通过模型辅助、人在回路的流程构建，覆盖 14,289 张渲染图像中的 80,049 个伪影区域，每个区域带像素级掩码与八类缺陷标签之一，标签涵盖几何、混合与光度退化。
- 将 3DGS 伪影诊断转化为显式、可度量的任务。
- 提出 GeoCritic：几何引导的多任务模型，融合 RGB 外观与深度衍生线索，联合定位伪影并分类其缺陷类型。
- 将细粒度诊断用于下游操作：高斯致密化、属性修正与离群点剪枝。

### 主要贡献
- 发布 GaussFlaw-80K 数据集，为 3DGS 伪影提供像素级掩码和八类缺陷标签，使细粒度诊断成为可显式评估的任务。
- 提出 GeoCritic 多任务模型，联合完成伪影定位与缺陷分类。
- 展示诊断引导的细化在多种数据集和 3DGS 主干上改善所报告的全局与裁剪级指标。
- 摘要报告 GeoCritic 达到 AUC-J 0.9507、Acc@1 80.08%。

### 局限性
摘要未提供足够信息。例如数据集构建的具体人工标注协议、八类标签的详细定义与分布、GeoCritic 的网络结构与训练细节、计算开销、跨场景泛化边界，以及诊断引导细化在各指标上的具体提升幅度，摘要均未展开。

### 阅读优先级
高。理由：该工作同时涉及 3DGS 渲染伪影的细粒度评估基准与诊断模型，并连接诊断到下游细化操作，对关注 3DGS 质量分析、伪影定位与可控优化的读者具有直接相关性；但具体实验细节需查阅全文确认。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：UniCross3D: Unified Cross-View and Cross-Domain Diffusion for Consistent Single-Image 3D Generation
- 作者：U-Chae Jun, Jaeeun Ko, Jiwoo Kang
- 出版日期：2026-11-02T06:57:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.02631 ；PDF https://arxiv.org/pdf/2611.02631

### 一句话总结
UniCross3D 提出统一的跨视角与跨域扩散框架，通过跨视角隐变量正则和跨域互信息目标，缓解单图三维生成中的视角几何不一致与语义对齐不足问题。

### 研究问题
从单张 RGB 图像重建细节几何与真实外观具有根本挑战，原因包括遮挡、光照变化、纹理与几何耦合等固有歧义。摘要指出，现有基于扩散的生成模型虽显著提升新视角合成，但存在两个关键局限：缺乏跨视角几何一致性，以及跨域语义对齐不足。

### 核心思路/方法
论文提出 UniCross3D，一个面向一致且物理连贯三维生成的统一跨视角与跨域扩散框架。方法包含两项核心设计：
1. 跨视角隐变量正则：通过对隐变量方差施加惩罚，在合成视角之间强化跨视角几何一致性。
2. 跨域互信息目标：基于图像形成物理，显式对齐合成的颜色图与法线图。

### 主要贡献
- 提出统一的跨视角与跨域扩散框架 UniCross3D，用于一致且物理连贯的单图三维生成。
- 引入跨视角隐变量正则，以惩罚隐变量方差的方式增强多合成视角间的几何一致性。
- 引入基于图像形成物理的跨域互信息目标，显式对齐合成颜色与法线表示。
- 摘要称大量实验表明，该方法在视角一致性与语义对齐上显著优于当前先进方法，并在挑战性纹理与歧义视角下获得更高保真重建。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集、评价指标与定量结果。
- 摘要未提供足够信息说明方法在计算开销、训练稳定性或推理效率方面的表现。
- 摘要未提供足够信息说明失败案例、适用场景边界或对输入图像质量的敏感程度。
- 摘要未提供足够信息说明跨视角隐变量正则与跨域互信息目标的具体实现细节及超参数影响。

### 阅读优先级
中。理由：该论文聚焦单图三维生成中的跨视角一致性与跨域语义对齐，问题定义清晰，两项技术设计具有较强的针对性；但当前仅依据摘要，实验细节、定量证据与实现可行性信息不足，适合作为相关方向的重点跟踪文献，待全文可获取后再决定是否提升为高优先级。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Unified Loss-Aware Density Control for 3D Gaussian Splatting
- 作者：Tae-Young Kim, Jiwoo Chung, Jae-Pil Heo
- 出版日期：2026-11-01T16:47:33Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.02044) ｜ [PDF](https://arxiv.org/pdf/2611.02044)

### 一句话总结
该论文将 3D Gaussian Splatting 的自适应密度控制重新表述为局部损失下降决策，并借助 Taylor 近似为分裂、克隆与不透明度衰减三种操作建立统一的损失感知框架。

### 研究问题
标准 3DGS 密度控制依赖启发式视空间梯度、尺度阈值和全局不透明度重置，而没有显式评估每次分裂、克隆或不透明度更新对降低损失的效用，因此可能把基元分配到已充分重建的区域、漏掉欠重建结构，并通过全局不透明度变化破坏训练稳定性。

### 核心思路/方法
论文把自适应密度控制视为一系列局部损失下降决策，推导高效的、基于 Taylor 的近似的逐 Gaussian 代理量，用于预测分裂、克隆和不透明度衰减三种基元级操作引起的目标变化，形成统一的损失感知框架。其三个组件为：
1. 将二阶分裂扩展到归一化的联合位置-尺度空间，使子基元不仅能调整位置，也能调整各向异性范围；
2. 将重复克隆表述为代理最小化问题，只选择复制贡献被预测能改善重建的 Gaussian，并为每个子基元分配有原则的不透明度；
3. 用选择性软不透明度衰减替代全局不透明度重置，削弱有害基元同时保留有用基元。

### 主要贡献
- 将 3DGS 自适应密度控制重构为局部损失下降决策集合。
- 提出基于 Taylor 的逐 Gaussian 代理量，预测分裂、克隆与不透明度衰减造成的目标变化。
- 将二阶分裂扩展到归一化联合位置-尺度空间。
- 将克隆建模为代理最小化并赋予子基元原则化不透明度。
- 以选择性软不透明度衰减替代全局不透明度重置。
- 摘要称在标准 3DGS 基准上实现更有针对性的基元分配，并在可比或更小 Gaussian 预算下取得更好的渲染质量。

### 局限性
摘要未提供足够信息说明计算开销、Taylor 近似的误差边界、超参数敏感性、具体数据集与定量指标、与各类基线的完整对比，以及失败场景或适用限制。

### 阅读优先级
中。理由：该工作针对 3DGS 密度控制中的启发式与全局重置问题提出统一损失感知替代方案，问题定位清晰且方法组件具体；但摘要未给出定量结果与实现细节，是否值得优先精读取决于读者对 3DGS 训练效率与基元分配方向的关注程度。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：VLSplat: Vision-Language Guided Object-Centric 3D Gaussian Splatting via Scene Graph
- 作者：Yuntae Jeon, Younho Jeon, Sujin Jin, Sungho Jo, Seunghee Park
- 出版日期：2026-11-01T14:20:38Z
- 分类：Neural Scene Representations & Rendering（主分类；无副分类信息）
- 链接：摘要页 https://arxiv.org/abs/2611.01939 ；PDF https://arxiv.org/pdf/2611.01939 ；项目页 https://vlsplat.github.io/

### 一句话总结
VLSplat 提出一种由视觉-语言模型提供对象级语义先验、并以对象组场景图进行细化的 3D Gaussian Splatting 语义提升方法，旨在缓解仅依赖 2D 分割掩码监督所导致的局部证据驱动问题。

### 研究问题
摘要指出，现有面向 3D Gaussian Splatting 的 2D-to-3D 语义提升方法主要依赖 2D 分割监督，缺少对象级先验，导致学到的表示更多由局部掩码证据驱动，而非整体对象结构。论文关注的核心问题是：如何在 3D Gaussian Splatting 中实现以对象为中心、语义一致且结构完整的语义提升。

### 核心思路/方法
- 在基于掩码的语义提升基础上，引入来自视觉-语言模型的对象级语义先验。
- 使用对象组场景图（object-group scene graph）对高斯表示进行细化。
- 细化通过两个语言引导模块完成：
  - 组内细化（intra-group refinement）：抑制对象组内部的语义噪声；
  - 组间获取（inter-group acquisition）：从相邻组中引入结构相关的候选，扩展对象支撑区域。

### 主要贡献
- 提出 VLSplat，一种视觉-语言引导的、以对象为中心的 3D Gaussian Splatting 语义提升方法。
- 将视觉-语言模型的对象级语义先验与对象组场景图结合，用于细化高斯表示。
- 设计组内细化与组间获取两个语言引导模块，分别针对组内语义噪声和对象支撑区域扩展。
- 摘要称在室内场景数据集上的广泛实验表明，方法提升了对象级类别的语义一致性与结构完整性。
- 公开代码与模型（项目页链接由摘要给出）。

### 局限性
- 具体实验设置、数据集名称、评价指标与定量结果：摘要未提供足够信息。
- 与基线方法的详细对比数值与消融实验细节：摘要未提供足够信息。
- 方法对视觉-语言模型质量的依赖程度、失败案例与计算开销：摘要未提供足够信息。
- 场景图构建方式及其鲁棒性分析：摘要未提供足够信息。
- 方法在室外场景或更大规模场景中的泛化能力：摘要未提供足够信息。

### 阅读优先级
中。理由：该论文聚焦 3D Gaussian Splatting 的语义理解与对象级语义提升，问题定位清晰，方法结合视觉-语言先验与场景图细化，具有一定新意；但摘要未给出定量结果、数据集细节与消融信息，是否显著优于现有方法尚无法仅凭摘要判断。若读者关注 3D Gaussian Splatting 语义表示、开放词汇/视觉-语言引导的 3D 场景理解，可列为中高优先级；否则可列为中低优先级。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：AbacusGS: Gaussian Splatting without Per-Splat Sorting
- 作者：Jiacheng Ding, Yanliang Qi, Cong Guo, Peihua Mai
- 出版日期：2026-11-01T04:05:12Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.01534) / [PDF](https://arxiv.org/pdf/2611.01534)

### 一句话总结
AbacusGS 将 3DGS 场景的混合顺序写入场景布局，按八叉树盒子组织 splat，使每帧只需对可见盒子排序并用一次点积决定盒内读写方向，从而避免逐 splat 排序。

### 研究问题
3D Gaussian Splatting 每帧都要按深度对每个 splat 排序。对于使用硬件光栅器绘制 splat、并在 CPU 上排序的查看器（如多数 Web 和移动端查看器），这一排序占用大部分帧时间。论文关注如何减少或避免这种逐 splat 排序开销。

### 核心思路/方法
- 将 splat 分组为八叉树盒子，每个盒子最多 128 个 splat。
- 在写入时沿选定轴按顺序存储每个盒子，把混合顺序编码进场景布局。
- 每帧只对可见盒子排序，并用每个盒子一次点积决定该盒子是正向还是反向读取。
- 通过短时间的顺序感知微调将现有 3DGS 模型转换为 AbacusGS，同时保持 3DGS 的 over 算子不变。
- 还提出每 splat 17 字节的紧凑格式，以及使用相同顺序的 CUDA tile 渲染器。

### 主要贡献
- 提出无需逐 splat 排序的 AbacusGS 表示与渲染思路：把混合顺序存入场景布局，每帧仅排序可见盒子。
- 给出将现有 3DGS 模型转换为 AbacusGS 的顺序感知微调方法，且不改变 3DGS 的 over 算子。
- 在 13 个标准场景上，相比同等微调的 3DGS 模型平均损失 0.13 dB PSNR。
- 在 CPU 上对 splat 排序的 OpenGL 查看器中，帧渲染速度相比逐 splat 排序快 4.5 倍。
- 提出每 splat 17 字节的紧凑格式及使用同一顺序的 CUDA tile 渲染器；代码将发布。

### 局限性
- 摘要仅报告了平均 PSNR 损失和 OpenGL 查看器中的 4.5 倍加速，未提供更多场景级误差分布、其他硬件或渲染后端的具体性能数据。
- CUDA tile 渲染器和紧凑格式的效果细节：摘要未提供足够信息。
- 方法依赖八叉树盒子划分与顺序感知微调，其在不同场景规模、复杂度或动态场景下的适用性：摘要未提供足够信息。
- 与其它加速排序或渲染方案的全面对比：摘要未提供足够信息。

### 阅读优先级
中。理由：论文针对 3DGS 中逐 splat 排序这一明确性能瓶颈，提出结构清晰、改动较小的场景布局与排序替代方案，并给出 PSNR 损失和 OpenGL 查看器加速数据；但摘要未提供充分实验细节与多后端验证，适合对 3DGS 渲染效率、Web/移动端查看器优化感兴趣的读者进一步阅读全文确认。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MoSoLoco: Monocular 3D Human Localization through Visual Latent Features and Social Context
- 作者：Yasamin Borhani, Javad Khoramdel, Yang Gao, Po-Chien Luan, Alexandre Alahi
- 出版日期：2026-11-02T14:20:20Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供）
- 链接：[摘要](https://arxiv.org/abs/2611.03189) | [PDF](https://arxiv.org/pdf/2611.03189)

### 一句话总结
MoSoLoco 是一种逐帧单目 3D 人体定位器：它复用姿态检测器的内部视觉特征并结合 2D 骨架，且可选地引入同帧稀疏多人上下文，在 JRDB 和 NuScenes 上取得改进，并保持可用于 Jetson AGX Xavier 推理的轻量性。

### 研究问题
从单目相机估计人的度量 3D 位置对机器人导航和运动预测很重要。基于姿态的轻量定位器因使用紧凑 2D 关键点，适合算力有限的机器人硬件，但通常会丢弃姿态估计器计算出的更丰富视觉表示。论文希望在不额外引入 RGB 或深度编码器的前提下，利用这些被丢弃的内部视觉特征和稀疏多人上下文来改善定位。

### 核心思路/方法
- 输入为逐帧单目图像中检测到的 2D 骨架；方法复用姿态检测器的内部视觉特征，而不是只使用 2D 关键点。
- 不额外增加 RGB 或深度编码器，直接结合姿态检测器内部视觉特征与检测到的 2D 骨架进行 3D 人体定位。
- 进一步引入同帧的稀疏多人上下文（附近检测）来细化个体位置估计。
- 下游通过受控轨迹预测实验评估收益；完整流程声称适合在 Jetson AGX Xavier 上高效推理。

### 主要贡献
- 提出 MoSoLoco：逐帧单目 3D 人体定位器，结合姿态检测器内部视觉特征与 2D 骨架，无需额外 RGB 或深度编码器。
- 引入稀疏同帧多人上下文模块，用同一图像中的附近检测进一步细化个体位置。
- 在 JRDB 和 NuScenes 上实验：复用姿态检测器表示改善定位，JRDB 最佳误差相对最强被评估的基于关键点基线降低约 23%。
- 通过受控轨迹预测实验显示下游收益，并说明完整流程适合 Jetson AGX Xavier 高效推理。

### 局限性
- 摘要未提供足够信息说明方法在遮挡、远距离、多人密集场景或跨数据集泛化方面的具体失败模式。
- 摘要未提供足够信息说明 23% 误差降低对应的具体误差指标定义、比较协议和统计显著性。
- 摘要未提供足够信息说明 Jetson AGX Xavier 推理的帧率、延迟、功耗或内存占用等量化指标。
- 摘要未提供足够信息说明轨迹预测实验的设置、指标和增益幅度。

### 阅读优先级
中。理由：论文聚焦机器人/具身应用中的轻量单目 3D 人体定位，问题明确且声称在 JRDB 上相对关键点基线显著降低误差，并强调边缘设备推理与下游轨迹预测收益；但摘要未给出方法细节、完整实验协议和量化效率数据。是否优先阅读取决于读者对轻量机器人感知、姿态特征复用或多人体上下文定位的兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation
- 作者：Zhongkai Gu, Yang Liu, Wei Zhu, Mitsuhiro Hayashibe
- 出版日期：2026-11-02T11:36:51Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.02968 ；PDF https://arxiv.org/pdf/2611.02968

### 一句话总结
ReContact 以物体为中心的接触计划来重建并重定向视频中的人—物交互，使类人机器人能够在遮挡和接触力要求下学习全身接触切换操作。

### 研究问题
论文关注从人类视频学习类人机器人操作时的两个问题：一是身体遮挡会破坏物体位姿跟踪并污染重定向后的运动；二是仅精确复现物体轨迹，并不能保证机器人在预期接触点施加稳定力，可能导致后续阶段滑移或掉落。目标是把人类视频中的接触切换转化为机器人可执行的、富含接触的全身操作策略。

### 核心思路/方法
方法核心是“以物体为中心的接触计划”，该计划规定接触阶段、接触对、锚点、按压方向以及粘着或滑动模式。利用接触先验在遮挡情况下稳定物体位姿重建。在冻结的全身跟踪器之上训练一个残差策略，奖励其在计划锚点处发生接触，并使力的方向与指定方向对齐。摘要还提到用一个策略在 247 条参考上训练，并针对新放置重新求解。

### 主要贡献
- 提出 ReContact，通过以物体为中心的接触计划重建并重定向人—物交互。
- 利用接触先验缓解遮挡对物体位姿重建的影响。
- 在冻结全身跟踪器上使用残差策略，奖励按计划锚点和方向施加接触力。
- 仿真中，在大腿支撑的再抓取任务上，ReContact 在三个训练种子下平均 83.5% 的回合实现计划的双掌底部保持，而最佳适配基线为 0.16%。
- 一个在 247 条参考上训练的策略针对新放置重新求解后，将工作空间内管件传递成功率从 20.4%（仅源参考）提升到 97.8%。
- 在真实 Unitree G1 上，策略执行了七项富含接触的操作任务和两项移动操作任务。

### 局限性
摘要未提供足够信息说明方法的失败案例、对视频质量或遮挡程度的敏感边界、真实机器人实验的定量成功率、泛化到未见物体类别的能力，以及计算成本与训练数据规模的具体限制。

### 阅读优先级
高。理由：该工作直接针对从人类视频到类人机器人富含接触全身操作的关键瓶颈，摘要给出了明确的仿真定量对比和真实机器人任务展示，且提出的接触计划表示对遮挡与接触力稳定性问题有针对性；但真实实验的定量细节需阅读全文确认。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Scaling Action-Free Video Latent Prediction for Transferable Representations in End-to-End Autonomous Driving
- 作者：Xingtai Gui, Xubin Zhou, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan, Jianbing Shen
- 出版日期：2026-11-02T09:54:12Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.02853；PDF https://arxiv.org/pdf/2611.02853

### 一句话总结
论文提出 ScaleDrive，一个仅用大规模互联网开放世界驾驶视频、无需动作标注的驾驶导向预训练框架，并通过冻结预训练视频编码器，研究无动作视频潜变量预测的规模化能否为端到端自动驾驶规划提供可迁移的视觉表征。

### 研究问题
端到端自动驾驶策略需要同时捕捉空间场景结构与时间动态的视觉表征。视频潜变量预测已被视为学习时空视觉表征的有效范式，但论文指出：**用无动作驾驶视频规模化这一目标，是否能产生有利于端到端规划的表征，仍不清楚**。因此论文关注无动作视频潜变量预测作为可扩展预训练目标时的表征迁移问题。

### 核心思路/方法
- 将**无动作视频潜变量预测**作为可扩展的预训练目标进行研究。
- 提出 **ScaleDrive**：面向驾驶的框架，**仅在大规模互联网开放世界驾驶视频上预训练**，不使用动作标注，也不使用基准特定数据。
- 在下游端到端规划训练中**保持预训练视频编码器冻结**，以隔离并评估从互联网驾驶视频中学到的表征的可迁移性。
- 通过**自运动（ego-motion）与深度探针**分析冻结表征中编码的时间与几何信息是否随无动作视频预训练规模化而逐步增强。
- 系统研究视觉表征在**不同端到端驾驶策略**与**闭环基准**之间的迁移效果。

### 主要贡献
- 研究并验证了无动作视频潜变量预测作为可扩展预训练目标在端到端自动驾驶中的价值。
- 提出 ScaleDrive，仅依赖大规模互联网开放世界驾驶视频预训练，不依赖动作标注或基准特定数据。
- 通过冻结编码器的设置隔离表征迁移性，并用自运动与深度探针表明：规模化无动作视频预训练会逐步增强冻结表征中的时间与几何信息。
- 摘要称 ScaleDrive 在不同端到端驾驶策略和闭环基准上**一致提升下游性能**，说明规模化无动作视频潜变量预测得到的表征可跨规划策略架构、评估场景与协议泛化。

### 局限性
- 摘要未提供足够信息说明预训练视频数据的具体规模、来源构成与筛选标准。
- 摘要未提供足够信息说明自运动与深度探针的具体设计、评价指标与量化结果。
- 摘要未提供足够信息说明下游端到端规划策略、闭环基准、评价协议及性能提升幅度的具体细节。
- 摘要未提供足够信息说明计算成本、预训练效率或规模化带来的资源需求。
- 摘要未提供足够信息说明冻结编码器之外的其他迁移设置或消融实验细节。
- 摘要未提供足够信息说明方法在真实道路部署、安全性与极端场景下的表现。

### 阅读优先级
**中**。理由：论文主题直接关联端到端自动驾驶中的可迁移视觉表征预训练，且“无动作、仅互联网驾驶视频、冻结编码器评估迁移”的研究设定具有明确问题意识；但当前仅能基于摘要判断，关键实验规模、基准细节与提升幅度均未提供，适合作为相关方向的重点跟踪候选，而非仅凭摘要即可高置信度优先精读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation
- 作者：Gyeonghun Kim, Donghoon Kim, Minsoo Choi, Suyun Lee
- 出版日期：2026-11-02T07:20:12Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.02660) / [PDF](https://arxiv.org/pdf/2611.02660)

### 一句话总结
HeLM 提出一种分层 VLA 框架，通过显式语言记忆、因子化事件检测与事件触发式记忆更新，使机器人操作能够应对需要工作记忆的非马尔可夫任务。

### 研究问题
现有 VLA 模型多依赖马尔可夫假设，仅将当前观测映射为动作，难以在需要历史信息的非马尔可夫环境中完成任务。论文关注机器人操作中“工作记忆”缺失的问题，尤其是跨任务边界仍需保持上下文的任务场景。

### 核心思路/方法
受人类“内心独白”启发，HeLM 将任务相关历史以显式语言形式保存，并采用分层 VLA 框架。方法包含因子化的事件检测和由事件触发的记忆更新机制，从而在非马尔可夫操作任务中维护任务相关历史。摘要未提供更具体的网络结构、事件定义或训练细节。

### 主要贡献
- 提出 HeLM，一种分层显式语言记忆 VLA 框架，用于非马尔可夫机器人操作。
- 通过因子化事件检测与事件触发记忆更新，以显式语言维护任务相关历史。
- 在 10 个非马尔可夫真实世界任务、56 个变体上进行评估，其中包括五个新提出的跨回合任务，要求跨任务边界保持上下文。
- 相比最强基线，回合内成功率提升 12.8 个百分点；在组合泛化任务上达到 78% 子任务成功率。
- 在长时程场景下，相比关键帧基线最多使用 4.5 倍更少内存，运行速度快 2.5 倍。

### 局限性
摘要未提供足够信息说明方法在更多任务类型、不同机器人平台或更长时程下的泛化能力；也未提供失败案例分析、计算开销的绝对数值、事件检测错误的影响以及记忆内容质量的评估细节。摘要未提供足够信息。

### 阅读优先级
中。理由：论文聚焦 VLA 的非马尔可夫操作与显式语言记忆，问题定义清晰，并给出真实世界多任务评估与效率对比；但摘要未展开方法细节和局限性分析，适合关注机器人操作记忆机制与 VLA 架构的研究者进一步阅读全文确认。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Interactive 3D Cutaway Visualization for Subsurface Target Localization in Robot-Assisted Surgery
- 作者：Yuxin Chen, Wenxuan Wang, Wanwen Chen, Qi Zeng, Septimiu E. Salcudean
- 出版日期：2026-11-02T05:07:26Z
- 分类：主分类 Embodied / Robotics / AR Applications；无副分类
- 链接：摘要页 https://arxiv.org/abs/2611.02537 ；PDF https://arxiv.org/pdf/2611.02537

### 一句话总结
该论文提出名为 Virtual Box 的可交互 3D 剖切可视化界面，并在组织体模对照实验中考察其相较深度增强混合 AR 叠加显示，对机器人辅助手术中皮下靶点定位的影响。

### 研究问题
摘要指出，混合 AR 叠加显示可能产生深度线索歧义，使皮下解剖结构看起来悬浮于组织表面之上。论文研究的问题是：交互式 3D 剖切可视化能否改善机器人辅助的目标定位。

### 核心思路/方法
论文提出 Virtual Box，一种交互式 3D 剖切界面，允许用户独立操纵观察视角以检视皮下靶点。研究采用受控、平衡设计的受试者内组织体模实验：15 名工程学生分别使用 Virtual Box 和深度增强混合 AR 叠加显示，在水箱中将 da Vinci 器械定位到虚拟靶点。使用配准的 3D 经直肠超声测量 3D 定位误差与深度误差，并采集完成时间和主观评分。

### 主要贡献
- 提出 Virtual Box 交互式 3D 剖切可视化界面，用于检视皮下靶点并支持独立操纵观察视角。
- 在 15 名工程学生的组织体模受试者内实验中，报告 Virtual Box 相较深度增强混合 AR 叠加显示降低了定位误差：平均 3D 误差由 12.92 mm 降至 4.96 mm（降低 61.6%），深度误差由 9.48 mm 降至 2.07 mm（降低 78.2%），两者均 p < 0.001。
- 报告空间理解、深度感知和信心评分更高（均未校正 p < 0.001），完成时间由 21.64 s 增至 32.58 s（p = 0.008），总体工作负荷无显著差异。
- 结论认为 Virtual Box 在该受控任务中改善了定位准确性和感知空间理解，但增加了完成时间，支持进一步评估其用于手术导航。

### 局限性
- 实验对象为 15 名工程学生，非临床外科医生；摘要未提供足够信息说明该样本对临床用户的代表性。
- 实验任务为水箱中的组织体模虚拟靶点定位，非真实手术场景；摘要未提供足够信息说明在真实组织、呼吸运动或临床工作流中的表现。
- 摘要未提供足够信息说明误差测量以外的安全性、学习效应、长期使用效果或不同界面参数的影响。
- 完成时间显著增加；摘要未提供足够信息说明该时间代价在临床场景中是否可接受。
- 摘要未提供足够信息说明统计细节（如多重比较校正以外的效应量）、用户主观反馈的具体内容及失败案例。

### 阅读优先级
中。理由：论文针对机器人辅助手术中 AR 深度线索歧义这一明确问题，给出了可交互 3D 剖切方案，并在受试者内体模实验中报告了较大幅度的定位误差降低，主题与机器人辅助手术和 AR 应用相关；但证据来自 15 名工程学生的小样本体模研究，且完成时间增加，摘要未提供临床验证信息。若关注手术导航中的 3D 可视化与深度感知，值得阅读；若关注临床有效性，则需等待进一步评估。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：AgiWorld: An Agentic Video World Model for Building Persistent Worlds
- 作者：Shaoheng Fang, Yiqun Mei, Hanwen Jiang, Xin Sun, Haitian Zheng, Hao Tan, Kalyan Sunkavalli, Georgios Pavlakos, Qixing Huang, Yiwei Hu
- 出版日期：2026-11-02T00:39:40Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.02341) / [PDF](https://arxiv.org/pdf/2611.02341)

### 一句话总结
AgiWorld 是一个“智能体式”视频世界模型，通过智能体高层规划与视频生成模型低层实现的闭环，从单张图像和自由形式指令出发，构建在长时间探索中保持持久一致的世界。

### 研究问题
现有交互式视频世界模型虽然能从单张图像生成视觉上吸引人的视频，但存在两个问题：
1. 依赖用户提供相机运动和文本提示等低层控制，用户需要付出大量努力才能实现高层意图；
2. 随着探索推进，生成的世界难以保持持久性（persistence）。

论文旨在解决：如何从单张图像和自由形式指令出发，自动进行高层规划并生成在长时间探索中保持一致、忠实于用户意图的持久世界。

### 核心思路/方法
论文提出 AgiWorld，一个智能体式视频世界模型，分为两个层级：

- **高层规划（AgiWorld-Agent）**：智能体在世界状态中设计世界及其探索旅程，并指导探索。
- **低层实现（AgiWorld-WM）**：视频世界模型逐块（chunk by chunk）生成视频，并将其与几何信息一起存入空间记忆（spatial memory）；智能体从该空间记忆中更新其世界状态。

两层通过**共享空间记忆**以及**度量相机轨迹与结构化提示的接口**进行协同设计，形成闭环，使世界忠实于用户意图，并使智能体的世界状态与生成内容保持一致。

针对长时 rollout 中空间记忆的遮挡和累积几何误差，AgiWorld-WM 提出：
- **遮挡感知历史选择（occlusion-aware history selection）**：按表面可见性检索过去视角；
- **基于可靠性的记忆维护（reliability-based memory maintenance）**：偏好可靠几何与更早的观测。

### 主要贡献
1. 提出 AgiWorld，一个智能体式视频世界模型，从单张图像和自由形式指令构建持久世界。
2. 设计高层智能体规划与低层视频生成相结合的闭环框架，通过共享空间记忆和度量相机轨迹/结构化提示接口协同两层。
3. 提出遮挡感知历史选择与基于可靠性的记忆维护，以应对长时 rollout 中的遮挡和累积几何误差。
4. 摘要称 AgiWorld-WM 在世界重访与探索基准上取得最先进的整体性能；定性结果与消融表明，AgiWorld 能在分钟级旅程中依据自由形式指令构建持久世界。
5. 论文指出持久性并非仅来自视频模型本身，而来自其与智能体的闭环。

### 局限性
- 摘要未提供足够信息说明具体的基准名称、评测指标、定量对比数值和消融实验细节。
- 摘要未提供足够信息说明方法对计算资源、推理时延或长时 rollout 上限的要求。
- 摘要未提供足够信息说明失败案例或方法在哪些场景下不适用。
- 摘要未提供足够信息说明“分钟级旅程”的具体时长范围与可扩展性边界。

### 阅读优先级
**中**。理由：论文主题涉及视频世界模型、智能体规划与持久世界构建，属于 Embodied / Robotics / AR Applications 方向，问题定义清晰且方法闭环设计有吸引力；但摘要未提供定量实验细节、基准名称和失败分析，需阅读全文才能判断其实际效果与可复现性。若读者关注交互式视频生成、空间记忆或智能体与世界模型结合，可优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GoalDex: Learning Image-Goal-Conditioned Policies for Dexterous In-Hand Manipulation
- 作者：Arjun Bhardwaj, Mayank Mittal, Maximum Wilder-Smith, Vaishakh Patil, Marco Hutter
- 出版日期：2026-11-01T20:19:51Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：未提供
- 链接：摘要页 https://arxiv.org/abs/2611.02171 ；PDF https://arxiv.org/pdf/2611.02171

### 一句话总结
提出一种不依赖显式物体位姿估计的端到端视觉运动框架，用 RGB 观测与本体感知学习灵巧手内重定向策略，并支持以图像目标直接指定目标物体构型。

### 研究问题
摘要指出，灵巧手内操作通常围绕显式物体位姿估计来建模，但在严重手—物遮挡下可靠位姿跟踪困难，且往往需要物体特定监督。这种对位姿估计的依赖形成感知与控制之间的瓶颈，可能限制鲁棒性与可扩展性。

### 核心思路/方法
- 构建端到端视觉运动框架，用于灵巧手内重定向，输入为 RGB 观测与本体感知，不进行中间位姿估计。
- 通过从具有特权状态的教师策略进行行为蒸馏，并结合辅助重建目标，联合学习视觉表征与控制策略。
- 引入图像目标条件的重定向，使目标物体构型可直接由图像指定，而非规范位姿表示。

### 主要贡献
- 提出不依赖显式位姿估计的端到端 RGB 加本体感知的灵巧手内重定向框架。
- 采用行为蒸馏与辅助重建目标联合学习视觉表征与控制策略。
- 提出图像目标条件的重定向设定，用图像而非规范位姿表示指定目标构型。
- 在仿真中跨多种物体几何与实例评估，声称一致优于基于位姿的方法以及基于预训练视觉编码器的策略。
- 展示单一图像目标条件策略在五个真实物体上的直接 sim-to-real 迁移，表明无需显式位姿估计也可实现准确灵巧重定向。

### 局限性
- 摘要未提供足够信息说明具体实验规模、物体集合细节、成功率指标、对比方法配置与统计显著性。
- 摘要未提供足够信息说明 sim-to-real 迁移的失败案例、鲁棒性边界与安全约束。
- 摘要未提供足够信息说明方法对严重遮挡以外其他感知挑战的适用性。
- 摘要未提供足够信息说明计算成本、训练数据需求与实时性表现。

### 阅读优先级
中。理由：论文主题聚焦灵巧手内操作中去除显式位姿估计瓶颈，并提出图像目标条件策略与 sim-to-real 迁移，问题设定清晰且与感知—控制耦合相关；但摘要未给出定量结果与实验细节，是否值得优先精读取决于读者对灵巧操作、视觉运动策略与图像目标条件控制的直接兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Reconstruction as Spatial Evaluation: Diagnosing Cross-View Spatial Intelligence in Large Vision-Language Models
- 作者：Junfei Wu, Qiuyue Wang, Xuhong Huang, Qihang Peng, Mingsheng Li, Jian Guan, Qiang Liu, Shu Wu, Liang Wang, Shuai Bai, Tieniu Tan
- 出版日期：2026-11-01T16:16:15Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.02026 ；PDF https://arxiv.org/pdf/2611.02026

### 一句话总结
论文提出以多视角 3D 场景重建作为评测载体，用结构一致性和度量准确性两个维度诊断大型视觉语言模型（LVLMs）的跨视角空间智能，并发现模型在相对场景结构上表现较好、但在物理尺度与相机锚定位置上存在明显差距。

### 研究问题
论文关注 LVLMs 的空间智能，即模型能否把局部视觉观察组合成几何一致的物理世界表示。作者指出现有评测存在两类不足：静态基准多评估孤立的空间判断（如相对方向或距离），而交互式具身评测又把感知与探索、规划、控制及模拟器执行混在一起。因此，论文试图在二者之间建立更聚焦的评测方式，用于诊断跨视角空间智能及其与下游导航的关系。

### 核心思路/方法
论文提出 RECONSPATIAL 基准，覆盖室内、桌面和户外环境，围绕多视角 3D 场景重建展开评测。任务形式是：给定真实多视角图像和目标物体查询，要求 LVLMs 在共享的、以相机为锚点的度量坐标系中联合预测有向 3D 边界框。评测沿两个互补维度展开：Structure 关注相对布局，Metric 关注物理尺度和相机锚定放置。基准还包含九个原子空间 QA 任务，分为 Geometric Perception 和 Spatial Relations 两组，用于探查联合重建涉及的空间能力；并通过离线导航将评测扩展到路径规划。论文还进行了诊断分析、3D 地图注入实验和空间微调实验。

### 主要贡献
- 提出 RECONSPATIAL 基准，以多视角 3D 场景重建评测 LVLMs 的跨视角空间智能，覆盖室内、桌面和户外环境。
- 设计 Structure 与 Metric 两个互补评测维度，并设置九个原子空间 QA 任务，用于关联分析重建质量与原子空间能力。
- 对 18 个前沿 LVLMs 进行评测，报告了相对场景结构与度量重建之间的持续差距；摘要给出 GPT-6-Astra 在 Structure 上为 81.4%、在 Metric 上为 58.7% 的示例。
- 通过诊断分析表明，关系一致性本身不足以保证度量准确性；通过 3D 地图注入实验区分场景构建与路径规划，并说明几何误差如何限制导航成功。
- 摘要称空间微调在空间和通用视觉语言基准上均带来广泛迁移。

### 局限性
摘要未提供足够信息说明基准规模、数据来源细节、标注质量控制、评测协议细节、各模型完整结果、统计显著性、计算成本或空间微调的具体设置。因此无法基于摘要判断这些方面的局限。摘要本身提到现有静态基准和交互式具身评测的不足，但未明确列出 RECONSPATIAL 自身的局限。

### 阅读优先级
高。理由：论文直接针对 LVLMs 跨视角空间智能的评测缺口，提出重建式基准和结构/度量双轴诊断，并给出 18 个前沿模型的评测结果及导航相关分析；对关注具身智能、机器人、AR 应用和视觉语言模型空间能力评测的研究者有较强相关性。但需注意，摘要未提供实验细节和基准规模，深入采用前应阅读全文核实。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：OCBI: Order-Sensitive Cross-Branch Interaction for Image Manipulation Localization
- 作者：Zhouli Yu
- 出版日期：2026-11-01T10:46:20Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2611.01783) ｜ [PDF](https://arxiv.org/pdf/2611.01783)

### 一句话总结
论文提出 OCBI，将 RGB 引导的跨分支注意力与取证自注意力在组合顺序上的差异作为建模对象，用于图像篡改定位，并在摘要报告的设定下取得相对基线的小幅指标提升。

### 研究问题
图像篡改定位需要结合语义结构与取证痕迹来识别被修改的像素。摘要指出，分支内的空间混合与 RGB 引导的跨分支混合在按相反顺序组合时会产生不同的信息，而论文关注如何建模这两种组合顺序之间的差异，并将其用于定位任务。

### 核心思路/方法
- 将 OCBI 定义为 Co-Transformers 的扩展，显式建模上述两种组合顺序之间的差异。
- 局部跨分支融合模块使用 RGB 引导的跨注意力与取证自注意力的交换子（commutator），为特征传递加入可学习的带符号修正。
- 采用逐像素自适应多尺度聚合，在预测前融合空间上下文。
- 使用 Co-Transformers 作为骨干与监督方式。
- 对比实验中，基线为重新训练的 Co-Transformers；训练设定为仅使用 CASIA 任务训练、50 个 epoch 预算、取最终 epoch 评估。

### 主要贡献
- 提出以组合顺序差异为核心的 OCBI 方法，用于图像篡改定位。
- 设计基于交换子的局部跨分支融合，为特征传递引入可学习的带符号修正。
- 引入逐像素自适应多尺度聚合以融合空间上下文。
- 摘要报告的实验结果：在五个干净测试数据集上，OCBI 的宏平均 PixelF1 为 0.5773，比基线高 0.43 个百分点；在三个数据集上施加 JPEG 压缩、高斯模糊和缩放，共 21 个数据集-变换条件，平均 PixelF1 比基线高 0.95 个百分点。
- 具体消融实验、各数据集分项结果、计算开销等信息：摘要未提供足够信息。

### 局限性
- 摘要仅报告相对重新训练 Co-Transformers 的提升幅度；绝对性能（宏平均 PixelF1 为 0.5773）是否满足实际应用需求，摘要未提供足够信息。
- 训练仅使用 CASIA、50 个 epoch、最终 epoch 评估；该设定对结论泛化性的影响，摘要未提供足够信息。
- 鲁棒性仅覆盖 JPEG 压缩、高斯模糊和缩放三类变换及三个数据集；其他篡改类型、数据分布或攻击方式的适用性，摘要未提供足够信息。
- 方法依赖 Co-Transformers 骨干与监督，交换子修正和多尺度聚合各自的具体增益，摘要未提供足够信息。
- 计算复杂度、推理速度、参数量等工程指标，摘要未提供足够信息。
- 论文分类标注为 Embodied / Robotics / AR Applications，与图像篡改定位主题的匹配性，摘要未提供足够信息。

### 阅读优先级
中。理由：论文聚焦一个较具体的建模点（跨分支组合顺序差异），摘要给出了明确的对比设定和量化提升，适合关注图像篡改定位与跨分支注意力机制的研究者阅读；但提升幅度较小，且摘要未提供消融、分项结果与效率信息，若需要全面评估方法价值，需进一步阅读全文。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts
- 作者：Amir Hossain Raj, Xuesu Xiao
- 出版日期：2026-11-01T05:32:18Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2611.01600)｜[PDF](https://arxiv.org/pdf/2611.01600)

### 一句话总结
SCOUT 是一个面向遮挡场景的规划框架，利用以对象为中心的场景表示重建隐藏几何，并结合大语言模型（LLM）提出结构化动作候选与 MCTS（蒙特卡洛树搜索）的物理推演，以在密集杂乱环境中完成长程操作规划。

### 研究问题
机器人在杂乱空间中操作时，常需从目标、周围几何与可用自由空间被前景物体遮挡的部分视图进行规划。摘要指出，反应式策略容易忽略这些隐藏约束，而穷举搜索在密集杂乱中计算代价过高。因此，问题是如何在遮挡条件下高效规划，并推理隐藏几何对可行动作的限制。

### 核心思路/方法
- 采用以对象为中心的（object-centric）场景表示，重建隐藏几何，并导出关系型规划状态，用于刻画“遮挡层级”（blocker hierarchies）与“可达通道”（accessibility corridors）。
- 为应对杂乱环境中的巨大动作空间，由 LLM 提出结构化动作候选。
- 使用学习到的“动作条件世界模型”，通过 MCTS 对候选动作进行严格评估与推演（rollouts），从而将高层 deliberation 与落地的物理推演结合。
- 摘要称该框架为 occlusion-aware planning framework，目标是桥接高层推理与基于物理的推演评估。

### 主要贡献
- 提出 SCOUT 遮挡感知规划框架，结合对象中心场景表示、关系规划状态、LLM 动作候选生成与基于学习世界模型的 MCTS 评估。
- 在 “Reveal” 与 “Placement” 任务上进行评估，摘要称其优于 Vision-Language-Action（VLA）策略、具身智能体与 3D 世界模型，并在需要对遮挡几何进行推理的长程任务上有显著增益。
- 通过杂乱货架环境中的真实机器人操作验证框架鲁棒性。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性、对对象中心表示或世界模型精度的依赖程度，以及失败模式。
- 摘要未提供足够信息说明真实世界实验的规模、任务数量、成功率数值与对比基线细节。
- 摘要未提供足够信息说明 LLM 动作候选生成的具体接口、约束方式与潜在错误传播影响。
- 摘要未提供足够信息说明在更广泛遮挡类型、动态场景或不同机器人平台上的泛化能力。

### 阅读优先级
高。理由：该论文直接针对机器人操作中遮挡导致规划困难的问题，方法组合（对象中心表示 + LLM 候选 + 世界模型 MCTS）与长程杂乱操作规划高度相关，且摘要报告了仿真任务对比与真实机器人验证；若关注遮挡感知规划、世界模型推演或 LLM 辅助机器人决策，值得优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Shades of Success: Evaluating Manipulation Quality from Object-Centric Constraints
- 作者：Lorena Maria Genua, Sarvesh Prajapati, Ananya Trivedi, Taskin Padir
- 出版日期：2026-10-31T20:30:31Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.01250 ；PDF https://arxiv.org/pdf/2611.01250

### 一句话总结
论文提出 SPECTRA，一种以物体为中心的框架，从少量仿真 oracle 演示中学习相对位姿约束，并用 Task Quality Index Q∈[0,1] 量化刚体操作执行质量，以区分“成功但精度不同”的执行。

### 研究问题
学习型操作策略越来越能完成实际任务，但评估“任务完成得有多好”仍是基础挑战。二值成功标签只能确认成功，无法区分不同几何精度的成功执行。论文关注：如何在不依赖二值标签的情况下，量化刚体操作任务的执行质量。

### 核心思路/方法
- 从仿真中生成的一小组 oracle 演示出发，用与进度对齐的相对位姿表示物体交互。
- SPECTRA 从演示中识别哪些相对位姿方向受到约束，以及这些约束的允许变化范围。
- 这些约束构成评估机器人操作任务的参考。
- 对未见执行进行评分时，将超出允许变化范围的偏差汇总为 Task Quality Index Q，取值在 [0,1]。
- 摘要还提到：利用仿真中学到的任务参考，选择得分最高的演示用于在硬件上训练 diffusion policy。

### 主要贡献
- 提出 SPECTRA，一个以物体为中心、用于量化刚体操作执行质量的框架。
- 用进度对齐的相对位姿和允许变化范围建立任务约束参考，并给出 [0,1] 区间的 Task Quality Index Q。
- 在七个仿真任务上，每任务使用 30 条演示时，约束恢复准确率为 94%。
- 在三个学习策略的 rollout 上，SPECTRA 分数与人类判断的合并 Spearman 相关性为：全部 rollout p=0.81，成功 rollout 中 p=0.61，且在两个子集上均超过所有基线。
- 探索性结果显示，使用 SPECTRA 选出的最高分演示训练硬件上的 diffusion policy，成功率高于随机选择演示训练。

### 局限性
- 摘要仅报告七个仿真任务和三个学习策略的评估，未说明真实硬件上的系统评测规模。
- 硬件实验仅描述为“探索性结果”，未提供具体成功率数值或统计细节。
- 摘要未提供约束恢复准确率 94% 的具体误差类型、任务差异或消融分析。
- 摘要未提供 SPECTRA 对非刚体对象、复杂接触或非仿真演示的适用性信息。
- 摘要未提供计算开销、对 oracle 演示质量的敏感性等信息。
- 上述未提供的信息均属于“摘要未提供足够信息”。

### 阅读优先级
中。理由：论文直接针对操作策略评估中二值成功标签不足的问题，提出可量化的任务质量指标，并与人类判断做相关性比较，同时对策略训练数据选择有潜在应用价值；但摘要仅覆盖仿真任务与探索性硬件结果，是否具备广泛泛化性和实际部署价值仍需阅读全文确认。

</details>

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
