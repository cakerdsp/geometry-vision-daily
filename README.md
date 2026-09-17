# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：50
- 分类分布：
  - Embodied / Robotics / AR Applications: 17
  - Neural Scene Representations & Rendering: 15
  - 3D Reconstruction & Multi-view Geometry: 11
  - Geometry Foundation Models: 5
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **几何先验正在从“辅助模块”升级为“可靠性基础设施”**  
   NormLift、CADSplat、GeoCond、IRIS、Geometry beneath the Waves 均围绕同一核心矛盾：2D 语义、单目深度、稀疏视角或前馈基础模型预测的几何本身不可靠，直接使用会产生静默失败、语义错位或初始化瓶颈。今天的多条路线不再只追求端到端指标，而是把几何条件、几何先验或可靠性信号显式建模。GeoCond 以姿态级不确定性门控细化，NormLift 以特征范数作为语义可靠性信号，CADSplat 与水下 3DGS 工作则用 CAD 或稠密先验来约束可解空间，IRIS 试图在隐式渲染与显式 3D 之间寻找几何结构化折中。

2. **稀疏、无位姿、受限视角成为 3D 重建的默认困难设定**  
   CADSplat 面向少于 15 个宽基线视角，Geometry beneath the Waves 面向稀疏视角水下场景，IRIS 面向无位姿多视角，ORCA 面向单张图像的新视角探索，SOL-SLAM 面向仅前视声纳的局部 SLAM。这些论文的共同点是把“视角不足”当作研究前提，而不是补充实验条件。对应的方法取向是引入外部先验、物理模型或更适配的表示形式，而不是单纯扩大模型容量。

3. **4D/动态重建开始强调物理可解释性，而不只是光度拟合**  
   Wind on Trees 明确指出直接学习的变形场可能只优化光度一致性而未恢复真实运动，因此用阻尼谐振子先验与可微分 RK4 替代自由变形场，并设计受控合成测试台来检验物理参数是否被恢复。这与动态 4D 重建中长期存在的“拟合得好但物理不 grounding”问题直接相关，代表一种从“能渲染”转向“是否恢复物理机制”的评价思路。

4. **机器人与具身应用中的几何/语义表示开始服务于组合泛化与交互决策**  
   GraphPoint 关注子任务内和跨子任务的组合复用，AdaGeoVLN 关注几何基础模型在表示深度与导航时间上的选择性使用，PRISM 关注从被动观察中推断行人交互特质，PASSAGE 关注感知条件化的人形通行行为选择，DeformSmith 关注可变形资产的物理可信生成。它们共同表明：机器人方向对 3D 视觉的需求正在从“提供地图或位姿”转向“提供可组合、可选择性调用、可交互验证的结构化表示”。

5. **3DGS 生态继续向传输、SLAM、全景与单图探索等系统工程方向扩散**  
   MoQSplat 处理 GB 级 3DGS 数据的自适应流式传输，PanoGS-SLAM 将 3DGS SLAM 扩展到全景相机，ORCA 处理单图新视角中的去遮挡补全，CADSplat 与水下 3DGS 工作处理受限视角重建。3DGS 不再只是新视角合成方法，而是逐步成为覆盖采集、传输、跟踪、补全和交互的表示底座。

#### 技术路线观察

- **几何基础模型方向**：GeoCond 与 AdaGeoVLN 代表两种不同思路。GeoCond 不修改冻结骨干，只附加轻量可靠性适配器，输出姿态级不确定性与 refinement gate；AdaGeoVLN 则把 GFM 的层级中间表示按策略阶段耦合，并保留历史 VGGT 全局注意力 KV 状态。前者偏“诊断与门控”，后者偏“选择性融合与记忆”。两者共同指向一个判断：几何基础模型的末端输出可能不是最优使用方式，中间表示与可靠性信号同样重要。

- **3D/4D 重建方向**：CADSplat、水下 3DGS、IRIS、ORCA 和 Wind on Trees 分别处理稀疏宽基线、水下稀疏视角、无位姿、单图去遮挡和风驱动植被。技术路线分化明显：CADSplat 用检索到的 CAD 模型锚定高斯并联合优化形变场；水下工作强调稠密几何先验对初始化的作用；IRIS 用潜在神经场在自预测相机下查询；ORCA 按缺失区域大小决定 RGB-D 修复还是生成式修补；Wind on Trees 用物理参数化先验替代自由变形场。整体上，重建研究正在从“统一大模型”转向“按退化类型引入结构化约束”。

- **神经场景表示与渲染方向**：NormLift、MoQSplat、PanoGS-SLAM 和几何驱动阴影协调论文分别处理语义提升、传输、SLAM 和合成人脸重打光。NormLift 的理论贡献在于把逐高斯语义分配重新表述为 CLIP 单位球面上的余弦对齐问题，并给出 L2 归一化反投影特征的闭式解与范数分解。MoQSplat 则把 3DGS 内容映射到 MoQ 传输层次，用空间 Track、语义 Group 和渐进质量 Subgroup 组织数据。PanoGS-SLAM 在球面域做可微渲染与位姿优化，并补偿等距柱状投影的面积畸变。

- **机器人/AR 应用方向**：GraphPoint、PRISM、PASSAGE、DeformSmith、SOL-SLAM、水下协同定位折射偏差、CARLA 模仿学习与假肢感知姿态估计，共同构成一条从底层感知到高层决策的链条。SOL-SLAM 用稠密直接配准替代稀疏特征，PRISM 用潜空间交互特质补充几何状态，GraphPoint 用语义实体图与夹爪点轨迹连接语言和几何控制，PASSAGE 用大规模场景对齐动捕数据训练规划器—跟踪器，DeformSmith 用物理测试架闭环生成可变形资产。这些工作显示，机器人应用对 3D 视觉的评判标准正在从“感知精度”扩展到“是否支持组合泛化、交互验证与实时闭环”。

#### 值得优先阅读的论文

1. **NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting**  
   优先理由：它处理的是 3DGS 开放词汇理解中一个被广泛使用但理论解释不足的操作，即 2D 语义特征向 3D 高斯的提升。论文从 3D 侧将逐高斯分配建模为 CLIP 单位球面上的余弦对齐问题，并给出闭式解与范数分解，这对后续语义 3DGS、开放词汇查询和可靠性加权都有直接理论价值。

2. **GeoCond: A Conditioning-Aware Reliability Adapter for Feed-Forward 3D Reconstruction**  
   优先理由：前馈 3D 基础模型在低重叠、低视差和极端旋转下的静默失败是当前实际部署的关键风险。GeoCond 以轻量适配器输出姿态级不确定性和 refinement gate，且训练监督可来自帧置换轨道方差、真值姿态误差或无标签循环残差，兼顾了有标签与无标签场景，实用性强。

3. **CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction**  
   优先理由：它展示了在少于 15 个宽基线视角下，如何用 CAD 形状先验同时解决模型检索、相机—物体位姿和 3DGS 正则化。论文还指出渲染质量增益主要来自 splats 被约束的方式，而非 CAD 形状本身，这一观察对稀疏视角重建的后续设计有启发。

4. **Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting**  
   优先理由：它把 4D 动态重建的评价从光度拟合推进到物理参数恢复，并用受控合成测试台检验模型是否真正学到物理机制。对于关注动态 4D 重建、物理先验和可解释变形建模的研究者，这是方法论文与评测论文的结合。

5. **PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM**  
   优先理由：作为首个基于 3DGS 的全景稠密 SLAM 系统，它在球面域做可微渲染与位姿优化，并引入球面一致光度损失补偿等距柱状投影

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-17T12:57:45-04:00
**Total number of papers:** 50
**Number of papers added in the latest update:** 18
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

#### 2026-09-16 - AdaGeoVLN: Selective Geometry Across Representation Depth and Navigation Time for Vision-Language Navigation

