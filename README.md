# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：69
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 22
  - Embodied / Robotics / AR Applications: 20
  - Neural Scene Representations & Rendering: 15
  - Dynamic / 4D Reconstruction: 7
  - Geometry Foundation Models: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **评测基准与数据供给正在成为独立的研究贡献，而不再只是方法论文的附属品。** 本批论文中至少有三篇以“基准/数据集”为核心贡献：BhopalMLS 提供异构非规划城市的大规模 LiDAR 语义分割数据集；3DGS-VBench+ 构建 3DGS 视频质量评估的主观基准；Visibility-Aware Reference Generation 则直接针对植被密集场景缺乏几何真值的问题设计 LiDAR 参考生成流程。三者共同指向一个变化：当感知与重建模型本身趋于成熟后，**“如何可靠地测”成为瓶颈**，且评测对象从单帧/单视图扩展到序列、视频与跨区域迁移。

2. **前馈几何基础模型的“下游化”与“轻量化”改造密集出现。** DUNEDepth 将 3D 视觉基础模型混合适配到支气管镜深度与位姿估计；CoReMatch 用 Transformer + 循环坐标细化替代离散置信图匹配；SPA-Q 针对 Depth Anything 类 MDE 模型做低比特训练后量化；SR-DP 用冻结 VGGT 编码器提供多任务判别性视觉条件；Manifold Embedding 则把基础模型特征嵌入流形以正则化图像匹配。这些工作不追求新的大模型，而是**围绕已有基础模型解决适配、压缩、正则与任务迁移问题**，反映出“基础模型已就位，工程化与领域化是当前主战场”。

3. **动态/4D 与神经场景表示向“非理想采集条件”和“内容生产管线”两端延伸。** 一端是鲁棒性：Phase-DGS 处理未同步多视角视频，SettleSplat 处理单目在线序列中的视野内物体移动，IGSW 处理天气编辑图像的结构失真传播，EndoS3 处理内窥镜可变形场景；另一端是可用性：GSCV++ 用标准视频编解码器压缩 3DGS 序列，3DGS-VBench+ 建立 3DGS 视频质量评估。这说明 3DGS/动态重建的研究重心正从“能否重建”转向“**在真实采集缺陷下能否稳定重建，以及重建产物能否被存储、传输和评估**”。

4. **机器人/具身方向出现“物理属性估计 + 3D 世界模型”的耦合路线。** Physical Diffusion Policy 用 3DGS 与可微 MPM 耦合从视觉演示中估计材质参数，再注入 Mixture-of-Experts 扩散策略；Hybrid Particle-Voxel Dynamics 用粒子-体素自编码器加动作条件潜动力学，在统一 3D 表示下联合预测外观、几何与触觉。二者共同点是**把物理仿真或物理参数作为 3D 表示与策略/世界模型之间的中间层**，而非仅做视觉模仿。

5. **多会话、多传感器与在线标定的“长期运行可靠性”议题集中出现。** Sparse Anchors 处理环境变化下的多会话配准，MiCaDe 在线检测 LiDAR-相机外参漂移，Mamba3R 用固定容量状态记忆适配长序列流式重建，Do Pretrained Backbones Transfer 系统研究物理传感器模态下的预训练迁移。这批工作共同关注**部署后的漂移、变化与长时程退化**，而非静态离线精度。

#### 技术路线观察

- **几何基础模型方向**：路线分化明显。DUNEDepth 走“混合架构 + 合成监督/自监督联合微调”，强调领域数据（CT 派生虚拟视图）与基础模型组件的拼接；Manifold Embedding 走“函数映射 + 谱方法”路线，用 Galerkin 有限元从深度特征流形导出离散 LBO，试图以结构性正则替代启发式后处理；SR-DP 则把 VGGT 编码器冻结后仅做轻量适配，重心放在去噪器的谱路由分解上。三者对“基础模型该怎么用”给出了不同答案：**全量微调、结构正则、冻结特征+轻量适配**并存，尚未收敛。

- **3D/4D 重建方向**：传统多视图几何与神经表示的分工在变化。Visibility-Aware Reference Generation 仍以 SfM 与前馈模型为被评测对象，用 LiDAR 生成参考；Mamba3R 在预训练循环模型上做状态-记忆适配以控制长序列误差累积；CoReMatch 在匹配层用连续坐标细化替代离散网格。可以看到**几何精度问题正从“前端匹配/后端优化”转向“状态容量管理与连续表示”**。

- **神经场景表示方向**：3DGS 生态已形成“重建—压缩—评估”的完整链条。GSCV++ 关注编码器兼容性与低复杂度，IGSW 关注本征解耦以隔离天气编辑误差，SettleSplat 关注在线地图的瞬态/持久变化区分，EndoS3 关注实例级运动分解与语义节点分配。技术侧重点从外观拟合转向**属性解耦（反照率/辐照度、瞬态/持久、静态/动态实例）**，这是当前 3DGS 论文较一致的方法论取向。

- **机器人/AR 应用方向**：Embodied 类论文普遍把 3D 表示当作策略或世界模型的内部状态，而非仅作可视化产物。Physical Diffusion Policy 与 Hybrid Particle-Voxel Dynamics 都强调**统一 3D 表示支撑多模态（视觉+触觉）与几何一致渲染**；BhopalMLS 与 MiCaDe 则分别从数据与标定两侧支撑真实部署。整体看，应用侧对“物理正确性”和“长期可靠性”的要求正在反向塑造表示与评测设计。

#### 值得优先阅读的论文

1. **Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments**：它提出的 LDGVS 与 HPR 尺度选择针对的是 LiDAR 累积扫描可见性误差这一常被忽视的评测污染源，且同时覆盖前馈模型与传统 SfM 的零样本比较。对任何做户外重建评测的工作都有直接方法论参考价值。

2. **Phase-DGS: Phase-guided Dynamic Gaussian Splatting from Unsynchronized Multi-view Video**：未同步多视角是动态重建落地的高频障碍，用“语义相位”替代时间戳的思路具有较强迁移性，且摘要称可与多种 DGS 骨干集成，值得优先确认其相位估计的鲁棒性与失效条件。

3. **Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation**：把粒子-体素混合表示用于动作条件世界模型并联合预测触觉，是具身方向中较完整的“表示—动力学—多模态”闭环设计，适合作为理解 3D 世界模型技术栈的入口。

4. **SPA-Q: Structure-Preserving Adaptive Post-Training Quantization for Monocular Depth Estimation**：低比特 PTQ 对 MDE 基础模型的部署是现实痛点，其指出的“独立量化 Q/K 破坏注意力图”与“逐层误差累积”两个问题具体且可验证，方法组件（APC + 通道级分布对齐）也较易复现比较。

5. **Do Pretrained Backbones Transfer to Physical Sensors? A Systematic Study of Multimodal Initialization Across the Sensor Stack**：2.82M 图像、16 数据集、物理与模型导出模态混合的系统研究，对多传感器预训练选型有直接指导意义；其关于模态稀疏性对 MultiMAE 类方法影响的结论值得全文核对。

#### 可能的研究机会

- **评测侧的“参考质量”本身可被建模与优化**：Visibility-Aware Reference Generation 的 LDGVS 只解决点级可见性过滤，尚未看到对参考深度图不确定性的端到端传播建模。可将参考生成的不确定性纳入评测指标置信区间，或与 3DGS-VBench+ 这类主观基准结合，形成“参考质量—客观指标—主观感知”的联合分析。

- **3DGS 压缩与质量评估的闭环**：GSCV++ 优化率失真与编解码速度，3DGS-VBench+ 提供多维度主观评分与 RR/NR 客观模型。二者之间

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-05T15:39:33-05:00
**Total number of papers:** 71
**Number of papers added in the latest update:** 14
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

#### 2026-11-04 - Trainspotting: Learning Object-Centric 3D Reconstruction from Found Photos

