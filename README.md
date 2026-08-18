# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：42
- 分类分布：
  - Neural Scene Representations & Rendering: 14
  - 3D Reconstruction & Multi-view Geometry: 12
  - Embodied / Robotics / AR Applications: 10
  - Geometry Foundation Models: 5
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **几何基础模型正从“重建专用”走向“多任务统一骨干”**  
   今日多篇论文（GeoUP、Map-Det3D、RbFT-Net）不再将3D重建视为孤立任务，而是将重建导向的潜表示或重建先验作为统一骨干，直接服务于下游感知任务（深度估计、3D检测、占用预测）。GeoUP明确将VGGT的重建潜表示适配到自动驾驶多相机流中；Map-Det3D则把前馈度量重建模型作为几何先验，将检测直接引入重建出的3D空间。这表明**重建先验正在成为一种通用的几何骨干范式**。

2. **3D高斯溅射（3DGS）正进入“结构可控化”与“跨模态扩展”阶段**  
   LocusGS通过显式3D锚点（中心+支撑半径）约束查询的空间连贯性，解决“同一查询解码的高斯散落远隔区域”的问题，代表3DGS前馈范式从纯隐式向**空间显式可控**演进。GS²CI将3DGS与快照压缩成像（SCI）结合，并借助视觉基础模型先验提升重建鲁棒性，显示3DGS正在向**极端输入条件（单次测量、信息严重压缩）** 扩展。

3. **大规模视觉基础模型（VFM）正被系统性“借用”到三维与多模态表示中**  
   今日至少5篇论文直接依赖视觉基础模型：GS²CI（3D VFM初始化+2D VFM伪视图监督）、DreamX-Phi（冻结V-JEPA teacher+SAM3掩码）、Semantic Radiance Fields（预训练分割模型提升语义到3D）、RGB-HS（从RGB基础模型向热成像分支施加层级监督）、Seed2GS（QD-SAM3）。**基础模型作为先验提供者（初始化、监督、掩码、几何约束）已成为跨模态与跨任务迁移的主流技术路线**。

4. **仿真器与基准正在向“物理真实+语义可用+形态多样”三位一体演进**  
   HumanoidVLN构建物理接地的人形机器人VLN仿真器，覆盖4种不同形态的机器人，并验证sim-to-real迁移；RoadWeaver从零生成大规模车道级HD地图供驾驶模拟闭环评估；Semantic Radiance Fields提出将语义辐射场作为空间推理智能体的仿真器。**仿真平台不再仅追求视觉真实感，而是强调物理约束（双足平衡、相机运动畸变）、语义真值（逐类查询）和形态多样性（多种机器人、多种车辆视角）。**

5. **标注协议与数据本身正在被重新设计，以覆盖长尾物理差异**  
   ProPose提出统一健全肢体、义肢和残肢的拓扑标注协议，并设计Real-to-Synthetic数据扩充缓解极端长尾；MV2数据集则设计了多车交叉轨迹评估协议（用一辆车的视角训练、另一辆车的视角测试），以更严格评估大视点变化下的NVS。**这些工作反映出：性能瓶颈正从模型结构转向数据协议与评估协议的设计创新。**

---

#### 技术路线观察

| 方向 | 核心关注点 | 代表性论文 | 技术侧重点 |
|---|---|---|---|
| **几何基础模型** | 重建先验的多任务泛化、跨域鲁棒性 | GeoUP、Map-Det3D | 将重建潜表示/重建前馈模型作为几何骨干，注入校准感知编码与跨视图注意力 |
| **3D/4D重建与NVS** | 稀疏输入下的鲁棒重建、空间可控性、真实驾驶场景评估 | GS²CI、LocusGS、MV2 | VFM初始化与伪监督、显式锚点状态逐步细化、多轨迹交叉测试协议 |
| **神经场景表示** | 语义与几何联合编码、解释性、对象提取 | Semantic Radiance Fields、COGENT、Seed2GS | 将2D语义提升到3D辐射场/3DGS；在高斯参数空间做反事实优化；单参考视图引导对象分割 |
| **机器人/AR应用** | 物理接地仿真、动作条件预测、多形态泛化 | HumanoidVLN、DreamX-Phi、AMR-Pose | 物理引擎+RL运动策略、SE(3)几何编码注入注意力、主动LED标记+概率切换PnP |
| **底层几何优化** | 经典问题的效率与可扩展性 | Fast Iterative Five-point | Dog Leg迭代优化替代代数解法，精度不变、速度翻倍 |

**关键观察：**
- 几何基础模型与3DGS两条路线在今日论文中出现了明显交汇：GeoUP与Map-Det3D将重建模型作为检测/感知的几何先验，而GS²CI将VFM先验引入3DGS重建，两者方向相反但共同指向“**重建学习与感知任务互为先验**”的循环范式。
- 视觉基础模型的角色已从“直接微调”转变为“多样化先验提供者”：初始化（GS²CI）、伪标签教师（DreamX-Phi、RGB-HS）、语义提升（Semantic Radiance Fields）、开放词汇分割（Seed2GS）。
- 仿真与数据层面不再只追求“更多数据”，而是追求“更可控的多样性”：HumanoidVLN控制机器人形态与身高，RoadWeaver控制路网拓扑与规模，MV2控制视点差异幅度。

---

#### 值得优先阅读的论文

1. **GeoUP（2608.13147）**  
   *理由*：本文将几何基础模型（VGGT）的重建潜表示系统性地适配到自动驾驶多相机感知场景，并以因子化注意力+校准感知射线编码实现深度、检测、占用三任务统一。它代表了“重建-感知统一骨干”这一最新技术路线的典型范式，对从事自动驾驶或统一3D感知的读者有直接参考价值。

2. **GS²CI（2608.13502）**  
   *理由*：单次快照压缩测量即可重建3D场景，是3DGS与极端输入条件结合的前沿探索。其提出的SCI专用稠密化策略（OSGR）针对弱监督下3DGS不稳定的问题，具有普适借鉴意义。此外，它展示了VFM作为初始化与伪监督的双重用法。

3. **LocusGS（2608.12825）**  
   *理由*：指出了查询式前馈3DGS的典型失败模式（同一查询解码的高斯空间分散），并给出简洁有效的解决方案（显式3D锚点状态）。将为进一步研究“3DGS的空间可控生成”提供重要基础，值得精读。

4. **Map-Det3D（2608.12179）**  
   *理由*：直接挑战“2D检测后提升到3D”的脆弱范式，转而用前馈度量重建模型作为几何先验，在重建出的3D空间中做检测。这一思路跳出检测头设计的传统框架，对无深度传感器的机器人与自动驾驶感知有方法论意义。

5. **HumanoidVLN（2608.12860）**  
   *理由*：首个面向多种人形机器人形态的物理接地VLN仿真器与基准，直指现有VLN基准忽视双足物理约束与形态差异的缺陷。其分层控制栈（RL运动+PD/MPC路径跟踪）和多智能体指令生成流水线具有较高工程参考价值；对从事具身导航与仿真研究的读者应优先关注。

---

#### 可能的研究机会

1. **“重建-感知”双向循环的可扩展验证**  
   GeoUP和Map-Det3D各自证明了“重建先验→感知”的可行性，但尚未看到“感知反馈→改进重建”的闭环研究。将两者结合，构建一个重建与感知互相提供监督信号的统一框架，是一个待填补的空白。

2. **3DGS空间可控生成与语义/实例级编辑的结合**  
   LocusGS已经让高斯查询具备显式空间锚点，这一机制自然可与Seed2GS（单参考视图对象提取）或COGENT（高斯参数空间反事实解释）结合，实现语义级、实例级的3DGS编辑与可解释操作。例如，将LocusGS的锚点与语义标签绑定，实现“指哪儿改哪儿”的可控生成。

3. **在康复医学与辅助技术中

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-18T09:05:58-04:00
**Total number of papers:** 36
**Number of papers added in the latest update:** 12
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

### 2026-08

#### 2026-08-15 - VGGT-Align: Bridging Local Reconstruction and Global Consistency for Long-Sequence 3D Reconstruction

