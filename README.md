# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：51
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 16
  - Neural Scene Representations & Rendering: 15
  - Embodied / Robotics / AR Applications: 14
  - Geometry Foundation Models: 5
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**1. 几何基础模型（Geometry Foundation Models）从“重建”走向“感知骨干”**
本周多篇论文不再将几何基础模型仅仅视为离线重建工具，而是将其作为在线、流式感知系统的共享骨干。GeoUP 将 VGGT 的重建导向潜表示适配到多相机驾驶场景，作为统一 3D 感知的几何底座；Map-Det3D 则直接将前馈式度量 3D 重建模型作为检测模型的几何骨干，将 3D 检测框直接在重建出的度量空间中预测，绕开“2D 检测 + 3D 提升”的脆弱范式。这表明该领域正从“重建即目标”转向“重建即基础设施”。

**2. 前馈式 3D 高斯溅射（3DGS）持续追求“空间结构化”与“低开销”**
查询式前馈 3DGS 方法（如 LocusGS）开始暴露纯隐式查询表示的局限——同一查询解码的高斯散布于远距区域，空间连贯性弱。LocusGS 通过显式 3D 锚点（中心 + 支撑半径）将查询“接地”到场景局部区域，改善空间组织性。与此同时，Seed2GS 则追求无需相机位姿、无需场景特定训练的物体提取（9.3秒、92.1% mIoU），体现了前馈式方法在“效率”与“可用性”（不需要原始重建相机）上的双重发力。

**3. 重建先验与视觉基础模型（VFM）成为弱/受限观测下重建的“救命稻草”**
当观测信息严重不足（单次快照压缩成像）或模态退化（热成像、水下成像）时，研究者转而依赖大规模预训练模型先验来补偿信息缺失。GS²CI 利用 3D VFM 初始化与 2D VFM 伪视图监督，从单张 SCI 测量重建 3D 场景；RGB-HS 通过层级 token 对齐将 RGB 基础模型知识迁移到热成像深度估计；AMR-Pose 虽未使用 VFM，但也通过主动 LED 标记弥补水下光学退化。这一趋势表明，基础模型先验正成为解决“病态逆问题”的通用补丁。

**4. 世界模型与仿真环境迈向“物理可行 + 语义可查询”**
机器人相关论文显示，仿真与预测正从“视觉逼真”转向“物理忠实 + 语义可用”。DreamX-Phi 1.0 通过 PRoPE 几何编码确保预测视频遵循手臂级 SE(3) 指令路径，并通过深度分支与 SAM3 掩码保持物体一致性；HumanoidVLN 强调双足运动的物理约束、形态多样性和步态导致的相机动态畸变；Semantic Radiance Fields 则将 2D 语义分割提升至 3D 辐射场，使真实场景重建同时具备几何真实性、新视角合成与语义/自由空间查询能力，服务于空间推理智能体的训练与评估。

**5. 自动驾驶与机器人的“大规模/统一基准”缺口被逐步填补，且新数据集生成呈自动化趋势**
MV2 数据集弥补了多视角、多车辆轨迹下新视角合成评估的空缺；HumanoidVLN 提供物理接地的人形 VLN 基准；ProPose 提出统一拓扑的义肢/残肢姿态估计基准。同时，RoadWeaver 展示了从零生成大规模车道级 HD 地图的自动化管线（1.39–3.50 秒生成完整地图），进一步压缩了仿真场景构建的时间成本。这类工作指向一个共同诉求：以更低的成本获得覆盖更广、更真实的评测资源。


#### 技术路线观察

- **几何基础模型**：GeoUP 与 Map-Det3D 均将重建模型（VGGT、前馈度量重建模型）用作多视图感知的几何骨干，但 GeoUP 采用因子化注意力（自/时间/视图）分解跨图像交互，Map-Det3D 则直接将检测框映射进重建空间。两者的共同逻辑是“用重建先验替代语义预训练骨干的几何短板”，差异在于架构耦合的深度。
- **3D/4D 重建与神经场景表示**：可明显看到两条分叉路线——一是优化式/表示增强路线（LocusGS 的显式锚点、GS²CI 的 OSGR 稠密化策略），强调在既有表征（3DGS、辐射场）中注入更强的空间结构或 SCI 专用约束；二是免训练/免相机路线（Seed2GS），强调对预构建 3DGS 资产的即取即用。此外，COGENT 提出了全新应用维度——将高斯表示用于可解释性（反事实解释），扩展了神经场景表示的下游消费场景。
- **机器人/AR 应用**：世界模型（DreamX-Phi 1.0）与仿真器（HumanoidVLN、SRF 模拟器）均强调“物理约束 + 语义接口”的耦合：前者通过几何编码与物体一致性保持实现动作忠实，后者通过物理引擎与语义查询实现闭环训练。与此同时，4D 雷达-相机深度补全（RbFT-Net）与水下位姿估计（AMR-Pose）则反映出对极端/异质传感模态的鲁棒感知重建正在成为独立关注点。
- **自监督预训练**：受控条件下的 SSL 对比研究（论文 2608.13183）提供了一个重要但容易被忽视的视角——在有限资源下，DINOv2 风格预训练综合最优，且图像 SSL 与视频 SSL 的联合训练存在语义/几何任务间的权衡。这提示 3D 感知社区在采用大规模预训练骨干时，需要警惕任务类型的匹配性。


#### 值得优先阅读的论文

1. **GeoUP（2608.13147）**：将几何基础模型引入统一 3D 驾驶感知，是当前“重建先验 + 感知”融合趋势的代表作，对自动驾驶与多视图 3D 感知研究者有直接参考价值。
2. **Map-Det3D（2608.12179）**：与 GeoUP 思路互补，将度量重建先验直接用于 3D 检测，绕开 2D-to-3D 提升的脆弱性。对 monocular 3D detection 域偏移问题有兴趣者必读。
3. **LocusGS（2608.12825）**：直击查询式前馈 3DGS 的“空间散乱”要害，显式锚点思想简洁且可推广，对该子方向的后续发展有启示意义。
4. **GS²CI（2608.13502）**：将快照压缩成像与 3DGS 及视觉基础模型结合，属多领域交叉创新，其 SCI 专用稠密化策略（OSGR）对极端观测条件下的重建有方法论借鉴价值。
5. **A Controlled Study of Self-Supervised Image and Video Pretraining under Limited Resources（2608.13183）**：稀缺的受控对比研究，对依赖预训练骨干的 3D/多模态感知研究者有很强的资源配置与方法选型的指导意义。


#### 可能的研究机会

- **“重建先验 + 感知”的更深层融合**：GeoUP 与 Map-Det3D 均将重建模型作为骨干，但与任务头（检测、占用）的耦合仍较浅。未来可在重建潜空间内直接联合优化检测、跟踪、预测，探索真正“以重建为中心”的自动驾驶感知架构。
- **SCI/压缩感知条件下的 3D 重建通用化**：GS²CI 聚焦单测量 SCI，但该方法是否可推广到其他压缩成像设置（如光谱、全息）？其 OSGR 稠密化策略能否迁移至其他弱监督重建任务（如稀疏视角 3DGS）值得探索。
- **基础模型先验的“分层监督”范式泛化**：RGB-HS 的层级 token 对齐策略能否扩展到其他跨模态（雷达、事件相机、超声）的深度/几何估计？其基于 RGB 图像质量的教师加权机制也是一种可复用的教务设计。
- **语义辐射场作为通用机器人模拟器**：目前仅以果园苹果抓取为例，可扩展到室内服务机器人、手术机器人、搜索救援等场景；如何高效更新

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-14T09:39:26-04:00
**Total number of papers:** 42
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

#### 2026-08-11 - Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically Consistent 3D Vision Foundation Models

