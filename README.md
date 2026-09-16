# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：21
- 分类分布：
  - Neural Scene Representations & Rendering: 7
  - Embodied / Robotics / AR Applications: 6
  - 3D Reconstruction & Multi-view Geometry: 5
  - Geometry Foundation Models: 2
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **从“新视角合成”走向“物理量渲染”：雷达、全息、雾天介质成为新前沿**
   今日多篇论文不再满足于 RGB 意义上的“看起来对”，而是要求渲染器输出可被下游物理系统直接使用的量。`3DPS` 直接从雷达方程立体角形式推导可微点渲染，输出复数相量而非功率幅度；`CVQPG` 把 2D 高斯基元替换为二次相位函数，直接调制全息波前；`Tri-DehazeGS` 把场景与参与介质显式解耦，用独立三平面场建模散射介质。三者共同指向一个趋势：**神经渲染器正在从“图像逼真”转向“物理保真”**，且介质、相位、材质被显式建模而非交给不透明隐特征。

2. **3DGS 生态进入“精细化治理”阶段：剪枝、不确定性认证、跨表示蒸馏、重定位耦合**
   3DGS 不再只是“如何建得更快更好”，而是围绕其工程与可信度缺陷做系统性补丁。`LinearMask-GS` 聚焦学习掩码剪枝中 Gumbel-Sigmoid 导致的早熟双峰分布，改线性增量激活；`VSCP` 关注 3DGS 渲染的视图级覆盖保证，把新视角合成当作结构化回归做共形预测；`RouteBridge` 处理 NeRF 与 3DGS 之间“全局固定教师会传播局部误差”的问题，按光线做可靠性路由；`RIDE` 则把 render–match–PnP 重定位的稀疏度量深度与视频深度先验结合，让 3DGS 地图反过来服务稠密深度。这类工作数量最多，说明**3DGS 正从表示创新期转入可靠性与可部署性补课期**。

3. **几何基础模型与图像匹配的边界正在消融，但“零样本匹配”本身仍未解决**
   `RoMa-$Ω$` 直接追问“前馈 3D 模型到底知道多少图像匹配”，通过三种场景（patch 特征零样本匹配、3D 点预测直接匹配、在其表征上训练完整匹配器）进行分析，并以 VGGT-$Ω$ 替换 DINO 骨干。`SAMV-DUSt3R` 则把 SAM2 2D 掩码注入 MV-DUSt3R，做实例级场景解耦。`Learning Global Camera Poses from Noisy View-Graphs` 用置换等变边条件 GNN 从带噪相对位姿回归全局外参，无需真值监督。这些工作共同反映：**几何基础模型正在吸收匹配与解耦能力，但“零样本深层特征直接做匹配”表现不佳，仍需要在其表征之上训练任务头**，这本身是一个被实验明确化的空白。

4. **动态/4D 重建向长时程突破，前馈模型开始处理数百帧**
   `Point4D` 明确针对现有 4D 方法“至多几十帧”的窗口限制，用基于 3D 查询的运动解码器解耦轨迹预测与图像平面可见性，预测的 3D 端点可在下一时间块直接重新查询，无需重投影或匹配。这代表 **4D 重建的竞赛焦点从“短窗口精度”转向“长时程稳定跟踪”**，且“跨帧复用视觉描述符优于仅用源 patch”是一个可复用的设计结论。

5. **具身与机器人应用层开始整合“感知—仿真—控制—运维”全链路，而非单点算法**
   `HROS`/Argos 把四足巡检组织为机器人运行时、自主技能、认知智能体运行时、交互运维平面，并用共享上下文连接物理状态与推理；`SyncWorld` 用“视觉校准片段”在上下文里指定动作-视觉映射，使世界模型成为零样本模拟器；`Grounding Generated Video Plans` 用生成 HOI 视频提供运动参考、在仿真中 grounding 超过 1500 个视频；`RealSimLoop` 在降阶神经子空间做可微仿真，用视觉反馈在线校正材料参数。**机器人方向今日的关键词是“闭环”与“校准”**——动作不是像素空间的通用语言，视觉校准、可靠性路由、安全门控都是为了让闭环可控。

#### 技术路线观察

- **几何基础模型**：`RoMa-$Ω$` 和 `Learning Global Camera Poses` 代表两条不同路线。前者是“表征复用”——把前馈重建模型（VGGT）的内部表征迁移到匹配器；后者是“端到端学习全局 SfM”——用图神经网络直接回归全局外参，训练信号仅为相对位姿一致性。`SAMV-DUSt3R` 则走“注入式”路线，把 2D 基础模型（SAM2）的掩码作为条件信号注入重建网络。三者的共同点是不再迷信单一基础模型的零样本能力，而是**显式地在其上做条件化、路由或重训练**。

- **3D/4D 重建**：`Point4D` 是今日唯一明确的长时程 4D 工作，技术核心是“查询解耦”——3D 端点跨块直接重查询，绕过重投影与匹配，这对长视频中的漂移控制有直接价值。`Field Converter` 则代表体育/转播场景的世界坐标人体姿态，用相机与球场几何初始化根节点、再预测时序残差，其“几何初始化+残差精修”的范式与 `Point4D` 的“查询+重查询”形成有趣对照：都是用几何或查询提供稳定锚点，再让网络学习修正量。

- **神经场景表示**：分化最明显。雷达（`3DPS`）走物理方程推导路线，强调复值与材质；全息（`CVQPG`）走波前调制路线，强调频域保留；雾天（`Tri-DehazeGS`）走场景-介质解耦路线，强调梯度重平衡；3DGS 压缩（`LinearMask-GS`）与可靠性（`VSCP`）走工程治理路线；跨表示（`RouteBridge`）走按光线路由路线。**没有单一主导技术路线，而是按输出物理量、介质假设和可靠性需求分层演化**。

- **机器人/AR 应用**：`HROS`、`SyncWorld`、`Grounding Generated Video Plans`、`RealSimLoop` 共同显示，应用层论文的贡献越来越难用单一算法指标衡量，而是以系统能力（闭环可追踪、零样本迁移、参考运动可扩展、在线自适应）来主张价值。`GoDeep` 则代表另一条线：用语言空间做 3D 开放词汇理解，把 VLM 当“翻译器”而非特征提取器，强调离散文本带来的可解释性。

#### 值得优先阅读的论文

1. **`3DPS` (3D Point Splatting for mmWave Radar NVS, 2609.11894)**
   优先理由：它是今日唯一明确“首个”定位的工作，且技术推导路径清晰（从雷达方程立体角形式直接推导可微点渲染器），复数输出使同一优化场景可通过 FFT 流水线产出 ADC、CRP、RA 多种格式，避免了按格式重训练。对雷达感知、物理渲染、复值神经表示三个方向都有交叉参考价值。建议重点验证其“单卡约 3 分钟/场景”是否在摘要之外有完整实验支撑。

2. **`Point4D` (Long-range 4D Motion Reconstruction, 2609.09145)**
   优先理由：直接针对 4D 重建公认的短窗口瓶颈，提出 3D 查询解耦与跨块重查询机制，且在 200 帧以上长视频追踪基准上取得领先。其“视觉描述符从任意可见帧提取优于仅用源 patch”的结论具有可迁移性，适合做长视频动态重建的基线或改进起点。

3. **`RoMa-$Ω$` (What Feed-Forward 3D Models Know About Image Matching, 2609.09507)**
   优先理由：它不是单纯提出一个匹配器，而是系统回答了“前馈

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-16T12:51:30-04:00
**Total number of papers:** 40
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

### 2026-09

#### 2026-09-15 - G3AR: Graph-Guided Neural Visual Geometry for Scalable Multi-Sequence Aerial Registration

