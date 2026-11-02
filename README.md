# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：62
- 分类分布：
  - Neural Scene Representations & Rendering: 22
  - 3D Reconstruction & Multi-view Geometry: 19
  - Embodied / Robotics / AR Applications: 11
  - Dynamic / 4D Reconstruction: 5
  - Geometry Foundation Models: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“重建—理解—生成”正在收敛为统一框架，而非独立流水线。**
   LucidLyra 将生成式 3D 重建与开放词汇语义、实例分组蒸馏到一个前馈模型；GenSight 把未来视频生成与深度、具身分割、光流放进同一个 DiT 的速度预测空间；SonoWorld4D 则把视觉 4D 场景与空间音频场联合生成。三篇论文的共同信号是：下游应用（机器人、物理 AI、可交互内容）不再满足于“好看的重建”，而要求重建结果自带语义、运动和物理一致性，且尽量走前馈、免逐场景优化路线。

2. **4D 与动态场景成为新前沿，评价维度从“视觉真实”扩展到“视听/物理一致”。**
   SonoWorld4D 定义 Video-to-4DAVScene 任务，把声音纳入 4D 场景；GenSight 用统一时空表示覆盖动态世界的几何、语义与运动；Hierarchical Diffusion 处理长视频相机可控生成中的几何漂移；LucidLyra 声称其潜变量形式可扩展到单目视频的动态结构化重建。动态重建正从“逐帧重建 + 事后一致性修补”转向“生成式扩散先验 + 显式几何约束”的组合。

3. **3D Gaussian Splatting 的竞争焦点从“能否实时渲染”转向“表示质量与感知可用性”。**
   今日多篇论文集中在 3DGS 的表示控制：ACD-GS 用二阶深度响应替代一阶屏幕梯度做致密化判据，抑制冗余高斯；BudSplat 在渲染预算下做前馈 3DGS 的基元剪枝；GradSplat 在前向传播内部用学习到的梯度步细化高斯形状；COGS 则直接质疑“高斯属性是否都有益”，发现属性子集可优于全集。这提示 3DGS 研究正在从追求 PSNR 转向紧凑性、几何准确性与属性可解释性。

4. **“野外/极端/分布外环境”成为 3D 视觉的集中验证场。**
   MLLM-GS 面向退化场景的新视角合成，用冻结 MLLM 先验做视图增强；RoSAMDepth 用 SAM 对象级先验提升自监督深度在不利条件下的鲁棒性；单目深度估计在月球环境中的有效性研究、SKiD-SLAM 的行星任务实地部署，共同构成“地球外/受限环境”这条应用线索。与之配套的是基准与评测反思：COGS 提供属性诊断基准，单视图新视角合成的位姿对齐论文指出评测协议本身可能不公平。

5. **具身与机器人方向出现“世界模型 + 数据/执行工程”双轮驱动。**
   GenSight 代表世界模型路线的统一化；DEED 则走另一条务实路线：通过演示扩展（多指令、多相机、多光照渲染）和执行设计（逆运动学、夹爪映射、闭环重规划）把预训练 VLA 策略适配到细粒度操作任务。同时，KITScenes Aerial 与单目 RGB 人体跟踪的决策级误差归因表明，社区在补齐“数据基准”和“安全决策评估”这两类基础设施，而非只堆模型。

#### 技术路线观察

**几何基础模型方向**
PhysInsert 最有代表性：它把 VGGT 几何流与图像流、文本流耦合，在目标场景特征监督下做空间一致的对象插入，并配套构建 Blender 渲染的严格对齐反事实配对数据集与 PhysInsert-Bench。这说明几何基础模型正被当作“可组合的几何先验模块”嵌入生成/编辑任务，而不再只是重建工具。风险在于，摘要未说明几何流是否冻结、如何与扩散生成端到端衔接，需全文确认。

**3D/4D 重建方向**
可分出三条子路线。其一是前馈生成式重建：LucidLyra 从视频潜变量前馈预测携带语义与实例的高斯；BudSplat、GradSplat 都在前馈 3DGS 框架内解决“预测质量落后于逐场景优化”的问题，前者靠预算约束剪枝，后者靠前向内部梯度细化。其二是扩散先验驱动的逆问题重建：极端稀疏视角 CT 论文在“训练稀疏、推理稀疏”设定下学姿态感知扩散先验，用测量保真、共享体积重投影和投影物理一致性引导采样。其三是全景/特殊成像几何：GOFish 直接在鱼眼图像上训练并栅格化超过 180° 视场，同时提取对齐网格，指向仿真就绪数字孪生这一明确下游。

**神经场景表示方向**
3DGS 相关论文呈现明显的“判据精细化”趋势：ACD-GS 质疑一阶梯度判据无法区分真实几何不连续与高频纹理，转而用二阶深度响应做非对称克隆/分裂调控；COGS 则从感知侧反向提问——哪些高斯属性真正被 3D 架构利用，并给出保留属性特定证据的 HALO 参考模型。两者合起来提示：表示层面的“长什么样”和感知层面的“被怎么用”需要联合设计，而不是各自优化。

**机器人/AR 应用方向**
应用侧的关键词是“资源约束”与“决策可信”。SKiD-SLAM 先调研真实行星任务的通信与计算预算，再据此选模块，并完成洞穴与模拟地形的实地部署；单目 RGB 人体跟踪论文提出双因素 Shapley 归因，把停止/继续决策错误拆分为安全规则贡献与感知贡献，并证明横向距离规则是平面距离的下界（安全但会产生多余停止）；DEED 把部署阶段的逆运动学、夹爪映射、闭环重规划视为与训练同等重要的设计对象。这些工作共同说明，机器人视觉的瓶颈正在从“感知精度”转向“感知误差如何影响下游决策”。

#### 值得优先阅读的论文

1. **SonoWorld4D（2610.40640）**
   提出新任务 Video-to-4DAVScene，把 4D 视觉与空间音频纳入同一框架，且支持实时新视角视觉与空间音频渲染。对做 4D 生成、多模态场景建模和 VR/AR 的人是方向性论文；即使不做音频，“单目视频 → 360 背景 + 显式运动轨迹 + 双空间扩散同步”的流程设计也值得借鉴。

2. **GenSight（2610.39232）**
   统一视频生成与稠密 4D 感知于单一预训练视频 DiT，且推理支持“多步生成 + 对齐稠密预测”与“单步稠密感知”两种模式。对具身世界模型、视频扩散用于几何感知两条线都有直接参考价值，是今日“统一化”趋势中最完整的一篇。

3. **LucidLyra（2610.40495）**
   前馈生成式重建 + 开放词汇语义 + 类别无关实例，且训练不需人工 3D 标注或多视角采集。如果关注“生成式重建结果能否直接被机器人查询使用”，这篇的任务定义与蒸馏方案是今日最贴近该问题的。

4. **ACD-GS（2610.39399）与 COGS（2610.39201）可组合阅读**
   前者从训练期致密化判据入手，后者从属性使用诊断入手，二者共同回答“3DGS 表示里哪些部分真正有用”。对做 3DGS 感知、压缩、架构设计的人，这两篇合读比单读一篇更能形成判断。

5. **单目 RGB 人体跟踪的决策级误差归因（2610.40199）**
   它不是性能刷榜论文，而是提出一种把安全规则与感知误差分离的评测方法，并给出横向距离规则的下界性质。对做机器人在人附近导航、感知安全评估的人，这类“决策级指标”方法论稀缺且可直接迁移。

#### 可能的研究机会

- **4D 视听场景的评测空白。** SonoWorld4D 建立了任务和框架，但摘要只提到真实动态场景评估与用户研究，未见标准化的视听一致性指标。可跟进：空间音频与视觉运动的事件级对齐度量、多声源一致性基准。

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-30T13:59:26-04:00
**Total number of papers:** 39
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

#### 2026-10-27 - GPA-VGGT: Geometry-Preserving Acceleration of VGGT

