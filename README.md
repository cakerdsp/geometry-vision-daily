# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日总览

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

- 当前滚动窗口论文数：44
- 分类分布：
  - Neural Scene Representations & Rendering: 14
  - Embodied / Robotics / AR Applications: 13
  - 3D Reconstruction & Multi-view Geometry: 12
  - Dynamic / 4D Reconstruction: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### interests.md 指令分析

未指定 `generate daily trend report`，因此未执行额外趋势报告任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-03T01:30:19-04:00
**Total number of papers:** 44
**Number of papers added in the latest update:** 44
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

No papers in the current README window.

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-02 - PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting

**Authors:** Adrian Ramlal, John S. Zelek
**Links:** [abs](https://arxiv.org/abs/2606.03479) - [pdf](https://arxiv.org/pdf/2606.03479)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, 4D Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (3DGS) methods reconstruct time-varying scenes from synchronized multi-camera video using photometric supervision. When a moving object becomes fully occluded from all training cameras, this supervision vanishes: the Gaussians representing it receive no gradient signal and degrade. Existing approaches to incomplete observations in neural reconstruction rely on learned generative priors that prioritize visual plausibility over physical correctness. We propose $\textbf{PersistGS}$, a method that restores object permanence during occlusion by coupling differentiable rigid body simulation with 3D Gaussian Splatting. Our approach decomposes the scene into per-object Gaussians and collision meshes, estimates friction and velocity from the observed pre-occlusion trajectory via differentiable simulation, and uses the resulting SE(3) trajectory to position object Gaussians throughout the occlusion period. Because the predicted trajectory satisfies the governing equations of rigid body dynamics, it faithfully captures contact events (bounces, friction-based deceleration, direction changes) that kinematic extrapolation cannot model. We introduce a centroid silhouette loss that isolates positional gradients from appearance noise, yielding 40% lower trajectory error than photometric supervision. We evaluate using cameras withheld from training that observe the object during its occlusion. Experiments on synthetic scenes show that PersistGS outperforms constant velocity extrapolation by +2.46dB PSNR and comes within 0.19dB of a ground-truth trajectory upper bound.

</details>

#### 2026-06-01 - TROPHIES: Temporal Reconstruction of Places, Humans, and Cameras from Multi-view Videos

**Authors:** Jinpeng Liu, Yukang Xu, Yutong Li, Xingyu Liu
**Links:** [abs](https://arxiv.org/abs/2606.02350) - [pdf](https://arxiv.org/pdf/2606.02350)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** temporal reconstruction

<details>
<summary>Abstract</summary>

Reconstructing humans and their surrounding environments in a globally consistent 4D space is essential for comprehensive perception. However, prior works typically assume single-view inputs or decouple humans, scenes, and cameras, making them unable to recover coherent geometry, stable motion, and physically aligned trajectories. These limitations motivate us to introduce a new task: unified human-scene-camera reconstruction from multi-view videos, which aims to jointly estimate dynamic humans, static scenes, and camera poses in one global coordinate frame. We propose TROPHIES--Temporal Reconstruction of Places, Humans, and Cameras from Multi-view Videos-a unified framework tailored for this task. TROPHIES features a Human Branch that models humans through temporal and spatial reasoning, and a Scene Branch that reconstructs static geometry with human-aware attention. A global alignment and optimization module couples both branches by enforcing scale consistency, contact priors, and cross-view temporal coherence. Experiments on EgoHuman and EgoExo4D demonstrate that TROPHIES achieves globally aligned, physically plausible 4D reconstructions and consistently outperforms existing paradigms in both global fidelity and human-scene consistency.

</details>

#### 2026-06-01 - WebSpline: Structure-Informed Splines for Real-Time 3D Gaussians from Monocular Videos

**Authors:** Jongmin Park, Jeonghwan Yun, Minh-Quan Viet Bui, Munchurl Kim
**Links:** [abs](https://arxiv.org/abs/2606.02096) - [pdf](https://arxiv.org/pdf/2606.02096)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, dynamic Gaussian, scene reconstruction, rendering

<details>
<summary>Abstract</summary>

Dynamic scene reconstruction from monocular videos remains highly challenging, as existing methods often struggle to balance global structural coherence and local fine-grained details under limited multi-view cues. To address this challenge, we propose WebSpline, a novel dynamic 3D Gaussian framework that enables structurally coherent and high-fidelity reconstruction from monocular videos with fast rendering. The core of WebSpline is the Structure-Informed Spline (SIS) representation, which models each dynamic Gaussian trajectory using a learnable cubic Hermite spline whose motion is structurally organized with an auxiliary Structural Proxy Graph (SPG). The proposed framework is optimized in two stages: (i) in the first stage, the SPG is initialized from 2D point tracks and refined with temporal rigidity regularization to establish structural coherence for moving objects across the sequence; and (ii) in the second stage, the SIS representation is initialized from the refined SPG and optimized under both spatial and structural neighborhood constraints. At inference, Gaussian motion is obtained solely by evaluating the learned SIS, enabling fast rendering. Extensive experiments on the challenging monocular dynamic scene benchmarks, iPhone and NVIDIA, demonstrate that our WebSpline achieves state-of-the-art rendering quality while rendering over 10 times faster than WorldTree, the second-best method on the iPhone dataset.

</details>

#### 2026-06-01 - TIDES: Time-Derivative Event Simulation via Deformable Reconstruction

**Authors:** Christopher Thirgood, Dipon Kumar Ghosh, Simon Hadfield
**Links:** [abs](https://arxiv.org/abs/2606.02058) - [pdf](https://arxiv.org/pdf/2606.02058)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** deformable reconstruction, dynamic Gaussian, Gaussian Splatting, scene representation, rendering, splatting, simulation

<details>
<summary>Abstract</summary>

Event cameras emit asynchronous events in response to environmental appearance changes. The scarcity of real-world event datasets makes simulation essential. However, most simulators infer event timestamps from frame sequences, forcing many threshold crossings to share a small set of discrete times; a failure mode we term timestamp batching that worsens under fast motion and occlusion. We present TIDES, a continuous-time event simulator built on dynamic Gaussian splatting. Because TIDES operates on an explicit 3D scene representation with learnt geometry and motion, it can derive per-pixel intensity dynamics directly from the scene, rather than by differencing rendered frames. This enables accurate threshold-crossing prediction, including multiple crossings per rendering step, without temporal upsampling or frame interpolation. The same 3D scene model reveals where objects partially occlude one another; TIDES uses this to guide adaptive time stepping, concentrating computation only in regions where occlusion dynamics make simple models of brightness change unreliable. Finally, we model finite sensor bandwidth using a tile-level arbiter whose throughput, jitter, and event drops reproduce realistic sensor artifacts. Across paired RGB-event benchmarks, TIDES attains state-of-the-art event-stream fidelity. We also show that events simulated by TIDES transfer more effectively to real downstream tasks than competitors'.

</details>

#### 2026-06-01 - DisFlow: Scene Flow from Distance Field for Object Pose, Velocity Tracking, and Dynamic Object Reconstruction

**Authors:** Lan Wu, Sheila Sutjipto, Jennifer Wakulicz, Teresa Vidal-Calleja
**Links:** [abs](https://arxiv.org/abs/2606.01824) - [pdf](https://arxiv.org/pdf/2606.01824)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** scene flow, pose estimation, surface reconstruction

<details>
<summary>Abstract</summary>

We present \emph{DisFlow}, a novel framework for online scene flow estimation from distance field that enables \emph{6DoF dynamic object pose estimation}, \emph{motion tracking}, and \emph{surface reconstruction}. The scene is represented by Gaussian Process Implicit Surfaces (GPIS), with surface normals serving as derivative constraints, enabling accurate signed distance computations near the surface and gradient queries with uncertainty. With this representation as a foundation, we compute a scene flow from the distance field that describes how surface points are transported over time in consecutive frames. Through our flow, we can estimate an object's pose and motion by incrementally registering a new observed point cloud via an elegant closed-form optimisation. Unlike prior methods that operate in the camera or world frame, our approach performs probabilistic fusion directly in the \emph{object frame}, where the object remains geometrically consistent over time. The tight coupling of the DisFlow method in space and time yields dense geometry, surface normals, object pose trajectories, velocities, and uncertainty, all at real-time rates. We evaluate DisFlow on dynamic object sequences and demonstrate that it achieves accurate pose and motion tracking while simultaneously reconstructing high-quality object surfaces. Code publicly available at \href{https://github.com/LanWu076/disflow_ros2}{https://github.com/LanWu076/disflow\_ros2}

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

#### 2026-06-02 - SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image

**Authors:** Inhee Lee, Sangwon Baik, Sungjoo Kim, Hyeonwoo Kim, Hyunsoo Cha, Hanbyul Joo
**Links:** [abs](https://arxiv.org/abs/2606.03994) - [pdf](https://arxiv.org/pdf/2606.03994)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, scene reconstruction, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image
- 作者：Inhee Lee, Sangwon Baik, Sungjoo Kim, Hyeonwoo Kim, Hyunsoo Cha, Hanbyul Joo
- 出版日期：2026-06-02
- 分类：3D重建与多视角几何（主要）；具身/机器人/AR应用（次要）
- 链接：摘要页 https://arxiv.org/abs/2606.03994 ，PDF https://arxiv.org/pdf/2606.03994

### 一句话总结
SimuScene 提出一种将物理模拟作为诊断工具的3D场景重建流程，从单张图像生成可稳定用于物理仿真的组合式3D场景。

### 研究问题
如何从单张图像重建出组合式3D场景，使其在物理模拟中不出现物体穿透、悬空或下沉等不稳定现象。

### 核心思路/方法
1. 将物理引擎嵌入形状和布局估计的生成过程中，而非仅作为后处理校正。
2. 通过模拟重力作用下重建物体的行为，将穿透和支撑失败转化为量化校正信号。
3. 利用这些信号驱动重力轴拉伸和模态形状重采样，形成有物理反馈的循环，逐步修正累积的重建误差，最终输出稳定的仿真就绪场景。

### 主要贡献
- 提出一种物理在环的组合式3D重建流水线，将物理模拟作为诊断测量工具用于生成过程。
- 将物理稳定性作为校正信号，实现重力轴拉伸和形状重采样，解决穿透和支撑问题。
- 在物理稳定性和几何对齐基准上达到最先进性能，并验证了在人形控制与机器人臂操作任务中的实用性。

### 与相关方法的关系
- 与 VGGT、DUSt3R、MASt3R、CroCo、NeRF、Gaussian Splatting、动态场景重建方法的关系：摘要未提供足够信息。
- 与现有物理感知方法的关系：明确指出这些方法将物理处理严格视为后处理的布局校正，无法解决底层几何误差；SimuScene 则将物理模拟集成至生成过程中，实现持续反馈和修正。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该方法针对具身智能和机器人操控中的关键瓶颈（仿真就绪场景重建），提出了一种将物理模拟融入生成过程的创新范式，实验表明在稳定性和对齐性上优于现有方法，且在人形控制和机械臂任务中有直接应用价值。对3D重建、物理模拟、机器人学方向的研究者具有重要参考意义。

</details>

<details>
<summary>Abstract</summary>

Reconstructing interactive, simulation-ready 3D scenes from a single image is a critical bottleneck for robotic manipulation. While recent single-image lifters recover plausible per-object shapes, composing them yields scenes that collapse under physical simulation due to interpenetrating, hovering, or sinking objects. Existing physics-aware methods address this strictly as a post-hoc layout correction, leaving the underlying geometric errors unresolved. To address this, we introduce SimuScene, a compositional 3D reconstruction pipeline that puts physics in the loop of shape and layout estimation. Rather than using physics merely for layout cleanup, we utilize the physics engine as a diagnostic measurement tool during the generative process itself. By diagnostically simulating reconstructed objects under gravity, we convert penetration and support failures into quantitative correction signals that drive gravity-axis stretching and amodal shape resampling. This physics-informed feedback loop mitigates accumulated reconstruction errors and produces a stable, simulation-ready compositional 3D scene. Extensive experiments demonstrate state-of-the-art performance on physical stability and geometric alignment benchmarks. We further highlight SimuScene's utility by deploying reconstructed environments in humanoid control and robot-arm manipulation tasks.

</details>

#### 2026-06-02 - PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation

**Authors:** Shinjeong Kim, Ignacio Alzugaray, Callum Rhodes, Paul H. J. Kelly, Andrew J. Davison
**Links:** [abs](https://arxiv.org/abs/2606.03989) - [pdf](https://arxiv.org/pdf/2606.03989)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

好的，这是基于您提供的论文元数据和摘要生成的简要分析。

### Metadata
- 标题：PixVOD: 像素分布式直接视觉里程计与深度估计
- 作者：Shinjeong Kim, Ignacio Alzugaray, Callum Rhodes, Paul H. J. Kelly, Andrew J. Davison
- 出版日期：2026-06-02
- 分类：3D重建与多视图几何
- 链接：摘要: https://arxiv.org/abs/2606.03989，PDF: https://arxiv.org/pdf/2606.03989

### 一句话总结
本文提出一种完全可并行化的视觉里程计与深度估计方法，该方法通过高斯置信传播（GBP）在像素之间分布式地进行相机运动和深度的推理，旨在实现传感器内计算。

### 研究问题
如何设计一种能够直接在图像传感器像素级别进行分布式计算的视觉里程计和深度估计算法，以减少从传感器传输冗余、噪声数据的开销，并减轻下游计算负担。

### 核心思路/方法
1.  **像素级分布式处理**：核心思想是将视觉里程计和深度估计的计算过程分布到每个像素上，而不是在传统处理器上进行集中式计算。这契合了焦平面传感器-处理器（focal-plane sensor-processor）的硬件趋势。
2.  **高斯置信传播（GBP）**：通过GBP算法，使传感器上的每个像素能够与其邻居像素交换信息，从而就相机运动达成共识，并根据每个像素的光度观测值和表面法线先验来推断深度。
3.  **关键帧锚定机制**：为了优化过程中的几何稳定性，引入了一种类似关键帧的锚定机制。该机制通过调节帧之间的有效基线，使得运动和深度更新能够保持一致性。

### 主要贡献
根据摘要，主要贡献是：
1.  提出了一种基于像素级分布式计算的视觉里程计和深度估计方法（PixVOD）。
2.  证明了基于高斯置信传播（GBP）的像素级分布式里程计与深度估计的可行性。
3.  提出了关键帧锚定机制，以实现在传感器上的稳定优化。
4.  在现实数据集上对该方法的可行性进行了评估。

### 与相关方法的关系
摘要未提供足够信息。因此无法说明它与VGGT、DUSt3R、MASt3R、CroCo、NeRF、Gaussian Splatting、动态场景重建方法的具体关系。摘要仅将自身定位为一种与“焦平面传感器-处理器”硬件趋势相关的、全新的分布式计算范式。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**
理由：该方法提出了一个颇具新意的计算范式，即完全在像素级别分布式地进行视觉里程计。这对于关注传感器内计算、低功耗视觉和边缘AI的研究者来说是一个有趣的方向。然而，当前信息仅包含初步的可行性验证，对于其实际性能（如精度、鲁棒性、与现有集中式方法的对比）以及具体的硬件实现细节尚不清楚，因此优先级设为中等。

</details>

<details>
<summary>Abstract</summary>

Images composed of 2D pixel arrays are the standard input to computer vision algorithms, yet many underlying computations can be distributed across pixels. Transmitting raw, redundant, and noisy pixel data off the sensor remains inefficient, motivating a shift toward focal-plane sensor-processors that perform a significant part of the computation directly within each pixel. We envision pixels synthesizing higher-level signals locally, reducing downstream load, and providing richer inputs for higher-level vision tasks. We propose a fully parallelizable form of visual odometry and depth estimation across pixels, where sensor-processors exchange information through Gaussian Belief Propagation (GBP) to achieve consensus about camera motion and infer depth from per-pixel photometric observations and a surface normal prior. To maintain geometric stability during optimization, we introduce a keyframe-like anchoring mechanism that regulates the effective baseline between frames, enabling consistent motion and depth updates. Our method is evaluated on realistic datasets, demonstrating the feasibility of GBP-based pixel-level distributed odometry and depth estimation with keyframe anchoring on-sensor. Project Page: https://www.shinjeongkim.com/pixvod/

</details>

#### 2026-06-02 - Multi-Robot Bearing-only Pose Estimation via Angle Rigidity

**Authors:** J. Francisco Presenza, Leonardo J. Colombo, Ignacio Mas, Juan I. Giribet
**Links:** [abs](https://arxiv.org/abs/2606.03931) - [pdf](https://arxiv.org/pdf/2606.03931)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：基于角度刚性的多机器人仅方位姿态估计
- 作者：J. Francisco Presenza, Leonardo J. Colombo, Ignacio Mas, Juan I. Giribet
- 出版日期：2026-06-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.03931

### 一句话总结
本文提出一种基于角度刚性的分布式仅方位（bearing-only）估计器，利用机器人间方位测量即可同时估计三维位置和姿态，并在弱于传统刚性条件的角度刚性拓扑下保证局部指数稳定性。

### 研究问题
如何在时变多机器人系统中，仅使用从机体坐标系获取的方位信息（无需先验方向或全局位置），分布式地估计机器人在ℝ³中的位置和SO(3)中的姿态。

### 核心思路/方法
1. 从机体坐标系的轴承测量中计算出机器人之间的夹角度量。
2. 基于这些角度建立位置估计器，无需知道机器人各自的朝向。
3. 利用估计出的位置、原始轴承及其导数，反推出每个机器人的SO(3)姿态。
4. 要求感知拓扑满足“角度刚性”（angle-rigid）条件——该条件比常用的轴承刚性更弱。
5. 在部分机器人具有持续激励（persistently exciting）运动的前提下，证明估计器的局部一致指数稳定性。

### 主要贡献
- 提出首个基于角度刚性的分布式仅方位姿态估计方法，无需全局坐标系或姿态先验。
- 证明该方法在三维空间中同时恢复位置和旋转，且要求拓扑条件弱于传统轴承刚性。
- 给出连续时间估计器的局部指数稳定性证明（依赖持续激励假设）。
- 通过仿真验证了方法的有效性和实用性。

### 与相关方法的关系
摘要未提供足够信息。文中未提及VGGT、DUSt3R、MASt3R、CroCo、NeRF、Gaussian Splatting或动态场景重建方法，无法判断与之关系。

### 局限性
摘要未提供足够信息。例如未讨论传感器噪声、编队规模、收敛速度、非持续激励状态下的性能退化等局限。

### 阅读优先级
中  
理由：对于多机器人分布式定位和编队控制领域有参考价值，属于方法论创新；但属于特定应用场景（仅方位估计）的增强型方案，非通用视觉重建或SLAM方法。

</details>

<details>
<summary>Abstract</summary>

This letter proposes a novel distributed bearing-based pose estimator for time-varying multi-robot systems. The method uses angles computed from body-frame bearings to estimate the robots' positions in $\mathbb{R}^3$ without knowledge of their orientations. The orientations in $\mathrm{SO}(3)$ are recovered from the estimated positions, the bearings, and the bearing derivatives. The proposed observer only requires the (directed) sensing topology to be \textit{angle-rigid}, a weaker condition than the commonly used ones like bearing rigidity. Local uniform exponential stability of the proposed observer is established under the assumption of persistently exciting motions for a subset of robots. Simulations are presented and discussed to evaluate the scheme's effectiveness and practicality.

</details>

#### 2026-06-02 - SAMatcher: Co-Visibility Modeling with Segment Anything for Robust Feature Matching

**Authors:** Xu Pan, Qiyuan Ma, Mingyue Dong, He Chen, Wei Ji, Xianwei Zheng
**Links:** [abs](https://arxiv.org/abs/2606.03406) - [pdf](https://arxiv.org/pdf/2606.03406)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** image matching, structure from motion, feature matching, localization

<details>
<summary>Abstract</summary>

Reliable correspondence estimation is a fundamental problem in image processing, underpinning applications such as Structure from Motion, visual localization, and image registration. Existing learning-based methods have significantly improved local feature representations, yet most still operate at the pixel or patch level and lack explicit modeling of regions that are jointly visible across views. We propose SAMatcher, a feature matching framework that formulates correspondence estimation through co-visibility modeling. Instead of directly matching local features, SAMatcher first predicts co-visible region masks and bounding boxes as structured priors for correspondence estimation. Built upon the Segment Anything Model (SAM), it introduces a symmetric cross-view interaction mechanism that enables bidirectional feature exchange and cross-view semantic alignment. We further develop a unified supervision scheme that jointly optimizes mask prediction and box localization through mask learning, box regression, and mask-box consistency constraints. Extensive experiments on challenging benchmarks demonstrate substantial improvements over existing matching pipelines, particularly under large viewpoint and scale variations. Our results show that foundation models originally designed for monocular segmentation can be effectively extended to multi-view correspondence reasoning through explicit co-visibility modeling, offering a new perspective on structured representation learning for image matching. Code and project page: https://xupan.top/Projects/samatcher

</details>

#### 2026-06-02 - BA-T: An Iterative Transformer for Two-View Bundle Adjustment

**Authors:** Ganlin Zhang, Weirong Chen, Daniel Cremers, Xi Wang
**Links:** [abs](https://arxiv.org/abs/2606.03287) - [pdf](https://arxiv.org/pdf/2606.03287)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, bundle adjustment

<details>
<summary>Abstract</summary>

Feed-forward models for 3D reconstruction have achieved strong performance using deep cross-view attention to exchange information across images. However, these approaches often depend on heavy decoder stacks and lack a structured mechanism for geometry refinement, resulting in poor multi-view consistency. We address this by drawing inspiration from classical bundle adjustment (BA), which can be viewed as an iterative information propagation process between poses and local geometry. Inspired by BA, we propose BA-T, an iterative Transformer that implements BA-style structured updates as a repeatable layer in implicit token space. Instead of relying on deep attention stacks, BA-T refines predictions based on latent residual by a single lightweight layer. Experiments demonstrate that BA-T progressively improves pose and reconstruction accuracy across iterations, achieves stronger cross-view consistency than conventional decoders, and matches or surpasses substantially larger models while using only 16% of their decoder parameters. BA-T provides a compact, efficient, and structural alternative to depth-heavy attention, enabling accurate 3D reconstruction within a lightweight architecture. The code will be made publicly at https://github.com/zhangganlin/BA-T.

</details>

#### 2026-06-01 - BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting

**Authors:** Yanchen Wang, Lenny Aharon, Wangshu Zhu, Kyle Daruwalla, Linghua Zhang, Jiaru Zou, Selmaan Chettih, Helen Hou, Liam Paninski, Matthew R Whiteway
**Links:** [abs](https://arxiv.org/abs/2606.02937) - [pdf](https://arxiv.org/pdf/2606.02937)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, pose estimation, Gaussian Splatting, novel view synthesis, view synthesis, differentiable rendering, rendering, splatting

<details>
<summary>Abstract</summary>

Multi-view video recordings are increasingly used to capture the 3D movements of animals in experimental settings, yet extracting rich 3D representations from these recordings remains challenging. Supervised pose estimation requires extensive manual annotation, while general-purpose 3D reconstruction models trained on generic scene datasets fail on the specialized imagery and sparse-view setting of laboratory experiments. We address these limitations with BEAST3D, a self-supervised pretraining framework that learns 3D visual representations from unlabeled, calibrated multi-view video. BEAST3D uses a vision transformer to predict 3D Gaussian splats that reconstruct held-out views through differentiable rendering, while simultaneously segmenting the animal from the background. BEAST3D reconstructs 3D structure with as few as four views by conditioning directly on known camera parameters--unlike general-purpose models, which must estimate camera geometry from dense overlapping viewpoints that are seldom available in lab settings. Through comprehensive evaluation across four species, we demonstrate that BEAST3D produces rich, viewpoint-invariant features that transfer effectively to three downstream tasks: novel view synthesis, which validates the quality of the learned 3D representations; multi-view pose estimation, which provides the sparse keypoint trajectories widely used in behavioral analysis; and neural encoding, which relates 3D behavioral features to simultaneously recorded neural activity. BEAST3D thus establishes a versatile framework for behavioral analysis that leverages 3D structure in modern multi-view laboratory recordings.

</details>

#### 2026-06-01 - Modeling Depth Ambiguity: A Mixture-Density Representation for Flying-Point-Free Depth Estimation

**Authors:** Siyuan Bian, Congrong Xu, Jun Gao
**Links:** [abs](https://arxiv.org/abs/2606.02552) - [pdf](https://arxiv.org/pdf/2606.02552)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>Abstract</summary>

Despite advances in depth estimation, flying points remain a persistent failure mode: near object boundaries, depth estimators often predict spurious 3D points in the empty space between foreground and background surfaces. We trace this artifact to a standard modeling choice: assigning each pixel a single depth hypothesis. At boundaries, a pixel can straddle a foreground and a background surface, so its true depth is ambiguous between the two. A model that predicts a single depth cannot keep both possibilities, so training instead pulls the prediction toward an intermediate depth that lies on neither surface. We address this with MDA, a mixture-density representation that lets the model predict multiple depth hypotheses and their associated probabilities for each pixel. Near boundaries, different hypotheses can align with different surfaces, and the decoded depth is selected from one of these hypotheses rather than placed in the empty space between them. Across different backbones, MDA substantially improves boundary reconstruction and largely removes flying-point artifacts even under severe input blur, while adding negligible runtime overhead. The same mixture-density framework naturally extends to transparent objects, where it predicts multiple depth layers at transparent pixels, and to sky regions, where a dedicated component separates the unbounded sky from finite-depth regions, producing flying-point-free skylines. Project Page: https://biansy000.github.io/mda-site/.

</details>

#### 2026-06-01 - Symmetry-Aware 9D Pose Estimation with Sim(3)-Consistent Feature and Spherical Inception Convolution

**Authors:** Panfei Cheng, Hongshan Yu, Wenrui Chen, Xiaojun Tang, Jian Liu, Naveed Akhtar
**Links:** [abs](https://arxiv.org/abs/2606.02219) - [pdf](https://arxiv.org/pdf/2606.02219)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Object pose estimation is a fundamental problem for an agent system to perceive or manipulate objects in images or videos. However, current instance-level methods struggle with generalization to unseen objects. Category-level methods seek to address this, but remain constrained by the complexities of learning in the non-linear Sim(3) space and intra-class variations. To address these challenges, We propose an effective method for category-level object pose estimation with two key innovations: (1) A translation/size estimator, featuring a semantic-guided symmetry-aware module that leverages robust generalization capabilities of a large vision model (LVM) to infer symmetry points, resulting in accurate translation and size without shape priors. This result serves as a precomputed cue for rotation estimation, thereby reducing the difficulty of learning in the non-linear Sim(3) space and laying a robust foundation for tackling the inherently more challenging rotation estimation. (2) A feature fusion module, based on our proposed spherical large-kernel inception convolution, fuses semantic features from the LVM with systematically computed geometric features to extract essential pose features from intra-class variations by modeling long-range dependencies without excessive computational cost. Built on these innovations, we achieve SOTA on benchmarks and real-world scenes, while developing a robust robotic picking system capable of handling diverse objects. Our code will be available at the project page: {\hypersetup{urlcolor=blue}https://panfei-cheng.github.io/SSH-Pose}.

</details>

#### 2026-06-01 - PerBite: A Curated Diagnostic Workflow for Bite-Aware Food Volume Estimation

**Authors:** Ahmad AlMughrabi, Farid Al-Areqi, David Fernández Gómez, Umair Haroon, Marc Bolaños, Ricardo Marques, Petia Radeva
**Links:** [abs](https://arxiv.org/abs/2606.02021) - [pdf](https://arxiv.org/pdf/2606.02021)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction

<details>
<summary>Abstract</summary>

Can a visually plausible food mesh be trusted to estimate the volume of consumed food? \method investigates this question using selected paired before- and after-consumption states from the MetaFood CVPR 2026 Continuous 3D Reconstruction While Eating Challenge. The submitted workflow follows a curated reconstruction protocol: SAM~3 segments the food and plate regions; Hunyuan3D/SAM~3D generates a dimensionless food mesh; the plate diameter provides the metric scale; the plate geometry is removed in Blender; and the remaining mesh is hole-filled, made watertight, and integrated to estimate volume. MoGe-2 is used only as an auxiliary cue for initial dish-diameter estimation when direct plate measurement is uncertain; it is not the primary scale source for the reported challenge result. \method ranks first, with an average Chamfer distance of 8.31 across 34 meshes using rigid ICP without scale correction. On 17 before- and after-pairs, it achieves 33.87\% state-level volume MAPE and zero monotonicity violations, while consumed-volume MAPE remains 53.74\%. The results show that surface reconstruction, metric scale, controlled mesh cleanup, watertight volume integration, and physical depletion consistency should be evaluated separately for dietary assessment. Source code and evaluation scripts will be available at \href{https://github.com/GCVCG/PerBite-CVPR-MetaFood-2026}{github.com/GCVCG/PerBite-CVPR-MetaFood-2026}.

</details>

#### 2026-06-01 - Closed-Form Pose Estimation of Endoluminal Medical Devices via Gradiometer-Based Electromagnetic Localization System

**Authors:** Zhiwei Wu, Jiahao Luo, Yubo Pu, Siyi Wei, Yuankai Chen, Jinhui Zhang
**Links:** [abs](https://arxiv.org/abs/2606.01946) - [pdf](https://arxiv.org/pdf/2606.01946)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, localization

<details>
<summary>Abstract</summary>

Embedded magnetic tracking holds highly attractive prospects for remote navigation of endoluminal medical devices. However, existing six-degree-of-freedom pose recovery approaches often require pre-calibrated workspace field maps or iterative nonlinear optimization. This letter presents a Gradiometer-Based Electromagnetic Localization System (GELS), a closed-form tracking framework that uses a compact magnetometer array as an embedded quasi-gradiometer to estimate local magnetic fields and gradient tensors. These quantities are mapped by the Euler homogeneous relation to displacements between source and array, from which multi-source Procrustes registration recovers the array orientation and position using at least three non-collinear sources. The algorithm requires known source positions and array geometry, but no pre-calibrated workspace field maps, initial pose guesses, or calibrated excitation-source moments. The recovered pose also enables a proof-of-concept sub-level dipole localization task by serving as a mobile magnetic reference frame. Benchtop experiments across sensor-array configurations and excitation modes demonstrate sequence-averaged position errors of \SI{10.80}{\milli\meter}--\SI{15.57}{\milli\meter}, a fastest update rate of \SI{14.49}{\hertz}, and a median solver runtime of \SI{172.00}{\micro\second}. A perturbation-based error propagation analysis further identifies inter-sensor inconsistency and dipole-model mismatch as the dominant accuracy limits, thereby informing future sensor array and magnetic source design for further reducing pose-estimation error.

</details>

#### 2026-06-01 - SCAPO: Self-Supervised Category-Level Articulated Pose Estimation from a Single 3D Observation

**Authors:** Can Zhang, Gim Hee Lee
**Links:** [abs](https://arxiv.org/abs/2606.01940) - [pdf](https://arxiv.org/pdf/2606.01940)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Existing methods for category-level object articulation from a single 3D observation often rely on dense supervision, multi-frame inputs, or CAD templates, and still struggle to disentangle geometry from articulation or to recover explicit joint parameters. We propose SCAPO, a self-supervised framework that estimates canonical geometry, rigid part segmentation, and joint pivots, axes, and articulation states from a single RGB-D observation without ground-truth labels or category-specific models. Our SCAPO first uses an SE(3)-equivariant vector-neuron autoencoder to factor out global pose and align diverse instances into a shared canonical space. On this aligned shape, a joint-aware blend-skinning module is then designed to model part motion. We learn this representation through cycle reconstruction between observed and canonical shapes and cross-space alignment with a learnable canonical template that decouples shared category geometry from instance-specific residual shape. Experiments on synthetic and real articulated-object datasets show that our SCAPO recovers consistent part structure and accurate articulation parameters and outperforms all self-supervised baselines.

</details>

### 2026-05

#### 2026-05-31 - ActMVS: Active Scene Reconstruction with Monocular Multi-View Stereo

**Authors:** Guo Pu, Yixuan Han, Zhouhui Lian
**Links:** [abs](https://arxiv.org/abs/2606.01367) - [pdf](https://arxiv.org/pdf/2606.01367)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, scene reconstruction, multi-view stereo, stereo depth, spatial intelligence

<details>
<summary>Abstract</summary>

Active scene reconstruction enables robots/UAVs to autonomously plan trajectories and reconstruct environments without costly manual data acquisition. Unlike passive methods, active reconstruction requires real-time construction of high-confidence occupancy maps for collision-free navigation. Existing approaches rely on depth sensors for occupancy map updates, increasing platform cost and weight. To advance spatial intelligence, we aim for a vision-only monocular solution. However, current monocular scene reconstruction methods operate offline and fail to deliver globally consistent dense depth at the frame rates required for robots/UAVs navigation. To bridge this gap, we introduce ActMVS, the first framework for monocular active reconstruction. Our framework integrates a view factor graph construction for informed Multi-View Stereo depth prediction, along with a global depth optimization, to enable the online generation of high-quality, globally consistent dense depth maps. This enables monocular robots/UAVs to maintain reliable occupancy maps for safe trajectory planning during reconstruction. Experiments on Replica datasets demonstrate performance competitive with RGB-D methods. Our code and data are available at https://github.com/TrickyGo/ActMVS.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-02 - SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation

**Authors:** Qingpo Wuwu, Xiaobao Wei, Peng Chen, Nan Huang, Zhongyu Zhao, Hao Wang, Ming Lu, Ningning Ma, Shanghang Zhang
**Links:** [abs](https://arxiv.org/abs/2606.03909) - [pdf](https://arxiv.org/pdf/2606.03909)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic scene reconstruction, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, scene representation, rendering, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation
- 作者：Qingpo Wuwu, Xiaobao Wei, Peng Chen, Nan Huang, Zhongyu Zhao, Hao Wang, Ming Lu, Ningning Ma, Shanghang Zhang
- 出版日期：2026-06-02T17:06:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03909

### 一句话总结
SparseStreet 提出一种针对街景的3D高斯泼溅压缩框架，通过可学习剪枝和背景压缩实现高达80%的压缩比，在保持动态物体高保真度的同时显著降低存储和渲染开销。

### 研究问题
现有3D高斯泼溅方法在街景重建中需要大量高斯基元以捕捉细节，导致存储成本高和渲染速度慢，特别是动态物体（如车辆、行人）和静态背景之间存在冗余不均衡的问题。

### 核心思路/方法
1. **节点可学习剪枝策略**：系统地移除低贡献的高斯基元，同时保留视觉关键区域（如动态物体）。
2. **背景压缩**：在场景表示稳定后，进一步减少静态区域的冗余高斯基元。
3. 综合应用以上两步，在不显著降低质量的前提下，大幅压缩总高斯基元数量。

### 主要贡献
- 提出专门面向街景场景的通用压缩框架SparseStreet。
- 设计节点级可学习剪枝方法，保留动态物体几何与外观。
- 引入背景压缩策略，消除静态区域冗余。
- 在Waymo和nuScenes上实现最高80%压缩比，且质量损失极小。

### 与相关方法的关系
- **NeRF、Gaussian Splatting**：基于3D高斯泼溅（Gaussian Splatting）改进，而非NeRF；针对其高存储和低速度问题提出压缩方案。
- **动态场景重建方法**：专注于动态物体（车辆、行人）的高保真重建，与一般动态场景方法在技术路径上不同（侧重压缩而非建模）。
- **VGGT、DUSt3R、MASt3R、CroCo**：摘要未提供足够信息，无法判断关联。

### 局限性
摘要未提供足够信息，例如：未报告在极高压缩比下的具体质量损失指标（如PSNR/SSIM）、未讨论不同场景的鲁棒性、未给出实际渲染帧率或推理时间、未说明剪枝策略的训练稳定性和超参数敏感性。

### 阅读优先级
**高**
理由：论文针对3D高斯泼溅在街景重建中的实际部署瓶颈（存储和速度），提出有效压缩框架（80%压缩比），且实验结果来自主流数据集（Waymo、nuScenes），对从事自动驾驶、城区数字孪生和实时渲染的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting has shown promising results in street scene reconstruction, existing methods require massive numbers of Gaussian primitives to capture fine details, leading to prohibitive storage costs and slow rendering speeds. We observe that dynamic objects (e.g., vehicles and pedestrians) demand high-fidelity representations to maintain temporal consistency, while static background regions often contain substantial redundancy. Motivated by this, we propose SparseStreet, a general compression framework specifically designed for street scenes. First, we introduce a node-based learnable pruning strategy that systematically removes low-contributing Gaussian primitives while preserving visually critical regions. Second, after the scene representation stabilizes, we apply background compression, further reducing redundancy in static regions. Our method effectively preserves the geometry and appearance of dynamic objects while significantly reducing the total number of Gaussian primitives. Extensive experiments on the Waymo and nuScenes demonstrate that SparseStreet achieves up to 80% compression ratio with minimal quality degradation, enabling resource-efficient, high-fidelity dynamic scene reconstruction. Project website: https://sparsestreet.github.io/.

</details>

#### 2026-06-02 - MLP Splatting: Object-Centric Neural Fields

**Authors:** Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison
**Links:** [abs](https://arxiv.org/abs/2606.03877) - [pdf](https://arxiv.org/pdf/2606.03877)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MLP Splatting: Object-Centric Neural Fields
- 作者：Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03877

### 一句话总结
MLP-Splatting 使用多个紧凑的 MLP 作为空间局部化的光场基元，在实现照片级真实感新视角合成的同时，可通过少量基元选择实现对象级场景分解与编辑，且内存和渲染效率优于现有方法。

### 研究问题
如何获得一种既能提供照片级真实感新视角合成，又能轻松将场景分解为可编辑对象级基元的3D表示，从而避免额外的分割或分组步骤。

### 核心思路/方法
- 将场景表示为若干独立的紧凑 MLP（多层感知机），每个 MLP 具有局部空间支持，负责预测光线在该区域的 radiance（辐射度）和 opacity（不透明度）。
- 渲染时，通过稀疏体素合成（sparse volumetric compositing）沿光线与基元交互进行高效计算。
- 仅使用 RGB 监督训练，导致基元自动对应局部场景区域（常与对象或对象部分对应），从而无需分割掩码即可通过选择少量基元进行交互式对象级编辑。
- 可选语义特征蒸馏以支持开放词汇场景交互和开放集实例分割。

### 主要贡献
- 提出一种基于可学习、空间局部化的 MLP 基元的场景表示，兼具高表达能力和局部性。
- 实现无需额外分割掩码的对象级编辑能力，通过选择少量基元即可。
- 相比语义 3DGS 方法，内存使用降至 1/15，渲染速度提升至 3 倍。
- 可选语义蒸馏实现开放词汇交互与开放集实例分割。

### 与相关方法的关系
- **NeRF** 和 **Gaussian Splatting**：摘要明确指出 MLP-Splatting 与这两类方法对比——它们虽能实现照片级真实感新视角合成，但缺乏易于将场景分解为少量基元的能力。MLP-Splatting 通过局部 MLP 基元解决了此问题。
- **VGGT、DUSt3R、MASt3R、CroCo**：摘要未提供足够信息说明与这些方法的关系。
- **动态场景重建方法**：摘要未提供足够信息说明与动态场景重建方法的关系。

### 局限性
- 摘要未提供足够信息说明该方法在处理复杂遮挡、大尺度场景或极端视角时的表现。
- 未提及对非静态场景（动态场景）的适用性。
- 摘要未提供定量比较之外的失败案例或边界情况分析。

### 阅读优先级
**高**。
理由：该方法针对 NeRF / 3DGS 等主流方法缺乏对象级分解这一关键局限，提出了使用局部 MLP 基元的高效解决方案，在编辑能力、内存和速度上均有显著优势，并支持开放词汇交互。主题新颖且实用，适合对场景表示、新视角合成和三维交互感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

3D representations are fundamental to scene rendering, understanding, and interaction. Recent approaches, such as 3D Gaussian Splatting and Neural Radiance Fields, achieve impressive photorealistic novel-view synthesis, but lack the ability to easily decompose scene elements into a few primitives, requiring additional segmentation or grouping for object-level manipulation. We present MLP-Splatting, a method that enables scene decomposition via a few expressive light-field primitives while providing photorealistic novel-view synthesis. MLP-Splatting models each primitive as an independent compact MLP with localized spatial support that predicts radiance and opacity. In contrast to low-level Gaussian primitives or a single global radiance field, our neural primitives provide greater expressive capacity while remaining spatially localized. Rendering is performed through efficient sparse volumetric compositing over ray-primitive interactions. Our primitives are supervised using RGB supervision alone, which yields primitives that represent local scene regions often corresponding to objects or object parts, enabling interactive object-level editing without segmentation masks by selecting a handful of primitives. Our method, augmented with optional semantic feature distillation, enables open-vocabulary scene interaction and open-set instant segmentation. Compared to state-of-the-art methods, we achieve substantially lower memory usage (1/15$\times$) and faster rendering (3$\times$), as we show in our experiments compared to semantic 3DGS methods. Project Page: https://shinjeongkim.com/mlp-splatting

</details>

#### 2026-06-02 - GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation

**Authors:** Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li
**Links:** [abs](https://arxiv.org/abs/2606.03682) - [pdf](https://arxiv.org/pdf/2606.03682)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

好的，以下是根据您提供的论文元数据和摘要生成的简要分析。

### Metadata
- 标题：GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation
- 作者：Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li
- 出版日期：2026-06-02
- 分类：神经场景表示与渲染
- 链接：论文摘要: https://arxiv.org/abs/2606.03682, PDF: https://arxiv.org/pdf/2606.03682

### 一句话总结
本文提出了一个名为GN0的统一框架，通过构建大规模数据集GN-Matrix、高保真仿真平台和BEV基准GN-Bench，并利用RL驱动的导航基础模型BAE，旨在解决视觉语言导航（VLN）中数据稀缺和泛化能力不足的问题。

### 研究问题
视觉语言导航（VLN）系统面临数据规模和质量的限制，导致其泛化能力和长期任务执行能力不足。

### 核心思路/方法
1.  **数据生成**：策划多样化的3D场景，并开发自动化管线以生成大规模导航数据，构建GN-Matrix数据集。
2.  **仿真平台**：基于3D高斯泼溅引擎（3DGS），构建一个支持交互式漫游和碰撞感知导航的高保真模拟平台。
3.  **评估基准**：提出首个基于鸟瞰图（BEV）的基准GN-Bench，该基准集成了动态3DGS化身用于人机交互评估。
4.  **策略学习**：开发一个名为BAE（Break and Establish）的RL驱动的导航基础模型。该模型先进行监督学习，然后通过DAgger算法处理rollout产生的状态，以打破狭窄的专家中心化分布，并启用下游的强化学习探索。
5.  **统一范式**：GN0将基于地图和无地图的任务（如指令跟随、人类跟随、目标导航）统一在一个框架内。GN-BAE将高保真3DGS渲染的BEV表示形式化为紧凑记忆，以解锁视觉语言模型（VLM）中的潜在空间推理能力。

### 主要贡献
1.  提出了一个统一的数据、仿真和学习框架GN0，用于推进具身导航的研究与应用。
2.  创建了大规模导航数据集GN-Matrix和基于3DGS的高保真仿真平台。
3.  提出了首个包含动态3DGS化身的BEV基准GN-Bench。
4.  开发了名为BAE的RL驱动导航基础模型。
5.  在GN-Bench和VLN-CE基准上，GN0的性能超越了现有的最先进VLN方法。

### 与相关方法的关系
- **NeRF**：摘要提及该方法使用了**3D高斯泼溅（3DGS）**引擎作为仿真核心，这与NeRF类似，但采用了不同的场景表示技术（高斯泼溅而非神经辐射场）。
- **Gaussian Splatting**：本文的仿真平台和GN-Bench基准中的动态化身均基于3DGS构建，是其核心组件。
- **VGGT、DUSt3R、MASt3R、CroCo**：这些论文与方法主要涉及3D结构重建或跨视角匹配。虽然它们可能与VLN中的场景理解相关，但**摘要未提供足够信息**以说明GN0与这些特定方法的关系或对比。
- **动态场景重建方法**：GN-Bench基准中包含了“动态3DGS化身”，这需要处理动态对象，因此与动态场景重建方法相关。然而，**摘要未提供足够信息**来详细阐述GN0在动态重建方面的具体技术细节或与其区别。

### 局限性
- **摘要未提供足够信息**：摘要未提及该方法的计算复杂度、实时性、对复杂环境（如遮挡严重或光照剧烈变化）的鲁棒性，以及BAE模型训练的具体收敛情况和数据规模扩充后的性能边际效应。也未讨论其失败案例或潜在的偏差问题。

### 阅读优先级
**高**

**理由**：该工作提出了一套非常完整的端到端VLN系统，涵盖数据、仿真、评估和策略学习四大核心环节，并在多个基准上取得了SOTA性能。对于从事具身智能、机器人导航、视觉语言学习的研究人员，这是一个具有重大参考价值的系统性工作。其提出的数据集、基准和训练范式可能成为该领域社区的重要基础设施。

</details>

<details>
<summary>Abstract</summary>

Embodied navigation connects intelligent agents with the physical world and is fundamental for general robotic intelligence. Limited availability and quality of navigation data have constrained Vision-and-Language Navigation (VLN) systems' generalization and long-horizon capabilities. To address this, we curate diverse 3D scenes and develop an automated pipeline for large-scale navigation data, resulting in the GN-Matrix dataset. Building on a 3D Gaussian Splatting (3DGS) engine, we introduce a high-fidelity simulation platform supporting interactive roaming and collision-aware navigation. We further propose GN-Bench, the first BEV-based benchmark incorporating dynamic 3DGS avatars for human-robot interaction evaluation. To leverage the simulator, we develop an RL-driven navigation foundation model, Break and Establish (BAE). After supervised learning, DAgger exposes the model to rollout-induced states, breaking narrow expert-centric distributions and enabling downstream RL exploration. This unified VLN paradigm integrates map-based and map-free tasks, including instruction following, human following, and goal navigation. GN-BAE formalizes high-fidelity 3DGS-rendered Bird's Eye View representations as compact memory, unlocking latent spatial reasoning in VLMs. Extensive evaluations on GN-Bench and VLN-CE show that GN0 outperforms state-of-the-art VLN methods. Overall, GN-Matrix offers a unified framework spanning data, simulation, and learning, advancing embodied navigation in research and industrial applications.

</details>

#### 2026-06-02 - UnsOcc: 3D Semantic Occupancy Prediction in Unstructured Scene via Rendering Fusion

**Authors:** Ye Wu, Ruiqi Song, Baiyong Ding, Nanxin Zeng, Junjie Cheng, Yunfeng Ai
**Links:** [abs](https://arxiv.org/abs/2606.03581) - [pdf](https://arxiv.org/pdf/2606.03581)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UnsOcc: 非结构化场景下基于渲染融合的三维语义占据预测
- 作者：Ye Wu, Ruiqi Song, Baiyong Ding, Nanxin Zeng, Junjie Cheng, Yunfeng Ai
- 出版日期：2026-06-02
- 分类：神经场景表示与渲染
- 链接：https://arxiv.org/abs/2606.03581

### 一句话总结
本文提出UnsOcc，一种针对非结构化场景（如露天矿）的多模态三维语义占据预测框架，通过渲染融合模块和基于高斯泼溅的细节感知辅助监督，提升跨模态对齐和长尾类别预测性能。

### 研究问题
非结构化场景中，场景稀疏性阻碍有效的跨模态融合，且长尾分布更严重，导致现有三维语义占据预测方法性能下降。

### 核心思路/方法
1. 构建专用非结构化场景数据集（露天矿）。
2. 提出渲染融合模块（RenderFusion），通过双向渲染监督增强跨模态特征对齐。
3. 提出基于高斯泼溅的细节感知辅助监督（GSRefinement），将稀疏三维占据预测投影为密集二维语义分割图，实现对长尾类别的有效监督。

### 主要贡献
- 提出首个面向非结构化场景的多模态三维语义占据预测框架UnsOcc。
- 设计RenderFusion模块，利用渲染监督改善跨模态融合。
- 提出GSRefinement方法，通过高斯泼溅投影提供长尾类别监督。
- 在露天矿数据集和nuScenes数据集上超越现有最先进方法。

### 与相关方法的关系
- 与NeRF/Gaussian Splatting的关系：本文使用**高斯泼溅**（Gaussian Splatting）作为辅助监督手段（GSRefinement），将其生成的密集语义图用于监督稀疏占据预测；未提及与NeRF的直接对比或融合。
- 与VGGT、DUSt3R、MASt3R、CroCo的关系：摘要未提供足够信息。
- 与动态场景重建方法的关系：摘要未提供足够信息。

### 局限性
摘要未提供关于计算效率、实时性、对恶劣光照/天气的鲁棒性、以及长尾类别具体性能增益的详细信息。

### 阅读优先级：中
理由：该方法针对特定应用场景（非结构化环境如矿山）设计，技术贡献明确（渲染融合+高斯泼溅辅助监督），但方法通用性和效率细节不足，适合对该细分领域感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

Unstructured scenes present unique challenges for autonomous driving, as irregular obstacles and sparse scene layouts undermine the effectiveness of traditional perception methods such as 3D object detection. 3D semantic occupancy prediction has emerged as a prominent focus due to its ability to provide dense spatial representations by assigning semantic labels to individual voxels in 3D space. However, directly applying 3D semantic occupancy prediction to unstructured scenes remains challenging because scene sparsity hinders effective cross-modal fusion and the more severe long-tail distribution in these scenarios further degrades prediction performance. To validate the effectiveness of our approach, we construct a dedicated dataset of unstructured scenes collected from open-pit mines. Based on this, we propose UnsOcc, a multi-modal 3D semantic occupancy prediction framework that improves robustness in unstructured environments. At its core, we introduce a rendering-based fusion module, RenderFusion, which enhances cross-modal feature alignment through bidirectional rendering supervision. Furthermore, we propose GSRefinement, a detail-aware auxiliary supervision method based on Gaussian Splatting that projects sparse 3D occupancy predictions into dense 2D semantic segmentation maps, enabling effective supervision for long-tail categories. Extensive experiments on both the open-pit mine dataset and the nuScenes dataset demonstrate that our method significantly outperforms existing state-of-the-art approaches.

</details>

#### 2026-06-02 - Characterizing Detectability in 3DGS Poisoning: A Stage-wise Benchmark

**Authors:** Quoc-Anh Bui-Huynh, Thanh Duc Ngo, Xue Geng, Kaixin Xu, Wang Zhe, Xulei Yang, Ngai-Man Cheung
**Links:** [abs](https://arxiv.org/abs/2606.03499) - [pdf](https://arxiv.org/pdf/2606.03499)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Characterizing Detectability in 3DGS Poisoning: A Stage-wise Benchmark
- 作者：Quoc-Anh Bui-Huynh, Thanh Duc Ngo, Xue Geng, Kaixin Xu, Wang Zhe, Xulei Yang, Ngai-Man Cheung
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03499

### 一句话总结
本文提出了一个面向3D高斯泼溅（3DGS）投毒检测的分阶段基准（Poison-3DGS），系统地分析了不同攻击在重建流水线各阶段的可检测性，揭示检测效果高度依赖于信号出现阶段。

### 研究问题
针对3DGS容易遭受多种投毒攻击（如幻觉物体注入、计算开销放大、事后水印嵌入）但防御检测研究不足的现状，从检测视角出发，研究以下核心问题：如何系统地表征和评估投毒攻击在3DGS多阶段重建流水线中的可检测性，特别是不同攻击在不同阶段产生的法医信号分布规律。

### 核心思路/方法
1.  **识别核心挑战**：3DGS重建流水线具有多阶段特性（生成多视角图像、几何体、训练动态、高斯参数），这导致攻击在不同阶段会留下异质性中间表征，法医信号具有阶段依赖性。
2.  **构建基准**：提出Poison-3DGS基准，该基准公开了多种场景和攻击类型下各流水线阶段的专有伪影（包括多视角图像、几何体、训练动态、高斯参数）。
3.  **系统性研究**：利用该基准，对不同攻击类型在流水线各阶段的可检测性进行系统性分析，比较各阶段的检测效果差异。

### 主要贡献
1.  提出并发布了第一个专门用于3DGS投毒检测的**分阶段基准（Poison-3DGS）**。
2.  首次**系统性地表征了3DGS中与阶段相关的可检测性**，揭示了可检测性在不同阶段差异显著，且没有一个单一阶段对所有攻击类型普遍最优。
3.  发现不同攻击会产生**不同阶段的特异性法医信号**，例如训练动态和高斯参数统计量等后期信号能提供早期阶段无法观测到的强检测线索。

### 与相关方法的关系
摘要未提供足够信息。本文主要关注3DGS的投毒攻击检测，与NeRF、Gaussian Splatting等相关，但未提及与VGGT、DUSt3R、MASt3R、CroCo、动态场景重建方法的具体关系。

### 局限性
摘要未提供足够信息。具体实验层面（如使用的数据集规模、具体攻击方法数量、防御检测算法的性能量化结果等）的局限性未在摘要中描述。

### 阅读优先级
**高**
理由：3DGS是当前实时视图合成的主流技术，但其安全性（尤其是防御检测）是开放且前沿的问题。本文首次构建了系统的分阶段检测基准并发布，对后续研究鲁棒3DGS系统具有重要的基础性支撑价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has rapidly emerged as a leading representation for real-time novel view synthesis, but recent work shows it is vulnerable to diverse poisoning attacks, including illusory object injection, computation cost amplification, and post hoc model watermarking. Despite this expanding threat surface, existing studies focus mainly on attack success, while defense and detection remain underexplored. From a detection perspective, a key challenge and opportunity arise from the multi-stage nature of the 3DGS reconstruction pipeline, which produces heterogeneous intermediate representations. Forensic signals for detecting poisoning are inherently stage dependent: an attack introduced at one stage may produce signals that emerge only at later stages. This motivates a stage-wise view of detectability that goes beyond single-stage evaluation. We introduce Poison-3DGS, a benchmark for stage-wise characterization of poisoning detection in 3DGS. It exposes stage-specific artifacts, including multi-view images, geometry, training dynamics, and Gaussian parameters, across a diverse set of scenes and attacks. Using it, we conduct a systematic study of detectability across pipeline stages. Our analysis reveals several insights. First, detectability varies significantly across stages, and no single stage consistently dominates across attack types. Second, different attacks exhibit distinct stage-specific forensic signals, so detection effectiveness depends critically on where signals are observed. Third, later-stage signals such as training dynamics and Gaussian parameter statistics provide strong cues not observable at earlier stages. Overall, our work provides a principled benchmark and the first systematic characterization of stage-dependent detectability in 3DGS, offering a foundation for future research on robust and reliable 3DGS systems.

</details>

#### 2026-06-02 - FreeStreamGS: Online Feed-forward 3D Gaussian Splatting from Unposed Streaming Inputs

**Authors:** Ruiyang Chen, Feiran Li, Chu Zhou, Zonglin Li, Zhanyu Ma, Heng Guo
**Links:** [abs](https://arxiv.org/abs/2606.03254) - [pdf](https://arxiv.org/pdf/2606.03254)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) allows efficient and high-fidelity novel view synthesis (NVS) from an offline recorded image sequence. However, achieving online NVS from streaming and unposed image inputs remains challenging. Although online feed-forward geometric estimation methods have been proposed for streaming depth and point cloud recovery, they cannot be adapted to NVS due to severe rendering artifacts. This is because NVS demands stricter multi-view consistency in Gaussian scales and pose-geometry alignment; even minor deviations would accumulate over time and visibly degrade rendering quality. To this end, we propose FreeStreamGS, a robust online feed-forward framework for efficient and high-quality NVS. We introduce two key mechanisms: a Decoupled Intrinsic Recovery Head that removes cumulative camera intrinsic bias and prevents scene scale jitter during long-term streaming, and a Dynamic Point Refinement Offset strategy that relaxes rigid unprojection to correct coupled pose-depth drift. Extensive experiments show that FreeStreamGS achieves rendering quality competitive with state-of-the-art offline feed-forward 3DGS methods, despite operating without access to future frames.

</details>

#### 2026-06-02 - KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis

**Authors:** Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy
**Links:** [abs](https://arxiv.org/abs/2606.03120) - [pdf](https://arxiv.org/pdf/2606.03120)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel view synthesis by representing scenes as collections of anisotropic Gaussians optimized via differentiable rasterization. However, standard pixel-space losses (L1, SSIM) constrain only aggregate reconstruction error, permitting the optimization to redistribute error across frequency scales. This leads to oversmoothing and structural artifacts, particularly in sparse-view settings where supervision is limited. We propose KC-3DGS, which augments 3DGS training with wavelet-domain supervision based on natural image statistics. Our method combines three components: (1) a multi-scale wavelet coefficient alignment loss that explicitly penalizes missing high-frequency detail, (2) a supervised kurtosis concentration loss that encourages rendered images to match the heavy-tailed frequency statistics of ground-truth images, and (3) a cross-band covariance penalty that promotes frequency specialization. We provide theoretical analysis showing that pixel-space losses admit a family of indistinguishable perturbations under wavelet redistribution, and that our joint objective excludes degenerate solutions. Experiments across MipNeRF360, Tanks&Temples, MVImgNet, DeepBlending, and WRIVA-ULTRRA demonstrate consistent improvements in perceptual quality. On the challenging WRIVA-ULTRRA outdoor dataset, KC-3DGS achieves a 9.48% improvement in DreamSim while also improving PSNR, SSIM, and LPIPS. In sparse-view settings with only 12 training images, our method improves PSNR by up to 0.5 dB on MipNeRF360 while maintaining perceptual quality. The approach integrates seamlessly into existing 3DGS pipelines as a plug-and-play regularization strategy.

</details>

#### 2026-06-01 - The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset

**Authors:** Richard Schwarzkopf, Fabian Immel, Alexander Blumberg, Jonas Merkert, Nils Rack, Kaiwen Wang, Fabian Konstantinidis, Julian Truetsch, Carlos Fernandez, Annika Bätz, Kevin Rösch, Marlon Steiner, Willi Poh, Yinzhe Shen, Royden Wagner, Felix Hauser, Dominik Strutz, Jaime Villa, Gleb Stepanov, Holger Caesar, Ömer Şahin Taş, Frank Bieder, Jan-Hendrik Pauls, Christoph Stiller
**Links:** [abs](https://arxiv.org/abs/2606.02956) - [pdf](https://arxiv.org/pdf/2606.02956)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, novel view synthesis, view synthesis, embodied AI, autonomous driving, localization

<details>
<summary>Abstract</summary>

Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity. We present KITScenes Multimodal, a European dataset built around high-fidelity sensors and maps. Our fully synchronized sensor suite combines high-resolution global-shutter cameras, long-range lidar beyond 400m, 4D imaging radar, and redundant GNSS/INS localization. Our HD maps are, to our knowledge, the most complete of any sensor dataset, validated through autonomous driving trials on open-source software. For the first time in a public dataset, all driving-relevant traffic elements, such as traffic lights, are mapped in 3D to a reprojection-accurate level with full topological connectivity. Recorded in cities with irregular street layouts and mixed traffic modes, our dataset complements existing datasets by broadening the available geographic diversity. We also introduce four benchmarks, each advancing spatial learning for embodied AI: online HD map construction, long-range depth estimation, novel view synthesis, and end-to-end driving. Project page: https://kitscenes.com/

</details>

#### 2026-06-01 - VEDAL: Variational Error-Driven Asynchronous Learning for 3D Gaussian Splatting Pruning

**Authors:** Aoduo Li, Jiancheng Li, Huan Ye, Hongjian Xu, Shiting Wu, Xiujun Zhang, Zimeng Li, Xuhang Chen
**Links:** [abs](https://arxiv.org/abs/2606.02346) - [pdf](https://arxiv.org/pdf/2606.02346)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves remarkable novel view synthesis quality with real-time rendering, yet suffers from excessive memory consumption due to millions of Gaussian primitives. Existing pruning methods rely on heuristic importance scores or synchronous batch updates, leading to suboptimal compression and training instability. We propose VEDAL, a principled framework that formulates Gaussian pruning as variational free energy minimization. Our approach introduces (1) a prediction-error gating mechanism that asynchronously activates pruning based on per-Gaussian reconstruction uncertainty, and (2) a variational uncertainty head that models pruning decisions as latent variables with learnable priors. The free energy objective naturally balances reconstruction fidelity against model complexity through an information-theoretic lens. Extensive experiments on Mip-NeRF 360, Tanks&Temples, and Deep Blending demonstrate that VEDAL achieves 5.2x compression with only 0.31 dB PSNR drop, outperforming PUP 3D-GS by +0.05 dB at a higher compression ratio and LightGaussian by +0.35 dB at comparable quality, while maintaining real-time rendering at 185 FPS.

</details>

#### 2026-06-01 - Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image

**Authors:** Kaidi Zhang, Guanxu Zhu
**Links:** [abs](https://arxiv.org/abs/2606.02068) - [pdf](https://arxiv.org/pdf/2606.02068)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

Recently, novel view synthesis has witnessed remarkable progress, with mainstream methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) delivering impressive results. However, these approaches often struggle to balance rendering speed and model size, and their optimization-based training can be highly time-consuming. Furthermore, they typically rely on dense observations, often failing to produce satisfactory results under sparse-view conditions. Although feed-forward reconstruction significantly reduces the optimization time of 3DGS, its pixel-aligned formulation generates millions of Gaussians from a single image, severely limiting its practical deployment on mobile devices. To address these limitations, we revisit the Multiplane Image(MPI) representation, which represents scenes using a compact set of planar layers for efficient novel view synthesis. Leveraging recent advances in visual foundation models, we utilize predicted point maps for reliable geometric initialization, followed by differentiable optimization. To address the issues of holes and artifacts in sparsely initialized MPI, we introduce one-step diffusion, which participates in both the differentiable optimization of MPI and the postprocessing of rendering results. Compared with a representative GS-based method, our approach is 30.7% faster and uses only 14.8% of its model size, while achieving competitive synthesis quality on front-view scenarios

</details>

#### 2026-06-01 - Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects

**Authors:** Jens U. Kreber, Lukas Mack, Joerg Stueckler
**Links:** [abs](https://arxiv.org/abs/2606.01950) - [pdf](https://arxiv.org/pdf/2606.01950)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, splatting, manipulation, simulation, world model

<details>
<summary>Abstract</summary>

World models enable intelligent agents to predict the consequences of their actions on the environment. In this paper, we propose Multi Rigid Object Gaussian World Model (MRO-GWM), a novel model that learns action-conditional dynamics of rigid objects in 3D. By representing the scene by object-centric Gaussians, we can represent arbitrary object shapes and multi-object scenes. We develop a novel spatio-temporal transformer architecture that predicts future rigid body motion from a history of object Gaussians and future actions. Objects are represented by their Gaussians in a canonical frame, which allows for describing object motion as rigid body transformation. Our model is trained on reconstructions from multiple viewpoints, which requires the model to handle partial observations of objects due to occlusions. We analyze prediction performance of our approach on synthetic datasets composed of typical household objects with multi-object dynamics and interactions by a robot end effector. We also evaluate our model in model-predictive control for non-prehensile manipulation in simulation.

</details>

#### 2026-06-01 - Effective Multi-sensor Conditioning for Street-view Novel-view Synthesis

**Authors:** Zhengfei Kuang, Adam Sun, Liyuan Zhu, Tong Wu, Shengqu Cai, Jonathan Tremblay, Iro Armeni, Ehsan Adeli, Lior Yariv, Gordon Wetzstein
**Links:** [abs](https://arxiv.org/abs/2606.01590) - [pdf](https://arxiv.org/pdf/2606.01590)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** metric depth, novel view synthesis, view synthesis, rendering, driving scene

<details>
<summary>Abstract</summary>

Modern vehicle platforms are equipped with a rich sensor suite, including LiDAR, calibrated multi-camera rigs, and accurate ego-motion, that in principle offers strong signal for re-rendering a driving scene from novel viewpoints. A growing line of recent work leverages video diffusion models for this task, using their generative priors to synthesize plausible novel views from sparse vehicle observations. In practice, however, existing methods exploit only a fragment of this signal, and their quality tends to degrade as the target trajectory departs from the recorded driving path. We argue that this is fundamentally a multi-sensor fusion problem: sparse LiDAR reprojections supply accurate but incomplete metric geometry, surround-view reference imagery supplies dense appearance but no metric depth, and camera poses tie the two together across views. We introduce StreetNVS, a video diffusion framework that jointly conditions on all three signals through a Reference-Enhanced Camera Attention module based on a relative ray-level positional encoding. We develop a two-stage curriculum training strategy that gradually exposes the model to increasingly sparse LiDAR. On the Waymo Open Dataset, StreetNVS substantially outperforms state-of-the-art baselines under sparse LiDAR conditioning, matches methods that rely on 10-100 times denser point clouds. We further show capabilities of synthesizing coherent videos along extreme out-of-trajectory paths such as elevation, lane-shift, pullback, and rotation. Our website: https://streetnvs.github.io

</details>

### 2026-05

#### 2026-05-31 - LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World

**Authors:** Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang, Mac Schwager
**Links:** [abs](https://arxiv.org/abs/2606.01458) - [pdf](https://arxiv.org/pdf/2606.01458)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, manipulation, simulation

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) policies for humanoid loco-manipulation is constrained by the high cost and complexity of collecting human teleoperation demonstrations. VLA policies fine-tuned in simulators have, until now, failed to transfer effectively in humanoid loco-manipulation tasks. We present LEGS (Loco-manipulation via Embodied Gaussian Splatting), a hybrid simulator that composites a mesh foreground (robot, objects, props) over a photorealistic 3D Gaussian Splatting (3DGS) background reconstructed from a handheld scene capture. LEGS uses a procedural motion-primitive generator to synthesize labeled demonstrations at scale without human teleoperation, and a deterministic two-stage color calibration to align the rendered 3DGS image to the robot's deployment camera. On a Unitree G1 humanoid robot, across three pick-and-place tasks of increasing whole-body difficulty and three VLA backbones (psi_0, pi_0.5, GR00T N1.6), a policy trained purely on LEGS data matches or exceeds one trained on human teleoperation demos on every experiment. It also outperforms a mesh-only simulation baseline that ablates the effect of the 3DGS background, showing that photorealistic rendering is a key enabler for synthetic data transfer. Humanoid motion is recorded independently of scene appearance in LEGS, allowing the same auto-generated demonstrations to be re-rendered under new backgrounds and object meshes--covering a new scene at more than 15x lower cost than teleoperation--to augment training data for robustness to scene variations. Under combined object-and-scene appearance shift, the policy trained on re-rendered LEGS-AUG data maintains task success while the baseline trained on teleoperation data fails entirely. Our project page is located at https://legsvla.github.io/.

</details>

#### 2026-05-31 - RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation

**Authors:** Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang
**Links:** [abs](https://arxiv.org/abs/2606.01261) - [pdf](https://arxiv.org/pdf/2606.01261)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, digital twin, simulation

<details>
<summary>Abstract</summary>

Real-scene indoor millimeter-wave simulation requires efficient modeling of radio frequency (RF)-computable geometry and electromagnetic material properties. To address the low efficiency of manual scene modeling, the limited RF adaptability of visually reconstructed meshes, and the lack of material binding in 28 GHz ray-tracing simulation, RFDT-Channel is developed as an RF digital twin scene construction workflow based on red-green-blue (RGB) images and light detection and ranging (LiDAR) point clouds. Indoor videos and point clouds are collected by a Jetson Orin platform with LiDAR and GMSL cameras. An initial triangular mesh is generated through COLMAP, 3D Gaussian Splatting, and SuGaR. The LiDAR point cloud then provides geometric and scale references for RF-oriented regularization in Blender, including alignment, wall solidification, door/window opening construction, and topology repair. OpenScene semantic segmentation maps major indoor structures to concrete, glass, wood, and metal materials, and Sionna RT performs 28 GHz ray tracing. Under a fixed transmitter-receiver deployment, the generated channel impulse response (CIR), channel frequency response (CFR), and Radio Map results show that material binding mainly changes weak reflection, transmission, and scattering paths, reducing the number of effective paths from about 742 to about 52 while keeping the dominant path amplitude nearly unchanged.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-02 - OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs

**Authors:** Yifei Li, Pengyiang Liu, Yuhang Zang, Zhongyue Shi, Qi Fu, Hongye Hao, Jiwen Lu
**Links:** [abs](https://arxiv.org/abs/2606.03890) - [pdf](https://arxiv.org/pdf/2606.03890)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, autonomous driving, mapping, AR, simulation, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs
- 作者：Yifei Li, Pengyiang Liu, Yuhang Zang, Zhongyue Shi, Qi Fu, Hongye Hao, Jiwen Lu
- 出版日期：2026-06-02T16:51:32Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03890

### 一句话总结
本文提出了一个用于评估多模态大模型（MLLMs）在连续第一人称视角下空间推理能力的分层基准OVO-S-Bench，实验显示当前最强模型落后人类专家27个百分点，其中“异中心映射”是主要瓶颈。

### 研究问题
如何系统评估多模态大模型在流式（连续、实时）第一人称视频输入中的空间智能，特别是对当前视野之外的空间结构和布局进行推理的能力？

### 核心思路/方法
1.  **数据集构建**：基于348个源视频，由12名训练有素的标注员经过约804小时多轮质量保证，人工标注了1680个问题，每个问题都附带查询时间戳和证据区间。
2.  **评估范式**：模型在评估时只能看到查询时间戳之前的视频片段（即流式前缀），不能看到完整视频。
3.  **分层问题设计**：将问题分为四个抽象层级：瞬时自我中心感知、时空上下文跟踪、空间模拟与推理、异中心映射。
4.  **模型评估**：在38个专有和开源MLLM上测试，并对比人类专家表现。

### 主要贡献
1.  **新基准和数据集**：提出了OVO-S-Bench，一个完全人工标注、专为流式空间智能设计的基准和数据集。
2.  **系统性评估**：对大量MLLM进行了评估，揭示了现有模型在流式空间推理方面的显著不足。
3.  **关键发现**：
    - 当前最强模型Gemini-3.1-Pro得分为59.2，而人类专家为86.6，差距达27分。
    - “异中心映射”是所有模型的主要瓶颈。
    - 专门进行流式和空间微调的MLLM性能反而低于其基础骨干模型。
    - 当思维链推理未基于流式输入时，会放大空间错误。

### 与相关方法的关系
摘要未提供足够信息。未提及与VGGT、DUSt3R、MASt3R、CroCo、NeRF、Gaussian Splatting、动态场景重建方法的关系。

### 局限性
摘要未提供足够信息。从文本推断，可能存在的局限性包括：基准仅覆盖特定类型的视频和场景；仅评估了固定时间前缀下的推理，未涉及更复杂的交互式或主动感知设置；未深入分析模型在不同空间推理层级上的具体失败模式（但指出了主要瓶颈）。

### 阅读优先级
**高**。
理由：该工作为评估多模态大模型在具身智能、增强现实等核心应用场景（连续流式空间推理）中的能力提供了一个急需的、经过严格标注的基准。其关键发现（如异中心映射是瓶颈、专用微调反而降低性能等）对领域研究有重要指导意义，有助于识别当前MLLM在该方向的核心弱点。

</details>

<details>
<summary>Abstract</summary>

Multimodal agents in robotics, AR, and autonomous driving must reason about places and layouts from continuous egocentric streams, often using evidence outside the current view. Existing benchmarks either evaluate offline over full videos or target events rather than spatial structure. We introduce OVO-S-Bench, a fully human-annotated benchmark for streaming spatial intelligence, comprising 1,680 questions over 348 source videos. Annotation involves 12 trained annotators, each also serving as a blind cross-reviewer, across roughly 804 person-hours of multi-round quality assurance. Each question carries a query timestamp and an evidence interval, and at evaluation, the model sees only the prefix preceding the query. Questions span four levels of increasing abstraction: instantaneous egocentric perception, spatiotemporal context tracking, spatial simulation and reasoning, and allocentric mapping. Across 38 proprietary and open-source MLLMs, Gemini-3.1-Pro trails human experts by 27 points, 59.2 vs. 86.6, with allocentric mapping as the dominant bottleneck. Notably, streaming and spatially fine-tuned MLLMs underperform their own backbones. We further find that chain-of-thought reasoning amplifies spatial errors when ungrounded in the stream. By exposing these limitations, OVO-S-Bench establishes a demanding testbed for next-generation streaming spatial MLLMs.

</details>

#### 2026-06-02 - A 3D Isovist World Model -- Revealing a City's Unseen Geometry and Its Emergent Cross-City Signature

**Authors:** Xuhui Lin, Stephen Law, Nanjiang Chen, Kunyao Li, Tao Yang
**Links:** [abs](https://arxiv.org/abs/2606.03609) - [pdf](https://arxiv.org/pdf/2606.03609)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A 3D Isovist World Model -- Revealing a City's Unseen Geometry and Its Emergent Cross-City Signature
- 作者：Xuhui Lin, Stephen Law, Nanjiang Chen, Kunyao Li, Tao Yang
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications（具身/机器人/增强现实应用）
- 链接：摘要: https://arxiv.org/abs/2606.03609, PDF: https://arxiv.org/pdf/2606.03609

### 一句话总结
本文提出一种基于3D等视域（isovist）的具身世界模型，通过预测导航几何结构而非外观，发现单城市训练的模型能学习到跨城市的空间特征。

### 研究问题
现有世界模型主要预测场景外观（如照片真实感渲染），或使用鸟瞰图占据网格压缩三维环境，忽略了可导航空间的立体结构（如地面以上及多层空间）和光照信息。问题是如何构建一个既无光度纠缠、又不丢失三维信息的可导航几何预测目标。

### 核心思路/方法
1. **3D等视域编码**：将开放体积（建筑间负面空间）编码为球形可见性深度图，记录每个方向到最近表面的距离。
2. **深度残差预测**：将下一等视域的预测公式化为深度残差，使解码器保留建筑边缘等锐利几何特征。
3. **自回滚调度采样**：训练时使用自回滚调度采样，使被破坏的上下文保持在几何流形上。
4. **持久潜在鸟瞰空间地图**：配备跨路径一致性的潜在空间图，以维持路径一致性。
5. **跨城市实验**：仅在曼哈顿和巴黎上训练一个城市盲模型，发现其时间潜伏可线性解码出城市身份，且显著高于单帧基线。

### 主要贡献
1. 提出以3D等视域作为具身世界模型的预测目标，避免光度纠缠并保留完整导航几何。
2. 设计深度残差预测、自回滚调度采样和持久潜在空间图，实现高质量几何预测。
3. **意外发现**：单城市训练模型产生跨城市空间特征，城市身份可从动力学潜伏中解码，表明该特征存在于学习动态而非外观。
4. 轻量、可解释、可复现的几何表示，并开源数据集和流程。

### 与相关方法的关系
摘要未提供与VGGT、DUSt3R、MASt3R、CroCo的对比信息。与NeRF和Gaussian Splatting的关系：本文明确不预测外观（光度），而NeRF和Gaussian Splatting主要关注光度真实感渲染，因此核心目标不同。动态场景重建方法：本文模型通过动作预测下一等视域，隐含处理动态场景，但摘要未具体讨论动态复现细节。

### 局限性
摘要未提供足够信息，无法从正文中得知具体局限性，例如模型对大规模场景的可扩展性、对稀疏输入的敏感性，或跨城市泛化能力的具体边界。建议阅读全文以获取详细信息。

### 阅读优先级
**中**  
理由：论文提出新颖的等视域几何表示和跨城市空间特征发现，对具身AI和机器人导航有潜在价值。但与其主要竞争对手（如预测外观的世界模型或传统鸟瞰图方法）的定量对比未在摘要中提供，且实验细节缺失，因此优先级为中等，适合对几何导航或城市分析感兴趣的读者进一步查阅。

</details>

<details>
<summary>Abstract</summary>

Embodied agents that navigate cities rely on world models that predict how their surroundings will change as they move. But for navigation, what matters is not what the buildings look like; it is where the agent can go. Most world models nonetheless predict appearance, learning how a scene looks rather than the space an agent can move through. Those that do target geometry, such as bird's-eye-view occupancy grids, flatten the three-dimensional environment onto a ground plane, discarding the above-ground and multi-level structure that shapes real navigation. What is missing is a predictive target that captures the navigable geometry an agent actually traverses, without photometric entanglement and without collapsing the third dimension. Our key idea is to model the open volume between buildings, the negative space, encoded as a 3D isovist: a spherical visibility-depth map recording the distance to the nearest surface in every direction. We introduce an embodied world model that predicts the next isovist from a short history of past isovists and a movement action. The prediction is formulated as a depth residual so the decoder inherits sharp building edges, trained with self-rollout scheduled sampling to keep corrupted context on the geometry manifold, and equipped with a persistent latent bird's-eye-view spatial map for cross-path consistency. Our central finding is emergent and unexpected: a single city-blind model trained on Manhattan and Paris develops a cross-city spatial signature, with city identity linearly decodable from its temporal latents far above single-frame baselines, so the signature lives in the learned dynamics rather than in appearance. The representation is lightweight, interpretable, and reproducible, offering a geometric substrate for spatial reasoning in embodied AI, robotics, and urban analysis, released with an open dataset and pipeline.

</details>

#### 2026-06-02 - TASE: Truncation-Aware Semantic Embeddings for 3D Scene Understanding and Editing

**Authors:** Tim-Felix Faasch, Jochen Kall, Lucas Nunes, Jens Behley, Cyrill Stachniss
**Links:** [abs](https://arxiv.org/abs/2606.03314) - [pdf](https://arxiv.org/pdf/2606.03314)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, autonomous driving, simulation, scene understanding

<details>
<summary>Abstract</summary>

High-fidelity semantic 3D scene representations are crucial for numerous applications, including robotics, autonomous driving, and simulation. Beyond this, the ability to edit such representations enables developers to adapt these applications more easily to specific target scenarios. Current approaches provide limited support for controllable editing. We introduce TASE, a method that projects pretrained 2D semantic features into a truncation-aware embedding space to enable flexible 3D scene editing. Our method explicitly optimizes a feature space in which progressively reducing feature channels yields increasingly abstract semantic representations, while retaining more channels preserves fine-grained detail. Additionally, we improve multi-view consistency of the features using a scale- and translation-equivariance loss. The resulting truncation-aware embedding space enables text-driven edits to 3D scenes, providing explicit control over how strongly edits adhere to the original scene content and allowing more substantial modifications than prior methods. Moreover, we propose a finetuning stage for the editing diffusion model to mitigate artifacts caused by geometric changes. Experimental results demonstrate competitive performance in 3D scene editing, substantially outperforming prior methods on edits involving large geometric modifications.

</details>

#### 2026-06-02 - GeoSem-WAM: Geometry- and Semantic-Aware World Action Models

**Authors:** Fulong Ma, Daojie Peng, Wenjun Yue, Jiahang Cao, Bintao Wang, Qiang Zhang, Jun Ma
**Links:** [abs](https://arxiv.org/abs/2606.03188) - [pdf](https://arxiv.org/pdf/2606.03188)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding, world modeling

<details>
<summary>Abstract</summary>

Recent World Action Models (WAMs) have demonstrated impressive capabilities in embodied decision-making. However, whether their effectiveness stems from explicit future imagination during inference or representation learning induced by predictive training remains an open question. Emerging evidence suggests the primary advantage lies in learning robust latent representations rather than generating future observations at test time. Nevertheless, existing WAMs mainly rely on RGB-based future prediction, which provides limited structural and spatial understanding of complex environments. To address this, we propose a structured world modeling framework that enhances latent representations through geometric and semantic supervision. Alongside future RGB prediction, our model introduces two auxiliary prediction branches for future geometry and semantic representations, enabling it to jointly capture scene dynamics, spatial geometry, and semantic context within a unified latent space. Crucially, our approach preserves efficient inference by avoiding explicit future rollout or video generation at test time. Extensive experiments show that incorporating structured world supervision consistently improves action prediction accuracy, scene understanding, and robustness under challenging embodied scenarios, highlighting its potential for advancing scalable and efficient WAMs.

</details>

#### 2026-06-02 - NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation

**Authors:** NVIDIA, :, Aarti Basant, Amlan Kar, Despoina Paschalidou, Fangyin Wei, Francesco Ferroni, Guillermo Garcia Cobo, Haithem Turki, Huan Ling, Jaewoo Seo, James Lucas, Jay Zhangjie Wu, Jialiang Wang, Jonathan Lorraine, Jun Gao, Kai He, Katarina Tothova, Kevin Xie, Michał Tyszkiewicz, Qi Wu, Riccardo de Lutio, Ruilong Li, Sanja Fidler, Seung Wook Kim, Tianchang Shen, Tianshi Cao, Tobias Pfaff, William Lew, Xindi Wu, Xuanchi Ren, Yifan Lu, Yuxuan Zhang, Zan Gojcic, Zian Wang
**Links:** [abs](https://arxiv.org/abs/2606.03159) - [pdf](https://arxiv.org/pdf/2606.03159)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation, world model

<details>
<summary>Abstract</summary>

As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck. In closed-loop simulation, the driving policy model actively interacts with the environment, where its actions dynamically update the simulator state and directly influence the next set of generated sensor observations. While recent reconstruction-based neural simulators offer photorealism, they are fundamentally constrained by their initial captured data and struggle to generalize to highly dynamic or novel scenes. To overcome these limitations, we introduce OmniDreams, a foundation generative world model mid- and post-trained from the Cosmos diffusion model to autoregressively generate action-conditioned videos in real time. By leveraging the rich visual priors of Cosmos and mid- and post-training on 21k hours of driving scenarios, OmniDreams synthesizes complex, unobserved phenomena that are hard for traditional simulators to capture, such as extreme weather and unpredictable dynamic agent behaviors. Crucially, it autoregressively conditions its photorealistic sensor generation on past frames, the current simulator state, and immediate driving actions. Deployed in a closed-loop system with the Alpamayo 1 policy model and AlpaSim orchestrator, OmniDreams acts as a highly responsive, reactive environment, providing a scalable and comprehensive solution for training and evaluating next-generation autonomous driving policies. We additionally show preliminary results indicating that a world-action model (WAM) post-trained from OmniDreams achieves strong performance on the Physical AI Autonomous Vehicles NuRec dataset, surpassing the VLA-based Alpamayo 1.5 research policy model while using only 1/5 the total parameters. These results highlight the potential for a real-time world model like OmniDreams to also serve as a backbone for policy architectures.

</details>

#### 2026-06-02 - MARIO: Motion-Augmented Real-Time Multi-Sensor Inertial Odometry

**Authors:** Yiquan Li, Taeyoung Yeon, Chenfeng Gao, Vasco Xu, Xuanyou Liu, Karan Ahuja
**Links:** [abs](https://arxiv.org/abs/2606.02996) - [pdf](https://arxiv.org/pdf/2606.02996)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, AR, augmented reality

<details>
<summary>Abstract</summary>

Inertial odometry (IO) using only Inertial Measurement Units (IMUs) provides a lightweight solution for human motion tracking in augmented reality (AR) and wearable devices. Recent learning-based IO methods have improved the generalizability of inertial localization through large-scale pretraining on human motion datasets. However, these approaches remain prone to drift and noise because they do not explicitly capture human motion dynamics, especially on daily activity datasets such as Nymeria. In this work, we propose to ground inertial odometry in human kinematics through a learned IMU-inferred pose prior, which promotes physically consistent motion constraints. We integrate this pose prior into existing IO architectures and reduce positional drift by up to 36% on the challenging Nymeria dataset, which is 5x larger than datasets used in prior work. We further improve long-term performance with a sensor-fusion framework that incorporates auxiliary signals from lightweight sensors already available on commercial AR glasses, including magnetometers, barometers, and secondary IMUs. With this fusion strategy, positional drift is reduced by up to 42%, improving robustness and generalization across diverse motion conditions. Together, our results introduce a new paradigm for inertial and lightweight odometry by unifying human motion kinematics with multimodal sensing, setting a new benchmark for accurate and robust camera-less human tracking. Our website is available at https://spice-lab.org/projects/MARIO/.

</details>

#### 2026-06-02 - Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion

**Authors:** Oskar Natan, Jun Miura
**Links:** [abs](https://arxiv.org/abs/2606.02979) - [pdf](https://arxiv.org/pdf/2606.02979)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth estimation, autonomous driving, simulation

<details>
<summary>Abstract</summary>

We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass. The model performs multiple views of semantic segmentation, depth estimation, light detection and ranging (LiDAR) segmentation, and bird's eye view projection simultaneously without being supported by other models. We also provide an adaptive loss weighting algorithm to tackle the imbalanced learning issue that occurred due to plenty of given tasks. Through data pre-processing and intermediate sensor fusion techniques, the model can process and combine multiple input modalities retrieved from RGB cameras, dynamic vision sensors (DVS), and LiDAR placed at several positions on the ego vehicle. Therefore, a better understanding of a dynamically changing environment can be achieved. Based on the ablation study, the model variant trained with our proposed method achieves a better performance. Furthermore, a comparative study is also conducted to clarify its performance and effectiveness against the combination of some recent models. As a result, our model maintains better performance even with much fewer parameters. Hence, the model can inference faster with less GPU memory utilization. Moreover, the result tends to be consistent in 3 different CARLA simulation datasets and 1 real-world nuScenes-lidarseg dataset. To support future research, we share codes and other files publicly at https://github.com/oskarnatan/compact-perception.

</details>

#### 2026-06-01 - MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data

**Authors:** Teng Hu, Mingchun Lu, Yating Wang, Jiangning Zhang, Jinkun Hao, Ye Pan, Ran Yi, Lizhuang Ma, Dacheng Tao
**Links:** [abs](https://arxiv.org/abs/2606.02753) - [pdf](https://arxiv.org/pdf/2606.02753)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, simulation, world model, world modeling

<details>
<summary>Abstract</summary>

Video world models are a foundational generative technology for embodied AI and the Metaverse, yet existing approaches are inherently limited to a single agent observing from a single perspective. Extending these models to multi-agent settings introduces two critical challenges: data scarcity (coordinated multi-view recordings are prohibitively expensive to collect for general open-domain scenarios) and world state alignment (independently generated video streams cannot ensure that shared physical environments and events evolve consistently across views). To address these challenges, we propose MetaWorld, a novel framework that scales multi-agent video world models to open-domain environments directly from single-view videos. First, we introduce Monocular World-State Unrolling (MWSU) to explicitly decompose monocular footage into the camera operator's ego-motion and the visible subject's spatial trajectory. This camera-trajectory decomposition naturally extracts synchronized multi-agent motion data within a shared 3D space, completely bypassing the need for multi-camera setups. Second, for precise visual control, we develop the Subject-Aware World Generator to enable appearance-driven simulation conditioned on per-agent identity images. Finally, to ensure both views are grounded in the identical physical reality, we propose World-State Alignment, a per-frame inter-branch cross-attention mechanism inserted at every transformer layer of the video DiT. By jointly synchronizing the denoising process, WSA enforces both static geometric consistency and dynamic motion consistency, encouraging that the shared 3D environment and physical events remain well-aligned across both egocentric views. Extensive experiments demonstrate that MetaWorld achieves superior cross-view consistency and identity fidelity, establishing a highly scalable, physics-driven paradigm for multi-agent video world modeling.

</details>

#### 2026-06-01 - MASER: Modality-Adaptive Specialist Routing for Embodied 3D Spatial Intelligence

**Authors:** Hilton Raj, Vishnuram AV
**Links:** [abs](https://arxiv.org/abs/2606.02463) - [pdf](https://arxiv.org/pdf/2606.02463)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>Abstract</summary>

In 3D environments, Embodied Agents answer spatially relevant questions through reasoning from a mixture of modalities including natural language, RGB images, point clouds, depth maps and camera poses. Existing Vision-Language models (VLMs) are fine-tuned over a single modality. This completely ignores the question semantics which may favor a different modality than the finetuned modality. To address this, we propose MASER (Modality-Adaptive SpEcialist Routing), a lightweight framework that trains five different modality adapters of a shared VLM backbone and learns a neural routing policy that selects the best adapter based on the question during inference. We encode each question with a frozen sentence transformer and pass the embedding through a small Multi-layer Perceptron (MLP) trained on oracle adapter-accuracy labels. We evaluate our methodology over the Open3D-VQA benchmark and our evaluations show that no single modality is universally optimal -- point-cloud answers are best in 51.5% of cases. MASER routes with 51.3% oracle agreement, outperforming a Random-Forest ablation (43.5%), with only a single adapter call per question.

</details>

#### 2026-06-01 - SAVMap: Structure-Aided Visual Mapping of Large-Scale 2.5D Manhattan Wireframes from Panoramic Video

**Authors:** Howard Huang, Bharath Surianarayanan, Keifer Lee, Chenyu Wang, Chen Feng
**Links:** [abs](https://arxiv.org/abs/2606.01939) - [pdf](https://arxiv.org/pdf/2606.01939)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** structure from motion, mapping, localization, digital twin

<details>
<summary>Abstract</summary>

Precise 3D representations of industrial environments enable tasks such as robot localization and digital twin generation. We propose SAVMap, a method for generating a semantic wireframe map of warehouse shelf and light structures using only a panoramic video camera as the sensor input. Sequences of rectified images with shelf and ceiling-facing views are extracted from a panoramic video captured along the warehouse aisles. Using a semantic segmentation network front end, a set of sparse, semantic structure feature points (e.g., corners of shelf structures, centers of lights) are extracted from each image and tracked across the sequences. By accounting for real-world geometric relationships among the points such as Manhattan grids, a constrained structure-from-motion algorithm yields the 3D points that form a wireframe map. We demonstrate the scalability and accuracy of our proposal in a warehouse with 46 shelving rows, each with faces spanning 55\,m by 7\,m. From an hour of panoramic video content, we create wireframe maps for over 5000 shelf elements across the rows, achieving an aggregate mean absolute error of 4.8\,cm with respect to ground-truth.

</details>

#### 2026-06-01 - Unified Driving Tokens: Representation- and Geometry-Guided Discrete Tokenizer for Driving World Models and Planning

**Authors:** Ziyang Yao, Zeyu Zhu, YunCheng Jiang, Zibin Guo, Huijing Zhao
**Links:** [abs](https://arxiv.org/abs/2606.01935) - [pdf](https://arxiv.org/pdf/2606.01935)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world model, world modeling

<details>
<summary>Abstract</summary>

Discrete visual tokens should provide a compact representation for both token-based world modeling and planning in autonomous driving. However, most tokenizers are inherited from image generation and are optimized mainly for pixel reconstruction, which may leave a gap between what is easy to generate and what is useful to decode for driving decisions. We present a representation-guided and geometry-enhanced tokenizer that learns discrete tokens under joint supervision. The tokenizer aligns its discrete bottleneck with a frozen DINO feature space through feature decoding, while preserving appearance via RGB reconstruction with perceptual and adversarial losses. To inject geometric state-related cues, we add adjacent-frame depth and relative-pose supervision during training and stabilize joint objectives with multi-codebook quantization. We evaluate the same learned tokens with a lightweight planning readout and a GPT-style next-token world model. Experiments on NAVSIM show improved reconstruction fidelity and representation consistency, competitive planning performance under a fixed decoder, and better generative quality under matched settings.

</details>

#### 2026-06-01 - Trans2Occ: Voxel Occupancy Estimation and Grasp for Transparent Objects from Simulation to Reality

**Authors:** Yixuan Yang, Sha Zhang, Rui Li, Zhenfei Yin, Xinzhu Ma, Yiran Qin, Lei Bai, Xudong Xu, Shilin Shan, Wangmeng Zuo, Yanyong Zhang, Wanli Ouyang, Feng Zheng, Shixiang Tang, Dongzhan Zhou
**Links:** [abs](https://arxiv.org/abs/2606.01777) - [pdf](https://arxiv.org/pdf/2606.01777)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, robotics, manipulation, simulation

<details>
<summary>Abstract</summary>

Transparent objects remain challenging for robotic perception due to unreliable depth sensing caused by refraction and reflection. While prior approaches rely on multi-view reconstruction or depth completion, they are often difficult to scale or deploy in real-world robotic systems. In this paper, we present a practical framework for transparent object perception and manipulation based on single-view RGB input. Our approach predicts voxel-space occupancy directly from a single image, providing a geometry-aware representation that supports downstream robotic grasping. To enable large-scale training, we construct a simulation pipeline that generates paired RGB images and voxel occupancy annotations under diverse materials and lighting conditions. We demonstrate that the predicted occupancy representation is robust to domain shifts and transfers effectively from simulation to real-world robotic setups without fine-tuning. A simple rule-based grasping strategy built on top of the occupancy further achieves reliable grasp performance on transparent objects. Extensive experiments in both simulation and real-world environments show that our framework provides accurate 3D understanding and enables practical manipulation of transparent objects. These results suggest that single-view occupancy prediction offers a scalable and effective solution for transparent object perception in robotics.

</details>

#### 2026-06-01 - Hierarchical Object Representation for Spatial Robot Perception: Points, Meshes, and Superquadrics

**Authors:** Ceng Zhang, Wan Su, Mohamed Samshad, Gregory S. Chirikjian, Rajat Talak
**Links:** [abs](https://arxiv.org/abs/2606.01545) - [pdf](https://arxiv.org/pdf/2606.01545)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, robot perception, robot navigation, localization

<details>
<summary>Abstract</summary>

Hierarchical 3D Scene Graphs (3DSG) have emerged as an actionable and scalable representation for long-term autonomy incorporating metric, semantic, and topological information in the scene. However, the question of geometric representation of objects in 3DSG has been overlooked as most methods use simplified geometric models such as partial point clouds or 3D bounding boxes. In this work, we introduce a hierarchical object representation that can be leveraged for high-fidelity object-level reconstruction, object-based robust re-localization or map alignment, and efficient and analytical collision checking for safe robot navigation planning in dense and cluttered environments. The representation is structurally organized into four distinct layers, progressively abstracting the scene from raw sensor data to dense 3D meshes to analytical primitives such as superquadrics, which provide a sparse and analytical representation for object geometry. We develop a pipeline that builds the hierarchical object representation from RGB-D image stream captured by a robot, and demonstrate its working in real-world open-set object scenes in both indoor and outdoor environments. Extensive experiments across diverse datasets including HOPE, ReplicaCAD, Kimera-Multi, and NUS Campus Dataset collected using Unitree B2 Robot validate our pipeline in both indoor and outdoor environments. We show that our superquadric-based map alignment method outperforms the current state-of-the-art object based map alignment method ROMAN. Our code can be found at https://github.com/perceptica-robotics/Hickory.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
