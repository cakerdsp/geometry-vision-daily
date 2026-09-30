# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：46
- 分类分布：
  - Neural Scene Representations & Rendering: 16
  - Embodied / Robotics / AR Applications: 16
  - 3D Reconstruction & Multi-view Geometry: 7
  - Dynamic / 4D Reconstruction: 4
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **几何基础模型从“单一透视假设”走向“异构输入与稀疏高效”**
   - 代表论文：MEOW（混合相机前馈重建）、ReSS（3D ViT 稀疏注意力）。
   - 趋势：一边扩展输入形态的包容性（透视/鱼眼/全景混合、免标定免位姿），一边直面多视图 token 增长带来的计算瓶颈。MEOW 用“数据适配”而非改架构来吸收异构相机；ReSS 则指出注意力概率不等于块重要性，把稀疏选择目标从“保留注意力质量”改为“最小化残差流漂移”。两条线共同说明：几何基础模型正在从“能跑通”转向“输入更杂、视图更多、成本更低”。

2. **视频生成先验与几何隐空间/3D 表示的系统性耦合**
   - 代表论文：GeoVerse（几何隐空间+视频外观先验）、GenNVS（解耦 3D 先验条件化视频扩散）、RoGSW4RLD（多相机 rollout 提升为 4D 高斯场）。
   - 趋势：不再满足于“用扩散模型生成好看的新视角”，而是把生成过程锚定到几何表示（几何隐空间、3DGS、度量 4D 场）中，以抑制视频生成在顺序视角上的不一致累积。GeoVerse 用全局空间记忆对齐跨视角；GenNVS 用前景/背景解耦先验加 Dual-Stream Masking；RoGSW4RLD 直接把世界模型输出空间化为可跨视角、跨时间查询的度量场。这是“生成先验 + 几何约束”路线的集中体现。

3. **3DGS 从“重建表示”扩散为下游任务的基础设施**
   - 代表论文：CollisionSplatting（3DGS 上的碰撞感知规划）、EviSplat（3DGS 开放词汇分割）、AGILE-GS（主动 3DGS 的 NBV 选择）、OIC-GS（全向 3DGS 编解码）、SurgGMF（高斯运动预测）。
   - 趋势：3DGS 不再只是渲染/重建的终点，而被当作可查询、可规划、可编码、可预测的统一场景表示。CollisionSplatting 直接在标准 3DGS 上定义概率式距离度量；EviSplat 把多视图证据保留到查询时刻；SurgGMF 从历史高斯运动场预测未来高斯状态。3DGS 正在成为机器人、VR、医学等应用共享的空间中间层。

4. **具身智能强调“统一动作/场景表示 + 跨本体迁移”**
   - 代表论文：UMR/WEPVLA（统一操作表示）、RoGSW4RLD、DexAgent（Human2Sim2Robot 智能体框架）。
   - 趋势：跨本体数据难以复用，核心障碍是动作空间本体相关。UMR 把操作拆成世界坐标系物体运动（World Flow）+ 相对末端运动（Ego Trajectory），用 SE(3) 共轭耦合实现零样本技能迁移；DexAgent 用智能体式流程从单段人类视频生成物理合理轨迹；RoGSW4RLD 把多相机世界模型输出统一为度量 4D 场。三者都在回答“如何让异构演示/预测汇入共享表示”。

5. **评测有效性、数据/视角选择等“元问题”被显式提出**
   - 代表论文：When the Score Becomes the Target（自动驾驶度量有效性）、Less Is More（遗传视图选择）、AGILE-GS（NBV 选择）。
   - 趋势：当分数成为优化目标、当视图数量不再是越多越好、当信息搜索与相机选择可分离，研究开始反思“评的是什么”“选哪些输入”。这类工作不直接提升模型能力，但影响结论可信度与系统效率，值得关注。

#### 技术路线观察

- **几何基础模型**：MEOW 与 ReSS 代表两种应对思路——前者靠程序化数据引擎把异构相机当数据适配问题，保留透视预训练骨干；后者针对多视图全局注意力的计算主导，从注意力概率启发式转向残差流漂移最小化。共同点是尽量不推翻预训练骨干，而在输入分布或计算路径上做“外科手术”。这与 GeoVerse 利用预训练 3D 基础模型几何隐空间、只注入视频先验的思路一脉相承。

- **3D/4D 重建**：VideoPhysEdit 用刚体物理场景重建把物理推理显式化，支持反事实编辑；RoGSW4RLD 做前馈 4D 高斯提升，强调跨视角一致与度量性；3D Point Tracking with State Space Models 用冻结光流+度量深度前端，只学深度残差，并用 Mamba 状态空间模型控制内存。三者都在“重建之外”附加物理、时间或度量约束，且都倾向组合冻结前端、只学少量残差。

- **神经场景表示**：GeoVerse、GenNVS、EviSplat 都围绕 3DGS/几何隐空间做文章，但侧重不同——GeoVerse 强调跨视角世界一致性，GenNVS 强调前景几何结构保持，EviSplat 强调查询前不合并观测以保留证据。OIC-GS 则把 3DGS 推向编解码与传输，用分层 HEALPix 网格和率失真目标自适应分配基元。总体上，表示层正在被要求同时满足渲染质量、几何精度、可查询性和传输效率。

- **机器人/AR 应用**：CollisionSplatting 把 3DGS 拉进运动规划；MarsLab 与 Terrain-Aware Planetary Exploration 构成行星探索的仿真-实机组合；UMR、DexAgent、RoGSW4RLD 分别从动作表示、数据生成、世界模型空间化三个角度服务具身操作。应用侧的共同诉求是：表示必须可被规划器/策略直接消费，且尽量少依赖标定、位姿或本体特定定义。

#### 值得优先阅读的论文

1. **MEOW（2609.35658）**：混合相机单次前馈重建且免标定免位姿，若成立，对异构采集场景的通用性影响大；数据适配而非改架构的设计哲学也值得借鉴。
2. **GeoVerse（2609.35734）**：把视频生成先验注入几何隐空间并用全局空间记忆对齐，是“生成+几何”路线中较为完整的方案，直接关系到新视角合成的世界一致性问题。
3. **ReSS（2609.35593）**：对“注意力概率预测块重要性”这一常见假设提出反例，并给出残差流漂移的替代目标，对任何用 3D ViT 做多视图任务的工作都有方法迁移价值。
4. **RoGSW4RLD（2609.35311）**：把多相机世界模型 rollout 提升为度量 4D 高斯场，连接了世界模型与可查询空间表示，对机器人预测与规划有直接意义。
5. **UMR/WEPVLA（2609.34256）**：统一操作表示直击跨本体迁移痛点，0.5B 参数规模与双流 Point Action Adapter 的设计对具身策略研究有参考价值。

#### 可能的研究机会

- **异构相机与稀疏注意力的结合**：MEOW 解决输入形态异构，ReSS 解决视图增多后的注意力成本。二者尚未交叉——如果在混合相机元组上直接套用 3D ViT，全局注意力的开销与相机类型异质性可能同时恶化，值得研究面向异构输入的稀疏/分块注意力。
- **几何隐空间作为多任务共享中间层**：GeoVerse 用几何隐空间注入视频先验，EviSplat 用 3DGS 保留多视图证据，LEGAU 用语义高斯场作为位姿先验。可以探索一个统一的几何隐空间，同时服务新视角合成、开放词汇分割与类别级位姿估计，减少重复的场景表示。
- **世界模型输出的空间化与规划闭环**：RoGSW4RLD 把视频预测提升为 4D 高斯场，CollisionSplatting 在

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-29T14:04:22-04:00
**Total number of papers:** 46
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
<summary>AI 简析</summary>

