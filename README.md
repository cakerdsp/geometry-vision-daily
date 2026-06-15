# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：42
- 分类分布：
  - Embodied / Robotics / AR Applications: 17
  - Neural Scene Representations & Rendering: 11
  - 3D Reconstruction & Multi-view Geometry: 10
  - Dynamic / 4D Reconstruction: 2
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，基于您提供的论文列表，以下是综合分析报告。

---

#### 今日主要趋势

1.  **从“高效渲染”到“高效且物理准确”的演进**: 本批论文中，3D高斯泼溅（3DGS）和神经辐射场（NeRF）的研究重点不再仅仅是速度和质量的权衡。多篇工作致力于解决现有方法的物理不一致性问题。例如，`MaterialClusterGS` 引入调色板（palette）概念来解决逐基元（primitive）材质分解的欠约束问题，`Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields` 统一了前向与反向的光传输管线，摒弃了光栅化流程，旨在实现全局照明的、物理准确的逆渲染。这表明领域正从“快速好看”向“物理可解释”过渡。

2.  **“视觉-语言模型”的渗透与语义化**: 视觉-语言模型（VLM）的应用正从零样本分类、检测扩展到更复杂的具身任务。`Zero-Shot Semantic Re-Identification for Autonomous Driving` 探索了使用VLM生成结构化语义描述替代视觉特征进行重识别，这代表了从“匹配像素”到“匹配语义”的范式转变。`GEAR-VLA` 则尝试将VLA模型与几何感知的3D表征结合，生成更具泛化性的操作动作。这揭示了VLM/LLM在复杂视觉推理和结构化理解方面扮演着越来越核心的角色。

3.  **跨视角与多智能体一致性成为研究热点**: 解决不同视角下的信息对齐和一致性是当前的一个关键挑战。这体现在两个层面：一是**跨视图几何**，如 `Meridian` 在非城市环境中匹配航拍图与地面图，`G2G` 解决了已知组内几何的两个图像组之间的位姿估计。二是**多智能体世界模型**，如 `Prisma-World` 明确提出在视频世界模型中解决多智能体视角在场景布局、物体外观上的一致性。这表明从单一视角的静态重建，正在向多视角、动态、协同的场景理解迈进。

4.  **面向低算力与实时性的极致优化**: 在追求高性能的同时，针对资源受限平台和实时应用的优化需求同样迫切。`REFINE` 通过无渲染的解析度量，将3DGS剪枝的计算复杂度降低了3,000倍；`RadiusFPS` 则是针对3D感知管线中核心算子FPS的算法级与硬件级加速。`Efficient Minimal Solvers for Relative Pose Estimation` 和 `Efficient Minimal Solvers for Visual-Inertial Relative Pose Estimation` 通过代数技巧和先验信息，显著降低了位姿估计的计算量，其目标都是适配自动驾驶和机器人上的实时性要求。

#### 技术路线观察

- **几何与位姿估计（3D Reconstruction & Multi-view Geometry）**：本批论文在该方向的技术路线非常鲜明——**利用先验降维增效**。`Efficient Minimal Solvers` 的两篇论文（2606.09569, 2606.09477）都通过引入IMU的垂直方向、旋转轴先验或平面运动假设，将复杂的相对位姿估计问题简化为低次多项式求解（如六次），追求在RANSAC框架下的极速假设生成。`G2G` 则选择了另一条路：**冻结强大的多视角基础模型**，仅添加轻量级可学习模块来桥接两组图像，实现高效且数据不敏感的组间位姿估计。

- **神经场景表示与渲染（Neural Scene Representations & Rende）**：技术路线呈现多元化和专业化趋势。
    - **基元层面的创新**：`Beyond Spherical Harmonics` 跳出球谐函数（SH）的框架，系统评估并提出新的球面基函数（Normalized Anisotropic Spherical Gabor），旨在以更紧凑的参数高效建模高频外观。
    - **框架层面的融合**：`Leveraging NeRF-Rendered Images for 3DGS` 和 `UniSHARP` 体现了“取长补短”的思路。前者利用NeRF的渲染结果（如去除瞬态物）来优化3DGS的输入，后者将针孔相机的视图合成方法扩展到各类相机（鱼眼、全景）。
    - **物理层面的约束**：`MaterialClusterGS` 和 `Path-Traced Inverse Rendering` 都致力于将物理模型（BRDF, 光传输方程）嵌入到可微渲染框架中，从“拟合像素”转向“拟合光照与材质”。
    - **效率层面的优化**：`REFINE` 代表了剪枝领域的范式转变，从“先渲染后评估”到“理论推导直接评估重要性”。

- **具身/机器人/AR应用（Embodied / Robotics / AR Applications）**：该方向的论文覆盖面广，技术路线侧重于**如何利用多模态信息和几何先验来提升通用性和鲁棒性**。
    - **强化真实物理**：`Real-IKEA` 强调提升仿真器中的“物理保真度”（如精确的碰撞网格和动力学参数），认为这是训练出可迁移到真实世界的鲁棒策略的前提。
    - **融合几何与语义**：`Meridian` 结合度量（Metric）与语义（Semantics）基元进行匹配，`GEAR-VLA` 显式地将几何嵌入到VLA模型中，`RGB-S` 利用运动学将触觉信号投影到图像域（视觉-触觉对齐）。
    - **隐空间解耦**：`Latent Diffusion Policy` 通过CVAE将场景理解与轨迹生成解耦到不同的隐空间，简化了扩散模型的学习难度。

#### 值得优先阅读的论文

1.  **Beyond Spherical Harmonics: Rethinking Appearance Models for Radiance Reconstruction** (arXiv: 2606.09794)
    - **理由**：该工作挑战了神经渲染领域一个非常基础且普遍使用的组件——球谐函数。它并非工程改进，而是理论上的反思和基函数层面的创新，这可能会推动整个场景表示领域的效率和质量边界，对任何从事NeRF/3DGS相关研究的学者都极具参考价值。

2.  **REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance** (arXiv: 2606.09074)
    - **理由**：文中报告了3,000倍的剪枝计算加速，是一个很值得关注的效率提升幅度。该方法直接跳过耗时的渲染步骤，通过解析模型来评估基元重要性，是一种方法论上的创新。这项技术对于将3DGS部署到移动设备和低功耗平台至关重要，并且其“无渲染”的思路也可能启发对其他渲染步骤的优化。

3.  **Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields** (arXiv: 2606.09606)
    - **理由**：这项工作统一了3DGS下的前向和反向光传输，且显式处理了全局照明。该工作解决了逆渲染领域一个常见的“管线不一致”问题，代表了从光栅化逆渲染向更物理准确的路径追踪逆渲染的演进方向。对于从事材质与光照估计的研究者来说，是不可忽视的进展。

