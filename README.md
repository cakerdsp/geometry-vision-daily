# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：6
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 4
  - Embodied / Robotics / AR Applications: 1
  - Neural Scene Representations & Rendering: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，基于今日提供的论文列表，以下是针对计算机视觉与三维重建领域的科研趋势综合分析。

---

#### 今日主要趋势

1.  **从单目到“隐式多视图”的范式转变：挖掘单张图像中的多重几何线索**
    传统单目3D重建面临不适定问题，而今日趋势显示，研究者们正积极从单张图像中挖掘“隐式多视图”信息。例如，`MooMIns` (2606.14389) 巧妙地利用了工业场景中堆叠的多个物体实例，将其视为同一物体的多视图观测，并创新性地反转了高斯溅射的经典流程（从“多相机渲染单场景”变为“单相机渲染多实例”）。这表明未来研究方向正从依赖显式的多视角输入，转向利用场景中的重复结构或物理先验来创造几何约束。

2.  **端到端与任务统一化：深度融合传统几何与学习范式**
    多个工作展现了将传统几何算法（如SfM、光线投射、可微分优化）与深度学习特征提取、任务解码头（如全景分割）进行端到端融合的趋势。`StereoGeo` (2606.14619) 将基于学习的特征提取与可微分优化器结合，实现立体相机联合标定。`Pano3D` (2606.14307) 则明确地将底层的几何重建与高层的全景分割任务统一在一个前馈网络框架下，并证明任务间的相互促进。这反映了领域内试图打破“几何”与“语义”壁垒，构建更强健、更通用3D理解模型的努力。

3.  **对3D视觉系统鲁棒性进行多层次审视：从算法到物理层面**
    除了追求更好的性能，安全性研究成为新热点。`Scratched Lenses` (2606.14504) 跳出了传统对抗攻击（如patch或投影）的框架，揭示了由物理硬件损伤（镜头划痕）引入的、场景触发的安全漏洞。这标志着3D视觉的安全性研究已从纯“数字域”攻击扩展到“物理-光学-算法”的复合层面，促使研究者关注现实世界中不可忽视的物理退化对几何推理的影响。同时，`BIM-Loc` (2606.14237) 对“设计模型”与“真实环境”之间差异的感知，也体现了面向实际应用时的鲁棒性考量。

4.  **神经场景表示中的高效表示与基础性研究回归**
  `Beyond Spherical Harmonics` (2606.09794) 并非提出全新框架，而是回归到对基本数学模型（球面函数）的系统性评估与替换。针对神经辐射场中高频外观模型（如镜面反射）与计算/内存开销的经典矛盾，该工作通过实验驱动的方式提出更高效的基函数。这表明当NeRF等场景表示方法逐渐成熟后，学术界开始重新审视其底层组件，通过优化基础函数来获得量级级别的效率提升，而非仅仅依赖更深的网络或更复杂的架构。

#### 技术路线观察

-   **几何基础模型**：今日论文中，**可微优化器** (StereoGeo)、**运动恢复结构（SfM）** (MooMIns)、**光线投射** (BIM-Loc) 等经典几何算法模型仍作为核心模块被集成。不同之处在于，这些几何模块现在被设计成可学习的“管道”或“层”，与神经网络深度耦合。
-   **3D/4D 重建**：**高斯溅射 (Gaussian Splatting)** 的灵活运用是亮点。`MooMIns` 对其经典流程进行了反向推理，展示了Gaussian Splatting作为表示和渲染工具的模块化潜力。而 `Pano3D` 则代表了**前馈式（feedforward）Transformer重建网络**与语义理解的集成，是另一种主流路线。
-   **神经场景表示与渲染**：主要关注点集中在**效率**上。`Beyond Spherical Harmonics` 不依赖于改进网络架构，而是通过引入新的、更高效的数学基函数（Normalized Anisotropic Spherical Gabor）来优化表示本身。这暗示了一个“返璞归真”的趋势：通过优化基础数学工具来提升表达能力和运行速度。
-   **机器人/AR应用**：论文如 `BIM-Loc` 直接面向**实用化**和**鲁棒性**。该技术路线强调利用现有信息（如BIM设计图纸）来弥补传感器数据的不足，并在线感知模型与真实环境的偏差，这对于工业巡检、室内服务机器人等应用场景至关重要。

