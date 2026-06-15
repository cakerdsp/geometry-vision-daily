# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：16
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 6
  - Embodied / Robotics / AR Applications: 5
  - Neural Scene Representations & Rendering: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，以下是根据您提供的论文列表生成的中文科研趋势综合分析。

---

#### 今日主要趋势

1.  **从“单视角/场景”到“多实例/多视角协同”的几何与感知：** 本日论文中一个显著趋势是突破传统单目/单个场景的限制，转向利用“多”的优势。这体现在两个方面：一是利用同一图像中**多个物体实例**隐式提供的多视图几何信息，从本质上的不适定问题中求解3D结构（如`MooMIns`利用堆叠物体进行重建与位姿估计）；二是针对**多个智能体**（如多无人机、多视角摄像机）的场景，探索如何保证跨视角感知的几何一致性与可控性（如`Prisma-World`生成多智能体视角一致的视频，`Trajectory Optimization in Single and Dual-UAV`优化双机观测几何）。这表明研究正从孤立感知走向协同和互补性几何推理。

2.  **对感知系统鲁棒性与实用性的深刻关注：** 研究重点不再局限于干净环境下的性能提升，而是更多地考虑真实世界中的不理想因素。这具体表现为三类工作：一是**对抗性攻击**研究，发现硬件物理损伤（如镜头划痕）可作为新的被动攻击面，扰乱深度估计（`Scratched Lenses`），挑战了传统对攻击面的认知；二是**低成本与自动化**，利用设计阶段的建筑信息模型（BIM）替代昂贵的预先地图进行室内定位（`BIM-Loc`），或用纯单目视觉结合地面几何约束实现度量级导航（`VGP-Nav`），降低了部署门槛；三是**零样本与语义化**，探索用VLM生成的语义描述代替视觉特征进行目标重识别（`Zero-Shot Semantic Re-Identification`），追求更强的可解释性和鲁棒性。

3.  **神经渲染进入“精细化”与“工程化”阶段：** 以3DGS和NeRF为代表的神经渲染技术，正从基础框架构建迈向对核心环节的精细优化和面向应用的有效组合。一方面，`REFINE`和`Beyond Spherical Harmonics`分别针对3DGS的**剪枝效率**和**外观建模**两大核心痛点，提出理论驱动的解析解与新型基函数；另一方面，`Leveraging NeRF-Rendered Images for 3DGS`利用NeRF生成高质量训练数据来“指导”3DGS训练，`MaterialClusterGS`则引入调色板概念解决材质分解中的欠约束问题。这表明领域正从“能否实现”转向“如何更高效率、更高质量、更易编辑地实现”。

4.  **自动驾驶感知中的“轻量级”与“先验驱动”求解器：** 在自动驾驶和机器人应用的几何估计问题上，多篇论文聚焦于设计高效的最小求解器（`Efficient Minimal Solvers`系列）。它们共同的核心策略是：通过创新的参数化方法，并充分利用IMU提供的**强先验信息**（如垂直方向、旋转轴方向）或车辆的运动约束（如平面运动），大幅减少对特征点数量的需求和计算复杂度。这不仅提升了实时性，也增强了对特征缺失场景的鲁棒性，代表了实际部署中的重要技术路线。

---

#### 技术路线观察

- **几何基础模型（3D Reconstruction & Multi-view Geometry）**：这部分论文的技术路线呈现多元化。`StereoGeo`延续了“学习+可微分优化”的深度学习标定范式；`MooMIns`和`Pano3D`则代表了“重建与感知任务联合”的趋势，前者创新性地反向使用高斯溅射，后者则为前馈网络附加语义解码器。而多篇`Efficient Minimal Solvers`坚持了经典的“解析几何+鲁棒估计”路线，通过代数技巧和先验信息实现高效求解。

- **神经场景表示与渲染（Neural Scene Representations & Rendering）**：技术路线正从“渲染质量”和“速度”的基本盘转向“可编辑性”与“效率”。在3DGS领域，`REFINE`追求剪枝效率，`MaterialClusterGS`追求材质编辑的一致性。在更广泛的外观模型上，`Beyond Spherical Harmonics`尝试用更高效的基函数替代经典方法。同时，不同表示方法之间的“混合”策略，如`Leveraging NeRF-Rendered Images for 3DGS`，成为一种实用的技术路线。

- **具身/机器人/AR应用（Embodied / Robotics / AR Applications）**：技术路线强调**实用性**和**健壮性**。
    - **导航与定位**：从依赖多传感器融合（LiDAR+相机）的趋势中，出现了向**单目视觉**（`VGP-Nav`）和**利用建筑设计模型**（`BIM-Loc`）的转移，追求低成本、高自动化的解决方案。
    - **传感器与系统级安全**：`Scratched Lenses`从物理硬件漏洞出发，开创了一种新型的安全攻击面，这是对现代视觉系统鲁棒性的一种逆向思维挑战。
    - **世界模型的构建**：`Prisma-World`代表了从单智能体视频生成向**多智能体、几何一致的未来帧预测**的跨越，这需要更复杂的数据集和联合生成机制。

