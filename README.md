# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：52
- 分类分布：
  - Embodied / Robotics / AR Applications: 18
  - Neural Scene Representations & Rendering: 15
  - 3D Reconstruction & Multi-view Geometry: 12
  - Dynamic / 4D Reconstruction: 4
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **3DGS/4DGS 从“能重建”转向“能部署”：压缩、剪枝、容量分配成为主线。**
   今日多篇论文的核心不再是提升峰值渲染质量，而是解决存储、内存和推理一致性问题：COSA-GS 用 anchor 因果分解 + 量化感知训练/整数推理实现跨平台一致的熵解码；OceanXL 用分块划分与自适应剪枝把 3DGS 推向大规模水下场景；AdaTex4D 用可见性归一化梯度与形变局部尺度做自适应纹理容量分配；Only What Was Seen 用 per-Gaussian 观测 Gram 矩阵把球谐系数压缩统一为率失真/量化问题（降阶、阶数分配、向量量化）。这反映出 3DGS 正从“表示能力竞争”正式进入“工程可用性竞争”。

2. **几何基础模型被当作“上游先验”，通过轻量适配补齐度量尺度和任务能力。**
   WildHSR 不改基础模型本身，而是用尺度伪标签预训练 Scale Readout 再微调适配器，补足“度量尺度”与“持续人物身份”；FounRef 直接冻结单目基础先验，用稀疏 LiDAR 锚点做保结构度量精化，且免训练、模块化。两者共同指向一个方向：基础模型负责通用几何先验，任务落地靠“薄适配层 + 稀疏监督”。

3. **4D/动态表示从纯重建扩展到下游任务：伪标签、变化分类、语义分割。**
   SplatLabel 用 4D 高斯显式时间流形建模基元轨迹与生命周期，从 2D 基础模型蒸馏语义先验，生成带置信度的 LiDAR 分割伪标签与语义占据栅格；PlenoCI 从 3DGS 解析全光导数构造对欠约束表示鲁棒的变化特征，做几何/外观变化分类；PePESeg3D 把感知先验同时注入几何重建与对比特征学习。动态高斯表示正在成为“数据引擎”和“感知中间层”，而不仅是可视化载体。

4. **多模态/跨视角融合成为机器人感知的默认设定，而非可选项。**
   M3GD 组合冻结的 2D 图像与 3D 点云基础模型，利用投影后特征共享空间结构做 Camera–LiDAR 生成式 NVS；Underwater C3-JEPA 用 held-out-view attention 融合多相机证据做对象中心世界模型；ReVNM 把远程监控相机同时当作观测源与隐式地图，并用 exo2ego 模块预测机器人自身视角深度。多模态与跨视角的证据融合已经是机器人场景的基线需求。

5. **数据构建与评测本身被当作方法贡献：数据集、仿真框架、度量指标齐出。**
   Ego-Exo4D-HM 为 Ego-Exo4D 提供稠密 4D 人体运动重建数据集与流程；众包建图论文提出 GOSPAM 差异度量并系统评估车队规模影响；SplatLabel 将伪标签评估重述为选择性分类并采用广义风险-召回指标；水下巡检论文也构建了配套数据与多模态采集流程。说明该领域正在从“算法单点突破”转向“数据—指标—流程”一体化建设。

#### 技术路线观察

- **几何基础模型方向**：核心矛盾是“基础模型强但尺度不确定、任务能力缺失”。FounRef 与 WildHSR 都选择**不动主干、只加读出/适配**的路线，分别用稀疏 LiDAR 锚点验证和网络视频尺度伪标签来补足度量。共同点是强调**免训练或轻量微调、跨域开箱即用**，并把“锚点校验/伪标签质量”作为关键工程问题。
- **3D/4D 重建方向**：出现明显分化。一条是**规模化与效率**（OceanXL 分块、AdaTex4D 容量分配、COSA-GS 压缩），另一条是**结构化参数化**（心肌重建把不规则三维重建转为共享 UV 域的坐标场补全）。前者面向大场景/实时/存储，后者面向医学等低数据、强解剖约束场景；4D 方向则普遍依赖显式时间流形或形变场来建模动态。
- **神经场景表示方向**：3DGS 正在被“二次开发”为多种角色——可压缩表示、可解析特征源（PlenoCI）、可注入语义先验的几何（PePESeg3D）、可承载伪标签的 4D 表示（SplatLabel）。技术侧重点从“如何拟合场景”转向“如何从表示中稳定地抽取可复用信号”。
- **机器人/AR 应用方向**：重点是**在缺少标记、缺少预建地图、缺少接触传感器条件下**完成感知与规划。ReVNM 用远程相机+学习合成解决数据稀缺；RWM 把规划直接嵌入表示几何，推理时构造潜在路径并用逆动力学恢复动作；Underwater C3-JEPA 与水下巡检都强调无接触/无标记；S2Planner 则聚焦端到端规划并主动披露 navtest 选型的偏差风险。

#### 值得优先阅读的论文

1. **COSA-GS（2609.30245）**：同时处理压缩性能与跨平台 bit-exact 熵解码，这是 3DGS 真正落地的硬门槛，且架构简单（仅线性变换+激活）、方法可迁移性强。
2. **Only What Was Seen（2609.28997）**：把球谐压缩统一到观测 Gram 矩阵下的率失真框架，降阶/阶数分配/向量量化都能纳入同一度量，方法学价值高，可能成为后续压缩工作的通用工具。
3. **FounRef（2609.29224）** 与 **WildHSR（2609.29106）**：两者共同定义了“冻结几何基础模型 + 稀疏/伪标签适配”的范式，一个偏深度精化、一个偏 4D 人物场景重建，对照阅读可快速把握基础模型落地路线。
4. **M3GD（2609.30056）**：用冻结的图像与点云基础模型、不加跨模态预训练翻译器就完成 Camera–LiDAR NVS，对多模态表示复用有直接启发。
5. **SplatLabel（2609.29836）**：把 4D 高斯当作伪标签引擎，且重定义了评估指标，兼顾表示、语义与数据闭环，适合作为“表示即数据工具”路线的入口。

（Ego-Exo4D-HM 因摘要缺少方法细节，暂不列入优先精读，但值得作为数据资源跟踪。）

#### 可能的研究机会

- **压缩与几何先验结合**：将 COSA-GS 的 anchor 因果分解与 Only What Was Seen 的观测 Gram 矩阵度量结合，在 anchor 层面做率失真最优的球谐/属性分配，可能优于现有独立压缩策略。
- **基础模型适配层的统一化**：FounRef 的锚点校验与 WildHSR 的尺度伪标签可以合并为“通用度量读出模块”，支持 LiDAR、人体姿态、已知尺度物体等多种锚点源，且保持模块可替换。
- **4D 表示的语义—几何联合自监督**：PePESeg3D 的“感知先验注入上游几何”与 SplatLabel 的“4D 时间流形伪标签”可以组合，用语义一致性反哺动态几何，缓解弱监督下的几何漂移。
- **跨视角世界模型与远程导航的结合**：Underwater C3-JEPA 的多视角 token 融合与 ReVNM 的 exo2ego 都面临“非自身视角观测导致视野受限”问题，可探索共享的视角对齐与隐式地图表示。
- **欠约束表示下的稳定性评测**：PlenoCI 指出的“独立优化重建收敛到不同基元配置”问题，可能同样影响 COSA-GS、AdaTex4D 等压缩/剪枝方法的可复现评测，值得建立统一的欠约束鲁棒性基准。
- **数据整理作为可学习方法**：众包建图的 GOSPAM 与海事 PTZ 视频的上下文感知采样都属“

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-29T14:04:22-04:00
**Total number of papers:** 61
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

#### 2026-09-28 - Many Eyes, One World: Feed-Forward 3D Reconstruction from Mixed Cameras