4.  **Prisma-World: Camera-Controllable Multi-Agent Video World Model** (arXiv: 2606.09507)
    - **理由**：视频世界模型从“单视角”走向“多视角一致”是迈向更高层次理解和决策的关键一步。该工作通过联合去噪、几何感知注意力等机制显式解决跨视角一致性问题，并发布了大规模多智能体数据集。这项工作对于世界模型、多智能体系统以及自动驾驶仿真都具有重要的引领意义。

5.  **GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation** (arXiv: 2606.08530)
    - **理由**：VLA模型是目前机器人操作领域的前沿，其泛化性是公认的瓶颈。该工作明确指出了当前VLA缺乏几何感知，并提出了一个包含粗到细动作学习、语义对齐3D集成和具身标准化的系统方案。这项研究对于希望理解并改进VLA模型泛化能力的研究者来说，提供了非常具体且有潜力的技术路线。

#### 可能的研究机会

1.  **先验与学习融合的极致化**: `Efficient Minimal Solvers` 系列工作展示了利用IMU先验进行极速位姿

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-14T22:27:58-04:00
**Total number of papers:** 16
**Number of papers added in the latest update:** 5
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

No papers in the current README window.

## 3D Reconstruction & Multi-view Geometry

### 2026-06

#### 2026-06-12 - StereoGeo: an end-to-end stereo camera calibration method

