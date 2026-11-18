# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：46
- 分类分布：
  - Embodied / Robotics / AR Applications: 17
  - 3D Reconstruction & Multi-view Geometry: 14
  - Neural Scene Representations & Rendering: 6
  - Dynamic / 4D Reconstruction: 6
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“渲染指标 ≠ 三维/度量正确性”成为多个子方向的共同反思。** 
 - 3DGS 分割方向：VODA 指出渲染掩码准确不代表三维选择完整，alpha 混合监督让遮挡/低贡献高斯欠监督，并引入 Removal-3D 与 RDE 评估体积完整性（2611.21383）。
 - 单目度量深度方向：*What the Averages Hide* 指出跨数据集平均指标掩盖逐图严重失败，剩余困难主要是尺度（2611.20518）。
 - 位姿估计方向：MomentPnP 针对无对应关系的盲 PnP，强调在不依赖显式对应的情况下获得位姿（2611.20797）。
 - 共同信号：评价体系从“平均/渲染层面好看”转向“逐图失败率、体积完整性、尺度偏差、无对应鲁棒性”等更贴近下游任务的指标。

2. **3DGS 从“能渲染”走向“可操作、可信任、可管理”。** 
 - 可信任/不确定性：QuantileGS 为 3DGS 新视角合成提供逐像素 RGB 误差上界与共形校准（2611.21253）。
 - 可操作/对象级：VODA 关注 Gaussian 分割的三维完整性（2611.21383）。
 - 可管理/系统效率：GDM-GS 把结构化 3DGS 轨迹渲染重构为空间数据管理问题，在视图内、跨视图、跨处理器三层去冗余（2611.20546）。
 - 这说明 3DGS 研究重心正从表示与渲染质量，扩展到分割监督、不确定性量化与系统级数据管理。

3. **动态/4D 重建强调“物理或几何约束 + 前馈效率”。** 
 - IGRecon4D 用实例先验蒸馏抑制动态目标泄漏到静态表示，并用 LiDAR 锚定高斯位置缓解跨视角几何漂移（2611.21126）。
 - Cosmos4D 用引力势与共享低维力场约束星系恒星运动，并按亮度分层建模（2611.20089）。
 - 两者都反对“自由形变拟合图像”的路线，转而引入领域约束（交通参与者先验、LiDAR、引力）来提升 4D 表示的物理/几何可信度。

4. **机器人/具身方向出现“数据规模化 + 架构模块化”的双线推进。** 
 - 数据规模化：WinDEX 面向野外第一人称双目视频，构建度量 3D 手部标注、端到端网络、蒸馏流式模型与低成本采集硬件（2611.21143）；AnyR2V 把路侧多模态观测转成七摄像头环视视频，用路侧数据扩充自动驾驶训练（2611.19830）；AsymEEF 用少量源演示迁移到异构双臂末端执行器（2611.20557）。
 - 架构模块化：EasyNav 以显式共享导航状态作为模块唯一接口，实现表示无关的 ROS2 导航框架（2611.19894）；视觉语言导航系统把 Grounding DINO、深度定位、语义建图与 Nav2 串成端到端 ROS2 系统（2611.20558）。
 - 共同点：不再只追求单点算法，而是围绕“数据飞轮”和“可替换模块/时序契约”构建系统。

5. **几何基础模型与经典几何方法并行回暖。** 
 - 几何基础模型被用于前馈 4D 驾驶重建（IGRecon4D，2611.21126）和单目度量深度评估（2611.20518）。
 - 同时，MomentPnP 用置换不变矩 + EM 的无学习路线在盲 PnP 上大幅降低旋转误差（2611.20797）；Polygraph 用位姿图、学习式图像检索、稀疏特征匹配与两级一致性门控实现在线多会话轨迹优化（2611.21163）。
 - 趋势不是“基础模型取代经典几何”，而是两者在鲁棒性、可解释性与在线效率上互补。

#### 技术路线观察

- **几何基础模型**：IGRecon4D 把实例级语义先验蒸馏进动态掩码学习，并用稀疏 LiDAR 引导稠密深度、反投影锚定高斯位置，体现“基础模型先验 + 传感器几何锚定”的组合路线。*What the Averages Hide* 则对 11 个近期架构做逐图失败分析，说明几何基础模型的评估正从平均指标转向失败模式与尺度归因。MomentPnP 代表另一极：不依赖学习，用矩匹配 + EM 处理无对应盲 PnP，强调可解释的几何初始化。

- **3D/4D 重建**：Polygraph 走“在线、逐关键帧/空间簇、不建 3D 地图”的位姿图路线，用学习式检索 + 稀疏匹配 + 两级门控保证跨会话边可靠；MomentPnP 解决无对应位姿初始化；IGRecon4D 与 Cosmos4D 分别把 4D 重建推向驾驶场景与天文场景，共同点是引入外部约束（LiDAR、引力）而非纯自由形变。WinDEX 则把度量 3D 手部重建与视觉惯性 SLAM 结合，服务遥操作与策略学习。

- **神经场景表示**：3DGS 相关论文分化为三条线：监督目标（VODA 的体素监督）、不确定性（QuantileGS 的共形误差上界）、系统效率（GDM-GS 的空间数据管理）。Cosmos4D 把 4D 高斯泼溅与引力约束结合，说明高斯表示正在向“带物理先验的动态表示”扩展。整体看，3DGS 的竞争点从渲染保真度转向三维完整性、可靠性保证与轨迹级效率。

- **机器人/AR 应用**：WinDEX、AsymEEF、AnyR2V 关注数据采集与跨形态/跨视角复用，目标都是降低具身数据成本；EasyNav、视觉语言导航系统、Polygraph 关注系统架构与在线运行；Radar Panoptic Transformer 则在稀疏雷达点云上做全景分割，服务动态场景理解。应用侧的技术侧重是“可部署性”：时序契约、实时推理、低成本硬件、仿真验证与真实机器人实验。

- **触觉与感知补充**：非成像光学触觉传感器综述（2611.20770）提出把机械载荷、光学编码、读出与触觉推断统一到机器人任务需求的框架，提示具身感知不只依赖视觉，触觉传感的“可辨识性 + 反馈时序”是另一条评估主线。

#### 值得优先阅读的论文

1. **The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation（2611.21383）** 
 优先理由：直接挑战 3DGS 分割中“渲染掩码即对象”的隐含假设，提出即插即用监督目标与新基准/指标，对对象级 3DGS 编辑、移除、操作等下游任务影响面大。

2. **What the Averages Hide: Monocular Metric Depth Models Still Fail in Everyday Scenes, Mostly on Scale（2611.20518）** 
 优先理由：对 11 个架构、18 个模型评估、7 个基准 4,406 张图做逐图失败分析，结论“剩余困难主要是尺度”对单目度量深度、SLAM、机器人导航都有直接参考价值，且方法论可迁移到其他感知任务评估。

3. **Polygraph: Large-Scale Multi-Session Trajectory Optimization using Pose Graphs（2611.21163）** 
 优先理由：在线多会话轨迹优化是机器人/AR 长期建图的现实问题，论文明确处理“不建 3D 地图、逐关键帧/空间簇、两级一致性门控”，工程与系统参考价值高。

4. **QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting（2611.21253）** 
 优先理由：把共形校准引入 3DGS 渲染误差上界，补足“新视角可靠性”

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-18T16:26:10-05:00
**Total number of papers:** 52
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

#### 2026-11-17 - Refin3R: Geometry-Guided Refinement for Feed-Forward 3D Reconstruction

