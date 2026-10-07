# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：68
- 分类分布：
  - Neural Scene Representations & Rendering: 20
  - 3D Reconstruction & Multi-view Geometry: 20
  - Embodied / Robotics / AR Applications: 17
  - Geometry Foundation Models: 8
  - Dynamic / 4D Reconstruction: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“几何基础模型”正在从重建器演变为可编排的空间推理底座。** GeoWM、Revar3R、M3SunAgent、DepthWorld 都直接把 Geometry Foundation Models 或前馈几何模型当作世界模型/智能体的上游模块：GeoWM 用几何基础模型把 RGB 转成“几何历史”再预测未来几何，M3SunAgent 以 LLM 规划器调度深度与 grounding 工具，DepthWorld 则先解决大规模 3D 监督再训练多视角 RGB-深度扩散世界模型。这类工作共同指向“几何先验 + 下游任务”的分层架构，而非端到端单模型。

2. **稀疏输入下的鲁棒性与不确定性成为前馈 3D 的显式议题。** DensiTok 不再合成额外像素，而是直接致密化内部几何 token；MGE 通过遮蔽跨视角上下文并蒸馏全上下文教师，换取长序列可扩展性与抗干扰；ReVar3R 指出无训练扰动不确定性会被输出规范（gauge）对称性污染，并给出闭式诊断。三者从不同角度回应同一个问题：前馈 3D 模型在少视角、长序列、跨视角噪声下的可靠性。

3. **神经场景表示正从“能重建”转向“能压缩、能复用、能结构化”。** GSCV 用标准视频编解码器压缩 GS 序列并解决 PLAS 随机性导致的帧间相关性弱问题；OpenSplatGraph 把高斯式开放词汇语义地图直接提升为持久 3D 场景图；Post-Training Semantic Lifting 则把语义提升误差拆成检测器、提升与标签迁移三类。方向从追求渲染质量，转向部署、语义结构化与误差可归因。

4. **机器人/具身方向密集出现“单策略、去中心化、无通信”的协作与规划范式。** CoRE 让同一策略在无身份标签、无机器人间消息条件下学习互补角色；OntoPlan 用本体化符号场景表示加选择性检索替代“把整个场景塞进 LLM 文本”；WareFly-VLA 补上仓库 UAV 语言条件控制的基准缺口。共同点是：不再假设全局状态可获取，而是强调局部观测、共享参数和可扩展的符号/语言接口。

5. **Real2Sim2Real 与仿真闭环成为跨方向连接器，但分歧明显。** DT-R2S2R 走数字孪生条件化扩散生成，为自动驾驶新区域合成带免费标注的数据；Sionna-Isaac 联合仿真把射线追踪信道实时反馈进控制回路；WareFly-VLA、DepthWorld 也都依赖 Isaac Sim 或校准数据集。可见“仿真/数字孪生”正从评测工具变成数据与监督的来源，但生成式增广与物理仿真两条路线的取舍尚未收敛。

#### 技术路线观察

- **几何基础模型：从“一次前馈出结果”走向“可被条件化、可被遮蔽、可被诊断”。** GeoWM 把几何基础模型作为历史编码器，用 flow-matching transformer 直接跳到未来时域；MGE 在训练时主动丢弃 frame token，说明全对全注意力并非最优；ReVar3R 则质疑“跑两次看方差”的朴素不确定性，强调先对齐相似变换框架。三者共同的隐含判断是：几何基础模型的瓶颈已不全在网络容量，而在上下文组织方式与输出规范的处理。
- **3D/4D 重建：多传感器、物理失真与语义结构并重。** SURGE 把相机与 2D 成像声呐在因子图中联合估计轨迹与目标位置，再用度量位姿驱动声呐高斯泼溅；水下折射校正则把平口相机图像在图像空间物理校正为针孔透视，且对下游 SLAM 保持不可知。这与 DepthWorld 的 DROID-3D 校准流程（立体深度 + 联合因子图恢复机器人运动学与外参）属于同一逻辑：先修几何/标定，再谈重建与下游。
- **神经场景表示：压缩与结构化是两条并行主线。** GSCV 关注 GS 序列在无跟踪信息条件下的视频编解码可压缩性；AIMS 把“可用观测数”与“全局合成模型处理视图数”解耦；LSA 从 INR 的谱分解角度改激活函数。结构化方向则由 OpenSplatGraph 和 Post-Training Semantic Lifting 代表：前者把稠密语义场提升为场景图，后者把语义提升误差显式拆分。二者都在解决“特征场有了，但对象级推理和误差归因不够”的问题。
- **机器人/AR 应用：语言与符号接口在变厚，底层控制仍难。** WareFly-VLA 明确报告仓库语言条件空中控制“仍远未解决”；CoRE 用动作-专家对齐损失在无角色标签下监督专家选择；OntoPlan 用本体词汇降低 token 成本并满足前置条件。相较之下，Sionna-Isaac 把通信链路质量实时并入感知-行动-通信回路，提示机器人导航的仿真边界正在从“几何+物理”扩展到“几何+物理+无线信道”。
- **实时渲染：预计算与神经表示结合，把运行时积分挪到训练时。** NEF 在发光体局部坐标系中预计算位置、法线、视线方向、材质参数化的神经场，使互反射、自遮挡、形变被吸收进表示而不增加运行时成本。这与 GS 压缩、AIMS 的固定全局预算思路一致：把昂贵计算前移或解耦，是当前表示类工作的共同工程取向。

#### 值得优先阅读的论文

1. **DepthWorld: 3D World Model for Robot Manipulation** — 同时贡献校准数据集 DROID-3D 与多视角 RGB-深度扩散世界模型，直接回应“视频世界模型逐帧对但 3D 不一致”的核心痛点；其校准流程对任何使用 DROID 的工作都有复用价值。
2. **GeoWM: Efficient Direct World Modeling in Explicit Geometry** — 提出非递归、指定未来时域直接预测显式几何的范式，并用轻量相机运动预测器提供未来视角先验；若成立，可绕开图像/潜表示世界模型的误差累积问题，值得验证其长时域几何一致性。
3. **Revar3r: gauge-aware perturbation uncertainty for feed-forward 3d reconstruction** — 对“无训练不确定性”给出闭式诊断与规范对齐修正，问题定义清晰且可能影响所有前馈 3D 模型的置信度使用方式；30 个真实 VGGT view-sets 的验证信号也较具体。
4. **MGE: Less Context, Better Geometry** — 提出遮蔽跨视角上下文 + 全上下文教师蒸馏，并配套 Anchor-Guided Adaptive token merging；如果结论稳健，将同时改善长序列推理与抗遮挡/抗相似视图干扰能力。
5. **OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs** — 把在线高斯式开放词汇语义地图直接提升为持久 3D 场景图，兼顾语言引导定位与关系推理；对机器人感知的“特征场 → 对象级结构”链路有直接参考价值。

#### 可能的研究机会

- **把“校准/规范对齐”做成前馈 3D 的通用前置模块。** DepthWorld 的联合因子图标定与 ReVar3R 的相似变换配准处理的是同一类问题：输出帧未观测对称性会污染监督与不确定性。可探索将 gauge-aware 对齐与多传感器标定统一为可微分预处理层。
- **稀疏视角前馈 3D 的“内部致密化”与“外部生成增广”需要系统对比。** DensiTok 在隐空间补全几何 token，DT-R2S2R 则在像素/模拟器渲染层面生成新视角。二者在 3D 一致性、成本、可迁移性上的边界尚不清晰，值得做控制变量比较。
- **结构化场景图与语义提升的误差归因可以打通。** Post-Training Semantic Lifting 已把误差拆成检测器、提升、标签迁移三类，OpenSplatGraph 则构建对象级图。若把前者的误差分解用于后者的节点/边置信度，可能得到可

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-07T14:56:43-04:00
**Total number of papers:** 68
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

#### 2026-10-06 - DepthWorld: 3D World Model for Robot Manipulation

