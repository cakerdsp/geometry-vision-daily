# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：56
- 分类分布：
  - Neural Scene Representations & Rendering: 18
  - 3D Reconstruction & Multi-view Geometry: 15
  - Embodied / Robotics / AR Applications: 11
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 6
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“前馈几何基础模型 + 轻量后端优化/适配”成为长时序与大场景重建的主流范式。**  
   HiP3R 不重新训练前馈模型，而是在分块短窗口结果之上构建分层位姿图（块级 Sim(3) 管全局布局与尺度，帧级共享 SE(3) 管局部一致）；Stream4D 同样不训练，直接复用因果 Transformer 主干的 KV 缓存做运动解耦。两者都在回答同一个问题：前馈模型能力已足够，瓶颈转移到了“如何在不重训的情况下拼接、校正、传播约束”。

2. **相机/成像模型假设正在被显式放宽，“任意几何”成为单目重建的新默认需求。**  
   OmniRay 针对鱼眼、全景等非针孔成像，把射线场拆成单调径向基 + 球谐残差 + 自由形式残差的分层表示，推理时不需要相机参数；WildDepth-v2 与月球 Visual SLAM 评测则从数据与基准侧指出，真实传感器（雷达、LiDAR、低纹理强光照）与理想针孔假设之间的落差是实际部署的主要障碍。这一线索表明“相机无关”正从口号变成可建模的设计目标。

3. **多视图上下文从“成对匹配”走向“一次性联合推理”，并开始复用冻结几何基础模型。**  
   MVLoMa 把匹配从图像对扩展为中心—多邻居星形图，用冻结的多视图几何模型（DA3、π³、VGGT 系列）提供跨视角几何上下文，一次前向完成全部邻边匹配；WovenAnchor Matcher 则从算子层面区分为图内（WovenMamba 结构化二维传播）与图间（AnchorCrossAttention 局部锚点交叉注意力）两种聚合角色。这说明匹配研究的重心从“更好的描述子”转向“更好的上下文聚合结构与基础模型复用方式”。

4. **动态/4D 与语义理解在 3DGS 与流式重建上交汇，且普遍强调“免训练/免场景特定优化”。**  
   Stream4D 用动态掩码抑制动态区域对因果注意力的干扰；R4DGS 把语言指代引入 4DGS 并配套 R4D-Bench-QA；RecallGS 用“检索历史观测”替代“额外学习 3D 网络”来补几何—语义证据；ClunoGS 则从压缩角度指出语义重要的高斯不能被纯渲染导向的剪枝删掉。共同信号：语义与动态不再作为后处理插件，而是被纳入重建/表示的主目标函数。

5. **机器人侧从“策略学习”转向“世界模型 + 记忆 + 结构化动作分解”，并配以新基准。**  
   SkeLAM 把潜在动作分解为骨架监督的运动学分量与残差分量；软衣物操作论文用 Transformer 世界模型从部分点云历史做上下文学习；WholeBodyMem 提出对象引导的预历史记忆并发布 HuMeGo 人形记忆基准；动作重定向 STR 用 VLM 选取关键帧与关键身体部位来分配优化预算。这些工作共同显示：机器人方向的瓶颈正从“能否执行”转向“如何在部分观测、非马尔可夫、跨具身条件下保持可控与可解释”。

---

#### 技术路线观察

**几何基础模型方向：从“用模型”到“改造模型的使用方式”。**  
MVLoMa、DewHand、WildDepth-v2 都建立在冻结或预训练的几何基础模型之上（VGGT、VGGT-Ω、DA3、π³）。区别在于：MVLoMa 把基础模型当作跨视角上下文注入器，重点在匹配头的结构设计；DewHand 把场景级几何特征与手部特定特征分工，用 flow matching 处理遮挡下的多模态不确定性；WildDepth-v2 则把基础模型能力放到新传感器（成像雷达）与新评测协议下检验。这条路线共同的隐含判断是：几何基础模型的表征已足够通用，创新点在于如何按任务解耦其输出、如何构造监督与评测。

**3D/4D 重建方向：一致性与动态性是两个独立但耦合的战场。**  
长时序一致性（HiP3R）与动态解耦（Stream4D、R4DGS）表面上是两个问题，但都指向“分块/流式处理导致的坐标帧与语义帧不一致”。HiP3R 用分层图优化处理几何一致性，Stream4D 用注意力缓存中的时序线索处理运动一致性，二者可以组合：前者管全局尺度与回环，后者管局部动态区域抑制。值得注意的是，两类方法都明确选择“免训练”路线，说明该方向当前的算力与工程成本约束很强。

**神经场景表示方向：语义、光照、压缩三条支线同时成熟。**  
3DGS 相关论文（RecallGS、ClunoGS、GSHeadRelight、H-2DGS、SplatLab、R4DGS）覆盖了语义增强、存储压缩、可重光照、医学表面重建、自动化研究流程和 4D 指代分割。技术侧重点分化明显：RecallGS 与 ClunoGS 都在对抗“语义属性带来的额外成本”，前者用检索替代学习，后者用统一约束目标替代顺序剪枝+量化；GSHeadRelight 用线性响应的神经辐射传输表示换取重光照速度；H-2DGS 用高度场 + TSDF 换取有限视角下的几何锐利度。共性是把 3DGS 从“渲染表示”推向“可查询、可压缩、可物理组合的场景接口”。

**机器人/AR 应用方向：记忆、分解、重定向三条工程化路线。**  
WholeBodyMem 解决“线索消失”的非马尔可夫性，SkeLAM 解决“潜在动作与控制不对应”，STR 解决“统一迭代预算浪费在非关键帧”。三者分别对应感知记忆、动作表征、优化资源分配三个层面，但都依赖一个外部结构化信号（SAM3 跟踪、机器人骨架、VLM 选帧）来约束学习或优化过程。这说明在真实机器人数据稀缺的前提下，“用结构化先验替代大规模标注”是当前最现实的路线。

---

#### 值得优先阅读的论文

1. **HiP3R（2610.31635）**  
   理由：它给出了长时序重建中“块级 Sim(3) + 帧级 SE(3)”这一清晰的分层设计，且不依赖额外训练，工程可复现性高。对任何做流式/分块重建的工作，其位姿图层级选择的分析几乎是必读的对照框架。

2. **OmniRay（2610.31645）**  
   理由：把“相机几何的层次复杂性”显式建模为径向基 + 球谐 + 自由残差的复合射线场，是相机无关重建中少见的、有明确归纳偏置的设计。对广角/鱼眼/全景单目重建和 NeRF/3DGS 的射线参数化都有直接借鉴价值。

3. **Stream4D（2610.31320）**  
   理由：核心观察“因果注意力 KV 缓存隐式编码时序运动线索”具有很强的可迁移性，且方法免训练、可插入 StreamVGGT/Stream3R。若关注动态场景下的流式重建与位姿漂移，这是最直接的起点。

4. **MVLoMa（2610.31321）**  
   理由：它同时示范了“把匹配从对扩展到星形图”和“复用任意冻结多视图几何基础模型”两件事，并在四种编码器上做了消融。对 SfM、视觉定位、以及任何需要一图对多图匹配的下游任务都有参考意义。

5. **R4DGS（2610.30326）**  
   理由：它把一个相对空白的任务（4D 动态场景中的语言指代分割）连同基准 R4D-Bench-QA 一起提出，并给出统一框架。若关注 4DGS 的语义接口或动态场景的开放词汇理解，这是定义问题边界的论文。

（若阅读预算更偏机器人侧，可用 WholeBodyMem（2610.31166）替换第 5 篇：其 HuMeGo 基准与“保留正确帧而非更多帧”的

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-27T13:58:35-04:00
**Total number of papers:** 62
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

### 2026-10

#### 2026-10-26 - Does VGGT Know What It Does Not Know?

