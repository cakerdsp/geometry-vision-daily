# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：74
- 分类分布：
  - Neural Scene Representations & Rendering: 27
  - 3D Reconstruction & Multi-view Geometry: 20
  - Embodied / Robotics / AR Applications: 16
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

## 今日滚动窗口科研趋势综合分析

> 说明：以下分析仅基于所提供的标题、分类与摘要信息。凡涉及实验规模、具体指标、消融细节的判断，均标注为“需全文验证”。

---

### 今日主要趋势

#### 趋势一：从“几何重建”走向“几何 + 语义/物理/声音”的多属性联合场景表示

本批次论文中，最清晰的方向变化是：三维/四维场景不再只追求视觉真实感，而是把**语义、实例、物理合理性、声音**等属性纳入同一表示或同一生成流程。

- **LucidLyra**（3D Reconstruction & Multi-view Geometry）：通过多任务蒸馏把开放词汇语义、类别无关实例线索与几何、外观一起编码进 3D Gaussian，并强调“前馈、无需逐场景优化、无需人工 3D 标注”。
- **SonoWorld4D**（Dynamic / 4D Reconstruction）：明确指出现有 4D 场景生成“声音基本未被建模”，提出 Video-to-4DAVScene 新任务，把 360° 背景、发声前景轨迹与多声源一致声场联合生成。
- **GenSight**（Embodied / Robotics）：把未来视频生成与深度、具身分割、2D 光流统一到同一个视频扩散 Transformer，强调“想象 + 感知”一体化。
- **COGS**（Neural Scene Representations & Rendering）：反过来做诊断——系统检验 3DGS 的异构属性（外观、不透明度、协方差相关）对对象级感知的实际贡献，指出“属性子集可优于完整属性集”。

这一趋势的共性是：**表示层正在从“渲染导向”转向“下游任务导向”**，语义与物理属性不再是后处理附加物，而是训练目标的一部分。

#### 趋势二：前馈化与“前馈 + 轻量自细化”成为 3DGS 的主流效率路线

多篇论文围绕前馈 3D Gaussian Splatting 的**精度—效率—紧凑性**三角展开，且不再单纯追求“更大模型”，而是引入轻量修正机制。

- **GradSplat**：指出前馈预测与逐场景优化的差距主要在高斯形状（尺度、旋转），提出在前向传播内部做学习到的梯度步骤自细化，并提出 log-anisotropy correction。
- **BudSplat**：面向“渲染预算”约束，用细节感知重要性分数与质量感知剪枝，在有限基元数下保留最有价值高斯。
- **ACD-GS**：针对训练期致密化的启发式问题，用二阶深度响应作为结构先验，对克隆与分裂做非对称调控，并结合多视角光度一致性与容量感知自适应策略。
- **GOFish**：把前馈/优化式 3DGS 推向鱼眼全视场（>180°）并同时提取对齐网格。

技术信号是：**“冗余基元”和“形状不准”被识别为前馈 3DGS 的两个核心瓶颈**，对应地出现“剪枝/预算约束”和“内部梯度细化”两条互补路线。

#### 趋势三：扩散模型从“生成器”转变为“先验源/同步器/统一预测空间”

扩散模型在本批次中的角色明显多样化，不再只是图像/视频生成器：

- **SonoWorld4D**：用“双空间音频扩散同步”合成多声源一致声场。
- **MLLM-GS**：用冻结 MLLM 的视觉先验增强退化视图，再用轻量校正网络抑制像素错位与颜色偏差，服务于极端环境 NVS。
- **Hierarchical Diffusion**：把视频生成重构为“变形 + 修复”（warping-and-inpainting），用分层长上下文去噪缓解自回归漂移。
- **Extremely Sparse-View CT**：从每训练样本仅一张 2D 投影学习姿态感知扩散先验，并在采样中注入测量保真、共享体积重投影与投影物理一致性。
- **GenSight**：在统一速度预测空间中联合优化视频、深度、分割、光流。

共性是：**扩散先验正被“结构化约束”包裹**——位姿、几何、物理一致性、长程上下文都作为采样或训练中的显式引导项出现。

#### 趋势四：评测与基准本身成为研究贡献，“对齐/诊断”问题被显式提出

本批次有多篇论文的核心贡献不是新模型，而是**评测方法或诊断基准**：

- **Aligning Misaligned Benchmarks for Single-View NVS**：指出测试时位姿优化本质病态，导致方法在任意局部最优处被评估；提出用传统 2D-2D / 2D-3D 匹配对齐重建，并仅在共视区域评测。
- **COGS**：构建 15,675 个对象、40 类的 3DGS 数据集与属性诊断基准，揭示属性使用的不均匀性。
- **KITScenes Aerial**：把航空建图、空中辅助在线 HD 建图、跨视角定位统一到同一数据基础，覆盖 53 个地图类别并兼容三类设置。
- **PhysInsert**：构建 Insert World 严格对齐反事实配对数据集与 PhysInsert-Bench，要求光照与位姿适配而非仅复制粘贴。

这说明领域正在从“刷指标”转向**质疑指标本身的有效性**，尤其集中在坐标对齐、属性归因、跨视角泛化等易被忽略的环节。

#### 趋势五：机器人/具身应用向“资源受限 + 真实部署 + 决策级安全”收敛

Embodied / Robotics 类论文呈现明显的工程落地导向：

- **SKiD-SLAM**：调研真实行星任务的通信与计算预算，据此选模块，并在韩国熔岩管洞穴与模拟地形完成实地部署。
- **DEED**：通过演示扩展（多指令、多相机、多光照）与执行设计（逆运动学、任务特定夹爪映射、闭环重规划）适配预训练 VLA 策略。
- **Decision-Level Error Attribution**：把单目 RGB 跟踪的误差拆分为“安全规则贡献”与“感知贡献”，并区分漏检与定位误差，用 Shapley 归因。
- **AFast Robot Localization**：仅用四个测距传感器、无需航向信息的蒙特卡洛粒子滤波定位。

信号是：**“在预算约束下能跑通、能被归因、能实地验证”正成为具身方向的重要评价维度**，而非单纯追求感知精度。

---

### 技术路线观察

#### 几何基础模型方向

- **PhysInsert** 是本批次中最明确的“几何基础模型 + 生成”结合：把 VGGT 几何流与图像流、文本流并列，在目标场景特征监督下做空间一致插入。其关键设计是**几何先验作为约束项而非替代项**，并配合 2D 物体—场景空间监督实现双向交互。
- **LucidLyra** 走的是“蒸馏”路线：从相机控制视频扩散模型与冻结 2D 视觉基础模型蒸馏互补知识，避免依赖多视角采集与逐场景优化。
- **RoSAMDepth** 则把 SAM 的对象级先验引入自监督深度，从特征对比、区域平滑、可靠性估计三方面注入对象级信息。

对比可见：几何基础模型的使用方式分化为**“作为输入流/约束”**（PhysInsert）与**“作为蒸馏教师”**（LucidLyra）两类；而 SAM 类分割基础模型更多被用作**对象级结构先验**而非直接预测器。

#### 3D/4D 重建方向

- **SonoWorld4D** 代表 4D 重建的“多模态扩展”：单目视频 → 360° 背景 + 显式运动轨迹 + 一致声场，且要求实时新视角视觉与空间音频渲染。
- **GenSight** 代表 4D 感知的“统一架构”路线：一个 DiT 骨干、统一时空表示、统一速度预测空间，支持生成与单步感知两种推理模式。
- **SKiD-SLAM** 与 **Efficacy of Monocular Depth in Lunar Environments** 代表“极端/分布外环境下的重建可靠性”：前者是分布式多机器人 LiDAR SLAM 的

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-30T13:59:26-04:00
**Total number of papers:** 74
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

#### 2026-10-26 - Does VGGT Know What It Does Not Know?

