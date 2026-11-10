# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：49
- 分类分布：
  - Neural Scene Representations & Rendering: 16
  - 3D Reconstruction & Multi-view Geometry: 11
  - Embodied / Robotics / AR Applications: 9
  - Geometry Foundation Models: 8
  - Dynamic / 4D Reconstruction: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“几何基础模型 + 经典优化/重建管线”深度融合，而非简单替换。**
   多篇论文将基础模型（深度估计、DINOv3、VGGT 类前馈重建）作为先验或初始化嵌入经典优化框架：MetricTrail 将单图像度量深度作为软约束注入 DPVO 稀疏局部估计器；XM4D 用基础深度模型提升点轨迹后构建可验证全局最优的 bundle adjustment；AffineGS 指出单目深度存在区域分段线性失真，改用空间变化仿射校正。这说明当前趋势从“用大模型直接出结果”转向“用大模型提供结构化先验、由可解释优化保证精度与一致性”。

2. **前馈/在线化成为神经场景表示的主战场，核心矛盾转向“速度—质量—表示规模”的三方权衡。**
   HIBS 针对在线增量 GS 初始化机会少的问题，用 beta 核形状参数表达几何置信度；BudgetSplat 针对前馈像素对齐 GS 的高斯冗余，将压缩建模为重要性、覆盖、跨视角冗余的联合问题；P-MGS 按感知复杂度而非网格密度分配高斯；InstantHand 从单图前馈生成可动画手部 avatar 且无需测试时优化。共同点：不再追求“离线逐场景优化到极致”，而是解决在线/前馈条件下的初始化质量、表示紧凑性与可控性。

3. **动态/4D 与“物理感知渲染”成为独立增长点，运动表示与坐标系设计被显式讨论。**
   SM4RT 采用级联前馈（先几何后运动）并将逐像素 3D 运动表达在对应相机坐标系以缓解相机运动歧义；XM4D 将相机运动与非刚性形变分离为两阶段 QCQP；4DPS 将显式运动点 splat 到距离—多普勒 bin，输出雷达原始复数回波。这些工作共同反映：动态重建正从“端到端黑箱”转向“分解子问题 + 物理/几何可验证性 + 跨模态（雷达、事件相机）”。

4. **三维重建从“局部几何”走向“地理/度量/跨视角对齐”，并延伸到机器人数据规模化。**
   X-VGGT 联合地面图像与卫星图像预测场景级重力—尺度—偏航—平移变换，实现地理配准；Trainspotting 构建跨年份、跨环境、跨实物单元的“found photos”数据集，揭示前馈模型在真实档案数据上的失效模式；WVS 从多透视相机合成几何一致宽视角。另一方面，Spatial-UMI-Dream 把度量深度显式纳入 World Action Model 的联合预测，MOMASPLAT 用动态新视角合成增强移动操作示范。趋势是：几何精度与度量/地理一致性正成为下游 embodied 应用的前置条件。

5. **轻量化、能耗与资源约束重新受到关注，且与“大模型叙事”并存。**
   SpikePose 用脉冲编码器 + 轻量时序模块在非事件视频任务上逼近 ANN；STAG-Net 以关键点组注意力实现轻量头部姿态估计；4D Point Splatting 用自定义 CUDA 核做序列级拟合。这与前馈大模型路线形成互补：一端追求规模化泛化，一端追求边缘部署可行性。

#### 技术路线观察

- **几何基础模型路线（Geometry Foundation Models）**：代表为 X-VGGT、MetricTrail、Trainspotting。侧重点在“把基础模型输出接入几何一致性框架”——X-VGGT 用场景级变换参数化跨视角对齐，MetricTrail 用度量深度作软约束并冻结 DINOv3 特征适配，Trainspotting 则反向暴露现有前馈模型的训练分布偏差。该路线的方法论特征是：不重训大模型主体，而设计适配器、约束或评估协议。

- **动态/4D 重建路线**：SM4RT 与 XM4D 形成两种典型思路——前者用级联前馈 + 相机坐标系运动表达 + 弱监督损失处理标签稀疏；后者用可验证全局最优的 QCQP/SDP 分解优化 + 动态高斯泼溅细化。前者偏“学习式、可扩展”，后者偏“优化式、可保证”。两者共同说明 4D 领域正分化为“前馈泛化”与“几何可证”两条并行技术路线，未来可能出现前馈初始化 + 可证优化的混合方案。

- **神经场景表示与渲染路线**：HIBS、BudgetSplat、P-MGS、AffineGS、InstantHand、4DPS、WVS 覆盖了高斯/核表示的结构改造（beta 核、感知复杂度分配、空间变化仿射）、表示规模控制（预算可控压缩）、跨模态渲染（雷达微多普勒）与跨相机几何（宽视角）。技术侧重点从“如何渲染得更像”转向“如何让表示更可编辑、更紧凑、更可控、更有物理/几何意义”。

- **机器人/AR 应用路线**：MOMASPLAT、Spatial-UMI-Dream、TactileLab、WVS 体现两种牵引力——一是用 NVS/世界模型生成感知数据以缓解示范稀缺与视角敏感，二是用度量几何/触觉流等物理量提升 sim-to-real 保真度。值得注意的是，这些工作普遍把“几何/物理一致性”作为数据增强有效性的前提，而非仅追求视觉逼真。

- **轻量感知与多视图几何路线**：SpikePose、STAG-Net、事件相机 LED 位姿估计代表资源受限与高动态场景需求，方法上强调轻量编码器 + 紧凑时序/结构模块，与主流的“大模型前馈”形成不同约束下的技术分支。

#### 值得优先阅读的论文

1. **XM4D（2611.07902）**：把 4D 重建拆成两个可验证全局最优的 QCQP 并用 SDP 求解，再初始化动态高斯泼溅。其“可证最优 + 学习式细化”的混合范式可能影响后续 4D 重建的方法论设计，且对理解几何优化与神经表示如何衔接有直接价值。

2. **AffineGS（2611.07709）**：指出单目深度网络存在区域分段线性失真这一被广泛忽视的假设缺陷，并提出空间变化仿射校正。该发现可能影响所有使用单目深度先验做 GS 正则化的后续工作，属于“修正社区默认假设”类贡献。

3. **SM4RT（2611.08436）**：级联前馈 + 相机坐标系运动表达 + 弱监督运动损失，是当前动态场景前馈重建的典型技术组合。适合作为理解“几何先行、运动引导”路线的入口，也便于与 XM4D 的优化式路线对比阅读。

4. **BudgetSplat（2611.06593）**：将前馈 GS 压缩从重要性排序重新表述为重要性、覆盖、冗余联合问题，且单模型支持多预算。对关注前馈表示规模化部署与渲染成本控制的读者优先级高。

5. **Trainspotting（2611.06849）**：构建跨年份、跨环境、跨实物单元的 found photos 数据集并系统评估前馈模型失效模式。其价值不在单一方法，而在于揭示现有前馈重建训练分布与真实档案数据之间的系统性差距，可能催生新的评估与微调方向。

#### 可能的研究机会

- **前馈初始化 + 可证几何优化的混合 4D 管线**：SM4RT 的级联前馈与 XM4D 的可验证 QCQP 优化尚未结合。可探索用前馈模型提供运动/几何初值，再用 SDP 松弛做全局一致性校正，兼顾泛化与可证性。

- **单目深度先验失真的系统建模与跨任务迁移**：AffineGS 发现的分段线性失真是否普遍存在于不同深度网络、不同场景类型？能否将该校正推广到动态 4D、SLAM 与机器人度量深度预测中？这是低风险、高杠杆的跟进方向。

- **动态场景下的表示预算与几何置信度联合控制**：HIBS 的 beta 核形状参数表达几何置信度，BudgetSplat 的

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-10T15:28:03-05:00
**Total number of papers:** 60
**Number of papers added in the latest update:** 29
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

#### 2026-11-09 - V3DSAM: Semantic-Geometric Loop Verification and Geometry-Anchored Persistent Instance Mapping for Feed-Forward Dense SLAM