**Authors:** Wei Zhang, Yihang Wu, Songhua Li, Qi Wang
**Links:** [abs](https://arxiv.org/abs/2608.15260) - [pdf](https://arxiv.org/pdf/2608.15260)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction

<details>
<summary>Abstract</summary>

Maintaining global geometric consistency is a central challenge in long-sequence 3D reconstruction, with scale drift being the most critical failure mode. In chunk-based inference pipelines, the scale degree of freedom in sequential Sim(3) alignment is left unconstrained, causing estimation errors to compound multiplicatively and distort global trajectories and point cloud geometry. We present a scale-consistency enhancement framework built on a key insight: in structured environments such as driving scenes, geometric quantities arising from environmental regularity remain inherently invariant across temporal segments, and discrepancies in their per-chunk measurements directly expose inter-chunk scale drift. We propose Scene Geometric Invariant Anchoring (SGIA), which extracts dominant geometric invariants from each chunk's predicted point cloud via coarse-to-fine robust estimation and exploits their cross-chunk consistency to establish scale constraints independent of point cloud registration, explicitly degenerating 7-DoF Sim(3) alignment into 6-DoF rigid-body transformation and severing chain-wise scale error propagation at its source. We further introduce a lightweight test-time adaptation strategy that fine-tunes only normalization-layer parameters via multi-objective self-supervision, progressively improving intra-chunk predictions along the sequence. Both modules are plug-and-play and require no offline retraining. Experiments on multiple long-sequence benchmarks demonstrate state-of-the-art performance, reducing absolute trajectory error by up to 32% with significant gains in trajectory stability and reconstruction quality. Code: https://github.com/WZ-CS/VGGT-Align

</details>

#### 2026-08-13 - Geometry-Grounded Unified 3D Perception for Autonomous Driving

**Authors:** Longfei Xu, Xiaohui Wang, Zehao Huang, Han Li, Ya Yang, Naiyan Wang, Si Liu
**Links:** [abs](https://arxiv.org/abs/2608.13147) - [pdf](https://arxiv.org/pdf/2608.13147)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, metric depth, depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry-Grounded Unified 3D Perception for Autonomous Driving
- 作者：Longfei Xu, Xiaohui Wang, Zehao Huang, Han Li, Ya Yang, Naiyan Wang, Si Liu
- 出版日期：2026-08-13
- 分类：Geometry Foundation Models（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.13147

### 一句话总结
本文提出GeoUP框架，将基于几何基础模型的重建导向潜表示适配到多相机驾驶场景，通过因子化跨图像注意力和校准感知的射线图编码，实现度量深度估计、3D目标检测和语义占用预测的统一3D感知。

### 研究问题
现有基于相机的自动驾驶感知框架通常使用为语义识别预训练的骨干网络，并通过下游任务特定模块引入3D几何，导致其共享表示难以保留显式的度量几何和一致的3D场景结构。本文旨在构建一种能够保持度量3D结构的统一共享表示，以支持多种3D感知任务。

### 核心思路/方法
- 将重建导向的VGGT潜表示适配到经过标定的、流式的多相机驾驶场景中。
- 将跨图像交互分解为自注意力、时间注意力和视图注意力，以分别捕获结构上不同的时间和跨视图对应关系。
- 注入校准感知的射线图编码，以提供度量尺度和相机几何信息。
- 将几何基础的潜表示解码为度量深度估计、3D目标检测和语义占用预测，分别对应同一3D场景的表面级、实例级和体素级读取。
- 通过多任务和多数据集联合训练，利用异构标注并泛化到不同的传感器配置和感知范围。

### 主要贡献
- 提出GeoUP框架，将几何基础模型的潜表示引入统一的3D驾驶感知。
- 设计因子化的自/时间/视图注意力结构，以捕获时间和跨视图的结构性对应关系。
- 引入校准感知的射线图编码，提供度量尺度和相机几何。
- 在nuScenes、Argoverse 2、Waymo、KITTI和DDAD等多个数据集上实现检测、占用和深度估计的SOTA性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶统一3D感知中的核心瓶颈——共享表示的度量几何保持问题，提出了基于几何基础模型的全新方案，并在五个公开数据集上取得SOTA结果，方法思路新颖且实验覆盖广泛，对从事多相机3D感知、几何基础模型及应用的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera-based autonomous driving perception requires a shared representation that preserves metric 3D structure across synchronized multi-camera streams. However, existing image-based frameworks often rely on backbones pretrained for semantic recognition, and introduce 3D geometry through downstream task-specific modules. As a result, their shared representations may fail to preserve explicit metric geometry and consistent 3D scene structure. In this paper, we present a Geometry-grounded Unified 3D Perception (GeoUP) framework that adapts the reconstruction-oriented latent of VGGT to calibrated, streaming multi-camera driving scenes. GeoUP factorizes cross-image interaction into self, temporal, and view attention to capture structurally distinct temporal and cross-view correspondences. It further injects calibration-aware raymap encodings to provide metric scale and camera geometry. The resulting geometry-grounded latent is decoded for metric depth estimation, 3D object detection, and semantic occupancy prediction, corresponding to surface-, instance-, and volume-level readouts of the same 3D scene. Through joint multi-task and multi-dataset training, GeoUP effectively leverages heterogeneous annotations and generalizes across diverse sensor configurations and perception ranges. Extensive experiments on nuScenes, Argoverse 2, Waymo, KITTI, and DDAD demonstrate that GeoUP achieves SOTA performance across detection, occupancy, and depth estimation. These results validate the effectiveness of geometry-grounded representations for unified 3D driving perception.

</details>

#### 2026-08-13 - RbFT-Net: Rectify-Before-Fuse Temporal Radar Anchors for 4D Radar-Camera Depth Completion

**Authors:** Wentao Zhao, Shouxuan Wu, Yongtao Cen, Tianchen Deng, Yuyang Zhang, Jingchuan Wang
**Links:** [abs](https://arxiv.org/abs/2608.13102) - [pdf](https://arxiv.org/pdf/2608.13102)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** depth prediction, metric depth, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RbFT-Net: Rectify-Before-Fuse Temporal Radar Anchors for 4D Radar-Camera Depth Completion
- 作者：Wentao Zhao, Shouxuan Wu, Yongtao Cen, Tianchen Deng, Yuyang Zhang, Jingchuan Wang
- 出版日期：2026-08-13
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2608.13102

### 一句话总结
RbFT-Net提出了一种“先矫正后融合”的端到端框架，通过对多帧4D雷达点进行图像条件化矫正与可靠性估计，再选择性传播锚点，以提升雷达-相机深度补全的精度与鲁棒性。

### 研究问题
多帧雷达-相机深度补全中，聚合后的雷达测量虽能提供更密的度量提示，但存在时间错位、动态物体干扰、杂波和多径反射等问题，直接传播不可靠测量会污染大范围深度预测区域。

### 核心思路/方法
- 将累积的雷达返回视为带有噪声的时序锚点候选，而非直接视为准确测量。
- 设计图像条件化矫正模块，联合修正锚点在图像平面上的位置和度量深度，并同时估计逐点可靠性。
- 经矫正后的锚点在高层多模态融合之前进行选择性传播，以抑制不可靠测量的影响。
- 整体采用“先矫正后融合”（rectify-before-fuse）的端到端训练框架。

### 主要贡献
- 提出RbFT-Net，一个端到端的“先矫正后融合”多帧4D雷达-相机深度补全框架。
- 不再假设累积雷达返回准确，而是将其建模为带噪声的时序锚点候选，并引入图像条件化矫正与可靠性估计。
- 在ZJU-4DRadarCam及新采集的4D雷达-相机-激光雷达数据集上，持续优于所评估的独立雷达-相机方法，并与使用辅助单目深度模型的插件式方案保持竞争力。
- 跨平台评估和组件分析验证了所提矫正与可靠性感知传播策略的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向自动驾驶中的雷达-相机深度补全，方法设计合理且有跨数据集验证，但摘要未给出具体数值性能或与最先进方法的详细对比，若读者关注多模态深度补全或雷达感知可进一步阅读全文，否则优先度一般。

</details>

<details>
<summary>Abstract</summary>

Dense metric depth prediction from cameras and millimeter-wave radar offers a cost-effective sensing solution for autonomous systems. However, radar measurements are inherently sparse and susceptible to clutter, multipath reflections, and projection errors. While aggregating multiple radar frames provides denser metric cues, it also introduces temporal misalignment and dynamic-object interference. Directly propagating such unreliable measurements can therefore corrupt large regions of the predicted depth map. To address this issue, we propose RbFT-Net, an end-to-end rectify-before-fuse framework for multi-frame 4D radar-camera depth completion. Rather than assuming accumulated radar returns to be accurate, RbFT-Net treats them as noisy temporal anchor candidates. An image-conditioned rectification module jointly corrects their image-plane locations and metric depths while estimating pointwise reliability. The rectified anchors are then selectively propagated before high-level multi-modal fusion, suppressing the influence of unreliable measurements. Experiments on ZJU-4DRadarCam and a newly collected 4D radar-camera-LiDAR dataset show that RbFT-Net consistently outperforms the evaluated independent radar-camera methods and remains competitive with plug-in pipelines using auxiliary monocular depth models. Cross-platform evaluation and component analyses further support the effectiveness of the proposed rectification and reliability-aware propagation strategy.

</details>

#### 2026-08-12 - Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs

**Authors:** Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò, Sunghwan Hong, Denis Rozumny, Johannes Schönberger, Zuria Bauer, Hermann Blum, Peter Kontschieder, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2608.12179) - [pdf](https://arxiv.org/pdf/2608.12179)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs
- 作者：Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò, Sunghwan Hong, Denis Rozumny, Johannes Schönberger, Zuria Bauer, Hermann Blum, Peter Kontschieder, Marc Pollefeys
- 出版日期：2026-08-12
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.12179

### 一句话总结
Map-Det3D 将前馈式度量 3D 重建模型作为几何骨干，将多视角 3D 物体检测直接引入重建出的度量 3D 空间中，从而从单目视频流中实现稳定的度量级 3D 检测。

### 研究问题
如何在缺乏深度传感器的情况下，从单目视频流中实现可靠的度量级 3D 物体检测，尤其是克服单张图像中深度和绝对尺度欠约束带来的检测不稳定性，以及在相机、运动或环境发生域偏移时的泛化问题。

### 核心思路/方法
- 设计在线多视角 3D 检测模型 Map-Det3D，将短时间窗口内的多视图映射为输入，使用前馈度量 3D 重建模型作为几何骨干，并调整其面向物体的能力。
- 直接在重建出的度量 3D 空间中预测 3D 检测框，绕过常用的 2D 检测后提升至 3D（2D-to-3D lifting）的范式。
- 在多个基准上验证了在线性能和鲁棒的跨域迁移能力。

### 主要贡献
- 提出 Map-Det3D，将检测直接融入从 RGB 重建的 3D 空间中，避免 2D 到 3D 提升的脆弱性。
- 展示了将重建先验训练用于检测是获得单目视频稳定度量 3D 检测的实用路径。
- 验证了该设计在多个基准上的强在线性能及无需适应的鲁棒迁移能力，并开源代码与模型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目 3D 检测中尺度欠约束的核心难题，提出了一种新颖的“重建-检测”一体化范式，且实验显示跨域迁移能力强，对面向具身智能的视觉感知研究具有较高参考价值。摘要中虽未给出定量结果细节，但问题动机清晰、方法路径创新，建议优先精读。

</details>

<details>
<summary>Abstract</summary>

Metric 3D object detection is a core capability for embodied agents, yet most reliable systems lean on depth sensors, trading away cost, power, and integration simplicity. This motivates monocular 3D detection, which avoids additional constraints, yet it faces a major obstacle: from a single image, depth, and especially absolute scale, are underconstrained. As a result, the prevailing pattern of detecting in 2D and then predicting 3D attributes is often brittle, since modest range errors can dominate 3D localization, and the learned scale prior can fail when cameras, motion, or environments undergo domain shifts. To address this, we propose Map-Det3D, an online multi-view 3D object detection model that brings detection directly into a 3D space reconstructed from RGB. We map a short temporal window into multiple views and repurpose a feed-forward metric 3D reconstruction model as our geometric backbone while tuning its object-aware capabilities. Building on this representation, Map-Det3D directly predicts boxes in metric 3D space, without the widely used 2D-to-3D lifting. Experiments across different benchmarks show that this design supports strong online performance and robust transfer without adaptation, suggesting that training reconstruction priors for detection is a practical route to stable metric 3D detection from monocular video. Code and models are available at https://royyang0714.github.io/Map-Det3D.

</details>

## Dynamic / 4D Reconstruction

No papers in the current README window.

## 3D Reconstruction & Multi-view Geometry

### 2026-08

#### 2026-08-17 - Binarized High-Efficiency RAW Video Restoration and Beyond

**Authors:** Tianyu Zhu, Ying Fu, Hesong Li, Gengchen Zhang, Xin Yuan, Yulun Zhang
**Links:** [abs](https://arxiv.org/abs/2608.16756) - [pdf](https://arxiv.org/pdf/2608.16756)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>Abstract</summary>

RAW video restoration is fundamental to high-quality low-level perception and serves as the basis for a wide range of downstream vision applications. While binary neural networks (BNNs) enable efficient lightweight deployment for image enhancement, their deficiencies in modeling temporal coherence and activation value distributions hinder their effectiveness when applied to video scenarios. In this paper, we propose BinRVR, a binarized RAW video restoration framework that reduces computation and parameters by approximately 96% while incurring only about 4% performance degradation. Specifically, we present a Binarized Information Interaction Module (BIIM) to jointly model spatial and temporal information in an efficient and unified manner. Moreover, we develop a Distribution-Aware Binarized Convolution (DAB-Conv) that leverages the statistics of full-precision activations to mitigate quantization errors. The proposed framework further supports multi-bit quantization, enabling flexible accuracy-efficiency trade-offs across different hardware constraints. Extensive experiments demonstrate that our BinRVR achieves competitive performance compared with state-of-the-art binarized methods on RAW video restoration tasks, including low-light enhancement, denoising, deblurring, and super-resolution. We further explore the potential of our method on downstream video applications, including object detection and monocular depth estimation.

</details>

#### 2026-08-15 - TinyDETR-Pose: Towards End-to-End Real-Time Single-Stage 6DoF Object Pose Estimation with Lightweight Transformers

**Authors:** Paul Julius Kühn, Duc Anh Nguyen, Saptarshi Neil Sinha, Michael Weinmann, Arjan Kuijper
**Links:** [abs](https://arxiv.org/abs/2608.15297) - [pdf](https://arxiv.org/pdf/2608.15297)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, monocular depth

<details>
<summary>Abstract</summary>

Real-time 6DoF object pose estimation on resource-constrained hardware remains challenging, as accurate correspondence-based and refinement pipelines typically rely on non-differentiable PnP/RANSAC stages or costly iterative refinement, while recent foundation-model-based approaches incur inference costs that are prohibitive for edge deployment. We present TinyDETR-Pose, a lightweight, end-to-end, single-stage framework that jointly detects objects and regresses their full 6D pose in a single forward pass. Built on the efficient LW-DETR architecture, TinyDETR-Pose formulates detection and pose estimation as a set-prediction problem and attaches dedicated MLP heads for rotation, monocular depth, and projected object center regression to each decoder query, eliminating the need for PnP, NMS (non-maximum suppression), or iterative pose refinement. Object symmetries are handled through a ADD-S loss applied uniformly to all objects, without the need for object-specific loss schedules or separate geodesic/ADD supervision. In addition, predictions are assigned to ground truth using a symmetry-safe Hungarian matcher based on class and 2D spatial cues, yielding stable assignment under symmetry and depth ambiguity. On YCB-V, TinyDETR-Pose achieves a comparable ADD-S AUC of 85.9, while requiring up to 72.7% fewer parameters than other DETR-based single-stage pose-estimation approaches. Due to its compact design, TinyDETR-Pose runs in real time and achieves an inference latency of only ~4.5 ms per frame on an NVIDIA Jetson Nano using TensorRT, demonstrating that accurate end-to-end transformer-based 6D pose estimation can be made practical for edge deployment.

</details>

#### 2026-08-15 - Robust structure from motion for aerial-ground images via detector-free feature matching and multi-view track refinement

**Authors:** San Jiang, Hui Wang, Xing Zhang, Zhongwen Hu, Zhijun Wang, Ruisheng Wang, Wanshou Jiang, Qingquan Li
**Links:** [abs](https://arxiv.org/abs/2608.15251) - [pdf](https://arxiv.org/pdf/2608.15251)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, feature matching

<details>
<summary>Abstract</summary>

Integrated 3D reconstruction from aerial-ground images is essential for generating high-precision urban 3D models, yet severe variations in viewpoint, scale, and rotation make robust feature matching highly challenging. To address these limitations, this study introduces a rotation-robust detector-free matching network coupled with multi-view track refinement for incremental Structure from Motion (ISfM). The proposed workflow features four key modules. First, rotation-aware feature extraction replaces traditional convolutions with an Omnidirectional State Space Block (OSS Block) that selectively scans across eight symmetrical directions to model long-range spatial dependencies and synthesize rotation-invariant feature maps. Second, multi-scale attention transformation utilizes quadtree attention to build a hierarchical token pyramid that isolates high-association token regions and discards irrelevant areas, capturing long-range context with linear computational complexity. Third, bi-directional feature matching executes a symmetric coarse-to-fine matching scheme where coarse alignment computes dual-direction Softmax confidence matrices under mutual nearest neighbor constraints, and fine alignment uses a multi-layer perceptron to regress sub-pixel coordinate offsets. Finally, multi-view track refinement employs an integrated indexing structure to evaluate localized spatial proximity and link disjoint sub-tracks to the highest-confidence anchor point, ensuring stable feature repeatability across the ISfM pipeline. By using real aerial-ground datasets, experimental results demonstrate that the proposed method improves AUC at 5° pose error by 93.9% compared with LoFTR and achieves the highest precision in ISfM reconstruction, with the improved accuracy ranging from 27.6% to 32.7%. The proposed method provides a reliable solution for integrated 3D reconstruction of aerial-ground images.

</details>

#### 2026-08-13 - A Controlled Study of Self-Supervised Image and Video Pretraining under Limited Resources

**Authors:** Brunó B. Englert, Gijs Dubbelman
**Links:** [abs](https://arxiv.org/abs/2608.13183) - [pdf](https://arxiv.org/pdf/2608.13183)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Controlled Study of Self-Supervised Image and Video Pretraining under Limited Resources
- 作者：Brunó B. Englert、Gijs Dubbelman
- 出版日期：2026-08-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.13183

### 一句话总结
本文在受控资源条件下对比了多种图像与视频自监督学习目标，发现DINOv2风格预训练综合表现最佳，且将其与视频目标（如VideoMAE）结合会在语义任务上带来提升、但在几何任务上造成退化。

### 研究问题
在资源受限（数据、架构、计算预算均匹配）的情况下，图像与视频自监督学习（SSL）目标如何表现？不同SSL目标（对比、重建、特征预测、扩散）之间是否存在性能差异？联合训练图像-视频SSL目标是否能产生优于单一目标的效果？

### 核心思路/方法
作者在匹配的数据、架构和计算预算条件下，对图像与视频SSL目标进行受控对照研究。比较了对比学习（contrastive）、重建（reconstruction）、特征预测（feature-prediction）和扩散（diffusion）四类目标，并评估了单独训练以及联合训练的图像-视频SSL组合，在一系列图像与视频理解任务上进行评测。

### 主要贡献
- 在受控资源条件下系统对比了多种图像和视频SSL目标，填补了该场景下的比较空白。
- 发现DINOv2风格预训练在有限资源下综合性能最优。
- 揭示图像SSL（DINOv2）与视频SSL（如VideoMAE）联合训练可提升图像分类和分割性能，但会损害视频跟踪和相机位姿估计性能，表明语义表示与几何表示学习之间存在权衡。

### 局限性
摘要未提供足够信息，如具体数据集、模型规模、训练时长、评测任务细节及定量结果等均未给出。

### 阅读优先级
**中**。理由：该研究针对资源受限场景下的SSL目标比较具有实用价值，且揭示了联合训练带来的语义-几何权衡这一有意义的发现；但作者未提供定量实验细节，结论的普适性和可复现性无法从摘要评估，适合对SSL预训练策略感兴趣的读者阅读原文获取具体数据。

</details>

<details>
<summary>Abstract</summary>

Visual foundation models are a cornerstone of image and video understanding but typically require large amounts of data and computation. The current scale required for pretraining visual foundation models may be unsustainable or unnecessary, and significant benefits arise when effective models can be obtained with fewer resources. To better understand how self-supervised learning (SSL) objectives behave under resource constraints, we conduct a controlled study of image and video SSL objectives under matched data, architecture, and compute budgets. We compare contrastive, reconstruction, feature-prediction, and diffusion objectives and evaluate both standalone and jointly trained image-video SSL formulations across a diverse set of image and video understanding tasks. Our results show that DINOv2-style pretraining consistently provides the strongest overall performance under limited resources. Furthermore, combining DINOv2 with video SSL objectives such as VideoMAE substantially improves image classification and segmentation performance, but degrades video tracking and camera-pose estimation performance, revealing an important tradeoff between semantic and geometric representation learning. These findings suggest that combining image and video SSL objectives can be beneficial in resource-limited settings, while highlighting the need for improved methods that better balance semantic, temporal, and geometric supervision.

</details>

#### 2026-08-13 - Fast Iterative Five point Relative Pose Estimation

**Authors:** Johan Hedborg, Michael Felsberg
**Links:** [abs](https://arxiv.org/abs/2608.13114) - [pdf](https://arxiv.org/pdf/2608.13114)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fast Iterative Five point Relative Pose Estimation
- 作者：Johan Hedborg, Michael Felsberg
- 出版日期：2026-08-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.13114

### 一句话总结
本文提出一种基于Powell's Dog Leg算法的快速迭代式五点相对位姿估计方法，在精度与Nister算法相当的情况下，速度约为其两倍。

### 研究问题
如何加速五点法相对位姿估计，同时保持与当前最先进方法相当的精度，并使其易于扩展至多于五个点的情形。

### 核心思路/方法
- 提出一种新的迭代方法，基于Powell's Dog Leg算法（一种非线性优化方法）。
- 该方法在RANSAC框架下使用，具备与Nister五点法相同的精度，但速度约为其两倍。
- 方法易于扩展到多于五个点的情况，同时保持高效的误差度量，因此也适合作为细化（refinement）步骤。
- 在三种具有已知真值的数据集上进行了系统评估。

### 主要贡献
1. 提出一种新的快速迭代式五点相对位姿估计算法。
2. 在精度不降低的前提下，速度约为Nister算法的两倍。
3. 算法可自然扩展至超过五个点，适合作为位姿细化步骤。
4. 在三种已知真值的数据集上进行了系统评估，验证了方法的有效性。

### 局限性
摘要未提供足够信息（例如：未提及方法对噪声、离群点的具体鲁棒性表现，未给出具体数据集类型与规模，也未说明与Nister算法以外的其他方法（如七点法、八点法）的比较情况）。

### 阅读优先级
**中**
理由：该工作针对经典五点相对位姿估计问题提出性能改进，方向明确且速度提升显著，对从事三维重建、多视图几何的读者有一定参考价值。但摘要仅提供了性能对比的高层结论，缺乏具体的实验数值和评估细节，适合作为速读参考，而非必读精读文献。

</details>

<details>
<summary>Abstract</summary>

Robust estimation of the relative pose between two cameras is a fundamental part of Structure and Motion methods. For calibrated cameras, the five point method together with a robust estimator such as RANSAC gives the best result in most cases. The current state-of-the-art method for solving the relative pose problem from five points is due to Nister [9], because it is faster than other methods and in the RANSAC scheme one can improve precision by increasing the number of iterations. In this paper, we propose a new iterative method, which is based on Powell's Dog Leg algorithm. The new method has the same precision and is approximately twice as fast as Nister's algorithm. The proposed method is easily extended to more than five points while retaining a efficient error metrics. This makes it also very suitable as an refinement step. The proposed algorithm is systematically evaluated on three types of datasets with known ground truth.

</details>

#### 2026-08-13 - Topology-Unified 2D Pose Estimation across Intact, Residual and Prosthetic Limbs

**Authors:** Tianye Qi, Tengyue Zhang, Jiaying Ying, Tianqing Zhu, Xin Yu
**Links:** [abs](https://arxiv.org/abs/2608.13047) - [pdf](https://arxiv.org/pdf/2608.13047)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Topology-Unified 2D Pose Estimation across Intact, Residual and Prosthetic Limbs
- 作者：Tianye Qi, Tengyue Zhang, Jiaying Ying, Tianqing Zhu, Xin Yu
- 出版日期：2026-08-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.13047

### 一句话总结
本文提出统一拓扑表示的ProPose基准和结构感知的ProLoss损失函数，以改善包含健全肢体、义肢和残肢的人体姿态估计性能。

### 研究问题
现有主流人体姿态估计数据集存在严重的表示偏差，主要面向健全人，对义肢（如跑步刀片）和未安装假肢的残肢缺乏统一的标注协议，导致模型在这些多样化肢体形态上难以泛化，且长尾分布下关节分类精度不足。

### 核心思路/方法
1. 提出**ProPose**基准：设计一种新型标注协议，在单一框架内统一生物学肢体、多种义肢和物理缺失肢体的拓扑表示。
2. 设计**Real-to-Synthetic数据扩充管道**：针对真实义肢图像稀缺且呈极端长尾分布的问题，显式合成并扩充该类样本。
3. 提出**ProLoss**损失函数：结构感知目标函数，强制同一肢体内部关键点之间的依赖关系，防止模型在机械结构上幻觉出不存在的关节。

### 主要贡献
- 引入大规模基准ProPose，首次在统一拓扑框架下覆盖健全、残肢与义肢场景。
- 提出Real-to-Synthetic数据扩充策略，缓解义肢数据的极端长尾问题。
- 设计ProLoss结构感知损失，约束关键点间依赖关系，避免不真实预测。
- 实验表明，在不损失坐标定位精度的前提下，长尾义肢关节分类准确率提升2%至6%。

### 局限性
摘要未提供足够信息。具体而言，关于ProPose数据集的规模与构成细节、各方法的消融实验对比、具体实验设置（如backbone、训练配置）以及在不同下游任务上的泛化验证等均未在摘要中提及。

### 阅读优先级
**中**。理由：该工作面向人体姿态估计中的包容性/公平性研究，属于较细分的进阶方向，当前可能不是通用姿态估计领域的主流热点；但问题定义清晰、方法具有工程创新性，且摘要中的量化提升明确，适合研究义肢场景或关注数据长尾问题的读者参考。

</details>

<details>
<summary>Abstract</summary>

Driven by the availability of large-scale datasets, Human Pose Estimation (HPE) plays a critical role in numerous downstream tasks. However, mainstream benchmarks exhibit severe representation bias, predominantly featuring able-bodied individuals. While a few pioneering datasets have attempted to address limb differences, their annotation protocols fail to generalize, struggling to represent specialized mechanical structures like running blades or unprosthetized residual limbs. To bridge this gap, we introduce ProPose, a large-scale benchmark featuring a novel annotation protocol that unifies the topological representation of biological limbs, diverse prostheses, and physical absences within a single framework. Because real-world prosthetic images are inherently scarce and exhibit extreme long-tail distributions, we design a Real-to-Synthetic data expansion pipeline to explicitly synthesize and expand the underrepresented cases. However, simply training existing models on this enriched dataset often leads to suboptimal solutions, as they estimate each keypoint independently and might hallucinate non-existent joints on mechanical structures. To resolve this, we propose ProLoss, a structure-aware objective that enforces keypoint dependencies within a single limb to prevent unrealistic limb predictions. Extensive experiments demonstrate that our approach improves the classification accuracy of long-tail prosthetic joints by 2% to 6% without compromising spatial coordinate localization performance. This work sets a foundation for inclusive pose estimation, unlocking new possibilities for understanding the interactions between human bodies and assistive devices.

</details>

#### 2026-08-13 - AMR-Pose: An Active LED Marker-Based Relative Pose Estimation Framework With Probabilistic Switching PnP for Cooperative AUVs

**Authors:** Zeyu Sha, Xiaorui Wang, Mingyang Yang, Feitian Zhang
**Links:** [abs](https://arxiv.org/abs/2608.12866) - [pdf](https://arxiv.org/pdf/2608.12866)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, robotics, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AMR-Pose: An Active LED Marker-Based Relative Pose Estimation Framework With Probabilistic Switching PnP for Cooperative AUVs
- 作者：Zeyu Sha, Xiaorui Wang, Mingyang Yang, Feitian Zhang
- 出版日期：2026-08-13T06:29:43Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.12866

### 一句话总结
本文提出AMR-Pose，一种基于主动LED标记与概率切换PnP的水下自主机器人（AUV）相对位姿估计框架，通过紧凑标记模块与自适应估计机制在复杂水下环境中实现稳健的六自由度相对定位。

### 研究问题
如何在存在浑浊、光照变化、反射和间歇性特征遮挡等严重光学退化条件下，实现合作AUV之间可靠、鲁棒的基于视觉的相对位姿估计。

### 核心思路/方法
- 设计一个紧凑的主动LED标记模块，包含一个红色中心LED和三个蓝色外围LED，安装在领航AUV上，以在复杂水下条件下提供独特的视觉特征。
- 基于检测到的标记观测，开发概率切换PnP估计器（PSwPnP），结合SE(3)上的李群位姿传播、概率标记关联和可见性自适应测量融合。
- 框架根据标记可见性动态调整估计过程，在部分观测和可见性切换期间保持几何一致性和时间稳定性。

### 主要贡献
- 提出AMR-Pose框架，基于主动LED标记实现水下合作AUV的相对位姿估计。
- 开发紧凑的LED标记模块，提供水下复杂环境中可辨识的视觉特征。
- 设计概率切换PnP估计器（PSwPnP），融合李群位姿传播、概率关联与自适应融合。
- 通过水槽实验（运动捕捉系统提供真值）验证了框架在挑战性水下条件下的准确性、平滑性和鲁棒性。
- 闭环领航-跟随实验证明其在合作水下机器人实时相对位姿反馈中的可行性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作面向水下多机器人协作中的关键难题（光学退化下的相对定位），提出了结合主动标记设计与概率切换PnP的完整解决方案，并通过水槽真值实验和闭环实验验证了实用性。对于从事水下机器人、视觉定位或多机器人协同的研究人员具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Reliable relative pose estimation between autonomous underwater vehicles (AUVs) is critical for cooperative ocean exploration, sampling, and multi-robot coordination. However, achieving robust vision-based relative localization in underwater environments remains challenging due to severe optical degradation, including turbidity, illumination variations, reflections, and intermittent feature occlusions. This paper presents AMR-Pose, an active LED marker-based relative pose estimation framework for cooperative AUVs. A compact marker module consisting of one red central LED and three blue peripheral LEDs is developed and integrated onto the leader AUV to provide distinctive visual features under complex underwater conditions. Building upon the detected marker observations, a probabilistic switching Perspective-n-Point estimator (PSwPnP) is developed by combining Lie-group pose propagation on $SE(3)$, probabilistic marker association, and visibility-adaptive measurement fusion for robust six-degree-of-freedom relative pose estimation. The proposed framework dynamically adapts the estimation process according to marker visibility, maintaining geometric consistency and temporal stability during partial observations and visibility transitions. Extensive water-tank experiments with motion-capture ground truth validate that AMR-Pose achieves accurate, smooth, and robust relative pose estimation under challenging underwater conditions. Closed-loop leader-follower experiments further demonstrate its feasibility for real-time relative pose feedback in cooperative underwater robotics.

</details>

#### 2026-08-12 - MV2: Multi-View Multi-Vehicle Driving Dataset for Novel View Synthesis

**Authors:** Sanjay Bhargav Dharavath, Hanvitha Saraswathi Mukkamala, Faizan Farooq Khan, Ioannis Kakogeorgiou, Aditya Arun, C V Jawahar, Zakaria Laskar
**Links:** [abs](https://arxiv.org/abs/2608.12442) - [pdf](https://arxiv.org/pdf/2608.12442)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, camera pose estimation, pose estimation, novel view synthesis, view synthesis, differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MV2: Multi-View Multi-Vehicle Driving Dataset for Novel View Synthesis
- 作者：Sanjay Bhargav Dharavath, Hanvitha Saraswathi Mukkamala, Faizan Farooq Khan, Ioannis Kakogeorgiou, Aditya Arun, C V Jawahar, Zakaria Laskar
- 出版日期：2026-08-12T16:02:32Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：https://arxiv.org/abs/2608.12442

### 一句话总结
本文提出MV2数据集与基准，通过多车辆（汽车、摩托车、无人机）同步轨迹拍摄，评估新视角合成方法在动态城市场景中大幅视点变化下的性能。

### 研究问题
新视角合成在真实驾驶场景中因稀疏采集视角、动态物体和有限的多轨迹数据而难以应用，现有数据集多为单一轨迹，难以评估视点大幅变化下的模型表现。

### 核心思路/方法
构建MV2数据集：使用汽车、摩托车和无人机三台设备同步采集，各自沿不同但同步的轨迹行驶；训练时使用某一车辆的相机流，测试时换用另一车辆的相机流，从而引入大幅视点变化。所有序列通过Structure-from-Motion配准，并使用手动像素级对应标注验证相机位姿，最终得到50个高质量场景、12000张图像。在此基础上，对近期NVS方法和相机位姿估计方法进行基准测试。

### 主要贡献
- 提出MV2数据集，包含50个高质量场景、12000张图像，支持动态城市场景下大幅视点变化的NVS评估。
- 设计多车辆交叉轨迹的基准协议，使训练和测试视点差异显著大于现有单轨迹数据集。
- 通过基准测试发现：NVS性能随视点差异增大而下降；前馈位姿估计器明显落后于优化方法，验证了MV2作为驾驶NVS测试床的严格性。
- 公开数据集、基准协议及项目资源。

### 局限性
摘要未提供足够信息：未说明数据集在场景多样性（如天气、光照、交通密度）上的覆盖范围，也未提及与现有驾驶数据集的定量对比，或方法失败的典型案例分析。

### 阅读优先级
**中**。理由：该工作主要贡献在于新数据集与基准，对从事驾驶场景新视角合成或位姿估计的研究者有一定参考价值，但属于资源型工作而非新方法提出；若不在该领域，则关联度有限。

</details>

<details>
<summary>Abstract</summary>

Differentiable rendering has advanced novel view synthesis (NVS), yet applying it to real-world driving remains difficult due to sparse capture viewpoints, dynamic objects, and limited multi-trajectory data. We introduce the Multi-View Multi-Vehicle (MV2) dataset and benchmark for evaluating NVS models under large viewpoint changes in dynamic urban scenes. MV2 features synchronized captures from a car, scooter, and drone, each following distinct yet synchronized trajectories. Training NVS methods on one vehicle's camera stream and testing on another enables evaluation under substantially larger viewpoint variations than existing single-trajectory datasets. All sequences are registered via Structure-from-Motion and camera poses verified using manual pixel-level correspondence annotations, yielding 50 high-quality scenes with 12000 images. Benchmarking recent NVS and camera pose estimation methods shows that NVS performance degrades with increasing viewpoint disparity, and that feed-forward pose estimators notably lag behind optimization-based approaches, highlighting MV2 as a rigorous testbed for NVS in driving. The dataset, benchmark protocol, and project resources are available at https://mv2-dataset.github.io/.

</details>

#### 2026-08-12 - HSTGFormer: Hyper Spatial-Temporal Graph Transformer for 3D Human Pose Estimation

**Authors:** Ruochen Li, Shuang Chen, Wenke E, Farshad Arvin, Amir Atapour-Abarghouei
**Links:** [abs](https://arxiv.org/abs/2608.12187) - [pdf](https://arxiv.org/pdf/2608.12187)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HSTGFormer: Hyper Spatial-Temporal Graph Transformer for 3D Human Pose Estimation
- 作者：Ruochen Li, Shuang Chen, Wenke E, Farshad Arvin, Amir Atapour-Abarghouei
- 出版日期：2026-08-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.12187

### 一句话总结
本文提出一种图增强的Transformer框架HSTGFormer，通过超时空图将空间与时间推理耦合成局部图聚合，实现高效且精度高的单目3D人体姿态估计。

### 研究问题
现有基于Transformer的3D人体姿态估计方法通常将空间和时间推理分为两个独立阶段，这可能导致对动作中固有的统一时空依赖建模不足，并在时间建模之前压缩了帧级结构信息。本文旨在解决这一问题，构建更统一的时空关联推理方式。

### 核心思路/方法
- 提出**Hyper Spatial-Temporal Graph (HSTG)**：将每帧的骨架图扩展到时间邻域，将全局时空推理分解为围绕每个“关节点-时间”节点的局部时空感受野，实现结构感知的耦合推理，同时保留局部结构运动信息。
- 引入**Adaptive Dual-Scale Temporal Graph (ADSTG)**：在互补的短窗口和长窗口内捕获关节点特定的时间依赖。
- 设计轻量级的**节点级融合模块**：自适应地整合两种图表示，用于每个“关节点-时间”节点。

### 主要贡献
- 提出将时空推理重新表述为“关节点-时间”节点上的局部耦合图聚合，替代传统分离式时空建模。
- 设计HSTG实现局部结构感知的耦合时空推理，并保留局部结构运动信息。
- 引入ADSTG与节点级融合模块，增强跨尺度时间依赖建模。
- 在Human3.6M和MPI-INF-3DHP数据集上验证了强精度与高计算效率（摘要提供实验范围，具体数值未给出）。

### 局限性
摘要未提供足够信息，具体局限性（如对遮挡、极端姿态的鲁棒性、长序列效率等）未在摘要中说明。

### 阅读优先级
**高**  
理由：该工作针对3D人体姿态估计中时空建模分离的核心问题提出了统一的耦合图推理框架，并声称在主要基准上取得强精度与高效率，方法设计具有新意，对关注人体姿态估计和时空建模的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Transformer-based methods have achieved strong performance in monocular 3D human pose estimation, but most existing approaches organise spatial and temporal reasoning as separate stages, which may weaken unified spatial-temporal interdependencies inherent in human motion and compress frame-level structural information before temporal modelling. In this paper, we propose HSTGFormer, a graph-enhanced Transformer framework that reformulates spatial-temporal reasoning as localised coupled graph aggregation over joint-time nodes. Specifically, HSTGFormer introduces a Hyper Spatial-Temporal Graph (HSTG), which decomposes global spatial-temporal reasoning into local spatial-temporal receptive fields around individual joint-time nodes by extending per-frame skeleton graphs into temporal neighbourhoods, thereby enabling structure-aware coupled reasoning while preserving local structural motion information. It further incorporates an Adaptive Dual-Scale Temporal Graph (ADSTG) to capture joint-specific temporal dependencies over complementary short- and long-range windows. A lightweight node-wise fusion module further adaptively integrates the two graph representations for each joint-time node. Experiments on Human3.6M and MPI-INF-3DHP show that HSTGFormer achieves strong accuracy with high computational efficiency.

</details>

#### 2026-08-12 - Repurposing RGB-based Foundation Model for Depth Estimation on Thermal Images Using Hierarchical Supervision

**Authors:** Jie Hong, Tingtian Li, Xuesong Li, Xiao Li
**Links:** [abs](https://arxiv.org/abs/2608.11564) - [pdf](https://arxiv.org/pdf/2608.11564)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Repurposing RGB-based Foundation Model for Depth Estimation on Thermal Images Using Hierarchical Supervision
- 作者：Jie Hong, Tingtian Li, Xuesong Li, Xiao Li
- 出版日期：2026-08-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.11564

### 一句话总结
本文提出RGB-HS框架，通过从RGB基础模型向热成像编码器施加层级监督，以提升热成像深度估计性能。

### 研究问题
如何更充分地利用RGB基础模型在热成像深度估计任务中的表征能力，尤其是其编码器中蕴含的层级结构信息。

### 核心思路/方法
- 将热成像编码器替换为RGB基础模型，并引入同架构的RGB分支作为教师网络。
- 在两个编码器的多个层级之间进行token对齐，使热成像学生分支同时获得结构精度与语义抽象信息。
- 引入验证机制，根据RGB图像质量对教师分支的token进行加权，优化对齐过程。

### 主要贡献
- 提出RGB-HS框架，利用层级监督从RGB基础模型迁移知识到热成像深度估计。
- 通过在多个层级进行token对齐，更全面地利用基础模型的层级表征。
- 引入基于RGB图像质量的验证机制，细化对齐过程。
- 在公开基准上验证了该方法的竞争力，表明其能更有效地挖掘RGB基础模型的表征能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向热成像深度估计这一特定应用场景，方法核心在于层级监督与跨模态对齐，思路有一定新颖性，但摘要未给出定量结果或与现有方法的详细对比，读者若从事多模态深度估计或基础模型迁移研究可关注，否则优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

Depth estimation from thermal images is highly valuable for robotic applications in adverse conditions, such as nighttime and rainy weather. Recent studies have sought to transfer knowledge from RGB-based foundation models to thermal modalities, yet the rich hierarchical representations these models encode remain underutilized. To address this limitation, we propose RGB-HS, a novel framework for thermal-image depth estimation that leverages hierarchical supervision from an RGB-based foundation model. Specifically, we first replace the baseline thermal encoder with a foundational model and introduce a parallel RGB branch that also employs a foundational model as an encoder of the same architecture, taking RGB images as input. The alignment is then performed across multiple levels between the tokens of the two encoders, allowing the thermal student branch to capture both structural precision and semantic abstraction from the RGB teacher branch. Furthermore, we introduce verification to refine the alignment process by weighting tokens from the RGB branch based on RGB image quality. Extensive experiments on the popular benchmark demonstrate that RGB-HS achieves competitive performance and more effectively exploits the representational capacity of RGB-based foundation models for depth estimation on thermal images.

</details>

#### 2026-08-11 - Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives

**Authors:** Songlin Du, Xiaoyong Lu, Zeyu Wu, Xiaobo Lu, Guobao Xiao, Bin Fan, Jiayi Ma, Takeshi Ikenaga
**Links:** [abs](https://arxiv.org/abs/2608.11093) - [pdf](https://arxiv.org/pdf/2608.11093)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives（跨视角特征匹配：综述、基准测试与基础模型视角）
- 作者：Songlin Du, Xiaoyong Lu, Zeyu Wu, Xiaobo Lu, Guobao Xiao, Bin Fan, Jiayi Ma, Takeshi Ikenaga
- 出版日期：2026-08-11
- 分类：3D重建与多视角几何
- 链接：https://arxiv.org/abs/2608.11093

### 一句话总结
本文是对跨视角特征匹配领域的系统性综述，构建了统一分类体系并对代表性方法进行了同协议基准测试，着重分析了视觉基础模型对该领域的影响与未来方向。

### 研究问题
跨视角特征匹配领域存在以下核心问题：问题定义、模型架构、训练范式和评估协议高度分散，缺乏统一理解框架；该领域正从任务特化模型向统一化、可泛化对应模型演进，但演进脉络尚不清晰；视觉基础模型（VFMs）的出现带来了新机遇，但缺乏系统分析。

### 核心思路/方法
- 提出一个结构化分类体系（taxonomy），涵盖五个维度：特征提取、单类型特征匹配器、多类型特征匹配器、基于视觉基础模型（VFM）的方法、训练策略与鲁棒估计。
- 梳理近年进展，提炼关键设计原则，重点阐明领域向统一化和可泛化对应模型转变的趋势。
- 在统一评估协议下，对代表性最先进方法进行实验基准测试，实现公平全面的性能对比。

### 主要贡献
1. 提出了一个统一的跨视角特征匹配分类体系，为领域内方法提供结构化分析与比较框架。
2. 系统梳理了该领域十年来的演进历程，总结了从任务特化到统一可泛化模型转变的关键设计原则。
3. 在一致协议下提供了多方法基准测试结果，实现公平的性能对比。
4. 讨论了开放挑战与未来方向，包括效率、极端条件下的鲁棒性以及跨域泛化问题。

### 局限性
摘要未提供具体实验设置、数据集规模、性能数值等细节，也未提及综述纳入的论文数量范围。关于基准测试的具体结果、局限性和失败案例，摘要未提供足够信息。

### 阅读优先级
**高**。理由如下：
1. 本文具备综述+基准测试双重属性，是获取领域全景和横向对比的关键资源。
2. 作者团队来自多所机构（如东南大学、武汉大学、早稻田大学等），且该方向处于视觉基础模型与几何匹配的交叉热点，引用概率高。
3. 统一分类体系对后续做系统定位和实验对照有直接参考价值。若读者只需单一算法细节，可跳读对应章节。

</details>

<details>
<summary>Abstract</summary>

Cross-view feature matching aims to establish reliable correspondences across images with large viewpoint variations. Over the past decade, the field has evolved from task-specific models toward increasingly unified and generalizable correspondence models, with recent progress further driven by the emergence of vision foundation models (VFMs). Despite these advances, existing studies remain highly diverse in their problem formulations, model architectures, training paradigms, and evaluation protocols, making it difficult to obtain a unified understanding of the field. In this survey, we present a unified review of cross-view feature matching. We first introduce a structured taxonomy covering feature extraction, single-type feature matcher, multi-type feature matcher, VFMs based methods, training strategy and robust estimation, providing a coherent framework for analysis and comparison. We further examine recent advances, distilling key design principles and highlighting the shift toward unified and generalizable correspondence models. We also provide a unified experimental benchmarking of representative state-of-the-art methods under consistent protocols, enabling fair and comprehensive performance comparisons. In addition, we discuss open challenges and future directions, including efficiency, robustness under extreme conditions, and cross-domain generalization. This survey aims to provide a comprehensive and structured reference for understanding the evolution, current landscape, and future development of cross-view feature matching in the era of vision foundation models.

</details>

#### 2026-08-11 - GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting

**Authors:** Huaiyuan Weng, Chul Min Yeum, Su-Min Kang
**Links:** [abs](https://arxiv.org/abs/2608.10938) - [pdf](https://arxiv.org/pdf/2608.10938)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, rendering, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting
- 作者：Huaiyuan Weng, Chul Min Yeum, Su-Min Kang
- 出版日期：2026-08-11T14:06:51Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10938

### 一句话总结
GS-CPE 提出一种基于 3D 高斯泼溅的粗到细框架，将几何粗姿态估计与 3DGS 重渲染优化结合，实现统一且高精度的 6 自由度相机姿态估计。

### 研究问题
如何在保持鲁棒泛化能力的同时，提高视觉定位中 6 自由度相机姿态估计的精度，解决传统方法在准确性和泛化性之间难以兼顾的问题。

### 核心思路/方法
- 采用粗到细（coarse-to-fine）的两阶段框架。
- 粗阶段：通过检索引导（retrieval-guided）的几何姿态估计，在 3D 高斯泼溅（3DGS）场景表示上获得初始粗略姿态。
- 细阶段：通过最小化一个可见性感知的掩码 RGB 重投影（warping）目标函数，在多尺度优化框架中进行姿态细化，并引入自适应重渲染（adaptive re-rendering）机制。

### 主要贡献
- 提出 GS-CPE，一个统一了基于几何的粗姿态估计与基于 3DGS 重投影的细姿态优化的 6-DoF 姿态估计框架。
- 引入可见性感知的掩码 RGB 重投影目标函数及多尺度优化策略，配合自适应重渲染进行精细化。
- 在多个室内外基准（7Scenes、Cambridge Landmarks、FAST-LIVO2）及自建数据集上取得领先的准确性与泛化性能。

### 局限性
摘要未提供足够信息，无法判断具体局限性（如计算开销、对动态场景的适应性、对初始姿态的敏感度等）。

### 阅读优先级
**高**。理由：该工作提出了一种结合 3DGS 的粗到细姿态估计统一框架，涉及新颖的可见性感知优化目标，且在多个基准上报告了先进的准确性与泛化能力。研究主题面向视觉定位与神经场景表示的前沿交叉，对相关领域研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Despite substantial progress in visual localization, from scene coordinate regression to direct camera pose regression, achieving both robust generalization and high accuracy remain challenging. This study introduces GS-CPE (Gaussian Splatting based Camera Pose Estimation), a coarse-to-fine framework for 6-DoF camera pose estimation that unifies geometry-based coarse pose estimation with robust 3D Gaussian Splatting (3DGS) warping based pose refinement. GS-CPE first estimates a coarse pose via retrieval-guided geometric pose estimation on a 3DGS scene representation, then refines it by minimizing a visibility aware masked RGB warping objective in a multi-scale optimization framework, with adaptive re-rendering. Extensive experiments on indoor and outdoor benchmarks including 7Scenes, Cambridge Landmarks, FAST-LIVO2 datasets, and a custom dataset demonstrate state-of-the-art performance, consistently outperforming in both accuracy and generalization.

</details>

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-17 - SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis

**Authors:** Yejun Zhang, Zihan Wang, Xu Ji, Yihao Wang, Yuxin Hou, Junyuan Fang, Juho-Matti Kilpeläinen, Arno Solin, Hamed Rezazadegan Tavakoli, Esa Rahtu, Juho Kannala
**Links:** [abs](https://arxiv.org/abs/2608.16863) - [pdf](https://arxiv.org/pdf/2608.16863)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, 3DGS, novel view synthesis, view synthesis, rendering

<details>
<summary>Abstract</summary>

Generating photorealistic novel views from unposed images requires both 3D geometric understanding and the ability to synthesize unseen content. A natural strategy combines feed-forward 3DGS reconstruction with multi-view diffusion. Yet prior pipelines extract at most one signal from the reconstruction, either pixel rendering or learned features, while none exploits per-Gaussian visibility for occlusion-aware reference selection. This *information disconnect* leaves renderable geometry, visibility cues, and learned features unused. SplatGuide closes this disconnect by reusing a single 3DGS scene across three complementary roles. Rendered images provide pixel-aligned geometric conditioning. Per-Gaussian source-view indices are rendered into a target-view voting map for occlusion-aware reference selection. Reconstruction tokens supply feature-level guidance via cross-attention. All three signals derive from the same reconstruction forward pass. Across RealEstate10K, DL3DV, Tanks-and-Temples, and Mip-NeRF 360, SplatGuide achieves state-of-the-art pose-free novel view synthesis. On RealEstate10K, with a moderate number of input views, it surpasses the ground-truth-pose baseline.

</details>

#### 2026-08-17 - LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting

**Authors:** Louen Pottier
**Links:** [abs](https://arxiv.org/abs/2608.16324) - [pdf](https://arxiv.org/pdf/2608.16324)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, splatting, simulation

<details>
<summary>Abstract</summary>

We present LaGSplat (Latent Lagrangian Gaussian Splatting), a framework that infers interactive, physics-governed dynamics from one or a few monocular videos. At inference it lets a user push on the filmed object, rigid or deformable, with an external force that was never measured, annotated, or seen during training. This is possible because a low-dimensional latent state $\mathbf{q} \in \mathbb{R}^d$ plays two roles at once: it is the generalised coordinate of a learned dissipative Lagrangian and the conditioning variable of a Gaussian Splatting decoder. The inductive bias of this decoder, whose primitives are explicit points $μ_i(\mathbf{q})$ that move with the object, is what lets a force $f$ applied in the image pull back into a latent generalised force $J(\mathbf{q})^\top f$ and enter the equations of motion, which pixel-space (CNN) or neural-field (NeRF) decoders cannot do. We validate LaGSplat on test cases of increasing difficulty, from rigid to deformable and from autonomous to forced real systems, combining monocular video and sensor measurements. We further demonstrate interactive use: forces of arbitrary magnitude and direction can be applied to the reconstructed object at any time, its response rendered in real time, in 2D or 3D. Assuming a dissipative Euler-Lagrange equation over a few generalised coordinates trades generality for a bounded, plausible response to unseen forces, where an unconstrained predictor diverges.

</details>

#### 2026-08-17 - Beyond Similarity Matching: Structured Reasoning for Open-Vocabulary Referring Segmentation in 3DGS

**Authors:** Yizhao Wang, Xinfa Wang, Jingbo Wang, Jingbo Wang, Guantao Zhang, Yafeng Han, Guohong Gao, Yuhe Xia
**Links:** [abs](https://arxiv.org/abs/2608.16103) - [pdf](https://arxiv.org/pdf/2608.16103)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, splatting

<details>
<summary>Abstract</summary>

Open-vocabulary referring segmentation in 3D Gaussian Splatting (3DGS) requires a neural model to select Gaussian primitives according to free-form language expressions. Existing 3DGS-based methods usually rely on global text-region similarity, which is weak for queries involving attributes, reference objects, spatial relations, and fine-grained parts. This often causes target-reference confusion, granularity mismatch, part-whole leakage, and relation violations. We propose QAGaussian, a query-adaptive neural reasoning framework for language-guided Gaussian primitive selection. QAGaussian first learns query-conditioned multi-scale Gaussian slots as differentiable candidates whose receptive fields are shaped by the input expression. It then builds a relation-aware slot graph with language-conditioned edge weighting to propagate target-reference, attribute, part-whole, and contextual evidence. A granularity-adaptive router softly combines region-level, object-level, part-level, attribute-aware, and relation-aware mask branches, followed by relation-constrained refinement for spatial, part-whole, attribute, and geometric consistency. QAGaussian is pretrained only on Mosaic3D-5.6M for Gaussian-text alignment and evaluated on independent benchmarks without target-dataset fine-tuning. It achieves 47.2 Avg. mIoU and 63.2 Avg. F1, outperforming the strongest 3DGS referring baseline by 2.7 mIoU points and 2.9 F1 points. It also improves Part-mIoU from 38.6 to 43.4, Rel-mIoU from 44.4 to 50.8, and reduces target-reference confusion from 10.8 to 7.4. These results demonstrate that query-conditioned slot learning, relation-aware graph reasoning, and adaptive routing provide an effective neural modeling strategy for open-vocabulary referring segmentation in 3DGS. The code is available at https://github.com/zqeslwyz/QAGaussian.

</details>

#### 2026-08-16 - RoofGS: Roofline-Guided End-to-End Acceleration of 3D Gaussian Splatting

**Authors:** Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao
**Links:** [abs](https://arxiv.org/abs/2608.15785) - [pdf](https://arxiv.org/pdf/2608.15785)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel-view synthesis but remains limited on GPUs at high resolutions. Through a stage-wise Roofline characterization, we identify two distinct hardware bottlenecks: global memory traffic dominates the front end, whereas instruction throughput limits rasterization. Guided by this analysis, we develop RoofGS, a rendering framework that applies bottleneck-specific optimizations rather than generic kernel acceleration. For the memory-bound front end, we design a resolution-adaptive quantized depth sorting key that compresses each key to 32 bits. For the compute-bound rasterizer, we introduce a range-aware bit-level fast exponential approximation tailored to the bounded exponent range after opacity culling, with a derived per-pixel error bound. These two core techniques are complemented by additional optimizations (kernel fusion, compact attribute storage, culling, dual-pixel evaluation) that additionally reduce memory traffic and improve instruction-level parallelism. Experiments show that RoofGS achieves a 10.1$\times$ end-to-end speedup over 3DGS at 4K on an RTX 4090, increasing throughput from 61 to 616 FPS, with only a 0.028 dB PSNR loss.

</details>

#### 2026-08-16 - Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats

**Authors:** Bin Ren, Qi Ma, Yue Li, Zongyan Han, Yidi Li, Yuqian Fu, Rao Muhammad Anwer, Theo Gevers, Fahad Shahbaz Khan, Salman Khan
**Links:** [abs](https://arxiv.org/abs/2608.15651) - [pdf](https://arxiv.org/pdf/2608.15651)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) represents 3D content with anisotropic primitives that jointly encode geometry and appearance. Fixed-budget encoders consume sampled observations of Gaussian assets, so the same object may be observed through different primitive realizations. Existing self-supervised methods mainly reconstruct masked Gaussian attributes, tying supervision to one sampled realization and requiring an input-space decoder. Latent prediction offers an alternative, but its application to Gaussian tokens requires targets that accommodate coupled attributes and heterogeneous spatial support. We introduce Gaussian-JEPA, which predicts representations of held-out Gaussian token blocks from visible context. An online encoder processes the context, while a shared exponential-moving-average encoder supplies stop-gradient features for multi-scale targets. Complementary target projections and feature-space grounding provide latent supervision without reconstructing Gaussian attributes. We evaluate the features under Gaussian resampling, partial observations, and renderable shape completion, together with transfer to part segmentation and object classification. Compared with matched reconstruction pretraining, Gaussian-JEPA is more consistent across resampled inputs, retains more instance information under partial observations, and provides stronger frozen features for Gaussian completion. These results support latent prediction as an effective objective for reusable 3D Gaussian representations. Code is on the project page (https://amazingren.github.io/Gaussian-JEPA/).

</details>

#### 2026-08-15 - HistReNeRF: Historic Image Relocalisation within Contemporary Neural Radiance Field Reconstructions

**Authors:** Benjamin T. Hughes, Stuart James
**Links:** [abs](https://arxiv.org/abs/2608.15420) - [pdf](https://arxiv.org/pdf/2608.15420)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, radiance

<details>
<summary>Abstract</summary>

Relocalising archival photographs within a contemporary scene model is challenging because historic and modern views can differ in photographic appearance, visible objects, and spatial layout. Therefore, we present HistReNeRF, a framework that estimates the 6-DoF pose of a historic photograph by matching adapted DINOv2 patch features to candidate rays sampled from a contemporary Neural Radiance Field (NeRF) reconstruction. The continuous representation of a NeRF provides a queryable scene interface from which candidate rays can be sampled and matched, enabling domain adaptation between historic photography and contemporary images directly in the feature representation used for localisation. We evaluate embedding-space-based domain adaptation against pixel-space methods on a new cross-temporal dataset comprising 10,545 contemporary street-level images and 230 archival photographs from three European landmarks. Embedding-space adaptation reduces translation and rotation errors by an average of 11% and 16%, respectively, across the three scenes. These results show that neural scene relocalisation provides a natural interface for feature-space adaptation, reducing cross-temporal appearance shift without modifying the query image. Code and dataset at https://github.com/ARTUROLab/HistReNeRF.

</details>

#### 2026-08-13 - GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors

**Authors:** Yanming Yang, Chenxi Song, Ping Wang, Xin Yuan, Chi Zhang
**Links:** [abs](https://arxiv.org/abs/2608.13502) - [pdf](https://arxiv.org/pdf/2608.13502)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS²CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors
- 作者：Yanming Yang, Chenxi Song, Ping Wang, Xin Yuan, Chi Zhang
- 出版日期：2026-08-13
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.13502

### 一句话总结
该论文提出一种新框架，利用3D高斯溅射与大规模视觉基础模型先验，从单次快照压缩成像测量中重建高质量3D场景，并通过专用稠密化策略提升重建鲁棒性与效率。

### 研究问题
如何从单一快照压缩成像（SCI）测量中高效、高质量地重建3D场景，克服信息损失、视点多样性有限以及3D表示与相机位姿联合优化的计算负担等挑战。

### 核心思路/方法
- 主重建阶段：将测量数据与3D视觉基础模型（VFM）初始化结合，进行SCI感知的高斯优化。
- 辅助细化阶段：在粗阶段收敛后，引入2D视觉基础模型在合成视点处提供伪视图监督，用于局部外观细化。
- 专用稠密化策略（OSGR）：包括基于局部不透明度统计扩展分裂候选、通过平均不透明度正则抑制损失补偿性的不透明度膨胀，以及用显式候选比例和高斯数量约束限制表示增长，以应对SCI监督模糊导致的不稳定性。

### 主要贡献
- 提出首个结合3DGS与大规模视觉基础模型先验的SCI单测量3D重建框架。
- 设计SCI专用的不透明度引导分裂与增长调节（OSGR）稠密化策略。
- 在多个基准上实现最佳综合性能，兼顾领先的重建质量、对视点变化的鲁棒性以及竞争力的计算效率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作将快照压缩成像与3D高斯溅射及视觉基础模型结合，属于多领域交叉创新，面向3D重建的前沿方向。其提出的稠密化策略针对SCI特有监督模糊问题，具有明确的方法贡献和广泛的实验验证（摘要提及多基准），适合关注3D表示学习、压缩感知或高效重建的研究者深入阅读。

</details>

<details>
<summary>Abstract</summary>

Snapshot Compressive Imaging (SCI) offers an efficient solution for high-speed video acquisition and, under exposure-time camera--scene relative motion, multi-view scene capture by compressing temporal or spatial information into a single 2D measurement. While recent studies have explored SCI for 3D scene reconstruction, existing methods struggle with significant challenges due to information loss, limited viewpoint diversity, and the computational burden of jointly optimizing 3D representations and camera poses. In this work, we propose a novel framework that reconstructs high-quality 3D scenes from a single SCI measurement by leveraging 3D Gaussian Splatting (3DGS) and the powerful priors of large-scale vision foundation models (VFMs). Our primary reconstruction combines measurement-derived 3D VFM initialization with SCI-aware Gaussian optimization. After coarse-stage convergence, an auxiliary 2D VFM provides pseudo-view supervision at synthesized viewpoints for local appearance refinement. To further address the instability caused by ambiguous SCI supervision during 3DGS optimization, we introduce Opacity-Guided Splitting and Growth Regulation (OSGR), an SCI-specific densification strategy that augments split candidates using local opacity statistics, discourages loss-compensating opacity inflation through mean-opacity regulation, and bounds representation growth with explicit candidate-ratio and Gaussian-count constraints. Extensive experiments across multiple benchmarks demonstrate that our method achieves the strongest overall performance, combining leading reconstruction quality and robustness to viewpoint variation with competitive computational efficiency.

</details>

#### 2026-08-13 - Semantic Radiance Fields as Simulators for Spatial Reasoning in Real-World Scenes

**Authors:** Nico Heider, Michał Jan Włodarczyk, Katarzyna Wasielewska-Michniewska, Przemysław Hołda, Martin Schieck, Marcin Paprzycki, Maria Ganzha, Bogdan Franczyk
**Links:** [abs](https://arxiv.org/abs/2608.13095) - [pdf](https://arxiv.org/pdf/2608.13095)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, novel view synthesis, view synthesis, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Semantic Radiance Fields as Simulators for Spatial Reasoning in Real-World Scenes
- 作者：Nico Heider, Michał Jan Włodarczyk, Katarzyna Wasielewska-Michniewska, Przemysław Hołda, Martin Schieck, Marcin Paprzycki, Maria Ganzha, Bogdan Franczyk
- 出版日期：2026-08-13T11:01:09Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.13095

### 一句话总结
本文提出将语义辐射场（SRF）作为真实场景中空间推理智能体的模拟器，通过联合编码几何、外观和逐类语义身份，实现真实感与语义标注的统一。

### 研究问题
如何为空间推理智能体的训练与评估提供既具备几何真实性又可语义查询的多样化环境？现有合成模拟器虽提供真值语义但缺乏真实感，而基于真实场景重建的模拟器虽外观真实却默认缺少语义真值。

### 核心思路/方法
使用语义辐射场（SRF）作为模拟器：将预训练视觉模型产生的2D语义分割提升到3D辐射场中，使辐射场联合编码几何、外观和逐类语义身份。该表示从真实场景的有姿态RGB图像重建，支持新视角合成、语义查询和自由空间查询，并可将这些能力提供给物理引擎使用。

### 主要贡献
- 提出将SRF用作空间推理智能体的模拟器，统一了真实感与语义真值。
- SRF从真实场景重建，同时支持新视角渲染、语义查询和自由空间查询，形成单一三维接地表示。
- 能够高效生成多样化的真实世界环境，用于训练和评估空间推理模型。
- 以果园苹果抓取任务为例，展示了SRF驱动模拟器的应用流程（相机渲染、语义真值、占用查询供物理引擎使用）。

### 局限性
摘要未提供足够信息。摘要中仅以果园苹果抓取任务作为示例应用，未讨论方法在场景规模、动态物体、语义类别覆盖、计算开销或泛化能力等方面的潜在限制。

### 阅读优先级
**中**。理由：该方法对空间推理或神经场景表示领域有一定新颖性，且提出的SRF模拟器思路清晰，具有应用潜力；但摘要未涉及实验验证和量化结果，属于概念性方案论述，若读者关注该交叉方向可进一步阅读，若仅需成熟方法则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Training and evaluating spatial reasoning in embodied agents requires diverse environments that are both geometrically faithful and semantically queryable. Synthetic simulators offer ground truth semantics but sacrifice realism; simulators based on reconstructions of real-world environments have realistic appearance but lack ground truth semantics by default. We propose using Semantic Radiance Fields (SRF) as simulators for spatial reasoning agents. SRFs are a representation that unifies these requirements by lifting 2D semantic segmentations from pretrained vision models into a 3D radiance field that jointly encodes geometry, appearance, and per-class semantic identity. The resulting fields are reconstructed from posed RGB captures of real scenes and support novel-view synthesis, semantic and free-space queries within a single grounded representation. This enables the efficient generation of diverse real-world environments to train and evaluate spatial reasoning models. As an example application, we outline an SRF-driven simulator for an orchard apple-reaching task, in which the radiance field supplies camera rendering, semantic ground truth, and occupancy queries to a physics engine.

</details>

#### 2026-08-13 - HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments

**Authors:** Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao, Tuyen P. Le, Truong Nguyen, Quan Nguyen
**Links:** [abs](https://arxiv.org/abs/2608.12860) - [pdf](https://arxiv.org/pdf/2608.12860)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments
- 作者：Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao, Tuyen P. Le, Truong Nguyen, Quan Nguyen
- 出版日期：2026-08-13T06:16:05Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.12860

### 一句话总结
本文提出了HumanoidVLN，一个基于物理的仿真器与基准，用于评估跨多种人形机器人的视觉-语言导航任务，并验证了其仿真到现实迁移的有效性。

### 研究问题
现有视觉-语言导航（VLN）基准未考虑人形机器人特有的物理约束（如双足运动限制）、多平台形态差异以及步态导致的视觉相机动态畸变，本文旨在填补这一空白，提出面向人形机器人形态多样性的VLN仿真环境与评测基准。

### 核心思路/方法
- 基于NVIDIA Isaac Sim构建物理仿真平台，支持可扩展的人形机器人配置，涵盖4种机器人（Unitree G1、H1、Internal-A、Internal-B），身高1.17m至1.80m，下肢自由度10–12。
- 采用分层控制栈：强化学习运动策略结合可替换的PD或MPC路径跟踪器。
- 环境来源包括艺术家设计场景与3D高斯泼溅重建，筛选可通行面积超过100平方米的区域。
- 指令生成采用“生成器-评审器-释义器”多智能体流水线并有人类在环验证，产出933条冲突感知参考片段，每条含1条细粒度指令和3种风格变体（正式、自然、随意）。
- 兼容性验证：支持NaVILA、DualVLN、StreamVLN、JanusVLN等VLN模型。
- 仿真到现实迁移：使用DualVLN和Unitree G1进行20片段试点实验。

### 主要贡献
- 提出了首个面向多种人形机器人形态的物理仿真VLN基准（HumanoidVLN）。
- 构建了可扩展的仿真平台，支持新机器人和新VLN模型的低成本集成。
- 发布了包含933条高质量参考片段的多粒度指令数据集。
- 在4个模型和4种机器人上进行了系统评估，其中JanusVLN获得最高平均成功率43.55%和nDTW 48.38。
- 通过20片段实机实验验证了仿真到现实的强相关性（r=0.935），平均绝对误差0.68m，平均轨迹相似度0.782 nDTW（±0.188）。

### 局限性
摘要未提供足够信息。摘要未明确讨论该方法在计算开销、仿真多样性覆盖范围、不同指令风格对性能的影响分析、以及内部机器人（Internal-A/B）的实机验证情况等方面的局限性。

### 阅读优先级
**高**。
理由：该工作针对人形机器人VLN这一前沿且实际约束突出的问题，提供了完整的仿真-数据-基准-实机验证闭环，实验结果（含sim-to-real强相关性）具有较强说服力，对从事VLN、机器人导航和人形机器人研究的读者有直接参考价值，且代码和数据承诺开放。

</details>

<details>
<summary>Abstract</summary>

Vision-Language Navigation (VLN) for humanoid robots poses challenges existing benchmarks fail to address: bipedal locomotion imposes physical constraints absent from wheeled agents, humanoid morphologies vary across platforms, and egocentric observations are distorted by locomotion-induced camera dynamics. We present HumanoidVLN, a physics-grounded simulator and benchmark for VLN across diverse humanoid embodiments. Built on NVIDIA Isaac Sim, our platform supports an extensible set of humanoid configurations, demonstrated on four robots (Unitree G1, Unitree H1, Internal-A, Internal-B) spanning 10-12 lower-body DoF and heights from 1.17m to 1.80m, via a hierarchical control stack combining a reinforcement learning locomotion policy with interchangeable PD or MPC path trackers. New robots and VLN models integrate with minimal effort; we demonstrate compatibility with NaVILA, DualVLN, StreamVLN, and JanusVLN. Environments are drawn from artist-designed scenes and 3D Gaussian Splatting reconstructions, filtered for navigable areas exceeding 100 square meters. Instructions are generated by a dual generator-reviewer plus paraphraser multi-agent pipeline with human-in-the-loop verification, yielding 933 collision-aware reference episodes, each paired with one fine-grained instruction and three coarse-grained stylistic variants (formal, natural, casual). Across four models and four embodiments, JanusVLN achieves the highest mean success rate of 43.55% and nDTW of 48.38. In a 20-episode sim-to-real pilot with DualVLN and the Unitree G1, navigation errors correlate strongly (r=0.935), with a mean absolute difference of 0.68m and mean trajectory similarity of 0.782 (+/-0.188) nDTW. These results highlight the interaction between VLN models, controllers, and humanoid embodiments under physical execution. Code, benchmark, and data will be released upon acceptance at https://humanoid-vln.github.io/.

</details>

#### 2026-08-13 - LocusGS: Spatially Grounded Tokens for Feed-Forward 3D Gaussian Splatting

**Authors:** Wenyu Li, Sidun Liu, Tongrui Hu, Peng Qiao, Yong Dou
**Links:** [abs](https://arxiv.org/abs/2608.12825) - [pdf](https://arxiv.org/pdf/2608.12825)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LocusGS: Spatially Grounded Tokens for Feed-Forward 3D Gaussian Splatting
- 作者：Wenyu Li, Sidun Liu, Tongrui Hu, Peng Qiao, Yong Dou
- 出版日期：2026-08-13
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.12825

### 一句话总结
LocusGS 通过为查询式前馈 3D 高斯泼溅中的每个高斯查询引入显式的 3D 锚点状态（中心+支撑半径），改善查询的空间连贯性，从而提升渲染质量。

### 研究问题
现有查询式前馈 3DGS 方法中，从同一查询解码出的高斯常常散布在场景中相距较远的区域，导致查询级别的空间连贯性弱、与场景结构对齐差。作者将这一问题归因于现有高斯查询所采用纯隐式表示，缺乏显式空间约束。

### 核心思路/方法
LocusGS 为每个高斯查询增加一个 3D 锚点状态，包含中心位置和支撑半径。锚点状态在解码器各层中逐步细化，并在查询交互、多视图特征聚合和高斯生成三个环节中统一使用。具体包括：
1. 锚点-射线几何偏置：引导查询只关注与其锚点空间相关的图像观测。
2. 锚点中心解码：将查询生成的 Gaussians 限制在锚点周围的局部区域内。

### 主要贡献
1. 提出 LocusGS 方法，通过显式 3D 锚点状态增强高斯查询的空间定位能力。
2. 在相同高斯预算下，较查询式高斯 token 基线方法在新型视图合成基准上取得更好的渲染质量。
3. 实验分析表明，学习到的锚点形成连贯的空间布局，高斯分布更加结构化，证明显式锚点状态改善了空间组织性。

### 局限性
摘要未提供足够信息，无法得知该方法在计算开销、对遮挡或复杂场景的鲁棒性、以及与大场景或动态场景的适配性等方面的局限性。

### 阅读优先级
**中**。该工作针对查询式前馈 3DGS 的空间连贯性问题提出了明确改进，方法设计清晰、实验验证充分，适合关注 3D 场景表示与神经渲染的研究者阅读。但摘要未展示与更多当前主流方法（如非查询式方法）的全面对比，也未涉及多尺度或大规模场景的扩展讨论，因此作为方向性参考价值较高，而非必须优先精读的突破性工作。

</details>

<details>
<summary>Abstract</summary>

Recent query-based feed-forward 3DGS methods represent a scene using learnable queries, each aggregating multi-view evidence and decoding a group of Gaussians. Ideally, different queries should specialize in coherent local regions of the scene. However, we observe that Gaussians decoded from the same query often scatter across distant scene regions, resulting in weak query-level spatial coherence and poor alignment with the scene structure. We attribute this behavior to the purely latent representation of existing Gaussian queries. To address this limitation, we introduce LocusGS, which augments each Gaussian query with a 3D anchor state consisting of a center and a support radius. The anchor state is progressively refined across decoder layers and is used throughout query interaction, multi-view feature aggregation, and Gaussian generation. Specifically, an anchor-to-ray geometric bias guides each query toward spatially relevant image observations, while anchor-centered decoding organizes its Gaussians within a local region. Experiments on novel view synthesis benchmarks show that LocusGS improves rendering quality over query-based Gaussian token baselines under the same Gaussian budget. Further analysis shows that the learned anchors form coherent spatial layouts and lead to more structured Gaussian distributions, demonstrating that explicit anchor states improve the spatial organization. Our project page: https://leo-frank.github.io/LocusGS_viewer.

</details>

#### 2026-08-12 - Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding

**Authors:** Zongjian Ding, Yudong Gao, Jiale Liu, Xinglin Yu, Junxing Ren, Dong Wei, Yajing Chen, Shan Huang, Mingjun Cheng, Min Li
**Links:** [abs](https://arxiv.org/abs/2608.11928) - [pdf](https://arxiv.org/pdf/2608.11928)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding
- 作者：Zongjian Ding, Yudong Gao, Jiale Liu, Xinglin Yu, Junxing Ren, Dong Wei, Yajing Chen, Shan Huang, Mingjun Cheng, Min Li
- 出版日期：2026-08-12
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.11928

### 一句话总结
Seed2GS提出一种无需原始重建相机、无需场景特定训练的目标物体提取方法，从3D高斯溅射场景中通过单参考视图标注实现对目标的高精度分割，在LERF-MASK上达到92.1% mIoU。

### 研究问题
如何从预构建的3D高斯溅射(3DGS)场景中高效且准确地提取目标物体，同时不依赖原始重建相机信息，也不需要针对每个场景进行耗时的表示训练。

### 核心思路/方法
核心思想是将“目标身份识别”与“3D覆盖范围”分离处理。具体方法包括：
- 利用QD-SAM3从多个开放词汇候选掩码中选出唯一可靠的参考掩码，一次性固定目标身份；
- 通过种子提升(Seed lift)和可见性自适应虚拟轨道(visibility-adaptive virtual orbits)从新视角暴露物体；
- 使用跟踪传播种子，避免重复检测；
- 场景保持冻结，掩码仅用于监督每个高斯分布的单一临时前景logit。

### 主要贡献
- 在不使用原始重建相机、不进行场景特定表示训练的条件下，达到当前最高的LERF-MASK分割精度（92.1% mIoU）；
- 测量计算延迟仅9.3秒，比最强的场景训练基线高3.7个百分点，比最接近的无相机基线高7.6个百分点；
- 在固定单个测试参考视图时，完整流程仍保持91.1% mIoU；
- 使用真实掩码替换预测种子仅提升0.72个百分点，说明种子预测已接近上限；
- 在3D-OVS数据集上达到95.7% mIoU。

### 局限性
摘要未提供足够信息。具体包括：未提及该方法对复杂场景、遮挡情况、多目标场景的鲁棒性，未说明不同数据集间的泛化表现差异原因，未讨论失败案例或常见错误模式，也未提供与其他方法在运行时间、内存占用等方面的详细对比数据。

### 阅读优先级
**高**。理由：该方法在无需原始相机且无需训练的条件下，显著提升了3DGS目标提取的精度（LERF-MASK 92.1% mIoU），同时计算延迟极低（9.3秒），具有实际应用价值；且其“分离身份与覆盖范围”的方法设计具有新颖性，对交互式3D编辑和场景理解领域有参考意义。

</details>

<details>
<summary>Abstract</summary>

Extracting a target object from a pre-built 3D Gaussian Splatting (3DGS) scene enables interactive 3D editing. Existing methods either train for tens of minutes per scene, sacrifice accuracy, or require original reconstruction cameras that pre-built assets may not include. We present Seed2GS, which achieves the highest reported LERF-MASK accuracy without original reconstruction cameras or scene-specific representation training. Its key insight is to separate target identity from 3D coverage. QD-SAM3 selects one reliable reference mask from several open-vocabulary candidates, fixing identity once. Seed lift and visibility-adaptive virtual orbits then expose the object from new viewpoints, while tracking propagates the seed without repeated detection. Because the scene remains frozen, these masks supervise only one temporary foreground logit per Gaussian. On LERF-MASK, Seed2GS reaches 92.1% mean intersection over union (mIoU) with a measured compute-only latency of 9.3 seconds, 3.7 points above the strongest scene-trained baseline and 7.6 points above the closest camera-free baseline. With one fixed test reference per scene, the complete pipeline retains 91.1% mIoU; replacing its predicted seed with a ground-truth mask improves mIoU by only 0.72 points. On 3D-OVS, Seed2GS reaches 95.7% mIoU.

</details>

#### 2026-08-11 - COGENT: Counterfactual Gaussian Explanations for Volumetric Medical Images

**Authors:** Dorian Rząsa, Bartosz Zabdyr, Krzysztof Piekarz, Jakub Grzywaczewski, Bartlomiej Sobieski, Przemyslaw Biecek, Żaneta Świderska-Chadaj, Olga Śliwicka, Przemysław Spurek, Joanna Świebocka-Więk
**Links:** [abs](https://arxiv.org/abs/2608.11422) - [pdf](https://arxiv.org/pdf/2608.11422)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation, differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：COGENT: Counterfactual Gaussian Explanations for Volumetric Medical Images
- 作者：Dorian Rząsa, Bartosz Zabdyr, Krzysztof Piekarz, Jakub Grzywaczewski, Bartlomiej Sobieski, Przemyslaw Biecek, Żaneta Świderska-Chadaj, Olga Śliwicka, Przemysław Spurek, Joanna Świebocka-Więk
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.11422

### 一句话总结
COGENT 提出一种在三维高斯体素表征参数空间中生成反事实解释的新框架，用于体素级医学影像（如肺部 CT）的可解释性分析。

### 研究问题
如何在三维体素医学影像（如肺 CT）中生成既保持解剖一致性、又具有空间局部性的反事实解释，以替代传统逐像素/逐体素归因方法。

### 核心思路/方法
- 基于 MedGS 和 Sybil 肺癌风险预测模型构建框架。
- 在基于高斯的体素表征参数空间中优化选定的高斯基元（Gaussian primitives），而非在体素空间操作。
- 通过可微渲染管线传递下游预测器的梯度，识别对模型决策影响最大的表征组件。
- 将可解释性问题形式化为显式三维场景表示上的反事实优化问题，生成稀疏、局部化且解剖一致的解释。

### 主要贡献
- 提出首个在高斯参数空间中生成反事实解释的框架（COGENT）。
- 将可解释性从体素空间扩展到显式三维场景表征，改变了传统归因范式。
- 在肺 CT 上结合定量比较和医学专家定性分析，验证了解释的临床意义和有效性。

### 局限性
摘要未提供足够信息——未提及方法的计算开销、对不同三维表示或任务类型的泛化性、反事实生成的时间成本或潜在失败模式等细节。

### 阅读优先级
**中**。理由：该工作结合了三维场景表征与医学影像可解释性，视角新颖，对从事体绘可解释性、三维医学影像诊断的读者有参考价值；但摘要中实验细节有限，且仅针对单一任务（肺癌风险预测）验证，若需深入评估需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Explainability is essential for deploying deep learning models in high-stakes medical applications. Existing explainability methods for volumetric imaging predominantly operate in voxel space, overlooking the structured representations introduced by recent advances in 3D scene modeling. We present COGENT (Counterfactual Gaussian Explanations), a framework that generates counterfactual explanations directly in the parameter space of Gaussian-based volumetric representations. Built upon MedGS and the Sybil lung cancer risk prediction model, COGENT optimizes selected Gaussian primitives through a differentiable rendering pipeline, enabling gradients from the downstream predictor to identify representation components that most influence model decisions. Unlike conventional pixel- or voxel-level attribution methods, our approach formulates explainability as a counterfactual optimization problem over an explicit 3D scene representation, producing sparse and spatially localized explanations while preserving anatomical consistency. We evaluate COGENT on lung CT scans using quantitative comparisons with existing explainability methods together with qualitative analysis by medical experts. The results demonstrate that representation-space counterfactual optimization provides clinically meaningful explanations while offering a new perspective on interpreting volumetric deep learning models.

</details>

#### 2026-08-11 - CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting

**Authors:** Jiayu Ding, Meilu Song, Yun Chen, Wei Gao, Ge Li
**Links:** [abs](https://arxiv.org/abs/2608.11150) - [pdf](https://arxiv.org/pdf/2608.11150)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting
- 作者：Jiayu Ding, Meilu Song, Yun Chen, Wei Gao, Ge Li
- 出版日期：2026-08-11T17:09:49Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.11150

### 一句话总结
本文提出CausalSplat框架，将视觉语言模型与3D场景图结合，以解决3D高斯泼溅在隐含意图、空间约束和常识推理等层次化推理任务上的不足。

### 研究问题
现有3D高斯泼溅（3DGS）开放词汇场景理解方法仅支持显式查询，难以处理实际具身交互中所需的隐含意图、复杂空间约束和常识推理（如因果、空间、功能与反事实推理）。本文定义并研究"推理式3D高斯分割"这一新任务。

### 核心思路/方法
- 构建两个基准：**Causal-LERF**和**Causal-ScanNet**，系统评估常识、空间、功能和反事实推理能力。
- 提出**CausalSplat**框架：将**视觉语言模型**与**3D场景图**集成，将显式结构感知与隐式逻辑推理解耦，以分层方式完成推理式分割。

### 主要贡献
1. 首次定义并引入"推理式3D高斯分割"任务。
2. 构建两个推理基准（Causal-LERF、Causal-ScanNet），覆盖四类推理能力。
3. 提出CausalSplat框架，结合视觉语言模型与3D场景图实现解耦推理。
4. 实验表明CausalSplat在推理基准上达到最优性能，并在标准指代与开放词汇3D分割任务上表现出强泛化性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作定义了3D场景理解领域的新任务（推理式分割），并同时提供基准与新型框架，对具身智能和开放词汇3D理解研究方向具有直接参考价值；且实验覆盖推理基准与标准任务，验证了方法的有效性与泛化性，属于方法+数据集双重贡献的综合性工作。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting (3DGS) has advanced open vocabulary scene understanding, existing methods remain confined to explicit queries. They struggle to interpret implicit intents, complex spatial constraints, and commonsense reasoning required for practical embodied interactions. To address this gap, we introduce the task of reasoning 3D Gaussian segmentation and construct two benchmarks, Causal-LERF and Causal-ScanNet. These benchmarks systematically evaluate commonsense, spatial, affordance, and counterfactual reasoning. Evaluations reveal that current state of the art methods perform poorly on these reasoning challenges. Therefore, we propose CausalSplat, a framework that integrates vision-language models with 3D scene graphs to disentangle explicit structural perception from implicit logical inference. Extensive experiments demonstrate that CausalSplat achieves state of the art performance on our reasoning benchmarks while showing strong generalizability on standard referring and open vocabulary 3D segmentation tasks. Project Page: https://jiayuding031020.github.io/CausalSplat

</details>

#### 2026-08-11 - WildFireGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes

**Authors:** Nienke Driessen, Joris Rijsdijk, Sören Pirk, Wojtek Palubicki, Dominik L. Michels, Michael Weinmann
**Links:** [abs](https://arxiv.org/abs/2608.11100) - [pdf](https://arxiv.org/pdf/2608.11100)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WildFireGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes
- 作者：Nienke Driessen, Joris Rijsdijk, Sören Pirk, Wojtek Palubicki, Dominik L. Michels, Michael Weinmann
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.11100

### 一句话总结
本文提出 WildFireGS，一种直接在语义增强的大规模 3D 高斯泼溅森林重建场景上运行的基于物理的野火模拟框架，无需显式网格或体素转换即可模拟点火、传热、燃烧和火焰传播。

### 研究问题
现有基于物理的野火模型虽然逼真度高，但主要局限于具有完整理想化森林结构知识的合成环境，难以直接应用于由航空影像重建的真实世界场景。本文旨在弥合学习式场景重建与环境模拟之间的鸿沟，实现基于观测数据的真实世界野火数字孪生。

### 核心思路/方法
- 在 3D 高斯泼溅森林重建中，为高斯原语附加语义和材料属性，以编码植被类型和燃料特征。
- 引入一种基于粒子的燃烧模型，原生运行在高斯表示上，无需转换为显式网格或体素网格，即可模拟点火、传热、燃烧及火焰在复杂森林结构中的传播。
- 通过基于能量汇过程的降雨驱动冷却机制展示框架的模块化，用于模拟火势遏制。

### 主要贡献
- 提出 WildFireGS，一种直接在大规模、语义增强的 3D 高斯泼溅森林重建上运行的基于物理的野火模拟框架。
- 通过粒子燃烧模型实现高斯表示上的原生火灾行为模拟，避免网格/体素转换。
- 在合成场景和真实航空森林采集数据上验证，显示物理一致的野火行为，包括随植被密度、风速和地形坡度变化的传播特性。
- 通过新型防火隔离带实验和生物质损失估计进行模型验证。

### 局限性
摘要未提供足够信息（未明确讨论方法的计算开销、对场景重建质量的依赖程度、实时性能或特定失效模式等局限性）。

### 阅读优先级
**高**  
理由：该工作将最新的 3D 高斯泼溅场景表示与物理模拟结合，直接面向真实世界野火数字孪生，跨越了神经渲染与物理仿真两个热点领域；且摘要展示了完整的模拟管线与多场景验证，方法新颖性强、应用潜力大，对从事场景表示、物理仿真或环境应用的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Climate-driven environmental change is driving an increase in both the frequency and severity of wildfire events, making accurate simulation and prediction critical for effective risk mitigation and landscape management. While recent physics-based wildfire models achieve high realism by explicitly simulating combustion, heat transfer, and fuel dynamics, they remain largely restricted to synthetic environments with complete and idealized knowledge of forest structure, limiting their applicability to real-world environments captured via aerial imagery. To provide a pathway toward real-world wildfire digital twins derived directly from observational data, we present WildFireGS, a physics-based wildfire simulation framework operating directly on large-scale, semantics-enriched 3D Gaussian Splatting forest reconstructions. Our approach bridges learning-based scene reconstruction and environmental simulation by augmenting Gaussian primitives with semantics and material properties that encode vegetation type and fuel characteristics. We introduce a particle-based combustion model that operates natively on Gaussian representations, simulating ignition, heat transfer, combustion, and flame propagation across complex forest structures. This enables direct physics-based simulation of fire behavior on reconstructed real-world environments, without requiring conversion to explicit meshes or volumetric grids. We demonstrate the modularity of WildFireGS through a rain-driven cooling mechanism in terms of an energy-sink process to realistically model fire containment. Evaluations on synthetic scenes and real aerial forest captures show physically consistent wildfire behavior, reproducing characteristic dynamics including propagation scaling with vegetation density, wind velocity, and terrain slope. In addition, we validate our model through novel firebreak experiments and biomass loss estimation.

</details>

## Embodied / Robotics / AR Applications

### 2026-08

#### 2026-08-17 - ViHaTeleop: A Low-Cost, Lightweight Visual-Haptic Teleoperation System for Dexterous Manipulation Learning

**Authors:** Fucai Zhu, Yanhou Lai, Paul Maestre, Koichi Hashimoto
**Links:** [abs](https://arxiv.org/abs/2608.16572) - [pdf](https://arxiv.org/pdf/2608.16572)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, manipulation, simulation

<details>
<summary>Abstract</summary>

Learning from demonstration is a promising approach for dexterous manipulation, but collecting high-quality contact-critical demonstrations remains difficult with low-cost teleoperation hardware. We present ViHaTeleop, a lightweight (0.7 kg), low-cost (\$550) visual-haptic teleoperation system with SLAM-based wrist tracking, camera-based hand tracking, and finger-wise vibrotactile feedback through Linear Resonant Actuators (LRA). The system includes several design choices (LED illumination, fisheye hand camera, and tactile-aware retargeting constraints) and is deployed on Franka + LEAP Hand + 9DTact in both real and simulated environments. Under matched with/without-haptic conditions with nine participants across six contact-critical tasks, haptics improved success rates across all tasks (+2.2 to +15.6 percentage points), while completion-time effects were task-dependent. Subjective ratings showed significant gains in contact clarity and grasp confidence in both simulation and real-world settings (Wilcoxon signed-rank, $p<0.05$). We also integrate a lightweight depth-camera-based tactile proxy in Isaac Sim, enabling a full pipeline from multi-modal demonstration collection to visual-tactile policy training. Preliminary downstream validation by training visual-tactile policies from collected demonstrations shows tactile cues benefit contact-critical subtasks (peg-in-hole: +17 percentage points over vision-only).

</details>

#### 2026-08-17 - GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation

**Authors:** Tianchen Deng, Xuefeng Chen, Shuang Wu, Qu Chen, Jiajun Zhu, Bo Dai, Jianfei Yang, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2608.16234) - [pdf](https://arxiv.org/pdf/2608.16234)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, scene understanding, world model

<details>
<summary>Abstract</summary>

Driving World Models (DWMs) have recently advanced rapidly with generative models, yet most existing methods mainly focus on conditional scene generation and lack explicit 3D scene understanding, language-grounded reasoning, and controllable 4D editing capabilities. Moreover, commonly used point cloud, occupancy, or BEV representations make it difficult to achieve fine-grained alignment between textual information and the underlying 3D scene structure. To address these limitations, we propose a foundation-feature Gaussian driving world model that unifies scene understanding, language-grounded reasoning, controllable 4D editing, and multi-modal generation within a single framework. Specifically, we introduce a foundation-feature Gaussian tokenizer that directly distills Qwen/SigLIP visual-language features into 3D Gaussian primitives, building a compact open-vocabulary Gaussian semantic field. We further design a geometry-aware Gaussian adapter that combines importance-aware hierarchical selection with text-conditioned Perceiver-style cross-attention to aggregate dense Gaussian primitives into compact world tokens. To improve representation compatibility, we introduce a KL-based Gaussian--image distribution alignment objective that aligns Gaussian world tokens with foundation image tokens. Based on the aligned Gaussian representation, our framework further supports instruction-controllable scene editing, including weather-conditioned generation and dynamic vehicle manipulation. Extensive experiments on broader driving benchmarks demonstrate that our method achieves state-of-the-art performance across scene understanding, visual grounding, planning-oriented reasoning, and controllable 4D generation tasks. We will release the code and datasets publicly on Github.

</details>

#### 2026-08-13 - DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation

**Authors:** DreamX Team, Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li, Qingfeng Shi, Datao Tang, Jing Tang, Jun Wang, Pengfei Zhang
**Links:** [abs](https://arxiv.org/abs/2608.13489) - [pdf](https://arxiv.org/pdf/2608.13489)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation
- 作者：DreamX Team, Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li, Qingfeng Shi, Datao Tang, Jing Tang, Jun Wang, Pengfei Zhang
- 出版日期：2026-08-13
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.13489

### 一句话总结
DreamX-Phi 1.0 是一个动作条件下的视频世界模型，通过几何编码、深度分支和物体一致性保持等技术，实现机器人操作中的高质量未来帧预测，并在 WorldArena 2.0 挑战赛中取得优异成绩。

### 研究问题
如何构建一个既具备视觉真实感、又能严格遵循动作指令且保持物体一致性的机器人操作视频世界模型，以准确预测给定动作序列下的未来观测。

### 核心思路/方法
- 以当前观测帧、语言指令和末端执行器位姿及夹爪状态序列为条件，预测未来观测视频。
- 采用 **PRoPE-style 几何编码**：将每只手臂的 SE(3) 变换注入注意力机制，保持手臂身份与刚体运动结构，确保预测遵循各臂指令路径。
- 引入轻量 **深度分支** 建模场景级几何信息。
- 利用 **SAM3 掩码** 与冻结的 **V-JEPA teacher** 维持抓取过程中小物体的语义一致性。
- 通过 **分布匹配蒸馏** 将多步生成器压缩为少步学生模型，提升部署效率。

### 主要贡献
- 提出动作条件视频世界模型 DreamX-Phi 1.0，兼顾视觉真实感与动作/物体级忠实性。
- 创新性引入 PRoPE-style 几何编码实现手臂级 SE(3) 约束。
- 结合深度分支与 SAM3+V-JEPA 教师机制，解决场景几何与物体演化建模难题。
- 通过分布匹配蒸馏实现高效生成推理。
- 在 WorldArena 2.0 挑战赛中获得 Track 1 第一名、Track 2 第二名。

### 局限性
摘要未提供足够信息：论文未在摘要中报告量化实验误差、模型参数量、训练数据规模、推理速度或具体蒸馏加速比等细节，也未说明当前方法在哪些场景下可能失效或存在何种限制。

### 阅读优先级
**高**

理由：该工作面向机器人操作中的视频世界建模这一前沿方向，方法整合了几何编码、深度估计、物体分割与蒸馏技术，设计较为系统，且已在公开挑战赛中验证效果，对从事具身智能、视频预测和机器人控制的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mathrm{SE}(3)$ transformations into attention via \textbf{PRoPE-style geometric encoding}, preserving arm identity and rigid-motion structure. Action control alone does not fully constrain scene geometry or the evolution of small manipulated objects. We therefore add a lightweight \textbf{depth branch} for scene-level geometry and use \textbf{SAM3 masks} with a frozen \textbf{V-JEPA teacher} to maintain object consistency throughout grasping. We further distill the multi-step generator into a few-step student via distribution-matching distillation for efficient deployment. At the time of writing, \model{} achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge. Our model and code will be publicly available.

</details>

#### 2026-08-12 - Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations

**Authors:** AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini, AmirMohsen Eshghi, Siavash Arjomand Bigdel
**Links:** [abs](https://arxiv.org/abs/2608.12299) - [pdf](https://arxiv.org/pdf/2608.12299)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations
- 作者：AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini, AmirMohsen Eshghi, Siavash Arjomand Bigdel
- 出版日期：2026-08-12T17:45:03Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.12299

### 一句话总结
本文对2016年以来57篇以方法为中心的类激活映射（CAM）相关论文进行系统综述，提出了按归因机制、架构依赖和评估目标划分的分类法，总结了该领域从单一CNN层向多层、概率化、令牌感知及基础模型感知解释的演进趋势。

### 研究问题
类激活映射（CAM）作为可解释人工智能中广泛使用的视觉解释方法家族，其研究现状和发展趋势如何？具体包括：不同CAM方法如何归类和区分、各方法的主要贡献与遗留问题是什么，以及当前评估协议是否统一。

### 核心思路/方法
作者严格筛选了2016年以来57篇以方法为中心的论文，构建了一个分类法，从三个维度对CAM方法进行划分：（1）归因机制（gradient-based vs. gradient-free vs. hybrid）；（2）架构依赖（CNN、Transformer、基础模型等）；（3）评估目标（忠实性、定位、鲁棒性、计算成本、人类信任等）。在此基础上，分三类综述了梯度式CAM、近期与混合CAM风格方法，以及基于模型或架构感知的方法，并检视了每种方法留下的未解决缺口及后续方法的补足尝试。

### 主要贡献
1. 提供了一个严格的、以方法为中心的57篇论文综述语料库。
2. 构建了新的CAM分类法，按归因机制、架构依赖和评估目标实现多维划分。
3. 系统梳理了CAM从经典CNN场景到Transformer、基础模型时代的演进路径。
4. 明确指出评估协议碎片化问题，并分析了各方法在忠实性、定位、鲁棒性、成本和人类信任等维度上的贡献与缺口。

### 局限性
摘要未提供足够信息：未提及关于语料库选择的具体排除/纳入标准、各方法的定量对比结果、以及评估协议碎片化的具体表现或标准化建议。摘要也未报告综述过程中的偏倚控制方法或对未来研究方向的详细建议。

### 阅读优先级
**中**。理由：该文是一篇综述论文，对所涉领域（可解释视觉、CAM方法）有系统梳理价值，适合该方向研究者了解宏观脉络和分类框架。但由于其分类为“Embodied / Robotics / AR Applications”，与纯计算机视觉方向略有距离，且摘要未提供具体的实证对比结论，对于追求具体方法细节或实验复现的读者优先级略低。若读者正从事视觉可解释性研究或需要CAM方向的全景认知，则值得一读。

</details>

<details>
<summary>Abstract</summary>

Class activation mapping (CAM) is one of the most widely used visual explanation families in explainable artificial intelligence. Its purpose is intuitive: it converts internal model evidence into a heatmap that highlights the image regions, convolutional channels, tokens, or patches that support a target class or concept. Since the first CAM formulation in 2016, the field has moved far beyond global-average-pooled CNN classifiers. CAM-style methods now include gradient-based post-hoc explanations, gradient-free score and ablation methods, high-resolution upscaling, weakly supervised localization and segmentation, transformer token attribution, causal and debiasing methods, and foundation-model-era approaches that use CLIP, DINO, SAM, or feature-distribution comparisons. This review synthesizes a strict corpus of 57 method-centered papers published from 2016 onward. The paper develops a taxonomy that separates methods by attribution mechanism, architectural dependence, and evaluation objective. It then reviews gradient-based CAMs, recent and hybrid CAM-style methods, and model-based or architecture-aware methods. Across the corpus, the main trend is clear: the field is shifting from explaining one class score in one low-resolution CNN layer toward comparative, multi-layer, probabilistic, token-aware, and foundation-model-aware explanations. At the same time, evaluation remains fragmented. Faithfulness, localization, robustness, computational cost, and human trust are often measured with different protocols. The review therefore emphasizes not only what each method contributes, but also which gap it leaves open and which later methods attempt to close that gap.

</details>

#### 2026-08-12 - STAR: A Spatial-Topology Aware Routing Framework for Generalizable 3D Scene Understanding

**Authors:** Mingwei Xing, Xinliang Wang, Yifeng Shi
**Links:** [abs](https://arxiv.org/abs/2608.11699) - [pdf](https://arxiv.org/pdf/2608.11699)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：STAR: A Spatial-Topology Aware Routing Framework for Generalizable 3D Scene Understanding
- 作者：Mingwei Xing, Xinliang Wang, Yifeng Shi
- 出版日期：2026-08-12
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.11699

### 一句话总结
STAR 提出一种空间拓扑感知的路由框架，通过引入多属性自监督预训练和域感知专家路由机制，解决跨传感器模态3D场景理解中专家分配困难的问题。

### 研究问题
如何克服不同传感器模态之间的拓扑差异，构建统一的3D场景理解模型？具体而言，在语义一致性与几何异质性共存时，传统的基于特征仅使用MoE路由器难以有效分配专家，导致性能受限。

### 核心思路/方法
- 提出STAR（Spatial-Topology Aware Routing Framework）框架，包含两个主要分支：
  1. **多属性自监督预训练分支**：覆盖拓扑和纹理变化，用于锚定跨域结构先验。
  2. **域感知专家分支**，包含两个机制：
     - **Domain-Spatial-Guided Routing (DSR)**：从空间上下文捕获局部拓扑变化。
     - **Entropy-controlled Dynamic Allocation (EDA)**：根据路由不确定性调整激活专家数量。
- 两个分支结合，实现稳定的跨域表示学习与自适应专家分配。

### 主要贡献
- 提出STAR框架，将空间拓扑信息纳入MoE路由决策，改善跨域3D场景理解。
- 设计多属性自监督预训练分支，增强跨域结构先验的学习。
- 引入DSR和EDA两种机制，分别解决局部拓扑建模和动态专家分配问题。
- 实验结果表明STAR在ScanNet验证集达到80.1% mIoU，在S3DIS达到77.2% mIoU，优于强基线模型。

### 局限性
摘要未提供足够信息。摘要未明确提及方法的失败案例、计算开销、对特定传感器类型的敏感性或扩展性限制。

### 阅读优先级
**中**  
理由：该工作针对3D场景理解中的跨模态泛化问题提出系统性框架，并给出明确性能提升数据，对从事3D理解或多模态融合研究的读者有参考价值。但摘要未提供详细的实验对比和消融信息，方法的普适性和局限性难以全面评估，故优先级为中。

</details>

<details>
<summary>Abstract</summary>

Constructing a unified 3D scene understanding model has long been hindered by the topological discrepancies across sensor modalities. While applying the Mixture-of-Experts (MoE) architecture is a flexible approach for multi-domain 3D understanding, we observe that conventional feature-only MoE routers may underrepresent local sampling topology under semantic supervision, making expert allocation difficult when semantic consistency coexists with geometric heterogeneity. To overcome this challenge, we propose STAR (Spatial-Topology Aware Routing Framework). Specifically, we introduce a multi-attribute self-supervised pre-training branch, covering topological and textural variations, to anchor cross-domain structural priors. Building upon this, we design a domain-aware expert branch with two mechanisms: Domain-Spatial-Guided Routing (DSR), which captures local topological variations from spatial context, and Entropy-controlled Dynamic Allocation (EDA), which adjusts the number of activated experts according to routing uncertainty. Together, these branches combine stable cross-domain representation learning with adaptive expert allocation. Extensive experiments across various tasks, encompassing both indoor and outdoor scenes, demonstrate the effectiveness of STAR. It achieves 80.1% mIoU on the ScanNet validation set and 77.2% mIoU on S3DIS, consistently improving over strong baselines. Code is available at our project page (https://xmw666.github.io/STAR/).

</details>

#### 2026-08-12 - RoadWeaver: Large-Scale Lane-Level HD Map Generation from Scratch for Autonomous Driving Simulation

**Authors:** Yueyuan Li, Zexi Chen, Weijie Xi, Mingyang Jiang, Songan Zhang, Hanyang Zhuang, Ming Yang
**Links:** [abs](https://arxiv.org/abs/2608.11580) - [pdf](https://arxiv.org/pdf/2608.11580)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoadWeaver: Large-Scale Lane-Level HD Map Generation from Scratch for Autonomous Driving Simulation
- 作者：Yueyuan Li, Zexi Chen, Weijie Xi, Mingyang Jiang, Songan Zhang, Hanyang Zhuang, Ming Yang
- 出版日期：2026-08-12
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.11580

### 一句话总结
RoadWeaver 提出了一种从零生成大规模车道级高清地图的粗到细框架，可在数秒内生成拓扑一致、可直接用于自动驾驶仿真的完整地图。

### 研究问题
如何从零（无需真实地图或人工设计）生成大规模、多样化且拓扑一致的车道级高清地图，以支撑自动驾驶仿真中的长距离闭环评估。

### 核心思路/方法
采用粗到细的三阶段框架：
1. 合成全局道路布局；
2. 将布局扩展为连通的道路网络；
3. 构建车道级几何，并保证车道连接关系的拓扑一致性。

### 主要贡献
- 提出 RoadWeaver，首个从零生成大规模完整车道级 HD 地图的框架；
- 相比现有 SOTA 生成方法，端点对齐误差降低 94.4%；
- 生成时间仅需 1.39–3.50 秒，满足仿真场景的快速构建需求；
- 生成的地图可直接部署至驾驶模拟器，支撑闭环评估；
- 将开源训练代码与开箱即用实现。

### 局限性
摘要未提供足够信息，未明确讨论方法在极端复杂路网（如环岛、多层立交）、地图语义丰富度、泛化到不同城市风格或真实路网一致性方面的潜在局限；也未报告与真实地图数据分布差异的定量分析。

### 阅读优先级
**高**。理由：该工作针对自动驾驶仿真中高清地图生成的关键瓶颈，提出完整且可扩展的解决方案，量化指标突出（99.8%可达性、低死端率、亚米级对齐误差），且代码即将开源，对仿真平台构建和闭环评测研究具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous driving simulation requires diverse and scalable lane-level HD maps to support long-horizon evaluation across complex road networks. Existing approaches either rely on handcrafted or reconstructed real-world maps, which limits scalability, or generate only local road structures rather than complete HD maps. We present RoadWeaver, a coarse-to-fine framework for from-scratch generation of diverse, large-scale HD maps. RoadWeaver first synthesizes a global road layout, expands it into a connected road network, and then constructs lane-level geometry with topologically consistent lane connectivity. Experimental results show that RoadWeaver achieves a 99.8\% reachability, a 10.7\% dead-end ratio, and an endpoint alignment error of 0.24 m. Compared with SOTA generation methods, it reduces endpoint alignment error by 94.4\% while generating complete HD maps in 1.39--3.50 s. The generated maps can be directly deployed in driving simulators, providing scalable simulation environments for future closed-loop evaluation of autonomous driving systems. The training code and an out-of-the-box implementation of RoadWeaver will be released upon acceptance.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