**Authors:** Adityan Thirumani Srinivasan, David Nordström
**Links:** [abs](https://arxiv.org/abs/2610.35806) - [pdf](https://arxiv.org/pdf/2610.35806)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, point map, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models such as VGGT regress cameras and geometry in a single forward pass, but they report no uncertainty for the camera poses they predict: an incorrect relative pose looks no different from a correct one. We ask whether the frozen model nonetheless knows when its pose is wrong. On HardMatch, a benchmark of 1,000 deliberately difficult image pairs on which VGGT fails on 35% of pairs, a linear probe on VGGT's frozen features predicts pose failure on held-out categories with ROC-AUC 93.5%, compared with 79.7% for VGGT's own point-map confidence and 77.7% for a classifier trained on all of VGGT's outputs. The probe catches failures VGGT is confident about, lets a downstream system abstain on the pairs it distrusts, and transfers without retraining to rotation failures on PhotoTourism and ScanNet-1500, beyond what co-visibility explains. This knowledge is absent from the per-image encoder: it is computed partway through the layers that fuse the two views, and the same holds for a second model, $π^3$. In essence, we find that VGGT knows more about its own failures than it reports.

</details>

#### 2026-10-26 - PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry

**Authors:** Yihang Chen, Bin Tan, Yujun Shen, Yinghao Xu, Nan Xue
**Links:** [abs](https://arxiv.org/abs/2610.34845) - [pdf](https://arxiv.org/pdf/2610.34845)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, DUSt3R, 3D reconstruction, SfM, SLAM, pose estimation

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
<summary>Abstract</summary>

Camera motion recognition requires separating viewpoint changes caused by camera translation, rotation, or zoom from object motion and scene dynamics. Video-language models often rely on semantic cues and struggle with the geometric evidence needed for this task. Joint-Embedding Predictive Architectures such as V-JEPA offer strong spatio-temporal representations, but our experiments suggest that they underrepresent geometric cues in some regions. Under temporal-reversal supervision, V-JEPA improves overall but degrades on several motion families, whereas a weaker geometry-oriented VGGT predictor improves across all families. We refer to these geometrically underrepresented regions as geometric blind spots and propose Fovea-JEPA to identify and address them. Using V-JEPA as the base model and VGGT as a geometry expert, we construct intervention pseudo-labels from their prediction errors to weakly supervise a blind-spot predictor. The predictor produces token-wise response maps, which are aggregated into a clip-level intervention score to guide adaptive fusion of visual and geometric features. This selective intervention introduces complementary geometric information while preserving reliable visual predictions. Experiments on CameraMotionDataset, CameraBench, and ShotBench demonstrate the effectiveness of Fovea-JEPA, with gains of 9.67, 8.67, and 24.38 percentage points over previously reported state-of-the-art baselines, respectively. Code and models will be released upon acceptance.

</details>

#### 2026-10-22 - MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model

**Authors:** Xinyang Lu, Shengzhe Wei, Sheng Tang, Weiqi Zhang, Juntong Fang, Zesong Li
**Links:** [abs](https://arxiv.org/abs/2610.31321) - [pdf](https://arxiv.org/pdf/2610.31321)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** geometry foundation model, VGGT, structure from motion, feature matching, NeRF, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model
- 作者：Xinyang Lu, Shengzhe Wei, Sheng Tang, Weiqi Zhang, Juntong Fang, Zesong Li
- 出版日期：2026-10-22T14:12:02Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.31321) / [PDF](https://arxiv.org/pdf/2610.31321)

### 一句话总结
MVLoMa 将稀疏局部特征匹配从图像对扩展到以中心图像和多个邻域图像构成的星形图，并借助冻结的多视图几何基础模型注入跨视角几何上下文，实现一次前向完成中心图像与所有邻域图像的匹配。

### 研究问题
论文指出，局部特征匹配通常按图像对建模，但 structure-from-motion 和视觉定位常需要将一幅参考图像与多个检索或共视邻域图像匹配。若独立地对每条中心—邻域边运行成对匹配器，会重复参考侧计算，且无法利用其余观测提供的互补多视图几何证据。

### 核心思路/方法
- 提出 MVLoMa，一种稀疏星形图匹配器，将 LoMa 从图像对扩展到多视图。
- 首先使用冻结的多视图几何模型联合描述星形图中的所有图像，并将得到的跨视角几何上下文注入局部描述子。
- 随后通过逐视图自注意力和双向中心—邻域交叉注意力，在一次前向中完成中心图像与所有邻域图像的匹配。
- 监督方面，仅从深度有效且相互可见的稠密 warp 中推导正对应，并显式惩罚违反极几何的高置信匹配。
- 摘要称同一设计支持四种冻结几何编码器：DA3、$π^3$、VGGT 和 VGGT-$Ω$；其中 DA3-Giant 在所有报告的编码器消融指标上表现最好。

### 主要贡献
- 将稀疏局部特征匹配从成对形式扩展到多视图星形图形式，减少中心—邻域边逐对独立匹配的重复计算。
- 利用冻结的多视图几何基础模型为局部描述子提供跨视角几何上下文。
- 设计一次前向的多视图匹配机制，结合逐视图自注意力与双向中心—邻域交叉注意力。
- 提出基于深度有效、相互可见稠密 warp 的正对应监督，并加入违反极几何的负监督。
- 摘要报告在 HyperSim、ScanNet++、Mip-NeRF 360 和 Tanks and Temples 的 25 视图星形图上，三个阈值下的 macro-average relative-pose AUC 均为 58.65/85.41/90.99，且匹配器比顺序评估 24 条中心—邻域边快 2.20 倍。
- 通过受控消融隔离几何感知描述子、可见性过滤、几何负监督和联合多视图推理的作用。

### 局限性
- 摘要未提供足够信息说明方法在非星形图结构、动态场景或大规模视图数量下的表现。
- 摘要未提供足够信息说明对几何基础模型冻结权重的依赖程度、推理显存开销及失败案例。
- 摘要未提供足够信息给出完整实验设置、数据集划分、基线细节和消融的具体数值。
- 摘要未提供足够信息讨论实际部署中的鲁棒性、实时性边界和泛化范围。

### 阅读优先级
高。理由：该论文直接针对多视图局部特征匹配中的重复计算与多视图几何证据利用问题，问题定义清晰；摘要给出了明确的速度提升和位姿 AUC 结果，并涉及多种冻结几何基础模型的适配与消融，对 3D 重建、视觉定位和多视图几何方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Local feature matching is typically formulated for image pairs, although structure-from-motion and visual localization commonly match one reference image against many retrieved or covisible neighbours. Applying a pairwise matcher independently to these centre-neighbour edges duplicates reference-side computation and prevents the matcher from exploiting complementary multi-view geometric evidence from the remaining observations. To address these limitations, we introduce MVLoMa, a sparse star-graph matcher that extends LoMa from image pairs to multiple views. MVLoMa first uses a frozen multi-view geometry model to jointly describe all images in a star, then injects the resulting cross-view geometric context into local descriptors. It then matches the centre image to all neighbours in a single forward pass through per-view self-attention and bidirectional centre-neighbour cross-attention. For supervision, we derive positive correspondences only from depth-valid, mutually visible dense warps and explicitly penalize high-confidence matches that violate epipolar geometry. On 25-view star graphs from HyperSim, ScanNet++, Mip-NeRF 360, and Tanks and Temples, MVLoMa obtains the best macro-average relative-pose AUC among the compared methods at all three thresholds (58.65/85.41/90.99). Its matcher is 2.20 times faster than sequential evaluation of the 24 centre-neighbour edges. The same design supports four tested frozen geometry encoders -- DA3, $π^3$, VGGT, and VGGT-$Ω$ -- with DA3-Giant performing best on all reported encoder-ablation metrics. Controlled ablations further isolate the effects of geometry-aware descriptors, visibility filtering, geometric negative supervision, and joint multi-view inference.

</details>

#### 2026-10-22 - WildDepth-v2: A Synchronized RGB--LiDAR--Radar Dataset and Benchmark for Metric Depth, Motion, and Tracking of Wildlife

**Authors:** Muhammad Aamir, Sangyun Shin, Naoya Muramatsu, Matthew Wijers, Amir Patel, Andrew Loveridge, Andrew Markham
**Links:** [abs](https://arxiv.org/abs/2610.31123) - [pdf](https://arxiv.org/pdf/2610.31123)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** metric depth, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WildDepth-v2: A Synchronized RGB--LiDAR--Radar Dataset and Benchmark for Metric Depth, Motion, and Tracking of Wildlife
- 作者：Muhammad Aamir, Sangyun Shin, Naoya Muramatsu, Matthew Wijers, Amir Patel, Andrew Loveridge, Andrew Markham
- 出版日期：2026-10-22T11:40:54Z
- 分类：主分类 Geometry Foundation Models；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.31123) / [PDF](https://arxiv.org/pdf/2610.31123)

### 一句话总结
论文发布 WildDepth-v2 数据集，在同步 RGB--LiDAR 野生动物数据基础上加入成像雷达，并提供用于度量深度、运动与跟踪的基准与评测。

### 研究问题
摘要指出，野生动物距离与运动（以米制单位）的测量是丰度估计、形态测量和运动生态学的基础；但单目视频缺乏度量尺度，现有野生动物数据集也缺乏度量真值。论文在此基础上进一步关注：如何利用雷达与 LiDAR 等信息提升野生动物度量距离、深度补全、3D 轨迹与运动分析的精度。

### 核心思路/方法
- **数据扩展**：在同步 RGB--LiDAR 的 WildDepth 数据集基础上，新增 37 个 RGB--LiDAR--4D 雷达序列（19,716 帧），包含逐点多普勒速度与测量误差预算，摘要称其为首批成像雷达野生动物记录。
- **基准评测**：构建冻结、带校验和的隐藏测试集，用于 RGB-only 距离估计与 RGB+稀疏 LiDAR 深度补全，并分别在动物像素与背景像素上评估。
- **运动与跟踪**：利用 LiDAR、雷达或单目深度将 2D 轨迹提升为度量 3D 轨迹，比较不同标定与提升方式的效果。

### 主要贡献
- 发布带成像雷达的同步 RGB--LiDAR--4D 雷达野生动物数据集，包含逐点多普勒速度与测量误差预算。
- 提供隐藏测试集与评测设置，覆盖 RGB-only 距离估计和 RGB+稀疏 LiDAR 深度补全，并区分动物与背景像素。
- 在 48,723 个动物帧上表明：对象级雷达标定可改善单目深度（AbsRel 0.120 对场景级 LiDAR 标定的 0.198），且推理时无需 LiDAR；但动物级 LiDAR 标定仍更准确（0.052）。
- 在 431 条轨迹上表明：每条轨迹一次的雷达缩放可将 3D 位置误差从 2.20 m 降至 0.58 m（约四倍），并将距离采样检测函数偏差从 -13% 降至 -2%，与每条轨迹一次的 LiDAR 标定相当。
- 将雷达多普勒迁移到 LiDAR 可生成更密集的运动掩码（密度为单独雷达的 3.7 倍，精度 72%），降低运动动物 LiDAR 累积误差 37%，并估计径向速度（r = 0.60），但存在约 50% 低估。

### 局限性
- 摘要明确给出部分方法仍存在误差：雷达迁移运动掩码精度为 72%；径向速度估计虽相关（r = 0.60）但约低估 50%；对象级雷达标定的单目深度精度仍低于动物级 LiDAR 标定。
- 关于数据采集地点、物种范围、传感器具体型号、标注协议、计算成本、泛化到其他物种或环境的表现等，**摘要未提供足够信息**。

### 阅读优先级
**中**。理由：论文涉及野生动物度量深度、3D 跟踪与 RGB--LiDAR--雷达多模态数据，且提供隐藏测试集与多项定量基准；若关注多模态深度估计、雷达辅助标定或生态监测中的度量视觉，具有参考价值。但摘要未提供数据规模之外的采集细节与泛化评估，是否高优先级取决于读者对野生动物场景或多模态基准的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Measuring animal distance and motion in metric units underpins abundance estimation, morphometrics, and movement ecology, yet monocular video lacks metric scale and wildlife datasets lack metric ground truth. We present WildDepth 2, extending the synchronized RGB-LiDAR WildDepth dataset in three directions. (i) Imaging radar: 37 RGB-LiDAR-4D-radar sequences (19,716 frames) with per-point Doppler velocity and a measured error budget, to our knowledge the first imaging-radar wildlife recordings. (ii) Benchmarking: a frozen, checksummed hidden test set for RGB-only distance estimation and RGB+sparse-LiDAR depth completion, evaluated separately on animal and background pixels. (iii) Motion and tracking: metric 3D trajectories obtained by lifting 2D tracks using LiDAR, radar, or monocular depth. Across 48,723 animal frames, object-level radar calibration improves monocular depth over scene-level LiDAR calibration without requiring LiDAR at inference (AbsRel 0.120 vs. 0.198), although animal-level LiDAR remains more accurate (0.052). Across 431 tracks, once-per-track radar scaling reduces 3D position error four-fold (2.20 to 0.58 m) and distance-sampling detection-function bias from -13% to -2%, matching once-per-track LiDAR calibration. Transferring radar Doppler onto LiDAR produces motion masks 3.7 times denser than radar alone at 72% precision, reduces moving-animal LiDAR accumulation error by 37%, and estimates radial speed (r = 0.60), albeit with approximately 50% underestimation.

</details>

#### 2026-10-21 - DewHand: Direct Metric World-Space Hand Motion Reconstruction from Egocentric Videos

**Authors:** Naru Suzuki, Satoshi Ikehata, Takehiko Ohkawa, Yoichi Sato, Shuhei Kurita
**Links:** [abs](https://arxiv.org/abs/2610.29936) - [pdf](https://arxiv.org/pdf/2610.29936)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Dynamic / 4D Reconstruction
**Matched keywords:** VGGT, motion reconstruction, motion trajectories, SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DewHand: Direct Metric World-Space Hand Motion Reconstruction from Egocentric Videos
- 作者：Naru Suzuki, Satoshi Ikehata, Takehiko Ohkawa, Yoichi Sato, Shuhei Kurita
- 出版日期：2026-10-21T16:08:38Z
- 分类：主分类 Geometry Foundation Models；次分类 Dynamic / 4D Reconstruction
- 链接：abstract_url: https://arxiv.org/abs/2610.29936；pdf_url: https://arxiv.org/pdf/2610.29936

### 一句话总结
DewHand 提出一个单阶段统一模型，从第一视角视频直接联合重建世界坐标系中的手部与相机运动，并借助场景几何特征、度量监督与流匹配生成式建模应对尺度歧义及遮挡/出视野问题。

### 研究问题
论文关注从第一视角视频恢复度量世界空间中的手部运动，以支持理解人类交互并迁移到具身智能体。摘要指出三项挑战：
1. 多阶段流程会传播来自独立估计的手部运动与相机运动的误差；
2. 单目观测导致物理尺度歧义；
3. 遮挡与手部出视野会带来多种可能运动轨迹。
摘要还指出，该任务需要同时处理手部运动、相机运动、尺度以及遮挡/出视野下的不确定性。

### 核心思路/方法
- 采用单阶段统一模型，在共享世界坐标系中联合预测手部运动与相机运动，以避免多阶段估计的误差累积。
- 为缓解度量尺度歧义，结合来自 VGGT-$Ω$ 的场景级几何特征与度量空间监督；同时使用手部特定特征保留细粒度关节运动。
- 将重建表述为带 flow matching 的条件运动生成，以处理遮挡和出视野手部；摘要称在同一架构下，该生成式形式仅用两步采样即在准确性和时间平滑性上优于直接回归。
- 摘要提到在 HOT3D 与 ARCTIC 上实验，并报告相对 StableHand 的刚性对齐世界空间误差从 32.9 mm 降至 28.4 mm（HOT3D），从 76.2 mm 降至 36.2 mm（ARCTIC）；在 HOT3D 上三分之二片段相机尺度恢复误差在 10% 以内，而 SLAM 约为四分之一。零样本评估在 HoloAssist、H2O、TACO 上均取得最低刚性对齐世界空间误差（WA-MPJPE）。

### 主要贡献
- 提出 DewHand，一个用于从第一视角视频直接联合重建世界空间手部与相机运动的统一单阶段模型。
- 针对度量尺度歧义，结合场景级几何特征与度量空间监督，并保留手部细粒度特征。
- 将遮挡与出视野下的手部重建建模为条件运动生成，使用 flow matching，并报告仅两步采样即可优于直接回归。
- 在 HOT3D 与 ARCTIC 上报告世界空间准确性与时间一致性优于现有方法，并给出具体误差与相机尺度恢复指标。
- 在 HoloAssist、H2O、TACO 上报告零样本评估取得最低 WA-MPJPE。

### 局限性
摘要未提供足够信息说明方法局限性、失败场景、计算成本、对特定数据或设备的依赖、生成式建模的潜在风险，以及各模块的消融细节。摘要也未提供训练数据规模、推理速度、超参数敏感性或更细粒度的实验设置。

### 阅读优先级
高。理由：该论文直接针对第一视角世界空间手部运动重建中的误差累积、度量尺度歧义与遮挡/出视野三项核心挑战，提出单阶段联合重建与生成式建模思路；摘要给出了明确的定量改进、跨数据集零样本结果，并与几何基础模型分类相关，具备较强的问题针对性与方法参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering metric world-space hand motion from egocentric video supports understanding human interactions and transferring them to embodied agents. Three challenges complicate this task: multi-stage pipelines propagate errors from independently estimated hand and camera motion; monocular observations leave physical scale ambiguous; and occlusion and out-of-view hands admit multiple plausible motion trajectories. We present DewHand, a unified model for direct joint reconstruction of world-space hand and camera motion. To avoid compounding errors from multi-stage estimation, DewHand jointly predicts hand and camera motion in a shared world coordinate system within a single-stage pipeline. To resolve metric-scale ambiguity, it combines scene-level geometric features from VGGT-$Ω$ with metric-space supervision, while hand-specific features preserve fine-grained articulation. To handle occlusion and out-of-view hands, we formulate reconstruction as conditional motion generation with flow matching. Under the same architecture, this generative formulation outperforms direct regression in both accuracy and temporal smoothness with only two sampling steps. Experiments on HOT3D and ARCTIC demonstrate improved world-space accuracy and temporal consistency over state-of-the-art methods. DewHand reduces rigid-aligned world-space error relative to StableHand from 32.9 to 28.4 mm on HOT3D and from 76.2 to 36.2 mm on ARCTIC. It also recovers camera scale within 10% on two thirds of HOT3D clips, versus about a quarter for SLAM. Moreover, in zero-shot evaluations on HoloAssist, H2O, and TACO, captured with different devices, DewHand achieves the lowest rigid-aligned world-space error (WA-MPJPE) on each dataset.

</details>

#### 2026-10-21 - GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

**Authors:** Qinfan Zhang, Yifan Luo, Haoyuan Shi, Guanlin Liu, Han Dong, Haozhe Shan, Yong Dai, Xiangcong Ren, Xiaozhu Ju
**Links:** [abs](https://arxiv.org/abs/2610.29866) - [pdf](https://arxiv.org/pdf/2610.29866)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** geometry foundation model, point map, 3D reconstruction, manipulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models
- 作者：Qinfan Zhang, Yifan Luo, Haoyuan Shi, Guanlin Liu, Han Dong, Haozhe Shan, Yong Dai, Xiangcong Ren, Xiaozhu Ju
- 出版日期：2026-10-21T15:23:18Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.29866) / [PDF](https://arxiv.org/pdf/2610.29866)

### 一句话总结
GeoMem-VLA 将显式 3D 几何监督内化到可学习的几何 token 中，并作为时间记忆用于动作生成，使推理阶段无需调用 3D 教师模型或显式重建场景。

### 研究问题
摘要指出，几何结构对机器人操作和理解 3D 世界至关重要；多数 VLA 模型依赖当前观测的 2D 表示，而几何感知方法往往需要额外 3D 信息。与此同时，从单次观测独立推断的几何通常被丢弃，未能累积为持续的任务表示。论文要解决的问题是：如何让动作生成获得紧凑、任务相关且可持续更新的几何抽象，而不是每一步都依赖完整可渲染的 3D 重建。

### 核心思路/方法
论文提出 GeoMem-VLA 框架，将显式 3D 监督内化到专门的几何 token 中，并把这些 token 维护为用于动作生成的时间记忆。其做法不是直接将 VLM 原生视觉嵌入与教师特征空间对齐。

训练阶段，冻结的几何基础模型通过几何流匹配目标监督可学习的 GeoPlan token；该目标定义在当前场景点图和未来末端执行器轨迹上。这些 token 与观测表示的记忆集成：历史信息被检索、与当前观测自适应融合，并随着任务推进进行整合，以保留事件帧。

推理阶段，策略检索历史表示，并将其与当前工作表示融合以预测动作，不调用 3D 教师模型，也不显式重建场景。摘要还提到，方法经过基准特定的下游适配后取得相应结果。

### 主要贡献
- 提出 GeoMem-VLA，将显式 3D 监督内化为几何 token，并作为时间记忆用于 VLA 动作生成。
- 设计以冻结几何基础模型监督可学习 GeoPlan token 的训练机制，监督目标为当前场景点图与未来末端执行器轨迹上的几何流匹配。
- 将几何 token 与观测表示记忆结合，支持历史信息检索、与当前观测的自适应融合及任务推进中的记忆整合。
- 推理阶段无需调用 3D 教师模型或显式重建场景。
- 摘要报告的结果：经基准特定下游适配后，LIBERO 平均成功率 98.9%；RoboTwin 干净/随机化设置分别为 91.10% / 91.24%；五个真实世界任务平均成功率 78.0%。

### 局限性
- 摘要未提供足够信息说明几何流匹配目标的具体形式、网络结构、训练数据规模与训练成本。
- 摘要未提供足够信息说明“基准特定下游适配”的具体做法及其对各结果的影响程度。
- 摘要未提供足够信息说明时间记忆的容量、更新频率、遗忘机制及长时序任务中的表现。
- 摘要未提供足够信息说明与基线方法的完整对比、消融实验和失败案例分析。
- 摘要未提供足够信息说明真实世界五个任务的具体设置、评价协议与统计显著性。
- 摘要未提供足够信息说明方法对几何基础模型质量、传感器噪声或视角变化的敏感性。

### 阅读优先级
中。理由：该论文聚焦 VLA 中 3D 几何理解的内化与时间记忆，问题定位清晰，且摘要给出了多个基准和真实任务的成功率结果；但当前仅有摘要与元数据，缺少方法细节、基线对比和消融信息。若读者关注机器人操作中的几何表示、时间记忆或 VLA 架构，值得进一步阅读全文；若仅需快速了解结论，摘要信息已较集中。

</details>

<details>
<summary>Abstract</summary>

Geometric structure is essential for robotic manipulation and understanding the 3D world. Most VLA models rely on 2D representations of current observations, while geometry-aware approaches often require additional 3D information. However, geometry inferred independently from individual observations is often discarded rather than accumulated into a persistent task representation. Our key insight is that action generation needs a compact, task-relevant geometric abstraction that can be continuously updated, rather than a complete, renderable 3D reconstruction at every step. We introduce GeoMem-VLA, a VLA framework that internalizes explicit 3D supervision into dedicated geometric tokens and maintains them as temporal memory for action generation, without directly aligning the VLM's native visual embeddings with the teacher feature space. During training, a frozen geometry foundation model supervises learnable GeoPlan tokens through a geometric flow-matching objective over the current scene point map and future end-effector tracks. These tokens are integrated with the memory of observation representations, where historical information is retrieved, adaptively fused with current observations, and consolidated to retain event frames as the task progresses. At inference, the policy retrieves historical representations and fuses them with the current working representation to predict actions, without invoking the 3D teacher or explicitly reconstructing the scene. After benchmark-specific downstream adaptation, GeoMem-VLA achieves 98.9% average success on LIBERO and 91.10% / 91.24% on RoboTwin's clean/randomized settings. Across five real-world tasks, GeoMem-VLA achieves 78.0% average success. These results suggest that internalizing and remembering 3D scene understanding is a promising approach to robot control.

</details>

#### 2026-10-21 - BlazeVGGT: 13x Faster VGGT at 2,000 Frames via Camera Token without Training

**Authors:** Shujun Yao, Junhui Lin, Congying Han, Tiande Guo, Ziwen Liu, Bonan Li
**Links:** [abs](https://arxiv.org/abs/2610.29454) - [pdf](https://arxiv.org/pdf/2610.29454)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, multi-view reconstruction, camera pose estimation, pose estimation, point cloud reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BlazeVGGT: 13x Faster VGGT at 2,000 Frames via Camera Token without Training
- 作者：Shujun Yao, Junhui Lin, Congying Han, Tiande Guo, Ziwen Liu, Bonan Li
- 出版日期：2026-10-21T09:11:19Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.29454 ；PDF https://arxiv.org/pdf/2610.29454

### 一句话总结
BlazeVGGT 提出一种无需训练的即插即用方法，利用 VGGT 相机 token 的相似性做视图级键值稀疏化，在保留全部帧作为查询的同时减少跨视图冗余计算，摘要称在 2,000 帧时推理约快 13 倍，并将 Chamfer Distance 从 0.41 降至 0.32。

### 研究问题
摘要指出，以 VGGT 为代表的前馈视觉几何模型通过稠密全局注意力实现多视图重建，但全对全跨视图计算随输入视图数量呈二次增长；由于高度重叠观测之间存在显著帧级冗余，长序列推理成本尤其高。论文关注的问题是如何在不训练、不更新参数的前提下，降低 VGGT 长序列推理中的冗余跨视图计算。

### 核心思路/方法
- 观察：摘要称 VGGT 相机 token 呈现“先拓扑、后几何”的演化，浅层 token 能可靠捕获局部视图邻域，深层 token 逐步编码全局组织的视图间几何。
- 方法：提出 BlazeVGGT，一种无需训练的结构感知帧级 key–value 稀疏化框架。
- 具体机制：在每个全局注意力块中，基于相机 token 关系构建视图级相似性核，并使用贪心行列式点过程（DPP）推断选择一组相互补充的紧凑视图。
- 注意力设计：被选视图构成 key–value 上下文，而所有输入帧保留为 query，形成非对称注意力，以维持稠密的逐帧预测并消除冗余跨视图计算。
- 集成方式：可直接作为即插即用模块集成到预训练 VGGT 中，无需参数更新。

### 主要贡献
- 揭示 VGGT 相机 token 的“拓扑优先、几何随后”演化现象，并据此设计帧级稀疏化。
- 提出无需训练的 BlazeVGGT，通过相机 token 相似性与贪心 DPP 选择互补视图，构建非对称 key–value 注意力。
- 摘要报告在 2,000 帧时相比 VGGT 推理约快 13 倍，Chamfer Distance 从 0.41 降至 0.32。
- 摘要称实验覆盖点云重建与相机位姿估计的精度—效率权衡，并与 FastVGGT、LiteVGGT 等现有加速器兼容，且可迁移到 StreamVGGT 和 PAGE-4D 等基于 VGGT 的模型。
- 代码已公开。

### 局限性
- 摘要未提供足够信息说明方法在非高度重叠视图、极端视角变化或不同序列长度下的具体表现边界。
- 摘要未提供足够信息说明贪心 DPP 选择带来的额外计算开销及其对端到端加速比的影响。
- 摘要未提供足够信息说明在更多数据集、更多基线或完整消融实验中的细节。
- 摘要未提供足够信息说明方法对相机 token 质量或 VGGT 特定结构的依赖程度。
- 摘要未提供足够信息说明与 FastVGGT、LiteVGGT 组合时的具体加速与精度数值。

### 阅读优先级
高。理由：该论文直接针对 VGGT 类前馈视觉几何模型长序列推理的二次复杂度瓶颈，提出无需训练、即插即用的加速方案，并给出 2,000 帧约 13 倍加速及 Chamfer Distance 改善的摘要级结果；若关注多视图重建、3D 重建效率或 VGGT 加速，具有较高阅读价值。但具体实验细节与局限性需以全文为准。

</details>

<details>
<summary>Abstract</summary>

Feed-forward visual geometry models, exemplified by VGGT, have demonstrated strong multi-view reconstruction capabilities through dense global attention. However, the resulting all-to-all cross-view computation scales quadratically with the number of input views, making long-sequence inference particularly expensive due to substantial frame-level redundancy among highly overlapping observations. We uncover a topology-first, geometry-later evolution in VGGT camera tokens: shallow-layer tokens reliably capture local view neighborhoods, whereas deeper-layer tokens progressively encode globally organized inter-view geometry. Motivated by this observation, we introduce BlazeVGGT, a training-free framework for structure-aware frame-level key--value sparsification. At each global-attention block, BlazeVGGT constructs a view-level similarity kernel from camera-token relations and employs greedy determinantal point process inference to select a compact set of mutually complementary views. The selected views constitute the key--value context, while all input frames are retained as queries. This asymmetric attention design preserves dense per-frame predictions while eliminating redundant cross-view computation, allowing our method to be directly integrated into pretrained VGGT as a plug-and-play module without parameter updates. Its advantages become increasingly pronounced with sequence length: at 2,000 frames, BlazeVGGT achieves approximately 13$\times$ faster inference than VGGT while reducing the Chamfer Distance from 0.41 to 0.32. Extensive experiments demonstrate a favorable accuracy--efficiency trade-off in point-cloud reconstruction and camera-pose estimation, compatibility with existing VGGT accelerators such as FastVGGT and LiteVGGT, and transferability to VGGT-based models including StreamVGGT and PAGE-4D. Codes are publicly available at https://github.com/MagiciannnY/BlazeVGGT.git.

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-26 - GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting

**Authors:** Tom Yachil, Andrei Sharf
**Links:** [abs](https://arxiv.org/abs/2610.35224) - [pdf](https://arxiv.org/pdf/2610.35224)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, 4D Gaussian, Gaussian Splatting, splatting

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
<summary>Abstract</summary>

Dynamic Gaussian reconstruction requires compact scene features to support coordinated changes in geometry and appearance. A factorized grid provides efficient local queries, but accurate interpolation alone does not ensure that the resulting dynamic attributes remain compatible across space and time. We introduce DimFlow, a framework that learns these features through bidirectional interaction between a multi-resolution grid and a coordinate-based expert branch. Feature-level adversarial alignment connects their distributions, adaptive fusion transfers complementary information, and activation-masked residual feedback refines the grid during training. Four attribute experts organize deformation, rotation, opacity, and temporal information before Gaussian rendering. In the aggregate comparison across D-NeRF, HyperNeRF, and DAVIS, DimFlow achieves 39.73 dB PSNR, improving on 4D-GS by 1.92 dB while matching its reported 85 FPS rendering speed. The model occupies 18.9 MB, compared with 18.3 MB for 4D-GS. Component and attribute-expert ablations reveal complementary contributions from feature alignment, adaptive exchange, and temporal processing.

</details>

#### 2026-10-22 - Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention

**Authors:** Wei Zhang, Ying Feng, Mengtong Wu, Shiqiang Gong, Huaqi Zhang, Qi Zhang
**Links:** [abs](https://arxiv.org/abs/2610.31320) - [pdf](https://arxiv.org/pdf/2610.31320)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 4D reconstruction, scene reconstruction, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention
- 作者：Wei Zhang, Ying Feng, Mengtong Wu, Shiqiang Gong, Huaqi Zhang, Qi Zhang
- 出版日期：2026-10-22T14:11:34Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 3D Reconstruction & Multi-view Geometry
- 链接：abstract_url: https://arxiv.org/abs/2610.31320；pdf_url: https://arxiv.org/pdf/2610.31320

### 一句话总结
Stream4D 提出一种无需训练的流式 4D 重建框架，利用因果注意力 KV 缓存中的时序运动线索生成动态掩码，并通过软键掩码抑制动态区域干扰，以改善相机位姿估计和长序列重建中的鬼影问题。

### 研究问题
现有流式 4D 重建方法通常假设场景是静态的，因此在包含动态物体的长序列中，会出现位姿漂移和鬼影伪影。论文关注的问题是如何在不重新训练模型的前提下，将静态区域与动态区域解耦，并提升流式重建对动态场景的鲁棒性。

### 核心思路/方法
论文提出 Stream4D，一个无需训练、运动解耦的流式重建框架，可直接集成到因果 Transformer 主干（如 StreamVGGT、Stream3R）中。其核心观察是因果注意力在 KV 缓存中隐式编码了丰富的时序运动线索。方法从多个注意力层和时间窗口中自适应聚合这些线索，并与深度先验融合，以处理遮挡和无纹理区域等困难情况，从而生成精确的动态掩码，实现静态与动态区域解耦。随后采用软键掩码方案，利用动态掩码抑制因果注意力中动态区域的干扰，以提高相机位姿估计精度。Stream4D 继承了因果注意力的效率，并与现有流式架构保持兼容。

### 主要贡献
- 提出无需训练的 Stream4D 流式 4D 重建框架，可直接集成到因果 Transformer 主干中。
- 利用因果注意力 KV 缓存中的时序运动线索，并结合多注意力层、多时间窗口聚合与深度先验，生成动态掩码以解耦静态和动态区域。
- 引入软键掩码方案，利用动态掩码抑制动态区域对因果注意力的干扰，从而改善相机位姿估计。
- 摘要称在多种动态场景基准上显著提升相机位姿估计和静态场景重建质量，生成可靠动态掩码，并有效缓解长序列鬼影。

### 局限性
摘要未提供足够信息。论文未在摘要中给出具体实验设置、数据集规模、定量指标、失败案例或计算开销等细节，因此无法基于摘要进一步判断其局限性。

### 阅读优先级
高。理由：该论文直接针对流式 4D 重建中动态场景处理的关键问题，提出无需训练且可兼容现有因果 Transformer 架构的方法，若摘要所述效果成立，对动态 / 4D 重建与多视图几何方向具有较高参考价值；但需注意摘要未提供定量实验细节，阅读时应重点核查实验验证与适用边界。

</details>

<details>
<summary>Abstract</summary>

4D scene reconstruction requires robust handling of dynamic objects, yet existing streaming methods commonly assume static scenes, leading to pose drift and ghosting artifacts over long sequences. We introduce Stream4D, a training-free, motion-decoupled streaming reconstruction framework that can be directly integrated into causal Transformer backbones (e.g., StreamVGGT, Stream3R). Our key observation is that causal attention implicitly encodes rich temporal motion cues within the KV cache. We adaptively aggregate these cues from multiple attention layers and across temporal windows, and fuse them with depth priors to handle challenging cases such as occlusions and textureless regions, producing precise dynamic masks that decouple static and dynamic regions. We then apply a soft key masking scheme that leverages these dynamic masks to suppress interference from dynamic regions in causal attention, thereby improving camera pose estimation accuracy. Stream4D inherits the efficiency of causal attention and remains compatible with existing streaming architectures. On diverse dynamic-scene benchmarks, Stream4D significantly improves camera pose estimation and static-scene reconstruction quality, yields reliable dynamic masks, and effectively mitigates long-sequence ghosting.

</details>

#### 2026-10-21 - R4DGS: Referring Segmentation in 4D Gaussian Splatting

**Authors:** Bangpu Chen, Yaxuan Li, Shirui Peng, Xiangtian Si, Liuxin Chu, Xitong Cao, Hongbo Jin, Jiayu Ding
**Links:** [abs](https://arxiv.org/abs/2610.30326) - [pdf](https://arxiv.org/pdf/2610.30326)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：R4DGS: Referring Segmentation in 4D Gaussian Splatting
- 作者：Bangpu Chen, Yaxuan Li, Shirui Peng, Xiangtian Si, Liuxin Chu, Xitong Cao, Hongbo Jin, Jiayu Ding
- 出版日期：2026-10-21T18:42:09Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.30326 ；PDF https://arxiv.org/pdf/2610.30326 ；项目页 https://chenbangpu.github.io/R4DGS/

### 一句话总结
论文提出 Referring 4D Gaussian Splatting（R4DGS）任务及配套基准 R4D-Bench-QA，并提出无需场景特定语义优化的统一框架 ReferGaussian，用于动态 4D 场景中基于自然语言指代的定位与分割。

### 研究问题
现有基于 4D Gaussian Splatting（4DGS）的动态表示在重建与渲染方面表现较强，但在动态场景中支持复杂自然语言指代方面仍有限。已有 4D Gaussian 方法主要面向渲染导向的动态建模，而语义扩展往往依赖场景特定的语义优化，或在相对简单的查询设置下评估。论文关注的问题包括：在动态 4D 场景中处理随时间变化、多目标或推理密集型、零目标或干扰项表达式的指代定位。

### 核心思路/方法
论文将任务定义为 Referring 4D Gaussian Splatting（R4DGS），并构建 R4D-Bench-QA 基准，提供结构化查询标注。方法上提出 ReferGaussian 统一框架：以 4DGS 为基础，将低层动态 Gaussians 转换为持久、可由语言寻址的实体；通过 EntityBank 组织带 mask 支持的 Gaussian 实体；利用多模态大语言模型（MLLMs）将复杂查询分解为可跟踪的对象短语与结构化指代约束；执行约束感知的 grounding，且不依赖场景特定语义优化，实现训练无关的指代推理。

### 主要贡献
- 提出并研究 R4DGS 任务，覆盖动态场景中时间变化、多目标或推理密集型、零目标或干扰项等自然语言指代设置。
- 构建 R4D-Bench-QA 基准，提供结构化查询标注以支持该任务评估。
- 提出 ReferGaussian 统一框架，将动态 Gaussians 组织为语言可寻址实体，并结合 MLLM 查询分解与约束感知 grounding，实现无需场景特定语义优化的指代推理。
- 在 R4D-Bench-QA 与 4D LangSplat 协议上的实验表明，时间目标选择有所改进，并在无场景特定语义训练条件下取得有竞争力的时空 grounding 表现。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、计算开销、对 MLLM 或 mask 质量的依赖程度、基准规模与标注细节，也未给出定量实验结果和对比方法细节。

### 阅读优先级
中。理由：该论文提出新任务、新基准与新框架，问题定义清晰，且强调训练无关与免场景特定语义优化，对 4D 动态场景理解与语言 grounding 方向具有参考价值；但当前信息仅来自摘要，缺少定量结果、实现细节与局限性分析，需阅读全文后再判断其方法有效性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Dynamic representations based on 4D Gaussian Splatting (4DGS) have shown strong capabilities in reconstruction and rendering, yet current methods remain limited in supporting complex natural-language referring in dynamic scenes. Existing 4D Gaussian methods are primarily designed for rendering-oriented dynamic modeling, while current semantic extensions often rely on scene-specific semantic optimization or are evaluated on relatively simple query settings. In this paper, we study Referring 4D Gaussian Splatting (R4DGS), a task for grounding temporally varying, multi-target or reasoning-intensive, and zero-target or distractor expressions in dynamic 4D scenes. To support this task, we introduce R4D-Bench-QA, a benchmark with structured query annotations. We further present ReferGaussian, a unified framework built upon 4DGS that converts low-level dynamic Gaussians into persistent, language-addressable entities for training-free referring inference. ReferGaussian organizes mask-supported Gaussian entities in an EntityBank, uses Multimodal Large Language Models (MLLMs) to decompose complex queries into trackable object phrases and structured referring constraints, and performs constraint-aware grounding without scene-specific semantic optimization. Experiments on R4D-Bench-QA and the 4D LangSplat protocol demonstrate improved temporal target selection and competitive spatiotemporal grounding without scene-specific semantic training. Project resources are available at https://chenbangpu.github.io/R4DGS/.

</details>

#### 2026-10-20 - AEON: Unifying Video and 3D World Models

**Authors:** Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou
**Links:** [abs](https://arxiv.org/abs/2610.28631) - [pdf](https://arxiv.org/pdf/2610.28631)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, 4D Gaussian, Gaussian Splatting, rendering, splatting, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AEON: Unifying Video and 3D World Models
- 作者：Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou
- 出版日期：2026-10-20T17:59:51Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.28631)｜[PDF](https://arxiv.org/pdf/2610.28631)｜[项目页](https://weiqi-zhang.github.io/AEON)

### 一句话总结
AEON 提出一个统一视频生成式世界模型与 3D 生成式世界模型的框架，在文本或图像条件视频潜空间中生成可渲染的 4D Gaussian Splatting（4DGS）作为显式世界表示，以兼顾真实感与 3D 一致性。

### 研究问题
摘要指出，当前面向显式世界模拟的世界模型主要沿两条路径发展：（1）视频生成模型（如 Sora）能模拟真实外观，但无法保持 3D 一致性；（2）3D 生成模型（如 Marble）能生成几何一致的场景，但往往产生静态、真实感较弱的观测。论文旨在弥合这两类世界模型，并结合二者优势。

### 核心思路/方法
AEON 的关键思路是构建一个生成模型，使其在文本或图像条件视频的潜空间中运行，同时产可渲染的 4D 图形基元，具体为 4D Gaussian Splatting（4DGS），作为显式世界表示。方法上包括：
- 训练一个 4D 重建模型，从单目视频中预测 4DGS 与相机位姿，作为初始化的 4D 解码器；
- 设计域适配器，通过在视频 VAE 上的蒸馏过程，将生成式视频潜变量转换为重建式 4D 潜变量；
- 通过在预测的相机轨迹上渲染 4DGS，自然支持基于视频的世界建模，并构建具有场景动态的持久 4D 环境。

### 主要贡献
基于摘要可确认的贡献包括：
- 提出统一框架 AEON，桥接基于视频与基于 3D 的世界模型，结合两者优势；
- 在条件视频潜空间中生成可渲染的 4DGS 显式世界表示；
- 训练单目视频的 4D 重建模型以预测 4DGS 和相机位姿，并作为 4D 解码器初始化；
- 设计域适配器，通过视频 VAE 上的蒸馏将生成式视频潜变量转为重建式 4D 潜变量；
- 支持基于视频的世界建模与具有场景动态的持久 4D 环境构建，并在标准基准上取得摘要所称的 state-of-the-art 性能。

### 局限性
摘要未提供足够信息。摘要仅给出高层方法与性能声明，未说明具体实验设置、基准名称、评价指标、失败情形、计算开销或适用范围限制，因此无法基于给定内容可靠总结局限性。

### 阅读优先级
中。理由：该论文涉及视频世界模型与 3D/4D 显式表示的融合，主题与 Dynamic / 4D Reconstruction、神经场景表示与渲染、具身/机器人/AR 应用相关，问题定位清晰；但摘要未提供实验细节与定量结果，是否值得深入阅读需结合全文的实验严谨性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consistency; and (2) 3D generative models (e.g., Marble), which generate geometrically consistent scenes but often yield static, less realistic observations. We present AEON, a unified framework that bridges video-based and 3D-based world models and combines the benefits of both. The key insight of AEON lies in a generative model that operates within the text- or image-conditioned video latent space while producing renderable 4D graphics primitives---specifically, 4D Gaussian Splatting (4DGS)---as the explicit world representation. We train a 4D reconstruction model to predict both 4DGS and camera poses from monocular videos, serving as our initialized 4D decoder. Furthermore, we design a domain adapter that translates generative video latents into reconstructive 4D latents through a distillation process on the video VAE. AEON naturally supports video-based world modeling by rendering 4DGS at predicted camera trajectories, and constructs a persistent 4D environment with scene dynamics for realistic world simulation. Consequently, AEON empowers a diverse range of world modeling applications and achieves state-of-the-art performance on standard benchmarks. Project Page: https://weiqi-zhang.github.io/AEON

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-26 - Metric Scale for Insta360 Structure-from-Motion from the Camera's Embedded IMU

**Authors:** Davide Cuttini, Diego Di Tommaso, Alessio Antoniacomi, Luca Simonetti
**Links:** [abs](https://arxiv.org/abs/2610.35554) - [pdf](https://arxiv.org/pdf/2610.35554)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, structure from motion, SfM

<details>
<summary>Abstract</summary>

Structure-from-motion (SfM) from the dual-fisheye video of a consumer 360-degree camera recovers geometry only up to a similarity transform; in the pipeline considered here, metric scale is obtained from smartphone ARKit or ARCore poses captured alongside the camera. This paper evaluates a self-contained alternative: the IMU embedded in the Insta360 X5 and X6, recorded at 1 kHz. The sensor is characterised (noise density, camera-IMU synchronisation, accelerometer scale factor, bias stability), the camera-IMU rotation and frame timing are estimated from the data, and the scale is recovered by a linear visual-inertial alignment over the SfM poses of a whole survey. The standard formulation, with gravity and accelerometer bias shared across the survey, overestimates the scale by 3.4% on average; estimating each contiguous segment independently and averaging removes the bias. On nine surveys with a co-mounted LiDAR scanner the inertial scale deviates from the LiDAR by 0.74% in mean absolute error, against 1.94% for the smartphone scale; on printed fiducial markers both agree within the 1% uncertainty of the target. On the reference trajectories of thirty sequences of a public benchmark, brought to scales of 1/40, 1 and 40, the estimator recovers the metric scale with a mean error of -0.07% and a standard deviation of 1.28%. On fifty production surveys where the smartphone is the only reference, the two scales agree to a standard deviation of 2.6%, the inertial scale being 0.9% lower on average; the difference does not depend on window construction, grows with the extent of the smartphone anchor, and cannot be attributed to either reference. An ablation over window construction and a comparison with monocular metric-depth networks complete the study.

</details>

#### 2026-10-26 - Generative Structure from Motion with Native 3D Diffusion

**Authors:** Haobin Duan, Binbin Huang, Mochu Xiang, Yiqun Zhao, Zibo Zhao, Yi Ma, Shenghua Gao
**Links:** [abs](https://arxiv.org/abs/2610.35522) - [pdf](https://arxiv.org/pdf/2610.35522)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, pose estimation

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
<summary>Abstract</summary>

Deep learning facilitates rapid single shot three dimensional (3D) reconstruction using fringe projection profilometry (FPP), but recovering accurate surface height from a single high frequency fringe image remains challenging because both long-range spatial consistency and fine geometric details must be preserved. Convolutional networks are limited in modeling long range dependencies, whereas window-based Transformers establish global interactions only progressively with increasing depth. To address these limitations, a hybrid Mamba Transformer network is proposed for fringe to height regression. The network adopts a Swin based U shaped architecture and introduces visual state space modeling at the intermediate resolution encoder stage. An axial and dilated vision state space (ADVSS) block is further developed to enhance prescan feature encoding through local, dilated, and axial depthwise convolutions while retaining four directional selective scanning. This design combines linear complexity long range modeling with direction aware preservation of local fringe structures. Experiments on a publicly available FPP dataset show that the proposed method outperforms hNet, SwinConvUNet, UHRNet, and HiDNet in mean absolute error(MAE), root mean square error (RMSE), absolute relative error, and structural similarity index measure (SSIM). Using only one deformed fringe image, the proposed method achieves an RMSE of 0.548 mm and an SSIM of 0.9985, reducing RMSE by 65.2% and 59.6% relative to UHRNet and HiDNet, respectively. These results demonstrate the effectiveness of combining selective state space modeling with hierarchical window based attention for accurate single-shot FPP reconstruction.

</details>

#### 2026-10-22 - OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields

**Authors:** Namitha Guruprasad, Abhay Yadav, Cheng Peng, Rama Chellappa, Anand Bhattad
**Links:** [abs](https://arxiv.org/abs/2610.31645) - [pdf](https://arxiv.org/pdf/2610.31645)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields
- 作者：Namitha Guruprasad, Abhay Yadav, Cheng Peng, Rama Chellappa, Anand Bhattad
- 出版日期：2026-10-22T17:55:30Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供。
- 链接：摘要页 https://arxiv.org/abs/2610.31645 ；PDF 链接 https://arxiv.org/pdf/2610.31645

### 一句话总结
OmniRay 是一个前馈式单目 3D 重建模型，通过由单调径向基、球谐残差和自由形式残差组成的复合射线场，在不同相机几何下预测逐像素射线方向与尺度未知的径向距离，从而在推理时无需相机信息即可恢复 3D 点云。

### 研究问题
摘要指出，多数单目 3D 重建模型假设针孔相机，因此在鱼眼、全景等广角镜头图像上会产生扭曲的几何；相机感知模型虽通过预测逐像素射线场来摆脱针孔假设，却用单一固定基同时表示整体相机投影与更细变化。论文要解决的问题是如何更有效地表示多样相机几何，并实现与相机无关的单目 3D 重建。

### 核心思路/方法
论文提出将相机几何视为具有层次复杂性的射线表示，并设计 OmniRay 的前馈模型，其 Ray Module 由三部分组成：
1. 单调径向基，用于捕捉径向对称结构；
2. 球谐残差，用于表示相对于径向基的平滑偏差；
3. 自由形式残差，用于表示剩余的局部变化。
这些组件以球面上的连续旋转方式组合，使表示能够适应多样相机几何。给定单张图像，OmniRay 为每个像素预测射线方向和尺度未知的径向距离，并由此恢复 3D 点云，推理时不需要相机信息。

### 主要贡献
- 提出 OmniRay，一个与相机无关的单目前馈 3D 重建模型。
- 设计复合射线场表示，将射线表示拆分为单调径向基、球谐残差和自由形式残差，并以球面连续旋转组合。
- 在推理时无需相机信息，即可从单张图像预测逐像素射线方向和尺度未知径向距离，进而恢复 3D 点云。
- 摘要称在不同相机配置上的广泛实验表明，OmniRay 在相机无关单目 3D 重建上建立了新的 state-of-the-art。

### 局限性
摘要未提供足够信息说明局限性。摘要未给出具体实验数据集、评价指标、定量结果、失败案例、计算开销或对不同相机类型的覆盖范围等细节；这些信息摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对相机无关单目 3D 重建中的相机几何表示问题，提出层次化复合射线场，并声称在多种相机配置下达到新的 state-of-the-art；若关注广角、鱼眼或全景图像的单目 3D 重建，该工作与问题设定高度相关。但需注意，摘要未提供实验细节，阅读全文前应保持对结论范围和适用条件的审慎判断。

</details>

<details>
<summary>Abstract</summary>

Monocular models recover 3D geometry from a single image in one pass, but most assume a pinhole camera and produce distorted geometry on the wide-angle imagery produced by fisheye and panoramic lenses. Camera-aware models remove this assumption by predicting a per-pixel ray field. However, they represent different camera geometries using a single fixed basis to capture both the overall camera projection and its finer variations. We argue that camera geometry can be viewed as having a hierarchy of complexity for representing rays. We present OmniRay, a feed-forward model whose Ray Module is composed of three components: a monotone radial base that captures radially symmetric structure, a spherical-harmonic residual for smooth deviations from it, and a free-form residual for remaining local variation. These components are composed as successive rotations on the sphere, allowing the representation to accommodate diverse camera geometries. Given a single image, OmniRay predicts a ray direction and an up-to-scale radial distance for every pixel, from which a 3D point cloud is recovered without needing camera information at inference time. Extensive experiments across different camera configurations demonstrate that OmniRay establishes a new state-of-the-art in camera-agnostic monocular 3D reconstruction.

</details>

#### 2026-10-22 - HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction

**Authors:** Zunnan Xu, Shangchen Zhou, Yihang Luo, Chen Change Loy
**Links:** [abs](https://arxiv.org/abs/2610.31635) - [pdf](https://arxiv.org/pdf/2610.31635)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction
- 作者：Zunnan Xu, Shangchen Zhou, Yihang Luo, Chen Change Loy
- 出版日期：2026-10-22T17:51:10Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.31635) / [PDF](https://arxiv.org/pdf/2610.31635)

### 一句话总结
HiP3R 提出分层位姿图：先用块级 Sim(3) 图建立全局布局与尺度，再固定布局、按帧估计共享 SE(3) 相机，以缓解长视频分块重建中的全局一致性与局部修正之间的权衡。

### 研究问题
前馈模型可对短视频窗口准确估计相机运动与 3D 几何，但计算和内存成本使其无法直接处理数千帧序列。长视频因此被切分为重叠块，产生坐标帧不一致、共享相机重复估计的独立局部重建。要实现全局一致性，需要跨相邻重叠和远距离重访传播约束，这自然指向位姿图优化；但图层级选择存在权衡：块级图能高效处理尺度漂移和大回环，却无法用刚体变换修正内部误差或冲突的帧预测；帧级优化提供局部灵活性，但全局扩展计算昂贵且可能破坏度量尺度。

### 核心思路/方法
HiP3R 使用分层位姿图解决上述权衡。首先优化一个鲁棒的块级 Sim(3) 图，以建立全局布局和尺度；随后固定该布局，为每一帧估计一个共享的 SE(3) 相机，将重叠窗口预测转化为单一轨迹。该方法可应用于基于块和流式的后端，且无需额外训练或微调。

### 主要贡献
- 提出分层位姿图 HiP3R，用于长时序 3D 重建中的全局一致性优化。
- 通过块级 Sim(3) 图建立全局布局与尺度，再固定布局进行帧级共享 SE(3) 相机估计，以结合块级效率与帧级局部灵活性。
- 摘要称在多个基准上验证了方法在改善相机轨迹和 3D 重建方面的有效性。
- 方法适用于基于块和流式的后端，无需额外训练或微调，并提供代码链接。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集规模、计算开销、失败案例或定量对比细节；分层优化的具体鲁棒性边界、对极端尺度漂移或严重冲突预测的表现也摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对长视频 3D 重建中“分块独立重建导致全局不一致”的关键问题，提出清晰的分层位姿图方案，问题动机和方法权衡描述较明确；但摘要未提供定量实验结果与实现细节，是否优先精读取决于读者对长时序重建、位姿图优化或流式后端的直接兴趣。

</details>

<details>
<summary>Abstract</summary>

Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distant revisits across the sequence. This requirement naturally motivates pose graph optimization. However, the choice of graph level creates a trade-off. Chunk-level graphs efficiently resolve scale drift and close large loops. Yet, their rigid transformations cannot correct internal errors or conflicting frame predictions. Conversely, frame-level optimization offers local flexibility, but scaling it globally is computationally expensive and can break metric scale. HiP3R resolves this trade-off using a hierarchical pose graph. HiP3R first optimizes a robust chunk-level $\mathrm{Sim}(3)$ graph to establish the global layout and scale. It then holds this layout fixed and estimates one shared $\mathrm{SE}(3)$ camera per frame, turning overlapping window predictions into a single trajectory. Experiments across multiple benchmarks demonstrate the effectiveness of HiP3R in improving camera trajectories and 3D reconstruction. Our method applies to both chunk-based and streaming backends without additional training or fine-tuning. The codes are available at https://kkakkkka.github.io/HiP3R.

</details>

#### 2026-10-22 - F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation

**Authors:** Jinyu Zhang, Haitao Lin, Jiashu Hou, Xiangyang Xue, Yanwei Fu
**Links:** [abs](https://arxiv.org/abs/2610.31623) - [pdf](https://arxiv.org/pdf/2610.31623)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation
- 作者：Jinyu Zhang, Haitao Lin, Jiashu Hou, Xiangyang Xue, Yanwei Fu
- 出版日期：2026-10-22T17:43:34Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2610.31623) / [PDF](https://arxiv.org/pdf/2610.31623)

### 一句话总结
F2G-Pose 提出一种实时、直接、单次前向的类别级 RGB-D 物体姿态估计框架，通过将稠密视觉基础特征提升到部分点云并结合几何与专家混合 Transformer，在一次前向中预测姿态、度量尺寸和相机坐标系下的补全形状。

### 研究问题
论文研究类别级 RGB-D 物体姿态估计：在没有实例特定 CAD 模型或参考视图的情况下，恢复物体的 3D 旋转与平移。该任务因类内差异、对称性和部分观测而高度模糊。摘要指出，现有方法难以兼顾可靠性与效率：基于中间结构的方法容易产生误差传播，扩散模型则存在推理延迟高和后处理候选提取复杂的问题。

### 核心思路/方法
F2G-Pose 是一个实时、直接、单次前向的框架，从单次 RGB-D 观测中预测类别级姿态、度量尺寸和相机坐标系下的补全形状。方法将稠密视觉基础特征提升到部分点云上，使用 DGCNN tokenization 编码局部几何，并通过 Mixture-of-Experts Transformer 整合物体级结构。联合的尺寸预测与相机坐标系形状补全通过稠密几何监督促进度量一致性。其任务特定网络仅在带姿态标注的合成 SOPE 数据上训练，冻结的 RADIO 主干为外部预训练。

### 主要贡献
- 提出 F2G-Pose，一个实时、直接、单次前向的类别级 RGB-D 物体姿态估计框架，同时预测姿态、度量尺寸和相机坐标系补全形状。
- 设计将稠密视觉基础特征提升到部分点云、结合 DGCNN tokenization 与 Mixture-of-Experts Transformer 的几何感知方法。
- 通过联合尺寸预测与形状补全及稠密几何监督，促进度量一致性。
- 摘要报告其在 SOPE 和 ROPE 上达到 state-of-the-art 精度，仅姿态推理运行速度为 28 FPS，并在 HouseCat6D 上展示相机坐标系几何能力、在 HANDAL 上展示真实物体迁移能力。
- 摘要还提到对延迟、鲁棒性、形状补全和 GenPose++ 候选行为的分析，以及真实世界操作实验展示部署潜力；项目页面、代码和预训练模型已公开。

### 局限性
摘要未提供足够信息说明明确局限性。仅能从摘要中看到：任务特定网络仅在带姿态标注的合成 SOPE 数据上训练；真实世界实验基于分割后的 RGB-D 输入；摘要未给出失败案例、泛化边界或计算资源需求的详细讨论。

### 阅读优先级
高。理由：该论文针对类别级 RGB-D 物体姿态估计中可靠性与效率的权衡问题，提出单次前向实时框架，摘要声称在 SOPE 和 ROPE 上达到 state-of-the-art，并报告 28 FPS 姿态推理速度，同时涉及形状补全、真实物体迁移和真实操作实验，与该方向的研究和部署关注点高度相关。

</details>

<details>
<summary>Abstract</summary>

This paper studies category-level RGB-D object pose estimation, which recovers an object's 3D rotation and translation without instance-specific CAD models or reference views. This task is highly ambiguous due to intra-class variations, symmetries, and partial observations. Current solutions struggle to balance reliability and efficiency: methods based on intermediate structures are prone to error propagation, while diffusion models suffer from high inference latency and complex post-hoc candidate extraction. To address this, we present F2G-Pose, a real-time direct, single-pass framework that predicts category-level pose, metric size, and camera-frame completed shape from a single RGB-D observation in one feed-forward pass. F2G-Pose lifts dense visual foundation features to partial point clouds, encodes local geometry with DGCNN tokenization, and integrates object-level structure with a Mixture-of-Experts Transformer. Joint size prediction and camera-frame shape completion encourage metric consistency through dense geometric supervision. With its task-specific network trained only on pose-annotated synthetic SOPE data and its frozen RADIO backbone externally pretrained, F2G-Pose achieves state-of-the-art accuracy on SOPE and ROPE while running at 28 FPS for pose-only inference, and further demonstrates strong camera-frame geometry on HouseCat6D and real-object transfer on HANDAL. Analyses of latency, robustness, shape completion, and GenPose++ candidate behavior further demonstrate the efficiency and reliability of F2G-Pose, with real-world manipulation experiments demonstrating deployment potential under segmented RGB-D inputs. The project page, code, and pretrained models are made available at https://jrryzh.github.io/F2G-Pose/.

</details>

#### 2026-10-22 - H-2DGS: Height-Field Gaussian Splatting for Sharp and Deformable Neurosurgical Surface Reconstruction

**Authors:** Zhang Zichuan, Bart Brouwers, Rembrandt Bakker, Maud Landers, Geert-Jan Rutten, Maxime Chamberland
**Links:** [abs](https://arxiv.org/abs/2610.30910) - [pdf](https://arxiv.org/pdf/2610.30910)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：H-2DGS: Height-Field Gaussian Splatting for Sharp and Deformable Neurosurgical Surface Reconstruction
- 作者：Zhang Zichuan, Bart Brouwers, Rembrandt Bakker, Maud Landers, Geert-Jan Rutten, Maxime Chamberland
- 出版日期：2026-10-22T08:33:14Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.30910 ；PDF https://arxiv.org/pdf/2610.30910

### 一句话总结
论文提出 H-2DGS，一种三阶段的高度场 2D 高斯泼溅流程，用于在神经外科场景中获得尖锐、可变形且能与 MRI 和扩散示踪路径共同可视化的皮层表面重建。

### 研究问题
神经外科导航通常以 2D MRI 切片呈现信息，难以将切片中的解剖结构与手术显微镜下观察到的皮层表面对应起来。论文希望构建一个共同的 3D 可视化，将肿瘤手术中暴露皮层的照片级真实重建、全脑 MRI 背景以及扩散示踪路径结合起来。该任务要求重建的皮层形成清晰的解剖边界，而不是模糊、会遮挡内部结构的弥散体积。传统 3D Gaussian Splatting 虽能复现观察视角，但在手术视角覆盖有限时，可能将不透明度分布到较厚且几何含糊的带状区域中。

### 核心思路/方法
论文提出 height-field 2D Gaussian Splatting（H-2DGS），包含三个阶段：
1. 进行稳健的 3DGS 重建；
2. 将其深度融合到共享的截断符号距离场（TSDF）表面中；
3. 用弯曲的、面向表面的 Gaussian 基元表示该表面。

方法中分别使用高度、颜色和不透明度基来表示局部几何与外观，并通过邻居过渡目标协调重叠 patch。显式表面还支持术后对齐：由 MRI 导出的深度使重建发生变形，而带跟踪的颜色监督与交替优化用于保持外观。

### 主要贡献
- 提出 H-2DGS 三阶段流程，将 3DGS 重建、TSDF 表面融合与面向表面的 2D Gaussian 表示结合，以缓解有限手术视角下传统 3DGS 不透明度弥散和几何含糊的问题。
- 通过高度、颜色、不透明度分离基以及邻居过渡目标，建模局部几何与外观并协调重叠 patch。
- 利用显式表面支持术后对齐，包括 MRI 深度驱动的形变和带跟踪颜色监督的交替优化。
- 在五个真实神经外科案例中报告了较低的多视角深度不一致性、紧凑的 7.97MB 表示，以及每帧 29--42ms 的交互式渲染。
- 摘要称所得尖锐、可变形表面可与示踪路径和 MRI 解剖清晰整合，并包括术后切除腔。

### 局限性
摘要未提供足够信息来说明方法的局限性、失败案例、适用范围边界或更全面的定量对比结果。摘要仅提到五个真实神经外科案例及部分指标，未提供数据规模细节、统计显著性、基线完整对比或临床验证信息。

### 阅读优先级
高。理由：论文聚焦神经外科导航中的 3D 可视化与皮层表面重建，问题明确；方法将 3DGS、TSDF 与可变形表面表示结合，并给出真实病例、表示大小和交互渲染时间等摘要级结果；对多视角几何、神经渲染及医学图像引导重建方向具有较高相关性。但摘要未提供完整实验细节和局限性，深入判断仍需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Neurosurgical navigation commonly presents magnetic resonance imaging (MRI) as 2D slices, making it difficult to relate the anatomy in those slices to the cortical surface observed through the surgical microscope. We seek a common 3D visualization that combines a photorealistic reconstruction of the exposed cortex during tumor surgery with whole-brain MRI context and diffusion tractography pathways. This requires the reconstructed cortex to form a clear boundary around the brain anatomy rather than a diffuse volume that obscures internal structures. Conventional 3D Gaussian Splatting (3DGS) can reproduce observed views but, under limited surgical view coverage, may distribute opacity through a thick and geometrically ambiguous band. We introduce height-field 2D Gaussian Splatting (H-2DGS), a three-stage pipeline that concentrates a robust 3DGS reconstruction, fuses its depth into a shared truncated signed distance field (TSDF) surface, and represents that surface with curved, surface-oriented Gaussian primitives. Separate height, color, and opacity bases provide local geometry and appearance, while a neighbor-transition objective coordinates overlapping patches. The explicit surface further supports postoperative alignment: MRI-derived depth deforms the reconstruction, and tracked-color supervision with alternating optimization preserves its appearance. Across five real neurosurgical cases, H-2DGS gives low multi-view depth inconsistency, a compact 7.97MB representation, and interactive rendering at 29--42ms per frame. The resulting sharp, deformable surface integrates clearly with tractography and MRI anatomy, including a postoperative resection cavity.

</details>

#### 2026-10-22 - WovenAnchor Matcher: Specialized Intra- and Inter-Image Context Modeling for Feature Matching

**Authors:** Zhiyang Li, Ruijiang Jin, Thibaut Klenke, Yusuke Sekikawa, Nakamasa Inoue
**Links:** [abs](https://arxiv.org/abs/2610.30799) - [pdf](https://arxiv.org/pdf/2610.30799)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WovenAnchor Matcher: Specialized Intra- and Inter-Image Context Modeling for Feature Matching
- 作者：Zhiyang Li, Ruijiang Jin, Thibaut Klenke, Yusuke Sekikawa, Nakamasa Inoue
- 出版日期：2026-10-22T06:24:39Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.30799 ；PDF https://arxiv.org/pdf/2610.30799

### 一句话总结
论文提出 WovenAnchor Matcher（WAM），一种基于“角色专门化上下文聚合”的半稠密特征匹配框架，分别用 WovenMamba 做图内聚合、AnchorCrossAttention 做图间聚合，并在 MegaDepth 上报告了相对 JamMa 基线的姿态估计提升。

### 研究问题
半稠密局部特征匹配通常在进行由粗到细的对应估计之前聚合上下文信息。论文指出，图内聚合与图间聚合承担不同角色：图内聚合应在每幅图像内传播空间证据并保留结构化的二维依赖；图间聚合应从可能对应的区域收集信息，同时限制无关位置带来的噪声。论文关注的是：如何为这两类聚合设计角色专门化的建模方式。

### 核心思路/方法
WAM 是一个基于角色专门化上下文聚合的半稠密匹配框架，引入两个互补算子：
- WovenMamba：通过“先水平、后垂直”的状态空间传播进行图内聚合，使垂直更新作用于已经过水平上下文化的特征，从而鼓励形成结构化的二维感受野偏置。
- AnchorCrossAttention：通过交叉注意力进行图间聚合，从图像对中可能对应的区域收集上下文；该交换在局部代表锚点上进行，而这些锚点聚合每个窗口内的特征证据。
整体流程位于半稠密局部特征匹配的“先聚合上下文、再由粗到细估计对应”的框架之下。

### 主要贡献
- 提出 WAM，一个基于角色专门化上下文聚合的半稠密匹配框架，明确区分图内聚合与图间聚合的不同职责。
- 提出 WovenMamba，以水平后垂直的状态空间传播实现图内聚合，鼓励结构化的二维感受野偏置。
- 提出 AnchorCrossAttention，基于局部代表锚点进行交叉注意力图间聚合，以从可能对应区域收集信息并限制无关位置噪声。
- 在 MegaDepth 上报告 66.1 pose AUC@5°，在相同评估设置下较 JamMa 基线提升 2.0 AUC 点。
- 消融显示移除或替换任一专门化组件都会降低精度，为图内传播与图间检索受益于角色专门化聚合设计提供证据。
- 代码与预训练权重已公开于 https://github.com/mmaiLab/WovenAnchorMatcher。

### 局限性
摘要未提供足够信息。摘要未说明计算开销、参数量、推理速度、内存占用、训练数据规模与训练细节、除 MegaDepth 外其他数据集的表现、失败场景或方法适用范围等局限相关信息。

### 阅读优先级
中。理由：论文聚焦半稠密特征匹配中的图内/图间上下文聚合角色区分，问题界定清晰，方法由两个职责明确的算子组成，并在 MegaDepth 上给出相对 JamMa 基线的定量提升与组件消融证据；对于关注特征匹配、多视图几何与 3D 重建中上下文建模的研究者有直接相关性。但摘要仅覆盖单一数据集上的姿态 AUC 与消融结论，未提供效率、泛化到其他基准或局限性的信息，若需要全面评估方法适用性，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Semi-dense local feature matching commonly aggregates contextual information before coarse-to-fine correspondence estimation. However, intra-image and inter-image aggregation serve different roles: the former should propagate spatial evidence within each image while retaining structured two-dimensional dependencies, whereas the latter should gather information from plausible corresponding regions while limiting noise from unrelated locations. We propose WovenAnchor Matcher (WAM), a semi-dense matching framework based on role-specialized context aggregation. WAM introduces two complementary operators. WovenMamba performs intra-image aggregation through horizontal-then-vertical state-space propagation, allowing vertical updates to operate on horizontally contextualized features and thereby encouraging a structured two-dimensional receptive-field bias. AnchorCrossAttention performs inter-image aggregation by using cross-attention to gather context from plausible corresponding regions across the image pair. It performs this exchange over local representative anchors that aggregate feature evidence within each window. On MegaDepth, WAM achieves 66.1 pose AUC@5$^\circ$, improving on the JamMa baseline by 2.0 AUC points under the same evaluation setup. Ablations show that removing or replacing either specialized component reduces accuracy, providing evidence that intra-image propagation and inter-image retrieval benefit from role-specific aggregation designs. Code and pretrained weights are available at https://github.com/mmaiLab/WovenAnchorMatcher.

</details>

#### 2026-10-22 - Evaluation of Front-End Feature Matching for Lunar Visual SLAM

**Authors:** Guillem Casadesus Vila, Grace Gao
**Links:** [abs](https://arxiv.org/abs/2610.30774) - [pdf](https://arxiv.org/pdf/2610.30774)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, visual SLAM, feature matching, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evaluation of Front-End Feature Matching for Lunar Visual SLAM
- 作者：Guillem Casadesus Vila, Grace Gao
- 出版日期：2026-10-22T05:52:13Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.30774) / [PDF](https://arxiv.org/pdf/2610.30774)

### 一句话总结
该论文在九个月球合成数据、月球试验台和地球类比数据集上，对十一种经典与学习型检测-匹配器组合及一个特征跟踪器，进行两两位姿精度和视觉里程计轨迹误差的基准评测。

### 研究问题
月球车在导航卫星服务部署前主要依赖相机定位，之后仍需要相机进行相对导航、危险检测和地表操作。视觉里程计（VO）和同步定位与建图（SLAM）大多通过帧间特征匹配估计运动，但现有特征匹配器多在城市、室内和驾驶场景中开发；行星研究或在轨道配准中比较匹配器，或在完整 SLAM 系统中比较，且带有参考位姿的真实月球图像稀缺。因此，在低纹理、光照严苛的月球地形上，月球车帧间匹配的表现及其对 VO 的影响尚未得到比较。

### 核心思路/方法
- 基准评测十一种经典与学习型检测器-匹配器组合，以及一个特征跟踪器。
- 使用九个月球合成、月球试验台和地球类比数据集。
- 评价指标包括：两两位姿精度（与基线比较）以及所得 VO 的轨迹误差。
- 在仅旋转度量下比较匹配器；并联合旋转与平移方向进行评分。
- 在立体 VO 中评估各配对能否持续跟踪全部八个序列数据集。
- 分析光照条件（如低聚光灯与漫射光）对经典检测器配对和 SuperPoint 的影响。
- 报告学习型组合的速度，并讨论 DINOv2 检索提案是否仍需几何验证。

### 主要贡献
- 在月球相关场景下系统比较经典与学习型特征检测-匹配组合，而非仅依赖城市、室内或驾驶场景结论。
- 指出在仅旋转度量下，SuperPoint 配对在两个月球试验台和一个类比站点上优于使用比率检验 FLANN 匹配的 SIFT；但在合成数据上差异较小或未解决。
- 指出当联合评分旋转与平移方向时，该 SIFT 配对在四个合成数据集上超过两个 SuperPoint 配对，说明仅凭合成结果不能确定真实月球车图像上的相对性能。
- 发现在立体 VO 中 SuperPoint 配对并不始终比 SIFT 更准确，但只有它们能在全部八个序列数据集上保持跟踪。
- 发现经典检测器配对依赖光照，而 SuperPoint 变化较小；同一试验台视图下低聚光灯使经典配对比漫射光更准确，这与更高对比度和检测到更多关键点一致。
- 报告 SuperPoint 与 LightGlue 是最快的学习型组合（每帧 16 ms），并指出 DINOv2 检索提案仍需要几何验证。

### 局限性
- 摘要未提供足够信息说明各数据集的规模、具体序列数量（除八个序列数据集外）、场景多样性及采集条件细节。
- 摘要未提供足够信息说明 VO 系统实现细节、基线定义、评价指标的具体计算方式与统计显著性。
- 摘要未提供足够信息说明 DINOv2 检索提案的具体实验配置及其几何验证需求的程度。
- 摘要未提供足够信息说明结论在真实月球任务环境中的泛化能力。
- 摘要未提供足够信息说明除 SuperPoint、SIFT、LightGlue、DINOv2 外其余检测-匹配组合的具体表现。

### 阅读优先级
高。理由：该论文直接面向月球视觉 SLAM 前端特征匹配这一关键但缺乏真实月球图像比较的问题，提供了跨合成、试验台和地球类比数据的基准结果，并明确指出合成结果与真实场景性能之间的差异，对月球车视觉定位与 VO 研究具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However, feature matchers are developed on urban, indoor and driving scenes, planetary studies compare them on orbital registration or within complete SLAM systems, and real lunar imagery with reference poses is scarce, so matching between rover frames on low-texture, harshly lit terrain, and its effect on VO, has not been compared. We benchmark eleven classical and learned detector-matcher combinations on nine synthetic, lunar-testbed, and terrestrial-analogue datasets, and a feature tracker, scoring pairwise pose accuracy against baseline and the trajectory error of the resulting VO. Under a common rotation-only metric, the SuperPoint pairings outperform SIFT with ratio-tested FLANN matching on both lunar testbeds and one analogue site, with smaller or unresolved differences on synthetic data. When rotation and translation direction are scored jointly, this SIFT pairing exceeds both SuperPoint pairings on four synthetic datasets, so synthetic results alone do not establish relative performance on real rover imagery. In stereo VO, the SuperPoint pairings are not consistently more accurate than SIFT, but only they keep tracking on all eight sequential datasets. Pairings with classical detectors depend on lighting while SuperPoint changes little: a low spotlight makes them more accurate than diffuse light on the same testbed views, consistent with more contrast and detected keypoints. SuperPoint with LightGlue is the fastest learned combination (16 ms per frame), and DINOv2 retrieval proposals still need geometric verification.

</details>

#### 2026-10-20 - Depth-guided Geometric Adaptation for Few-shot Image Classification

**Authors:** Zhiqi Miao, Estefanía Talavera, Weichuan Zhang, Jiapan Guo
**Links:** [abs](https://arxiv.org/abs/2610.28856) - [pdf](https://arxiv.org/pdf/2610.28856)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** monocular depth, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Depth-guided Geometric Adaptation for Few-shot Image Classification
- 作者：Zhiqi Miao, Estefanía Talavera, Weichuan Zhang, Jiapan Guo
- 出版日期：2026-10-20T19:29:42Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.28856 ；PDF https://arxiv.org/pdf/2610.28856

### 一句话总结
论文提出 DAFIC 框架，将单目深度引入少样本图像分类的表征学习、episodic adaptation 和密集支持集-查询集匹配，以缓解背景杂波与 RGB 外观相似导致的视觉歧义。

### 研究问题
少样本图像分类（FSIC）在数据稀缺条件下容易受到视觉歧义影响：背景杂波和 RGB 外观相似性会妨碍判别性特征匹配。论文旨在缓解这一问题。

### 核心思路/方法
DAFIC 是一个几何引导框架，包含三个要点：
1. 通过 RGB-D 自监督预训练学习几何感知的 token 表征；
2. 使用 Depth-guided Geometric Adaptation（DGA）模块，以深度导出的几何信息细化 patch 表征，引入几何丰富的类别上下文，同时抑制背景干扰；
3. 使用 Spatial Bidirectional Patch Matching（SBiM）对细化后的特征进行双向密集匹配，以降低对虚假对应和背景杂波的敏感性。

### 主要贡献
- 提出 DAFIC，将单目深度纳入少样本图像分类的表征学习、episodic adaptation 与密集支持集-查询集匹配。
- 提出 DGA 模块，利用深度几何细化 patch 表征并抑制背景干扰。
- 提出 SBiM，对细化特征进行双向密集匹配，降低对虚假对应和背景杂波的敏感性。
- 摘要称在四个基准上进行了大量实验，DAFIC 相较现有方法取得较强性能；消融与鲁棒性分析支持将几何条件化的 episodic adaptation 与双向匹配结合用于少样本视觉识别的有效性。

### 局限性
- 摘要未提供足够信息说明具体数据集名称、实验设置、量化指标和对比方法细节。
- 摘要未提供足够信息说明计算开销、推理效率或对深度质量/可用性的依赖程度。
- 摘要未提供足够信息说明失败案例、适用范围限制或是否存在明显性能瓶颈。

### 阅读优先级
中。理由：论文主题聚焦少样本图像分类中的视觉歧义与背景干扰，方法将单目深度与双向密集匹配结合，问题明确且模块设计清晰；但摘要仅给出总体性能结论，未提供具体实验数据与细节，需阅读全文后才能判断其实际效果与适用性。

</details>

<details>
<summary>Abstract</summary>

Few-shot image classification (FSIC) frequently suffers from visual ambiguity, where background clutter and RGB appearance similarities hinder discriminative feature matching in data-scarce settings. To mitigate this, we propose DAFIC, a geometry-guided framework that incorporates monocular depth into representation learning, episodic adaptation, and dense support-query matching. DAFIC first learns geometry-aware token representations through RGB-D self-supervised pre-training. Subsequently, the Depth-guided Geometric Adaptation (DGA) module uses depth-derived geometry to refine patch representations with geometry-enriched class context while suppressing background interference. Spatial Bidirectional Patch Matching (SBiM) then performs bidirectional dense matching on the refined features, reducing sensitivity to spurious correspondences and background clutter. Extensive experiments on four benchmarks show that DAFIC achieves strong performance against existing methods, with ablation and robustness analyses supporting the effectiveness of coupling geometry-conditioned episodic adaptation with bidirectional matching for few-shot visual recognition.

</details>

#### 2026-10-20 - VeriCalib: Verifiable Target-Based LiDAR-Camera Calibration

**Authors:** Xiangcheng Hu, Xieyuanli Chen, Feiyi Chen, Shengli Ren, Shiyang Chen, Guoqiang Ye, Hao Wang, Ping Tan, Steven L. Waslander, Fuchun Sun, Jin Wu
**Links:** [abs](https://arxiv.org/abs/2610.28791) - [pdf](https://arxiv.org/pdf/2610.28791)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VeriCalib: Verifiable Target-Based LiDAR-Camera Calibration
- 作者：Xiangcheng Hu, Xieyuanli Chen, Feiyi Chen, Shengli Ren, Shiyang Chen, Guoqiang Ye, Hao Wang, Ping Tan, Steven L. Waslander, Fuchun Sun, Jin Wu
- 出版日期：2026-10-20T18:21:00Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类）；次要分类：摘要未提供足够信息
- 链接：abstract_url: https://arxiv.org/abs/2610.28791；pdf_url: https://arxiv.org/pdf/2610.28791

### 一句话总结
该论文提出 VeriCalib，将基于标靶的 LiDAR-相机外参标定表述为可验证估计问题，并通过结构化协方差、方向精度解耦、一致性检查以及最小可检测偏差，输出可用于判断是否接受结果或如何采集数据的“标定状态”。

### 研究问题
论文指出，基于标靶的外参标定通常用拟合残差的均方根误差评估结果，但该标量误差在同一批观测上计算，因此无法说明应当接受结果，还是重新提取、重新采集或增加观测。论文希望解决的核心问题是：如何让外参标定结果具备可验证性，并能指示估计是否可靠以及数据采集应如何改进。

### 核心思路/方法
论文的关键观察是一个“两级外参补偿机制”：在残差层面，外参补偿每个观测误差中的刚性部分；在参数层面，旋转与平移相互补偿。因此，拟合残差既不能揭示观测与模型之间的不一致，也不能说明估计外参在每个方向上是否可靠。

为此，VeriCalib 采用结构化协方差评估标定，该协方差联合传播相机与 LiDAR 标靶特征的不确定性，并引入已知几何先验；其尺度作为方差分量从残差中估计。在该协方差基础上，方法解耦旋转与平移，以分析各方向精度，并引导数据采集朝向最弱方向。由于精度分析假设观测一致，论文进一步提出视图内检查与跨视图检查，分别检验内部残差和观测间刚性差异，并使用在未知噪声水平下仍保持显著性水平的阈值。论文还将最小可检测偏差扩展到外参，以界定各方向上可检测故障的下界。上述准则共同构成标定状态。

### 主要贡献
- 将基于标靶的外参标定表述为可验证估计问题，并输出标定状态，用于指示是否接受结果或如何采集数据。
- 揭示两级外参补偿机制导致拟合残差无法同时反映观测-模型不一致性与各方向可靠性。
- 提出结构化协方差方法，联合传播相机与 LiDAR 标靶特征不确定性并利用已知几何先验，且从残差估计方差分量尺度。
- 在协方差上解耦旋转与平移，以分析各方向精度并指导数据采集。
- 提出视图内与跨视图一致性检查，并给出在未知噪声水平下保持显著性水平的阈值。
- 将最小可检测偏差扩展到外参，以界定各方向最小可检测故障。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集、对比方法、定量结果、实时性、适用范围或失败案例等细节；因此无法基于摘要判断方法在真实场景中的精度、鲁棒性和计算开销。

### 阅读优先级
中。理由：该论文针对 LiDAR-相机外参标定的结果可验证性与数据采集指导提出明确问题，并给出协方差分析、一致性检查和最小可检测偏差等方法框架，对做多传感器标定与可信估计的研究者有参考价值；但摘要未提供实验验证细节与定量结果，是否值得优先精读需结合全文实验部分进一步判断。

</details>

<details>
<summary>Abstract</summary>

Target-based extrinsic calibration estimates the rigid transform between sensors from a few observations of a known target, and its result is commonly assessed by the root-mean-square error of the fitted residuals. However, this scalar error is computed on the same observations and therefore cannot indicate whether to accept the result, re-extract, recollect or add observations. This paper presents VeriCalib, which formulates extrinsic calibration as a verifiable estimation problem and reports a calibration state. The key insight is a two-level extrinsic compensation mechanism, in which the extrinsic compensates the rigid part of each observation error at the residual level, and rotation and translation compensate each other at the parameter level. Consequently, the fitted residual can reveal neither an inconsistency between the observations and the model nor whether the estimated extrinsic is reliable in every direction. Accordingly, we assess the calibration through a structured covariance that jointly propagates the uncertainty of the camera and LiDAR board features with a known-geometry prior, and estimate its scale as a variance component from the residuals. On this covariance, we decouple rotation and translation to resolve the precision along each direction and guide data collection toward the weakest one. Since this precision presumes consistent observations, we further develop within-view and cross-view checks that examine the internal residual and the rigid discrepancy between observations, respectively, with thresholds that hold their significance level under an unknown noise level. We also extend the minimal detectable bias to the extrinsic to bound the smallest detectable fault along each direction. These criteria form a calibration state that indicates whether to accept the result or how to collect the data...

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-26 - FL4N: Feed-forward Latent Model for 4D Novel View Synthesis

**Authors:** Eunbeen Hong, Hyeonseo Yu, Honggyu An, Jooho Son, Hyunah Ko, Soowon Son, Chaehyun Kim, Jahyeok Koo, Jisoo Kim, Junhwa Hur, Seungryong Kim
**Links:** [abs](https://arxiv.org/abs/2610.35854) - [pdf](https://arxiv.org/pdf/2610.35854)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, novel view synthesis, view synthesis, rendering

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
<summary>Abstract</summary>

Language-aware 3D Gaussian Splatting (3DGS) has advanced language-driven 3D scene understanding by incorporating semantic and relational cues into reconstructed scenes. However, relation-aware grounding depends not only on representing such information, but also on whether the underlying scene-side evidence is reliable and sufficient. Multi-view semantic aggregation can incorporate weak observations, while object relations can remain under-observed along the available camera trajectory, leading to ambiguous evidence for target disambiguation. We present RelateGS, a structured language-aware Gaussian representation that selectively refines semantic and relational evidence for 3D visual grounding. RelateGS suppresses unreliable observations during semantic feature uplifting and consolidates multi-view object observations into a persistent 3D graph. The graph further identifies under-observed object relations and guides targeted re-querying of informative existing frames to complement their evidence. Experiments on Sr3D+ and Nr3D demonstrate competitive 3D grounding performance, improving the previous best by 7.9 and 1.7 percentage points at Acc@0.25, respectively.

</details>

#### 2026-10-22 - RecallGS: Geometry-Grounded Recall for Online Semantic Gaussian Splatting

**Authors:** Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran
**Links:** [abs](https://arxiv.org/abs/2610.31293) - [pdf](https://arxiv.org/pdf/2610.31293)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RecallGS: Geometry-Grounded Recall for Online Semantic Gaussian Splatting
- 作者：Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran
- 出版日期：2026-10-22T13:55:31Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.31293 ；PDF https://arxiv.org/pdf/2610.31293

### 一句话总结
RecallGS 提出一种轻量、免训练的“召回—几何校验—融合”机制，从智能体历史观测中以非参数方式恢复几何—语义证据，用于在线语义 3D Gaussian Splatting，避免额外学习 3D 网络。

### 研究问题
在线语义 3D Gaussian Splatting（3DGS）可从流式观测中进行开放词汇场景理解。现有方法通常借助额外学习的 3D 网络来恢复图像语义特征中缺失的几何上下文，但会带来额外训练和运行时开销。论文关注的问题是：这类几何—语义证据是否已存在于智能体的观测历史中，能否通过“检索”而非“学习”获得。

### 核心思路/方法
论文观察到几何—语义证据可能已存在于智能体的观测历史中，因此将过去观测视为非参数化的几何—语义先验，提出 RecallGS。其流程为“recall–ground–fuse”：
1. 使用 CLIP 检索相关观测；
2. 利用 alpha 合成权重识别具有几何支撑的视角；
3. 在每个 Gaussian 的渲染覆盖区域上聚合这些视角的语义特征。
该机制被描述为轻量、免训练。

### 主要贡献
- 提出 RecallGS，一种轻量、免训练的机制，将历史观测作为非参数几何—语义先验，用于在线语义 3DGS。
- 设计“召回—几何校验—融合”流程：CLIP 检索、alpha 合成权重筛选几何支撑视角、按 Gaussian 渲染覆盖区域聚合语义特征。
- 在 ScanNet 和 ScanNet++ 上取得较强的语义分割性能，并以 2.48 FPS 运行，表明无需额外学习 3D 分支即可从观测历史中有效恢复几何—语义上下文。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、对检索质量的敏感性、内存或存储开销、与更多基线方法的完整比较，以及 2.48 FPS 对应的硬件配置等细节。

### 阅读优先级
中。理由：该工作针对在线语义 3DGS 中额外学习 3D 网络的开销问题，提出免训练的检索式替代思路，问题明确且方法流程清晰；摘要报告了 ScanNet/ScanNet++ 上的语义分割表现与 2.48 FPS 运行速度。但摘要未提供与现有方法的完整定量对比、消融实验和实现细节，是否值得优先精读需结合全文实验部分进一步判断。

</details>

<details>
<summary>Abstract</summary>

Online semantic 3D Gaussian Splatting (3DGS) enables open-vocabulary scene understanding from streaming observations. However, existing methods recover geometric context missing from image-derived semantic features using an additionally learned 3D network, incurring extra training and runtime overhead. We observe that such geometric-semantic evidence may already exist in the agent's observation history and can be retrieved rather than learned. Based on this insight, we introduce RecallGS (Geometry-Grounded Recall for Online Semantic Gaussian Splatting), a lightweight, training-free mechanism that treats past observations as a non-parametric geometric-semantic prior. RecallGS follows a recall-ground-fuse pipeline: CLIP retrieves relevant observations, alpha-compositing weights identify geometrically supported views, and aggregate their semantic features over each Gaussian's rendered footprint. On ScanNet and ScanNet++, RecallGS achieves strong semantic segmentation performance at 2.48 FPS, demonstrating that geometric-semantic context can be effectively recovered from observation history without an additional learned 3D branch.

</details>

#### 2026-10-22 - GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis

**Authors:** Henglei Lv, Bailin Deng, Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang, Lin Gao
**Links:** [abs](https://arxiv.org/abs/2610.30619) - [pdf](https://arxiv.org/pdf/2610.30619)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, relighting, rendering, radiance, AR, augmented reality, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis
- 作者：Henglei Lv, Bailin Deng, Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang, Lin Gao
- 出版日期：2026-10-22T02:31:54Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.30619 ；PDF https://arxiv.org/pdf/2610.30619 ；项目页 http://www.geometrylearning.com/GSHeadRelight/

### 一句话总结
论文提出 GSHeadRelight，面向 3D Gaussian 人头合成，设计基于统一神经辐射传输表示的光照模型，并借助 in-the-wild 图像实现重光照与更快渲染。

### 研究问题
论文关注人像的重光照与新视角合成，应用场景包括人像摄影、VR 和 AR。摘要指出，3D-aware 人像重光照仍具挑战，原因在于同时需要照片级真实渲染、实时性能和对外观未见过受试者的泛化能力。现有工作要么依赖有限且昂贵的光照棚采集数据做监督，要么结果不理想；不少方法基于生成式 NeRF，存在 3D 一致性差和实时性能低的问题。

### 核心思路/方法
论文利用生成式 3D Gaussian 的进展，设计一个基于统一神经辐射传输表示的光照模型，该表示对入射光呈线性响应。方法仅使用 in-the-wild 图像进行训练或建模，摘要未提供更具体的数据设置与实现细节。

### 主要贡献
- 面向 3D Gaussian 人头合成提出 GSHeadRelight，以提升重光照能力与速度。
- 设计基于统一神经辐射传输表示、对入射光线性响应的光照模型。
- 仅使用 in-the-wild 图像，摘要声称达到当时最优的重光照结果。
- 摘要声称相较此前 3D-aware 人像重光照研究，渲染速度显著更快（×12）。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、泛化边界、数据依赖范围、计算资源需求及定量实验设置；仅在 abstract 中提及不依赖昂贵光照棚监督并使用 in-the-wild 图像，但未展开其限制。

### 阅读优先级
中。理由：论文主题与 3D Gaussian 人头合成、重光照和实时渲染直接相关，摘要给出明确的速度提升与 SOTA 声称，适合关注人像重光照、VR/AR 与神经渲染的读者进一步核查；但摘要未提供实验细节和局限性说明，需阅读全文后再判断结论强度。

</details>

<details>
<summary>Abstract</summary>

Relighting and novel view synthesis of human portraits are essential in applications such as portrait photography, virtual reality (VR), and augmented reality (AR). Despite recent progress, 3D-aware portrait relighting remains challenging due to the demands for photorealistic rendering, real-time performance, and generalization to unseen subjects. Existing works either rely on supervision from limited and expensive light stage captured data or produce suboptimal results. Moreover, many works are based on generative NeRFs, which suffer from poor 3D consistency and low real-time performance. We resort to recent progress on generative 3D Gaussians and design a lighting model based on a unified neural radiance transfer representation, which responds linearly to incident light. Using only in-the-wild images, our method achieves state-of-the-art relighting results and a significantly faster rendering speed ($\times12$) compared to previous 3D-aware portrait relighting research. Project page: http://www.geometrylearning.com/GSHeadRelight/.

</details>

#### 2026-10-21 - SplatLab: Autonomous Scientific Discovery for 3DGS Research

**Authors:** Seemandhar Jain, Manmohan Chandraker
**Links:** [abs](https://arxiv.org/abs/2610.30468) - [pdf](https://arxiv.org/pdf/2610.30468)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatLab: Autonomous Scientific Discovery for 3DGS Research
- 作者：Seemandhar Jain, Manmohan Chandraker
- 出版日期：2026-10-21T21:30:32Z
- 分类：主分类 Neural Scene Representations & Rendering；次级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.30468 ；PDF https://arxiv.org/pdf/2610.30468

### 一句话总结
SplatLab 是面向 3D Gaussian Splatting 的自主研究系统，可在给定研究提示、目标论文链接或无输入的情况下，复现基线、提出扩展、训练与消融、撰写论文，并把每个报告数值绑定到已记录的训练运行。

### 研究问题
摘要指出，复现一篇已发表的 3DGS 论文需要数周专家工程工作，之后才能提出扩展；既有自主研究系统受限于短固定模板、低可执行性和弱可追溯性，且尚未在活跃的计算机视觉子领域中端到端展示。SplatLab 旨在解决这些限制。

### 核心思路/方法
摘要给出五个设计选择：
1. 候选方法从“已验证复现的骨架”出发，以插件形式变异，并与已发表基线匹配；
2. 在八个“岛”上运行级联加权 Elo 锦标赛，用实测 GPU PSNR 评分候选，并结合语言梯度反馈；
3. 设置常驻“证伪器”，失败时扣减 Elo，把压力测试存活情况纳入选择；
4. 每个报告数值绑定到已记录训练运行，且只要存在未支撑的主张，运行就不能终止；
5. 用七类 3DGS 分类法将 EVOLVE-BLOCK 标记包裹在领域对齐脚手架中，可跨 3DGS 仓库迁移。

系统流程包括：复现已发表基线、提出扩展、在 Mip-NeRF 360 和 LLFF 上训练与消融、撰写手稿、绑定数值到训练日志。

### 主要贡献
- 提出面向 3DGS 的自主研究系统 SplatLab，覆盖复现、扩展、训练、消融、写作与数值追溯的端到端流程。
- 给出五项设计选择：插件式候选变异、级联加权 Elo 锦标赛、常驻证伪器、数值与训练运行绑定、七类 3DGS 分类法脚手架。
- 在 PSNR 目标运行中，摘要称其手稿相对复现目标提升 +0.18 至 +3.78 dB，其中包括天体摄影星云渲染的 +3.78 dB，并称此前不存在该任务的 3DGS 方法。
- 摘要称研究周期从数月研究生时间压缩到数天、以自主计算为主；代码、手稿、实验账本和跨运行论文库见项目页。

### 局限性
摘要未提供足够信息说明以下内容：实验的完整设置与统计显著性、与其他人自主研究系统的定量对比、失败案例与适用范围、人工干预程度、计算资源开销、跨仓库分类法脚手架的泛化验证细节、LLFF 与 Mip-NeRF 360 上的逐项结果，以及“无输入”模式的具体表现。摘要仅给出 PSNR 目标运行的总体提升区间和一个星云渲染案例，未提供完整实验细节。

### 阅读优先级
中。理由：该工作涉及 3DGS 与自主科研系统交叉，摘要提供了较清晰的方法框架和可追溯性设计，并对活跃视觉子领域做端到端演示；但摘要未给出完整实验细节、对比基线和失败分析，是否值得深入阅读取决于读者对自主研究流程、3DGS 自动化实验或数值可追溯机制的关注程度。

</details>

<details>
<summary>Abstract</summary>

Reproducing a published 3DGS paper takes weeks of expert engineering before any extension can be proposed. Prior autonomous-research systems read papers, draft hypotheses, and write code, but are limited by short fixed templates, low executability, and weak traceability, and none has been demonstrated end-to-end in a live computer-vision subfield with intense activity. SplatLab is an autonomous research system for 3D Gaussian Splatting that addresses these limitations. Given a research prompt, a target-paper URL, or no input at all, it reproduces a published baseline, proposes an extension, trains and ablates across Mip-NeRF 360 and LLFF, writes the manuscript, and binds every reported number to a logged training run. Five design choices distinguish it: (i) candidates mutate plugins from a verified-reproduction backbone matched to published baselines; (ii) a cascade-weighted Elo tournament across eight islands scores candidates on measured GPU PSNR with verbal-gradient feedback; (iii) a standing falsifier subtracts Elo on failure, integrating stress-test survival into selection; (iv) every reported number is bound to a logged training run, and the run cannot terminate while any claim is unbacked; (v) a seven-category 3DGS taxonomy wraps EVOLVE-BLOCK markers in domain-aligned scaffolds transferable across 3DGS repositories. On PSNR-targeted runs, SplatLab's manuscripts beat their reproduced targets by +0.18 to +3.78 dB, including +3.78 dB on astrophotographic nebula rendering, for which no prior 3DGS method exists. The research cycle compresses from months of graduate-student time to days of mostly autonomous compute. Code, all manuscripts, experiment ledgers, and the cross-run paper store are available on the project page.

</details>

#### 2026-10-21 - TerraTransfer++: Demonstration-Free End-to-End Planner

**Authors:** Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan
**Links:** [abs](https://arxiv.org/abs/2610.30319) - [pdf](https://arxiv.org/pdf/2610.30319)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TerraTransfer++: Demonstration-Free End-to-End Planner
- 作者：Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan
- 出版日期：2026-10-21T18:31:28Z
- 分类：主分类为 Neural Scene Representations & Rendering；无次级分类
- 链接：摘要页 https://arxiv.org/abs/2610.30319 ；PDF https://arxiv.org/pdf/2610.30319

### 一句话总结
论文提出一种不依赖人工专家演示的端到端自动驾驶训练框架：先在向量化仿真器中通过自博弈预训练策略，再将其蒸馏为流匹配轨迹教师，并在冻结视觉主干上训练轻量适配器，得到闭环策略与规划器两个学生模型。

### 研究问题
端到端自动驾驶的标准训练范式成本高昂：模仿学习依赖车队规模驾驶日志，且行为分布对安全关键长尾覆盖稀薄；照片级仿真器中的闭环强化学习受样本效率、逐步渲染成本和大型视觉主干前向计算限制。论文关注能否在不使用人工专家演示、也不依赖日志轨迹监督对齐的情况下，获得具备自然多样行为与高反应性的端到端策略与规划器。

### 核心思路/方法
论文利用向量化仿真器自博弈的效率优势：在每秒数百万 rollout 步的规模下，获得包含碰撞、近失误与恢复等自然多样性的状态分布，并由基础驾驶质量奖励产生高反应性策略。方法分三步：
1. 通过自博弈预训练单一策略；
2. 将其 rollout 蒸馏为同时具备规划能力的流匹配轨迹教师；
3. 在冻结的预训练视觉主干上训练轻量适配器，通过动作 KL 散度、批关系低秩结构损失，以及面向规划器的轨迹匹配损失，复现教师的潜空间。
所有监督目标均回溯到自博弈策略，因此对齐过程从不以日志轨迹为监督；仅需成对的（图像、场景状态）帧数据集，无需整理好的专家演示。由同一自博弈教师得到两个端到端学生：闭环策略与规划器。

### 主要贡献
- 提出无演示的端到端训练路线，避免模仿学习对车队规模驾驶日志与专家演示的依赖，也规避照片级仿真器闭环强化学习的样本效率与渲染成本瓶颈。
- 设计从自博弈策略到流匹配轨迹教师的蒸馏流程，并在冻结视觉主干上以多种损失训练轻量适配器，实现潜空间对齐。
- 从单一自博弈教师产出两个学生模型：闭环策略在照片级 3D Gaussian splatting 闭环基准 HUGSim 上优于所有已发表的基于模仿的端到端方法；规划器在 NAVSIM navhard 上达到 59.4 EPDMS，高于包括 DriveZero-Scale（57.1）在内的所有已发表方法，在 navtest 上达到 95.5 PDMS，且不使用人类演示。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、计算开销、跨场景泛化边界、安全保证或消融实验细节。摘要未提供足够信息说明自博弈奖励设计细节、教师蒸馏的稳定性条件，以及在不同传感器配置或真实部署中的表现。

### 阅读优先级
高。理由：论文直接针对端到端自动驾驶训练成本与专家演示依赖这一核心瓶颈，给出无需人工演示的统一训练框架，并在 HUGSim、NAVSIM navhard 与 navtest 上报告了优于已发表方法的定量结果；若关注端到端规划、自博弈仿真训练或教师-学生蒸馏，该工作具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all existing paradigms: imitation learning requires fleet-scale driving logs whose behavior distribution only thinly covers the safety-critical tail; closed-loop reinforcement learning in a photorealistic simulator, while offering diverse behaviors, is bottlenecked by sample-efficiency, per-step cost of rendering, and a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: at millions of rollout steps per second, one can obtain a state distribution with natural diversity in collisions, near-misses, and recoveries that no driving log contains, and a highly reactive policy emerges from a basic driving-quality reward. Our approach exploits this asymmetry. We pretrain a single policy by self-play, distill its rollouts into a flow-matching trajectory teacher that also plans, and train lightweight adapters on a frozen pretrained vision backbone to reproduce the latent space of either teacher through the action KL divergence, a batch-relational low-rank structural loss, and, for the planner, a trajectory-matching loss. Every target traces back to the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. From this one self-play teacher we obtain two end-to-end students: a closed-loop policy that outperforms every published imitation-based end-to-end method on the photorealistic 3D Gaussian splatting closed-loop benchmark HUGSim, and a planner that reaches 59.4 EPDMS on NAVSIM navhard, above every published method including DriveZero-Scale (57.1), and 95.5 PDMS on navtest, without human demonstrations.

</details>

#### 2026-10-21 - ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization

**Authors:** Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin
**Links:** [abs](https://arxiv.org/abs/2610.30013) - [pdf](https://arxiv.org/pdf/2610.30013)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization
- 作者：Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin
- 出版日期：2026-10-21T16:43:53Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.30013；PDF https://arxiv.org/pdf/2610.30013

### 一句话总结
ClunoGS 提出一个面向 Language 3D Gaussian Splatting 的紧凑化框架，通过语义感知的高斯稀疏化与向量量化统一优化，在压缩模型存储的同时尽量保持开放词汇语义预测能力。

### 研究问题
Language 3DGS 通过为高斯基元关联语言特征来支持开放词汇场景理解，但这些语义属性会增加模型存储。现有 3DGS 压缩方法主要面向 RGB 渲染质量；若顺序执行稀疏化和量化，仅依据渲染质量剪枝可能删除 RGB 贡献小但对语义预测重要的高斯，且被删除后的语义信息无法由后续量化恢复。因此，问题是如何在压缩 Language 3DGS 时同时兼顾渲染质量、语义准确性和紧凑性，避免语义无关剪枝与顺序压缩造成语义表示退化。

### 核心思路/方法
论文将语义感知的高斯稀疏化与向量量化结合为一个统一的约束目标，并在稀疏化过程中使用语义监督。该统一目标同时考虑渲染质量、语义准确性和紧凑性，并通过交替进行原始变量更新、稀疏化、量化和对偶更新来优化。方法的核心是避免“先按渲染质量剪枝、再量化”的顺序式压缩，因为这种语义无关的稀疏化会不可逆地丢失对语义预测重要但 RGB 贡献较小的高斯信息。

### 主要贡献
- 提出 ClunoGS，一个面向 Language 3DGS 的紧凑框架，将语义感知高斯稀疏化与向量量化纳入统一约束目标。
- 在稀疏化中引入语义监督，使剪枝不只依据渲染质量，从而减少对语义重要高斯的误删。
- 设计交替优化流程，联合更新原始变量、稀疏化、量化和对偶变量。
- 在 LERF 和 ScanNet-10 基准上评估开放词汇定位与分割；摘要称在激进压缩下，该统一语义感知表述显著缓解了顺序压缩和语义无关稀疏化导致的语义表示退化。
- 消融结果显示，联合协调稀疏化与量化比独立应用二者更能保持语义准确率。

### 局限性
摘要未提供足够信息说明计算开销、训练时间、压缩率与存储节省的具体数值、不同压缩强度下的完整定量结果、对语言特征类型的依赖、超参数敏感性，以及方法在其他 3DGS 变体或更大场景上的泛化表现。摘要未提供足够信息给出与具体基线方法的逐项数值对比细节。

### 阅读优先级
中。理由：该论文关注 Language 3DGS 的存储压缩与语义保持之间的冲突，问题定义清晰，统一优化和语义感知剪枝的思路对 3DGS 压缩与开放词汇场景理解交叉方向有参考价值；但摘要仅给出任务级评估和消融结论，缺少具体压缩率、精度数值和效率数据，是否值得优先精读需结合全文实验细节再判断。

</details>

<details>
<summary>Abstract</summary>

Language 3D Gaussian Splatting enables open-vocabulary scene understanding by associating Gaussian primitives with language features. These semantic attributes increase model storage, while most existing 3DGS compression methods are designed mainly to preserve RGB rendering quality. One straightforward approach is to apply sparsification and quantization sequentially. However, pruning based only on rendering quality can remove Gaussians that have small RGB contributions but are important for semantic prediction. Once removed, their semantic information cannot be recovered by later quantization. We propose ClunoGS, a compact framework for Language 3DGS that combines semantics-aware Gaussian sparsification and vector quantization in a unified constrained objective. Semantic supervision is used during sparsification, and the objective jointly considers rendering quality, semantic accuracy, and compactness. We optimize the unified objective with alternating primal, sparsification, quantization, and dual updates. We evaluate ClunoGS on open-vocabulary localization and segmentation using the LERF and ScanNet-10 benchmarks. Under aggressive compression, our unified, semantics-aware formulation substantially alleviates the degradation of semantic representations caused by sequential compression and semantics-agnostic Gaussian sparsification. Ablations further show that jointly coordinating sparsification and quantization better preserves semantic accuracy than applying them independently.

</details>

#### 2026-10-21 - AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments

**Authors:** Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Mingsheng Li, Qingsong Yan, Chao Yan, Yuhang Zhang, Mir Feroskhan
**Links:** [abs](https://arxiv.org/abs/2610.29699) - [pdf](https://arxiv.org/pdf/2610.29699)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments
- 作者：Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Mingsheng Li, Qingsong Yan, Chao Yan, Yuhang Zhang, Mir Feroskhan
- 出版日期：2026-10-21T13:13:00Z
- 分类：主分类为 Neural Scene Representations & Rendering；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.29699 ；PDF https://arxiv.org/pdf/2610.29699

### 一句话总结
论文提出 AirPlayground，一个面向空中导航策略训练与评估的统一基准，包含 94 个真实感重建环境、自动化专家飞行数据采集流程、可扩展 API，以及多范式基线在已见/未见环境中的闭环评测。

### 研究问题
现有大规模空中资源在两方面存在局限：（1）缺少面向不同策略形式的密集采样飞行演示；（2）缺少覆盖广泛环境、可用于标准化闭环评估的资源。论文希望解决空中导航策略训练数据与标准化闭环评测环境不足的问题。

### 核心思路/方法
论文构建 94 个真实感 3D Gaussian Splatting（3DGS）环境，覆盖室内、城市户外和植被场景，并配有对齐的碰撞几何。基于这些环境，论文开发场景自适应流程自动采集专家飞行数据，得到 94K 演示和 46.5M 同步的观测-状态-动作样本，频率为 50 Hz。论文还提供可扩展 API，支持在共享语料上训练不同策略形式，并在对应环境中按统一协议评估。论文在三种导航设置、已见和未见环境中对四类策略范式的七个基线进行基准测试，并进一步考察 ACT 的规模扩展行为；同时分析离线预测误差与闭环结果之间的关系。

### 主要贡献
- 构建 94 个真实感 3DGS 空中导航环境，覆盖室内、城市户外和植被场景，并提供对齐碰撞几何。
- 提出场景自适应自动化专家飞行采集流程，产出 94K 演示和 46.5M 同步观测-状态-动作样本（50 Hz）。
- 提供可扩展 API，支持不同策略形式的训练与统一协议下的闭环评估。
- 建立跨三种导航设置、四类策略范式、七个基线的已见/未见环境基准测试。
- 给出 ACT 的规模扩展结果：训练语料从 5 个场景扩展到 70 个场景，已见和未见环境的中位成功率分别从 30.6% 和 16.8% 提升到 41.2% 和 29.4%。
- 分析离线预测误差、执行协议和场景交互对闭环性能的作用。

### 局限性
摘要未提供足够信息。摘要未说明环境重建精度、数据采集成本、基线覆盖范围之外的泛化性、真实世界部署差距或计算资源需求等局限。

### 阅读优先级
中。理由：该论文聚焦空中导航基准、3DGS 重建环境、大规模专家演示与闭环评估，问题定义和资源贡献较明确；但摘要未提供具体方法细节、基线配置和局限分析，是否适合深入阅读取决于读者对空中导航基准、3DGS 场景资源或闭环策略评估的兴趣。

</details>

<details>
<summary>Abstract</summary>

Large-scale aerial resources provide a foundation for learning navigation across diverse environments. However, existing resources remain limited in providing (1) densely sampled flight demonstrations for learning different policy formulations and (2) broad environment coverage for standardized closed-loop evaluation. To address these limitations, we introduce AirPlayground, a unified benchmark for training and evaluating aerial navigation policies across diverse environments. We first construct 94 photorealistic 3D Gaussian Splatting (3DGS) environments spanning indoor, urban outdoor, and vegetation settings, with aligned collision geometry. Building on these environments, we develop a scene-adaptive pipeline for automated expert flight collection, yielding 94K demonstrations and 46.5M synchronized observation-state-action samples at 50 Hz. We further provide an extensible API that supports training different policy formulations on this shared corpus and evaluating them under unified protocols in the corresponding environments. We benchmark seven baselines spanning four policy paradigms across three navigation settings in seen and unseen environments, and further examine scaling behavior with ACT. Scaling ACT's training corpus from 5 to 70 scenes raises median success rates on seen and unseen environments from 30.6% and 16.8% to 41.2% and 29.4%, respectively. Through this shared training and evaluation framework, AirPlayground supports analysis of how offline prediction errors relate to closed-loop outcomes. Our analyses highlight the roles of prediction errors, execution protocols, and scene interactions in closed-loop performance.

</details>

#### 2026-10-21 - AutoPhyX: Automatic Text-Condition Physics Property Generation

**Authors:** Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang
**Links:** [abs](https://arxiv.org/abs/2610.29517) - [pdf](https://arxiv.org/pdf/2610.29517)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AutoPhyX: Automatic Text-Condition Physics Property Generation
- 作者：Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang
- 出版日期：2026-10-21T10:05:23Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.29517 ；PDF https://arxiv.org/pdf/2610.29517

### 一句话总结
AutoPhyX 是一个文本条件驱动的框架，用于预测空间变化的物理属性，以支持高保真 4D 物理仿真中的物理参数分配。

### 研究问题
论文针对高保真 4D 物理仿真中“准确物理参数分配”的难题。摘要指出已有方法存在两个瓶颈：一是依赖计算密集的逐场景优化；二是仅从纯视觉输入预测参数，存在固有歧义，例如仅凭橡胶外观无法区分其刚度。因此，研究问题是如何在避免上述瓶颈的情况下，为多样化材质属性生成与语义和物理一致的参数分配。

### 核心思路/方法
摘要给出的核心思路包括：
1. 提出文本条件框架 AutoPhyX，用于预测空间变化的物理属性。
2. 由于训练稳健的前馈模型需要细粒度监督，作者首先引入一种“部件可控的数据生成流程”，将复杂 3D 资产分解为语义上不同的组件，并为它们配对物理上合理、多样的参数及对应文本描述。
3. 基于该数据，AutoPhyX 采用跨模态调制机制，使文本特征动态调制视觉特征，以实现精确的物理 grounding。
4. 方法将属性预测构建在体素场中，从而兼容多种 3D 表示，包括网格、点云、Gaussian Splatting 和 NeRF。
5. 摘要称实验表明该方法可在单次前向传播中实现物理上合理、文本驱动的参数分配，并对野外物体具有较高准确率和稳健泛化能力。

### 主要贡献
- 提出 AutoPhyX，一个文本条件驱动的空间变化物理属性预测框架。
- 引入部件可控的数据生成流程，用于生成带细粒度监督的 3D 资产、物理参数与文本描述配对数据。
- 设计跨模态调制机制，利用文本特征动态调制视觉特征以进行物理 grounding。
- 将属性预测表述在体素场中，以兼容多种 3D 表示形式。
- 摘要声称方法支持单次前向传播的文本驱动参数分配，并具备较高准确率和对野外物体的泛化能力。

### 局限性
摘要未提供足够信息。论文摘要未说明方法的具体失败情形、数据生成流程的适用范围、计算成本、对文本描述质量的敏感性，也未给出实验设置、定量指标和对比基线的细节。

### 阅读优先级
中。理由：该论文关注文本条件物理属性预测与 4D 物理仿真参数分配，问题定义清晰，且提出数据生成与跨模态调制思路；但当前仅有摘要和元数据，缺少实验细节与定量结果，是否值得优先精读需结合全文中的实验充分性与实际应用价值进一步判断。

</details>

<details>
<summary>Abstract</summary>

High-fidelity 4D physical simulation requires accurate physical parameter assignments that align with diverse material properties. Previous methods struggle with critical bottlenecks: they either rely on computationally intensive per-scene optimization or predict parameters from purely visual inputs. The latter suffers from inherent ambiguity, e.g., the inability to distinguish the stiffness of rubber from its appearance alone. To bridge this gap, we propose AutoPhyX, a text-conditioned framework for predicting spatially-varying physical properties. Since training robust feed-forward models requires fine-grained supervision, we first introduce a novel part-controllable data generation pipeline that decomposes complex 3D assets into semantically distinct components and pairs them with physically plausible, diverse parameters and corresponding text descriptions. Leveraging this dataset, AutoPhyX employs a cross-modal modulation mechanism where text features dynamically modulate visual features for precise physical grounding. By formulating property prediction within a voxel field, AutoPhyX ensures compatibility with diverse 3D representations, including meshes, point clouds, Gaussian Splatting, and NeRF. Experiments demonstrate that our method enables physically plausible, text-driven parameter assignment in a single forward pass. It achieves high accuracy and robust generalization to in-the-wild objects, paving the way for future physics-intensive embodied and robotic applications.

</details>

#### 2026-10-21 - AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting

**Authors:** Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin
**Links:** [abs](https://arxiv.org/abs/2610.29374) - [pdf](https://arxiv.org/pdf/2610.29374)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting
- 作者：Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin
- 出版日期：2026-10-21T08:02:14Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.29374) / [PDF](https://arxiv.org/pdf/2610.29374)

### 一句话总结
AOV-GS 是一个基于 3D Gaussian Splatting 的主动建图系统，借助冻结的 SAM 与 CLIP 基础模型，把探索过程引向语义信息更丰富的视角，并在离线拟合轻量语言场后支持新视角上的开放词汇文本查询分割。

### 研究问题
论文面向部署在人类环境中的机器人建图需求：地图既要支持几何导航，也要支持超出固定标签集的开放词汇语义查询。关键挑战在于，如何在不依赖人工标注分割掩码、也不依赖闭集语义类别的情况下，为地图补充语义信息。摘要指出，现有几何驱动的主动建图只最大化覆盖，语义只是采集轨迹的被动副产品；而主动语义建图通常依赖有监督语义分割。

### 核心思路/方法
- 使用冻结的基础模型引导探索：SAM 提供实例分割掩码，CLIP 提供与语言对齐的嵌入。
- 在粗探索阶段，对几何上有前景的候选视角，根据 CLIP 掩码嵌入的新颖性重新排序，使探索偏向语义信息丰富的区域。
- 建图全过程由冻结的 SAM 和 CLIP 提供实例掩码与语言对齐嵌入。
- 离线拟合一个轻量、场景特定的语言场，直接拟合已采集的 CLIP 嵌入，而不依赖人工标注掩码，从而在新视角上实现开放词汇文本查询分割。
- 在受控比较中，使用相同的 SAM-CLIP 感知栈，与仅几何的主动规划对比。

### 主要贡献
- 提出 AOV-GS：一个主动 3D Gaussian 建图系统，用冻结基础模型引导探索，并构建开放词汇语义地图。
- 将主动探索从单纯几何覆盖转向语义信息新颖性：用 SAM 实例分割和 CLIP 掩码嵌入计算候选视角的语义新颖性并重排序。
- 以离线拟合场景特定语言场的方式，把 CLIP 嵌入转化为可文本查询的分割能力，避免人工标注掩码。
- 摘要报告：在 Replica 八个场景上，语言场平均 mIoU 较仅几何主动规划提升 1.3 个百分点，达到 34.6%；在 Matterport3D 五个场景上提升 1.8 个百分点，达到 23.1%。使用 CorrCLIP 时，Replica 上达到 35.6%，比匹配的 Geometry-based + CorrCLIP 基线高 2.0 个百分点。两个数据集上新视角 PSNR 与仅几何基线相当，Replica 上深度 L1 改善。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性或在线部署约束。
- 摘要未提供足够信息说明对 SAM/CLIP 失败情形、掩码噪声或开放词汇范围外查询的鲁棒性。
- 摘要未提供足够信息说明除 Replica 与 Matterport3D 外的泛化表现，也未说明真实机器人平台实验。
- 摘要未提供足够信息说明语言场离线拟合所需时间、数据规模及超参数敏感性。
- 摘要未提供足够信息说明与依赖有监督语义分割的主动语义建图方法的直接对比。

### 阅读优先级
中。理由：论文主题同时涉及 3D Gaussian Splatting、主动建图与开放词汇语义，和主分类及机器人应用次分类直接相关；摘要给出了明确的受控对比与量化增益，方法路线清晰。但增益幅度相对有限，摘要层面的分析更偏系统整合与探索重排序；若关注开放词汇机器人建图或主动语义探索，值得阅读；若只关注大幅性能突破，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Robots deployed in human-centered environments need maps that support both geometric navigation and open-vocabulary semantic queries beyond a fixed label set. A key challenge is enriching such maps with semantic information without relying on manually annotated segmentation masks or closed-set semantic categories. Existing geometry-driven active mapping maximizes coverage but treats semantics as a passive by-product of the collected trajectory, whereas active semantic mapping typically depends on supervised semantic segmentation. We present AOV-GS, an active 3D Gaussian mapping system that guides exploration using frozen foundation models. During coarse exploration, AOV-GS re-ranks geometrically promising candidate views according to CLIP mask-embedding novelty computed from SAM instance segmentation, biasing exploration toward semantically informative regions. Frozen SAM and CLIP provide instance masks and language-aligned embeddings throughout mapping, while a lightweight scene-specific language field is fitted offline directly to the collected CLIP embeddings rather than manually annotated masks, enabling open-vocabulary text-query segmentation on novel views. In a controlled comparison using the same SAM-CLIP perception stack, AOV-GS improves average language-field mIoU over geometry-only active planning by 1.3 percentage points on Replica (34.6% on eight scenes) and by 1.8 points on Matterport3D (23.1% on five scenes). With CorrCLIP, AOV-GS reaches 35.6% on Replica, 2.0 points above the matched Geometry-based + CorrCLIP baseline. Novel-view PSNR remains comparable to the geometry-only baseline on both datasets while depth L1 improves on Replica. Code is available at https://github.com/OptimusFaber/AOV-GS.

</details>

#### 2026-10-21 - DriftNeRF: Cross-Ray Density Drifting for Sparse-View Neural Radiance Fields

**Authors:** Juntang Wang, Yihan Wang, Sheng'en Li, Hao Wu, Dongmian Zou, Shixin Xu
**Links:** [abs](https://arxiv.org/abs/2610.29106) - [pdf](https://arxiv.org/pdf/2610.29106)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DriftNeRF: Cross-Ray Density Drifting for Sparse-View Neural Radiance Fields
- 作者：Juntang Wang, Yihan Wang, Sheng'en Li, Hao Wu, Dongmian Zou, Shixin Xu
- 出版日期：2026-10-21T02:49:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.29106) / [PDF](https://arxiv.org/pdf/2610.29106)

### 一句话总结
论文指出稀疏视角下 NeRF 的渲染损失逐射线独立求和、缺少跨射线密度一致性约束，并提出即插即用的 DriftNeRF 正则项，通过跨射线密度漂移场抑制无支撑的密度分歧。

### 研究问题
NeRF 在稠密图像集合下可合成逼真新视角，但在可用视角很少时质量急剧下降。作者将这一缺陷归因于优化目标本身：渲染损失是对独立射线的求和，不包含比较不同射线对同一空间区域所赋予密度的项，因此邻近 3D 点可能在每个训练像素都被正确重建的同时收敛到相互矛盾的密度。论文关注的核心问题是：能否显式度量并约束这种跨射线密度不一致，从而提升稀疏视角 NeRF 的表现。

### 核心思路/方法
作者在训练中直接测量“跨射线密度不一致”（cross-ray density disagreement），并报告其在原始 NeRF 中保持较高、在基于频率的正则化下仅偶然下降、且在稀疏情形下与留出集质量同向变化。基于此，论文提出 DriftNeRF：一个在密度采样上实例化“漂移场”（drifting-field）模板的即插即用正则项。具体地，一个带掩码的指数核将其他射线上邻近点的密度聚合为 stop-gradient 的共识目标，由此得到的漂移场惩罚缺乏支撑的密度分歧，同时保留已被一致认同的边界。该正则项只读取采样位置、射线标识和预测密度，因此不需要预训练模型、外部几何或额外图像，并可跨场参数化迁移。

### 主要贡献
- 将稀疏视角 NeRF 的一个具体、可度量的缺陷归因于渲染目标：逐射线独立求和，缺少跨射线密度比较项。
- 在训练中显式度量跨射线密度不一致，并观察其在原始 NeRF 中较高、在频率正则化下仅偶然下降、且与稀疏情形下的留出质量同向变化。
- 提出 DriftNeRF 正则项：以掩码指数核聚合邻近其他射线密度，形成 stop-gradient 共识目标，惩罚无支撑分歧并保留一致边界。
- 该正则项无需预训练模型、外部几何或额外图像，且可跨场参数化迁移。
- 摘要报告：在 NeRF-Synthetic 上将残余分歧降低一个数量级；在 NeRF-Synthetic、DTU、LLFF 上，3 视角 PSNR 相比最强 MLP-NeRF 基线提升 0.42–0.65 dB；在匹配协议下与稀疏视角 Gaussian 流程相比具有竞争力，且不使用其深度、光流或共视预处理。

### 局限性
- 摘要未提供足够信息说明计算开销、训练时间或显存占用的具体影响。
- 摘要未提供足够信息说明核函数尺度、掩码阈值等超参数的选择与敏感性分析。
- 摘要未提供足够信息说明在视角数进一步减少（如 2 视角或单视角）时的表现。
- 摘要未提供足够信息说明与 Gaussian 流程比较时“匹配协议”的具体定义及公平性细节。
- 摘要未提供足够信息说明在动态场景、大尺度场景或非合成数据上的泛化边界。
- 摘要未提供足够信息说明失败案例或与频率正则化组合时的相互作用。

### 阅读优先级
高。理由：论文将稀疏视角 NeRF 的性能缺陷明确归因于渲染目标缺少跨射线密度一致性项，并给出可度量指标与即插即用正则项；摘要报告了数量级的分歧下降和一致的 PSNR 增益，且方法不依赖预训练模型、外部几何或额外图像，问题定位清晰、方法约束少，对稀疏视角神经渲染方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Neural Radiance Fields (NeRF) synthesize photorealistic novel views from dense image collections, but degrade sharply when few views are available. We attribute a specific, measurable defect to the objective itself: the rendering loss is a sum over independent rays and contains no term comparing densities that different rays assign to the same region of space, so nearby 3D points can settle on contradictory densities while every training pixel is reproduced correctly. We make this quantity explicit by measuring cross-ray density disagreement directly during training, and show that it stays high in vanilla NeRF, falls only incidentally under frequency-based regularization, and moves together with held-out quality in the sparse regime. We then close the gap with DriftNeRF, a drop-in regularizer that instantiates the drifting-field template on density samples: a masked exponential kernel aggregates densities from nearby points on other rays into a stop-gradient consensus target, and the resulting drifting field penalizes unsupported disagreement while leaving agreed-upon boundaries intact. The regularizer reads only sampled positions, ray identifiers, and predicted densities, so it requires no pretrained model, external geometry, or additional images, and transfers across field parameterizations. On NeRF-Synthetic it reduces residual disagreement by an order of magnitude, and across NeRF-Synthetic, DTU, and LLFF it improves 3-view PSNR over the strongest MLP-NeRF baseline by 0.42-0.65 dB and remains competitive with sparse-view Gaussian pipelines under a matched protocol without their depth, flow, or covisibility preprocessing.

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-26 - Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data

**Authors:** Dianyi Yang, Mengya Liu, Zhumei Wang, Yu Liu, Xiaochen Zhang, Yixuan Li, Le Ma, Yuhang Yang, Weiqi Huang, Wei Liang, Baoxiong Jia, Siyuan Huang
**Links:** [abs](https://arxiv.org/abs/2610.35075) - [pdf](https://arxiv.org/pdf/2610.35075)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

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
<summary>Abstract</summary>

WiFi Channel State Information (CSI) enables fine-grained sensing of spatial relationships between wireless devices. The WiFi Sensor for Robotics (WSR) toolbox demonstrated that WiFi-CSI measurements collected during robot motion, combined with odometry, can be used to synthesize virtual antenna arrays, enabling motion-induced bearing estimation in multi-robot experiments. However, deploying the WSR approach has remained challenging due to its limited integration with standard robotics tools and reliance on deprecated WiFi-CSI acquisition hardware. This work presents an open-source simulation framework that integrates the WSR sensing pipeline within the robotic simulator Gazebo. The framework generates synthetic WiFi-CSI measurements with realistic physical signal properties and leverages realistic robot motion required for motion-induced sensing and downstream localization. It further supports processing both simulated and real WiFi-CSI data for direct comparison and validation. Our aim is to make WSR-style sensing accessible as a modular sensing modality for robotic research. We validate our framework by comparing simulated and real-world experiments using TurtleBot3 robots, and demonstrate its use for bearing estimation and robot localization. This work lowers the barrier to entry for WiFi-CSI-based sensing in multi-robot systems and provides a foundation for integrating WiFi-CSI sensing with multi-modal perception for localization and coordination. All code and experimental details are publicly available at https://github.com/baharhaghighat/DARS_2026_Dijkstra_et_al

</details>

#### 2026-10-22 - Skeleton-Grounded Latent Action Model for Robot World Models

**Authors:** Qi Lv, Jiayi Lin, Yuxin Jiang, Jianzong Wang, Xiang Deng, Mike Shou Zheng
**Links:** [abs](https://arxiv.org/abs/2610.31474) - [pdf](https://arxiv.org/pdf/2610.31474)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** video reconstruction, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Skeleton-Grounded Latent Action Model for Robot World Models
- 作者：Qi Lv, Jiayi Lin, Yuxin Jiang, Jianzong Wang, Xiang Deng, Mike Shou Zheng
- 出版日期：2026-10-22T16:01:33Z
- 分类：Embodied / Robotics / AR Applications（主分类）；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.31474 ；PDF https://arxiv.org/pdf/2610.31474

### 一句话总结
SkeLAM 提出用机器人骨架监督把潜在动作分解为运动学分量与残差分量，以改善机器人世界模型中潜在动作与机器人控制之间的对应关系，并支持从当前观测和机器人动作生成未来观测。

### 研究问题
机器人世界模型需要模拟环境如何随机器人动作演化。潜在动作模型可以从视频中通过把视觉变化编码为代理动作来学习动力学，但摘要指出：由重建驱动的潜在动作会把机器人运动与物体响应及其他场景变化混在一起，使其难以与机器人控制对应。SkeLAM 针对的正是这一“潜在动作与机器人控制对应不清”的问题，目标是在可控机器人世界建模中让潜在动作更具运动学可解释性和可控制性。

### 核心思路/方法
- 将潜在动作分解为两部分：由机器人骨架监督锚定的运动学分量，以及保留互补视觉动态的残差分量。
- 采用跨模态交换重建，鼓励 RGB 导出的运动学表示与骨架导出的运动学表示在视频重建过程中可以互换。
- 世界模型通过两条独立的条件通路分别引入上述两个分量，并使用 branch dropout 降低模型对未来导出的残差信息的依赖。
- 使用轻量适配器把机器人动作映射到运动学空间，再通过世界模型微调使生成适应这些预测条件。
- 推理时，模型根据当前观测和机器人动作生成未来观测。
- 摘要报告在 DROID 上相较 DreamDojo，末端执行器 ADE 降低 19.5%，LPIPS 降低 11.1%；运动探测支持运动学专门化；定性结果显示生成 rollout 中具备零样本人类到机器人运动迁移；策略评估显示预测成功率与真实机器人执行测得成功率一致。

### 主要贡献
- 提出 SkeLAM：一种骨架引导的潜在动作模型，用于可控机器人世界建模。
- 通过骨架监督将潜在动作拆分为运动学分量与残差分量，缓解重建驱动潜在动作混合机器人运动与场景变化的问题。
- 引入跨模态交换重建，促进 RGB 与骨架两种来源的运动学表示在视频重建中可互换。
- 在世界模型中以独立条件通路整合两类分量，并用 branch dropout 减少对未来残差信息的依赖。
- 使用轻量适配器连接机器人动作与运动学空间，并通过微调适配预测条件。
- 摘要给出的实证包括：DROID 上相较 DreamDojo 的 ADE 与 LPIPS 改善、运动探测支持运动学专门化、零样本人类到机器人运动迁移的定性结果，以及策略评估中预测成功率与真实机器人执行成功率一致。

### 局限性
- 摘要未提供足够信息说明方法在 DROID 之外的泛化能力。
- 摘要未提供足够信息说明骨架监督的获取方式、标注成本或对骨架质量波动的敏感性。
- 摘要未提供足够信息说明跨模态交换重建的具体实现细节与消融结果。
- 摘要未提供足够信息说明 branch dropout 的具体设置及其对其他任务的影响。
- 摘要未提供足够信息说明零样本人类到机器人运动迁移的定量范围与失败情形。
- 摘要未提供足够信息说明策略评估的规模、统计显著性与真实机器人执行条件。
- 摘要未提供足够信息说明计算开销、推理时延与训练资源需求。

### 阅读优先级
高。理由：该论文聚焦机器人世界模型中“潜在动作与机器人控制对应不清”的关键问题，提出骨架监督分解与跨模态交换重建等明确方法设计；摘要同时给出 DROID 上的定量改善、运动探测、零样本人类到机器人运动迁移和真实机器人策略评估一致性等多类证据，与具身智能/机器人世界模型方向高度相关。但摘要未展开实现细节与局限，适合作为优先阅读并进一步核查全文实验与消融的候选论文。

</details>

<details>
<summary>Abstract</summary>

Robot world models simulate how environments evolve in response to robot actions. Latent action models enable learning dynamics from videos by encoding visual transitions as proxy actions. However, reconstruction-driven latent actions mix robot motion with object responses and other scene changes, complicating their correspondence with robot controls. We propose SkeLAM, a skeleton-guided latent action model for controllable robot world modeling. SkeLAM decomposes latent actions into a kinematic component grounded by robot skeleton supervision and a residual component retaining complementary visual dynamics. Cross-modal swap reconstruction encourages RGB-derived and skeleton-derived kinematic representations to be interchangeable during video reconstruction. The world model incorporates both components through separate conditioning pathways, while branch dropout reduces its dependence on future-derived residual information. A lightweight adapter maps robot actions to the kinematic space, and subsequent world-model fine-tuning adapts generation to these predicted conditions. At inference, the model generates future observations from the current observation and robot actions. On DROID, SkeLAM reduces end-effector ADE by 19.5% and LPIPS by 11.1% compared with DreamDojo. Motion probing supports kinematic specialization, while qualitative results demonstrate zero-shot human-to-robot motion transfer in generated rollouts. Policy evaluation shows agreement between predicted success rates and those measured in real robot executions.

</details>

#### 2026-10-22 - Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

**Authors:** Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
**Links:** [abs](https://arxiv.org/abs/2610.31166) - [pdf](https://arxiv.org/pdf/2610.31166)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation
- 作者：Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
- 出版日期：2026-10-22T12:24:25Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2610.31166 ；PDF https://arxiv.org/pdf/2610.31166

### 一句话总结
论文提出面向人形机器人全身视觉-语言-动作策略的对象引导预历史记忆机制 WholeBodyMem，并构建人形记忆基准 HuMeGo，以解决动态场景中任务对象线索随时间消失导致的非马尔可夫问题。

### 研究问题
论文指出，动态场景中的人形机器人移动操作具有非马尔可夫性质：对象变化、被遮挡，或随着机器人转身和行走而离开视野时，相关线索会消失；而现有的全身视觉-语言-动作（VLA）策略只感知当前时刻。因此，论文关注的核心问题是：如何让全身 VLA 策略在动作前保留并利用目标对象此前出现过的视觉历史信息。

### 核心思路/方法
- 提出 WholeBodyMem，一种对象引导的感知记忆，用于保留机器人在执行目标动作之前所见对象事件的预历史。
- 使用 SAM3 跟踪任务对象。
- 对象事件以因果方式在自适应预算内选择关键帧。
- 动作专家通过交叉注意力读取这些关键帧，并结合编码外观、几何和时间的对象 token。
- 强调“保留正确的帧”而非“保留更多帧”。
- 构建 HuMeGo 人形记忆基准，包含六个仿真和六个真实世界 Unitree G1 任务。

### 主要贡献
- 提出 WholeBodyMem 对象引导感知记忆机制，将预历史对象事件引入全身 VLA 策略。
- 设计基于 SAM3 跟踪、对象事件因果选帧和对象 token（外观、几何、时间）的记忆读取方式。
- 构建 HuMeGo 基准，覆盖六个仿真与六个真实世界 Unitree G1 任务。
- 摘要报告：相比无记忆和均匀记忆基线，WholeBodyMem 将基础策略成功率从仿真 29.1% 提升至 72.6%，真实机器人从 36.7% 提升至 88.3%；标准 SIMPLE 任务从 70.2% 提升至 86.9%。

### 局限性
- 摘要未提供足够信息说明方法在不同对象类别、遮挡时长、光照变化或复杂动态场景下的泛化边界。
- 摘要未提供足够信息说明 HuMeGo 基准的任务多样性细节、评价指标细节和统计显著性。
- 摘要未提供足够信息说明计算开销、实时性、自适应预算的具体设定及其敏感性。
- 摘要未提供足够信息说明失败案例、与更多基线方法的系统比较以及消融实验的完整结果。

### 阅读优先级
高。理由：论文直接针对全身 VLA 人形移动操作中的非马尔可夫感知问题，提出记忆机制并构建仿真与真实机器人基准，且摘要给出了较大的成功率提升；对具身智能、机器人操作和 VLA 策略记忆方向具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert reads by cross-attention together with object tokens encoding appearance, geometry and time. We also contribute HuMeGo, a humanoid memory benchmark with six simulated and six real-world Unitree G1 tasks. Keeping the right frames rather than more frames, WholeBodyMem surpasses memoryless and uniform-memory baselines, raising its base policy's success from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, while also improving the standard SIMPLE tasks (70.2% to 86.9%).

</details>

#### 2026-10-22 - In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

**Authors:** Hengyi Sim, Quentin Rouxel, Dennis Hong, Darwin Caldwell, Fei Chen
**Links:** [abs](https://arxiv.org/abs/2610.30988) - [pdf](https://arxiv.org/pdf/2610.30988)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations
- 作者：Hengyi Sim, Quentin Rouxel, Dennis Hong, Darwin Caldwell, Fei Chen
- 出版日期：2026-10-22T09:34:18Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.30988；PDF https://arxiv.org/pdf/2610.30988

### 一句话总结
论文提出一种基于 Transformer 的“软物体世界模型”，通过可变长度部分点云历史进行上下文学习以推断形状与材料潜变量，并进行生成式全状态估计与动作条件动力学预测，再与目标条件动作规划器结合，用于双臂软衣物折叠。

### 研究问题
软物体（如衣物）的鲁棒操作是服务与家庭机器人需要具备的关键能力，但由于状态空间维度高且形变依赖材料属性而具有挑战性。人类可通过“心理世界模型”从部分观测中想象形状与材料属性并预测动作对未来状态的影响。论文关注如何让机器人嵌入类似世界模型以提升对多种衣物的泛化能力，同时应对学习世界模型通常需要大量难以采集的真实世界数据、以及需要推断支配动力学的潜属性这两个问题。

### 核心思路/方法
论文提出 Soft-Object World Model，使用 Transformer 骨干网络在大规模模拟软物体交互数据上训练，执行生成式全状态估计和动作条件动力学预测，并采取缓解模拟到现实差距的措施。模型通过对可变长度部分点云历史进行上下文学习，学习推断潜在的形状与材料线索，从而在无需权重更新的情况下泛化到不同机器人形态、材料参数、衣物类型与形状以及操作协调模式。随后，该世界模型与目标条件动作规划器集成以进行运动合成。摘要称在仿真和真实世界中验证了双臂衣物折叠，并报告了重建保真度、预测准确性和任务成功率的提升。

### 主要贡献
- 提出 Soft-Object World Model，用于软物体的生成式全状态估计与动作条件动力学预测。
- 使用 Transformer 骨干并在大规模模拟软物体交互上训练，同时包含缓解模拟到现实差距的措施。
- 通过可变长度部分点云历史的上下文学习推断潜在形状与材料线索，实现无需权重更新的跨机器人形态、材料参数、衣物类型与形状、操作协调模式泛化。
- 将世界模型与目标条件动作规划器集成用于运动合成。
- 在仿真和真实世界中验证双臂衣物折叠，并报告重建保真度、预测准确性和任务成功率方面的改进。

### 局限性
- 摘要未提供足够信息说明模拟到现实差距缓解措施的具体内容与效果边界。
- 摘要未提供足够信息说明真实世界实验规模、衣物种类数量、成功率数值及对比基线细节。
- 摘要未提供足够信息说明模型在非折叠类软物体任务或其他操作任务上的适用性。
- 摘要未提供足够信息说明训练数据规模、计算需求及推理实时性。
- 摘要未提供足够信息说明失败案例与安全风险。

### 阅读优先级
中。理由：论文聚焦软物体双臂操作中的世界模型与部分观测泛化，问题定义和方法组合（上下文学习、点云历史、动作条件动力学、目标条件规划）对具身操作与软物体 manipulation 方向有参考价值；但摘要未给出具体实验数值、基线对比和真实世界规模，若需评估方法有效性需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations. Humans address this challenge by using mental world models that "imagine" the shape and material properties from partial observations, which enables them to predict how actions affect future states. As such, embedding such world models in robots allows for better generalization in manipulating a wide variety of garments in the real world. However, learned world models typically require large amounts of real world data that is strenuous to collect, and a mechanism to infer latent properties that govern dynamics. We present a Soft-Object World Model that performs generative full-state estimation and action-conditioned dynamics prediction using a transformer backbone trained on large-scale simulated soft object interactions, with measures to mitigate the sim-to-real gap. By learning to infer latent shape and material cues through in-context learning over a variable-length partial point-cloud history, the model generalizes across robot embodiments, material parameters, garment types and shapes, and manipulation coordination modes without weight updates. The world model is then integrated with a Goal-Conditioned action planner for motion synthesis. We validate the approach in simulation and real world for bimanual garment folding, reporting improvements in reconstruction fidelity, prediction accuracy, and task success.

</details>

#### 2026-10-21 - Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation

**Authors:** Xiongbo Shi, Shihang Du, Zongyou Yu, Ao Zhou, Xudong Zhang, Ziyu Lin, Haodong Zhang, Junqiao Zhao, Guang Chen
**Links:** [abs](https://arxiv.org/abs/2610.30540) - [pdf](https://arxiv.org/pdf/2610.30540)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation
- 作者：Xiongbo Shi, Shihang Du, Zongyou Yu, Ao Zhou, Xudong Zhang, Ziyu Lin, Haodong Zhang, Junqiao Zhao, Guang Chen
- 出版日期：2026-10-21T23:54:17Z
- 分类：Embodied / Robotics / AR Applications（主分类）；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.30540 ；PDF https://arxiv.org/pdf/2610.30540

### 一句话总结
论文提出 Spatiotemporal Retargeting（STR），利用关键帧和关键身体部位分配优化资源，并结合 Mechanics-Aware Contact Anchoring（MCA）与 Spatiotemporal Reinforcement Learning（STRL），以改善人形机器人物体交互动作重定向的计算效率和接触保真度。

### 研究问题
摘要指出，人形机器人动作重定向需要把人类示范转换为全身控制和 loco-manipulation 的参考轨迹。对于物体交互任务，成功执行依赖于在关键阶段准确保留身体—物体关系；但统一的逐帧迭代预算没有考虑这些局部化的精度需求，从而限制了重定向的计算效率。论文即针对这一“局部精度需求与统一计算预算不匹配”的问题展开。

### 核心思路/方法
论文提出 Spatiotemporal Retargeting（STR），其核心是按时空重要性分配优化努力：
- 使用视觉语言模型选择相关运动信号和身体部位；
- 根据所选信号的变化识别关键帧；
- 对关键帧分配更多求解器迭代，对所选身体部位赋予更高的交互权重；
- 引入 Mechanics-Aware Contact Anchoring（MCA），利用近似物体力旋量模型细化物体表面接触位置，同时保留所选表面方向；
- 在所得参考轨迹基础上，提出 Spatiotemporal Reinforcement Learning（STRL），结合自适应关键阶段采样，以及基于目标接近度和物体接触力的接触奖励，用于下游控制。

### 主要贡献
- 提出 STR，通过关键帧和关键身体部位的空间—时间偏好来分配重定向优化资源，以应对局部精度需求。
- 引入 MCA，用近似物体力旋量模型细化物体表面接触位置，以提升接触保真度。
- 提出 STRL，将自适应关键阶段采样与基于目标接近度和物体接触力的接触奖励结合，用于下游控制。
- 摘要报告：在 Unitree G1 仿真实验和 Unitree R1 真实世界实验中，STR 以更低计算成本提升几何接触覆盖和连续性，所得参考轨迹改善多种物体交互动作的下游任务完成情况。

### 局限性
- 摘要未提供足够信息说明方法在更多机器人平台、更多物体类别或更复杂接触场景中的泛化能力。
- 摘要未提供足够信息说明关键帧识别、视觉语言模型选择及 MCA 近似模型失败时的鲁棒性。
- 摘要未提供足够信息给出计算成本、接触覆盖、连续性及下游任务完成率的具体量化指标和统计显著性。
- 摘要未提供足够信息说明真实世界实验的规模、任务数量和评价协议。
- 摘要未提供足够信息讨论对视觉语言模型依赖、物体模型精度或力旋量近似误差的敏感性。

### 阅读优先级
中。理由：论文主题聚焦人形机器人动作重定向与 loco-manipulation，方法上把关键帧/关键部位选择、接触锚定和强化学习控制结合起来，并与摘要中提到的仿真和真实机器人实验相关；但当前仅依据摘要，缺少具体量化结果、实验规模和失败案例分析，适合作为相关方向的重点候选阅读，而非仅凭摘要即可判定为高优先级必读。

</details>

<details>
<summary>Abstract</summary>

Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration budgets do not account for these localized accuracy requirements, limiting the computational efficiency of retargeting. To address this limitation, we present Spatiotemporal Retargeting (STR), which uses keyframes and key body parts to allocate optimization effort. Specifically, a vision-language model selects relevant motion signals and body parts, and keyframes are identified from changes in the selected signals. Based on these selections, STR assigns additional solver iterations to keyframes and higher interaction weights to the selected parts. To further improve contact fidelity, we introduce Mechanics-Aware Contact Anchoring (MCA) to refine object-surface contact positions using an approximate object-wrench model while retaining the selected surface directions. Building on the resulting references, we develop Spatiotemporal Reinforcement Learning (STRL), which combines adaptive key-stage sampling with a contact reward based on target proximity and object contact forces for downstream control. Simulation experiments on a Unitree G1 and real-world experiments on a Unitree R1 demonstrate that STR improves geometric contact coverage and continuity at lower computational cost, while the resulting references improve downstream task completion across diverse object-interaction motions.

</details>

#### 2026-10-21 - RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation

**Authors:** Samuel Foo Enze, Manthan Patel, Fan Yang, Linus Kramer, Pascal Roth, Marco Hutter, Cesar Cadena
**Links:** [abs](https://arxiv.org/abs/2610.29845) - [pdf](https://arxiv.org/pdf/2610.29845)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation
- 作者：Samuel Foo Enze, Manthan Patel, Fan Yang, Linus Kramer, Pascal Roth, Marco Hutter, Cesar Cadena
- 出版日期：2026-10-21T15:06:08Z
- 分类：主分类 Embodied / Robotics / AR Applications；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.29845 ；PDF https://arxiv.org/pdf/2610.29845 ；项目网站 https://rangenav.github.io/

### 一句话总结
RangeNav 提出一个仅 183k 参数、完全用合成数据预训练的 LiDAR range-image 编码器，通过导航对齐的多任务预训练后冻结用于策略学习，并在仿真与真实四足机器人上验证导航表现。

### 研究问题
论文针对密集人群与杂乱场地中移动机器人需要 360° 感知的问题，指出全景 LiDAR 虽能全覆盖，但在稀疏奖励下用强化学习直接学习表示样本效率低，而现有 3D 预训练点云编码器对大规模并行 RL 仿真而言内存开销过大。因此需要一种紧凑、适合并行仿真且能提供有效感知表示的方案。

### 核心思路/方法
- 采用 LiDAR range-image 作为输入形式，构建紧凑编码器（183k 参数），完全在合成数据上预训练。
- 针对 range image 的极端长宽比与方位角接缝，使用各向异性卷积和循环填充。
- 预训练目标为导航对齐的多任务组合：range reconstruction、semantic segmentation 与 bird's-eye-view (BEV) prediction。
- 预训练完成后冻结编码器，用于后续策略学习。

### 主要贡献
- 提出紧凑的 LiDAR range-image 编码器 RangeNav，参数量仅 183k，预训练完全基于合成数据，面向大规模并行 RL 仿真的内存约束。
- 设计适配 range image 极端长宽比与方位角接缝的网络结构（各向异性卷积、循环填充）。
- 提出导航对齐的预训练目标，联合 range reconstruction、semantic segmentation 与 BEV prediction。
- 仿真结果显示，相较仅重建基线，加入语义与 BEV 监督在程序化生成的训练环境和分布外真实感测试环境中分别平均提升成功率 32.03 与 23.73 个百分点。
- 在 Unitree B2-W 四足机器人上进行零样本真实部署，摘要称其在密集人群、低光环境和施工区域中表现稳健，而有限视场深度策略在这些场景中表现困难。

### 局限性
- 摘要未提供足够信息说明预训练数据规模、合成数据来源与多样性。
- 摘要未提供足够信息说明真实世界实验的定量指标、试验次数与统计显著性。
- 摘要未提供足够信息说明与更多基线方法的系统对比。
- 摘要未提供足够信息说明编码器冻结后策略学习的具体算法与训练成本。
- 摘要未提供足够信息说明失败案例与安全性分析。

### 阅读优先级
高。理由：论文聚焦机器人导航中全景 LiDAR 感知与 RL 样本效率/内存瓶颈的实际问题，方法紧凑且给出仿真提升幅度与真实四足机器人零样本部署结果，并承诺开源代码与模型；对具身智能、机器人导航与 LiDAR 表示学习方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous mobile robots operating in dense crowds and cluttered sites require $360^\circ$ perception to react to surrounding hazards. While panoramic LiDAR offers full-surround coverage, learning representations within reinforcement learning (RL) is sample-inefficient under sparse rewards, and existing 3D pretrained point-cloud encoders are too memory-heavy for massively parallel RL simulation. We present RangeNav, a compact (183k parameters) LiDAR range-image encoder pretrained entirely on synthetic data. RangeNav uses anisotropic convolutions and circular padding to handle the extreme aspect ratio and azimuthal seam of range images. We pretrain the network using a navigation-aligned objective combining range reconstruction, semantic segmentation, and bird's-eye-view (BEV) prediction, then freeze it for policy learning. In simulation, adding semantic and BEV supervision increases success rates over a reconstruction-only baseline by an average of 32.03 and 23.73 percentage points (pp) in procedurally generated training and out-of-distribution realistic test environments, respectively. Zero-shot real-world deployments on a Unitree B2-W quadruped demonstrate robust navigation through dense crowds, low-light settings, and construction zones where limited-field-of-view depth policies struggle. Code and models will be open-sourced. Project website: https://rangenav.github.io/.

</details>

#### 2026-10-20 - COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation

**Authors:** Jiahui Yang, Jason Jingzhou Liu, Ray Muxin Liu, Andrew E. Wang, Kenneth Shaw, Deepak Pathak, Ruslan Salakhutdinov
**Links:** [abs](https://arxiv.org/abs/2610.28948) - [pdf](https://arxiv.org/pdf/2610.28948)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation
- 作者：Jiahui Yang, Jason Jingzhou Liu, Ray Muxin Liu, Andrew E. Wang, Kenneth Shaw, Deepak Pathak, Ruslan Salakhutdinov
- 出版日期：2026-10-20T21:59:10Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.28948 ；PDF https://arxiv.org/pdf/2610.28948

### 一句话总结
COWBOY 提出一种可扩展的仿真到现实（sim-to-real）框架，通过“向量化环境感知全身控制器 + 局部强化学习专家 + 蒸馏为单一视觉策略”的组合，让移动机械臂根据物体与场景空间上下文自适应地完成全身灵巧抓取。

### 研究问题
移动机械臂不仅要适应物体本身，还要适应物体出现的空间上下文：底座应放在哪里、如何操作、在绕行周围场景几何时应看向何处。论文关注如何学习这种“上下文感知的全身操作”，并使其能够从仿真迁移到真实世界、扩展到大量物体与多样场景。

### 核心思路/方法
- 不直接在仿真中用强化学习（RL）学习场景适应，而是设计一个向量化的、环境感知的全身控制器（WBC），在上千个场景中通过协调底座—机械臂运动、避障和主动视觉来完成到达。
- 在局部场景中训练用于物体交互的局部 RL 专家，这些专家可跨数千个完整场景布局复用。
- 将组合后的 WBC-RL 教师策略蒸馏为一个单一的视觉策略；该策略从点云观测出发，控制移动底座、机械臂、灵巧手和可驱动相机。
- 得到的策略表现出上下文全身行为：根据观测到的场景与物体几何，自动调整底座位置、相机视角、机械臂轨迹和抓取策略。

### 主要贡献
- 提出 COWBOY：面向上下文全身操作的可扩展 sim-to-real 框架。
- 在全身灵巧抓取任务上，COWBOY 零样本迁移到数百个物体和多样野外场景，包括杂乱桌面、架子、抽屉及其他非结构化环境（摘要所述）。
- 提出将向量化环境感知 WBC 与可复用的局部 RL 专家结合，并蒸馏为单一视觉策略的路线，避免直接在仿真中用 RL 学习场景适应。
- 策略能够从点云观测同时控制移动底座、机械臂、灵巧手和可驱动相机，并展现自适应的底座放置、视角选择、轨迹与抓取策略。

### 局限性
- 摘要未提供足够信息说明真实世界实验的规模、成功率、失败模式与定量对比。
- 摘要未提供足够信息说明方法对未见物体类别、极端杂乱或动态环境的泛化边界。
- 摘要未提供足够信息说明 WBC、局部 RL 专家与蒸馏策略各自的训练成本、仿真依赖程度及 sim-to-real 差距的具体来源。
- 摘要未提供足够信息说明安全性、碰撞保证或主动视觉在真实部署中的鲁棒性。

### 阅读优先级
高。理由：该论文聚焦移动机械臂的上下文感知全身灵巧操作与可扩展 sim-to-real，方法路线（WBC + 局部 RL 专家 + 蒸馏视觉策略）对具身智能与机器人操作研究具有较强参考价值；且摘要声称零样本迁移到数百物体与多样非结构化场景，若属实具有较高影响力。但需注意：上述判断仅基于摘要与元数据，具体实验证据需阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Mobile manipulators must adapt not only to objects, but also to the spatial context in which they appear: where to position the base, how to manipulate, and where to look while navigating surrounding scene geometry. To address this, we present COWBOY, a scalable sim-to-real framework for learning such contextual whole-body manipulation. On whole-body dexterous grasping, COWBOY transfers zero-shot to hundreds of objects and diverse in-the-wild scenes, spanning cluttered tabletops, shelves, drawers, and other unstructured settings. Rather than learning scene adaptation directly with RL in simulation, a vectorized environment-aware whole-body controller (WBC) handles reaching in thousands of scenes by coordinating base-arm motion, collision avoidance, and active vision. Then, local RL experts are trained in local scenes for object interaction and can be reused across thousands of full-scene layouts. We distill these composed WBC-RL teachers into a single vision policy that controls the mobile base, arm, dexterous hand, and actuated camera from point-cloud observations. The resulting policy exhibits contextual whole-body behavior, automatically adapting base placement, camera viewpoint, arm trajectory, and grasp strategy to observed scene and object geometry. Videos are available at https://cowboy-manip.com

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
