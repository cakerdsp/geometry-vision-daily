# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：49
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 14
  - Neural Scene Representations & Rendering: 14
  - Embodied / Robotics / AR Applications: 13
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，基于您提供的论文列表，以下是针对今天科研趋势的综合分析。

---

#### 今日主要趋势

1.  **从静态重建到动态与未来预测的范式迁移**：一个明显的趋势是，研究不再满足于静态场景的3D重建，而是深入探索动态场景的建模、合成，甚至超越观测窗口进行未来预测。代表性论文包括：
    - **GrainGS** 和 **FA-LAM** 专注于动态/4D场景的高效与新视角合成，后者更关注可动画化的人头模型。
    - **FutureSurf** 直接提出了一个关于“未来表面重建”的基准和数据集，明确将评估指标从当前观测窗口延伸到未来时刻，标志着该领域评估范式的转变。

2.  **高斯泼溅（3DGS）作为核心支柱，持续演化与融合**：3DGS已从单纯的渲染技术演变为诸多任务的基石和工具。论文展示了其在**前馈式重建**、**动态重建**、**SLAM**、**数据合成（用于去模糊）** 以及**混合现实比较**等方向上的广泛适应性和深度融合。代表性论文包括：
    - **ATSplat** 和 **SubSplat** 分别从自适应容量分配和亚像素分辨率两个角度改进前馈式3DGS。
    - **GLAM-SLAM** 将3DGS与SLAM结合，解决大规模室外场景的实时性问题。
    - **RealVDeblur** 利用3DGS构建物理真实的数据合成管道，服务于视频去模糊任务。
    - **MR-Compare** 则利用3DGS进行混合现实环境下的重建质量对比。

3.  **鲁棒性与泛化性：应对恶劣条件与特定领域挑战**：多个工作针对特定领域或恶劣条件，提出了增强鲁棒性的解决方案，推动了从理想环境到真实世界的应用。代表性论文包括：
    - **WAT3R** 专门解决水下环境的光学衰减和散射问题，实现前馈式水下3D重建。
    - **DAPM** 针对无人机航拍中高度动态的视角（高度、俯仰、翻滚角）设计，提升单目深度估计的泛化能力。
    - **Boosting Robustness for All-Weather...** 则专门应对自动驾驶在雨、雾等恶劣天气下自监督深度估计的鲁棒性问题。

4.  **解耦表征与知识蒸馏：破解复杂任务中的“纠缠”问题**：面对复杂任务（如视频动态、多任务学习），研究者倾向于通过解耦、路由和蒸馏等技术，将复杂问题分解或转移知识，从而提升模型效率与性能。代表性论文包括：
    - **Self-Supervised Learning of Structured Dynamics from Videos** 的目标就是解耦视频中的相机运动与物体运动。
    - **PerceptDrive** 采用自适应专家路由机制，从冻结的感知基础模型中蒸馏先验知识，服务于端到端驾驶规划。
    - **FA-LAM** 通过双阶段训练显式地解耦重建与动画任务的目标冲突。
    - **Boosting Robustness for All-Weather...** 通过多教师蒸馏（Multi-Teacher Distillation）在恶劣天气下提供鲁棒的深度估计先验。

#### 技术路线观察

- **Geometry Foundation Models / 3D Reconstruction & Multi-view Geometry**: 这批论文技术高度务实，针对特定传感器（平面Lidar, 单目UAV）和特定环境（水下）设计轻量级或专用网络。**变分推断被弱监督与自监督策略取代**，例如**DAPM**利用几何先验间接监督、**WAT3R**的退化适配模块、**Factorized Spatio-Temporal Convolutions**的跨模态自监督。**核心创新在于从数据表征或网络结构入手，而非模型架构本身的革命性突破**。

- **Dynamic / 4D Reconstruction**: 与静态场景不同，动态重建的核心难题是**运动建模与结构稳定性的平衡**。**GrainGS**采用了**层级锚定+每高斯形变**的结构，并通过**梯度解耦**来巧妙分离两者，代表了动态重建中一种精细化控制的趋势。**FA-LAM**则从**重构与动画任务的冲突**这一更抽象的角度切入，提出解耦式训练流水线，显示出对系统级瓶颈的深入洞察。

- **Neural Scene Representations & Rendering**: **前馈式3DGS**成为一个重要子方向（**ATSplat**、**SubSplat**）。它们的共同目标是克服优化式3DGS效率低、泛化性差的缺点。**ATSplat**的亮点在于恢复了“自适应容量分配”这一核心能力；**SubSplat**则巧妙地在计算复杂度和渲染分辨率之间找到新的平衡点，**亚像素重参数化**提供了一种节省计算量的思路。**3D-GIMP**展示了**混合范式**的竞争力——用一次生成+确定性传播取代多次迭代的神经渲染，在效率和一致性之间取得了优势。

- **Embodied / Robotics / AR Applications**: 研究热点明显集中在**真实世界数据与仿真环境的桥梁构建**上。**TableVerse**的*Real2Sim*管道直接处理无约束图像生成物理真实的仿真数据，**KineBench**则通过**显式运动学接地**解决评估中的归因模糊问题。同时，**交互式决策**（**A Real-Time Generalized Nash Equilibrium...**）和**多模态先验融合**（**PerceptDrive**）代表了自动驾驶规划层面的两种主流技术路线。

#### 值得优先阅读的论文

1.  **FutureSurf (arXiv:2607.21471)**: **高优先级**。它不仅仅是提出了一个新的基准，而是定义了一个全新的评估范式——“未来表面重建”。这项工作指出了现有动态重建评估的根本盲点，对任何从事动态场景理解与重建的研究者都极具启发性。

2.  **ATSplat (arXiv:2607.20417)** & **SubSplat (arXiv:2607.20813)**: **高优先级**。这两篇代表了前馈式3DGS的两个重要进展。ATSplat解决了自适应容量分配问题，SubSplat解决了低计算成本下的高分辨率渲染问题。对比着读，可以全面了解前馈式3DGS的核心挑战和解决方案。

3.  **Self-Supervised Learning of Structured Dynamics from Videos (arXiv:2607.21576)**: **高优先级**。该工作试图从自监督角度解决视频理解中的核心难题——解耦相机和物体运动。它提出的结构化动力学模型（SDM）与纯监督方法（如VGGT）的性能对比，揭示了自监督学习的巨大潜力，是对比学习与运动表征的重要工作。

4.  **GrainGS (arXiv:2607.21448)**: **高优先级**。在动态3DGS领域，GrainGS的**梯度解耦**思想非常巧妙，解决了动态重建中“树欲静而风不止”的问题。方法设计优雅且效果显著，是该方向的标杆性工作。

#### 可能的研究机会

1.  **“未来预测”基准驱动的动态重建方法**：FutureSurf的出现为动态重建方法提出了新目标。如何设计能够显式或隐式预测未来几何的模型，将成为新的研究热点。可以探索将**神经微分方程**或**物理先验**融入4D重建框架中，以更好地泛化到未见过的未来时间点。

2.  **融合前馈与优化的混合3DGS系统**：前馈式（ATSplat、SubSplat）速度快但精度上限受限于特征，优化式（传统3DGS）精度高但慢。一个明显的机会是：**用前馈方法提供高质量初始化，再辅以轻量级微调**。GLAM-SLAM的“前端轻量追踪+后端精细建图”的解耦设计也可以为这一方向提供借鉴。

3.  **从“感知”到“行动”的无缝闭环**：KineBench精确地指出了当前世界模型评估的归因模糊问题。基于此，可以研究**将显式运动学接地直接作为世界模型输出的一部分**。KineBench的**存在即合理**——既然评估时需要显示解耦，那为什么不把它融入模型中，从而实现直接对接物理仿真器的生成模型？

4.  **基于对抗/自适应数据合成的鲁棒重建**：RealVDeblur和TableVerse都展示了合成数据的巨大价值。未来的方向是构建**对抗式退化网络**，自动生成对当前

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-24T10:09:43-04:00
**Total number of papers:** 49
**Number of papers added in the latest update:** 27
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

### 2026-07

#### 2026-07-23 - Self-Supervised Learning of Structured Dynamics from Videos