---

#### 值得优先阅读的论文

1.  **Pano3D**：**理由**：它成功地将3D重建与3D全景分割统一在一个框架中，解决了前馈重建网络缺乏语义理解的关键开放性问题，并通过实验证明了几何与语义学习可以互相促进。其方法通用性强，能适配多种骨干网络，对推动3D视觉的综合性发展具有里程碑式意义。
2.  **REFINE**：**理由**：针对3DGS剪枝这一实际部署的核心痛点，提出了一个优雅且高效的理论解。通过解析推导重要性度量，避免了计算昂贵的渲染过程，实现了3000倍加速。对关注神经渲染压缩、高效表示及边缘部署的研究者而言，这是必读之作。
3.  **BIM-Loc**：**理由**：该工作解决了机器人室内定位中一个非常现实的工程问题——如何在无法预先构建精确地图的情况下利用设计蓝图。其“差异感知”的在线更新机制，使得定位系统能适应环境变化，思路新颖且极具应用价值，对SLAM和机器人定位方向有重要启发。
4.  **Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields**：**理由**：该工作直面了当前3DGS逆渲染方法中因管线不一致（光栅化 vs. 路径追踪）带来的伪影问题。通过设计的“路径空间等效交互模型”，首次在3DGS中实现了统一的、支持全局光照的路径追踪逆渲染，理论坚实，有望成为该领域的新标准。
5.  **Beyond Spherical Harmonics**：**理由**：对于任何从事神经渲染或可微渲染的研究者来说，该工作挑战了球谐函数作为“万金油”的惯例。其系统性评估并引入新型球面函数，为建模视角依赖的复杂高频效果（如镜面反射）提供了更紧凑、更高效的新工具，可能引发外观表示方法的革新。

---

#### 可能的研究机会

1.  **融合多视角一致性先验的世界模型**：`Prisma-World`展示了如何生成多视角一致的视频。未来的研究可以进一步探索如何将这种通过全局注意力机制实现的“几何一致性”与物理知识或因果推断结合，使生成的世界模型具有更好的泛化性和可解释性。

2.  **物理损伤感知的鲁棒视觉系统**：`Scratched Lenses`揭示了硬件损伤是潜在的攻击面。反向思考，是否可以研发一种算法，能够**主动检测并补偿**视觉系统中由灰尘、划痕或光学畸变引起的结构化的分布外噪声，从而提升系统的整体鲁棒性和安全性？

3.  **神经渲染与经典几何/估计器的深度结合**：从`MooMIns`和`Leveraging NeRF-Rendered Images for 3DGS`中可以看到神经渲染与经典SfM或基于图像的渲染结合的潜力。未来的研究可以探索如何利用3DGS或NeRF的连续/显式表示，为传统的视觉里程计、SLAM或3D重建问题提供更鲁棒的中间表征（如深度、法向、梯度），或用于生成高质量的伪标注数据来训练其他模型。

4.  **基于语义的、可交互的3D资产创建与

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-14T22:27:58-04:00
**Total number of papers:** 6
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
<summary>AI 简析</summary>

### Metadata
- 标题：StereoGeo: an end-to-end stereo camera calibration method
- 作者：Imane Meddour, Andréa Macario Barros, Cédric Gouy-Pailler
- 出版日期：2026-06-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.14619

### 一句话总结
本文提出了一种基于端到端网络的立体相机标定方法StereoGeo，能够同时估计左右相机的焦距、重力方向以及两者之间的相对外参。

### 研究问题
如何设计一种端到端的方法，在无需结构化环境中的标定图案、且不局限于单目或多视角设置的情况下，同时完成立体相机的内参（焦距、重力方向）和外参（相对位姿）标定。

### 核心思路/方法
扩展GeoCalib算法，将深度神经网络的特征提取与可微分优化器相结合，构建一个端到端的网络架构，用于立体相机标定。

### 主要贡献
1. 提出了StereoGeo，首个端到端的立体相机标定网络，同时估计左右相机的焦距、重力方向及相对外参。
2. 在真实世界基准数据集上，该方法在内参标定上达到有竞争力表现，并在立体外参估计上准确度优于现有的单目方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法聚焦于立体相机标定这一专业子领域，解决了现有方法在端到端联合标定上的不足，但论文公开的摘要篇幅有限，缺乏对方法架构细节、实验设置和量化结果的深入描述，适合对该方向有特定需求的读者作为参考。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Scratched Lenses, Shifted Depth: Passive Camera-Side Optical Attacks
- 作者：Qinlin He, Zeming Zhuang, Yongji Wu, Lan Zhang, Xiaoyong, Yuan
- 出版日期：2026-06-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.14504