#### 值得优先阅读的论文

1.  **Pano3D (2606.14307)** - **阅读优先级：高**
    - **理由**：该文最具当前趋势代表性，完美融合了**几何重建**与**语义理解**（全景分割）两大任务，并在ScanNet等多个数据集上取得SOTA，具备很强的实用价值和启发意义。

2.  **Beyond Spherical Harmonics (2606.09794)** - **阅读优先级：高**
    - **理由**：直击神经渲染领域的核心计算瓶颈（高频表示与效率的权衡），提出了一种系统性的评估方法和改进方案（新基函数），报告了**5倍内存节省**，对希望优化现有NeRF或3D Gaussian模型的研究者极具参考价值。

3.  **BIM-Loc (2606.14237)** - **阅读优先级：高**
    - **理由**：技术架构清晰且创新（多命中射线投射、差异感知），并且直接面向机器人定位这一硬核应用，能启发如何将“不完美”（设计图纸）与“现实”（传感器数据）结合的研究思路。其模拟和真实实验的双重验证也增加了可信度。

4.  **MooMIns (2606.14389)** - **阅读优先级：中**
    - **理由**：提出了利用“隐式多视图”这一非常有启发性的思路，并且巧妙反转了Gaussian Splatting流程，概念层面创新性突出。阅读优先级低于前三篇是因为其应用场景相对局限（特定工业堆叠场景）。

#### 可能的研究机会

1.  **“隐式多视图”的通用化**：`MooMIns` 的思路能否扩展到非工业场景？例如，在自动驾驶中，同一类别的目标（如行人、车辆）是否可以被视为提供隐式视图的“实例”？或者，能否通过合成数据的扩散模型，人为创造多实例去辅助单目重建？
2.  **物理攻击防御**：`Scratched Lenses` 揭示了镜头物理损伤的威胁。直接的研究机会是设计**对抗或鲁棒的光学硬件设计**，或是开发**在线检测与消除此类光学伪影的算法**。这将是连接光学、物理和算法的交叉方向。
3.  **统一框架下的双向促进**：`Pano3D` 证明了几何和语义在统一框架中的互利。下一个机会是**将这种范式推广到时间维度（4D）**，例如在动态场景重建中，如何让时域运动和语义分割任务相互促进。
4.  **新型基函数与场景表示架构的结合**：`Beyond Spherical Harmonics` 提出的新基函数可以立即应用于当前各类场景表示（如3D Gaussian Splatting、Tri-planes等），有望在不显著增加模型复杂度的情况下提升渲染质量。将其与**极端的压缩技术**或**实时渲染管线**结合是很有价值的方向。
5.  **消除设计-现实鸿沟的持续学习**：`BIM-Loc` 只是在线检测与BIM的差异。进一步的研究可以是**利用这些差异信息进行在线地图更新**，即让机器人从未被设计图中预期的环境变化中学习，实现真正的持续学习与地图自适应。

#### 风险和不确定性

-   **实验规模和对比基线**：所有论文的结论均基于**摘要**。`StereoGeo` 和 `MooMIns` 声称效果优于现有方法，但优势大小、对比基线的具体配置和数据集规模需要在**全文**中确认。`Pano3D` 和 `BIM-Loc` 在多个数据集上有结果，但具体指标和显著性检验需全文验证。
-   **物理攻击的可重复性与泛化性**：`Scratched Lenses` 的SLASH攻击在真实实验里需要多大的划痕、在多强的光源下才能成功？其攻击效果对不同模型（

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

No papers in the current README window.

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