**Authors:** Quan-Dung Pham, Anh Dao, Danh Vinh Le, Nguyen Viet Tri Pham, The-Anh Nguyen, Zhirui Dai, Yiyu Chen, Tuyen P. Le, Truong Nguyen, Quan Nguyen
**Links:** [abs](https://arxiv.org/abs/2609.18789) - [pdf](https://arxiv.org/pdf/2609.18789)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AdaGeoVLN: Selective Geometry Across Representation Depth and Navigation Time for Vision-Language Navigation
- 作者：Quan-Dung Pham, Anh Dao, Danh Vinh Le, Nguyen Viet Tri Pham, The-Anh Nguyen, Zhirui Dai, Yiyu Chen, Tuyen P. Le, Truong Nguyen, Quan Nguyen
- 出版日期：2026-09-16T15:10:04Z
- 分类：Geometry Foundation Models（主分类）；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2609.18789 ；PDF https://arxiv.org/pdf/2609.18789

### 一句话总结
论文提出 AdaGeoVLN，一个流式视觉语言导航框架，通过层级几何基础模型与 VLM 的多深度融合，以及导航感知的几何记忆保留机制，来同时处理“表示深度”和“导航时间”两个维度上的几何信息选择问题。

### 研究问题
视觉语言导航需要将语言与视觉观察对齐，并在时间维度上维持空间理解。几何基础模型（GFMs）在其层级结构中暴露了中间表示，但导航策略应如何使用这些特征、以及如何保留历史几何证据，仍尚未解决。论文聚焦两个问题：在表示深度上如何选择 GFM 特征，在导航时间上如何选择性保留历史几何信息。

### 核心思路/方法
- 提出 AdaGeoVLN，一个流式 VLN 框架，在“表示深度”和“导航时间”两个维度上处理几何特征使用问题。
- 层级 GFM–VLM 融合：将较早、中间和较晚的 GFM 表示分别耦合到连续的策略阶段，而不是反复注入末端特征。
- 导航感知 GFM 记忆：根据指令相关性、几何置信度和转移新颖性，在每层有界预算下保留历史 VGGT 全局注意力 KV 状态。
- 被保留的状态在融合到策略之前，为后续观察提供几何上下文。

### 主要贡献
- 提出跨表示深度的层级 GFM–VLM 融合方式，并指出在匹配融合位置时，多深度耦合显著优于反复注入末端特征。
- 提出导航感知的有界 GFM 记忆保留机制，在保持导航性能的同时，相较更大记忆的时序保留方式显著减少 GFM-KV 内存。
- 在 R2R-CE 和 RxR-CE 上，使用单一 RGB 流且不额外使用导航专用外部数据，取得较强性能。
- 研究结果表明，应联合考察暴露给策略的几何表示与为未来推理保留的历史证据。
- 代码将在接收后发布于 https://humanoid-research.github.io/adageovln/ 。

### 局限性
- 具体实验设置、基线对比细节、失败案例和计算开销的完整分析：摘要未提供足够信息。
- 不同场景下的泛化能力与鲁棒性：摘要未提供足够信息。
- 记忆预算的具体取值与敏感性分析：摘要未提供足够信息。
- 是否依赖特定 GFM 或 VLM 架构之外的其他假设：摘要未提供足够信息。

### 阅读优先级
中。理由：该论文关注 VLN 中几何基础模型层级特征使用与历史几何记忆保留这两个具体问题，并给出在 R2R-CE 与 RxR-CE 上的结果与消融结论；对几何基础模型与视觉语言导航交叉方向的研究者有直接参考价值。但摘要未提供完整实验细节与局限性讨论，是否需要精读取决于读者对多深度 GFM 融合与 KV 记忆压缩这一具体技术路线的兴趣。

</details>

<details>
<summary>Abstract</summary>

Vision-language navigation requires aligning language with visual observations while maintaining spatial understanding over time. Geometry foundation models (GFMs) expose intermediate representations throughout their hierarchy, but how navigation policies should use these features and retain historical geometric evidence remains unresolved. We introduce \method{}, a streaming VLN framework that addresses these questions across \textbf{representation depth} and \textbf{navigation time}. Hierarchical GFM--VLM fusion couples earlier, intermediate, and later GFM representations to successive policy stages instead of repeatedly injecting a terminal feature. Navigation-aware GFM memory retains historical VGGT global-attention KV states according to instruction relevance, geometric confidence, and transition novelty under a bounded per-layer budget. Retained states provide geometric context for subsequent observations before fusion with the policy. Across R2R-CE and RxR-CE, \method{} achieves strong performance using a single RGB stream without additional navigation-specific external data. Controlled ablations show that multi-depth coupling substantially outperforms repeated terminal-feature injection at matched fusion locations. Bounded navigation-aware retention preserves navigation performance while considerably reducing GFM-KV memory relative to larger-memory temporal retention. These findings support jointly examining the geometric representations exposed to the policy and the historical evidence retained for future inference. Code will be released upon acceptance at https://humanoid-research.github.io/adageovln/.

</details>

#### 2026-09-16 - GeoCond: A Conditioning-Aware Reliability Adapter for Feed-Forward 3D Reconstruction

**Authors:** David Ahmedt-Aristizabal, Mohammad Ali Armin, Russell Tsuchida, Lars Petersson
**Links:** [abs](https://arxiv.org/abs/2609.18465) - [pdf](https://arxiv.org/pdf/2609.18465)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, feed-forward 3D reconstruction, 3D reconstruction, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoCond: A Conditioning-Aware Reliability Adapter for Feed-Forward 3D Reconstruction
- 作者：David Ahmedt-Aristizabal, Mohammad Ali Armin, Russell Tsuchida, Lars Petersson
- 出版日期：2026-09-16T11:00:01Z
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.18465) / [PDF](https://arxiv.org/pdf/2609.18465)

### 一句话总结
GeoCond 是一个面向冻结的前馈式 3D 重建骨干网络的轻量可靠性适配器，通过读取已预测的几何信息来输出姿态级不确定性，从而在低重叠、低视差和极端相对旋转等困难条件下识别不可靠预测。

### 研究问题
前馈式 3D 基础模型（如 VGGT）能在单次前向中预测相机、深度和点图，但在低重叠、低视差和极端相对旋转条件下可能静默失败。摘要指出，针对这些因素的分层分析表明，这类失败由几何条件（geometric conditioning）主导，而模型原生的偶然不确定性（aleatoric confidence）难以充分刻画这些失败。因此，问题在于：如何在不改变冻结骨干网络的前提下，为其提供可靠的姿态级不确定性信号。

### 核心思路/方法
GeoCond 是一个轻量级可靠性适配器，附加在冻结的前馈式 3D 骨干网络之上。它读取骨干网络预测的几何信息，输出姿态级不确定性以及一个 refinement gate（细化门控）。训练监督来源包括三类：帧置换轨道方差（frame-permutation orbit variance）、在标签可用时的真值姿态误差，以及来自无标签独立姿态图的循环残差（cycle residuals）。推理时，默认头只需一次骨干网络前向和一个小型 MLP。摘要还提到，同一可靠性信号可支持门控细化、姿态图加权、校准、筛选和采集决策。

### 主要贡献
- 提出 GeoCond，一个面向冻结前馈式 3D 骨干网络的轻量可靠性适配器，输出姿态级不确定性与 refinement gate。
- 在 VGGT 上，将分布外（OOD）AUSE（sparsification-error curve 下面积，越低越好）从 0.32 改善至 0.20（相对原生置信度），并零样本迁移到户外极端视角场景。
- 避免了对所有情况统一应用 bundle adjustment 所导致的崩溃（collapse）。
- 在多个骨干网络上，循环蒸馏（cycle-distilled）变体提供了一条无需真值的适配路径，包括在等变模型上置换方差消失的情况。
- 表明同一可靠性信号可支持门控细化、姿态图加权、校准、筛选和采集决策。

### 局限性
摘要未提供足够信息。摘要未说明具体实验数据集、评价指标细节、计算开销、适配器参数量、失败案例或方法在何种条件下仍可能失效等信息。

### 阅读优先级
高。理由：该论文聚焦于前馈式 3D 基础模型在困难几何条件下的静默失败问题，提出了轻量适配器方案，并在摘要中报告了明确的 OOD AUSE 改进与零样本迁移结果；对于关注 3D 重建可靠性、不确定性估计和几何基础模型鲁棒性的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D foundation models such as VGGT predict cameras, depth, and point maps in a single pass, but can fail silently under low overlap, low parallax, and extreme relative rotation. Stratified analyses over these factors show that these failures are governed by geometric conditioning and are poorly captured by native aleatoric confidence. We introduce GeoCond, a lightweight reliability adapter for frozen feed-forward 3D backbones. GeoCond reads the backbone's predicted geometry and outputs pose-level uncertainty and a refinement gate. During training, it can be supervised by frame-permutation orbit variance, ground-truth pose error when labels are available, or cycle residuals from unlabelled independent pose graphs. At inference, the default head requires only one backbone pass and a small MLP. On VGGT, GeoCond improves out-of-distribution (OOD) AUSE (area under the sparsification-error curve; lower is better) from $0.32$ to $0.20$ over native confidence, transfers zero-shot to outdoor extreme-view scenes, and avoids the collapse caused by applying bundle adjustment uniformly. Across multiple backbones, cycle-distilled variants provide a ground-truth-free adaptation route, including cases where permutation variance vanishes on equivariant models. The same reliability signal supports gated refinement, pose-graph weighting, calibration, curation, and capture decisions. Reliable feed-forward 3D reconstruction requires not only predicting geometry, but also knowing when that geometry should be trusted.

</details>

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

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-15 - Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting

**Authors:** Weiying Chen, Edmond Lou
**Links:** [abs](https://arxiv.org/abs/2609.17810) - [pdf](https://arxiv.org/pdf/2609.17810)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting
- 作者：Weiying Chen, Edmond Lou
- 出版日期：2026-09-15T20:27:16Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.17810) ｜ [PDF](https://arxiv.org/pdf/2609.17810)

### 一句话总结
该论文用物理参数化的阻尼谐振子变形先验替代 4D Gaussian Splatting 中直接学习的变形场，并通过受控合成树木测试平台检验该先验是否真正具备物理基础，而非仅仅拟合观测数据。

### 研究问题
单目重建风驱动植被运动存在严重欠约束：沿视线方向的运动基本不可观测；移动树冠缺乏可靠对应关系；场景几乎整体动态，缺少静态参考。因此，4D Gaussian Splatting 中直接学习的变形场倾向于优化光度一致性，而非恢复产生该运动的真实物理运动。论文关注的核心问题是：引入物理参数化变形先验后，模型是否真正恢复物理规律，还是仅表现良好拟合。

### 核心思路/方法
- 用物理参数化的变形先验替代直接学习的变形场。
- 每个刚性部件建模为一个阻尼谐振子，由观测到的风驱动。
- 使用可微分 RK4 进行积分。
- 仅以光度监督进行训练。
- 构建受控合成测试平台：三棵程序化生成的树，骨架复杂度跨越一个数量级。
- 每个部件的固有频率由其自身几何决定，阻尼比为固定常数，二者均不参与训练。
- 评估维度包括：留出视角、时间外推、对未见风速的零样本迁移，以及物理参数本身的恢复情况。

### 主要贡献
- 提出将阻尼谐振子物理先验嵌入 4D Gaussian Splatting 的变形建模方式，并用可微分 RK4 积分、仅用光度监督训练。
- 构建了受控合成树木测试平台，用于检验物理先验是否真正“物理落地”，而非仅拟合训练分布。
- 报告了多维度评估结果：该先验在分布内视角上牺牲了外观保真度，但在训练时间窗口和训练风速之外的外推表现明显更好。
- 揭示了参数恢复的脆弱性：频率恢复仅在三棵树中最稀疏的一棵上能通过未训练的空对照，阻尼完全无法恢复。

### 局限性
- 摘要未提供足够信息说明真实场景数据上的验证结果；测试主要基于合成测试平台。
- 摘要未提供足够信息说明该方法在更复杂植被、多种风力条件或真实拍摄条件下的泛化表现。
- 摘要未提供足够信息说明计算成本、训练时间或与基线方法的定量对比细节。
- 论文自身指出：参数恢复远弱于表面印象，频率恢复仅在最稀疏树上通过未训练空对照，阻尼完全未恢复；这说明物理先验的“物理落地”程度有限。
- 摘要未提供足够信息说明失败案例的具体原因分析或改进方向。

### 阅读优先级
中。理由：该论文针对 4D Gaussian Splatting 中物理先验是否真正可恢复物理参数这一关键质疑，设计了受控测试并给出诚实的负面结果，对动态重建与神经场景表示方向有方法论参考价值；但摘要显示其验证主要在合成平台，且参数恢复结论偏消极，若读者关注真实场景应用或更强物理约束方法，需进一步阅读全文确认适用范围。

</details>

<details>
<summary>Abstract</summary>

Monocular reconstruction of wind-driven vegetation is severely underconstrained: motion along the viewing direction is largely unobservable, a moving canopy offers few reliable correspondences, and nearly the entire scene is dynamic, providing little static reference. Directly-learned deformation fields in 4D Gaussian Splatting therefore optimize photometric consistency rather than recover the motion that produced it. We replace that field with a physically parameterized deformation prior: one damped harmonic oscillator per rigid part, driven by the observed wind and integrated by differentiable RK4, supervised photometrically alone. To test whether such a prior is physically grounded rather than merely well fit, we build a controlled synthetic testbed of three procedurally generated trees spanning an order of magnitude in skeleton complexity, whose per-part natural frequency follows from its own geometry and whose damping ratio is a fixed constant, both held out of training. On it, we measure held-out views, temporal extrapolation, zero-shot transfer to unseen wind speeds, and recovery of the physical parameters themselves. The prior costs appearance fidelity on in-distribution views and extrapolates markedly better outside the training window and the training wind, while parameter recovery is far weaker than it first appears: frequency recovery survives an untrained null control on only the sparsest of the three trees, and damping is not recovered at all.

</details>

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

#### 2026-09-16 - SOL-SLAM: Inverse Compositional Gauss-Newton Direct Registration for Fast Sonar-Only Local SLAM

**Authors:** Kalvik Jakkala, Jason O'Kane
**Links:** [abs](https://arxiv.org/abs/2609.18893) - [pdf](https://arxiv.org/pdf/2609.18893)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SOL-SLAM: Inverse Compositional Gauss-Newton Direct Registration for Fast Sonar-Only Local SLAM
- 作者：Kalvik Jakkala, Jason O'Kane
- 出版日期：2026-09-16T16:25:11Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.18893

### 一句话总结
本文提出 SOL-SLAM，一种仅用前视声纳的稠密直接配准局部 SLAM 方法，通过逆向复合高斯-牛顿优化实现实时运行。

### 研究问题
自主水下导航通常依赖复杂昂贵的多模态传感器套件以保证全局 SLAM 精度，但粗导航和避障等局部反应行为只需局部一致性，理论上仅用前视声纳即可实现，然而这一问题尚未得到充分解决，形成了 FLS-only 局部 SLAM 的关键空白。此外，现有声学 SLAM 框架大多依赖稀疏特征提取，丢弃了本就信息稀疏的声学回波中的大量信息。

### 核心思路/方法
本文提出一种稠密直接配准方法，将完整的声学强度扫描与递归更新的局部地图对齐。为达到实时运行，采用逆向复合高斯-牛顿优化策略以最小化计算开销。

### 主要贡献
- 提出仅用前视声纳的局部 SLAM 方法，填补 FLS-only 局部 SLAM 的空白。
- 采用稠密直接配准，避免现有稀疏特征提取方法造成的信息丢失。
- 通过逆向复合高斯-牛顿优化实现实时执行，降低计算开销。
- 实验评估显示，相比稀疏关键点基线，该方法在平移误差上有显著改善，并在较大位移间隔下保持稳定的亚米级跟踪精度。
- 在特征丰富环境中，其里程计性能可与多传感器融合管线（FLS、DVL 和 IMU）相媲美，从而避免昂贵的载荷依赖。
- 通过 AUV 现场试验，在嵌入式资源受限计算机上机载运行完整局部 SLAM 方法，验证了实际适用性。

### 局限性
摘要未提供足够信息。摘要未提及方法在特征稀疏环境下的表现、失败案例、计算资源的具体量化指标、与多传感器融合管线对比的详细实验条件，以及现场试验的具体规模和评估细节。

### 阅读优先级
中。理由：该工作针对 FLS-only 局部 SLAM 这一特定空白，提出了稠密直接配准与逆向复合高斯-牛顿优化相结合的方案，并宣称在平移误差、亚米级跟踪精度和与多传感器融合管线可比性方面取得效果，还包含 AUV 现场试验。对水下声学 SLAM、直接配准或资源受限平台导航感兴趣的研究者具有参考价值；但摘要未提供充分的定量细节与局限性讨论，若需评估其方法通用性和可复现性，还需进一步阅读正文。

</details>

<details>
<summary>Abstract</summary>

Autonomous underwater navigation typically relies on complex and expensive multi-modal sensor suites designed to prioritize global Simultaneous Localization and Mapping (SLAM) accuracy. However, local reactive behaviors such as coarse navigation and obstacle avoidance require only local consistency---a capability that should be feasible using only a Forward-Looking Sonar (FLS), yet remains largely unaddressed, leaving a critical gap in FLS-only local SLAM. Moreover, existing acoustic SLAM frameworks predominantly rely on sparse feature extraction methods that discard substantial portions of the already information-sparse acoustic returns. To overcome these limitations, this work introduces a dense direct registration approach that aligns full acoustic intensity scans to a recursively updated local map. Real-time execution is achieved via an Inverse Compositional Gauss-Newton optimization strategy that minimizes computational overhead. Experimental evaluations show that this dense method yields significant improvements on translation error compared to sparse keypoint baselines, maintaining stable sub-meter tracking precision over wide displacement gaps. Moreover, this approach delivers odometry performance comparable to multi-sensor fusion pipelines (FLS, DVL, and IMU), bypassing expensive payload dependencies in feature-rich environments. We validate real-world applicability through AUV field trials, running the full local SLAM approach onboard an embedded, resource-constrained computer.

</details>

#### 2026-09-16 - Active perception for robotic harvesting: 3D reconstruction and localisation of tomatoes hidden within clusters in a Mediterranean greenhouse

**Authors:** Fernando Cañadas-Aránega, Rowan Border, José C. Moreno, José L. Blanco-Claraco
**Links:** [abs](https://arxiv.org/abs/2609.18738) - [pdf](https://arxiv.org/pdf/2609.18738)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, pose estimation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Active perception for robotic harvesting: 3D reconstruction and localisation of tomatoes hidden within clusters in a Mediterranean greenhouse
- 作者：Fernando Cañadas-Aránega, Rowan Border, José C. Moreno, José L. Blanco-Cláraco
- 出版日期：2026-09-16T14:33:08Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.18738；https://arxiv.org/pdf/2609.18738

### 一句话总结
该研究提出一套面向地中海温室番茄簇的主动感知与三维重建流水线，用于在严重遮挡条件下重建并定位簇内被遮挡的番茄果实。

### 研究问题
论文关注密集农业中机器人采摘的自动化问题，尤其是地中海温室环境下植物几何结构复杂、果实相互遮挡的挑战。摘要指出，现有文献多针对孤立生长的作物（如苹果、甜椒或桃），而簇生蔬菜中固定传感器安装在机器人系统上时，无法检测被可见表面遮挡的果实。因此，核心问题是：如何在簇生番茄中实现包括严重遮挡个体在内的完整三维重建与精确定位。

### 核心思路/方法
论文提出一条五阶段流水线，用于提取完整簇几何并识别部分隐藏的番茄：
1. 使用 AgriSEE Next Best View（NBV）主动规划器进行点云采集；
2. 通过 Statistical Outlier Removal（SOR）进行随机噪声滤波；
3. 使用 Region Growing（RG）进行表面分类与分割；
4. 通过 Density-Based Spatial Clustering of Applications with Noise（DBSCAN）分离并恢复被遮挡果实；
5. 进行三维位姿估计，包括位置与朝向。

该方法在模拟框架中、针对不同遮挡程度的多个场景进行了评估，该模拟框架据摘要称经过真实世界条件的严格验证。

### 主要贡献
- 提出一套针对簇生番茄的主动感知与三维重建流水线，覆盖从点云采集、滤波、分割到遮挡果实恢复与位姿估计的完整流程。
- 针对固定传感器无法检测簇内隐藏果实的问题，引入 NBV 主动规划与后续几何处理步骤，以提取完整簇几何并可靠识别部分隐藏番茄。
- 在多种遮挡程度的模拟场景中评估系统性能，报告 precision 超过 90%、平均 recall 为 82.8%、mIoU 为 80.7%。
- 报告质心估计具有高重复性，RMSE 仅为 4.2 mm，用于说明自主采摘操作的技术可行性与高精度。

### 局限性
摘要未提供足够信息说明真实温室实验规模、真实数据与模拟数据的差距、计算实时性、硬件平台细节、失败案例或泛化到其他作物与品种的能力。摘要仅说明评估在模拟框架中进行，并称该框架经过真实世界条件验证，但未提供具体验证方式与范围。

### 阅读优先级
高。理由：该论文聚焦机器人采摘中簇生作物严重遮挡这一关键难题，提出完整五阶段流水线，并给出 precision、recall、mIoU 与质心 RMSE 等量化指标；主题属于 3D Reconstruction & Multi-view Geometry，且与主动感知、农业机器人操作高度相关，适合优先阅读。

</details>

<details>
<summary>Abstract</summary>

Automating robotic harvesting in intensive agriculture within Mediterranean greenhouses requires overcoming significant challenges related to the geometric complexity of plants and occluded fruits. Although existing literature offers solutions targeting crops that grow in isolation (e.g., apples, sweet peppers, or peaches), the fundamental challenge lies in cluster-growing vegetables, where fixed sensors mounted on robotic systems fail to detect fruits hidden behind the visible surface. To address this limitation, this study presents a comprehensive pipeline for the 3D reconstruction and precise localization of each fruit within a cluster, including heavily occluded instances. The proposed methodology is structured into five sequential stages: i) point cloud acquisition using the AgriSEE Next Best View (NBV) active planner; ii) stochastic noise filtering via Statistical Outlier Removal (SOR); iii) surface classification and segmentation using Region Growing (RG); iv) isolation and recovery of occluded fruits through Density-Based Spatial Clustering of Applications with Noise (DBSCAN); and v) 3D pose estimation (position and orientation). This approach extracts the complete cluster geometry, ensuring the reliable identification of partially hidden tomatoes. Evaluated across multiple scenarios with varying occlusion levels within a simulation framework rigorously validated against real-world conditions, the system achieves a precision exceeding 90\%, an average recall of 82.8\%, and a mean Intersection over Union (mIoU) of 80.7\%. Furthermore, it demonstrates high repeatability in centroid estimation with a Root Mean Square Error (RMSE) of merely 4.2~mm, verifying its technical feasibility and high accuracy for autonomous harvesting operations.

