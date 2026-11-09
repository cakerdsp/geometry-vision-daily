# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：75
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 21
  - Neural Scene Representations & Rendering: 20
  - Embodied / Robotics / AR Applications: 16
  - Geometry Foundation Models: 10
  - Dynamic / 4D Reconstruction: 8
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **前馈化与“去逐场景优化”成为 3D/4D 重建的主流工程方向。**
   - SM4RT 用级联前馈模型依次完成几何重建与运动估计；InstantHand 从单图直接构建可动画 Gaussian 手部 avatar，明确强调“无测试时优化”；BudgetSplat 让单一前馈模型支持多变视角数与多测试预算；X-VGGT 用前馈 Transformer 联合处理地面图与卫星图。
   - WV-GS 也以“免逐场景优化”为卖点切入自动驾驶宽视角合成。共同信号是：重建系统的竞争力越来越取决于**单次前向即可泛化**，而非每场景长时优化。

2. **几何精度与表示效率被单独拎出来作为一等目标，而非照片级质量的附属品。**
   - AffineGS 指出单目深度网络存在区域相关的分段线性失真，推翻 3DGS 中常用的全局 scale-shift 对齐；P-MGS 主张按“感知复杂度”而非网格密度分配高斯；HIBS 用 beta 核形状参数充当几何置信度旋钮；BudgetSplat 直接做预算可控的冗余抑制。
   - 这反映出一个方向转变：从“渲染得更像”转向“渲染得像的同时，几何可验证、表示可压缩、规模可控制”。

3. **可验证/可解释的优化重新回到 4D 重建叙事中。**
   - XM4D 将相机运动与非刚性形变分离，分别建模为结构化 QCQP，给出 SDP 松弛与全局最优性证书，再用结果初始化动态高斯泼溅。这与纯学习式前馈路线形成互补：一条追求前馈泛化，一条追求几何解的可证明性。
   - MetricTrail 则用度量深度作为软约束改进 DPVO 式稀疏局部估计，本质也是“把几何先验以轻量方式注入局部优化”。

4. **几何基础模型正在向“跨视角、跨坐标系、跨数据形态”扩展。**
   - X-VGGT 把地面图像与带地理参考的卫星图统一到一个场景级变换（重力、尺度、偏航、平移）中；Trainspotting 指出前馈重建模型在“found photos”（跨年份、跨环境、跨物理个体）上严重失效，并给出数据集与微调证据；MetricTrail 用冻结 DINOv3 特征增强对应估计。
   - 共同问题是：现有基础模型的训练分布（单次采集、局部坐标）与真实部署分布（多源、地理参考、开放档案）之间存在系统性 gap。

5. **神经场景表示与机器人/AR 应用的耦合在加深，且开始处理“动态交互”而非静态场景。**
   - MOMASPLAT 指出现有 NVS 示范增强假设静态场景，无法重渲染接触后被操作物体，因此分别重建静态场景与物体；Spatial-UMI-Dream 用度量深度把 UMI 的夹爪相机运动与物体运动解耦；4DPS 把可微渲染搬到毫米波雷达微多普勒域，直接服务人体感知数据合成；TactileLab 用光流式触觉流替代软体仿真。
   - 这些工作共同说明：**场景表示正在成为机器人数据引擎的一部分**，而不仅是可视化终端。

#### 技术路线观察

- **几何基础模型（Geometry Foundation Models）**：路线分化明显。X-VGGT 走“联合输入、统一变换参数化”的前馈统一路线；MetricTrail 走“复用成熟稀疏局部估计器 + 度量深度软约束 + 冻结大模型特征适配器”的模块化路线；Trainspotting 则从数据分布角度质疑现有前馈模型的泛化性，属于“先诊断再修”的路线。三者对“基础模型应该端到端还是模块化”给出了不同答案。

- **3D/4D 重建**：SM4RT 与 XM4D 代表两种哲学——前者是级联前馈、弱监督补标签稀疏；后者是分离优化、用 SDP 证书保证全局最优。InstantHand 把 4D 重建收缩到单图可动画 avatar 这一窄而实用的子问题，并用 Soft Alpha Band 与 Reliability-gated Appearance Transfer 处理轮廓泄漏和颜色漂移，说明**细分任务上的损失/正则设计仍有很大空间**。

- **神经场景表示与渲染**：3DGS 生态内部出现明显的“表示质量分层”——HIBS 改核函数形状与致密化策略，P-MGS 改高斯分配依据，AffineGS 改深度先验对齐方式，BudgetSplat 改压缩与预算控制。四者分别对应核、分配、先验、压缩四个正交维度，说明 3DGS 的改进已从“整体架构创新”进入**组件级精修阶段**。4DPS 则把 splatting 从可见光扩展到雷达距离-多普勒域，是表示迁移的有趣信号。

- **机器人/AR 应用**：MOMASPLAT、Spatial-UMI-Dream、TactileLab 的共同技术侧重点是**把仿真/重建中的几何与物理量显式化**（物体级重建、度量深度、触觉流场），以缩小 sim-to-real 或跨本体 gap。与纯视觉重建论文相比，这些工作更关心“合成数据是否保真到足以训练策略”，评估协议也更偏向任务成功率而非 PSNR。

#### 值得优先阅读的论文

1. **XM4D（2611.07902）**：在普遍追求前馈泛化的浪潮中，它提供了“可验证全局最优”的另一条路线，且两阶段 QCQP/SDP 的建模方式对做几何优化的人有直接方法论价值。优先读可判断其证书在实际噪声数据下是否仍然紧。

2. **AffineGS（2611.07709）**：它提出的“单目深度区域相关分段线性失真”如果成立，会直接影响大量用单目深度先验正则 3DGS 的工作，属于**可能改变默认假设**的论文。