**Authors:** Maolin Ye, Dongqing Zhao, Linyang Li, Shuai Xue, Yuan Liu, Yiyuan Wang, Wen Li
**Links:** [abs](https://arxiv.org/abs/2611.12452) - [pdf](https://arxiv.org/pdf/2611.12452)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, SLAM, mapping

<details>
<summary>Abstract</summary>

To address unreliable cross-view association in long-sequence feed-forward dense SLAM, this letter presents V3DSAM, an open-vocabulary semantic dense SLAM system that establishes physical correspondences at both the scene and object levels. The system combines feed-forward geometric estimates from VGGT-SLAM 2.0 with open-vocabulary semantic observations from SAM3. We introduce semantic-geometric dual-scale loop verification, which identifies false loop closures using pixel-level bidirectional reprojection and object-level 3D spatial correspondences, without accessing backbone-internal features. We further propose geometry-anchored persistent instance mapping, which defines physical instances through class-constrained 3D connectivity in an optimized global coordinate system and assigns global IDs without inter-frame identity propagation. The proposed verifier rejects all four false loop candidates in our TUM RGB-D evaluation, while long-sequence ScanNet experiments show improved instance identity consistency. Thus, V3DSAM reduces dependence on internal backbone features and temporal ID propagation for robust long-term cross-view association.

</details>

#### 2026-11-05 - Georeferenced Cross-View 3D Reconstruction from Ground and Satellite Images

**Authors:** David G. Shatwell, Mubarak Shah
**Links:** [abs](https://arxiv.org/abs/2611.07575) - [pdf](https://arxiv.org/pdf/2611.07575)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Georeferenced Cross-View 3D Reconstruction from Ground and Satellite Images
- 作者：David G. Shatwell, Mubarak Shah
- 出版日期：2026-11-05T07:26:29Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.07575) | [PDF](https://arxiv.org/pdf/2611.07575)

### 一句话总结
论文提出 X-VGGT，一个前馈式跨视角几何 Transformer，联合处理地面图像与带地理参考的卫星图像，同时预测地面相机位姿、稠密 3D 点图以及场景级变换参数，从而将局部重建对齐到卫星平面，实现地面图像的地理配准。

### 研究问题
从地面图像进行地理参考 3D 重建，不仅需要恢复局部场景几何，还需要把每个相机中心和 3D 点定位到地理坐标系中。摘要指出，现有跨视角地理定位方法只能估计单个地面相机的 GPS 坐标，不能重建稠密 3D 几何；而近期的前馈多视图 3D 重建模型只在局部坐标系中预测点图和相机位姿。因此，如何将跨视角地理定位与稠密 3D 重建统一起来，是本文关注的问题。

### 核心思路/方法
论文提出 X-VGGT，一种前馈式跨视角几何 Transformer。其核心是联合处理一组地面级图像和一张带地理参考的卫星图像，并预测三类输出：
1. 地面视角相机位姿；
2. 稠密 3D 点图；
3. 一个场景级变换，该变换由重力、尺度、偏航角和 translation 参数化。

该变换用于将局部重建投影到卫星平面，从而完成所有地面图像与带地理参考卫星图像的地理配准。论文还提出了针对这一联合任务的评估协议。

### 主要贡献
- 提出 X-VGGT，将地面图像与卫星图像联合处理，统一跨视角地理定位与稠密 3D 重建任务。
- 在输出中同时预测地面相机位姿、稠密 3D 点图，以及由重力、尺度、偏航角和 translation 参数化的场景级变换，用于将局部重建投影到卫星平面并实现地理配准。
- 提出针对该联合任务的评估协议。
- 摘要称，在多个跨视角数据集上，X-VGGT 能产生准确的地理参考重建，并优于先前的跨视角地理定位和多视图 3D 重建模型。

### 局限性
摘要未提供足够信息。例如具体数据集名称、实验设置、定量指标、失败案例、计算开销、对卫星图像质量或地面图像覆盖范围的敏感性等，均未在摘要中说明。

### 阅读优先级
高。理由：该论文直接针对跨视角地理定位与前馈多视图 3D 重建之间的任务缺口，提出联合建模方法和评估协议；摘要明确声称在多个跨视角数据集上优于现有两类方法，问题定义和方法输出均较清晰，适合关注 3D 重建、多视图几何与跨视角地理定位交叉方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Georeferenced 3D reconstruction from ground images requires recovering not only the local scene geometry, but also localizing every camera center and 3D point in a geographic coordinate frame. Existing cross-view geo-localization methods are able to estimate the GPS coordinate of a single ground camera, but do not reconstruct dense 3D geometry, while recent feed-forward multi-view 3D reconstruction models predict point maps and camera poses only in a local coordinate frame. We introduce X-VGGT, a feed-forward cross-view geometry transformer that unifies these tasks by jointly processing a set of ground-level images and a georeferenced satellite image to predict ground-view camera poses, dense 3D point maps, and a scene-level transform parameterized by gravity, scale, yaw and translation. This transform projects the local reconstruction into the satellite plane, resulting in the geo-registration of all ground images with the georeferenced satellite image. We further propose an evaluation protocol for this joint task and show that, across multiple cross-view datasets, X-VGGT produces accurate georeferenced reconstructions and outperforms prior cross-view geo-localization and multi-view 3D reconstruction models.

</details>

#### 2026-11-05 - MetricTrail: Revisiting the Power of Metric Depth and Local Optimization for Long-Sequence Streaming 3D Reconstruction

**Authors:** Jingnan Gao, Jiahui Huang, Sven Elflein, Jianhao Zheng, Bingxin Ke, Xiaokang Yang, Yichao Yan, Laura Leal-Taixé, Qunjie Zhou, Jiawei Ren, Shengyu Huang
**Links:** [abs](https://arxiv.org/abs/2611.07555) - [pdf](https://arxiv.org/pdf/2611.07555)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, 3D reconstruction, dense reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MetricTrail: Revisiting the Power of Metric Depth and Local Optimization for Long-Sequence Streaming 3D Reconstruction
- 作者：Jingnan Gao, Jiahui Huang, Sven Elflein, Jianhao Zheng, Bingxin Ke, Xiaokang Yang, Yichao Yan, Laura Leal-Taixé, Qunjie Zhou, Jiawei Ren, Shengyu Huang
- 出版日期：2026-11-05T07:02:32Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.07555 ；PDF https://arxiv.org/pdf/2611.07555

### 一句话总结
MetricTrail 是一个面向长单目视频的流式系统，通过引入单图像度量深度改进 DPVO 式稀疏局部估计器，并结合冻结 DINOv3 表示的学习适配器提升对应估计，从而实现相机运动估计与稠密重建。

### 研究问题
论文关注从长单目视频中进行准确的相机运动估计与稠密重建。为在长序列上保持推理效率，作者重新审视 DPVO 的稀疏局部估计器，试图在不重新训练对应网络、不扩大优化窗口的前提下提升轨迹精度，并改善对应估计与系统模块的可替换性。

### 核心思路/方法
- 沿用 DPVO 的稀疏局部估计器以保持长序列推理效率。
- 利用单图像度量深度初始化 patch 深度，并在优化过程中将其作为软约束，从而提升轨迹精度；摘要强调无需重新训练对应网络或扩大优化窗口。
- 通过学习的适配器，将冻结的 DINOv3 表示用于增强匹配特征与循环上下文，以改进对应估计。
- 对应估计器与适配器在多样的短片段上训练，不进行额外的长序列训练。
- 模块化设计使深度提供者可以独立升级，并支持提供相机内参与标定立体观测而无需重新训练。

### 主要贡献
- 提出 MetricTrail 流式系统，用于长单目视频的相机运动估计与稠密重建。
- 表明单图像度量深度可显著提升 DPVO 式稀疏局部估计器的轨迹精度，且无需重新训练对应网络或扩大优化窗口。
- 引入基于冻结 DINOv3 表示的学习适配器以增强匹配特征和循环上下文。
- 系统设计具备模块化特性：深度提供者可独立升级，并支持输入相机内参与标定立体观测而无需重训练。
- 摘要报告在仅 RGB 协议下，于 KITTI、Oxford Spires 和 VBR 上取得所评估方法中最低的平均轨迹误差；将估计位姿与单图像深度预测配对后，在室内外基准上产生较强稠密重建，并对野外视频产生连贯重建。
- 摘要报告在提供内参时，系统处理 KITTI-02 达到 12.70 FPS，峰值 GPU 内存 3.21 GB。

### 局限性
- 摘要未提供足够信息说明方法在极端长序列、剧烈运动、低纹理或动态场景下的具体表现。
- 摘要未提供足够信息说明对单图像度量深度预测质量的依赖程度及失败模式。
- 摘要未提供足够信息给出完整实验设置、对比方法细节、消融实验规模与训练数据规模。
- 摘要未提供足够信息说明稠密重建的定量指标细节与实时性在不同硬件上的泛化表现。
- 摘要未提供足够信息讨论标定立体观测与提供内参场景下的系统开销与精度变化。

### 阅读优先级
中。理由：论文聚焦长序列流式单目 3D 重建，结合度量深度、局部优化与冻结视觉基础模型适配器，问题明确且摘要给出多基准轨迹误差与效率数据；但摘要未展开实验细节与局限性，适合作为相关方向的重点跟踪论文，而非仅凭摘要即可完全评估其方法细节的必读高优先级。

</details>

<details>
<summary>Abstract</summary>

We present MetricTrail, a streaming system for accurate camera motion estimation and dense reconstruction from long monocular videos. To keep inference efficient over long sequences, we revisit DPVO's sparse local estimator. We find that single-image metric depth substantially improves its trajectory accuracy, without retraining the correspondence network or enlarging the optimization window. Metric predictions initialize patch depths and remain as soft constraints during optimization. We further improve correspondence estimation through learned adapters that augment matching features and recurrent context with frozen DINOv3 representations. The correspondence estimator and adapters are trained on diverse short clips without additional long-sequence training. This modular design also allows the depth provider to be independently upgraded and supports supplied camera intrinsics and calibrated stereo observations without retraining. Under the reported RGB-only protocols, MetricTrail achieves the lowest average trajectory error among evaluated methods on KITTI, Oxford Spires, and VBR. Pairing the estimated poses with single-image depth predictions also produces strong dense reconstruction on indoor and outdoor benchmarks and coherent reconstructions of in-the-wild videos. With supplied intrinsics, the system processes KITTI-02 at 12.70 FPS with 3.21 GB peak GPU memory.

</details>

#### 2026-11-04 - Trainspotting: Learning Object-Centric 3D Reconstruction from Found Photos

**Authors:** Hanyu Chen, Noah Snavely
**Links:** [abs](https://arxiv.org/abs/2611.06849) - [pdf](https://arxiv.org/pdf/2611.06849)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, feedforward reconstruction, 3D reconstruction, multi-view stereo, stereo depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Trainspotting: Learning Object-Centric 3D Reconstruction from Found Photos
- 作者：Hanyu Chen, Noah Snavely
- 出版日期：2026-11-04T18:05:22Z
- 分类：Geometry Foundation Models（主）；3D Reconstruction & Multi-view Geometry（次）
- 链接：[摘要](https://arxiv.org/abs/2611.06849) ｜ [PDF](https://arxiv.org/pdf/2611.06849)

### 一句话总结
论文构建了来自 Wikimedia Commons 的“found photos”物体中心多视角数据集 Trainspotting（12,068 个物体、311,886 张照片），并指出当前前馈重建模型在其中两类场景下失效严重，微调 VGGT-Ω 可显著改善相机位姿、深度与 3D 几何。

### 研究问题
现有前馈重建模型主要在“单次采集”的物体照片上训练，这类照片中视角变化但物体与环境近乎固定；而公共照片档案中的“found photos”由不同人跨越多年、不同环境、不同相机甚至不同实物拍摄同一物体或设计，构成另一种多视角数据形态。论文关注：这类真实档案数据上，当前前馈重建模型表现如何、在哪些情形下失效，以及能否通过在该类数据上微调来改善。

### 核心思路/方法
- 构建 Trainspotting 数据集：从 Wikimedia Commons 收集 12,068 个物体、311,886 张照片。
- 对每个物体进行重建，恢复相机位姿、多视角立体深度与物体掩码。
- 将物体划分为三类情形：固定于单一地点的物体、在多地之间移动的物体、由多个实物共享的同一设计。
- 在 Trainspotting 上评估近期前馈重建模型，并对 VGGT-Ω 进行微调以验证改进效果。

### 主要贡献
- 提出 Trainspotting 数据集，提供来自公共照片档案的物体中心“found photos”多视角数据，并附带相机位姿、多视角立体深度与物体掩码等重建产物。
- 给出三类物体情形的划分框架（固定单点、跨地点移动、多实物共享设计）。
- 实证表明近期前馈重建模型在 Trainspotting 上表现不佳，且在“跨地点移动”和“多实物共享设计”两类情形下失效最严重。
- 在 Trainspotting 上微调 VGGT-Ω 后，留出物体上的相机位姿、深度与 3D 几何显著改善；在独立的 NAVI in-the-wild 基准（每个物体处于不同环境）上观察到类似改进，而传统基准上的性能基本不变。

### 局限性
- 摘要未提供足够信息说明数据集的筛选标准、标注质量控制与规模偏差等细节。
- 摘要未提供足够信息说明微调的具体配置、训练成本与超参数。
- 摘要未提供足够信息给出各模型、各情形下的定量指标数值与消融结果。
- 摘要未提供足够信息说明三类情形划分的判定方式及其可靠性。
- 摘要未提供足够信息讨论在传统基准上“基本不变”的具体度量与范围。

### 阅读优先级
中。理由：该工作聚焦前馈重建模型在真实公共照片档案上的失效模式，并提供新数据集与微调验证，对物体中心 3D 重建与多视角几何方向有参考价值；但摘要未给出定量细节，是否高优先级取决于读者对“found photos”数据形态与 VGGT-Ω 微调的具体兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation
- 作者：Sihang Chen, Chen Ye, Wei Chen, Xiaohan Lei, Zhipeng Tang, Sha Zhang, Yuan Zhang, Zixuan Chen, Jiajun Deng, Houqiang Li, Yanyong Zhang
- 出版日期：2026-11-04T13:16:32Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.06475 ；PDF https://arxiv.org/pdf/2611.06475

### 一句话总结
该论文提出 RoboCasa-Mem 基准，用于评估长时程移动操作中依赖交互历史的环境记忆与过程记忆决策，并提供 HMAP 基线方法。

### 研究问题
摘要指出，真实世界中移动操作机器人需要执行复杂物体交互与多步决策，且常依赖当前已不可观测的任务相关信息；然而现有基准对移动操作中这类依赖记忆的决策评估有限。论文旨在填补这一评估缺口。

### 核心思路/方法
- 构建 RoboCasa-Mem：包含九个移动操作任务，要求智能体在关键决策点使用交互历史。
- 记忆分类：任务分为两类记忆能力——环境记忆（空间位置、物体属性、物体关系）与过程记忆（单任务进度、多任务调度）。
- 评估设计：提出 Behavior-Conditioned Evaluation；对存在多条有效执行路径的任务，不固定单一目标或轨迹，而是由机器人早期动作推导后续任务约束，以评估后续行为是否与自身交互历史一致，并减少基于固定目标分配的捷径。
- 数据：提供 1,800 条成功演示用于策略训练。
- 基线：提出 Hierarchical Memory-Augmented Policy（HMAP）；高层规划器使用结构化实体记忆与过程记忆生成子任务，低层 VLA 控制器使用子目标条件查询，将 VGGT-Omega 几何信息纳入动作生成。

### 主要贡献
- 提出 RoboCasa-Mem 基准，包含九个需在关键决策点使用交互历史的移动操作任务，并区分环境记忆与过程记忆两类能力。
- 引入 Behavior-Conditioned Evaluation，针对多有效执行路径任务，依据机器人早期动作推导后续约束，评估行为与自身交互历史的一致性。
- 提供 1,800 条成功演示用于策略训练。
- 提出 HMAP 基线，结合结构化实体与过程记忆的高层规划，以及融合 VGGT-Omega 几何信息的低层 VLA 控制。

### 局限性
摘要未提供足够信息。摘要未说明基准任务的多样性边界、仿真到现实差距、HMAP 的具体实验表现、对比方法范围、演示数据质量与规模充分性等细节。

### 阅读优先级
高。理由：该工作直接针对长时程移动操作中“依赖不可观测交互历史”的评估缺口，提出新基准与行为条件评估方式，并提供训练演示与基线方法，对具身智能、机器人策略学习和记忆机制评估具有较强相关性；但具体实验效果需阅读全文确认。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Scale Anchoring via Implicit Semantics and Sequence-Consistent Loop Closure for VGGT-Based SLAM
- 作者：Ziyi Jin, Kangjin Yu, Beichen Wang, Can Jiang, Zhongpu Xia, Jie Xu
- 出版日期：2026-11-04T10:42:52Z
- 分类：Geometry Foundation Models（主类）；3D Reconstruction & Multi-view Geometry（次类）
- 链接：[摘要](https://arxiv.org/abs/2611.06308) | [PDF](https://arxiv.org/pdf/2611.06308)

### 一句话总结
该论文在 VGGT-SLAM 2.0 基础上引入固定根尺度锚定与短序列辅助的直接闭环连接，以缓解子图尺度漂移和跨子图重访测量不一致的问题。

### 研究问题
前馈几何基础模型可进行无需相机标定的稠密单目重建，但独立重建的子图会累积尺度漂移；即使发生有效重访，也可能得到不一致的跨子图测量。论文关注如何在此类基于 VGGT 的 SLAM 框架中进行尺度锚定并建立可靠的跨子图闭环连接。

### 核心思路/方法
- 扩展 VGGT-SLAM 2.0，加入“固定根尺度锚定”和“短序列辅助的直接闭环连接”。
- 尺度锚定：SALAD 在初始子图与每个符合条件的新子图之间选择图像对；联合 VGGT 推理利用学习到的隐式语义—几何线索提供仅尺度锚定，同时保留原有重叠链。
- 闭环：邻近图像对支持一致性检查与平移—尺度对齐；每个被接受的候选在已有中心帧节点之间贡献一个稳健的 Sim(3) 因子，不引入辅助闭环子图。

### 主要贡献
- 提出固定根尺度锚定与短序列辅助的直接闭环连接方案。
- 在 17 个序列比较中，9 个 TUM 序列的平均 Sim(3) ATE 相对 VGGT-SLAM 2.0 基线从 0.1018 m 降至 0.0451 m。
- 锚定在全部 7 个无闭环模块消融中均有改善。
- 在 3 个 Clio 场景的固定闭环比较中，直接连接流程优于所测试的辅助子图流程。
- 单独的候选审计显示，短序列检查会额外拒绝视觉重叠的图像对。

### 局限性
- 摘要未说明方法在更大规模、更多场景类型或实时性方面的表现，摘要未提供足够信息。
- 摘要未给出失败案例、计算开销或对基础模型依赖程度的详细分析，摘要未提供足够信息。
- 摘要提到候选审计暴露额外拒绝，但未量化其对最终精度与召回的综合影响，摘要未提供足够信息。

### 阅读优先级
中。理由：论文聚焦 VGGT 类 SLAM 的尺度漂移与闭环一致性，给出了明确的基线对比和消融结果；但摘要仅覆盖有限数据集与指标，若关注几何基础模型 SLAM 的尺度与闭环问题，可作为相关方法阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：METRIC-GS: Selective Metric-Scale Estimation for 3D Gaussian Splatting
- 作者：Sooyeun Yang, Jongseong Brad Choi
- 出版日期：2026-11-04T06:17:08Z
- 分类：主分类 Geometry Foundation Models；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.06020 ；PDF https://arxiv.org/pdf/2611.06020

### 一句话总结
该论文提出 METRIC-GS，一种面向真实室内照片的选择性尺度估计器：它利用 3DGS 重建自身的语义内容推断度量尺度，并在证据不足时显式拒绝估计；拒绝的样本再被路由到 MASt3R，以减少对重量级度量模型的调用。

### 研究问题
3D Gaussian Splatting 重建继承了来自 structure-from-motion 的任意单位，因此在没有外部提供尺度时，无法被测量，也无法用于放置 AR 内容。摘要指出，两种标准做法在真实拍摄上都很脆弱：在五个具有卷尺测量天花板的室内场景上，分位数地板到天花板启发式误差为 27%，而度量深度对齐在三个网络上误差为 35-71%。因此，论文关注如何为真实室内照片的 3DGS 重建估计度量尺度，并避免在证据薄弱时给出不可靠估计。

### 核心思路/方法
METRIC-GS 是一个选择性尺度估计器，它从重建自身的语义内容中读取尺度，并且重要的是，在证据薄弱时拒绝估计。其方法包括：
- 使用冻结的 2D 教师模型，通过可见性感知投票为 Gaussian 打标签；
- 对建筑和家具类别（门、桌子、地板到天花板的间隙）使用实例级尺寸先验，并通过鲁棒的最大似然步骤融合；
- 使用 inlier-mass 检验将薄弱证据转化为显式弃权，该弃权同时作为路由到重量级度量模型（MASt3R）的机制。

摘要还提到，可见性感知投票将估计器可作用的场景从 16 个提高到 28 个，且部署精度不变。

### 主要贡献
- 提出选择性尺度估计器 METRIC-GS，基于重建自身语义内容估计尺度，并在证据不足时显式弃权。
- 在 47 个带激光真值的 ScanNet++ 场景上，配置在公开评估前冻结：该估计器单独将启发式的平均误差从 21.1% 降至 16.6%，在其作用的 28 个场景上为 9.3%，每场景约 11 秒。
- 提出选择性混合配置：仅将拒绝样本路由到 MASt3R，可在调用次数减少 60% 的情况下匹配“处处运行 MASt3R”的效果；摘要称 MASt3R 仍是更准确的独立估计器（9.9%）。
- 可见性感知投票将估计器可作用的场景从 16 个提高到 28 个，部署精度不变。
- 在自有的 13 个手机和无人机拍摄上，MASt3R 有 12 次未通过自身注册门限；系统在其作用的 5 个拍摄上均有改善且无退化。
- 报告当前前馈度量模型在其训练混合内基准上得分为 2.3%，在未见过的拍摄上为 28-35%，说明已发表的度量尺度数字是最佳情况，而非部署估计。

### 局限性
- 摘要显示，MASt3R 仍是更准确的独立估计器（9.9%），METRIC-GS 单独估计的平均误差为 16.6%，在其作用的 28 个场景上为 9.3%，因此单一估计器精度仍有限。
- 方法依赖语义内容与实例级尺寸先验，并在证据薄弱时弃权；摘要未提供弃权率、失败场景类型或先验覆盖范围的详细分析。
- 在自有的 13 个手机和无人机拍摄上，系统仅作用于 5 个拍摄；其余场景的行为与原因摘要未提供足够信息。
- 关于计算开销，仅提供约 11 秒每场景的估计器运行时间；混合路由的总体开销、内存需求等摘要未提供足够信息。
- 关于不同室内布局、类别分布或极端拍摄条件下的泛化能力，摘要未提供足够信息。

### 阅读优先级
中。理由：该论文聚焦 3DGS 的度量尺度估计与选择性弃权/路由机制，问题定义清晰，并给出 ScanNet++ 激光真值评估与自采手机/无人机数据结果；但摘要显示其独立估计精度仍低于 MASt3R，主要价值在于减少重量级模型调用并显式处理证据不足。对于关注 3DGS 度量尺度、AR 内容放置或基础模型路由的研究者有参考价值；若关注更高精度的独立度量估计，则需结合全文进一步判断。

</details>

<details>
<summary>Abstract</summary>

A 3D Gaussian Splatting (3DGS) reconstruction inherits arbitrary units from structure-from-motion, so it cannot be measured or used to place AR content until someone supplies a scale. Both standard recipes are fragile on real captures: on five indoor scenes with tape-measured ceilings, a quantile floor-to-ceiling heuristic errs by 27% and metric-depth alignment by 35-71% across three networks. We present METRIC-GS, a selective scale estimator for real indoor photographs: it reads the scale off the reconstruction's own semantic content and, just as importantly, refuses when the evidence is thin. A frozen 2D teacher labels Gaussians by visibility-aware voting; instance-level size priors for architectural and furniture classes (doors, tables, the floor-to-ceiling gap) are fused by a robust maximum-likelihood step; and an inlier-mass test turns thin evidence into an explicit abstention that doubles as a router to a heavyweight metric model. On 47 ScanNet++ scenes with laser ground truth, with a configuration frozen before public evaluation, the estimator alone cuts the heuristic's mean error from 21.1% to 16.6% (9.3% on the 28 scenes it acts on) at ~11 s per scene. MASt3R remains the more accurate standalone estimator (9.9%), but routing only our refusals to it matches running it everywhere with 60% fewer invocations; this selective hybrid is the configuration we advocate. Visibility-aware voting raises the scenes the estimator can act on from 16 to 28 at unchanged deployed accuracy. Applied unchanged to 13 phone and drone captures of our own, on which MASt3R fails its own registration gate 12 times, the system improves all five captures it acts on and degrades none. We also report that a current feed-forward metric model scores 2.3% on a benchmark inside its training mixture and 28-35% on captures it has never seen: a published metric-scale number is a best case, not a deployment estimate.

</details>

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-08 - Kinematic Total-Body PET Video Reconstruction via Hierarchical List-Mode EM and Validation-Adaptive Space-Time Regularisation

**Authors:** Andrew J. Reader, Gary J. R. Cook, Paul K. Marsden, Sarah-May Gould, Alexander Hammers, Simon R. Cherry
**Links:** [abs](https://arxiv.org/abs/2611.11052) - [pdf](https://arxiv.org/pdf/2611.11052)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>Abstract</summary>

Kinematic PET is introduced as an imaging task focused on visualisation of early radiotracer delivery and rapid multi-organ motion without gating. The proposed kinematic video reconstruction method uses 33-ms frames (~30 frames per second), initialised with 3D expectation maximisation (EM) time of flight (TOF) list-mode reconstruction, followed by cycles of a 2-stage update. These 2 stages are i) a hierarchical EM (HEM) update using multiple temporal pooling levels, and ii) a validation-adaptive space-time (VAST) regularisation update. HEM combines frame-specific EM corrections with corrections estimated from higher-count temporal blocks, slowing noise amplification for the ultrashort frames. VAST mixes each 3D target patch in a frame with source patches sampled nearby in space and time. It selects the candidate that best matches the mean of the corresponding patches in the two adjacent frames, with the unchanged patch also eligible. Optional temporal block sum correction uses the initial EM temporal sum as a reference to reduce loss of spatial detail. HEM+VAST was evaluated with a dynamic digital phantom, and demonstrated on human FDG data acquired on a Siemens Biograph Vision Quadra (28 - 58 s post-injection). At a background spatial coefficient of variation of 10%, the temporal full width at half maximum of the fastest phantom bolus was 151 ms with HEM+VAST, compared with 86 ms for the ground truth. The video frame rate FDG images reveal vascular and organ detail, radiotracer bolus passage and respiration-related multi-organ motion. Kinematic PET could complement conventional dynamic PET by supporting the development of image-derived physiological biomarkers and motion estimation for quantitative reconstruction. Future work should compare HEM+VAST with prior 4D PET reconstruction methods at the same 33-ms frame duration and matched noise levels.

</details>

#### 2026-11-05 - SM4RT: Cascaded Feed-forward Model for 4D Reconstruction

**Authors:** Pang-Chi Lo, Jhao-Syun Lai, Tsung-Wei Ke
**Links:** [abs](https://arxiv.org/abs/2611.08436) - [pdf](https://arxiv.org/pdf/2611.08436)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** geometric reasoning, 4D reconstruction, dynamic scene reconstruction, scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SM4RT: Cascaded Feed-forward Model for 4D Reconstruction
- 作者：Pang-Chi Lo, Jhao-Syun Lai, Tsung-Wei Ke
- 出版日期：2026-11-05T18:28:38Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.08436) | [PDF](https://arxiv.org/pdf/2611.08436)

### 一句话总结
SM4RT 是一个多任务级联前馈模型，先重建 3D 几何，再基于预测结构估计运动，用于从 RGB 视频进行动态场景重建。

### 研究问题
现有前馈方法通常将几何重建与运动估计分开处理，且往往在单一坐标系中预测运动，需要额外应对相机运动带来的歧义；同时真实世界的运动标注稀疏。论文旨在解决动态场景中几何与运动联合重建的上述问题。

### 核心思路/方法
SM4RT 采用级联方式依次完成两项任务：先重建 3D 几何，再以预测出的结构为基础引导运动估计。模型将每个像素的 3D 运动表达在其对应的相机坐标系中，以降低相机运动引起的歧义。针对运动标签稀疏问题，引入弱监督损失，利用另一时间步的已标注点位置约束未标注点的运动。模型为多任务前馈架构。

### 主要贡献
- 提出级联前馈框架 SM4RT，将几何重建与运动估计顺序结合，而非分开处理。
- 在对应相机坐标系中表达逐像素 3D 运动，以缓解相机运动带来的歧义。
- 引入弱监督损失，利用另一时间步的标注点位置正则化未标注点运动，应对真实运动标签稀疏问题。
- 在 Kubric、Waymo、Point Odyssey 三个动态场景数据集上评估运动估计，据摘要称在多数指标上优于先前基线；并在五个动态场景数据集上评估几何重建，据摘要称达到与 state-of-the-art 方法有竞争力的表现。
- 摘要指出该统一框架表明级联结合几何重建与运动估计不仅避免性能权衡，还能通过改善几何推理增强运动估计。

### 局限性
- 摘要未提供足够信息说明具体网络结构、参数量、训练细节与推理效率。
- 摘要未提供足够信息说明弱监督损失的具体形式与权重设置。
- 摘要未提供足够信息说明各数据集上的具体数值结果、对比基线细节及失败案例。
- 摘要未提供足够信息说明方法在非动态场景、极端相机运动或标注极少条件下的表现。

### 阅读优先级
中。理由：论文主题属于动态/4D 重建中的几何与运动联合估计，级联前馈与相机坐标系运动表达的思路具有一定方法参考价值；但摘要仅给出高层描述与有限实验结论，未提供足够细节判断其实际效果与可复现性，适合在需要了解该方向新框架时进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

We introduce SM4RT, a multi-task cascade feed-forward model for dynamic scene reconstruction from RGB videos. While existing feed-forward approaches typically address geometry reconstruction and motion estimation separately--and often predict motions in a single coordinate frame that must account for camera movement--SM4RT solves these tasks sequentially by first reconstructing 3D geometry and then bootstrapping motion estimation from the predicted structure. By expressing each pixel's 3D motion in its corresponding camera frame, SM4RT reduces ambiguity arising from camera motion. To address the sparsity of real-world motion labels, SM4RT further incorporates a weakly supervised loss that regularizes unlabeled point motions using labeled point positions at the other time step. We evaluate motion estimation on three dynamic-scene datasets--Kubric, Waymo, and Point Odyssey--and SM4RT achieves the best performance on most metrics compared with prior baselines. We additionally benchmark geometry reconstruction on five dynamic scene datasets and show that SM4RT achieves competitive performance with state-of-the-art methods. Overall, our unified framework demonstrates that combining geometry reconstruction and motion estimation in a cascade not only avoids performance trade-offs but also enhances motion estimation through improved geometric reasoning.

</details>

#### 2026-11-05 - InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image

**Authors:** Chanho Kim, Muhammad Salman Ali, Kyeonghwan Gwak, Muhammad Shaheryar, Incheol Park, Jeongwan On, Seungryul Baek
**Links:** [abs](https://arxiv.org/abs/2611.08330) - [pdf](https://arxiv.org/pdf/2611.08330)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** avatar reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image
- 作者：Chanho Kim, Muhammad Salman Ali, Kyeonghwan Gwak, Muhammad Shaheryar, Incheol Park, Jeongwan On, Seungryul Baek
- 出版日期：2026-11-05T17:21:08Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.08330 ；PDF https://arxiv.org/pdf/2611.08330

### 一句话总结
InstantHand 提出一种前馈框架，利用现成的 MANO、相机与掩码估计，从单张图像直接构建可动画的 3D Gaussian 手部 avatar，无需测试时优化，并针对轮廓监督不足与外观颜色漂移提出两项正则/迁移策略。

### 研究问题
论文关注从单张图像重建可动画手部 avatar 的问题。摘要指出，现有手部 avatar 重建通常依赖多视角采集或逐受试者优化，限制了可扩展性。本文试图在无需测试时优化的前提下，以单图输入构建可动画的 3D Gaussian 手部 avatar。摘要还指出两个具体问题：图像平均损失对 alpha 泄漏监督不足，导致细手指轮廓变厚；从图像特征回归的颜色即使在观测区域也可能漂向学习到的先验。

### 核心思路/方法
- 采用前馈框架，从单张图像构建可动画的 3D Gaussian 手部 avatar。
- 使用现成的 MANO、相机和掩码估计作为输入条件，不进行测试时优化。
- 提出 Soft Alpha Band 正则器，将监督集中在轮廓边界，以缓解图像平均损失对 alpha 泄漏监督不足、细手指轮廓变厚的问题。
- 提出 Reliability-gated Appearance Transfer：根据每个 Gaussian 的渲染贡献迁移源颜色，以保留观测外观；同时以全局源身份为条件，用学习到的先验补全未观测区域，以缓解颜色向先验漂移的问题。
- 摘要报告构建 avatar 用时 2.84 秒，渲染速度 161 FPS。

### 主要贡献
- 提出 InstantHand：一种从单张图像前馈构建可动画 3D Gaussian 手部 avatar 的框架，无需测试时优化，依赖现成 MANO、相机和掩码估计。
- 提出 Soft Alpha Band regularizer，针对轮廓边界集中监督，以改善 alpha 泄漏导致的细手指轮廓变厚问题。
- 提出 Reliability-gated Appearance Transfer，按 Gaussian 渲染贡献迁移源颜色以保留观测外观，并用全局源身份条件化的先验补全未观测区域。
- 摘要称其在 InterHand2.6M 上匹配逐受试者优化基线，在 HanCo 的零样本评估中保持竞争力，并给出 2.84 秒构建与 161 FPS 渲染的效率指标。

### 局限性
- 摘要未提供足够信息说明方法在遮挡、极端姿态、手部与物体交互或低质量输入条件下的具体表现。
- 摘要未提供足够信息说明对 MANO、相机和掩码估计质量的敏感程度及失败案例。
- 摘要未提供足够信息说明 Soft Alpha Band 正则器与 Reliability-gated Appearance Transfer 的消融细节和定量增益。
- 摘要未提供足够信息说明在 InterHand2.6M 与 HanCo 上的完整评估协议、指标定义及零样本评估的具体设置。
- 摘要未提供足够信息说明方法对非手部区域、背景或全身场景的适用性。

### 阅读优先级
中。理由：该论文聚焦单图前馈手部 avatar 重建，问题定义清晰，且给出构建时间与渲染帧率等效率指标，对动态/4D 重建与神经场景表示渲染方向有参考价值；但摘要未提供充分实验细节与消融结果，是否值得优先精读需结合全文的实验完整性与与自身研究方向的相关性判断。

</details>

<details>
<summary>Abstract</summary>

Hand avatar reconstruction typically relies on multi-view capture or per-subject optimization, limiting its scalability. We introduce InstantHand, a feed-forward framework that constructs an animatable 3D Gaussian hand avatar from a single image using off-the-shelf MANO, camera, and mask estimates, without test-time optimization. Image-averaged losses provide insufficient supervision for alpha leakage, which thickens thin finger contours. To address this issue, we propose a Soft Alpha Band regularizer that concentrates supervision on silhouette boundaries. Furthermore, colors regressed from image features can drift toward a learned prior even in observed regions. Our Reliability-gated Appearance Transfer preserves observed appearance by transferring source colors according to each Gaussian's rendering contribution, while completing unobserved regions using the learned prior conditioned on global source identity. InstantHand constructs an avatar in 2.84 seconds and renders at 161 FPS, matching per-subject-optimized baselines on InterHand2.6M and remaining competitive in zero-shot evaluation on HanCo.

</details>

#### 2026-11-05 - XM4D: 4D Reconstruction through Certifiable Geometric Optimization

**Authors:** Haoyu Han, Jack Benarroch Jedlicki, Jiahui Lei, Heng Yang
**Links:** [abs](https://arxiv.org/abs/2611.07902) - [pdf](https://arxiv.org/pdf/2611.07902)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** depth prediction, 4D reconstruction, non-rigid reconstruction, dynamic Gaussian, bundle adjustment, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：XM4D: 4D Reconstruction through Certifiable Geometric Optimization
- 作者：Haoyu Han, Jack Benarroch Jedlicki, Jiahui Lei, Heng Yang
- 出版日期：2026-11-05T12:20:52Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.07902 ；PDF https://arxiv.org/pdf/2611.07902

### 一句话总结
XM4D 将 4D 重建中的相机运动估计与非刚性形变估计分离，分别建模为可验证全局最优性的结构化 QCQP 并求解，再用所得几何初始化动态高斯泼溅进行光度细化。

### 研究问题
论文关注准确的 4D 重建问题：联合估计相机运动、场景几何与非刚性形变属于高度非凸优化，难以保证全局最优性。摘要指出，如何在保证精度与效率的同时获得可验证的全局最优性，是该方法要解决的核心问题。

### 核心思路/方法
- 总体框架：将相机运动估计与非刚性形变估计分离，两个阶段都形式化为结构化二次约束二次规划（QCQP），并给出半定规划（SDP）松弛与可验证的全局最优性证书。
- 相机运动估计：利用基础深度预测模型将静态点轨迹提升到 3D，构建同时估计相机位姿、深度尺度与静态路标的缩放式 bundle adjustment 问题；通过解析消去平移与路标，将问题约化为关于缩放旋转的 QCQP。
- 非刚性重建：使用嵌入式形变图（EDG）表示动态运动，并说明其跟踪、刚性与时序正则目标同样可约化为仅含旋转的 QCQP。
- 求解方式：两个问题均采用 SDP 松弛，并使用基于黎曼优化的 GPU 加速 Burer–Monteiro 求解器高效求解。
- 后续细化：恢复的几何用于初始化动态高斯泼溅，以进行光度细化。

### 主要贡献
- 提出 XM4D 框架，以可证明全局最优的几何优化为基础实现 4D 重建。
- 通过分离相机运动与非刚性形变，将两个阶段分别转化为结构化 QCQP，并提供 SDP 松弛与可验证的全局最优性证书。
- 在相机运动阶段，通过解析消去平移与路标，把缩放式 bundle adjustment 约化为缩放旋转上的 QCQP。
- 在非刚性阶段，基于 EDG 将跟踪、刚性与时序正则目标约化为仅含旋转的 QCQP。
- 使用 GPU 加速的 Burer–Monteiro 黎曼优化求解器处理 SDP 松弛，并以恢复几何初始化动态高斯泼溅进行光度细化。
- 摘要称在七个基准上进行了广泛实验，展示了静态与动态场景中的准确相机运动估计、可扩展到数千帧的高效优化，以及当前最优的新视角渲染质量。

### 局限性
- 摘要未提供足够信息说明失败情形、对基础深度预测模型误差的敏感性、SDP 松弛在何种条件下保证紧致性，以及计算开销的具体量级。
- 摘要未提供足够信息说明七个基准的具体构成、评测协议、与基线方法的定量对比细节及消融实验结果。
- 摘要未提供足够信息说明方法对极端非刚性运动、遮挡、弱纹理或大规模场景的适用边界。

### 阅读优先级
高。理由：摘要明确针对 4D 重建中非凸优化与全局最优性保证这一核心难题，提出可验证最优性的 QCQP/SDP 建模路线，并覆盖相机运动、非刚性形变与动态高斯泼溅细化；若关注动态/4D 重建与神经场景表示，该论文的问题设定和方法框架具有较高阅读价值。但需注意，摘要未给出定量实验细节，阅读全文时应重点核查全局最优性证书的实际适用条件与实验支撑。

</details>

<details>
<summary>Abstract</summary>

Accurate 4D reconstruction remains challenging: jointly estimating camera motion, scene geometry, and non-rigid deformation entails highly nonconvex optimization, making global optimality difficult to guarantee. We present XM4D, a framework for accurate and efficient 4D reconstruction built upon certifiably globally optimal geometric optimization. By separating the estimation of camera motion from non-rigid deformation, we formulate both stages as structured quadratically constrained quadratic programs (QCQP) that admit semidefinite programming (SDP) relaxations and verifiable global optimality certificates. For camera motion estimation, we lift static point tracks into 3D using foundational depth prediction models and formulate a scaled bundle adjustment problem that jointly estimates camera poses, depth scales, and static landmarks. By analytically eliminating translations and landmarks, we reduce the problem to a QCQP over scaled rotations. For non-rigid reconstruction, we represent dynamic motion using an embedded deformation graph (EDG) and show that its tracking, rigidity, and temporal regularization objectives similarly reduce to a rotation-only QCQP. Both problems admit SDP relaxations that we solve efficiently with a GPU-accelerated Burer-Monteiro solver based on Riemannian optimization. The recovered geometry further initializes dynamic Gaussian splatting for photometric refinement. Extensive experiments across seven benchmarks demonstrate accurate camera motion estimation on both static and dynamic scenes, efficient optimization that scales to thousands of frames, and state-of-the-art novel-view rendering quality.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-09 - Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks

**Authors:** Hao Gu, Jin Yao, Zezhou Cheng
**Links:** [abs](https://arxiv.org/abs/2611.12875) - [pdf](https://arxiv.org/pdf/2611.12875)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, geometric reconstruction

<details>
<summary>Abstract</summary>

Despite impressive progress, existing feed-forward large 3D reconstruction models produce a single, irrevocable prediction. When these models fail, there is no mechanism to correct their mistakes. To address this limitation, we introduce Click3R, a framework for interactive geometric correction of feed-forward models using sparse human correspondence clicks. Given an image pair and a small set of cross-view point correspondences provided by a user, Click3R injects geometric constraints into the 3D reconstruction networks through a lightweight point correspondence adapter, enabling the model to resolve ambiguities in challenging scenarios such as repetitive textures, symmetric structures, large viewpoint changes, or textureless regions. To evaluate interactive reconstruction, we curate a challenging benchmark specifically designed to expose failure modes of existing feed-forward 3D reconstruction methods. Experiments show that Click3R reduces reconstruction error with as few as a single correspondence click, improving performance on both standard and our curated benchmarks. Our results highlight that sparse human interaction provides an effective and practical mechanism for correcting geometric reconstruction errors.

</details>

#### 2026-11-09 - A forensic evaluation framework for egocentric foundation models: an EFM3D case study for crime scene reconstruction

**Authors:** Davidson Chisom Onwubiko, Shahana Bano, Carlos Francisco Moreno-García
**Links:** [abs](https://arxiv.org/abs/2611.12259) - [pdf](https://arxiv.org/pdf/2611.12259)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, scene understanding

<details>
<summary>Abstract</summary>

Foundation models increasingly combine geometry, semantics, and spatial context for three-dimensional scene understanding, but their suitability for forensic crime scene reconstruction remains unclear. This study presents a structured forensic evaluation framework for egocentric foundation models and demonstrates it using the Egocentric Foundation Model for 3D (EFM3D). Four simulated indoor crime scenes were recorded with Meta Project Aria Gen~1 at Robert Gordon University's East Lodge House forensic training facility. The framework evaluates room-scale reconstruction, semantic scene understanding, computational performance, and forensic suitability. Across the four scenes, EFM3D generated meshes averaging $12{,}668\pm2{,}430$ vertices and $24{,}838\pm4{,}903$ faces, with 39,529 recorded semantic predictions spanning 21--24 categories at a mean confidence of 0.40. Because reference meshes and expert-labelled 3D ground truth were unavailable, these statistics are treated as descriptive outputs rather than measures of geometric or detection accuracy. Final inference runs processed $1{,}388\pm203$ snippets per scene at $0.69\pm0.01$ samples/s and required $50.77\pm6.12$ minutes per recording. A seven-criterion capability profile indicated stronger support for room geometry, furniture localisation, scene context, and spatial relationships than for fine-scale forensic evidence. The results position EFM3D as a complementary tool for contextual documentation and scene review rather than a replacement for high-fidelity forensic capture. The framework provides a reproducible basis for evaluating future egocentric foundation models in specialised forensic settings.

</details>

#### 2026-11-09 - DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing

**Authors:** Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta, Xin He
**Links:** [abs](https://arxiv.org/abs/2611.12038) - [pdf](https://arxiv.org/pdf/2611.12038)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** metric depth, scene reconstruction, simultaneous localization and mapping, SLAM, visual SLAM, camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping, localization

<details>
<summary>Abstract</summary>

This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Dynamic observations can contaminate camera tracking and scene reconstruction in visual SLAM (simultaneous localization and mapping). Although 3DGS (3D Gaussian splatting) enables efficient dense mapping, existing 3DGS-SLAM systems may exhibit instability when dynamic objects violate their underlying static-scene assumption. Excluding dynamic observations can reduce their influence on tracking and mapping, but may leave occluded static backgrounds missing or weakly constrained. Our proposed DPGS-SLAM is a monocular RGB SLAM framework that supports provisional representations of insufficiently observed static backgrounds through asynchronous diffusion-based background completion and provenance-aware Gaussian mapping. Dynamic regions are identified through optical-flow-based motion discovery and temporally consistent mask propagation by SAM2 (segment anything model 2). For selected keyframes, a fine-tuned diffusion inpainting model generates plausible background appearance in occluded regions, while Metric3D v2 predicts metric depth from the completed images to initialize provisional Gaussian primitives. Provenance labels distinguish generated primitives from observation-supported primitives, excluding generated content from camera-pose estimation and observed-map optimization. When previously occluded backgrounds become visible, eligible generated primitives are removed, and observation-supported primitives are independently initialized from real RGB observations and predicted depth. Experimental results demonstrated competitive camera tracking, with average ATE RMSE values of 1.2 cm on TUM RGB-D and 2.7 cm on BONN RGB-D. On StaDy4D, DPGS-SLAM improved average PSNR by 4.60 dB over WildGS-SLAM using only monocular RGB input.

</details>

#### 2026-11-09 - HIST3R: Decomposing and Rectifying State Updates with History for Streaming 3D Reconstruction

**Authors:** Kenneth Yang, Yu-Chiang Frank Wang
**Links:** [abs](https://arxiv.org/abs/2611.12011) - [pdf](https://arxiv.org/pdf/2611.12011)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, camera pose estimation, pose estimation, depth estimation, scene understanding

<details>
<summary>Abstract</summary>

Streaming 3D reconstruction with recurrent states enables long-video scene understanding under bounded memory, but turns reconstruction into a state-evolution problem: each incoming frame updates a compact scene memory on which all subsequent predictions depend, so unreliable updates overwrite historical context and accumulate into long-horizon geometric drift. We analyze CUT3R-style recurrent updates through a direction--magnitude decomposition, in which the magnitude sets the update gain, i.e., how strongly an observation is written into the state, and the direction encodes the geometric intent, i.e., where the update drives the state. This decomposition provides a unified view of CUT3R and its variants, revealing that existing training-free extensions perform magnitude-only control: they can attenuate an unreliable update but cannot correct its direction. We propose HIST3R, a training-free framework built on CUT3R that controls both components using history. HIST3R rectifies the update direction using locally consistent historical states, and modulates the update magnitude according to the visual discrepancy between the current observation and its history, suppressing redundant updates while preserving complementary evidence. Across camera pose estimation, 3D reconstruction, and video depth estimation, HIST3R consistently improves long-horizon performance while retaining the memory footprint and inference speed of CUT3R. With 1000 input frames, it reduces ATE by 23.87% on ScanNet and 33.65% on TUM-Dynamics relative to the strongest competing method; with 500 frames, it improves median reconstruction accuracy over the strongest CUT3R-based variant by 56.52% on 7-Scenes and 33.96% on NRGBD.

</details>

#### 2026-11-09 - 3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model

**Authors:** Zixiang Ai, Zhenyu Cui, Xu Zou, Jiahuan Zhou
**Links:** [abs](https://arxiv.org/abs/2611.11964) - [pdf](https://arxiv.org/pdf/2611.11964)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, scene reconstruction

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models have demonstrated strong generalization under large-scale pre-training, yet they struggle in long-tail scenarios such as low-light reconstruction, joint human-scene reconstruction, and test-time adaptation. We observe relational attention structure collapse, manifested as the failure of cross-view correspondences, as a primary cause of these limitations. While adaptation offers a practical way to bridge this gap, existing parameter-efficient fine-tuning (PEFT) approaches mainly perform channel-wise feature adjustment and lack mechanisms to explicitly adapt relational structures, leaving correspondence failures unresolved. In this work, we formulate adaptation of 3D reconstruction models as a problem of correspondence recovery under domain shift and propose 3R-Adapter, a PEFT paradigm for long-tail 3D reconstruction scenarios. Our method consists of three components: Deformable Retrieval for task-adaptive relation candidate retrieval, Relational Rewiring for reconstructing cross-view relational structures, and Consistency Refinement for injecting the rewired relations into stable predictions. Extensive experiments on low-light reconstruction, joint human-scene reconstruction, and test-time adaptation demonstrate that our approach significantly improves robustness over existing PEFT methods while maintaining efficient lightweight adaptation. Our code is released at https://github.com/PKU-OV3-LAB/3R-Adapter.

</details>

#### 2026-11-09 - Scale-Consistent Monocular Fisheye Visual Odometry via Spherical Bundle Adjustment-Guided Unsupervised Depth Learning

**Authors:** Wanhui Luo, Hongbo Zhao, Yi Zhou, Qijun Chen, Yiming Nie, Rui Fan
**Links:** [abs](https://arxiv.org/abs/2611.11934) - [pdf](https://arxiv.org/pdf/2611.11934)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, bundle adjustment, depth estimation, view synthesis, mapping, localization

<details>
<summary>Abstract</summary>

The wide field of view of fisheye cameras and the simplicity of a monocular setup make monocular fisheye visual odometry (VO) attractive for robotic localization and mapping. Nevertheless, scale drift remains a major challenge over long trajectories. Unsupervised depth learning can help to mitigate this issue, but the pronounced distortion of fisheye images poses challenges for accurate depth estimation. This article presents S$^2$D-FVO, a monocular fisheye VO framework integrating spherical bundle adjustment (SBA)-guided unsupervised depth learning to improve scale consistency and depth estimation accuracy. Given that pixel reprojection residuals do not uniformly reflect angular deviations between viewing rays and that the first-order linearization of a scalar angular reprojection residual is insensitive to perturbations along one tangent direction, SBA employs tangent-space angular reprojection residuals derived from the spherical logarithmic map. These residuals retain sensitivity along both tangent directions, with their norms equal to the corresponding scalar angular residuals. A median depth-based scale regularization term is further integrated into SBA to constrain the reconstruction scale. Building on these formulations, SBA replaces the pose estimation network during unsupervised depth learning, providing more reliable relative poses for view synthesis. In turn, depth estimates from the well-trained depth estimation network provide scale references for SBA, improving scale consistency while allowing individual 3-D landmark positions to be refined. Extensive experiments conducted on multiple public datasets, as well as two newly collected large-scale datasets, demonstrate that the proposed framework outperforms representative existing approaches in both depth and trajectory estimation accuracy and is applicable to different camera models.

</details>

#### 2026-11-09 - Budget-aware Correspondence-driven View Selection for Real-time 3D Perception of Mobile Robots

**Authors:** Vaishnav Ramesh, Jacob Carter, Shivali J. Patel, Sanjeev J. Koppal, Md Jahidul Islam
**Links:** [abs](https://arxiv.org/abs/2611.11809) - [pdf](https://arxiv.org/pdf/2611.11809)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, structure from motion, SfM, camera pose estimation, pose estimation, robotics

<details>
<summary>Abstract</summary>

3D visual perception and scene reconstruction are critical for autonomous robots and intelligent transportation, yet real-world deployments often generate long, redundant image sequences that hinder downstream processing. This report investigates BCVS (budget-aware correspondence-driven view sampling), a pose-free view selection algorithm that offers 22+ FPS on a CPU, enabling online filtering for efficient 3D perception by mobile robots. Unlike existing approaches that rely on full structure-from-motion (SfM) pipelines or camera pose estimation, BCVS employs a purely correspondence-based scoring strategy that prioritizes view novelty while maintaining sufficient overlap for geometric stability. Given a user-specified budget, BCVS iteratively selects the most distinct frames and suppresses near-duplicates, producing compact subsets that preserve connectivity and minimize reconstruction loss. Extensive experiments on benchmark show that BCVS outperforms CPU-friendly baselines at tight budgets and remains competitive as budgets scale. Field trials with large aerial and marine robotics data further validate its practicality and scalability: BCVS reduces redundancy up to 16% while sustaining robust SfM registration and high-quality 3D reconstructions.

</details>

#### 2026-11-09 - Towards Rotation-Only Imaging Geometry: Multi-View Pose Estimation

**Authors:** Xinrui Li, Qi Cai, Yuanxin Wu
**Links:** [abs](https://arxiv.org/abs/2611.11770) - [pdf](https://arxiv.org/pdf/2611.11770)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM, pose estimation

<details>
<summary>Abstract</summary>

Global structure-from-motion (SfM) commonly refines relative poses on individual image pairs and then estimates global rotations by rotation averaging. Pairwise refinement does not explicitly combine feature-level constraints with multi-view consistency during rotation initialization. We introduce Global Rotations from Aggregated Matches (GRAM), which estimates global rotations directly from initial relative rotations and inlier matches by minimizing edge-wise rotation-only algebraic residuals. GRAM replaces two-view relative-pose optimization and rotation averaging with a single stage. We further extend rotation- only imaging geometry to multiple views and develop Multi-view Optimization with Rotation-only Reprojection Error (MORE) for nonlinear global rotation refinement. Analytical Rotation-guided Translation (ART) derives locally scaled triplet translations from Linear Global Translation (LiGT) constraints and recovers global translations using weighted least squares. Synthetic and real-world experiments demonstrate the accuracy, robustness, and efficiency of the proposed methods.

</details>

#### 2026-11-09 - LangDepth: Vision-Language Scene Priors for Semantic Binning and Cross-Domain Monocular Depth Estimation

**Authors:** Reyhaneh Ahani Manghotay, Jie Liang
**Links:** [abs](https://arxiv.org/abs/2611.11763) - [pdf](https://arxiv.org/pdf/2611.11763)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation, monocular depth

<details>
<summary>Abstract</summary>

Monocular depth estimation has advanced through large-scale pretraining and strong visual backbones, yet metric depth remains sensitive to scene-level scale. Indoor rooms and outdoor driving scenes occupy very different depth ranges, but most depth decoders infer this global structure implicitly from visual features. We ask whether scene-level semantic structure can instead act as an upstream prior that shapes the metric output space before dense prediction. We present LangDepth (SemanticBins), a monocular depth architecture that couples strong visual features with a scene-conditioned output space. A frozen CLIP encoder and a learnable bank of scene- and geometry-oriented concept keys convert image features into a compact scene descriptor, without requiring per-image text or an external captioner. A Scene Prior Module (SPM) maps this descriptor to a scene-conditioned metric depth interval, providing a global range anchor before dense decoding. In parallel, a DINOv2-L backbone with a lightweight FPN extracts dense visual features, and a Per-Pixel Assignment Network (PPAN) assigns pixels to the scene-prescribed bin structure. A confidence gate fuses the dense visual estimate with the SPM prior. We train LangDepth jointly on NYU Depth V2 and KITTI under a modest supervised depth budget, without web-scale depth supervision or pseudo-labelled depth data. A single model achieves delta_1 = 0.960 on NYU, 0.960 on KITTI, 0.887 on DIODE indoor, 0.946 on iBims-1, and 0.861 on SUN RGB-D. Beyond aggregate accuracy, the SPM predicts compact indoor ranges and much wider outdoor KITTI ranges, the gate becomes SPM-dominant on outdoor scenes, and perturbing the routed scene context causes large drops on KITTI and iBims-1. These results support scene-conditioned output spaces as a practical and interpretable mechanism for cross-domain monocular depth estimation.

</details>

#### 2026-11-08 - Martine: Benchmarking Multi-View 3D Surface Reconstruction Across Viewpoint Coverage, Resolution, and Lighting

**Authors:** Robin Bruneau, Baptiste Brument, Frederic Giraud, Bastian Sigrist, Sascha Jecklin, Philipp Fürnstahl, Bjoern Menze, Lilian Calvet
**Links:** [abs](https://arxiv.org/abs/2611.11602) - [pdf](https://arxiv.org/pdf/2611.11602)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** multi-view stereo, surface reconstruction, photogrammetry, camera calibration, Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Controlled acquisition setups are widely used for high-accuracy multi-view 3D surface reconstruction, as they allow sensor configuration, image resolution, viewpoint distribution, and illumination to be specified. Yet benchmarking remains difficult, since reconstruction accuracy depends jointly on the reconstruction paradigm, object properties, and acquisition regime. Existing benchmarks often restrict viewpoint coverage, resolution, or illumination, which can bias comparisons towards methods suited to the chosen setting. Others lack accurate 3D ground truth or quantified image-to-geometry alignment, limiting their use for metric surface evaluation. We introduce Martine, a benchmark for controlled 3D object surface reconstruction. Martine comprises 28 objects, including transparent materials and fine structures, captured at 9568 x 6376 pixels from 84 views over a spherical cap under both single-light and multi-light regimes. It provides object-independent camera calibration, accurate 3D ground-truth scans, calibration and image-to-geometry accuracy quantified on test images, and 3D property masks for analysing errors by material properties, visibility, curvature and fine structures. Experiments across photogrammetry, classical multi-view stereo, neural implicit surfaces, Gaussian-splatting-based reconstruction, and multi-view photometric stereo show that Martine enables regime-aware evaluation with explicit control over reference-data accuracy. The benchmark resolves sub-millimetric reconstruction differences, with a best observed Chamfer distance of 0.058 mm over the evaluated visible surface.

</details>

#### 2026-11-08 - TransArt3D: From Two States to Articulated 3D Reconstruction with Video Transition Priors

**Authors:** Chenhao Guan, Liying Yang, Xinxing Yu, Hao Mo, Tianshun Han, Renjun Gao, Yanyan Liang
**Links:** [abs](https://arxiv.org/abs/2611.11304) - [pdf](https://arxiv.org/pdf/2611.11304)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, robotics, localization, simulation

<details>
<summary>Abstract</summary>

Reconstructing interactable articulated assets from a few images is key to robotics and simulation, yet highly underconstrained. Existing optimization-based methods fit an articulated asset under a static 3D prior that scores each state independently, so per-state reconstruction errors leak into the estimated moving part and joint as false motion. Video diffusion models capture how objects move between states, but only implicitly in 2D. To this end, we present TransArt3D, an optimization-based framework that reconstructs an articulated 3D asset from two endpoint images by translating this video transition prior into explicit part structure and joint kinematics. It first lifts frames generated between the endpoints with a transition-coupled 3D consensus that applies the static 3D prior jointly across frames, stabilizing unchanging regions and initializing the parts and joint. A rectified-flow kinematic refinement then lets the video prior supervise a 3D motion field over the whole transition, while part assignment and a shared joint constrain the field throughout optimization, keeping per-state errors out of the articulation. Finally, a motion-aware canonical appearance fusion uses the recovered articulation to map both endpoint images onto one canonical surface, texturing regions that only one state reveals. On PartNet-Mobility, TransArt3D outperforms methods given the same two endpoints in geometry and joint accuracy, and surpasses methods given six observed states in articulated-state geometry, joint localization and appearance.

</details>

#### 2026-11-05 - PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation

**Authors:** Chuanxin Song, Peixi Peng
**Links:** [abs](https://arxiv.org/abs/2611.07873) - [pdf](https://arxiv.org/pdf/2611.07873)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** motion trajectories, depth estimation, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation
- 作者：Chuanxin Song, Peixi Peng
- 出版日期：2026-11-05T11:47:33Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.07873；PDF https://arxiv.org/pdf/2611.07873

### 一句话总结
论文提出全景视频深度估计数据集 PanoCARLA 与端到端框架 PVDepth，通过球面感知噪声初始化与立方体贴图校正时序建模，缓解 ERP 全景视频中几何畸变和非线性时序动态带来的迁移困难。

### 研究问题
全景视频深度估计对虚拟现实和世界模型等应用重要，但领域进展受两个障碍制约：一是大规模训练数据稀缺；二是等距柱状投影（ERP）特有的时空挑战，使透视视频深度模型难以直接迁移。论文关注的核心问题是：如何让源自透视视频的深度模型适应 ERP 全景视频中的几何畸变与非线性的时序动态。

### 核心思路/方法
论文首先构建 PanoCARLA，一个大规模合成 RGB-D 全景视频数据集，具有自然运动轨迹和类无人机漫游视角。在此基础上提出 PVDepth，一个从透视视频深度模型改造而来的端到端框架。针对 ERP 特有的几何畸变及其导致的非线性时序动态，论文引入两个核心机制：
1. Progressive Sphere-aware Noise Initialization：将噪声分布从平面退火到球面，引导模型适应非均匀的信息密度；
2. Cube-rectified Temporal Modeling：引入辅助的立方体贴图时序分支，用于校正 ERP 域中的非线性时序动态。

### 主要贡献
- 提出 PanoCARLA 大规模合成 RGB-D 全景视频数据集，包含自然运动轨迹与类无人机漫游视角。
- 提出 PVDepth 端到端框架，将透视视频深度模型适配到全景视频深度估计。
- 设计 Progressive Sphere-aware Noise Initialization，以平面到球面的噪声分布退火应对 ERP 非均匀信息密度。
- 设计 Cube-rectified Temporal Modeling，借助辅助立方体贴图时序分支校正 ERP 域非线性时序动态。
- 摘要称大量实验显示 PVDepth 性能更优，能生成几何准确且时序一致的深度序列；代码和数据将公开。

### 局限性
- 摘要未提供足够信息说明 PanoCARLA 的规模、采集细节、场景多样性与标注质量。
- 摘要未提供足够信息说明实验设置、对比方法、评价指标与具体定量结果。
- 摘要未提供足够信息说明两个核心机制的计算开销、实时性或在真实全景视频上的泛化表现。
- 摘要未提供足够信息说明方法对非合成数据、不同 ERP 分辨率或极端运动场景的适用边界。

### 阅读优先级
高。理由：该论文同时针对数据稀缺与 ERP 时空适配两个明确瓶颈，提出数据集与端到端方法，并给出两个针对性机制；若关注全景视频深度估计、VR 或世界模型相关三维感知，摘要显示其问题设定与贡献较为直接相关。但具体实验证据与数据规模需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Panoramic video depth estimation is pivotal for applications such as Virtual Reality and World Models. However, advancements in this field are impeded by two primary obstacles: the scarcity of large-scale training data and the unique spatiotemporal challenges of Equirectangular Projection (ERP), which hinder the direct transfer of perspective models. In this paper, we first present PanoCARLA, a large-scale synthetic RGB-D panoramic video dataset, featuring natural motion trajectories and drone-like roaming perspectives. Building on this foundation, we propose PVDepth, an end-to-end framework adapted from perspective video depth models. To tackle ERP-specific geometric distortions and consequent non-linear temporal dynamics, we introduce two core mechanisms: (1) A Progressive Sphere-aware Noise Initialization strategy that anneals the noise distribution from planar to spherical, guiding the model to adapt to non-uniform information density; and (2) A Cube-rectified Temporal Modeling module that incorporates an auxiliary cubemap temporal branch to rectify non-linear temporal dynamics in the ERP domain. Extensive experiments demonstrate that PVDepth achieves superior performance, generating geometrically accurate and temporally consistent depth sequences. Code and data will be released at https:// github.com/ChuanxinSong/PVDepth.

</details>

#### 2026-11-05 - STAG-Net: Structure-Aware Attention over Landmark Groups for Lightweight Head Pose Estimation

**Authors:** Asiri Gawesha Lindamulage, Sanka Mohottala, Dharshana Kasthurirathna, Nuwan Kodagoda
**Links:** [abs](https://arxiv.org/abs/2611.07828) - [pdf](https://arxiv.org/pdf/2611.07828)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：STAG-Net: Structure-Aware Attention over Landmark Groups for Lightweight Head Pose Estimation
- 作者：Asiri Gawesha Lindamulage, Sanka Mohottala, Dharshana Kasthurirathna, Nuwan Kodagoda
- 出版日期：2026-11-05T11:09:34Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.07828 ；PDF https://arxiv.org/pdf/2611.07828

### 一句话总结
STAG-Net 是一种基于面部关键点组的结构感知注意力轻量头部姿态估计方法，摘要声称其在多个跨数据集和 subject independent 设置下取得对比方法中最低的平均绝对误差，同时显著降低参数量、FLOPs 与训练/推理成本。

### 研究问题
摘要指出，头部姿态估计对人机交互和驾驶员监控很重要，但许多基于图像的方法对资源受限部署而言成本仍然过高。论文关注如何在轻量化条件下，利用面部关键点进行头部姿态估计，并兼顾精度与训练、推理效率。

### 核心思路/方法
摘要给出的方法要点包括：
- 从面部关键点估计头部姿态；
- 使用 movement aware selection、空间聚类、紧凑 DeepSet 编码器、自注意力以及全局几何描述符；
- 在关键点组上施加结构感知注意力；
- 分别使用 FaceMesh 和 Face Alignment Network 关键点构建变体；
- 在 300W-LP、AFLW2000 和 BIWI 上，采用跨数据集和 subject independent 协议评估。

### 主要贡献
摘要中明确列出的贡献包括：
- 提出 STAG-Net，用于轻量头部姿态估计，并给出 FaceMesh 与 FAN 两种关键点变体；
- 在所有评估设置中，取得对比的基于关键点方法里最低的平均绝对误差；
- 在 BIWI 有效检测帧上，FAN 变体在跨数据集评估中达到 \(3.51^\circ\)，在 subject independent 评估中达到 \(2.39^\circ\)，为所有对比方法中最低总体误差；
- 回归器仅使用 0.012 至 0.043 百万参数和 24.1 至 83.6 千 FLOPs，摘要称 FLOPs 比 FSA-Net 少约三个数量级；
- 包含关键点提取与回归的 FaceMesh 流程在 Tesla T4 GPU 上达到 322.9 FPS，摘要称为最快被测图像基线 164.5 FPS 的近两倍，并在 CPU 上达到 111.0 FPS；
- 按数据集大小归一化后，训练样本处理速度比 FSA-Net 快七至八倍，比 HopeNet 和 TokenHPE 快一百倍以上，完整训练在 28 分钟内完成。

### 局限性
摘要未提供足够信息说明方法在极端姿态、遮挡、关键点检测失败场景下的鲁棒性，也未给出失败案例分析、跨域泛化边界或与更多非关键点方法的系统性比较细节。摘要未提供足够信息说明统计显著性、误差方差、模型鲁棒性消融的完整结果，以及不同硬件条件下的能耗或内存占用。摘要未提供足够信息说明训练数据规模、超参数敏感性及实际部署限制。

### 阅读优先级
中。理由：论文主题聚焦轻量头部姿态估计，摘要给出了较明确的精度、参数量、FLOPs、FPS 和训练时间对比，适合关注高效视觉模型与关键点姿态估计的读者；但摘要未展开方法细节和局限性分析，是否精读需结合对结构感知注意力、DeepSet 编码及跨数据集评估设计的兴趣。

</details>

<details>
<summary>Abstract</summary>

Head pose estimation is important for human computer interaction and driver monitoring, but many image based methods remain too costly for resource constrained deployment. We propose STAG-Net, a structure-aware attention over landmark groups for lightweight head Pose estimation that estimates head pose from facial landmarks using movement aware selection, spatial clustering, compact DeepSet encoders, self attention, and a global geometry descriptor. We develop variants using FaceMesh and Face Alignment Network landmarks and evaluate them under cross dataset and subject independent protocols on 300W-LP, AFLW2000, and BIWI. STAG-Net achieves the lowest mean absolute error among all compared landmark based methods in every evaluated setting. On BIWI frames with valid detections, the FAN variant also records the lowest overall error among all compared methods, reaching $3.51^\circ$ under cross dataset evaluation and $2.39^\circ$ under subject independent evaluation. The regressors use only 0.012 to 0.043 million parameters and 24.1 to 83.6 thousand FLOPs, about three orders of magnitude fewer FLOPs than FSA-Net. Despite including landmark extraction and regression, the FaceMesh pipeline reaches 322.9 frames per second on a Tesla T4 GPU, nearly twice the 164.5 frames per second of the fastest measured image based baseline, and 111.0 frames per second on CPU. After normalization by dataset size, STAG-Net processes training samples seven to eight times faster than FSA-Net and more than one hundred times faster than HopeNet and TokenHPE, while complete training finishes within 28 minutes. These results show that STAG-Net combines leading landmark based accuracy with substantially lower training and inference cost.

</details>

#### 2026-11-05 - Real-Time Event-Based LED Tracking and Pose Estimation with PWM-Encoded Markers

**Authors:** Junkai Niu, Sheng Zhong, Delei Kong, Xin Wang, Kaizhen Sun, Yusen Zhang, Mingzhen Gan, Yi Zhou
**Links:** [abs](https://arxiv.org/abs/2611.07630) - [pdf](https://arxiv.org/pdf/2611.07630)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-Time Event-Based LED Tracking and Pose Estimation with PWM-Encoded Markers
- 作者：Junkai Niu, Sheng Zhong, Delei Kong, Xin Wang, Kaizhen Sun, Yusen Zhang, Mingzhen Gan, Yi Zhou
- 出版日期：2026-11-05T08:16:07Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；无次要分类
- 链接：摘要页 https://arxiv.org/abs/2611.07630 ；PDF https://arxiv.org/pdf/2611.07630

### 一句话总结
论文提出一种基于事件相机的实时框架，通过脉冲宽度调制（PWM）编码的 LED 标记实现 LED 跟踪与六自由度相对位姿估计。

### 研究问题
论文关注在快速运动、运动模糊和高动态范围（HDR）光照条件下，如何利用事件相机对 LED 标记进行实时跟踪并估计 6-DoF 相对位姿。摘要指出需要解决多 LED 的身份关联、快速运动下的像素级跟踪以及实时度量位姿估计问题。

### 核心思路/方法
- 利用事件相机像素异步响应亮度变化、具备微秒级时间分辨率的特性，捕获 LED 的高频闪烁模式。
- 多个 LED 共享同一闪烁频率，并通过不同 PWM 占空比编码各自身份，以降低频率资源需求和计算成本。
- 采用双速率异步跟踪框架：低速率进行 LED 检测，高速率利用原始事件更新，从而在快速运动下保持 LED 身份关联和像素级跟踪。
- 根据 LED 身份与位置建立 2D-3D 对应关系，实现实时度量 6-DoF 相对位姿估计。

### 主要贡献
- 提出基于 PWM 编码 LED 标记的事件相机实时 LED 跟踪与 6-DoF 相对位姿估计框架。
- 设计多 LED 共享闪烁频率、以不同占空比区分身份的编码方式，减少频率资源需求和计算开销。
- 提出双速率异步跟踪框架，结合低速率检测与高速率原始事件更新，提升快速运动下的身份关联与跟踪稳定性。
- 在自采集数据集上进行广泛评估，摘要称其在大运动流和图像平面 LED 瞬态重叠下具有鲁棒性。
- 构建由四旋翼和麦轮移动机器人组成的协同机器人平台，在时变 HDR 光照下通过悬停和目标跟随实验展示闭环无人机引导潜力，并在 NVIDIA Jetson Orin NX 上板载部署。
- 摘要称将公开数据集和实现以促进后续研究。

### 局限性
- 摘要未提供足够信息说明方法在极端遮挡、LED 完全重叠或非 HDR 场景下的具体表现。
- 摘要未提供足够信息说明自采集数据集的规模、标注方式、对比基线及定量误差指标。
- 摘要未提供足够信息说明计算资源消耗、实时性具体帧率或延迟数据。
- 摘要未提供足够信息说明 PWM 占空比编码在 LED 数量增加时的可扩展性上限。
- 摘要未提供足够信息说明户外强光、远距离或低信噪比条件下的失效边界。

### 阅读优先级
中。理由：论文面向事件相机、LED 标记跟踪与实时 6-DoF 位姿估计，属于 3D 重建与多视图几何相关方向，且包含机器人平台闭环实验与板载部署信息；但摘要未给出定量实验细节和与现有方法的对比结果，是否具有显著性能优势需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Event cameras are neuromorphic vision sensors with pixels that independently and asynchronously respond to brightness changes at microsecond resolution, supporting state estimation under rapid motion, motion blur, and high dynamic range (HDR) illumination. This also enables capture of high-frequency blinking patterns from light-emitting diodes (LEDs). Based on this, we propose a real-time event-based framework for LED tracking and six-degree-of-freedom (6-DoF) relative pose estimation using pulse-width modulation (PWM)-encoded LED markers. Multiple LEDs share a common blinking frequency and encode identities through distinct PWM duty cycles, reducing frequency-resource requirements and computational cost. Our dual-rate asynchronous tracking framework combines low-rate LED detection with high-rate raw-event updates, maintaining robust LED identity association and accurate pixel-level tracking under rapid motion. LED identities and positions establish reliable 2D-3D correspondences for real-time metric 6-DoF relative pose estimation. Extensive evaluations on a self-collected dataset demonstrate robustness under large motion flow and transient image-plane LED overlap. Furthermore, we develop a coordinated robotic platform comprising a quadrotor and a Mecanum-wheeled mobile robot, demonstrating the proposed framework's potential for closed-loop drone guidance through hovering and target-following experiments under time-varying HDR illumination, with onboard deployment on an NVIDIA Jetson Orin NX. The dataset and implementation will be released to facilitate further research.

</details>

#### 2026-11-04 - SpikePose: Lightweight Video Human Pose Estimation

**Authors:** Yunhao Huang, Kaushik Bhargav Sivangi, Tianyi Yu, Fani Deligianni
**Links:** [abs](https://arxiv.org/abs/2611.06594) - [pdf](https://arxiv.org/pdf/2611.06594)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpikePose: Lightweight Video Human Pose Estimation
- 作者：Yunhao Huang, Kaushik Bhargav Sivangi, Tianyi Yu, Fani Deligianni
- 出版日期：2026-11-04T14:48:33Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次级分类
- 链接：[摘要](https://arxiv.org/abs/2611.06594)｜[PDF](https://arxiv.org/pdf/2611.06594)

### 一句话总结
SpikePose 是一种轻量视频人体姿态估计器，用帧重置单步脉冲编码器提供逐帧空间证据，并用运动对齐热图记忆（MAM）处理时序信息，以在精度、运动质量与能耗之间取得平衡。

### 研究问题
摘要指出，高效视频人体姿态估计需要在定位精度、运动质量和能量开销之间平衡。论文关注的是：如何让脉冲神经网络（SNN）在非事件驱动的大规模视频任务上，缩小与经典人工神经网络（ANN）之间的差距，同时保持较低能耗。

### 核心思路/方法
- 编码器：采用帧重置（frame-reset）、单步（single-step）的脉冲编码器，为每一帧提供空间证据。
- 时序模块：提出运动对齐热图记忆（MAM），用于估计关节位移、对齐历史热图，并将其与当前预测自适应融合。
- 结构设计：将时序推理限制在脉冲骨干网络之外的紧凑轻量模块中，从而把时序建模与脉冲骨干解耦。

### 主要贡献
- 提出 SpikePose，将帧重置单步脉冲编码器与 MAM 结合，用于轻量视频人体姿态估计。
- 通过把时序推理放在脉冲骨干之外的轻量模块中，试图缩小 SNN 与经典 ANN 在非事件驱动大规模视频任务上的差距。
- 在 MPII 和固定的 NTU60 Cross-Subject 子集上评估空间精度、运动误差和估计算术能耗。
- 与使用 MAM 的同架构 ANN 相比，SpikePose 在 PCK_HB(0.5) 上仅下降 1.12 个点，同时估计算术能耗降低 91.4%。
- 在 SpikePose 内部加入 MAM 后，速度误差和加速度误差分别降低 28.13% 和 31.46%，定位略有提升，代价仅为 0.003M 参数和每帧 0.0023 解析 GFLOPs。
- 摘要称代码将在录用后发布于 GitHub。

### 局限性
- 摘要未提供足够信息说明方法在更广泛数据集、真实事件相机数据或部署硬件上的表现。
- 摘要未提供足够信息说明能耗为“估计算术能耗”之外的实际功耗测量结果。
- 摘要未提供足够信息说明与更多现有视频姿态估计方法的完整对比。
- 摘要未提供足够信息说明失败案例、遮挡或复杂运动场景下的表现。

### 阅读优先级
中。理由：论文聚焦轻量视频人体姿态估计与脉冲网络能效，给出了明确的能耗与精度权衡数据；但摘要篇幅有限，实验范围、实际部署效果和完整对比细节需阅读全文进一步确认。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：UniLoop: Unified Loop Closure Detection from Retrieval to Geometric Verification and Relative Pose Estimation
- 作者：Jingwen Yu, Pengyu Wang, Jin Wu, Weinan Chen, Ping Tan, Hong Zhang
- 出版日期：2026-11-04T11:41:55Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.06378) / [PDF](https://arxiv.org/pdf/2611.06378)

### 一句话总结
UniLoop 提出统一回环检测框架，复用预训练几何基础模型的分层表示，将全局检索、几何验证和相对位姿估计从多模型级联改为共享特征的单流程。

### 研究问题
传统回环检测通常串联独立模型：全局检索、几何验证、相对位姿估计分阶段进行，导致计算冗余且各阶段视觉表示彼此割裂。论文要解决的是：能否用一个统一框架，复用同一基础模型的表示，减少冗余主干计算，同时提升回环检测的鲁棒性和精度。

### 核心思路/方法
- 复用预训练几何基础模型的分层表示，贯穿检索、验证和位姿估计全流程。
- 共享图像编码器产生特征，用于形成紧凑的全局描述子。
- 同一组特征被送入跨视角解码器，用于成对验证。
- 原始几何预测提供相对相机约束，用于位姿图优化。
- 整体目标是替代“全局检索→几何验证→相对位姿估计”的模块化级联流水线。

### 主要贡献
- 提出 UniLoop 统一回环检测框架，将检索、验证和相对位姿估计纳入共享表示流程。
- 通过复用同一图像编码器和几何基础模型特征，减少模块化流水线中的冗余主干计算。
- 在地点识别、回环验证和相对位姿估计实验中，报告了回环闭合鲁棒性和精度的提升。
- 在 MSLS 上取得 96.6 Recall@10，在 Pitts30k 上取得 99.3 Recall@10，均为对比方法中最佳。
- 验证分支达到 95.63 AP 和 96.29 ROC-AUC，超过现有几何验证基线。

### 局限性
- 摘要未提供足够信息说明训练数据规模、模型参数量、推理时延和计算开销的具体数值。
- 摘要未提供足够信息说明跨数据集泛化能力、失败案例或消融实验细节。
- 摘要未提供足够信息说明与更多近期回环检测方法的完整对比范围。
- 摘要未提供足够信息说明对动态场景、剧烈光照变化或严重遮挡的鲁棒性。
- 摘要未提供足够信息说明相对位姿估计的定量指标和位姿图优化端到端效果。

### 阅读优先级
高。理由：论文直接针对回环检测中“多模型级联导致冗余计算和表示割裂”的核心痛点，提出统一框架，并在地点识别和几何验证上给出明确的最优指标；主题属于 3D Reconstruction & Multi-view Geometry 中的视觉定位与回环检测方向，方法和实验结论对相关流水线设计有较强参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Quo Vadis, Driving Scene Reconstruction? Occlusion-Aware Gaussian Densification
- 作者：Dung Do Tien, Kien Nguyen Do Trung, Kiet Dang Vu, Trung Thai Tran, Duc Dung Nguyen
- 出版日期：2026-11-04T10:17:04Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.06273 ；PDF https://arxiv.org/pdf/2611.06273

### 一句话总结
论文提出 OccSplat，一个前馈式驾驶场景重建框架，其核心是遮挡感知的高斯致密化：不再只对渲染图像做图像空间修复，而是为缺乏高斯支撑的被遮挡区域预测新的三维高斯原语，从而在三维表示中补全场景并提升新视角合成。

### 研究问题
现有的前馈式 3D Gaussian Splatting 方法虽然能高效地从环视图像重建驾驶场景，但它们依赖单次观测，导致新视角合成受限：输入中被遮挡的区域在新视角下可能可见，而对应的重建高斯欠约束、不完整。论文要解决的是这种三维场景几何缺失，而非仅仅修复渲染图像中的缺失像素。

### 核心思路/方法
OccSplat 是一个前馈框架，核心贡献为 Occlusion-Aware Gaussian Densification。方法包含两个关键环节：
1. **Gaussian Occlusion Mapping**：识别缺乏高斯支撑的被遮挡区域；
2. **Gaussian Occlusion Completion**：为这些区域生成新的高斯原语。

预测出的原语被整合进原始表示中，以改善新视角合成，同时保持前馈推理，无需逐场景优化。

### 主要贡献
- 提出 OccSplat 前馈框架，核心是遮挡感知的高斯致密化。
- 明确针对缺失的场景几何而非缺失像素，避免仅依赖图像空间修复。
- 通过 Gaussian Occlusion Mapping 定位缺乏高斯支撑的遮挡区域，并通过 Gaussian Occlusion Completion 生成新原语。
- 将新原语整合进原始三维表示，在保持前馈推理、无需逐场景优化的同时改善新视角合成。
- 在 nuScenes 基准上的实验表明，OccSplat 相比对比方法有所提升，且在遮挡区域增益尤其大，重建更准确、视觉更连贯。

### 局限性
摘要未提供足够信息。摘要未给出计算开销、推理速度、对极端遮挡或稀疏视角的鲁棒性、失败案例，以及各模块的消融细节等局限相关信息。

### 阅读优先级
**高**。理由：该论文直接针对前馈式 3D Gaussian Splatting 驾驶场景重建中的关键欠约束问题，提出明确的三维几何补全机制，且摘要报告在 nuScenes 遮挡区域有显著增益；主题与 3D 重建、神经场景表示和自动驾驶场景理解高度相关。但若读者只关注逐场景优化或非驾驶场景，相关性可降为中等。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：基于像素级可见光通信的投影空间三维位姿估计
- 作者：Michikuni Eguchi, Takefumi Hiraki
- 出版日期：2026-11-04T08:07:10Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.06121) / [PDF](https://arxiv.org/pdf/2611.06121)

### 一句话总结
论文将像素级可见光通信（PVLC）的平面位姿估计扩展为三维位姿估计，通过把设备上四个共面光电传感器接收到的二维像素位置与其已知三维布局构成 PnP 问题，实现无需外部传感基础设施的实时三维位姿估计。

### 研究问题
基于投影仪的增强现实需要投影仪与设备之间精确的位置对齐。PVLC 能够在不依赖外部传感基础设施的情况下，通过高速亮度调制将不可见空间码嵌入每个投影像素，从而完成对齐并保持图像质量。但 PVLC 传输的信息本质上是平面的，因此现有方法只能处理在平面上运动的设备，无法估计三维空间中设备（例如空中机器人）的三维位姿。论文要解决的问题是：如何将基于 PVLC 的位姿估计从平面扩展到三维空间。

### 核心思路/方法
论文将三维位姿估计建模为 Perspective-n-Point（PnP）问题：
- 图像点：设备上四个共面光电传感器通过 PVLC 接收到的二维像素位置；
- 物体点：这四个光电传感器已知的三维布局；
- 通过 PnP 求解设备的三维位姿。

论文还提到在卡尔曼滤波后进行位置估计，并报告了延迟与位置 RMSE 指标。

### 主要贡献
- 将 PVLC 位姿估计形式化为 PnP 问题，把原本平面的信息用于三维位姿求解。
- 实验报告显示，该系统以约 8 ms 的延迟估计三维位姿，卡尔曼滤波后的三维位置 RMSE 为 19.2 mm。
- 作者称这些结果确认了“首个与高质量投影图像内容协同、且无需外部传感基础设施的实时三维位姿估计”的实现。

### 局限性
摘要未提供足够信息说明以下方面：四个共面光电传感器的具体配置与尺寸、实验环境与设备类型、遮挡或光照变化等鲁棒性测试、与基线方法的对比、卡尔曼滤波的具体设计，以及“首个”这一表述的完整验证范围。摘要仅给出延迟和滤波后位置 RMSE，未提供姿态角误差、未滤波性能或更大工作空间下的表现。

### 阅读优先级
中。理由：该工作将 PVLC 与 PnP 结合以扩展到三维位姿估计，问题定义清晰，并给出了延迟与位置精度指标；但摘要未提供充分的实验细节、对比与鲁棒性分析，是否值得深入阅读取决于读者对投影式 AR、可见光通信或无需外部传感的位姿估计是否感兴趣。

</details>

<details>
<summary>Abstract</summary>

Projector-based augmented reality enables natural interaction between users and devices by overlaying digital information onto the physical world through projected imagery. A key technical requirement of such systems is accurate positional alignment between the projector and the devices. Pixel-level Visible Light Communication (PVLC) achieves this alignment without external sensing infrastructure by embedding invisible spatial codes into each projected pixel through high-speed brightness modulation that preserves image quality. However, the information that PVLC transmits is inherently planar. PVLC has therefore been limited to devices moving on a flat surface and cannot estimate the 3D pose of devices in three-dimensional space, such as aerial robots. To extend PVLC-based pose estimation to three dimensions, we formulate it as a Perspective-n-Point (PnP) problem. The 2D pixel positions that four coplanar photosensors on the device receive via PVLC serve as the image points, and their known 3D layout provides the object points. Experiments show that the proposed system estimates 3D pose with a latency of approximately 8~ms and a 3D position RMSE of 19.2~mm after Kalman filtering. These results confirm the first realization of real-time 3D pose estimation coordinated with high-quality projected image content without external sensing infrastructure.

</details>

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-09 - Plant Orbiter: 3D Plant Reconstruction and Generation with Video Diffusion Orbit Cameras and 3D Gaussian Splatting

**Authors:** Zane K. J. Hartley, Yong En Kok, Lewis A. G. Stuart, Andrew P. French, Michael P. Pound
**Links:** [abs](https://arxiv.org/abs/2611.12739) - [pdf](https://arxiv.org/pdf/2611.12739)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Modern digital phenotyping pipelines require the precise measurement of a range of 3D morphological plant traits. The accurate, high throughput acquisition of these traits helps breeders and researchers accelerate the development of new varieties, techniques and products. Recent advances in 3D technologies have enabled a rapid transition from 2D to 3D pipelines, but high throughput acquisition of digital 3D twins of plants remains a significant challenge due to complex morphology, thin structures and occlusions. In this paper we present Plant Orbiter, a new approach to generating 3D plants that leverages recent advances in video diffusion to produce high quality 3D Gaussian Splats of plants from a single image. We show that our method more accurately recreates plant morphology than other state-of-the-art methods, achieving the highest 3D F-score against all baselines, while being more practical for high throughput pipelines due to easier alignment and reduced cost of camera placement. Combined with a 2D diffusion model, we show that our method also achieves state-of-the-art results in the generation of 3D plant models from a text prompt.

</details>

#### 2026-11-09 - Spaghetti Splatting: Differentiating Curvilinear Dirac Masses via Convolution

**Authors:** George Shramko, Shrisudhan Govindarajan, Rudy Lam, Yizheng Xie, Daniel Rebain, David B. Lindell, Andrea Tagliasacchi
**Links:** [abs](https://arxiv.org/abs/2611.12716) - [pdf](https://arxiv.org/pdf/2611.12716)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, simulation

<details>
<summary>Abstract</summary>

In production systems, 3D geometry is represented by primitives such as points, lines, and triangles, as rendering hardware is optimized to generate images from them very efficiently. Learning such primitives from images by volume rendering is challenging, as they are Dirac masses defined at infinitesimal locations in space. EWA splatting, Poisson reconstruction, and 3D Gaussian Splatting overcome this by convolving Dirac masses with a low-frequency kernel, a recipe that generalizes along two axes: the kernel and the primitive. As points and triangles have already received significant attention, we investigate this recipe for curvilinear primitives, and introduce Spaghetti Splatting. We approximate curves by polylines whose convolution converges to that of the continuous curve, and volume render each segment so that connected segments composite without overcounting at their joints. For fast training and inference, we linearize the camera projection per segment, which also accommodates kernels beyond Gaussians, such as Beta kernels. As a point is a curve of zero length, our representation is a strict superset of 3D Gaussian Splatting. It remains competitive with the state-of-the-art on general scenes, outperforms methods specialized to line-like geometry, natively supports anti-aliasing, and produces long connected strands that are directly amenable to physics simulation.

</details>

#### 2026-11-09 - Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs

**Authors:** Junha Ryu, Hoi-Jun Yoo
**Links:** [abs](https://arxiv.org/abs/2611.12319) - [pdf](https://arxiv.org/pdf/2611.12319)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic, real-time rendering on commodity GPUs and is increasingly adopted in generative world models and autonomous driving simulators. However, existing optimizations rely on algorithmic changes that often require retraining, or on specialized accelerators that lack flexibility across evolving 3DGS variants. In this paper, we identify a fundamental inefficiency in GPU-based 3DGS rendering: severe SM-level load imbalance caused by uneven workloads across screen tiles. This imbalance creates a long execution tail, leaving most SMs idle while a few process computationally intensive tiles, particularly in large-scale urban scenes. To address this, we present a software-defined GPU scheduling approach that mitigates the execution tail. Our approach uses a persistent kernel to schedule heavy tiles first and selectively chunks outlier tiles across multiple CTAs. A lightweight per-frame policy determines when and how much to chunk using tile statistics already available in the rendering pipeline. Our approach requires neither retraining nor specialized hardware and can be applied orthogonally to existing optimizations across diverse 3DGS variants. Averaged per scene, it accelerates alpha blending by up to 2.93x on a large-scale urban scene, and by up to 5.6x on its most imbalanced frames, while retaining the original alpha blending formulation.

</details>

#### 2026-11-09 - UltraVoxelGS: Voxel-First Feed-Forward Gaussian Splatting for 3D Ultrasound Reconstruction

**Authors:** Yue Wang, Haoxin Chen, Xiaoqing Guo
**Links:** [abs](https://arxiv.org/abs/2611.11951) - [pdf](https://arxiv.org/pdf/2611.11951)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, scene representation, rendering, splatting

<details>
<summary>Abstract</summary>

We present UltraVoxelGS, a 3D ultrasound reconstruction method that achieves both fast reconstruction and physically faithful rendering for the first time, bringing live spatial feedback during 2D ultrasound scanning within reach. This is made possible by a feed-forward design that predicts a complete Gaussian scene representation from posed ultrasound images directly, entirely bypassing the per-scene optimization bottleneck that has confined prior methods to offline use. Realising such feed-forward prediction in this setting is non-trivial: unlike natural images, ultrasound slices share at most one-dimensional intersections and exhibit view-dependent appearance due to acoustic propagation and attenuation, violating the dense overlap and photometric consistency assumed by existing feed-forward Gaussian methods. Hence, to achieve fast reconstruction, we introduce a feed-forward voxel-to-Gaussian pass that decouples representation size from input count by lifting all posed slices into a fixed-size voxel support and predicting Gaussian parameters directly. For faithful rendering, we propose ultrasound-aware appearance rendering strategy factorize reflection from cumulative attenuation during training and exploit appearance continuity among spatially adjacent slices for efficient Render-time Appearance Adaptation. On both real-world and simulated datasets, UltraVoxelGS achieves best PSNR/SSIM compared with per-scene optimization baselines while reducing inference from 10-20 minutes to approximately 10 seconds (over 35 times faster) and scales to sequences exceeding 1,000 frames. Code is available at https://github.com/YuebyYue/UltraVoxelGS-camera-ready.

</details>

#### 2026-11-08 - FastGRT: Accelerating Training of 3D Gaussian Ray Tracing

**Authors:** Meet Banthia, Xiaoteng Liu, Hexu Zhao, Aurojit Panda, Jinyang Li
**Links:** [abs](https://arxiv.org/abs/2611.11586) - [pdf](https://arxiv.org/pdf/2611.11586)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Ray Tracing enables rendering capabilities that are difficult to achieve with rasterization-based approaches such as 3D Gaussian Splatting (3DGS). However, the training cost of Gaussian-based ray tracing (GRT) is much higher than that of 3DGS. In this paper, we study how ray tracing using Gaussians executes on GPUs and show that a considerable fraction of the training cost arises from how the computation is organized. We develop FastGRT, which decouples ray traversal from blending and reuses work done in the forward pass for the backward pass. FastGRT further incorporates optimizations such as fast gradient accumulation and a hybrid BVH update strategy to tackle other major bottlenecks in the training pipeline. We implement FastGRT in Vulkan. To the best of our knowledge, it is the first Vulkan-based GRT implementation that supports both training and rendering. Compared to 3DGRT, FastGRT improves training time by 1.9$\times$ to 4.97$\times$, while preserving the original rendering formulation. Our code is open source.

</details>

#### 2026-11-05 - MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation

**Authors:** Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri, Georgios Pavlakos, Roberto Martín-Martín
**Links:** [abs](https://arxiv.org/abs/2611.08372) - [pdf](https://arxiv.org/pdf/2611.08372)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting, manipulation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation
- 作者：Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri, Georgios Pavlakos, Roberto Martín-Martín
- 出版日期：2026-11-05T17:50:35Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.08372) | [PDF](https://arxiv.org/pdf/2611.08372)

### 一句话总结
MOMASPLAT 提出一种面向移动操作（MoMa）的动态新视角示范增强框架，通过分别重建静态场景与被操作物体，并从未见过的机器人基座位姿合成包含动态交互的完整操作轨迹示范。

### 研究问题
摘要指出，通过模仿学习训练的视觉运动策略对相机视角变化高度敏感。在移动操作中，由于导航不确定性、定位漂移和环境约束，机器人很少能在与示范采集时完全相同的基座位姿下执行操作。已有的新视角合成增强方法假设场景是静态的，因此无法在接触后交互阶段重新渲染被操作物体，导致示范中最关键的部分未被增强。论文要解决的核心问题是：如何为移动操作生成包含动态物体交互的新视角示范，从而提升策略对未见基座位姿的鲁棒性。

### 核心思路/方法
摘要给出的关键洞察是：标准 MoMa 数据采集过程天然提供了重建静态场景与被操作物体所需的多视角观测。MOMASPLAT 将 3D Gaussian Splatting、前馈 3D 基础模型与基于运动学的动作重定向相结合，分别重建场景和被操作物体，从新视角渲染二者，并生成几何一致的合成示范及相应的变换后动作。该方法强调合成的是完整操作轨迹，包括动态物体交互阶段。

### 主要贡献
- 提出 MOMASPLAT，一个面向移动操作的新视角示范增强框架，能够从未见过的机器人基座位姿合成完整操作轨迹，并覆盖动态物体交互。
- 利用标准 MoMa 数据采集天然提供的多视角观测，分别重建静态场景与被操作物体。
- 结合 3D Gaussian Splatting、前馈 3D 基础模型和基于运动学的动作重定向，生成几何一致的合成示范与变换后的动作。
- 在五个真实世界移动操作任务（涉及刚性与铰接物体、跨三个场景）上评估，并在仿真中对照真值验证合成示范的保真度。
- 摘要报告：显著提升对未见基座位姿的鲁棒性，平均成功率超过最强基线两倍以上，并在所有基线均失败的大基座位移情况下仍保持非平凡成功率，同时减少对大规模真实世界数据采集的需求。

### 局限性
- 摘要未提供足够信息说明方法在非刚性物体、透明/反光物体或严重遮挡条件下的表现。
- 摘要未提供足够信息说明多视角重建对采集数据覆盖度、标定精度或计算开销的具体要求与限制。
- 摘要未提供足够信息说明真实世界评估的样本规模、统计显著性或失败模式分析。
- 摘要未提供足够信息说明动作重定向在接触丰富或高精度操作任务中的误差边界。

### 阅读优先级
中。理由：该工作针对移动操作中视角鲁棒性与动态新视角示范增强这一明确问题，方法组合（3D Gaussian Splatting、3D 基础模型、动作重定向）与真实世界任务评估在摘要中已有清晰概述，对具身智能与机器人视觉运动策略方向具有相关性；但摘要未提供实验细节、定量表格与局限性讨论，是否值得深入阅读需结合全文的实验严谨性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Visuomotor policies trained through imitation learning are highly sensitive to changes in camera viewpoint. This is particularly problematic for mobile manipulation (MoMa), where robots rarely execute manipulation from the exact same base pose used during demonstration collection due to navigation uncertainty, localization drift, and environmental constraints. Recent approaches use novel-view synthesis (NVS) to augment demonstrations with unseen viewpoints, but they assume static scenes and therefore fail to re-render the manipulated object during the post-contact interaction phase, leaving the most critical parts of the demonstration unaugmented. We present MOMASPLAT, a novel-view demonstration augmentation framework for mobile manipulation that synthesizes full manipulation trajectories from unseen robot base poses, including dynamic object interactions. Our key insight is that standard MoMa data collection naturally provides the multiview observations needed to reconstruct both the static scene and the manipulated object in 3D. MOMASPLAT combines 3D Gaussian Splatting, feed-forward 3D foundation models, and kinematics-based action retargeting to separately reconstruct the scene and manipulated object, render them from novel viewpoints, and generate geometrically consistent synthetic demonstrations paired with transformed actions. We evaluate MOMASPLAT on five real-world mobile manipulation tasks involving both rigid and articulated objects across three scenes, and validate the fidelity of its synthesized demonstrations against ground truth in simulation. MOMASPLAT substantially improves robustness to unseen base poses, more than doubling the average success rate of the strongest baseline and maintaining non-trivial success at large base displacements where all baselines fail, while reducing the need for largescale real-world data collection.

</details>

#### 2026-11-05 - 4D Point Splatting for mmWave Radar Micro-Doppler Differentiable Rendering

**Authors:** Adnan Armouti, Guanyue Qian, Rajalakshmi Nandakumar
**Links:** [abs](https://arxiv.org/abs/2611.08342) - [pdf](https://arxiv.org/pdf/2611.08342)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4D Point Splatting for mmWave Radar Micro-Doppler Differentiable Rendering
- 作者：Adnan Armouti, Guanyue Qian, Rajalakshmi Nandakumar
- 出版日期：2026-11-05T17:27:29Z
- 分类：Neural Scene Representations & Rendering（主分类）；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.08342 ；PDF https://arxiv.org/pdf/2611.08342

### 一句话总结
提出 4DPS——一种基于物理的可微渲染器，将显式运动场景拟合到真实毫米波雷达采集，渲染原始复数回波，以缩小雷达人体感知数据的 sim2real 差距。

### 研究问题
毫米波雷达可借微多普勒感知步态、手势、活动、姿态与生命体征，但雷达数据集规模远落后于视觉与语言数据；暴力采集无法弥合差距，而现有合成方法（仅前向模拟器、学习式生成器、静态场景逆渲染器）无法拟合真实运动人体采集，存在 sim2real 差距。

### 核心思路/方法
- 用同步相机初始化房间与人体，将场景表示为带朝向的点，每点携带材质、法线与速度。
- 将每个点 splat 到距离（range）与多普勒（Doppler）bin 中，输出真实雷达记录的原始复数回波。
- 对渲染数据施加与真实数据相同的信号处理，从而获得任意表示，用于训练任意 SOTA 下游模型。
- 使用自定义 CUDA 核实现序列级拟合。

### 主要贡献
- 提出 4DPS，一种拟合真实运动场景采集的物理可微毫米波雷达渲染器。
- 在 HuPR 的 235 条序列与 RT-Pose 的 100 条序列上完成拟合，重建达到 SOTA：距离-方位中位相关 0.940 / 0.830，距离-多普勒 0.829 / 0.695，微多普勒 0.988 / 0.966。
- 渲染数据在下游 sim2real 差距上达到 SOTA：RT-Pose 上用渲染数据训练的姿态模型在真实数据上达 21.9 cm MPJPE（真实训练 16.7 cm，RF-Genesis 基线 127.6 cm），且渲染训练与真实训练模型学到近乎相同的特征。
- 单张 H100 上拟合一条序列耗时 5.7 分钟（HuPR）/ 12.9 分钟（RT-Pose），首次使毫米波雷达的数据集级逆渲染成为可能。
- 摘要称可支持任意以人为中心的下游任务的合成数据生成，以及用于数据增强的场景编辑。

### 局限性
- 摘要未提供足够信息说明方法在无同步相机的纯雷达场景、不同雷达硬件泛化或极端遮挡/多人场景下的表现。
- 摘要未提供足够信息说明渲染与真实训练之间 21.9 cm 与 16.7 cm 差距的具体来源与改进空间。
- 摘要未提供足够信息说明 5.7/12.9 分钟拟合耗时的可扩展性边界（如更大数据集或更多序列并行时的开销）。
- 摘要未提供足够信息给出定量实验之外的失败案例或误差分析。

### 阅读优先级
高。理由：该工作针对雷达人体感知数据稀缺与 sim2real 差距这一关键瓶颈，给出可微逆渲染方案，并在两个不同雷达数据集上报告重建与下游姿态估计的 SOTA 定量结果，且具备数据集级可行性；对神经场景表示、雷达感知与合成数据生成方向均有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Millimeter-wave radar resolves the micrometer displacements of a moving body as micro-Doppler, enabling gait, gesture, activity, pose and vital-sign sensing. Each task relies on a downstream model trained on real data, yet radar datasets lag orders of magnitude behind vision and language. Brute-force collection will not close that gap, and existing synthesis methods (forward-only simulators, learned generators and static-scene inverse renderers) cannot fit a real capture of a moving body, leaving a sim2real gap. We present 4D Point Splatting (4DPS), a physics-based differentiable renderer that fits an explicit moving scene to a real capture. Using the synchronized camera to initialize the room and body, we represent the scene as oriented points carrying material, normal and velocity, and splat each point into range and Doppler bins. Our output is the raw complex return a real radar records, so we apply the same signal processing on the rendered data to obtain any representation for training any SOTA downstream model. We fit 235 sequences on HuPR and 100 on RT-Pose, two datasets with different radars. Our reconstructions set the state of the art, with median correlations of 0.940 and 0.830 on range-azimuth, 0.829 and 0.695 on range-Doppler, and 0.988 and 0.966 on micro-Doppler. Our renders also set the state of the art in downstream sim2real gap. On RT-Pose, a pose model trained on them reaches 21.9 cm MPJPE on real data, against 16.7 cm for real training and 127.6 cm for the RF-Genesis baseline, where both the rendered- and real-trained models learn nearly the same features. Our custom CUDA kernels fit a sequence in 5.7 minutes on HuPR and 12.9 on RT-Pose on one H100, making dataset-scale inverse rendering of mmWave radar possible for the first time. This work can enable synthetic data generation for any human-centered downstream task and model, and scene editing for data augmentation.

</details>

#### 2026-11-05 - Hierarchical Incremental Beta Splatting for Online Reconstruction

**Authors:** Linus Franke
**Links:** [abs](https://arxiv.org/abs/2611.08288) - [pdf](https://arxiv.org/pdf/2611.08288)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hierarchical Incremental Beta Splatting for Online Reconstruction
- 作者：Linus Franke
- 出版日期：2026-11-05T16:52:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2611.08288

### 一句话总结
该论文提出 HIBS（分层增量 Beta Splatting），将 beta 核引入在线 3D 重建，通过可调形状参数与置信度感知初始化、误差驱动重定位及 LOD 合并，在 Mip-NeRF 360 的 on-the-fly 协议下提升 PSNR 并缩短优化时间。

### 研究问题
在线 3D Gaussian Splatting 在采集过程中重建场景：每个关键帧只生成一次基元，并且仅对其进行数十次迭代优化，因此难以修正较差的初始化或补足缺失细节；同时高斯本身偏“软”，需要大量重叠才能表现实心表面。

### 核心思路/方法
- 将 beta 核引入增量重建，其形状参数可在“软的高斯状剖面”和“平顶、接近不透明的 surfel”之间插值，作为几何置信度的调节手段。
- 置信度感知生成：利用几何可观测性和多视图深度一致性来初始化不透明度与形状；几何可验证处生成实心基元，不可验证处生成软且可修正的基元。
- 在线致密化中的误差驱动重定位：将陈旧基元回收至光度误差热点。
- 有界 beta 核支撑带来精确 tile 剔除和更快光栅化；闭式、保形合并公式提供 LOD 层次，用于快速优化与实时渲染。

### 主要贡献
- 提出 HIBS，将 beta 核用于增量式在线重建，并以形状参数表达几何置信度。
- 提出置信度感知的基元生成策略，结合几何可观测性与多视图深度一致性初始化不透明度和形状。
- 引入误差驱动重定位进行在线致密化，回收陈旧基元。
- 利用有界支撑实现精确 tile 剔除与更快光栅化，并给出保形合并的 LOD 层次。
- 在 Mip-NeRF 360 的 on-the-fly 协议下，PSNR 最高提升 0.8 dB，优化时间最多减少 40%。

### 局限性
摘要未提供足够信息（未说明失败场景、适用范围限制、对特定数据集的依赖或计算/内存开销等）。

### 阅读优先级
中。理由：该工作聚焦在线增量重建中初始化与细节修正的关键痛点，方法组合（beta 核、置信度感知生成、重定位、LOD）较完整，并给出定量提升；但摘要仅报告单一数据集协议下的结果，且作者与实验规模信息有限，是否具有广泛适用性需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Online 3D Gaussian Splatting reconstructs a scene during capture: each keyframe spawns primitives once and refines them for only a few dozen iterations, leaving little chance to fix poor initialization or missing detail. Gaussians are also inherently soft, needing many overlaps for solid surfaces. We present Hierarchical Incremental Beta Splatting (HIBS), which brings beta kernels to incremental reconstruction. Their shape parameter interpolates between a soft, Gaussian-like profile and a flat-topped, near-opaque surfel, acting as a confidence dial for geometry. Our confidence-aware spawning uses geometric observability and multi-view depth agreement to initialize both opacity and shape, producing solid primitives where geometry is verifiable and soft, correctable primitives where it is not. As online densification, error-driven relocation recycles stale primitives into photometric-error hotspots. Bounded beta kernel support enables exact tile culling and faster rasterization, and a closed-form, shape-preserving merging formulation provides a level-of-detail (LOD) hierarchy for fast optimization and real-time rendering. On Mip-NeRF 360 in the on-the-fly protocol, HIBS improves PSNR by up to 0.8 dB while reducing optimization time by up to 40%. Project page: https://linus-franke.com/hibs/

</details>

#### 2026-11-05 - Perception Over Geometry: Rethinking Gaussian Allocation in Mesh-based Splatting

**Authors:** Yuting Wang, Yang Zhao, Shanding Diao, Penglin Wang, Yuan Chen, Wei Jia, Ronggang Wang
**Links:** [abs](https://arxiv.org/abs/2611.07979) - [pdf](https://arxiv.org/pdf/2611.07979)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Perception Over Geometry: Rethinking Gaussian Allocation in Mesh-based Splatting
- 作者：Yuting Wang, Yang Zhao, Shanding Diao, Penglin Wang, Yuan Chen, Wei Jia, Ronggang Wang
- 出版日期：2026-11-05T13:09:42Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.07979 ；PDF https://arxiv.org/pdf/2611.07979

### 一句话总结
论文提出 P-MGS，将外观建模与几何控制分离，按感知复杂度而非网格面密度分配高斯，以较少高斯实现较优新视角合成并支持连贯的网格编辑。

### 研究问题
现有基于网格的 3D Gaussian Splatting 方法通常为每个三角面分配固定数量的高斯，但外观重建所需的表示能力取决于局部外观复杂度，而非仅由网格细分密度决定。摘要指出这一做法存在表示分配与外观需求不匹配的问题。

### 核心思路/方法
P-MGS 的核心是分离外观建模与几何控制。具体包括：引入感知复杂度引导的分配策略，根据多视角观测估计的表面外观需求来分配高斯；高斯在优化时不受网格约束，之后通过事后绑定与原始网格关联，从而在保留网格拓扑的同时维持自适应细化能力；在网格编辑时，采用局部仿射变形传递，在网格变形下更新高斯中心与协方差，减少错位与漂浮伪影。

### 主要贡献
摘要声称的贡献包括：提出按感知复杂度分配高斯的策略；通过无网格约束优化加事后绑定，兼顾重建灵活性与网格拓扑保留；设计面向网格编辑的局部仿射变形传递以更新高斯参数；实验层面摘要称在新视角合成平均质量上更优、使用更少高斯，并获得连贯的网格编辑效果。具体实验设置、数据集与定量指标摘要未提供足够信息。

### 局限性
摘要未提供足够信息。可确认的边界是：摘要未给出失败案例、计算开销、绑定误差或编辑类型覆盖范围的细节；亦未说明感知复杂度估计的具体实现与消融结果。

### 阅读优先级
中。理由：该论文针对基于网格的 3DGS 中“固定每面高斯分配”这一明确问题，提出分配策略与编辑传递方法，主题与神经场景表示及渲染直接相关；但摘要未提供定量实验细节与实现信息，是否值得优先精读取决于读者对网格编辑与高斯分配策略的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic novel-view synthesis but lacks explicit topology for geometric editing. Existing mesh-based methods enable geometric manipulation by associating Gaussians with triangular mesh faces, typically assigning a fixed number of Gaussians to each face. However, the representation capacity required for appearance reconstruction depends on local appearance complexity rather than merely on mesh tessellation density. To address these limitations, we propose P-MGS, a framework that separates appearance modeling from geometric control to achieve high quality rendering, compact representation, and flexible mesh editing. P-MGS introduces a perceptual complexity guided allocation strategy that distributes Gaussians according to surface appearance demand estimated from multiview observations. To preserve reconstruction flexibility, Gaussians are optimized without mesh constraints and subsequently associated with the original mesh through post hoc binding, retaining adaptive refinement while preserving mesh topology. During mesh editing, local affine deformation transfer updates Gaussian centers and covariances under mesh deformation, reducing misalignment and floating artifacts. Experiments demonstrate superior average novel view synthesis quality with fewer Gaussians and coherent mesh editing.

</details>

#### 2026-11-05 - AffineGS: Unlocking Accurate Geometry in 3DGS via Spatially Varying Affine Rectification

**Authors:** Tze Ho Elden Tse, Jizong Peng, Richard Chen, Angela Yao
**Links:** [abs](https://arxiv.org/abs/2611.07709) - [pdf](https://arxiv.org/pdf/2611.07709)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** metric depth, monocular depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AffineGS: Unlocking Accurate Geometry in 3DGS via Spatially Varying Affine Rectification
- 作者：Tze Ho Elden Tse, Jizong Peng, Richard Chen, Angela Yao
- 出版日期：2026-11-05T09:27:56Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.07709 ；PDF https://arxiv.org/pdf/2611.07709

### 一句话总结
论文指出单目深度网络存在随区域变化的“分段线性”失真，使 3DGS 中常用的全局尺度—平移对齐失效，因此提出空间变化的仿射校正与法向感知正则，以在保持高斯泼溅照片级质量的同时提升几何精度。

### 研究问题
3D Gaussian Splatting（3DGS）在新视角合成上视觉质量突出，但几何精度落后于其视觉质量。现有深度引导方法通常用单目深度先验正则化优化，并采用一个全局的 scale-and-shift 对齐；作者认为这一假设存在根本缺陷：现代单目深度网络系统性地表现出区域相关、分段线性的失真，而全局对齐会因强制单一变换而扭曲场景几何。

### 核心思路/方法
针对上述问题，论文提出：
1. **空间变化的仿射校正模型**：将单目视差校正为一致的度量深度，使用区域平滑、边缘感知的场来建模空间变化的仿射关系，而不是全局统一变换。
2. **法向感知正则器**：利用空间梯度，将校正后的视差与 3DGS 的深度和法向耦合起来。
3. 方法定位为**无需传感器（sensor-free）**，在多种实验设置下同时追求高斯泼溅的强光度质量与更高的几何精度。

### 主要贡献
- 发现并指出单目深度网络存在区域相关、分段线性失真的现象，说明标准全局对齐策略会扭曲场景几何。
- 提出空间变化的仿射校正模型，用区域平滑且边缘感知的场将单目视差校正为一致的度量深度。
- 推导法向感知正则器，以空间梯度耦合校正视差与 3DGS 的深度、法向。
- 摘要声称：在多种实验设置下，该无传感器方法在保持高斯泼溅强光度质量的同时显著提升几何精度，并优于当前聚焦几何的最先进方法。

### 局限性
- 摘要未提供足够信息说明方法对哪些场景类型、数据集规模或退化条件不适用。
- 摘要未提供足够信息说明空间变化仿射场的具体参数化、优化开销或实时性影响。
- 摘要未提供足够信息给出定量指标、对比基线细节与消融实验规模。
- 摘要未提供足够信息说明“区域平滑、边缘感知”假设在强非仿射失真或深度先验严重错误时的失效边界。

### 阅读优先级
**高**。理由：该工作直接挑战 3DGS 深度引导中广泛使用的全局对齐假设，问题定位清晰；若摘要所述“区域相关分段线性失真”成立，则对基于单目深度先验的 3DGS 几何优化具有方法层面的普遍意义，且摘要声称在几何精度上优于聚焦几何的最先进方法，值得优先阅读以核验其假设、正则设计与实验证据。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become the leading approach for photorealistic novel view synthesis, yet its geometric accuracy lags behind its visual quality. Existing depth-guided methods attempt to resolve this by regularizing the optimization with monocular depth priors, typically using a single global scale-and-shift alignment. Crucially, we discover a fundamental flaw in this assumption: modern monocular depth networks systematically exhibit region-dependent, piecewise-linear distortions. This discovery invalidates standard global alignment strategies, which warp scene geometry by enforcing a single transform. To address this, we introduce a spatially varying affine rectification model that corrects monocular disparity into consistent metric depth using regionally smooth, edge-aware fields. We further derive a normal-aware regularizer that uses spatial gradients to couple the rectified disparity with 3DGS depth and normals. Across diverse experimental settings, our sensor-free method shows strong photometric quality of Gaussian Splatting while substantially improving geometric accuracy and outperforming state-of-the art geometry-focused methods.

</details>

#### 2026-11-05 - Integrating Learned Priors through Prior-Space Reparameterization for Physically Based Inverse Rendering

**Authors:** Hun Hwangbo, Minjun Park, Yongsung Kim, Wooseok Song, Jungmin Ko, Junghyun Hwang, Sungroh Yoon
**Links:** [abs](https://arxiv.org/abs/2611.07573) - [pdf](https://arxiv.org/pdf/2611.07573)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Integrating Learned Priors through Prior-Space Reparameterization for Physically Based Inverse Rendering
- 作者：Hun Hwangbo, Minjun Park, Yongsung Kim, Wooseok Song, Jungmin Ko, Junghyun Hwang, Sungroh Yoon
- 出版日期：2026-11-05T07:20:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.07573) / [PDF](https://arxiv.org/pdf/2611.07573)

### 一句话总结
论文提出一种基于先验空间的材质重参数化方法，将学习到的材质预测作为先验来约束优化空间，同时保持纯光度目标不变，从而改善物理逆渲染中的材质分解与重光照效果。

### 研究问题
物理逆渲染需要从外观中分解材质与光照，但该问题本身具有歧义性。现有方法多通过辅助正则损失引入学习到的材质先验，这会改变优化目标，并需要平衡先验影响与光度拟合。论文关注的是：如何在不改变目标函数的情况下，有效利用学习到的材质先验来约束逆渲染优化。

### 核心思路/方法
论文提出一种先验引导的材质重参数化方法，利用预测特征之间的关系限制优化空间，而不改变优化目标。具体做法包括：将多视角材质预测融合到网格上，并在得到的先验特征空间中构造 permutohedral lattice；使具有相似预测的表面点共享材质变量，并将这些变量与几何、光照一起在纯光度目标下联合优化。摘要还提到，该重参数化会汇聚带噪声的光度梯度，使采样视角间的更新更一致，从而支持缩短联合优化时间。

### 主要贡献
- 提出一种先验引导的材质重参数化方法，通过限制优化空间引入学习先验，同时保持目标函数不变。
- 使用多视角材质预测融合、先验特征空间中的 permutohedral lattice 以及相似预测表面点共享材质变量的机制。
- 在两个学习预测器、三个合成基准和 Stanford-ORB 上进行实验，报告改善材质分解与重光照。
- 在 Synthetic4Relight 和 TensoIR-Synthetic 上，相比评估中最强的基于网格的基线，重光照 PSNR 提升 1.5-2.5 dB。
- 在受控比较中，优于使用相同先验的正则损失方法。
- 展示了该重参数化可汇聚噪声光度梯度，使采样视角间更新更一致，并支持不足一分钟的缩短联合优化计划，同时在 TensoIR-Synthetic 上保持高于所有评估基线的重光照质量。

### 局限性
摘要未提供足够信息说明方法在非合成数据上的泛化能力、对材质预测器质量的敏感性、计算开销的完整分析，以及失败案例或局限条件。摘要未提供足够信息说明更多实验细节与消融范围。

### 阅读优先级
高。理由：论文直接针对物理逆渲染中“如何引入学习先验而不改变优化目标”的关键问题，提出明确的重参数化机制，并在摘要中报告了重光照 PSNR 提升、优于同先验正则损失以及缩短优化时间的结果；对神经场景表示与渲染、逆渲染和材质分解方向具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Physically based inverse rendering decomposes appearance into materials and illumination, an ambiguous problem for which learned material predictions provide useful prior information. Most existing methods incorporate these cues through auxiliary regularization losses, which alter the optimization objective and require balancing their influence against photometric fitting. We propose a prior-guided material reparameterization that uses the predicted feature relationships to restrict the optimization space while leaving the objective unchanged. We fuse multi-view material predictions onto a mesh and construct a permutohedral lattice in the resulting prior feature space. Surface points with similar predictions share material variables, which are optimized jointly with geometry and illumination using a purely photometric objective. Experiments with two learned predictors on three synthetic benchmarks and Stanford-ORB demonstrate improved material decomposition and relighting. Our method improves relighting PSNR by 1.5-2.5 dB over the strongest evaluated mesh-based baseline on Synthetic4Relight and TensoIR-Synthetic, and outperforms a regularization loss using the same prior in controlled comparisons. We further show that our reparameterization pools noisy photometric gradients, producing updates that are more consistent across sampled views. This consistency enables a shortened joint optimization schedule that takes less than a minute while retaining relighting quality above all evaluated baselines on TensoIR-Synthetic.

</details>

#### 2026-11-04 - Wide View Synthesis from Overlapping Perspective Cameras in Autonomous Driving

**Authors:** Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Xiatian Zhu
**Links:** [abs](https://arxiv.org/abs/2611.07081) - [pdf](https://arxiv.org/pdf/2611.07081)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, view synthesis, rendering, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wide View Synthesis from Overlapping Perspective Cameras in Autonomous Driving
- 作者：Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Xiatian Zhu
- 出版日期：2026-11-04T19:36:54Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.07081) / [PDF](https://arxiv.org/pdf/2611.07081)

### 一句话总结
本文提出宽视角合成任务 WVS，并给出免逐场景优化的前馈高斯泼溅框架 WV-GS，用于从自动驾驶中空间分离的多透视相机观测合成指定虚拟视点的几何一致宽视角图像。

### 研究问题
论文关注自动驾驶中多透视相机系统产生的空间分离观测。作者将宽视角合成（WVS）定义为：在指定虚拟视点，从多个透视相机合成几何一致的宽视角图像。摘要将其与传统图像拼接区分开：WVS 需要推理 3D 几何与可见性，以处理由相机中心空间分离导致的深度相关视差和遮挡。摘要还指出，原始 3D Gaussian Splatting（3DGS）依赖逐场景优化，限制其在驾驶场景中的适用性；WVS 还面临透视投影下的边缘拉伸和跨相机光度不一致等挑战。

### 核心思路/方法
作者提出 Wide-View Gaussian Splatting（WV-GS），一个无需逐场景优化的前馈高斯泼溅框架，用于合成宽视角。方法包含两个明确组件：
- Piecewise Perspective Rendering（PPR）：通过共享同一相机中心的局部透视投影，缓解边缘拉伸问题；
- Spatial Affine Photometric Modeling（SAPM）：在训练中建模相机相关的光度变化。

此外，作者引入 WideDrive 合成基准，提供稠密真值宽视角，并在真实世界数据集上适配 LiDAR 投影的稀疏参考协议。

### 主要贡献
- 形式化定义宽视角合成（WVS）任务，强调其与图像拼接在 3D 几何、可见性、视差与遮挡处理上的差异。
- 提出 WV-GS 前馈高斯泼溅框架，避免逐场景优化，并设计 PPR 与 SAPM 应对边缘拉伸和跨相机光度不一致。
- 引入 WideDrive 合成基准（提供稠密真值宽视角），并为真实世界数据集适配 LiDAR 投影稀疏参考协议。
- 摘要称在多个数据集上的广泛实验证明 WV-GS 对 WVS 的有效性；数据集与代码将公开。

### 局限性
摘要未提供足够信息说明具体实验设置、对比方法、定量结果、失败案例或方法适用范围。摘要未提供足够信息说明 WV-GS 在真实世界数据上的具体性能上限与计算开销。摘要未提供足够信息说明 WideDrive 的规模、场景多样性及 LiDAR 投影稀疏参考协议的具体细节。

### 阅读优先级
高。理由：该论文明确面向自动驾驶多相机宽视角合成，提出新任务定义、前馈 3DGS 框架与新基准，且摘要给出清晰的方法动机与组件；若关注神经渲染、自动驾驶多相机感知与宽视角合成，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Multi-perspective-camera systems are widely adopted since they provide broad visual coverage for autonomous driving, motivating the synthesis of a unified wide view from spatially separated observations. In this work, we formulate wide view synthesis (WVS), which aims to synthesize a geometrically consistent wide view at a specified virtual viewpoint from multiple perspective cameras. Unlike conventional image stitching, WVS requires reasoning about 3D geometry and visibility to handle depth-dependent parallax and occlusions arising from spatially separated camera centers. While vanilla 3D Gaussian Splatting (3DGS) enables high-fidelity view synthesis, its reliance on per-scene optimization limits its applicability to driving scenes. Furthermore, WVS introduces additional challenges, *e.g.*, peripheral stretching under perspective projection and photometric inconsistencies across cameras. To address these challenges, we propose **Wide-View Gaussian Splatting (WV-GS)**, a feed-forward Gaussian-splatting framework that synthesizes wide views without per-scene optimization. Specifically, we introduce Piecewise Perspective Rendering (PPR) to mitigate peripheral stretching through local perspective projections sharing a common camera center, and Spatial Affine Photometric Modeling (SAPM) to account for camera-dependent photometric variations during training. We further introduce **WideDrive**, a synthetic benchmark providing dense ground-truth wide views and adapt a LiDAR-projected sparse-reference protocol to real-world datasets. Extensive experiments on multiple datasets demonstrate the effectiveness of WV-GS for WVS. Dataset and code will be publicly released.

</details>

#### 2026-11-04 - BudgetSplat: Budget-Controllable Generalizable Gaussian Splatting

**Authors:** Yuxi Hu, Jun Zhang, Wei Mao, Yuchen Rao, Friedrich Fraundorfer
**Links:** [abs](https://arxiv.org/abs/2611.06593) - [pdf](https://arxiv.org/pdf/2611.06593)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BudgetSplat: Budget-Controllable Generalizable Gaussian Splatting
- 作者：Yuxi Hu, Jun Zhang, Wei Mao, Yuchen Rao, Friedrich Fraundorfer
- 出版日期：2026-11-04T14:46:59Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.06593) / [PDF](https://arxiv.org/pdf/2611.06593)

### 一句话总结
BudgetSplat 提出一种前馈式、可由用户指定保留比例来控制最终高斯表示规模的可泛化 3D Gaussian Splatting 框架，在保持渲染质量的同时降低表示存储与渲染开销。

### 研究问题
现有前馈、像素对齐的 3D Gaussian Splatting 方法常生成高度冗余的高斯基元，导致最终表示大小和渲染成本随图像分辨率与输入视角数量快速增长。论文关注的问题是：如何在不针对每个预算重新训练、也不做逐场景压缩的前提下，让单一模型适应不同数量的上下文视角和多种测试时预算（保留比例）。

### 核心思路/方法
- 将压缩从“简单重要性排序”重新表述为重要性估计、空间覆盖与跨视角冗余的联合问题。
- 提出 Intra-Cross Mask Supervision，为学习高斯重要性提供结构、覆盖和冗余感知的监督。
- 使用 budget-conditioned feature modulation，根据请求的保留比例调整高斯不透明度与属性。
- 提出 Coverage-Aware Budget Selection，结合 patch 级预选、视角级不透明度排序和 3D 冗余抑制，构造紧凑且空间分布合理的高斯表示。
- 单个训练模型支持变化的上下文视角数量和多个测试时预算，无需按预算重训或逐场景压缩。

### 主要贡献
- 提出预算可控的前馈可泛化高斯泼溅框架 BudgetSplat，使最终高斯表示适配用户指定的保留比例。
- 将表示压缩建模为重要性、空间覆盖与跨视角冗余的联合问题，而非单一重要性排序。
- 设计 Intra-Cross Mask Supervision 与 budget-conditioned feature modulation，以学习高斯重要性并适配不同保留比例。
- 提出 Coverage-Aware Budget Selection，用于构建紧凑且空间分布良好的高斯表示。
- 摘要称在室内重建与跨数据集泛化实验中，不同输入视角数量和保留比例下表现出一致的质量—大小权衡，并在保持渲染质量的同时显著降低最终表示存储与渲染成本。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集名称、定量指标、计算开销细节、失败案例或与基线方法的完整对比，因此无法基于摘要判断方法的具体局限。

### 阅读优先级
中。理由：该论文针对前馈 3D Gaussian Splatting 的表示冗余与预算控制问题，问题定义清晰且方法包含监督设计、特征调制和预算选择三个组成部分；但摘要未提供定量结果与实验细节，是否值得优先精读取决于读者对高斯泼溅压缩、可泛化新视角合成和测试时预算控制的兴趣。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting enables efficient generalizable novel view synthesis, but existing pixel-aligned methods often generate highly redundant Gaussian primitives, causing the final representation size and rendering cost to grow rapidly with image resolution and the number of input views. We propose BudgetSplat, a budget-controllable feed-forward framework that adapts the final Gaussian representation to a user-specified preservation ratio. Rather than treating compaction as simple importance ranking, we formulate it as a joint problem of importance estimation, spatial coverage, and cross-view redundancy. A single trained model supports varying numbers of context views and multiple test-time budgets without per-budget retraining or per-scene compression. To realize this formulation, Intra-Cross Mask Supervision provides structure-, coverage-, and redundancy-aware guidance for learning Gaussian importance, while budget-conditioned feature modulation adapts Gaussian opacity and attributes to the requested preservation ratio. Coverage-Aware Budget Selection further combines patch-wise pre-selection, view-wise opacity ranking, and 3D redundancy suppression to construct compact yet spatially distributed Gaussian representations. Experiments on indoor reconstruction and cross-dataset generalization demonstrate consistent quality--size trade-offs across different input view counts and preservation ratios, substantially reducing final representation storage and rendering cost while preserving rendering quality.

</details>

#### 2026-11-04 - T$^2$-Splat: Adaptive Topology Mesh Splatting with Texture Residuals

**Authors:** Zhihao Tang, Youjia Zhang, Mingbo Zhao, Wei Yang
**Links:** [abs](https://arxiv.org/abs/2611.06974) - [pdf](https://arxiv.org/pdf/2611.06974)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：T$^2$-Splat: Adaptive Topology Mesh Splatting with Texture Residuals
- 作者：Zhihao Tang, Youjia Zhang, Mingbo Zhao, Wei Yang
- 出版日期：2026-11-04T13:09:22Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.06974) / [PDF](https://arxiv.org/pdf/2611.06974)

### 一句话总结
提出 T$^2$-Splat，将拓扑自适应与外观细化解耦，在较紧凑的网格上实现有竞争力的新视角合成结果。

### 研究问题
基于三角形的 splatting 将新视角合成与传统图形管线连接起来，但通常需要过多细分（excessive tessellation）来保留外观细节。论文关注如何在不依赖过度细分的情况下兼顾网格拓扑适配与外观细节表达。

### 核心思路/方法
- 将拓扑自适应与外观细化解耦。
- 使用 Safe Restricted Delaunay Triangulation（Safe RDT）初始化网格连通性。
- 通过 Dynamic Topology Evolution（DTE）以边坍缩和顶点分裂操作调整三角形分配。
- 在固定网格上使用逐面残差 Mip-textures，并结合尺度自适应滤波细化外观。

### 主要贡献
- 提出 T$^2$-Splat 框架，解耦拓扑适配与外观细化。
- 引入 Safe RDT 初始化网格连通性，并用 DTE 通过边坍缩与顶点分裂自适应分配三角形。
- 使用逐面残差 Mip-textures 和尺度自适应滤波在固定网格上细化外观。
- 在 Mip-NeRF 360、Tanks & Temples 和 DTU 上展示使用紧凑网格的竞争性结果；在 Mip-NeRF 360 上相较 MeshSplatting 提升 PSNR 0.71dB。
- 压缩实验显示可灵活控制网格复杂度，面预算可低至原始面数的 10%。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败场景、对特定数据类型或场景规模的限制、运行开销或内存消耗等细节。

### 阅读优先级
中。理由：论文聚焦三角形 splatting 中的拓扑自适应与外观细化解耦，报告了紧凑网格下的竞争性结果和明确的 PSNR 提升，并支持低至 10% 面预算的压缩控制；但摘要未提供失败案例、效率开销等限制信息，是否优先阅读取决于读者对基于网格的新视角合成与压缩控制的兴趣。

</details>

<details>
<summary>Abstract</summary>

Triangle-based splatting connects novel view synthesis with conventional graphics pipelines, but often requires excessive tessellation to preserve appearance details. We present T$^2$-Splat, which decouples topology adaptation from appearance refinement. Safe Restricted Delaunay Triangulation (Safe RDT) initializes mesh connectivity. Dynamic Topology Evolution (DTE) then adapts triangle allocation through edge collapse and vertex split operations. Residual per-face Mip-textures then refine appearance on the fixed mesh using scale-adaptive filtering. Experiments on Mip-NeRF 360, Tanks & Temples, and DTU demonstrate competitive results with compact meshes. T$^2$-Splat improves PSNR by 0.71dB over MeshSplatting on Mip-NeRF 360. Additional compression experiments demonstrate flexible control of mesh complexity, supporting face budgets as low as 10% of the original face count. Project page: https://t2-splat.github.io/.

</details>

#### 2026-11-04 - TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics

**Authors:** Shu'ang Sun, Yibo Qiu, Haoliang Ye, Zan Huang, Ao Tian, Kan Ding, Ronald Xu, Mingzhai Sun
**Links:** [abs](https://arxiv.org/abs/2611.06442) - [pdf](https://arxiv.org/pdf/2611.06442)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, robotics, manipulation, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics
- 作者：Shu'ang Sun, Yibo Qiu, Haoliang Ye, Zan Huang, Ao Tian, Kan Ding, Ronald Xu, Mingzhai Sun
- 出版日期：2026-11-04T12:44:51Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.06442) | [PDF](https://arxiv.org/pdf/2611.06442)

### 一句话总结
TwinBridge 用 3D Gaussian splatting 与物理仿真构建数字孪生，把仿真中的任务事件与几何进展转化为策略预训练和稠密视觉奖励，用于真实实验室机器人操作的人机在环在线强化学习。

### 研究问题
论文针对真实世界在线强化学习在实验室精细操作中的两个瓶颈：真实演示成本高，且难以获得稠密的过程奖励。摘要指出，这些问题阻碍了在线强化学习的实际应用。

### 核心思路/方法
- 通过结合 3D Gaussian splatting 与物理仿真构建数字孪生。
- 在物理前提、顺序约束下，由仿真器状态提供任务事件与几何进展，并据此产生奖励，用于基于仿真演示和强化学习的策略预训练。
- 将上述监督蒸馏为视觉奖励模型。
- 在真实世界交互中，将视觉奖励模型的预测与执行历史结合，计算稠密奖励，用于人机在环的策略精炼。

### 主要贡献
- 提出数字孪生驱动的框架，为真实世界在线学习同时提供策略初始化与稠密视觉奖励。
- 将仿真器提供的任务事件与几何进展监督蒸馏为视觉奖励模型，并在真实交互中结合执行历史生成稠密奖励。
- 在五个真实实验室任务上报告最终平均自主成功率为 98%，每个任务最多使用 25 分钟真实世界交互。
- 实验表明，稠密奖励相比稀疏奖励提升交互效率，基于仿真的策略初始化进一步加速学习。

### 局限性
- 摘要仅报告五个真实实验室任务与总体成功率，未提供各任务的具体成功率、方差或失败案例分析；摘要未提供足够信息。
- 摘要未说明视觉奖励模型在分布外场景或不同实验室环境中的泛化表现；摘要未提供足够信息。
- 摘要未给出人机在环干预的频率、形式与人工成本细节；摘要未提供足够信息。
- 摘要未提供与基线方法的完整定量对比、消融实验设置及统计显著性信息；摘要未提供足够信息。
- 摘要未说明数字孪生构建所需的时间、标注或建模成本；摘要未提供足够信息。

### 阅读优先级
中。理由：该工作面向真实机器人强化学习中“演示成本高、奖励稀疏”的关键问题，方法组合（3D Gaussian splatting + 物理仿真 + 视觉奖励蒸馏）与实验室操作场景具有明确应用价值，且摘要给出了成功率与交互时长等结果信号；但摘要未提供基线对比、消融细节与泛化分析，是否值得深入阅读需结合全文实验严谨性进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：CrossPressor: Scalable Cross-View Fusion for Feed-Forward 3D Gaussian Splatting
- 作者：Yuxi Hu, Wenhao Dong, Jun Zhang, Friedrich Fraundorfer
- 出版日期：2026-11-04T10:07:15Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.06258) | [PDF](https://arxiv.org/pdf/2611.06258) | [项目页](https://yuhsihu.github.io/CrossPressor/)

### 一句话总结
CrossPressor 是一种免训练的可扩展 anchor 融合方法，通过 coverage-cycled evidence routing 缓解固定 anchor 与增长支撑视图之间的表示—融合失配，在保持接近稠密融合的重建质量的同时显著加速跨视图融合。

### 研究问题
前馈 3D Gaussian Splatting（3D-GS）在扩展到长多视图序列时，表示规模会显著增长。基于 anchor 的压缩方法（如 ZPressor）通过仅从一小组紧凑的 anchor 特征图解码 Gaussians 来缓解该问题，但保持 anchor 固定会迫使每个 anchor 聚合越来越多的支撑视图，从而产生“表示—融合失配”（representation–fusion mismatch）。论文即针对该失配问题展开。

### 核心思路/方法
CrossPressor 是一种免训练（training-free）的可扩展 anchor 融合方法。其核心做法包括：
- 保留所有面向解码器的 anchor queries；
- 通过 coverage-cycled evidence routing 约束随视图增长的支撑序列，将保留的空间证据分布到各支撑视图与融合层中，同时保持所有支撑视图均被表示；
- 在 K/V 投影之前进行路由，并结合 joint context packing，以进一步降低支撑侧融合成本，且无需重新训练。

### 主要贡献
- 识别出固定 anchor 压缩方法在长视图序列下的表示—融合失配问题；
- 提出免训练的 CrossPressor，用于可扩展的基于 anchor 的融合；
- 通过 coverage-cycled evidence routing 在支撑视图与融合层间分配空间证据，并保持所有支撑视图被表示；
- 在 K/V 投影前路由并结合 joint context packing 降低融合成本，无需重训练；
- 摘要称在长输入序列上保持接近稠密融合的重建质量，跨视图融合最高加速 \(26.12\times\)，端到端最高加速 \(1.43\times\)。

### 局限性
摘要未提供足够信息。例如具体数据集、基线设置、质量指标的完整数值、不同序列长度下的详细消融、训练-free 特性对其他 anchor 方法的普适性等，均未在摘要中给出。

### 阅读优先级
中。理由：该工作针对前馈 3D-GS 在长多视图序列下的可扩展融合问题，提出免训练且报告了显著加速，问题定义清晰、工程价值明确；但摘要未提供充分实验细节与质量指标，需阅读全文后才能判断其泛化性与实际收益。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3D-GS) becomes increasingly difficult to scale to long multi-view sequences. Anchor-based compression methods such as ZPressor alleviate representation growth by decoding Gaussians only from a compact set of anchor feature maps, but keeping these anchors fixed forces each one to aggregate an increasing number of support views. We identify this representation--fusion mismatch and introduce \textbf{CrossPressor}, a training-free method for scalable anchor-based fusion. CrossPressor preserves all decoder-facing anchor queries while constraining the view-growing support sequence through coverage-cycled evidence routing, distributing retained spatial evidence across support views and fusion layers while keeping all support views represented. Routing before K/V projection, together with joint context packing, further reduces support-side fusion cost without retraining. CrossPressor maintains reconstruction quality close to dense fusion while achieving up to $26.12\times$ faster cross-view fusion and $1.43\times$ end-to-end acceleration on long input sequences. Our project page is at: https://yuhsihu.github.io/CrossPressor.

</details>

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-09 - AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA

**Authors:** Yuguang Yang, Zhewen Tan, Canyu Chen, Linlin Yang, Cheng Chi, Chunyang Liu, Kehua Sheng, Jinyu Yang, Baochang Zhan, Bo Zhang, Yan Wang, Xianbin Cao
**Links:** [abs](https://arxiv.org/abs/2611.12382) - [pdf](https://arxiv.org/pdf/2611.12382)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous trajectory. We address this gap with TrajCond, which introduces a discrete trajectory-geometric condition for VLA planning. Specifically, we represent TrajCond as a 1D-Brohan differential action trajectory and learn it with a two-stage training framework before final continuous trajectory prediction. With the simultaneous autoregressive generation of discrete and numeric trajectories, we name our method AutoVLA-D (Double). Experiments on NAVSIM navtest, nuScenes, and NeuroNCAP show that discrete trajectories are weaker as direct outputs but more effective as TrajCond, consistently improving final continuous trajectory prediction across closed-loop and open-loop driving benchmarks. Code is available at https://github.com/ShivaTeam/AutoVLA-D.

</details>

#### 2026-11-09 - QCC-WM: Linking Macro-State Dynamics and Visual Generation via Quotient Causal Construction

**Authors:** Zhizhong Fu, Wei Zhou, Zhaoyang Jiang, Yudong Lin, Songlun Li, Zhi Li, Feifan Chen, Gaoming Li, Xiaorong Ding, Yifan Chen
**Links:** [abs](https://arxiv.org/abs/2611.12353) - [pdf](https://arxiv.org/pdf/2611.12353)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>Abstract</summary>

A key challenge in action-conditioned world modeling is to construct macro-states from high-dimensional observations that support recursive prediction under actions, while keeping their predicted evolution consistent with visual changes in generated observations. We propose QCC-WM, a visual world model based on Quotient-based Causal Construction. QCC-WM uses action responses to guide macro-variable construction for recursive action-conditioned prediction. A shared reference quotient measurement constrains the consistency between predicted states and observed changes, allowing macro-level predictions to provide structured constraints for future visual generation. Using translational and rotational actions and their predicted responses, the model aggregates local visual features into macro-nodes with spatial correspondence through causal abstraction, and recursively predicts node content and motion under a shared reference measurement. Macro-level predictions guide future observation generation, while predicted motion transports historical appearance information. Node-level errors between generated observations and macro-level targets are then mapped back to the corresponding spatial regions for correction, improving consistency between visual generation and macro-level predictions. On the US-VLA dataset, QCC-WM achieves an ROI-MSE of 0.01861 for four-step prediction. Compared with the best baseline at each prediction horizon, it reduces LPIPS by 48.59%, 41.68%, and 30.23% for four-step prediction and eight- and sixteen-step recursive extrapolation, respectively. Ablation studies and mechanism analyses show that motion-guided reference transport mainly improves pixel reconstruction, while node-level error feedback further improves perceptual quality and consistency between generated observations and macro-level predictions.

</details>

#### 2026-11-09 - UniOMA: Unified Optimal-Transport Multi-Modal Structural Alignment for Robot Perception

**Authors:** Xinrui Zu, Mark Hoogendoorn, Kevin Sebastian Luck, Shujian Yu
**Links:** [abs](https://arxiv.org/abs/2611.12351) - [pdf](https://arxiv.org/pdf/2611.12351)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot perception

<details>
<summary>Abstract</summary>

Achieving generalizable and well-aligned multimodal representations remains a core challenge in robot learning. While recent approaches have attempted to align modalities by modeling conditional or higher-order statistical dependencies, they do not explicitly consider the structural coherence across modalities. In this work, we propose a novel multimodal alignment method that augments existing contrastive losses with a geometry-aware Gromov--Wasserstein (GW) distance-based regularization. To this end, we encode intra-modal geometry for each modality and reduce cross-modal structural discrepancies through a dynamically learned GW barycenter, thereby encouraging structural consistency in addition to instance-level contrastive alignment. We apply this optimal-transport-based alignment strategy to robot perception tasks involving underexplored modalities such as force and tactile signals, where modality data often exhibit varying sample densities. Extensive experiments on five robotic benchmarks show that our method improves structural alignment and downstream performance over state-of-the-art multimodal contrastive baselines across a wide range of downstream tasks, including robot and environment state prediction. Moreover, our GW-based regularization can be seamlessly integrated into most InfoNCE-like objectives.

</details>

#### 2026-11-09 - GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation

**Authors:** Jinghe Wang, Xinrui Cao, Duo Wu, Chenghao Gu, Yong Zhong, Linjia Kang, Tianyi Xiong, Zhi Wang
**Links:** [abs](https://arxiv.org/abs/2611.12175) - [pdf](https://arxiv.org/pdf/2611.12175)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>Abstract</summary>

Robotic manipulation has advanced rapidly in mapping visual observations and language instructions to actions. However, reliable manipulation in open-world environments requires robust spatial understanding: the ability to identify targets in complex layouts (spatial reasoning) and adapt to scenes that continuously evolve through interaction (spatial memory). Yet existing embodied benchmarks fall short in evaluating spatial understanding: they often introduce strong visual cues that bypass spatial reasoning, and focus on static scenes that offer little insight into an agent's capacity for spatial memory. To address this gap, we introduce GeoMind, a systematic benchmark for structured spatial understanding through tabletop manipulation. GeoMind comprises 54 evaluated task variants organized around spatial reasoning and spatial memory. It also incorporates a scalable pipeline that automates the generation and annotation of task instances with verified targets and executable interactions. Extensive evaluations across diverse embodied agents reveal their consistent weaknesses in spatial understanding. Our findings highlight that these agents struggle to track identities after spatial changes and convert relational or geometric constraints into executable actions. We release the GeoMind benchmark at https://github.com/Notfound-JH/GEOMIND-benchmark.git.

</details>

#### 2026-11-09 - OASIS: Optimization-Aware Subgoal Inference with Safety Constraints for Autonomous Mobile Robot Navigation

**Authors:** Arian Hajizadeha, Javad Pourrafia, Negar Shenavara, Sana Bashiria, Seyed Majid Esmailzadeh
**Links:** [abs](https://arxiv.org/abs/2611.11996) - [pdf](https://arxiv.org/pdf/2611.11996)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>Abstract</summary>

Navigation in dynamic environments requires mobile robots to make progress toward their goals while respecting motion limits and avoiding surrounding obstacles. Learned subgoal policies can guide model predictive control beyond its local prediction horizon, but a geometrically suitable subgoal does not necessarily lead to a successfully solved control problem. This paper proposes OASIS, a hierarchical navigation framework that incorporates recent optimization outcomes into reinforcement learning-based subgoal generation. A high-level policy trained using Soft Actor--Critic generates local subgoals, while a nonlinear model predictive controller tracks them subject to motion limits, geometric collision-avoidance constraints, and embedded high-order control barrier function constraints. The outcomes of controller optimizations over each subgoal interval are summarized and provided to the policy at its next decision, without requiring additional optimization calls. The framework is evaluated in five navigation scenarios with static and moving obstacles, including dense interactions and sensing uncertainty. Comparisons with hierarchical and direct-goal control variants show that OASIS achieves the highest aggregate navigation success. Matched comparisons across three training seeds further show a consistent success advantage over the otherwise identical hierarchy without optimization-status input. The selected-policy comparison also shows fewer primary optimization failures with similar mean controller time.

</details>

#### 2026-11-08 - Feel My Focus: Gaze-Triggered Digital Twin Creation for Remote Collaboration

**Authors:** Shih-Yu Ma, Suibi Che-Chuan Weng, Ming-Yuan Pai, Tom Yeh, Ellen Yi-Luen Do
**Links:** [abs](https://arxiv.org/abs/2611.11640) - [pdf](https://arxiv.org/pdf/2611.11640)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mixed reality, digital twin

<details>
<summary>Abstract</summary>

We present Feel My Focus, a gaze-triggered mixed reality (MR) demonstration that enables rapid creation and sharing of lightweight 3D digital twins during remote collaboration. Unlike systems that use gaze primarily as a referential pointer, Feel My Focus treats sustained visual attention as a generative action: a fixation on a physical object initiates single-image capture, attention-guided segmentation, and one-shot 3D reconstruction, allowing a remote partner to inspect and discuss the object in situ. The system integrates gaze-tracking glasses, modular segmentation and reconstruction services, and an MR client for runtime streaming and interaction. This design prioritizes responsiveness and experiential continuity over photometric fidelity. We report observations from a public demonstration, highlighting design trade-offs, failure modes, and user control considerations for deploying gaze-triggered generative systems in real-world collaborative settings.

</details>

#### 2026-11-08 - ScanDreamer: A Map-Grounded World Model for Quadrotor Navigation

**Authors:** Yunyi Gao, Yixing Shi, Yize Liu, Hai-Duong Tran, Nhat-Hoang P. Nguyen, Shuai Wang, Yi Deng, Shengming Liu, Sim Kuan Goh, Duc-Thinh Pham, Sameer Alam
**Links:** [abs](https://arxiv.org/abs/2611.11605) - [pdf](https://arxiv.org/pdf/2611.11605)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding, world model

<details>
<summary>Abstract</summary>

Quadrotors inspecting buildings and tunnels must navigate unknown clutter with a forward-facing depth camera whose limited field of view constrains scene understanding and collision-avoiding navigation. Recent world-model agents learn navigation through imagined experience (e.g., AirDreamer), but remain data-intensive and often lack explicit geometric memory and awareness of what the camera can observe. We propose ScanDreamer, a map-grounded world model that constructs an online 2D scan-memory map from depth images and vehicle pose. Our world model, actor, and critic are conditioned on this map, which also defines a geodesic progress reward. Moreover, a forward-cone penalty discourages horizontal motion outside the camera's viewing direction. During imagination, ScanDreamer propagates the quadrotor pose over a frozen map and derives progress and wall-contact signals from the mapped geometry. We train ScanDreamer for 0.8 million environment steps (5.5 h on one GPU) and evaluate it in NVIDIA Isaac Sim over 1560 episodes spanning unseen layouts and parameter ranges. Across three seeds (mean $\pm$ SD), ScanDreamer achieves 96.3 $\pm$ 0.3% success with 3.6 $\pm$ 0.3% collision, compared with 59.6 $\pm$ 3.0% success and 28.8 $\pm$ 2.8% collision for AirDreamer at the same online-interaction budget. Removing the forward-cone penalty increases collisions to 9.9 $\pm$ 3.1%. These results show that combining explicit map memory, map-grounded imagination, and perception-aware motion substantially improves navigation performance and data efficiency. The source code is available at https://github.com/WANGSHUAIzzzz/ScanDreamer.

</details>

#### 2026-11-08 - How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding

**Authors:** Gengyuan Zhang, Xiao Han, Shijie Zhou, Abdullah Koukash, Jingpei Wu, Jindong Gu, Yuqicheng Zhu, Nassir Navab, Volker Tresp, Ghazal Ghazaei
**Links:** [abs](https://arxiv.org/abs/2611.11437) - [pdf](https://arxiv.org/pdf/2611.11437)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, scene understanding

<details>
<summary>Abstract</summary>

Evaluating general-purpose multimodal large language models (MLLMs) for surgical scene understanding remains limited due to scarce surgical data and fragmented evaluation protocols. We address these challenges through a two-stage evaluation framework for surgical scene understanding. In Stage I, we introduce SurgKnowBench, a diagnostic benchmark that harmonizes public surgical datasets across procedures and tasks and evaluates proprietary and open-source MLLMs to map the boundary of pretrained surgical competence. SurgKnowBench reveals that current models retain partial visual priors but remain weak on relational and procedural understanding and workflow assessment. Building on this failure frontier and motivated by the scaffolded nature of surgical training, we introduce SurgAgentGym, an agentic environment where general-purpose MLLM agents can use bounded knowledge search over SurgWiki and general-purpose visual grounding for surgical tasks. SurgAgentGym evaluates whether generalist agents can improve surgical understanding at inference time through tool-mediated evidence use, without additional surgical training. Our results show that agentic inference narrows the gap mainly for perception-heavy tasks, while fine-grained localization and expert-style assessment remain persistent bottlenecks. This opens a path toward future studies of agentic surgical understanding.

</details>

#### 2026-11-08 - DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight

**Authors:** Zhongxi Chen, Yi Yang, Xinyi Chen, Mingzhe Ye, Yaping Li, Zhihong Liu, Congsheng Xu, Haonan Wang, Zhijie Deng
**Links:** [abs](https://arxiv.org/abs/2611.11166) - [pdf](https://arxiv.org/pdf/2611.11166)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world model

<details>
<summary>Abstract</summary>

Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand. Existing world-action models often acquire such predictive knowledge through explicit future prediction. We introduce DexForesight, a framework that learns spatial foresight implicitly by injecting dynamics-aware world representations into the latent space of a dexterous policy. During training, DexForesight learns an action-conditioned spatial world model from offline scene depth, kinematic hand geometry, and demonstration trajectories. The world model predicts 3D hand-point motion and visual feature changes, capturing both articulated hand dynamics and scene changes under demonstrated actions, including the motion of fingers occluded from the cameras. We then freeze the world model and align policy queries with its predictive world queries, transferring the learned spatial dynamics into policy latents and using them to condition action generation. At deployment, only the policy is retained, operating on RGB observations, language, and robot state without depth input or explicit future prediction. On 11 DexJoCo simulation tasks, DexForesight improves the overall success rate of the base policy from 49.4% to 60.5%. On three real-robot dexterous manipulation tasks, DexForesight achieves 58.3% success, compared with 50.0% for the strongest baseline.Project page https://dexforesight.github.io/

</details>

#### 2026-11-08 - MOSU2: Long-range Navigation System with Multi-modal Scene Understanding

**Authors:** Jing Liang, Zhenyu Hou, Senthurbavan Kirubaharan, Md Safwan Mondal, Ashok Gudivada, Xuesu Xiao, Dinesh Manocha
**Links:** [abs](https://arxiv.org/abs/2611.11148) - [pdf](https://arxiv.org/pdf/2611.11148)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>Abstract</summary>

Robots that travel long distances through public outdoor spaces must do more than avoid obstacles: they must remain on terrain suited to their mobility and decide when to proceed, yield, or detour around pedestrians, cyclists, vehicles, traffic signals, and temporary restrictions. These decisions are difficult because their correctness often depends on how a scene evolves, such as whether an approaching car is slowing or a cyclist will cross the robot's path. Vision-language models (VLMs) can interpret such cues, but they reason over images that lack metric geometry and motion. Supplying this evidence at every step is too slow for real-time navigation, and hand-crafted triggers cannot anticipate the open-ended variety of outdoor situations. We present MOSU2, a long-range navigation system with two-stage trajectory selection, in which first-stage contextual reasoning determines when additional evidence is needed and what to retrieve. Only when an interaction remains unresolved does the first stage trigger the second stage to retrieve geometric and dynamic information and align it with scene context to make navigation decisions. Building on MOSU, MOSU2 follows routes from GPS-based route planning and filters candidate trajectories through multi-modal traversability analysis before selecting a trajectory to move the robot. In real-world experiments spanning stop gestures, construction sites, crosswalks, and roads shared with vehicles, cyclists, and pedestrians, MOSU2 raises mean navigation success from 61.8% to 94.2% and condition-detection accuracy from 72.2% to 91.4% over its single-image predecessor, at about 2.2 times its mean decision latency. Project website: https://jinggm.github.io/mosu2/

</details>

#### 2026-11-08 - ObjectWorld: Scaling Object-Centric World Models with A Large-Scale 3D Full-Object Flow Dataset

**Authors:** Haonan Chen, Sicheng Isabella Lu, Haitian Li, Jiajin Wu, Hexiang Wei, Jiawei Zhang, Xin Fei, Yiwen Hou, Chenrui Tie, Chongkai Gao, Sheng Wang, Lin Shao
**Links:** [abs](https://arxiv.org/abs/2611.11085) - [pdf](https://arxiv.org/pdf/2611.11085)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model, world modeling

<details>
<summary>Abstract</summary>

Generative world modeling from large-scale visual data offers a promising path toward scalable robot manipulation. This calls for an intermediate representation that can be supervised at scale and remains actionable for downstream control. We propose 3D full-object flow, an object-centric motion representation that assigns dense 3D trajectories to points across the complete surface of a target object, including its occluded regions. By extending visible-surface object flow to the full object geometry, this representation makes complete object motion explicit and applies uniformly to both rigid and deformable objects. To realize the potential of this representation at scale, we introduce a 1210-hour full-object flow dataset that addresses the scarcity of large-scale supervision for complete 3D object motion. The dataset integrates diverse real-world videos and physical simulations, with a scalable annotation pipeline for recovering full-object motion from real-world observations and quality metrics for systematically assessing annotation quality. We then train a world model that takes an image and a task description as input and predicts dense full-object flow over the reconstructed object geometry. Experiments show reliable annotation quality, data-scalable flow prediction, and effective downstream manipulation across novel scenes and robot embodiments. Project website with additional results and videos: https://nus-lins-lab.github.io/ObjectWorld/.

</details>

#### 2026-11-05 - TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

**Authors:** Yijiong Lin, Wenhao He, Toby Jack, Max Yang, Haoran Li, Nathan F. Lepora
**Links:** [abs](https://arxiv.org/abs/2611.07881) - [pdf](https://arxiv.org/pdf/2611.07881)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation
- 作者：Yijiong Lin, Wenhao He, Toby Jack, Max Yang, Haoran Li, Nathan F. Lepora
- 出版日期：2026-11-05T12:01:12Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.07881 ；PDF https://arxiv.org/pdf/2611.07881

### 一句话总结
TactileLab 是一个基于 IsaacLab 的可扩展多模态触觉仿真框架，用基于光流的“模拟触觉流”替代高计算成本的软体/可变形仿真来表征接触剪切，并结合真到仿触觉翻译与新的数据采集方法，实现从仿真训练到真实双臂与灵巧手内操作部署的端到端 sim-to-real 流程。

### 研究问题
论文关注接触丰富操作中的触觉仿真问题：高保真地模拟触觉传感中的剪切通常依赖可变形或软体仿真，计算开销大，难以扩展到大规模强化学习。因此需要一种可扩展、能高效表征剪切相关接触动力学的触觉仿真方式，并解决仿真触觉与真实触觉之间的迁移问题，以支持真实机器人上的灵巧操作部署。

### 核心思路/方法
- 构建于 IsaacLab 之上的可扩展多模态触觉仿真框架 TactileLab。
- 提出“模拟触觉流”（simulated tactile flow）：不依赖软体物理建模剪切变形，而使用刚体仿真高效估计接触界面的稠密切向运动，生成编码剪切相关接触动力学的触觉流场。
- 该流场与接触深度场提供的几何特征互补，形成多模态触觉表征。
- 提出一种新的策略架构，用于联合处理长时程本体感知信号与丰富触觉观测。
- 为促进 sim-to-real 部署，提出真到仿触觉翻译方法，将真实触觉图像流映射为模拟触觉流与深度场，并提出新的触觉数据采集方法，在不同触觉传感器设计上进行验证。
- 使用该流程在包含双臂与灵巧手内操作的任务上展示真实世界部署。

### 主要贡献
- 提出 TactileLab：基于 IsaacLab 的可扩展多模态触觉仿真框架，聚焦剪切敏感触觉。
- 提出基于光流的模拟触觉流表征，以刚体仿真高效估计接触界面稠密切向运动，避免依赖高成本软体/可变形仿真来建模剪切。
- 将触觉流场与接触深度场结合，形成互补的触觉观测。
- 提出联合处理长时程本体感知与丰富触觉观测的新策略架构。
- 提出真到仿触觉翻译方法，将真实触觉图像流映射为模拟触觉流和深度场，并配合新的触觉数据采集方法，在多种触觉传感器设计上验证。
- 在多种接触丰富任务中，使用模拟触觉流训练的策略表现出可扩展的高效学习，并出现接触感知行为；在真实世界双臂与灵巧手内操作任务上完成部署。
- 整体上提供面向可扩展触觉策略学习的端到端 sim-to-real 框架，支持异构触觉机器人系统上的剪切敏感操作。

### 局限性
摘要未提供足够信息。摘要未给出具体任务清单、成功率、训练规模、仿真与真实实验的定量对比、失败案例、传感器型号与数量、计算开销数据，也未说明方法在超出已验证传感器设计与任务范围外的适用性限制。

### 阅读优先级
中。理由：该论文聚焦触觉仿真中的剪切表征与 sim-to-real 迁移，对接触丰富操作、触觉强化学习和灵巧操作方向具有明确相关性；其“用刚体仿真估计触觉流替代软体仿真”的思路和真到仿触觉翻译具有一定方法新颖性。但仅凭摘要无法判断定量效果、可复现性与跨传感器泛化程度，建议在需要评估触觉仿真效率或灵巧操作 sim-to-real 方案时阅读全文进一步核实。

</details>

<details>
<summary>Abstract</summary>

Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable multimodal tactile simulation framework built on IsaacLab, with a particular focus on a new optical-flow-based tactile representation termed \textit{simulated tactile flow}. Instead of relying on soft-body physics to model shear deformation, TactileLab uses rigid-body simulation to efficiently estimate dense tangential motion at the contact interface, producing tactile flow fields that encode shear-relevant contact dynamics. This flow field complements geometric features from a contact depth field. We further introduce a novel policy architecture for jointly processing long-horizon proprioceptive signals and rich tactile observations. Across multiple contact-rich tasks, policies trained using simulated tactile flow learn efficiently at scale and exhibit emergent contact-aware behaviours. To facilitate sim-to-real policy deployment, we then propose a novel real-to-sim tactile translation method that maps real tactile image streams to simulated tactile flow and depth fields, together with a new tactile data collection method, and validate it across diverse tactile sensor designs. Using this pipeline, we demonstrate real-world deployment on tasks encompassing dual-arm and dexterous in-hand manipulation. Overall, TactileLab provides an end-to-end sim-to-real framework for scalable tactile policy learning, enabling diverse shear-sensitive manipulation across heterogeneous tactile robotic systems.

</details>

#### 2026-11-04 - Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation

**Authors:** Weiduo Yuan, Ze Yuan, Sihan Liu, Jionghao Wang, Liang Heng, Zhenyu Zhao, Yue Wang
**Links:** [abs](https://arxiv.org/abs/2611.07229) - [pdf](https://arxiv.org/pdf/2611.07229)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation
- 作者：Weiduo Yuan, Ze Yuan, Sihan Liu, Jionghao Wang, Liang Heng, Zhenyu Zhao, Yue Wang
- 出版日期：2026-11-04T23:34:19Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.07229) / [PDF](https://arxiv.org/pdf/2611.07229)

### 一句话总结
提出 Spatial-UMI-Dream，一个基于 605 小时 RGB-D UMI 数据、经两阶段训练以联合预测未来 RGB、鱼眼对齐度量深度与动作的 5B 空间 World Action Model，并配套构建 RoboTwin-UMI 基准以评估 UMI 策略在环境与机器人本体变化下的泛化性。

### 研究问题
UMI 虽支持与特定机器人无关的可扩展演示采集，但其移动的近距夹爪相机使相机运动与物体运动相互纠缠，缺乏稳定外部视角；精确操作所需的度量几何信息仅隐含在 RGB 中。此外，评估 UMI 策略需要检验其“机器人无关演示采集”能否转化为跨机器人本体的策略泛化，以及对环境变化的鲁棒性。

### 核心思路/方法
- 构建 5B 规模的 Spatial-UMI-Dream（WAM），在 605 小时 RGB-D UMI 数据上预训练。
- 采用两阶段训练：先进行 world-only 适配，再进行 world-action 联合学习。
- 联合预测未来 RGB、鱼眼对齐的度量深度与动作；通过立体视觉推导的深度，在统一的双夹爪 RGB-D 表示中显式表达场景尺度与空间关系。
- 提出 RoboTwin-UMI：基于 RoboTwin 的二十任务仿真基准，使用 UMI 腕部安装鱼眼观测，可在不额外微调的情况下，分别及联合控制环境与本体变化进行评估。

### 主要贡献
- 提出融合度量几何与 RGB-D 表示的空间 World Action Model，以显式空间尺度缓解 UMI 视角下几何信息隐含的问题。
- 构建 RoboTwin-UMI 二十任务仿真基准，支持在环境变化、本体变化及二者联合条件下对 UMI 策略进行受控、可重复评估。
- 在 RoboTwin-UMI 上报告：域内成功率 79.10%，本体与环境联合偏移下 72.15%，分别超过最强评估基线 4.65 与 10.30 个百分点；在本体迁移下表现出评估策略中最小的成功率下降。
- 匹配预训练消融显示：仅 RGB 预训练相较 RGB-D 预训练使域内成功率下降 5.75 个百分点。
- 在六个真实世界任务上平均成功率达 85.0%，超过最强基线 24.2 个百分点。

### 局限性
- 摘要未提供足够信息说明模型参数量 5B 带来的计算成本、推理延迟或训练资源需求。
- 摘要未提供足够信息说明 RoboTwin-UMI 基准的任务多样性细节、仿真到现实差距及评测协议细节。
- 摘要未提供足够信息说明六个真实世界任务的具体设置、基线列表与统计显著性。
- 摘要未提供足够信息说明方法在非 UMI 采集设置或其他传感模态下的适用性。
- 摘要未提供足够信息说明失败案例、安全性或长期运行稳定性。

### 阅读优先级
高。理由：该工作同时涉及 UMI 操作中的度量几何建模、World Action Model 的大规模预训练与跨本体/环境泛化评测基准，摘要给出了明确的量化收益与消融结果，对具身操作与世界模型方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

The Universal Manipulation Interface (UMI) enables scalable demonstration collection independently of a specific robot. However, its moving, close-range gripper cameras entangle camera and object motion without a stable external view, leaving the metric geometry needed for precise manipulation implicit in RGB. We introduce Spatial-UMI-Dream, a 5B spatial World Action Model (WAM) pretrained on 605 hours of RGB-D UMI data through two-stage training -- world-only adaptation followed by joint world-action learning -- to jointly predict future RGB, fisheye-aligned metric depth, and actions. Stereo-derived depth makes scene scale and spatial relationships explicit within a unified dual-gripper RGB-D representation. Furthermore, evaluating UMI policies requires testing whether UMI's robot-independent demonstration collection translates into policy generalization across robot embodiments, alongside robustness to environmental changes. We introduce RoboTwin-UMI, a twenty-task simulation benchmark built on RoboTwin with UMI wrist-mounted fisheye observations, enabling controlled, repeatable evaluation of UMI policies under environment and embodiment changes separately and jointly without additional fine-tuning. On RoboTwin-UMI, Spatial-UMI-Dream achieves 79.10% in-domain success and 72.15% under combined embodiment and environment shifts, exceeding the strongest evaluated baseline in each setting by 4.65 and 10.30 percentage points, respectively. It also exhibits the smallest success-rate drop under embodiment transfer among the evaluated policies. In a matched pretraining ablation, RGB-only pretraining leads to a 5.75-percentage-point decrease in in-domain success compared with RGB-D pretraining. Across six real-world tasks, Spatial-UMI-Dream achieves 85.0% average success, exceeding the strongest baseline by 24.2 percentage points. Project page: https://weiduoyuan.com/spatial-umi-dream/

</details>

#### 2026-11-04 - USI-Brain: Enhancing Underwater Spatial Intelligence via Spatial Data-Driven Vision-Language Modeling

**Authors:** Zhiliang Zhu, Zhiqiang Zhao, Xie'an Jiang, Yingxin Lai, Kangye Zheng, Dawei Zhao
**Links:** [abs](https://arxiv.org/abs/2611.06040) - [pdf](https://arxiv.org/pdf/2611.06040)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：USI-Brain: Enhancing Underwater Spatial Intelligence via Spatial Data-Driven Vision-Language Modeling
- 作者：Zhiliang Zhu, Zhiqiang Zhao, Xie'an Jiang, Yingxin Lai, Kangye Zheng, Dawei Zhao
- 出版日期：2026-11-04T06:44:37Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.06040) / [PDF](https://arxiv.org/pdf/2611.06040)

### 一句话总结
该论文构建了一个水下空间数据引擎，用于生成大规模问答语料并训练 USI-Brain 视觉语言模型；该模型结合水下先验引导整流器（UPR），以增强水下空间推理能力。

### 研究问题
水下空间推理依赖物体边界和几何线索，但散射、颜色失真和低能见度会遮蔽这些线索。现有水下资源虽通过图像、标注和深度图记录这些线索，但为视觉语言模型提供的监督是碎片化的。论文试图解决如何将这些分散的视觉与几何信息组织为可用于视觉语言模型训练的空间监督。

### 核心思路/方法
- 提出一个空间数据引擎：通过增强、2D 与几何辅助的问题生成、专家过滤，将视觉外观与物体级几何连接起来，产出覆盖五类能力组的 4.27M 问答对。
- 使用该语料训练 USI-Brain。
- 引入 Underwater Prior-guided Rectifier（UPR），对视觉特征施加门控校正。
- 提出 USI-Bench，用 6,525 条留出问答对评估相关能力，包含 15 项任务指标。
- 评估时两个变体均使用原始图像。

### 主要贡献
- 构建空间数据引擎，生成覆盖五类能力组的 4.27M 问答对。
- 训练 USI-Brain，并引入 UPR 对视觉特征进行门控校正。
- 提出 USI-Bench（6,525 条留出问答对、15 项任务指标）。
- 在 USI-Bench 的 15 项任务指标上，USI-Brain 与 USI-Brain + UPR 分别平均优于 Qwen3-VL-8B-Instruct 5.76 和 7.63 分（100 分制有符号差异）。
- 消融显示：关闭 UPR 时，几何辅助监督使深度和顺序任务分别提升 4.8 和 6.1 分；在匹配训练数据下，UPR 在场景描述上增加 18.0 分。
- 在 NautData、UWBench 和 MarineEval 上，USI-Brain 在 32 项指标中的 28 项取得最佳或并列最佳。
- 模型权重与 USI-Bench 将发布。

### 局限性
- 摘要未提供数据引擎中各环节的具体实现细节与参数。
- 摘要未提供 USI-Bench 各任务指标的完整定义与细分结果。
- 摘要未提供 UPR 的门控机制结构、训练配置与计算开销。
- 摘要未提供与更多基线模型的系统比较细节。
- 摘要未提供失败案例、误差分析或跨域泛化限制的充分信息。
- 论文的局限性讨论、伦理与安全性分析：摘要未提供足够信息。

### 阅读优先级
中。理由：论文涉及水下视觉语言建模、空间推理数据构建与基准评测，对具身/机器人及水下感知方向有潜在相关性；摘要给出了明确的语料规模、基准规模和多项量化提升，但关键方法细节与局限性需阅读全文才能判断。若关注水下视觉语言模型或空间推理数据引擎，可列为中高优先级；若仅需概览，则为中。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：OdorSpaces: Visual-Olfactory Embodied Navigation in 3D Environments
- 作者：Changyeon Lee, Kelin Yu, Zheng Wei, Shuna Ni, Ruohan Gao
- 出版日期：2026-11-03T23:21:27Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2611.05738)｜[PDF](https://arxiv.org/pdf/2611.05738)

### 一句话总结
本文提出 OdorSpaces——一个基于物理模拟的视觉-嗅觉具身导航平台与基准，并给出一个融合视觉观察与嗅觉测量的多模态强化学习初始策略，用于室内气味源搜寻任务。

### 研究问题
摘要指出，嗅觉能提供关于空气中化学线索的关键信息，但在具身 AI 中仍很少被探索；已有机器嗅觉工作主要聚焦于语义层面的气味感知。因此，本文关注的问题是：如何让具身智能体在三维逼真室内环境中同时利用视觉与嗅觉观察进行导航，并完成气味源搜寻任务。

### 核心思路/方法
- **平台构建**：在 Habitat-Sim 基础上进行扩展，引入由 Fire Dynamics Simulator（FDS）模拟的三维气味传输与扩散，使智能体能够在照片级逼真的室内环境中使用视觉与嗅觉两种观察。
- **基准任务**：包含两个代表性的源搜寻场景——不可见气体泄漏定位与早期火灾定位。
- **策略方法**：开发了一个初始的多模态强化学习策略，随时间整合视觉观察与嗅觉测量。

### 主要贡献
- 提出 OdorSpaces，一个面向视觉-嗅觉具身导航的基于物理的模拟平台与基准。
- 将 FDS 模拟的三维气味传输与扩散与 Habitat-Sim 的逼真室内环境结合，支持视觉与嗅觉联合观察。
- 定义了不可见气体泄漏定位与早期火灾定位两个代表性源搜寻场景。
- 提出一个融合视觉与嗅觉时序信息的多模态强化学习初始策略；摘要称其优于多种基线，为后续视觉-嗅觉具身导航研究建立了较强参考。

### 局限性
- 摘要仅给出“优于多种基线”的总体结论，未提供具体基线类型、实验设置、评价指标与定量结果，**摘要未提供足够信息**。
- 策略被描述为“初始的”多模态强化学习策略，但其架构细节、训练方式与泛化能力，**摘要未提供足够信息**。
- 基准仅提及两个场景，是否覆盖更多气味类型、环境复杂度与真实迁移情形，**摘要未提供足够信息**。
- 模拟平台与真实世界之间的差距及验证情况，**摘要未提供足够信息**。

### 阅读优先级
**中**。理由：该工作将嗅觉模态引入具身导航并提供物理模拟平台与基准，问题设定具有探索价值；但摘要未提供实验细节与定量证据，若关注视觉-嗅觉多模态具身导航或气味源搜寻基准，可优先阅读全文以核实方法与结果。

</details>

<details>
<summary>Abstract</summary>

Olfaction provides critical information about airborne chemical cues, yet it remains largely underexplored in embodied AI, with limited prior machine olfaction work focusing primarily on semantic odor perception. We introduce OdorSpaces, a physics-based simulation platform and benchmark for visual-olfactory embodied navigation. OdorSpaces augments Habitat-Sim with 3D odor transport and dispersion simulated by Fire Dynamics Simulator (FDS), enabling agents to navigate photorealistic indoor environments using both visual and olfactory observations. The benchmark includes two representative source-seeking scenarios: invisible gas-leak localization and early-stage fire localization. We develop an initial multimodal reinforcement learning policy that integrates visual observations and olfactory measurements over time. Experiments show that the policy outperforms a diverse set of baselines, establishing a strong reference for future research on visual-olfactory embodied navigation.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
