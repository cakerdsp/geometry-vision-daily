# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：40
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 12
  - Embodied / Robotics / AR Applications: 12
  - Neural Scene Representations & Rendering: 11
  - Geometry Foundation Models: 4
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **3D Gaussian Splatting 从“渲染”走向“系统级底座”**
   今日多篇论文不再把 3DGS 仅当作新视角合成工具，而是作为更上层系统的基础设施：ORCA 用 Gaussian-anchor 承载单图可探索场景，PanoGS-SLAM 把 3DGS 做成全景稠密 SLAM，BRAVE-6D 与 Neverwhere 则用 3DGS 视图合成构建机器人基准与闭环评测环境，Bi-FlowGS 用光流连接生成式补全与高斯几何正则。技术重心从“渲染质量”转向“几何正确性、可扩展性、系统可用性”。

2. **稀疏/欠约束重建中的“生成 vs 几何”边界被重新划定**
   ORCA 明确主张：小范围去遮挡优先用已有 RGB-D 修复，生成式修补只留给无法恢复的大区域；Bi-FlowGS 则指出稀疏视图下“渲染合理但几何错误”的 Geometry Cheating，并用双向光流把生成视频的时间先验转成几何监督。这两篇共同反映一个趋势：不再无条件信任生成先验，而是按缺失结构的大小、置信度和几何可约束性做分层处理。

3. **评测与基准成为独立且紧迫的研究贡献**
   BRAVE-6D 针对机器人主动视觉 6DOF 位姿估计，Neverwhere 针对视觉运动控制器的闭环评估，Monaco4D 针对高速户外 4D 重建，NeuroSymbEAD 针对自动驾驶场景的神经符号描述，还有面向作物表型与 LiDAR 仿真保真度的评测工作。多篇论文的核心贡献不是新模型，而是“可复现、可比较、缩小训练/评估差距”的场景与指标，说明该领域正从单点方法竞赛转向系统级验证。

4. **机器人/具身智能与重建、位姿、风险建模深度耦合**
   ProxiDex 用接近度动态替代触觉硬件依赖，UniDex-ViTac 用人类视频引导仿真生成视触觉策略，CueNav 用 BEV 与本体可见性引导视频规划并由 IDM 翻译为动作，CorrRisk-WM 把候选轨迹走廊与风险世界模型耦合，SWIM 面向软体机器人全身操作。重建与位姿估计不再只是感知前端，而是直接嵌入策略学习、风险评估和闭环控制。

5. **几何基础模型开始面对“可扩展配准”与“类别先验显式化”**
   G3AR 用图像邻近图与分块图最大生成树处理数千张航空多序列图像的稠密神经几何配准；PriorPose 则批评无先验方法把规范化坐标系隐式记在权重里、有先验方法串行“先变形后对齐”导致误差级联，转而联合求解规范化与对齐。两者分别从规模扩展和先验使用方式两个方向推进几何基础模型。

#### 技术路线观察

- **几何基础模型**：G3AR 走“图引导分块 + Sim(3) 注册”的可扩展路线，强调全上下文不可行时的分治与拓扑对齐；PriorPose 走“参考引导对应 + 显式类别先验 + 联合优化”路线。共同点是都在反思“端到端隐式记忆”的泛化代价，转向显式结构约束。
- **3D/4D 重建**：FastFlowGS 与 Monaco4D 聚焦稀疏固定外部相机下的高速动态主体流式 4D 重建，填补“户外 + 快速运动 + 流式 + 非自车视角”的空白；Bi-FlowGS 与 ORCA 聚焦稀疏/单视图下的几何补全与去遮挡；作物表型与文化遗产两篇则把重建流程推向领域落地与评估。
- **神经场景表示与渲染**：3DGS 仍是主流表示，但改进点明显集中在几何一致性（Bi-FlowGS 的光流双向约束、ORCA 的深度锚点）、球面域渲染（PanoGS-SLAM）、以及作为仿真与基准环境（BRAVE-6D、Neverwhere）。纯渲染质量竞赛的论文在今日列表中占比很低。
- **机器人/AR 应用**：路线分化明显。一路是策略学习（ProxiDex、UniDex-ViTac、SWIM、CueNav），强调从人类视频、接近度、视觉线索中提取可执行动作；一路是评测与安全（BRAVE-6D、Neverwhere、CorrRisk-WM），强调闭环、可复现和风险量化；还有一路是自感知硬件（模块化连续体机器人），试图减少对外部追踪与触觉硬件的依赖。
- **语义与语言接地**：HuMemSLAM 把语义地点识别集成进 ORB-SLAM3，NeuroSymbEAD 构建以自车为中心的知识图谱与多层级描述，CueNav 用 BEV 传递全局任务上下文。语言与语义正在从“附加标签”变为规划与定位的输入条件。

#### 值得优先阅读的论文

1. **Bi-FlowGS（2609.17039）**
   直接命中稀疏视图 3DGS 的核心失败模式“Geometry Cheating”，并提出 V2G 与 G2V 双向光流协同。若你在做稀疏重建或生成先验与几何正则的结合，这是今日方法论最完整的一篇。

2. **ORCA（2609.17450）**
   对“生成式补全该用到什么程度”给出了清晰的分层原则：小缺失用 RGB-D 修复，大缺失才生成。这一设计哲学可能影响后续单图/少视图可探索场景的补全策略。

3. **FastFlowGS / Monaco4D（2609.16310）**
   同时提出方法与基准，瞄准“稀疏固定外部相机 + 高速运动 + 流式”这一此前无人覆盖的场景。对做 4D 重建、体育/赛事数字化或流式重建的人优先级很高。

4. **G3AR（2609.16603）**
   几何基础模型的可扩展配准问题会随着航空、城市级采集越来越重要。图引导分块与 Sim(3) 注册的路线具有工程可复现性，适合关注大规模神经几何落地的人。

5. **PanoGS-SLAM（2609.17387）**
   首个基于 3DGS 的全景稠密 SLAM，把可微渲染与位姿优化放到球面域，并用球面一致光度损失处理等距柱状投影畸变。对 SLAM 与全景感知交叉方向有参考价值。

#### 可能的研究机会

- **分层式补全策略的通用化**：ORCA 按缺失区域大小与结构分流，这一思想可迁移到稀疏视图 3DGS、4D 重建和 SLAM 建图中。可研究如何自动判定“哪些缺失可由几何修复、哪些必须生成”，并给出置信度估计。
- **生成先验的几何监督化**：Bi-FlowGS 用光流把视频生成的时间对应转成几何监督。可进一步探索其他生成先验（深度、法线、分割、动态掩码）如何转成显式几何约束，减少对 RGB 伪监督的依赖。
- **3DGS 作为机器人闭环评测基础设施**：BRAVE-6D 与 Neverwhere 分别用于位姿估计和视觉运动控制。可研究如何统一这些 3DGS 基准的场景格式、任务接口与失败模式标注，形成跨任务的可复现评测层。
- **稀疏外部相机下的流式 4D 重建与下游任务耦合**：FastFlowGS 目前聚焦重建，若把重建结果接入 CueNav 类视频规划或 CorrRisk-WM 类风险建模，可探索“重建—预测—规划”的端到端实时管线。
- **类别先验的显式表示与联合优化**：PriorPose 主张先验显式化并联合求解规范化与对齐。可研究该思路在部件级、关节物体、可变形物体位姿估计上的扩展，以及先验失效时的回退机制。
- **具身策略中的接触/接近度表示统一**：ProxiDex 用接近度替代触觉，UniDex-ViT

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-16T12:51:30-04:00
**Total number of papers:** 40
**Number of papers added in the latest update:** 31
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

### 2026-09

#### 2026-09-15 - G3AR: Graph-Guided Neural Visual Geometry for Scalable Multi-Sequence Aerial Registration