3. **SM4RT（2611.08436）**：级联前馈 + 相机坐标系表达运动 + 弱监督补运动标签，是 4D 重建中较完整的技术组合，且评估覆盖 Kubric、Waymo、Point Odyssey 三个异质数据集，适合作为 4D 前馈路线的当前参照点。

4. **Trainspotting（2611.06849）**：它不是提出新模型，而是用 12,068 个物体、311,886 张 found photos 暴露前馈重建模型的失效模式，并给出微调可改善的证据。对做基础模型评测与数据分布研究的人优先级高。

5. **MOMASPLAT（2611.08372）**：把动态物体交互纳入新视角示范增强，问题定义清晰（接触后阶段未被增强），技术组合（3DGS + 前馈 3D 基础模型 + 运动学重定向）对做机器人数据合成的人有直接参考价值。

#### 可能的研究机会

- **前馈泛化与可验证优化的结合**：XM4D 的证书式优化能否作为前馈模型的“质检器”或初始化器？例如用 SDP 证书筛选前馈预测中几何不可信的子集，再局部精修。目前两篇论文各自独立，组合空间明显。

- **单目深度先验的失真建模向其他任务迁移**：AffineGS 发现的分段线性失真是否也影响 MetricTrail 的度量深度软约束、X-VGGT 的点图预测、Spatial-UMI-Dream 的立体深度？若成立，这些系统的深度对齐策略都需要重新审视。

- **动态场景表示的“物体级分离”标准化**：MOMASPLAT 分别重建静态场景与被操作物体，SM4RT 先结构后运动，二者都暗示“把动态物体从背景中显式分离”是提升 4D 质量的关键。可探索一个通用的物体级动态表示接口，服务于机器人示范增强、4D 重建与雷达/触觉等多模态渲染。

- **found photos / 开放档案数据上的基础模型鲁棒性**：Trainspotting 只做了诊断与微调验证，

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-06T14:57:26-05:00
**Total number of papers:** 49
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

### 2026-11

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

## Dynamic / 4D Reconstruction

### 2026-11

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

## 3D Reconstruction & Multi-view Geometry

### 2026-11

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

## Neural Scene Representations & Rendering

### 2026-11

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

## Embodied / Robotics / AR Applications

### 2026-11

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

#### 2026-11-03 - Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation

**Authors:** Mengjie Zhao, Yuxin Chen, Yiyang Shao, Chuye Hong, Jiakang Chen, Koushil Sreenath, Masayoshi Tomizuka
**Links:** [abs](https://arxiv.org/abs/2611.05507) - [pdf](https://arxiv.org/pdf/2611.05507)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation
- 作者：Mengjie Zhao, Yuxin Chen, Yiyang Shao, Chuye Hong, Jiakang Chen, Koushil Sreenath, Masayoshi Tomizuka
- 出版日期：2026-11-03T19:04:27Z
- 分类：Embodied / Robotics / AR Applications（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2611.05507) ｜ [PDF](https://arxiv.org/pdf/2611.05507)

### 一句话总结
论文提出 Ctrl-F，一个分层的人形机器人“运动—力”框架，通过在每个指定接触部位（如手或脚）上附加三维力指令，将运动跟踪扩展为可施加可控交互力的 loco-manipulation。

### 研究问题
现有的人形运动跟踪已能泛化复现多样的人类动作，但行为发生在自由空间：跟踪器只知道身体该在哪里，不知道应如何与环境交互。另一些工作把物体纳入目标，却把交互抽象为接触或几何，导致高难度交互情形研究不足。论文要解决的问题是：如何为运动模仿补充“施多大力”的指令通道，使机器人能在需要大且持续交互力的场景中完成 loco-manipulation。

### 核心思路/方法
- **核心主张**：力是连接运动模仿与物体交互的自然指令通道，不仅指定接触位置，还指定接触力度。
- **框架**：分层运动—力框架，为运动跟踪增加显式力指令，即在每个指定接触身体部位上的三维力。
  1. **统一运动—力控制器**：跟踪参考运动，同时向世界施加指令力。
  2. **高层力规划器**：基于物体状态与本体感知观测，在线给出力指令。
- **验证方式**：在仿真和硬件上完成需要大且持续交互力的 loco-manipulation，并在负载变化时在线调整指令；硬件上展示手部拖拽、推动、举升以及脚部踢击。

### 主要贡献
- 提出以“力”作为运动模仿与物体交互之间的显式命令接口，弥补自由空间运动跟踪与抽象接触/几何交互之间的空白。
- 设计分层运动—力框架，包含统一运动—力控制器与在线高层力规划器。
- 在仿真与硬件上展示需要大且持续交互力的 loco-manipulation，并能在线适应负载变化；硬件上成功推动和踢击最重 20kg 的箱子，而“无力感知”的基线失败。
- 展示手部拖拽、推动、举升与脚部踢击等多类接触操作。

### 局限性
- 摘要未提供足够信息说明方法在更广泛物体类别、接触部位或地形条件下的泛化能力。
- 摘要未提供足够信息说明力跟踪精度、控制器稳定性或失败案例的定量分析。
- 摘要未提供足够信息说明高层力规划器的具体输入表示、训练方式与在线计算开销。
- 摘要未提供足够信息说明仿真与硬件实验的完整设置、基线配置与评价指标细节。

### 阅读优先级
**高**。理由：论文直指人形运动跟踪从“自由空间运动”走向“带力交互”的关键缺口，提出明确的力指令接口与分层框架，并在硬件上给出 20kg 级推动/踢击及在线负载适应的结果；对关注人形 loco-manipulation、运动跟踪与力控制结合的研究者具有较高参考价值。

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