**Authors:** Seokhyun Youn, Dahyeon Kye, Sung-Ho Bae, Jihyong Oh
**Links:** [abs](https://arxiv.org/abs/2608.10708) - [pdf](https://arxiv.org/pdf/2608.10708)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, pointmap, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically Consistent 3D Vision Foundation Models
- 作者：Seokhyun Youn, Dahyeon Kye, Sung-Ho Bae, Jihyong Oh
- 出版日期：2026-08-11
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2608.10708

### 一句话总结
本文提出一种无需真值、即插即用的测试时自适应方法Self-Geometry，通过显式多视图几何约束直接提升三维视觉基础模型的位姿与几何估计一致性。

### 研究问题
现有三维视觉基础模型（VFMs）在单次前向传播中预测深度、相机位姿和点图，虽泛化能力强，但因训练时未施加显式多视图几何一致性约束（如光束平差法计算成本过高），导致推理时存在几何不一致。如何在不依赖真值的前提下，通过测试时自适应提升模型的几何一致性？

### 核心思路/方法
- 核心思想：与先前工作利用模型输出的隐式自一致性（如点图、特征）不同，本文直接用2D像素对应关系作为伪真值，显式引入多视图几何约束。
- **几何解耦优化（Geometric Disentanglement Optimization）**：联合多视图一致性损失与对极一致性损失，并引入梯度解耦以阻止梯度冲突。
- **帧角邻居（Frame Angular-Neighbor）**：基于SO(3)测地距离的视图采样器，以轻量方式施加上述约束。
- **轻量测试时自适应（Lightweight TTA）**：通过LoRA适配基础模型。

### 主要贡献
- 提出首个直接施加显式多视图几何约束的测试时自适应方法，而非依赖隐式一致性信号。
- 设计几何解耦优化策略，避免多视图与对极一致性损失之间的梯度冲突。
- 提出基于SO(3)测地距离的视图采样方法，实现轻量约束施加。
- 在6种VFMs（VGGT、π³、DA3-Giant/Large/Base/Small）和4个基准（7Scenes、ETH3D、ScanNet++、HiRoom）上，位姿和几何估计均取得一致提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作聚焦于3D视觉基础模型的关键痛点——几何不一致性，提出无需真值、即插即用的测试时自适应方案，且验证模型和基准覆盖面广（6种VFMs、4个基准），对三维视觉与基础模型研究均有较强参考价值。方法设计层面（梯度解耦、SO(3)视图采样）也有一定创新性。

</details>

<details>
<summary>Abstract</summary>

Recent Vision Foundation Models (VFMs) predict depth, camera pose, and pointmap in a single forward pass without per-scene optimization, achieving strong generalization. However, enforcing explicit multi-view geometric consistency, e.g., through bundle adjustment, is computationally costly and is thus not imposed during VFM pretraining, so such inconsistency can arise. To address this, implicit self-consistency derived from model outputs (e.g., pointmaps, features), though enforced at test-time in prior work, delivers inherently limited performance gain, especially on scenes where the pretrained VFM is highly inaccurate. In contrast to this implicit signal, we propose Self-Geometry, a plug-and-play test-time adaptation pipeline that directly imposes explicit multi-view geometric constraints using 2D pixel correspondences as pseudo ground-truth. Our proposed Self-Geometry consists of Geometric Disentanglement Optimization, which combines Multi-View Consistency and Epipolar Consistency losses with Gradient Disentanglement to prevent gradient conflict; Frame Angular-Neighbor, a view sampler based on SO(3) geodesic distances for lightly imposing these constraints; and Lightweight TTA, which adapts VFMs via LoRA. Our method achieves consistent improvements in both pose and geometry estimation across six VFMs (VGGT, $π^3$, DA3-Giant/Large/Base/Small) and four benchmarks (7Scenes, ETH3D, ScanNet++, HiRoom).

</details>

#### 2026-08-11 - Visual Geometry Foundation-Aware Gaussians for Single-Frame Surround-View Driving Reconstruction

**Authors:** Junhong Lin, Jinlong Wang, Xianda Guo, Yanlun Peng, Wei Zheng, Guoqing Liu, Hanli Wang, Tiesong Zhao, Wei Gao
**Links:** [abs](https://arxiv.org/abs/2608.10682) - [pdf](https://arxiv.org/pdf/2608.10682)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visual Geometry Foundation-Aware Gaussians for Single-Frame Surround-View Driving Reconstruction
- 作者：Junhong Lin, Jinlong Wang, Xianda Guo, Yanlun Peng, Wei Zheng, Guoqing Liu, Hanli Wang, Tiesong Zhao, Wei Gao
- 出版日期：2026-08-11T09:04:33Z
- 分类：Geometry Foundation Models（主分类）；Neural Scene Representations & Rendering（次分类）
- 链接：https://arxiv.org/abs/2608.10682

### 一句话总结
本文提出VGGD框架，利用预训练视觉几何基础模型的先验知识，增强单帧环视驾驶场景重建中的几何稳定性和渲染质量。

### 研究问题
单帧环视重建因相机间重叠区域极小，面临严重的几何不稳定和渲染伪影问题；现有方法依赖复杂解码器或辅助线索，但受限于上游特征几何能力不足。

### 核心思路/方法
- 核心主张：利用预训练视觉几何先验增强上游表征，缓解稀疏环视视角下的几何歧义。
- 具体流程：
  1. 使用VGGT生成可迁移的多视角几何先验token；
  2. 引入双路径颈部结构，解耦几何一致表征与外观相关表征，改善弱观测区域的外观补全；
  3. 应用尺度预热策略，稳定早期几何学习并抑制自我姿态变化下的尺度漂移；
  4. 使用混合像素-体素高斯解码器，生成可渲染的3D高斯场景用于新视角合成。

### 主要贡献
- 提出VGGD框架，将几何建模前移至前端，并适配基础模型先验到驾驶相机设置；
- 引入双路径颈部以解耦几何与外观表征；
- 提出尺度预热策略提升训练稳定性；
- 在nuScenes单帧基准上取得最佳整体渲染质量，并改善了相对几何一致性。

### 局限性
摘要未提供足够信息，未提及明确的局限性、失败案例或性能边界分析。

### 阅读优先级
**高**。理由：该工作面向单帧环视驾驶重建这一实际应用场景，结合了视觉几何基础模型与3D高斯泼溅这一当前热门技术路线，并在公开基准（nuScenes）上报告了领先效果；对从事自动驾驶场景重建、新视角合成或多视角几何建模的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-frame surround-view reconstruction faces severe geometric instability and rendering artifacts due to minimal inter-camera overlap. While existing methods rely on complex decoders or auxiliary cues, they remain bottlenecked by the weak geometric capacity of upstream features. We argue that leveraging pretrained visual geometry priors strengthens upstream representations and alleviates the geometric ambiguity in sparse surround views. To this end, we propose VGGD, a visual geometry foundation-aware 3D Gaussian Splatting framework for feed-forward surround-view driving reconstruction, which shifts geometric modeling to the frontend and adapts foundation priors to the driving camera setting. First, VGGD leverages VGGT to provide transferable multi-view geometric prior tokens. Next, we introduce a Dual-Path Neck to decouple geometry-consistent and appearance-aware representations, improving appearance completion in weakly observed regions. We further apply Scale Warmup to stabilize early geometry learning and suppress scale drift under ego-pose changes. Finally, we use a hybrid pixel--volume Gaussian decoder to produce a renderable 3D Gaussian scene for novel-view synthesis. Experiments on the nuScenes single-frame benchmark show that VGGD achieves the best overall rendering quality among the compared methods and improves relative geometric consistency.

</details>

## Dynamic / 4D Reconstruction

### 2026-08

#### 2026-08-10 - Marrying Optimal Transport and ODEs for Unified Continuous-Time 4D Reconstruction and Tracking

**Authors:** Liying Yang, Hao Mo, Jialun Liu, Chen Liu, Xinxing Yu, Chenhao Guan, Hui Ma, Xiao Cao, Ajian Liu, Yanyan Liang
**Links:** [abs](https://arxiv.org/abs/2608.09613) - [pdf](https://arxiv.org/pdf/2608.09613)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Marrying Optimal Transport and ODEs for Unified Continuous-Time 4D Reconstruction and Tracking
- 作者：Liying Yang, Hao Mo, Jialun Liu, Chen Liu, Xinxing Yu, Chenhao Guan, Hui Ma, Xiao Cao, Ajian Liu, Yanyan Liang
- 出版日期：2026-08-10
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2608.09613

### 一句话总结
本文提出Uni4R框架，通过最优传输与常微分方程的协同，学习连续速度场，统一实现任意时间戳下的4D重建与点跟踪。

### 研究问题
现有统一4D重建与点跟踪方法依赖启发式插值或仅在整数时间戳预测，缺乏运动学一致性，无法建模任意时间戳的动态。本文旨在解决这一问题，实现统一的连续时间4D重建与点跟踪。

### 核心思路/方法
- 提出Uni4R框架，学习连续速度场作为运动学先验，同时服务于4D重建与点跟踪。
- 提出Flow Matching Guided Decoder（FMGD）：全局速度分支提取锚点特征，捕捉序列全局动态状态；利用Flow Matching理论，在锚点特征流形上构建由最优传输定义的概率路径，实例化为FM引导的速度特征，用于速度预测，形成稳健的运动学归纳偏置。
- 点重建分支提供几何特征；局部速度预测模块结合上述特征与时间嵌入，解码任意时间戳的速度。
- 提出积分一致性训练策略：针对分数帧缺乏高质量真实速度的问题，使用ODE求解器对速度积分以恢复目标点图，使模型可直接从整数时间戳进行端到端监督。

### 主要贡献
- 提出Uni4R，首次将最优传输与ODE结合，实现连续时间下的统一4D重建与点跟踪。
- 设计FMGD模块，利用Flow Matching理论建立运动学归纳偏置，提升动态建模能力。
- 提出积分一致性训练策略，解决分数帧速度监督缺失问题。
- 实验表明Uni4R在4D重建与点跟踪上达到SOTA，并在新提出的连续时间运动学感知基准上取得SOTA。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：本文针对统一4D重建与点跟踪这一前沿任务，提出新颖的最优传输+ODE融合方案，并解决了连续时间建模与训练监督的关键难题，实验达到SOTA。对于从事动态场景重建、点跟踪及相关方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing unified 4D reconstruction and point tracking approaches typically rely on heuristic interpolations or just predict at integer timestamps, lacking kinematic coherence and failing to model dynamics at any arbitrary timestamp. In this paper, we propose Uni4R, a framework that unifies these tasks by learning continuous velocity fields through the synergy of Optimal Transport (OT) and Ordinary Differential Equation (ODE). Importantly, this continuous velocity field acts as a kinematic prior that mutually benefits both 4D reconstruction and point tracking. Specifically, we propose the Flow Matching Guided Decoder (FMGD). A global velocity branch first extracts anchor features that capture the global dynamic state of the sequence. Then, FMGD leverages Flow Matching (FM) theory to formulate a probability path defined by OT on the anchor feature manifold, instantiating it as FM-guided velocity features for velocity prediction. This establishes a robust kinematic inductive bias. Meanwhile, a point reconstruction branch provides geometric features. The local velocity prediction module then joint above features and time embeddings, to decode velocities at arbitrary timestamps. To overcome the absence of high-quality ground-truth velocities in fractional frames, we propose an integral-consistency training strategy. This strategy uses an ODE solver to integrate velocities to recover target pointmaps, enabling the model to be supervised end-to-end directly from integer timestamps. Experimental results demonstrate that Uni4R achieves SOTA performance in both 4D reconstruction and point tracking, and achieves SOTA in our new kinematics-aware benchmark at continuous time.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-08

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

#### 2026-08-11 - Gaussian Sculpting: End-to-End Controllable Surface Reconstruction via Field Optimization

**Authors:** Ke Jiaxin, Juncheng Liu, Yi Wang, Zhouhui Lian, Bin Liu, Shengfa Wang, Xiangjia He
**Links:** [abs](https://arxiv.org/abs/2608.10602) - [pdf](https://arxiv.org/pdf/2608.10602)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Sculpting: End-to-End Controllable Surface Reconstruction via Field Optimization
- 作者：Ke Jiaxin, Juncheng Liu, Yi Wang, Zhouhui Lian, Bin Liu, Shengfa Wang, Xiangjia He
- 出版日期：2026-08-11T07:42:24Z
- 分类：3D Reconstruction & Multi-view Geometry（次要：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.10602

### 一句话总结
本文提出 Gaussian Sculpting，一种将3D高斯原语锚定在可微表面上、通过双层训练策略联合优化有符号距离场（SDF）与高斯参数，以实现端到端可控高质量表面重建的框架。

### 研究问题
3D高斯溅射（3DGS）在有限视角下难以恢复准确表面，且高斯原语的不规则性导致几何误差难以手动修正。如何实现高质量、可控且端到端的表面重建是该文要解决的核心问题。

### 核心思路/方法
- 将高斯原语锚定在一个演化的可微表面上，使它们引导SDF优化，而非仅在后期处理中提取表面。
- 设计双层训练策略：外层循环优化SDF表示的几何，内层循环固定几何并更新高斯参数，以实现稳定梯度隔离。
- 对高斯参数施加约束，确保其与底层表面的一致性，提升几何与外观保真度。
- 引入基于八叉树类划分的多分辨率细分方案，保留细节同时降低内存消耗。

### 主要贡献
- 提出完全可微的端到端框架Gaussian Sculpting，用于高质量表面重建。
- 设计双层训练策略实现几何与高斯的联合优化与梯度隔离。
- 通过对高斯参数的约束增强几何-外观一致性。
- 提出多分辨率细分方案，兼顾细节保留与内存效率。
- 在物体级场景实验中有效去除冗余表面、恢复有限视角下缺失结构，并在较低分辨率下仍实现良好重建质量。

### 局限性
摘要未提供足够信息。摘要未提及方法的失败案例、对大规模场景的适应性、训练/推理时间成本、与已有方法的定量对比细节，以及多分辨率方案在极端复杂几何下的表现等潜在局限。

### 阅读优先级
**高**。理由：该方法针对3DGS在表面重建中的核心痛点（有限视角、几何误差、手动修正困难）提出了端到端可微框架和双层优化策略，思路明确且有物体级实验支撑，对从事三维重建、神经渲染和几何优化方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has recently enabled real-time novel view synthesis with impressive quality. However, it struggles to recover accurate surfaces under limited viewpoints and due to the inherent irregularity of Gaussian primitives. The resulting geometric errors are notoriously difficult to correct manually. To address these issues, we propose Gaussian Sculpting, a fully differentiable end-to-end framework for high-quality surface reconstruction. Our key insight is to anchor Gaussians onto an evolving differentiable surface, allowing them to guide signed distance field (SDF) optimization instead of extracting the surface only during post-processing. To enable stable gradient isolation during joint optimization, we design a bi-level training strategy in which the outer loop optimizes the geometry represented by the SDF, while the inner loop updates the Gaussians with the geometry fixed. We further impose constraints on Gaussian parameters to ensure consistency with the underlying surface, thereby improving both geometric and appearance fidelity during optimization. In addition, we introduce a multi-resolution subdivision scheme based on octree-like partitioning to preserve fine details while reducing memory consumption. Experiments on object-level scenes demonstrate that our method effectively removes redundant surfaces, recovers missing structures caused by limited viewpoints, and achieves strong reconstruction quality even at relatively low resolutions.

</details>

#### 2026-08-10 - A Semantic Communication Approach to Fiducial Marker Processing in 5G-Enabled Edge SLAM

**Authors:** Boris Radovanovic, Vukan Ninkovic, Katarina Vidojevic, Buda Bajic Papuga, Dejan Vukobratovic
**Links:** [abs](https://arxiv.org/abs/2608.09620) - [pdf](https://arxiv.org/pdf/2608.09620)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Semantic Communication Approach to Fiducial Marker Processing in 5G-Enabled Edge SLAM
- 作者：Boris Radovanovic, Vukan Ninkovic, Katarina Vidojevic, Buda Bajic Papuga, Dejan Vukobratovic
- 出版日期：2026-08-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.09620

### 一句话总结
本文提出一种基于语义通信的标定标记（fiducial marker）处理框架，将深度网络在机器人与边缘服务器之间进行分割推理，并集成到5G使能的边缘SLAM系统中，以实现通信感知的任务卸载。

### 研究问题
如何在5G边缘SLAM场景下，通过语义通信实现标定标记检测任务的通信高效分割与部署，克服传统检测流水线难以进行有效任务划分的问题。

### 核心思路/方法
受DeepTag启发的卷积神经网络被分割部署在机器人端和边缘服务器端，中间层特征表示作为面向任务的语义信息通过无线链路传输。整个框架集成于ROS2机器人架构中，并在真实5G通信测试平台上进行性能评估。

### 主要贡献
- 提出面向标定标记处理的语义分割推理框架，支持任务导向的语义信息无线传输。
- 将框架集成到ROS2架构中，并在真实5G测试平台上完成验证。
- 通过实验展示关键点估计精度及其对下游位姿估计的影响。
- 量化不同分割点下的通信–计算权衡，为通信感知的深度视觉感知部署提供实践指导。

### 局限性
摘要未提供足够信息：摘要未明确提及具体局限性，例如对不同网络条件、多机器人协作场景或系统鲁棒性的讨论。

### 阅读优先级
**中**。理由：该工作面向机器人边缘计算与5G语义通信的交叉方向，具有较好的应用价值，但更偏向系统集成与权衡分析，而非提出全新的算法突破。若读者关注通信感知推理或边缘SLAM实践，可优先阅读；若仅关注视觉基础方法，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Autonomous robots increasingly rely on edge computing to offload computationally intensive perception tasks while maintaining real-time operation over 5G networks. However, conventional fiducial marker detection pipelines provide limited opportunities for efficient task partitioning, making them poorly suited for communication-aware edge deployment. This paper proposes a semantic split inference framework for fiducial marker processing in 5G-enabled Edge SLAM. A DeepTag-inspired convolutional neural network is partitioned between the robot and the edge server, where intermediate feature representations serve as task-oriented semantic information transmitted over the wireless link. The framework is integrated into a ROS2-based robotic architecture and characterized over a real 5G communication testbed. Experimental results demonstrate accurate keypoint estimation, illustrate the impact on downstream pose estimation, and quantify the communication--computation trade-offs associated with different split points, providing practical insights for communication-aware deployment of deep visual perception in connected robotic systems.

</details>

#### 2026-08-10 - You Only Flow Once: Calibrated and Real-Time Radar Pose Estimation with Multi-Hypothesis Normalizing Flows

**Authors:** Jonas Leo Mueller, Sebastian Hoefler, Dario Zanca, Naga Venkata Sai Jitin Jami, Thomas Altstidl, Bjoern M. Eskofier
**Links:** [abs](https://arxiv.org/abs/2608.09579) - [pdf](https://arxiv.org/pdf/2608.09579)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：You Only Flow Once: Calibrated and Real-Time Radar Pose Estimation with Multi-Hypothesis Normalizing Flows
- 作者：Jonas Leo Mueller, Sebastian Hoefler, Dario Zanca, Naga Venkata Sai Jitin Jami, Thomas Altstidl, Bjoern M. Eskofier
- 出版日期：2026-08-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.09579

### 一句话总结
本文提出基于条件归一化流的多假设雷达姿态估计方法MH-NFPG，在保持校准不确定性的同时实现实时推理，性能超越扩散模型。

### 研究问题
稀疏且含噪的毫米波雷达点云通常对应多种合理的人体姿态，导致确定性姿态估计存在本质上的不适定性；现有雷达方法多为确定性估计，无法处理多模态歧义，而扩散模型虽能建模多假设分布但推理成本高且缺乏校准的不确定性。

### 核心思路/方法
将条件归一化流与时空Transformer骨干结合：Transformer提取雷达点云时空特征，条件归一化流将Laplace基分布变换为表达力强的后验分布，通过单次前向传播并行生成多个姿态假设，从而以低推理成本获得多模态分布并支持校准的不确定性估计。

### 主要贡献
- 提出MH-NFPG：首个面向雷达姿态估计的多假设归一化流方法，兼具多模态建模与单次前向推理效率。
- 在三个雷达基准（MM-Fi、mmRadPose、mRI）上超越扩散模型的校准性能，并在两个数据集上提升姿态精度，第三个数据集精度持平。
- 推理速度比扩散模型快20倍以上，校准误差最高降低85%。
- 发现扩散模型在校准上显著退化，而基于流的方法在跨环境设置下仍保持可靠覆盖率。

### 局限性
摘要未提供足够信息。例如：未提及方法在极端噪声、遮挡或训练数据规模有限时的表现，也未讨论模型参数量、显存开销或失败案例。

### 阅读优先级
**优先级：中**。理由：该方法在雷达姿态估计任务上展示了归一化流对扩散模型的计算效率与校准优势，对关注实时不确定性感知姿态估计的研究者有参考价值；但若你不是该子领域（毫米波雷达人体姿态估计）从业者，或更关注通用生成模型方法论，则与本工作的直接相关性有限。

</details>

<details>
<summary>Abstract</summary>

Sparse and noisy millimeter-wave radar point cloud observations often correspond to multiple plausible human poses, making deterministic pose estimation fundamentally ill-posed. Yet existing radar methods remain deterministic, collapsing this ambiguity into a single estimate. Diffusion-based alternatives can model multi-hypothesis distributions but require costly sequential denoising for each distribution sample and lack calibrated uncertainty. We propose Multi-Hypothesis Normalizing Flow Pose Generator (MH-NFPG), which models pose distributions from radar point clouds using a conditional normalizing flow. Specifically, we combine a spatiotemporal transformer backbone with a normalizing flow that transforms a Laplace base distribution into an expressive posterior, generated in parallel through a single forward pass. Leveraging this efficiency, we outperform diffusion-based alternatives in calibration across three radar benchmarks (MM-Fi, mmRadPose, mRI), improve pose accuracy on two, and match it on the third, while achieving over 20x faster inference for applications and reducing calibration error by up to 85%. We find that calibration degrades substantially for diffusion models, whereas our flow-based approach maintains reliable coverage, also in cross-environment settings. These results demonstrate normalizing flows as a practical alternative to diffusion models for real-time, uncertainty-aware radar pose estimation. Our code will be made publicly available.

</details>

## Neural Scene Representations & Rendering

### 2026-08

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

#### 2026-08-11 - Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting

**Authors:** Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji
**Links:** [abs](https://arxiv.org/abs/2608.10756) - [pdf](https://arxiv.org/pdf/2608.10756)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting
- 作者：Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji
- 出版日期：2026-08-11T10:16:30Z
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.10756

### 一句话总结
本文提出一种基于语义3D高斯泼溅的具身多模态对齐框架，通过显式可刷新的3D语义接地提升开放词汇移动操作在杂乱、遮挡与视角变化下的鲁棒性。

### 研究问题
如何让具身移动操作机器人将语言指令、视觉观察、三维场景结构与动作可行性在执行前有效对齐，从而在本地家庭工作空间中实现开放词汇目标接地与少样本操作。

### 核心思路/方法
- 构建任务驱动的局部语义3D高斯泼溅（Semantic-3DGS）作为共享接口，统一主动多视角感知、语言条件3D定位、障碍感知场景推理、基座准备与动作模型语义条件化。
- 引入可达性感知的基座定位，确保操作姿态可行。
- 采用扩散式视觉-语言-动作（VLA）策略，并将3D语义线索仅注入动作专家网络的后期模块，以保留预训练动作先验。

### 主要贡献
- 提出一个将Semantic-3DGS作为多阶段共享表示的具身多模态接地框架，覆盖从主动感知到动作生成的完整链路。
- 通过仅在动作模型后期注入语义，避免破坏预训练动作先验。
- 在50次真实机器人试验中，长时程任务成功率60%，优于PointVLA（40%）与DexVLA（28%）；高杂乱操作成功率74%，优于单视角变体（52%）与PointVLA（46%）。
- 在75厘米高度偏移下保持75%成功率，并消除了照片引起的错误抓取。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法涉及具身智能、语义3D场景表示与VLA策略的交叉，且提供了真实机器人上的多维度对比实验（成功率、杂乱场景、高度偏移、误抓消除），对从事机器人操作与神经场景表示研究的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Embodied mobile manipulation requires language, visual observations, three-dimensional scene structure, and action feasibility to be aligned before execution. We study open-vocabulary target grounding with few-shot manipulation in local household workspaces and present an embodied multimodal grounding framework that integrates active multi-view Semantic 3D Gaussian Splatting (Semantic-3DGS), reachability-aware base positioning, and a diffusion-based vision-language-action policy. A task-driven local Semantic-3DGS serves as a shared interface across active sensing, language-conditioned 3D localization, obstacle-aware scene reasoning, base preparation, and semantic conditioning of the action model. To preserve pretrained action priors, the 3D semantic cues are injected only into the late action-expert blocks. In expanded 50-trial real-robot evaluations against representative vision-language-action (VLA) approaches, the full system achieves 60% long-horizon success compared with 40% for PointVLA and 28% for DexVLA, and reaches 74% success in heavily cluttered manipulation compared with 52% for the single-view variant and 46% for PointVLA. It also maintains 75% success under a 75 cm height shift and eliminates photo-induced false grasps. These results indicate that explicit, refreshable 3D semantic grounding can improve robustness under clutter, occlusion, viewpoint variation, and embodiment constraints.

</details>

#### 2026-08-11 - Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging

**Authors:** Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss
**Links:** [abs](https://arxiv.org/abs/2608.10712) - [pdf](https://arxiv.org/pdf/2608.10712)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging
- 作者：Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10712

### 一句话总结
本文提出一种基于显著性引导的原始高斯合并流水线，将逐像素的高斯原语压缩为紧凑的内容自适应表示，在保留视觉质量的同时将高斯数量减少至约1/20。

### 研究问题
如何将前馈式3D高斯泼溅方法生成的冗余逐像素原语，转化为更紧凑且高效的表示，同时保持渲染质量。

### 核心思路/方法
- 采用结构感知的合并流水线，通过自适应超像素分割对空间连续、外观相似的高斯进行聚类，聚类粒度由显著性图引导——纹理区域细分，均匀区域粗分。
- 每个聚类通过学习的编码器压缩为紧凑的潜在表示。
- 在不同视图之间基于几何重叠和特征相似性，通过学习的合并器匹配并整合表示。
- 使用细节层次（level-of-detail）解码器以可控分辨率生成最终高斯，支持推理时的质量-效率灵活权衡。
- 作为后处理模块，该方法与骨干网络无关，可兼容任意前馈方法。

### 主要贡献
- 提出一种骨干无关的显著性引导高斯合并流水线，可将前馈方法输出的逐像素高斯压缩至约1/20数量。
- 通过自适应超像素分割和显著性引导，实现内容自适应的紧凑表示。
- 通过可学习的编码器、合并器和细节层次解码器，支持可控分辨率的灵活质量-效率权衡。
- 与已有减少原语数量的方法相比，在更紧凑表示下实现了更好且更稳健的视觉质量。

### 局限性
摘要未提供足够信息。摘要未涉及方法在特定场景下的失败案例、计算开销、内存占用、对不同输入视图数量的鲁棒性边界、以及与其他方法的定量对比实验细节。

### 阅读优先级
**中**。理由：该工作针对3D高斯泼溅表示冗余的问题提出了一种通用后处理压缩方案，对关注神经场景表示和渲染效率的研究者具有参考价值。但摘要未给出关键定量结果和实验对比细节，且方法链路较复杂（编码器、合并器、解码器均需学习），在未看到实验验证前其实际效果和适用性需要进一步评估。

</details>

<details>
<summary>Abstract</summary>

3D scene reconstruction, modeling, and rendering are highly relevant for numerous tasks, and 3D Gaussian splatting has become a standard choice in this context. Its feed-forward variants provide fast reconstruction from sparse input views but often produce per-pixel primitives, leading to highly redundant and thus inefficient representations. We present a structure-aware merging pipeline that takes per-pixel primitives from any feed-forward method and consolidates them into a compact, content-adaptive Gaussian set while largely retaining visual quality at just $\frac{1}{20}^\text{th}$ of the Gaussians of a per-pixel method. We group spatially coherent Gaussians of similar appearance into variable-size clusters via adaptive superpixel segmentation guided by a saliency map, which allocates fine segments to textured regions and coarse segments to homogeneous areas. We compress each cluster into a compact latent representation through a learned encoder, then match and consolidate representations across views based on geometric overlap and feature similarity via a learned merger. A level-of-detail decoder then produces the final Gaussians at a controllable resolution, enabling a flexible quality-efficiency trade-off at inference. As a post-processing module, the pipeline is backbone-agnostic, leveraging the strengths of existing feed-forward methods. This leads to better and more robust quality than achieved by previous approaches that target a reduction in primitive count, while providing a highly compact representation, that can be rendered efficiently.

</details>

#### 2026-08-11 - Amulet: Frame Extrapolation Through Sparse Layered Scene Representation and Adaptive Shading

**Authors:** Sebastian Künzel, Fabian Schmierer, Sergej Geringer, Guido Reina, Daniel Weiskopf, Dieter Schmalstieg
**Links:** [abs](https://arxiv.org/abs/2608.10423) - [pdf](https://arxiv.org/pdf/2608.10423)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Amulet: Frame Extrapolation Through Sparse Layered Scene Representation and Adaptive Shading
- 作者：Sebastian Künzel, Fabian Schmierer, Sergej Geringer, Guido Reina, Daniel Weiskopf, Dieter Schmalstieg
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10423

### 一句话总结
Amulet 提出了一种基于稀疏分层图像空间缓存的自适应着色方法，通过将低频着色率外推至高刷新率显示，实现无神经网络的精确多帧外推渲染。

### 研究问题
如何在不依赖神经网络或重投影的前提下，以显式且非幻觉的方式实现高频帧外推，尤其是在处理新出现遮挡区域和动态场景时保持高质量渲染。

### 核心思路/方法
- 将场景转换为稀疏、分块、分层的中间表示（缓存），并显式光栅化潜在可见几何体。
- 缓存以预测方式提前填充未来视图的着色信息，并在多帧之间摊销成本。
- 新视图合成通过从前到后层级遍历缓存完成，对过期或缺失的着色进行实时细化。
- 使用基于梯度的预测调度器为每个分块分配生命周期，实现运动与动态光照下的自适应着色更新。
- 将光栅化与着色频率从显示刷新率中解耦，从而允许单个着色帧支撑多个外推帧。

### 主要贡献
- 提出一种稀疏分层图像空间缓存，支持预测式填充分层场景表示，用于高频帧外推。
- 设计了自适应的梯度驱动调度器，以控制分块生命周期和着色更新。
- 实现了显式处理新遮挡区域的非神经多帧外推，避免幻觉。
- 在4K分辨率下可达250 Hz，在多项指标上与DLSS和神经流方法等现有帧生成技术竞争。

### 局限性
摘要未提供足够信息。摘要未提及方法在极端动态场景、复杂光照或性能退化条件下的具体局限，也未给出与对比方法的详细定量失败案例或资源开销分析。

### 阅读优先级
**高**。理由：该工作针对帧生成与外推这一热点方向提出了非神经的显式表示方案，具备高刷新率（250 Hz @4K）和与DLSS等工业级方法竞争的能力，方法和贡献描述清晰，适合渲染与帧生成领域研究者阅读。

</details>

<details>
<summary>Abstract</summary>

We introduce Amulet, a rendering method that transforms a scene into a sparse, tiled and layered intermediate scene representation (cache) for high-frequency frame extrapolation. In contrast to reprojection-based techniques, Amulet explicitly rasterizes and stores potentially visible geometry in its layered image-space cache, allowing accurate shading and inpainting of newly disoccluded regions without hallucination. Our key contribution is a cache that is predictively filled with shading information for future views, amortized over multiple current frames. Novel views are synthesized by hierarchically traversing the cache front to back and refining stale or missing shading on the fly. Using a predictive, gradient-based scheduler that assigns lifetimes for each tile, we enable adaptive shading updates under motion and dynamic lighting. Amulet decouples the rasterization and shading rate from the refresh rate of the display. In many scenarios, our cache can use a single shaded frame to synthesize multiple extrapolated frames with only a few localized updates. In a typical application, we extrapolate a 60 Hz shading rate to a 240 Hz display. Amulet achieves up to 250 Hz at 4K resolution and is competitive with state-of-the-art frame generation methods, including DLSS and neural-flow approaches, in multiple metrics. Amulet explores the design space of sparse layered image-space representation. It enables accurate, non-neural multi frame extrapolation with explicit handling of disocclusions. Our findings show that Amulet can extrapolate many more frames than contemporary methods with high quality, rivaling latency-bound frame interpolation methods with similar quality in many scenes.

</details>

#### 2026-08-11 - CasDeblurGS: Cascaded 2D-to-3D Multi-View Consistency for 3D Gaussian Splatting from Two Blurry Images

**Authors:** Haeyun Choi, Minhyuk Jang, I-Gil Kim
**Links:** [abs](https://arxiv.org/abs/2608.10345) - [pdf](https://arxiv.org/pdf/2608.10345)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, neural rendering, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CasDeblurGS: Cascaded 2D-to-3D Multi-View Consistency for 3D Gaussian Splatting from Two Blurry Images
- 作者：Haeyun Choi, Minhyuk Jang, I-Gil Kim
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10345

### 一句话总结
本文提出一种级联框架，仅从两张已知内参的运动模糊图像中重建连贯的3D场景，通过先建立局部2D对应再聚合为全局3D引导，实现无需位姿和额外辅助的3D高斯泼溅重建与高质量新视角合成。

### 研究问题
在仅有**两张运动模糊图像**、已知相机内参、但**无输入视角位姿、无辅助清晰图像、无逐场景测试时优化**的严格条件下，如何重建连贯的3D场景并进行新视角合成。现有模糊感知神经渲染方法通常依赖多视角冗余、精确相机位姿或昂贵的逐场景优化，难以应对该实际设置。

### 核心思路/方法
提出级联框架 CasDeblurGS，分两阶段由局部到全局逐步恢复可靠的跨视角信息：
- **Stage 1**：通过**遮挡感知的对应关系过滤**构建局部可靠的引导信息。
- **Stage 2**：聚合中间恢复结果，构建**无需位姿的临时3D高斯表示**；该表示的输入视角重渲染结果提供密集的全局引导，用于最终的恢复。
- 最终得到的视角支持更连贯的3D表示与更高质量的新视角合成。

### 主要贡献
- 提出一种新的级联框架，针对仅两张模糊图像、无位姿的极端稀疏视角场景进行3D高斯泼溅重建。
- 设计遮挡感知的对应过滤与临时3D高斯引导机制，实现从局部2D对应到全局3D引导的渐进式信息恢复。
- 在真实世界和合成 Deblur-NeRF 场景上均取得一致性提升，PSNR 分别提高 1.19 dB 和 2.11 dB。
- 通过渐进式消融、跨视角对应可视化和相机重投影分析，验证了渲染质量与多视角几何一致性的改进。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对“仅两张模糊图像、无位姿”这一极具挑战性和实际意义的设置，提出了级联的解决方案，在稀疏视角与模糊退化两个难点上均有创新，且实验结果显著（PSNR提升超过2dB）。对于从事3D重建、神经渲染和图像去模糊交叉方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Free-viewpoint 3D scene media is increasingly important for immersive applications, yet practical capture often suffers from severe view sparsity and motion blur. Although neural rendering has advanced sparse-view synthesis, existing blur-aware methods typically require substantial multi-view redundancy, accurate camera poses, or costly per-scene optimization. We address a stringent yet practical setting: reconstructing a coherent 3D scene from only two motion-blurred images with known intrinsics, without input-view poses, auxiliary sharp images, or per-scene test-time optimization. To this end, we propose CasDeblurGS, a cascaded framework that progressively recovers reliable cross-view information from local 2D correspondences to global 3D guidance. Stage 1 constructs locally reliable guidance through occlusion-aware correspondence filtering, while Stage 2 aggregates the intermediate restorations into a provisional pose-free 3D Gaussian representation whose input-view re-renders provide dense global guidance for final restoration. The resulting views enable a more coherent 3D representation and higher-quality novel-view synthesis. Experiments on real-world and synthetic Deblur-NeRF scenes show consistent gains over strong baselines, improving PSNR by 1.19 dB and 2.11 dB, respectively. Progressive ablations, cross-view correspondence visualization, and camera reprojection analysis further demonstrate improvements in both rendering quality and multi-view geometric consistency.

</details>

#### 2026-08-10 - TRACE-GS: On-Policy Trajectory Distillation with Privileged Geometric Conditioning for Sparse-View 3DGS Restoration

**Authors:** Linlian Jiang, Yuchen Xi, Sadman Rakib Pinon, Ruigang Yang, Yang Wang, Xinxin Zuo
**Links:** [abs](https://arxiv.org/abs/2608.10286) - [pdf](https://arxiv.org/pdf/2608.10286)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRACE-GS: On-Policy Trajectory Distillation with Privileged Geometric Conditioning for Sparse-View 3DGS Restoration
- 作者：Linlian Jiang, Yuchen Xi, Sadman Rakib Pinon, Ruigang Yang, Yang Wang, Xinxin Zuo
- 出版日期：2026-08-10T22:43:06Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10286

### 一句话总结
TRACE-GS 提出一种利用训练时特权几何信息进行在线轨迹蒸馏的框架，用于稀疏视角 3D 高斯泼溅（3DGS）重建，使扩散先验适应稀疏视角场景并显著提升重建质量与泛化能力。

### 研究问题
现有基于扩散模型的稀疏视角 3DGS 重建方法存在根本性局限：在独立噪声状态下进行的监督无法覆盖推理时实际到达的状态。由于稀疏视角下几何约束不足，去噪过程从一开始就产生偏差，且这些偏差沿轨迹逐步累积，导致重建效果不佳。本文旨在解决这一训练-推理分布不匹配问题。

### 核心思路/方法
TRACE-GS 采用在线策略轨迹蒸馏（on-policy trajectory distillation）策略：
- 在训练阶段，一个以额外训练视角提供的更丰富几何信息为条件的教师模型，为稀疏视角学生模型自身采样轨迹上的每个状态提供监督目标。
- 该方法在每个访问状态上对齐去噪方向与跨视角响应，使训练分布贴合推理分布。
- 该训练时使用的额外几何信息属于学习使用特权信息（LUPI）范式；部署时仅保留稀疏视角学生模型，其修复后的渲染结果作为伪观测用于 3DGS 精化。

### 主要贡献
1. 首次将在线策略监督与特权几何信息相结合，用于稀疏视角 3DGS 重建任务。
2. 提出一种新的训练范式，在训练时利用丰富几何条件引导扩散先验适应稀疏输入，而非设计更复杂的重建网络结构。
3. 在多个数据集和多种稀疏视角设置下取得一致性能提升，并展现出良好的泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对稀疏视角 3DGS 重建这一活跃研究方向的根本性训练-推理分布不匹配问题，提出了概念新颖的在线轨迹蒸馏与特权信息学习框架，且报告了跨数据集和多种稀疏设置的一致提升，对相关领域研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

We present TRACE-GS, an on-policy trajectory distillation framework that leverages privileged geometric conditioning at training time, thereby adapting a diffusion prior to sparse-view 3D Gaussian Splatting (3DGS) restoration. Rather than pursuing increasingly sophisticated restoration architectures, we identify a more fundamental limitation shared by existing diffusion-based approaches: supervision at independently noised states does not cover those reached during inference. In sparse-view 3DGS, under-constrained geometry biases denoising from the outset, and the resulting deviations compound along the rollout. TRACE-GS instead performs on-policy trajectory distillation: a teacher conditioned on richer geometry from additional training views supplies targets along the sparse-view student's own rollout, aligning denoising directions and cross-view responses at each visited state. This training-only geometry places TRACE-GS in the learning using privileged information (LUPI) setting. At deployment, only the sparse-view student is retained, and its restored renderings serve as pseudo-observations for 3DGS refinement. To the best of our knowledge, TRACE-GS is the first to derive on-policy supervision from privileged geometry for sparse-view 3DGS restoration, achieving consistent gains and strong generalization across datasets and sparse-view settings.

</details>

#### 2026-08-10 - LEGO: Leveled Language Gaussian Splatting

**Authors:** Yuning Peng, Haiping Wang, Yuan Liu, Yipeng Lu, Zhen Dong, Bisheng Yang
**Links:** [abs](https://arxiv.org/abs/2608.10057) - [pdf](https://arxiv.org/pdf/2608.10057)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LEGO: Leveled Language Gaussian Splatting
- 作者：Yuning Peng, Haiping Wang, Yuan Liu, Yipeng Lu, Zhen Dong, Bisheng Yang
- 出版日期：2026-08-10
- 分类：Neural Scene Representations & Rendering（神经场景表征与渲染）
- 链接：https://arxiv.org/abs/2608.10057

### 一句话总结
LEGO 通过将多视图 SAM 产生的易变粒度自动重分级为统一的 3D 一致层级，并结合 CLIP 与空间关系构建层级化语言场景图，实现了先进的开放词汇 3D 场景理解与空间推理。

### 研究问题
如何超越基础概念识别，在 3D 场景中捕捉并建模内在的语义层级结构（如“花盆→花束→花蕾→花瓣”），并支持开放词汇的跨视图一致的层级化分割与空间推理。

### 核心思路/方法
- 利用基础模型（如 SAM）可在 2D 中识别多粒度结构，但其划分严格受视角限制、缺乏跨视图一致性。
- LEGO 提出自适应性重新分级机制，将多视图下不稳定的 SAM 粒度统一为 3D 一致的层级结构，为 3D 场景的多层级分割提供精确监督。
- 将各层级分割结果与 CLIP 嵌入对齐，恢复开放词汇的跨层级语义逻辑。
- 通过引入空间关系，将分割结果提升为层级化的语言场景图，使大语言模型能够进行复杂的上下文感知空间推理和精确视觉定位。

### 主要贡献
- 提出 LEGO 框架，实现先进的开放词汇 3D 场景理解，核心创新在于捕获场景内在语义层级。
- 自动将多视图 SAM 粒度重分级为 3D 一致的统一层级，解决跨视图一致性问题。
- 结合 CLIP 与空间关系，构建层级语言场景图，支持大语言模型驱动的空间推理与视觉定位。
- 实验表明，在 promptable 和开放词汇 3D 分割基准上均达到新的最先进性能。

### 局限性
摘要未提供足够信息，例如：方法在复杂/遮挡场景下的鲁棒性、不同规模场景的扩展性、运行时开销、对 SAM/CLIP 基础模型依赖的具体限制等均未提及。

### 阅读优先级
**高**。理由：该论文发表于 2026 年，针对开放词汇 3D 场景理解这一热门方向提出了从 2D SAM 粒度到 3D 层级结构的新颖融合思路，并声称在多个基准上达到 SOTA，且涉及大语言模型的空间推理能力，对神经场景表征与渲染领域的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce LEGO for advanced open-vocabulary scene understanding. Beyond basic concept recognition, its core innovation lies in capturing the intrinsic semantic hierarchies within the scene, such as the "flowerpot -> bouquet -> bud -> petal" lineage. While foundation models like SAM can identify multi-granular structures in 2D, their partitions are strictly perspective-bound and lack cross-view consensus. LEGO self-adaptively re-grades volatile multi-view SAM granularities into a unified, 3D-consistent hierarchy. This provides precise supervision for the structurally coherent, multi-level segmentation of 3D scenes. By grounding these segments with CLIP embeddings, LEGO recovers open-vocabulary semantic logic across hierarchical levels. Furthermore, by incorporating spatial relationships, we elevate these segments into level-wise language scene graphs, effectively empowering Large Language Models to perform complex, context-aware spatial reasoning and precise visual grounding. Experimental results demonstrate that LEGO establishes new state-of-the-art performance across both promptable and open-vocabulary 3D segmentation benchmarks, exhibiting advanced hierarchical scene decomposition and context-aware spatial reasoning.

</details>

## Embodied / Robotics / AR Applications

### 2026-08

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

#### 2026-08-11 - Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models

**Authors:** Kiet T. Nguyen, Hanbo Shim, Jinwoo Kim, Seunghoon Hong
**Links:** [abs](https://arxiv.org/abs/2608.10864) - [pdf](https://arxiv.org/pdf/2608.10864)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models
- 作者：Kiet T. Nguyen, Hanbo Shim, Jinwoo Kim, Seunghoon Hong
- 出版日期：2026-08-11
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.10864

### 一句话总结
本文提出多视角关系蒸馏（MVRD），通过蒸馏跨视角的patch级余弦相似度而非教师特征本身，在保持视觉-语言对齐的同时提升视觉语言模型的空间推理能力。

### 研究问题
视觉语言模型（VLM）的视觉-空间表征在几何上较为脆弱，导致其在具身AI、机器人和自动驾驶所需的空间推理任务中表现不佳。现有方法（如直接在空间问答上微调或融合几何基础视觉模型特征）分别存在伪相关表征或推理时模型规模过大的问题。

### 核心思路/方法
MVRD不直接匹配几何基础教师模型的多视角特征，而是蒸馏跨视角的patch-wise余弦相似度。这些关系编码了几何对应信息，足以支持空间理解，同时对学生表征的约束是欠定的，使其能够保持在预训练的视觉-语言空间附近，从而不破坏原有的视觉-文本对齐。

### 主要贡献
- 提出多视角关系蒸馏（MVRD）方法，用于增强VLM的空间推理能力。
- 在多个代表性VLM上，MVRD优于监督微调和特征蒸馏，性能接近特征融合方法但参数量更少、延迟更低。
- 实验表明MVRD使视觉表征更具几何性，同时保持语言对齐。
- 方法可泛化到3D场景理解任务，包括物体定位、密集描述和问答。

### 局限性
摘要未提供足够信息（未具体说明失败案例、计算资源需求、蒸馏对教师模型依赖程度等局限性）。

### 阅读优先级
**高**

理由：该工作针对VLM空间推理这一关键瓶颈，提出了一种轻量且有效的蒸馏范式，在性能接近高开销特征融合方法的同时大幅降低推理成本，且已展示到3D场景理解的泛化能力。对从事具身AI、机器人、自动驾驶及多模态表征学习的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have achieved strong image and video understanding, yet their visual-spatial representations remain geometrically fragile, leading to failures in spatial reasoning needed for embodied AI, robotics, and autonomous driving. Prior approaches to geometry grounding either fine-tune VLMs on spatial question answering, which can perpetuate spurious visual representations, or fuse features from large geometry-grounded vision models, which substantially increases model size at inference. Knowledge distillation from geometry-grounded vision models offers an alternative, but directly matching multi-view teacher features can disrupt the pretrained alignment between visual and textual representations, degrading object- and language-semantic capabilities. We propose multi-view relational distillation (MVRD), which distills patch-wise cosine similarities across views instead of the teacher features themselves. These relations encode geometric correspondences adequate for spatial understanding, while leaving the student representation underdetermined, allowing it to remain close to its pretrained vision- language space. Across representative VLMs, MVRD improves visual-spatial reasoning, outperforming supervised fine-tuning and feature distillation while approaching feature fusion methods with considerably fewer added parameters and lower latency. We show that MVRD makes visual representations more geometric while retaining language alignment, and generalizes to 3D scene understanding tasks such as object grounding, dense captioning, and question answering.

</details>

#### 2026-08-11 - Cross-View Sequential Visual Localization with Spatio-Temporal Context Modeling for Autonomous Driving

**Authors:** Jiaping Wang, Shaobo Li, Zhen Wang
**Links:** [abs](https://arxiv.org/abs/2608.10660) - [pdf](https://arxiv.org/pdf/2608.10660)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cross-View Sequential Visual Localization with Spatio-Temporal Context Modeling for Autonomous Driving
- 作者：Jiaping Wang, Shaobo Li, Zhen Wang
- 出版日期：2026-08-11T08:44:42Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.10660

### 一句话总结
本文提出一种基于时空上下文建模的跨视角序列视觉定位框架，通过循环跨帧模块聚合历史信息，显著提升自动驾驶场景下跨视角定位的精度与鲁棒性。

### 研究问题
现有跨视角视觉定位方法大多逐帧独立处理，未充分利用时序信息，在动态遮挡、光照变化和重复纹理等场景下精度受限。本文旨在通过时序上下文增强来解决这一问题。

### 核心思路/方法
- 提出时间上下文增强的跨视角序列视觉定位框架。
- 设计循环跨帧模块，从上一状态聚合历史上下文，增强当前帧的粗粒度地面特征。
- 增强后的特征用于卫星候选区域分类，同时利用层次化细粒度特征进行精确的局部偏移估计。

### 主要贡献
- 提出一种循环跨帧模块以聚合历史时序信息，增强当前帧特征表达。
- 在CVIS数据集上将平均定位误差从3.80 m降至1.57 m，R@1 m从8.14%提升至40.22%。
- 在KITTI-CVL数据集上直接迁移平均误差为2.61 m，目标域微调后降至2.27 m。
- 真实车辆零样本实地实验平均误差为2.84 m，R@5 m达到96.86%，验证了方法的泛化能力与实用性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶跨视角定位的时序信息利用问题提出了明确且有效的解决方案，在公开基准和真实场景上均获得显著精度提升，实验结果量化且具说服力。对从事视觉定位、自动驾驶感知相关研究的人员具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Continuous and reliable localization is essential for autonomous driving. Cross-view visual localization matches ground images with satellite maps, providing complementary localization cues for pipelines that depend on Global Navigation Satellite System (GNSS) signals and high-definition (HD) maps. Most existing cross-view visual localization methods process each frame independently, leaving temporal information underused and limiting accuracy under dynamic occlusion, illumination variation, and repetitive textures. This study proposes a temporal-context-enhanced framework for cross-view sequence visual localization. The proposed recurrent cross-frame module aggregates historical context from the previous state to enhance the coarse ground feature of each current frame. These enhanced features facilitate satellite candidate-region classification, while hierarchical fine-grained features enable precise local offset estimation. On the CVIS dataset, the proposed method reduces mean localization error from 3.80 m to 1.57 m and increases R@1 m from 8.14% to 40.22%. Direct transfer to KITTI-CVL achieves a mean error of 2.61 m, with target-domain fine-tuning further reducing the mean error to 2.27 m. Zero-shot field experiments on a real-world vehicle achieve a mean error of 2.84 m and R@5 m of 96.86%. These results demonstrate that temporal context enhancement significantly improves cross-view localization accuracy and supports robust deployment on public benchmarks and real-world roads.

</details>

#### 2026-08-11 - Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent

**Authors:** Zitong Shan, Baichuan Lou, Yanxin Zhou, Shuge Wu, Xianqi He, Bolin Zhao, Sheng Zhao, Zhouheng Li, Chee Kiong Ong, King Ho Holden Li, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2608.10618) - [pdf](https://arxiv.org/pdf/2608.10618)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent
- 作者：Zitong Shan, Baichuan Lou, Yanxin Zhou, Shuge Wu, Xianqi He, Bolin Zhao, Sheng Zhao, Zhouheng Li, Chee Kiong Ong, King Ho Holden Li, Chen Lv
- 出版日期：2026-08-11T08:01:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要页](https://arxiv.org/abs/2608.10618) | [PDF](https://arxiv.org/pdf/2608.10618)

### 一句话总结
该研究提出一种以世界模型为中心的自动驾驶赛车智能体，通过在真实车辆和仿真环境中联合探索认知与物理极限，实现高速交互场景下的高成功率自主驾驶。

### 研究问题
具身智能系统在极端条件下（如高速、近饱和动力学、对抗性交互）的能力边界尚未被充分理解；现有系统虽能实现高速性能，但很少联合建模和优化认知极限与物理极限。

### 核心思路/方法
- 构建以世界模型为中心的闭环学习框架，从接近极限的成功与失败样本中学习预测世界模型，以捕获交互演化、自车动力学和可行运动边界。
- 将世界状态构建、未来感知推理和近极限控制整合在一个闭环优化过程中。
- 训练数据来自真实车辆自动驾驶赛车（最高速度256.3 km/h，峰值横向加速度26.8 m/s²），并在全尺寸仿真环境中进行验证和泛化测试。
- 通过世界模型与策略的闭环细化，提升极限利用率、失败模式恢复和跨场景泛化能力。

### 主要贡献
- 提出一种边界感知方法，使具身智能体能够表示、预测并持续细化自身能力边界。
- 在真实车辆极端工况下采集训练数据，验证了系统在高速和高峰值加速度下的鲁棒定位与感知能力。
- 在全尺寸仿真中达到88.3%的交互成功率，并展示了对不同场景和未知赛道的泛化能力。
- 实例化了一种将认知与物理极限联合探索的自主赛车智能体范式。

### 局限性
摘要未提供足够信息：未说明仿真与真实世界的差距、失败模式的具体类型、计算资源要求、对比基线方法、消融实验细节以及安全保证机制。

### 阅读优先级
**高**。理由：该工作将世界模型与自主赛车结合，直指具身智能在极端动态条件下的能力边界问题，且包含真实高速数据（256.3 km/h）和仿真验证（88.3%成功率），兼具理论深度与应用价值，对自动驾驶、具身智能和机器人控制领域有重要参考意义。

</details>

<details>
<summary>Abstract</summary>

Embodied artificial intelligence aims to develop agents that perceive, reason, and act through continuous interaction with the physical world. However, most embodied systems are still evaluated within conservative safety margins or moderate interaction regimes, leaving their capability boundaries under extreme conditions insufficiently understood. Autonomous racing provides a stringent testbed by combining high-frequency localization and perception, adversarial interaction, near-saturated vehicle dynamics, and strict safety constraints. Existing systems push high-speed performance but rarely model and refine cognitive and physical limits jointly. Here we show that a world-model-centric autonomous racing agent provides a concrete step toward exploring these coupled limits. The framework learns predictive world models from near-limit successes and failures to capture interaction evolution, ego dynamics, and feasible-motion boundaries, coupling world-state construction, future-aware reasoning, and near-limit control in a closed-loop refinement process. Training data were collected from real-vehicle autonomous racing, where the onboard system maintained robust localization and perception at speeds up to 256.3 km/h and peak lateral acceleration of 26.8 m/s$^2$. In full-scale simulated racing, the well trained world-model-centric agent achieves an 88.3% interaction success rate across various challenging simulated racing scenarios. Closed-loop refinement of the world model and policy further improved utilization of cognitive-physical limits, recovery from failure modes, and generalization across varying conditions and unseen circuits. These results suggest a boundary-aware methodology in which world models help embodied agents represent, predict, and continually refine their capability boundaries for safer real-world deployment.

</details>

#### 2026-08-11 - PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots

**Authors:** Shuo Bao, Wei Dong, Shuyue Zhang, Ming Shang, Yuchen Huang, Han Yu, Chengjie Xu, Yiheng Bi, Kai Sun, Fuchun Sun, Xinzhou Wang
**Links:** [abs](https://arxiv.org/abs/2608.10449) - [pdf](https://arxiv.org/pdf/2608.10449)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots
- 作者：Shuo Bao, Wei Dong, Shuyue Zhang, Ming Shang, Yuchen Huang, Han Yu, Chengjie Xu, Yiheng Bi, Kai Sun, Fuchun Sun, Xinzhou Wang
- 出版日期：2026-08-11
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.10449

### 一句话总结
本文提出PBD-AG框架，通过将稳定环境基线（baseline）与可更新的动态物体事件（delta）解耦，为长时程服务机器人构建可追溯、可修订的持久世界模型。

### 研究问题
长时程服务机器人在未见环境中自主建图并动态更新任务相关物体状态时，现有方法存在定位与观测误差累积、静态场景表示无法捕捉物体持续变化、以及缺乏可验证3D几何证据的视觉-语言整体预测等问题。本文旨在解决如何构建既稳定又能够随物体变化而修订的持久世界模型这一核心问题。

### 核心思路/方法
- 提出**持久基线-增量活动图（Persistent Baseline-Delta Active Graph）**框架，将机器人已验证的稳定固定设施（fixtures）与可修订的动态物体事件解耦。
- 机器人通过机载探索**自主引导**结构基线，并检查发现的固定设施以构建分层物体信念。
- 维护带可靠性权重的物体状态，涵盖几何、语义、身份、存在性及支撑关系。
- 引入**几何可见性门控**（geometric visibility gate）机制，减少遮挡导致的错误删除。
- 采用**图条件化策略**选择检查视点，综合权衡目标覆盖、移动成本、碰撞风险与冗余观测。

### 主要贡献
- 提出一种将稳定基线与动态变化解耦的持久世界模型框架，支持长时程自主建图与修订。
- 设计可靠性加权物体状态表示与几何可见性门控，提升物体存在性判断的鲁棒性。
- 提出图条件化主动检查视点选择策略，均衡覆盖、成本与风险。
- 在多种仿真环境及受控动态评估中，相比能力匹配的对照方法，在粗固定设施F1、身份连续性和事件召回率上取得更好表现。
- 通过物理机器人定性演示，验证了与机载感知集成的可行性，提供可追溯的世界模型。

### 局限性
摘要未提供足够信息，未明确讨论方法在真实复杂场景中的计算开销、扩展性、长期运行稳定性极限、失败模式或对感知噪声的敏感度等局限性。

### 阅读优先级
**高**。理由：论文面向服务机器人长期自主感知这一实际重要挑战，提出的基线-增量解耦思想与不确定性感知检查机制具有明确的方法创新性，且同时提供仿真定量评估与实物定性验证，对从事机器人建图、主动感知和世界模型研究的人员具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Long-horizon service robots require persistent world models that can be built autonomously in unseen environments and revised as task-relevant objects change. Existing methods rely on online mapping, which accumulates localization and observation errors, static scene representations that cannot capture persistent object changes, or holistic vision-language predictions that lack verifiable 3D geometric evidence. We present PBD-AG, a persistent baseline-delta active graph framework that decouples robot-verified stable fixtures from revisable dynamic object events. Under our framework, the robot autonomously bootstraps the structural baseline from onboard exploration and inspects discovered fixtures to ground hierarchical object beliefs. PBD-AG maintains reliability-weighted object states over geometry, semantics, identity, existence, and support relations, utilizing a geometric visibility gate to mitigate false deletions under occlusion. Inspection viewpoints are selected by a graph-conditioned policy that balances target coverage, travel cost, collision risk, and redundant observation. Simulation experiments in multiple environments and under controlled dynamic evaluation show higher aggregate coarse-fixture F1 than capability-matched controls, as well as stronger identity continuity and event recall. A qualitative physical-robot demonstration further illustrates integration with onboard sensing, providing a traceable world model for long-horizon robotic perception. The project page of PBD-AG is available at https://shuobao214.github.io/PBD-AG/

</details>

#### 2026-08-10 - 4D-WAM: 4D Consistent World Modeling for Autonomous Driving

**Authors:** Jiacheng Fu, Yibo Yuan, Meng Tian, Yue Li, Jiangtong Zhu, Jianhua Han, Yueyi Zhang, Jianwu Fang, Jianru Xue, Hang Xu, Zhiwei Xiong
**Links:** [abs](https://arxiv.org/abs/2608.10107) - [pdf](https://arxiv.org/pdf/2608.10107)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric foundation model, autonomous driving, driving scene, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4D-WAM: 4D Consistent World Modeling for Autonomous Driving
- 作者：Jiacheng Fu, Yibo Yuan, Meng Tian, Yue Li, Jiangtong Zhu, Jianhua Han, Yueyi Zhang, Jianwu Fang, Jianxue Xue, Hang Xu, Zhiwei Xiong
- 出版日期：2026-08-10T18:14:52Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.10107

### 一句话总结
4D-WAM 通过引入几何基础模型在训练阶段提供 4D 一致性监督，使自动驾驶世界模型能够预测物理一致的 4D 场景演化，从而提升轨迹规划性能。

### 研究问题
现有世界-动作模型（WAM）仅基于视频（2D 投影）训练，缺乏对底层 4D 驾驶场景结构的理解，导致生成视觉上合理但 4D 不一致的未来预测，进而误导下游规划任务。

### 核心思路/方法
- 将 WAM 预测的未来帧输入到几何基础模型中，利用其输出的 4D 感知响应定义 4D 一致性损失，在训练时监督模型理解并预测物理一致的 4D 场景，且不增加推理成本。
- 识别出 WAM 的“早期决策”现象，并提出面向决策的时间步采样策略，重点关注早期高噪声阶段（此时驾驶决策主要形成），将 4D 监督传播到该关键阶段以进一步改进轨迹规划。

### 主要贡献
- 提出 4D-WAM，一种利用几何基础模型进行训练时监督、实现 4D 一致世界建模的方法。
- 提出决策导向的时间步采样策略，针对 WAM 的早期决策现象强化关键阶段监督。
- 在 NAVSIM-v1 和 NAVSIM-v2 基准上取得最先进性能，有效建模 4D 一致的场景演化。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶中世界模型的核心缺陷（4D 不一致）提出新颖且低成本的解决思路（训练时监督+决策导向采样），并在两个挑战性基准上达到 SOTA，对自动驾驶感知与规划交叉领域具有较强参考价值。摘要提供了完整的方法动机和验证结论，适合目标研究者深入阅读。

</details>

<details>
<summary>Abstract</summary>

Emerging World-Action Models (WAMs) have demonstrated promising performance in autonomous driving by jointly modeling future driving scene evolution and trajectory planning. However, existing WAMs are typically trained with video data, which is only 2D projections of the underlying 4D driving scene. Consequently, WAMs fail to understand and capture the structure of 4D scenes and thus generate visually plausible yet 4D inconsistent future predictions that mislead downstream planning. To alleviate this issue, we present 4D-WAM, a model that leverages geometric foundation models for training-time supervision to enable 4D consistent world modeling. Specifically, we feed WAM-predicted future frames into a geometric foundation model, and use 4D-aware responses to define a 4D consistency loss. This loss encourages the model to understand, represent, and predict physically consistent 4D scenes during training, without additional inference cost. Moreover, we identify an early-decision phenomenon in WAMs and propose a decision-oriented timestep sampling strategy that emphasizes supervision at early, high-noise stages, where driving decisions are primarily formed. By propagating 4D supervision to this critical decision-formation phase, the proposed strategy further improves trajectory planning. Extensive experiments demonstrate that 4D-WAM effectively models 4D consistent scene evolution and achieves state-of-the-art performance on challenging NAVSIM-v1 and NAVSIM-v2 benchmarks.

</details>

#### 2026-08-10 - SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation

**Authors:** Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen, Jingjiao Zhao, Xiansheng Chen, Pengwei Wang, Lemao Liu, Dejing Dou
**Links:** [abs](https://arxiv.org/abs/2608.09771) - [pdf](https://arxiv.org/pdf/2608.09771)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation
- 作者：Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen, Jingjiao Zhao, Xiansheng Chen, Pengwei Wang, Lemao Liu, Dejing Dou
- 出版日期：2026-08-10T15:58:39Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.09771

### 一句话总结
本文提出一种仅0.5B参数的紧凑型机器人操作策略SLIM，通过自监督学习动作相关的潜在动态表征，在减少计算资源的同时匹配或超越大型VLA基线的性能。

### 研究问题
如何在不依赖大规模多模态骨干网络和额外具身预训练的情况下，学习紧凑且有效的动作相关潜在表征，以支持语言条件下的机器人连续操作。

### 核心思路/方法
- 提出SLIM（Self-supervised Latent Interaction Model），一种0.5B参数的潜在交互策略。
- 学习“动作锚定的预测性潜在表征”（action-grounded predictive latents），同时捕获动作条件化的未来状态转移，以及能够解释观测变化的动作。
- 采用自监督掩码轨迹预测，结合动作重建与未来潜在预测两个目标进行表征学习。
- 使用紧凑的Mixture-of-Transformers（MoT）骨干网络建模观测潜在与动作token之间的交互。
- 最终策略通过流匹配（flow matching）训练，实现语言条件下的动作生成。

### 主要贡献
- 提出一种紧凑的0.5B参数潜在交互策略，避免大型多模态骨干网络带来的计算开销。
- 设计自监督掩码轨迹预测方法，使模型学习动作与观测变化之间的因果关系。
- 在仿真基准和真实机器人评估中，以更少的参数、更低的推理延迟和GPU内存占用，匹配或超越代表性大型VLA和世界动作模型基线，且无需额外具身预训练。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法的适用边界、失败案例、泛化场景限制或计算复杂度对比的具体数值。

### 阅读优先级
**高**。理由：该工作针对视觉-语言-动作策略计算开销大的痛点，提出紧凑高效的替代方案，在保持性能的同时大幅降低资源需求，对资源受限的机器人部署具有实际意义；且仿真与真实实验均验证了有效性，值得关注。

</details>

<details>
<summary>Abstract</summary>

Vision-language-action policies rely on large multimodal backbones to jointly perform perception, language conditioning, and action generation at every control step. Much of this capacity supports open-domain semantics, whereas continuous robot manipulation primarily requires compact representations of observations, actions, and the transitions induced by actions. Pixel-level world models provide another route, but predicting visual details irrelevant to control can be unnecessarily expensive. We propose SLIM (Self-supervised Latent Interaction Model), a compact 0.5B-parameter latent interaction policy. SLIM learns action-grounded predictive latents that capture both action-conditioned future transitions and the actions that explain observed changes. SLIM learns these representations through self-supervised masked trajectory prediction, combining action reconstruction with future-latent prediction. A compact Mixture-of-Transformers (MoT) backbone models interactions between observation latents and action tokens. The resulting policy is trained with flow matching for language-conditioned action generation. Across simulation benchmarks and real-world evaluation, SLIM matches or exceeds representative large-scale VLA and world-action-model baselines with fewer parameters, no additional embodied pretraining, lower inference latency, and substantially lower GPU memory usage.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
