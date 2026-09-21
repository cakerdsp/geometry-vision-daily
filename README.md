# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：76
- 分类分布：
  - Embodied / Robotics / AR Applications: 27
  - Neural Scene Representations & Rendering: 24
  - 3D Reconstruction & Multi-view Geometry: 16
  - Geometry Foundation Models: 7
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **3D Gaussian Splatting 从“能重建”转向“能维护、能压缩、能进入生产管线”**
   本次窗口内多篇论文不再以新视角合成质量为唯一目标，而是处理高斯表示的工程化约束：PhGS 针对单视图前馈 3DGS 的射线级冗余做后处理剪枝与循环精修；EliGSiR 针对在线 RGB-D 连续建图，在有限算力预算下做视图调度、保真度自适应和几何定向增长；GS-PI 试图把烘焙辐射度的 GS 解耦为可重光照的 PBR 资产；RawSLAM 与 VGGT-GS SLAM 则把高斯表示嵌入 SLAM 的在线优化循环。这反映出一条共同诉求：高斯泼溅正从“离线、封闭、长优化”的演示范式，迁移到“在线、开放、预算受限、需与下游管线兼容”的系统范式。

2. **几何基础模型与前馈先验成为三维重建/SLAM 的新“底座”**
   GRF-Recon 明确归入 Geometry Foundation Models，用 LoRA 把单目几何线索蒸馏进前馈主干，并做全局射线场优化以缓解长序列漂移；VGGT-GS SLAM 直接以前馈 VGGT 位姿与深度为先验，再做子图可微 BA 与未标定内参/畸变优化。二者与 PhGS 形成对照：一派是把基础模型当作可微调或可注入先验的骨架，另一派是把基础模型冻结、只在其输出上做后处理。无论哪派，共同点是承认单目/前馈先验已足够强，研究重心转向“如何把先验接进需要长期一致性和标定自由度的系统”。

3. **物理与接触建模从“渲染真实感”扩展到“交互与决策”**
   SplashSplat 处理真实飞溅液体，其核心原则是“仅在观测可约束处施加物理结构”，并用水平集传输与拉格朗日载体补充动态；Feel-WM 把本体感觉引入越野导航世界模型，要求同时预测“相机将看到什么”和“机器人将感受到什么”；SnapPhysics 从单图估计质量、摩擦、重心并构建物理感知场景图；DexTouch-WM 用人类触摸数据训练动作条件触觉世界模型。这一组论文的共同趋势是：三维/四维表示不再只服务于观看，而是要为接触、打滑、倾倒、抓取等物理交互提供可决策的状态。

4. **语义、语言与多智能体协作开始叠加在高斯地图之上**
   CoRef-GS 将“指代式”语言查询放到多智能体独立重建并融合后的高斯地图上，要求几何可对齐、实例级语义可比、以及视角条件化的关系推理；Semantic SLAM 在精准农业中用贝叶斯推断维护物体及其语义属性的概率地图。二者说明语义高斯地图的研究前沿已从“单图/单智能体查询”走向“融合地图上的跨视角、跨智能体推理”。

5. **评测与系统级验证成为独立且紧迫的议题**
   SLAMSqueezeBench 指出多数 SLAM 系统在隔离环境测试却报告为独占资源，提出在边缘硬件上施加计算/内存约束并模拟丢帧；VA-Bench 要求 MLLM 完成“观察—推理—行动—修正”闭环且不给出特权位姿或 oracle 轨迹；AURORA 强调生成场景不仅要能执行，还要忠实实现用户要求的空间、时间、通信与行为关系。这与前述工程化趋势一致：领域正在补“可信、可比较、可约束”的评测基础设施。

#### 技术路线观察

- **几何基础模型方向**：GRF-Recon 与 VGGT-GS SLAM 代表两种接入方式。GRF-Recon 用 LoRA 适配把单目几何线索蒸馏进前馈主干，并叠加混合权重稀疏射线场优化和轨迹拼接，重点在长单目序列的全局一致性与可扩展性；VGGT-GS SLAM 则把 VGGT 作为初始化先验，随后用子图可微 BA 联合优化位姿、高斯地图、共享内参与径向—切向畸变，并用 Gaussian-native alignment 做子图间尺度精化与回环验证。前者偏“训练时注入”，后者偏“推理时优化”，但都依赖前馈模型提供足够好的初值。

- **3D/4D 重建方向**：SplashSplat 是本次窗口中最具 4D 色彩的工作，处理真实飞溅液体这种几乎无纹理、视角依赖、难以追踪的对象，方法上把逐帧液体 SDF、水平集传输得到的粗速度场、拉格朗日载体推进与局部高斯解码串起来。Printing the Underdetermined 则从另一个角度切入 4D/多解问题：不追求单一可恢复三维场景，而是用视频生成模型采样多条相机环绕序列，分别重建为高斯表示，并让密度光晕与鬼影显式暴露未解决的自由度。两者共同表明，动态重建正在从“缓慢形变表面”和“合成液体”走向更极端、更不适定的真实动态。

- **神经场景表示方向**：PhGS、GS-PI、EliGSiR、RawSLAM 四篇集中体现表示层的分化。PhGS 关注前馈单视图生成的冗余压缩，保持骨干冻结、只做后处理；GS-PI 关注材质与光照解耦，把 PBR 属性生成建成几何条件下的 3D 点云扩散过程，再蒸馏回高斯；EliGSiR 关注持续建图中的预算分配，把视图调度、监督分辨率和几何增长都变成可控变量；RawSLAM 关注 HDR 线性辐射度输入，用无 MLP 的对数颜色参数化、Reinhard 压缩光度目标和结构引导梯度加权实现在线跟踪与建图。四者分别对应压缩、解耦、预算、动态范围四个不同的“表示可用性”维度。

- **机器人/AR 应用方向**：可再分为三类。其一是交互与操作，DexTouch-WM、AnyViewDex、SnapPhysics、VA-Bench 分别从触觉世界模型、视角不变策略、单图物理属性估计和具身空间智能评测切入，共同点是都在减少对测试时特权 3D 传感或人工标注的依赖。其二是导航与野外场景，Feel-WM 把本体感觉作为世界模型条件，Semantic SLAM 把语义属性概率地图与图优化 SLAM 结合用于农田。其三是系统与协同验证，VAST 做 V2X/动态地图感知的自动驾驶验证工具链，AURORA 做自然语言驱动的空地协同仿真编译与验证，SLAMSqueezeBench 则提供资源约束下的 SLAM 比较框架。整体上，应用侧论文不再只报告单一任务成功率，而是更多涉及跨组件互操作、资源约束和关系忠实性。

#### 值得优先阅读的论文

1. **SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos**
   理由：本次窗口中最具“新问题定义”价值的工作。它同时贡献了据称首个同步多视角飞溅液体基准和一套“仅在可观测处施加物理结构”的方法原则，对动态重建、物理仿真与神经渲染交叉方向的研究者都有直接参考意义。若该基准与评测划分如摘要所述可用，可能成为后续飞溅/破碎/颗粒动态重建的常用起点。

2. **GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction**
   理由：直接触及前馈重建扩展到长单目序列时的三个硬约束——显存、局部几何退化、长期漂移。其 LoRA 几何先验注入加混合权重稀疏射线场优化的组合，是理解“几何基础模型如何与经典优化互补”的一个清晰样本，适合关注长序列 SLAM/重建统一框架的读者。

3. **VGGT-GS SLAM: Uncalibrated Monocular Gaussian Splatting SLAM with Feed-Forward Priors**
   理由：把前馈 VGGT 先验、子图可微 BA、解析标定雅可比和 Gaussian-native alignment 组合进未标定单目高斯 SL

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-18T12:22:06-04:00
**Total number of papers:** 64
**Number of papers added in the latest update:** 27
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

#### 2026-09-17 - GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction

**Authors:** Enpeng Li, Yunzhou Zhang, Zhiyao Zhang, Dexuan Lyu, Chenyu Wang, Chiyuan Cui, Cheng Cheng
**Links:** [abs](https://arxiv.org/abs/2609.20012) - [pdf](https://arxiv.org/pdf/2609.20012)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward reconstruction, feed-forward 3D reconstruction, 3D reconstruction, SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction
- 作者：Enpeng Li, Yunzhou Zhang, Zhiyao Zhang, Dexuan Lyu, Chenyu Wang, Chiyuan Cui, Cheng Cheng
- 出版日期：2026-09-17T10:21:52Z
- 分类：Geometry Foundation Models（主类）；3D Reconstruction & Multi-view Geometry（次类）
- 链接：[摘要](https://arxiv.org/abs/2609.20012) | [PDF](https://arxiv.org/pdf/2609.20012)

### 一句话总结
本文提出 GRF-Recon，一个面向长单目序列的馈送式 3D 重建统一框架，通过粗到细轨迹对齐、几何先验注入与混合权重稀疏射线场优化，在保持可扩展性的同时提升全局一致性与轨迹精度。

### 研究问题
摘要指出，馈送式 3D 重建虽能高效建模，但在扩展到大规模单目场景时面临三重约束：GPU 显存占用过大、局部几何退化、长期轨迹漂移。现有基于分块（chunk-based）的优化策略几何约束有限，难以在长轨迹上维持全局一致性。

### 核心思路/方法
- 构建粗到细的轨迹对齐流程，并辅以轻量级几何先验注入。
- 通过 LoRA 适配将单目几何线索蒸馏进馈送式主干，在保持推理效率的同时提升精细结构上的深度精度。
- 提出混合权重稀疏射线场优化，利用高频几何特征引导局部点云精化，并施加一致的帧间射线约束；与既有分块方法相比，建立强跨帧几何耦合且保持可扩展性。
- 采用带联合射线误差优化的高效轨迹拼接策略，显式减少累积漂移。

### 主要贡献
- 提出面向长单目序列的稳定、可扩展馈送式 3D 重建统一框架。
- 将单目几何先验以 LoRA 方式蒸馏进馈送式主干，兼顾精细结构深度精度与推理效率。
- 设计混合权重稀疏射线场优化，实现跨帧几何耦合下的局部点云精化。
- 提出联合射线误差优化的轨迹拼接策略以抑制长期漂移。
- 摘要称实验表明其轨迹精度可与代表性 SLAM 系统竞争，并在大规模场景中保持全局一致的 3D 重建。

### 局限性
- 摘要未提供足够信息说明具体实验数据集、评测指标数值、与 SLAM 系统对比的详细结果。
- 摘要未提供足够信息说明方法的计算开销、实时性、显存占用的量化结果。
- 摘要未提供足够信息说明在极端场景（如剧烈运动、弱纹理、动态物体）下的表现。
- 摘要未提供足够信息说明 LoRA 适配、射线场优化中各超参数的影响与消融结果。

### 阅读优先级
中。理由：该工作针对长序列馈送式重建的显存、局部几何与轨迹漂移等明确痛点，方法组合（几何先验蒸馏 + 稀疏射线场 + 轨迹拼接）具有一定新意，且主类为 Geometry Foundation Models，与 3D 重建方向相关度高；但摘要未给出量化实验细节与开源信息，若关注具体性能提升幅度或工程落地，需进一步阅读全文验证。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction provides an efficient paradigm for scene modeling from image sequences. Scaling these models to large monocular scenarios are constrained by excessive GPU memory footprint, degraded local geometry, and long-term trajectory drift. Existing chunk-based optimization strategies provide limited geometric constraints and fail to maintain global consistency over extended trajectories. We present a unified framework for stable and scalable feed-forward 3D reconstruction from long monocular sequences. Our approach builds on coarse-to-fine trajectory alignment augmented by lightweight geometric prior injection. Distilling monocular geometric cues into the feed-forward backbone via LoRA adaptation improves depth accuracy on fine structures while preserving inference efficiency. We introduce a hybrid-weight sparse ray-field optimization that leverages high-frequency geometric features to guide local point-cloud refinement and enforce consistent inter-frame ray constraints. Unlike prior chunk-based methods, this establishes strong cross-frame geometric coupling while maintaining scalability. Finally, an efficient trajectory stitching strategy with joint ray-error optimization explicitly reduces accumulated drift. Extensive experiments show that our approach achieves competitive trajectory accuracy compared with representative SLAM systems, while maintaining globally consistent 3D reconstruction in large-scale scenarios.

</details>

#### 2026-09-17 - VGGT-GS SLAM: Uncalibrated Monocular Gaussian Splatting SLAM with Feed-Forward Priors

**Authors:** Yuhang Han, Hao Wang, Jiaxi Cao, Xingyu Liu
**Links:** [abs](https://arxiv.org/abs/2609.19628) - [pdf](https://arxiv.org/pdf/2609.19628)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** VGGT, SLAM, bundle adjustment, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VGGT-GS SLAM: Uncalibrated Monocular Gaussian Splatting SLAM with Feed-Forward Priors
- 作者：Yuhang Han, Hao Wang, Jiaxi Cao, Xingyu Liu
- 出版日期：2026-09-17T03:18:23Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry、Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.19628) / [PDF](https://arxiv.org/pdf/2609.19628)

### 一句话总结
论文提出 VGGT-GS SLAM，一个面向未标定单目视频的 3D Gaussian Splatting SLAM 系统，借助前馈 VGGT 位姿与深度先验，联合优化相机参数、位姿与三维高斯地图。

### 研究问题
摘要指出，该工作针对的是**未标定视频（uncalibrated videos）**下的单目 3D Gaussian Splatting SLAM 问题。其关注点包括：在缺少标定信息的情况下进行定位与建图，并在未标定设置下提升定位精度与渲染质量。摘要未提供足够信息说明其具体应对的失败模式、评价指标细节或与既有方法的定量差距。

### 核心思路/方法
- 以**前馈 VGGT 位姿与深度先验**作为起点。
- 执行**子图可微 bundle adjustment**，联合精化相机位姿与 3D Gaussian 地图。
- 通过**解析标定雅可比**优化子图共享的内参以及径向—切向畸变。
- 引入 **Gaussian-native alignment（GNA）**，用于序列子图之间以相机为锚的尺度精化，并用于回环候选的验证，以提升全局一致性。

### 主要贡献
- 提出 VGGT-GS SLAM，一个面向未标定视频的单目 3D Gaussian Splatting SLAM 系统。
- 将前馈 VGGT 位姿与深度先验引入子图可微 bundle adjustment，联合优化相机位姿与 3D Gaussian 地图。
- 通过解析标定雅可比在优化中处理子图共享内参与径向—切向畸变。
- 提出 Gaussian-native alignment（GNA），用于子图间相机锚定尺度精化与回环候选验证。
- 摘要称在标准室内基准上，未标定设置下定位精度与渲染质量有一致提升，并称其为未标定 Gaussian SLAM 的强基线。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算开销、对 VGGT 先验质量的依赖程度、评测数据集名称与规模、消融实验细节、与基线方法的定量比较结果，以及是否适用于室外或大规模场景。上述内容均无法仅凭给定摘要判断。

### 阅读优先级
**中**。理由：该论文处于几何基础模型、三维重建与神经场景表示/渲染的交叉点，主题明确，方法要素（前馈先验、可微 BA、解析标定、GNA）具有参考价值；但当前仅有摘要，缺少实验数据、基线对比与消融细节，是否值得优先精读取决于读者对未标定单目 Gaussian SLAM 或 VGGT 先验应用的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

We present VGGT-GS SLAM, a monocular 3D Gaussian Splatting SLAM system designed for uncalibrated videos. Starting from feed-forward VGGT pose and depth priors, our system performs submap differentiable bundle adjustment that jointly refines camera poses and a 3D Gaussian map, while optimizing submap-shared intrinsics and radial--tangential distortion through analytic calibration Jacobians. To improve global consistency, we introduce Gaussian-native alignment (GNA) for camera-anchored scale refinement between sequential submaps and verification of loop-closure candidates. Extensive experiments on standard indoor benchmarks show consistent improvements in localization accuracy and strong rendering quality under uncalibrated settings, establishing a strong baseline for uncalibrated Gaussian SLAM.

</details>

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

#### 2026-09-17 - Underwater Visual Target Tracking with Target-Specific Depth Estimation and Adaptive Model-Fusion Predictive Control

**Authors:** Yuheng Zhou, Haiyang Cheng, Yanqi Feng, Pangkit Fong, Mei Xuan Lee, Marcus Gee, Chongrong Fang, Jianping He
**Links:** [abs](https://arxiv.org/abs/2609.20731) - [pdf](https://arxiv.org/pdf/2609.20731)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Underwater Visual Target Tracking with Target-Specific Depth Estimation and Adaptive Model-Fusion Predictive Control
- 作者：Yuheng Zhou, Haiyang Cheng, Yanqi Feng, Pangkit Fong, Mei Xuan Lee, Marcus Gee, Chongrong Fang, Jianping He
- 出版日期：2026-09-17T17:22:01Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2609.20731 ，PDF https://arxiv.org/pdf/2609.20731

### 一句话总结
面向自主水下航行器（AUV），该论文提出一种立体视觉伺服框架，通过目标特定的深度估计与卡尔曼滤波获得稳定三维相对状态，并用自适应模型融合预测控制实现实时平移控制。

### 研究问题
摘要指出，基于视觉的水下目标跟踪面临两个主要挑战：深度测量不可靠，以及目标运动未知。论文即针对这两点，为 AUV 构建水下视觉目标跟踪方案。

### 核心思路/方法
论文方法的要点（均来自摘要）如下：

- 总体框架：为 AUV 提出立体视觉伺服（stereo visual-servoing）框架。
- 感知端：
  - 通过目标特定的深度提取（target-specific depth extraction）和卡尔曼滤波，从立体图像得到稳定的三维相对状态。
  - 利用颜色、视差和时间线索构建目标深度掩码（target-depth mask），以选出可靠的目标像素。
  - 对得到的深度测量和检测到的图像中心分别进行滤波。
- 控制端：
  - 将偏航调节（yaw regulation）与平移控制解耦，从而避免计算开销大的耦合多自由度优化，使实时平移 MPC 成为可能。
  - 平移控制器采用自适应模型融合预测控制，融合恒速（constant-velocity）与零速（zero-velocity）两种目标模型，以适应不同目标运动模式。
  - 依据历史预测误差更新模型权重。
  - 在满足执行机构、跟随距离和视场（field-of-view）约束的条件下计算平移控制指令。
- 验证方式：通过仿真和真实世界实验验证框架有效性，并声称性能优于已有框架。

### 主要贡献
- 提出面向 AUV 的立体视觉伺服跟踪框架。
- 感知上提出目标特定的深度提取方法，结合颜色/视差/时间线索构造目标深度掩码，并对深度与图像中心分别滤波，以缓解水下深度测量不可靠问题。
- 控制上通过偏航与平移解耦，避免昂贵的耦合多自由度优化，实现实时平移 MPC。
- 提出自适应模型融合预测控制，以恒速与零速目标模型的加权融合适应未知目标运动，并由历史预测误差在线更新权重。
- 在控制中显式考虑执行机构、跟随距离与视场约束。
- 通过仿真与真实实验验证，并报告相较现有框架更优的表现。

### 局限性
摘要未提供足够信息。摘要中未给出实验平台细节、数据集或场景规模、对比方法的具体名称与指标数值、失败案例、计算资源与实时性量化结果，也未说明该方法在何种条件下会失效或适用边界。

### 阅读优先级
中。理由：该论文聚焦水下视觉目标跟踪中“深度不可靠 + 目标运动未知”的实际问题，将目标特定深度提取与自适应模型融合 MPC 结合，问题设定清晰、模块划分明确，对水下机器人感知与控制交叉方向有参考价值；但摘要层面未提供量化结果与实验细节，是否值得精读需进一步阅读正文确认其方法新颖度与验证充分性。

</details>

<details>
<summary>Abstract</summary>

Vision-based underwater target tracking is challenged by unreliable depth measurements and unknown target motion. This paper proposes a stereo visual-servoing framework for an autonomous underwater vehicle (AUV). For perception, the framework derives a stable 3D relative state from stereo images through target-specific depth extraction and Kalman filtering. It constructs a target-depth mask from color, disparity, and temporal cues to select reliable target pixels, and then filters the resulting depth measurement and detected image center separately. For control, the framework decouples yaw regulation from translational control, avoiding computationally expensive coupled multi-DOF optimization and enabling real-time translational MPC. The translational controller employs adaptive model-fusion predictive control, combining constant-velocity and zero-velocity target models to accommodate different target-motion patterns. It updates the model weights using historical prediction errors and computes translational commands subject to actuation, following-distance, and field-of-view constraints. Through simulations and real-world experiments, we validate the effectiveness of the proposed framework and show it has better performance than existing frameworks.

</details>

#### 2026-09-17 - Semantic SLAM in Precision Agriculture using Bayesian Inference

**Authors:** Ruben Beumer, Sander Doodeman, René van de Molengraft, Duarte Antunes
**Links:** [abs](https://arxiv.org/abs/2609.20604) - [pdf](https://arxiv.org/pdf/2609.20604)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Semantic SLAM in Precision Agriculture using Bayesian Inference
- 作者：Ruben Beumer, Sander Doodeman, René van de Molengraft, Duarte Antunes
- 出版日期：2026-09-17T15:51:05Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.20604 ；PDF https://arxiv.org/pdf/2609.20604

### 一句话总结
该论文提出一个面向精准农业自主机器人的实时语义世界建模框架，将基于贝叶斯推断的物体及其语义属性概率建图与基于 g²o 的图优化 SLAM 结合，并在仿真与室内人工植物场地实验中用 Spot 机器人验证了实时建图能力。

### 研究问题
如何在精准农业场景中，使自主机器人在不完全依赖 GPS 的情况下，实现准确的建图与定位，同时利用植物类型、大小、健康等语义信息边执行任务边完成自身定位与建图。

### 核心思路/方法
- 构建实时语义世界建模框架，面向精准农业自主机器人。
- 对物体及其语义属性进行概率建图，并通过贝叶斯推断进行更新。
- 与基于图优化的 SLAM 方法结合，具体采用 g²o 这一通用图优化框架实现。
- 该集成使系统在准确建图与定位的同时，不必完全依赖 GPS。
- 利用植物类型、大小、健康等语义信息，支持机器人在作物田中边执行任务边建图与定位。
- 通过 Gazebo 仿真和室内人工植物场地物理实验验证，使用 Boston Dynamics 的机器狗 Spot。
- 训练 YOLOv8n 目标检测模型，从深度相机观测中提取物体和语义数据。

### 主要贡献
- 提出面向精准农业的实时语义世界建模框架，融合概率语义建图与图优化 SLAM。
- 将贝叶斯推断用于物体及其语义属性的更新，并集成 g²o 图优化实现 SLAM。
- 通过仿真与物理实验验证系统可成功实时建图至少 400 株植物。
- 使用 YOLOv8n 从深度相机观测中提取物体与语义数据，支撑语义 SLAM 流程。

### 局限性
- 摘要未提供足够信息说明该方法在真实农田、不同光照与天气条件下的表现。
- 摘要未提供足够信息说明其定位精度、建图精度、实时性指标或与基线方法的定量对比。
- 摘要未提供足够信息说明贝叶斯推断的具体模型形式、计算开销或失败案例。
- 摘要未提供足够信息说明 400 株植物上限之外的可扩展性。
- 摘要未提供足够信息说明 YOLOv8n 检测误差对 SLAM 与语义建图的影响。

### 阅读优先级
中。理由：该论文主题位于语义 SLAM、机器人与精准农业的交叉点，方法组合（贝叶斯推断 + g²o 图优化 + YOLOv8n）和实验平台（Spot、Gazebo、室内人工植物场地）对相关方向有参考价值；但摘要未给出定量结果、精度指标与真实农田验证细节，若需评估实际性能或复现实验，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

This paper presents a real-time semantic world modeling framework specialized for precision agriculture using autonomous robots. The framework combines probabilistic mapping of objects and their semantic attributes, updated through Bayesian inference, with a graph-based Simultaneous Localization and Mapping (SLAM) approach implemented using $g^2o$, a general framework for graph optimization. This integration enables accurate mapping and localization without relying solely on GPS. By leveraging semantic information such as plant type, size, and health, the robot can perform tasks while mapping and localizing itself within a field of crops. The proposed framework was validated through Gazebo simulations and physical experiments on an indoor field with artificial plants using Boston Dynamics' robot dog Spot. A YOLOv8n object detection model was trained to extract object and semantic data from depth camera observations. These simulations and experiments demonstrate that the system can successfully perform real-time mapping of up to at least 400 plants.

</details>

#### 2026-09-17 - RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

**Authors:** Marina Orozco González, Luis Merino
**Links:** [abs](https://arxiv.org/abs/2609.20589) - [pdf](https://arxiv.org/pdf/2609.20589)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, SLAM, visual SLAM, Gaussian Splatting, rendering, radiance, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RawSLAM: Online HDR Gaussian SLAM from Linear Radiance
- 作者：Marina Orozco González, Luis Merino
- 出版日期：2026-09-17T15:41:32Z
- 分类：3D Reconstruction & Multi-view Geometry（主）；Neural Scene Representations & Rendering（次）
- 链接：[摘要页](https://arxiv.org/abs/2609.20589) / [PDF](https://arxiv.org/pdf/2609.20589)

### 一句话总结
论文提出 RawSLAM，据摘要称是首个直接在单次曝光 16 位线性 HDR 图像上进行跟踪与建图的在线高斯 SLAM 框架。

### 研究问题
现有稠密视觉 SLAM 系统几乎只依赖 8 位色调映射后的 LDR 输入，在极端光照下阴影与高光会导致跟踪漂移和建图崩溃；而已有的 raw/HDR 重建流程严格离线，依赖 Structure-from-Motion 预处理，不适用于大帧间运动。

### 核心思路/方法
方法由三个核心组件构成：
1. 架构无关的 HDR 高斯泼溅模块，采用无 MLP 的对数参数化高斯颜色特征；
2. Reinhard 范围压缩的光度目标函数；
3. 结构引导的空间梯度加权。
三者结合使该方法在轨迹与重建精度上优于对 MonoGS 的直接 HDR 适配，并能以线性场景辐射度原生渲染以供后渲染处理。同一形式无需修改即可运行于标准 8 位输入。

### 主要贡献
- 据摘要称，提出首个在线高斯 SLAM 框架，直接在单次曝光 16 位线性 HDR 图像上跟踪与建图。
- 提出三个核心组件：架构无关 HDR 高斯泼溅模块（无 MLP 对数颜色参数化）、Reinhard 范围压缩光度目标、结构引导空间梯度加权。
- 在轨迹与重建精度上优于对 MonoGS 的直接 HDR 适配，并在标准 8 位输入上约为 MonoGS 基线误差的一半。
- HDR 高斯模块可无缝迁移至 SplaTAM、Gaussian SLAM 和 DROID-W，消除这些系统在挑战性光照序列上的全部跟踪失败。
- 引入 RawSLAM 数据集：10 个真实室内序列，含 16 位 RAW 图像、对齐深度、IMU 测量与外部 OptiTrack 位姿。代码与数据集将公开。

### 局限性
- 摘要未提供足够信息说明方法的计算开销、实时性能指标或帧率。
- 摘要未提供足够信息说明数据集规模之外的多样性、场景类型或与其他数据集的跨域泛化表现。
- 摘要未提供足够信息说明在 8 位输入上误差减半的具体实验设定与对比细节。
- 摘要未提供足够信息说明结构引导空间梯度加权的具体实现细节与消融结果。
- 摘要未提供足够信息说明代码与数据集的具体公开时间。

### 阅读优先级
高。理由：该工作针对极端光照下 SLAM 鲁棒性这一明确痛点，提出在线 HDR 高斯 SLAM，并声称在多个现有系统上消除跟踪失败，同时配套发布 16 位 RAW 室内数据集，对 3D 重建、神经渲染与 SLAM 交叉方向具有潜在参考价值。

</details>

<details>
<summary>Abstract</summary>

Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure-from-Motion preprocessing and are not suited for large inter-frame motion. We present, to the best of our knowledge, the first online Gaussian SLAM framework that tracks and maps directly on single-exposure 16-bit linear HDR imagery. Our method rests on three core components: an architecture-agnostic HDR Gaussian Splatting module featuring an MLP-free logarithmic parameterization of Gaussian color features; a Reinhard range-compressed photometric objective; and structure-guided spatial gradient weighting. Combined, these components allow our approach to outperform a direct HDR adaptation of MonoGS in both trajectory and reconstruction accuracy, while rendering natively in linear scene radiance for post-rendering processing. The same formulation runs unchanged on standard 8-bit inputs, roughly halving the MonoGS baseline error. Furthermore, our HDR Gaussian module transfers seamlessly to SplaTAM, Gaussian SLAM, and DROID-W, eliminating all tracking failures these systems suffer on challenging illumination sequences. To enable this research, we introduce RawSLAM: a dataset of 10 real-world indoor sequences featuring 16-bit RAW imagery, aligned depth, IMU measurements, and external OptiTrack poses. Code and dataset will be made publicly available soon.

</details>

#### 2026-09-17 - SLAMSqueezeBench: Comparing SLAM Systems under Resource Constraints

**Authors:** Mohamed Hefny, Karthik Dantu, Steven Y. Ko
**Links:** [abs](https://arxiv.org/abs/2609.19533) - [pdf](https://arxiv.org/pdf/2609.19533)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, Gaussian Splatting, splatting, manipulation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SLAMSqueezeBench: Comparing SLAM Systems under Resource Constraints
- 作者：Mohamed Hefny, Karthik Dantu, Steven Y. Ko
- 出版日期：2026-09-17T00:59:01Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.19533 ；PDF https://arxiv.org/pdf/2609.19533

### 一句话总结
论文提出 SLAMSqueezeBench，一个在边缘硬件上对 SLAM 系统施加计算与内存资源约束，并模拟有限缓冲下相机丢帧的测试框架，用于比较九种 SLAM 系统。

### 研究问题
SLAM 通常是自主机器人上运行的服务之一，用于辅助规划、操作等任务，这些任务都运行在边缘硬件上并受到严重资源约束。但大多数 SLAM 系统是在隔离环境中构建和测试的，其性能报告仿佛它是系统上唯一运行的任务。作者观察到，现有基准缺乏在真实资源约束下比较 SLAM 系统的通用机制。

### 核心思路/方法
作者开发了 SLAMSqueezeBench，该框架允许在边缘硬件的真实工作负载下测试 SLAM 系统。其做法是在执行期间对 SLAM 系统可用的计算和内存资源施加约束。它还模拟真实的相机帧采集过程，当有限缓冲区满时会发生丢帧。作者使用 SLAMSqueezeBench 比较了九种 SLAM 系统，涵盖经典系统、基于学习的系统以及用于高斯泼溅的方法。

### 主要贡献
- 指出并针对现有基准缺乏在真实资源约束下比较 SLAM 系统的通用机制这一问题。
- 提出 SLAMSqueezeBench 框架，可在边缘硬件上以真实工作负载测试 SLAM 系统。
- 该框架通过对执行期间的可用计算和内存资源施加约束，并模拟有限缓冲满时丢帧的真实相机帧采集。
- 使用该框架比较了九种 SLAM 系统，涵盖经典系统、基于学习系统和高斯泼溅方法。
- 作者表示该测试框架将在论文发表后供社区使用。

### 局限性
摘要未提供足够信息说明具体资源约束的设置、边缘硬件平台、九种系统的具体名称、评价指标、实验结论、框架开销或适用范围限制。摘要未提供足够信息说明该框架是否覆盖其他资源类型或更广泛机器人任务场景。

### 阅读优先级
中。理由：该工作针对 SLAM 评测中资源约束这一实际且常被忽视的问题，并提出可比较多类 SLAM 系统的框架，对边缘机器人、SLAM 评测和具身应用研究者有参考价值；但摘要未给出具体实验设置、指标和结论，是否具有强实证说服力需阅读全文后才能判断。

</details>

<details>
<summary>Abstract</summary>

Simultaneous localization and mapping (SLAM) is one of the services running on an autonomous robot. It is typically run to assist other tasks such as planning, manipulation, etc. All these tasks are run on edge hardware and are subject to severe resource constraints. However, most SLAM systems are built and tested in isolation, and their performance is reported as if they are the only task running on a system. We observe that existing benchmarks lack a common mechanism for comparing SLAM systems under realistic resource constraints. To address this limitation, we have developed SLAMSqueezeBench, a framework that allows testing of SLAM systems under realistic workloads on edge hardware. It does so by imposing constraints on compute and memory resources available for the SLAM system during execution. It also simulates realistic camera frame acquisition with frame drops when a finite buffer is full. Using SLAMSqueezeBench, we compare nine SLAM systems spanning classical systems, learning-based systems, and approaches for Gaussian splatting. Our testing framework will be available for use by the community upon publication.

</details>

#### 2026-09-17 - AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend

**Authors:** Hengyi Wang, Lourdes Agapito
**Links:** [abs](https://arxiv.org/abs/2609.19518) - [pdf](https://arxiv.org/pdf/2609.19518)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend
- 作者：Hengyi Wang, Lourdes Agapito
- 出版日期：2026-09-17T00:11:16Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供足够信息
- 链接：abstract_url: https://arxiv.org/abs/2609.19518；pdf_url: https://arxiv.org/pdf/2609.19518

### 一句话总结
AMB3R-SLAM 是一个可在单块消费级 GPU 上实时运行的单目 SLAM 系统，通过轻量前端与分层后端实现万帧级、公里级轨迹重建，并能自然处理动态场景，还可扩展至双目、RGB-D 与 LiDAR 输入。

### 研究问题
论文关注的是实时单目 SLAM 在超长序列、公里级轨迹和 10k 帧规模下的重建与跟踪问题，同时试图避免依赖静态世界假设的 bundle adjustment，从而处理复杂动态场景。

### 核心思路/方法
方法由轻量前端和分层后端组成：前端用于低延迟在线跟踪；后端按局部、中层和全局层级逐步施加一致性约束。该系统避免使用依赖静态世界假设的 bundle adjustment，因此可自然应对复杂动态场景。作者还说明该方法可扩展到利用双目、RGB-D 和 LiDAR 作为额外输入。

### 主要贡献
- 提出 AMB3R-SLAM，一个能在单块消费级 GPU 上实时运行、在 10k 帧上重建公里级轨迹的单目 SLAM 系统。
- 设计轻量前端与分层后端结合的结构，后端逐步强制局部、中层与全局一致性。
- 避免依赖静态世界假设的 bundle adjustment，使系统可直接处理复杂动态场景。
- 展示方法可扩展至双目、RGB-D 和 LiDAR 额外输入。
- 在 9 个数据集上取得较强的相机跟踪性能，并在 VBR 与 Oxford Spires 上将先前最先进方法的绝对轨迹误差降低超过 70%；加入 LiDAR 输入后，在 KITTI 与 VBR 上将 ATE 进一步降至亚米级。

### 局限性
摘要未提供足够信息。论文未在摘要中说明失败场景、计算资源具体配置、实时性指标细节、各数据集上的完整定量结果或方法对额外输入的依赖程度等局限。

### 阅读优先级
高。理由：该工作面向公里级、万帧规模的实时单目 SLAM，提出分层后端并规避静态世界假设，且在多个数据集上报告了显著 ATE 降低；主题属于 3D 重建与多视图几何中的核心问题，具有较强的方法与系统参考价值。

</details>

<details>
<summary>Abstract</summary>

We present AMB3R-SLAM, a real-time monocular SLAM system capable of reconstructing kilometer-scale trajectories over 10k frames on a single consumer-grade GPU. Our model couples a lightweight front-end for low-latency online tracking with a hierarchical backend that progressively enforces local, mid-level, and global consistency. By avoiding bundle adjustment that relies on the static world assumption, our system naturally handles complex dynamic scenes out of the box. Furthermore, we demonstrate that our method can be extended to leverage stereo, RGB-D, and LiDAR as additional inputs. AMB3R-SLAM achieves strong camera tracking performance across 9 datasets, reducing the absolute trajectory error (ATE) of previous state-of-the-art methods on VBR and Oxford Spires by over 70%. With additional LiDAR input, our model further reduces ATE to sub-meter level on KITTI and VBR datasets.

</details>

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

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-17 - SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos

**Authors:** Peiyu Liu, Dingxi Zhang, Federico Tombari, Marc Pollefeys, Christina Tsalicoglou, Daniel Barath
**Links:** [abs](https://arxiv.org/abs/2609.20818) - [pdf](https://arxiv.org/pdf/2609.20818)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic Gaussian, Gaussian Splatting, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos
- 作者：Peiyu Liu, Dingxi Zhang, Federico Tombari, Marc Pollefeys, Christina Tsalicoglou, Daniel Barath
- 出版日期：2026-09-17T17:59:41Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.20818

### 一句话总结
本文针对飞溅液体难以重建的问题，构建了真实多视角飞溅液体基准数据集，并提出 SplashSplat——一种“仅在观测可约束处施加物理结构”的表示方法，在真实与合成基准上优于现有动态高斯泼溅方法，且训练成本更低。

### 研究问题
飞溅液体存在时间极短：液片会撕裂成液丝与液滴，外观具有视角依赖性且几乎无纹理，且几乎没有能持久追踪的特征。因此，重建研究此前主要集中于烟雾、合成液体或缓慢形变的表面。据作者所述，目前尚不存在同步多视角的飞溅液体数据集，真实飞溅液体的重建缺乏数据与有效方法。

### 核心思路/方法
方法建立在单一原则之上：仅在观测能够约束的地方施加物理结构。具体包括：
- 由掩码融合得到的逐帧液体 SDF 提供几何；
- 在相邻 SDF 之间进行水平集传输，得到粗略速度场；
- 沿该流场推进拉格朗日载体（Lagrangian carriers），每个新观测对其进行修正，并在覆盖丢失处重新播种；
- 最终解码为局部高斯，用于可微渲染。

### 主要贡献
1. 提出据作者所知尚不存在的同步多视角飞溅液体基准：20 个真实场景，从连贯水流到剧烈飞溅，由七台同步标定的 4K 相机以 60 fps 采集，并提供人工精修的各视角液体与容器掩码以及固定评测划分。
2. 提出 SplashSplat 方法，基于上述“仅在可约束处施加物理结构”的原则，结合掩码融合 SDF、水平集传输、拉格朗日载体推进与局部高斯解码。
3. 在真实采集数据与合成基准上，SplashSplat 优于当前最先进的动态高斯泼溅方法，运动在物理上更合理且训练成本更低。同一表示还支持无需重新优化的时间插值与风格迁移。

### 局限性
摘要未提供足够信息。摘要中未说明方法的失败情形、适用边界、对掩码精度的依赖程度、计算与内存开销的具体限制，或基准数据集本身的覆盖不足等局限。

### 阅读优先级
高。理由：该工作同时贡献了此前缺失的真实飞溅液体多视角基准数据集与对应重建方法，问题设定（极短时、无纹理、视角依赖、难以追踪的液体）具有明显挑战性与新颖性，且声称在真实与合成基准上均优于现有动态高斯泼溅方法并降低训练成本，对动态场景重建、神经渲染与流体相关视觉研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

A splash lives for a fraction of a second: sheets tear into ligaments and droplets, appearance is view-dependent and nearly textureless, and little persists long enough to track. Reconstruction research has consequently focused on smoke, synthetic liquids, or gently deforming surfaces. To our knowledge, no synchronized multi-view dataset of splashing liquids exists. We therefore introduce a benchmark of 20 real scenes, from coherent streams to violent splashes, captured by seven synchronized, calibrated 4K cameras at 60 fps, with manually refined per-view liquid and container masks and fixed evaluation splits. We further present SplashSplat, built on a single principle: impose physical structure only where the observations can constrain it. Per-frame liquid SDFs fused from the masks provide the geometry, level-set transport between consecutive SDFs yields a coarse velocity field, and Lagrangian carriers advected along this flow, corrected against each new observation and reseeded where coverage is lost, decode local Gaussians for differentiable rendering. SplashSplat outperforms state-of-the-art dynamic Gaussian splatting methods on our real captures and on a synthetic benchmark, with physically more plausible motion and a lower training cost. The same representation supports temporal interpolation and style transfer without re-optimization.

</details>

#### 2026-09-17 - PhGS: Post-Hoc Pruning and Refinement of Single-View Feed-Forward 3D Gaussian Reconstructions

**Authors:** Rinto Yagawa, Han Cheng, Dieter Schmalstieg, Hideo Saito, Shohei Mori
**Links:** [abs](https://arxiv.org/abs/2609.20623) - [pdf](https://arxiv.org/pdf/2609.20623)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PhGS: Post-Hoc Pruning and Refinement of Single-View Feed-Forward 3D Gaussian Reconstructions
- 作者：Rinto Yagawa, Han Cheng, Dieter Schmalstieg, Hideo Saito, Shohei Mori
- 出版日期：2026-09-17T16:07:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.20623) / [PDF](https://arxiv.org/pdf/2609.20623)

### 一句话总结
针对单视图前馈 3DGS 生成中因每条相机射线预测固定数量高斯而导致的空间冗余，提出一种骨干无关的后处理压缩流程：冻结基模型，通过重要性分数剪枝与轻量循环精修模块迭代恢复图像质量。

### 研究问题
单视图前馈 3D Gaussian Splatting（3DGS）生成方法会在每条相机射线上预测固定数量的高斯，从而引入严重的空间冗余。现有的大多数压缩（compaction）策略面向多视图设置，依赖跨视图一致性，因而与单图像模型不兼容。论文要解决的核心问题是：在不重新训练基础前馈网络的前提下，如何压缩单视图前馈 3DGS 生成的冗余高斯表示。

### 核心思路/方法
论文的关键思路是保持基础模型冻结，对生成的高斯施加后处理剪枝与循环精修，而非重新训练前馈网络直接输出紧凑表示。具体地，提出一个骨干无关的压缩流程，包含两个耦合组件：
1. 基于重要性分数的剪枝机制；
2. 可训练的轻量循环精修模块，用于迭代更新存活下来的基元（primitives）以恢复图像质量。
此外，方法支持在推理时灵活设定保留比例（keep ratios）以适应不同应用需求。

### 主要贡献
- 提出骨干无关（backbone-agnostic）的单视图前馈 3DGS 压缩流程。
- 将基于重要性分数的剪枝与可训练轻量循环精修模块相结合，在压缩后迭代恢复图像质量。
- 无需重新训练基础前馈网络，可无缝集成现有基线方法。
- 在保持新视图渲染保真度的同时实现较高的内存缩减。
- 支持推理时灵活的保留比例设置。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集、基线对比对象及定量指标。
- 摘要未提供足够信息说明重要性分数的具体定义与剪枝细节。
- 摘要未提供足够信息说明精修模块的架构、训练代价与推理开销。
- 摘要未提供足够信息说明保留比例的可调范围及其对质量与内存的定量影响。
- 摘要未提供足够信息说明方法在何种失败情形或边界条件下表现受限。

### 阅读优先级
中。理由：该工作面向单视图前馈 3DGS 的冗余压缩这一具体且实际的问题，提出冻结基模型 + 后处理剪枝与精修的思路，具备与现有基线解耦、推理时可调保留比例等实用特性；但摘要未给出定量结果与实验细节，是否在保真度与压缩率上具有显著优势尚无法从摘要判断，因此对关注 3DGS 压缩与单视图重建方向的读者具有中等参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent single-view feed-forward 3D Gaussian Splatting (3DGS) generation predicts a fixed number of Gaussians per camera ray, introducing severe spatial redundancy. Most existing compaction strategies target multi-view setups to exploit cross-view consistency and are incompatible with single-image models. Instead of retraining the base feed-forward network to directly output compact representations, our insight is to keep the base models frozen and apply post-hoc pruning and recurrent refinement to the generated Gaussians. Consequently, we propose a backbone-agnostic compaction pipeline for single-view feed-forward 3DGS that couples an importance-score-based pruning mechanism with a trainable, lightweight recurrent refinement module, which iteratively updates the surviving primitives to restore image quality. Our results demonstrate seamless integration with existing baselines while preserving novel-view rendering fidelity and achieving high memory reduction. Furthermore, our method supports flexible inference-time keep ratios for application needs.

</details>

#### 2026-09-17 - CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding

**Authors:** Zhikun Zhou, Kunyu Peng, Runyi Yang, Junhao Cai, Di Wen, Ruiping Liu, Danda Pani Paudel, Yi Zhou, Luc Van Gool, Kailun Yang
**Links:** [abs](https://arxiv.org/abs/2609.20586) - [pdf](https://arxiv.org/pdf/2609.20586)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding
- 作者：Zhikun Zhou, Kunyu Peng, Runyi Yang, Junhao Cai, Di Wen, Ruiping Liu, Danda Pani Paudel, Yi Zhou, Luc Van Gool, Kailun Yang
- 出版日期：2026-09-17T15:39:25Z
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（次）
- 链接：[摘要](https://arxiv.org/abs/2609.20586) / [PDF](https://arxiv.org/pdf/2609.20586)

### 一句话总结
CoRef-GS 面向多机器人协同场景，提出在独立重建并融合后的高斯地图上完成"指代式"语义定位与视角关系推理的框架，并配套发布双四足机器人基准 CoQuad-Ref。

### 研究问题
具身机器人的指代式场景理解需要从指定视角对以物体为中心和以关系为中心的语言查询进行定位。单个智能体的局部语义高斯地图可以支持这种定位，但在协同场景下，地图由各智能体独立重建后再对齐融合，此时被指代的目标或作为上下文参照的地标可能来自其他智能体的观测，而空间关系仍需从发起查询的机器人视角来解释。论文将该问题形式化为"融合地图上的协同指代高斯定位"，并指出其需要满足三个条件：几何可对齐性、实例级语义可比性、以及视角条件化的关系推理。现有语言感知高斯方法多聚焦单地图查询，而高斯配准方法仅优化几何或光度对齐，不保留面向语言定位的语义兼容性。

### 核心思路/方法
CoRef-GS 包含三个环节：首先构建局部开放词汇、实例感知的高斯地图；随后通过跨智能体对齐模块，以几何与语义一致性对部分重叠的地图进行对齐；最后使用视角条件化的掩码关系图（view-conditioned mask relation graph）完成查询定位。论文同时提出 CoQuad-Ref，一个覆盖真实世界与仿真室内场景的双四足机器人基准。

### 主要贡献
- 提出协同指代高斯定位问题设定：在独立重建并对齐融合的地图上，处理可能跨智能体来源的目标与地标，同时保持查询机器人的视角关系解释。
- 提出 CoRef-GS 框架，包含开放词汇实例感知局部高斯地图构建、几何与语义一致性驱动的跨智能体对齐模块，以及视角条件化掩码关系图的查询定位。
- 提出 CoQuad-Ref 双四足机器人基准，覆盖真实与仿真室内场景。
- 实验报告：仿真场景中旋转误差从粗初始化后的 2.58° 降至细化后的 0.15°；真实世界指代 mIoU 相比 ReferSplat 从 52.6% 提升至 68.8%。
- 承诺公开基准与源代码（https://github.com/ruojiruoli17/CoRef-GS.git）。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败情形、对重叠程度的敏感性、计算开销、智能体数量上限，也未给出仿真场景指代精度等其他指标，亦未说明基准的规模与数据构成细节。

### 阅读优先级
高。理由：该工作同时涉及多智能体协同、语言指代定位与高斯泼溅交叉方向，提出新问题设定、新方法、新基准并给出量化改进；但判断是否与自身研究直接相关，仍需摘要未提供的实验设置与数据细节。

</details>

<details>
<summary>Abstract</summary>

Referring scene understanding for embodied robots requires grounding object- and relation-centric language queries from a designated viewpoint. While a local semantic Gaussian map can support such grounding within one agent's observations, cooperative settings require this ability to remain effective after independently reconstructed maps are aligned and fused. In this setting, the referred target or its contextual landmark may come from another agent's observations, while spatial relations must still be interpreted from the querying robot's viewpoint. We formulate this problem as cooperative referring Gaussian grounding over fused maps, which requires geometric alignability, instance-level semantic comparability, and view-conditioned relation reasoning. Existing language-aware Gaussian methods mainly focus on single-map querying, whereas Gaussian registration methods optimize geometric or photometric alignment without preserving language-grounding-oriented semantic compatibility. We propose CoRef-GS, a cooperative referring Gaussian splatting framework. CoRef-GS constructs local open-vocabulary instance-aware Gaussian maps, then aligns partially overlapping maps with a cross-agent alignment module by geometric and semantic consistency, and grounds queries using a view-conditioned mask relation graph. We further introduce CoQuad-Ref, a dual-quadruped benchmark spanning both real-world and simulated indoor scenes. Experiments show that, on simulated scenes, CoRef-GS reduces the rotation error from 2.58° after coarse initialization to 0.15° after refinement, and improves real-world referring mIoU over ReferSplat from 52.6% to 68.8%. The established benchmark and source code will be publicly released at https://github.com/ruojiruoli17/CoRef-GS.git.

</details>

#### 2026-09-17 - EliGSiR: Continual RGB-D Mapping with Gaussian Splatting under Bounded Compute

**Authors:** Björn Ellensohn, Elmar Rueckert, Christian Rauch
**Links:** [abs](https://arxiv.org/abs/2609.20348) - [pdf](https://arxiv.org/pdf/2609.20348)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EliGSiR: Continual RGB-D Mapping with Gaussian Splatting under Bounded Compute
- 作者：Björn Ellensohn, Elmar Rueckert, Christian Rauch
- 出版日期：2026-09-17T13:12:49Z
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：[摘要](https://arxiv.org/abs/2609.20348) / [PDF](https://arxiv.org/pdf/2609.20348)

### 一句话总结
EliGSiR 是一个面向在线 RGB-D 连续建图的持续高斯泼溅映射器，通过视图调度、自适应监督分辨率和定向几何增长，在有限算力预算下持续更新并保留已重建区域。

### 研究问题
传统 3D Gaussian Splatting 假设观测集合封闭且优化流程较长；而连续 RGB-D 建图要求新观测在线到达，同时必须保留此前已重建的区域，因此需要解决如何在计算预算受限且地图持续演化的条件下分配优化资源的问题。

### 核心思路/方法
论文提出 EliGSiR（Evidence-guided Load-adaptive Incremental Gaussian Splatting with Image Replay），一种持续高斯映射器，控制随重建演化而变化的优化预算使用方式，包含三个机制：
- Map-Guided View Scheduling：过滤冗余的 incoming views，并根据地图当前状态重新考虑保留的视图；
- Load-Adaptive Fidelity：根据当前建图负载调整监督分辨率，而非遵循固定分辨率计划；
- Targeted Geometry Growth：将深度监督与高斯创建分离，仅在重复 RGB-D 观测表明结构缺失或错位处增加几何容量。
这些机制在建图活跃期间共同自适应决定优化哪些视图、使用多少图像细节以及在哪里扩展表示。

### 主要贡献
- 提出 EliGSiR 持续高斯映射框架，面向在线到达观测与已重建区域保留的需求，在有限算力预算下自适应使用优化资源。
- 设计 Map-Guided View Scheduling、Load-Adaptive Fidelity 与 Targeted Geometry Growth 三项机制，分别控制视图优化选择、监督细节程度和几何容量增长位置。
- 在 Replica、TUM RGB-D、ScanNet++ 以及真实 RGB-D 传感器序列上进行评估，同时考虑最终重建结果与采集过程中的地图状态。
- 在 TUM RGB-D fr3/long_office_household 上，使用与受控基线相同的地面真值建图位姿时达到 21.52 dB，而 SplaTAM 为 19.42 dB；在跟踪位姿比较中，使用实时 ORB-SLAM3 位姿的 EliGSiR 在 155.5 s 内达到 23.02 dB，而 CaRtGS 使用其原生跟踪器在 230.9 s 内为 20.10 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对连续 RGB-D 建图中的在线观测、有限算力与地图保留问题，提出可操作的自适应优化机制，并在多个数据集与真实传感器序列上给出定量对比，对神经场景表示与机器人/AR 应用方向均有参考价值。

</details>

<details>
<summary>Abstract</summary>

Conventional 3D Gaussian Splatting assumes a closed set of observations and long optimization schedules. Continual RGB-D mapping in contrast poses the problem that new observations arrive online, while previously reconstructed regions must be preserved. We present EliGSiR (Evidence-guided Load-adaptive Incremental Gaussian Splatting with Image Replay), a continual Gaussian mapper that controls how the available optimization budget is used as the reconstruction evolves. Map-Guided View Scheduling filters redundant incoming views and reconsiders retained views according to the current state of the map. Load-Adaptive Fidelity adjusts supervision resolution to the current mapping load instead of following a fixed resolution schedule. Targeted Geometry Growth separates depth supervision from Gaussian creation and adds geometric capacity only where repeated RGB-D observations indicate missing or misplaced structure. Together, these mechanisms adapt which views are optimized, how much image detail is used, and where the representation grows while mapping remains active. We evaluate EliGSiR on Replica, TUM RGB-D, ScanNet++, and real RGB-D sensor sequences, considering both the final reconstruction and the map available throughout acquisition. On TUM RGB-D fr3/long_office_household, EliGSiR reaches 21.52 dB with the same ground-truth mapping poses used by the controlled baselines, compared with 19.42 dB for SplaTAM. In the tracked-pose comparison, EliGSiR with live ORB-SLAM3 poses reaches 23.02 dB in 155.5 s, compared with 20.10 dB in 230.9 s for CaRtGS using its native tracker. We further evaluate reconstruction throughout acquisition and show how EliGSiR adaptive view scheduling, supervision fidelity, and geometry growth improve the use of the available mapping budget.

</details>

#### 2026-09-17 - GS-PI: An Optimization-Decoupled Appearance Decomposition Approach for Generating PBR Gaussian Assets

**Authors:** Jieting Xu, Rengan Xie, Zijian Huang, Zehui Jin, Rui Wang, Yuchi Huo
**Links:** [abs](https://arxiv.org/abs/2609.19907) - [pdf](https://arxiv.org/pdf/2609.19907)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, inverse rendering, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-PI: An Optimization-Decoupled Appearance Decomposition Approach for Generating PBR Gaussian Assets
- 作者：Jieting Xu, Rengan Xie, Zijian Huang, Zehui Jin, Rui Wang, Yuchi Huo
- 出版日期：2026-09-17T08:51:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.19907) / [PDF](https://arxiv.org/pdf/2609.19907)

### 一句话总结
GS-PI 提出一种优化解耦的框架，将 PBR 材质生成建模为 3D 点云上以几何为条件的扩散过程，从而把 Gaussian Splatting 模型转换为可重新光照的 PBR-GS 资产。

### 研究问题
Gaussian Splatting 在新视角合成上表现优异，但其编码的是“烘焙”后的辐射度，光照与几何紧密耦合，难以无缝接入基于物理的渲染（PBR）管线。现有逆渲染方法尝试通过联合优化解耦材质，但常因目标相互竞争而出现严重歧义与残留光照伪影。

### 核心思路/方法
论文将 PBR 材质生成重新表述为 3D 点云上以几何为条件的扩散过程，直接在 3D 域中操作，从而天然保证多视角一致性，规避 2D 扩散方法面临的像素对应问题。方法引入多尺度跨视角条件机制，整合三类互补信息：全局语义先验、以源视角为锚定的光度线索、以及绝对空间学习视角方向条件信号。整体流程为：从预训练 Gaussian 模型中提取点云，通过条件扩散预测 PBR 属性，再经由可微光栅化蒸馏回 Gaussian 表示，最终得到完全可重新光照的 PBR-GS 资产。

### 主要贡献
- 提出优化解耦框架 GS-PI，将 PBR 材质生成建模为几何条件下的 3D 点云扩散过程，避免联合优化中的目标竞争与歧义。
- 直接在 3D 域操作，保证多视角一致性，规避 2D 扩散方法的像素对应难题。
- 设计多尺度跨视角条件机制，融合全局语义先验、源锚定光度线索与绝对空间学习视角方向信号，压缩复杂多视角证据，缓解跨视角投影错位，并防止镜面高光被烘焙进本征颜色。
- 以“学习式扩散 + 短程目标驱动蒸馏”替代逐场景的联合光照/BRDF 优化，且无需代理网格。
- 摘要声称其性能优于近期逆渲染基线。

### 局限性
摘要未提供足够信息。论文摘要未给出具体实验设置、失败案例、计算开销、数据依赖或泛化边界等细节，因此无法基于所给材料判断其局限。

### 阅读优先级
中。理由：该工作针对 Gaussian Splatting 与 PBR 管线衔接的关键痛点，提出优化解耦与 3D 扩散相结合的思路，对神经渲染与逆渲染方向有参考价值；但摘要未提供实验细节与定量结果，且发布时间较新，需阅读全文才能评估其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting (GS) excels at novel-view synthesis but encodes baked-in radiance, tightly entangling illumination with geometry and preventing seamless integration into physically based rendering (PBR) pipelines. Existing inverse-rendering methods attempt to disentangle materials via joint optimization, but often suffer from competing objectives that cause severe ambiguities and residual lighting artifacts. To overcome this, we present GS-PI, a novel optimization-decoupled framework that casts PBR material generation as a geometry-conditioned diffusion process on 3D point clouds. By operating directly in the 3D domain, our method inherently guarantees multi-view consistency, sidestepping the severe pixel correspondence issues that challenge 2D diffusion approaches. We introduce a multi-scale cross-view conditioning mechanism that integrates three complementary components: a global semantic prior, source-anchored photometric cues, and an absolute spatial learned view-direction conditioning signal. This design efficiently compresses complex multi-view evidence, mitigating cross-view projection misalignment and successfully preventing specular highlights from baking into intrinsic colors. By extracting a point cloud from a pre-trained Gaussian model, predicting PBR attributes via conditional diffusion, and distilling them back through differentiable rasterisation, we yield a fully relightable PBR-GS asset. GS-PI outperforms recent inverse-rendering baselines while replacing per-scene joint illumination/BRDF optimization with a learned diffusion pass followed by a short target-driven distillation, without requiring proxy meshes.

</details>

#### 2026-09-17 - Printing the Underdetermined: Materializing Multi-solutionness in Figurative Paintings

**Authors:** Yutao Ming, Teng Xu, Youjia Wang, Yunyang Liu, Fengmin Yang, Fuqiang Zhao, Jingyi Yu, Hua Yang, Yanjun Zhou
**Links:** [abs](https://arxiv.org/abs/2609.19782) - [pdf](https://arxiv.org/pdf/2609.19782)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Printing the Underdetermined: Materializing Multi-solutionness in Figurative Paintings
- 作者：Yutao Ming, Teng Xu, Youjia Wang, Yunyang Liu, Fengmin Yang, Fuqiang Zhao, Jingyi Yu, Hua Yang, Yanjun Zhou
- 出版日期：2026-09-17T06:50:54Z
- 分类：Neural Scene Representations & Rendering（Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2609.19782 ；PDF：https://arxiv.org/pdf/2609.19782

### 一句话总结
论文针对具象绘画被当作单一可恢复三维场景这一常规假设，提出将“多解性”（与单幅绘画相容的多种三维配置）显式保留、重建并通过 DreamPrinting 实体化的工作流程。

### 研究问题
常规做法把具象绘画视为描绘了一个单一可恢复的三维场景：观看者推断深度与遮挡，重建流程试图收敛到一个稳定模型。论文要处理的核心问题是这种“唯一解”假设忽略了多解性。摘要指出多解性来自两方面：
- 未观测内容：背面和被遮挡体积允许多种合理补全；
- 已观测线索：透视、明暗和遮挡仍然对几何约束不足。
当使用视频生成模型在无显式三维约束下合成额外视角时，帧级的小漂移是不可避免的，而非例外。

### 核心思路/方法
- 从一幅绘画中采样多个相机环绕的多视角视频序列。
- 对每个序列用 3D Gaussian Splatting 重建为基于点的 Gaussian 场景表示。
- 在该表示中，密度光晕（density halos）与鬼影（ghosting）被用来暴露未解决的自由度。
- 使用 DreamPrinting 将这些表示制作成物理实体。
- 整体上把多种相容解释作为显式输出，而不是当作残差误差来处理。

### 主要贡献
- 提出并突出“多解性”（multi-solutionness）概念，即与单幅绘画相容的三维配置的非唯一性，并将其保持为可见、可物质化的对象。
- 提出一条工作流程：单幅绘画 → 多个相机环绕多视角视频序列 → 3D Gaussian Splatting → 显式暴露未解自由度的 Gaussian 场景表示 → DreamPrinting 实体化。
- 将多种相容解释视为显式输出而非误差，为具象绘画的空间解读提供一个可在数字与物理形式中检视、比较和讨论的计算框架。

### 局限性
摘要未提供足够信息。摘要中未给出定量实验结果、用户研究、方法失败案例、计算成本、生成视频数量或实体化的具体精度限制等细节。

### 阅读优先级
中。理由：论文提出了一个较有新意的视角（把多解性作为显式输出并实体化），涉及视频生成、3D Gaussian Splatting 与 DreamPrinting 的组合流程，对神经场景表示与渲染、计算艺术/绘画空间解读交叉方向有参考价值；但摘要未提供实验验证细节与定量结论，实际价值需进一步阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

Figurative paintings are often approached as if they depict a single recoverable 3D scene: viewers infer depth and occlusion, and reconstruction pipelines attempt to converge to one stable model. We instead foreground multi-solutionness, the non-uniqueness of 3D configurations compatible with a single painted image, and propose a workflow that keeps this non-uniqueness visible and material. Multi-solutionness arises from two sources: unobserved content, where backsides and occluded volumes admit multiple plausible completions, and observed cues, where perspective, shading, and occlusion still underconstrain geometry. When additional views are synthesized by a video generative model without explicit 3D constraints, small frame-level drifts become inevitable rather than exceptional. Our pipeline samples multiple camera-orbit multi-view video sequences from one painting, reconstructs each sequence with 3D Gaussian Splatting into a point-based Gaussian scene representation where density halos and ghosting expose unresolved degrees of freedom, and fabricates these representations as physical artifacts using DreamPrinting. By treating multiple compatible interpretations as explicit outputs rather than residual error, we provide a computational framework for spatial readings of figurative painting that can be inspected, compared, and discussed in both digital and physical form.

</details>

#### 2026-09-17 - GAPrompt++: Multi-Granular Geometry-Aware Point Cloud Prompt for 3D Vision Model

**Authors:** Zixiang Ai, Zhenyu Cui, Yufei Guo, Wenwen Qiang, Lei Chen, Jiwen Lu, Jiahuan Zhou
**Links:** [abs](https://arxiv.org/abs/2609.19716) - [pdf](https://arxiv.org/pdf/2609.19716)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view stereo, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GAPrompt++: Multi-Granular Geometry-Aware Point Cloud Prompt for 3D Vision Model
- 作者：Zixiang Ai, Zhenyu Cui, Yufei Guo, Wenwen Qiang, Lei Chen, Jiwen Lu, Jiahuan Zhou
- 出版日期：2026-09-17T05:14:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.19716) | [PDF](https://arxiv.org/pdf/2609.19716)

### 一句话总结
GAPrompt++ 提出一种多粒度、几何感知的点云提示（prompting）方法，用于以极低可训练参数代价将预训练 3D 视觉模型高效适配到下游任务，并构建了两个更具挑战性的点云评测基准。

### 研究问题
预训练 3D 视觉模型虽推动了点云分析的发展，但通过全量微调适配下游任务在计算和存储上代价高昂。参数高效微调（PEFT）是潜在的替代方案，然而现有基于提示（prompting）的方法忽略了点云内在的几何结构，具体表现为：既无法同时编码细粒度几何线索与粗粒度结构语义，也无法在模型层级中有效传播这些信息，从而限制了适配能力。

### 核心思路/方法
针对上述问题，论文提出 GAPrompt++，一种多粒度几何感知的提示方法，为高效的 3D 任务适配提供更丰富的几何引导，由三个组件构成：
1. **Point Shift Prompter（点偏移提示器）**：在不同尺度上提取多粒度几何特征，从而在适配过程中实现实例特定的几何调整。
2. **Keypoint Prompter（关键点提示器）**：自适应地生成点级别的提示，以突出局部几何显著性和细粒度结构细节。
3. **Prompt Propagation（提示传播）机制**：将上述多粒度几何线索注入整个特征提取层级，增强捕获关键几何特征的能力。

### 主要贡献
- 提出 GAPrompt++，一种多粒度几何感知的提示方法，为高效 3D 任务适配提供更丰富的几何引导。
- 设计 Point Shift Prompter、Keypoint Prompter 与 Prompt Propagation 三个组件，分别处理多尺度几何调整、点级局部显著性提示与层级信息传播。
- 实验表明，GAPrompt++ 在基于提示的 PEFT 方法中达到 state-of-the-art，并在多个基准上超越全量微调，同时可训练参数少于 2%。
- 针对现有评测数据集趋于饱和的问题，构建了两个分别源自 3D Gaussian Splatting 与 Multi-View Stereo 重建的更具挑战性基准，以提供多样且真实的点云场景，推动未来研究。

### 局限性
- 具体实验设置、数据集名称、对比方法与数值结果：摘要未提供足够信息。
- 两个新基准的规模、标注方式与评价协议：摘要未提供足够信息。
- 方法在具体下游任务（如分类、分割、检测等）上的适用范围：摘要未提供足够信息。
- 少于 2% 可训练参数的具体计算口径与模型规模：摘要未提供足够信息。

### 阅读优先级
高。理由：该工作聚焦 3D 视觉模型的高效适配这一实际问题，同时给出方法（多粒度几何感知提示）与评测资源（两个新基准）两方面贡献；且摘要声称在多个基准上超越全量微调且可训练参数少于 2%，属于值得优先验证的结论性主张。

</details>

<details>
<summary>Abstract</summary>

Pre-trained 3D vision models have substantially advanced point cloud analysis, yet adapting them to downstream tasks via full fine-tuning is computationally expensive and storage-intensive. Parameter-Efficient Fine-Tuning (PEFT) offers a promising alternative by reducing both adaptation cost and storage burden. However, existing prompting-based approaches ignore the intrinsic geometric structures of point clouds, thereby limiting their adaptation capability. This limitation stems from their inability to encode both fine-grained geometric cues and coarse-grained structural semantics, as well as failing to propagate such information effectively through the model hierarchy. To address these challenges, we propose GAPrompt++, a multi-granular geometry-aware prompting method that provides richer geometric guidance for efficient 3D task adaptation. Specifically, we introduce a Point Shift Prompter that extracts multi-granular geometric features across different scales, enabling instance-specific geometric adjustments during adaptation. Next, a Keypoint Prompter adaptively generates point-level prompts to highlight local geometric saliency and fine-grained structural details. Furthermore, a Prompt Propagation mechanism injects these multi-granular geometric cues throughout the feature extraction hierarchy, strengthening the ability to capture essential geometric characteristics. Extensive experiments show that GAPrompt++ achieves state-of-the-art performance among prompting-based PEFT methods and even surpasses full fine-tuning across diverse benchmarks, while requiring less than 2\% trainable parameters. In addition, to address the saturation of existing evaluation datasets, we construct two more challenging benchmarks derived from 3D Gaussian Splatting and Multi-View Stereo reconstruction, offering diverse and realistic point cloud scenarios to promote future research.

</details>

#### 2026-09-16 - ParticleSplat: Self-supervised Object-centric Latent Particle Splatting

**Authors:** Lyuxing He, Daniel Guo, Elizabeth Terveen, Deepak Pathak, David Held, Tal Daniel
**Links:** [abs](https://arxiv.org/abs/2609.19463) - [pdf](https://arxiv.org/pdf/2609.19463)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** geometric reasoning, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ParticleSplat: Self-supervised Object-centric Latent Particle Splatting
- 作者：Lyuxing He, Daniel Guo, Elizabeth Terveen, Deepak Pathak, David Held, Tal Daniel
- 出版日期：2026-09-16T22:05:05Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.19463) | [PDF](https://arxiv.org/pdf/2609.19463)

### 一句话总结
ParticleSplat 将 Deep Latent Particles 的 2D 潜在粒子扩展到 3D 潜在粒子空间，借助前馈 3D 高斯泼溅与视图合成目标，实现自监督的以物体为中心的场景分解。

### 研究问题
DLP 框架虽能以粒子（含位置、尺度、视觉外观等属性）表示图像，但其本质是 2D 的，无法进行显式的 3D 空间与几何推理，而这对于机器人操作等下游任务至关重要。论文旨在解决这一 2D 局限。

### 核心思路/方法
- 利用潜在粒子与 3D 高斯基元之间的结构相似性，构建 3D 潜在粒子空间，并以新颖视图合成目标进行训练。
- 模型将带相机位姿的多视图联合编码到一个共享的 3D 以物体为中心的潜在空间中。
- 随后把粒子转换为与粒子对齐的 3D 高斯，通过其组合重建完整场景。
- 训练方式为自监督。

### 主要贡献
- 提出 ParticleSplat，一种基于前馈 3D 高斯泼溅的自监督、以物体为中心的学习方法，把场景分解为表示语义实体的潜在“粒子”集合。
- 将 DLP 的 2D 粒子表示扩展为 3D 潜在粒子空间，并引入新颖视图合成目标进行训练，使模型具备显式 3D 空间与几何推理能力。
- 在模拟与真实世界数据集上表明，该形式能无监督地学到物体掩码。
- 支持可控的 3D 场景编辑，例如通过在潜在空间中修改粒子来移动物体。
- 表明所学 3D 表示提升了机器人操作任务的下游性能。

### 局限性
- 具体实验设置、数据集名称、评价指标与定量结果：摘要未提供足够信息。
- 物体掩码“无监督学到”的验证方式与精度：摘要未提供足够信息。
- 3D 场景编辑的操作细节与定性/定量表现：摘要未提供足够信息。
- 机器人操作任务的具体类型、提升幅度与对比基线：摘要未提供足够信息。
- 方法的计算开销、训练规模与失效场景：摘要未提供足够信息。

### 阅读优先级
中。理由：该工作处于以物体为中心的表示学习与神经场景表示/渲染的交叉点，将 DLP 扩展到 3D 并结合 3D 高斯泼溅，思路清晰，且宣称具备无监督物体掩码、可控 3D 编辑与机器人操作下游增益等实用价值；但摘要未给出定量证据与实验细节，难以仅凭摘要判断其相对现有方法的具体优势与可靠性。

</details>

<details>
<summary>Abstract</summary>

We present ParticleSplat, a self-supervised object-centric learning method that decomposes scenes into a set of latent ''particles'' representing semantic entities through feedforward 3D Gaussian Splatting. Building on the Deep Latent Particles (DLP) framework, which represents images as a set of particles with attributes such as position, scale, and visual appearance, we address a key limitation of DLP: its inherently 2D nature, which prevents explicit 3D spatial and geometric reasoning that are critical for downstream tasks such as robotic manipulation. Leveraging the structural similarity between latent particles and 3D Gaussian primitives, we introduce a 3D latent particle space trained with a novel view synthesis objective. Our model jointly encodes multiple views with camera poses into a shared 3D object-centric latent space, then transforms particles into particle-aligned 3D Gaussians whose composition reconstructs the full scene. On simulated and real-world datasets, we show that this formulation inherently learns object masks without supervision and supports controllable 3D scene editing, such as moving objects by modifying particles in the latent space. We further establish that the learned 3D representation improves downstream performance on robotic manipulation tasks.

</details>

#### 2026-09-16 - RGS: Reflection-aware Gaussian Splatting via Learning Geometry Continuity for Reflective Objects

**Authors:** Xiaobiao Du, Yida Wang, Cheng Bi, Kun Zhan, Xin Yu
**Links:** [abs](https://arxiv.org/abs/2609.19421) - [pdf](https://arxiv.org/pdf/2609.19421)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RGS: Reflection-aware Gaussian Splatting via Learning Geometry Continuity for Reflective Objects
- 作者：Xiaobiao Du, Yida Wang, Cheng Bi, Kun Zhan, Xin Yu
- 出版日期：2026-09-16T20:55:24Z
- 分类：Neural Scene Representations & Rendering（secondary_categories 未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.19421) / [PDF](https://arxiv.org/pdf/2609.19421)

### 一句话总结
针对现有 3DGS 在反射区域易发生表面塌陷、几何与高光质量差的问题，提出基于物理的延迟渲染框架 RGS，通过几何连续性建模来改善反射物体的新视角合成。

### 研究问题
摘要指出，现有 3D Gaussian Splatting（3DGS）方法在反射区域常出现"表面塌陷"（surface collapse）问题，由此导致几何结构不佳以及低质量的高光（specular）渲染。论文要解决的是：如何准确建模反射区域的高光，并提升此类物体的新视角合成质量。

### 核心思路/方法
- 提出一个基于物理的延迟渲染（physically-based deferred rendering）框架，命名为 Reflection-aware Gaussian Splatting（RGS）。
- 观察到一个强大的 3D 基础模型能够提供强 3D 几何先验，用于促进正确的几何建模。
- 基于此提出跨视角形状一致性正则化（cross-view shape consistency regularization），用大模型先验与跨视角约束来正则化几何表面，从而在反射区域产生更平滑的几何表面并减少几何空洞（geometric hollows）。
- 提出反射感知致密化策略（reflection-aware densification strategy），用于捕捉不同视角间的高光变化，以进一步改善反射区域的渲染结果。

### 主要贡献
- 提出 RGS 这一基于物理的延迟渲染框架，可准确建模高光区域并提升新视角合成性能。
- 利用 3D 基础模型先验与跨视角约束构建跨视角形状一致性正则化，缓解反射区域的表面塌陷/几何空洞，得到更平滑的几何表面。
- 提出反射感知致密化策略，捕捉跨视角高光变化，提升反射物体的渲染质量。
- 摘要称大量实验表明该方法能持续渲染高质量反射物体，并达到 state-of-the-art 性能。

### 局限性
- 具体的定量指标、对比方法与消融实验设置：摘要未提供足够信息。
- 所用 3D 基础模型的具体类型、先验形式及使用方式：摘要未提供足够信息。
- 反射感知致密化策略的具体实现细节与判据：摘要未提供足够信息。
- 方法的计算开销、训练/渲染效率及对非反射或混合场景的适用性：摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对 3DGS 在反射物体上的明确缺陷（表面塌陷与高光质量差）提出针对性方案，属于神经场景表示与渲染方向的直接改进，且摘要声称达到 state-of-the-art；若关注反射物体建模、几何正则化或 3DGS 改进，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has significantly improved the quality of novel view synthesis with explicit Gaussian representation. However, we observed that existing 3D Gaussian Splatting methods (3DGS) often suffer from surface collapse issues on reflective regions, and thus produce inferior geometry and low-quality specular. In this work, we propose a physically-based deferred rendering framework, named Reflection-aware Gaussian Splatting (RGS), that can accurately model specular regions and improve novel view synthesis performance. Specifically, we found that a powerful 3D foundation model can provide a strong 3D geometric prior to foster correct geometric modeling. Based on this, we propose a cross-view shape consistency regularization to regularize the geometry surface with the large model prior and cross-view constraints. In this manner, our RGS can produce smoother geometric surfaces on reflective regions while reducing geometric hollows. To further improve rendering results on reflective regions, we present a reflection-aware densification strategy that is designed to capture specular variations across various views. With this strategy, our RGS is able to render novel views of objects in higher quality. Extensive experiments demonstrate our method consistently renders high-quality reflective objects, achieving state-of-the-art performance.

</details>

#### 2026-09-16 - SemSafe-3DGS: Semantic Risk-Aware Active Navigation in Uncertain 3D Gaussian Splatting Maps

**Authors:** Amirhossein Mollaei Khass, Athanasios Cosse, Nader Motee
**Links:** [abs](https://arxiv.org/abs/2609.19330) - [pdf](https://arxiv.org/pdf/2609.19330)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SemSafe-3DGS: Semantic Risk-Aware Active Navigation in Uncertain 3D Gaussian Splatting Maps
- 作者：Amirhossein Mollaei Khass, Athanasios Cosse, Nader Motee
- 出版日期：2026-09-16T18:56:13Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.19330

### 一句话总结
论文提出一种面向带属性 3D 高斯地图的语义风险感知安全主动感知导航框架，通过类相关风险权重调制碰撞间隙模型，并将语义风险约束与主动感知统一在 CBF-QP 中。

### 研究问题
自主机器人需要在部分观测环境中安全导航，同时获取有助于未来规划的观测。现有安全形式化方法主要围绕几何推理，导致几何相似但语义后果不同的场景元素可能引发相近的控制响应。论文关注如何在不确定的 3D 高斯表示地图中，使导航安全约束能够体现语义差异，并兼顾主动感知以减少地图不确定性。

### 核心思路/方法
论文面向带属性的 3D 高斯地图提出语义风险感知的安全主动感知框架。其核心做法包括：使用类相关风险权重调制 Average Value-at-Risk 碰撞间隙模型，使安全关键的 Gaussian primitives 在复合障碍函数中具有更大影响；将加权后的间隙聚合为控制障碍函数；引入与轨迹相关的主动感知障碍，鼓励获取能够降低机器人预期运动方向上几何地图不确定性的观测。两类目标被集成到统一的 CBF-QP 中，将语义风险感知碰撞避免作为硬约束，同时在信息获取与安全或任务进展冲突时对信息获取进行放松。

### 主要贡献
- 提出面向 attributed 3D Gaussian maps 的语义风险感知安全主动感知导航框架。
- 通过类相关风险权重将语义属性引入 Average Value-at-Risk 碰撞间隙模型，使安全关键 Gaussian primitives 在复合障碍中影响更大。
- 将加权间隙聚合为控制障碍函数，并设计轨迹相关的主动感知障碍以降低预期运动方向上的几何地图不确定性。
- 在统一 CBF-QP 中集成安全硬约束与可放松的信息获取目标。
- 摘要称实验展示了高效安全约束、通过主动感知改善导航、语义相关轨迹适应以及 Ackermann 动力学下的实机执行。

### 局限性
摘要未提供足够信息说明方法的计算复杂度、可扩展性、失败案例或与其他方法的定量对比细节。摘要未提供足够信息说明语义属性与风险权重的获取方式、标注依赖或泛化能力。摘要未提供足够信息说明实验规模、数据集、评价指标及消融实验设置。

### 阅读优先级
高。理由：该论文将语义风险、主动感知、控制障碍函数与 3D 高斯地图导航结合，主题聚焦于不确定环境下的安全自主导航，且摘要明确提到统一 CBF-QP 与实机执行；若关注语义安全、主动感知或 3DGS 机器人应用，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous robots operating in partially observed environments must navigate safely while acquiring observations that improve future planning. Existing safety formulations generally reason primarily about geometry. Consequently, geometrically similar scene elements may induce comparable control responses despite having different semantic consequences. We present a semantic risk aware safe-active perception framework for navigation in attributed 3D Gaussian maps. Semantic attributes modulate an Average Value-at-Risk collision clearance model through class dependent risk weights, allowing safety-critical Gaussian primitives to receive greater influence in the composite barrier. The resulting weighted clearances are aggregated into a control barrier function, while a trajectory-relevant active perception barrier promotes observations that reduce geometric map uncertainty along the robot's anticipated motion. Both objectives are integrated in a unified CBF-QP that enforces semantic risk-aware collision avoidance as a hard constraint while relaxing information acquisition when it conflicts with safety or task progress. Experiments demonstrate efficient safety constraint, improved navigation through active perception, semantic dependent trajectory adaptation, and real-robot execution under Ackermann dynamics.

</details>

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

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-17 - DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation

**Authors:** Yan Qin, Yue Chen, Wenwei Lin, Shujia Liu, Chuqiao Lyu, Kailun Su, Chenze Yu, Ping Luo, Wenbo Ding, Tianxing Chen, Renjing Xu
**Links:** [abs](https://arxiv.org/abs/2609.20649) - [pdf](https://arxiv.org/pdf/2609.20649)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation
- 作者：Yan Qin, Yue Chen, Wenwei Lin, Shujia Liu, Chuqiao Lyu, Kailun Su, Chenze Yu, Ping Luo, Wenbo Ding, Tianxing Chen, Renjing Xu
- 出版日期：2026-09-17T16:28:34Z
- 分类：Embodied / Robotics / AR Applications（一级分类；二级分类未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.20649) ｜ [PDF](https://arxiv.org/pdf/2609.20649)

### 一句话总结
DexTouch-WM 是一种动作条件化的世界模型，利用可扩展的人类触摸数据与共享触觉传感布局，联合预测未来 RGB 观测与双侧触觉动态，以缓解真实机器人触觉交互数据难以规模化的问题。

### 研究问题
学习接触丰富的灵巧操作预测模型需要密集的触觉交互数据，但这类数据在真实机器人上采集成本高、难以扩展，并且与具体本体（embodiment）的传感器绑定。论文试图解决：如何利用可扩展的人类触摸数据来监督机器人触觉世界模型的学习。

### 核心思路/方法
- 核心洞察：当触觉观测与动作空间被“兼容化”后，人类与机器人操作共享可迁移的接触动态。
- 硬件与数据对齐：在人类手与灵巧机器人手上部署具有共享传感布局的柔性压阻阵列；并将人类运动重定向到机器人动作空间。
- 模型结构：DexTouch-WM 将预训练视频专家与轻量触觉专家耦合，使用解剖学感知的触觉 token（anatomy-aware tactile tokens）和对齐的动作条件。
- 训练与预测目标：以人类交互监督同一个用于真实机器人预测的动态模型，联合预测未来 RGB 观测与双侧触觉动态。
- 缩放实验设计：固定 5 小时真实机器人监督，将人类交互从 0 小时增至 100 小时，在人类与机器人任务集不相交的条件下评估留出的机器人域视觉、几何与接触预测。

### 主要贡献
- 提出 DexTouch-WM：一种动作条件化、可同时预测未来 RGB 观测与双侧触觉动态的世界模型。
- 通过共享触觉传感布局与人类动作重定向，构建人类触摸监督机器人触觉世界模型的可迁移路径。
- 在固定真实机器人监督量的设置下，验证增加人类交互时长（0 到 100 小时）可显著提升留出的机器人域视觉、几何与接触预测表现。
- 将世界模型进一步评估为策略评估的替代环境，以及用于真实机器人策略学习的合成轨迹生成器，表明可扩展人类交互是学习灵巧机器人世界模型的补充数据轴。

### 局限性
- 摘要未提供足够信息说明真实机器人实验的具体平台、任务种类、评估指标细节、人类与机器人任务集不相交的具体范围。
- 摘要未提供足够信息说明模型计算开销、推理速度、实时性表现。
- 摘要未提供足够信息说明触觉传感布局的具体设计、重定向方法的误差或失败案例。
- 摘要未提供足够信息说明在策略评估与合成轨迹生成上的定量结果与局限性。

### 阅读优先级
高。理由：该工作提出利用人类触摸数据监督机器人触觉世界模型的新数据轴，涉及人机触觉传感对齐、动作条件世界模型、虚实/人机迁移与策略学习等关键问题，且设置了从 0 到 100 小时人类交互的缩放实验，对接触丰富灵巧操作与触觉世界模型方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Learning predictive models of contact-rich dexterous manipulation requires dense tactile interaction, but such data are costly to scale on real robots and remain tied to embodiment-specific sensors. We introduce DexTouch-WM, an action-conditioned world model that learns from scalable human touch to jointly predict future RGB observations and bilateral tactile dynamics. Our insight is that human and robot manipulation share transferable contact dynamics when their tactile observations and action spaces are made compatible. We deploy flexible piezoresistive arrays with a shared sensing layout on both human and dexterous robot hands, and retarget human motion into the robot action space so that human interaction can supervise the same dynamics model used for real-robot prediction. DexTouch-WM couples a pretrained video expert with a lightweight tactile expert using anatomy-aware tactile tokens and aligned action conditioning. In human-to-robot scaling experiments, we keep five hours of real-robot supervision fixed while increasing human interaction from 0 to 100 hours, and observe substantial improvements in held-out robot-domain visual, geometric, and contact prediction despite disjoint human and robot task sets. Beyond prediction, we evaluate the world models as surrogate environments for policy evaluation and as generators of synthetic trajectories for real-robot policy learning, showing that scalable human interaction provides a complementary data axis for learning dexterous robot world models.

</details>

#### 2026-09-17 - AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations

**Authors:** Soham Patil, Om Sanjay Gunjal, Sourabh Bhosale, Arhan Chavare, Ramandeep Singh Hora, Spandan Roy
**Links:** [abs](https://arxiv.org/abs/2609.20107) - [pdf](https://arxiv.org/pdf/2609.20107)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations
- 作者：Soham Patil, Om Sanjay Gunjal, Sourabh Bhosale, Arhan Chavare, Ramandeep Singh Hora, Spandan Roy
- 出版日期：2026-09-17T12:07:28Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.20107) / [PDF](https://arxiv.org/pdf/2609.20107)

### 一句话总结
AnyViewDex 提出一种非对称训练流程，通过在仿真训练中引入多视角对比对齐与特权 3D 几何监督，使多指灵巧操作策略在部署时仅依赖未标定单目 RGB 与本体感知即可实现视角不变的零样本抓取。

### 研究问题
多指灵巧操作的视觉运动策略对相机视角变化高度敏感。为实现视角不变性，近期方法多依赖 RGB-D 或点云等显式 3D 模态，但这会带来硬件依赖、标定要求以及真实部署中对传感器噪声的脆弱性。论文试图解决的问题是：能否在不依赖测试时显式 3D 传感的条件下实现视角不变控制。

### 核心思路/方法
论文提出 AnyViewDex，一种非对称训练流程，将多视角对比对齐与特权 3D 几何监督相结合。具体而言，在仿真训练阶段回归绝对 3D 物体坐标，以此作为辅助目标，提供几何 grounding 信号，缓解全局池化对比嵌入的空间坍缩问题。部署阶段，策略仅使用未标定单目 RGB 和本体感知，进行零样本操作，不依赖测试时深度。方法在强化学习和学生-教师蒸馏两种设定下进行了验证。

### 主要贡献
- 证明无需测试时显式 3D 传感即可实现视角不变控制，方法是在仿真训练中将几何知识编码进视觉表示。
- 提出非对称训练流程，结合多视角对比对齐与特权 3D 几何监督。
- 通过回归绝对 3D 物体坐标作为辅助目标，缓解全局池化对比嵌入的空间坍缩。
- 在 xArm7 与 16-DoF LEAP Hand 硬件评估中，跨八种未见物体和六个未标定视角达到 76.7% 抓取成功率（480 次试验；所有消融条件共 2,400 次）。
- 表明几何 grounded 的单目策略可零样本迁移，无需测试时深度。

### 局限性
- 摘要未提供足够信息说明方法在更大规模物体类别、更复杂操作任务（如非抓取类灵巧操作）上的泛化能力。
- 摘要未提供足够信息说明对极端光照、遮挡、动态场景或传感器噪声的鲁棒性。
- 摘要未提供足够信息说明仿真到现实迁移中特权 3D 监督所需数据的具体获取成本与可扩展性。
- 摘要未提供足够信息说明与依赖 RGB-D 或点云的方法在同等条件下的详细对比结果。
- 摘要未提供足够信息说明失败案例的具体模式与原因分析。

### 阅读优先级
高。理由：该论文针对灵巧操作中视角不变性这一关键问题，提出不依赖测试时 3D 传感的单目 RGB 方案，并在真实硬件上进行了较大规模评估（480 次试验、多物体多视角），对具身智能与机器人操作方向具有较强参考价值；同时摘要给出了明确的方法机制与量化结果，值得进一步阅读全文以了解实验细节与局限。

</details>

<details>
<summary>Abstract</summary>

Visuomotor policies for multi-fingered dexterous manipulation are highly sensitive to camera viewpoint shifts. To achieve view invariance, recent methods increasingly rely on explicit 3D modalities like RGB-D or point clouds, which can introduce hardware dependencies, calibration requirements, and vulnerability to sensor noise during real-world deployment. In this work, we show that view-invariant control can be achieved without explicit test-time 3D sensing by encoding geometric knowledge into the visual representation during simulation. We present AnyViewDex, an asymmetric training pipeline that combines multi-view contrastive alignment with privileged 3D geometric supervision. By regressing absolute 3D object coordinates during simulated training, this auxiliary objective provides a geometric grounding signal that mitigates the spatial collapse of the globally pooled contrastive embedding. At deployment, the policy operates zero-shot using only uncalibrated monocular RGB and proprioception. We validate this approach across both reinforcement learning and student-teacher distillation. In hardware evaluation on an xArm7 with a 16-DoF LEAP Hand, AnyViewDex reaches 76.7% grasping success across eight unseen objects and six uncalibrated viewpoints (480 trials; 2,400 across all ablation conditions), indicating that geometrically grounded monocular policies transfer zero-shot without test-time depth. Project Page: https://anyviewdex.github.io/

</details>

#### 2026-09-17 - Feeling Terrain Before Crossing: World Models for Off-Road Navigation

**Authors:** E-In Son, Dong-Wook Kim, Ji-Hoon Hwang, Kangsun Lee, Jisung Bae, Jung-Taak Kim, Seung-Woo Seo
**Links:** [abs](https://arxiv.org/abs/2609.19863) - [pdf](https://arxiv.org/pdf/2609.19863)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Feeling Terrain Before Crossing: World Models for Off-Road Navigation
- 作者：E-In Son, Dong-Wook Kim, Ji-Hoon Hwang, Kangsun Lee, Jisung Bae, Jung-Taak Kim, Seung-Woo Seo
- 出版日期：2026-09-17T08:19:06Z
- 分类：Embodied / Robotics / AR Applications（主分类；二级分类摘要未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.19863) / [PDF](https://arxiv.org/pdf/2609.19863)

### 一句话总结
论文提出 Feel-WM，这是首个引入本体感觉（proprioception）条件的越野导航世界模型，在预测相机所见场景的同时预测机器人未来将“感受到”的物理状态与失败风险，从而在非结构化地形上实现更优的前瞻规划。

### 研究问题
导航世界模型通过“预见”来规划：预测各候选动作序列产生的未来并选择最优者，而非直接将观测映射为动作。但论文指出，城市环境中预测场景已足以作为决策代理，而越野导航的关键在于机器人—地形的交互，因此预测不能只覆盖相机将看到什么，还必须覆盖机器人将感受到什么。现有以场景为中心的模型无法预测机器人在规划轨迹上会打滑、倾斜或震动的程度。如何让世界模型在越野场景中同时预测视觉未来与物理未来，是本文要解决的问题。

### 核心思路/方法
- 以本体感觉作为输入条件：摘要指出本体感觉直接捕捉上述动力学，作为输入时可改进对物理未来的预测。
- Feel-WM 同时预测两类未来：机器人将感受到的物理未来（以未来本体感觉状态和失败风险的形式表示），以及相机将看到的场景。
- 无人工标签学习：未来本体感觉状态与失败风险均从机器人自身经验中学习，无需人工标注。
- 规划器设计：规划器将物理未来与场景一并展开（roll out），并在一个可分离的评分中权衡预测失败风险与目标相似度，而非将二者混为一谈。

### 主要贡献
- 提出 Feel-WM，被描述为首个以本体感觉为条件、在预测相机所见之外还预测机器人所感的越野导航世界模型。
- 给出物理未来的具体表征形式：未来本体感觉状态 + 失败风险，二者均从机器人自身经验学习、无需人工标签。
- 提出可分离评分机制，将预测失败风险与目标相似度分开加权。
- 在真实越野数据与仿真中验证：在开环规划与闭环崎岖地形导航上，Feel-WM 优于仅视觉的导航世界模型，且覆盖轮式与足式平台。
- 部署验证：在 Husky 上于山地小径进行车载规划，提前预测粗糙地面并绕行，完成了端到端策略失败的路线。

### 局限性
摘要未提供足够信息。可确认的边界是：论文仅报告了在真实越野数据、仿真以及 Husky 山地小径部署上的结果，未在摘要中说明具体地形类型范围、失败案例、计算开销、跨平台迁移的泛化边界或与更多基线方法的对比细节。

### 阅读优先级
中。理由：选题处于具身智能与越野机器人导航的交叉点，“以本体感觉为条件预测物理未来”的思路对世界模型与机器人规划方向的研究者有明确参考价值，且包含真实平台部署验证；但摘要未给出定量结果、方法细节与消融信息，若研究兴趣不涉及越野导航、世界模型或机器人—地形交互，优先级可下调。

</details>

<details>
<summary>Abstract</summary>

Navigation world models plan by foresight, predicting the future that each candidate action sequence produces and selecting the best, rather than mapping observations to actions directly. Unlike urban settings where a predicted scene is a sufficient proxy, off-road navigation hinges on the robot--terrain interaction, so the prediction must cover not only what the camera will see but what the robot will feel. However, existing scene-focused models do not predict how much the robot will slip, tilt or shake along a planned trajectory. Proprioception captures these dynamics directly and, when used as input, improves the prediction of the physical future. We present Feel-WM, the first off-road navigation world model that conditions on proprioception and predicts what the robot will feel alongside what the camera will see. The physical future takes the form of a future proprioceptive state and a failure risk, both learned from the robot's own experience without human labels. The planner rolls out the physical future alongside the scene and weighs the predicted failure risk against goal similarity in a separable score. Experiments on real off-road data and in simulation demonstrate that Feel-WM outperforms visual-only navigation world models in open-loop planning and closed-loop rough-terrain navigation across wheeled and legged platforms. Deployed on a Husky on mountain trails, Feel-WM plans onboard, predicts rough ground ahead and steers around it, completing courses that an end-to-end policy fails.

</details>

#### 2026-09-17 - SnapPhysics: A Physics-Aware Scene Graph from a Single View for Interactive Mixed Reality Scenes

**Authors:** Suji Kang, Seok-Young Kim, Young Bin Kim, Taewook Ha, Dieter Schmalstieg, Shohei Mori, Woontack Woo
**Links:** [abs](https://arxiv.org/abs/2609.19815) - [pdf](https://arxiv.org/pdf/2609.19815)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SnapPhysics: A Physics-Aware Scene Graph from a Single View for Interactive Mixed Reality Scenes
- 作者：Suji Kang, Seok-Young Kim, Young Bin Kim, Taewook Ha, Dieter Schmalstieg, Shohei Mori, Woontack Woo
- 出版日期：2026-09-17T07:26:56Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.19815 ；PDF https://arxiv.org/pdf/2609.19815 ；项目页 https://snapphysics-ismar2026.github.io/

### 一句话总结
SnapPhysics 是一个无需训练、从单张图像重建三维物体并估计质量、摩擦和重心等物理属性的框架，通过物理感知场景图结合实例级三维重建与空间对齐，为混合现实提供物理上连贯的交互。

### 研究问题
在混合现实（MR）中，物理上连贯的交互不仅依赖几何，也依赖质量、摩擦、重心等物理属性。现有方法存在两类局限：一是通过分析视频中的物体动态来推断这些属性，计算代价高；二是对单张图像查询视觉语言模型（VLM），缺乏几何基础与物体间关系。论文旨在解决单视图下物理属性估计的上述问题。

### 核心思路/方法
SnapPhysics 是一个无需训练的框架，从单张图像重建三维物体并估计其物理属性（质量、摩擦、重心）。方法将实例级三维重建与空间对齐，与一个物理感知场景图相结合；该场景图编码物体间关系和每个物体的度量几何，作为结构化上下文，用于基于 VLM 的物理属性推理。由此弥补 VLM 单图查询缺乏几何基础与物体间关系的不足，并避免基于视频动态推断的高计算成本。摘要称其无需人工参数调优即可支持物理交互式 MR 体验。

### 主要贡献
- 提出 SnapPhysics，一个无需训练、从单张图像重建三维物体并估计质量、摩擦、重心等物理属性的框架。
- 结合实例级三维重建与空间对齐，以及编码物体间关系和逐物体度量几何的物理感知场景图，作为 VLM 属性推理的结构化上下文。
- 在 3D-FRONT 上，场景级 F-Score 相比最佳基于学习的方法提升 18.6%。
- 在具有真实质量标注的真实采集场景中，相比纯 VLM 估计，平均绝对对数差误差（mALDE）最多降低 20.5%，对数尺度相关性（\(r^2_{\mathrm{ls}}\)）最多提升 19.6%。
- 使物理交互式 MR 体验无需人工参数调优。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败情形、对特定场景或物体类别的依赖、重建精度上限、推理耗时、对 VLM 的依赖程度及泛化能力等局限。

### 阅读优先级
高。理由：该工作面向 MR 中物理属性估计这一关键问题，提出无需训练的单视图框架，并在 3D-FRONT 与真实采集场景上给出明确的定量提升；同时涉及三维重建、场景图与 VLM 推理的结合，对具身/机器人与 AR 应用方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We propose SnapPhysics, a training-free framework that reconstructs 3D objects and estimates their physical properties such as mass, friction, and center of gravity from a single image. For physically coherent interactions in mixed reality (MR), such properties are as important as geometry. Prior approaches infer them by analyzing object dynamics in video, which is computationally costly, or by querying vision-language models (VLMs) on single images, which lacks geometric grounding and inter-object relationships. We address these limitations by combining instance-level 3D reconstruction and spatial alignment with a physics-aware scene graph that encodes these relationships and per-object metric geometry as structured context for VLM-based property reasoning. Experiments on 3D-FRONT show that SnapPhysics improves scene-level F-Score by 18.6% over the best learning-based method, and on real captured scenes with ground-truth mass, it reduces the mean absolute log difference error (mALDE) by up to 20.5% and improves log-scale correlation ($r^2_{\mathrm{ls}}$) by up to 19.6% over VLM-only estimation. SnapPhysics enables physically interactive MR experiences without manual parameter tuning. Project page: https://snapphysics-ismar2026.github.io/.

</details>

#### 2026-09-17 - VAST: V2X/Dynamic Map-Aware Autonomous Driving Systems Validation Toolchain

**Authors:** Shunsuke Ito, Takuya Azumi
**Links:** [abs](https://arxiv.org/abs/2609.19681) - [pdf](https://arxiv.org/pdf/2609.19681)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VAST: V2X/Dynamic Map-Aware Autonomous Driving Systems Validation Toolchain
- 作者：Shunsuke Ito, Takuya Azumi
- 出版日期：2026-09-17T04:25:47Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无副分类
- 链接：摘要链接 https://arxiv.org/abs/2609.19681 ；PDF 链接 https://arxiv.org/pdf/2609.19681

### 一句话总结
VAST 是一个面向 V2X 与动态地图的自动驾驶系统级验证工具链，通过集成 Scenic、Scenario Simulator v2、AWSIM、Autoware 和 SIM-LDM 解决互操作性问题，并在遮挡交叉口等场景中量化了边界案例发现效率与动态地图可用性带来的安全收益。

### 研究问题
论文关注 IoT-to-Edge-to-Cloud 连续体中的协同自动驾驶系统级验证问题。该验证需要覆盖车辆、基础设施传感器、边缘侧动态地图服务和车载自动驾驶栈，因此面临跨组件互操作与联合仿真的挑战。摘要指出 VAST 不提出新的搜索算法，而是针对以下互操作性问题：Lanelet2 到 Scenic 的映射、通过 SS2 进行基于 ROS 2 的联合仿真、动态地图对象注入 Autoware，以及 TTC、PET、碰撞、超时和性能测量的收集。

### 核心思路/方法
VAST 的核心思路是构建一个 V2X/动态地图感知的验证工具链，将 Scenic、Scenario Simulator v2、AWSIM、Autoware 和 SIM-LDM 连接起来，以实现系统级联合仿真与验证。其方法重点不在搜索算法创新，而在互操作性工程，包括：
- Lanelet2 到 Scenic 的映射；
- 基于 ROS 2 通过 SS2 实现联合仿真；
- 将动态地图对象注入 Autoware；
- 收集 TTC、PET、碰撞、超时和性能测量。

摘要中报告了在遮挡交叉口场景下的评估：Lanelet2 兼容的约束采样将边界案例发现率从 40.0% 提升到 80.0%，并将每个已发现边界案例的平均时间从 259.7 秒降低到 110.4 秒。在相同生成场景分布下，动态地图可用性将碰撞率从 78.0% 降低到 40.0%，并将非碰撞结果从 22.0% 增加到 60.0%，同时 TTC/PET 出现统计显著变化。此外，在 1 至 16 个 NPC 的吞吐量研究中，采样时间保持在 0.1 秒以下，而 AWSIM/Autoware 执行与重启开销主导了运行时间。

### 主要贡献
- 提出 VAST 工具链，连接 Scenic、Scenario Simulator v2、AWSIM、Autoware 和 SIM-LDM，用于 V2X/动态地图感知的自动驾驶系统级验证。
- 解决多项互操作性问题，包括 Lanelet2-to-Scenic 映射、基于 ROS 2 的联合仿真、动态地图对象注入 Autoware，以及 TTC/PET/碰撞/超时/性能测量收集。
- 在遮挡交叉口场景中展示约束采样可提升边界案例发现率并缩短发现时间。
- 展示动态地图可用性可降低碰撞率并增加非碰撞结果，且 TTC/PET 变化具有统计显著性。
- 通过 1-16 个 NPC 的吞吐量研究，指出采样开销较低，而 AWSIM/Autoware 执行与重启开销是运行时主要瓶颈。
- 将 VAST 定位为协同自动驾驶 CPS 的实用验证基础设施。

### 局限性
摘要未提供足够信息说明 VAST 在遮挡交叉口之外的场景泛化能力、所依赖工具链的版本兼容性边界、动态地图注入的完整性与实时性约束、统计显著性的具体检验方法与效应量、以及真实世界部署验证情况。摘要也未提供关于失败案例、超时判定的具体阈值、性能测量的详细定义与可复现性配置的信息。此外，摘要明确 VAST 不引入新的搜索算法，因此其贡献主要限于互操作性与验证基础设施层面，搜索策略本身的创新性未在摘要中体现。

### 阅读优先级
中。理由：该论文针对协同自动驾驶系统级验证中的工具链互操作问题，提供了具体的集成方案与量化结果，对从事 V2X、动态地图、自动驾驶仿真验证和 CPS 系统测试的研究者与工程师有直接参考价值。但摘要表明其不提出新的搜索算法，核心贡献偏工程集成与验证基础设施，若读者关注算法创新或理论突破，优先级可能降低；若关注可落地的验证工具链与实验指标，则值得阅读。

</details>

<details>
<summary>Abstract</summary>

Cooperative autonomous driving in the IoT-to-Edge-to-Cloud continuum requires system-level validation across vehicles, infrastructure sensors, edge-side Dynamic Map services, and in-vehicle autonomous-driving stacks. This paper presents VAST, a V2X/Dynamic Map-aware validation toolchain that connects Scenic, Scenario Simulator v2, AWSIM, Autoware, and SIM-LDM. VAST does not introduce a new search algorithm; instead, it addresses interoperability challenges, including Lanelet2-to-Scenic mapping, ROS 2-based co-simulation through SS2, Dynamic Map object injection into Autoware, and collection of TTC, PET, collision, timeout, and performance measurements. In occluded-intersection scenarios, Lanelet2-compatible constrained sampling increases the edge-case discovery rate from 40.0% to 80.0% and reduces the average time per discovered edge case from 259.7 s to 110.4 s. Under the same generated scenario distribution, Dynamic Map availability reduces the collision rate from 78.0% to 40.0% and increases non-collision outcomes from 22.0% to 60.0%, with statistically significant TTC/PET shifts. A throughput study with 1-16 NPCs shows that sampling remains below 0.1 s, whereas AWSIM/Autoware execution and restart overhead dominate runtime. These results position VAST as a practical validation infrastructure for cooperative autonomous-driving CPSs.

</details>

#### 2026-09-17 - VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control

**Authors:** Zhongbo Zhang, Jiayi Jin, Yifan Wang, Zaibin Zhang, Haiwen Diao, Lijun Wang, Huchuan Lu
**Links:** [abs](https://arxiv.org/abs/2609.19554) - [pdf](https://arxiv.org/pdf/2609.19554)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control
- 作者：Zhongbo Zhang, Jiayi Jin, Yifan Wang, Zaibin Zhang, Haiwen Diao, Lijun Wang, Huchuan Lu
- 出版日期：2026-09-17T01:24:51Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.19554 ；PDF https://arxiv.org/pdf/2609.19554

### 一句话总结
论文提出 VA-Bench，用于评估通用多模态大模型在“观察—推理—行动—修正”闭环中的具身空间智能，覆盖仅 RGB 演示、主动选择视角与度量笛卡尔指令执行，并报告当前模型在长时程任务上的显著不足。

### 研究问题
论文关注的是：在不完整观测下，模型是否能够识别并主动获取缺失证据，将其解释到共同的空间参照系中，并据此采取行动。空间智能不仅是描述物体位置，还需要完成完整的 observe-reason-act-revise 闭环。VA-Bench 旨在检验通用 MLLM 能否把视觉演示与主动获取的证据转化为成功的具身行动。

### 核心思路/方法
VA-Bench 要求通用 MLLM 从仅 RGB 的演示中学习程序性上下文，主动选择相机视角，发出度量笛卡尔命令，并根据执行反馈修正命令。模型不获得特权物体位姿、oracle 轨迹或学习到的动作头。一个固定的、与模型无关的控制器只执行模型指定的目标。VA-Bench 包含 14 个基础任务族（11 个单臂和 3 个双臂）、7 个留出的几何/布局变体，以及一条长时程五物体组合赛道。评估在每项基础任务相同的 20 个经物理验证的种子上，对 12 个主要模型条件进行三次独立运行，报告终端成功率、九项轨迹级行为诊断和子任务进度。

### 主要贡献
- 提出 VA-Bench，用于评估完整 observe-reason-act-revise 闭环中的具身空间智能。
- 设计涵盖仅 RGB 演示、主动相机视角选择、度量笛卡尔命令发布与基于执行反馈修正的评测流程。
- 构建包含 14 个基础任务族、7 个留出几何/布局变体以及长时程五物体组合赛道的任务体系。
- 在 12 个主要模型条件、三次独立运行和每项基础任务 20 个物理验证种子上进行系统评估，并报告终端成功率、九项轨迹级行为诊断与子任务进度。
- 实验发现：最佳模型在标注运行中目标定位得分为 100.0%，空间关系得分为 78.9%，但三次运行宏平均任务成功率仅为 53.93±3.17%；主动相机控制显著优于被动多视角观察，一组匹配比较中成功率从 27.86% 升至 57.50%；留出几何迁移可使任务成功率下降超过 30 个百分点；没有任何模型完成严格的长时程回合，尽管取得了可观的子任务进展。

### 局限性
摘要未提供足够信息说明 VA-Bench 在真实机器人平台上的部署范围、任务种类之外的可扩展性、计算成本、模型规模影响、失败模式的具体归因，以及除已报告指标外的其他评测维度。摘要也未提供关于数据集规模、标注成本、仿真与真实环境比例、控制器具体实现细节和统计显著性的充分信息。

### 阅读优先级
高。理由：该论文直接针对具身空间智能与通用 MLLM 的闭环行动能力，提出了包含主动感知、度量控制和反馈修正的基准，并给出多个定量发现，如主动相机控制带来显著提升、留出几何迁移导致大幅下降、长时程任务无人完成。这些结果对具身智能、机器人学习和多模态模型评测具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires more than describing object locations. Under incomplete observation, models must identify and acquire missing evidence, interpret it in a common spatial frame, and act on it. We introduce VA-Bench to evaluate the complete observe-reason-act-revise loop. General-purpose MLLMs learn procedural context from RGB-only demonstrations, actively select camera viewpoints, issue metric Cartesian commands, and revise them from execution feedback. Models receive no privileged object poses, oracle trajectories, or learned action heads. A fixed model-agnostic controller executes only model-specified targets. VA-Bench contains 14 base task families (11 single-arm and three dual-arm), seven held-out geometry/layout variants, and a long-horizon five-object composition track. We evaluate 12 primary model conditions in three independent runs over the same 20 physically verified seeds per base task, reporting terminal success, nine trajectory-level behavioral diagnostics, and subtask progress. First, the best-performing model scores 100.0% on target localization and 78.9% on spatial relations in the annotated run. Its three-run macro-average task success is only 53.93+/-3.17%. Second, active camera control significantly improves task success over passive multi-view observation. In one matched comparison, success rises from 27.86% to 57.50%. Third, held-out geometric transfer can reduce task success by over 30 percentage points. No model completes a strict long-horizon episode, despite substantial partial progress. VA-Bench thus tests whether general-purpose MLLMs can turn visual demonstrations and actively acquired evidence into successful embodied action.

</details>

#### 2026-09-17 - AURORA: A Natural Language-Driven Agentic Framework for Understanding, Reasoning, and Orchestrating Reliable Air-Ground Co-Simulation

**Authors:** Keshu Wu, Hao Zhang, Rui Gan, Xiangbo Gao, Xiaopeng Li, Zhengzhong Tu, Yang Zhou
**Links:** [abs](https://arxiv.org/abs/2609.19527) - [pdf](https://arxiv.org/pdf/2609.19527)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AURORA: A Natural Language-Driven Agentic Framework for Understanding, Reasoning, and Orchestrating Reliable Air-Ground Co-Simulation
- 作者：Keshu Wu, Hao Zhang, Rui Gan, Xiangbo Gao, Xiaopeng Li, Zhengzhong Tu, Yang Zhou
- 出版日期：2026-09-17T00:41:46Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.19527 ；PDF https://arxiv.org/pdf/2609.19527

### 一句话总结
AURORA 将自然语言驱动的空地协同仿真场景生成建模为“编译与验证”过程，通过显式中间表示与运行时验证、局部修复，提升生成场景对用户所要求交互关系的忠实实现能力。

### 研究问题
空地交通研究日益依赖协同仿真，但场景构建劳动密集且难以验证。论文指出的关键问题是：生成场景可能成功执行，却未能实现用户所要求的空间、时间、通信或行为关系。因此，研究问题可概括为：如何从自然语言出发，生成不仅可执行、而且忠实实现所请求交互关系的可靠空地协同仿真场景。

### 核心思路/方法
论文提出 AURORA，一个自然语言驱动的智能体框架，将空地场景生成视为带有验证的编译过程。其核心是 Air-Ground Scenario Graph（AGSG），一种带类型的中间表示，显式连接智能体、空中任务、事件、通信链路、成功条件及其跨域依赖关系。该共享表示支持统一工作流中的多项能力：基于仿真器的解析、道路—空域联合落地、时间规划、执行前可行性检查、基于轨迹的运行时验证、失败定位，以及有界修复。论文还引入 AURORA-Bench，用于评估生成场景不仅是否执行，而且是否忠实实现所请求的交互。

### 主要贡献
- 提出 AURORA 框架，将自然语言驱动的空地协同仿真场景生成形式化为“编译并验证”的过程。
- 提出 Air-Ground Scenario Graph（AGSG）作为带类型的中间表示，显式建模智能体、空中任务、事件、通信链路、成功条件及跨域依赖。
- 基于 AGSG 构建统一工作流，涵盖解析、联合落地、时间规划、执行前可行性检查、运行时验证、失败定位与有界修复。
- 引入 AURORA-Bench，用于评估生成场景是否忠实实现所请求交互，而不仅是是否可执行。
- 实验显示：结构化执行显著提升可靠性；运行时验证能暴露基于完成度评估所忽略的“静默失败”；局部修复可在不重新生成整个场景的情况下解决许多违规。

### 局限性
摘要未提供足够信息说明具体实验设置、基线对比、语言模型范围、AURORA-Bench 的规模与指标细节、有界修复的失败案例与适用范围、计算开销、可扩展性或真实系统部署限制。以上方面均需依据论文全文进一步确认。

### 阅读优先级
高。理由：该论文聚焦自然语言驱动的可靠协同仿真生成，提出显式中间表示与运行时验证机制，并给出基准 AURORA-Bench；对关注具身/机器人/AR 应用、空地交通仿真、语言驱动场景生成与可验证智能体工作流的研究者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Air-ground transportation research increasingly relies on co-simulation, yet constructing scenarios remains labor-intensive and difficult to validate. More importantly, a generated scenario may execute successfully while failing to realize the spatial, temporal, communication, or behavioral relationships requested by the user. This paper presents AURORA, a natural-language-driven agentic framework that treats air-ground scenario generation as a process of compilation with verification. Central to AURORA is the Air-Ground Scenario Graph (AGSG), a typed intermediate representation that explicitly connects agents, aerial missions, events, communication links, success conditions, and their cross-domain dependencies. This shared representation enables simulator-grounded parsing, joint road-airspace grounding, temporal planning, pre-execution feasibility checking, trace-based runtime verification, failure localization, and bounded repair within a unified workflow. We further introduce AURORA-Bench to evaluate not only whether generated scenarios execute, but whether they faithfully realize the requested interactions. Experiments across multiple language models show that structured execution substantially improves reliability, while runtime verification exposes silent failures that completion-based evaluation overlooks. Localized repair further resolves many violations without regenerating the entire scenario. The results show that reliable scenario generation requires verifying realized behavior, not merely executable code, and demonstrate the value of explicit intermediate representations for verifiable and repairable language-driven co-simulation.

</details>

#### 2026-09-16 - WZPlanner: Safe End-to-End Path Planning for Autonomous Driving in Work Zones

**Authors:** Nishad Sahu, Changzhong Qian, Guangzhou Cai, Shounak Sural, Ragunathan, Rajkumar
**Links:** [abs](https://arxiv.org/abs/2609.19393) - [pdf](https://arxiv.org/pdf/2609.19393)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WZPlanner: Safe End-to-End Path Planning for Autonomous Driving in Work Zones
- 作者：Nishad Sahu, Changzhong Qian, Guangzhou Cai, Shounak Sural, Ragunathan, Rajkumar
- 出版日期：2026-09-16T20:22:51Z
- 分类：Embodied / Robotics / AR Applications（主要分类，二级分类未提供）
- 链接：摘要页 https://arxiv.org/abs/2609.19393 ；PDF https://arxiv.org/pdf/2609.19393 ；代码与数据集 https://github.com/Nishad-Sahu/WZPlanner

### 一句话总结
论文面向施工区（Work Zone）中车道几何被临时交通管制改变、且可能不在车载地图中的场景，提出数据集 WorkZonePlan、半自动数据生成流程 WAVE 以及联合预测车道边界、施工区边界与行驶轨迹的 BoundaryFormer（BF/BF++），并在闭环 CARLA 评估路线上报告了优于 SimLingo 与 TransFuser++ 的 Driving Score。

### 研究问题
施工区通过临时交通控制和封路改变车道几何，这些变化可能不存在于车载地图中，给自动驾驶车辆的感知与规划带来挑战。同时，具有结构化几何监督的公开数据集稀缺，限制了模型的泛化能力。论文关注的核心问题是：如何在缺乏地图先验、且几何结构被临时改变的施工区中，实现更安全的端到端路径规划。

### 核心思路/方法
论文从数据与模型两方面入手：

1. **数据集 WorkZonePlan**：包含 149K+ 合成样本和 5K+ 真实世界多模态样本，带有车道边界、施工区边界和行驶轨迹选项的 3D 标注；并提供 76 个闭环 CARLA 场景，在三种天气条件下回放，生成 228 条 Bench2Drive 格式的评估路线。
2. **数据生成流程 WAVE**（Work-zone-focused AV data generation in Virtual and rEal Environments）：用于创建该数据集的半自动化流程。
3. **模型 BoundaryFormer（BF）**：基于 transformer，联合预测车道边界多项式、施工区边界多项式和行驶轨迹；边界预测使用 slot attention。
4. **消融发现与 BF++**：消融表明，使用边界 slot 特征的独立轨迹解码器相比仅用 slot attention 的方法能显著改善轨迹预测。基于此，BF++ 提供 Camera 和 Camera+LiDAR 两种变体，并引入度量地平面编码、带类型的边界/轨迹查询、长程点锚点、图像空间曲线细化，以及保守的门控 LiDAR 融合。
5. **评估结果**：在评估冻结时四个模型共有的 211 条路线上，BF++-Camera 与 BF++-Camera+LiDAR 的 Driving Score 分别为 63.0 和 64.4，对比 SimLingo 的 59.3 和 TransFuser++ 的 26.1。BF++ 参数量比 SimLingo 小 40 倍，比 TransFuser++ 小 10 倍以上，同时 Driving Score 更高。

### 主要贡献
- 提出面向施工区的多模态数据集 WorkZonePlan，覆盖合成与真实样本，并提供车道边界、施工区边界、行驶轨迹选项的 3D 标注，以及闭环 CARLA 评估场景与 Bench2Drive 格式评估路线。
- 提出半自动化数据生成流程 WAVE，用于在虚拟与真实环境中构建该数据集。
- 提出 BoundaryFormer（BF），以 transformer 联合预测车道边界多项式、施工区边界多项式和行驶轨迹，并采用 slot attention 进行边界预测。
- 通过消融识别出使用边界 slot 特征的独立轨迹解码器对轨迹预测的关键作用，并据此发展出 BF++，集成度量地平面编码、带类型查询、长程点锚点、图像空间曲线细化与保守门控 LiDAR 融合。
- 在共同评估路线上报告 BF++ 以显著更小的模型规模取得高于 SimLingo 与 TransFuser++ 的 Driving Score，支持“联合预测车道边界、施工区边界与行驶轨迹”作为施工区安全自动驾驶的有前景方向。

### 局限性
- 摘要未提供足够信息说明真实世界样本的采集地区、传感器配置、标注质量控制或数据分布偏差。
- 摘要未提供足够信息说明 WAVE 流程的自动化程度边界、人工介入比例及其可扩展性。
- 摘要未提供足够信息说明 BF++ 各组件（如门控 LiDAR 融合、图像空间曲线细化）的独立消融结果。
- 摘要未提供足够信息说明失败案例、安全边界、极端天气或极端施工区布局下的表现。
- 摘要未提供足够信息说明与更多基线方法的对比，以及评估冻结所依据的具体标准。
- 摘要未提供足够信息说明模型的计算延迟、实时性与车载部署可行性。

### 阅读优先级
**高**。理由：该工作同时覆盖数据集、数据生成流程与端到端规划模型，且针对施工区这一地图先验易失效的安全关键场景；摘要给出了明确的闭环评估指标与模型规模对比，并以显著更小的参数量取得更高 Driving Score，对自动驾驶感知与规划交叉方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Work zones alter lane geometry through temporary traffic controls and closures that may be absent from on-board maps, challenging autonomous vehicle (AV) perception and planning. Generalization is also limited by scarce public datasets with structured geometric supervision. We present WorkZonePlan, a dataset comprising 149K+ synthetic and 5K+ real-world multimodal samples with 3D annotations for lane boundaries, work zone boundaries, and driving trajectory options. It also provides 76 closed-loop CARLA scenarios replayed under three weather conditions, yielding 228 Bench2Drive-format evaluation routes. We introduce WAVE (Work-zone-focused AV data generation in Virtual and rEal Environments), a semi-automated pipeline for creating the dataset, and BoundaryFormer (BF), a transformer-based model that jointly predicts lane and work zone boundary polynomials and driving trajectories. BF uses slot attention for boundary prediction. Ablations show that a separate trajectory decoder using boundary slot features substantially improves trajectory prediction over a slot-attention-only approach. Building on this finding, BF++ offers Camera and Camera+LiDAR variants with metric ground-plane encoding, typed boundary/trajectory queries, long-range point anchors, image-space curve refinement, and conservative gated LiDAR fusion. On the 211 routes common to all four models at the evaluation freeze, BF++-Camera and BF++-Camera+LiDAR achieve Driving Scores of 63.0 and 64.4, respectively, compared with 59.3 for SimLingo and 26.1 for TransFuser++ (TF++). BF++ is 40 times smaller than SimLingo and more than 10 times smaller than TF++, while achieving higher Driving Scores. These results support jointly predicting lane boundaries, work zone boundaries, and driving trajectories as a promising direction toward safer AV operation in work zones. Code and dataset: https://github.com/Nishad-Sahu/WZPlanner.

</details>

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

#### 2026-09-16 - 4D Radar Perception Algorithms for Autonomous Driving: A Review

**Authors:** Xumin Wu, Jun Zhou, Jilin Mei, Chen Min, Yu Hu
**Links:** [abs](https://arxiv.org/abs/2609.19216) - [pdf](https://arxiv.org/pdf/2609.19216)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** dynamic scene reconstruction, scene reconstruction, autonomous driving, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4D Radar Perception Algorithms for Autonomous Driving: A Review
- 作者：Xumin Wu, Jun Zhou, Jilin Mei, Chen Min, Yu Hu
- 出版日期：2026-09-16T12:46:07Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.19216

### 一句话总结
这是一篇围绕自动驾驶中 4D 毫米波雷达感知算法的综述，按感知任务与算法演进脉络，梳理从稀疏目标感知走向动态空间理解的研究进展。

### 研究问题
论文关注 4D 毫米波雷达感知算法在近年快速扩展背景下，如何按感知任务和算法演进进行系统组织与比较，包括信号处理、目标检测、语义分割、运动估计、占据预测和动态场景重建等方向。

### 核心思路/方法
综述以感知任务演变为组织主线：先介绍雷达基础、数据表示和质量增强方法，再回顾目标级感知、运动与定位、局部与稠密空间感知以及动态场景理解。在这些方向中，比较仅雷达学习、多模态融合、跨模态监督与知识蒸馏三类路线，并特别关注高度、多普勒测量和雷达物理先验在各任务中如何被利用。此外，总结现有数据集的任务覆盖、输入数据、标注和评估协议，并讨论共同挑战与未来方向。

### 主要贡献
- 以任务导向视角组织 4D 雷达感知领域，覆盖从目标级感知到动态空间理解的演进。
- 系统梳理雷达基础、数据表示与质量增强方法，以及目标级感知、运动与定位、局部与稠密空间感知、动态场景理解等任务方向。
- 对比仅雷达学习、多模态融合、跨模态监督与知识蒸馏，并关注高度、多普勒测量和雷达物理先验的利用方式。
- 总结现有数据集的任务覆盖、输入数据、标注与评估协议，明确不同研究方向的实证支持情况。
- 讨论 4D 雷达感知在自动驾驶中的共同挑战与未来方向。

### 局限性
摘要未提供足够信息说明该综述在文献筛选标准、覆盖时间范围、实验复现或定量比较等方面的具体局限。

### 阅读优先级
高。理由：该文是面向自动驾驶 4D 毫米波雷达感知算法的综述，任务覆盖面广，且按感知任务演进和多模态/跨模态方法进行比较，适合需要快速建立该方向整体图景的读者；但摘要未提供足够信息说明其具体实验细节与定量结论。

</details>

<details>
<summary>Abstract</summary>

Research on 4D millimeter-wave radar perception algorithms has flourished in recent years, extending from signal processing and object detection to semantic segmentation, motion estimation, occupancy prediction, and dynamic scene reconstruction. This review organizes the field according to the evolution of perception tasks and algorithms. It first introduces radar fundamentals, data representations, and quality-enhancement methods, and then reviews object-level perception, motion and localization, local and dense spatial perception, and dynamic scene understanding. Across these directions, we compare radar-only learning, multimodal fusion, and cross-modal supervision and knowledge distillation. Particular attention is paid to how elevation, Doppler measurements, and radar physical priors are exploited across tasks. We further summarize the task coverage, input data, annotations, and evaluation protocols of existing datasets, clarifying the empirical support for different research directions. Finally, we discuss the common challenges and future directions of 4D radar perception for autonomous driving. This review provides a task-oriented perspective on the transition from sparse object perception to dynamic spatial understanding.

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

#### 2026-09-16 - "Your Robot Was Trained on a Lie": Collision Mesh Poisoning Attacks on Robotic Manipulation

**Authors:** Gengyang Xu, Dongwei Xiao, Yiteng Peng, Yanbo Dai, Ruochen Zhou, Shing-Chi Cheung, Xiaoyu Ji, Wenyuan Xu, Shuai Wang
**Links:** [abs](https://arxiv.org/abs/2609.18122) - [pdf](https://arxiv.org/pdf/2609.18122)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题："Your Robot Was Trained on a Lie": Collision Mesh Poisoning Attacks on Robotic Manipulation
- 作者：Gengyang Xu, Dongwei Xiao, Yiteng Peng, Yanbo Dai, Ruochen Zhou, Shing-Chi Cheung, Xiaoyu Ji, Wenyuan Xu, Shuai Wang
- 出版日期：2026-09-16T04:58:17Z
- 分类：主分类 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.18122；PDF https://arxiv.org/pdf/2609.18122

### 一句话总结
论文揭示机器人仿真资产中视觉网格与碰撞网格的合法不一致（V–C Gap）可被利用，提出通过 3D 资产供应链仅篡改碰撞网格的 Collision Mesh Poisoning（CMP）攻击，使策略在仿真中表现正常却在真机上退化、失败或产生物理安全风险。

### 研究问题
学习驱动的机器人操作依赖仿真器在真实部署前进行策略训练与评估。仿真器中的 3D 资产包含两种分离的几何体：用于渲染的视觉网格与用于物理交互的碰撞网格。出于计算效率，碰撞网格被刻意设计为粗糙近似，不必与视觉网格几何一致，作者将这种合法且普遍存在的差异称为 Visual–Collision Gap（V–C Gap）。论文研究的问题是：这一差异是否构成新的攻击面，能否被用于对机器人操作策略实施投毒攻击。

### 核心思路/方法
作者提出 Collision Mesh Poisoning（CMP），据摘要称为首个通过 3D 资产供应链实施的针对机器人操作的投毒攻击。攻击者仅修改 3D 资产的碰撞网格，保持视觉网格及所有其他组件不变。使用被投毒资产训练和评估的策略在整个仿真过程中表现正常，但一旦部署到真实世界便会出现性能退化、失败或物理安全风险。由于当前资产审查实践覆盖恶意软件、版权和格式合规，但不覆盖视觉—碰撞一致性，被投毒资产可通过合法供应链渠道分发。论文还评估了若干防御手段，结果表明这些防御不足以抵御 CMP。

### 主要贡献
- 识别出 Visual–Collision Gap（V–C Gap）这一合法且普遍的视觉网格与碰撞网格差异，并将其揭示为新的实际攻击面。
- 提出 Collision Mesh Poisoning（CMP），据摘要为首个通过 3D 资产供应链投递、针对机器人操作的投毒攻击。
- 展示仅修改碰撞网格即可使策略在仿真中表现正常、在真实世界部署后退化、失败或产生物理安全风险。
- 指出当前资产审查不覆盖视觉—碰撞一致性，使投毒资产可经合法供应链渠道传播。
- 评估若干防御并显示其不足以防御 CMP，强调需要新的防御手段。

### 局限性
- 摘要未提供足够信息说明实验所用的具体仿真器、机器人平台、任务类型与数据集。
- 摘要未提供足够信息说明攻击成功率、性能退化幅度等定量结果。
- 摘要未提供足够信息说明所评估防御的具体种类与评估设置。
- 摘要未提供足够信息说明该攻击在真实供应链中的实际可行性验证细节。
- 摘要未提供足够信息说明碰撞网格修改的具体算法或约束条件。

### 阅读优先级
高。理由：该论文指出了一个此前未被审查覆盖的机器人仿真资产供应链攻击面，并声称是首个通过 3D 资产供应链实施的机器人操作投毒攻击，同时表明现有防御不足，对机器人学习系统的安全部署与资产审查流程具有直接警示意义。

</details>

<details>
<summary>Abstract</summary>

Learning-enabled robotic manipulation increasingly relies on robot simulators for policy training and evaluation before real-world deployment. Inside a simulator, a 3D asset contains two separate geometries: a visual mesh used for rendering and a collision mesh used for physical interaction. For computational efficiency, the collision mesh is deliberately a coarse approximation that need not have the same geometry as the visual mesh, a legitimate and pervasive discrepancy we call the Visual--Collision Gap (V--C Gap). We show that the V--C Gap opens a new and practical attack surface, and propose Collision Mesh Poisoning (CMP), the first poisoning attack against robotic manipulation delivered through the 3D asset supply chain. An attacker modifies only the collision mesh of a 3D asset, leaving the visual mesh and all other components unchanged. A policy trained and evaluated with the poisoned asset behaves normally throughout simulation, yet degrades, fails, or creates physical safety risks once deployed in the real world. Since current asset review practices cover malware, copyright, and format compliance, but not visual--collision consistency, poisoned assets can be distributed through legitimate supply chain channels. We evaluate several defenses and our results show that they are insufficient to defend against CMP, highlighting the need for new defenses.

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