### Metadata
- 标题：Many Eyes, One World: Feed-Forward 3D Reconstruction from Mixed Cameras
- 作者：Qiaoge Li, Yifan Zhan, Haijun Yang, Haiyang Liu, Yiyi Cai, Chenchi Luo
- 出版日期：2026-09-28T17:21:52Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.35658) | [PDF](https://arxiv.org/pdf/2609.35658)

### 一句话总结
MEOW 是一个前馈式 3D 重建系统，能在不提供标定、畸变参数、相机类型标签或位姿的情况下，从混合透视、鱼眼和全景图像的 N 视图元组中单次前向重建度量点图与相机位姿。

### 研究问题
真实世界采集具有异构性：同一重建任务中可能同时存在透视、鱼眼和 360° 全景图像，但大多数前馈 3D 重建模型假设输入为透视图像且表示统一。摘要指出，近期处理多种相机类型的模型要么需要告知每个视图的相机类型，要么一次只重建一对图像；尚无单次方法能从图像本身重建包含完整全景图的混合相机元组。

### 核心思路/方法
- 设计哲学：将异构相机重建视为数据适配问题，而非架构重新设计。
- 保留透视预训练骨干网络，通过程序化数据引擎学习异构相机。
- 数据引擎将每个场景渲染在连续的相机模型流形上，提供精确光线和深度，并为每个相机采样的训练元组认证共视性。
- 仅用合成元组训练，零样本迁移到真实采集。

### 主要贡献
- 提出 MEOW，一个前馈系统，可从单个 N 视图混合相机元组（透视、鱼眼、完整全景）中一次前向联合重建度量点图和相机位姿，且不提供标定、畸变参数、相机类型标签或位姿。
- 提出以数据适配为核心的设计思路，保留透视预训练骨干，依靠程序化数据引擎学习异构相机。
- 摘要报告了零样本迁移结果：在异构 2D3DS 元组上达到 79.9 mAA@30，而 Wid3R 在已知每个视图相机类型时为 53.8；在激光扫描混合相机基准上，每个四视图混合元组配准达到 79.4 AUC@30。
- 将发布数据引擎、基准和完整评估流程。

### 局限性
- 摘要未提供足够信息说明方法在真实场景中的失败模式、计算成本、对极端相机模型的泛化边界或消融实验细节。
- 摘要未提供足够信息说明训练数据规模、合成与真实域差距的具体影响。
- 摘要未提供足够信息说明基准的完整构成与评估协议细节。

### 阅读优先级
高。理由：该工作针对混合相机前馈 3D 重建这一明确且具挑战性的问题，声称在单次前向中处理包含全景图的异构元组，并报告了相对基线的显著指标提升；同时涉及数据引擎、基准与评估流程的发布，对 3D 重建与多视图几何方向具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：ReSS: Residual-Restoring Sparse Attention for 3D Vision Transformers
- 作者：Yongsung Kim, Jaehoon Lee, Minjun Park, Wooseok Song, Hun Hwangbo, Sungroh Yoon
- 出版日期：2026-09-28T16:43:55Z
- 分类：primary: Geometry Foundation Models；secondary: 未提供
- 链接：摘要页 https://arxiv.org/abs/2609.35593 ；PDF https://arxiv.org/pdf/2609.35593 ；代码 https://github.com/libary753/ReSS

### 一句话总结
ReSS 将 3D 视觉 Transformer 中的注意力块稀疏选择，从“保留高注意力概率块”改为“最小化稀疏化在残差流中造成的漂移”，以在相同稀疏度下更好地保持稠密性能。

### 研究问题
3D 视觉 Transformer（如 VGGT）在多视图图像上单次前向预测相机位姿和场景几何，但其对所有拼接视图 token 的全局注意力会随视图数量增长而主导计算。已有的 SparseVGGT 和 HeSS 在块级别稀疏化注意力，并都保留高注意力概率的块。然而论文观察到：注意力概率并不能很好预测移除某个块后模型行为的实际变化，这种不匹配正是稀疏度提高时性能崩溃的原因。

### 核心思路/方法
论文提出 ReSS（ReSidual-ReStoring Sparse Attention），将块选择问题重新表述为：不再最大化保留的注意力质量，而是最小化稀疏化在残差流中留下的漂移。具体引入一个漂移分数（drift score），量化每个块对残差的偏移程度；由于一个被丢弃集合的漂移取决于贡献向量的方向而非仅其幅度，论文进一步采用迭代式残差恢复程序，从整体上细化丢弃集合。

### 主要贡献
- 指出注意力概率与实际移除块后模型行为变化之间存在不匹配，并说明该不匹配是稀疏度增加时性能崩溃的原因。
- 提出 ReSS，将块选择从最大化保留注意力质量转为最小化残差流漂移，并引入漂移分数与迭代残差恢复程序。
- 在三个骨干网络和五个数据集上，ReSS 在匹配稀疏度下比先前方法更好地保持稠密性能。
- 提供两项支持“漂移是决定稀疏化代价的量”的结果：最大化漂移会比随机选择更快降低性能；以实际漂移而非稀疏度作图时，所有方法大致落在一个曲线上。
- 代码已公开。

### 局限性
摘要未提供足够信息。摘要未说明具体骨干网络、数据集名称、计算开销细节、不同稀疏度范围、失败案例或方法适用边界。

### 阅读优先级
高。理由：该论文针对 3D 视觉 Transformer 全局注意力随视图数增长的计算瓶颈，提出与既有“高注意力概率保留”不同的稀疏化准则，并且摘要给出跨三个骨干、五个数据集的对比结果以及支持核心论点的额外证据，同时公开代码；对关注 3D 视觉 Transformer、几何基础模型和注意力稀疏化的读者具有较高参考价值。

</details>

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

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-28 - RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts

**Authors:** Jin Hyun Kim, Min Young Kim, Soohwan Song, Daekyum Kim
**Links:** [abs](https://arxiv.org/abs/2609.35311) - [pdf](https://arxiv.org/pdf/2609.35311)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, 4D Gaussian, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts
- 作者：Jin Hyun Kim, Min Young Kim, Soohwan Song, Daekyum Kim
- 出版日期：2026-09-28T14:46:58Z
- 分类：Dynamic / 4D Reconstruction；次要分类：Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.35311 ；PDF https://arxiv.org/pdf/2609.35311

### 一句话总结
RoGSW4RLD 以前馈式两阶段框架，将多相机机器人世界模型产生的视频预测提升为统一的、可随时间查询的度量 4D 高斯场。

### 研究问题
动作条件视频世界模型能够从多相机预测未来机器人交互，但其输出仍是彼此分离的视频集合，而非可在不同视角和时间上查询的共享度量场景。现有 4D 重建方法虽然可用于空间化这些预测，但独立重建并合并各相机流无法保证跨视角一致性；当移动的机器人搭载相机与固定外部视角混合时，这一问题尤为严重。摘要未提供更多关于问题定义边界或适用范围的细节。

### 核心思路/方法
- 提出 RoGSW4RLD，一个前馈框架，将同步多相机 rollout 提升为统一的、可随时间查询的度量 4D 高斯场。
- 不学习单独的几何转移模型，而是直接重建现有世界模型生成的视觉未来。
- 核心为两阶段架构：
  - 阶段 1：融合跨视角证据与机器人特定的铰接几何和运动学，联合形成度量 4D 场。
  - 阶段 2：细化场的几何与外观，同时严格保持初始时间位移。

### 主要贡献
- 提出面向机器人世界模型 rollout 的前馈式 4D 高斯提升框架，将多相机视频预测统一为可跨视角与时间查询的度量 4D 表示。
- 设计两阶段架构，在阶段 1 融合跨视角证据与机器人铰接几何/运动学，在阶段 2 细化几何与外观并保持时间位移。
- 在 256 个留出的 DROID episode 上评估，相比逐相机重建加校准合并，新视角 PSNR 提升 2.15 dB，深度 AbsRel 降低 47%，机器人位移误差降低 61%。
- 在动作条件 Cosmos 3 rollout 上同样获得稳健增益，表明预测的视频未来可被转化为一致、可空间查询的 4D 度量表示。
- 摘要未提供足够信息说明其具体网络结构、训练损失、数据预处理细节或计算成本。

### 局限性
- 摘要未提供足够信息说明方法在极端视角变化、遮挡、动态物体复杂性或长时序下的表现。
- 摘要未提供足够信息说明对世界模型预测误差的敏感性与鲁棒性。
- 摘要未提供足够信息说明评测是否覆盖真实机器人闭环控制或仅限离线指标。
- 摘要未提供足够信息说明计算资源、推理速度与实时性。
- 摘要未提供足够信息说明与其他 4D 重建方法的全面对比范围。

### 阅读优先级
高。理由：该工作直接针对机器人世界模型输出难以跨视角、跨时间统一查询的问题，提出前馈 4D 高斯提升与两阶段融合思路，并在摘要中给出明确的定量提升；主题同时涉及动态/4D 重建、神经场景表示与机器人/具身应用，属于交叉热点，值得优先阅读。

</details>

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

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-28 - VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction

**Authors:** Conghan Yue, Yuanjie Chen, Yue Han, Ya Gao, Yunyan Xiao, WeiYao Zhang, Zhineng Chen
**Links:** [abs](https://arxiv.org/abs/2609.35134) - [pdf](https://arxiv.org/pdf/2609.35134)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction
- 作者：Conghan Yue, Yuanjie Chen, Yue Han, Ya Gao, Yunyan Xiao, WeiYao Zhang, Zhineng Chen
- 出版日期：2026-09-28T13:25:37Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.35134 ；PDF https://arxiv.org/pdf/2609.35134 ；代码 https://github.com/Hammour-steak/VideoPhysEdit

### 一句话总结
VideoPhysEdit 提出一种免训练流程，通过刚体物理场景重建显式进行物理推理，以生成物理反事实视频编辑结果，并配套构建基准与评价指标。

### 研究问题
论文关注“物理反事实视频编辑”（PCVE）：给定源视频、一个物理编辑及其执行帧，生成描绘编辑后运动与交互结果的视频。既有视频编辑方法多关注阴影、遮挡等视觉后果，而对编辑引发的后续运动与交互等物理后果探索不足。PCVE 的难点在于需要理解场景物理、推断物理干预引起的下游运动与交互，同时缺乏成对的事实/反事实数据和专门评价指标。

### 核心思路/方法
论文提出 VideoPhysEdit，一个面向刚体场景的免训练 PCVE 流程。其核心是通过一种新的物理场景重建方法使物理推理显式化：重建出的场景能够在仿真下复现观察到的运动与交互，从而支持将物理编辑作为干预施加，并利用产生的轨迹引导反事实视频生成。论文还构建了 PCVE-RigidBench 合成基准，包含成对的源视频与反事实目标视频以及物理真值，并提出 Physical Edit Score 指标。

### 主要贡献
- 形式化定义了物理反事实视频编辑（PCVE）任务。
- 提出免训练流程 VideoPhysEdit，通过刚体物理场景重建实现显式物理推理，并用仿真轨迹引导反事实视频生成。
- 构建 PCVE-RigidBench 合成基准，提供成对源视频、反事实目标视频与物理真值。
- 提出 Physical Edit Score 评价指标。
- 实验显示 VideoPhysEdit 在物理编辑准确率上显著高于开源方法与商业模型，同时保持有竞争力的视觉保真度，其 Physical Edit Score 为 0.376，是对比方法中唯一为正的分数；真实视频定性比较显示其适用于真实场景，并比对比方法更好地描绘编辑引发的下游运动与交互。

### 局限性
摘要未提供足够信息说明方法在非刚体场景、复杂真实场景泛化能力、计算成本、失败案例或基准多样性方面的具体局限；仅可从摘要推断其方法面向刚体场景，且基准为合成基准，但摘要未给出进一步局限讨论。

### 阅读优先级
高。理由：论文提出新的任务定义 PCVE，并同时给出方法、合成基准与评价指标，属于问题设定与方法/评测配套的工作；且摘要声称在物理编辑准确率上显著优于开源与商业方法，并报告唯一正值的 Physical Edit Score，对视频编辑、物理推理、3D 重建与多视图几何交叉方向具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：LEGAU: Learning Semantic Gaussian Priors for Scalable Category-level Pose Estimation
- 作者：Hongli Xu, Zhaowei Lu, Junwen Huang, Jiaqi Hu, Peter KT Yu, Benjamin Busam, Federico Tombari, Slobodan ilic
- 出版日期：2026-09-28T12:42:19Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.35046 ；PDF https://arxiv.org/pdf/2609.35046

### 一句话总结
LEGAU 通过联合预测 NOCS 对应、物体位姿与尺寸、以及规范化语义高斯场，将高斯场作为类别条件下的结构先验参与多模态特征融合，从而提升类别级 6D 位姿估计的可扩展性。

### 研究问题
单张 RGB-D 观测下的类别级 6D 位姿估计本质上是欠约束问题：需要在部分可见几何的基础上，结合物体的规范化结构才能确定稳定位姿。摘要指出，该任务需要同时解释局部可见几何与全局规范结构，因此如何有效耦合形状表征与位姿推理是关键问题。

### 核心思路/方法
LEGAU 是一个统一框架，同时预测三部分输出：NOCS 对应、物体位姿与尺寸、以及规范语义高斯场。其核心设计不是把重建当作独立的辅助任务，而是将高斯场作为“类别条件下的结构先验”，参与多模态特征融合，并为局部位姿推理提供全局引导。方法以类别文本嵌入为条件，通过基于 transformer 的融合模块处理 RGB-D 观测，整合视觉、几何与类别级线索，最终解码出 NOCS 图、位姿与尺寸信息以及基于高斯的物体表征。

### 主要贡献
- 提出统一框架 LEGAU，联合学习规范对应、物体形状与位姿对齐。
- 将语义高斯场作为类别条件结构先验，融入多模态特征融合并引导局部位姿推理，而非作为分离的辅助重建任务。
- 在合成与真实世界基准上验证了该耦合位姿-形状公式在单模型多类别设定下的性能，摘要称在 SOPE 上最高提升 22%，并具有竞争力的真实数据迁移表现。

### 局限性
摘要未提供足够信息。摘要未说明具体失败场景、计算开销、对类别文本嵌入质量的依赖、真实数据迁移的具体限制或消融分析的细节。

### 阅读优先级
中。理由：该论文关注类别级 6D 位姿估计中形状先验与位姿推理的耦合，属于 3D 重建与多视图几何方向，且摘要报告了较明显的性能提升；但摘要未提供足够实验细节与局限说明，是否值得深入精读需结合全文的实验设计、基线对比与真实场景泛化能力进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Functional Hand Type Prior for 3D Hand Pose Estimation and Action Recognition from Egocentric View Monocular Videos
- 作者：Wonseok Roh, Seung Hyun Lee, Won Jeong Ryoo, Jakyung Lee, Gyeongrok Oh, Sooyeon Hwang, Hyung-gun Chi, Sangpil Kim
- 出版日期：2026-09-28T02:29:40Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类；次要分类摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2609.34149) / [PDF](https://arxiv.org/pdf/2609.34149)

### 一句话总结
论文提出以“功能性手部类型”作为先验，通过估计三维手部姿态、物体类别与手部类型，并聚合长时段逐帧知识，提升第一视角单目视频中的动作识别性能。

### 研究问题
当前第一视角动作识别方法在感知动态手部运动时，往往仅依赖几何或物理信息，难以充分理解真实场景中的细粒度交互。论文希望解决如何利用手部功能配置与物体之间的关联，来增强对连续手部交互的解释能力。

### 核心思路/方法
论文从功能视角引入一种实用的手部类型分类体系，并基于该体系对现有数据集进行逐帧手部类型标注。随后提出一个考虑手部类型语义细节作为先验的手部动作识别框架，以增强网络对动作序列中连续手部交互的理解。

整体流程包含三个主要模块：
1. **Feature Extraction**：特征提取。
2. **Egocentric Knowledge Module**：利用短时线索估计三维手部姿态、物体类别和手部类型。
3. **Egocentric Action Module**：在更长时间范围内聚合逐帧知识，包括手部类型的文本嵌入。

### 主要贡献
- 从功能视角提出一种实用的手部类型分类体系，并用于现有数据集的逐帧手部类型标注。
- 提出一种新的手部动作识别框架，将手部类型的语义细节作为先验纳入建模。
- 设计包含特征提取、第一视角知识模块和第一视角动作模块的整体流程，其中动作模块聚合逐帧知识及手部类型文本嵌入，以增强对连续手部交互的理解。
- 在大规模基准 FPHA 和 H2O 上的广泛实验表明，模型优于当前最先进方法，展示出更优性能。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法的具体失败场景、计算开销、对标注质量的依赖程度、跨数据集泛化限制或消融实验细节。

### 阅读优先级
中。理由：论文聚焦第一视角单目视频中的三维手部姿态估计与动作识别，并提出“功能性手部类型先验”这一较有辨识度的建模思路，且声称在 FPHA 和 H2O 上优于现有方法；但摘要未提供足够实验细节、方法限制与可复现信息，是否值得深入阅读需结合全文中的实验设置、消融与泛化分析进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：EpiTransfer: Sparse, Training-Free Long-Range Depth Estimation from Temporal Monocular Aerial Frames
- 作者：Diksha Aggarwal, Rutvik Dagadkhair, Sanjana Srivastava, Bradley Denby, Kevin Kochersberger
- 出版日期：2026-09-27T21:30:23Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.33939

### 一句话总结
本文提出一种无需训练、基于对极转移（epipolar transfer）的深度估计方法，仅用两帧单目图像和相机位姿估计，通过合成虚拟立体对将时间对应转化为立体三角化任务，在无人机与室内场景中表现优于未针对该域训练的现成学习基线。

### 研究问题
可靠的三维空间理解对自主导航、避障和场景重建至关重要。现有学习型深度估计方法在分布内精度高，但对新视角和新高度泛化能力差。论文希望在无需训练数据的条件下，利用稀疏单目航拍时序帧实现长距离深度估计。

### 核心思路/方法
- 采用几何推导的、无需训练（training-free）的深度估计方法。
- 输入仅为两张单目图像和相机位姿估计。
- 利用相机运动合成一个基线可自由选择的虚拟立体对。
- 将时序对应问题转化为立体三角化任务。
- 该方法旨在缓解直接双视图三角化固有的几何退化问题。
- 验证场景包括户外无人机飞行（最大约 90 m 范围）和室内 OptiTrack 环境，并以 LiDAR 真值作为参考。

### 主要贡献
- 提出一种几何推导、无需训练、稀疏的长距离深度估计方法，仅依赖两帧单目图像与相机位姿。
- 通过合成虚拟立体对，将时序对应转化为立体三角化，以缓解直接双视图三角化的几何退化。
- 在户外无人机飞行与室内 OptiTrack 环境中使用 LiDAR 真值验证，室内达到 AbsRel 0.092、δ<1.25 为 0.940。
- 与直接三角化（AbsRel 0.073）精度相当，但在更具挑战性的场景中保留有效深度的比例更大。
- 显著优于未针对该域训练或微调的现成学习基线 ZoeDepth（AbsRel 0.225）和 Depth Anything V2（AbsRel 0.570），且无需训练数据。

### 局限性
- 摘要仅给出室内 AbsRel 与 δ<1.25 指标，户外场景的量化结果摘要未提供足够信息。
- 摘要未提供方法对相机位姿估计误差的敏感性分析，摘要未提供足够信息。
- 摘要未提供不同基线选择策略的具体影响，摘要未提供足够信息。
- 摘要未提供计算效率或实时性数据，摘要未提供足够信息。
- 摘要未提供与直接三角化相比在哪些具体挑战场景下有效深度比例更大的细节，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文聚焦无需训练、仅依赖两帧单目航拍图像与相机位姿的长距离深度估计，问题设定明确，且提供了与 LiDAR 真值及多个现成学习基线的定量对比；对三维重建、多视图几何和空中自主导航方向具有直接参考价值。

</details>

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

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-28 - GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space

**Authors:** Kerui Ren, Tao Lu, Linning Xu, Changjian Jiang, Mu Huang, Chunhua Shen, Mulin Yu, Bo Dai
**Links:** [abs](https://arxiv.org/abs/2609.35734) - [pdf](https://arxiv.org/pdf/2609.35734)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space
- 作者：Kerui Ren, Tao Lu, Linning Xu, Changjian Jiang, Mu Huang, Chunhua Shen, Mulin Yu, Bo Dai
- 出版日期：2026-09-28T17:51:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.35734) / [PDF](https://arxiv.org/pdf/2609.35734)

### 一句话总结
GeoVerse 在预训练 3D 基础模型的几何隐空间中融合视频生成模型的外观先验，并通过全局空间记忆实现跨视角一致的新视角合成。

### 研究问题
从稀疏图像进行新视角合成时，需要同时满足两个目标：对已观测区域进行忠实重建，以及对未见内容进行合理补全，并在不同视角之间保持世界一致性。摘要指出，现有基于几何的方法能保留已观测场景结构，但往往难以补全未见区域；视频生成模型虽提供丰富外观先验，但在顺序生成视角时会累积不一致性。

### 核心思路/方法
- 在预训练 3D 基础模型的几何隐空间中执行生成，而非直接在图像空间生成。
- 从 Wan2.2 VACE 提取多层级特征，并通过 ControlNet 风格的适配器注入几何隐扩散模型，以引入视频学习到的外观先验来增强结构补全。
- 引入全局空间记忆，持续聚合已观测与已合成内容，并将目标对齐的引导重新投影，使后续预测锚定到共享场景表示，从而增强跨视角一致性。

### 主要贡献
- 提出 GeoVerse 框架，将视频生成模型的外观先验注入几何隐空间扩散模型，以兼顾几何结构与未见区域补全。
- 设计 ControlNet 风格适配器，实现 Wan2.2 VACE 多层级特征向几何隐扩散模型的注入。
- 提出全局空间记忆机制，通过重投影目标对齐引导来维持跨视角的世界一致性。
- 摘要报告了在多个数据集上的实验：相比 GLD，在 DL3DV 上 PSNR 高 2.23 dB，在 Mip-NeRF360 上 ATE 低 32.4%。

### 局限性
- 摘要未提供足够信息说明方法的具体失败情形或适用边界。
- 摘要未提供足够信息说明对计算资源、训练数据规模或推理速度的要求。
- 摘要未提供足够信息说明全局空间记忆在长序列或大范围场景中的扩展性。
- 摘要未提供足够信息说明各数据集上除 PSNR 与 ATE 外的其他指标表现。

### 阅读优先级
高。理由：该论文聚焦稀疏视角新视角合成中的世界一致性与未见区域补全这一核心难题，方法上结合 3D 基础模型几何隐空间、视频生成先验与空间记忆机制，且摘要给出了相对基线 GLD 的明确量化提升，适合关注神经场景表示与渲染方向的研究者优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism
- 作者：R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti
- 出版日期：2026-09-28T16:57:15Z
- 分类：Neural Scene Representations & Rendering（主分类）；副分类摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2609.35619) ｜ [PDF](https://arxiv.org/pdf/2609.35619)

### 一句话总结
论文提出 CollisionSplatting——一种直接作用于标准 3D Gaussian Splatting 场景、可调保守度的 GPU 加速概率式距离度量，用于将碰撞感知代价与图像条件奖励统一到运动规划中。

### 研究问题
将稠密视觉信息整合进运动规划仍然困难：几何规划器依赖丢弃视觉丰富度的抽象场景表示，而学习型视觉模型往往缺乏几何可解释性与计算效率。论文试图在保留 3DGS 场景视觉丰富度的同时，实现具备几何可解释性和高效率的碰撞感知规划。

### 核心思路/方法
- 提出 CollisionSplatting：一种简单、模块化、GPU 加速、受概率启发且保守度可调的距离度量，直接运行在标准 3DGS 场景上。
- 与学习到的图像条件奖励函数结合后，该度量通过将碰撞感知代价与图像空间目标统一起来，支持几何与视觉的联合规划。
- 将该度量分别集成进 GPU 加速的 Model Predictive Path Integral（MPPI）与 Rapidly-Exploring Random Tree（RRT）规划器中。
- 在真实世界的视觉引导导航与操作任务中展示了该度量的有效性，并强调 3DGS 可作为丰富感知与实时运动规划之间的实用桥梁。

### 主要贡献
- 提出直接作用于标准 3DGS 场景的、可调保守度的概率式距离度量 CollisionSplatting。
- 实现碰撞感知代价与图像条件目标的统一，从而支持几何与视觉联合规划。
- 将该度量集成到 GPU 加速的 MPPI 与 RRT 规划器中。
- 在碰撞分类性能上与代表性基线持平或更优，同时碰撞检测吞吐显著更高、VRAM 占用显著更低（具体数值摘要未提供足够信息）。
- 在真实世界视觉引导导航与操作任务中验证了该度量的有效性。

### 局限性
摘要未提供足够信息。摘要未提及具体实验设置、对比基线的细节、失败案例、度量保守度调节的代价、方法对 3DGS 重建质量的依赖程度，以及真实世界任务的具体规模与评价指标。

### 阅读优先级
中。理由：该工作面向 3DGS 与运动规划交叉方向，提出的是模块化度量并集成到两种主流规划器中，且报告了吞吐与显存方面的优势，对关注神经场景表示用于机器人规划的研究者有参考价值；但摘要未给出定量结果细节与消融信息，是否构成关键突破需进一步阅读全文判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Less Is More: Genetic Frame Selection for Efficient Novel View Synthesis
- 作者：Diego E. Farchione, Ramzi Idoughi, Alberto Jaspe-Villanueva, Peter Wonka
- 出版日期：2026-09-28T16:33:50Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.35573 ；PDF https://arxiv.org/pdf/2609.35573

### 一句话总结
提出一种无需渲染的视图选择器，从已拍摄序列中挑选固定数量且信息量最大的输入帧，用于高效的新视角合成，并声称在多个数据集和输入预算下优于几何与重建感知的基线方法。

### 研究问题
前馈式新视角合成可从多张输入图像中单次前向重建场景，但更多视图不一定带来更好性能：冗余或选择不佳的帧会增加计算成本，甚至可能降低重建质量。论文关注的核心问题是：在已捕获的序列中，如何为指定目标视角选取一个固定大小的、对重建最具信息量的输入子集。

### 核心思路/方法
- 提出一种**无需渲染的视图选择器**，对候选帧从三个互补标准进行打分：
  1. **目标视图覆盖度**：以已观测帧作为目标视角的替代进行度量；
  2. **与已选视图的冗余度**；
  3. **图像清晰度**。
- 使用一个轻量级打分网络，在推理时无需渲染、重建或逐场景优化即可选出信息量最大的帧。
- 训练选择器时，通过**蒸馏一个昂贵的离线搜索过程**：用遗传算法在训练场景上直接优化重建性能，找出高质量子集；选择器仅从几何和图像级特征中学习复现这些选择。
- 摘要称该方法在六类数据集和多种输入预算下，持续优于几何类和重建感知的视图选择基线，选择成本显著低于基于重建的替代方案；精心选择的子集甚至可超过使用完整输入序列的前馈重建。
- 学习到的选择器可泛化到多种重建范式（前馈、3D Gaussian Splatting、NeRF）、目标物体重建，以及目标视角来自独立采集过程的跨捕获设定。

### 主要贡献
- 提出一种无需渲染的视图选择方法，通过目标覆盖度、冗余度和清晰度三项标准选择固定大小输入子集。
- 使用遗传算法离线搜索高质量子集，并蒸馏到轻量级打分网络，使其在推理时无需渲染或逐场景优化。
- 在六个数据集和多种输入预算上，声称优于几何和重建感知的视图选择基线，且选择成本显著更低。
- 表明精心选择的子集可优于完整输入序列的前馈重建。
- 验证学习到的选择器可泛化到前馈、3D Gaussian Splatting 和 NeRF 等多种重建范式，以及目标物体重建和跨捕获设定。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、对特定场景类型或数据分布的敏感性分析、遗传算法离线搜索的计算开销细节、打分网络规模与推理延迟的具体数值，也未说明选择器在极端输入预算或严重遮挡、动态场景等条件下的表现。

### 阅读优先级
高。理由：该论文聚焦新视角合成中“输入视图选择”这一效率与质量的关键问题，提出无需渲染的选择器并结合遗传算法蒸馏，且声称在多种数据集、重建范式和跨捕获设定下均有优势；若关注高效三维重建、神经渲染或视图选择，值得优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation
- 作者：Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im
- 出版日期：2026-09-28T10:46:23Z
- 分类：Neural Scene Representations & Rendering（主类）；Embodied / Robotics / AR Applications（次类）
- 链接：[摘要](https://arxiv.org/abs/2609.34853) / [PDF](https://arxiv.org/pdf/2609.34853)

### 一句话总结
EviSplat 提出在 3D Gaussian Splatting 中保留每个观测的独立特征作为“证据”，等到文本查询到来时再根据查询动态聚合，从而避免查询前多视图信息合并造成的线索损失。

### 研究问题
开放词汇三维场景理解希望无需固定类别词表，就能根据自由文本查询定位与分割对象。已有方法多基于 3D Gaussian Splatting，并在查询未知之前，将多视图观测（如单视图的掩码裁剪）整合为语言特征或紧凑对象描述符。但摘要指出，同一对象的不同视角观测信息量并不相等：有的包含与特定查询相关的线索，有的则提供不完整甚至误导性的证据。查询前的提前整合，可能抑制后续查询真正依赖的线索。

### 核心思路/方法
EviSplat 的核心是“保留个体观测特征，直到文本查询时刻再使用”。具体而言：
- 将个体观测特征保留在类别无关的三维实例中，这些实例可表示对象、对象部件或背景区域。
- 为每个 Gaussian 学习一个分布，描述其观测支持哪些视觉外观。
- 给定文本查询后，先对每个实例使用其最相关的观测进行打分。
- 再为每个 Gaussian 计算分数，方式是结合实例级相关性与局部支持的证据，并按该 Gaussian 被观测的频率与明确程度进行加权。
- 由此，不同查询可以从同一份保留证据中调用不同的视觉线索。

### 主要贡献
- 提出 EviSplat，在开放词汇三维分割中保留多视图个体观测特征作为证据，而不是在查询前将其合并为单一语言特征或对象描述符。
- 将证据保留在类别无关的三维实例中，并学习每个 Gaussian 的外观支持分布。
- 设计查询时打分机制：先按实例最相关观测评分，再融合实例级相关性与局部证据，并按观测频率与明确程度加权。
- 摘要称在多种数据集和评估协议上取得 state-of-the-art 性能，支持“将多视图证据保留到查询时并按查询聚合”的有效性。

### 局限性
摘要未提供足够信息。摘要未给出具体失败情形、计算开销、内存占用、对 Gaussian 数量或视图数量的敏感性、在极端遮挡或观测不足条件下的表现，也未说明“观测频率与明确程度”加权方式可能带来的偏差。相关实验细节与消融结果需查阅原文。

### 阅读优先级
高。理由：该工作针对开放词汇三维场景理解中“查询前多视图信息整合”的关键问题提出明确替代思路，问题动机具体，方法与 3D Gaussian Splatting 紧密相关，且摘要声称在多样数据集与评估协议上达到 state-of-the-art；对三维场景表示、开放词汇分割及具身/机器人应用方向具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering
- 作者：Jingqian Sun, Yichao Tang
- 出版日期：2026-09-28T09:31:12Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.34733 ；PDF：https://arxiv.org/pdf/2609.34733

### 一句话总结
SurgGMF 提出一种全因果高斯运动预测框架，通过从历史高斯运动场预测未来高斯的位置、尺度和旋转残差，并结合“全因果末帧渲染协议”避免目标帧信息泄漏，从而把手术场景神经渲染从回顾式重建推进到预测式建模。

### 研究问题
动态手术场景建模对机器人感知、仿真和决策支持很重要。现有神经渲染方法虽能高效重建和渲染可变形手术场景，但主要聚焦于已观测帧的重建，而不是预测未来场景状态。论文要解决的核心问题是：如何在避免目标泄漏的前提下，实现面向未来手术场景渲染的因果高斯运动预测。

### 核心思路/方法
- 不直接预测未来 RGB 图像，而是从历史高斯运动场中预测未来高斯运动状态，具体表示为位置、尺度、旋转残差（X/S/R）。
- 引入 full-causal-last rendering protocol（全因果末帧渲染协议）：渲染未来高斯状态时不访问目标帧高斯属性，同时保留因果外观传播，以防止目标泄漏。
- 在 12 个 EndoNeRF 和 StereoMIS 视频切片上评估，使用神经时间学习器与经典动力学基线，并在统一预测协议下比较。
- 分析精度与效率的权衡：在当前实现下，TKAN 精度最高，而 GRU 和 LSTM 在模块级延迟方面更具优势。

### 主要贡献
- 提出 SurgGMF，一个用于预见性手术场景渲染的全因果高斯运动预测框架。
- 将预测目标从未来 RGB 图像转为未来高斯运动状态（位置、尺度、旋转残差）。
- 引入 full-causal-last 渲染协议，以避免目标帧高斯属性泄漏，同时保持因果外观传播。
- 在 12 个 EndoNeRF 和 StereoMIS 视频切片上，使用神经时间学习器和经典动力学基线进行统一预测协议下的评估。
- 结果显示，学习到的高斯运动预测在渲染空间上持续优于经典动力学基线，说明其收益超过手工状态外推。
- 延迟分析揭示了精度—效率权衡，并指出 TKAN、GRU、LSTM 在当前实现下的不同表现。
- 论文将结果定位为可复现的因果高斯运动预测框架，推动手术高斯表示从回顾式重建走向预测式场景建模。

### 局限性
摘要未提供足够信息。摘要未说明具体失败案例、数据规模限制、泛化到其他手术类型或设备的能力、临床部署可行性，也未给出完整计算成本、推理速度数值、超参数敏感性或与其他预测范式的全面对比。

### 阅读优先级
高。理由：该论文聚焦手术场景神经渲染中的未来状态预测，问题设定明确，且提出全因果渲染协议以避免目标泄漏；同时包含多数据集评估、神经时间学习器与经典动力学基线对比，以及精度—效率权衡分析，对关注动态手术场景建模、高斯表示和预测式渲染的研究者有较强参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GenNVS: Geometry-enhanced Novel View Synthesis via Disentangled 3D Prior
- 作者：Yajiao Xiong, Youyu Luan, Xiaoyu Zhou, Yongtao Wang
- 出版日期：2026-09-28T08:23:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接：https://arxiv.org/abs/2609.34579 ；PDF 链接：https://arxiv.org/pdf/2609.34579

### 一句话总结
GenNVS 通过解耦前景与背景的 3D 先验，并将其对齐为统一 3D 场景来条件化视频扩散模型，从而提升单图新视角合成中的几何结构保持与空间一致性。

### 研究问题
论文关注单图像新视角合成任务。摘要指出，该任务的核心困难在于底层 3D 几何高度模糊。尽管近期基于扩散的方法能产生看似合理的结果，但它们往往难以保持前景对象的几何结构和空间连贯性。

### 核心思路/方法
GenNVS 的核心是“通过解耦 3D 先验实现几何增强的新视角合成”。具体而言：
- 使用 3D Gaussian Splatting 分别建模前景对象和背景；
- 通过由粗到细的几何优化过程将二者对齐，形成统一的 3D 场景；
- 用该场景条件化一个视频扩散模型；
- 提出 Dual-Stream Masking 机制，联合利用渲染的有效性掩码和几何感知变形来引导合成。

### 主要贡献
- 提出 GenNVS 框架，用于几何增强的新视角合成，核心在于解耦的 3D 先验。
- 采用 3D Gaussian Splatting 分别表示前景对象与背景，并通过由粗到细的几何优化对齐成统一 3D 场景。
- 提出 Dual-Stream Masking 机制，以渲染有效性掩码和几何感知变形共同条件化视频扩散模型。
- 摘要称实验结果显示，GenNVS 在视觉质量和几何精度上优于近期方法，并自然支持灵活的场景编辑。

### 局限性
摘要未提供足够信息。未说明方法的具体失败场景、计算开销、对输入图像或场景类型的假设、评估数据集与指标细节，也未给出消融实验或用户研究等信息。

### 阅读优先级
高。理由：该论文聚焦单图新视角合成中关键的几何模糊与空间一致性问题，提出解耦 3D 先验、3D Gaussian Splatting 与视频扩散模型结合的具体框架，并声称在视觉质量和几何精度上优于近期方法，同时支持场景编辑；这些信息对神经场景表示与渲染方向具有较高相关性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting
- 作者：Yulong Cheng, Youneng Bao, Junfeng Zhou, Mu Li, Jie Wen
- 出版日期：2026-09-28T05:44:08Z
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（次）
- 链接：[摘要](https://arxiv.org/abs/2609.34367) / [PDF](https://arxiv.org/pdf/2609.34367)

### 一句话总结
论文提出 OIC-GS，一种基于分层 HEALPix 基元网格表示的全向高斯泼溅编解码器，通过球面率失真目标自适应决定基元分配并移除低收益基元，在单个比特流下同时支持全球、视口相关与渐进解码。

### 研究问题
学习图像编解码器（LICs）重建质量高，但解码速度不足以支撑沉浸式 VR；高斯泼溅（GS）编解码器渲染更快，但在重建质量上仍落后，且通常在决定基元分配时未考虑每个基元的编码代价。论文旨在解决全向 GS 编解码中重建质量、解码效率与基元分配之间的问题。

### 核心思路/方法
- 引入 OIC-GS，一种采用分层 HEALPix 基元网格表示的全向 GS 编解码器。
- 高斯基元锚定在预定义球面位置上，从而消除显式坐标编码。
- 更细层级对更粗祖先进行细化，自然支持粗到细重建和分层传输。
- 预定义网格支持高效视口解码，仅选择与视图相关的基元。
- 引入针对量化基元的轻量熵模型，并在球面率失真目标下优化编解码器。
- 当量化后不透明度变为零时，自动移除率失真收益不足的基元，使 OIC-GS 无需固定基元预算即可自适应调整基元密度和细节层级。
- 单个比特流支持全球、视口相关和渐进解码。

### 主要贡献
- 提出 OIC-GS 全向 GS 编解码器与新的分层 HEALPix 基元网格表示。
- 通过预定义球面锚点消除显式坐标编码，并支持粗到细重建、分层传输与视口相关解码。
- 引入轻量熵模型，并在球面率失真目标下优化，使基元可根据率失真收益自动移除，避免固定基元预算。
- 单个比特流支持全球、视口相关和渐进三种解码方式。
- 摘要报告：首个视口仅解码 52% 比特流即达到最终质量，渲染速度为 1,270 FPS；在 100 图像全向基准上，OIC-GS 优于所有被评估的 GS 编解码器，相比 GaussianImage++ 将 WS-PSNR BD-rate 降低 49.6%，相比使用学习熵模型的 SGI 降低 68.6%。

### 局限性
- 除摘要给出的结果外，论文的具体实验设置、数据集细节、消融实验、复杂度与内存开销等均未提供足够信息。
- 熵模型、率失真优化与基元移除策略的具体实现细节未提供足够信息。
- 与其他方法对比的完整评测范围、指标定义与统计方式未提供足够信息。
- 摘要未提供足够信息说明该方法在真实 VR 系统或不同硬件条件下的部署表现。
- 摘要未提供足够信息说明其在不同场景类型、分辨率或比特率下的泛化能力。

### 阅读优先级
高。理由：该论文直接针对全向 GS 编解码中重建质量、解码速度与基元分配代价之间的核心矛盾，提出分层 HEALPix 表示与率失真自适应基元选择，并报告了显著的 BD-rate 降低和视口解码效率，属于神经场景表示与渲染方向中较有实际价值的工作。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting
- 作者：Amirhossein Mollaei Khass, Nader Motee
- 出版日期：2026-09-28T02:53:40Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.34176

### 一句话总结
AGILE-GS 将“寻找信息最多的位置”与“在候选池中选择相机”分离，通过优化一个不一定可达的虚拟锚点姿态来引导候选视角评分，从而在无需渲染全部候选的情况下快速选出下一个最佳视角。

### 研究问题
辐射场重建需要大量视角，且视角的布置位置与数量同样重要。针对 3D Gaussian Splatting 的下一个最佳视角（NBV）选择，现有方法通常需要对候选池中的每个候选逐一评分再保留一个，搜索信息与选择相机混在一起，导致选择延迟高。论文要解决的问题是：如何在不渲染全部候选、也不对整个候选池计算 Fisher 信息的前提下，高效选出一个高质量的下一视角。

### 核心思路/方法
方法的核心是把信息搜索与相机选择拆成两个可分离的问题：

1. **锚点优化**：在 SE(3) 上用黎曼梯度上升优化一个虚拟锚点姿态，目标是期望信息增益。该锚点不需要可达，也不必存在于候选池中，它只用于标示模型最不确定的位置。
2. **候选评分与筛选**：候选视角依据锚点的观察几何进行评分，再通过一个贪心的 ridge-leverage 步骤把候选池蒸馏成一个小的、非冗余的候选短名单，此过程不渲染任何候选。
3. **两种使用方式**：
   - **AGILE-GS**：直接取短名单上的第一个视角作为下一视角，因此不对任何候选计算 Fisher 信息。
   - **AGILE-GS+**：对短名单中每个视角计算 Fisher 信息增益并选最优，使昂贵评估只在一小部分视角上运行，而非整个候选池。

### 主要贡献
- 提出将 NBV 选择中的信息搜索与相机选择分离的框架，并引入可不可达的虚拟锚点来标记模型最不确定的位置。
- 提出锚点引导的候选评分与贪心 ridge-leverage 筛选机制，在不渲染任何候选的情况下将候选池压缩为非冗余短名单。
- 提供两种变体：AGILE-GS 不计算任何候选的 Fisher 信息；AGILE-GS+ 仅对短名单计算 Fisher 信息。
- 摘要声称在标准基准和闭环具身采集场景中，两种变体均匹配或超过现有基线，同时将选择延迟降低一到两个数量级。

### 局限性
摘要未提供足够信息。摘要中未说明锚点优化是否依赖特定场景假设、短名单大小如何确定、在什么条件下 Fisher 信息评估不可省略、失败案例或具体延迟数值与基准名称等实验细节。

### 阅读优先级
中。理由：论文针对 3DGS 主动视角选择中的效率瓶颈提出了结构清晰的两段式分离方案，并声称延迟降低一到两个数量级，对关注主动重建、NBV 选择与 3DGS 效率的研究者有潜在参考价值；但摘要未提供具体实验设置、基准名称与定量结果，且该工作尚未经过摘要之外的信息验证，是否值得精读需结合全文实验与自身方向判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors
- 作者：Ge Gao, Siyue Teng, Chanqgi Wang, Fan Zhang, Nantheera Anantrasirichai, Jui Chiu Chiang, Wen-Hsiao Peng, David Bull
- 出版日期：2026-09-27T22:14:31Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2609.33969 ；PDF 链接 https://arxiv.org/pdf/2609.33969

### 一句话总结
论文提出 SAGA，一种基于稀疏 4D anchors 与 3D Gaussian Splatting 的体积视频编解码方法，通过层次化 anchor、坐标型 INR 解码与固定大小记忆槽的熵上下文建模，压缩动态 3D 场景并在摘要报告的实验中对 GIFStream 取得显著 BD-rate 降低。

### 研究问题
沉浸式视频通信需要既照片级真实、渲染高效又紧凑的动态场景表示。动态 3D Gaussian Splatting 虽具潜力，但因 primitives 密集且存在时空冗余而难以压缩。现有基于 anchor 的方法虽能以稀疏 scaffold 共享几何与外观来提升紧凑性，但通常依赖对单一 canonical scaffold 做变形，并且每个 primitive 仅独立地以其关联 anchor 为条件，这限制了处理非局部动态与去遮挡的能力，也未能充分利用 anchor 之间的相关性，尤其在运动或纹理密集区域。

### 核心思路/方法
论文提出 SAGA，作为建立在稀疏 anchor 辅助 Gaussian splatting 表示之上的体积视频编解码器。其核心包括：
- 使用层次化组织的稀疏 4D anchors 表示动态 3D 场景；
- 通过基于坐标的 INR 解码器，从 anchor 间插值生成精细 anchors 与 Gaussian primitives，从而在时空结构间实现紧凑的参数共享；
- 针对非结构化 anchors 之间的长程依赖，引入固定大小 memory slots，并采用 orthogonality-informed updates，用于准确的熵上下文建模。

### 主要贡献
- 提出 SAGA 体积视频编解码框架，基于稀疏 anchor 辅助的 Gaussian splatting 表示。
- 采用层次化稀疏 4D anchors 与坐标型 INR 解码器，通过 anchor 间插值生成精细 anchors 和 Gaussian primitives，实现跨时空结构的紧凑参数共享。
- 引入固定大小 memory slots 与 orthogonality-informed updates，以建模非结构化 anchors 间的长程依赖并服务于熵上下文建模。
- 实验显示 SAGA 对 GIFStream 取得强率失真性能，在 Neu3D 和 MPEG MIV 上分别实现 80.39% 与 83.94% 的 PSNR BD-rate 降低。

### 局限性
摘要未提供足够信息说明方法的失败场景、计算开销、解码复杂度、泛化边界或与更多基线方法的完整对比。摘要仅报告了相对 GIFStream 的 PSNR BD-rate 结果，未提供其他评价指标、数据集细节、消融实验细节或运行时信息，因此这些方面的局限性无法从给定材料判断。

### 阅读优先级
高。理由：该论文聚焦动态 3D Gaussian Splatting 压缩这一沉浸式视频通信中的关键问题，所提方法结合稀疏 4D anchors、INR 插值与 memory-based 熵建模，且摘要报告了在 Neu3D 和 MPEG MIV 上相对 GIFStream 的大幅 BD-rate 降低，对神经场景表示、体积视频压缩与渲染效率方向具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation
- 作者：Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang
- 出版日期：2026-09-27T19:48:57Z
- 分类：Neural Scene Representations & Rendering（主分类）；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.33872 ；PDF https://arxiv.org/pdf/2609.33872 ；项目网站 https://robot-gst.github.io

### 一句话总结
Robot-GST 提出一种几何感知的时空行为表示与评估框架，通过 3D Gaussian Splatting 与 SAM3D 构建高斯-SAM 机器人环境进行真机到仿真的策略验证，在动作执行前先仿真评估候选动作序列，以提升长时程操作部署的可靠性。

### 研究问题
机器人操作策略日益依赖视觉语言模型进行端到端决策，但可靠部署仍面临挑战：许多策略缺乏显式机制来预测任务结果，也缺乏评估生成动作能否达成期望最终状态的能力，导致长时程操作中执行误差不断累积。论文试图解决如何在真实执行前对策略生成的动作进行可行性与最终状态评估的问题。

### 核心思路/方法
- 构建几何感知的时空行为表示与评估框架 Robot-GST。
- 基于 RGB-D 观测，利用 3D Gaussian Splatting 与 SAM3D 构建高保真机器人环境，形成 Gaussian-SAM 机器人环境，用于真机到仿真的策略验证，实现“先仿真评估、再执行”。
- 将视觉观测与语言指令结合，借助大型视觉语言模型进行时空推理以支持长时程任务规划。
- 为衔接高层规划与真实执行，引入高斯感知的最终状态估计，通过几何采样与基于状态的轨迹规划实现。
- 在执行前，将候选动作序列放入 Gaussian-SAM 环境中仿真与评估，以过滤不可行的行为。

### 主要贡献
- 提出 Robot-GST 框架，将几何感知的时空行为表示与评估引入机器人操作策略部署流程。
- 构建基于 3D Gaussian Splatting 与 SAM3D 的 Gaussian-SAM 机器人环境，支持从 RGB-D 观测生成高保真仿真环境，实现先评估后执行。
- 引入高斯感知的最终状态估计与基于状态的轨迹规划，连接高层视觉语言规划与真实执行。
- 在涉及刚性、软性和可变形物体的代表性操作任务（包括方块放置、玩具打包、鸭子重排）上进行验证，表明几何感知的时空推理与状态感知执行可提升不同物体类别下的操作可靠性。
- 结果表明，将几何感知重建与高质量渲染和仿真结合，为评估机器人操作行为提供了可扩展的途径。

### 局限性
- 摘要未提供足够信息说明方法在何种硬件平台、实时性、计算开销或大规模场景下的表现。
- 摘要未提供足够信息说明该方法在失败案例、极端物体类别或复杂动态环境中的边界条件。
- 摘要未提供足够信息说明与现有基线方法的定量对比结果及具体评价指标。
- 摘要未提供足够信息说明 Gaussian-SAM 环境构建精度对最终策略执行效果的影响程度。

### 阅读优先级
中。理由：该论文聚焦机器人操作策略的可靠部署与“先仿真评估再执行”的评估框架，结合 3D Gaussian Splatting、SAM3D 与视觉语言模型，主题具有明确的应用价值与交叉性；但摘要仅给出方法概览和任务类别，未提供定量结果、基线对比与实现细节，因此对需要深入评估方法有效性或复现实验的读者而言，需进一步阅读全文才能判断其贡献强度。

</details>

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

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-28 - Terrain-Aware Autonomous Planetary Exploration for Exteroceptive-Proprioceptive Mapping with Quadruped Scouts

**Authors:** Alberto Sanchez-Delgado, João Carlos Virgolino Soares, Victor Barasuol, Claudio Semini
**Links:** [abs](https://arxiv.org/abs/2609.35493) - [pdf](https://arxiv.org/pdf/2609.35493)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Terrain-Aware Autonomous Planetary Exploration for Exteroceptive-Proprioceptive Mapping with Quadruped Scouts
- 作者：Alberto Sanchez-Delgado, João Carlos Virgolino Soares, Victor Barasuol, Claudio Semini
- 出版日期：2026-09-28T16:01:24Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2609.35493) / [PDF](https://arxiv.org/pdf/2609.35493)

### 一句话总结
该论文提出一种面向四足侦察机器人的地形感知自主探索框架，在外星类似月球环境中融合外部感知与本体感知建图，用于规划兼顾碰撞规避与地形交互成本的自主探索与导航。

### 研究问题
论文关注的是自主行星探索场景下，机器人如何在未知、崎岖地形中导航，同时评估风险、可通行性与能量代价。四足侦察机器人适合此类任务，因为其能穿越不规则表面并在运动过程中收集与移动性相关的信息。因此，核心问题是如何将外部感知的几何信息与本体感知的地形交互信息结合，支持自主探索与后续导航。

### 核心思路/方法
论文提出一个地形感知探索框架，结合外部感知与本体感知建图，面向类似月球环境中的四足机器人。具体而言：
- 机载 RGB-D 相机构建以机器人为中心的高程图，估计几何可通行性，并推导用于自主规划的导航代价。
- 本体感知测量提供交互感知的地形线索，补充基于几何的评估。
- 局部地图被增量配准到全局多层表示中，探索模块利用该表示在未探索的兴趣区域中选择目标。
- 自主导航系统利用可用的地图与代价层，引导碰撞感知的运动到达目标。

### 主要贡献
- 提出融合外部感知与本体感知的 terrain-aware 探索框架，用于四足机器人在月球类似环境中的自主探索。
- 构建机器人中心高程图，估计几何可通行性并推导导航代价，同时利用本体感知提供交互感知地形线索。
- 将局部地图增量配准为全局多层表示，并用于在未探索兴趣区域中选择探索目标。
- 在 NVIDIA Isaac Sim 中进行仿真，展示自主探索、地图扩展以及地形几何与机器人—地形交互之间的空间关联。
- 使用该信息进行后续导航时，平均运输成本（Cost of Transport, CoT）低于初始探索阶段。

### 局限性
摘要未提供足够信息说明以下方面：真实世界实验验证情况、不同地形或环境条件下的泛化能力、与已有方法的定量对比、计算资源与实时性表现、失败案例或方法适用边界。因此，无法仅根据摘要评估这些潜在局限。

### 阅读优先级
高。理由：该论文聚焦四足机器人在行星探索中的自主探索与地形感知建图，明确结合外部感知与本体感知，并涉及多层地图、可通行性代价与运输成本等关键机器人自主导航问题；摘要给出了较完整的方法框架与仿真验证结果，对相关方向具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library
- 作者：Youhui Wang, Yunzhu Li, Li Fei-Fei, Jiajun Wu, Huang Huang
- 出版日期：2026-09-28T14:49:06Z
- 分类：Embodied / Robotics / AR Applications（主要分类；次要分类未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.35318) / [PDF](https://arxiv.org/pdf/2609.35318)

### 一句话总结
DexAgent 是一个智能体式的 Human2Sim2Robot 框架，可将单段第一视角人类视频与任务提示转化为物理合理的机器人轨迹，并通过自进化工具库与验证反馈机制支持多样化物体和长时程任务。

### 研究问题
现有的人类到仿真再到机器人（Human2Sim2Robot）流水线依赖预定义流程，难以适应多样化的物体属性和交互方式，尤其是涉及铰接物体和可变形物体的情形。论文旨在解决：如何从单段第一视角人类视频出发，自动生成物理合理、可迁移至真实机器人的灵巧操作轨迹，并应对不同物体属性与长时程任务。

### 核心思路/方法
DexAgent 是一个智能体式框架，输入为单段第一视角人类视频和任务提示，输出为可用于策略训练的、物理合理的机器人轨迹。框架包含四个阶段：
1. 人类视频的语义理解；
2. 基于物体属性的仿真重建；
3. 机器人轨迹优化；
4. 机器人数据生成。

在每个阶段，DexAgent 会根据任务与物体属性，从工具库中选择合适技能，或在需要时开发新技能。属性特定的验证器评估各阶段结果是否满足物理有效性与任务特定要求，并给出反馈用于细化，从而防止错误在工作流中传播。在最后阶段，DexAgent 在仿真中改变物体与机器人状态，从单段人类视频生成多样化机器人轨迹，并对渲染观测进行重纹理化以促进仿真到真实的迁移。新开发的技能与验证器会保留在工具库中，使框架具备自进化能力，可积累可复用能力；随着处理更多人类视频，处理时间会减少。

### 主要贡献
- 提出 DexAgent，一个智能体式 Human2Sim2Robot 框架，将单段第一视角人类视频与任务提示转化为物理合理的机器人轨迹，用于策略训练。
- 设计四阶段流程，并通过属性特定验证器提供反馈与细化，防止错误传播，从而适应多样化物体属性与长时程任务。
- 引入自进化工具库：新技能与验证器可被保留复用，使框架随处理视频增多而减少处理时间。
- 在最后阶段通过变化仿真中的物体与机器人状态生成多样化轨迹，并通过重纹理化渲染观测促进仿真到真实迁移。
- 在十一个真实世界任务中，使用 DexAgent 生成数据训练的策略成功率比竞争基线高 3.5 倍。

### 局限性
摘要未提供足够信息。摘要未提供关于失败案例、计算开销、对特定物体类别或任务类型的适用边界、真实机器人实验设置细节、基线具体构成、验证器设计细节及其可能失效情形等信息。

### 阅读优先级
高。理由：该工作针对灵巧操作中 Human2Sim2Robot 流水线的自适应与可扩展性问题，提出智能体式框架与自进化工具库，并报告了在十一个真实世界任务上相对基线 3.5 倍的成功率提升，主题与具身智能、机器人操作及仿真到真实迁移高度相关，值得优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MarsLab: A Martian Rover Simulator for Planetary Rover Autonomous Navigation
- 作者：Hoyun Kim, Beomsu Kim, Giseop Kim
- 出版日期：2026-09-28T09:18:28Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类为 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2609.34702 ；PDF https://arxiv.org/pdf/2609.34702 ；项目页 https://kimhoyun-robotair.github.io/MarsLab/

### 一句话总结
MarsLab 是一个开源、原生支持 ROS2 的火星车仿真器，基于 NVIDIA Isaac Sim 构建，用于在可配置地形、光照和大气尘埃条件下开发与评测自主导航算法。

### 研究问题
未来火星任务需要火星车在非结构化地形、光照变化、大气尘埃和通信受限条件下具备自主能力。仿真是在部署前研究这些条件的实用手段，但现有与火星相关的资源在范围上各不相同，包括面向任务的仿真器、固定模拟数据集、任务特定环境和开放机器人接口。论文试图在这一背景下提供一个统一、可配置的火星车自主导航仿真平台。

### 核心思路/方法
MarsLab 将源自 HiRISE 的地形与程序化生成地形相结合，并提供可定制的岩石、陨石坑、太阳光照和大气尘埃设置；在 NVIDIA Isaac Sim 中运行一个毅力号级别的火星车模型。运行时通过标准 ROS2 话题发布 RGB、深度、RGB-D 点云、LiDAR、IMU、轮式里程计和 Ground Truth（GT）位姿数据。论文用 SLAM 基准测试演示 MarsLab，覆盖不同传感模态、尘埃水平、场景几何和路线长度；并用 Visual Place Recognition（VPR）基准测试，在光照和尘埃变化下对重复的火星基地穿越进行评测。

### 主要贡献
- 提出 MarsLab：一个开源、ROS2 原生的火星车仿真器，面向自主与导航算法开发。
- 将 HiRISE 派生地形与程序化地形结合，并提供岩石、陨石坑、太阳光照和大气尘埃的可定制设置。
- 在 NVIDIA Isaac Sim 中运行毅力号级火星车模型。
- 通过标准 ROS2 话题发布多种传感与状态数据：RGB、深度、RGB-D 点云、LiDAR、IMU、轮式里程计和 GT 位姿。
- 展示了两类基准测试：跨传感模态、尘埃水平、场景几何和路线长度的 SLAM 基准；以及光照和尘埃变化下重复火星基地穿越的 VPR 基准。
- 结果表明，受控场景变化和共享 GT 轨迹可用于在同一仿真器内比较轨迹级估计与图像级地点识别。

### 局限性
摘要未提供足够信息。摘要未说明仿真到现实的差距、计算资源需求、地形或尘埃模型的真实度验证、基准测试的绝对性能结论、与其他仿真器的定量比较，以及是否支持多火星车或更广泛任务场景等细节。

### 阅读优先级
高。理由：该工作直接面向行星火星车自主导航，提供开源、ROS2 原生且集成 Isaac Sim 的仿真环境，并同时给出 SLAM 与 VPR 基准，对从事行星机器人、自主导航、SLAM 和视觉地点识别的研究者有较强相关性；且论文明确提供项目页，便于进一步获取资源。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：When the Score Becomes the Target: Rethinking Metric Validity in Autonomous Driving
- 作者：Morui Zhu, Deyuan Qu, Qi Chen, Kentaro Oguchi, Qing Yang
- 出版日期：2026-09-28T06:59:37Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.34440

### 一句话总结
论文质疑当自动驾驶评测分数本身成为优化目标时，分数提升是否仍能可靠反映驾驶行为改进，并指出需要同时审查评分过程测量什么以及被优化行为如何被执行。

### 研究问题
驾驶基准分数不仅用于评测，也越来越被当作优化目标。论文提出的核心问题是：一旦分数本身被优化，分数增益是否仍然是驾驶改进的可靠证据。具体关注评分过程如何响应驾驶行为变化，以及这些增益在重复执行和重新规划下是否持续。

### 核心思路/方法
论文将评分过程分解为执行、测量、子分数映射和聚合四个环节。通过受控干预，观察那些在请求运动与执行运动之间被省略、阈值化或衰减的行为区分，是否会带来显著行为变化却只得到很小的分数响应。进一步通过闭环比较，检验当执行接口变化时优化增益是否会发生反转，从而说明增益依赖于请求如何被执行并作为反馈返回。

### 主要贡献
- 提出并检验“分数成为优化目标后，分数增益是否仍可靠”这一问题。
- 将评分过程拆解为执行、测量、子分数映射与聚合，用于分析分数对行为变化的响应机制。
- 通过受控干预揭示行为变化与分数响应之间的脱节，并指出这种脱节源于行为区分在请求与执行之间被省略、阈值化或衰减。
- 通过闭环比较说明优化增益可能在执行接口改变时反转，强调增益的迁移依赖于执行与反馈方式。
- 结论是：在优化条件下讨论度量有效性，需要同时考察评分过程测量什么，以及被优化行为如何被执行。

### 局限性
摘要未提供足够信息说明具体实验平台、数据集、评估指标、干预设计的细节、统计显著性、样本规模以及所涉及的自动驾驶任务范围。摘要也未提供足够信息说明该方法是否在真实车辆或仅仿真环境中验证，以及其结论对其他驾驶基准或评分体系的泛化程度。

### 阅读优先级
中。理由：论文关注自动驾驶基准分数作为优化目标时的度量有效性问题，问题意识明确且具有方法反思价值；但摘要未提供具体实验细节、平台和量化结果，因此对需要直接复用实验结论或工程落地的读者，优先级取决于其是否关心评测方法论与闭环优化可靠性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：UMR: Universal Manipulation Representation
- 作者：Song Liu, Linyi Li, Yanshun Zhao, Rxuan Li, Xinrui Xu, Yi Ju, Yahui Deng, Senge Zhang, Guoyu Liu, Yixuan Li, Wuyang Zhang, Yao Li, Congcong Zhu, Jingrun Chen
- 出版日期：2026-09-28T04:01:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接 https://arxiv.org/abs/2609.34256 ；PDF 链接 https://arxiv.org/pdf/2609.34256 ；项目页面 https://umr-wepvla.github.io/

### 一句话总结
论文提出统一操作表示 UMR，将操作动作分解为世界坐标系下的物体运动（World Flow）与相对当前位姿的末端执行器运动（Ego Trajectory），并实例化为 0.5B 参数的 WEPVLA 策略，实现从人类演示到异构机器人的零样本技能迁移。

### 研究问题
现有策略依赖特定本体的动作空间，导致跨本体演示难以大规模利用，并限制了向新本体和空间变化的迁移。论文试图解决如何在统一动作表示下，使通用具身操作能够跨本体内在泛化并易于扩展。

### 核心思路/方法
UMR 将操作分解为两个功能不同但几何关联的部分：本体无关的 World Flow，描述世界坐标系中任务相关物体运动；Ego Trajectory，表示相对于当前位姿的末端执行器运动。两者通过 \(SE(3)\) 共轭耦合。作者将 UMR 实例化为 WEPVLA，一个 0.5B 参数的紧凑策略，通过双流 Point Action Adapter 和统一 Point Action Expert 在统一几何动作空间中学习。为提升数据效率，提出 Data-Efficient Strategy（DES），通过阶段感知点云编辑丰富物体配置，同时保留演示的接触几何。

### 主要贡献
- 提出统一操作表示 UMR，用于跨本体、可扩展的通用操作动作表示。
- 将 UMR 实例化为 WEPVLA，一个 0.5B 参数策略，采用双流 Point Action Adapter 与统一 Point Action Expert，并通过 \(SE(3)\) 共轭耦合 World Flow 与 Ego Trajectory。
- 提出数据高效策略 DES，通过阶段感知点云编辑多样化物体配置并保留演示接触几何。
- 摘要报告：仿真中 WEPVLA 在 LIBERO 上平均成功率 97.5%，在 10 任务 RLBench 上为 85.7%；真实实验中，仅用人类演示加 DES 增强训练单个策略，每任务约 10 分钟人类演示且无机器人演示，在六种评估设置下平均成功率 91.7%，对比 HumanEgo 为 60.8%。

### 局限性
摘要未提供足够信息。未说明失败案例、跨本体类型范围、真实实验任务数量与具体设置、DES 的适用边界、计算成本、安全性或长期自主性等细节。

### 阅读优先级
高。理由：该论文聚焦具身操作中跨本体统一动作表示这一核心问题，提出明确的两组件分解与可实例化策略，并报告了仿真与真实实验的成功率及零样本迁移结果；若关注 VLA、跨本体迁移或人类演示规模化利用，该工作具有较高相关性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：3D Point Tracking with State Space Models
- 作者：Masahiro Ogawa, Qi An, Atsushi Yamashita
- 出版日期：2026-09-27T23:56:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.34035) / [PDF](https://arxiv.org/pdf/2609.34035)

### 一句话总结
该论文提出一种无位姿、单目、可在单张消费级 GPU 上运行的度量级 3D 点追踪方法，通过冻结的 2D 光流与单目度量深度前端，仅用紧凑状态空间模型学习难以提供的深度残差。

### 研究问题
论文关注动态场景中任意点的度量级 3D 追踪，即输出以绝对米为单位、而非未知尺度下的 3D 位置。作者指出这类能力对 3D/4D 重建、机器人导航和自动驾驶至关重要，因为这些场景的决策依据是米而非像素。目标是在无位姿、单目、单张消费级 GPU 的预算下，实现绝对度量准确的 3D 点追踪。

### 核心思路/方法
方法基于一个观察：一旦某点的 2D 图像轨迹固定，决定其度量精度的量就是沿该像素射线的深度。因此作者不采用端到端学习追踪，而是组合两个冻结前端：用于 2D 对应的稠密光流，以及用于第三维的单目度量深度网络；只学习它们无法提供的残差，即由紧凑状态空间模型（Mamba-3）在 DINOv3 外观特征条件下精化的深度。选择状态空间模型而非最强 3D 追踪器所用的 Transformer，是为了在单 GPU 预算下可行：状态空间模型以固定大小循环状态汇总轨迹，内存开销随帧数恒定，而注意力机制需要随帧数线性增长的键值缓存。在 TAPVid-3D minival 基准上，最佳配置在相同评估条件下取得最高绝对度量精度（平均度量 Average Jaccard 为 0.256），超过强前馈追踪器；论文还包含一项伴随分析，用各竞争者自己的评估器复现，解释为何若干已发表追踪器在该预算下损失大部分精度。

### 主要贡献
- 提出一种无位姿、单目、单张消费级 GPU 的度量级 3D 点追踪方法。
- 观察到 2D 轨迹固定后，度量精度由沿像素射线的深度决定，并据此组合冻结的稠密光流与单目度量深度前端，仅学习深度残差。
- 使用紧凑状态空间模型（Mamba-3）并在 DINOv3 外观特征条件下精化深度，以获得随帧数恒定的内存开销。
- 在 TAPVid-3D minival 上，最佳配置取得相同条件下最高绝对度量精度，平均度量 Average Jaccard 为 0.256。
- 提供伴随分析，用各竞争者自己的评估器解释为何若干已发表追踪器在该预算下损失大部分精度。

### 局限性
摘要未提供足够信息。摘要未提供关于方法失败案例、泛化能力、计算开销具体数值、不同数据集表现、消融实验细节或实际部署限制的充分信息。

### 阅读优先级
高。理由：该论文针对度量级 3D 点追踪这一对机器人、自动驾驶和 3D/4D 重建重要的任务，提出在单张消费级 GPU、无位姿、单目预算下的方案，并在 TAPVid-3D minival 上报告了相同条件下最高的绝对度量精度；其冻结前端加状态空间模型的设计思路和伴随分析也具有较强参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：DexTaG: Tactile-as-Guidance in Reinforcement Learning for Dexterous Manipulation
- 作者：Han Yang, Yian Wang, Yunlong Song, Zhenjia Xu, Chuang Gan
- 出版日期：2026-09-27T19:56:41Z
- 分类：Embodied / Robotics / AR Applications
- 链接：abstract_url: https://arxiv.org/abs/2609.33882；pdf_url: https://arxiv.org/pdf/2609.33882

### 一句话总结
DexTaG 提出一种以触觉信号为引导的强化学习框架，利用手套采集的人类接触模式指导灵巧手操作策略学习，并通过统一重定向器与蒸馏学生控制器提升效率与真实世界部署能力。

### 研究问题
基于手套的动作捕捉虽可规模化采集灵巧手演示数据，但由于人手与机器人手之间的运动学差异，记录的人类动作无法直接迁移到机器人上，尤其在涉及手内重定向的富接触工具使用任务中更为困难。已有工作通过强化学习或轨迹优化在仿真中弥合差距，但难以保留人类接触模式，常导致不自然操作和不稳定的功能性抓取；同时这些方法通常为每条参考轨迹单独训练策略或求解优化，效率较低。

### 核心思路/方法
DexTaG 是一个触觉引导的强化学习框架，用于灵巧操作。训练过程中，由手套采集的触觉信号引导策略搜索朝向测量到的人类接触模式，从而减少接触监督对精确参考几何的依赖。为提升效率，方法对同一物体的所有训练轨迹联合训练一个可泛化的重定向器；该重定向器进一步蒸馏为一个无触觉的学生控制器，并以目标物体轨迹为条件，用于真实世界部署。

### 主要贡献
- 提出使用触觉信号作为强化学习中的引导，使策略搜索趋向人类接触模式，降低对精确参考几何进行接触监督的依赖。
- 针对同一物体的所有训练轨迹联合训练一个可泛化的重定向器，而非为每条参考轨迹单独训练策略或求解优化，以提升效率。
- 将重定向器蒸馏为无触觉的学生控制器，并以目标物体轨迹为条件，面向真实世界部署。
- 在 marker-pen 和 hammer 操作任务上，DexTaG 学到自然、富接触的行为，而基于距离的接触启发式基线无法学到这些行为；方法能泛化到同一物体与任务的留出轨迹，并在 OakInk2 上优于单轨迹基线。

### 局限性
摘要未提供足够信息说明方法的失败案例、对触觉手套数据质量或标定的敏感性、真实世界部署的具体限制、计算成本细节，以及在更多物体类别或更复杂任务上的泛化边界。摘要也未提供足够信息说明学生控制器在真实世界中的定量表现与安全性评估。

### 阅读优先级
高。理由：该论文聚焦于灵巧手操作中人类演示到机器人迁移的关键难题，提出触觉引导强化学习与统一重定向器及无触觉蒸馏部署路径，问题重要且方法具有明确的新意；摘要已报告在具体工具使用任务上优于基线，适合关注机器人学习、灵巧操作和触觉引导策略的研究者优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：SLIP-VLA: Single-Step Latent Imagination for Policy Learning in Vision-Language-Action Models
- 作者：Tianfu Li, Haoxuan Xu, Wenbo Chen, Haitian Li, Changchuan Yang, Xinhu Zheng, Jun Ma, Yuan Liu, Lujia Wang, Haoang Li
- 出版日期：2026-09-27T13:53:29Z
- 分类：Embodied / Robotics / AR Applications（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2609.33575) / [PDF](https://arxiv.org/pdf/2609.33575)

### 一句话总结
SLIP-VLA 通过单步去噪在潜空间中生成时间稠密的未来表示，并结合几何/语义对齐与动作条件世界建模，实现高效且高性能的未来感知动作预测。

### 研究问题
现有 Vision-Language-Action（VLA）模型大多直接从当前观测预测动作，未显式建模未来场景演化。引入未来预测的方法中，稠密未来建模往往依赖昂贵的迭代去噪，而单步替代方案的表现又可能弱于多步版本。因此核心问题是如何在高效未来建模与强动作性能之间取得平衡。

### 核心思路/方法
- 提出 SLIP-VLA 策略学习框架，为 VLA 模型配备“单步潜想象（Single-Step Latent Imagination）”以实现未来感知的动作预测。
- 通过单次去噪更新获得时间稠密的未来潜表示。
- 将中间潜表示与未来几何和语义特征对齐，以提升其感知充分性。
- 通过动作条件潜世界建模与逆动力学建模，将潜状态转移与机器人动作显式耦合，以提升其控制充分性。

### 主要贡献
- 提出 SLIP-VLA，一种面向 VLA 的单步潜想象策略学习框架。
- 在单步去噪条件下获得时间稠密的未来潜表示。
- 通过几何/语义对齐提升潜表示的感知充分性，通过动作条件世界建模与逆动力学建模提升控制充分性。
- 在多种仿真基准和真实世界操作任务上取得 state-of-the-art 性能，单步潜想象耗时仅 12 ms。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体适用边界、失败场景、对特定任务类型的依赖、计算资源需求或与基线方法的详细对比条件，也未提及消融实验或误差分析。

### 阅读优先级
中。理由：该论文针对 VLA 中未来建模效率与性能的权衡问题提出明确的单步方案，并报告了 12 ms 的推理开销与多基准 state-of-the-art 结果，对机器人操作与具身智能方向有直接参考价值；但摘要未提供具体实验设置、基线细节和开源信息，是否高优先级需进一步阅读正文确认。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：SceneScaffold: Active Scene-State Construction for Unified 3D Scene Understanding
- 作者：Xiangqi Li, Libo Huang, Jiarui Zhao, Weilun Feng, Chuanguang Yang, Zhulin An, Yongjun Xu
- 出版日期：2026-09-27T12:39:53Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.33518 ；PDF https://arxiv.org/pdf/2609.33518 ；代码 https://github.com/lixiangqi707/SceneScaffold

### 一句话总结
SceneScaffold 将 3D 大 multimodal 模型中的视觉瓶颈从被动特征压缩器重构为主动场景组织器，通过构建角色感知的空间脚手架来改善统一 3D 场景理解中的空间关系推理。

### 研究问题
论文关注的是当前 3D 大 multimodal 模型（3D-LMMs）中视觉瓶颈的局限：它通常将异构的 3D 场景证据被动压缩为同质的、以对象为中心的统一 token 序列，导致场景的空间组织信息表达不足。这种不足迫使 LLM 从被“压平”的 token 序列中恢复空间关系，从而在关系密集和空间模糊的场景中产生不稳定的推理。

### 核心思路/方法
SceneScaffold 提出一种主动场景状态构建框架，用于统一 3D 场景理解。其核心是将视觉瓶颈从被动特征压缩器转变为主动场景组织器，在语言推理之前构建角色感知的空间脚手架。

具体而言，SceneScaffold 将 superpoint 级别的视觉证据组织为具有不同结构角色的场景状态组件：
- 实体状态（entity states）：保留核心对象语义；
- 场景框架状态（scene-frame states）：通过边界和区域锚点维持空间参考；
- 关系状态（relation states）：编码对象与环境的交互线索；
- 全局摘要（global summary）：提供紧凑上下文。

通过这种角色感知的构建方式，SceneScaffold 在语言推理之前为 LLM 提供空间上已组织的场景表示。

### 主要贡献
- 提出 SceneScaffold，将 3D-LMM 中的视觉瓶颈从被动压缩器重新定义为主动场景组织器。
- 设计角色感知的空间脚手架，包含实体状态、场景框架状态、关系状态和全局摘要，以显式表达场景空间组织。
- 在统一 3D 场景理解任务上进行实验，包括 3D 视觉定位、问答和密集描述，证明方法有效性；诊断结果进一步显示其对关系密集和空间模糊场景的适用性。
- 提供代码链接。

### 局限性
摘要未提供足够信息。论文未在摘要中说明具体实验设置、数据集规模、模型规模、计算开销、失败案例或与其他方法的完整对比细节，因此无法仅基于摘要评估其泛化性、效率或潜在限制。

### 阅读优先级
中。理由：该论文针对 3D-LMM 中视觉瓶颈导致空间组织信息不足这一明确问题，提出结构化的角色感知场景状态构建方法，并覆盖 3D 视觉定位、问答和密集描述等统一 3D 场景理解任务，对具身智能、机器人及 AR 应用方向有一定相关性。但摘要未提供足够的实验细节、定量结果和局限讨论，是否值得深入阅读取决于读者对 3D 场景表示、视觉瓶颈设计或多模态 LLM 空间推理的具体兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Scanning While Imagining: A Scene-Graph World Model for Robotic Ultrasound Navigation
- 作者：Xuesong Li, Shuai Chen, Feng Li, Zhongliang Jiang, Nassir Navab, Yuan Bi
- 出版日期：2026-09-26T18:10:52Z
- 分类：主分类：Embodied / Robotics / AR Applications；次分类：摘要未提供
- 链接：摘要链接 https://arxiv.org/abs/2609.32837 ；PDF 链接 https://arxiv.org/pdf/2609.32837 ；项目页 https://noseefood.github.io/us-sonograph-wm/

### 一句话总结
论文提出 SonoGraph-WM——一种以场景图表示解剖结构、联合预测未来场景图与探头位姿的动作与目标条件世界模型，用于机器人超声导航中的前瞻性探头规划。

### 研究问题
超声采集依赖操作者解读解剖结构并预判探头运动将如何改变视图，但许多机器人超声导航方法在选择动作时并未显式预测这些解剖变化。论文关注的问题是：如何在不合成超声图像的前提下，让机器人导航方法能够预测解剖结构随探头运动的演变，并据此规划到达目标视图的路径。

### 核心思路/方法
- 提出 SonoGraph-WM，一个动作与目标条件化的世界模型，用于前瞻性探头导航。
- 以场景图（SG）表示解剖结构，捕捉可见结构、其几何以及空间关系，而不合成超声图像。
- 给定场景图历史与探头位姿，使用统一 Transformer 联合预测未来场景图与位姿。
- 采用滚动时域规划器：递归想象候选轨迹，选择到达目标图的最短预测路径，并在短执行时域内跟随该路径，随后基于新观测重新规划。
- 为减少对带追踪和解剖标注的超声序列的依赖，从计算机断层扫描（CT）标签图沿表面约束的探头轨迹生成对齐的场景图—位姿训练数据。

### 主要贡献
- 提出以场景图为核心、避免超声图像合成的解剖世界模型，用于机器人超声探头导航。
- 设计统一 Transformer 联合预测未来场景图与探头位姿，并配合滚动时域规划器实现目标条件化导航。
- 提出基于 CT 标签图沿表面约束轨迹生成对齐场景图—位姿训练数据的方案，以降低对带标注超声序列的依赖。
- 在四个留出 CT 病例上报告：20 个预测步内空间关系 F1 保持 93% 以上；使用标注导出的场景图时，闭环导航在胆囊和胰腺上分别达到 77.50% 与 75.00% 成功率。
- 在机器人—体模导航实验中，使用标签图导出的场景图，规划器在 73.7% 的试验中到达目标视图。

### 局限性
- 摘要提到需要频繁观测更新以保证可靠导航，暗示对观测更新频率存在依赖。
- 摘要未提供足够信息说明方法在真实临床超声场景、不同解剖变异或不同操作者条件下的泛化能力。
- 摘要未提供足够信息说明 CT 监督数据生成流程对真实超声域差异的鲁棒性细节。
- 摘要未提供足够信息说明失败案例的具体模式、计算开销或实时性表现。

### 阅读优先级
高。理由：该论文聚焦机器人超声导航中的前瞻性解剖预测与世界模型，任务明确、方法描述具体，并给出了预测精度与闭环导航成功率的量化结果，对具身机器人、医学机器人与超声导航方向具有直接参考价值。

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