**Authors:** Adityan Thirumani Srinivasan, David Nordström
**Links:** [abs](https://arxiv.org/abs/2610.35806) - [pdf](https://arxiv.org/pdf/2610.35806)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, point map, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Does VGGT Know What It Does Not Know?
- 作者：Adityan Thirumani Srinivasan, David Nordström
- 出版日期：2026-10-26T17:37:39Z
- 分类：Geometry Foundation Models（主分类）；二级分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2610.35806) / [PDF](https://arxiv.org/pdf/2610.35806)

### 一句话总结
论文探究前馈式三维重建模型 VGGT 是否在其冻结特征中隐含对相机位姿预测失败的自知能力，并表明线性探针可对此进行高精度预测。

### 研究问题
VGGT 等前馈式三维重建模型在单次前向传播中回归相机与几何，但不报告相机位姿的不确定性，错误相对位姿与正确位姿在外观上无差别。论文追问：冻结的 VGGT 模型是否“知道”自己的位姿何时出错。

### 核心思路/方法
- 构建 HardMatch 基准，包含 1,000 对刻意困难的图像对，VGGT 在其中 35% 的图像对上失败。
- 在 VGGT 冻结特征上训练线性探针，用于预测位姿失败，并在留出类别上评估。
- 与 VGGT 自身的点图置信度、以及在 VGGT 全部输出上训练的分类器进行比较。
- 分析该知识在模型中的位置：比较逐图像编码器与融合双视角的层。
- 将探针不重新训练地迁移到 PhotoTourism 与 ScanNet-1500 的旋转失败检测，并与共视性解释进行比较。
- 在第二个模型 $π^3$ 上验证类似现象。

### 主要贡献
- 提出 HardMatch 基准，用于评估困难图像对上的位姿失败。
- 发现冻结 VGGT 特征上的线性探针预测位姿失败的 ROC-AUC 为 93.5%，高于 VGGT 自身点图置信度的 79.7% 和基于全部输出分类器的 77.7%。
- 表明探针能捕捉 VGGT 高置信却失败的案例，可支持下流系统对不信任的图像对弃权。
- 展示探针无需重新训练即可迁移到 PhotoTourism 和 ScanNet-1500 的旋转失败检测，且超出共视性所能解释的范围。
- 定位该知识不在逐图像编码器中，而是在融合双视角的层的中途计算得到；$π^3$ 也呈现相同情况。
- 总结为：VGGT 对自身失败的了解多于其报告的内容。

### 局限性
- 摘要未提供足够信息说明 HardMatch 的构建细节、数据来源与类别划分方式。
- 摘要未提供足够信息说明线性探针的具体结构、训练设置与统计显著性。
- 摘要未提供足够信息说明与共视性比较的具体方法和定量结果。
- 摘要未提供足够信息说明在 $π^3$ 上的实验规模与完整结果。
- 摘要未提供足够信息说明方法在更多模型、更多任务或真实部署场景中的泛化性。

### 阅读优先级
中。理由：论文聚焦前馈三维重建模型的失败自感知与不确定性报告问题，提出可解释性探针和可迁移的失败预测方法，对几何基础模型的可信部署有参考价值；但摘要未提供实验细节与完整局限性，需阅读全文才能判断其普适性。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models such as VGGT regress cameras and geometry in a single forward pass, but they report no uncertainty for the camera poses they predict: an incorrect relative pose looks no different from a correct one. We ask whether the frozen model nonetheless knows when its pose is wrong. On HardMatch, a benchmark of 1,000 deliberately difficult image pairs on which VGGT fails on 35% of pairs, a linear probe on VGGT's frozen features predicts pose failure on held-out categories with ROC-AUC 93.5%, compared with 79.7% for VGGT's own point-map confidence and 77.7% for a classifier trained on all of VGGT's outputs. The probe catches failures VGGT is confident about, lets a downstream system abstain on the pairs it distrusts, and transfers without retraining to rotation failures on PhotoTourism and ScanNet-1500, beyond what co-visibility explains. This knowledge is absent from the per-image encoder: it is computed partway through the layers that fuse the two views, and the same holds for a second model, $π^3$. In essence, we find that VGGT knows more about its own failures than it reports.

</details>

#### 2026-10-26 - E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling

**Authors:** X-Era AI Lab Team, :, Jianhao Lai, Zhihao Zhan, Zhiquan Liao, Qichang Li, Shubin Chen, Zhiyuan Liu, Hongsen Lei, Jianman Lin, Xiaoxin Lin, Ke Gong, Baiyue Gu, Shiming Chen, Junlin He, Longqi Yang, Junrong Xiao, Haolin Luo, Xiaojuan Su, Jianfeng Li, Yu Luo, Xu Sun, Likui Zhang, Jusheng Zhang, Qinhan Lyu, Tianshui Chen, Liang Lin, Guangrun Wang
**Links:** [abs](https://arxiv.org/abs/2610.36011) - [pdf](https://arxiv.org/pdf/2610.36011)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling
- 作者：X-Era AI Lab Team, Jianhao Lai, Zhihao Zhan, Zhiquan Liao, Qichang Li, Shubin Chen, Zhiyuan Liu, Hongsen Lei, Jianman Lin, Xiaoxin Lin, Ke Gong, Baiyue Gu, Shiming Chen, Junlin He, Longqi Yang, Junrong Xiao, Haolin Luo, Xiaojuan Su, Jianfeng Li, Yu Luo, Xu Sun, Likui Zhang, Jusheng Zhang, Qinhan Lyu, Tianshui Chen, Liang Lin, Guangrun Wang
- 出版日期：2026-10-26T17:00:09Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.36011 ；PDF https://arxiv.org/pdf/2610.36011

### 一句话总结
E0.5 提出一种以 3D 基础模型为主干、原生以 3D 几何为世界表示并显式预测未来 3D 状态与动作的世界-动作模型，在 RoboTwin 2.0 与真实机器人操作任务上验证了其效果。

### 研究问题
摘要指出，世界-动作模型（WAMs）对具身智能具有前景，但主流方法以视频基础模型或视觉-语言模型（VLM）为中心；即使引入 VGGT 等 3D 模型提取的几何特征，这些特征通常也只是作为辅助输入或预测目标送入视频模型或 VLM，3D 几何并未成为世界建模的原生基础。论文要解决的问题是：能否将 3D 基础模型本身作为世界-动作建模的主干，使几何成为世界建模与动作预测的原生表示。

### 核心思路/方法
E0.5 是一个直接构建在 3D 基础模型之上的“几何原生”世界-动作模型，包含两项关键创新：
1. 采用 3D 基础模型作为主骨干，使 3D 几何成为世界建模和动作预测的原生表示，而非辅助输入。
2. 显式地联合预测未来 3D 状态与动作，从而捕捉超越“仅动作建模”或“未来视频预测”的几何世界动态。
摘要还提到，E0.5 在 AgiBotWorld-Beta 的超过 160k 条机器人轨迹上进行具身预训练，在预训练的 3D 基础模型内联合学习机器人动作与未来几何；E0.5 是 VWA 系列世界-动作模型的成员。

### 主要贡献
- 提出 E0.5，一种以 3D 基础模型为主干的几何原生世界-动作模型，将 3D 几何作为世界建模与动作预测的原生表示。
- 显式联合预测未来 3D 状态与动作，使模型能够建模几何世界动态。
- 在 RoboTwin 2.0 上，未经具身数据预训练即取得 clean 设置 89.90%、randomized 设置 50.09% 的成功率。
- 在 AgiBotWorld-Beta 的 160k+ 机器人轨迹上进行具身预训练后，在 AgileX Piper 和 Zerith H1 上的真实世界操作平均成功率分别提升约 15 和 7 个百分点。
- 结果表明几何原生基础模型具备获取机器人交互知识并迁移到物理操作任务的潜力。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、计算成本、推理速度、随机化设置成功率偏低的原因、预训练数据规模之外的其他训练细节，也未与其他方法进行系统性对比或消融分析。

### 阅读优先级
中。理由：论文提出“以 3D 基础模型为主干、显式预测未来 3D 状态与动作”的几何原生 WAM 思路，并给出 RoboTwin 2.0 与两个真实机器人平台的结果，对具身智能与 3D 基础模型交叉方向有参考价值；但摘要未提供方法细节、消融、对比与失败分析，需阅读全文才能判断其技术严谨性与可复现性。

</details>

<details>
<summary>Abstract</summary>

World-action models (WAMs) offer a promising framework for embodied intelligence, yet mainstream approaches remain centered on video foundation models or vision-language models. Even when geometric features extracted by 3D models such as VGGT are incorporated, they are typically passed into a video model or VLM that serves as the primary backbone, leaving 3D geometry as an auxiliary input or prediction target rather than the native foundation for world modeling. We present E0.5, a geometry-native world-action model built directly on 3D foundation models. E0.5 introduces two key innovations. First, it adopts a 3D foundation model as the primary backbone, making 3D geometry the native representation for both world modeling and action prediction. Second, it explicitly predicts future 3D states together with actions, enabling the model to capture geometric world dynamics beyond action-only modeling or future video prediction. Experiments on RoboTwin 2.0 first demonstrate the effectiveness of E0.5 without embodied-data pretraining, achieving success rates of 89.90\% and 50.09\% under clean and randomized settings, respectively. Building on these results, we further pretrain E0.5 on more than 160k robot trajectories from AgiBotWorld-Beta, jointly learning robot actions and future geometry within the pretrained 3D foundation. This embodied pretraining improves mean real-world manipulation success rates by approximately 15 and 7 percentage points on AgileX Piper and Zerith H1, respectively. Together, these results demonstrate the potential of geometry-native foundations to acquire robot interaction knowledge and transfer it to physical manipulation. E0.5 embodies this geometry-native approach as a member of the VWA family of world-action models.

</details>

#### 2026-10-26 - PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry

**Authors:** Yihang Chen, Bin Tan, Yujun Shen, Yinghao Xu, Nan Xue
**Links:** [abs](https://arxiv.org/abs/2610.34845) - [pdf](https://arxiv.org/pdf/2610.34845)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, DUSt3R, 3D reconstruction, SfM, SLAM, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry
- 作者：Yihang Chen, Bin Tan, Yujun Shen, Yinghao Xu, Nan Xue
- 出版日期：2026-10-26T04:55:36Z
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（次分类）
- 链接：[摘要](https://arxiv.org/abs/2610.34845) / [PDF](https://arxiv.org/pdf/2610.34845)

### 一句话总结
PosePlaner 通过 flow matching 把位姿精化建模为条件生成问题，以粗几何匹配与初始位姿为条件，并将多个位姿假设融合为单一精化估计，从而在测试阶段为前馈位姿预测器提供基于几何证据的纠正机制。

### 研究问题
摘要指出，近期多视角 Transformer（如 DUSt3R、VGGT）将特征提取、匹配和位姿估计等经典 SfM/SLAM 流程子步骤合并为单次前馈推理，但这种“包含”隐藏了流水线各阶段之间的接口：对应关系、几何与位姿在单次前向中被纠缠在一起。由此带来的问题是：改进主要依赖有监督微调，且在测试阶段缺乏利用几何证据纠正预测的机制。

### 核心思路/方法
- 恢复对应关系与位姿之间的经典耦合，通过 flow matching 将位姿精化视为条件生成问题。
- 输入条件为粗几何匹配与初始位姿，输出为融合后的单一精化位姿估计。
- 该机制被描述为 RANSAC 投票的连续、数据驱动类比。
- 方法在两视角数据上高效训练，但可作为流式 n 视角位姿估计器的周期性精化器使用，且无需重新训练。

### 主要贡献
- 提出 PosePlaner，为前馈位姿预测器补充测试时可用的几何证据纠正机制。
- 将位姿精化表述为基于粗几何匹配和初始位姿的条件生成，并融合位姿假设。
- 在训练上仅使用两视角数据，却能服务于流式 n 视角位姿估计且无需重训练。
- 摘要报告的实验效果包括：纠正前馈预测器的失败、显著改进基于对应关系的求解器、减少长流式序列中的累积漂移。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集、定量指标、失败案例、计算开销或方法适用边界等细节，因此无法基于所给信息进一步判断局限性。

### 阅读优先级
中。理由：该工作针对前馈多视角位姿预测缺乏测试时几何纠正机制的问题，提出可插拔的周期性精化思路，并与经典几何求解器及流式长序列漂移问题相关；但摘要未提供定量结果与实现细节，是否值得优先精读取决于读者对前馈位姿估计、flow matching 位姿精化或流式 3D 重建方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Recent multi-view Transformers (e.g., DUSt3R and VGGT) have advanced 3D reconstruction by scaling training data and model capacity from two views to many views and long sequences, subsuming the classical SfM/SLAM pipeline of feature extraction, matching, and pose estimation in a single feed-forward pass. Yet this subsumption hides the interfaces between pipeline stages---correspondences, geometry, and pose are entangled in a single forward pass, leaving supervised fine-tuning as the major path to improvement and offering no mechanism to correct predictions from geometric evidence at test time. We propose PosePlaner to close this gap by reviving the classical coupling between correspondences and pose via flow matching, treating pose refinement as a conditional generation problem that takes coarse geometric matches and initial pose as input condition and fuses the resulting pose hypotheses into a single refined estimate, providing a continuous, data-driven analog of RANSAC voting. Our method is trained efficiently on two-view data, yet serves as a periodic refiner for streaming n-view pose estimators with no retraining. Empirically, it corrects failures of feed-forward predictors, substantially improves correspondence-based solvers, and reduces accumulated drift in long streaming sequences.

</details>

#### 2026-10-25 - Fovea-JEPA: Overcoming Geometric Blind Spots in V-JEPA for Camera Motion Recognition

**Authors:** Xiangkun Shi, Hanhui Li, Shiyue Zhang, Chang Liu, Junwen Pan, Zhenbang Sun, Xiaodan Liang
**Links:** [abs](https://arxiv.org/abs/2610.34033) - [pdf](https://arxiv.org/pdf/2610.34033)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fovea-JEPA: Overcoming Geometric Blind Spots in V-JEPA for Camera Motion Recognition
- 作者：Xiangkun Shi, Hanhui Li, Shiyue Zhang, Chang Liu, Junwen Pan, Zhenbang Sun, Xiaodan Liang
- 出版日期：2026-10-25T03:54:24Z
- 分类：主分类 Geometry Foundation Models；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.34033)｜[PDF](https://arxiv.org/pdf/2610.34033)

### 一句话总结
论文提出 Fovea-JEPA，用 VGGT 作为几何专家识别并弥补 V-JEPA 在相机运动识别中的“几何盲点”，通过介入伪标签和 token 级响应图实现视觉与几何特征的自适应融合。

### 研究问题
相机运动识别需要将相机平移、旋转或缩放造成的视角变化与物体运动、场景动态区分开。摘要指出，视频-语言模型常依赖语义线索，难以提供该任务所需的几何证据；V-JEPA 等联合嵌入预测架构虽具有较强时空表示，但实验显示其在部分区域对几何线索表示不足。摘要将这类区域称为“几何盲点”，并指出在时间反转监督下，V-JEPA 总体提升但在若干运动类别上退化，而一个较弱的、面向几何的 VGGT 预测器却在所有运动类别上均有提升。

### 核心思路/方法
- 以 V-JEPA 为基础模型，以 VGGT 作为几何专家。
- 根据二者的预测误差构造“介入伪标签”，用于弱监督一个盲点预测器。
- 盲点预测器输出 token 级响应图，并聚合为片段级介入分数。
- 使用该介入分数指导视觉特征与几何特征的自适应融合，以选择性引入互补几何信息，同时保留可靠的视觉预测。

### 主要贡献
- 识别并形式化 V-JEPA 在相机运动识别中的“几何盲点”问题。
- 提出 Fovea-JEPA，通过介入伪标签、盲点预测器和自适应融合机制，选择性引入 VGGT 的几何信息。
- 摘要报告在 CameraMotionDataset、CameraBench 和 ShotBench 上分别相对此前报告的最优基线提升 9.67、8.67 和 24.38 个百分点。

### 局限性
- 摘要未提供足够信息说明方法在不同相机运动类别上的细粒度表现、失败案例或计算开销。
- 摘要未提供足够信息说明“介入伪标签”的构造细节、盲点预测器的具体结构及训练稳定性。
- 摘要未提供足够信息说明三个数据集上的完整实验设置、消融结果与统计显著性。
- 代码与模型“录用后发布”，摘要未提供当前可复现性信息。

### 阅读优先级
高。理由：该论文直接针对 V-JEPA 的几何表示不足提出可操作的选择性融合方法，并在三个相机运动相关基准上报告了较大幅度提升；若关注视频几何表示、相机运动识别或基础模型互补融合，值得优先阅读。但需注意当前判断仅基于摘要，实验细节与可复现性信息尚不充分。

</details>

<details>
<summary>Abstract</summary>

Camera motion recognition requires separating viewpoint changes caused by camera translation, rotation, or zoom from object motion and scene dynamics. Video-language models often rely on semantic cues and struggle with the geometric evidence needed for this task. Joint-Embedding Predictive Architectures such as V-JEPA offer strong spatio-temporal representations, but our experiments suggest that they underrepresent geometric cues in some regions. Under temporal-reversal supervision, V-JEPA improves overall but degrades on several motion families, whereas a weaker geometry-oriented VGGT predictor improves across all families. We refer to these geometrically underrepresented regions as geometric blind spots and propose Fovea-JEPA to identify and address them. Using V-JEPA as the base model and VGGT as a geometry expert, we construct intervention pseudo-labels from their prediction errors to weakly supervise a blind-spot predictor. The predictor produces token-wise response maps, which are aggregated into a clip-level intervention score to guide adaptive fusion of visual and geometric features. This selective intervention introduces complementary geometric information while preserving reliable visual predictions. Experiments on CameraMotionDataset, CameraBench, and ShotBench demonstrate the effectiveness of Fovea-JEPA, with gains of 9.67, 8.67, and 24.38 percentage points over previously reported state-of-the-art baselines, respectively. Code and models will be released upon acceptance.

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

#### 2026-10-26 - GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting

**Authors:** Tom Yachil, Andrei Sharf
**Links:** [abs](https://arxiv.org/abs/2610.35224) - [pdf](https://arxiv.org/pdf/2610.35224)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting
- 作者：Tom Yachil, Andrei Sharf
- 出版日期：2026-10-26T11:14:09Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.35224) / [PDF](https://arxiv.org/pdf/2610.35224)

### 一句话总结
该论文提出 GaussianSpline，用自适应的非均匀分段三次 Bézier 样条建模每个高斯的运动，并联合学习控制点与时间分段，以提升高度动态场景的 4D Gaussian Splatting 重建质量。

### 研究问题
现有动态 4D Gaussian Splatting 方法常基于全局形变、固定阶多项式或均匀参数化样条，摘要指出这些方式难以同时兼顾复杂快速运动与近静态区域的紧凑表示；论文关注如何在每个高斯的轨迹表示中实现全局平滑与局部自适应。

### 核心思路/方法
- 对每个高斯使用自适应、非均匀的分段三次 Bézier 样条建模运动。
- 联合学习 Bézier 控制点与每个高斯轨迹的时间划分，而非采用全局形变、固定阶多项式或均匀参数化样条。
- 该自适应表示将更多时间容量分配给高度动态区域，同时让近静态区域保持紧凑轨迹。
- 使用基于控制点反射的约束，在相邻 Bézier 段之间施加 \(G^1\) 连续性，以兼顾全局平滑运动与局部自适应。
- 摘要称由此获得平滑、完全可微的轨迹，同时保留非均匀时间参数化的灵活性。

### 主要贡献
- 提出 GaussianSpline：一种基于自适应非均匀分段三次 Bézier 样条逐高斯运动的动态 4D Gaussian Splatting 方法。
- 联合学习 Bézier 控制点和每个高斯轨迹的时间分区，实现动态区域与近静态区域之间的时间容量自适应分配。
- 通过反射式控制点约束实现相邻 Bézier 段间的 \(G^1\) 连续性，支持平滑且完全可微的轨迹。
- 摘要报告在 Neural 3D Video benchmark、Google Immersive dataset 以及合成场景上的实验表明：在高度非均匀和困难动态场景中重建质量显著提升，同时在一般动态场景上与先进 4D Gaussian Splatting 方法保持有竞争力的性能。

### 局限性
- 摘要未提供足够信息说明方法的具体计算开销、训练时间或内存占用。
- 摘要未提供足够信息说明 Bézier 段数量、时间分区策略的超参数敏感性或失败案例。
- 摘要未提供足够信息说明在极端运动、遮挡或稀疏视角下的具体表现。
- 摘要未提供足够信息说明与各基线方法的完整定量对比细节。

### 阅读优先级
中。理由：该论文聚焦 4D Gaussian Splatting 中逐高斯自适应样条运动表示，问题和方法描述较清晰，且摘要声称在高度动态场景上有明显改进；但当前仅有摘要与元数据，缺少定量结果和实现细节，适合作为动态/4D 重建方向的候选阅读，需进一步查看全文后再判断优先级是否提升。

</details>

<details>
<summary>Abstract</summary>

We present GaussianSpline, a dynamic 4D Gaussian Splatting method that models per-Gaussian motion using adaptive, non-uniform piecewise cubic Bézier splines. Unlike approaches based on global deformations, fixed-order polynomials, or uniformly parameterized splines, GaussianSpline jointly learns the Bézier control points and the temporal partition of each Gaussian's trajectory. This adaptive representation allocates greater temporal capacity to highly dynamic regions while maintaining compact trajectories for near-static regions, enabling high-fidelity reconstruction of complex and rapidly changing motion. To jointly achieve globally smooth motion and local adaptivity, we enforce $G^1$ continuity between consecutive Bézier segments using a reflection-based constraint on their control points. This produces smooth, fully differentiable trajectories while preserving the flexibility of non-uniform temporal parameterization. Experiments on the Neural 3D Video benchmark, the Google Immersive dataset, as well as on synthetic scenes demonstrate that GaussianSpline substantially improves reconstruction quality in scenes with highly non-uniform and challenging dynamics, while maintaining competitive performance on general dynamic scenes compared with state-of-the-art 4D Gaussian Splatting methods.

</details>

#### 2026-10-26 - DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction

**Authors:** Beizhen Zhao, Nanjie Yao, Boyi Fu, Qingsong Yan, Haofan Ren, Kaiyong Zhao, Hao Wang
**Links:** [abs](https://arxiv.org/abs/2610.35002) - [pdf](https://arxiv.org/pdf/2610.35002)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction
- 作者：Beizhen Zhao, Nanjie Yao, Boyi Fu, Qingsong Yan, Haofan Ren, Kaiyong Zhao, Hao Wang
- 出版日期：2026-10-26T08:14:00Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.35002 ；PDF https://arxiv.org/pdf/2610.35002

### 一句话总结
论文提出 DUET4D，一个面向稀疏视角 4D 高斯泼溅的自校正耦合引导框架，用当前 4D 表示反向引导生成先验，以提供时空一致的监督，并抑制冗余基元与漂浮伪影。

### 研究问题
稀疏视角 4D 重建在仅有少量相机时高度欠约束。摘要指出：生成先验可恢复缺失外观，但视频模型用于迭代重建在计算上不现实，而单视图模型产生的伪观测在时间上不一致；此外，将不确定的生成输出直接吸收进高斯优化，常导致冗余基元与漂浮伪影。

### 核心思路/方法
- 总体框架：DUET4D 是用于稀疏视角 4D 高斯泼溅的自校正耦合引导框架。
- 自校正循环：4D 表示引导生成先验，生成先验再为 4D 表示提供时空一致的监督。
- 具体步骤一：从当前高斯证据构建序列对齐，用于引导潜空间恢复。
- 具体步骤二：使用 Sequential Fidelity Resampling 将生成监督提升到高斯空间，以选择性区分被重复支持的基元。
- 循环机制：校正后的表示再为下一轮恢复提供更可靠的高斯证据。
- 摘要未提供足够信息说明网络结构细节、损失函数形式、训练数据与具体实现参数。

### 主要贡献
- 提出 DUET4D，将稀疏视角 4D 重建表述为“4D 表示—生成先验”耦合的自校正引导过程。
- 设计从当前高斯证据到潜空间恢复的序列对齐机制，以引导生成先验。
- 提出 Sequential Fidelity Resampling，将生成监督提升到高斯空间并筛选被重复支持的基元，以缓解冗余基元与漂浮伪影。
- 摘要称大量实验表明该方法显著提升渲染质量与渲染效率；具体数据集、指标与对比方法摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法对相机数量下限、视角分布、动态复杂度或生成先验质量的敏感性。
- 摘要未提供足够信息说明计算开销、迭代轮数、收敛性及失败案例。
- 摘要未提供足够信息说明与视频模型、单视图模型及其他稀疏视角 4D 方法的定量对比细节。
- 摘要未提供足够信息说明 Sequential Fidelity Resampling 的阈值设计、消融实验与统计显著性。

### 阅读优先级
中。理由：该论文聚焦稀疏视角 4D 重建中生成先验与高斯优化的耦合问题，问题定义清晰，方法包含自校正循环与重采样筛选，对动态 4D 重建与神经渲染方向有潜在参考价值；但摘要未给出定量结果、数据集与实现细节，需阅读全文后才能判断其实际效果与可复现性。

</details>

<details>
<summary>Abstract</summary>

Sparse-view 4D reconstruction is highly under-constrained when only a few cameras are available. Generative priors can recover missing appearances, but video models are computationally impractical for iterative reconstruction, whereas single-view models produce temporally inconsistent pseudo-observations. Moreover, directly absorbing uncertain generative outputs into Gaussian optimization often creates redundant primitives and floating artifacts. To address these challenges, we propose DUET4D, a self-corrective coupled guidance framework for sparse-view 4D Gaussian splatting. The core of our approach is a self-corrective framework where the 4D representation guides generative prior for spatio-temporal consistent supervisions. We first construct sequential alignments from current Gaussian evidence to steer the latent restoration. Then we use Sequential Fidelity Resampling to lift generative supervisions into Gaussian space to selectively distinguish repeatedly supported primitives. The corrected representation then provides more reliable Gaussian evidence for the next restoration cycle. Extensive experiments demonstrate that DUET4D significantly improves rendering quality and rendering efficiency.

</details>

#### 2026-10-26 - DimFlow: Bidirectional Grid-Expert Learning for Dynamic Gaussian Reconstruction

**Authors:** Gabriel Adineera, Jinoh Kim
**Links:** [abs](https://arxiv.org/abs/2610.34952) - [pdf](https://arxiv.org/pdf/2610.34952)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, NeRF, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DimFlow: Bidirectional Grid-Expert Learning for Dynamic Gaussian Reconstruction
- 作者：Gabriel Adineera, Jinoh Kim
- 出版日期：2026-10-26T07:20:03Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.34952 ；PDF https://arxiv.org/pdf/2610.34952

### 一句话总结
DimFlow 通过多分辨率网格与坐标专家分支的双向交互学习动态高斯重建所需的紧凑场景特征，并在 D-NeRF、HyperNeRF、DAVIS 的汇总比较中报告 39.73 dB PSNR、85 FPS 与 18.9 MB 模型体积。

### 研究问题
动态高斯重建需要紧凑的场景特征来支持几何与外观的协同变化。分解式网格能提供高效的局部查询，但仅靠准确的插值并不能保证所得动态属性在空间和时间上保持兼容。论文要解决的是：如何学习这类特征，使其在空间与时间维度上具有兼容性，并支撑后续动态高斯渲染。

### 核心思路/方法
DimFlow 让多分辨率网格与基于坐标的专家分支进行双向交互来学习特征。具体包括：
- 特征级对抗对齐：连接网格与专家分支的特征分布；
- 自适应融合：传递互补信息；
- 激活掩码残差反馈：在训练过程中细化网格；
- 四个属性专家：分别组织形变、旋转、不透明度与时间信息，再进入高斯渲染。

### 主要贡献
- 提出 DimFlow 框架，以网格—专家分支的双向交互学习动态高斯重建特征。
- 引入特征级对抗对齐、自适应融合与激活掩码残差反馈，用于连接分布、传递互补信息并在训练中细化网格。
- 设计四个属性专家，分别组织形变、旋转、不透明度与时间信息。
- 在 D-NeRF、HyperNeRF、DAVIS 的汇总比较中报告 39.73 dB PSNR，较 4D-GS 提升 1.92 dB，并匹配其报告的 85 FPS 渲染速度；模型体积 18.9 MB，4D-GS 为 18.3 MB。
- 组件与属性专家消融显示特征对齐、自适应交换与时间处理的互补贡献。

### 局限性
- 摘要仅给出汇总比较结果，未提供各数据集上的逐项指标、训练设置、运行环境与误差分析；“摘要未提供足够信息”。
- 摘要未说明特征级对抗对齐、自适应融合与激活掩码残差反馈的具体实现细节与超参数；“摘要未提供足够信息”。
- 摘要未给出失败案例、边界条件或与其他方法在内存、训练时间等方面的完整对比；“摘要未提供足够信息”。
- 摘要提到模型体积 18.9 MB 略高于 4D-GS 的 18.3 MB，但未讨论该差异的影响；“摘要未提供足够信息”。

### 阅读优先级
中。理由：论文聚焦动态/4D 高斯重建中的网格—专家双向特征学习，报告了 PSNR、FPS 与模型体积的汇总结果，并包含组件与属性专家消融，与动态高斯重建和神经场景表示方向直接相关；但摘要未提供逐数据集细节、训练配置与完整局限性分析，需阅读全文才能判断方法稳健性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Dynamic Gaussian reconstruction requires compact scene features to support coordinated changes in geometry and appearance. A factorized grid provides efficient local queries, but accurate interpolation alone does not ensure that the resulting dynamic attributes remain compatible across space and time. We introduce DimFlow, a framework that learns these features through bidirectional interaction between a multi-resolution grid and a coordinate-based expert branch. Feature-level adversarial alignment connects their distributions, adaptive fusion transfers complementary information, and activation-masked residual feedback refines the grid during training. Four attribute experts organize deformation, rotation, opacity, and temporal information before Gaussian rendering. In the aggregate comparison across D-NeRF, HyperNeRF, and DAVIS, DimFlow achieves 39.73 dB PSNR, improving on 4D-GS by 1.92 dB while matching its reported 85 FPS rendering speed. The model occupies 18.9 MB, compared with 18.3 MB for 4D-GS. Component and attribute-expert ablations reveal complementary contributions from feature alignment, adaptive exchange, and temporal processing.

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

#### 2026-10-26 - Any3R: Feedforward 3D Reconstruction from Any Camera Type

**Authors:** Jingong Chen, Qingwen Zhang, Youming Deng, Chulwoo Pack, Olaf Wysocki, Boris Jutzi, Kwanghee Won, Kyle Gao
**Links:** [abs](https://arxiv.org/abs/2610.36150) - [pdf](https://arxiv.org/pdf/2610.36150)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Any3R: Feedforward 3D Reconstruction from Any Camera Type
- 作者：Jingong Chen, Qingwen Zhang, Youming Deng, Chulwoo Pack, Olaf Wysocki, Boris Jutzi, Kwanghee Won, Kyle Gao
- 出版日期：2026-10-26T18:53:14Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.36150) · [PDF](https://arxiv.org/pdf/2610.36150) · [项目页](https://jingong-chen.github.io/Any3R/)

### 一句话总结
Any3R 是一个前馈三维重建模型，通过用稠密光线场对位置编码和训练损失进行条件化，使其无需按镜头类型重新训练即可处理任意中心相机。

### 研究问题
现有几何基础模型虽能以前馈网络从多张图像恢复相机位姿和稠密几何，但其假设输入为针孔图像；这一假设深入骨干网络内部——位置编码和训练损失都将图像位置绑定到空间方向，且二者依赖镜头。因此，模型难以直接适用于非针孔或异构相机图像。

### 核心思路/方法
论文提出用稠密光线场（每个像素对应的单位方向）同时对位置编码和训练损失进行条件化，该表示可描述任意中心相机，而无需镜头类型、畸变系数或视场角限制。
- **角度坐标**：为旋转编码提供每个 patch 的实测光线角度，并按视图评估。
- **立体角加权**：用每个像素在球面上覆盖的面积缩放点损失。
这样编码与监督均不依赖镜头，模型可接受任意中心相机，并对同一场景混合多种相机类型具有鲁棒性，且无需针对每种镜头重新训练。

### 主要贡献
- 提出 Any3R，一个可接受任意中心相机的前馈三维重建模型。
- 将位置编码与训练损失从针孔假设中解耦，改为基于稠密光线场条件化，并引入角度坐标旋转编码与立体角加权点损失。
- 支持同一场景混合多种相机类型且无需按镜头重训练。
- 在三个数据集、十三种中心相机的基准上，各方法均使用自身预测的相机位姿进行重建时，Any3R 被描述为最 consistently 准确的方法。
- 面向异构众包与档案图像集合的可扩展三维重建。

### 局限性
- 具体网络架构、训练数据规模与训练细节：摘要未提供足够信息。
- 基准数据集的构成、评价指标定义及定量结果：摘要未提供足够信息。
- 对非中心相机（如非中心投影或特殊成像模型）的适用性：摘要未提供足够信息。
- 计算开销、推理速度与内存需求：摘要未提供足够信息。
- 失败案例与鲁棒性边界：摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接针对几何基础模型中“针孔假设”这一基础性限制，方法思路清晰且具有通用性；若关注多视图三维重建、异构相机或前馈几何模型，摘要显示其问题定义与贡献具有较高相关性。但需注意，摘要未给出定量实验细节，深入评估需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Geometry foundation models recover camera poses and dense geometry from a set of images with a feed-forward network, but they expect pinhole images. That assumption is inside the backbone too: the positional encoding and the training loss both bind an image position to a direction in space, and both depend on the lens. We condition both on the dense ray field, the unit direction through every pixel, which describes any central camera without a lens type, distortion coefficients or a bound on field of view. Angular coordinates give the rotary encoding the measured ray angle of each patch, evaluated per view, and solid-angle weighting scales the point loss by the area each pixel covers on the sphere, so neither the encoding nor the supervision depends on the lens. Any3R is therefore a feed-forward model that takes any central camera, and is robust to mixing many camera types per scene, with no retraining per lens. On a benchmark of thirteen central cameras across three datasets, where every method reconstructs with its own predicted camera poses, it is the most consistently accurate method. Any3R enables scalable 3D reconstruction from heterogeneous crowdsourced and archival imagery collections sourced across diverse camera types. Project page: https://jingong-chen.github.io/Any3R/

</details>

#### 2026-10-26 - Metric Scale for Insta360 Structure-from-Motion from the Camera's Embedded IMU

**Authors:** Davide Cuttini, Diego Di Tommaso, Alessio Antoniacomi, Luca Simonetti
**Links:** [abs](https://arxiv.org/abs/2610.35554) - [pdf](https://arxiv.org/pdf/2610.35554)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, structure from motion, SfM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Metric Scale for Insta360 Structure-from-Motion from the Camera's Embedded IMU
- 作者：Davide Cuttini, Diego Di Tommaso, Alessio Antoniacomi, Luca Simonetti
- 出版日期：2026-10-26T14:57:37Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.35554) / [PDF](https://arxiv.org/pdf/2610.35554)

### 一句话总结
论文评估用 Insta360 X5/X6 内置 IMU（1 kHz）替代手机 ARKit/ARCore 位姿，为双鱼眼 SfM 恢复公制尺度，并在多组测量中与 LiDAR、标定板及手机尺度对比。

### 研究问题
消费级 360 度相机双鱼眼视频的 SfM 只能恢复到相似变换，缺少公制尺度。现有流程依赖同步采集的智能手机 ARKit/ARCore 位姿提供尺度。论文要回答：能否仅用相机内置 IMU 实现自包含的公制尺度恢复，以及其精度与手机尺度相比如何。

### 核心思路/方法
- 对 Insta360 X5/X6 内置 IMU 进行传感器表征：噪声密度、相机-IMU 同步、加速度计尺度因子、偏置稳定性。
- 从数据中估计相机-IMU 旋转与帧时间关系。
- 在整段测量的 SfM 位姿上做线性视觉-惯性对齐以恢复尺度。
- 指出标准做法（整段共享重力与加速度计偏置）平均高估尺度 3.4%；改为逐连续段独立估计再平均可消除该偏差。
- 补充窗口构建消融实验，并与单目公制深度网络比较。

### 主要贡献
- 提出并评估一种不依赖手机 AR 位姿、仅用相机内置 IMU 的 SfM 公制尺度恢复方案。
- 给出该 IMU 的表征结果与相机-IMU 旋转、帧时间估计方法。
- 发现并修正整段共享重力/偏置导致的尺度高估偏差。
- 在九组与 LiDAR 同机采集的测量中，惯性尺度平均绝对误差 0.81%，手机尺度为 1.94%；在打印基准标记上两者均在目标 1% 不确定度内一致。
- 在公开基准三十条参考轨迹（尺度 1/40、1、40）上，尺度恢复平均误差 -0.07%，标准差 1.28%。
- 在五十组仅以手机为参考的生产测量中，两种尺度标准差 2.3%，惯性尺度平均低 0.3%；差异与运行长度不相关、随手机锚点范围增大而增大，且无法归因于任一参考。

### 局限性
- 摘要未提供足够信息说明 IMU 表征的具体数值、实验环境条件与失败案例。
- 摘要未提供足够信息说明窗口构建消融与单目公制深度网络比较的具体结果。
- 摘要提到五十组生产测量中两种尺度差异“无法归因于任一参考”，但未给出最终尺度真值判定方法。
- 摘要未提供足够信息说明方法在非 Insta360 相机或其他 IMU 上的泛化性。

### 阅读优先级
中。理由：论文针对 360 相机 SfM 的公制尺度这一明确工程问题，给出了多组定量对比与偏差修正，对使用 Insta360 做三维重建的读者有直接参考价值；但主题较专门，且摘要未展开消融与深度网络对比细节，非该方向读者的普适性有限。

</details>

<details>
<summary>Abstract</summary>

Structure-from-motion (SfM) from the dual-fisheye video of a consumer 360-degree camera recovers geometry only up to a similarity transform; in the pipeline considered here, metric scale is obtained from smartphone ARKit or ARCore poses captured alongside the camera. This paper evaluates a self-contained alternative: the IMU embedded in the Insta360 X5 and X6, recorded at 1 kHz. The sensor is characterised (noise density, camera-IMU synchronisation, accelerometer scale factor, bias stability), the camera-IMU rotation and frame timing are estimated from the data, and the scale is recovered by a linear visual-inertial alignment over the SfM poses of a whole survey. The standard formulation, with gravity and accelerometer bias shared across the survey, overestimates the scale by 3.4% on average; estimating each contiguous segment independently and averaging removes the bias. On nine surveys with a co-mounted LiDAR scanner the inertial scale deviates from the LiDAR by 0.81% in mean absolute error, against 1.94% for the smartphone scale; on printed fiducial markers both agree within the 1% uncertainty of the target. On the reference trajectories of thirty sequences of a public benchmark, brought to scales of 1/40, 1 and 40, the estimator recovers the metric scale with a mean error of -0.07% and a standard deviation of 1.28%. On fifty production surveys where the smartphone is the only reference, the two scales agree to a standard deviation of 2.3%, the inertial scale being 0.3% lower on average; the difference is uncorrelated with run length, grows with the extent of the smartphone anchor, and cannot be attributed to either reference. An ablation over window construction and a comparison with monocular metric-depth networks complete the study.

</details>

#### 2026-10-26 - Generative Structure from Motion with Native 3D Diffusion

**Authors:** Haobin Duan, Binbin Huang, Mochu Xiang, Yiqun Zhao, Zibo Zhao, Yi Ma, Shenghua Gao
**Links:** [abs](https://arxiv.org/abs/2610.35522) - [pdf](https://arxiv.org/pdf/2610.35522)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Generative Structure from Motion with Native 3D Diffusion
- 作者：Haobin Duan, Binbin Huang, Mochu Xiang, Yiqun Zhao, Zibo Zhao, Yi Ma, Shenghua Gao
- 出版日期：2026-10-26T14:40:40Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.35522) | [PDF](https://arxiv.org/pdf/2610.35522)

### 一句话总结
GenSfM 将基于图像的 3D 重建与原生 3D 扩散模型结合，在共享自注意力下联合去噪形状潜变量与逐视图位姿潜变量，从少量未标定视图同时恢复物体 3D 结构与相机运动。

### 研究问题
论文关注从少量未标定视图恢复物体的 3D 结构与相机运动这一计算机视觉基础问题。摘要指出：经典 Structure-from-Motion 方法能恢复与输入图像一致的 3D 几何，但无法恢复未观测区域；原生生成方法能生成看似合理的 3D 物体，但与输入图像的相关性不一定忠实。简单地将重建与生成串联会导致误差在两个阶段间级联，难以得到同时符合数据分布与输入图像的 3D 物体。

### 核心思路/方法
摘要给出的方法要点如下：
- 提出 GenSfM，将基于图像的 3D 重建与原生 3D 扩散模型集成。
- 使用多模态扩散 Transformer，在共享自注意力机制下联合去噪形状潜变量与逐视图位姿潜变量，使生成几何以观测视图为条件，并利用物体级先验推断未观测区域。
- 采用紧凑的 3D 原生 UV-volume tokenization，使视图增加时联合序列仍保持较小规模。
- 使用位姿感知阶段，在恢复的相机位姿下采样逐体素图像特征，以细化几何与纹理。

### 主要贡献
- 提出 GenSfM，将图像 3D 重建与原生 3D 扩散模型结合，以联合去噪方式处理形状与位姿，而非简单串联重建与生成。
- 引入多模态扩散 Transformer 的共享自注意力联合去噪机制，使生成几何同时受观测视图约束并利用物体级先验。
- 提出紧凑的 3D 原生 UV-volume tokenization，控制多视图联合序列规模。
- 设计位姿感知细化阶段，在恢复位姿下采样逐体素图像特征以细化几何与纹理。
- 摘要报告在 Toys4k 与 GSO 上、使用 4 个未标定视图时，相较强原生 3D 生成基线，新视角 PSNR 提升 3.2–4.5 dB，中位 Chamfer 距离降低 2.8–3.8 倍；输入视图位姿恢复达到 96% 以上 Acc@5°，且无需外部位姿估计骨干、事后优化或已知内参。

### 局限性
摘要未提供足够信息。摘要未说明方法失败场景、计算开销、对视图数量或物体类别的敏感性、与重建类基线的完整对比，也未给出消融实验细节。

### 阅读优先级
中。理由：该论文面向少视图未标定条件下的 3D 重建与位姿恢复，试图统一重建与生成并避免两阶段误差级联，且摘要给出明确的定量提升与无需外部位姿骨干的特点；但摘要未提供方法细节、失败案例与完整实验设置，需阅读全文才能判断其适用边界与可复现性。

</details>

<details>
<summary>Abstract</summary>

Recovering an object's 3D structure and camera motion from a few uncalibrated views is a fundamental problem in computer vision. Classical structure from motion methods recover 3D geometry consistent with the input images but cannot recover unseen regions; native generation methods produce plausible 3D objects which are related but not necessarily faithful to the input images. Methods simply concatenating reconstruction and generation allow error to cascade across the two stages, instead of producing a 3D object consistent with both the distribution and the input. We propose GenSfM, which integrates image-based 3D reconstruction with a native 3D diffusion model. In particular, we use a multi-modal diffusion transformer to jointly denoise the shape latent and per-view pose latents under shared self-attention, grounding generated geometry in the observed views while using object-level priors to infer unobserved regions. A compact 3D-native UV-volume tokenization keeps the joint sequence small as views are added, and a pose-aware stage refines geometry and texture by sampling per-voxel image features at the recovered camera poses. On Toys4k and GSO, for $4$ uncalibrated views, GenSfM improves novel-view PSNR by $3.2$-$4.5$ dB and reduces median Chamfer distance by $2.8$-$3.8\times$ over a strong native-3D generation baseline, while recovering input-view poses over $96\%$ Acc@$5^\circ$ without any external pose-estimation backbone, post-hoc optimization, or known intrinsics. Project page: https://dotb1ue.github.io/GenSfm/.

</details>

#### 2026-10-26 - Learning Scene Coordinate Reconstruction from Unposed Images via Pose Graph Optimization

**Authors:** Tze Ho Elden Tse, Jizong Peng, Angela Yao
**Links:** [abs](https://arxiv.org/abs/2610.35501) - [pdf](https://arxiv.org/pdf/2610.35501)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** geometric reasoning, structure from motion, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Scene Coordinate Reconstruction from Unposed Images via Pose Graph Optimization
- 作者：Tze Ho Elden Tse, Jizong Peng, Angela Yao
- 出版日期：2026-10-26T14:29:13Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.35501 ；PDF https://arxiv.org/pdf/2610.35501

### 一句话总结
该论文在无需真值监督的 ACE-Zero 类学习式 structure-from-motion 流程中引入位姿图优化，并利用极线与光流一致性估计置信度，以缓解相机位姿漂移和错误精化问题。

### 研究问题
论文关注的是：基于学习的 structure-from-motion 方法（如 ACE-Zero）虽然能够从无序图像集合中估计相机位姿和场景坐标，且不依赖真值监督，但 ACE-Zero 缺少全局和多视图一致性约束，因此在复杂或歧义场景中容易出现位姿漂移与错位。作者希望在不改变学习式推理主体的前提下，增强位姿估计的鲁棒性和准确性。

### 核心思路/方法
论文提出一个混合框架，将位姿图优化（PGO）集成到 ACE-Zero 中，用于精化相机位姿并抑制错误的精化结果。具体做法包括：
1. 直接从 ACE-Zero 的输出构建位姿图，通过预测的场景坐标提取相对位姿约束；
2. 引入不确定性感知的优化策略，利用几何先验估计置信度分数，包括跨视图的极线一致性和光流一致性；
3. 通过上述全局几何推理对学习式推理进行补充，以提升 structure-from-motion 中的位姿估计表现。

### 主要贡献
- 提出将位姿图优化与 ACE-Zero 结合的混合框架，用于从无序、无位姿图像中精化相机位姿。
- 设计从 ACE-Zero 预测场景坐标中提取相对位姿约束并构建位姿图的方式。
- 引入基于几何先验（极线一致性与光流一致性）的不确定性感知优化策略，以抑制不可靠的精化。
- 论证全局几何推理可以有效补充学习式 structure-from-motion 推理。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集、评价指标、定量实验结果、计算开销、实时性分析，也未说明方法在何种场景或失败模式下的具体边界。

### 阅读优先级
中。理由：该论文针对学习式 structure-from-motion 中位姿漂移和多视图一致性问题提出明确的混合优化思路，问题定位清晰，方法组合具有参考价值；但摘要未提供定量结果和实验细节，是否显著优于现有方法尚无法从给定信息判断。若关注无位姿图像的三维重建、位姿图优化与学习式 SfM 结合，建议优先阅读；若仅需结论性性能对比，则需进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

Learning-based structure-from-motion methods such as ACE-Zero have demonstrated strong performance in estimating cameraposes and scene coordinates from unordered image collections without requiring ground truth supervision. However, the lack of global and multi-view consistency constraints in ACE-Zero can lead to pose drift and misalignment, particularly in complex or ambiguous scenes. In this work, we propose a hybrid framework that integrates pose graph optimization (PGO) into ACE-Zero to refine camera poses and suppress incorrect refinements. We construct pose graphs directly from ACE-Zero outputs by extracting relative pose constraints from predicted scene coordinates. Furthermore, we introduce an uncertainty-aware optimization strategy by estimating confidence scores using geometric priors, including epipolar and optical flow consistencies across views. Our approach improves the robustness and accuracy of pose estimation, demonstrating that global geometric reasoning can effectively complement learning-based inference in structure-from-motion.

</details>

#### 2026-10-26 - SG-Splat: Stable Geometry Learning under Pose Uncertainty for Pose-Free 3D Gaussian Splatting

**Authors:** Xiaohan Lu, Jiaqi Zhang, Weijia Jiang, Siwei Ma
**Links:** [abs](https://arxiv.org/abs/2610.35361) - [pdf](https://arxiv.org/pdf/2610.35361)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, pose estimation, bundle adjustment, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SG-Splat: Stable Geometry Learning under Pose Uncertainty for Pose-Free 3D Gaussian Splatting
- 作者：Xiaohan Lu, Jiaqi Zhang, Weijia Jiang, Siwei Ma
- 出版日期：2026-10-26T12:50:21Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Neural Scene Representations & Rendering（次分类）
- 链接：[摘要](https://arxiv.org/abs/2610.35361) ｜ [PDF](https://arxiv.org/pdf/2610.35361)

### 一句话总结
SG-Splat 是一个无位姿前馈 3D Gaussian Splatting 框架，通过解耦几何估计与高斯属性预测、引入由粗到细的位姿与几何修正流程，以及混合真实与预测位姿的双路径训练策略，提升对残余位姿误差的鲁棒性并稳定高斯基元学习。

### 研究问题
现有无位姿前馈 3DGS 方法直接从无位姿输入图像重建高斯表示，但仍对残余位姿误差敏感：位姿误差会扰动规范空间中的高斯变换，从而给几何与属性学习引入噪声监督。论文旨在解决这一位姿不确定性下的几何学习不稳定问题。

### 核心思路/方法
- 将几何估计与高斯属性预测解耦为两个专用分支，以减少位姿敏感的几何误差与高斯属性之间的误差耦合。
- 引入由粗到细的修正流程：
  - Flow-Guided Pose Refinement（FGPR）：利用基于光流的相关特征与可微 bundle adjustment 精化相机位姿。
  - Residual-Guided Geometry Correction（RGC）：利用 FGPR 得到的深度残差修正初始点图，从而获得更可靠的高斯中心。
- 训练稳定化：采用双路径策略，混合真实位姿与预测位姿进行规范变换，为高斯属性提供干净监督，同时提升几何对残余位姿误差的鲁棒性。

### 主要贡献
- 提出 SG-Splat，一个面向位姿不确定性的无位姿前馈 3DGS 框架，提升对残余位姿误差的鲁棒性并稳定高斯基元学习。
- 设计几何估计与高斯属性预测的双分支解耦结构，降低误差耦合。
- 提出 FGPR 与 RGC 组成的由粗到细修正流程，在高斯属性重建前改善几何对齐。
- 引入混合真实位姿与预测位姿的双路径训练策略，为高斯属性提供干净监督并增强几何鲁棒性。
- 摘要称在 DL3DV 与 RealEstate10K 上于新视角合成与位姿估计两项任务均达到 state-of-the-art 性能。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、计算开销、对真实位姿监督的依赖程度、分支解耦的具体代价，以及在不同位姿噪声水平下的定量退化分析等细节。

### 阅读优先级
高。理由：该论文直接针对无位姿前馈 3DGS 中位姿误差传播导致几何学习不稳定的关键问题，方法上同时涉及解耦架构、可微位姿精化与训练策略，且摘要声称在新视角合成与位姿估计上均达到 state-of-the-art；对 3D 重建、多视角几何与神经渲染交叉方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become a promising representation for real-time novel view synthesis and 3D scene reconstruction. For practical deployment, recent studies have explored pose-free feed-forward 3DGS, which reconstructs Gaussian representations directly from unposed input images. However, these methods remain sensitive to residual pose errors, which perturb canonical-space Gaussian transformation, introducing noisy supervision for geometry and attribute learning. To address this problem, we present SG-Splat, a pose-free feed-forward 3DGS framework that improves robustness to pose uncertainty and stabilizes the learning of Gaussian primitives. SG-Splat decouples geometry estimation and Gaussian attribute prediction into two dedicated branches, reducing error coupling between pose-sensitive geometry and Gaussian attributes. We further introduce a coarse-to-fine refinement pipeline, consisting of Flow-Guided Pose Refinement (FGPR) and Residual-Guided Geometry Correction (RGC), to improve geometric alignment before Gaussian attribute reconstruction. Specifically, FGPR refines camera poses with flow-based correlation features and differentiable bundle adjustment. RGC then corrects initial point maps using depth residuals derived from FGPR, producing more reliable Gaussian centers. To stabilize training, we introduce a dual-path strategy that mixes ground-truth and predicted poses for canonical transformation. It provides clean supervision for Gaussian attributes while improving geometry robustness to residual pose errors. Extensive experiments on DL3DV and RealEstate10K show that SG-Splat achieves state-of-the-art performance in both novel view synthesis and pose estimation.

</details>

#### 2026-10-26 - CVTSplat: Multi-view Reconstruction Using an Adaptive Centroidal Voronoi Tessellation

**Authors:** Briac Toussaint, Diego Thomas, Jean-Sébastien Franco, Edmond Boyer, Christian Theobalt
**Links:** [abs](https://arxiv.org/abs/2610.35347) - [pdf](https://arxiv.org/pdf/2610.35347)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CVTSplat: Multi-view Reconstruction Using an Adaptive Centroidal Voronoi Tessellation
- 作者：Briac Toussaint, Diego Thomas, Jean-Sébastien Franco, Edmond Boyer, Christian Theobalt
- 出版日期：2026-10-26T12:39:58Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.35347) | [PDF](https://arxiv.org/pdf/2610.35347)

### 一句话总结
CVTSplat 提出使用自适应质心 Voronoi 剖分（CVT），在多视图重建中兼顾自适应空间划分与形状较规则的单元，以提高优化过程中的剖分与渲染效率。

### 研究问题
摘要指出，Voronoi 剖分已被用于从多视图图像进行形状与外观重建的自适应空间划分离散化；但常规 Voronoi 产生的不规则单元会使优化过程中反复重建剖分的代价较高。论文关注的问题是如何在保持自适应性的同时，使单元更规则、便于高效计算与重建。

### 核心思路/方法
论文探索自适应质心 Voronoi 剖分（CVT）：在标准 CVT 基础上引入非均匀单元尺寸，同时保留规则、形状良好的单元。CVTSplat 中，单元尺寸由不断演化的 signed distance field 调制，使站点（sites）集中在零水平集附近，同时保持单元接近质心化。由于单元具有规则性，作者对整个流程进行专门化，包括用于最近邻查询与近似 Voronoi 构建的 GPU 算法，以及面向小型、近似各向同性单元的 rasterizer。摘要称，在这一情形下其 Voronoi 构建比通用替代方案快 5 至 10 倍。

### 主要贡献
- 提出 CVTSplat，将自适应 CVT 用于多视图重建，以非均匀单元尺寸适配 signed distance field，同时保持单元接近质心化与规则形状。
- 针对该规则单元特性专门化流程，包括 GPU 最近邻查询、近似 Voronoi 构建以及面向小型近各向同性单元的 rasterizer。
- 摘要报告其 Voronoi 构建在此情形下比通用方案快 5 至 10 倍。
- 在 DTU 与 BlendedMVS 上，摘要称其几何精度可与最佳 Gaussian-splatting 表面方法竞争，且单 GPU 训练约 2.5 分钟。

### 局限性
摘要未提供足够信息。摘要未说明方法在复杂拓扑、大尺度场景、内存开销、对初始化或超参数的敏感性、与其他方法训练时间的完整对比，也未给出失败案例或定量误差细节。

### 阅读优先级
中。理由：该工作聚焦多视图重建中的自适应空间划分与效率问题，摘要给出了明确的加速与训练时间主张，并与 Gaussian-splatting 表面方法进行精度对比；但摘要未提供足够实验细节与局限性信息，是否优先精读取决于读者对 Voronoi 离散化、GPU 重建流程或快速多视图表面重建的关注程度。

</details>

<details>
<summary>Abstract</summary>

Voronoi tessellations have recently emerged as an adaptive, space-partitioning discretization for shape and appearance reconstruction from multi-view images. However, the irregular cells they produce make the repeated reconstruction of the tessellation during optimization costly. We therefore explore adaptive centroidal Voronoi tessellations (CVTs), which extend standard CVTs with non-uniform cell sizes while preserving the regular, well-shaped cells that make them efficient to compute. In CVTSplat, cell size is modulated by the evolving signed distance field, concentrating sites near the zero level set while keeping cells nearly centroidal. This regularity lets us specialize the whole pipeline, with GPU algorithms for nearest-neighbor queries and approximate Voronoi construction, and a rasterizer tailored to small, nearly isotropic cells. Our Voronoi construction is 5 to 10 times faster than general-purpose alternatives in this regime. On DTU and BlendedMVS, CVTSplat reaches geometric accuracy competitive with the best Gaussian-splatting surface methods while training in about 2.5 minutes on a single GPU.

</details>

#### 2026-10-26 - Zero-Shot Monocular Depth Estimation for Visual Perception in Lower-Limb Prostheses

**Authors:** Ishi Vijayvergiya, Marc Hölle, Youssef Dawoud, Amir El-Ghoussani, Michele De Vita, Rohan Asthana, Philipp Beckerle, Vasileios Belagiannis
**Links:** [abs](https://arxiv.org/abs/2610.35018) - [pdf](https://arxiv.org/pdf/2610.35018)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Zero-Shot Monocular Depth Estimation for Visual Perception in Lower-Limb Prostheses
- 作者：Ishi Vijayvergiya, Marc Hölle, Youssef Dawoud, Amir El-Ghoussani, Michele De Vita, Rohan Asthana, Philipp Beckerle, Vasileios Belagiannis
- 出版日期：2026-10-26T08:30:31Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.35018) / [PDF](https://arxiv.org/pdf/2610.35018)

### 一句话总结
论文面向下肢假肢的视觉感知场景，构建了模拟膝部假肢视角的 LP 数据集，并对四个先进单目深度估计基础模型的零样本表现进行系统评测。

### 研究问题
单目深度估计基础模型已在多样视觉域中表现出较强的零样本泛化能力，但这类模型能否用于下肢假肢的视觉感知尚缺乏系统研究。假肢使用者在楼梯、不平整地形等复杂环境中导航时，需要可靠的深度感知，因此有必要评估从假肢视角出发的深度估计性能。

### 核心思路/方法
论文提出 Lower-Limb Prosthesis（LP）数据集，作为从模拟膝部假肢视角评估深度感知的基准；在该数据集上对四个先进的单目深度估计基础模型进行评测，以分析这些模型在假肢视角下的零样本深度估计表现。

### 主要贡献
- 引入 LP 数据集，用于从模拟膝部假肢视角评测深度感知。
- 基于该数据集对四个先进的单目深度估计基础模型进行评估。
- 提供首个从假肢视角开展的单目深度估计性能系统基准，并揭示基础模型在假肢感知系统中部署的挑战与潜力。

### 局限性
- 摘要未提供足够信息说明所评测的四个模型具体名称、评测指标、定量结果及误差分析。
- 摘要未提供足够信息说明 LP 数据集的规模、采集方式、场景构成与标注细节。
- 摘要未提供足够信息说明模拟膝部假肢视角的具体构建方式及其与真实假肢感知系统的差异。
- 摘要未提供足够信息说明是否包含真实假肢使用者实验或临床验证。

### 阅读优先级
中。理由：该论文将零样本单目深度估计基础模型与下肢假肢视觉感知这一具体应用场景结合，并提出新基准数据集，对计算机视觉在辅助感知中的应用研究具有参考价值；但摘要未给出具体模型、实验设置和定量结论，是否值得深入阅读需结合全文实验细节进一步判断。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation has advanced rapidly with the development of foundation models that demonstrate strong zero-shot generalisation across diverse visual domains. However, the applicability of these models to visual perception for lower-limb prosthetics remains largely unexplored. Reliable depth perception is particularly important for prosthesis users, who often experience significant challenges when navigating stairs, uneven terrain, and other complex environments. To address this gap, we introduce the Lower-Limb Prosthesis (LP) dataset, a benchmark designed to evaluate depth perception from an emulated knee-level prosthetic viewpoint. Using this dataset, we evaluate four state-of-the-art monocular depth estimation foundation models. Our results provide the first systematic benchmark of monocular depth estimation performance from a prosthetic viewpoint, while highlighting both the challenges and the potential of deploying foundation models in prosthetic perception systems. The code and dataset are available at https://github.com/Ishivijay/lp_dataset.

</details>

#### 2026-10-25 - Hybrid Mamba-Transformer Network for Single-Shot 3D Reconstruction from Fringe Patterns

**Authors:** Xinjie Zhou, XiaoLei Li
**Links:** [abs](https://arxiv.org/abs/2610.33988) - [pdf](https://arxiv.org/pdf/2610.33988)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hybrid Mamba-Transformer Network for Single-Shot 3D Reconstruction from Fringe Patterns
- 作者：Xinjie Zhou, XiaoLei Li
- 出版日期：2026-10-25T01:58:48Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2610.33988 ；PDF https://arxiv.org/pdf/2610.33988

### 一句话总结
提出一种基于 Swin U 形架构的 Mamba-Transformer 混合网络，用于从单张条纹图回归高度，在公开 FPP 数据集上以 MAE、RMSE、绝对相对误差和 SSIM 优于 hNet、SwinConvUNet、UHRNet 与 HiDNet。

### 研究问题
论文关注基于条纹投影轮廓术（FPP）的单帧 3D 重建：如何从单张高频条纹图像中恢复准确表面高度。摘要指出难点在于同时保持长程空间一致性与精细几何细节。卷积网络在建模长程依赖方面受限，而基于窗口的 Transformer 只能随深度增加逐步建立全局交互。

### 核心思路/方法
- 任务形式：条纹到高度（fringe-to-height）回归。
- 总体架构：采用基于 Swin 的 U 形架构，并在中间分辨率的编码器阶段引入视觉状态空间建模。
- 关键模块：提出轴向与膨胀视觉状态空间（ADVSS）块，通过局部、膨胀和轴向深度卷积增强预扫描特征编码，同时保留四方向选择性扫描。
- 设计目标：结合线性复杂度的长程建模与方向感知的局部条纹结构保持能力。

### 主要贡献
- 提出用于单帧 FPP 条纹到高度回归的混合 Mamba-Transformer 网络。
- 在 Swin U 形架构的中间分辨率编码器阶段引入视觉状态空间建模。
- 设计 ADVSS 块，以局部、膨胀、轴向深度卷积增强预扫描特征编码，并保留四方向选择性扫描。
- 在公开 FPP 数据集上与 hNet、SwinConvUNet、UHRNet、HiDNet 对比，在 MAE、RMSE、绝对相对误差和 SSIM 上均取得更优结果。
- 仅使用一张变形条纹图时，报告 RMSE 为 0.548 mm、SSIM 为 0.9985；相对 UHRNet 与 HiDNet，RMSE 分别降低 65.2% 与 59.6%。

### 局限性
- 摘要仅给出在公开 FPP 数据集上的整体指标对比，未提供数据集名称、训练细节、参数量、推理速度或跨数据集泛化结果。
- 摘要未提供消融实验的完整设置与逐项结果，因此各模块（如 ADVSS）的独立增益无法从摘要中确认。
- 摘要未讨论方法在高频条纹、噪声、遮挡或非理想成像条件下的失效情形。
- 上述未提及内容均属于“摘要未提供足够信息”。

### 阅读优先级
中。理由：论文面向单帧 FPP 3D 重建这一明确任务，给出可量化的 RMSE 与 SSIM 改进，并与多个基线对比，主题与 3D 重建分类直接相关；但摘要未提供数据集名称、消融细节、效率指标与泛化实验，若需评估方法可复现性或实际部署价值，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Deep learning facilitates rapid single shot three dimensional (3D) reconstruction using fringe projection profilometry (FPP), but recovering accurate surface height from a single high frequency fringe image remains challenging because both long-range spatial consistency and fine geometric details must be preserved. Convolutional networks are limited in modeling long range dependencies, whereas window-based Transformers establish global interactions only progressively with increasing depth. To address these limitations, a hybrid Mamba Transformer network is proposed for fringe to height regression. The network adopts a Swin based U shaped architecture and introduces visual state space modeling at the intermediate resolution encoder stage. An axial and dilated vision state space (ADVSS) block is further developed to enhance prescan feature encoding through local, dilated, and axial depthwise convolutions while retaining four directional selective scanning. This design combines linear complexity long range modeling with direction aware preservation of local fringe structures. Experiments on a publicly available FPP dataset show that the proposed method outperforms hNet, SwinConvUNet, UHRNet, and HiDNet in mean absolute error(MAE), root mean square error (RMSE), absolute relative error, and structural similarity index measure (SSIM). Using only one deformed fringe image, the proposed method achieves an RMSE of 0.548 mm and an SSIM of 0.9985, reducing RMSE by 65.2% and 59.6% relative to UHRNet and HiDNet, respectively. These results demonstrate the effectiveness of combining selective state space modeling with hierarchical window based attention for accurate single-shot FPP reconstruction.

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

#### 2026-10-26 - SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation

**Authors:** Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou
**Links:** [abs](https://arxiv.org/abs/2610.36312) - [pdf](https://arxiv.org/pdf/2610.36312)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation
- 作者：Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou
- 出版日期：2026-10-26T21:34:06Z
- 分类：Neural Scene Representations & Rendering（主分类）；3D Reconstruction & Multi-view Geometry（次分类）
- 链接：[摘要](https://arxiv.org/abs/2610.36312)｜[PDF](https://arxiv.org/pdf/2610.36312)

### 一句话总结
SG^2SLAM 针对单目户外导航，将流式空间几何与光线条件化的 3D Gaussian Splatting 内核结合，以块级度量先验替代逐帧跨维对应，联合优化空间几何与位姿，从而提升跟踪与建图的一致性。

### 研究问题
摘要指出，单目户外导航需要稳健的相机运动估计与稠密、可导航地图；3D Gaussian Splatting SLAM 通过显式可微参数化与闭式投影服务于该任务。但通常几何重建依赖 2D 像素与 3D 点的关联，模块化 SLAM 系统会把跟踪误差吸收进地图，导致级联退化。论文即针对这一误差传播与几何—位姿一致性问题展开。

### 核心思路/方法
- 提出 SG^2SLAM，将**流式空间几何**与**光线条件化的 3DGS 内核**耦合。
- **流式空间几何**：用块级度量先验替代逐帧跨维对应，由同一来源监督跟踪与建图。
- **光线条件化内核**：为每个基元扩展一个视角方向子空间，以感知单目相机视角。
- **联合优化**：对空间几何与位姿进行联合优化，以获得全局一致的地图与轨迹结果。
- 摘要称在 KITTI 与 Waymo Open 数据集上，该方法在单目户外导航任务中优于逐帧关联基线。

### 主要贡献
1. 提出 SG^2SLAM，面向单目户外导航的 3D Gaussian Splatting SLAM 框架。
2. 引入流式空间几何，以块级度量先验统一监督跟踪与建图，替代逐帧跨维对应。
3. 设计光线条件化 3DGS 内核，为基元增加视角方向子空间以感知单目相机视角。
4. 通过空间几何与位姿的联合优化提升地图与轨迹的全局一致性。
5. 在 KITTI 与 Waymo Open 上报告优于逐帧关联基线的结果；代码将在接收后公开。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性、内存占用与大规模场景可扩展性。
- 摘要未提供足够信息说明失败模式、对极端光照/动态物体/无纹理区域的鲁棒性。
- 摘要未提供足够信息说明与更多 SLAM 或 3DGS 基线方法的完整定量对比与消融细节。
- 摘要未提供足够信息说明块级度量先验的块大小选择、超参数敏感性及跨数据集泛化边界。

### 阅读优先级
**中**。理由：论文主题聚焦单目户外导航中的 3DGS SLAM 与几何—位姿一致性问题，问题定义清晰，且涉及 KITTI、Waymo Open 上的验证；但摘要仅给出方法要点与相对基线的结论，未提供足够的定量结果、消融与实时性信息。若读者关注 3DGS SLAM、单目户外建图或几何先验监督，可列为中高关注；若需要立即判断工程可用性，则需等待全文与代码。

</details>

<details>
<summary>Abstract</summary>

Monocular outdoor navigation requires robust camera motion estimation and a dense, navigable map, where 3D Gaussian Splatting SLAM serves this task through an explicit differentiable parameterization and closed-form projection. However, typically, the geometry is recovered by associating 2D pixels with 3D points, so a modular SLAM system absorbs tracking error into the map, leading to cascading degradation. To address these gaps, we present SG^2SLAM, which couples streaming spatial geometry with a ray-conditioned 3DGS kernel. Streaming spatial geometry replaces the per- frame cross-dimensional correspondence with a chunk-level metric prior that supervises tracking and mapping from one source. A ray-conditioned kernel extends each primitive with a viewing-direction subspace that senses the monocular camera viewpoints. The joint optimization over spatial geometry and poses ensures a globally consistent map and trajectory outcome. Experiments on the KITTI and Waymo Open datasets show that our SG^2SLAM surpasses the per-frame association baselines in the monocular outdoor navigation task. Code will be made publicly available upon acceptance.

</details>

#### 2026-10-26 - PrinGS: Privacy Preservation in Gaussian Splatting

**Authors:** Gaurav Behera, Abhinav Raundhal, Archisha Panda, Saumya Balina, Gargi Shroff, Ponnurangam Kumaraguru
**Links:** [abs](https://arxiv.org/abs/2610.36168) - [pdf](https://arxiv.org/pdf/2610.36168)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PrinGS: Privacy Preservation in Gaussian Splatting
- 作者：Gaurav Behera, Abhinav Raundhal, Archisha Panda, Saumya Balina, Gargi Shroff, Ponnurangam Kumaraguru
- 出版日期：2026-10-26T19:02:22Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.36168

### 一句话总结
该论文提出 PrinGS，通过表示层面的匿名化框架，在训练后的 3D Gaussian Splatting 表示中定位并匿名化敏感区域，并扩展出隐私保护训练策略，以避免敏感内容在优化过程中被嵌入表示。

### 研究问题
3D Gaussian Splatting 已成为高保真新视角合成与三维场景重建的常用表示，但其学习到的表示会编码人脸、车牌、文档和电脑屏幕等敏感视觉信息；当训练好的 splat 被共享或部署时，会带来隐私风险。论文关注的问题是：如何在 Gaussian Splatting 表示层面实现隐私保护，使敏感信息不出现在后续渲染的新视角中，同时保持整体场景几何与视觉保真度。摘要指出，这是一个尚未被充分探索的问题。

### 核心思路/方法
论文提出一个表示层面的匿名化框架，直接对已训练好的 splat 进行匿名化。给定一个训练好的 splat 和一张用户提供的、用于标识敏感内容的参考视图，方法在底层三维表示中定位对应区域并直接匿名化这些区域，从而确保敏感信息不会出现在后续渲染的新视角中，同时保留整体场景几何和视觉保真度。摘要称这种训练后匿名化可在不到 1 秒内完成。

此外，论文将该框架扩展为一种“隐私设计”训练策略，在优化过程中阻止敏感内容被嵌入表示，从而能够直接从训练图像生成隐私保护 splat。

### 主要贡献
1. 针对 Gaussian Splatting 中尚未被充分探索的隐私保护问题，提出表示层面的匿名化框架，可直接匿名化训练好的 splat。
2. 方法基于用户提供的参考视图定位敏感内容，并在底层三维表示中直接匿名化对应区域，使敏感信息在后续新视角渲染中缺失，同时保持场景几何与视觉保真度。
3. 实现快速训练后匿名化，摘要称耗时少于 1 秒。
4. 扩展出隐私设计训练策略，防止敏感内容在优化过程中被嵌入表示，从而直接从训练图像生成隐私保护 splat。
5. 摘要报告的量化结果包括：Face Similarity Measure（FSM）低至 9.79%，在保留 Face Detection Rate（FDR）为 39.47% 的情况下；敏感文本完全不可读，OCR Character Error Rate 为 1.00。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法对哪些场景类型或敏感内容类别存在失效情况，也未说明计算开销、内存需求、不同数据规模下的表现，以及隐私保护与视觉质量之间的详细权衡。摘要未提供足够信息以判断其泛化能力、对参考视图质量的依赖程度，或与现有隐私保护方法的全面对比。

### 阅读优先级
中。理由：该论文聚焦 3D Gaussian Splatting 的隐私保护这一较新且具有实际部署意义的问题，提出了训练后匿名化与隐私设计训练两种路径，并给出明确的量化隐私指标；但摘要未提供充分的实验设置、对比基线和局限性信息，适合作为了解该方向研究思路的入口，若需评估方法稳健性与通用性，还需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has rapidly become the preferred representation for high-fidelity novel view synthesis and 3D scene reconstruction. However, the learned representation encodes sensitive visual information including human faces, license plates, documents, and computer screens, raising significant privacy concerns when trained splats are shared or deployed. In this work, we address the underexplored problem of privacy preservation in Gaussian Splatting by proposing a representation-level anonymization framework that directly anonymizes a trained splat. Given a trained splat and a user-provided reference view identifying sensitive content, our method localizes the corresponding regions in the underlying 3D representation and directly anonymizes them, ensuring that the sensitive information is absent from all subsequently rendered novel views while preserving the overall scene geometry and visual fidelity. We achieve this post-training anonymization in less than 1 second. Furthermore, we extend our framework with a privacy-by-design training strategy that prevents sensitive content from being embedded into the representation during optimization, enabling the generation of privacy-preserving splats directly from training images. Our method achieves a remarkably low Face Similarity Measure (FSM) of 9.79% at a retained Face Detection Rate (FDR) of 39.47% and makes sensitive text completely unreadable with an OCR Character Error Rate of 1.00. Our work aims to serve as the primary stepping stone towards privacy-aware 3D representations and motivates further research along these directions.

</details>

#### 2026-10-26 - FL4N: Feed-forward Latent Model for 4D Novel View Synthesis

**Authors:** Eunbeen Hong, Hyeonseo Yu, Honggyu An, Jooho Son, Hyunah Ko, Soowon Son, Chaehyun Kim, Jahyeok Koo, Jisoo Kim, Junhwa Hur, Seungryong Kim
**Links:** [abs](https://arxiv.org/abs/2610.35854) - [pdf](https://arxiv.org/pdf/2610.35854)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FL4N: Feed-forward Latent Model for 4D Novel View Synthesis
- 作者：Eunbeen Hong, Hyeonseo Yu, Honggyu An, Jooho Son, Hyunah Ko, Soowon Son, Chaehyun Kim, Jahyeok Koo, Jisoo Kim, Junhwa Hur, Seungryong Kim
- 出版日期：2026-10-26T17:58:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.35854) / [PDF](https://arxiv.org/pdf/2610.35854)

### 一句话总结
FL4N 提出首个前馈式隐式 4D 新视角合成模型，将 4D 场景先验编码为跨空间与时间的统一隐式表示，避免显式 4D 基元带来的时序不一致与渲染伪影。

### 研究问题
4D 新视角合成需要同时推断三维结构与时间动态，即在任意视角与时间戳下渲染动态场景。现有单目前馈方法多依赖显式 4D 高斯表示，摘要指出其易出现时序不一致与严重渲染伪影。摘要未提供足够信息说明现有方法的具体失效场景或定量问题。

### 核心思路/方法
- 不依赖显式 4D 基元，而是将 4D 场景先验编码为跨空间与时间的统一隐式表示。
- 核心洞见：在预训练静态隐式先验之上，将时间动态学习为残差，从而在动态训练数据有限时仍能有效建模 4D。
- 引入轻量动态编码器，利用静态场景特征将物体运动与相机视差解耦。
- 仅以图像合成目标训练，摘要称其达到当前最优 4D 新视角合成质量并支持实时渲染。

### 主要贡献
- 提出首个前馈式隐式 4D 新视角合成模型 FL4N。
- 以统一隐式表示替代显式 4D 基元，针对时序不一致与渲染伪影问题。
- 提出“静态先验 + 动态残差”的学习范式，并设计轻量动态编码器解耦物体运动与相机视差。
- 仅用图像合成目标训练即可实时渲染，且隐式表示可泛化到真实视频并解耦视角与时间。
- 摘要未提供足够信息说明具体数据集、评价指标、消融实验与定量对比结果。

### 局限性
- 摘要未提供足够信息说明方法在不同动态复杂度、遮挡或长时序场景下的失效情况。
- 摘要未提供足够信息说明“动态训练数据有限”的具体规模及对性能的影响。
- 摘要未提供足够信息说明实时渲染的分辨率、帧率与硬件条件。
- 摘要未提供足够信息说明与显式 4D 高斯方法在计算开销与内存占用上的对比。

### 阅读优先级
中。理由：该论文面向 4D 动态新视角合成，提出前馈隐式表示与静态先验残差建模思路，并声称实时渲染与真实视频泛化，主题具有参考价值；但摘要未给出数据集、指标、消融与定量结果，需阅读全文才能判断其实际效果与可复现性。

</details>

<details>
<summary>Abstract</summary>

4D novel view synthesis (NVS) aims to render dynamic scenes across viewpoints and timestamps, which requires jointly inferring 3D structure and temporal dynamics. Existing monocular feed-forward methods often rely on explicit 4D Gaussian representations, which are prone to temporal inconsistency and severe rendering artifacts. We present FL4N, the first feed-forward latent 4D NVS model. Instead of relying on explicit 4D primitives, FL4N encodes a 4D scene prior into a unified latent representation across space and time. Our core insight is that learning temporal dynamics as residuals on top of a pretrained static latent prior enables effective 4D modeling with limited dynamic training data. To this end, we introduce a lightweight dynamic encoder that leverages static scene features to disentangle object motion from camera-induced parallax. Trained solely with an image synthesis objective, FL4N achieves state-of-the-art 4D NVS quality while rendering in real time. Its learned latent representation generalizes to real-world videos and disentangles viewpoint from time.

</details>

#### 2026-10-26 - VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion

**Authors:** Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang
**Links:** [abs](https://arxiv.org/abs/2610.35756) - [pdf](https://arxiv.org/pdf/2610.35756)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion
- 作者：Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang
- 出版日期：2026-10-26T17:03:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.35756) | [PDF](https://arxiv.org/pdf/2610.35756)

### 一句话总结
VidEdit3D 将文本引导的 3D 高斯场景编辑重新表述为基于相机轨迹的视频编辑任务，借助预训练视频扩散模型的时空先验提升多视角一致性与结构编辑灵活性，并通过轨迹引导渲染、流对齐视频编辑和区域选择性 3DGS 精化实现编辑传播与背景泄漏抑制。

### 研究问题
摘要指出，现有文本引导 3D 编辑方法（尤其基于 3D Gaussian Splatting 的方法）仍不如 2D 编辑工具灵活。核心矛盾在于：方法难以同时兼顾多视角一致性与允许结构修改；基于图像编辑器的方案在从异常角度观察对象时，也可能难以将预期编辑正确施加到对象上。论文旨在缓解这一权衡问题。

### 核心思路/方法
- 将静态 3D 场景中的相机运动类比为视频中的时间动态，把 3D 场景编辑转化为轨迹驱动的视频编辑任务，以利用预训练 Video Diffusion Models 的时空先验，促进跨视角的语义与结构一致性。
- **Trajectory-Guided Rendering (TGR)**：选择有信息量的关键帧，并构建与 VDM 输入要求对齐的平滑视频片段。
- **Flow-Aligned Video Editing (FAVE)**：一个免训练框架，包含 **Editing Consistency Guidance (ECG)** 机制，将编辑从锚点视角传播到上述视频片段。ECG 在共享潜在状态上对比源图像与编辑后图像条件，并通过调度式源图像增强，在保持原始场景上下文的同时加强对编辑参考的遵循。
- **Region-Selective 3DGS Refinement (RS-GS)**：将几何与外观更新严格限制在目标基元上，以减少背景属性泄漏。

### 主要贡献
- 提出 VidEdit3D 框架，将 3D 场景编辑重构为轨迹式视频编辑任务，并利用视频扩散模型的时空先验增强跨视角一致性。
- 提出 TGR，用于选择关键帧并构建符合 VDM 输入要求的平滑视频片段。
- 提出免训练的 FAVE 框架及 ECG 机制，实现从锚点视角到视频片段的编辑传播，并平衡编辑遵循与原始场景上下文保持。
- 提出 RS-GS，将 3DGS 的几何与外观更新限制在目标基元，减少背景属性泄漏。
- 摘要称实验显示该方法相比基线具有更强的指令对齐和更好的多视角一致性。

### 局限性
- 摘要仅给出方法概述与结论性表述，未提供具体实验设置、数据集、评价指标、定量结果或失败案例分析；这些信息摘要未提供足够信息。
- 摘要未说明方法对视频扩散模型质量的依赖程度、计算开销、编辑类型覆盖范围及极端视角下的具体表现；摘要未提供足够信息。
- 摘要未提供与基线方法的完整对比细节及消融实验信息；摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文面向文本引导 3DGS 编辑中“多视角一致性 vs. 结构修改灵活性”的关键权衡，提出轨迹式视频编辑重构及 TGR、FAVE/ECG、RS-GS 等完整组件，问题定义和方法组合具有较强针对性；若关注 3D 场景编辑、视频扩散先验迁移或 3DGS 精化，值得优先阅读。但摘要未给出定量实验细节，实际效果需进一步查阅全文验证。

</details>

<details>
<summary>Abstract</summary>

Recent advancements in text-guided 3D editing, particularly with 3D Gaussian Splatting (3DGS), have shown promise but still lag behind the flexibility of 2D editing tools. Existing methods face a critical trade-off between preserving multi-view consistency and allowing structural modifications. Image-based editors can also struggle to apply the intended edit to objects viewed from unusual angles. To address these limitations, we introduce VidEdit3D, a framework that reformulates 3D scene editing as a trajectory-based video editing task. By drawing a parallel between camera movement in static 3D scenes and temporal dynamics in video, we leverage the robust spatiotemporal priors of pre-trained Video Diffusion Models (VDMs) to encourage semantic and structural coherence across views. Specifically, we propose Trajectory-Guided Rendering (TGR) to select informative keyframes and construct smooth video clips aligned with VDM input requirements. To propagate edits from an anchor view to these clips, we develop Flow-Aligned Video Editing (FAVE), a training-free framework incorporating an Editing Consistency Guidance (ECG) mechanism. ECG contrasts source and edited image conditions at a shared latent state, using scheduled source-image amplification to strengthen adherence to the edited reference while maintaining original scene context. Finally, we introduce Region-Selective 3DGS Refinement (RS-GS) to strictly confine geometric and appearance updates to target primitives, reducing background attribute leakage. Experiments demonstrate stronger instruction alignment and better multi-view consistency than the baselines.

</details>

#### 2026-10-26 - Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies

**Authors:** Zuoxu Wang, Xiao Liang
**Links:** [abs](https://arxiv.org/abs/2610.35626) - [pdf](https://arxiv.org/pdf/2610.35626)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies
- 作者：Zuoxu Wang, Xiao Liang
- 出版日期：2026-10-26T15:40:03Z
- 分类：主分类为 Neural Scene Representations & Rendering；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.35626 ；PDF https://arxiv.org/pdf/2610.35626

### 一句话总结
论文提出一种基于 3D Gaussian Splatting 的数据生成流程，用机器人对齐位姿渲染腕部相机观测，并为 VLA 策略提供视觉-动作监督；同时加入指令条件化的到达验证器，用于电子废弃物拆解中的精确预接触到达。

### 研究问题
摘要指出，VLA 策略学习面临机器人数据采集效率瓶颈，尤其是需要精确末端执行器定位和相机-动作对齐的任务。电子废弃物拆解场景中，零件密集、外观相似且存在薄、反光或机械结构复杂的部件，完整数字孪生仿真难以获得准确的对象级网格和接触模型。论文聚焦预接触到达阶段，研究如何为腕部相机 VLA 策略适配提供机器人对齐的数据与监督。

### 核心思路/方法
- 使用 3D Gaussian Splatting（3DGS）重建真实工作空间。
- 从机器人对齐位姿渲染多样化的腕部相机观测。
- 将渲染观测与平滑、结构化的到达轨迹配对，形成机器人对齐的视觉-动作监督，用于 VLA 微调。
- 为 VLA 策略增加指令条件化的 reach verifier，用于估计目标接近程度，并在物理交互前提供可靠终止判断。
- 实验场景为主板拆解，目标是在仅使用腕部相机观测、不使用外部侧视相机的条件下实现精确 VLA 到达。

### 主要贡献
- 提出面向腕部相机 VLA 适配的 3DGS 数据生成管线，通过机器人对齐位姿渲染观测并与结构化到达轨迹配对。
- 引入指令条件化的 reach verifier，用于预接触阶段的接近估计与可靠终止。
- 在主主板拆解实验中报告：使用 π0.5 时，1,500 条生成轨迹在三个目标上达到 80.0% 精确到达成功率；相比 150 条遥操作演示的 58.7% 更高，且主动人类采集时间少于 10 分钟（上述数值均来自摘要）。
- 摘要称实验展示了仅依靠腕部相机观测即可实现精确 VLA 到达，无需外部侧视相机。

### 局限性
- 论文聚焦预接触到达，摘要未说明其是否覆盖接触后操作或完整拆解流程。
- 实验主要在主板拆解场景中验证，摘要未提供跨更多任务或对象的泛化结果。
- 摘要未提供 3DGS 重建质量、渲染与真实观测差异、验证器误判率等定量分析。
- 摘要未提供生成轨迹规模、遥操作演示数量与成功率之间更细粒度的消融实验信息。
- 摘要未提供计算成本、训练时间、硬件配置和安全性评估细节。
- 摘要未说明 1,500 条生成轨迹与 150 条遥操作演示在数据采集成本之外的可比条件细节。
- 其他未在摘要中出现的信息：摘要未提供足够信息。

### 阅读优先级
中。理由：论文主题涉及 3DGS 用于机器人数据生成、腕部相机 VLA 与预接触精确到达，和神经场景表示及具身机器人应用均相关；摘要给出了明确的问题动机和量化结果。但若关注完整拆解操作、广泛泛化或详细实验设计，摘要信息不足以判断，需要阅读全文进一步确认。

</details>

<details>
<summary>Abstract</summary>

Efficient robotic data collection remains a major bottleneck for vision-language-action (VLA) policy learning, especially for tasks requiring accurate end-effector positioning and camera-action alignment. This challenge is particularly severe in electronic-waste disassembly, where robots operate in cluttered assemblies of densely packed, visually similar components. Full digital-twin simulation is difficult because many parts are thin, reflective, or mechanically complex, making accurate object-level meshes and contact models difficult to obtain. In this work, we focus on pre-contact reaching and propose a 3D Gaussian Splatting (3DGS)-based data generation pipeline for wrist-camera VLA adaptation. Our method reconstructs the real workspace with 3DGS and renders diverse wrist-camera observations from robot-aligned poses. These observations are paired with smooth, structured reaching trajectories to provide robot-aligned visual-action supervision for VLA fine-tuning. We further augment the VLA policy with an instruction-conditioned reach verifier that estimates target proximity and provides reliable termination before physical interaction. Experiments in motherboard disassembly demonstrate precise VLA-based reaching using wrist-camera observations alone, without an external side-view camera. With $π$0.5, 1,500 generated trajectories achieve 80.0\% precise-reaching success across three targets, compared with 58.7\% using 150 teleoperated demonstrations, while requiring less than 10 minutes of active human capture. Project website: https://001-wang.github.io/PrecisionReach-GS/

</details>

#### 2026-10-26 - Complexity-guided Regularization for Generalizable Human Gaussian Splatting

**Authors:** Gun Ryu, Gi-Mun Um, Won-Sik Cheong, Wonjun Kim
**Links:** [abs](https://arxiv.org/abs/2610.35152) - [pdf](https://arxiv.org/pdf/2610.35152)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Complexity-guided Regularization for Generalizable Human Gaussian Splatting
- 作者：Gun Ryu, Gi-Mun Um, Won-Sik Cheong, Wonjun Kim
- 出版日期：2026-10-26T10:18:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.35152 ；PDF https://arxiv.org/pdf/2610.35152 ；代码与模型 https://github.com/DCVL-3D/CGR-GS_release

### 一句话总结
论文提出一种由复杂度引导的正则化方案，利用基于局部熵的复杂度先验约束高斯放置并引导局部块采样，以改善可泛化人体高斯泼溅在复杂几何与纹理区域的细节重建。

### 研究问题
现有可泛化人体高斯泼溅方法在多视角图像合成未见人体新视角方面已有进展，但仍难以表示人体对象的细粒度细节，而这些细节本身具有较高的几何与纹理复杂度。摘要指出，原因在于以往方法未对高斯放置的密集程度施加约束，导致复杂区域渲染结果常出现模糊。

### 核心思路/方法
论文提出复杂度引导的正则化方案，核心是使用由穿衣人体几何与纹理特征的局部熵计算得到的复杂度先验。该先验用于两方面：一是防止高斯在复杂区域被粗放放置，从而促进对精细结构的忠实重建；二是依据该复杂度先验，主要从复杂区域采样局部块，使模型能够被局部细节充分监督。

### 主要贡献
- 提出复杂度引导的正则化方案，用于可泛化人体高斯泼溅。
- 利用穿衣人体几何与纹理特征的局部熵构造复杂度先验，约束高斯在复杂区域的放置密度，缓解复杂区域渲染模糊。
- 依据复杂度先验从复杂区域优先采样局部块，增强对局部细节的监督。
- 摘要称在基准数据集上取得最先进性能，同时保持可泛化人体高斯泼溅的实时推理速度。
- 公开代码与模型。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、适用范围限制、计算开销细节、对复杂度先验超参数的敏感性，以及在不同数据集或极端人体姿态/遮挡条件下的表现。摘要仅概括性报告基准数据集上的最先进性能和实时推理速度，未给出实验设置、对比方法、指标数值和消融细节。

### 阅读优先级
中。理由：该论文聚焦可泛化人体高斯泼溅中的细节重建与高斯放置约束问题，问题定义清晰，方法思路简洁，且摘要声称保持实时推理并公开代码，适合关注人体新视角合成与高斯泼溅正则化方向的研究者阅读；但摘要未提供定量实验细节与局限性信息，是否构成重要突破需进一步阅读全文验证。

</details>

<details>
<summary>Abstract</summary>

Recent studies on generalizable human Gaussian splatting have achieved the notable progress in synthesizing novel views of unseen human subjects from multi-view images. Despite this progress, existing methods still struggle to represent fine-grained details of human subjects, which inherently involve high geometric and textural complexity. This is because previous methods do not impose a constraint on how densely Gaussians are placed, which often leads to blurry rendering results in complex regions. To address this problem, we propose a complexity-guided regularization scheme. The key idea is to leverage a complexity prior computed via the local entropy in geometric and textural characteristics of a clothed human. This effectively prevents Gaussians from being coarsely placed in complex regions, which facilitates the faithful reconstruction of intricate structures. Furthermore, we sample local patches predominantly from complex regions according to this complexity prior, which allows the model to be sufficiently supervised by local details. Experimental results on benchmark datasets demonstrate that our method delivers state-of-the-art performance while maintaining the real-time inference speed in generalizable human Gaussian splatting. The code and model are publicly available at https://github.com/DCVL-3D/CGR-GS_release.

</details>

#### 2026-10-26 - SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments

**Authors:** Luke Hollis, Tianxing Fan, Heng Yang
**Links:** [abs](https://arxiv.org/abs/2610.34745) - [pdf](https://arxiv.org/pdf/2610.34745)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** photogrammetry, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments
- 作者：Luke Hollis, Tianxing Fan, Heng Yang
- 出版日期：2026-10-26T02:45:35Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.34745) / [PDF](https://arxiv.org/pdf/2610.34745)

### 一句话总结
SceneAgent 是一个智能体流水线，通过基于模拟器的视觉检查与修复，将多种 3D/4D 视觉采集转换为可交互的仿真环境，并支持策略学习。

### 研究问题
视觉采集能提供详细的场景外观，但将其转换为交互式仿真环境时，需要完成物体重建、物理建模以及中间错误的修正；摘要指出这些步骤存在中间错误，SceneAgent 要解决的问题就是如何协调并纠错，完成从采集到仿真环境的转换。

### 核心思路/方法
- 构建一个 agentic pipeline（智能体流水线），通过基于模拟器的视觉检查与修复来协调各步骤。
- 可处理的输入包括：3D Gaussian Splatting (3DGS)、摄影测量、LiDAR 采集、AI 生成的 3DGS 场景，以及动态场景的 4D 视频。
- 流水线组合了物体分割、物理参数估计、部件分解、铰接建模与可变形仿真。
- 为支持策略学习，生成多样化的物体变体（“digital sisters”）和脚本化的演示数据。

### 主要贡献
- 提出 SceneAgent 智能体流水线，将 3D/4D 采集转换为仿真环境，并通过模拟器视觉检查与修复中间错误。
- 在 GraspClutter6D 的杂乱箱体场景中，对于每个具备可评分输出的编码智能体，SceneAgent 均提升了 1 cm 阈值下的 F1；无论是否使用其 skills 均如此。
- 其重建结果优于 SimFoundry：所有智能体配置的 F1 均超过 SimFoundry，最佳为 60.75% 对 6.9%。
- 在 4DCodeBench 的三个动态场景上，将 Gemini 4 Argon 的平均动态 IoU 从 0.86% 提升到 99.09%。
- 进一步展示了多样化的模拟交互，以及初步的策略向真实机器人迁移。

### 局限性
- 摘要未提供足够信息说明方法在各步骤中的具体技术细节与失败条件。
- 摘要未提供足够信息说明真实机器人策略迁移的量化结果、实验规模与评测设置。
- 摘要未提供足够信息说明计算开销、运行时间或对输入采集质量的敏感性。
- 摘要未提供足够信息说明在 GraspClutter6D 与 4DCodeBench 之外的泛化能力。

### 阅读优先级
高。理由：该工作直接面向从真实/生成 3D 与 4D 采集到可交互仿真环境的自动化转换，涉及场景表示、物理建模与机器人策略学习，摘要给出了明确的量化对比（F1 与动态 IoU 的显著提升）和真实机器人迁移的初步验证，与主次分类均高度相关。

</details>

<details>
<summary>Abstract</summary>

Visual captures provide detailed scene appearance, but converting them into interactive simulation environments requires object reconstruction, physical modeling, and correction of intermediate errors. We present SceneAgent, an agentic pipeline that coordinates these steps through simulator-based visual inspection and repair. The pipeline processes 3D Gaussian Splatting (3DGS), photogrammetry, LiDAR captures, AI-generated 3DGS scenes, and 4D videos of dynamic scenes, and combines object segmentation, physical parameter estimation, part decomposition, articulation, and deformable simulation. To support policy learning, SceneAgent generates diverse object variants ("digital sisters") and scripted demonstrations. On a cluttered bin scene from GraspClutter6D, SceneAgent raises F1 at 1 cm for every coding agent with scorable outputs both with and without its skills, and its reconstructions are better than SimFoundry: all agent configurations exceed SimFoundry's F1 score, with a best of 60.75% versus 6.9%. On three dynamic scenes from 4DCodeBench, SceneAgent raises the mean dynamic IoU of Gemini 4 Argon from 0.86% to 99.09%. We further demonstrate diverse simulated interactions and preliminary policy transfer to a real robot.

</details>

#### 2026-10-25 - RIDE-Splat: Reflection Removal for In-the-Wild Driving Environments

**Authors:** Kevin David Hayes, Alex Hanson, Allen Tu, Pranav Asthana, Matthias Zwicker, Tom Goldstein
**Links:** [abs](https://arxiv.org/abs/2610.34632) - [pdf](https://arxiv.org/pdf/2610.34632)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RIDE-Splat: Reflection Removal for In-the-Wild Driving Environments
- 作者：Kevin David Hayes, Alex Hanson, Allen Tu, Pranav Asthana, Matthias Zwicker, Tom Goldstein
- 出版日期：2026-10-25T23:11:47Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.34632) / [PDF](https://arxiv.org/pdf/2610.34632)

### 一句话总结
RIDE-Splat 提出一种从带位姿的真实驾驶视频中去除挡风玻璃反射、重建无反射 3D 场景的两阶段 3D Gaussian Splatting 流程，无需干净图像、反射掩码或预训练网络。

### 研究问题
通过挡风玻璃拍摄的驾驶视频会违反 3D Gaussian Splatting（3DGS）所假设的世界空间一致性：道路场景呈现视差，而车内反射附着于相机。这导致标准 3DGS 将反射内容嵌入重建场景中。论文要解决的是：在没有干净图像、反射掩码和预训练网络条件下，如何从带位姿驾驶视频实现无反射的三维重建。

### 核心思路/方法
- 将世界一致的挡风玻璃透射分配给 3DGS 场景，将主要相机附着反射建模为一张共享的有符号 RGB 图像。
- 采用两阶段训练：
  1. 第一阶段学习 3D 几何与有符号反射图像，该图像同时表示附加辐射和透射衰减；
  2. 第二阶段使用去反射后的训练图像拟合干净的 3DGS 模型。
- 推理时丢弃反射图像，保持标准 3DGS 渲染路径。

### 主要贡献
- 提出 RIDE-Splat 流程，实现无需干净图像、反射掩码或预训练网络的驾驶视频无反射三维重建。
- 将反射建模为相机附着的共享有符号 RGB 图像，并使其与 3DGS 场景中的世界一致透射分离。
- 提出 RIDE-Splat Dataset，摘要称其为首个用于驾驶视频去反射三维重建的基准，包含真实驾驶场景、训练视图中的物理挡风玻璃反射，以及单独采集的无反射评估图像。
- 在 RIDE-Splat Dataset、XLD 和 Wayve 上，摘要称 RIDE-Splat 在全部九项聚合指标上优于 3DGS、DC-Gaussian 和 RobustSplat，PSNR 最高提升 3.59 dB，LPIPS 最高降低 0.0876；在 42 项逐场景比较中取得 38 项最高指标。

### 局限性
摘要未提供足够信息。摘要未说明方法对反射类型、相机运动、训练数据规模或计算成本的适用边界与失效情形。

### 阅读优先级
高。理由：该论文直接针对 3DGS 在真实驾驶视频中的世界空间一致性破坏问题，提出无需额外监督输入的反射分离与两阶段重建方案，并给出新基准与多数据集定量对比；对神经渲染、自动驾驶场景重建和反射去除方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Driving video captured through a windshield violates the world-space consistency assumed by 3D Gaussian Splatting (3DGS): the road scene exhibits parallax while cabin reflections remain attached to the camera, causing standard 3DGS to embed reflected content into the reconstructed scene. We introduce RIDE-Splat, a pipeline for reflection-free 3D reconstruction from posed driving video without clean images, reflection masks, or pretrained networks. RIDE-Splat assigns world-consistent transmission through the windshield to a 3DGS scene and the dominant camera-attached reflection to one shared, signed RGB image. It builds the clean reconstruction in two passes. First, it learns the 3D geometry and the signed reflection image, representing both added radiance and transmission attenuation. Then, it uses the reflection-removed training images to fit a clean 3DGS model. At inference, the reflection image is discarded, preserving the standard 3DGS rendering path. We also introduce the RIDE-Splat Dataset, the first 3D reconstruction benchmark for reflection removal from driving video -- with real driving scenes, physical windshield reflections in training views, and separately captured non-reflective evaluation images. Across the RIDE-Splat Dataset, XLD, and Wayve, RIDE-Splat outperforms 3DGS, DC-Gaussian, and RobustSplat on all nine aggregate metrics, improving PSNR by up to 3.59 dB and reducing LPIPS by up to 0.0876. We achieve the highest metrics in 38 out of 42 per-scene comparisons and removes windshield reflections that remain visible in the baselines while preserving the transmitted scene.

</details>

#### 2026-10-25 - Birth-Death Structural Learning for 3D Gaussian Splatting

**Authors:** Quan Tran Hong, Long Nguyen-Chi, Binh T. Nguyen
**Links:** [abs](https://arxiv.org/abs/2610.34344) - [pdf](https://arxiv.org/pdf/2610.34344)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Birth-Death Structural Learning for 3D Gaussian Splatting
- 作者：Quan Tran Hong, Long Nguyen-Chi, Binh T. Nguyen
- 出版日期：2026-10-25T14:56:56Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.34344)｜[PDF](https://arxiv.org/pdf/2610.34344)

### 一句话总结
论文提出一种基于重建损失一阶变分的“出生—死亡”结构控制分数，用来替代 3DGS 自适应密度控制中的代理启发式信号，指导新高斯点的分配与低价值基元的剪枝。

### 研究问题
3DGS 的质量—效率权衡高度依赖自适应密度控制，但现有克隆、分裂、剪枝规则使用的代理信号（位置梯度、不透明度、图像空间误差）并不能直接回答结构控制的核心问题：应在何处新增高斯点以降低多视角重建损失，以及哪些现有基元可以以最小惩罚被剪除。摘要指出，这些代理信号在实践中有效，但并非直接针对重建损失的结构决策依据。

### 核心思路/方法
论文提出用于 3DGS 的一阶变分出生—死亡控制（first-variation birth-death control）。在每次结构更新时，冻结当前高斯种群，为每个基元附加辅助“质量坐标”，并对多视角损失关于这些坐标求导。作者说明该分数是 Splat Regression Model 一阶变分的坐标，从而为出生—死亡移动提供严格的局部下降替代量：高分高斯被选为出生位置，低分且低不透明度的高斯被选为移除对象。摘要还提到，将该分数集成到 3DGS-MCMC 中。

### 主要贡献
- 提出以重建损失的一阶变分分数替代 3DGS 密度控制中的代理启发式信号，用于出生与死亡的结构决策。
- 给出理论说明：该分数是 Splat Regression Model 一阶变分的坐标，可作为出生—死亡移动的局部下降替代量。
- 摘要称在标准 3DGS 基准上，将该分数集成到 3DGS-MCMC 后取得 state-of-the-art 重建质量，并在紧高斯预算下带来最显著增益。
- 摘要称其结果为“基于梯度的变分度量可作为 3DGS 中代理启发式的原则性替代”提供了有力证据。

### 局限性
摘要未提供足够信息说明计算开销、辅助质量坐标的具体实现细节、实验基准与对比方法的完整列表、紧预算的具体设定、消融实验规模，以及方法在动态场景或非标准场景中的适用性。摘要未提供足够信息。

### 阅读优先级
中。理由：论文主题直接针对 3DGS 自适应密度控制的关键结构问题，且摘要声称在标准基准上取得 state-of-the-art 并在紧预算下增益最大，具有较高相关性；但仅凭摘要无法核验实验细节、计算成本与泛化性，需阅读全文后再判断其实际影响。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become a standard representation for real-time novel-view synthesis. Yet, its quality-efficiency trade-off still relies heavily on adaptive density control. Existing cloning, splitting, and pruning rules use proxy signals, such as position gradients, opacity, and image-space error. Although effective in practice, these signals do not directly answer the structural question behind density control: where should new Gaussians be allocated to reduce the multi-view reconstruction loss, and which existing primitives can be pruned with minimal penalty. To address this, we propose first-variation birth-death control for 3DGS, a principled approach that replaces heuristic structural decisions with a variational score derived from the reconstruction loss. At each structural update, we freeze the current Gaussian population, attach auxiliary mass coordinates to each primitive, and differentiate the multiview loss with respect to these coordinates. We demonstrate that this score is a coordinate of the first variation of the Splat Regression Model, giving a rigorous local descent surrogate for birth-death moves: high-score Gaussians are selected as birth sites, while low-score, low-opacity Gaussians are selected for removal. Across standard 3DGS benchmarks, integrating this score into 3DGS-MCMC yields state-of-the-art reconstruction quality and outperforms existing methods, delivering the most significant gains under tight Gaussian budgets. Ultimately, our work provides compelling evidence that gradient-based variational metrics offer a principled alternative to proxy heuristics in 3DGS.

</details>

#### 2026-10-25 - RacerGS: Residual-Autoregressive Context for 3D Gaussian Splatting Compression

**Authors:** Wenqing Wang, Huimin Zeng, Yun Fu
**Links:** [abs](https://arxiv.org/abs/2610.34263) - [pdf](https://arxiv.org/pdf/2610.34263)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RacerGS: Residual-Autoregressive Context for 3D Gaussian Splatting Compression
- 作者：Wenqing Wang, Huimin Zeng, Yun Fu
- 出版日期：2026-10-25T12:49:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.34263) / [PDF](https://arxiv.org/pdf/2610.34263)

### 一句话总结
RacerGS 是一种面向 3D Gaussian Splatting 的压缩框架，通过哈希投影、FiLM 调制的自回归 GRU 上下文模型及锚点属性残差熵编码，在保持渲染质量的同时显著降低存储规模。

### 研究问题
3D Gaussian Splatting 能实现快速、高质量的新视角渲染，但其参数量大，成为存储和传输的瓶颈。论文关注如何在尽量保持保真度的前提下，显著压缩 3DGS 的存储规模。

### 核心思路/方法
- 设计哈希投影模型，将锚点哈希编码投影为紧凑的上下文特征，以获得紧凑且空间连贯的特征表示。
- 引入 FiLM 调制的自回归 GRU 上下文模型，利用锚点特征组之间的因果依赖，并用循环隐藏状态细化熵模型参数，以提升比特率效率。
- 对量化后的锚点-属性残差，相对于其上下文预测均值进行自适应熵编码，利用空间一致性降低符号熵。

### 主要贡献
- 提出 RacerGS 紧凑 3DGS 压缩框架，在显著降低存储尺寸的同时保持保真度并完成场景重建。
- 设计哈希投影模型生成紧凑、空间连贯的上下文特征。
- 引入 FiLM 调制的自回归 GRU 上下文模型，利用因果依赖和循环隐藏状态改进熵建模。
- 对量化锚点-属性残差进行自适应熵编码，利用空间一致性降低符号熵。
- 摘要称 RacerGS 相对原始 3DGS 实现超过 150 倍压缩，相对 Scaffold-GS 实现 28 倍压缩，并提供可比渲染质量；在五个数据集上的实验表明其在存储缩减和率失真性能上优于先前 3DGS 压缩方法。

### 局限性
- 摘要未提供足够信息说明计算复杂度、编码/解码耗时或内存开销。
- 摘要未提供足够信息说明各模块的消融实验细节与各自增益。
- 摘要未提供足够信息说明五个数据集的具体名称、场景类型及评测协议。
- 摘要未提供足够信息说明失败案例、极端场景表现或对不同 3DGS 变体的泛化性。
- 摘要未提供足够信息说明与更多基线方法的逐项定量对比。

### 阅读优先级
中。理由：该论文聚焦 3DGS 存储与传输瓶颈，压缩幅度声称显著，且方法组合具有明确的技术针对性；但当前仅有摘要信息，缺少实验细节、复杂度与消融结果，适合作为 3DGS 压缩方向的候选跟踪论文，待全文可获取后再决定是否深入研读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as a promising approach for fast, high-quality novel-view rendering. However, its large parameter size remains a bottleneck for storage and transmission. We propose RacerGS, a compact 3DGS compression framework that achieves scene reconstruction at significantly reduced storage sizes with preserved fidelity. To obtain compact and spatially coherent features, we design a hash projection model that projects the anchor hash encodings into compact context features. Additionally, we introduce a FiLM-modulated autoregressive GRU context model that utilizes causal dependencies among anchor feature groups and uses recurrent hidden states to refine entropy-model parameters, improving bitrate efficiency. Furthermore, we adaptively entropy-code quantized anchor-attribute residuals relative to their context-predicted means, leveraging spatial consistency to reduce symbol entropy. Overall, RacerGS achieves more than 150x compression over vanilla 3DGS and 28x over Scaffold-GS, while providing comparable rendering quality. Extensive experiments across five datasets demonstrate that RacerGS outperforms prior 3DGS compression methods in both storage reduction and rate-distortion performance.

</details>

#### 2026-10-25 - ParetoGS: High-Quality Continuous-Budget 3D Gaussian Splatting with Sparse Adapted Anchors

**Authors:** Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu
**Links:** [abs](https://arxiv.org/abs/2610.34235) - [pdf](https://arxiv.org/pdf/2610.34235)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ParetoGS: High-Quality Continuous-Budget 3D Gaussian Splatting with Sparse Adapted Anchors
- 作者：Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu
- 出版日期：2026-10-25T12:05:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.34235) / [PDF](https://arxiv.org/pdf/2610.34235)

### 一句话总结
ParetoGS 通过少量“预算锚点”和残差图谱，把高预算 3D Gaussian Splatting 模型解码为连续预算表示，在减少高斯数量的同时尽量保持渲染质量。

### 研究问题
可扩展 3D Gaussian Splatting 希望用同一场景表示服务不同的 Gaussian 数量预算，但其质量—预算曲线可能落后于针对每个预算单独优化的模型。摘要指出，减少 Gaussian 数量会同时改变被选成员及其承担的重建任务，而直接从高预算模型继承的参数可能不适合低预算表示。

### 核心思路/方法
- 用一小组经过适配的预算锚点描述成员变化与参数演化，并在解码时生成中间预算，而不必对每个请求数量单独优化。
- 交替进行剪枝与固定成员适配，构建具有持久身份标识的嵌套锚点。
- 将各锚点相对完整模型的参数变化编码为紧凑的残差图谱。
- 解码时对共享成员状态进行插值，并逐步引入新成员的渲染贡献，从而把稀疏锚点连接为连续预算表示。

### 主要贡献
- 提出面向连续预算的 ParetoGS 框架，以稀疏适配锚点和残差图谱支持中间预算解码。
- 在 13 个场景上，于各方法自身完整模型 10% 的预算处，以更少 Gaussian 取得更好的平均 PSNR、SSIM 和 LPIPS。
- 从共享完整模型出发，在训练预算 1%、5%、10% 上优于 FlexGS-imp，在 1% 和 0.1% 预算上优于 NanoGS-imp。
- 在 Garden 场景上，非锚点质量在较高保留比例下接近独立优化 GNS 模型的经验参考，并在部分更低预算点超过该参考。
- 编码将 13 个场景的平均额外状态从 390.0 MB 降至 85.7 MB，平均 PSNR 变化为 0.01 dB。

### 局限性
摘要未提供足够信息说明计算开销、训练时间、内存峰值、更多场景或数据集上的泛化表现，也未给出失败案例或方法适用边界。

### 阅读优先级
高。理由：该论文直接针对连续预算 3D Gaussian Splatting 的质量与状态开销问题，摘要给出了多场景定量结果、与近期方法的比较以及明确的压缩收益，适合关注高效神经场景表示与渲染的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Scalable 3D Gaussian Splatting allows one scene representation to serve different Gaussian-count budgets, yet its quality-budget curve may lag behind models optimized separately for each budget. Reducing the number of Gaussians changes both the selected members and the reconstruction tasks carried by the survivors; parameters inherited from a high-budget model may fit a low-budget representation poorly. We propose ParetoGS, which describes member changes and parameter evolution with a small set of adapted budget anchors and decodes intermediate budgets without separate optimization at every requested count. ParetoGS alternates pruning and fixed-member adaptation to build nested anchors with persistent identities, and encodes their parameter changes relative to the full model in a compact residual atlas. At decoding, it interpolates the states of shared members and gradually introduces the rendering contributions of new members, connecting sparse anchors into a continuous-budget representation. Across 13 scenes, ParetoGS attains better average PSNR, SSIM, and LPIPS with fewer Gaussians than the compared prefix methods at 10% of each method's own full model. From a shared full model, it also outperforms FlexGS-imp at its trained 1%, 5%, and 10% budgets and NanoGS-imp at the 1% and 0.1% budgets. On Garden, its non-anchor quality approaches an empirical reference from independently optimized GNS models at higher retention ratios and exceeds it at some lower-budget points. Across 13 scenes, encoding reduces mean additional state from 390.0 to 85.7 MB with an average PSNR change of 0.01 dB. Project page: https://xiaobin2001.github.io/ParetoGS-Web/

</details>

#### 2026-10-25 - BoundedGS: Memory-Efficient High-Resolution Training for 3D Gaussian Splatting

**Authors:** Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu
**Links:** [abs](https://arxiv.org/abs/2610.34233) - [pdf](https://arxiv.org/pdf/2610.34233)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BoundedGS: Memory-Efficient High-Resolution Training for 3D Gaussian Splatting
- 作者：Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu
- 出版日期：2026-10-25T12:00:20Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.34233) / [PDF](https://arxiv.org/pdf/2610.34233) / [项目页](https://xiaobin2001.github.io/BoundedGS-Web/)

### 一句话总结
针对高分辨率 3D Gaussian Splatting 训练中光栅化缓存随像素与高斯-瓦片相交数增长而导致峰值显存膨胀的问题，BoundedGS 通过分离反向传播、限制局部光栅化工作集并压缩梯度与投影存储，在保持重建质量的同时显著降低显存占用。

### 研究问题
高分辨率 3D Gaussian Splatting 训练会提高像素与 Gaussian-tile 的相交计数，使光栅化缓存扩张，并与投影和梯度状态在峰值内存处共存，形成显存压力。论文关注的是：如何在完整视图更新语义下，控制高分辨率训练和渲染过程中的峰值工作集，同时不显著损害重建质量与训练效率。

### 核心思路/方法
- 利用“完整视图更新”的性质：梯度可跨视图聚合，因此每个区域在前向与反向中的缓存可在其贡献被收集后释放。
- 将光栅化与投影的反向传播过程分离，并根据实测负载限制活跃的局部光栅化工作集。
- 采用候选索引的投影表示与紧凑梯度存储，处理该改变所暴露的视图级峰值。
- 在渲染之外，使用 CPU 辅助的结构重建与有界图像供给来管理资源。
- 摘要给出的机制描述集中在显存边界控制、缓存释放与状态压缩；具体实现细节与完整算法流程需参见原文。

### 主要贡献
- 提出 BoundedGS，面向高分辨率 3D Gaussian Splatting 训练的内存高效方法。
- 在约 6M Gaussian 的固定数量下进行分辨率扫描，测得渲染工作集在 1K 到 16K 范围内保持在 1.073–1.077 GiB。
- 在 11K 分辨率下，预热通过耗时 19.79 秒，对比全帧执行的 21.76 秒。
- 在五个原生 5K 室外场景上，完整训练将平均渲染工作集从 9.97 GiB 降至 1.76 GiB（降低 82.3%），保持相近的重建质量，并将训练时间从 36.7 分钟缩短至 33.9 分钟。
- 摘要报告了显存、时间与重建质量方面的结果；更细粒度的消融、不同场景逐项指标与失败案例分析：摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法在非室外场景、不同高斯数量或更高分辨率下的泛化表现。
- 摘要未提供足够信息说明“相近重建质量”的具体量化指标、评价协议与统计显著性。
- 摘要未提供足够信息说明 CPU 辅助结构重建与有界图像供给的开销、硬件依赖及对训练稳定性的影响。
- 摘要未提供足够信息说明与其它显存优化方法的直接对比。
- 摘要未提供足够信息说明代码、数据与复现实验的完整细节。

### 阅读优先级
高。理由：该论文直接针对高分辨率 3D Gaussian Splatting 训练的显存瓶颈，摘要给出了明确的工作集边界、时间与质量保持结果，且涉及反向传播分离、缓存释放与状态压缩等可复用的系统级思路；对关注三维重建训练效率与显存优化的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

High-resolution 3D Gaussian Splatting training increases pixel and Gaussian-tile intersection counts, expanding rasterization caches that coexist with projection and gradient state at peak memory. A complete-view update aggregates gradients across the view; each region's forward and backward caches can be released after its contribution is collected. BoundedGS separates rasterization and projection backward passes and bounds the active local rasterization working set according to its measured load. Candidate-indexed projection and compact gradient storage address the view-level peaks exposed by this change, while CPU-assisted structure rebuilding and bounded image supply manage resources outside rendering. In a resolution sweep at a fixed count of about 6M Gaussians, the measured rendering working set stays within 1.073-1.077 GiB from 1K to 16K; at 11K, a warm pass takes 19.79 seconds versus 21.76 for full-frame execution. Across five native 5K outdoor scenes, full training reduces the mean rendering working set from 9.97 to 1.76 GiB (82.3%), retains similar reconstruction quality, and shortens training time from 36.7 to 33.9 minutes. Project page: https://xiaobin2001.github.io/BoundedGS-Web/

</details>

#### 2026-10-24 - RelateGS: Reliable Semantic and Relational Evidence for 3D Scene Understanding with Gaussian Splatting

**Authors:** Seongjun Choi, Sangyoun Lee
**Links:** [abs](https://arxiv.org/abs/2610.33868) - [pdf](https://arxiv.org/pdf/2610.33868)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RelateGS: Reliable Semantic and Relational Evidence for 3D Scene Understanding with Gaussian Splatting
- 作者：Seongjun Choi, Sangyoun Lee
- 出版日期：2026-10-24T19:20:57Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.33868) / [PDF](https://arxiv.org/pdf/2610.33868)

### 一句话总结
RelateGS 提出一种结构化的语言感知 3D 高斯表示，通过筛选不可靠语义观测并补全观测不足的物体关系证据，提升三维视觉定位中的目标消歧能力。

### 研究问题
语言感知的 3D 高斯泼溅已能将语义与关系线索融入重建场景，但关系感知的定位不仅依赖信息表示，还取决于场景侧证据是否可靠和充分。多视角语义聚合可能引入弱观测；同时，现有相机轨迹下物体关系可能观测不足，导致目标消歧时证据模糊。论文针对这两个证据可靠性问题展开研究。

### 核心思路/方法
- 在语义特征提升过程中抑制不可靠观测。
- 将多视角物体观测整合为持久的三维图结构。
- 利用该图识别观测不足的物体关系，并指导对已有信息帧进行定向重新查询，以补全关系证据。
- 面向三维视觉定位，选择性精炼语义与关系证据。

### 主要贡献
- 提出 RelateGS，一种结构化的语言感知高斯表示，用于选择性精炼三维视觉定位所需的语义和关系证据。
- 针对语义提升中的不可靠观测进行抑制，并通过持久三维图整合多视角物体观测。
- 通过三维图识别观测不足的对象关系，并引导对现有帧的定向重查询以补充证据。
- 在 Sr3D+ 与 Nr3D 上报告了有竞争力的三维定位性能；按摘要，在 Acc@0.25 上分别较此前最佳提升 7.9 和 1.7 个百分点。

### 局限性
摘要未提供足够信息说明方法的具体失效条件、计算开销、对相机轨迹质量的敏感程度，以及在不同数据集或场景类型上的泛化边界。摘要亦未提供消融实验细节与错误案例分析。

### 阅读优先级
高。理由：该工作直接针对语言感知 3DGS 中关系证据可靠性与观测不足问题，问题定义清晰，且摘要报告了在 Sr3D+ 和 Nr3D 上的明确性能提升；同时涉及具身/机器人/AR 应用方向，具有较高的相关性与跟踪价值。

</details>

<details>
<summary>Abstract</summary>

Language-aware 3D Gaussian Splatting (3DGS) has advanced language-driven 3D scene understanding by incorporating semantic and relational cues into reconstructed scenes. However, relation-aware grounding depends not only on representing such information, but also on whether the underlying scene-side evidence is reliable and sufficient. Multi-view semantic aggregation can incorporate weak observations, while object relations can remain under-observed along the available camera trajectory, leading to ambiguous evidence for target disambiguation. We present RelateGS, a structured language-aware Gaussian representation that selectively refines semantic and relational evidence for 3D visual grounding. RelateGS suppresses unreliable observations during semantic feature uplifting and consolidates multi-view object observations into a persistent 3D graph. The graph further identifies under-observed object relations and guides targeted re-querying of informative existing frames to complement their evidence. Experiments on Sr3D+ and Nr3D demonstrate competitive 3D grounding performance, improving the previous best by 7.9 and 1.7 percentage points at Acc@0.25, respectively.

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

#### 2026-10-26 - Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data

**Authors:** Dianyi Yang, Mengya Liu, Zhumei Wang, Yu Liu, Xiaochen Zhang, Yixuan Li, Le Ma, Yuhang Yang, Weiqi Huang, Wei Liang, Baoxiong Jia, Siyuan Huang
**Links:** [abs](https://arxiv.org/abs/2610.35075) - [pdf](https://arxiv.org/pdf/2610.35075)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data
- 作者：Dianyi Yang, Mengya Liu, Zhumei Wang, Yu Liu, Xiaochen Zhang, Yixuan Li, Le Ma, Yuhang Yang, Weiqi Huang, Wei Liang, Baoxiong Jia, Siyuan Huang
- 出版日期：2026-10-26T09:20:31Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.35075 ；PDF https://arxiv.org/pdf/2610.35075 ；项目页 https://young-bit.github.io/zero-hlm/

### 一句话总结
Zero-HLM 提出一个 real-to-sim-to-real 框架，将智能手机采集与仿真源示范转化为可扩展的人形 loco-manipulation 训练数据，并声称无需真实机器人数据即可实现零样本迁移。

### 研究问题
论文关注人形机器人 loco-manipulation 的可泛化学习受限于昂贵真实世界示范的问题。摘要指出，仿真虽然提供了可扩展替代方案，但需要视觉逼真、物理就绪的场景以及可执行全身运动；论文即围绕如何构建这样的仿真训练数据并实现零样本迁移展开。

### 核心思路/方法
摘要给出的方法要点包括：
1. **Real-to-sim-to-real 框架**：将智能手机采集和仿真源示范转化为人形 loco-manipulation 的可扩展训练数据。
2. **Gaussian-guided agentic real-to-sim reconstruction**：用于对齐视觉场景与物理场景。
3. **Motion-environment co-adaptation**：利用 rollout 反馈修正全身参考运动与交互几何。
4. **数据生成与训练**：生成 4,800 条经过物理验证的示范，用于三个 Unitree G1 任务的零样本迁移；仿真训练的 GR00T N1.7 被用于评估。

### 主要贡献
摘要明确给出的贡献包括：
- 提出 Zero-HLM 这一 real-to-sim-to-real 框架，面向无需真实机器人数据的人形 loco-manipulation 训练。
- 通过高斯引导的 agentic real-to-sim 重建对齐视觉与物理场景，并通过 rollout 反馈进行运动-环境协同适配。
- 生成 4,800 条物理验证示范，并报告在三个 Unitree G1 任务上的零样本迁移结果。
- 报告仿真训练的 GR00T N1.7 平均全任务成功率为 66.7%，而真实数据训练为 46.7%。
- 在泛化配置上，扩展仿真训练将 pooled success 从基于真实数据策略的 23% 提升到 69%，且不增加真实示范。

### 局限性
- 摘要未提供足够信息说明真实机器人实验的具体设置、任务定义、评估协议与统计显著性。
- 摘要未提供足够信息说明智能手机采集的规模、质量要求及失败案例。
- 摘要未提供足够信息说明 real-to-sim 重建与运动-环境协同适配的计算成本、人工介入程度和泛化边界。
- 摘要未提供足够信息说明与其它基线方法的完整对比及消融实验细节。

### 阅读优先级
**高**。理由：论文直接针对人形 loco-manipulation 中真实数据昂贵这一关键瓶颈，提出无需真实机器人数据的 real-to-sim-to-real 数据生成与零样本迁移框架，并给出明确的成功率对比与泛化配置结果；若关注人形机器人学习、仿真到现实迁移或可扩展示范生成，该摘要信息具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Learning generalizable humanoid loco-manipulation remains bottlenecked by costly real-world demonstrations. Simulation provides a scalable alternative, but requires visually faithful, physics-ready scenes and executable whole-body motions. We present Zero-HLM, a real-to-sim-to-real framework that transforms smartphone captures and simulated source demonstrations into scalable training data for humanoid loco-manipulation. Gaussian-guided agentic real-to-sim reconstruction aligns visual and physical scenes; motion-environment co-adaptation uses rollout feedback to correct whole-body references and interaction geometry. We generate 4,800 physically validated demonstrations for zero-shot transfer across three Unitree G1 tasks. Simulation-trained GR00T N1.7 achieves 66.7% mean full-task success, versus 46.7% with real-data training. On generalized configurations, expanded simulation training raises pooled success from 23% for base-trained real-data policies to 69%, without additional real demonstrations. Project page: https://young-bit.github.io/zero-hlm/

</details>

#### 2026-10-25 - How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder: A Hierarchical, Matched Sim-Real Benchmark for Physical Interaction

**Authors:** Haibao Yu, Jiaqi Meng, Zijian Zhang, Bowen Jing, Lei Yang, Yue Hu, Chenchen Ge, Yiming Hou, Chenbo Xin, Dawen Ye, Haifang Qin, Jin Li, Weitao Zhou, Jianing Qiu, Jiankai Sun, Dandan Zhang, Zaiqing Nie, Ping Luo, Ding Zhao
**Links:** [abs](https://arxiv.org/abs/2610.34527) - [pdf](https://arxiv.org/pdf/2610.34527)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder: A Hierarchical, Matched Sim-Real Benchmark for Physical Interaction
- 作者：Haibao Yu, Jiaqi Meng, Zijian Zhang, Bowen Jing, Lei Yang, Yue Hu, Chenchen Ge, Yiming Hou, Chenbo Xin, Dawen Ye, Haifang Qin, Jin Li, Weitao Zhou, Jianing Qiu, Jiankai Sun, Dandan Zhang, Zaiqing Nie, Ping Luo, Ding Zhao
- 出版日期：2026-10-25T19:41:02Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.34527 ；PDF https://arxiv.org/pdf/2610.34527

### 一句话总结
论文提出 PhysLadder——一个面向富接触操作、物理与视觉匹配的层级式 Sim-Real 基准，并用 16 个家务任务评估 GPT-6 Astra 零样本表现，发现其成功率随交互层级升高而显著下降，在 L3 上降至 0.0%。

### 研究问题
如何系统评估模型在富接触操作中的物理交互能力，尤其是接触选择、持续接触下的力调节，以及协调的接触重构与力调节；以及匹配的仿真环境能否作为可重复、可扩展的测试平台来研究这些能力边界。

### 核心思路/方法
构建 PhysLadder 层级式 Sim-Real 基准：16 个家务任务分为三个累积层级——L1 接触选择与几何对齐、L2 持续接触中的力调节、L3 协调的接触重构与力调节。每个任务在物理和视觉匹配的仿真与真实环境中实例化，并共享任务定义与成功标准。对 GPT-6 Astra 进行零样本评估，每个任务在每个环境中试验三次。

### 主要贡献
- 提出 PhysLadder：包含 16 个家务任务、三层累积难度的层级式 Sim-Real 基准，强调物理与视觉匹配及共享任务定义和成功标准。
- 提供 GPT-6 Astra 的零样本评测结果：真实环境成功率从 L1 的 80.0% 降至 L2 的 47.6%、L3 的 0.0%；仿真环境对应为 66.7%、47.6%、0.0%。
- 报告 Sim-Real 一致性观察：16 个任务中有 10 个在两种环境下的成功次数相同，其余 6 个相差一次成功（三次试验中）。
- 归纳反复出现的困难：空间推理、接触选择、力调节与协调，常使局部物理进展无法累积为任务完成。

### 局限性
- 摘要仅报告 GPT-6 Astra 的零样本结果，每个任务每环境仅三次试验；未提供其他模型、训练方法或更大规模试验的信息。
- 摘要未提供任务的具体构成、成功判定的细节、仿真与真实环境匹配程度的定量指标，以及误差分析或统计显著性信息。
- 摘要未提供关于基准可扩展性、任务多样性覆盖或真实环境实验设置的具体信息。
- 摘要未提供足够信息以判断结论对其他模型或更广泛富接触任务的泛化性。

### 阅读优先级
高。理由：该工作直接给出富接触操作中分层能力边界的实证结果，并强调匹配 Sim-Real 的可重复评测设计；对关注具身智能评测、物理交互与仿真到现实一致性的研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce PhysLadder, a hierarchical Sim-Real benchmark for evaluating physical interaction capabilities in contact-rich manipulation. Its 16 household tasks span three cumulative levels: contact selection and geometric alignment (L1), force regulation within sustained contact (L2), and coordinated contact reconfiguration and force regulation (L3). Each task is instantiated in physically and visually matched simulated and real-world environments, with shared task definitions and success criteria. We evaluate GPT-6 Astra zero-shot with three trials per task in each environment. Real-world success rates decline from 80.0% at L1 to 47.6% at L2 and 0.0% at L3, with corresponding simulation rates of 66.7%, 47.6%, and 0.0%. Ten of the 16 tasks have identical success counts across environments; the remaining six differ by one success out of three trials. Across both environments, recurring difficulties in spatial reasoning, contact selection, force regulation, and coordination often prevent local physical progress from accumulating into task completion. These findings characterize Astra's observed capability boundary across increasing interaction demands and, for this model, support matched simulation as a repeatable, scalable testbed for studying the sustained, coordinated physical interactions that limit reliable manipulation.

</details>

#### 2026-10-25 - AuRA: From Atoms to Bits through Autonomous Robot Interaction

**Authors:** Xinchen Yu, Yoonkyo Jung, Haoran Chen, Zikui Cai, Aayush Talreja, Seungjae Lee, Hyunjin Kim, Furong Huang
**Links:** [abs](https://arxiv.org/abs/2610.34452) - [pdf](https://arxiv.org/pdf/2610.34452)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AuRA: From Atoms to Bits through Autonomous Robot Interaction
- 作者：Xinchen Yu, Yoonkyo Jung, Haoran Chen, Zikui Cai, Aayush Talreja, Seungjae Lee, Hyunjin Kim, Furong Huang
- 出版日期：2026-10-25T17:10:27Z
- 分类：主分类 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.34452 ；PDF https://arxiv.org/pdf/2610.34452

### 一句话总结
AuRA 通过自主机器人交互与数据准备流程，减少数字孪生重建中对人工操作和标注的依赖，并在 13 个可变形物体上降低人工投入与采集时间。

### 研究问题
仿真可支持规模化机器人学习实验，但获取符合物理规律的数字孪生往往需要人工操作和手动标注记录到的交互数据。论文关注如何减少数字孪生重建过程中对人类劳动的依赖。

### 核心思路/方法
AuRA 是一个自动化机器人交互与数据准备的系统，用于数字孪生重建。摘要给出的方法组成包括：
- 执行感知的抓取选择；
- 从机器人状态推导夹爪运动测量；
- 使用配准后的交互前几何与外观先验。

这些设计旨在支持自主采集、避免依赖视觉夹爪跟踪，并恢复被机器人遮挡的物体信息。

### 主要贡献
- 提出 AuRA 系统，自动化机器人交互和数据准备，以支持数字孪生重建。
- 在 13 个可变形物体上，相对基线将每个成功重建资产的主动人工劳动减少 88.5%，实际采集时间减少 55.4%。
- 与人工采集的 PhysTwin 基线相比，在已知夹爪运动的未来预测任务中，9 项指标中有 7 项改善，其中单向 \(L_1\) Chamfer 距离降低 28.1%。
- 在所评估的未见交互下，取得相近的平均轮廓 IoU 和 Chamfer 距离。
- 结果表明自主机器人交互有潜力支持更高效的数字孪生获取，并保持可比的重建质量。

### 局限性
摘要未提供足够信息说明局限性与失败情形。摘要未提供足够信息说明方法在更多物体类别、真实部署条件、不同机器人平台或更广泛交互场景下的适用性。摘要未提供足够信息说明“未见交互”的具体定义、评估规模及统计细节。

### 阅读优先级
中。理由：论文主题涉及机器人学习、数字孪生获取与自主数据采集，摘要给出了明确的人工劳动与采集时间降幅及重建指标对比；但摘要篇幅有限，未展开方法细节、实验设置和局限性。若关注可变形物体数字孪生或机器人自主数据采集，可优先阅读全文进一步核验。

</details>

<details>
<summary>Abstract</summary>

Simulation enables robot-learning experiments at scale, but acquiring physics-informed digital twins often requires human manipulation and manual annotation of recorded interactions. To reduce this reliance on human effort, we present AuRA, a system that automates robot interaction and data preparation for digital-twin reconstruction. AuRA combines execution-aware grasp selection, gripper-motion measurements derived from robot states, and registered pre-interaction geometry and appearance priors. These choices enable autonomous collection, avoid reliance on visual gripper tracking, and recover object information obscured by the robot. Across 13 deformable objects, AuRA reduces active human labor and wall-clock collection time per successfully reconstructed asset by 88.5% and 55.4%, respectively. Relative to the human-collected PhysTwin baseline, AuRA improves seven of nine metrics for future prediction under known gripper motion, including a 28.1% reduction in one-way $L_1$ Chamfer distance. It also achieves similar mean silhouette IoU and Chamfer distance under the evaluated unseen interactions. These results highlight the potential of autonomous robot interaction to support more efficient digital-twin acquisition with comparable reconstruction quality.

</details>

#### 2026-10-25 - On Distributed Sensing and Adversarial Localization of Narrowband Acoustic Sources for Offshore Data Center Monitoring

**Authors:** Adnan Abdullah, David Blow, Harsha Gundala Sureshbabu, Dongyoon Joung, Sara Rampazzi, Md Jahidul Islam
**Links:** [abs](https://arxiv.org/abs/2610.34393) - [pdf](https://arxiv.org/pdf/2610.34393)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：On Distributed Sensing and Adversarial Localization of Narrowband Acoustic Sources for Offshore Data Center Monitoring
- 作者：Adnan Abdullah, David Blow, Harsha Gundala Sureshbabu, Dongyoon Joung, Sara Rampazzi, Md Jahidul Islam
- 出版日期：2026-10-25T15:54:02Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2610.34393 ；PDF https://arxiv.org/pdf/2610.34393

### 一句话总结

针对海上数据中心面临的窄带对抗性声源威胁，论文提出一种结合移动接收器锚点约束与粒子滤波的分布式声学定位与跟踪框架，以缓解稀疏传感器下 TDOA 混叠导致的定位模糊问题。

### 研究问题

论文关注海上数据中心监测场景中的被动声学监视问题，具体是定位并跟踪具有威胁性的窄带对抗性声源。摘要指出，传统声源定位方法依赖宽带信号和紧凑接收阵列，而该场景具有两个关键困难：一是声源为窄带发射，二是传感器稀疏。在此条件下，观测到的 TDOA 测量会发生混叠，产生多解的模糊解空间，使传统定位方法失效。因此，核心问题是：在窄带、稀疏传感器、接收器位置不确定和感知噪声条件下，如何约束可行解空间并实现稳定的声源定位与跟踪。

### 核心思路/方法

论文提出一种两阶段流水线：

1. **锚点约束的初始位置估计**：引入一个移动接收器，使其与选定的固定接收器临时组成锚点对，从而对可行的解空间施加约束，缓解窄带 TDOA 混叠带来的模糊性。
2. **粒子滤波联合跟踪**：在获得初始源位置后，初始化粒子滤波，联合跟踪声源的位置与速度；跟踪过程使用一个实时锚点测量，并结合质量自适应的固定接收器对测量。

方法整体面向稀疏传感器与窄带发射条件下的分布式声学感知，强调通过移动锚点与测量质量自适应来提升定位与跟踪的可行性。

### 主要贡献

- 提出面向海上数据中心声学监视的窄带对抗性声源定位与跟踪框架。
- 针对窄带发射与稀疏传感器导致的 TDOA 混叠和多解模糊问题，设计移动接收器临时锚点对约束解空间的两阶段方法。
- 将初始锚点约束估计与粒子滤波联合位置—速度跟踪结合，并引入质量自适应的固定接收器对测量。
- 通过蒙特卡洛声学仿真、ROS-Gazebo 机器人演示和开放水域现场实验进行评估；摘要报告仿真中定位成功率为 91%，10 次现场试验中有 9 次在接收器位置不确定与感知噪声条件下跟踪误差低于 2 m。

### 局限性

摘要未提供足够信息说明方法的具体失败模式、计算开销、可扩展性、不同窄带条件与传感器稀疏程度下的系统性能边界，也未提供现场实验中未成功试验的原因分析。此外，摘要未提供足够信息说明与现有基线方法的定量对比细节、实验规模和数据采集条件。

### 阅读优先级

**中**。理由：该论文面向海上数据中心基础设施的被动声学监视，问题设定明确，结合移动锚点约束与粒子滤波的思路对窄带稀疏传感定位具有针对性，且包含仿真、机器人演示与开放水域实验等多层验证。但摘要未给出与现有方法的详细对比和充分局限性分析；若读者关注窄带 TDOA 混叠、稀疏阵列定位或基础设施声学监视，优先级可视为中偏高；若仅关注通用声源定位方法，则为中等。

</details>

<details>
<summary>Abstract</summary>

This report investigates an acoustic surveillance framework for localizing and tracking narrowband adversarial acoustic sources that threaten offshore data centers. Unlike conventional sound source localization (SSL) methods that rely on broadband signals and compact receiver arrays, the considered scenario involves narrowband emissions and sparse sensors. In such scenarios, the observed time-difference-of-arrival (TDOA) measurements are aliased and produce an ambiguous solution space, rendering conventional localization methods ineffective. To address this challenge, we integrate a mobile receiver that temporarily forms anchor pairs with selected fixed receivers, constraining the feasible solution space. The proposed two-stage pipeline first estimates the initial source position using anchor constraints, then initializes a particle filter that jointly tracks source position and velocity using one live anchor measurement and quality-adaptive fixed-pair measurements. We evaluate the proposed method through Monte Carlo acoustic simulations, ROS-Gazebo robotic demonstrations, and open-water field experiments. Our framework achieves a localization success rate of 91% in simulation, while 9 of 10 field trials show tracking error below 2m under receiver-position uncertainty and noisy sensing conditions. These findings demonstrate the feasibility of passive acoustic surveillance for protecting large-scale infrastructure against acoustic threats.

</details>

#### 2026-10-25 - From Presence Labels to Bounding Boxes: Can Multimodal Large Language Models Scale Surgical Instrument Localization?

**Authors:** Mohamed Hamdy, Muraam Abdel-Ghani, Fatmaelzahraa Ahmed, Sifna Nasar, Mariam Ahmed, Khalid Al-Jalham, Abdulaziz Al-Ali, Shidin Balakrishnan
**Links:** [abs](https://arxiv.org/abs/2610.34218) - [pdf](https://arxiv.org/pdf/2610.34218)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Presence Labels to Bounding Boxes: Can Multimodal Large Language Models Scale Surgical Instrument Localization?
- 作者：Mohamed Hamdy, Muraam Abdel-Ghani, Fatmaelzahraa Ahmed, Sifna Nasar, Mariam Ahmed, Khalid Al-Jalham, Abdulaziz Al-Ali, Shidin Balakrishnan
- 出版日期：2026-10-25T11:18:07Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.34218) | [PDF](https://arxiv.org/pdf/2610.34218)

### 一句话总结
论文提出并评估一个基于多模态大语言模型（MLLM）的可扩展标注框架，将手术帧与已有的器械存在性标签转换为器械边界框，并在 Cholec80 腹腔镜胆囊切除术数据上系统分析其可靠性、成本与设计敏感性。

### 研究问题
手术器械的空间定位依赖边界框标注，是手术场景理解的基础，但现有标注往往只覆盖部分帧、视频子集或数据集变体，而非完整手术流程；人工扩展标注耗时且依赖专家。弱监督方法和基于检测器的伪标签又需要任务特定训练，且可能不精确。因此论文关注：能否利用 MLLM 将已有器械存在性标签规模化地转换为准确边界框，并系统评估其可靠性、成本与设计敏感性。

### 核心思路/方法
- 设计一个基于 MLLM 的可扩展标注框架，将手术帧和已有的器械存在性标签转换为边界框。
- 在 Cholec80 的腹腔镜胆囊切除术数据上实例化该框架，使用六个 MLLM 及一种多调用配置。
- 采用精心设计的分层方案，由两名标注者独立标注 1,000 帧，并由一名专家外科医生审核其中一组标注以建立参考。
- 比较不同模型和调用配置的识别与定位表现，并分析结构化多阶段标注流程的效果。

### 主要贡献
- 提出将器械存在性标签转换为边界框的 MLLM 标注框架，并系统分析其可靠性、成本和设计敏感性。
- 实验显示器械集合识别 F1 为 88.2 至 92.7，而 mIoU 为 0.180 至 0.735，表明相近的识别表现可能掩盖较大的定位差异。
- 结构化多阶段标注流程达到 0.784 mIoU，高于最佳单次调用基线的 0.735，接近人-人一致性的 0.814。
- 使用最佳准确率流程创建并公开发布 Cholec80 的空间扩展：覆盖 80 个视频的全部 184,498 个已标注帧，共 285,977 个边界框；标注与人工参考已在 GitHub 公开。

### 局限性
- 论文仅在 Cholec80 的腹腔镜胆囊切除术数据上实例化框架，摘要未提供在其他手术类型或数据集上的验证信息。
- 摘要未提供六种 MLLM 的具体名称、多调用配置的细节、成本分析的具体结果，以及设计敏感性分析的具体维度与结论。
- 人工参考仅由专家外科医生审核两名标注者中的一组标注集，摘要未说明另一组标注是否也经过专家审核。
- 摘要未提供推理成本、运行时间或计算资源需求的具体数据。
- 摘要未提供失败案例、误差来源或框架在低质量存在性标签下的表现。

### 阅读优先级
中。理由：该工作直接针对手术数据边界框标注的可扩展性问题，并公开发布大规模 Cholec80 空间扩展标注，对手术场景理解、检测与视觉-语言应用有实用价值；同时揭示了识别指标与定位指标之间的显著差异，具有方法学警示意义。但摘要未提供跨数据集验证和详细成本结果，若读者关注特定 MLLM 选型、标注成本或非胆囊切除术场景，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Spatial localization of surgical instruments through bounding-box annotations is a foundational component of surgical scene understanding, supporting detection, tracking, interaction analysis, and grounded vision-language applications. Yet existing annotations often cover selected frames, video subsets, or dataset variants rather than complete procedures. Manual extension is time-consuming and expert-dependent. Additionally, weakly supervised and detector-based pseudo-labels require task-specific training and may be imprecise. In this study, we design a scalable MLLM-based annotation framework that converts surgical frames and existing instrument-presence labels into accurate bounding boxes, and systematically analyze its reliability, cost, and design sensitivity. We instantiate the framework using six MLLMs and a multi-call configuration on laparoscopic cholecystectomy in Cholec80. Using a carefully designed stratification scheme, two annotators independently label 1,000 frames, and an expert surgeon reviews one annotation set to establish the reference. Results show that instrument-set F1 ranges from 88.2 to 92.7,whereas mIoU ranges from 0.180 to 0.735, showing that comparable recognition can conceal large localization differences. A structured multi-stage annotation pipeline achieves 0.784 mIoU, compared with 0.735 for the best single-call baseline and 0.814 human-human agreement. Using the best accuracy pipeline, we create and publicly release a spatial extension of Cholec80 comprising 285,977 bounding boxes across all 184,498 annotated frames from the 80 videos. The annotations and human references are made available on GitHub

</details>

#### 2026-10-25 - PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy

**Authors:** Mengdi Li, Boxian Yao, Xiyu Zhu, Yifan Yang, Yunfan Lou, Xuan Han, Tao Liu, Zhibo Pang
**Links:** [abs](https://arxiv.org/abs/2610.34147) - [pdf](https://arxiv.org/pdf/2610.34147)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy
- 作者：Mengdi Li, Boxian Yao, Xiyu Zhu, Yifan Yang, Yunfan Lou, Xuan Han, Tao Liu, Zhibo Pang
- 出版日期：2026-10-25T08:29:58Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.34147 ；PDF https://arxiv.org/pdf/2610.34147

### 一句话总结
PS-DLO 提出一种结合物体物理属性先验与未来空间监督信息的可变形线性物体操作策略，并在真实单臂/双臂多任务及视觉变化条件下验证其有效性。

### 研究问题
论文关注可变形线性物体（DLO）操作中的耦合感知与控制难题：一方面，细长几何形态导致精确定位困难；另一方面，形变依赖物体特定的物理属性。摘要指出，需要同时应对定位困难与属性相关形变的问题。

### 核心思路/方法
- 使用对比式图像—文本学习，将初始观测映射为 DLO 属性的类别化描述，为动作生成提供显式的物理与结构先验。
- 使用 SAM3 从未来观测中提取掩码引导特征，并将这些特征蒸馏到策略的动作专家中，以编码任务相关的 DLO 区域及其后续构型。
- 在单臂和双臂平台上分别训练共享多任务策略，并在九个真实世界任务上评估。

### 主要贡献
- 提出 PS-DLO 策略，将物体属性先验与未来空间监督结合用于 DLO 操作。
- 在九个真实世界任务、单臂与双臂平台上评估，每个 embodiment 训练共享多任务策略；平均成功率为 68.9%，比最强基线高 20.0 个百分点。
- 在蝴蝶结解结任务的泛化实验中，于七种视觉偏移条件中的六种取得高于基线的成功率，表明对视觉变化具有更好的鲁棒性。

### 局限性
- 摘要未提供足够信息说明方法在更广泛 DLO 类型、任务分布或真实部署条件下的适用边界。
- 摘要未提供足够信息说明对比式图像—文本学习所依赖的属性类别描述范围及其标注需求。
- 摘要未提供足够信息说明 SAM3 未来观测特征蒸馏的具体实现细节、计算开销与失败模式。
- 摘要未提供足够信息说明未取得优势的那一种视觉偏移条件的具体原因。
- 摘要未提供足够信息说明与最强基线之外的更多基线比较情况。

### 阅读优先级
高。理由：摘要明确给出真实世界多任务评估结果、相对最强基线的定量提升以及视觉泛化实验结论，且问题设定聚焦 DLO 操作中的感知—控制耦合难点；若关注机器人操作策略、物体属性先验或未来空间监督，该文具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Deformable linear objects (DLO) pose a coupled perception and control challenge: their slender geometry makes precise localization difficult, while their deformations depend on object-specific physical properties. To address this challenge, we propose PS-DLO, a property- and spatially aware DLO manipulation policy. First, contrastive image-text learning maps the initial observation to categorical descriptions of DLO properties, providing explicit physical and structural priors for action generation. Second, SAM3 extracts mask-guided features from future observations, which are distilled into the policy's action expert to encode task-relevant DLO regions and their subsequent configurations. We evaluate PS-DLO on nine real-world tasks across single-arm and bimanual platforms, training a shared multi-task policy for each embodiment. PS-DLO achieves an average success rate of 68.9%, exceeding the strongest baseline by 20.0 percentage points. In generalization experiments, PS-DLO achieves higher success rates than the baseline in six of seven visual-shift conditions on butterfly-knot untying. These results demonstrate that combining object-property priors with future spatial supervision improves multi-task DLO manipulation and robustness to visual variation.

</details>

#### 2026-10-25 - Enabling Motion-Induced WiFi-CSI Sensing in Multi-Robot Systems: A Simulation Framework

**Authors:** Brendan Dijkstra, Ninad Jadhav, Maurice Stoffijn, Stephanie Gil, Bahar Haghighat
**Links:** [abs](https://arxiv.org/abs/2610.34034) - [pdf](https://arxiv.org/pdf/2610.34034)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Enabling Motion-Induced WiFi-CSI Sensing in Multi-Robot Systems: A Simulation Framework
- 作者：Brendan Dijkstra, Ninad Jadhav, Maurice Stoffijn, Stephanie Gil, Bahar Haghighat
- 出版日期：2026-10-25T03:55:16Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.34034 ；PDF https://arxiv.org/pdf/2610.34034

### 一句话总结
该论文提出一个开源仿真框架，将 WiFi Sensor for Robotics（WSR）传感流程集成进 Gazebo，以生成具有较真实物理信号特性的合成 WiFi-CSI 测量，用于多机器人系统中运动诱导的感知、方位估计与定位研究。

### 研究问题
论文关注的问题是：WSR 方法虽已表明，机器人运动过程中采集的 WiFi-CSI 测量结合里程计可合成虚拟天线阵列，并实现运动诱导的方位估计，但其部署仍面临困难，主要原因是与标准机器人工具的集成有限，以及依赖已过时的 WiFi-CSI 采集硬件。因此，作者希望降低 WiFi-CSI 传感在多机器人系统中的使用门槛。

### 核心思路/方法
论文的核心方法是构建一个开源仿真框架，将 WSR 传感流程集成到机器人仿真器 Gazebo 中。该框架生成具有较真实物理信号特性的合成 WiFi-CSI 测量，并利用运动诱导传感及下游定位所需的较真实机器人运动。框架还支持处理仿真和真实 WiFi-CSI 数据，以便直接比较和验证。作者使用 TurtleBot3 机器人，通过比较仿真实验与真实世界实验来验证框架，并展示其在方位估计和机器人定位中的用途。

### 主要贡献
- 提出一个开源仿真框架，将 WSR 传感流程集成进 Gazebo。
- 生成具有较真实物理信号特性的合成 WiFi-CSI 测量。
- 利用较真实的机器人运动支持运动诱导传感和下游定位。
- 支持处理仿真与真实 WiFi-CSI 数据，用于直接比较和验证。
- 通过 TurtleBot3 机器人的仿真与真实实验比较验证框架，并展示其在方位估计和机器人定位中的应用。
- 旨在使 WSR 风格传感成为机器人研究中可访问的模块化传感模态，为将 WiFi-CSI 传感与多模态感知结合用于定位和协调提供基础。

### 局限性
摘要未提供足够信息说明该框架在信号模型精度、仿真与真实数据差距、可扩展性、计算开销、硬件依赖或更广泛场景下的局限。摘要也未提供足够信息说明实验规模、定量性能指标和失败案例。

### 阅读优先级
中。理由：该工作面向多机器人 WiFi-CSI 传感的仿真与开源工具，问题明确且对相关机器人感知研究有实用价值；但摘要未给出定量实验结果和详细局限，是否优先阅读取决于读者对 WiFi-CSI 传感、Gazebo 仿真或多机器人定位工具链的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

WiFi Channel State Information (CSI) enables fine-grained sensing of spatial relationships between wireless devices. The WiFi Sensor for Robotics (WSR) toolbox demonstrated that WiFi-CSI measurements collected during robot motion, combined with odometry, can be used to synthesize virtual antenna arrays, enabling motion-induced bearing estimation in multi-robot experiments. However, deploying the WSR approach has remained challenging due to its limited integration with standard robotics tools and reliance on deprecated WiFi-CSI acquisition hardware. This work presents an open-source simulation framework that integrates the WSR sensing pipeline within the robotic simulator Gazebo. The framework generates synthetic WiFi-CSI measurements with realistic physical signal properties and leverages realistic robot motion required for motion-induced sensing and downstream localization. It further supports processing both simulated and real WiFi-CSI data for direct comparison and validation. Our aim is to make WSR-style sensing accessible as a modular sensing modality for robotic research. We validate our framework by comparing simulated and real-world experiments using TurtleBot3 robots, and demonstrate its use for bearing estimation and robot localization. This work lowers the barrier to entry for WiFi-CSI-based sensing in multi-robot systems and provides a foundation for integrating WiFi-CSI sensing with multi-modal perception for localization and coordination. All code and experimental details are publicly available at https://github.com/baharhaghighat/DARS_2026_Dijkstra_et_al

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