**Authors:** Jai Bardhan, Josef Sivic, Vladimir Petrik
**Links:** [abs](https://arxiv.org/abs/2610.08780) - [pdf](https://arxiv.org/pdf/2610.08780)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** geometric reasoning, metric depth, stereo depth, robotics, manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DepthWorld: 3D World Model for Robot Manipulation
- 作者：Jai Bardhan, Josef Sivic, Vladimir Petrik
- 出版日期：2026-10-06T17:59:00Z
- 分类：Geometry Foundation Models（主类）；Embodied / Robotics / AR Applications（次类）
- 链接：https://arxiv.org/abs/2610.08780 ；PDF：https://arxiv.org/pdf/2610.08780

### 一句话总结
论文提出用于机器人操作的 3D 世界模型 DepthWorld，通过构建校准的 3D 数据集 DROID-3D，并训练同时预测多视角 RGB 与深度的扩散世界模型，以缓解现有基于 RGB 的视频世界模型缺乏一致 3D 几何的问题。

### 研究问题
摘要指出，世界模型可作为传统机器人模拟器的数据驱动替代方案，用于策略评估、改进和规划；但这些用途都依赖可信的 3D 几何。当前基于视频的世界模型仅用 RGB 训练，生成的 rollout 虽然逐帧看起来正确，却不能组合成一致的 3D 世界。因此，论文关注两个方面的缺口：机器人操作领域的大规模 3D 监督，以及能够吸收这些监督而不破坏强预训练视频先验的架构。

### 核心思路/方法
论文包含数据集构建与模型训练两部分：

1. **校准流程与 DROID-3D**：提出一种校准流程，将学习到的立体深度与联合因子图结合，汇集来自同一物理机器人的所有 episode，以恢复该机器人共享的运动学参数以及每个场景的外参。将该流程应用于 DROID 数据集后，得到 DROID-3D，这是一个校准的 3D 数据集，提供密集度量深度和重新校准的多视角外参；摘要称在 90% 的 episode 上，外部相机达到小于 0.7 px 的重投影误差。

2. **DepthWorld 模型**：基于 Stable Video Diffusion 训练世界模型 DepthWorld，通过空间 latent tiling 联合预测多视角 RGB 和深度，同时保持预训练 VAE 不变。摘要强调，在相同训练预算下，深度监督使 RGB 预测本身相比仅 RGB 的相同基线提升 +1.48 dB PSNR，同时产生可用于下游几何推理的准确度量深度。

### 主要贡献
- 提出一种校准流程，结合学习到的立体深度与联合因子图，汇集同一物理机器人的所有 episode，恢复共享运动学参数和逐场景外参。
- 构建 DROID-3D：在 DROID 数据集上应用上述流程得到的校准 3D 数据集，提供密集度量深度和重新校准的多视角外参，并报告外部相机在 90% episode 上低于 0.7 px 重投影误差。
- 提出 DepthWorld：基于 Stable Video Diffusion 的世界模型，通过空间 latent tiling 联合预测多视角 RGB 与深度，并保持预训练 VAE 不变。
- 报告深度监督在相同训练预算下将 RGB 预测相对仅 RGB 基线提升 +1.48 dB PSNR，同时产出准确度量深度以支持下游几何推理。

### 局限性
摘要未提供足够信息说明以下方面：数据集规模、机器人平台种类、校准流程对失败案例或不同相机配置的鲁棒性、DepthWorld 在真实机器人操作任务中的策略评估/规划效果、推理速度与计算成本、泛化到 DROID 之外数据的能力、以及深度预测误差的定量指标。摘要也未提供消融实验细节、基线选择范围和训练数据具体规模。

### 阅读优先级
高。理由：论文同时涉及机器人操作中的 3D 世界模型、大规模 3D 监督数据集构建与视频扩散模型架构改造，问题定义明确，且摘要给出了可量化的改进结果；对关注几何基础模型、具身智能、机器人策略评估与规划的研究者有直接相关性。

</details>

<details>
<summary>Abstract</summary>

World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look correct frame-by-frame but do not compose into a consistent 3D world. Closing this gap requires progress on two fronts: large-scale 3D supervision for manipulation, and an architecture that can absorb it without disturbing strong pretrained video priors. We introduce a calibration pipeline that combines learned stereo depth with a joint factor graph, pooling all episodes collected from the same physical robot to recover its shared kinematic parameters alongside per-scene extrinsics. Applied to the DROID dataset, this yields DROID-3D, a calibrated 3D dataset providing dense metric depth and recalibrated multi-view extrinsics (achieving <0.7 px reprojection error on 90% of episodes for external cameras). We then train DepthWorld, a Stable Video Diffusion-based world model that jointly predicts multi-view RGB and depth via spatial latent tiling, leaving the pretrained Variational Autoencoder (VAE) unchanged. Depth supervision improves RGB prediction itself by +1.48 dB PSNR over an identical RGB-only baseline at equal training budget, while simultaneously yielding accurate metric depth for downstream geometric reasoning.

</details>

#### 2026-10-06 - M3SunAgent: Monocular 3D Spatial Understanding Agent for Metric Depth Estimation and 3D Visual Grounding

**Authors:** Jinsong Zhang, Kejun Wu, Ming Zhu, Renjie Qiao, Chengtao Cai, Zhengguo Li
**Links:** [abs](https://arxiv.org/abs/2610.07982) - [pdf](https://arxiv.org/pdf/2610.07982)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：M3SunAgent: Monocular 3D Spatial Understanding Agent for Metric Depth Estimation and 3D Visual Grounding
- 作者：Jinsong Zhang, Kejun Wu, Ming Zhu, Renjie Qiao, Chengtao Cai, Zhengguo Li
- 出版日期：2026-10-06T08:45:25Z
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（次分类）
- 链接：[摘要](https://arxiv.org/abs/2610.07982) / [PDF](https://arxiv.org/pdf/2610.07982)

### 一句话总结
本文提出统一的单目 3D 空间理解智能体 M3SunAgent，以 LLM 作为任务规划器协调多种工具，将实例级度量深度估计与单目 3D 视觉定位整合到同一框架中，并构建了对应的评测基准 M3SI。

### 研究问题
单目度量深度估计与 3D 视觉定位被视为单目 3D 空间理解（M3Sun）的两个互补基石，可为具身智能系统提供基础 3D 空间信息。但摘要指出，这两类互补任务通常由分离的框架分别完成，导致空间信息获取不灵活、不对齐，难以满足具身智能系统的需求。

### 核心思路/方法
- 提出统一的单目 3D 空间理解智能体 M3SunAgent，利用大语言模型（LLM）作为任务规划器进行空间视觉编程，灵活生成结构化程序并协调调用工具。
- 面向实例级度量深度估计：M3SunAgent 调用目标检测工具定位目标，使用深度估计工具在选定点上估计深度，并将这些预测聚合为实例级深度估计。
- 面向单目 3D 视觉定位：M3SunAgent 使用视觉语言模型（VLM）工具定位目标并输出基础空间属性，再结合反投影工具与维度提升工具预测其 3D 边界框。
- 构建 M3Sun Instance（M3SI）数据集，包含 2,910 个样本，用于评测。

### 主要贡献
- 提出统一的 M3SunAgent，以 LLM 作为任务规划器协调工具，缓解两个互补任务由分离框架处理所带来的空间信息不灵活与不对齐问题。
- 给出针对实例级度量深度估计与单目 3D 视觉定位的工具调用与程序化流程设计。
- 构建 M3SI 基准数据集，包含 2,910 个样本。
- 实验结果显示：在实例级单目度量深度估计评测中，M3SunAgent 在所有对比模型中表现最佳，52.61% 的预测实例深度误差低于 0.25（δ < 0.25）；在单目 3D 视觉定位评测中，取得 41.73% 的 3D mIoU，超过当时最优的 MonoVLM 模型 3.62%。

### 局限性
摘要未提供足够信息。摘要未说明 M3SunAgent 的具体失败情形、计算开销、对工具质量的依赖程度、M3SI 数据集的构成细节与泛化性验证等，因此无法基于现有信息分析其局限性。

### 阅读优先级
高。理由：该论文将单目度量深度估计与 3D 视觉定位统一到一个 LLM 驱动的智能体框架中，并给出定量提升与新建基准，对关注具身智能、单目 3D 空间理解、LLM 工具编排与视觉编程的研究方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular metric depth estimation and 3D visual grounding represent the two complementary cornerstones of monocular 3D spatial understanding (M3Sun), from which the fundamental 3D spatial information required by M3Sun can be acquired. However, these complementary tasks are generally conducted by separate frameworks, which pose challenges of inflexible and unaligned spatial information access for embodied intelligence systems. In this paper, we propose a unified agent for monocular 3D spatial understanding (M3SunAgent) that leverages a large language model (LLM) as a task planner for spatial visual programming, which flexibly generate structured programs and coordinate tools. For instance-level metric depth estimation task, M3SunAgent invokes an object detector tool to locate the target, estimates depth at selected points with a depth estimation tool, and aggregates these predictions into an instance-level depth estimate. We also construct the M3Sun Instance (M3SI) dataset, a benchmark with 2,910 samples for evaluation. For monocular 3D visual grounding task, M3SunAgent uses a vision-language model (VLM) tool to locate the target and output basic spatial attributes, then combines back-projection tool with a dimension-lifting tool to predict its 3D bounding box. Experimental results demonstrate the superior performance of M3SunAgent. Specifically, in evaluations of instance-level monocular metric depth estimation, M3SunAgent achieves the best performance among all compared models, 52.61% of predicted instances are distributed below depth error 0.25 ($δ< 0.25$). In evaluations of monocular 3D visual grounding, M3SunAgent demonstrates overall competitive performance than vision and VLM models, reaching a 3D mean intersection over union (mIoU) of 41.73% and exceeding the state-of-the-art MonoVLM model by 3.62%.

</details>

#### 2026-10-06 - Revar3r: gauge-aware perturbation uncertainty for feed-forward 3d reconstruction

**Authors:** Sammam Mahdi, Fariha Binta Salim, Rakin Bin Rabbani, Aniqua Nusrat Zereen
**Links:** [abs](https://arxiv.org/abs/2610.07883) - [pdf](https://arxiv.org/pdf/2610.07883)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** VGGT, MASt3R, feed-forward 3D reconstruction, 3D reconstruction, novel view synthesis, view synthesis, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Revar3r: gauge-aware perturbation uncertainty for feed-forward 3d reconstruction
- 作者：Sammam Mahdi, Fariha Binta Salim, Rakin Bin Rabbani, Aniqua Nusrat Zereen
- 出版日期：2026-10-06T07:29:54Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry、Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.07883 ；PDF https://arxiv.org/pdf/2610.07883

### 一句话总结
ReVar3R 针对前馈 3D 重建中的无训练扰动不确定性，提出在计算逐点方差前先把预测稳健配准到统一相似变换框架，以消除由对称性/规范（gauge）引起的伪不确定性，并在多个骨干与数据集上评估其对 AUSE 等指标的影响。

### 研究问题
论文关注前馈 3D 重建中“无训练扰动不确定性”的缺陷：当输出包含未被观察到的对称性时，多次运行之间的变化可能反映对称性（输出帧的旋转/规范差异），而不是真实误差。对于 point maps，摘要指出会导出一个闭式、与误差无关的方差项，该项随场景范围增长并可能淹没所需信号。因此问题是如何在不重训练、不修改冻结模型的前提下，获得更可靠的不确定性估计。

### 核心思路/方法
- 核心观察：一个正确重建的远距离点，即使冻结的 3D 模型处理等价输入，也可能因输出帧发生微小旋转而显得不确定。
- 诊断：对 point maps 推导出闭式、与误差无关的方差项，随场景范围增长，并预测其具有 $\|x_p\|^2$ 特征；模拟复现该效应，30 个真实 VGGT view-sets 均表现出该预测特征。
- 方法：ReVar3R 在计算逐点方差前，将预测稳健配准到共同相似框架；无需重训练或修改冻结模型。
- 可选步骤：使用留出划分进行校准与融合。
- 评估：在 VGGT、π3、MASt3R 三个骨干与六个数据集上，使用同一估计器比较 AUSE 与内置置信度，并分阶段评估无标签核心、无标签等权融合、留出权重融合以及加入内置信号后的表现；同时与训练过的 evidence head 比较。

### 主要贡献
- 指出无训练扰动不确定性在存在未观察对称性时可能测量的是规范/对称性变化而非误差。
- 对 point maps 推导并验证一个与误差无关、随场景范围增长的方差项，具有 $\|x_p\|^2$ 特征。
- 提出 ReVar3R：一种 gauge-aware 的稳健相似框架配准方法，用于计算逐点方差，无需重训练或修改冻结模型。
- 在 VGGT、π3、MASt3R 与六个数据集上评估，报告同一估计器在 18 个条件中的 15 个将 AUSE 降至内置置信度以下。
- 分阶段评估结果：无标签核心 11/18 胜，无标签等权融合 12/18，留出权重 14/18，加入内置信号 15/18。
- 与训练过的 evidence head 形成权衡：后者在幅度校准更好且在其训练域领先，而 ReVar3R 可跨骨干迁移而无需适配。
- 其排序改进点过滤，但不能检测稳定的系统偏差、不能帮助新视角合成、也不能跨域迁移校准。

### 局限性
- 摘要明确说明：不能检测稳定的系统偏差。
- 摘要明确说明：不 aid novel-view synthesis（不能帮助新视角合成）。
- 摘要明确说明：不能跨域迁移校准。
- 与训练过的 evidence head 相比，后者在幅度校准上更好并在其训练域领先。
- 其他潜在局限、实验细节、失败案例、计算开销、超参数敏感性等：摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接挑战前馈 3D 重建中无训练不确定性估计的一个基础问题（gauge/对称性导致伪方差），给出可诊断的闭式项与无需重训练的配准方法，并在多个主流骨干与数据集上报告了较系统的 AUSE 对比和分阶段增益；对关注 3D 基础模型不确定性、点图置信度与点过滤的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

A correctly reconstructed distant point appears uncertain even when a frozen 3D model processes equivalent inputs because its output frame rotates fractionally. This exposes a weakness of trainingfree perturbation uncertainty: when outputs contain an unobserved symmetry, run-to-run variation potentially reflects symmetry rather than error. Existing alternatives have trade-offs: built-in confidence is outperformed in most evaluated conditions, while trained evidential heads require modelspecific supervision. For point maps, this research derives a closed-form, error-independent variance term that grows with scene extent and potentially overwhelms the desired signal. Simulation reproduces the effect; all 30 real VGGT view-sets tested exhibit its predicted $\|x_p\|^2$ signature. ReVar3R robustly registers predictions to a common similarity frame before computing per-point variance, without retraining or modifying the frozen model. Optional calibration and fusion use a held-out split. Across VGGT, π3, and MASt3R on six datasets, the same estimator on every backbone lowers AUSE below built-in confidence in 15 of 18 conditions. The staged evaluation yields 11 of 18 wins for the label-free core, 12/18 for label-free equal-weight fusion, 14/18 with held-out weights, and 15/18 when the built-in signal is included. Against a trained evidential head, the result is a trade-off: the head calibrates magnitude better and leads in its training domain, whereas ReVar3R transfers across backbones without adaptation. Its ranking improves point filtering, but it does not detect stable systematic bias, aid novel-view synthesis, or transfer calibration across domains.

</details>

#### 2026-10-05 - VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges

**Authors:** Sungjae Choi, Hanna Bae, Sunghyun Baek, Junmo Kim
**Links:** [abs](https://arxiv.org/abs/2610.06594) - [pdf](https://arxiv.org/pdf/2610.06594)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges
- 作者：Sungjae Choi, Hanna Bae, Sunghyun Baek, Junmo Kim
- 出版日期：2026-10-05T16:07:04Z
- 分类：Geometry Foundation Models
- 链接：[摘要](https://arxiv.org/abs/2610.06594) / [PDF](https://arxiv.org/pdf/2610.06594)

### 一句话总结
VGGT-Bridge 通过在分块对齐框架中引入跨越远距离分块的长程“跳边”约束，在不重新训练的前提下缓解逐帧误差沿序列累积造成的漂移，并在多个里程计数据集上降低 ATE。

### 研究问题
前馈式视觉几何 Transformer（如 VGGT）能从图像集合中一次性重建稠密 3D 结构，但其注意力复杂度为二次型，难以扩展到数千帧的长序列。分块对齐框架通过将长序列切分为有重叠的分块，并把各分块局部重建拼接成位姿图来应对该问题；然而，现有方法只连接序列上相邻的分块，导致逐帧的小误差沿链条累积成大规模漂移。

### 核心思路/方法
论文提出 VGGT-Bridge，在相邻分块的顺序边之外，增加长程跳边，直接约束非相邻分块，且无需重新训练。具体做法是：在稀疏采样的粗分块上运行 VGGT，让每个粗分块把相距较远的细分块桥接成单一直接约束。作者还将 VGGT 的首帧尺度偏置转化为漂移校正：以反向顺序输入选定的粗分块；并采用一种回路感知策略，使该反向操作与已有的回路闭合保持兼容。

### 主要贡献
- 提出 VGGT-Bridge，用长程跳边突破仅依赖顺序相邻分块的位姿图结构，直接约束非相邻分块，且不需要重新训练。
- 通过稀疏粗分块运行 VGGT，将远距离细分块桥接为直接约束。
- 将 VGGT 的首帧尺度偏置转化为漂移校正，并通过回路感知策略保持与已有回路闭合的兼容性。
- 在 KITTI Odometry、Virtual KITTI 和 Waymo Open 上，相较于 SwiftVGGT 基线分别降低 ATE 28.3%、18.8% 和 10.0%，在所有分块对齐方法中取得最佳性能。

### 局限性
摘要未提供足够信息。摘要未说明方法对粗分块采样策略的敏感性、反向输入带来的额外计算或工程代价、在不同序列长度或不同重叠比例下的表现，也未提供失败案例或与所有已有方法的完整对比细节。

### 阅读优先级
高。理由：该工作针对前馈视觉几何模型在长序列重建中的可扩展性与漂移累积问题，提出无需重训练的长程约束机制，并在多个自动驾驶里程计数据集上报告了明确且一致的 ATE 改进，属于“Geometry Foundation Models”方向中兼顾方法简洁性与实证效果的研究，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward visual geometry transformers such as VGGT reconstruct dense 3D structure from images in a single forward pass, simplifying multi-view 3D reconstruction. However, their quadratic attention complexity makes them difficult to scale to long sequences with thousands of frames. Chunk-and-align frameworks address this by splitting a long sequence into overlapping chunks and stitching their local reconstructions into a pose graph. Yet existing methods connect only sequentially adjacent chunks, so small per-frame errors accumulate along the chain into large-scale drift. To move beyond sequential edges, we propose VGGT-Bridge, which adds long-range skip edges that directly constrain non-adjacent chunks without retraining. By running VGGT on sparsely sampled coarse chunks, each coarse chunk bridges distant fine chunks into a single direct constraint. We further turn VGGT's first-frame scale bias into a drift correction by feeding selected coarse chunks in reverse, and a loop-aware policy keeps this reversal compatible with existing loop closures. VGGT-Bridge reduces ATE by 28.3% on KITTI Odometry, 18.8% on Virtual KITTI, and 10.0% on Waymo Open over the SwiftVGGT baseline, achieving the best performance among all chunk-and-align methods.

</details>

#### 2026-10-05 - MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs

**Authors:** Yun Jiang, Bo Zheng, Yingying Zhang, Xueming Xiao, Tao Hu, Hutao Cui, Zhiguo Meng, Ke Gao, Yang Gao, Meibao Yao
**Links:** [abs](https://arxiv.org/abs/2610.07110) - [pdf](https://arxiv.org/pdf/2610.07110)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, 3D reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs
- 作者：Yun Jiang, Bo Zheng, Yingying Zhang, Xueming Xiao, Tao Hu, Hutao Cui, Zhiguo Meng, Ke Gao, Yang Gao, Meibao Yao
- 出版日期：2026-10-05T15:46:50Z
- 分类：Geometry Foundation Models（主）；Neural Scene Representations & Rendering（次）
- 链接：https://arxiv.org/abs/2610.07110 ；PDF: https://arxiv.org/pdf/2610.07110

### 一句话总结
MoonGS 是首个面向月球场景的前馈式 3D 高斯泼溅框架，仅用两张输入图像即可单次前向预测像素对齐的高斯基元，在稀疏、弱纹理的月球数据上实现无需逐场景优化的高质量新视角渲染。

### 研究问题
从稀疏的巡视器图像中进行高质量月球地形三维重建，对自主月球探测至关重要，但面临三个挑战：视点重叠不足、表面纹理弱、数据量有限。摘要指出该问题在现有条件下仍具挑战性，MoonGS 正是针对这些困难提出。

### 核心思路/方法
- 任务设定：仅输入两张图像，单次前向预测像素对齐的高斯基元，直接渲染逼真的新视角，无需任何逐场景优化。
- 骨干设计：采用可适配的骨干结构，无缝集成先进视觉基础模型以提取鲁棒的深度特征。
- 语义先验：以两种方式引入语义先验——将语义线索与视觉特征融合以精化高斯参数估计；采用语义排序损失对背景深度进行正则化。
- 稀疏观测增强：采用熵引导的启发式重采样策略，以可忽略的开销选择最具信息量的远距离视点来扩充稀疏观测。
- 评测：在 LuSNAR 基准与自建合成弱纹理数据集 MoonBlender 上验证，并展示可有效利用包括 VGGT 在内的先进骨干以显著提升性能；在嫦娥任务影像上做定性评估。

### 主要贡献
- 提出 MoonGS，摘要称为首个面向月球场景的前馈式 3D 高斯泼溅框架，仅凭两张图像即可实现无需逐场景优化的逼真新视角渲染。
- 设计可适配骨干以集成先进视觉基础模型，提取鲁棒深度特征。
- 以融合语义线索精化高斯参数、并以语义排序损失正则化背景深度两种方式引入语义先验。
- 提出熵引导的启发式重采样策略，以极低开销选取信息量最大的远距离视点来增强稀疏观测。
- 实验显示在 LuSNAR 基准与 MoonBlender 数据集上超越前馈式 NeRF/3DGS 基线：PSNR +4.9 dB、SSIM +0.29、LPIPS 降低 40%，并保持亚秒级推理；同时验证框架可有效利用包括 VGGT 在内的先进骨干提升性能，并在嫦娥任务影像上取得对比方法中最佳的视觉质量，表明对真实月球数据的鲁棒性。
- 摘要声明源代码与数据集已公开于 https://github.com/InRobots/MoonBlender 。

### 局限性
- 摘要未提供足够信息说明方法在何种失败场景下失效，或对极端光照、更大规模场景、更多输入图像时的表现。
- 摘要未提供足够信息说明计算资源、显存占用、训练数据规模与训练时长等细节。
- 摘要未提供足够信息说明定量实验的具体基准划分、对比方法清单与消融实验细节。
- 摘要未提供足够信息说明在真实嫦娥影像上是否仅做定性评估、是否存在定量真实数据结果。
- 摘要未提供足够信息说明“亚秒级推理”所对应的硬件平台与输入分辨率。

### 阅读优先级
高。理由：该工作针对月球探测这一明确且困难的应用场景，提出前馈式 3DGS 新框架，报告了相对前馈式 NeRF/3DGS 基线的显著定量提升（PSNR +4.9 dB、SSIM +0.29、LPIPS 降低 40%）并保持亚秒级推理，同时涉及视觉基础模型集成、语义先验与稀疏观测增强等可迁移方法要素，且声明代码与数据集公开，对三维重建、机器人感知与行星探测交叉方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

High-quality 3D reconstruction of lunar terrain from sparse rover images is indispensable for autonomous lunar exploration, but remains challenging because viewpoint overlap is insufficient, surface textures are weak, and data volume is limited. We propose MoonGS, the first feed-forward 3D Gaussian Splatting framework tailored to lunar scenes. Given only two input images, MoonGS predicts pixel-aligned Gaussian primitives in a single forward pass and renders photorealistic novel views without any per-scene optimization. MoonGS (i) adopts an adaptable backbone design that seamlessly integrates advanced vision foundation models to extract robust depth features; (ii) integrates semantic priors in two manners: merging semantic cues with visual features to refine Gaussian parameter estimation, and adopting a semantic ranking loss that regularizes background depth; and (iii) employs an entropy-guided heuristic resampling strategy to augment sparse observations by selecting the most informative distant viewpoints with negligible overhead. Experiments on the LuSNAR benchmark and our synthetic weak-texture MoonBlender dataset show that MoonGS surpasses state-of-the-art feed-forward NeRF/3DGS baselines by +4.9 dB PSNR, +0.29 SSIM, and 40\% lower LPIPS while maintaining sub-second inference. Furthermore, we validate the broad applicability of our framework by demonstrating that it effectively leverages state-of-the-art backbones, including VGGT, to significantly boost performance. Qualitative evaluations on Chang'e mission imagery also show the best visual quality among compared methods, indicating robustness on real lunar data. The source code and dataset are publicly available at https://github.com/InRobots/MoonBlender.

</details>

#### 2026-10-04 - Deep Prior Learning for Embodied Perception

**Authors:** Yimou Wu, Jiaxin Guo, Yun-hui Liu, Zheng Li
**Links:** [abs](https://arxiv.org/abs/2610.05531) - [pdf](https://arxiv.org/pdf/2610.05531)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Deep Prior Learning for Embodied Perception
- 作者：Yimou Wu, Jiaxin Guo, Yun-hui Liu, Zheng Li
- 出版日期：2026-10-04T20:53:38Z
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2610.05531

### 一句话总结
论文提出基于 VGGT 的 VPGGT 框架，通过先验残差连接与 Metric Global Attention，在具身感知中更有效地利用带噪相机位姿、内参和深度先验，以缓解先验稀释并恢复物理尺度。

### 研究问题
具身系统需要超越单纯图像的几何感知。现有前馈 3D 模型虽引入相机位姿、内参和深度等几何先验，但处理带噪位姿、保持准确先验以及恢复物理尺度，并不仅仅是直接接受这些输入即可解决。论文关注的核心问题之一是“先验稀释”：预测结果反而不如所提供的位姿先验准确。

### 核心思路/方法
论文提出 Vision-Prior Geometry Grounded Transformer（VPGGT），这是一个基于 VGGT 的框架，并在 OmniVGGT 基础上扩展，用于先验感知的具身感知。方法包括：
- 从真实轨迹出发构造受传感器启发的位姿扰动，用于训练；扰动仅针对相机位姿，提供的相机内参和深度不额外加噪。
- 引入无参数的 prior residual connection（PRC），以缓解 prior dilution。
- 引入 Metric Global Attention，使全局尺度 token 条件化于可用的位姿尺度和深度尺度，并为几何输出预测共享的度量缩放因子。

### 主要贡献
- 提出 VPGGT，一个基于 VGGT 并扩展 OmniVGGT 的先验感知具身感知框架。
- 构造面向相机位姿的传感器启发式扰动训练设定。
- 提出无参数 prior residual connection，用于缓解预测精度低于输入位姿先验的先验稀释问题。
- 提出 Metric Global Attention，用于预测共享度量缩放因子并恢复物理尺度。
- 在四个数据集上的实验表明，当所有视角提供相机先验时，在精确位姿和受扰动位姿下，PRC 相比匹配训练基线提升了平移方向准确率和联合位姿 AUC。

### 局限性
摘要未提供足够信息说明方法在更多模态、更复杂噪声类型或真实部署场景中的表现。摘要未提供足够信息说明推理效率、计算开销、失败案例以及与其他基线方法的完整比较细节。摘要未提供足够信息说明四个数据集的具体构成、评价协议和消融实验完整结果。

### 阅读优先级
中。理由：论文主题集中在具身感知、几何先验利用和前馈 3D 模型扩展，对关注 VGGT/OmniVGGT、位姿先验鲁棒性和度量尺度恢复的研究者具有直接相关性；但摘要仅给出方法框架与部分实验结论，未提供完整实验细节和外部验证信息，因此不适合作为仅凭摘要即可深入复现或全面评估的优先阅读材料。

</details>

<details>
<summary>Abstract</summary>

Embodied systems need geometric perception that exploits available observations beyond images alone. Recent feed-forward 3D models incorporate geometric priors, including camera poses, intrinsics, and depth. However, handling noisy poses, preserving accurate priors, and recovering physical scale require more than simply accepting these inputs. We introduce \emph{Vision-Prior Geometry Grounded Transformer} (VPGGT), a VGGT-based framework that extends OmniVGGT for prior-aware embodied perception. We formulate sensor-motivated pose corruptions from ground-truth trajectories for training and introduce a parameter-free \emph{prior residual connection} (PRC) to mitigate \emph{prior dilution}, where predictions are less accurate than their supplied pose priors. Our noise formulation targets camera poses; supplied intrinsics and depth receive no additional corruption. We further introduce \emph{Metric Global Attention}, which conditions a global scale token on available pose and depth scales and predicts a shared metric scaling factor for the geometric outputs. Experiments across four datasets show that \emph{PRC} improves translation-direction accuracy and joint pose AUC over a matched training baseline when camera priors are provided for all views, under both exact and corrupted poses. These results support explicit prior access during refinement as a useful addition to feature-level conditioning.

</details>

#### 2026-10-01 - MVDG: Efficient Multi-view 3D Disambiguation on Unconstrained Real-World Images

**Authors:** Hanyuan Xiao, Gonglin Chen, Haolin Xiong, Wenbin Teng, Haiwei Chen, Yajie Zhao
**Links:** [abs](https://arxiv.org/abs/2610.01098) - [pdf](https://arxiv.org/pdf/2610.01098)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, structure from motion, SfM, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MVDG: Efficient Multi-view 3D Disambiguation on Unconstrained Real-World Images
- 作者：Hanyuan Xiao, Gonglin Chen, Haolin Xiong, Wenbin Teng, Haiwei Chen, Yajie Zhao
- 出版日期：2026-10-01T05:41:05Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.01098) / [PDF](https://arxiv.org/pdf/2610.01098)

### 一句话总结
MVDG 是一个基于 3D 基础模型 VGGT 的可扩展多视角消歧框架，通过单次编解码多视角图像减少对成对比较的依赖，在保持相近成对精度的同时提升 SfM 精度与推理速度。

### 研究问题
论文关注的是“doppelgangers”问题：不同但视觉上相似的 3D 表面之间会产生虚假匹配，这是大规模、真实场景下 3D 重建与视觉定位的基础性障碍。既有方法多用成对分类器缓解该问题，但摘要指出这种设计限制了多视角上下文推理，并给下游 SfM 带来 O(n^2) 推理复杂度。

### 核心思路/方法
- 提出 MVDG，一个可扩展的多视角消歧框架，构建在 3D 基础模型 VGGT 之上，可对任意数量的多视角图像进行联合推理。
- 通过引入 3D 感知的多视角特征，在单次前向过程中编码和解码视图，从而减少对成对比较的依赖。
- 摘要提到直接对 VGGT 进行多视角微调在噪声监督下可能不稳定；受 Doppelgangers 中标签歧义启发，作者从 AerialMegaDepth 构建伪成对训练集，并发现采样子集上的微调能带来稳定优化和对留出场景的较强泛化。
- 由于完整 SfM 评估即使使用 GLOMAP 等更快流程仍昂贵，作者处理伪成对数据集以进行高效验证，并推导常规 SfM 指标与该伪成对测试分类精度之间的预测关系。

### 主要贡献
- 提出 MVDG 多视角 3D 消歧框架，减少对成对分类设计的依赖，并支持任意数量多视角图像的联合推理。
- 针对 VGGT 多视角微调在噪声监督下的不稳定问题，构建基于 AerialMegaDepth 的伪成对训练集，并展示采样子集微调可实现稳定优化与对留出场景的泛化。
- 提出一种高效验证方式：处理伪成对数据集，并推导常规 SfM 指标与伪成对测试分类精度之间的预测关系，以规避昂贵完整 SfM 评估。
- 摘要声称实验表明该方法在保持可比成对精度的同时，相较基线提升了 SfM 精度与推理速度。

### 局限性
- 摘要未提供足够信息说明 MVDG 在何种具体场景、数据集规模或硬件条件下失效或性能下降。
- 摘要未提供足够信息说明伪成对训练集与真实成对监督之间的差距及其对最终性能的影响。
- 摘要未提供足够信息说明推导出的 SfM 指标与伪成对分类精度之间预测关系的适用范围与误差边界。
- 摘要未提供足够信息说明方法对 VGGT 基础模型的依赖程度，以及替换基础模型后的泛化表现。
- 摘要未提供足够信息给出完整实验设置、基线细节、定量结果与消融研究。

### 阅读优先级
中。理由：该工作针对真实场景 3D 重建与视觉定位中的多视角消歧问题，提出基于 3D 基础模型的可扩展框架，并涉及训练稳定性与高效评估，主题与 Geometry Foundation Models 和 3D Reconstruction & Multi-view Geometry 相关。但当前仅有摘要与元数据，缺少具体实验细节、定量结果和与基线的完整对比，因此适合作为方向性了解或后续精读候选，而非仅凭摘要即可高置信度判断其实际影响。

</details>

<details>
<summary>Abstract</summary>

Illusory matches between distinct yet visually similar 3D surfaces--doppelgangers--remain a fundamental obstacle for large-scale, in-the-wild 3D reconstruction and visual localization. Prior work mitigates this issue with pairwise classifiers, but this design limits multi-view contextual reasoning and incurs O(n^2) inference complexity for downstream structure-from-motion (SfM). We present MVDG, a scalable multi-view disambiguation framework built on the 3D foundation model VGGT, which jointly reasons over an arbitrary number of multiview images. By incorporating 3D-aware multi-view features, our method reduces dependence on pairwise comparisons by encoding and decoding views in a single pass. We further observe that direct multi-view fine-tuning of VGGT can be unstable under noisy supervision; motivated by label ambiguity in Doppelgangers, we construct a pseudo-pairwise training set from AerialMegaDepth and show that fine-tuning on sampled subsets yields stable optimization and strong generalization to held-out scenes. Finally, because full SfM evaluation (even with faster pipelines such as GLOMAP) remains expensive, we process a pseudo-pairwise dataset for efficient validation; we derive a predictive relationship between regular SfM metrics and the classification accuracy on this pseudo-pairwise test. Experiments show that our method achieves comparable pairwise accuracy while improving both SfM accuracy and inference speed over baselines.

</details>

#### 2026-10-01 - VASC: Value-Aware Sparse Attention with Cross-Layer Memory for Efficient 3D Reconstruction

**Authors:** Junyi Wu, Fanqing Kong, Leyang Chen, Shaoqiu Zhang, Yulun Zhang
**Links:** [abs](https://arxiv.org/abs/2610.01013) - [pdf](https://arxiv.org/pdf/2610.01013)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, scene reconstruction, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VASC: Value-Aware Sparse Attention with Cross-Layer Memory for Efficient 3D Reconstruction
- 作者：Junyi Wu, Fanqing Kong, Leyang Chen, Shaoqiu Zhang, Yulun Zhang
- 出版日期：2026-10-01T03:57:47Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.01013 ；PDF https://arxiv.org/pdf/2610.01013

### 一句话总结
VASC 面向 VGGT 等前馈式 3D 视觉模型，提出免训练的稀疏注意力方法，通过“值感知块选择”与“执行感知跨层记忆”在固定计算预算下减少冗余注意力，从而在 7Scenes 与 NeuralRGB-D 上改善位姿估计和重建质量，并相较稠密 VGGT 实现最高约 2.29 倍推理加速。

### 研究问题
前馈式 3D 视觉模型（如 VGGT）将相机估计与稠密场景重建统一在单次前向中，但其二次复杂度的全局注意力在长图像序列上代价高昂。现有稀疏方法可能偏向被高度关注但“值”上冗余的区域，从而未能有效保留真正有区分度的内容。论文即针对这一效率与信息选择问题展开。

### 核心思路/方法
论文提出 VASC，一种免训练的稀疏注意力方法，核心由两部分组成：
1. 值感知块选择：将池化后的 query-key 相关性与邻近 value 对比度结合，用于减少冗余，同时保留与 query 相关且具有区分性的内容。
2. 执行感知跨层记忆：跟踪跨层尚未被服务到的需求，并根据实际执行情况更新该状态，使先前未被充分覆盖的块也能在固定计算预算下参与竞争。

### 主要贡献
- 提出 VASC，一种免训练的稀疏注意力方法，结合值感知块选择与执行感知跨层记忆。
- 设计值感知块选择机制，融合池化 query-key 相关性与邻近 value 对比，以降低冗余并保留 query 相关且具区分性的内容。
- 设计跨层记忆机制，跟踪并更新跨层未服务需求，使先前未被充分服务的块在固定计算预算下仍可竞争。
- 在 7Scenes 和 NeuralRGB-D 上，结合 VGGT 与 π³ 的实验显示，相较 FasterVGGT 在位姿估计与重建质量上有改进，并相较稠密 VGGT 实现最高 2.29 倍推理加速。代码已公开。

### 局限性
摘要未提供足够信息。论文未在给定摘要中说明方法在更长序列、不同模型规模或更广泛数据集上的表现，也未给出失败案例、计算预算设置细节或与更多稀疏基线方法的系统比较。

### 阅读优先级
中。理由：该工作针对前馈式 3D 视觉模型中的全局注意力效率瓶颈，提出免训练稀疏注意力与跨层记忆机制，问题定位清晰，且报告了位姿估计、重建质量与推理加速方面的结果；但其方法细节、实验广度与局限性在摘要中披露有限，是否具有广泛适用性需进一步阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D vision models such as VGGT have achieved remarkable progress, unifying camera estimation and dense scene reconstruction in a single pass. However, their quadratic global attention makes long image sequences expensive, while existing sparse methods may favor highly attended yet value-redundant regions. To address these limitations, we introduce VASC, a training-free sparse attention method combining value-aware block selection and execution-aware cross-layer memory. Our value-aware block selection integrates pooled query--key relevance with neighboring value contrast, reducing redundancy while preserving query-relevant and distinctive content. Cross-layer memory tracks unserved demand across layers and updates this state according to actual execution, enabling previously underserved blocks to compete under a fixed computation budget. Experiments on 7Scenes and NeuralRGB-D with VGGT and $π^3$ demonstrate improved pose estimation and reconstruction quality compared with FasterVGGT, together with up to $2.29\times$ faster inference than dense VGGT. Code is available at https://github.com/kosakayamahoo-design/VASC.

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-04 - DynaMesh: Dynamic 3D Texture Generation

**Authors:** Raj Hansini, Guan Chen, Rana Hanocka, Itai Lang
**Links:** [abs](https://arxiv.org/abs/2610.05529) - [pdf](https://arxiv.org/pdf/2610.05529)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D, video-to-4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DynaMesh: Dynamic 3D Texture Generation
- 作者：Raj Hansini, Guan Chen, Rana Hanocka, Itai Lang
- 出版日期：2026-10-04T20:52:25Z
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2610.05529

### 一句话总结
DynaMesh 提出一种在保持三维网格几何不变的前提下，根据文本提示生成随时间演变的动态纹理/外观效果的方法。

### 研究问题
论文关注如何在三维网格上生成“传播式”的视觉动态效果。已有动态三维内容生成工作主要关注几何与位置的运动会改变而外观保持不变；而纹理生成方法则把外观作为固定表面属性绘制到形状上，而非一个演变过程。两者都没有处理视觉效果在三维物体上传播的问题。摘要指出，直接用“视频模型 + 逐帧图像到三维生成”的自然路线会因后者没有时间概念，导致序列闪烁、丢失效果细节，并且每一视频帧都产生不同网格。

### 核心思路/方法
方法以无纹理形状和描述效果的文本提示为输入，输出几何不变、纹理逐帧变化的单一网格。具体做法是：先以网格渲染图和文本提示为条件驱动视频模型，得到参考视频；再对视频运行一个冻结的图像到三维生成器，但做了两处改动：一是每帧的条件在时间窗口上进行混合，二是针对每个形状拟合低秩适配器以恢复丢失的细节。网格在整个序列中只编码一次，因此几何按构造保持恒定，最终输出为单一网格加上每一帧的纹理。

### 主要贡献
- 提出 DynaMesh，一种面向三维网格的动态纹理生成方法，在几何不变的情况下产生随时间演变的外观。
- 针对视频到三维逐帧生成导致的闪烁、细节丢失和网格不一致问题，提出时间窗口条件混合与逐形状低秩适配器两项改动。
- 通过只编码一次网格，使几何恒定成为构造性保证，输出为单一网格与逐帧纹理。
- 摘要称其在多种物体和效果上显著优于近期 video-to-4D 与纹理化方法，并能将时间效果泛化到训练中未见过的不同形状。

### 局限性
摘要未提供足够信息。（论文未在摘要中明确讨论失败情形、计算开销、对提示或视频模型的依赖限制，以及泛化能力的边界等。）

### 阅读优先级
中。理由：该工作处于动态三维内容生成与三维纹理生成的交叉点，问题定义清晰，方法思路具有针对性；但摘要未给出定量结果、实验设置与局限分析，若读者关注动态纹理或 video-to-4D 方向，可优先阅读原文以核实实验细节与泛化表现。

</details>

<details>
<summary>Abstract</summary>

We present DynaMesh, a dynamic texture generation method for 3D meshes. Given a textureless shape and a text prompt describing an effect, our method produces an appearance that evolves while the object's geometry remains unchanged. Previous works on dynamic 3D content generation have focused on motion, where an object's geometry and position change while keeping its appearance the same. Methods on texture generation sit on the other side of the problem, painting appearance onto a shape as a fixed surface property and not as an evolving process. Neither addresses a visual effect that propagates on a 3D object. A natural route consists of two generators: a video model that shows the effect from a single view, and an image-to-3D generator that lifts each frame to 3D. However, the latter has no notion of time, so running it per video frame produces a sequence that flickers, loses effect details, and yields a different mesh at every video frame. Our method addresses these failures by conditioning a video model on a render of the mesh and the prompt to obtain a reference video, then running a frozen image-to-3D generator on the video with two changes. The conditioning of each frame is blended over a temporal window, and low-rank adapters are fit per shape to restore the lost details. The mesh is encoded once for the whole sequence, so geometry is constant by construction, and the output is a single mesh with a texture per frame. Applied to various objects and effects, DynaMesh substantially improves over recent video-to-4D and texturing methods, and can generalize its temporal effect to different shapes never seen during training. Our project page is at https://threedle.github.io/dynamesh/.

</details>

#### 2026-10-04 - Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting

**Authors:** Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu
**Links:** [abs](https://arxiv.org/abs/2610.05289) - [pdf](https://arxiv.org/pdf/2610.05289)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting
- 作者：Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu
- 出版日期：2026-10-04T15:07:47Z
- 分类：主分类为 Dynamic / 4D Reconstruction；次分类为 Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2610.05289；PDF 链接 https://arxiv.org/pdf/2610.05289；代码链接 https://xiaobiaodu.github.io/mobile-4dgs-project/

### 一句话总结
Mobile-4DGS 提出一个面向移动端的统一轻量框架，用于静态与动态高斯表示的实时渲染，通过压缩外观、精简高斯基元以及显式紧凑 4D 表示来降低存储与逐帧计算开销。

### 研究问题
论文关注的问题是：尽管 3D Gaussian Splatting（3DGS）在新视角合成上表现突出，但将静态和动态高斯表示部署到资源受限的移动设备上仍然困难，主要原因包括存储负担重、高斯基元冗余以及逐帧计算代价高。

### 核心思路/方法
论文提出 Mobile-4DGS，一个统一的轻量框架，目标是在移动平台上实现高保真实时的静态与动态高斯渲染。方法层面包括：
- 紧凑外观建模：引入 Monte Carlo Specular Energy Aggregator，将高阶辐射残差压缩到一阶 Spherical Harmonics（SH）；并结合 Attribute-Conditioned SH Enhancement 模块，其预测偏移在推理前预先烘焙。
- 基元精简：提出 Multi-View Alpha-Based Densification and Pruning 策略，在保持多视角一致性的同时抑制冗余高斯基元。
- 动态场景表示：构建紧凑显式 4D 表示，包括二阶高斯运动、可学习时间支撑以及二值静态-动态划分，从而无需运行时变形网络即可进行连续时间建模。
- 播放效率优化：基于静态-动态划分，提出 Depth-Order Certificate，选择性复用此前已提交的深度顺序，以减少播放过程中的重投影、排序、合并与索引缓冲区更新。

### 主要贡献
- 提出统一的轻量框架 Mobile-4DGS，面向移动端静态与动态高斯实时渲染。
- 引入 Monte Carlo Specular Energy Aggregator 与 Attribute-Conditioned SH Enhancement，用于压缩外观表示，并将预测偏移预烘焙以降低推理开销。
- 提出 Multi-View Alpha-Based Densification and Pruning，减少冗余高斯基元并维持多视角一致性。
- 构建紧凑显式 4D 表示，通过二阶高斯运动、可学习时间支撑和二值静态-动态划分，实现无需运行时变形网络的连续时间建模。
- 提出 Depth-Order Certificate，复用已提交深度顺序，以减少动态播放中的重投影、排序、合并与索引缓冲区更新。
- 摘要称在静态与动态场景上的大量实验表明，Mobile-4DGS 显著降低存储和渲染开销，同时保持有竞争力的视觉质量，并支持移动设备上的实时 3D 与 4D 高斯 Splatting。

### 局限性
摘要未提供足够信息。摘要未给出具体实验平台、移动设备型号、帧率、存储压缩比例、视觉质量指标、失败案例或方法适用范围等细节，因此无法基于摘要判断其局限性。

### 阅读优先级
高。理由：该论文聚焦 3DGS 在移动端部署中的存储、冗余基元和逐帧计算瓶颈，并同时覆盖静态与动态高斯表示，属于动态/4D 重建与神经场景表示渲染交叉方向；若关注移动端实时高斯渲染、4D 表示压缩或高效动态场景建模，该工作具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable performance in novel view synthesis, yet deploying both static and dynamic Gaussian representations on resource-constrained mobile devices remains challenging due to heavy storage, redundant primitives, and costly per-frame computation. We present Mobile-4DGS, a unified lightweight framework for high-fidelity real-time static and dynamic Gaussian rendering on mobile platforms. For compact appearance modeling, we introduce a Monte Carlo Specular Energy Aggregator that compresses high-order radiance residuals into the first-order Spherical Harmonics (SH), together with an Attribute-Conditioned SH Enhancement module whose predicted offsets are pre-baked before inference. We further propose a Multi-View Alpha-Based Densification and Pruning strategy to suppress redundant primitives while maintaining multi-view consistency. For dynamic scenes, we develop a compact explicit 4D representation by constructing second-order Gaussian motion, learnable temporal support, and a binary static-dynamic partition, enabling continuous-time modeling without runtime deformation networks. Based on this partition, a Depth-Order Certificate selectively reuses previously committed depth orders to reduce re-projection, sorting, merging, and index-buffer updates during playback. Extensive experiments on static and dynamic scenes demonstrate that Mobile-4DGS substantially reduces storage and rendering overhead while maintaining competitive visual quality, enabling real-time 3D and 4D Gaussian Splatting on mobile devices. \textcolor{magenta}{\href{https://xiaobiaodu.github.io/mobile-4dgs-project/}{Code has been released: https://xiaobiaodu.github.io/mobile-4dgs-project/}}.

</details>

#### 2026-10-01 - Dyna3: VLM-Guided Training-Free 4D Reconstruction via Depth Foundation Models

**Authors:** Xinhao Xiang, Weiyang Li, Zhijie Zheng, Abhijeet Rastogi, Jiawei Zhang
**Links:** [abs](https://arxiv.org/abs/2610.01286) - [pdf](https://arxiv.org/pdf/2610.01286)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 4D reconstruction, dynamic scene reconstruction, scene reconstruction, pose estimation, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dyna3: VLM-Guided Training-Free 4D Reconstruction via Depth Foundation Models
- 作者：Xinhao Xiang, Weiyang Li, Zhijie Zheng, Abhijeet Rastogi, Jiawei Zhang
- 出版日期：2026-10-01T08:24:21Z
- 分类：Dynamic / 4D Reconstruction（次要分类：3D Reconstruction & Multi-view Geometry）
- 链接：摘要页 https://arxiv.org/abs/2610.01286 ；PDF https://arxiv.org/pdf/2610.01286

### 一句话总结
Dyna3 是一个无需微调的训练无关框架，将原本面向静态场景的深度基础模型 DA3 扩展到 4D 动态场景重建，并通过 VLM 引导 SAM 3 实现实例级动态物体分割。

### 研究问题
现有深度基础模型（如 Depth Anything 3，DA3）虽然在多视图深度估计上表现突出，但假设场景是静态 3D 的，因此在真实动态环境中适用性受限。已有训练无关的 4D 方法（如 Easi3R、VGGT4D）依赖经过对应关系训练的主干网络，其注意力机制编码了跨帧匹配信息，而 DA3 这类纯深度模型不具备这一性质。因此问题在于：如何在不进行微调的前提下，把纯深度的基础模型用于动态 4D 重建。

### 核心思路/方法
- 关键观察：DA3 的跨视图特征虽然只针对深度一致性训练，但在结合跨帧最佳匹配特征搜索后，隐含地编码了可区分运动的信号——静态表面能在全局找到一致匹配，动态物体则不能。
- 采用视觉语言模型（VLM）自动生成场景特定的语义提示，用于 SAM 3，实现精确的实例级分割，从而区分“哪些物体在动”与“存在哪些物体”。
- 重建时将场景解耦为跨帧对齐的静态背景与逐帧动态点云两部分。

### 主要贡献
- 提出 Dyna3，一个无需任何微调、训练无关的框架，将 DA3 扩展到 4D 动态场景重建。
- 揭示并利用了 DA3 跨视图特征中隐含的运动判别信号，通过跨帧最佳匹配特征搜索加以利用。
- 引入 VLM 生成场景特定语义提示驱动 SAM 3，实现实例级分割，区分运动物体与静态存在物体。
- 在四个数据集上的实验表明：在动态物体分割上以 +5.5pp J-Mean 超过当前最优 VGGT4D；姿态估计最高提速 13 倍，4D 重建提速 3 倍，内存降低 4 至 8 倍；有望支持更密集的时间采样。

### 局限性
摘要未提供足够信息。摘要未说明方法在何种场景下会失效、对 VLM 或 SAM 3 错误的敏感性、所依赖的假设边界，也未给出具体数据集名称、失败案例分析或计算资源下限等细节。

### 阅读优先级
高。理由：该工作针对深度基础模型无法处理动态场景这一明确痛点，提出无需微调的 4D 重建方案，并在摘要中给出了相对当前最优方法的定量提升（分割 +5.5pp、姿态最高 13 倍加速、重建 3 倍加速、内存降低 4 至 8 倍），同时结合了 VLM 与 SAM 3 的语义引导思路，对动态/4D 重建及多视图几何方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent depth foundation models like Depth Anything 3 (DA3) achieve remarkable multi-view depth estimation but assume static 3D scenes, limiting their applicability to real-world dynamic environments. Existing training-free 4D methods like Easi3R and VGGT4D rely on correspondence-trained backbones whose attention encodes cross-frame matching, a property absent in depth-only models like DA3. We present Dyna3, a training-free framework that extends DA3 for 4D dynamic scene reconstruction without any fine-tuning. Our key insight is that DA3's cross-view features, though trained only for depth consistency, implicitly encode motion-discriminative signals when combined with best-match feature search across frames. Its static surfaces find consistent matches globally, while dynamic objects cannot. We further adopt vision-language models (VLM) to automatically generate scene-specific semantic prompts for SAM 3, enabling precise instance-level segmentation that distinguishes which objects move from what objects exist. For reconstruction, we decouple the scene into a cross-frame aligned static background and per-frame dynamic point clouds. Experiments on four datasets demonstrate that Dyna3 surpasses correspondence-trained methods with +5.5pp J-Mean over state-of-the-art VGGT4D on dynamic object segmentation, while achieving up to 13x faster pose estimation and 3x faster 4D reconstruction with 4 to 8x lower memory. Dyna3 could therefore enable much denser temporal sampling that prior methods cannot support.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-06 - Digital Twin-Driven Real2Sim2Real: Simulator-Conditioned Generation via Paired Driving-Scene Reconstruction

**Authors:** Hojun Lim, Hyeongseok Jeon, Donghyun Kim, Soonyoung Jung, Heecheol Yoo
**Links:** [abs](https://arxiv.org/abs/2610.08339) - [pdf](https://arxiv.org/pdf/2610.08339)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, autonomous driving, driving scene, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Digital Twin-Driven Real2Sim2Real: Simulator-Conditioned Generation via Paired Driving-Scene Reconstruction
- 作者：Hojun Lim, Hyeongseok Jeon, Donghyun Kim, Soonyoung Jung, Heecheol Yoo
- 出版日期：2026-10-06T13:36:50Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.08339 ；PDF https://arxiv.org/pdf/2610.08339

### 一句话总结
论文提出数字孪生驱动的 Real2Sim2Real 流程 DT-R2S2R：先在带地理坐标的数字孪生中重建真实驾驶片段以对齐模拟器渲染，再以此条件化扩散模型，从而在无目标区域真实图像参与训练的情况下，为新的目标区域合成带免费标注的逼真驾驶数据。

### 研究问题
基于相机的自动驾驶 3D 感知依赖大规模带标注数据集，而将系统部署到新的目标区域通常需要重新采集与标注数据。现有生成式增广方法存在根本取舍：标签条件方法要消耗它本意替代的标注，模拟器条件方法虽提供免费标注，却缺乏对特定真实环境的视觉接地。论文因此研究：数字孪生驱动的 Real2Sim2Real 流程能在多大程度上替代目标区域的真实数据。

### 核心思路/方法
论文构建 DT-R2S2R 流程。第一步为 DT-R2S：在带地理参照的数字孪生（DT）中重建已录制的驾驶片段。第二步为 DT-S2R：以几何对齐的模拟器渲染为条件，训练扩散模型，形成以数字孪生为接地的 Sim2Real 模型。该模型可在数字孪生覆盖范围内的已重建场景以及新模拟器场景中，依据低成本且带地理参照的模拟器数据合成逼真驾驶图像。生成数据的有效性在多种 3D 检测器上验证。

### 主要贡献
- 提出数字孪生驱动的 Real2Sim2Real 流程 DT-R2S2R，用带地理参照的数字孪生重建真实驾驶片段，以几何对齐的模拟器渲染条件化扩散模型。
- 得到数字孪生接地的 Sim2Real 模型 DT-S2R，可依据低成本、带地理参照的模拟器数据，在数字孪生覆盖范围内的已重建场景和新模拟器场景中合成逼真驾驶图像。
- 在多种 3D 检测器上验证生成数据有效性；其中 DETR3D 在不使用目标图像训练检测器的情况下，达到目标区域真实数据 oracle 所获 mAP 的 93.18%。
- 表明与既有目标区域外真实数据进行简单协同训练可超过该 oracle，说明在数字孪生可用区域，DT-R2S2R 可显著降低人工现场采集与标注成本，为扩展 3D 感知提供实用基础。

### 局限性
- 方法适用范围受“数字孪生覆盖范围”和“数字孪生可用区域”限制；摘要未提供足够信息说明覆盖范围之外或缺乏数字孪生的区域表现如何。
- 摘要未提供足够信息说明数字孪生重建的精度要求、重建误差对下游生成与检测的影响。
- 摘要未提供足够信息说明扩散模型训练细节、数据规模、计算成本与推理开销。
- 摘要未提供足够信息说明所验证的 3D 检测器完整清单、数据集构成以及除 DETR3D 外各检测器的具体指标。
- 摘要未提供足够信息说明协同训练设置中“目标区域外真实数据”的来源、数量与配比敏感性。

### 阅读优先级
高。理由：该工作直接针对自动驾驶 3D 感知中跨区域部署的数据采集与标注成本问题，提出数字孪生接地的 Real2Sim2Real 生成式增广方案，并给出接近目标区域真实数据 oracle 的量化结果（DETR3D 达 93.18% mAP），且协同训练可超过 oracle，对数据高效 3D 感知与仿真到现实迁移方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera-based 3D perception for autonomous driving relies heavily on large annotated datasets, and deploying such a system to a new target region typically requires data collection and annotation. Generative augmentation has been proposed to reduce this cost, but existing approaches face a fundamental trade-off: label-conditioned methods consume the very annotations they aim to replace, while simulator-conditioned methods offer free annotations but lack visual grounding to specific real environments. This work investigates the extent to which a digital-twin-driven Real2Sim2Real pipeline (DT-R2S2R) can substitute for target-region real data. By reconstructing recorded driving clips inside a georeferenced digital twin (DT-R2S), we condition a diffusion model on geometrically aligned simulator renderings, establishing a digital twin-grounded Sim2Real model (DT-S2R). As a result, DT-S2R synthesizes photorealistic driving images given low-cost yet georeferenced simulator data across both reconstructed and novel simulator scenes within digital-twin coverage. The efficacy of generated data is verified on diverse 3D detectors. DETR3D, especially, reports 93.18% of mAP obtained by a target-region real-data oracle, without employing target images for detector training. Furthermore, simple co-training with existing out-of-target real data outperforms the oracle. Thus, DT-R2S2R can substantially reduce the cost of manual on-site data collection and annotation in digital twin-available districts, providing a practical foundation for scaling 3D perception.

</details>

#### 2026-10-06 - Image-Space Refraction Correction for Underwater 3D Reconstruction: Warping Flat-Port Views into Pinhole Perspective

**Authors:** Chelim Lim, Tobias Fischer, Emilio Olivastri, Beverley Gorry, Michael Milford, Alejandro Fontan
**Links:** [abs](https://arxiv.org/abs/2610.07788) - [pdf](https://arxiv.org/pdf/2610.07788)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, SfM, SLAM, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Image-Space Refraction Correction for Underwater 3D Reconstruction: Warping Flat-Port Views into Pinhole Perspective
- 作者：Chelim Lim, Tobias Fischer, Emilio Olivastri, Beverley Gorry, Michael Milford, Alejandro Fontan
- 出版日期：2026-10-06T05:33:46Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.07788) / [PDF](https://arxiv.org/pdf/2610.07788)

### 一句话总结
提出一种在图像空间进行的基于物理的水下折射校正方法，将平面端口平口相机视图变形为针孔透视，以消除重建中的碗状畸变。

### 研究问题
消费级相机广泛应用于水下探索与珊瑚礁、海底栖息地测绘，但平口外壳界面处的折射会导致重建场景和相机轨迹出现碗状变形，损害测绘与导航所需的度量精度。论文旨在在重建之前移除主要的折射畸变。

### 核心思路/方法
在图像空间引入基于物理的折射校正，将平面端口视图变形为针孔透视。该方法与下游任务无关，校正后的图像可直接作为现有重建和 SLAM 算法的输入。通过光线追踪仿真刻画折射畸变，并在两个具有不同场景结构的真实水下数据集上验证校正效果。

### 主要贡献
- 提出图像空间的、基于物理的折射校正方法，将平口视图变形为针孔透视。
- 方法对下游任务无关，校正图像可直接供现有重建与 SLAM 算法使用。
- 通过光线追踪仿真刻画折射畸变，并在两个真实水下数据集上验证。
- 与常规及折射式 Structure-from-Motion（SfM）相比，方法在去除重建变形的同时注册更多帧并保持较低重投影误差。
- 校正可泛化到多种重建与 VSLAM 后端，显示对下游视觉流程的广泛适用性。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体计算复杂度、对极端水下条件或不同相机参数的泛化边界、失败案例，也未提供定量实验指标的详细数值。

### 阅读优先级
高。理由：论文针对水下 3D 重建中由平口折射引起的系统性几何畸变这一实际问题，提出与下游算法解耦的图像空间校正方案，并在真实数据集上验证且声称可泛化到多种重建与 VSLAM 后端，对水下视觉测绘与导航流程具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Consumer-grade cameras in flat-port housings are widely used for underwater exploration and mapping of coral reefs and seafloor habitats due to their low cost and accessibility. However, refraction at flat-port interfaces causes bowl-shaped deformation in reconstructed scenes and camera trajectories, compromising the metric accuracy required for mapping and navigation. To remove the dominant refractive distortion before reconstruction, we introduce a physics-based refraction correction in image space. Our method is downstream-agnostic: the refraction-corrected images can be directly used as input to existing reconstruction and SLAM algorithms. We characterize the refractive distortion through ray-tracing simulations and validate our correction on two real underwater datasets with differing scene structures. Compared with conventional and refractive Structure-from-Motion (SfM), our approach removes reconstruction deformation while registering more frames and maintaining low reprojection error. The correction further generalizes across diverse reconstruction and VSLAM backends, demonstrating its broad applicability to downstream vision pipelines.

</details>

#### 2026-10-05 - SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation

**Authors:** Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin
**Links:** [abs](https://arxiv.org/abs/2610.07472) - [pdf](https://arxiv.org/pdf/2610.07472)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, pose estimation, Gaussian Splatting, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation
- 作者：Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin
- 出版日期：2026-10-05T22:38:27Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.07472 ；PDF https://arxiv.org/pdf/2610.07472

### 一句话总结
SURGE 是一个面向水下 ROV 的相机-声呐融合框架，通过在因子图中联合估计轨迹与目标位置，并将恢复出的度量位姿用于声呐高斯泼溅，从而在真实水下 RGB-声呐数据上改善定位一致性并得到更紧凑、原生度量的重建结果。

### 研究问题
水下 ROV 在洞穴、沉船和水下基础设施等环境中执行探索与巡检任务时，需要准确的三维环境理解，这依赖可靠的载体定位和度量场景重建。然而水下外部定位常常不可用，小型 ROV 主要依赖自身感知。光学视觉能提供丰富视觉与几何信息，但存在尺度模糊和轨迹漂移；二维成像声呐能提供度量距离，却缺少完整三维几何。现有水下重建方法通常分别处理这些限制，或假设传感器位姿已知，导致定位与重建相互割裂。论文要解决的问题是如何在外部定位不可用的情况下，将视觉与声学观测结合，实现定位与重建的联合估计。

### 核心思路/方法
SURGE 是一个相机-声呐框架，其核心是在因子图中整合视觉观测和声学观测，联合估计 ROV 轨迹与目标位置。在获得恢复出的度量位姿后，方法使用这些位姿进行声呐高斯泼溅，从而完成重建。摘要没有提供因子图的具体节点、因子形式、优化细节、图像门控机制的具体实现，也没有提供网络结构、损失函数或训练策略等细节。

### 主要贡献
- 提出 SURGE，一个相机-声呐融合框架，将视觉与声学观测在因子图中结合，联合估计 ROV 轨迹和目标位置。
- 利用恢复出的度量位姿驱动声呐高斯泼溅，将定位与重建连接起来。
- 在真实水下 RGB-声呐观测上进行实验，摘要称 SURGE 相比传统基于视觉的位姿估计显著提升了定位一致性，并相比 RGB 高斯泼溅基线产生更紧凑、原生度量的重建。
- 摘要未提供足够信息说明消融实验、定量指标、数据集规模或与更多基线的系统比较。

### 局限性
摘要未提供足够信息说明方法的具体适用边界、失败场景、计算代价、实时性、对传感器标定误差的敏感性、不同水质或浑浊度下的表现，以及定量评价指标的完整情况。摘要仅提到实验在真实水下 RGB-声呐观测上进行，未说明实验环境数量、目标类型、轨迹长度或重建精度数值。

### 阅读优先级
高。理由：该论文位于 3D 重建与多视图几何、神经场景表示与渲染、以及水下机器人应用的交叉方向，直接针对水下 ROV 在无外部定位条件下定位与重建割裂的问题，提出相机-声呐因子图联合估计与声呐高斯泼溅结合的方案，问题定义清晰且应用场景明确。若关注水下感知、多模态融合定位建图或声呐神经渲染，该论文具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Remotely operated vehicles (ROVs) are widely used to explore and inspect underwater environments such as caves, shipwrecks, and submerged infrastructure. These missions require accurate 3D understanding of the surrounding environment, which depends on both reliable vehicle localization and metric scene reconstruction. However, external positioning is often unavailable underwater, requiring small ROVs to rely primarily on onboard perception. Optic vision provides rich visual and geometric information but suffers from scale ambi- guity and trajectory drift, whereas 2D imaging sonar provides metric range but incomplete 3D geometry. Existing underwater reconstruction approaches typically address these limitations separately or assume known sensor poses, leaving localization and reconstruction disconnected. We present SURGE, a camera sonar framework that jointly estimates the ROV trajectory and target location by integrating visual and acoustic observations within a factor graph, then uses the recovered metric poses for sonar Gaussian splatting. Experiments on real underwater RGB sonar observations show that SURGE substantially improves localization consistency over conventional vision based pose estimation and produces a more compact, natively metric reconstruction than RGB Gaussian splatting baselines.

</details>

#### 2026-10-05 - Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models

**Authors:** Zhimin Shao, Xijun Liu, Zhaoliang Zhang, Yutao Tang, Abhay Yadav, Rama Chellappa, Cheng Peng
**Links:** [abs](https://arxiv.org/abs/2610.06813) - [pdf](https://arxiv.org/pdf/2610.06813)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models
- 作者：Zhimin Shao, Xijun Liu, Zhaoliang Zhang, Yutao Tang, Abhay Yadav, Rama Chellappa, Cheng Peng
- 出版日期：2026-10-05T17:55:06Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要链接 https://arxiv.org/abs/2610.06813；PDF 链接 https://arxiv.org/pdf/2610.06813

### 一句话总结
论文提出 Masked Geometric Encoder（MGE），通过在训练中从全局注意力中策略性丢弃帧 token 并向预训练的全上下文教师模型蒸馏，学习在不完整跨视角上下文下更鲁棒的几何表示，并配套提出 Anchor-Guided Adaptive token merging 以提升推理效率。

### 研究问题
- 现有 3D 基础模型依赖全对全全局注意力，导致二次复杂度并限制长序列推理。
- 无约束的跨视角交互可能传播来自遮挡视图或“视觉相似但几何距离较远”视图的不可靠证据。
- 因此需要在不完整跨视角上下文条件下，学习更鲁棒的几何表示，同时兼顾标准基准性能与推理效率。

### 核心思路/方法
- 提出 Masked Geometric Encoder（MGE），在训练时策略性地从全局注意力中丢弃 frame tokens。
- 通过从预训练的全上下文教师模型进行蒸馏，使模型学习内在更丰富的逐帧表示，并提供足够的中间监督以避免性能退化。
- 在推理阶段，提出 Anchor-Guided Adaptive token merging 技术：保留具有代表性的 anchor frames，同时联合合并其余视图中的冗余 token。
- 目标是在保持较高重建质量的同时实现推理加速，尤其在有限视图设置下。

### 主要贡献
- 提出 MGE，在遮挡和“doppelganger views”场景下带来更强性能，同时在标准基准上保持高性能。
- 表明更丰富的逐帧表示可提升推理阶段 token 减少的有效性。
- 提出 Anchor-Guided Adaptive token merging 技术，以保留代表性 anchor frames 并合并冗余 tokens。
- 与其他高效推理方法相比，在实现推理加速的同时持续保持更高的重建质量，尤其在有限视图设置下。

### 局限性
- 摘要未提供足够信息说明具体实验数据集、评价指标、计算开销细节、失败案例或方法适用范围。
- 摘要未提供足够信息说明 MGE 丢弃 frame tokens 的具体策略、教师模型结构、蒸馏损失细节及 token merging 的完整算法流程。
- 摘要未提供足够信息说明在哪些条件下性能可能下降，或是否对特定场景、视图数量、硬件条件存在限制。

### 阅读优先级
高。理由：该论文针对 3D 基础模型中的全局注意力复杂度与跨视角不可靠证据传播问题提出明确方法，并同时关注遮挡、doppelganger views、标准基准和有限视图下的推理效率与重建质量，问题重要且方法方向清晰，适合关注 3D 重建、多视图几何与高效推理的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent progress in 3D foundation models has enabled rapid 3D reconstruction and camera calibration by leveraging learned 3D priors from vast amount of spatial data. However, the all-to-all global attention design leads to quadratic complexity and limits long-sequence inference; unconstrained cross-view interactions also can propagate unreliable evidence from occluded or visually similar but geometrically distant views. In this paper, We introduce a Masked Geometric Encoder (MGE), which promotes the learning of robust geometric representations under incomplete cross-view context. During training, MGE strategically drops frame tokens from global attention and distills from a pretrained full-context teacher model. This allows the model to learn an intrinsically richer per-frame representation while providing sufficient intermediate supervision to avoid performance degradation. Through extensive experiments, we show that MGE leads to much stronger performance under occlusion and doppelganger views while retaining high performance on standard benchmarks. Such a richer frame representation also leads to more effective token reduction during inference. To this end, we develop a novel Anchor-Guided Adaptive token merging technique that preserves representative anchor frames while jointly merging redundant tokens from the remaining views. Compared to other efficient inference approaches, we can achieve inference speedup while consistently maintaining higher reconstruction quality, particularly in limited-view settings.

</details>

#### 2026-10-05 - FrontVeg V2: A Training-Free Software Framework for Foreground-Aware Zero-Shot Plant Trait Segmentation in High-Resolution Images of Trellised Crops

**Authors:** Abdoul Djalil Ousseini Hamza, Herearii Metuarea, Corentin Lothod{é}, Morgane Roth, Jacem Ben Hamden, Eric Duch{ê}ne, Lionel Ley, David Alletru, David Rousseau
**Links:** [abs](https://arxiv.org/abs/2610.06575) - [pdf](https://arxiv.org/pdf/2610.06575)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FrontVeg V2: A Training-Free Software Framework for Foreground-Aware Zero-Shot Plant Trait Segmentation in High-Resolution Images of Trellised Crops
- 作者：Abdoul Djalil Ousseini Hamza, Herearii Metuarea, Corentin Lothod{é}, Morgane Roth, Jacem Ben Hamden, Eric Duch{ê}ne, Lionel Ley, David Alletru, David Rousseau
- 出版日期：2026-10-05T15:53:57Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.06575 ；PDF https://arxiv.org/pdf/2610.06575

### 一句话总结
FrontVeg V2 是一个开源、免训练的软件框架，用于在棚架作物高分辨率图像中实现前景感知的零样本植物性状分割。

### 研究问题
论文针对棚架作物高分辨率图像中的植物性状分割问题，尤其是邻近植被行造成的干扰。摘要指出，该框架旨在分割植物器官和病害症状，同时减少由邻近植被行引发的检测。摘要未提供足够信息说明具体作物种类、病害类型或评估数据集细节。

### 核心思路/方法
FrontVeg V2 采用免训练、零样本的分割流程，包含以下组成部分：
- 单目深度估计；
- 使用 Valley-Aware Depth Thresholding 进行自动前景提取；
- 分块零样本分割；
- Graph-Based Mask Assembly；
- 几何感知融合。

当前实现集成了 Depth Anything V2（DAV2）与 SAM3，并支持命令行批处理和 Napari 图形界面两种使用方式。摘要未提供足够信息说明各模块的具体算法细节、参数设置或处理流程。

### 主要贡献
- 提出 FrontVeg V2，一个开源、免训练的前景感知零样本植物性状分割软件框架。
- 将单目深度估计、前景提取、分块零样本分割、掩码组装与几何感知融合组合为统一流程。
- 支持在无需任务特定模型重训练的情况下，用于多作物、多性状的数字表型分析。
- 当前实现集成 DAV2 与 SAM3，并提供命令行批处理与 Napari 图形界面。
- 摘要未提供足够信息说明定量实验结果、精度指标或与基线方法的比较。

### 局限性
- 摘要未提供足够信息说明该框架在何种数据集、作物种类或病害症状上进行了验证。
- 摘要未提供足够信息说明分割精度、鲁棒性、运行效率或失败案例。
- 摘要未提供足够信息说明 Valley-Aware Depth Thresholding、Graph-Based Mask Assembly 和几何感知融合的具体实现限制。
- 摘要未提供足够信息说明对 Depth Anything V2 和 SAM3 的依赖是否带来计算资源或泛化性方面的约束。
- 摘要未提供足够信息说明与监督学习方法或其他零样本方法的对比结果。

### 阅读优先级
中。理由：该论文提出的是面向高分辨率棚架作物图像、免训练且零样本的分割框架，并整合了深度估计与基础分割模型，主题与植物表型、零样本分割和农业视觉相关。但摘要未提供定量实验、数据集和对比结果，无法仅凭摘要判断其实际性能与创新程度；若关注农业视觉、零样本分割或数字表型工具，可列为中等优先级阅读。

</details>

<details>
<summary>Abstract</summary>

FrontVeg V2 is an open-source, training-free software framework for foregroundaware zero-shot segmentation of plant traits in high-resolution images of trellised crops. The pipeline combines monocular depth estimation, automatic foreground extraction using Valley-Aware Depth Thresholding, tiled zero-shot segmentation, Graph-Based Mask Assembly, and geometry-aware fusion. This design enables plant organs and disease symptoms to be segmented while reducing detections arising from neighboring vegetation rows. The current implementation integrates Depth Anything V2 (DAV2) and SAM3 and can be used through both command-line batch processing and a Napari graphical interface. FrontVeg V2 provides a reusable framework for multi-crop, multi-trait digital phenotyping without task-specific model retraining.

</details>

#### 2026-10-05 - Structural Foundations of Nonlinear Systems with Unknown Inputs: The UID-Induced Normal Form and Minimal-Sensing Structure-from-Motion

**Authors:** Agostino Martinelli
**Links:** [abs](https://arxiv.org/abs/2610.05939) - [pdf](https://arxiv.org/pdf/2610.05939)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Structural Foundations of Nonlinear Systems with Unknown Inputs: The UID-Induced Normal Form and Minimal-Sensing Structure-from-Motion
- 作者：Agostino Martinelli
- 出版日期：2026-10-05T07:56:38Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.05939) / [PDF](https://arxiv.org/pdf/2610.05939)

### 一句话总结
本文提出非线性未知输入系统的首个通用结构性状态估计方案（UID 诱导标准型），统一解决了未知输入的解耦与重构问题，并以一种仅需三个点特征与单轴陀螺仪的最小 Structure-from-Motion 配置验证了其可行性。

### 研究问题
论文关注由未知输入驱动的非线性系统的状态估计问题，试图在不对未知输入施加任何模型或随机假设的前提下，从结构层面处理未知输入对可观测动态的影响，即如何将未知输入信息分解、解耦并重建，并探索该框架在最小传感配置下的 Structure-from-Motion 应用。

### 核心思路/方法
- 基于非线性未知输入可观测性理论，证明任意此类系统都存在一个结构等价的表示，称为 UID 诱导标准型（UID-induced normal form）。
- 该表示将未知输入携带的信息分解为两个互补部分：与可观测动态在结构上解耦的未知输入方向，以及完全表示影响可观测动态的未知输入信息的可观测量。
- 由此在不需要任何未知输入模型或随机假设的条件下，统一给出未知输入解耦与未知输入重构的结构性方案。
- 将该框架应用于一种此前未被探索的最小 Structure-from-Motion 配置：仅使用三个点特征和单个单轴陀螺仪进行递归状态估计，可恢复三维结构与相机运动，但存在一个未知的全局尺度因子。

### 主要贡献
- 建立了首个针对未知输入驱动非线性系统的通用结构性状态估计解。
- 提出 UID 诱导标准型，将未知输入信息分解为结构性解耦方向与可观测表示量，统一了未知输入解耦与重构，且不依赖未知输入的模型或随机假设。
- 展示了一个此前未被探索的最小 Structure-from-Motion 配置，说明仅用三个点特征和单轴陀螺仪即可进行递归状态估计并恢复结构、相机运动（至多相差未知全局尺度）。
- 在真实世界数据上的实验验证了该框架，并证明了该最小传感配置的可行性。

### 局限性
- 摘要仅提及恢复三维结构与相机运动“至多相差一个未知全局尺度因子”，尺度不确定性未被消除。
- 摘要未说明计算复杂度、收敛性保证、对噪声或异常值的鲁棒性，也未给出与现有方法的定量对比——摘要未提供足够信息。
- 摘要未说明实验所用真实数据的规模、场景类型及评价指标——摘要未提供足够信息。
- 摘要未说明该标准型在更一般系统上的构造条件或适用范围限制——摘要未提供足够信息。

### 阅读优先级
高。理由：论文声称首次给出未知输入非线性系统状态估计的通用结构性解，并提出最小传感 Structure-from-Motion 配置，主题与 3D 重建及多视图几何直接相关；但具体适用边界与实验细节需阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

This paper establishes the first general structural solution to the problem of state estimation for nonlinear systems driven by unknown inputs. Building upon nonlinear unknown-input observability theory, we show that every such system admits a structurally equivalent representation, referred to as the UID-induced normal form. The proposed representation decomposes the information carried by the unknown inputs into two complementary components: unknown-input directions that are structurally decoupled from the observable dynamics and observable quantities that completely represent the unknown-input information affecting the observable dynamics. As a consequence, the UID-induced normal form provides a unified structural solution to unknown-input decoupling and unknown-input reconstruction, without requiring any model or stochastic assumption on the unknown inputs. The practical significance of the proposed framework is demonstrated through a previously unexplored minimal Structure-from-Motion configuration. The proposed representation enables recursive state estimation from only three point features and a single-axis gyroscope, allowing the recovery of the three-dimensional structure and camera motion up to an unknown global scale factor. Experiments on real-world data validate the proposed framework and demonstrate the feasibility of this minimal sensing configuration.

</details>

#### 2026-10-05 - Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

**Authors:** Junhyun Nam, Wonse Jo
**Links:** [abs](https://arxiv.org/abs/2610.05757) - [pdf](https://arxiv.org/pdf/2610.05757)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM
- 作者：Junhyun Nam, Wonse Jo
- 出版日期：2026-10-05T04:06:38Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要链接 https://arxiv.org/abs/2610.05757 ；PDF 链接 https://arxiv.org/pdf/2610.05757

### 一句话总结
论文提出 Hybrid DeepSEE（HDS），一种人在回路（HITL）的神经符号框架，用于在视觉 SLAM 中主动预判漂移，并借助 LLM 将人类定性上下文转化为可解释的符号约束，以提升可靠性。

### 研究问题
视觉 SLAM 中的数据驱动模型虽然具备预测能力，但其“黑盒”特性在分布外（OOD）环境中常常产生物理上不一致的输出，从而影响漂移预判的可靠性。

### 核心思路/方法
HDS 将神经漂移风险估计与符号约束推理相结合。具体而言，框架使用一个大型语言模型（LLM）作为推理桥梁，把定性的、来自人类上下文的输入转化为可解释的符号约束，从而在神经预测基础上引入符号层面的推理与约束。

### 主要贡献
- 提出 Hybrid DeepSEE（HDS），一种人在回路（HITL）的神经符号框架，面向视觉 SLAM 的主动漂移预判。
- 将神经漂移风险估计与符号约束推理相集成，以应对数据驱动模型在 OOD 环境中输出物理不一致的问题。
- 使用 LLM 作为推理桥梁，把定性的人类上下文翻译为可解释的符号约束。
- 在该架构基础上，提出一个更强的漂移预判框架，旨在提升视觉 SLAM 的可靠性与一致性。

### 局限性
摘要未提供足够信息。包括具体的实验设置、数据集、评价指标、定量结果、与基线方法的对比、LLM 的具体使用方式与失败案例、HITL 的交互负担、符号约束的覆盖范围与可扩展性，以及实时性等，摘要均未提供足够信息。

### 阅读优先级
中。理由是：该论文聚焦视觉 SLAM 漂移预判中的可靠性、可解释性与 OOD 问题，并将神经符号方法与人在回路、LLM 推理桥接相结合，主题具有一定交叉创新性；但摘要未给出实验验证与量化结果，难以仅凭摘要判断其实际效果与相对优势。

</details>

<details>
<summary>Abstract</summary>

This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drift risk estimation with symbolic constraint reasoning. By utilizing a Large Language Model (LLM) as a reasoning bridge, the framework translates qualitative human context into interpretable symbolic constraints. Building upon this architecture, we propose a superior drift anticipation framework that ensures enhanced reliability and consistency in Visual SLAM

</details>

#### 2026-10-04 - F$^2$ SLAM: Turning Feed-Forward Geometry into Persistent Factors for SLAM

**Authors:** Zhisong Xu, Fan Zhu, Jiawei Qian, Ziyu Chen, Zhenjun Zhao, Javier Civera
**Links:** [abs](https://arxiv.org/abs/2610.05207) - [pdf](https://arxiv.org/pdf/2610.05207)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, bundle adjustment, dense reconstruction, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：F$^2$ SLAM: Turning Feed-Forward Geometry into Persistent Factors for SLAM
- 作者：Zhisong Xu, Fan Zhu, Jiawei Qian, Ziyu Chen, Zhenjun Zhao, Javier Civera
- 出版日期：2026-10-04T13:24:27Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类；未提供二级分类）
- 链接：[摘要](https://arxiv.org/abs/2610.05207) / [PDF](https://arxiv.org/pdf/2610.05207)

### 一句话总结
该论文提出 F$^2$SLAM，将前馈三维模型提供的多视图几何直接转化为持久稠密因子图中的优化原生“目标-权重”测量，从而在统一的稠密光束法平差中联合约束位姿、逆深度与可选相机内参。

### 研究问题
前馈三维模型能提供较强的多视图几何先验，而在线 SLAM 主要依赖局部测量，在长序列上会累积漂移。现有结合二者的尝试通常把前馈预测当作外部几何状态，在在线估计完成后再进行对齐或融合，这导致更广泛的多视图证据被排除在优化 SLAM 状态的优化器之外。

### 核心思路/方法
- 不将前馈几何作为事后对齐或融合的外部状态，而是直接转换为优化原生的目标-权重测量，并附着在持久稠密因子图上。
- 采用双频流结构：高频流维持局部跟踪约束与图连通性；低频流利用更宽的多视图上下文，在状态一致性检查后有选择地刷新已有测量。
- 两条流通过单一稠密光束法平差共同约束同一组位姿、逆深度以及可选的相机内参。

### 主要贡献
- 提出把前馈几何转化为持久优化因子/测量的 SLAM 框架，使多视图证据进入优化器内部，而非停留在事后融合层面。
- 设计高频局部跟踪与低频多视图上下文刷新相结合的双频机制，并引入状态一致性检查以选择性更新测量。
- 在统一稠密光束法平差中同时约束位姿、逆深度和可选内参，覆盖标定与未标定设置。
- 摘要称在多个基准上展示出稳定的轨迹估计与改进的稠密重建；在 Replica 数据集未标定配置下，将平均 ATE RMSE 从最强前馈基线的 0.030 m 降至 0.002 m。

### 局限性
- 摘要未提供足够信息说明方法的具体计算开销、实时性、高频流与低频流的具体频率设置。
- 摘要未提供足够信息说明状态一致性检查的具体判据与失败情形。
- 摘要未提供足够信息说明除 Replica 外其他基准的详细结果、消融实验及与更多 SLAM 方法的完整对比。
- 摘要未提供足够信息说明在极端场景（如快速运动、弱纹理、动态环境）下的表现与鲁棒性。

### 阅读优先级
高。理由：该论文针对前馈几何与在线 SLAM 结合方式提出“直接转为优化原生持久因子”的明确新思路，并报告了未标定设置下显著的 ATE RMSE 改进；若关注多视图几何先验与 SLAM 优化器的深度耦合、稠密重建或标定/未标定统一优化，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D models provide strong multi-view geometric priors, while on- line simultaneous localization and mapping (SLAM) relies mainly on local mea- surements and can accumulate drift over long sequences. Existing attempts to combine the two typically treat feed-forward predictions as an external geomet- ric state that is aligned or fused with the online estimate after the fact, which keeps broader multi-view evidence outside the optimizer that refines the SLAM state. We present F2SLAM, which instead converts feed-forward geometry di- rectly into optimization-native target-weight measurements attached to a persis- tent dense factor graph. A high-frequency stream maintains local tracking con- straints and graph connectivity, while a low-frequency stream uses wider multi- view context to selectively refresh existing measurements after a state-consistency check. Both streams constrain the same poses, inverse depths, and optional cam- era intrinsics through a single dense bundle adjustment. Experiments on multiple benchmarks demonstrate consistently strong trajectory estimation and improved dense reconstruction in both calibrated and uncalibrated settings. Notably, the uncalibrated configuration reduces the average ATE RMSE from 0.030 m for the strongest feed-forward baseline to 0.002 m on the Replica dataset.

</details>

#### 2026-10-04 - SPACE-CLIPv2: Decoding Local Geometry from Frozen CLIP for Monocular Depth Estimation

**Authors:** Hyun Song, Taewan Cho, Kangmin Kim, Andrew Jaeyong Choi
**Links:** [abs](https://arxiv.org/abs/2610.05029) - [pdf](https://arxiv.org/pdf/2610.05029)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SPACE-CLIPv2: Decoding Local Geometry from Frozen CLIP for Monocular Depth Estimation
- 作者：Hyun Song, Taewan Cho, Kangmin Kim, Andrew Jaeyong Choi
- 出版日期：2026-10-04T07:50:10Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.05029 ；PDF：https://arxiv.org/pdf/2610.05029

### 一句话总结
SPACE-CLIPv2 在冻结 CLIP 主干上，通过固定局部邻域 token 聚合与门控残差、token 空间高通分支，改进单目深度估计中的局部几何解码。

### 研究问题
论文关注：CLIP 等视觉-语言基础模型虽具强语义表示，但其 patch token 并非直接为稠密度量几何优化；SPACE-CLIP 已表明冻结 CLIP 特征可通过层组特征融合支持单目深度估计，但仍未解决“相邻 CLIP token 应如何组合以恢复精细局部结构”的问题。

### 核心思路/方法
提出 SPACE-CLIPv2，一种冻结主干深度解码器，在 CLIP token 空间聚合固定局部邻域。具体而言：在选定的解码器阶段，模型采样固定 token stencil，预测聚合权重，并通过门控残差更新注入响应；此外，token 空间高通分支用于保留浅层局部对比。论文还比较固定采样与学习偏移采样，并在 NYU Depth V2 上相对匹配的 SPACE-CLIP 基线改进；五种子实验一致偏向固定采样而非学习偏移采样。零样本 iBims-1 评估进一步改善边界和平面几何指标。

### 主要贡献
- 提出 SPACE-CLIPv2：在冻结 CLIP 特征上通过固定局部邻域 token 聚合来解码局部几何的深度解码器。
- 在选定解码器阶段引入固定 token stencil、预测聚合权重和门控残差更新机制。
- 引入 token 空间高通分支以保留浅层局部对比。
- 在 NYU Depth V2 上相对匹配 SPACE-CLIP 基线取得改进，并通过五种子实验支持固定采样优于学习偏移采样。
- 在零样本 iBims-1 评估中改善边界与平面几何指标。

### 局限性
摘要未提供足够信息。未提供关于模型规模、计算开销、失败场景、固定 stencil 设计选择依据、学习偏移采样劣势原因、其他数据集泛化表现等细节。

### 阅读优先级
中。理由：该工作聚焦冻结 CLIP 特征用于单目深度估计中的局部 token 聚合问题，问题定义清晰，且给出 NYU Depth V2 与零样本 iBims-1 上的摘要级结果；但摘要未展开方法细节、消融规模与完整实验设置，若研究兴趣直接涉及 CLIP 几何解码或单目深度估计，可优先阅读，否则可作为中等优先级参考。

</details>

<details>
<summary>Abstract</summary>

Vision-language foundation models such as CLIP provide strong semantic representations, but their patch tokens are not directly optimized for dense metric geometry. SPACE-CLIP showed that frozen CLIP features can support monocular depth estimation through layer-group feature fusion, yet it leaves open how neighboring CLIP tokens should be combined to recover fine local structure. We present SPACE-CLIPv2, a frozen-backbone depth decoder that aggregates fixed local neighborhoods in CLIP token space. At selected decoder stages, the model samples a fixed token stencil, predicts aggregation weights, and injects the resulting response through a gated residual update. A token-space high-pass branch further preserves shallow local contrast. On NYU Depth V2, SPACE-CLIPv2 improves over a matched SPACE-CLIP baseline, while five-seed experiments consistently favor fixed over learned-offset sampling. Zero-shot iBims-1 evaluation further improves boundary and planar-geometry measures. These results support constrained local token aggregation as a practical mechanism for decoding geometry from frozen CLIP representations.

</details>

#### 2026-10-01 - DecomVoxel: Harnessing 3D-Native Priors with Guided In-situ Denoising Optimization for Decompositional Scene Reconstruction

**Authors:** Junfeng Ni, Zirui Zhou, Yixin Chen, Yu Liu, Nan Jiang, Zhifei Yang, Song-Chun Zhu, Siyuan Huang
**Links:** [abs](https://arxiv.org/abs/2610.01914) - [pdf](https://arxiv.org/pdf/2610.01914)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DecomVoxel: Harnessing 3D-Native Priors with Guided In-situ Denoising Optimization for Decompositional Scene Reconstruction
- 作者：Junfeng Ni, Zirui Zhou, Yixin Chen, Yu Liu, Nan Jiang, Zhifei Yang, Song-Chun Zhu, Siyuan Huang
- 出版日期：2026-10-01T15:54:23Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要链接：https://arxiv.org/abs/2610.01914 ；PDF：https://arxiv.org/pdf/2610.01914 ；代码：https://github.com/DecomVoxel/DecomVoxel

### 一句话总结
DecomVoxel 将物体补全表述为一种引导式的原位去噪优化，把 3D 原生先验与神经场景重建结合，以提升重遮挡下分解式场景重建的质量。

### 研究问题
论文关注分解式场景重建，即同时重建高质量物体与背景。摘要指出，现有方法在严重遮挡条件下仍难以达到理想质量。生成式先验被视为潜在解决方案，但存在两类问题：基于 2D 图像的先验由于缺乏 3D 感知，常出现多视角不一致；3D 原生先验虽具有更强的结构归纳偏置，却容易在复杂场景中导致空间漂移和错位。

### 核心思路/方法
论文提出 DecomVoxel，将物体补全建模为“引导式原位去噪优化”（guided in-situ denoising optimization），用于连接 3D 原生先验与神经场景重建。方法层面，摘要提到两项关键设计：
1. 重新表述的基于 epsilon 的蒸馏损失（reformulated epsilon-based distillation loss），用于确保稳定的潜在细化；
2. 自适应空间引导（adaptive spatial guidance），利用已占据锚点与空置锚点并结合时间退火，以抑制生成式幻觉并缓解空间漂移。

### 主要贡献
- 提出 DecomVoxel，面向分解式场景重建，将物体补全表述为引导式原位去噪优化，以桥接 3D 原生先验与神经场景重建。
- 引入重新表述的基于 epsilon 的蒸馏损失，以保障稳定的潜在细化。
- 设计自适应空间引导，结合已占据/空置锚点与时间退火，用于抑制生成式幻觉和缓解空间漂移。
- 在 Replica 与 ScanNet++ 上报告实验，称 DecomVoxel 显著优于当前最优方法，同时忠实保留原始空间布局、结构保真度与风格一致的纹理；并称其可输出具有干净拓扑、几何与外观的高质量带纹理网格。

### 局限性
摘要未提供足够信息。摘要未给出失败案例、适用边界、计算开销、对特定数据集或先验模型的依赖程度，也未说明方法在何种场景下可能失效。

### 阅读优先级
高。理由：该论文聚焦 3D 重建与多视角几何中的分解式场景重建问题，明确针对重遮挡、2D 先验多视角不一致与 3D 原生先验空间漂移等关键矛盾，并提出具体方法设计与公开代码；若关注生成式先验与神经场景重建结合、遮挡下物体补全或高质量网格重建，该工作具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Decompositional scene reconstruction aims to reconstruct high-quality objects and background, yet existing methods still struggle with the level of quality under heavy occlusions. While generative priors offer a potential solution, 2D image-based priors often suffer from multi-view inconsistency due to a lack of 3D awareness. Conversely, 3D-native priors provide stronger structural inductive biases but frequently lead to spatial drift and misalignment within complex scenes. To address these issues, we propose DecomVoxel, formulating object completion as a guided in-situ denoising optimization that bridges 3D-native priors with neural scene reconstruction. Our framework introduces a reformulated epsilon-based distillation loss to ensure stable latent refinement, alongside adaptive spatial guidance that utilizes occupied and vacant anchors with temporal annealing to suppress generative hallucinations and mitigate spatial drift. Experiments on Replica and ScanNet++ show that DecomVoxel significantly outperforms state-of-the-art methods while faithfully preserving the original spatial layout, structural fidelity, and style-consistent texture. Our method pushes the boundary of decompositional reconstruction by delivering high-quality textured meshes with clean topology, geometry, and appearance, providing a robust solution for the decompositional reconstruction of complex real-world scenes. Code is available at https://github.com/DecomVoxel/DecomVoxel.

</details>

#### 2026-10-01 - Towards Physical Underwater Robotic Assistance for Scuba Diver Movement in Confined Spaces

**Authors:** Demetrious T. Kutzke, Junaed Sattar
**Links:** [abs](https://arxiv.org/abs/2610.01906) - [pdf](https://arxiv.org/pdf/2610.01906)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Physical Underwater Robotic Assistance for Scuba Diver Movement in Confined Spaces
- 作者：Demetrious T. Kutzke, Junaed Sattar
- 出版日期：2026-10-01T15:50:23Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类信息
- 链接：[摘要](https://arxiv.org/abs/2610.01906) / [PDF](https://arxiv.org/pdf/2610.01906)

### 一句话总结
论文提出并初步验证了一种可穿戴水下机器人 RADMCS，通过推进器驱动的方向引导与触觉反馈，帮助潜水员在受限空间中与海底结构保持固定距离。

### 研究问题
水肺潜水员通常被训练控制深度以避免快速上升或下降带来的严重伤害，如气体栓塞和气压伤。但许多水下任务还需要横向控制，即与珊瑚礁、水下钻探仪器或未爆炸弹药等海底结构保持距离。论文关注的核心问题是：如何通过可穿戴机器人系统，为潜水员提供方向性物理辅助，以帮助其在受限空间中维持与海底结构的距离。

### 核心思路/方法
论文提出 RADMCS（Robotic Assisted Diver Movement in Confined Spaces），一种可穿戴机器人方案，其特点是通过推进器驱动提供方向引导，而不是像已有推进辅助外骨骼那样提供推进助力。该系统利用单目深度估计等感知技术，并结合潜水推进器的力反馈，向潜水员提供触觉反馈，从而辅助其与海底结构保持固定距离。系统体积小、结构紧凑，被定位为一个可扩展的基础平台，未来可加入更复杂的控制与导航行为。

### 主要贡献
- 提出一种面向水肺潜水员的可穿戴机器人方案，通过推进器驱动提供方向引导，区别于既往的推进辅助外骨骼。
- 引入 RADMCS 系统，利用单目深度估计和潜水推进器力反馈，为潜水员提供触觉反馈，以辅助维持与海底结构的距离。
- 报告了 IRB 水下研究结果，涉及八名人类水肺潜水员参与者，包括封闭水域游泳设施和海洋环境中的阈值敏感性测试、封闭水域中的距离保持实验，以及海洋中的形态、适配和功能测试。
- 结果表明，相对较低的推力值（最大值的 10%）即可利用机器人引导的物理感受来引导人类运动方向。

### 局限性
- 论文的长期目标或更复杂控制与导航行为的可行性，摘要仅将其描述为“可扩展的基础平台”，未提供具体验证结果。
- 除“八名人类水肺潜水员参与者”和实验场景类型外，摘要未提供参与者人口统计信息、实验样本量细节、统计分析方法或具体性能指标。
- 摘要未提供单目深度估计的具体精度、触觉反馈的量化效果、不同环境下的对比数据或失败案例。
- 摘要未提供系统的续航、成本、鲁棒性或安全性评估。
- 摘要未提供与已有推进辅助外骨骼的定量比较。
- 摘要未提供代码、数据集或硬件设计的开放获取信息。
> 摘要未提供足够信息，以上局限中涉及未提及内容的条目均无法从摘要中进一步确认。

### 阅读优先级
中。理由：该论文提出了一个具有明确应用场景的水下可穿戴机器人系统，并包含 IRB 人体水下实验，涉及八名潜水员，主题具有一定新颖性和实践意义。但摘要未给出具体性能指标、统计结果或与已有方法的定量对比，且主分类为 3D Reconstruction & Multi-view Geometry，与水下机器人辅助这一主题的常规归类存在差异。若读者关注水下人机交互、可穿戴机器人和潜水辅助技术，该论文值得阅读；若需要详细的实验数据和系统评估，则需查阅全文。

</details>

<details>
<summary>Abstract</summary>

Scuba divers are taught to control their depth to avoid rapid ascents and descents, which could result in serious injuries such as gas embolisms and barotrauma. However, many underwater tasks necessitate lateral control, maintaining distance between subsea structures such as coral reefs, submerged drilling instrumentation, or unexploded ordnance. In this work, we discuss a first-of-its-kind wearable robotic solution providing thruster-actuated directional guidance to a diver, as distinct from prior propulsive-assistance exoskeletons. We introduce ``Robotic Assisted Diver Movement in Confined Spaces'' (RADMCS), a wearable robot that assists divers in maintaining a fixed distance from subsea structures by leveraging perception techniques in monocular depth estimation and force-feedback from submersible thrusters to provide haptic feedback. Its small and compact form factor creates a foundational platform that could be expanded to include more sophisticated control and navigation behaviors. We present results from Institutional Review Board (IRB) in-water studies with eight human scuba diver participants on threshold sensitivity tests in both a closed-water swimming facility and ocean environments; distance-maintaining experiments in a closed-water facility; and form, fit, and function testing in the ocean. We demonstrate that relatively low thrust values (10 percent of maximum) allow robotic direction of a human's movement using the physical sensation of the robot's guidance.

</details>

#### 2026-10-01 - LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction

**Authors:** Zhening Huang, Yueyan Li, Johnathan Chiu, Xiaoyang Lyu, Matt Zhou, Yuxin Yao, Joan Lasenby, Shangzhe Wu
**Links:** [abs](https://arxiv.org/abs/2610.01863) - [pdf](https://arxiv.org/pdf/2610.01863)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, scene reconstruction, embodied AI, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction
- 作者：Zhening Huang, Yueyan Li, Johnathan Chiu, Xiaoyang Lyu, Matt Zhou, Yuxin Yao, Joan Lasenby, Shangzhe Wu
- 出版日期：2026-10-01T15:25:35Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.01863；PDF https://arxiv.org/pdf/2610.01863；代码 https://github.com/LiteReality/LiteReality-Agent/

### 一句话总结
LiteReality-Agent 将 RGB-D 室内场景的三维重建建模为一个“编码问题”，通过编码智能体调用专用工具、迭代编辑可执行的 Python 脚本 Room.py，生成具有铰接结构、可直接用于仿真的室内三维数字孪生。

### 研究问题
如何从 RGB-D 扫描中重建真实室内环境，使其成为真实感强、具有铰接结构、且可直接用于仿真的三维场景。摘要指出，该工作面向真实到仿真（real-to-sim）的需求，并强调与近期前沿模型（如 Astra 和 Fable）的生成结果相比，需要在几何精度、视觉真实感和仿真兼容性上取得更好表现。

### 核心思路/方法
- 将三维重建表述为编码问题：由一个编码智能体使用专用工具收集证据，并迭代编辑一个 Python 脚本 Room.py。
- 执行 Room.py 可生成房间的三维数字孪生。
- 开发了稳健的 observe-edit-verify（观察—编辑—验证）框架，在重建全过程中支持证据收集、测量、验证、布局优化、仿真就绪和质量控制。
- 系统定位为一个编排框架：随着智能体能力提升，可为未来智能体提供专用工具、结构化工作流和稳健的验证机制，以提升重建质量与可靠性。

### 主要贡献
- 提出 LiteReality-Agent，一个面向可交互三维室内场景重建的智能体系统，可从 RGB-D 扫描生成真实、铰接、仿真就绪的三维场景。
- 将三维重建形式化为编码问题，并围绕可执行的 Room.py 脚本构建智能体工作流。
- 设计 observe-edit-verify 框架，覆盖证据收集、测量、验证、布局优化、仿真就绪与质量控制。
- 摘要声称其重建结果在几何精度、视觉真实感和仿真兼容性上优于近期前沿模型 Astra 与 Fable。
- 将系统定位为稳健 real-to-sim 系统的实用且重要的构建模块，并公开源代码与数据采集应用。

### 局限性
- 摘要未提供足够信息说明系统在何种扫描条件、场景类型或硬件配置下会失效。
- 摘要未提供足够信息说明其定量实验结果、评测指标、数据集规模和基线对比细节。
- 摘要未提供足够信息说明 observe-edit-verify 框架各模块的具体实现与计算开销。
- 摘要未提供足够信息说明对智能体能力（如编码模型能力）的依赖程度及其失败模式。
- 摘要未提供足够信息说明“仿真就绪”的具体判定标准与下游具身 AI 任务验证情况。

### 阅读优先级
高。理由：该论文处于三维重建与具身/机器人应用的交叉方向，提出将重建转化为智能体编码任务的新范式，并声称在几何精度、视觉真实感和仿真兼容性上优于前沿模型；同时公开代码与数据采集应用，对 real-to-sim、具身 AI 和三维场景重建研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We present LiteReality-Agent, an agentic system for reconstructing real indoor environments as realistic, articulated, and simulation-ready 3D scenes from RGB-D scans. At its core, LiteReality-Agent formulates 3D reconstruction as a coding problem, in which a coding agent gathers evidence using specialised tools and iteratively edits a Python script, Room.py, which can be executed to produce a 3D digital twin of the room. With this formulation, we develop a robust observe-edit-verify harness that supports evidence gathering, measurement, verification, layout optimisation, simulation readiness, and quality control throughout the reconstruction process. LiteReality-Agent produces high-quality reconstructions suitable for simulation and downstream embodied AI tasks. Furthermore, as agent capabilities continue to improve rapidly, the system introduced by LiteReality-Agent remains a strong orchestration framework for future agents: it equips them with specialised tools, structured workflows, and robust verification mechanisms that substantially improve reconstruction quality and reliability. We demonstrate that LiteReality-Agent produces reconstructions that are more geometrically accurate, visually realistic, and simulation-compatible than those generated by recent frontier models, such as Astra and Fable. We therefore view LiteReality-Agent as a practical and important building block for robust real-to-sim systems. Both the source code and the data-capture application are publicly available. Code:https://github.com/LiteReality/LiteReality-Agent/

</details>

#### 2026-10-01 - GenCOPE: Syn2Real Generalized Category-Level Object Pose Estimation for Robotic Picking

**Authors:** Jian Liu, Wei Sun, Zhenqi Dai, Hui Yang, Jian Xiao, Nicu Sebe, Na Zhao
**Links:** [abs](https://arxiv.org/abs/2610.01758) - [pdf](https://arxiv.org/pdf/2610.01758)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, manipulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GenCOPE: Syn2Real Generalized Category-Level Object Pose Estimation for Robotic Picking
- 作者：Jian Liu, Wei Sun, Zhenqi Dai, Hui Yang, Jian Xiao, Nicu Sebe, Na Zhao
- 出版日期：2026-10-01T14:20:38Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：abstract_url: https://arxiv.org/abs/2610.01758；pdf_url: https://arxiv.org/pdf/2610.01758；项目页: https://paperreview99.github.io/GenCOPE/

### 一句话总结
GenCOPE 面向机器人抓取场景，提出仅用合成数据训练、直接泛化到真实世界的类别级物体位姿估计方法，通过域不变表示学习与 2D-3D 交叉一致性学习缓解合成到真实的域差距。

### 研究问题
现有类别级物体姿态估计（COPE）虽然能泛化到类内未知物体，但在面对新物体类别时仍需耗费人力重新采集真实世界训练数据，限制了实际应用中的可扩展性。本文关注的问题是：能否实现合成到真实（Syn2Real）的广义 COPE，即模型只在渲染合成数据上训练，却能直接泛化到真实世界部署。核心挑战在于合成数据与真实数据之间存在显著域差距，尤其是纹理外观方面。

### 核心思路/方法
- 目标：通过学习域不变表示，捕捉同一类别内物体的语义共性，从而提升域泛化能力。
- 约束设计：引入 2D 和 3D 语义一致性约束，降低特征编码器对域特定特征的敏感性。
- 位姿回归框架：提出端到端的位姿回归框架，执行 2D-3D 交叉一致性学习，并利用密集跨模态融合进一步精炼位姿估计。
- 架构取向：考虑到真实机器人部署对简洁性和有效性的要求，模型仅依赖全局特征，形成高度轻量且高效的架构。
- 评测：在 REAL275 和 Wild6D 基准以及真实机器人操作场景上进行实验，展示其 Syn2Real 泛化性能。

### 主要贡献
- 提出面向 Syn2Real 广义类别级物体位姿估计的 GenCOPE 方法，目标是仅用合成数据训练并泛化到真实世界。
- 引入 2D 和 3D 语义一致性约束，以学习域不变表示并降低编码器对域特定特征的敏感性。
- 提出端到端位姿回归框架，结合 2D-3D 交叉一致性学习与密集跨模态融合来精炼位姿估计。
- 设计仅依赖全局特征的轻量高效架构，以适应真实机器人部署需求。
- 在 REAL275、Wild6D 及真实机器人操作场景中展示 Syn2Real 泛化性能，并发布代码与演示。

### 局限性
摘要未提供足够信息。摘要未说明方法在极端域差距、未见类别范围、计算资源需求、失败案例或真实机器人部署中的具体限制。

### 阅读优先级
高。理由：该论文聚焦机器人抓取中的类别级位姿估计，并针对实际应用中真实数据采集成本高的问题提出 Syn2Real 泛化方案；同时涉及域不变表示、2D-3D 跨模态一致性和轻量部署，主题与机器人 3D 场景理解及具身应用高度相关。若关注机器人抓取、Sim2Real/Syn2Real 泛化或类别级位姿估计，该文具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Category-level object pose estimation (COPE), capable of generalizing to intra-class unknown objects, has become a core technique for robotic 3D scene understanding. However, existing COPE methods still require labor-intensive recollection of real-world training data for novel object categories, which limits their scalability in practical applications. This paper aims to achieve synthetic-to-real (Syn2Real) generalized COPE, where a model is trained solely on rendered synthetic data and directly generalized to real-world deployments. The central challenge lies in the significant domain gap between synthetic and real-world data, particularly in texture appearance. To address this, we aim to enhance domain generalization by learning domain-invariant representations that capture semantic commonalities among objects within the same category. We introduce 2D and 3D semantic consistency constraints to reduce the sensitivity of feature encoders to domain-specific features. In addition, we propose an end-to-end pose regression framework that performs 2D-3D cross consistency learning, leveraging dense cross-modality fusion to further refine pose estimation. Since simplicity and effectiveness are essential for real-world robotic deployment, our model operates exclusively on global features, yielding a highly lightweight and efficient architecture. Extensive experiments on the REAL275 and Wild6D benchmarks, as well as real-world robotic manipulation scenes, show superior Syn2Real generalization performance of our paradigm. Code and demos are released at https://paperreview99.github.io/GenCOPE/.

</details>

#### 2026-10-01 - MEGA: Object-Level Mesh Extraction from 3D Gaussian Splatting via Spatial Visual Distillation

**Authors:** Liwei Liao, Yingkui Zhang, Qianqian Tong, Ronggang Wang
**Links:** [abs](https://arxiv.org/abs/2610.01707) - [pdf](https://arxiv.org/pdf/2610.01707)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** mesh reconstruction, surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MEGA: Object-Level Mesh Extraction from 3D Gaussian Splatting via Spatial Visual Distillation
- 作者：Liwei Liao, Yingkui Zhang, Qianqian Tong, Ronggang Wang
- 出版日期：2026-10-01T13:52:12Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.01707 ；https://arxiv.org/pdf/2610.01707

### 一句话总结
MEGA 提出一种“先分割、后建网格”的框架，通过空间视觉蒸馏（SVD）与掩码引导的神经表面重建模块，从复杂 3DGS 场景中提取对象级、水密（watertight）的网格。

### 研究问题
从 3D Gaussian Splatting（3DGS）中提取网格，旨在为 3D 高斯赋予准确几何结构，实现显式且精确的 3D 占用表示。但现有方法主要聚焦场景级网格提取，无法表示对象级占用，且常导致非水密表面。因此，论文关注的问题是如何从复杂 3DGS 场景中提取对象级、水密的网格。

### 核心思路/方法
论文提出 MEGA（Mesh Extraction from GAussians），是一个“segment-then-mesh”（先分割、后建网格）框架，用于从复杂 3DGS 场景中提取对象级、水密网格。其核心包括：
- 空间视觉蒸馏（Spatial Visual Distillation, SVD）：将 3DGS 模型视为教师模型，采样多样相机位姿，并渲染每个已分割对象对应的视图；这些观测随后通过光度监督用于训练网格重建模型。
- 掩码引导的神经表面重建模块：与 SVD 共同构成方法核心，用于从上述观测中重建对象级网格。

### 主要贡献
- 提出 MEGA，一个面向复杂 3DGS 场景的“segment-then-mesh”框架，用于提取对象级、水密网格。
- 引入空间视觉蒸馏（SVD），将 3DGS 作为教师模型，通过采样相机位姿并渲染分割对象视图，以光度监督方式训练网格重建模型。
- 结合掩码引导的神经表面重建模块，实现对对象级占用的恢复。
- 根据摘要，在多个广泛使用基准上的大量实验表明，MEGA 在恢复准确的对象级 3D 占用方面达到 state-of-the-art 性能。
- 摘要称 MEGA 通过结合高质量对象级网格（用于几何占用）与 3DGS 表示（用于照片级真实感渲染），支持复杂物理交互。

### 局限性
- 摘要未提供足够信息说明方法在计算开销、训练时间、内存占用方面的限制。
- 摘要未提供足够信息说明其对分割质量、相机采样策略或复杂场景类型的依赖与失败情形。
- 摘要未提供足够信息说明实验基准、评价指标、对比方法及消融实验的具体细节。
- 摘要未提供足够信息说明“复杂物理交互”的具体实现方式、验证场景与定量结果。

### 阅读优先级
高。理由：该论文聚焦 3DGS 到对象级水密网格提取这一明确且重要的问题，提出“segment-then-mesh”框架与空间视觉蒸馏思路，并声称在对象级 3D 占用上达到 state-of-the-art；若研究兴趣涉及 3D 重建、神经场景表示、3DGS 几何提取或对象级占用，值得优先阅读。但需注意，当前仅基于摘要，具体实验细节与局限需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Mesh extraction from 3D Gaussian Splatting (3DGS) aims to endow 3D Gaussians with accurate geometric structures, enabling explicit and precise 3D occupancy. However, existing methods primarily focus on scene-level mesh extraction, making them unable to represent object-level occupancy and often resulting in non-watertight surfaces. To overcome these limitations, we propose \textbf{MEGA} (\underline{M}esh \underline{E}xtraction from \underline{GA}ussians), a ``segment-then-mesh'' framework for extracting object-level, watertight meshes from complex 3DGS scenes. At the core of MEGA are \textbf{Spatial Visual Distillation (SVD)} and a mask-guided neural surface reconstruction module. SVD treats the 3DGS model as a teacher, sampling diverse camera poses and rendering the corresponding views of each segmented object. These observations are then used to train a mesh reconstruction model through photometric supervision. Extensive experiments on several widely used benchmarks demonstrate that MEGA achieves state-of-the-art performance in recovering accurate object-level 3D occupancy. Moreover, MEGA enables complex physical interactions by combining high-quality object-level meshes for geometric occupancy with 3DGS representations for photorealistic rendering.

</details>

#### 2026-10-01 - The Impact of Processing Parameters on High-Accuracy Measurements in UAV Photogrammetry

**Authors:** Paweł Ćwiąkała, Edyta Puniach, Elżbieta Pastucha, Wojciech Gruszczyński
**Links:** [abs](https://arxiv.org/abs/2610.01438) - [pdf](https://arxiv.org/pdf/2610.01438)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** photogrammetry, camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Impact of Processing Parameters on High-Accuracy Measurements in UAV Photogrammetry
- 作者：Paweł Ćwiąkała, Edyta Puniach, Elżbieta Pastucha, Wojciech Gruszczyński
- 出版日期：2026-10-01T10:34:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.01438) / [PDF](https://arxiv.org/pdf/2610.01438)

### 一句话总结
该研究通过 768 种处理变体的全因子实验，系统评估了 Bundle Block Adjustment 参数设置对 UAV 摄影测量 3D 精度及变形指标确定精度的影响。

### 研究问题
UAV 摄影测量被越来越多地用于滑坡、采矿、微地形变化等需要高精度的场景。虽然采集策略已被广泛研究，但处理流程——尤其是 Bundle Block Adjustment 参数设置——对最终精度的影响仍缺乏充分探索。本研究针对这一空白，考察处理参数如何影响最终 3D 精度以及位移、倾斜变化和水平应变确定的精度。

### 核心思路/方法
- 采用系统性、全因子评估方法，对 768 种处理变体进行测试。
- 数据基础为 1.5 年内、在 220 公顷研究区采集的十组 UAV 数据集。
- 分析了八个关键参数。
- 评估处理流程优化对位移、倾斜变化和水平应变确定精度的影响。
- 将优化配置与作者此前使用的基线配置进行对比。

### 主要贡献
- 揭示了最终 3D 精度存在显著变异性：最佳变体 RMSE 为 16 mm，最弱变体达到 303 mm。
- 识别出最具影响力的因素：地面控制点数量、附加相机标定校正的应用，以及使用 Post-Processing Kinematic GNSS 方法确定相机投影中心坐标。
- 在变形指标方面，随机位移误差保持稳定（RMSE 约 6–7 mm）；系统误差在所有轴上降低超过一半，垂直中位绝对误差从 14 mm 降至 7 mm（优化配置相较基线）。
- 据摘要所述，这是首个大规模、面向实践的处理参数选择对摄影测量产品和变形指标确定精度影响的评估，并为构建更稳健、可重复的高精度 UAV 摄影测量工作流提供可操作指导。

### 局限性
- 摘要未提供足够信息说明研究区具体地形、气候或地表覆盖条件对结论外推性的限制。
- 摘要未提供足够信息说明 768 种变体是否存在参数交互效应的详细统计显著性分析。
- 摘要未提供足够信息说明除 RMSE、中位绝对误差外的其他精度评价指标或验证方式。
- 摘要未提供足够信息说明该方法在非 220 公顷研究区、非 1.5 年数据跨度场景下的泛化能力。

### 阅读优先级
高。理由：该研究直接针对 UAV 摄影测量高精度应用中处理参数选择这一实践痛点，实验规模大（768 种变体、十组数据集、1.5 年跨度），量化了最佳与最差配置间的巨大精度差异（16 mm vs 303 mm），并给出可操作的工作流优化方向，对从事高精度变形监测、3D 重建和摄影测量流程设计的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Unmanned aerial vehicle (UAV) photogrammetry is increasingly used in applications requiring high accuracy, such as determining ground surface changes caused by landslides, mining, or microrelief transformation. While acquisition strategies have been widely studied, the influence of the processing workflow-particularly Bundle Block Adjustment parameter settings-remains insufficiently explored. This study addresses this gap through a systematic, full-factorial evaluation of 768 processing variants applied to ten UAV datasets collected over 1.5 years in a 220 ha study area. Eight key parameters were analysed. The results show substantial variability in final 3D accuracy: the best performing variant achieved a root mean square error (RMSE) of 16 mm, whereas the weakest reached 303 mm. The most influential factors were the number of ground control points, the application of additional camera calibration corrections, and the use of the Post-Processing Kinematic GNSS method for determining camera projection center coordinates. The study also evaluates how workflow optimization affects the accuracy of displacement, tilt changes, and horizontal strain determination. While random displacement errors remained stable (RMSE of ~6-7 mm), systematic errors were significantly reduced by over half in all axes, with vertical median absolute error decreasing from 14 mm to 7 mm in the optimized configuration compared to the baseline previously used by the authors. This study provides the first large-scale, practice-oriented assessment of how processing parameter selection shapes the accuracy of both photogrammetric products and deformation indices determination. The results offer actionable guidance for developing more robust and repeatable UAV photogrammetry workflows tailored to high-precision monitoring.

</details>

#### 2026-10-01 - Resolving Mixed Single-Photon LiDAR Returns for Foreground-View and Hidden Scene Reconstruction

**Authors:** Ziting Wen, Runrong Deng, Zili Zhang, Haitao Zheng, Yuecong Xu, Xiaoqiang Ren, Guodong Shi, Kemi Ding
**Links:** [abs](https://arxiv.org/abs/2610.01206) - [pdf](https://arxiv.org/pdf/2610.01206)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, scene representation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Resolving Mixed Single-Photon LiDAR Returns for Foreground-View and Hidden Scene Reconstruction
- 作者：Ziting Wen, Runrong Deng, Zili Zhang, Haitao Zheng, Yuecong Xu, Xiaoqiang Ren, Guodong Shi, Kemi Ding
- 出版日期：2026-10-01T07:15:54Z
- 分类：3D Reconstruction & Multi-view Geometry（无二级分类）
- 链接：摘要页 https://arxiv.org/abs/2610.01206 ；PDF https://arxiv.org/pdf/2610.01206

### 一句话总结
提出一种状态感知框架，从被部分透射遮挡物混合的单光子 LiDAR 直方图中同时重建前景视图与被遮挡场景，并配套一个真实配对遮挡数据集。

### 研究问题
部分透射屏幕与防护罩在机器人巡检中十分常见，会使 LiDAR 同时接收到前景材料和其后场景的混合回波。传统基于峰值的 LiDAR 通常会丢弃较弱的隐藏回波；单光子 LiDAR 虽能记录保留衰减与重叠回波的时间分辨直方图，但现有瞬态重建方法通常只对测得波形拟合单一场景表示。在遮挡下，较弱或距离较近的前景—隐藏回波可能形成宽峰或微弱肩部；而这类波形同样可被“位移的单表面”或“较厚密度分布”解释，因此准确的瞬态拟合并不必然意味着几何正确。

### 核心思路/方法
- 面向被遮挡的单光子直方图，提出状态感知（state-aware）框架，用于前景视图与隐藏场景重建。
- 对每条光线估计局部回波证据，将回波状态判定为：无可可靠表面证据、单回波证据、双回波三类。
- 推断出的回波状态用于路由监督一个双头神经场（two-head neural field）：所有光线都约束波形重建，而可靠锚点提供几何定位。
- 同时引入一个真实配对单光子 LiDAR 遮挡数据集，在同一固定位姿下采集遮挡与干净（无遮挡）数据。

### 主要贡献
- 提出状态感知框架，从被遮挡单光子直方图中进行前景视图与隐藏场景重建。
- 通过逐光线回波证据估计（无可靠表面/单回波/双回波）来路由双头神经场的监督，以缓解“波形拟合正确但几何错误”的歧义。
- 引入真实配对单光子 LiDAR 遮挡数据集（固定位姿下的遮挡与干净采集）。
- 在真实数据集上的实验表明，相比基线方法，隐藏场景深度与点云精度有所提升；结果说明单光子分层重建是穿过部分透射遮挡物进行 3D 感知的可行路径。

### 局限性
- 摘要未提供足够信息说明方法的失效场景、适用遮挡物类型范围、对极端弱回波或强噪声的鲁棒性边界。
- 摘要未提供足够信息说明数据集的规模、场景多样性、采集设备与标注细节。
- 摘要未提供足够信息说明与基线方法的定量对比数值、评价指标定义及消融实验情况。
- 摘要未提供足够信息说明计算开销、实时性与可扩展性。

### 阅读优先级
高。理由：该工作针对“部分透射遮挡下的混合单光子回波”这一具有明确实际动机的问题，提出了状态感知与双头神经场相结合的重建思路，并配套真实配对数据集；对单光子 LiDAR、遮挡场景重建与 3D 感知方向的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Partially transmissive screens and protective covers are common in robotic inspection, but they create mixed LiDAR returns from both the foreground material and the scene behind it. Conventional peak-based LiDAR usually discards weak hidden returns, while single-photon LiDAR records time-resolved histograms that preserve attenuated and overlapping echoes. However, existing transient reconstruction methods typically fit a single scene representation to the measured waveform. Under occlusion, weak or nearby foreground--hidden echoes can form a broad peak or subtle shoulder. Because such waveforms can also be explained by a displaced single surface or a thick density distribution, accurate transient fitting does not necessarily imply correct geometry. We propose a state-aware framework for foreground-view and hidden scene reconstruction from occluded single-photon histograms. For each ray, we estimate local echo evidence, identifying no reliable surface evidence, single-return evidence, or two returns. The inferred echo state routes supervision for a two-head neural field: all rays constrain waveform reconstruction, while reliable anchors provide geometry localization. We also introduce a real paired single-photon LiDAR occlusion dataset with occluded and clean captures at fixed poses. Experiments on a real dataset show improved hidden scene depth and point-cloud accuracy over baselines. Our results demonstrate single-photon layered reconstruction as a practical route for 3D perception through partially transmissive occluders.

</details>

#### 2026-10-01 - Semantic RGB--Depth Based Surgical Skill Assessment in Microscopic Stereo Videos

**Authors:** Jecia Z. Y. Mao, Sue M. Cho, Francis X. Creighton, Deepa Galaiya, Russell H. Taylor, Manish Sahu
**Links:** [abs](https://arxiv.org/abs/2610.01205) - [pdf](https://arxiv.org/pdf/2610.01205)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** monocular depth, stereo depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Semantic RGB--Depth Based Surgical Skill Assessment in Microscopic Stereo Videos
- 作者：Jecia Z. Y. Mao, Sue M. Cho, Francis X. Creighton, Deepa Galaiya, Russell H. Taylor, Manish Sahu
- 出版日期：2026-10-01T07:15:49Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.01205

### 一句话总结
本文提出一种语义 RGB-Depth 框架，利用显微镜立体视频中的深度信息与语义分解的 RGB 流，通过分层注意力架构进行手术技能等级分类。

### 研究问题
显微外科技术技能的客观评估对基于能力的培训和质量保证至关重要，但现有基于视频的方法主要依赖 RGB 图像，忽略了器械—解剖结构交互的 3D 空间关系。虽然立体手术显微镜可提供互补的深度信息，但传统立体匹配算法在高放大成像条件下会产生稀疏且不可靠的深度估计，限制了其在自动化技能评估中的应用。

### 核心思路/方法
提出语义 RGB-Depth 手术技能评估框架。采用基于回归的深度融合方法，将稀疏的度量立体深度与密集的单目深度估计相结合，生成手术场景的密集几何表示。该表示与语义分解的 RGB 流（对应单个手术器械和周围解剖结构）相集成。使用分层注意力架构联合编码这些流，以捕捉不同培训水平外科医生在器械使用和器械—解剖结构交互方面的判别性模式。

### 主要贡献
- 提出语义 RGB-Depth 框架，将稀疏立体深度与密集单目深度融合为密集几何表示，用于显微立体视频的手术技能评估。
- 将几何表示与语义分解的器械及解剖结构 RGB 流结合，并通过分层注意力架构联合编码。
- 在 33 例离体经口显微喉部手术（6 名外科医生，包括主治医师和住院医师）上采用留一外科医生交叉验证进行评估：所提语义 RGB-Depth 模型的技能等级分类 F1 为 0.938，而语义 RGB 为 0.696，语义深度为 0.929。
- 学习的空间、时间和语义注意力模式可支持对模型关注区域、视频片段和语义流进行定性检查。

### 局限性
摘要未提供足够信息（如计算成本、实时性、跨机构泛化能力、深度估计误差的详细分析等均未提及）。

### 阅读优先级
高。理由：该工作针对显微外科技能评估中 RGB 方法忽略 3D 空间关系的问题，提出了明确的语义 RGB-Depth 融合方案，并在摘要中报告了相对语义 RGB 的显著 F1 提升（0.938 对 0.696），主题与 3D 重建及多视角几何分类相关，且涉及医学图像与技能评估交叉方向，具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Objective assessment of microsurgical technical skill is essential for competency-based training and quality assurance, yet existing video-based approaches predominantly rely on RGB images and therefore overlook the 3D spatial relationships that characterize instrument-anatomy interactions. Although stereo operating microscopes provide complementary depth information, conventional stereo matching algorithms can produce sparse and unreliable depth estimates under high-magnification imaging conditions, limiting their use for automated skill assessment. This work presents a semantic RGB-Depth framework for surgical skill assessment from microscopic stereo videos. A regression-based depth fusion method combines sparse metric stereo depth with dense monocular depth estimates to generate a dense geometric representation of the surgical scene. This representation is integrated with semantically decomposed RGB streams corresponding to individual surgical instruments and surrounding anatomy. A hierarchical attention architecture jointly encodes these streams to capture discriminative patterns of instrument use and instrument-anatomy interaction across surgeons at different training levels. The framework was evaluated on 33 ex vivo transoral microlaryngeal procedures performed by six surgeons, comprising attending surgeons and surgical residents, using leave-one-surgeon-out cross-validation. The proposed semantic RGB-Depth model achieved an F1 score of 0.938 for skill-level classification, compared with 0.696 for semantic RGB and 0.929 for semantic depth. These results suggest that geometric information can improve automated surgical skill assessment from microscopic stereo videos. The learned spatial, temporal, and semantic attention patterns also support qualitative examination of the scene regions, video segments, and semantic streams emphasized by the model.

</details>

#### 2026-10-01 - quARtet Marker: A 3D-Printable Multi-Tag Fiducial for Robust Near-Frontal Pose Estimation

**Authors:** Araki Wakiuchi, Hikaru Sasaki, Takamitsu Matsubara
**Links:** [abs](https://arxiv.org/abs/2610.01072) - [pdf](https://arxiv.org/pdf/2610.01072)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：quARtet Marker: A 3D-Printable Multi-Tag Fiducial for Robust Near-Frontal Pose Estimation
- 作者：Araki Wakiuchi, Hikaru Sasaki, Takamitsu Matsubara
- 出版日期：2026-10-01T05:13:15Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类；次要分类未提供）
- 链接：摘要页 https://arxiv.org/abs/2610.01072 ；PDF https://arxiv.org/pdf/2610.01072

### 一句话总结
提出一种可3D打印的多标签基准物 quARtet marker，通过在紧凑足迹内倾斜布置四个 AprilTag，使标记正面朝向相机时各标签仍处于非正面视角，从而提升近正面位姿估计的稳健性，并在三种布局间权衡位姿估计一致性与抓取性。

### 研究问题
实验室器具操作中，透明或反射物体的识别与定位较困难。编码平面基准标记是实用的改造方案：易于打印，且标记面保持平整、可抓取。然而单个平面标签在近正面视角下最不可靠，因为透视线索消失。非平面几何结构可恢复这些线索，但会侵入平行夹爪必须接触的平整表面。因此核心问题是：如何在不破坏可抓取平整面的前提下，改善近正面视角下的位姿估计可靠性。

### 核心思路/方法
核心思路是在一个紧凑足迹内倾斜多个标签，使标记即使正对相机，每个标签也被以非正面角度观测。

具体方法：
- 提出 quARtet marker，一种可3D打印的基准物，体现上述思路。
- 其四个倾斜 AprilTag 的所有被检测角点进入同一次 Perspective-n-Point（PnP）求解。
- 使用一套共享配置同时定义制造几何与检测器模型。
- 由于倾斜会占用平坦面积，提出三种布局，在位姿估计一致性与可抓取性之间权衡。

### 主要贡献
- 提出 quARtet marker 这一可3D打印的多标签基准物设计，通过倾斜多标签在近正面视角下保留透视线索。
- 采用统一 PnP 求解融合四个倾斜 AprilTag 的全部检测角点，并以共享配置连接制造几何与检测器模型。
- 提出三种布局，明确权衡位姿估计一致性与抓取性。
- 实验结果显示：在机器人参考系、同一装置、固定相机实验中，三种布局将平均正面朝向误差从单个平面标签的 2.18 度降至 0.24–0.47 度，均方根位置误差从 1.50 mm 降至 0.17–0.20 mm。
- 机器人搭载相机的位姿保持测试在闭环视觉反馈下确认了这种分离。
- 在相同条件下的摆落试验中，带平整接触条的两种布局约保留 2 mm 的抓取内滑动，而无平整条布局滑动约 100 mm。
- 在测试条件下支持一条规则：位姿估计一致性优先时选无平整条布局，标记面必须保持可抓取时选带平整条布局。

### 局限性
- 摘要未提供足够信息说明实验的具体硬件配置、相机型号、标记尺寸、工作距离范围等细节。
- 摘要未提供足够信息说明三种布局的完整几何参数与设计差异的量化描述。
- 摘要未提供足够信息说明透明或反射物体的实际实验结果；摘要仅提及这类物体是动机背景。
- 摘要未提供足够信息说明摆落试验的具体条件、次数与统计方差。
- 摘要未提供足够信息说明与其他非平面基准或替代方案的对比。
- 摘要未提供足够信息说明该方法是否适用于其他类型标签或更广泛的视角范围。

### 阅读优先级
中。理由：该工作针对近正面位姿估计这一明确痛点提出可3D打印的实用设计，并给出位姿误差与抓取滑动的定量结果及布局选择规则，对机器人操作与视觉基准设计有参考价值；但摘要未提供足够信息说明完整实验细节、消融与对比，若需深入评估方法泛化性与设计参数影响，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation of labware is difficult when transparent or reflective objects must be identified and localized. Coded planar fiducials are a practical retrofit: easy to print, they leave the marked face flat and graspable. Yet a single planar tag is least reliable in near-frontal views, where perspective cues fade. Non-planar geometries restore those cues but intrude on the flat face that a parallel-jaw gripper must contact. Our idea is to tilt multiple tags within one compact footprint, so that each tag is seen at a non-frontal angle even when the marker faces the camera. We propose the quARtet marker, a 3D-printable fiducial embodying this idea: all detected corners of its four tilted AprilTags enter one Perspective-n-Point solve, and a shared configuration defines the fabricated geometry and the detector model. Because tilting consumes flat area, its three layouts trade pose-estimation consistency against graspability. In robot-referenced, same-setup fixed-camera experiments, all three layouts reduced the mean frontal orientation error from 2.18 degree for a single planar tag to 0.24-0.47 degree and the root-mean-square position error from 1.50 to 0.17-0.20 mm. A robot-mounted-camera pose-hold test confirmed this separation under closed-loop visual feedback. In swing-down trials under identical conditions, the two layouts with flat contact strips retained the object with about 2 mm of in-grasp slip, whereas the layout without flat strips slipped by roughly 100 mm. For the tested conditions, the results support a rule: the layout without flat strips when pose-estimation consistency dominates, a layout with flat strips when the marked face must remain graspable.

</details>

#### 2026-10-01 - HierGF: Hierarchical Gaussian Fields via Geometry-perception Message Passing for Sparse-view 3D Reconstruction

**Authors:** Bi'an Du, Zhimin Zhang, Daizong Liu, Baoquan Chen, Wei Hu
**Links:** [abs](https://arxiv.org/abs/2610.01056) - [pdf](https://arxiv.org/pdf/2610.01056)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, AR, augmented reality, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HierGF: Hierarchical Gaussian Fields via Geometry-perception Message Passing for Sparse-view 3D Reconstruction
- 作者：Bi'an Du, Zhimin Zhang, Daizong Liu, Baoquan Chen, Wei Hu
- 出版日期：2026-10-01T04:50:55Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.01056 ；PDF https://arxiv.org/pdf/2610.01056

### 一句话总结
论文提出 HierGF（分层高斯场），从分层几何感知视角处理稀疏视角 3D 重建，通过将粗 3D 几何信息与额外 2D 生成先验转化为结构化伪监督，以缓解多视角一致性不足与欠采样区域结构缺失问题。摘要未提供足够信息说明其具体实验表现。

### 研究问题
论文关注稀疏视角 3D 重建这一多媒体应用场景，包括 AR/VR 内容创建、文化遗产数字化和部分机器人应用；这些场景中可能只有少量随机采集的视角可用。稀疏视角包含的 3D 信息有限，带来两个主要挑战：
1. 可用于匹配的图像过少，难以建立多视角一致性；
2. 视角覆盖不足导致欠采样区域信息缺乏，造成物体结构缺失。

摘要还指出，现有方法大多依赖有限的重投影误差和正则项，容易过拟合到单一视角，并出现跨视角外观不一致；在几何欠采样区域，它们常依赖启发式密度控制，缺乏可靠引导，往往导致模糊和结构空洞。

### 核心思路/方法
论文提出 Hierarchical Gaussian Fields（HierGF），从分层几何感知视角重新审视稀疏视角重建，目标是把有限观测转化为可靠的自生成监督，超越固定先验和启发式密度控制。

具体而言：
- 通过两阶段几何感知骨干网络，将粗 3D 几何信息和额外 2D 生成先验转化为结构化伪监督，从而在极少量输入视角下增强多视角一致性。
- 引入可学习置信度网络，引导梯度朝向跨视角一致的内容。
- 引入几何一致致密化模块，以改善多视角对齐和欠采样区域的重建。

摘要未提供足够信息说明该方法的网络结构细节、训练流程、损失函数形式或具体实现参数。

### 主要贡献
- 提出 HierGF，从分层几何感知角度处理稀疏视角 3D 重建问题。
- 将粗 3D 几何信息与额外 2D 生成先验转化为结构化伪监督，以增强极少输入视角下的多视角一致性。
- 引入可学习置信度网络，引导梯度朝向跨视角一致内容。
- 引入几何一致致密化模块，改善多视角对齐与欠采样区域重建。

摘要未提供足够信息说明其与现有方法的具体量化对比、消融实验结论或应用验证范围。

### 局限性
摘要未提供足够信息说明论文的局限性。摘要中未报告失败案例、计算开销、对先验质量的依赖程度、适用场景边界或实验未覆盖情况。

### 阅读优先级
中。理由：该论文聚焦稀疏视角 3D 重建这一明确且常见的问题，并提出分层几何感知、结构化伪监督、可学习置信度网络和几何一致致密化等思路；若读者关注 3D Reconstruction & Multi-view Geometry 或 AR/VR、机器人相关三维重建，具有潜在参考价值。但摘要未提供实验设置、量化结果、与基线对比和局限性信息，因此无法仅凭元数据和摘要判断其实际效果与稳健性，优先级不宜直接定为高。

</details>

<details>
<summary>Abstract</summary>

Sparse view 3D reconstruction is an important and common scenario in multimedia applications, such as augmented reality/virtual reality (AR/VR) content creation, cultural heritage digitization, and certain robotic applications, where only a limited number of randomly captured views may be available. However, sparse views contain only limited 3D information, posing two major challenges:1) too few images are available for matching, making it difficult to build multi-view consistency; 2) insufficient view coverage leads to a lack of information in under-sampled regions, resulting in missing parts of object structure. Existing methods mostly still rely on limited reprojection errors and regularization terms, which are prone to overfitting to a single view and inconsistent appearances across views. In geometrically under-sampled regions, they often rely on heuristic density control, lacking reliable guidance and often resulting in blurring and structural holes.To address these issues, this paper proposes Hierarchical Gaussian Fields (HierGF), which revisits sparse-view reconstruction from a hierarchical geometry-perception perspective and converts limited observations into reliable self-generated supervision beyond fixed priors and heuristic density control. In particular, we transform coarse 3D geometric information and additional 2D generative priors into structured pseudo-supervision through a two-stage geometry-perception backbone network, thereby enhancing multi-view consistency with very few input views. In addition, we introduce a learnable confidence network to guide gradients toward cross-view consistent content, and a geometrically consistent densification module to improve the reconstruction of multi-view alignment and under-sampled regions.

</details>

### 2026-09

#### 2026-09-30 - Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation

**Authors:** Sanya Verma, Luca Cilio, Velissarios Christodoulou
**Links:** [abs](https://arxiv.org/abs/2610.00731) - [pdf](https://arxiv.org/pdf/2610.00731)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation
- 作者：Sanya Verma, Luca Cilio, Velissarios Christodoulou
- 出版日期：2026-09-30T21:22:08Z
- 分类：3D Reconstruction & Multi-view Geometry（次要分类：未提供）
- 链接：[摘要](https://arxiv.org/abs/2610.00731) / [PDF](https://arxiv.org/pdf/2610.00731)

### 一句话总结
论文通过在同一双臂机器人单元上构建“定制重建”与“默认开源重建”两套仿真环境并进行对照实验，发现提高重建质量（视觉保真度、物理参数定制、度量尺度）能显著提升仿真评分与真实评分的相关性，并缩小 sim-to-real 差距。

### 研究问题
仿真评估在机器人策略评测中越来越常用于替代或补充真实评估，其价值取决于仿真结果能否紧密跟随真实机器人的表现。论文要检验：一种结合度量尺度物体几何、自定义物理参数与场景重建的流程，相比默认开源方案，是否能减少仿真与真实机器人评分之间的不一致。

### 核心思路/方法
- 构建同一个双臂机器人单元的两个仿真版本：
  - **定制重建（authored reconstruction）**：使用估计度量尺度下的物体几何、投影纹理、自定义物理参数，以及自研场景 splat。
  - **默认重建（default reconstruction）**：采用开源方案，即基于生成式单图网格、引擎默认物理和 Gaussian-splat 场景。
- 两种重建使用相同的物体照片与场景视频。
- 两个策略各运行五个任务，形成十个“任务—策略”对（称为 cells）。
- 每个 cell 在每种重建下运行二十次，其余设置保持不变。
- 两种重建均以同一批真实试验为评分基准，由第三方评估者打分。
- 比较指标为十个 cell 均值下仿真与真实评分之间的 Pearson 相关系数，以及平均分数误差。

### 主要贡献
- 报告了定制重建与默认重建在仿真—真实评分一致性上的量化对比：
  - Pearson 相关系数：定制重建 r = 0.90，默认重建 r = 0.51。
  - 平均分数误差：定制重建 6.97 个百分点，默认重建 17.54 个百分点，减少 10.56 个百分点。
- 结论表明：通过更高视觉保真度、自定义物理和度量尺度提升环境重建质量，可使仿真更贴近真实世界，缩小 sim-to-real 差距。
- 释放了测试框架、逐次试验评分、所有报告运行的配置，以及两种重建的资产与场景。

### 局限性
- 实验仅基于一个双臂机器人单元，摘要未提供跨更多机器人平台或场景的验证信息。
- 仅涉及两个策略、五个任务、十个 cell，摘要未提供更大规模任务或策略多样性的信息。
- 真实评分仅由第三方评估者给出，摘要未提供评分者数量、一致性或评分协议细节。
- 摘要未提供物理参数的具体设定方式、度量尺度估计误差、纹理与 splat 质量指标的细节。
- 摘要未提供计算成本、重建耗时或可扩展性分析。
- 摘要未提供统计显著性检验或置信区间信息。
- 摘要未提供基线开源方案的具体名称与版本信息。
- 摘要未提供失败案例或两套重建在哪些任务上差异最大的分析。

### 阅读优先级
**中**。理由：该论文聚焦 real-to-sim 评估中的重建质量对 sim-to-real 一致性的影响，问题明确、对照设计清晰，并报告了相关系数与平均误差的量化结果，对从事机器人仿真评估与 3D 重建应用的研究者有直接参考价值。但实验规模限于单一机器人单元、两个策略与五个任务，且摘要未提供统计显著性与更广泛的泛化验证，因此优先度定为中等而非高；若读者关注 sim-to-real 评估协议或重建资产对策略评分的影响，则可优先阅读。

</details>

<details>
<summary>Abstract</summary>

Simulated evaluation is increasingly used alongside real-world evaluation of robot policies because it is cheaper and easier to repeat; however, its value depends on how closely its outcomes track the real robot's. We test whether our reconstruction pipeline, combining metrically scaled object geometry, authored physical parameters and scene reconstruction, reduces disagreement between simulated and real robot scores relative to a default open-source recipe. We constructed two simulated versions of one bimanual robot cell: an authored reconstruction, using object geometry at estimated metric scale, projected textures, authored physics and our own scene splat; and a baseline, referred to as the default reconstruction, using the open-source recipe of a generative single-image mesh, engine-default physics and a Gaussian-splat scene. Both reconstructions use the same object photographs and scene video. Two policies ran five tasks each, giving ten task-policy pairs, which we call cells; each cell was run twenty times in each reconstruction with all other settings held fixed. Both reconstructions were scored against the same real trials, graded by a third-party evaluator. Pearson correlation between the ten simulated and real cell means is r = 0.90 for the authored reconstruction and 0.51 for the default. Mean score error is 6.97 percentage points for the authored reconstruction and 17.54 for the default, a reduction of 10.56 percentage points. These results show that improving the quality of the environment reconstruction through higher visual fidelity, authored physics and metric scale makes the simulation more faithful to the real world and narrows the sim-to-real gap. We release the harness, the per-trial scores, every reported run's configuration, and the assets and scenes of both reconstructions.

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-06 - Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error

**Authors:** Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González
**Links:** [abs](https://arxiv.org/abs/2610.08756) - [pdf](https://arxiv.org/pdf/2610.08756)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Transfer Error
- 作者：Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González
- 出版日期：2026-10-06T17:47:47Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.08756) | [PDF](https://arxiv.org/pdf/2610.08756)

### 一句话总结
提出一种面向 3D Gaussian Splatting 的后训练语义提升方法，通过跨视角累积目标/非目标证据并按可见性加权，再用双阈值过滤高斯，从而将 2D 检测器、语义提升与表示间标签迁移三类误差分离开来。

### 研究问题
3D Gaussian Splatting 中的同一个高斯会被多个视角观测，但不同视角对其类别的判断并不总是一致：有些视角下该高斯被遮挡，检测器在不同视角下的置信度也不同。此外，真值以带标注的网格形式给出，因为两次训练运行不会产生相同的高斯。因此论文关注如何在多视角不一致、遮挡与置信度差异下进行语义提升，并区分误差来源。

### 核心思路/方法
- 提出一种后训练（post-training）语义提升方法，每次处理一个目标类别。
- 同时累积“目标”和“非目标”证据，并按每个高斯在每个视角中的可见性进行加权。
- 高斯过滤使用两个阈值：主阈值 β 选取高置信度种子，较低的阈值 γβ 用于补充其周围的连通分量。
- 评估时将标签从高斯迁移到既可见又有标注的网格顶点。
- 该设计可分离三类误差来源：2D 检测器、语义提升、以及两种表示之间的标签迁移。
- 阈值与迁移算子基于七个 Replica 验证场景选择，并在十个留出的 ScanNet++ 场景上以对所有场景和类别相同的取值进行评估。

### 主要贡献
- 提出一种跨视角融合、按可见性加权的后训练语义提升方法，一次处理一个目标类别。
- 采用双阈值策略（β 与 γβ）过滤高斯，兼顾高置信种子与周围连通分量。
- 通过将标签从高斯迁移到可见且标注的网格顶点，实现对三类误差来源的分离分析。
- 与逐视角阈值化证据的先前版本相比，该方法在测试 mIoU 上提升 0.24，并使两个数据集的所有类别和场景可共用一个单一阈值。
- 误差分析显示，剩余误差主要来自检测器。

### 局限性
- 摘要未提供足够信息说明方法对更多类别、更复杂场景或不同类型检测器的泛化能力。
- 摘要未提供足够信息说明双阈值 β 与 γβ 的具体取值、敏感性或调参成本。
- 摘要未提供足够信息说明在遮挡严重或视角一致性极差情况下的具体失败模式。
- 摘要未提供足够信息说明训练时间、推理开销或计算资源需求。
- 摘要未提供足够信息说明与更多现有语义提升方法的全面对比。

### 阅读优先级
中。理由：该工作聚焦 3D Gaussian Splatting 的语义提升与误差分解，问题定义清晰，且给出跨数据集的量化结果（验证集 mIoU 0.93/0.65，测试集 0.80/0.54），对关注 3D 语义表示与误差分析的研究者有参考价值；但摘要未展示与广泛基线方法的系统对比，也未提供方法细节与开源信息，因此优先级为中等。

</details>

<details>
<summary>Abstract</summary>

The same Gaussian of a 3D Gaussian Splatting model is seen from many views, and these views do not always agree on the class it belongs to. The Gaussian may be occluded in some of them, and the confidence of the detector is not the same from one view to another. The ground truth, on the other hand, is given as an annotated mesh, because two training runs do not produce the same Gaussians. In this work, we propose a post-training lifting method that works with one target class at a time and combines the information coming from all the views. Target and non-target evidence are accumulated simultaneously, weighted by the visibility of each Gaussian in each view. After that, the Gaussians are filtered with two thresholds: a main threshold $β$ selects the high-confidence seeds, and a lower one $γβ$ adds the connected components around them. For the evaluation, the labels are transferred from the Gaussians to the mesh vertices that are both visible and annotated. With this design, we can separate three sources of error: the 2D detector, the lifting and the transfer between representations. The thresholds and the transfer operator are chosen on seven Replica validation scenes, and the method is evaluated on ten held-out ScanNet++ scenes with the same values for every scene and class. The mean mIoU on the validation scenes was 0.93 with masks from the dataset annotations and 0.65 with YOLO masks, and on the ScanNet++ test scenes it was 0.80 and 0.54. Compared with thresholding the evidence per view, as a previous version of the method did, the fraction improves the test mIoU by 0.24 and makes it possible to use a single threshold for all the classes and scenes of both datasets. Finally, the error analysis shows that most of the remaining error comes from the detector.

</details>

#### 2026-10-06 - DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given

**Authors:** Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee
**Links:** [abs](https://arxiv.org/abs/2610.07958) - [pdf](https://arxiv.org/pdf/2610.07958)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given
- 作者：Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee
- 出版日期：2026-10-06T08:29:41Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.07958) | [PDF](https://arxiv.org/pdf/2610.07958)

### 一句话总结
DensiTok 是一个可插拔模块，通过在低维隐空间中补全前馈 3DGS 模型内部几何 token，使冻结骨干网络在稀疏视角输入下表现出“看到更多视角”的效果。

### 研究问题
前馈 3D Gaussian Splatting（3DGS）通过单次前向传播重建场景，但其质量在输入图像数量减少时会急剧下降。摘要指出，瓶颈位于重建头之前：从少量无位姿视角出发，模型内部表示中缺乏未观测区域的证据，导致空洞、浮点和模糊。常见做法是用图像或视频生成器合成额外视角像素再重新编码，但这种方式成本高，且本身不具备 3D 一致性。

### 核心思路/方法
- 不合成额外图像像素，而是“加密证据本身”，即直接对内部几何 token 进行致密化。
- DensiTok 作为预训练前馈 3DGS 模型的插件模块，保持骨干网络和重建头冻结。
- 将几何 token 压缩到紧凑隐空间，在相机几何条件下以单步 flow-matching 补全未观测视角的隐变量，再解码回 token 供原重建头使用。
- 由于在低维隐空间完成补全，不需要图像合成，也不需要额外编码器前向传播。
- 同一模块设计可集成到不同的预训练预测器中。

### 主要贡献
- 提出 DensiTok，一种直接致密化前馈 3DGS 内部几何 token 的插件模块。
- 通过隐空间补全而非像素合成来提供未观测区域证据，避免额外图像生成与重新编码开销。
- 在保持各骨干网络及其重建头冻结的情况下，可集成到不同预训练预测器中。
- 摘要称在三个预训练骨干和两个基准上，DensiTok 一致改善稀疏视角重建，并缩小了与密集视角重建的差距。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算开销细节、对相机位姿质量的依赖程度、隐空间补全的误差上界，以及在不同数据集或极端稀疏条件下的泛化表现。实验细节、消融结果和定量指标均未在摘要中给出。

### 阅读优先级
中。理由：该工作针对前馈 3DGS 在稀疏视角下的关键瓶颈提出模块化、免图像合成的隐空间补全思路，且声称跨多个骨干和基准一致有效，具有较强的问题针对性和方法普适性；但摘要未给出实验细节、定量结果与失败案例分析，需进一步阅读正文才能判断其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) reconstructs a scene in a single forward pass, replacing per-scene optimization with a network trained across many scenes. Its quality, however, degrades sharply as the number of input images drops. The bottleneck is upstream of the reconstruction heads: from a few unposed views, the internal representation they read carries no evidence for unobserved regions, leaving holes, floaters, and blur. The common remedy supplies that evidence as pixels, synthesizing extra views with an image or video generator and re-encoding them, which is costly and not 3D-consistent by construction. We instead densify the evidence itself. We present DensiTok, a plug-in module for pretrained feed-forward 3DGS models that densifies their internal geometry tokens directly, making a frozen backbone behave as though it had observed many more views than it was given. DensiTok compresses those tokens into a compact latent space, completes the latents of the unobserved viewpoints in a single flow-matching step conditioned on camera geometry, and decodes them back into tokens that the original reconstruction heads. The same module design can be integrated into different pretrained predictors while keeping each backbone and its reconstruction heads frozen. Completion in a low-dimensional latent space requires no image synthesis or additional encoder passes. Across three pretrained backbones and two benchmarks, DensiTok consistently improves sparse-view reconstruction and recovers much of the gap to dense-view reconstruction.

</details>

#### 2026-10-06 - Efficient Gaussian Splatting Sequence Compression with Standard Video Codecs

**Authors:** Qi Yang, Shuting Xia, Le Yang, Geert Van Der Auwera, Zhu Li
**Links:** [abs](https://arxiv.org/abs/2610.07795) - [pdf](https://arxiv.org/pdf/2610.07795)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Efficient Gaussian Splatting Sequence Compression with Standard Video Codecs
- 作者：Qi Yang, Shuting Xia, Le Yang, Geert Van Der Auwera, Zhu Li
- 出版日期：2026-10-06T05:43:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2610.07795 ；PDF 链接 https://arxiv.org/pdf/2610.07795 ；代码 https://github.com/Qi-Yangsjtu/GSCV

### 一句话总结
论文提出 GSCV，一种利用标准视频编解码器压缩高斯泼溅（GS）序列的方法，通过 Inter-PLAS 增强 GS 图像在 I 帧与 P 帧之间的帧间相关性，并采用高比特深度 GS 图像的新流程提升可压缩性与质量上限。

### 研究问题
论文关注 GS 序列压缩问题。摘要指出，现有基于视频的 GS 序列压缩依赖 Parallel Linear Assignment Sorting（PLAS）和被跟踪的基元信息，将 GS 转换为平滑的 2D 视频；但在大多数实际应用中，被跟踪信息并不可用。缺少该信息时，直接使用原始 PLAS 会因其随机性导致生成图像的帧间相关性较弱，从而影响视频编解码器的帧间压缩性能。

### 核心思路/方法
论文提出的方法名为 GSCV，用于 GS 序列压缩，并利用视频编解码器。针对原始 PLAS 在缺少被跟踪信息时帧间相关性弱的问题，GSCV 引入了一种简单而高效的 Inter-PLAS 方法，使 GS 在 I 帧和 P 帧之间生成更接近的图像，从而显著增强视频编解码器的帧间性能。此外，GSCV 基于最先进的视频编解码器实现了一个新流程，处理高比特深度 GS 图像，从而在提供更高质量上限的同时实现更高的可压缩性。

### 主要贡献
- 提出 GSCV，一种利用标准视频编解码器进行 GS 序列压缩的有效方法。
- 提出 Inter-PLAS，用于在 I 帧与 P 帧之间生成更接近的 GS 图像，提升视频编解码器的帧间性能。
- 实现基于最先进视频编解码器与高比特深度 GS 图像的新流程，提升可压缩性并提供更高质量上限。
- 实验结果表明，GSCV 在 GS 序列压缩方面相较 MPEG 视频锚点和基于点云的锚点有明显提升。
- 公开代码链接。

### 局限性
摘要未提供足够信息说明 GSCV 的具体计算开销、实时性、对不同 GS 表示或数据集的泛化能力，以及与更多基线方法的完整对比细节。摘要未提供足够信息说明 Inter-PLAS 的具体实现细节和参数敏感性。摘要未提供足够信息说明高比特深度流程对兼容性和部署成本的影响。

### 阅读优先级
中。理由：该论文聚焦 GS 序列压缩与标准视频编解码器结合，问题明确，且摘要声称相较 MPEG 视频和点云锚点有性能提升，并公开代码，对 GS 压缩、视频编码和神经场景表示方向的研究者有参考价值。但用户未提供额外兴趣方向，且摘要未展开实验细节，因此优先级定为中而非高。

</details>

<details>
<summary>Abstract</summary>

This paper presents a novel effective Gaussian Splatting (GS) sequence Compression method that utilizes the Video codec (GSCV). Existing video-based GS sequence compression relies on the Parallel Linear Assignment Sorting (PLAS) and tracked primitive information to convert GS into smooth 2D videos. However, tracked information is not available for most practical applications, and without it, using the vanilla PLAS can generate images exhibiting weak inter-frame correlation, due to its stochastic nature. GSCV incorporates a simple yet efficient Inter-PLAS method to produce close images between the I- and P-frames of GS, enhancing the inter-frame performance of video codec greatly. GSCV also realizes a new pipeline based on the state-of-the-art video codecs with high bit-depth GS images, achieving higher compressibility while simultaneously providing a higher quality upper bound. Experimental results show that the proposed GSCV exhibits obviously improved performance over MPEG video and point cloud-based anchors in GS sequence compression. The code is available at https://github.com/Qi-Yangsjtu/GSCV.

</details>

#### 2026-10-06 - OntoPlan: An Ontology-Grounded Scene Representation and Agentic Framework for Scalable Robot Task Planning

**Authors:** Hyeongwoo Nam, Woongje Cho, Juwon Kim, Jongeun Choi
**Links:** [abs](https://arxiv.org/abs/2610.07649) - [pdf](https://arxiv.org/pdf/2610.07649)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OntoPlan: An Ontology-Grounded Scene Representation and Agentic Framework for Scalable Robot Task Planning
- 作者：Hyeongwoo Nam, Woongje Cho, Juwon Kim, Jongeun Choi
- 出版日期：2026-10-06T02:45:03Z
- 分类：Neural Scene Representations & Rendering（主分类；未提供次级分类）
- 链接：摘要页 https://arxiv.org/abs/2610.07649 ；PDF https://arxiv.org/pdf/2610.07649 ；代码 https://github.com/namhyeongwoo/OntoPlan

### 一句话总结
论文提出本体驱动的场景表示与智能体框架 OntoPlan，用共享符号词汇表达对象、空间、关系和状态，并选择性检索任务相关信息，以提升大环境下长程机器人任务规划的成功率并显著降低 token 开销。

### 研究问题
基于大语言模型（LLM）的机器人任务规划在开放式指令跟随上具有潜力，但在大环境中的长程任务上表现退化。具体问题包括：以文本向 LLM 传递空间信息时，模型可能无法捕捉空间上下文，且 token 成本随环境规模增长；直接用 LLM 生成动作序列也难以满足当前世界状态与动作前置条件。

### 核心思路/方法
论文从两方面回应上述问题：
1. **本体驱动的场景表示**：将对象、空间、关系与状态对齐到共享的符号词汇中，以支持空间推理与任务规划。
2. **OntoPlan 智能体框架**：解释指令、选择性检索与任务相关的信息、形式化目标与约束，并生成可执行计划。

### 主要贡献
- 提出本体驱动的场景表示，将对象、空间、关系和状态统一到共享符号词汇，用于空间推理和任务规划。
- 提出 OntoPlan 智能体框架，可解释指令、选择性检索任务相关信息、形式化目标与约束并产出可执行计划。
- 在覆盖五种室内环境、三种场景尺度的 150 个通用任务上，OntoPlan 平均任务成功率为 0.89，最强基线为 0.27；平均每任务总 token 为 18.1k，约为最高效基线的 1/5.6。
- 随着场景尺度增大，上述优势持续存在，而先前方法在成功率上下降更剧烈、token 成本仍远更高。
- OntoPlan 对模糊或不可行指令能通过追问或报告信息不足来恰当响应，而非强行给出无效计划。

### 局限性
- 摘要未提供足够信息说明实验的具体任务类型、环境构建方式、基线方法与评价细节。
- 摘要未提供足够信息说明本体构建成本、泛化边界、真实机器人部署情况或失败案例分析。
- 摘要未提供足够信息说明推理延迟、计算资源需求及不同 LLM 后端的影响。

### 阅读优先级
高。理由：该工作同时针对 LLM 机器人任务规划中的空间上下文丢失、世界状态与动作前置条件满足、以及环境规模扩大带来的 token 成本问题，给出了本体驱动场景表示与智能体框架；摘要报告了在 150 个任务、五种室内环境和三种场景尺度上的显著成功率与 token 效率优势，且涉及模糊/不可行指令处理，属于可扩展机器人任务规划方向的重要进展。

</details>

<details>
<summary>Abstract</summary>

Large language model (LLM)-based robot task planning is promising for open-ended instruction following, but degrades on long-horizon tasks in large environments. When spatial information is conveyed to the LLM through text, the model can fail to capture spatial context, and token cost grows with environment size. Generating action sequences directly with an LLM also makes it difficult to satisfy the current world state and action preconditions. We address this with an ontology-grounded scene representation that aligns objects, spaces, relations, and states in a shared symbolic vocabulary for spatial reasoning and task planning, and with OntoPlan, an agentic framework that interprets instructions, selectively retrieves task-relevant information, formalizes goals and constraints, and produces executable plans. Across 150 general tasks spanning five indoor environments and three scene scales, OntoPlan achieves 0.89 average task success, compared with 0.27 for the strongest baseline, while using 18.1k total tokens per task on average, about 5.6$\times$ fewer than the most efficient baseline. These advantages persist as scene scale increases, whereas prior methods degrade more sharply in success and remain far more costly in tokens. OntoPlan also responds appropriately to ambiguous or infeasible instructions by asking follow-up questions or reporting insufficient information rather than committing to invalid plans. Code available at https://github.com/namhyeongwoo/OntoPlan.

</details>

#### 2026-10-06 - OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception

**Authors:** Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam
**Links:** [abs](https://arxiv.org/abs/2610.07569) - [pdf](https://arxiv.org/pdf/2610.07569)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D mapping, Gaussian Splatting, 3D Gaussian Splatting, splatting, robotics, robot perception, mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception
- 作者：Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam
- 出版日期：2026-10-06T00:58:30Z
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（次）
- 链接：[摘要](https://arxiv.org/abs/2610.07569) | [PDF](https://arxiv.org/pdf/2610.07569) | [项目页](https://csiro-robotics.github.io/OpenSplatGraph)

### 一句话总结
OpenSplatGraph 提出一个统一框架，从基于高斯泼溅的在线开放词汇语义地图中直接构建持久的 3D 场景图，以同时支持语言引导的目标定位与结构化关系推理。

### 研究问题
论文针对机器人感知中的一个割裂问题：基于 3D Gaussian Splatting 的稠密语义建图虽能提供高保真几何与高效的开放词汇感知，但其语义通常表示为非结构化特征场，限制了以对象为中心的推理；而 3D 场景图虽能显式建模对象及其关系以支持结构化推理，但通常基于稀疏几何表示构建，未能充分利用稠密语义地图的信息。因此，核心问题是如何将稠密开放词汇语义建图与结构化对象中心表示紧密结合。

### 核心思路/方法
- 提出统一框架 OpenSplatGraph，从在线高斯式开放词汇语义地图中直接构建持久的 3D 场景图。
- 在稠密语义地图上引入“可靠性感知语义场”（reliability-aware semantic field），维护轻量级观测统计，用于置信度感知、查询条件化的对象提取。
- 将提取的对象实例关联到持久图节点，使对象属性与关系能够跨观测与查询增量更新。
- 通过紧密耦合稠密语义建图与持久对象中心表示，在保持高斯建图几何保真度的同时，支持语言引导的目标定位和结构化关系推理。

### 主要贡献
- 提出从稠密高斯开放词汇语义地图直接构建持久 3D 场景图的统一框架。
- 设计可靠性感知语义场与置信度感知、查询条件化的对象提取机制。
- 实现对象属性与关系随观测和查询进行增量更新的持久图节点关联。
- 据摘要所述，在标准 3D 场景理解基准和真实机器人实验中，该方法在在线开放词汇感知与下游机器人任务上取得了有竞争力的表现。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集规模、对比基线、评价指标及定量结果。
- 摘要未提供足够信息说明方法的计算开销、实时性、可扩展性或失败情形。
- 摘要未提供足够信息说明可靠性感知语义场的具体实现细节与超参数。
- 摘要未提供足够信息说明在真实机器人实验中的任务类型与具体表现。

### 阅读优先级
高。理由：该工作位于神经场景表示与机器人/具身智能的交叉点，直指稠密开放词汇建图与结构化场景图之间的关键衔接问题；若关注开放词汇机器人感知、3D 场景图或高斯泼溅建图，该文的问题设定与“可靠性感知 + 持久图节点”思路具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Dense 3D mapping with semantic understanding is essential for robotic perception in complex environments. Recent 3D Gaussian Splatting-based mapping approaches enable high-fidelity geometry and efficient open-vocabulary perception, but typically represent semantics as unstructured feature fields that limit object-centric reasoning. In contrast, 3D scene graphs explicitly model objects and their relationships for structured reasoning, but are commonly constructed from sparse geometric representations that do not fully exploit dense semantic maps. In this work, we present OpenSplatGraph, a unified framework that constructs persistent 3D scene graphs directly from an online Gaussian-based open-vocabulary semantic map. The proposed framework augments the dense semantic map with a reliability-aware semantic field that maintains lightweight observation statistics for confidence-aware, query-conditioned object extraction. Extracted object instances are associated with persistent graph nodes, allowing object attributes and relationships to be incrementally updated across observations and queries. By tightly coupling dense semantic mapping with persistent object-centric representations, our framework supports both language-guided object grounding and structured relational reasoning while preserving the geometric fidelity of Gaussian-based mapping. Comprehensive evaluations on standard 3D scene understanding benchmarks and real-world robotic experiments demonstrate that OpenSplatGraph achieves competitive performance for online open-vocabulary perception and downstream robotic tasks. Project page: https://csiro-robotics.github.io/OpenSplatGraph.

</details>

#### 2026-10-06 - AIMS: Anchor-Integrated Multi-View Synthesis for Scalable Novel View Rendering

**Authors:** JooHyun Park, HanYoung Jang, HyeongYeop Kang
**Links:** [abs](https://arxiv.org/abs/2610.07566) - [pdf](https://arxiv.org/pdf/2610.07566)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AIMS: Anchor-Integrated Multi-View Synthesis for Scalable Novel View Rendering
- 作者：JooHyun Park, HanYoung Jang, HyeongYeop Kang
- 出版日期：2026-10-06T00:54:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.07566) / [PDF](https://arxiv.org/pdf/2610.07566)

### 一句话总结
AIMS 通过“锚点视图 + 邻近观测融合”的解耦式设计，在保持下游全局合成视图预算固定的前提下利用更多输入观测，从而提升前馈新视角合成的可扩展性。

### 研究问题
前馈式新视角合成方法能从带位姿的多视角输入中获得较强泛化能力，但扩展到大规模输入视图集合时存在困难：
- 基于 Transformer 的方法联合处理所有输入视图 token，随视图数量增长，计算和内存开销迅速增加；
- 简单的视图子采样虽然降低开销，但会丢弃可能有用的观测信息。

因此，核心问题是如何在视图数量增长时，既控制全局合成模型的处理成本，又不浪费额外观测信息。

### 核心思路/方法
AIMS 提出一种可扩展框架，将“可用观测数量”与“全局合成模型处理的视图数量”解耦。具体包括：
- 使用最远点采样（farthest point sampling）选择一组固定数量、空间上分散的锚点视图；
- 将每个锚点附近的观测分组；
- 使用轻量级可学习整合器（learnable integrator）将各组观测信息融合为增强后的锚点表示；
- 这样额外观测可以参与合成，但下游全局视图预算保持固定。

### 主要贡献
- 提出 AIMS 框架，将输入观测规模与全局合成模型处理的视图数量解耦，以提升前馈新视角合成的可扩展性。
- 采用最远点采样选择空间分布的锚点视图，并用轻量级可学习整合器融合邻近观测，使额外观测信息可被利用而不增加全局视图预算。
- 在 RealEstate10K 和 ScanNet 上进行评估，展示了相对于 Transformer 类和高斯类基线在质量—效率权衡上的优势。
- 报告结果：两个数据集上 PSNR 分别为 29.41 dB 和 17.73 dB，渲染平均每视图 7.24 ms。

### 局限性
- 摘要未提供足够信息说明方法在不同规模输入视图集合下的具体扩展边界。
- 摘要未提供足够信息说明锚点数量、分组策略或整合器设计对性能的敏感性分析。
- 摘要未提供足够信息说明在更复杂场景、动态场景或极端视角变化下的表现。
- 摘要未提供足够信息说明与基线相比在内存占用、训练成本或推理总吞吐方面的完整细节。
- 摘要未提供足够信息说明失败案例或该方法不适用的情况。

### 阅读优先级
高。该论文关注前馈新视角合成中的可扩展性问题，提出的“锚点 + 邻近观测融合”思路明确针对 Transformer 类方法随视图数增长的计算/内存瓶颈，且摘要给出了具体数据集、PSNR 和渲染时间指标，对关注新视角合成、神经场景表示与渲染效率的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward novel view synthesis methods achieve strong generalization from posed multi-view inputs, but scaling them to large input view sets remains challenging. Transformer-based approaches that jointly process all input-view tokens incur rapidly increasing computation and memory as the number of views grows, while simple view subsampling discards potentially useful observations. We introduce Anchor-Integrated Multi-View Synthesis (AIMS), a scalable framework that decouples the number of available observations from the number of views processed by the global synthesis model. AIMS selects a fixed set of spatially distributed anchor views using farthest point sampling, groups nearby observations around each anchor, and uses a lightweight learnable integrator to fuse their information into enriched anchor representations. This allows additional observations to contribute to synthesis while keeping the downstream global view budget fixed. Evaluations on RealEstate10K and ScanNet demonstrate a favorable quality--efficiency trade-off against transformer-based and Gaussian-based baselines. AIMS achieves 29.41 dB and 17.73 dB PSNR on the two datasets, respectively, with rendering averaging 7.24 ms per view.

</details>

#### 2026-10-05 - Learnable Spectral Activations

**Authors:** Tamir Shor, Or Litany, Alex Bronstein
**Links:** [abs](https://arxiv.org/abs/2610.07419) - [pdf](https://arxiv.org/pdf/2610.07419)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural radiance field, radiance field, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learnable Spectral Activations
- 作者：Tamir Shor, Or Litany, Alex Bronstein
- 出版日期：2026-10-05T21:29:04Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.07419 ；PDF: https://arxiv.org/pdf/2610.07419

### 一句话总结
论文提出可学习谱激活（LSA），用残差截断傅里叶级数替代固定神经元级非线性，在不扩大渐近函数类的前提下改变表示分解方式，以改善隐式神经表示的重建质量。

### 研究问题
隐式神经表示（INRs）的表示能力受输入编码和激活函数所诱导的谱结构影响。现有方法主要通过坐标编码或周期性非线性来改变网络可用的频率，但摘要指出“频率可及性并非唯一瓶颈”：对于具有局部结构或空间变化结构的信号，网络还需要有效地将频率组合成多谐波内部响应。因此，问题在于如何让网络更有效地进行频率组合与谱塑形，而不仅仅是提供更多频率。

### 核心思路/方法
- 提出可学习谱激活（LSA），将固定的神经元级非线性替换为残差截断傅里叶级数。
- 该傅里叶级数的谐波振幅在训练过程中学习得到。
- LSA 不扩大渐近函数类，而是改变表示的分解方式：线性权重负责选择特征，激活系数负责控制谱塑形，二者由不同的梯度分别更新。
- 在固定预激活的前提下，激活输出对系数是仿射的，因此谱调优成为一个更直接的子问题，而不是与特征选择纠缠在一起。
- 摘要提到经验上这种分解使更多目标信号能量集中在神经正切核（NTK）的前导特征模中，与优化行为改善一致。
- 在音频、图像、神经辐射场和神经声学场任务上，LSA 提升了重建质量。

### 主要贡献
- 提出 LSA，用可学习的残差截断傅里叶级数作为神经元级激活，学习谐波振幅以进行谱塑形。
- 强调该方法的机制不是扩展渐近函数类，而是改变表示分解，使谱调优与特征选择通过分离的梯度解耦。
- 给出经验观察：该分解使目标信号能量更集中于 NTK 前导特征模，与优化行为改善一致。
- 在音频、图像、神经辐射场和神经声学场任务上报告了重建质量提升。

### 局限性
摘要未提供足够信息。摘要未说明计算开销、参数增加、训练稳定性、与具体基线方法的详细比较、消融实验、失败场景或适用范围限制。

### 阅读优先级
中。理由：论文主题属于隐式神经表示与神经场景表示中的激活/谱结构设计，问题定位明确，方法思路具有结构性意义，并覆盖音频、图像、NeRF 和神经声学场多类任务；但摘要未提供充分的实验细节、定量结果和局限分析，是否值得优先精读取决于读者对 INR 激活函数设计或谱分解优化的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Implicit neural representations (INRs) are shaped by the spectral structure induced by their input encodings and activation functions. Existing methods improve fitting primarily by modifying which frequencies are available to the network, through coordinate encodings or periodic nonlinearities. However, frequency access is not the only bottleneck: signals with localized or spatially varying structure require the network to efficiently compose frequencies into multi-harmonic internal responses. We introduce learnable spectral activations (LSA), which replace fixed neuron-level nonlinearities with a residual truncated Fourier series whose harmonic amplitudes are learned during training. LSA does not expand the asymptotic function class. Instead, it changes the factorization of the representation: linear weights select features while activation coefficients control spectral shaping, and the two are updated by separate gradients. Because the activation output is affine in the coefficients given fixed pre-activations, spectral tuning becomes a more direct subproblem compared to architectures where it is entangled with feature selection. Empirically, this factorization concentrates more target-signal energy in the leading eigenmodes of the neural tangent kernel, consistent with improved optimization behavior. Across audio, image, neural radiance field, and neural acoustic field tasks, LSA also improves reconstruction quality.

</details>

#### 2026-10-05 - Real-time Rendering of Pre-integrated Neural Emitters

**Authors:** Arno Coomans, Floor Verhoeven, Edoardo A. Dominici, Markus Steinberger
**Links:** [abs](https://arxiv.org/abs/2610.06762) - [pdf](https://arxiv.org/pdf/2610.06762)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-time Rendering of Pre-integrated Neural Emitters
- 作者：Arno Coomans, Floor Verhoeven, Edoardo A. Dominici, Markus Steinberger
- 出版日期：2026-10-05T17:35:36Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.06762) / [PDF](https://arxiv.org/pdf/2610.06762)

### 一句话总结
论文提出 Neural Emission Fields（NEF），通过在发光体周围空间预计算光照，消除运行时积分，从而实时渲染复杂发光体的无噪声无遮挡直接光照。

### 研究问题
论文关注实时渲染中复杂发光体的直接光照瓶颈，具体包括具有遮挡外壳、高多边形发光网格、空间变化发光或可变形组件的发光体。现有实时方案要么依赖简化解析表示，要么回退到运行时采样：解析方法受限于简单发光体几何，纯采样估计器需要高采样预算才能无噪声，代理表示仍需在运行时对发光体周围出射辐射度进行积分。

### 核心思路/方法
论文提出 Neural Emission Fields（NEF），该表示通过在发光体周围体积中预计算光照来消除运行时积分。该神经场由位置、法线、视线方向和材质参数参数化。采用双头漫反射/光泽架构，每个着色点只需一次网络评估即可得到无噪声、无遮挡的直接光照。由于训练在发光体局部坐标系中进行，训练后的 NEF 可作为可移植光照资产，在刚性变换下跨场景复用。内部互反射、自遮挡、空间变化发光和形变均被吸收到学习到的表示中，且不增加运行时成本。

### 主要贡献
- 提出 Neural Emission Fields（NEF），一种在发光体周围空间预计算光照的表示，消除运行时积分。
- NEF 由位置、法线、视线方向和材质参数参数化，并采用双头漫反射/光泽架构。
- 每个着色点仅需一次网络评估即可获得无噪声、无遮挡的直接光照。
- 由于在发光体局部坐标系中训练，NEF 可作为可移植光照资产，在刚性变换下跨场景复用。
- 内部互反射、自遮挡、空间变化发光和形变被吸收进学习表示，且不增加运行时成本。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对实时渲染中复杂发光体直接光照的明确瓶颈，提出预计算神经场以消除运行时积分，并强调可移植光照资产与零额外运行时成本，问题定位和方法思路较清晰；但摘要未提供实验细节、性能数据、对比结果或局限性信息，因此难以仅凭摘要判断其实际效果与适用范围。

</details>

<details>
<summary>Abstract</summary>

Direct illumination from non-trivial emitters with occluding housing, high-polygon emissive meshes, spatially varying emission, or deformable assemblies is a persistent bottleneck in real-time rendering. Current real-time solutions either rely on simplified analytical representations or fall back to runtime sampling. Analytical methods are restricted to simple emitter geometry, pure sampling-based estimators need high sampling budgets to be noise-free, and proxy representations still require runtime integration over outgoing radiance around the emitter. We present Neural Emission Fields (NEF), a representation that eliminates runtime integration by precomputing the illumination in the volume around the emitter. This neural field is parameterized by position, normal, view direction, and material parameters. Using a two-headed diffuse/glossy architecture, it yields noise-free unoccluded direct illumination from a single network evaluation per shading point. Because training is performed in the emitter's local frame, a trained NEF acts as a portable lighting asset reusable across scenes under rigid transforms. Internal interreflections, self-occlusion, spatially varying emission, and deformations are absorbed into the learned representation at zero additional runtime cost.

</details>

#### 2026-10-05 - GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting

**Authors:** Boaz Keren-Gil, James Gain, Patrick Marais
**Links:** [abs](https://arxiv.org/abs/2610.06688) - [pdf](https://arxiv.org/pdf/2610.06688)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting
- 作者：Boaz Keren-Gil, James Gain, Patrick Marais
- 出版日期：2026-10-05T16:52:37Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.06688 ；PDF：https://arxiv.org/pdf/2610.06688

### 一句话总结
GS-Pool 面向同一空间两次独立 3DGS 重建之间的对象级变化检测，通过将 SAM2 掩码提升到高斯、引入跨访问摄影载体并结合几何、颜色与蒸馏 DINOv3 特征，输出发生变化的对象及其掩码。

### 研究问题
工厂、博物馆和测量场景会在相隔数月后拍摄同一空间，需要判断哪些对象发生了变化。当每次访问都用 3D Gaussian Splatting（3DGS）重建后，直接比较两个重建结果无法回答该问题：训练具有随机性，因此未变化空间的两次重建不会重合；并且第二次访问通常只是快速重扫描，照片数量远少于第一次。论文要解决的是在这种独立重建、且第二次扫描照片更少的情况下，如何进行对象级变化检测。

### 核心思路/方法
- 输入为同一空间两次独立重建得到的高斯场，目标是返回每次访问中发生变化的对象及其掩码。
- 将每次访问照片的 SAM2 掩码提升到渲染这些照片的高斯上，并合并为一个对象池，使每个决策在 3D 中按对象只做一次。
- 引入“摄影载体”：将每个输入重建的 3DGS 训练损失作用于另一访问的照片，并反向传播到渲染每个像素的高斯上。
- 将该载体与 GS-Diff 的几何项和颜色项，以及蒸馏的 DINOv3 特征相结合。
- 将这些证据与两次访问中都存在的对象证据进行比较，从而为每个场景设定变化阈值。
- 每个变化对象以一组高斯的形式返回，并附带其决策依据，供检查者在 3D 中复核。

### 主要贡献
- 提出 GS-Pool，用于两个独立重建的 3D 高斯场之间进行对象级变化检测并输出变化对象掩码。
- 设计基于 SAM2 掩码提升与对象池的 3D 对象级决策机制。
- 提出跨访问照片训练损失反向传播得到的“摄影载体”，并与 GS-Diff 几何/颜色项及蒸馏 DINOv3 特征融合。
- 通过比较两次访问共有对象的证据，为每个场景设定变化阈值。
- 在 PASLCD 上达到 mIoU/F1 为 0.751/0.846，相较最强先前方法 GS-Diff 的 0.644/0.758 提升 17%/12%；mIoU 相比 O-SCD、PlenoCI、MV-3DCD 分别高 36%、40%、57%；在 CL-Splats 上达到 0.855 mIoU，比 MV-3DCD 高 33%。

### 局限性
摘要未提供足够信息。摘要未说明方法在训练随机性、第二次扫描照片数量极少、对象池构建错误或阈值设定失败等情况下的失败模式，也未提供计算成本、实时性、跨场景泛化、标注依赖或消融实验细节。

### 阅读优先级
高。该论文直接针对 3DGS 重建之间对象级变化检测这一具体任务，提出明确的跨访问证据融合方案，并在摘要中给出与 GS-Diff 等方法的定量对比；若关注 3D 场景变化检测、3DGS 下游理解或对象级 3D 比较，该文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Factories, museums and surveyors photograph the same space months apart and need to know which objects changed. When each visit is reconstructed with 3D Gaussian Splatting (3DGS), a direct comparison of the two reconstructions does not answer this. Training is stochastic, so two reconstructions of an unchanged space never coincide, and the second visit is often a quick re-scan with far fewer photographs. We propose GS-Pool, which takes two independently reconstructed Gaussian fields of the same space and returns the changed objects in each, together with their masks. SAM2 masks of each visit's photographs are lifted onto the Gaussians that render them and merged into an object pool, so every decision is taken once per object in 3D. We introduce a photographic carrier, the 3DGS training loss of each input reconstruction against the other visit's photographs, backpropagated to the Gaussians that rendered each pixel. We combine it with GS-Diff's geometry and colour terms and our distilled DINOv3 features. This evidence is compared with that of the objects present in both visits, which sets a change threshold for each scene. On PASLCD, GS-Pool reaches mIoU/F1 scores of 0.751/0.846 against 0.644/0.758 for GS-Diff, the strongest prior method, a gain of 17%/12%. Its mIoU is also 36%, 40% and 57% above that of O-SCD, PlenoCI and MV-3DCD, and it reaches 0.855 mIoU on CL-Splats, 33% above MV-3DCD. Each changed object is returned as a set of Gaussians with the evidence behind its decision, which an inspector can review in 3D.

</details>

#### 2026-10-05 - MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks

**Authors:** Eunji Kim, Gahyeon Kim, Gianella Cravioto, Dong-hun Lee, Chaewon Moon, Chae-yeong Song, Sang-hyo Park
**Links:** [abs](https://arxiv.org/abs/2610.06472) - [pdf](https://arxiv.org/pdf/2610.06472)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks
- 作者：Eunji Kim, Gahyeon Kim, Gianella Cravioto, Dong-hun Lee, Chaewon Moon, Chae-yeong Song, Sang-hyo Park
- 出版日期：2026-10-05T15:02:47Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.06472；PDF: https://arxiv.org/pdf/2610.06472

### 一句话总结
MaRO-GS 是一个面向目标物体的 3D 高斯泼溅框架，可直接从带物体掩码的多视角图像优化目标物体高斯，并在多视角掩码不一致时保持鲁棒。

### 研究问题
论文关注 Gaussian Splatting 中的准确 3D 物体重建问题。现有物体级 3DGS 方法在只需要目标物体时仍重建整个场景，而不是直接优化目标物体，带来较大计算开销；同时，它们依赖 2D 分割掩码将高斯与物体关联，但掩码在多视角之间往往不一致。这种不一致会破坏高斯优化，产生错误监督的高斯，从而降低物体重建保真度。

### 核心思路/方法
论文提出 MaRO-GS，一个 3DGS 框架，直接从带物体掩码的多视角图像中优化目标物体高斯，并对不一致监督保持鲁棒。为提供可靠监督，方法使用 mask-reliability view filtering 排除不可靠视角；通过 object-supported Gaussian density control 抑制与目标物体无关的高斯并防止背景密集化；同时使用 Silhouette-aligned Object Loss 维持面向物体的优化。

### 主要贡献
- 提出 MaRO-GS，直接优化目标物体高斯，而非重建整个场景。
- 针对多视角掩码不一致问题，引入 mask-reliability view filtering 以排除不可靠视角。
- 引入 object-supported Gaussian density control，抑制目标物体无关高斯并防止背景密集化。
- 引入 Silhouette-aligned Object Loss，维持物体聚焦优化。
- 摘要称在多种数据集上的实验表明，该方法提升了 PSNR、分割准确率和计算效率，并在小物体 LERF-Mask 数据集上取得最大 2.05 dB 的 PSNR 增益。

### 局限性
摘要未提供足够信息。未提供关于失败案例、方法适用范围、对掩码质量下限的要求、计算资源需求、具体数据集组成或消融实验细节等信息。

### 阅读优先级
高。该论文聚焦 3DGS 物体级重建中的关键问题：多视角掩码不一致与计算开销，并给出针对性方法设计；若关注 3D 高斯泼溅、物体级重建或鲁棒分割监督，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

We address the challenge of accurate 3D object reconstruction from multi-view images in Gaussian Splatting. Existing object-level 3DGS methods reconstruct the entire scene rather than directly optimizing the target object, even when only the target object is needed, which incurs substantial computational overhead. They also rely on 2D segmentation masks to associate Gaussians with objects, but these masks are often inconsistent across views. Such inconsistencies corrupt Gaussian optimization and produce incorrectly supervised Gaussians that degrade object reconstruction fidelity. To overcome these limitations, we propose MaRO-GS, a 3DGS framework that directly optimizes target-object Gaussians from object-masked multi-view images and remains robust to inconsistent supervision. For reliable supervision, mask-reliability view filtering excludes unreliable views. Object-supported Gaussian density control suppresses Gaussians irrelevant to the target object and prevents background densification, while Silhouette-aligned Object Loss maintains object-focused optimization. Extensive experiments across diverse datasets demonstrate that MaRO-GS improves PSNR, segmentation accuracy, and computational efficiency, with the largest PSNR gain of 2.05 dB on the small-object LERF-Mask dataset.

</details>

#### 2026-10-05 - Controllable and Photorealistic Pedestrian Risky Motion Generation for End-to-End Driving Safety Evaluation

**Authors:** Siyuan Liu, Miao Li, Haibao Yu, Haohong Lin, Qing Zhou, Bingbing Nie, Ding Zhao
**Links:** [abs](https://arxiv.org/abs/2610.06171) - [pdf](https://arxiv.org/pdf/2610.06171)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Controllable and Photorealistic Pedestrian Risky Motion Generation for End-to-End Driving Safety Evaluation
- 作者：Siyuan Liu, Miao Li, Haibao Yu, Haohong Lin, Qing Zhou, Bingbing Nie, Ding Zhao
- 出版日期：2026-10-05T11:43:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.06171

### 一句话总结
ControlPed 结合轨迹级冲突合成与 3D 高斯泼溅（3DGS），生成具有照片级真实感和运动可控性的行人类安全关键场景，用于端到端自动驾驶安全评估。

### 研究问题
在罕见且安全关键的车辆-行人交互场景下评估端到端自动驾驶，需要传感器级、照片级真实的场景。然而，基于轨迹的场景生成器无法合成原始视觉观测，而基于视频的方法又缺乏可控性。论文聚焦于如何同时兼顾视觉真实感与运动可控性，生成用于安全评估的高危行人运动场景。

### 核心思路/方法
论文提出 ControlPed 框架，将轨迹级冲突合成与 3D 高斯泼溅（3DGS）相结合。其构建于 HazardPed 数据集之上，该数据集包含来自 10,352 个交通视频的 422 条冲突轨迹、HD 地图以及 857 条标注的 3D 人体运动。方法流程为：首先生成冲突轨迹；随后通过文本条件化的运动扩散模型将这些轨迹提升为 3D 人体运动序列；最后使用可动画的 3DGS 化身渲染多视角传感器观测。

### 主要贡献
- 提出 ControlPed 框架，结合轨迹级冲突合成与 3DGS，生成照片级真实、运动可控的安全关键行人场景，以弥补轨迹生成器无法合成视觉观测、视频方法缺乏可控性的空白。
- 基于 HazardPed 数据集（10,352 个交通视频、422 条冲突轨迹、HD 地图、857 条标注 3D 人体运动）构建方法流程。
- 在 88 个渲染的照片级真实场景中进行安全评估，发现七个领先端到端驾驶模型性能严重下降，平均 HDScore 从 88.8 骤降至 47.4，暴露了在危险行人行为下的主要失效模式。
- 将发布数据集与测试基准，以促进车辆-行人交互的安全评估。

### 局限性
摘要未提供足够信息。摘要仅提及方法框架、数据来源、评估结果与发布计划，未说明方法本身的技术限制、计算成本、泛化边界、失败案例或评估覆盖范围的不足。

### 阅读优先级
高。理由：该工作直接针对端到端自动驾驶安全评估中的关键痛点（罕见安全场景的传感器级生成与可控性），并给出了七个领先模型性能显著下降的量化证据，对自动驾驶安全评测、场景生成与 3DGS 应用方向具有较高参考价值，且承诺发布数据集与基准。

</details>

<details>
<summary>Abstract</summary>

Evaluating end-to-end autonomous driving under rare, safety-critical vehicle-pedestrian interactions requires photorealistic, sensor-level scenarios. However, trajectory-based scenario generators cannot synthesize raw visual observations, whereas video-based approaches lack controllability. To bridge this gap, we present ControlPed, a novel framework that combines trajectory-level conflict synthesis with 3D Gaussian Splatting (3DGS) to generate photorealistic, motion-controllable safety-critical scenarios. Built upon HazardPed, a dataset derived from 10,352 traffic videos comprising 422 conflict trajectories, HD maps, and 857 annotated 3D human motions, ControlPed first generates conflict trajectories, lifts them into 3D human motion sequences via text-conditioned motion diffusion, and finally renders multi-view sensor observations using animatable 3DGS avatars. Safety evaluation in 88 rendered photorealistic scenarios reveals that seven leading end-to-end driving models suffer a severe performance drop, with their mean HDScore plunging from 88.8 to 47.4, exposing major failure modes under dangerous pedestrian behaviors. The dataset and testing benchmarks will be released to facilitate safety assessment of vehicle-pedestrian interactions.

</details>

#### 2026-10-05 - Casual Flash Lighting for Gaussian Splat Inverse Rendering

**Authors:** Jiamin Xu, Dongheng Wei, Jiarong Zhao, Qi Wang, James Tompkin, Weiwei Xu, Gang Xu
**Links:** [abs](https://arxiv.org/abs/2610.06035) - [pdf](https://arxiv.org/pdf/2610.06035)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Casual Flash Lighting for Gaussian Splat Inverse Rendering
- 作者：Jiamin Xu, Dongheng Wei, Jiarong Zhao, Qi Wang, James Tompkin, Weiwei Xu, Gang Xu
- 出版日期：2026-10-05T09:34:05Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.06035（PDF：https://arxiv.org/pdf/2610.06035）

### 一句话总结
本文提出一种结合日常室内拍摄中静态光照与闪光灯（开/关）图像的高斯泼溅逆渲染方法，通过 GS 锚定的漫反射场避免闪光残差在视角间被 alpha 混合漂移吸收，从而改进材质分解与重光照。

### 研究问题
- 从照片中恢复几何、材质和光照在仅有静态光照时高度病态（ambiguous）。
- 主动光照方案可降低歧义，但需要暗室或专用硬件。
- 如何利用日常室内拍摄中同时存在的静态光照与闪光光照（开或关、各自独立视角）来缓解逆渲染的歧义，是本文关注的问题。

### 核心思路/方法
- 协同利用 casual indoor capture 中的静态光照与闪光光照（flash on/off），两者来自独立视角。
- 闪光残差用于约束反照率（albedo）和 BRDF；静态光照则捕捉闪光遗漏的掠射角高光（grazing-angle specular highlights）。
- 以 2DGS 重建为框架。
- 关键贡献是 GS-anchored diffuse field：在光栅化的 2DGS 深度处查询一个哈希编码 MLP。
- 由于该场仅依赖世界位置，它在 3D 中具有视角一致性（view consistent），可使闪光残差驱动材质分解，而不被跨视角的 alpha-blending drift 吸收。
- 同时以延迟着色（deferred shading）渲染静态光照，使其也能监督材质分解。

### 主要贡献
- 提出结合静态与闪光光照的日常室内捕获逆渲染方案，避免主动光照对暗室或专用硬件的需求。
- 提出 GS-anchored diffuse field：哈希编码 MLP 在 2DGS 深度处查询，仅依赖世界位置，保证 3D 视角一致性，防止闪光残差被 alpha 混合漂移吸收。
- 使用延迟着色渲染静态光照，使其参与材质分解监督。
- 在五个合成场景和三个真实室内场景上，该方法在漫反射颜色、反照率与粗糙度材质参数上优于六个近期基线；在重光照任务中，PSNR 相比次优基线提升 4.17 dB。

### 局限性
- 摘要未提供足够信息说明方法的失败场景、硬件依赖、计算成本或对拍摄条件的限制。
- 摘要未提供足够信息说明合成与真实场景的具体规模、评价协议细节及基线选择依据。
- 摘要未提供足够信息说明 GS-anchored diffuse field 在极端视角或复杂材质下的表现边界。

### 阅读优先级
高。理由：该工作针对逆渲染中光照歧义这一核心问题，提出结合日常闪光与静态光照的实用采集方案，并在材质分解与重光照指标上给出明确的量化提升（PSNR +4.17 dB），对神经渲染、逆渲染与材质估计方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering geometry, materials, and lighting from photographs is highly ambiguous when only static illumination is available. Active-lighting setups reduce the ambiguity but require dark rooms or specialized hardware. Instead, we synergize both static and flash lighting from casual indoor capture, with the flash on or off, each from independent viewpoints. The flash residual constrains albedo and the BRDF, while static lighting captures grazing-angle specular highlights that flash misses. With a 2DGS reconstruction framing, our key contribution is a GS-anchored diffuse field: a hash-encoded MLP is queried at the rasterized 2DGS depth. As it depends only on world position, it is view consistent in 3D and allows the flash residual to drive material decomposition instead of being absorbed by alpha-blending drift across views. At the same time, we render static lighting with deferred shading such that it can also supervise material decomposition. On five synthetic and three real indoor scenes, our method outperforms six recent baselines on diffuse color, albedo and roughness material parameters, and in relighting where PSNR improves by 4.17 dB over the next-best baseline.

</details>

#### 2026-10-04 - SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering

**Authors:** Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger
**Links:** [abs](https://arxiv.org/abs/2610.05576) - [pdf](https://arxiv.org/pdf/2610.05576)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering
- 作者：Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger
- 出版日期：2026-10-04T22:25:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.05576 ；https://arxiv.org/pdf/2610.05576

### 一句话总结
针对基于 3D Gaussian Splatting 的随机顺序无关透明渲染中输出噪声明显的问题，从表示与图像合成两个层面降低高频噪声，以提升随机渲染的收敛速度与图像质量。

### 研究问题
随机顺序无关透明渲染可高效、优雅地渲染如 3D Gaussian Splatting 之类的基元辐射场，但由于输出中存在固有的可见噪声，实际应用仍不理想。论文旨在最小化高频噪声，并从表示与图像合成层面处理噪声来源。

### 核心思路/方法
论文提出一种系统性方法来最小化高频噪声，分别从表示层面和图像合成层面处理噪声来源。在随机渲染过程中，采用基于历史的空间重采样方案大幅加速图像收敛，并使用时间重要性重采样保证相机运动下的连贯性。在训练过程中，使用颜色正则化器隐式降低 3DGS 模型沿视光线的方差。基于这些特性，其优化的 Vulkan 渲染器在低采样数和高采样数下都能有效缓解输出噪声。

### 主要贡献
- 提出从表示和图像合成层面最小化高频噪声的系统性方法。
- 在随机渲染中引入基于历史的空间重采样方案，显著加速图像收敛。
- 引入时间重要性重采样，以在相机运动下保持连贯性。
- 在训练中使用颜色正则化器，隐式降低 3DGS 模型沿视光线的方差。
- 实现基于 Vulkan 的优化渲染器，在每像素 1 采样时相较此前随机方法取得约 13 dB 的 PSNR 提升，并快速收敛到排序 3DGS，平均 L1 误差小于 $10^{-4}$。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直接针对 3D Gaussian Splatting 随机渲染中的关键实际瓶颈——输出噪声与收敛速度，并报告了显著的 PSNR 提升和低 L1 误差；若关注 3DGS 渲染、顺序无关透明或随机渲染质量优化，该论文具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Stochastic order-independent transparency enables efficient and elegant rendering of primitive-based radiance fields like 3D Gaussian Splatting models, but remains impractical due to the inherent visible noise in the output. We propose a principled approach to minimize high-frequency noise, addressing its sources at the representation and image synthesis level. During stochastic rendering, our history-based spatial resampling scheme drastically accelerates image convergence, while temporal importance resampling ensures coherence under camera movement. During training, a color regularizer implicitly reduces the variance along view rays in the 3DGS models. With these properties, our optimized, Vulkan-based renderer effectively mitigates output noise at low and high sample counts, achieving a substantial 13~dB PSNR increase in quality over previous stochastic methods at 1 sample per pixel and quickly converging to sorted 3DGS with an average L1 error of less than $10^{-4}$.

</details>

#### 2026-10-04 - Universal Test-Time Training

**Authors:** Zefan Cai, Qinzhe Hu, Ziqiao Ma, Hao Tan, Junjie Hu
**Links:** [abs](https://arxiv.org/abs/2610.05484) - [pdf](https://arxiv.org/pdf/2610.05484)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Universal Test-Time Training
- 作者：Zefan Cai, Qinzhe Hu, Ziqiao Ma, Hao Tan, Junjie Hu
- 出版日期：2026-10-04T19:43:36Z
- 分类：Neural Scene Representations & Rendering（主分类）；次要分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.05484 ；PDF https://arxiv.org/pdf/2610.05484

### 一句话总结
论文提出 uTTT，将所有层原本各自私有的快速权重记忆改为所有层共享的单一记忆，使记忆在时间与深度两个维度上递归，并在语言建模与新视角合成任务上验证其效果。

### 研究问题
现有 Test-Time Training（TTT）架构把上下文压缩为在线更新的快速权重，并作为记忆被查询。但这些设计让记忆对每一层保持私有：记忆只在时间上递归，深度仅用于索引 L 个彼此独立的记忆。论文质疑“记忆归属是否必须绑定到深度”，并研究共享记忆能否带来更好的效果。

### 核心思路/方法
论文提出 Universal Test-Time Training（uTTT）：所有层读写同一份共享记忆，同时保留各层特有的骨干参数。这样共享记忆在时间与深度两个维度上递归，递归单位分别是 chunk 和 layer——某个 chunk 中深层写入的内容，可以被下一个 chunk 的浅层读取。

论文给出两种实例化：
- uTTT-MoE：每个 token head 被路由到由所有层共享的专家池中的少数专家。
- uTTT-Dense：在每个层都应用完整的共享记忆，不进行路由。

### 主要贡献
- 提出 uTTT，将 TTT 中的记忆所有权从“按深度私有”改为“所有层共享一份记忆”。
- 使记忆在时间与深度两个维度上递归，以 chunk 和 layer 为递归单位。
- 给出两种具体实现：uTTT-MoE 与 uTTT-Dense。
- 在语言建模中，uTTT-MoE 在 124M 和 760M 规模达到 15.5 与 27.9 RULER 准确率，在相同状态与活跃计算量下分别比层私有对应方法高 2.6 与 2.1 分，为所测试的有界状态模型中最高，且每 token 损失匹配或优于全注意力。
- 在新视角合成中，在固定每层计算量下共享记忆，路由模型在 view-23 物体 PSNR 上提升 0.92 dB，稠密模型提升 0.76 dB。

### 局限性
摘要未提供足够信息。摘要未说明计算开销、内存占用、训练稳定性、模型规模上限、任务范围之外的泛化性、实现细节或失败案例等局限。

### 阅读优先级
中。理由：该论文针对 TTT 记忆机制提出明确且可检验的结构性改动，并在语言建模与新视角合成两类任务上给出定量增益；但摘要仅覆盖核心方法与主要结果，若读者关注 TTT、快速权重记忆或跨层共享机制，值得进一步阅读全文以确认细节与适用边界。

</details>

<details>
<summary>Abstract</summary>

Recent Test-Time Training (TTT) architectures compress context into fast weights that are updated online and queried as memory. Existing TTT designs keep this memory private to each layer: it recurs only over time, and depth merely indexes L separate memories. We argue that memory ownership need not be tied to depth, and introduce Universal Test-Time Training (uTTT), in which all layers read and write one shared memory while retaining layer-specific backbone parameters. The shared memory thus recurs over two dimensions, time and depth, with chunks and layers as their units: a write by a deep layer in one chunk can be read by a shallow layer in the next. We instantiate this idea as uTTT-MoE and uTTT-Dense. uTTT-MoE routes each token head to a few experts in a pool shared by all layers; uTTT-Dense applies the whole shared memory at every layer without routing. In language modeling, uTTT-MoE reaches 15.5 and 27.9 RULER accuracy at 124M and 760M, 2.6 and 2.1 points above its layer-private counterpart at equal state and active compute, the highest among tested bounded-state models, with per-token loss matching or beating full attention. In novel view synthesis, sharing at fixed per-layer compute gains 0.92 dB in view-23 object PSNR in routed models and 0.76 dB in dense models.

</details>

#### 2026-10-03 - NAMVIS: Next-Scale Autoregressive Multi-View Image Synthesis

**Authors:** Ramil Khafizov, Ilya Statsenko, Ruslan Rakhimov, Artem Komarichev, Peter Wonka, Evgeny Burnaev
**Links:** [abs](https://arxiv.org/abs/2610.04722) - [pdf](https://arxiv.org/pdf/2610.04722)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NAMVIS: Next-Scale Autoregressive Multi-View Image Synthesis
- 作者：Ramil Khafizov, Ilya Statsenko, Ruslan Rakhimov, Artem Komarichev, Peter Wonka, Evgeny Burnaev
- 出版日期：2026-10-03T19:22:02Z
- 分类：Neural Scene Representations & Rendering（主分类）；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.04722 ；PDF https://arxiv.org/pdf/2610.04722 ；项目页 https://corl-team.github.io/namvis/

### 一句话总结
NAMVIS 将稀疏视角多视角图像合成从扩散式迭代去噪改写为“几何条件下的下一尺度自回归”，在 Objaverse、GSO、OmniObject3D 上以更高指标和 3 倍以上加速优于所评估的扩散基线。

### 研究问题
稀疏视角新视角合成是 3D 内容生成的核心问题。摘要指出，基于扩散的方法受限于迭代去噪，导致多视角生成在推理阶段代价高昂。

### 核心思路/方法
- 提出 NAMVIS，一个“无扩散”框架，将多视角图像合成重新表述为几何条件下的“下一尺度自回归”。
- 不通过重复去噪生成目标视角，而是用少量由粗到细的尺度步骤预测离散视觉 token；在每个尺度内以及各目标视角之间并行采样所有 token。
- 提出 Multi-scale Projective Pose Encoding，在每个分辨率上把源相机与目标相机的变换注入目标视角自注意力以及源到目标的交叉注意力，从而将生成过程锚定到显式相机几何。
- 结合全局条件与稠密的几何感知交叉注意力，使模型在保持源视角外观的同时维持目标视角一致性。

### 主要贡献
- 提出无扩散的几何条件下一尺度自回归多视角合成框架 NAMVIS。
- 提出 Multi-scale Projective Pose Encoding，用于在多个分辨率上注入源与目标相机变换。
- 通过全局条件与稠密几何感知交叉注意力的结合，兼顾源视角外观保持与目标视角一致性。
- 在 Objaverse、GSO、OmniObject3D 上，在 PSNR、SSIM、LPIPS 指标上优于所评估的扩散基线，并在相同评估设置下比所评估的扩散基线快 3 倍以上。

### 局限性
摘要未提供足够信息。摘要中仅给出正向结论与速度对比，未提及失败情形、适用边界（如视角数量、物体类型、场景尺度等）、计算资源需求或误差分析。

### 阅读优先级
高。理由：该论文针对稀疏视角多视角合成中扩散推理昂贵的明确痛点，给出非扩散的下一尺度自回归替代方案，并在多个数据集与三项指标上报告优于所评估扩散基线、且推理速度提升 3 倍以上；若关注 3D 内容生成与多视角合成的效率与质量权衡，属于值得优先阅读的工作。

</details>

<details>
<summary>Abstract</summary>

Sparse-view novel view synthesis is a central problem in 3D content creation, but diffusion-based approaches remain limited by iterative denoising, making multi-view generation expensive at inference time. We introduce NAMVIS, a diffusion-free framework that reformulates multi-view image synthesis as geometry-conditioned next-scale autoregression. Instead of generating target views through repeated denoising, NAMVIS predicts discrete visual tokens through a small number of coarse-to-fine scale steps, while sampling all tokens within each scale and across target views in parallel. To anchor this generation process to explicit camera geometry, we propose Multi-scale Projective Pose Encoding, which injects source and target camera transformations into both target-view self-attention and source-to-target cross-attention at every resolution. NAMVIS further combines global conditioning with dense geometry-aware cross-attention, enabling the model to preserve source-view appearance while maintaining target-view consistency. Across Objaverse, GSO, and OmniObject3D, NAMVIS outperforms diffusion-based baselines in PSNR, SSIM, and LPIPS, while running over 3 times faster than the evaluated diffusion baselines under the same evaluation setting. These results suggest that geometry-conditioned next-scale autoregression is a promising and efficient alternative to diffusion for sparse-view multi-view synthesis. Additional qualitative results, videos, and resources are available at https://corl-team.github.io/namvis/

</details>

#### 2026-10-01 - EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation

**Authors:** Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang
**Links:** [abs](https://arxiv.org/abs/2610.01876) - [pdf](https://arxiv.org/pdf/2610.01876)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation
- 作者：Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang
- 出版日期：2026-10-01T15:32:49Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.01876) / [PDF](https://arxiv.org/pdf/2610.01876)

### 一句话总结
EvenSplat 通过耦合图像空间的光照分解与高斯所携带的光照场，并引入相机响应网络与局部曝光补偿模块，以在曝光和光照变化下改进 3D Gaussian Splatting 的重建效果。

### 研究问题
论文关注的是在曝光变化和光照不均匀条件下的多视角重建问题。摘要指出，同一表面在均匀光照下从不同角度看起来几乎一致，但在不均匀光照下则不然；视角之间存在曝光变化、单张图像内部存在光照变化、局部强光源还会造成亮暗并存的区域。3D Gaussian Splatting 等方法会把这类光照伪影当作场景本身属性，从而把采集相关的光照与几何、颜色纠缠在一起。

### 核心思路/方法
EvenSplat 的核心是将采集相关的光照影响与场景本身的几何和颜色分离。具体而言，该方法耦合了图像空间的光照分解与由高斯携带的光照场，使二维视图和三维视图共享同一套对光照的解释；同时使用相机响应网络和局部曝光补偿模块来吸收训练图像之间残留的全局与局部差异。

### 主要贡献
- 提出 EvenSplat 框架，用于在曝光和光照变化下进行高斯泼溅重建。
- 将图像空间光照分解与高斯携带的光照场进行耦合，使 2D 与 3D 视图共享对光照的解释。
- 引入相机响应网络和局部曝光补偿模块，处理跨训练图像的全局与残余差异。
- 摘要称在多个数据集及多种不均匀光照形式（跨视角曝光、空间光照变化、高对比度光照）上，在真实采集和模拟基准中总体优于当前先进方法，尤其在高对比度光照下表现突出。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败场景、计算开销、对极端或未知光照条件的泛化能力、对特定数据假设的依赖，以及消融实验细节等。

### 阅读优先级
高。理由是论文针对 3D Gaussian Splatting 在曝光和光照变化下将光照伪影与场景属性纠缠的问题提出分离思路，且摘要声称在多种不均匀光照和多个基准上总体优于现有方法，尤其在高对比度光照下表现突出；该主题与神经场景表示与渲染方向直接相关。

</details>

<details>
<summary>Abstract</summary>

A surface photographed under even light presents nearly the same appearance from every angle; the same surface under uneven light does not. Exposure changes between views, illumination varies within a single image, and locally strong light sources leave one region bright and its neighbor in shadow. Multi-view reconstruction methods such as 3D Gaussian Splatting treat these lighting artifacts as if they were properties of the scene, entangling capture-specific illumination with the geometry and color they recover. We present EvenSplat, a framework that separates the two. EvenSplat couples an image-space illumination decomposition with an illumination field carried by the Gaussians, so that the same explanation of the lighting is shared between the two-dimensional and three-dimensional views of the scene; a camera-response network and a local exposure-compensation module absorb the global and residual differences that remain across training images. Through extensive experiments across multiple datasets and diverse forms of uneven illumination (cross-view exposure, spatial illumination variation, and high-contrast lighting) on both real-world captured and simulated benchmarks, EvenSplat generally outperforms state-of-the-art methods, particularly under high-contrast illumination.

</details>

#### 2026-10-01 - Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation

**Authors:** Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai
**Links:** [abs](https://arxiv.org/abs/2610.01114) - [pdf](https://arxiv.org/pdf/2610.01114)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation
- 作者：Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai
- 出版日期：2026-10-01T05:52:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.01114 ；PDF https://arxiv.org/pdf/2610.01114

### 一句话总结
本文提出一种仿射对齐图集（affine-aligned atlas）下的规范高斯表示，通过帧级仿射变换先吸收全局运动，再构建规范高斯，以缓解大相机运动视频中规范表示与各帧失配的问题。

### 研究问题
现有基于高斯的视频表示通常将视频分解为规范高斯（canonical Gaussians）与时间形变（temporal deformation）。但当视频包含较大全局运动（如相机移动）时，规范表示可能与单帧图像发生错位，从而加重时间形变模型的负担。论文关注的核心问题是：如何减少规范表示与目标帧之间的差距，尤其在全局运动较大的视频序列中提升重建质量。

### 核心思路/方法
论文提出“仿射图集规范高斯表示”：在一个更大的仿射对齐图集空间中构建规范高斯。具体而言，先对每一帧应用仿射变换以吸收全局运动，然后再进行规范高斯构建，从而缩小规范表示与目标帧之间的差距。作者强调，该方法只修改规范构建阶段，因此可以集成到已有的基于规范高斯的方法中，且额外参数开销可忽略。

### 主要贡献
- 提出一种仿射对齐图集空间中的规范高斯表示，用于视频表示中的规范高斯构建。
- 通过帧级仿射变换在构建规范高斯前吸收全局运动，缓解规范表示与单帧之间的错位问题。
- 方法仅修改规范构建阶段，可集成到现有基于规范高斯的方法中，且额外参数成本可忽略。
- 实验显示，该方法尤其在相机运动较大的序列上提升了重建质量。

### 局限性
摘要未提供足够信息。摘要中未说明具体实验数据集、评价指标、与哪些基线方法比较、仿射变换如何估计、是否处理非全局运动或复杂动态场景、计算开销的具体数值、失败案例或方法适用边界。上述内容均需参考原文进一步确认。

### 阅读优先级
中。理由：该工作针对基于高斯的视频表示中“大全局运动导致规范表示失配”这一明确问题，提出阶段局部修改且易于集成的方案，对关注高斯泼溅、视频表示与神经场景表示的研究者有参考价值；但摘要未提供实验设置、量化结果和实现细节，且论文分类为神经场景表示与渲染，是否具有广泛跨领域影响需进一步阅读原文判断。

</details>

<details>
<summary>Abstract</summary>

Gaussian splatting has recently emerged as an efficient representation for images and videos due to its explicit structure and fast rendering capability. Existing Gaussian-based video representations often decompose a video into canonical Gaussians and temporal deformation. However, when a video contains large global motion such as camera movement, the canonical representation may become misaligned with individual frames, increasing the burden on the temporal deformation model. In this paper, we propose an affine-atlas canonical Gaussian representation, which constructs canonical Gaussians in a larger affine-aligned atlas space. Frame-wise affine transforms absorb global motion before canonical Gaussian construction, reducing the gap between the canonical representation and target frames. Since the proposed method only modifies the canonical construction stage, it can be integrated into existing canonical-Gaussian-based methods with negligible additional parameter cost. Experiments show that our method improves reconstruction quality especially for sequences with large camera motion.

</details>

### 2026-09

#### 2026-09-30 - TRACE: Privacy-Preserving Next-Best-View Selection over Distributed 3D Gaussian-Splat Maps

**Authors:** Amirhossein Mollaei Khass, Athanasios Cosse, Qiyu Sun, Nader Motee
**Links:** [abs](https://arxiv.org/abs/2610.00822) - [pdf](https://arxiv.org/pdf/2610.00822)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRACE: Privacy-Preserving Next-Best-View Selection over Distributed 3D Gaussian-Splat Maps
- 作者：Amirhossein Mollaei Khass, Athanasios Cosse, Qiyu Sun, Nader Motee
- 出版日期：2026-09-30T23:32:16Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.00822 ，PDF：https://arxiv.org/pdf/2610.00822

### 一句话总结
在多个机器人各自维护私有 3D Gaussian Splatting 地图的场景下，TRACE 通过只交换与视图选择相关的两类射线聚合量，在不共享 splats 的前提下近似复现集中式的 next-best-view 选择。

### 研究问题
多个机器人各自构建并私有保存自己的 3D Gaussian Splatting 地图时，如何进行 next-best-view 选择。单个机器人候选视图的期望信息增益（EIG）由所有机器人地图共同决定，因为其他机器人的 splats 会遮挡它自己的 splats、也会在其后方发光，因此 EIG 需要针对合并后的地图评估。但没有任何一个机器人拥有这个合并地图，问题在于如何在不共享地图的情况下完成这一评估。

### 核心思路/方法
论文指出，地图之间的耦合只通过两个射线量传导：某个 splat 前方的透射率（transmittance）和其后的辐射亮度（radiance），而这两者都是沿射线命中点的求和。因此它们可以按机器人分解：每个机器人沿候选视图的射线，在自己的地图上按深度分箱（depth bins）对这两个量求和，并把和及其相对位姿的导数发送出去。规划视图的机器人据此恢复出自己的 EIG 及其在 SO(3) 上的梯度。用于 EIG 通信的这两个量称为 Transmittance and Radiance Aggregates，协议因此命名为 TRACE。机器人不共享 splats，且消息大小不随地图规模增长。

### 主要贡献
- 提出 TRACE 协议，使各机器人无需共享私有 3D Gaussian Splatting 地图，即可协同进行 next-best-view 选择。
- 证明 EIG 的跨地图耦合可通过透射率与辐射亮度两类射线聚合量分解，并由各机器人按深度分箱在本地计算后通信。
- 给出的通信内容仅为聚合量及其位姿导数，且消息大小不随地图规模增长。
- 证明在某一 splat 之后的深度分箱未混合两个机器人的命中点时，重建是精确的，并给出否则的误差上界。
- 在 Habitat-Sim 中进行了超过 100 次 next-best-view 决策，TRACE 在 83.3% 的情况下选出的朝向与集中式结果相差在 15 度以内，其视图达到集中式 EIG 的 97.9%。

### 局限性
- 精确重建有一个前提条件：某一 splat 之后的深度分箱不能混合来自两个机器人的命中点；摘要仅说明在此条件下精确、否则给出误差上界，未说明该条件在实际场景中出现的频率或影响程度。
- 摘要未提供足够信息说明实验中的机器人数量、地图规模、通信开销实测、不同场景类型或与更多基线方法的对比。
- 摘要未提供足够信息说明透射率与辐射亮度聚合量通信的隐私强度分析（例如是否可能反推出地图信息）。
- 摘要未提供足够信息说明深度分箱的具体划分方式及其对精度与通信量的影响。

### 阅读优先级
中。理由：该工作面向多机器人分布式 3D Gaussian Splatting 地图下的隐私保护 next-best-view 选择，问题设定明确、方法有理论分解与误差界，并给出量化实验指标；但摘要未提供足够信息以判断隐私保障强度、实际通信开销和多场景泛化性，适合对分布式神经渲染、隐私保护多机器人规划感兴趣的读者进一步阅读。

</details>

<details>
<summary>Abstract</summary>

Share the light, not the map. We study next-best-view selection for a team of robots, each of which builds its own 3D Gaussian Splatting map and keeps it private. A robot picks the view with the largest expected information gain (EIG) about the splats along its own path. This gain depends on the other maps. Their splats occlude its own and shine behind them, so the gain has to be evaluated against the pooled map. No robot has this map. We show that the coupling passes through only two ray quantities, the transmittance in front of a splat and the radiance behind it, and that both are sums over the hits of the ray. Hence, they decompose across the robots, and each robot sums them over depth bins in its own map, along the rays of a candidate view, and sends the sums with their pose derivatives. The robot planning the view turns them into its EIG and gradient on SO(3). Transmittance and Radiance Aggregates, communicated for the EIG, give the protocol its name: TRACE. No robot shares its splats, and the message size does not grow with a map. We prove that the reconstruction is exact unless a depth bin behind a splat mixes hits of two robots, and we bound the error otherwise. Over 100 next-best-view decisions in Habitat-Sim, TRACE picks a heading within 15 degrees of the centralized one in 83.3% of the cases, and its views reach 97.9% of the centralized EIG.

</details>

#### 2026-09-30 - What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting

**Authors:** Rezvan Joshaghani, Steven Cutchin
**Links:** [abs](https://arxiv.org/abs/2610.00749) - [pdf](https://arxiv.org/pdf/2610.00749)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting
- 作者：Rezvan Joshaghani, Steven Cutchin
- 出版日期：2026-09-30T21:41:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.00749

### 一句话总结
该研究通过分离亮度与色度通道监督来训练 3DGS 模型，发现标准 3DGS 的几何形成强烈由亮度主导但并非完全排他，且色度外观可在空间支持形成后重新拟合恢复。

### 研究问题
标准 3D Gaussian Splatting (3DGS) 从 RGB 监督中联合学习几何与外观，难以分离亮度和色度对学习表示的贡献。论文试图回答：亮度和色度分别如何影响 3DGS 的几何学习和重建质量？

### 核心思路/方法
- 在不同通道监督下训练模型（亮度单独、色度单独、RGB 等），并冻结非外观参数（位置、尺度、旋转、不透明度）。
- 使用相同的求解器重新估计外观，然后比较留出重建（held-out reconstruction）结果。
- 在 11 个基准场景上，每个场景进行 4 次独立运行。
- 比较高阶球谐函数对亮度和色度重建质量的贡献差异。
- 通过删除色度后重新拟合，测试在冻结几何上恢复色度外观的能力。
- 对比仅色度监督与仅亮度监督产生的几何质量差距，并分析密化（densification）对差距的解释程度。

### 主要贡献
- 量化了仅亮度监督学习的几何与 RGB 训练几何在留出重建上的平均差距仅为 0.085 dB。
- 发现从训练模型删除色度后，足够表达力的求解器可在冻结几何上重新拟合色度至原始质量或略好。
- 揭示高阶球谐函数对亮度的重建质量贡献远大于对色度的贡献（平均 PSNR 提升 1.44 dB vs 0.19 dB），尽管在镜面表面上色调仍随视角变化。
- 证明几何形成阶段亮度优势更大，仅色度监督产生的几何在相同外观求解后比仅亮度监督差 3.9–5.5 dB，密化可解释部分差距。
- 总体结论：标准 3DGS 的几何形成强烈由亮度主导但非亮度排他，大部分色度外观可在空间支持形成后恢复。

### 局限性
摘要未提供足够信息。论文摘要未提及方法的适用场景限制、失败案例、计算成本分析或对非基准数据集的泛化能力。

### 阅读优先级
高。该研究直接挑战 3DGS 中几何与外观联合学习的常见假设，通过受控实验分离亮度与色度贡献，对理解 3DGS 表示学习机制有重要价值，且结论可能影响后续外观建模和压缩策略的设计。

</details>

<details>
<summary>Abstract</summary>

Standard 3D Gaussian Splatting (3DGS) learns geometry and appearance jointly from RGB supervision, making it difficult to isolate how luminance and chroma contribute to the learned representation. We study this by training models under different channel supervision, freezing their non-appearance parameters (position, scale, rotation, and opacity), and re-estimating appearance with the same solver before comparing held-out reconstruction. Across eleven benchmark scenes with four independent runs each, geometry learned from luminance alone supports held-out reconstruction 0.085 dB below RGB-trained geometry on average. If chroma is deleted from a trained model, a sufficiently expressive solver can re-fit it on the frozen geometry to the original quality or slightly better. Higher-order spherical harmonics contribute much more reconstruction quality to luminance than to chroma, improving PSNR by 1.44 dB versus 0.19 dB on average, although on mirror-like surfaces hue does still change with viewpoint. The luminance advantage is even larger when geometry is being formed. Chroma-only supervision produces geometry 3.9-5.5 dB worse than luminance-only supervision after the same appearance solve; densification explains part of this gap. Overall, geometry formation in standard 3DGS is strongly luminance-dominated but not luminance-exclusive, and much of the chromatic appearance can be recovered after spatial support has formed.

</details>

#### 2026-09-30 - Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems

**Authors:** Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li
**Links:** [abs](https://arxiv.org/abs/2610.00618) - [pdf](https://arxiv.org/pdf/2610.00618)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems
- 作者：Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li
- 出版日期：2026-09-30T19:19:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.00618

### 一句话总结
论文提出用有限窗 DFT 的精确 Dirichlet 核替代 3D Gaussian splatting 中的高斯足迹，以实现波相干成像逆问题的可微渲染，并配合专用求解器 DSFW 完成优化。

### 研究问题
波相干成像（如太赫兹层析、合成孔径声学、毫米波雷达）通过傅里叶处理有限长信号成像，其点扩散函数是 Dirichlet 核（复值、振荡、周期），而不是高斯。论文指出，将 3D Gaussian splatting 直接移植到相干感知中会因构造而失败：高斯 splat 丢弃了旁瓣能量（占总能量的 10-20%）以及控制反射体之间相干干涉的相位。

### 核心思路/方法
核心思想是用有限窗 DFT 的物理精确 Dirichlet 核替换可学习的高斯足迹，并由携带面积、法线和材质信息的 surfel 进行调制，使渲染基元匹配测量物理而非近似它。优化方面提出专用求解器 Dirichlet Sliding Frank-Wolfe（DSFW），结合变量投影、残差对偶证书、由证书驱动的低效用 surfel 硬替换，以及周期性低分辨率耦合 Levenberg-Marquardt 校正，以应对破坏通用一阶优化器的崎岖损失景观。Dirichlet 核具有 O(1) 闭式求值，使前向模型在保持端到端可微的同时，与 FFT 真值匹配到机器精度。

### 主要贡献
- 指出将 3D Gaussian splatting 移植到相干感知中因丢弃旁瓣能量和相位而失败。
- 提出以有限窗 DFT 的精确 Dirichlet 核作为渲染基元，并由 surfel 调制，使渲染匹配测量物理。
- 提出专用求解器 DSFW，结合变量投影、残差对偶证书、证书驱动的硬替换和周期性低分辨率耦合 Levenberg-Marquardt 校正。
- Dirichlet 核支持 O(1) 闭式求值，前向模型与 FFT 真值匹配到机器精度且端到端可微。
- 在密集太赫兹重建中，以 0.018 bin RMSE 恢复反射体中心，比波形级自动微分快 10-50 倍，而 Gaussian splats 失败。

### 局限性
摘要未提供足够信息（未给出方法的适用边界、失败情形、计算开销上限、对其他波段的泛化实验或消融细节）。

### 阅读优先级
高。理由：论文针对波相干成像逆问题提出与测量物理精确匹配的可微渲染基元及专用求解器，并在太赫兹重建上给出定量结果与速度对比，对神经场景表示与渲染、可微逆问题方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Wave-based coherent imaging, including terahertz tomography, synthetic-aperture acoustics, and millimeter-wave radar, forms images by Fourier-processing finite-length signals, with an exact point spread function that is not Gaussian but a Dirichlet kernel: complex-valued, oscillatory, and periodic. However, transplanting 3D Gaussian splatting to coherent sensing fails by construction; Gaussian splats discard the sidelobe energy (10-20% of the total) and the phase that governs coherent interference between reflectors. Our key idea is to replace the learned Gaussian footprint with the physically exact Dirichlet kernel of the finite-window DFT, modulated by a surfel that carries area, normal, and material, so that the rendering primitive matches the measurement physics instead of approximating it. We pair this primitive with a specialized solver, Dirichlet Sliding Frank-Wolfe (DSFW), that combines variable projection, residual dual certificates, and certificate-driven hard replacement of low-utility surfels, with periodic low-resolution coupled Levenberg-Marquardt correction, navigating the rugged loss landscape that breaks generic first-order optimizers. The Dirichlet kernel admits an O(1) closed-form evaluation, so the forward model matches FFT ground truth to machine precision while remaining differentiable end-to-end. On dense terahertz reconstruction, our method recovers reflector centers to 0.018 bin RMSE, 10-50x faster than waveform-level automatic differentiation, where Gaussian splats fail.

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-06 - Demo: Closed-Loop Sionna-Isaac Sim Co-Simulation Framework for Wireless-Aware Robot Navigation over ROS 2

**Authors:** Yi Shen Lim, Seungeun Oh, Jihong Park
**Links:** [abs](https://arxiv.org/abs/2610.08618) - [pdf](https://arxiv.org/pdf/2610.08618)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Demo: Closed-Loop Sionna-Isaac Sim Co-Simulation Framework for Wireless-Aware Robot Navigation over ROS 2
- 作者：Yi Shen Lim, Seungeun Oh, Jihong Park
- 出版日期：2026-10-06T16:17:51Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.08618) / [PDF](https://arxiv.org/pdf/2610.08618)

### 一句话总结
该论文演示了一个基于 ROS 2 的 NVIDIA Isaac Sim 与 NVIDIA Sionna 实时闭环联合仿真框架，用于无线感知的机器人导航。

### 研究问题
当机器人将控制回路卸载到网络时，接收机随机器人移动，链路质量取决于机器人所在位置。要仿真这一场景，需要同时具备物理引擎和站点特定的传播模型。据作者所知，尚无模拟器原生统一两者，已有的两者耦合仅局限于离线分析。

### 核心思路/方法
提出一个实时联合仿真框架，通过 ROS 2 耦合 NVIDIA Isaac Sim 与 NVIDIA Sionna，闭合两者之间的感知-行动-通信（PAC）回路。Sionna 在 Isaac Sim 所仿真的精确几何环境上进行基站到机器人信道的射线追踪，而非随机建模，并将信道状态实时反馈到控制回路。射线追踪在 GPU 上运行，覆盖图刷新约 16ms（约 60 Hz），足以支持实时控制。为展示框架实用性，在基于 OpenStreetMap（OSM）的 SUTD 校园数字孪生中，使用两台 Nova Carter 机器人实现了一个无线感知导航应用。

### 主要贡献
- 提出并演示了一个基于 ROS 2 的实时闭环联合仿真框架，耦合 NVIDIA Isaac Sim 与 NVIDIA Sionna，闭合感知-行动-通信（PAC）回路。
- 使用 Sionna 在 Isaac Sim 的精确几何上进行基站到机器人的信道射线追踪，并实时反馈信道状态到控制回路。
- 展示了 GPU 射线追踪使覆盖图刷新约 16ms（约 60 Hz），满足实时控制需求。
- 在 OSM 派生的 SUTD 校园孪生中用两台 Nova Carter 机器人实现无线感知导航应用：闭环规划器在仅比最短路径基线增加 7.4% 遍历时间的情况下消除了通信中断，而最短路径基线在其 81.2 s 运行中有 7.9 s 处于断连状态。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作属于演示（Demo）性质，聚焦于联合仿真框架的构建与一个具体导航应用展示，对从事机器人仿真、无线感知导航或 ROS 2 集成的读者有直接参考价值；但摘要未提供更广泛的实验对比、可扩展性或通用性验证信息，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

A robot that offloads its control loop to the network carries the receiver with it, so link quality is decided by where it goes. Simulating this requires both a physics engine and a site-specific propagation model at once; to our knowledge no simulator natively unifies both, with existing couplings of the two limited to offline analyses. We demonstrate a real-time co-simulation framework coupling NVIDIA Isaac Sim and NVIDIA Sionna over ROS 2 that closes the perception-action-communication (PAC) loop between them. Sionna ray-traces the base-station-to-robot channel over the exact geometry Isaac Sim simulates on, rather than modeling it stochastically, and feeds channel states back into the control loop in real time. Ray-traced on GPU, the coverage map is refreshed in ~16ms (~60 Hz), fast enough for real-time control. To showcase the framework's utility, we implement a wireless-aware navigation application in an OpenStreetMap(OSM)-derived SUTD campus twin with two Nova Carter robots: the closed-loop planner eliminates communication outage at only +7.4% traversal time over the shortest-path baseline (which spends 7.9 s of its 81.2 s run disconnected).

</details>

#### 2026-10-06 - WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses

**Authors:** Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen, Dung D. Le, Ngo Anh Vien, H. Nguyen-Xuan
**Links:** [abs](https://arxiv.org/abs/2610.08526) - [pdf](https://arxiv.org/pdf/2610.08526)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses
- 作者：Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen, Dung D. Le, Ngo Anh Vien, H. Nguyen-Xuan
- 出版日期：2026-10-06T15:21:14Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：abs: https://arxiv.org/abs/2610.08526 ；pdf: https://arxiv.org/pdf/2610.08526

### 一句话总结
论文提出 WareFly-VLA——一个面向智能仓库中语言引导无人机人员搜索、定位与跟踪的真实感 VLA 框架与数据集，并基于四个开源 VLA 架构建立统一基准，结果显示仓库中的语言条件空中控制仍远未解决。

### 研究问题
- 视觉-语言-动作（VLA）模型在机器人操作与地面移动导航中已取得显著成果，但智能仓库中无人机的语言条件控制仍基本未被探索。
- 主要障碍在于缺乏同时提供连续底层飞行动作、细粒度自然语言目标描述以及真实工业环境的基准。
- 因此需要构建相应的数据集与评测协议，以检验现有 VLA 模型能否胜任仓库场景下的语言引导空中任务。

### 核心思路/方法
- 构建 WareFly-VLA：一个真实感 UAV VLA 框架与数据集，用于仓库环境中语言引导的人员搜索、定位与跟踪。
- 数据在 NVIDIA Isaac Sim 中采集，包含 507 段人工遥操作飞行回合与 8,504 个高分辨率 RGB 转换样本；每个样本配有人工撰写的目标工人外观描述以及同步的四自由度控制指令。
- 覆盖两类空中任务：目标接近（target approach）与人员跟随（person following），并设置遮挡、远距离搜索、高度变化与杂乱环境等条件。
- 建立统一基准，纳入四个开源 VLA 架构（SmolVLA、GR00T N1.7、pi_0、OpenVLA），在无泄漏的回合级协议下、于两种控制频率进行评测。
- 数据集同时提供同步的视频、语言、动作、位姿与难度标注，以支持世界模型研究。

### 主要贡献
- 提出并发布 WareFly-VLA 框架与数据集，填补智能仓库中语言条件无人机控制基准的空白。
- 提供 507 段人工遥操作飞行回合与 8,504 个高分辨率 RGB 转换，每项均配有人工外观描述与四自由度同步控制指令。
- 覆盖目标接近与人员跟随两类任务，并包含遮挡、远距离搜索、高度变化与杂乱等挑战条件。
- 建立四个开源 VLA 架构在两种控制频率、无泄漏回合级协议下的统一基准。
- 给出关键实证发现：严格泛化设置下性能大幅下降；连续动作建模持续优于离散动作 token 化；单帧下仅前向通道可靠可学；当前基础模型接口从地面与类人形态向空中平台迁移效果差。
- 发布数据集、基线方法与评测协议，以支持智能仓库中的语言接地空中自主研究。

### 局限性
- 摘要未提供足够信息说明真实世界部署验证情况；数据均在 NVIDIA Isaac Sim 中采集。
- 摘要未提供足够信息说明数据集规模相对于任务复杂度的充分性讨论。
- 摘要未提供足够信息说明各基线模型的具体失败模式细节与定量数值。
- 摘要未提供足够信息说明四自由度控制指令的具体维度构成与动作空间定义。
- 摘要未提供足够信息说明难度标注的具体分级标准与标注一致性。
- 摘要未提供足够信息说明除前向通道外其他通道不可靠学习的原因分析。

### 阅读优先级
高。理由：该工作同时提供新数据集、统一基准与明确的反直觉实证结论（如连续动作优于离散 token 化、基础模型跨形态迁移差、单帧仅前向通道可学），对 VLA 与空中具身智能交叉方向具有直接参考价值；摘要所述内容足以支撑将其列为重点跟踪对象。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved impressive results in robotic manipulation and ground-mobile navigation, yet language-conditioned control of unmanned aerial vehicles (UAVs) in smart warehouses remains largely unexplored, hindered by the lack of benchmarks that jointly provide continuous low-level flight actions, fine-grained natural-language target descriptions, and realistic industrial environments. This paper introduces WareFly-VLA, a photorealistic UAV VLA framework and dataset for language-guided human search, localization, and tracking in warehouse environments. It contains 507 human-teleoperated flight episodes and 8,504 high-resolution RGB transitions collected in NVIDIA Isaac Sim, each paired with a human-written appearance description of the target worker and a synchronized four-degree-of-freedom control command. Two aerial tasks are covered: target approach and person following, under occlusion, long-range search, altitude variation, and clutter. A unified benchmark of four open-source VLA architectures (SmolVLA, GR00T N1.7, pi_0 and OpenVLA) is established under a leakage-free episode-level protocol at two control rates. The results show that language-conditioned aerial control in warehouses is far from solved: performance drops substantially under strict generalization settings, continuous action modeling consistently outperforms discrete action tokenization, only the forward channel is reliably learnable from a single frame, and current foundation-model interfaces transfer poorly from ground and humanoid embodiments to aerial platforms. The synchronized video, language, action, pose, and difficulty annotations further support world-model research. The dataset, baselines, and evaluation protocol are released to support language-grounded aerial autonomy in smart warehouses.

</details>

#### 2026-10-06 - Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization

**Authors:** Xuekang Zhu, Kaiwen Feng, Ruifeng Wang, Xiwen Wang, Xiaochen Ma, Bo Du, Changjiang Jiang, Chenfan Qu, Songyu Ye, Xia Du, Wentao Feng, Jian Liu, Ji-Zhe Zhou
**Links:** [abs](https://arxiv.org/abs/2610.07916) - [pdf](https://arxiv.org/pdf/2610.07916)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization
- 作者：Xuekang Zhu, Kaiwen Feng, Ruifeng Wang, Xiwen Wang, Xiaochen Ma, Bo Du, Changjiang Jiang, Chenfan Qu, Songyu Ye, Xia Du, Wentao Feng, Jian Liu, Ji-Zhe Zhou
- 出版日期：2026-10-06T07:58:40Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次要分类信息
- 链接：摘要页 https://arxiv.org/abs/2610.07916；PDF https://arxiv.org/pdf/2610.07916

### 一句话总结
该论文将图像篡改定位（IML）重新解释为以伪影为隐变量的概率问题，指出现有模型对伪影的隐式建模不足，并提出通过成对编辑关系进行特征解耦的两阶段学习范式 PAL 与 SL，同时构建了 EditGroup-45K 数据集。

### 研究问题
论文关注图像篡改定位任务。作者首先揭示伪影的潜在性质，将 IML 从常规的全监督学习重新表述为隐变量问题：$P(y|x)=\int P(y|z)\,P(z|x)\,dz$，其中 $z$ 表示伪影。基于这一解释，作者指出现有 IML 模型不足的原因在于它们采用隐式的伪影建模策略，并强调以显式方式建模 $z$ 的必要性。

### 核心思路/方法
由于没有伪影的直接标签，作者认为特征解耦是进行显式建模最合适的方案。为此，论文提出一个两阶段学习范式，包含 Pairwise Artifacts Learning (PAL) 与 Standard Localization (SL) 两个阶段，分别通过编辑关系估计 $P(z|x)$ 与 $P(y|z)$。为支持这种基于编辑关系的学习，作者构建了 EditGroup-45K，一个以源图像为锚、组织为编辑组以构造配对的数据集。摘要提到进行了大量实验。

### 主要贡献
- 揭示伪影的潜在性质，将 IML 重新解释为隐变量问题 $P(y|x)=\int P(y|z)\,P(z|x)\,dz$。
- 指出现有 IML 模型不足的原因是其隐式伪影建模策略，并强调显式建模 $z$ 的必要性。
- 提出两阶段学习范式 PAL 与 SL，通过编辑关系分别估计 $P(z|x)$ 和 $P(y|z)$。
- 构建 EditGroup-45K 数据集，采用源图像锚定并组织为编辑组以支持配对构造。
- 摘要称实验表明 PAL 范式在多种 IML 架构上带来一致提升，且经验分析验证 PAL 确实通过特征解耦显式捕获了伪影。

### 局限性
摘要未提供足够信息说明该方法的具体失败情形、计算开销、对特定编辑类型的敏感性、数据集覆盖范围之外的泛化能力，也未给出具体实验设置、评价指标细节与消融结果；此外，论文被归入 Embodied / Robotics / AR Applications 分类，但摘要未说明该分类与 IML 任务之间的具体关联。

### 阅读优先级
中。理由：该论文对 IML 提出了较清晰的问题重构（隐变量视角）与显式的解耦学习方案，并配套提出数据集，若关注图像篡改定位、特征解耦或数据集构建，具有一定参考价值；但摘要未提供足够的实验细节与量化结果，且分类标签与任务主题之间的关联不明确，因此优先级不宜直接判为高。

</details>

<details>
<summary>Abstract</summary>

Image Manipulation Localization (IML) is commonly formulated as a fully supervised learning task that estimates the optimal manipulation mask $y$ for a given image $x$. In this work, we first reveal the latent nature of artifacts and thus reinterpret IML as a latent-variable problem, $P(y|x)=\int P(y|z)\,P(z|x)\,dz$, where $z$ denotes the artifacts. Following this interpretation, we pinpoint the cause for the current IML models' insufficiency as their implicit artifacts modeling strategy, highlighting the necessity of modeling $z$ in an explicit manner. Without direct labels, feature disentanglement is the most appropriate solution for this explicit modeling. Accordingly, we propose a two-stage learning paradigm with the Pairwise Artifacts Learning (PAL) and Standard Localization (SL) phases to estimate $P(z|x)$ and $P(y|z)$ via edit relations. To support our edit-relation-based learning, we further curate EditGroup-45K, a source-anchored dataset organized into edit groups for pair construction. Extensive experiments show that our PAL paradigm yields consistent improvements across diverse IML architectures, and empirical analyses further verify that PAL does capture artifacts explicitly through feature disentanglement. Code and dataset are available at https://github.com/venus-guangjian/PAL

</details>

#### 2026-10-06 - CoRE: Learning Collaboration-Role Experts for Decentralized Collaborative Manipulation with One Policy

**Authors:** Yanan Zhou, Zhaoyan Qian, Zihao Li, Mingyuan Ba, Ranpeng Qiu, Weiming Zhi
**Links:** [abs](https://arxiv.org/abs/2610.07752) - [pdf](https://arxiv.org/pdf/2610.07752)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoRE: Learning Collaboration-Role Experts for Decentralized Collaborative Manipulation with One Policy
- 作者：Yanan Zhou, Zhaoyan Qian, Zihao Li, Mingyuan Ba, Ranpeng Qiu, Weiming Zhi
- 出版日期：2026-10-06T04:49:11Z
- 分类：Embodied / Robotics / AR Applications（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2610.07752) / [PDF](https://arxiv.org/pdf/2610.07752) / [项目页](https://aus.bot/research/core/)

### 一句话总结
CoRE 面向“单策略、去中心化”的协作操作设定，通过从多任务多机器人演示中学习“协作角色专家”，让每个机器人在共享参数下仅凭局部视觉与本体感知采取互补动作。

### 研究问题
论文研究的是**单策略去中心化协作**：每个机器人执行同一个策略，输入仅为自身的视觉观测和本体感知，不使用任务提示、身份标签或机器人间通信。核心挑战在于：在共享参数的前提下学习出互补的团队行为，并使每个机器人能基于**局部观测**选择恰当的动作。

### 核心思路/方法
- 从**汇总的多任务、多机器人演示**中学习“协作角色专家”（Collaboration-Role Experts）。
- 使用**融合的外观与几何信息**作为局部交互证据。
- 采用**查询条件化的交叉注意力专家**，提供可适应的预测路径；由**局部路由器**在每个动作块（action-chunk）位置上对各专家进行组合。
- 训练阶段引入**动作—专家对齐损失**：在固定输入下，以相对强制路由预测误差对比演示来监督专家选择，且**无需角色标签**。

### 主要贡献
- 提出 CoRE 方法，在无任务提示、无身份标签、无机器人间通信的单策略去中心化设定下学习互补协作行为。
- 设计基于外观与几何融合的局部交互证据、查询条件化交叉注意力专家与局部路由器组合机制。
- 提出无需角色标签的动作—专家对齐损失，用相对强制路由预测误差监督专家选择。
- 摘要称：在仿真基准中，CoRE 在所评估的去中心化方法中取得最高平均性能；物理实验显示其在多种操作任务中有效协作，并对伙伴延迟和减速具有鲁棒性。

### 局限性
- 具体仿真基准名称、任务数量、对比方法清单及量化指标：摘要未提供足够信息。
- 物理实验的平台、任务细节、评价指标与样本规模：摘要未提供足够信息。
- 方法对更复杂场景（如更多机器人、更高维感知、不同通信约束变体）的泛化能力：摘要未提供足够信息。
- 训练所需演示数据的规模、采集成本与对演示质量的敏感性：摘要未提供足够信息。
- 与集中式或带通信方法的性能差距分析：摘要未提供足够信息。

### 阅读优先级
**中**
理由：该论文聚焦去中心化单策略协作操作，且声称在仿真中取得所评估去中心化方法中的最高平均性能，并有物理实验验证，对具身智能与多机器人协作方向具有参考价值；但摘要未给出具体基准、指标与实验细节，无法仅凭摘要判断其性能优势幅度与方法边界，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

Collaborative manipulation requires robots to perform complementary actions as interactions unfold. We study single-policy decentralized collaboration: every robot runs the same policy from its visual observations and proprioception, without task prompts, identity labels, or inter-robot messages. The challenge is to learn complementary team behaviors within shared parameters and select appropriate actions from each robot's local observations. We introduce CoRE, which learns Collaboration-Role Experts from pooled multi-task, multi-robot demonstrations. Fused appearance and geometry provide local interaction evidence. Query-conditioned cross-attention experts provide adaptable prediction paths, which a local router combines at each action-chunk position. During training, an action-expert alignment loss supervises expert selection using relative forced-route prediction errors against demonstrations under fixed inputs, without role labels. Across simulation benchmarks, CoRE achieves the highest average performance among evaluated decentralized methods. Physical experiments demonstrate effective collaboration across diverse manipulation tasks and robustness to partner delays and slowdowns. Project page: https://aus.bot/research/core/.

</details>

#### 2026-10-05 - GeoWM: Efficient Direct World Modeling in Explicit Geometry

**Authors:** Mehrdad Noori, Guile Wu, Sam Hosseini, Dongfeng Bai
**Links:** [abs](https://arxiv.org/abs/2610.07381) - [pdf](https://arxiv.org/pdf/2610.07381)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometry foundation model, robotics, manipulation, autonomous driving, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoWM: Efficient Direct World Modeling in Explicit Geometry
- 作者：Mehrdad Noori, Guile Wu, Sam Hosseini, Dongfeng Bai
- 出版日期：2026-10-05T20:52:18Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.07381 ；PDF https://arxiv.org/pdf/2610.07381

### 一句话总结
GeoWM 是一种直接在显式几何空间中进行世界建模的方法，通过几何基础模型构建几何历史并借助流匹配 transformer，直接预测指定未来时刻的场景几何，从而避免递归 rollout 带来的误差累积与计算开销。

### 研究问题
论文关注 3D 场景几何及其随时间演化的建模问题，指出这一能力对自动驾驶和机器人领域至关重要。现有常见范式是使用世界模型预测未来图像或环境的潜在表示，再从这些预测中恢复几何。摘要指出该范式存在两点不足：一是没有显式建模几何结构，二是通常依赖递归 rollout 来达到更长的预测时域，导致误差累积与计算成本上升。

### 核心思路/方法
GeoWM 的核心是“直接”在显式几何上预测未来场景几何，而非递归 rollout，也不经过“先预测图像或潜表示、再恢复几何”的间接路径。其关键设计包括：
- 利用几何基础模型将观测到的 RGB 帧转换为“几何历史”；
- 以该几何历史作为条件，输入一个流匹配 transformer，预测指定未来时域的场景几何；
- 使用轻量级相机运动预测器估计未来视角；
- 将观测到的几何投影到预测视角中，作为未来几何预测的有效几何先验。

### 主要贡献
- 提出 GeoWM，一种几何世界模型，可直接预测指定未来时域的场景几何，无需递归 rollout。
- 借助几何基础模型构建几何历史，并以此条件化流匹配 transformer 进行未来几何预测。
- 展示轻量级相机运动预测器可准确估计未来视角，且将观测几何投影到预测视角可为未来几何预测提供有效几何先验。
- 在覆盖城市驾驶、空中飞行和动态操作的四个数据集上进行实验，摘要称 GeoWM 在深度、相机位姿和 3D 场景几何预测上优于所评估的世界模型，同时在更长预测时域下显著降低推理时间。

### 局限性
- 摘要未提供足够信息说明方法在极端场景、不同传感器配置或分布外数据上的表现。
- 摘要未提供足够信息说明各数据集的具体规模、评价指标细节及消融实验的完整结果。
- 摘要未提供足够信息说明几何基础模型与流匹配 transformer 的具体架构、训练成本及超参数敏感性。
- 摘要未提供足够信息说明相机运动预测器的适用范围与失效条件。

### 阅读优先级
高。理由：该论文针对世界模型中递归 rollout 导致误差累积和长时域推理成本高这一明确痛点，提出直接在显式几何空间预测未来场景几何的替代范式，并声称在四类数据集上同时提升深度、位姿与 3D 几何预测表现、降低长时域推理时间。对自动驾驶、机器人和具身智能中需要几何一致长时预测的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Modeling 3D scene geometry and its evolution over time is essential for autonomous driving and robotics. A common paradigm is to use world models to predict future images or latent representations of the environment and subsequently recover geometry from these predictions. However, this paradigm does not explicitly model geometric structure and typically relies on recursive rollouts to reach longer prediction horizons, leading to error accumulation and increasing computational cost. To address these limitations, we present GeoWM, a geometry world model that directly forecasts future scene geometry at specified future horizons without recursive rollout. The key idea is to leverage a geometry foundation model to transform observed RGB frames into a geometric history, which conditions a flow-matching transformer to predict the scene geometry at a specified future horizon. We further show that a lightweight camera-motion predictor can accurately estimate the future viewpoint, and that projecting the observed geometry into the predicted viewpoint provides an effective geometric prior for future geometry forecasting. Extensive experiments on four datasets spanning urban driving, aerial flight, and dynamic manipulation demonstrate that GeoWM outperforms the evaluated world models in forecasting depth, camera pose, and 3D scene geometry, while substantially reducing inference time at longer horizons.

</details>

#### 2026-10-05 - AIM: Adaptive Interaction Modeling Networks for Real-to-Sim Soft-Body Simulation

**Authors:** Tiancheng Yang, Dingshuo Chen, Tianle Chen, Zhaocheng Liu, Qiang Liu
**Links:** [abs](https://arxiv.org/abs/2610.07116) - [pdf](https://arxiv.org/pdf/2610.07116)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AIM: Adaptive Interaction Modeling Networks for Real-to-Sim Soft-Body Simulation
- 作者：Tiancheng Yang, Dingshuo Chen, Tianle Chen, Zhaocheng Liu, Qiang Liu
- 出版日期：2026-10-05T16:52:23Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[abstract_url](https://arxiv.org/abs/2610.07116) / [pdf_url](https://arxiv.org/pdf/2610.07116)

### 一句话总结
AIM 将真实到仿真的软体仿真建模为局部—全局交互问题，通过自适应粒子关系建模与几何条件化的全局通信，提升可变形物体在外力交互下的形变预测精度与长时程稳定性。

### 研究问题
可变形物体操作（如叠衣物、处理食物）要求机器人同时控制物体形状变化与运动。预测式软体仿真可通过预判外力交互下的形变来支持这类任务，但存在两个问题：
1. 基于空间邻域的关系建模可能错误表达形变依赖，引入局部误差，并在连续预测中不断累积；
2. 针对单个场景拟合的模型，难以适应物体几何形状与操作条件的变化。

### 核心思路/方法
AIM 将 real-to-sim 软体仿真视为局部—全局交互建模问题，主要包含：
- 利用运动历史与几何信息，在当前空间邻居与保留连接（retained connections）之上自适应地调整粒子关系；
- 使用几何条件化的全局通信，协调物体整体层面的响应；
- 采用统一运动学控制点接口，表示不同的操作配置；
- 使用多步自回归监督，让模型在自己的预测轨迹上进行训练。

### 主要贡献
- 提出 AIM 框架，将 real-to-sim 软体仿真形式化为局部—全局交互建模问题。
- 通过运动历史与几何自适应的粒子关系建模，以及几何条件化的全局通信，缓解局部邻域建模误差及其累积问题。
- 设计统一运动学控制点接口与多步自回归监督，以适配不同操作配置并提升长时程预测能力。
- 在 PhysTwin 与 PGND 上的实验显示：相对 PhysTwin，未来预测跟踪误差降低 20.0%；相对 PGND，在六类物体上的平均长时程粒子误差降低 22.8%。
- 支持跨动作、跨物体实例与跨场景迁移，包括从机器人交互到人类操作的零样本迁移，且无需目标域动力学拟合。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作面向机器人可变形物体操作中的 real-to-sim 软体仿真核心难题，提出了局部—全局交互建模的统一框架，并报告了明确的误差下降与跨动作、跨实例、跨场景乃至零样本迁移能力；对具身智能、机器人操作与仿真学习方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Deformable-object manipulation is essential for robotic tasks such as folding laundry and handling food, where robots must control shape changes as well as object motion. Predictive soft-body simulation supports these tasks by anticipating deformation under external interactions. However, spatial neighborhoods can misrepresent deformation dependencies, introducing local errors that accumulate over successive predictions. Models fitted to individual scenes must also accommodate changes in object geometry and manipulation conditions. In this work, we propose AIM, an Adaptive Interaction Modeling framework that treats real-to-sim soft-body simulation as a local-global interaction modeling problem. AIM uses motion history and geometry to adapt particle relations over current spatial neighbors and retained connections, while geometry-conditioned global communication coordinates object-wide responses. A unified kinematic control-point interface represents different manipulation configurations, and multi-step autoregressive supervision trains the model on its own predicted trajectories. Experiments on PhysTwin and PGND demonstrate improved motion accuracy and visual fidelity, with a 20.0% reduction in future-prediction tracking error relative to PhysTwin and a 22.8% reduction in mean long-horizon particle error across six object categories relative to PGND. The framework further supports transfer across actions, object instances, and scenes, including zero-shot transfer from robot interactions to human manipulation without target-domain dynamics fitting.

</details>

#### 2026-10-04 - RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation

**Authors:** Huapeng Li, Fuxiang Feng, Jinqiu Fan, Shuo Yang, Fengjiao Chen, Xuezhi Cao, Ran Song, Wei Zhang
**Links:** [abs](https://arxiv.org/abs/2610.05414) - [pdf](https://arxiv.org/pdf/2610.05414)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation
- 作者：Huapeng Li, Fuxiang Feng, Jinqiu Fan, Shuo Yang, Fengjiao Chen, Xuezhi Cao, Ran Song, Wei Zhang
- 出版日期：2026-10-04T17:55:26Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.05414 ；PDF https://arxiv.org/pdf/2610.05414 ；项目页 https://mxxq-stack.github.io/rmmbench-project/

### 一句话总结
RMMBench 是一个面向机器人移动操作的评测基准，通过统一框架整合高层与低层具身任务，构建 70 个“导航—操作”任务场景，用于更细粒度地评估 VLM 在连续空间长时程任务中的具身能力。

### 研究问题
尽管视觉语言模型（VLMs）提升了机器人的环境理解与任务推理能力，但如何全面评估 VLMs 在机器人导航与操作中的集成效果仍是问题。摘要指出，当前基准缺乏评估多样化机器人任务的综合方法，评估指标也相对有限，难以全面、细粒度地衡量 VLMs 的具身能力。

### 核心思路/方法
论文提出 RMMBench，要求机器人理解语言指令并在连续空间中执行长时程任务。该基准将高层和低层具身任务无缝集成到统一框架中，构建了一个“导航—操作”任务套件，包含 70 个规范任务场景，覆盖从局部操作到长时程复合导航的任务范围。

### 主要贡献
- 提出 RMMBench，一个面向机器人移动操作的综合评测基准。
- 将高层与低层具身任务整合进统一框架。
- 构建包含 70 个规范任务场景的“导航—操作”任务套件，覆盖从局部操作到长时程复合导航。
- 通过该基准评估发现，领先 VLMs 在执行移动操作任务时仍面临空间定位方面的重大挑战，并凸显在长时程交互中增强机器人空间感知能力的必要性。

### 局限性
摘要未提供足够信息。摘要未说明基准的具体实验设置、对比方法数量、评测指标细节、任务成功判定方式、仿真或真实环境配置，也未说明其局限性或失败案例。

### 阅读优先级
高。理由：该论文聚焦 VLM 与机器人移动操作评测，提出统一的高层/低层任务框架和 70 个任务场景，并给出对当前领先 VLMs 在空间定位与长时程交互方面的关键发现；对具身智能、机器人导航与操作、VLM 机器人集成评测方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Although the advancement of vision-language models (VLMs) has endowed robots with enhanced environmental understanding and task reasoning, a comprehensive evaluation methodology is important to advance the integration of VLMs in robotic navigation and manipulation. However, current benchmarks lack a comprehensive method to evaluate diverse robotic tasks, and evaluation metrics remain relatively constrained, making it difficult to assess the embodied capabilities of VLMs in a thorough and fine-grained manner. To address this issue, we propose RMMBench, an evaluation benchmark that requires robots to understand language instructions and perform long-horizon tasks in continuous spaces. RMMBench seamlessly integrates high- and low-level embodied tasks into a unified framework, constructing a "navigation-manipulation" task suite comprising 70 canonical task scenarios that range from localized manipulation to long-horizon composite navigation. The results reveal that leading VLMs still face major challenges in spatial localization when performing mobile manipulation tasks, and also highlight the necessity of enhancing the spatial perception capability of robots during long-horizon interactions. RMMBench can be accessed at https://mxxq-stack.github.io/rmmbench-project/

</details>

#### 2026-10-04 - Reflection-Robust 6DoF Object Tracking with Light Fields

**Authors:** Nikolai Goncharov, Donald G. Dansereau
**Links:** [abs](https://arxiv.org/abs/2610.04883) - [pdf](https://arxiv.org/pdf/2610.04883)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reflection-Robust 6DoF Object Tracking with Light Fields
- 作者：Nikolai Goncharov, Donald G. Dansereau
- 出版日期：2026-10-04T02:45:31Z
- 分类：Embodied / Robotics / AR Applications（主要分类；次要分类摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2610.04883) | [PDF](https://arxiv.org/pdf/2610.04883)

### 一句话总结
该论文提出一种基于光场的抗反射 6DoF 刚体目标跟踪方法，将反射造成的视角相关外观变化从干扰转化为位姿线索，并在自建光场跟踪数据集与两段实拍光场序列上验证，是唯一在高反射条件下保持精度的对比方法。

### 研究问题
现有 6DoF 刚体目标跟踪器普遍假设目标外观在序列中保持稳定，但这一假设在反射表面上不成立——反射表面的外观会随其映照的环境而变化。论文要解决的核心问题是：如何在存在视角相关反射外观的情况下，仍然稳健地跟踪运动刚体目标的 6DoF 位姿。

### 核心思路/方法
- 利用光场信息，将反射这一“表面麻烦”重新解释为位姿线索。
- 逐帧流程：
  1. 在抗反射条件下鲁棒地恢复深度，并反投影为点云，进而估计表面法线；
  2. 将目标的视角相关外观分解为漫反射反照率与其所反射的环境贴图，得到一个可重光照的表面光场；
  3. 从粗略初始化出发，用恢复出的环境贴图进行重光照，并在光度损失上优化位姿。
- 关键机制：由于运动目标会映照出场景中的新部分，环境贴图随序列推进不断被填充，使该光度信号随时间变得更锐利、更有利。

### 主要贡献
- 提出一种光场基础、抗反射的 6DoF 跟踪器，把视角相关反射外观显式建模为漫反射反照率与环境贴图的分解，并用于位姿优化。
- 提出一种随序列推进而自我增强的机制：运动目标不断映照新场景区域，使环境贴图逐步补全、跟踪信号逐步锐化。
- 构建了一个新的光场跟踪数据集：从机器人操作基准重新渲染，包含四个受控反射率水平，并为每一水平配以模拟深度，用以复现消费级 RGB-D 传感器在光亮表面上的失效模式。
- 额外在两段实拍光场序列上进行评估。
- 实验结论：在漫反射目标上，该方法落后于最强基线；但在完全反射目标上，它是唯一保持精度的方案，而所有基线均出现性能退化。

### 局限性
- 摘要明确承认在漫反射目标上弱于最强基线，说明方法并非在所有外观条件下占优。
- 摘要未提供足够信息：具体基线方法名称、各数据集上的量化指标数值、消融实验、运行时间与实时性、对光场采集硬件与标定的依赖程度、失败案例与边界条件。
- 摘要未提供足够信息：四个受控反射率水平的具体设定，以及模拟深度的具体失效建模方式。
- 摘要未提供足够信息：方法对非刚性形变、遮挡、快速运动等更一般场景的适用性。

### 阅读优先级
高。理由：该论文针对 6DoF 跟踪中长期被假设忽略的反射外观问题提出明确的新建模思路（可重光照表面光场 + 环境贴图随时间补全），并配套了带受控反射率与模拟深度失效的新基准数据集；摘要给出的结论对比鲜明（漫反射略逊、全反射唯一不退化），对机器人操作、自动驾驶与 AR 相关跟踪研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Tracking the 6DoF pose of a moving rigid object is fundamental to robotics and autonomous driving, but existing trackers assume that object appearance is stable across a sequence, an assumption that breaks down on reflective surfaces whose appearance changes as they mirror the environment. We introduce a light field based reflection-robust 6DoF tracker that turns this apparent nuisance into a pose cue. Per frame, our method recovers depth robustly against reflections, back-projects it into a point cloud, and estimates surface normals. It then decomposes the object's view-dependent appearance into a diffuse albedo and the environment map it reflects, resulting in a relightable surface light field. Starting from a coarse initialization, we relight it by the recovered environment map and optimize the pose on the photometric loss. Because a moving object mirrors new parts of the scene, the environment map fills in as the sequence proceeds, sharpening this signal over time. To evaluate this approach, we introduce a light field tracking dataset re-rendered from a robotic manipulation benchmark at four controlled reflectivity levels, each paired with simulated depth that reproduces how consumer RGB-D sensors fail on shiny surfaces. Additionally, we evaluate on two captured light field sequences. Our method trails the strongest baselines on diffuse objects and is the only one that holds its accuracy on fully reflective objects, where every baseline degrades.

</details>

#### 2026-10-01 - World Observer: Joint Actor-Observer Generation for Persistent World Modeling

**Authors:** Hyunwook Choi, Dahyun Chung, Hyunsung Kim, Siyoon Jin, Jinhyeok Choi, Junyoung Seo, Seungryong Kim
**Links:** [abs](https://arxiv.org/abs/2610.02162) - [pdf](https://arxiv.org/pdf/2610.02162)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：World Observer: Joint Actor-Observer Generation for Persistent World Modeling
- 作者：Hyunwook Choi, Dahyun Chung, Hyunsung Kim, Siyoon Jin, Jinhyeok Choi, Junyoung Seo, Seungryong Kim
- 出版日期：2026-10-01T17:53:20Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类摘要未提供足够信息
- 链接：摘要链接 https://arxiv.org/abs/2610.02162 ；PDF 链接 https://arxiv.org/pdf/2610.02162

### 一句话总结
World Observer 通过将“观察”与“行动”解耦，联合生成以智能体为中心的 actor 视角与一个或多个全景 observer，以缓解视频世界模型在物体离开 actor 视野后丢失其演化状态的问题。

### 研究问题
论文关注视频世界模型中的持续世界建模问题：现有视频世界模型通常以 actor 为中心来模拟环境随动作的演化，但一旦物体离开 actor 的当前视野，模型就失去对该物体演化的直接证据，导致物体重新进入视野时难以保持其状态与动态。核心问题是：世界模型如何持续观察 actor 当前视野之外的区域？

### 核心思路/方法
- 将观察与行动解耦：不再仅生成 actor 视角，而是联合生成一个以智能体为中心的 perspective actor，以及一个或多个观察选定世界区域的全景 observer。
- 通过 observer 保持离视野物体的视觉演化：离开 actor 视野的物体仍可在 observer 中持续演化，从而在其重新进入 actor 视野时反映更新后的状态。
- 几何对应：从共享的全景源进行 warp，以显式建立 actor 与 observer 之间的几何对应关系。
- Observer Sink：引入高分辨率透视参考，用于在物体重新进入视野时恢复精细外观。
- 灵活放置与控制：由于 observer 与 actor 解耦，observer 可自由放置在场景中、扩展到多个位置以扩大覆盖范围，并可由控制信号驱动以引导视野外的演化。
- 评估方式：提出 world-space metrics 以及覆盖真实与合成场景的 benchmark，用于评估视野外演化。

### 主要贡献
- 提出 World Observer，一种联合 actor-observer 生成框架，用于持续世界建模，使离开 actor 视野的物体仍能被持续观察并保持演化。
- 通过共享全景源 warp 建立 actor 与 observer 的显式几何对应，并引入 Observer Sink 高分辨率透视参考来恢复重新进入时的精细外观。
- 将 observer 与 actor 解耦，使其可自由放置、多位置扩展，并可由控制信号驱动以引导视野外演化。
- 引入用于评估视野外演化的 world-space metrics 和覆盖真实与合成场景的 benchmark。
- 摘要声称 World Observer 在显著改善视野外动态的同时，在视觉保真度、相机控制和 3D  adherence 方面仍具竞争力。

### 局限性
摘要未提供足够信息。论文摘要未说明具体失败场景、计算成本、对 observer 数量或放置方式的依赖、benchmark 规模、真实场景与合成场景的具体构成，也未给出与基线方法的详细定量比较。

### 阅读优先级
高。理由：该论文针对视频世界模型中一个明确且重要的问题，即 actor 离开视野后物体状态与动态难以保持，并提出了解耦 actor 与 observer 的框架、配套评估指标与 benchmark。对于关注 embodied / robotics / AR 应用、视频世界模型、持续世界建模与视野外演化生成的研究者，具有较高相关性和潜在参考价值。

</details>

<details>
<summary>Abstract</summary>

How can a world model continuously observe regions beyond the actor's current view? Video world models simulate how an environment evolves from an agent's actions, yet remain actor-centric. Once an object leaves the actor's view, they lose direct evidence of its evolution, often failing to preserve its state and dynamics upon re-entry. To address this, we introduce World Observer, which decouples observing from acting by jointly generating a perspective actor for the agent-centric view with one or more panoramic observers that watch selected world regions. This allows objects that leave the actor's view to remain visually evolving in an observer, so their updated states are reflected when they re-enter. We ground the actor and observers by warping from a shared panoramic source for explicit geometric correspondence, and introduce an Observer Sink of high-resolution perspective references to restore fine appearance upon re-entry. Since the observers are decoupled from the actor, they can be placed freely across the scene, extended to multiple locations for broader coverage, and driven by control signals to steer out-of-view evolution. To evaluate out-of-view evolution, we further introduce world-space metrics and a benchmark spanning real and synthetic scenes. World Observer substantially improves out-of-view dynamics while remaining competitive in visual fidelity, camera control, and 3D adherence.

</details>

#### 2026-10-01 - GlassGuard: Verified Glass Plane Mapping for Robot Navigation

**Authors:** Hanwen Guo, Zhengzhi Lin, Yusen Xie, Ji Zhang
**Links:** [abs](https://arxiv.org/abs/2610.02110) - [pdf](https://arxiv.org/pdf/2610.02110)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GlassGuard: Verified Glass Plane Mapping for Robot Navigation
- 作者：Hanwen Guo, Zhengzhi Lin, Yusen Xie, Ji Zhang
- 出版日期：2026-10-01T17:31:23Z
- 分类：Embodied / Robotics / AR Applications（无二级分类信息）
- 链接：[摘要](https://arxiv.org/abs/2610.02110) | [PDF](https://arxiv.org/pdf/2610.02110)

### 一句话总结
GlassGuard 是一个面向机器人导航的玻璃平面重建框架，利用视觉与 LiDAR 的互补证据恢复建筑玻璃平面，并在“玻璃覆盖率”与“自由空间污染”两个维度上同时优化。

### 研究问题
透明和镜面表面对基于 LiDAR 的 SLAM 与导航构成严重挑战：激光回波可能穿过玻璃，导致碰撞边界在地图中缺失。已有工作尝试重建缺失表面，但不准确的障碍物放置可能引发相反方向的失败，即污染可通行的自由空间。因此论文将玻璃重建视为一个双重需求问题：既要覆盖玻璃，又要避免自由空间被错误占据。

### 核心思路/方法
- 提出 GlassGuard，一个面向导航的框架，从互补的视觉与 LiDAR 证据中重建平面建筑玻璃。
- 将“成功”定义为同时考虑玻璃覆盖率与自由空间污染，并将这一原则贯穿提案验证与全局地图构建。
- 方法流程：基础视觉模型提供玻璃实例掩码；结构化 3D 线索生成度量平面假设；无深度的 2D 投影几何检查其朝向；随后进入统一的全局地图。

### 主要贡献
- 明确提出玻璃重建中的双重需求：既不能漏掉玻璃碰撞边界，也不能因此污染自由空间。
- 提出结合视觉实例掩码、结构化 3D 线索与无需深度的 2D 投影几何验证的玻璃平面重建流程。
- 在九个建筑尺度场景中评估，覆盖多样玻璃结构、空间尺度与光照条件，包含超过一小时、2.1 km 的真实机器人行进。
- 全景版本达到 85% 的总玻璃覆盖率；在相同针孔输入下达到 82% 总覆盖率（对比基线最高 61%），同时每帧假体素数减少 5–17 倍。
- 定性示例表明，结合导航规划器时，重建平面能够阻断穿过玻璃的路径，同时保留可通行路线。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、计算开销、不同玻璃类型（如曲面玻璃、多层玻璃）的适用边界，也未给出基线的具体名称与完整实验设置。

### 阅读优先级
高。理由：论文针对 LiDAR 导航中玻璃导致的碰撞边界缺失这一实际痛点，且同时关注漏检与自由空间污染的双重指标；提供了建筑尺度真实机器人数据上的覆盖率与假体素对比结果，对机器人导航、SLAM 与建图方向的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Transparent and specular surfaces pose a serious challenge to LiDAR-based SLAM and navigation because laser returns may pass through glass, leaving collision boundaries absent from the map. Prior work attempts to reconstruct the missing surfaces, but inaccurate obstacle placement can create the opposite failure: contamination of traversable free space. Recognizing this dual requirement, we present GlassGuard, a navigation-oriented framework for reconstructing planar architectural glass from complementary visual and LiDAR evidence. We formulate success in terms of both glass coverage and free-space contamination and apply this principle throughout proposal verification and global map construction. A foundation vision model provides glass-instance masks, structural 3D cues generate metric plane hypotheses, and depth-free 2D projective geometry checks their orientations before they enter a consolidated global map. We evaluate GlassGuard in nine building-scale scenes spanning diverse glass structures, spatial scales, and lighting conditions, with more than one hour and 2.1 km of real-world robot traversal. GlassGuard achieves 85% of total glass coverage for its panoramic version. Under identical pinhole inputs, GlassGuard achieves 82% total coverage, compared with at most 61% for the evaluated baselines, while producing 5-17x fewer false voxels per frame. Qualitative examples with a navigation planner illustrate the reconstructed planes blocking paths through glass while leaving traversable routes open. The project page is available at https://glassguardproject.github.io/.

</details>

#### 2026-10-01 - From Reasoning Failures to Composable Video Spatial Intelligence

**Authors:** Pengzhan Sun, Junbin Xiao, Ramanathan Rajaraman, Shiu-hong Kao, Angela Yao
**Links:** [abs](https://arxiv.org/abs/2610.01999) - [pdf](https://arxiv.org/pdf/2610.01999)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Reasoning Failures to Composable Video Spatial Intelligence
- 作者：Pengzhan Sun, Junbin Xiao, Ramanathan Rajaraman, Shiu-hong Kao, Angela Yao
- 出版日期：2026-10-01T16:31:19Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.01999 ；PDF https://arxiv.org/pdf/2610.01999

### 一句话总结
论文通过统一模式与坐标约定对比预测和真实空间上下文，将视频空间推理失败拆解为四类可诊断错误，并提出免训练的 CROSS 几何算子与空间技能库来显式处理空间约定，从而在多个基准上提升视觉语言模型的空间推理表现。

### 研究问题
论文关注的问题是：现有的空间推理基准虽然评估视觉语言模型在多种任务上的表现，但任务级分数无法揭示成功或失败背后的底层能力差异。作者认为每个任务都需要恢复空间证据、表示几何并进行推理，因此需要将空间推理能力解耦，诊断具体错误来源，并在此基础上修复系统性推理失败。

### 核心思路/方法
论文将空间推理拆解为若干底层能力：恢复空间证据、表示几何、以及在其上进行推理。作者通过在一个共享模式和坐标契约下比较预测的空间上下文与真实空间上下文，对失败进行诊断。该比较揭示出四类反复出现的错误来源：感知不准确、空间上下文信息缺失、选择错误的测量方式、以及参考系错误或位置与方向跟踪错误。

基于这一诊断，作者提出 CROSS，一个免训练的类型化几何算子与空间技能库。该库在可用证据上运行，以支持可靠的视频空间推理。CROSS 可以为非编程视觉语言模型提供经过验证的上下文，或为 SpatialClaw 智能体提供可调用的技能。论文在五个基准上评估 CROSS，摘要提到其在 ReVSI 上将平均分从 55.9% 提升至 60.2%，并将 DSI-Bench 上的 SpatialClaw 结果从 62.8% 提升至 66.3%。作者据此说明，显式处理空间约定可以在不额外训练的情况下修复系统性推理失败。

### 主要贡献
- 提出一种诊断视角：通过共享模式和坐标契约，对比预测与真实空间上下文，将视频空间推理失败归因于四类可复现错误来源。
- 提出 CROSS：一个免训练的、可组合的类型化几何算子与空间技能库，用于在可用证据上支持可靠的视频空间推理。
- 展示 CROSS 的两种使用方式：为非编程视觉语言模型提供经过验证的上下文，或为 SpatialClaw 智能体提供可调用技能。
- 在五个基准上进行评估，并报告在 ReVSI 和 DSI-Bench 上的具体提升，证明显式处理空间约定可修复系统性推理失败且无需额外训练。

### 局限性
摘要未提供足够信息说明 CROSS 的具体实现细节、算子覆盖范围、计算开销、失败案例、基准之外的泛化能力，以及四类错误来源之间的相互影响。摘要也未提供五个基准的完整名称与全部结果，仅报告了 ReVSI 和 DSI-Bench 上的部分数值。此外，摘要未说明该方法的适用边界或对输入证据质量的依赖程度。

### 阅读优先级
高。理由：论文针对视频空间推理中任务级评分无法解释失败原因的问题，提出可诊断的错误分类和免训练的可组合几何算子库，并在多个基准上报告一致提升。对于关注视觉语言模型空间推理、具身智能、机器人及 AR 应用的研究者而言，该工作提供了从失败诊断到可复用技能修复的明确路径，且不依赖额外训练，具有较强的实用性和可扩展性。

</details>

<details>
<summary>Abstract</summary>

Spatial reasoning benchmarks evaluate vision-language models across diverse tasks, but task-level scores do not reveal which underlying capabilities account for success or failure. Each task requires recovering spatial evidence, representing geometry, and reasoning over it. We disentangle these capabilities by comparing predicted and ground-truth spatial context under a shared schema and coordinate contract. This comparison reveals four recurring sources of error: inaccurate perception, missing information in the spatial context, selection of the wrong measurement, and errors in reference frames or in tracking position and orientation. Guided by this diagnosis, we develop CROSS, a training-free library of typed geometric operators and spatial skills that function over available evidence to support reliable video spatial reasoning. The resulting library supplies verified context to non-coding VLMs or callable skills to a SpatialClaw agent. We evaluate \methodname{} on five benchmarks. \methodname{} raises the average score from 55.9\% to 60.2\% on ReVSI and improves the SpatialClaw result from 62.8\% to 66.3\% on DSI-Bench. These gains demonstrate that explicit handling of spatial conventions can repair systematic reasoning failures without additional training.

</details>

#### 2026-10-01 - TouchTherm: Building Multimodal Digital Twins of Objects for Tactile and Thermal Rendering

**Authors:** Yitao Zhang, Hong Ying, Haoran Guo, Xiaoying Zhou, Guanyu Chen, Chenxi Xiao
**Links:** [abs](https://arxiv.org/abs/2610.01943) - [pdf](https://arxiv.org/pdf/2610.01943)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** rendering, VR, virtual reality, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TouchTherm: Building Multimodal Digital Twins of Objects for Tactile and Thermal Rendering
- 作者：Yitao Zhang, Hong Ying, Haoran Guo, Xiaoying Zhou, Guanyu Chen, Chenxi Xiao
- 出版日期：2026-10-01T16:10:08Z
- 分类：primary_category: Embodied / Robotics / AR Applications；secondary_categories: Neural Scene Representations & Rendering
- 链接：abstract_url: https://arxiv.org/abs/2610.01943；pdf_url: https://arxiv.org/pdf/2610.01943

### 一句话总结
TouchTherm 提出一个从真实物体构建可用于仿真的视觉—触觉—热觉多模态数字孪生资产的框架，以同时支持光学触觉渲染和随时间变化的温度反馈。

### 研究问题
机器人仿真和虚拟现实不仅需要物体的视觉几何与外观，还需要能够反映触觉与热觉交互的物理线索。现有 3D 数据集和重建方法主要表示物体尺度的几何与视觉外观，忽视了用于高保真触觉渲染的微观表面结构，以及用于温度感知交互的瞬态温度动态。因此，论文关注如何从真实物体构建同时具备视觉、触觉和热觉信息的仿真就绪资产。

### 核心思路/方法
论文提出 TouchTherm 框架，用于从真实世界物体构建仿真就绪的视觉—触觉—热觉物体资产。

在视觉与触觉重建方面，方法结合结构光扫描与从光度立体获得的多视角法线图。法线图被配准到扫描几何上，并转换到切线空间，以恢复用于光学触觉渲染的局部微观高度场；粗网格则用于碰撞检测。

在热觉重建方面，方法在受控加热后捕获自然冷却过程的同步多视角红外视频，并重建物理正则化的动态热场。

### 主要贡献
- 提出 TouchTherm 框架，从真实物体构建仿真就绪的视觉—触觉—热觉物体资产。
- 在视觉与触觉重建中，结合结构光扫描和光度立体的多视角法线图，将法线图配准到扫描几何并转换到切线空间，以恢复局部微观高度场，同时使用粗网格进行碰撞检测。
- 在热觉重建中，捕获受控加热后自然冷却的同步多视角红外视频，并重建物理正则化的动态热场。
- 在 20 个物体上的实验表明，重建的微观高度场保留主要表面结构，并恢复粗几何之外更高频的细节；热场在 30 秒和 45 秒时的留出表面温度 MAE 分别为 0.465 摄氏度和 0.592 摄氏度。
- 生成的触觉资产支持从触觉观测进行合成到真实的物体识别；基于手套的 VR 系统展示了空间和时间上变化的温度反馈。

### 局限性
摘要未提供足够信息。摘要未说明该方法在更广泛物体类别、复杂材质、不同环境条件或实时性能方面的限制，也未提供失败案例或与其他方法的完整定量比较。

### 阅读优先级
中。理由：该论文面向机器人仿真与 VR 中的多模态数字孪生，结合视觉、触觉和热觉重建，任务方向明确，并给出了 20 个物体上的热场 MAE 与触觉识别、VR 温度反馈演示；但摘要未提供足够信息来判断其方法细节、泛化能力、实时性和完整实验对比，因此对需要多模态物体资产或触觉/热觉仿真的读者具有一定价值，但优先级不宜直接判为最高。

</details>

<details>
<summary>Abstract</summary>

Robotic simulation and virtual reality increasingly require object assets that capture not only visual geometry but also the physical cues underlying tactile and thermal interaction. Existing 3D datasets and reconstruction methods primarily represent object-scale geometry and visual appearance, overlooking microscale surface structure for high-fidelity haptic rendering and transient temperature dynamics for temperature-aware interaction. We present TouchTherm, a framework for constructing simulation-ready visuo-tactile-thermal object assets from real-world objects. For visual and tactile reconstruction, we combine structured-light scanning with multiview normal maps obtained from photometric stereo. The normal maps are registered to the scanned geometry and transformed into tangent space to recover local micro-height fields for optical tactile rendering, while the coarse mesh handles collision detection. For thermal reconstruction, we capture synchronized multiview infrared videos of natural cooling following controlled heating and reconstruct a physics-regularized dynamic thermal field. Experiments on 20 objects show that the reconstructed micro-height fields preserve dominant surface structures and recover higher-frequency details beyond the coarse geometry, while the thermal fields achieve held-out surface-temperature MAEs of 0.465 degrees C and 0.592 degrees C at 30 s and 45 s, respectively. The resulting tactile assets support synthetic-to-real object recognition from tactile observations, while a glove-based VR system demonstrates spatially and temporally varying thermal feedback. These results highlight the potential of TouchTherm for multimodal sensory simulation and temperature-aware virtual interaction.

</details>

#### 2026-10-01 - Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models

**Authors:** Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis
**Links:** [abs](https://arxiv.org/abs/2610.01942) - [pdf](https://arxiv.org/pdf/2610.01942)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models
- 作者：Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis
- 出版日期：2026-10-01T16:09:34Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.01942) / [PDF](https://arxiv.org/pdf/2610.01942)

### 一句话总结
提出 Latent-Foresight，一个端到端联合学习潜在分词器与基于流的生成式动态模型的框架，显式塑造具备时间可预测性的潜在表示，以替代传统两阶段流水线。

### 研究问题
论文关注场景未来演化的预测这一世界建模的基础能力。现有工作虽已表明在视觉基础模型（VFM）的特征空间中操作可得到语义丰富的表示，但存在解耦问题：两阶段流水线先用固定降维（如 PCA）或独立训练的自编码器压缩 VFM 特征，再在冻结的潜在空间上训练单独的预测器；而直接在原始 VFM 特征上施加预测器的方法，也无法保证潜在空间是为可预测动态而组织的。

### 核心思路/方法
提出 Latent-Foresight 端到端框架，联合学习一个潜在分词器（latent tokenizer）和一个基于流的生成式动态模型，从而显式地将表示塑造成支持时间可预测性的形式。为实现稳定的联合优化，作者引入若干关键设计选择，以防止潜在坍塌（latent collapse），并使重建目标与生成目标对齐。

### 主要贡献
- 提出端到端框架 Latent-Foresight，联合学习潜在分词器与基于流的生成式动态模型，显式塑造可预测的潜在表示。
- 引入防止潜在坍塌、对齐重建与生成目标的关键设计，以支持稳定的联合优化。
- 据摘要所述，实验表明该方法学到的时间一致潜在表示更优，在多个未来场景理解任务和预测时间范围上持续优于两阶段基线，同时消除了分离的训练阶段（包括在高分辨率适配时）。
- 提供了实现代码与模型权重。

### 局限性
摘要未提供足够信息。例如未给出具体任务、数据集、评价指标、计算开销、失败案例或设计选择的具体细节，均无法从摘要判断。

### 阅读优先级
中。理由：该工作针对潜在世界模型表示学习与动态预测解耦这一明确问题，提出端到端方案且声称在多项任务上持续优于两阶段基线，思路有参考价值；但摘要未提供实验细节与定量结果，若关注世界模型或具身/机器人方向的表示学习，可进一步阅读原文验证；若仅需概览，可暂缓。

</details>

<details>
<summary>Abstract</summary>

Predicting the future evolution of a scene is a fundamental capability for world modeling. Recent work has shown that operating in the feature space of Vision Foundation Models (VFMs) yields semantically rich representations that support diverse future scene understanding tasks. However, existing approaches rely on two-stage pipelines, where VFM features are first compressed using fixed dimensionality reduction (e.g., PCA) or independently trained autoencoders, and a separate predictor is trained on top of the resulting frozen latent space. This decoupling between representation learning and temporal prediction, as well as approaches that apply predictors directly on raw VFM features, provides no guarantee that the latent space is structured for predictable dynamics. In this work, we propose Latent-Foresight, an end-to-end framework that jointly learns a latent tokenizer and a flow-based generative dynamics model, explicitly shaping the representation to support temporal predictability. To enable stable joint optimization, we introduce several key design choices that prevent latent collapse and align reconstruction with generative objectives. Extensive experiments show that our approach learns more temporally coherent latent representations and consistently outperforms two-stage baselines across multiple future scene understanding tasks and prediction horizons, while eliminating separate training stages, including during high-resolution adaptation. We provide the implementation code and model weights at https://github.com/Sta8is/Latent-Foresight

</details>

#### 2026-10-01 - FlashDexRetarget: Accelerating Dexterous Manipulation Data Generation through Multi-Motion Retargeting

**Authors:** Kyungmin Lee, Sibeen Kim, Dongyoon Hwang, Yoonsang Oh, Donghu Kim, Youngdo Lee, I Made Aswin Nahrendra, Jaegul Choo, Hojoon Lee
**Links:** [abs](https://arxiv.org/abs/2610.01849) - [pdf](https://arxiv.org/pdf/2610.01849)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FlashDexRetarget: Accelerating Dexterous Manipulation Data Generation through Multi-Motion Retargeting
- 作者：Kyungmin Lee, Sibeen Kim, Dongyoon Hwang, Yoonsang Oh, Donghu Kim, Youngdo Lee, I Made Aswin Nahrendra, Jaegul Choo, Hojoon Lee
- 出版日期：2026-10-01T15:15:42Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.01849

### 一句话总结
FlashDexRetarget 是一个基于强化学习的灵巧操作运动重定向框架，旨在提高人-物演示向机器人本体迁移的成功率与训练效率。

### 研究问题
人类手-物演示可作为可复用的灵巧机器人操作数据来源，但跨本体迁移需要物理可行的重定向。现有基于物理的方法在重定向成功率与特定运动的训练效率方面存在局限，或两者兼有。论文旨在解决高成功率与高效率难以兼顾的问题。

### 核心思路/方法
- 提出 FlashDexRetarget，一个基于 RL 的灵巧运动重定向框架。
- 为便于学习演示交互，结合物体点云观测、手-物距离特征、未来轨迹编码，并配合互补奖励来监督物体运动与参考手-物关系。
- 为加速学习，采用分离的左手和右手 actor-critic 网络，并将 off-policy 算法 FlashSAC 适配到灵巧运动跟踪任务。
- 在涵盖单物体与双物体交互的 50 个运动基准上进行评估；并在 200、500、1000 个运动规模下测试扩展性。

### 主要贡献
- 提出 FlashDexRetarget，用于高成功率、高效的灵巧运动重定向。
- 在 50 运动基准上达到 90% 成功率，约为所评估的基于采样基线的 2.5 倍，同时训练计算量比所评估的基于 RL 的基线最多少 100 倍。
- 在 XHand 与 Sharpa Wave Hand 上评估显示一致增益，并通过组件级消融考察各设计选择的贡献。
- 在 200、500、1000 运动规模下验证方法在大规模下仍保持稳定，并随训练集增长更高效地产生成功重定向运动。
- 使用真实世界采集演示的定性回放结果展示框架对录制人类操作的适用性。

### 局限性
- 摘要未提供足够信息关于失败案例、未覆盖的运动类型或具体计算资源规模。
- 摘要未提供足够信息关于真实机器人部署的定量结果与安全性评估。
- 摘要未提供足够信息关于方法对演示质量、物体类别或传感器噪声的敏感性分析。
- 摘要未提供足够信息关于与更多近期方法的完整对比范围。

### 阅读优先级
高。理由：该工作直接针对灵巧操作数据生成中的成功率与训练效率瓶颈，报告了显著的量化提升与大规模扩展验证，且涉及多本体一致性与真实演示回放，对具身智能与机器人操作数据生成方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Human hand-object demonstrations offer a reusable source of dexterous robot manipulation data, but transferring them across embodiments requires physically feasible retargeting. Existing physics-based approaches face limitations in retargeting success, motion-specific training efficiency, or both. To address these limitations, we introduce FlashDexRetarget, an RL-based framework for high-success, efficient dexterous motion retargeting. To make the demonstrated interaction easier to learn, we combine object point-cloud observations, hand-object distance features, and future trajectory encodings with complementary rewards that supervise object motion and reference hand-object relationships. To further accelerate learning, we employ separate left- and right-hand actor critic networks and adapt the off-policy algorithm, FlashSAC to dexterous motion tracking. On a benchmark of 50 motions spanning single-object and two-object interactions, FlashDexRetarget achieves a 90% success rate, approximately 2.5x that of the evaluated sampling-based baselines, while requiring up to 100x less training compute than the evaluated RL-based baselines. Evaluations on both XHand and Sharpa Wave Hand show consistent gains, and component-wise ablations examine the contributions of our design choices. Beyond the 50-motion benchmark, experiments with 200, 500, and 1,000 motions demonstrate that our method remains stable at larger scales and produces successful retargeted motions more efficiently as the training set grows. Qualitative replay results using real-world-captured demonstrations further illustrate the applicability of our framework to recorded human manipulation. Videos and code are available at https://davian-robotics.github.io/FlashDexRetarget/

</details>

#### 2026-10-01 - GIFTBench: Diagnosing Generalization in Image Forgery Localization and Informing Model Design

**Authors:** Baoke Dou, Ziye Wang, Hao Wang, Guoqing Cai, Wende Tan, Chenyang Si, Liucheng Guo, Yueming Lyu
**Links:** [abs](https://arxiv.org/abs/2610.01778) - [pdf](https://arxiv.org/pdf/2610.01778)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GIFTBench: Diagnosing Generalization in Image Forgery Localization and Informing Model Design
- 作者：Baoke Dou, Ziye Wang, Hao Wang, Guoqing Cai, Wende Tan, Chenyang Si, Liucheng Guo, Yueming Lyu
- 出版日期：2026-10-01T14:31:20Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次要分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.01778 ；PDF https://arxiv.org/pdf/2610.01778 ；数据集展示页 https://giftbench-preview.doudoudouya337.chatgpt.site

### 一句话总结
论文提出多轴图像伪造定位基准 GIFTBench，用于诊断模型在多种分布变化下的泛化能力，并基于诊断结果设计改进框架 ForenScope，同时将基准作为训练资源以提升跨域定位表现。

### 研究问题
现有图像伪造定位（IFL）评测基准常覆盖有限的篡改条件，或在跨数据集评测中混合多个因素，导致聚合性能无法完整反映模型在分布变化下的定位泛化能力。论文关注如何更可靠地评估 IFL 模型在多种变化条件下的泛化表现，并将诊断结果用于指导模型设计。

### 核心思路/方法
论文提出 GIFTBench，一个包含 115,013 张篡改图像、具有像素级标注的多轴基准，覆盖篡改来源、语义目标、编辑操作和组合复杂度四个维度，并支持轴特定迁移分析与在十二个外部数据集上的评测。基于该基准的诊断研究揭示了三类现象：跨来源迁移存在不对称性、失败以召回为主导、以及在语义/操作/组合变化下退化程度异质。除评测外，GIFTBench 的规模与多样性提供了比传统 IFL 数据集更广的训练分布，用于训练代表性定位器可提升对外部数据集的聚合迁移表现。受诊断发现指导，论文进一步提出 ForenScope，一个结合分类适配表示、多深度多尺度空间特征、学习式层融合以及选择性粗尺度条件化的检测与定位框架。

### 主要贡献
1. 提出 GIFTBench，一个覆盖多个篡改维度、包含 115,013 张像素级标注篡改图像的多轴 IFL 基准，支持轴特定迁移分析和十二个外部数据集评测。
2. 通过诊断研究揭示 IFL 泛化中的关键失败模式：跨来源迁移不对称、召回主导的失败、以及在不同语义/操作/组合变化下的异质退化。
3. 证明 GIFTBench 不仅可作为评测工具，也可作为有效训练资源：在其上训练代表性定位器能一致提升对外部数据集的聚合迁移表现。
4. 基于诊断发现提出 ForenScope 框架，融合分类适配表示、多深度多尺度空间特征、学习式层融合和选择性粗尺度条件化，在提升跨数据集定位的同时保留图像级检测能力。

### 局限性
摘要未提供足够信息。摘要中未说明 GIFTBench 的构建成本、标注一致性、潜在偏差、覆盖盲区，也未给出 ForenScope 的具体计算开销、失败案例或与现有方法的完整定量对比。论文所述“十二个外部数据集”的具体名称与评测协议细节，摘要未提供足够信息。分类标注为 Embodied / Robotics / AR Applications 与图像伪造定位主题之间的关系，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作同时涉及基准构建、泛化诊断和模型设计，对图像伪造定位与跨域泛化评测方向有直接参考价值；但摘要未提供具体实验数值、对比方法细节和局限性讨论，若需判断其相对现有基准的实际优势，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Reliable evaluation of image forgery localization (IFL) requires assessing models under diverse distribution changes, yet existing benchmarks often cover limited manipulation conditions or entangle multiple factors in cross-dataset evaluation. Consequently, aggregate performance provides an incomplete view of localization generalization. We introduce GIFTBench, a multi-axis benchmark of 115,013 manipulated images with pixel-level annotations spanning manipulation source, semantic target, editing operation, and composition complexity. GIFTBench supports axis-specific transfer analysis and evaluation on twelve external datasets. Its diagnostic studies reveal asymmetric cross-source transfer, recall-dominated failures, and heterogeneous degradation across semantic, operational, and compositional changes. Beyond diagnosis, the scale and diversity of GIFTBench provide a substantially broader training distribution than conventional IFL datasets. Training representative localizers on GIFTBench consistently improves their aggregate transfer to external datasets, showing that the benchmark serves not only as an evaluation tool but also as an effective training resource for cross-domain localization. Guided by the diagnostic findings, we further develop ForenScope, a detection and localization framework combining classification-adapted representations with multi-depth, multi-scale spatial features, learned layer fusion, and selective coarse-scale conditioning. Experiments show improved cross-dataset localization while retaining image-level detection capability. The GIFTBench dataset showcase page is available at https://giftbench-preview.doudoudouya337.chatgpt.site.

</details>

#### 2026-10-01 - EIDA: Execution-Interface Dynamics Adaptation for Real-to-Sim-to-Real Robot Navigation

**Authors:** Yiwei Qian, Shanze Wang, Qingyuan Hu, Xinming Zhang, Wei Zhang
**Links:** [abs](https://arxiv.org/abs/2610.01219) - [pdf](https://arxiv.org/pdf/2610.01219)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EIDA: Execution-Interface Dynamics Adaptation for Real-to-Sim-to-Real Robot Navigation
- 作者：Yiwei Qian, Shanze Wang, Qingyuan Hu, Xinming Zhang, Wei Zhang
- 出版日期：2026-10-01T07:24:32Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.01219 ；PDF：https://arxiv.org/pdf/2610.01219

### 一句话总结
EIDA 通过用目标平台执行数据拟合“执行接口”层面的动力学响应，并在轻量 GPU 并行仿真器中使用这些拟合模型，以改善真实到仿真再到真实的机器人导航迁移。

### 研究问题
仿真到机器人迁移可能失败，因为速度指令产生的运动与反馈不同于策略训练时建模的情况。论文关注的问题是如何在不重建执行器动力学的情况下，适配这种执行接口层面的差异，从而提升导航策略的迁移效果。

### 核心思路/方法
EIDA 不重建执行器动力学，而是从目标平台执行数据中拟合速度指令对应的响应。具体包括：一个模型预测机体坐标系下的位姿增量，用于更新仿真器几何；另一个单独模型预测策略所观察到的速度反馈；策略输入中包含一小段速度反馈历史。拟合后的模型被用于一个轻量级 GPU 并行仿真器中。

### 主要贡献
- 提出执行接口动力学适配方法 EIDA，用目标平台执行数据拟合速度指令响应，而不重建执行器动力学。
- 分别建模机体坐标系位姿增量以更新仿真器几何，以及策略面对的速度反馈预测，并将速度反馈短历史加入策略输入。
- 在 Jackal 和 Go2 完整验证集上，拟合模型相对仿真器预定义运动模型降低了位置和偏航预测误差。
- 在 100 个基准导航环境中、于独立物理仿真器评估时，EIDA 在有和没有全局引导的情况下均取得相比对比学习策略最高的成功率和导航分数。
- 反馈消融进一步支持匹配策略面对的速度估计的必要性。
- 在物理 Unitree Go2 上，EIDA 在全部 20 次静态场景试验中无碰撞到达目标，而基线为 20 次中 4 次。

### 局限性
摘要未提供足够信息。摘要未说明方法在动态场景、不同平台泛化、计算开销、失败案例或更广泛真实环境中的表现与限制。

### 阅读优先级
高。理由：论文直接针对 real-to-sim-to-real 机器人导航中的执行接口动力学适配问题，并同时给出仿真基准与物理机器人验证结果，且摘要报告了较明显的迁移性能提升，对机器人导航与仿真迁移方向具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Simulation-to-robot transfer can fail when velocity commands produce motion and feedback that differ from those modeled during policy training. We present execution-interface dynamics adaptation (EIDA), which fits these responses from target-platform execution data without reconstructing actuator dynamics. A model of body-frame pose increments updates simulator geometry, while a separate model predicts the velocity feedback observed by the policy; a short history of velocity feedback is included in the policy input. The fitted models are used within a lightweight GPU-parallel simulator. On the full Jackal and Go2 validation sets, the fitted models reduced position and yaw prediction errors relative to the simulator's predefined motion model. Across 100 benchmark navigation environments evaluated in a separate physics-based simulator, EIDA achieved the highest success rate and navigation score among the compared learned policies, both with and without global guidance. Feedback ablations further supported the need to match policy-facing velocity estimates. On a physical Unitree Go2, EIDA reached the goal without collision in all 20 static-scene trials, compared with 4 of 20 for the baseline. These results show that execution-interface adaptation can improve navigation transfer without detailed actuator simulation.

</details>

### 2026-09

#### 2026-09-30 - Harnessing Vision-Language Models for Perceptual Quality Assessment and Autonomous Content Adjustment in Augmented Reality

**Authors:** Elias Rotondo, Lin Duan, Yanming Xiu, Sangjun Eom, Conrad Li, Maria Gorlatova
**Links:** [abs](https://arxiv.org/abs/2610.00677) - [pdf](https://arxiv.org/pdf/2610.00677)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Harnessing Vision-Language Models for Perceptual Quality Assessment and Autonomous Content Adjustment in Augmented Reality
- 作者：Elias Rotondo, Lin Duan, Yanming Xiu, Sangjun Eom, Conrad Li, Maria Gorlatova
- 出版日期：2026-09-30T20:13:50Z
- 分类：主分类为 Embodied / Robotics / AR Applications；未提供次级分类
- 链接：[摘要](https://arxiv.org/abs/2610.00677)｜[PDF](https://arxiv.org/pdf/2610.00677)

### 一句话总结
论文提出一个基于视觉语言模型（VLM）的增强现实（AR）内容自动评估与调整框架，并构建 RateAR 基准，验证 VLM 质量预测与人类主观判断的相关性，进而实现自动化 AR 内容调整。

### 研究问题
AR 头戴显示设备面临场景几何受限、空间抖动和时间不稳定等问题，影响终端用户的沉浸感与舒适度。用户研究是 AR 视觉质量评估的标准方法，但其成本高、可扩展性下降且灵活性不足，成为迭代应用设计中的瓶颈。因此，论文关注如何用自动化方法评估和预测用户感知的 AR 场景视觉保真度，并进一步自动调整 AR 内容。

### 核心思路/方法
论文提出一个基于视觉语言模型的自动化 AR 内容评估与优化框架，用于评估和预测用户感知的 AR 场景视觉保真度。首先构建 RateAR 基准，包含在多样场景和环境条件下采集的 AR 图像与视频，并在对象放置、尺度、阴影一致性等感知因素上具有良好到优秀的可靠性（ICC(2,5) >= .90）。随后在 RateAR 上评估十一个商业 VLM，考察其质量预测与人类主观判断的相关性。论文还进行了消融研究，比较不同提示策略，指出上下文提示（contextual prompting）相比其他策略能更好地与人类评分对齐，同时平衡引入的复杂度线索。基于上述发现，论文构建了自动化 AR 内容调整系统，并开展了 21 名参与者参与的用户研究。

### 主要贡献
- 提出 RateAR 基准，涵盖多样场景与环境条件下的 AR 图像和视频，并针对对象放置、尺度、阴影一致性等感知因素报告了良好到优秀的可靠性（ICC(2,5) >= .90）。
- 在 RateAR 上评估十一个商业 VLM，结果表明基于 VLM 的质量预测与人类主观判断强相关，Spearman 秩相关最高达 0.8695。
- 通过消融研究显示，与其他提示策略相比，上下文提示在更好对齐人类评分的同时平衡了引入的复杂度线索。
- 构建自动化 AR 内容调整系统，并通过 21 名参与者的用户研究验证效果，超过 90% 的参与者认为系统改善了虚拟内容的放置和尺寸一致性。

### 局限性
摘要未提供足够信息。摘要未说明 RateAR 的规模、场景覆盖范围的具体边界、十一个商业 VLM 的具体名称、消融实验中各提示策略的详细设置、自动化调整系统的技术细节、用户研究的完整实验设计与统计细节，以及该方法在更广泛 AR 设备或任务上的泛化能力。上述内容均无法仅凭摘要确定。

### 阅读优先级
中。理由：该论文聚焦 AR 视觉质量评估与自动内容调整，将 VLM 用于感知质量预测并构建基准和用户研究，对 AR 应用、人机交互和视觉语言模型评估方向有参考价值；但摘要未提供足够信息说明具体方法细节、基准规模和系统实现，若读者关注可复现实验或具体技术方案，需要进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Advancements in augmented reality (AR) continue to foster innovative solutions, facilitating novel methodologies within educational systems, healthcare delivery, and risk-mitigation protocols. However, optimizing for end-user immersion and comfort remains challenging, as AR head-mounted displays contend with constrained scene geometry, spatial jitter, and temporal instability. User studies are the standard AR evaluation method for visual quality, but their cost, diminishing scalability, and inflexibility pose bottlenecks during iterative application design. To address this problem, we present an automated framework for AR content evaluation and refinement, built on vision-language models (VLMs), to evaluate and predict the visual fidelity of AR scenes as perceived by users. First, we introduce RateAR, a benchmark of AR images and videos collected across diverse scenes and environmental conditions, with good-to-excellent reliability (ICC(2,5) >= .90) across perceptual factors, including object placement, scale, and shadow consistency. Subsequently, we evaluate eleven commercial VLMs on the crafted benchmark. Results support that VLM-based quality predictions strongly correlate with human subjective judgments, achieving Spearman's rank-order correlations of up to 0.8695. An ablation study further suggests that, compared to other prompting strategies, our contextual prompting yields better alignment with human ratings while balancing introduced complexity cues. Building on these findings, we construct an automated AR content adjustment system and conduct a 21-participant user study. More than 90% of participants found that the system improved placement and size coherence of virtual content.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