</details>

#### 2026-09-16 - Prosthesis-Aware 3D Human Pose Estimation: A Dataset and Benchmark for RSP Users

**Authors:** Yilin Wen, Kechuan Dong, Fumiya Suginaka, Ken Endo, Yusuke Sugano
**Links:** [abs](https://arxiv.org/abs/2609.18406) - [pdf](https://arxiv.org/pdf/2609.18406)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Prosthesis-Aware 3D Human Pose Estimation: A Dataset and Benchmark for RSP Users
- 作者：Yilin Wen, Kechuan Dong, Fumiya Suginaka, Ken Endo, Yusuke Sugano
- 出版日期：2026-09-16T09:59:54Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.18406

### 一句话总结
针对跑步专用假肢（RSP）使用者，论文构建了首个 3D 数据集 RSP3D，正式定义了假肢感知 3D 姿态估计任务，并提出一个结合模型基身体关节估计与无模型 RSP 形状恢复的混合基线。

### 研究问题
从视频中恢复 3D 人体运动对康复评估和运动表现评价等应用很重要。对于假肢使用者，这一任务需要同时捕捉自然身体关节和假肢装置的几何形状，而现有方法并非为此设计：模型基估计器依赖在非截肢个体上训练的身体模型，无法表示假肢几何；无模型方法缺乏身体运动学先验，在遮挡下不可靠。这一问题在 RSP 使用者中尤为突出，因为 RSP 具有复杂的弯曲几何并在运动过程中动态移动。

### 核心思路/方法
论文通过多相机、基于标记点的运动捕捉装置，采集了 RSP3D——首个面向 RSP 使用者的 3D 数据集，覆盖参与者的关键日常生活和运动动作，并包含不同截肢情况。论文正式定义了假肢感知 3D 姿态估计任务，在零样本设定下评估了代表性方法并确认它们各自的局限。在此基础上，作者提出一个混合基线：将模型基身体关节估计与无模型 RSP 形状恢复相结合，作为未来研究的起点。

### 主要贡献
- 构建 RSP3D：据摘要称为首个 RSP 使用者的 3D 数据集，覆盖日常生活与运动动作，参与者截肢情况多样。
- 正式定义“假肢感知 3D 姿态估计”任务。
- 在零样本设定下评估代表性方法，确认其各自的局限。
- 提出一个混合基线，将模型基身体关节估计与无模型 RSP 形状恢复结合，为后续研究提供起点。

### 局限性
- 摘要未提供足够信息说明 RSP3D 的具体规模（参与者人数、序列数、帧数等）。
- 摘要未提供足够信息说明所评估的代表性方法具体是哪些，也未给出定量结果。
- 摘要未提供足够信息说明混合基线的具体精度、失败情形或消融实验。
- 摘要未提供足够信息说明数据采集的标记协议、相机数量、环境条件及数据多样性边界。
- 摘要未提供足够信息说明该方法是否能泛化到非 RSP 假肢或其他运动场景。

### 阅读优先级
高。理由：该工作同时涉及新数据集构建、新任务定义与基线方法，针对的是现有 3D 人体姿态估计方法明确未覆盖的假肢使用者群体；若研究兴趣在 3D 人体姿态估计、康复评估、运动分析或数据集与基准建设，该论文具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering 3D human body motion from video is important for applications such as rehabilitation assessment and sports performance evaluation. For prosthesis users, this requires capturing both natural body joints and the geometry of the prosthetic device, a challenge that existing methods are not designed to address. Model-based estimators rely on body models trained on non-amputee individuals and cannot represent prosthesis geometry, while model-free methods lack body kinematic priors and are unreliable under occlusion. This challenge is particularly prominent for users of running-specific prostheses (RSPs), where the RSP has a complex curved geometry and moves dynamically during exercise. To fill this gap, we collect RSP3D, the first 3D dataset of RSP users, covering essential daily-life and exercise actions from participants with varied amputation conditions, using a multi-camera marker-based motion capture setup. We formally define the task of prosthesis-aware 3D pose estimation, evaluate representative methods in a zero-shot setting, and confirm their individual limitations. We further propose a hybrid baseline combining model-based body joint estimation with model-free RSP shape recovery, establishing a starting point for future research.

</details>

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

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-16 - NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting

**Authors:** Yihan Zang, Da Li, Dominik Engel, Shinkyu Park, Ivan Viola
**Links:** [abs](https://arxiv.org/abs/2609.18898) - [pdf](https://arxiv.org/pdf/2609.18898)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting
- 作者：Yihan Zang, Da Li, Dominik Engel, Shinkyu Park, Ivan Viola
- 出版日期：2026-09-16T16:35:35Z
- 分类：Neural Scene Representations & Rendering
- 链接：abstract_url: https://arxiv.org/abs/2609.18898；pdf_url: https://arxiv.org/pdf/2609.18898

### 一句话总结
论文从 3D 侧重新审视 3D Gaussian Splatting 中的 2D 语义特征提升问题，将逐高斯分配建模为 CLIP 单位球面上的余弦对齐问题，并据此提出无需训练的 NormLift 框架，以特征范数作为语义可靠性信号来指导模式投票细化。

### 研究问题
论文关注的是：在开放词汇场景理解中，训练-free 的加权聚合常被用于把 2D 语义特征提升到 3D Gaussian 上，但其理论基础仍未被充分理解。现有分析多从渲染侧出发，把 Gaussian 特征视为可用于重建 2D 特征图的线性可组合欧氏变量；然而，这种观点与下游 3D 使用方式不一致，因为下游通常会在基于余弦的嵌入空间中独立查询每个 Gaussian。因此，论文要重新回答特征提升在 3D 侧应如何被理解和公式化。

### 核心思路/方法
论文从 3D 侧重新审视特征提升，将 per-Gaussian assignment 表述为 CLIP 单位球面上的余弦对齐问题。在该目标下，L2 归一化后的语义反投影特征成为闭式解，从而为标准的 lifting rule 提供一种来自逐高斯语义分配视角的互补解释。同一公式进一步给出范数分解，分为 intra-view consistency 与 inter-view consistency，说明特征幅值本身可以作为语义可靠性信号。该可靠性分数由有效的多视角支持进行校准，并用于指导一种 mode-voting refinement；该细化通过避免线性平均来保持 CLIP 特征的有效性。实验用于开放词汇 3D 语义分割，显示 NormLift 是高效、无需训练的框架，并在多种评估协议上取得较强性能。

### 主要贡献
- 从 3D 侧而非渲染侧重新审视 3D Gaussian Splatting 中的特征提升问题。
- 将逐高斯语义分配建模为 CLIP 单位球面上的余弦对齐问题。
- 指出 L2 归一化语义反投影特征是该目标下的闭式解，为标准 lifting rule 提供互补解释。
- 给出范数分解，将特征幅值解释为由 intra-view 和 inter-view consistency 构成的语义可靠性信号。
- 提出以有效多视角支持校准可靠性分数，并指导 mode-voting refinement，避免线性平均以保持 CLIP 特征有效性。
- 提出无需训练、高效的 NormLift 框架，并在开放词汇 3D 语义分割的多种评估协议上取得较强表现。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、计算开销数值、对不同数据集或协议的详细对比、超参数敏感性、对 CLIP 特征质量的依赖程度，以及方法在更广泛开放词汇任务上的适用边界。

### 阅读优先级
中。理由：该论文针对 3D Gaussian Splatting 中语义特征提升的理论解释与无需训练改进，问题定义清晰，且把余弦对齐、特征范数与语义可靠性联系起来，具有一定方法启发性；但摘要未提供充分实验细节与局限性信息，且主题较专门，适合关注 3D 场景表示、开放词汇 3D 理解或 CLIP 特征提升的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Training-free weighted aggregation is widely used to lift 2D semantic features onto 3D Gaussians for open-vocabulary scene understanding, yet its theoretical role remains insufficiently understood. Existing analyses typically justify this operation from the rendering side, treating Gaussian features as linearly composable Euclidean variables for reconstructing 2D feature maps. However, this view does not match downstream 3D usage, where each Gaussian is often queried independently in a cosine-based embedding space. We revisit feature lifting from the 3D side and formulate per-Gaussian assignment as a cosine alignment problem on the CLIP unit sphere. Under this objective, the L2-normalized semantic back-projected feature emerges as the closed-form solution, providing a complementary interpretation of the standard lifting rule from the perspective of per-Gaussian semantic assignment. The same formulation further yields a norm decomposition into intra-view and inter-view consistency, suggesting that feature magnitude itself can serve as a semantic reliability signal. Calibrated by effective multi-view support, this reliability score guides a mode-voting refinement that preserves CLIP feature validity by avoiding linear averaging. Experiments on open-vocabulary 3D semantic segmentation show that NormLift is an efficient, training-free framework that achieves strong performance across evaluation protocols.

</details>

#### 2026-09-16 - Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting

**Authors:** Harvey Caldeira, Haoran Wang, Guoxi Huang, Shaoyu Cai, Rachel Fu, Nantheera Anantrasirichai
**Links:** [abs](https://arxiv.org/abs/2609.18737) - [pdf](https://arxiv.org/pdf/2609.18737)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting
- 作者：Harvey Caldeira, Haoran Wang, Guoxi Huang, Shaoyu Cai, Rachel Fu, Nantheera Anantrasirichai
- 出版日期：2026-09-16T14:32:58Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.18737 ；PDF：https://arxiv.org/pdf/2609.18737

### 一句话总结
该论文针对稀疏视角水下 3D 高斯泼溅重建质量受限于初始化几何的问题，提出利用稠密先验来改善几何基础的研究方向（具体方法细节摘要未提供足够信息）。

### 研究问题
水下 3D 重建具有海洋生态监测、海底检测、水下考古、教育和沉浸式可视化等应用价值。3D Gaussian Splatting 已使实时逼真新视角渲染变得可行，而水下变体通过引入基于物理的成像模型来分离介质效应与场景辐射。然而，这些方法的重建质量从根本上仍受用于初始化的几何所限制。论文聚焦的问题正是：在稀疏视角水下场景中，如何通过更好的几何初始化/先验来突破这一瓶颈。

### 核心思路/方法
摘要仅指出核心关注点是“用于初始化的几何”以及“稠密先验（Dense Priors）”。标题暗示方法围绕为稀疏视角水下 3D Gaussian Splatting 提供稠密几何先验展开。具体网络设计、先验来源、损失函数、训练策略等，摘要未提供足够信息。

### 主要贡献
摘要未提供足够信息。可确认的仅为：论文提出/研究以稠密先验改善稀疏视角水下 3D Gaussian Splatting 几何初始化的方向，以缓解现有水下 3DGS 变体因初始化几何受限而导致的重建质量问题。具体贡献点、实验验证和量化结果均未在摘要中给出。

### 局限性
- 摘要未提供足够信息，无法判断方法的具体适用范围、对先验质量的依赖程度、计算开销、是否需额外输入或设备，以及在不同水体条件/稀疏程度下的表现。
- 摘要未提供实验设置、对比基线、数据集和定量指标，因此无法评估其相对现有水下 3DGS 方法的实际提升。
- 摘要未提供失败案例或边界条件讨论。

### 阅读优先级
中。理由：选题切中水下 3D Gaussian Splatting 中“初始化几何决定重建上限”的关键瓶颈，且稀疏视角与稠密先验的组合具有明确问题意识，属于神经场景表示与渲染方向下较有潜力的课题；但当前仅有标题与摘要，缺少方法细节、实验证据与量化结论，尚不足以判断其技术新颖性与实际效果是否显著，故定为中等优先级。若后续公开的方法与实验显示在稀疏视角水下场景上有稳定提升，可上调为高。

</details>

<details>
<summary>Abstract</summary>

Underwater 3D reconstruction supports applications ranging from marine ecosystem monitoring and subsea inspection to underwater archaeology, education, and immersive visualisation. 3D Gaussian Splatting has made real-time photorealistic novel-view rendering practical, while underwater variants incorporate physically based image-formation models to separate medium effects from scene radiance. Their reconstruction quality, however, remains fundamentally limited by the geometry used for initialisation.

</details>

#### 2026-09-16 - MoQSplat: Adaptive Progressive Streaming of 3D Gaussian Splatting via MoQ

**Authors:** Emanuele Artioli, Mohammadreza Ghafari, Md Tariqul Islam, Farzad Tashtarian, Christian Rothenberg, Christian Timmerer
**Links:** [abs](https://arxiv.org/abs/2609.18624) - [pdf](https://arxiv.org/pdf/2609.18624)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MoQSplat: Adaptive Progressive Streaming of 3D Gaussian Splatting via MoQ
- 作者：Emanuele Artioli, Mohammadreza Ghafari, Md Tariqul Islam, Farzad Tashtarian, Christian Rothenberg, Christian Timmerer
- 出版日期：2026-09-16T13:14:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.18624

### 一句话总结
MoQSplat 将 3D Gaussian Splatting 场景数据映射到 Media over QUIC（MoQ）传输层次上，通过空间 Track、语义 Group 与渐进质量 Subgroup 的分层组织，结合订阅端驱动的自适应请求机制，缓解传统 HTTP/TCP 自适应流式传输在细粒度 3DGS 交付中的队头阻塞与分段过粗问题。

### 研究问题
3D Gaussian Splatting 能实现逼真的新视角合成，但其场景数据可达 GB 级别，对沉浸式应用的传输构成挑战。传统基于 TCP 的 HTTP 自适应流式传输存在队头（HOL）阻塞，且其粗粒度分段方式不适合细粒度的 3DGS 交付。论文即针对这一问题，探索更适配 3DGS 数据特性的传输与自适应方案。

### 核心思路/方法
- 将 3DGS 内容映射到 Media over QUIC（MoQ）传输层次。
- 场景划分：把场景切分为空间上的 Tracks。
- 聚类：将 splats 聚类为语义一致的 Groups。
- 渐进质量：构造渐进质量的 Subgroups，并映射到相互独立的 QUIC 流上，以消除连接级 HOL 阻塞。
- 自适应机制：采用无状态、订阅端驱动的自适应循环，客户端依据六自由度（6-DoF）视锥可见性、距离与中央凹对齐（foveal alignment）动态请求空间区域与质量层级。
- 原型评估：在原型实现上评估核心组件，显示基于不透明度（opacity）的剪枝在渐进交付上优于基于尺度（scale）的剪枝。

### 主要贡献
- 提出 MoQSplat，将 3DGS 内容映射到 MoQ 传输层次，以支持细粒度交付。
- 设计空间 Track、语义 Group、渐进质量 Subgroup 的分层数据组织，并利用独立 QUIC 流规避连接级 HOL 阻塞。
- 提出无状态、订阅端驱动的自适应循环，依据 6-DoF 视锥可见性、距离和中央凹对齐请求空间区域与质量层级。
- 在原型实现上评估核心组件，得出基于不透明度的剪枝优于基于尺度的剪枝这一结论。
- 公开源代码（https://github.com/emanuele-artioli/MoQSplat）。

### 局限性
- 摘要仅说明在原型实现上评估了核心组件，未提供端到端系统性能、真实网络条件或大规模场景的评估细节。
- 除“基于不透明度的剪枝优于基于尺度的剪枝”外，摘要未提供与其他流式传输方案的定量对比结果。
- 摘要未提供所提自适应循环的延迟、带宽开销或质量-码率权衡的具体数据。
- 摘要未提供 Track/Group/Subgroup 划分策略的参数敏感性或构建开销信息。
- 摘要未提供 6-DoF 视锥、距离与中央凹对齐三者如何加权或组合的具体机制。
- 摘要未提供是否支持多用户、缓存或鲁棒性（丢包、抖动）方面的信息。

### 阅读优先级
中。理由：该论文聚焦 3DGS 的流式传输与自适应交付，将 3DGS 与 MoQ/QUIC 结合，问题定位清晰，且提供开源代码，对沉浸式媒体传输方向有参考价值；但摘要未给出端到端性能与横向对比等关键实验细节，需进一步阅读全文才能判断其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic novel view synthesis, but transmitting gigabyte-scale scene data remains challenging for immersive applications. Traditional HTTP Adaptive Streaming over TCP introduces Head-of-Line (HOL) blocking and coarse segmenting ill-suited to fine-grained 3DGS delivery. We propose MoQSplat, which maps 3DGS content onto the Media over QUIC (MoQ) transport hierarchy. MoQSplat partitions scenes into spatial Tracks, clusters splats into semantically coherent Groups, and constructs progressive-quality Subgroups mapped to independent QUIC streams to eliminate connection-level HOL blocking. Using a stateless, subscriber-driven adaptation loop, clients dynamically request spatial regions and quality tiers based on six degrees of freedom (6-DoF) frustum visibility, distance, and foveal alignment. We evaluate the core components on a prototype implementation, showing that opacity-based pruning outperforms scale-based pruning for progressive delivery. The source code is available at https://github.com/emanuele-artioli/MoQSplat.

</details>

#### 2026-09-16 - CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction

**Authors:** Kristof Overdulve, Lode Jorissen, Nick Michiels
**Links:** [abs](https://arxiv.org/abs/2609.18473) - [pdf](https://arxiv.org/pdf/2609.18473)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, augmented reality, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction
- 作者：Kristof Overdulve, Lode Jorissen, Nick Michiels
- 出版日期：2026-09-16T11:07:21Z
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：[摘要](https://arxiv.org/abs/2609.18473)｜[PDF](https://arxiv.org/pdf/2609.18473)

### 一句话总结
CADSplat 用显式 CAD 形状先验正则化 3D Gaussian Splatting，在少于 15 个稀疏宽基线视角下重建照片级真实且几何准确的物体数字孪生。

### 研究问题
从稀疏（<15 视角）、宽基线的已定位图像中重建物体的照片级真实且几何准确的数字孪生。使用 CAD 形状先验需要解决两个前提问题：找到与图像中物体形状相似的 CAD 模型，以及确定每个相机相对于物体的位姿。摘要指出，在视角最稀缺、物体强自遮挡的情况下，形状知识尤为关键。

### 核心思路/方法
- 通过将分割后的物体轮廓与从 CAD 库渲染的轮廓进行匹配，同时获得匹配的 CAD 模型和相机到物体的位姿（保留最佳匹配模型的相机—物体位姿）。
- 将 3D Gaussian 基元锚定在检索到的模型表面上。
- 联合优化 3DGS 参数、相机—物体配准，以及一个非刚性形变场，以补偿实物与 CAD 模型之间的形状差异。
- 摘要强调：渲染质量的大部分增益来自 splats 被约束的方式——一组固定在表面上、由单一平滑形变场驱动的固定 splats——而非 CAD 形状本身。

### 主要贡献
- 提出 CADSplat 框架，在稀疏宽基线已定位图像下以 CAD 形状先验正则化 3DGS。
- 通过轮廓匹配从 CAD 库同时完成模型检索与相机—物体位姿确定。
- 在表面锚定 splats，并联合优化 3DGS 参数、相机—物体配准与非刚性形变场。
- 在两个真实世界数据集上优于无约束、少样本和网格纹理化基线，并可优雅退化到仅 3 个视角。
- 分析表明渲染质量增益主要来自 splats 的约束方式，CAD 模型主要在视角最稀疏和强自遮挡时补充形状知识，并将每个相机置于物体自身坐标系中。
- 支持超越新视角合成的应用：无标记增强现实配准、逐图像物体位姿估计、物理仿真，以及将设计中的部件标签迁移到重建结果。

### 局限性
- 摘要未提供足够信息说明方法在 CAD 库中不存在相似模型时的表现。
- 摘要未提供足够信息说明轮廓分割失败或位姿初值不佳时的影响。
- 摘要未提供足够信息说明计算开销、运行时间与内存需求。
- 摘要未提供足够信息说明非刚性形变场能容忍的形状差异范围。
- 摘要提到“两个真实世界数据集”，但摘要未提供足够信息说明数据集构成、物体类别与评测指标细节。
- 摘要提到“3 个视角”的退化表现，但摘要未提供足够信息说明更少视角下的具体结果。
- 应用列举（AR 配准、位姿估计、物理仿真、部件标签迁移）为摘要所述潜力，摘要未提供足够信息说明这些应用的定量验证。

### 阅读优先级
高。理由：该工作针对稀疏视角 3DGS 这一明确痛点，提出 CAD 先验与表面锚定 splats 结合的具体方案，并给出“增益主要来自 splats 约束方式而非 CAD 形状本身”的反直觉结论；同时涉及数字孪生、AR 配准与机器人相关应用（次分类含 Embodied / Robotics / AR Applications），对稀疏重建与跨领域应用读者均有参考价值。

</details>

<details>
<summary>Abstract</summary>

We present CADSplat, a framework that reconstructs photorealistic, geometrically accurate digital twins from sparse ($<15$ views), wide-baseline posed images of an object by regularizing 3D Gaussian Splatting (3DGS) with an explicit CAD shape prior. Using such a prior requires finding a CAD model whose shape resembles the object depicted in the images and determining the pose of each camera relative to the object. We obtain both by matching segmented object silhouettes against silhouettes rendered from a CAD library and keeping the camera-to-object poses of the best-matching model. We then anchor 3D Gaussian primitives to the surface of the retrieved model and jointly optimize the 3DGS parameters, the camera-to-object registration, and a non-rigid deformation field to account for shape differences between the physical object and the CAD model. Across two real-world datasets, CADSplat outperforms unconstrained, few-shot, and mesh-texturing baselines and degrades gracefully to as few as 3 views. Our experiments show that most of the gain in rendering quality comes from how the splats are constrained---a fixed set of splats tied to a surface and moved by a single smooth deformation field---rather than from the CAD shape itself. The CAD model adds shape knowledge where views are scarcest, in the sparsest captures and on strongly self-occluded objects, and it places every camera in the object's own frame. This enables applications beyond novel-view synthesis, such as markerless augmented reality registration, per-image object pose estimation, physical simulations, and the transfer of part labels from the design to the reconstruction.

</details>

#### 2026-09-16 - IRIS: Implicit Rendering Matters for Pose-Free Novel View Synthesis

**Authors:** Wenyu Li, Sidun Liu, Peng Qiao, Yong Dou, Tongrui Hu
**Links:** [abs](https://arxiv.org/abs/2609.18034) - [pdf](https://arxiv.org/pdf/2609.18034)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IRIS: Implicit Rendering Matters for Pose-Free Novel View Synthesis
- 作者：Wenyu Li, Sidun Liu, Peng Qiao, Yong Dou, Tongrui Hu
- 出版日期：2026-09-16T02:35:22Z
- 分类：primary_category: Neural Scene Representations & Rendering；secondary_categories: 摘要未提供足够信息
- 链接：abstract_url: https://arxiv.org/abs/2609.18034；pdf_url: https://arxiv.org/pdf/2609.18034；项目页: https://leo-frank.github.io/IRIS

### 一句话总结
IRIS 是一个全自监督的、无位姿（pose-free）新视角合成框架，通过在自预测相机下查询潜在神经场进行渲染，在隐式潜在空间渲染与显式 3D 表示之间取得折中，以兼顾优化灵活性与几何结构。

### 研究问题
从无位姿的多视角图像进行新视角合成仍具挑战性，因为模型必须在没有位姿监督的情况下同时学习场景表示与相机参数。现有方法大致处于两个极端：
- 隐式潜在空间渲染灵活且易于优化，但相机估计往往缺乏几何依据（weakly grounded）；
- 显式 3D 表示具有更强的几何依据，但参数化更重、优化更脆弱。

### 核心思路/方法
IRIS 不再解码自由的潜在 token，也不重建完全显式的 3D 基元，而是：
- 将场景表示为潜在神经场（latent neural field）；
- 在自预测相机下查询该场来渲染新视角；
- 具体地，将参考视角的投影特征在采样 3D 点上聚合，形成逐点潜在特征，再沿目标光线组合以完成渲染。

该设计在保留隐式建模的灵活性与优化稳定性的同时，引入了比无约束潜在渲染更强的几何结构。

### 主要贡献
- 提出 IRIS，一个全自监督框架，在隐式潜在空间渲染与显式 3D 表示两种范式之间提供实用折中。
- 采用潜在神经场表示，并在自预测相机下通过聚合参考视角投影特征、沿目标光线组合的方式进行渲染。
- 据摘要所述，大量实验表明 IRIS 在全自监督学习下取得了良好的新视角合成质量，并具有有竞争力的位姿精度。

### 局限性
- 摘要未提供足够信息说明具体失败场景、边界条件或定量局限。
- 摘要未提供足够信息说明方法对特定数据分布、视角数量或场景类型的依赖与适用范围。
- 摘要未提供足够信息说明计算开销、训练效率或与基线方法的详细对比结果。
- 摘要未提供足够信息说明位姿精度与合成质量之间的权衡细节。

### 阅读优先级
中。理由：该论文聚焦无位姿新视角合成中隐式与显式表示的折中设计，问题定位清晰，方法思路具有一定的范式融合意义；但摘要未给出具体实验设置、定量结果与局限分析，是否值得深入阅读需结合全文的实验充分性与实际性能表现进一步判断。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis from unposed multi-view images remains challenging, as the model must jointly learn scene representations and camera parameters without pose supervision. Existing approaches largely fall into two extremes: implicit latent-space rendering is flexible and easy to optimize, but often yields weakly grounded camera estimation; explicit 3D representations provide stronger geometric grounding, but introduce heavier parameterization and more fragile optimization. In this paper, we present IRIS, a fully self-supervised framework that provides a practical middle ground between these two paradigms. Instead of decoding free latent tokens or reconstructing fully explicit 3D primitives, IRIS represents the scene as a latent neural field and renders novel views by querying this field under self-predicted cameras. Specifically, projected features from reference views are aggregated at sampled 3D points to form point-wise latent features, which are then composed along target rays for rendering. This design preserves the flexibility and optimization stability of implicit modeling, while introducing stronger geometric structure than unconstrained latent rendering. Extensive experiments show that IRIS achieves strong novel view synthesis quality with competitive pose accuracy under fully self-supervised learning. Our project page: https://leo-frank.github.io/IRIS

</details>

#### 2026-09-15 - Geometry-Driven Shadow Harmonisation for Composited Faces: A Multiplicative, Albedo-Preserving Relighting Pipeline

**Authors:** Vijesh KP
**Links:** [abs](https://arxiv.org/abs/2609.17740) - [pdf](https://arxiv.org/pdf/2609.17740)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry-Driven Shadow Harmonisation for Composited Faces: A Multiplicative, Albedo-Preserving Relighting Pipeline
- 作者：Vijesh KP
- 出版日期：2026-09-15T18:47:05Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.17740 ；PDF: https://arxiv.org/pdf/2609.17740

### 一句话总结
提出一种几何驱动的“仅变暗”乘性重打光流程，通过从三维人脸代理估计逐像素增益场并统一乘到线性 RGB 上，在不重绘人脸、不改变肤色与纹理的前提下，为合成人脸注入形体阴影以实现光影协调。

### 研究问题
人脸替换与合成流程通常得到几何对齐但光度不合理的脸：供体脸带有平坦的、近正面的影棚光照，而宿主身体与背景带有方向性场景光。现有补救方法（颜色迁移、神经重打光、逆渲染）往往存在改变身份、肤色和纹理的风险。论文要解决的是：如何在尽量不改变人脸本身外观属性的前提下，协调合成人脸与宿主场景的光照。

### 核心思路/方法
- 采用保守的替代方案：几何驱动的形体阴影注入，流程**从不重绘人脸**。
- 从栅格化的三维人脸代理估计逐像素增益场 g ∈ [g_min, 1]，并**按通道均匀**乘到线性 RGB 上，因此操作只能使像素变暗，且不会改变色度。
- 将密集关键点网格栅格化为深度缓冲，由此推导表面法线、空腔项（cavity term）和屏幕空间投射阴影。
- 主光方向从宿主侧线索估计（身体、背景、发丝光晕）；人脸自身的线索被降权，因为它们反映的是供体的光照。
- 阴影幅度不与宿主匹配，而是由三参数传递 (τ, σ, g_min) 设定。
- 阴影场先在皮肤区域按其第 75 百分位归一化，然后经过门控、缩放、截断、平滑，并在羽化的、皮肤门控的人脸掩码内重新裁剪。
- 在解析人脸高度场上，默认参数 (τ, σ, g_min) = (0.90, 0.45, 0.82) 修改了 56.5% 的人脸像素，平均增益 0.938（在被修改像素上为 0.890），3.4% 的像素被压到下限。色相不变性是该算子的推论。
- 论文对传递函数进行了闭式分析，消融其参数，并讨论了单调、仅变暗形式化的失败模式，包括非平坦供体的双重阴影问题。

### 主要贡献
- 提出一种乘性、保反照率（albedo-preserving）的几何驱动阴影协调流程，仅变暗且不改变色度。
- 使用密集关键点网格构建深度缓冲以推导法线、空腔与屏幕空间投射阴影，并从宿主侧线索估计主光方向。
- 给出基于三参数 (τ, σ, g_min) 的阴影幅度传递设计，并在解析人脸高度场上给出定量结果。
- 对传递函数进行闭式分析与参数消融，并讨论了该单调、仅变暗方法的失败模式，如非平坦供体的双重阴影。

### 局限性
- 论文自述其失败模式包括：单调、仅变暗形式化带来的限制，以及非平坦供体的双重阴影（double-shadowing）问题。
- 摘要未提供足够信息说明该方法的定量评测指标（如身份保持度量、与基线的对比实验、用户研究等）。
- 摘要未提供足够信息说明其在真实合成管线中的运行效率、泛化性与大规模数据集验证情况。
- 摘要未提供足够信息说明除解析人脸高度场之外的实验设置与结果细节。

### 阅读优先级
中。理由：该工作提出的“仅变暗、保色度”的乘性重打光思路在概念上简洁且对合成人脸管线有实用价值，并对失败模式有自省式讨论；但摘要仅给出解析高度场上的定量结果，缺少与现有方法的对比评测与真实场景验证，是否值得深入阅读取决于读者对光照协调/人脸合成这一具体方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Face swapping and face compositing pipelines routinely produce a face that is geometrically well aligned but photometrically implausible: the donor face carries flat, near-frontal studio illumination while the host body and background carry directional scene light. Most existing remedies re-synthesise the face through colour transfer, neural relighting, or inverse rendering, and therefore risk altering identity, skin tone, and texture. We present a conservative alternative: geometry-driven form-shadow injection. The pipeline never repaints the face. It estimates a per-pixel gain field $g\in[g_{\min},1]$ from a rasterised 3D face proxy and multiplies it channel-uniformly onto linear RGB, so the operator can only darken and cannot shift chromaticity. A dense landmark mesh is rasterised into a depth buffer, from which we derive surface normals, a cavity term, and screen-space cast shadows. Key-light direction is estimated from host-side cues (body, background, hair halo); on-face cues are downweighted because they recover the donor's lighting. Shadow magnitude is not matched to the host: it is set by a three-parameter transfer $(τ,σ,g_{\min})$. The shading field is divided by its 75th percentile over skin, then gated, scaled, clamped, smoothed, and re-clipped inside a feathered, skin-gated face mask. On an analytic face heightfield, the default $(τ,σ,g_{\min})=(0.90,0.45,0.82)$ modifies 56.5% of face pixels with mean gain 0.938 (0.890 on modified pixels) and drives 3.4% of pixels to the floor. Hue invariance is a corollary of the operator. We analyse the transfer in closed form, ablate its parameters, and discuss failure modes of a monotone, darkening-only formulation, including double-shadowing of non-flat donors.

</details>

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

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-16 - PASSAGE: Scaling Scene-Aligned Motion Learning for Perceptive Humanoid Traversal in Cluttered Environments

**Authors:** Yuxuan Ma, Zicheng Zeng, Chunlin Peng, Zhoujian Li, Zetong Zhao, Zhikai Zhang, Yunrui Lian, Han Xue, Sikai Liang, Weiyi Zhu, Mulin Chen, Chenghuai Lin, Jiayu Zeng, Yanwei An, Songan Zhang, Jiayuan Gu, Jilong Wang, Jingbo Wang, He Wang, Li Yi
**Links:** [abs](https://arxiv.org/abs/2609.18732) - [pdf](https://arxiv.org/pdf/2609.18732)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, virtual reality, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PASSAGE: Scaling Scene-Aligned Motion Learning for Perceptive Humanoid Traversal in Cluttered Environments
- 作者：Yuxuan Ma, Zicheng Zeng, Chunlin Peng, Zhoujian Li, Zetong Zhao, Zhikai Zhang, Yunrui Lian, Han Xue, Sikai Liang, Weiyi Zhu, Mulin Chen, Chenghuai Lin, Jiayu Zeng, Yanwei An, Songan Zhang, Jiayuan Gu, Jilong Wang, Jingbo Wang, He Wang, Li Yi
- 出版日期：2026-09-16T14:30:52Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.18732) / [PDF](https://arxiv.org/pdf/2609.18732)

### 一句话总结
PASSAGE 提出一种感知条件化的“规划器—跟踪器”框架，利用大规模场景对齐的人类动捕数据训练人形机器人在杂乱环境中自主选择并组合跨越、侧身通过、低头躲避等通行行为，并在真实机载感知与计算条件下完成无需预建地图的实物测试。

### 研究问题
人形机器人虽然具备跨越、侧身挤过、低头钻过障碍等能力，但如何从机载感知中学习**选择并协调**这些行为仍然困难。现有方法多依赖任务特定的强化学习目标或人工整理的动作库，导致行为覆盖面的扩展成本高昂。论文关注的核心问题是：能否不依赖技能标注或障碍专用策略，仅用统一框架实现复杂杂乱场景下的通用人形通行？

### 核心思路/方法
- **数据收集**：使用虚拟现实与惯性动捕，在 1,500 个杂乱场景中采集 100 小时场景对齐的人类运动数据。
- **框架结构**：采用感知条件化的规划器—跟踪器（planner–tracker）框架。
- **规划器**：条件流匹配（conditional flow-matching）规划器，输入为运动历史、局部目的地以及以机器人为中心的多层高程图，输出短时域参考动作。
- **跟踪器**：感知式全身跟踪器，以 50 Hz 执行参考动作，并利用几何反馈进行校正。
- **一致性机制**：实时分块（real-time chunking）促进块间一致性。
- **后训练**：在冻结跟踪器的条件下，对规划器侧进行强化学习后训练，以提升闭环性能。
- **能力特点**：无需技能标注或障碍专用策略，单一规划器—跟踪器对即可在未见几何结构上选择与组合通行行为。

### 主要贡献
- 提出 PASSAGE，一种用于人形通行的感知条件化规划器—跟踪器框架。
- 构建了 100 小时、覆盖 1,500 个杂乱场景的场景对齐人类运动数据集。
- 通过仿真中的组件消融实验，量化各阶段的贡献。
- 在三个独立训练种子下，将采集数据从 6 小时扩展至 100 小时，使留出场景上的平均无接触成功率从 48.1% 提升至 68.9%；结合经验证的场景增强后，最终模型达到 70.3%。
- 实现完全机载系统：集成第一人称 3D LiDAR 感知、在线占据建图、6.25 Hz 规划与 50 Hz 控制，运行于 Jetson AGX Orin；在 50 个未见物理布局上测试，无需预建地图或离线计算即可完成通行。

### 局限性
摘要未提供足够信息。摘要未说明该系统的失败案例、安全性边界、能耗与实时性权衡、仿真与实物性能差距、数据采集成本，以及与基线方法的详细对比结果。

### 阅读优先级
高。理由：该工作同时涉及大规模场景对齐动捕数据、感知条件化流匹配规划、全身跟踪与真实机载部署，且给出了多随机种子下的数据规模缩放结果与 50 个未见实物布局测试，对具身智能与人形机器人通行研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Humanoid robots can step over, squeeze past, and duck under obstacles, but learning to select and coordinate these behaviors from onboard perception remains challenging. Many existing approaches rely on task-specific reinforcement-learning objectives or curated motion libraries, making broad behavioral coverage costly. We present PASSAGE, a perception-conditioned planner--tracker framework for humanoid traversal. Using virtual reality and inertial motion capture, we collect 100 h of scene-aligned human motion across 1,500 cluttered scenes. A conditional flow-matching planner generates short-horizon references from motion history, a local destination, and a robot-centric multi-layer elevation map, while a perceptive whole-body tracker executes them at 50 Hz with geometric feedback. Real-time chunking promotes inter-chunk consistency, and planner-side RL post-training under the frozen tracker further improves closed-loop performance. Without skill annotations or obstacle-specific policies, one planner--tracker pair selects and composes traversal behaviors across unseen geometries. In simulation, component ablations quantify the contribution of each stage. Across three independent training seeds, scaling captured data from 6 to 100 h increases mean contact-free success from 48.1% to 68.9% on held-out scenes, while the final model with validated scene augmentation reaches 70.3%. The fully onboard system integrates egocentric 3D LiDAR perception, online occupancy mapping, 6.25 Hz planning, and 50 Hz control on a Jetson AGX Orin; tests across 50 unseen physical layouts demonstrate traversal without prebuilt maps or offboard computation.

</details>

#### 2026-09-16 - DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation

**Authors:** Can Li, Jie Gu, Zishun Deng, Jingmin Chen, Lei Sun
**Links:** [abs](https://arxiv.org/abs/2609.18620) - [pdf](https://arxiv.org/pdf/2609.18620)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation
- 作者：Can Li, Jie Gu, Zishun Deng, Jingmin Chen, Lei Sun
- 出版日期：2026-09-16T13:10:34Z
- 分类：Embodied / Robotics / AR Applications（未提供二级分类）
- 链接：[摘要](https://arxiv.org/abs/2609.18620) / [PDF](https://arxiv.org/pdf/2609.18620) / [项目页](https://can-lee.github.io/deformsmith-web/)

### 一句话总结
DeformSmith 是一个从文本或单张图像自动生成可变性资产（几何、外观、物理属性）的框架，通过分层智能体式构建与共享的物理“测试架”（harness）来逐步生成、测试和精炼资产，并利用机器人交互反馈闭环，使其可用于仿真与操作。

### 研究问题
为机器人操作创建可变性资产需要同时指定几何、外观和物理属性。对可变性物体而言，文本和图像对“如何变形、如何响应接触”提供的信息有限，而这些响应直接决定资产是否适合交互。因此自动化生成需要解决耦合的物理需求，并利用交互证据来指导构建与精炼。

### 核心思路/方法
- 从文本或单张图像出发，自动生成可交互、物理可信的可变性资产。
- 采用分层智能体式（hierarchical agentic）构建流程，配合一个共享的、以物理为基础的测试架（physics-grounded harness）。
- 逐步构建、测试并精炼几何、物理模型、材料行为以及机器人交互，直到资产可用于仿真与操作。
- 通过操作反馈与可回放的交互数据，使机器人交互闭合生成循环。

### 主要贡献
- 提出 DeformSmith 框架，实现从文本或单图自动生成可交互、物理可信的可变性资产。
- 引入分层智能体式构建与共享物理测试架，用于联合处理几何、物理模型、材料行为与机器人交互的生成与精炼。
- 通过机器人操作反馈与可回放交互数据闭合生成循环。
- 摘要称其在视觉质量与物理合理性上优于 PhysGen3D、PhysGM、PhysX-Omni 等基线，并支持为可变性物体的机器人操作合成数据。

### 局限性
摘要未提供足够信息。摘要未提及方法的失败情形、计算成本、对特定物体类别或任务范围的限制、真实机器人部署的验证程度，以及基线对比的具体指标与实验设置。

### 阅读优先级
高。理由：该工作面向具身智能与机器人操作中的可变性资产生成这一关键且具挑战性的问题，提出将物理测试架与机器人交互反馈纳入生成闭环的思路，若关注仿真到操作的资产构建与数据合成，具有较强相关性；但具体实验细节需查阅原文确认。

</details>

<details>
<summary>Abstract</summary>

Creating deformable assets for robot manipulation requires jointly specifying their geometry, appearance, and physical properties. This is especially challenging for deformable objects, since text and images provide limited evidence about how they deform and respond to contact, yet these responses directly affect their suitability for interaction. Automated generation therefore needs to resolve coupled physical requirements and use interaction evidence to guide construction and refinement. We present DeformSmith, a framework that enables automated generation of interactive, physically credible deformable assets from text or a single image. Through hierarchical agentic construction and a shared physics-grounded harness, it progressively builds, tests, and refines geometry, physical models, material behavior, and robot interaction until the resulting asset is ready for simulation and manipulation. Robot interaction closes the generation loop through manipulation feedback and replayable interaction data. Results show that DeformSmith generates assets with better visual quality and physical plausibility than state-of-the-art baselines, including PhysGen3D, PhysGM, and PhysX-Omni, while supporting the synthesis of data for robotic manipulation of deformable objects. Project page: https://can-lee.github.io/deformsmith-web/

</details>

#### 2026-09-16 - GraphPoint: Semantic Entity Graphs and Point Trajectories for Compositional Robot Manipulation

**Authors:** Kang Luo, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2609.18358) - [pdf](https://arxiv.org/pdf/2609.18358)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GraphPoint: Semantic Entity Graphs and Point Trajectories for Compositional Robot Manipulation
- 作者：Kang Luo, Hesheng Wang
- 出版日期：2026-09-16T09:17:32Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.18358) / [PDF](https://arxiv.org/pdf/2609.18358)

### 一句话总结
论文提出 GraphPoint 框架，通过语义实体图与夹爪点轨迹预测来提升机器人操作策略在组合式指令与长时程任务中的泛化能力，并引入 CoMani 基准用于评估。

### 研究问题
机器人操作策略在超出演示范围时泛化能力不足，即使新指令涉及熟悉的对象和行为。当训练中语言与场景强相关时，策略可能学到固定的视觉-动作映射，而非真正响应所请求的行为。论文关注两个层面的组合式复用：子任务内（组合熟悉的实体、动作类型和动作修饰语）与跨子任务（在未见过的长时程任务中复用已学子任务）。

### 核心思路/方法
- 提出 CoMani 基准，包含受控的数据划分，用于评估上述两个层面的组合泛化能力。
- CoMani 通过匹配初始场景并仅对单一语义因素进行受控变化，促使策略依赖语言而非视觉捷径。
- 提出 GraphPoint 框架，将语义实体图与几何控制相连接：预测未来的夹爪点轨迹，并利用机器人几何将其转换为动作。
- 框架按语义角色组织夹爪与物体，并以动作类型和修饰语为条件建模其交互。
- 预测的进度在执行过程中引导子任务之间的切换。

### 主要贡献
- 识别并形式化了机器人操作中两个层面的组合式复用问题。
- 提出 CoMani 基准，支持对子任务内组合与跨子任务复用进行受控评估。
- 提出 GraphPoint 方法，结合语义实体图与夹爪点轨迹预测，并利用机器人几何生成动作。
- 在 CoMani 上的实验与消融验证了所提方法在两个层面的指令依赖泛化上的有效性。

### 局限性
- 摘要未提供足够信息说明方法的计算开销、对真实机器人平台的迁移效果、对传感器噪声或环境扰动的鲁棒性。
- 摘要未提供足够信息说明 CoMani 基准的规模、任务数量、对象类别覆盖范围及与其他基准的对比。
- 摘要未提供足够信息说明失败案例、方法的具体假设或适用边界。
- 代码仅声明“将发布”，摘要未提供足够信息说明当前可复现性状态。

### 阅读优先级
中。理由：论文聚焦机器人操作策略的组合泛化与指令依赖泛化，问题定义清晰，且同时提出基准与方法，对具身智能与机器人操作方向的研究者有参考价值；但摘要未提供实验规模、真实机器人验证及具体性能数据，尚不足以判断其实际影响力和可复现性，因此不宜定为高优先级。

</details>

<details>
<summary>Abstract</summary>

Robot manipulation policies often struggle to generalize beyond their demonstrations, even when new instructions involve familiar objects and behaviors. When language and scenes are strongly correlated during training, a policy can learn a fixed visual-action mapping rather than respond to the requested behavior. We investigate compositional reuse at two levels: within a subtask, combining familiar entities, action types, and action modifiers; and across subtasks, reusing learned subtasks in unseen long-horizon tasks. We introduce CoMani, a benchmark with controlled splits for evaluating both capabilities. Matched initial scenes and controlled changes to a single semantic factor encourage reliance on language rather than visual shortcuts. We further propose GraphPoint, which connects semantic entity graphs to geometric control by predicting future gripper point trajectories and converting them into actions using robot geometry. The framework organizes the gripper and objects by semantic roles and conditions their interactions on action types and modifiers, while predicted progress guides transitions during execution. Experiments and ablations on CoMani validate the effectiveness of our method for instruction-dependent generalization at both levels. Code will be released at GraphPoint.

</details>

#### 2026-09-16 - PRISM: Predictive Representation of Interaction Style and Motion for Social Robot Navigation

**Authors:** Bo-Han Chen, Hiromu Taketsugu, Norimichi Ukita
**Links:** [abs](https://arxiv.org/abs/2609.18125) - [pdf](https://arxiv.org/pdf/2609.18125)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PRISM: Predictive Representation of Interaction Style and Motion for Social Robot Navigation
- 作者：Bo-Han Chen, Hiromu Taketsugu, Norimichi Ukita
- 出版日期：2026-09-16T05:01:27Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.18125 ；PDF: https://arxiv.org/pdf/2609.18125

### 一句话总结
PRISM 通过被动观察人与人交互来推断行人的交互特质，并将其编码为连续有序潜空间表示，同时配合时间稳定性分数供导航策略使用，以改善机器人在动态人群中的社交导航。

### 研究问题
论文关注的是人群中的机器人导航问题：现有方法通常主要用观测到的几何状态来表示行人，而将个体在交互倾向上的差异隐式忽略。论文希望解决如何从被动观察中推断行人的交互特质，并将这些特质用于社交导航决策。

### 核心思路/方法
PRISM 从被动观察到的人与人交互中推断交互特质。具体而言，它将人类轨迹编码到一个连续的有序潜空间中，使用 transformer 编码器，并通过 Rank-N-Contrast loss 进行训练。每个推断出的特质会与一个时间稳定性分数配对，该分数被提供给导航策略，用于 crowd navigation。

### 主要贡献
- 提出 PRISM 框架，用于从被动观察到的人与人交互中推断交互特质。
- 使用 transformer 编码器将人类轨迹编码到连续有序潜空间，并以 Rank-N-Contrast loss 训练。
- 将推断出的特质与时间稳定性分数结合，并输入导航策略。
- 在随机人群仿真中，相比仅使用几何状态的基线，PRISM 降低了碰撞率，并在导航时间和路径长度指标上有小幅改善。

### 局限性
- 摘要未提供足够信息说明真实世界实验、真实人群场景或非仿真环境中的验证情况。
- 摘要未提供足够信息说明数据集规模、仿真设置细节、基线完整列表、评价指标数值和统计显著性。
- 摘要未提供足够信息说明时间稳定性分数的具体计算方式、消融实验以及计算成本。
- 摘要未提供足够信息说明该方法的失败场景、安全边界或对不同人群分布的泛化能力。

### 阅读优先级
中。理由：该论文聚焦社交机器人导航中行人交互特质的被动推断，问题定义清晰，方法要素明确，并且在随机人群仿真中报告了碰撞率下降及导航时间、路径长度的小幅改善。但摘要未提供真实世界验证、详细实验设置和充分数值结果；若关注社交导航、行人建模或潜特质推断，可优先阅读，否则可作为中等优先级参考。

</details>

<details>
<summary>Abstract</summary>

Humans often observe others before interacting and adjust their behavior accordingly. Robot navigation in crowds, however, often represents pedestrians mainly by observed geometric states, leaving individual differences in interaction tendencies implicit. We propose PRISM (Predictive Representation of Interaction Style and Motion), a framework that infers interaction traits from passive observations of human-human interactions. PRISM encodes human trajectories into a continuous ordinal latent space with a transformer encoder trained by Rank-N-Contrast loss, and pairs each inferred trait with a temporal-stability score supplied to the navigation policy. In randomized crowd simulations, PRISM reduces collision rates over the geometry-only baseline and yields small improvements in navigation-time and path-length metrics. These results suggest the utility of passive latent-trait inference for social navigation in dynamic crowds.

</details>

#### 2026-09-16 - Characterizing Refraction-Induced Ranging Bias in Underwater Collaborative Localization

**Authors:** Timothy Kogucki, Alan Papalia
**Links:** [abs](https://arxiv.org/abs/2609.18073) - [pdf](https://arxiv.org/pdf/2609.18073)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Characterizing Refraction-Induced Ranging Bias in Underwater Collaborative Localization
- 作者：Timothy Kogucki, Alan Papalia
- 出版日期：2026-09-16T03:19:51Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.18073

### 一句话总结
该工作通过仿真研究水下声学测距中的折射偏差如何在公里尺度上影响多智能体协同定位，并指出在声速梯度剧烈的区域，估计轨迹会出现显著退化。

### 研究问题
论文关注的是：折射引起的测距偏差（refraction-induced ranging bias）如何影响多智能体协同定位，尤其是在不同海洋条件和空间尺度下。摘要指出，多智能体测距辅助导航虽然是大范围水下定位的有前景方案，但其精度强烈依赖测距质量；而标准传感器融合流程为了算法可处理性假设声线直线传播，这与实际声速变化导致的声线折射（弯曲）不符。折射会系统性地使测距结果比直线假设预测的更长，但这种偏差对公里尺度多智能体协同定位的影响此前尚未被充分探索。

### 核心思路/方法
论文采用一系列仿真实验，让多个智能体在公里尺度上运行。仿真中使用 HYCOM 再分析数据重建真实海洋条件，使用射线追踪生成包含折射信息的测距值，并使用集中式多智能体因子图估计器来量化由此产生的测量偏差对估计轨迹的影响。作者还公开了仿真环境以支持后续研究。

### 主要贡献
- 研究了折射引起的测距偏差在多种海洋条件和空间尺度下对多智能体协同定位的影响。
- 构建了基于 HYCOM 再分析数据、射线追踪和集中式多智能体因子图估计器的仿真实验框架。
- 初步结果表明，折射引起的偏差可导致估计轨迹显著退化，尤其是在声速梯度剧烈的区域。
- 公开了仿真环境以支持进一步研究（https://github.com/UMich-RobotExploration/manta-ray）。

### 局限性
摘要未提供足够信息说明实验的具体规模、智能体数量、定量误差指标、不同海洋条件之间的系统比较，以及与真实数据的验证情况。摘要仅报告了“初步结果”，未提供足够信息说明方法的完整适用范围或失败边界。

### 阅读优先级
中。理由：该论文聚焦水下协同定位中一个具体但重要的误差来源，问题定义清晰，且提供了可复用的仿真环境，对水下机器人导航与多智能体定位方向有参考价值；但摘要仅给出初步结果，缺少定量细节和真实环境验证信息，因此优先级为中等而非高。

</details>

<details>
<summary>Abstract</summary>

This work studies how refraction-induced bias on acoustic ranging affects multi-agent collaborative localization in a range of oceanographic conditions and spatial scales. While multi-agent range-aided navigation, which uses range measurements to either fixed infrastructure or other agents, is a promising solution to the challenges of large-scale underwater localization, its accuracy depends strongly on the quality of range measurements. Sound speed variability induces refraction (bending) of acoustic rays, yet, for algorithmic tractability, standard sensor fusion pipelines assume straight-line propagation. This refraction systematically biases range measurements to be longer than the straight-line assumption predicts. However, the effects of this bias on multi-agent collaborative localization on kilometer scales remains unexplored. We present a series of simulated experiments with several agents operating over kilometer scales. The simulation uses HYCOM reanalysis data to recreate realistic oceanographic conditions, ray tracing to generate refraction-informed ranges, and a centralized multi-agent factor graph estimator to quantify the resulting measurement bias on estimated trajectories. Preliminary results indicate that refraction-induced bias can induce significant degradation of estimated trajectories, particularly in regions with sharp sound-speed gradients. We also share the simulation environment to support further studies https://github.com/UMich-RobotExploration/manta-ray.

</details>

#### 2026-09-15 - Imitation Learning for Autonomous Driving in CARLA

**Authors:** Jordy Kieto
**Links:** [abs](https://arxiv.org/abs/2609.17757) - [pdf](https://arxiv.org/pdf/2609.17757)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Imitation Learning for Autonomous Driving in CARLA
- 作者：Jordy Kieto
- 出版日期：2026-09-15T19:08:03Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.17757 ；https://arxiv.org/pdf/2609.17757

### 一句话总结
该论文研究一个紧凑的多模态策略能否仅通过 CARLA 中的离线专家演示，获得闭环自动驾驶能力。

### 研究问题
论文关注行为克隆在自动驾驶中的核心矛盾：策略在离线专家演示上训练，但部署是闭环的，每一步动作都会影响后续观测。作者希望研究紧凑多模态策略在 CARLA 模拟器中，从离线演示中能获得多少闭环驾驶能力。

### 核心思路/方法
- 采用行为克隆，在离线专家演示上训练策略。
- 策略输入为五帧历史信息，包括 RGB 图像、LiDAR、车辆遥测和车道航点。
- 输出为油门、刹车和转向，控制频率为 20 Hz。
- 演示数据分三阶段收集，最后阶段使用系统性路线生成流程：枚举生成点和可行机动，并验证已完成的自动驾驶路线。
- 训练数据为 236,882 个窗口，来自 448 次采集，约 3.3 小时驾驶数据。
- 发布的策略参数量为 1.36 million。
- 论文报告离线指标，并区分实测结果与定性闭环观察。
- 发布内容包括代码、训练检查点、ONNX 模型、数据样本以及证据审计。

### 主要贡献
- 研究并展示了一个紧凑多模态策略在 CARLA 中从离线演示学习闭环驾驶的可行性。
- 构建了包含三阶段收集流程的演示数据，并提出系统性路线生成与验证流程。
- 训练出的策略可在训练路线和留出路线上自主驾驶数小时。
- 在作者运行中，该策略未发生碰撞，并在定性上迁移到一个具有不同道路几何结构的未见 CARLA 城镇。
- 作者还观察到策略能从较大轨迹偏差中恢复，但明确不声称在无控制评估下具有系统性恢复能力。
- 发布代码、训练检查点、ONNX 模型、数据样本和证据审计，以支持所报告结论。

### 局限性
- 摘要未提供足够信息说明系统性恢复能力，作者明确表示未进行受控评估，因此不声称系统性恢复。
- 摘要未提供足够信息说明离线指标的具体数值、类型或对比结果。
- 摘要未提供足够信息说明闭环测试的路线数量、驾驶时长统计、碰撞率统计细节或评估协议。
- 摘要未提供足够信息说明迁移到未见 CARLA 城镇的定量结果，仅提到定性迁移。
- 摘要未提供足够信息说明与其它方法的比较、消融实验或模型架构细节。
- 摘要未提供足够信息说明真实世界部署或 CARLA 之外环境的泛化能力。

### 阅读优先级
- 优先级：中
- 理由：该论文关注行为克隆在闭环自动驾驶中的实际能力，提供了 CARLA 中的多模态策略、较大规模离线演示数据以及开放资源，适合对自动驾驶模仿学习、闭环评估和 CARLA 实验感兴趣的研究者阅读。但摘要未给出具体定量闭环结果、系统对比或受控恢复评估，因此若关注严格基准比较或真实世界泛化，其直接参考价值可能有限。

</details>

<details>
<summary>Abstract</summary>

Behavioral cloning trains a policy offline on expert demonstrations, but deployment is closed loop: each action affects the observations the policy receives next. We study how much closed-loop driving competence a compact multimodal policy can acquire from offline demonstrations in the CARLA simulator. The policy uses five-frame histories of RGB images, LiDAR, vehicle telemetry, and lane waypoints to predict throttle, brake, and steering at 20 Hz. Demonstrations were collected in three stages, ending with a systematic route-generation procedure that enumerates spawn points and feasible maneuvers and verifies completed autopilot routes. The released 1.36 million parameter policy was trained on 236,882 windows, representing about 3.3 hours of driving from 448 captures. The resulting policy drives autonomously for hours on training and held-out routes. In our runs, it did so without collisions and also transferred qualitatively to an unseen CARLA town with different road geometry. We also observed recovery from large trajectory deviations, although we do not claim systematic recovery without controlled evaluation. We report offline metrics and distinguish measured results from qualitative closed-loop observations. We release the code, trained checkpoint, ONNX model, data sample, and an evidence audit for the reported claims.

</details>

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

#### 2026-09-15 - Visual Cue Guided Video Planning for Generalizable Robot Navigation

**Authors:** Hojin Lee, Sizhe Lester Li, Maximilian Hilger, Susie Lu, Achim J. Lilienthal, Vincent Sitzmann, Daniel A. Duecker
**Links:** [abs](https://arxiv.org/abs/2609.16737) - [pdf](https://arxiv.org/pdf/2609.16737)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visual Cue Guided Video Planning for Generalizable Robot Navigation
- 作者：Hojin Lee, Sizhe Lester Li, Maximilian Hilger, Susie Lu, Achim J. Lilienthal, Vincent Sitzmann, Daniel A. Duecker
- 出版日期：2026-09-15T07:11:21Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.16737) / [PDF](https://arxiv.org/pdf/2609.16737)

### 一句话总结
CueNav 通过鸟瞰图与机器人本体视觉线索引导视频规划，并结合特定具身的逆动力学模型将视频计划转化为机器人动作，以提升长时程与具身感知的导航泛化能力。

### 研究问题
论文关注现有生成式视频模型用于机器人导航时的两个不足：
1. 长时程规划尚未充分探索，已有方法常依赖短时程引导；
2. 视频到动作的精确转换不够充分，已有方法多通过场景重建恢复几何路点。

因此，论文希望解决如何利用视频规划实现更长时程、更精确且更具泛化性的机器人导航。

### 核心思路/方法
论文提出 CueNav，一个基于视频模型的导航框架，主要由两部分构成：
1. **视觉线索引导的视频规划**：
   - 使用鸟瞰图（BEV）地图作为视觉线索，传达全局任务上下文；
   - 在自我中心观测中保留部分机器人本体，以暴露具身上下文；
   - 这些线索共同引导视频规划器。
2. **具身特定逆动力学模型（IDM）**：
   - 将视频计划中提取的密集流场转换为机器人动作；
   - 实现视频到动作的精确映射。

摘要指出，带有全局任务上下文的视觉线索编码使 CueNav 在迷宫导航中的成功率接近无线索规划的两倍；结合本体感知视图与 IDM，在狭窄通道中达到 70% 成功率，而对比方法大多无法完成该任务。

### 主要贡献
1. 提出 CueNav，将视觉线索引导的视频规划与具身特定 IDM 结合，用于机器人导航。
2. 引入 BEV 地图作为全局任务上下文线索，以及保留机器人本体的自我中心视图作为具身上下文线索。
3. 通过 IDM 将视频计划中的密集流场转化为机器人动作，探索精确的视频到动作转换。
4. 展示零样本语义条件导航，以及同一视频规划器在不同机器人平台上的部署。
5. 摘要报告了迷宫导航成功率接近 2 倍提升，以及在狭窄通道中 70% 成功率的结果。

### 局限性
摘要未提供足够信息。未提供关于失败案例、计算开销、真实世界部署规模、安全性、不同任务类型下的泛化边界等局限性的具体说明。

### 阅读优先级
**高**。理由：该论文聚焦视频生成模型在机器人导航中的长时程规划与视频到动作转换问题，并报告了迷宫导航、狭窄通道、零样本语义条件导航和跨平台部署等结果；若关注具身智能、机器人导航或视频模型用于决策，具有较高参考价值。

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