### 一句话总结
本文提出一种新型被动摄像端物理对抗攻击：通过在镜头或保护罩上制造微小划痕，当特定视觉条件（如强光源、镜面反射）触发时，划痕会产生结构化的光学伪影，从而扭曲单目深度估计和3D目标检测中的深度信息。

### 研究问题
- 如何利用摄像端物理损伤（如镜头划痕）作为持久的、场景触发的对抗攻击，来误导几何推理（尤其是深度估计）？

### 核心思路/方法
- 将攻击建模为光学空间中的触发条件通道：划痕作为固定但场景触发的光学扰动源。
- 提出SLASH（Scratch-induced Lens Adversarial Streak Hijacking）攻击：利用微小划痕与明亮光源、镜面反射交互产生条纹伪影，扭曲深度线索。
- 在数字和真实世界中评估：分别测试单目深度估计和单目3D目标检测任务；物理实验验证攻击可从数字仿真迁移至真实相机录制结果。

### 主要贡献
- 识别了一种新的对抗攻击表面：看似无害的硬件缺陷（如镜头划痕）可作为潜在、场景触发的对抗机制。
- 提出并验证了SLASH攻击：在固定划痕约束下，单目深度估计的相对误差可达32%。
- 证明了该攻击在物理世界中的可迁移性：真实相机录制结果显示深度偏移超过模型自然预测基线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该工作揭示了硬件物理损伤作为新攻击面的安全风险，对3D视觉系统鲁棒性研究有启发意义。但方法聚焦于特定物理实现（镜头划痕），且未在摘要中提供防御思路或大规模基准对比，适合对对抗攻击与3D视觉交叉领域感兴趣的研究者，非该领域读者优先级可适度降低。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MooMIns -- Monocular 3D Reconstruction and Object Pose Estimation from Multiple Instances
- 作者：Robert Langendörfer, Markus Hillemann, Markus Ulrich
- 出版日期：2026-06-12T12:24:50Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.14389

### 一句话总结
提出一种基于高斯溅射（Gaussian-splatting）的框架MooMIns，通过利用单张单目图像中同一物体的多个实例，同时实现3D重建和6D位姿估计。

### 研究问题
如何从单张单目图像中同时进行3D重建和6D物体位姿估计？原始问题本身是不适定的，但工业场景中堆叠物体提供隐式多视图线索，可被利用来解决此问题。

### 核心思路/方法
- 反向高斯溅射：将原始高斯溅射的“从多相机渲染单场景”反转，变为“从单相机渲染多物体实例”。
- 初始化：使用SAM3实例分割掩码和修改后的运动恢复结构（SfM）流水线。
- 几何重建：强调基于图像证据的真正几何重建，而非基于训练数据先验的深度估计，避免产生幻觉。

