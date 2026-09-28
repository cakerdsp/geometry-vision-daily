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

**Last updated:** 2026-09-25T13:08:13-04:00
**Total number of papers:** 52
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

### 2026-09

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

#### 2026-09-21 - SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation

**Authors:** Jiangshan Gong, Yuqun Wu, Qiqian Fu, Yao Xiao, Chuhang Zou, Shenlong Wang, Derek Hoiem
**Links:** [abs](https://arxiv.org/abs/2609.25490) - [pdf](https://arxiv.org/pdf/2609.25490)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, 3D reconstruction, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation
- 作者：Jiangshan Gong, Yuqun Wu, Qiqian Fu, Yao Xiao, Chuhang Zou, Shenlong Wang, Derek Hoiem
- 出版日期：2026-09-21T23:39:19Z
- 分类：主分类 Geometry Foundation Models；副分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2609.25490 ；PDF https://arxiv.org/pdf/2609.25490

### 一句话总结
SAM-V 将前馈几何模型 VGGT 的特征直接融入 2D 分割基础模型 SAM，端到端训练实现单次前向传播的多视角一致实例分割，无需离线掩码匹配或显式 3D 重建。

### 研究问题
多视角物体分割在剧烈视角变化与遮挡下仍具挑战。现有做法主要有两条路线：一是直接在点云上做 3D 实例分割，但受限于稀缺的 3D 标注；二是依赖离线的 2D 掩码匹配流程，但跨帧存在物体身份歧义问题。论文关注的核心问题是：如何联合利用强 2D 先验与强 3D 先验，避免后处理匹配带来的身份不一致。

### 核心思路/方法
- 不以事后匹配的方式结合 2D 与 3D 先验，而是将前馈几何模型（VGGT）的特征直接集成进 2D 分割基础模型（SAM），针对跨视角实例预测进行端到端训练。
- 提出提示融合机制（prompt-fusion）：用视角相关的相机 token 与局部 VGGT 特征增强稀疏的 SAM 提示 token，使提示表示既具备视角感知能力，又具备空间接地能力。
- 配套设计掩码解码器（mask decoder），同时关注稠密的 2D 与 3D 特征。
- 通过将掩码解码直接条件化于多视角几何，在单次前向传播中即可对被提示物体产生一致的多视角分割，无需离线掩码匹配或显式 3D 重建。

### 主要贡献
- 提出 SAM-V，将几何基础模型特征与 2D 分割基础模型端到端融合，用于多视角实例分割。
- 提出提示融合机制，使 SAM 的稀疏提示 token 同时具备视角感知与空间接地特性。
- 设计可同时关注稠密 2D 与 3D 特征的掩码解码器，直接以多视角几何为条件生成一致的跨视角分割。
- 在 IGGT 3D 跟踪基准上，于 ScanNet++ 划分中相比最先进的多视角实例分割基线，整体 IoU 提升 5 点、帧级召回提升 12 点；并在零样本 ScanNet 划分的所有指标上领先。
- 代码与预训练模型已公开。

### 局限性
摘要未提供足够信息（未提及失败情形、计算开销、对 VGGT 或 SAM 的依赖风险、标注需求或泛化边界等具体限制）。

### 阅读优先级
中。理由：该工作面向多视角一致实例分割，思路（将几何基础模型特征注入 2D 分割基础模型、避免离线匹配与显式重建）与几何基础模型方向直接相关，且报告了较明显的基准提升并开源代码；但摘要未给出方法细节与局限性的充分信息。是否优先精读，取决于读者对多视角分割、3D 跟踪或几何与 2D 基础模型融合的具体兴趣，摘要未提供额外兴趣方向。

</details>

<details>
<summary>Abstract</summary>

Consistent multi-view object segmentation is critical for 3D perception and robotics, yet remains challenging under severe viewpoint and occlusion changes. Existing methods typically perform 3D instance segmentation on point clouds or rely on offline 2D mask-matching pipelines. However, 3D instance segmentation is limited by scarce 3D annotations, while offline 2D matching suffers from object identity ambiguity across frames. To leverage strong 2D and 3D priors jointly, we propose SAM-V (Geometry-Aware Segment Anything for Multi-View Instance Segmentation). Instead of combining the two priors through post-hoc matching, SAM-V directly integrates features from a feed-forward geometry model (VGGT) into a 2D segmentation foundation model (SAM), trained end-to-end for cross-view instance prediction. SAM-V introduces a prompt-fusion mechanism that enriches sparse SAM prompt tokens with view-specific camera tokens and local VGGT features, making the prompt representation both view-aware and spatially grounded, together with a mask decoder that attends to dense 2D and 3D features. By conditioning the mask decoding directly on multi-view geometry, SAM-V produces consistent multi-view segmentation of a prompted object in a single forward pass without offline mask matching or explicit 3D reconstruction. On the IGGT 3D tracking benchmark, where consistent instance identity across frames directly determines performance, SAM-V improves overall IoU by 5 points and frame-level recall by 12 points on the ScanNet++ split over the state-of-the-art multi-view instance segmentation baseline and leads on all metrics in the zero-shot ScanNet split. Our code and pretrained models are available at https://github.com/gong208/SAM-V.git.

</details>

## Dynamic / 4D Reconstruction

### 2026-09

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

#### 2026-09-22 - GTR: Gated Token Recurrence for Efficient Dense Prediction

**Authors:** Zhe Feng, Longfei Liu, Wei Liu, Kai Chen, Jiangang Kong, Wei Zhou, Yifeng Qian, Dexiong Chen, Xuanlong Yu, Xi Shen
**Links:** [abs](https://arxiv.org/abs/2609.26590) - [pdf](https://arxiv.org/pdf/2609.26590)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GTR: Gated Token Recurrence for Efficient Dense Prediction
- 作者：Zhe Feng, Longfei Liu, Wei Liu, Kai Chen, Jiangang Kong, Wei Zhou, Yifeng Qian, Dexiong Chen, Xuanlong Yu, Xi Shen
- 出版日期：2026-09-22T15:34:20Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2609.26590) / [PDF](https://arxiv.org/pdf/2609.26590)

### 一句话总结
论文提出 GTR——一种无需 softmax、基于门控线性注意力与交替空间扫描方向的循环视觉骨干，用于在高分辨率密集预测中替代全局 softmax 注意力，并报告了在 COCO 检测与多任务迁移上的精度及延迟结果。

### 研究问题
基于自注意力的视觉骨干在密集预测任务上表现良好，但全局 softmax 注意力的二次计算成本随图像分辨率增大而限制其效率。论文关注的问题是：能否用循环式的 token 混合机制，作为全局 softmax 注意力的高效替代方案，服务于高分辨率密集预测与边缘部署。

### 核心思路/方法
- 提出 Gated Token Recurrence（GTR），一种 softmax-free 的循环视觉骨干。
- 方法组合了三个要素：门控线性注意力、交替空间扫描方向、以及空间增强的 SwiGLU 模块。
- 训练上采用蒸馏策略：从一个面向检测专门化的 DINOv3 教师模型中蒸馏，仅使用最终层 patch-token 对齐，通过线性投影和平方 ℓ2 损失实现；不使用 masked-token prediction，也不使用中间层监督。
- 使用 Objects365 检测器预训练。
- 实现层面提供了专门的 chunkwise CUDA 算子，并涉及编译 FP16 执行与 TensorRT 部署。

### 主要贡献
- 提出 GTR 这一无需 softmax 的循环视觉骨干，将门控线性注意力、交替空间扫描方向与空间增强 SwiGLU 结合，用于高效密集预测。
- 给出一种简化的蒸馏方案：仅依赖最终层 patch-token 对齐（线性投影 + 平方 ℓ2 损失），无需 masked-token prediction 与中间层监督。
- 在 Objects365 检测器预训练后，GTR-L 在 COCO val2017 上达到 58.9 box AP，并在 RTX 4090 编译 FP16 执行下报告 1.908 ms 的 batch-one 中位延迟。
- 同一骨干可迁移至实例分割、姿态估计、旋转检测、语义分割与单目深度估计。
- 在 RTX 4090、1.6K tokens 的孤立 kernel 基准中，专用 chunkwise CUDA 算子比 FLA v0.5.0 快 4.0 倍。
- 在 DRIVE AGX Thor 上的 TensorRT 部署中，所评估模型达到 2.282–8.769 ms 的 batch-one 中位延迟。

### 局限性
- 摘要未提供足够信息说明各迁移任务的具体精度表现、对比基线设置、数据集规模与训练细节。
- 摘要未提供足够信息说明 GTR 在不同分辨率、不同硬件或不同 token 长度下的完整效率曲线与 scaling 行为。
- 摘要未提供足够信息说明蒸馏方案与 masked-token prediction 或中间层监督方案的消融对比。
- 摘要未提供足够信息说明方法在非检测类密集预测任务上是否同样需要 Objects365 检测器预训练。
- 摘要未提供足够信息说明与全局 softmax 注意力骨干在同等精度下的系统性效率对比。
- 主分类标注为 3D Reconstruction & Multi-view Geometry，但摘要未提供足够信息说明该工作与三维重建或多视图几何的直接关联。

### 阅读优先级
中。理由：论文主题（高效密集预测骨干、softmax-free 循环 token 混合、边缘部署延迟）具有明确的工程与应用价值，且摘要给出了具体 AP 与延迟数字，便于快速判断相关性；但摘要未涉及具体任务精度细节、消融与完整实验设置，若关注三维重建或多视图几何方向，则需进一步确认其相关性。

</details>

<details>
<summary>Abstract</summary>

Self-attention-based vision backbones perform well on dense prediction, but the quadratic computational cost of global softmax attention limits their efficiency as image resolution increases. We introduce Gated Token Recurrence (GTR), a softmax-free recurrent vision backbone that combines gated linear attention, alternating spatial scan directions, and spatially enhanced SwiGLU blocks. GTR is distilled from a detection-specialized DINOv3 teacher using only final-layer patch-token alignment through a linear projection and squared $\ell_2$ loss, without masked-token prediction or intermediate-layer supervision. With Objects365 detector pre-training, GTR-L achieves 58.9 box AP on COCO \texttt{val2017} with 1.908\,ms median batch-one latency under compiled FP16 execution on an RTX~4090. The same backbone also transfers to instance segmentation, pose estimation, oriented detection, semantic segmentation, and monocular depth estimation. In an isolated kernel benchmark, our specialized chunkwise CUDA operator is $4.0\times$ faster than FLA v0.5.0 at 1.6K tokens on RTX~4090. TensorRT deployment on DRIVE AGX Thor achieves 2.282--8.769\,ms median batch-one latency across the evaluated models. These results show that recurrent token mixing can provide an efficient alternative to global softmax attention for high-resolution dense prediction and edge deployment. Project page: https://intellindust-ai-lab.github.io/projects/GTR/

</details>

#### 2026-09-22 - Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation

**Authors:** John Church, Vazghen Nikolian
**Links:** [abs](https://arxiv.org/abs/2609.26561) - [pdf](https://arxiv.org/pdf/2609.26561)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation
- 作者：John Church, Vazghen Nikolian
- 出版日期：2026-09-22T15:13:44Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2609.26561 ；PDF https://arxiv.org/pdf/2609.26561

### 一句话总结
该工作用大规模自监督 ViT 基础模型（DINOv3）替换此前较小的卷积/ViT 编码器，在仅用合成数据训练的条件下提升了已知非合作航天器的单目位姿估计精度，并给出面向嵌入式推理的实测结果。

### 研究问题
如何在已知、非合作航天器的单目位姿估计任务中，进一步提升旋转误差精度，同时保持仅使用合成数据训练，并验证大模型在具备在轨飞行历史的处理器族上的嵌入式推理可行性。

### 核心思路/方法
- 沿用此前已建立的基于热力图的位姿估计架构。
- 将此前工作中较小的卷积编码器和 ViT 编码器替换为大型自监督 ViT 基础模型 DINOv3，并进行适配。
- 模型规模从 300M 扩展到 840M 参数，且作者称尚未观察到饱和。
- 最佳模型配置：以 LoRA 适配的 DINOv3 840M 作为编码器（rank 64），采用三随机种子集成与四旋转测试时增强。
- 在 Jetson Orin NX 16GB 上评估 840M 模型，测量单次网络前向推理时间与整板功耗。

### 主要贡献
- 报告了作者所知在 SPEED+ lightbox 和 sunlamp 测试集上、针对已知非合作航天器的最低平均旋转误差。
- 显示从 300M 到 840M 参数扩展带来位姿估计精度提升，且尚未观察到饱和。
- 给出嵌入式推理实测：840M 模型在 Jetson Orin NX 16GB 上单次裁剪推理 133.8 ms，整板功耗 32.0 W，表明在具有在轨飞行历史的处理器族上具备嵌入式推理可行性。
- 仅用合成数据训练，在 lightbox 与 sunlamp 两个域上均优于此前模型。
- 具体结果：最佳模型在 sunlamp 上平均旋转误差 1.56°，在 lightbox 上 1.17°；对比此前已知最佳 EagerNet 的 2.66° 与 1.75°。

### 局限性
- 摘要未提供足够信息说明合成训练数据的具体来源、规模与生成方式。
- 摘要未提供足够信息说明模型在真实在轨数据或其他非 SPEED+ 数据集上的泛化表现。
- 摘要未提供足够信息说明功耗与推理时间之外的其他嵌入式资源占用（如内存）细节。
- 摘要未提供足够信息说明消融实验、失败案例或位姿估计中的平移误差表现。
- 仅报告旋转误差指标，摘要未提供足够信息说明完整六自由度位姿的评估情况。

### 阅读优先级
高。理由：该论文直接针对航天器单目位姿估计这一明确任务，报告了在公开测试集上相对此前最佳结果的显著旋转误差改进，同时覆盖“基础模型适配”与“嵌入式推理可行性”两个关键维度，且仅用合成数据训练，对航天视觉与资源受限部署方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We present an improvement on previous spacecraft pose estimation architectures that results in the lowest published mean rotation errors we know of on the SPEED+ lightbox and sunlamp test sets for a known, non-cooperative spacecraft. By using a previously established heatmap-based pose estimation architecture and adapting a large self-supervised ViT foundation model (DINOv3) in place of the smaller convolutional and ViT encoders of previous work, we show that pose estimation accuracy improves from 300M to 840M parameters with no saturation yet observed. We also evaluate our 840M model on a Jetson Orin NX 16GB, measuring single-pass network inference at 133.8 ms per crop with a board draw of 32.0 W. These measurements demonstrate embedded inference feasibility on a processor family with orbital flight heritage. Our resulting model outperforms previous models across lightbox and sunlamp domains while training only on synthetic data. Our best model, using DINOv3 840M adapted with LoRA as the encoder (rank 64, three-seed ensemble with four-rotation test-time augmentation), results in $1.56^\circ$ mean rotation error on sunlamp and $1.17^\circ$ on lightbox, compared to the previous best mean rotation errors we know of on these test sets, $2.66^\circ$ and $1.75^\circ$ by EagerNet.

</details>

#### 2026-09-22 - ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards

**Authors:** Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci
**Links:** [abs](https://arxiv.org/abs/2609.26315) - [pdf](https://arxiv.org/pdf/2609.26315)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** SLAM, monocular depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards
- 作者：Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci
- 出版日期：2026-09-22T12:25:10Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.26315 ；PDF https://arxiv.org/pdf/2609.26315

### 一句话总结
ArborSplat 是一个面向果园场景的在线语义 3D Gaussian Splatting SLAM 系统，通过 LiDAR 里程计跟踪并在高斯地图上直接优化语义，以改善树干、棚架和果实等细小结构的语义建图效果。

### 研究问题
论文关注果园机器人建图需求：需要保留树干、棚架和果实等体积小但语义重要的结构。现有 3D Gaussian Splatting SLAM 虽然具有高光度保真度，但其优化仍以外观驱动为主；将图像语义迁移到 3D 点对细薄结构不可靠，因为这些结构的像素可能从背景表面获得深度。因此，问题在于如何在线构建兼具几何、外观与可靠语义的果园 3DGS 地图。

### 核心思路/方法
摘要给出的核心方法包括：
- 使用 LiDAR 里程计进行跟踪。
- 在高斯地图上直接优化语义。
- 使用类别特定的高度带约束，该高度带基于每个关键帧立体点云拟合出的地平面。
- 在线融合多视角证据为语义点云。
- 拒绝与局部地表面或单目深度不一致的标签。
- 采用类别约束细化，为代表性不足的结构保留高斯容量；在降低预算时，提高树木类别的训练视角准确率。

### 主要贡献
- 提出 ArborSplat，一个面向果园的在线语义 3DGS SLAM 系统，结合 LiDAR 里程计跟踪与高斯地图上的直接语义优化。
- 引入基于每个关键帧立体点云拟合地平面的类别特定高度带约束。
- 在线融合多视角语义证据为语义点云，并拒绝与局部地表面或单目深度不一致的标签。
- 通过类别约束细化为代表性不足结构保留高斯容量，并在降低预算下提升树木类别的训练视角准确率。
- 在苹果园和梨园的休眠期、开花期和采收期进行评估；完整路线上 12 次遍历的 ATE 均低于 0.5 m；在共享 301 帧片段上，相比 SGS-SLAM 和 GS3LAM 提升训练视角与留出集 mIoU，并运行更快；SemGauss-SLAM 在全部六个片段上出现 GPU 内存不足。

### 局限性
摘要未提供足够信息说明该方法的具体失败场景、适用范围限制、计算资源需求细节、对 LiDAR 或立体相机的依赖程度，以及在不同果园环境中的泛化边界。摘要仅提到 SemGauss-SLAM 在全部六个共享片段上 GPU 内存不足，但未说明 ArborSplat 自身是否存在类似内存或实时性限制。其他潜在局限摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对果园语义 SLAM 与 3DGS 结合中的细薄结构语义不可靠问题，提出在线语义优化、地平面高度带约束和多视角融合等具体机制，并包含跨物候期与多果园的定量比较；对农业机器人、语义建图和 3DGS SLAM 交叉方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Orchard robots need maps that preserve small but semantically important structures such as trunks, trellises, and fruit. 3D Gaussian Splatting (3DGS) SLAM achieves high photometric fidelity. However, its optimization remains appearance-driven, and transferring image semantics to 3D points is unreliable for thin structures, whose pixels may receive depth from background surfaces. We present ArborSplat, an online semantic 3DGS SLAM system that tracks with LiDAR odometry and optimizes semantics directly on the Gaussian map, constrained by class-specific height bands above a ground plane fitted to each keyframe's stereo point cloud, and fuses multi-view evidence into a semantic point cloud online while rejecting labels inconsistent with the local ground surface or with monocular depth. Class-constrained refinement reserves Gaussian capacity for underrepresented structures and, under reduced budgets, increases training-view accuracy on tree classes. We evaluate the approach on apple and pear orchards during dormancy, flowering, and harvesting. On full routes, it keeps ATE below 0.5 m on all 12 traversals. On shared 301-frame segments, it exceeds SGS-SLAM and GS3LAM by 0.23 to 0.50 training-view and 0.15 to 0.36 held-out mIoU while running 1.7 to 7.5 times faster, whereas SemGauss-SLAM runs out of GPU memory on all six.

</details>

#### 2026-09-22 - LiFR v2: Completion-Augmented Event Propagation for High-Rate Dense Prediction

**Authors:** Tao Wan, Xiaoshan Wu, Yifei Yu, Bo Wang, Xiaoyang Lyu, Muxin Liu, Aoxuan Pan, Zhongrui Wang, Xiaojuan Qi
**Links:** [abs](https://arxiv.org/abs/2609.25803) - [pdf](https://arxiv.org/pdf/2609.25803)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LiFR v2: Completion-Augmented Event Propagation for High-Rate Dense Prediction
- 作者：Tao Wan, Xiaoshan Wu, Yifei Yu, Bo Wang, Xiaoyang Lyu, Muxin Liu, Aoxuan Pan, Zhongrui Wang, Xiaojuan Qi
- 出版日期：2026-09-22T07:36:01Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类）；次要分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.25803 ；PDF https://arxiv.org/pdf/2609.25803

### 一句话总结
LiFR v2 提出了一个统一的“传播—补全—记忆”框架，从 RGB 关键帧与事件流进行因果式任意时刻与流式稠密预测，以缓解 RGB 低更新率与事件空间稀疏性带来的互补性利用不足问题。

### 研究问题
动态环境中的高帧率稠密感知受限于 RGB 相机的低更新率，因为帧间可能发生快速场景变化。事件相机提供时间上稠密但空间稀疏的测量，与空间稠密的 RGB 观测互补。然而，直接融合无法充分利用这种互补性；而事件引导的传播在无有效 RGB 支持的新出现区域或被遮挡后再出现（disocclusion）区域会失败。

### 核心思路/方法
论文提出的 LiFR v2 是一个统一的传播—补全—记忆框架，用于从一张 RGB 关键帧和事件流进行因果式任意时刻与流式稠密预测。具体包含两个模块：
- Event-Guided Completion Module (EGCM)：在传播不受支持的区域恢复任务相关表示。
- History Retrieval Module (HRM)：在连续查询之间复用已补全的表示。

该框架支持语义分割、单目深度估计与多任务稠密预测。论文还引入 SHF-Emerge 用于评估快速物体出现与去遮挡情况。

### 主要贡献
- 提出 LiFR v2，一个用于从 RGB 关键帧与事件进行因果式任意时刻及流式稠密预测的统一传播—补全—记忆框架。
- 引入 Event-Guided Completion Module (EGCM)，在传播不受支持处恢复任务相关表示。
- 引入 History Retrieval Module (HRM)，在连续查询间复用已补全表示。
- 框架支持语义分割、单目深度估计与多任务稠密预测。
- 提出 SHF-Emerge，用于评估快速物体出现与去遮挡。
- 在 DSEC 上达到 74.37% mIoU；在 SHF-Emerge 上达到 56.13% mIoU，相比 LiFR-Seg 提升 1.85 个百分点；在 SHF-Emerge 上将深度 RMSE 从传播基线的 1.564 m 降至 1.118 m。
- 分割与深度均超过 100 FPS，展示了超出 RGB 帧率的准确且高效的高帧率感知。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的具体失败情形、对特定数据集或硬件条件的依赖、计算资源需求、长期流式场景下的误差累积、事件噪声或传感器失配等潜在限制；也未提供 SHF-Emerge 的构建细节与统计特性。

### 阅读优先级
高。理由：该工作针对高帧率稠密感知中 RGB 低更新率与事件空间稀疏性的核心矛盾，提出明确的模块化解决方案，并在语义分割、单目深度估计与多任务稠密预测上报告了定量结果与超过 100 FPS 的效率指标；同时提出了新的评估设置 SHF-Emerge 以针对物体快速出现与去遮挡，这些内容对事件相机与稠密预测交叉方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

High-rate dense perception in dynamic environments is limited by the low update rate of RGB cameras, as rapid scene changes can occur between frames. Event cameras offer temporally dense but spatially sparse measurements, complementary to spatially dense RGB observations. Direct fusion cannot fully exploit this complementarity, while event-guided propagation fails on newly appearing or disoccluded regions without valid RGB support. We present LiFR v2, a unified propagation-completion-memory framework for causal anytime and streaming dense prediction from an RGB keyframe and events. LiFR v2 introduces an Event-Guided Completion Module (EGCM) to recover task-relevant representations where propagation is unsupported, and a History Retrieval Module (HRM) to reuse completed representations across successive queries. The framework supports semantic segmentation, monocular depth estimation, and multi-task dense prediction, and we further introduce SHF-Emerge to evaluate rapid object emergence and disocclusion. LiFR v2 achieves 74.37% mIoU on DSEC and 56.13% on SHF-Emerge, improving LiFR-Seg by 1.85 percentage points on the latter, while reducing SHF-Emerge depth RMSE from 1.564 m to 1.118 m over the propagation baseline. It also exceeds 100 FPS for both segmentation and depth, demonstrating accurate and efficient high-rate perception beyond RGB frame rates.

</details>

#### 2026-09-22 - Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning

**Authors:** Dingkang Yang, Yizhou Liu, Wendong Cheng, Zizhi Chen, Shunli Wang, Yang Liu, Hongsheng Li, Lihua Zhang
**Links:** [abs](https://arxiv.org/abs/2609.25741) - [pdf](https://arxiv.org/pdf/2609.25741)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, geometric reconstruction, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning
- 作者：Dingkang Yang, Yizhou Liu, Wendong Cheng, Zizhi Chen, Shunli Wang, Yang Liu, Hongsheng Li, Lihua Zhang
- 出版日期：2026-09-22T06:22:31Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.25741) | [PDF](https://arxiv.org/pdf/2609.25741)

### 一句话总结
提出统一的视觉-语言-几何框架 Fysiverse-3D-Vision，从单张图像出发进行生成式 3D 场景重建，并将其空间布局推理与资产生成分离，以支持可执行 3D 内容的生成。

### 研究问题
从单张图像生成可控且可执行的 3D 场景仍具挑战性。现有 3D 生成方法虽能合成视觉上合理的物体与场景，但其空间布局估计与特定资产生成器相耦合，难以联合建模物体语义、度量几何与场景级空间关系——而这些对于交互式编辑、物理仿真和具身应用至关重要。

### 核心思路/方法
- 构建统一的视觉-语言-几何框架，用于单张图像的生成式 3D 场景重建与可执行资产构建。
- 建立共享表示，使空间推理与几何重建相互增强，从而让物体布局推断摆脱单个资产生成器的约束。
- 在统一 Transformer 中整合文本监督、语义视觉线索与几何表示，以捕捉场景上下文、度量几何和物体级交互。
- 设计物体条件布局模块，在目标物体表示与全局几何特征之间执行交叉注意力，预测物体的平移、旋转与尺度。
- 采用渐进式训练：先学习几何-语言对齐，再在保持重建能力的前提下引入布局推理，最后通过碰撞感知优化提升物理一致性。
- 通过将空间布局推理与资产合成分离，提供可适配接口，用于交互式场景编辑、物体级操作和可执行 3D 内容生成。

### 主要贡献
- 提出 Fysiverse-3D-Vision 框架，从单张图像生成 3D 场景，并解耦空间布局推理与资产合成。
- 通过共享表示与统一 Transformer 联合建模语义、度量几何与场景级空间关系，使布局推断不再受限于特定资产生成器。
- 引入物体条件布局模块与交叉注意力机制，显式预测物体的平移、旋转和尺度。
- 设计渐进式训练策略与碰撞感知优化，以提升物理一致性并保留重建能力。
- 提供面向交互式编辑与可执行 3D 内容生成的适配接口。

### 局限性
摘要仅声称在几何一致性、布局估计、渲染质量和物理属性理解方面优于现有方法，未给出具体实验设置、数据集、评价指标、失败案例或计算成本等信息。因此这些方面的局限性“摘要未提供足够信息”。

### 阅读优先级
中。理由：该工作聚焦单图到可执行 3D 场景的生成与布局解耦，问题设定与接口设计对 3D 重建、场景生成和具身应用方向有参考价值；但摘要未提供定量结果、数据集和实现细节，是否值得深入精读需结合正文实验与代码/补充材料进一步判断。

</details>

<details>
<summary>Abstract</summary>

Generative models have advanced image-conditioned 3D content creation, yet generating controllable and executable 3D scenes from a single image remains challenging. Existing 3D generative approaches can synthesize visually plausible objects and scenes, but their spatial layout estimation is coupled with specific asset generators. They struggle to jointly model object semantics, metric geometry, and scene-level spatial relationships, which are essential for interactive editing, physical simulation, and embodied applications. We propose Fysiverse-3D-Vision, a unified vision-language-geometry framework for generative 3D scene reconstruction and executable asset construction from a single image. We establish a shared representation where spatial reasoning and geometric reconstruction mutually enhance each other, allowing object layouts to be inferred beyond the constraints of individual asset generators. Our model integrates textual supervision, semantic visual cues, and geometric representations within a unified Transformer to capture scene context, metric geometry, and object-level interactions. An object-conditioned layout module performs cross-attention between target object representations and global geometric features to predict object translation, rotation, and scale. Training progressively learns geometry-language alignment, introduces layout reasoning while preserving reconstruction capability, and refines physical consistency through collision-aware optimization. By separating spatial layout reasoning from asset synthesis, Fysiverse-3D-Vision provides an adaptable interface for interactive scene editing, object-level manipulations, and executable 3D content generation. Experiments demonstrate that our framework achieves superior geometric consistency, layout estimation, rendering quality, and physical property understanding compared with existing approaches.

</details>

#### 2026-09-22 - Point Diffusion Mamba: Unified Diffusion-State-Space Modeling for Single-View 3D Reconstruction under Data Scarcity

**Authors:** Wei Zhou, Xinzhe Shi, Xingxing Hao, Xing Hao, Kang Li, Jinye Peng, Ying He
**Links:** [abs](https://arxiv.org/abs/2609.25538) - [pdf](https://arxiv.org/pdf/2609.25538)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, point cloud reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Point Diffusion Mamba: Unified Diffusion-State-Space Modeling for Single-View 3D Reconstruction under Data Scarcity
- 作者：Wei Zhou, Xinzhe Shi, Xingxing Hao, Xing Hao, Kang Li, Jinye Peng, Ying He
- 出版日期：2026-09-22T01:11:24Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：abstract_url: https://arxiv.org/abs/2609.25538；pdf_url: https://arxiv.org/pdf/2609.25538；代码：https://github.com/NWUzhouwei/PDM

### 一句话总结
提出 Point Diffusion Mamba（PDM），将扩散模型的生成能力与状态空间模型的效率结合，用于数据稀缺条件下的单视图 3D 重建。

### 研究问题
单视图 3D 重建虽已有显著进展，但从本质上具有歧义的 2D 观测中推断复杂 3D 结构仍是根本性的不适定问题，在数据稀缺情形下尤为突出且研究不足。论文聚焦于数据稀缺条件下的单视图 3D 重建。

### 核心思路/方法
- 将扩散模型的生成能力与状态空间模型的效率相结合，形成面向数据稀缺单视图 3D 重建的方法 PDM。
- 采用轻量级重建模块处理无序点云输入。
- 结合 Local Geometric Aggregation 模块与 Mamba blocks，联合建模全局几何结构与局部细节。
- 针对 Mamba 模块提取的高层特征仅包含稀疏点的抽象语义信息、而重建中初始噪声输入的每个点都需要精确预测这一差距，引入 Hierarchical Feature Integration Network，将高层语义特征与局部几何特征逐点融合，以克服基于 token 的点云重建的局限。
- 提出 Dynamic Weighted Sampling 策略，利用生成先验自适应地统一 3D 生成与单视图重建，以提升重建质量。

### 主要贡献
- 提出 PDM，将扩散模型与状态空间模型统一用于数据稀缺条件下的单视图 3D 重建。
- 设计轻量级重建模块，并通过 Local Geometric Aggregation 与 Mamba blocks 联合建模全局几何结构和局部细节。
- 提出 Hierarchical Feature Integration Network，逐点融合高层语义与局部几何特征。
- 提出 Dynamic Weighted Sampling 策略，自适应统一 3D 生成与单视图重建。
- 在 ShapeNet 和 Pix3D 基准上实验，摘要称其优于现有最先进方法（具体指标与对比细节摘要未提供足够信息）。

### 局限性
- 摘要未提供足够信息说明方法的具体失败情形或适用边界。
- 摘要未提供足够信息说明数据稀缺的具体定义、数据规模范围及对数据稀缺程度的敏感性。
- 摘要未提供足够信息说明计算开销、推理速度或模型参数量等效率细节（虽提及状态空间模型的效率，但无定量说明）。
- 摘要未提供足够信息说明在 ShapeNet 和 Pix3D 上的具体评价指标、数值结果及消融实验细节。
- 摘要未提供足够信息说明 Dynamic Weighted Sampling 的具体实现方式与超参数敏感性。

### 阅读优先级
高。理由：该论文聚焦数据稀缺条件下的单视图 3D 重建这一研究不足且具有实际意义的问题，方法上融合扩散模型与状态空间模型（Mamba）并涉及点云重建、层次特征融合与动态加权采样等设计；同时提供公开代码，便于复现与进一步验证。但需注意，摘要未提供足够信息说明具体实验细节与定量结果，阅读全文时需重点核查实验设置与消融分析。

</details>

<details>
<summary>Abstract</summary>

While single-view 3D reconstruction has seen significant progress, extrapolating complex 3D structures from inherently ambiguous 2D observations remains fundamentally ill-posed, particularly in the critically underexplored data-scarce regime. To address this challenge, we propose Point Diffusion Mamba (PDM), a method that integrates the generative power of diffusion models with the efficiency of state-space model for single-view 3D reconstruction under data-scarce conditions. Specifically, PDM employs a lightweight reconstruction module tailored to handle unordered point-cloud inputs effectively. By combining a Local Geometric Aggregation module with Mamba blocks, our approach jointly models global geometric structures and local details. In 3D reconstruction, each point in the initial noisy input requires a precise prediction, yet the high-level features extracted by the Mamba module capture only abstract semantic information from sparse points. To bridge this gap, we introduce the Hierarchical Feature Integration Network, which fuses high-level semantic and local geometric features for each point, overcoming the limitations of token-based point-cloud reconstruction. Furthermore, we propose a Dynamic Weighted Sampling strategy that adaptively unifies 3D generation with single-view reconstruction by leveraging generative priors to enhance reconstruction quality. Experimental results on the ShapeNet and Pix3D benchmarks demonstrate that PDM outperforms state-of-the-art methods, providing an effective solution for 3D reconstruction under data-scarce settings. Code is available at: https://github.com/NWUzhouwei/PDM.

</details>

## Neural Scene Representations & Rendering

### 2026-09

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

#### 2026-09-22 - φ-RIE: From Photorealistic Reconstruction to Interactive Environments

**Authors:** Runyi Yang, Deheng Zhang, Xiaoye Wang, Kanzhi Wu, Lei Sun, Ajad Chhatkuli, Kunyu Peng, Luc Van Gool, Danda Pani Paudel
**Links:** [abs](https://arxiv.org/abs/2609.26795) - [pdf](https://arxiv.org/pdf/2609.26795)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：φ-RIE: From Photorealistic Reconstruction to Interactive Environments
- 作者：Runyi Yang, Deheng Zhang, Xiaoye Wang, Kanzhi Wu, Lei Sun, Ajad Chhatkuli, Kunyu Peng, Luc Van Gool, Danda Pani Paudel
- 出版日期：2026-09-22T17:59:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.26795) | [PDF](https://arxiv.org/pdf/2609.26795)

### 一句话总结
φ-RIE 是一个基于高斯表示的原生流水线，将 3DGS 重建场景中选定的物体转化为可移动的仿真资产，同时保留并补全其余重建内容，从而把照片级重建转变成可交互环境。

### 研究问题
3D Gaussian Splatting 虽能对捕获场景进行照片级重建，但其表示本身不支持物理交互。机器人仿真需要物体级别的变化，即物体能够独立移动、发生接触，并揭示此前被遮挡的周围环境。摘要指出该差距源于两点：物体外观可能与背景纠缠；隐藏的物体几何与被遮挡的背景内容可能未被观测到。

### 核心思路/方法
核心观察是：资产生成与源移除应当耦合，即同一个物体身份既定义可移动资产，也定义需要移除并补全的场景内容。φ-RIE 据此构建了一个 Gaussian-native 流水线：Scene Observation 为 Coupled Scene Construction 提供共享证据；后者创建已配准的资产，并生成补全后的背景高斯，用于 Interactive Environment 中由仿真器驱动的渲染。这种耦合在保持未编辑高斯不变的同时，对齐视觉状态与物理状态。

### 主要贡献
- 提出 φ-RIE，一个将选定物体转化为可移动仿真资产、同时保留其余重建内容的 Gaussian-native 流水线。
- 提出资产构建与源移除耦合的关键思路，由同一物体身份统一定义可移动资产及需移除和补全的场景内容。
- 通过 Scene Observation 与 Coupled Scene Construction 的共享证据，生成配准资产与补全背景高斯，支持交互环境中的仿真器驱动渲染。
- 在 50 个 ScanNet++ 场景上，基于证据的选择与配准重试在固定保留率下将 20 mm 的匹配 F1 从 0.336 提升至 0.383。
- 进一步的测试展示了资产可执行性、相较单一生成器基线的操作增益，以及转换的视觉代价。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败情形、适用场景边界、计算开销、对未观测区域补全质量的定量限制，也未给出关于泛化能力或依赖条件的明确局限陈述。

### 阅读优先级
中。理由：该工作面向 3DGS 与机器人仿真的交叉问题，提出从照片级重建到交互环境的转换框架，并给出 ScanNet++ 上的定量结果与额外测试，对神经场景表示、可交互场景构建和仿真资产生成方向有参考价值；但摘要未提供额外兴趣方向，且局限性与方法细节有限，是否高优先阅读取决于读者对 3DGS 物理交互与机器人仿真的具体需求。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) can reconstruct a captured scene photorealistically, but the resulting representation does not by itself support physical interaction. Robot simulation instead requires object-level change, \textit{i.e.}, objects must move independently, make contact, and reveal previously occluded surroundings. This gap arises because object appearance may remain entangled with the background, while hidden object geometry and occluded background content may be unobserved. To address this challenge, we present φ-RIE, a Gaussian-native pipeline that converts selected objects into movable simulator assets while preserving the remaining reconstruction. Our key observation is that asset construction and source removal should be coupled, \textit{i.e.}, one object identity should define the movable asset and the scene content to remove and complete. Accordingly, Scene Observation supplies shared evidence to Coupled Scene Construction, which creates registered assets and completed background Gaussians for simulator-driven rendering in an Interactive Environment. This coupling preserves unedited Gaussians while aligning visual and physical state. On 50 ScanNet++ scenes, evidence-based selection and registration retry increase matched F1 at 20\,mm from 0.336 to 0.383 at fixed retention. Further tests demonstrate asset executability, manipulation gains over a single-generator baseline, and the visual cost of conversion. Together, these results demonstrate that \name\ enables interactive scene conversion.

</details>

#### 2026-09-22 - Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models

**Authors:** Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan
**Links:** [abs](https://arxiv.org/abs/2609.26007) - [pdf](https://arxiv.org/pdf/2609.26007)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models
- 作者：Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan
- 出版日期：2026-09-22T11:08:50Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.26007) / [PDF](https://arxiv.org/pdf/2609.26007)

### 一句话总结
论文提出 Skytopia：一种仅依赖前向单目相机、基于动作条件潜在世界模型的无人机导航策略，其核心主张是策略从世界模型中需要的是“能产生预测的表示”而非预测本身，因此在部署时丢弃预测器以降低推理成本，并统一支持点目标、图像目标与无目标导航。

### 研究问题
单目无人机导航要求在未见环境中，仅凭单个前向相机的输入到达目标，但这类输入对深度与尺度提供的线索很少。世界模型通过建模“观测如何在动作下演化”来应对该问题，但摘要指出这类方法通常是为部署执行而设计的：预测在部署时产生，并在每个控制步被反馈进行动生成。论文质疑这一范式的必要性，并试图回答：策略究竟需要世界模型的预测，还是产生该预测所需的表示？

### 核心思路/方法
- **核心论点**：在飞行中，已执行的动作几乎解释了观测之间的全部变化，因此预测可归约为“在已知位移下对静态场景的重投影”，策略真正需要的是支撑该预测的表示，而非预测结果本身。
- **方法构成**：提出 Skytopia，一个建立在动作条件潜在世界模型之上的策略；同时提出用于训练该策略的 3D Gaussian Splatting 平台。
- **双目标训练**：前向目标从意图运动预测下一观测的表示；逆向目标从预测的转移中恢复该运动。
- **部署设计**：由于预测不会进入动作生成环节，预测器在部署时被丢弃，从而降低推理开销；同一个策略可服务点目标、图像目标和无目标三种导航设定。
- **验证方式（摘要层面）**：仿真实验中在三类设定下均优于所有基线，成功率分别为 57.8%、66.0%、49.0%；丢弃预测器可去除 59.4% 的推理成本；同一策略随后在未微调的情况下部署到实体无人机，并在室内、开阔室外和林地环境中到达目标。

### 主要贡献
- 提出对世界模型在策略中作用的新观点：策略需要的是“用于产生预测的表示”，而非部署时的预测输出。
- 构建 Skytopia 策略，结合动作条件潜在世界模型与 3D Gaussian Splatting 训练平台，采用前向-逆向双目标学习。
- 在部署阶段丢弃预测器，实现 59.4% 的推理成本削减，同时不将预测反馈至动作生成。
- 用同一个策略统一支持点目标、图像目标与无目标三种导航规范。
- 仿真结果显示在三种设定下均超越所有基线；并在实体无人机上零微调部署，覆盖室内、开阔室外与林地环境。

### 局限性
摘要未提供足够信息。摘要未给出基线方法的具体构成、实验环境数量与规模、失败案例、实体部署的定量指标、3D Gaussian Splatting 平台的具体假设与依赖，也未讨论策略在动态场景、极端光照或相机标定误差下的表现与限制。

### 阅读优先级
高。理由：论文提出的“丢弃预测器、仅保留表示”的论点直接挑战世界模型在具身控制中的常见部署范式，并给出仿真成功率与推理成本削减的量化结果，还宣称在实体无人机上零微调跨室内外与林地部署。主题同时落在神经场景表示与具身/机器人导航的交叉点，对单目无人机导航与世界模型效率研究方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular drone navigation requires reaching a goal in an unseen environment from a single forward-facing camera, which offers few cues for depth and scale. World models address this by modelling how observations evolve under actions, but they are built to be executed: the prediction is produced at deployment and fed back into action generation at every control step. We argue that what a policy needs from a world model is not the prediction but the representation required to produce it: in flight the executed action explains almost all of the change between observations, so prediction reduces to reprojecting a static scene under a known displacement. We therefore introduce skytopia, a policy built on an action-conditioned latent world model, and the 3D Gaussian Splatting platform on which it is trained. A forward objective predicts the representation of the next observation from the intended motion, and an inverse objective recovers that motion from the predicted transition. Because the prediction never reaches action generation, the predictor is discarded and one policy serves point-goal, image-goal, and goal-free navigation. Simulation experiments show that skytopia outperforms every baseline under all three specifications, attaining 57.8%, 66.0%, and 49.0% success rate, while discarding the predictor removes 59.4% of the inference cost. The same policy is subsequently deployed on a physical drone without fine-tuning and reaches goals in indoor, open outdoor, and woodland environments.

</details>

#### 2026-09-22 - GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration

**Authors:** Karim Slimani, Catherine Achard, Eric Marchand, Brahim Tamadazte
**Links:** [abs](https://arxiv.org/abs/2609.25966) - [pdf](https://arxiv.org/pdf/2609.25966)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dense correspondence, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration
- 作者：Karim Slimani, Catherine Achard, Eric Marchand, Brahim Tamadazte
- 出版日期：2026-09-22T10:22:32Z
- 分类：主分类为 Neural Scene Representations & Rendering；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.25966 ；PDF https://arxiv.org/pdf/2609.25966

### 一句话总结
GRIP 提出一种基于位姿条件的细化框架，通过高斯特征泼溅将学习到的三维点特征柔和渲染到图像网格，并与图像特征在像素对齐的 Transformer 中融合，以改善像素到点匹配和 2D 到 3D 配准。

### 研究问题
论文关注图像到点云配准中的像素到点匹配与 2D 到 3D 配准问题。摘要指出其核心挑战在于基于网格的图像描述子与无序点云描述子之间存在结构不匹配。GRIP 在给定初始粗略位姿估计的条件下，试图缓解这种跨模态结构差异，并进一步细化配准结果。

### 核心思路/方法
- 输入设定：给定初始粗略位姿估计。
- 跨模态桥接：通过高斯特征泼溅，将学习到的三维点特征柔和渲染到图像网格上，得到由点云派生的特征图。
- 特征融合：将渲染得到的点云派生特征图与图像特征通过像素对齐的 Transformer 进行融合，使视觉语义线索和几何线索在共享的二维表示中交互。
- 解码与传播：对细化后的特征进行解码，并传播到更细分辨率，用于密集对应估计和最终位姿细化。
- 输出目标：像素到点匹配以及最终的 2D 到 3D 配准位姿细化。

### 主要贡献
- 提出 GRIP，一个位姿条件下的细化框架，用于像素到点匹配和 2D 到 3D 配准。
- 使用高斯特征泼溅作为跨模态桥梁，将无序点云特征渲染到图像网格，以缓解图像网格描述子与无序点云描述子之间的结构不匹配。
- 通过像素对齐 Transformer 融合渲染的点云派生特征图与图像特征，在共享二维表示中实现视觉语义与几何线索的交互。
- 将细化特征解码并传播到更细分辨率，用于密集对应估计和最终位姿细化。
- 在 RGB-D Scenes V2 和 7 Scenes 上报告了 state-of-the-art 的 inlier ratio 和具有竞争力的 registration recall，并在更严格评估阈值下表现更强。

### 局限性
- 摘要未提供足够信息说明方法对初始粗略位姿估计质量的敏感程度或失败情形。
- 摘要未提供足够信息说明计算开销、实时性、内存占用或高斯泼溅与 Transformer 融合带来的复杂度。
- 摘要未提供足够信息说明在 RGB-D Scenes V2 和 7 Scenes 之外的泛化能力。
- 摘要未提供足够信息说明消融实验、各模块具体贡献或超参数影响。
- 摘要未提供足够信息说明是否依赖特定传感器、标定质量或训练数据规模。
- 摘要未提供足够信息说明与基线方法在具体指标数值上的差距。

### 阅读优先级
中。理由：该论文主题属于图像到点云配准与神经场景表示/渲染的交叉方向，核心方法将高斯特征泼溅用于跨模态特征对齐，并声称在 inlier ratio 和严格阈值下表现较强，对相关领域读者有参考价值。但摘要未提供具体实验数值、消融细节、计算成本或失败案例分析，且兴趣方向未额外指定，因此不适合无条件列为高优先级；若读者关注 2D-3D 配准、跨模态特征融合或高斯泼溅应用，可提升为高优先级。

</details>

<details>
<summary>Abstract</summary>

This paper introduces GRIP, a pose-conditioned refinement framework for pixel-to-point matching and 2D to 3D registration. Given an initial coarse pose estimate, GRIP addresses the structural mismatch between grid based image descriptors and unordered point cloud descriptors by softly rendering learned 3D point features onto the image grid through Gaussian feature splatting. The rendered point derived feature map is then fused with image features by a pixel aligned transformer, enabling visual semantic and geometric cues to interact in a shared 2D representation. The refined features are decoded and propagated to finer resolutions for dense correspondence estimation and final pose refinement. Experiments on RGB D Scenes V2 and 7 Scenes demonstrate state of the art inlier ratio and competitive registration recall, with stronger performance under stricter evaluation thresholds.

</details>

#### 2026-09-22 - NaCR: Visual Localization via NeRF-aided Camera Ray Regression

**Authors:** Yesheng Zhang, Xiang Dai, Xu Zhao, Chongyang Zhang
**Links:** [abs](https://arxiv.org/abs/2609.25907) - [pdf](https://arxiv.org/pdf/2609.25907)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** NeRF, novel view synthesis, view synthesis, rendering, radiance, mapping, localization, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NaCR: Visual Localization via NeRF-aided Camera Ray Regression
- 作者：Yesheng Zhang, Xiang Dai, Xu Zhao, Chongyang Zhang
- 出版日期：2026-09-22T09:13:21Z
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2609.25907 ；PDF https://arxiv.org/pdf/2609.25907

### 一句话总结
论文提出 NaCR，将 NeRF 与相机光线回归（CRR）在光线层级统一起来，通过增强 CRR 基线、利用预训练 NeRF 合成新视角数据、以及将渲染光度误差反传以优化预测光线，并用两阶段训练课程保证收敛，以提升视觉定位精度。

### 研究问题
视觉定位（Visual Localization, VL）是虚拟现实等视觉应用的基础技术。近年出现的“相机光线回归”（Camera Ray Regression, CRR）范式将 2D 图像块映射到 3D 相机光线，但其精度有限。论文要解决的问题是如何提升 CRR 的定位精度。

### 核心思路/方法
作者观察到一种互补的对偶关系：CRR 从图像块预测光线，而 NeRF 的新视角合成恰恰执行该映射的逆过程——通过可微的光线步进从相机光线渲染图像块。基于这一互补关系，论文提出 NaCR（NeRF-aided Camera Ray Regression），一个在光线层级无缝连接 NeRF 与 CRR 的统一框架，具体包含三部分：
1. 在 CRR 基线上引入三项简单而有效的增强；
2. 利用预训练 NeRF 合成新视角，为高效的图像块级消费定制增强训练数据；
3. 利用 NeRF 的可微性，构建闭环监督流程，将光度渲染误差反向传播以优化预测的相机光线。
此外，为在高度非凸的图像空间中保证稳定收敛，论文引入两阶段训练课程。

### 主要贡献
- 提出 NaCR，一个在光线层级统一 NeRF 与 CRR 的框架，利用二者的对偶互补关系提升视觉定位精度。
- 在 CRR 基线中加入三项简单有效的增强。
- 利用预训练 NeRF 合成面向图像块级消费的新视角数据以增强训练。
- 构建基于 NeRF 可微性的闭环监督流程，用光度渲染误差反传优化预测光线。
- 引入两阶段训练课程以保证在高非凸图像空间中的稳定收敛。
- 在室内与室外基准上进行大量实验，表明 NaCR 取得有竞争力的精度；消融研究验证了各组件的有效性。

### 局限性
摘要仅说明在室内外基准上取得“有竞争力的精度”，未给出具体精度数值、对比方法、实验设置与失败案例；三项 CRR 增强的具体内容、两阶段训练课程的细节、以及闭环监督的收敛性分析均未提供。摘要未提供足够信息说明方法的适用范围限制、对预训练 NeRF 质量的依赖程度以及在真实场景中的泛化表现。

### 阅读优先级
**中**。理由：论文主题属于神经场景表示与渲染、视觉定位的交叉方向，将 NeRF 的可微渲染用于监督相机光线回归的思路具有一定新颖性，且涉及 VR/机器人/AR 等应用场景，对该方向读者有参考价值。但摘要仅给出方法框架与结论性表述，缺少定量结果与实现细节，无法从摘要判断其相对现有方法的实际提升幅度，因此优先级定为中而非高；若读者专攻视觉定位或 NeRF 应用，可适当上调关注度。

</details>

<details>
<summary>Abstract</summary>

Visual localization (VL) is a fundamental technology for vision applications such as virtual reality. Recently, a novel VL paradigm, Camera Ray Regression (CRR), has emerged, which maps 2D image patches to 3D camera rays, but its accuracy is limited. To improve CRR accuracy, we notice a compelling duality: the inverse of this mapping is inherently performed by the novel view synthesis model, \ie, Neural Radiance Fields (NeRF). While NeRF renders image patches from camera rays via differentiable ray marching, CRR predicts the rays from image patches. Motivated by this complementary relationship, we propose NeRF-aided Camera Ray Regression (NaCR), a unified framework that seamlessly bridges NeRF and CRR at the ray level. First, NaCR incorporates three simple yet effective enhancements into the CRR baseline. Second, leveraging a pre-trained NeRF, NaCR augments the training data by synthesizing novel views tailored for efficient, patch-level consumption. Finally, exploiting the differentiability of NeRF, NaCR forms a closed-loop supervision pipeline where photometric rendering errors are back-propagated to optimize the predicted camera rays. To ensure stable convergence within the highly non-convex image space, we introduce a two-stage training curriculum. Extensive experiments across indoor and outdoor benchmarks demonstrate that NaCR achieves competitive accuracy. Comprehensive ablation studies validate the efficacy of each proposed component.

</details>

#### 2026-09-22 - Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking

**Authors:** Edward Beng Wai Tan, Siew-Kei Lam
**Links:** [abs](https://arxiv.org/abs/2609.25746) - [pdf](https://arxiv.org/pdf/2609.25746)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking
- 作者：Edward Beng Wai Tan, Siew-Kei Lam
- 出版日期：2026-09-22T06:35:43Z
- 分类：Neural Scene Representations & Rendering（主类）；3D Reconstruction & Multi-view Geometry（次类）
- 链接：摘要页 https://arxiv.org/abs/2609.25746 ；PDF https://arxiv.org/pdf/2609.25746

### 一句话总结
该论文提出双协方差参数化的 3D 高斯泼溅 SLAM，让渲染与配准分别使用不同的协方差，以缓解同一协方差在两类任务中的需求冲突，并提升实时跟踪鲁棒性。

### 研究问题
在基于 ICP 的 3D Gaussian Splatting SLAM 中，传入帧需要与地图高斯进行配准，而每个高斯的协方差同时被用于渲染和配准。摘要指出，这两种用途对协方差的要求相互冲突：建图器为最小化光度误差会将其压平贴向表面，而鲁棒配准通常更受益于测量不确定性。论文要解决的核心问题即是如何在同一高斯表达中消解这一冲突，从而兼顾渲染优化与鲁棒跟踪。

### 核心思路/方法
论文提出一种“双协方差”参数化：每个高斯保留单一均值，但持有两个协方差——一个是由建图器优化的渲染协方差，另一个是由 RGB-D 传感器噪声模型导出的跟踪协方差。此外，作者将跟踪协方差用作图像角点的高斯锚点，为深度几何较弱的方向提供约束。方法面向实时跟踪，摘要称其跟踪速度约为 60 FPS。

### 主要贡献
- 提出双协方差参数化，将渲染协方差与跟踪协方差解耦，使同一高斯可同时服务渲染优化与配准需求。
- 引入由 RGB-D 传感器噪声模型导出的跟踪协方差，用于配准而非渲染。
- 将跟踪协方差作为图像角点的高斯锚点，在深度几何较弱的方向上补充约束。
- 在 TUM RGB-D、ScanNet、Replica 以及两段由 RealSense D435i 在轮式和手持平台录制的户外序列上进行评估。
- 摘要报告了跨多个场景的鲁棒跟踪性能和降低的里程计漂移，并保持约 60 FPS 的跟踪速度。

### 局限性
- 摘要未提供足够信息说明双协方差相比单协方差在计算或内存上的额外开销。
- 摘要未提供足够信息说明具体指标数值、各数据集上的逐项结果或消融实验。
- 摘要未提供足够信息说明退化场景、动态场景或极端光照条件下的失败模式。
- 摘要未提供足够信息说明跟踪协方差所依赖的 RGB-D 噪声模型的具体形式与参数来源。
- 摘要未提供足够信息说明与现有 3DGS SLAM 方法的详细对比结论。
- 摘要未提供足够信息说明该方法的适用传感器范围是否仅限 RGB-D。

### 阅读优先级
中。理由：论文针对 3DGS SLAM 中渲染与配准共用协方差的明确冲突提出解耦方案，问题表述清晰，且报告了约 60 FPS 的实时性与跨多数据集评估，对关注 3DGS SLAM、实时跟踪和 RGB-D 里程计的研究者具有参考价值。但摘要未给出具体定量结果、对比方法和消融细节，是否真正带来显著且稳健的改进需进一步阅读正文验证，因此不直接列为高优先级。

</details>

<details>
<summary>Abstract</summary>

ICP-based 3D Gaussian Splatting (3DGS) SLAM tracks in real time by registering incoming frames against map Gaussians, using each primitive's covariance for both rendering and registration. These two uses place conflicting demands on one covariance. The mapper shapes it to minimize photometric error, often flattening it against surfaces, while robust registration typically benefits from measurement uncertainty. We propose a dual-covariance parameterization. Each Gaussian keeps a single mean but holds two covariances: a rendering covariance optimized by the mapper, and a tracking covariance derived from an RGB-D sensor noise model. We further use the tracking covariances as Gaussian anchors for image corners, providing constraints in directions where depth geometry is weak. We evaluate on TUM RGB-D, ScanNet, Replica, and two outdoor sequences recorded with a RealSense D435i on wheeled and handheld platforms. We achieve robust tracking performance across multiple scenes and reduced odometry drift, while tracking at $\sim$ 60 FPS.

</details>

#### 2026-09-22 - Ultra-fast Neural Inference for Stochastic Gaussian Splatting Denoising

**Authors:** Chenxiao Hu, Hao Zhang, Yanchen Zhang, Meng Gai, Guoping Wang, Sheng Li
**Links:** [abs](https://arxiv.org/abs/2609.25604) - [pdf](https://arxiv.org/pdf/2609.25604)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Ultra-fast Neural Inference for Stochastic Gaussian Splatting Denoising
- 作者：Chenxiao Hu, Hao Zhang, Yanchen Zhang, Meng Gai, Guoping Wang, Sheng Li
- 出版日期：2026-09-22T02:51:29Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.25604 ；https://arxiv.org/pdf/2609.25604

### 一句话总结
该论文针对随机高斯泼溅渲染中因去除排序与 alpha 混合而引入的空间噪声，提出了一种时序神经去噪器，以在保持无排序、无混合光栅化性能的同时获得时间稳定且视觉可用的输出。

### 研究问题
随机渲染消除了高斯泼溅中的排序和 alpha 混合过程，但代价是引入空间噪声。论文关注的问题是：如何对视图一致的随机泼溅渲染器共享的像素流进行时序去噪，从而在自由相机导航时抑制噪声并获得时间稳定、视觉上令人满意的输出，同时不牺牲无排序、无混合光栅化带来的性能优势。

### 核心思路/方法
论文将时序去噪建模在视图一致的随机泼溅渲染器共享的像素流上，并在随机 2D 高斯泼溅渲染上验证所提出的时序神经去噪器。该方法组合了以下组件：
- 双路径指数移动平均累积；
- 逐像素学习到的信任预测，用于历史验证；
- 固定的各向异性空间滤波器；
- 带稳定化的方差门控合成。

### 主要贡献
- 提出了一种面向随机高斯泼溅渲染的时序神经去噪器，用于处理随机渲染引入的空间噪声。
- 在随机 2D 高斯泼溅渲染上验证了该去噪器。
- 方法结合了双路径指数移动平均累积、逐像素学习信任预测、固定各向异性空间滤波以及方差门控合成与稳定化。
- 去噪器能够在自由相机导航期间抑制噪声，产生时间稳定、视觉上 compelling 的输出，同时保留无排序、无混合光栅化性能。
- 组合流水线相对于排序 alpha 混合渲染器仍保留 PSNR 差距，但去噪器的开销低于移除排序和混合所节省的时间。

### 局限性
- 组合流水线相对于排序 alpha 混合渲染器仍存在 PSNR 差距。
- 摘要未提供足够信息说明具体实验数据集、评价指标数值、消融实验细节、不同场景下的泛化能力以及失败案例。
- 摘要未提供足够信息说明该方法是否适用于随机 2D 高斯泼溅之外的其它随机泼溅渲染设置。
- 摘要未提供足够信息说明训练成本、推理硬件条件以及实时性能的具体量化结果。

### 阅读优先级
中。理由：该工作针对随机高斯泼溅渲染去噪这一具体问题，提出了包含历史验证、空间滤波和方差门控合成的时序神经去噪方案，并强调去噪开销低于去除排序与混合节省的时间，具有明确的系统性能取向。但摘要未给出具体实验数据、对比细节和泛化范围，若读者关注随机高斯泼溅渲染、无排序无混合光栅化或时序神经去噪，则值得进一步阅读；若仅关注成熟高斯泼溅管线的通用改进，则优先级相对有限。

</details>

<details>
<summary>Abstract</summary>

Stochastic rendering eliminates the sorting and alpha blending process in Gaussian splatting, at the cost of introducing spatial noise. Formulating temporal denoising over the pixel stream shared by view-consistent stochastic splatting renderers, we propose a temporal neural denoiser validated on stochastic 2D Gaussian Splatting rendering, combining dual-path exponential moving average accumulation, per-pixel learned trust prediction for history validation, a fixed anisotropic spatial filter and a variance-gated composition with stabilization. The denoiser suppresses the noise, achieving temporally stable, visually compelling outputs during free camera navigation, all while retaining the sort-free, blend-free rasterization performance. The combined pipeline retains a PSNR gap to sorted alpha-blending renderers, but the denoiser's overhead stays below the time saved by removing sorting and blending.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

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

#### 2026-09-22 - Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping

**Authors:** Markus Käppeler, Rohit Mohan, Abhinav Valada
**Links:** [abs](https://arxiv.org/abs/2609.26325) - [pdf](https://arxiv.org/pdf/2609.26325)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping
- 作者：Markus Käppeler, Rohit Mohan, Abhinav Valada
- 出版日期：2026-09-22T12:36:48Z
- 分类：Embodied / Robotics / AR Applications（主要分类；二级分类摘要未提供）
- 链接：摘要页 https://arxiv.org/abs/2609.26325 ；PDF https://arxiv.org/pdf/2609.26325

### 一句话总结
论文提出一个无需 LiDAR 构建先验地图的框架：利用视觉方法从历史相机轨迹构建带语义特征的静态点云先验地图，并在运行时将其与多视角相机特征在 BEV 空间融合，以提升基于相机的 3D 目标检测与在线矢量化 HD 地图构建。

### 研究问题
基于相机的 3D 目标检测和在线矢量化 HD 地图构建能提供紧凑的场景表示，但二者都依赖准确的度量几何，并受深度歧义限制。长期部署中，重复轨迹的观测可累积为持久的点云先验，提供超出当前观测的几何上下文；然而现有显式点云先验方法依赖 LiDAR 建图，需要昂贵的 3D 测距传感器。论文关注的问题是：能否仅用视觉构建点云先验，并用于提升上述两个相机感知任务？

### 核心思路/方法
- 使用 Pi3X 从既往相机轨迹构建静态点云先验地图，并为每个点附加 DINOv3 特征。
- 运行时通过全局定位检索局部先验块，用稀疏体素骨干网络编码，并在鸟瞰图（BEV）中与提升后的多视角相机特征融合。
- 融合表示输入任务特定的稀疏 Transformer 头，分别预测 3D 目标和矢量化地图元素。

### 主要贡献
- 提出一个使用视觉构建几何-语义点云先验的框架，先验地图构建与在线推理均不需要 LiDAR。
- 在 Argoverse 2 上，视觉先验将强基线从 0.287 提升至 0.299 CDS，并将矢量化地图构建 mAP 从 0.669 提升至 0.750。
- 消融实验显示，语义 DINOv3 特征对矢量化地图构建尤其重要。
- 结果表明，视觉构建的几何-语义先验可作为长期场景记忆，改善两个相机感知任务。

### 局限性
- 除 Argoverse 2 外，是否在其他数据集或场景下有效，摘要未提供足够信息。
- 框架对全局定位、Pi3X 建图质量、DINOv3 特征质量的具体依赖程度与失效条件，摘要未提供足够信息。
- 与 LiDAR 先验方法相比的性能差距、计算与存储开销、长期部署中的更新机制，摘要未提供足够信息。
- 摘要未提供足够信息说明 3D 目标检测与矢量化地图构建两侧收益差异的具体原因。

### 阅读优先级
中。理由：该工作针对相机感知中深度歧义与 LiDAR 依赖问题，提出用视觉构建点云先验并同时服务两个重要任务，在 Argoverse 2 上有明确指标提升，且消融指出语义特征对地图构建重要；但摘要未提供跨数据集验证、计算开销和与 LiDAR 先验的对比等关键细节，是否具有广泛通用性尚不明确。

</details>

<details>
<summary>Abstract</summary>

Camera-based 3D object detection and online vectorized HD mapping provide compact scene representations for autonomous driving, but both depend on accurate metric geometry and remain limited by depth ambiguity. Over long-term deployment, observations from repeated traversals can be accumulated into persistent point cloud priors that provide geometric context beyond the current observations. Existing explicit point cloud prior approaches, however, rely on LiDAR-based map construction and therefore require expensive 3D ranging sensors. We propose a framework that constructs a static point cloud prior map from previous camera traversals using Pi3X and augments each point with DINOv3 features. At runtime, a local prior patch is retrieved using global localization, encoded with a sparse voxel backbone, and fused in bird's-eye view (BEV) with lifted multi-view camera features. Task-specific sparse transformer heads then predict 3D objects and vectorized map elements from the fused representation. On Argoverse 2, the vision-based prior improves a strong baseline from 0.287 to 0.299 CDS and from 0.669 to 0.750 vectorized mapping mAP. Ablations show that semantic DINOv3 features are particularly important for vectorized mapping. These results demonstrate that vision-built geometric-semantic priors provide an effective form of long-term scene memory for camera-based perception, improving both tasks without LiDAR for prior-map construction or online inference.

</details>

#### 2026-09-22 - MatchFusion: Explicit-Implicit Instance Matching for Spatio-Temporal Multimodal Autonomous Driving

**Authors:** Xiaoyu Li, Jiajia Fu, Long Shi, Tianyu Du, Ruihang Li, Xian Wu, Lijun Zhao, Yingtao Zhang, Lining Sun, Ruifeng Li
**Links:** [abs](https://arxiv.org/abs/2609.25860) - [pdf](https://arxiv.org/pdf/2609.25860)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MatchFusion: Explicit-Implicit Instance Matching for Spatio-Temporal Multimodal Autonomous Driving
- 作者：Xiaoyu Li, Jiajia Fu, Long Shi, Tianyu Du, Ruihang Li, Xian Wu, Lijun Zhao, Yingtao Zhang, Lining Sun, Ruifeng Li
- 出版日期：2026-09-22T08:24:12Z
- 分类：Embodied / Robotics / AR Applications
- 链接：abs: https://arxiv.org/abs/2609.25860 ；pdf: https://arxiv.org/pdf/2609.25860

### 一句话总结
MatchFusion 提出一种可学习的“显式—隐式”实例匹配与融合模块，用几何相似度与类别一致性初始化实例关联，再借助实例嵌入选择性细化，从而统一支持空间 LiDAR-相机与时间过去-当前交互，并在 nuScenes 上同时提升感知精度、降低计算与显存开销。

### 研究问题
论文关注多模态感知与端到端自动驾驶（E2EAD）中的稀疏实例表示交互问题：在空间 LiDAR-相机融合以及时间过去-当前交互中，由于几何差异和异构语义表示，可靠实例对应关系难以建立。摘要指出，已有路线存在两难：基于注意力的方法可利用上下文语义，但常需专门表示对齐，计算开销增加；基于结构化目标状态的关联方法高效且可解释，却缺乏上下文证据以解决歧义匹配。因此，核心问题是如何在保持高效与可解释的同时，获得足够的上下文信息来完成可靠实例匹配与融合。

### 核心思路/方法
摘要给出的方法要点如下：
- 提出 MatchFusion，一个面向时空多模态自动驾驶的可学习实例匹配与融合模块。
- 匹配初始化：使用几何相似度和类别一致性初始化成对亲和度。
- 选择性细化：对结构上合理的关联，使用实例嵌入进行选择性细化，以补充上下文证据。
- 融合机制：由得到的软匹配图（soft matchmap）引导一个通用的残差聚合算子，实现自适应信息交换。
- 统一形式：该“匹配—融合”统一 formulation 同时支持空间 LiDAR-相机交互与时间过去-当前交互，分别使用多视图图像平面几何和运动补偿 BEV 几何作为结构先验。
- 端到端集成：将时间 MatchFusion 集成进 SparseDrive，可在 E2E 框架内提升感知，且无需额外监督。

### 主要贡献
- 提出显式—隐式结合的实例匹配与融合模块 MatchFusion，用于时空多模态自动驾驶中的稀疏实例交互。
- 将几何相似度、类别一致性等结构化先验与实例嵌入的上下文细化结合，以缓解歧义匹配问题。
- 用统一的匹配—融合形式覆盖空间 LiDAR-相机与时间过去-当前两类交互，并分别采用多视图图像平面几何与运动补偿 BEV 几何作为结构先验。
- 在 nuScenes 上验证：在不同前端配置下取得一致的感知增益。
- 与先前以实例为中心的融合方法相比，MatchFusion 系统在更高感知精度的同时，FLOPs 降低 55.3%，GPU 显存使用降低 39.3%，匹配—融合模块仅占总感知延迟的 3.7%。
- 将时间 MatchFusion 集成到 SparseDrive 中，可在 E2E 框架内进一步提升感知，且无需额外监督。

### 局限性
摘要未提供足够信息。摘要未说明失败场景、对特定数据集或前端配置的依赖程度、匹配错误的影响、可扩展性边界、训练数据需求、超参数敏感性、实时性在更广泛硬件或平台上的表现，也未提供定量结果之外的定性失败案例分析。

### 阅读优先级
高。理由：该工作直接针对多模态自动驾驶中稀疏实例时空交互的关键问题，且摘要报告了在 nuScenes 上精度提升的同时显著降低 FLOPs 和 GPU 显存，并将模块集成到 E2E 框架 SparseDrive 中；对关注多模态感知、端到端自动驾驶、实例级融合与效率优化方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Sparse instance representations provide a compact interface for spatial LiDAR-camera and temporal past-current interaction in multimodal perception and E2EAD. Effective interaction requires reliable instance correspondences despite geometric discrepancies and heterogeneous semantic representations. Attention-based methods exploit contextual semantics but often require specialized representation alignment, increasing computational overhead. In contrast, association based on structured object states is efficient and interpretable but lacks contextual evidence to resolve ambiguous matches. To combine these complementary strengths, we propose MatchFusion, a learnable instance matching and fusion module for spatio-temporal multimodal autonomous driving. MatchFusion initializes pairwise affinities using geometric similarity and category consistency, then selectively refines structurally plausible associations using instance embeddings. The resulting soft matchmap guides a common residual aggregation operator for adaptive information exchange. This unified matching-fusion formulation supports spatial LiDAR-camera and temporal past-current interaction, using multi-view image-plane geometry and motion-compensated BEV geometry as the respective structural priors. Experiments on nuScenes demonstrate consistent perception gains across diverse front-end configurations. Compared with a prior instance-centric fusion method, the MatchFusion-equipped system achieves higher perception accuracy while reducing FLOPs by 55.3% and GPU memory usage by 39.3%, with the matching-fusion module accounting for only 3.7% of total perception latency. Integrating temporal MatchFusion into SparseDrive further improves perception within an E2E framework without additional supervision. These results establish explicit-implicit matching as an effective and efficient mechanism for spatio-temporal instance interaction.

</details>

#### 2026-09-22 - Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes

**Authors:** Yuling Xi, Haokai Zhang, Muzhi Zhu, Hao Zhong, Zongze Du, Hengyu Zhao, Chenchen Jing, Yufei Yin, Bin Qin, Yongjie Yang, Zhenbo Luo, Hao Chen, Chunhua Shen
**Links:** [abs](https://arxiv.org/abs/2609.25841) - [pdf](https://arxiv.org/pdf/2609.25841)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D mapping, embodied AI, manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes
- 作者：Yuling Xi, Haokai Zhang, Muzhi Zhu, Hao Zhong, Zongze Du, Hengyu Zhao, Chenchen Jing, Yufei Yin, Bin Qin, Yongjie Yang, Zhenbo Luo, Hao Chen, Chunhua Shen
- 出版日期：2026-09-22T08:09:21Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.25841；PDF https://arxiv.org/pdf/2609.25841

### 一句话总结
论文提出面向室内场景的 Metric-Bench 基准与 MetricReasoner 微调方案，利用图像内已知物理尺寸的参考物体，引导 VLM 在不依赖相机内参的情况下进行上下文空间度量推理，并报告了多项基准上的性能提升。

### 研究问题
视觉语言模型（VLM）的度量推理对具身智能任务（如机器人操作、自主导航）至关重要，但当前空间推理受限于僵化的像素级监督；这种局部化优化可能损害通用多模态智能，导致性能下降或对广泛推理能力的灾难性遗忘。

### 核心思路/方法
- 构建 Metric-Bench：一个聚焦的基准，通过引入图像内具有已知物理尺寸的参考物体，利用上下文信息引导度量空间推理，使模型隐式学习 2D 到 3D 的映射，且不依赖相机内参。
- 提出 MetricReasoner：一种面向参考物 grounded 度量推理的任务适配强化微调方案，使用结构化提示和可验证的数值奖励。

### 主要贡献
- 提出 Metric-Bench，用于指导基于上下文信息的度量空间推理。
- 提出 MetricReasoner 强化微调方法，用于参考物 grounded 的度量推理。
- 在 Metric-Bench 上，方法显著增强空间度量理解，超过现有模型甚至更大的专有模型 43.1%。
- 下游具身性能相比空间专用对照模型，在 RoboSpatial 总体准确率上提升 30.4%，在 ERQA 上提升 9.3%。
- 在通用基准上也有持续增益：V$\star$Bench 提升 15.9%，BLINK 提升 88.9%，表明该适配不一定损害通用 VLM 能力。

### 局限性
- 论文摘要未提供足够信息说明基准的规模、数据来源、标注方式或场景多样性。
- 摘要未提供足够信息说明实验设置、对比基线细节、消融实验或失败案例。
- 摘要未提供足够信息说明方法在不同 VLM 架构、训练成本或真实机器人部署中的适用性与限制。
- 摘要未提供足够信息说明数值奖励的具体设计、结构化提示的具体形式及可验证性的边界。

### 阅读优先级
高。理由：该论文聚焦具身 AI 中关键的度量空间推理问题，同时提出基准与微调方法，并在摘要中报告了在空间、具身及通用基准上的多项显著提升；对关注 VLM 空间推理、机器人操作与自主导航的研究者有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Metric reasoning is a critical and challenging task for Vision Language Models (VLMs), playing a pivotal role in embodied AI tasks such as robotic manipulation and autonomous navigation. However, current spatial reasoning remains bottlenecked by rigid pixel-level supervision; such localized optimization often compromises general multimodal intelligence, triggering performance degradation or catastrophic forgetting of broad reasoning capabilities. To address these limitations, we introduce Metric-Bench, a focused benchmark designed to guide metric-spatial reasoning using contextual information. By incorporating in-image reference objects with known physical dimensions, Metric-Bench guides models to implicitly learn the 2D-to-3D mapping without camera intrinsics. We further present MetricReasoner, a task-adapted reinforcement fine-tuning recipe for reference-grounded metric reasoning, using structured prompts and verifiable numerical rewards. Extensive experiments on Metric-Bench demonstrate that our approach significantly enhances spatial metric understanding, outperforming existing and even larger proprietary models by 43.1\%, while improving downstream embodied performance over a spatial-specialized counterpart by 30.4\% on RoboSpatial overall accuracy and 9.3\% on ERQA, and additionally delivering consistent gains on general benchmarks (15.9\% on V$\star$Bench, 88.9\% on BLINK), indicating that the proposed adaptation does not necessarily compromise general VLM capabilities.

</details>

#### 2026-09-22 - PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation

**Authors:** Yu Zheng, Qiyu Feng, Yixin Wu, Baoquan Yang, Yixuan Zhou, Bingyang Hu, Kemeng Huang, Guansheng Yang, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2609.25653) - [pdf](https://arxiv.org/pdf/2609.25653)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation
- 作者：Yu Zheng, Qiyu Feng, Yixin Wu, Baoquan Yang, Yixuan Zhou, Bingyang Hu, Kemeng Huang, Guansheng Yang, Hesheng Wang
- 出版日期：2026-09-22T04:03:34Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.25653 （PDF: https://arxiv.org/pdf/2609.25653）

### 一句话总结
PhyVisGen 是一个兼顾物理与视觉高保真的机器人操作数据生成框架，用仿真数据训练的策略在五个真实机器人任务上达到 65–95% 成功率，且无需真实演示数据或策略微调。

### 研究问题
大规模操作演示数据对学习鲁棒的视觉运动策略至关重要，但真实世界数据采集成本高、难以规模化。仿真虽有潜力，但物理与视觉差异会限制合成数据的迁移性，尤其是在使用软体夹爪的操作场景中。

### 核心思路/方法
论文从物理与视觉两方面构建高保真数据生成框架：
- 物理侧：提出基于增量势接触（IPC）的机械臂—夹爪耦合方法，使完整操作轨迹中保持高保真软体接触。
- 视觉侧：结合真实场景重建与实时路径追踪，在保留所采集场景外观的同时生成视觉逼真的观测。

### 主要贡献
- 提出 PhyVisGen 框架，面向可扩展的机器人操作数据生成，兼具物理与视觉高保真。
- 引入基于 IPC 的机械臂—夹爪耦合方法，支持完整操作轨迹中的高保真软接触。
- 结合真实场景重建与实时路径追踪，生成保留场景外观的视觉逼真观测。
- 定量评估验证了框架的物理与视觉保真度。
- 仅用合成操作演示训练的策略在五个真实机器人任务上取得 65–95% 成功率，无需真实机器人演示数据或策略微调。

### 局限性
摘要未提供足够信息。摘要未说明方法的计算开销、IPC 耦合在更复杂接触场景下的适用边界、视觉重建对场景采集条件的要求、五个任务的具体类型与难度，以及失败案例或成功率波动的来源；也未提供与基线方法的对比细节。

### 阅读优先级
高。理由：该工作直接针对机器人操作数据规模化中的核心瓶颈（仿真到真实的物理与视觉差距），并给出无需真实演示与微调即可在真实任务上取得 65–95% 成功率的验证结果，对具身智能与机器人学习方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Large-scale manipulation demonstrations are essential for learning robust visuomotor policies, yet real-world data collection is expensive and difficult to scale. Simulation offers a promising alternative, but physical and visual discrepancies can limit the transferability of synthetic data, particularly for manipulation with soft grippers. We present PhyVisGen, a physically and visually high-fidelity framework for scalable robotic manipulation data generation. On the physical side, PhyVisGen introduces an arm-gripper coupling method based on the Incremental Potential Contact (IPC), enabling high-fidelity soft contact throughout complete manipulation trajectories. On the visual side, it combines real-scene reconstruction with real-time path tracing to generate visually realistic observations while preserving captured scene appearance. Quantitative evaluations demonstrate the physical and visual fidelity of PhyVisGen. Policies trained exclusively on synthetic manipulation demonstrations achieve 65-95% success across five real-robot tasks, without real-robot demonstration data or policy fine-tuning.

</details>

#### 2026-09-22 - Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation

**Authors:** Sunyu Wang, Jean Oh, Nancy S. Pollard
**Links:** [abs](https://arxiv.org/abs/2609.25619) - [pdf](https://arxiv.org/pdf/2609.25619)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation
- 作者：Sunyu Wang, Jean Oh, Nancy S. Pollard
- 出版日期：2026-09-22T03:25:32Z
- 分类：Embodied / Robotics / AR Applications（主要分类；次要分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2609.25619 ；PDF https://arxiv.org/pdf/2609.25619

### 一句话总结
该论文将手与工具建模为统一的“手-物体机构”（HOM），以相对接触速度约束来描述其运动，并提出一种轻量、物理可解释的运动规划与接触估计框架，使多指机器人手完成从抓取工具、装载到合适位姿再到挥舞工具的完整操作流程。

### 研究问题
如何让通用多指机器人手执行完整的工具操作过程，即拾取工具、将工具装载到合适位姿、然后挥舞工具。摘要指出，该工作关注的是完整流程，而不仅是其中某一环节。

### 核心思路/方法
- 受人类工具操作与机械设计原理启发，将手和工具建模为统一的“手-物体机构”（HOM），其由子装配体组成。
- 将 HOM 定义为由手、物体和广义接触坐标系构成，使 HOM 的运动可以用同一组笛卡尔空间相对接触速度表示，不依赖于手的运动学与几何结构。
- 将 HOM 的子装配体定义为手指之间的相对接触速度与接触力约束。
- 基于上述定义，开发了一个轻量且物理可解释的运动规划与接触估计框架，使用最小二乘法与互补滤波器。
- 评估方式为在仿真中遥操作五种不同的机器人手。

### 主要贡献
- 提出以相对接触速度统一表达手-工具机构运动的形式化定义，强调其不依赖具体手的运动学与几何。
- 提出将 HOM 分解为子装配体，并以手指间相对接触速度与接触力约束来定义子装配体。
- 提出基于最小二乘与互补滤波器的轻量、物理可解释的运动规划与接触估计框架。
- 实验结果显示，该框架使五种不同的手都能执行完整工具操作流程，并能从相同、简单的参考轨迹产生灵巧行为。
- 结果还展示了该框架对不同手、工具与任务具有一定适应性，其基础在于运动学与几何层面的建模。

### 局限性
- 摘要仅说明评估在仿真中通过遥操作五种机器人手完成，未提供真实机器人实验信息。
- 摘要未提供足够信息说明该方法在接触估计精度、规划鲁棒性、泛化边界、失败案例或计算开销方面的具体局限。
- 摘要未提供足够信息说明所测试工具、任务的具体范围以及“灵巧行为”的量化评价标准。
- 摘要未提供足够信息说明最小二乘与互补滤波器框架在不同噪声、不确定性或复杂接触条件下的表现。

### 阅读优先级
中。理由：该工作聚焦多指机器人手完整工具操作流程，并提出统一的手-物体机构表示与轻量规划/接触估计框架，对机器人操作与具身智能方向具有潜在参考价值；但摘要未提供真实机器人验证细节与定量局限信息，是否需要优先精读取决于读者对仿真验证、统一接触速度建模或工具操作规划的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

This work investigates how to enable general multi-finger robotic hands to perform the complete tool manipulation process, which entails picking up a tool, loading it into a suitable pose, and then wielding it. Inspired by human tool manipulation and mechanical design principles, we model the hand and the tool as a unified hand-object mechanism (HOM) composed of sub-assemblies. Specifically, we define a HOM as consisting of the hand, the object, and the generalized contact frames, allowing the HOM's motions to be expressed with the same set of Cartesian-space relative contact velocities, irrespective of the hand's kinematics and geometry. Then, we define a HOM's sub-assemblies as relative contact velocity and contact force constraints between fingers. Building on these definitions, we developed a lightweight and physically interpretable motion planning and contact estimation framework using least squares and a complementary filter. We evaluated our framework in simulation by teleoperating five different robotic hands. The results show that our framework enabled all five hands to execute the complete tool manipulation process, achieving dexterous behaviors even from identical, simple reference trajectories. Furthermore, the results showcase our framework's adaptability to different hands, tools, and tasks, enabled by its kinematic and geometric foundation.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