**Authors:** Muyeol Sung, Jangwon Kim, Jongwoo Lim
**Links:** [abs](https://arxiv.org/abs/2610.37000) - [pdf](https://arxiv.org/pdf/2610.37000)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GPA-VGGT: Geometry-Preserving Acceleration of VGGT
- 作者：Muyeol Sung, Jangwon Kim, Jongwoo Lim
- 出版日期：2026-10-27T10:46:52Z
- 分类：Geometry Foundation Models
- 链接：[摘要](https://arxiv.org/abs/2610.37000) / [PDF](https://arxiv.org/pdf/2610.37000)

### 一句话总结
GPA-VGGT 是一种免训练加速方法，它针对 VGGT 中开销很大的全局注意力做结构替换与 K/V 合并，目标是在获得与既有加速方法相当的加速比的同时，仍保留精确几何估计所需的信息。

### 研究问题
VGGT 这类前馈几何模型能在单次前向中从一到数百个视图恢复相机参数、深度图和点图，但它的全局注意力开销随帧数呈二次增长，并在长序列上主导端到端运行时间。已有的免训练效率方法（如 token merging）会带来精度下降，因此难以直接替代 VGGT。

### 核心思路/方法
- 在早期 block 中，用“帧注意力 + 共享的跨帧 K/V 集合”替代全局注意力。
- 在其余 block 中，只合并 keys 和 values，保留所有 queries。
- 恢复每个被合并 key 所代表 token 的注意力质量。
- 将匹配度量随机投影到 128 维，以降低匹配成本。
- 方法定位为 training-free（免训练）。

### 主要贡献
- 提出 GPA-VGGT，一种用于加速 VGGT 的免训练方法。
- 通过早期 block 的注意力替换与后续 block 的 K/V 合并策略，在获得与先前工作相当的加速比的同时，保留精确几何估计所需信息。
- 摘要称，在 AUC@3 指标下保留超过 99% 的 VGGT 位姿精度。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集、序列长度范围、绝对运行时间、与其他方法逐项精度对比、内存开销，也未说明随机投影或注意力质量恢复的消融结果与失败情形。

### 阅读优先级
中。理由：该工作直接针对 VGGT 长序列推理效率与几何精度保持之间的权衡，且声称免训练、位姿精度保留超过 99%，对该方向读者有参考价值；但当前仅有摘要，缺乏实验细节与完整对比，需阅读全文后再判断其通用性与稳健性。

</details>

<details>
<summary>Abstract</summary>

Feed-forward geometry models such as VGGT recover camera parameters, depth maps, and point maps from one to hundreds of views in a single forward pass, making them powerful backbones for multi-view 3D perception. However, VGGT's global attention is quadratic in the number of frames and dominates end-to-end runtime on long sequences, which has motivated a range of training-free efficiency methods such as token merging. These methods, however, come with a drop in accuracy that makes them hard to use in place of VGGT. We propose GPA-VGGT, a training-free acceleration method that replaces global attention in early blocks with frame attention augmented by a shared cross-frame K/V set. In the remaining blocks, we merge only keys and values while preserving all queries, restore the attention mass of the tokens each merged key represents, and randomly project the matching metric to 128 dimensions to reduce matching cost. Across diverse multi-view geometry tasks, GPA-VGGT provides training-free acceleration at speedups comparable to prior work while preserving the information required for precise geometric estimation, retaining over 99% of VGGT's pose accuracy under AUC@3.

</details>

## Dynamic / 4D Reconstruction

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

#### 2026-10-27 - 4D Reconstruction with Events & RGB

**Authors:** Dulanga Weerakoon, Darshana Rathnayake, Van Minh Do, Hemanth Sabbella, Kaichen Zhou, Fangneng Zhan, Alok Prakash, Sanjay E. Sarma, Archan Misra, Paul Pu Liang
**Links:** [abs](https://arxiv.org/abs/2610.36610) - [pdf](https://arxiv.org/pdf/2610.36610)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, dynamic 3D, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4D Reconstruction with Events & RGB
- 作者：Dulanga Weerakoon, Darshana Rathnayake, Van Minh Do, Hemanth Sabbella, Kaichen Zhou, Fangneng Zhan, Alok Prakash, Sanjay E. Sarma, Archan Misra, Paul Pu Liang
- 出版日期：2026-10-27T04:11:39Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.36610 ；PDF https://arxiv.org/pdf/2610.36610

### 一句话总结
该初步研究在现有纯 RGB 的 4D 重建模型 Monst3R 上增加一个事件相机输入分支，其余架构不变，在 3 个基准数据集上相对纯 RGB 基线平均降低 Abs Rel 3.4%，且改进随相机与物体运动幅度增大而更明显。

### 研究问题
从单一运动相机重建随时间变化的动态 3D 场景（4D 重建）对机器人与 AR/VR 应用很重要，但现有前馈方法仅依赖 RGB 帧，因而继承传统相机的失效模式，包括快速或非均匀相机与物体运动下的运动模糊和时间混叠。事件相机以微秒分辨率异步报告逐像素亮度变化，提供互补信号且基本不受上述伪影影响；问题是能否在不做完整架构重设计的情况下，把这一模态纳入现有基于 RGB 的 4D 重建流程。

### 核心思路/方法
论文进行一项初步研究，采用最小扩展：在已有的纯 RGB 4D 重建模型 Monst3R 上增加一个额外的事件相机输入分支，并保持架构其余部分不变。摘要将其描述为简单的 RGB-事件融合，并在 3 个基准数据集上评估。

### 主要贡献
- 提出并验证一种轻量、非侵入式的事件数据融合方式：仅为 Monst3R 增加事件输入分支，其余架构不变。
- 在 3 个基准数据集上，相对纯 RGB 的 Monst3R 基线，Abs Rel 平均降低 3.4%。
- 敏感性分析显示改进随相机和物体运动幅度增大而增长，在纯 RGB 重建退化最严重的高物体运动条件下增益最大。
- 作者据此认为，即使是轻量、非侵入式的事件数据融合也能实质提升 4D 重建鲁棒性，并以此动机推动未来更系统的架构研究。

### 局限性
- 摘要明确称其为 preliminary study（初步研究），并非完整架构探索。
- 仅报告 Abs Rel 平均降低 3.4% 及敏感性趋势；其他指标、数据集名称、具体实验设置与统计细节摘要未提供足够信息。
- 方法仅为在 Monst3R 上增加事件分支的最小扩展，未进行架构重设计；更系统的架构研究被留作未来工作。
- 事件相机数据采集条件、事件与 RGB 的同步/对齐方式、失败案例分析等摘要未提供足够信息。

### 阅读优先级
中。理由：主题属于动态/4D 重建与机器人、AR/VR 应用交叉方向，问题明确且事件相机与 RGB 融合的思路直接；但摘要定位为初步研究，方法为最小扩展，定量结果仅给出 Abs Rel 平均 3.4% 的相对改进，实验细节与架构创新有限。对关注事件相机用于 4D 重建或希望了解轻量融合可行性的读者有参考价值，对追求完整方法或充分实验对比的读者优先级较低。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic 3D scenes over time (4D reconstruction) from a single moving camera is central to robotics and AR/VR applications, yet state-of the-art feed-forward methods rely solely on RGB frames and therefore inherit the failure modes of conventional cameras, including motion blur and temporal aliasing under fast or non-uniform camera and object motion. Event cameras report per-pixel brightness changes asynchronously at microsecond resolution, offering a complementary signal that is largely immune to these artifacts, but whether this modality can be incorporated into existing RGB based 4D reconstruction pipelines without a full architectural redesign remains an open question. In this preliminary study, we investigate a minimal extension: we augment Monst3R, an existing RGB-only 4D reconstruction model, with an additional event-camera input branch, leaving the rest of the architecture unchanged. Across 3 benchmark datasets, this simple RGB-event fusion reduces Abs Rel by 3.4% on average relative to the RGB-only Monst3R baseline, and a sensitivity analysis shows that the improvement grows with the magnitude of camera and object motion, with the largest gains observed under high object motion conditions where RGB-only reconstruction degrades most. These early results suggest that even a lightweight, non-invasive fusion of event data can meaningfully improve 4D reconstruction robustness, motivating a more thorough architectural investigation in future work.

</details>

## 3D Reconstruction & Multi-view Geometry

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

#### 2026-10-27 - Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction

**Authors:** Prakhar Kaushik, Soumava Paul, Alan Yuille
**Links:** [abs](https://arxiv.org/abs/2610.37668) - [pdf](https://arxiv.org/pdf/2610.37668)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, surface reconstruction, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction
- 作者：Prakhar Kaushik, Soumava Paul, Alan Yuille
- 出版日期：2026-10-27T17:59:59Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37668) / [PDF](https://arxiv.org/pdf/2610.37668)

### 一句话总结
论文提出一种平面六边形表面基元“Hexels”，它使用带一阶空间颜色场的更少、更大的基元来表示 2D 图像与 3D 场景，以改善内存和计算受限场景下的质量-效率权衡。

### 研究问题
新视角合成与 3D 重建虽因辐射场和 splatting 快速发展，但内存与计算需求限制了它们在资源受限环境中的使用。论文关注：如何用更紧凑的表面基元，在降低内存和计算开销的同时，保持或提升场景渲染与重建质量。

### 核心思路/方法
- 提出称为 **Hexels** 的平面六边形表面元素，并为每个基元引入 **一阶空间颜色场**，用于高效表示 3D 场景与 2D 图像。
- 利用局部平面区域及平滑变化的外观，采用**更少、更大**的基元。
- 六边形支撑域被描述为面积和边界高效的域，局部颜色场用于捕捉单个基元内部的外观变化。
- 摘要称其作为通用基元，也可改进 2D 图像表示。

### 主要贡献
- 提出 Hexels 这种紧凑六边形表面基元，并用于高效 3D 场景和 2D 图像表示。
- 在 34 个场景上，与内存匹配的 2DGS 相比，Hexels 在不同数据集上 PSNR 提升 **4.53–7.38 dB**，且训练 VRAM 更低。
- 消融显示：按每个基元比较，Hexels 相比 2DGS 最高提升 **4.74 dB**，训练 VRAM 更低，FPS 快 **2.31 倍**。
- 在 15 个 DTU 扫描上，与内存匹配的 2DGS 相比，3D 表面重建误差降低 **28.9%**。
- 在 6 个 Tanks and Temples 表面场景上，Hexels 取得对比方法中最高的平均 F1（**34.38%**，2DGS 为 **31.72%**）。
- 摘要还称 Hexels 在 2D 图像表示上优于 Image-GS，并推动表面对齐基元在质量-效率权衡上的 Pareto 前沿。

### 局限性
- 摘要未提供足够信息说明具体数据集名称、训练时长、参数量、推理内存等完整实验细节。
- 摘要未提供足够信息说明方法在不同尺度、非平面区域、复杂反射或透明材质等困难场景下的失效情况。
- 摘要未提供足够信息说明六边形基元初始化、优化稳定性及实现复杂度等工程限制。
- 摘要未提供足够信息说明与更多类型基元或方法的系统性对比范围。

### 阅读优先级
**高**。理由：论文直接针对表面基元表示的质量-效率权衡，摘要给出了多数据集、多任务的定量结果，并声称在渲染质量、训练内存、FPS 和表面重建误差上均有改进；对关注高效神经场景表示、3D 重建与渲染的读者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis and 3D reconstruction have advanced rapidly with radiance fields and splatting, yet their memory and computational demands limit their use in resource-constrained settings. We introduce Hexels: novel planar hexagonal surface elements with a first-order spatial color field for efficient 3D scene and 2D image representation. Hexels exploit locally planar regions with smoothly varying appearance using fewer, larger primitives. Their hexagonal support provides an area- and boundary-efficient domain, while the local color field captures appearance variation within each primitive. Across 34 scenes, Hexels improve PSNR over memory-matched 2DGS by 4.53-7.38 dB across datasets while requiring lower training VRAM. We further ablate Hexels by showing that per primitive, Hexels outperform 2DGS by upto 4.74 dB while using lower training VRAM and having 2.31 times faster FPS. Even in unconstrained settings, Hexels offers complementary quality-memory trade-offs. For efficient 3D surface reconstruction, Hexels reduce error by 28.9% compared with memory-matched 2DGS across 15 DTU scans. On 6 Tanks and Temples surface scenes, Hexels achieves the highest mean F1 among compared methods (34.38%, versus 31.72% for 2DGS). We further also show that Hexels, as a general primitive, improves 2D image representation over Image-GS. Hexels push the Pareto frontier on the quality-efficiency trade-off of surface-aligned primitives.

</details>

#### 2026-10-27 - GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling

**Authors:** Kang He, Wenshuo Peng, Chuanhao Li, Zihui Gao, Xiaojie Xu, Zhengyuan Lin, Yuzhe Ding, Donghong Ji, Kaipeng Zhang, Yongtao Ge
**Links:** [abs](https://arxiv.org/abs/2610.37257) - [pdf](https://arxiv.org/pdf/2610.37257)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** camera pose estimation, pose estimation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling
- 作者：Kang He, Wenshuo Peng, Chuanhao Li, Zihui Gao, Xiaojie Xu, Zhengyuan Lin, Yuzhe Ding, Donghong Ji, Kaipeng Zhang, Yongtao Ge
- 出版日期：2026-10-27T13:53:14Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.37257) / [PDF](https://arxiv.org/pdf/2610.37257)

### 一句话总结
论文提出分钟级游戏玩法视频数据集 GameVerse，用于缓解长时程交互式世界建模中长时程训练数据稀缺的问题。

### 研究问题
当前交互式世界模型在约一分钟 rollout 之后难以保持连贯性；作者认为该限制的根源在于长时程训练数据稀缺，而非模型容量不足。现有游戏视频数据集通常由不足十秒的片段构成，且字幕以粗粒度、未区分整体的文本描述整个片段，不足以支撑可控的长时程生成。

### 核心思路/方法
构建面向长时程交互式世界建模的分钟级游戏玩法视频数据集 GameVerse，并采用统一处理流程：场景一致性分割、质量过滤、相机位姿估计、基于事件的字幕标注。每个片段配有在数分钟内保持时间稳定的相机轨迹，以及将静态场景上下文与动态前景事件分离、并对齐事件边界而非固定时间窗口的字幕。

### 主要贡献
- 提出 GameVerse 数据集：包含 69.7K 片段，覆盖 1,655 小时、3.496 亿帧，涵盖多种第一人称与第三人称游戏玩法。
- 包含 1,358 小时的连续两分钟序列，规模比先前数据集长一个数量级。
- 设计统一数据处理流程，包括场景一致性分割、质量过滤、相机位姿估计与事件字幕标注。
- 每个片段配有时间稳定的相机轨迹，以及区分静态场景上下文与动态前景事件、对齐事件边界的字幕。
- 摘要称综合分析显示 GameVerse 在规模、多样性和标注质量上超过现有公开数据集；实验表明在其上训练可显著延长交互式世界模型的时间跨度。

### 局限性
- 摘要未提供足够信息说明具体的实验设置、对比基线、评价指标及定量结果。
- 摘要未提供足够信息说明数据集在游戏类型、视觉风格或平台上的具体覆盖范围与潜在偏差。
- 摘要未提供足够信息说明标注流程的人工参与程度、标注一致性评估或质量控制细节。
- 摘要未提供足够信息说明相机位姿估计与场景一致性分割的具体方法及其误差影响。
- 摘要未提供足够信息说明数据集的许可、伦理审查或使用限制。

### 阅读优先级
中。理由：该论文聚焦长时程交互式世界建模的数据瓶颈，数据集规模与序列长度在摘要中有明确量化描述，并与 3D 重建、多视角几何及具身/机器人/AR 应用相关；但若关注具体模型训练效果、评测协议或数据构建细节，需进一步阅读全文，摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Recent advances in interactive world models have made it possible to generate controllable, dynamic environments from action inputs. Yet current models struggle to maintain coherence beyond roughly one minute of rollout, a limitation rooted not in model capacity but in the scarcity of long-horizon training data. Existing gameplay video datasets typically consist of clips under ten seconds, with captions that describe whole clips in coarse and undifferentiated text, which is insufficient for controllable long-horizon generation. We address this with GameVerse, a minute-scale gameplay video dataset purpose-built for long-horizon interactive world modeling. GameVerse contains 69.7K clips spanning 1,655 hours and 349.6 million frames across diverse first- and third-person gameplay, including 1,358 hours of continuous two-minute sequences, an order of magnitude longer than prior datasets. Clips pass through a unified pipeline of scene-consistent segmentation, quality filtering, camera pose estimation, and event-based caption annotation. Each clip is paired with a temporally stable camera trajectory that remains coherent across minutes, together with captions that separate static scene context from dynamic foreground events and align to event boundaries rather than fixed time windows. Comprehensive analysis shows that GameVerse surpasses existing public datasets in scale, diversity, and annotation quality. Experiments further demonstrate that training on GameVerse substantially extends the temporal horizon of interactive world models.

</details>

#### 2026-10-27 - RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty

**Authors:** Xinyi Chen, Yichen Zhang, Chenxing Jiang, Shaojie Shen
**Links:** [abs](https://arxiv.org/abs/2610.37111) - [pdf](https://arxiv.org/pdf/2610.37111)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty
- 作者：Xinyi Chen, Yichen Zhang, Chenxing Jiang, Shaojie Shen
- 出版日期：2026-10-27T12:08:37Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.37111 ；PDF https://arxiv.org/pdf/2610.37111

### 一句话总结
RAVEN 是一个面向四旋翼飞行器的统一主动 SLAM 框架，在定位不确定性下联合权衡探索未知区域与主动回环，并通过感知感知导航生成平滑执行轨迹。

### 研究问题
论文关注主动 SLAM 中的核心矛盾：一方面需要探索未知空间以扩大覆盖，另一方面需要利用已访问区域执行主动回环以维持定位精度。摘要指出，已有工作多面向地面机器人；空中机器人机动性强但传感器配置受限，面临更显著的定位漂移，因此需要专门的主动 SLAM 规划。此外，如何形成一种能根据任务特定优先级自适应调整性能的统一策略，仍是开放问题。

### 核心思路/方法
摘要给出的方法流程包括：
1. 识别前沿（frontiers）与主动回环候选；
2. 基于这些候选生成全局巡回候选（global tour candidates）；
3. 使用一个“效用向量”分别量化探索效率与定位精度，并依据取值在 [0,1] 的优先级参数选择最终巡回；
4. 由感知感知导航规划器基于在线 Fisher 信息场生成平滑执行轨迹，以最小化视觉状态估计误差。

整体上，RAVEN 将“探索—回环”的权衡显式参数化，并把定位不确定性纳入规划与轨迹生成过程。

### 主要贡献
摘要明确提到的贡献包括：
- 提出面向四旋翼的统一主动 SLAM 框架 RAVEN，系统性地考虑定位不确定性；
- 通过效用向量分别量化探索效率与定位精度，并支持由优先级参数调节最终巡回选择；
- 使用在线 Fisher 信息场进行感知感知导航规划，生成平滑执行轨迹以降低视觉状态估计误差；
- 基准评估显示其优于现有主动 SLAM 方法，并能在不同优先级下产生一系列性能表现；
- 使用定制立体惯性四旋翼完成全机载现场实验，验证在挑战性环境中的实际适用性；
- 摘要称将开源源代码。

### 局限性
摘要未提供足够信息说明以下方面：具体实验环境与规模、基准测试的完整设置与对比指标细节、失败案例或边界条件、计算资源与实时性开销、优先级参数选择的敏感性分析，以及现场实验的定量结果。因此无法基于摘要对这些局限作出可靠判断。

### 阅读优先级
中。理由：该工作面向空中机器人主动 SLAM，明确处理定位不确定性与探索—回环权衡，并声称有基准比较与全机载现场实验；若关注空中机器人自主探索、主动 SLAM 或感知感知规划，具有较高相关性。但摘要未提供实验细节与定量结果，需阅读全文后才能判断其方法新颖性与验证充分性。

</details>

<details>
<summary>Abstract</summary>

Active simultaneous localization and mapping (SLAM) addresses the problem of planning robot motion to build complete and accurate maps of unknown environments through efficient exploration while maintaining high localization accuracy. This raises a dilemma between exploring unknown spaces to expand coverage and exploiting visited regions to perform active loop closures. Despite numerous prior works on ground robots, aerial robots with high agility and constrained sensor suites face more significant localization drift and thereby demand dedicated active SLAM planning. Moreover, a unified strategy that adapts performance based on task-specific priorities remains an open question. In this article, we introduce RAVEN, a unified active SLAM framework for Rapid Autonomous Visual ExploratioN using quadrotors, which systematically accounts for localization uncertainty. The framework starts with identifying frontiers and active loop closure candidates, from which global tour candidates are generated. These candidates are evaluated using a utility vector that separately quantifies exploration efficiency and localization accuracy, and the final tour is selected according to a prioritization parameter ranging from $[0,1]$. Finally, a perception-aware navigation planner generates smooth execution trajectories that minimize visual state estimation error based on the online Fisher information field that provides visual localization information in real-time. Benchmark evaluations demonstrate that RAVEN outperforms state-of-the-art active SLAM methods, highlighting its advantages in producing a spectrum of performance across prioritizations. Fully onboard field experiments with a customized stereo-inertial quadrotor further validate its practical applicability in challenging environments. The source code will be released to benefit the community.

</details>

#### 2026-10-27 - Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction

**Authors:** Haoyu Yao, Chenguo Lin, Ruize Du, Yadong Mu
**Links:** [abs](https://arxiv.org/abs/2610.37046) - [pdf](https://arxiv.org/pdf/2610.37046)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction
- 作者：Haoyu Yao, Chenguo Lin, Ruize Du, Yadong Mu
- 出版日期：2026-10-27T11:15:41Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.37046) / [PDF](https://arxiv.org/pdf/2610.37046)

### 一句话总结
SceneEvolve 将 3D 场景表示为可执行代码，通过围绕小型开源智能体演化“harness”（执行框架/脚手架），在固定模型参数、动作语义与执行后端的前提下，提升从真实图像重建可编辑、组合式 3D 场景的能力。

### 研究问题
论文关注从单张真实图像重建可编辑、组合式 3D 场景的问题。该任务需要同时推理几何、物体结构与空间关系。摘要指出，现有设定下需要探索如何利用较小开源模型完成此类重建，并在不更新参数的情况下获得可复用的重建流程。

### 核心思路/方法
SceneEvolve 的核心是将 3D 场景表示为可执行代码，并围绕小型开源智能体演化 harness。方法包含两个组成部分：
- SceneAct：组合式语义动作接口，基于参数化基元、分层组合与语义空间关系构建。
- SceneHarness-RSI：利用更强的教师智能体，基于开发集重建反馈迭代演化 harness。

在整个 harness 演化过程中，模型参数、动作语义和执行后端保持不变。演化得到的 harness 形成可复用的重建过程，使小型开源模型无需参数更新或教师辅助即可重建未见场景。

### 主要贡献
- 提出 SceneEvolve 框架，将 3D 场景表示为可执行代码，并通过 harness 演化改进组合式 3D 重建。
- 提出 SceneAct 组合式语义动作接口，结合参数化基元、分层组合与语义空间关系。
- 提出 SceneHarness-RSI，利用教师智能体与开发集重建反馈迭代演化 harness，且保持模型参数、动作语义和执行后端固定。
- 摘要报告：在两个域内数据集和一个域外数据集上，使用较紧凑的 Qwen3.8-27B 模型时，四项重建指标均提升，平均推理时间相对基模型减少 47.0%。
- 摘要报告：尽管使用显著更小的模型，SceneEvolve 的重建质量比大型专有模型 GPT-5.6-Sol 高 32.3%，同时平均等效部署成本降低 59.8%。
- 摘要报告：使用 Qwen3.8-27B 演化得到的 harness 可泛化到 Kimi-K3，并取得与 GPT-6-Astra 可比的重建性能。

### 局限性
摘要未提供足够信息说明方法局限性、失败场景、对教师智能体或开发集质量的依赖程度，以及具体实验设置与指标定义。摘要未提供足够信息说明 harness 演化过程的计算开销、可复现性细节与跨更多模型/数据集的泛化边界。

### 阅读优先级
中。理由：论文主题属于组合式 3D 重建与智能体框架交叉方向，摘要给出了较明确的性能与效率对比，具有一定参考价值；但当前仅有摘要与元数据，缺少实验细节、局限讨论与方法实现信息，适合作为后续按兴趣深入阅读的候选。

</details>

<details>
<summary>Abstract</summary>

Reconstructing editable and compositional 3D scenes from a real image requires jointly reasoning about geometry, object structure, and spatial relationships. We introduce SceneEvolve, a framework that represents 3D scenes as executable code and improves reconstruction by evolving the harness around a small open-source agent. SceneEvolve combines SceneAct, a compositional semantic action interface built on parameterized primitives, hierarchical composition, and semantic spatial relations, with SceneHarness-RSI, which leverages a stronger teacher agent to iteratively evolve the harness using feedback from development-set reconstructions. Throughout harness evolution, the model parameters, action semantics, and execution backend remain fixed. The resulting harness provides a reusable reconstruction procedure that enables the small open-source model to reconstruct unseen scenes without parameter updates or teacher assistance. Across two in-domain datasets and one out-of-domain dataset, SceneEvolve with the comparatively compact Qwen3.8-27B model improves all four evaluated reconstruction metrics while reducing mean inference time by 47.0% relative to the base model. More notably, despite relying on a substantially smaller model, SceneEvolve achieves 32.3% higher reconstruction quality than the large proprietary GPT-5.6-Sol model, while reducing mean equivalent deployment cost by 59.8%. Furthermore, the harness evolved using Qwen3.8-27B also generalizes to Kimi-K3, achieving comparable reconstruction performance to GPT-6-Astra. The project page is https://haoyu-agent.github.io/SceneEvolve.

</details>

#### 2026-10-27 - LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM

**Authors:** Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel
**Links:** [abs](https://arxiv.org/abs/2610.36853) - [pdf](https://arxiv.org/pdf/2610.36853)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** camera prediction, SLAM, depth estimation, Gaussian Splatting, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM
- 作者：Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel
- 出版日期：2026-10-27T08:51:00Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.36853 ；PDF https://arxiv.org/pdf/2610.36853

### 一句话总结
LingGS 将前馈几何预测与相机跟踪解耦：由冻结的流式 3D 基础模型提供深度，再由显式几何求解器估计相机运动，并配合流式高斯建图，以提升单目 RGB 高斯泼溅 SLAM 在有限优化预算下的重建质量与跟踪效率。

### 研究问题
论文面向单目 RGB 高斯泼溅 SLAM，在有限优化预算下同时实现高质量重建与响应式相机跟踪仍然困难。摘要指出，该工作关注如何结合学习到的几何先验与显式几何相机跟踪，并比较其相对于学习式相机预测在跟踪精度上的表现。

### 核心思路/方法
- 使用冻结的流式 3D 基础模型作为虚拟 RGB-D 传感器，从单目视频提供深度估计。
- 使用显式几何求解器通过特征重投影估计相机运动。
- 使用流式高斯映射器将得到的观测整合为稠密场景表示。
- 摘要还指出，几何跟踪在代表性流式几何骨干上可提升相机位姿精度，说明方法具有更广的适用性。

### 主要贡献
- 提出一种在线系统，将学习到的几何先验与显式几何相机跟踪结合，用于单目 RGB 高斯泼溅 SLAM。
- 将前馈几何预测与相机跟踪解耦，并表明显式几何相机跟踪在跟踪精度上可显著优于学习式相机预测。
- 展示几何跟踪可跨代表性流式几何骨干提升相机位姿精度。
- 在室内和户外数据集上的大量实验表明，该方法相较现有方法显著提升重建质量；在单张 RTX 4090 上约达到 7 FPS，吞吐量为所评估的先前 SLAM 系统的 2–3 倍。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、对冻结 3D 基础模型深度质量的依赖程度、极端光照或快速运动下的表现、内存占用、长期漂移等细节。

### 阅读优先级
高。理由：论文直接针对单目 RGB 高斯泼溅 SLAM 中重建质量、跟踪精度与效率的权衡，提出解耦前馈几何预测与显式几何跟踪的在线方案，并报告了明确的精度、重建质量和吞吐量收益；对 3D 重建、多视图几何与神经场景表示相关方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Achieving high-quality reconstruction and responsive camera tracking remains challenging for monocular RGB Gaussian splatting SLAM under a limited optimization budget. We present an online system that addresses this challenge by combining learned geometric priors with explicit geometric camera tracking, which can substantially outperform learned camera prediction in terms of tracking accuracy. A frozen streaming 3D foundation model serves as a virtual RGB-D sensor, providing depth estimation from monocular video. An explicit geometric solver then estimates camera motion through feature reprojection, and a streaming Gaussian mapper integrates the resulting observations into a dense scene representation. We further show that geometric tracking improves camera pose accuracy across representative streaming geometry backbones, demonstrating the broader applicability of our approach. Extensive experiments on indoor and outdoor datasets show that our method significantly improves reconstruction quality over existing approaches, achieving about 7 FPS on a single RTX 4090 and delivering 2-3 times the throughput of the evaluated prior SLAM systems.

</details>

#### 2026-10-27 - Polarity--Time Interaction and Multi-Level Reliability for Event-Based Spacecraft Pose Estimation

**Authors:** Yonglong Zhang, Zongwu Xie, Yang Liu
**Links:** [abs](https://arxiv.org/abs/2610.36625) - [pdf](https://arxiv.org/pdf/2610.36625)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Polarity--Time Interaction and Multi-Level Reliability for Event-Based Spacecraft Pose Estimation
- 作者：Yonglong Zhang, Zongwu Xie, Yang Liu
- 出版日期：2026-10-27T04:29:19Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.36625) / [PDF](https://arxiv.org/pdf/2610.36625)

### 一句话总结
论文提出一种可靠性感知框架，将极性—时间定位、几何恢复、事件—CAD 细化与轨迹优化串联起来，用于基于事件的航天器位姿估计。

### 研究问题
稀疏事件响应会导致关键点误差不均匀，而这些误差对航天器位姿的影响取决于对应几何关系以及连续观测的可靠性。论文关注如何在这种条件下进行可靠的事件相机航天器位姿估计。

### 核心思路/方法
- 构建可靠性感知框架，连接极性—时间定位、几何恢复、事件—CAD 细化与轨迹优化。
- 采用三分支表示，结合正事件、负事件和近期事件时间信息，并通过跨分支注意力与门控，随后进行时空聚合。
- 使用有序语义点头估计相对对应精度，用于几何约束下的位姿恢复。
- 利用事件边缘与 CAD 投影一致性，在关键点几何保护机制下指导局部位姿细化。
- 在序列层面构造十维描述符，结合热图形状、重投影一致性和几何条件，设置时间对齐的观测尺度。

### 主要贡献
- 提出面向事件航天器位姿估计的多级可靠性框架。
- 在官方 SPADES 挑战测试集上，完整系统取得 0.0474 的组合位姿分数，摘要称约比 PASAN+IRIS 低 5.4%。
- 消融结果显示：基础定位配合均匀 PnP 的分数为 0.0772，完整级联降至 0.0514；在相同单帧观测下，质量加权将常数权重优化的 0.0549 降至 0.0514。
- 摘要强调质量加权在相同单帧观测下带来分数下降。

### 局限性
摘要未提供足够信息说明计算开销、实时性、不同事件噪声条件下的鲁棒性、数据集规模与训练细节，也未给出与 PASAN+IRIS 比较的完整实验设置和统计显著性。

### 阅读优先级
中。理由：论文针对事件相机航天器位姿估计中的稀疏关键点可靠性问题，给出较完整的级联框架和官方挑战集结果；但摘要未提供充分的实验细节与泛化验证信息，适合作为相关方向的方法参考而非立即精读优先。

</details>

<details>
<summary>Abstract</summary>

Sparse event responses produce uneven keypoint errors whose effects on spacecraft pose depend on correspondence geometry and the reliability of successive observations. We present a reliability-aware framework connecting polarity--time localization, geometric recovery, event--CAD refinement, and trajectory optimization. A three-branch representation combines positive events, negative events, and recent-event timing through cross-branch attention and gating, followed by spatiotemporal aggregation. An ordered semantic-point head estimates relative correspondence precision for geometrically constrained pose recovery. Event-edge and CAD-projection agreement then guide local pose refinement under keypoint-geometry safeguards. At the sequence level, a ten-dimensional descriptor combines heatmap shape, reprojection consistency, and geometric conditioning to set time-aligned observation scales. On the official SPADES challenge test set, the complete system achieves a combined pose score of 0.0474, approximately 5.4\% below PASAN+IRIS. Validation ablations reduce the score from 0.0772 for base localization with uniform PnP to 0.0514 for the complete cascade; on identical single-frame observations, quality weighting reduces the score from 0.0549 with constant-weight optimization to 0.0514.

</details>

#### 2026-10-27 - Camera-to-Quadruped Robot Pose Estimation from Sequential Images

**Authors:** Seobin Hwang, Ji-Seong Beom, Yeong-Jun Cho
**Links:** [abs](https://arxiv.org/abs/2610.36599) - [pdf](https://arxiv.org/pdf/2610.36599)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Camera-to-Quadruped Robot Pose Estimation from Sequential Images
- 作者：Seobin Hwang, Ji-Seong Beom, Yeong-Jun Cho
- 出版日期：2026-10-27T03:59:43Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.36599) / [PDF](https://arxiv.org/pdf/2610.36599)

### 一句话总结
该论文提出 QuadPose，从单目视频序列估计四足机器人全身 18 自由度姿态（6-DoF 基座位姿 + 12-DoF 关节角度），并发布首个相机到四足机器人姿态基准 QuadSyn。

### 研究问题
四足机器人常用于灾害响应、设施巡检等危险环境，需要外部相机监控以保障安全运行。但四足机器人是多关节系统，腿部关节随时间变化、腿部对称且自遮挡频繁，导致关键点对应关系不明确；同时缺少公开基准，难以进行定量比较。论文即针对上述姿态估计与评测基准缺失问题展开。

### 核心思路/方法
论文提出 QuadPose，从单目视频序列中估计四足机器人全身 18-DoF 姿态，包括 6-DoF 基座位姿和 12-DoF 关节角度。为支持定量比较，论文同时构建并引入 QuadSyn，这是首个相机到四足机器人姿态基准。摘要未提供 QuadPose 的具体网络结构、训练策略或损失函数等实现细节。

### 主要贡献
- 提出 QuadPose，用于从单目视频序列估计四足机器人全身 18-DoF 姿态（6-DoF 基座位姿 + 12-DoF 关节角度）。
- 引入 QuadSyn，定位为首个相机到四足机器人机器人姿态基准，用于缓解该任务缺少公开基准的问题。
- 在 QuadSyn 上报告了定量结果：PCK@2.5px 为 92.18%，PCK-AUC 为 95.54%，ADD@20cm 为 85.94%，ADD-AUC 为 66.98%，平均关节角度误差为 3.65 度，运行速度约 33 FPS。

### 局限性
- 摘要未提供足够信息说明 QuadPose 在真实场景、跨域数据或不同于 QuadSyn 的数据上的泛化表现。
- 摘要未提供足够信息说明 QuadSyn 的采集方式、规模、标注方式与数据多样性。
- 摘要未提供足够信息说明方法对严重自遮挡、腿部对称歧义等挑战的具体处理机制与消融结果。
- 摘要未提供足够信息说明与现有其他方法的定量对比细节。
- 摘要未提供足够信息说明 33 FPS 所对应的硬件平台与运行条件。

### 阅读优先级
中。理由：该工作同时提出方法与首个相关基准，并给出较完整的定量指标，对四足机器人外部监控与姿态估计方向具有参考价值；但摘要未展开方法细节与基准构建细节，是否优先精读取决于读者对四足机器人姿态估计或多关节目标姿态估计的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Quadruped robots are increasingly deployed in hazardous environments such as disaster response and facility inspection, where external-camera monitoring is essential for safe operation. This setting is challenging because quadrupeds are articulated systems with time-varying leg joints, leg symmetry, and frequent self-occlusions, which make keypoint correspondence ambiguous. Moreover, no public benchmark exists, making quantitative comparison difficult. To address these challenges, we propose QuadPose, which estimates the full-body 18-DoF pose (6-DoF base pose + 12-DoF joint angles) from monocular video sequences, and introduce QuadSyn, the first camera-to-quadruped robot pose benchmark. On QuadSyn, QuadPose achieves 92.18% PCK@2.5px, 95.54% PCK-AUC, 85.94% ADD@20cm, 66.98% ADD-AUC, and 3.65 degree mean joint-angle error at approximately 33 FPS.

</details>

## Neural Scene Representations & Rendering

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

#### 2026-10-27 - GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction

**Authors:** Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang, Yen-Liang Lin, David Held, Matthias Zwicker, Tom Goldstein
**Links:** [abs](https://arxiv.org/abs/2610.37818) - [pdf](https://arxiv.org/pdf/2610.37818)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction
- 作者：Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang, Yen-Liang Lin, David Held, Matthias Zwicker, Tom Goldstein
- 出版日期：2026-10-27T18:32:45Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.37818) / [PDF](https://arxiv.org/pdf/2610.37818)

### 一句话总结
GOFish 是首个直接在鱼眼图像上训练、可栅格化超过 180° 视场并从同一场景提取对齐网格的 3D Gaussian Splatting 表面重建方法，面向无需 LiDAR 的仿真就绪数字孪生。

### 研究问题
机器人和自动驾驶车辆以及消费级 360° 相机用鱼眼镜头获得大视场，仿真就绪的数字孪生要求全视场下的照片级渲染与对齐的碰撞网格。但已有鱼眼 Gaussian Splatting 方法最多只栅格化至 180° 且不生成网格，而 Gaussian 表面重建方法假设针孔训练图像，因此现有方法无法同时满足全视场渲染与网格提取的需求。

### 核心思路/方法
论文提出 GOFish，直接以鱼眼图像训练 3D Gaussian Splatting 表面重建，栅格化超过 180° 的视场，并从同一场景提取对齐网格。方法包含三项关键组件：Calibrated Densification 用于在整个视场内恢复表面；Calibrated Mip Filtering 与 Wide-Angle Appearance Modeling 用于避免像素模糊和镜头衰减进入场景与网格。

### 主要贡献
- 提出首个直接在鱼眼图像上训练、可栅格化超过 180° 视场并提取对齐网格的 3D Gaussian Splatting 表面重建方法。
- 通过 Calibrated Densification 在整个视场恢复表面，并用 Calibrated Mip Filtering 和 Wide-Angle Appearance Modeling 抑制像素模糊与镜头衰减对场景和网格的影响。
- 在 200° FIORD 与 205° FullCircle 基准上，PSNR 分别较最佳先前方法提升 2.28 dB 和 1.97 dB；在其自身视场内优于鱼眼渲染基线；在 FIORD 和 ScanNet++ 主集上取得最高网格 F-score。
- 高斯场景与网格共同构成无需 LiDAR、仿真就绪的数字孪生，可实时渲染、对全视场进行光线追踪并提供碰撞几何。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算开销、对标定误差的敏感性，以及对不同鱼眼相机或场景类型的泛化限制；也未提供各组件消融的详细结果。

### 阅读优先级
高。理由：该工作直接针对鱼眼全视场渲染与网格提取的统一问题，声称在多个基准上取得定量提升，并面向机器人、自动驾驶与 AR 等仿真就绪数字孪生应用，问题定义清晰且贡献点明确；但具体实验细节与局限性需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Robots, autonomous vehicles, and consumer 360° cameras use fisheye lenses for wide fields of view (FoVs). Simulation-ready digital twins require photorealistic rendering across the full FoV and an aligned collision mesh. However, prior fisheye Gaussian Splatting methods only rasterize up to 180° and do not produce meshes, while Gaussian surface reconstruction methods assume pinhole training images. We present GOFish, the first 3D Gaussian Splatting surface reconstruction method to train directly on fisheye images, rasterize FoVs beyond 180°, and extract an aligned mesh from the same scene. Calibrated densification recovers the surface across the entire FoV, while Calibrated Mip Filtering and Wide-Angle Appearance Modeling keep pixel blur and lens falloff out of the scene and mesh. Across the 200° FIORD and 205° FullCircle benchmarks, GOFish improves PSNR over the best prior method by 2.28 and 1.97 dB, respectively. It also outperforms fisheye rendering baselines within their own FoVs and achieves the highest mesh F-score on FIORD and the main ScanNet++ set. Together, the Gaussian scene and mesh form a LiDAR-free, simulation-ready digital twin that renders in real time, ray traces the full FoV, and provides collision geometry.

</details>

#### 2026-10-27 - GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis

**Authors:** Akshay Krishnan, Matias Turkulainen, Jamie Wynn, Zawar Qureshi, Mohamed Sayed, Guillermo Garcia-Hernando, Sara Vicente, James Hays, Michael Firman, Daniyar Turmukhambetov
**Links:** [abs](https://arxiv.org/abs/2610.37545) - [pdf](https://arxiv.org/pdf/2610.37545)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis
- 作者：Akshay Krishnan, Matias Turkulainen, Jamie Wynn, Zawar Qureshi, Mohamed Sayed, Guillermo Garcia-Hernando, Sara Vicente, James Hays, Michael Firman, Daniyar Turmukhambetov
- 出版日期：2026-10-27T16:56:45Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要 https://arxiv.org/abs/2610.37545 ；PDF https://arxiv.org/pdf/2610.37545

### 一句话总结
提出一种以卫星图像作为额外条件的多视图扩散模型，用于户外稀疏街景的新视角合成，以缓解外推时空间布局幻觉，且无需三维重建。

### 研究问题
多视图或视频扩散模型在稀疏图像集合的新视角合成中效果突出，但在输入视角之外（场景外推）合成时容易产生不真实的空间布局幻觉。论文聚焦户外场景，试图利用卫星图像提供额外场景布局信息来约束生成。

### 核心思路/方法
将卫星图像与街景输入图像共同作为条件，构建卫星条件化的多视图扩散模型；采用基于交叉注意力的条件注入方式，以保留预训练多视图扩散先验，在生成新视角时同时贴合卫星图像所见的场景布局；方法不依赖三维场景重建，仅使用带位姿的街景与卫星视图。

### 主要贡献
- 面向户外外推场景，提出使用卫星图像作为多视图生成模型的额外条件来源。
- 提出卫星条件化多视图扩散模型，结合卫星图像与街景输入图像进行新视角生成。
- 通过交叉注意力条件注入保留预训练多视图扩散先验，生成无缝、真实的新视角并遵循卫星图像中的场景布局。
- 方法不进行三维场景重建，仅依赖带位姿的街景和卫星视图。
- 摘要称在户外数据集实验中优于卫星条件化或街景条件化的基线，尤其在目标视角与源视角重叠很少的困难情形下。

### 局限性
摘要未提供足够信息。摘要未给出计算开销、对卫星图像时效性或对齐质量的敏感性、失败案例、定量指标细节及数据集规模等限制性信息。

### 阅读优先级
中。理由：选题针对稀疏街景外推中的布局幻觉，且用卫星图像做条件、无需三维重建，具有明确的问题意识与应用潜力；但当前仅有摘要信息，缺少定量结果、实验设置与局限性细节，需阅读全文后再判断其方法稳健性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Multi-view or video diffusion models have recently emerged as state-of-the-art approaches for novel-view synthesis from sparse image collections. While they can produce high quality images, they tend to hallucinate unrealistic spatial layouts when synthesizing views outside the input views (scene extrapolation). We propose to address this challenge for outdoor scenes by using satellite images as an additional information source to condition the multi-view generative model. We introduce a new satellite-conditioned multi-view diffusion model that combines conditioning from a satellite image and street-level input images when generating novel-views. Our cross-attention based conditioning allows us to retain pretrained multi-view diffusion priors to generate seamless, realistic, novel views from a handful of source views, while also adhering to the scene layout as seen from satellite images. Our model does not use 3D scene reconstruction, and only relies on posed street and satellite views. Our experiments on outdoor datasets show that our model is better than both satellite-conditioned or street-view conditioned baselines on novel-view synthesis, especially on challenging cases where target views have very little overlap with source views. Project page: https://nianticspatial.github.io/groundcontrol

</details>

#### 2026-10-27 - CTBakeGS: training-free baking of photorealistic CT volume renderings into 3D Gaussian splats

**Authors:** Haruki Fukuda, Constantin Lux, Wolf Schweitzer, Tadashi Hosoya, Lars Ebert
**Links:** [abs](https://arxiv.org/abs/2610.37406) - [pdf](https://arxiv.org/pdf/2610.37406)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CTBakeGS: training-free baking of photorealistic CT volume renderings into 3D Gaussian splats
- 作者：Haruki Fukuda, Constantin Lux, Wolf Schweitzer, Tadashi Hosoya, Lars Ebert
- 出版日期：2026-10-27T15:21:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37406) / [PDF](https://arxiv.org/pdf/2610.37406)

### 一句话总结
该论文提出一种无需训练的“烘焙”方法，将 CT 体渲染结果直接转换为 3D Gaussian splats 模型，从而在普通设备上实时展示照片级 CT 渲染。

### 研究问题
CT 体渲染能直观呈现解剖结构，但依赖 CT 数据、专用软件和强大 GPU。现有医学 3DGS 方法需要为每个场景训练数分钟到数小时。论文要解决的问题是：能否不经过训练，直接把 CT 体渲染转换为可实时显示的 3DGS 模型。

### 核心思路/方法
- 将 splats 放置在毫米级单元格的自适应八叉树上。
- 在 GPU 上利用渲染器的光照计算 splat 的颜色和不透明度。
- 将单元格不透明度解析地转换为 splat 不透明度。
- 对低于标准 3DGS 光栅器 1/255 不透明度下限的微弱 splat，采用随机方式保留。
- 在 6 个公开 CT 扫描（1.5-mm 体素）上，使用三种传递函数进行转换，并与收敛参考比较 PSNR、结构相似性和学习感知指标。

### 主要贡献
- 提出无需训练的 CT 体渲染到 3DGS 的直接转换流程。
- 给出基于自适应八叉树、GPU 光照计算、解析不透明度转换和随机保留微弱 splat 的具体方法。
- 报告转换后的模型可在普通计算机上实时渲染：200 万 splat 模型在骨、对比增强血管、皮肤与骨三类设置下分别达到 PSNR 32.6 ± 0.9 dB、30.1 ± 1.0 dB、32.3 ± 1.5 dB。
- 报告转换效率：一次转换通常在笔记本电脑上耗时 4–30 秒，在配备 4-GB 显卡的台式机上耗时 9–60 秒；笔记本电脑上 800 × 800 像素渲染达到 68 fps。

### 局限性
- 摘要仅报告 6 个公开 CT 扫描、1.5-mm 体素和三种传递函数，未说明更大规模或更多样化数据的泛化表现。
- 摘要称保真度“足以用于交互式查看”，但未提供临床诊断或定量医学任务上的验证。
- 摘要未提供与训练型医学 3DGS 方法在同等条件下的系统对比细节。
- 摘要未说明方法对低不透明度 splat 随机保留可能带来的时域稳定性或感知一致性问题。
- 摘要未提供代码、数据或复现细节。

### 阅读优先级
中。理由：该方法针对医学 CT 体渲染的实时可视化，提出无需训练的 3DGS 转换流程，问题明确且报告了转换速度与渲染帧率；但摘要显示评估范围有限，主要面向交互式查看，若关注临床验证、泛化性或与训练型方法的系统比较，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Photorealistic volume rendering of computed tomography (CT) may convey anatomy intuitively, but it needs the CT data, dedicated software and a powerful graphics processor. Three-dimensional Gaussian splatting (3DGS) displays photorealistic scenes in real time on less powerful devices, but existing medical approaches train each scene for minutes to hours. We aimed to convert a CT volume rendering directly into a 3DGS model without training. Splats were placed on an adaptive octree of millimetre-sized cells. Their colour and opacity were computed on the graphics processor with the renderer's lighting, cell opacity was converted analytically into splat opacity, and faint splats were retained stochastically above the 1/255 opacity floor of standard 3DGS rasterisers. Six public CT scans (1.5-mm voxels) were converted with three transfer functions and compared with converged references by peak signal-to-noise ratio (PSNR), structural similarity and a learned perceptual metric. Two-million-splat models reached a PSNR of 32.6 +/- 0.9 dB for bone, 30.1 +/- 1.0 dB for contrast-enhanced vessels and 32.3 +/- 1.5 dB for skin and bone. A conversion pass (usually two or three per model) took 4-30 s on a current laptop and 9-60 s on a desktop with a 4-GB graphics card. On the laptop, the models rendered at 68 frames per second at 800 x 800 pixels. Training-free conversion produced real-time 3DGS models of photorealistic CT renderings in about a minute or less per conversion pass on ordinary computers, with fidelity that we consider sufficient for interactive viewing.

</details>

#### 2026-10-27 - DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality

**Authors:** Anastasiya Pechko, Agata Szymańska, Piotr Borycki, Joanna Szelewska, Michał Mnich, Sławomir Tadeja, Przemysław Spurek
**Links:** [abs](https://arxiv.org/abs/2610.37172) - [pdf](https://arxiv.org/pdf/2610.37172)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality
- 作者：Anastasiya Pechko, Agata Szymańska, Piotr Borycki, Joanna Szelewska, Michał Mnich, Sławomir Tadeja, Przemysław Spurek
- 出版日期：2026-10-27T12:58:16Z
- 分类：Neural Scene Representations & Rendering；次要分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.37172)｜[PDF](https://arxiv.org/pdf/2610.37172)

### 一句话总结
论文提出 DomeGS，将传统 VR 中的“天空穹顶”概念融入 3D Gaussian Splatting 重建场景本身，以补全无界户外场景中不完整的地平线背景，并通过用户实验表明其在空间临场感与真实感上优于天空盒基线。

### 研究问题
摘要指出，VR 对高质量 3D 内容需求旺盛，3DGS 是有前景的高保真场景生成方法；但用 3DGS 重建无界户外场景时，由于数据缺失或缺少远景几何约束，地平线可能不完整，破坏 VR 的沉浸感。传统 VR 常用纹理立方体（skybox）或球体（skydome）营造远景背景，但这些方法与重建的 3DGS 几何难以无缝融合。论文即针对这一背景补全与融合问题展开。

### 核心思路/方法
DomeGS 框架的核心是将 skydome 概念从“平坦的背景外壳”转变为“重建的 Gaussian Splatting 3D 场景的一部分”。通过把地平线与天空整合进 3DGS 表示，方法旨在提供一个统一、场景一致的环境，使前景与背景相衔接，从而提升真实感。摘要未提供足够信息说明具体的网络结构、训练策略、损失函数或数据采集细节。

### 主要贡献
- 提出 DomeGS 框架，将天空穹顶作为 3DGS 场景的组成部分而非独立背景壳，用于无界户外场景的背景补全。
- 通过将地平线与天空纳入 3DGS 表示，构建前景与背景统一、场景一致的环境，以增强 VR 真实感。
- 开展 N=36 的用户实验评估：相比 skybox 基线，DomeGS 显著提升空间临场感（p=0.042）与真实感（p=0.042）。

### 局限性
摘要未提供足够信息说明方法在计算开销、不同场景泛化性、几何一致性定量指标、用户实验设计细节及统计效力等方面的局限；也未提供失败案例或边界条件。

### 阅读优先级
中。理由：该工作聚焦 3DGS 在无界户外 VR 场景中的背景补全与感知一致性，问题明确且有人类用户实验支持（N=36，两项指标显著），对 3DGS/VR 内容生成方向有参考价值；但摘要未披露方法细节与更全面的定量评估，是否需要优先精读取决于读者对 3DGS 背景补全或 VR 感知评估的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

The growing need for high-quality 3D content remains among the most prevalent challenges in virtual reality (VR). Recently, novel view synthesis techniques have enabled rapid content creation, with 3D Gaussian Splatting (3DGS) emerging as one of the most promising methods for generating high-fidelity 3D scenes. However, using 3DGS to reconstruct unbounded outdoor scenes can leave horizons incomplete due to missing data or a lack of distant geometric constraints. Such incompleteness can break immersion, compromising VR's core characteristic. A typical workaround in traditional VR systems is a textured cube (skybox) or sphere (skydome) surrounding the environment to create the illusion of a distant background. However, these approaches struggle to blend seamlessly with the reconstructed 3DGS geometry. To address these issues, we introduce the DomeGS framework, which incorporates the skydome concept not as a flat background shell, but as a part of the reconstructed Gaussian Splatting 3D scene. By integrating the horizon and sky into the 3DGS representation, our method provides a unified, scene-consistent environment bridging foregrounds and backgrounds for greater realism. Experimental evaluation with N=36 users demonstrates that DomeGS significantly increases spatial presence (p=0.042) and realism (p=0.042) compared to the skybox baseline.

</details>

#### 2026-10-27 - GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing

**Authors:** Jinxin Ai, Matthias Niessner
**Links:** [abs](https://arxiv.org/abs/2610.37036) - [pdf](https://arxiv.org/pdf/2610.37036)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing
- 作者：Jinxin Ai, Matthias Niessner
- 出版日期：2026-10-27T11:11:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37036) / [PDF](https://arxiv.org/pdf/2610.37036)

### 一句话总结
GraftRay 提出一种统一方法，将网格对象以物理一致的方式插入由 2DGS/3DGS 表示的室内场景中，通过显式建模空间扩展光源并联用路径追踪，实现视角一致的着色、互反射与软阴影。

### 研究问题
将虚拟物体插入通过 2D 或 3D Gaussian Splatting 重建的场景，是内容创作、AR 和合成数据生成的关键能力。真实感插入要求物体被场景光照并反之在场景上投射物理合理的阴影。现有方法要么在图像空间协调外观而牺牲多视角一致性，要么用插入点处的环境贴图近似场景光照，无法表示窗户、灯具等主导室内照明的近场面光源。

### 核心思路/方法
- 面向由 2D 或 3D Gaussians 表示的室内场景，实现网格对象的物理一致插入。
- 利用扩散先验恢复场景材质与表面法线。
- 显式建模空间扩展发光体，并以闭式解求解其辐射亮度。
- 采用混合渲染器，对场景 Gaussians 与插入网格进行联合路径追踪，产生视角一致的着色、互反射与软阴影。

### 主要贡献
- 提出 GraftRay，一种将网格对象物理一致地插入 2D/3D Gaussian 室内场景的统一方法。
- 通过扩散先验恢复材质与法线，并显式建模空间扩展光源、闭式求解其辐射亮度，以弥补环境贴图无法表示近场面光源的不足。
- 混合渲染器联合路径追踪场景 Gaussians 与插入网格，生成视角一致着色、互反射和软阴影。
- 在 FIPT 上取得新的 state of the art，在渲染保真度与阴影准确性上优于 ComGS、EAG-PT 等近期基线，同时保持很有竞争力的渲染效率。

### 局限性
摘要未提供足够信息。摘要未给出方法的具体失败情形、适用场景边界、计算开销数值或对非室内场景的泛化表现等细节。

### 阅读优先级
中。理由：该工作针对 Gaussian Splatting 场景中物理一致插入这一明确且实用的问题，提出显式近场面光源建模与联合路径追踪的方案，并在 FIPT 上报告了优于 ComGS、EAG-PT 的结果；但摘要未提供实验规模、定量指标、效率数据和局限分析，是否值得深入阅读需结合全文的实验细节与自身对 Gaussian Splatting 编辑/渲染方向的兴趣判断。

</details>

<details>
<summary>Abstract</summary>

Inserting virtual objects into scenes reconstructed via 2D or 3D Gaussian Splatting (2DGS/3DGS) is a key capability for content creation, AR, and synthetic data generation. However, realistic insertion requires the object to be seamlessly lit by the scene and, conversely, to cast physically plausible shadows onto it. Existing approaches either harmonize appearance in image space, sacrificing multi-view consistency, or approximate scene illumination with an environment map at the insertion point, which cannot represent near-field area lights such as windows and lamps that dominate indoor lighting. To address this, we present GraftRay, a unified method for physically consistent insertion of mesh objects into indoor scenes represented by either 2D or 3D Gaussians. We recover scene materials and surface normals with diffusion-based priors, and explicitly model spatially-extended emitters, solving their radiance in closed form. A hybrid renderer then jointly path-traces the scene Gaussians and inserted meshes, producing view-consistent shading, interreflections, and soft shadows. On FIPT, GraftRay sets a new state of the art, outperforming recent baselines such as ComGS and EAG-PT in rendering fidelity and shadow accuracy, while maintaining highly competitive rendering efficiency.

</details>

#### 2026-10-27 - GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting

**Authors:** Jiale Wang, Chen Zhao, Haoyang Zhang, Yanhao Wu, Fei He, Yanhu Shan, Rui Wu, Wei Ke, Tong Zhang
**Links:** [abs](https://arxiv.org/abs/2610.36760) - [pdf](https://arxiv.org/pdf/2610.36760)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting
- 作者：Jiale Wang, Chen Zhao, Haoyang Zhang, Yanhao Wu, Fei He, Yanhu Shan, Rui Wu, Wei Ke, Tong Zhang
- 出版日期：2026-10-27T07:15:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2610.36760 ；PDF 链接 https://arxiv.org/pdf/2610.36760 ；项目页 https://comedy0913.github.io/projects/geogsplat

### 一句话总结
GeoGSplat 是一种几何先验驱动的非像素对齐前馈高斯泼溅模型，通过显式引入几何约束来缓解非像素对齐方法中高斯中心错位和大幅视角变化下的渲染伪影问题。

### 研究问题
论文关注前馈高斯泼溅中的两个问题：一是像素对齐预测会使高斯基元数量随图像分辨率和视角数量增长，带来冗余和计算成本上升；二是非像素对齐方法虽能预测固定数量的高斯，但在缺乏显式射线和深度约束时，高斯中心位置不准确，导致在大视角变化下出现渲染伪影。论文旨在保持非像素对齐框架低冗余优势的同时，提升几何准确性和新视角合成质量。

### 核心思路/方法
GeoGSplat 在非像素对齐框架中显式加入几何先验。方法包含双分支编码器：分别构建 Anchors 和 Triplane，用于捕获粗略 3D 结构和细粒度场景特征。随后使用分层解码器逐步解码密集 3D 点和高斯基元，从而同时支持 3D 重建和新视角合成。

### 主要贡献
- 提出 GeoGSplat，将几何先验显式融入非像素对齐前馈高斯泼溅框架。
- 设计双分支编码器，通过 Anchors 和 Triplane 分别建模粗略 3D 结构与细粒度场景特征。
- 采用分层解码器逐步解码密集 3D 点与高斯基元，用于重建和新视角合成。
- 摘要称其在 DTU 和 NRGBD 上的新视角合成与重建性能超过像素对齐和非像素对齐的先进高斯泼溅方法；并指出当目标视角远离输入相机时优势更明显，表现出对大幅视角变化更强的泛化能力。

### 局限性
摘要未提供足够信息说明计算开销、推理速度、内存占用、训练数据规模、对不同场景类型的泛化边界或失败案例。摘要未提供足够信息说明方法在动态场景、极端稀疏视角或更复杂真实场景中的表现。

### 阅读优先级
高。理由：论文针对前馈高斯泼溅中“非像素对齐但几何不准确”的关键矛盾提出明确方法，且摘要声明在 DTU 和 NRGBD 上同时优于像素对齐与非像素对齐方法，并强调大视角变化下的泛化优势；这些信息对关注神经场景表示、前馈重建与新视角合成的研究者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Feed-forward Gaussian Splatting enables efficient novel view synthesis, but pixel-aligned prediction makes the primitive count grow with image resolution and view count, leading to substantial redundancy and increased computational cost. Non-pixel-aligned methods address this limitation by predicting a fixed number of Gaussians. Without explicit ray and depth constraints, these methods yield misplaced Gaussian centers, causing rendering artifacts under large viewpoint changes. To address this issue, we introduce GeoGSplat, a geometry-grounded feed-forward model that explicitly incorporates geometric priors into the non-pixel-aligned framework. A dual-branch encoder constructs Anchors and Triplane to capture coarse 3D structure and fine-grained scene features, respectively. Subsequently, a hierarchical decoder progressively decodes dense 3D points and Gaussian primitives, enabling 3D reconstruction and novel view synthesis. GeoGSplat surpasses both state-of-the-art pixel-aligned and non-pixel-aligned Gaussian Splatting methods on DTU and NRGBD in terms of novel view synthesis and reconstruction. The advantage of our geometry-grounded paradigm further increases as target viewpoints move farther from the input cameras, demonstrating stronger generalization to large viewpoint changes. Project Page: https://comedy0913.github.io/projects/geogsplat

</details>

#### 2026-10-27 - ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting

**Authors:** Jaesung Lee, Hyeontaek Hwang, Gabriel Manalu, Daeyoung Kim
**Links:** [abs](https://arxiv.org/abs/2610.36462) - [pdf](https://arxiv.org/pdf/2610.36462)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting
- 作者：Jaesung Lee, Hyeontaek Hwang, Gabriel Manalu, Daeyoung Kim
- 出版日期：2026-10-27T01:12:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.36462 ；PDF https://arxiv.org/pdf/2610.36462 ；项目页 https://jaesung8.github.io/clustersplat/

### 一句话总结
ClusterSplat 将 3D Gaussian Splatting 中的 3D 视觉定位从“对稠密基元相关性分数做启发式阈值/比例筛选”改为“在场景自适应簇候选上做簇级选择”，并让被选簇同时定义显式 3D 目标与渲染 2D 掩码。

### 研究问题
论文研究 3D Gaussian Splatting（3DGS）中的 3D 视觉定位：给定指代表达，需要同时输出渲染的 2D 掩码和一组显式 3D Gaussians 作为目标对象。摘要指出，现有方法通常对稠密基元级相关性分数施加启发式阈值或 top-ratio 过滤来提取 3D 目标；但这些分数在不同场景和提示之间常显著变化，使启发式筛选敏感且导致定位不稳定。

### 核心思路/方法
- 将 3D 目标选择重新表述为：在场景自适应候选上进行簇级选择，而非依赖基元级分数阈值。
- 学习实例感知的 Gaussian 特征。
- 形成特征感知的种子体素。
- 当描述长度准则下降时，合并相邻种子体素，从而生成场景特定的簇候选集合。
- 给定指代表达，使用轻量 MLP 作为查询条件化的簇评分器，对簇候选排序。
- 被选中的簇直接定义显式 3D 目标；其簇分数用于渲染 2D 掩码。
- 摘要报告的评测包括 ScanRefer、Ref-LERF 和 ScanNet v2 类名查询；具体实验设置、训练细节和消融结果摘要未提供足够信息。

### 主要贡献
- 提出 ClusterSplat，将 3DGS 中的 3D 视觉定位目标选择从基元级启发式筛选转为簇级选择。
- 设计场景自适应簇候选构建流程：实例感知 Gaussian 特征、特征感知种子体素、基于描述长度准则的相邻种子体素合并。
- 使用查询条件化的轻量 MLP 簇评分器排序候选，并统一支持显式 3D 目标与 2D 掩码渲染。
- 摘要声称在 ScanRefer 上，相比所比较的 3DGS 基线，取得最佳渲染 2D 分割和显式 3D 目标指标；在 Ref-LERF 上取得最佳平均分数；在 ScanNet v2 类名查询上取得最强渲染 2D 结果和最高 3D 匹配准确率，同时保持有竞争力的 3D IoU。具体数值和对比基线列表摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明计算开销、推理延迟或簇候选构建的复杂度。
- 摘要未提供足够信息说明对描述长度准则的敏感性、超参数选择及失败案例分析。
- 摘要未提供足够信息说明训练数据规模、监督形式、模型泛化到未见场景或开放词汇设置的表现。
- 摘要未提供足够信息说明与更多非 3DGS 方法或更强基线的系统比较。
- 摘要未提供足够信息说明 2D 掩码与显式 3D 目标之间一致性误差的定量分析。

### 阅读优先级
高。理由：该论文直接针对 3DGS 中 3D 视觉定位的稳定性问题，提出明确的簇级选择范式，并在摘要中报告了 ScanRefer、Ref-LERF 和 ScanNet v2 类名查询上的多类指标优势；若关注 3DGS 场景理解、指代定位或 2D-3D 一致目标选择，该工作具有较强相关性。但摘要未给出实验细节和数值，需阅读全文核实贡献强度。

</details>

<details>
<summary>Abstract</summary>

We study 3D visual grounding in 3D Gaussian Splatting (3DGS), where a referring expression should identify a target object as both a rendered 2D mask and a set of explicit 3D Gaussians. Prior methods typically extract 3D targets by applying heuristic thresholding or top-ratio filtering to dense primitive-level relevance scores. However, these scores often vary substantially across scenes and prompts, making such heuristics sensitive and leading to unstable targeting. ClusterSplat addresses this by reframing 3D target selection as cluster-level selection over scene-adaptive candidates. The method first learns instance-aware Gaussian features, forms feature-aware seed voxels, and merges neighboring seed voxels when a description-length criterion decreases, producing a scene-specific set of cluster candidates. Given a referring expression, a query-conditioned cluster scorer ranks the cluster candidates with a lightweight MLP, and the selected cluster directly defines the explicit 3D target while its cluster score is rendered for the 2D mask. On ScanRefer, ClusterSplat achieves the best rendered 2D segmentation and explicit 3D target metrics among the compared 3DGS baselines. It also obtains the best average Ref-LERF scores, supporting the same trend under fine-grained referring descriptions. On ScanNet v2 class name queries, ClusterSplat achieves the strongest rendered 2D results and the highest 3D matching accuracy, while maintaining competitive 3D IoU. Our project page is available at https://jaesung8.github.io/clustersplat/ .

</details>

## Embodied / Robotics / AR Applications

### 2026-10

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

#### 2026-10-27 - Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation

**Authors:** Dequan Ou, Austin Lopez, Quentin Missinne, Christophe De Wagter, Guido C. H. E. de Croon
**Links:** [abs](https://arxiv.org/abs/2610.37543) - [pdf](https://arxiv.org/pdf/2610.37543)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** rendering, robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation
- 作者：Dequan Ou, Austin Lopez, Quentin Missinne, Christophe De Wagter, Guido C. H. E. de Croon
- 出版日期：2026-10-27T16:56:18Z
- 分类：Embodied / Robotics / AR Applications；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37543) / [PDF](https://arxiv.org/pdf/2610.37543)

### 一句话总结
论文提出一种无需图像渲染、直接从场景几何与自运动合成事件流的解析事件模拟器，用于加速事件相机自主机器人导航的强化学习训练，并验证了策略在仿真和真实小型无人机上的迁移与部署。

### 研究问题
现有事件相机仿真器通常先渲染照片级图像再转换为事件，导致大规模强化学习训练非常慢。论文关注的问题是：能否绕开视觉渲染，直接根据事件相机本质上测量的运动对比边缘来合成事件流，从而显著加速事件相机导航策略的端到端强化学习训练，并实现真实机器人部署。

### 核心思路/方法
论文提出解析事件模拟器，利用事件相机 fundamentally 测量“运动对比边缘”这一特性，直接从场景几何和自运动合成事件流，而不进行视觉渲染。该模拟器在单 GPU 上生成 64x64 事件观测仅需 17 微秒，摘要称其比最先进的渲染管线快 400 倍以上。基于该模拟器，论文进行目标导向避障的端到端强化学习训练，使训练在 30 分钟内收敛。策略还被量化为 1.2 MB 的 int8 网络，并部署在搭载 Prophesee GenX320 事件相机和 OpenMV N6 微控制器板的 56 克 Crazyflie 上。

### 主要贡献
- 提出一种无需渲染的解析事件模拟器，直接从场景几何与自运动合成事件流。
- 该模拟器生成 64x64 事件观测耗时 17 微秒，摘要称比最先进渲染管线快 400 倍以上。
- 使目标导向避障的端到端强化学习在 30 分钟内收敛，摘要称比在渲染事件上训练快三个数量级。
- 策略零样本迁移到基于物理的事件仿真（ray-traced Isaac Sim）。
- 在训练中未见的杂乱赛道中达到 83% 成功率（中等难度，可通行概率约 0.57），平均目标速度 2.4 m/s；在模拟纹理密集室内大厅中保持 70% 成功率。
- 将策略量化为 1.2 MB int8 网络，完全机载运行于 56 克 Crazyflie；无需微调、外部处理或定位，在三条难度递增的真实障碍赛道中平均成功率为 82%（5/5、5/6、4/6 次飞行）。

### 局限性
- 摘要未提供足够信息说明模拟器对复杂光照、运动模糊、噪声模型或非理想事件相机特性的覆盖程度。
- 摘要未提供足够信息说明真实实验的完整统计显著性、失败模式分析或更广泛环境下的泛化边界。
- 摘要未提供足够信息说明训练所用场景分布、奖励设计细节及与其他强化学习方法的系统对比。
- 摘要未提供足够信息说明机载计算功耗、延迟分布及长期运行稳定性。

### 阅读优先级
高。理由：论文直击事件相机仿真训练慢这一关键瓶颈，提出无需渲染的解析事件模拟器，并给出从训练加速、零样本仿真迁移到 56 克 Crazyflie 机载真实飞行的完整验证链条；对事件相机机器人导航与高效强化学习训练具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Event cameras offer low latency, high dynamic range, and milliwatt-level power consumption, making them ideal for agile robots such as tiny drones navigating through cluttered environments. However, existing simulators generally render photorealistic images before converting them into events, making large-scale reinforcement learning prohibitively slow. We propose an analytic event simulator that exploits what event cameras fundamentally measure - moving contrast edges - to synthesize event streams directly from scene geometry and ego-motion without visual rendering. Our simulator generates a 64x64 event observation in 17 microseconds on a single GPU - over 400x faster than a state-of-the-art rendering pipeline - enabling end-to-end reinforcement learning for goal-directed obstacle avoidance to converge in under 30 minutes - three orders of magnitude faster than training on rendered events. Policies transfer zero-shot to physically based event simulations (ray-traced Isaac Sim). Our policy reaches 83% success in cluttered courses unseen during training (mid-difficulty, traversability probability approx. 0.57), at 2.4 m/s average goal velocity, and retains 70% in a simulated texture-dense indoor hall. Furthermore, we quantized the policy to a 1.2 MB int8 network running fully onboard a 56-gram Crazyflie equipped with a Prophesee GenX320 event camera and an OpenMV N6 microcontroller board. Without any fine-tuning, external processing, or positioning, the policy achieves an average success rate of 82% (5/5, 5/6, 4/6 flights) across three real-world obstacle courses of increasing difficulty. Code: https://github.com/tudelft/rendering-free-event-nav

</details>

#### 2026-10-27 - GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation

**Authors:** Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu, Xiang Gao
**Links:** [abs](https://arxiv.org/abs/2610.37091) - [pdf](https://arxiv.org/pdf/2610.37091)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation
- 作者：Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu, Xiang Gao
- 出版日期：2026-10-27T11:55:31Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.37091)｜[PDF](https://arxiv.org/pdf/2610.37091)

### 一句话总结
GAWM 是一个参数少于 1 亿、无需机器人或视频预训练的紧凑多任务世界-动作模型，在冻结 DINOv3 编码器的潜空间中预测未来观测，并在多个基准和真机任务上取得与十亿参数级模型可比或更优的表现。

### 研究问题
现有世界-动作模型（WAMs）大多依赖十亿参数级的视觉-语言或视频生成骨干网络，导致训练成本高、推理延迟大。论文关注的问题是：能否用紧凑模型在潜空间中完成未来观测预测，从而降低训练与推理开销，同时保持多任务机器人操作性能。

### 核心思路/方法
- 在冻结的 DINOv3 编码器潜空间中预测未来观测，而非生成像素或依赖大型视频生成骨干。
- 将每个相机视角的特征压缩为少量 token。
- 使用轻量预测器，以任务为条件、而非以动作为条件，预测两个未来时间视野的 token。
- 预测以未来帧的稠密 patch 特征进行监督，促使模型编码未来场景的空间布局。
- 动作解码器直接从当前 token 与预测 token 回归未来动作块。

### 主要贡献
- 提出 GAWM，一个参数少于 100M、无需机器人或视频预训练的多任务世界-动作模型。
- 在 RoboTwin 2.0 上优于十亿参数级 WAMs，在 LIBERO 上与十亿参数级 VLAs 表现相当。
- 在双臂机器人上，于留出演示数据上取得比微调的十亿参数 VLA 更低的动作预测误差，且推理延迟显著更低。
- 消融研究表明，在训练数据或训练时间受限时，潜空间世界模型能显著提升性能。
- 代码已公开。

### 局限性
- 摘要未提供足够信息说明模型在更多任务类型、真实场景多样性或长期任务上的泛化边界。
- 摘要未提供足够信息说明失败案例、安全性或部署约束。
- 摘要未提供足够信息说明与基线在训练成本、显存占用和能耗方面的完整对比细节。
- 摘要未提供足够信息说明消融实验的具体设置与完整数值。

### 阅读优先级
高。理由：该论文直接针对世界-动作模型“大参数、高成本、高延迟”的核心痛点，提出紧凑替代方案，并在多个基准和真机任务上给出与十亿参数模型可比或更优的结果；同时涉及潜空间世界模型监督、任务条件预测和动作块回归等可复用设计，对机器人操作与高效具身策略学习具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

World-action models (WAMs) incorporate the prediction of future observations into robot policy learning. However, most WAMs build on billion-parameter vision-language or video-generation backbones, which incur high training cost and inference latency. In this letter, we present GAWM (Geometry-Aware World Model), a compact multi-task WAM that predicts future observations in the latent space of a frozen DINOv3 encoder. GAWM compresses the features of each camera view into a small set of tokens. A lightweight predictor, conditioned on the task rather than on actions, forecasts these tokens at two future horizons. The forecast is supervised with the dense patch features of future frames, which requires it to encode the spatial layout of the future scene. An action decoder directly regresses a chunk of future actions from the current and predicted tokens. With fewer than 100M parameters and no robot or video pretraining, GAWM outperforms billion-parameter WAMs on RoboTwin 2.0 and performs comparably to billion-parameter VLAs on LIBERO. On a dual-arm robot, it achieves lower action-prediction error on held-out demonstrations than a fine-tuned billion-parameter VLA, with substantially lower inference latency. Ablation studies show that the latent world model substantially improves performance when training data or training time is limited. Code is available at https://github.com/gaoxiang12/ga-wm.

</details>

#### 2026-10-27 - ActiveAlign: Aligning Egocentric Manipulation via Active Perception

**Authors:** Ri-Zhao Qiu, Bowen Wen, Yifeng Jiang, Chen Tessler, Eric Heiden, Xue Bin Peng, Xiaolong Wang, Stan Birchfield, Erwin Coumans
**Links:** [abs](https://arxiv.org/abs/2610.36859) - [pdf](https://arxiv.org/pdf/2610.36859)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** differentiable rendering, rendering, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ActiveAlign: Aligning Egocentric Manipulation via Active Perception
- 作者：Ri-Zhao Qiu, Bowen Wen, Yifeng Jiang, Chen Tessler, Eric Heiden, Xue Bin Peng, Xiaolong Wang, Stan Birchfield, Erwin Coumans
- 出版日期：2026-10-27T08:54:27Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.36859 ；PDF https://arxiv.org/pdf/2610.36859

### 一句话总结
提出 ActiveAlign 框架，用主动感知（挥手做手眼标定、触摸做物体对齐）缩小 Real2Sim2Real 中被动观测带来的 real2sim 差距，并在真实 Unitree G1 上展示毫米级精细操作。

### 研究问题
现有 Real-to-Sim-to-Real 方法多依赖被动感知，因观测不完美而产生 real2sim 差距。论文关注如何通过主动交互而非被动观测来对齐这一差距，尤其是机器人操作场景下的手眼标定与物体对齐问题。

### 核心思路/方法
受人类通过动作主动感知的启发，ActiveAlign 将主动感知用于 Real2Sim2Real 对齐，包含两个互补模块：
- ActiveAlign-Waving：利用主动手部运动与可微渲染进行手眼标定。
- ActiveAlign-Touching：通过触觉反馈细化物体对齐，达到毫米级精度。
二者结合用于实现较强的 real2sim 对齐；摘要还指出 ActiveAlign-Waving 可用于为开源未标定机器人操作数据集整理仿真环境。

### 主要贡献
- 提出 ActiveAlign 框架，以主动感知对齐 Real2Sim2Real 差距，区别于被动感知路线。
- 设计 ActiveAlign-Waving（主动手部运动 + 可微渲染做手眼标定）与 ActiveAlign-Touching（触觉反馈细化物体对齐，毫米级精度）两个互补模块。
- 展示 ActiveAlign-Waving 可用于为开源未标定机器人操作数据集构建/整理仿真环境。
- 在真实 Unitree G1 机器人上演示毫米级物体精细操作，如按按钮和移动滑块。

### 局限性
摘要未提供足够信息。具体实验规模、成功率、基线对比、触觉传感器配置、可微渲染细节、失败案例与泛化边界均未在摘要中说明。

### 阅读优先级
中。理由：论文聚焦 Real2Sim2Real 对齐与主动感知，方法模块清晰且给出真实机器人毫米级操作演示，对具身操作与仿真对齐方向有参考价值；但摘要未提供定量结果与对比细节，需阅读全文后才能判断其效果与适用范围。

</details>

<details>
<summary>Abstract</summary>

Real-to-Sim-to-Real (Real2Sim2Real) enables structured world representations for planning, interpretability, and safe execution. Most existing approaches rely on passive perception, which creates real2sim gaps due to imperfect observation. Inspired by how humans perceive actively through actions, we propose ActiveAlign, a framework that leverages active perception to align the Real2Sim2Real gap from interactions. ActiveAlign introduces two complementary modules: (i) ActiveAlign-Waving, which performs hand-eye calibration by exploiting active hand motions and differentiable rendering, and (ii) ActiveAlign-Touching, which refines object alignment through tactile feedback to achieve millimeter-level precision. Together, these capabilities enable strong real2sim alignment. We demonstrate that ActiveAlign-Waving can be used to curate simulation environments for open-sourced uncalibrated robot manipulation datasets, and demonstrate on a real Unitree G1 robot that ActiveAlign enables fine manipulation of millimeter-scale objects such as pressing buttons and moving sliders.

</details>

#### 2026-10-27 - OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation

**Authors:** Adithyavairavan Murali, Yash Oza, Karanbir Chahal, Neel Jawale, Silas De Vries, Hesam Rabeti, Erwin Coumans, Balakumar Sundaralingam, Stan Birchfield
**Links:** [abs](https://arxiv.org/abs/2610.36598) - [pdf](https://arxiv.org/pdf/2610.36598)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation
- 作者：Adithyavairavan Murali, Yash Oza, Karanbir Chahal, Neel Jawale, Silas De Vries, Hesam Rabeti, Erwin Coumans, Balakumar Sundaralingam, Stan Birchfield
- 出版日期：2026-10-27T03:58:54Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.36598) / [PDF](https://arxiv.org/pdf/2610.36598)

### 一句话总结
OpenJaws 是一个完全开源、以低成本立体相机改进 UMI 手持数据采集定位精度的软硬件框架，并配套提出定位精度基准。

### 研究问题
手持数据采集接口（如 UMI）可以在没有机器人参与的情况下在野外采集操作演示，但其动作标签质量受视觉定位精度限制。现有系统使用单目视觉惯性里程计恢复末端执行器位姿，存在尺度模糊和漂移问题；或依赖闭源模块和外部基础设施，重新引入成本与部署负担。

### 核心思路/方法
- 提出 OpenJaws：面向传感器化 UMI 的完全开源硬件与软件框架，旨在改进定位并简化跨机器人平台部署。
- 硬件上，将模块化 3D 打印夹爪（带标准化 ISO 适配器）与低成本立体相机配对，用于恢复度量尺度的相机轨迹。
- 提出 UMI-Loc-Bench-v1：用于量化手持数据采集设备真实世界定位精度的基准。
- 摘要称立体定位显著优于单目替代方案，并展示用 OpenJaws 采集数据训练的策略可在真实机器人上跨多个任务部署。

### 主要贡献
- 开源硬件与软件框架 OpenJaws，面向传感器化 UMI，采用立体相机进行度量定位。
- 模块化 3D 打印夹爪与标准化 ISO 适配器设计。
- 提出 UMI-Loc-Bench-v1 定位精度基准。
- 摘要报告立体定位显著优于单目方案。
- 展示基于 OpenJaws 数据训练的策略可在真实机器人多任务部署。
- 硬件、软件和数据以商业宽松许可证发布。

### 局限性
- 摘要未提供足够信息说明具体任务数量、机器人平台类型、策略类型及定量成功率。
- 摘要未提供足够信息说明立体定位与单目方案的具体精度数值、基准规模与评测设置。
- 摘要未提供足够信息说明硬件成本、计算需求、实时性及在不同环境下的鲁棒性。
- 摘要未提供足够信息说明与闭源或外部基础设施方案的直接对比细节。

### 阅读优先级
中。理由：该工作聚焦 UMI 数据采集中的定位精度与开源部署问题，并发布基准与开源资源，对具身操作数据采集方向有参考价值；但摘要未给出定量实验细节，需阅读全文才能判断实际精度提升幅度与部署效果。

</details>

<details>
<summary>Abstract</summary>

Handheld data-collection interfaces such as the Universal Manipulation Interface (UMI) allow manipulation demonstrations to be gathered in the wild without a robot in the loop, but the quality of the resulting action labels is bounded by the accuracy of vision-based localization. Existing systems recover end-effector pose from monocular visual-inertial odometry, which is subject to scale ambiguity and drift, or delegate tracking to closed-source modules and external infrastructure that reintroduce cost and setup burden. We present OpenJaws, a fully open hardware and software framework for sensorized UMI that improves localization and simplifies deployment across robot platforms. OpenJaws pairs a modular, 3D-printed gripper exposing a standardized ISO adapter with a low-cost stereo camera to recover metric camera trajectories. We further introduce UMI-Loc-Bench-v1, a benchmark quantifying real-world localization accuracy for handheld data-collection devices, and show that stereo localization substantially outperforms monocular alternatives. Finally, we demonstrate that policies trained on data collected with OpenJaws can be deployed on a real robot across multiple tasks. Hardware, software, and data are released under a commercially permissive license. Code, data, and videos are available at https://open-jaws.github.io/

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