### 主要贡献
- 提出MooMIns框架，利用单张图像中多个物体实例的隐式多视图几何。
- 在合成与真实堆叠抓取场景下，实现高精度的3D重建和可靠的单实例6D位姿估计。
- 不同于基于学习的单目深度估计，方法避免了训练数据的先验偏差。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中** —— 该方法针对工业堆叠场景中的3D重建与位姿估计，思路新颖，反向利用了高斯溅射，但评估仅提及合成和真实场景，缺乏与主流方法的定量对比细节。对单目重建与位姿估计方向的研究者有一定参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Pano3D: Unified 3D Reconstruction and Panoptic Segmentation
- 作者：Victor Barberteguy, Ahmet Iscen, Mathilde Caron, Alireza Fathi, Gül Varol, Cordelia Schmid
- 出版日期：2026-06-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2606.14307) | [PDF](https://arxiv.org/pdf/2606.14307)

### 一句话总结
本文提出一种统一框架，将前馈式3D重建网络与基于集合的掩码解码器结合，实现无需相机参数的3D重建与全景分割联合学习，并在多个数据集上达到最优性能。

### 研究问题
如何使前馈式3D重建神经网络在无需相机参数的情况下，同时具备鲁棒的3D全景分割语义理解能力？

### 核心思路/方法
- 在现有3D重建模型基础上，增加一个基于集合的掩码解码器。
- 联合训练几何损失和语义损失，使几何特征与语义特征相互促进。
- 特征初始化时利用几何信息，然后微调以同时捕获几何与语义。
- 方法适用于在线注意力和全对注意力两种重建骨干网络。

### 主要贡献
1. 首次在统一框架中实现3D重建与3D全景分割的联合学习。
2. 通过共享训练目标，证明了几何与语义损失具有相互促进作用。
3. 在ScanNet、ScanNet200和ScanNet++数据集上取得了3D全景分割的最优结果。
4. 消融实验表明联合训练能为前馈式3D重建网络提供全景分割能力，并实现双向性能提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该方法将3D重建与全景分割统一在单框架中，兼具理论创新（特征联合初始化与微调）和实际性能（SOTA结果），且泛化至多种骨干网络，对3D视觉领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D feedforward reconstruction neural networks have achieved remarkable success in dense reconstruction from images without any camera parameters. Yet, equipping these models with robust semantic understanding remains an open problem. Here we introduce an approach that performs 3D reconstruction and 3D panoptic segmentation in a unified framework. We build on existing 3D reconstruction models and augment them with a set-based mask decoder. The approach is jointly trained with a geometric and semantic loss, which are shown to be mutually beneficial. More precisely, the features are initialized from the geometric information and then finetuned to capture jointly geometry and semantics. We demonstrate the generality of our approach by successfully applying our framework both to online and all-to-all attention reconstruction backbones. Our method achieves state-of-the-art performance in 3D panoptic segmentation across ScanNet, ScanNet200, and ScanNet++ datasets. Ablation studies show that such joint training of a unified model equips 3D feedforward reconstruction neural networks with panoptic segmentation and yields mutually beneficial improvements.

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

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-12 - BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization

**Authors:** Yinqiang Zhang, Liang Lu, Yipeng Pan, Maolin Lei, Yuhan Xie, Zhanteng Xie, Xiaowei Luo, Jia Pan
**Links:** [abs](https://arxiv.org/abs/2606.14237) - [pdf](https://arxiv.org/pdf/2606.14237)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization
- 作者：Yinqiang Zhang, Liang Lu, Yipeng Pan, Maolin Lei, Yuhan Xie, Zhanteng Xie, Xiaowei Luo, Jia Pan
- 出版日期：2026-06-12T08:20:02Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.14237

### 一句话总结
本文提出一种基于LiDAR的室内定位方法BIM-Loc，通过直接集成设计阶段的建筑信息模型（BIM），在实现轨迹估计的同时在线检测真实环境与BIM之间的差异。

### 研究问题
如何在特征稀疏的室内环境中，利用设计阶段的BIM模型实现准确、鲁棒的定位，并在线检测真实观测与BIM之间的不一致性。

### 核心思路/方法
1. **多命中射线投射策略**：高效实现BIM与点云数据的关联，并将3D观测投影到2D纹理空间。
2. **BIM集成因子的姿态图优化框架**：联合优化里程计、序列扫描与BIM结构之间的约束一致性。
3. **分层贝叶斯推理模块**：增量更新连续2D表面表示，用于检测不一致性，实现从像素级到结构级的传播更新。

### 主要贡献
1. 提出一种直接集成BIM的LiDAR定位方法，无需依赖精确的预先地图。
2. 创新性地将定位与BIM-现实差异检测在线融合。
3. 通过模拟与真实实验证明，在定位精度与鲁棒性上显著优于现有基于地图的方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对服务与巡检机器人等实际应用中常见的特征稀疏室内环境，提出一种无需预先精确地图即可利用设计阶段BIM的定位方案，具备很强的实用价值。方法上引入差异感知与在线更新机制，创新性明确，且已在模拟与真实场景中验证性能优势。适用于从事机器人定位、BIM应用或室内导航的研究者。

</details>

<details>
<summary>Abstract</summary>

Accurate and robust localization is a fundamental requirement for service and inspection robots, particularly in feature-sparse indoor environments where traditional systems struggle due to a lack of distinct landmarks. While prior maps can enhance robustness, precise and compact maps capturing real-world details are often unavailable for new or frequently changing environments. This paper presents BIM-Loc, a novel discrepancy-aware LiDAR-based localization method that directly integrates Building Information Models (BIM) from the design phase. BIM-Loc simultaneously estimates trajectories aligned with the BIM coordinate system and identifies discrepancies between real-world observations and the as-designed BIM in an online fashion. Our core contributions include: (1) a novel multi-hit ray casting strategy for efficient BIM-point data association and projection of 3D observations into 2D texture space; (2) a pose graph optimization framework with BIM-integrated factors that enforces consistency among odometry, sequential scans, and BIM structures; and (3) a hierarchical Bayesian inference module that incrementally updates a continuous 2D surface representation for discrepancy detection, propagating updates from the pixel to the structure level. Extensive evaluations in both simulation and real-world applications demonstrate that BIM-Loc significantly outperforms state-of-the-art map-based methods in localization accuracy and robustness.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