**Authors:** Jeng Wen Joshua Lean, Ting-Yu Yen, Wei-Fang Sun, Simon See, Hung-Kuo Chu, Shih-Hsuan Hung
**Links:** [abs](https://arxiv.org/abs/2609.16603) - [pdf](https://arxiv.org/pdf/2609.16603)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G3AR: Graph-Guided Neural Visual Geometry for Scalable Multi-Sequence Aerial Registration
- 作者：Jeng Wen Joshua Lean, Ting-Yu Yen, Wei-Fang Sun, Simon See, Hung-Kuo Chu, Shih-Hsuan Hung
- 出版日期：2026-09-15T03:58:17Z
- 分类：Geometry Foundation Models（主分类）；次要分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.16603 ；PDF https://arxiv.org/pdf/2609.16603

### 一句话总结
G3AR 通过几何验证的图像邻近图来引导分块与对齐拓扑，从而在航空多序列场景中实现可扩展的稠密神经几何配准。

### 研究问题
论文关注航空多序列图像集合中的可扩展配准问题。摘要指出两点困难：一是全上下文的神经视觉几何对数千张图像不现实；二是按序列分块的方式难以刻画多序列航空采集中不规则的、非局部的重叠关系。因此需要一种既能扩展到大图像规模、又能正确处理跨序列复杂重叠的稠密神经几何方法。

### 核心思路/方法
G3AR 是一个图引导的可扩展稠密神经几何框架，具体流程在摘要中描述为：
1. 在局部推理之前，构建一个经过几何验证的图像邻近图；
2. 该图引导生成有界重叠的分块（bounded overlapping chunks）；
3. 由这些分块诱导出一个分块图，其最大生成树定义对齐拓扑；
4. 兼容的骨干网络独立处理各分块；
5. 利用共享图像上的预测估计三维相似变换（Sim(3)），将局部相机与几何注册到统一坐标系中。

### 主要贡献
- 提出 G3AR，一个用于航空配准的图引导可扩展稠密神经几何框架。
- 通过几何验证的图像邻近图构建有界重叠分块，并用分块图的最大生成树确定对齐拓扑。
- 在共享图像上估计 Sim(3) 变换，实现局部相机与几何在公共坐标系中的注册。
- 在四个真实航空场景上，与匹配的 VGGT 和 Pi3 骨干对比中改善了位姿误差与运行时间；其 DA3 变体在被评估的神经几何方法中取得最低位姿误差。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败情形、对图构建质量的敏感性、可扩展性的具体上限、内存或计算开销细节、数据集规模与多样性、与更广泛基线比较的完整结果，以及 DA3 变体的具体配置。

### 阅读优先级
中。理由：论文针对航空多序列配准的可扩展性问题给出图引导的分块与对齐拓扑思路，并在真实场景中报告了位姿误差与运行时间的改进，对神经几何与大规模配准方向有参考价值；但摘要未披露实验细节、局限与消融信息，是否与本领域具体需求高度相关需进一步阅读正文判断。

</details>

<details>
<summary>Abstract</summary>

Full-context neural visual geometry is impractical for thousands of images, while sequence-based chunking poorly captures irregular non-local overlap in multi-sequence aerial collections. We present Graph-Guided Neural Visual Geometry for Aerial Registration (G3AR), a graph-guided framework for scalable dense neural geometry. Before local inference, G3AR builds a geometrically verified image-proximity graph that guides bounded overlapping chunks and induces a chunk graph whose maximum spanning tree defines alignment topology. Compatible backbones process chunks independently; shared-image predictions then estimate three-dimensional similarity (Sim(3)) transforms that register local cameras and geometry in a common frame. Across four real aerial scenes, G3AR improves pose error and runtime in matched VGGT- and Pi3-backed comparisons, while its DA3 variant achieves the lowest pose error among evaluated neural-geometry methods.

</details>

#### 2026-09-14 - SURE-Map: Self-Correcting Streaming Geometric Foundation Model

**Authors:** Mingkai Liu, Hao Zhao, Xingxing Zuo
**Links:** [abs](https://arxiv.org/abs/2609.15795) - [pdf](https://arxiv.org/pdf/2609.15795)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** geometric foundation model, feed-forward reconstruction, SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SURE-Map: Self-Correcting Streaming Geometric Foundation Model
- 作者：Mingkai Liu, Hao Zhao, Xingxing Zuo
- 出版日期：2026-09-14T16:10:53Z
- 分类：Geometry Foundation Models
- 链接：摘要页 https://arxiv.org/abs/2609.15795；PDF https://arxiv.org/pdf/2609.15795

### 一句话总结
SURE-Map 提出一种具备自校正能力的流式几何基础模型框架，通过跨视角几何不确定性和多时间尺度自校正，缓解流式重建中局部误差累积导致的几何畸变与长程尺度漂移。

### 研究问题
流式几何基础模型正成为 SLAM 系统的一种有吸引力的替代方案。然而，流式预测每次仅基于有限上下文，容易受到动态物体和弱纹理影响，小型局部误差会累积为严重的几何畸变和长程尺度漂移。论文因此主张：可靠的流式重建要求几何基础模型不仅具备预测能力，还应具备自校正能力。

### 核心思路/方法
SURE-Map 是一个自校正框架，建立在两个互补原则之上：

1. **显式建模跨视角几何不确定性**：不同于传统深度或点置信度主要反映单视角预测可靠性，该不确定性直接衡量联合预测的位姿与深度是否产生几何一致的跨视角像素对应。
2. **多时间尺度自校正**：由于仅靠局部校正无法消除缓慢累积的尺度误差，框架采用快速连续帧推理保持流式效率，同时利用稀疏关键帧窗口推理提供更长程的几何证据，以周期性重新校准近期轨迹的尺度。

### 主要贡献
- 提出 SURE-Map，一个面向流式几何基础模型的自校正框架，强调模型应兼具预测与自校正能力。
- 引入跨视角几何不确定性建模，直接衡量联合位姿与深度预测是否产生几何一致的跨视角像素对应。
- 提出多时间尺度自校正机制，结合快速连续帧推理与稀疏关键帧窗口推理，以周期性重校准近期轨迹尺度。
- 在长程在线前馈重建基准上取得新的最优性能：KITTI 上 ATE-RMSE 从 24.00 m 降至 17.24 m，Oxford Spires 从 5.11 m 降至 4.74 m，VBR 从 31.37 m 降至 28.58 m；结合回环闭合细化后进一步改善至 15.17 m、4.63 m 和 22.12 m。

### 局限性
摘要未提供足够信息。摘要未说明方法对特定场景类型、传感器配置、计算资源消耗、实时性上限或失败案例的具体限制；也未提供与消融实验、不同基线或边缘情况的详细分析。

### 阅读优先级
高。理由：该论文针对流式几何基础模型中的核心难题——局部误差累积与长程尺度漂移——提出明确的自校正框架，报告了在多个长程基准上的定量改进，并给出项目页面，主题与几何基础模型及在线前馈重建方向高度相关。

</details>

<details>
<summary>Abstract</summary>

Streaming geometric foundation models are emerging as a compelling alternative to SLAM systems. Yet this streaming nature introduces a fundamental issue: each prediction is made from limited context, which is vulnerable to dynamic objects and weak textures. Small local errors accumulate into severe geometric distortion and long-horizon scale drift. We argue that reliable streaming reconstruction requires geometric foundation models to be not only predictive, but also self-correcting. We introduce SURE-Map, a self-correcting framework built upon two complementary principles. First, we explicitly model cross-view geometric uncertainty. Unlike conventional depth or point confidence, which primarily reflects the reliability of individual-view prediction, our uncertainty directly measures whether the jointly predicted pose and depth induce geometrically consistent cross-view pixel correspondences. Second, because local correction alone cannot eliminate slowly accumulating scale errors, we introduce multi-timescale self-correction: fast consecutive-frame inference preserves streaming efficiency, while sparse keyframe-window inference provides longer-range geometric evidence to periodically recalibrate the scale of recent trajectories. SURE-Map establishes new state-of-the-art performance for online feed-forward reconstruction across long-horizon benchmarks, reducing ATE-RMSE from 24.00 to 17.24 m on KITTI, 5.11 to 4.74 m on Oxford Spires, and 31.37 to 28.58 m on VBR, with further improvements to 15.17, 4.63, and 22.12 m when incorporating loop-closure refinement. Project page: https://mingkai-liu.github.io/projects/sure-map/.

</details>

#### 2026-09-14 - Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras

**Authors:** Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu
**Links:** [abs](https://arxiv.org/abs/2609.15032) - [pdf](https://arxiv.org/pdf/2609.15032)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Dynamic / 4D Reconstruction
**Matched keywords:** geometry foundation model, multi-view transformer, dynamic 3D, human reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras
- 作者：Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu
- 出版日期：2026-09-14T04:50:52Z
- 分类：Geometry Foundation Models（主类）；Dynamic / 4D Reconstruction（次类）
- 链接：abstract_url: https://arxiv.org/abs/2609.15032；pdf_url: https://arxiv.org/pdf/2609.15032

### 一句话总结
Tele360 是一个面向稀疏、未标定 RGB 视频流的实时前馈人体重建与自由视角可视化系统，可在单次前向传播中联合估计相机位姿并重建动态 3D 高斯表示。

### 研究问题
摘要指出，真实人体的实时自由视角可视化对沉浸式通信和交互式数字体验很重要，但现有方法要么依赖计算开销大的优化，要么需要已标定相机和低分辨率输入，难以实现实时高分辨率部署。该论文要解决的问题是：如何从稀疏、未标定（unposed）的 RGB 流中，实时前馈地完成动态人体重建与自由视角可视化。

### 核心思路/方法
- 提出 Tele360，摘要称其为首个面向稀疏、未标定 RGB 流的实时前馈动态人体重建与实时自由视角可视化系统。
- 在单次前向传播中，联合估计相机位姿，并为每个时间实例重建动态 3D 高斯表示。
- 设计轻量级、稀疏感知的多视角 Transformer 主干：对前景人体区域进行 token 化，同时通过共享场景 token 保留全局上下文。
- 使用全 Transformer 的高斯解码器，以缓解卷积导致的过度平滑，同时保持解码稀疏且高效。
- 引入混合特征金字塔，将多尺度外观线索注入几何预测。
- 引入轻量级可微 Levenberg-Marquardt 相机细化层，以增强多视角一致性和几何对齐。
- 通过教师—学生蒸馏，从大型视觉—几何基础模型迁移多视角几何先验，以稳定稀疏、未标定输入下的学习。
- 将预测的高斯图通过视频编解码器流式传输到远程设备，用于交互式自由视角渲染。

### 主要贡献
- 提出 Tele360，摘要称其为首个面向稀疏、未标定 RGB 流的实时前馈动态人体重建与实时自由视角可视化系统。
- 实现单次前向传播中联合相机位姿估计与动态 3D 高斯表示重建。
- 设计稀疏感知多视角 Transformer 主干、全 Transformer 高斯解码器、混合特征金字塔和可微 Levenberg-Marquardt 相机细化层。
- 通过教师—学生蒸馏从大型视觉—几何基础模型迁移多视角几何先验。
- 摘要报告：在 studio benchmarks 上达到 state-of-the-art 视觉质量，并在单张消费级 GPU 上支持 2K 输入到渲染的实时性能，超过 25 FPS；额外采集序列展示了在多相机设置下不同受试者、服装和运动中的表现。

### 局限性
- 摘要未提供足够信息说明方法在何种条件下会失败或性能下降。
- 摘要未提供足够信息说明对相机数量、稀疏程度、遮挡、极端运动或非 studio 场景的泛化限制。
- 摘要未提供足够信息说明实时 2K 超过 25 FPS 的具体硬件配置、延迟分解或分辨率细节。
- 摘要未提供足够信息说明与基线方法的完整定量对比、误差指标或消融结果。
- 摘要未提供足够信息说明教师—学生蒸馏中教师模型的具体身份、蒸馏损失或训练数据规模。
- 摘要未提供足够信息说明视频编解码器流式传输对渲染质量、延迟或带宽的影响。

### 阅读优先级
高。理由：该论文聚焦稀疏、未标定相机下的实时前馈动态人体重建与自由视角可视化，摘要明确声称在单次前向传播中联合位姿估计与 3D 高斯重建，并报告单张消费级 GPU 上 2K 输入到渲染超过 25 FPS；同时涉及 Transformer 主干、可微相机细化与基础模型蒸馏等多项技术组合，对实时人体重建、动态 4D 重建和几何基础模型方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Live free-viewpoint visualization of real humans is critical for immersive communication and interactive digital experiences. Existing methods either rely on computationally expensive optimization or require calibrated cameras and low-resolution inputs, making real-time high-resolution deployment impractical. In this work, we present Tele360, the first real-time feed-forward system for dynamic human reconstruction and live free-viewpoint visualization from sparse, unposed RGB streams. Our system jointly estimates camera poses and reconstructs a dynamic 3D Gaussian representation for each time instance in a single forward pass. To achieve this, we start by designing a lightweight sparsity-aware multi-view transformer backbone that tokenizes foreground human regions while preserving global context through a shared scene token. We then employ a fully transformer-based Gaussian decoder to mitigate convolution-induced over-smoothing while keeping decoding sparse and efficient. In addition, we introduce a hybrid feature pyramid that injects multi-scale appearance cues into geometry prediction. We further introduce a lightweight differentiable Levenberg-Marquardt camera refinement layer to enhance multi-view consistency and geometric alignment. Moreover, to stabilize learning under sparse, unposed inputs, we transfer multi-view geometry priors from a large visual-geometry foundation model via teacher-student distillation. Finally, the predicted Gaussian maps are streamed with video codecs to remote devices for interactive free-viewpoint rendering. Extensive experiments show that Tele360 achieves state-of-the-art visual quality on studio benchmarks while supporting real-time 2K input-to-rendering at over 25 FPS on a single consumer GPU. Additional captured sequences illustrate its performance across varied subjects, clothing, and motions under our multi-camera setup.

</details>

#### 2026-09-10 - SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views

**Authors:** Langxu Zhao, Zuan Gu, Yingdan Zhang, Pengfei Zhao, Tianhan Gao
**Links:** [abs](https://arxiv.org/abs/2609.11279) - [pdf](https://arxiv.org/pdf/2609.11279)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** DUSt3R, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views
- 作者：Langxu Zhao, Zuan Gu, Yingdan Zhang, Pengfei Zhao, Tianhan Gao
- 出版日期：2026-09-10T09:12:48Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.11279 ；PDF https://arxiv.org/pdf/2609.11279

### 一句话总结
该论文提出端到端模型 SAMV-DUSt3R，将 SAM2 的 2D 掩码注入 MV-DUSt3R 重建流程，以在稀疏多视角下实现以实例为中心的三维场景解耦，并报告了重建精度与参考视图选择方面的提升。

### 研究问题
从三维场景中解耦物体（实例级分离）的需求日益增长，论文关注在稀疏多视角条件下实现实例级的三维场景解耦与重建。摘要指出其目标是在不依赖多阶段流水线的情况下完成物体级解耦，并同时提升形状精度与重建稳定性。

### 核心思路/方法
- 提出端到端模型 SAMV-DUSt3R，将 SAM2 的二维掩码注入到 MV-DUSt3R 的重建过程中。
- 设计 Cross Flow Mask Block，利用这些掩码引导网络朝向目标实例，从而联合提升形状精度并实现物体级解耦，且无需多阶段流水线。
- 为保证重建稳定性，引入轻量级 Spatial RankGNN 来选择最优参考视图，摘要给出选择准确率为 73.5%。

### 主要贡献
- 提出将 SAM2 二维掩码注入 MV-DUSt3R 重建的端到端方法，实现以实例为中心的三维场景解耦，避免多阶段流水线。
- 通过 Cross Flow Mask Block 引导网络关注目标实例，联合改善形状精度并实现物体级解耦。
- 引入轻量级 Spatial RankGNN 进行最优参考视图选择，报告选择准确率为 73.5%。
- 摘要称大量实验表明，与最先进基线相比，该方法在多种指标上平均重建精度提升 11%，并展现出较强的实例解耦能力，对驾驶、机器人、AR/VR 和遗产数字化具有明显益处。

### 局限性
- 摘要未提供足够信息说明实验数据集、评价指标细节、对比基线的具体配置以及消融实验设置。
- 摘要未提供足够信息说明方法在不同稀疏视角数量、遮挡、动态场景或类别分布下的失效条件与适用范围。
- 摘要未提供足够信息说明 Spatial RankGNN 选择错误时对重建结果的影响程度，以及 Cross Flow Mask Block 对 SAM2 掩码质量的依赖与鲁棒性。
- 摘要未提供足够信息说明计算开销、推理速度、模型规模与训练数据需求。

### 阅读优先级
高。理由：该论文聚焦稀疏多视角下的实例级三维场景解耦，提出端到端注入 2D 掩码与参考视图选择的组合方案，并在摘要中报告了明确的重建精度提升与选择准确率；主题同时关联几何基础模型与具身/机器人/AR 应用，对三维重建与实例解耦方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

With the rising demand to decouple objects from 3D scenes, we propose SAMV-DUSt3R, an end-to-end model that injects SAM2 2D masks into MV-DUSt3R reconstruction. A Cross Flow Mask Block uses these masks to steer the network toward the target instance, jointly improving shape accuracy and achieving object-level disentanglement without multi-stage pipelines. To ensure reconstruction stability, a lightweight Spatial RankGNN selects the optimal reference view with a selection accuracy of 73.5\%. Extensive experiments demonstrate that our method boosts average reconstruction precision by 11\% across various metrics compared to state-of-the-art baselines. These results reveal a strong instance-disentanglement capability and clear benefits for driving, robotics, AR/VR, and heritage digitisation.

</details>

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-14 - Racing in Volume with Flow Ensembles

**Authors:** Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre
**Links:** [abs](https://arxiv.org/abs/2609.16310) - [pdf](https://arxiv.org/pdf/2609.16310)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Racing in Volume with Flow Ensembles
- 作者：Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre
- 出版日期：2026-09-14T20:18:59Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.16310 ；PDF：https://arxiv.org/pdf/2609.16310

### 一句话总结
论文针对“从稀疏固定外部相机流式重建快速运动主体”这一未被覆盖的场景，提出流式 4D 高斯泼溅方法 FastFlowGS，并发布基于 Unreal Engine 5 的高速户外重建基准 Monaco4D。

### 研究问题
摘要指出，流式 4D 重建此前仅在室内、密集相机环绕、主体以人类速度移动的条件下得到验证；户外 4D 重建要么依赖安装在移动车辆上的相机，要么依赖覆盖有限、离线观测准静态主体的相机阵列。而真正对观众重要的场景是：快速移动的主体，被稀疏的、以非自我中心方式布置的相机环观测，并进行流式处理。摘要明确表示，目前没有方法针对这一场景，也没有用于评估该场景的基准。

### 核心思路/方法
- 任务设定：从少量固定外部相机出发，流式重建快速移动的主体。
- 方法名称：FastFlowGS，一种流式 4D Gaussian Splatting 方法。
- 技术要点：融合稀疏匹配（sparse matches）、半稠密轨迹（semi-dense tracks）和稠密光流（dense optical flow）；将每种信号以几何不确定性提升到 3D；通过 Kalman 式的时序更新进行组合。
- 基准：Monaco4D，基于 Unreal Engine 5 的写实高速户外重建基准，提供不同光照下、来自赛道边、车载和无人机视角的 Formula 1 序列，并带有稠密真值。

### 主要贡献
- 提出 FastFlowGS，面向从少量固定外部相机流式重建快速移动主体的流式 4D 高斯泼溅方法。
- 提出融合稀疏匹配、半稠密轨迹与稠密光流，并以几何不确定性提升到 3D、通过 Kalman 式时序更新组合的技术路线。
- 发布 Monaco4D，一个基于 Unreal Engine 5 的写实高速户外重建基准，包含 Formula 1 序列、多种光照条件、赛道边/车载/无人机视角以及稠密真值。
- 摘要报告的结果：在 CMU-Panoptic 上，FastFlowGS 相比最强基线在 VMAF 上超出 12.6%，效率提升 35%；在 Monaco4D 上，现有流式方法严重退化，而该方法将动态区域 PSNR 最多提升 18.6%，每帧优化时间降低 28.3%。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败情形、对相机数量或布置的敏感度、对特定场景或数据类型的依赖、计算资源需求上限、基准本身的覆盖边界等潜在限制。

### 阅读优先级
高。理由：摘要明确指出该任务场景此前没有方法针对性解决、也没有评估基准，属于空白问题设定；同时论文同时给出方法、基准和多项定量结果，并公开项目页面。对 4D 重建、流式重建、动态场景表示与高速户外场景感兴趣的读者，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Streaming 4D reconstruction has been demonstrated only indoors, on dense camera rigs surrounding subjects that move at human pace. Outdoor 4D reconstruction exists but relies either on cameras mounted on the moving vehicle itself, or on limited-coverage arrays observing quasi-static subjects offline. The case that actually matters for spectators is a fast-moving subject, watched from a sparse ring of allocentric cameras, streaming. No method targets this, and no benchmark exists to evaluate one. To this end, we introduce FastFlowGS, a streaming 4D Gaussian Splatting method for reconstructing fast-moving subjects from a small set of fixed external cameras, and Monaco4D, a photorealistic Unreal Engine 5 benchmark for high-speed outdoor reconstruction. FastFlowGS fuses sparse matches, semi-dense tracks, and dense optical flow by lifting each signal to 3D with geometric uncertainty and combining them through a Kalman-style temporal update. Monaco4D provides Formula 1 sequences under varied illumination from trackside, onboard, and drone viewpoints with dense ground truth. On CMU-Panoptic, FastFlowGS exceeds the strongest baseline by 12.6% VMAF at 35% greater efficiency. On Monaco4D, where existing streaming methods degrade severely, it improves dynamic-region PSNR by up to 18.6% with 28.3% lower per-frame optimization time. Dataset and additional details can be found at https://humansensinglab.github.io/monaco4d/.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-15 - EventEgoHands++: Event-based Egocentric 3D Hand Mesh Reconstruction with Real Dataset

**Authors:** Ryosei Hara, Wataru Ikeda, Masashi Hatano, Mariko Isogawa
**Links:** [abs](https://arxiv.org/abs/2609.17189) - [pdf](https://arxiv.org/pdf/2609.17189)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EventEgoHands++: Event-based Egocentric 3D Hand Mesh Reconstruction with Real Dataset
- 作者：Ryosei Hara, Wataru Ikeda, Masashi Hatano, Mariko Isogawa
- 出版日期：2026-09-15T13:46:02Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.17189 ；PDF https://arxiv.org/pdf/2609.17189

### 一句话总结
该论文提出 EventEgoHands++，用事件相机进行第一人称视角 3D 手部网格重建，通过实例级手部检测和自适应注意力缓解背景事件干扰，并构建了新的真实事件相机第一人称手部数据集 EEH-R。

### 研究问题
第一人称视角下的 3D 手部网格重建对人机交互和 AR/VR 等下游应用很重要。传统相机方法在低光环境和严重运动模糊下表现受限，因此事件相机因其高动态范围和高时间分辨率受到关注。但将事件相机用于第一人称手部重建存在困难：相机佩戴者的运动会产生密集背景事件，掩盖手部信号。此前首个第一人称事件相机方法虽用手部分割缓解该问题，但其二值手部掩码不区分左右手，导致模型缺少实例级手部信息；即使只有一只手或没有手时也会预测双手，进而造成手间关系错误并降低重建精度。

### 核心思路/方法
论文提出 EventEgoHands++ 框架，用于从第一人称视角基于事件进行 3D 手部网格重建。方法包含一个 Hand Detector，用于估计左右手的实例级边界框和掩码。此外引入 Adaptive Attention，根据这些检测结果动态控制注意力门控，以准确学习双手之间的空间关系和相互交互。为训练和评估该框架，作者扩展了合成 N-HOT3D 数据集，并新建了 EEH-R，一个真实世界事件相机第一人称手部数据集，包含约 100 万标注帧，采集环境包括低光条件。

### 主要贡献
- 提出 EventEgoHands++，一个从第一人称视角进行基于事件的 3D 手部网格重建框架。
- 引入 Hand Detector，估计左右手的实例级边界框和掩码，以提供实例级手部信息。
- 引入 Adaptive Attention，基于检测结果动态门控注意力，学习双手间的空间关系和相互交互。
- 扩展合成 N-HOT3D 数据集，并构建 EEH-R，据摘要称为目前最大的真实事件相机第一人称手部数据集，含约 100 万标注帧，覆盖包括低光在内的环境。
- 在合成和真实数据集上进行大量实验，摘要称该方法持续优于基线。

### 局限性
摘要未提供足够信息。摘要未说明具体基线方法、评价指标、数值结果、失败案例、计算成本、泛化边界或数据集采集细节的局限。

### 阅读优先级
中。理由：该工作针对事件相机第一人称 3D 手部重建中的明确痛点，即背景事件干扰和左右手实例区分不足，并同时提出方法框架与新真实数据集；对事件视觉、第一人称手部重建、AR/VR 与人机交互相关方向有参考价值。但仅凭摘要无法判断实验优势幅度、基线设置和实际可用性，因此优先级为中等而非高。

</details>

<details>
<summary>Abstract</summary>

3D hand mesh reconstruction is a challenging yet essential task for downstream applications, including human-robot interaction and AR/VR. Although conventional cameras have been widely adopted for this task, methods that rely on them struggle in low-light environments and under severe motion blur. To address these limitations, event-based cameras have recently attracted attention for their high dynamic range and high temporal resolution. However, applying event cameras to egocentric hand reconstruction remains challenging because camera wearer's motion produces dense background events that obscure hand-specific signals. Although the first egocentric event-based approach mitigates this issue using hand segmentation, its binary hand mask does not distinguish between left and right hands. As a result, the model lacks instance-level hand information and predicts both hands even when only one or neither hand is present. This limitation leads to incorrect inter-hand relationships and degraded reconstruction accuracy. In this paper, we propose EventEgoHands++, a framework for event-based 3D hand mesh reconstruction from an egocentric viewpoint. The proposed method incorporates a Hand Detector that estimates instance-level bounding boxes and masks for both the left and right hands. Moreover, we introduce Adaptive Attention, which dynamically gates the attention based on these detection results to accurately learn the spatial relationship and mutual interactions between the hands. To train and evaluate our framework, we extend the synthetic N-HOT3D dataset and newly construct EEH-R, the largest real-world event-based egocentric hand dataset to date, comprising approximately 1M annotated frames captured in environments including low-light conditions. Extensive experiments on both synthetic and real datasets demonstrate that our method consistently outperforms the baselines.

</details>

#### 2026-09-15 - HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM

**Authors:** Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei, Andrew Bradley, Alexander Rast
**Links:** [abs](https://arxiv.org/abs/2609.17168) - [pdf](https://arxiv.org/pdf/2609.17168)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM
- 作者：Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei, Andrew Bradley, Alexander Rast
- 出版日期：2026-09-15T13:32:32Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；次要分类：未提供
- 链接：摘要页 https://arxiv.org/abs/2609.17168 ；PDF https://arxiv.org/pdf/2609.17168

### 一句话总结
论文受人类记忆与感知启发提出 HuMem-VPR 语义地点识别方法，并将其集成到 ORB-SLAM3 得到 HuMemSLAM，旨在兼顾高检索精度与低延迟，以提升视觉 SLAM 在感知歧义和感知变化下的鲁棒性。

### 研究问题
自主系统需要可靠的地点识别来支撑高效的同时定位与建图（SLAM）。传统几何视觉 SLAM 依赖低层特征与几何一致性，但容易受到两类问题影响：感知歧义（不同地点看起来相似）和感知变化（同一地点看起来不同）。语义 SLAM 与现代学习式视觉地点识别（VPR）方法在困难感知条件下提升了鲁棒性，但实时部署同时要求高检索精度与低延迟。论文即针对这一精度—延迟权衡问题展开。

### 核心思路/方法
- 提出 HuMem-VPR：受人类记忆与感知启发，利用自下而上的感知证据与自上而下的上下文推理之间的双向关系，实现高层的地点理解。
- 提出 HuMemSLAM：将 HuMem-VPR 与 ORB-SLAM3 集成。
- 摘要提及在真实图像基准、CARLA 基准以及在线实验中评估，并涉及 Recall @1 与提交给几何后端的候选提案数量等指标。

### 主要贡献
- 提出 HuMem-VPR，一种受人类记忆与感知启发的语义地点识别方法。
- 在真实图像基准上取得最高综合检索精度；在 CARLA 基准上取得有竞争力的精度；相比所评估的当前最优 VPR 方法，延迟约低两到三倍。
- 将 HuMem-VPR 集成进 ORB-SLAM3 形成 HuMemSLAM；在所评估的数据集族和在线实验中，相比 ORB-SLAM3 原生检索显著提升了集成 Recall @1，同时减少了提交给几何后端的候选提案数量。

### 局限性
- 摘要未提供足够信息说明方法的具体网络结构、训练细节、超参数设置与推理硬件环境。
- 摘要未提供足够信息说明各基准的完整数据集名称、规模与评测协议细节。
- 摘要未提供足够信息说明失败案例、极端场景表现、内存占用或功耗等部署约束。
- 摘要未提供足够信息说明与 ORB-SLAM3 集成时的具体修改位置及对建图精度、轨迹误差等完整 SLAM 指标的影响。
- 摘要未提供足够信息说明“所评估的当前最优 VPR 方法”具体包含哪些对比方法。

### 阅读优先级
中。理由：论文主题处于视觉 SLAM、语义地点识别与实时部署的交叉点，且明确报告了精度与延迟方面的优势，对关注 SLAM 鲁棒性和 VPR 效率的读者有参考价值；但仅凭摘要无法判断实验覆盖面、可复现性与完整 SLAM 精度影响，需阅读全文后才能评估其实际贡献强度。

</details>

<details>
<summary>Abstract</summary>

Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place appears different. Although semantic SLAM and modern learned visual place recognition (VPR) methods improve robustness under challenging perceptual conditions, real-time deployment requires both high retrieval accuracy and low latency. Inspired by human memory and perception, we propose HuMem-VPR, which exploits the bidirectional relationship between bottom-up perceptual evidence and top-down contextual reasoning to achieve high-level place understanding. We further introduce HuMemSLAM, the integration of HuMem-VPR with ORB-SLAM3. HuMem VPR achieved the highest aggregate retrieval accuracy on the real-image benchmark, competitive accuracy on the CARLA benchmark, and approximately two to three times lower latency than the evaluated state-of-the-art VPR methods. Across the evaluated dataset families and online experiments, HuMemSLAM substantially improved integrated Recall @1 over ORB-SLAM3's native retrieval while reducing the proposals submitted to its geometric backend.

</details>

#### 2026-09-15 - BRAVE-6D: Benchmark for Robotic Active Vision in 6DOF Pose Estimation

**Authors:** Philipp Ausserlechner, Bernhard Neuberger, Alessandro Scherl, Michael Schebek, Stefan Thalhammer, Markus Vincze
**Links:** [abs](https://arxiv.org/abs/2609.17106) - [pdf](https://arxiv.org/pdf/2609.17106)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** pose estimation, 3DGS, view synthesis, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BRAVE-6D: Benchmark for Robotic Active Vision in 6DOF Pose Estimation
- 作者：Philipp Ausserlechner, Bernhard Neuberger, Alessandro Scherl, Michael Schebek, Stefan Thalhammer, Markus Vincze
- 出版日期：2026-09-15T12:38:20Z
- 分类：primary_category: 3D Reconstruction & Multi-view Geometry；secondary_categories: Neural Scene Representations & Rendering
- 链接：abstract_url: https://arxiv.org/abs/2609.17106；pdf_url: https://arxiv.org/pdf/2609.17106

### 一句话总结
论文提出 BRAVE-6D，一个利用高斯泼溅（3DGS）视图合成来评估机器人主动视觉 6DOF 物体位姿估计系统的基准，并给出在该场景中进行视觉伺服与位姿估计的基线方案。

### 研究问题
机器人检测与抓取小物体仍是显著挑战。主动视觉（机器人靠近物体）是直观的解决方案，但由于需要完全相同的物理场景设置，不同方法难以在共同基础上进行比较。因此，论文关注如何为机器人主动视觉的物体位姿估计（抓取物体的关键第一步）提供可比较的评估基准。

### 核心思路/方法
BRAVE-6D 利用基于高斯 Splats（3DGS）的视图合成，提供用于基准测试主动视觉系统的场景与工具。摘要提到展示了基线方案，这些基线在场景内执行视觉伺服并准确估计小物体的位姿。

### 主要贡献
- 提出 BRAVE-6D，一个面向机器人主动视觉、用于物体位姿估计评估的基准。
- 该基准利用基于高斯 Splats（3DGS）的视图合成来提供场景与工具，以支持主动视觉系统的基准测试。
- 展示了在场景内执行视觉伺服并准确估计小物体位姿的基线方案。

### 局限性
- 具体基线方法细节、评估指标、数据集规模、实验设置与定量结果：摘要未提供足够信息。
- 与现有基准的详细对比：摘要未提供足够信息。
- 3DGS 视图合成与真实物理场景之间的差异分析：摘要未提供足够信息。
- 方法的泛化能力与失败案例：摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对机器人主动视觉 6DOF 位姿估计提出基准，并借助 3DGS 视图合成解决物理场景难以复现的问题，对具身智能、机器人抓取和位姿估计方向有参考价值；但摘要仅给出高层思路与基线概述，缺少实验细节与定量结果，是否值得精读需进一步查看正文。

</details>

<details>
<summary>Abstract</summary>

Detecting and grasping small objects remains a significant challenge in robotics. Active vision, where the robot moves closer to the object, is an intuitive solution, yet comparing approaches on common ground is difficult since identical physical scene setups are required. Hence, we introduce BRAVE-6D, a benchmark designed to evaluate robotic active vision systems for object pose estimation, a crucial first step in grasping objects. BRAVE-6D leverages view synthesis based on Gaussian Splats (3DGS) to provide scenes and tools for benchmarking active vision systems. We show baseline solutions performing visual servoing within the scene and accurately estimating the poses of small objects.

</details>

#### 2026-09-15 - Evaluating Mesh Reconstruction Methods for Crop Phenotyping

**Authors:** Karanvir Singh, Theo Morales, Binh-Son Hua, Mukesh Saini
**Links:** [abs](https://arxiv.org/abs/2609.16926) - [pdf](https://arxiv.org/pdf/2609.16926)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mesh reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evaluating Mesh Reconstruction Methods for Crop Phenotyping
- 作者：Karanvir Singh, Theo Morales, Binh-Son Hua, Mukesh Saini
- 出版日期：2026-09-15T10:02:29Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：摘要链接 https://arxiv.org/abs/2609.16926 ；PDF 链接 https://arxiv.org/pdf/2609.16926

### 一句话总结
该工作面向农作物表型分析中的远程 3D 数字化需求，评估了 7 种网格重建流程，并在定性与定量指标下发现 GGGS、PGSR 和 2DGS 的输出更优。

### 研究问题
农作物表型分析对其全生命周期研究和提高产量具有重要意义，但对于生长在远程地点的作物，专家无法到现场是一个挑战。论文试图借助 3D 重建技术实现作物数字化，使专家能够随时随地访问生成的 3D 作物模型，因此需要评估当前 3D 重建流程在作物表型分析任务中的表现。

### 核心思路/方法
论文评估了近期的 3D 重建流程用于作物表型分析，重点关注 7 种网格重建流程，并从定性和定量两个方面衡量其输出的保真度与一致性。评价指标包括 User ratings、Chamfer distance、LPIPS、PSNR 和 SSIM，并据此比较不同流程的优劣。

### 主要贡献
- 针对作物表型分析任务，评估了 7 种网格重建流程。
- 对重建输出的保真度和一致性进行了定性与定量测量。
- 结果显示 GGGS、PGSR 和 2DGS 的网格优于其他流程。
- 在包含 User ratings、Chamfer distance、LPIPS、PSNR、SSIM 五个维度的雷达图上，GGGS 流程比第二好的 2DGS 流程约高 27%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该论文主题明确，聚焦作物表型分析中的网格重建方法评估，并给出了 7 种流程的比较结论与具体指标维度；但用户未提供额外兴趣方向，且摘要未展开数据集、实验设置和完整局限性，因此适合作为相关方向的方法评估参考，而非必须优先精读的通用突破性论文。

</details>

<details>
<summary>Abstract</summary>

Phenotyping an agricultural crop is crucial for studying its entire life cycle, as it provides vital insights to improve yield and, ultimately, food production. Doing the same for crops grown on remote sites is a challenge for the specialists who cannot be available on-site. 3D reconstruction techniques offer a promising solution to this problem by enabling crop digitization, allowing specialists to access the resulting 3D crop models from anywhere at any time. In this work, we evaluate recent 3D reconstruction pipelines for crop phenotyping. We focus on 7 mesh reconstruction pipelines and measure the fidelity and consistency of their outputs qualitatively and quantitatively. Our results suggest that the meshes produced by the GGGS, PGSR, and 2DGS are preferable to the other pipelines, owing to their quantitative metrics and visually pleasing outputs. The GGGS pipeline is better than the second-best pipeline (2DGS) by about 27\% on the radar chart with 5 dimensions, namely, User ratings, Chamfer distance, LPIPS, PSNR, and SSIM.

</details>

#### 2026-09-15 - PriorPose: Reference-Guided Joint Deformation and Alignment for Category-Level Object Pose Estimation

**Authors:** Yihan Chen, Huan Ren, Wenfei Yang, Hang Du, Tianzhu Zhang, Feng Wu
**Links:** [abs](https://arxiv.org/abs/2609.16727) - [pdf](https://arxiv.org/pdf/2609.16727)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PriorPose: Reference-Guided Joint Deformation and Alignment for Category-Level Object Pose Estimation
- 作者：Yihan Chen, Huan Ren, Wenfei Yang, Hang Du, Tianzhu Zhang, Feng Wu
- 出版日期：2026-09-15T06:57:34Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2609.16727) / [PDF](https://arxiv.org/pdf/2609.16727)

### 一句话总结
PriorPose 提出一种参考引导的对应关系框架，将类别先验显式保留，并在共享特征空间中联合求解规范化与对齐，以缓解无先验方法的泛化问题和串行“先变形后对齐”流程的误差级联。

### 研究问题
论文关注类别级物体位姿估计：对未见过的实例，在没有实例专属 CAD 模型的情况下恢复相似变换 \((R,t,s)\)。摘要指出，多数有竞争力的方法基于对应关系，但存在两类问题：
- 无先验方法直接从局部观测回归规范化（NOCS）坐标，并在网络权重中隐式记忆规范化坐标系，使参数与类别典型朝向绑定，在分布偏移下泛化性受损。
- 有先验方法虽引入类别先验，但通常采用串行的“先变形再对齐”流程；其中欠约束的规范化补全可能破坏对应关系，并在位姿估计中引发误差级联。

### 核心思路/方法
论文提出 PriorPose，一种参考引导的对应关系框架，核心是保持类别先验显式，并在共享特征空间中联合求解规范化与对齐。具体而言：
- 使用参考引导的种子 Transformer，将部分观测和类别先验分别嵌入为 token 集合，并通过几何感知种子进行融合。
- 网络基于融合特征联合预测：可见点的逐点 NOCS 场，以及先验的规范化变形，从而重建完整的规范化实例。
- 深度位姿头从由此诱导的对应关系中回归 \((R,t,s)\)。
- 引入两部分形状一致性目标，包含规范化空间一致性和相机空间一致性损失，将对应关系、变形与位姿耦合起来，以减少对记忆化规范朝向的依赖，并避免“先变形后对齐”的误差级联。

### 主要贡献
- 提出 PriorPose，一个参考引导的对应关系框架，将类别先验显式保留，并在共享特征空间中联合求解规范化与对齐。
- 设计参考引导的种子 Transformer，将部分观测与类别先验作为 token 集合融合，并联合预测 NOCS 场与先验的规范化变形。
- 引入包含规范化空间和相机空间一致性的两部分形状一致性目标，耦合对应关系、变形与位姿，缓解对记忆化规范朝向的依赖并避免串行流程的误差级联。
- 摘要声称在标准及更大类别基准上，多数评估指标达到新的最优结果，尤其在严格位姿阈值下表现突出；在宽松位姿与 IoU 指标上保持竞争力，并在形状变化和域偏移下展现更好的鲁棒性。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算开销、对先验质量的依赖程度、在极端遮挡或严重域偏移下的表现，也未提供消融实验细节和定量结果的具体数值。因此无法基于摘要判断其局限性细节。

### 阅读优先级
高。理由：该论文针对类别级物体位姿估计中无先验方法的泛化瓶颈和有先验方法的误差级联问题，提出联合变形与对齐的新框架，并声称在多个基准上取得最优结果，尤其严格阈值下表现突出；若关注类别级位姿估计、NOCS 对应关系、类别先验利用或 Transformer 在 3D 任务中的应用，该论文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Category-level object pose estimation seeks to recover a similarity transform $(R,t,s)$ for unseen instances without instance-specific CAD models. Most competitive methods are correspondence-based: prior-free variants regress canonical (NOCS) coordinates directly from local observations and implicitly memorize the canonical frame in the weights, which ties the parameters to category-typical orientations and hurts generalization under distribution shift; prior-based variants introduce a category prior but typically follow a serial deform-then-align pipeline, where underconstrained canonical completion can corrupt correspondences and induce error cascades in pose. We propose PriorPose, a reference-guided correspondence framework that keeps the category prior explicit and solves canonicalization and alignment jointly in a shared feature space. A reference-guided seeded transformer embeds the partial observation and the category prior as token sets and fuses them via geometry-aware seeds, from which the network jointly predicts a per-point NOCS field for visible points and a canonical deformation of the prior that reconstructs a full canonical instance, while a deep pose head regresses $(R,t,s)$ from the induced correspondences. A two-part shape consistency objective, with canonical-space and camera-space consistency losses, couples correspondence, deformation, and pose, reducing reliance on memorized canonical orientations and avoiding deform-then-align error cascades. Experiments on standard and larger-category benchmarks demonstrate that PriorPose sets new state-of-the-art results on most evaluated metrics, especially under strict pose thresholds, while remaining competitive on relaxed pose and IoU metrics and showing improved robustness under shape variation and domain shift.

</details>

#### 2026-09-14 - Tendon-Driven Continuum Robot with Modular Stiffness and In-Situ Self Pose Estimation

**Authors:** Guo Ning, Sue, Zheng Cao, Junzhe Hu, Xiangyun Bu, David Quinn, Tiancheng Wu, Zackory Erickson, Carmel Majidi
**Links:** [abs](https://arxiv.org/abs/2609.16256) - [pdf](https://arxiv.org/pdf/2609.16256)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tendon-Driven Continuum Robot with Modular Stiffness and In-Situ Self Pose Estimation
- 作者：Guo Ning, Sue, Zheng Cao, Junzhe Hu, Xiangyun Bu, David Quinn, Tiancheng Wu, Zackory Erickson, Carmel Majidi
- 出版日期：2026-09-14T19:21:09Z
- 分类：3D Reconstruction & Multi-view Geometry（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2609.16256) / [PDF](https://arxiv.org/pdf/2609.16256)

### 一句话总结
本文提出一种模块化连续体机器人平台，通过可互换的连续关节实现机械可重构与刚度预设，并借助磁传感器与模块化学习框架实现本体位姿自估计，从而摆脱对外部追踪基础设施的依赖。

### 研究问题
连续体机器人虽能实现平滑形变并在受限环境中安全交互，但现有系统多针对特定任务设计，且依赖外部传感基础设施，导致其适应性与实际部署能力受限。本文关注的核心问题是：能否构建一个自包含的连续体机器人平台，同时具备机械可重构性与机载位姿自感知能力。

### 核心思路/方法
- **机械层面**：机器人由可互换的连续关节构成，关节刚度通过解析方式预先计算，从而支持快速组装并可直接对机器人形状进行编程。
- **感知层面**：采用磁传感器实现本体感知，并配合模块化学习框架——每个关节训练单一模型，该模型可在不同构型间复用。
- **验证方式**：在真实世界环境中进行实验验证，展示自感知能力与无需外部追踪的自适应能力。

### 主要贡献
1. 提出一个自包含的模块化连续体机器人平台，将机械可重构性与机载位姿估计相结合。
2. 设计可互换连续关节，其刚度经解析预计算，支持快速组装与机器人形状的直接编程。
3. 构建基于磁传感器与模块化学习框架的本体感知方案，实现单关节模型跨构型复用。
4. 在真实世界实验中验证了系统的自感知与自适应能力，且不依赖外部追踪。

### 局限性
摘要未提供足够信息。摘要中未说明具体的实验规模、精度指标、关节数量上限、模型泛化边界、磁传感器受环境干扰的影响，也未提及失败案例或与基线方法的对比结果。

### 阅读优先级
**中**。理由：该工作将模块化机械设计与机载本体感知结合，问题定位清晰，且强调无需外部追踪的实际部署能力，对连续体机器人领域有一定参考价值；但摘要未给出定量结果与实验细节，且其一级分类标注为“3D Reconstruction & Multi-view Geometry”，与论文主题的匹配度存疑，需进一步阅读全文才能判断方法深度与验证充分性。

</details>

<details>
<summary>Abstract</summary>

Continuum robots enable smooth shape morphing and safe interaction in confined environments. However, most existing systems are task-specific and depend on external sensing infrastructure, limiting their adaptability and real-world deployment. This paper presents a self-contained modular continuum robotic platform that combines mechanical reconfigurability with onboard pose estimation. The robot is constructed from interchangeable continuum joints with analytically precomputed stiffness, allowing rapid assembly and direct programming of the robot shape. Proprioceptive sensing is achieved using magnetic sensors and a modular learning-based framework, where a single model is trained per joint and reused across configurations. The system is experimentally validated in real world, demonstrating self-sensing capabilities and adaptation without external tracking.

</details>

#### 2026-09-14 - Integrating Multi-view Multi-light Surface Reconstruction into Cultural Heritage Workflows

**Authors:** Baptiste Brument, Robin Bruneau, Benjamin Coupry, Vincent Demoulin, Jean Mélou, Antoine Laurent, Fabien Castan, Jean-Denis Durou, Lilian Calvet
**Links:** [abs](https://arxiv.org/abs/2609.15833) - [pdf](https://arxiv.org/pdf/2609.15833)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** surface reconstruction, photogrammetry

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Integrating Multi-view Multi-light Surface Reconstruction into Cultural Heritage Workflows
- 作者：Baptiste Brument, Robin Bruneau, Benjamin Coupry, Vincent Demoulin, Jean Mélou, Antoine Laurent, Fabien Castan, Jean-Denis Durou, Lilian Calvet
- 出版日期：2026-09-14T16:31:18Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.15833) / [PDF](https://arxiv.org/pdf/2609.15833)

### 一句话总结
作者将现成的多视图、多光照表面重建计算机视觉组件集成到开源摄影测量框架 Meshroom 中，以形成面向文化遗产工作流的可用软件层。

### 研究问题
文化遗产记录日益依赖基于图像的三维表面重建，摄影测量软件已使相关流程对考古学家、保护人员和遗产技术人员可行。然而，这些工具通常在常规多视图采集中表现良好，却不常规地利用更丰富的多视图、多光照数据，尽管这类数据有潜力改善精细尺度表面重建。该问题在遗产场景中尤为相关，因为诸如 RTI 穹顶等可控光照采集设备已被用于采集光照变化的图像集。因此，挑战在于如何将现有采集实践与近期计算机视觉方法连接起来，并使其能以可用于实际遗产工作流的形式落地。

### 核心思路/方法
论文不提出新的重建算法，而是组装并暴露现有的先进方法，将其集成到开源摄影测量框架 Meshroom 中。具体整合的组件包括：完整的光度立体生态（标定、自标定和通用模式）、自动对象掩膜，以及多视图法线与反射率整合。由此，系统在计算机视觉研究代码与实际文化遗产应用之间提供了一个中间软件层，使近期技术更易于使用和评估。

### 主要贡献
- 将多视图、多光照表面重建的先进计算机视觉组件集成到 Meshroom 这一开源摄影测量框架中。
- 集成内容涵盖完整光度立体生态（标定、自标定、通用）、自动对象掩膜，以及多视图法线与反射率整合。
- 不提出新重建算法，而是组装并暴露现有先进方法，形成面向遗产场景的可用工作流。
- 提供计算机视觉研究代码与文化遗产实际应用之间的中间软件层，降低近期技术的使用与评估门槛。

### 局限性
摘要未提供足够信息。论文未在摘要中给出实验细节、定量结果、与基线方法的比较、适用对象范围、对采集条件的硬性要求、运行效率或失败案例等信息。

### 阅读优先级
中。理由：该工作属于系统集成与工作流落地型贡献，而非新算法提出；若关注文化遗产数字化、光度立体与摄影测量工具链整合，具有直接参考价值。但由于摘要未提供实验验证与性能细节，若目标是评估重建精度或方法优越性，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Cultural heritage documentation increasingly relies on image-based 3D surface reconstruction, with photogrammetry software making such workflows accessible to archaeologists, conservators, and heritage technicians. These tools have been successful for conventional multi-view acquisition, but they do not routinely exploit richer multi-view, multi-light data, despite its potential for improving fine-scale surface reconstruction. This limitation is particularly relevant in heritage contexts, where controlled-light acquisition devices such as RTI domes are already used to capture illumination-varying image sets. The challenge is therefore to connect these existing acquisition practices with recent computer vision methods in a form that can be used within operational heritage workflows. In this work, we address this need by integrating state-of-the-art components from computer vision for multi-view, multi-light surface reconstruction into Meshroom, an open-source photogrammetry framework. Rather than proposing a new reconstruction algorithm, our contribution is to assemble and expose existing advanced methods, namely a complete photometric stereo ecosystem (calibrated, self-calibrated and universal), automatic object masking, and multi-view normal-and-reflectance integration, within a usable heritage-oriented workflow. The proposed system thus provides an intermediate software layer between computer vision research code and practical cultural heritage applications, making recent techniques easier to use and evaluate.

</details>

#### 2026-09-14 - LG-VLN: A Zero-Shot Vision-and-Language Navigation Framework with LangGraph State Orchestration

**Authors:** Jianhe Zhao, Yanhua Qiu, Zhiyu Zhang, Zibo Zhao, Jinhua Xie
**Links:** [abs](https://arxiv.org/abs/2609.15098) - [pdf](https://arxiv.org/pdf/2609.15098)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, pose estimation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LG-VLN: A Zero-Shot Vision-and-Language Navigation Framework with LangGraph State Orchestration
- 作者：Jianhe Zhao, Yanhua Qiu, Zhiyu Zhang, Zibo Zhao, Jinhua Xie
- 出版日期：2026-09-14T06:23:31Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次级分类
- 链接：摘要页 https://arxiv.org/abs/2609.15098 ；PDF https://arxiv.org/pdf/2609.15098

### 一句话总结
LG-VLN 是一个仅用单目 RGB 的零样本连续环境视觉语言导航框架，通过共享视觉特征与基于 LangGraph 的状态编排，在 R2R-CE val-unseen 的固定 550 回合子集上取得 21.3% 成功率和 12.1% SPL。

### 研究问题
论文针对连续环境视觉语言导航（VLN-CE）：需要在未见过的 3D 环境中理解自然语言指令并执行连续低层动作。摘要指出既有方法存在两方面问题：一是常依赖 LiDAR、全景相机或额外传感器；二是几何建图与语义导航使用分离的视觉表示，可能导致长轨迹上的空间—语义不一致。

### 核心思路/方法
- 提出 LG-VLN，一个单目、零样本框架，使用共享视觉特征与基于 LangGraph 的状态编排。
- 在线前馈 3D 重建网络预测深度、相机位姿和稠密点云，用于智能体位姿估计与全局地图融合。
- 几何与导航共享稠密 CleanDIFT 特征：语义一致性用于拒绝错误的帧间对应关系；目标实例约束定义视觉参考，其相似度与局部 BLIP-2 图文相关性结合，形成语义价值图。
- LangGraph 将指令解析、几何感知、语义价值更新、路径规划、动作执行和失败恢复表示为有向状态图，具备条件转移、持久状态和模块化恢复机制。

### 主要贡献
- 提出仅依赖单目 RGB 的零样本 VLN-CE 框架 LG-VLN，无需 LiDAR、全景相机或额外传感器。
- 通过共享稠密 CleanDIFT 特征缓解几何建图与语义导航之间的空间—语义不一致问题。
- 使用结合视觉相似度与 BLIP-2 图文相关性的语义价值图。
- 将导航流程建模为 LangGraph 有向状态图，包含条件转移、持久状态与失败恢复机制。
- 在 R2R-CE val-unseen 固定 550 回合子集上报告 21.3% 成功率和 12.1% SPL。
- 消融表明共享语义特征提升导航表现，结合视觉相似度与图文相关性后进一步提升。
- 摘要称代码将公开以支持可复现性。

### 局限性
- 摘要仅报告了在 R2R-CE val-unseen 的固定 550 回合子集上的结果，未提供其他数据集或完整验证集上的表现。
- 未提供与具体基线方法的逐项对比细节。
- 未提供计算开销、推理速度、实时性相关信息。
- 未提供失败案例、失败类型或恢复机制有效性的定量分析。
- 未提供消融实验的完整设置与具体数值。
- 未提供模型训练细节、是否使用预训练模型的具体配置等信息。
- 摘要未提供足够信息说明该方法在更长轨迹、更复杂指令或真实机器人平台上的泛化能力。
- 摘要未提供足够信息说明代码与模型的具体开源时间与范围。

### 阅读优先级
中。理由：该工作将零样本单目 VLN-CE、共享视觉特征和 LangGraph 状态编排结合，选题与框架设计具有一定新意，且提供了明确的定量结果与消融结论；但摘要未给出与基线的详细对比、完整实验设置和效率信息，若关注具体性能优势与工程可行性，需要阅读全文进一步确认。

</details>

<details>
<summary>Abstract</summary>

Continuous-environment vision-and-language navigation (VLN-CE) requires interpreting natural-language instructions in unseen 3D environments and executing continuous low-level actions. Existing methods often depend on LiDAR, panoramic cameras, or extra sensors; separate geometric-mapping and semantic-navigation visual representations can cause long-trajectory spatial-semantic inconsistencies. We propose LG-VLN, a monocular zero-shot framework with shared visual features and LangGraph-based state orchestration. An online feed-forward 3D reconstruction network predicts depth, camera poses, and dense point clouds for agent-pose estimation and global map fusion. Geometry and navigation share dense CleanDIFT features: semantic consistency rejects incorrect inter-frame correspondences, while target-instance constraints define visual references whose similarity combines with local BLIP-2 image-text relevance to form a semantic value map. LangGraph represents instruction parsing, geometric perception, semantic value updates, path planning, action execution, and failure recovery as a directed state graph with conditional transitions, persistent state, and modular recovery mechanisms. On a fixed 550-episode subset of the R2R-CE val-unseen split, LG-VLN achieves 21.3% success and 12.1% success weighted by path length. Ablations show shared semantic features improve navigation, further boosted by combining visual similarity and image-text relevance. Results establish shared visual representations and explicit state orchestration as effective for zero-shot VLN-CE using monocular RGB alone. Code will be publicly released for reproducibility.

</details>

#### 2026-09-10 - Visual-SLAM for the detection of hidden tomatoes in greenhouses by Hierarchical Localization and GLOMAPfor robotized harvesting

**Authors:** Fernando Cañadas-Aránega, José C. Moreno, José L. Blanco-Claraco, Francisco Rodríguez
**Links:** [abs](https://arxiv.org/abs/2609.11766) - [pdf](https://arxiv.org/pdf/2609.11766)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** structure from motion, SLAM, visual SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visual-SLAM for the detection of hidden tomatoes in greenhouses by Hierarchical Localization and GLOMAPfor robotized harvesting
- 作者：Fernando Cañadas-Aránega, José C. Moreno, José L. Blanco-Claraco, Francisco Rodríguez
- 出版日期：2026-09-10T16:19:36Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.11766 ；PDF https://arxiv.org/pdf/2609.11766

### 一句话总结
该工作提出一种面向温室番茄作物建图的低成本单目 Visual-SLAM 系统，结合 Hierarchical Localization 与基于 Structure-From-Motion 的 GLOMAP，实现对被遮挡番茄的识别与三维重建。

### 研究问题
温室内部先进的作物监测是研究中心的重点目标之一。传统上常使用 LiDAR 或立体相机等高性能传感器，但成本往往较高。论文关注的是：能否用成本显著更低的单目相机 Visual-SLAM 系统，面向农业应用（如温室番茄作物建图）完成检测与建图任务，尤其是识别被遮挡、经典视觉技术难以访问的番茄。

### 核心思路/方法
论文提出使用单目相机的 Visual-SLAM 系统，针对农业应用（温室番茄作物建图）定制。测试在 Agroconnect 实验温室的真实番茄串上进行。开发了一个 ROS 2 Humble 节点，运行在机器人上以采集作物图像，随后存储用于离线处理。为生成温室作物的三维建图模型，将基于 Structure-From-Motion 的 GLOMAP 建图器与 Hierarchical Localization 工具箱集成。系统采用基于由粗到细策略的分层定位范式：先进行全局检索以生成位置假设，再在识别出的候选区域内结合局部特征。

### 主要贡献
- 提出一种使用单目相机的 Visual-SLAM 系统，相比 LiDAR 或立体相机等方案成本显著更低，并面向农业应用定制。
- 将基于 Structure-From-Motion 的 GLOMAP 建图器与 Hierarchical Localization 工具箱集成，用于生成温室作物的三维建图模型。
- 采用由粗到细的分层定位范式：先全局检索生成位置假设，再在候选区域内结合局部特征。
- 开发 ROS 2 Humble 节点用于机器人端图像采集与离线处理。
- 结果显示能够正确识别番茄簇，并正确表征被经典视觉技术遮挡且不可访问的番茄。
- 重建的三维模型通过人工真值测量（果实大小、质心位置和朝向）进行了验证，确认了所提低成本单目流程的几何精度。

### 局限性
- 摘要未提供足够信息说明系统在更多温室场景、不同作物或更大规模环境中的泛化能力。
- 摘要未提供足够信息说明实时性能、计算资源消耗或在线运行能力。
- 摘要未提供足够信息说明与 LiDAR 或立体相机方案在精度、鲁棒性上的系统对比。
- 摘要未提供足够信息说明对光照变化、遮挡程度差异、相机运动等干扰因素的鲁棒性。
- 摘要未提供足够信息说明数据集规模、测试样本数量及统计显著性。
- 摘要仅提到该初始建图是未来更高级算法分析生长模式、优化农业管理的基础，因此面向机器人化采收的完整闭环能力在摘要中未提供足够信息。

### 阅读优先级
中。理由：该论文主题明确，聚焦低成本单目 Visual-SLAM 在温室番茄检测与三维重建中的应用，并涉及 Hierarchical Localization 与 GLOMAP 的集成，对农业机器人、三维重建和视觉定位方向有一定参考价值。但摘要未提供足够信息说明实验规模、实时性、泛化性和与高成本传感器的系统对比，若读者关注机器人化采收的完整系统或大规模验证，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Advanced crop monitoring inside greenhouses is becoming one of the primary objectives of research centers. High-performance sensors, such as LiDAR or stereo cameras, have traditionally been employed for this purpose, though these often have a high cost. This work proposes a Visual-SLAM system using a monocular camera, which is significantly more cost-effective and specifically tailored for agricultural applications, such as mapping tomato crops in a greenhouse. Tests were carried out on a real tomato bunch, located in the Agroconnect experimental greenhouse. A ROS 2 Humble node was developed to run on the robot in order to capture images of these crops, which were then stored for offline processing. To generate a 3D mapped model for the crop in the greenhouse, the GLOMAP mapper, based on Structure-From-Motion, was integrated with the Hierarchical Localization toolbox. This initial mapping is a foundation for future, more advanced algorithms to analyze growth patterns, and optimize agricultural management. The system leverages a hierarchical localization paradigm based on a coarse-to-fine strategy: it first performs global retrieval to generate location hypotheses, then combines local features within the identified candidate regions. The results show a correct identification of the tomato cluster, correctly characterising the tomato that is occluded and inaccessible by classical vision technologies. The reconstructed 3D model was further validated against manual ground-truth measurements of fruit size, centroid position, and orientation, confirming the geometric accuracy of the proposed low-cost monocular pipeline.

</details>

#### 2026-09-10 - RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting

**Authors:** Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen
**Links:** [abs](https://arxiv.org/abs/2609.11079) - [pdf](https://arxiv.org/pdf/2609.11079)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, depth estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, robot perception, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting
- 作者：Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen
- 出版日期：2026-09-10T04:36:58Z
- 分类：3D Reconstruction & Multi-view Geometry（主类别）；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次类别）
- 链接：摘要页 https://arxiv.org/abs/2609.11079 ；PDF https://arxiv.org/pdf/2609.11079

### 一句话总结
RIDE 利用 render–match–PnP 重定位中获得的稀疏度量深度观测，结合预训练视频深度模型的几何先验，从机器人 RGB 流中估计稠密度量深度。

### 研究问题
论文关注的是：render–match–PnP 重定位虽能建立查询图像像素与 3D 地图点之间的对应关系以恢复相机位姿，但其支持稠密深度估计的潜力常被忽视。RIDE 旨在利用这类几何信息，在给定度量尺度的 3D Gaussian Splatting（3DGS）模型条件下，从机器人 RGB 流中估计稠密度量深度。

### 核心思路/方法
- 以度量尺度的 3DGS 模型为基础，利用 PnP-RANSAC 内点对应关系导出稀疏度量深度观测。
- 将这些稀疏度量深度观测与预训练视频深度模型的几何先验相结合。
- 针对观测不均匀和间歇性的问题，引入全局与局部深度校正以及时间记忆机制。
- 在度量尺度初始化后，支持在短观测间隔内继续进行深度估计。
- 在公开 RGB-D 视频上训练，并在机器人序列上不做微调进行评估。

### 主要贡献
- 提出 RIDE，将重定位几何信息用于稠密度量深度估计。
- 结合 PnP-RANSAC 内点对应得到的稀疏度量深度与预训练视频深度模型的几何先验。
- 通过全局/局部深度校正与时间记忆，应对不均匀、间歇的稀疏观测，并支持短观测间隔下的深度估计。
- 实验显示，相比仅做尺度校准，RIDE 在深度精度和时间一致性上有所提升，表明定位几何可同时支持位姿恢复与稠密机器人感知。

### 局限性
摘要未提供足够信息。摘要未给出具体实验平台、序列数量、失败情形、计算开销、实时性、对 3DGS 模型质量或重定位成功率的依赖程度等细节。

### 阅读优先级
中。理由：该工作位于 3D 重建、神经场景表示与机器人/AR 应用的交叉点，核心思路明确，且强调无需微调即可在机器人序列上评估；但摘要未提供充分的实验细节与对比设置，是否值得精读取决于读者对重定位辅助稠密深度估计、3DGS 机器人感知这一具体方向的关注程度。

</details>

<details>
<summary>Abstract</summary>

Render--match--PnP relocalization establishes correspondences between query image pixels and 3D map points for camera pose recovery, but their potential to support dense depth estimation is often overlooked. To exploit this geometric information, we present RIDE, which estimates dense metric depth from a robot's RGB stream. Given a metrically scaled 3D Gaussian Splatting (3DGS) model, RIDE combines sparse metric depth observations derived from PnP-RANSAC inlier correspondences with the geometric prior of a pretrained video-depth model. To handle uneven and intermittent observations, it integrates global and local depth correction with temporal memory, supporting depth estimation through short observation gaps after metric scale initialization. Trained on public RGB-D videos, RIDE is evaluated on robot sequences without fine tuning. Experiments show improved depth accuracy and temporal consistency over scale-only calibration, demonstrating how localization geometry can support both pose recovery and dense robot perception.

</details>

#### 2026-09-09 - GRADE: Single-Frame Generative Radar Depth Estimation Under Visual Degradation

**Authors:** Bin Zhao, Patrick Chiou, Nakul Garg
**Links:** [abs](https://arxiv.org/abs/2609.10756) - [pdf](https://arxiv.org/pdf/2609.10756)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GRADE: Single-Frame Generative Radar Depth Estimation Under Visual Degradation
- 作者：Bin Zhao, Patrick Chiou, Nakul Garg
- 出版日期：2026-09-09T18:57:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.10756

### 一句话总结
GRADE 将预训练生成先验与单帧雷达几何相融合，在烟雾、雾气和黑暗等视觉退化条件下实现高保真度量深度估计。

### 研究问题
在烟雾、雾气和黑暗等条件下，光学传感器无法穿透空气中的颗粒物，导致密集 3D 深度感知失效。毫米波雷达在这些条件下仍可使用并能准确测距，但其小孔径限制了角分辨率。论文旨在解决：如何在视觉退化条件下，利用单帧雷达几何与生成先验估计高保真度量深度。

### 核心思路/方法
GRADE 首先将原始 4D 雷达频谱映射为粗略的度量深度。随后，一个潜在扩散骨干网络在恢复结构细节的同时，将每个去噪步骤都条件化在该深度估计上。一个像素空间适配器在有可用信息时利用残余相机线索，并在清晰、烟雾退化和遮挡输入上进行训练，使得随着能见度下降，整体输出趋近于雷达条件化路径。

### 主要贡献
- 提出 GRADE，将预训练生成先验锚定在单帧雷达几何中，用于估计高保真度量深度。
- 设计了两阶段方法：先将原始 4D 雷达频谱映射为粗略度量深度，再通过潜在扩散骨干网络恢复结构细节并条件化每一去噪步骤。
- 引入像素空间适配器，利用残余相机线索，并在清晰、烟雾退化和遮挡输入上训练，使输出随能见度下降趋近雷达条件化路径。
- 在 12 栋建筑约 95K 帧（含真实烟雾）上训练与评估，清晰场景 MAE 为 0.303 m，烟雾下为 0.313 m，优于现有基线。
- 代码与数据集已公开。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对视觉退化条件下的深度感知这一明确难题，结合雷达与生成先验，给出了具体量化结果，且涉及 3D 重建与多视角几何方向，摘要信息显示其方法路径与评估结果较为完整，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Dense 3D depth perception fails under smoke, fog, and darkness because optical sensors cannot penetrate airborne particulates. mmWave radar remains usable and measures range accurately under these conditions, but its small aperture limits angular resolution. We present GRADE, which grounds a pretrained generative prior in single-frame radar geometry to estimate high-fidelity metric depth. GRADE first maps raw 4D radar spectra to coarse metric depth. A latent diffusion backbone then recovers structural detail while conditioning every denoising step on this estimate. A pixel-space adapter uses residual camera cues when available and is trained across clear, smoke-degraded, and occluded inputs so the full output approaches the radar-conditioned path as visibility degrades. Trained and evaluated on ~95K frames across 12 buildings with real smoke, GRADE achieves an MAE of 0.303 m in clear scenes and 0.313 m under smoke, outperforming existing baselines. Code and datasets are available at https://phi-lab-rice.github.io/GRADE.

</details>

#### 2026-09-09 - Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts

**Authors:** Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte
**Links:** [abs](https://arxiv.org/abs/2609.10498) - [pdf](https://arxiv.org/pdf/2609.10498)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts
- 作者：Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte
- 出版日期：2026-09-09T17:35:16Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.10498) / [PDF](https://arxiv.org/pdf/2609.10498)

### 一句话总结
该论文提出 Field Converter，通过相机与球场几何初始化球员根节点，并利用时序残差修正，实现从已标定足球转播中估计共享世界坐标系下的 3D 球员姿态。

### 研究问题
从单目体育转播中恢复 3D 人体姿态时，难点不仅在于相对自身身体的姿态重建，还在于需要将球员定位到共享的度量世界坐标系中。论文聚焦于从已标定的足球转播视频中进行世界坐标下的 3D 球员姿态估计。

### 核心思路/方法
- 使用相机和球场几何信息，通过射线-地面相交来初始化球员根节点。
- 在几何初始化基础上，预测时序残差修正。
- 残差预测使用姿态、图像、相机和几何线索。
- 在匹配不重叠的评估序列上，比较了不同时序骨干：逐帧 MLP、TCN 和 Transformer。

### 主要贡献
- 提出 Field Converter，一个几何初始化与时序残差修正结合的世界坐标 3D 球员姿态估计框架。
- 利用相机和球场几何进行根节点初始化，并通过时序残差修正降低根节点误差。
- 报告中，几何单独使根误差为 49cm，逐帧 MLP 降至 14cm，TCN 降至 10cm，Transformer 达到可比的 11cm；世界空间 MPJPE 达到 13.2cm。
- 消融显示，残差预测明显优于直接全局根节点回归；时序上下文比具体时序骨干更重要。
- 失败分析指出，空中动作是基于地面几何初始化的主要局限。

### 局限性
- 摘要明确指出失败分析发现空中动作是基于地面几何初始化的主要限制。
- 除空中动作外，其他局限性摘要未提供足够信息。
- 实验细节、数据集规模、跨场景泛化能力、计算成本等信息摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对足球转播中的世界坐标 3D 人体姿态估计，问题设定明确，且给出了根误差、MPJPE 和消融结论；如果关注体育视频分析、单目 3D 人体姿态或几何初始化方法，具有参考价值。但摘要未提供完整实验设置、数据规模和更广泛的泛化分析，是否高优先级取决于读者对足球转播场景的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Recovering 3D human pose from monocular sports broadcasts remains challenging when players must be localized in a shared metric world coordinate system rather than only reconstructed relative to their own body. We introduce Field Converter, a geometry-initialized temporal residual framework for world-grounded 3D player pose estimation from calibrated soccer broadcasts. Our method first uses camera and pitch geometry to initialize the player root through ray-ground intersection, then predicts a temporal residual correction from pose, image, camera, and geometric cues. On match-disjoint evaluation sequences, residual refinement reduces root error from 49cm with geometry alone to 14cm with a frame-wise MLP and 10cm with a TCN, while a Transformer achieves a comparable 11cm. The resulting world-space MPJPE reaches 13.2cm, and ablations show that residual prediction clearly outperforms direct global-root regression while temporal context matters more than the specific temporal backbone. Failure analysis further identifies airborne motion as the main limitation of the ground-based geometric initialization.

</details>

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-15 - ORCA: Occlusion-Aware Refinement and Completion for Novel View Synthesis

**Authors:** Weronika Jakubowska, Maciej Zięba, Przemysław Spurek
**Links:** [abs](https://arxiv.org/abs/2609.17450) - [pdf](https://arxiv.org/pdf/2609.17450)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** monocular depth, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ORCA: Occlusion-Aware Refinement and Completion for Novel View Synthesis
- 作者：Weronika Jakubowska, Maciej Zięba, Przemysław Spurek
- 出版日期：2026-09-15T16:53:54Z
- 分类：primary_category: Neural Scene Representations & Rendering；secondary_categories: 未提供
- 链接：abstract_url: https://arxiv.org/abs/2609.17450；pdf_url: https://arxiv.org/pdf/2609.17450

### 一句话总结
ORCA 提出一种遮挡感知的单图像新视角合成方法，按缺失区域的大小与结构分别处理，优先用重建场景中已有的 RGB-D 信息修复小范围去遮挡，仅在较大区域使用生成式修补，从而减少生成导致的幻觉并保持原场景内容与结构。

### 研究问题
从单张图像进行新视角合成本质上是一个存在歧义的问题：当相机偏离输入视角时，原本被遮挡的区域会变得可见，暴露出缺失的几何结构和重建场景中的空洞。现有方法通常依赖生成模型来补全这些区域，但摘要指出，许多伪影其实只是深度边界附近的小缝隙，并不需要生成新的场景内容。因此，问题在于如何避免对生成式修补的过度依赖，同时有效处理探索过程中出现的缺失区域。

### 核心思路/方法
ORCA 是一种遮挡感知的方法，用于从单张图像重建并补全可探索的 3D 场景。

- 首先，ORCA 利用单目深度将 3D 结构引入高斯锚点（Gaussian-anchor）表示中，同时保留原始相机-射线对应关系。
- 在场景探索过程中，缺失区域根据其大小和结构进行处理：小范围去遮挡利用重建中已有的 RGB-D 信息进行修复；生成式修补仅保留给无法从场景中可靠恢复的较大区域。
- 新的高斯锚点会被添加并进行局部优化，而不修改已有的表示。

### 主要贡献
- 提出 ORCA，一种遮挡感知的单图像新视角合成方法，能够重建并补全可探索的 3D 场景。
- 通过区分小范围去遮挡与大范围缺失，减少对生成式修补的不必要依赖，从而限制生成引发的幻觉，并更好地保留原始场景的内容与结构。
- 在 DIV2K 上，ORCA 在所有报告指标上优于 VistaDream，MUSIQ 从 61.60 提升至 68.71，CLIP-IQA 从 0.474 提升至 0.574。
- 结果表明，许多新视角伪影可以通过复用重建场景中已有的信息来有效修复。

### 局限性
摘要未提供足够信息说明 ORCA 的局限性，例如方法对深度估计误差的敏感性、生成式修补在较大区域中的失败情况、计算成本、对其他数据集的泛化能力等，均未在摘要中提及。

### 阅读优先级
高。理由：该论文针对单图像新视角合成中遮挡区域处理这一核心问题，提出了明确的遮挡感知策略，并在 DIV2K 上给出了相对 VistaDream 的量化提升；方法思路与高斯锚点表示、单目深度和生成式修补的取舍直接相关，对神经场景表示与渲染方向的研究具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Novel-view synthesis from a single image is a fundamentally ambiguous problem. As the camera moves away from the input viewpoint, previously hidden regions become visible, exposing missing geometry and holes in the reconstructed scene. Existing methods often rely on generative models to complete such regions. However, many of these artifacts are small gaps near depth boundaries and do not require generating new scene content. In order to eliminate expensive process of generating image we introduce ORCA, an occlusion-aware method for reconstructing and completing explorable 3D scenes from a single image. ORCA first introduces 3D structure into a Gaussian-anchor representation using monocular depth while preserving the original camera-ray correspondence. During scene exploration, missing regions are handled based on their size and structure. Small disocclusions are repaired using RGB-D information already available in the reconstruction, while generative inpainting is reserved for larger regions that cannot be reliably recovered from the scene. New Gaussian anchors are added and optimized locally without modifying the existing representation. By reducing unnecessary reliance on generative inpainting, ORCA limits generation-induced hallucinations and better preserves the content and structure of the original scene. On DIV2K, ORCA improves novel-view quality over VistaDream across all reported metrics, increasing MUSIQ from 61.60 to 68.71 and CLIP-IQA from 0.474 to 0.574. These results show that many novel-view artifacts can be repaired effectively by reusing information already present in the reconstructed scene.

</details>

#### 2026-09-15 - PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM

**Authors:** Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang
**Links:** [abs](https://arxiv.org/abs/2609.17387) - [pdf](https://arxiv.org/pdf/2609.17387)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, differentiable rendering, rendering, splatting, robotics, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM
- 作者：Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang
- 出版日期：2026-09-15T16:26:12Z
- 分类：Neural Scene Representations & Rendering（主分类）；3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications（次分类）
- 链接：[摘要](https://arxiv.org/abs/2609.17387) / [PDF](https://arxiv.org/pdf/2609.17387)

### 一句话总结
PanoGS-SLAM 是首个基于 3D Gaussian Splatting 的全景稠密 SLAM 系统，通过在球面域内进行可微渲染与位姿优化，利用全向光度约束提升跟踪稳定性，并在真实与合成全景基准上取得优于几何与 GS 类基线的性能。

### 研究问题
实时稠密 SLAM 是机器人在动态或快速变化环境中进行鲁棒定位与高质量建图的核心能力。现有基于 3DGS 的 SLAM 方法大多面向窄视场（narrow-FoV）针孔相机，角度覆盖有限削弱了位姿可观测性，在快速运动和大视角变化下常导致光度优化不稳定。本文试图解决：如何在全景（全向）感知几何下构建稠密 3DGS SLAM，以增强位姿可观测性与优化稳定性。

### 核心思路/方法
- 直接在球面域中执行可微渲染与位姿优化，提供全向光度约束，从而获得更稳定的跟踪。
- 引入球面一致的光度损失（sphere-consistent photometric loss），以补偿等距柱状投影（equirectangular projection）带来的面积畸变。
- 提出深度引导的高斯初始化策略（depth-guided Gaussian initialization），以稳定新观测区域的增量建图。
- 在真实与合成全景基准（PALVIO 与 SynPano）上进行实验，并与几何类及 GS 类基线比较跟踪精度与渲染质量。

### 主要贡献
- 提出 PanoGS-SLAM，被表述为首个基于 3D Gaussian Splatting 的全景稠密 SLAM 系统。
- 在球面域内完成可微渲染与位姿优化，实现全向光度约束。
- 提出球面一致光度损失以补偿等距柱状投影面积畸变；提出深度引导高斯初始化策略以稳定增量建图。
- 在 PALVIO 与 SynPano 基准上，报告其在跟踪精度与渲染质量上持续优于几何与 GS 类基线，并具备快速前端收敛与实时性能。
- 通过受控视场实验，揭示随角度覆盖增加，优化条件与收敛稳定性呈现清晰的单调改善，强调感知几何对可微高斯 SLAM 优化景观的根本作用。

### 局限性
- 摘要未提供足够信息说明方法在极端动态场景、不同全景相机标定误差或大尺度场景下的具体表现与失效条件。
- 摘要未提供足够信息说明实时性能的具体指标（如帧率、硬件平台、分辨率）与内存/计算开销。
- 摘要未提供足够信息说明与基线对比的完整实验设置、消融实验细节及定量指标数值。
- 摘要未提供足够信息说明代码公开的具体时间与范围，仅提及源代码将公开。

### 阅读优先级
高。理由：该工作定位为首个基于 3DGS 的全景稠密 SLAM，直接针对窄视场 3DGS SLAM 在快速运动与大视角变化下的优化不稳定问题；方法层面提出球面域渲染、球面一致光度损失与深度引导初始化，且摘要给出在真实与合成基准上优于基线的结论，并涉及感知几何对优化景观影响的受控实验，对神经渲染、3D 重建与机器人/AR 应用交叉方向均有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-time dense SLAM is a core capability for robotics applications that require robust localization and high- quality mapping in dynamic or fast-changing environments. Recent 3D Gaussian Splatting (3DGS)-based SLAM methods have shown promising performance, but most are designed for narrow-FoV pinhole cameras, where limited angular coverage weakens pose observability and often leads to unstable photo- metric optimization under rapid motion and large viewpoint changes. We present PanoGS-SLAM, the first panoramic dense SLAM system built on 3D Gaussian Splatting. Our method per- forms differentiable rendering and pose optimization directly in the spherical domain, enabling omnidirectional photometric constraints for more stable tracking. To improve geometric consistency and robustness, we introduce (1) a sphere-consistent photometric loss that compensates for the area distortion of equirectangular projection, and (2) a depth-guided Gaussian initialization strategy that stabilizes incremental mapping in newly observed regions. Extensive experiments on both real and synthetic panoramic benchmarks (PALVIO and SynPano) show that PanoGS-SLAM consistently outperforms geometric and GS-based baselines in tracking accuracy and rendering quality, while achieving fast front-end convergence and real-time perfor- mance. In addition, controlled field-of-view experiments reveal a clear monotonic improvement in optimization conditioning and convergence stability as angular coverage increases, high- lighting the fundamental role of sensing geometry in shaping the optimization landscape of differentiable Gaussian-based SLAM. The source code will be made publicly available.

</details>

#### 2026-09-15 - Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement

**Authors:** Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo
**Links:** [abs](https://arxiv.org/abs/2609.17039) - [pdf](https://arxiv.org/pdf/2609.17039)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement
- 作者：Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo
- 出版日期：2026-09-15T11:47:35Z
- 分类：primary_category: Neural Scene Representations & Rendering；secondary_categories: 未提供
- 链接：abstract_url: https://arxiv.org/abs/2609.17039；pdf_url: https://arxiv.org/pdf/2609.17039

### 一句话总结
Bi-FlowGS 提出用光流在生成式视图补全与 3D 高斯几何之间建立双向协同精炼，以缓解稀疏视图 3DGS 重建中的几何退化问题。

### 研究问题
稀疏视图下的 3D 高斯泼溅（3DGS）重建本质上是欠约束的。摘要指出，即使渲染结果看似合理，几何仍可能错误：高斯的位置或深度误差可能被不透明度、尺度和外观所掩盖，作者将这一失败模式称为 “Geometry Cheating”。现有正则化方法受限于已观测视图；基于视频扩散的方法虽能补全未见视图，但主要将其用作 RGB 伪监督，未能充分利用运动与时间先验，也缺乏显式几何监督。

### 核心思路/方法
- 核心桥梁：使用光流连接“生成式视图补全”和“高斯几何正则化”。
- **Video-to-Geometry Flow Distillation (V2G)**：从恢复视频中蒸馏时间对应先验到高斯几何，以缓解 Geometry Cheating，且为即插即用模块。
- **Geometry-to-Video Flow-Guided Restoration (G2V)**：反过来利用当前 3DGS 几何引导时间一致的视频恢复，从而提供更可靠的生成式监督。
- 二者共同构成隐式双向协同精炼过程，使恢复视频与优化的 3DGS 场景迭代式相互提升。
- 实验层面：摘要称在宽基线与无界 360° 基准上提升了渲染质量和几何一致性。

### 主要贡献
- 提出 Bi-FlowGS，通过光流桥接生成式视图补全与高斯几何正则化。
- 提出即插即用的 V2G，将恢复视频中的时间对应先验蒸馏到高斯几何中，以缓解 Geometry Cheating。
- 提出 G2V，用当前 3DGS 几何引导时间一致的视频恢复，提供更可靠的生成式监督。
- 将 V2G 与 G2V 组合为隐式双向协同精炼框架，使恢复视频与 3DGS 场景迭代互促。
- 摘要声称在宽基线与无界 360° 基准上改善了渲染质量与几何一致性。

### 局限性
摘要未提供足够信息。未给出具体失败场景、计算开销、对视频扩散模型质量的依赖程度、在极端稀疏视图下的表现边界，也未提供定量实验结果细节。

### 阅读优先级
高。理由：该工作针对稀疏视图 3DGS 中“渲染合理但几何错误”的关键问题提出新失败模式命名，并设计 V2G/G2V 双向流协同机制，方向明确且具方法创新性；若研究兴趣涉及稀疏视图重建、3DGS 几何正则化或生成先验与几何优化的结合，应优先阅读。

</details>

<details>
<summary>Abstract</summary>

Sparse-view 3D scene reconstruction with 3D Gaussian Splatting (3DGS) is inherently underconstrained. Plausible renderings can also coexist with erroneous Gaussian geometry, as errors in positions or depths may be concealed by opacity, scale, and appearance; we term this failure mode Geometry Cheating. Existing regularization methods constrain geometry but remain limited to observed views, while video-diffusion-based methods complete unseen views yet mainly use them as RGB pseudo-supervision, underusing motion and temporal priors and lacking explicit geometry supervision. We present Bi-FlowGS, which uses optical flow to bridge generative view completion and Gaussian geometry regularization. Our plug-and-play Video-to-Geometry Flow Distillation (V2G) distills temporal correspondence priors from restored videos into Gaussian geometry to alleviate Geometry Cheating. Conversely, Geometry-to-Video Flow-Guided Restoration (G2V) uses the current 3DGS geometry to guide temporally consistent video restoration, providing more reliable generative supervision. Together, V2G and G2V form an implicit bidirectional co-refinement process, enabling restored videos and the optimized 3DGS scene to iteratively improve each other. Experiments demonstrate improved rendering quality and geometric consistency across wide-baseline and unbounded 360° benchmarks.

</details>

#### 2026-09-14 - The Neverwhere Visual Parkour Benchmark Suite

**Authors:** Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang
**Links:** [abs](https://arxiv.org/abs/2609.16443) - [pdf](https://arxiv.org/pdf/2609.16443)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Neverwhere Visual Parkour Benchmark Suite
- 作者：Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang
- 出版日期：2026-09-14T23:50:08Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2609.16443) / [PDF](https://arxiv.org/pdf/2609.16443)

### 一句话总结
该工作提出 Neverwhere 基准套件，用超过六十个基于 3D Gaussian Splatting 重建的城市室内外场景构建高逼真闭环评估环境，以缩小视觉运动控制器的训练/评估差距，并分析仅依赖 3D Gaussian 生成数据训练的风险。

### 研究问题
当前最先进的视觉运动控制器在处理复杂视觉环境方面能力越来越强，这使得在部署前评估其真实世界性能变得越来越困难。论文试图缩小训练与评估之间的差距。摘要未提供足够信息说明该差距的具体定量表现或已有评估方法的具体缺陷。

### 核心思路/方法
- 构建一组高逼真、闭环的评估环境，即 The Neverwhere Benchmark Suite。
- 该套件包含超过六十个城市室内和室外场景的 3D Gaussian Splatting 重建。
- 目标是让基于 Gaussian splats 的重建更容易创建并集成到模拟连续测试流程中，从而促进大规模、可复现的机器人评估。
- 提供在多个 Neverwhere 场景上训练的策略检查点，并在新场景中评估其性能。
- 通过上述分析指出仅依赖 3D Gaussian 生成数据进行训练的潜在陷阱，并说明需要来源多样的数据来保证性能。

### 主要贡献
- 提出 Neverwhere Benchmark Suite：一组超过六十个基于 3D Gaussian Splatting 的城市室内外高逼真闭环评估环境。
- 旨在推动大规模、可复现的机器人评估，降低将 Gaussian splats 重建集成到模拟连续测试中的门槛。
- 提供在多个 Neverwhere 场景上训练的策略检查点，并给出其在新场景中的评估表现。
- 强调仅依赖 3D Gaussian 生成数据训练的风险，说明多样化数据来源对性能的必要性。

### 局限性
摘要未提供足够信息说明该基准套件在场景覆盖、评估指标、计算成本、真实机器人迁移效果或策略检查点具体性能数值等方面的局限。

### 阅读优先级
高。理由：该工作直接针对视觉运动控制器在复杂视觉环境中的真实世界部署前评估难题，提供大规模高逼真闭环基准套件，并讨论仅用 3D Gaussian 生成数据训练的潜在陷阱；如果研究兴趣涉及机器人视觉运动控制、闭环评估、3D Gaussian Splatting 在机器人仿真中的应用，该论文具有较高参考价值。摘要未提供足够信息说明其具体实验规模和指标细节，但主题与主分类和机器人评估紧密相关。

</details>

<details>
<summary>Abstract</summary>

State-of-the-art visual locomotion controllers are increasingly capable at handling complex visual environments, making evaluating their real-world performance before deployment increasingly difficult. This work intends to narrow this train/evaluation gap by developing a collection of hyper-photo-realistic, closed-loop evaluation environments - The Neverwhere Benchmark Suite - comprised of over sixty 3D Gaussian Splatting reconstructions of urban indoor and outdoor scenes. Our goal is to encourage large-scale and reproducible robot evaluation by making it easier to create and integrate Gaussian splats-based reconstructions into simulated continuous testing setups. We also underscore the potential pitfalls of relying exclusively on 3D Gaussian-generated data for training, by providing policy checkpoints trained over multiple Neverwhere scenes and their performance when evaluated in novel scenes. Our analysis illustrates the necessity of sourcing diverse data to ensure performance. Code and data are available on the project page: https://ziyc.github.io/neverwhere-bench/.

</details>

#### 2026-09-14 - G-ray: Ray-Level Relative Geometric Position Encoding in Multi-View Vision Transformers under Camera Heterogeneity

**Authors:** Shuo Zhang, Xin Su, Wei Wang, Jun Liu, Xinrui Zeng, Yongsen Chen, Chenjie Wang, Guibo Zhu, Jinqiao Wang, Bin Luo, Liangpei Zhang
**Links:** [abs](https://arxiv.org/abs/2609.15018) - [pdf](https://arxiv.org/pdf/2609.15018)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** pointmap, 3D reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G-ray: Ray-Level Relative Geometric Position Encoding in Multi-View Vision Transformers under Camera Heterogeneity
- 作者：Shuo Zhang, Xin Su, Wei Wang, Jun Liu, Xinrui Zeng, Yongsen Chen, Chenjie Wang, Guibo Zhu, Jinqiao Wang, Bin Luo, Liangpei Zhang
- 出版日期：2026-09-14T04:30:34Z
- 分类：Neural Scene Representations & Rendering（主要分类；次要分类未提供）
- 链接：摘要页 https://arxiv.org/abs/2609.15018 ；PDF https://arxiv.org/pdf/2609.15018 ；项目页 https://g-ray-project.github.io/

### 一句话总结
论文提出 G-ray，一种以相机局部光线角度参数化旋转相位的“光线级”相对位置编码，旨在让多视角视觉 Transformer 在相机异构（视场角、投影模型不同）条件下获得投影不变的位置一致性。

### 研究问题
多视角视觉 Transformer 在相机异构场景（例如视场角不同或投影模型不同）下的相对位置编码问题。现有旋转式相对位置编码通常使用图像平面位置坐标，会产生依赖投影的相对相位，从而在跨投影注意力中给出不一致的几何线索。

### 核心思路/方法
G-ray 的核心是将旋转相位用“相机局部光线角度”来参数化，而非图像平面坐标。这样，同一对相机局部光线在不同投影下会产生相同的相对相位，从而提供投影不变的位置一致性。G-ray 可以直接使用，也可以与现有编码集成，在不需要额外可学习参数的情况下保留互补的几何线索。论文在三种宿主编码（RoPE、GTA、RayRoPE）中验证 G-ray，任务涵盖 3D 重建和新视角合成（NVS）。

### 主要贡献
- 提出 G-ray：一种光线级相对位置编码，旋转相位由相机局部光线角度参数化，从而在跨投影时保持相对相位一致。
- 强调投影不变的位置一致性：同一相机局部光线对在不同投影下诱导相同相对相位。
- 具备使用灵活性：G-ray 可直接使用，也可与现有编码集成，且不增加额外可学习参数，保留互补几何线索。
- 在三种宿主编码 RoPE、GTA、RayRoPE 上验证，覆盖 3D 重建与 NVS。
- 实验结果（摘要所述）：在三个异构 3D 重建基准、50 视角设置下，G-ray 在全部六项平均指标上领先，并将平均 pointmap 相对误差相比 MapAnything 降低 45.8%（两者均提供标定）。
- 泛化表现（摘要所述）：仅在均匀针孔图像上训练的 3D 重建模型，无需重训练即可处理混合针孔与非针孔输入，并在均匀针孔 3D 重建协议上保持竞争力。
- NVS 方面（摘要所述）：在视点与视场角联合变化下，GTA 与 RayRoPE 结合 G-ray 后取得提升。

### 局限性
- 摘要未提供足够信息说明 G-ray 在何种条件下会失效或性能下降。
- 摘要未提供足够信息说明其计算开销、内存占用或推理速度。
- 摘要未提供足够信息说明除 RoPE、GTA、RayRoPE 外，G-ray 是否适用于其他位置编码或更广泛的 Transformer 架构。
- 摘要未提供足够信息说明非针孔投影类型的具体覆盖范围、极端视场角或强畸变条件下的表现。
- 摘要未提供足够信息说明 45.8% 误差降低所对应基准、指标定义、消融设置及统计显著性。
- 摘要未提供足够信息说明 NVS 提升的量化幅度与具体实验配置。

### 阅读优先级
高。理由：该论文针对多视角视觉 Transformer 在相机异构下的相对位置编码提出明确的新方法 G-ray，问题定义清晰，且摘要给出了跨三种宿主编码、3D 重建与 NVS 的验证，并报告了具体误差降低比例（45.8%）与无需重训练处理混合投影输入的泛化表现，对神经场景表示、多视角 Transformer 与异构相机几何相关研究方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We study relative position encoding for multi-view vision Transformers under camera heterogeneity, including varying fields of view (FoVs) or projection models. Existing rotary relative position encodings commonly use image-plane positional coordinates, producing projection-dependent relative phases and inconsistent geometric cues for cross-projection attention. We introduce G-ray, a ray-level relative position encoding whose rotary phases are parameterized by camera-local ray angles. The same camera-local ray pair induces the same relative phase across projections, providing projection-invariant positional consistency. G-ray can be used directly or integrated with existing encodings, retaining complementary geometric cues without additional learned parameters. We validate G-ray in three host encodings, RoPE, GTA, and RayRoPE, across 3D reconstruction and novel-view synthesis (NVS). Across three heterogeneous 3D reconstruction benchmarks at 50 views, G-ray leads all six averaged metrics and reduces mean pointmap relative error by 45.8% over MapAnything, with calibration supplied to both. Trained exclusively on homogeneous pinhole images, the 3D reconstruction model handles mixed pinhole and non-pinhole inputs without retraining and remains competitive on homogeneous pinhole 3D reconstruction protocols. For NVS, GTA and RayRoPE improve with G-ray under joint viewpoint and FoV variation. The project's webpage is available at https://g-ray-project.github.io/.

</details>

#### 2026-09-14 - HydroMap: Probabilistic Water Surface Elevation Mapping for Semantic Scene Representation in Inland Waterways

**Authors:** Zhongbi Luo, Yunjia Wang, Herman Bruyninckx, Peter Slaets
**Links:** [abs](https://arxiv.org/abs/2609.14903) - [pdf](https://arxiv.org/pdf/2609.14903)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, scene representation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HydroMap: Probabilistic Water Surface Elevation Mapping for Semantic Scene Representation in Inland Waterways
- 作者：Zhongbi Luo, Yunjia Wang, Herman Bruyninckx, Peter Slaets
- 出版日期：2026-09-14T01:46:04Z
- 分类：主分类为 Neural Scene Representations & Rendering；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.14903 ；PDF https://arxiv.org/pdf/2609.14903

### 一句话总结
HydroMap 是一个与里程计解耦的框架，利用双目观测重建水面高程，并将其与结构地图融合为持续的概率高程图及统一的 2.5D 语义表示，以补足 LiDAR 建图中缺失的水面信息。

### 研究问题
在内河航道运行的水面自主车辆需要同时持续表示周围结构和水面。基于 LiDAR 的同时定位与建图往往产生稀疏或缺失的水面回波，导致这一可操作表面在重建场景中缺失。论文要解决的就是如何在 LiDAR 结构地图之外，持续、概率化地重建水面高程，并进一步形成包含水面、边界、结构和上方区域的统一语义表示。

### 核心思路/方法
HydroMap 是一个与里程计解耦的框架：从双目观测中重建水面高程，并将其与结构地图集成。每一帧的水面点与传播的双目不确定性和位姿不确定性一起，形成联合的栅格观测；连续观测被融合进一个持续的概率高程图。随后，语义地图转换将高程图与结构几何结合，形成统一的水面、边界、结构和上方区域的 2.5D 表示。

### 主要贡献
- 提出 HydroMap，一个与里程计解耦的框架，用于从双目观测重建水面高程并与结构地图集成。
- 将每帧水面点与传播的双目和位姿不确定性结合为联合栅格观测，并将连续观测融合为持续的概率高程图。
- 通过语义地图转换，将高程图与结构几何结合为水面、边界、结构和上方区域的统一 2.5D 表示。
- 在 Pohang Canal 和 Leuven Vaart 数据集上，相对于同一地图坐标系下的 LiDAR 参考，高程 RMSE 保持在 5 cm 以下；高程图和语义图分别以 2 Hz 和 1 Hz 发布。
- 以持续的水面表示补充 LiDAR 地图，服务于内河航道的下游导航。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败情形、对特定传感器或数据集的依赖程度、计算开销、实时性上限、在更复杂水域或恶劣条件下的表现，也未提供与替代方法的完整对比。

### 阅读优先级
中。理由：该工作面向内河航道自主水面车辆的场景表示，问题明确，且给出了定量精度与发布频率；但摘要未展开方法细节、对比实验和局限性，是否值得深入阅读取决于读者对水面高程建图、概率地图融合或内河机器人导航的具体关注程度。

</details>

<details>
<summary>Abstract</summary>

Autonomous surface vehicles operating in inland waterways require a persistent representation of both surrounding structures and the water surface. LiDAR-based simultaneous localization and mapping often produces sparse or missing water returns, leaving this operational surface absent from the reconstructed scene. We propose HydroMap, an odometry-decoupled framework that reconstructs water surface elevation from stereo observations and integrates it with the structural map. Per-frame water points form joint cell observations with propagated stereo and pose uncertainty, and successive observations are fused into a persistent probabilistic elevation map. Semantic map conversion then combines the elevation map with structural geometry in a unified 2.5D representation of water, boundaries, structures, and overhead regions. On the Pohang Canal and Leuven Vaart datasets, the elevation RMSE remains below 5 cm relative to LiDAR references expressed in the same map frame. The elevation and semantic maps are published at 2 Hz and 1 Hz, respectively. HydroMap thereby complements LiDAR maps with a persistent representation of the water surface for downstream navigation in inland waterways.

</details>

#### 2026-09-14 - What Makes a 3D Scene Editable? A Factorized Benchmark of Fidelity, Locality, Consistency, and Preservation

**Authors:** Sariah Patro, Arjun Mehra, Nikhil Bhatia
**Links:** [abs](https://arxiv.org/abs/2609.14899) - [pdf](https://arxiv.org/pdf/2609.14899)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：What Makes a 3D Scene Editable? A Factorized Benchmark of Fidelity, Locality, Consistency, and Preservation
- 作者：Sariah Patro, Arjun Mehra, Nikhil Bhatia
- 出版日期：2026-09-14T01:38:38Z
- 分类：Neural Scene Representations & Rendering（主要分类；次要分类未提供）
- 链接：摘要页 https://arxiv.org/abs/2609.14899 ；PDF https://arxiv.org/pdf/2609.14899

### 一句话总结
论文提出 EditBench3D——一个与表示无关的神经 3D 场景编辑基准，将编辑视为受控的信息替换，并指出语义保真度与其他编辑属性仅弱相关，没有单一方法在所有维度上最优。

### 研究问题
当前神经 3D 场景编辑常仅以语义对齐（semantic alignment）作为评价标准，但一个看似合理的结果可能改动了无关内容，或在不同视角之间变得不一致。因此，论文追问：什么使一个 3D 场景真正“可编辑”？需要从哪些互补属性来刻画编辑质量？

### 核心思路/方法
- 将编辑形式化为**受控的信息替换**（controlled information replacement），并构建表示无关（representation-agnostic）的基准 EditBench3D。
- 评估四个互补属性：指令保真度（instruction fidelity）、空间局部性（spatial locality）、跨视角一致性（cross-view consistency）、非目标内容保持（preservation of non-target content）。
- 评测协议结合：可见性感知的 3D 目标支持（visibility-aware 3D target supports）、成对描述（paired descriptions）、留出相机（held-out cameras），以及覆盖外观、材质、几何和物体级变化的五类编辑族（five edit families）。
- 在 240 个场景-编辑对上，评估八种代表性编辑器，涵盖 NeRF、3D Gaussian Splatting、混合方法以及基于代理（proxy-based）的方法。
- 结论：语义保真度与其他编辑属性仅弱相关；没有任何单一方法在所有维度上最优。显式高斯编辑器整体平衡性较强，而直接代理操纵提供最保守的编辑，代价是开放式保真度受限。

### 主要贡献
- 提出 EditBench3D：一个表示无关的 3D 场景编辑基准，将编辑评价从单一语义对齐扩展为多目标刻画。
- 给出四维评价协议及配套评测设计（可见性感知目标支持、成对描述、留出相机、五类编辑族）。
- 在 240 个场景-编辑对上对八类代表性编辑器进行实证比较，揭示语义保真度与其他编辑属性弱相关、且不存在全维度最优方法。
- 主张将“可编辑性”作为多目标画像（multi-objective profile）报告，而非单一语义分数。

### 局限性
摘要未提供足够信息。摘要未说明基准的场景来源、评测指标的具体计算方式、八种编辑器的具体名称或配置、统计显著性与误差分析、以及对基准本身偏差或覆盖范围的局限讨论。

### 阅读优先级
高。理由：该论文直接针对 3D 场景编辑评价体系提出可操作的分解框架与实证结论，指出“语义分数不等于可编辑性”，对关注神经 3D 编辑评测方法、基准设计或方法比较的研究者具有较高的参考价值；但具体实验细节需查阅原文确认。

</details>

<details>
<summary>Abstract</summary>

Neural 3D scene editing is often evaluated by semantic alignment alone, although a convincing result may alter unrelated content or become inconsistent across views. We introduce EditBench3D, a representation-agnostic benchmark that treats editing as controlled information replacement. It evaluates four complementary properties: instruction fidelity, spatial locality, cross-view consistency, and preservation of non-target content. The protocol combines visibility-aware 3D target supports, paired descriptions, held-out cameras, and five edit families covering appearance, material, geometry, and object-level changes. We evaluate eight representative NeRF, 3D Gaussian Splatting, hybrid, and proxy-based editors on 240 scene-edit pairs. The study shows that semantic fidelity is only weakly associated with the other editing properties, and that no single method is optimal across all dimensions. Explicit Gaussian editors offer a strong overall balance, whereas direct proxy manipulation provides the most conservative edits at the cost of open-ended fidelity. These findings support reporting editability as a multi-objective profile rather than a single semantic score.

</details>

#### 2026-09-13 - Gaussian Process Implicit Surfaces as Participating Media: Realization-Free Rendering from Level-Crossing Statistics

**Authors:** Jack Cui, Kehan Xu, Eugene d'Eon, Wojciech Jarosz
**Links:** [abs](https://arxiv.org/abs/2609.14695) - [pdf](https://arxiv.org/pdf/2609.14695)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Process Implicit Surfaces as Participating Media: Realization-Free Rendering from Level-Crossing Statistics
- 作者：Jack Cui, Kehan Xu, Eugene d'Eon, Wojciech Jarosz
- 出版日期：2026-09-13T17:52:57Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.14695 ；PDF：https://arxiv.org/pdf/2609.14695

### 一句话总结
论文提出一种连接高斯过程隐式曲面（GPIS）与参与介质的散射理论，通过 Kac–Rice 水平穿越公式与局部条件近似，从点态 GPIS 统计量直接推导出各向异性辐射传输方程（RTE），并实现无需采样具体实现（realization-free）的渲染。

### 研究问题
如何从 GPIS 的点态统计量出发，建立其与参与介质之间的双向理论联系，从而在不生成具体几何实现的情况下进行渲染，并统一粗糙表面、多孔与非高度场几何以及参与介质等情形；同时反向构建与兼容 RTE 参数对应的 GPIS 家族，使已有体数据资产可渲染为 GPIS。

### 核心思路/方法
- 在局部条件近似下应用 Kac–Rice 水平穿越公式，从点态 GPIS 统计量直接导出完整各向异性 RTE。
- 使用共享投影面积耦合消光与散射，保证 GPIS 与其体积表示之间的几何一致性。
- 由同一统计结构导出支持面内与面外各向异性的全球 Beckmann 与 GGX 法线分布函数，并证明可退化为 SGGX、Beckmann、GGX 特例，且支持精确的可见法线重要性采样。
- 推导解析的遮蔽–阴影函数与镜面微表面单次散射模型，并扩展到多次散射。
- 在高度场极限下，证明局部条件近似退化为 Smith 独立性假设。
- 反向方向：刻画与兼容 RTE 参数对应的 GPIS 家族，并针对异质密度场开发实用的提升方法，使已有体数据资产可渲染为 GPIS；训练好的辐射场重建可无需网格提取地产出表面几何与着色法线，并以密度形式表示几何不确定性。

### 主要贡献
- 建立 GPIS 与参与介质之间双向联系的光散射理论。
- 从点态 GPIS 统计量直接导出完整各向异性 RTE，且消光与散射通过共享投影面积保持几何一致。
- 提出无需生成具体实现的渲染方式，相对基于实现的方法提升渲染效率，并可在标准体积渲染器中实现。
- 导出全球 Beckmann 与 GGX 法线分布函数，可退化为 SGGX、Beckmann、GGX，并支持精确可见法线重要性采样。
- 给出解析遮蔽–阴影函数与单次散射表面模型，并扩展到多次散射。
- 证明高度场极限下局部条件近似等价于 Smith 独立性假设。
- 反向刻画兼容 GPIS 家族，提出异质密度场的实用提升方法，使已有体数据资产可渲染为 GPIS，并让训练好的辐射场重建无需网格提取即可给出表面几何、着色法线与基于密度的几何不确定性表示。

### 局限性
摘要未提供足够信息。摘要未提及该方法的计算开销、数值稳定性、对特定 GPIS 核或统计假设的依赖、实现细节、实验对比范围及失败情形等局限。

### 阅读优先级
高。理由：该工作涉及神经场景表示与渲染中的核心问题，提出 GPIS 与参与介质的双向理论连接、无需实现的渲染路径以及对 SGGX/Beckmann/GGX 的统一与退化关系，并覆盖正向渲染与反向提升两类任务；对关注隐式曲面、体积渲染、辐射传输与各向异性微表面模型的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We present a theory of light scattering that connects Gaussian Process Implicit Surfaces (GPISes) and participating media in both directions. Applying the Kac--Rice level-crossing formula under a local-conditioning approximation yields a complete anisotropic radiative transfer equation (RTE) directly from pointwise GPIS statistics. A shared projected area couples extinction and scattering, ensuring geometric consistency between the GPIS and its volumetric representation. The framework spans rough surfaces, porous and non-height-field geometries, and participating media. From the same statistical structure, we derive full-sphere Beckmann and GGX normal distribution functions supporting in-plane and out-of-plane anisotropy. These families provably recover SGGX, Beckmann, and GGX as special cases and admit exact visible-normal importance sampling. We also derive analytic masking--shadowing functions and single-scattering surface models for specular microsurfaces, with extensions to multiple scattering. In the height-field limit, we prove that the local-conditioning approximation reduces to Smith's independence assumption. Our realization-free approach improves rendering efficiency over realization-based methods and can be implemented within a standard volume renderer. In the inverse direction, we characterize families of GPISes corresponding to compatible RTE parameters and develop practical lifts for heterogeneous density fields. Existing volumetric assets thereby become renderable as GPISes, while trained radiance-field reconstructions yield surface geometry and shading normals without mesh extraction and provide a density-based representation of geometric uncertainty.

</details>

#### 2026-09-10 - 3D Point Splatting for mmWave Radar Novel View Synthesis

**Authors:** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar
**Links:** [abs](https://arxiv.org/abs/2609.11894) - [pdf](https://arxiv.org/pdf/2609.11894)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D Point Splatting for mmWave Radar Novel View Synthesis
- 作者：Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar
- 出版日期：2026-09-10T17:52:17Z
- 分类：Neural Scene Representations & Rendering（主分类）；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2609.11894 ；PDF https://arxiv.org/pdf/2609.11894

### 一句话总结
论文提出 3DPS——首个面向毫米波雷达的可微点渲染器，直接从雷达方程立体角形式推导，以复数相位输出实现与格式无关的新视角合成，在保持物理保真度的同时将训练时间压缩到单卡约 3 分钟/场景。

### 研究问题
毫米波雷达新视角合成（NVS）需要一个同时满足三个性质的渲染器：物理忠实、复数值、多视角可优化。摘要指出此前没有方法能同时具备这三点：
- 可微蒙特卡洛（MC）光线追踪器直接实现雷达前向模型，具有显式材质建模和复数输出，但无法扩展到 NVS 所需的多视角优化规模；
- 从光学 NVS 移植的 NeRF、哈希网格和 3D 高斯训练快，但丢弃了相位，并以不透明的学习特征替代显式材质建模，因此只限于功率域的距离-方位（RA）幅度。

### 核心思路/方法
- 从雷达方程的标准立体角形式直接推导出可微点渲染器 3DPS。
- 每个有向 3D 点携带 ITU-R P.2040 材质模型，并以闭式求值。
- 将得到的复数相量通过预计算的点扩散函数（PSF）splat 到距离单元中。
- 复数输出使渲染器与下游输出格式无关：同一个优化后的场景可通过标准 FFT 流水线产出 ADC、复数距离剖面（CRP）和 RA 输出，无需针对每种格式重新训练。

### 主要贡献
- 提出 3DPS，据摘要所述为首个面向雷达的可微点渲染器。
- 从雷达方程立体角形式直接推导，赋予渲染器物理忠实性。
- 通过 ITU-R P.2040 材质模型与闭式复数相量计算，兼顾显式材质建模与复数输出。
- 借助复数输出实现格式无关性，一套优化场景即可支持 ADC、CRP、RA 多种输出。
- 在六个户外 ColoRadar 场景上，持出 RA 图像达到 0.587 的平均皮尔逊相关，为三个光学 NVS 基线（RadarSplat、Radar Fields、DART）的 1.7 倍至 5.2 倍；单张 RTX 4090 上每场景训练约 3 分钟。

### 局限性
- 摘要未提供足够信息说明方法在非户外场景、其他雷达频段或不同硬件条件下的泛化表现。
- 摘要未提供足够信息说明 3DPS 在 ADC、CRP 输出上的定量评估结果，仅给出 RA 图像的皮尔逊相关指标。
- 摘要未提供足够信息说明与 MC 光线追踪器在物理保真度上的直接定量对比。
- 摘要未提供足够信息说明多视角优化中视角数量、稀疏度或场景规模对性能的影响。
- 摘要未提供足够信息说明 0.587 平均皮尔逊相关的方差、逐场景分布或失败案例。
- 摘要未提供足够信息说明材质模型参数是否可学习、初始化方式或对 ITU-R P.2040 假设的敏感性。

### 阅读优先级
中。理由：雷达 NVS 属于相对专门的方向，但该工作提出的“物理忠实 + 复数 + 多视角可训练”三性合一问题定位清晰，且报告了显著的相对基线提升与极短训练时间；若关注可微渲染、雷达感知或 NeRF/3D 高斯之外的非光学传感器 NVS，则值得优先阅读。由于摘要未给出代码、完整实验设置与 ADC/CRP 定量结果，是否精读可待正文确认。

</details>

<details>
<summary>Abstract</summary>

Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-view optimization NVS demands. Optical-NVS ports of NeRF, hash grids, and 3D Gaussians train fast but discard phase and replace explicit material modeling with opaque learned features, restricting them to power-only range-azimuth (RA) magnitudes. We propose 3D Point Splatting (3DPS), the first differentiable point renderer for radar, derived directly from the standard solid-angle form of the radar equation. Each oriented 3D point carries an ITU-R P.2040 material model, evaluated in closed form, with the resulting complex phasor splatted into range bins through a precomputed point spread function (PSF). The complex-valued output makes the renderer product-agnostic. The same optimized scene yields analog-to-digital converter (ADC), complex range profile (CRP), and RA outputs through standard fast Fourier transform (FFT) pipelines without retraining for each format. On six outdoor ColoRadar scenes, 3DPS reaches 0.587 mean Pearson correlation on held-out RA images. This is between 1.7x and 5.2x the three optical-NVS baselines (RadarSplat, Radar Fields, DART). Training takes approximately 3 minutes per scene on a single RTX 4090.

</details>

#### 2026-09-10 - Hologram Representation via Quadratic Phase Gaussian Splatting

**Authors:** Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu
**Links:** [abs](https://arxiv.org/abs/2609.11434) - [pdf](https://arxiv.org/pdf/2609.11434)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hologram Representation via Quadratic Phase Gaussian Splatting
- 作者：Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu
- 出版日期：2026-09-10T12:06:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.11434) / [PDF](https://arxiv.org/pdf/2609.11434)

### 一句话总结
该论文提出复数域二次相位高斯（CVQPG），用可学习的二维二次相位函数替代 2D Gaussian Splatting 中的标准二维高斯表示，以提升全息重建的视觉质量。

### 研究问题
如何改进全息图表示方法，使其在重建质量上优于现有先进方法，同时保持参数高效。摘要指出，作者希望验证“调制基元的波前”是否是一种有效且轻量的全息表示增强方式。

### 核心思路/方法
- 提出 Complex-Valued Quadratic Phase Gaussian (CVQPG)。
- 将 2D Gaussian Splatting 中使用的标准二维高斯表示替换为二维二次相位函数。
- 引入额外可学习参数，用于控制这些基元的曲率。
- 通过等参数数量评估，比较该方法与现有先进方法在全息重建中的表现。
- 进行频域分析，观察自然图像中高频与中高频段的保留情况。

### 主要贡献
- 提出 CVQPG，一种新的全息图表示方法，核心是用二维二次相位函数替代标准二维高斯基元。
- 在等参数数量评估中，表明调制基元波前可作为全息表示的有效且轻量增强。
- 在全息重建视觉质量上平均超过现有先进方法：RGB 提升 +0.19 dB，灰度提升 +0.33 dB。
- 频域分析显示，CVQPG 成功保留了自然图像的中高频段。

### 局限性
摘要未提供足够信息。未说明计算开销、训练时间、数据集规模、泛化能力、硬件依赖性、失败案例或与其他表示方法的全面比较。等参数数量评估之外的其他实验设置也未在摘要中给出。

### 阅读优先级
中。理由：该工作与神经场景表示、Gaussian Splatting 和全息显示相关，提出的二次相位基元替代思路较直接，且摘要给出了明确的定量提升和频域分析；但摘要未披露数据集、实现细节和完整实验设置，是否具有广泛适用性需阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

We introduce Complex-Valued Quadratic Phase Gaussian (CVQPG), a novel hologram representation method that replaces standard 2D Gaussian representations used in 2D Gaussian Splatting with 2D quadratic phase functions. CVQPG incorporates additional learnable parameters to control the curvature of these bases. We evaluate our approach against state-of-the-art methods, exceeding the visual quality by +0.19 dB (RGB) and +0.33 dB (grayscale) on average in holographic reconstructions. Specifically, our equal parameter count evaluations show that modulating the primitive's wavefront is an effective and lightweight enhancement for hologram representations. In addition, our frequency domain analysis illustrates that CVQPG has successfully preserved the mid-to-high frequency band of natural images.

</details>

#### 2026-09-10 - Tri-DehazeGS: Scene--Medium Decoupled Gaussian Splatting with Transmittance-Aware Optimization

**Authors:** Kui Jiang, Yang Gu, Jiacheng Liu, Shiyu Liu, Youyu Chen, Hui Liu
**Links:** [abs](https://arxiv.org/abs/2609.11223) - [pdf](https://arxiv.org/pdf/2609.11223)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tri-DehazeGS: Scene--Medium Decoupled Gaussian Splatting with Transmittance-Aware Optimization
- 作者：Kui Jiang, Yang Gu, Jiacheng Liu, Shiyu Liu, Youyu Chen, Hui Liu
- 出版日期：2026-09-10T08:24:16Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.11223

### 一句话总结
Tri-DehazeGS 提出一种场景—介质解耦的高斯泼溅框架，用独立视图共享三平面场建模参与介质，并通过透射率梯度补偿优化低透射区域，以改善雾天多视角图像下的干净新视角重建。

### 研究问题
从有雾多视角图像中恢复干净三维场景具有挑战性，因为雾会衰减场景辐射并引入大气散射。现有散射感知高斯泼溅方法虽引入物理雾模型，但常在图像空间施加退化，或把介质相关变量绑定到高斯基元上，导致干净场景辐射与大气效应相互纠缠；同时低透射率区域对高斯优化提供的监督较弱，使远处或浓雾区域重建不足。

### 核心思路/方法
论文认为雾下干净重建需要同时实现场景—介质解耦与透射率感知的优化重平衡。为此提出 Tri-DehazeGS：
- 用高斯基元表示干净场景；
- 用独立的视图共享三平面场建模参与介质；
- 通过物理散射模型合成有雾观测。
此外引入 Medium-Decoupled Transmittance Gradient Compensation（MD-TGC），在介质冻结后补偿被雾抑制的梯度，且不改变前向渲染。

### 主要贡献
- 提出 Tri-DehazeGS，一个场景—介质解耦的高斯泼溅框架，将干净场景与参与介质分别表示并依据物理散射模型组合。
- 引入 MD-TGC，在介质冻结后补偿雾抑制的梯度，以重平衡低透射率区域的优化。
- 在真实与合成雾基准上实验显示，Tri-DehazeGS 改善了干净新视角重建，并提供代码链接。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算开销、对极端天气或动态场景的适用性，也未给出定量指标、消融细节或与基线方法的完整对比。

### 阅读优先级
高。理由：该论文针对雾天三维重建中场景与介质纠缠、低透射率区域监督不足两个明确问题，提出解耦表示与梯度补偿机制，属于神经场景表示与渲染方向中物理模型与高斯泼溅结合的前沿工作，且提供代码，便于复现与后续研究。

</details>

<details>
<summary>Abstract</summary>

Recovering clean 3D scenes from hazy multi-view images is challenging because haze attenuates scene radiance and introduces atmospheric scattering. Recent scattering-aware Gaussian Splatting methods introduce physical haze models into reconstruction, but they often apply degradation in image space or bind medium-related variables to Gaussian primitives, which can entangle clean scene radiance with atmospheric effects. Moreover, low-transmittance regions provide weakened supervision for Gaussian optimization, causing distant or dense-haze areas to be under-reconstructed. We argue that clean reconstruction under haze requires both scene--medium disentanglement and transmittance-aware optimization rebalancing. To this end, we propose Tri-DehazeGS, a scene--medium decoupled Gaussian Splatting framework. It represents the clean scene with Gaussian primitives, models the participating medium using an independent view-shared tri-plane field, and composes hazy observations through a physical scattering model. We further introduce Medium-Decoupled Transmittance Gradient Compensation (MD-TGC), which compensates haze-suppressed gradients after medium freezing without altering forward rendering. Experiments on real and synthetic haze benchmarks show that Tri-DehazeGS improves clean novel-view reconstruction. Code is available at https://github.com/aptx46/Tri-DehazeGS.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-15 - SWIM: Vision-Language-Grounded Soft Whole-Body Interactive Manipulation

**Authors:** Tingcong Liu, Aye Phyu Phyu Aung, Junjie Xiong, Siyi Ma, Bo An, Ke Wu, Senthilnath Jayavelu
**Links:** [abs](https://arxiv.org/abs/2609.17035) - [pdf](https://arxiv.org/pdf/2609.17035)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SWIM: Vision-Language-Grounded Soft Whole-Body Interactive Manipulation
- 作者：Tingcong Liu, Aye Phyu Phyu Aung, Junjie Xiong, Siyi Ma, Bo An, Ke Wu, Senthilnath Jayavelu
- 出版日期：2026-09-15T11:41:36Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.17035 ；PDF https://arxiv.org/pdf/2609.17035

### 一句话总结
SWIM 是一个将初始 RGB 观测与语言指令映射为完整驱动命令序列的框架，其 VLA 策略 SWIM-VLA 结合扩散动作头与 Visual Soft Proprioception（VSP），并在平面腱驱动软体机器人上评估了打包、到达与抓取任务。

### 研究问题
软体与连续体机器人通过分布式身体变形和接触实现操作，但如何将语言与视觉上下文转化为可执行的全身驱动，仍是一个基础挑战。论文关注的问题即：如何从初始 RGB 观测与语言指令出发，生成可由软体机器人物理执行的完整驱动命令序列。

### 核心思路/方法
论文提出 SWIM 框架，将初始 RGB 观测和语言指令映射为完整的驱动命令序列。其视觉-语言-动作策略 SWIM-VLA 通过 RGB 观测、语言指令与腱状态的共享表示，将扩散动作头与 Visual Soft Proprioception（VSP）结合。扩散动作头对专家命令块的条件分布进行建模；VSP 则利用仿真真值监督有序的身体锚点预测，促使表示在有限演示学习下仍保留身体几何信息。物理执行方面，依托具身机械智能执行由不断演化的仿真观测经迭代虚拟 rollout 生成的命令序列，并由内在柔顺性提供局部接触适应，而无需在线策略查询。评估任务包括平面腱驱动软体机器人上的打包、到达和抓取，其中抓取目标被锚定。

### 主要贡献
- 提出 SWIM 框架，实现从初始 RGB 观测与语言指令到完整驱动命令序列的映射。
- 提出 SWIM-VLA 策略，将扩散动作头与 Visual Soft Proprioception（VSP）通过共享表示结合，利用仿真真值监督身体锚点预测。
- 通过迭代虚拟 rollout 与内在柔顺性支持物理执行，使局部接触适应无需在线策略查询。
- 在平面腱驱动软体机器人上评估打包、到达与抓取任务：仿真中 SWIM-VLA 成功率分别为 100%、96%、88%，优于适配的 OpenVLA-OFT 基线与受控消融；硬件上 SWIM 成功率分别为 100%、80%、75%，而同一策略检查点直接在线部署分别为 75%、40%、25%。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法在更复杂任务、不同软体机器人形态、真实环境泛化性、计算开销或失败模式等方面的局限。

### 阅读优先级
高。理由：该论文针对软体机器人中语言与视觉到全身驱动的关键挑战，提出了结合扩散策略与软体本体感知的 VLA 框架，并同时给出仿真与硬件结果，且硬件上相较直接在线部署有明显提升；对具身智能、软体机器人与视觉-语言-动作方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Soft and continuum robots enable manipulation through distributed body deformation and contact, yet translating language and visual context into executable whole-body actuation remains a fundamental challenge. We present SWIM, a framework that maps an initial RGB observation and a language instruction to a complete actuation-command sequence. Its vision-language-action (VLA) policy, SWIM-VLA, combines a diffusion action head with Visual Soft Proprioception (VSP) through a shared representation of RGB observations, language instructions, and tendon states. The diffusion head models conditional distributions of expert command chunks, while VSP supervises ordered body-anchor predictions using simulation ground truth, encouraging the representation to retain body geometry when learning from limited demonstrations. Embodied mechanical intelligence supports physical execution of command sequences generated through iterative virtual rollout from evolving simulated observations, with intrinsic compliance providing local contact adaptation without online policy queries. We evaluate SWIM on packing, reaching, and grasping on a planar tendon-driven soft robot, with grasping targets anchored. In simulation, SWIM-VLA achieves success rates of 100\%, 96\%, and 88\%, respectively, outperforming an adapted OpenVLA-OFT baseline and controlled ablations. On hardware, SWIM achieves success rates of 100\%, 80\%, and 75\%, compared with 75\%, 40\%, and 25\% for direct online deployment of the same policy checkpoint.

</details>

#### 2026-09-15 - NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving

**Authors:** Muhammad Ahmed Ullah Khan, Mohammed Elamine, Sheikh Talha Uddin, Didier Stricker, Sk Aziz Ali, Muhammad Zeshan Afzal
**Links:** [abs](https://arxiv.org/abs/2609.16919) - [pdf](https://arxiv.org/pdf/2609.16919)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving
- 作者：Muhammad Ahmed Ullah Khan, Mohammed Elamine, Sheikh Talha Uddin, Didier Stricker, Sk Aziz Ali, Muhammad Zeshan Afzal
- 出版日期：2026-09-15T09:52:51Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.16919

### 一句话总结
该论文提出了 NeuroSymbEAD，一个基于 KITTI-360 构建的大规模神经符号描述数据集，通过以自车为中心的静态与动态物体知识图谱生成多层级文本描述，并用于驾驶常识与交通场景理解的基准测试。

### 研究问题
论文关注如何为自动驾驶场景构建神经符号表示，并将 3D 驾驶场景转换为结构化的、以自车为中心的语言描述，以支持交通场景解释、3D 推理和可解释的自动驾驶感知。摘要指出，基于自然语言的 grounded captioning 对物体及其复杂关系的描述在室内场景任务中已被广泛采用，而本文试图将类似思路扩展到自动驾驶场景。

### 核心思路/方法
论文构建了一个以自车为中心的知识图谱（KG），对静态和动态物体标注类别、分类、朝向、方向和与自车的距离。这些标注在 KITTI-360 数据集上用于生成多层级文本描述，表示轻量级的以自车为中心的场景地图。数据标注流程允许生成多样化的地图片段，在任意 3D 目标检测网络预测的边界框内填充模拟或真实物体，并构建分层文本描述。论文使用预训练的 grounding 网络和学习的自回归 captioning 网络对神经符号及本体论描述生成进行基准测试。户外场景地图重建、视觉识别和目标 grounding 被用作驾驶常识与交通/场景理解的基线。

### 主要贡献
- 提出 NeuroSymbEAD，一个大规模神经符号描述数据集，包含以自车为中心的静态与动态物体知识图谱，标注类别、分类、朝向、方向和距离。
- 基于 KITTI-360 生成多层级文本描述，表示轻量级以自车为中心的场景地图。
- 提供数据标注流程，可生成多样化地图片段，并可在任意 3D 目标检测网络预测的边界框内填充模拟或真实物体。
- 使用预训练 grounding 和自回归 captioning 网络进行基准测试。
- 通过将 3D 驾驶场景转换为结构化自车中心语言，为交通场景解释、3D 推理和可解释自动驾驶感知提供视觉语言与基础模型的基准。

### 局限性
摘要未提供足够信息。论文未在摘要中说明数据规模的具体数值、标注质量评估、基准测试的定量结果、方法在真实驾驶场景中的泛化能力、计算成本或潜在偏差等细节。

### 阅读优先级
中。该论文属于自动驾驶与视觉语言交叉方向，提出了新的数据集与基准，对从事交通场景理解、3D 推理、可解释自动驾驶感知或多模态基础模型的研究者有参考价值。但摘要未给出实验细节与定量结果，若需评估其实际效果和适用性，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

This paper introduces NeuroSymbEAD, a large-scale neuro-symbolic caption dataset featuring an ego-centric knowledge graph (KG) of static and dynamic objects annotated with classes, categories, heading directions, orientations, and distances from the ego-vehicle. These annotations are used on the KITTI-360 dataset to generate multilevel textual captions representing a lightweight version of an ego-centric scene map. Outdoor scene-map reconstruction, visual recognition, and object grounding establish baselines for driving common sense and traffic/scene understanding. For these purposes, natural language-based grounded captioning of objects and their complex relationships is a widely adopted contextual representation for indoor scene tasks. Neuro-symbolic representations have proven effective in handling structured information for various computer vision and language applications. Our data annotation pipeline allows the generation of varied map segments, populating simulated or real objects within the bounding boxes predicted by any 3D object detection network, and building hierarchical text captions. We benchmark our neuro-symbolic and ontological caption generation using pre-trained grounding and learned auto-regressive captioning networks. By converting 3D driving scenes into structured ego-centric language, NeuroSymbEAD provides a benchmark for vision-language and foundation models for traffic-scene explanation, 3D reasoning, and interpretable autonomous-driving perception.

</details>

#### 2026-09-15 - Seeing What Matters: Visual Cue Guided Video Planning for Generalizable Robot Navigation

**Authors:** Hojin Lee, Sizhe Lester Li, Maximilian Hilger, Susie Lu, Achim J. Lilienthal, Vincent Sitzmann, Daniel A. Duecker
**Links:** [abs](https://arxiv.org/abs/2609.16737) - [pdf](https://arxiv.org/pdf/2609.16737)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seeing What Matters: Visual Cue Guided Video Planning for Generalizable Robot Navigation
- 作者：Hojin Lee, Sizhe Lester Li, Maximilian Hilger, Susie Lu, Achim J. Lilienthal, Vincent Sitzmann, Daniel A. Duecker
- 出版日期：2026-09-15T07:11:21Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.16737 ；PDF https://arxiv.org/pdf/2609.16737

### 一句话总结
CueNav 将鸟瞰图（BEV）与保留机器人本体的自我中心视角作为视觉线索引导视频规划，并用特定具身的逆动力学模型（IDM）把视频计划中的稠密光流翻译为机器人动作，以提升长时程规划与具身感知控制的泛化能力。

### 研究问题
生成式视频模型可作为机器人导航的骨干，通过预测未来观测形成视频计划。但近期方法通常以短时程引导为条件，并通过场景重建恢复几何路点，导致更长时程规划与精确的视频到动作翻译仍探索不足。论文关注如何利用视觉线索引导视频规划，并实现视频计划到机器人动作的精确、具身化落地。

### 核心思路/方法
- 提出 CueNav：一个基于视频模型的导航框架，将“视觉线索引导的视频规划”与“具身特定的逆动力学模型（IDM）”结合。
- 视觉线索包括：鸟瞰图（BEV）地图，用于传达全局任务上下文；以及在自我中心观测中保留部分机器人本体，用于暴露具身上下文。
- 视频规划器由上述视觉线索引导；IDM 则将从视频计划中提取的稠密光流场翻译为机器人动作。
- 摘要给出部分结果：具有全局任务上下文的视觉线索编码使迷宫导航成功率相比无该线索的规划提升近 2 倍；带 IDM 的具身感知视角在狭窄通道中实现 70% 成功率，而对比方法在该任务上大多失败。
- 摘要还提到展示了零样本语义条件导航，以及同一视频规划器在不同机器人平台上的部署。

### 主要贡献
- 提出结合视觉线索引导视频规划与具身特定 IDM 的导航框架 CueNav。
- 使用 BEV 地图承载全局任务上下文、在自我中心观测中保留机器人本体以暴露具身上下文，作为引导视频规划器的视觉线索。
- 通过 IDM 将视频计划中的稠密光流场转换为机器人动作，推动视频到动作的精确翻译。
- 摘要报告在迷宫导航中成功率近 2 倍提升，在狭窄通道中达到 70% 成功率；并展示零样本语义条件导航及跨不同机器人平台部署同一视频规划器的能力。
- 声明项目网站提供额外结果与代码：https://cuenav.github.io 。

### 局限性
摘要未提供足够信息。摘要未提供关于实验设置、基线细节、失败案例、计算成本、真实世界与仿真差异、跨平台部署的具体限制或泛化边界等信息。

### 阅读优先级
高。理由：该工作直接针对视频模型驱动机器人导航中的长时程规划与视频到动作翻译问题，并提出结合全局任务上下文与具身上下文的视觉线索方案；摘要中给出了迷宫导航与狭窄通道的量化结果，并声称支持零样本语义条件导航和跨机器人平台部署，对具身导航与视频规划方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Generative video models can serve as a promising backbone for robot navigation by predicting future observations as video plans. Recent approaches often condition video planning on short-horizon guidance and recover geometric waypoints through scene reconstruction, leaving longer-horizon planning and precise video-to-action translation less explored. We present CueNav, a video model-based navigation framework combining visual cue guided video planning with an embodiment-specific Inverse-Dynamics Model (IDM). As visual cues, we use a Bird's-Eye View (BEV) map to convey global task context and retain part of the robot body in the egocentric observation to expose embodiment context. These cues guide the video planner, while the IDM translates dense flow fields extracted from the video plan into robot actions. With the visual cue encoding global task context, CueNav achieves nearly 2x higher success in maze navigation than planning without the cue. The body-aware view with the IDM enables precise navigation with 70% success in a narrow passage where comparison methods largely fail to complete the task. We further demonstrate zero-shot semantic-conditioned navigation and deployment of the same video planner across different robot platforms. Our results show that visual cue-guided video planning with embodiment-specific action grounding paves the way toward a generalizable navigation framework for longer-horizon planning and embodiment-aware control. Additional results and code are available on our project website: https://cuenav.github.io.

</details>

#### 2026-09-15 - CorrRisk-WM: Corridor-Conditioned Risk World Modeling for Safety-Critical Trajectory Planning

**Authors:** Tingyu Guo, Reza Langari
**Links:** [abs](https://arxiv.org/abs/2609.16724) - [pdf](https://arxiv.org/pdf/2609.16724)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reasoning, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CorrRisk-WM: Corridor-Conditioned Risk World Modeling for Safety-Critical Trajectory Planning
- 作者：Tingyu Guo, Reza Langari
- 出版日期：2026-09-15T06:56:08Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要链接 https://arxiv.org/abs/2609.16724 ；PDF 链接 https://arxiv.org/pdf/2609.16724

### 一句话总结
CorrRisk-WM 提出一种面向规划的局部世界模型，将环境演化预测与候选轨迹走廊内的侵入/近失事件监督预测耦合，用于安全关键场景下的风险评估与候选轨迹选择。

### 研究问题
安全局部规划需要预测周围智能体的运动，并评估“候选轨迹特定”的风险，因为相同的智能体运动对不同自车轨迹可能构成不同风险。论文关注的核心问题是：如何在规划中同时建模环境演化，并针对每条候选轨迹走廊进行风险预测与评估。

### 核心思路/方法
- 提出 CorrRisk-WM，一个面向规划的“部分世界模型”，将环境演化与有界候选轨迹走廊上的侵入和近失监督预测耦合。
- 使用潜在环境模型递归预测智能体状态，并更新智能体—智能体、智能体—地图交互。
- 每个候选轨迹通过足迹感知几何和学习的智能体—走廊表示，查询不断演化的环境。
- 使用轻量级循环风险模块，基于时间上下文估计逐切片危险；通过生存聚合得到首次进入事件概率和时域级事件概率。

### 主要贡献
- 提出将环境演化建模与候选轨迹条件化几何推理耦合的风险世界模型，用于风险预测和安全导向的候选选择。
- 在 Waymo 验证集 100 个分片的 29,176 个场景上，报告侵入平均精度（AP）为 0.8567，1 米近失首次进入 AP 为 0.8671。
- 在基线比较中，报告在三个距离阈值上均取得最高近失 AP，并取得最低观测开环碰撞率 4.88%，路线进展为 15.35 米。
- 消融结果显示：在三个随机种子下，移除动态环境建模或候选条件化几何交互，会使平均侵入 AP 从 0.8590 分别降至 0.7624 和 0.7252。

### 局限性
摘要未提供足够信息。摘要未说明方法在更广泛数据集、不同传感器配置、真实闭环部署、计算开销、失败案例或与更多规划基线的完整比较等方面的局限性。

### 阅读优先级
高。理由：论文主题聚焦安全关键轨迹规划，提出候选轨迹条件化的风险世界模型，并在大规模 Waymo 验证场景上报告了定量结果与消融分析；对关注自动驾驶安全规划、世界模型和风险预测的研究者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Safe local planning requires forecasting surrounding-agent motion and evaluating candidate-specific risks, since identical agent motion can pose different risks to different ego trajectories. We present CorrRisk-WM, a planning-oriented partial world model coupling environment evolution with supervised intrusion and near-miss prediction over bounded candidate-trajectory corridors. A latent environment model recursively predicts agent states and updates agent-agent and agent-map interactions. Each candidate queries the evolving environment through footprint- aware geometry and learned agent-corridor representations. A lightweight recurrent risk module uses temporal context to estimate per-slice hazards; survival aggregation yields first-entry and horizon-level event probabilities. On 29,176 scenarios from 100 Waymo validation shards, CorrRisk-WM achieves intrusion average precision (AP) of 0.8567 and 1-m near-miss first-entry AP of 0.8671. In baseline comparisons, it attains the highest near-miss AP at all three distance thresholds and the lowest observed open-loop collision rate (4.88%), with route progress of 15.35 m. Across three seeds, removing dynamic environment modeling or candidate-conditioned geometric interaction reduces mean intrusion AP from 0.8590 to 0.7624 and 0.7252, respectively. These results support coupling environment evolution with candidate-conditioned geometric reasoning for risk prediction and safety-oriented candidate selection.

</details>

#### 2026-09-15 - ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation

**Authors:** Yushan Bai, Boyu Zheng, Zhiyang Mao, Hongzheng Sun, Yuchuang Tong, En Li, Zhengtao Zhang
**Links:** [abs](https://arxiv.org/abs/2609.16586) - [pdf](https://arxiv.org/pdf/2609.16586)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation
- 作者：Yushan Bai, Boyu Zheng, Zhiyang Mao, Hongzheng Sun, Yuchuang Tong, En Li, Zhengtao Zhang
- 出版日期：2026-09-15T03:31:55Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.16586

### 一句话总结
ProxiDex 提出一种以手—物接近度作为交互状态、结合动作条件接近动态建模与动态一致性监督的灵巧操作策略框架，以缓解视觉遮挡与触觉硬件依赖带来的接触不确定性。

### 研究问题
多指灵巧操作依赖稳定的手—物交互，但这种交互在实践中只能被部分观测：视觉常被手部遮挡，触觉传感器带来硬件特定模态与标定负担，且现有策略很少建模这些线索在动作下如何演化，导致在接触不确定性下表现脆弱。论文旨在解决该部分可观测与鲁棒性问题。

### 核心思路/方法
- 将手—物接近度（hand-object proximity）视为灵巧操作的一种交互状态。
- 重建交互点云，并将几何距离转化为接近度线索，形成与硬件无关的接触表示，在 VR 遥操作中提供沉浸式反馈。
- 基于该表示，学习动作条件接近动态，采用耦合的前向—逆向设计：由动作预测未来观测隐变量，同时从隐变量变化中解码接近度变化。
- 利用该动态，在操作各阶段自适应地对接近度 token 重新加权，并以动态一致性监督引导策略推理，从而在不可靠视觉反馈下稳定动作生成。

### 主要贡献
- 提出 ProxiDex 动态引导接近度策略框架，将手—物接近度建模为交互状态。
- 构建硬件无关的接近度接触表示，用于交互点云重建与 VR 遥操作沉浸式反馈。
- 设计耦合前向—逆向的动作条件接近动态学习机制，并引入动态一致性监督与接近度 token 自适应重加权。
- 据摘要，仿真与真实实验在标准、未见物体及扰动场景下相较代表性基线取得更高成功率与鲁棒性（具体数值与实验设置摘要未提供足够信息）。

### 局限性
- 摘要未提供足够信息说明方法对点云重建质量的依赖程度与失败边界。
- 摘要未提供足够信息说明真实实验的硬件平台、物体集合、扰动类型与量化指标。
- 摘要未提供足够信息说明与触觉基线对比的具体条件及接近度表示的标定需求。
- 摘要未提供足够信息说明计算开销、实时性与泛化到更复杂任务的验证情况。

### 阅读优先级
高。理由：论文针对灵巧操作中视觉遮挡与触觉硬件依赖这一关键瓶颈，提出硬件无关的接近度表示与动态一致性策略学习思路，且声称在仿真与真实扰动场景下优于代表性基线；若关注部分可观测下的鲁棒灵巧操作与 VR 遥操作反馈，该工作具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Multi-finger dexterous manipulation relies on stable hand-object interactions, yet these interactions are partially observable in practice. Visual observations are often occluded by the hand, tactile sensors introduce hardware-specific modalities and calibration burdens, and existing policies rarely model how these cues evolve under actions, making them brittle under contact uncertainty. To address these, we present ProxiDex, a dynamics-guided proximity policy framework that treats hand-object proximity as an interaction state for dexterous manipulation. ProxiDex reconstructs interaction point clouds and converts geometric distances into proximity cues, forming a hardware-agnostic contact representation that provides immersive feedback during VR teleoperation. Built on this representation, ProxiDex learns action-conditioned proximity dynamics with a coupled forward-inverse design: future observation latents are predicted from actions, while proximity variations are decoded from latent changes. Leveraging these dynamics, ProxiDex adaptively reweights proximity tokens across manipulation phases and uses dynamics-consistency supervision to guide policy inference, stabilizing action generation under unreliable visual feedback. Simulation and real-world experiments demonstrate improved success rates and robustness over representative baselines across standard, unseen objects, and perturbation scenarios. Additional visualizations are available at https://proxidex.github.io/.

</details>

#### 2026-09-15 - UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data

**Authors:** Hyesung Lee, Si-Hwan Heo, Sungwook Yang
**Links:** [abs](https://arxiv.org/abs/2609.16504) - [pdf](https://arxiv.org/pdf/2609.16504)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data
- 作者：Hyesung Lee, Si-Hwan Heo, Sungwook Yang
- 出版日期：2026-09-15T01:52:33Z
- 分类：Embodied / Robotics / AR Applications（secondary_categories 摘要未提供足够信息）
- 链接：https://arxiv.org/abs/2609.16504 ；PDF：https://arxiv.org/pdf/2609.16504 ；项目页：https://unidex-vitac.github.io/

### 一句话总结
该论文提出 UniDex-ViTac 框架，通过人类视频引导的仿真生成带指尖接触观测的机器人示范，训练一个无需人类参考和物体身份/位姿先验的可部署视触觉灵巧操作策略。

### 研究问题
人类视频能提供灵巧操作的示范，但缺少机器人可执行的动作和触觉测量。如何利用这类数据学习可部署的视触觉灵巧操作策略，是论文关注的问题。

### 核心思路/方法
- 使用人类视频引导的仿真，生成与指尖接触观测配对的机器人示范。
- 采用物体特定的残差强化学习专家，将带标注的人-物交互参考适配到机械臂-机械手系统。
- 成功 rollout 中，最终机器人动作目标与机器人侧指尖接触观测配对。
- 基于 10 个物体的 50 个人类示范，收集 10,000 条仿真轨迹，训练单个基于 Action Chunking with Transformers（ACT）的通用策略。
- 策略输入结合点云、本体感觉和四个二值接触信号；接触信号通过指尖标签和单独 token 编码。
- 部署时不需要人类参考，也不需要特权物体身份和位姿。

### 主要贡献
- 提出从人类视频引导仿真中学习统一视触觉灵巧操作策略的框架 UniDex-ViTac。
- 构建了包含指尖接触观测的机器人示范生成流程，并用于训练基于 ACT 的通用策略。
- 在仿真中，接触增强配置达到 68.3% 宏平均成功率，点云基线为 55.5%。
- 在无真机示范、无策略微调条件下，物理试验中成功 73/110（66.4%），覆盖六个已见和五个未见物体；基线为 60/110（54.5%），提升 11.8 个百分点。
- 结果支持从视频引导仿真交互中学习统一视触觉灵巧操作策略的可行性。

### 局限性
- 摘要未提供足够信息说明仿真到现实的差距、失败模式、接触信号可靠性或方法在更复杂任务上的泛化边界。
- 摘要未提供足够信息说明人类视频标注成本、仿真生成流程的适用范围以及对不同机械手或传感器的迁移能力。
- 摘要未提供足够信息报告除成功率外的其他指标、统计显著性、训练资源消耗或消融细节。

### 阅读优先级
高。理由：该工作直接针对机器人灵巧操作中“人类视频缺乏动作与触觉”的关键缺口，提出视触觉统一策略，并同时给出仿真与物理试验成功率对比；若关注从人类视频学习、视触觉融合或灵巧操作策略部署，这篇论文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Human videos provide demonstrations of dexterous manipulation but lack robot-executable actions and tactile measurements. We present UniDex-ViTac, a framework that uses human-video-guided simulation to generate robot demonstrations paired with fingertip contact observations for training a deployable visuo-tactile policy. Object-specific residual reinforcement learning specialists adapt annotated human-object interaction references to a robotic arm-hand system. Their successful rollouts pair final robot action targets with robot-side fingertip contact observations. From 50 human demonstrations across ten objects, we collect 10,000 simulated trajectories to train a single Action Chunking with Transformers (ACT) based generalist. The policy combines point clouds, proprioception, and four binary contact signals encoded through fingertip labels and a separate token, without requiring human references or privileged object identity and pose at deployment. The contact-augmented configuration achieves 68.3% macro-average success in simulation, compared with 55.5% for the point-cloud-only baseline. Without real-robot demonstrations or policy fine-tuning, it succeeds in 73/110 physical trials (66.4%) across six seen and five unseen objects, compared with 60/110 (54.5%) for the baseline, an increase of 11.8 percentage points. These results support the feasibility of learning a unified visuo-tactile dexterous manipulation policy from video-guided simulated interactions. Project page: https://unidex-vitac.github.io/

</details>

#### 2026-09-14 - Geometry vs Structure: Graph-Based Diagnostics for LiDAR Point-Cloud Simulation Fidelity

**Authors:** Ghazal Farhani, Taufiq Rahman
**Links:** [abs](https://arxiv.org/abs/2609.16378) - [pdf](https://arxiv.org/pdf/2609.16378)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry vs Structure: Graph-Based Diagnostics for LiDAR Point-Cloud Simulation Fidelity
- 作者：Ghazal Farhani, Taufiq Rahman
- 出版日期：2026-09-14T21:41:08Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.16378 ；PDF https://arxiv.org/pdf/2609.16378

### 一句话总结
论文提出一种基于图的诊断框架，通过构造点云图、Louvain 社区检测与质心邻近匹配，并计算图谱度量 \(r_\lambda\)，来评估仿真 LiDAR 点云相对真实扫描的结构保真度，并与密度感知 Chamfer 距离（CDC）进行互补对比。

### 研究问题
数字孪生被用于自动驾驶与 ADAS 传感器流程验证，但其保真度难以量化，尤其是 3D LiDAR 点云。传统几何指标可能忽略重要的结构差异，例如连通性、拓扑或对象级组织。论文关注的问题是：如何在扫描级几何相似度之外，评估仿真 LiDAR 点云的结构保真度。

### 核心思路/方法
- 从真实与仿真点云分别构造图。
- 使用 Louvain 社区检测识别空间上连贯的子图。
- 通过质心邻近匹配对应的社区。
- 对每一对匹配社区，计算有界图谱度量 \(r_\lambda\)，其动机来自 Weyl 不等式。
- 以密度感知 Chamfer 距离（CDC）作为几何基线进行比较。
- 通过受控扰动实验验证 \(r_\lambda\)：对刚性变换不变、对传感器噪声稳健，同时对结构变形敏感。
- 在 50 对真实与仿真 LiDAR 扫描上评估，真实数据由 Velodyne VLP-32C 传感器采集，仿真数据由 CARLA 生成；数据集包含四个代表性类别（车辆、植被、树木、建筑墙面）的 1000 多个匹配社区。

### 主要贡献
- 提出一个基于图的框架，用于评估仿真 LiDAR 点云相对真实扫描的结构保真度。
- 引入图谱度量 \(r_\lambda\)，用于匹配社区之间的结构比较，并展示其对刚性变换和传感器噪声的特性。
- 将结构度量与几何度量 CDC 进行对比，表明几何与结构度量捕捉的是仿真保真度的互补方面。
- 在真实与 CARLA 仿真 LiDAR 扫描配对数据上进行了评估，覆盖多个对象类别与大量匹配社区。
- 支持将图谱分析作为验证 ADAS 与自动驾驶数字孪生的额外诊断层。

### 局限性
摘要未提供足够信息。摘要未说明该框架在更大规模数据集、不同传感器、不同仿真器或不同场景下的泛化能力；未提供计算复杂度、运行效率或参数敏感性分析；也未说明 \(r_\lambda\) 的具体阈值、失败案例或与下游任务性能的关联。

### 阅读优先级
高。理由：该论文直接针对 LiDAR 点云仿真保真度评估这一数字孪生与自动驾驶验证中的关键问题，提出区别于传统几何指标的图结构诊断方法，并给出在真实 Velodyne 与 CARLA 数据上的配对评估。若关注 ADAS/自动驾驶传感器仿真验证、点云结构分析或图方法在 3D 感知中的应用，该文具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Digital twins provide a scalable and cost-effective complement to real-world testing for validating autonomous-driving and advanced driver-assistance system (ADAS) sensor pipelines. However, quantifying their fidelity remains challenging, particularly for 3D LiDAR point clouds, where conventional geometric metrics may overlook important structural discrepancies. We present a graph-based framework for evaluating the structural fidelity of simulated LiDAR point clouds against real-world scans. While scan-level metrics such as Chamfer distance capture point-wise geometric similarity, they do not explicitly represent connectivity, topology, or object-level organization. Our framework constructs graphs from real and simulated point clouds, applies Louvain community detection to identify spatially coherent subgraphs, and matches corresponding communities using centroid proximity. For each matched pair, we compute $r_λ$, a bounded graph-spectral metric motivated by Weyl's inequality, and compare it with density-aware Chamfer distance (CDC) as a geometric baseline. Controlled perturbation experiments demonstrate that $r_λ$ is invariant to rigid transformations and robust to sensor noise while remaining sensitive to structural deformation. We evaluate the framework on 50 paired real and simulated LiDAR scans acquired using a Velodyne VLP-32C sensor and CARLA, respectively. The dataset contains more than 1,000 matched communities across four representative classes: vehicles, vegetation, trees, and building walls. The results show that geometric and structural measures capture complementary aspects of simulation fidelity, supporting graph-spectral analysis as an additional diagnostic layer for validating digital twins in ADAS and autonomous-driving applications.

</details>

#### 2026-09-14 - JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion

**Authors:** Qihao Yuan, Yixuan Qiu, Ziyu Cao, Ming Cao, Kailai Li
**Links:** [abs](https://arxiv.org/abs/2609.15770) - [pdf](https://arxiv.org/pdf/2609.15770)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion
- 作者：Qihao Yuan, Yixuan Qiu, Ziyu Cao, Ming Cao, Kailai Li
- 出版日期：2026-09-14T15:54:26Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：摘要链接 https://arxiv.org/abs/2609.15770 ；PDF 链接 https://arxiv.org/pdf/2609.15770 ；开源实现、实验数据集与硬件设计方案：https://github.com/ASIG-X/JEPLO

### 一句话总结
JEPLO 是一个面向足式机器人的单阶段、免建图 LiDAR 感知运动学习框架，通过本体-外感知 JEPA 世界模型与并行的 JEPA 师生训练流程，学习预测性自中心地形表征并训练运动策略，实现了仿真到真实的迁移和鲁棒的全向复杂地形通行。

### 研究问题
- 在感知式足式运动领域，LiDAR 相较 RGB-D 感知得到的探索较少，现有基于 LiDAR 的方法通常依赖显式建图（explicit mapping）。
- 论文希望解决的是：如何在不进行显式建图的前提下，直接从机载观测（包括原始 LiDAR 扫描）学习可用于足式机器人感知运动的地形表征与策略。

### 核心思路/方法
- 提出 JEPLO，一个用于足式机器人的单阶段学习框架，目标是实现免建图、基于 LiDAR 的感知运动。
- 引入 PE-JEPA（proprio-exteroceptive JEPA）世界模型，从机载观测（含原始 LiDAR 扫描）中学习预测性的自中心（egocentric）地形表征。
- 提出 CJTS（concurrent JEPA-teacher-student）流水线，在仿真中利用深度强化学习，以 JEPA 潜在表征为信息训练运动策略，并采用简单的奖励设计。
- 框架实现仿真到真实迁移，支持轻量机载计算下的多地形全向通行。

### 主要贡献
- 提出 JEPLO 单阶段学习框架，实现免建图、基于 LiDAR 的足式机器人感知运动。
- 提出 PE-JEPA 世界模型，用于从机载观测（包括原始 LiDAR 扫描）学习预测性自中心地形表征。
- 提出 CJTS 训练流水线，将 JEPA 潜在表征与深度强化学习结合，在简单奖励形式下训练运动策略。
- 实现仿真到真实迁移，支持包括长楼梯和高箱体在内的多样地形全向通行，且机载计算轻量。
- 评估显示其鲁棒性优于现有感知运动框架，尤其在遮挡、稀疏和噪声导致的感知退化条件下；进一步分析验证了 JEPLO 在这些挑战条件下保留任务相关信息的能力。
- 开源实现、实验数据集和硬件设计方案。

### 局限性
- 摘要未提供足够信息说明方法在计算资源、传感器配置或真实部署规模上的具体限制。
- 摘要未提供足够信息说明失败案例、极端地形类型或感知退化条件之外的其他性能边界。
- 摘要未提供足够信息说明与基线方法比较的定量指标、实验场景数量和消融研究的详细结果。
- 摘要未提供足够信息说明 PE-JEPA 与 CJTS 各自的独立贡献程度及训练稳定性问题。

### 阅读优先级
高。理由：该论文针对 LiDAR 感知足式运动中“依赖显式建图”的关键问题，提出免建图的单阶段学习框架，并报告了仿真到真实迁移、鲁棒性优势及开源实现与数据集；对具身智能、机器人感知运动和多模态表征学习方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing LiDAR-based approaches often rely on explicit mapping. We present JEPLO (Joint-Embedding Predictive learning for legged LOcomotion), a single-stage learning framework for mapping-free, LiDAR-based perceptive locomotion for legged robots. We introduce a proprio-exteroceptive JEPA (PE-JEPA) world model to learn predictive egocentric terrain representations from onboard observations, including raw LiDAR scans. A concurrent JEPA-teacher-student (CJTS) pipeline is further proposed to train a locomotion policy informed by JEPA latent representations in simulation using deep reinforcement learning with a simple reward formulation. The framework achieves successful sim-to-real transfer, enabling omnidirectional traversal of diverse terrains, including long staircases and high boxes, with lightweight onboard computation. Evaluations demonstrate greater robustness than existing perceptive locomotion frameworks, particularly under degraded perception caused by occlusion, sparsity and noise. Further analysis validates JEPLO's ability to retain task-relevant information under these challenging conditions. We open-source our implementation, experimental datasets, and hardware setup designs https://github.com/ASIG-X/JEPLO.

</details>

#### 2026-09-14 - Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands

**Authors:** Zhenjie Yang, Yideng Zhang, Dongjie Zhang, Chenyu Jiang, Xianshuai Liu, Yufeng Li, Zuhao Ge, Xingyu Jiao, Zheng Zhang, Kaiyu He, He Wang, Yuwen Zhong, Yi Deng, Muyun Jiang, Xianliang Huang, Haisheng Su, Donghang Zhang, Jian Zhang, Xue Yang, Hongyang Li, Zuxuan Wu, Yu-Gang Jiang, Xiaosong Jia, Junchi Yan
**Links:** [abs](https://arxiv.org/abs/2609.15726) - [pdf](https://arxiv.org/pdf/2609.15726)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands
- 作者：Zhenjie Yang, Yideng Zhang, Dongjie Zhang, Chenyu Jiang, Xianshuai Liu, Yufeng Li, Zuhao Ge, Xingyu Jiao, Zheng Zhang, Kaiyu He, He Wang, Yuwen Zhong, Yi Deng, Muyun Jiang, Xianliang Huang, Haisheng Su, Donghang Zhang, Jian Zhang, Xue Yang, Hongyang Li, Zuxuan Wu, Yu-Gang Jiang, Xiaosong Jia, Junchi Yan
- 出版日期：2026-09-14T15:22:59Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.15726 ；PDF https://arxiv.org/pdf/2609.15726

### 一句话总结
Bench2Dex 是一个覆盖 12 种灵巧手、26 项双臂操作任务的仿真基准，通过统一的仿真触觉接口提供同步视觉、触觉、本体感觉、动作与物体状态观测，用于在一致实验设置下研究跨灵巧手的视触觉双臂灵巧操作。

### 研究问题
论文关注的核心问题是：触觉传感能提供视觉难以推断的接触信息，但灵巧手的触觉硬件尚未收敛到统一设计，不同灵巧手在手指结构、接触面和传感器布局上各不相同，且仿真触觉信号与物理传感器测量仍存在差异；这些因素使得在一致实验设置下研究跨多种灵巧手的视触觉操作变得困难。Bench2Dex 旨在为跨灵巧手的视触觉学习提供统一平台。

### 核心思路/方法
- 构建一个面向跨 12 种灵巧手的视触觉双臂操作仿真基准 Bench2Dex。
- 改造已有机器人模型，采用共享的仿真触觉接口，将局部接触几何转换为类图像的触觉观测。
- 该接口在不同手部形态之间提供一致的观测格式，但不试图复现某一特定物理触觉传感器的输出。
- 基准包含 26 项双臂操作任务，涉及工具使用、铰接物体交互和多阶段操作，并提供约 1.3K 人类遥操作演示。
- 提供同步的视觉、触觉、本体感觉、动作和物体状态观测，以及可执行的任务指标。
- 为评估鲁棒性，将七类扰动划分为两类轴：不变性轴（正确动作不随扰动改变）和等变性轴（正确动作随扰动改变）。
- 在 Bench2Dex 上评估 ACT、Diffusion Policy、pi0.5 和 GR00T N1.5，并报告其性能与失败模式。

### 主要贡献
- 提出 Bench2Dex：一个覆盖 12 种灵巧手的视触觉双臂操作仿真基准。
- 设计共享仿真触觉接口，将局部接触几何转为类图像触觉观测，实现跨不同手部形态的一致观测格式。
- 提供 26 项双臂操作任务，涵盖工具使用、铰接物体交互和多阶段操作。
- 提供约 1.3K 人类遥操作演示，以及同步的视觉、触觉、本体感觉、动作与物体状态观测和可执行任务指标。
- 引入按不变性轴与等变性轴分组的七类扰动，用于鲁棒性评估。
- 在统一基准上评估 ACT、Diffusion Policy、pi0.5 和 GR00T N1.5，并报告性能与失败模式。

### 局限性
- 论文明确说明 Bench2Dex 不假设仿真触觉观测可以替代真实触觉传感；它提供的是在触觉硬件与仿真模型仍演进过程中的共享算法开发设置。
- 关于仿真触觉与真实传感器之间差距的具体量化、任务难度的详细分层、演示数据质量、评估协议细节、各方法的具体数值结果和失败模式内容，摘要未提供足够信息。
- 关于 12 种灵巧手的具体型号、26 项任务的具体清单、七类扰动的具体定义，摘要未提供足够信息。
- 关于 ACT、Diffusion Policy、pi0.5、GR00T N1.5 的具体配置、训练细节与计算成本，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对跨灵巧手的视触觉双臂操作这一具有现实意义的问题，提供统一仿真基准、多任务与多演示数据、同步多模态观测及鲁棒性扰动轴设计，并给出多种代表性策略的评估与失败模式，对具身智能与机器人操作方向的研究者有参考价值；但摘要未提供具体任务清单、手部型号、扰动定义和数值结果，若需判断其与自身研究的直接相关性，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Tactile sensing provides contact information that can be difficult to infer from vision alone, but tactile hardware for dexterous hands has not converged to a common design. Dexterous hands differ in finger structure, contact surfaces, and sensor layouts, while simulated tactile signals still differ from measurements produced by physical sensors. These factors make it difficult to study visuo-tactile manipulation across diverse dexterous hands within a consistent experimental setting. We present Bench2Dex, a simulation benchmark for visuo-tactile bimanual manipulation across 12 dexterous hands. We adapt existing robot models with a shared simulated tactile interface that converts local contact geometry into image-like tactile observations. The interface provides a consistent observation format across different hand morphologies without attempting to reproduce the output of a specific physical tactile sensor. Bench2Dex includes 26 bimanual manipulation tasks that involve tool use, articulated-object interaction, and multi-stage manipulation, together with about 1.3K human-teleoperated demonstrations. The benchmark provides synchronized visual, tactile, proprioceptive, action, and object-state observations, together with executable task metrics. For robustness, we group seven perturbation types into invariance axis, where the correct action does not change, and equivariance axis, where the correct action changes together with the perturbation. We evaluate ACT, Diffusion Policy, pi0.5, and GR00T N1.5 on Bench2Dex and report their performance and failure modes. Bench2Dex is meant as a platform for studying visuo-tactile learning across dexterous hands. It does not assume that simulated tactile observations can replace real tactile sensing; it offers a shared setting for algorithm development while tactile hardware and simulation models are still evolving.

</details>

#### 2026-09-14 - From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation

**Authors:** Ailing Zhang, Fan Gao, Song Zhang, Kawa Leong, Ziyu Wu, Yafei Wang
**Links:** [abs](https://arxiv.org/abs/2609.15382) - [pdf](https://arxiv.org/pdf/2609.15382)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation
- 作者：Ailing Zhang, Fan Gao, Song Zhang, Kawa Leong, Ziyu Wu, Yafei Wang
- 出版日期：2026-09-14T11:09:21Z
- 分类：Embodied / Robotics / AR Applications（主分类）；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2609.15382 ；PDF https://arxiv.org/pdf/2609.15382

### 一句话总结
论文提出 World-Action Model（WAM），通过世界模型对多个铲掘候选动作进行几何筛选、地形变化与载荷联合预测并排序，在连续料堆挖掘任务中实现决策层面的提升，并在全尺寸装载机上完成闭环部署验证。

### 研究问题
轮式装载机挖掘被作者描述为序列决策问题：每一次铲掘都会改变后续动作可用的地形。论文关注的核心问题是：一个实用世界模型需要同时满足三点——准确预测动作后果、实时对候选动作排序、并能运行在全尺寸机器的闭环之中。摘要未提供足够信息说明该问题在此前的具体研究空白或已有方法的具体失败模式。

### 核心思路/方法
论文提出 World-Action Model（WAM），整体流程为：
1. 提出多个铲掘候选动作；
2. 拒绝几何上不可行的候选；
3. 联合预测带符号的地形变化与装载体积；
4. 执行预测载荷最大的候选动作；
5. 从新观测到的地形重新规划。

摘要还提到对输入表示、空间支持和五种架构进行了比较，以识别一个准确且高效的“物理结构化预测器”。在系统层面，作者将完整的感知—提议—预测—选择—执行闭环部署用于自主挖掘。

### 主要贡献
摘要中明确给出的贡献包括：
- 提出 WAM 这一世界模型引导的动作选择框架，用于连续料堆挖掘。
- 在 32 个几何不相交的 MinSlope 测试回合上，将世界模型排序加入匹配的扩散提议后，平均铲掘次数从 651.8 降至 540.6（降低 17.1%），保持 32/32 完成率，并在每一个配对回合上均有改善。
- 在完整系统比较中，WAM 完成 32/32 个回合，而独立训练的 soft actor-critic 策略完成 29/32。
- 通过输入表示、空间支持与五种架构的比较，识别出准确且高效的物理结构化预测器。
- 在事件不相交的全尺寸装载机数据上评估该接口，并部署完整闭环用于自主挖掘。
- ROS2/TensorRT 实现在 Jetson AGX Orin 上处理 5 个候选耗时 72.4 ms。
- 作者总结：仿真结果确立决策层面的收益，物理实验证明真实世界闭环可行性。

### 局限性
摘要未提供足够信息说明以下方面：仿真环境与真实场景之间的差距程度、全尺寸装载机物理实验的具体规模与评价指标、方法的失败案例或边界条件、计算资源以外的部署限制、以及该方法对其他挖掘任务或地形的泛化能力。摘要仅说明物理实验“证明真实世界闭环可行性”，未提供足够信息量化物理实验性能。

### 阅读优先级
中。理由：论文主题属于具身智能与机器人自主挖掘，提出世界模型引导的动作选择，并同时给出仿真决策层面收益与全尺寸机器闭环部署，工程完整度较高；但摘要未提供足够信息说明其相对已有方法在物理场景中的量化优势，且无二级分类、无额外兴趣方向提示，因此优先级定为中而非高。

</details>

<details>
<summary>Abstract</summary>

Wheel-loader excavation is a sequential decision problem in which every scoop changes the terrain available to subsequent actions. A practical world model must predict action consequences accurately, rank candidates in real time, and operate inside the closed loop of a full-size machine. We present the World-Action Model (WAM), which proposes multiple scoops, rejects geometrically inadmissible candidates, jointly predicts signed terrain change and loaded volume, executes the candidate with the largest predicted load, and replans from the newly observed terrain. On 32 geometry-disjoint MinSlope test episodes, adding world-model ranking to matched diffusion proposals reduces the mean scoop count from 651.8 to 540.6 (17.1%), preserves 32/32 completion, and improves every paired episode. In a complete-system comparison, WAM completes 32/32 episodes versus 29/32 for an independently trained soft actor-critic policy. Comparisons of input representations, spatial support, and five architectures identify an accurate and efficient physics-structured predictor. We further evaluate the interface on event-disjoint full-size-loader data and deploy the complete perception-proposal-prediction-selection-execution loop for autonomous excavation. The ROS2/TensorRT implementation processes five candidates in 72.4 ms on a Jetson AGX Orin. The simulation results establish decision-level gains, while the physical experiments demonstrate real-world closed-loop feasibility.

</details>

#### 2026-09-14 - Legislating World-Model-Based Planning with Legal Reasoning

**Authors:** Dylan Waldner, Yiannis Kantaros, Guido Governatori, Risto Miikkulainen, Amir Banifatemi
**Links:** [abs](https://arxiv.org/abs/2609.15113) - [pdf](https://arxiv.org/pdf/2609.15113)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Legislating World-Model-Based Planning with Legal Reasoning
- 作者：Dylan Waldner, Yiannis Kantaros, Guido Governatori, Risto Miikkulainen, Amir Banifatemi
- 出版日期：2026-09-14T06:45:58Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.15113 ；PDF https://arxiv.org/pdf/2609.15113

### 一句话总结
论文提出一种基于可废止道义逻辑（DDL）约束运动规划器的“法律规划栈”，利用学习到的世界模型为规划提供法律上下文，从而在非法动作执行前进行事前治理，并在仿真机械臂推方块任务上验证其有效性。

### 研究问题
论文关注将法律规范整合进日益通用的机器人系统时所面临的对齐同构问题，具体提出并度量两个关键挑战：（1）grounding isomorphism gap，即感知错误会为法律推理 grounding 出错误原子；（2）ontological isomorphism gap，即同一个法律结论可对应多种忠实的规划约束翻译。核心问题是：如何让机器人规划受法律规范约束，并在运行时实现可审计、可适应、事前的合法行为控制。

### 核心思路/方法
论文引入一个 legal planning stack，使用 Defeasible Deontic Logic（DDL）来约束运动规划器。该栈借助学习到的世界模型进行规划并提供法律上下文，使治理发生在非法动作执行之前，即 ex ante governance。论文在仿真机械臂于 3×3 网格推动方块的任务上部署该栈，并对上述两个同构缺口进行了度量。

### 主要贡献
摘要中列出的发现包括：（1）受法律约束的智能体比未受约束的智能体遵守率显著更高，建模感知不确定性后遵守率进一步提升；（2）法律推理在运行时高效执行，其裁决可审计；（3）该栈能适应外生信号和内生的规则变化；（4）度量了世界模型与探针误差对 DDL 推理器事实输入的污染；（5）发现单一法律可对应多种忠实的度量解释，导致遵守率差异巨大。论文据此认为 ex ante legislation 能按预期发挥作用，并指出通过标准化的法律到运行时约束映射以及改进感知事实 grounding，可望实现稳健法律，使机器人行为符合社会规范。

### 局限性
摘要未提供足够信息说明实验规模、仿真环境的具体限制、真实机器人部署情况、方法在更复杂法律体系或开放环境中的可扩展性，以及计算开销的定量边界。摘要仅给出了在仿真机械臂 3×3 网格推方块任务上的结果，未提供其他任务或现实场景的验证信息。

### 阅读优先级
高。理由：该论文直接处理机器人法律合规与事前治理这一具有现实意义的问题，明确形式化了两个对齐缺口，并给出可度量指标与仿真验证结果；对于关注机器人安全、规范对齐、法律推理与运动规划交叉方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

As robotic systems grow more general, legal norms are needed to integrate them into society. This paper extends the isomorphism problem of aligning legal source texts with their encodings, and measures two key challenges to robot normative control: (1) the \textit{grounding isomorphism gap}, where perception error grounds false atoms for legal reasoning, and (2) the \textit{ontological isomorphism gap}, where one legal conclusion admits many faithful translations into planning constraints. The paper introduces a legal planning stack that employs Defeasible Deontic Logic (DDL) to constrain a motion planner. The stack leverages learned world models to plan and to provide legal context, enabling \textit{ex ante} governance that intervenes before an illegal action is executed. It was deployed on a simulated robot arm pushing a cube across a $3\times3$ grid. The findings were (1) the legislated agent abided substantially more often than the non-legislated one, and modeling perception uncertainty lifted abidance even further, (2) the legal reasoning ran efficiently at runtime and its verdicts were auditable, and (3) the stack adapted to exogenous signals and endogenous rule changes. Both gaps were measured: (4) world model and probe error corrupted the factual input for the DDL reasoner, and (5) a single law admitted several faithful metric interpretations yielding drastically different abidance. Thus, \textit{ex ante} legislation functions as intended, and closing these gaps with a standardized mapping from the law to runtime constraints and improved fact grounding from perception will yield robust laws that align robot behavior with society's norms.

</details>

#### 2026-09-10 - Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection

**Authors:** Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie, Gang Liu, Hongjie Yan, Wei Zhou
**Links:** [abs](https://arxiv.org/abs/2609.11225) - [pdf](https://arxiv.org/pdf/2609.11225)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** stereo depth, robot navigation, mapping, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- 作者：Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie, Gang Liu, Hongjie Yan, Wei Zhou
- 出版日期：2026-09-10T08:25:46Z
- 分类：Embodied / Robotics / AR Applications（主要分类）；次要分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.11225 ；PDF https://arxiv.org/pdf/2609.11225

### 一句话总结
论文提出统一的具身智能体运行时 HROS 及其住宅小区巡检实现 Argos，将四足机器人导航、感知、认知推理、语音交互与安全约束下的自演化整合为可追踪的闭环巡检系统。

### 研究问题
自主物业巡检不仅需要稳健的机器人导航，还需要在可追踪的运行闭环中连接异构传感、可复用的自主能力、多模态场景理解、人机交互与企业响应。现有四足巡检系统常通过任务专用接口集成这些功能，导致上下文协调、知识复用和受控适应变得困难。

### 核心思路/方法
- 提出 Harness Robotic OS（HROS），一个统一的具身智能体运行时；Argos 是其面向住宅小区巡检的具体实现。
- HROS 将系统组织为机器人运行时、具身自主技能、认知智能体运行时、交互与运维平面。
- 通过共享上下文连接物理状态与智能体推理。
- 支持流式 ASR/TTS 的语音任务交互。
- 采用分层的工作记忆、情景记忆与语义记忆来保存运行知识。
- 设计安全门控的自演化闭环，将执行轨迹转化为带版本的候选更新，不允许无约束的在线修改。
- Argos 原型集成 Vbot 四足机器人、Fast-LIO2 定位与建图、Hobot-Stereo 深度感知、PCT-Planner 全局规划、EGO-Planner 局部运动生成，以及 OpenClaw 编排的 Qwen3-VL 巡检分析。

### 主要贡献
- 提出统一的具身智能体运行时 HROS，用于闭环四足巡检，缓解任务专用接口带来的上下文协调与知识复用困难。
- 给出 Argos 实现，将机器人运行时、自主技能、认知推理、语音交互和安全门控自演化组织为分层系统。
- 在住宅物业环境中验证部署的导航与巡检闭环，报告了 100% 航点可达率、户外定位误差低于 10 cm、局部障碍响应延迟低于 200 ms、代表性危险检测率 85–95%、告警投递与结构化报告生成成功率 99%。
- 摘要称 HROS 为记忆增强、语音感知且可持续改进的具身巡检智能体提供可扩展软件基础。

### 局限性
- 论文仅提供摘要，未提供关于实验规模、场景数量、基线对比、消融研究、失败案例和统计显著性的细节；这些信息摘要未提供足够信息。
- 危险检测率 85–95% 的具体类别、测试条件与误报情况，摘要未提供足够信息。
- 自演化闭环的版本管理机制、安全门控具体策略及其长期有效性，摘要未提供足够信息。
- 系统在住宅小区之外的泛化能力、不同机器人平台的可移植性，摘要未提供足够信息。
- 真实部署中的成本、维护、隐私与法规问题，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文聚焦具身智能体运行时与四足机器人闭环巡检的系统集成，涉及导航、感知、认知记忆、语音交互与安全自演化等完整链路，并给出可量化的部署指标；对具身智能系统落地、机器人操作系统架构和物业巡检应用有直接参考价值。但需注意仅凭摘要无法评估实验严谨性与泛化性，建议获取全文后重点核查实验细节与自演化机制。

</details>

<details>
<summary>Abstract</summary>

Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