**Authors:** Qiaoge Li, Yifan Zhan, Haijun Yang, Haiyang Liu, Yiyi Cai, Chenchi Luo
**Links:** [abs](https://arxiv.org/abs/2609.35658) - [pdf](https://arxiv.org/pdf/2609.35658)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>Abstract</summary>

Real-world capture is heterogeneous: perspective, fisheye, and $360^\circ$ panoramic images can coexist within a single reconstruction task, yet most feed-forward 3D reconstruction models assume perspective imagery and a uniform input representation. Recent models handling several camera types are either informed of the camera type for each view or reconstruct one image pair at a time. No single-pass method reconstructs mixed-camera tuples containing full panoramas from images alone. We present MEOW, a feed-forward system that jointly reconstructs metric pointmaps and camera poses from one N-view tuple mixing perspective, fisheye and full-panorama images, in a single forward pass from images alone: no calibration, distortion parameters, camera-type labels or poses are supplied for any view. Our guiding design philosophy is to treat heterogeneous-camera reconstruction as a data-adaptation problem rather than an architectural redesign. MEOW retains a perspective-pretrained backbone and learns heterogeneous cameras entirely from a procedural data engine, which renders each scene across a continuous manifold of camera models with exact rays and depth, and certifies covisibility for every camera-sampled training tuple. Trained on synthetic tuples only, MEOW transfers zero-shot to real captures: on heterogeneous 2D3DS tuples it achieves 79.9 mAA@30 against 53.8 for Wid3R given the camera type of every view; on our laser-scanned mixed-camera benchmark it registers every four-view mixed tuple with 79.4 AUC@30. The data engine, benchmark, and complete evaluation pipeline will be released.

</details>

#### 2026-09-28 - ReSS: Residual-Restoring Sparse Attention for 3D Vision Transformers

**Authors:** Yongsung Kim, Jaehoon Lee, Minjun Park, Wooseok Song, Hun Hwangbo, Sungroh Yoon
**Links:** [abs](https://arxiv.org/abs/2609.35593) - [pdf](https://arxiv.org/pdf/2609.35593)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>Abstract</summary>

3D vision transformers such as VGGT predict camera poses and scene geometry from multi-view images in a single forward pass, but their global attention over all concatenated view tokens dominates computation as the number of views grows. To reduce this cost, SparseVGGT and HeSS sparsify attention at the block level, and both retain blocks with high attention probability. However, we observe that attention probability poorly predicts how much the model's behavior actually changes when a block is removed, and we show that this mismatch is why performance collapses as sparsity increases. In this paper, we propose ReSS (ReSidual-ReStoring Sparse Attention), which recasts block selection from a problem of maximizing the retained attention mass to one of minimizing the drift that sparsification leaves in the residual stream. We introduce a drift score that quantifies how much each block shifts the residual, and, since the drift of a drop set depends on the directions of the contribution vectors rather than on their magnitudes alone, an iterative residual restoration procedure that refines the drop set as a whole. Across three backbones and five datasets, ReSS preserves dense performance better than prior methods at matched sparsity. Two further results support drift as the quantity that governs the cost of sparsification: maximizing drift degrades performance faster than random selection, and plotted against realized drift instead of sparsity, all methods fall approximately onto a single curve. Code is available at https://github.com/libary753/ReSS.

</details>

#### 2026-09-24 - FounRef: Robust, Structure-Preserving, and Fast Metric Refinement of Frozen Monocular Foundation Priors with Sparse Anchors

**Authors:** Dan Halperin, Mirko Mählisch
**Links:** [abs](https://arxiv.org/abs/2609.29224) - [pdf](https://arxiv.org/pdf/2609.29224)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** depth prediction, metric depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FounRef: Robust, Structure-Preserving, and Fast Metric Refinement of Frozen Monocular Foundation Priors with Sparse Anchors
- 作者：Dan Halperin, Mirko Mählisch
- 出版日期：2026-09-24T08:32:29Z
- 分类：主分类为 Geometry Foundation Models；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.29224 ；PDF https://arxiv.org/pdf/2609.29224

### 一句话总结
FounRef 是一种免训练方法，通过稀疏度量锚点对冻结的单目基础模型先验进行全局与局部度量校正，在保持几何结构的同时输出稠密度量深度，并在域外数据上实现更低误差、更低表面法向噪声和更快推理。

### 研究问题
从相机获取稠密度量深度对现实三维应用很重要，但同时实现精度、可靠表面几何和快速推理仍然困难。单目基础模型提供丰富、可迁移的几何先验，但缺乏可靠的度量尺度；深度补全网络虽能恢复度量深度，却可能牺牲几何保真度、跨域鲁棒性或速度。论文关注如何在不进行任务特定训练的前提下，将冻结的单目基础先验与稀疏度量锚点对齐，得到稠密度量深度。

### 核心思路/方法
FounRef 是一种免训练方法，用于将冻结的单目基础先验与稀疏度量锚点对齐以产生稠密度量深度。其设计是模块化的：深度先验、锚点来源和精化求解器都可以独立替换。论文实例化时使用 MoGe-2 和 LiDAR 锚点。方法会针对先验的稠密深度预测验证每个锚点，拒绝由跨传感器错位引起、仅靠几何过滤器无法检测的不一致锚点。随后通过保持结构的求解器施加全局和局部度量校正，保留先验的细粒度几何。FounRef 不需要任务特定训练，可在陌生相机和场景中开箱即用。

### 主要贡献
- 提出 FounRef，一种免训练、模块化的稠密度量深度精化方法，可独立替换深度先验、锚点来源和精化求解器。
- 以 MoGe-2 与 LiDAR 锚点进行实例化，并通过对先验稠密深度预测验证锚点，拒绝跨传感器错位导致的不一致。
- 通过保持结构的全局与局部度量校正，在获得度量深度的同时保留先验的细粒度几何。
- 在域外数据上，相比先进深度补全网络 DMD3C，实现最高降低 24% 的深度误差、降低 92% 的表面法向噪声，以及接近 15 倍的推理加速。
- 将度量对齐与几何预测解耦，使方法可直接受益于未来基础模型和度量传感器的进展。

### 局限性
摘要未提供足够信息。摘要未给出具体失败场景、对锚点稀疏程度或质量的敏感性、跨传感器设置范围、计算资源需求细节，也未提供与更多基线或数据集的完整对比。

### 阅读优先级
高。理由：该工作针对稠密度量深度的精度、几何保真与速度权衡提出免训练模块化方案，并在摘要中报告了相对先进深度补全网络的显著定量改进；对关注单目基础模型度量对齐、深度补全、跨域鲁棒性和三维视觉应用的研究者有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Dense metric depth from cameras is essential to real-world 3D applications, yet achieving accuracy, faithful surface geometry, and fast inference simultaneously remains challenging. Monocular foundation models provide rich, transferable geometric priors but lack reliable metric scale, while depth-completion networks recover metric depth at the cost of geometric fidelity, cross-domain robustness, or speed. We present FounRef, a training-free method that aligns a frozen monocular foundation prior with sparse metric anchors to produce dense metric depth. FounRef is modular by design: its depth prior, anchor source, and refinement solver can each be replaced independently. We instantiate FounRef with MoGe-2 and LiDAR anchors. FounRef validates each anchor against the prior's dense depth prediction, rejecting inconsistencies caused by cross-sensor misalignment that geometry-only filters cannot detect. It then applies global and local metric corrections through a structure-preserving solver, retaining the prior's fine-grained geometry. FounRef requires no task-specific training and operates out of the box across unfamiliar cameras and scenes. On out-of-domain data, it delivers up to 24% lower depth error, 92% lower surface-normal noise, and almost 15x faster inference than DMD3C, a state-of-the-art depth-completion network. By decoupling metric alignment from geometry prediction, FounRef provides an accurate, geometrically faithful, and efficient approach to dense metric depth that can directly benefit from future advances in foundation models and metric sensors.

</details>

#### 2026-09-23 - Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces

**Authors:** Andrew Bond, Ege Erdem Özlü, Tuna Çimen, Ilkin Umut Melanlioglu, Tolga Birdal, Erkut Erdem, Aykut Erdem
**Links:** [abs](https://arxiv.org/abs/2609.27988) - [pdf](https://arxiv.org/pdf/2609.27988)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces
- 作者：Andrew Bond, Ege Erdem Özlü, Tuna Çimen, Ilkin Umut Melanlioglu, Tolga Birdal, Erkut Erdem, Aykut Erdem
- 出版日期：2026-09-23T12:17:02Z
- 分类：Geometry Foundation Models（主要类别）；次要类别未提供
- 链接：摘要链接 https://arxiv.org/abs/2609.27988 ；PDF 链接 https://arxiv.org/pdf/2609.27988 ；项目页 https://cyberiada.github.io/TaskInducedViTs/

### 一句话总结
论文指出 Vision Transformer 特征空间中常用的欧氏距离或余弦相似度隐含“各方向同等重要”的假设，转而用任务诱导的拉回度量刻画特征空间几何，并提出可学习低秩近似的 Spectral Pullback Network 及用于 token 剪枝的重要性头。

### 研究问题
- ViT 特征空间上的方法通常依赖欧氏距离或余弦相似度，默认所有方向同等有意义，但摘要指出没有理由相信真实任务几何具有该性质。
- 任务敏感的特征空间几何由拉回度量 \(g(F) = J(F)^\top J(F)\) 给出，其中 \(J\) 是解码器输出相对于特征的雅可比矩阵，解码器输出被送入任务特定距离。
- 在现代规模下存储完整 \(g\) 不可行；对于深度图等稠密输出，连构造 \(J\) 都不切实际。
- 因此核心问题是：能否学习该度量的低秩近似，以及这种低秩近似是否可学是否取决于模型—解码器组合。

### 核心思路/方法
- 使用任务敏感的拉回度量 \(g(F) = J(F)^\top J(F)\) 描述 ViT 特征空间的真实任务几何。
- 提出一种无矩阵诊断量 \(\kappa_{cap}(r)\)，可用少量雅可比向量积计算，用于判断低秩近似是否可学，并刻画其依赖于模型—解码器对。
- 对可处理的模型—解码器对，提出 Spectral Pullback Network（SPN），通过随机幂迭代学习度量的低秩版本。
- 将 SPN 蒸馏为一个约 310K 参数的重要性头，直接从特征预测 token 重要性。
- 当雅可比谱过于分散、不适合低秩近似时，摘要提出让解码器输入特征通过 VAE 瓶颈以恢复可处理性。
- 在 DPT、DINOv2、CLIP、VGGT 骨干上，用 \(\kappa_{cap}(r)\) 预测哪些学习度量架构可行。
- 几何 token 剪枝在 DPT 深度任务、剪枝比例 0.5 下，将基于 ToMe 的 token 选择带来的额外深度误差降低 25%，且不微调 ViT。

### 主要贡献
- 指出现有 ViT 特征空间方法默认欧氏或余弦几何的假设问题，并引入任务诱导的拉回度量作为任务敏感几何描述。
- 提出可计算少量雅可比向量积的无矩阵诊断 \(\kappa_{cap}(r)\)，用于判断低秩度量近似是否可学，并说明其取决于模型—解码器对。
- 提出 Spectral Pullback Network（SPN），用随机幂迭代学习低秩度量，并蒸馏为约 310K 参数的重要性头。
- 在多个骨干上验证 \(\kappa_{cap}(r)\) 对学习度量架构可行性的预测作用。
- 报告重要性头在 DINOv2 CLS 上达到 Spearman \(\rho = 0.998\)，并在 DPT 深度任务上以几何 token 剪枝降低 ToMe 式 token 选择的额外深度误差 25%。

### 局限性
- 摘要未提供足够信息说明方法在非视觉任务、其他模态或更广泛数据集上的泛化能力。
- 摘要未提供足够信息说明 \(\kappa_{cap}(r)\) 的计算成本、超参数敏感性或失败边界。
- 摘要未提供足够信息说明 VAE 瓶颈恢复可处理性的具体代价、精度损失或适用范围。
- 摘要未提供足够信息说明重要性头在 CLS 之外的 token 类型、不同剪枝比例或不同任务上的表现。
- 摘要未提供足够信息说明是否与微调方法、其他 token 剪枝方法进行了全面对比。
- 摘要未提供足够信息说明低秩近似与完整度量之间的理论误差界。

### 阅读优先级
高。理由：论文直接针对 ViT 特征空间几何这一基础假设，提出可诊断低秩可学性的 \(\kappa_{cap}(r)\)、可学习度量的 SPN 与轻量重要性头，并在 DPT、DINOv2、CLIP、VGGT 上给出验证和深度任务剪枝提升；对关注 ViT 特征几何、token 剪枝与任务感知表示的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Methods operating on Vision Transformer (ViT) feature spaces typically rely on Euclidean distance or cosine similarity. This assumes that every direction is equally meaningful, but there is no reason to believe the true task geometry has this property. The task-sensitive geometry of the feature space is given by the pullback metric $g(F) = J(F)^\top J(F)$, where $J$ is the Jacobian of the decoder's output fed to a task-specific distance, with respect to the features. Storing the full $g$ is infeasible at modern scales, and for dense outputs such as depth maps even forming $J$ is impractical. We show that whether a low-rank approximation of this metric can be learned depends on the model-decoder pair, and we characterize this with a matrix-free diagnostic $κ_{cap}(r)$ computable with a low number of Jacobian-vector products. For tractable pairs, we develop the Spectral Pullback Network (SPN), which learns a low-rank version of the metric from randomized power iteration, and we distill it into a $310$K-parameter importance head that predicts token importance directly from the features. When the Jacobian spectrum is too spread out for a low-rank approximation, passing the decoder's input features through a VAE bottleneck can restore tractability. Across DPT, DINOv2, CLIP, and VGGT backbones, $κ_{cap}(r)$ predicts which learned-metric architectures are viable. The importance head reaches Spearman $ρ= 0.998$ on DINOv2 CLS, and our geometric token pruning reduces the additional depth error of ToMe-based token selection by $25\%$ on DPT depth at prune ratio $0.5$, without fine-tuning the ViT. Project page: https://cyberiada.github.io/TaskInducedViTs/

</details>

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-28 - RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts

**Authors:** Jin Hyun Kim, Min Young Kim, Soohwan Song, Daekyum Kim
**Links:** [abs](https://arxiv.org/abs/2609.35311) - [pdf](https://arxiv.org/pdf/2609.35311)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, 4D Gaussian, world model

<details>
<summary>Abstract</summary>

Action-conditioned video world models predict future robot interactions from multiple cameras, yet their outputs remain disparate video collections rather than a shared metric scene queryable across viewpoints and time. While existing 4D reconstruction methods offer a path to spatialize these predictions, independently reconstructing and merging each camera stream fails to enforce cross-view consistency. This limitation is particularly detrimental when combining moving robot-mounted cameras with fixed external views. To address this, we introduce RoGSW4RLD, a feed-forward framework that lifts synchronized multi-camera rollouts into a unified, time-queryable metric 4D Gaussian field. Rather than learning a separate geometric transition model, RoGSW4RLD directly reconstructs the visual future generated by existing world models. Its core innovation is a two-stage architecture: Stage 1 jointly forms the metric 4D field by fusing cross-view evidence with robot-specific articulated geometry and kinematics, while Stage 2 refines the field's geometry and appearance while strictly preserving the initial temporal displacements. Evaluated on 256 held-out DROID episodes, RoGSW4RLD significantly outperforms camera-wise reconstruction with calibrated merging, improving novel-view PSNR by 2.15 dB, reducing depth AbsRel by 47%, and lowering robot displacement error by 61%. These robust gains extend to action-conditioned Cosmos 3 rollouts, demonstrating that predicted video futures can be successfully translated into consistent, spatially queryable 4D metric representations.

</details>

#### 2026-09-24 - Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures

**Authors:** Abhiram Maddukuri, Georgios Pavlakos
**Links:** [abs](https://arxiv.org/abs/2609.30187) - [pdf](https://arxiv.org/pdf/2609.30187)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion reconstruction, embodied AI

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures
- 作者：Abhiram Maddukuri, Georgios Pavlakos
- 出版日期：2026-09-24T17:30:36Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2609.30187) / [PDF](https://arxiv.org/pdf/2609.30187) / [项目页](https://abhiram824.github.io/egoexo4d_human_meshes)

### 一句话总结
针对 Ego-Exo4D 仅提供稀疏 3D 人体姿态标注的问题，本文构建了大规模 4D 人体运动重建数据集 Ego-Exo4D-HM，并公开了配套的重建流程。

### 研究问题
Ego-Exo4D 虽然提供了同步的自我中心与多视角外中心视频，是技能学习与评估、程序性活动理解以及具身 AI 的丰富资源，但其自带的人体标注仅有稀疏 3D 姿态。从这些多视角拍摄中重建稠密的人体运动并非易事。因此，本文关注的核心问题是：如何为 Ego-Exo4D 的拍摄数据提供稠密的 4D 人体运动重建，并给出可复用的重建方案。

### 核心思路/方法
摘要仅说明本文提出了 Ego-Exo4D-HM——一个面向 Ego-Exo4D 拍摄数据的大规模 4D 人体运动重建数据集，并同时发布了配套的重建流程（reconstruction pipeline）。摘要未提供足够信息说明该重建流程的具体技术细节、网络结构、优化策略或监督方式。

### 主要贡献
- 提出 Ego-Exo4D-HM：面向 Ego-Exo4D 拍摄数据的大规模 4D 人体运动重建数据集。
- 发布配套的人体运动重建流程。
- 公开代码、数据集与文档（项目页链接已给出）。

摘要未提供足够信息说明该数据集的具体规模、覆盖范围、精度指标或与稀疏姿态标注的定量对比。

### 局限性
摘要未提供足够信息说明方法或数据集的局限性、失败情形、计算成本与精度上限。

### 阅读优先级
中。理由：该工作面向 4D 人体运动重建与自我-外中心多视角数据这一明确任务，对从事人体运动捕捉、具身 AI 与多视角重建的研究者具有直接参考价值；但摘要内容较简短，未给出方法细节与量化结果，因此难以仅凭摘要判断其技术新颖性与性能水平，优先级定为中。

</details>

<details>
<summary>Abstract</summary>

Ego-Exo4D is a large-scale dataset providing synchronized egocentric and multi-view exocentric video, a rich resource for skill learning and assessment, procedural activity understanding, and embodied AI. However, the dataset ships with only sparse 3D human pose annotations, and reconstructing dense human motion from its multi-view captures is nontrivial. To this end, we present Ego-Exo4D-HM, a large-scale dataset of 4D human motion reconstructions for Ego-Exo4D's captures, and release the accompanying reconstruction pipeline. The code, dataset, and documentation can be found at https://abhiram824.github.io/egoexo4d_human_meshes.

</details>

#### 2026-09-24 - ADATEX4D: adaptive texture capacity allocation for 4D gaussian splatting

**Authors:** De Jiang, Peiqiang Wang, Kehong Yuan, Shaohua Ma
**Links:** [abs](https://arxiv.org/abs/2609.29963) - [pdf](https://arxiv.org/pdf/2609.29963)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ADATEX4D: adaptive texture capacity allocation for 4D gaussian splatting
- 作者：De Jiang, Peiqiang Wang, Kehong Yuan, Shaohua Ma
- 出版日期：2026-09-24T15:19:23Z
- 分类：Primary: Dynamic / 4D Reconstruction；Secondary: Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.29963 ；PDF https://arxiv.org/pdf/2609.29963

### 一句话总结
AdaTex4D 为基于形变的 4D 高斯泼溅引入自适应纹理容量分配模块，让每个高斯的打包 RGBA 三平面按可见性归一化的屏幕空间梯度与形变后的局部尺度独立增长两轴，从而在保持重建质量的同时将纹理存储减少一半以上。

### 研究问题
带纹理的高斯能提升局部外观表达能力，但为每个基元分配相同的纹理分辨率，会在低细节或弱可见区域浪费存储。论文要解决的问题是：如何在 4D 高斯表示中更高效地分配局部外观容量。

### 核心思路/方法
- 面向基于形变的 4D Gaussian Splatting，提出自适应纹理容量模块 AdaTex4D。
- 每个高斯携带打包的 RGBA 三平面（packed RGBA triplanes）。
- 三平面的两个轴根据两种信号独立增长：可见性归一化的屏幕空间梯度，以及形变后的局部尺度。
- 由此实现动态、各向异性的纹理分配，而非对所有基元统一纹理分辨率。

### 主要贡献
- 提出 AdaTex4D，一个用于基于形变的 4D 高斯泼溅的自适应纹理容量模块。
- 在 N3DV 和 PanopticSports 上，纹理存储减少一半以上，同时保持重建质量。
- 在固定内存预算下，自适应分配相比统一纹理分配提升质量，并降低整体模型内存与峰值内存。
- 结果表明，动态、各向异性的纹理分配是 4D 高斯表示中分配局部外观容量更高效的方式。

### 局限性
摘要未提供足够信息。摘要未提及方法的具体失败情形、对特定场景或运动类型的敏感性、额外计算开销的细节，也未给出定量指标、消融实验细节或与更多基线方法的比较，以上均无法基于现有信息判断。

### 阅读优先级
高。理由：该论文直接针对 4D 高斯泼溅中纹理容量分配效率这一明确问题，摘要给出了存储减半以上、固定内存预算下质量提升与内存下降等具体结论，且发表于 Dynamic / 4D Reconstruction 方向，对该方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Textured Gaussians improve local appearance capacity, but assigning the same texture resolution to every primitive wastes storage on low-detail or weakly visible regions. We introduce AdaTex4D, an adaptive texture-capacity module for deformation-based 4D Gaussian Splatting. Each Gaussian carries packed RGBA triplanes whose two axes grow independently according to visibility normalized screen-space gradients and deformed local scales. Experiments on N3DV and PanopticSports show that AdaTex4D reduces texture storage by more than half while preserving reconstruction quality. Under fixed memory budgets, adaptive allocation also improves quality over uniform texture assignment and reduces overall model and peak memory. These results show that dynamic, anisotropic texture allocation provides a more efficient way to distribute local appearance capacity in 4D Gaussian representations.

</details>

#### 2026-09-24 - SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting

**Authors:** Nitya Nanvani, Andras Palffy, Holger Caesar
**Links:** [abs](https://arxiv.org/abs/2609.29836) - [pdf](https://arxiv.org/pdf/2609.29836)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting
- 作者：Nitya Nanvani, Andras Palffy, Holger Caesar
- 出版日期：2026-09-24T14:05:59Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要 https://arxiv.org/abs/2609.29836 ；PDF https://arxiv.org/pdf/2609.29836

### 一句话总结
SplatLabel 提出一种基于 4D 高斯表示的自动化流程，用于从 2D 视觉基础模型蒸馏语义先验，从而生成带预测置信度的 LiDAR 分割伪标签和任意体素分辨率的语义占据栅格。

### 研究问题
论文关注如何将 2D 视觉基础模型的先验自动转化为稳健的 3D 语义伪标签。摘要指出，通常这一转化需要复杂的启发式方法或多模型集成；同时，动态环境中的运动物体跟踪与物体出现/消失的界定也构成挑战。SplatLabel 试图在无需预标注 3D 边界框的情况下，处理动态环境并完成 LiDAR 分割与语义占据预测的伪标签生成。

### 核心思路/方法
SplatLabel 以 4D 高斯表示为核，通过显式的时间流形建模单个 3D 基元的轨迹和生命周期，从而跟踪运动主体并严格定义物体出现与消失，且完全不需要预标注 3D 边界框。该表示由结构与语义先验支撑：一方面通过虚拟深度图整合 360 度 LiDAR，以引导未观测区域的场景几何；另一方面不依赖特定领域的提示工程，而是直接从 2D 模型蒸馏连续软概率，以在时间和空间上消解语义歧义。此外，论文将伪标签评估重新表述为选择性分类任务，并采用广义风险-召回指标，以反映精度与召回之间的真实权衡。

### 主要贡献
- 提出 SplatLabel，一种利用 4D 高斯表示从 2D 视觉基础模型自动提取 LiDAR 分割伪标签和语义占据栅格的流程，并带有预测置信度。
- 通过显式时间流形建模 3D 基元的轨迹与生命周期，实现动态主体的准确跟踪以及物体出现/消失的严格界定，且无需预标注 3D 边界框。
- 通过虚拟深度图整合 360 度 LiDAR 来引导未观测区域的场景几何，并直接蒸馏 2D 模型的连续软概率以解决语义歧义，避免领域特定提示工程。
- 将伪标签评估重新表述为选择性分类任务，使用广义风险-召回指标来反映精度与召回的权衡。
- 摘要称在 SemanticKITTI 上，SplatLabel 在多个召回水平上持续优于当前最优基线，为 3D LiDAR 分割和占据预测建立了稳健框架。

### 局限性
摘要未提供足够信息。未提及计算开销、对特定数据集的依赖程度、在 SemanticKITTI 之外场景的泛化能力、失败案例或实现细节等潜在局限。

### 阅读优先级
高。理由：该论文涉及 4D 高斯表示、2D 基础模型到 3D 伪标签的蒸馏、动态场景跟踪以及伪标签评估指标重构，属于动态/4D 重建与神经场景表示交叉方向；摘要声称在 SemanticKITTI 上多个召回水平优于现有基线，若关注 3D 语义伪标签、LiDAR 分割或占据预测，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

While 2D Vision Foundation Models offer a pathway to automate 3D semantic pseudo-labelling, translating these priors into robust 3D representations typically requires complex heuristics or multi-model ensembles. We introduce SplatLabel, an automated pipeline that leverages a 4D Gaussian representation to extract LiDAR segmentation with predictive confidence, as well as semantic occupancy grids at arbitrary voxel resolutions. At its core, SplatLabel handles dynamic environments through an explicit temporal manifold that models the trajectories and lifespans of individual 3D primitives. This allows the system to accurately track moving actors and strictly define when objects appear and disappear, completely eliminating the need for pre-annotated 3D bounding boxes. To robustly support this dynamic tracking, the representation is grounded by structural and semantic priors: we guide scene geometry in unobserved regions by integrating 360-degree LiDAR via virtual depth maps, and rather than relying on domain-specific prompt engineering, we directly distill continuous soft probabilities from 2D models to inherently resolve semantic ambiguities over time and space. Finally, to accurately reflect the real-world trade-off between precision and recall, we reframe pseudo-label evaluation as a selective classification task using a generalized risk-recall metric. Experiments on SemanticKITTI demonstrate that SplatLabel consistently outperforms state-of-the-art baselines across multiple recall levels, establishing a highly robust framework for both 3D LiDAR segmentation and occupancy prediction.

</details>

#### 2026-09-23 - High Dynamic Range Video Reconstruction from Single-Exposure Raw Sequences

**Authors:** Tao Zhang, Peixian Su, Xingyu Gao, Yunhao Zou, Yu Lu, Zunjie Zhu, Bolun Zheng, Ying Fu, Chenggang Yan
**Links:** [abs](https://arxiv.org/abs/2609.27274) - [pdf](https://arxiv.org/pdf/2609.27274)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：High Dynamic Range Video Reconstruction from Single-Exposure Raw Sequences
- 作者：Tao Zhang, Peixian Su, Xingyu Gao, Yunhao Zou, Yu Lu, Zunjie Zhu, Bolun Zheng, Ying Fu, Chenggang Yan
- 出版日期：2026-09-23T03:01:47Z
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2609.27274

### 一句话总结
该论文提出 RawHDRV，一个面向单曝光 Raw 视频的端到端 HDR 重建框架，通过利用 Bayer 数据的线性响应与通道特性，在无需交替曝光或额外硬件的情况下缓解高光裁剪与暗部细节丢失问题。

### 研究问题
传统图像传感器动态范围有限，导致拍摄的低动态范围视频常出现高光裁剪和暗部细节丢失。现有交替曝光 HDR 方法会牺牲帧率并面临运动对齐困难，难以适用于真实拍摄场景。因此，如何从单曝光视频序列中高质量重建 HDR 视频是一个具有挑战性的问题。

### 核心思路/方法
论文提出 RawHDRV 端到端框架，核心在于利用 Bayer 数据的线性响应和通道特定特性：
- 采用通道分解的时间对齐与融合策略，分别处理 Bayer 各通道以利用其不同曝光特性，并结合曝光感知加权融合。
- 引入曝光互补性掩码引导的恢复模块，利用帧间曝光冗余自适应融合可靠信息并抑制饱和伪影。
- 提出掩码引导的颜色损失，结合归一化误差约束与梯度平滑以增强高光恢复。
- 同时构建了一个大规模移动端 Raw-HDR 视频数据集，并带有逐帧 HDR 标注。

### 主要贡献
- 提出 RawHDRV，一个面向单曝光 Raw 视频 HDR 重建的端到端框架。
- 设计通道分解时间对齐与融合策略及曝光感知加权融合。
- 引入曝光互补性掩码引导的恢复模块和掩码引导颜色损失。
- 构建带逐帧 HDR 标注的大规模移动端 Raw-HDR 视频数据集。
- 实验表明该方法在所有指标上达到当前最优，在极端曝光条件下具有更优的空间质量和时间稳定性。

### 局限性
摘要未提供足够信息。摘要中未说明方法的具体失败场景、计算开销、对特定硬件的依赖程度、数据集规模与多样性的详细限制，也未提及在非移动端设备或其他传感器上的泛化能力。

### 阅读优先级
中。理由：该工作针对单曝光 Raw 视频 HDR 重建这一具有实际价值的问题，提出了结合 Bayer 通道特性与掩码引导的完整框架，并构建了新数据集，且声称在所有指标上达到最优。但摘要未提供足够的实验细节、量化结果和局限性讨论，若读者关注 HDR 视频重建、Raw 域处理或动态场景重建，可作为相关方向的重要参考；若仅需泛读，则可暂列为中等优先级。

</details>

<details>
<summary>Abstract</summary>

Due to the limited dynamic range of conventional image sensors, captured low dynamic range (LDR) video often suffers from highlight clipping and shadow detail loss, making high-quality high dynamic range (HDR) reconstruction from single-exposure sequences highly challenging without alternating exposures or extra hardware. Alternating-exposure HDR methods sacrifice frame rate and struggle with motion alignment, making them impractical for real-world capture. To address this, we propose RawHDRV, an end-to-end framework for single-exposure Raw video HDR reconstruction, that fundamentally exploits the linear response and channel-specific characteristics of Bayer data. Specifically, it features a channel-decomposition temporal alignment and fusion strategy that processes Bayer channels separately to exploit their distinct exposure characteristics, together with exposure-aware weighted fusion. It further incorporates an exposure complementarity mask-guided restoration module that leverages inter-frame exposure redundancy to adaptively fuse reliable information and suppress saturation artifacts, and introduces a mask-guided color loss that combines normalized error constraints with gradient smoothing to enhance highlight recovery. Furthermore, we construct a large-scale mobile Raw-HDR video dataset with per-frame HDR annotations. Experiments show that our method achieves the state-of-the-art results in all metrics, demonstrating superior spatial quality and temporal stability under extreme exposure conditions. The code is available at https://github.com/supeixian/RawHDRV.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-28 - VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction

**Authors:** Conghan Yue, Yuanjie Chen, Yue Han, Ya Gao, Yunyan Xiao, WeiYao Zhang, Zhineng Chen
**Links:** [abs](https://arxiv.org/abs/2609.35134) - [pdf](https://arxiv.org/pdf/2609.35134)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, simulation

<details>
<summary>Abstract</summary>

Video editing has advanced substantially in recent years, with methods increasingly accounting for the visual consequences of edits, such as changes to shadows and occlusions. However, the physical consequences of edits, including changes to subsequent motion and interactions, remain less explored. We formulate this problem as physical counterfactual video editing (PCVE), which aims to generate a counterfactual video depicting the resulting motion and interactions given a source video, a physical edit, and its execution frame. PCVE is challenging because it requires understanding scene physics and inferring the downstream motion and interactions induced by a physical intervention, while paired factual and counterfactual data and dedicated evaluation metrics are lacking. We introduce VideoPhysEdit, a new training-free pipeline for PCVE in rigid-body scenes. It makes physical reasoning explicit through a novel physical scene reconstruction method that recovers a scene reproducing the observed motion and interactions under simulation, enabling the pipeline to apply physical edits as interventions and use the resulting trajectories to guide counterfactual video generation. We further construct PCVE-RigidBench, a synthetic benchmark with paired source and counterfactual target videos and physical ground truth, and introduce the Physical Edit Score. VideoPhysEdit achieves substantially higher physical edit accuracy than open-source methods and commercial models while maintaining competitive visual fidelity. Its Physical Edit Score is 0.376, the only positive score among the compared methods. Qualitative comparisons on real videos further show that VideoPhysEdit applies to real-world scenes and better depicts the downstream motion and interactions induced by the edits than the compared methods. Code: https://github.com/Hammour-steak/VideoPhysEdit

</details>

#### 2026-09-28 - LEGAU: Learning Semantic Gaussian Priors for Scalable Category-level Pose Estimation

**Authors:** Hongli Xu, Zhaowei Lu, Junwen Huang, Jiaqi Hu, Peter KT Yu, Benjamin Busam, Federico Tombari, Slobodan ilic
**Links:** [abs](https://arxiv.org/abs/2609.35046) - [pdf](https://arxiv.org/pdf/2609.35046)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Category-level 6D pose estimation from a single RGB-D observation is inherently under-constrained, since partial visible geometry must be interpreted together with a canonical object structure before a stable pose can be determined. We present LEGAU, a unified framework that jointly predicts NOCS correspondence, object pose and size, and a canonical Semantic Gaussian Field. Rather than treating reconstruction as a detached auxiliary task, LEGAU uses the Gaussian field as a category-conditioned structural prior that participates in multimodal feature fusion and provides global guidance for local pose reasoning. Conditioned on a categorical text embedding, LEGAU processes RGB-D observations through a transformer-based fusion module that integrates visual, geometric, and category-level cues, decoding the NOCS map, pose and size information and the Gaussian-based object representation. Extensive experiments on synthetic and real-world benchmarks show that this coupled pose-shape formulation achieves strong performance in a single-model multi-category setting, with up to 22\% on SOPE and competitive transfer to real-world data. These results highlight the benefit of jointly learning canonical correspondence, object shape, and pose alignment within a unified representation.

</details>

#### 2026-09-28 - Functional Hand Type Prior for 3D Hand Pose Estimation and Action Recognition from Egocentric View Monocular Videos

**Authors:** Wonseok Roh, Seung Hyun Lee, Won Jeong Ryoo, Jakyung Lee, Gyeongrok Oh, Sooyeon Hwang, Hyung-gun Chi, Sangpil Kim
**Links:** [abs](https://arxiv.org/abs/2609.34149) - [pdf](https://arxiv.org/pdf/2609.34149)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Current methods for egocentric view action recognition often face challenges in perceiving dynamic hand movements relying solely on geometrical or physical information. In this work, we effectively address this problem by gaining insights into the correlation between functional hand configurations and objects, which improves the detailed interpretation of real-world scenarios. To this end, we introduce a practical taxonomy of hand types based on the functioning perspective and utilize it for per-frame hand type labeling on existing datasets. We also propose a novel hand action recognition framework considering semantic details of the hand type as prior. This approach boosts the network's understanding of the continuous hand interaction throughout the action sequence. Our whole pipeline consists of three main modules: (1) Feature Extraction, (2) Egocentric Knowledge Module, which estimates 3D hand pose, object category, and hand type leveraging short-term cues, and (2) Egocentric Action Module, which aggregates per-frame knowledge, including text embeddings of hand type, over a longer time. In our extensive experiments with large-scale benchmarks, FPHA and H2O, our model outperforms current state-of-the-art methods, demonstrating its superior performance.

</details>

#### 2026-09-27 - EpiTransfer: Sparse, Training-Free Long-Range Depth Estimation from Temporal Monocular Aerial Frames

**Authors:** Diksha Aggarwal, Rutvik Dagadkhair, Sanjana Srivastava, Bradley Denby, Kevin Kochersberger
**Links:** [abs](https://arxiv.org/abs/2609.33939) - [pdf](https://arxiv.org/pdf/2609.33939)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, depth estimation

<details>
<summary>Abstract</summary>

Reliable 3D spatial understanding is essential for autonomous navigation, obstacle avoidance, and scene reconstruction. While state-of-the-art learned depth estimation techniques achieve high accuracy in-distribution, they often generalize poorly to novel viewpoints and altitudes. This paper presents a geometrically derived, training-free depth estimation method using epipolar transfer with only two monocular images and camera pose estimates. By leveraging camera motion to synthesize a virtual stereo pair with a freely chosen baseline, our approach transforms temporal correspondence into a stereo triangulation task while mitigating geometric degeneracies inherent to direct two-view triangulation. Validated across outdoor drone flights (to a maximum range of approximately 90\,m) and indoor OptiTrack environments against LiDAR ground truth, the method achieves an indoor AbsRel of 0.092 and $δ< 1.25$ of 0.940, comparable to direct triangulation (AbsRel 0.073) while retaining valid depth over a larger fraction of challenging scenes, and substantially outperforms off-the-shelf learning-based baselines such as ZoeDepth (AbsRel 0.225) and Depth Anything V2 (AbsRel 0.570), which are not trained or fine-tuned for this domain, with no training data required.

</details>

#### 2026-09-24 - Anatomy-Aligned Surface Field Learning for Myocardial Reconstruction from Sparse Short-Axis Cine MRI

**Authors:** Xiaohan Yuan, Xuan Yang, Qingya Li, Yangang Wang, Lei Li
**Links:** [abs](https://arxiv.org/abs/2609.29825) - [pdf](https://arxiv.org/pdf/2609.29825)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Anatomy-Aligned Surface Field Learning for Myocardial Reconstruction from Sparse Short-Axis Cine MRI
- 作者：Xiaohan Yuan, Xuan Yang, Qingya Li, Yangang Wang, Lei Li
- 出版日期：2026-09-24T13:58:16Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2609.29825 ；PDF https://arxiv.org/pdf/2609.29825

### 一句话总结
该论文提出一种解剖对齐的表面场学习框架，将心内膜与心外膜表面参数化到共享的环形-纵向 UV 域，从而把稀疏短轴电影 MRI 的不规则三维重建转化为结构化坐标场补全问题。

### 研究问题
患者特异性的 4D 心肌重建有助于定量功能评估、区域运动分析和基于仿真的建模。但常规采集的短轴（SAX）电影 MRI 在穿平面方向上采样稀疏，导致密集且解剖一致的心肌表面重建具有挑战性。

### 核心思路/方法
- 将心外膜和心内膜表面参数化到共享的环形-纵向 UV 域，把不规则三维重建转化为结构化的坐标场补全，并在受试者与心动相位之间建立显式对应。
- 将稀疏 SAX 轮廓编码为 UV 观测场。
- 采用覆盖感知采样，以提升对切片覆盖不完整的鲁棒性。
- 使用拓扑与失真感知学习，以保持环形连续性与局部表面质量。

### 主要贡献
- 提出解剖对齐的 UV 学习方法，用于稀疏电影 MRI 的心肌重建与心肌建模，作者称其具备准确、高效且对应关系感知的表示能力。
- 在三个公开电影 MRI 数据集上进行实验，报告所提方法持续优于代表性基于网格和隐式重建方法。
- 报告整体 Chamfer 距离：ACDC 为 2.887 mm，M&Ms 为 2.641 mm，M&Ms-2 为 2.810 mm。
- 重建序列保持心室功能，报告舒张末期容积误差为 3.3 mL，射血分数误差为 1.1%。
- 声明源代码将发布于 https://github.com/yuan-xiaohan/SAX2MyoSurf 。

### 局限性
- 摘要未提供足够信息说明方法在极端稀疏采样、切片缺失模式或不同病理群体中的失败情形与泛化边界。
- 摘要未提供足够信息说明计算效率的具体指标、训练与推理耗时、显存需求等。
- 摘要未提供足够信息说明三个数据集上对比方法的完整设置、统计显著性检验或消融实验细节。
- 摘要未提供足够信息说明 UV 参数化对心肌拓扑异常或配准误差的敏感性与处理策略。
- 摘要未提供足够信息说明心室功能指标之外的其他临床验证结果。

### 阅读优先级
高。理由：该工作直接针对稀疏短轴电影 MRI 的四维心肌重建这一具有临床与建模价值的问题，提出结构化的 UV 域学习思路，并给出多数据集定量结果与功能指标误差；同时涉及 3D 重建、解剖对应和稀疏观测补全，适合关注医学图像重建与心肌建模的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Patient-specific 4D myocardial reconstruction from cine MRI supports quantitative functional assessment, regional motion analysis, and simulation-based modeling. However, routinely acquired short-axis (SAX) cine MRI is sparsely sampled along the through-plane direction, making dense and anatomically consistent surface reconstruction challenging. In this study, we propose an anatomy-aligned surface learning framework that parameterizes the epicardial and endocardial surfaces on a shared circumferential-longitudinal UV domain. This formulation converts irregular 3D reconstruction into structured coordinate-field completion with explicit correspondence across subjects and cardiac phases. Sparse SAX contours are encoded as UV observation fields, coverage-aware sampling improves robustness to incomplete slice coverage, and topology- and distortion-aware learning preserves circumferential continuity and local surface quality. Experiments on three public cine MRI datasets showed that the proposed method consistently outperformed representative mesh-based and implicit reconstruction approaches, achieving overall Chamfer distances of $2.887$~mm on ACDC, $2.641$~mm on M\&Ms, and $2.810$~mm on M\&Ms-2. The reconstructed sequences also preserved ventricular function, with end-diastolic volume and ejection fraction errors of $3.3$~mL and $1.1 \%$, respectively. These results demonstrate that anatomy-aligned UV learning provides an accurate, efficient, and correspondence-aware representation for sparse cine MRI reconstruction and myocardial modeling. The source code will be available at https://github.com/yuan-xiaohan/SAX2MyoSurf.

</details>

#### 2026-09-24 - Markerless Multi-Modal Autonomous Robotic Inspection of Large Space Structures

**Authors:** Juan De Dios Alfaro, Arturo Ríos, David Rodríguez-Martínez, Carlos Pérez-del-Pulgar
**Links:** [abs](https://arxiv.org/abs/2609.29644) - [pdf](https://arxiv.org/pdf/2609.29644)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, geometric reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Markerless Multi-Modal Autonomous Robotic Inspection of Large Space Structures
- 作者：Juan De Dios Alfaro, Arturo Ríos, David Rodríguez-Martínez, Carlos Pérez-del-Pulgar
- 出版日期：2026-09-24T12:37:21Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2609.29644) / [PDF](https://arxiv.org/pdf/2609.29644)

### 一句话总结
该论文提出一种无标记、多模态的自主机器人巡检流程，以三维重建作为巡检支撑表示，在缺乏合作标记与先验信息的情况下采集空间相干数据并生成可用于视觉与几何评估的重建结果。

### 研究问题
未来轨道基础设施（如可展开天线、太阳能电站和大规模轨道平台）需要能在有限先验知识、无合作标记条件下运行的自主巡检系统。现有在轨服务方法通常依赖预定义轨迹、标准接口、基准标记或精确目标模型，面对大型、异构或部分未知的结构时扩展性受限。论文要解决的问题是如何在没有标记和准确目标模型的前提下，实现面向大型空间结构的自主巡检与多模态数据采集。

### 核心思路/方法
- 构建一个无标记的自主机器人巡检流程，将三维重建作为巡检的支撑性表示。
- 硬件系统为 Kinova Gen2 机械臂，末端安装多模态传感器头，包含 RGB-D 相机、热像仪和 2D LiDAR。
- 流程包括：估计近似巡检体积、生成视点、使用 MoveIt 规划无碰撞运动，并在 ROS2 中同步记录 RGB-D 图像、热数据和机器人位姿。
- 对候选重建方法进行评估以选择适用于该流程的实用方法，最终使用 Nerfacto 做几何重建，并使用 Thermal-Nerfacto 演示面向巡检的热感知渲染。

### 主要贡献
- 提出一种将三维重建作为巡检支撑表示的无标记自主巡检流程，面向大型非合作空间结构。
- 集成机械臂与 RGB-D、热像、2D LiDAR 多模态传感，实现视点生成、无碰撞运动规划和多模态数据同步记录。
- 通过候选重建方法评估选择 Nerfacto 与 Thermal-Nerfacto，展示了热感知渲染在巡检中的可行性。
- 在基于 Gazebo 的仿真器和初步实验室测试中进行验证，表明系统能自主获取空间相干的巡检数据并产生适用于视觉和几何评估的重建结果。

### 局限性
- 验证仅在基于 Gazebo 的仿真器和初步实验室测试中完成，摘要未提供在真实在轨环境或大型空间结构上的验证信息。
- 摘要未提供定量性能指标（如重建精度、巡检覆盖率、规划成功率、运行时间等）。
- 摘要未说明所生成视点对部分未知或异构结构的适应能力的具体边界。
- 摘要未提供与现有依赖标记或预定义轨迹方法的对比实验细节。
- 摘要未提供 Thermal-Nerfacto 热感知渲染结果的具体质量评估。
- 摘要未提供系统在通信延迟、计算资源受限或动态环境下的表现。
（以上未提及内容均因“摘要未提供足够信息”。）

### 阅读优先级
中。理由：该论文面向大型空间结构自主巡检这一具有明确应用价值的问题，并给出无标记、多模态、结合三维重建与运动规划的完整流程；但摘要仅报告仿真与初步实验室验证，未提供定量结果或与基线方法的对比，若读者关注在轨真实部署或性能评估，需要进一步阅读全文确认实验细节；若关注无标记巡检流程设计与多模态重建集成，则具有一定参考价值。

</details>

<details>
<summary>Abstract</summary>

Future orbital infrastructures, such as deployable antennas, solar farms, and large orbital platforms will require autonomous inspection systems able to operate with limited prior knowledge and without cooperative markers. Current on-orbit servicing approaches often rely on predefined trajectories, standard interfaces, fiducial markers or accurate target models, which limits scalability for large, heterogeneous or partially unknown structures. This paper presents a markerless autonomous robotic inspection pipeline in which 3D reconstruction is used as an inspection-support representation. The system integrates a Kinova Gen2 manipulator with an end-effector-mounted multimodal sensor head composed of an RGB-D camera, a thermal camera and a 2D LiDAR. The pipeline estimates an approximate inspection volume, generates viewpoints, plans collision-free motions with MoveIt, and synchronously records RGB-D images, thermal data, and robot poses in ROS2. Candidate reconstruction methods were evaluated to select a practical method for this pipeline, with Nerfacto used for geometric reconstruction and Thermal-Nerfacto used to demonstrate thermal-aware rendering for inspection. Validation in a Gazebo-based simulator and preliminary laboratory tests reveal that the proposed system can autonomously acquire spatially coherent inspection data and produce reconstructions suitable for visual and geometric assessment, representing a step towards inspection of large non-cooperative space structures.

</details>

#### 2026-09-24 - WildHSR: Metric Feed-Forward 4D People-Scene Reconstruction from a 3D Foundation Model

**Authors:** Jerrin Bright, John Zelek
**Links:** [abs](https://arxiv.org/abs/2609.29106) - [pdf](https://arxiv.org/pdf/2609.29106)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WildHSR: Metric Feed-Forward 4D People-Scene Reconstruction from a 3D Foundation Model
- 作者：Jerrin Bright, John Zelek
- 出版日期：2026-09-24T06:37:54Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.29106) | [PDF](https://arxiv.org/pdf/2609.29106)

### 一句话总结
WildHSR 通过轻量适配一个仅有尺度不确定性的 3D 基础模型，补足“度量尺度”与“持续人物身份”两个缺失输出，实现单目视频的前馈式度量级人物-场景 4D 重建。

### 研究问题
论文关注的核心矛盾是：部分最强的 3D 基础模型能在一次前向传播中恢复视频相机与几何，但其结果只具有“up-to-scale”（尺度不确定）性质。而联合的人物-场景重建需要两个该表示并未直接提供的输出：
1. **度量尺度（metric scale）**：如何从尺度不确定的基础表示中恢复真实世界尺度。
2. **持续人物身份（persistent person identity）**：如何在跨帧中保持同一人物的对应关系。

作者进一步提出：一个尺度不确定的基础表示，能否仅通过轻量适配同时支持这两者。

### 核心思路/方法
论文的方法围绕两个“读出”展开：

**1. 度量尺度读出（Scale Readout）**
- 精确度量标签稀缺，但无标注的野外视频充足。
- 利用精选网络视频中的人物进行初始化：一个带姿态的度量人体与 2D 关键点可给出近似的、闭式解形式的尺度伪标签。
- 这些伪标签用于预训练 Scale Readout，随后结合标准真实视频训练划分中的精确度量监督，与一个轻量 adapter 一起微调。
- 推理时，该 head 直接从基础模型 token 预测度量尺度，不再需要标尺或其教师。

**2. 人物身份读出**
- 作者单独探查预训练基础模型，发现其中间 query-key 特征有跨帧编码人物对应关系的证据。
- 在多数被评估的运动人物片段中，一个中间层 token 更偏好该人物，而非其离开的位置或其他人。
- 用一个很小的投影读取这种对应关系；它与度量骨盆运动、提议置信度一起，驱动对逐帧人体的 **dustbin-aware Sinkhorn association**。

**3. 整体流程**
- WildHSR 结合上述两个读出，从单目视频重建度量相机、场景与人物。
- 每个窗口以前馈方式预测；通过解析关联与 Sim(3) 组合连接各窗口。

### 主要贡献
- 提出 WildHSR，从单一尺度不确定的 3D 基础表示出发，通过轻量适配同时补足度量尺度与持续人物身份。
- 提出利用网络视频人物构造近似闭式尺度伪标签，并以此预训练 Scale Readout，再以精确度量监督微调。
- 发现并利用基础模型中间 query-key 特征中隐含的跨帧人物对应关系，以极小投影读取并驱动关联。
- 在 EMDB-2 上，WildHSR 是已发表比较中首个在 WA-MPJPE 与 RTE 上超过最佳优化类方法的前馈方法，并在三项世界坐标系指标上领先前馈方法。
- 在 RICH 上，其在 WA-MPJPE 与 W-MPJPE 上领先前馈式人物-场景方法。
- 完整流程在单张 GPU 上以 10.1 fps 运行。

### 局限性
摘要未提供足够信息。摘要未给出失败案例、适用场景限制、对基础模型具体类型或规模的依赖、伪标签质量的下界、以及在更广泛数据集上的泛化表现等信息。

### 阅读优先级
**高**。理由：该论文同时触及 3D 基础模型的尺度不确定性、人物-场景联合重建、跨帧身份关联与前馈式 4D 重建等关键问题，并声称在 EMDB-2 与 RICH 上取得相对优化类与前馈类方法的可比或领先结果，且给出 10.1 fps 的推理速度，对 3D 重建与多人场景理解方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D foundation models recover video cameras and geometry in one forward pass, but some of the strongest are up to scale. Joint people-scene reconstruction then requires two missing outputs: metric scale and persistent person identity. We ask whether one up-to-scale foundation representation can support both through lightweight adaptation. Exact metric labels are scarce, but unlabeled in-the-wild video is abundant. We use people in curated web video to initialise the solution: a posed metric body and 2D keypoints give an approximate, closed-form scale pseudo-label. These pseudo-labels pretrain a Scale Readout, which is then fine-tuned together with a lightweight adapter using exact metric supervision from standard real-video training splits. At inference the head predicts metric scale from foundation-model tokens, without the ruler or its teachers. For person identity, we probe the pretrained foundation model alone and find evidence that its intermediate query-key features encode person correspondence across frames. In most evaluated moving-person clips, a mid-layer token prefers that person over the vacated location and other people. A tiny projection reads this correspondence; together with metric pelvis motion and proposal confidence, it drives dustbin-aware Sinkhorn association of per-frame bodies. WildHSR combines both readouts to reconstruct metric cameras, scene and people from monocular video. Each window is predicted feed-forward; analytic association and Sim(3) composition connect windows. On EMDB-2, WildHSR is the first feed-forward method in the published comparison to beat the best optimization-based WA-MPJPE and RTE while leading feed-forward methods on all three world-frame metrics. On RICH, it leads feed-forward people-and-scene methods on WA-MPJPE and W-MPJPE. The complete pipeline runs at 10.1 fps on one GPU.

</details>

#### 2026-09-23 - PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting

**Authors:** Sungjae Choi, Seunghee Koh, Junmo Kim
**Links:** [abs](https://arxiv.org/abs/2609.28645) - [pdf](https://arxiv.org/pdf/2609.28645)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, monocular depth, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting
- 作者：Sungjae Choi, Seunghee Koh, Junmo Kim
- 出版日期：2026-09-23T18:00:11Z
- 分类：3D Reconstruction & Multi-view Geometry（主）；Neural Scene Representations & Rendering（次）
- 链接：摘要页 https://arxiv.org/abs/2609.28645 ；PDF https://arxiv.org/pdf/2609.28645 ；代码 https://github.com/BeCow5X5/PePESeg3D

### 一句话总结
PePESeg3D 将感知先验同时注入 3D 高斯泼溅的几何重建与对比特征学习，以提升多尺度 3D 分割与场景重建性能。

### 研究问题
现有 3D Gaussian Splatting（3DGS）多尺度分割方法存在两点不足：
1. 场景由高斯原语重建、多尺度分割特征被单独学习，导致几何不感知语义结构；
2. 特征学习依赖不完整的掩码监督。

### 核心思路/方法
提出 PePESeg3D 框架，将感知先验注入多尺度 3D 高斯分割流程，并同时用于对比特征学习和上游几何重建：
- **PePE Reconstruction**：引入单目深度与掩码约束，使物体结构具有语义一致性，从而获得对齐的几何。
- **PePE Contrastive Learning**：在已对齐的几何基础上，利用密集的深度-颜色线索和视图一致的中心点监督，补偿由 2D 基础模型获得的多尺度掩码的不完整性。

### 主要贡献
- 提出 PePESeg3D，将感知先验同时整合进几何优化与特征学习，用于准确的多尺度 3D 分割。
- 设计 PePE Reconstruction，通过单目深度与掩码约束保证语义连贯的物体结构。
- 设计 PePE Contrastive Learning，利用深度-颜色线索与视图一致的中心点监督，缓解多尺度掩码不完整问题。
- 在 SPIn-NeRF、LERF-Mask 和 NVOS 基准上的大量实验表明，该方法在多尺度分割与场景重建上均达到 state-of-the-art 性能。代码已公开。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、计算开销、对特定数据类型或基础模型质量的依赖程度等局限说明。

### 阅读优先级
**高**。理由：该工作针对 3DGS 多尺度分割中“几何与语义脱节”和“掩码监督不完整”两个明确问题，提出将感知先验同时用于几何与特征学习的方案，并在三个基准上声称取得 state-of-the-art；主题与 3D 重建、多视图几何及神经场景表示高度相关，且代码公开，适合优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent advancements in 3D Gaussian Splatting (3DGS) have extended its capabilities to multi-scale segmentation. Existing methods reconstruct a scene with Gaussian primitives and learn multi-scale segmentation features separately, which leaves the geometry unaware of semantic structure and the feature learning dependent on incomplete mask supervision. To address these limitations, we present PePESeg3D, a novel framework that injects perception priors into a multi-scale 3D Gaussian segmentation pipeline. To fully exploit perception priors, we integrate them not only into contrastive feature learning but also into the upstream geometry reconstruction. Specifically, PePE Reconstruction incorporates monocular depth and mask constraints to ensure semantically coherent object structures. Building on this aligned geometry, PePE Contrastive Learning leverages dense depth-color cues and view-consistent centroid supervision to compensate for the incompleteness of multi-scale masks obtained from a 2D foundation model. Extensive experiments on the SPIn-NeRF, LERF-Mask, and NVOS benchmarks demonstrate that PePESeg3D achieves state-of-the-art performance in both multi-scale segmentation and scene reconstruction, highlighting the importance of integrating perception priors into both geometry optimization and feature learning for accurate multi-scale 3D segmentation. Our code is available at https://github.com/BeCow5X5/PePESeg3D.

</details>

#### 2026-09-23 - Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

**Authors:** Preeti Chatterjee, Jin Lu, Jin Sun, Suchendra M. Bhandarkar
**Links:** [abs](https://arxiv.org/abs/2609.27509) - [pdf](https://arxiv.org/pdf/2609.27509)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, bundle adjustment, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM
- 作者：Preeti Chatterjee, Jin Lu, Jin Sun, Suchendra M. Bhandarkar
- 出版日期：2026-09-23T08:07:47Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.27509 ；PDF https://arxiv.org/pdf/2609.27509

### 一句话总结
KYS-SLAM 将语义、全景与运动先验转化为连续的特征匹配代价，用“惩罚而非剔除”的方式替代二值特征拒绝，作为 ORB-SLAM3 的模块化扩展以缓解立体视觉 SLAM 的数据关联退化与轨迹漂移。

### 研究问题
基于局部描述子的立体视觉 SLAM 面临三类问题：语义歧义、实例级混淆以及独立运动物体。这些问题都会破坏数据关联，并累积为轨迹漂移。

现有语义与动态 SLAM 方法通过二值特征剔除来应对，但作者认为这会以牺牲对应密度为代价来抑制离群点。论文主张“上下文不合理性”更适合表达为分级量，而不是排他性准则。

### 核心思路/方法
- 将 KYS-SLAM 定位为 ORB-SLAM3 的模块化扩展，用连续的对应调制替代特征剔除。
- 核心做法是把上下文证据重新表述为“对应代价”，应用于特征匹配阶段，并保持几何后端不变。
- 每个关键点被赋予语义、全景和运动先验，并通过分层兼容性公式融合。
- 融合中，语义类别与实例身份用于约束结构合理性；零样本运动分数用于降低位于独立运动物体上的特征权重。
- 该运动分数来自一个免训练模块：将深度感知的自运动模型拟合到背景光流，并通过自校准、覆盖感知的阈值对全景片段进行分类，从而只惩罚具有充分运动证据的片段，静态结构不被惩罚。
- 设计动机是：惩罚对应关系而不是丢弃它们，可以保留光束法平差所依赖的几何支撑集合。

### 主要贡献
- 提出 KYS-SLAM，将上下文证据从排除准则重构为对应代价，用于特征匹配。
- 引入分层语义—全景—运动先验融合，对关键点进行连续兼容性调制。
- 提出免训练、自校准、覆盖感知的动态片段判定方式，仅惩罚有足够运动证据的片段。
- 在固定配置、不按序列或数据集重新调参的条件下，报告了跨域结果：在 21 条立体序列上，室外 KITTI 的逐序列 ATE RMSE 降低 17.4%，室内 EuRoC 降低 27.7%，且无回退；在 KITTI Tracking 动态子集上降低 6.6%；在 Virtual KITTI 2 上降低 17.8%，最高达 31.2%。跨域涵盖室外驾驶、室内飞行和合成图像，并使用同一组常数。

### 局限性
- 摘要未提供足够信息说明方法对极端动态场景、低纹理场景或实时性开销的具体表现。
- 摘要未提供足够信息说明零样本运动分数模块的失败模式与阈值敏感性。
- 摘要未提供足够信息说明与更多基线方法的完整对比细节。
- 摘要未提供足够信息说明代码、数据集划分与完整实现配置。

### 阅读优先级
高。理由：该论文直接针对语义/动态 SLAM 中“剔除特征导致对应密度下降”的关键矛盾，提出连续对应代价这一较具方法学新意的重构思路；同时给出跨室外、室内与合成域的定量结果，且强调单一固定配置无回退，对视觉 SLAM、动态环境建图与语义几何融合方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier suppression. We contend that contextual implausibility is better expressed as a graded quantity than an exclusion criterion. We present Know-Your-Scene (KYS)-SLAM, a modular extension of ORB-SLAM3 that supplants feature rejection with continuous correspondence modulation. The contribution is the reframing of contextual evidence as correspondence cost, applied within feature matching and leaving the geometric backend unmodified. Each keypoint is augmented with semantic, panoptic, and motion priors fused through a hierarchical compatibility formulation, in which semantic class and instance identity enforce structural plausibility while a zero-shot motion score down-weights features on independently moving objects. That score comes from a training-free module fitting a depth-aware ego-motion model to background optical flow and classifying panoptic segments via self-calibrating, coverage-aware thresholds, so only segments with sufficient motion evidence are penalized and static structure is left unpenalized. Penalizing correspondences rather than discarding them preserves the geometric support bundle adjustment depends on. Under one fixed configuration, no coefficient retuned per sequence or dataset, KYS-SLAM reduces per-sequence ATE RMSE by 17.4% on outdoor KITTI and 27.7% on indoor EuRoC across 21 stereo sequences with no regressions, and by 6.6% on dynamic subsets of KITTI Tracking and 17.8%, up to 31.2%, on Virtual KITTI 2 -- cross-domain transfer across outdoor driving, indoor flight, and synthetic imagery under one set of constants.

</details>

#### 2026-09-23 - From LiDAR Maps to Visual Localization: Unified Visual Association for Robust Point-Line-Plane Pose Estimation

**Authors:** Wentao Zhao, Zikun Chen, Yihe Niu, Haoyu Chen, Jingchuan Wang
**Links:** [abs](https://arxiv.org/abs/2609.27363) - [pdf](https://arxiv.org/pdf/2609.27363)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From LiDAR Maps to Visual Localization: Unified Visual Association for Robust Point-Line-Plane Pose Estimation
- 作者：Wentao Zhao, Zikun Chen, Yihe Niu, Haoyu Chen, Jingchuan Wang
- 出版日期：2026-09-23T05:05:05Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.27363 ；PDF https://arxiv.org/pdf/2609.27363

### 一句话总结
该论文提出一种统一视觉关联的定位框架，将已有 LiDAR 地图渲染为带 2D-3D 来源信息的准图像，使相机观测与地图渲染视图可共享视觉特征与匹配器，从而实现全局定位与连续 6-DoF 位姿跟踪。

### 研究问题
论文关注的是：在已有 LiDAR 地图作为持久几何先验的条件下，如何实现相机定位。其核心挑战在于相机图像与点云地图之间存在显著的模态差异。摘要指出，该问题面向长期机器人导航，需要在严重光照变化和动态遮挡等条件下保持定位能力。

### 核心思路/方法
论文提出一个统一定位框架，使 LiDAR 地图变得“视觉可寻址”，而不是依赖专门的图像-LiDAR 对应模型。具体做法是：将地图几何与反射率渲染为 LiDAR 衍生的准图像，并保留显式的 2D-3D 来源关系，从而让相机观测和渲染地图视图能够共享成熟的视觉特征与匹配器，用于全局定位和连续位姿跟踪。

在对应关系上，通过这一共同视觉接口建立点和线对应；同时，利用保留的来源信息恢复度量 LiDAR 几何以及线支持的平面约束，用于位姿估计。

为提升在模糊关联和弱几何条件下的鲁棒性，论文进一步引入一种分布感知、可观测性互补的优化策略。该策略不是把匹配歧义压缩为单一置信度，而是将候选关联分布传播为方向性位姿信息不确定性，并根据可靠结构因子对当前弱位姿方向的互补能力，选择性增强这些结构因子。

### 主要贡献
- 提出统一视觉关联框架，将 LiDAR 地图渲染为带 2D-3D 来源的准图像，使相机图像与地图视图可共享视觉特征和匹配器。
- 通过共同视觉接口建立点、线对应，并利用来源信息恢复度量 LiDAR 几何和线支持的平面约束，用于位姿估计。
- 提出分布感知、可观测性互补的优化策略，将候选关联分布传播为方向性位姿信息不确定性，并选择性增强能互补弱位姿方向的可靠结构因子。
- 摘要称在 EuRoC MAV 基准和自采集真实世界序列上，仅使用预建 LiDAR 地图作为持久先验，实现了准确的全局定位和鲁棒的连续 6-DoF 跟踪，包括严重光照变化和动态遮挡条件下。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算开销、对地图质量或环境结构的依赖程度，也未提供与基线方法的定量对比细节、消融实验细节以及自采集序列的规模与条件。上述内容均需以论文正文为准。

### 阅读优先级
高。理由：该论文直接针对 LiDAR 地图与视觉定位之间的模态差异问题，提出统一视觉关联和点-线-平面位姿估计框架，并涉及全局定位、连续 6-DoF 跟踪以及严重光照和动态遮挡下的鲁棒性；同时发表在 3D Reconstruction & Multi-view Geometry 与机器人/AR 相关分类下，对视觉定位、机器人导航和多模态地图复用方向具有较高潜在参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera localization in a prior LiDAR map provides a persistent geometric reference for long-term robotic navigation, yet remains challenging because of the substantial modality gap between camera images and point-cloud maps. We present a unified localization framework that makes the LiDAR map visually addressable rather than relying on a dedicated image-LiDAR correspondence model. Map geometry and reflectivity are rendered into LiDAR-derived quasi-images with explicit 2D-3D provenance, enabling camera observations and rendered map views to share mature visual features and matchers for both global localization and continuous pose tracking. Point and line correspondences are established through this common visual interface, while the retained provenance recovers metric LiDAR geometry and line-supported planar constraints for pose estimation. To improve robustness under ambiguous associations and weak geometry, we further introduce a distribution-aware, observability-complementary optimization strategy. Instead of reducing matching ambiguity to a scalar confidence, candidate association distributions are propagated into directional pose-information uncertainty, and reliable structural factors are selectively reinforced according to their ability to complement the currently weak pose directions. Experiments on the EuRoC MAV benchmark and self-collected real-world sequences demonstrate accurate global localization and robust continuous 6-DoF tracking using only a pre-built LiDAR map as the persistent prior, including under severe illumination variations and dynamic occlusions.

</details>

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-28 - GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space

**Authors:** Kerui Ren, Tao Lu, Linning Xu, Changjian Jiang, Mu Huang, Chunhua Shen, Mulin Yu, Bo Dai
**Links:** [abs](https://arxiv.org/abs/2609.35734) - [pdf](https://arxiv.org/pdf/2609.35734)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, scene representation

<details>
<summary>Abstract</summary>

Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observed scene structure but often struggle to complete unseen regions, whereas video generative models offer rich appearance priors but accumulate inconsistencies during sequential view generation. We propose GeoVerse, a framework that synthesizes world-consistent novel views by performing generation within the geometric latent space of a pretrained 3D foundation model and injecting appearance priors from a video generative model. Specifically, GeoVerse extracts multilevel features from Wan2.2 VACE and injects them into the geometric latent diffusion model via a ControlNet-style adapter, incorporating video-learned appearance priors to enhance structural completion. To enforce cross-view coherence, a global spatial memory continuously aggregates observed and synthesized content, reprojecting target-aligned guidance to anchor subsequent predictions to a shared scene representation. Extensive experiments across diverse datasets demonstrate improved visual quality and geometric consistency, with a 2.23 dB higher PSNR on DL3DV and 32.4% lower ATE on Mip-NeRF360 compared to GLD.

</details>

#### 2026-09-28 - CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism

**Authors:** R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti
**Links:** [abs](https://arxiv.org/abs/2609.35619) - [pdf](https://arxiv.org/pdf/2609.35619)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, manipulation

<details>
<summary>Abstract</summary>

Incorporating dense visual information into motion planning remains challenging, as geometric planners rely on abstracted scene representations that discard visual richness, while learned visual models often lack geometric interpretability and computational efficiency. This paper introduces CollisionSplatting, a simple, modular, GPU-accelerated, probability-inspired distance metric with tunable conservatism that operates directly on standard 3D Gaussian Splatting (3DGS) scenes. When combined with learned image-conditioned reward functions, this metric enables joint geometric and visual planning by unifying collision-aware costs with image-space objectives. We integrate the metric into GPU-accelerated Model Predictive Path Integral (MPPI) and Rapidly-Exploring Random Tree (RRT) planners, and show on-par or better collision-classification performance compared to representative baselines while achieving substantially higher collision-checking throughput and significantly lower VRAM usage. Finally, we demonstrate the effectiveness of our metric in real-world vision-guided navigation and manipulation tasks, highlighting 3DGS as a practical bridge between rich perception and real-time motion planning.

</details>

#### 2026-09-28 - Less Is More: Genetic Frame Selection for Efficient Novel View Synthesis

**Authors:** Diego E. Farchione, Ramzi Idoughi, Alberto Jaspe-Villanueva, Peter Wonka
**Links:** [abs](https://arxiv.org/abs/2609.35573) - [pdf](https://arxiv.org/pdf/2609.35573)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, scene reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>Abstract</summary>

Feed-forward novel view synthesis reconstructs a scene from many input images in a single forward pass, yet more views do not necessarily improve performance: redundant or poorly chosen frames increase computational cost and may degrade reconstruction quality. We address the problem of selecting, from an already captured sequence, a fixed-size subset of input views that is most informative for reconstructing specified target viewpoints. We propose a render-free view selector that scores candidate frames based on three complementary criteria: target-view coverage, measured against observed frames that stand in for the targets, redundancy with previously selected views, and image sharpness. A lightweight scoring network then selects the most informative frames without rendering, reconstruction, or per-scene optimization at inference time. To train the selector, we distill an expensive offline search procedure in which a genetic algorithm identifies high-quality subsets by directly optimizing reconstruction performance on training scenes. The selector learns to reproduce these choices from geometric and image-level features alone. Across six datasets and multiple input budgets, our method consistently outperforms both geometric and reconstruction-aware view-selection baselines while incurring significantly lower selection costs than reconstruction-based alternatives. Moreover, carefully selected subsets can outperform feed-forward reconstruction from the full input sequence. The learned selector generalizes across diverse reconstruction paradigms (feed-forward, 3D Gaussian Splatting, and NeRF), to object-targeted reconstruction and to a cross-capture setting in which the target views come from a separate acquisition pass. More broadly, our results indicate that explicitly reasoning about target relevance and inter-view redundancy is a fundamental factor in efficient scene reconstruction.

</details>

#### 2026-09-28 - EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation

**Authors:** Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im
**Links:** [abs](https://arxiv.org/abs/2609.34853) - [pdf](https://arxiv.org/pdf/2609.34853)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, localization, scene understanding

<details>
<summary>Abstract</summary>

Open-vocabulary 3D scene understanding enables object localization and segmentation from free-form text queries without a fixed category vocabulary. Many recent methods build on 3D Gaussian Splatting and consolidate multi-view observations, such as masked crops from individual views, into language features or compact object descriptors before the query is known. However, observations of the same object vary across viewpoints and are not equally informative: some reveal cues relevant to a particular query, whereas others provide incomplete or misleading evidence. Pre-query consolidation can therefore suppress cues on which a later query depends. We introduce EviSplat, which preserves individual observation features as evidence for later text queries. EviSplat retains individual observation features within class-agnostic 3D instances that represent objects, object parts, or background regions. It also learns, for each Gaussian, a distribution describing which visual appearances its observations support. Given a text query, EviSplat scores each instance using its most relevant observations. It then computes a score for each Gaussian by combining instance-level relevance with locally supported evidence, weighted by how often and how unambiguously that Gaussian was observed. Different queries can thus draw on different visual cues from the same preserved evidence. Experiments across diverse datasets and evaluation protocols demonstrate state-of-the-art performance, supporting the benefit of preserving multi-view evidence until query time and aggregating it according to the query.

</details>

#### 2026-09-28 - SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering

**Authors:** Jingqian Sun, Yichao Tang
**Links:** [abs](https://arxiv.org/abs/2609.34733) - [pdf](https://arxiv.org/pdf/2609.34733)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural rendering, rendering, simulation

<details>
<summary>Abstract</summary>

Dynamic surgical scene modeling is essential for robotic perception, simulation, and decision support. Although existing neural rendering methods enable efficient reconstruction and rendering of deformable surgical scenes, they remain primarily focused on observed-frame reconstruction rather than forecasting future scene states. To this end, we present SurgGMF, a fully causal Gaussian motion forecasting framework for anticipatory surgical scene rendering. Rather than predicting future RGB images directly, SurgGMF forecasts future Gaussian motion states represented by position, scale, and rotation residuals (X/S/R) from historical Gaussian motion fields. To prevent target leakage, we introduce a full-causal-last rendering protocol, where future Gaussian states are rendered without accessing target-frame Gaussian attributes while preserving causal appearance propagation. We evaluate SurgGMF on 12 EndoNeRF and StereoMIS video slices using neural temporal learners and classical dynamics baselines under a unified forecasting protocol. Learned Gaussian motion forecasting consistently outperforms classical dynamics baselines in render space, demonstrating gains beyond hand-crafted state extrapolation. Latency analysis further reveals an accuracy--efficiency trade-off: under the current implementations, TKAN achieves the highest accuracy, whereas GRU and LSTM provide more favorable module-level latency profiles. These results establish SurgGMF as a reproducible framework for causal Gaussian motion forecasting and advance surgical Gaussian representations from retrospective reconstruction toward predictive scene modeling.

</details>

#### 2026-09-28 - GenNVS: Geometry-enhanced Novel View Synthesis via Disentangled 3D Prior

**Authors:** Yajiao Xiong, Youyu Luan, Xiaoyu Zhou, Yongtao Wang
**Links:** [abs](https://arxiv.org/abs/2609.34579) - [pdf](https://arxiv.org/pdf/2609.34579)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

Single-image novel view synthesis remains challenging because the underlying 3D geometry is highly ambiguous. Recent diffusion-based approaches produce plausible results, but they often struggle to preserve the geometric structure and spatial coherence of foreground objects. We present GenNVS, a framework for geometry-enhanced novel view synthesis via a disentangled 3D prior. Specifically, GenNVS models foreground objects and the background with 3D Gaussian Splatting and aligns them through a coarse-to-fine geometric optimization process to form a unified 3D scene. This scene conditions a video diffusion model through the proposed Dual-Stream Masking mechanism, which guides synthesis by jointly exploiting rendered validity masks and geometry-aware warping. Experimental results show that GenNVS performs favorably against recent methods in both visual quality and geometric accuracy, while naturally supporting flexible scene editing.

</details>

#### 2026-09-28 - Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting

**Authors:** Yulong Cheng, Youneng Bao, Junfeng Zhou, Mu Li, Jie Wen
**Links:** [abs](https://arxiv.org/abs/2609.34367) - [pdf](https://arxiv.org/pdf/2609.34367)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, splatting, VR, virtual reality

<details>
<summary>Abstract</summary>

Learned image codecs (LICs) achieve high reconstruction quality, but their decoding speed is often insufficient for immersive virtual reality (VR). Gaussian splatting (GS) codecs render much faster, yet still lag in reconstruction quality and typically decide primitive allocation without considering the coding cost of each primitive. We introduce OIC-GS, an omnidirectional GS codec with a new hierarchical HEALPix primitive grid representation. Gaussian primitives are anchored at predefined spherical locations, eliminating explicit coordinate coding. Finer levels refine their coarser ancestors, naturally supporting coarse-to-fine reconstruction and layered transmission. The predefined grid also enables efficient viewport decoding by selecting only view-relevant primitives. We further introduce a lightweight entropy model for quantized primitives and optimize the codec under a spherical rate-distortion objective. Primitives with insufficient rate-distortion benefit are automatically removed when their quantized opacity becomes zero, allowing OIC-GS to adapt both primitive density and level of detail without a fixed primitive budget. A single bitstream supports full-sphere, viewport-dependent, and progressive decoding. The first viewport reaches final quality after decoding only 52% of the bitstream, and is then rendered at 1,270 FPS. On a 100-image omnidirectional benchmark, OIC-GS outperforms all evaluated GS codecs, reducing WS-PSNR BD-rate by 49.6% over GaussianImage++ and 68.6% over SGI, which uses a learned entropy model.

</details>

#### 2026-09-28 - AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting

**Authors:** Amirhossein Mollaei Khass, Nader Motee
**Links:** [abs](https://arxiv.org/abs/2609.34176) - [pdf](https://arxiv.org/pdf/2609.34176)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

Radiance fields need hundreds of views, and their placement matters as much as their number. Next-best-view (NBV) selection for 3D Gaussian Splatting (3DGS) usually scores every candidate in the pool and keeps one. Searching for information and choosing a camera, however, are separable problems. We present AGILE-GS, an anchor-guided NBV method that separates the two. A virtual anchor pose is optimized on SE(3) by Riemannian gradient ascent on expected information gain. It need not be reachable or in the pool; it marks where the model is most uncertain. Candidates are scored against the anchor's viewing geometry, and a greedy ridge-leverage step distills the pool into a small, non-redundant shortlist without rendering any candidate. The shortlist can be used in two ways. AGILE-GS takes the first view on it as the next view, so no Fisher information is computed for any candidate. AGILE-GS+ computes the Fisher information gain of each shortlisted view and picks the best, so the expensive evaluation runs on a handful of views rather than the whole pool. On standard benchmarks and in closed-loop embodied acquisition, both match or exceed existing baselines while cutting selection latency by one to two orders of magnitude.

</details>

#### 2026-09-27 - Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors

**Authors:** Ge Gao, Siyue Teng, Chanqgi Wang, Fan Zhang, Nantheera Anantrasirichai, Jui Chiu Chiang, Wen-Hsiao Peng, David Bull
**Links:** [abs](https://arxiv.org/abs/2609.33969) - [pdf](https://arxiv.org/pdf/2609.33969)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic 3D, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

Immersive video communication requires photorealistic, render-efficient, and compact dynamic scene representations. 3D Gaussian Splatting (3DGS) offers a promising representation, but dynamic 3DGS remains difficult to compress due to dense primitives and spatiotemporal redundancy. Anchor-based formulations improve compactness with sparse scaffolds that share geometry and appearance across primitives. However, existing designs often rely on deforming a single canonical scaffold and condition each primitive on its associated anchor in isolation, limiting their ability to handle non-local dynamics and disocclusion while under-exploiting inter-anchor correlations, particularly in motion- or texture-dense regions. To address these limitations, we propose SAGA, a volumetric video codec built upon Sparse Anchor-assisted GAussian splatting representations. SAGA represents dynamic 3D scenes using hierarchically organized sparse 4D anchors, where coordinate-based INR decoders generate fine anchors and Gaussian primitives from inter-anchor interpolations, enabling compact parameter sharing across spatiotemporal structures. For long-range dependencies among unstructured anchors, we further introduce fixed-size memory slots with orthogonality-informed updates for accurate entropy-context modeling. Experiments show that SAGA achieves strong rate-distortion performance against GIFStream, with PSNR BD-rate reductions of 80.39% and 83.94% on Neu3D and MPEG MIV, respectively.

</details>

#### 2026-09-27 - Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation

**Authors:** Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang
**Links:** [abs](https://arxiv.org/abs/2609.33872) - [pdf](https://arxiv.org/pdf/2609.33872)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, manipulation, simulation

<details>
<summary>Abstract</summary>

Robotic manipulation policies are advancing rapidly with increasing reliance on vision-language models for end-to-end decision making. However, reliable deployment remains challenging because many policies lack explicit mechanisms for predicting task outcomes and evaluating whether generated actions will achieve desired final states, causing execution errors to accumulate during long-horizon manipulation. We present Robot-GST, a geometry-aware spatio-temporal behaviour representation and evaluation framework that constructs a Gaussian-SAM robotic environment for real-to-sim policy verification and improves the reliability of real-world manipulation deployment. Our approach constructs a high-fidelity robotic environment from RGB-D observations using 3D Gaussian Splatting and SAM3D, enabling ``simulation and evaluation before acting''. It integrates visual observations and language instructions with spatio-temporal reasoning for long-horizon task planning using large vision-language models. To bridge high-level planning and real-world execution, we introduce Gaussian-aware final-state estimation through geometric sampling and state-based trajectory planning. Before execution, candidate action sequences are simulated and evaluated in the Gaussian-SAM environment to filter infeasible behaviours. We validate our approach on representative manipulation tasks involving rigid, soft, and deformable objects, including cube placing, toy packing, and duck rearrangement, demonstrating that geometry-aware spatio-temporal reasoning and state-aware execution improve manipulation reliability across different object categories. Our results suggest that combining geometry-aware reconstruction with high-quality rendering and simulation provides a scalable approach for evaluating robotic manipulation behaviours. Website: https://robot-gst.github.io

</details>

#### 2026-09-24 - Towards Practical Compression of 3D Gaussian Splatting

**Authors:** Pengpeng Yu, Yueru Chen, Fei Song, Tai Qin, Qi Zhang, Jing Wang, Yulan Guo
**Links:** [abs](https://arxiv.org/abs/2609.30245) - [pdf](https://arxiv.org/pdf/2609.30245)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Practical Compression of 3D Gaussian Splatting
- 作者：Pengpeng Yu, Yueru Chen, Fei Song, Tai Qin, Qi Zhang, Jing Wang, Yulan Guo
- 出版日期：2026-09-24T17:57:56Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.30245) / [PDF](https://arxiv.org/pdf/2609.30245)

### 一句话总结
论文提出 COSA-GS，通过基于 anchor 的因果分解构建上下文，避免对不规则 3D 表示做空间聚合，并结合量化感知训练与整数推理，在提升 3DGS 压缩性能的同时实现跨平台一致的熵解码。

### 研究问题
3D Gaussian Splatting（3DGS）虽然能实现高质量新视角合成，但存储开销很大。现有压缩方法通常依赖对不规则 3D 表示进行空间上下文建模，这会增加训练和编码复杂度；同时，浮点上下文推理可能在不同平台之间引入数值不一致，导致熵解码失败。因此，论文关注的是如何在保持实用性的前提下，实现高效且跨平台一致的 3DGS 压缩。

### 核心思路/方法
论文提出 COSA-GS，其核心是不通过空间聚合来构建上下文，而是采用 anchor-wise causal factorization。具体来说：
- 使用每个 anchor 坐标导出的几何上下文来建模紧凑的可学习 anchor latent；
- 将 anchor latent 与几何上下文融合，形成用于属性编码的 anchor context；
- 该上下文模型架构简单，仅由线性变换和激活函数组成；
- 训练时使用率失真优化，并结合自适应 Gaussian 剪枝；
- 进一步开发量化感知训练和上下文模型的整数推理，以实现跨平台熵解码符号的 bit-exact 一致性。

### 主要贡献
- 提出 COSA-GS，用 anchor-wise causal factorization 构建上下文，避免对不规则 3D 表示做空间聚合，从而降低训练和编码复杂度。
- 设计了一个简单的上下文模型，仅包含线性变换和激活函数，并将 anchor latent 与几何上下文融合用于属性编码。
- 采用率失真优化与自适应 Gaussian 剪枝进行训练。
- 引入量化感知训练和整数推理，以实现跨平台熵解码符号的 bit-exact 一致性。
- 摘要声称实验表明 COSA-GS 达到 state-of-the-art 压缩性能，同时保持快速且一致的跨平台解码。

### 局限性
- 摘要未提供足够信息说明其在不同数据集、场景类型或硬件平台上的泛化能力。
- 摘要未提供足够信息说明量化感知训练和整数推理带来的额外训练成本或实现复杂度。
- 摘要未提供足够信息说明与具体已有压缩方法相比的完整实验设置、消融结果和失败案例。
- 摘要未提供足够信息说明自适应 Gaussian 剪枝的具体策略、超参数敏感性及其对重建质量的影响。

### 阅读优先级
高。理由：该论文聚焦 3DGS 压缩中的实际部署问题，尤其是跨平台熵解码一致性，这类问题对实际应用很重要；同时摘要声称在压缩性能和快速一致解码方面达到 state-of-the-art，并提供了代码链接，适合关注 3DGS 压缩、神经场景表示和实用编解码实现的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D representations, increasing the complexity of training and coding. Meanwhile, floating-point context inference can introduce numerical inconsistencies across platforms, causing entropy-decoding failures. To address these practical challenges, we propose COSA-GS, which constructs context without spatial aggregation through anchor-wise causal factorization. Specifically, we use geometry context derived from each anchor's coordinates to model a compact learnable anchor latent. The anchor latent is then fused with the geometry context to form an anchor context for attribute coding. The resulting context model features a simple architecture composed solely of linear transformations and activations. We train COSA-GS using rate--distortion optimization with adaptive Gaussian pruning. Further, we develop quantization-aware training and integer inference for the context model to achieve bit-exact consistency of entropy-decoded symbols across platforms. Experiments demonstrate that COSA-GS achieves state-of-the-art compression performance while retaining fast and consistent cross-platform decoding, providing a simple yet effective framework for practical 3DGS compression. Code is available at https://github.com/pengpeng-yu/COSA-GS.

</details>

#### 2026-09-24 - M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis

**Authors:** Yang Zhou, Jiuhong Xiao, Shizhao Ye, Long Quang, Carlos Nieto-Granda, Giuseppe Loianno
**Links:** [abs](https://arxiv.org/abs/2609.30056) - [pdf](https://arxiv.org/pdf/2609.30056)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis
- 作者：Yang Zhou, Jiuhong Xiao, Shizhao Ye, Long Quang, Carlos Nieto-Granda, Giuseppe Loianno
- 出版日期：2026-09-24T16:14:00Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.30056 ；PDF：https://arxiv.org/pdf/2609.30056

### 一句话总结
M3GD 提出一种 Camera–LiDAR 多模态表示，将冻结的 2D 图像与 3D 点云基础模型组合用于生成式新视角合成，并通过像素对齐的 LiDAR 信息提升目标视角 RGB 与深度合成效果。

### 研究问题
机器人新视角合成（NVS）需要同时恢复视觉外观和度量 3D 结构，但多数生成式 NVS 方法只依赖图像，忽略了机器人平台上常见的 LiDAR 这一互补传感器。论文要解决的问题是：如何在不单独预训练跨模态翻译器的前提下，把 Camera 与 LiDAR 结合用于生成式 NVS。

### 核心思路/方法
M3GD 组合独立预训练的 2D 图像基础模型与 3D 点云基础模型。作者指出，在相机投影之后，冻结的 LiDAR 特征与图像特征表现出显著共享的空间结构，从而构成一种自然的跨模态表示。基于这一结构，M3GD 用 LiDAR 条件化生成：将显式几何统计与学习到的点云描述子组合成图像潜变量网格上的视角对齐 packet，并通过轻量级残差适配器注入多视角 flow-matching 生成器；该生成器的潜空间、解码器和训练目标保持不变。目标视角 LiDAR 被用作几何查询，将请求视角与源观测关联起来。

### 主要贡献
- 提出 M3GD，一种用于生成式 NVS 的 Camera–LiDAR 多模态表示，无需单独预训练跨模态翻译器。
- 利用相机投影后冻结 LiDAR 与图像特征之间的共享空间结构，作为自然的跨模态表示。
- 通过轻量级残差适配器将视角对齐的 LiDAR packet 注入多视角 flow-matching 生成器，同时保持生成器原有潜空间、解码器与训练目标不变。
- 在 GrandTour 数据集上，相比同一骨干的纯图像版本，提升了目标视角 RGB 与深度合成效果。
- 消融表明增益来自像素对齐的 LiDAR 内容，且目标视角 LiDAR 起到连接请求视角与源观测的几何查询作用。
- 在地面机器人上部署，展示实际运行能力，并可通过 Euler 积分步数配置质量—成本权衡。

### 局限性
摘要未提供足够信息。摘要未说明方法在更广泛数据集、不同传感器配置、极端视角变化或实时性上限等方面的具体限制。

### 阅读优先级
中。理由：该工作聚焦机器人 NVS 中 Camera–LiDAR 多模态生成式合成，问题明确，方法思路具有启发性，并且包含数据集实验、消融与真实机器人部署；但摘要未提供与更多基线或更广泛场景的对比细节，是否具有普遍优势仍需阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Robotic novel view synthesis (NVS) must recover both visual appearance and metric 3D structure, yet most generative NVS methods rely only on images, overlooking LiDAR, a complementary sensor common on robotic platforms. We present M3GD, a Camera--LiDAR multimodal representation for generative NVS that composes independently pretrained 2D image and 3D point-cloud foundation models without separately pretraining a cross-modal translator. We show that, after camera projection, frozen LiDAR and image features exhibit substantial shared spatial structure, providing a natural cross-modal representation. M3GD conditions generation on LiDAR through this structure: it combines explicit geometry statistics with learned point-cloud descriptors into view-aligned packets on the image-latent grid, injected through a lightweight residual adapter into a multi-view flow-matching generator whose latent space, decoders, and training objective remain intact. On the GrandTour dataset, M3GD improves target-view RGB and depth synthesis over an image-only version of the same backbone. Ablations show that the gains come from pixel-aligned LiDAR content and that target-view LiDAR acts as a geometric query linking the requested view to source observations. Deployment on a ground robot demonstrates practical real-world operation, with a configurable quality--cost trade-off controlled by the number of Euler integration steps.

</details>

#### 2026-09-24 - OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning

**Authors:** Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai
**Links:** [abs](https://arxiv.org/abs/2609.29985) - [pdf](https://arxiv.org/pdf/2609.29985)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning
- 作者：Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai
- 出版日期：2026-09-24T15:35:08Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.29985) / [PDF](https://arxiv.org/pdf/2609.29985)

### 一句话总结
OceanXL 提出一种面向大规模水下场景的 3D Gaussian Splatting 框架，通过分块划分与自适应剪枝，在保持全局几何一致性的同时提升训练效率与渲染性能，并构建了一个大规模水下数据集。

### 研究问题
水下三维重建对海洋探索、生态监测和海底基础设施检测至关重要，但在大规模场景下仍面临困难，主要原因是光衰减、散射以及捕获覆盖范围有限。3D Gaussian Splatting（3DGS）虽能实现高质量实时渲染，但将其应用于大规模水下场景时，受限于高内存消耗和在大范围区域上的低效优化。

### 核心思路/方法
论文提出 OceanXL，一个快速且可扩展的、基于 3DGS 的大规模水下重建框架。方法采用分而治之策略，将场景划分为空间上连贯的块，以实现高效优化，同时保持全局几何一致性。论文还引入一种针对水下条件定制的自适应剪枝方案，去除冗余 primitives，从而在不牺牲视觉保真度的情况下产生紧凑表示。上述组件共同提升了大规模场景的训练效率和渲染性能。此外，论文还引入了一个覆盖多样海洋环境的大规模水下数据集。

### 主要贡献
- 提出 OceanXL，一个面向大规模水下重建的快速、可扩展 3DGS 框架。
- 采用分而治之的空间连贯块划分策略，在高效优化的同时保持全局几何一致性。
- 引入针对水下条件的自适应剪枝方案，去除冗余 primitives，得到紧凑表示且不牺牲视觉保真度。
- 引入一个覆盖多样海洋环境的大规模水下数据集。
- 在五个大规模场景上的实验表明，相较大规模场景基线，方法在可扩展性、紧凑性和效率—质量权衡方面表现良好。
- 在小规模 SeaThru-NeRF 数据集上的受控比较进一步显示，与水下专用方法相比，方法具有有竞争力的重建质量，且模型尺寸显著更小。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败情形、计算资源需求上限、数据集规模与采集细节、定量指标数值，以及与其他方法比较时的具体限制条件。局限性的详细内容需参见论文全文。

### 阅读优先级
中。理由：该论文聚焦水下大规模 3DGS 重建，针对光衰减、散射、覆盖有限、内存消耗高和优化效率低等明确问题，提出分块划分与自适应剪枝的组合方案，并附带大规模水下数据集；研究主题和应用场景较具体，对水下重建、3DGS 扩展性与大规模场景优化方向的研究者有参考价值。但摘要未提供定量结果和详细实验设置，是否具有广泛方法学影响需依赖全文判断，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

Underwater 3D reconstruction is critical for marine exploration, ecological monitoring, and subsea infrastructure inspection, yet remains challenging at large scale due to light attenuation, scattering, and limited capture coverage. While 3D Gaussian Splatting (3DGS) enables high-quality real-time rendering, its application to large underwater scenes is constrained by high memory consumption and inefficient optimization over extensive areas. We propose OceanXL, a fast and scalable 3DGS-based framework for large-scale underwater reconstruction. OceanXL adopts a divide-and-conquer strategy, partitioning scenes into spatially coherent blocks to enable efficient optimization while preserving global geometric consistency. We further introduce an adaptive pruning scheme tailored to underwater conditions that removes redundant primitives, producing compact representations without sacrificing visual fidelity. Together, these components improve training efficiency and rendering performance for large scenes. We also introduce a large-scale underwater dataset covering diverse marine environments. Experiments on five large-scale scenes demonstrate favorable scalability, compactness, and efficiency--quality trade-offs over large-scene baselines. Controlled comparisons on the small-scale SeaThru-NeRF dataset further show competitive reconstruction quality with substantially smaller model sizes than underwater-specific methods.

</details>

#### 2026-09-24 - Shadow Reduction in Ultrasound Imaging Using Differentiable Simulation and Radiance Field Decomposition

**Authors:** Valentin Bacher, Pak Hei Yeung, Bernhard Kainz, Madeleine K. Wyburd, Nicola K. Dinsdale, Michael Gray, Ana I. L. Namburete
**Links:** [abs](https://arxiv.org/abs/2609.29373) - [pdf](https://arxiv.org/pdf/2609.29373)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, rendering, radiance, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Shadow Reduction in Ultrasound Imaging Using Differentiable Simulation and Radiance Field Decomposition
- 作者：Valentin Bacher, Pak Hei Yeung, Bernhard Kainz, Madeleine K. Wyburd, Nicola K. Dinsdale, Michael Gray, Ana I. L. Namburete
- 出版日期：2026-09-24T10:55:49Z
- 分类：Neural Scene Representations & Rendering（主要分类）；次要分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.29373 ；PDF https://arxiv.org/pdf/2609.29373

### 一句话总结
提出 RFlash，一种基于可微辐射场分解的物理信息后处理方法，将波束形成后的超声图像分解为衰减图与散射强度图，并通过衰减自适应重渲染减轻声影，无需原始扫描数据或硬件改动。

### 研究问题
超声中来自骨骼等强衰减组织的声影会遮挡临床重要结构。在胎儿脑成像中，颅骨引起的伪影对靠近探头一侧（近端）半球造成的不利影响尤为严重，限制了左右半球的对称评估。现有校正方法需要原始扫描仪数据、对组织属性施加限制性假设，或依赖可能产生解剖结构幻觉的生成模型。

### 核心思路/方法
RFlash 是一种物理信息后处理方法，利用图像形成的可微辐射场表述，将波束形成后的超声图像分解为显式的衰减图与散射强度图。随后通过衰减自适应重渲染，去除每个深度处信号对中间组织的依赖，相当于虚拟地将探头推进到组织内部。该方法无需硬件修改，也无需访问原始扫描仪数据，并支持线性与曲率探头的 2D 和 3D 采集。

### 主要贡献
- 提出 RFlash，将波束形成超声图像分解为衰减图与散射强度图，并借助衰减自适应重渲染减轻声影。
- 在 1,261 例 3D 胎儿脑体积、143 例真实 2D 曲率腹部扫描和 1,200 例模拟 2D 线性探头肝脏扫描上，比经典 Hughes-Duck 衰减校正更有效地降低阴影相关强度差异。
- 对在远端半球（远离探头）训练并应用于近端半球的孕龄模型，预测误差相对原始图像降低 5.1 天（40%）。
- 估计的衰减图产生阴影置信图，可改善随机森林骨影分割，并在 SHAP 重要性上高于现有神经置信图基线，提示更好的物理一致性。
- 方法无需硬件修改或原始扫描仪数据，支持线性与曲率探头的 2D 和 3D 采集。

### 局限性
摘要未提供足够信息。摘要中未说明方法的失败情形、计算开销、对特定解剖或探头类型的适用边界、分解唯一性或潜在伪影等局限。

### 阅读优先级
中。理由：该工作针对超声声影这一明确临床问题，提出无需原始数据、可后处理且覆盖 2D/3D 与多种探头的物理信息方案，并在较大规模数据上给出定量改善，与可微渲染和神经场景表示方向相关。但摘要未提供方法细节、失败案例和计算成本，是否值得深入阅读取决于对超声后处理、可微仿真或辐射场分解的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Acoustic shadows from bone and other highly attenuating tissues obscure clinically important structures in ultrasound. In fetal brain imaging, skull-induced artefacts disproportionately degrade the hemisphere closer to the transducer (proximal), limiting symmetric assessment of the two hemispheres. Existing correction methods require raw scanner data, impose restrictive assumptions on tissue properties, or rely on generative models that may hallucinate anatomy. We present RFlash, a physics-informed post-processing method that decomposes beamformed ultrasound images into explicit attenuation and scatter-intensity maps using a differentiable radiance-field formulation of image formation. Attenuation-adaptive re-rendering then removes the dependence of the signal at each depth on the intervening tissue, equivalent to virtually advancing the transducer into the tissue. Across 1,261 3D fetal brain volumes, 143 real 2D curvilinear abdominal scans, and 1,200 simulated 2D linear-probe liver scans, RFlash reduces shadow-related intensity differences more effectively than classical Hughes-Duck attenuation correction. For a gestational-age model trained on the distal hemisphere (further from the transducer) and applied to the proximal hemisphere, prediction error decreases by 5.1 days (40%) relative to the original images. The estimated attenuation maps also yield shadow-confidence maps that improve random-forest bone-shadow segmentation over the image alone and receive greater SHAP importance than an existing neural confidence-map baseline, suggesting greater physical consistency. RFlash requires neither hardware modification nor access to raw scanner data and supports 2D and 3D acquisitions with linear and curvilinear probes, making it widely applicable allowing clinicians to use our method on their already acquired scanners and images.

</details>

#### 2026-09-24 - Only What Was Seen: Observation-Gram Compaction of View-Dependent Appearance in 3D Gaussian Splatting

**Authors:** Krzysztof Pietroszek
**Links:** [abs](https://arxiv.org/abs/2609.28997) - [pdf](https://arxiv.org/pdf/2609.28997)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Only What Was Seen: Observation-Gram Compaction of View-Dependent Appearance in 3D Gaussian Splatting
- 作者：Krzysztof Pietroszek
- 出版日期：2026-09-24T04:06:12Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.28997) / [PDF](https://arxiv.org/pdf/2609.28997)

### 一句话总结
论文提出用“每高斯观测 Gram 矩阵”作为系数变化到图像平方误差的一阶映射指标，并据此统一处理 3D Gaussian Splatting 中球谐颜色系数的降阶、阶数分配与向量量化压缩。

### 研究问题
3D Gaussian Splatting 模型的大部分内存用于存储球谐颜色系数，但每个高斯在训练时实际只被训练相机的狭窄方向锥观测到。论文关注的问题是：如何利用这种“只被部分方向观测”的特性，更有效地压缩视角相关外观表示。

### 核心思路/方法
论文将每个高斯的观测方向与混合权重累积为 per-Gaussian observation Gram matrix。该矩阵被描述为从系数变化到平方图像误差的精确一阶映射，且只需要模型和相机位姿即可计算。基于该失真度量：
- 阶数降低可写为闭式投影，并推广了截断操作；
- 阶数分配可建模为拉格朗日率失真问题；
- 向量量化可转化为矩阵加权的 Lloyd 算法，而 Compressed3D 的量化器是其标量情形。

作者将该度量替换进 Compressed3D 且保持其他部分不变，并报告了在微调前、匹配码率下以及无需训练图像场景中的效果。

### 主要贡献
- 提出 per-Gaussian observation Gram matrix，作为可用于其他压缩器的失真度量，用于描述系数变化到平方图像误差的一阶关系。
- 在该度量下，将球谐降阶、阶数分配和向量量化分别形式化为闭式投影、拉格朗日率失真问题和矩阵加权 Lloyd 算法。
- 将度量替换进 Compressed3D 后，摘要报告微调前 PSNR 提升 +0.49 dB，SSIM 与 LPIPS 也随之改善；在匹配码率下仍获得 +0.32 dB，且无需任何训练图像。
- 仅基于该度量的免训练压缩栈在 Mip-NeRF 360 上同等质量下比 image-free GSICO 小 15%。

### 局限性
摘要未提供足够信息说明计算观测 Gram 矩阵与矩阵加权量化带来的额外计算开销、内存峰值或运行时间。摘要未提供足够信息说明在训练相机覆盖不足或视角外推条件下的表现。摘要未提供足够信息说明除 Mip-NeRF 360 与 Compressed3D 相关设置外的泛化实验。摘要未提供足够信息说明代码、完整实现细节及消融实验范围。

### 阅读优先级
高。理由：该工作直接针对 3D Gaussian Splatting 的视角相关外观内存瓶颈，提出可插入现有压缩器的失真度量，并在摘要中给出明确的 PSNR、码率与模型体积收益；对神经渲染压缩、球谐系数压缩和率失真优化方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Most of the memory of a 3D Gaussian Splatting model holds spherical-harmonic colour coefficients, yet each Gaussian is seen only from the narrow cone of directions of the training cameras. We turn this into a distortion metric that other compressors can adopt: a per-Gaussian observation Gram matrix, accumulated from viewing directions and blending weights, is the exact first-order map from coefficient changes to squared image error and needs only the model and the camera poses. Under it, degree reduction becomes a closed-form projection that generalises truncation, degree allocation a Lagrangian rate-distortion problem, and vector quantisation the matrix-weighted Lloyd algorithm, of which Compressed3D's quantiser is the scalar case. Swapped into Compressed3D with everything else unchanged, the metric raises PSNR by +0.49 dB before fine-tuning, with SSIM and LPIPS following, and at matched rate still gains +0.32 dB without a single training image. A training-free stack built on the metric alone is 15% smaller than the image-free GSICO at equal quality on Mip-NeRF 360.

</details>

#### 2026-09-24 - PlenoCI: Plenoptic CharacterIstics for View Dependence Aware Change Classification

**Authors:** Jason Lai, Chamuditha Jayanga Galappaththige, Niko Suenderhauf, Dimity Miller, Donald G. Dansereau
**Links:** [abs](https://arxiv.org/abs/2609.28930) - [pdf](https://arxiv.org/pdf/2609.28930)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PlenoCI: Plenoptic CharacterIstics for View Dependence Aware Change Classification
- 作者：Jason Lai, Chamuditha Jayanga Galappaththige, Niko Suenderhauf, Dimity Miller, Donald G. Dansereau
- 出版日期：2026-09-24T02:27:24Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.28930) / [PDF](https://arxiv.org/pdf/2609.28930)

### 一句话总结
论文提出 PlenoCI——一种从 3DGS 所近似的全光场中导出的特征，通过解析全光导数捕捉视角相关视觉行为并忽略朗伯纹理，用于缓解欠约束辐射场重建在变化检测中的误报问题，并支持变化分类。

### 研究问题
辐射场表示（如 3DGS）虽能编码遮挡与视角依赖等复杂视觉现象，但本质上是欠约束的：即使场景未发生改变，独立优化的重建也会收敛到不同的基元配置。摘要指出，这一特性会给变化检测/分类带来困难，需要一种对欠约束表示具有鲁棒性的特征来区分真实变化与重建差异。

### 核心思路/方法
- 提出 PlenoCI（Plenoptic CharacterIstics），从辐射场近似所对应的全光场构建特征。
- PlenoCI 直接捕捉丰富的视觉行为，同时忽略朗伯纹理。
- 通过从 3DGS 表示推导闭式解析全光导数，高效检测这些 5D 结构。
- 方法在设计上对欠约束表示具有鲁棒性。
- 将 PlenoCI 用于变化分类：先用实例感知的 3DGS 流程检测变化，再借助 PlenoCI 将变化分类为几何变化或外观变化。

### 主要贡献
- 提出 PlenoCI 特征及其基于 3DGS 的闭式解析全光导数计算方式。
- 在未改变场景的独立重建之间，相比同期工作报告少两个数量级的假阳性。
- 在变化检测上，于 CL-Splats 取得当前最优结果，较最强竞争者提升 25.7% mIoU，同时在更具挑战性的 PASLCD 基准上保持竞争力。
- 借助 PlenoCI 将变化分类为几何/外观两类，平衡准确率为 0.735，与最佳基线相当。
- 作者认为全光导数与 PlenoCI 为视觉复杂环境中视角依赖感知的理解开辟了新方向；代码与数据已公开。

### 局限性
- 摘要未提供足够信息说明方法在非 3DGS 表示或其他辐射场表示上的适用性。
- 摘要未提供足够信息说明计算开销、实时性或可扩展性的具体表现。
- 摘要未提供足够信息说明在 PASLCD 上与最强方法的具体差距及失败案例。
- 摘要未提供足够信息说明变化分类中几何/外观类别定义、数据标注方式与评估细节。
- 摘要未提供足够信息说明对视角依赖极端场景或动态场景的泛化能力。

### 阅读优先级
高。理由：该工作针对辐射场欠约束这一核心问题提出新特征与解析导数方法，并在变化检测基准上报告了显著指标提升（CL-Splats 上 +25.7% mIoU，假阳性降低两个数量级），对神经场景表示、3DGS 变化检测与视角依赖理解方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Radiance field representations such as 3D Gaussian Splatting (3DGS) natively encode complex visual phenomena such as occlusions and view dependence, but they are inherently underconstrained. Independently optimized reconstructions converge to different primitive configurations, even in unchanged regions. We introduce Plenoptic CharacterIstics (PlenoCI), a novel feature built from the plenoptic field these representations approximate. PlenoCI directly captures rich visual behaviors while ignoring Lambertian textures. By deriving closed-form analytic plenoptic derivatives from a 3DGS representation, we efficiently detect these 5D structures. Our approach is robust to underconstrained representations by construction, reporting two orders of magnitude fewer false positives between independent reconstructions of unchanged scenes than concurrent work. We demonstrate PlenoCI's utility on change classification. First, we detect changes with an instance-aware 3DGS pipeline, achieving state-of-the-art results on CL-Splats with a 25.7% mIoU gain over the strongest competitor, while remaining competitive on the more challenging PASLCD benchmark. Leveraging PlenoCI, we classify changes as geometric or appearance-based with a balanced accuracy of 0.735, comparable to the best performing baseline. We believe plenoptic derivatives and PlenoCI open new directions for view dependence aware understanding in visually complex environments. Code and data are available at https://js0n-lai.github.io/plenoci.

</details>

#### 2026-09-23 - RoomLight: A 2.5D Illumination Prior for Indoor Environments

**Authors:** Andreea Ardelean, Bernhard Egger
**Links:** [abs](https://arxiv.org/abs/2609.28300) - [pdf](https://arxiv.org/pdf/2609.28300)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, differentiable rendering, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoomLight: A 2.5D Illumination Prior for Indoor Environments
- 作者：Andreea Ardelean, Bernhard Egger
- 出版日期：2026-09-23T15:46:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.28300 ；PDF: https://arxiv.org/pdf/2609.28300 ；项目页：https://andreead-a.github.io/RoomLight

### 一句话总结
该论文提出 RoomLight，一种基于真实室内全景图及其估计深度训练的 2.5D 空间感知光照先验，用于改进室内逆渲染中的光照恢复。

### 研究问题
逆渲染等不适定逆问题需要先验来约束解空间。现有学习式光照先验多依赖“远距离光照假设”，即把光照表示为远场环境贴图。这种表示难以适用于室内场景，因为室内光照会由于有限距离发光体、可见性变化和视差而在空间上高度变化，单一环境贴图难以近似。

### 核心思路/方法
论文提出一种空间感知的光照先验，训练数据为真实世界室内全景图及其估计深度。该方法使用变分自编码器学习一个紧凑、可优化的潜空间，解码得到 HDR radiance 和深度，并将结果参数化为面光源发射器，从而可直接集成到标准可微渲染管线中。通过联合建模 radiance 与深度，该先验捕捉室内光照的空间结构，而不是把光源视为无限远。摘要称该设计在学习先验的合理性保证与下游优化所需梯度流之间建立联系，并支持空间变化的光照建模。

### 主要贡献
- 提出 RoomLight，一种面向室内环境的空间感知光照先验。
- 使用真实世界室内全景图及其估计深度进行训练。
- 采用 VAE 学习紧凑、可优化的潜空间，并解码为 HDR radiance 与深度。
- 将解码结果参数化为面光源发射器，可直接接入标准可微渲染管线。
- 通过联合建模 radiance 与深度，捕捉室内光照的空间结构，而非假设光源在无限远处。
- 摘要称该方法相比现有方法能实现空间变化光照建模，并获得更高保真度的室内光照恢复。

### 局限性
摘要未提供足够信息。未提供关于失败案例、计算成本、对深度估计误差的敏感性、泛化范围外场景能力、与具体基线方法比较细节等限制信息。

### 阅读优先级
中。理由：该工作聚焦室内逆渲染中的光照先验，针对远场环境贴图假设的不足提出 2.5D 空间感知建模，并强调可接入可微渲染管线，对神经渲染、逆渲染和室内光照建模方向具有相关性。但由于摘要未给出定量结果、基线细节与局限分析，是否值得优先精读取决于读者对室内光照先验与可微渲染结合的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Ill-posed inverse problems require priors to constrain the solution space toward plausible outcomes. In inverse rendering, learned priors modeling the distribution of natural illumination improve the recovery of scene properties. However, existing models rely on the distant-illumination assumption, representing lighting as a far-field environment map. This limits their applicability to indoor scenes, where illumination is highly spatially varying due to finite-distance emitters, visibility changes, and parallax, all of which are poorly approximated by a single environment map. To address this, we introduce a spatially-aware illumination prior trained on real-world indoor panoramas and their estimated depth. Our variational autoencoder model learns a compact, optimizable latent space that decodes into HDR radiance and depth, parameterizing an area light emitter for direct integration into standard differentiable rendering pipelines. This design bridges the plausibility guarantees of a learned prior with the gradient flow required for downstream optimization. Crucially, by jointly modeling radiance and depth, our prior captures the spatial structure of indoor illumination, instead of treating the light sources as infinitely distant. We demonstrate that this formulation enables spatially-varying illumination modeling and achieves higher-fidelity recovery of indoor lighting compared to existing approaches. Project page: https://andreead-a.github.io/RoomLight

</details>

#### 2026-09-23 - InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies

**Authors:** Sai Puneeth Reddy Gottam, Elmar Rueckert, Vedant Dave
**Links:** [abs](https://arxiv.org/abs/2609.27734) - [pdf](https://arxiv.org/pdf/2609.27734)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, scene representation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies
- 作者：Sai Puneeth Reddy Gottam, Elmar Rueckert, Vedant Dave
- 出版日期：2026-09-23T11:47:58Z
- 分类：Neural Scene Representations & Rendering（二级分类：摘要未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.27734) | [PDF](https://arxiv.org/pdf/2609.27734)

### 一句话总结
InfiNoVA 通过将多相机演示重建为时变 3D 高斯表示并渲染新视角观测，为 VLA 策略提供密集且几何一致的视角增强，从而提升其在未见视角下的操作成功率。

### 研究问题
视觉-语言-动作（VLA）策略往往强依赖训练时所见相机视角，导致在未见视角下部署时性能显著下降。从足够多样的物理视角采集演示成本高昂，且对视角空间的覆盖仍然稀疏。

### 核心思路/方法
- 将同步多相机演示转换为密集、几何一致的训练视角分布。
- 把每条操作轨迹重建为时变 3D 高斯表示。
- 从采样的相机位姿渲染新观测，同时保留原始状态-动作对应关系。
- 该显式场景表示旨在提升帧级保真度与时间一致性，并减少生成式新视角合成中出现的任务关键幻觉。

### 主要贡献
- 提出 InfiNoVA 数据增强框架，用于将同步多相机演示转化为密集的几何一致训练视角。
- 在四个真实世界操作任务中，使用 InfiNoVA 训练的策略在未见随机视角下平均成功率比 VISTA 基线增强和未增强策略高 5.4 倍。
- 相比直接在全部五个物理相机视角上训练，InfiNoVA 成功率再高 1.7 倍。
- 结果表明，密集且几何 grounded 的视角增强可在不修改底层策略架构的情况下提升机器人策略的相机鲁棒性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直面 VLA 策略在视角泛化上的关键痛点，提出了不改变策略架构的数据增强方案，并报告了在真实世界任务中相对多个基线的显著提升；问题重要、方法思路清晰、结果量化明确，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies often rely strongly on the camera viewpoints seen during training, causing substantial performance degradation when deployed from unseen perspectives. Collecting demonstrations from sufficiently diverse physical viewpoints is expensive and still provides only sparse coverage of the viewpoint space. We introduce InfiNoVA, a data-augmentation framework that converts synchronized multi-camera demonstrations into a dense distribution of geometrically consistent training views. InfiNoVA reconstructs each manipulation trajectory as a time-varying 3D Gaussian representation and renders novel observations from sampled camera poses while preserving the original state-action correspondence. This explicit scene representation improves frame-level fidelity and temporal consistency while reducing task-critical hallucinations observed in generative novel-view synthesis. Across four real-world manipulation tasks, policies trained with InfiNoVA achieve 5.4x higher average success under unseen randomized viewpoints than both VISTA-based augmentation and the unaugmented policy. InfiNoVA further achieves 1.7x higher success than training directly on all five physical camera views. These results show that dense, geometrically grounded viewpoint augmentation provides a practical route toward camera-robust robot policies without modifying the underlying policy architecture.

</details>

#### 2026-09-23 - GaussPDE: Graph-Based Partial Differential Equation-Driven Rendering for 3D Gaussian Splatting

**Authors:** Haoyuan Yue, Fengyuan Ye, Ziyin Li
**Links:** [abs](https://arxiv.org/abs/2609.27264) - [pdf](https://arxiv.org/pdf/2609.27264)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussPDE: Graph-Based Partial Differential Equation-Driven Rendering for 3D Gaussian Splatting
- 作者：Haoyuan Yue, Fengyuan Ye, Ziyin Li
- 出版日期：2026-09-23T02:48:35Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.27264) | [PDF](https://arxiv.org/pdf/2609.27264)

### 一句话总结
GaussPDE 在预训练 3D 高斯场景上直接构建高斯图并演化偏微分方程，通过修改球谐直流颜色系数实现稳定、可控且空间连贯的动态渲染，无需网格提取、体素化或重训练。

### 研究问题
如何在不进行网格提取、体素化或重训练的前提下，将物理结构化的偏微分方程动力学注入预训练的 3D 高斯场景，从而实现稳定、可控且空间连贯的动态可视化。摘要指出，PDE 渲染不仅需要准确的外观，还需要可靠的离散计算域。

### 核心思路/方法
- 在 3DGS 重建阶段引入相机感知正则化，抑制相机附近的浮动体和过大的基元，以避免它们造成不稳定的图拓扑。
- 使用协方差感知距离以及不透明度、外观和边界感知电导，构建活跃高斯图。
- 在高斯基元上直接进行质量加权的图拉普拉斯 PDE 演化。
- 将演化中的标量 PDE 状态耦合回渲染：修改球谐直流颜色系数，同时保持几何、不透明度和视角相关渲染行为。

### 主要贡献
- 提出 GaussPDE 框架，将物理结构化的 PDE 动力学注入预训练 3D 高斯场景，且无需网格提取、体素化或重训练。
- 指出 PDE 渲染依赖可靠的离散计算域，并通过相机感知正则化改善图拓扑稳定性。
- 构建基于协方差感知距离与多属性电导的活跃高斯图，实现质量加权图拉普拉斯 PDE 演化。
- 通过修改球谐直流颜色系数将 PDE 状态耦合到渲染，同时保持几何、不透明度和视角相关渲染行为。
- 在真实与合成场景上的实验显示，相较基线方法，GaussPDE 产生稳定、可控、空间连贯的动态可视化，并减少跨边界泄漏。

### 局限性
摘要未提供足够信息。摘要未说明方法的计算开销、对复杂拓扑或大幅形变的适用性、对超参数的敏感性、具体失败案例，也未提供定量指标细节。

### 阅读优先级
中。理由：该工作面向 3D Gaussian Splatting 与 PDE 驱动渲染的交叉方向，提出无需网格提取、体素化或重训练的动态渲染思路，并强调图拓扑稳定性与跨边界泄漏改善，对神经场景表示与渲染方向的研究者具有参考价值；但摘要未提供定量结果、计算成本与失败案例分析，实际价值需进一步阅读全文验证。

</details>

<details>
<summary>Abstract</summary>

We present GaussPDE, a framework that injects physically structured partial differential equation (PDE) dynamics into pretrained 3D Gaussian scenes without mesh extraction, voxelization, or retraining. Our key observation is that PDE rendering requires not only accurate appearance, but also a reliable discrete computational domain. We therefore first introduce camera-aware regularization during 3DGS reconstruction to suppress camera-near floaters and oversized primitives that would create unstable graph topology. We then construct an active Gaussian graph using covariance-aware distances and opacity, appearance, and boundary-aware conductance, enabling mass-weighted graph Laplacian PDE evolution directly over Gaussian primitives. The evolving scalar PDE state is coupled back to rendering by modifying the direct-current spherical harmonic color coefficients while preserving geometry, opacity, and view-dependent rendering behavior. Experiments on real and synthetic scenes show that GaussPDE produces stable, controllable, and spatially coherent dynamic visualizations, with reduced cross-boundary leakage compared with baselines.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-28 - Terrain-Aware Autonomous Planetary Exploration for Exteroceptive-Proprioceptive Mapping with Quadruped Scouts

**Authors:** Alberto Sanchez-Delgado, João Carlos Virgolino Soares, Victor Barasuol, Claudio Semini
**Links:** [abs](https://arxiv.org/abs/2609.35493) - [pdf](https://arxiv.org/pdf/2609.35493)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation

<details>
<summary>Abstract</summary>

Autonomous planetary exploration requires robots to navigate unknown, uneven terrain while assessing risk, traversability, and energetic cost. Quadruped scouts are well suited for this task because they can traverse irregular surfaces and gather mobility-relevant information during locomotion. This paper presents a terrain-aware exploration framework that combines exteroceptive and proprioceptive mapping for a quadruped robot in lunar-like environments. An onboard RGB-D camera builds robot-centered elevation maps, estimates geometric traversability, and derives navigation costs for autonomous planning. In parallel, proprioceptive measurements provide interaction-aware terrain cues that complement geometry-based assessment. Local maps are incrementally registered into a global multi-layer representation, which is used by an exploration module to select targets in unexplored regions of interest. The targets are reached by an autonomous navigation system that guides collision-aware motion using the available map and cost layers. Simulation results on NVIDIA Isaac Sim show autonomous exploration, map expansion, and spatial association between terrain geometry and robot-terrain interaction. Subsequent navigation using this information exhibits lower average Cost of Transport (CoT) than initial exploration.

</details>

#### 2026-09-28 - DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library

**Authors:** Youhui Wang, Yunzhu Li, Li Fei-Fei, Jiajun Wu, Huang Huang
**Links:** [abs](https://arxiv.org/abs/2609.35318) - [pdf](https://arxiv.org/pdf/2609.35318)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Human videos offer a scalable source of demonstrations for dexterous robot manipulation. However, existing human-to-simulation-to-robot (Human2Sim2Robot) pipelines rely on predefined procedures that struggle to accommodate diverse object properties and interactions, particularly those involving articulated and deformable objects. We introduce DexAgent, an agentic Human2Sim2Robot framework that converts a single egocentric human video and a task prompt into physically grounded robot trajectories for policy training. It operates through four stages: semantic understanding of human videos, property-based simulation reconstruction, robot trajectory optimization, and robot data generation. At each stage, DexAgent adapts its approach to the task and object properties by selecting suitable skills from its tool library or developing new ones when needed. Property-specific verifiers assess stage outcomes for physical validity and task-specific requirements and provide feedback for refinement, preventing error propagation through the workflow. This adaptive, verification-guided process allows DexAgent to process diverse objects and long-horizon tasks. In the final stage, DexAgent varies object and robot states in simulation to generate diverse robot trajectories from a single human video, then retextures the rendered observations to facilitate sim-to-real transfer. Newly developed skills and verifiers are retained in its tool library, making it self-evolving to accumulate reusable capabilities. This reduces processing time as DexAgent encounters more human videos. Across eleven real-world tasks, policies trained with DexAgent-generated data achieve a 3.5x higher success rate than competing baselines. Project website: https://dexagent123.github.io/.

</details>

#### 2026-09-28 - MarsLab: A Martian Rover Simulator for Planetary Rover Autonomous Navigation

**Authors:** Hoyun Kim, Beomsu Kim, Giseop Kim
**Links:** [abs](https://arxiv.org/abs/2609.34702) - [pdf](https://arxiv.org/pdf/2609.34702)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** simultaneous localization and mapping, SLAM, robotics, mapping, localization, simulation

<details>
<summary>Abstract</summary>

Future Mars missions will require rover autonomy that can operate across unstructured terrain, changing illumination, atmospheric dust, and limited communication. Simulation is a practical way to study these conditions before deployment, but existing Mars-relevant resources differ in scope, including mission-oriented simulators, fixed analog datasets, task-specific environments, and open robotics interfaces. In this context, we present MarsLab, an open-source, ROS2-native Mars rover simulator for autonomy and navigation algorithm development. MarsLab combines HiRISE-derived and procedural terrain with customizable rock, crater, solar-illumination, and atmospheric-dust settings, and runs a Perseverance-class rover model in NVIDIA Isaac Sim. The runtime publishes RGB, depth, RGB-D point clouds, LiDAR, IMU, wheel odometry, and Ground Truth (GT) pose data through standard ROS2 topics. We demonstrate MarsLab with Simultaneous Localization and Mapping (SLAM) benchmarks across sensing modalities, dust levels, scene geometry, and route length, and with Visual Place Recognition (VPR) benchmarks over repeated Mars Base traversals under illumination and dust changes. The results illustrate how controlled scene variation and shared GT trajectories can be used to compare trajectory-level estimation and image-level place recognition within the same simulator. Our Project Page: https://kimhoyun-robotair.github.io/MarsLab/.

</details>

#### 2026-09-28 - When the Score Becomes the Target: Rethinking Metric Validity in Autonomous Driving

**Authors:** Morui Zhu, Deyuan Qu, Qi Chen, Kentaro Oguchi, Qing Yang
**Links:** [abs](https://arxiv.org/abs/2609.34440) - [pdf](https://arxiv.org/pdf/2609.34440)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>Abstract</summary>

Driving benchmark scores are increasingly used not only for evaluation but also as optimization targets. This raises a fundamental question: do score gains remain reliable evidence of driving improvement once the score itself is optimized? We address this question by examining how the scoring process responds to changes in driving behavior and whether the resulting gains persist under repeated execution and replanning. We decompose the process into execution, measurement, subscore mapping, and aggregation. Controlled interventions reveal substantial behavioral changes that receive little score response because distinctions are omitted, thresholded, or attenuated between requested and executed motion. Closed-loop comparisons further show that optimization gains can reverse when the execution interface changes, demonstrating their dependence on how requests are executed and returned as feedback. Together, these findings connect the behavioral distinctions preserved by a metric to the conditions under which its gains transfer. Metric validity under optimization therefore requires examining both what the scoring process measures and how the optimized behavior is executed.

</details>

#### 2026-09-28 - UMR: Universal Manipulation Representation

**Authors:** Song Liu, Linyi Li, Yanshun Zhao, Rxuan Li, Xinrui Xu, Yi Ju, Yahui Deng, Senge Zhang, Guoyu Liu, Yixuan Li, Wuyang Zhang, Yao Li, Congcong Zhu, Jingrun Chen
**Links:** [abs](https://arxiv.org/abs/2609.34256) - [pdf](https://arxiv.org/pdf/2609.34256)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

General-purpose embodied manipulation hinges on a unified action representation that generalizes across embodiments and scales readily. Yet existing policies rely on embodiment-specific action spaces, making cross-embodiment demonstrations difficult to leverage at scale and limiting transfer to new embodiments and spatial variations. To this end, we introduce Universal Manipulation Representation (UMR), a unified action representation that enables zero-shot skill transfer from human demonstrations to heterogeneous robots. UMR decomposes manipulation into two functionally distinct yet geometrically linked components: embodiment-agnostic World Flow, which describes task-relevant object motion in the world frame, and Ego Trajectory, which represents end-effector motion relative to the current pose. We instantiate UMR as World--Ego Point VLA (WEPVLA), a compact 0.5B-parameter policy that learns in the unified geometric action space through a dual-stream Point Action Adapter and a unified Point Action Expert, with an $SE(3)$ conjugation coupling the two components. To improve data efficiency, we complement UMR with a Data-Efficient Strategy (DES) that diversifies object configurations through stage-aware point-cloud editing while preserving demonstrated contact geometry. In simulation, WEPVLA achieves average success rates of 97.5\% on LIBERO and 85.7\% on the 10-task RLBench benchmark. In real-world experiments, a single policy trained on human demonstrations augmented by DES transfers zero-shot to diverse deployment conditions. With about 10 minutes of collected human demonstrations per task and no robot demonstrations, it achieves 91.7\% average success across six evaluation settings, compared with 60.8\% for HumanEgo. Code and additional materials are available at https://umr-wepvla.github.io/.

</details>

#### 2026-09-27 - 3D Point Tracking with State Space Models

**Authors:** Masahiro Ogawa, Qi An, Atsushi Yamashita
**Links:** [abs](https://arxiv.org/abs/2609.34035) - [pdf](https://arxiv.org/pdf/2609.34035)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, 4D reconstruction, robot navigation, autonomous driving

<details>
<summary>Abstract</summary>

Tracking any point of a dynamic scene in metric 3D - in absolute meters, not up to an unknown scale - underpins 3D and 4D reconstruction, robot navigation, and autonomous driving, where decisions are made in meters, not pixels. Our objective is a 3D point tracker accurate in those absolute terms and operating within a single commodity GPU, pose-free, monocular budget. Our method rests on one observation: once a point's 2D image trajectory is fixed, the quantity that governs its metric accuracy is the depth along its pixel ray. Rather than learning tracking end-to-end, we therefore compose two frozen front-ends - dense optical flow for 2D correspondence and a monocular metric-depth network for the third dimension - and learn only the residual they cannot supply: that depth, refined by a compact state space model (Mamba-3) conditioned on appearance features (DINOv3). A state space model rather than the transformers the strongest 3D trackers adopt is what makes a single-GPU budget attainable: it summarises a track in a fixed-size recurrent state whose memory cost is constant in the number of frames, whereas attention requires a key-value cache that grows linearly with them. On the TAPVid-3D minival benchmark our best configuration attains the highest absolute metric accuracy among methods evaluated under identical conditions (mean metric Average Jaccard, 0.256), exceeding strong feed-forward trackers, while a companion analysis, reproduced with each competitor's own evaluator, explains why several published trackers lose most of their accuracy under this budget.

</details>

#### 2026-09-27 - DexTaG: Tactile-as-Guidance in Reinforcement Learning for Dexterous Manipulation

**Authors:** Han Yang, Yian Wang, Yunlong Song, Zhenjia Xu, Chuang Gan
**Links:** [abs](https://arxiv.org/abs/2609.33882) - [pdf](https://arxiv.org/pdf/2609.33882)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Glove-based motion capture is emerging as a scalable approach to collecting dexterous-hand demonstration data. However, due to the kinematic gap between the human and robot hand, the recorded human motions cannot be executed directly on the robot, especially for contact-rich tool-use tasks involving in-hand reorientation. Prior work bridges this gap in simulation through reinforcement learning (RL) or trajectory optimization, but the human contact pattern is hard to preserve under such formulations, often producing unnatural manipulation and unstable functional grasps. These methods also train a separate policy or solve a separate optimization for each reference trajectory, which is inefficient. To solve these problems, we propose DexTaG, a tactile-guided RL framework for dexterous manipulation. During training, tactile signals captured by the glove guide policy search toward the measured human contact pattern, reducing reliance on precise reference geometry for contact supervision. To improve efficiency, we train a single generalizable retargeter jointly on all training trajectories of the same object. The retargeter is further distilled into a tactile-free student controller conditioned on the target object trajectory for real-world deployment. On marker-pen and hammer manipulation tasks, DexTaG learns natural, contact-rich behaviors that baselines with distance-based contact heuristics fail to learn, generalizes to held-out trajectories of the same object and task, and outperforms single-trajectory baselines on OakInk2.

</details>

#### 2026-09-27 - SLIP-VLA: Single-Step Latent Imagination for Policy Learning in Vision-Language-Action Models

**Authors:** Tianfu Li, Haoxuan Xu, Wenbo Chen, Haitian Li, Changchuan Yang, Xinhu Zheng, Jun Ma, Yuan Liu, Lujia Wang, Haoang Li
**Links:** [abs](https://arxiv.org/abs/2609.33575) - [pdf](https://arxiv.org/pdf/2609.33575)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world modeling

<details>
<summary>Abstract</summary>

Vision-Language-Action models are increasingly effective for robotic manipulation, yet most predict actions directly from current observations without explicitly modeling future scene evolution. Recent methods introduce future prediction to improve action generation, but dense future modeling often requires expensive iterative denoising, while one-step alternatives can underperform their multi-step counterparts. To reconcile efficient future modeling with strong action performance, we present SLIP-VLA, a policy learning framework that equips VLA models with a Single-Step Latent Imagination for future-aware action prediction. SLIP-VLA obtains temporally dense future latent representations with a single denoising update, and we improve the perceptual sufficiency of these representations by aligning intermediate latents with future geometric and semantic features. We further improve their control sufficiency through action-conditioned latent world modeling and inverse dynamics modeling, explicitly coupling latent transitions with robot actions. SLIP-VLA achieves state-of-the-art performance across diverse simulation benchmarks and real-world manipulation tasks, while its single-step latent imagination takes only 12 ms.

</details>

#### 2026-09-27 - SceneScaffold: Active Scene-State Construction for Unified 3D Scene Understanding

**Authors:** Xiangqi Li, Libo Huang, Jiarui Zhao, Weilun Feng, Chuanguang Yang, Zhulin An, Yongjun Xu
**Links:** [abs](https://arxiv.org/abs/2609.33518) - [pdf](https://arxiv.org/pdf/2609.33518)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, scene understanding

<details>
<summary>Abstract</summary>

Recent 3D large multimodal models (3D-LMMs) rely on a visual bottleneck to compress complex 3D scene evidence into a limited number of visual tokens compatible with large language models (LLMs). Current visual bottlenecks, however, often passively compress heterogeneous 3D evidence into a homogeneous object-centric token sequence, leaving the spatial organization of the scene under-represented. This under-representation forces the LLM to recover spatial relations from a flattened token sequence, leading to unstable reasoning in relation-intensive and spatially ambiguous scenes. To address this issue, we propose SceneScaffold, an active scene-state construction framework for unified 3D scene understanding. SceneScaffold reformulates the visual bottleneck from a passive feature compressor into an active scene organizer, constructing a role-aware spatial scaffold before language reasoning. Specifically, SceneScaffold organizes superpoint-level visual evidence into scene-state components with distinct structural roles: entity states preserve core object semantics, scene-frame states maintain spatial references via boundary and region anchors, relation states encode object-environment interaction cues, and a global summary provides compact context. Through this role-aware construction, SceneScaffold provides the LLM with a spatially organized scene representation before language reasoning. Experiments on unified 3D scene understanding tasks, including 3D visual grounding, question answering, and dense captioning, demonstrate the effectiveness of SceneScaffold, while diagnostic results further show its applicability to relation-intensive and spatially ambiguous cases. Code is available at https://github.com/lixiangqi707/SceneScaffold.

</details>

#### 2026-09-26 - Scanning While Imagining: A Scene-Graph World Model for Robotic Ultrasound Navigation

**Authors:** Xuesong Li, Shuai Chen, Feng Li, Zhongliang Jiang, Nassir Navab, Yuan Bi
**Links:** [abs](https://arxiv.org/abs/2609.32837) - [pdf](https://arxiv.org/pdf/2609.32837)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>Abstract</summary>

Ultrasound (US) acquisition depends on the operator's ability to interpret anatomy and anticipate how the view will change with probe motion. Many robotic US navigation methods select actions without explicitly predicting these anatomical changes. We propose SonoGraph-WM, an action- and goal-conditioned world model for anticipatory probe navigation. The model represents anatomy as scene graphs (SGs), capturing visible structures, their geometry, and spatial relationships without synthesizing US images. Given a history of SGs and probe poses, a unified Transformer jointly predicts future SGs and poses. A receding-horizon planner recursively imagines candidate trajectories, selects the shortest predicted path reaching a goal graph, and follows it over a short execution horizon before replanning from new observations. To reduce reliance on tracked and anatomically annotated US sequences, we generate aligned SG--pose training data from computed tomography (CT) label maps along surface-constrained probe trajectories. On four held-out CT cases, spatial relation F1 remains above 93% over 20 prediction steps, and closed-loop navigation achieves 77.50% and 75.00% success for the gallbladder and pancreas, respectively, using annotation-derived SGs. In robot--phantom navigation experiments with label-map-derived SGs, the planner reached the target view in 73.7% of trials. These findings support CT-supervised anatomical world modeling for probe planning and highlight the importance of frequent observation updates for reliable navigation. Project Page: https://noseefood.github.io/us-sonograph-wm/

</details>

#### 2026-09-24 - Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage

**Authors:** Yuncong Yang, Jinlong Li, Yulong Xue, Feng Wu, Chunwen Zhang, Lei Qiao, Xuyang Wang
**Links:** [abs](https://arxiv.org/abs/2609.30214) - [pdf](https://arxiv.org/pdf/2609.30214)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage
- 作者：Yuncong Yang, Jinlong Li, Yulong Xue, Feng Wu, Chunwen Zhang, Lei Qiao, Xuyang Wang
- 出版日期：2026-09-24T17:45:42Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.30214

### 一句话总结
该论文提出一种面向近场重载水下 ROV 打捞任务的对象中心多视角预测世界模型，在不依赖接触传感器的情况下，从同步多视角 RGB 观测与载具控制信号中预测任务对象状态在接触交互和水动力滞后下的潜在演化。

### 研究问题
近场重载水下 ROV 打捞任务中，缺少接触传感器时，如何从同步多视角 RGB 观测和载具控制信号中预测任务对象状态随接触交互与载具水动力滞后的演化。

### 核心思路/方法
- 提出 Underwater C3-JEPA（cross-view, control-conditioned, context-extended），一种对象中心多视角预测世界模型。
- 将多相机观测编码为任务对象 token 与上下文 token。
- 通过 held-out-view attention 融合跨相机证据。
- 以控制信号为条件直接预测未来状态。
- 使用弱绑定（weak binding）以低标注成本锚定目标与夹爪。
- 使用 SIGReg 锐化几何表示。
- 所得预测接口支持模型预测控制（MPC）候选评估与 imagined-rollout 行为智能体训练。

### 主要贡献
- 提出对象中心、跨视角、控制条件化、上下文扩展的水下预测世界模型架构。
- 在不使用接触传感器的条件下，于潜在空间中预测接触交互与水动力滞后下的任务对象状态演化。
- 采用 held-out-view attention 进行跨相机证据融合，并引入弱绑定与 SIGReg 降低标注成本、增强几何表示。
- 实验表明，相比无重建的潜在基线，所学表示向下游探针传递了显著更多任务相关信息，同时保持预测器轻量。
- 在真实水下视频上验证同一架构可恢复被留出相机的对象状态并优于 persistence 基线，表明该方案可迁移至仿真之外。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集规模、任务成功率、MPC 实际部署效果与计算开销细节。
- 摘要未提供足够信息说明弱绑定与 SIGReg 的消融结果、失败案例或跨域泛化边界。
- 摘要未提供足够信息说明与更广泛世界模型或水下感知方法的系统对比。

### 阅读优先级
中。理由：该工作面向水下 ROV 打捞这一具体具身任务，提出多视角、控制条件化、对象中心的预测世界模型，并强调无接触传感器下的潜在状态预测与真实水下视频验证，对水下机器人操作、世界模型与 MPC 结合方向有参考价值；但摘要未提供充分的实验细节与对比信息，需进一步阅读正文才能判断其实际性能与通用性。

</details>

<details>
<summary>Abstract</summary>

We present Underwater C$^{3}$-JEPA (cross-view, control-conditioned, context-extended), an object-centric multi-view predictive world model for near-field heavy-load underwater ROV salvage. Without contact sensors, it predicts in latent space how the task-object state evolves through contact interaction and under the hydrodynamic lag of the vehicle, from synchronized multi-view RGB observations and vehicle control signals. C$^{3}$-JEPA encodes multi-camera observations into task-object and context tokens, fuses cross-camera evidence through held-out-view attention, and directly predicts future states conditioned on control. Weak binding anchors the target and gripper at low annotation cost, while SIGReg sharpens the geometric representation. Experiments show that the learned representation transfers substantially more task-relevant information to downstream probes than a reconstruction-free latent baseline, while keeping the predictor lightweight. The resulting predictive interface supports model-predictive-control (MPC) candidate evaluation and imagined-rollout behavior-agent training. Validation on real underwater video shows the same architecture recovering a withheld camera's object state and staying ahead of persistence, so the recipe transfers beyond simulation.

</details>

#### 2026-09-24 - S2Planner: Multi-Scale Semantic Planner for End-to-End Autonomous Driving

**Authors:** Zhaowei Lu, Liguo Zhou, Yujie Guo, Lei Yu, Alois Knoll
**Links:** [abs](https://arxiv.org/abs/2609.29813) - [pdf](https://arxiv.org/pdf/2609.29813)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S2Planner: Multi-Scale Semantic Planner for End-to-End Autonomous Driving
- 作者：Zhaowei Lu, Liguo Zhou, Yujie Guo, Lei Yu, Alois Knoll
- 出版日期：2026-09-24T13:48:08Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.29813 ，PDF：https://arxiv.org/pdf/2609.29813

### 一句话总结
S2Planner 是一种结合三个前视相机、自车运动历史与当前驾驶指令的轨迹规划器，通过自车条件化的轨迹初始化与多尺度图像特征的迭代几何引导采样来细化候选路点。

### 研究问题
面向端到端自动驾驶的轨迹规划问题：如何利用多相机图像、自车运动历史与驾驶指令，生成并细化候选路点，以提升规划性能。摘要未提供足够信息说明该问题在其他方法中的具体不足或论文所针对的确切研究缺口。

### 核心思路/方法
- 输入：三个前视相机、自车运动历史、当前驾驶指令。
- 视觉特征：使用微调后的 DINOv3 骨干网络与 Spatial Tuning Adapter，生成多尺度图像特征。
- 解码：采用粗到细解码器，结合轨迹自注意力（trajectory self-attention）与相机投影交叉注意力（camera-projected cross-attention）来细化候选路点。
- 方法定位：作者强调贡献在于“自车条件化的轨迹初始化”与“对多尺度图像特征的迭代、几何引导采样”的整合，而非提出新的视觉骨干网络或注意力算子。

### 主要贡献
- 提出 S2Planner 轨迹规划器，整合自车条件化轨迹初始化与迭代、几何引导的多尺度图像特征采样。
- 在 NAVSIM v1 non-reactive 评测上，先前报告的 navtest 运行获得 88.03 PDMS。
- 明确说明该结果因基于 navtest 性能进行选择而属于探索性结果，不能解释为无偏测试估计。

### 局限性
- 88.03 PDMS 来自基于 navtest 性能选择的运行，属于探索性结果，不能作为无偏测试估计。
- 摘要指出仍需在未曝光数据上进行验证集选择的评测、重复运行以及计算量测量，以确立泛化性与效率。
- 除上述内容外，摘要未提供足够信息说明其他局限性（如具体失败场景、消融细节、真实道路测试等）。

### 阅读优先级
中。理由：该工作聚焦端到端自动驾驶轨迹规划，方法整合了自车条件初始化与多尺度特征迭代采样，并给出 NAVSIM v1 上的 PDMS 数值，具有一定相关性；但摘要明确该数值为探索性、缺乏无偏测试估计与效率测量，且作者自述贡献是整合而非新骨干或新注意力算子，因此对追求稳健实证结论的读者优先级为中等。

</details>

<details>
<summary>Abstract</summary>

We present S2Planner, a trajectory planner that combines three front-facing cameras with ego-motion history and the current driving command. A fine-tuned DINOv3 backbone and a Spatial Tuning Adapter produce multi-scale image features; a coarse-to-fine decoder then uses trajectory self-attention and camera-projected cross-attention to refine candidate waypoints. The contribution is the integration of ego-conditioned trajectory initialization with iterative, geometry-guided sampling of multi-scale image features, rather than a new visual backbone or attention operator. On the NAVSIM v1 non-reactive evaluation, the previously reported navtest run obtained 88.03 PDMS. Because that run was selected using navtest performance, this number is exploratory and cannot be interpreted as an unbiased test estimate. Validation-selected evaluation on unexposed data, repeated runs, and computational measurements are needed to establish generalization and efficiency.

</details>

#### 2026-09-24 - Frame-to-Panorama Localization and Context-Aware Sampling for Scene-Specific Ship Detection in a Smart Marina Testbed

**Authors:** Ignat Romanov, Andreas Hadjipieris, Neofytos Dimitriou
**Links:** [abs](https://arxiv.org/abs/2609.29447) - [pdf](https://arxiv.org/pdf/2609.29447)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Frame-to-Panorama Localization and Context-Aware Sampling for Scene-Specific Ship Detection in a Smart Marina Testbed
- 作者：Ignat Romanov, Andreas Hadjipieris, Neofytos Dimitriou
- 出版日期：2026-09-24T12:05:00Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.29447

### 一句话总结
该论文提出一套面向历史PTZ海事视频的数据整理流程，通过帧到全景图的定位与上下文感知采样，将大量冗余视频帧压缩为紧凑且场景特定的训练集，用于船舶检测。

### 研究问题
智能海事基础设施虽能持续提供异构传感流，但仅有传感硬件不足以支持场景特定模型开发。历史视频流需要被空间索引、情境化，并缩减为可供标注的信息密集子集。论文针对的问题是：在缺乏可靠 pan、tilt、zoom 元数据的历史 PTZ 海事视频中，如何构建紧凑、场景特定且空间与上下文多样的船舶检测训练集，以减少标注负担。

### 核心思路/方法
论文提出一个端到端的数据整理流程，主要包含两个阶段：
1. 帧到全景图定位：使用 SuperPoint 和 LightGlue 将历史 PTZ 视频帧定位到参考全景图上，从而恢复相机视角信息，并加入天气与太阳状态元数据。
2. 上下文感知采样：先通过多样性采样保留相机视角与环境条件的变化；再针对地平线附近远距离船舶的样本不足问题，使用图块级视觉嵌入和高斯混合模型聚类进行第二阶段采样。

### 主要贡献
- 提出一种从缺乏可靠 PTZ 元数据的历史视频中恢复相机视角信息的方法，并结合环境上下文与视觉多样性构建紧凑、场景特定的训练集。
- 设计了两阶段采样流程：多样性采样保持视角与环境条件变化，上下文感知采样针对远距离船舶的欠代表样本进行补充。
- 在 CMMI MDigi-I Smart Marina 测试平台中应用该流程，将 40,718 个候选帧减少到 220 张标注图像，减少 99.5%。
- 在该子集上微调的 YOLO26-m 检测器在按序列分组的五折交叉验证下取得 mean AP50 为 94.78% ± 0.51%，mean AP50-95 为 75.10% ± 1.73%。
- 结果表明高冗余基础设施视频流可被转化为紧凑、空间与上下文多样的训练集，用于场景特定检测器适配，并显著降低标注成本。

### 局限性
摘要未提供足够信息。摘要未说明该流程在缺乏参考全景图、极端天气或不同测试平台下的泛化能力；也未提供失败案例、误检分析、计算开销、标注成本量化对比或与其他采样策略的消融实验细节。

### 阅读优先级
中。理由：该论文聚焦海事场景下的数据整理与采样，方法明确、指标清晰，且宣称大幅减少标注量，适合关注数据高效标注、场景特定检测适配和智能基础设施视觉应用的读者。但摘要未提供额外兴趣方向，且分类偏向具身/机器人/AR应用，若读者主要关注通用目标检测架构创新，优先级可能有限。

</details>

<details>
<summary>Abstract</summary>

Smart maritime infrastructures provide continuous access to heterogeneous sensing streams, enabling repeated experimentation, digital-twin development, and AI-based maritime services. However, sensing hardware alone is not sufficient for scene-specific model development: historical video streams must also be spatially indexed, contextualized, and reduced to informative subsets for annotation. This paper presents a frame-to-panorama localization and context-aware sampling pipeline for ship detection in historical PTZ maritime video lacking reliable pan, tilt, and zoom metadata. The main contribution is an end-to-end data-curation approach that recovers camera-view information from historical PTZ video and combines it with environmental context and visual diversity to construct compact, scene-specific training sets. Specifically, frames are localized on a reference panorama using SuperPoint and LightGlue, enriched with weather and solar-state metadata, and selected through diversity sampling to preserve variation across camera view and environmental conditions. A second context-aware stage targets under-represented distant-vessel cases near the horizon using tile-level visual embeddings and Gaussian Mixture Model clustering. Applied within the CMMI MDigi-I Smart Marina testbed, the proposed pipeline reduces 40,718 candidate frames to 220 images for annotation, corresponding to a 99.5% reduction. A YOLO26-m detector fine-tuned on this subset achieves a mean AP50 of 94.78% $\pm$ 0.51% and a mean AP50-95 of 75.10% $\pm$ 1.73% under sequence-grouped five-fold cross-validation. These results demonstrate that highly redundant infrastructure video streams can be transformed into compact, spatially and contextually diverse training sets for scene-specific detector adaptation while substantially reducing annotation effort.

</details>

#### 2026-09-24 - Assessing the Impact of Fleet Size on Crowdsourced Mapping Using a Dissimilarity Measure

**Authors:** Marie-Ngoïe Badibanga Kalenda, Philippe Bonnifait, Marie-Anne Mittet
**Links:** [abs](https://arxiv.org/abs/2609.29198) - [pdf](https://arxiv.org/pdf/2609.29198)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Assessing the Impact of Fleet Size on Crowdsourced Mapping Using a Dissimilarity Measure
- 作者：Marie-Ngoïe Badibanga Kalenda, Philippe Bonnifait, Marie-Anne Mittet
- 出版日期：2026-09-24T08:08:48Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.29198 ；PDF https://arxiv.org/pdf/2609.29198

### 一句话总结
论文提出一个基于仿真框架的方法，用名为 GOSPAM 的差异度量评估车队规模对众包交通标志建图质量的影响。

### 研究问题
准确数字地图对 ADAS 和自动驾驶至关重要，但传统测绘方法维护成本高、难以扩展。众包车队方法是有前景的替代方案，然而参与车辆数量与最终地图质量之间的关系尚不清晰。论文聚焦于：车队规模如何影响众包交通标志维护的性能。

### 核心思路/方法
- 提出一个基于仿真的框架，用于评估众包交通标志维护。
- 使用差异度量 GOSPAM（Generalized Optimal SubPattern Assignment for Maps），该度量结合定位误差与检测性能，并考虑假阳性（FP）和假阴性（FN）。
- 系统对多车观测建模，包含代表性传感器噪声、检测错误和语义识别不确定性。
- 通过空间聚类与语义过滤聚合多车观测，以估计交通标志位置。
- 使用由实验车辆在含真值交通标志区域生成的仿真轨迹，评估车队规模影响；车辆数量范围为 5 到 50。
- 使用标准评估指标并与 GOSPAM 进行比较分析。

### 主要贡献
- 提出一个用于评估众包交通标志维护的仿真框架。
- 引入 GOSPAM 差异度量，将定位误差与检测性能（FP、FN）结合，用于评估众包建图质量。
- 通过仿真实验评估车队规模（5 至 50 辆车）对众包建图性能的影响。
- 结果表明 GOSPAM 可有效评估众包建图质量，例如首批车辆的贡献或大量车辆带来的改进。

### 局限性
- 摘要未提供足够信息说明仿真框架在真实场景中的泛化能力。
- 摘要未提供足够信息说明 GOSPAM 与其他标准评估指标的具体比较结果细节。
- 摘要未提供足够信息说明实验所覆盖的地理区域、交通标志类型或传感器配置的具体范围。
- 摘要未提供足够信息说明车队规模超过 50 辆或低于 5 辆时的表现。
- 摘要未提供足够信息说明该方法对通信延迟、数据隐私或车辆异构性的处理。

### 阅读优先级
中。理由：该论文关注众包建图中车队规模与地图质量的关系，并提出结合定位误差与检测性能的 GOSPAM 度量，对自动驾驶地图维护和众包感知评估有一定参考价值；但摘要未展示具体实验数值、对比细节或真实道路验证范围，是否具有广泛适用性需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Accurate digital maps are essential for Advanced Driver Assistance Systems (ADAS) or Autonomous Driving (AD), providing critical information such as road geometry, traffic signs and speed limits required by safety functions including Intelligent Speed Assistance (ISA). Maintaining these map layers using traditional surveying methods is costly and difficult to scale. Crowdsourced approaches based on fleets provide a promising alternative for continuously validating and updating map information. However, the relationship between the number of contributing vehicles and the quality of the resulting map remains poorly understood. To address this gap, this paper presents a simulation-based framework for evaluating crowdsourced traffic sign maintenance using a dissimilarity measure called GOSPAM (Generalized Optimal SubPattern Assignment for Maps), which combines localization errors with detection performance by accounting for False Positives (FP) and False Negatives (FN). The proposed system models multivehicle observations with representative sensor noise, detection errors, and semantic recognition uncertainties. Observations from multiple vehicles are aggregated using spatial clustering and semantic filtering to estimate traffic sign locations. Using simulated trajectories generated from data carried out by an experimental vehicle in an area containing ground-truth traffic signs, we assess the influence of fleet size on the performance of crowdsourced mapping. The number of vehicles ranges from 5 to 50, and performance is analyzed using standard evaluation metrics which are compared to the GOSPAM . The results show that GOSPAM can be used to effectively assess the quality of crowdsourced mapping, such as the contributions made by the first vehicles or the improvements made by numerous vehicles.

</details>

#### 2026-09-24 - Representation World Model: Learning States, Transition and Executable Plans in Representation

**Authors:** Yijun Yuan, Weicheng Zheng, Weibang Wang, Minghui Qin, Chang Sun, Junhao Huang, Kenan Li, Anmin Liu, Yicheng Yao, Hang Zhao
**Links:** [abs](https://arxiv.org/abs/2609.29171) - [pdf](https://arxiv.org/pdf/2609.29171)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Representation World Model: Learning States, Transition and Executable Plans in Representation
- 作者：Yijun Yuan, Weicheng Zheng, Weibang Wang, Minghui Qin, Chang Sun, Junhao Huang, Kenan Li, Anmin Liu, Yicheng Yao, Hang Zhao
- 出版日期：2026-09-24T07:43:35Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：https://arxiv.org/abs/2609.29171 ；PDF：https://arxiv.org/pdf/2609.29171

### 一句话总结
RWM 将状态、转移与可执行规划直接学习在表示空间中，通过在表示几何中构造潜在路径并用逆动力学恢复动作，避免递归 rollout 和动作空间搜索。

### 研究问题
现有世界模型通常在学习潜在表示的同时，学习显式的动力学模型，并依赖搜索、优化或基于策略的预测来完成规划。论文关注的问题是：能否不采用这种“表示 + 显式动力学 + 传统规划”的范式，而是把规划直接融入所学的表示几何中，从而在推理时更直接地完成规划。

### 核心思路/方法
论文提出 Representation World Model（RWM），核心是在表示空间中直接学习状态、转移和可执行计划。

与现有世界模型不同，RWM 不将潜在表示与显式动力学模型分开学习并通过搜索、优化或策略预测来做规划，而是把规划直接纳入学习到的表示几何。具体地，RWM 通过从端点表示构造潜在路径，并沿这些潜在路径局部施加逆动力学监督，来学习表示几何；这种监督要求潜在路径保留任务相关的状态和转移信息。

在推理阶段，规划通过直接在当前表示和目标表示之间构造潜在路径来完成，并使用逆动力学恢复对应动作，不需要递归 rollout，也不需要动作空间搜索。

### 主要贡献
- 提出 Representation World Model（RWM），将状态、转移和可执行计划直接学习在表示空间中。
- 将规划直接融入表示几何，而不是依赖显式动力学模型加搜索、优化或策略预测。
- 采用基于端点表示构造潜在路径并施加局部逆动力学监督的学习方式，要求路径保留任务相关的状态与转移信息。
- 推理时通过构造当前表示与目标表示之间的潜在路径，并用逆动力学恢复动作，实现无需递归 rollout 或动作空间搜索的直接规划。
- 在连续控制基准上展示了 RWM 用于直接规划的有效性；在机器人操作任务上的结果进一步显示其扩展到更复杂具身控制任务的潜力。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、基线对比、失败案例、计算开销、表示维度或任务范围等细节，因此无法基于所给信息判断其局限。

### 阅读优先级
中。理由：论文主题属于具身智能与机器人控制中的世界模型与规划方向，提出了一种将规划嵌入表示几何、避免递归 rollout 和动作空间搜索的思路，具有一定新颖性；摘要提到连续控制基准和机器人操作的初步结果，显示潜在应用价值。但当前仅有摘要和元数据，缺少实验细节、对比结果与局限性说明，因此适合作为方向性跟踪阅读，优先级为中等。

</details>

<details>
<summary>Abstract</summary>

We propose the Representation World Model (RWM), which learns states, transitions, and executable plans directly in representation space. Unlike existing world models that typically learn latent representations together with explicit dynamics models and perform planning through search, optimization, or policy-based prediction, RWM directly incorporates planning into the learned representation geometry. RWM learns the representation geometry by applying inverse-dynamics supervision locally along latent paths constructed from endpoint representations, requiring these paths to preserve task-relevant state and transition information. At inference, planning is performed by directly constructing a latent path between the current and goal representations, with inverse dynamics used to recover the corresponding actions, without recursive rollouts or action-space search. Experiments on continuous-control benchmarks demonstrate the effectiveness of RWM for direct planning, while results on robotic manipulation further show its potential to extend to more complex embodied control tasks. These results suggest that planning directly in representation space provides a promising alternative to conventional world-model planning.

</details>

#### 2026-09-24 - ReVNM: Learning-Based Visual Navigation from a Remote Camera

**Authors:** Michikuni Eguchi, Kohei Honda, Masafumi Endo, Yasuhiro Yoshimura, Ryo Yonetani
**Links:** [abs](https://arxiv.org/abs/2609.28976) - [pdf](https://arxiv.org/pdf/2609.28976)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReVNM: Learning-Based Visual Navigation from a Remote Camera
- 作者：Michikuni Eguchi, Kohei Honda, Masafumi Endo, Yasuhiro Yoshimura, Ryo Yonetani
- 出版日期：2026-09-24T03:43:13Z
- 分类：Embodied / Robotics / AR Applications（主分类）；二级分类：摘要未提供足够信息
- 链接：abstract_url: https://arxiv.org/abs/2609.28976；pdf_url: https://arxiv.org/pdf/2609.28976

### 一句话总结
论文提出 ReVNM，利用单一远程监控相机同时作为观测来源和隐式环境地图，通过 exo2ego 模块从远程视角预测机器人自身视角的深度观测，从而在无需预建地图的情况下实现视觉导航。

### 研究问题
- 现有 Visual Navigation Models（VNMs）虽可让机器人基于自身视角视觉观测进行导航，无需几何定位与规划，但长距离导航仍依赖预建地图。
- 使用远程相机有望消除预建地图需求和机载视觉处理需求，但其有限视野替代自身视角观测后，难以实现无碰撞导航。
- 训练鲁棒 VNM 所需的大规模、多样化远程视角数据缺失，进一步加剧挑战。
- 因此，论文关注的核心问题是：如何利用远程相机作为观测来源与隐式环境地图，并克服远程视角有限视野带来的无碰撞导航困难与训练数据不足问题。

### 核心思路/方法
- 提出 Remote Visual Navigation Model（ReVNM），使用单个远程监控相机同时作为观测源和隐式环境地图。
- 扩展当前最先进的 VNM 架构，引入 exocentric-to-egocentric（exo2ego）模块，从远程相机观测中预测机器人自身视角的深度观测。
- 借助该模块，VNM 能在规划路径时考虑机器人前方的障碍物。
- 采用 learning-by-synthesis 方法，仅在随机生成、包含多样障碍物布局和相机视角的世界中训练 ReVNM，并希望无需额外微调即可泛化到真实机器人导航。
- 实验在仿真和真实世界环境中进行，摘要称结果证实了所提方法的有效性。

### 主要贡献
- 提出 ReVNM，将单一远程监控相机同时用作观测来源和隐式环境地图，以支持视觉导航。
- 设计 exo2ego 模块，将远程相机观测转换为机器人自身视角的深度观测，帮助 VNM 在路径规划中考虑前方障碍物。
- 采用 learning-by-synthesis 方式，仅在随机生成的多样障碍物布局与相机视角世界中训练，并声称无需额外微调即可泛化到真实机器人导航。
- 在仿真和真实环境中进行实验，摘要称结果验证了该方法的有效性。

### 局限性
- 摘要未提供足够信息说明方法对远程相机视野范围、安装位置、遮挡情况的具体敏感程度或失效条件。
- 摘要未提供足够信息说明 exo2ego 模块的预测误差对导航安全性和成功率的具体影响。
- 摘要未提供足够信息说明仿真与真实世界实验的规模、指标、对比基线、消融实验及定量结果。
- 摘要未提供足够信息说明“无需额外微调即可泛化到真实机器人导航”的适用边界与失败案例。
- 摘要未提供足够信息说明训练数据生成方式、随机世界分布与真实环境差异带来的潜在域偏移问题。

### 阅读优先级
高。理由：该论文针对远程相机视觉导航中“有限视野导致无碰撞导航困难”和“缺乏多样远程视角训练数据”两个关键问题提出明确方法，且涉及 VNM 架构扩展、exo2ego 模块与 learning-by-synthesis，主题与具身智能、机器人导航和视觉导航模型直接相关；若关注无需预建地图的视觉导航或远程相机辅助机器人控制，该文具有较高参考价值。不过，由于摘要未给出实验规模与定量结果，实际优先级仍需结合后续全文实验细节判断。

</details>

<details>
<summary>Abstract</summary>

Visual Navigation Models (VNMs) enable robots to navigate from egocentric visual observations without geometric localization and planning, but long-range navigation still requires pre-built maps. This paper presents the Remote Visual Navigation Model (ReVNM), which uses a single remote surveillance camera to serve as both an observation source and an implicit environmental map for visual navigation. While the use of remote cameras could eliminate the need for pre-built maps as well as onboard vision processing, their limited field of view instead of egocentric observations makes it hard to achieve collision-free navigation. The lack of existing data with diverse remote viewpoints, which are crucial for training robust VNMs, further complicates the challenge. In this work, we propose a learning-by-synthesis approach to address this two-fold challenge. Our ReVNM extends a state-of-the-art VNM architecture with an exocentric-to-egocentric (exo2ego) module that predicts an egocentric depth observation from remote-camera observations. This helps the VNM to plan a path while considering obstacles in front of the robot. Trained only on randomly generated worlds with diverse obstacle layouts and camera viewpoints, ReVNM can generalize well to real robot navigation without additional fine-tuning. Experiments in both simulation and real-world environments confirmed the effectiveness of the proposed approach.

</details>

#### 2026-09-23 - AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios

**Authors:** Zhipeng Bao, Wenjie Zhao, Tianle Zhu, Haohua Que, Chence Yang, Geng Yuan, Qianwen Li
**Links:** [abs](https://arxiv.org/abs/2609.28366) - [pdf](https://arxiv.org/pdf/2609.28366)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios
- 作者：Zhipeng Bao, Wenjie Zhao, Tianle Zhu, Haohua Que, Chence Yang, Geng Yuan, Qianwen Li
- 出版日期：2026-09-23T16:38:06Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2609.28366) / [PDF](https://arxiv.org/pdf/2609.28366)

### 一句话总结
论文提出 AnchorReasoning——一个面向长尾自动驾驶、基于 WOD-E2E 构建的视觉 grounded 推理数据集，通过 VG-CoT 监督与课程式微调，将决策关键视觉证据与推理及轨迹规划相连接。

### 研究问题
视觉语言模型（VLMs）在长尾自动驾驶中具有潜力，但现有驾驶数据集对“将决策关键的视觉证据与推理和规划相连接”所提供的监督有限。论文针对这一监督不足的问题展开研究。

### 核心思路/方法
- 构建 AnchorReasoning 数据集，基于 WOD-E2E，包含 416,119 个标注帧和 395,379 个决策关键元素，覆盖 4 个大类、19 个细粒度类型。
- 每帧组织为视觉 grounded 的思维链（VG-CoT），连接：决策关键元素的识别与定位、元素属性与含义、驾驶动作依据，以及动作与轨迹规划。
- 提出课程式监督微调策略，逐步学习上述分层能力。
- 提出一个物体尺寸感知的 grounding 指标，用于评估定位质量。
- 在八种通用、具身智能和自动驾驶专用骨干模型上进行实验。

### 主要贡献
- 提出 AnchorReasoning 数据集，为长尾自动驾驶提供视觉 grounded 的推理监督，规模为 416,119 帧、395,379 个决策关键元素，含 4 大类 19 细类。
- 提出 VG-CoT 标注组织方式，将元素识别定位、属性含义、动作依据与轨迹规划串联为一条推理链。
- 提出课程式监督微调策略与物体尺寸感知的 grounding 评估指标。
- 实验显示 VG-CoT 监督提升了 grounded 推理与轨迹预测：5-s ADE 和 FDE 分别下降 7.84 和 11.86，RFS Frame 和 Cluster 分别提升 1.66 和 1.70；同时平均减少 18.5 个推理 token，每帧推理延迟降低 0.32 秒。

### 局限性
- 摘要未提供足够信息说明数据集的具体采集条件、标注质量控制与一致性验证方式。
- 摘要未提供足够信息说明实验的完整设置、基线对比细节与消融研究。
- 摘要未提供足够信息说明该方法在真实闭环驾驶或安全关键场景中的验证情况。
- 摘要未提供足够信息说明物体尺寸感知 grounding 指标的具体定义与计算方式。
- 摘要未提供足够信息说明课程式微调各阶段的具体划分与超参数。

### 阅读优先级
高。理由：该工作同时涉及数据集构建、视觉 grounded 思维链监督、课程式微调与自动驾驶轨迹预测评测，且给出了明确的量化收益（ADE/FDE 下降、效率提升），对长尾自动驾驶与 VLM 推理规划交叉方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) offer a promising approach to long-tail autonomous driving, but existing driving datasets provide limited supervision for connecting decision-critical visual evidence with reasoning and planning. We introduce AnchorReasoning, a visually grounded reasoning dataset built on WOD-E2E, containing 416,119 annotated frames and 395,379 decision-critical elements across four major categories and 19 fine-grained types. Each frame is organized as a visually grounded chain-of-thought (VG-CoT) that links decision-critical element identification and localization, element attributes and implications, driving-action rationale, and action and trajectory planning. We further develop a curriculum supervised fine-tuning strategy that progressively learns these hierarchical capabilities, together with an object-size-aware grounding metric for evaluating localization quality. Experiments across eight general-purpose, embodied-AI, and AV-specific backbones show that VG-CoT supervision improves grounded reasoning and trajectory prediction. Across models, 5-s ADE and FDE decrease by 7.84 and 11.86, while RFS Frame and Cluster improve by 1.66 and 1.70. These gains are achieved with 18.5 fewer reasoning tokens and 0.32 s/frame lower inference latency on average, demonstrating the value of visually grounded, decision-focused supervision for VLM reasoning and planning in long-tail autonomous driving.

</details>

#### 2026-09-23 - VLMs Can Describe, But Not Measure: Object-Centric Scene Understanding for Robotic Manipulation

**Authors:** Enrico Saccon, Tommaso Faraci, Iñigo De La Ossa Zarzuelo, Luigi Palopoli, Marco Roveri, Matteo Saveriano
**Links:** [abs](https://arxiv.org/abs/2609.28184) - [pdf](https://arxiv.org/pdf/2609.28184)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth estimation, manipulation, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VLMs Can Describe, But Not Measure: Object-Centric Scene Understanding for Robotic Manipulation
- 作者：Enrico Saccon, Tommaso Faraci, Iñigo De La Ossa Zarzuelo, Luigi Palopoli, Marco Roveri, Matteo Saveriano
- 出版日期：2026-09-23T14:26:22Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2609.28184 ；PDF https://arxiv.org/pdf/2609.28184

### 一句话总结
论文提出一种由 VLM 驱动、模块化的物体级场景理解框架，通过将单次 RGB-D 观测分割为物体区域、由 VLM 标注并结合深度信息，构建与任务无关的物体中心表示，从而在保留语义能力的同时改善定位与深度估计。

### 研究问题
面向未见过环境中的机器人操作，系统既需要语义理解，也需要可靠的度量（几何）信息。摘要指出，视觉-语言模型（VLM）具备较强的语义能力，但其几何估计不够可靠。因此，论文关注如何在机器人场景理解中同时获得可靠的语义与度量信息。

### 核心思路/方法
论文提出的方法是一个 VLM 驱动、模块化的感知框架，使用现成（off-the-shelf）方法完成场景理解。具体流程为：从单次 RGB-D 观测出发，将场景分割为物体级区域；由 VLM 对这些区域进行标注；再利用深度信息进行 grounding（落地/对齐），从而构建一个与任务无关的物体中心表示。该表示还被集成到任务规划框架中，用于机器人执行。

### 主要贡献
- 提出一种模块化的、由 VLM 驱动的物体中心场景理解感知框架，基于现成方法构建。
- 从单次 RGB-D 观测生成物体级区域分割，并由 VLM 标注，再用深度信息进行 grounding，形成任务无关的物体中心表示。
- 在 151 个桌面场景上进行实验，摘要称该分解方法在保持较强语义性能的同时，相较直接 VLM 推理显著改善了定位与深度估计。
- 将该表示与任务规划框架集成，用于机器人执行。

### 局限性
摘要未提供足够信息。摘要未说明具体失败案例、适用场景边界、对特定 VLM 或分割方法的依赖程度、计算开销、真实机器人实验的规模与条件，也未给出定量指标细节与消融分析。

### 阅读优先级
中。理由：该论文聚焦 VLM 在机器人操作中的语义与几何度量分工问题，并提出模块化、物体中心的表示方法，且包含桌面场景实验与任务规划集成，对具身智能与机器人感知方向有参考价值；但摘要未提供足够的实验细节、对比方法与真实机器人验证信息，是否值得深入阅读需结合全文的定量结果与实验设置进一步判断。

</details>

<details>
<summary>Abstract</summary>

Robotic operation in previously unseen environments requires both semantic understanding and reliable metric information. While vision--language models (VLMs) provide strong semantic capabilities, their geometric estimates remain less reliable. In this paper, we propose a VLM-driven, modular perception framework for scene understanding using off-the-shelf approaches. Starting from a single RGB-D observation, the scene is segmented into object-level regions, annotated by a VLM, and grounded with depth information to construct a task-independent object-centric representation. Experiments on 151 tabletop scenes show that the proposed decomposition preserves strong semantic performance while substantially improving localization and depth estimation over direct VLM inference. The resulting representation is also integrated with a task-planning framework for robotic execution.

</details>

#### 2026-09-23 - Wave-Robust Passive AUV Localization Using FP-MUSIC

**Authors:** Usama Saqib, Ola Rønning, Andrzej Wąsowski
**Links:** [abs](https://arxiv.org/abs/2609.27712) - [pdf](https://arxiv.org/pdf/2609.27712)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wave-Robust Passive AUV Localization Using FP-MUSIC
- 作者：Usama Saqib, Ola Rønning, Andrzej Wąsowski
- 出版日期：2026-09-23T11:29:56Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.27712

### 一句话总结
针对水面波浪引起的水听器阵列六自由度扰动问题，提出利用 IMU 测量对快拍协方差进行去扭曲的定点迭代 MUSIC 算法（FP-MUSIC），以实现接收端被动的 AUV 三维定位与空间建图。

### 研究问题
在无预部署海底应答器、也无法直接访问载体自身传感器的条件下，如何对自主水下航行器（AUV）进行定位。核心困难在于：水面波浪运动带来六自由度扰动，会使阵列在相邻快拍之间发生旋转，从而降低传统子空间处理的性能。

### 核心思路/方法
- 系统构成：单个浮动水面浮标，配备水听器阵列与惯性测量单元（IMU），实现接收端被动的三维定位与空间建图。
- 核心算法 FP-MUSIC：一种定点迭代的 MUSIC 算法，利用 IMU 测量在到达方向估计之前对快拍协方差进行“去扭曲”（de-warp）。
- 距离与前后向分辨：采用子空间投影的宽带匹配滤波器解算信标距离，并利用功率不对称性进行独立的前后向识别。

### 主要贡献
- 提出接收端被动的三维定位与空间建图系统方案，仅依赖单个配备水听器阵列和 IMU 的水面浮标。
- 提出 FP-MUSIC，利用 IMU 测量在 DOA 估计前对快拍协方差去扭曲，以应对波浪引起的阵列旋转。
- 采用子空间投影宽带匹配滤波器解算信标距离，并用功率不对称性实现独立的前后向识别。
- 在多种模拟海况下评估：FP-MUSIC 相比未补偿方法显著降低定位误差，并在波浪扰动下维持稳健的三维跟踪与载体姿态估计；中等海况下，2 米信标间隔的准确率从约 45% 提升至 75%。

### 局限性
摘要未提供足够信息。摘要仅在模拟海况下给出评估结果，未提供实际海试、真实环境验证、计算复杂度、实时性、不同阵列构型或不同海况上界的表现等信息。

### 阅读优先级
中。理由：该工作面向水下被动定位中波浪扰动导致子空间处理退化的具体问题，方法思路（IMU 辅助协方差去扭曲 + 定点迭代 MUSIC）较为明确，且给出了量化的性能提升；但摘要仅覆盖模拟评估，缺乏实海况验证等关键信息，是否具备工程落地价值需进一步阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

Localizing an autonomous underwater vehicle without pre-deployed seabed transponders, or direct access to onboard vehicle sensors remains a core challenge. We present a receiver-passive 3-D localization and spatial mapping system utilizing a single floating surface buoy equipped with a hydrophone array and an inertial measurement unit (IMU). The central difficulty is that surface wave motion induces six-degree-of-freedom (6-DOF) perturbations that rotate the array between snapshots, degrading conventional subspace processing. We resolve this by introducing a fixed-point iterative MUltiple SIgnal Classification algorithm (FP-MUSIC) that uses IMU measurements to de-warp snapshot covariances prior to direction-of-arrival estimation. Furthermore, we employ a subspace-projected wideband matched filter to resolve beacon ranges and use power asymmetry for independent front-back identification. Evaluations across simulated sea states demonstrate that FP-MUSIC substantially reduces localization error relative to uncompensated methods and sustains robust 3-D tracking and vehicle orientation estimation under wave-induced motion. At moderate sea state, FP-MUSIC increases the 2-m beacon-separation accuracy from approximately 45% to 75%.

</details>

#### 2026-09-23 - DAVIO: Dense Monocular-Inertial SLAM with Feed-Forward Initialization and Pose-Conditioned Mapping

**Authors:** Jaafar Mahmoud, Arthur Movsesyan, Mikhail Iumanov, Sergey Kolyubin
**Links:** [abs](https://arxiv.org/abs/2609.27702) - [pdf](https://arxiv.org/pdf/2609.27702)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DAVIO: Dense Monocular-Inertial SLAM with Feed-Forward Initialization and Pose-Conditioned Mapping
- 作者：Jaafar Mahmoud, Arthur Movsesyan, Mikhail Iumanov, Sergey Kolyubin
- 出版日期：2026-09-23T11:21:38Z
- 分类：Embodied / Robotics / AR Applications（主）；3D Reconstruction & Multi-view Geometry（次）
- 链接：摘要页 https://arxiv.org/abs/2609.27702 ；PDF https://arxiv.org/pdf/2609.27702

### 一句话总结
DAVIO 利用单一多视角深度模型 Depth Anything 3，同时承担单目惯性 SLAM 的启动初始化与建图，实现具备真实尺度与重力约束的实时稠密 SLAM。

### 研究问题
仅用相机与 IMU 进行度量尺度定位与稠密建图时，传统视觉-惯性滤波器必须等待足够的视差才能启动，并且只能保留稀疏路标；而前馈几何模型虽然能从少量图像预测稠密结构，却无法提供度量尺度与重力方向。论文试图融合两类方法的优势，解决启动慢、定位误差与建图稠密度/精度之间的矛盾。

### 核心思路/方法
- 使用单一多视角深度模型 Depth Anything 3 同时服务于启动阶段与建图阶段。
- 启动阶段：由五张图像窗口与预积分 IMU 测量构成一个无特征（feature-free）线性系统，通过带鲁棒性与条件数检查的求解，经缓冲重放（buffered replay）引导 VIO 滤波器完成初始化。
- 跟踪阶段：用滤波器的度量位姿对深度模型进行条件化（conditioning）。
- 残差尺度仅沿视线方向进行校正，以保持度量相机基线不变。
- 使用保持重力的子图（gravity-preserving submap graph）并结合带漂移门控的重访机制对地图进行精化。
- 论文声明发布 DAVIO 代码，定位为实时稠密度量 SLAM 系统。

### 主要贡献
- 提出用单一前馈多视角深度模型同时完成启动初始化与稠密建图的 SLAM 框架。
- 设计无特征、带条件数检查的线性启动方案，借助 IMU 预积分实现更早启动并获得度量尺度与重力信息。
- 提出位姿条件化建图与仅沿视线方向的尺度校正策略，在保持相机基线的同时修正残差尺度。
- 引入保持重力的子图图结构与漂移门控重访进行地图精化。
- 在 EuRoC 上相较 SOTA 前馈建图方法启动更早、定位误差更低、建图更准确（在相同位姿条件下）；在建筑尺度的 ORI 序列上，在相同里程计下达到或优于 SOTA 建图方法，且在将 GT 位姿替换为真实里程计时性能下降更小。
- 向社区开源代码。

### 局限性
- 具体运行时间、帧率、内存占用等实时性指标：摘要未提供足够信息。
- 除 EuRoC 与 ORI 之外的数据集或场景泛化能力：摘要未提供足够信息。
- 深度模型预测偏差对系统的影响分析：摘要未提供足够信息。
- 与更多类型基线（如非前馈方法、其他 VIO/SLAM 系统）的定量对比细节：摘要未提供足够信息。
- 消融实验与各模块贡献的定量结果：摘要未提供足够信息。

### 阅读优先级
中。理由：该工作面向单目+IMU 的稠密度量 SLAM，将前馈深度模型与 VIO 滤波器结合，选题在机器人与 AR 应用方向具有明确价值，且涉及启动初始化、尺度校正与建图精化等实际工程问题。但由于仅提供摘要，无法判断实验规模、实时性指标与开源代码质量，是否值得精读取决于读者对单目惯性稠密 SLAM 或前馈几何先验融合方向的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

A camera and an IMU are the minimal sensor setup for metric localization and dense mapping, yet classical visual--inertial filters must wait for parallax before they start and then retain only sparse landmarks. Feed-forward geometry models, in contrast, predict dense structure from a few images but provide neither metric scale nor gravity. We present DAVIO, which uses a single multi-view depth model, Depth Anything~3, for both start-up and mapping. At start-up, a five-image window and preintegrated IMU measurements form a feature-free linear system. Its robust, conditioning-checked solution bootstraps a VIO filter through buffered replay. During tracking, the filter's metric poses condition the depth model. Residual scale is corrected only along viewing rays, which preserves the metric camera baselines, and a gravity-preserving submap graph with drift-gated revisits refines the map. On EuRoC, DAVIO starts markedly earlier, reduces the localization error, and maps more accurately than SOTA feed-forward mappers given identical poses. On building-scale ORI sequences, DAVIO is on bar or better than SOTA mappers on the same odometry, and degrades far less when GT poses are replaced by real odometry. We release the code of DAVIO, a real-time dense metric SLAM system, to the community.

</details>

#### 2026-09-23 - Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization

**Authors:** Byeonggyu Park, Mingu Jeon, Seong-Woo Kim
**Links:** [abs](https://arxiv.org/abs/2609.27346) - [pdf](https://arxiv.org/pdf/2609.27346)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization
- 作者：Byeonggyu Park, Mingu Jeon, Seong-Woo Kim
- 出版日期：2026-09-23T04:33:01Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.27346 ；PDF: https://arxiv.org/pdf/2609.27346

### 一句话总结
该论文提出一个反射感知框架，用于在自车运动条件下融合前视相机图像与 2D 雷达点云，通过推断反射阶数和反射面分布并借助物理引导射线追踪重建反射路径，从而定位处于非视距（NLOS）状态的行人。

### 研究问题
如何在外来自车动态的户外场景中，可靠地定位非视距（NLOS）行人。摘要指出，这一问题对城市自动驾驶安全至关重要，但在自车运动环境下极具挑战，因为自车运动会使雷达多径传播变得复杂且噪声严重。

### 核心思路/方法
- 面向户外测试场场景中移动自车的 NLOS 行人定位，提出反射感知框架。
- 融合前视相机图像和 2D 雷达点云。
- 在鸟瞰图（bird’s-eye-view）空间中推断反射阶数和反射面分布。
- 使用物理引导的射线追踪重建失真的反射路径，并据此定位被遮挡行人。
- 在自车动态条件下的户外测试场场景中进行验证。

### 主要贡献
- 提出一个面向移动自车 NLOS 行人定位的反射感知框架。
- 将前视相机图像与 2D 雷达点云融合，并在鸟瞰图空间推断反射阶数和反射面分布。
- 引入物理引导射线追踪以重建失真反射路径并定位隐藏行人。
- 在户外测试场场景中、自车动态条件下验证框架有效性。摘要声称结果证明了该框架在移动自车 NLOS 行人定位中的有效性。

### 局限性
- 摘要未提供足够信息说明具体实验规模、数据集组成、评价指标和定量结果。
- 摘要未提供足够信息说明框架在不同场景、天气、光照、交通密度或传感器配置下的泛化能力。
- 摘要未提供足够信息说明失败案例、计算开销、实时性、对雷达噪声或多径复杂度的鲁棒性边界。
- 摘要未提供足够信息说明与已有方法的对比情况。
- 摘要未提供足够信息说明“户外测试场场景”的具体范围及其对真实城市开放道路的代表性。

### 阅读优先级
中。理由：该论文关注自动驾驶中 NLOS 行人定位这一安全相关且具有挑战性的问题，方法上结合多模态感知、鸟瞰图推理和物理引导射线追踪，具有一定技术针对性；但根据摘要，验证局限于户外测试场场景，且摘要未给出定量结果、对比和泛化性信息。因此对 NLOS 感知、雷达多径利用或自动驾驶行人安全方向的研究者优先级较高，对一般读者则为中等。

</details>

<details>
<summary>Abstract</summary>

Reliable localization of non-line-of-sight (NLOS) pedestrians is critical for safe urban autonomous driving, yet it remains highly challenging in ego-dynamic outdoor environments, where ego-vehicle motion makes radar multipath propagation complex and noisy. In this paper, we present a reflection-aware framework for NLOS pedestrian localization with a moving ego-vehicle in outdoor testbed scenarios. Our framework fuses front-view camera images and 2D radar point clouds to infer reflection orders and reflective surface distributions in bird's-eye-view space. It then uses physics-guided ray tracing to reconstruct distorted reflection paths and localize the hidden pedestrian. We validate the framework in outdoor testbed scenarios under ego-dynamic conditions. The results demonstrate the effectiveness of the proposed framework for NLOS pedestrian localization with a moving ego-vehicle.

</details>

#### 2026-09-23 - BladeMaster: Real-Time Robotic Cutting Simulation with Online-Generated Persistent Discontinuities

**Authors:** Zhanyu Yang, Yunuo Chen, Yanjia Huang, Joseph Masterjohn, Yin Yang, Chenfanfu Jiang
**Links:** [abs](https://arxiv.org/abs/2609.27342) - [pdf](https://arxiv.org/pdf/2609.27342)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BladeMaster: Real-Time Robotic Cutting Simulation with Online-Generated Persistent Discontinuities
- 作者：Zhanyu Yang, Yunuo Chen, Yanjia Huang, Joseph Masterjohn, Yin Yang, Chenfanfu Jiang
- 出版日期：2026-09-23T04:29:39Z
- 分类：Embodied / Robotics / AR Applications（二级分类：未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.27342) / [PDF](https://arxiv.org/pdf/2609.27342)

### 一句话总结
BladeMaster 是一个基于全拉格朗日物质点法（TLMPM）的 GPU 加速切割仿真框架，通过在物质点上在线生成持久侧标签来编码切割历史，从而在无需预设切割面或复制粒子的情况下实现实时机器人切割仿真。

### 研究问题
可变形物体的切割会同时改变其形状与拓扑结构，这给机器人操作中的精确仿真带来挑战。仿真器需要：
- 在切割发展过程中跟踪切割工具；
- 在工具撤出后保留产生的间断（不连续性）；
- 使新暴露的表面能够与工具以及彼此之间发生交互。

而现有方法通常预先指定切割面，或将材料分离与辅助几何场耦合，难以满足上述需求。

### 核心思路/方法
- 基于**全拉格朗日物质点法（TLMPM）**，并利用 **GPU 加速**。
- 核心思想：将切割历史**直接编码在物质点上**，通过由刀片几何形状**在线生成**的持久侧标签（persistent side labels）实现。
- 这些标签控制**粒子-网格耦合**：在完整材料内部保持连通性，同时在工具撤出后阻止切割面之间的虚假耦合。
- 该形式支持**渐进切割与相交切割**，无需预定义切割面，也无需复制粒子。
- 通过**材料-材料接触**，切割面可以重新接触并相互滑动而不会重新连接。
- 通过**工具-材料双向耦合**，材料反作用力能够影响工具运动。

### 主要贡献
- 提出 BladeMaster，一个基于 TLMPM 的 GPU 加速切割框架。
- 通过在线生成的持久侧标签将切割历史编码于物质点，控制粒子-网格耦合以保留切割间断。
- 支持渐进切割与相交切割，无需预设切割面或粒子复制。
- 支持切割面重新接触与滑动而不重新连接，并支持工具与材料的双向耦合。
- 实验展示了工具驱动切割后的操作，并在代表性任务上实现**快于实时**的性能。

### 局限性
- 摘要未提供足够信息（未说明方法的适用边界、失败情形、精度与稳定性限制、对比基线的具体范围等）。
- 摘要未提供足够信息（未给出实验任务的具体类型、规模、硬件配置及性能指标的量化细节）。
- 摘要未提供足够信息（未说明该方法对特定材料模型、本构或参数选择的依赖与敏感性）。

### 阅读优先级
**高**。理由：该工作直面机器人切割仿真中拓扑变化、间断保留与实时性等核心难题，提出的在线生成持久标签思路具有方法层面的新颖性，且声称达到快于实时的性能，对机器人操作与可变形体仿真方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Cutting changes both the shape and topology of deformable objects, making accurate simulation challenging for robotic manipulation. A simulator must track the cutting tool as a cut develops, preserve the resulting discontinuities after tool withdrawal, and enable newly exposed surfaces to interact with the tool and with each other. Existing formulations often prescribe cut surfaces in advance or couple material separation to auxiliary geometric fields. We introduce BladeMaster, a GPU-accelerated cutting framework based on the total Lagrangian material point method (TLMPM). Our key idea is to encode the cutting history directly on material points through persistent side labels generated online from the blade geometry. These labels govern particle-grid coupling, preserving connectivity within intact material while preventing spurious coupling across cut faces after tool withdrawal. Our formulation supports progressive and intersecting cuts without predefined cut surfaces or particle duplication. Material-material contact enables cut surfaces to recontact and slide against each other without reconnecting, while two-way tool-material coupling allows material reaction forces to influence tool motion. Experiments demonstrate tool-driven cutting followed by manipulation, with faster-than-real-time performance on representative tasks.

</details>

#### 2026-09-23 - Spatial and Semantic Reasoning for LLM-Driven Robot Navigation via MCP

**Authors:** Jungsoo Lee, Jaegyun Park, Wansoo Kim
**Links:** [abs](https://arxiv.org/abs/2609.27340) - [pdf](https://arxiv.org/pdf/2609.27340)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatial and Semantic Reasoning for LLM-Driven Robot Navigation via MCP
- 作者：Jungsoo Lee, Jaegyun Park, Wansoo Kim
- 出版日期：2026-09-23T04:29:01Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.27340 ；PDF https://arxiv.org/pdf/2609.27340

### 一句话总结
该论文提出一种非侵入式框架，通过面向导航的表示层并经 MCP 标准化工具，将 LLM 推理与 ROS 导航连接起来，使 LLM 能够利用度量/位姿感知图像与语义路点标注完成地图构建及空间、语义导航目标选择。

### 研究问题
论文指出现有 LLM 与 ROS 导航集成存在两个缺口：一是占据栅格等导航数据为原始几何消息，LLM 难以直接将其用作空间或语义上下文；二是添加 LLM 驱动能力通常需要自定义封装或机器人专用接口，限制了跨系统复用。

### 核心思路/方法
提出一个非侵入式框架，连接 LLM 推理与基于 ROS 的导航。框架包含面向导航的表示层，并通过 Model Context Protocol（MCP）暴露为标准化、可复用工具，使任何 MCP 兼容的 LLM 无需机器人专用封装即可访问。具体模块包括：视觉地图模块将占据栅格转换为度量、位姿感知图像以供目标推理；语义标注模块记录带有机器人位姿的路点级观测。评估任务为自主建图、基于空间推理的导航、基于语义推理的导航。

### 主要贡献
- 提出一种非侵入式框架，在不修改现有 ROS 导航栈的情况下，将 LLM 推理与 ROS 导航连接。
- 设计导航导向表示层：视觉地图模块把占据栅格转为度量、位姿感知图像；语义标注模块记录带位姿的路点级观测。
- 通过 MCP 将上述能力暴露为标准化、可复用工具，使任意 MCP 兼容 LLM 无需机器人专用封装即可使用。
- 在模拟室内环境中评估三类任务，报告所评估的 LLM 后端利用这些表示达到超过 97% 的地图覆盖率，并能根据自然语言指令选择空间或语义导航目标。

### 局限性
摘要未提供足够信息。摘要未说明模拟环境的规模与多样性、所评估的具体 LLM 后端、与基线方法的对比、失败案例、真实机器人验证情况，以及 MCP 工具在跨系统复用方面的实际测试范围。

### 阅读优先级
中。理由：该工作聚焦 LLM 与 ROS 导航集成中的表示与接口复用问题，提出 MCP 标准化工具与非侵入式框架，并报告了超过 97% 地图覆盖率及空间/语义目标选择结果；但摘要仅给出模拟室内环境下的有限任务评估，未提供与基线的对比细节、真实机器人验证和跨系统复用测试信息。对关注 LLM 机器人导航、ROS 集成或 MCP 工具化的读者具有参考价值，但若需判断其泛化性与实际部署效果，摘要信息尚不充分。

</details>

<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used as natural-language interfaces for robotic systems, yet their integration with Robot Operating System (ROS)-based navigation remains limited by two gaps. First, navigation data such as occupancy grids are represented as raw geometric messages that are difficult for LLMs to use directly as spatial or semantic context. Second, adding LLM-driven capabilities often requires custom wrappers or robot-specific interfaces, limiting reuse across systems. To address these challenges, we propose a non-invasive framework that connects LLM reasoning with ROS-based navigation through a navigation-oriented representation layer, exposed through the Model Context Protocol (MCP) as standardized, reusable tools so that any MCP-compatible LLM can access them without robot-specific wrappers. The visual map modules transform occupancy grids into metric, pose-aware images for goal reasoning, while the semantic annotation modules record waypoint-level observations with robot poses. We evaluate the framework on three tasks: autonomous mapping, spatial reasoning-based navigation, and semantic reasoning-based navigation. The results show that the evaluated LLM backends use these representations to achieve over 97% map coverage and select spatial or semantic navigation targets from natural-language instructions in a simulated indoor environment. This demonstrates representation-mediated LLM navigation without modifying the existing ROS navigation stack.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