**Authors:** Jeng Wen Joshua Lean, Ting-Yu Yen, Wei-Fang Sun, Simon See, Hung-Kuo Chu, Shih-Hsuan Hung
**Links:** [abs](https://arxiv.org/abs/2609.16603) - [pdf](https://arxiv.org/pdf/2609.16603)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>Abstract</summary>

Full-context neural visual geometry is impractical for thousands of images, while sequence-based chunking poorly captures irregular non-local overlap in multi-sequence aerial collections. We present Graph-Guided Neural Visual Geometry for Aerial Registration (G3AR), a graph-guided framework for scalable dense neural geometry. Before local inference, G3AR builds a geometrically verified image-proximity graph that guides bounded overlapping chunks and induces a chunk graph whose maximum spanning tree defines alignment topology. Compatible backbones process chunks independently; shared-image predictions then estimate three-dimensional similarity (Sim(3)) transforms that register local cameras and geometry in a common frame. Across four real aerial scenes, G3AR improves pose error and runtime in matched VGGT- and Pi3-backed comparisons, while its DA3 variant achieves the lowest pose error among evaluated neural-geometry methods.

</details>

#### 2026-09-14 - SURE-Map: Self-Correcting Streaming Geometric Foundation Model

**Authors:** Mingkai Liu, Hao Zhao, Xingxing Zuo
**Links:** [abs](https://arxiv.org/abs/2609.15795) - [pdf](https://arxiv.org/pdf/2609.15795)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** geometric foundation model, feed-forward reconstruction, SLAM

<details>
<summary>Abstract</summary>

Streaming geometric foundation models are emerging as a compelling alternative to SLAM systems. Yet this streaming nature introduces a fundamental issue: each prediction is made from limited context, which is vulnerable to dynamic objects and weak textures. Small local errors accumulate into severe geometric distortion and long-horizon scale drift. We argue that reliable streaming reconstruction requires geometric foundation models to be not only predictive, but also self-correcting. We introduce SURE-Map, a self-correcting framework built upon two complementary principles. First, we explicitly model cross-view geometric uncertainty. Unlike conventional depth or point confidence, which primarily reflects the reliability of individual-view prediction, our uncertainty directly measures whether the jointly predicted pose and depth induce geometrically consistent cross-view pixel correspondences. Second, because local correction alone cannot eliminate slowly accumulating scale errors, we introduce multi-timescale self-correction: fast consecutive-frame inference preserves streaming efficiency, while sparse keyframe-window inference provides longer-range geometric evidence to periodically recalibrate the scale of recent trajectories. SURE-Map establishes new state-of-the-art performance for online feed-forward reconstruction across long-horizon benchmarks, reducing ATE-RMSE from 24.00 to 17.24 m on KITTI, 5.11 to 4.74 m on Oxford Spires, and 31.37 to 28.58 m on VBR, with further improvements to 15.17, 4.63, and 22.12 m when incorporating loop-closure refinement. Project page: https://mingkai-liu.github.io/projects/sure-map/.

</details>

#### 2026-09-14 - Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras

**Authors:** Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu
**Links:** [abs](https://arxiv.org/abs/2609.15032) - [pdf](https://arxiv.org/pdf/2609.15032)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Dynamic / 4D Reconstruction
**Matched keywords:** geometry foundation model, multi-view transformer, dynamic 3D, human reconstruction, rendering

<details>
<summary>Abstract</summary>

Live free-viewpoint visualization of real humans is critical for immersive communication and interactive digital experiences. Existing methods either rely on computationally expensive optimization or require calibrated cameras and low-resolution inputs, making real-time high-resolution deployment impractical. In this work, we present Tele360, the first real-time feed-forward system for dynamic human reconstruction and live free-viewpoint visualization from sparse, unposed RGB streams. Our system jointly estimates camera poses and reconstructs a dynamic 3D Gaussian representation for each time instance in a single forward pass. To achieve this, we start by designing a lightweight sparsity-aware multi-view transformer backbone that tokenizes foreground human regions while preserving global context through a shared scene token. We then employ a fully transformer-based Gaussian decoder to mitigate convolution-induced over-smoothing while keeping decoding sparse and efficient. In addition, we introduce a hybrid feature pyramid that injects multi-scale appearance cues into geometry prediction. We further introduce a lightweight differentiable Levenberg-Marquardt camera refinement layer to enhance multi-view consistency and geometric alignment. Moreover, to stabilize learning under sparse, unposed inputs, we transfer multi-view geometry priors from a large visual-geometry foundation model via teacher-student distillation. Finally, the predicted Gaussian maps are streamed with video codecs to remote devices for interactive free-viewpoint rendering. Extensive experiments show that Tele360 achieves state-of-the-art visual quality on studio benchmarks while supporting real-time 2K input-to-rendering at over 25 FPS on a single consumer GPU. Additional captured sequences illustrate its performance across varied subjects, clothing, and motions under our multi-camera setup.

</details>

#### 2026-09-10 - SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views

**Authors:** Langxu Zhao, Zuan Gu, Yingdan Zhang, Pengfei Zhao, Tianhan Gao
**Links:** [abs](https://arxiv.org/abs/2609.11279) - [pdf](https://arxiv.org/pdf/2609.11279)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** DUSt3R, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views
- 作者：Langxu Zhao, Zuan Gu, Yingdan Zhang, Pengfei Zhao, Tianhan Gao
- 出版日期：2026-09-10T09:12:48Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.11279 ；PDF https://arxiv.org/pdf/2609.11279

### 一句话总结
该论文提出端到端模型 SAMV-DUSt3R，将 SAM2 的 2D 掩码注入 MV-DUSt3R 重建流程，以在稀疏多视角下实现以实例为中心的三维场景解耦，并报告了重建精度与参考视图选择方面的提升。

### 研究问题
从三维场景中解耦物体（实例级分离）的需求日益增长，论文关注在稀疏多视角条件下实现实例级的三维场景解耦与重建。摘要指出其目标是在不依赖多阶段流水线的情况下完成物体级解耦，并同时提升形状精度与重建稳定性。

### 核心思路/方法
- 提出端到端模型 SAMV-DUSt3R，将 SAM2 的二维掩码注入到 MV-DUSt3R 的重建过程中。
- 设计 Cross Flow Mask Block，利用这些掩码引导网络朝向目标实例，从而联合提升形状精度并实现物体级解耦，且无需多阶段流水线。
- 为保证重建稳定性，引入轻量级 Spatial RankGNN 来选择最优参考视图，摘要给出选择准确率为 73.5%。

### 主要贡献
- 提出将 SAM2 二维掩码注入 MV-DUSt3R 重建的端到端方法，实现以实例为中心的三维场景解耦，避免多阶段流水线。
- 通过 Cross Flow Mask Block 引导网络关注目标实例，联合改善形状精度并实现物体级解耦。
- 引入轻量级 Spatial RankGNN 进行最优参考视图选择，报告选择准确率为 73.5%。
- 摘要称大量实验表明，与最先进基线相比，该方法在多种指标上平均重建精度提升 11%，并展现出较强的实例解耦能力，对驾驶、机器人、AR/VR 和遗产数字化具有明显益处。

### 局限性
- 摘要未提供足够信息说明实验数据集、评价指标细节、对比基线的具体配置以及消融实验设置。
- 摘要未提供足够信息说明方法在不同稀疏视角数量、遮挡、动态场景或类别分布下的失效条件与适用范围。
- 摘要未提供足够信息说明 Spatial RankGNN 选择错误时对重建结果的影响程度，以及 Cross Flow Mask Block 对 SAM2 掩码质量的依赖与鲁棒性。
- 摘要未提供足够信息说明计算开销、推理速度、模型规模与训练数据需求。

### 阅读优先级
高。理由：该论文聚焦稀疏多视角下的实例级三维场景解耦，提出端到端注入 2D 掩码与参考视图选择的组合方案，并在摘要中报告了明确的重建精度提升与选择准确率；主题同时关联几何基础模型与具身/机器人/AR 应用，对三维重建与实例解耦方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

With the rising demand to decouple objects from 3D scenes, we propose SAMV-DUSt3R, an end-to-end model that injects SAM2 2D masks into MV-DUSt3R reconstruction. A Cross Flow Mask Block uses these masks to steer the network toward the target instance, jointly improving shape accuracy and achieving object-level disentanglement without multi-stage pipelines. To ensure reconstruction stability, a lightweight Spatial RankGNN selects the optimal reference view with a selection accuracy of 73.5\%. Extensive experiments demonstrate that our method boosts average reconstruction precision by 11\% across various metrics compared to state-of-the-art baselines. These results reveal a strong instance-disentanglement capability and clear benefits for driving, robotics, AR/VR, and heritage digitisation.

</details>

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-14 - Racing in Volume with Flow Ensembles

**Authors:** Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre
**Links:** [abs](https://arxiv.org/abs/2609.16310) - [pdf](https://arxiv.org/pdf/2609.16310)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Streaming 4D reconstruction has been demonstrated only indoors, on dense camera rigs surrounding subjects that move at human pace. Outdoor 4D reconstruction exists but relies either on cameras mounted on the moving vehicle itself, or on limited-coverage arrays observing quasi-static subjects offline. The case that actually matters for spectators is a fast-moving subject, watched from a sparse ring of allocentric cameras, streaming. No method targets this, and no benchmark exists to evaluate one. To this end, we introduce FastFlowGS, a streaming 4D Gaussian Splatting method for reconstructing fast-moving subjects from a small set of fixed external cameras, and Monaco4D, a photorealistic Unreal Engine 5 benchmark for high-speed outdoor reconstruction. FastFlowGS fuses sparse matches, semi-dense tracks, and dense optical flow by lifting each signal to 3D with geometric uncertainty and combining them through a Kalman-style temporal update. Monaco4D provides Formula 1 sequences under varied illumination from trackside, onboard, and drone viewpoints with dense ground truth. On CMU-Panoptic, FastFlowGS exceeds the strongest baseline by 12.6% VMAF at 35% greater efficiency. On Monaco4D, where existing streaming methods degrade severely, it improves dynamic-region PSNR by up to 18.6% with 28.3% lower per-frame optimization time. Dataset and additional details can be found at https://humansensinglab.github.io/monaco4d/.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-15 - EventEgoHands++: Event-based Egocentric 3D Hand Mesh Reconstruction with Real Dataset

**Authors:** Ryosei Hara, Wataru Ikeda, Masashi Hatano, Mariko Isogawa
**Links:** [abs](https://arxiv.org/abs/2609.17189) - [pdf](https://arxiv.org/pdf/2609.17189)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction, AR, VR

<details>
<summary>Abstract</summary>

3D hand mesh reconstruction is a challenging yet essential task for downstream applications, including human-robot interaction and AR/VR. Although conventional cameras have been widely adopted for this task, methods that rely on them struggle in low-light environments and under severe motion blur. To address these limitations, event-based cameras have recently attracted attention for their high dynamic range and high temporal resolution. However, applying event cameras to egocentric hand reconstruction remains challenging because camera wearer's motion produces dense background events that obscure hand-specific signals. Although the first egocentric event-based approach mitigates this issue using hand segmentation, its binary hand mask does not distinguish between left and right hands. As a result, the model lacks instance-level hand information and predicts both hands even when only one or neither hand is present. This limitation leads to incorrect inter-hand relationships and degraded reconstruction accuracy. In this paper, we propose EventEgoHands++, a framework for event-based 3D hand mesh reconstruction from an egocentric viewpoint. The proposed method incorporates a Hand Detector that estimates instance-level bounding boxes and masks for both the left and right hands. Moreover, we introduce Adaptive Attention, which dynamically gates the attention based on these detection results to accurately learn the spatial relationship and mutual interactions between the hands. To train and evaluate our framework, we extend the synthetic N-HOT3D dataset and newly construct EEH-R, the largest real-world event-based egocentric hand dataset to date, comprising approximately 1M annotated frames captured in environments including low-light conditions. Extensive experiments on both synthetic and real datasets demonstrate that our method consistently outperforms the baselines.

</details>

#### 2026-09-15 - HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM

**Authors:** Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei, Andrew Bradley, Alexander Rast
**Links:** [abs](https://arxiv.org/abs/2609.17168) - [pdf](https://arxiv.org/pdf/2609.17168)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, mapping

<details>
<summary>Abstract</summary>

Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place appears different. Although semantic SLAM and modern learned visual place recognition (VPR) methods improve robustness under challenging perceptual conditions, real-time deployment requires both high retrieval accuracy and low latency. Inspired by human memory and perception, we propose HuMem-VPR, which exploits the bidirectional relationship between bottom-up perceptual evidence and top-down contextual reasoning to achieve high-level place understanding. We further introduce HuMemSLAM, the integration of HuMem-VPR with ORB-SLAM3. HuMem VPR achieved the highest aggregate retrieval accuracy on the real-image benchmark, competitive accuracy on the CARLA benchmark, and approximately two to three times lower latency than the evaluated state-of-the-art VPR methods. Across the evaluated dataset families and online experiments, HuMemSLAM substantially improved integrated Recall @1 over ORB-SLAM3's native retrieval while reducing the proposals submitted to its geometric backend.

</details>

#### 2026-09-15 - BRAVE-6D: Benchmark for Robotic Active Vision in 6DOF Pose Estimation

**Authors:** Philipp Ausserlechner, Bernhard Neuberger, Alessandro Scherl, Michael Schebek, Stefan Thalhammer, Markus Vincze
**Links:** [abs](https://arxiv.org/abs/2609.17106) - [pdf](https://arxiv.org/pdf/2609.17106)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** pose estimation, 3DGS, view synthesis, robotics

<details>
<summary>Abstract</summary>

Detecting and grasping small objects remains a significant challenge in robotics. Active vision, where the robot moves closer to the object, is an intuitive solution, yet comparing approaches on common ground is difficult since identical physical scene setups are required. Hence, we introduce BRAVE-6D, a benchmark designed to evaluate robotic active vision systems for object pose estimation, a crucial first step in grasping objects. BRAVE-6D leverages view synthesis based on Gaussian Splats (3DGS) to provide scenes and tools for benchmarking active vision systems. We show baseline solutions performing visual servoing within the scene and accurately estimating the poses of small objects.

</details>

#### 2026-09-15 - Evaluating Mesh Reconstruction Methods for Crop Phenotyping

**Authors:** Karanvir Singh, Theo Morales, Binh-Son Hua, Mukesh Saini
**Links:** [abs](https://arxiv.org/abs/2609.16926) - [pdf](https://arxiv.org/pdf/2609.16926)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mesh reconstruction

<details>
<summary>Abstract</summary>

Phenotyping an agricultural crop is crucial for studying its entire life cycle, as it provides vital insights to improve yield and, ultimately, food production. Doing the same for crops grown on remote sites is a challenge for the specialists who cannot be available on-site. 3D reconstruction techniques offer a promising solution to this problem by enabling crop digitization, allowing specialists to access the resulting 3D crop models from anywhere at any time. In this work, we evaluate recent 3D reconstruction pipelines for crop phenotyping. We focus on 7 mesh reconstruction pipelines and measure the fidelity and consistency of their outputs qualitatively and quantitatively. Our results suggest that the meshes produced by the GGGS, PGSR, and 2DGS are preferable to the other pipelines, owing to their quantitative metrics and visually pleasing outputs. The GGGS pipeline is better than the second-best pipeline (2DGS) by about 27\% on the radar chart with 5 dimensions, namely, User ratings, Chamfer distance, LPIPS, PSNR, and SSIM.

</details>

#### 2026-09-15 - PriorPose: Reference-Guided Joint Deformation and Alignment for Category-Level Object Pose Estimation

**Authors:** Yihan Chen, Huan Ren, Wenfei Yang, Hang Du, Tianzhu Zhang, Feng Wu
**Links:** [abs](https://arxiv.org/abs/2609.16727) - [pdf](https://arxiv.org/pdf/2609.16727)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Category-level object pose estimation seeks to recover a similarity transform $(R,t,s)$ for unseen instances without instance-specific CAD models. Most competitive methods are correspondence-based: prior-free variants regress canonical (NOCS) coordinates directly from local observations and implicitly memorize the canonical frame in the weights, which ties the parameters to category-typical orientations and hurts generalization under distribution shift; prior-based variants introduce a category prior but typically follow a serial deform-then-align pipeline, where underconstrained canonical completion can corrupt correspondences and induce error cascades in pose. We propose PriorPose, a reference-guided correspondence framework that keeps the category prior explicit and solves canonicalization and alignment jointly in a shared feature space. A reference-guided seeded transformer embeds the partial observation and the category prior as token sets and fuses them via geometry-aware seeds, from which the network jointly predicts a per-point NOCS field for visible points and a canonical deformation of the prior that reconstructs a full canonical instance, while a deep pose head regresses $(R,t,s)$ from the induced correspondences. A two-part shape consistency objective, with canonical-space and camera-space consistency losses, couples correspondence, deformation, and pose, reducing reliance on memorized canonical orientations and avoiding deform-then-align error cascades. Experiments on standard and larger-category benchmarks demonstrate that PriorPose sets new state-of-the-art results on most evaluated metrics, especially under strict pose thresholds, while remaining competitive on relaxed pose and IoU metrics and showing improved robustness under shape variation and domain shift.

</details>

#### 2026-09-14 - Tendon-Driven Continuum Robot with Modular Stiffness and In-Situ Self Pose Estimation

**Authors:** Guo Ning, Sue, Zheng Cao, Junzhe Hu, Xiangyun Bu, David Quinn, Tiancheng Wu, Zackory Erickson, Carmel Majidi
**Links:** [abs](https://arxiv.org/abs/2609.16256) - [pdf](https://arxiv.org/pdf/2609.16256)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Continuum robots enable smooth shape morphing and safe interaction in confined environments. However, most existing systems are task-specific and depend on external sensing infrastructure, limiting their adaptability and real-world deployment. This paper presents a self-contained modular continuum robotic platform that combines mechanical reconfigurability with onboard pose estimation. The robot is constructed from interchangeable continuum joints with analytically precomputed stiffness, allowing rapid assembly and direct programming of the robot shape. Proprioceptive sensing is achieved using magnetic sensors and a modular learning-based framework, where a single model is trained per joint and reused across configurations. The system is experimentally validated in real world, demonstrating self-sensing capabilities and adaptation without external tracking.

</details>

#### 2026-09-14 - Integrating Multi-view Multi-light Surface Reconstruction into Cultural Heritage Workflows

**Authors:** Baptiste Brument, Robin Bruneau, Benjamin Coupry, Vincent Demoulin, Jean Mélou, Antoine Laurent, Fabien Castan, Jean-Denis Durou, Lilian Calvet
**Links:** [abs](https://arxiv.org/abs/2609.15833) - [pdf](https://arxiv.org/pdf/2609.15833)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** surface reconstruction, photogrammetry

<details>
<summary>Abstract</summary>

Cultural heritage documentation increasingly relies on image-based 3D surface reconstruction, with photogrammetry software making such workflows accessible to archaeologists, conservators, and heritage technicians. These tools have been successful for conventional multi-view acquisition, but they do not routinely exploit richer multi-view, multi-light data, despite its potential for improving fine-scale surface reconstruction. This limitation is particularly relevant in heritage contexts, where controlled-light acquisition devices such as RTI domes are already used to capture illumination-varying image sets. The challenge is therefore to connect these existing acquisition practices with recent computer vision methods in a form that can be used within operational heritage workflows. In this work, we address this need by integrating state-of-the-art components from computer vision for multi-view, multi-light surface reconstruction into Meshroom, an open-source photogrammetry framework. Rather than proposing a new reconstruction algorithm, our contribution is to assemble and expose existing advanced methods, namely a complete photometric stereo ecosystem (calibrated, self-calibrated and universal), automatic object masking, and multi-view normal-and-reflectance integration, within a usable heritage-oriented workflow. The proposed system thus provides an intermediate software layer between computer vision research code and practical cultural heritage applications, making recent techniques easier to use and evaluate.

</details>

#### 2026-09-14 - LG-VLN: A Zero-Shot Vision-and-Language Navigation Framework with LangGraph State Orchestration

**Authors:** Jianhe Zhao, Yanhua Qiu, Zhiyu Zhang, Zibo Zhao, Jinhua Xie
**Links:** [abs](https://arxiv.org/abs/2609.15098) - [pdf](https://arxiv.org/pdf/2609.15098)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, pose estimation, mapping

<details>
<summary>Abstract</summary>

Continuous-environment vision-and-language navigation (VLN-CE) requires interpreting natural-language instructions in unseen 3D environments and executing continuous low-level actions. Existing methods often depend on LiDAR, panoramic cameras, or extra sensors; separate geometric-mapping and semantic-navigation visual representations can cause long-trajectory spatial-semantic inconsistencies. We propose LG-VLN, a monocular zero-shot framework with shared visual features and LangGraph-based state orchestration. An online feed-forward 3D reconstruction network predicts depth, camera poses, and dense point clouds for agent-pose estimation and global map fusion. Geometry and navigation share dense CleanDIFT features: semantic consistency rejects incorrect inter-frame correspondences, while target-instance constraints define visual references whose similarity combines with local BLIP-2 image-text relevance to form a semantic value map. LangGraph represents instruction parsing, geometric perception, semantic value updates, path planning, action execution, and failure recovery as a directed state graph with conditional transitions, persistent state, and modular recovery mechanisms. On a fixed 550-episode subset of the R2R-CE val-unseen split, LG-VLN achieves 21.3% success and 12.1% success weighted by path length. Ablations show shared semantic features improve navigation, further boosted by combining visual similarity and image-text relevance. Results establish shared visual representations and explicit state orchestration as effective for zero-shot VLN-CE using monocular RGB alone. Code will be publicly released for reproducibility.

</details>

#### 2026-09-10 - Visual-SLAM for the detection of hidden tomatoes in greenhouses by Hierarchical Localization and GLOMAPfor robotized harvesting

**Authors:** Fernando Cañadas-Aránega, José C. Moreno, José L. Blanco-Claraco, Francisco Rodríguez
**Links:** [abs](https://arxiv.org/abs/2609.11766) - [pdf](https://arxiv.org/pdf/2609.11766)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** structure from motion, SLAM, visual SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visual-SLAM for the detection of hidden tomatoes in greenhouses by Hierarchical Localization and GLOMAPfor robotized harvesting
- 作者：Fernando Cañadas-Aránega, José C. Moreno, José L. Blanco-Claraco, Francisco Rodríguez
- 出版日期：2026-09-10T16:19:36Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.11766 ；PDF https://arxiv.org/pdf/2609.11766

### 一句话总结
该工作提出一种面向温室番茄作物建图的低成本单目 Visual-SLAM 系统，结合 Hierarchical Localization 与基于 Structure-From-Motion 的 GLOMAP，实现对被遮挡番茄的识别与三维重建。

### 研究问题
温室内部先进的作物监测是研究中心的重点目标之一。传统上常使用 LiDAR 或立体相机等高性能传感器，但成本往往较高。论文关注的是：能否用成本显著更低的单目相机 Visual-SLAM 系统，面向农业应用（如温室番茄作物建图）完成检测与建图任务，尤其是识别被遮挡、经典视觉技术难以访问的番茄。

### 核心思路/方法
论文提出使用单目相机的 Visual-SLAM 系统，针对农业应用（温室番茄作物建图）定制。测试在 Agroconnect 实验温室的真实番茄串上进行。开发了一个 ROS 2 Humble 节点，运行在机器人上以采集作物图像，随后存储用于离线处理。为生成温室作物的三维建图模型，将基于 Structure-From-Motion 的 GLOMAP 建图器与 Hierarchical Localization 工具箱集成。系统采用基于由粗到细策略的分层定位范式：先进行全局检索以生成位置假设，再在识别出的候选区域内结合局部特征。

### 主要贡献
- 提出一种使用单目相机的 Visual-SLAM 系统，相比 LiDAR 或立体相机等方案成本显著更低，并面向农业应用定制。
- 将基于 Structure-From-Motion 的 GLOMAP 建图器与 Hierarchical Localization 工具箱集成，用于生成温室作物的三维建图模型。
- 采用由粗到细的分层定位范式：先全局检索生成位置假设，再在候选区域内结合局部特征。
- 开发 ROS 2 Humble 节点用于机器人端图像采集与离线处理。
- 结果显示能够正确识别番茄簇，并正确表征被经典视觉技术遮挡且不可访问的番茄。
- 重建的三维模型通过人工真值测量（果实大小、质心位置和朝向）进行了验证，确认了所提低成本单目流程的几何精度。

### 局限性
- 摘要未提供足够信息说明系统在更多温室场景、不同作物或更大规模环境中的泛化能力。
- 摘要未提供足够信息说明实时性能、计算资源消耗或在线运行能力。
- 摘要未提供足够信息说明与 LiDAR 或立体相机方案在精度、鲁棒性上的系统对比。
- 摘要未提供足够信息说明对光照变化、遮挡程度差异、相机运动等干扰因素的鲁棒性。
- 摘要未提供足够信息说明数据集规模、测试样本数量及统计显著性。
- 摘要仅提到该初始建图是未来更高级算法分析生长模式、优化农业管理的基础，因此面向机器人化采收的完整闭环能力在摘要中未提供足够信息。

### 阅读优先级
中。理由：该论文主题明确，聚焦低成本单目 Visual-SLAM 在温室番茄检测与三维重建中的应用，并涉及 Hierarchical Localization 与 GLOMAP 的集成，对农业机器人、三维重建和视觉定位方向有一定参考价值。但摘要未提供足够信息说明实验规模、实时性、泛化性和与高成本传感器的系统对比，若读者关注机器人化采收的完整系统或大规模验证，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Advanced crop monitoring inside greenhouses is becoming one of the primary objectives of research centers. High-performance sensors, such as LiDAR or stereo cameras, have traditionally been employed for this purpose, though these often have a high cost. This work proposes a Visual-SLAM system using a monocular camera, which is significantly more cost-effective and specifically tailored for agricultural applications, such as mapping tomato crops in a greenhouse. Tests were carried out on a real tomato bunch, located in the Agroconnect experimental greenhouse. A ROS 2 Humble node was developed to run on the robot in order to capture images of these crops, which were then stored for offline processing. To generate a 3D mapped model for the crop in the greenhouse, the GLOMAP mapper, based on Structure-From-Motion, was integrated with the Hierarchical Localization toolbox. This initial mapping is a foundation for future, more advanced algorithms to analyze growth patterns, and optimize agricultural management. The system leverages a hierarchical localization paradigm based on a coarse-to-fine strategy: it first performs global retrieval to generate location hypotheses, then combines local features within the identified candidate regions. The results show a correct identification of the tomato cluster, correctly characterising the tomato that is occluded and inaccessible by classical vision technologies. The reconstructed 3D model was further validated against manual ground-truth measurements of fruit size, centroid position, and orientation, confirming the geometric accuracy of the proposed low-cost monocular pipeline.

</details>

#### 2026-09-10 - RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting

**Authors:** Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen
**Links:** [abs](https://arxiv.org/abs/2609.11079) - [pdf](https://arxiv.org/pdf/2609.11079)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, depth estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, robot perception, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting
- 作者：Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen
- 出版日期：2026-09-10T04:36:58Z
- 分类：3D Reconstruction & Multi-view Geometry（主类别）；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次类别）
- 链接：摘要页 https://arxiv.org/abs/2609.11079 ；PDF https://arxiv.org/pdf/2609.11079

### 一句话总结
RIDE 利用 render–match–PnP 重定位中获得的稀疏度量深度观测，结合预训练视频深度模型的几何先验，从机器人 RGB 流中估计稠密度量深度。

### 研究问题
论文关注的是：render–match–PnP 重定位虽能建立查询图像像素与 3D 地图点之间的对应关系以恢复相机位姿，但其支持稠密深度估计的潜力常被忽视。RIDE 旨在利用这类几何信息，在给定度量尺度的 3D Gaussian Splatting（3DGS）模型条件下，从机器人 RGB 流中估计稠密度量深度。

### 核心思路/方法
- 以度量尺度的 3DGS 模型为基础，利用 PnP-RANSAC 内点对应关系导出稀疏度量深度观测。
- 将这些稀疏度量深度观测与预训练视频深度模型的几何先验相结合。
- 针对观测不均匀和间歇性的问题，引入全局与局部深度校正以及时间记忆机制。
- 在度量尺度初始化后，支持在短观测间隔内继续进行深度估计。
- 在公开 RGB-D 视频上训练，并在机器人序列上不做微调进行评估。

### 主要贡献
- 提出 RIDE，将重定位几何信息用于稠密度量深度估计。
- 结合 PnP-RANSAC 内点对应得到的稀疏度量深度与预训练视频深度模型的几何先验。
- 通过全局/局部深度校正与时间记忆，应对不均匀、间歇的稀疏观测，并支持短观测间隔下的深度估计。
- 实验显示，相比仅做尺度校准，RIDE 在深度精度和时间一致性上有所提升，表明定位几何可同时支持位姿恢复与稠密机器人感知。

### 局限性
摘要未提供足够信息。摘要未给出具体实验平台、序列数量、失败情形、计算开销、实时性、对 3DGS 模型质量或重定位成功率的依赖程度等细节。

### 阅读优先级
中。理由：该工作位于 3D 重建、神经场景表示与机器人/AR 应用的交叉点，核心思路明确，且强调无需微调即可在机器人序列上评估；但摘要未提供充分的实验细节与对比设置，是否值得精读取决于读者对重定位辅助稠密深度估计、3DGS 机器人感知这一具体方向的关注程度。

</details>

<details>
<summary>Abstract</summary>

Render--match--PnP relocalization establishes correspondences between query image pixels and 3D map points for camera pose recovery, but their potential to support dense depth estimation is often overlooked. To exploit this geometric information, we present RIDE, which estimates dense metric depth from a robot's RGB stream. Given a metrically scaled 3D Gaussian Splatting (3DGS) model, RIDE combines sparse metric depth observations derived from PnP-RANSAC inlier correspondences with the geometric prior of a pretrained video-depth model. To handle uneven and intermittent observations, it integrates global and local depth correction with temporal memory, supporting depth estimation through short observation gaps after metric scale initialization. Trained on public RGB-D videos, RIDE is evaluated on robot sequences without fine tuning. Experiments show improved depth accuracy and temporal consistency over scale-only calibration, demonstrating how localization geometry can support both pose recovery and dense robot perception.

</details>

#### 2026-09-09 - GRADE: Single-Frame Generative Radar Depth Estimation Under Visual Degradation

**Authors:** Bin Zhao, Patrick Chiou, Nakul Garg
**Links:** [abs](https://arxiv.org/abs/2609.10756) - [pdf](https://arxiv.org/pdf/2609.10756)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GRADE: Single-Frame Generative Radar Depth Estimation Under Visual Degradation
- 作者：Bin Zhao, Patrick Chiou, Nakul Garg
- 出版日期：2026-09-09T18:57:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.10756

### 一句话总结
GRADE 将预训练生成先验与单帧雷达几何相融合，在烟雾、雾气和黑暗等视觉退化条件下实现高保真度量深度估计。

### 研究问题
在烟雾、雾气和黑暗等条件下，光学传感器无法穿透空气中的颗粒物，导致密集 3D 深度感知失效。毫米波雷达在这些条件下仍可使用并能准确测距，但其小孔径限制了角分辨率。论文旨在解决：如何在视觉退化条件下，利用单帧雷达几何与生成先验估计高保真度量深度。

### 核心思路/方法
GRADE 首先将原始 4D 雷达频谱映射为粗略的度量深度。随后，一个潜在扩散骨干网络在恢复结构细节的同时，将每个去噪步骤都条件化在该深度估计上。一个像素空间适配器在有可用信息时利用残余相机线索，并在清晰、烟雾退化和遮挡输入上进行训练，使得随着能见度下降，整体输出趋近于雷达条件化路径。

### 主要贡献
- 提出 GRADE，将预训练生成先验锚定在单帧雷达几何中，用于估计高保真度量深度。
- 设计了两阶段方法：先将原始 4D 雷达频谱映射为粗略度量深度，再通过潜在扩散骨干网络恢复结构细节并条件化每一去噪步骤。
- 引入像素空间适配器，利用残余相机线索，并在清晰、烟雾退化和遮挡输入上训练，使输出随能见度下降趋近雷达条件化路径。
- 在 12 栋建筑约 95K 帧（含真实烟雾）上训练与评估，清晰场景 MAE 为 0.303 m，烟雾下为 0.313 m，优于现有基线。
- 代码与数据集已公开。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对视觉退化条件下的深度感知这一明确难题，结合雷达与生成先验，给出了具体量化结果，且涉及 3D 重建与多视角几何方向，摘要信息显示其方法路径与评估结果较为完整，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Dense 3D depth perception fails under smoke, fog, and darkness because optical sensors cannot penetrate airborne particulates. mmWave radar remains usable and measures range accurately under these conditions, but its small aperture limits angular resolution. We present GRADE, which grounds a pretrained generative prior in single-frame radar geometry to estimate high-fidelity metric depth. GRADE first maps raw 4D radar spectra to coarse metric depth. A latent diffusion backbone then recovers structural detail while conditioning every denoising step on this estimate. A pixel-space adapter uses residual camera cues when available and is trained across clear, smoke-degraded, and occluded inputs so the full output approaches the radar-conditioned path as visibility degrades. Trained and evaluated on ~95K frames across 12 buildings with real smoke, GRADE achieves an MAE of 0.303 m in clear scenes and 0.313 m under smoke, outperforming existing baselines. Code and datasets are available at https://phi-lab-rice.github.io/GRADE.

</details>

#### 2026-09-09 - Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts

**Authors:** Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte
**Links:** [abs](https://arxiv.org/abs/2609.10498) - [pdf](https://arxiv.org/pdf/2609.10498)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts
- 作者：Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte
- 出版日期：2026-09-09T17:35:16Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.10498) / [PDF](https://arxiv.org/pdf/2609.10498)

### 一句话总结
该论文提出 Field Converter，通过相机与球场几何初始化球员根节点，并利用时序残差修正，实现从已标定足球转播中估计共享世界坐标系下的 3D 球员姿态。

### 研究问题
从单目体育转播中恢复 3D 人体姿态时，难点不仅在于相对自身身体的姿态重建，还在于需要将球员定位到共享的度量世界坐标系中。论文聚焦于从已标定的足球转播视频中进行世界坐标下的 3D 球员姿态估计。

### 核心思路/方法
- 使用相机和球场几何信息，通过射线-地面相交来初始化球员根节点。
- 在几何初始化基础上，预测时序残差修正。
- 残差预测使用姿态、图像、相机和几何线索。
- 在匹配不重叠的评估序列上，比较了不同时序骨干：逐帧 MLP、TCN 和 Transformer。

### 主要贡献
- 提出 Field Converter，一个几何初始化与时序残差修正结合的世界坐标 3D 球员姿态估计框架。
- 利用相机和球场几何进行根节点初始化，并通过时序残差修正降低根节点误差。
- 报告中，几何单独使根误差为 49cm，逐帧 MLP 降至 14cm，TCN 降至 10cm，Transformer 达到可比的 11cm；世界空间 MPJPE 达到 13.2cm。
- 消融显示，残差预测明显优于直接全局根节点回归；时序上下文比具体时序骨干更重要。
- 失败分析指出，空中动作是基于地面几何初始化的主要局限。

### 局限性
- 摘要明确指出失败分析发现空中动作是基于地面几何初始化的主要限制。
- 除空中动作外，其他局限性摘要未提供足够信息。
- 实验细节、数据集规模、跨场景泛化能力、计算成本等信息摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对足球转播中的世界坐标 3D 人体姿态估计，问题设定明确，且给出了根误差、MPJPE 和消融结论；如果关注体育视频分析、单目 3D 人体姿态或几何初始化方法，具有参考价值。但摘要未提供完整实验设置、数据规模和更广泛的泛化分析，是否高优先级取决于读者对足球转播场景的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Recovering 3D human pose from monocular sports broadcasts remains challenging when players must be localized in a shared metric world coordinate system rather than only reconstructed relative to their own body. We introduce Field Converter, a geometry-initialized temporal residual framework for world-grounded 3D player pose estimation from calibrated soccer broadcasts. Our method first uses camera and pitch geometry to initialize the player root through ray-ground intersection, then predicts a temporal residual correction from pose, image, camera, and geometric cues. On match-disjoint evaluation sequences, residual refinement reduces root error from 49cm with geometry alone to 14cm with a frame-wise MLP and 10cm with a TCN, while a Transformer achieves a comparable 11cm. The resulting world-space MPJPE reaches 13.2cm, and ablations show that residual prediction clearly outperforms direct global-root regression while temporal context matters more than the specific temporal backbone. Failure analysis further identifies airborne motion as the main limitation of the ground-based geometric initialization.

</details>

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-15 - ORCA: Occlusion-Aware Refinement and Completion for Novel View Synthesis

**Authors:** Weronika Jakubowska, Maciej Zięba, Przemysław Spurek
**Links:** [abs](https://arxiv.org/abs/2609.17450) - [pdf](https://arxiv.org/pdf/2609.17450)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** monocular depth, novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Novel-view synthesis from a single image is a fundamentally ambiguous problem. As the camera moves away from the input viewpoint, previously hidden regions become visible, exposing missing geometry and holes in the reconstructed scene. Existing methods often rely on generative models to complete such regions. However, many of these artifacts are small gaps near depth boundaries and do not require generating new scene content. In order to eliminate expensive process of generating image we introduce ORCA, an occlusion-aware method for reconstructing and completing explorable 3D scenes from a single image. ORCA first introduces 3D structure into a Gaussian-anchor representation using monocular depth while preserving the original camera-ray correspondence. During scene exploration, missing regions are handled based on their size and structure. Small disocclusions are repaired using RGB-D information already available in the reconstruction, while generative inpainting is reserved for larger regions that cannot be reliably recovered from the scene. New Gaussian anchors are added and optimized locally without modifying the existing representation. By reducing unnecessary reliance on generative inpainting, ORCA limits generation-induced hallucinations and better preserves the content and structure of the original scene. On DIV2K, ORCA improves novel-view quality over VistaDream across all reported metrics, increasing MUSIQ from 61.60 to 68.71 and CLIP-IQA from 0.474 to 0.574. These results show that many novel-view artifacts can be repaired effectively by reusing information already present in the reconstructed scene.

</details>

#### 2026-09-15 - PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM

**Authors:** Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang
**Links:** [abs](https://arxiv.org/abs/2609.17387) - [pdf](https://arxiv.org/pdf/2609.17387)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, differentiable rendering, rendering, splatting, robotics, mapping, localization

<details>
<summary>Abstract</summary>

Real-time dense SLAM is a core capability for robotics applications that require robust localization and high- quality mapping in dynamic or fast-changing environments. Recent 3D Gaussian Splatting (3DGS)-based SLAM methods have shown promising performance, but most are designed for narrow-FoV pinhole cameras, where limited angular coverage weakens pose observability and often leads to unstable photo- metric optimization under rapid motion and large viewpoint changes. We present PanoGS-SLAM, the first panoramic dense SLAM system built on 3D Gaussian Splatting. Our method per- forms differentiable rendering and pose optimization directly in the spherical domain, enabling omnidirectional photometric constraints for more stable tracking. To improve geometric consistency and robustness, we introduce (1) a sphere-consistent photometric loss that compensates for the area distortion of equirectangular projection, and (2) a depth-guided Gaussian initialization strategy that stabilizes incremental mapping in newly observed regions. Extensive experiments on both real and synthetic panoramic benchmarks (PALVIO and SynPano) show that PanoGS-SLAM consistently outperforms geometric and GS-based baselines in tracking accuracy and rendering quality, while achieving fast front-end convergence and real-time perfor- mance. In addition, controlled field-of-view experiments reveal a clear monotonic improvement in optimization conditioning and convergence stability as angular coverage increases, high- lighting the fundamental role of sensing geometry in shaping the optimization landscape of differentiable Gaussian-based SLAM. The source code will be made publicly available.

</details>

#### 2026-09-15 - Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement

**Authors:** Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo
**Links:** [abs](https://arxiv.org/abs/2609.17039) - [pdf](https://arxiv.org/pdf/2609.17039)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Sparse-view 3D scene reconstruction with 3D Gaussian Splatting (3DGS) is inherently underconstrained. Plausible renderings can also coexist with erroneous Gaussian geometry, as errors in positions or depths may be concealed by opacity, scale, and appearance; we term this failure mode Geometry Cheating. Existing regularization methods constrain geometry but remain limited to observed views, while video-diffusion-based methods complete unseen views yet mainly use them as RGB pseudo-supervision, underusing motion and temporal priors and lacking explicit geometry supervision. We present Bi-FlowGS, which uses optical flow to bridge generative view completion and Gaussian geometry regularization. Our plug-and-play Video-to-Geometry Flow Distillation (V2G) distills temporal correspondence priors from restored videos into Gaussian geometry to alleviate Geometry Cheating. Conversely, Geometry-to-Video Flow-Guided Restoration (G2V) uses the current 3DGS geometry to guide temporally consistent video restoration, providing more reliable generative supervision. Together, V2G and G2V form an implicit bidirectional co-refinement process, enabling restored videos and the optimized 3DGS scene to iteratively improve each other. Experiments demonstrate improved rendering quality and geometric consistency across wide-baseline and unbounded 360° benchmarks.

</details>

#### 2026-09-14 - The Neverwhere Visual Parkour Benchmark Suite

**Authors:** Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang
**Links:** [abs](https://arxiv.org/abs/2609.16443) - [pdf](https://arxiv.org/pdf/2609.16443)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

State-of-the-art visual locomotion controllers are increasingly capable at handling complex visual environments, making evaluating their real-world performance before deployment increasingly difficult. This work intends to narrow this train/evaluation gap by developing a collection of hyper-photo-realistic, closed-loop evaluation environments - The Neverwhere Benchmark Suite - comprised of over sixty 3D Gaussian Splatting reconstructions of urban indoor and outdoor scenes. Our goal is to encourage large-scale and reproducible robot evaluation by making it easier to create and integrate Gaussian splats-based reconstructions into simulated continuous testing setups. We also underscore the potential pitfalls of relying exclusively on 3D Gaussian-generated data for training, by providing policy checkpoints trained over multiple Neverwhere scenes and their performance when evaluated in novel scenes. Our analysis illustrates the necessity of sourcing diverse data to ensure performance. Code and data are available on the project page: https://ziyc.github.io/neverwhere-bench/.

</details>

#### 2026-09-14 - G-ray: Ray-Level Relative Geometric Position Encoding in Multi-View Vision Transformers under Camera Heterogeneity

**Authors:** Shuo Zhang, Xin Su, Wei Wang, Jun Liu, Xinrui Zeng, Yongsen Chen, Chenjie Wang, Guibo Zhu, Jinqiao Wang, Bin Luo, Liangpei Zhang
**Links:** [abs](https://arxiv.org/abs/2609.15018) - [pdf](https://arxiv.org/pdf/2609.15018)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** pointmap, 3D reconstruction, novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

We study relative position encoding for multi-view vision Transformers under camera heterogeneity, including varying fields of view (FoVs) or projection models. Existing rotary relative position encodings commonly use image-plane positional coordinates, producing projection-dependent relative phases and inconsistent geometric cues for cross-projection attention. We introduce G-ray, a ray-level relative position encoding whose rotary phases are parameterized by camera-local ray angles. The same camera-local ray pair induces the same relative phase across projections, providing projection-invariant positional consistency. G-ray can be used directly or integrated with existing encodings, retaining complementary geometric cues without additional learned parameters. We validate G-ray in three host encodings, RoPE, GTA, and RayRoPE, across 3D reconstruction and novel-view synthesis (NVS). Across three heterogeneous 3D reconstruction benchmarks at 50 views, G-ray leads all six averaged metrics and reduces mean pointmap relative error by 45.8% over MapAnything, with calibration supplied to both. Trained exclusively on homogeneous pinhole images, the 3D reconstruction model handles mixed pinhole and non-pinhole inputs without retraining and remains competitive on homogeneous pinhole 3D reconstruction protocols. For NVS, GTA and RayRoPE improve with G-ray under joint viewpoint and FoV variation. The project's webpage is available at https://g-ray-project.github.io/.

</details>

#### 2026-09-14 - HydroMap: Probabilistic Water Surface Elevation Mapping for Semantic Scene Representation in Inland Waterways

**Authors:** Zhongbi Luo, Yunjia Wang, Herman Bruyninckx, Peter Slaets
**Links:** [abs](https://arxiv.org/abs/2609.14903) - [pdf](https://arxiv.org/pdf/2609.14903)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, scene representation, mapping, localization

<details>
<summary>Abstract</summary>

Autonomous surface vehicles operating in inland waterways require a persistent representation of both surrounding structures and the water surface. LiDAR-based simultaneous localization and mapping often produces sparse or missing water returns, leaving this operational surface absent from the reconstructed scene. We propose HydroMap, an odometry-decoupled framework that reconstructs water surface elevation from stereo observations and integrates it with the structural map. Per-frame water points form joint cell observations with propagated stereo and pose uncertainty, and successive observations are fused into a persistent probabilistic elevation map. Semantic map conversion then combines the elevation map with structural geometry in a unified 2.5D representation of water, boundaries, structures, and overhead regions. On the Pohang Canal and Leuven Vaart datasets, the elevation RMSE remains below 5 cm relative to LiDAR references expressed in the same map frame. The elevation and semantic maps are published at 2 Hz and 1 Hz, respectively. HydroMap thereby complements LiDAR maps with a persistent representation of the water surface for downstream navigation in inland waterways.

</details>

#### 2026-09-14 - What Makes a 3D Scene Editable? A Factorized Benchmark of Fidelity, Locality, Consistency, and Preservation

**Authors:** Sariah Patro, Arjun Mehra, Nikhil Bhatia
**Links:** [abs](https://arxiv.org/abs/2609.14899) - [pdf](https://arxiv.org/pdf/2609.14899)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, splatting, manipulation

<details>
<summary>Abstract</summary>

Neural 3D scene editing is often evaluated by semantic alignment alone, although a convincing result may alter unrelated content or become inconsistent across views. We introduce EditBench3D, a representation-agnostic benchmark that treats editing as controlled information replacement. It evaluates four complementary properties: instruction fidelity, spatial locality, cross-view consistency, and preservation of non-target content. The protocol combines visibility-aware 3D target supports, paired descriptions, held-out cameras, and five edit families covering appearance, material, geometry, and object-level changes. We evaluate eight representative NeRF, 3D Gaussian Splatting, hybrid, and proxy-based editors on 240 scene-edit pairs. The study shows that semantic fidelity is only weakly associated with the other editing properties, and that no single method is optimal across all dimensions. Explicit Gaussian editors offer a strong overall balance, whereas direct proxy manipulation provides the most conservative edits at the cost of open-ended fidelity. These findings support reporting editability as a multi-objective profile rather than a single semantic score.

</details>

#### 2026-09-13 - Gaussian Process Implicit Surfaces as Participating Media: Realization-Free Rendering from Level-Crossing Statistics

**Authors:** Jack Cui, Kehan Xu, Eugene d'Eon, Wojciech Jarosz
**Links:** [abs](https://arxiv.org/abs/2609.14695) - [pdf](https://arxiv.org/pdf/2609.14695)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, rendering, radiance

<details>
<summary>Abstract</summary>

We present a theory of light scattering that connects Gaussian Process Implicit Surfaces (GPISes) and participating media in both directions. Applying the Kac--Rice level-crossing formula under a local-conditioning approximation yields a complete anisotropic radiative transfer equation (RTE) directly from pointwise GPIS statistics. A shared projected area couples extinction and scattering, ensuring geometric consistency between the GPIS and its volumetric representation. The framework spans rough surfaces, porous and non-height-field geometries, and participating media. From the same statistical structure, we derive full-sphere Beckmann and GGX normal distribution functions supporting in-plane and out-of-plane anisotropy. These families provably recover SGGX, Beckmann, and GGX as special cases and admit exact visible-normal importance sampling. We also derive analytic masking--shadowing functions and single-scattering surface models for specular microsurfaces, with extensions to multiple scattering. In the height-field limit, we prove that the local-conditioning approximation reduces to Smith's independence assumption. Our realization-free approach improves rendering efficiency over realization-based methods and can be implemented within a standard volume renderer. In the inverse direction, we characterize families of GPISes corresponding to compatible RTE parameters and develop practical lifts for heterogeneous density fields. Existing volumetric assets thereby become renderable as GPISes, while trained radiance-field reconstructions yield surface geometry and shading normals without mesh extraction and provide a density-based representation of geometric uncertainty.

</details>

#### 2026-09-10 - 3D Point Splatting for mmWave Radar Novel View Synthesis

**Authors:** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar
**Links:** [abs](https://arxiv.org/abs/2609.11894) - [pdf](https://arxiv.org/pdf/2609.11894)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D Point Splatting for mmWave Radar Novel View Synthesis
- 作者：Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar
- 出版日期：2026-09-10T17:52:17Z
- 分类：Neural Scene Representations & Rendering（主分类）；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2609.11894 ；PDF https://arxiv.org/pdf/2609.11894

### 一句话总结
论文提出 3DPS——首个面向毫米波雷达的可微点渲染器，直接从雷达方程立体角形式推导，以复数相位输出实现与格式无关的新视角合成，在保持物理保真度的同时将训练时间压缩到单卡约 3 分钟/场景。

### 研究问题
毫米波雷达新视角合成（NVS）需要一个同时满足三个性质的渲染器：物理忠实、复数值、多视角可优化。摘要指出此前没有方法能同时具备这三点：
- 可微蒙特卡洛（MC）光线追踪器直接实现雷达前向模型，具有显式材质建模和复数输出，但无法扩展到 NVS 所需的多视角优化规模；
- 从光学 NVS 移植的 NeRF、哈希网格和 3D 高斯训练快，但丢弃了相位，并以不透明的学习特征替代显式材质建模，因此只限于功率域的距离-方位（RA）幅度。

### 核心思路/方法
- 从雷达方程的标准立体角形式直接推导出可微点渲染器 3DPS。
- 每个有向 3D 点携带 ITU-R P.2040 材质模型，并以闭式求值。
- 将得到的复数相量通过预计算的点扩散函数（PSF）splat 到距离单元中。
- 复数输出使渲染器与下游输出格式无关：同一个优化后的场景可通过标准 FFT 流水线产出 ADC、复数距离剖面（CRP）和 RA 输出，无需针对每种格式重新训练。

### 主要贡献
- 提出 3DPS，据摘要所述为首个面向雷达的可微点渲染器。
- 从雷达方程立体角形式直接推导，赋予渲染器物理忠实性。
- 通过 ITU-R P.2040 材质模型与闭式复数相量计算，兼顾显式材质建模与复数输出。
- 借助复数输出实现格式无关性，一套优化场景即可支持 ADC、CRP、RA 多种输出。
- 在六个户外 ColoRadar 场景上，持出 RA 图像达到 0.587 的平均皮尔逊相关，为三个光学 NVS 基线（RadarSplat、Radar Fields、DART）的 1.7 倍至 5.2 倍；单张 RTX 4090 上每场景训练约 3 分钟。

### 局限性
- 摘要未提供足够信息说明方法在非户外场景、其他雷达频段或不同硬件条件下的泛化表现。
- 摘要未提供足够信息说明 3DPS 在 ADC、CRP 输出上的定量评估结果，仅给出 RA 图像的皮尔逊相关指标。
- 摘要未提供足够信息说明与 MC 光线追踪器在物理保真度上的直接定量对比。
- 摘要未提供足够信息说明多视角优化中视角数量、稀疏度或场景规模对性能的影响。
- 摘要未提供足够信息说明 0.587 平均皮尔逊相关的方差、逐场景分布或失败案例。
- 摘要未提供足够信息说明材质模型参数是否可学习、初始化方式或对 ITU-R P.2040 假设的敏感性。

### 阅读优先级
中。理由：雷达 NVS 属于相对专门的方向，但该工作提出的“物理忠实 + 复数 + 多视角可训练”三性合一问题定位清晰，且报告了显著的相对基线提升与极短训练时间；若关注可微渲染、雷达感知或 NeRF/3D 高斯之外的非光学传感器 NVS，则值得优先阅读。由于摘要未给出代码、完整实验设置与 ADC/CRP 定量结果，是否精读可待正文确认。

</details>

<details>
<summary>Abstract</summary>

Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-view optimization NVS demands. Optical-NVS ports of NeRF, hash grids, and 3D Gaussians train fast but discard phase and replace explicit material modeling with opaque learned features, restricting them to power-only range-azimuth (RA) magnitudes. We propose 3D Point Splatting (3DPS), the first differentiable point renderer for radar, derived directly from the standard solid-angle form of the radar equation. Each oriented 3D point carries an ITU-R P.2040 material model, evaluated in closed form, with the resulting complex phasor splatted into range bins through a precomputed point spread function (PSF). The complex-valued output makes the renderer product-agnostic. The same optimized scene yields analog-to-digital converter (ADC), complex range profile (CRP), and RA outputs through standard fast Fourier transform (FFT) pipelines without retraining for each format. On six outdoor ColoRadar scenes, 3DPS reaches 0.587 mean Pearson correlation on held-out RA images. This is between 1.7x and 5.2x the three optical-NVS baselines (RadarSplat, Radar Fields, DART). Training takes approximately 3 minutes per scene on a single RTX 4090.

</details>

#### 2026-09-10 - Hologram Representation via Quadratic Phase Gaussian Splatting

**Authors:** Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu
**Links:** [abs](https://arxiv.org/abs/2609.11434) - [pdf](https://arxiv.org/pdf/2609.11434)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hologram Representation via Quadratic Phase Gaussian Splatting
- 作者：Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu
- 出版日期：2026-09-10T12:06:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.11434) / [PDF](https://arxiv.org/pdf/2609.11434)

### 一句话总结
该论文提出复数域二次相位高斯（CVQPG），用可学习的二维二次相位函数替代 2D Gaussian Splatting 中的标准二维高斯表示，以提升全息重建的视觉质量。

### 研究问题
如何改进全息图表示方法，使其在重建质量上优于现有先进方法，同时保持参数高效。摘要指出，作者希望验证“调制基元的波前”是否是一种有效且轻量的全息表示增强方式。

### 核心思路/方法
- 提出 Complex-Valued Quadratic Phase Gaussian (CVQPG)。
- 将 2D Gaussian Splatting 中使用的标准二维高斯表示替换为二维二次相位函数。
- 引入额外可学习参数，用于控制这些基元的曲率。
- 通过等参数数量评估，比较该方法与现有先进方法在全息重建中的表现。
- 进行频域分析，观察自然图像中高频与中高频段的保留情况。

### 主要贡献
- 提出 CVQPG，一种新的全息图表示方法，核心是用二维二次相位函数替代标准二维高斯基元。
- 在等参数数量评估中，表明调制基元波前可作为全息表示的有效且轻量增强。
- 在全息重建视觉质量上平均超过现有先进方法：RGB 提升 +0.19 dB，灰度提升 +0.33 dB。
- 频域分析显示，CVQPG 成功保留了自然图像的中高频段。

### 局限性
摘要未提供足够信息。未说明计算开销、训练时间、数据集规模、泛化能力、硬件依赖性、失败案例或与其他表示方法的全面比较。等参数数量评估之外的其他实验设置也未在摘要中给出。

### 阅读优先级
中。理由：该工作与神经场景表示、Gaussian Splatting 和全息显示相关，提出的二次相位基元替代思路较直接，且摘要给出了明确的定量提升和频域分析；但摘要未披露数据集、实现细节和完整实验设置，是否具有广泛适用性需阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

We introduce Complex-Valued Quadratic Phase Gaussian (CVQPG), a novel hologram representation method that replaces standard 2D Gaussian representations used in 2D Gaussian Splatting with 2D quadratic phase functions. CVQPG incorporates additional learnable parameters to control the curvature of these bases. We evaluate our approach against state-of-the-art methods, exceeding the visual quality by +0.19 dB (RGB) and +0.33 dB (grayscale) on average in holographic reconstructions. Specifically, our equal parameter count evaluations show that modulating the primitive's wavefront is an effective and lightweight enhancement for hologram representations. In addition, our frequency domain analysis illustrates that CVQPG has successfully preserved the mid-to-high frequency band of natural images.

</details>

#### 2026-09-10 - Tri-DehazeGS: Scene--Medium Decoupled Gaussian Splatting with Transmittance-Aware Optimization

**Authors:** Kui Jiang, Yang Gu, Jiacheng Liu, Shiyu Liu, Youyu Chen, Hui Liu
**Links:** [abs](https://arxiv.org/abs/2609.11223) - [pdf](https://arxiv.org/pdf/2609.11223)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tri-DehazeGS: Scene--Medium Decoupled Gaussian Splatting with Transmittance-Aware Optimization
- 作者：Kui Jiang, Yang Gu, Jiacheng Liu, Shiyu Liu, Youyu Chen, Hui Liu
- 出版日期：2026-09-10T08:24:16Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.11223

### 一句话总结
Tri-DehazeGS 提出一种场景—介质解耦的高斯泼溅框架，用独立视图共享三平面场建模参与介质，并通过透射率梯度补偿优化低透射区域，以改善雾天多视角图像下的干净新视角重建。

### 研究问题
从有雾多视角图像中恢复干净三维场景具有挑战性，因为雾会衰减场景辐射并引入大气散射。现有散射感知高斯泼溅方法虽引入物理雾模型，但常在图像空间施加退化，或把介质相关变量绑定到高斯基元上，导致干净场景辐射与大气效应相互纠缠；同时低透射率区域对高斯优化提供的监督较弱，使远处或浓雾区域重建不足。

### 核心思路/方法
论文认为雾下干净重建需要同时实现场景—介质解耦与透射率感知的优化重平衡。为此提出 Tri-DehazeGS：
- 用高斯基元表示干净场景；
- 用独立的视图共享三平面场建模参与介质；
- 通过物理散射模型合成有雾观测。
此外引入 Medium-Decoupled Transmittance Gradient Compensation（MD-TGC），在介质冻结后补偿被雾抑制的梯度，且不改变前向渲染。

### 主要贡献
- 提出 Tri-DehazeGS，一个场景—介质解耦的高斯泼溅框架，将干净场景与参与介质分别表示并依据物理散射模型组合。
- 引入 MD-TGC，在介质冻结后补偿雾抑制的梯度，以重平衡低透射率区域的优化。
- 在真实与合成雾基准上实验显示，Tri-DehazeGS 改善了干净新视角重建，并提供代码链接。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算开销、对极端天气或动态场景的适用性，也未给出定量指标、消融细节或与基线方法的完整对比。

### 阅读优先级
高。理由：该论文针对雾天三维重建中场景与介质纠缠、低透射率区域监督不足两个明确问题，提出解耦表示与梯度补偿机制，属于神经场景表示与渲染方向中物理模型与高斯泼溅结合的前沿工作，且提供代码，便于复现与后续研究。

</details>

<details>
<summary>Abstract</summary>

Recovering clean 3D scenes from hazy multi-view images is challenging because haze attenuates scene radiance and introduces atmospheric scattering. Recent scattering-aware Gaussian Splatting methods introduce physical haze models into reconstruction, but they often apply degradation in image space or bind medium-related variables to Gaussian primitives, which can entangle clean scene radiance with atmospheric effects. Moreover, low-transmittance regions provide weakened supervision for Gaussian optimization, causing distant or dense-haze areas to be under-reconstructed. We argue that clean reconstruction under haze requires both scene--medium disentanglement and transmittance-aware optimization rebalancing. To this end, we propose Tri-DehazeGS, a scene--medium decoupled Gaussian Splatting framework. It represents the clean scene with Gaussian primitives, models the participating medium using an independent view-shared tri-plane field, and composes hazy observations through a physical scattering model. We further introduce Medium-Decoupled Transmittance Gradient Compensation (MD-TGC), which compensates haze-suppressed gradients after medium freezing without altering forward rendering. Experiments on real and synthetic haze benchmarks show that Tri-DehazeGS improves clean novel-view reconstruction. Code is available at https://github.com/aptx46/Tri-DehazeGS.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-15 - SWIM: Vision-Language-Grounded Soft Whole-Body Interactive Manipulation

**Authors:** Tingcong Liu, Aye Phyu Phyu Aung, Junjie Xiong, Siyi Ma, Bo An, Ke Wu, Senthilnath Jayavelu
**Links:** [abs](https://arxiv.org/abs/2609.17035) - [pdf](https://arxiv.org/pdf/2609.17035)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Soft and continuum robots enable manipulation through distributed body deformation and contact, yet translating language and visual context into executable whole-body actuation remains a fundamental challenge. We present SWIM, a framework that maps an initial RGB observation and a language instruction to a complete actuation-command sequence. Its vision-language-action (VLA) policy, SWIM-VLA, combines a diffusion action head with Visual Soft Proprioception (VSP) through a shared representation of RGB observations, language instructions, and tendon states. The diffusion head models conditional distributions of expert command chunks, while VSP supervises ordered body-anchor predictions using simulation ground truth, encouraging the representation to retain body geometry when learning from limited demonstrations. Embodied mechanical intelligence supports physical execution of command sequences generated through iterative virtual rollout from evolving simulated observations, with intrinsic compliance providing local contact adaptation without online policy queries. We evaluate SWIM on packing, reaching, and grasping on a planar tendon-driven soft robot, with grasping targets anchored. In simulation, SWIM-VLA achieves success rates of 100\%, 96\%, and 88\%, respectively, outperforming an adapted OpenVLA-OFT baseline and controlled ablations. On hardware, SWIM achieves success rates of 100\%, 80\%, and 75\%, compared with 75\%, 40\%, and 25\% for direct online deployment of the same policy checkpoint.

</details>

#### 2026-09-15 - NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving

**Authors:** Muhammad Ahmed Ullah Khan, Mohammed Elamine, Sheikh Talha Uddin, Didier Stricker, Sk Aziz Ali, Muhammad Zeshan Afzal
**Links:** [abs](https://arxiv.org/abs/2609.16919) - [pdf](https://arxiv.org/pdf/2609.16919)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, scene understanding

<details>
<summary>Abstract</summary>

This paper introduces NeuroSymbEAD, a large-scale neuro-symbolic caption dataset featuring an ego-centric knowledge graph (KG) of static and dynamic objects annotated with classes, categories, heading directions, orientations, and distances from the ego-vehicle. These annotations are used on the KITTI-360 dataset to generate multilevel textual captions representing a lightweight version of an ego-centric scene map. Outdoor scene-map reconstruction, visual recognition, and object grounding establish baselines for driving common sense and traffic/scene understanding. For these purposes, natural language-based grounded captioning of objects and their complex relationships is a widely adopted contextual representation for indoor scene tasks. Neuro-symbolic representations have proven effective in handling structured information for various computer vision and language applications. Our data annotation pipeline allows the generation of varied map segments, populating simulated or real objects within the bounding boxes predicted by any 3D object detection network, and building hierarchical text captions. We benchmark our neuro-symbolic and ontological caption generation using pre-trained grounding and learned auto-regressive captioning networks. By converting 3D driving scenes into structured ego-centric language, NeuroSymbEAD provides a benchmark for vision-language and foundation models for traffic-scene explanation, 3D reasoning, and interpretable autonomous-driving perception.

</details>

#### 2026-09-15 - Seeing What Matters: Visual Cue Guided Video Planning for Generalizable Robot Navigation

**Authors:** Hojin Lee, Sizhe Lester Li, Maximilian Hilger, Susie Lu, Achim J. Lilienthal, Vincent Sitzmann, Daniel A. Duecker
**Links:** [abs](https://arxiv.org/abs/2609.16737) - [pdf](https://arxiv.org/pdf/2609.16737)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, robot navigation

<details>
<summary>Abstract</summary>

Generative video models can serve as a promising backbone for robot navigation by predicting future observations as video plans. Recent approaches often condition video planning on short-horizon guidance and recover geometric waypoints through scene reconstruction, leaving longer-horizon planning and precise video-to-action translation less explored. We present CueNav, a video model-based navigation framework combining visual cue guided video planning with an embodiment-specific Inverse-Dynamics Model (IDM). As visual cues, we use a Bird's-Eye View (BEV) map to convey global task context and retain part of the robot body in the egocentric observation to expose embodiment context. These cues guide the video planner, while the IDM translates dense flow fields extracted from the video plan into robot actions. With the visual cue encoding global task context, CueNav achieves nearly 2x higher success in maze navigation than planning without the cue. The body-aware view with the IDM enables precise navigation with 70% success in a narrow passage where comparison methods largely fail to complete the task. We further demonstrate zero-shot semantic-conditioned navigation and deployment of the same video planner across different robot platforms. Our results show that visual cue-guided video planning with embodiment-specific action grounding paves the way toward a generalizable navigation framework for longer-horizon planning and embodiment-aware control. Additional results and code are available on our project website: https://cuenav.github.io.

</details>

#### 2026-09-15 - CorrRisk-WM: Corridor-Conditioned Risk World Modeling for Safety-Critical Trajectory Planning

**Authors:** Tingyu Guo, Reza Langari
**Links:** [abs](https://arxiv.org/abs/2609.16724) - [pdf](https://arxiv.org/pdf/2609.16724)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reasoning, world model, world modeling

<details>
<summary>Abstract</summary>

Safe local planning requires forecasting surrounding-agent motion and evaluating candidate-specific risks, since identical agent motion can pose different risks to different ego trajectories. We present CorrRisk-WM, a planning-oriented partial world model coupling environment evolution with supervised intrusion and near-miss prediction over bounded candidate-trajectory corridors. A latent environment model recursively predicts agent states and updates agent-agent and agent-map interactions. Each candidate queries the evolving environment through footprint- aware geometry and learned agent-corridor representations. A lightweight recurrent risk module uses temporal context to estimate per-slice hazards; survival aggregation yields first-entry and horizon-level event probabilities. On 29,176 scenarios from 100 Waymo validation shards, CorrRisk-WM achieves intrusion average precision (AP) of 0.8567 and 1-m near-miss first-entry AP of 0.8671. In baseline comparisons, it attains the highest near-miss AP at all three distance thresholds and the lowest observed open-loop collision rate (4.88%), with route progress of 15.35 m. Across three seeds, removing dynamic environment modeling or candidate-conditioned geometric interaction reduces mean intrusion AP from 0.8590 to 0.7624 and 0.7252, respectively. These results support coupling environment evolution with candidate-conditioned geometric reasoning for risk prediction and safety-oriented candidate selection.

</details>

#### 2026-09-15 - ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation

**Authors:** Yushan Bai, Boyu Zheng, Zhiyang Mao, Hongzheng Sun, Yuchuang Tong, En Li, Zhengtao Zhang
**Links:** [abs](https://arxiv.org/abs/2609.16586) - [pdf](https://arxiv.org/pdf/2609.16586)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, VR, simulation

<details>
<summary>Abstract</summary>

Multi-finger dexterous manipulation relies on stable hand-object interactions, yet these interactions are partially observable in practice. Visual observations are often occluded by the hand, tactile sensors introduce hardware-specific modalities and calibration burdens, and existing policies rarely model how these cues evolve under actions, making them brittle under contact uncertainty. To address these, we present ProxiDex, a dynamics-guided proximity policy framework that treats hand-object proximity as an interaction state for dexterous manipulation. ProxiDex reconstructs interaction point clouds and converts geometric distances into proximity cues, forming a hardware-agnostic contact representation that provides immersive feedback during VR teleoperation. Built on this representation, ProxiDex learns action-conditioned proximity dynamics with a coupled forward-inverse design: future observation latents are predicted from actions, while proximity variations are decoded from latent changes. Leveraging these dynamics, ProxiDex adaptively reweights proximity tokens across manipulation phases and uses dynamics-consistency supervision to guide policy inference, stabilizing action generation under unreliable visual feedback. Simulation and real-world experiments demonstrate improved success rates and robustness over representative baselines across standard, unseen objects, and perturbation scenarios. Additional visualizations are available at https://proxidex.github.io/.

</details>

#### 2026-09-15 - UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data

**Authors:** Hyesung Lee, Si-Hwan Heo, Sungwook Yang
**Links:** [abs](https://arxiv.org/abs/2609.16504) - [pdf](https://arxiv.org/pdf/2609.16504)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Human videos provide demonstrations of dexterous manipulation but lack robot-executable actions and tactile measurements. We present UniDex-ViTac, a framework that uses human-video-guided simulation to generate robot demonstrations paired with fingertip contact observations for training a deployable visuo-tactile policy. Object-specific residual reinforcement learning specialists adapt annotated human-object interaction references to a robotic arm-hand system. Their successful rollouts pair final robot action targets with robot-side fingertip contact observations. From 50 human demonstrations across ten objects, we collect 10,000 simulated trajectories to train a single Action Chunking with Transformers (ACT) based generalist. The policy combines point clouds, proprioception, and four binary contact signals encoded through fingertip labels and a separate token, without requiring human references or privileged object identity and pose at deployment. The contact-augmented configuration achieves 68.3% macro-average success in simulation, compared with 55.5% for the point-cloud-only baseline. Without real-robot demonstrations or policy fine-tuning, it succeeds in 73/110 physical trials (66.4%) across six seen and five unseen objects, compared with 60/110 (54.5%) for the baseline, an increase of 11.8 percentage points. These results support the feasibility of learning a unified visuo-tactile dexterous manipulation policy from video-guided simulated interactions. Project page: https://unidex-vitac.github.io/

</details>

#### 2026-09-14 - Geometry vs Structure: Graph-Based Diagnostics for LiDAR Point-Cloud Simulation Fidelity

**Authors:** Ghazal Farhani, Taufiq Rahman
**Links:** [abs](https://arxiv.org/abs/2609.16378) - [pdf](https://arxiv.org/pdf/2609.16378)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>Abstract</summary>

Digital twins provide a scalable and cost-effective complement to real-world testing for validating autonomous-driving and advanced driver-assistance system (ADAS) sensor pipelines. However, quantifying their fidelity remains challenging, particularly for 3D LiDAR point clouds, where conventional geometric metrics may overlook important structural discrepancies. We present a graph-based framework for evaluating the structural fidelity of simulated LiDAR point clouds against real-world scans. While scan-level metrics such as Chamfer distance capture point-wise geometric similarity, they do not explicitly represent connectivity, topology, or object-level organization. Our framework constructs graphs from real and simulated point clouds, applies Louvain community detection to identify spatially coherent subgraphs, and matches corresponding communities using centroid proximity. For each matched pair, we compute $r_λ$, a bounded graph-spectral metric motivated by Weyl's inequality, and compare it with density-aware Chamfer distance (CDC) as a geometric baseline. Controlled perturbation experiments demonstrate that $r_λ$ is invariant to rigid transformations and robust to sensor noise while remaining sensitive to structural deformation. We evaluate the framework on 50 paired real and simulated LiDAR scans acquired using a Velodyne VLP-32C sensor and CARLA, respectively. The dataset contains more than 1,000 matched communities across four representative classes: vehicles, vegetation, trees, and building walls. The results show that geometric and structural measures capture complementary aspects of simulation fidelity, supporting graph-spectral analysis as an additional diagnostic layer for validating digital twins in ADAS and autonomous-driving applications.

</details>

#### 2026-09-14 - JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion

**Authors:** Qihao Yuan, Yixuan Qiu, Ziyu Cao, Ming Cao, Kailai Li
**Links:** [abs](https://arxiv.org/abs/2609.15770) - [pdf](https://arxiv.org/pdf/2609.15770)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation, world model

<details>
<summary>Abstract</summary>

Light detection and ranging (LiDAR) remains less explored than RGB-D sensing for perceptive legged locomotion, and existing LiDAR-based approaches often rely on explicit mapping. We present JEPLO (Joint-Embedding Predictive learning for legged LOcomotion), a single-stage learning framework for mapping-free, LiDAR-based perceptive locomotion for legged robots. We introduce a proprio-exteroceptive JEPA (PE-JEPA) world model to learn predictive egocentric terrain representations from onboard observations, including raw LiDAR scans. A concurrent JEPA-teacher-student (CJTS) pipeline is further proposed to train a locomotion policy informed by JEPA latent representations in simulation using deep reinforcement learning with a simple reward formulation. The framework achieves successful sim-to-real transfer, enabling omnidirectional traversal of diverse terrains, including long staircases and high boxes, with lightweight onboard computation. Evaluations demonstrate greater robustness than existing perceptive locomotion frameworks, particularly under degraded perception caused by occlusion, sparsity and noise. Further analysis validates JEPLO's ability to retain task-relevant information under these challenging conditions. We open-source our implementation, experimental datasets, and hardware setup designs https://github.com/ASIG-X/JEPLO.

</details>

#### 2026-09-14 - Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands

**Authors:** Zhenjie Yang, Yideng Zhang, Dongjie Zhang, Chenyu Jiang, Xianshuai Liu, Yufeng Li, Zuhao Ge, Xingyu Jiao, Zheng Zhang, Kaiyu He, He Wang, Yuwen Zhong, Yi Deng, Muyun Jiang, Xianliang Huang, Haisheng Su, Donghang Zhang, Jian Zhang, Xue Yang, Hongyang Li, Zuxuan Wu, Yu-Gang Jiang, Xiaosong Jia, Junchi Yan
**Links:** [abs](https://arxiv.org/abs/2609.15726) - [pdf](https://arxiv.org/pdf/2609.15726)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Tactile sensing provides contact information that can be difficult to infer from vision alone, but tactile hardware for dexterous hands has not converged to a common design. Dexterous hands differ in finger structure, contact surfaces, and sensor layouts, while simulated tactile signals still differ from measurements produced by physical sensors. These factors make it difficult to study visuo-tactile manipulation across diverse dexterous hands within a consistent experimental setting. We present Bench2Dex, a simulation benchmark for visuo-tactile bimanual manipulation across 12 dexterous hands. We adapt existing robot models with a shared simulated tactile interface that converts local contact geometry into image-like tactile observations. The interface provides a consistent observation format across different hand morphologies without attempting to reproduce the output of a specific physical tactile sensor. Bench2Dex includes 26 bimanual manipulation tasks that involve tool use, articulated-object interaction, and multi-stage manipulation, together with about 1.3K human-teleoperated demonstrations. The benchmark provides synchronized visual, tactile, proprioceptive, action, and object-state observations, together with executable task metrics. For robustness, we group seven perturbation types into invariance axis, where the correct action does not change, and equivariance axis, where the correct action changes together with the perturbation. We evaluate ACT, Diffusion Policy, pi0.5, and GR00T N1.5 on Bench2Dex and report their performance and failure modes. Bench2Dex is meant as a platform for studying visuo-tactile learning across dexterous hands. It does not assume that simulated tactile observations can replace real tactile sensing; it offers a shared setting for algorithm development while tactile hardware and simulation models are still evolving.

</details>

#### 2026-09-14 - From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation

**Authors:** Ailing Zhang, Fan Gao, Song Zhang, Kawa Leong, Ziyu Wu, Yafei Wang
**Links:** [abs](https://arxiv.org/abs/2609.15382) - [pdf](https://arxiv.org/pdf/2609.15382)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>Abstract</summary>

Wheel-loader excavation is a sequential decision problem in which every scoop changes the terrain available to subsequent actions. A practical world model must predict action consequences accurately, rank candidates in real time, and operate inside the closed loop of a full-size machine. We present the World-Action Model (WAM), which proposes multiple scoops, rejects geometrically inadmissible candidates, jointly predicts signed terrain change and loaded volume, executes the candidate with the largest predicted load, and replans from the newly observed terrain. On 32 geometry-disjoint MinSlope test episodes, adding world-model ranking to matched diffusion proposals reduces the mean scoop count from 651.8 to 540.6 (17.1%), preserves 32/32 completion, and improves every paired episode. In a complete-system comparison, WAM completes 32/32 episodes versus 29/32 for an independently trained soft actor-critic policy. Comparisons of input representations, spatial support, and five architectures identify an accurate and efficient physics-structured predictor. We further evaluate the interface on event-disjoint full-size-loader data and deploy the complete perception-proposal-prediction-selection-execution loop for autonomous excavation. The ROS2/TensorRT implementation processes five candidates in 72.4 ms on a Jetson AGX Orin. The simulation results establish decision-level gains, while the physical experiments demonstrate real-world closed-loop feasibility.

</details>

#### 2026-09-14 - Legislating World-Model-Based Planning with Legal Reasoning

**Authors:** Dylan Waldner, Yiannis Kantaros, Guido Governatori, Risto Miikkulainen, Amir Banifatemi
**Links:** [abs](https://arxiv.org/abs/2609.15113) - [pdf](https://arxiv.org/pdf/2609.15113)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world model

<details>
<summary>Abstract</summary>

As robotic systems grow more general, legal norms are needed to integrate them into society. This paper extends the isomorphism problem of aligning legal source texts with their encodings, and measures two key challenges to robot normative control: (1) the \textit{grounding isomorphism gap}, where perception error grounds false atoms for legal reasoning, and (2) the \textit{ontological isomorphism gap}, where one legal conclusion admits many faithful translations into planning constraints. The paper introduces a legal planning stack that employs Defeasible Deontic Logic (DDL) to constrain a motion planner. The stack leverages learned world models to plan and to provide legal context, enabling \textit{ex ante} governance that intervenes before an illegal action is executed. It was deployed on a simulated robot arm pushing a cube across a $3\times3$ grid. The findings were (1) the legislated agent abided substantially more often than the non-legislated one, and modeling perception uncertainty lifted abidance even further, (2) the legal reasoning ran efficiently at runtime and its verdicts were auditable, and (3) the stack adapted to exogenous signals and endogenous rule changes. Both gaps were measured: (4) world model and probe error corrupted the factual input for the DDL reasoner, and (5) a single law admitted several faithful metric interpretations yielding drastically different abidance. Thus, \textit{ex ante} legislation functions as intended, and closing these gaps with a standardized mapping from the law to runtime constraints and improved fact grounding from perception will yield robust laws that align robot behavior with society's norms.

</details>

#### 2026-09-10 - Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection

**Authors:** Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie, Gang Liu, Hongjie Yan, Wei Zhou
**Links:** [abs](https://arxiv.org/abs/2609.11225) - [pdf](https://arxiv.org/pdf/2609.11225)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** stereo depth, robot navigation, mapping, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- 作者：Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie, Gang Liu, Hongjie Yan, Wei Zhou
- 出版日期：2026-09-10T08:25:46Z
- 分类：Embodied / Robotics / AR Applications（主要分类）；次要分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.11225 ；PDF https://arxiv.org/pdf/2609.11225

### 一句话总结
论文提出统一的具身智能体运行时 HROS 及其住宅小区巡检实现 Argos，将四足机器人导航、感知、认知推理、语音交互与安全约束下的自演化整合为可追踪的闭环巡检系统。

### 研究问题
自主物业巡检不仅需要稳健的机器人导航，还需要在可追踪的运行闭环中连接异构传感、可复用的自主能力、多模态场景理解、人机交互与企业响应。现有四足巡检系统常通过任务专用接口集成这些功能，导致上下文协调、知识复用和受控适应变得困难。

### 核心思路/方法
- 提出 Harness Robotic OS（HROS），一个统一的具身智能体运行时；Argos 是其面向住宅小区巡检的具体实现。
- HROS 将系统组织为机器人运行时、具身自主技能、认知智能体运行时、交互与运维平面。
- 通过共享上下文连接物理状态与智能体推理。
- 支持流式 ASR/TTS 的语音任务交互。
- 采用分层的工作记忆、情景记忆与语义记忆来保存运行知识。
- 设计安全门控的自演化闭环，将执行轨迹转化为带版本的候选更新，不允许无约束的在线修改。
- Argos 原型集成 Vbot 四足机器人、Fast-LIO2 定位与建图、Hobot-Stereo 深度感知、PCT-Planner 全局规划、EGO-Planner 局部运动生成，以及 OpenClaw 编排的 Qwen3-VL 巡检分析。

### 主要贡献
- 提出统一的具身智能体运行时 HROS，用于闭环四足巡检，缓解任务专用接口带来的上下文协调与知识复用困难。
- 给出 Argos 实现，将机器人运行时、自主技能、认知推理、语音交互和安全门控自演化组织为分层系统。
- 在住宅物业环境中验证部署的导航与巡检闭环，报告了 100% 航点可达率、户外定位误差低于 10 cm、局部障碍响应延迟低于 200 ms、代表性危险检测率 85–95%、告警投递与结构化报告生成成功率 99%。
- 摘要称 HROS 为记忆增强、语音感知且可持续改进的具身巡检智能体提供可扩展软件基础。

### 局限性
- 论文仅提供摘要，未提供关于实验规模、场景数量、基线对比、消融研究、失败案例和统计显著性的细节；这些信息摘要未提供足够信息。
- 危险检测率 85–95% 的具体类别、测试条件与误报情况，摘要未提供足够信息。
- 自演化闭环的版本管理机制、安全门控具体策略及其长期有效性，摘要未提供足够信息。
- 系统在住宅小区之外的泛化能力、不同机器人平台的可移植性，摘要未提供足够信息。
- 真实部署中的成本、维护、隐私与法规问题，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文聚焦具身智能体运行时与四足机器人闭环巡检的系统集成，涉及导航、感知、认知记忆、语音交互与安全自演化等完整链路，并给出可量化的部署指标；对具身智能系统落地、机器人操作系统架构和物业巡检应用有直接参考价值。但需注意仅凭摘要无法评估实验严谨性与泛化性，建议获取全文后重点核查实验细节与自演化机制。

</details>

<details>
<summary>Abstract</summary>

Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