**Authors:** Imane Meddour, Andréa Macario Barros, Cédric Gouy-Pailler
**Links:** [abs](https://arxiv.org/abs/2606.14619) - [pdf](https://arxiv.org/pdf/2606.14619)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration

<details>
<summary>Abstract</summary>

In this work, we propose StereoGeo, an end-to-end network-based approach for stereo camera calibration. Our method estimates the focal lengths and gravity directions of the left and right cameras, as well as the relative extrinsic transformation relating them. Existing methods often rely on calibration patterns in structured environments or address only a single camera configuration, being limited to either intrinsic or extrinsic estimation, and depending on a multi-view setups. StereoGeo extends the GeoCalib algorithm, integrating deep neural network feature extraction with a differentiable optimizer. Extensive experiments on real-world benchmarks demonstrate that StereoGeo achieves competitive performance for intrinsic calibration and provides accurate stereo extrinsic estimation, outperforming existing methods that are limited to monocular settings. The dataset used in this work is partially publicly available at https://github.com/meddourimane/StereoGeo-dataset.

</details>

#### 2026-06-12 - Scratched Lenses, Shifted Depth: Passive Camera-Side Optical Attacks

**Authors:** Qinlin He, Zeming Zhuang, Yongji Wu, Lan Zhang, Xiaoyong, Yuan
**Links:** [abs](https://arxiv.org/abs/2606.14504) - [pdf](https://arxiv.org/pdf/2606.14504)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, manipulation

<details>
<summary>Abstract</summary>

Physical adversarial attacks on vision systems are typically studied through scene manipulation, such as adversarial patches or projections, where the adversary controls what the camera observes. Camera-side attacks using stickers or auxiliary optics have also been explored, but they treat attacks as image-space perturbations from designed patterns. This misses how physical imperfections interact with scene-dependent lighting and optics. We identify a threat: passive lens-side damage that is persistent yet trigger-conditioned, producing optical artifacts that bias geometric inference under particular visual conditions. We instantiate this threat through Scratch-induced Lens Adversarial Streak Hijacking SLASH, a physical-world attack caused by small scratches on a camera lens or protective cover. Scratches interact with bright light sources and specular reflections to create structured streak artifacts that distort depth cues. Since the perturbation is fixed in the optical path but triggered by the scene, it is both persistent and selective. We formulate the attack in optical space, model the scratch pattern as a trigger-conditioned optical channel, and optimize one fixed configuration across diverse viewing conditions. We evaluate SLASH on monocular depth estimation and monocular 3D object detection in digital and real-world settings. Under the fixed-scratch constraint, directional depth shifts reach up to 32% relative error for monocular depth estimation, with consistent effects on monocular 3D object detection. Physical experiments confirm transfer to real camera recordings, inducing depth shifts above the model's natural prediction baseline. These findings reveal an attack surface where benign-looking hardware imperfections act as latent, scene-triggered adversarial mechanisms, challenging assumptions about physical robustness and motivating defenses for secure vision systems.

</details>

#### 2026-06-12 - MooMIns -- Monocular 3D Reconstruction and Object Pose Estimation from Multiple Instances

**Authors:** Robert Langendörfer, Markus Hillemann, Markus Ulrich
**Links:** [abs](https://arxiv.org/abs/2606.14389) - [pdf](https://arxiv.org/pdf/2606.14389)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, structure from motion, SfM, pose estimation, depth estimation, monocular depth, Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Simultaneous 3D reconstruction and 6D object pose estimation from a single monocular image is an inherently ill-posed problem. In industrial settings, however, multiple instances of an object are often randomly arranged in bins, implicitly providing several views of the same object within a single image. We show that this implicit multi-view geometry can be exploited to simultaneously reconstruct the object in 3D and estimate the 6D pose of each visible object instance. We present MooMIns, a new Gaussian-splatting-based approach that inverts the original Gaussian splatting formulation: instead of rendering a single scene from multiple cameras, we render multiple object instances from a single camera. Our method is initialized with SAM3 instance segmentation masks and a modified Structure from Motion (SfM) pipeline. In contrast to learned monocular depth estimation, we perform true geometry-based reconstruction from image evidence, avoiding hallucinations caused by training data priors. We evaluate MooMIns on synthetic and real bin-picking scenarios, and demonstrate accurate reconstruction of previously unseen objects as well as reliable pose estimation of individual instance

</details>

#### 2026-06-12 - Pano3D: Unified 3D Reconstruction and Panoptic Segmentation

**Authors:** Victor Barberteguy, Ahmet Iscen, Mathilde Caron, Alireza Fathi, Gül Varol, Cordelia Schmid
**Links:** [abs](https://arxiv.org/abs/2606.14307) - [pdf](https://arxiv.org/pdf/2606.14307)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feedforward reconstruction, 3D reconstruction, dense reconstruction

<details>
<summary>Abstract</summary>

Recent advances in 3D feedforward reconstruction neural networks have achieved remarkable success in dense reconstruction from images without any camera parameters. Yet, equipping these models with robust semantic understanding remains an open problem. Here we introduce an approach that performs 3D reconstruction and 3D panoptic segmentation in a unified framework. We build on existing 3D reconstruction models and augment them with a set-based mask decoder. The approach is jointly trained with a geometric and semantic loss, which are shown to be mutually beneficial. More precisely, the features are initialized from the geometric information and then finetuned to capture jointly geometry and semantics. We demonstrate the generality of our approach by successfully applying our framework both to online and all-to-all attention reconstruction backbones. Our method achieves state-of-the-art performance in 3D panoptic segmentation across ScanNet, ScanNet200, and ScanNet++ datasets. Ablation studies show that such joint training of a unified model equips 3D feedforward reconstruction neural networks with panoptic segmentation and yields mutually beneficial improvements.

</details>

#### 2026-06-08 - Efficient Minimal Solvers for Relative Pose Estimation in Autonomous Driving Applications

**Authors:** Tao Li, Liang Liu, Jianli Han, Weimin Lv
**Links:** [abs](https://arxiv.org/abs/2606.09569) - [pdf](https://arxiv.org/pdf/2606.09569)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, robot navigation, autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Efficient Minimal Solvers for Relative Pose Estimation in Autonomous Driving Applications
- 作者：Tao Li, Liang Liu, Jianli Han, Weimin Lv
- 出版日期：2026-06-08
- 分类：3D Reconstruction & Multi-view Geometry (主要), Embodied / Robotics / AR Applications (次要)
- 链接：摘要：https://arxiv.org/abs/2606.09569, PDF：https://arxiv.org/pdf/2606.09569

### 一句话总结
本文针对自动驾驶中多相机系统的相对位姿估计，提出一种基于新颖平移参数化和一阶旋转近似的统一框架，并设计了三个高效最小求解器，旨在减少点对应数量和代数复杂度，从而在RANSAC管线中实现更快的假设生成。

### 研究问题
如何在自动驾驶等实时性要求高的场景中，降低相对位姿估计的计算成本，同时减少对大量特征匹配的依赖。

### 核心思路/方法
1.  **统一框架**：基于一种新颖的平移参数化方法（具体形式未详述）和一阶旋转近似（简化旋转计算的近似策略）。
2.  **三个高效最小求解器**：
    *   利用惯性测量单元提供的垂直方向先验。
    *   利用转向操作时旋转轴方向的先验。
    *   针对结构化道路上地面车辆的平面运动假设。
3.  **性能优化**：通过减少最小点对应数量和代数复杂度，在RANSAC框架内加速假设生成。

### 主要贡献
1.  提出一个用于高效相对位姿估计的统一框架（基于新平移参数化与一阶旋转近似）。
2.  设计了三个专门针对自动驾驶车辆的最小求解器，分别利用垂直方向先验、旋转轴方向先验和平面运动假设。
3.  在合成数据集和KITTI基准上验证，所提求解器在速度和精度之间取得了优于现有算法的平衡。

### 局限性
摘要未提供足够信息，例如三个特定求解器在更极端场景（如无IMU数据、快速转向或非平面道路）下的鲁棒性，以及各个求解器之间性能差异的具体原因。

### 阅读优先级
**高**。
理由：该论文针对自动驾驶中实时性要求高的相对位姿估计问题提出了新的求解方案，且选用的实验基准（KITTI）在该领域具有权威性。对于从事自动驾驶、机器人导航或实时多视图几何的研究者，该方法有直接参考价值。标题与摘要内容高度吻合，方法创新点明确。

</details>

<details>
<summary>Abstract</summary>

With the advancement of visual sensing systems, computer vision is playing an increasingly important role in autonomous driving and robot navigation. Relative pose estimation in multi-camera systems is essential for accurate vehicle localization and environment perception, demanding high real-time performance and robustness. Existing methods, however, often involve high computational costs and rely heavily on abundant feature matches, limiting their applicability in time-sensitive driving scenarios. To address these limitations, this paper introduces a unified framework for efficient relative pose estimation, built upon a novel translation parameterization and first-order rotation approximation. Within this framework, we propose three efficient minimal solvers specifically designed for autonomous vehicles. The first solver integrates the vertical direction prior from Inertial Measurement Units (IMUs), the second utilizes the rotation axis direction prior during steering maneuvers, and the third is designed for planar motion - a realistic assumption for ground vehicles operating on structured roads. By reducing both the minimal number of point correspondences and the algebraic complexity, our methods enable faster hypothesis generation within RANSAC-based pipelines, improving suitability for real-time systems. Extensive experiments on synthetic datasets and the KITTI autonomous driving benchmark demonstrate that the proposed solvers achieve a favorable balance between speed and accuracy compared to existing state-of-the-art algorithms.

</details>

#### 2026-06-08 - Efficient Minimal Solvers for Visual-Inertial Relative Pose Estimation in Multi-Camera Systems

**Authors:** Tao Li, Zhenbao Yu, Banglei Guan, Jianli Han, Weimin Lv
**Links:** [abs](https://arxiv.org/abs/2606.09477) - [pdf](https://arxiv.org/pdf/2606.09477)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：高效的多相机系统视觉-惯性相对位姿估计最小求解器
- 作者：Tao Li, Zhenbao Yu, Banglei Guan, Jianli Han, Weimin Lv
- 出版日期：2026-06-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：arXiv:2606.09477 (https://arxiv.org/abs/2606.09477)

### 一句话总结
本文提出两种利用IMU先验信息的最小求解器，仅需四个点对应即可将多相机相对位姿估计问题简化为求解一元六次多项式，在计算效率和精度上优于现有方法。

### 研究问题
如何高效且鲁棒地估计多相机系统之间的相对位姿，同时减少对大量点对应的依赖和计算复杂度。

### 核心思路/方法
1. **参数化与先验信息利用**：采用新型参数化方法，分别利用IMU提供的垂直方向先验和旋转轴方向先验。
2. **求解器设计**：
   - 第一个求解器：使用垂直方向先验。
   - 第二个求解器：使用旋转轴方向先验。
3. **约简问题复杂度**：将多相机相对位姿估计问题从传统的八次多项式化简为求解一元六次多项式。
4. **集成框架**：该方法特别适合嵌入RANSAC框架用于视觉里程计。

### 主要贡献
1. 提出两种仅需四个点对应的多相机相对位姿估计最小求解器。
2. 通过引入IMU先验，将问题降阶为六次多项式求解，显著降低计算复杂度。
3. 在合成数据和KITTI基准上验证了优越的计算效率和与现有方法相当的精度。

### 局限性
摘要未提供足够信息。例如，未提及方法对IMU噪声的鲁棒性、两种求解器各自适用的场景或失败案例。

### 阅读优先级
**高**  
理由：该工作针对多相机系统相对位姿估计这一计算机视觉基础问题，解决了计算复杂度和点对应数目的关键瓶颈。方法简洁（六次多项式）、实用性强（适用于RANSAC和视觉里程计），且与当前自动驾驶等热点应用紧密相关。

</details>

<details>
<summary>Abstract</summary>

Estimating the relative poses of multi-camera systems is a fundamental problem in computer vision, with critical applications in autonomous vehicles, mobile devices, and unmanned aerial vehicles (UAVs). However, existing solutions often suffer from high computational complexity or rely on an excessive number of point correspondences, limiting their real-world applicability. To address these limitations, we propose two efficient minimal solvers for estimating the relative poses of multi-camera systems using a novel parameterization. The first solver leverages the vertical direction prior provided by Inertial Measurement Units (IMUs), while the second utilizes the rotation axis direction prior from IMUs. Our methods require only four point correspondences and reduce the problem of multi-camera relative pose estimation to solving a univariate 6th-degree polynomial, a significant improvement over existing approaches, which typically involve 8th-degree polynomials. This reduction in computational complexity and correspondence requirements makes our solvers particularly effective when integrated into RANSAC frameworks, demonstrating strong potential for visual odometry applications. Through rigorous evaluations on synthetic data and the KITTI benchmark, our methods achieved superior computational efficiency and competitive accuracy compared to state-of-the-art algorithms.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-08 - Beyond Spherical Harmonics: Rethinking Appearance Models for Radiance Reconstruction

**Authors:** Ewa Miazga, Jorge Condor, Piotr Didyk
**Links:** [abs](https://arxiv.org/abs/2606.09794) - [pdf](https://arxiv.org/pdf/2606.09794)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, radiance field, novel view synthesis, view synthesis, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Spherical Harmonics: Rethinking Appearance Models for Radiance Reconstruction
- 作者：Ewa Miazga, Jorge Condor, Piotr Didyk
- 出版日期：2026-06-08
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.09794

### 一句话总结
本文系统评估了多种球面函数在场景重建中的表现，并提出一种名为Normalized Anisotropic Spherical Gabor的新型球面函数，以更高效、更紧凑的方式建模高频视角依赖的外观效果。

### 研究问题
如何在辐射场重建中高效且紧凑地建模高频视角依赖的外观（如镜面反射、闪烁），同时避免传统球谐函数（SH）带来的高内存开销和计算成本。

### 核心思路/方法
1. 系统评估多种球面函数在场景重建中的表现，其中部分函数是首次被引入图形学和计算机视觉领域。
2. 基于实验洞察，提出Normalized Anisotropic Spherical Gabor函数，该函数能在保持紧凑表示的同时，高效建模和学习高频外观现象。

### 主要贡献
1. 首次系统评估并引入多种新的球面函数用于场景重建。
2. 提出一种新型球面函数（Normalized Anisotropic Spherical Gabor），能高效建模高频视角依赖效应。
3. 相比现有方法，该函数在重建质量（如闪烁效果）上更高，同时在内存使用上高效最多五倍，且计算效率更高。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直接针对神经辐射场/场景重建中的关键瓶颈（高频外观建模与内存/计算效率的权衡），且提出了新颖的函数形式并报告了显著的效率提升（五倍内存节省），对相关领域研究者有较强的参考价值。

</details>

<details>
<summary>Abstract</summary>

View-dependent appearance modeling remains a challenging problem in novel-view synthesis and reconstruction. Accurately representing complex angular effects often requires substantial memory and computational resources. For new learning-based methods, a common approach is to rely on SH. However, capturing high-frequency phenomena such as specular reflections demands high-order expansions, which increase memory usage and computational cost. Consequently, most methods employ low-order SH, which limits the ability to model complex view-dependent effects, resulting in overly smooth or diffuse representations. To address these limitations, we systematically evaluate a wide range of spherical functions in the context of scene reconstruction. Some of them are introduced to graphics and computer vision for the first time in this paper. Based on the insights from the experiment, we develop a novel spherical formulation, the Normalized Anisotropic Spherical Gabor function that enables efficient modeling and learning of high-frequency appearance effects while maintaining compact representation. Compared to existing approaches, our function achieves higher-quality reconstruction of view-dependent phenomena such as glints, while being up to five times more memory-efficient and more efficient to evaluate. We validate its performance in radiance-field reconstruction tasks.

</details>

#### 2026-06-08 - Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields

**Authors:** Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li
**Links:** [abs](https://arxiv.org/abs/2606.09606) - [pdf](https://arxiv.org/pdf/2606.09606)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields
- 作者：Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li
- 出版日期：2026-06-08
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.09606

### 一句话总结
本文提出一种基于统一光线追踪管线的3D高斯场逆渲染框架，通过路径空间交互模型实现无光栅化、支持全局照明的材质与环境优化。

### 研究问题
现有基于3D高斯场的逆渲染方法在正向渲染与反向优化时采用不一致的光传输管线（光栅化估计G-buffer + 屏幕空间优化），且忽略间接照明，导致路径追踪渲染下的着色不一致、伪影以及材质-光照估计不准确。

### 核心思路/方法
1. **统一管线**：在3D高斯场中定义正向光传输与反向梯度传播全程使用光线追踪，摒弃光栅化的splatting步骤。
2. **路径空间等效交互模型**：为重叠的高斯图元设计路径空间等效交互模型，确保蒙特卡洛路径追踪对光传输积分的无偏估计，并在同一光线追踪交互上重放逐路径梯度（而非从屏幕空间缓冲区计算）。
3. **完整渲染方程优化**：在包含光线追踪可见性及多弹次光传输的完整渲染方程下，优化材质与紧致球面高斯环境光照。

### 主要贡献
- 提出首个无需splatting的路径追踪逆渲染框架，统一了3D高斯场的前向与反向光传输管道。
- 设计了路径空间等效交互模型，使光线追踪为无偏估计，并实现路径级梯度传导。
- 在完整渲染方程下实现全局照明逆渲染，实验表明在材质逆推、路径追踪渲染质量、阴影、反射和重光照效果上优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法针对当前逆渲染领域关键瓶颈（管线不一致、缺乏全局照明）提出创新解决方案，且实验结果获得显著提升，对神经渲染与逆向图形学方向的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Ray tracing enables 3D Gaussian fields to serve as a representation for physically based light transport. Faithful inverse rendering requires forward rendering and backward optimization to be defined within a consistent light-transport pipeline. Existing inverse rendering methods estimate G-buffers via splatting and optimize materials in screen space, tying the recovered properties to a rasterization-based pipeline. This pipeline mismatch, together with simplified rendering equations that neglect indirect illumination, often leads to inconsistent shading, visible artifacts, and inaccurate material-lighting estimation under path-traced rendering. Therefore, we propose a splatting-free path-traced inverse rendering framework for 3D Gaussian fields, where forward light transport and backward gradient propagation are defined within a unified ray-tracing pipeline. Our key idea is to define a path-space equivalent interaction model for overlapping Gaussian primitives, under which Monte-Carlo-based path tracing is unbiased for the induced light-transport integral, while pathwise gradients are replayed over the same ray-traced interactions rather than splatting-derived screen-space buffers. The framework optimizes materials and a compact Spherical-Gaussian environment under the full rendering equation with ray-traced visibility and multi-bounce light transport. Extensive experiments demonstrate competitive material inversion and improved path-traced rendering quality, producing more plausible shadows, reflections, and relighting results under global illumination.

</details>

#### 2026-06-08 - REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance

**Authors:** Zhang Chen, Shuai Wan, Mengting Yu, Fuzheng Yang, Junhui Hou
**Links:** [abs](https://arxiv.org/abs/2606.09074) - [pdf](https://arxiv.org/pdf/2606.09074)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance
- 作者：Zhang Chen, Shuai Wan, Mengting Yu, Fuzheng Yang, Junhui Hou
- 出版日期：2026-06-08
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.09074

### 一句话总结
本文提出REFINE，一种无需渲染的3D高斯泼溅剪枝框架，通过解析近似的感知权重度量实现超高效剪枝，在保持渲染质量的同时将剪枝计算复杂度降低3000倍。

### 研究问题
现有3D高斯泼溅剪枝方法存在两类缺陷：要么剪枝后渲染质量严重下降，要么计算开销过高。如何设计一种既高效又能保持高渲染质量的剪枝方法成为核心问题。

### 核心思路/方法
- 提出无需渲染的原始重要性度量，替代传统依赖渲染前向传播的剪枝策略。
- 利用解析近似的、感知相关的海森矩阵（Hessian field）量化移除单个高斯原语后预期的感知误差。
- 联合建模可见性、投影几何和内容自适应超参数，推导出各向异性的感知权重场，作为原始重要性的高保真代理。
- 完全绕过了计算代价高昂的渲染前向传播过程。

### 主要贡献
- 提出REFINE框架，实现超高效的3D高斯泼溅剪枝。
- 首创无需渲染的原始重要性度量方法，大幅降低剪枝计算复杂度。
- 在多个基准数据集上验证：剪枝计算复杂度相比现有最优方法降低3000倍，同时保持高度竞争性的渲染质量。

### 局限性
摘要未提供足够信息。未提及该方法在极端剪枝率下的性能表现、对不同场景类型的适用局限性，或与其他剪枝方法在内存消耗、推理速度等方面的对比细节。

### 阅读优先级
**高**
理由：该工作直接针对3DGS剪枝核心痛点（计算开销与质量权衡），提出理论创新的解析度量（无需渲染的海森矩阵），并取得了数量级计算加速（3000x），对于从事3D神经渲染、模型压缩和实时图形学的读者有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing pruning methods for 3D Gaussian splatting (3DGS) suffer from either severe quality degradation or prohibitive computational overhead. In this paper, we propose REFINE, a highly accelerated 3DGS pruning framework centered on a novel rendering-free primitive importance metric. Our approach leverages an analytically approximated, rendering-aware Hessian field to quantify the expected perceptual error induced by the removal of individual primitives. By modeling the joint modulation of visibility, projection geometry and the content adaptive hyperparameter, we entirely bypass costly forward rendering passes and derive an anisotropic perceptual weight field that serves as a high-fidelity proxy for primitive importance. Extensive experiments across multiple benchmark datasets demonstrate that REFINE maintains highly competitive rendering quality while achieving an unprecedented $3,000\times$ reduction in pruning-related computational complexity compared to state-of-the-art pruning methods.

</details>

#### 2026-06-08 - Leveraging NeRF-Rendered Images for 3D Gaussian Splatting

**Authors:** Mizuki Morikawa, Yuta Shimizu, Chunyu Li, Yusuke Monno, Masatoshi Okutomi
**Links:** [abs](https://arxiv.org/abs/2606.09034) - [pdf](https://arxiv.org/pdf/2606.09034)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Leveraging NeRF-Rendered Images for 3D Gaussian Splatting
- 作者：Mizuki Morikawa, Yuta Shimizu, Chunyu Li, Yusuke Monno, Masatoshi Okutomi
- 出版日期：2026-06-08
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.09034, PDF: https://arxiv.org/pdf/2606.09034

### 一句话总结
本文提出利用街道场景下NeRF生成的图像（包括移除瞬态物体的训练图像和鸟瞰视角图像）来训练3DGS，并结合扩散模型增强图像质量，以在保持3DGS渲染速度的同时继承NeRF的高质量渲染。

### 研究问题
如何结合NeRF的高渲染质量与3DGS的快速渲染速度，特别是在街道场景中，提升3DGS的渲染效果。

### 核心思路/方法
首先，利用预训练的街景专用NeRF方法生成训练图像：用于移除输入视图中的瞬态物体，并生成鸟瞰视角作为附加视图。其次，在3DGS训练中使用这些NeRF渲染图像，将NeRF的高质量渲染特性迁移到3DGS中。最后，引入基于扩散模型的图像增强技术，进一步提升附加视图的图像质量。

### 主要贡献
1. 提出了一种利用NeRF渲染图像来改进3DGS训练的方法，针对街道场景。
2. 通过NeRF渲染图像实现瞬态物体移除和鸟瞰视角生成，使3DGS继承NeRF的高渲染质量。
3. 引入扩散模型增强附加视图质量，在合成和两个真实数据集上验证了方法在保持3DGS速度与NeRF质量的同时，改进了街道场景渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工作针对街道场景提出了NeRF与3DGS结合的特定应用方案，有明确的性能继承思路（速度+质量），但摘要未提供详细的实验对比和局限性分析，适合对该方向（神经渲染、街景建模）感兴趣者快速浏览。

</details>

<details>
<summary>Abstract</summary>

Neural radiance field (NeRF) and 3D Gaussian splatting (3DGS) are two mainstream approaches for novel view synthesis. They often show complementary performance, i.e., 3DGS demonstrating faster rendering speed and NeRF demonstrating higher rendering quality. Motivated by this, we propose leveraging NeRF-rendered images for 3DGS. Specifically, we target street scenes and utilize a pre-trained street-specific NeRF method to produce training images for a target 3DGS method. In our 3DGS training, NeRF-rendered images are used to remove transient objects in street-level input views and to generate bird's-eye views as additional views, inheriting the higher-quality rendering of NeRF into 3DGS. We further incorporate a diffusion-based image enhancement to improve the image quality of the additional views. Experimental results on one synthetic and two real datasets demonstrate that our proposed method improves street-scene rendering while preserving the speed of 3DGS and the quality of NeRF.

</details>

#### 2026-06-08 - MaterialClusterGS: Palette-Based Material Decomposition and Physically-Based Relighting with 2D Gaussian Splatting

**Authors:** Hao Zhang, Ang Li, Boyan Du, Junke Zhu, Fei Zhu, Meng Gai, Zhangjin Huang, Guoping Wang, Sheng Li
**Links:** [abs](https://arxiv.org/abs/2606.09018) - [pdf](https://arxiv.org/pdf/2606.09018)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, inverse rendering, relighting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MaterialClusterGS: Palette-Based Material Decomposition and Physically-Based Relighting with 2D Gaussian Splatting
- 作者：Hao Zhang, Ang Li, Boyan Du, Junke Zhu, Fei Zhu, Meng Gai, Zhangjin Huang, Guoping Wang, Sheng Li
- 出版日期：2026-06-08
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.09018

### 一句话总结
提出MaterialClusterGS框架，基于调色板（palette）方法将2D高斯溅射分解为共享BRDF原型，实现物理基重光照与材质编辑。

### 研究问题
现有基于高斯溅射的逆向渲染方法为每个基元独立分配BRDF参数，导致材质恢复严重欠约束（阴影、间接光照等被吸收进局部估计），且缺乏材质结构共享，编辑时无法将同一材质的变化一致传播。

### 核心思路/方法
1. 用紧凑的全局调色板表示场景材质，其中包含共享的BRDF原型。
2. 通过连续空间材质场为每个位置分配调色板中的原型。
3. 在基于物理的渲染目标下联合优化材质场、调色板原型和环境光照。

### 主要贡献
1. 提出调色板基材质分解框架，利用共享BRDF原型实现空间连贯的材质恢复。
2. 相比逐基元分解，该方法使材质编辑、重光照和材质迁移更一致。
3. 在2D高斯溅射中集成物理基渲染，同时保持紧凑表示。

### 局限性
摘要未提供足够信息。未提及实验设置、定量/定性结果、具体应用场景局限或失败案例。

### 阅读优先级
中。理由：该方法针对高斯溅射中材质欠约束问题提出了调色板基的创新思路，但摘要缺乏实验验证和性能对比，对编辑任务感兴趣者可进一步阅读正文。

</details>

<details>
<summary>Abstract</summary>

We present MaterialClusterGS, a palette-based material decomposition framework for 2D Gaussian Splatting that enables physically based relighting and material editing. Existing Gaussian inverse rendering methods typically assign independent BRDF parameters to individual primitives. While flexible, this local fitting strategy makes material recovery highly under-constrained: shadows, indirect illumination, geometric errors, and visibility residuals can be absorbed into thousands of slightly different local material estimates. Meanwhile, recent palette-based appearance methods operate solely in RGB space without modeling physical materials or illumination. To bridge this gap, we represent scene materials using a compact global palette of shared BRDF prototypes assigned via a continuous spatial material field. Without shared material structure, editing one region does not propagate consistently to others of the same material, making per-primitive decompositions impractical for editing. We jointly optimize the material field, palette prototypes, and environment lighting under a physically based rendering objective. The resulting framework recovers compact, spatially coherent attributes directly usable for material editing, relighting, and transfer.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-12 - BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization

**Authors:** Yinqiang Zhang, Liang Lu, Yipeng Pan, Maolin Lei, Yuhan Xie, Zhanteng Xie, Xiaowei Luo, Jia Pan
**Links:** [abs](https://arxiv.org/abs/2606.14237) - [pdf](https://arxiv.org/pdf/2606.14237)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>Abstract</summary>

Accurate and robust localization is a fundamental requirement for service and inspection robots, particularly in feature-sparse indoor environments where traditional systems struggle due to a lack of distinct landmarks. While prior maps can enhance robustness, precise and compact maps capturing real-world details are often unavailable for new or frequently changing environments. This paper presents BIM-Loc, a novel discrepancy-aware LiDAR-based localization method that directly integrates Building Information Models (BIM) from the design phase. BIM-Loc simultaneously estimates trajectories aligned with the BIM coordinate system and identifies discrepancies between real-world observations and the as-designed BIM in an online fashion. Our core contributions include: (1) a novel multi-hit ray casting strategy for efficient BIM-point data association and projection of 3D observations into 2D texture space; (2) a pose graph optimization framework with BIM-integrated factors that enforces consistency among odometry, sequential scans, and BIM structures; and (3) a hierarchical Bayesian inference module that incrementally updates a continuous 2D surface representation for discrepancy detection, propagating updates from the pixel to the structure level. Extensive evaluations in both simulation and real-world applications demonstrate that BIM-Loc significantly outperforms state-of-the-art map-based methods in localization accuracy and robustness.

</details>

#### 2026-06-08 - Prisma-World: Camera-Controllable Multi-Agent Video World Model

**Authors:** Huiqiang Sun, Zhan Peng, Size Wu, Kun Wang, Kang Liao, Dianyi Wang, Xingyu Zeng, Sheng Jin, Yangguang Li, Zhiguo Cao, Ziwei Liu, Wei Li
**Links:** [abs](https://arxiv.org/abs/2606.09507) - [pdf](https://arxiv.org/pdf/2606.09507)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Prisma-World: Camera-Controllable Multi-Agent Video World Model
- 作者：Huiqiang Sun, Zhan Peng, Size Wu, Kun Wang, Kang Liao, Dianyi Wang, Xingyu Zeng, Sheng Jin, Yangguang Li, Zhiguo Cao, Ziwei Liu, Wei Li
- 出版日期：2026-06-08T13:59:50Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.09507

### 一句话总结
Prisma-World 提出了一种通过几何感知联合去噪过程生成多智能体视角一致视频的世界模型，并配套提供了大规模多智能体数据集 PrismaDataset。

### 研究问题
现有视频世界模型通常模拟单一观察者视角，当扩展到多智能体时，独立生成各智能体未来状态会导致跨视角场景（如物体、布局、外观）不一致。

### 核心思路/方法
1. 将多智能体视频生成建模为联合几何感知去噪过程，所有智能体视频在同一个全注意力序列中处理。
2. 设计多智能体旋转位置编码（RoPE），区分智能体身份并保持同步时间坐标。
3. 将相对相机几何信息注入注意力机制，使重叠视角偏向共享场景证据。
4. 引入重叠衰减课程训练范式和最小地图（minimap）条件结构引导，增强多视角一致性和全局空间感知。
5. 基于UE5构建 PrismaDataset，包含全景采集、可组合多智能体视图组及精确相机/动作标注。

### 主要贡献
1. 提出首个相机可控的多智能体视频世界模型 Prisma-World，可生成视角一致的多智能体视频。
2. 设计多智能体 RoPE、几何感知注意力及重叠衰减课程训练等技术，显式约束跨视角一致性。
3. 引入 minimap 结构引导作为额外空间锚点，提升全局空间感知。
4. 构建大规模仿真数据集 PrismaDataset，支持多智能体模型训练与评估。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该工作针对多智能体视频生成中视角一致性这一关键难题，提出了创新的几何感知联合去噪框架，并提供了配套数据集，对具身智能、机器人及AR应用领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Video world models have made rapid progress in generating controllable visual experiences, but most of them still simulate the world from a single observer. Extending such models to multiple agents raises a central challenge: if each agent's future state is generated independently, overlapping views may instantiate different versions of the same scene, leading to inconsistent objects, layouts, and appearances across agents. Conventional camera conditioning controls individual trajectories, but it does not explicitly couple the generation of views that should agree under shared scene geometry. We introduce Prisma-World, a camera-controllable multi-agent world model that formulates multi-agent generation as a joint geometry-aware denoising process for cross-view consistency. Prisma-World processes all agent videos within one full-attention sequence, uses a multi-agent RoPE design to distinguish agent identities while preserving synchronized temporal coordinates, and injects relative camera geometry into attention to bias overlapping viewpoints toward shared scene evidence. To further strengthen multi-view consistency and enhance global spatial perception, we augment our framework with an overlap-decaying curriculum training paradigm alongside minimap-conditioned structural guidance. To facilitate the training and evaluation of multi-agent models, we introduce PrismaDataset, a large-scale UE5 dataset with panoramic acquisition across diverse scenes, composable multi-agent view groups with flexible agent counts and complex camera trajectories, and precise camera/action annotations for consistency training and evaluation. Experiments show that a single Prisma-World model can generate high-fidelity multi-agent videos with flexible agent numbers, camera controllability, improved cross-view consistency, and spatial grounding under minimap guidance.

</details>

#### 2026-06-08 - Zero-Shot Semantic Re-Identification for Autonomous Driving: A VLM Baseline Study

**Authors:** Eduardo Borges, Manuel Abreu, Luís Garrote, Urbano J. Nunes
**Links:** [abs](https://arxiv.org/abs/2606.09362) - [pdf](https://arxiv.org/pdf/2606.09362)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Zero-Shot Semantic Re-Identification for Autonomous Driving: A VLM Baseline Study
- 作者：Eduardo Borges, Manuel Abreu, Luís Garrote, Urbano J. Nunes
- 出版日期：2026-06-08
- 分类：具身/机器人/增强现实应用
- 链接：[摘要](https://arxiv.org/abs/2606.09362) | [PDF](https://arxiv.org/pdf/2606.09362)

### 一句话总结
本文提出一种零样本语义重识别管道，利用视觉-语言模型为自动驾驶中的交通参与者生成结构化文本描述，用于跨观测的身份匹配，并在可解释性上优于监督CNN基线。

### 研究问题
自动驾驶中的重识别通常依赖视觉外观嵌入，但易受视角、遮挡、光照和传感器域变化影响，缺乏可解释性和鲁棒性。本文研究能否用VLMs生成的语义描述代替视觉特征进行身份匹配。

### 核心思路/方法
提出零样本管道：使用视觉-语言模型为检测到的交通参与者生成结构化语义属性描述（包括类别、颜色、形状、姿态、可见部分、空间上下文和独特视觉线索），然后基于这些文本描述进行跨观测的身份匹配，而非依赖底层视觉相似性。

### 主要贡献
1. 首次为自动驾驶场景建立基于语言的重识别基准研究。
2. 证明零样本语义描述能实现有效对象重识别，检索性能与监督CNN基线相当。
3. 通过显式身份线索提供更高可解释性。

### 局限性
摘要明确指出两大挑战：
- 属性描述在不同视角下不一致。
- 对视觉相似实例的细粒度鉴别能力有限。

摘要未提供的信息包括：具体模型架构、数据集规模、完整实验结果对比等，均明确标记为“摘要未提供足够信息”。

### 阅读优先级
**中**  
理由：本研究属于自动驾驶重识别领域的新范式（语言驱动的零样本方法），思路新颖且提供了与监督CNN基线的对比，但摘要明确指出了匹配性能和细粒度方面的局限性，且未提供完整实验细节，适合对该方向有兴趣的读者快速了解基线框架，而非深度使用。

</details>

<details>
<summary>Abstract</summary>

Re-Identification (ReID) in autonomous driving is typically formulated as a visual matching problem, where observations of vehicles, pedestrians, and cyclists are associated across time, frames, or camera views using learned appearance embeddings, often complemented by motion, geometric, or multimodal cues. However, purely visual representations may be sensitive to viewpoint, occlusion, illumination, and sensor-domain variations, limiting their interpretability and robustness in complex driving scenes. We propose a baseline study of a zero-shot pipeline using Vision-Language Models (VLMs) to generate textual descriptions of detected traffic participants and evaluate whether these descriptions can support identity matching across observations. Instead of relying only on low-level visual similarity, the proposed formulation represents each object through structured semantic attributes, including category, color, shape, pose, visible parts, spatial context, and distinctive visual cues. This study provides an initial benchmark for language-based re-identification in autonomous-driving scenarios, discussing and evaluating the strengths and limitations of current VLMs for this task. Results demonstrate that zero-shot semantic descriptions can support effective object re-identification, achieving retrieval performance comparable to a supervised CNN baseline while offering greater interpretability through explicit identity cues. However, the experiments also reveal important challenges, including attribute inconsistency across viewpoints and limited fine-grained discrimination between visually similar instances.

</details>

#### 2026-06-08 - VGP-Nav: Metric-Aware Visual Geometric Perception for Robot Navigation

**Authors:** Hewei Pan, Weiye Zhu, Zekai Zhang, Zitong Huang, Rongtao Xu, Jinbao Wang, Feng Zheng
**Links:** [abs](https://arxiv.org/abs/2606.09268) - [pdf](https://arxiv.org/pdf/2606.09268)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VGP-Nav: Metric-Aware Visual Geometric Perception for Robot Navigation
- 作者：Hewei Pan, Weiye Zhu, Zekai Zhang, Zitong Huang, Rongtao Xu, Jinbao Wang, Feng Zheng
- 出版日期：2026-06-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.09268

### 一句话总结
本论文提出VGP-Nav，一个仅依赖单目RGB相机的统一框架，通过将视觉几何与地面平面几何的尺度约束相结合，同时实现精确的全局定位和稠密的度量障碍物感知，从而支持低成本的自主机器人导航。

### 研究问题
如何在仅使用单目视觉（无主动传感器如LiDAR）的情况下，同时实现高效、全局一致的定位和稠密、具有度量一致性的障碍物几何感知，以支持可靠的机器人导航？现有单目系统难以同时满足这两个需求。

### 核心思路/方法
核心洞察是将基于定位的视觉几何锚定到由地面平面几何导出的物理有意义的尺度约束上。具体而言，该方法利用地面平面几何作为度量参考，在线解决单目视觉的尺度模糊性，从而生成直接可用于下游路径规划的、定位锚定的度量障碍物表示。

### 主要贡献
1. 提出了一个统一的单目视觉框架（VGP-Nav），同时支持度量级定位和障碍物感知，无需多传感器融合。
2. 利用地面平面几何提供可靠的度量参考，在线解决单目尺度模糊性。
3. 在多种不同环境中展示了强大的泛化能力，并成功在实际移动机器人上部署，证明其可扩展性、低成本和安全性的实用性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
低。理由：论文标题和摘要聚焦于机器人导航的工程应用，提出了一个巧妙的单目视觉解决方案。如果读者的兴趣是感知理论或通用视觉方法，该工作的创新点较为具体（地面平面约束），且摘要未提供定量实验结果或与SOTA的详细对比。适用于对低成本导航系统设计感兴趣的读者，但对纯方法论研究者帮助有限。

</details>

<details>
<summary>Abstract</summary>

Reliable robotic navigation necessitates the seamless integration of accurate global localization and dense, metric-consistent obstacle perception. A common strategy to achieve these capabilities involves integrating diverse sensing modalities: cameras offer rich visual features for localization, while active sensors like LiDAR provide direct metric measurements. However, such multi-sensor configurations necessitate complex spatial-temporal calibration and increase deployment overhead. Although vision-only approaches offer a low-cost and scalable alternative, existing monocular visual systems typically struggle to simultaneously achieve efficient, globally consistent localization and dense, metric-consistent geometric perception. To bridge this gap, we propose \textbf{VGP-Nav}, a unified framework for \textit{Metric-Aware Visual Geometric Perception} that relies solely on monocular RGB input to jointly support metric localization and obstacle perception. Our key insight is to anchor localization-grounded visual geometry to physically meaningful scale constraints derived from ground-plane geometry, thereby providing a reliable metric reference for monocular perception. VGP-Nav resolves monocular scale ambiguity online and produces localization-grounded, metric obstacle representations that are directly applicable to downstream planning. Extensive experiments demonstrate strong generalization across diverse environments and successful deployment on real mobile robots, highlighting the practicality of our approach for scalable, low-cost, and safe autonomous navigation.

</details>

#### 2026-06-08 - Trajectory Optimization in Single and Dual-UAV Bearing-Only Target Localization

**Authors:** Zhijian Xiao, Huayu Huang, Bin Li, Yang Shang, Banglei Guan
**Links:** [abs](https://arxiv.org/abs/2606.09188) - [pdf](https://arxiv.org/pdf/2606.09188)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：单机与双机仅测角目标定位中的轨迹优化
- 作者：Zhijian Xiao, Huayu Huang, Bin Li, Yang Shang, Banglei Guan
- 出版日期：2026-06-08
- 分类：Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：https://arxiv.org/abs/2606.09188

### 一句话总结
本文提出一种基于Fisher信息矩阵的无人机轨迹优化方法，通过引入谱加权目标和视线角正弦项，显著提升了单机和双机仅测角定位的精度与鲁棒性。

### 研究问题
如何通过优化无人机轨迹，在仅测角（bearing-only）目标定位场景下建立有利的观测几何，从而提高目标定位精度。

### 核心思路/方法
1. 构建基于Fisher信息矩阵（FIM）的优化框架，动态集成几何构型与无人机机动性。
2. 提出“谱加权FIM目标函数”，在退化构型附近提供更优的梯度动态，使规划器能快速摆脱不良观测条件。
3. 针对双机场景，引入“交会角正弦项”，通过优化视线交会角改善三角测量几何，防止轨迹聚集。
4. 改进粒子群优化（PSO）算法，加入运动模型约束与粒子归一化，确保轨迹物理可行性，增强与目标函数的兼容性。

### 主要贡献
1. 提出一种结合FIM与运动约束的轨迹优化方法，适用于单/双UAV仅测角定位。
2. 在单机场景下，中位定位误差相比传统FIM方法降低99.21%；双机场景下提升69.70%。
3. 改进PSO算法，保证轨迹的物理可行性与函数适配性。
4. 在远程高机动目标的长时仅测角定位中表现出优越性能。

### 局限性
摘要未提供足够信息。具体局限性包括：未讨论实际飞行实验验证、未分析算法计算复杂度、未提及对初始轨迹的敏感性或环境干扰的鲁棒性等。

### 阅读优先级
**高**  
理由：该方法在单/双机仅测角定位中取得了显著的精度提升（误差降低超99%），改进的FIM与PSO策略具有理论创新性，适合关注无人机自主导航、目标定位与轨迹优化的研究人员阅读。

</details>

<details>
<summary>Abstract</summary>

Bearing-only target localization is a fundamental problem in optical measurement and finds extensive applications in unmanned aerial vehicle (UAV) technology. Effective trajectory planning establishes favorable observation geometries, thereby enhancing the target localization accuracy of bearing-only UAV systems. This paper proposes an trajectory optimization method for unmanned aerial vehicles (UAVs) in bearing-only target localization scenarios. By leveraging the Fisher Information Matrix (FIM), the proposed approach dynamically integrates the geometric configuration and vehicle maneuverability into the optimization framework. Specifically, we introduce a spectrally-weighted FIM objective function that provides better gradient dynamics near degenerate configurations, enabling the planner to rapidly escape from poor observation conditions. For dual-UAV scenarios, an intersection angle sine term is introduced to optimize triangulation geometry by improving the sight-line intersection angle, thereby preventing trajectory aggregation. Furthermore, we propose an improved Particle Swarm Optimization (PSO) algorithm with motion model constraints and particle normalization to ensure the physical feasibility of the trajectory and enhance the compatibility with the objective functions. Simulation results demonstrate that the proposed method reduces the median localization error by 99.21% compared to conventional FIM-based approaches in single-UAV scenarios, and achieves a 69.70% improvement for dual-UAV configurations, exhibits superior performance in long-duration bearing-only target localization of maneuverability targets at extended ranges.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