**Authors:** Lukas Knobel, Andrew Zisserman, Yuki M. Asano
**Links:** [abs](https://arxiv.org/abs/2607.21576) - [pdf](https://arxiv.org/pdf/2607.21576)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Self-Supervised Learning of Structured Dynamics from Videos
- 作者：Lukas Knobel, Andrew Zisserman, Yuki M. Asano
- 出版日期：2026-07-23
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.21576

### 一句话总结
本文提出了一种结构化动力学模型（SDM），通过结合自监督学习与弱监督，从预训练图像模型的视频特征中分解出相机运动和物体运动两种动态来源。

### 研究问题
如何从视频中恢复结构化的运动表征，将相机运动与物体运动分离开，以学习更稳健的动力学表示。

### 核心思路/方法
1. 利用预训练图像视觉Transformer的冻结特征。
2. 提出结构化动力学模型（SDM），通过未来帧特征预测，显式分离主导时间变化与残差动力学。
3. 训练结合了真实视频的自监督学习和合成Kubric数据上场景动力学的弱监督。
4. 在ProbeMotion评估套件上进行测试，该套件涵盖合成与真实视频中的相机运动、物体运动及混合动态。

### 主要贡献
1. 提出SDM模型，能够从预训练图像模型特征中提取结构化视频动力学表征。
2. 在自监督框架下实现相机运动与物体运动的分离，无需强监督。
3. 在ProbeMotion评测中，SDM优于使用全局CLS或平均池化特征的基线，并与强监督VGGT方法相比表现相当，但使用更弱的监督。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：本文针对视频理解中相机运动与物体运动解耦这一重要且未充分探索的问题，提出了结合自监督与弱监督的结构化动力学模型，在较弱的监督下取得了与强监督方法相当的效果，对运动表征学习研究具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Understanding motion in video is a fundamental challenge for visual learning, as frame-to-frame change entangles two sources of dynamics: camera motion and object motion. This decomposition has remained underexplored in representation learning, partly because these factors are tightly coupled in natural videos and difficult to supervise separately. Yet recovering it is important for learning robust motion representations that separate meaningful object dynamics from camera-induced variation. We study whether such structured motion representations can be recovered from frozen features of a pretrained image vision transformer. We propose the Structured Dynamics Model (SDM), which explicitly separates the dominant source of temporal change from residual dynamics through future-feature prediction, rather than representing video change with a single entangled latent or with unstructured, spatially dense transition tokens. Training combines self-supervised learning on real video with weak supervision of scene dynamics on synthetic Kubric data. We evaluate SDM on ProbeMotion, a new evaluation suite spanning synthetic and real videos with camera motion, object motion, and combined dynamics. SDM outperforms backbone baselines using global CLS or average-pooled features, and compares favorably to strongly supervised representations such as VGGT on several probes, despite using substantially weaker supervision. These results suggest that pretrained image models can be readily repurposed into structured video-dynamics representations, providing a useful inductive bias for learning and analyzing latent video dynamics.

</details>

#### 2026-07-21 - IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer

**Authors:** Zhengyu Zou, Hao Li, Kuixuan Jiao, Liu Liu, Tingyang Xiao, Xiaolin Zhou, Fangzhou Hong, Zhizhong Su, Dingwen Zhang, Ziwei Liu
**Links:** [abs](https://arxiv.org/abs/2607.19228) - [pdf](https://arxiv.org/pdf/2607.19228)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** feed-forward reconstruction, feed-forward 3D reconstruction, 3D reconstruction, pose estimation, scene understanding, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer
- 作者：Zhengyu Zou, Hao Li, Kuixuan Jiao, Liu Liu, Tingyang Xiao, Xiaolin Zhou, Fangzhou Hong, Zhizhong Su, Dingwen Zhang, Ziwei Liu
- 出版日期：2026-07-21
- 分类：Geometry Foundation Models（主要），3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications（次要）
- 链接：摘要: https://arxiv.org/abs/2607.19228 ; PDF: https://arxiv.org/pdf/2607.19228

### 一句话总结
提出一种流式实例-几何融合的Transformer（IGGT4D），能够在线处理视频序列，实现动态场景中几何与实例一致性的4D理解与重建。

### 研究问题
现有流式3D重构方法偏重于几何信息，缺乏时间一致的物体级别理解；而语义重建与3D视觉-语言方法多依赖外部2D语义线索或松散耦合的几何输入，无法在长时间动态场景中实现统一的几何-实例学习。因此，需要一种能在流式视频中同时保持几何和实例一致性的在线4D场景理解方法。

### 核心思路/方法
1. **流式架构**：顺序处理视频帧，通过因果时空建模复用历史上下文，增量更新包含相机运动、几何和物体标识的统一表示。
2. **数据集构建**：为解决高质量4D监督数据缺乏的问题，构造了包含真实/合成、静态/动态场景的大型数据集InsScene4D-147K，并采用自动化几何引导标注流程生成时间一致的实例掩码。
3. **前馈重建**：支持长序列的前馈式重建，在动态环境中保持几何-实例一致性。

### 主要贡献
1. 提出IGGT4D，一个流式实例-几何融合的Transformer，实现在线4D场景理解。
2. 构建大规模数据集InsScene4D-147K，涵盖多种场景类型及时间一致的实例标注。
3. 在3D重建、位姿估计、实例空间追踪和开放词汇分割任务中，IGGT4D优于现有流式基线方法，同时保持对长动态序列的可扩展在线推理能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对流式动态场景的4D理解与重建任务，在方法上融合了几何与实例学习，并提供了新的数据集，对从事3D/4D场景理解、空间智能的相关方向有参考价值。但摘要未透露关键设计细节（如Transformer结构、因果建模的具体机制），需进一步阅读正文评估创新深度。

</details>

<details>
<summary>Abstract</summary>

Real-world spatial intelligence requires agents to understand scenes from continuous video streams, where objects move, persist, disappear, and reappear over time. While recent spatial foundation models have enabled generalizable feed-forward 3D reconstruction, most streaming methods remain geometry-centric and lack temporally consistent object-level understanding. Meanwhile, existing semantic reconstruction and 3D-aware vision-language methods largely rely on externally extracted 2D semantic cues or loosely coupled geometry inputs, limiting unified geometry-instance learning in long dynamic scenes. In this paper, we propose IGGT4D, a streaming instance-grounded geometry Transformer for online 4D scene understanding. IGGT4D processes video frames sequentially, reuses historical context through causal spatial-temporal modeling, and incrementally updates a unified representation of camera motion, geometry, and object identity. This enables long-sequence feed-forward reconstruction with geometry-instance consistency in dynamic environments. To address the lack of high-quality 4D supervision, we further construct InsScene4D-147K, a large-scale dataset spanning real/synthetic and static/dynamic scenes, with RGB images, depth, poses, and temporally consistent instance masks generated by an automated geometry-guided annotation pipeline. Experiments on 3D reconstruction, pose estimation, instance spatial tracking, and open-vocabulary segmentation demonstrate that IGGT4D outperforms existing streaming baselines while maintaining scalable online inference for long dynamic sequences.

</details>

#### 2026-07-20 - Fine-Detail Monocular Geometry Estimation with Self-Guided Sparse Volumetric Refinement

**Authors:** Lingyu Kong, Ruicheng Li, Ruicheng Wang, Sicheng Xu, Chengtang Yao, Jianfeng Xiang, Jiaolong Yang
**Links:** [abs](https://arxiv.org/abs/2607.17967) - [pdf](https://arxiv.org/pdf/2607.17967)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** point map, monocular geometry

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fine-Detail Monocular Geometry Estimation with Self-Guided Sparse Volumetric Refinement
- 作者：Lingyu Kong, Ruicheng Li, Ruicheng Wang, Sicheng Xu, Chengtang Yao, Jianfeng Xiang, Jiaolong Yang
- 出版日期：2026-07-20
- 分类：Geometry Foundation Models
- 链接：摘要URL: https://arxiv.org/abs/2607.17967 ; PDF: https://arxiv.org/pdf/2607.17967

### 一句话总结
本文提出一种自引导稀疏体素精化（SSR）方法，通过将单目几何估计从2D图像空间提升到3D空间，显著提升细粒度几何（如薄结构和小物体）的重建保真度。

### 研究问题
现有单目几何估计模型在局部3D结构（尤其是细粒度细节，如薄结构和小物体）上存在显著畸变，原因在于大多数模型在2D参数化下解码3D几何，特征交互受图像平面邻近性而非真实3D空间关系主导，导致来自几何上距离较远表面的特征混合，产生过度平滑的几何。

### 核心思路/方法
1. 从基础模型中提取粗尺度的度量点云图。
2. 将该粗点云图提升到稀疏体素壳（sparse voxel shell）上。
3. 通过自引导稀疏体素精化（SSR）模块进行精化。该模块采用基于3D空间局部性的稀疏卷积聚合特征，避免深度不连续处的特征混合，从而生成高保真的度量尺度点图。

### 主要贡献
1. 明确了现有单目几何估计模型在细粒度结构上性能受限的关键原因：2D参数化导致的特征混合问题。
2. 提出了SSR方法，将单目几何建模从2D图像空间提升到3D空间，通过稀疏体素精化实现高保真度量点图。
3. 在多个数据集上的实验表明，该方法在定量指标和定性可视化上均显著优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
- 优先级：高
- 理由：该方法针对单目几何估计中长期存在的细粒度细节畸变问题，提出了新颖的3D稀疏体素精化范式，且实验证明了显著改进。对于从事3D视觉、几何重建、单目深度估计等方向的研究者具有重要参考价值。方法思路清晰，问题定义明确，具备较高实用与学术价值。

</details>

<details>
<summary>Abstract</summary>

Monocular geometry estimation has recently achieved impressive performance across diverse scenes. However, state-of-the-art models still face notable distortion in local 3D structure, especially in fine details, like thin structures and small objects. We attribute this limitation to an architectural mismatch: most current models decode 3D geometry within a 2D parameterization, where feature interactions are governed by image-plane proximity rather than true 3D spatial relationships. This inadvertently mixes features from geometrically distant surfaces, resulting in over-smoothed geometry particularly around thin or elongated structure. In this paper, we propose a fine-detail monocular geometry estimation with Self-Guided Sparse 3D Refinement (SSR) that lifts monocular geometry modeling from 2D image space to 3D space for high-fidelity metric-scale point maps. Our model lifts the coarse point map from a foundation base model onto a sparse voxel shell and refines it via SSR. The SSR employs sparse convolutions that aggregate features based on 3D spatial locality, avoiding feature mixing across depth discontinuities. Extensive experiments on diverse datasets demonstrate that our method significantly outperforms existing approaches in recovering fine detailed 3D geometry across both quantitative metrics and qualitative visualizations.

</details>

#### 2026-07-20 - MuViSeg: Multi-View Segment Correspondences from Dense Geometry Priors

**Authors:** Denis Fatykhoph, Timur Akhtyamov, Konstantin Pakulev, German Devchich, Gonzalo Ferrer
**Links:** [abs](https://arxiv.org/abs/2607.17938) - [pdf](https://arxiv.org/pdf/2607.17938)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, MASt3R, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MuViSeg: Multi-View Segment Correspondences from Dense Geometry Priors
- 作者：Denis Fatykhoph, Timur Akhtyamov, Konstantin Pakulev, German Devchich, Gonzalo Ferrer
- 出版日期：2026-07-20
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.17938

### 一句话总结
本文提出MuViSeg方法，通过三种匹配头（LightGlue风格、DPT风格和多视图联合自注意力）在实例分割层面建立多视图对应关系，并在零样本评估中提升了拓扑导航性能。

### 研究问题
如何从密集几何先验出发，建立多视角图像之间的实例分割级别对应关系，以弥补传统像素/关键点匹配与物体级消费系统（如物体级建图、拓扑导航）之间的鸿沟。

### 核心思路/方法
1. **基础框架**：采用类无关分割器每张图生成实例分割，然后从大型3D基础模型（MASt3R、VGGT）中池化特征作为分段描述符。
2. **三个学习的匹配头**：
   - **LightGlue风格注意力头**：基于冻结的MASt3R描述符，采用DoubleSoftmax评分进行段级匹配。
   - **DPT风格多尺度融合模块**：在VGGT基础模型中池化前，暴露层次化空间细节。
   - **多视图扩展头（主要贡献）**：同时对多个视图中的段进行联合自注意力，恢复严格成对匹配器无法获得的传递性对应关系。

### 主要贡献
1. 提出了一个多视图实例段对应框架，包含两个新的单视图匹配头和一个多视图扩展头。
2. 在Replica和Virtual KITTI 2的零样本协议下，LightGlue风格头相比无参数Sinkhorn匹配器，AUPRC分别提升+4.85和+25.9。
3. 将多视图变体集成到RoboHop拓扑导航流水线（Habitat-Matterport 3D基准）中，无需重新训练即实现成功率从50%提升至70%，LightGlue风格头使SPL从45.7提升至59.1。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文提出了一种新颖的多视图实例段对应方法，并通过零样本评估在经典导航基准上取得了显著提升，对物体级对应和拓扑导航领域有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Classical image correspondence is solved at the level of sparse keypoints or dense pixels, but the systems that consume these matches - object-level mapping, topological navigation, scene-graph maintenance - reason about whole objects. Recent work narrows this gap by matchng directly at the level of instance segments: a class-agnostic segmenter partitions each image, and per-segment descriptors are obtained by pooling features from large 3D foundation models over the masks. We build on this segment-level matching paradigm and propose three learned matching heads: a LightGlue-style attention head with DoubleSoftmax scoring on frozen MASt3R descriptors; a DPT-style multi-scale fusion module that exposes layered spatial detail from the VGGT foundation model before pooling; and - as our main contribution - a multi-view extension that performs joint self-attention over segments drawn from several views at once, recovering transitive correspondences that strictly pairwise matchers cannot reach. Under a stratified zero-shot protocol on Replica and Virtual KITTI 2 with controlled viewpoint baselines from 0 deg to 180 deg, the LightGlue-style head improves over a parameter-free Sinkhorn matcher on the same MASt3R backbone by +4.85 AUPRC on Replica and +25.9 AUPRC on Virtual KITTI 2. Dropped into the RoboHop topological navigation pipeline on the Habitat-Matterport 3D (HM3D) Instance Image Navigation benchmark without retraining, our multi-view variant raises success rate from 50% to 70%, and our LightGlue-style head raises SPL from 45.7 to 59.1.

</details>

#### 2026-07-19 - VIDAR: Visual-Inertial Dense Alignment and Reconstruction via a Geometric Foundation Model

**Authors:** Diyari Mohammed Salih, Lingxiang Hu, Naima AitOufroukh-Mammar, Fabien Bonardi
**Links:** [abs](https://arxiv.org/abs/2607.17171) - [pdf](https://arxiv.org/pdf/2607.17171)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** geometric foundation model, dense reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VIDAR: Visual-Inertial Dense Alignment and Reconstruction via a Geometric Foundation Model
- 作者：Diyari Mohammed Salih, Lingxiang Hu, Naima AitOufroukh-Mammar, Fabien Bonardi
- 出版日期：2026-07-19
- 分类：Geometry Foundation Models
- 链接：[Abstract](https://arxiv.org/abs/2607.17171) | [PDF](https://arxiv.org/pdf/2607.17171)

### 一句话总结
VIDAR 是一种视觉惯性密集重建框架，通过将视觉惯性里程计（SVO+IMU）与基础模型 Depth Anything 3 耦合，利用度量锚点（metric anchor）对齐单目基础模型的稠密几何预测，实现稳定尺度的稠密重建。

### 研究问题
如何解决单目基础模型（如 Depth Anything 3）在稠密几何预测中缺乏稳定度量尺度（metric scale）的问题，从而实现实用的度量稠密单目重建。

### 核心思路/方法
- 使用视觉惯性前端（SVO+IMU）作为度量锚点，提供相机位姿、尺度以及一致的世界坐标系，用于对齐跨时间的基础模型稠密预测。
- 基础模型贡献局部精细几何细节，并通过融合策略整合到全局重建中。
- 研究了两种对齐策略：1）位姿条件化的深度预测（pose-conditioned DA3）；2）解耦对齐策略（decoupled alignment）。

### 主要贡献
- 提出 VIDAR 框架，将视觉惯性度量约束与基础模型稠密几何能力结合，实现了鲁棒的度量稠密重建。
- 展示两种对齐策略效果：在 EuRoC 数据集上，位姿注入使尺度误差降至约 1%，F@0.10 均值达 0.463；解耦混合策略在无真值位姿时提升至 0.676。
- 在 EuRoC 和 TUM RGB-D 数据集上的实验表明，该方法为度量稠密单目重建提供了实用方案。

### 局限性
摘要未提供足够信息。未说明失败案例、计算开销、对光照或纹理的敏感性，也未提及与其他方法的全面对比。

### 阅读优先级
**中**  
理由：提出了一种将传统视觉惯性里程计与新兴几何基础模型结合的实用框架，对于从事单目深度估计或 SLAM 的研究者有一定参考价值。但方法明确依赖 Depth Anything 3 和特定惯性前端，通用性待评估；且摘要未提供完整消融实验和局限性，创新性主要体现为架构组合而非全新理论。

</details>

<details>
<summary>Abstract</summary>

Monocular foundation models provide dense geometry but usually lack a stable metric scale. This paper presents VIDAR, a visual-inertial dense reconstruction framework that couples SVO+IMU odometry with Depth Anything 3. VIDAR uses the visual-inertial front end as a metric anchor: it provides camera poses, scale, and a consistent world frame for aligning dense foundation-model predictions across time. The foundation model then contributes detailed local geometry that is fused into a global reconstruction. We study both pose-conditioned DA3 and a decoupled alignment strategy. On EuRoC, pose injection reduces scale error to about 1\% and reaches 0.463 mean F@0.10; the decoupled hybrid improves this to 0.676 without ground-truth poses. Results on EuRoC and TUM RGB-D show that VIDAR is a practical route to metric dense monocular reconstruction.

</details>

#### 2026-07-19 - DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation

**Authors:** Yuxuan Chen, Brook Du
**Links:** [abs](https://arxiv.org/abs/2607.17058) - [pdf](https://arxiv.org/pdf/2607.17058)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, SLAM, visual SLAM, depth estimation, robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation
- 作者：Yuxuan Chen, Brook Du
- 出版日期：2026-07-19
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要：https://arxiv.org/abs/2607.17058 ；PDF：https://arxiv.org/pdf/2607.17058

### 一句话总结
提出一种名为 Metric-DROID 的端到端递归架构，通过集成本体感受里程计作为几何锚点，解决单目视觉SLAM系统的尺度模糊和漂移问题，实现精确的公尺度深度估计。

### 研究问题
摘要未提供足够信息，但根据背景描述，研究问题为：单目系统固有的尺度模糊与尺度漂移问题，如何使基于递归光流的SLAM系统恢复公尺度度量，以实现自主机器人导航所需的高精度深度估计。

### 核心思路/方法
1. 设计一个**LSTM更新算子**，将高频里程计序列编码为空间特征图，为迭代优化提供持续的度量偏置。
2. 提出**不确定性感知度量后端（$BA_{odom}$）**：将里程计视为几何锚点，并学习其异方差协方差；通过回归时变度量不确定性$\Sigma_{o}$，智能平衡视觉重投影误差与度量平移残差，从而减轻轮滑与传感器噪声的影响。
3. 采用**选择性残差微调策略**，在保护预训练几何先验的同时，实现零样本的度量对齐。

### 主要贡献
1. 提出一种端到端递归架构Metric-DROID，集成里程计锚定视觉SLAM到物理现实。
2. 引入LSTM更新算子编码高频里程计序列。
3. 设计不确定性感知度量后端（$BA_{odom}$）并学习时变度量不确定性。
4. 提出选择性残差微调策略，保留预训练先验的同时实现零样本度量对齐。

### 局限性
摘要未提供足够信息。根据摘要，方法涉及轮滑和传感器噪声的缓解，但未明确讨论系统的实时性、实际部署局限、对特定里程计类型的依赖程度、或失败边界条件。

### 阅读优先级
**高**  
理由：该工作直接面向视觉SLAM中的关键尺度问题，提出结合里程计与不确定性的创新框架，结构设计清晰（LSTM编码、度量后端、残差微调），且包含零样本对齐能力，对自主机器人导航领域的研究者和工程师具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture that anchors visual SLAM to physical reality by integrating proprioceptive odometry. Our framework introduces the following innovations: (1) A LSTM Update Operator that encodes high-frequency odometry sequences into spatial feature maps, providing a persistent metric bias for iterative refinement. (2) An Uncertainty-Aware Metric Backend ($BA_{odom}$) that treats odometry as a geometric anchor with learned heteroscedastic covariance. By regressing a time-varying metric uncertainty $Σ_{o}$, our system intelligently balances visual re-projection and metric translation residuals, effectively mitigating the impact of wheel-slip and sensor noise. (3) We further propose a selective residual fine-tuning strategy to preserve pre-trained geometric priors while enabling zero-shot metric alignment.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

#### 2026-07-23 - GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis

**Authors:** Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian
**Links:** [abs](https://arxiv.org/abs/2607.21448) - [pdf](https://arxiv.org/pdf/2607.21448)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis
- 作者：Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian
- 出版日期：2026-07-23
- 分类：Dynamic / 4D Reconstruction; Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2607.21448; PDF: https://arxiv.org/pdf/2607.21448

### 一句话总结
GrainGS 提出了一种结合层级锚定结构与每高斯形变的动态框架，通过梯度解耦、静态预热和规范残差外观分解，实现了动态场景的高质量、实时与紧凑的渲染。

### 研究问题
如何平衡动态场景重建中对细微运动建模、结构稳定性和紧凑表示的需求，避免现有方法（如每基元方法导致冗余增长、锚定方法抑制局部运动）的不足。

### 核心思路/方法
1. **层级锚定+每高斯形变**：结合层级锚定支架（anchor scaffold）与每个高斯独立的形变能力，实现结构约束下的局部运动建模。
2. **静态预热阶段**：在所有时间戳观测数据上建立一个时间不变的规范表示。
3. **梯度解耦操作**：在联合训练中，使用 stop-gradient 操作阻断通过形变传递到规范位置的梯度路径，同时保留通过重建目标对规范位置的直接优化。
4. **规范-残差外观分解**：将帧依赖的光度变化建模为规范残差，而非强制纳入几何形变。

### 主要贡献
1. 提出了 GrainGS 框架，实现了高重建质量、实时新视角合成和紧凑存储。
2. 在合成单目和真实多视图基准上，达到平均峰值信噪比36.98分贝、渲染速度435.6帧每秒、存储需求4.67兆字节。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对动态场景重建中的关键权衡问题（运动建模、稳定性、紧凑性）提出了创新性框架，且实验指标突出（36.98 dB PSNR、435.6 FPS、4.67 MB存储），在动态/4D重建和神经渲染领域具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic scene reconstruction with 3D Gaussian Splatting requires a balance between fine-grained motion modeling, structural stability, and compact representation. Existing per-primitive methods provide flexible local deformation but often suffer from redundant primitive growth, while anchor-based methods improve spatial regularity at the cost of suppressing locally varying motion. To address these issues, we present GrainGS, a dynamic Gaussian framework that combines a hierarchical anchor scaffold with per-Gaussian deformation. A static warm-up stage first establishes a time-invariant canonical representation from observations across all timestamps. During joint training, a stop-gradient operation blocks the deformation-mediated gradient pathway to the canonical positions while preserving their direct refinement through the reconstruction objective. Each Gaussian then predicts independent temporal offsets for position, rotation, and scale, enabling detailed local motion within a structurally constrained scaffold. A canonical-residual appearance decomposition further models frame-dependent photometric changes without forcing them into geometric deformation. Experiments on synthetic monocular and real-world multiview benchmarks show that GrainGS achieves high reconstruction quality, real-time novel view synthesis, and compact storage. Under the synthetic benchmark setting, it reaches an average peak signal-to-noise ratio of 36.98 decibels, renders at 435.6 frames per second, and requires 4.67 megabytes of storage.

</details>

#### 2026-07-23 - FA-LAM: Focus-Aware Large Avatar Model for One-Shot 4D Animatable Gaussian Head

**Authors:** Yingdong Hu, Yisheng He, Yiming Jiang, Zehong Lin, Steven Hoi, Jun Zhang
**Links:** [abs](https://arxiv.org/abs/2607.20922) - [pdf](https://arxiv.org/pdf/2607.20922)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, dynamic 4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FA-LAM: Focus-Aware Large Avatar Model for One-Shot 4D Animatable Gaussian Head
- 作者：Yingdong Hu, Yisheng He, Yiming Jiang, Zehong Lin, Steven Hoi, Jun Zhang
- 出版日期：2026-07-23
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2607.20922

### 一句话总结
FA-LAM 是一个用于单次生成可动画化高斯头部模型的焦点感知大模型，通过分析注意力机制与训练任务冲突，改进了3D/4D头部重建质量。

### 研究问题
如何解决现有方法在单次可动画化高斯头部生成中存在的两个问题：(1) 注意力激活不正确且带有噪声；(2) 重建任务与动画任务之间的目标冲突。

### 核心思路/方法
1. **对称语义注意力正则化**：利用人头的语义和结构对称性，对注意力激活进行正则化。
2. **双阶段训练流水线**：将大视角幻觉能力与动画能力解耦至不同模块，分别优化。
3. **核心自回归修改与可见性感知令牌融合**：支持多视角和流式4D重建，提高效率与内存友好性。

### 主要贡献
- 指出了现有方法在3D全头生成质量低下的两个根本原因（注意力问题与任务冲突）。
- 提出了对称语义注意力正则化策略，改善注意力激活质量。
- 设计了双阶段训练流水线，消除重建与动画任务间的冲突。
- 增强了模型对多视角和流式4D重建的支持，并保持内存高效。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对可动画化高斯头部生成中的核心瓶颈（注意力噪声与任务冲突）提出了系统性解决方案，并支持4D流式重建，对动态3D人脸/头部建模领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We propose FA-LAM, a Focus-Aware Large Avatar Model for one-shot animatable Gaussian head creation, while simultaneously enabling static 3D and dynamic 4D full-head recovery. The core of our method lies in a thorough analysis of the attention mechanisms and the entangled reconstruction and animation training pipeline adopted by prior state-of-the-art approaches. Our analysis identifies two main factors that compromise the quality of 3D full-head generation: (1) incorrect and noisy attention activations, and (2) conflicts between the tasks of reconstruction and animation. To address the first issue, we introduce a symmetric and semantic attention regularization strategy that leverages the inherent semantics and structural symmetry of human heads. To disentangle the objectives of reconstruction and animation, we develop a novel dual-phase training pipeline that separates the model's capabilities for large-view hallucination and animation into distinct modules. Moreover, we enhance our model to support multi-view and streaming 4D reconstruction in an efficient and memory-friendly manner through a core autoregressive modification with tailored visibility-aware token fusion. Collectively, these innovations enable FA-LAM to reconstruct animatable Gaussian full heads with superior quality, particularly in fine facial regions and large viewing angles.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-23 - Boosting Robustness for All-Weather Self-Supervised Depth Estimation in Autonomous Driving

**Authors:** Mengshi Qi, Xiaoyang Bi, Xianlin Zhang, Huadong Ma
**Links:** [abs](https://arxiv.org/abs/2607.21526) - [pdf](https://arxiv.org/pdf/2607.21526)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Boosting Robustness for All-Weather Self-Supervised Depth Estimation in Autonomous Driving
- 作者：Mengshi Qi, Xiaoyang Bi, Xianlin Zhang, Huadong Ma
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2607.21526 | PDF https://arxiv.org/pdf/2607.21526

### 一句话总结
本文提出一种自训练框架，通过多教师蒸馏和鲁棒的雷达融合方法，提升自动驾驶在恶劣天气下自监督深度估计的鲁棒性，并在全天候数据集上达到最优性能。

### 研究问题
恶劣天气条件下（如雨、雾等）自监督深度估计的鲁棒性问题。具体包括两个子问题：
1. 恶劣天气会扭曲像素对应关系，违反自监督损失函数假设，导致深度预测错误；
2. 雷达传感器虽常见于恶劣天气，但其点云在相机视角（POV）中分布稀疏，使得自监督融合困难。

### 核心思路/方法
1. **不确定性感知的多教师蒸馏（Uncertainty-Aware Multi-Teacher Distillation）**：使用不同恶劣天气条件输入生成多个教师模型，再通过不确定性建模对知识蒸馏损失进行加权。
2. **POV-BEV雷达融合（POV-BEV Radar Fusion）**：利用相机像素射线约束，建立POV（相机视角）与雷达BEV（鸟瞰视角）之间的联系，从而利用更稠密的雷达点，同时捕捉两种视角的互补信息。

### 主要贡献
- 提出了针对全天候自监督深度估计的鲁棒自训练框架，结合多教师蒸馏与雷达融合。
- 设计了POV-BEV雷达融合方法，有效利用稠密雷达点以增强恶劣天气下的深度预测。
- 在全天候数据集上的定性和定量实验均展示了鲁棒性，实现了当时最优性能。

### 局限性
摘要未提供足够信息。未提及方法在特定天气条件下的失败案例、计算开销或对传感器硬件的要求。

### 阅读优先级
**高**
理由：该工作直接针对自动驾驶在恶劣天气下的关键安全挑战，提出了融合多教师蒸馏与雷达的创新方案，并达到SOTA性能，对相关领域研究者和工程师具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Self-supervised depth estimation is challenging for safe autonomous driving under various adverse weather conditions due to sensor perception degradation. These challenges arise from two main aspects. Firstly, adverse conditions can distort pixel correspondences and violate the assumptions embedded in the self-supervised loss function, leading to erroneous depth predictions. Secondly, while radar is a widely adopted sensor in adverse weather conditions, the sparse distribution of radar points in the Point of View (POV) poses challenges for self-supervised fusion. To address these issues, we introduce a novel self-training pipeline using unpaired real all-weather data through multi-teacher distillation and robust radar fusion. We propose the Uncertainty-Aware Multi-Teacher Distillation method to generate diverse teacher models with different adverse condition inputs, and then employ uncertainty modeling to weigh the knowledge distillation loss. Additionally, we design the POV-BEV Radar Fusion approach, which leverages camera-pixel ray constraints to establish connections between the camera's Point of View (POV) and the radar's Bird's-Eye View (BEV). This approach enables the utilization of denser radar points, effectively capturing the complementary perspectives of both POV and BEV. Extensive quantitative and qualitative experiments demonstrate the robustness of our proposed method on all-weather datasets, achieving state-of-the-art performance. Our code and models are available at https://github.com/MICLAB-BUPT/RobustDepth.

</details>

#### 2026-07-23 - Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window

**Authors:** Yukun Shi, Minglun Gong
**Links:** [abs](https://arxiv.org/abs/2607.21471) - [pdf](https://arxiv.org/pdf/2607.21471)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, scene reconstruction, surface reconstruction, 3DGS, novel view synthesis, view synthesis, rendering, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Future Rendering ≠ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window
- 作者：Yukun Shi, Minglun Gong
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.21471

### 一句话总结
本文提出了一个名为FutureSurf的基准测试和数据集，用于评估动态场景中超出观测时间窗口的几何表面重建（未来表面）的准确性。

### 研究问题
当前动态场景重建方法几乎只在观测时间窗口内评估，但实际应用（如AR覆盖、机器人交互）需要预测未来时刻的表面几何形状。问题在于：**没有标准基准来衡量未来表面重建的准确性**。

### 核心思路/方法
1.  **基准定义**：要求方法训练于序列的前75%观测数据，然后在保留的未来数据上评估每帧的表面几何（使用Chamfer距离）。主要分数为绝对未来CD，诊断指标为未来/观测误差差距。
2.  **数据集**：包含8个解析定义的受控运动，其中3个为证伪控制（用于检验方法是否正确忽略不影响表面的变化）。提供每帧精确的ground truth网格。
3.  **基线实验**：在受控运动上测试了DG-Mesh和Deformable-3DGS两个骨干方法，发现未来表面误差显著（2.0-6.6×差距），且未来渲染质量与未来表面准确性统计上解耦。

### 主要贡献
1.  **提出FutureSurf基准与数据集**：首个专门用于评估动态场景未来时间点表面重建的受控诊断基准，包含精确地面真值和证伪控制。
2.  **揭示现有方法局限**：即使对于原则可预测的未来运动，现有方法（DG-Mesh, Deformable-3DGS）仍存在显著未来表面误差（2.0-6.6×），且渲染质量指标无法反映几何误差。
3.  **提供工具与资源**：公开了分割文件、评分代码、基准卡片、Croissant元数据及数据集，便于社区复现和比较。
4.  **建立未来表面与渲染的差异**：通过统计证明新视角合成指标与未来几何准确性无关，未来误差主要集中于表面移动区域。

### 局限性
摘要未提供关于局限性的信息，例如数据集只有8个受控运动（场景多样性有限）以及基线方法类型有限（仅使用DG-Mesh和Deformable-3DGS）等限制。

### 阅读优先级
**高**
- **理由**：该工作填补了动态重建领域的一个明确空白——缺乏未来表面预测的标准评估，提出的基准和数据集具有开创性。实验揭示了现有方法（包括流行的DG-Mesh和Deformable-3DGS）在预测未来几何时的系统性不足，并指出渲染质量无法替代几何准确性，这对从事动态场景重建、AR/VR和机器人交互的研究者具有重要警示和参考价值。资源已公开，便于直接复现和使用。

</details>

<details>
<summary>Abstract</summary>

Dynamic-scene reconstruction is almost always evaluated inside the observed time window, yet deployment settings such as AR overlays, robot interaction, and anticipatory planning need the future surface: the geometry at times beyond those captured. No standard benchmark measures this. We introduce FutureSurf, a controlled diagnostic benchmark and dataset for future-time surface reconstruction that trades scene diversity for exact future ground truth and falsification controls. A method trains on the observed first 75% of a sequence; we score its extracted per-frame surface on the held-out future by Chamfer distance, reporting absolute future CD as the primary score and the future/observed gap as a diagnostic. The dataset contains eight analytically defined controlled motions, including three falsification controls, with exact per-frame ground-truth meshes. We also provide a ground-truth-side recoverability oracle. The release includes split files, scoring code, a benchmark card, and Croissant metadata. On the controlled motions, the DG-Mesh backbone leaves a 2.7-4.1$\times$ gap even for futures predictable in principle (four of five recoverable from observed motion by a fixed rule), while the falsification controls behave as designed (the surface-invariant motion shows no gap). Beyond the contributed dataset, the gap persists across six animated DG-Mesh asset scenes and a second backbone, Deformable-3DGS (2.0-6.6$\times$; both share a deformation-MLP temporal model). The benchmark also shows that future rendering quality and future-surface accuracy are statistically decoupled, so the novel-view-synthesis metrics the field reports do not track future geometry. The future error is structured, concentrating where the surface moves. The dataset, evaluation toolkit, and scoring code are available on Hugging Face and GitHub (https://github.com/Ricky-S/futuresurf).

</details>

#### 2026-07-23 - DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV

**Authors:** Tong Ling, Wenhui Diao, Yingchao Feng, Hanbo Bi, Zhongyan Hou, Xian Sun
**Links:** [abs](https://arxiv.org/abs/2607.21438) - [pdf](https://arxiv.org/pdf/2607.21438)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, camera pose estimation, pose estimation, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV
- 作者：Tong Ling, Wenhui Diao, Yingchao Feng, Hanbo Bi, Zhongyan Hou, Xian Sun
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：arXiv:2607.21438

### 一句话总结
该论文提出了DAPM，一种针对无人机航拍图像的单目深度估计框架，能够在高度、俯仰角、翻滚角与视场角持续变化下联合估计相机姿态与深度，并达到最优性能。

### 研究问题
无人机在动态变化的高度、俯仰角、翻滚角和视场角下进行单目深度估计时，现有方法难以泛化到这些多样视角以及航拍场景中深度分布的大尺度范围。

### 核心思路/方法
1. 通过理论分析建立无人机视角与视距的几何对应关系，并以此为观测基准。
2. 提出理想地面深度（IGD）模块，利用推导出的几何关系实现密集相机姿态监督并增强深度特征。
3. 设计粗到细的渐进量化箱（PQB）模块，通过渐进监督与层次量化箱实现复杂航拍图像中的鲁棒估计。
4. 构建UAPD数据集，涵盖全面且连续的姿态参数分布，用于评估框架。

### 主要贡献
- 第一个针对无人机航拍图像、在连续变化视角下联合估计相机姿态与深度的单目框架（DAPM）。
- 提出IGD模块，利用几何关系实现密集相机姿态监督与深度特征增强。
- 提出PQB模块，通过渐进式监督与层次量化箱提升复杂航拍场景的估计鲁棒性。
- 创建UAPD数据集，包含连续分布的姿态参数，并在该数据集上达到深度与相机姿态估计指标的最优性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：本文针对无人机实际部署中高度动态视角下的核心难题提出了首个专用框架，理论分析严谨，方法设计（IGD与PQB）具有明确创新性，并开源代码与数据集，对3D重建、自主导航等领域有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation is a fundamental prerequisite for 3D reconstruction and autonomous navigation in Unmanned Aerial Vehicles (UAVs). In practical deployments, UAVs operate under highly dynamic camera poses characterized by continuous variations in height, pitch, roll, and field of view (FOV). Existing monocular depth estimation methods frequently fail to generalize across such diverse perspectives and the expansive scale of depth distributions inherent in aerial scenes. To address these challenges, we establish a quantitative representation of UAV viewing angles through rigorous theoretical analysis, deriving the geometric correspondence between viewing angles and view distances using the ground plane as a reference for observation. Building upon this, we propose Depth Estimation for Any Perspectives Model (DAPM), representing the first monocular framework specifically designed for UAV aerial imagery to jointly estimate camera pose and depth under continuously varying viewpoints. Specifically, we introduce an Ideal Ground Depth (IGD) module that leverages the derived geometric relationships between UAV perspectives and view distances to implement dense camera-pose supervision and enhance depth features. And we further develop a coarse-to-fine Progressive Quantization Bins (PQB) module. By incorporating progressive supervision and hierarchical quantization bins, the PQB module enables robust estimation in complex UAV aerial imagery. To evaluate the proposed framework, we present the UAV Any Perspectives Depth (UAPD) dataset, featuring comprehensive and continuous distributions of pose parameters. Experimental results on UAPD demonstrate that DAPM achieves state-of-the-art performance across both depth and camera-pose estimation metrics. The source code and datasets are available at: https://github.com/ThisIsLT/DAPM.

</details>

#### 2026-07-23 - GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition

**Authors:** Panagiotis Mermigkas, Argyris Manetas, Petros Maragos
**Links:** [abs](https://arxiv.org/abs/2607.21416) - [pdf](https://arxiv.org/pdf/2607.21416)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition
- 作者：Panagiotis Mermigkas, Argyris Manetas, Petros Maragos
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要 https://arxiv.org/abs/2607.21416；PDF https://arxiv.org/pdf/2607.21416

### 一句话总结
GLAM-SLAM 提出一种实时、解耦的高斯泼溅SLAM系统，通过流致密化锚定策略和场景空间分解，实现大规模室外场景的长序列建图与定位。

### 研究问题
现有基于高斯泼溅的单目SLAM系统在处理长序列、大规模室外场景时，存在实时性差、GPU内存需求过高的问题，限制了其在真实长时任务中的应用。

### 核心思路/方法
1. **轻量追踪**：采用基于特征鲁棒的SLAM前端进行轻量化位姿估计。
2. **稀疏锚点网格表示**：采用结构化的稀疏锚点网格进行建图，保证大规模操作的可扩展性和场景一致性。
3. **几何流致密化锚定策略**：基于对极几何约束，通过流致密化满足3D高斯泼溅（3DGS）的密集初始化需求。
4. **场景分割策略**：将建图视为多场景问题，通过MLP初始化引入强空间归纳偏置，生成局部化高斯体。

### 主要贡献
- 提出首个实时、解耦的高斯泼溅SLAM系统，专为大规模室外长序列场景设计。
- 引入几何流致密化锚定策略，解决3DGS密集初始化的需求。
- 提出基于场景分割的空间分解方法，借助MLP初始化实现局部高斯化。
- 在KITTI Odometry、Oxford RobotCar和Málaga数据集上，重建质量相比次优方法提升15%，同时保持实时性和长序列扩展能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：论文针对高斯泼溅SLAM在真实长序列大规模场景中的实际瓶颈（实时性、内存、扩展性）提出系统级解决方案，方法新颖（流致密化、场景分解），并在多个挑战性基准上取得显著提升。对该领域（3D重建、SLAM、机器人、AR）的研究者和工程师具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing Gaussian-splatting-based monocular Simultaneous Localization and Mapping (SLAM) systems are either tailored to short sequences, are not real-time, or suffer from prohibitive GPU memory requirements, limiting their applicability in realistic, long-horizon scenarios. To address this, we present GLAM-SLAM, a real-time, decoupled Gaussian-splatting SLAM system designed for large-scale outdoor scenes. We ensure lightweight tracking using a robust, feature-based SLAM frontend, while for mapping, we adopt a structured, sparse anchor grid representation that ensures scalable operation and maintains scene coherence across long-term sequences. To satisfy the dense initialization requirements of 3D Gaussian Splatting (3DGS), we introduce a geometry-based flow-densification anchoring strategy using epipolar constraints. Furthermore, by treating mapping as a multi-scene problem, we propose a scene-partitioning strategy that introduces a strong spatial inductive bias via MLP initializations to generate localized Gaussians. We evaluate our system on the challenging, long-sequence KITTI Odometry, Oxford RobotCar, and M'alaga datasets. Extensive ablations and comparisons demonstrate a 15% improvement in reconstruction quality over the second-best performer, while maintaining real-time performance and the ability to scale to longer sequences. Code is publicly available for the benefit of the community.

</details>

#### 2026-07-23 - Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar

**Authors:** Simone Arreghini, Mirko Nava, Nicholas Carlotti, Antonio Paolillo, Alessandro Giusti
**Links:** [abs](https://arxiv.org/abs/2607.21309) - [pdf](https://arxiv.org/pdf/2607.21309)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar
- 作者：Simone Arreghini, Mirko Nava, Nicholas Carlotti, Antonio Paolillo, Alessandro Giusti
- 出版日期：2026-07-23
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.21309

### 一句话总结
本文提出一种基于时空分离卷积的轻量级网络，利用平面LiDAR序列实现服务机器人的全向人体检测与二维姿态估计，通过跨模态自监督训练减少人工标注需求。

### 研究问题
如何利用计算资源受限的服务机器人上常见的全向平面LiDAR传感器，实现高效、精确的人体检测、距离估计和朝向识别。

### 核心思路/方法
设计基于“时空块”的轻量级网络，将沿扫描射线的空间处理与跨扫描帧的时间聚合显式分离；训练阶段使用RGB-D人体追踪器在传感器重叠区域提供跨模态自监督信号，避免手动标注LiDAR数据。

### 主要贡献
1. 提出显式分离空间与时间处理的轻量级网络结构，适配平面LiDAR序列。
2. 采用跨模态自监督训练方法，消除对LiDAR人工标注的依赖。
3. 在定量实验中，相比参数匹配的基线模型，在距离误差（-38%）、位置误差（-28%）和朝向误差（-15%）上均有显著改善。
4. 在FROG公开数据集上验证性能，并在真实服务机器人上实现实时CPU推理和现场演示。

### 局限性
摘要未提供足够信息。例如未讨论在极端光照、动态遮挡或复杂多人场景下的性能退化情况，也未说明跨模态自监督对RGB-D追踪器精度有多少依赖。

### 阅读优先级
**高**
理由：本文直接针对服务机器人最常见的低算力平面LiDAR场景，提出兼具轻量级、低标注成本和高精度的解决方案，对社交机器人导航与人机交互具有直接应用价值。实验数据具体（误差降低百分比）且涵盖公开数据集与真实部署，适合相关领域研究者阅读。

</details>

<details>
<summary>Abstract</summary>

Localizing nearby humans and estimating their facing direction are key capabilities for safe navigation and socially aware human-robot interaction. Many pose-estimation pipelines target cameras and 3D LiDAR or assume GPU-class compute, whereas service robots are often equipped only with omnidirectional planar LiDARs and modest onboard processors. We address omnidirectional human detection and relative 2D pose estimation from planar LiDAR sequences with a lightweight network based on Space-Time Blocks, which explicitly separate spatial processing along scan rays from temporal aggregation across scans. Our network processes 360° LiDAR sequences to output per-ray human presence, distance, and relative orientation. We train it via cross-modal self-supervision from a narrow RGB-D body tracker in the sensors' overlap region, removing the need for manual LiDAR labels. Quantitative experiments show that our approach consistently outperforms a parameter-matched baseline model, reducing errors in distance (-38%), position (-28%), and orientation (-15%). We further benchmark on the public FROG dataset, report real-time CPU inference on a service robot, and validate with in-field demonstrations, supporting its suitability for spatial perception on computationally constrained service robots.

</details>

#### 2026-07-23 - TransBiolab: A Real-World Multi-View Dataset of Cluttered Transparent Biomedical Objects

**Authors:** Ke Ma, Yifei Wang, Meng Wang, Tian Xia
**Links:** [abs](https://arxiv.org/abs/2607.21071) - [pdf](https://arxiv.org/pdf/2607.21071)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, depth estimation, camera calibration, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TransBiolab: 杂乱透明生物医学物体的真实多视角数据集
- 作者：Ke Ma、Yifei Wang、Meng Wang、Tian Xia
- 出版日期：2026-07-23
- 分类：3D重建与多视角几何
- 链接：https://arxiv.org/abs/2607.21071

### 一句话总结
提出一个针对杂乱透明生物医学物体的真实世界RGB-D多视角数据集TransBiolab，包含大量标注帧和多种任务基准，旨在推动自动化实验室操作中的视觉感知研究。

### 研究问题
现有透明物体数据集通常不评估真实实验室操作场景中的多物体杂乱、遮挡和标定多视角捕获的组合设置，导致该领域缺乏高质量的真实世界数据。

### 核心思路/方法
1. 构建真实世界RGB-D数据集，包含98个场景共161,315帧，覆盖15种实验室物体类型，提供1.03M实例标注。
2. 数据集沿三个难度轴组织：物体类别、帧中物体总数、相机视角。
3. 定义以数据集为中心的基准任务：分割、深度估计与补全、6D姿态估计。
4. 通过释放的标注和标定执行系统级机器人操作评估。

### 主要贡献
1. 提供首个面向杂乱透明生物医学物体的标定多视角真实世界数据集。
2. 数据集包含6D姿态、全掩码与可见掩码、深度和逐帧相机标定等丰富标注。
3. 定义了多种视觉任务的基准并报告了机器人操作评估结果。
4. 聚焦重复透明实例、杂乱场景和实验室多视角捕获，补充现有数据集的空白。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该数据集针对透明生物医学物体这一特殊场景，填补了现有数据集的空白，同时涵盖多视角、杂乱、遮挡等实际挑战，对自动化实验室视觉感知领域有直接推动作用；且提供了多种基准任务和机器人操作评估，具有较高实用价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous biomedical laboratories increasingly rely on visual perception to recognize, localize, and manipulate transparent plasticware, yet high-quality real-world datasets for this setting remain limited. The scarcity of domain-relevant data is particularly restrictive in cluttered multi-object scenes, where mutual occlusion and view-dependent appearance changes remain challenging even for contemporary visual foundation models. Existing transparent-object datasets have advanced segmentation, depth, and pose estimation, but they usually do not evaluate the combined setting of multi-object clutter, occlusion, and calibrated multi-view capture that characterizes real laboratory manipulation scenes. To address this gap, we present TrainsBiolab, a real-world RGB-D dataset of cluttered transparent biomedical objects captured as calibrated multi-view sequences. TrainsBiolab contains 161,315 frames from 98 scenes and 1.03M instance annotations over 15 laboratory object types, including 6D poses, full and visible masks, depth, and per-frame camera calibration. The dataset is organized along three axes that reflect operational difficulty: object category, the total number of objects in a frame, and camera viewpoint. We further define dataset-centric benchmarks for segmentation, depth estimation and completion, and 6D pose estimation, and report a system-level robot manipulation evaluation enabled by the released annotations and calibrations. By focusing on repeated transparent instances, clutter, and multi-view laboratory capture, TrainsBiolab provides a resource for segmentation, depth estimation, 6D pose estimation, and multi-view reasoning in autonomous laboratory manipulation. Project page: https://dualtransparency.github.io/TransBiolab/.

</details>

#### 2026-07-23 - WAT3R: Feedforward Underwater 3D Reconstruction

**Authors:** Jiayi Xu, Jiahao Lu, Ziqiang Zheng, Yihao Tan, Yaolong Zhu, Yuan Liu, Sai-Kit Yeung
**Links:** [abs](https://arxiv.org/abs/2607.21023) - [pdf](https://arxiv.org/pdf/2607.21023)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, multi-view reconstruction, camera pose estimation, pose estimation, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WAT3R: Feedforward Underwater 3D Reconstruction
- 作者：Jiayi Xu, Jiahao Lu, Ziqiang Zheng, Yihao Tan, Yaolong Zhu, Yuan Liu, Sai-Kit Yeung
- 出版日期：2026-07-23T08:07:43Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.21023

### 一句话总结
提出了一种前馈式框架WAT3R，通过轻量级神经适配模块处理水下光照衰减和背向散射，直接从水下图像高效重建高质量3D场景。

### 研究问题
水下图像因光线衰减和背向散射导致视觉质量下降、跨视角特征不一致，使得前馈式3D重建难以获得准确的多视图几何结构。

### 核心思路/方法
将水下成像退化视为一种受几何约束的过程，集成一个轻量级神经适配模块来灵活建模成像效应，从而在单个前向传播中从水下视频直接输出像素对齐的3D点图与相机位姿。

### 主要贡献
1. 提出了WAT3R，一个前馈式水下3D重建框架，无需迭代优化即可高效重建。
2. 设计退化适配模块，将水下成像效应作为几何约束过程处理，改善多视图重建质量。
3. 在FLSea、SQUID和USOD10K数据集上，该方法在多视图/单目深度估计与相机位姿估计任务上均超越现有最先进方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对水下环境这一特定场景提出前馈式3D重建方案，并在公开数据集上取得显著提升，方法具有实用性；但未涉及泛化性分析或极端退化案例，且摘要未提供实验细节，适合对水下视觉或前馈式3D重建感兴趣的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Reliable feedforward underwater 3D reconstruction remains challenging due to severe light attenuation and backscattering, which degrade visual quality and disrupt feature consistency across views, leading to inaccurate multi-view geometry. To address this issue, we propose WAT3R, a feed-forward framework for reconstructing 3D scenes directly from underwater images. By leveraging degradation adaptation as a geometry-constrained process, WAT3R integrates a lightweight neural adaptation module to flexibly account for these underwater imaging effects, thereby improving multi-view reconstruction quality. Implemented in a single forward pass, WAT3R directly and efficiently outputs pixel-aligned 3D point maps and camera poses from underwater videos, allowing a high-quality underwater 3D reconstruction. Experiments conducted on the FLSea, SQUID, and USOD10K datasets show that our method consistently outperforms state-of-the-art approaches on 3D reconstruction tasks, including multi-view/monocular depth estimation and camera pose estimation.

</details>

#### 2026-07-20 - Robust Multimodal Dynamic Object Segmentation

**Authors:** Zhe Xin, Hanzhi Chang, Penghui Huang, Yinian Mao, Guoquan Huang
**Links:** [abs](https://arxiv.org/abs/2607.18153) - [pdf](https://arxiv.org/pdf/2607.18153)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robust Multimodal Dynamic Object Segmentation  
- 作者：Zhe Xin, Hanzhi Chang, Penghui Huang, Yinian Mao, Guoquan Huang  
- 出版日期：2026-07-20  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2607.18153  

### 一句话总结  
提出一种融合2D点轨迹、3D重建和语义信息的多模态动态物体分割框架，通过Transformer与特征聚类聚合模块实现精确且完整的动态掩膜生成。  

### 研究问题  
现有基于光流的方法无法保证物体边界的静态/动态分割一致性，而基于3D重建的方法对重建误差高度敏感。如何实现鲁棒且精确的动态物体分割？  

### 核心思路/方法  
1. 设计融合Transformer和特征聚类聚合模块的网络，对多模态特征轨迹进行静态/动态分类。  
2. 模型能够根据场景特征自适应决定主导模态，并缓解特征退化问题。  
3. 引入基于点查询的SAM后处理方法，可处理单个掩膜内的多个物体。  

### 主要贡献  
- 提出整合2D点轨迹、3D重建和语义信息的多模态动态分割框架。  
- 设计自适应模态主导机制与特征退化缓解策略。  
- 提出点查询SAM后处理，支持单掩膜多物体处理。  
- 实验表明在动态物体分割与静态场景重建任务中达到最佳性能。  

### 局限性  
摘要未提供足够信息。  

### 阅读优先级  
**高**  
理由：该文在动态分割领域提出融合多种模态（2D轨迹、3D重建、语义）的新框架，并明确指出了现有方法的缺陷（边界不一致、对重建误差敏感），方法设计具有创新性（自适应模态选择、点查询SAM），同时宣称在两项任务上达到SOTA，适合对视觉分割、3D场景理解感兴趣的读者优先关注。

</details>

<details>
<summary>Abstract</summary>

Dynamic object segmentation plays a critical role in many visual applications such as static scene reconstruction from dynamic videos. However, existing optical flow-based methods fail to ensure consistent static/dynamic segmentation along object boundaries, while 3D reconstruction-based approaches are highly sensitive to reconstruction errors. To address these limitations, we present a dynamic object segmentation framework that can generate both precise and complete dynamic masks by integrating multimodal cues including 2D point tracks, 3D reconstruction, and semantic information. We design a network combining Transformer architectures with feature clustering aggregation modules to perform static/dynamic classification of multimodal feature trajectories. It enables the model to adaptively determine which type of feature should dominate based on the characteristics of each scene, while also mitigating the impact of feature degradation. Additionally, we introduce a novel point-query-based SAM post-processing method capable of handling multiple objects within a single mask. Extensive experiments demonstrate that our approach achieves state-of-the-art performance in both dynamic object segmentation and static scene reconstruction tasks.

</details>

#### 2026-07-20 - Plenoptic Condensation: A Novel Approach to Generalized Scene Reconstruction

**Authors:** Brevin Tilmon, Alex DeJournett, John Leffingwell, Scott Ackerson
**Links:** [abs](https://arxiv.org/abs/2607.18151) - [pdf](https://arxiv.org/pdf/2607.18151)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, rendering, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Plenoptic Condensation: A Novel Approach to Generalized Scene Reconstruction
- 作者：Brevin Tilmon, Alex DeJournett, John Leffingwell, Scott Ackerson
- 出版日期：2026-07-20
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.18151

### 一句话总结
本文提出一种名为“全光凝聚”（Plenoptic Condensation, PCon）的新型通用场景重建方法，通过多阶段重建管道将图像转化为可自适应凝聚的结构化元素，实现了高保真渲染与精细损伤测量。

### 研究问题
如何实现通用场景重建（Generalized Scene Reconstruction, GSR），在保持高保真渲染与测量精度的同时，自适应地处理不同区域（如锐利边缘、光滑反射面）的表示能力需求？

### 核心思路/方法
PCon采用多阶段重建管道：
1. **初始转化**：将输入图像转换为低表示能力的“汤状”场景元素（soupy scene elements）。
2. **自适应凝聚**：将“汤状”元素自适应地凝聚为高表示能力的“结构化”元素，从而高效表示复杂特征（如锐利边缘、光滑反射面）。
3. **输出模型**：生成的场景模型称为“实相模型”（Reality Models, Relms），具有空间可变的表示能力，支持高保真渲染、测量和场景理解。

### 主要贡献
1. 提出了PCon这一GSR新方法，通过多阶段凝聚机制实现空间可变的表示能力。
2. 展示了使用消费级手机和无人机拍摄的野外场景重建效果（包括“Damaged Fiat”案例）。
3. 在“Damaged Fiat”案例中，PCon在重建汽车发动机盖时精度是SOTA方法（NeRO和RT-Splatting）的两倍以上，且局部损伤剖面误差仅为35微米（0.035毫米），而对比方法基本无法测量损伤。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法提出了一种新颖的多阶段凝聚范式，在消费级设备上实现了远超SOTA的重建精度（尤其在高精度局部测量任务中），对3D重建与多视图几何领域具有潜在重要影响。

</details>

<details>
<summary>Abstract</summary>

We present a novel Generalized Scene Reconstruction (GSR) approach called Plenoptic Condensation (PCon). PCon uses a multi-stage reconstruction pipeline, initially converting images into "soupy" scene elements with low (representational) power, then adaptively condensing the "soup" into "structured" elements of higher power capable of efficiently representing, for example, sharp edges and smooth reflective surfaces. PCon scene models called Reality Models (Relms) enable spatially varying representational power, which is essential for high-fidelity rendering, measurement, and scene understanding. We showcase several in-the-wild PCon reconstructions captured with consumer phone cameras and drones. In one case called "Damaged Fiat", PCon is benchmarked against two state-of-the-art (SOTA) GSR methods: NeRO and RT-Splatting. Referring to Figure 1 below, PCon reconstructs the car hood more than twice as accurately as the SOTA methods. But more importantly, the local damage profile error for PCon is 35 um (0.035 mm), whereas the two other SOTA methods are essentially unable to measure the damage at all. Our project website is available at https://quidient.github.io/pcon-2026.html.

</details>

#### 2026-07-20 - UMCP: A Unified Multi-Task Collaborative Perception Network for Luggage Trolley Pose Estimation

**Authors:** Zhirui Sun, Zhihao Jiang, Yao Wang, Jianwei Peng, Jiankun Wang
**Links:** [abs](https://arxiv.org/abs/2607.17950) - [pdf](https://arxiv.org/pdf/2607.17950)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UMCP: A Unified Multi-Task Collaborative Perception Network for Luggage Trolley Pose Estimation
- 作者：Zhirui Sun, Zhihao Jiang, Yao Wang, Jianwei Peng, Jiankun Wang
- 出版日期：2026-07-20T13:51:01Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2607.17950；PDF: https://arxiv.org/pdf/2607.17950

### 一句话总结
本文提出一个名为UMCP的统一多任务协作感知网络，用于同时进行行李车检测、关键点检测和朝向估计，在保持竞争精度的同时显著降低模型复杂度和计算成本。

### 研究问题
在机器人自动收集行李车的任务中，如何实现高精度且实时的视觉感知，以避免现有级联多模型推理导致的推理延迟增加和部署成本过高的问题。

### 核心思路/方法
基于YOLOv12架构，将关键点特征与朝向特征融合，并送入朝向特征增强模块（OFEM）以提升朝向估计精度；此外，采用圆形概率分布建模和KL散度损失进一步优化朝向估计。

### 主要贡献
1. 提出统一的单阶段多任务协作网络UMCP，同时实现检测、关键点检测和朝向估计。
2. 设计朝向特征增强模块（OFEM），通过融合关键点特征增强朝向估计。
3. 引入圆形概率分布建模与KL散度损失，提升朝向估计精度。
4. 实验表明，该方法在保持竞争精度的同时，显著降低了模型复杂度和计算成本。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法针对行李车姿态估计这一特定应用场景，虽有一定通用性（多任务协作），但核心创新点（YOLOv12架构基础上的特征融合与概率建模）属于工程优化，理论贡献有限；且摘要未提供具体精度与速度数值，需要阅读全文才能评估实际效果。

</details>

<details>
<summary>Abstract</summary>

In robotic autonomous luggage trolley collection, robots must continuously localize scattered luggage trolleys in cluttered and dynamic environments. This requires the vision system to achieve both high accuracy and real-time performance. However, existing visual perception approaches for luggage trolleys often rely on cascaded multi-model inference, leading to increased inference latency and high deployment costs. To address these limitations, this article presents a unified multi-task collaborative perception network (UMCP) that simultaneously performs luggage trolley detection, keypoint detection and orientation estimation. Based on the YOLOv12 architecture, keypoint features are fused with orientation features and then fed into an orientation feature enhancement module (OFEM), thereby improving orientation estimation accuracy. In addition, circular probability distribution modeling with a Kullback-Leibler (KL) divergence loss is adopted to enhance orientation estimation accuracy further. Experimental results demonstrate that the proposed method achieves competitive overall accuracy while substantially reducing model complexity and computational cost compared with existing methods. A website about this work is available at https://sites.google.com/view/robot-umcp.

</details>

#### 2026-07-20 - SLAM in Low-Light Environments: Project Report

**Authors:** Oleh Basystyi, Anna Stasyshyn, Oleksandr Kosovan, Yaroslav Prytula
**Links:** [abs](https://arxiv.org/abs/2607.17699) - [pdf](https://arxiv.org/pdf/2607.17699)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, feature matching, robotics, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SLAM in Low-Light Environments: Project Report  
- 作者：Oleh Basystyi, Anna Stasyshyn, Oleksandr Kosovan, Yaroslav Prytula  
- 出版日期：2026-07-20  
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.17699  

### 一句话总结
该报告在低光照环境下基准测试了六种SLAM系统，发现仅惯性融合与全局优化并存的系统（Kimera-VIO）能稳定完成全部序列，而纯RGB方法在高难度低光照序列中普遍失效。

### 研究问题
低光照环境下，仅使用标准RGB摄像头的SLAM系统能达到何种跟踪精度与鲁棒性？当前主流方法的局限性及潜在改进方向是什么？

### 核心思路/方法
在LaMARia数据集的五个不同难度与光照水平序列上，对六种SLAM系统（ORB-SLAM3、DSO、Kimera-VIO、OpenVINS、DPVO、DPV-SLAM）进行基准测试，使用绝对姿态误差、相对姿态误差以及控制点召回率作为评价指标。

### 主要贡献
1. 系统性地评估了六种SLAM范式（特征法、直接法、滤波法、学习法）在低光照环境下的表现。  
2. 发现仅Kimera-VIO（同时包含惯性融合与全局优化）能成功跟踪全部五条序列，且相对姿态误差最低，但绝对误差因无闭环修正而持续增长。  
3. 指出学习型方法（DPVO、DPV-SLAM）虽不丢失跟踪，但在低光照下绝对误差可达约100米；经典单目及滤波方法在大多数困难低光照序列上彻底失败或发散。

### 局限性
- 摘要未提及实验的具体扫描环境、序列长度或计算资源开销。  
- 摘要未说明Kimera-VIO为何比其他系统更优的具体机制。  
- 摘要未提供各方法的完整定量误差值，仅给出了定性结论。  

### 阅读优先级
中  
理由：该工作针对低光照SLAM这一实际工程难点进行了系统基准测试，结论具有参考价值；但摘要未提供详细实验数据，且问题叙述较为通用，适合关注SLAM鲁棒性评估的读者，而非寻求新算法或创新方法的读者。

</details>

<details>
<summary>Abstract</summary>

Simultaneous localization and mapping (SLAM) is one of the fundamental problems in robotics, as it enables autonomous operations in real-world scenarios. Under low illumination, reduced contrast, sensor noise, and motion blur degrade both feature extraction and feature matching, while compensating with LiDAR, depth, or thermal sensors raises cost, power draw, and integration complexity. Existing benchmarks remain dominated by well-lit indoor or daylight sequences, leaving open how far SLAM with standard RGB cameras can be pushed in the dark. We benchmark six systems spanning the feature-based, direct, filter-based, and learning-based paradigms - ORB-SLAM3, DSO, Kimera-VIO, OpenVINS, DPVO, and DPV-SLAM - on five LaMARia sequences of varying difficulty and illumination, reporting absolute and relative pose error alongside control-point recall. Kimera-VIO is the only system to track all five sequences to completion, combining the lowest relative pose error with steadily growing absolute error due to the absence of loop closure; DPVO and DPV-SLAM never lose tracking but incur absolute errors of roughly 100 m under low light; and the classical monocular pipelines (ORB-SLAM3, DSO) together with the filter-based OpenVINS fail outright or diverge on most of the harder and low-light sequences. The results suggest that RGB-only SLAM maintains stable low-light tracking only when both inertial fusion and global optimization are present. Closing the remaining gap will likely require low-light-specific learned front-ends or a return to complementary sensing.

</details>

#### 2026-07-19 - DepthART: Scaling Foundation Monocular Depth to Tiny Models

**Authors:** Feng Xue, Wu Chen, Mingshuai Zhao, Guofeng Zhong, Anlong Ming, Haozhe Wang, Dianqiao Lei, Zhaowen Lin, Haiyang Zhang, Nicu Sebe
**Links:** [abs](https://arxiv.org/abs/2607.17099) - [pdf](https://arxiv.org/pdf/2607.17099)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DepthART: Scaling Foundation Monocular Depth to Tiny Models
- 作者：Feng Xue, Wu Chen, Mingshuai Zhao, Guofeng Zhong, Anlong Ming, Haozhe Wang, Dianqiao Lei, Zhaowen Lin, Haiyang Zhang, Nicu Sebe
- 出版日期：2026-07-19
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.17099

### 一句话总结
本文提出DepthART，一种针对小型模型设计的紧凑型单目深度估计模型，通过抗偏置数据采样与相机条件微调两项策略，在保持低计算量的同时显著提升了零样本泛化能力和度量精度。

### 研究问题
如何将先进的几何基础模型（如Metric3D、Depth Anything）在单目深度估计中的跨场景泛化与度量预测能力，有效迁移至资源受限的微型模型上，解决微型模型因容量不足而导致的过拟合和度量不稳定问题。

### 核心思路/方法
1. **识别瓶颈**：发现微型模型存在两个关键瓶颈：一是过度拟合数据集特定的分布偏置；二是在相机参数变化时度量尺度调整不稳定，全参数微调会破坏可迁移的几何知识。
2. **抗偏置数据采样**：设计一种数据采样方案，在相同训练预算下减少分布偏置的影响。
3. **相机条件微调协议**：冻结蒸馏后的编码器，仅根据相机内参条件调整度量尺度，从而保留跨数据集的泛化能力。

### 主要贡献
- 提出DepthART模型，首次将基础模型的深度估计优势成功扩展到微型模型，适合设备端部署。
- 识别并解决了微型模型在深度估计中的两个关键容量瓶颈。
- 提供可扩展的模型家族，DepthART-S在RTX A6000上达到347/245 FPS（FP32），在Jetson Nano 4GB上超过15 FPS。
- 在多个数据集上超越先前微型基线，例如在NYUD v2上零样本δ₁=0.964，部分结果接近大型模型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。
理由：该工作聚焦于将基础模型压缩至微型设备，对边缘计算和实时应用有实际意义；方法明确且性能提升显著。但若读者不关注模型部署或微型模型压缩，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Recent geometric foundation models (e.g., Metric3D, Depth Anything and UniDepth) have substantially improved monocular depth estimation (MDE) in both cross-scene generalization and metric-scale prediction, yet these gains have not translated to tiny models. We bridge this gap with DepthART (Depth Anything Rethought for Tiny Models), which is a compact MDE model for on-device deployment across diverse scenes. We first identify two capacity-driven bottlenecks in tiny models: (i) overfitting to dataset-specific distribution bias and (ii) unstable metric adaptation under camera shift, where full fine-tuning easily damages transferable geometry. Accordingly, DepthART combines two simple but effective strategies: a bias-resistant data sampling scheme to reduce distribution bias under the same training budget, and a camera-conditioned fine-tuning protocol that freezes the distilled encoder and adjusts metric scale conditioned on intrinsics while better preserving cross-dataset generalization. Across datasets, DepthART consistently surpasses previous tiny baselines in both zero-shot generalization and metric accuracy (e.g., zero-shot $δ_1$=0.964 for DepthART-S on NYUD v2), and in some cases approaches heavy models. We further provide a scalable model family, with DepthART-S reaching 347/245 FPS (strict FP32) on an RTX A6000 at $224^2/448^2$, 102 FPS (TF32) on a Orin NX 8GB, and over 15 FPS (FP32) on a Jetson Nano 4GB.

</details>

#### 2026-07-18 - Splat-based 3D Scene Reconstruction with Extreme Motion-blur

**Authors:** Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim
**Links:** [abs](https://arxiv.org/abs/2607.16926) - [pdf](https://arxiv.org/pdf/2607.16926)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, scene reconstruction, camera pose estimation, pose estimation, 3D mapping, Gaussian Splatting, scene representation, radiance, splatting, robotics, mapping, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Splat-based 3D Scene Reconstruction with Extreme Motion-blur
- 作者：Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim
- 出版日期：2026-07-18
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2607.16926) | [PDF](https://arxiv.org/pdf/2607.16926)

### 一句话总结
本文提出一种基于高斯溅射的RGB-D三维场景重建方法，通过联合相机位姿估计与图像去模糊，有效应对极端运动模糊场景下的重建挑战。

### 研究问题
在低光照或快速运动条件下，RGB图像常因长时间曝光产生严重运动模糊，导致传统相机位姿估计方法（如COLMAP）和三维重建技术（如NeRF、Gaussian Splatting）失效；同时，深度传感器的视野限制和快速相机运动减少了点云重叠，降低了ICP算法位姿估计的效果。如何在此极端条件下实现高质量三维重建是核心问题。

### 核心思路/方法
1. **输入与数据对齐**：利用光流和ICP算法初步对齐连续RGB-D帧。
2. **位姿与几何优化**：通过调整高斯位置以实现最佳深度对齐，从而细化相机位姿和三维几何。
3. **运动模糊处理**：在曝光时间内建模相机运动，通过比较输入图像与一系列清晰渲染帧实现去模糊。
4. **框架基础**：基于高斯溅射框架，结合三维高斯溅射和深度输入增强场景表示。

### 主要贡献
- 提出一种结合相机位姿估计与图像去模糊的高斯溅射方法，专门应对极端运动模糊。
- 通过建模曝光期间的相机运动，实现从模糊输入恢复清晰场景。
- 构建了一个新的极端运动模糊RGB-D数据集，并公开代码与数据集。
- 实验表明，该方法在挑战条件下优于现有技术，对机器人、自动驾驶和增强现实等三维映射应用有重要意义。

### 局限性
摘要未提供足够信息。例如，未提及方法在非运动模糊场景下的性能、计算开销、对深度传感器噪声的敏感性，或与无深度输入方法的对比。

### 阅读优先级
**高**。理由：该工作针对低光照和快速运动这一实际难题提出了新的解决方案，结合了去模糊与高斯溅射框架，且公开了代码与数据集，对从事三维重建、机器人感知、AR/VR的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We propose a splat-based 3D scene reconstruction method from RGB-D input that effectively handles extreme motion blur, a frequent challenge in low-light environments. Under dim illumination, RGB frames often suffer from severe motion blur due to extended exposure times, causing traditional camera pose estimation methods, such as COLMAP, to fail. This results in inaccurate camera pose and blurry color input, compromising the quality of 3D reconstructions. Although recent 3D reconstruction techniques like Neural Radiance Fields and Gaussian Splatting have demonstrated impressive results, they rely on accurate camera trajectory estimation, which becomes challenging under fast motion or poor lighting conditions. Furthermore, rapid camera movement and the limited field of view of depth sensors reduce point cloud overlap, limiting the effectiveness of pose estimation with the ICP algorithm. To address these issues, we introduce a method that combines camera pose estimation and image deblurring using a Gaussian Splatting framework, leveraging both 3D Gaussian splats and depth inputs for enhanced scene representation. Our method first aligns consecutive RGB-D frames through optical flow and ICP, then refines camera poses and 3D geometry by adjusting Gaussian positions for optimal depth alignment. To handle motion blur, we model camera movement during exposure and deblur images by comparing the input with a series of sharp, rendered frames. Experiments on a new RGB-D dataset with extreme motion blur show that our method outperforms existing approaches, enabling high-quality reconstructions even in challenging conditions. This approach has broad implications for 3D mapping applications in robotics, autonomous navigation, and augmented reality. Both code and dataset are publicly available on https://github.com/KAIST-VCLAB/gs-extreme-motion-blur.

</details>

#### 2026-07-18 - GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

**Authors:** Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
**Links:** [abs](https://arxiv.org/abs/2607.16897) - [pdf](https://arxiv.org/pdf/2607.16897)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM
- 作者：Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- 出版日期：2026-07-18
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.16897

### 一句话总结
本文提出GLidE-SLAM，一种面向嵌入式设备的单目混合间接-直接SLAM框架，通过将GPU加速的直接跟踪与CPU间接管线分离，在资源受限硬件上实现了高达9倍的帧率提升。

### 研究问题
如何在嵌入式设备上部署Visual SLAM时，在保持高跟踪帧率的同时，为地图扩展和维护保留足够的计算资源。

### 核心思路/方法
采用架构分离策略：系统使用OpenGL ES 3.1 compute shaders（独立于CUDA）在中间帧上进行GPU加速的直接跟踪（仅位姿估计，无需深度优化或地图点创建），而将完整的间接管线（用于地图扩展和全局一致性）保留给CPU处理。这种设计将适合高度并行的图像对齐操作卸载到GPU，从而释放CPU资源用于后端任务。

### 主要贡献
1. 提出首个在嵌入式设备上通过compute shaders实现完整直接光度位姿估计的SLAM系统。
2. 通过GPU-CPU架构分离，在目标平台上实现比仅CPU基线高达9倍的帧率提升，同时保持轨迹精度。
3. 采用vendor-agnostic的OpenGL ES 3.1标准，使系统可在更广泛的商用嵌入式平台上部署，无需CUDA支持。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该方法针对嵌入式设备上的SLAM性能优化，提出了创新的GPU加速直接跟踪方案，实验显示显著帧率提升。若读者关注资源受限硬件上的高效V-SLAM，则值得阅读；若对SLAM算法精度或通用框架设计更感兴趣，则优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

With the growing demand for robotics, autonomous drones, and wearable extended reality systems, the deployment of Visual SLAM on embedded devices remains challenging. Tracking must sustain high frame rates while preserving compute resources for map extension and maintenance. This paper presents GLidE-SLAM, a monocular hybrid indirect-direct framework that addresses this by architectural separation: the system performs GPU-accelerated direct tracking on intermediate frames, while reserving the full indirect pipeline for map extension and global consistency. We leverage highly parallel image-alignment operations for pose-only estimation without depth optimization or map point creation, making the workload suitable for GPU offloading and freeing CPU resources for backend tasks. We implement the direct tracker using vendor-agnostic OpenGL ES~3.1 compute shaders, enabling deployment across a broader range of commodity embedded platforms without requiring CUDA support. To our knowledge, this is the first complete direct photometric pose estimator realized via compute shaders for embedded-class devices. Experiments on target platforms demonstrate up to 9$\times$ higher frame rates than the CPU-only baseline while maintaining trajectory accuracy and improving practical deployment across commodity resource-constrained hardware.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-23 - SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization

**Authors:** Jiun Lee, Jaekwang Kim, Sangmin Lee
**Links:** [abs](https://arxiv.org/abs/2607.20813) - [pdf](https://arxiv.org/pdf/2607.20813)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization
- 作者：Jiun Lee, Jaekwang Kim, Sangmin Lee
- 出版日期：2026-07-23
- 分类：Neural Scene Representations & Rendering (神经场景表征与渲染)
- 链接：摘要: https://arxiv.org/abs/2607.20813 | PDF: https://arxiv.org/pdf/2607.20813

### 一句话总结
SubSplat 提出了一种亚像素高斯重参数化方法（SPGR），通过将低分辨率特征中的主高斯分解为细粒度基元，在保持低计算成本的同时实现了高分辨率、像素对齐的逼真新视角合成。

### 研究问题
像素对齐的高斯泼溅在渲染高分辨率图像时面临两难困境：提高输入分辨率可改善细节但使网络计算成本呈二次方增长；而保持低分辨率输入虽能稳定计算成本，却导致高斯密度不足并产生视觉伪影。SubSplat 旨在解决这一计算效率与渲染保真度之间的权衡问题。

### 核心思路/方法
核心思路是引入 **Sub-pixel Gaussian Reparameterizer (SPGR)**，直接从低分辨率特征中恢复高斯密度。具体做法是：将原始（初级）高斯体细分为更精细的基元（fine-grained primitives），从而在不依赖高分辨率输入的情况下重现必要的结构细节。此外，通过 **特征聚合（feature aggregation）** 增强重参数化质量，该机制能有效地从多视角捕捉高频细节。

### 主要贡献
1. 提出 SubSplat 框架，成功解决了像素对齐高斯泼溅中重参数化保真度与网络计算成本之间的固有矛盾。
2. 引入 SPGR，在低计算成本下从低分辨率特征重建高密度高斯基元，实现高效的高分辨率渲染。
3. 通过多视图特征聚合增强重参数化效果，提升高频细节的捕获能力。
4. 在 RealEstate10K 和 ACID 数据集上验证了该方法在渲染质量和效率上的优越性。

### 局限性
摘要未提供足够信息，例如在特定场景（如非朗伯表面或极稀疏视图）下的表现、对视频/动态场景的适用性，或计算资源需求的具体量化指标。

### 阅读优先级
**高**。理由：该工作直接针对像素对齐高斯泼溅在多分辨率下的核心计算瓶颈（二次方增长 vs. 密度不足），并提出了一种新颖的重参数化解法。结合其在标准数据集（RealEstate10K, ACID）上的验证，对关注高效神经渲染和 3D 高斯泼溅优化的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Pixel-aligned Gaussian splatting enables efficient and generalizable novel-view synthesis. However, high-resolution rendering faces a critical trade-off where increasing input resolution improves detail at the expense of quadratically rising network computational cost. Conversely, maintaining low-resolution inputs stabilizes this cost but results in insufficient Gaussian density and artifacts. To address this, we propose SubSplat, which introduces Sub-pixel Gaussian Reparameterizer(SPGR) to subdivide primary Gaussians into fine-grained primitives, restoring structural density directly from low-resolution features. We further enhance the reparameterization quality through feature aggregation, which effectively captures high-frequency details across multiple views. Experiments on RealEstate10K and ACID demonstrate that SubSplat achieves high-fidelity rendering with superior efficiency. Our results validate that the proposed framework successfully resolves the trade-off between reparameterization fidelity and network computational cost inherent in pixel-aligned Gaussian Splatting.

</details>

#### 2026-07-22 - 3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch

**Authors:** Xuening Tian, Dieter Schmalstieg, Shohei Mori
**Links:** [abs](https://arxiv.org/abs/2607.20789) - [pdf](https://arxiv.org/pdf/2607.20789)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch
- 作者：Xuening Tian, Dieter Schmalstieg, Shohei Mori
- 出版日期：2026-07-22
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.20789

### 一句话总结
本文提出3D-GIMP方法，通过一次生成式修补结合3D-aware PatchMatch传播，高效实现3D高斯泼溅场景中的高保真物体移除，避免了逐帧扩散的高成本与多视图不一致问题。

### 研究问题
如何在3D高斯泼溅场景中高效、高保真地去除物体，同时保持渲染速度、视图一致性和高频细节，避免逐帧扩散带来的计算瓶颈和“幻觉漂移”导致的视图不一致与结构伪影。

### 核心思路/方法
1. **单参考视图生成**：仅对单个关键参考视图进行一次生成式修补，将其作为外观先验。
2. **3D-aware PatchMatch传播**：设计三维感知的PatchMatch算法，通过对应匹配将参考纹理传播至所有剩余视图，避免逐帧扩散的随机性。
3. **重建一致性优先**：优先保证重建数学一致性而非迭代生成，从而在不同分辨率下维持高频细节，确保三维重建在数学上一致。

### 主要贡献
- 提出一种新的混合范式3D-GIMP，将单次生成修补与3D-aware PatchMatch结合，用于3D高斯泼溅中的高保真物体移除。
- 实验表明，3D-GIMP在修补质量上与使用多视图扩散的先前方法竞争力相当，同时在渲染速度和视图一致性上超越这些方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接针对3D场景编辑中的核心痛点（计算效率、视图一致性、细节保留），提出一种轻量且有效的混合方案；实验表明其性能在渲染速度和一致性上优于主流的多视图扩散方法，对实际应用具有重要潜力。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D scene editing have leveraged iterative diffusion models to update input views. However, this process is computationally expensive and struggles to produce sharp details. Meanwhile, ``hallucination drift'' frequently introduces multi-view inconsistencies, leading to structural artifacts when rendering novel viewpoints. To address this problem, we present 3D-GIMP (3D Gaussian Inpainting Meets Patch Matching), a novel hybrid paradigm designed for high-fidelity object removal in 3D Gaussian Splatting. Instead of diffusing every view, 3D-GIMP performs a single generative inpainting on a key reference view, which serves as an appearance prior. We then introduce a 3D-aware PatchMatch algorithm to propagate these reference textures across all remaining views via correspondence matching, effectively bypassing the stochastic nature of frame-by-frame diffusion. By prioritizing reconstructive consistency over iterative generation, 3D-GIMP maintains high-frequency details across arbitrary resolutions while ensuring a mathematically consistent 3D reconstruction. Our experiments demonstrate that 3D-GIMP not only achieves competitive inpainting quality as previous methods using diffusion in multiple views, but also outperforms these methods in rendering speed and view consistency.

</details>

#### 2026-07-22 - RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring

**Authors:** Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue
**Links:** [abs](https://arxiv.org/abs/2607.20628) - [pdf](https://arxiv.org/pdf/2607.20628)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring
- 作者：Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue
- 出版日期：2026-07-22（需注意该日期晚于当前时间，可能为未来论文或笔误）
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：摘要URL: https://arxiv.org/abs/2607.20628；PDF URL: https://arxiv.org/pdf/2607.20628

### 一句话总结
本文提出RealVDeblur，一个基于单步扩散模型的视频去模糊框架，通过物理驱动的模糊合成管道和高效推理设计，实现在真实世界多样条件下的鲁棒复原。

### 研究问题
真实世界视频去模糊面临运动模式多样化、退化复杂以及真实训练数据稀缺的挑战，且需为下游任务（如移动成像、3D重建）提供稳健的复原结果。

### 核心思路/方法
1. **模糊合成管道**：利用场景级3D高斯泼溅（3DGS）资产和高帧率视频构建大规模、物理逼真的模糊合成管道，生成包含相机运动模糊和物体运动模糊的训练数据。
2. **视频扩散先验**：采用视频扩散模型作为复原先验，为适应帧间模糊变化，禁用VAE中的时间压缩并改用逐帧编码方案。
3. **高效推理**：将扩散模型的多步采样蒸馏为单步生成器，并引入无需训练的“时间窗口掩码”方法，在训练时长外稳定推理且保持内存恒定。

### 主要贡献
- 提出一个从3DGS和高帧率视频出发的物理驱动模糊合成管线，用于生成丰富多样的真实模糊训练数据。
- 设计了适配帧间模糊变化的视频扩散复原框架，并通过蒸馏实现高效单步生成。
- 开发了一种无需训练的时间窗口掩码技术，支持长视频推理且内存占用恒定。
- 在多个真实世界基准上展示了出色的感知质量、语义保真度、时间一致性，以及在下游3D重建任务中对严重运动模糊的鲁棒性提升。

### 局限性
摘要未提供足够信息。未讨论方法的计算资源需求、模型规模或对特定模糊类型（如极端低光）的适用性。

### 阅读优先级
**高**。理由：本文针对真实世界视频去模糊这一实际难题，提出了一个包含数据合成、扩散模型适配和高效率推理的完整框架，且在下游任务（3D重建）上验证了鲁棒性，对计算机视觉与神经渲染领域有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-world video deblurring remains challenging due to diverse motion patterns, complex degradations, and the scarcity of realistic training data, yet robust restoration is critical for downstream pipelines such as mobile imaging and 3D reconstruction. This work presents \textbf{RealVDeblur}, an efficient generative framework designed to improve in-the-wild robustness under diverse real capture conditions. First, a large-scale, physically grounded blur synthesis pipeline is constructed from scene-level 3D Gaussian Splatting (3DGS) assets and high-frame-rate videos, providing realistic training data covering both camera-induced and object-motion blur. Second, a video diffusion prior is leveraged for restoration; to better accommodate frame-dependent blur variations, temporal compression in the VAE is disabled and a frame-wise encoding scheme is adopted. For practical deployment on long videos, multi-step diffusion sampling is distilled into an efficient one-step generator, and a training-free Temporal Window Mask stabilizes inference beyond the training horizon with constant memory usage. Extensive experiments on diverse real-world benchmarks demonstrate strong perceptual quality, semantic fidelity, and temporal consistency on unseen videos, as well as improved robustness in downstream 3D reconstruction under severe motion blur. Project page: https://rbjin.github.io/RealVDeblur

</details>

#### 2026-07-22 - ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion

**Authors:** Cho In, Jeonghwan Cho, Mijin Yoo, Gim Hee Lee, Seon Joo Kim
**Links:** [abs](https://arxiv.org/abs/2607.20417) - [pdf](https://arxiv.org/pdf/2607.20417)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- **标题**：ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion
- **作者**：Cho In, Jeonghwan Cho, Mijin Yoo, Gim Hee Lee, Seon Joo Kim
- **出版日期**：2026-07-22
- **分类**：Neural Scene Representations & Rendering
- **链接**：https://arxiv.org/abs/2607.20417

### 一句话总结
ATSplat 提出了一种自适应令牌扩展的前馈式 3D 高斯泼溅方法，通过稀疏锚点令牌和自适应扩展机制，在保持紧凑表示的同时实现了高质量的新视角合成。

### 研究问题
现有的前馈式 3D 高斯泼溅（3DGS）方法通常将高斯体素固定到输入像素并沿射线提升，导致高斯体素的数量和位置依赖图像分辨率而非场景复杂度，产生密集且冗余的高斯集，丧失了 3DGS 优化中的自适应容量分配能力。

### 核心思路/方法
1. **稀疏锚点令牌生成**：先利用粗粒度的图像块深度和相机线索，在 3D 空间中生成稀疏的锚点令牌，形成场景的紧凑骨架。
2. **局部高斯回归**：每个令牌通过学习到的 3D 偏移量回归出局部高斯体素，使体素放置与输入图像网格解耦。
3. **自适应令牌扩展**：通过预测令牌维度的不确定性分数（由渲染误差图监督），选择性地利用可学习扩展层对高不确定性令牌进行扩展，从而在挑战区域集中更多高斯体素，同时保持整体表示紧凑。

### 主要贡献
1. 提出了一种前馈式 3DGS 框架 ATSplat，恢复了 3DGS 优化中的自适应分配能力。
2. 通过稀疏锚点令牌和自适应令牌扩展机制，将高斯体素的数量减少至密集前馈方法（如 5.7 倍）的同时，获得更优或相当的渲染质量。
3. 在 RealEstate10K 和 DL3DV 数据集上达到最先进的渲染质量，且推理速度快：12 张 512×960 输入图像，在单 GPU 上完成重建不到 1 秒，渲染 1136 FPS（512×960），仅用 311K 个高斯体素。

### 局限性
摘要未提供足够信息，无法判断该方法的局限性，例如对输入图像数量、场景动态性、光照变化的鲁棒性等。

### 阅读优先级
**高**
理由：该方法有效解决了前馈式 3DGS 中高斯体素冗余的核心问题，在保持高质量渲染的同时实现显著压缩和高速推理，对实时场景重建与渲染有重要实践价值；实验结果在多个指标上表现突出，且方法设计新颖（自适应令牌扩展），适合关注 3D 场景表示、新视角合成和高效渲染的读者。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves high-quality novel-view synthesis by optimizing freely placed primitives in 3D and adaptively densifying them in under-reconstructed regions. However, this scene-adaptive capacity allocation is largely lost in existing feed-forward 3DGS methods, which commonly regress Gaussians at input pixels and lift them along camera rays. Such pixel-aligned formulations make the number and placement of primitives depend on image resolution and input viewpoints rather than scene complexity, resulting in dense and often redundant Gaussian sets. We present ATSplat, a feed-forward 3DGS framework that restores the adaptive allocation capability of 3DGS optimization through Adaptive 3D Tokens. ATSplat first lifts coarse patch-level depth and camera cues into sparse 3D anchor tokens, forming a compact scaffold of the scene. Each token is then regressed into local Gaussians with learnable 3D offsets, decoupling primitive placement from input image grids. An Adaptive Token Expansion module predicts a token-level uncertainty score, supervised by rendering error maps, and selectively expands high-uncertainty tokens through learnable expansion layers. This sparse-to-adaptive formulation enables ATSplat to concentrate primitives in challenging regions while maintaining a compact representation. Experiments on two representative datasets, RealEstate10K and DL3DV, show that ATSplat achieves state-of-the-art rendering quality while reducing the number of Gaussians by more than $5.7\times$ compared with dense feed-forward 3DGS methods. From 12 input images at $512 \times 960$ resolution, ATSplat completes reconstruction in less than a second using a single commercial GPU, and renders high-quality novel views at 1136 FPS ($512 \times 960$) with only 311K Gaussians.

</details>

#### 2026-07-22 - MR-Compare: A Mixed-Reality Framework for Spatially Grounded Visual Comparison of 3D Gaussian Splatting and Mesh Reconstructions with the Physical Environment

**Authors:** Changrui Zhu, Ernst Kruijff, Pengju Zhang, Simon Julier
**Links:** [abs](https://arxiv.org/abs/2607.20325) - [pdf](https://arxiv.org/pdf/2607.20325)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MR-Compare: 一种用于三维高斯泼溅和网格重建与物理环境空间锚定视觉比较的混合现实框架
- 作者：Changrui Zhu, Ernst Kruijff, Pengju Zhang, Simon Julier
- 出版日期：2026年7月22日
- 分类：神经场景表示与渲染 / 具身/机器人/增强现实应用
- 链接：摘要URL：https://arxiv.org/abs/2607.20325；PDF：https://arxiv.org/pdf/2607.20325

### 一句话总结
本文提出了一个名为MR-Compare的混合现实框架，通过视频透视技术实现三维高斯泼溅和网格重建与物理环境的空间对齐视觉比较，并在两个室内房间中通过用户研究验证了其可行性。

### 研究问题
如何在混合现实中实现三维高斯泼溅（3DGS）和网格重建与真实物理环境的精确空间对齐和直观视觉对比？

### 核心思路/方法
1. 基于PC连接的Meta Quest 3头显，构建一个混合现实框架，包含一个两阶段配准流程和一个用于跨媒体比较的3D滑块。
2. 通过一个包含30名用户的探索性用户研究，在静态室内房间中评估了五种典型的桌面和移动端重建工作流，着重测量配准误差和视觉一致性。
3. 提出了一种各向异性滤波器，作为一种零样本模块，利用高斯泼溅的各向异性特性来改进3DGS在MR-Compare中的配准性能，并通过控制Replica阈值扫描发现适度修剪可提升鲁棒性并降低残差。

### 主要贡献
1. 提出了MR-Compare框架，实现了厘米级的翻译误差和较高的感知可用性、低工作负荷。
2. 系统评估显示桌面端3DGS工作流（尤其是3DGS-MCMC）在配准误差和VST参考视觉一致性上表现最佳。
3. 提出的各向异性滤波器在零样本条件下可提升3DGS配准的鲁棒性，且适度修剪能减少残差误差。

### 局限性
1. 摘要明确指出这些结果“建立了在测试场景下的系统级可行性，而非任务级有效性或独立部署”，因此缺乏对实际任务完成效果和独立使用场景的验证。
2. 评估仅在两个静态室内房间中进行，场景多样性和动态环境适应性未涉及。
3. 摘要未提供具体用户研究任务细节、错误率的定量比较，以及各向异性滤波器在不同工作流下的普适性验证。

### 阅读优先级
中  
理由：该工作在场景重建与混合现实的交叉领域提出了一个实用框架和评价方法，对从事AR/VR场景可视化或三维重建比较的研究者有参考价值。但由于摘要明确其验证限于系统可行性而非任务级效果，且缺乏对动态场景或通用性部署的讨论，对追求算法性能提升或应用落地的读者吸引力有限。

</details>

<details>
<summary>Abstract</summary>

We introduce MR-Compare, a mixed reality framework for spatially grounded visual comparison between 3D Gaussian splatting and mesh reconstructions with live video see-through (VST). Implemented on a PC-tethered Meta Quest~3, it combines a two-stage registration pipeline with a 3D Slider for cross-media comparison. We evaluated five representative desktop and mobile reconstruction workflows through a real-world benchmark with an exploratory user study ($n=30$) in two static indoor rooms. MR-Compare achieved centimetre-level translation error across all workflows. The two desktop 3DGS workflows showed the strongest overall pattern, with 3DGS-MCMC yielding the lowest registration error and strongest VST-referenced visual consistency. Room-session measures indicated high perceived usability and low workload. We further propose an anisotropy filter, a zero-shot module that leverages Gaussian anisotropies to improve 3DGS registration in MR-Compare. A controlled Replica threshold sweep shows that moderate pruning can improve robustness and reduce residual errors. These results establish system-level feasibility in the tested setting rather than task-level effectiveness or standalone deployment. The project is available at https://github.com/changruizhu96/MR-Compare.

</details>

#### 2026-07-22 - Look Before You Edit: Attention-Guided Camera Placement and Multi-View Alignment for 3D Gaussian Splatting Editing

**Authors:** Jaeyeon Park, Taeho Kang, Youngki Lee
**Links:** [abs](https://arxiv.org/abs/2607.19777) - [pdf](https://arxiv.org/pdf/2607.19777)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Look Before You Edit: Attention-Guided Camera Placement and Multi-View Alignment for 3D Gaussian Splatting Editing
- 作者：Jaeyeon Park, Taeho Kang, Youngki Lee
- 出版日期：2026-07-22
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.19777

### 一句话总结
本文提出LB-Edit框架，通过注意力引导的编辑相机放置和多视图对齐技术，解决了基于3D高斯泼溅（3DGS）的文本驱动场景编辑中编辑范围受限和多视图不一致的问题。

### 研究问题
现有文本驱动的3DGS编辑方法使用固定训练相机视角，导致编辑空间覆盖有限，且难以对复杂场景中的特定对象进行局部编辑，同时多个视角的编辑结果不一致，影响3D场景的全局一致性。

### 核心思路/方法
1. **注意力引导的编辑相机放置（ACP）**：在多个候选相机距离下探测扩散模型的自注意力和交叉注意力，找到注意力在感兴趣区域内高度集中的最优距离，然后在该距离处放置一组紧凑且几何多样的编辑相机。
2. **多视图注意力对齐（MAA）**：通过两条轴对齐多视图编辑：一是通过令牌级对应共享自注意力特征来对齐外观；二是将交叉注意力图提升到3D高斯上作为共享的3D注意力场，对齐空间位置，从而抑制外观和空间漂移。

### 主要贡献
- 提出ACP方法，能够自动选择最优编辑相机位置和距离，实现局部、紧凑的编辑。
- 提出MAA方法，通过注意力机制在多个视图间对齐编辑的外观和空间位置，提升3D一致性。
- 实验表明，该方法仅需5个编辑视图，在指令保真度、多视图一致性和编辑局部性上达到最高用户偏好，且延迟比现有方法降低最多7倍。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文针对3DGS编辑中的关键难题（局部编辑受限与多视图不一致）提出创新性框架，实验效果显著，效率提升明显，且属于神经场景表示与渲染领域的前沿工作，对相关研究和应用具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Text-driven 3D scene editing with 3D Gaussian Splatting (3DGS) typically applies a 2D diffusion editor to views rendered from fixed training cameras, limiting both the spatial coverage of edits and the user's freedom to target specific objects in complex scenes. We present LB-Edit, a framework that addresses two coupled problems: where to place editing cameras for localized edits, and how to make per-view edits agree with one another so that the 3D scene remains consistent after fine-tuning. First, Attention-Guided Editing Camera Placement (ACP) probes the diffusion model's self- and cross-attention at multiple candidate camera distances to find where attention is well-contained in the region of interest, then places a compact, geometrically diverse editing camera set at that attention-optimal distance. Second, Multi-view Attention Alignment (MAA) steers the editor toward the same edit across views along two axes: it aligns appearance by sharing self-attention features via token-level correspondence, and aligns spatial location by lifting cross-attention maps onto the 3D Gaussians as a shared 3D attention field, suppressing both appearance and spatial drift. Experiments on multi-object and single-object scenes show that our method achieves the highest user preference in instruction fidelity, multi-view consistency, and editing locality, using as few as 5 editing views and reducing latency by up to 7x over existing methods.

</details>

#### 2026-07-22 - Extending a Large View Synthesis Model for Multi-view Panoptic Segmentation

**Authors:** Kwonyoung Ryu, In-Jae Lee, Jonghyun Jin, Hyunjee Lee, Jongmin Lee, Jaesik Park
**Links:** [abs](https://arxiv.org/abs/2607.19765) - [pdf](https://arxiv.org/pdf/2607.19765)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, novel view synthesis, view synthesis, rendering, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Extending a Large View Synthesis Model for Multi-view Panoptic Segmentation
- 作者：Kwonyoung Ryu, In-Jae Lee, Jonghyun Jin, Hyunjee Lee, Jongmin Lee, Jaesik Park
- 出版日期：2026-07-22
- 分类：神经场景表示与渲染
- 链接：[摘要](https://arxiv.org/abs/2607.19765) | [PDF](https://arxiv.org/pdf/2607.19765)

### 一句话总结
本文提出首个将大规模视图合成模型扩展至3D场景理解的工作，利用冻结的视图合成模型直接将输入视图中的全景标签传播到新视角，无需3D重建或针对分割的额外训练。

### 研究问题
如何在不进行3D重建或专门训练的情况下，利用大型视图合成模型的跨视图对应能力，实现多视图全景分割？

### 核心思路/方法
1. **观察基础**：发现视图合成模型从RGB监督中学到的空间对应关系可以泛化到非真实感信号（如双编码的全景标签），使得标签传播后仍保持一致的空间结构。
2. **标签编码与传播**：将输入视图的全景标签编码为二进制通道表示，然后直接通过预训练且冻结的视图合成模型，生成目标视图的分割结果。
3. **无需额外训练**：视图合成模型不进行任何分割相关的微调或训练，仅利用其已有的跨视图注意力机制。

### 主要贡献
1. 首个将大规模视图合成模型扩展到外观渲染之外，应用于3D场景理解的工作。
2. 提出一种无需3D重建或分割训练的全景分割管线，仅依靠输入标签传播。
3. 在ScanNet上，分割质量与需要显式3D重建的高斯方法相当，且在视图合成任务上PSNR高出7 dB以上。
4. 标签传播具有跨数据集迁移能力，无需微调即可在Replica数据集上超越对比方法。

### 局限性
- 摘要未提供足够信息：未讨论方法在复杂遮挡、标签噪声或大规模场景下的性能表现。
- 摘要未提供足够信息：未提及标签编码的具体实现细节（如二进制通道的构造方式）或计算开销。
- 摘要未提供足够信息：未分析模型对输入标签准确性的依赖程度或误差传播问题。

### 阅读优先级
**高**
- **理由**：该文提出的方法创新性强——首次将视图合成模型的能力从RGB渲染扩展到语义理解，且无需3D重建或额外训练，具有潜在的实用价值。实验结果在分割精度和视图合成质量上均有显著优势，并展现了跨数据集泛化能力，适合关注神经渲染、场景理解或无监督域迁移的研究者参考。

</details>

<details>
<summary>Abstract</summary>

Large view synthesis models synthesize novel views through cross-view attention without explicit 3D representations, and recent studies have shown that they learn accurate spatial correspondence from RGB supervision alone. We observe that this correspondence generalizes beyond appearance. When non-photorealistic signals such as binary encoded panoptic labels are passed through the model, they are propagated to novel views with consistent spatial structure. These results indicate that the correspondence learned for RGB view synthesis can also propagate view-independent per-pixel labels. From this observation, we present the first work to extend large view synthesis models beyond appearance rendering to 3D scene understanding. We propose a panoptic segmentation pipeline that reuses a frozen view synthesis model to propagate panoptic labels from input views to novel views, without 3D reconstruction or any segmentation-specific training of the view synthesis model. Given panoptic labels on the input views, we encode them into binary channel representations and pass them through the same model to render target-view segmentation. On ScanNet, our method achieves segmentation quality on par with Gaussian based approaches requiring explicit 3D reconstruction, while outperforming them in novel view synthesis by more than 7 dB. The label propagation also transfers across datasets, surpassing these approaches on Replica without any fine-tuning.

</details>

#### 2026-07-22 - Fast Wave-optics Rendering of Multiplane Images for 3D Holographic Displays

**Authors:** Brian Chao, Dario Seyb, Nathan Matsuda, Oliver Cossairt, Yang Zhou, Douglas Lanman, Gordon Wetzstein, Grace Kuo, Changwon Jang
**Links:** [abs](https://arxiv.org/abs/2607.19731) - [pdf](https://arxiv.org/pdf/2607.19731)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, neural rendering, novel view synthesis, view synthesis, rendering, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fast Wave-optics Rendering of Multiplane Images for 3D Holographic Displays
- 作者：Brian Chao, Dario Seyb, Nathan Matsuda, Oliver Cossairt, Yang Zhou, Douglas Lanman, Gordon Wetzstein, Grace Kuo, Changwon Jang
- 出版日期：2026-07-22
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.19731

### 一句话总结
本文提出一种基于多平面图像（MPI）的波动光学渲染管线，用于高效合成高质量全息图，相比现有方法在速度上提升高达25万倍，同时保持可比的图像质量。

### 研究问题
如何将基于神经渲染生成的3D场景表示（如MPI）高效转换为与全息显示兼容的格式，以实现高保真、高沉浸感的3D全息显示？

### 核心思路/方法
提出一种基于多平面图像（MPI）的波动光学渲染管线，用于计算机生成全息术（CGH）。该方法利用MPI的层状结构，通过优化的波动光学计算，直接合成全息图。

### 主要贡献
- 提出一种基于MPI的全息图合成算法，在运行时间上显著超越最先进的基元类CGH算法（速度提升高达25万倍），且图像质量可比。
- 在图像质量上显著优于传统基于分层的CGH算法。
- 在多种3D场景数据集上，通过仿真和实验验证了该方法在3D焦点堆栈和4D光场重建中的出色性能，且不牺牲效率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文针对全息显示这一新兴领域提出了高效解决方案，实现了数量级的速度提升，且实验结果涵盖仿真与实物验证，方法具有实际应用潜力，适合对全息显示、神经渲染或3D重建感兴趣的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent advances in neural rendering have unlocked unprecedented capabilities in 3D reconstruction and novel view synthesis, giving rise to applications such as virtual fly-throughs of a 3D scene reconstructed from a set of sparse, casually captured images. However, these renderings are viewed on a computer screen or conventional VR headsets as 2D images, greatly limiting the perceptual realism and immersiveness of such experiences. The rapid development in novel 3D scene representations calls for dedicated rendering algorithms that convert these readily-available 3D contents into formats that are compatible with emerging 3D display technologies, such as holographic displays. In this paper, we propose a wave-optics rendering pipeline that works with multiplane images (MPIs) for efficient and high-quality hologram synthesis. Our MPI-based computer-generated holography algorithm greatly outperforms state-of-the-art primitive-based CGH algorithms in terms of runtime, achieving speedups up to 250,000x while achieving comparable image quality, and significantly outperforms conventional layer-based CGH algorithms in terms of image quality. We validate our method extensively on a wide variety of 3D scene datasets both in simulation and through experimentally captured results, showing exceptional 3D focal stack and 4D light field reconstruction performance without sacrificing efficiency.

</details>

#### 2026-07-20 - QIRF Quantum-Inspired Non-Orthogonal Function-Space Compression for 3D Gaussian Splatting

**Authors:** Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang
**Links:** [abs](https://arxiv.org/abs/2607.18067) - [pdf](https://arxiv.org/pdf/2607.18067)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：QIRF: 量子启发的非正交函数空间压缩方法用于3D高斯泼溅
- 作者：Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang
- 出版日期：2026-07-20
- 分类：神经场景表示与渲染
- 链接：摘要: https://arxiv.org/abs/2607.18067 / PDF: https://arxiv.org/pdf/2607.18067

### 一句话总结
本文提出QIRF方法，通过量子启发的非正交函数空间压缩技术，在保持重建质量的同时大幅减少3D高斯泼溅中的高斯原语数量与存储成本。

### 研究问题
如何有效压缩3D高斯泼溅模型中因高斯基函数强重叠和非正交性导致的冗余，从而降低存储和渲染开销。

### 核心思路/方法
1. 将相邻高斯原语建模为局部非正交基，并将原语减少问题转化为子空间感知的选择问题。
2. 构建解析高斯重叠矩阵和辐射响应密度矩阵，分别表征功能冗余和渲染相关性。
3. 利用广义特征分解识别主导局部子空间，并选择代表性高斯原语。
4. 基于RRDM的响应模型和细节感知保护机制，在激进剪枝下保留视觉重要的高频结构。

### 主要贡献
1. 提出QIRF，一种量子启发的非正交函数空间压缩方法，首次系统探索高斯基函数非正交性导致的冗余。
2. 在13个场景（Mip-NeRF 360、Tanks and Temples、Deep Blending）上，平均高斯数量减少71.7%，原始PLY存储压缩约3.54倍。
3. 重建质量与3DGS相当，平均PSNR提升0.10 dB，平均渲染速度相比3DGS提升34.3%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该方法针对3D高斯泼溅中的非正交基冗余这一未充分探索的问题提出创新压缩框架，实验在多个基准数据集上取得显著压缩率和渲染速度提升，且质量保持良好，对场景表示与渲染领域的实际应用有重要价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves high-quality real-time rendering by representing a scene with a large collection of anisotropic Gaussian primitives. However, complex scenes often require millions of Gaussians, resulting in substantial storage and rendering costs. Existing compression methods mainly reduce redundancy through primitive-wise pruning, attribute quantization, clustering, or neural coding, while redundancy caused by strongly overlapping and non-orthogonal Gaussian basis functions remains largely unexplored. We present QIRF, a quantum-inspired non-orthogonal function-space compression method for 3D Gaussian Splatting. QIRF models neighboring Gaussian primitives as a local non-orthogonal basis and formulates primitive reduction as a subspace-aware selection problem. Specifically, an analytic Gaussian overlap matrix and a radiance-response density matrix are constructed to characterize functional redundancy and rendering relevance. Generalized eigendecomposition is then used to identify the dominant local subspace and select representative Gaussian primitives. An RRDM-based response model and detail-aware safeguarding further preserve visually important high-frequency structures under aggressive pruning. Experiments on 13 scenes from Mip-NeRF 360, Tanks and Temples, and Deep Blending show that QIRF reduces the Gaussian count and raw PLY storage by 71.7 percent on average, corresponding to approximately 3.54 times compression, while maintaining reconstruction quality comparable to 3DGS and achieving a marginal average PSNR improvement of 0.10 dB. QIRF also improves the average rendering speed over 3DGS by 34.3 percent. These results suggest that non-orthogonal function-space redundancy is an important yet underexplored source of representational redundancy in explicit Gaussian radiance fields.

</details>

#### 2026-07-20 - Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting

**Authors:** Chengbo Wang, Guozheng Ma, Jinhong Wu, Tie Ji, Yizhen Lao
**Links:** [abs](https://arxiv.org/abs/2607.17965) - [pdf](https://arxiv.org/pdf/2607.17965)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting
- 作者：Chengbo Wang, Guozheng Ma, Jinhong Wu, Tie Ji, Yizhen Lao
- 出版日期：2026-07-20
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.17965

### 一句话总结
本文发现3D高斯泼溅优化中存在一种称为“模糊陷阱”的梯度偏差，并通过引入随机播种和随机分裂两种简单探索策略来克服该陷阱，从而提升渲染质量。

### 研究问题
3D高斯泼溅的显式建模在优化过程中会产生梯度偏差，导致非凸优化容易收敛到局部次优解（即“模糊陷阱”），如何解决这一根本性局限？

### 核心思路/方法
1. 通过数学分析将模糊陷阱分为两种子类型：远侧模糊陷阱和近侧模糊陷阱。
2. 提出两种简单的探索策略：随机播种用于缓解远侧模糊陷阱，随机分裂用于缓解近侧模糊陷阱。

### 主要贡献
1. 首次识别并形式化了3D高斯泼溅优化中的“模糊陷阱”问题，并将其分为两类。
2. 提出了两种极简的探索操作（随机播种和随机分裂），互补性地有效克服了该陷阱。
3. 实验证明这些探索机制在多个数据集上实现了高质量渲染性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文针对3D高斯泼溅这一当前热门渲染方法的根本优化缺陷提出了新的解决思路，问题明确、方法简单有效，对从事神经渲染或场景重建的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) employs Gaussian primitives for explicit scene representation, facilitating real-time, high-fidelity reconstruction and novel view synthesis of complex scenes. However, the explicit modeling inherent in 3DGS introduces a gradient bias during optimization, rendering its non-convex optimization process highly susceptible to convergence toward local suboptimal solutions. This constitutes a fundamental limitation in 3DGS optimization, which we term the Blur Trap. To address this limitation, we integrate simple explicit exploration into the 3DGS optimization framework. First, through rigorous mathematical analysis of the 3DGS optimization formulation, we identify the underlying optimization bias responsible for the Blur Trap and categorize it into two distinct subtypes: the Far-Side Blur Trap and the Near-Side Blur Trap. Subsequently, we propose two highly straightforward exploration strategies (Random Seeding and Random Splitting) to mitigate the far-side and near-side blur traps, respectively. Experimental validation demonstrates that the incorporation of these exploration operators effectively and complementarily overcome the Blur Trap, achieving high-quality rendering performance across multiple datasets. Project page: https://chengbo-wang.github.io/ExploreGS/

</details>

#### 2026-07-20 - Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based Error Concealment

**Authors:** Yuxuan Tao, Xuerui Ma, Hao Zhang, Chunhua Peng
**Links:** [abs](https://arxiv.org/abs/2607.17916) - [pdf](https://arxiv.org/pdf/2607.17916)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based Error Concealment
- 作者：Yuxuan Tao, Xuerui Ma, Hao Zhang, Chunhua Peng
- 出版日期：2026-07-20
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.17916

### 一句话总结
本文提出了一种针对3D高斯溅射（3DGS）压缩流在丢包网络传输中的鲁棒性增强框架，通过原子锚点打包和基于图神经网络的错误隐藏机制，显著减少渲染失真。

### 研究问题
现有3DGS压缩方案（如HAC++）的比特流在网络传输时对丢包敏感，丢包会导致锚点属性不一致、渲染出现严重伪影，影响实时神经渲染的可靠性。

### 核心思路/方法
- **编码端**：采用原子锚点级别打包，将每个锚点的所有属性联合封装，使丢包从属性损坏变为干净的锚点缺失；配合分层随机分组，将丢包在空间上分散，避免连续大空洞。
- **解码端**：将恢复视为先验感知的属性修复。提出上下文感知残差插值分支（CARI），利用哈希网格先验预测和邻域残差构建鲁棒基线；轻量双层图神经网络（GNN）通过交叉注意力机制在哈希网格先验上细化高频属性残差；引入属性级置信度控制，当学习到的预测不可靠时回退至插值。

### 主要贡献
- 提出首个针对3DGS压缩流在丢包网络传输的鲁棒框架，并集成原子打包与分层分组策略。
- 设计结合哈希网格先验、残差插值及图神经网络的错误隐藏方法，实现先验感知的属性修复。
- 在三种基准数据集（BungeeNeRF, Mip-NeRF 360, Tanks and Temples）上，20%随机丢包条件下，相比无隐藏方案显著提升，将平均PSNR退化限制在约3 dB以内（相对于无损HAC++参考）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接解决3DGS压缩在实时网络传输中的实际鲁棒性问题，方法结合了原子打包、GNN和先验感知修复，实验验证效果显著；针对新兴的3DGS应用场景具有明确价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) and recent compression schemes such as HAC++ enable high-fidelity real-time neural rendering, but their bitstreams are fragile under packet loss during network streaming. Existing compression methods often separate correlated anchor attributes into independent streams, so losing one packet can create attribute-inconsistent broken anchors and severe rendering artifacts. We propose a packet-loss robust 3DGS transmission and error concealment framework. On the encoder side, anchor-level atomic packaging jointly encapsulates all attributes of each anchor, converting corrupted-attribute failures into clean missing-anchor erasures. Stratified random grouping further disperses packet losses across the spatial domain to avoid large contiguous voids. On the decoder side, we formulate recovery as prior-aware attribute inpainting. A Context-Aware Residual Interpolation (CARI) branch uses hash-grid prior predictions and neighboring residuals to build a robust baseline, while a lightweight two-layer graph neural network with cross-attention over hash-grid priors refines high-frequency attribute residuals. Attribute-wise confidence control falls back to interpolation when learned predictions are unreliable. Experiments under 20 percent random packet loss on BungeeNeRF, Mip-NeRF 360, and Tanks and Temples show that the proposed method substantially improves over no-concealment transmission and limits average PSNR degradation to about 3 dB relative to the lossless HAC++ reference.

</details>

#### 2026-07-20 - CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling

**Authors:** Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen
**Links:** [abs](https://arxiv.org/abs/2607.17842) - [pdf](https://arxiv.org/pdf/2607.17842)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling
- 作者：Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen
- 出版日期：2026-07-20T11:33:51Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.17842

### 一句话总结
CaT-GS 通过帧间缓存、预计算和分块调度优化，大幅提升大场景3D高斯泼溅（3DGS）渲染效率，实现最高10倍加速。

### 研究问题
大场景下3DGS渲染存在冗余预处理、视角相关的遮挡冗余以及分块级负载不均问题，导致GPU利用率低、性能下降。

### 核心思路/方法
提出三项关键技术：1）投机性多帧预处理方法，消除连续帧间的冗余计算；2）帧间缓存机制，消除视角冗余渲染阶段；3）专用内核重构光栅化任务，缓解分块负载不均衡，提升GPU利用率。

### 主要贡献
- 识别并系统分析大场景3DGS渲染中的三大效率瓶颈。
- 提出CaT-GS，一种高效的新型3DGS渲染管线，包含帧间缓存与分块调度策略。
- 实验表明，相比原始3DGS实现最高10倍加速，相比此前最先进方法提升最高70%，为大场景高保真实时渲染设立新基准。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：针对3DGS在大规模场景下的实际部署瓶颈，提出了系统性的工程优化方案，加速比显著且方法新颖，对实时神经渲染应用有直接指导价值。

</details>

<details>
<summary>Abstract</summary>

Recent breakthroughs in 3D Gaussian Splatting (3DGS) have advanced neural rendering with high fidelity and speed. However, its performance degrades significantly in large-scale scenes due to the computational burden of tile-based rasterization. Existing optimization efforts either require costly scene re-training or focus on narrow aspects of the pipeline, overlooking critical inefficiencies in real-world deployments. Through a comprehensive analysis, we identify three primary sources of redundancy and low GPU utilization: redundant inter-frame pre-processing, viewpoint-based occlusion redundancy, and severe tile-level load imbalance. To address these issues, we propose CaT-GS, a novel and efficient 3DGS rendering pipeline. CaT-GS introduces a speculative multi-frame preprocessing method to eliminate redundant computations across consecutive frames, and an inter-frame caching mechanism to eliminate viewpoint redundant rendering stages. Furthermore, it refactors rasterization tasks with a dedicated kernel to mitigate tile load imbalance, significantly boosting GPU utilization. Extensive experiments demonstrate that CaT-GS achieves a speedup of up to 10 times over the original 3DGS and up to 70% over previous state-of-the-art methods, establishing a new benchmark for high-fidelity, real-time rendering of large-scale scenes.

</details>

#### 2026-07-20 - FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System

**Authors:** Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang
**Links:** [abs](https://arxiv.org/abs/2607.17803) - [pdf](https://arxiv.org/pdf/2607.17803)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, Gaussian Splatting, inverse rendering, rendering, splatting, manipulation, mapping, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System
- 作者：Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang
- 出版日期：2026-07-20
- 分类：Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.17803, PDF: https://arxiv.org/pdf/2607.17803

### 一句话总结
本文提出FF-ProCams，一种前馈式3D高斯逆渲染框架，用于投影-相机系统，在保持高保真结果的同时实现实时重建（0.13秒），显著速度提升并支持未知投影模式和视角。

### 研究问题
如何解决投影-相机系统中传统逆渲染方法耗时优化（每场景优化）与前馈方法无法适应空间可变投影照明之间的矛盾，实现精度与效率的平衡。

### 核心思路/方法
1. **前馈框架设计**：采用混合Mamba2-Transformer编码器，从稀疏多视角观测中聚合跨视角几何和光度线索，并通过轻量级头部一次性预测可重照明的3D高斯表示。
2. **投影感知渲染器**：设计可微渲染器，合成任意主动照明和投影-相机姿态下的相机观测图像。
3. **大规模合成数据集**：构建覆盖多样物体几何和表面材质的合成ProCams数据集，用于前馈训练。

### 主要贡献
1. 提出了首个前馈式3D高斯逆渲染框架FF-ProCams，用于投影-相机系统，无需每场景优化。
2. 设计了投影感知的可微渲染器，支持任意主动照明和姿态下的图像合成。
3. 构建了大规模合成ProCams数据集，支持前馈训练。
4. 实验表明：仅用8个输入视图，性能优于使用297视图的优化基线，并将测试时重建速度降至0.13秒（三个到五个数量级加速）。

### 局限性
摘要未提供足够信息（如对复杂光照、极端材质或真实场景的泛化能力，以及大规模合成数据与真实世界性能的固有差异均未提及）。

### 阅读优先级
**高**
理由：该工作以极快的速度（0.13秒）重建高保真投影-相机系统结果，克服了传统优化方法耗时的缺点，且代码和数据集已开源。对于从事增强现实、投影映射、逆渲染等方向的读者，具有很强的实用参考价值和复现吸引力。

</details>

<details>
<summary>Abstract</summary>

Projector-camera (ProCams) systems achieve active scene perception and controllable appearance manipulation via structured illumination, serving as a core infrastructure for spatial augmented reality, projection mapping, and surface reflectance acquisition. Existing inverse-rendering methods for ProCams deliver high-fidelity results but rely on time-consuming per-scene optimization, while mainstream feed-forward 3D reconstruction models produce baked appearance that cannot adapt to spatially varying projector illumination. To resolve this accuracy-efficiency trade-off, we propose FF-ProCams, a Feed-Forward 3D Gaussian inverse-rendering framework for ProCams. A hybrid Mamba2-Transformer encoder aggregates cross-view geometric and photometric cues from sparse multi-view observations, and lightweight heads predict a relightable Gaussian representation in a single forward pass. We further design a projector-aware differentiable renderer to synthesize camera observations under arbitrary active illumination and ProCams poses. To enable feed-forward training, we construct a large-scale synthetic ProCams dataset covering diverse object geometries and surface materials. Experiments show FF-ProCams achieves high-fidelity projector-aware rendering, generalizes to unseen patterns, and supports novel projector-camera poses. Using only 8 input views, it outperforms optimization-based baselines with 297 views while reducing test-time reconstruction to 0.13 seconds (a three-to-five-order-of-magnitude speedup). The code and data are available at https://github.com/CPREgroup/FF-ProCams/.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-23 - HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors

**Authors:** Siyu Li, Kunyu Peng, Di Wen, Beiping Hou, Zhiyong Li, Kailun Yang
**Links:** [abs](https://arxiv.org/abs/2607.21281) - [pdf](https://arxiv.org/pdf/2607.21281)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors
- 作者：Siyu Li, Kunyu Peng, Di Wen, Beiping Hou, Zhiyong Li, Kailun Yang
- 出版日期：2026-07-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.21281

### 一句话总结
本文提出HGeo-TopoMap方法，通过显式先验地图与隐式空间关系分层提升自动驾驶拓扑地图构建的精度与鲁棒性，尤其解决了中心线检测难题。

### 研究问题
拓扑地图需要检测中心线等实例及其连接关系，但由于真实环境中中心线缺乏明确标注，中心线实例的检测仍是一个重大挑战。

### 核心思路/方法
1. **几何自适应学习模块**：针对逆透视变换得到的道路结构图，离散编码语义和空间特征，并用先验掩码注意力机制聚焦信息区域。
2. **几何一致性学习模块**：利用中心线的几何特性与空间关系，在几何感知解码器中通过对齐具有相同几何朝向的中心线特征来强制空间一致性。

### 主要贡献
1. 提出HGeo-TopoMap，使用显式先验地图与隐式空间关系分层提升拓扑地图构建。
2. 设计几何自适应学习与几何一致性学习两个模块，分别处理道路结构图与中心线空间一致性。
3. 在OpenLane-V2数据集上，方法在中心线、车道段及鲁棒性基准测试中均显著提升拓扑地图准确性，并在标准与挑战条件下稳定优于基线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中等**。理由：该方法聚焦于自动驾驶拓扑地图构建中中心线检测的具体痛点，属于计算机视觉与机器人领域的专项技术。如果研究方向涉及拓扑映射、鲁棒性感知或自动驾驶感知系统，则具有较高参考价值；否则对通用视觉任务研究者而言优先级一般。

</details>

<details>
<summary>Abstract</summary>

Topological maps are key outputs of autonomous driving perception systems, delivering essential road information for path planning. They identify instances such as centerlines and traffic signs, along with their connectivity relationships. Due to the lack of explicit markings for centerlines in real-world environments, the detection of centerline instances remains a significant challenge. To tackle this problem, we propose HGeo-TopoMap, which leverages an explicit prior map and implicit spatial relations to hierarchically boost topological mapping. First, a geometric adaptive learning module is designed for the road structure map obtained via inverse perspective mapping. This module discretely encodes semantic and spatial features from the map, followed by a prior-mask attention mechanism that selectively focuses on informative regions. Then, a geometric consistency learning module is devised, which leverages the geometric properties and spatial relationships of centerlines. Built on the geometry-aware decoder, it enforces spatial consistency by aligning features of centerline instances with identical geometric orientations. The proposed method is evaluated on the OpenLane-V2 dataset across the centerline, lane segment, and robustness benchmarks. Beyond substantial improvements in topological mapping accuracy, the proposed method offers the benefit of enhanced robustness, consistently outperforming baselines under both standard and challenging conditions. The source code and model weights will be made publicly available at https://github.com/lynn-yu/HGeo-TopoMap.

</details>

#### 2026-07-23 - A Real-Time Generalized Nash Equilibrium Framework for Interaction-Aware Autonomous Driving in Mixed Traffic

**Authors:** Nouhed Naidja, Mohamed-Cherif Rahal, Steve Pechberti, Stéphane Font, Guillaume Sandou, Marc Revilloud
**Links:** [abs](https://arxiv.org/abs/2607.21043) - [pdf](https://arxiv.org/pdf/2607.21043)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Real-Time Generalized Nash Equilibrium Framework for Interaction-Aware Autonomous Driving in Mixed Traffic
- 作者：Nouhed Naidja, Mohamed-Cherif Rahal, Steve Pechberti, Stéphane Font, Guillaume Sandou, Marc Revilloud
- 出版日期：2026-07-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.21043

### 一句话总结
本文提出了一个基于广义纳什均衡问题的实时决策框架，用于混合交通中自动驾驶汽车与人驾驶车辆的交互，并在真实测试轨道上验证了其有效性。

### 研究问题
如何在混合交通环境中，通过显式建模自动驾驶车辆与人驾驶车辆之间的共享约束（安全性、几何约束），实现实时、安全且自然的交互决策。

### 核心思路/方法
将驾驶交互形式化为一个广义纳什均衡问题（GNEP），以此显式建模自动驾驶策略与对手动作之间的动态可行性关联；为解决该非凸问题的实时性，采用基于粒子群优化（PSO）的专用求解器。

### 主要贡献
1. 提出了一个将驾驶交互建模为GNEP的决策框架，与解耦优化方法不同，该框架显式考虑了共享安全与几何约束。
2. 设计了一个基于PSO的实时求解器，在真实测试中实现了低于50毫秒的收敛时间。
3. 使用真实的雷诺Zoé自动驾驶车辆与人类驾驶员在测试轨道上进行了实验验证，表明系统能生成舒适、类人的轨迹。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由是：该工作聚焦于自动驾驶中交互决策的具体技术路线（GNEP+PSO），并在真实车辆上验证了实时性能，对从事运动规划与交互建模的研究者有参考价值；但摘要未提供与现有方法的定量对比或失败案例，创新性程度需结合全文评估，因此优先级为中等。

</details>

<details>
<summary>Abstract</summary>

Safe and efficient navigation in mixed-traffic environments remains a critical challenge for Autonomous Vehicles (AVs), primarily due to the complex interdependence between the AV's decisions and the unpredictable reactions of human drivers. This paper introduces a comprehensive decision-making framework that formulates the driving interaction as a Generalized Nash Equilibrium Problem (GNEP). Unlike decoupled optimization approaches, this framework explicitly models shared safety and geometric constraints, ensuring that the feasibility of the AV's strategy is dynamically linked to the opponent's actions. To solve this non-convex problem in real-time, we propose a dedicated solver based on Particle Swarm Optimization (PSO). The complete architecture was validated on a test track using a real autonomous Renault Zoé interacting with a human driver. Experimental results demonstrate the system's ability to handle critical scenarios by generating comfortable, human-like trajectories. Benchmarks confirm the solver's operational feasibility, achieving convergence in under 50 ms.

</details>

#### 2026-07-23 - TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation

**Authors:** Boyuan Wang, Yue Zhang, Xutao Xue, Xueyu Song, Yu Sun
**Links:** [abs](https://arxiv.org/abs/2607.21017) - [pdf](https://arxiv.org/pdf/2607.21017)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation
- 作者：Boyuan Wang, Yue Zhang, Xutao Xue, Xueyu Song, Yu Sun
- 出版日期：2026-07-23
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.21017；PDF: https://arxiv.org/pdf/2607.21017

### 一句话总结
本文提出TableVerse，一个全自动的Real2Sim pipeline，通过从非结构化互联网图像中确定性重建物理可信的桌面场景，构建了包含10万个独特环境与交互轨迹的大规模数据集TableVerse-100K，旨在推动通用机器人操作策略的研究。

### 研究问题
如何克服现有自动化数据合成方法生成的场景数据物理不真实、难以反映真实环境复杂杂乱布局的问题，从而为通用机器人操作提供大规模、高保真的数据基础。

### 核心思路/方法
- 提出全自动的**Real2Sim pipeline**：从现实生活图像数据（如互联网媒体）中确定性地重建桌面环境，而非依赖文本生成或程序化生成的“想象布局”。
- 该pipeline能够输出具有**精确度量尺度、真实拓扑结构和已验证机械稳定性**的高保真仿真环境。
- 集成**自动化任务条件轨迹生成框架**，为每个环境合成高质量、无碰撞的抓取与放置演示轨迹。
- 利用该流程构建**TableVerse-100K**数据集：包含10万个物理一致的独特环境及对应的交互轨迹。

### 主要贡献
- 提出将范式从“想象布局生成”转向“从非结构化图像数据中确定性重建”的TableVerse自动化流程。
- 构建了大规模、高保真的TableVerse-100K数据集，包含10万个物理一致的环境与交互演示，具有真实的资产组成和空间分布。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对通用机器人操作中数据规模与保真度不足的核心瓶颈，提出了一种新颖的确定性重建范式，并提供了大规模公开数据集（10万环境），对Embodied AI和机器人学习领域具有显著价值。

</details>

<details>
<summary>Abstract</summary>

The development of generalizable robotic manipulation policies is inherently bounded by the availability of large-scale, high-fidelity scene data. While recent automated synthesis methods attempt to bridge this gap via text-to-layout hallucination or simplified procedural generation, they frequently suffer from physical implausibility and fail to capture the complex, dense clutter of actual human environments. In this paper, we introduce TableVerse, a fully automated Real2Sim pipeline that shifts the paradigm from imaginative layout generation to deterministic reconstruction from unstructured, in-the-wild image data. Our framework seamlessly processes unscripted internet media into high-fidelity, simulation-ready tabletop environments with accurate metric scales, authentic topologies, and verified mechanical stability. Furthermore, an automated task-conditioned trajectory generation framework is integrated to synthesize high-quality, collision-free pick-and-place demonstrations. Leveraging this complete pipeline, we construct the TableVerse-100K Dataset, a large-scale corpus comprising 100,000 unique, physically consistent environments paired with interactive manipulation trajectories. By capturing diverse asset compositions, realistic spatial distributions, and high-quality demonstrations, TableVerse-100K establishes a highly scalable and high-fidelity data foundation, providing significant value to facilitate future research in generalizable robotic manipulation tasks.

</details>

#### 2026-07-22 - PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving

**Authors:** Yushan Liu, Tianxiong Lv, Bohua Wang, Hangqi Fan, Chenxu Zhao, He Zheng, Xuchang Zhong, Yifan Xie, Congyang Zhao, Zhihao Liao, Leigang Luo, Yang Cai, Xiao-Ping Zhang, Wenbo Ding
**Links:** [abs](https://arxiv.org/abs/2607.20175) - [pdf](https://arxiv.org/pdf/2607.20175)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving
- 作者：Yushan Liu, Tianxiong Lv, Bohua Wang, Hangqi Fan, Chenxu Zhao, He Zheng, Xuchang Zhong, Yifan Xie, Congyang Zhao, Zhihao Liao, Leigang Luo, Yang Cai, Xiao-Ping Zhang, Wenbo Ding
- 出版日期：2026-07-22T14:09:15Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.20175

### 一句话总结
PerceptDrive提出了一种自适应专家路由的感知先验世界-动作建模框架，在不使用测试时候选选择的情况下，仅依赖单目前视相机，实现了端到端自动驾驶的规划性能提升。

### 研究问题
如何将冻结的感知基础模型编码的丰富先验知识（几何、语义、动态）有效地转化为规划动作，解决窄条件化接口导致的任务相关线索衰减以及静态融合无法适应不同场景专家贡献的问题。

### 核心思路/方法
1. **感知先验世界-动作建模框架**：将来自冻结、驾驶自适应提供者的教师蒸馏先验，与来自冻结自监督视频编码器的密集观测潜变量，输入到可训练的专家路由世界-动作模型中。
2. **自适应专家路由**：利用专家特定查询分支处理信号，并通过先验保留目标将每个分支锚定到其先验。一个路由器从共享场景表示中预测软门控，组合专家条件后再进行轨迹生成。
3. **训练与推理**：训练时，使用特权规则驱动的子度量估计为分支特定轨迹草稿提供软门控蒸馏目标；推理时，移除特权组件，仅用单目前视相机生成单条轨迹，无测试时评分或重排序。

### 主要贡献
- 提出了PerceptDrive框架，将感知先验知识以自适应专家路由方式融入世界-动作建模，改善了端到端规划。
- 在NAVSIM v1和v2上实现了先进性能（PDMS 90.4 / EPDMS 90.2），无需测试时候选选择。
- 消融实验证实先验保留和场景条件化路由的互补增益，以及三个先验的差异化依赖。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：论文在主流自动驾驶基准（NAVSIM）上取得领先性能，且方法新颖（自适应专家路由与先验保留），对端到端规划领域的隐私感知和动作生成有直接参考价值。出版日期为2026年，属于较新研究，适合关注前沿方法的读者。

</details>

<details>
<summary>Abstract</summary>

Frozen perception foundation models encode rich geometric, semantic, and dynamic knowledge. Yet narrow conditioning interfaces may attenuate task-relevant cues, while static fusion cannot adjust expert contributions to each scene. We cast this challenge as the prior-to-plan transfer problem and introduce PerceptDrive, a perception prior world-action modeling framework with adaptive expert routing. PerceptDrive feeds teacher-distilled priors from a frozen, driving-adapted provider and dense observation latents from a frozen self-supervised video encoder into a trainable expert-routed world-action model. Expert-specific query branches process these signals, while a prior-retention objective anchors each branch to its prior. A router predicts soft gates from a shared scene representation and combines the expert conditions before trajectory generation. During training, privileged rule-based sub-metric estimates for branch-specific trajectory drafts provide soft-gate distillation targets. The predicted action-free future latent conditions a flow-matching actor. At inference, privileged components are absent; with one front-facing camera, PerceptDrive generates one trajectory per planning step without test-time scoring, reranking, or search. Experiments show that PerceptDrive achieves state-of-the-art performance with 90.4 PDMS on NAVSIM v1 and 90.2 EPDMS on NAVSIM v2, outperforming existing methods. Ablations confirm complementary gains from prior retention and scene-conditioned routing, alongside differential reliance on the three priors. These results demonstrate that preserving and adaptively routing perception priors improves direct planning without test-time candidate selection.

</details>

#### 2026-07-22 - KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding

**Authors:** Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai, Xuelong Li
**Links:** [abs](https://arxiv.org/abs/2607.19876) - [pdf](https://arxiv.org/pdf/2607.19876)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding
- 作者：Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai, Xuelong Li
- 出版日期：2026-07-22
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2607.19876) | [PDF](https://arxiv.org/pdf/2607.19876)

### 一句话总结
本文提出KineBench，一种不依赖逆动力学模型（IDM-free）的闭环基准测试，通过显式运动学接地直接提取6D末端执行器姿态，用于评估具身世界模型的物理一致性。

### 研究问题
现有评估具身世界模型物理一致性的闭环方法严重依赖逆动力学模型（IDM），但IDM在像素-运动学映射中存在分布外脆弱性，导致无法区分世界模型误差与提取器误差。如何减少这种归因模糊性？

### 核心思路/方法
提出KineBench，其核心是显式运动学接地管道：对生成视频逐帧使用级联视觉基础模型直接提取6D末端执行器姿态，随后在物理模拟器中执行以进行闭环验证。它还引入两个经典3D运动学指标（频谱弧长SPARC和Maruyama可操作性指数）以描述轨迹平滑度和运动学可行性，并基于ManiSkill3中的20个多样化操作任务构建四个递进评估套件（基础执行、任务迁移、视觉分布外泛化、复杂度条件缩放）。

### 主要贡献
1. 提出IDM-free闭环基准KineBench，消除IDM引入的归因模糊性。
2. 采用显式运动学接地管道，结合级联视觉基础模型和物理模拟器验证。
3. 引入机器人视角的运动学指标（SPARC、可操作性指数）用于更精细的评估。
4. 通过前沿模型评估揭示了具身视频生成中任务复杂度界定的非线性缩放行为，为数据扩展策略提供经验指导。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作专注于具身世界模型的评估基准构建，对设计可验证的物理一致性评估方法有方法论贡献。但如果读者当前不涉及具身世界模型、运动学接地或仿真评估框架，则优先度较低。摘要显示了清晰的方法论创新和实证发现，但未提供具体性能对比或失败案例，因此优先级中等。

</details>

<details>
<summary>Abstract</summary>

Evaluating the physical consistency of embodied world models(EWMs) is a critical open challenge. While closed-loop evaluation via simulator rollouts offers a more faithful assessment of physical plausibility than open-loop alternatives, existing frameworks almost exclusively rely on Inverse Dynamics Models(IDMs) for action extraction. Due to the intricate mapping from 2D pixel space to 3D kinematic space, the learned IDMs can be brittle to data outside their training distribution, resulting in unreliable action extraction from the generated videos with novel objects and scenarios. This creates an unavoidable attribution ambiguity between world model inaccuracies and extractor errors. To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for EWMs, built upon an explicit kinematic grounding pipeline. Given a generated video, KineBench employs cascaded visual foundation models to directly extract 6D end-effector poses from individual frames, which are then executed in a physics simulator for closed-loop validation. Beyond execution-based task success, KineBench incorporates two classical 3D kinematic metrics--Spectral Arc Length (SPARC) and the Maruyama Manipulability Index--to characterize trajectory smoothness and kinematic feasibility from a robot-centric perspective. Built on 20 diverse manipulation tasks in ManiSkill3, KineBench evaluates EWMs across four progressive suites: basic execution, task transfer, visual out-of-distribution generalization, and complexity-conditioned scaling. Evaluation across frontier models reveals task-complexity-bounded nonlinear scaling in embodied video generation, providing empirical guidance for future data-scaling strategies.

</details>

#### 2026-07-22 - SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving

**Authors:** Jiangfan Liu, Zexuan Cui, Tianyuan Zhang, Zonglei Jing, Zonghao Ying, Yaoyuan Zhang, Jiakai Wang, Xiaoqi Jiang, Aishan Liu, Xianglong Liu
**Links:** [abs](https://arxiv.org/abs/2607.19701) - [pdf](https://arxiv.org/pdf/2607.19701)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving
- 作者：Jiangfan Liu, Zexuan Cui, Tianyuan Zhang, Zonglei Jing, Zonghao Ying, Yaoyuan Zhang, Jiakai Wang, Xiaoqi Jiang, Aishan Liu, Xianglong Liu
- 出版日期：2026-07-22
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.19701，PDF: https://arxiv.org/pdf/2607.19701

### 一句话总结
SafeGen提出了一种基于目标条件的视频扩散框架，用于生成安全关键场景（如危险的人车交互），以测试和提升基于视觉语言模型（VLM）的自动驾驶系统的安全性。

### 研究问题
如何生成真实、多样且具有不可预见性的人-车交互安全关键场景，以有效评估基于VLM的自动驾驶系统（VLMAD）的安全性，并克服现有基于模拟器方法存在的“模拟到现实”差距（sim-to-real gap）。

### 核心思路/方法
- 核心公式：将场景生成建模为**目标条件扩散过程（goal-conditioned diffusion process）**——预设的灾难性最终状态（catastrophic end-state）作为强监督信号，引导生成时间上连贯的视频轨迹，使其自然演化到安全关键结局。
- 两步流程：
  1. **Context Grounded End State Reasoning**：利用VLM分析正常的驾驶上下文，推断人-车交互中的潜在脆弱性，生成结构化的最终状态规格（end-state specifications），从而诱发高风险场景。
  2. **End State Conditioned Video Evolution**：将语义威胁落地为物理上合理的视觉动态。具体包括：通过深度感知几何投影（depth-aware geometric projection）在场景中实例化高风险代理，再通过边界条件扩散（boundary-conditioned diffusion）生成中间帧，确保运动模式一致和时间连贯性。

### 主要贡献
- 提出了SafeGen框架，将安全关键场景生成转化为目标条件扩散过程，克服了模拟器方法的局限性。
- 引入了“Context Grounded End State Reasoning”，利用VLM自动从良性驾驶上下文中推断出潜在风险，生成结构化目标。
- 设计了“End State Conditioned Video Evolution”机制，将语义威胁转化为符合物理规律的视觉动态。
- 实验表明，在3个VLMAD上，SafeGen将评估VLMAD理解与决策的“Judge Overall Score”平均提升24.25%（对比当前最优方法），且基于其生成的场景微调VLMAD后，在真实驾驶场景中的性能平均提升15.9%。

### 局限性
摘要未提供足够信息来讨论该方法的局限性，例如计算成本、对VLM推理的依赖程度、生成场景的多样性边界或在不同天气/光照条件下的鲁棒性等。

### 阅读优先级
**高**。理由：该工作针对自动驾驶安全评估这一核心难题，提出了一种基于扩散模型的新颖框架，直接解决了模拟器方法的关键弱点（sim-to-real gap）。实验指标提升显著（24.25%和15.9%），且方法结合了VLM推理与视频生成，体现了前沿技术融合趋势，对于从事自动驾驶安全、VLM评估或视频生成的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

VLMs are increasingly deployed in AD systems, creating an urgent need for rigorous safety evaluation under rare yet safety-critical scenarios. Among these, interactions with vulnerable road users represent a major source of real-world failures. However, existing safety-critical scenario generation methods predominantly rely on simulator-based pipelines, which suffer from a substantial sim-to-real gap and often fail to capture realistic, diverse, and unforeseen human-vehicle interaction dynamics. We present SafeGen, a goal-conditioned diffusion framework for safety-critical scenario generation in VLMADs. Our key insight is to formulate scenario generation as a goal-conditioned diffusion process, where a predefined catastrophic end-state serves as a strong supervisory signal, guiding the generation of temporally coherent video trajectories that naturally evolve toward safety-critical outcomes. Building on this formulation, we introduce Context Grounded End State Reasoning, which leverages VLMs to analyze benign driving contexts and infer latent vulnerabilities in human-vehicle interactions, producing structured end-state specifications that induce high-risk scenarios. Conditioned on these targets, we further propose End State Conditioned Video Evolution, which grounds semantic threats into physically plausible visual dynamics. Specifically, we instantiate high-risk agents within the scene via depth-aware geometric projection, followed by boundary-conditioned diffusion to generate intermediate frames with consistent motion patterns and temporal coherence. Extensive experiments across 3 VLMADs demonstrate that SafeGen increases the Judge Overall Score, a metric using a VLM judge to evaluate VLMADs' understanding and decision-making, by 24.25% on average compared to SoTA baselines. Furthermore, fine-tuning a VLMAD improves performance in real-world driving scenes by an average of 15.9%.

</details>

#### 2026-07-21 - LowPowAR: Power-Constrained Tone Mapping for Augmented Reality

**Authors:** Weikai Lin, Sheng Zhao, Ian Ross, Carl Marshall, Sushant Kondguli, Yuhao Zhu
**Links:** [abs](https://arxiv.org/abs/2607.19509) - [pdf](https://arxiv.org/pdf/2607.19509)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LowPowAR: Power-Constrained Tone Mapping for Augmented Reality
- 作者：Weikai Lin, Sheng Zhao, Ian Ross, Carl Marshall, Sushant Kondguli, Yuhao Zhu
- 出版日期：2026-07-21T18:48:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2607.19509，PDF https://arxiv.org/pdf/2607.19509

### 一句话总结
本文提出一种受功率约束的色调映射框架，将增强现实眼镜的显示功耗优化问题转化为在给定功率预算下最大化感知质量的色调映射问题，并通过学习的方法实现实时部署。

### 研究问题
如何在全天候穿戴式增强现实眼镜的严格功率限制下，优化显示功耗以在有限功耗预算内最大化视觉感知质量。

### 核心思路/方法
将显示功率优化形式化为功率约束的色调映射问题，提出一种基于人类视觉感知的学习框架。具体包括：设计一种优化友好的色调映射算子参数化方法，并采用渐进式优化策略来权衡质量与功耗；将迭代优化过程蒸馏为一个轻量级的前馈神经网络，以实现实时推理。

### 主要贡献
1. 将AR显示功耗优化重新定义为功率约束的色调映射问题。
2. 提出一种基于人类视觉、可学习的框架，在给定功耗预算下最大化感知质量。
3. 引入优化友好的色调映射参数化方案和渐进式优化策略。
4. 通过蒸馏迭代优化为轻量级神经网络实现实时部署。
5. 主观实验表明在同等功耗预算下，该方法比先前工作具有更好的感知质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工作聚焦于AR显示功耗优化的具体技术问题，方法新颖且具有实际部署潜力。但摘要中未提供明确的数值对比或详细实验设置，对于追求技术深度细节的读者可能需要查阅全文。对于从事AR硬件优化或低功耗视觉计算的从业者而言具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Everyday-wearable Augmented Reality (AR) glasses must meet strict power limits, making displays a key target for optimization. We cast display power optimization as a power-constrained tone-mapping problem and propose a human-vision-grounded, learning-based framework that maximizes perceptual quality under a given power budget. We introduce an optimization-friendly tone-mapping operator (TMO) parameterization along with a progressive optimization strategy to effectively navigate the quality-vs-power landscape. We distill the iterative optimization into a lightweight feed-forward neural network for real-time deployment. Subjective experiments show that our method yields better perceptual quality than prior work at the same power budget. Project page: https://horizon-lab.org/lowpowar/.

</details>

#### 2026-07-21 - Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents

**Authors:** Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen
**Links:** [abs](https://arxiv.org/abs/2607.19190) - [pdf](https://arxiv.org/pdf/2607.19190)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents
- 作者：Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen
- 出版日期：2026-07-21
- 分类：具身/机器人/AR应用
- 链接：https://arxiv.org/abs/2607.19190

### 一句话总结
该工作提出一个基于视觉-语言智能体的框架，能将真实世界的物体-机器人交互记录自动转换为可运行的物理仿真场景（即“数字孪生”），在多个领域实现统一且低成本的现实到仿真转换。

### 研究问题
如何将真实世界中的物体-机器人交互过程，自动转化为可直接用于物理仿真运行的“数字孪生”场景，并克服现有流程依赖手动调参、网格清理、坐标系对齐等繁琐步骤的局限。

### 核心思路/方法
提出**Agentic Real2Sim**框架，利用视觉-语言智能体（VLM）驱动决策，自动完成真实场景的几何重建、物体状态恢复、物理参数推断，并组装参与者（机器人）、物体、相机、位姿和运动轨迹，形成可运行的物理仿真孪生体。智能体决策可由开源VLM后端驱动，成本仅为前沿模型的零头。

### 主要贡献
1. 提出首个统一框架，可处理刚体操作、可变形物体交互和类人运动场景的Real2Sim转换（传统上这些场景需不同管道）。
2. 框架由视觉-语言智能体自动完成繁琐的工程步骤，无需人工干预。
3. 证明智能体决策可使用低成本开源VLM后端，仍能达到与前沿模型相当的成功率。
4. 生成的仿真孪生体与真实世界对齐，可用于下游机器人策略学习与评估。

### 局限性
摘要未提供关于实验失败案例、场景复杂性上限、物理精度量化对比、计算资源消耗等具体局限性的信息。摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作瞄准机器人仿真中关键且困难的“真实到仿真”自动转换问题，提出的多场景统一框架具有实用潜力，且采用低成本VLM的方案降低了门槛。对于从事具身智能、机器人策略迁移或物理仿真研究的读者，有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-to-sim conversion for robotic interaction with objects remains labor-intensive because it requires more than visual reconstruction: a streamlined real2sim process must recover scene geometries and object states, infer physical parameters, and assemble actors, objects, cameras, poses, and trajectories into a runnable physical simulation. Today this process still depends on manual tuning of visual foundation models, mesh cleanup, coordinate-frame alignment, and brittle workflow glue across visual perception tools and simulators. We introduce \textit{Agentic Real2Sim}, a framework for generalized physical world modeling with vision-language agents, converting a real-world recording of object-robot interaction into a simulatable episodic twin which preserves observations, geometries, robot interactions, and object states. We evaluate Agentic Real2Sim on rigid-object manipulation, deformable-object interaction, and humanoid motion scenes, spanning domains that are usually handled by separate Real2Sim pipelines, marking a first step toward scalable conversion. The framework's agentic decisions can be driven by an open-weight VLM backend at a small fraction of the cost of frontier models, while attaining comparable conversion success rate. We aim to use the resulting real-world-aligned twins for downstream robotics tasks, specifically policy learning and evaluation. The project site is available at https://agentic-real2sim.github.io/.

</details>

#### 2026-07-20 - When 2D Cues Fail: Improving Image Manipulation Localization with Reliable 3D Geometry

**Authors:** Guofeng Yu, Zhiqing Guo, Dan Ma, Gaobo Yang
**Links:** [abs](https://arxiv.org/abs/2607.18040) - [pdf](https://arxiv.org/pdf/2607.18040)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reasoning, manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：When 2D Cues Fail: Improving Image Manipulation Localization with Reliable 3D Geometry
- 作者：Guofeng Yu, Zhiqing Guo, Dan Ma, Gaobo Yang
- 出版日期：2026-07-20
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.18040

### 一句话总结
本文提出一种利用可靠3D几何线索（深度、表面法向）来增强图像篡改定位性能的框架GFrame，以解决纯2D线索在篡改区域与外观高度融合时失效的问题。

### 研究问题
当篡改区域在2D外观上与周围环境高度一致时，传统基于低层伪影、噪声痕迹、语义不一致等2D取证线索的图像篡改定位方法判别能力下降，需要引入几何推理来提供互补证据。

### 核心思路/方法
1. 利用单目重建提取辅助几何线索：深度图和表面法向图。
2. 考虑到被篡改图像中重建的几何信息天然带有噪声，直接作为证据不可靠，因此先估计这些几何线索的可靠性，再选择性使用。
3. 设计一个几何感知框架GFrame，将可靠的几何线索与RGB特征融合，并进行跨尺度传播以改善细粒度定位。

### 主要贡献
1. 指出纯2D线索在篡改区域外观融合良好时的局限，并引入可靠3D几何线索作为互补取证证据。
2. 提出GFrame框架，通过估计并选择性利用深度和表面法向的可靠性，实现更鲁棒的篡改定位。
3. 在有限预算下实现优秀性能，并计划公开代码。

### 局限性
摘要未提供足够信息，无法确认方法在复杂场景、计算成本、不同篡改类型上的具体表现或失败模式。

### 阅读优先级
中
理由：该方法属于图像取证领域的实用创新，思路明确（引入3D几何推理），但摘要未给出详尽的实验对比或代码开源时间，建议在需要解决2D线索失败场景时再深入阅读。

</details>

<details>
<summary>Abstract</summary>

Existing image manipulation localization (IML) methods rely heavily on 2D forensic cues, such as low-level artifacts, noise traces, and semantic inconsistencies in the manipulated image. While effective in many cases, these cues become much less discriminative when manipulated regions are well blended with their surrounding context in appearance. In such cases, a manipulated region may remain locally appearance-consistent, but still violate the geometric structure of the surrounding scene. This limitation motivates us to go beyond purely 2D evidence and introduce geometric reasoning into IML. To this end, we leverage monocular reconstruction to obtain auxiliary geometric cues, including depth and surface normals. However, a key challenge lies in the fact that reconstructed geometry on manipulated images is inherently noisy and cannot be used naively. Rather than treating depth and normals as direct evidence, we estimate their reliability and exploit them selectively for localization. Based on this principle, we design a geometry-aware framework (GFrame) that fuses reliable geometric cues with RGB features and propagates them across scales to improve fine-grained localization. Extensive experiments show that the proposed method achieves excellent performance under limited budget constraints. These results indicate that reliable 3D geometry provides complementary forensic evidence beyond traditional 2D cues for IML. Related code will be released.

</details>

#### 2026-07-20 - Lifelong Localization in Dynamic Indoor Environments Combining Odometry with Sparse Distance Sampling

**Authors:** Michael M. Bilevich, Tomer Buber, Dan Halperin
**Links:** [abs](https://arxiv.org/abs/2607.17852) - [pdf](https://arxiv.org/pdf/2607.17852)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, rendering, robot navigation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lifelong Localization in Dynamic Indoor Environments Combining Odometry with Sparse Distance Sampling
- 作者：Michael M. Bilevich, Tomer Buber, Dan Halperin
- 出版日期：2026-07-20T11:46:57Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.17852

### 一句话总结
论文提出了一种结合里程计与稀疏距离采样的鲁棒终身定位框架，可在动态室内环境中实现高效、可证明收敛的机器人定位，仅需少量距离样本即可达到类似SLAM的定位效果。

### 研究问题
如何在动态室内环境中实现机器人终身鲁棒定位，尤其是在预建地图因动态障碍物变得不准确，以及机器人可能被“绑架”（kidnapped robot problem）的情况下。

### 核心思路/方法
1. **稀疏距离采样提供鲁棒先验**：利用机器人获取的稀疏距离样本（如仅16个距离值）作为初始位置先验，可实时解决机器人绑架问题（存在对称性歧义时除外）。
2. **融合里程计与先验**：随时间将距离采样提供的先验与里程计数据融合，逐步收敛到机器人真实位姿。
3. **应对动态障碍**：基于真实世界记录数据的洞察，设计方法处理动态障碍物对定位的影响。
4. **理论基础**：证明在静态环境中方法可确保收敛到真实位姿；在动态环境中，若变化规律被正确学习，同样可保证收敛。

### 主要贡献
1. 提出一种终身定位框架，仅需稀疏距离采样（而非完整LiDAR范围），在传感器成本、隐私、存储和传输带宽方面具有优势。
2. 方法可实时解决机器人绑架问题，并在动态环境中保持鲁棒性。
3. 通过理论证明和真实世界实验验证，该方法在静态和动态环境中均能收敛到真实位姿，定位效果与SLAM相当。

### 局限性
摘要未提供具体局限性信息，但可推断：
- 动态环境中的收敛保证依赖于“变化规律被正确学习”，即需要准确建模动态障碍物的行为模式，这在实际应用中可能存在挑战。
- 绑架问题仅能“up to symmetries”（即对称性歧义可能无法完全消除），摘要未明确说明如何解决对称性场景。
- 实验仅在特定真实室内环境中验证，未提及跨场景泛化性。

### 阅读优先级
**高**
理由：该工作提出了新颖的稀疏距离采样定位方法，兼具理论收敛保证和实际应用优势（低传感器成本、隐私友好），且解决了动态环境下的终身定位难题，对机器人领域研究人员具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Localization is a key task in robot navigation, and many techniques exist for it. In many plausible scenarios, a robot might face unforeseen, dynamic obstacles, rendering any pre-determined map inaccurate for localization. In this work, we propose a robust lifelong localization framework in dynamic planar indoor environments, using the robot's odometry and sparse distance sampling. We demonstrate how distance samples can be used to provide a robust prior on the robot's location. This technique can solve the kidnapped robot problem in real time, up to symmetries. Based on insights from real-world recorded data, we also account for dynamic obstacles. We then fuse this prior, over time, with the odometry to converge to the robot's location. A central property of our method is that it provably converges to the robot's ground truth pose even in large indoor environments when the environment is static. We further show that this guarantee also holds in dynamic environments, as long as the nature of those changes has been correctly learned. We demonstrate the effectiveness of our approach in different real-world indoor environments. In particular, we achieve a localization comparable to SLAM with merely a few (sixteen) distance samples, as opposed to the full LiDAR range. Sufficing with only sparse distance sampling is advantageous in terms of sensor cost, privacy, storage space, and transmission bandwidth.

</details>

#### 2026-07-20 - Attention from Above: A Multimodal Model for Drone-Based Object Localization

**Authors:** Hyun-Ki Jung
**Links:** [abs](https://arxiv.org/abs/2607.17669) - [pdf](https://arxiv.org/pdf/2607.17669)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Attention from Above: A Multimodal Model for Drone-Based Object Localization（来自上方的注意力：面向无人机目标定位的多模态模型）
- 作者：Hyun-Ki Jung
- 出版日期：2026-07-20
- 分类：Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：论文摘要链接: https://arxiv.org/abs/2607.17669 ；PDF链接: https://arxiv.org/pdf/2607.17669

### 一句话总结
本文基于YOLO-World框架，通过引入注意力机制的A2C2f层替换原有C2f层，提出了一种改进的多模态无人机目标检测模型，在VisDrone数据集上显著提升了检测精度，尤其是对小目标的检测性能。

### 研究问题
如何改进基于多模态（文本提示+视觉）的无人机目标检测模型，以提升对小目标或边界清晰目标的检测准确性。

### 核心思路/方法
1. **基础框架**：采用YOLO-World作为基线多模态检测模型。
2. **关键改进**：将YOLOv8骨干网络中的C2f层替换为基于注意力机制的A2C2f层。
3. **设计目标**：通过注意力机制和并行处理结构，增强模型对局部特征的表示能力，特别针对小目标或具有清晰边界的对象。
4. **验证实验**：在VisDrone数据集上进行对比实验，与原始YOLO-World模型比较。

### 主要贡献
1. 提出了一种基于注意力机制的新型模块A2C2f，有效提升了多模态检测模型对局部特征的捕捉能力。
2. 在VisDrone数据集上验证了所提模型的有效性：相比原始YOLO-World，检测精度（precision）从43.0%提升至45.1%，召回率（recall）从32.8%升至35.0%，F1分数从37.2%升至39.4%，mAP@0.5从32.5%升至35.2%，mAP@0.5-0.95从18.5%升至19.9%。
3. 为基于无人机的图像和视频目标检测应用提供了一种更精确的解决方案。

### 局限性
摘要未提供足够信息。具体局限性（如模型的计算成本、推理速度、对复杂场景的泛化能力、多模态融合的失败案例等）未在摘要中说明。

### 阅读优先级
**高**
理由：该论文针对无人机场景下小目标检测这一实际且具有挑战性的问题，在近期主流模型YOLO-World基础上进行了明确的可量化改进（所有评估指标均有提升），且实验基于公开数据集VisDrone。方向契合无人机、机器人和多模态应用领域，对于关注轻量化或嵌入式检测的研究者具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Drone-based object detection technology has advanced rapidly, becoming increasingly sophisticated and efficient. Recently, research trends have expanded beyond the detection of predefined objects toward the identification of specified target objects. For example, desired targets can be specified through textual prompts, enabling accurate detection of objects of interest. To address this demand, this paper proposes an efficient multimodal-based object detection model aimed at improving small object detection performance. The proposed method is built upon the YOLO-World framework and replaces the C2f layers used in the YOLOv8 backbone with attention-based A2C2f layers. This modification enables more precise representation of local features, particularly for small objects or objects with well-defined boundaries. In addition, the incorporation of attention mechanisms and parallel processing structures significantly enhances the model's computational accuracy. Comparative experiments conducted on the VisDrone dataset demonstrate that the proposed model outperforms the original YOLO-World model. Specifically, precision increases from 43.0% to 45.1%, recall from 32.8% to 35.0%, the F1 score from 37.2% to 39.4%, mAP@0.5 from 32.5% to 35.2%, and mAP@0.5-0.95 from 18.5% to 19.9%, confirming a substantial improvement in detection accuracy. These results verify that the proposed approach provides an effective and highly accurate solution for object detection in drone-based image and video application environments.

</details>

#### 2026-07-20 - GeoWorldAD: Geometry World Action Model for Autonomous Driving

**Authors:** Songyan Zhang, Jinyuan Tian, Hanbing Li, Daqi Liu, Hao Chen, Wenhui Huang, Fang Li, Guang Chen, Hangjun Ye, Long Chen, Kuiyuan Yang, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2607.17521) - [pdf](https://arxiv.org/pdf/2607.17521)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** dynamic 3D, autonomous driving, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoWorldAD: Geometry World Action Model for Autonomous Driving  
- 作者：Songyan Zhang, Jinyuan Tian, Hanbing Li, Daqi Liu, Hao Chen, Wenhui Huang, Fang Li, Guang Chen, Hangjun Ye, Long Chen, Kuiyuan Yang, Chen Lv  
- 出版日期：2026-07-20T03:56:07Z  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.17521  

### 一句话总结
GeoWorldAD提出了一种基于几何世界建模的自动驾驶动作模型，通过引入自车对齐的3D几何线索和潜在未来几何令牌，实现更安全、更高效的轨迹规划。

### 研究问题
自动驾驶在动态3D环境中需要兼顾安全与效率的规划决策。现有视觉/视频动作模型往往缺乏显式的几何基础和未来感知的空间引导，难以在避免碰撞与保持行驶进度之间取得平衡。

### 核心思路/方法
- **显式几何锚定**：将轨迹规划嵌入到自车对齐的3D空间中，利用当前几何信息提供空间约束。  
- **潜在未来几何建模**：通过隐式未来几何令牌预测短时场景演化，包括周围代理和自车自由空间的变化，以减少过于保守的决策。  
- **渐进式轨迹优化**：利用多尺度的当前几何和潜在未来几何，通过迭代细化逐步优化轨迹。

### 主要贡献
- 提出了GeoWorldAD框架，将显式3D几何基础与未来几何世界建模相结合。  
- 在NAVSIM v1和v2基准上取得了最先进的性能，验证了该方法对安全与效率的平衡效果。  
- 强调了利用几何线索（当前与未来）对于自动驾驶规划的重要性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：论文提出了一种新颖的几何世界动作模型，在自动驾驶规划中同时考虑当前与未来几何线索，并在标准基准上取得领先性能，对安全性提升和决策保守问题具有明确贡献。尽管实验细节有限，其方法思路对相关领域研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous driving requires both safe and efficient planning decisions in dynamic 3D environments. Although recent Vision/Video-Action models learn policies directly from visual observations and scale well with advances in vision transformers and large-scale training data, they often lack explicit geometric grounding and future-aware spatial guidance, limiting their ability to balance collision avoidance and driving progress. In this work, we propose GeoWorldAD, a geometry world action model that grounds trajectory planning in ego-aligned 3D space and anticipates short-horizon scene evolution with latent future geometry tokens. Present geometry provides essential spatial constraints for safe planning, while future geometry reveals how surrounding agents and ego-centric free space may evolve, reducing overly conservative decisions without sacrificing safety. To efficiently exploit these geometric cues, GeoWorldAD progressively aggregates multi-scale present geometry and latent future geometry through iterative trajectory refinement. Experiments on NAVSIM v1 and v2 demonstrate state-of-the-art performance, highlighting the effectiveness of explicit 3D geometry grounding and future geometry world modeling for safe and efficient autonomous driving.

</details>

#### 2026-07-18 - A BIM-enabled, Agent-based Discrete-event Simulation Platform for Robotic Studies: A Method based on Graph Theory

**Authors:** Ping Xu, Xinghua Gao
**Links:** [abs](https://arxiv.org/abs/2607.16920) - [pdf](https://arxiv.org/pdf/2607.16920)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** simultaneous localization and mapping, SLAM, robot navigation, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A BIM-enabled, Agent-based Discrete-event Simulation Platform for Robotic Studies: A Method based on Graph Theory
- 作者：Ping Xu, Xinghua Gao
- 出版日期：2026-07-18
- 分类：Embodied / Robotics / AR Applications；3D Reconstruction & Multi-view Geometry
- 链接：摘要：https://arxiv.org/abs/2607.16920；PDF：https://arxiv.org/pdf/2607.16920

### 一句话总结
该研究提出一个基于BIM、基于图论的智能体离散事件仿真平台，用于支持室内机器人进行知识驱动的导航与操作规划，通过将环境离散化为网格并映射为图节点，利用图论算法实现高效无碰撞导航。

### 研究问题
如何利用建筑信息模型（BIM）的丰富语义和几何信息，弥补现有导航方法对室内环境理解不足的问题，从而实现室内机器人在复杂设施管理任务（如定位和维修泄漏管道）中的知识驱动导航与操作规划。

### 核心思路/方法
1. 将室内环境离散化为网格单元，并将这些单元映射为图节点。
2. 根据与建筑元素的空间关系，将节点分类为目标节点、障碍节点或常规节点。
3. 为连接相邻节点的边分配遍历成本，使图论算法能够计算高效且无碰撞的导航路径。
4. 采用基于智能体的离散事件仿真框架，集成BIM信息，支持虚拟评估。

### 主要贡献
- 提出一种BIM赋能的、基于图论的室内机器人仿真平台，将BIM信息与机器人导航和操作规划结合。
- 通过网格离散化和图节点分类方法，实现了高效且无碰撞的导航。
- 识别并缓解了粗糙离散化造成的目标占用单元与障碍占用单元重叠的问题，通过网格细化提高了空间精度和路径可行性。
- 支持在部署前对机器人操作进行虚拟评估，为BIM赋能的设施管理机器人系统奠定基础。

### 局限性
- 摘要指出关键局限：粗糙离散化会导致目标占用单元与障碍占用单元重叠问题，虽通过网格细化缓解，但该处理可能带来计算或精度上的折中，摘要未提供具体权衡细节。
- 摘要未提供场景规模、计算效率、实验对比等具体信息。

### 阅读优先级
中。理由：该研究针对室内机器人复杂任务场景，提出BIM与图论结合的方法，思路清晰且有仿真验证，对建筑机器人应用有一定参考价值。但摘要未提供详细实验数据和性能指标，且方法本身的创新性（网格+图）较为常规，需阅读全文评估实际效果和局限性。

</details>

<details>
<summary>Abstract</summary>

Indoor robots are increasingly employed for facility management tasks such as cleaning and inspection. These applications primarily rely on navigation and can be effectively supported by predefined routes or perception-driven Simultaneous Localization and Mapping (SLAM) techniques. However, more complex tasks, such as locating and repairing leaking pipes, require not only navigation but also access to building information, including the location, geometry, material, and operational attributes of components. Existing navigation approaches provide only limited environmental understanding and cannot readily supply such information. In contrast, Building Information Modeling (BIM) contains rich geometric, semantic, and operational information that remains largely underutilized in robotic applications. This study proposes a BIM-enabled, agent-based simulation platform for knowledge-driven indoor robot navigation and operation planning. Within the framework, indoor environments are discretized into grid cells that are mapped to graph nodes and classified as target, obstacle, or regular nodes according to their spatial relationships with building elements. Traversal costs are assigned to edges connecting neighboring nodes, enabling graph-theoretic algorithms to compute efficient and collision-free navigation paths while avoiding obstacles. Simulation results demonstrate that the proposed graph representation enables efficient and collision-free navigation. A key limitation associated with coarse discretization, namely overlap between target-occupied and obstacle-occupied cells, is identified and mitigated through grid refinement, improving spatial accuracy and path feasibility. The proposed platform supports virtual evaluation of robotic operations prior to deployment and provides a foundation for BIM-informed robotic systems in facility management.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