**Authors:** Jongmin Lee, Jaeyeong Kim, Seungryong Kim
**Links:** [abs](https://arxiv.org/abs/2611.23051) - [pdf](https://arxiv.org/pdf/2611.23051)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** point map, feed-forward 3D reconstruction, 3D reconstruction, structure from motion, SfM

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models predict dense point maps from multiple images in a single pass. Without explicit geometric constraints, however, their predictions are often inconsistent across views and lack fine-grained precision. Recent methods incorporate geometric priors such as camera pose or depth, but use them merely as auxiliary inputs, process each view independently, or refine the geometry only where the priors are available. We present Refin3R, which refines feed-forward point maps with Structure-from-Motion (SfM) points, propagating SfM geometry over the image grid. In its dual-branch architecture, a 2D branch extends SfM geometry beyond its coverage using geometry-aware backbone features, while a 3D branch reasons over the SfM points of all views, capturing multi-view structure that the image grid alone cannot represent. The two branches exchange information bidirectionally to jointly refine each view, yielding dense and accurate point maps. Across ScanNet++, ETH3D, Tanks\&Temples, and out-of-domain human and surgical scenes, Refin3R consistently outperforms feed-forward and geometry-guided methods in point map accuracy while running faster than the strongest geometry-guided baseline.

</details>

#### 2026-11-16 - IGRecon4D: Dynamic-Object-Aware Feed-Forward Reconstruction of Driving Scenes

**Authors:** Yifei Tong, Ziyang Huang, Yizhao Han, Xiaoxiao Long, Hao Zhu
**Links:** [abs](https://arxiv.org/abs/2611.21126) - [pdf](https://arxiv.org/pdf/2611.21126)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** feed-forward reconstruction, dynamic scene reconstruction, scene reconstruction, depth estimation, autonomous driving, driving scene, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IGRecon4D: Dynamic-Object-Aware Feed-Forward Reconstruction of Driving Scenes
- 作者：Yifei Tong, Ziyang Huang, Yizhao Han, Xiaoxiao Long, Hao Zhu
- 出版日期：2026-11-16T14:05:54Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.21126)｜[PDF](https://arxiv.org/pdf/2611.21126)

### 一句话总结
IGRecon4D 是一个前馈式 4D 驾驶场景重建框架，通过训练时实例先验蒸馏与 LiDAR 锚定的高斯定位，来缓解动态交通参与者语义泄漏到静态表示、以及高斯位置跨视角几何漂移这两类问题。

### 研究问题
论文针对当前前馈式 4D 驾驶场景重建中的两个互补失效模式：
1. **语义泄漏**：交通参与者被泄漏进静态表示中；
2. **几何漂移**：高斯位置在不同视角之间发生漂移。
摘要强调，这些问题会影响动态自动驾驶场景的高效建模与重建质量。

### 核心思路/方法
论文提出 IGRecon4D，主要包括两条技术路径：
1. **训练时实例先验蒸馏**：使用实例级语义分支提供“可能为动态参与者”的先验，并通过 Instance-Dynamic Consistency Constraint 将其蒸馏到动态掩码学习中，以鼓励对易发生动态-静态泄漏的交通参与者区域进行高召回定位。
2. **LiDAR 锚定的高斯定位**：利用稀疏 LiDAR 测量引导稠密深度估计，并将得到的深度反投影以锚定高斯位置，从而提升多视角几何一致性。

### 主要贡献
1. 提出 IGRecon4D 前馈式动态场景重建框架，明确面向动态交通参与者语义泄漏与高斯位置跨视角漂移两类失效模式。
2. 引入实例级语义先验蒸馏与 Instance-Dynamic Consistency Constraint，用于动态掩码学习并提升交通参与者区域定位召回。
3. 使用稀疏 LiDAR 引导稠密深度估计，并通过深度反投影锚定高斯位置，以改善多视角几何一致性。
4. 在 Waymo Open Dataset 上实验，并在 nuScenes 上做零样本评估；摘要报告主基准全图重建有所提升，跨数据集评估下交通参与者区域重建更强。

### 局限性
- 摘要未提供足够信息说明计算开销、推理速度或实时性表现。
- 摘要未提供足够信息说明对 LiDAR 稀疏度、标定误差或缺失 LiDAR 条件的敏感性。
- 摘要未提供足够信息给出具体量化指标、消融实验细节及各模块的独立贡献幅度。
- 摘要未提供足够信息说明失败案例、极端场景表现或与其他方法的完整对比范围。
- 摘要未提供足够信息说明实例级语义分支的来源、训练依赖及泛化边界。

### 阅读优先级
**中**
理由：该论文问题定义清晰，针对前馈 4D 驾驶场景重建中的动态-静态泄漏与多视角几何漂移提出对应机制，并在 Waymo 与 nuScenes 零样本设置下评估，适合关注驾驶场景重建、动态对象感知与多视角几何一致性的读者。但摘要未给出量化结果、消融细节与效率信息，是否构成显著方法突破需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 4D driving-scene reconstruction enables efficient modeling of dynamic autonomous-driving scenes, but current methods suffer from two complementary failure modes: semantic leakage of traffic participants into the static representation and geometric drift of Gaussian locations across viewpoints. We propose \textbf{IGRecon4D}, a feed-forward dynamic scene reconstruction framework that addresses these failures with training-time instance-prior distillation and LiDAR-anchored Gaussian positioning. Specifically, an instance-level semantic branch provides a potentially dynamic participant prior, which is distilled into dynamic-mask learning through the Instance-Dynamic Consistency Constraint to encourage high-recall localization of traffic-participant regions prone to dynamic-static leakage. In parallel, sparse LiDAR measurements guide dense depth estimation, and the resulting depths are back-projected to anchor Gaussian positions for improved multi-view geometric consistency. Experiments on the Waymo Open Dataset and zero-shot evaluation on nuScenes demonstrate improved full-image reconstruction on the main benchmark and stronger traffic-participant-region reconstruction under cross-dataset evaluation.

</details>

#### 2026-11-16 - What the Averages Hide: Monocular Metric Depth Models Still Fail in Everyday Scenes, Mostly on Scale

**Authors:** Hualie Jiang, Yujie Luo, Ziyang Song, Ximeng Li, Zhiqiang Lou, Rui Xu
**Links:** [abs](https://arxiv.org/abs/2611.20518) - [pdf](https://arxiv.org/pdf/2611.20518)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：What the Averages Hide: Monocular Metric Depth Models Still Fail in Everyday Scenes, Mostly on Scale
- 作者：Hualie Jiang, Yujie Luo, Ziyang Song, Ximeng Li, Zhiqiang Lou, Rui Xu
- 出版日期：2026-11-16T04:44:13Z
- 分类：Geometry Foundation Models
- 链接：[摘要](https://arxiv.org/abs/2611.20518) / [PDF](https://arxiv.org/pdf/2611.20518)

### 一句话总结
论文指出，平均指标会掩盖单目度量深度模型在日常场景中的严重失败；基于逐图结果的分析表明，剩余困难主要来自尺度，结构问题相对较少。

### 研究问题
现有零样本单目度量深度模型通常通过跨数据集平均的度量指标和尺度对齐指标来评估，这种平均方式无法揭示：仍有多少图像存在严重错误的度量深度、深度被低估还是高估，以及不同模型是否在相同图像上失败。论文旨在回答这些问题，尤其关注日常场景中度量深度估计是否真正解决，以及失败主要源于结构还是尺度。

### 核心思路/方法
论文提出一套基于逐图结果的评估框架，包括：
- 失败率：以度量 δ₁ < 0.5 定义严重失败；
- 结构评估：使用尺度对齐后的指标；
- 尺度评估：分析对齐尺度的偏差、离散度和绝对误差；
- 跨模型比较：区分共享失败与模型特定失败。

作者将该框架应用于 11 个近期架构，在有和无真值内参两种条件下共 18 个模型评估，使用 MoGe-2 所用的 7 个日常场景基准，共 4,406 张图像。

### 主要贡献
- 揭示平均指标会隐藏严重的逐图失败，指出日常场景中的度量深度估计尚未解决，剩余困难主要是尺度。
- 报告最佳评估仍有 7.7% 的失败率；在所有失败中，78.8% 的结构完整，经尺度校正后 98.3% 不再失败。
- 发现至少 6 个架构共同失败的图像占数据 7.3%，集中在 HAMMER 和 DIODE；这些图像在其他家族架构选择下仍占前 6 模型 34%–40% 的误差，而随机图像仅占 14%–18%。
- 发现加入物体可降低多数模型的尺度误差；真值内参和多数家族中更大的模型能减少失败但不能消除失败。
- 建议分别报告失败率、结构和尺度，并按失败模型数量分层报告结果；将发布代码、带共享失败标签的逐图结果，以及两个基于 TUM RGB-D 的诊断集。

### 局限性
摘要未提供足够信息说明方法在非日常场景、其他数据集分布或实时应用中的表现；也未提供各模型的具体架构细节、计算成本、训练数据影响及失败原因的深入归因。摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接质疑常用平均评估的可靠性，提出逐图失败率与尺度分解视角，并给出跨模型共享失败分析，对单目度量深度评测和模型选择具有较强警示意义；摘要信息集中且结论明确。

</details>

<details>
<summary>Abstract</summary>

Zero-shot monocular metric depth models are evaluated by averaging metric and scale-aligned scores across datasets. Averages cannot show how many images still have severely wrong metric depth, whether depth is under- or overestimated, or whether different models fail on the same images. We propose an evaluation built on per-image results: the failure rate (metric $δ_1$ < 0.5); scale-aligned metrics for structure, and the bias, dispersion and absolute error of the alignment scale for scale; and a cross-model comparison that separates shared from model-specific failures. We apply it to 11 recent architectures with and without ground-truth intrinsics (18 model evaluations) on the 7 everyday-scene benchmarks (4,406 images) used by MoGe-2. Metric depth estimation is not solved in everyday scenes, and the remaining difficulty is mainly scale: the best of the 18 evaluations still has a failure rate of 7.7% (datasets weighted equally); pooled over all failures, 78.8% have intact structure, and after scale correction 98.3% no longer fail. Images failed by at least 6 architectures make up 7.3% of the data, concentrated on HAMMER and DIODE; even when selected only by architectures of other families, they hold 34% to 40% of the error of the top 6 models, against 14% to 18% for as many random images from the same datasets. Adding objects reduces the scale error of most models; ground-truth intrinsics and, in most families, larger models reduce the failures but do not remove them. We recommend reporting failure rates, structure and scale separately, and results stratified by how many models fail. We will release the code, the per-image results with shared-failure labels, and two diagnostic sets built from TUM RGB-D.

</details>

#### 2026-11-12 - Kosmo-GFM: A Production-Ready Geometry Foundation Model

**Authors:** Sheng Tang, Shengzhe Wei, Tiancheng Chen, Wenhua Jin, Xinyang Lu, Tinghao Jiang, Shuoxuan Feng, Yupeng Liu, Yu Zhang, Xingshuo Chang, Keren Zhou, Yuhan Xiong, Jiahao Li, Haoming Liu, Jituo Tian, Hui Liang, Chaoqun Tang, Feng Tian, Wentao Ouyang, Kaojin Zhu, Xiaolin Chai, Peihuang Fu, Miao Zheng, Yunbo Hu, Feixue Cai, Zizhen Zou, Weigang Wang, Yexuan Yang, Haoyu Feng, Weiqi Zhang, Juntong Fang, Zesong Li
**Links:** [abs](https://arxiv.org/abs/2611.16840) - [pdf](https://arxiv.org/pdf/2611.16840)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Dynamic / 4D Reconstruction, Neural Scene Representations & Rendering
**Matched keywords:** geometry foundation model, dynamic 3D, scene flow, 4D Gaussian, scene reconstruction, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Kosmo-GFM: A Production-Ready Geometry Foundation Model
- 作者：Sheng Tang, Shengzhe Wei, Tiancheng Chen, Wenhua Jin, Xinyang Lu, Tinghao Jiang, Shuoxuan Feng, Yupeng Liu, Yu Zhang, Xingshuo Chang, Keren Zhou, Yuhan Xiong, Jiahao Li, Haoming Liu, Jituo Tian, Hui Liang, Chaoqun Tang, Feng Tian, Wentao Ouyang, Kaojin Zhu, Xiaolin Chai, Peihuang Fu, Miao Zheng, Yunbo Hu, Feixue Cai, Zizhen Zou, Weigang Wang, Yexuan Yang, Haoyu Feng, Weiqi Zhang, Juntong Fang, Zesong Li
- 出版日期：2026-11-12T14:17:22Z
- 分类：Geometry Foundation Models；Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.16840) / [PDF](https://arxiv.org/pdf/2611.16840)

### 一句话总结
Kosmo-GFM 是一个面向生产场景重建的系统，将几何基础模型（GFM）、位姿优化引擎（PoseEngine）和来自 KosmoWorld 的重建监督结合起来，以提升相机参数、深度、跨视图对应和动态 3D 点预测，并服务于下游 3D/4D Gaussian Splatting。

### 研究问题
论文关注的是场景级重建中如何利用学习到的几何先验：GFM 需要从图像和视频预测相机参数、深度、跨视图对应关系和动态 3D 点；PoseEngine 需要把这些预测与几何优化结合，恢复场景级相机位姿与几何；KosmoWorld 则要从重建的真实场景生成图像和几何监督，以改进 GFM 的几何预测。摘要未提供足够信息说明具体失败模式或问题定义细节。

### 核心思路/方法
系统由三部分组成。第一，GFM 从图像和视频中预测相机参数、深度、跨视图对应关系和动态 3D 点。第二，PoseEngine 将这些预测与几何优化相结合，恢复场景级相机位姿和几何，供下游 3D 与 4D Gaussian Splatting 使用。第三，KosmoWorld 从重建的真实世界场景生成图像与几何监督，用于提升 GFM 的几何预测。此外，PoseEngine Flash 提供了进一步的精度—效率权衡，并报告了混合精度运行时间。摘要还提到独立扩展实验显示，随着数据、模型计算和训练预算增加，总体趋势较为有利。

### 主要贡献
- 提出 Kosmo-GFM 场景重建系统，整合 GFM、PoseEngine 与 KosmoWorld 的重建派生监督。
- GFM 在 SpatialBench 的 Sparse 和 Medium 子集上，相比所比较方法取得最低绝对相对深度误差和最高 5 度相对位姿 AUC。
- 在五个评估数据集上，GFM 取得最低的动态点与场景流平均端点误差。
- 在全部比较重建系统均完成的 34 个场景上，PoseEngine 在 1、3、5 度阈值下取得最高场景平均位姿 AUC，累计运行时间 14.07 小时，约为 GLUEMAP 69.67 小时的 20%。
- PoseEngine Flash 测得混合精度运行时间 2.62 小时，约为 GLUEMAP 运行时间的 4%。
- 扩展实验显示，随着数据、模型计算和训练预算增加，总体趋势较为有利。

### 局限性
摘要未提供足够信息说明失败场景、精度上限、对特定数据分布的依赖、PoseEngine Flash 的精度代价细节，以及各数据集和场景规模的具体范围。摘要未提供足够信息说明系统在极端稀疏视图、强动态场景或生产部署条件下的限制。

### 阅读优先级
中。理由：论文涉及几何基础模型、场景级位姿优化和 3D/4D 重建的完整系统，并给出了与 GLUEMAP 的运行时间和位姿 AUC 对比，以及深度、位姿、动态点和场景流指标；对关注几何基础模型与生产级重建流水线的读者有参考价值。但摘要未展开方法细节、失败案例和完整实验设置，是否精读取决于对 PoseEngine、KosmoWorld 监督机制或 3D/4D Gaussian Splatting 下游流程的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

We present Kosmo-GFM, a scene reconstruction system that integrates a geometry foundation model (GFM), a pose optimization engine (PoseEngine), and reconstruction-derived supervision from KosmoWorld. GFM predicts camera parameters, depth, cross-view correspondences, and dynamic 3D points from images and videos. PoseEngine combines these predictions with geometric optimization to recover scene-level camera poses and geometry for downstream 3D and 4D Gaussian Splatting. KosmoWorld generates images and geometric supervision from reconstructed real-world scenes to improve GFM's geometric predictions. On the Sparse and Medium subsets of SpatialBench, GFM achieves the lowest absolute relative depth error and the highest relative-pose AUC at 5 degrees among the compared methods. It also achieves the lowest mean endpoint errors for dynamic points and scene flow across the five evaluated datasets. Across 34 scenes completed by all compared reconstruction systems, PoseEngine achieves the highest scene-averaged pose AUC at thresholds of 1, 3, and 5 degrees, with a cumulative runtime of 14.07 hours, approximately 20% of GLUEMAP's 69.67 hours. PoseEngine Flash provides a further accuracy-efficiency trade-off, with a measured mixed-precision runtime of 2.62 hours, approximately 4% of GLUEMAP's runtime. Separate scaling experiments show generally favorable trends with increased data, model computation, and training budgets. These results support the use of learned geometric priors within a scene-level reconstruction pipeline.

</details>

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-17 - ARG-Avatar: Animation-Rendering Guidance for Efficient Feedforward Avatar Reconstruction

**Authors:** Jianjin Xu, Soham Dasgupta, Fernando De la Torre
**Links:** [abs](https://arxiv.org/abs/2611.22207) - [pdf](https://arxiv.org/pdf/2611.22207)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** avatar reconstruction, rendering, augmented reality

<details>
<summary>Abstract</summary>

Reconstructing animatable 3D human avatars from images is important for applications such as gaming and augmented reality. Feedforward methods make avatar reconstruction accessible by reducing inference time to a few seconds, but recent approaches rely heavily on scaling model capacity, training data, and computation. We ask whether such scaling is necessary. To this end, we introduce ARG-Avatar, an efficient feedforward framework with only 68M trainable parameters that achieves SOTA reconstruction quality. Our key insight is that 3D animation and rendering already provide strong geometric correspondences that existing methods largely attempt to learn from data. In light of this, we design the Foreground Avatar Coordinate RoPE attention (FACRoPE) and Intermediate Token Rendering (ITR) pipeline to guide avatar tokens to attend to their corresponding patches. Experiments across multiple datasets show that ARG-Avatar consistently outperforms prior methods when using two or more input images. Compared with LHM++, ARG-Avatar uses approximately 9$\times$ fewer trainable parameters, 4.8$\times$ fewer training sequences, and 14$\times$ less training compute, while running 6$\times$ faster and achieving a 2.7 dB PSNR improvement on the out-of-distribution NeuMan benchmark.

</details>

#### 2026-11-17 - VTT: Reading Vehicle Size and Powertrain Type from Motion Trajectory Across Unseen Car Models

**Authors:** Yuhang Wang, Yuechen Guo, Jingxin Yang, Chuheng Wei, Suyang Chen, Abdulaziz Alhuraish, Yiyi Wang, Mingyang Ban, Jingran Sun, Hao Zhou
**Links:** [abs](https://arxiv.org/abs/2611.22109) - [pdf](https://arxiv.org/pdf/2611.22109)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion trajectory, simulation

<details>
<summary>Abstract</summary>

Vehicle size and powertrain information can enrich trajectory data for traffic analysis and simulation. We present VTT, a dataset and benchmark for identifying these attributes from motion and controller area network (CAN) signals across unseen car models. The dataset contains 9,062 drives, about 3,950 h, from 1,431 vehicles and 174 car models. It provides three footprint-based size classes, powertrain labels, and evaluation on unseen car models and unseen drivers. Using 60-s windows, we compare four sequence architectures, statistical features and physical features proposed by large language models. Training with auxiliary physical targets, data augmentation and task-specific weighting raises drive-level macro-F1 to 92.6-93.0% for battery-electric versus combustion vehicles and from 62.9% to 67.1% for size classification. On public logs from 4,061 additional drivers, the full-input model identifies powertrain correctly for 86 of 88 car models; size accuracy is 63.2%, close to the internal vehicle-level result of 63.5%. Physical-feature analysis links powertrain recognition to deceleration behaviour and size recognition to steering response. Errors near size-class boundaries and limited gains from longer observations highlight the importance of label resolution and training-fleet coverage for cross-model generalisation.

</details>

#### 2026-11-17 - CueSplat: Learning to Schedule Sparse Deformation for Dynamic Gaussian Splatting on Edge Devices

**Authors:** Qingyuan Tang, He Zhu, Shixuan Sun, Anbang Wu, Jingwen Leng, Minyi Guo, Yu Feng
**Links:** [abs](https://arxiv.org/abs/2611.22095) - [pdf](https://arxiv.org/pdf/2611.22095)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Deformation-based 4D Gaussian splatting (4DGS) enables dynamic scene rendering. However, evaluating deformation networks for all Gaussians at every frame is compute-intensive on edge devices. We find that Gaussian trajectories are often locally predictable, yet prediction reliability varies across Gaussians and time. Thus, we propose CueSplat, a post-training framework that exploits local temporal regularity while keeping the pretrained backbone frozen and retaining its Gaussian set. Specifically, CueSplat predicts Gaussian attributes from recent history and uses a lightweight learned router to select exact deformation updates within a scene-specific budget calibrated offline. Selection accounts for prediction reliability and rendering contribution. Selected indices are reused across nearby frames to reduce routing overhead, while selected Gaussians still receive exact updates each frame. To control accumulated prediction error, we use drift signals to schedule three consecutive full-deformation frames that rebuild the prediction history. Evaluated across four mainstream 4DGS algorithms, CueSplat achieves up to $6.74\times$ and $8.15\times$ speedups on Jetson AGX Orin and Orin NX, respectively, with a negligible quality drop (at most $0.16$ dB in dataset-average PSNR).

</details>

#### 2026-11-16 - WinDEX: Metric 3D Hand Motion Reconstruction in the Wild for Dexterous Teleoperation and Policy Learning

**Authors:** Hongyu Ma, Hairong Qu, Shiqi Zhao, Yongsong Yang, Kai Shi, Jiahao Ai, Xin You, Peng Yin
**Links:** [abs](https://arxiv.org/abs/2611.21143) - [pdf](https://arxiv.org/pdf/2611.21143)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion reconstruction, SLAM, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WinDEX: Metric 3D Hand Motion Reconstruction in the Wild for Dexterous Teleoperation and Policy Learning
- 作者：Hongyu Ma, Hairong Qu, Shiqi Zhao, Yongsong Yang, Kai Shi, Jiahao Ai, Xin You, Peng Yin
- 出版日期：2026-11-16T14:14:54Z
- 分类：Dynamic / 4D Reconstruction（主分类；无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2611.21143)｜[PDF](https://arxiv.org/pdf/2611.21143)

### 一句话总结
WinDEX 面向野外第一人称双目视频，构建从度量尺度 3D 手部标注、端到端重建网络到蒸馏流式模型与低成本采集硬件的完整系统，用于灵巧遥操作与强化学习策略训练。

### 研究问题
摘要指出，人类操作数据常用于训练机器人实现类人灵巧性，但低成本、大规模“in the wild”采集仍然困难；现有方法在以下方面存在局限：具有几何依据的度量尺度重建、真实世界泛化能力以及推理速度。论文即针对这三点展开。

### 核心思路/方法
摘要给出的方法组成包括：
1. **几何-时间优化标注**：从野外第一人称双目视频生成度量 3D 手部标注，并结合视觉-惯性 SLAM 进行世界坐标系重建。
2. **WinDEX-Net**：端到端、原生支持鱼眼镜头的网络，融合已标定双目、局部细节与时间上下文；配套“数据-模型飞轮”，即模型辅助标注与再训练。
3. **蒸馏模型**：分别支持离线重建与因果流式推理，服务于强化学习与遥操作。
4. **采集硬件与数据集**：低成本 CyberCap 双目-惯性采集设备，形成 WinDEX-Hand 数据集，包含 1,000 小时训练标注，以及留出的人工标注野外 2D 评测集和独立光学动捕评测集。
摘要报告离线重建 43.61 FPS、因果流式 171 FPS；留出数据上离线重建重投影误差 14.5 像素，结合视觉-惯性里程计的世界坐标系关节误差 37.29 mm；相较以 WiLoR 和 HaWoR 运动参考训练的强化学习策略，任务成功率分别为其 7.6 倍和 3.6 倍，并展示实时手臂-手部遥操作。

### 主要贡献
- 提出面向野外第一人称双目视频的度量尺度 3D 手部运动重建系统 WinDEX，整合几何-时间优化与视觉-惯性 SLAM 的世界坐标系重建。
- 提出鱼眼原生的端到端网络 WinDEX-Net，并设计模型辅助标注与再训练的数据-模型飞轮。
- 提供面向离线重建与因果流式的蒸馏模型，支撑强化学习与实时遥操作。
- 构建低成本 CyberCap 双目-惯性采集方案与 WinDEX-Hand 数据集（1,000 小时训练标注及两类留出评测集）。
- 摘要报告了推理速度、留出集精度及下游强化学习任务成功率方面的量化结果。

### 局限性
- 摘要未提供足够信息说明方法在非鱼眼相机、不同硬件配置或极端野外场景下的泛化边界。
- 摘要未提供足够信息说明 CyberCap 的具体成本、佩戴方式与采集舒适性。
- 摘要未提供足够信息说明 1,000 小时训练标注中模型辅助标注与人工标注的比例及质量控制细节。
- 摘要未提供足够信息说明遥操作实验的规模、受试者数量与用户研究结果。
- 摘要未提供足够信息说明与更多基线方法的系统对比及消融实验细节。
- 摘要未提供足够信息说明失败案例、计算资源需求与训练成本。

### 阅读优先级
**高**。理由：该工作同时覆盖度量 3D 手部重建、野外数据采集、实时流式推理与下游灵巧操作策略学习，且摘要给出了明确的精度、速度与任务成功率指标；对动态/4D 重建、遥操作与机器人策略学习方向具有直接参考价值。是否精读全文可结合对鱼眼双目、视觉-惯性 SLAM 或强化学习数据管线具体细节的兴趣决定。

</details>

<details>
<summary>Abstract</summary>

Human manipulation data are widely used to train robots for human-like dexterity. However, low-cost, large-scale collection in the wild remains challenging. Existing methods remain limited in geometrically grounded metric-scale reconstruction, real-world generalization and inference speed. We present WinDEX, integrating (1) geometric-temporal optimization for metric 3D hand annotation from in-the-wild egocentric stereo videos, combined with visual-inertial SLAM for world-frame reconstruction; (2) WinDEX-Net, an end-to-end, fisheye-native network combining calibrated stereo, local detail and temporal context, with a data-model flywheel of model-assisted annotation and retraining; (3) distilled models for offline reconstruction and causal streaming, supporting reinforcement learning and teleoperation; and (4) low-cost CyberCap stereo-inertial capture, forming the WinDEX-Hand dataset with 1,000 hours of training annotations and held-out human-annotated in-the-wild 2D and independent optical motion-capture evaluation sets. Offline reconstruction runs at 43.61 FPS and causal streaming at 171 FPS. On held-out data, offline reconstruction achieves state-of-the-art accuracy: 14.5 pixels in-the-wild reprojection error and, with visual-inertial odometry, 37.29 mm world-frame joint error. We achieve 7.6 and 3.6 times the task success rates of reinforcement learning policies trained with WiLoR and HaWoR motion references, respectively, and demonstrate real-time arm-hand teleoperation. Project website: https://fruitrabbit.github.io/WinDEX/.

</details>

#### 2026-11-15 - See the Lives of Stars in a Handful of Light

**Authors:** Shuhong Liu, Gengjia Chang, Quanfeng Xu, Ziteng Cui, Qianyu Zhou, Xiaoyu Dong, Lin Gu, Tatsuya Harada
**Links:** [abs](https://arxiv.org/abs/2611.20089) - [pdf](https://arxiv.org/pdf/2611.20089)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：See the Lives of Stars in a Handful of Light
- 作者：Shuhong Liu, Gengjia Chang, Quanfeng Xu, Ziteng Cui, Qianyu Zhou, Xiaoyu Dong, Lin Gu, Tatsuya Harada
- 出版日期：2026-11-15T16:05:51Z
- 分类：Dynamic / 4D Reconstruction（次要：Neural Scene Representations & Rendering）
- 链接：[摘要](https://arxiv.org/abs/2611.20089) | [PDF](https://arxiv.org/pdf/2611.20089)

### 一句话总结
论文提出 Cosmos4D，用引力约束的 4D 高斯泼溅，以及按亮度分层的动力学建模、由模拟多视角图像重建星系演化，并以八个星系构建 4D 数据集验证其在光度质量与物理准确性上优于动态高斯基线。

### 研究问题
论文关注能否从星系的多视角图像中在四维（空间+时间）上重建星系演化。摘要指出该设定对现有动态场景方法构成挑战：数百万恒星每颗仅覆盖少量像素，暗淡星群融入弥散光中，且自由形变虽能复现图像却不遵循引力。

### 核心思路/方法
Cosmos4D 包含两个核心组件：
1. **Gravitational 4D Gaussian Splatting**：将每颗恒星表示为自发光高斯，其运动通过引力势与所有恒星共享的低维力场进行积分。
2. **Luminosity-stratified dynamics**：亮星获得跨图像尺度监督的个体轨道；暗星群体则由从光流估计的速度场带动。

此外，论文从四个宇宙学模拟中构建了包含八个星系的 4D 数据集。

### 主要贡献
- 提出 Cosmos4D 方法，将引力势与共享低维力场引入 4D 高斯泼溅，以约束星系中恒星的运动。
- 提出按亮度分层的动力学建模策略，分别处理亮星的个体轨道与暗星群体的速度场。
- 构建了来自四个宇宙学模拟、包含八个星系的 4D 数据集。
- 摘要称在该数据集上，Cosmos4D 在光度质量与物理准确性两方面均优于动态高斯基线，并可在九十六帧中呈现星系八亿年的生命历程。

### 局限性
- 摘要未提供足够信息说明方法在真实观测数据上的适用性；所述数据均来自宇宙学模拟。
- 摘要未提供足够信息说明计算开销、训练时间或内存需求。
- 摘要未提供足够信息说明对暗星速度场估计误差的敏感性与失败情形。
- 摘要未提供足够信息说明数据集中星系类型、分辨率、帧数设置及评测指标的完整细节。
- 摘要未提供足够信息说明与更多非高斯类动态重建方法的比较。

### 阅读优先级
**中**。理由：该论文将 4D 重建与物理约束（引力、力场）结合，并针对极稀疏、暗弱星群提出分层动力学设计，问题设定与方法组合具有新意；同时构建了多模拟来源的 4D 星系数据集，对动态场景重建与神经场景表示方向有参考价值。但摘要未给出真实数据验证、计算成本与完整评测细节，是否值得优先精读取决于读者对物理约束 4D 重建或天文模拟数据的兴趣。

</details>

<details>
<summary>Abstract</summary>

Galaxies evolve over hundreds of millions of years, and no telescope has ever watched one move. Cosmological simulations make this evolution visible as a sequence of multi-view images, inviting the question of whether a galaxy can be recovered in four dimensions from its images. This setting defeats existing dynamic scene methods, since millions of stars span only a few pixels each, faint populations blend into diffuse light, and free deformations reproduce the images without obeying gravity. We present Cosmos4D, which rests on two components. Gravitational 4D Gaussian Splatting represents each star as a self-luminous Gaussian whose motion is integrated through a gravitational potential and a low-dimensional force field shared by all stars. Luminosity-stratified dynamics give bright stars individual orbits supervised across image scales and carry faint populations with a velocity field estimated from optical flow. We further build a 4D dataset of eight galaxies from four cosmological simulations, on which Cosmos4D outperforms dynamic Gaussian baselines in both photometric quality and physical accuracy. With these advancements, we glimpse eight hundred million years of a galaxy's life in ninety-six frames.

</details>

#### 2026-11-15 - Spatiotemporal Reconstruction of Auroral Precipitations with Neural Fields

**Authors:** Nazar Misyats, Mizuki Fukizawa, Yoshimasa Tanaka, Satoshi Ikehata
**Links:** [abs](https://arxiv.org/abs/2611.19757) - [pdf](https://arxiv.org/pdf/2611.19757)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** spatiotemporal reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatiotemporal Reconstruction of Auroral Precipitations with Neural Fields
- 作者：Nazar Misyats, Mizuki Fukizawa, Yoshimasa Tanaka, Satoshi Ikehata
- 出版日期：2026-11-15T03:38:35Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要页 https://arxiv.org/abs/2611.19757 ；PDF https://arxiv.org/pdf/2611.19757

### 一句话总结
该论文提出用带时间条件的神经网络建模动态极光电子 precipitation 场，从地面相机极光图像中重建随时间变化的电子能量谱空间分布，并在合成动态序列与真实多视角极光视频上评估。

### 研究问题
极光提供了对沉降到高层大气的高能电子的远程光学观测，其能量分布编码了大规模磁层过程的关键信息。但从地面极光相机图像反演 underlying electron precipitation field 是一个具有挑战性的逆问题。摘要指出，现有极光层析技术常受限于简化的静态设定、离散的空间与能量网格，或对电子能谱的强假设。论文要解决的是：如何在动态、连续且较少依赖能谱强假设的条件下，从极光图像重建时空变化的电子 precipitation 场。

### 核心思路/方法
论文提出用时间条件神经网络建模动态极光电子 precipitation 场。具体而言：
- 每一帧的 precipitation 场状态由一个 per-frame latent code 表示；
- 这些 latent code 由学习到的离散动力学驱动；
- 一个共享解码器将水平位置与 latent state 映射为电子能量谱；
- 预测的通量被转换为多波长体积发射率，并在考虑 delayed emissions 的情况下渲染为相机图像；
- 在合成动态极光序列和真实多视角极光视频上评估，展示所提出表示能产生时间连贯的 precipitation 重建，且图像投影与观测一致。

### 主要贡献
- 提出一种基于时间条件神经网络、由逐帧隐编码和学习到的离散动力学驱动的动态极光电子 precipitation 场建模方法。
- 使用共享解码器从水平位置和隐状态映射到电子能量谱，避免摘要中所述现有方法对离散空间/能量网格或强能谱假设的依赖。
- 将预测通量转换为多波长体积发射率，并考虑延迟发射渲染为相机图像，形成可从图像观测评估的重建框架。
- 在合成动态极光序列和真实多视角极光视频上展示了时间连贯的重建以及与观测一致的图像投影。

### 局限性
- 摘要未提供足够信息说明方法在真实数据上的定量精度、失败案例或对相机标定与噪声的敏感性。
- 摘要未提供足够信息说明“学习到的离散动力学”的具体形式、训练数据规模、计算成本及泛化能力。
- 摘要未提供足够信息说明与现有极光层析方法的定量对比结果。
- 摘要未提供足够信息说明 delayed emissions 建模的物理假设范围及多视角设置的具体限制。

### 阅读优先级
中。理由：该论文针对极光电子 precipitation 的动态反演问题，结合神经场、隐动力学与可微渲染，属于动态/4D 重建与地球物理逆问题的交叉方向；摘要明确给出了方法框架和在合成与真实多视角数据上的评估结论。但摘要未提供定量结果、对比细节和局限讨论，若读者关注极光层析或神经场逆渲染可优先细读，否则可作为方法参考级阅读。

</details>

<details>
<summary>Abstract</summary>

Auroras provide remote optical observations of energetic electrons precipitating into the upper atmosphere, and whose energy distribution encodes key information about large scale magnetospheric processes. Recovering the underlying electron precipitation field from ground-based camera images of auroras remains a challenging inverse problem. Existing auroral tomography techniques are often limited to simplified static settings, discrete spatial and energy grids, or strong assumptions on the electron energy spectrum. We propose to model the dynamic auroral electron precipitation field via a temporally conditioned neural network. The state of the precipitation field at each frame is represented by a per-frame latent code driven by learned discrete dynamics. A shared decoder maps horizontal positions and latent states to electron energy spectra. The predicted flux is converted to multi-wavelength volume emission rates and rendered into camera images accounting for delayed emissions. We evaluate the method on synthetic dynamic auroral sequences and real multi-view auroral videos, showing that the proposed representation produces temporally coherent precipitation reconstructions and image projections consistent with the observations.

</details>

#### 2026-11-12 - Reconstruct What You Can: Distractor-free 4D Gaussian Splatting

**Authors:** Joel Julin, Liuyue Xie, Ananya Bal, Mose Sakashita, Koichiro Niinuma, Laszlo A. Jeni
**Links:** [abs](https://arxiv.org/abs/2611.16259) - [pdf](https://arxiv.org/pdf/2611.16259)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reconstruct What You Can: Distractor-free 4D Gaussian Splatting
- 作者：Joel Julin, Liuyue Xie, Ananya Bal, Mose Sakashita, Koichiro Niinuma, Laszlo A. Jeni
- 出版日期：2026-11-12T03:59:45Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.16259 ；PDF https://arxiv.org/pdf/2611.16259

### 一句话总结
提出 ReCan-GS，一种 4D Gaussian Splatting 框架，利用从学习到的形变场导出的、基于 Jacobian 的形变敏感性分数区分一致场景内容与不一致观测，从而在无掩码、无预训练分割器、无介质专属监督的情况下抑制动态重建中的干扰物。

### 研究问题
从随意拍摄的视频进行动态重建时，需要在保留有效主体运动的同时抑制瞬态遮挡物、阴影和体积效应。现有方法要么通过静态场景假设抑制了有效运动，要么对所有观测联合建模，导致鬼影和不稳定几何。论文关注如何将一致的场景内容与不一致的观测分离开来。

### 核心思路/方法
ReCan-GS 从学习到的形变场中导出基于 Jacobian 的形变敏感性分数，并将其作为重建歧义的经验代理。该分数引导两种处理方式：一是将高斯分离为动态的 Core Gaussians 与逐视角的 Distractor Gaussians；二是对敏感的 Core Gaussians 进行事后剪枝。同一准则支持去除空间遮挡物、光度伪影以及演化中的烟雾或雾，且不需要掩码、预训练分割器或介质特定监督。

### 主要贡献
- 提出 ReCan-GS 4D Gaussian Splatting 框架，用于分离一致场景内容与不一致观测。
- 引入基于 Jacobian 的形变敏感性分数，作为重建歧义的经验代理，并用于 Core/Distractor 高斯分离或事后剪枝。
- 同一准则可处理空间遮挡物、光度伪影及演化烟雾/雾，无需掩码、预训练分割器或介质专属监督。
- 在合成与真实动态场景以及合成烟雾/雾场景上进行了实验，显示其在所评估的干扰物情形下具有效用。

### 局限性
摘要未提供足够信息。摘要未给出定量实验结果、具体失败情形、计算开销、对形变场质量的依赖程度，也未说明在何种干扰物类型或场景条件下可能失效。

### 阅读优先级
中。理由：该工作针对 casual video 动态重建中干扰物抑制这一明确问题，方法思路清晰且声称无需掩码或预训练分割器，具有一定通用性；但摘要仅提供方法概述与实验场景类型，未给出定量结果与失败分析，需阅读全文才能判断实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Dynamic reconstruction from casual video must preserve valid subject motion while suppressing transient occluders, shadows, and volumetric effects. Existing methods either suppress valid motion through static-scene assumptions or model all observations jointly, producing ghosting and unstable geometry. We introduce ReCan-GS, a 4D Gaussian Splatting framework that separates coherent scene content from inconsistent observations. It derives a Jacobian-based deformation-sensitivity score from the learned deformation field, using it as an empirical proxy for reconstruction ambiguity. The score guides separation into dynamic Core Gaussians and per-view Distractor Gaussians, or post-hoc pruning of sensitive Core Gaussians. The same criterion supports removal of spatial occluders, photometric artifacts, and evolving smoke or fog without masks, pretrained segmenters, or medium-specific supervision. Experiments on synthetic and real dynamic scenes and synthetic smoke/fog scenes demonstrate its usefulness across the evaluated distractor regimes.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-17 - TRIDENT: Efficient Triple-Task Learning of Dehazing, Depth, and Uncertainty Estimation for Underwater 3-D Robot Visual Perception

**Authors:** Geonmo Yang, Younggun Cho
**Links:** [abs](https://arxiv.org/abs/2611.22224) - [pdf](https://arxiv.org/pdf/2611.22224)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, feature matching

<details>
<summary>Abstract</summary>

Underwater visual systems often suffer from blurry textures and low color contrast due to the inevitable light propagation. These issues can significantly degrade the perception of stable robotic operations. In this paper, we introduce a novel learning-based sensing system that tackles the multidimensional vision tasks in underwater; concretely, we deal with image enhancement, depth estimation, and uncertainty for 3-D visual systems. Also, we propose a TRIDENT model in a fast and lightweight manner; TRIDENT consists of three parallelized decoders and one backbone structure for efficient feature sharing. In addition, it is designed to be trained to express complex parameterization. In experimental evaluation on several standard datasets, we demonstrate that TRIDENT significantly outperforms other existing methods on image enhancement and depth estimation. Despite performing three tasks, our model has better efficiency than the others for both memory size and inference time. Finally, our joint learning approach demonstrates robustness in feature matching and seamlessly extends from 2-D to 3-D vision tasks. Supplements are available at https://sites.google.com/view/underwater-trident/home

</details>

#### 2026-11-17 - Joint-ID: Transformer-based Joint Image Enhancement and Depth Estimation for Underwater Environments

**Authors:** Geonmo Yang, Gilhwan Kang, Juhui Lee, Younggun Cho
**Links:** [abs](https://arxiv.org/abs/2611.22212) - [pdf](https://arxiv.org/pdf/2611.22212)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, feature matching, robotics

<details>
<summary>Abstract</summary>

Underwater imaging is a challenging task due to factors such as scattering, absorption, and turbulence, which degrade image quality and limit visibility. In this paper, we propose a novel approach for enhancing underwater images that leverages the benefits of joint learning for simultaneous image enhancement and depth estimation. We introduce Joint-ID, a transformer-based neural network that can obtain high-perceptual image quality and depth information from raw underwater images. Our approach formulates a multi-modal objective function that addresses invalid depth, lack of sharpness, and image degradation based on color and local texture. We design an end-to-end training pipeline that enables joint restoration and depth estimation in a shared hierarchical feature space. Additionally, we propose a synthetic dataset with various distortions and scene depths for multi-task learning. We evaluate Joint-ID on synthetic and standard datasets, as well as real underwater images with diverse spectra and harsh turbidity, demonstrating its effectiveness for underwater image enhancement and depth estimation. Furthermore, we demonstrate the ability of Joint-ID to perform feature matching and saliency detection for visually guided underwater robots. Our proposed method has the potential to improve the visual perception of underwater environments and benefit applications such as oceanography and underwater robotics. Supplements are available at: https://sites.google.com/view/joint-id/home

</details>

#### 2026-11-17 - HandRSI: Recursive Self-Improvement for Hand Pose Estimation

**Authors:** Zhekai Wang, Luqing Luo, Wenhao Yao, Junjie Lu, Huanan Zhu, Feifei Gao, Yuhua Jiang
**Links:** [abs](https://arxiv.org/abs/2611.22164) - [pdf](https://arxiv.org/pdf/2611.22164)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Egocentric 3D hand pose estimators still miss hands at the image border, misplace occluded hands and jitter. Such failures are usually fixed by hand-written inference refinements and by fine-tuning, two interdependent steps that are tuned separately. We present HandRSI, a recursive self-improvement framework for a hand pose system that consists of a video estimator and its executable inference harness. In each round, coding agents refine the harness, and a change is accepted only if it improves a composite of all ten benchmark metrics on held-out data without significantly regressing any of them. The accepted harness then guides the estimator through selective distillation, which supervises hand presence and temporal consistency on frames without ground truth, while ground truth supervises pose. Since the updated estimator may change which refinements remain useful, the harness is re-validated on it. Starting from the released ACE-Ego-Hand model, five rounds reduce MPJPE-p by 35% on HOT3D and 11% on ARCTIC and roughly halve jitter. On HOT3D, HandRSI's MPJPE-p is 16% lower than that of ACE-Ego-Hand fine-tuned on the same ground truth. Under a unified protocol, it outperforms nine re-run published methods on all ten metrics of both benchmarks. Hypervolume selection on the accuracy-speed front yields Lite, Medium and Heavy systems running at 20.7 to 41.1 FPS. This report gives the full method, every stage of every round and the complete protocol. Code, evaluator, harnesses and weights are public.

</details>

#### 2026-11-16 - Polygraph: Large-Scale Multi-Session Trajectory Optimization using Pose Graphs

**Authors:** Petar Lukovic, Tian Yi Lim, Marc Pollefeys, Pablo Speciale, Hermann Blum, Zuria Bauer
**Links:** [abs](https://arxiv.org/abs/2611.21163) - [pdf](https://arxiv.org/pdf/2611.21163)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, pose estimation, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Polygraph: Large-Scale Multi-Session Trajectory Optimization using Pose Graphs
- 作者：Petar Lukovic, Tian Yi Lim, Marc Pollefeys, Pablo Speciale, Hermann Blum, Zuria Bauer
- 出版日期：2026-11-16T14:27:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.21163) | [PDF](https://arxiv.org/pdf/2611.21163)

### 一句话总结
Polygraph 提出一种面向多会话轨迹的在线优化流程：按关键帧与空间簇逐步处理各会话轨迹，在不构建 3D 地图的前提下，通过跨会话检索、匹配与两级一致性门控建立位姿图边，从而融合为全局一致的轨迹集合。

### 研究问题
机器人、车辆和可穿戴设备多次经过同一环境时，每次通行会产生各自独立的轨迹（来自视觉或视觉惯性里程计）。这些轨迹局部准确，但会随时间漂移，且处于互不相关的坐标系中。如何将多个独立轨迹转化为一个全局一致的集合，即大规模多会话轨迹优化问题。现有方案大多离线工作：所有会话必须预先可用，固定一个会话作为参考坐标系，再优化单一融合地图。

### 核心思路/方法
- 以在线方式处理会话，一次处理一个关键帧和一个空间簇，且不构建 3D 地图。
- 将关键帧分组为局部簇；当簇闭合时，通过学习式图像检索将其与其他所有会话匹配。
- 候选对通过稀疏特征匹配、单目度量深度和鲁棒位姿估计进行验证。
- 采用两级一致性门控：只有当独立证据相互印证后，才允许跨会话边进入共享位姿图。
- 使用低成本增量求解保持图的最新状态，并通过周期性鲁棒批量求解剔除离群值。

### 主要贡献
- 提出 Polygraph 多会话轨迹优化流程，支持在线、逐关键帧与逐空间簇处理，且不构建 3D 地图。
- 设计结合学习式图像检索、稀疏特征匹配、单目度量深度与鲁棒位姿估计的跨会话匹配与验证机制。
- 引入两级一致性门控与增量/批量求解结合的策略，以控制跨会话边的引入并剔除离群值。
- 在摘要列出的多种场景（立体户外驾驶、HoloLens 与 iPad 室内通行、Boston Dynamics Spot 室内步行、大规模户外车辆与手持路线）上进行评估；与最接近的先前工作在同一 GPU 模型上按其报告时间对比，Polygraph 运行更快、提交更少回环边，并在精度上匹配或更优。

### 局限性
摘要未提供足够信息。例如，各场景的具体数据集规模、精度指标数值、失败案例、在线处理的延迟上限、对学习式检索与单目度量深度的依赖程度、内存与计算资源需求等，均未在摘要中说明。

### 阅读优先级
高。理由：该论文直指多会话轨迹优化中“离线、需固定参考会话、构建融合地图”的常见限制，提出在线且不建 3D 地图的流程，并在多种平台与场景上与先前工作对比；若关注多会话 SLAM、位姿图优化或跨会话回环，摘要显示其问题设定与方法组合具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Robots, vehicles, and wearable devices often traverse the same environment many times. Each pass produces its own trajectory from onboard visual or visual-inertial odometry. These trajectories are locally accurate but drift over time and live in unrelated coordinate frames. Turning many such independent trajectories into one globally consistent set is the large-scale multi-session trajectory optimization problem. Existing solutions largely work offline. All sessions must be available up front, one session is fixed as the reference frame, and a single fused map is then optimized. This paper presents Polygraph, a multi-session trajectory optimization pipeline that processes sessions online, one keyframe and one spatial cluster at a time, and never builds a 3D map. Keyframes are grouped into local clusters. When a cluster closes, it is matched against every other session through learned image retrieval. Candidate pairs are verified with sparse feature matching, monocular metric depth, and robust pose estimation. A two-tier consensus gate admits a cross-session edge into the shared pose graph only once independent evidence corroborates it. A cheap incremental solve keeps the graph current, and a periodic robust batch solve prunes outliers. We evaluate Polygraph on stereo outdoor driving, HoloLens and iPad indoor traversals, legged indoor locomotion with a Boston Dynamics Spot, and large-scale outdoor vehicle and handheld routes. Against the closest prior work on the same GPU model, using its reported timings, Polygraph runs faster, commits fewer loop-closure edges, and matches or improves on accuracy.

</details>

#### 2026-11-16 - Correspondence-Free Camera Pose Estimation by Matching Moments

**Authors:** Subhransu S. Bhattacharjee, Dylan Campbell, Rahul Shome
**Links:** [abs](https://arxiv.org/abs/2611.20797) - [pdf](https://arxiv.org/pdf/2611.20797)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Correspondence-Free Camera Pose Estimation by Matching Moments
- 作者：Subhransu S. Bhattacharjee, Dylan Campbell, Rahul Shome
- 出版日期：2026-11-16T09:44:04Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.20797) / [PDF](https://arxiv.org/pdf/2611.20797)

### 一句话总结
论文提出一种无需特征对应的无学习相机位姿估计方法 MomentPnP：通过匹配四阶以内的十四种置换不变图像矩，完成盲 PnP 的位姿初始化，再用 EM 迭代优化位姿与对应权重。

### 研究问题
论文关注盲透视 n 点（blind PnP）问题：在已标定相机的条件下，仅凭 2D 与 3D 点集估计相机位姿，而点与点之间的对应关系未知。论文要回答的是：能否利用对点集顺序不敏感的矩统计量，在不依赖学习模型、也不依赖显式对应关系的条件下，得到可靠的位姿估计，并在含离群点的场景下保持稳定。

### 核心思路/方法
- 对完整、无噪声的观测，论文指出：四阶以内的十四个置换不变图像矩可以为几乎每一个包含至少二十个点的 3D 点集唯一确定一个固定相机位姿。
- 方法本身不依赖学习：在观测到的 2D 点与投影后的 3D 点之间匹配上述矩，以此初始化一个无对应关系的相机位姿。
- 随后使用期望最大化（EM）迭代优化相机位姿与对应权重。

### 主要贡献
- 提出 MomentPnP，一种无需学习、无需初始对应的盲 PnP 位姿估计流程。
- 给出关于矩的判别性结论：对完整、无噪声观测，四阶以内十四个置换不变矩可识别几乎每个至少含二十个点的 3D 点集所对应的固定相机位姿。
- 在三个基准的测试集上，相对最佳学习基线，论文方法将中位旋转误差降低 5–170 倍，含离群点与不含离群点的情形均如此。
- 在离群点数量与内点数量相当的情况下，仍能恢复较准确的位姿。
- 在稠密 ETH3D 扫描上，随着点集增大，位姿精度提升，即使单个对应关系变得更难分辨。

### 局限性
- 摘要未提供足够信息说明方法在部分观测、噪声观测或非完整点集下的理论保证与表现边界。
- 摘要未提供足够信息说明计算复杂度、运行时间与实时性。
- 摘要未提供足够信息说明在极端离群点比例（超过内点数量）下的失效条件。
- 摘要未提供足够信息说明对点集规模下限、退化构型以及矩匹配失败情形的处理细节。
- 摘要未提供足够信息说明除旋转误差外的平移误差、完整误差分布及消融实验细节。

### 阅读优先级
中。理由：该工作针对盲 PnP 提出无学习、基于矩匹配加 EM 的清晰技术路线，并在摘要中给出较大幅度的旋转误差改进与抗离群点表现，对 3D 重建与多视图几何中的无对应位姿估计有直接参考价值；但摘要未提供计算效率、退化情形与更完整误差指标等信息，是否优先精读取决于读者对无对应配准或无学习几何方法的关注程度。

</details>

<details>
<summary>Abstract</summary>

The blind perspective-$n$-point (PnP) problem is to estimate the pose of a calibrated camera from 2D and 3D point sets with unknown correspondences. We show that, for complete, noiseless observations, fourteen permutation-invariant image moments up to order four identify a fixed camera pose for almost every 3D point set containing at least twenty points. Our learning-free method, MomentPnP, matches these moments between the observed 2D points and the projected 3D points to initialize a camera pose without correspondences and refines the pose and correspondence weights using expectation--maximization. Across the test sets of three benchmarks, our method reduces median rotation error by $5$--$170\times$ relative to the best learned baseline, both with and without outliers. We recover accurate poses even with as many outliers as inliers. On dense ETH3D scans, pose accuracy improves as the point sets grow, even as individual correspondences become harder to resolve.

</details>

#### 2026-11-16 - sqrtVINS-Based 360 Visual-Inertial SLAM Systems: Hilti-Trimble SLAM Challenge 2026 Entry

**Authors:** Jungwoo Lee, Hogyun Kim, Jiwon Choi, Jinyong Jeong, Younggun Cho
**Links:** [abs](https://arxiv.org/abs/2611.20568) - [pdf](https://arxiv.org/pdf/2611.20568)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：sqrtVINS-Based 360 Visual-Inertial SLAM Systems: Hilti-Trimble SLAM Challenge 2026 Entry
- 作者：Jungwoo Lee, Hogyun Kim, Jiwon Choi, Jinyong Jeong, Younggun Cho
- 出版日期：2026-11-16T05:50:01Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.20568 ；PDF https://arxiv.org/pdf/2611.20568

### 一句话总结
该报告介绍了一套仅使用双鱼眼图像流与 IMU 测量的 360 相机视觉惯性 SLAM 流水线，作为 2026 年 Hilti-Trimble SLAM Challenge 的参赛方案。

### 研究问题
面向长室内序列中的暗区、重复走廊、动态物体和有限几何视差等挑战，构建可复现的 360 视觉惯性 SLAM 系统，并在给定 ROS2 工作空间内完成提交。摘要未提供足够信息说明具体评测指标与对比基线。

### 核心思路/方法
系统仅使用提供的双鱼眼图像流和 IMU 测量。前端流程为：原始图像先做低光增强与静态/动态掩码预处理，再输入 $\sqrt{\text{VINS}}$ 前端作为局部里程计，特征包括基于深度学习的 SuperPoint 特征、ELSED 线段以及 LightGlue 匹配。后端采用基于 GTSAM 的紧耦合因子图优化，结合 SALAD 全局描述子和视觉 bundle adjustment（BA），执行局部到全局的无结构 BA、紧正则化的内参外参细化，以及由已知相机间基线和跨视角约束支持的全局尺度调整。设计目标是在给定 ROS2 工作空间中保持流水线可复现。

### 主要贡献
- 提出一套面向 360 双鱼眼相机与 IMU 的视觉惯性 SLAM 流水线，并提交至 2026 Hilti-Trimble SLAM Challenge。
- 前端结合低光增强、静态/动态掩码、SuperPoint 特征、ELSED 线段与 LightGlue 匹配，并接入 $\sqrt{\text{VINS}}$ 前端做局部里程计。
- 后端采用 GTSAM 紧耦合因子图优化，融合 SALAD 全局描述子与视觉 BA，并进行内参外参细化和基于跨视角约束的全局尺度调整。
- 摘要称 Fig. 1 显示所提方法在若干室内序列上与楼层平面图对齐良好。

### 局限性
摘要未提供足够信息说明定量精度、运行效率、失败案例、消融实验、与其他系统的对比结果，以及各模块的具体贡献程度。摘要也未提供足够信息说明低光增强、动态掩码和线段特征在挑战场景中的实际收益与适用边界。

### 阅读优先级
中。理由：该文是 SLAM 挑战赛技术报告，方法组合较完整且覆盖 360 视觉惯性 SLAM 的多个工程环节，对相关方向有参考价值；但摘要未给出定量结果与详细实验分析，若需评估性能或复现细节，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

This report describes our submission to the 2026 Hilti-Trimble SLAM Challenge. The system is a 360-camera visual-inertial pipeline that uses only the provided dual-fisheye image streams and IMU measurements. First, raw images are preprocessed with low-light enhancement and static/dynamic masking, and then fed into a $\sqrt{\text{VINS}}$ frontend as the local odometry, with deep learning-based SuperPoint features, ELSED line segments, and LightGlue matching. The resulting trajectory is refined using a GTSAM-based backend that performs tightly-coupled factor graph optimization with SALAD global descriptor and visual bundle adjustment (BA). The backend performs local-to-global structureless BA, tightly regularized intrinsic and extrinsic refinement, and global scale adjustment supported by the known inter-camera baseline and cross-view constraints. The design targets long indoor sequences with dark regions, repetitive corridors, dynamic objects, and limited geometric parallax, while keeping the pipeline reproducible in the provided ROS2 workspace. Fig. 1 demonstrates that our proposed method aligns well with the floorplan across several indoor sequences.

</details>

#### 2026-11-16 - Pointillist Maize: 3D Reconstruction of Field-Grown Maize Using RGB UAV Imagery

**Authors:** Dewi Endah Kharismawati, Toni Kazic
**Links:** [abs](https://arxiv.org/abs/2611.20502) - [pdf](https://arxiv.org/pdf/2611.20502)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, multi-view stereo, structure from motion

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Pointillist Maize: 3D Reconstruction of Field-Grown Maize Using RGB UAV Imagery
- 作者：Dewi Endah Kharismawati, Toni Kazic
- 出版日期：2026-11-16T04:13:56Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.20502) / [PDF](https://arxiv.org/pdf/2611.20502)

### 一句话总结
该论文评估消费级无人机 RGB 视频结合 Structure from Motion 与多视图立体能否重建田间玉米的可识别结构，并分析采集轨迹与帧采样对重建完整性和点分散的影响。

### 研究问题
田间玉米的细长、柔韧、相互遮挡的结构以及植株运动会给三维重建带来困难。论文关注两个问题：消费级 UAV RGB 影像能否恢复可识别的田间玉米器官；采集轨迹和帧采样策略如何影响重建结果。

### 核心思路/方法
使用消费级 UAV RGB 视频，经 Structure from Motion 和多视图立体进行重建，并以 COLMAP 重建结果分析可识别结构。摘要提到的采集策略比较包括：同一视频的两组各 295 帧（单轨道以 5 帧/秒采样，与三种不同高度的轨道即“ribbon skirt”以 2 帧/秒采样）进行等帧数比较；在密集种植苗行中比较单轨道 1 帧/秒、增加蛇形航线以及将原轨道以 3 帧/秒采样时的可见空洞比例；并提及 2024 年在另一田块测试的 curlicue 轨迹。

### 主要贡献
- 表明 COLMAP 重建能够保留可识别的叶片、茎、雄穗分枝、果穗、花丝和支撑根。
- 给出等帧数条件下单轨道与 ribbon skirt 轨迹的重建对比：去地面后分别包含 520,601 和 375,318 个点；单轨道在植株结构内的点更集中、可见缺口更少，ribbon skirt 的散点更少且孤立点比例略低。
- 在密集苗行中报告可见空洞占渲染场景的比例：单轨道 1 帧/秒为 17.57%，增加蛇形航线后降至 5.07%，原轨道以 3 帧/秒采样时降至 2.68%。
- 指出增加观测也会增加与植株运动相关的点分散。
- 报告 2024 年另一田块中 curlicue 轨迹可区分单株且未见明显重复结构，但仍存在较大空洞，主要在土表。

### 局限性
- 摘要明确指出的局限包括：细长、柔韧、遮挡结构和植株运动使重建复杂；增加观测会带来与植株运动相关的点分散；curlicue 轨迹下仍有较大空洞，主要位于土表。
- 摘要明确指出，在用于定量表型分析前仍需独立的几何验证。
- 关于重建精度、误差指标、不同基因型或环境下的泛化能力、计算成本等，摘要未提供足够信息。
- 关于“ribbon skirt”和“curlicue”轨迹的具体参数细节，摘要未提供足够信息。

### 阅读优先级
中。理由：该论文直接讨论田间玉米 UAV 三维重建的可行性及采集策略与重建完整性的权衡，对相关三维重建和田间表型采集设计有参考价值；但摘要显示其重点在可行性评估，且作者明确指出仍需独立几何验证，尚未进入可定量表型的验证阶段。

</details>

<details>
<summary>Abstract</summary>

Three-dimensional reconstruction can extend field phenotyping to individual maize organs, but thin, flexible, occluding structures and plant movement complicate reconstruction. We evaluated whether consumer-grade UAV RGB video processed with Structure from Motion and multi-view stereo could recover recognizable field-grown maize structures, and examined the effects of acquisition trajectories and frame sampling. COLMAP reconstructions preserved recognizable leaves, stems, tassel branches, ears, silks, and brace roots. For an equal-frame comparison, we reconstructed one plant from two sets of 295 frames from the same video: a single orbit sampled at 5 frames/second and three orbits at different altitudes (ribbon skirt) sampled at 2 frames/second. After ground removal, the reconstructions contained 520,601 and 375,318 points, respectively. The single orbit yielded greater point concentration within plant structures and fewer visible gaps, while the ribbon skirt yielded fewer scattered points and slightly lower proportions of isolated points. In densely planted nursery rows, visible voids occupied 17.57% of the rendered scene with one orbit at 1 frame/second, decreasing to 5.07% with additional serpentine passes and 2.68% when the original orbit was sampled at 3 frames/second. Additional observations also increased point dispersion associated with plant movement. A curlicue trajectory tested in a different field in 2024 produced distinguishable individual plants without visible duplicated structures, although substantial voids remained, mainly on the soil surface. These results demonstrate the feasibility of recovering recognizable maize organs from consumer UAV imagery and reveal trade-offs between acquisition strategies, reconstruction completeness, and point dispersion. Independent geometric validation is still needed before quantitative phenotyping.

</details>

#### 2026-11-16 - Structure-Guided Multi-Granularity Spatiotemporal Transformer for Efficient Monocular 3D Human Pose Estimation

**Authors:** Sheng Xu, Aoduo Li, Rongli He
**Links:** [abs](https://arxiv.org/abs/2611.20361) - [pdf](https://arxiv.org/pdf/2611.20361)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Structure-Guided Multi-Granularity Spatiotemporal Transformer for Efficient Monocular 3D Human Pose Estimation
- 作者：Sheng Xu, Aoduo Li, Rongli He
- 出版日期：2026-11-16T00:41:54Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.20361) / [PDF](https://arxiv.org/pdf/2611.20361)

### 一句话总结
论文提出一种结构引导的多粒度时空 Transformer，通过融入骨骼结构先验并利用关键帧注意力降低冗余计算，以提升单目 3D 人体姿态估计的准确性与效率。

### 研究问题
现有单目 3D 人体姿态估计的多粒度方法偏重空间关节特征，未充分利用骨骼结构信息，包括全局连通性与时间连续性；同时，对整个帧序列建模会带来较高计算成本。论文旨在解决结构信息利用不足与计算效率不高的问题。

### 核心思路/方法
论文提出 Structure-Aware Multi-Granularity Spatiotemporal Transformer，在空间与时间表示中整合结构先验。方法包括：
- 三级特征提取器，在关节、骨骼和肢体层面捕捉人体拓扑结构；
- Gated Adaptive Spatial Attention（GASA），将结构约束嵌入空间注意力；
- Multi-Granularity Feature Enhancement（MGFE），通过分层池化与融合增强局部细节和全局语义；
- Temporal Segment Fusion（TSF），对齐不同粒度的时间上下文，以捕捉短程和长程运动模式；
- Hierarchical Cross-Attention（HCA），促进不同粒度间的时空交互；
- Keyframe Attention（KFA），选择信息量较高的运动片段，以减少冗余和计算成本。

### 主要贡献
- 提出结构感知的多粒度时空 Transformer，将骨骼结构先验融入空间与时间表示；
- 设计三级特征提取与 GASA、MGFE 模块，强化关节、骨骼、肢体层面的拓扑建模与多粒度特征融合；
- 引入 TSF、HCA 与 KFA，用于时间上下文对齐、跨粒度时空交互和关键帧选择，以兼顾精度与效率；
- 摘要称实验表明，该方法相较传统 Transformer 方法在准确性和效率上有所提升。

### 局限性
摘要未提供足够信息说明具体实验设置、数据集、评价指标、计算开销数值、消融实验细节及失败场景。论文的实际泛化能力、对遮挡或复杂动作的鲁棒性，以及 KFA 选择策略的潜在误差，均无法仅凭摘要判断。

### 阅读优先级
中。理由：该论文聚焦单目 3D 人体姿态估计中的结构先验利用与计算效率问题，方法模块设计较完整，适合关注多粒度时空建模或 Transformer 效率改进的读者进一步阅读；但摘要未给出定量结果与实验细节，是否需要优先精读取决于读者对骨骼结构引导和关键帧注意力机制的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Existing multi-granularity methods for monocular 3D human pose estimation emphasize spatial joint features while underusing skeletal structure, including global connectivity and temporal continuity. Moreover, modeling entire frame sequences incurs high computational costs. We propose a Structure-Aware Multi-Granularity Spatiotemporal Transformer that integrates structural priors across spatial and temporal representations for accurate and efficient pose estimation. A three-level feature extractor captures human topology at the joint, bone, and limb levels. Gated Adaptive Spatial Attention (GASA) embeds structural constraints into spatial attention, while Multi-Granularity Feature Enhancement (MGFE) uses hierarchical pooling and fusion to strengthen local details and global semantics. Temporal Segment Fusion (TSF) aligns temporal contexts across granularities to capture both short- and long-range motion patterns. Hierarchical Cross-Attention (HCA) promotes spatiotemporal interaction between granularities, and Keyframe Attention (KFA) selects informative motion segments to reduce redundancy and computational cost. Experiments demonstrate improved accuracy and efficiency over conventional Transformer-based approaches, highlighting the effectiveness of structure-aware multi-granularity modeling for monocular 3D human pose estimation.

</details>

#### 2026-11-15 - AstroPIE-53: Towards Understanding Failure Modes of Human Pose Estimation in Space

**Authors:** Stephanie Käs, Marten Flaig, Lukas Woyke, Osmanalp Ömeroğlu, Felix Krueckel, Onur Alp Çulha, Bastian Leibe
**Links:** [abs](https://arxiv.org/abs/2611.20207) - [pdf](https://arxiv.org/pdf/2611.20207)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AstroPIE-53: Towards Understanding Failure Modes of Human Pose Estimation in Space
- 作者：Stephanie Käs, Marten Flaig, Lukas Woyke, Osmanalp Ömeroğlu, Felix Krueckel, Onur Alp Çulha, Bastian Leibe
- 出版日期：2026-11-15T19:14:51Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.20207 ；PDF https://arxiv.org/pdf/2611.20207

### 一句话总结
论文发布了一个包含 53 段已标注宇航员视频的试点数据集 AstroPIE-53，并在零样本部署条件下系统分析人体检测与姿态估计在太空场景中的失败模式。

### 研究问题
现代计算机视觉在地球上能够实现较准确的人体检测和姿态估计，但其在太空环境中的鲁棒性由于数据有限而“基本未被量化”。论文关注：在真实太空任务视频中，现有人体检测与姿态估计模型会出现哪些性能退化，以及这些失败与哪些场景因素相关。

### 核心思路/方法
作者从公开任务影像中收集 53 段宇航员视频并进行标注，构建试点数据集 AstroPIE-53。为规避版权限制，数据集不发布原始视频，而是提供视频标识符、重建脚本和密集标注。标注内容包括边界框、挑战类别以及人工标注的姿态失败标签。随后，作者在现实的零样本部署条件下对先进的人体检测和姿态估计模型进行基准测试，并开展针对宇航员监测的首个系统性失败分析。

### 主要贡献
- 提出 AstroPIE-53：一个包含 53 段标注宇航员视频的试点数据集，用于太空场景人体姿态估计研究。
- 在版权限制下采用“视频标识符 + 重建脚本 + 密集标注”的发布方式。
- 提供边界框、挑战类别和人工姿态失败标签等多类标注。
- 在零样本部署条件下对先进人体检测与姿态估计模型进行基准评测。
- 开展针对宇航员监测的首个系统性失败分析，指出遮挡、异常身体朝向、低对比度和微重力运动模式会导致显著性能退化。

### 局限性
- 数据集规模仅为 53 段视频，属于试点数据集；更大规模下的泛化性摘要未提供足够信息。
- 由于版权限制，未发布原始视频，使用方需依赖视频标识符和重建脚本获取数据；实际可复现性和数据可获得性细节摘要未提供足够信息。
- 摘要仅给出失败因素类别和“显著性能退化”的结论，未提供具体模型、量化指标、实验设置和统计细节。
- 论文聚焦人体检测与姿态估计的失败分析，是否覆盖其他宇航员监测任务摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对太空场景下人体姿态估计的数据稀缺与失败模式问题，选题明确，且提供数据集、标注与零样本基准分析，对相关研究方向有参考价值；但摘要显示其为 53 段视频的试点数据集，且未给出具体量化结果与完整实验细节，是否值得优先精读取决于读者对太空人体监测或姿态估计鲁棒性分析的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Reliable monitoring of astronauts is essential for safety, situational awareness, and autonomous assistance in space missions. While modern computer vision enables accurate human detection and pose estimation on Earth, its robustness in space environments remains largely unquantified due to limited data availability. We present AstroPIE-53, a pilot dataset of 53 annotated astronaut videos collected from publicly available mission footage. To respect copyright restrictions, we release video identifiers, reconstruction scripts, and dense annotations rather than raw videos. The dataset includes bounding boxes, challenge classes, and human-annotated pose failure tags. We benchmark state-of-the-art person detection and pose estimation models under realistic zero-shot deployment conditions and perform the first systematic failure analysis for astronaut monitoring. Our results reveal substantial performance degradation caused by occlusions, unusual body orientations, low contrast, and microgravity motion patterns.

</details>

#### 2026-11-15 - SemLite-GS: Semantic-Selective Parallel Gaussian Splatting for Lightweight Building Reconstruction from UAV Oblique Imagery

**Authors:** Tengfei Wang, Xin Wang, Zihan Li, Quanjian Ji, Yifei Yu, Dong Lin, Zongqian Zhan
**Links:** [abs](https://arxiv.org/abs/2611.19773) - [pdf](https://arxiv.org/pdf/2611.19773)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, multi-view stereo, dense reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SemLite-GS: Semantic-Selective Parallel Gaussian Splatting for Lightweight Building Reconstruction from UAV Oblique Imagery
- 作者：Tengfei Wang, Xin Wang, Zihan Li, Quanjian Ji, Yifei Yu, Dong Lin, Zongqian Zhan
- 出版日期：2026-11-15T03:59:03Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Neural Scene Representations & Rendering
- 链接：摘要页：https://arxiv.org/abs/2611.19773 ；PDF：https://arxiv.org/pdf/2611.19773

### 一句话总结
SemLite-GS 面向无人机倾斜影像中的建筑物，提出以建筑实例为中心的语义选择性并行高斯泼溅框架，用于重建轻量化建筑网格，并在摘要报告的大规模 UAV 数据集实验中减少重建时间、改善主导平面与建筑结构边界的保持。

### 研究问题
论文关注从大规模 UAV 倾斜影像生成轻量化 3D 建筑模型的问题。摘要指出，此类模型虽支持城市空间分析，但其生产通常依赖稠密场景重建、建筑提取与网格简化等多个环节。现有 3D Gaussian Splatting 方法虽比传统多视图立体更高效，但摘要认为大规模方法仍缺乏语义选择与并行的实例级训练能力。

### 核心思路/方法
摘要给出的方法包含三个主要环节：
1. 利用正交参考图建立全局一致的建筑身份，并将其传播到倾斜视图，形成相机—实例对与感兴趣区域。
2. 采用语义选择性并行 PGSR 训练，在相关图像区域内联合处理多个相机—实例对，但只更新目标高斯，上下文高斯保持固定以维持可见性。
3. 从渲染得到的深度、不透明度与法线图中提取建筑平面，用以引导有符号距离场优化，从而生成具有自适应多边形分配和明确结构边界的网格。

### 主要贡献
- 提出以建筑为中心的 SemLite-GS 框架，用于从大规模 UAV 倾斜影像重建轻量化建筑网格。
- 引入基于正交参考图的全局建筑身份建立与向倾斜视图传播机制，形成相机—实例对和感兴趣区域。
- 设计语义选择性并行 PGSR 训练策略，仅更新目标高斯并固定上下文高斯。
- 利用渲染深度、不透明度和法线图提取建筑平面，引导有符号距离场优化，实现自适应多边形分配与结构边界保持。
- 摘要称在多个大规模 UAV 数据集上，相比代表性全场景 3DGS 方法显著减少建筑重建时间；在相近多边形预算下，相比“稠密重建后网格简化”的流程，更好地保持主导平面结构和锐利建筑过渡。
- 摘要提供源代码链接：https://github.com/IRIS-LAB-whu/SemLite-GS

### 局限性
摘要未提供足够信息说明方法的具体失败情形、对建筑类型或影像条件的敏感性、精度指标细节、内存与并行开销、跨数据集泛化能力，以及与传统方法在非平面结构上的对比表现。摘要仅报告了重建时间减少和相近多边形预算下的结构保持优势，未给出完整实验设置、定量指标数值和消融细节。

### 阅读优先级
中。理由：该论文主题明确，聚焦 UAV 倾斜影像的轻量化建筑重建，并结合语义选择、并行高斯训练与网格生成，和 3D 重建及神经场景表示相关。但当前仅有摘要与元数据，缺少定量结果、实验规模和实现细节；若读者关注建筑级轻量化重建或 3DGS 的实例级并行训练，可优先进一步阅读全文，否则可保持中等优先级。

</details>

<details>
<summary>Abstract</summary>

Lightweight 3D building models support urban spatial analysis, but their production often requires dense scene reconstruction, building extraction, and mesh simplification. Although 3D Gaussian Splatting (3DGS) is more efficient than conventional multi-view stereo, existing large-scale methods lack semantic selection and parallel instance-level training. We present SemLite-GS, a building-centric framework that reconstructs lightweight building meshes from large-scale UAV oblique imagery. First, an orthographic reference map establishes globally consistent building identities, which are propagated to oblique views to form camera-instance pairs and regions of interest. Second, semantic-selective parallel PGSR training jointly processes multiple pairs within relevant image regions while updating only target Gaussians; contextual Gaussians remain fixed to preserve visibility. Third, architectural planes extracted from rendered depth, opacity, and normal maps guide signed distance field optimization, producing meshes with adaptive polygon allocation and well-defined structural boundaries. Experiments on multiple large-scale UAV datasets demonstrate that our SemLite-GS substantially reduces building reconstruction time compared with representative full-scene 3DGS methods. With comparable polygon budgets, SemLite-GS achieves superior preservation of dominant planar structures and sharp architectural transitions compared with conventional dense reconstruction followed by mesh decimation. The source code is available at https://github.com/IRIS-LAB-whu/SemLite-GS.

</details>

#### 2026-11-12 - EG360: Efficient and Generalizable $360^\circ$ Depth Estimation via Adaptive Panorama-Perspective Distillation and Spherical Cross-Level Feature Fusion

**Authors:** Laiyan Ding, Chongxi Meng, Rui Huang
**Links:** [abs](https://arxiv.org/abs/2611.16793) - [pdf](https://arxiv.org/pdf/2611.16793)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EG360: Efficient and Generalizable $360^\circ$ Depth Estimation via Adaptive Panorama-Perspective Distillation and Spherical Cross-Level Feature Fusion
- 作者：Laiyan Ding, Chongxi Meng, Rui Huang
- 出版日期：2026-11-12T13:38:57Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2611.16793) / [PDF](https://arxiv.org/pdf/2611.16793)

### 一句话总结
EG360 是一个以轻量深度模型为基础的全景深度估计模型，通过自适应全景-透视蒸馏（APPD）和球面跨层特征融合（SCFF），在仅 6.593M 参数（重参数化后）下实现较强零样本泛化，并在 Jetson Orin NX 16GB（MAXN 模式）上达到 35 FPS。

### 研究问题
论文关注全景深度估计中“强泛化但计算昂贵”与“轻量但泛化差”两类模型之间的差距：使用大型预训练模型的方法零样本泛化较好，但高计算成本使嵌入式平台实时推理困难；此前的轻量全景模型多面向单域评估，因域偏移而泛化不佳。作者希望构建同时兼顾高效与可泛化的全景深度估计模型。

### 核心思路/方法
- 以轻量深度模型为基础构建 EG360。
- 设计自适应全景-透视蒸馏策略（Adaptive Panorama-Perspective Distillation, APPD），并由场景几何引导。
- 引入球面跨层特征融合模块（Spherical Cross-Level Feature Fusion, SCFF），用于全局语义感知。
- 通过重参数化后仅 6.593M 参数，在真实世界基准上取得较强零样本性能，并在 Jetson Orin NX 16GB（MAXN 模式）上以 35 FPS 运行；摘要称此前 ViT-small 模型在该设备上低于 2 FPS。

### 主要贡献
- 提出 EG360，一个高效且可泛化的全景深度估计模型，旨在缩小强泛化大模型与轻量单域模型之间的差距。
- 提出由场景几何引导的自适应全景-透视蒸馏策略 APPD。
- 提出用于全局语义感知的球面跨层特征融合模块 SCFF。
- 在仅 6.593M 参数（重参数化后）条件下，于真实世界基准取得较强零样本性能，并在指定嵌入式平台上实现 35 FPS；摘要提及代码将公开。

### 局限性
- 摘要未提供足够信息说明 APPD 中场景几何引导的具体形式、蒸馏损失设计及训练数据构成。
- 摘要未提供足够信息说明所采用的真实世界基准名称、零样本评估指标数值及与具体对比方法的完整结果。
- 摘要未提供足够信息说明 SCFF 的具体网络结构、融合层级与计算开销分析。
- 摘要未提供足够信息说明 35 FPS 对应的输入分辨率、精度设置及端到端流水线范围。
- 摘要未提供足够信息说明方法在不同域偏移类型或极端场景下的失败模式与局限性讨论。

### 阅读优先级
中。理由：该论文聚焦全景深度估计的轻量化与零样本泛化，并给出嵌入式平台实时性结果，对关注高效 3D 感知与全景深度估计的研究者有参考价值；但摘要未提供具体基准、指标数值和消融细节，需阅读全文才能判断方法有效性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Generalized panorama depth estimation has witnessed great advances in recent years. These methods typically achieve robust zero-shot generalization performance using large pretrained models, but their high computational cost makes real-time inference on embedded platforms challenging. In contrast, previous lightweight panorama models have mostly been developed for single-domain evaluations and cannot generalize well due to domain shifts. To reduce the gap between these two types of models, we introduce EG360, an efficient and generalizable panorama depth estimation model. Specifically, building on a lightweight depth model, we design an Adaptive Panorama-Perspective Distillation (APPD) strategy guided by scene geometry, along with a Spherical Cross-Level Feature Fusion (SCFF) module for global semantic perception. As a result, with only 6.593M parameters after reparameterization, EG360 achieves strong zero-shot performance on real-world benchmarks and runs at 35 FPS on a Jetson Orin NX 16GB in MAXN mode, whereas a previous ViT-small model runs at less than 2 FPS. Our code will also be made public for future research.

</details>

#### 2026-11-12 - RGB-D SLAM on the Edge: Benchmarking and Profiling RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5

**Authors:** Himanshu Patil, Jaideep Joshi, Rohit Saluja, Ganesh Ramakrishnan
**Links:** [abs](https://arxiv.org/abs/2611.16472) - [pdf](https://arxiv.org/pdf/2611.16472)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RGB-D SLAM on the Edge: Benchmarking and Profiling RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5
- 作者：Himanshu Patil, Jaideep Joshi, Rohit Saluja, Ganesh Ramakrishnan
- 出版日期：2026-11-12T08:29:56Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.16472 ；PDF https://arxiv.org/pdf/2611.16472

### 一句话总结
该论文在 Raspberry Pi 5 上对 RTAB-Map 与 ORB-SLAM3 两套 RGB-D SLAM 系统进行基准测试与分阶段、函数级性能剖析，重点报告跟踪覆盖率、轨迹误差、每帧时间、内存、CPU 负载和温度，并指出精度比较因运行间轨迹误差波动而无法定论。

### 研究问题
论文关注的问题是：在 ARM 边缘板（Raspberry Pi 5）上，标准 RGB-D SLAM 系统的实际运行表现如何。摘要指出，无 GPS 的微型飞行器常在 ARM 边缘板上运行 SLAM，但关于标准 RGB-D SLAM 系统在此类硬件上行为表现的公开数据很少。因此，论文以 RTAB-Map 和 ORB-SLAM3 为对象，考察其在边缘硬件上的跟踪覆盖、精度、耗时、资源占用与热行为。

### 核心思路/方法
- 在 Raspberry Pi 5 上使用 6 个 TUM RGB-D 序列、3 种图像分辨率对 RTAB-Map 和 ORB-SLAM3 进行基准测试。
- 每次运行记录跟踪覆盖率、轨迹误差、每帧时间、内存、CPU 负载和温度。
- 对两套系统进行阶段级和函数级剖析。
- RTAB-Map 被配置为处理并保留每一帧，因此其后端每帧运行，而不是按其默认 1 Hz 频率运行。
- 汇报结果时强调时间与精度必须结合覆盖率解读：在四分之一分辨率下，两套系统在多数序列上丢失跟踪，而丢失跟踪的运行更早结束，并且在其保留的位姿上报告更低误差。

### 主要贡献
- 提供了 RTAB-Map 与 ORB-SLAM3 在 Raspberry Pi 5 上使用 TUM RGB-D 序列的基准测试数据，覆盖 3 种分辨率，并记录跟踪覆盖率、轨迹误差、每帧时间、内存、CPU 负载和温度。
- 给出了两套系统的阶段级与函数级剖析结果。
- 报告了具体耗时特征：在所有配置均能跟踪的序列上，RTAB-Map 前端每帧 38–74 ms、完整流水线 150–462 ms；ORB-SLAM3 分别为 13–45 ms 和 26–62 ms。
- 指出 RTAB-Map 的主要开销来自优化不断增长的位姿图，原因是其默认工作内存无界；ORB-SLAM3 的局部 bundle adjustment 开销约与跟踪相当，但运行在并行线程中。
- 指出计时可重复性在 1–5% 以内，但相同运行之间的轨迹误差波动可达 27%，因此两系统之间的精度差异无法定论。
- 报告未发生热降频。

### 局限性
- 摘要未提供足够信息说明除 Raspberry Pi 5 之外的硬件平台、其他边缘设备的对比结果。
- 摘要未提供足够信息说明 6 个 TUM RGB-D 序列的具体名称与场景构成。
- 摘要未提供足够信息说明内存、CPU 负载和温度的具体数值或统计方式。
- 摘要未提供足够信息说明函数级剖析的具体工具与热点函数清单。
- 摘要未提供足够信息说明 RTAB-Map 非默认配置对结论外推的影响范围。
- 摘要未提供足够信息说明精度比较的统计检验方法；仅指出轨迹误差波动可达 27%，精度差异无法定论。
- 摘要未提供足够信息说明四分之一分辨率下丢失跟踪的具体序列数量与原因分析。

### 阅读优先级
中。理由：该论文针对 ARM 边缘板上的 RGB-D SLAM 基准测试与性能剖析，提供了 RTAB-Map 与 ORB-SLAM3 在 Raspberry Pi 5 上的耗时、覆盖率与资源数据，并对精度比较给出谨慎结论；对关注边缘部署、系统选型与性能瓶颈的读者有直接参考价值。但摘要显示精度差异无法定论，且实验范围限于摘要所述平台、序列与配置，若读者更关注算法精度创新或更广泛硬件对比，则需要进一步查看全文，摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Micro aerial vehicles that operate without GPS often run SLAM on ARM-based edge boards, yet there is little published data on how standard RGB-D SLAM systems behave on such hardware. We benchmark RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5 using six TUM RGB-D sequences at three image resolutions, recording tracking coverage, trajectory error, time per frame, memory, CPU load and temperature for every run, and we profile both systems at the stage and function level. RTAB-Map was configured to process and keep every frame, so its back end runs on every frame rather than at its default rate of 1 Hz. On the sequences that every configuration tracked, its front end takes 38-74 ms per frame and its full pipeline 150-462 ms, compared with 13-45 ms and 26-62 ms for ORB-SLAM3. RTAB-Map's main cost is optimizing a pose graph that keeps growing, because its working memory is unbounded by default; ORB-SLAM3's local bundle adjustment costs about as much as its tracking but runs in a parallel thread. At quarter resolution, both systems lose tracking on most sequences, and runs that lose tracking finish sooner and report lower error on the poses they keep, so time and accuracy must be read alongside coverage. Timing is repeatable to within 1-5%, but trajectory error varies by up to 27% between identical runs, so the accuracy differences between the two systems are inconclusive. No thermal throttling occurred.

</details>

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-17 - ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting

**Authors:** Chuanzhi Xu, Boyu Wei, Chengkun Yue, Xuanhua Yin, Yiyang Li, Haodong Chen, Qiang Qu, Weidong Cai
**Links:** [abs](https://arxiv.org/abs/2611.23054) - [pdf](https://arxiv.org/pdf/2611.23054)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic scene reconstruction. Existing 3DGS color transfer and interactive editing methods are guided by reference images and user-specified color adjustments. However, in many applications, users simply want aesthetically guided color enhancement that automatically makes the scene more visually appealing while maintaining consistent colors and tones across viewpoints. We present ReTouchGS, to our knowledge the first framework for reference-free aesthetic color enhancement of pretrained 3DGS models. It predicts a scene-level color lookup table (LUT) from the model and its associated camera parameters. ReTouchGS also supports reference-guided color transfer by fitting a scene-level LUT using one edited view of the same scene and its corresponding original render. A shared blend-aware color refinement network with only 44.7K parameters refines an analytic color update to realize either color mapping without rendering. It preserves geometry and delivers standard 3DGS assets in seconds. We also design the ReTouch3D benchmark to support the evaluation of aesthetic color enhancement and reference-guided color transfer across viewpoints. Experiments demonstrate high color accuracy and strong generalization to unseen scenes in both aesthetic color enhancement and reference-guided color transfer.

</details>

#### 2026-11-17 - DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting

**Authors:** Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang
**Links:** [abs](https://arxiv.org/abs/2611.22805) - [pdf](https://arxiv.org/pdf/2611.22805)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Traditional Gaussian Splatting (GS) methods use in-core training, i.e. assuming that GPU memory is large enough to accommodate all the primitives. This assumption breaks down when the primitives exceed the capacity of GPU memory, e.g. GS on large environments. Recent out-of-core training research starts to address this issue, but is limited to static scenes. Unlike static GS, dynamic GS primitives move in space and time, breaking common assumptions held in existing out-of-core research and impose new challenges in memory management and training. To this end, we propose Dynamic Out-of-core Optimization for Massive Gaussian Splatting (DOOM-GS), the first out-of-core optimization method designed specifically for massive-scale dynamic GS. DOOM-GS is equipped with novel memory management strategies that optimize caching for spatio-temporal primitives, and a fast learning method for large numbers of primitives. Due to the lack of suitable datasets for large-scale dynamic GS, we also contribute a new dataset for evaluation. Since there are no directly comparable methods, we adapt several closely related methods for comparison. Through extensive evaluation, we demonstrate the effectiveness of DOOM-GS which now makes it possible to reconstruct city-scale dynamic scenes with high quality on moderate hardware, serving as a foundational tool for diverse future research and applications.

</details>

#### 2026-11-17 - Cross3DGS: Unified Vulkan-Based 3D Gaussian Splatting Training from Workstations to Mobile Devices

**Authors:** Hiroyuki Sato, Yusuke Takimoto
**Links:** [abs](https://arxiv.org/abs/2611.22240) - [pdf](https://arxiv.org/pdf/2611.22240)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

Scenes captured with handheld and wearable cameras are still shipped to a CUDA workstation for 3D Gaussian Splatting (3DGS) training. Training on the device that captured them, or on its companion phone or laptop, requires more than translating kernels: GPUs and drivers differ in parallel features, memory limits, and command submission, and these differences decide whether a training schedule executes and returns the correct update. We present Cross3DGS, a cross-vendor, cross-platform Vulkan trainer that keeps one optimizer and chooses its execution schedule per device in two steps: rules on device limits, workload size, and observed driver failures exclude the schedules known not to run correctly, and a fixed preference order selects one of the remaining feasible schedules. The same core completes standard-quality training (30k updates, one million Gaussians) on every configuration we measured, spanning NVIDIA, Intel, Arm, Qualcomm, AMD, and Apple GPUs and including Android devices and an iPhone, whereas the existing portable trainers VkSplat and Brush do not run on some of the mobile GPUs. Averaged over 11 scenes on a workstation, Cross3DGS has higher quality than VkSplat with no significant difference in training time, and Brush reports about three times the training time at comparable quality. The final quality of Cross3DGS is nearly identical across devices. A mobile application turns a handheld capture into a viewable model entirely on the device.

</details>

#### 2026-11-17 - CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure

**Authors:** Qi Shao, Zhihao Cao, Shuhao Zhai, Taoyu Wu, Zhuoxiao Li, Anh Nguyen, Long Hu, Xianzhi Li, Hong Liang, Baoru Huang, Liang Li
**Links:** [abs](https://arxiv.org/abs/2611.22235) - [pdf](https://arxiv.org/pdf/2611.22235)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, rendering, splatting, mapping

<details>
<summary>Abstract</summary>

Dense collaborative mapping is essential for search and rescue, building inspection, and warehouse automation, where panoramic cameras capture the entire surroundings in a single frame. Unlike pinhole agents that share views only at similar headings, panoramic agents observe overlapping scenes at any 3D orientation, yet searching full rotations also produces mutually consistent false loop closures across distinct symmetric rooms. Moreover, continuous monocular scale drift splits rigidly merged maps at revisited surfaces, while depth noise at short baselines distorts loop translation directions. To address these challenges, we propose CoSphere-SLAM, the first multi-agent Gaussian splatting SLAM framework for panoramic cameras, whose spherical loop closure aligns spherical features over $\mathrm{SO}(3)$ via fast Fourier correlation across arbitrary orientations and rejects symmetric false closures through global $\mathrm{Sim}(3)$ consensus. Building on these closures, directional global optimization solves a per-keyframe $\mathrm{Sim}(3)$ pose graph with log-scale regularization to correct scale drift while separating optical-flow translation directions from depth-based magnitudes. Finally, omnidirectional Gaussian fusion transforms each Gaussian with its keyframe similarity and renders Gaussians at their maximum ray response to jointly refine poses and maps. Experiments on indoor and cross-session multi-agent panoramic benchmarks demonstrate that CoSphere-SLAM achieves state-of-the-art trajectory accuracy and rendering quality among single-agent and multi-agent methods. Project website: https://cosphere-slam.github.io.

</details>

#### 2026-11-16 - The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation

**Authors:** Jeonghwan Cho, Minsu Kim, Junyoung Hong, Seon Joo Kim
**Links:** [abs](https://arxiv.org/abs/2611.21383) - [pdf](https://arxiv.org/pdf/2611.21383)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation
- 作者：Jeonghwan Cho, Minsu Kim, Junyoung Hong, Seon Joo Kim
- 出版日期：2026-11-16T16:44:07Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.21383) / [PDF](https://arxiv.org/pdf/2611.21383)

### 一句话总结
针对 3D Gaussian Splatting 分割中“渲染掩码准确但三维选择不完整”的问题，论文提出即插即用的体素监督目标 VODA，并引入 Removal-3D 基准与 Removal Depth Error 指标来评估分割的三维完整性。

### 研究问题
现有 3D Gaussian 分割方法主要在渲染视图上训练与评估，这与三维对象级操作存在不匹配。由于 alpha 混合的特征监督会使学习集中于主要贡献的 Gaussian，遮挡或低贡献的 Gaussian 监督较弱，因此即使渲染掩码准确，三维选择也可能不完整。论文关注如何评估并改善 Gaussian 分割在体积层面的完整性。

### 核心思路/方法
论文提出 VODA，一种即插即用的监督目标：利用局部深度结构对逐像素贡献者进行分组，并直接监督所选深度簇中的所有 Gaussian，从而绕开按贡献加权的梯度传递方式。为评估体积完整性，论文还提出合成对象移除基准 Removal-3D，以及比较预测与真实深度变化的指标 Removal Depth Error（RDE）。

### 主要贡献
- 指出并形式化“渲染掩码准确不等于三维选择完整”的监督不匹配问题。
- 提出即插即用的体素监督目标 VODA，直接监督所选深度簇内的全部 Gaussian。
- 引入 Removal-3D 合成对象移除基准和 Removal Depth Error（RDE）指标，用于评估体积分割完整性。
- 摘要称在四个基于渲染的基线方法上，VODA 在 Removal-3D 上持续提升体积分割效果，并在 LERF 和 ScanNet 上保持或提升性能；进一步分析显示 VODA 能恢复低贡献 Gaussian，而简单梯度重加权与空间传播无法复现可比增益。

### 局限性
摘要未提供足够信息说明 VODA 的具体计算开销、对深度质量的敏感性、在真实场景中的泛化边界，以及 Removal-3D 的构建细节与规模。摘要未提供足够信息。

### 阅读优先级
中。理由：论文聚焦 3D Gaussian Splatting 分割中“渲染指标与体积完整性不匹配”这一具体问题，并提出即插即用监督目标与新基准/指标，对相关方向有参考价值；但摘要未提供实验规模、实现细节与局限分析，是否具有广泛影响需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting enables object-level operations on Gaussian primitives, yet existing segmentation methods are largely trained and evaluated through rendered views. This mismatch can produce accurate rendered masks from incomplete 3D selections since alpha-blended feature supervision concentrates learning on dominant contributors while leaving occluded or low-contribution Gaussians weakly supervised. We propose VODA, a plug-and-play supervision objective that exploits local depth structure to group per-pixel contributors and directly supervises all Gaussians in selected depth clusters, bypassing contribution-weighted gradient delivery. To evaluate volumetric completeness, we introduce Removal-3D, a synthetic object-removal benchmark, and the Removal Depth Error (RDE), a metric comparing predicted and ground-truth depth changes. Across four rendering-based baselines, VODA consistently improves volumetric segmentation on Removal-3D while maintaining or improving performance on LERF and ScanNet. Further analysis shows that VODA recovers lower-contribution Gaussians, while simple gradient reweighting and spatial propagation fail to reproduce comparable gains.

</details>

#### 2026-11-16 - QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting

**Authors:** Haiyang Xu, Ziye Zhang, Bin Pan, Xia Xu, Zhenwei Shi
**Links:** [abs](https://arxiv.org/abs/2611.21253) - [pdf](https://arxiv.org/pdf/2611.21253)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting
- 作者：Haiyang Xu, Ziye Zhang, Bin Pan, Xia Xu, Zhenwei Shi
- 出版日期：2026-11-16T15:28:51Z
- 分类：主分类为 Neural Scene Representations & Rendering；无二级分类信息
- 链接：摘要页 https://arxiv.org/abs/2611.21253 ；PDF https://arxiv.org/pdf/2611.21253

### 一句话总结
QuantileGS 是一个面向 3D Gaussian Splatting 新视角合成的后处理框架，通过学习每个高斯预测的渲染误差分位数，并结合尺度归一化共形校准，为逐像素 RGB 平均绝对误差提供具有有限样本边际覆盖保证的上界。

### 研究问题
论文关注 3D Gaussian Splatting 在新视角合成中的渲染可靠性不确定量化问题。由于在未见视角上无法获得真实图像，渲染颜色与真实颜色之间的差异无法直接测量；因此论文试图对未知的逐像素 RGB 平均绝对误差给出上界。摘要同时指出，单纯学习得到的误差上界可能低估误差并高估渲染可靠性，因此需要校准到预设的覆盖水平。

### 核心思路/方法
QuantileGS 是一个后处理框架，将学习到的渲染误差分位数与尺度归一化共形校准结合，生成空间自适应的误差上界。框架分为三个阶段：第一阶段在冻结的 3DGS 模型上计算观测图像与预测之间的 RGB 平均绝对误差；第二阶段学习“有序高斯分位数场”，为每个高斯学习两个标量属性，用于预测渲染误差的下分位数与上分位数；第三阶段在留出图像上对上限预测进行尺度归一化共形校准，并利用分位数间距缩放修正量。摘要称，在所述假设下，所得上界具有有限样本边际覆盖保证。

### 主要贡献
- 提出 QuantileGS，一种面向 3DGS 新视角合成渲染误差的后处理不确定性量化框架，输出逐像素 RGB 平均绝对误差的空间自适应上界。
- 将学习到的渲染误差分位数与尺度归一化共形校准结合，以缓解学习上界低估误差、过度宣称渲染可靠性的问题。
- 摘要报告在名义覆盖率为 90% 时，校准将 LLFF 上的平均经验测试覆盖率从 69.6% 提升到 89.6%，将 Mip-NeRF 360 上的覆盖率从 80.1% 提升到 92.1%；在 LF 上覆盖率保持保守，校准前为 96.3%，校准后为 96.4%。
- 摘要说明这些上界可用于主动视角选择、高斯剪枝以及 RGB-D 同时定位与建图等下游决策。

### 局限性
摘要仅给出有限样本边际覆盖保证，且该保证依赖“所述假设”，但摘要未展开具体假设内容。摘要未提供计算开销、实时性、不同 3DGS 变体上的泛化表现、校准集规模影响、覆盖率方差或失败案例等信息。关于主动视角选择、高斯剪枝和 RGB-D SLAM 的应用，摘要仅说明可“示意”这些上界如何辅助下游决策，未提供具体实验设置与量化结果。因此，上述方面的详细评估：摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接处理 3DGS 新视角合成中“无真值图像时如何量化渲染可靠性”的关键问题，方法路径清晰，包含分位数学习与共形校准，并报告了覆盖率校准前后的定量变化；对不确定性量化、3DGS 可靠性评估及相关下游决策研究具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Uncertainty quantification for novel view synthesis with 3D Gaussian Splatting (3DGS) assesses rendering reliability at unseen viewpoints. This reliability depends on the discrepancy between rendered and true colors, which cannot be measured without ground-truth images. We therefore quantify uncertainty in this unknown discrepancy through upper bounds on per-pixel RGB mean absolute error. However, learned bounds may underestimate these errors and overstate rendering reliability, motivating calibration to a prescribed coverage level. In this paper, we propose QuantileGS, a post-hoc framework that combines learned rendering-error quantiles with scale-normalized conformal calibration to produce spatially adaptive error bounds. The framework comprises three phases. Phase 1, Rendering-Error Computation, measures RGB mean absolute error between observed images and predictions from a frozen 3DGS model. Phase 2, Ordered Gaussian Quantile Fields, learns two scalar attributes per Gaussian to predict lower and upper rendering-error quantiles. Phase 3, Scale-Normalized Conformal Calibration, calibrates the upper prediction on held-out images, using the quantile gap to scale the correction. Under the stated assumptions, the resulting bounds provide finite-sample marginal coverage. At a nominal coverage level of 90%, calibration raises mean empirical test coverage from 69.6% to 89.6% on LLFF and from 80.1% to 92.1% on Mip-NeRF 360. On LF, coverage remains conservative at 96.3% before and 96.4% after calibration. Applications to active view selection, Gaussian pruning, and RGB-D simultaneous localization and mapping illustrate how these bounds inform downstream decisions.

</details>

#### 2026-11-16 - A Gaussian Primitive Data Management Framework for Efficient 3DGS Trajectory Rendering

**Authors:** Haolun Ma, Ziyi Liu, Zizhuo Xu, Chuhan Hu, Lei Li
**Links:** [abs](https://arxiv.org/abs/2611.20546) - [pdf](https://arxiv.org/pdf/2611.20546)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Gaussian Primitive Data Management Framework for Efficient 3DGS Trajectory Rendering
- 作者：Haolun Ma, Ziyi Liu, Zizhuo Xu, Chuhan Hu, Lei Li
- 出版日期：2026-11-16T05:25:24Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.20546) / [PDF](https://arxiv.org/pdf/2611.20546)

### 一句话总结
论文将结构化 3DGS 的轨迹渲染视为空间数据管理问题，提出 GDM-GS，通过在视图内、跨视图、跨处理器三个层面消除冗余，降低轨迹渲染延迟并保持图像质量。

### 研究问题
轨迹渲染需要沿相机路径逐视图渲染重建 3D 场景的新视图，是数字孪生和自主巡检中的核心操作。结构化 3DGS 虽能通过按需解码稀疏锚点实时渲染单视图，但逐视图渲染轨迹时存在三类冗余：每个视图都要投影全部锚点进行选择；相邻视图已请求的锚点会被重复解码；所有步骤都在 GPU 上运行而 CPU 空闲。摘要未提供足够信息说明现有方法在具体场景规模、延迟量级或内存占用方面的详细瓶颈数据。

### 核心思路/方法
作者将锚点视为空间对象、视图视为范围查询、解码后的高斯视为共享派生数据，提出 GDM-GS，在三个层面去除冗余：
1. **视图内**：使用锚点索引和遮挡物索引，将每个视图作为带洞视锥范围查询处理，使视野外和可证明被遮挡的锚点不被解码。
2. **跨视图**：采用共享物化，对一组连续视图中的每个被请求锚点只解码一次，同时保留每个视图自身的选择结果。
3. **跨处理器**：采用混合流水线，在有界内存下先将选择任务在 CPU 与 GPU 之间平衡，再进行分组解码。

### 主要贡献
- 将结构化 3DGS 的轨迹渲染重新表述为空间数据管理问题，明确锚点、视图查询和解码高斯之间的对应关系。
- 提出 GDM-GS 框架，从视图内、跨视图、跨处理器三个层面消除冗余解码与计算。
- 摘要称在大规模公开场景上的实验表明，GDM-GS 在保持图像质量的同时显著降低轨迹渲染延迟；具体数据集、对比方法和量化指标摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法对非结构化 3DGS、动态场景或极端相机路径的适用性。
- 摘要未提供足够信息说明遮挡索引的构建成本、更新代价及其在复杂遮挡场景下的准确性。
- 摘要未提供足够信息说明有界内存的具体约束、CPU/GPU 负载划分策略的鲁棒性以及跨平台实现细节。
- 摘要仅给出“显著降低延迟”的定性结论，未提供具体延迟、吞吐、内存占用或图像质量指标的数值。
- 摘要未提供足够信息说明与现有轨迹渲染加速方法的直接对比结果。

### 阅读优先级
中。理由：论文针对 3DGS 轨迹渲染中的重复解码与处理器闲置问题提出了清晰的三层冗余消除框架，问题定义具有实际应用背景；但摘要未给出量化实验结果、对比基线细节和局限讨论，是否值得深入阅读需结合全文的实验充分性与方法适用性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Trajectory rendering, which renders novel views of a reconstructed 3D scene along a camera path, is a core operation in digital twins and autonomous inspection. Structured 3D Gaussian Splatting (3DGS) renders a single view in real time by decoding sparse anchors into Gaussians on demand, but it renders a trajectory view by view: every view projects all anchors to select them, re-decodes anchors already requested by neighboring views, and runs all steps on the GPU while the CPU idles. We treat this as a spatial data management problem, where anchors are spatial objects, views are range queries, and decoded Gaussians are shared derived data, and propose GDM-GS, which removes redundancy at three levels. Within a view, an anchor index and an occluder index answer each view as a holed-frustum range query, so out-of-view and provably hidden anchors are never decoded. Across views, shared materialization decodes each requested anchor once per group of consecutive views while preserving each view's selection. Across processors, a hybrid pipeline balances selections between the CPU and the GPU before grouped decoding under bounded memory. Experiments on large-scale public scenes show that GDM-GS substantially reduces trajectory rendering latency while preserving image quality.

</details>

#### 2026-11-12 - TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models

**Authors:** Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe, Min-Hung Chen, Yu-Chiang Frank Wang, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu, Cheng Sun
**Links:** [abs](https://arxiv.org/abs/2611.17331) - [pdf](https://arxiv.org/pdf/2611.17331)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** view synthesis, rendering, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models
- 作者：Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe, Min-Hung Chen, Yu-Chiang Frank Wang, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu, Cheng Sun
- 出版日期：2026-11-12T18:59:52Z
- 分类：Neural Scene Representations & Rendering（次要分类：摘要未提供）
- 链接：摘要页 https://arxiv.org/abs/2611.17331 ；PDF https://arxiv.org/pdf/2611.17331 ；项目页 https://test-time-baking.github.io

### 一句话总结
论文提出 Test-Time Baking（TTB），把仅解码器视图合成模型中的跨视图注意力映射“烘焙”进轻量 MLP，从而在保持高保真渲染质量的同时显著提升渲染效率。

### 研究问题
论文关注仅解码器的大规模视图合成模型（LVSMs）的效率问题：这类模型借助 KV-cache，在不重建三维几何的情况下从神经网络回归新视图，并达到先进质量；而 Test-Time Training（TTT）层虽然节省计算，却牺牲质量。因此，核心问题是：能否在不牺牲渲染质量的前提下，获得接近 TTT 的渲染效率。

### 核心思路/方法
TTB 的基本做法是学习把跨视图注意力中的全局场景信息烘焙进一个轻量 MLP，以支持快速、高保真的新视图解码。其两个关键设计如下：

1. **重新利用 TTT 的 fast-weight MLP**：不是用其完全替代注意力，而是让其从输入—输出对中显式学习跨视图注意力映射。这样可达到与 TTT 相同的渲染效率，同时显著提高质量。
2. **处理模态错位问题**：针对 context prefilling 与新视图渲染之间的模态错位，将 context tokens 解耦为两类——仅含相机信息的 context rendering tokens 作为 TTB 输入；含图像内容的 context ground-truth tokens 作为 TTB 映射目标。由此使被烘焙的 MLP 不必承担 context 与新视图处理之间的模态泛化挑战。

### 主要贡献
- 提出 Test-Time Baking（TTB）策略，将跨视图注意力中的全局场景信息烘焙进轻量 MLP，实现快速且高保真的新视图解码。
- 通过重新利用 TTT 的 fast-weight MLP 显式学习跨视图注意力映射，在保持 TTT 级渲染效率的同时显著提升质量。
- 通过解耦 context tokens（相机-only 渲染 tokens 作为输入、含图像内容的目标 tokens 作为映射目标），缓解 context prefilling 与新视图渲染之间的模态错位。
- 摘要称方法在多个基准上实现最高 **23x** 渲染加速，质量与当前最先进方法相当。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、适用场景边界、额外训练开销、对特定模型架构的依赖程度，也未给出各基准的详细定量结果与消融实验。

### 阅读优先级
**高**。理由：论文直接针对仅解码器视图合成模型的渲染效率与质量权衡，提出明确的“烘焙”思路与两项关键技术设计，并报告最高 23x 加速且质量与 SOTA 相当；对关注高效神经渲染、视图合成加速及 TTT 替代方案的研究者有较强相关性。但具体实验细节与泛化性需查阅原文确认。

</details>

<details>
<summary>Abstract</summary>

Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking (TTB), a strategy that learns to bake global scene information from cross-view attention into a lightweight MLP, enabling fast and high-fidelity novel-view decoding. The first key is to repurpose the fast-weight MLP of TTT to learn the cross-view attention mapping explicitly from its input-output pairs, rather than replacing attention entirely, achieving the same rendering efficiency as TTT while delivering substantially higher quality. The second key addresses a modality misalignment between context prefilling and novel-view rendering: we disentangle context tokens into camera-only context rendering tokens to serve as TTB input, and context ground-truth tokens with image content to serve as the TTB mapping target, ensuring the baked MLPs are relieved of the modality generalization challenge between context and novel-view processing. Our method achieves up to **23x** rendering speedup with quality on par with the state-of-the-art across several benchmarks. Project page: https://test-time-baking.github.io

</details>

#### 2026-11-12 - Learning the Missing Derivative: Neural Multiple-Scattering Operators for Inverse Volume Rendering

**Authors:** Sipeng Chen, Shibo Li
**Links:** [abs](https://arxiv.org/abs/2611.16650) - [pdf](https://arxiv.org/pdf/2611.16650)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning the Missing Derivative: Neural Multiple-Scattering Operators for Inverse Volume Rendering
- 作者：Sipeng Chen, Shibo Li
- 出版日期：2026-11-12T11:27:20Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.16650) ｜ [PDF](https://arxiv.org/pdf/2611.16650)

### 一句话总结
论文用神经算子预测多重散射场，并在逆渲染中对它求导，以替代冻结源断层成像中被丢弃的导数项和可微路径追踪中昂贵且噪声较大的采样估计。

### 研究问题
从照片重建光学厚介质时，需要建模多重散射及其对消光变化的响应。冻结源断层成像忽略了这一导数；可微路径追踪虽能估计该导数，但依赖昂贵、带噪的采样。因此，问题在于：如何在逆渲染中高效获得多重散射对消光变化的导数。

### 核心思路/方法
- 用神经算子预测多重散射场，并在逆渲染过程中通过该算子进行微分；透射率和单次散射则直接计算。
- 针对优化过程中的关键问题：一个在留出介质上能准确预测散射场的算子，在优化器实际访问的密度状态下仍可能给出较差的导数。
- 解决方式：在由该算子驱动的逆过程所产生的状态上做微调，并使用蒙特卡洛散射场监督。
- 在留出的光学厚云数据上评估重光照效果；与冻结源断层成像在相同时间下比较，与可微路径追踪在给予后者显著更多时间时比较。

### 主要贡献
- 提出以神经算子预测多重散射场并对该算子求导的逆体渲染方法，避免冻结源近似丢弃导数，也避免依赖可微路径追踪的高成本噪声采样。
- 识别并处理“预测场准确但优化访问状态处导数不佳”的问题，通过在逆过程生成状态上微调并使用蒙特卡洛散射场监督。
- 摘要报告：在留出的光学厚云上，同等时间下重光照优于冻结源断层成像；在可微路径追踪获得显著更多时间时优于后者；在逆轨迹上训练还改善了访问状态处的导数对齐并减少优化漂移。

### 局限性
- 摘要未提供足够信息说明方法在大规模场景、复杂材质或非云介质上的泛化能力。
- 摘要未提供足够信息说明微调阶段所需的蒙特卡洛监督成本、训练数据规模及对优化器设置的敏感性。
- 摘要未提供足够信息给出定量指标、误差分析或失败案例。

### 阅读优先级
中。理由：该工作聚焦逆体渲染中多重散射导数建模这一明确问题，方法思路与评估对比在摘要中较清晰；但摘要未给出定量结果和细节，是否值得深入阅读取决于对神经算子、逆体渲染及光学厚介质重光照的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Reconstructing optically thick media from photographs requires modeling multiple scattering and its response to changes in extinction. Frozen-source tomography discards this derivative; differentiable path tracing estimates it through expensive, noisy sampling. We instead predict the multiple-scattering field with a neural operator and differentiate through it during inverse rendering, while computing transmittance and single scattering directly. A further challenge arises during optimization: an operator that predicts the field accurately on held-out media can still produce poor derivatives at the density states visited by the optimizer. We address this by fine-tuning on states generated during inversions driven by the operator, using Monte Carlo scattering-field supervision. On held-out optically thick clouds, our method improves relighting over frozen-source tomography at equal time and outperforms differentiable path tracing given substantially more time. Training on inversion trajectories also improves derivative alignment at visited states and reduces optimization drift.

</details>

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-17 - Code World Model 2.0: Towards Infinite Controllable Video Generation

**Authors:** Ruoyu Wang, Hao Zhong, Yanming Yang, Jiahao Tian, Lin Liu, Biao Gong, Guoshan Lu, Yiding Tian, Chunhua Shen, Zhenzhong Lan, Chi Zhang
**Links:** [abs](https://arxiv.org/abs/2611.22925) - [pdf](https://arxiv.org/pdf/2611.22925)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>Abstract</summary>

Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming. Yet a practical renderer must address two challenges. Upstream proxies vary from coarse layouts to fine articulated geometry depending on the interaction, and streaming inference must operate in a few causal steps without accumulating drift across self-generated history. We present Invoker-Render, pairing a bidirectional creation model with a causal four-step streaming model under a shared conditioning interface over structural proxies, an appearance reference, and language. Trained on an aligned approximately 200-hour multi-granularity corpus, Invoker-Render honors fine geometric constraints when supplied while synthesizing plausible local motion under coarse proxies, enabling runtime selection of input detail. To bridge bidirectional creation and real-time streaming without compounding step compression and rollout drift, we introduce Progressive Forcing (ProForcing). ProForcing first trains a causal predictor and distills it into a four-step renderer using histories derived from training videos. Training then shifts to continuous self-generated rollouts. A pipelined serving stack supports efficient streaming inference. Experiments show versatile control across proxy families, granularities, and camera paths, consistent gains over recent streaming baselines, and stable 30-minute racing rollouts that preserve scene and subject appearance.

</details>

#### 2026-11-17 - Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, Chao Ma
**Links:** [abs](https://arxiv.org/abs/2611.22880) - [pdf](https://arxiv.org/pdf/2611.22880)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, driving scene, world model, world modeling

<details>
<summary>Abstract</summary>

Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible, they preserve many driving-irrelevant appearance details, i.e., only a small portion of the tokens directly encode critical planning-relevant factors, such as agent geometry, motion dynamics, and interactions. This introduces a significant performance bottleneck. An important question thus arises: what world state should a world VLA model reason over to support planning beyond pixel-level prediction? We argue that planning-oriented world modeling should focus on a compact and structured agent-centric latent state that captures the interactions between objects in the driving scene over time. As such, we introduce AgentWorld, an agent-centric VLA world model that uses discrete agent tokens jointly for reasoning and trajectory planning. Each token is dynamically grounded to a surrounding agent associated with its object's state, such as semantic identity, 3D geometry, motion, and interaction context. AgentWorld learns these tokens through three key processes: explicit geometric grounding, reasoning-oriented supervised fine-tuning, and agent-oriented reinforcement learning. Extensive open-loop and closed-loop experiments under diverse driving scenarios show that AgentWorld enhances planning capabilities, fully exploits visual evidence and agent dynamics, and yields interpretable agent-centric world states.

</details>

#### 2026-11-17 - Network-Exposed Configuration Attacks on LLM-Controlled Social Robots

**Authors:** Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung, Quang Dan Le, Hong Qing Yu
**Links:** [abs](https://arxiv.org/abs/2611.22761) - [pdf](https://arxiv.org/pdf/2611.22761)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, mapping

<details>
<summary>Abstract</summary>

Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings and the cloud LLM's system prompt through a management interface, without adversarial conversational input. Eleven prompt-injection attempts across five categories were reported as resisted, whereas both configuration-layer attack paths produced observable behavioural changes on physical hardware. We demonstrate local and network-adjacent access, mapping the weakness to CWE-306 (Missing Authentication for a Critical Function) and CWE-1327 (Binding to an Unrestricted IP Address), with a reported CVSS v3.1 score of 6.5 (Medium). A configuration endpoint also accepts cross-origin requests without a CORS preflight (CWE-352; 6.5 Medium), while the persistent-memory sink stores content without enforcing its stated restrictions. A source review of 59 public repositories identifies missing authentication in 10 of 11 source-verifiable genuine applications, or 11 of 11 including a framework-default case. These findings indicate recurrence within the sampled repositories, not prevalence in commercial products. We characterise a deployment gap between developer-oriented network assumptions and consumer-facing embodied AI security: inference-layer refusal cannot prevent unauthorised changes to model instructions. Potential consequences include surveillance through onboard cameras and microphones and social engineering of nearby users. Proof-of-concept code, evidence and the survey are available at https://bit.ly/reachypi.

</details>

#### 2026-11-17 - CascadeJEPA: Enhancing 3D Geometric Representations via Spatially Coupled Cascaded Prediction

**Authors:** Kailai Zhou, Ziqi Chen, Xiaoning Xu, Yuefeng Wu, Zixuan Fu, Zijun Lin, Zhihao Li, Youwei Pang, Xiaoqi Zhao, Xun Cao, Bihan Wen
**Links:** [abs](https://arxiv.org/abs/2611.22686) - [pdf](https://arxiv.org/pdf/2611.22686)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) have emerged as a promising paradigm for predictive visual representation learning. However, our analysis of I-JEPA reveals a growing discrepancy between semantic and geometric learning: improved semantic recognition during pretraining is accompanied by degraded 3D geometric representations. We hypothesize that this partly stems from predicting highly abstract latent representations with incomplete spatial context, favoring semantic regularities over fine-grained geometric information. To address this issue, we introduce CascadeJEPA, a spatially coupled cascaded prediction framework that promotes richer patch-level interactions through full-grid context encoding and cross-attention between prediction stages, while largely preserving the original I-JEPA architecture. Extensive experiments demonstrate substantial improvements over I-JEPA across multiple 3D geometric tasks while maintaining strong semantic recognition performance. Furthermore, its advantages extend to future feature forecasting and world model planning, highlighting the potential of enhanced geometric representations to support predictive world modeling.

</details>

#### 2026-11-17 - InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation

**Authors:** Chen Zhao, Zipeng Ye, Shifeng Bao, Yihan Lin, Haitao Shen, Yining Luo, Yuchen Xie, Jing Zhang
**Links:** [abs](https://arxiv.org/abs/2611.22584) - [pdf](https://arxiv.org/pdf/2611.22584)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>Abstract</summary>

Existing agentic manipulation systems treat pretrained vision-language-action (VLA) policies as opaque, language-only primitives: when a policy call fails under unfamiliar instructions or scene perturbations, the agent cannot steer its behavior and is forced into futile retries or costly manual takeover. We present InteractVLA, a framework that turns pretrained flow-based VLAs into geometrically steerable and inspectable tools through a bidirectional geometric interface with vision-language agents. In the forward direction, test-time geometric guidance translates an agent-specified end-effector target into input gradients through the action expert via a differentiable command-to-pose mapping, while soft-time target alignment treats arrival time as a latent execution index to match the target pose without distorting the policy's approach motion. In the reverse direction, action-informed agentic refinement exposes generated action chunks and calibrated camera reprojections back to the agent, allowing it to diagnose spatial discrepancies, revise targets for subsequent VLA calls, or locally adjust motion segments on top of the guided trajectory. Making the VLA controllable not only boosts online agentic tool use, but also unlocks effective recursive self-improvement (RSI), achieving state-of-the-art performance of 99.4\% on LIBERO-Plus, 48.62\% on RoboDojo, and 89.4\% on RoboCasa365. Project page: https://lingwupro.github.io/InteractVLA/.

</details>

#### 2026-11-17 - Inertial Video World Models

**Authors:** Yuan Gao, Fan Xu, Yu Guo, Yuxu Lu, Zhengru Fang, Hao Wu, Xiaomeng Huang
**Links:** [abs](https://arxiv.org/abs/2611.22314) - [pdf](https://arxiv.org/pdf/2611.22314)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world model

<details>
<summary>Abstract</summary>

The physical world has inertia: it evolves from what already exists rather than being recreated at every instant. However, many existing video world models lack an explicit mechanism for inertial state evolution, leaving the continuity of motion and structure implicit in video prediction. During autoregressive rollouts, repeated reconstruction can accumulate errors and destabilize the predicted dynamics. To address this limitation, we introduce InertialWorld, an Inertial Video World Model that makes inertia a structural prior for autoregressive prediction: existing scene evidence is carried across time rather than reconstructed at every step. Central to this formulation is Inertial Memory, which turns memory from passive predictive context into an evolving video state with two complementary views: a dense Eulerian grid preserves scene-aligned evidence, while persistent Lagrangian carriers bind local content to learned canonical coordinates. At each step, the model transports the carrier content according to action-conditioned motion, predicts the complete next video state from the transported carriers and dense grid, and uses a learned gate to combine transported and newly predicted content into the memory for the next step. Extensive experiments across multiple domains, including robot manipulation, 3D game simulation, and open-world navigation, demonstrate that InertialWorld achieves competitive autoregressive prediction performance against strong video world model baselines. Codes link: https://github.com/YuanGao-YG/InertialWorld

</details>

#### 2026-11-16 - From Human Videos to Bimanual Dexterous Manipulation Data: Confidence-Guided RL Refinement of Video Priors

**Authors:** Yanghong Liu, Yang Chen, Kailang Xu, Bang Du, Feiyang Yang, Jiawei Xia, Zhengtao Yao, Yubiao Zhang, Masayoshi Tomizuka, Ruihai Wu, Wei Zhan
**Links:** [abs](https://arxiv.org/abs/2611.21908) - [pdf](https://arxiv.org/pdf/2611.21908)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Collecting demonstrations for bimanual dexterous manipulation is costly, motivating the use of human videos as a source of robot training data. However, uncertainty in video-derived motion estimates and differences between human and robot embodiments make direct motion transfer challenging. In this work, we introduce PriDex, a framework that transforms human-video Priors into executable robot Dexterous manipulation demonstrations through reinforcement learning in simulation. PriDex preserves task-relevant interaction structure while allowing embodiment-specific behavior to be regenerated for the robot. Human-object interactions provide affordance cues for selecting task-relevant, robot-specific grasps from geometry-based candidates. For motion refinement, object trajectories provide a task-level reference, while relative bimanual wrist trajectories offer complementary guidance for coordinated motion. Since object-motion estimates can become unreliable under occlusion or visual ambiguity, PriDex uses object-motion confidence to adaptively balance these two priors, emphasizing object-level guidance when confidence is high and increasing the contribution of wrist-level guidance as confidence decreases. Reinforcement learning refines these video-derived priors under the robot's kinematic and physical constraints, and the resulting policies are rolled out to generate robot demonstrations for training a vision-based diffusion policy. We evaluate PriDex on four bimanual dexterous manipulation tasks, including pouring, sweeping into a dustpan, bottle-cap unscrewing, and plate cleaning, assessing both simulation-based robot data generation and downstream visuomotor policy learning.

</details>

#### 2026-11-16 - Non-Imaging Optical Tactile Sensors for Robotics: Transduction Principles, System Integration, and Robotic Applications

**Authors:** Hao Wu, Yu Feng, Haotian Guo, Huichan Zhao, Changsheng Wu, Jianshu Zhou
**Links:** [abs](https://arxiv.org/abs/2611.20770) - [pdf](https://arxiv.org/pdf/2611.20770)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Non-Imaging Optical Tactile Sensors for Robotics: Transduction Principles, System Integration, and Robotic Applications
- 作者：Hao Wu, Yu Feng, Haotian Guo, Huichan Zhao, Changsheng Wu, Jianshu Zhou
- 出版日期：2026-11-16T09:20:51Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2611.20770) ｜ [PDF](https://arxiv.org/pdf/2611.20770)

### 一句话总结
本文是一篇面向机器人应用的非成像光学触觉传感器综述，提出将机械载荷传递、光学编码、读出与触觉推断统一关联到机器人任务需求的框架，并据此讨论多类器件与评估要点。

### 研究问题
摘要指出，非成像光学触觉传感器通过光强、波长、光谱或光子计数变化来编码接触，具有多样架构；其有用性取决于两点：一是接触变量能否在耦合的力学与环境效应下被可靠区分，二是所得信息能否及时传递以指导动作。因此，综述需要回答：如何在一个统一框架下理解从机械载荷到光学编码、读出与触觉推断的链路，并如何依据机器人任务需求评估这些传感器。

### 核心思路/方法
本文采用综述方式，建立一个统一框架，将机械载荷传递、光学编码、读出和触觉推断与机器人任务要求相连接。摘要说明，综述考察的器件类型包括：反射式与波导式器件、微/纳米纤维、光纤光栅、干涉与谐振结构，以及机械致发光复合材料。分析围绕三点展开：第一，高光学灵敏度只有在相关接触与标定条件下目标变量仍可辨识时，才能支持准确的触觉估计；第二，空间覆盖与反馈时序需要在系统层面评估，需考虑复用、采集、解调与推断；第三，器件表征、离线识别与闭环机器人性能提供不同层级的证据，需要不同的评价标准。摘要还提到，代表性研究用于说明这些考虑如何影响力估计、接触定位、滑移校正与分布式交互。

### 主要贡献
- 提出一个统一框架，将机械载荷传递、光学编码、读出与触觉推断同机器人任务需求关联起来。
- 系统梳理多类非成像光学触觉传感器件，包括反射式与波导式器件、微/纳米纤维、光纤光栅、干涉与谐振结构、机械致发光复合材料。
- 归纳三项跨方法的关键考量：目标变量可辨识性、系统级空间覆盖与反馈时序、以及不同证据层级对应不同评价标准。
- 通过代表性研究说明上述考量对力估计、接触定位、滑移校正和分布式交互的影响。
- 提出后续优先方向：标定迁移、可靠接口、可扩展读出与基于任务的验证，为选择和开发面向机器人的非成像光学触觉架构提供依据。

### 局限性
- 摘要未提供足够信息说明综述的文献检索范围、纳入与排除标准、文献数量或时间覆盖范围。
- 摘要未提供足够信息说明对各器件类型的定量比较结果或性能基准。
- 摘要未提供足够信息说明所提出框架的验证方式或具体案例细节。
- 摘要未提供足够信息说明作者对各类架构优缺点的完整结论；仅能确认摘要中提及的三项考量与后续优先方向。

### 阅读优先级
高。理由：该文是综述，直接面向机器人非成像光学触觉传感器的传感原理、系统集成与应用评估，并明确提出标定迁移、可靠接口、可扩展读出与任务级验证等优先方向；对于关心触觉传感架构选型与系统级评估的研究者具有较高的参考价值。摘要未提供足够信息判断其文献覆盖广度与定量对比深度，因此优先级判断仅基于摘要所述框架与议题的相关性。

</details>

<details>
<summary>Abstract</summary>

Non-imaging optical tactile sensors encode contact through changes in optical intensity, wavelength, spectra, or photon counts, offering diverse architectures for robotic touch. Their usefulness depends on whether contact variables can be reliably distinguished from coupled mechanical and environmental effects, and whether the resulting information can be delivered in time to guide action. This review develops a unified framework linking mechanical load transmission, optical encoding, readout, and tactile inference to robotic task requirements. It examines reflective and waveguide-based devices, micro/nanofibers, fiber gratings, interferometric and resonant structures, and mechanoluminescent composites. Three considerations emerge across these approaches. First, high optical sensitivity supports accurate tactile estimation only when target variables remain identifiable under the relevant contact and calibration conditions. Second, spatial coverage and feedback timing must be assessed at the system level, accounting for multiplexing, acquisition, demodulation, and inference. Third, device characterization, offline recognition, and closed-loop robotic performance provide distinct levels of evidence and require different evaluation criteria. Representative studies illustrate how these considerations shape force estimation, contact localization, slip correction and distributed interaction. This review concludes with priorities for calibration transfer, reliable interfaces, scalable readout, and task-based validation, providing a basis for selecting and developing non-imaging optical tactile architectures for robotics.

</details>

#### 2026-11-16 - Vision-Language Grounded Semantic Navigation for Autonomous Mobile Robots

**Authors:** Ravindran Vasoor Saravanan, Chittin Varunav Ravi, Madhumita Singh, Thirulok Sundar Mohan Rasu
**Links:** [abs](https://arxiv.org/abs/2611.20558) - [pdf](https://arxiv.org/pdf/2611.20558)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Vision-Language Grounded Semantic Navigation for Autonomous Mobile Robots
- 作者：Ravindran Vasoor Saravanan, Chittin Varunav Ravi, Madhumita Singh, Thirulok Sundar Mohan Rasu
- 出版日期：2026-11-16T05:38:50Z
- 分类：主分类 Embodied / Robotics / AR Applications；次级分类：摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.20558 ；PDF https://arxiv.org/pdf/2611.20558

### 一句话总结
该论文构建了一个基于 ROS2 的完整系统，在仿真中将开放词汇目标检测、深度定位、语义建图与经典导航流程结合，使移动机器人能够按自然语言指令导航到指定物体。

### 研究问题
语言引导导航要求移动机器人在非结构化环境中理解自然语言命令并前往用户指定目标。论文关注的问题是：如何把开放词汇视觉感知与用于建图和导航的经典机器人流程整合起来，构建端到端的视觉语言接地导航系统，并分析其可行性与限制。

### 核心思路/方法
论文提出一个基于 ROS2 的完整系统，集成以下模块：
- 基于前沿（frontier-based）的探索；
- 使用 Grounding DINO 的开放词汇目标检测；
- 基于深度的 3D 定位；
- 语义建图。

系统接收类似“go to the yellow box”的自然语言命令，用文本提示从 RGB 图像中检测候选物体，估计其在世界坐标系中的位置，并生成由 Nav2 导航栈执行的目标点。论文在 Gazebo 室内环境中使用 TurtleBot3 机器人进行验证，系统无需任务特定训练。

### 主要贡献
- 提出一个集成了前沿探索、开放词汇检测、深度 3D 定位、语义建图和 Nav2 导航的 ROS2 端到端系统，用于仿真中的视觉语言接地导航。
- 系统能够根据自然语言命令检测候选物体、估计世界坐标位置并生成导航目标，且无需任务特定训练。
- 在 Gazebo 室内环境中使用 TurtleBot3 进行了初步验证：系统自主探索房间，检测到五个目标物体中的三个，并成功执行了测试的两个自然语言导航命令。
- 结果表明确认开放词汇接地模型可以集成到经典导航流程中，同时指出检测不确定性、基于深度的定位误差和探索覆盖不完整是当前限制。

### 局限性
- 摘要明确指出性能受检测不确定性、基于深度的定位误差以及探索覆盖不完整限制。
- 实验规模较小：仅检测到五个目标物体中的三个；执行了两个自然语言导航命令。
- 验证仅在 Gazebo 仿真环境中进行，使用 TurtleBot3 与轻量级、仅 CPU 架构；真实环境表现摘要未提供足够信息。
- 具体的检测精度、定位误差量化和导航成功率等详细实验指标：摘要未提供足够信息。

### 阅读优先级
中。理由：该工作围绕开放词汇感知与经典 ROS2 导航流程的集成，问题定义清晰，且明确报告了初步仿真验证与限制，适合关注视觉语言导航系统集成与轻量级部署的研究者参考；但摘要显示实验规模较小、仅在仿真中验证，且缺少详细定量结果，因此不属于必须优先精读的突破性工作。

</details>

<details>
<summary>Abstract</summary>

Language-guided navigation enables mobile robots to interpret natural language commands and navigate toward user-specified targets in unstructured environments. However, integrating open-vocabulary visual perception with classical robotics pipelines for mapping and navigation remains a challenging problem. In this work, we present a complete ROS2-based system that combines frontier-based exploration, open-vocabulary object detection using Grounding DINO, depth-based 3D localization, and semantic mapping to enable end-to-end vision-language grounded navigation in simulation. The system accepts natural language commands such as ``go to the yellow box,'' detects candidate objects from RGB images using text prompts, estimates their positions in the world frame, and generates navigation goals executed by the Nav2 stack. In a Gazebo-based indoor environment with a TurtleBot3 robot, the system autonomously explored the room, detected three of the five target objects, and successfully executed both natural language navigation commands tested, without task-specific training. The results indicate that open-vocabulary grounding models can be integrated into classical navigation pipelines, though performance is limited by detection uncertainty, depth-based localization error, and incomplete exploration coverage. These findings highlight both the feasibility and current limitations of deploying vision-language grounded navigation systems using lightweight, CPU-only architectures.

</details>

#### 2026-11-16 - AsymEEF: Bimanual Manipulation with Asymmetric End Effectors

**Authors:** Xiaokang Sun, Ningyue Wang, Kunqi Xu, Guangqi Jiang, Jianglong Ye, Yong Wu, Xueyan Zou
**Links:** [abs](https://arxiv.org/abs/2611.20557) - [pdf](https://arxiv.org/pdf/2611.20557)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AsymEEF: Bimanual Manipulation with Asymmetric End Effectors
- 作者：Xiaokang Sun, Ningyue Wang, Kunqi Xu, Guangqi Jiang, Jianglong Ye, Yong Wu, Xueyan Zou
- 出版日期：2026-11-16T05:36:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.20557) / [PDF](https://arxiv.org/pdf/2611.20557)

### 一句话总结
AsymEEF 提出一个面向双臂异构末端执行器的框架，用少量源数据生成可执行演示，并学习统一的双臂视觉运动策略。

### 研究问题
遥操作演示采集成本高，且在不同运动学和动作空间的末端执行器之间难以复用；在双臂操作中，每种末端执行器组合可能都需要重新采集数据，负担进一步加重。论文关注如何在无需额外遥操作的条件下，将演示迁移到二指、三指和五指末端执行器的异构组合，并支持统一的双臂策略学习。

### 核心思路/方法
给定小型源数据集，AsymEEF 将演示迁移到两个末端执行器的异构组合。方法包含两部分监督：运动学教师锚点提供几何监督，稀疏真实世界 X-Calib 锚点用于纠正抓取执行差异。模型使用共享编码器将腕部位姿和执行器状态映射到与形态无关的潜在空间，再由形态条件解码器重建目标命令。生成的轨迹经过回放过滤以保证任务级可执行性。该表示还支持跨多组末端执行器对训练统一的双臂视觉运动策略。

### 主要贡献
- 提出 AsymEEF 框架，实现跨末端执行器的可执行演示生成和统一双臂策略学习。
- 支持将小规模源数据迁移到二指、三指、五指末端执行器的异构双臂组合，无需额外遥操作。
- 结合运动学教师锚点与稀疏真实世界 X-Calib 锚点，分别提供几何监督和抓取执行纠正。
- 设计形态无关潜在空间与形态条件解码器，并对生成轨迹进行回放过滤。
- 摘要报告：在四个仿真和六个真实世界任务中，回放成功率优于适配后的迁移基线；仿真中平均回放有效扩展增益为 16.6 倍；并在真实机器人上进行下游策略训练评估。

### 局限性
摘要未提供足够信息说明方法在极端形态差异、接触丰富任务或大规模数据条件下的表现；也未给出真实世界任务的定量成功率、策略泛化边界、失败案例及计算成本等细节。摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直接针对双臂操作中跨异构末端执行器的演示复用与统一策略学习问题，问题定义清晰，且摘要给出了仿真与真实机器人任务上的评估结果；对关注机器人演示迁移、双臂操作和形态泛化策略的研究者有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Teleoperated demonstrations are costly to collect and rarely reusable across end-effectors with different kinematics and action spaces. This burden grows in bimanual manipulation, where each end-effector pair may require new data. We present AsymEEF, a framework for executable cross-end-effector demonstration generation and unified bimanual policy learning. Given a small source dataset, AsymEEF transfers demonstrations to heterogeneous combinations of two-, three-, and five-fingered end-effectors without additional teleoperation. Kinematic teacher anchors provide geometric supervision, while sparse real-world X-Calib anchors correct discrepancies in grasp execution. A shared encoder maps wrist poses and actuator states to a morphology-agnostic latent space, and a morphology-conditioned decoder reconstructs target commands. Generated trajectories undergo replay filtering for task-level executability. The representation also supports a unified bimanual visuomotor policy trained across multiple pairs. Across four simulated and six real-world tasks, AsymEEF improves replay success over adapted transfer baselines, achieves a mean replay-valid expansion gain of 16.6 times in simulation, and is evaluated through downstream policy training on real robots. Project website: https://asymeef.vercel.app/.

</details>

#### 2026-11-15 - Radar Panoptic Transformer: Semantic-Guided Mask Queries for Dynamic Scene Understanding

**Authors:** Mayank Mayank, Bharanidhar Duraisamy, Rohit Mohan, Abhinav Valada
**Links:** [abs](https://arxiv.org/abs/2611.20203) - [pdf](https://arxiv.org/pdf/2611.20203)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Radar Panoptic Transformer: Semantic-Guided Mask Queries for Dynamic Scene Understanding
- 作者：Mayank Mayank, Bharanidhar Duraisamy, Rohit Mohan, Abhinav Valada
- 出版日期：2026-11-15T18:59:54Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.20203) / [PDF](https://arxiv.org/pdf/2611.20203)

### 一句话总结
提出端到端点级网络 RPT，用语义引导的掩码查询与雷达自适应特征提取，在稀疏非均匀车载雷达点云上做全景分割，并在 RadarScenes 与 MAN TruckScenes 上报告了领先结果与实时推理速度。

### 研究问题
车载雷达具备长距离感知与直接多普勒速度测量能力，但其点云稀疏且非均匀采样，给全景分割带来显著挑战；动态物体往往只有少量检测点，且淹没在占主导的静态背景中，可用于区分物体实例的几何线索因此受到限制。论文旨在解决这一雷达点云全景分割问题。

### 核心思路/方法
- 提出 Radar Panoptic Transformer（RPT），一个端到端的基于点的网络，结合雷达自适应特征提取与语义引导的掩码预测。
- 主干网络通过分组向量注意力聚合姿态对齐的时序上下文，并学习以距离、方位角和雷达截面积（RCS）为条件的逐点邻域半径。
- 利用逐点语义预测在可能的前景点处初始化查询，并通过查询—点类别一致性引导掩码交叉注意力，从而在不依赖几何聚类的情况下生成实例掩码。
- 引入辅助的 RCS 一致性损失，使预测实例与标注实例在实例级统计量上保持一致。

### 主要贡献
- 面向稀疏、非均匀车载雷达点云，提出语义引导掩码查询的端到端全景分割网络 RPT。
- 设计雷达自适应主干：分组向量注意力聚合时序上下文，并按距离、方位角、RCS 学习逐点邻域半径。
- 以逐点语义初始化查询并引导掩码交叉注意力，避免几何聚类式实例生成；同时引入 RCS 一致性损失约束实例级统计。
- 在 RadarScenes 上报告 71.6% mIoU 与 82.2% PQ 的最先进性能；在 MAN TruckScenes 的长距离、全环绕雷达设置（感知范围至 230 m）中优于所评估的基线。
- 在 RadarScenes 上实现 31 Hz 的实时端到端推理，超过传感器帧率。

### 局限性
- 摘要未提供足够信息说明具体实验设置、对比基线细节、消融实验以及失败案例。
- 摘要未提供足够信息说明方法在极端稀疏、恶劣天气或不同雷达配置下的泛化表现。
- 摘要未提供足够信息说明 RCS 一致性损失各项的独立影响与计算开销分解。

### 阅读优先级
高。理由：该论文直接针对车载雷达点云稀疏、动态实例线索不足这一核心难题，提出端到端全景分割方法，并在两个数据集上报告领先精度与超过传感器帧率的实时推理，对自动驾驶与机器人感知中的雷达场景理解具有较强参考价值；但具体实验细节需阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Automotive radar provides long-range sensing and direct Doppler velocity measurements, but its sparse and non-uniformly sampled point clouds pose significant challenges for panoptic segmentation. Dynamic objects often yield only a few detections amid a dominant static background, providing limiting the geometric cues for separating object instances. We propose \emph{Radar Panoptic Transformer (RPT)}, an end-to-end point-based network that incorporates radar-adaptive feature extraction with semantic-guided mask prediction. Its backbone aggregates pose-aligned temporal context through grouped vector attention and learns per-point neighborhood radii conditioned on range, azimuth, and radar cross section (RCS). Point-wise semantic predictions initialize queries at likely foreground detections and guide masked cross-attention through query-point class agreement, producing instance masks without geometric clustering. An auxiliary RCS-consistency loss matches instance-level statistics between predicted and annotated instances. RPT achieves state-of-the-art performance on RadarScenes with $71.6\%$ mIoU and $82.2\%$ PQ. We further evaluate RPT on MAN TruckScenes, where it outperforms the evaluated baselines in a long-range, full-surround radar setting with sensing ranges up to $230\,\mathrm{m}$. RPT achieves real-time end-to-end inference at $31$\,Hz on RadarScenes, exceeding the sensor frame rate.

</details>

#### 2026-11-15 - Latent World Modeling for Point-Cloud Video Pretraining

**Authors:** Zhuoyue Zhang, Jian Liu, Jihua Zhu, Ajmal Saeed Mian
**Links:** [abs](https://arxiv.org/abs/2611.20090) - [pdf](https://arxiv.org/pdf/2611.20090)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Latent World Modeling for Point-Cloud Video Pretraining
- 作者：Zhuoyue Zhang, Jian Liu, Jihua Zhu, Ajmal Saeed Mian
- 出版日期：2026-11-15T16:06:31Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2611.20090

### 一句话总结
论文指出，点云视频的掩码建模存在信息泄漏问题，并提出 PointWM 隐世界模型；该模型只使用严格更早的上下文，预测未来帧的特征和几何，把“补全”任务变为“预测”任务，从而消除泄漏。

### 研究问题
- 掩码建模是点云视频自监督的主流范式，但论文认为，无论是 MAE 式重建掩码点，还是预测其隐特征，都存在信息泄漏：点云 token 锚定在每帧采样点上，因此在目标自身位置查询目标会暴露其几何移动到哪里。
- 对于隐预测器，随机时空掩码带来进一步捷径：每个目标两侧的可见帧允许插值而非预测，预训练任务因而退化为补全。
- 一旦隐藏目标位置，掩码隐预测器的表现仅略优于复制最后一帧。

### 核心思路/方法
- 提出 PointWM，一种隐世界模型：从严格更早的上下文预测未来帧的特征与几何，将补全转变为预测。
- 每个目标仅用其最后被观测到的位置和时间戳进行查询。
- 引入无需标注学习的隐动作（latent action），用于捕捉未来中由过去无法确定的部分。
- 在 HOI4D 动作分割任务上，以 P4Transformer 为骨干进行验证。

### 主要贡献
- 揭示点云视频掩码建模中两类信息泄漏：重建与隐预测中基于目标自身位置查询造成的泄漏，以及随机时空掩码下双侧可见帧带来的插值捷径。
- 提出 PointWM，以严格因果的早期上下文预测未来帧特征与几何，并学习无标注隐动作，构建无泄漏的预训练范式。
- 在 HOI4D 动作分割上，相比从头训练，F1@50 离线提升 24.9、严格因果推理下提升 29.1。
- 代码公开于 https://github.com/InitalZ/PointWM。

### 局限性
- 摘要仅报告 HOI4D 动作分割与 P4Transformer 骨干上的结果，未提供其他数据集、任务或骨干的验证信息。
- 隐动作的具体设计、训练目标细节与计算开销：摘要未提供足够信息。
- 与更多自监督范式的系统对比：摘要未提供足够信息。
- 离线与严格因果推理设置的完整实验配置：摘要未提供足够信息。

### 阅读优先级
中。理由：论文针对点云视频自监督预训练中的信息泄漏提出清晰的问题诊断与因果预测式替代方案，并给出显著的下游提升，适合关注点云视频表示学习与具身感知的研究者阅读；但摘要覆盖的任务与骨干较为单一，是否具有广泛适用性需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Masked modeling is the dominant self-supervised paradigm for point-cloud videos. However, it leaks the information it is meant to predict, whether it reconstructs masked points as in MAE-style methods or predicts their latent features. Because point-cloud tokens are anchored at points sampled from each frame, querying a target at its own position reveals where its geometry has moved, in reconstruction and latent prediction alike. For latent predictors, random spatio-temporal masks introduce a further shortcut, as visible frames on both sides of each target allow interpolation rather than forecasting. The pretext task thus reduces to completion. Once the target positions are withheld, a masked latent predictor performs only slightly better than copying the last frame. To remove this leakage, we propose PointWM, a latent world model that turns completion into forecasting by predicting the features and geometry of future frames from strictly earlier context. Each target is queried only with its last-seen position and timestamp, while a latent action learned without annotations is meant to capture the part of the future that the past leaves undetermined. On HOI4D action segmentation with a P4Transformer backbone, PointWM improves F1@50 over training from scratch by 24.9 offline and 29.1 under strictly causal inference. These results show the promise of latent world models as a leakage-free pretraining paradigm for point-cloud videos.Our code is publicly available at https://github.com/InitalZ/PointWM.

</details>

#### 2026-11-15 - EasyNav: A Modular Architecture for Real-Time Navigation Across Heterogeneous Robot Environments

**Authors:** Francisco Martín Rico, Francisco Miguel Moreno, Juan Sebastián Cely Gutiérrez, Esther Aguado, Miguel Ángel De Miguel Paraíso, José Miguel Guerrero
**Links:** [abs](https://arxiv.org/abs/2611.19894) - [pdf](https://arxiv.org/pdf/2611.19894)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EasyNav: A Modular Architecture for Real-Time Navigation Across Heterogeneous Robot Environments
- 作者：Francisco Martín Rico, Francisco Miguel Moreno, Juan Sebastián Cely Gutiérrez, Esther Aguado, Miguel Ángel De Miguel Paraíso, José Miguel Guerrero
- 出版日期：2026-11-15T09:17:37Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.19894 ；PDF https://arxiv.org/pdf/2611.19894

### 一句话总结
论文提出以显式共享导航状态作为模块间唯一交互接口的模块化导航架构，并实现为开源 ROS 2 框架 EasyNav，在异构场景中验证其实时性与资源效率优于 Nav2。

### 研究问题
现有机器人导航栈通常将建图、定位、规划与控制隐式绑定到特定表示与数据流，导致架构难以扩展、难以进行实验对比，也难以对端到端时序进行推理。该问题在异构场景中尤为关键：多种空间表示、传感模态与坐标帧共存，并以不同速率演化。

### 核心思路/方法
- 以显式、共享的“导航状态”作为模块化组件之间的唯一交互接口。
- 将建图、定位、规划与控制约束为在该共享状态上运行，从而支持可互换、与表示无关的流水线，并受显式兼容性与时序契约约束。
- 将该架构实现为开源 ROS 2 框架 EasyNav。
- 通过真实机器人实验验证：包括使用激光传感的室内导航，以及使用 GPS 与 3D LiDAR 的大规模室内外多层路线导航。
- 在匹配条件下与 Nav2 对比，报告反应延迟与资源使用差异。

### 主要贡献
- 提出以共享导航状态为中心的模块化导航架构，明确模块间交互接口，并引入兼容性与时序契约。
- 实现开源 ROS 2 框架 EasyNav。
- 在真实机器人室内与室内外异构场景中验证架构可行性。
- 与 Nav2 在匹配条件下对比：室内反应延迟由 377 ms 降至 33 ms，室外由 71 ms 降至 8 ms，同时使用更少 CPU 与内存。

### 局限性
- 摘要未提供足够信息说明实验规模、机器人平台数量、场景复杂度分布与统计显著性。
- 摘要未提供足够信息说明共享导航状态的具体数据结构、兼容性与时序契约的形式化定义。
- 摘要未提供足够信息说明与 Nav2 对比时的具体配置、公平性控制细节及失败案例。
- 摘要未提供足够信息说明该架构在极端动态环境、多机器人协作或非 ROS 2 生态中的适用性。
- 摘要未提供足够信息说明开源框架的维护状态、版本与可复现实验材料。

### 阅读优先级
高。理由：该论文直接针对导航栈的模块化、表示无关性与端到端时序问题，给出架构级方案与开源实现，并在真实机器人异构场景中与 Nav2 进行延迟和资源对比；对机器人导航系统架构、ROS 2 框架设计与实时性评估具有较强参考价值。但需注意，摘要未提供实验细节与形式化定义，深入评估需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Most robot navigation stacks implicitly bind mapping, localization, planning, and control to specific representations and data flows, yielding architectures hard to extend, compare experimentally, or reason about end-to-end timing. This is critical in heterogeneous scenarios, where multiple spatial representations, sensing modalities, and coordinate frames coexist and evolve at different rates. This paper presents a navigation architecture centered on an explicit, shared navigation state that serves as the sole interaction interface between modular components. Constraining mapping, localization, planning, and control to operate over this shared state enables interchangeable, representation-agnostic pipelines under explicit compatibility and timing contracts. We realize this architecture as EasyNav, an open source ROS 2 framework, and validate it through real-robot experiments, including indoor navigation with laser sensing and large-scale indoor-outdoor navigation with GPS and 3D LiDAR across multi-level routes. Compared with Nav2 under matched conditions, EasyNav reduces reaction latency from 377 to 33 ms indoors and from 71 to 8 ms outdoors, while also using less CPU and memory.

</details>

#### 2026-11-15 - Beyond Vehicle-Centric Data: Scaling Autonomous Driving through Roadside-to-Vehicle Generation

**Authors:** Yichen Zhang, Zihan Wang, Hao Chen, Runyi Huang, Ruixue Zong, Jing Wang, Yunong Mao, Lei He, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2611.19830) - [pdf](https://arxiv.org/pdf/2611.19830)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, scene representation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Vehicle-Centric Data: Scaling Autonomous Driving through Roadside-to-Vehicle Generation
- 作者：Yichen Zhang, Zihan Wang, Hao Chen, Runyi Huang, Ruixue Zong, Jing Wang, Yunong Mao, Lei He, Keqiang Li
- 出版日期：2026-11-15T06:23:23Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.19830；PDF https://arxiv.org/pdf/2611.19830

### 一句话总结
论文提出 AnyR2V 框架，将路侧多模态观测转换为不同车辆视角下的七摄像头环视视频，并构建 R2V360 数据集，以路侧交通记录扩充自动驾驶训练数据。

### 研究问题
自动驾驶模型训练依赖大规模、多样化数据，而现有数据主要由车辆采集；扩展这类数据需要投入车队运营、数据处理与标注。路侧基础设施能记录交通与多车交互，但路侧与车载传感器之间存在视角差异，限制了路侧数据的直接使用。论文关注的问题是：能否把路侧观测转化为可用于训练的车载环视视频与多视角训练数据。

### 核心思路/方法
论文提出 AnyR2V：先把序列路侧多模态观测聚合为共享的场景几何与道路使用者运动表示，再沿目标车辆轨迹渲染外观、深度和布局条件，生成七摄像头环视视频；生成过程受场景结构与道路使用者运动引导，并以时空对齐的路侧—车辆配对数据监督。论文还将既有路侧 3D 边界框变换到目标车辆坐标系并与生成图像配对，使一段交通记录及其标注可产生多个车辆视角的训练数据。论文构建了 R2V360 数据集，包含城市路口 89 段真实交通序列，以及对齐的多模态路侧数据与车载环视视频。

### 主要贡献
- 提出 AnyR2V，将多模态路侧观测转换为不同车辆视角的七摄像头环视视频。
- 利用时空对齐的路侧—车辆配对进行监督，并以场景结构与道路使用者运动引导生成。
- 将路侧 3D 边界框变换至目标车辆坐标并与生成图像配对，实现由单次交通记录及其标注生成多车辆视角训练数据。
- 构建 R2V360：城市路口 89 段真实交通序列，含对齐的多模态路侧数据与车载环视视频。
- 摘要报告：AnyR2V 在图像保真度，以及生成图像与真实车载图像之间的深度和语义一致性上，优于六种场景重建方法；在真实车载测试集上，将相当于原始真实训练帧数 50% 的生成帧加入真实训练数据后，三个 3D 目标检测器的 mAP 相对仅用真实数据的基线提升 3.3–3.4 AP 点。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败场景、对路侧数据覆盖与标注质量的依赖、跨场景泛化能力、计算成本、实时性，也未给出六种对比方法的细节及三个 3D 检测器的具体名称与完整实验设置。

### 阅读优先级
中。理由：论文针对路侧数据与车载视角不匹配这一数据扩展问题，提出生成式转换框架并给出数据集与检测增益结果，主题与自动驾驶数据扩增、路侧—车载协同感知相关；但摘要未提供方法实现细节、泛化验证与成本信息，是否高优先级阅读取决于读者对路侧数据生成或多视角数据扩增的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Training autonomous driving models requires large and diverse datasets, collected primarily by vehicles. Scaling them entails investment in fleet operation, data processing and annotation. Road infrastructure records traffic and multi-vehicle interactions, yet the viewpoint gap between roadside and onboard sensors limits its direct use for training. Here we introduce AnyR2V, a framework that transforms multimodal roadside observations into seven-camera surround-view videos for different vehicle perspectives. It aggregates sequential observations into a shared scene representation of geometry and road-user motion, then renders appearance, depth and layout conditions along target-vehicle trajectories. Supervised by spatiotemporally aligned roadside-vehicle pairs, AnyR2V generates surround-view videos guided by scene structure and road-user motion. Existing roadside 3D bounding boxes are transformed into target-vehicle coordinates and paired with generated images, allowing one traffic recording and its annotations to yield training data from multiple vehicle perspectives. We construct R2V360, a dataset of 89 real traffic sequences at an urban intersection, with aligned multimodal roadside data and onboard surround-view videos. AnyR2V outperforms six scene reconstruction methods in image fidelity and in depth and semantic agreement between generated and real onboard images. We further evaluate generated videos along other vehicles' trajectories by adding them to real training data. Adding generated frames equal to 50% of the original real training frame count improves mean average precision (mAP) by 3.3-3.4 AP-points across three 3D object detectors on the real onboard test set, relative to real-data-only baselines. These results demonstrate that roadside traffic records can provide training data from multiple vehicle perspectives, offering a new data source for autonomous driving.

</details>

#### 2026-11-15 - JEPA4R: Embodied JEPA World Models with 4D Point Planning

**Authors:** Jiarui Dong, Zhiheng Liang, Yanjun Li, Zeyu Zhang, Heejeong Nam, Haoyu Chen, Hao Tang
**Links:** [abs](https://arxiv.org/abs/2611.19771) - [pdf](https://arxiv.org/pdf/2611.19771)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, digital twin, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JEPA4R: Embodied JEPA World Models with 4D Point Planning
- 作者：Jiarui Dong, Zhiheng Liang, Yanjun Li, Zeyu Zhang, Heejeong Nam, Haoyu Chen, Hao Tang
- 出版日期：2026-11-15T03:51:21Z
- 分类：Embodied / Robotics / AR Applications（主分类）；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.19771 ；PDF https://arxiv.org/pdf/2611.19771

### 一句话总结
JEPA4R 提出一种以单深度相机的点云为观测、在潜空间中进行预测与规划的 JEPA 世界模型（称为“4D 点规划”），并通过解码器把模型“想象”的内容可视化为 4D 点云。

### 研究问题
摘要指出 JEPA 世界模型存在两个挑战：
1. 2D 图像使操作所作用的度量几何变得隐式，并与外观纠缠在一起；
2. 模型“想象”的内容不可见，主要只在仿真中通过短时程潜空间规划来评判。

### 核心思路/方法
- 观测形式改为单深度相机的点云，而非 2D 图像。
- 在点云的潜空间中进行预测与规划，并通过策略头作用于冻结的潜表示，作者称之为“4D 点规划”。
- 在冻结的世界模型上附加解码器，将模型想象的内容以 4D 点云形式展示。
- 摘要报告该解码在 200 步上的平均点误差在 1.1 cm 以内。

### 主要贡献
- 提出 JEPA4R：面向具身场景、基于点云观测并在潜空间规划与执行的 JEPA 世界模型。
- 提出“4D 点规划”范式，策略头作用于冻结潜表示。
- 通过解码器使世界模型的想象内容可视化，并报告 200 步内平均点误差 ≤ 1.1 cm。
- 在 OGBench 的 Cube-Single、Cube-Double、Cube-Triple 和 Scene 上，按 OGBench 与 CortexBench 的策略学习协议，优于像素 JEPA 模型；在 MetaWorld 与 Adroit Relocate 上分别以 98.4% 和 88.0% 排名第一，高于第二名 R3M 的 96.0% 和 65.3%。
- 仅在数字孪生中训练，JEPA4R 及其策略头在真实机械臂上以夹爪与灵巧手实现零样本运行。

### 局限性
- 摘要未提供足够信息说明方法的具体网络结构、训练细节与计算开销。
- 摘要未提供足够信息说明 1.1 cm 点误差的评测设置与统计口径。
- 摘要未提供足够信息说明零样本真机实验的任务范围、成功率与失败情况。
- 摘要未提供足够信息说明与像素 JEPA 模型对比的具体数值差距及消融结果。
- 摘要未提供足够信息说明方法在更广泛任务或数据集上的泛化表现。

### 阅读优先级
高。理由：摘要同时给出明确的方法创新（点云潜空间规划与想象可视化）、多项基准上的量化领先结果，以及仅数字孪生训练即可零样本迁移真机的具身应用价值；对具身世界模型与机器人操作方向具有较强参考意义。

</details>

<details>
<summary>Abstract</summary>

Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space. Two challenges remain: 2D images leave the metric geometry that manipulation acts on implicit and entangled with appearance, and what these models imagine stays hidden, as they are mostly judged in simulation by short-horizon latent planning. We present JEPA4R, a JEPA world model that observes single-depth-camera point clouds, predicts and plans in their latent space, and acts through a policy head on its frozen latents; we call this 4D point planning. A decoder on the frozen world model shows what it imagines as 4D point clouds, with a mean point error within 1.1 cm over 200 steps. Under the policy-learning protocols of OGBench and CortexBench, JEPA4R leads pixel JEPA models on OGBench Cube-Single, Cube-Double, Cube-Triple and Scene, and ranks first on MetaWorld and Adroit Relocate with 98.4% and 88.0%, above the runner-up, R3M, at 96.0% and 65.3%. Trained only in a digital twin, JEPA4R and its policy heads run zero-shot on the real arm with both a gripper and a dexterous hand.

</details>

#### 2026-11-15 - M-CROSS: A Multisensor Simulation Dataset for SLAM across Water--Land Transitions

**Authors:** Yan Dong, Tianyi Wu, Junyu Yang, Shaoqiang Qiu, Zefeng Yan, Tao Zhang, Bin Han
**Links:** [abs](https://arxiv.org/abs/2611.19765) - [pdf](https://arxiv.org/pdf/2611.19765)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：M-CROSS: A Multisensor Simulation Dataset for SLAM across Water--Land Transitions
- 作者：Yan Dong, Tianyi Wu, Junyu Yang, Shaoqiang Qiu, Zefeng Yan, Tao Zhang, Bin Han
- 出版日期：2026-11-15T03:47:30Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.19765) / [PDF](https://arxiv.org/pdf/2611.19765)

### 一句话总结
论文提出 M-CROSS——据摘要称为首个面向连续水陆过渡场景的多传感器 SLAM 仿真数据集与基准，并配套过渡感知评测协议，用于揭示现有 SLAM 系统在水陆切换过程中的定位退化与失败。

### 研究问题
水陆跨域机器人需要在陆地、过渡段与水下阶段之间保持连续定位，但传感器特性与可用性会在这些阶段间突变。摘要指出，现有数据集与传统指标并非为刻画过渡所引发的退化与失败而设计，因此缺少针对连续水陆过渡下 SLAM 性能的系统评测手段。

### 核心思路/方法
- 构建多传感器仿真数据集 M-CROSS，提供同步的 LiDAR、声呐、立体相机、IMU、DVL 与深度测量。
- 提供 6DoF 位姿真值、逐传感器的介质状态标注，以及依赖介质状态的传感器退化模型。
- 建立过渡感知评测协议，包含四项指标：轨迹完成率（TCR）、分段绝对位姿误差（PW-APE）、过渡结束误差（TEE）与过渡生存期（TSP），分别衡量轨迹完成情况、单一域内精度、过渡引发的误差以及长时间部分浸没下的定位存活能力。
- 用 6 个代表性 SLAM 系统进行实验，观察其在水陆过渡全过程中的表现。

### 主要贡献
- 提出据摘要称为首个面向连续水陆过渡 SLAM 的多传感器仿真数据集与基准 M-CROSS。
- 提供多模态同步测量、6DoF 位姿真值、介质状态标注与介质相关的传感器退化模型。
- 提出包含 TCR、PW-APE、TEE、TSP 的过渡感知评测协议。
- 实验表明现有方法难以在全部水陆过渡中同时保持定位精度与轨迹连续性，出现过渡引发的漂移、轨迹不连续与跟踪失败。
- 数据集已公开（链接见摘要）。

### 局限性
- 摘要未提供足够信息说明仿真环境与真实水陆场景之间的差距及 Sim-to-Real 影响。
- 摘要未提供足够信息说明各传感器的具体仿真参数、噪声建模细节与退化模型形式。
- 摘要未提供足够信息说明 6 个代表性 SLAM 系统的具体名称、配置与实验规模。
- 摘要未提供足够信息说明数据集规模（序列数量、时长、场景多样性）与标注精度。
- 摘要未提供足够信息说明各指标的计算细节与阈值设定。

### 阅读优先级
高。理由：该工作直接针对水陆过渡这一传感器特性突变场景，提出专用数据集与评测指标，且摘要明确指出现有 SLAM 方法在该场景下存在漂移、不连续与跟踪失败；对多传感器融合、跨域定位与 SLAM 鲁棒性评测方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Water--land cross-domain robots require continuous localization across land, transition and underwater phases, where sensor characteristics and availability change abruptly. Existing datasets and conventional metrics are not designed to capture transition-induced degradation and failures. We present \textbf{M-CROSS}, to the best of our knowledge, the first multisensor simulation dataset and benchmark for SLAM across continuous water--land transitions. It provides synchronized LiDAR, sonar, stereo camera, IMU, DVL, and depth measurements; 6DoF pose ground truth; sensor-wise medium-state annotations; and medium-dependent sensor degradation models. We establish a transition-aware protocol comprising the Trajectory Completion Rate (TCR), Piecewise Absolute Pose Error (PW-APE), Transition End Error (TEE), and Transition Survival Period (TSP), which measure trajectory completion, single-domain accuracy, transition-induced error, and localization survival under prolonged partial immersion, respectively. Experiments with 6 representative SLAM systems show that existing methods fail to maintain both localization accuracy and trajectory continuity across the full set of water--land transitions, exhibiting transition-induced drift, trajectory discontinuities, and tracking failures. M-CROSS is publicly available https://anonymous.4open.science/r/MCross-Dataset

</details>

#### 2026-11-12 - Spatial Foundry: A Multimodal Dataset for Spatial Intelligence

**Authors:** Ethan Lin, Yang Song
**Links:** [abs](https://arxiv.org/abs/2611.17318) - [pdf](https://arxiv.org/pdf/2611.17318)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, geometric reconstruction, spatial intelligence, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatial Foundry: A Multimodal Dataset for Spatial Intelligence
- 作者：Ethan Lin, Yang Song
- 出版日期：2026-11-12T18:58:36Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页面 https://arxiv.org/abs/2611.17318 ；PDF https://arxiv.org/pdf/2611.17318

### 一句话总结
该论文提出了 Spatial Foundry，一个包含 5,280 个带家具住宅 3D 场景配置、具备可编辑资产并对齐视觉、几何与时间信息的多模态数据集，旨在为空间智能和世界模型研究提供统一参考系下的数据基础。

### 研究问题
摘要指出，空间智能需要把视觉观察与环境几何、物体及持久状态联系起来；但仅靠图像会隐含这些关系，而彼此割裂的标注又难以在统一参考下研究外观、相机运动与场景变化。论文因此关注如何构建一个多模态、共享坐标且支持受控变化的数据集，以支撑空间感知与世界模型相关研究。

### 核心思路/方法
论文构建了 Spatial Foundry 数据集，包含 5,280 个带家具住宅 3D 场景配置，并提供可编辑资产以及对齐的视觉、几何和时间数据。其模态包括平面图、透视与全景 RGB、度量深度、点云、网格、实例级 3D 边界框，以及与视频配对的相机轨迹。共享场景坐标将跨视角、跨时间的观察联系起来；可编辑源场景支持生成额外相机路径和受控物体变化。摘要还描述了数据表示与构建流程。

### 主要贡献
- 提出 Spatial Foundry 多模态数据集：5,280 个带家具住宅 3D 场景配置，包含可编辑资产和对齐的视觉、几何、时间数据。
- 提供多种模态：平面图、透视/全景 RGB、度量深度、点云、网格、实例级 3D 边界框、相机轨迹与视频配对。
- 通过共享场景坐标连接跨视角和跨时间观察，并利用可编辑源场景支持额外相机路径与受控物体变化。
- 摘要列出潜在应用方向：平面图条件 3D 生成、几何重建、实例级感知、相机条件视频生成、共享世界建模和场景编辑。
- 摘要提到公开项目页面提供视频和交互式彩色点云预览。

### 局限性
- 摘要未提供足够信息说明数据集规模之外的多样性、真实感与仿真差距。
- 摘要未提供足够信息说明标注精度、质量控制或人工校验流程。
- 摘要未提供足够信息说明基线实验、评价指标或与其他数据集的定量比较。
- 摘要未提供足够信息说明数据许可、使用限制或伦理与隐私相关考虑。
- 摘要未提供足够信息说明可编辑场景变化的具体类型、范围与可控程度。

### 阅读优先级
中。理由：该工作与空间智能、具身/机器人/AR 应用中的多模态数据构建和世界模型研究相关，数据集模态较丰富且强调共享坐标与受控变化；但摘要未给出实验验证、定量结果或数据质量细节，是否值得深入阅读取决于读者对数据集构建、3D 场景理解或相机条件生成等方向的具体需求。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annotations make it difficult to study appearance, camera motion, and scene changes under a common reference. We introduce Spatial Foundry, a collection of 5,280 furnished residential 3D scene configurations with editable assets and aligned visual, geometric, and temporal data. Its modalities include floor plans, perspective and panoramic RGB, metric depth, point clouds, meshes, instance-level 3D bounding boxes, and camera trajectories paired with video. Shared scene coordinates link observations across views and time; editable source scenes enable additional camera paths and controlled object changes. We describe the data representation and construction workflow, and discuss applications in floor-plan-conditioned 3D generation, geometric reconstruction, instance-level perception, camera-conditioned video generation, shared world modeling, and scene editing. Controlled camera and scene variations support spatial perception and world-model research. The public project page provides videos and an interactive colored point-cloud preview.

</details>

#### 2026-11-12 - ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving

**Authors:** Ziying Song, Shengkai Zhang, Caiyan Jia, Lei Yang, Lin Liu, Yuchen Liu, Ziyang Liu, Zirui Li, Gang Wang, Peiliang Wu, Li Wang, Yadan Luo, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2611.16579) - [pdf](https://arxiv.org/pdf/2611.16579)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving
- 作者：Ziying Song, Shengkai Zhang, Caiyan Jia, Lei Yang, Lin Liu, Yuchen Liu, Ziyang Liu, Zirui Li, Gang Wang, Peiliang Wu, Li Wang, Yadan Luo, Chen Lv
- 出版日期：2026-11-12T10:10:39Z
- 分类：主分类 Embodied / Robotics / AR Applications；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.16579 ；PDF https://arxiv.org/pdf/2611.16579

### 一句话总结
论文提出 ActWorld-JEPA，将动作条件化的联合嵌入预测架构（JEPA）用于候选轨迹规划，并通过关系残差重排序（R³）把潜空间未来预测与候选规划评分连接起来，实现端到端自动驾驶的候选选择。

### 研究问题
摘要指出，JEPA 能在潜空间中进行未来预测而无需像素重建，但“潜预测一致性”本身并不能确立候选规划之间的相对驾驶质量。因此，核心问题是：如何利用 JEPA 的潜空间预测表示来评估和选择候选驾驶规划，使预测结果真正服务于驾驶决策。

### 核心思路/方法
论文给出一个面向候选规划的联合嵌入公式，包含两个主要部分：

1. **Plan-Conditioned JEPA（PC-JEPA）**：使用全局与逐步的轨迹意图引导循环潜预测，再通过门控交叉注意力（gated cross-attention）将预测未来与当前场景结合。
2. **Relational Residual Reranking（R³）**：在规划监督下建模“规划表示”与“未来表示”之间的一致性和差异，对基础规划分数产生有界、门控的残差修正。

该公式在推理时仅使用已观测上下文和候选轨迹，将潜预测与候选选择相连接。

### 主要贡献
- 提出 ActWorld-JEPA，将动作条件化的 JEPA 世界模型与潜空间规划结合，用于基于候选的端到端自动驾驶。
- 提出 PC-JEPA，以全局和逐步轨迹意图引导循环潜预测，并用门控交叉注意力融合预测未来与当前场景。
- 提出 R³，在规划监督下利用规划与未来表示的一致/差异信息，对基础规划分数进行有界门控残差修正。
- 报告了基准结果：NAVSIM v1 navtest 上 94.1 PDMS；NAVSIM v2 navtest 与 navhard 上分别为 91.6 和 42.7 EPDMS；nuScenes 上 1–6 秒平均 L2 误差 1.20 m、预测碰撞率 0.76%。
- 摘要称该工作为从 JEPA 预测表示走向“由预期后果指导驾驶决策”提供了有效路径。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性、模型规模或训练成本。
- 摘要未提供足够信息说明各模块的消融实验细节与各自增益。
- 摘要未提供足够信息说明失败案例、安全边界或分布外场景表现。
- 摘要提到“benchmark-specific implementations”以及最终选择器使用聚合 NAVTEST 反馈进行校准，但未提供足够信息说明其泛化性与公平性影响。
- 摘要未提供足够信息说明 nuScenes 评估的具体设置与对比基线细节。

### 阅读优先级
**中**。理由：论文主题处于 JEPA 世界模型与端到端自动驾驶规划的交叉点，方法结构（PC-JEPA + R³）和报告的基准指标具有明确参考价值；但摘要未展开实验细节、消融与局限性，需阅读全文后才能判断其方法增益与泛化性。若关注潜空间预测用于规划候选重排序，优先级可视为偏高；若仅需广泛了解自动驾驶规划进展，则为中等。

</details>

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) enable future prediction in latent space without pixel reconstruction. However, latent predictive consistency alone does not establish the relative driving quality of candidate plans. We present ActWorld-JEPA, a joint-embedding formulation for candidate-based driving. Where Plan-Conditioned JEPA (PC-JEPA) uses global and step-wise trajectory intentions to guide recurrent latent prediction, then combines the predicted future with the current scene through gated cross-attention; Relational Residual Reranking ($R^3$) models agreement and discrepancy between plan and future representations under planning supervision, yielding bounded, gated residual corrections to the base planning scores. This formulation connects latent prediction to candidate selection using only observed context and proposed trajectories at inference. Benchmark-specific implementations report 94.1 PDMS on NAVSIM v1 navtest, with the final selector calibrated using aggregate NAVTEST feedback, and 91.6 and 42.7 EPDMS on NAVSIM v2 navtest and navhard, respectively. The nuScenes evaluation reports a mean $L_2$ error of 1.20 m and a predicted collision rate of 0.76% over 1--6 s. This work provides an effective path from JEPA's predictive representations to driving decisions informed by anticipated consequences.

</details>

#### 2026-11-12 - VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation

**Authors:** Shengjia Zhu, Wenqiang Xu, Lin Shao
**Links:** [abs](https://arxiv.org/abs/2611.16423) - [pdf](https://arxiv.org/pdf/2611.16423)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation
- 作者：Shengjia Zhu, Wenqiang Xu, Lin Shao
- 出版日期：2026-11-12T07:33:05Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要 https://arxiv.org/abs/2611.16423 ；PDF https://arxiv.org/pdf/2611.16423

### 一句话总结
VOKE 是一个运动学感知框架，在现有物体位姿估计器输出基础上，补充估计物体的线速度、角速度、线加速度和角加速度，并将该运动状态用于位姿精化与下游强化学习控制。

### 研究问题
摘要指出，基于视觉的灵巧手内操作不仅需要知道物体“在哪里”，还需要知道物体“如何运动”；但多数机器人操作系统依赖的现成视觉感知模型只输出静态物体掩码、几何或 6D 位姿，导致下游控制器需要从带噪声的视觉观测中隐式推断物体动力学。VOKE 要解决的问题是：如何从视觉中显式恢复较完整的物体运动学状态，并让其可用于感知到控制的链路。

### 核心思路/方法
摘要给出的方法由两个核心感知模块和一个下游应用研究组成：

1. **Pluggable Kinematics Module（PKM，可插拔运动学模块）**：接在标准位姿估计器的输出之后，从时序视觉特征中预测物体的线速度、角速度、线加速度和角加速度。
2. **Kinematics-guided Pose Refinement Module（KPRM，运动学引导的位姿精化模块）**：将上述运动向量转换为二阶、运动先验的参考位姿，并据此精化逐帧位姿估计。
3. **下游应用 Kinematics-Augmented Reinforcement Learning（KARL，运动学增强强化学习）**：将运动学增强的策略与使用位姿历史的基线策略进行比较；策略先在仿真中训练，随后将运动学增强策略不做策略微调地迁移到实体机器人。

整体上，VOKE 将“位姿估计”扩展为包含位姿、线/角速度、线/角加速度的完整物体运动学状态估计。

### 主要贡献
基于摘要可归纳的贡献包括：

- 提出 VOKE 运动学感知感知框架，用于增强现有物体及手-物位姿估计器，输出更完整的物体运动学状态。
- 设计 PKM，可从时序视觉特征预测线/角速度与线/角加速度。
- 设计 KPRM，利用运动向量构造二阶运动先验参考位姿并精化逐帧位姿。
- 在 DexYCB 和 OakInk 上评估：摘要称其在三种不同 backbone 上一致改善物体位姿估计，并且相较“位姿差分”显著降低速度与加速度估计误差。
- 通过 KARL 展示下游应用：运动学增强策略在仿真训练后可零策略微调迁移至实体机器人，形成从感知到控制的完整通路。

### 局限性
- 摘要未提供足够信息说明 VOKE 在真实机器人上的感知鲁棒性、泛化范围或失败情形。
- 摘要未提供足够信息说明实验的定量指标细节、数据集划分、训练数据规模与计算开销。
- 摘要未提供足够信息说明 PKM 对位姿估计器误差的敏感程度，以及 KPRM 在快速运动或遮挡条件下的表现。
- 摘要未提供足够信息说明 KARL 相比位姿历史基线的具体性能差距与统计显著性。
- 摘要未提供足够信息说明方法对不同物体类别、手型或传感器配置的适用边界。

### 阅读优先级
**中**。理由：该论文聚焦灵巧手内操作中“显式运动学感知”这一感知到控制的关键缺口，方法模块清晰，且有跨数据集评估与实体机器人迁移的下游验证；但仅凭摘要无法判断定量提升幅度、真实场景鲁棒性和与现有方法的完整对比，适合在需要了解手内操作感知-控制链路时进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Vision-based dexterous in-hand manipulation requires knowing not only where an object is, but also how it moves. However, most robotic manipulation systems rely on off-the-shelf visual perception models whose outputs are limited to static object masks, geometry, or 6D poses, leaving downstream controllers to infer object dynamics implicitly from noisy visual observations. We present VOKE, a kinematics-aware perception framework that augments existing object and hand-object pose estimators to recover a complete object kinematic state comprising pose, linear and angular velocity, and linear and angular acceleration. VOKE contains two core perception modules and a downstream application study. First, a Pluggable Kinematics Module (PKM) attaches to the output of a standard pose estimator and predicts the object's linear and angular velocity and acceleration from temporal visual features. Second, a Kinematics-guided Pose Refinement Module (KPRM) converts this motion vector into a second-order, motion-prior reference pose and refines the per-frame pose estimates. We evaluate VOKE on DexYCB and OakInk, where it consistently improves object pose estimation across three different backbones and substantially reduces velocity and acceleration estimation error compared with pose differencing. As a downstream application, we use Kinematics-Augmented Reinforcement Learning (KARL) to compare a kinematics-augmented policy with a pose-history baseline. After training the policies in simulation, we transfer the kinematics-augmented policy to the physical robot without policy fine-tuning, demonstrating the complete perception-to-control pathway in the target domain.

</details>

#### 2026-11-12 - Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras

**Authors:** Raul Steinmetz, Jair Augusto Bottega, Ayanori Yorozu, Akihisa Ohya
**Links:** [abs](https://arxiv.org/abs/2611.16282) - [pdf](https://arxiv.org/pdf/2611.16282)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras
- 作者：Raul Steinmetz, Jair Augusto Bottega, Ayanori Yorozu, Akihisa Ohya
- 出版日期：2026-11-12T04:32:37Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.16282) / [PDF](https://arxiv.org/pdf/2611.16282)

### 一句话总结
论文研究利用固定外置相机进行室内机器人导航，指出 PPO 端到端学习在该设置下失败，并提出 VINE：先通过监督学习估计视角不变障碍图，再供 PPO 策略或 A* 规划器使用。

### 研究问题
论文关注室内环境下、基于固定外置相机（exocentric cameras，即基础设施安装、位于机器人外部的相机）的机器人导航与避障问题。作者指出，标准 PPO 在机载相机场景中可行，但在该外置相机设置下无法端到端学习导航；其归因是外置观测与以机器人为中心的动作和目标表述之间存在视角不匹配，仅靠奖励信号难以解决。

### 核心思路/方法
论文提出 VINE（Viewpoint-Invariant Navigation from Exocentric Cameras）。VINE 使用一个通过监督学习训练的障碍图估计网络，输入包括外置图像、相机位姿、机器人位姿和房间尺寸，输出视角不变的障碍图。该障碍图既可供 PPO 策略使用，也可供 A* 等规划器使用。摘要还称，该方法无需针对特定视角调参，仅需近似相机位姿估计，并对相机内参变化具有鲁棒性，且可扩展到部分覆盖的双相机设置。

### 主要贡献
- 明确指出标准 PPO 在外置固定相机端到端导航设置中失败，并将其归因于外置观测与以机器人为中心的动作和目标表述之间的视角不匹配。
- 提出 VINE，通过监督学习估计视角不变障碍图，并将该图接入 PPO 策略或 A* 规划器。
- 摘要声称其地图估计优于透视映射方法，可处理大范围位置和朝向的相机而无需视角特定调参。
- 摘要声称仅需近似相机位姿：x、y、z 各轴噪声标准差 30cm，平均旋转误差约 20°。
- 摘要声称对相机内参变化具有鲁棒性，并可扩展到部分覆盖的双相机设置。
- 摘要声称在评估时相机位置随机化的仿真环境中，VINE 的导航成功率超过使用机载相机的 PPO。

### 局限性
摘要未提供足够信息说明实验规模、仿真环境细节、真实机器人实验、失败案例、计算开销、与更多基线方法的系统比较，以及“优于透视映射方法”和“超过机载相机 PPO”的具体量化结果。摘要未提供足够信息说明方法在真实室内环境中的泛化能力与安全性边界。

### 阅读优先级
中。理由：该论文针对外置相机机器人导航中的视角不匹配问题提出明确的中间表征方案，并给出监督学习障碍图与 PPO/A* 的结合路径；若关注基础设施相机辅助机器人导航、视角不变表征或端到端策略失败分析，具有参考价值。但当前仅有摘要与元数据，缺少实验细节与量化结果，需阅读全文后再判断其证据强度。

</details>

<details>
<summary>Abstract</summary>

We study robot navigation in indoor environments from fixed exocentric cameras (infrastructure-mounted, external to the robot). We show that standard Proximal Policy Optimization (PPO), which succeeds with onboard cameras, fails to learn this navigation end-to-end in our setup. This failure results from the perspective mismatch between exocentric observations and egocentric action and goal formulations, which is too complex to resolve from the reward signal alone. To address this, we propose Viewpoint-Invariant Navigation from Exocentric Cameras (VINE). VINE uses an obstacle map estimation network, trained with supervised learning, that takes exocentric images, camera pose, robot pose, and room dimensions as input and produces a viewpoint-invariant obstacle map. This map can be used either by a PPO policy or by a planner such as A*. VINE's map estimation performs better than perspective mapping approaches, handles cameras placed across a wide range of positions and orientations without view-specific tuning, requires only approximate camera pose estimates (noise with a standard deviation of 30cm per axis in x, y, and z and about 20° of rotation error on average), is robust to intrinsic variation, and extends to two-camera setups with partial coverage. Despite operating from cameras randomized in position during evaluation, VINE surpasses the navigation success rate of PPO with an onboard camera in simulated environments.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