**Authors:** Hanyu Chen, Noah Snavely
**Links:** [abs](https://arxiv.org/abs/2611.06849) - [pdf](https://arxiv.org/pdf/2611.06849)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, feedforward reconstruction, 3D reconstruction, multi-view stereo, stereo depth

<details>
<summary>Abstract</summary>

State-of-the-art feedforward reconstruction models perform poorly on in-the-wild object-centric photo collections. They are trained largely on single-session object captures whose images vary in viewpoint while the object and its environment remain nearly fixed. Public photo archives contain a different form of multi-view data. They hold found photos of the same object or design: photos taken independently by many people across years, environments, cameras, and sometimes physical units. In this work, we introduce Trainspotting, a dataset of 12,068 objects and 311,886 photos from Wikimedia Commons. We reconstruct each object to recover camera poses, multi-view stereo depth, and object masks. We categorize the objects into three regimes: objects fixed at one site, objects that move between sites, and designs shared by many physical units. Evaluating recent feedforward reconstruction models on Trainspotting shows that they fail most severely in the last two regimes. Fine-tuning VGGT-$Ω$ on Trainspotting significantly improves camera pose, depth, and 3D geometry on held-out objects. We observe similar improvements on the independent NAVI in-the-wild benchmark, which contains photos of each object in different environments. Performance on conventional benchmarks remains largely unchanged.

</details>

#### 2026-11-04 - Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation

**Authors:** Sihang Chen, Chen Ye, Wei Chen, Xiaohan Lei, Zhipeng Tang, Sha Zhang, Yuan Zhang, Zixuan Chen, Jiajun Deng, Houqiang Li, Yanyong Zhang
**Links:** [abs](https://arxiv.org/abs/2611.06475) - [pdf](https://arxiv.org/pdf/2611.06475)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, manipulation

<details>
<summary>Abstract</summary>

In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable. However, existing benchmarks provide limited evaluation of such memory-dependent decision-making in mobile manipulation. To address this gap, we introduce RoboCasa-Mem, a new benchmark comprising nine mobile manipulation tasks that require agents to use interaction history at key decision points. Specifically, the tasks are grouped into two categories of memory: One is environment memory, which captures spatial locations, object attributes, and object relationships. The other is process memory, which captures single-task progress and multi-task scheduling. Particularly, we introduce Behavior-Conditioned Evaluation. For tasks with multiple valid execution paths, instead of fixing a single target or trajectory, the evaluator derives later task constraints from the robot's earlier actions. This allows us to evaluate whether later behavior is consistent with the robot's own interaction history while reducing shortcuts based on fixed target assignments. We provide 1,800 successful demonstrations for policy training. We also develop a baseline on our benchmark, namely Hierarchical Memory-Augmented Policy(HMAP). Its high-level planner uses structured entity and process memories to generate subtasks. Its low-level VLA controller uses subgoal-conditioned queries to incorporate VGGT-Omega geometry into action generation. Together, RoboCasa-Mem and HMAP baseline support systematic evaluation of memory-dependent behavior and the development of memory-aware mobile manipulation policies.

</details>

#### 2026-11-04 - Scale Anchoring via Implicit Semantics and Sequence-Consistent Loop Closure for VGGT-Based SLAM

**Authors:** Ziyi Jin, Kangjin Yu, Beichen Wang, Can Jiang, Zhongpu Xia, Jie Xu
**Links:** [abs](https://arxiv.org/abs/2611.06308) - [pdf](https://arxiv.org/pdf/2611.06308)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, SLAM, camera calibration

<details>
<summary>Abstract</summary>

Feed-forward geometric foundation models enable dense monocular reconstruction without requiring camera calibration, but independently reconstructed submaps can accumulate scale drift, and even a valid revisit can yield an inconsistent cross-submap measurement. We extend VGGT-SLAM 2.0 with fixed-root scale anchoring and short-sequence-assisted direct loop connections. SALAD selects an image pair between the initial submap and each eligible new submap; joint VGGT inference then uses learned implicit semantic-geometric cues to supply a scale-only anchor while preserving the original overlap chain. For loop closure, neighboring image pairs support a consistency check and translation-scale alignment. Each accepted candidate contributes one robust Sim(3) factor between existing center-frame nodes, without an auxiliary loop submap. A 17-sequence comparison lowers mean Sim(3) ATE on nine TUM sequences from 0.1018 to 0.0451 m relative to the VGGT-SLAM 2.0 baseline. Anchoring improves all seven no-loop module ablations. On three Clio scenes, a fixed-loop comparison favors the direct connection pipeline over the tested auxiliary-submap pipeline. A separate candidate audit exposes additional rejections of visually overlapping pairs by the short-sequence check. These comparisons distinguish the gains from long-range scale anchoring and loop connection choices from the limitations of candidate verification.

</details>

#### 2026-11-04 - METRIC-GS: Selective Metric-Scale Estimation for 3D Gaussian Splatting

**Authors:** Sooyeun Yang, Jongseong Brad Choi
**Links:** [abs](https://arxiv.org/abs/2611.06020) - [pdf](https://arxiv.org/pdf/2611.06020)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** MASt3R, metric depth, structure from motion, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, AR

<details>
<summary>Abstract</summary>

A 3D Gaussian Splatting (3DGS) reconstruction inherits arbitrary units from structure-from-motion, so it cannot be measured or used to place AR content until someone supplies a scale. Both standard recipes are fragile on real captures: on five indoor scenes with tape-measured ceilings, a quantile floor-to-ceiling heuristic errs by 27% and metric-depth alignment by 35-71% across three networks. We present METRIC-GS, a selective scale estimator for real indoor photographs: it reads the scale off the reconstruction's own semantic content and, just as importantly, refuses when the evidence is thin. A frozen 2D teacher labels Gaussians by visibility-aware voting; instance-level size priors for architectural and furniture classes (doors, tables, the floor-to-ceiling gap) are fused by a robust maximum-likelihood step; and an inlier-mass test turns thin evidence into an explicit abstention that doubles as a router to a heavyweight metric model. On 47 ScanNet++ scenes with laser ground truth, with a configuration frozen before public evaluation, the estimator alone cuts the heuristic's mean error from 21.1% to 16.6% (9.3% on the 28 scenes it acts on) at ~11 s per scene. MASt3R remains the more accurate standalone estimator (9.9%), but routing only our refusals to it matches running it everywhere with 60% fewer invocations; this selective hybrid is the configuration we advocate. Visibility-aware voting raises the scenes the estimator can act on from 16 to 28 at unchanged deployed accuracy. Applied unchanged to 13 phone and drone captures of our own, on which MASt3R fails its own registration gate 12 times, the system improves all five captures it acts on and degrades none. We also report that a current feed-forward metric model scores 2.3% on a benchmark inside its training mixture and 28-35% on captures it has never seen: a published metric-scale number is a best case, not a deployment estimate.

</details>

#### 2026-11-03 - Manifold Embedding of Deep Image Features for Image Matching via Neural Adjoint Maps

**Authors:** Nafie El Amrani, Moritz Heep, Florian Bernard
**Links:** [abs](https://arxiv.org/abs/2611.05083) - [pdf](https://arxiv.org/pdf/2611.05083)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** dense correspondence, image matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Manifold Embedding of Deep Image Features for Image Matching via Neural Adjoint Maps
- 作者：Nafie El Amrani, Moritz Heep, Florian Bernard
- 出版日期：2026-11-03T15:42:20Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.05083 ；PDF https://arxiv.org/pdf/2611.05083

### 一句话总结
论文提出利用神经伴随映射与基于深度图像特征流形嵌入构建的离散 Laplace-Beltrami 算子，将函数映射框架用于图像匹配，以缓解基础模型特征最近邻匹配的噪声与正则不足问题。

### 研究问题
论文关注真实图像中相似类别不同物体实例之间的语义对应估计，尤其是稠密对应场景。摘要指出，基础模型虽推动了困难图像对应问题的解决，但相关方法往往正则化不足；例如使用基础模型特征的常见最近邻匹配常产生噪声对应，在稠密对应中尤为突出。

### 核心思路/方法
论文通过函数映射处理图像匹配。函数映射因利用高效低维线性表示的光谱形式而在 3D 形状匹配中流行，但其要求定义域（本文中为矩形图像网格）具备有信息量且非平凡的几何结构。为给图像定义有意义的流形结构，作者使用有限元中的 Galerkin 方法，基于深度图像特征的流形嵌入推导离散 Laplace-Beltrami 算子（LBO）。此外，论文利用神经伴随映射来表示非线性映射。

### 主要贡献
- 将函数映射框架引入图像匹配，并针对图像网格缺乏非平凡几何的问题，通过深度图像特征的流形嵌入定义流形结构。
- 使用 Galerkin 有限元方法从该嵌入推导离散 Laplace-Beltrami 算子。
- 利用神经伴随映射表示非线性映射。
- 摘要称该方法在多个真实图像稠密对应基准上取得零样本图像对应方法的新 state of the art，并公开代码。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算开销、对特征质量或网格结构的敏感性，也未给出实验设置、基准名称与定量结果细节。因此无法基于给定摘要可靠总结其局限性。

### 阅读优先级
中。理由：论文涉及函数映射、流形嵌入、神经伴随映射与零样本稠密图像对应，主题与几何基础模型及多视图几何相关；摘要声称达到新 SOTA 并公开代码，具有一定参考价值。但摘要未提供实验细节与局限分析，是否需要精读取决于读者对函数映射用于图像匹配这一技术路线的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Estimating semantic correspondences between different object instances of similar categories in real-world images is a fundamental challenge in computer vision. While the recent progress in foundation models has significantly advanced solutions for such difficult image correspondence problems, respective methods are often insufficiently regularised. For example, common nearest-neighbour matching with foundation model features often results in noisy correspondences, which is particularly prominent when solving for dense correspondences. In this work, we tackle image matching via functional maps, which have been popularised for 3D shape matching due to their powerful spectral formalism utilising an efficient low-dimensional linear representation. However, functional maps require that domains (in our cases the rectangular image grids) are equipped with an informative and non-trivial geometry. To define a meaningful manifold structure for images, we use Galerkin's method from finite elements to derive a discrete Laplace-Beltrami operator (LBO) based on a manifold embedding of deep image features. Further, we leverage a neural adjoint map that allows to represent non-linear mappings. We demonstrate that our method sets the new state of the art among zero-shot image correspondence methods on multiple dense correspondence benchmarks of real-world images. Our code is publicly available: https://github.com/NafieAmrani/NAMI

</details>

#### 2026-11-03 - Spectrally Routed Diffusion Policy for Multi-Task Robotic Manipulation

**Authors:** Mingcong Li, Yihan Zhou, Jiayu Qu, Xueyang Guo, Yilin Mo
**Links:** [abs](https://arxiv.org/abs/2611.04477) - [pdf](https://arxiv.org/pdf/2611.04477)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spectrally Routed Diffusion Policy for Multi-Task Robotic Manipulation
- 作者：Mingcong Li, Yihan Zhou, Jiayu Qu, Xueyang Guo, Yilin Mo
- 出版日期：2026-11-03T08:09:15Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.04477 ；PDF https://arxiv.org/pdf/2611.04477

### 一句话总结
论文提出 SR-DP，通过增强多任务共享空间下的视觉条件判别性，并用谱路由分解去噪器线性层，缓解多任务联合训练中的梯度破坏性干扰，从而缩小多任务扩散策略与单任务专家之间的差距。

### 研究问题
摘要指出，基于扩散的策略在单任务机器人操作上表现较强，但单个模型在多个任务上联合训练时，持续落后于用相同示范训练的单任务专家。作者聚焦两个挑战：一是扩散策略常用的卷积编码器产生的视觉条件判别性不足；二是来自不兼容动作模式的梯度会沿相同方向更新共享去噪器的稠密参数，从而在联合训练中造成破坏性干扰。

### 核心思路/方法
摘要给出的方法包含两部分：
1. 视觉条件构建：使用冻结的 VGGT 编码器，并配合空间压缩适配器，生成紧凑的多尺度语义-几何 token，为共享工作空间中的任务提供更具任务判别性的视觉条件。
2. 去噪器参数组织：先以标准扩散策略训练去噪器，再对选定线性层做 SVD 分解，得到由正交秩一专家组成的冻结基，并通过谱路由与 Householder 输入旋转进行适配。

摘要将方法描述为两阶段流程：Stage 1 为标准扩散策略训练，Stage 2 为上述谱路由适配。

### 主要贡献
摘要明确提到的贡献包括：
- 提出 SR-DP（Spectrally Routed Diffusion Policy），同时针对视觉条件判别性不足和联合训练中稠密参数更新的破坏性干扰问题。
- 使用冻结 VGGT 编码器与空间压缩适配器生成多尺度语义-几何 token，以改善共享工作空间多任务场景下的视觉条件。
- 通过 SVD 将选定线性层分解为冻结的正交秩一专家基，并结合谱路由与 Householder 输入旋转进行适配。
- 在六个 RoboTwin 任务上，SR-DP 平均成功率为 68.4%，比多任务 VO-DP 高 21.8 个百分点，比最强单任务基线高 3.8 个百分点。
- 在四个真实世界双臂任务上，Stage 2 平均成功率为 43.0%，比 Stage 1 提升 19.0 个百分点。

### 局限性
- 摘要未提供足够信息说明计算开销、训练时间、参数量或推理效率。
- 摘要未提供足够信息说明六个 RoboTwin 任务与四个真实双臂任务的具体任务定义、数据规模与评估协议细节。
- 摘要未提供足够信息说明消融实验的完整设置，例如 VGGT 编码器、空间压缩适配器、SVD 秩一专家、谱路由与 Householder 旋转各自的独立贡献。
- 摘要未提供足够信息说明方法在更多任务数量、不同工作空间或非双臂平台上的泛化表现。
- 摘要未提供足够信息说明失败案例、鲁棒性测试与安全性评估。

### 阅读优先级
中。理由：论文针对多任务扩散策略中视觉条件判别性与梯度干扰两个明确问题，给出了结构化的方法组合，并在仿真与真实双臂任务上报告了成功率提升；如果关注多任务机器人操作、扩散策略或参数高效适配，具有较高参考价值。但摘要未展开消融、效率与泛化细节，是否值得深入精读需结合全文实验部分进一步判断。

</details>

<details>
<summary>Abstract</summary>

Diffusion-based policies have achieved strong performance on single-task robotic manipulation. However, a single model trained jointly on multiple tasks consistently underperforms the per-task specialists trained on the same demonstrations. We focus on two challenges. First, the convolutional encoders commonly used in diffusion-based policies produce visual conditions that are not discriminative enough. Second, gradients from incompatible action modes update the shared denoiser's dense parameters along the same directions, causing destructive interference during joint training. To address both, we propose SR-DP (Spectrally Routed Diffusion Policy). A frozen VGGT encoder with a spatial-compression adapter produces compact multi-scale semantic-geometric tokens, a task-discriminative visual condition for tasks that share a workspace. We first train the denoiser as a standard diffusion policy, then decompose selected linear layers by SVD into a frozen basis of orthogonal rank-one experts, adapted through spectral routing and Householder input rotations. On six RoboTwin tasks, SR-DP averages a 68.4% success rate, surpassing multi-task VO-DP by 21.8 points and the strongest per-task baseline by 3.8 points. On four real-world bimanual tasks, Stage 2 reaches a 43.0% average success rate and improves over Stage 1 by 19.0 points.

</details>

#### 2026-11-02 - DUNEDepth: Bronchoscopic Depth and Pose Estimation via Hybrid Adaptation of a 3D-Vision Foundation Model

**Authors:** Qi Chang, Austin Kao, Ange Lou, William E. Higgins
**Links:** [abs](https://arxiv.org/abs/2611.04025) - [pdf](https://arxiv.org/pdf/2611.04025)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** MASt3R, motion trajectories, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DUNEDepth: Bronchoscopic Depth and Pose Estimation via Hybrid Adaptation of a 3D-Vision Foundation Model
- 作者：Qi Chang, Austin Kao, Ange Lou, William E. Higgins
- 出版日期：2026-11-02T22:13:02Z
- 分类：primary: Geometry Foundation Models；secondary: 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.04025) / [PDF](https://arxiv.org/pdf/2611.04025)

### 一句话总结
DUNEDepth 通过混合适配 3D 视觉基础模型，从支气管镜视频中估计深度与相机运动，以支持将检查视频与术前胸部 CT 建立关联。

### 研究问题
论文关注支气管镜导航与计算机辅助诊断在早期肺癌检测中的应用背景。其关键问题是：如何从患者的支气管镜气道检查视频中准确推导支气管镜深度和相机运动，并将该视频与术前 3D 胸部 CT 扫描有效关联。摘要明确指出，从检查视频中推导这些关联仍是一个开放问题。

### 核心思路/方法
论文提出 DUNEDepth，一种混合架构，包含：
- 共享的 DUNE ViT 编码器；
- 孪生 MASt3R 交叉注意力解码器结构；
- 包含 MASt3R 与 Reloc3r 模型元素的预测头。

为适配该应用，论文采用集成的混合“合成监督/自监督”训练策略，训练数据来源包括支气管镜视频和由 CT 衍生的虚拟支气管镜视图。摘要还说明，该方法建立在近期提出的 3D 视觉基础模型之上。

### 主要贡献
- 提出 DUNEDepth 混合架构，用于支气管镜场景下的深度与相机运动估计。
- 将 DUNE ViT 编码器、孪生 MASt3R 交叉注意力解码器以及融合 MASt3R 与 Reloc3r 元素的预测头结合。
- 提出合成监督与自监督结合的混合训练策略，并利用支气管镜视频与 CT 衍生虚拟支气管镜视图进行微调。
- 摘要称，基于支气管镜视频序列的实验表明，DUNEDepth 在深度信息和相机运动轨迹推导上比此前提出的自监督方法更准确。

### 局限性
- 摘要未提供足够信息说明具体数据集规模、患者数量、数据采集条件或外部验证情况。
- 摘要未提供足够信息说明定量评价指标、误差定义、统计显著性或以 CT 关联为最终目标的端到端评估结果。
- 摘要未提供足够信息说明方法在不同支气管镜设备、不同气道区域、不同视频质量或真实临床部署条件下的鲁棒性。
- 摘要未提供足够信息说明合成监督与自监督各部分的具体权重、消融结果及失败案例。
- 摘要未提供足够信息说明计算开销、实时性或在临床工作流中的可用性。

### 阅读优先级
中。理由：该论文聚焦支气管镜视频中的深度与相机运动估计，并借助 3D 视觉基础模型进行混合适配，问题定义和架构思路与支气管镜导航、CT-视频关联及多视图几何相关。若读者关注内窥镜视觉、基础模型迁移或医学场景中的深度/位姿估计，具有参考价值；但摘要未给出充分的实验细节、临床验证规模和实时性信息，是否值得深入阅读取决于对支气管镜导航与 3D 基础模型适配方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

State-of-the-art bronchoscopy guidance systems and computer-aided diagnosis methods have emerged as important tools for early lung cancer detection. Effective use of these tools depends on being able to accurately link a patient's bronchoscopic airway exam video to their pre-operative 3D chest CT scan. Unfortunately, the derivation of such links, which include bronchoscope depth and camera motion, from the exam video remains an open problem. Building on recently proposed 3D-vision foundation models, we propose DUNEDepth, a hybrid architecture that combines a shared DUNE ViT encoder, a twin MASt3R cross-attention decoder structure, and a prediction head that includes elements of the MASt3R and Reloc3r models. To fine-tune the architecture to our application, we utilize an integrated hybrid synthetic-supervised/self-supervised training strategy that draws on both bronchoscopic video and CT-derived virtual bronchoscopic views. Experiments drawing on bronchoscopic video sequences demonstrate that DUNEDepth more accurately derives depth information and camera motion trajectories than previously proposed self-supervised methods.

</details>

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

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-03 - Phase-DGS: Phase-guided Dynamic Gaussian Splatting from Unsynchronized Multi-view Video

**Authors:** Hosung Jeon, Jun Young Jeong, Sangwoon Kwak, Joonsoo Kim, Sangmin Kim, Jaesik Park, Won-Sik Cheong, Hyon-Gon Choo
**Links:** [abs](https://arxiv.org/abs/2611.04666) - [pdf](https://arxiv.org/pdf/2611.04666)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, scene reconstruction, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Phase-DGS: Phase-guided Dynamic Gaussian Splatting from Unsynchronized Multi-view Video
- 作者：Hosung Jeon, Jun Young Jeong, Sangwoon Kwak, Joonsoo Kim, Sangmin Kim, Jaesik Park, Won-Sik Cheong, Hyon-Gon Choo
- 出版日期：2026-11-03T10:51:33Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.04666) / [PDF](https://arxiv.org/pdf/2611.04666)

### 一句话总结
论文提出 Phase-DGS，用“语义相位”替代传统时间戳，为未同步多视角视频中的每一帧建立跨相机的时空对应关系，从而支持动态高斯泼溅重建。

### 研究问题
动态高斯泼溅（DGS）的时空场景重建通常假设所有相机在时间上完美同步，但这一假设在实践中很少成立。工业级同步依赖昂贵的专用硬件和复杂设置；音频对齐、几何匹配、位姿跟踪等数据驱动替代方案又受限于特定环境或场景假设。论文要解决的问题是：在多相机时间不同步的情况下，如何建立帧间的时空对应关系并完成动态场景重建。

### 核心思路/方法
Phase-DGS 不再依赖传统时间戳，而是为每一帧引入一个“语义相位”，表示该帧在底层运动周期中所处的固有状态。这样，只要不同相机拍到的是同一运动状态，这些帧就共享同一相位，与由哪台相机拍摄、何时拍摄无关，从而自然建立未同步相机之间的时空对应。摘要还指出，该方法可与现有 DGS 骨干（包括 RealTime-4DGS 和 FreeTimeGS）无缝集成。

### 主要贡献
- 提出以语义相位替代时间戳的 Phase-DGS 框架，用于未同步多视角视频的动态场景重建。
- 利用同一运动状态共享相位的性质，在未同步相机之间建立时空对应关系。
- 在时间偏移、丢帧和相机冻结条件下进行验证，相较基线最高取得 +8.5 dB 的 PSNR 提升。
- 可与 RealTime-4DGS、FreeTimeGS 等现有 DGS 骨干集成。

### 局限性
- 摘要未提供足够信息说明“语义相位”的具体估计方式、是否需要额外监督或先验。
- 摘要未提供足够信息说明方法对非周期性运动、复杂多物体运动或大幅遮挡等情形的适用性。
- 摘要未提供足够信息说明实验数据集规模、相机数量、基线配置及 +8.5 dB 提升的具体实验条件。
- 摘要未提供足够信息说明计算开销、实时性与工程部署成本。

### 阅读优先级
中。理由：论文聚焦动态高斯泼溅中一个实际且关键的问题——多相机时间不同步，并提出用语义相位建立跨相机对应的思路，且报告了较明显的 PSNR 提升并支持与现有骨干集成；但摘要未给出相位估计细节、适用边界和完整实验条件，需阅读全文后才能判断其通用性与可靠性。

</details>

<details>
<summary>Abstract</summary>

Spatiotemporal scene reconstruction with Dynamic Gaussian Splatting (DGS) fundamentally depends on perfect temporal synchronization across all cameras, an assumption rarely achievable in practice. Industry-standard synchronization requires expensive specialized hardware and complex setup, while data-driven alternatives including audio-based alignment, geometry matching, and pose tracking remain limited by restrictive environmental or scene-specific assumptions. To overcome these limitations, we propose Phase-DGS, a framework that replaces conventional timestamps with a semantic phase representing each frame's inherent state within the underlying motion cycle. Frames capturing the same motion state share the same phase regardless of which camera records them or when, naturally establishing spatiotemporal correspondence across unsynchronized cameras. We validate Phase-DGS under temporal offsets, frame drops, and camera freezes, achieving up to +8.5 dB PSNR improvement over baselines while enabling seamless integration with existing DGS backbones including RealTime-4DGS and FreeTimeGS.

</details>

#### 2026-11-03 - IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting

**Authors:** Zhongquan Wang, Long Cao, Peijia Xie, Senlei Ma, Jie Li, Guofa Li
**Links:** [abs](https://arxiv.org/abs/2611.04374) - [pdf](https://arxiv.org/pdf/2611.04374)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** dynamic Gaussian, 4D Gaussian, scene reconstruction, Gaussian Splatting, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting
- 作者：Zhongquan Wang, Long Cao, Peijia Xie, Senlei Ma, Jie Li, Guofa Li
- 出版日期：2026-11-03T06:02:54Z
- 分类：Dynamic / 4D Reconstruction；3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.04374 ；PDF https://arxiv.org/pdf/2611.04374 ；项目页 https://akaxi6.github.io/IGSW/

### 一句话总结
IGSW 是一个两阶段框架，结合本征解耦的 4D 高斯场景建模与结构保持的天气精炼，用于多天气城市场景重建，以缓解天气编辑图像中的结构失真向 4D 重建传播的问题。

### 研究问题
论文关注高保真 4D 场景的多天气编辑与重建，以支持自动驾驶的端到端训练和闭环仿真。摘要指出，将生成式图像编辑与动态高斯表示结合可实现多天气场景重建，但天气编辑图像常包含结构失真；若直接拟合其外观，可能把教师图像中的错误传播到重建的 4D 场景中，损害原始场景结构和时间连续性。因此，核心问题是：在多天气编辑条件下，如何既获得目标天气外观，又保持场景结构与时间连续性。

### 核心思路/方法
IGSW 采用两阶段框架：

1. **Stage I：本征解耦的 4D 高斯场景建模**
   - 将背景高斯外观分解为：
     - 天气共享的反照率（albedo）与法线（normals）；
     - 天气特定的辐照度（irradiance）与残差（residuals）。
   - 使用基于扩散的图像编辑模型生成天气教师图像，并使用基于扩散的逆渲染器估计本征图。
   - 这些教师图像与本征图提供特征级软监督，用于稳定结构和光照变化。

2. **Stage II：结构保持的天气精炼**
   - 引入结构保持门控（structure-preservation gate），结合语义冲突与跨天气本征差异，抑制不可靠的教师区域。
   - 使用逐高斯天气传输变量和目标天气分支，在本征解耦场景上增强期望的天气外观。

### 主要贡献
- 提出 IGSW 两阶段框架，将本征解耦的 4D 高斯场景建模与结构保持的天气精炼结合。
- 在 Stage I 中，将背景高斯外观解耦为天气共享的反照率与法线，以及天气特定的辐照度与残差，并利用天气教师图像和本征图进行特征级软监督。
- 在 Stage II 中，提出结构保持门控，结合语义冲突与跨天气本征差异抑制不可靠教师区域；并通过逐高斯天气传输变量和目标天气分支增强目标天气外观。
- 摘要称在 nuScenes 和 Waymo 上，IGSW 在对比方法中取得最高的内容相似度和语义一致性，以及最低的时间误差，同时保留明显的天气相关光照与氛围。
- 提供项目页面。

### 局限性
- 摘要未提供足够信息说明方法在不同天气类型、极端天气或复杂动态场景下的具体适用范围与失败情况。
- 摘要未提供足够信息说明两阶段框架的计算开销、训练时间、推理效率或实时性。
- 摘要未提供足够信息说明对扩散式天气教师图像编辑模型和扩散式逆渲染器的依赖程度及其误差影响。
- 摘要未提供足够信息给出 nuScenes 与 Waymo 上的完整定量指标、消融实验细节和基线设置。
- 摘要未提供足够信息说明结构保持门控中语义冲突与跨天气本征差异的具体度量方式及阈值敏感性。

### 阅读优先级
**高**。理由：该论文直接面向动态/4D 重建与多天气城市场景重建，摘要明确涉及自动驾驶仿真应用，并提出两阶段方法处理天气编辑图像结构失真传播这一关键问题；若读者关注 4D 高斯、多天气场景编辑、结构保持监督或自动驾驶闭环仿真，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

High-fidelity weather editing of 4D scenes can support end-to-end training and closed-loop simulation for autonomous driving. Combining generative image editing with dynamic Gaussian representations enables multi-weather scene reconstruction, but weather-edited images often contain structural distortions. Directly fitting their appearance may propagate errors from teacher images into the reconstructed 4D scene, compromising the original scene structure and temporal continuity. To address these challenges, we propose IGSW, a two-stage framework that combines intrinsic-decoupled 4D Gaussian scene modeling with structure-preserving weather refinement. In Stage I, background Gaussian appearance is decomposed into weather-shared albedo and normals and weather-specific irradiance and residuals. Weather teacher images generated by a diffusion-based image editing model and intrinsic maps estimated by a diffusion-based inverse renderer provide feature-level soft supervision for stable structure and illumination changes. In Stage II, a structure-preservation gate combines semantic conflicts with cross-weather intrinsic discrepancies to suppress unreliable teacher regions. Per-Gaussian weather transport variables and target-weather branches then strengthen the desired weather appearance over the intrinsic-decoupled scene. Experiments on nuScenes and Waymo show that IGSW achieves the highest content similarity and semantic consistency and the lowest temporal error among the compared methods, while retaining pronounced weather-dependent illumination and atmosphere. The project page is available at https://akaxi6.github.io/IGSW/ .

</details>

#### 2026-11-02 - FlowRig: Unified Skeleton Generation for 3D and 4D Meshes via Flow Matching

**Authors:** Fengzhi Guo, Nate Morrill, Shiqi Li, Cheng Zhang
**Links:** [abs](https://arxiv.org/abs/2611.03775) - [pdf](https://arxiv.org/pdf/2611.03775)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, dynamic 4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FlowRig: Unified Skeleton Generation for 3D and 4D Meshes via Flow Matching
- 作者：Fengzhi Guo, Nate Morrill, Shiqi Li, Cheng Zhang
- 出版日期：2026-11-02T18:39:17Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.03775)｜[PDF](https://arxiv.org/pdf/2611.03775)

### 一句话总结
提出一个基于 flow matching 的统一骨架生成框架，旨在用单次前馈同时处理静态 3D 网格和动态 4D 网格的自动绑定问题（摘要中框架名称表述与标题不一致，详见局限性）。

### 研究问题
自动骨架绑定对静态 3D 网格动画和动态 4D 网格动画都是基础任务，但现有方法缺乏统一的前馈解决方案：静态 3D 绑定方法质量较高，却对骨骼数量控制有限，逐帧套用到动态网格上时会出现时序不稳定；已有 4D 方法通常依赖昂贵的逐序列优化。

### 核心思路/方法
- 构建模板无关、数据高效的统一 3D/4D 骨架生成框架，基于 flow matching。
- 对整段序列做单次前馈，生成时序对齐的骨架，同时可直接处理单网格 3D 绑定。
- 支持显式骨骼数量控制、用于候选选择的不确定性估计，以及基于掩码的插值、预测与回溯。
- 针对配对 4D 绑定数据有限的问题，采用课程式训练：先从大规模 3D 绑定数据初始化，再适配中等规模 4D 网格-骨架数据。

### 主要贡献
- 提出面向 3D 与 4D 网格的统一前馈骨架生成框架，避免逐帧绑定带来的时序不稳定和逐序列优化开销。
- 引入骨骼数量显式控制、不确定性估计与掩码式插值/预测/回溯等能力（具体实现细节摘要未提供足够信息）。
- 设计从 3D 数据到 4D 数据的课程式训练策略，以缓解配对 4D 绑定数据不足。
- 摘要称实验在静态 3D 绑定（骨骼复杂度可控）以及 4D 重建与预测（高质量、时序一致）上取得较强表现。

### 局限性
- 摘要中框架名称写作 “MoTWorld”，与标题 “FlowRig” 不一致，摘要未提供足够信息说明二者关系。
- 摘要未提供具体数据集、评价指标、定量结果、对比基线、运行时间或失败案例，相关实验细节摘要未提供足够信息。
- 摘要未说明骨骼数量控制的实现方式、不确定性估计的校准情况，以及掩码式预测/回溯的适用边界，摘要未提供足够信息。
- 课程式训练对 3D 与 4D 数据分布差异的敏感性与泛化能力，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对 3D/4D 统一自动绑定的明确空白，提出单次前馈、骨骼数可控与时序一致的思路，问题定位清晰且具应用价值；但当前仅有摘要，缺少定量实验与实现细节，且存在框架命名不一致，需阅读全文后再评估其实际效果与可复现性。

</details>

<details>
<summary>Abstract</summary>

Automatic rigging is a fundamental task for both static 3D and dynamic 4D mesh animation, yet existing methods do not provide a unified feedforward solution for these two settings. While static 3D riggers achieve strong quality, they often provide limited control over bone count and become temporally unstable when applied frame by frame to dynamic meshes. Existing 4D methods, in contrast, typically rely on expensive per-sequence optimization. We propose MoTWorld, a template-free, data-efficient framework for unified 3D and 4D skeleton generation. Built on flow matching, MoTWorld generates temporally aligned skeletons for an entire sequence in a single feedforward pass, while naturally handling single-mesh 3D rigging. The model further supports explicit skeleton-count control, uncertainty estimation for candidate selection, and masking-based interpolation, forecasting, and backcasting. To address limited paired 4D rigging data, we adopt a curriculum that initializes from large-scale 3D rigging data and adapts to mid-scale 4D mesh-skeleton data. Experiments show that MoTWorld achieves strong static 3D rigging performance with controllable bone complexity, as well as high-quality and temporally consistent 4D reconstruction and prediction results.

</details>

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

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-04 - SpikePose: Lightweight Video Human Pose Estimation

**Authors:** Yunhao Huang, Kaushik Bhargav Sivangi, Tianyi Yu, Fani Deligianni
**Links:** [abs](https://arxiv.org/abs/2611.06594) - [pdf](https://arxiv.org/pdf/2611.06594)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Efficient video human pose estimation must balance localisation accuracy, motion quality, and energy cost. We present SpikePose, a lightweight video pose estimator that pairs a frame-reset, single-step spiking encoder with motion-aligned heatmap memory (MAM). The encoder supplies per-frame spatial evidence, while MAM estimates joint displacement, aligns historical heatmaps, and adaptively fuses them with current predictions. By confining temporal reasoning to a compact, lightweight module outside the spiking backbone, SpikePose helps bridge the gap between spiking and classical Artificial Neural Networks (ANN) on large-scale, non-event-driven video tasks. We evaluate spatial accuracy, motion errors, and estimated arithmetic energy on MPII and a fixed NTU60 Cross-Subject subset. Against the architecture-matched ANN with MAM, SpikePose cuts estimated arithmetic energy by 91.4% at a cost of just 1.12 points in head-bone-normalised PCK at 0.5 threshold (PCK_HB(0.5)). Within SpikePose, adding MAM reduces velocity and acceleration errors by 28.13% and 31.46% while slightly improving localisation, at a cost of only 0.003M parameters and 0.0023 analytical GFLOPs per frame. Code will be released on GitHub upon acceptance.

</details>

#### 2026-11-04 - UniLoop: Unified Loop Closure Detection from Retrieval to Geometric Verification and Relative Pose Estimation

**Authors:** Jingwen Yu, Pengyu Wang, Jin Wu, Weinan Chen, Ping Tan, Hong Zhang
**Links:** [abs](https://arxiv.org/abs/2611.06378) - [pdf](https://arxiv.org/pdf/2611.06378)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** geometric foundation model, pose estimation

<details>
<summary>Abstract</summary>

Loop closure detection conventionally cascades separate models for global retrieval, geometric verification, and relative pose estimation, leading to redundant computation and disconnected visual representations. We propose UniLoop, a unified framework that reuses the hierarchical representations of the pretrained geometric foundation model throughout this pipeline. A shared image encoder produces features for compact global descriptors; the same features are passed to the cross-view decoder for pairwise verification; and the original geometric predictions provide relative camera constraints for pose-graph optimization. Experiments on place recognition, loop verification, and relative pose estimation show that UniLoop improves loop-closure robustness and accuracy while reducing redundant backbone computation relative to modular pipelines. UniLoop achieves the best Recall@10 on MSLS (96.6) and Pitts30k (99.3) among the compared methods, while its verification branch reaches 95.63 AP and 96.29 ROC-AUC, surpassing the existing geometric verification baselines.

</details>

#### 2026-11-04 - Quo Vadis, Driving Scene Reconstruction? Occlusion-Aware Gaussian Densification

**Authors:** Dung Do Tien, Kien Nguyen Do Trung, Kiet Dang Vu, Trung Thai Tran, Duc Dung Nguyen
**Links:** [abs](https://arxiv.org/abs/2611.06273) - [pdf](https://arxiv.org/pdf/2611.06273)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting, driving scene, mapping

<details>
<summary>Abstract</summary>

While recent feed-forward 3D Gaussian Splatting methods enable efficient driving-scene reconstruction from surround-view images, their reliance on a single observation fundamentally hinders novel-view synthesis. Regions occluded in the input can become visible from novel viewpoints, leaving the reconstructed Gaussians under-constrained and incomplete. Moving beyond image-space inpainting for rendered views, we introduce OccSplat, a feed-forward framework whose core contribution is Occlusion-Aware Gaussian Densification, explicitly targeting missing scene geometry rather than missing pixels. By predicting new Gaussian primitives for unsupported regions, OccSplat completes the scene directly in the 3D representation. Specifically, OccSplat first identifies occluded regions that lack Gaussian support through Gaussian Occlusion Mapping. Gaussian Occlusion Completion then generates new primitives for these regions. The predicted primitives are integrated into the original representation to improve novel-view synthesis while retaining feed-forward inference without per-scene optimization. Experiments on the nuScenes benchmark demonstrate that OccSplat improves on the compared methods and yields particularly large gains in occluded regions, leading to more accurate and visually coherent driving-scene reconstruction.

</details>

#### 2026-11-04 - 3D Pose Estimation in Projection Space via Pixel-level Visible Light Communication

**Authors:** Michikuni Eguchi, Takefumi Hiraki
**Links:** [abs](https://arxiv.org/abs/2611.06121) - [pdf](https://arxiv.org/pdf/2611.06121)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, augmented reality

<details>
<summary>Abstract</summary>

Projector-based augmented reality enables natural interaction between users and devices by overlaying digital information onto the physical world through projected imagery. A key technical requirement of such systems is accurate positional alignment between the projector and the devices. Pixel-level Visible Light Communication (PVLC) achieves this alignment without external sensing infrastructure by embedding invisible spatial codes into each projected pixel through high-speed brightness modulation that preserves image quality. However, the information that PVLC transmits is inherently planar. PVLC has therefore been limited to devices moving on a flat surface and cannot estimate the 3D pose of devices in three-dimensional space, such as aerial robots. To extend PVLC-based pose estimation to three dimensions, we formulate it as a Perspective-n-Point (PnP) problem. The 2D pixel positions that four coplanar photosensors on the device receive via PVLC serve as the image points, and their known 3D layout provides the object points. Experiments show that the proposed system estimates 3D pose with a latency of approximately 8~ms and a 3D position RMSE of 19.2~mm after Kalman filtering. These results confirm the first realization of real-time 3D pose estimation coordinated with high-quality projected image content without external sensing infrastructure.

</details>

#### 2026-11-03 - Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments

**Authors:** Zhipeng Zhong, Matthew Coombes, Cunjia Liu
**Links:** [abs](https://arxiv.org/abs/2611.05361) - [pdf](https://arxiv.org/pdf/2611.05361)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, SfM, depth estimation, surface reconstruction, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments
- 作者：Zhipeng Zhong, Matthew Coombes, Cunjia Liu
- 出版日期：2026-11-03T18:54:52Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[abstract_url](https://arxiv.org/abs/2611.05361) / [pdf_url](https://arxiv.org/pdf/2611.05361)

### 一句话总结
论文提出一种复用现有多传感器定位数据集中相机图像、LiDAR 扫描和参考位姿的 LiDAR 参考生成流程，并引入 LDGVS 进行可见性过滤与 HPR 尺度选择，用于在植被密集户外环境中评测视觉深度估计与 3D 重建方法。

### 研究问题
植被密集的户外环境中，视觉 3D 重建与深度估计的可靠评测受限于几何真值数据稀缺以及完整扫描测量的成本。论文关注如何生成可用于评测的参考数据，并比较前馈视觉几何模型、传统 SfM 方法在该场景下的零样本表现。

### 核心思路/方法
- 构建基于 LiDAR 的参考生成流程，复用现有多传感器定位数据集中的相机图像、LiDAR 扫描和参考位姿，生成逐视角深度图与可见参考点云。
- 针对累积 LiDAR 扫描中的可见性误差，提出 LargeDepth-Gap Visibility Score（LDGVS），用于逐点可见性过滤以及 Hidden Point Removal（HPR）中的自动尺度选择。
- 在 TartanAirV2 与 TartanGround 上，将 HPR 与 LDGVS 过滤组合与 Poisson 表面重建进行比较。
- 将流程应用于 BotanicGarden 数据集，系统比较深度估计与 3D 重建方法。

### 主要贡献
- 提出面向植被密集户外环境的 LiDAR 参考生成流程，用于评测前馈视觉几何模型与传统 SfM 方法的零样本性能。
- 引入 LDGVS 以处理累积 LiDAR 扫描中的可见性误差，并用于逐点可见性过滤和 HPR 自动尺度选择。
- 摘要报告：在 TartanAirV2 和 TartanGround 上，与适合完整扫描调查的 Poisson 表面重建相比，HPR 与 LDGVS 过滤组合在相近绝对相对误差下保留约三倍点密度。
- 在 BotanicGarden 上应用该流程进行比较，指出前馈方法能高效产生稠密深度预测，但其 3D 重建可能包含重复结构；传统 SfM 通常产生更连贯的几何，但重建仍稀疏且在困难植被场景中更易失败。
- 摘要称将发布基准工具包和数据集。

### 局限性
- 摘要未提供足够信息说明 LDGVS 的具体定义、阈值设置或参数敏感性。
- 摘要未提供足够信息说明实验的完整定量指标、误差分布和统计显著性。
- 摘要未提供足够信息说明 BotanicGarden 比较中各类方法的具体配置与训练/零样本设置细节。
- 摘要未提供足够信息说明方法在更广泛植被类型、传感器配置或天气条件下的泛化能力。
- 摘要未提供足够信息说明所发布工具包与数据集的具体范围、许可和使用方式。

### 阅读优先级
中。理由：论文主题聚焦植被密集环境下的 3D 重建评测与参考数据生成，方法点（LDGVS、HPR 尺度选择）和基准比较具有明确相关性；但摘要仅给出有限实验结论，若研究兴趣集中在可见性过滤、LiDAR 参考生成或植被场景基准评测，则值得进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Reliable evaluation of visual 3D reconstruction and depth estimation in vegetation-rich outdoor environments is limited by the scarcity of geometric ground-truth data and the cost of complete scanner surveys. We present a LiDARbased reference-generation pipeline for evaluating the zero-shot performance of feed-forward visual-geometry models alongside conventional structure-from-motion (SfM) methods. The pipeline reuses camera images, LiDAR scans, and reference poses from existing multi-sensor localization datasets to generate per-view depth maps and visible reference point clouds. To address visibility errors in accumulated LiDAR scans, we introduce the LargeDepth-Gap Visibility Score (LDGVS) for point-wise visibility filtering and automatic scale selection in Hidden Point Removal(HPR). Experiments on TartanAirV2 and TartanGround show that, compared with Poisson surface reconstruction, which is an approach suited to completed scan surveys, the combined HPR and LDGVS filtering retains approximately three times the point density at comparable absolute relative error. We also apply the pipeline to the BotanicGarden dataset to systematically compare depth estimation and 3D reconstruction methods. Feedforward methods produce dense depth predictions efficiently, but their 3D reconstructions can contain duplicated structures. Conventional SfM generally produces more coherent geometry, but its reconstructions remain sparse and more prone to failure in challenging vegetated scenes. The benchmark toolkit and datasets will be released.

</details>

#### 2026-11-03 - Sparse Anchors for Visual Multi-Session Registration in Changing Environments

**Authors:** Yunus Talha Erzurumlu, Niklas Trekel, Saurabh Gupta, Nico Koltermann, Olga Vysotska, Jens Behley, Louis Wiesmann, Cyrill Stachniss
**Links:** [abs](https://arxiv.org/abs/2611.05084) - [pdf](https://arxiv.org/pdf/2611.05084)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, feature matching, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sparse Anchors for Visual Multi-Session Registration in Changing Environments
- 作者：Yunus Talha Erzurumlu, Niklas Trekel, Saurabh Gupta, Nico Koltermann, Olga Vysotska, Jens Behley, Louis Wiesmann, Cyrill Stachniss
- 出版日期：2026-11-03T15:43:03Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.05084) / [PDF](https://arxiv.org/pdf/2611.05084)

### 一句话总结
该论文提出利用稀疏但可靠的绝对位姿锚点，并结合会话内相对位姿约束，将新采集的查询会话轨迹配准到已有参考地图，以应对环境显著变化下的视觉多会话定位问题。

### 研究问题
论文关注变化环境中的视觉多会话配准：机器人重复监测同一环境时，需要在多次访问之间实现定位，即使环境发生变化。摘要指出，环境变化可能大幅减少持续可见的视觉内容，重复结构也可能导致错误的跨会话对应。在视觉和结构显著变化下，跨会话定位可能只对轨迹的一部分可行。因此，核心问题是如何在仅有部分可靠跨会话对应的情况下，仍将完整查询轨迹配准到参考地图。

### 核心思路/方法
论文依赖一组稀疏的可靠绝对位姿约束，并将其与会话内相对位姿信息结合，以完成完整轨迹到参考地图的配准。具体流程包括：
1. 通过视觉位置识别、局部特征匹配和几何验证，估计绝对对齐假设；
2. 使用序列一致性拒绝与共同查询—参考对齐不一致的假设，保留剩余位姿作为绝对锚点；
3. 通过针对高斯特征场的特征度量对齐对锚点进行细化；
4. 将细化后的锚点与会话内相对位姿约束结合，在鲁棒位姿图优化中完成轨迹配准。

### 主要贡献
- 提出一种面向变化环境的视觉多会话配准方法，使用稀疏可靠绝对锚点结合会话内相对位姿约束来配准完整轨迹。
- 设计了两阶段策略：先通过视觉位置识别、局部特征匹配、几何验证和序列一致性筛选获得绝对锚点，再通过高斯特征场上的特征度量对齐细化锚点。
- 在 HILTI26 建筑工地数据集的 15 个跨会话实验中评估，报告在 1 米内达到 94.4% 召回率、5 米内达到 100.0% 召回率，并称优于独立图像定位和独立重建 Structure-from-Motion 几何的直接配准。

### 局限性
- 摘要未提供足够信息说明方法在实时性、计算开销或大规模地图扩展方面的表现。
- 摘要未提供足够信息说明方法对锚点数量、序列一致性阈值、特征场表示等关键参数的敏感性。
- 摘要未提供足够信息说明在完全无可靠跨会话对应或极端场景变化下的失败模式。
- 摘要未提供足够信息说明除 HILTI26 之外其他数据集上的泛化表现。
- 摘要未提供足够信息说明与更多基线方法的全面比较细节。

### 阅读优先级
高。理由：该论文直接针对变化环境中的多会话视觉配准这一具有实际机器人监测价值的问题，方法思路清晰，且摘要报告了在挑战性建筑工地数据集上的定量结果；若读者关注 3D 重建、多视图几何、跨会话定位或位姿图优化，该文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Repeated robotic monitoring requires localization across visits to the same environment, even if the environment changes. Such changes can substantially reduce persistent visual content, and repetitive structures can lead to incorrect cross-session correspondences. In this paper, we address visual multi-session registration of a new data recording (the query session) to a previously reconstructed reference map. Under substantial visual and structural changes, cross-session localization may be possible only for parts of the trajectory. In our approach, we therefore rely on a sparse set of reliable absolute pose constraints and combine them with within-session relative-pose information to register the complete trajectory to the reference map. We first estimate absolute alignment hypotheses through visual place recognition, local feature matching, and geometric verification. We then use sequence consensus to reject hypotheses that are inconsistent with a common query-to-reference alignment and retain the remaining poses as absolute anchors. These anchors are refined through featuremetric alignment against a Gaussian feature field and combined with within-session relative-pose constraints in a robust pose-graph optimization. We evaluate our approach on 15 cross-session experiments from the challenging HILTI26 construction-site dataset, covering substantial scene changes and difficult-to-match environments. Our method achieves 94.4% recall within 1m and 100.0% within 5m, outperforming independent image localization, which peaks at 65.3% and 70.7%, respectively, as well as direct registration of independently reconstructed Structure-from-Motion geometry. Our results show that sparse, reliable absolute anchors can provide accurate and complete trajectory registration even when reliable cross-session correspondences are available only for part of the query session.

</details>

#### 2026-11-03 - SPA-Q: Structure-Preserving Adaptive Post-Training Quantization for Monocular Depth Estimation

**Authors:** Jaemin Choi, Jincheol Yang, Nahyun Lim, Yun-Seong Jeong, Matti Zinke, Hyunwoo Yu, Suk-Ju Kang
**Links:** [abs](https://arxiv.org/abs/2611.04491) - [pdf](https://arxiv.org/pdf/2611.04491)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SPA-Q: Structure-Preserving Adaptive Post-Training Quantization for Monocular Depth Estimation
- 作者：Jaemin Choi, Jincheol Yang, Nahyun Lim, Yun-Seong Jeong, Matti Zinke, Hyunwoo Yu, Suk-Ju Kang
- 出版日期：2026-11-03T08:20:52Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类信息
- 链接：摘要页 https://arxiv.org/abs/2611.04491 ；PDF https://arxiv.org/pdf/2611.04491

### 一句话总结
论文提出面向单目深度估计（MDE）的结构保持自适应训练后量化框架 SPA-Q，用注意力保持校准与通道级分布对齐缓解 Depth Anything 类模型在低比特 PTQ 下的注意力结构破坏与逐层误差累积问题。

### 研究问题
摘要指出，以 Depth Anything 为代表的 MDE 基础模型虽泛化强，但 Transformer 架构带来高计算与内存开销，部署困难；PTQ 是实用压缩方案，但低比特 PTQ 对 MDE 仍具挑战。作者将 PTQ 应用于 Depth Anything 时识别出两个关键问题：
1. 分别最小化 query 与 key 投影的量化误差，无法保持二者交互形成的注意力图；
2. 量化误差跨层累积，导致中间特征分布发生偏移。

### 核心思路/方法
SPA-Q 是一个结构保持的自适应 PTQ 框架，包含两个主要组件：
1. **Attention-Preserving Calibration (APC，注意力保持校准）**：通过匹配全精度注意力分布来确定 query 与 key 的量化参数，而非独立最小化二者各自的量化误差。
2. **Channel-Wise Distribution Alignment (CWDA，通道级分布对齐）**：学习通道级仿射变换，以缓解量化引起的分布偏移；训练完成后，所学参数被吸收进权重。

摘要未提供 APC 与 CWDA 的具体实现细节、校准数据规模、训练流程或超参数设置。

### 主要贡献
- 识别并形式化了将 PTQ 用于 Depth Anything 时的两个关键问题：注意力图未被保持、逐层量化误差累积导致中间特征分布偏移。
- 提出 SPA-Q 框架，以 APC 保持注意力结构，以 CWDA 对齐通道分布，并将 CWDA 学习参数在训练后吸收进权重。
- 实验结果显示，在 4-bit 量化下，SPA-Q 持续优于现有 PTQ 方法；在 NYUv2 与 KITTI 数据集上平均取得 AbsRel 降低 25.9%、δ₁ 提升 17.3%。

摘要未提供具体对比方法清单、模型规模、硬件平台或推理加速数据。

### 局限性
- 摘要仅报告 4-bit 量化下的结果，未说明 2-bit、3-bit、8-bit 或混合精度设置的表现。
- 摘要未提供 APC 与 CWDA 的计算开销、校准时间、额外内存占用，也未给出参数吸收后的实际部署收益数据。
- 摘要未说明方法对其他 MDE 架构（非 Depth Anything 类 Transformer）的适用性。
- 摘要未提供消融实验细节、失败案例或对极端场景的鲁棒性分析。
- 摘要未提供训练/校准数据规模、是否依赖标注数据等实现条件。
- 以上均需注意：摘要未提供足够信息。

### 阅读优先级
**中**。理由：该论文聚焦 MDE 基础模型的低比特 PTQ 部署，问题定位明确（注意力结构保持与跨层分布偏移），方法组件清晰，且摘要给出 NYUv2/KITTI 上 4-bit 的量化指标提升，对模型压缩与高效部署方向具有参考价值。但摘要未披露实现细节、开销与更广泛比特设置下的表现，若读者关注具体工程落地或非 Depth Anything 架构的迁移，需进一步阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation (MDE) has advanced rapidly with the emergence of foundation models such as Depth Anything. Their transformer-based architectures provide strong generalization across diverse scenes and domains, but also incur high computational and memory cost, making efficient deployment challenging. Post-Training Quantization (PTQ) provides an efficient and practical solution for model compression, yet low-bit PTQ remains challenging for MDE models. When applying PTQ to Depth Anything, we identify two key challenges: (i) independently minimizing the quantization error of the query and key projections fails to preserve the attention maps induced by their interaction, and (ii) quantization errors accumulate across layers, resulting in intermediate feature distribution shifts. To address these issues, we propose SPA-Q, a Structure-Preserving Adaptive PTQ framework for MDE, consisting of two main components. First, Attention-Preserving Calibration (APC) determines query and key quantization parameters by matching the full-precision attention distribution. Second, Channel-Wise Distribution Alignment (CWDA) learns channel-wise affine transformations to mitigate quantization-induced distribution shifts, and the learned parameters are absorbed into the weights after training. Experimental results show that SPA-Q consistently outperforms existing PTQ methods under 4-bit quantization, achieving an average 25.9% reduction in AbsRel and a 17.3% improvement in $δ_1$ across NYUv2 and KITTI datasets.

</details>

#### 2026-11-03 - Mamba3R: Fixed-Capacity Selective State Memory for Long-Sequence 3D Reconstruction

**Authors:** Zhenxiang Xiong, Tianchen Deng, Nailin Wang, Lei Zhao, Guole Shen, Weidong Che
**Links:** [abs](https://arxiv.org/abs/2611.04221) - [pdf](https://arxiv.org/pdf/2611.04221)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mamba3R: Fixed-Capacity Selective State Memory for Long-Sequence 3D Reconstruction
- 作者：Zhenxiang Xiong, Tianchen Deng, Nailin Wang, Lei Zhao, Guole Shen, Weidong Che
- 出版日期：2026-11-03T03:03:35Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.04221) / [PDF](https://arxiv.org/pdf/2611.04221)

### 一句话总结
Mamba3R 提出一种容量固定的选择性状态记忆适配器，在不更新预训练循环模型主干与任务头的前提下，增强长序列流式三维重建的轨迹与几何精度。

### 研究问题
流式三维重建需要在固定 GPU 预算下对长输入保持几何质量。预训练循环模型虽提供有界状态，但冻结主干会固定其已学习的状态-观测交互，缺少可训练的适配路径。论文关注如何在有限且不变的记忆容量下改善长序列重建表现。

### 核心思路/方法
- 设计联合的状态-记忆适配器，提供可训练适配路径，同时不更新主干或任务头。
- 采用选择性状态空间混合器，联合变换原生状态特征与固定容量辅助记忆。
- 通过显式读、写路径跨帧传递信息，并用分解的反馈路径调节新增记忆向模型反馈的内容。
- 仅训练 1.28 百万适配器参数；在共享周期重置协议下与循环基线比较。
- 摘要提到进行匹配比较以支持混合算子选择和辅助记忆跨帧传递的有效性。

### 主要贡献
- 提出 Mamba3R 状态-记忆适配器，在冻结主干与任务头条件下实现可训练适配。
- 在公共室内、室外数据集及机器人记录轨迹上，相比循环基线降低轨迹误差，并提升累积表面与深度精度，摘要称某一指标最高提升 40%。
- 匹配比较支持混合算子的选择以及辅助记忆跨帧携带的作用。
- 报告分配内存保持不变；帧数从一千增至两千时，吞吐变化至多 1.4%。
- 离线回放记录轨迹时，RTX 4060 在 5.1 GiB 内使用同一检查点平均 11.7 FPS，平均吞吐覆盖 10 Hz 传感器速率。

### 局限性
- 摘要未提供足够信息说明方法在非室内/室外场景或更极端长序列下的泛化表现。
- 摘要未提供足够信息说明 1.28M 适配器参数之外的计算开销细节及训练成本。
- 摘要未提供足够信息说明与更多类型基线（如非循环方法）的系统比较。
- 摘要未提供足够信息说明失败案例、误差分布及对传感器噪声的鲁棒性。
- 摘要未提供足够信息说明“共享周期重置协议”的具体设定及其对结论的影响范围。

### 阅读优先级
高。理由：论文直接面向固定 GPU 预算下的长序列流式三维重建，提出仅训练少量参数的适配方案，并给出轨迹、表面、深度、内存与吞吐等多方面摘要级结果；若关注长序列重建的效率与精度平衡，该工作具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Streaming 3D reconstruction must maintain geometric quality over long inputs within a fixed GPU budget. A pretrained recurrent model provides bounded state, but freezing its backbone also fixes its learned state-observation interactions. We introduce Mamba3R, a jointly designed state-memory adapter that provides a trainable adaptation path without updating the backbone or task heads. A selective state-space mixer jointly transforms native state features and a fixed-capacity auxiliary memory, explicit read and write paths carry information across frames, and a decomposed feedback path regulates what the added memory feeds back. Only 1.28 million adapter parameters are trained. Under a shared periodic-reset protocol, it lowers trajectory error and improves accumulated surface and depth accuracy over recurrent baselines on public indoor and outdoor datasets and robot-recorded traversals, gaining up to 40 percent on one metric. Matched comparisons support both the choice of the mixing operator and the utility of carrying the auxiliary memory across frames. Allocated memory remains unchanged and throughput moves by at most 1.4 percent from one to two thousand frames. Replaying its recorded traversals offline, the platform's RTX 4060 averages 11.7 frames per second within 5.1 GiB with the same checkpoint, a mean throughput covering the 10 Hz sensor rate.

</details>

#### 2026-11-02 - Do Pretrained Backbones Transfer to Physical Sensors? A Systematic Study of Multimodal Initialization Across the Sensor Stack

**Authors:** Fabio Montello, Ronja Güldenring, Lucas Mogensen Sandby, Christoffer Koo Øhrstrøm, Lazaros Nalpantidis
**Links:** [abs](https://arxiv.org/abs/2611.04034) - [pdf](https://arxiv.org/pdf/2611.04034)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** stereo depth, dense reconstruction, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Do Pretrained Backbones Transfer to Physical Sensors? A Systematic Study of Multimodal Initialization Across the Sensor Stack
- 作者：Fabio Montello, Ronja Güldenring, Lucas Mogensen Sandby, Christoffer Koo Øhrstrøm, Lazaros Nalpantidis
- 出版日期：2026-11-02T22:29:36Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.04034；PDF https://arxiv.org/pdf/2611.04034

### 一句话总结
论文系统研究预训练骨干网络向真实物理传感器多模态场景的迁移表现，并通过构建大规模多传感器自动驾驶图像集合与改进 MultiMAE 预训练，比较域内预训练与常见现成预训练骨干在下游传感器融合任务上的效果。

### 研究问题
论文指出，多传感器计算机视觉中从预训练骨干迁移学习已成常见做法，但仍有两个开放问题：哪些预训练权重最适合迁移到多传感器设置；域内预训练能否优于现成方案。摘要还指出，MultiMAE 等方法依赖稠密、模型导出的模态，而真实物理传感器应用中，聚合多样公开数据集进行大规模预训练会天然引入模态稀疏性，因此这些方法能否稳健迁移到真实物理传感器场景尚不清楚。

### 核心思路/方法
- 构建一个多传感器自动驾驶图像集合，包含来自 16 个公开数据集的 2.82M 张图像，覆盖物理硬件模态（RGB、LWIR、NIR、Event）和模型导出模态（Stereo Depth、Segmentation）。
- 基于 MultiMAE 方法在该集合上进行域内预训练。
- 调整 MultiMAE 的损失公式以适应稀疏样本。
- 研究强制编码器瓶颈对模态对齐的影响，以及针对稠密重建的额外损失（SSIM 和 FFT）的影响。
- 在下游传感器融合任务上，系统比较常见预训练骨干（ViT、MAE、DINO、MultiMAE）。

### 主要贡献
- 构建并整理了一个大规模多传感器自动驾驶图像集合，用于域内预训练研究，规模为 2.82M 张图像、16 个公开数据集，涵盖物理硬件模态与模型导出模态。
- 针对真实物理传感器场景中的模态稀疏问题，调整 MultiMAE 损失公式，并考察编码器瓶颈与稠密重建额外损失（SSIM、FFT）的作用。
- 系统比较 ViT、MAE、DINO、MultiMAE 等预训练骨干在多传感器下游融合任务上的迁移表现。
- 摘要给出的发现是：MultiMAE 是出乎意料的强现成基线，即使对从未见过的模态也能有效迁移；而作者的目标性修改在多传感器迁移和整体稳健性上带来增量但一致的改进。

### 局限性
- 摘要未提供足够信息说明下游传感器融合任务的具体类型、评价指标和定量结果。
- 摘要未提供足够信息说明 16 个公开数据集的具体构成、各模态样本数量分布及模态稀疏程度。
- 摘要未提供足够信息说明编码器瓶颈和 SSIM/FFT 额外损失各自的消融细节与单独影响。
- 摘要未提供足够信息说明与 ViT、MAE、DINO、MultiMAE 比较时的具体预训练权重来源、训练配置和计算成本。
- 摘要未提供足够信息说明该研究结论对其他传感器栈、其他自动驾驶数据集或其他任务领域的泛化边界。

### 阅读优先级
中。理由：论文主题涉及多传感器预训练迁移、物理传感器模态和 MultiMAE 改进，对多模态计算机视觉与传感器融合研究有直接相关性；摘要给出了清晰的问题设定、数据规模和比较对象，并报告了“MultiMAE 强现成基线”和“目标修改带来一致增量改进”的结论。但摘要未提供具体任务、指标和定量结果，是否高优先级阅读取决于读者对传感器融合下游任务或 MultiMAE 域内预训练细节的兴趣。

</details>

<details>
<summary>Abstract</summary>

Transfer learning from pretrained backbones has become standard practice in multi-sensor computer vision---yet two questions remain open: which pretrained weights transfer best to multi-sensor setups, and can in-domain pretraining outperform off-the-shelf solutions? Frameworks like MultiMAE demonstrate the utility of masked autoencoding in a multi-modal context, but rely entirely on dense, model-derived modalities. It is unclear how robustly these methods translate to real-world applications that use physical sensors, where the aggregation of diverse public datasets for large-scale pretraining inherently introduces modality sparsity. To investigate this systematically, we curate a multi-sensor autonomous driving collection of $2.82M$ images from 16 publicly available datasets, incorporating both physical hardware modalities (RGB, LWIR, NIR, Event) and model-derived modalities (Stereo Depth, Segmentation). We use this collection for in-domain pretraining based on the MultiMAE approach. We adapt MultiMAE's loss formulation to accommodate sparse samples, and study the effect of an enforced encoder bottleneck for modality alignment and of additional losses specific to dense reconstruction (SSIM and FFT). We then systematically compare against common pretrained backbones (ViT, MAE, DINO and MultiMAE) across downstream sensor fusion tasks. We find that MultiMAE is a surprisingly strong out-of-the-box baseline, transferring effectively even to modalities it has never seen, while our targeted modifications yield incremental but consistent improvements on multi-sensor transfer and overall robustness.

</details>

#### 2026-11-02 - CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching

**Authors:** Robert J. Wang, Charles Ling, Boyu Wang
**Links:** [abs](https://arxiv.org/abs/2611.03932) - [pdf](https://arxiv.org/pdf/2611.03932)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, feature matching, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching
- 作者：Robert J. Wang, Charles Ling, Boyu Wang
- 出版日期：2026-11-02T20:36:30Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2611.03932

### 一句话总结
CoReMatch 提出一种在连续坐标空间中循环细化对应关系的特征匹配框架，旨在兼顾机器人感知任务中的匹配精度与实时效率。

### 研究问题
现有半稠密匹配器在固定网格上预测置信度，导致对应关系被限制在预定义位置；若要实现精确定位，需要高分辨率网格，计算成本较高。论文关注如何避免离散置信图预测的上述限制，并提升实时特征匹配的精度与效率。

### 核心思路/方法
CoReMatch 将对应关系直接在连续坐标空间中细化，而不是预测离散置信图。该框架通过跨迭代传播信息逐步改进对应估计：在粗阶段，使用 Deep Aggregated Transformer 捕获全局上下文并迭代更新对应坐标；随后由轻量回归头进一步锐化定位。

### 主要贡献
- 提出 CoReMatch，一种循环连续坐标细化框架，用于实时机器人特征匹配。
- 在连续坐标空间中细化对应关系，避免固定网格对对应位置的限制。
- 在粗阶段结合 Deep Aggregated Transformer 进行全局上下文建模与坐标迭代更新，并用轻量回归头进一步精化定位。
- 摘要称在室内和室外基准上取得精度与效率的较好平衡，精度优于 Efficient LoFTR，且在嵌入式边缘硬件上运行速度超过其 10 倍。

### 局限性
摘要未提供足够信息。未说明具体数据集、评价指标、网络结构细节、训练策略、计算资源、失败场景或泛化能力等。

### 阅读优先级
中。理由：论文主题与实时机器人特征匹配、连续坐标细化相关，摘要给出了明确的问题动机和效率优势；但摘要未提供充分实验细节与局限性信息，需阅读全文后才能判断其方法可靠性与适用边界。

</details>

<details>
<summary>Abstract</summary>

Feature matching underpins many robotic perception tasks, including visual localization, mapping, SLAM, and autonomous navigation. Existing semi-dense matchers predict confidence on fixed grids, limiting correspondences to predefined locations and requiring costly high-resolution grids for precise localization. We present CoReMatch (Coordinate Refinement Match), a recurrent framework that refines correspondences directly in continuous coordinate space rather than predicting discrete confidence maps. CoReMatch progressively improves correspondence estimates by propagating information across iterations. At the coarse stage, a Deep Aggregated Transformer captures global context and iteratively updates correspondence coordinates, while a lightweight regression head further sharpens their localization. Experiments on indoor and outdoor benchmarks show that CoReMatch strikes a strong balance between accuracy and efficiency, outperforming Efficient LoFTR in accuracy while running more than 10x faster on embedded edge hardware. These results demonstrate that recurrent coordinate refinement offers an efficient and scalable approach to real-time feature matching for robotic perception.

</details>

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

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-04 - BudgetSplat: Budget-Controllable Generalizable Gaussian Splatting

**Authors:** Yuxi Hu, Jun Zhang, Wei Mao, Yuchen Rao, Friedrich Fraundorfer
**Links:** [abs](https://arxiv.org/abs/2611.06593) - [pdf](https://arxiv.org/pdf/2611.06593)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting enables efficient generalizable novel view synthesis, but existing pixel-aligned methods often generate highly redundant Gaussian primitives, causing the final representation size and rendering cost to grow rapidly with image resolution and the number of input views. We propose BudgetSplat, a budget-controllable feed-forward framework that adapts the final Gaussian representation to a user-specified preservation ratio. Rather than treating compaction as simple importance ranking, we formulate it as a joint problem of importance estimation, spatial coverage, and cross-view redundancy. A single trained model supports varying numbers of context views and multiple test-time budgets without per-budget retraining or per-scene compression. To realize this formulation, Intra-Cross Mask Supervision provides structure-, coverage-, and redundancy-aware guidance for learning Gaussian importance, while budget-conditioned feature modulation adapts Gaussian opacity and attributes to the requested preservation ratio. Coverage-Aware Budget Selection further combines patch-wise pre-selection, view-wise opacity ranking, and 3D redundancy suppression to construct compact yet spatially distributed Gaussian representations. Experiments on indoor reconstruction and cross-dataset generalization demonstrate consistent quality--size trade-offs across different input view counts and preservation ratios, substantially reducing final representation storage and rendering cost while preserving rendering quality.

</details>

#### 2026-11-04 - TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics

**Authors:** Shu'ang Sun, Yibo Qiu, Haoliang Ye, Zan Huang, Ao Tian, Kan Ding, Ronald Xu, Mingzhai Sun
**Links:** [abs](https://arxiv.org/abs/2611.06442) - [pdf](https://arxiv.org/pdf/2611.06442)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, robotics, manipulation, digital twin, simulation

<details>
<summary>Abstract</summary>

Online reinforcement learning offers an effective approach to precise laboratory manipulation, yet costly real-world demonstrations and limited access to dense process rewards hinder its practical application. We present TwinBridge, a digital twin-driven framework that supplies policy initialization and dense visual rewards for real-world online learning. We construct digital twins by combining 3D Gaussian splatting with physics simulation. Here, simulator states provide task events and geometric progress under physical prerequisites and ordering constraints, yielding rewards for policy pretraining with simulated demonstrations and reinforcement learning. We distill this supervision into a visual reward model. During real-world interaction, its predictions are combined with execution history to compute dense rewards for human-in-the-loop policy refinement. Across five real-world laboratory tasks, TwinBridge achieves a final mean autonomous success rate of 98% with at most 25 minutes of real-world interaction per task. Experiments show that dense rewards improve interaction efficiency over sparse rewards, and simulation-based policy initialization further accelerates learning.

</details>

#### 2026-11-04 - CrossPressor: Scalable Cross-View Fusion for Feed-Forward 3D Gaussian Splatting

**Authors:** Yuxi Hu, Wenhao Dong, Jun Zhang, Friedrich Fraundorfer
**Links:** [abs](https://arxiv.org/abs/2611.06258) - [pdf](https://arxiv.org/pdf/2611.06258)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3D-GS) becomes increasingly difficult to scale to long multi-view sequences. Anchor-based compression methods such as ZPressor alleviate representation growth by decoding Gaussians only from a compact set of anchor feature maps, but keeping these anchors fixed forces each one to aggregate an increasing number of support views. We identify this representation--fusion mismatch and introduce \textbf{CrossPressor}, a training-free method for scalable anchor-based fusion. CrossPressor preserves all decoder-facing anchor queries while constraining the view-growing support sequence through coverage-cycled evidence routing, distributing retained spatial evidence across support views and fusion layers while keeping all support views represented. Routing before K/V projection, together with joint context packing, further reduces support-side fusion cost without retraining. CrossPressor maintains reconstruction quality close to dense fusion while achieving up to $26.12\times$ faster cross-view fusion and $1.43\times$ end-to-end acceleration on long input sequences. Our project page is at: https://yuhsihu.github.io/CrossPressor.

</details>

#### 2026-11-03 - GSCV++: Lightweight 3D Gaussian Splatting Sequence Compression via Standard Video Codecs

**Authors:** Qi Yang, Yingzhan Xu, Kai Zhang, Li Zhang
**Links:** [abs](https://arxiv.org/abs/2611.05359) - [pdf](https://arxiv.org/pdf/2611.05359)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GSCV++: Lightweight 3D Gaussian Splatting Sequence Compression via Standard Video Codecs
- 作者：Qi Yang, Yingzhan Xu, Kai Zhang, Li Zhang
- 出版日期：2026-11-03T18:54:29Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.05359) / [PDF](https://arxiv.org/pdf/2611.05359)

### 一句话总结
GSCV++ 提出一种基于标准视频编解码器的轻量级 3D Gaussian Splatting 序列压缩流程，通过改进预处理、3D 到 2D 映射和实际压缩配置，在保持低复杂度与硬件兼容性的同时提升率失真性能和编解码速度。

### 研究问题
论文面向工业场景对低复杂度和硬件兼容性的需求，研究如何利用标准视频编解码器高效压缩 3D Gaussian Splatting 序列。摘要指出，需要在预处理、3D 到 2D 映射以及实际视频压缩配置方面联合改进，以降低数据量、减少冗余信息、生成更适合视频编解码器的 2D 特征图，并控制压缩复杂度。

### 核心思路/方法
论文提出 GSCV++，从三个方面改进 GS 序列压缩：
1. **预处理**：提出能量自适应帧间球谐（SH）交流分量降维（EA-SHDR），用于生成紧凑且稳定的时间 SH AC 特征空间，从而减少后续映射和实际压缩的数据量，并在消除冗余信息的同时降低复杂度。
2. **3D 到 2D 映射**：设计基于先验的 Inter-MiniPLAS（P-MiniPLAS），通过基于先验的权重因子推断和小尺度重映射生成平滑的 2D 特征图。与原始 Parallel Linear Assignment Sorting（PLAS）和 Morton 扫描相比，P-MiniPLAS 旨在使生成的 2D 图更适合视频编解码器，同时保持较低计算复杂度。
3. **实际压缩**：提出内容感知广义压缩（CA-GC），使用非均匀位深拆分生成坐标图，并引入编码单元尺寸选择以有效控制压缩复杂度，从而在不涉及规范性变化的情况下充分利用视频编解码器性能。

### 主要贡献
- 提出 GSCV++，一个面向 3D Gaussian Splatting 序列的轻量级压缩流程，基于标准视频编解码器。
- 提出 EA-SHDR，用于预处理阶段生成紧凑、稳定的时间 SH AC 特征空间。
- 提出 P-MiniPLAS，用于生成更适合视频编解码器的平滑 2D 特征图，并保持较低计算复杂度。
- 提出 CA-GC，通过非均匀位深拆分和编码单元尺寸选择提升实际压缩效率与复杂度控制。
- 摘要称实验显示，与 SOTA 方法相比，GSCV++ 在帧内和帧间预测率失真上分别取得超过 20% 和 60% 的增益，并在 2D 图生成、编码和解码速度上快于使用同类视频编解码器的其他 SOTA 方法；消融研究验证了所提模块的有效性和鲁棒性。

### 局限性
摘要未提供足够信息说明方法的具体适用边界、失败场景、对不同 GS 序列规模或内容类型的敏感性，以及实验数据集、评价协议和完整消融细节。因此无法仅依据摘要判断其泛化性和实际部署限制。

### 阅读优先级
**中**。理由：该论文关注 3D Gaussian Splatting 序列压缩与标准视频编解码器的结合，问题明确且工程实用性强，摘要给出了较清晰的模块设计和性能声明；但若关注理论创新或非视频编解码器路线的压缩方法，则优先级可降低。是否优先阅读取决于对 GS 压缩、视频编码兼容性和低复杂度部署的兴趣。

</details>

<details>
<summary>Abstract</summary>

This paper presents GSCV++, a lightweight pipeline for 3D {G}aussian {S}platting (GS) sequences {C}ompression with standard {V}ideo codecs. To meet the requirements of low-complexity and hardware compatibility from the industry, GSCV++ jointly improves preprocessing, 3D-to-2D mapping, and practical video compression configuration of GS compression. First, for preprocessing, energy-adaptive inter-frame spherical harmonic (SH) alternative current (AC) dimensionality reduction (EA-SHDR) is proposed to produces a compact and stable temporal SH AC feature space. It can reduce the data volume of following mapping and practical compression, as well as less complexity while eliminating redundant information. Second, for 3D-to-2D mapping, prior-based Inter-MiniPLAS (P-MiniPLAS) is designed to generate smooth 2D feature maps through prior-based weighting factor inference and small scale remapping. Compared with vanilla Parallel Linear Assignment Sorting (PLAS) and Morton scan, P-MiniPLAS ensures the generated 2D maps are more suitable for the video codec while maintaining a low level of computational complexity. Third, for practical compression, content-aware generalized compression (CA-GC) is developed to use a non-uniform bit-depth split for coordinate map generation, and a coding unit size selection is introduced for efficient compression complexity control, which fully exploits the performance of video codecs without involving normative changes. Experiments demonstrate that GSCV++ reports over 20\% in intra- and 60\% in inter-prediction rate-distortion gains compared with state-of-the-art (SOTA) methods. GSCV++ also achieves faster 2D map generation, encoding, and decoding than other SOTA methods using the same type of video codecs. Ablation studies verify the effectiveness and robustness of the proposed modules and provide insights for subsequent research.

</details>

#### 2026-11-03 - 3DGS-VBench+ and 3DGSV-Assessor: A Multi-Dimensional Subjective Benchmark and a Reference-Flexible Objective Model for 3D Gaussian Splatting Video Quality Assessment

**Authors:** Yuke Xing, William Gordon, Jiarui Wang, Yujie Zhang, Guangtao Zhai, Yiling Xu
**Links:** [abs](https://arxiv.org/abs/2611.04498) - [pdf](https://arxiv.org/pdf/2611.04498)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3DGS-VBench+ and 3DGSV-Assessor: A Multi-Dimensional Subjective Benchmark and a Reference-Flexible Objective Model for 3D Gaussian Splatting Video Quality Assessment
- 作者：Yuke Xing, William Gordon, Jiarui Wang, Yujie Zhang, Guangtao Zhai, Yiling Xu
- 出版日期：2026-11-03T08:26:13Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.04498 ；PDF https://arxiv.org/pdf/2611.04498 ；项目/代码 https://github.com/YukeXing/3DGSV-Assessor

### 一句话总结
论文面向3D Gaussian Splatting（3DGS）视频质量评估，构建了覆盖整体、几何与颜色三个维度的主观基准3DGS-VBench+，并提出可在一次生成中输出三维质量分数、且支持减参考（RR）与无参考（NR）模式的客观评估框架3DGSV-Assessor。

### 研究问题
摘要指出，3DGS虽支持实时新视角合成，但存储开销大，因此压缩必不可少；而训练与压缩都会引入与表示相关的失真。由于不少方法中的生成式压缩对几何属性和颜色属性采用不同参数，可能产生“维度特定”的失真，这促使研究进行多维度质量评估。此外，真实场景采集通常缺乏与合成连续相机轨迹对齐的真值视频，只能获得稀疏采集视图作为参考。因此，论文要解决的问题是：在对齐参考稀缺的条件下，如何对3DGS视频进行多维度质量评估，并构建相应主观基准与客观模型。

### 核心思路/方法
论文首先提出3DGS-VBench+：一个大规模主观视频质量评估基准，包含3,036个3DGS重建，每个重建配对一个渲染视频，覆盖11个真实场景与22个合成场景，由6种代表性压缩算法在系统设计的级别下生成，并标注9,108个MOS，覆盖整体质量、几何质量与颜色质量。基于该基准，论文提出3DGSV-Assessor：一个参考灵活的大规模多模态框架，在一次生成过程中为三个维度打分，并通过有界门控将基于排序的参考线索融合进冻结回归器，支持减参考（RR）与无参考（NR）评估。摘要称大量实验表明其在该基准上与人类感知达到最先进相关性，并对其他新视角合成基准具有较强零样本泛化能力。

### 主要贡献
- 构建3DGS-VBench+：大规模3DGS视频主观质量评估基准，含3,036个重建及配对渲染视频、11个真实场景与22个合成场景、6种代表性压缩算法及系统设计级别，并提供9,108个覆盖整体、几何、颜色质量的MOS标注。
- 提出3DGSV-Assessor：参考灵活的大规模多模态客观质量评估框架，一次生成输出整体、几何、颜色三维分数，并通过有界门控融合基于排序的参考线索到冻结回归器，支持RR与NR评估。
- 摘要声称在3DGS-VBench+上与人类感知达到最先进相关性，并展现出对其他新视角合成基准的较强零样本泛化能力。
- 摘要说明数据集与代码将公开于 https://github.com/YukeXing/3DGSV-Assessor。

### 局限性
- 摘要未提供足够信息说明主观实验的具体受试者规模、标注流程一致性或MOS置信度分析。
- 摘要未提供足够信息说明3DGSV-Assessor的具体网络结构、训练细节、计算开销与推理时延。
- 摘要未提供足够信息说明“有界门控”的具体设计、超参数选择及其消融结果。
- 摘要未提供足够信息给出与其他方法对比的完整实验设置、评价指标数值及零样本泛化的具体基准与幅度。
- 摘要未提供足够信息讨论该方法在非3DGS表示或其他压缩类型下的适用边界。

### 阅读优先级
中。理由：若关注3DGS压缩后的质量评估、多维度主观基准构建或参考灵活（RR/NR）的多模态质量模型，该论文与问题设定直接相关，且同时提供基准与模型；但摘要未给出具体实验数值、方法细节与消融信息，需阅读全文才能判断其可复现性与实际增益，因此优先级定为中而非高。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel view synthesis (NVS), but its heavy storage makes compression essential, and both training and compression introduce representation-specific distortions. Since generative compression in many methods treats geometric and color attributes via different parameters, it can induce dimension-specific distortions, motivating multi-dimensional assessment. Moreover, real-world captures generally lack an aligned ground-truth video for a synthesized, continuous camera trajectory, leaving only sparse captured views as references. To enable multi-dimensional quality assessment of 3DGS videos with scarce aligned references, we first present 3DGS-VBench+, a large-scale subjective video quality assessment (VQA) benchmark comprising 3{,}036 3DGS reconstructions, each paired with a rendered video, across 11 real-world and 22 synthetic scenes, generated by 6 representative compression algorithms at systematically designed levels and annotated with 9{,}108 MOSs covering overall, geometry, and color quality. Based on 3DGS-VBench+, we propose 3DGSV-Assessor, a reference-flexible, large multimodal framework that scores all three dimensions in one generation pass and fuses a ranking-based reference cue into the frozen regressor through a bounded gate, supporting both reduced-reference (RR) and no-reference (NR) assessment. Extensive experiments demonstrate state-of-the-art correlation with human perception on 3DGS-VBench+ and strong zero-shot generalization to other NVS benchmarks. The dataset and code will be released at https://github.com/YukeXing/3DGSV-Assessor.

</details>

#### 2026-11-03 - Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation

**Authors:** Can Wang, Qiyuan Qiao, Lei Liu, Ge Yuan, Xinhui Liu, Dong Xu
**Links:** [abs](https://arxiv.org/abs/2611.04493) - [pdf](https://arxiv.org/pdf/2611.04493)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation
- 作者：Can Wang, Qiyuan Qiao, Lei Liu, Ge Yuan, Xinhui Liu, Dong Xu
- 出版日期：2026-11-03T08:21:49Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.04493 ；PDF https://arxiv.org/pdf/2611.04493

### 一句话总结
该论文提出一种物理感知的扩散策略，通过将 3D Gaussian Splatting 与可微 Material Point Method 模拟耦合来从视觉演示中估计物体材质属性，并据此构建材质感知的 Mixture-of-Experts 扩散策略，以提升异构物体操纵的成功率与泛化性。

### 研究问题
论文针对日常物体操纵策略学习中的核心困难：不同材质物体具有不同的形变与接触动力学。扩散策略虽能建模多模态操纵行为，但摘要指出其通常缺乏显式物理推理，面对异构物体时可能产生“平均化”的动作。论文要解决的问题是：如何让基于视觉模仿学习的扩散策略具备对物体物理属性的理解，从而在不同物理条件下自适应生成操纵行为。

### 核心思路/方法
摘要给出的方法链条包括三个环节：
1. **物理参数估计**：将 3D Gaussian Splatting 与可微 Material Point Method 模拟耦合，从视觉演示中恢复材质属性；其中视频引导与粒子级约束用于实现准确的物理参数估计。
2. **物理条件注入策略**：将估计出的物理条件集成到材质感知的 Mixture-of-Experts 扩散策略中，使行为生成可跨不同物理状态自适应。
3. **实际部署机制**：引入 physics memory bank，在不需要在线模拟优化的情况下提供高效的物理检索。

### 主要贡献
基于摘要可归纳的贡献为：
- 提出一种物理感知的扩散策略框架，将视觉模仿学习与物体物理理解相结合。
- 构建了由 3D Gaussian Splatting 与可微 MPM 模拟耦合的材质属性估计方法，并利用视频引导和粒子级约束提升参数估计准确性。
- 设计了材质感知的 Mixture-of-Experts 扩散策略，以适配不同物理状态下的行为生成。
- 提出 physics memory bank，用于部署阶段的高效物理检索，避免在线模拟优化。
- 摘要称在大量仿真与真实物体上的实验显示，相比现有基于扩散的方法，该方法在操纵成功率和泛化性上有提升。

### 局限性
摘要未提供足够信息说明以下方面：具体实验设置、基线方法细节、成功率数值、真实世界实验规模、材质属性估计的误差范围、Mixture-of-Experts 的结构与训练细节、physics memory bank 的存储与检索开销，以及方法在未见材质或复杂接触场景下的失效模式。因此无法基于给定摘要评估其定量性能边界与适用范围。

### 阅读优先级
**中**。理由：论文主题位于神经场景表示与机器人操纵的交叉处，若关注扩散策略的物理先验注入、3D Gaussian Splatting 用于物理参数估计、或可微 MPM 与策略学习的结合，则具有较高相关性；但摘要未提供定量结果与实验细节，无法仅凭摘要判断其相对优势的强度，需阅读全文进一步确认。

</details>

<details>
<summary>Abstract</summary>

Learning robust manipulation policies for diverse everyday objects remains challenging because objects with different materials exhibit distinct deformation and contact dynamics. While diffusion policies provide a powerful framework for modeling multimodal manipulation behaviors, they typically lack explicit physical reasoning and may produce averaged actions when facing heterogeneous objects. We present a physics-aware diffusion policy that augments visual imitation learning with object physical understanding. Our framework recovers material properties from visual demonstrations by coupling 3D Gaussian Splatting with differentiable Material Point Method simulation, where video guidance and particle-level constraints enable accurate physical parameter estimation. The estimated physics conditions are further integrated into a material-aware Mixture-of-Experts diffusion policy, allowing adaptive behavior generation across different physical regimes. For practical deployment, we introduce a physics memory bank that provides efficient physical retrieval without requiring online simulation optimization. Experiments on a wide range of simulated and real-world objects demonstrate improved manipulation success and generalization over existing diffusion-based approaches. These results show that incorporating physical knowledge is critical for scalable robot manipulation in diverse environments.

</details>

#### 2026-11-03 - EndoS3:Endoscopic Semantic Splatting SLAM

**Authors:** Mona Sheikh Zeinoddin, Benjamin Wright, Zafer Tandogdu, Greg Shaw, Evangelos Mazomenos, Danail Stoyanov
**Links:** [abs](https://arxiv.org/abs/2611.04358) - [pdf](https://arxiv.org/pdf/2611.04358)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** deformable reconstruction, SLAM, Gaussian Splatting, splatting, mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EndoS3:Endoscopic Semantic Splatting SLAM
- 作者：Mona Sheikh Zeinoddin, Benjamin Wright, Zafer Tandogdu, Greg Shaw, Evangelos Mazomenos, Danail Stoyanov
- 出版日期：2026-11-03T05:41:06Z
- 分类：Neural Scene Representations & Rendering；次要分类：3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.04358 ；PDF https://arxiv.org/pdf/2611.04358

### 一句话总结
论文提出基于高斯溅射（Gaussian Splatting）的内窥镜语义 SLAM 框架 EndoS3，并引入带 RGB-D 帧、相机位姿与实例标注的 ex-vivo 胆囊切除数据集 CRCD++，摘要称其在跟踪、重建和语义建图上优于对比方法。

### 研究问题
摘要指出，面向 3D 手术场景理解的语义 SLAM 仍研究不足，原因有二：一是需并行解决相机位姿跟踪、高保真可变形重建和语义建图三项困难任务；二是缺乏能在接近真实手术流程环境下全面评估这三项任务所需真值的数据集。论文旨在同时应对方法框架与评测数据两方面的缺口。

### 核心思路/方法
- 提出 EndoS3，一种以高斯溅射为基础、利用实例掩码引导三项任务的语义 SLAM 框架。
- 实例级运动分解模块：在补偿相机运动后评估残差光流，并考虑光流噪声、比较相邻实例间运动，以分离静态与动态实例。
- 相机跟踪针对静态高斯进行；实例感知的形变场为每个动态实例配置各自的控制节点与形变网络。
- 语义节点分配模块：按实例的尺寸与非刚性程度，在实例间重新分配固定节点预算。
- 构建 CRCD++：ex-vivo 胆囊切除数据集，包含 RGB-D 帧、相机位姿和实例标注，用于完整语义 SLAM 评估。

### 主要贡献
- 提出 EndoS3 语义 SLAM 框架，以实例掩码统一引导运动分解、相机跟踪、动态实例形变建模与语义节点分配。
- 提出实例级运动分解，通过残差光流、噪声考量与邻域实例比较区分静态/动态实例。
- 提出实例感知形变场与语义节点分配机制，为动态实例分配独立控制节点与形变网络，并按尺寸和非刚性重分配固定节点预算。
- 发布 CRCD++ ex-vivo 胆囊切除数据集，提供 RGB-D 帧、相机位姿与实例标注，支持完整语义 SLAM 评测。
- 摘要报告在 CRCD++ 与 SemSup 数据集上，EndoS3 在跟踪、重建和语义建图方面超过现有通用及手术语义 SLAM 方法；结论强调语义感知的运动与形变建模对手术语义 SLAM 至关重要。

### 局限性
- 摘要未提供足够信息说明具体实验设置、评价指标、对比方法数量与消融细节。
- 摘要未提供足够信息说明 EndoS3 在真实活体手术、不同术式或跨数据集条件下的泛化能力。
- 摘要未提供足够信息说明方法对实例掩码质量、光流噪声或动态场景复杂度的敏感性与失败情形。
- 摘要未提供足够信息说明 CRCD++ 的规模、采集设备、标注规范及数据多样性。
- 摘要未提供足够信息说明计算开销、实时性及临床部署可行性。

### 阅读优先级
中。理由：论文聚焦内窥镜语义 SLAM，将实例掩码、运动分解、可变形高斯重建与语义建图结合，并配套新数据集，对手术场景理解与神经渲染交叉方向具有参考价值；但摘要未给出实验规模、定量指标和失败案例分析，是否值得优先精读需结合全文实验与数据集细节进一步判断。

</details>

<details>
<summary>Abstract</summary>

Purpose: Despite advances in 3D surgical scene understanding, semantic simultaneous localisation and mapping (SLAM) remains under-explored for two key reasons. First, it requires solving three challenging tasks in parallel: camera pose tracking, high-fidelity deformable reconstruction, and semantic mapping, making progress particularly demanding. Second, the scarcity of datasets providing the necessary ground truth to evaluate all three tasks comprehensively under conditions that closely reflect real surgical procedures environments. Method: We propose EndoS3, a Gaussian Splatting-based semantic SLAM framework that uses instance masks to guide all three tasks. An instance-level motion decomposition module separates static and dynamic instances by evaluating residual flow after compensating for camera motion, accounting for flow noise and comparing motion across neighbouring instances. The camera is tracked against the static Gaussians, while an instance-aware warp field gives each dynamic instance its own control nodes and deformation network. A semantic node allocation module redistributes a fixed node budget across instances according to their size and non-rigidity. We also introduce CRCD++, an ex-vivo Cholecystectomy dataset with RGB-D frames, camera pose and instance annotations for full semantic SLAM evaluation. Results: EndoS3 surpasses all state-of-the-art general-purpose and surgical semantic SLAM methods in tracking, reconstruction and semantic mapping on the CRCD++ and SemSup datasets. Conclusion: Semantic-aware motion and deformation modelling is vital to surgical semantic SLAM. EndoS3 and CRCD++ offer a method and benchmark for improved geometric and semantic understanding in endoscopy.

</details>

#### 2026-11-03 - SettleSplat: Monocular Gaussian Mapping under In-View Scene Changes

**Authors:** Anh Thuan Tran, Xiyun Song, Yubin Zhou, Heather Yu, Jana Kosecka, Liang Peng
**Links:** [abs](https://arxiv.org/abs/2611.04195) - [pdf](https://arxiv.org/pdf/2611.04195)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, robotics, mapping, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SettleSplat: Monocular Gaussian Mapping under In-View Scene Changes
- 作者：Anh Thuan Tran, Xiyun Song, Yubin Zhou, Heather Yu, Jana Kosecka, Liang Peng
- 出版日期：2026-11-03T02:29:27Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.04195 ；PDF https://arxiv.org/pdf/2611.04195

### 一句话总结
SettleSplat 面向单目在线序列中相机视野内物体被操作引发的场景变化，通过高斯动态性场剔除瞬态变化，并利用几何矛盾与参数无关的渲染深度不确定性识别持久变化，从而维护更新的 3D 高斯地图。

### 研究问题
论文关注“视野内场景变化”（in-view scene changes）：在单个在线序列中，物体在相机前被操作。该设定不同于以往检测相机视野外变化或不同次拍摄之间变化的工作。其难点在于瞬态动态与持久动态交织：物体移动时可能是干扰物，稳定后则成为场景中的持久变化。现有方法多假设静态场景或将动态作为异常值过滤，近期工作虽开始移除干扰物以获得干净静态背景，但视野内场景变化仍研究不足。

### 核心思路/方法
基于摘要，方法包括两部分：
1. 将粗略的逐像素不确定性提升为高斯动态性场，并据此剪除瞬态高斯。
2. 针对持久变化，利用由参数无关的渲染深度不确定性加权的几何矛盾，区分真实变化与优化不足区域。
系统目标是在上述变化下维持最新的 3D 高斯地图，属于单目在线建图系统。

### 主要贡献
- 提出 SettleSplat，一个单目在线建图系统，可在视野内场景变化下维护更新的 3D 高斯地图。
- 将逐像素不确定性提升为高斯动态性场，用于剪除瞬态变化。
- 使用参数无关的渲染深度不确定性加权几何矛盾，以分离真实持久变化与优化不足区域。
- 在 Bonn 和 Co-Fusion 上报告了结果：SettleSplat 获得一致的 3D 高斯地图，在全图与变化区域上优于当前基线，并保持可比速度。

### 局限性
摘要未提供足够信息。未提供关于计算开销细节、失败案例、对特定场景类型或运动模式的适用边界、长期在线运行稳定性、参数敏感性等信息的说明。

### 阅读优先级
中。理由：该论文聚焦在线单目 3D 高斯建图中的视野内场景变化，问题设定对 AR、机器人和自主系统等应用具有相关性，且摘要给出了明确的方法要点与基准结果；但摘要未展开实验细节与局限分析，是否优先精读取决于读者对动态场景高斯建图或在线建图方向的直接兴趣。

</details>

<details>
<summary>Abstract</summary>

Online 3D Gaussian mapping enables fast and high-fidelity novel view synthesis, with broad applications in augmented reality, robotics, and autonomous systems. However, many current methods assume static scenes or filter out dynamics as outliers. In this paper, we study in-view scene changes where objects are manipulated in front of the camera within a single online sequence, unlike prior works that detect changes outside the camera view or between separate captures. This setting entangles transient and persistent dynamics, as objects can be distractors while moving and persistent once they settle. While recent studies start to address distractors by removing them for clean static background, in-view scene changes remain underexplored. To resolve this, we present SettleSplat, a monocular mapping system that maintains up-to-date 3D Gaussian maps under such changes. Specifically, we lift coarse per-pixel uncertainty into Gaussian dynamicity field, then prune transient ones. For persistent changes, we derive geometric contradictions weighted by parameter-free rendered depth uncertainty to separate true changes from under-optimized regions. On Bonn and Co-Fusion, SettleSplat achieves consistent 3D Gaussian maps, outperforming current baselines on both full images and change regions while maintaining comparable speed.

</details>

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

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-04 - USI-Brain: Enhancing Underwater Spatial Intelligence via Spatial Data-Driven Vision-Language Modeling

**Authors:** Zhiliang Zhu, Zhiqiang Zhao, Xie'an Jiang, Yingxin Lai, Kangye Zheng, Dawei Zhao
**Links:** [abs](https://arxiv.org/abs/2611.06040) - [pdf](https://arxiv.org/pdf/2611.06040)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>Abstract</summary>

Underwater spatial reasoning depends on object boundaries and geometric cues that are obscured by scattering, color distortion, and low visibility. Existing underwater resources capture these cues through images, annotations, and depth maps, but provide fragmented supervision for vision-language models. We present a spatial data engine that connects visual appearance with object-level geometry through enhancement, 2D and geometry-assisted question generation, and expert filtering. It produces 4.27M QA pairs across five capability groups. We use this corpus to train USI-Brain and introduce an Underwater Prior-guided Rectifier (UPR) that applies gated corrections to visual features. USI-Bench evaluates the resulting capabilities with 6,525 held-out QA pairs. On its 15 task metrics, USI-Brain and USI-Brain + UPR improve over Qwen3-VL-8B-Instruct by 5.76 and 7.63 points on average, respectively, using signed differences on 100-point scales. Ablations show that geometry-assisted supervision improves depth and ordering by 4.8 and 6.1 points with UPR disabled, while UPR adds 18.0 points in scene description under matched training data. Both variants use raw images at evaluation. Across NautData, UWBench, and MarineEval, USI-Brain achieves the best or joint-best score on 28 of 32 metrics. Model weights and USI-Bench will be released at https://github.com/SKY-Zhu-91/USI-Brain.

</details>

#### 2026-11-03 - OdorSpaces: Visual-Olfactory Embodied Navigation in 3D Environments

**Authors:** Changyeon Lee, Kelin Yu, Zheng Wei, Shuna Ni, Ruohan Gao
**Links:** [abs](https://arxiv.org/abs/2611.05738) - [pdf](https://arxiv.org/pdf/2611.05738)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, localization, simulation

<details>
<summary>Abstract</summary>

Olfaction provides critical information about airborne chemical cues, yet it remains largely underexplored in embodied AI, with limited prior machine olfaction work focusing primarily on semantic odor perception. We introduce OdorSpaces, a physics-based simulation platform and benchmark for visual-olfactory embodied navigation. OdorSpaces augments Habitat-Sim with 3D odor transport and dispersion simulated by Fire Dynamics Simulator (FDS), enabling agents to navigate photorealistic indoor environments using both visual and olfactory observations. The benchmark includes two representative source-seeking scenarios: invisible gas-leak localization and early-stage fire localization. We develop an initial multimodal reinforcement learning policy that integrates visual observations and olfactory measurements over time. Experiments show that the policy outperforms a diverse set of baselines, establishing a strong reference for future research on visual-olfactory embodied navigation.

</details>

#### 2026-11-03 - Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation

**Authors:** Mengjie Zhao, Yuxin Chen, Yiyang Shao, Chuye Hong, Jiakang Chen, Koushil Sreenath, Masayoshi Tomizuka
**Links:** [abs](https://arxiv.org/abs/2611.05507) - [pdf](https://arxiv.org/pdf/2611.05507)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Humanoid motion tracking has scaled to general policies that reproduce diverse human motion, but the resulting behavior is in free-space: the tracker knows where the body should be, not how it should interact with the environment. Other work makes the object part of the objective, yet abstracts that interaction to contact or geometry, which leaves the demanding cases under-explored. We argue that force is a natural command channel between motion imitation and object interaction, one that specifies not just where to make contact but how hard. We present Ctrl-F, a hierarchical motion-force framework that augments motion tracking with an explicit force command, a 3-D force at each designated contact body such as a hand or a foot. The hierarchical framework comprises: (1) A unified motion-force controller tracks the reference motion while applying the commanded force to the world. (2) A high-level force planner that issues a force command online based on object state and proprioception observations. In simulation and on hardware, Ctrl-F completes loco-manipulation that demands large, sustained interaction force and adjusts its command online as the load changes, both out of reach of a force-blind tracker. On hardware, Ctrl-F demonstrates hand-based dragging, pushing, and lifting, as well as foot-based kicking, successfully manipulating boxes weighing up to 20kg in pushing and kicking tasks where the force-blind baseline fails, while adapting online to additional loads introduced mid-task.

</details>

#### 2026-11-03 - Low-Density 3D Point Cloud Classification

**Authors:** Ahmed Baha Ben Jmaa, Faten Chaieb
**Links:** [abs](https://arxiv.org/abs/2611.05291) - [pdf](https://arxiv.org/pdf/2611.05291)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, autonomous driving, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Low-Density 3D Point Cloud Classification
- 作者：Ahmed Baha Ben Jmaa, Faten Chaieb
- 出版日期：2026-11-03T18:07:11Z
- 分类：主分类 Embodied / Robotics / AR Applications；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2611.05291) ｜ [PDF](https://arxiv.org/pdf/2611.05291)

### 一句话总结
本文针对低密度 3D 点云分类性能下降的问题，提出面向低密度点云的架构 LD-PointNet++，并在 ModelNet 基准上报告了跨密度水平保持 90% 以上准确率的结果。

### 研究问题
3D 点云分类在增强现实/虚拟现实、机器人、自动驾驶等领域应用广泛，但真实场景中由于传感技术限制和环境条件变化，点云密度会发生变化。现有分类方法在稠密点云上表现良好，但在低密度点云上性能可能下降。论文要解决的核心问题是：如何在密度水平变化的条件下，尤其是低密度条件下，稳定地进行 3D 点云分类。

### 核心思路/方法
论文提出名为 LD-PointNet++ 的架构，专门针对低密度点云分类进行优化。作为铺垫，作者还开展了首个系统性基准评测研究，在不同密度水平下评估当前最先进的点云分类方法，并据此揭示低密度环境下显著的性能下降。摘要未提供 LD-PointNet++ 的具体网络结构、模块设计或训练策略等细节。

### 主要贡献
- 开展首个系统性基准评测研究，在不同密度水平下评估最先进的点云分类方法，揭示低密度环境下性能显著下降的现象。
- 提出面向低密度点云分类的架构 LD-PointNet++。
- 在 ModelNet 基准数据集上的实验结果表明，LD-PointNet++ 在低密度场景下优于上述对比方法，并在不同密度水平下保持 90% 以上的稳定准确率。

### 局限性
摘要未提供足够信息说明方法的具体结构、计算开销、对真实传感器噪声的鲁棒性、除 ModelNet 外的泛化表现，以及基准评测所覆盖的具体方法清单和密度设置细节。因此无法基于摘要评估其适用范围与潜在限制。

### 阅读优先级
中。理由：该论文关注点云密度变化这一实际部署中的关键问题，并提供了跨密度基准评测与专门架构，对机器人、AR/VR 等主分类应用有直接相关性；但摘要未给出方法细节和更广泛的实验验证信息，需阅读全文后才能判断其技术新颖性与结论稳健性。

</details>

<details>
<summary>Abstract</summary>

3D point cloud classification, a task in computer vision, has recently gained substantial interest due to its extensive applications across various domains such as augmented and virtual reality, robotics, and autonomous driving. However, classifying 3D point clouds becomes challenging in real-world scenarios where the density levels vary. These variations are due to limitations inherent to current sensing technologies and variable environmental conditions, which often prevent the capture of detailed and comprehensive geometric representations. Existing classification methods, which have demonstrated impressive results on dense point clouds, may be affected and could experience reduced performance when dealing with low-density point clouds. Addressing this challenge, this paper introduces LD-PointNet++, an architecture optimized for the classification of low-density point clouds. To pave the way for LD-PointNet++, we conduct the first benchmarking study that systematically evaluates state-of-the-art point cloud classification methods across varying densities, revealing significant performance declines in low-density environments. Experimental results on the ModelNet benchmark dataset demonstrate that LD-PointNet++ not only outperforms these methods in low-density scenarios but also demonstrates consistent accuracy above 90% across different density levels.

</details>

#### 2026-11-03 - MiCaDe: Online LiDAR-Camera Miscalibration Change Detection for Autonomous Driving

**Authors:** Carlo Sgaravatti, Riccardo Pieroni, Matteo Corno, Sergio M. Savaresi, Luca Magri, Giacomo Boracchi
**Links:** [abs](https://arxiv.org/abs/2611.04912) - [pdf](https://arxiv.org/pdf/2611.04912)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** camera calibration, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MiCaDe: Online LiDAR-Camera Miscalibration Change Detection for Autonomous Driving
- 作者：Carlo Sgaravatti, Riccardo Pieroni, Matteo Corno, Sergio M. Savaresi, Luca Magri, Giacomo Boracchi
- 出版日期：2026-11-03T13:52:45Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.04912) / [PDF](https://arxiv.org/pdf/2611.04912)

### 一句话总结
MiCaDe 是一种在线检测 LiDAR-相机外参标定何时失效的方法，利用跨模态检测框的几何一致性构建统计监测流，并通过变点模型累积证据以发现细微漂移。

### 研究问题
自动驾驶多传感器感知依赖相机与 LiDAR 之间的准确标定。长期部署中，振动、热效应和轻微机械冲击会导致标定漂移，使外参不再准确，进而给下游融合任务带来系统性误差。论文关注的问题是：如何在不依赖标定靶标、不修改感知栈的前提下，在线检测外参标定是否已经不再准确。

### 核心思路/方法
论文提出 MiCaDe（Miscalibration Change Detection），核心假设是：在标定正确时，标准目标检测器产生的 3D 与 2D 边界框应保持几何一致。方法通过匹配跨模态检测结果，导出几何一致性指标，作为外参漂移的敏感指示量；将这些指标聚合成固定大小的批次，并与参考分布比较打分，形成似然流；随后用 Change Point Model（CPM）对该似然流进行监测。CPM 随时间累积统计证据，从而能够检测原本不易察觉的细微漂移。摘要称该方法无需标定靶标，也无需修改感知栈，并具有低误报率和可忽略的计算开销。

### 主要贡献
- 提出一种在线 LiDAR-相机外参标定变化检测方案 MiCaDe，用于判断外参是否仍准确。
- 利用标准目标检测器输出的 3D/2D 边界框跨模态几何一致性构造检测指标，不依赖标定靶标。
- 将一致性指标批量化并与参考分布比较，结合 CPM 累积统计证据，以检测细微标定漂移。
- 摘要称该方法无需修改感知栈，具有低误报率和可忽略的计算开销。
- 摘要称在多个长序列数据集以及一个物理诱导标定误差的真实世界数据集上进行了实验，验证了多条件下的可靠检测，并提供代码链接。

### 局限性
- 摘要未提供足够信息说明方法对检测器性能、检测漏检或跨模态匹配失败的敏感性。
- 摘要未提供足够信息说明参考分布如何构建、是否需要场景特定假设，以及冷启动或分布变化下的表现。
- 摘要未提供足够信息给出具体误报率、检测延迟、计算开销数值或与其他方法的定量对比。
- 摘要未提供足够信息说明在极端天气、稀疏点云、目标稀少场景下的适用性。
- 摘要未提供足够信息说明物理诱导标定误差实验的规模、标定误差类型与范围。

### 阅读优先级
中。理由：该论文针对自动驾驶长期部署中的在线标定漂移检测问题，问题定义清晰，方法思路简洁且不依赖标定靶标，若关注多传感器融合可靠性与在线监测，具有参考价值；但当前仅有摘要，缺少定量实验结果、误报率与检测延迟等关键细节，是否值得深入阅读需结合全文实验部分进一步判断。

</details>

<details>
<summary>Abstract</summary>

Reliable multi-sensor perception in autonomous vehicles requires accurate calibration between cameras and LiDAR. However, calibration drift is often unavoidable in long-term deployments: vibrations, thermal effects, and minor mechanical shocks may alter the relative pose between sensors, leading to systematic errors in downstream fusion tasks. We propose MiCaDe (Miscalibration Change Detection), an online solution detecting when the extrinsic LiDAR-camera calibration parameters are no longer accurate by means of sequential change detection. MiCaDe requires no calibration targets, or modification of the perception stack, providing low false-alarm rates with negligible computational overhead. Our key insight is that 3D and 2D bounding boxes produced by standard object detectors should remain geometrically consistent under correct calibration. By matching cross-modal detections, we derive geometric consistency metrics that serve as sensitive indicators of extrinsic drift. These metrics are aggregated into fixed-size batches and scored against a reference distribution, producing a likelihood stream that is monitored by a Change Point Model (CPM). Crucially, the CPM accumulates statistical evidence over time, enabling detection of subtle drifts that would otherwise go unnoticed. Experiments on multiple long-sequence datasets and on a real-world dataset with physically induced miscalibration confirm reliable detection under diverse conditions. Code available at: https://github.com/CarloSgaravatti/MiCaDe.

</details>

#### 2026-11-03 - BhopalMLS: A LiDAR Dataset for Semantic Scene Understanding in Heterogeneous Urban Environments

**Authors:** Pyare Lal Chauhan, Vaibhav Kumar, Bharat Lohani
**Links:** [abs](https://arxiv.org/abs/2611.04654) - [pdf](https://arxiv.org/pdf/2611.04654)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BhopalMLS: A LiDAR Dataset for Semantic Scene Understanding in Heterogeneous Urban Environments
- 作者：Pyare Lal Chauhan, Vaibhav Kumar, Bharat Lohani
- 出版日期：2026-11-03T10:41:37Z
- 分类：主分类 Embodied / Robotics / AR Applications；无次分类
- 链接：[摘要](https://arxiv.org/abs/2611.04654) / [PDF](https://arxiv.org/pdf/2611.04654)

### 一句话总结
论文提出面向印度博帕尔非规划、异构城市环境的移动激光扫描（MLS）大规模 LiDAR 数据集 BhopalMLS，并基于语义/实例分割与跨区域迁移实验，论证其细粒度子类型覆盖对 3D 感知可比性与迁移性的价值。

### 研究问题
现有 3D 数据集多采集于规划良好的城市，结构更统一、子类型多样性不足；而密集、异构、混合交通、非正式结构与狭窄非规划街道等场景缺乏专门基准。论文关注：此类非规划城市环境能否为 3D 语义/实例分割提供更具挑战和代表性的测试平台，以及其相对既有数据集在跨区域迁移上的特性。

### 核心思路/方法
- 构建 BhopalMLS：约 10 km 道路走廊、超过 12 亿点、19,518 个标注实例、62 个细粒度静态类别，并归并为 12 类与 21 类两套基准分类体系；另设 6 个可选运动类子类用于动态对象分析。
- 在两种粒度上进行语义分割与实例分割评测，比较微调基础模型与监督基线。
- 与 Ke-MLS、Toronto-3D、Paris-Lille-3D、SemanticKITTI 四个既有数据集做跨区域迁移实验，考察双向迁移性。
- 通过固定标签预算的因子控制重训练，区分数据集规模、走廊几何与子类型覆盖对迁移优势的贡献。

### 主要贡献
- 发布 BhopalMLS 数据集，覆盖非规划、异构城市环境的 MLS 点云，并提供 12 类/21 类基准分类与细粒度子类型标注，以及动态对象可选子类。
- 给出语义与实例分割基准结果：微调基础模型优于监督基线，如 Utonia(L) 在 12 类基准上达到 71.28% mIoU（对比从零训练的 PTv3 68.04%）和 44.07% mAP50。
- 揭示一致的“非对称可迁移性”：在每一对数据集上，BhopalMLS 训练的模型迁移到其他数据集优于反向迁移（Utonia(L) 与 Concerto(L) 平均 21.5、最高 36 mIoU 点），即使目标数据集更稠密亦然。
- 通过固定标签预算的因子控制实验，将迁移优势归因于 BhopalMLS 的子类型清单覆盖，而非数据集规模或走廊几何；将每类坍缩为单一子类型会使 Utonia(L) 与 Concerto(L) 分别损失 13.0 与 13.3 mIoU 点。
- 提供数据与交互式查看器链接。

### 局限性
- 摘要未提供足够信息说明传感器配置、采集平台细节、标注流程与质量控制、标注一致性或误差分析。
- 摘要未提供足够信息说明 21 类基准上的完整分割结果、各对比数据集的逐项数值，以及跨区域实验的具体协议细节。
- 摘要未提供足够信息说明动态对象分析（6 个运动子类）的评测结果。
- 摘要未提供足够信息说明数据集在天气、光照、季节或长期变化上的覆盖情况。
- 摘要未提供足够信息说明计算资源、训练时长与模型超参数等可复现性细节。

### 阅读优先级
中。理由：若关注 3D 语义/实例分割、LiDAR 数据集构建或跨区域迁移与域泛化，该文提供了非规划城市环境的新基准与“子类型覆盖驱动迁移性”的可检验结论，具有较高参考价值；但摘要未给出传感器、标注协议与完整实验细节，需阅读全文才能评估数据质量与可复现性。若仅关注方法创新而非数据与基准，优先级可下调。

</details>

<details>
<summary>Abstract</summary>

We introduce BhopalMLS, a large-scale Mobile Laser Scanning (MLS) dataset from a dense, heterogeneous urban environment in Bhopal, India, with mixed traffic, informal structures, and narrow unplanned streets. It spans approximately 10 km of road corridors with over 1.2 billion points and 19,518 annotated instances across 62 fine-grained static categories, grouped into 12-class and 21-class benchmark taxonomies; 6 optional moving-class subclasses support dynamic-object analysis. Existing 3D datasets, collected in well-planned cities, are structurally more uniform than such unplanned settings, and lack their subtype diversity. On semantic and instance segmentation at both granularities, fine-tuned foundation models surpass supervised baselines: Utonia(L) reaches 71.28% mIoU (vs. PTv3's 68.04% from scratch) and 44.07% mAP50 on the 12-class benchmark. Cross-region experiments against four established datasets (Ke-MLS, Toronto-3D, Paris-Lille-3D, SemanticKITTI) reveal a consistent asymmetric transferability: models trained on BhopalMLS transfer better than the reverse on every pair, for both Utonia(L) and Concerto(L) (mean 21.5, up to 36 mIoU points), holding even when the target is denser. Factor-controlled retraining at a fixed label budget, repeated on both models, attributes this to the coverage of BhopalMLS's subtype inventory rather than to dataset size or corridor geometry: collapsing each class to a single subtype costs 13.0 and 13.3 mIoU points for Utonia(L) and Concerto(L). BhopalMLS therefore offers a testbed for 3D perception beyond well-planned cities. Data and an interactive viewer are at https://geoai4cities.github.io/bhopalmls.

</details>

#### 2026-11-03 - Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation

**Authors:** Jimmy Wang, Yifan Chou, Kaifeng Zhang, Yixuan Wang, Binghao Huang, Tao Yu, Saleh Nabi, Yunzhu Li
**Links:** [abs](https://arxiv.org/abs/2611.04492) - [pdf](https://arxiv.org/pdf/2611.04492)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation
- 作者：Jimmy Wang, Yifan Chou, Kaifeng Zhang, Yixuan Wang, Binghao Huang, Tao Yu, Saleh Nabi, Yunzhu Li
- 出版日期：2026-11-03T08:20:53Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.04492 ；PDF https://arxiv.org/pdf/2611.04492

### 一句话总结
该论文提出“3D World Simulator”，用混合粒子-体素自编码器将点云压缩为紧凑 3D 体素潜变量，并通过动作条件潜动力学模型联合预测外观、几何与触觉，从而进行多模态 3D 世界模拟。

### 研究问题
论文关注的是：如何让动作条件世界模型显式建模底层 3D 场景，而不是仅在 2D 图像或视频空间预测未来观测。摘要指出，许多现有动作条件世界模型在 2D 空间预测未来观测，导致跨视角和长时程交互中的空间一致性具有挑战。因此，论文要解决的是在统一 3D 表示下进行动作条件、多模态、长时程世界预测的问题。

### 核心思路/方法
摘要给出的方法包括两部分：
1. 混合粒子-体素自编码器：将点云压缩为紧凑的 3D 体素潜变量；
2. 动作条件潜动力学模型：预测这些 3D 体素潜变量的演化。

二者共享统一的 3D 表示，使模型能够从任意视角进行几何一致的渲染，并灵活整合空间对齐的触觉信号。整体框架被描述为动作条件的多模态世界建模框架，联合预测外观、几何和触觉观测。

### 主要贡献
根据摘要，论文的贡献可归纳为：
- 提出 3D World Simulator，一个动作条件的多模态世界建模框架，从统一 3D 表示联合预测外观、几何与触觉观测；
- 结合混合粒子-体素自编码器与动作条件潜动力学模型，在紧凑 3D 体素潜空间中进行预测；
- 共享 3D 表示支持任意视角的几何一致渲染，并支持空间对齐触觉信号的灵活整合；
- 实验展示 50 Hz 的交互式、长时程、多模态预测；
- 展示该模型可利用触觉与多视角视觉观测（包括腕装相机和新视角相机）为策略训练与评估生成可扩展数据；
- 将方法扩展到包含多样物体的大型数据集，并展示基于模型的规划可处理未见物体和机器人配置。

### 局限性
摘要未提供足够信息说明局限性。摘要未提供足够信息说明失败案例、计算成本、对真实机器人部署的限制、触觉信号获取条件、数据集规模细节或与基线方法的定量比较。

### 阅读优先级
高。理由：该论文直接面向具身智能/机器人中的动作条件 3D 世界建模，问题定义清晰，方法将 3D 几何、外观与触觉统一到共享表示中，并声称支持 50 Hz 交互式长时程预测、策略数据生成和基于模型的规划；这些内容与机器人策略学习、评估和规划高度相关。但摘要未给出定量结果和局限性细节，阅读时需重点核查实验设置与泛化边界。

</details>

<details>
<summary>Abstract</summary>

Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning. However, many action-conditioned world models predict future observations in 2D image or video space without explicitly modeling the underlying 3D scene, making spatial consistency across viewpoints and over long-horizon interactions challenging. We introduce 3D World Simulator, an action-conditioned multimodal world modeling framework that jointly predicts appearance, geometry, and tactile observations from a unified 3D representation. Our approach combines a hybrid particle-voxel autoencoder that compresses point clouds into compact 3D voxel latents with an action-conditioned latent dynamics model that predicts their evolution. The shared 3D representation supports geometrically consistent rendering from arbitrary viewpoints and flexible integration of spatially aligned tactile signals. Our experiments demonstrate interactive, long-horizon, multimodal prediction at 50 Hz. We then show how our model enables scalable data generation for policy training and evaluation using tactile and multi-view visual observations, including wrist-mounted and novel camera views. Furthermore, we scale our method to large datasets containing diverse objects and demonstrate model-based planning with unseen objects and robot configurations. Together, these results highlight the potential of hybrid particle-voxel dynamics as a foundation for multimodal 3D world simulation.

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
