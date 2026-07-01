# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：66
- 分类分布：
  - Neural Scene Representations & Rendering: 24
  - 3D Reconstruction & Multi-view Geometry: 17
  - Embodied / Robotics / AR Applications: 16
  - Dynamic / 4D Reconstruction: 6
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的中文科研趋势综合分析。

---

#### 今日主要趋势

1.  **3D高斯泼溅 (3DGS) 进入“万物皆可3DGS”的泛化与实用化阶段。** 3DGS已不再局限于新颖视角合成，而是作为核心表示范式渗透到多个下游任务中。这包括：**稀疏视图重建** (StereoGS, 2606.30545) 通过引入立体先验解决几何过拟合问题；**大规模SLAM** (KiloGS-SLAM, 2606.30436) 将其扩展至千米级室外场景并解决内存和跟踪鲁棒性瓶颈；**前馈重建** (FastPano3D, 2606.30352; FFAvatar, 2606.30347）从单张或稀疏图像直接生成3DGS表示，追求极致的速度；以及**移动端部署** (Flux-GS, 2606.30017) 通过量化、能量聚合等手段降低计算和存储开销。此外，3DGS的**隐写** (IBRSteG, 2606.30024)、**具身导航** (VLK, 2606.30645) 和**城市仿真** (Shell-Supervised GS, 2606.30014) 等新颖应用也纷纷涌现，标志着3DGS正从一个基础渲染工具演变为一个通用的3D场景表示与处理平台。

2.  **从“静态”到“动态”与“可交互”：4D重建和具身智能成为核心驱动力。** 论文列表清晰地展示了研究方向从静态场景重建向动态4D重建和具身交互场景的转变。这体现在：**4D头部化身** (FFAvatar, 2606.30347)、**4D手部运动** (ViDiHand, 2606.30308) 和**单目视频4D重建** (Flow Splatting, 2606.29976) 追求的不仅是3D几何，更是随时间变化的动态属性。**人形机器人操作** (VLK, 2606.30645) 和**关节物体重建** (UnfoldArt, 2606.30608) 则直接面向具身AI场景，要求场景表示不仅要“好看”，更要能“推理”和“交互”，例如理解物体关节、进行物理交互。这种趋势将3D/4D重建技术与机器人、虚拟现实和增强现实等领域紧密绑定。

3.  **“合成数据”与“基础模型先验”成为突破数据稀缺瓶颈的关键路径。** 许多工作都致力于摆脱对大规模、高质量、带标注的真实世界数据的依赖。**合成数据**被用于训练人形机器人 (VLK, 2606.30645) 和全景3D重建 (Argus, 2606.30047)。另一方面，**预训练基础模型**的知识被大量迁移：视频扩散模型被用于4D手部重建 (ViDiHand, 2606.30308)；视觉语言模型 (VLM) 和视频模型被用于推理物体关节 (UnfoldArt, 2606.30608)；立体匹配基础模型被用于提供几何先验 (StereoGS, 2606.30545)；2D开放词汇检测器被用于驱动3D场景理解 (GaussDet, 2606.30638)。这些工作表明，利用合成数据或在预训练的大模型上进行微调/知识蒸馏，是当前克服特定任务标注困难、提升模型泛化能力的有效范式。

#### 技术路线观察

- **几何基础模型与3D重建：** 该方向侧重于解决几何重建的鲁棒性和精度问题。**SLAM**相关论文 (KiloGS-SLAM, TACO) 关注大规模、长轨迹下的位姿估计和异常值剔除。**稀疏视角重建** (StereoGS) 致力于引入更强的几何先验（立体匹配）来约束过拟合。**类别级位姿估计** (Shared Canonical Frame) 则探索自监督方式学习物体规范坐标系。这个方向的技术特点是强调**几何一致性**、**鲁棒性**和**可扩展性**，通常需要有扎实的几何基础和优化理论。

- **3D/4D重建与神经场景表示：** 3DGS是绝对的主流，几乎所有该方向的论文都围绕3DGS展开。技术路线可细分为：1）**前馈方法** (FastPano3D, FFAvatar, RenderFormer++)，追求从输入到输出的“一步到位”，速度快但泛化能力受限于训练数据；2）**优化方法** (StereoGS, KiloGS-SLAM, Flux-GS)，对单个场景进行优化，效果好但计算成本高，因此研究点在于如何通过先验知识 (立体、运动、能量分布) 来加速和改进优化过程；3）**动态场景表示** (Flow Splatting, ViDiHand)，通过在3DGS基础上增加时间维度或借助基础模型来建模运动。该方向的核心在于**平衡质量、速度、内存和泛化能力**之间的trade-off。

- **机器人/AR应用：** 该方向的论文更关注“端到端”的任务解决能力。**人形机器人操作** (VLK) 将3DGS重建、语言理解和运动规划串联成一个闭环。**关节物体重建** (UnfoldArt) 为机器人操作提供了先验知识。**容器化系统架构** (CSAR) 则是一个更底层的系统工程方案，旨在优化机器人软件的部署和计算资源管理。这些应用驱动的论文，其技术路线往往**模块化**和**灵活性**较强，旨在解决实际部署中的特定瓶颈。

#### 值得优先阅读的论文

1.  **ViDiHand (2606.30308) - 视频扩散模型用于4D手部运动重建**
    - **理由：** 该工作展示了利用预训练基础模型（特别是生成式模型）解决传统方法难以克服的瓶颈（如严重遮挡下的手部重建）的巨大潜力。其“利用扩散模型隐式习得的运动先验”的思路非常新颖，且效果提升显著（在多个基准上大幅超越SOTA），代表了利用生成式AI为感知任务提供强先验的前沿方向。

2.  **KiloGS-SLAM (2606.30436) - 千米级室外场景的单目3D高斯SLAM**
    - **理由：** 这是将3DGS SLAM推向极致规模的代表作，直面了在实际大规模应用（如自动驾驶、无人机测绘）中的两大核心难题：长时跟踪漂移和内存爆炸。其提出的“运动自适应混合跟踪”和“生命周期管理建图”策略具有很强的启发性，对于从事SLAM、3DGS或大规模3D重建的研究者都是必读文章。

3.  **UnfoldArt (2606.30608) - 零样本关节3D物体重建**
    - **理由：** 该工作创新性地运用了多智能体辩论机制来驱动零样本关节物体重建，体现了复杂场景中引入高层次推理能力（从VLM和视频模型中获取）的新趋势。对于想了解如何将大语言模型/多模态模型与3D视觉任务结合的研究者，这是一个极具启发性的案例。

4.  **StereoGS (2606.30545) - 基于立体先验的稀疏视角3DGS**
    - **理由：** 这项工作对3DGS的一个核心痛点——稀疏视图下的过拟合问题——给出了一个优雅且有效的解法。相比于依赖单目深度先验的传统方法，其引入的立体先验天然地具有绝对尺度和跨视图一致性，思想直接且有力。对于想要改进3DGS基础性能的研究者，这篇论文是强相关参考资料。

5.  **FFAvatar (2606.30347) - 前馈式4D头部化身重建**
    - **理由：** 在数字人领域，该方法实现了从稀疏图片到可驱动4D化身前馈式生成，且支持增量输入和身份-表情解耦。其“稀疏到稠密”的学习范式和运动细化模块设计精巧，兼顾了效率和个性化。对于关注数字人、虚拟现实和神经渲染的研究者，这是一篇高质量的前沿工作。

#### 可能的研究机会

1.  **“场景/物体理解”与“机器人/AR操作”的更深层次融合：** 目前多数工作要么

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-01T11:11:42-04:00
**Total number of papers:** 74
**Number of papers added in the latest update:** 21
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

### 2026-06

#### 2026-06-30 - AnyMatch: Supercharging Universal Multi-Modal Image Matching with Large-Scale Single-View Images

**Authors:** Meng Yang, Zizhuo Li, Linfeng Tang, Fan Fan, Jiayi Ma
**Links:** [abs](https://arxiv.org/abs/2606.31077) - [pdf](https://arxiv.org/pdf/2606.31077)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** image matching, MVS, SfM, depth estimation, monocular depth, localization

<details>
<summary>Abstract</summary>

Multi-modal image matching is essential for visual localization and multi-sensor fusion, but it is hindered by the scarcity of large-scale training data with precise geometric annotations. Existing real-world datasets suffer from prohibitive costs, limited scene diversity, and errors in SfM-MVS pipelines, while synthetic methods struggle to maintain 3D geometric consistency or achieve photorealistic appearance. To address this, we propose AnyMatch, a novel framework that leverages abundant, easily accessible single-view images at minimal cost to generate rich multi-modal training data. AnyMatch integrates monocular depth estimation, 3D reprojection, diffusion-based inpainting, and crossmodal image translation to synthesize multi-view, multi-modal image pairs with 3D geometric fidelity. Crucially, our method provides annotations that strictly adhere to 3D geometric consistency through explicit 3D reprojection, avoiding SfM-MVS error accumulation. Furthermore, AnyMatch offers strong scalability, enabling controllable scene diversity and annotation difficulty via adjustable input and camera parameters. We construct Any-syn, a large-scale synthetic multi-modal dataset using AnyMatch. Experimental results show that matching networks (e.g., LoFTR, EDM, RoMa) fine-tuned on Any-syn achieve substantial performance gains on multi-modal benchmarks, exhibiting superior generalization and robustness compared to models trained on existing data.

</details>

#### 2026-06-29 - AerialMetric: Benchmarking and Adapting UAV Monocular Metric Depth Estimation in the Real World

**Authors:** Zhongqiang Song, Guanying Chen, Yuqi Zhang, Yin Zou, Chuanyu Fu, Zhiyuan Yuan, Chuan Huang, Shuguang Cui, Xiaochun Cao
**Links:** [abs](https://arxiv.org/abs/2606.29716) - [pdf](https://arxiv.org/pdf/2606.29716)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** depth prediction, metric depth, depth estimation, photogrammetry

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AerialMetric: Benchmarking and Adapting UAV Monocular Metric Depth Estimation in the Real World
- 作者：Zhongqiang Song, Guanying Chen, Yuqi Zhang, Yin Zou, Chuanyu Fu, Zhiyuan Yuan, Chuan Huang, Shuguang Cui, Xiaochun Cao
- 出版日期：2026-06-29
- 分类：Geometry Foundation Models（主要），3D Reconstruction & Multi-view Geometry（次要）
- 链接：[摘要](https://arxiv.org/abs/2606.29716) | [PDF](https://arxiv.org/pdf/2606.29716)

### 一句话总结
本文为解决无人机航拍图像中单目度量深度估计的域偏移问题，构建了包含52K真实与16K合成图像-深度对的AerialMetric基准数据集，并基于此对现有模型进行评估与微调，实现了航拍场景下最先进的性能。

### 研究问题
无人机航拍图像中单目度量深度估计面临显著的领域鸿沟：现有数据驱动的方法主要基于街景和室内数据集训练，在航拍视角下性能严重下降。因此，核心问题是如何评估、并让模型适应无人机视角下的度量深度预测。

### 核心思路/方法
1.  **构建基准数据集AerialMetric**：从四个互补来源收集并标注数据——真实世界摄影测量数据、受控航拍采集数据、逼真合成场景以及网络图像。总计提供52K真实图像-深度对和16K合成图像-深度对，均带有可靠的度量真值。
2.  **系统评估**：在AerialMetric上对现有最先进的单目深度估计模型进行系统性评估，分析视角、高度和相机参数对度量深度预测的影响。
3.  **领域适应微调**：在AerialMetric数据集上对代表性度量深度模型进行微调，从而建立航拍视角下的基准，并实现最优性能。

### 主要贡献
- 提出了AerialMetric基准数据集，包含68K（52K真实+16K合成）航拍图像-深度对，且全部带有可靠的度量真值，用于评估和适应单目度量深度估计。
- 对现有最先进模型进行了航拍场景下的系统性评估，揭示了视角等因素对预测的影响。
- 通过在该数据集上微调，实现了在多样航拍图像上的最先进性能，并公开了数据集、代码和模型权重。

### 局限性
摘要未提供足够信息来指出该研究的具体局限性（例如模型在极端天气、动态场景下的表现，或数据集覆盖场景的边界等）。

### 阅读优先级
**高**
理由：该论文针对无人机航拍这一特定且重要的应用场景，解决了数据匮乏和领域迁移的瓶颈问题。它既提供了高价值的公开基准数据集（AerialMetric），又展示了系统评估和迁移适应的范式，对从事几何基础模型、三维重建及无人机视觉的研究人员具有直接的参考价值。

</details>

<details>
<summary>Abstract</summary>

This paper addresses the problem of monocular metric depth estimation in aerial UAV imagery. Although recent data-driven methods have achieved remarkable progress in ground-level scenarios, models trained primarily on street-view and indoor datasets exhibit significant domain gaps when applied to aerial viewpoints. To tackle these challenges, we introduce AerialMetric, a benchmark dataset designed to evaluate and facilitate the adaptation of monocular metric depth estimation under UAV aerial viewpoints. The dataset consists of four complementary subsets collected from different sources, jointly covering real-world photogrammetry data, controlled aerial acquisition settings, photorealistic synthetic scenes, and in-the-wild Internet imagery. Totally, AerialMetric provides 52K real-world and 16K synthetic image-depth pairs with reliable metric ground truth. Based on this dataset, we conduct systematic evaluations of existing state-of-the-art models under aerial settings and investigate the impact of viewpoint, altitude, and camera parameters on metric depth prediction. In addition, by fine-tuning representative metric depth model on our dataset, we establish a comprehensive aerial benchmark and achieve state-of-the-art performance across diverse aerial imagery. Our dataset, code, and model weight are publicly available at https://kuieless.github.io/AerialMetric-ECCV2026-page/.

</details>

#### 2026-06-28 - Multi-scale Object-Aware Gaze Estimation via Geometric Reasoning

**Authors:** Jiajie Mi, Xinyu Liu, Mengke Song, Chenglizhao Chen
**Links:** [abs](https://arxiv.org/abs/2606.29334) - [pdf](https://arxiv.org/pdf/2606.29334)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** geometric reasoning, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-scale Object-Aware Gaze Estimation via Geometric Reasoning
- 作者：Jiajie Mi, Xinyu Liu, Mengke Song, Chenglizhao Chen
- 出版日期：2026-06-28
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2606.29334

### 一句话总结
本文提出一种基于对象语义的两阶段注视估计框架，通过引入物体级表示、多尺度特征融合以及几何约束，将注视目标估计从像素级回归转化为层次化推理问题，在多个基准上取得了优异性能。

### 研究问题
现有注视目标估计方法通常将任务建模为从全局特征到注视热图的直接映射（像素级回归），未能显式地将注视对象作为独立实体表示，导致在复杂场景中预测不稳定且语义不一致。本文旨在解决如何明确建模注视对象并实现稳定、语义一致的预测。

### 核心思路/方法
1. **两阶段框架**：将注视目标估计重构为层次化推理过程。
2. **物体级表示**：在特征编码阶段融入物体级表征，使图像特征与离散语义实体对齐。
3. **多尺度特征融合与几何约束**：利用头部姿态和视线方向的几何信息，进行细粒度定位和物体级区分。
4. **模型设计**：保持紧凑的参数规模（7.1M），通过多尺度融合提升对不同大小目标的适应能力。

### 主要贡献
- 提出一种对象感知的两阶段注视估计框架，将任务转化为层次化推理，而非直接像素级回归。
- 集成物体级表示、多尺度特征融合和几何推理，增强了模型对注视对象的语义理解和定位能力。
- 在GazeFollow、VideoAttentionTarget、ChildPlay和GOO-Real四个基准上达到高AUC（分别为0.961、0.948、0.987、0.977），且参数量仅为7.1M。

### 局限性
摘要未提供足够信息，无法判断方法的具体局限性，例如对遮挡、多人场景或计算效率的潜在限制。

### 阅读优先级
**高**。理由：本文提出的方法在多个标准基准上取得了优异性能（AUC均超过0.94），且模型参数量小（7.1M），兼顾了性能与效率。该研究重新定义了注视目标估计的范式，具有创新性和实用性，适合视觉与几何推理领域的学者阅读。

</details>

<details>
<summary>Abstract</summary>

Gaze target estimation aims to predict the semantic object an observer fixates upon within an image, a task deeply rooted in the object-oriented nature of human gaze. Observers tend to select a specific semantic entity as the attentional target, rather than responding randomly across arbitrary regions of the image. However, existing methods typically model this task as a direct mapping from global features to gaze heatmaps, essentially treating it as a pixel-level regression problem. This approach fails to explicitly represent the gazed object as a distinct entity, making it difficult to produce stable and semantically consistent predictions in complex scenes. To address this, we propose a two-stage gaze estimation framework guided by object semantics, reformulating gaze target estimation as a hierarchical reasoning process. Our method incorporates object-level representations during feature encoding to align image features with discrete semantic entities, then introduces multi-scale feature fusion and geometric constraints from head pose and gaze direction for fine-grained localization and object-level discrimination. Extensive experiments on GazeFollow, VideoAttentionTarget, ChildPlay, and GOO-Real demonstrate that our method achieves AUC of 0.961, 0.948, 0.987, and 0.977 respectively, delivering strong performance across all benchmarks while maintaining a compact parameter size of 7.1M.

</details>

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-30 - One Video, One World: Turning Monocular Video into Physical 4D Scenes

**Authors:** Junhao Chen, Boran Zhang, Mingjin Chen, Henghaofan Zhang, Saining Zhang, Congcong Zhu, Hao Zhao, Ruqi Huang, Zhihao Li, Yufei Wang
**Links:** [abs](https://arxiv.org/abs/2606.31388) - [pdf](https://arxiv.org/pdf/2606.31388)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, video-to-4D, rendering, embodied AI, simulation

<details>
<summary>Abstract</summary>

We introduce \textbf{OVOW}, the first training-free system that reconstructs \emph{instance-level, simulation-ready} 4D mesh scenes from a single monocular video. Recent 4D reconstruction achieves impressive rendering quality, but its outputs (\eg, implicit fields, Gaussian primitives, or point clouds) lack the watertight topology, instance separation, and standardized physical interfaces required by physics simulators and embodied AI. OVOW closes this gap with a four-stage pipeline: a vision-language model discovers, labels, and motion-classifies all instances; category-aware reconstruction yields per-instance meshes for rigid objects and topology-consistent mesh sequences for deformable ones; an iterative render-match-optimize procedure recovers metric scale and 6-DoF pose trajectories; and physics-grounded assembly enforces ground contact and inter-object support. Crucially, we model all motion, rigid and non-rigid, through direct vertex deformation without category-specific priors or skeleton rigging, producing watertight mesh scenes ready for downstream physics simulation and editing. We further establish the first benchmark for \emph{structured Video-to-4D} evaluation, with metrics for geometric correctness, instance separation, and physical plausibility beyond visual fidelity; the same pipeline doubles as a scalable engine for \emph{synthesizing} paired video-to-4D simulation data for future 4D world models and embodied AI. Across two synthetic benchmarks (static and 4D), OVOW attains the best overall layout and geometry accuracy and the lowest photometric and semantic error among all baselines, and on monocular video runs one to two orders of magnitude faster than the baselines, while downstream physics simulation confirms its physical stability.

</details>

#### 2026-06-30 - JacobianAvatar: Temporally Consistent Semi-rigid Avatar Reconstruction from a Monocular Video

**Authors:** Changyeon Won, Min-Gyu Park, Seonghwan Park, Ju Hong Yoon, Hae-Gon Jeon
**Links:** [abs](https://arxiv.org/abs/2606.31115) - [pdf](https://arxiv.org/pdf/2606.31115)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** avatar reconstruction

<details>
<summary>Abstract</summary>

Generating realistic human avatars in complex motions--such as clothing dynamics--requires modeling of global and local deformations which remains challenging in monocular settings. We address this problem by leveraging neural Jacobian fields (NJFs) for representing semi-rigid deformations. We train self-supervised neural networks for predicting Jacobian matrices that give the pose-dependent deformations, by solving a Poisson equation. However, monocular input presents several difficulties such as self-occluded regions and invisible surfaces. To address these issues, we introduce three key components: a constrained Poisson solver, signed distance-based Jacobian regularization, and a deformation-guided residual flow loss, which together suppress boundary artifacts, recover frequently occluded regions such as armpits and thighs, and enforce temporal consistency during motion. Experiments on benchmark and in-the-wild videos demonstrate that our method generates temporally stable and geometrically coherent avatars, outperforming state-of-the-art approaches.

</details>

#### 2026-06-29 - FFAvatar: Feed-Forward 4D Head Avatar Reconstruction from Sparse Portrait Images

**Authors:** Jianjiang Yao, Ke Xian, Renxiang Dai, Robert Caiming Qiu
**Links:** [abs](https://arxiv.org/abs/2606.30347) - [pdf](https://arxiv.org/pdf/2606.30347)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** avatar reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FFAvatar: Feed-Forward 4D Head Avatar Reconstruction from Sparse Portrait Images
- 作者：Jianjiang Yao, Ke Xian, Renxiang Dai, Robert Caiming Qiu
- 出版日期：2026-06-29
- 分类：动态/4D重建
- 链接：摘要：https://arxiv.org/abs/2606.30347；PDF：https://arxiv.org/pdf/2606.30347

### 一句话总结
提出一种基于Transformer和3D高斯方法的FFAvatar框架，能从一张或多张稀疏肖像图像前馈式地快速重建高质量、可驱动的4D头部化身，并支持增量式输入与身份表情解耦。

### 研究问题
如何从稀疏、可变数量的肖像图像中高效构建高保真、可动画化的4D头部化身，并实现跨表情和视角的身份一致性渲染。

### 核心思路/方法
1. 使用基于Transformer的3D高斯框架，通过交替注意力机制解耦身份外观与表情/视角变化，重建姿态和表情下一致的规范3D外观。
2. 提出从稀疏到密集的学习范式：先使用基于FLAME顶点位置的稀疏基元学习粗略外观特征，后在UV域中稠密化以捕获细节几何与纹理。
3. 设计即插即用的运动细化模块，对参数化变形之外的残差运动进行建模，实现主体特定的动态个性化。

### 主要贡献
1. 支持增量重建，可随着参考图像增加逐步精炼化身表示，无需固定输入视图数量。
2. 通过交替注意力机制在Transformer框架中有效解耦身份与表情/视角因素。
3. 提出稀疏到密集的学习策略，在计算效率与视觉保真度之间取得平衡。
4. 引入运动细化模块，实现超越参数化变形的动态个性定制。

### 局限性
摘要未提供足够信息：原文未提及任何实验限制、失败案例、数据依赖或失败模式分析。

### 阅读优先级
高  
理由：该论文针对4D头部化身重建这一热点领域，提出支持增量输入、身份表情解耦和运动细化的新颖框架，方法设计清晰且关键模块（如稀疏到密集学习、交替注意力）具有较强技术参考价值。

</details>

<details>
<summary>Abstract</summary>

We present FFAvatar, a Transformer-based 3D Gaussian framework for fast construction of high-quality and animatable 4D head avatars from one or more reference portrait images. Unlike existing feed-forward approaches that require a fixed number of input views, FFAvatar supports incremental reconstruction, progressively refining the avatar representation as additional reference images become available. At the core of our method is an alternating attention mechanism that disentangles identity appearance from expression and viewpoint variations, enabling the reconstruction of a canonical 3D appearance that remains consistent across poses and facial expressions. To balance visual fidelity and computational efficiency, we introduce a sparse-to-dense learning paradigm. Coarse appearance features are first learned using sparse primitives anchored to the FLAME vertex level and are subsequently densified in the UV domain to capture fine-grained geometric and texture details. We further propose a plug-and-play motion refinement module that enables subject-specific dynamic personalization by modeling residual motion beyond parametric deformation. Extensive experiments demonstrate that FFAvatar efficiently produces high-fidelity and controllable 4D head avatars, achieving superior flexibility, driving efficiency, and identity-consistent rendering across diverse expressions and viewpoints.

</details>

#### 2026-06-29 - The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction

**Authors:** Yuxi Wang, Chengkai Jin, Yufei Liu, Wenqi Ouyang, Tianyi Wei, Zhiwei Zeng, Siyuan Huang, Zhiqi Shen, Xingang Pan
**Links:** [abs](https://arxiv.org/abs/2606.30308) - [pdf](https://arxiv.org/pdf/2606.30308)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion reconstruction, rendering, embodied AI

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction
- 作者：Yuxi Wang, Chengkai Jin, Yufei Liu, Wenqi Ouyang, Tianyi Wei, Zhiwei Zeng, Siyuan Huang, Zhiqi Shen, Xingang Pan
- 出版日期：2026-06-29
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2606.30308

### 一句话总结
本文提出 ViDiHand，利用预训练视频扩散模型的特征进行4D双手姿态重建，无需检测器或测试时优化，在多个基准上显著优于现有方法。

### 研究问题
如何从第一人称视频中鲁棒地重建4D双手运动，克服现有方法在严重遮挡、运动动态建模及手物交互方面的局限性。

### 核心思路/方法
- 利用互联网规模训练的视频扩散模型隐式习得的运动动态、遮挡推理和手物交互能力。
- 通过手部覆盖渲染目标（hand-overlay rendering objective）微调预训练视频扩散模型，使其特征专注于手部同时保留世界先验。
- 使用解码器从调整后的特征恢复公制尺度的双手姿态。
- 整个流程直接处理全帧图像，不依赖检测器、填充器或测试时优化。

### 主要贡献
- 提出 ViDiHand 方法，首次将预训练视频扩散模型作为手部运动重建的强基础。
- 在 ARCTIC、HOT3D 和 HOI4D 数据集上显著超越之前的方法。
- 为可扩展的野外数据收集提供了一条有前景的路径。

### 局限性
摘要未提供足够信息；未提及模型计算成本、实时性能、泛化到未见场景的能力或失败案例。

### 阅读优先级
**高**
理由：本文提出了一种新颖且有效的方法，利用视频扩散模型解决4D手部重建这一具有挑战性的任务，并在多个标准基准上取得大幅性能提升，对计算机视觉和具身智能领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

4D hand motion reconstruction from egocentric video is bottlenecked by clear limitations of existing methods: image-based pipelines depend on a detector that fails under heavy occlusion, while video-based methods rely on temporal modules learned only from scarce hand-pose annotations, a narrow signal insufficient to model motion dynamics, occlusion reasoning, and hand-object interaction. These capabilities, however, are exactly what video generative models must implicitly acquire when trained to synthesize coherent video at internet scale. Motivated by this, we present ViDiHand, which leverages the representations of a pretrained video diffusion model to reconstruct 4D two-hand pose. We adapt it via a hand-overlay rendering objective that specializes its features for hands while preserving its world priors. A decoder then recovers metric-scale pose from the adapted features. The whole pipeline operates directly on full frames--no detector, no infiller, and no test-time optimization. On ARCTIC, HOT3D, and HOI4D, ViDiHand substantially outperforms prior methods, establishing video diffusion models as a powerful new foundation for hand motion reconstruction and a promising route to scalable in-the-wild data collection for embodied AI. Project page: https://vidihand.github.io.

</details>

#### 2026-06-29 - Learning Efficient 4D Gaussian Representations from Monocular Videos with Flow Splatting

**Authors:** Shengjun Zhang, Jinzhao Li, Xin Fei, Yueqi Duan
**Links:** [abs](https://arxiv.org/abs/2606.29976) - [pdf](https://arxiv.org/pdf/2606.29976)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, 4D Gaussian, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Efficient 4D Gaussian Representations from Monocular Videos with Flow Splatting
- 作者：Shengjun Zhang, Jinzhao Li, Xin Fei, Yueqi Duan
- 出版日期：2026-06-29
- 分类：主分类 – Dynamic / 4D Reconstruction；次分类 – Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2606.29976，PDF https://arxiv.org/pdf/2606.29976

### 一句话总结
本文提出Flow Splatting方法，通过构建速度场并扩展传统体渲染的splatting技术来渲染光流，从而从单目视频中高效学习动态4D高斯表示，在训练时间、渲染速度和内存消耗上优于现有方法。

### 研究问题
如何从单目视频中高效重建动态3D场景，克服现有4D表示方法训练时间过长、渲染速度慢或内存消耗高的缺陷，同时充分利用稠密的动态信息。

### 核心思路/方法
1. **4D高斯表示扩展**：使用时变均值和时间协方差扩展4D体积，表达复杂动态场景。
2. **速度场构建与近似**：基于上述4D表示自然构造并近似速度场。
3. **Flow Splatting技术**：将传统splatting技术用于从速度场渲染光流，并通过考虑相机运动的影响来监督单目视频下的动态学习过程。
4. **体积渲染策略扩展**：在已有颜色场渲染能力基础上，扩展至速度场的splatting渲染。

### 主要贡献
- 提出Flow Splatting方法，将速度场引入splatting技术，用于从单目视频监督动态学习。
- 使用时变均值和协方差扩展4D表示，构建速度场并实现高效渲染。
- 在多个基准上实现比现有方法更优的图像质量、更少的训练时间和更快的渲染速度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**
理由：该方法针对动态场景重建的效率和速度提出了明确改进，且实验结果优于现有方法，对关注实时性或资源受限的动态渲染任务的研究者有参考价值。但摘要未提及具体的数值对比、消融实验或失败案例，需要阅读全文以评估实际突破。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic 3D scenes from monocular videos is challenging due to scene complexity and temporal dynamics. With the advancement of 3D Gaussian Splatting in novel view synthesis, existing methods extend 3D Gaussians to 4D domain with deformation fields, trajectories or spatiotemporal 4D volumes to model scene element deformation. However, these methods suffer from long training time, low rendering speed or high memory consumption for per-frame reconstruction of 4D volumes, without fully exploiting dense dynamic information. To address this issue, we propose Flow Splatting, which constructs the velocity field and enables the conventional splatting technique to render optical flow from the velocity field to supervise dynamics learning process from monocular videos. Specifically, we extend 4D volumes with time varying means and covariance to represent complex dynamics. Then, we construct and approximate the velocity field naturally based on this representations. While conventional volume rendering techniques support to render color fields, we extend the volume rendering strategy to splat the velocity field by considering the influence of camera motions. We conduct experiments on various benchmarks to demonstrate the efficiency and effectiveness of our method. Compared to the state-of-the-art methods, our model achieves better image quality with less time consumption and higher rendering speed.

</details>

#### 2026-06-28 - L2D2-GS: Learning to Densify for Feedforward Dynamic Gaussian Scene Reconstruction

**Authors:** Zetian Song, Chenming Wu, Junnan Liu, Chitian Sun, Liangliang He, Hangjun Ye, Jiaqi Zhang, Siwei Ma, Wen Gao
**Links:** [abs](https://arxiv.org/abs/2606.29374) - [pdf](https://arxiv.org/pdf/2606.29374)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** generalizable reconstruction, dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：L2D2-GS: Learning to Densify for Feedforward Dynamic Gaussian Scene Reconstruction
- 作者：Zetian Song, Chenming Wu, Junnan Liu, Chitian Sun, Liangliang He, Hangjun Ye, Jiaqi Zhang, Siwei Ma, Wen Gao
- 出版日期：2026-06-28
- 分类：Dynamic / 4D Reconstruction；次要分类：3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2606.29374；PDF：https://arxiv.org/pdf/2606.29374

### 一句话总结
L2D2-GS提出一个框架，将通用动态场景重建转化为迭代优化与稠密化过程，通过自监督稠密化策略和几何正则化机制，在PandaSet与Waymo数据集上实现了媲美或更优的重建保真度与零样本泛化能力。

### 研究问题
解决现有动态场景重建方法中两类主要瓶颈：一是基于3D高斯溅射（3DGS）的每场景优化方法开销大、难以扩展；二是前馈式推理方法在高分辨率下内存消耗巨大，且难以从密集多视角观测中融合出一致表达。

### 核心思路/方法
- 将可泛化重建建模为**迭代优化与稠密化**过程，而非一次性回归。
- 提出**自监督稠密化策略**：从全局重建增益中提取显式奖励信号，指导局部点云（高斯基元）的稠密化决策。
- 引入**几何正则化机制**：通过重参数化约束优化流形，抑制早期阶段不可逆的伪影，避免陷入不良局部最优解。

### 主要贡献
- 提出统一的L2D2-GS框架，将前馈动态场景重建泛化为迭代优化与稠密化问题。
- 设计自监督稠密化策略，以全局重建收益驱动局部基元生成。
- 引入几何正则化技术，缓解早期训练阶段的伪影问题。
- 在PandaSet和Waymo数据集上实现SOTA重建精度，零样本泛化能力强，且使用比基线更少的高斯基元。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：论文聚焦于动态城市场景重建这一高需求领域，方法创新性突出（迭代稠密化+自监督），且在公开数据集上验证了显著性能提升与零样本泛化能力，对实时仿真、自动驾驶等应用具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

High-fidelity reconstruction of dynamic urban environments is a cornerstone of autonomous driving simulation and large-scale world modeling. While 3D Gaussian Splatting (3DGS) has established a new standard for real-time rendering, its reliance on expensive per-scene optimization limits scalability. Conversely, recent feedforward methods that infer Gaussian parameters offer faster speed but face fundamental bottlenecks: they are memory-prohibitive at high resolutions and struggle to fuse dense multi-view observations consistently. This paper presents L2D2-GS, a unified framework that reformulates generalizable reconstruction not as a one-shot regression, but as a robust iterative process of optimization and densification. To resolve the ambiguity of supervision in primitive generation, we propose a self-supervised densification policy that derives explicit reward signals from global reconstruction gains to guide local densification. Furthermore, we mitigate irreversible early-stage artifacts through a geometric regularization mechanism, utilizing reparameterization to constrain the optimization manifold and prevent convergence to poor local optima. Extensive experiments on the PandaSet and Waymo datasets demonstrate that our method achieves state-of-the-art reconstruction fidelity and strong zero-shot generalization, while using fewer primitives than competing baselines.

</details>

#### 2026-06-28 - HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video

**Authors:** Yiming Jiang, Hanzhang Tu, Wenfeng Song, Siyou Lin, Liang An, Shuai Li, Aimin Hao, Yebin Liu
**Links:** [abs](https://arxiv.org/abs/2606.29333) - [pdf](https://arxiv.org/pdf/2606.29333)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction, human reconstruction, camera calibration, rendering, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video
- 作者：Yiming Jiang, Hanzhang Tu, Wenfeng Song, Siyou Lin, Liang An, Shuai Li, Aimin Hao, Yebin Liu
- 出版日期：2026-06-28
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2606.29333

### 一句话总结
本文提出HiReFF，一种前馈式方法，能够从未标定的稀疏视角视频（四视90°间隔）中重建2K分辨率的360度人体视频。

### 研究问题
如何从未标定的稀疏视角视频中，实现高分辨率（2K）、时间一致且计算高效的前馈式体积视频人体重建。

### 核心思路/方法
将问题分解为两个子任务：
1. **前景3D高斯重建**：针对四视稀疏视频，提出**尺度同步相机标定**解决多视角监督的尺度模糊性，以及**高斯级前景掩码**通过调制高斯参数来重建干净的前景。
2. **高效高分辨率合成**：提出**高分辨率侧调谐**，通过向高斯头部模型补充额外特征来保持主干网络运行在0.5K分辨率，从而实现2K渲染并大幅降低计算开销。

### 主要贡献
- 首次实现从无需标定的稀疏视角视频中进行前馈式2K分辨率360度人体重建。
- 提出尺度同步相机标定和高斯级前景掩码两项技术，分别解决尺度模糊性和前景分离问题。
- 提出高分辨率侧调谐机制，在保持主干低分辨率计算的同时实现高分辨率输出，显著提升效率。
- 实验表明，在高分辨率流式体积视频重建任务中，HiReFF显著优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作解决了未标定稀疏视角视频下的高分辨率人体重建这一前沿难题，技术上提出了创新的标定与高效渲染机制，且结果显著优于现有方法，对体积视频和AR/VR领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Uncalibrated volumetric video streaming for human reconstruction is essential for holographic communication and AR/VR, yet remains challenging due to the need for temporal consistency and computational efficiency from sparse-view inputs. Existing methods rely on per-scene optimization or calibrated cameras, while recent feed-forward models are limited to low-resolution (0.5K) single-frame synthesis. We present HiReFF, a feed-forward method for 2K-resolution 360° human video reconstruction from uncalibrated sparse-view videos. Our framework decomposes the problem into two key tasks: foreground 3D Gaussian reconstruction from sparse-view videos (four views separated by 90°) and computationally efficient high-resolution synthesis. To enable the former, we propose Scale-synchronized Camera Calibration to resolve scale ambiguity for multi-view supervision, and Gaussian-wise Foreground Masking to reconstruct clean foregrounds by modulating Gaussian parameters. For efficient high-resolution synthesis, our High-resolution Side-tuning achieves 2K rendering by augmenting the Gaussian head with supplementary features while keeping the backbone at 0.5K, drastically reducing computational overhead. Experiments demonstrate that HiReFF significantly outperforms existing methods in high-resolution streaming volumetric video reconstruction. https://iridescentjiang.github.io/HiReFF

</details>

#### 2026-06-25 - Look-Before-Move: Narrative-Grounded World Visual Attention in Dynamic 3D Story Worlds

**Authors:** Jiaming Bian, Bingliang Li, Yuehao Wu, Pichao Wang, Zhi Wang, Hailan Ma, Huadong Mo, Zhenhong Sun
**Links:** [abs](https://arxiv.org/abs/2606.26964) - [pdf](https://arxiv.org/pdf/2606.26964)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D, embodied AI

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Look-Before-Move: Narrative-Grounded World Visual Attention in Dynamic 3D Story Worlds
- 作者：Jiaming Bian, Bingliang Li, Yuehao Wu, Pichao Wang, Zhi Wang, Hailan Ma, Huadong Mo, Zhenhong Sun
- 出版日期：2026-06-25
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2606.26964

### 一句话总结
本文提出一个名为 Look-Before-Move 的相机规划框架，该框架通过先构建语义观察契约、进行蒙特卡洛视点搜索，再执行语义轨迹接地，使动态3D故事世界中的智能体能够根据叙事意图主动决定观察内容，而非被动生成运动。

### 研究问题
在动态3D故事世界中，相机如何从被动生成平滑运动转向主动选择观察目标（即根据叙事意图和物理约束决定“看什么”、“如何构图”以及“如何转移注意力”）？

### 核心思路/方法
该方法将相机规划拆分为“观察指定”和“运动执行”两个阶段。具体包含三个步骤：
1. **语义观察契约**：将导演意图（叙事目标）转化为可执行的视觉约束条件。
2. **蒙特卡洛视点搜索**：在满足叙事要求和几何可行性的前提下，搜索符合约束的视点。
3. **语义轨迹接地**：将选定视点连接成连续、无碰撞且时间一致的相机运动轨迹。

### 主要贡献
1. 提出“叙事接地世界视觉注意力”概念，将相机视为在动态3D故事世界中根据叙事意图和物理约束决定观察的具身观察者。
2. 设计 Look-Before-Move 框架，创新性地分离观察指定与运动执行，生成叙事一致且几何可行的相机轨迹。
3. 基于 StoryBlender 构建动态3D故事世界基准，包含50个故事、457个场景、1585个镜头，支持动画角色、语义配置和可执行3D环境。
4. 实验表明，该框架在主体感知、意图一致性和轨迹质量上优于代表性基线方法，验证了在生成相机运动前组织视觉注意力的重要性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中

理由：该工作专注于具身AI在动态3D环境中的视觉注意力与相机规划问题，属于较具体的交叉方向。若研究兴趣在于叙事驱动的智能体感知或动态场景中的运动规划，则本文有较高参考价值；若领域不涉及3D故事世界或具身视觉，则阅读优先级降低。

</details>

<details>
<summary>Abstract</summary>

As embodied AI and world models increasingly operate in dynamic 3D environments, visual perception must move beyond passively interpreting given observations toward actively deciding what to observe. We study this problem through camera planning in dynamic 3D story worlds, where the camera must not only generate smooth motion, but also decide what visual evidence should be acquired before it moves. We formulate this capability as Narrative-Grounded World Visual Attention, where the camera acts as an embodied observer that determines what to observe, how to compose the observation, and how to shift attention over time under narrative intent and physical 3D constraints. To realize this capability, we propose Look-Before-Move, a camera planning framework that separates observation specification from motion execution. It first builds a Semantic Observation Contract to convert directorial intent into executable visual constraints, then performs Monte Carlo Viewpoint Search to find narrative-compliant and geometrically feasible viewpoints, and finally applies Semantic Trajectory Grounding to connect selected viewpoints into continuous, collision-aware, and temporally coherent camera motion. We further construct a dynamic 3D Story World Benchmark based on StoryBlender, covering 50 stories, 457 scenes, and 1585 shots with animated characters, semantic scene configurations, and executable 3D environments. Experiments show that our framework improves subject perception, intent consistency, and trajectory quality over representative baselines, demonstrating the importance of organizing visual attention before generating camera motion.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

#### 2026-06-30 - Planar-SfM: Camera Pose Estimation via Homography Graph Embeddings

**Authors:** Gabi Pragier, Matan Karklinsky, David Ungarish, Avi Ben-Cohen
**Links:** [abs](https://arxiv.org/abs/2606.31979) - [pdf](https://arxiv.org/pdf/2606.31979)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM, camera pose estimation, pose estimation

<details>
<summary>Abstract</summary>

Structure from Motion (SfM) systems traditionally struggle with planar scenes, where standard epipolar geometry-based methods become degenerate. Rather than viewing planar surfaces as a limitation, we propose a unified framework that leverages them as a source of geometric constraints. Our key insight is that each planar surface visible across multiple views provides an independent estimate of relative camera poses through homography decomposition. By aggregating estimates from multiple planes or even from a single dominant plane we achieve robust pose recovery in scenarios where traditional methods fail. We introduce a novel graph-based approach that constructs a pose-graph from homography estimates and employs spectral embedding to identify and filter unreliable edges. Our method maps homography-based pose estimates onto the real line based on their geometric and visual consistency, enabling efficient extraction of a maximally consistent spanning tree for pose recovery. This approach naturally handles both highly planar scenes, such as indoor sports arenas, and general $3$D environments. We demonstrate superior performance on basketball court imagery where existing methods struggle, while matching or exceeding state-of-the-art results on unconstrained outdoor scenes from the IMC Phototourism benchmark.

</details>

#### 2026-06-30 - DrivingDepth: Sparse-Prompted Pixel-wise Scale Correction for Driving Depth Estimation

**Authors:** Chi Huang, Wenhao Zhang, Hang Yin, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Liang Wang
**Links:** [abs](https://arxiv.org/abs/2606.31488) - [pdf](https://arxiv.org/pdf/2606.31488)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, autonomous driving, mapping

<details>
<summary>Abstract</summary>

Dense depth estimation for autonomous driving faces a geometry-scale conflict: depth foundation models deliver pixel-aligned dense visual geometry without reliable metric scale, while projected LiDAR provides metric anchors that are sparse, noisy, and misaligned with image structures. Existing sparse-prompted methods incorporate LiDAR by regenerating depth from scratch, overriding the foundation model's coherent geometry and producing structural artifacts on visually continuous surfaces. Our key insight is that foundation models already capture geometrically coherent relative depth; no additional surface structure learning is required-only a per-pixel scale factor mapping relative geometry to metric coordinates. Based on this, we propose DrivingDepth, which treats sparse LiDAR as geometric prompts that locally calibrate a frozen foundation prior through residual pixel-wise scale correction, preserving dense visual geometry by construction. On nuScenes with 4-frame surround-view input, DrivingDepth achieves an AbsRel of 11.19 and an EdgeCR of 5.741, outperforming MapAnything (11.99/1.914) by simultaneously delivering SOTA metric accuracy and geometric consistency.

</details>

#### 2026-06-30 - CasaMaestro: Multi-View Panoramas for House-Scale 3D Reconstruction

**Authors:** Yuzhou Ji, Xiaotian Yang, Zhipeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.31086) - [pdf](https://arxiv.org/pdf/2606.31086)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, 3D reconstruction, point cloud reconstruction, embodied AI, simulation

<details>
<summary>Abstract</summary>

The rise of home-deployed embodied AI systems is driving a growing need for fast, metric 3D reconstruction of residential spaces to support navigation, interaction, and long-horizon task execution. However, the commonly used pinhole-camera 3D reconstruction pipelines struggle to model large indoor residences efficiently due to their limited field of view, to which achieving full coverage across multiple rooms often requires thousands of images and incurs drift from long chains of incremental alignment. In this work, we present CasaMaestro (Spanish words meaning ``house'' and ``master''), a feedforward model that can take only twenty to fifty sparse multi-view indoor panoramas as input and directly predicts metric depth along with camera poses, allowing fast point-cloud reconstruction of the entire house with full coverage. CasaMaestro is the first model that supports house-scale reconstruction with multi-view panoramas. Experiments show that CasaMaestro can robustly provide high quality results in both real-world and synthetic scenes, which can serve as a strong foundation for acquiring house-scale 3D indoor assets to be applied in close-loop simulation.

</details>

#### 2026-06-29 - Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation

**Authors:** Siddhant Bansal, Zhifan Zhu, Shashank Tripathi, Jiahe Zhao, Michael J. Black, Dima Damen
**Links:** [abs](https://arxiv.org/abs/2606.30598) - [pdf](https://arxiv.org/pdf/2606.30598)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation
- 作者：Siddhant Bansal, Zhifan Zhu, Shashank Tripathi, Jiahe Zhao, Michael J. Black, Dima Damen
- 出版日期：2026-06-29
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.30598

### 一句话总结
本文针对野外第一人称视角下的手-物体3D姿态估计难题，构建了带有密集3D接触标注的野外数据集EPIC-Contact，并提出端到端Transformer模型HOPformer，显著提升了估计成功率并降低了接触误差。

### 研究问题
如何从野外第一人称视角的RGB图像中准确估计手与物体的3D姿态，解决现有方法因严重遮挡和接触歧义而泛化性差、监督数据稀缺的问题。

### 核心思路/方法
1. **数据集构建**：提出EPIC-Contact野外数据集，包含2.3K个片段（62.3K帧），带有密集、双射的3D手-物体接触对应关系及姿态网格模型。
2. **模型设计**：提出HOPformer，一种端到端Transformer架构，单次前向传播即可联合预测双手和物体的3D姿态。其交叉注意力解码器利用手部先验信息调节物体特征，从而实现鲁棒的姿态估计。

### 主要贡献
1. 发布了EPIC-Contact数据集，为野外场景提供了密集的3D手-物体接触标注。
2. 提出了HOPformer模型，在ARCTIC室内数据集上达到82.4%的成功率（超越当前最优方法6.2个百分点）。
3. 在EPIC-Contact数据集上，HOPformer将成功率提升近一倍，同时将接触偏差减少75%。

### 局限性
摘要未提供足够信息。例如，未提及模型的计算成本、对极端光照或快速运动场景的鲁棒性，以及EPIC-Contact数据集的标注多样性或偏差分析。

### 阅读优先级
高。理由：该论文同时贡献了核心数据集和高效模型，在ARCTIC和自建野外数据集上均取得显著提升，且代码和模型已开源，对从事第一人称手-物体交互、3D姿态估计的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Estimating accurate 3D hand-object pose from in-the-wild egocentric RGB remains challenging due to severe occlusions and ambiguous contact. Existing learning-based methods often struggle to generalise to in-the-wild scenes and are limited by the scarcity of supervision. We address these issues with two contributions. First, we introduce EPIC-Contact, an in-the-wild egocentric dataset of 2.3K clips (62.3K frames) with dense, bijective 3D hand-object contact correspondences and posed meshes. Second, we propose HOPformer, an end-to-end transformer that jointly predicts bi-manual hand and object pose in a single forward pass. A cross-attention decoder conditions object features on hand priors, producing robust pose estimation. We test HOPformer on the in-lab 3D dataset, ARCTIC, as well as our newly introduced EPIC-Contact dataset. HOPformer reaches 82.4% success rate on ARCTIC (+6.2 pts over current SOTA). On EPIC-Contact, it nearly doubles the success rate while reducing contact deviation by 75%. EPIC-Contact, HOPformer code and checkpoints are released: https://sid2697.github.io/epic-contact.

</details>

#### 2026-06-29 - StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors

**Authors:** Wenhao Yuan, Yiyuan Ge, Deli Cai
**Links:** [abs](https://arxiv.org/abs/2606.30545) - [pdf](https://arxiv.org/pdf/2606.30545)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** depth estimation, monocular depth, stereo depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors
- 作者：Wenhao Yuan, Yiyuan Ge, Deli Cai
- 出版日期：2026-06-29
- 分类：3D Reconstruction & Multi-view Geometry (主要); Neural Scene Representations & Rendering (次要)
- 链接：摘要链接: https://arxiv.org/abs/2606.30545; PDF链接: https://arxiv.org/pdf/2606.30545

### 一句话总结
本文提出 StereoGS，一种在稀疏视图条件下通过引入立体先验（Stereo Priors）来增强3D高斯泼溅（3DGS）几何一致性的新框架，实现了无需额外推理开销的先进稀疏视图新视角合成性能。

### 研究问题
3D高斯泼溅（3DGS）在稀疏视图设置下因几何约束不足而严重过拟合，现有引入单目深度先验的方法存在尺度模糊和跨视图不一致性，导致几何缺陷。

### 核心思路/方法
1. **立体深度正则化（Stereo Depth Regularization）**：在优化过程中构造虚拟立体对，利用基础立体模型强制施加绝对尺度和双目一致的结构约束，替代传统的尺度不可知单目约束。
2. **梯度感知不透明度衰减（Gradient-Aware Opacity Decay）**：根据高斯原语的相对梯度幅度动态惩罚高斯体，以抑制过拟合并消除冗余原语。
3. **一致性感知密集初始化（Consistency-Aware Dense Initialization）**：使用零样本多视图深度估计方法，将高斯原语有效地锚定到准确的场景表面。

### 主要贡献
- 提出StereoGS框架，首次将立体先验系统性地整合到稀疏视图3DGS中，解决了单目先验的尺度模糊和跨视图不一致问题。
- 设计了立体深度正则化、梯度感知不透明度衰减和一致性感知密集初始化三项关键技术，分别用于建立可靠双目一致性、抑制过拟合和优化初始几何。
- 在LLFF、DTU、Mip-NeRF360和Blender四个数据集上取得稀疏视图下的最先进性能，且不增加额外推理开销。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对3DGS在稀疏视图下的核心难题（几何约束不足）提出了新颖的立体先验框架，方法设计系统且实验结果覆盖多个标准数据集。对于从事3D重建、新视角合成和神经渲染领域的研究者，该工作具有直接的应用价值与启发性。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has achieved remarkable success in real-time novel view synthesis, yet it suffers from severe overfitting under sparse-view settings due to insufficient geometric constraints. While recent methods introduce monocular depth priors to mitigate this, they inherently struggle with scale ambiguity and cross-view inconsistency, leading to defective geometry. In this paper, we propose StereoGS, a novel sparse-view 3DGS framework that integrates stereo priors to establish reliable binocular consistency. Unlike scale-agnostic monocular constraints, StereoGS introduces a Stereo Depth Regularization by constructing virtual stereo pairs during optimization and leveraging a foundation stereo model to enforce absolute scale and binocular-consistent structures. To further suppress overfitting and eliminate redundant primitives, we design a Gradient-Aware Opacity Decay strategy that dynamically penalizes Gaussians based on their relative opacity gradient magnitudes. Combined with a Consistency-Aware Dense Initialization using zero-shot multi-view depth estimation, StereoGS effectively anchors primitives to accurate scene surfaces. Extensive experiments on LLFF, DTU, Mip-NeRF360, and Blender datasets demonstrate that StereoGS achieves state-of-the-art performance in sparse-view settings without incurring any additional inference overhead. Project Page: https://stringerywh00.github.io/StereoGS_project_page/

</details>

#### 2026-06-29 - Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes

**Authors:** Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang
**Links:** [abs](https://arxiv.org/abs/2606.30436) - [pdf](https://arxiv.org/pdf/2606.30436)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes
- 作者：Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang
- 出版日期：2026-06-29
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.30436

### 一句话总结
本文提出KiloGS-SLAM，一种用于千米级室外场景的单目3D高斯SLAM系统，通过运动自适应混合跟踪与生命周期管理的建图策略，同时解决了长时姿态跟踪脆弱和内存开销过大的问题。

### 研究问题
如何将单目3D高斯SLAM扩展至千米级室外场景，同时克服长时位姿跟踪的脆弱性和大规模建图时的内存爆炸问题。

### 核心思路/方法
1. **运动自适应混合跟踪模块**：采用条件触发的三级求解管线，动态在Essential矩阵和PnP模型间切换以处理几何退化，并在需要时激活基础模型救援，防止轨迹灾难性漂移。
2. **生命周期管理的建图策略**：结合概率初始化、分块多视角稠密化与剪枝，通过全管线优化减少高斯原语冗余，同时保留高频细节。

### 主要贡献
- 提出首个联合解决千米级室外场景中姿态跟踪与内存瓶颈的单目3DGS-SLAM系统。
- 设计运动自适应跟踪模块，通过动态求解器切换和按需基础模型激活实现鲁棒长时位姿估计。
- 引入生命周期管理的建图策略，降低内存开销并保持重建质量。
- 在三个室外数据集上达到领先的跟踪精度与渲染质量，支持单GPU处理超1万帧序列。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作挑战了SLAM和3DGS在极大规模场景（千米级）下的部署难题，涉及跟踪与建图的双重工程创新，实验结果达到SOTA，对高精度实时机器人或自动驾驶场景有参考价值。

</details>

<details>
<summary>Abstract</summary>

Scaling monocular 3D Gaussian Splatting (3DGS) SLAM to kilometer-level outdoor environments poses two tightly coupled challenges: fragile long-term pose tracking and excessive memory overhead during large-scale mapping. In this paper, we propose KiloGS-SLAM, a highly efficient and robust monocular 3DGS-SLAM system that jointly addresses both bottlenecks. Since high-fidelity scene reconstruction fundamentally relies on drift-free camera poses, we first introduce a motion-adaptive hybrid tracking module. This module features a condition-triggered three-tier solving pipeline. It dynamically switches between Essential matrix and PnP models to handle geometric degeneracies. An on-demand foundation model can also be activated to rescue the trajectory from catastrophic drift. To ensure the system can sustain these long trajectories without memory exhaustion, we subsequently design a lifecycle-managed Gaussian mapping strategy. By integrating probabilistic initialization with chunk-based multi-view densification and pruning, this full-pipeline optimization effectively reduces primitive redundancy while preserving high-frequency details. Together, the robust tracking guarantees the geometric foundation required for accurate mapping, while the memory-efficient lifecycle-managed mapping enables large-scale operation. Extensive experiments across three challenging outdoor datasets demonstrate that our approach achieves state-of-the-art tracking accuracy and rendering quality, successfully scaling to sequences of over 10,000 frames on a single GPU.

</details>

#### 2026-06-29 - FastPano3D: Feed-Forward Indoor Panoramic 3D Reconstruction from a Single Image

**Authors:** Jianqiang Li, Liumei Zhang, Wenjia Guo, Tianlong Feng, Yongzhi Liao, Di Lu, Hanchi Ren, Jingjing Deng
**Links:** [abs](https://arxiv.org/abs/2606.30352) - [pdf](https://arxiv.org/pdf/2606.30352)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, scene reconstruction, NeRF, Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FastPano3D: Feed-Forward Indoor Panoramic 3D Reconstruction from a Single Image
- 作者：Jianqiang Li, Liumei Zhang, Wenjia Guo, Tianlong Feng, Yongzhi Liao, Di Lu, Hanchi Ren, Jingjing Deng
- 出版日期：2026-06-29T14:23:12Z
- 分类：主分类：3D重建与多视图几何；次分类：神经场景表示与渲染
- 链接：摘要：https://arxiv.org/abs/2606.30352；PDF：https://arxiv.org/pdf/2606.30352

### 一句话总结
FastPano3D提出一种端到端前馈框架，从单张全景图像直接生成可渲染的3D高斯表示，实现无需测试优化的快速室内场景重建。

### 研究问题
如何从单张全景输入中快速重建高保真室内3D场景，同时克服全景图像的等距柱状投影失真和特征分布不均匀问题，并避免多视图监督或逐场景优化。

### 核心思路/方法
1. **轻量级特征编码器**：对单张全景图进行高效特征提取。
2. **自适应高斯采样**：根据全景图的非均匀特征分布，自适应地生成3D高斯原语。
3. **点云引导精化策略**：利用点云信息引导高斯表示的精调，提升重建质量。
4. **前馈生成**：无需测试时优化，直接输出可渲染的3D高斯场景。

### 主要贡献
- 提出首个端到端前馈框架，从单张全景图直接生成3D高斯表示，无需多视图监督或逐场景优化。
- 设计自适应高斯采样和点云引导精化策略，解决全景图像的投影失真和特征分布不均匀挑战。
- 在推理速度上比现有最优方法（如Pano2Room）快156倍，参数量仅为其一半，且渲染质量与NeRF和3DGS方法相当。

### 局限性
摘要未提供关于方法在复杂场景、泛化能力或失败案例方面的局限性信息。

### 阅读优先级
**高**  
理由：该方法在单张图像室内全景3D重建上实现了显著的推理速度提升（156倍）和参数效率（减少一半），且无需测试优化，对实时应用有重要价值。研究背景（全景图失真、前馈生成）和贡献点明确，适合对快速3D场景重建、全景视觉或基于高斯泼溅的渲染方法感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D scene reconstruction have highlighted the intricate trade-offs among rendering quality, inference efficiency, and data dependency. To address the challenge of rapidly reconstructing detailed 3D indoor scenes from minimal input, we introduce FastPano3D, an end-to-end framework that directly generates renderable 3D Gaussian representations from a single panoramic image. Unlike perspective-based methods, panoramic images inherently suffer from equirectangular projection distortions and spatially non-uniform feature distributions, making direct feed-forward Gaussian generation particularly challenging. In contrast to existing Gaussian Splatting based methods that rely on multi-view supervision or per-scene optimization, FastPano3D employs a lightweight feature encoder, adaptive Gaussian sampling, and a point-cloud-guided refinement strategy to achieve efficient and accurate scene generation without any test-time optimization. Our approach reconstructs high-fidelity 3D scenes within seconds, achieving up to 156 times faster inference than prior state-of-the-art methods such as Pano2Room, while using only half the parameters. Extensive experiments demonstrate that FastPano3D delivers rendering quality comparable to NeRF- and 3DGS-based reconstructions, establishing a new benchmark for rapid, single-view 3D scene inference.

</details>

#### 2026-06-29 - Self-supervised Geometry Reasoning for LiDAR Simultaneous Localization and Mapping

**Authors:** Jiwoo Kim, Jinwoo Lee, Woojae Shin, Giseop Kim, Hyondong Oh
**Links:** [abs](https://arxiv.org/abs/2606.30166) - [pdf](https://arxiv.org/pdf/2606.30166)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Self-supervised Geometry Reasoning for LiDAR Simultaneous Localization and Mapping
- 作者：Jiwoo Kim, Jinwoo Lee, Woojae Shin, Giseop Kim, Hyondong Oh
- 出版日期：2026-06-29
- 分类：主分类：3D Reconstruction & Multi-view Geometry，次分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2606.30166) | [PDF](https://arxiv.org/pdf/2606.30166)

### 一句话总结
提出一种自监督框架，通过学习局部几何的显式符号表示（将点表示为高斯分布），并利用SLAM中的一致性关系进行递归优化，以提升低分辨率或稀疏点云下LiDAR SLAM的性能。

### 研究问题
现有LiDAR SLAM流水线依赖手工估计的局部分何（如协方差、对应关系和表面结构），在点云稀疏区域或使用低分辨率LiDAR时，这些估计噪声大且不稳定，导致SLAM性能下降。

### 核心思路/方法
1. 将点云中的每个点表示为高斯分布，用其协方差描述局部几何。
2. 设计自监督学习框架：不依赖密集几何标签或真值位姿，而是通过最大化局部几何的似然来学习；其自监督信号来自几何符号表示（预测的协方差、对应关系）与SLAM输出的轨迹之间的一致性。
3. 将学习到的几何反馈回LiDAR SLAM，形成互惠循环：更好的几何改善定位与建图，更好的定位又为几何推理提供更干净的监督信号。
4. 该框架后端无关，可直接嵌入现有LiDAR SLAM流水线，无需架构改动。

### 主要贡献
- 提出一种自监督的局部分何推理方法，能自主学习点云的几何表示。
- 利用SLAM中几何符号表示之间的一致性关系提供自监督信号，避免了对标签数据的依赖。
- 框架具有后端无关性，易于集成到现有LiDAR SLAM系统。
- 在KITTI数据集上通过不同LiDAR分辨率实验验证了方法对里程计和全局配准都有改进。

### 局限性
摘要未提供足够信息，无法判断该方法在计算开销、泛化到其他数据集或实际部署中的局限性。

### 阅读优先级
**高**。理由：该论文针对LiDAR SLAM中局部几何估计不稳定的核心痛点，提出了一种新颖的自监督学习框架，且实验（KITTI上多分辨率验证）显示有效。方法设计具有一般性（后端无关），对从事SLAM、三维重建或机器人自主定位的研究者有参考价值。

</details>

<details>
<summary>Abstract</summary>

LiDAR simultaneous localization and mapping (SLAM) relies on local geometric quantities such as covariances, correspondences, and surface structures. However, most existing pipelines rely on hand-crafted estimates of local geometry and use them as fixed inputs to LiDAR SLAM, which can make the estimated local geometry noisy and unstable in sparse regions of a point cloud or when using low-resolution LiDAR. To address this issue, this paper introduces a self-supervised framework that learns an explicit symbolic representation of local geometry and uses it to improve LiDAR SLAM recursively. Specifically, each point is represented as a Gaussian distribution, allowing local geometry to be described by a covariance. Without dense geometry labels or ground-truth poses, the framework learns by maximizing the likelihood of local geometry, with self-supervision derived from consistency relations over symbolic geometric representations, including predicted covariances, correspondences, and trajectory from SLAM. The learned geometry is then fed back into LiDAR SLAM, forming a reciprocal loop in which improved geometry enhances localization and mapping, and improved localization provides cleaner supervision for subsequent geometry reasoning. This framework is backend-agnostic and can be plugged into existing LiDAR SLAM pipelines without architectural changes. Experiments on KITTI under varying LiDAR resolutions show that the proposed method improves both odometry and global registration.

</details>

#### 2026-06-29 - Emergence of a Shared Canonical Object Frame from In-the-Wild Videos

**Authors:** Tom Fischer, Martin Sundermeyer, Adam Kortylewski, Eddy Ilg
**Links:** [abs](https://arxiv.org/abs/2606.30058) - [pdf](https://arxiv.org/pdf/2606.30058)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Emergence of a Shared Canonical Object Frame from In-the-Wild Videos
- 作者：Tom Fischer, Martin Sundermeyer, Adam Kortylewski, Eddy Ilg
- 出版日期：2026-06-29
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要：https://arxiv.org/abs/2606.30058

### 一句话总结
本文提出一种自监督方法，仅利用野外物体视频和带噪声的SfM相机位姿，通过共享的粗网格瓶颈，让模型自发学习出通用的规范物体坐标系，无需人工标注规范位姿。

### 研究问题
如何在不需要人工标注规范位姿的前提下，从野外视频中为不同类别的物体自动建立共享的规范坐标系，以便进行跨实例的位姿比较。

### 核心思路/方法
核心思路是让所有训练序列通过一个共享的几何瓶颈——一个不包含类别细节的粗规范网格。模型学习从图像像素到该网格的密集对应关系，并利用SfM的噪声几何估计每段序列的对齐参数。通过多视角一致性和特征提取器的语义先验，在没有规范位姿标签或类别条件的情况下，共享规范帧自然涌现。

### 主要贡献
- 证明仅通过自监督训练（使用野外视频和噪声SfM位姿）可以引导出共享的规范物体帧，无需人工标注。
- 在160,000个野外物体视频上训练后，该方法在类别级位姿估计基准上，达到了与依赖规范位姿监督的方法相当的精度。
- 提供了开源代码和模型检查点。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法在类别级位姿估计这一方向上提出了一种创新的自监督训练范式，消除了对规范位姿标注的依赖，具有一定的启发性。但摘要未提供详细的实验对比（如具体数据集、误差指标）和局限性分析，需进一步阅读原文评估其实际性能和改进空间。

</details>

<details>
<summary>Abstract</summary>

Comparing object orientations and positions across different instances requires their poses to be expressed in a shared canonical frame. Establishing such frames has traditionally required manual annotation, creating a scaling bottleneck that limits category and instance diversity. We show that a shared canonical frame can instead emerge from self-supervised training on object-centric videos captured in the wild, using only noisy camera poses from Structure-from-Motion. Our key idea is to route all training sequences through a shared geometric bottleneck: a coarse canonical mesh that carries no category-specific detail. By learning dense correspondences from image pixels to this mesh, and estimating per-sequence alignments from noisy SfM geometry, a common canonical frame emerges from multi-view consistency and the semantic priors of the feature extractor, without any canonical pose labels or category conditioning. Trained in a self-supervised manner on 160,000 in-the-wild object videos, our method achieves competitive accuracy on category-level pose estimation benchmarks compared to methods that rely on canonical pose supervision. The code and checkpoint is available on https://github.com/Fischer-Tom/Emergent-Canonical-Frame/.

</details>

#### 2026-06-29 - Argus: Metric Panoramic 3D Reconstruction for Indoor Scenes

**Authors:** Xi Li, Linyuan Li, Yan Wu, Tong Rao, Kai Zhang, Xinchen Hui, Cihui Pan
**Links:** [abs](https://arxiv.org/abs/2606.30047) - [pdf](https://arxiv.org/pdf/2606.30047)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, camera pose estimation, pose estimation, depth estimation, point cloud reconstruction, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Argus: Metric Panoramic 3D Reconstruction for Indoor Scenes
- 作者：Xi Li, Linyuan Li, Yan Wu, Tong Rao, Kai Zhang, Xinchen Hui, Cihui Pan
- 出版日期：2026-06-29
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.30047

### 一句话总结
本文提出了Realsee3D混合数据集（含10K室内场景和29.9万全景视点）以及基于该数据训练的Argus前馈网络，解决了因缺乏大规模全景RGB-D训练数据而导致的度量全景三维重建难题。

### 研究问题
如何实现室内场景的度量（metric）全景三维重建，尤其是应对稀疏无序全景图像中因坐标锚点选择不当导致的全局位姿漂移问题。

### 核心思路/方法
1. **数据集构建**：创建了包含1K真实场景和9K合成场景、共29.9万全景视点的Realsee3D混合数据集，并附有精确的度量标注。
2. **可学习共视模块**：Argus采用一个学习得到的共视模块，自动选择几何最优的参考视图作为度量世界坐标系的锚点，以缓解全局位姿漂移。
3. **解耦与多任务学习**：将双向像素到世界映射分解为可解释的子步骤，并引入逐步骤监督和跨坐标联合约束，增强不同预测分支（如相机位姿、深度、点云）之间的几何一致性。

### 主要贡献
- 发布了首个大规模混合全景室内数据集Realsee3D，包含度量标注。
- 提出了Argus前馈网络，在稀疏无序全景图像设置下实现了相机位姿估计、深度估计和点云重建的SOTA（最优）度量性能。
- 设计了可学习共视模块和分解式多任务学习策略，有效提升了几何一致性。

### 局限性
摘要未提供足够信息。文中未明确讨论数据集的覆盖场景多样性、合成到真实域的泛化差距、计算资源需求或失败案例。

### 阅读优先级
**高**
理由：该工作针对全景三维重建中缺乏大规模度量数据的空白，提出了数据集和解决方案，在稀疏输入下取得了SOTA结果，对室内三维重建、全景视觉等方向有较好的参考价值。

</details>

<details>
<summary>Abstract</summary>

Metric feed-forward 3D reconstruction for panoramic data remains under-explored due to the lack of large-scale panoramic RGB-D training data. We present Realsee3D, a hybrid dataset of 10K indoor scenes (1K real, 9K synthetic) with 299K panoramic viewpoints and precise metric annotations, and Argus, a feed-forward network trained on it for metric panoramic 3D reconstruction. In the sparse unordered capture setting of Realsee3D, a poorly chosen coordinate anchor can cause global pose drift. Argus addresses this with a learned covisibility module that selects the geometrically optimal reference view to anchor the metric world frame. To further improve multi-task learning, we decompose the bidirectional pixel-to-world mapping into interpretable sub-steps with per-step supervision and cross-coordinate joint constraints, reinforcing geometric consistency across prediction branches. On the Realsee3D benchmark, Argus achieves state-of-the-art metric performance in camera pose estimation, depth estimation, and point cloud reconstruction. Project page: https://argus-paper.realsee.ai.

</details>

#### 2026-06-29 - TACO: A Test and Check Framework for Robust Pose Graph Optimization

**Authors:** Emilio Olivastri, Alberto Pretto, Tobias Fischer
**Links:** [abs](https://arxiv.org/abs/2606.29851) - [pdf](https://arxiv.org/pdf/2606.29851)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, visual SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TACO: A Test and Check Framework for Robust Pose Graph Optimization  
- 作者：Emilio Olivastri, Alberto Pretto, Tobias Fischer  
- 出版日期：2026-06-29  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2606.29851  

### 一句话总结  
TACO是一个鲁棒位姿图优化框架，通过测试与检查两步法增量过滤异常测量值，在在线部署中兼顾强鲁棒性与计算效率。

### 研究问题  
位姿图优化对由感知混淆导致的异常测量值高度敏感，这些异常会显著降低估计轨迹的质量。现有方法难以在不牺牲在线部署效率的前提下保持鲁棒性。

### 核心思路/方法  
TACO不显式将测量值建模为内点或外点，而是通过两个互补组件增量接近最大一致测量集：  
1. **测试组件**（IPC算法）：在线评估每个新闭环约束的一致性。  
2. **检查组件**（开关式异常清理）：周期性地利用可切换约束，从一致集中移除可能被IPC错误包含的不一致测量值。

### 主要贡献  
1. 提出TACO框架，结合增量概率一致性测试与周期开关式异常清理，实现鲁棒PGO。  
2. 在2D和3D视觉SLAM数据集上，面对高达50%的异常率时，成功率分别超过90%和83%。  
3. 保持在线部署所需计算效率，2D和3D场景的平均收敛时间分别约为45ms和100ms。  
4. 开源实现。

### 局限性  
摘要未提供足够信息。

### 阅读优先级  
**高**  
理由：该工作针对SLAM中关键鲁棒性问题提出了新颖的增量式异常过滤框架，在2D/3D实验中展现了高成功率与低延迟，对实时SLAM系统具有实际应用价值，且代码已开源。

</details>

<details>
<summary>Abstract</summary>

Pose Graph Optimization (PGO) is one of the most widely adopted approaches for solving Simultaneous Localization and Mapping (SLAM) problems. However, PGO approaches are particularly sensitive to outliers, which can substantially degrade the quality of the estimated trajectories. These outliers arise from incorrect place recognition associations caused by perceptual aliasing in the environment. In this paper, we present TACO (short for Test And Check Optimization), a robust optimization framework designed to filter out outliers from PGO systems. Rather than explicitly modeling measurements as inliers or outliers, TACO finds an approximation to the maximally consistent set of measurements incrementally through two complementary components: (i) The test component, namely the Incremental Probabilistic Consensus (IPC) algorithm, evaluates the consistency of each incoming loop closure online. (ii) The check component dubbed Switchable Outlier Sanitization leverages the existing Switchable Constraints to periodically sanitize any inconsistent measurements from the consistent set that IPC may have mistakenly included. We evaluate TACO on 2D SLAM and 3D Visual SLAM datasets against several state-of-the-art methods. The results show robustness comparable to state-of-the-art offline methods while preserving the computational efficiency required for online deployment, achieving a success rate above 90% in 2D and 83% in 3D across outlier rates up to 50%, with mean convergence times of approximately 45 ms and 100 ms, respectively. We release an open-source implementation of our method with this paper.

</details>

#### 2026-06-29 - MyGO-Splat: Multi-Objective Closed-Loop Geometric Feedback for RGB-Only Gaussian SLAM

**Authors:** Fan Zhu, Ziyu Chen, Zhenjun Zhao, Zhisong Xu, Hui Zhu, Mingrui Li, Chunmao Jiang, Javier Civera
**Links:** [abs](https://arxiv.org/abs/2606.29738) - [pdf](https://arxiv.org/pdf/2606.29738)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** simultaneous localization and mapping, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MyGO-Splat: Multi-Objective Closed-Loop Geometric Feedback for RGB-Only Gaussian SLAM
- 作者：Fan Zhu, Ziyu Chen, Zhenjun Zhao, Zhisong Xu, Hui Zhu, Mingrui Li, Chunmao Jiang, Javier Civera
- 出版日期：2026-06-29
- 分类：3D Reconstruction & Multi-view Geometry（主分类），Neural Scene Representations & Rendering（副分类）
- 链接：摘要页 https://arxiv.org/abs/2606.29738，PDF https://arxiv.org/pdf/2606.29738

### 一句话总结
MyGO-Splat 提出了一种仅使用单目RGB输入的闭环高斯SLAM框架，通过将高斯原语光栅化为像素级深度和法线，实现地图对相机位姿的主动监督，并引入尺度自适应对齐形成自校正循环。

### 研究问题
实时单目SLAM存在尺度模糊性和缺乏几何自校正能力的问题。现有仅RGB的系统是开环的，因为深度先验被注入到建图过程，但精化后的几何无法有效调节跟踪漂移。

### 核心思路/方法
MyGO-Splat 是一个闭环高斯SLAM框架，通过两个关键设计实现自校正：
1. 将高斯原语分析性地光栅化为像素级深度和表面法线，使地图能够主动监督相机位姿优化。
2. 引入尺度感知的自适应对齐机制，将基础模型深度估计投影到全局优化的高斯空间中，形成尺度反馈的自校正循环。

### 主要贡献
- 提出闭环高斯SLAM框架，使地图能够主动监督相机位姿优化。
- 设计尺度感知的自适应对齐机制，桥接单目先验与尺度一致性。
- 实验表明，该闭环设计提升了尺度稳定性和外观-几何一致性，在使用仅单目输入的情况下，性能可与RGB-D方法相媲美。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：
- 该工作针对单目SLAM的尺度模糊和几何自校正这一核心难题，提出了闭环反馈的创新思路。
- 仅用RGB输入即达到RGB-D方法的性能，具有实际应用潜力（降低硬件成本）。
- 属于3D重建与SLAM的前沿方向，适合对实时定位与场景重建感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

Real-time monocular Simultaneous Localization and Mapping (SLAM) fundamentally suffers from scale ambiguity and a lack of geometric self-correction. While 3D Gaussian Splatting (3DGS) enables high-fidelity rendering, existing RGB-only systems remain open-loop because depth priors are injected into mapping but refined geometry cannot effectively regulate tracking drift. We present MyGO-Splat, a closed-loop Gaussian SLAM framework that analytically rasterizes Gaussian primitives into pixel-wise depth and surface normals, allowing the map to actively supervise camera pose optimization. To bridge monocular priors and scale consistency, our framework introduces scale-aware adaptive alignment that projects foundation-model depth estimates into the globally optimized Gaussian space, forming a self-correcting cycle for scale feedback. Extensive evaluations show that this closed-loop design improves scale stability and appearance-geometry consistency, achieving performance comparable to RGB-D methods while using only monocular input.

</details>

#### 2026-06-29 - MF-UAVPose6D: A Model-Free Monocular 6-DoF Pose Estimation Framework for Fixed-Wing UAVs

**Authors:** Juanqin Liu, Leonardo Plotegher, Eloy Roura, Shaoming He
**Links:** [abs](https://arxiv.org/abs/2606.29697) - [pdf](https://arxiv.org/pdf/2606.29697)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MF-UAVPose6D: A Model-Free Monocular 6-DoF Pose Estimation Framework for Fixed-Wing UAVs
- 作者：Juanqin Liu, Leonardo Plotegher, Eloy Roura, Shaoming He
- 出版日期：2026-06-29T02:06:37Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：抽象页面：https://arxiv.org/abs/2606.29697；PDF：https://arxiv.org/pdf/2606.29697

### 一句话总结
本文提出了一种无需CAD模型的单目6-DoF位姿估计框架MF-UAVPose6D，专门针对固定翼无人机，仅使用单张RGB图像和相机内参即可实现高效、鲁棒的位姿估计。

### 研究问题
如何在不依赖CAD模型或关键点先验的情况下，对非合作固定翼无人机进行可靠的6-DoF单目位姿估计。

### 核心思路/方法
1. **输入**：推理时仅需单张RGB图像和相机内参。
2. **目标锚点获取**：通过热力图引导的中心定位获得稳定的目标锚点。
3. **视角感知模块（PAM）**：建模观测射线先验，增强对视角变化的适应性。
4. **动态拓扑采样（DTS）**：补充来自机翼、机身和尾翼的弱结构线索，以应对非合作目标缺乏精细模型的问题。
5. **解耦的平移-旋转位姿解码机制**：分别估计平移和旋转分量，提升位姿估计的准确性和鲁棒性。
6. **数据集构建**：创建了FW-UAV6DPose合成数据集，覆盖不同距离、视角和姿态下的固定翼无人机观测样本。

### 主要贡献
- 提出了一种无模型的单目6-DoF位姿估计框架MF-UAVPose6D，不依赖CAD模型或关键点先验。
- 引入视角感知模块（PAM）和动态拓扑采样（DTS）来提升对非合作目标的鲁棒性。
- 构建了FW-UAV6DPose合成数据集，以支持固定翼无人机位姿估计研究。
- 实验表明，该方法在远距离旋转估计、深度恢复和联合位姿评估方面表现强鲁棒性，同时实现准确高效估计。

### 局限性
摘要未提供足够信息，未提及该方法的局限性或潜在不足（例如对极端遮挡、光照变化或实时性要求的限制等）。

### 阅读优先级
**中**。理由：本文提出了一个针对固定翼无人机的无模型6-DoF位姿估计方案，在无人机视觉感知领域具有实际应用价值，但方法创新点（如PAM和DTS）的通用性尚需进一步验证。对于从事3D重建、视觉定位或无人机避障的研究者有一定启发；如果非此领域，可暂缓阅读。

</details>

<details>
<summary>Abstract</summary>

For uncrewed aerial vehicles (UAVs), estimating six-degree-of-freedom (6-DoF) poses is essential for airspace situational awareness, target tracking, and counter-UAV operations. However, non-cooperative targets usually lack computer-aided design (CAD) models and keypoint priors, making existing model-based or keypoint-matching methods difficult to apply reliably. To address these challenges, this paper proposes MF-UAVPose6D, a model-free monocular 6-DoF pose estimation framework for fixed-wing UAVs. During inference, the method takes only a single red-green-blue (RGB) image and camera intrinsics as input. It first obtains a stable target anchor through heatmap-guided center localization, introduces a Perspective-Aware Module (PAM) to model observation-ray priors, exploits Dynamic Topological Sampling (DTS) to complement weak structural cues from the wings, fuselage, and tail, and adopts a decoupled translation-rotation pose decoding mechanism to estimate the 6-DoF pose. In addition, we construct the FW-UAV6DPose synthetic dataset, which covers fixed-wing UAV observations across diverse distances, viewpoints, and poses. Experimental results show that MF-UAVPose6D achieves accurate and efficient monocular 6-DoF pose estimation without requiring CAD models, and demonstrates strong robustness in long-range rotation estimation, depth recovery, and joint pose evaluation.

</details>

#### 2026-06-28 - One Scene, Two Depths: Probing Geometric Ambiguity in Monocular Foundation Models

**Authors:** Xiaohao Xu, Feng Xue, Xiang Li, Haowei Li, Shusheng Yang, Tianyi Zhang, Matthew Johnson-Roberson, Xiaonan Huang
**Links:** [abs](https://arxiv.org/abs/2606.29600) - [pdf](https://arxiv.org/pdf/2606.29600)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Scene, Two Depths: Probing Geometric Ambiguity in Monocular Foundation Models
- 作者：Xiaohao Xu, Feng Xue, Xiang Li, Haowei Li, Shusheng Yang, Tianyi Zhang, Matthew Johnson-Roberson, Xiaonan Huang
- 出版日期：2026-06-28
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：arXiv:2606.29600

### 一句话总结
论文提出单目深度估计中普遍存在几何歧义性（同一像素对应多个有效深度），并构建了双层序数基准MD-3k和Laplacian视觉提示方法，揭示不同基础模型对多层深度的偏好差异。

### 研究问题
单目深度估计模型将复杂的三维场景压缩为每个像素的单标量深度值，忽略了真实世界中单个相机光线可能包含多个几何有效表面（如透明场景中的前景玻璃和背景）。本文旨在衡量和揭示深度基础模型对这种“两层几何歧义性”的处理偏好。

### 核心思路/方法
1. **构建基准MD-3k（MultiDepth-3k）**：一个稀疏的两层序数深度数据集，用于测量模型的深度层偏好和多层空间关系准确性（ML-SRA指标）。
2. **引入Laplacian视觉提示（LVP）**：一种无需训练的频谱输入变换方法，可显著改变某些冻结模型输出的深度层选择。
3. **实验分析**：在标准RGB输入下，评测多种主流深度基础模型在MD-3k上的层偏好差异，并测试LVP对模型输出的影响。

### 主要贡献
1. 首次系统性地揭示单目深度基础模型在几何歧义场景下存在不同的“深度层偏好”，且这些偏好可通过数据/训练惯例而非场景固有真相决定。
2. 提出MD-3k基准和ML-SRA指标，为评估模型的多层几何处理能力提供标准化工具。
3. 发现Laplacian视觉提示（LVP）这种简单变换能有效改变冻结模型的层输出，最强RGB/LVP组合（DAv2-L）达到75.5% ML-SRA准确率。

### 局限性
摘要未提供足够信息（如MD-3k数据集规模、覆盖场景类型、模型类别清单，以及LVP方法在不同架构下的泛化限制等实验细节）。

### 阅读优先级
**高**
理由：该论文挑战了单目深度估计的经典假设（单像素单深度），提出歧义性视角和可测量的双层基准，对透明物体、遮挡等复杂场景的三维重建具有重要启发意义。方法简洁（LVP无需训练），实验设计新颖，适合关注基础模型三维理解能力的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

A faithful 3D world representation should account for layered geometry, where a single camera ray may contain multiple visible and geometrically valid surfaces. Monocular depth estimation, however, reduces this structure to one scalar depth per pixel. Transparent scenes make this ambiguity measurable: the same ray can pass through foreground glass and observe the background, turning the supervised target into a convention of annotation, data, and training rather than a scene-intrinsic truth. A learned predictor exposes this convention as its depth-layer preference. We introduce MultiDepth-3k (MD-3k), a sparse two-layer ordinal benchmark for measuring depth-layer preference and multi-layer spatial relationship accuracy (ML-SRA). On MD-3k, leading depth foundation models exhibit diverse layer preferences under standard RGB input, showing that the same layered geometry can be resolved differently across models. We further find that Laplacian Visual Prompting (LVP), a training-free spectral input transformation, can substantially change the reported layer for certain frozen models. The strongest RGB/LVP pair, DAv2-L, reaches 75.5% ML-SRA. These results suggest that depth foundation models may express complementary geometric hypotheses that standard RGB inference leaves unexpressed. We invite the community to rethink depth supervision and evaluation through an ambiguity-aware lens, where multiple valid 3D interpretations are treated as geometric structure to be measured, preserved, and expressed.

</details>

#### 2026-06-28 - VCS-SLAM: Geometry-Validated Semantic Evidence Fusion for 3D Gaussian SLAM

**Authors:** Raman Jha, Shuaihang Yuan, Yi Fang
**Links:** [abs](https://arxiv.org/abs/2606.29494) - [pdf](https://arxiv.org/pdf/2606.29494)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VCS-SLAM: Geometry-Validated Semantic Evidence Fusion for 3D Gaussian SLAM
- 作者：Raman Jha, Shuaihang Yuan, Yi Fang
- 出版日期：2026-06-28
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.29494

### 一句话总结
VCS-SLAM通过几何验证策略评估语义观测的可靠性，从而在RGB-D 3D高斯SLAM中抑制语义伪影并提升建图一致性。

### 研究问题
现有语义3D高斯SLAM方法在在线建图中，因遮挡、语义边界无支撑及射线几何歧义导致2D语义先验不可靠，进而向全局高斯地图引入持久性语义伪影。

### 核心思路/方法
VCS-SLAM提出了几何验证的语义证据融合框架，通过可见性一致性、表面支撑边界证据和射线级冲突不确定性来评估语义观测的几何可靠性，并基于此构建可靠性感知目标函数，抑制遮挡语义更新、减少无支撑语义渗色、延迟模糊区域标签分配。

### 主要贡献
1. 提出一种几何验证语义证据融合框架，用于RGB-D 3D高斯SLAM。
2. 设计基于可见性一致性、表面支撑边界证据和射线级冲突不确定性的可靠性评估机制。
3. 在Replica和ScanNet数据集上验证了该方法在语义一致性、边界保持、重建质量以及跟踪性能上的提升。

### 局限性
摘要中未提供关于该方法在计算效率、对动态场景的适应性、或对输入噪声鲁棒性等具体局限性信息。

### 阅读优先级
**中**。理由：该工作聚焦于改进语义SLAM中语义先验的可靠性问题，属于细粒度优化方向。如果读者关注三维语义建图中的伪影抑制和几何一致性，则值得阅读；若更关注整体SLAM系统性能或非高斯SLAM方法，则优先级较低。

</details>

<details>
<summary>Abstract</summary>

Visual SLAM performance often deteriorates in complex real-world applications. Semantic 3D Gaussian SLAM commonly fuses 2D semantic priors into a persistent 3D map using uniform optimization weights. However, such priors are not equally reliable in online mapping: occlusions, unsupported semantic boundaries, and ambiguous ray geometry can introduce persistent semantic artifacts into the global Gaussian map. We propose VCS-SLAM, a geometry-validated semantic evidence fusion framework for RGB-D 3D Gaussian SLAM. Instead of treating all semantic observations as uniformly valid supervision, VCS-SLAM evaluates their geometric reliability through visibility consistency, surface-supported boundary evidence, and ray-level conflict uncertainty. The resulting reliability-aware objective suppresses occluded semantic updates, reduces unsupported semantic bleeding, and delays premature label assignment in ambiguous regions. Experiments on Replica demonstrate improved semantic consistency, boundary preservation, and reconstruction quality. Results on ScanNet further show that VCS-SLAM maintains competitive tracking performance under real RGB-D inputs

</details>

#### 2026-06-25 - PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views

**Authors:** Zhisong Xu, Takeshi Oishi
**Links:** [abs](https://arxiv.org/abs/2606.27071) - [pdf](https://arxiv.org/pdf/2606.27071)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, SfM, SLAM, 3DGS, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views
- 作者：Zhisong Xu, Takeshi Oishi
- 出版日期：2026-06-25
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Neural Scene Representations & Rendering（副分类）
- 链接：摘要页（https://arxiv.org/abs/2606.27071），PDF（https://arxiv.org/pdf/2606.27071）

### 一句话总结
PanoImager 是一个无需 SfM 的框架，结合前馈深度/姿态先验、几何条件扩散视图补全和深度引导的 3DGS 优化，从稀疏全景图像中实现稳定的新视图合成与三维重建。

### 研究问题
如何在旋转主导、弱视差运动的极端稀疏全景视图输入下，实现稳定可靠的三维重建和新视图合成，克服传统 SfM/SLAM 初始化不稳定的问题。

### 核心思路/方法
1. **SfM-free 设计**：摒弃 SfM 流程，直接利用前馈任务提供姿态和深度先验。
2. **视图分解与补全**：将稀疏全景图分解为局部透视视图，通过几何条件扩散模型合成辅助视图，以丰富稀疏证据。
3. **深度引导的 3DGS 优化**：利用深度信息稳定高斯渲染优化，提升跨视图一致性。

### 主要贡献
- 提出 PanoImager 框架，在极端稀疏全景视角下实现更优的重建和合成稳定性，可作为 SfM/SLAM 初始化失败时的离线/背景组件，用于地图优化。
- 在多个基准测试中，展现了在极稀疏输入下的鲁棒性提升。

### 局限性
摘要未提供足够信息，无法详细说明具体局限性。

### 阅读优先级
**高**。
理由：该工作针对传统 SfM/SLAM 在稀疏全景场景下的核心痛点（初始化和弱视差）提出了创新的无 SfM 解决方案，结合了深度先验、扩散模型和 3DGS 优化，对实时建图、自主导航和 VR/AR 等领域具有潜在应用价值。

</details>

<details>
<summary>Abstract</summary>

Panoramic sensing offers wide field-of-view coverage, yet 3D reconstruction from sparse panoramas remains challenging under rotation-dominant, weak-parallax motion. In such regimes, SfM/SLAM initialization is often ill-conditioned and unreliable. We present PanoImager, an SfM-free framework that combines feed-forward pose/depth priors, geometry-conditioned diffusion view completion, and depth-guided 3DGS optimization. Given only a few panoramic images, PanoImager decomposes them into local perspective views, synthesizes auxiliary observations to enrich sparse evidence, and stabilizes Gaussian optimization for improved cross-view consistency. Experiments on multiple benchmarks show improved stability under extreme sparsity, suggesting PanoImager as an offline/background component for map refinement when SfM/SLAM fails to initialize.

</details>

#### 2026-06-25 - Rolling Shutter Relative Pose Estimation Made Practical

**Authors:** Daniel Barath
**Links:** [abs](https://arxiv.org/abs/2606.26863) - [pdf](https://arxiv.org/pdf/2606.26863)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rolling Shutter Relative Pose Estimation Made Practical
- 作者：Daniel Barath
- 出版日期：2026-06-25T10:47:53Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.26863

### 一句话总结
本文通过引入仿射对应（ACs）并推导滚动快门校正的仿射约束，将滚动快门相对位姿估计所需匹配点数从20对降至7对，从而使其在RANSAC框架中变得实用。

### 研究问题
如何在不牺牲精度和效率的前提下，减少滚动快门相机相对位姿估计所需的最小匹配点数，从而使其在RANSAC等鲁棒估计中实际可用。

### 核心思路/方法
1. **引入仿射对应（ACs）**：将仿射对应融入滚动快门双视图几何，推导出“RS校正的仿射约束”，每个仿射对应在标准极线约束之外额外提供两个方程。
2. **线性化代数求解器**：利用RS参数物理上的小量，线性化约束；通过零空间投影消除12个RS未知数；使用作用矩阵求解剩余20阶系统，整个求解耗时1.2毫秒。
3. **仅需7个仿射对应**即可同时估计位姿和RS运动参数。

### 主要贡献
- 提出RS校正的仿射约束，将最小匹配点数从20降至7。
- 实现一个高速（1.2毫秒）的线性化代数求解器。
- 在TUM RS基准上，位姿和RS参数精度均优于所有测试方法，且能准确估计平移速度（该量从点对应中因v-t耦合而难以恢复）。
- 在全局快门数据集EuRoC MAV上，精度与标准5点算法相当，表明其泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作解决了滚动快门相对位姿估计长期存在的实用性瓶颈（点数过多），提出了创新性的仿射约束和高效求解器，并在多个基准上验证了精度和泛化能力，对计算机视觉几何建图领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Rolling shutter (RS) cameras equip virtually all consumer devices, yet RS-aware relative pose estimation has remained impractical: the state-of-the-art solver requires a minimum of 20 point correspondences, making RANSAC-based robust estimation prohibitively expensive due to the exponential dependence of the iteration count on the sample size. We make RS relative pose estimation practical by introducing affine correspondences (ACs) into the RS two-view geometry. We derive novel \emph{RS-corrected affine constraints} that account for the coupling between point perturbations and the row-dependent essential matrix, providing two equations per correspondence beyond the standard epipolar constraint. Building on these constraints, we develop a linearized algebraic solver that estimates pose and RS motion from only 7 ACs. The solver exploits the physical smallness of RS parameters to linearize the constraints, eliminates the 12 RS unknowns via null-space projection, and solves the remaining degree-20 system via action matrices in 1.2\,ms. On the TUM RS benchmark, our method achieves the best pose and RS parameter accuracy among all tested methods and, uniquely among RS solvers, provides accurate translational velocity estimates -- which are poorly conditioned from point correspondences alone due to a $\vec{v}$-$\vec{t}$ coupling. On the global-shutter EuRoC MAV dataset, the solver achieves comparable accuracy to the standard 5-point algorithm, demonstrating that it generalizes well to the GS setting. Code is at https://github.com/danini/rolling_shutter_made_practical.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-30 - PointSplat: Compact Gaussian Splatting via Human-Centric Prediction

**Authors:** Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou
**Links:** [abs](https://arxiv.org/abs/2606.32036) - [pdf](https://arxiv.org/pdf/2606.32036)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our key insight is to perform predictions directly in 3D space, enabling the network to learn and produce a highly compact representation. To this end, we propose PointSplat, a novel human-centric approach that directly infers Gaussian primitives from an input point set. The proposed method first estimates a coarse geometric proxy and performs ray casting to prune redundant points and establish explicit 2D--3D correspondences. Subsequently, it employs a Point-Image Transformer to fuse appearance and geometry features, predicting Gaussian attributes in a single forward pass. This design restricts predictions to foreground regions of interest, substantially reducing the total number of Gaussians while improving novel-view rendering quality. Extensive experiments demonstrate that PointSplat achieves higher efficiency and quality while exhibiting strong robustness to variations in view count and image resolution across multiple datasets.

</details>

#### 2026-06-30 - NURBS Splatting: A Unified Differentiable Rendering Framework for Vector Graphics

**Authors:** Jingye Qiu, Shizhe Zhou
**Links:** [abs](https://arxiv.org/abs/2606.31764) - [pdf](https://arxiv.org/pdf/2606.31764)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** differentiable rendering, rendering, splatting

<details>
<summary>Abstract</summary>

Differentiable rendering of planar rational splines remains largely underexplored, despite their widespread use in vector graphics and design. Existing differentiable vector renderers primarily focus on Bézier curves and rely on analytic rasterization, which can suffer from gradient instability and limited flexibility. We propose NURBS Splatting, a unified framework that represents planar rational curves as continuous Gaussian fields. By sampling Gaussians along the curve parameter domain and inside closed regions, rendering is reformulated as a smooth accumulation process with stable gradients. Our method naturally supports long splines, rational weights, non-uniform knots, and closed-region filling. We demonstrate its effectiveness in calligraphy reconstruction, vectorization frameworks, and long-spline image abstraction, showing improved stability and reconstruction quality over existing approaches.

</details>

#### 2026-06-30 - Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera

**Authors:** Kristof Overdulve, Lode Jorissen, Nick Michiels
**Links:** [abs](https://arxiv.org/abs/2606.31679) - [pdf](https://arxiv.org/pdf/2606.31679)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

Mounted butterflies are among the most striking objects in natural history collections. However, their beauty is notoriously hard to digitize in 3D: they are small and fragile, with microscopic hairs and vein structures. Capturing them in sufficient detail, therefore, requires a macro lens, which has a very limited Depth of Field (DoF). Moreover, a camera body cannot be maneuvered beneath a pinned specimen to photograph its ventral surface (the underside of the wings). We introduce an end-to-end pipeline that resolves these challenges to turn such specimens into photo-realistic 3D models viewable from every direction. It combines three ingredients: handheld focus stacking for all-in-focus macro capture without a tripod, a non-contact first-surface mirror system that exposes the ventral surface without touching the specimen, and a segmentation-free, mirror-aware 3D Gaussian Splatting extension. We validate the reconstructions on four diverse specimens.

</details>

#### 2026-06-30 - Intrinsic decomposition and editing of 3D Gaussian splats

**Authors:** Alexandre Lanvin, Jeffrey Hu, Simon Lucas, Adrien Bousseau, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2606.31637) - [pdf](https://arxiv.org/pdf/2606.31637)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

Intrinsic decomposition which expresses image colors as the product of diffuse albedo and shading, possibly augmented with view-dependent residuals has a long history in image editing as it enables the modification of object colors and textures without altering lighting. We extend intrinsic decomposition to radiance fields represented with Gaussian splatting by proposing solutions to three key aspects of such decomposition. First, we describe how to model the intrinsic decomposition as independent sets of Gaussian primitives, which allows each set to adapt to the characteristics of the layer it represents. Second, we present an optimization procedure guided by data-driven predictions to disentangle multi-view photographs of a scene into the aforementioned intrinsic sets. Finally, we provide an editing workflow where users modify the texture of planar surfaces simply by modifying the albedo of that surface in one image. Capturing this edit within the intrinsic radiance field allows re-rendering of the edited scene with plausible lighting under arbitrary viewpoints.

</details>

#### 2026-06-30 - DPPE: Rethinking Camera-Based Positional Encoding for Scaling Multi-View Transformers

**Authors:** Shun Kenney, Teppei Suzuki
**Links:** [abs](https://arxiv.org/abs/2606.31585) - [pdf](https://arxiv.org/pdf/2606.31585)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

The remarkable scalability of Transformers has expanded their application to 3D computer vision, where camera-aware positional encoding is crucial for providing spatial cues in multi-view geometry. Recent advancements have established the practice of using camera parameters -- such as extrinsics or projection matrices -- as relative positional encoding into the query, key, and value vectors of the attention mechanism. However, when scaling up the training recipe of novel view synthesis (NVS) models with the camera-based positional encoding, we observe a significant issue: model performance stagnates in the late stages of training. In this paper, we investigate the cause of the performance bottleneck when scaling up and demonstrate that storing rotation and translation given by the positional encoding in the same dimensions of the value vector causes indeterminacy in their independent identification, hindering training scalability. To address this, we propose Decoupled Pose Positional Encoding (DPPE), a novel camera-based positional encoding that explicitly decouples rotation and translation. Extensive evaluations on NVS tasks demonstrate that DPPE enables stable long-term training even in scaled-up training setup. Furthermore, it exhibits superior generalization performance in extrapolation settings, such as handling an increased number of viewpoints and zoom-in scenarios.

</details>

#### 2026-06-30 - AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings

**Authors:** Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno
**Links:** [abs](https://arxiv.org/abs/2606.31556) - [pdf](https://arxiv.org/pdf/2606.31556)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, radiance field, Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

Generating high-quality novel views at real-time frame rates remains a central challenge in 3D vision, particularly in sparse-view scenarios. Neural radiance fields have demonstrated robust reconstruction from limited observations, but their reliance on volumetric rendering leads to high computational cost and slow inference. In contrast, Gaussian Splatting methods achieve real-time rendering through rasterization, but their optimization is highly sensitive to the quality of the initial geometry. This sensitivity becomes especially problematic in sparse-view settings, where limited observations often lead to incomplete or noisy point-cloud reconstructions. In this work, we present AugSplat, a simple framework for improving Gaussian Splatting in sparse-view regimes using radiance-field-based view augmentation. We first train a radiance field on the sparse input views and use it to synthesize additional images from nearby novel viewpoints, increasing the effective view-space coverage available for supervision. These synthetic views are then used as auxiliary supervision during Gaussian Splatting optimization. We study two variants: Staged AugSplat, which uses synthetic views for an initial optimization phase before switching to real images, and Dual AugSplat, which jointly trains on real and synthetic views with a decaying synthetic loss weight. Experiments on sparse-view mip-NeRF 360 scenes show that AugSplat improves reconstruction quality over standard Gaussian Splatting. Staged AugSplat achieves the strongest average performance, while Dual AugSplat provides a closely performing formulation that keeps real-image supervision active throughout training, and both variants preserve real-time rendering at inference.

</details>

#### 2026-06-30 - WarpHammer: Densifying Scene Warps with 3D Object Priors for Extreme View Synthesis

**Authors:** Michael Green, Gavriel Habib, Dvir Samuel, Tal Berkovitz Shalev, Issar Tzachor, Rami Ben-Ari, Or Litany
**Links:** [abs](https://arxiv.org/abs/2606.31258) - [pdf](https://arxiv.org/pdf/2606.31258)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** geometry foundation model, 3D reconstruction, novel view synthesis, view synthesis, rendering

<details>
<summary>Abstract</summary>

Projection-conditioned novel view synthesis (NVS) warps an explicit 3D reconstruction of the input view into the target camera and conditions a generator on the warped rendering. This works well for small viewpoint changes but degrades sharply under large orbital motion: the warp becomes sparse around the orbited object, where hidden surfaces dominate the new view and mirror-like artifacts emerge, causing the generator to lose both pixel content and the implicit camera cue carried by the warp. We introduce WarpHammer, a training-free framework that resolves this failure mode by augmenting the warped scene with an explicit 3D reconstruction of the object obtained from a native 3D generative prior (e.g., SAM3D). The reconstructed object adds missing foreground surfaces and occludes background points that should no longer be visible, restoring both appearance and camera cues without fine-tuning the base model. The same explicit object representation further unlocks a capability current NVS pipelines do not support: incorporating auxiliary views of the object from sources outside the target scene, for example, a casual snapshot of a car paired with a manufacturer studio shot of the same model. We process the reference and auxiliary images jointly with a pretrained multi-view geometry foundation model, which predicts a unified point cloud that we fuse into the 3D object reconstruction. This yields substantially more faithful geometry than single-image reconstruction, without requiring user-provided camera poses for the auxiliary views. On five benchmarks, WarpHammer produces stable novel views at viewpoint deviations where strong baselines collapse, and is the first scene-level NVS method that can naturally fuse auxiliary, pose-unknown object views from an external source.

</details>

#### 2026-06-30 - Diffusion-Based Material Regularization for Physics-Based Inverse Rendering

**Authors:** Jingwang Ling, Lifan Wu, Feng Xu, Shuang Zhao
**Links:** [abs](https://arxiv.org/abs/2606.31065) - [pdf](https://arxiv.org/pdf/2606.31065)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>Abstract</summary>

Reconstructing physics-based 3D assets -- geometry, materials, and illumination -- from multi-view images is a core problem in computer graphics and vision, and a prerequisite for realistic relighting and editing. Physics-based inverse rendering offers an accurate image-formation model, but is severely underconstrained: without strong priors, illumination is baked into materials, and reconstructions generalize poorly to novel views and lighting. Data-driven diffusion models, in contrast, predict visually plausible materials, yet their predictions rarely satisfy the rendering equation and are not directly usable for physics-based rendering. We bridge these two paradigms rather than replacing either. Our key idea is to treat the predictions of a state-of-the-art diffusion model not as target material values but as a similarity kernel for optimization: we introduce a regularization loss that penalizes deviations in the optimized material over surface regions where the diffusion predictions are near-constant, while leaving the optimization free to match the input images. Built on this regularizer, our end-to-end pipeline jointly reconstructs geometry, materials, and illumination, yielding high-quality assets that drop into standard rendering pipelines and relight faithfully. On the Synthetic4Relight, Stanford-ORB, and DTC-Synthetic datasets, our method significantly outperforms state-of-the-art baselines in both reconstruction accuracy and relighting quality.

</details>

#### 2026-06-30 - Learning Video Dynamics with Predictive Differentiable Rendering

**Authors:** Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun
**Links:** [abs](https://arxiv.org/abs/2606.31050) - [pdf](https://arxiv.org/pdf/2606.31050)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, differentiable rendering, rendering, splatting

<details>
<summary>Abstract</summary>

How to accurately predict a high-fidelity future world? While the visual world is inherently continuous, existing deterministic video prediction models operate in discrete pixel space and are mainly optimized with pixel-wise mean squared error (MSE), which often leads to over-smoothed predictions and a lack of fine-grained visual details. To address these limitations, we propose Predictive Differentiable Rendering (PDR), a novel end-to-end video prediction paradigm that bridges the gap between discrete and continuous representations. Inspired by recent progress in 3D reconstruction with 3D Gaussian Splatting, we introduce PredGS, a lightweight and plug-and-play adapter based on 2D Gaussian representation, which could be seamlessly integrated with existing pixel space predictors, significantly improving spatial detail preservation with negligible computational overhead. Furthermore, we develop predgsplat, a CUDA-accelerated differentiable 2D Gaussian renderer supporting arbitrary channels. Each Gaussian is defined by 5 + C learnable parameters (position, scale, rotation, and C channel amplitudes) and achieves up to 10x faster rendering than the baseline. Optimized by a combined L1 and SSIM loss, PDR overcomes the inherent blurring tendencies of MSE Loss, significantly enhancing the prediction performance. Extensive experiments on diverse real-world benchmarks, including TaxiBJ, WeatherBench, KTH, and Human3.6M, demonstrate that PDR consistently surpasses existing methods, delivering superior detail preservation, visual fidelity, and predictive accuracy.

</details>

#### 2026-06-29 - GRay: Ray Tracing 3D Gaussians Near the Speed of Splats

**Authors:** Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2606.30869) - [pdf](https://arxiv.org/pdf/2606.30869)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) is a popular representation for radiance field reconstruction, distinguished by the rendering speed of its rasterization-based renderer. While 3D Gaussians can also be ray traced, this approach has so far been slower, with 3D Gaussian Ray Tracing (3DGRT) taking nearly one order of magnitude longer to optimize. To address this, we present GRay, a fast ray tracer for 3D Gaussians designed to close this performance gap and match 3DGS's speed. Our method leverages the algorithmic difference between both approaches: unlike rasterization, ray tracing evaluates only Gaussians that are actually intersected by a ray, leading to potentially logarithmic--rather than linear--scaling in the number of primitives. This property allows ray tracing to better exploit dense scenes composed of numerous tiny Gaussians, a configuration which has largely been overlooked. Notably, we show that dense initialization--which creates many small Gaussians--slows down rasterization, but instead speeds up ray tracing. Designed to leverage this effect, GRay renders nearly 4x faster and optimizes nearly 10x faster than 3DGRT while maintaining similar quality, and has competitive speed with 3DGS albeit at somewhat lower quality. Code is available at https://repo-sam.inria.fr/nerphys/gray.

</details>

#### 2026-06-29 - Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields

**Authors:** Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2606.30861) - [pdf](https://arxiv.org/pdf/2606.30861)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, scene representation, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

Radiance fields such as 3D Gaussian Splatting allow real-time rendering of scenes captured from photos. They also reconstruct most specular reflections with high visual quality, but typically model them with "fake" reflected geometry, using primitives behind the reflector. Our goal is to correctly reconstruct the reflector and the reflected objects such as to make specular reflections editable. We present a proof of concept which exploits promising learning-based methods to extract diffuse and specular buffers from photos, as well as geometry and BRDF buffers. Our method builds on three key components. First, by using diffuse and specular buffers of input training views, we optimize a diffuse version of the scene and use path tracing to efficiently generate physically based specular reflections. Second, we present a specialized training method that allows this process to converge. Finally, we present a fast ray tracing algorithm for 3D Gaussian primitives that enables efficient multi-bounce reflections. Our method reconstructs reflectors and reflected objects, including those not seen in the input images, in a unique scene representation. Our solution allows real-time, consistent editing of captured scenes with specular reflections, including multi-bounce effects, changing roughness, and more. We mainly show results using ground truth buffers from synthetic scenes, and also preliminary results in real scenes with currently imperfect learning-based buffers. Code and data are available at: https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections/

</details>

#### 2026-06-29 - GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping

**Authors:** Annika Thomas, Mason Peterson, Jonathan P. How
**Links:** [abs](https://arxiv.org/abs/2606.30809) - [pdf](https://arxiv.org/pdf/2606.30809)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping

<details>
<summary>Abstract</summary>

Existing 3D Gaussian Splatting (3DGS) systems distribute representation capacity uniformly across a scene, ignoring the fact that many downstream robotic tasks engage only a fraction of the reconstructed geometry. This causes valuable onboard compute to be allocated towards optimizing irrelevant parts of the scene, either limiting online capacity or under-optimizing the most relevant parts of the scene. We introduce GaussLite, a task-driven 3DGS mapping system that conditions its representation density on a natural-language task specification. Given a posed RGB-D stream and a task such as "prepare to pick up the object on the desk," GaussLite uses a one-shot LLM parser to extract target and anchor objects, which are grounded per-frame by an open-vocabulary detector and segmented to produce per-pixel relevance masks in real time. The mapper allocates seeding density, gradient flow and scaling by task relevance. At matched Gaussian budget and real-time mapping at 4 Hz on resource-constrained hardware, GaussLite outperforms baselines on ROI PSNR on the Replica Dataset by an average +2.72 dB and on a real-hardware demonstration in indoor and outdoor settings by +2.23 dB. We further show that two task-specialized agents' maps can be fused into a single shared map via per-voxel voting on active-optimization counts in real time, outperforming concatenation by +3.42 dB while only sharing an average 7.08% of the map.

</details>

#### 2026-06-29 - VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes

**Authors:** Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu
**Links:** [abs](https://arxiv.org/abs/2606.30645) - [pdf](https://arxiv.org/pdf/2606.30645)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes
- 作者：Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu
- 出版日期：2026-06-29T17:59:55Z
- 分类：神经场景表示与渲染；具身/机器人/AR应用
- 链接：摘要URL: https://arxiv.org/abs/2606.30645；PDF: https://arxiv.org/pdf/2606.30645

### 一句话总结
该论文提出一个通过合成交互数据来训练人形机器人全身运动策略的框架，利用三维高斯喷溅重建场景，生成视觉-语言-运动学配对数据，并在真实机器人上验证其有效性。

### 研究问题
如何获取大规模、同步的自我中心视觉、语言指令和机器人兼容运动学轨迹数据，以训练感知驱动的人形机器人全身定位-操作策略。

### 核心思路/方法
1. **数据生成流水线**：使用三维高斯喷溅技术重建公制尺度室内场景；利用场景特权信息合成导航和物体交互轨迹；事后渲染配对的自我中心观察。该流水线无需人工干预生成48,000个配对轨迹。
2. **策略训练**：训练一个视觉-语言-运动学策略，预测短时程的全身运动学轨迹。
3. **执行与迁移**：通过全身轨迹跟踪器将预测转化为真实人形机器人的动作，并最终在物理Unitree G1机器人上进行评估。

### 主要贡献
- 提出一个无需人工干预的合成数据生成流水线，利用重建场景构建视觉-语言-运动学配对数据，解决了数据瓶颈问题。
- 在物理Unitree G1机器人上成功展示了基于视觉的导航和单物体运输任务，证明了合成交互数据对基于感知的仿真到现实人形定位-操作的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。
理由：该论文针对人形机器人感知控制中的数据稀缺这一关键瓶颈，提出一个创新性的合成数据生成框架，并结合完整的训练与真实部署验证流程。研究内容对机器人和神经渲染交叉领域具有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Perception-based humanoid loco-manipulation requires connecting egocentric observations and task instructions to whole-body motion. Learning this mapping requires synchronized egocentric images, language commands, and robot-compatible kinematic trajectories, yet no existing data source provides this complete tuple at scale. We address this bottleneck by generating vision-language-kinematics (VLK) supervision synthetically in reconstructed scenes. Our pipeline leverages 3D Gaussian Splatting to reconstruct metric-scale indoor environments, synthesizes navigation and object-interaction trajectories using privileged scene information, and renders paired egocentric observations after the fact. We produce 48,000 paired trajectories with no human intervention and train a VLK policy that predicts short-horizon whole-body kinematic trajectories. A whole-body tracker converts these predictions into actions on the physical humanoid. We evaluate on the physical Unitree G1 performing navigation and single-object transport, demonstrating that synthesized interactions in reconstructed scenes provide effective supervision for sim-to-real perception-based humanoid loco-manipulation. Project Website: https://vision-language-kinematics.github.io/

</details>

#### 2026-06-29 - Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors

**Authors:** Jameel Hassan, Yasiru Ranasinghe, Vishal Patel
**Links:** [abs](https://arxiv.org/abs/2606.30638) - [pdf](https://arxiv.org/pdf/2606.30638)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, rendering, splatting, embodied AI

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors
- 作者：Jameel Hassan, Yasiru Ranasinghe, Vishal Patel
- 出版日期：2026-06-29
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.30638

### 一句话总结
本文提出GaussDet方法，利用开放词汇的2D目标检测器为3D高斯场景实现零样本的开放词汇分割和指代表达式定位，避免了传统方法对稠密CLIP特征的依赖。

### 研究问题
现有基于3D高斯泼溅的开放词汇理解方法存在两个问题：1) 实例分组机制需要预定义实例数量或受噪声影响；2) 依赖CLIP特征限制了语义理解，无法处理复杂的指代表达式地面定位。

### 核心思路/方法
1. 利用具备指代表达能力、开放词汇的2D目标检测器，替代传统的稠密CLIP特征蒸馏。
2. 为每个3D高斯学习实例特征，从而将场景分解为3D实例组。
3. 渲染这些实例组，并从多视角2D检测结果中聚合语义投票，为每个3D实例生成视图聚合语义标签分布（VASD）。该分布作为强正则化器，抑制低质量实例分组带来的虚假标签。

### 主要贡献
1. 提出GaussDet方法，实现了从简单语言查询到复杂指代表达式定位的零样本扩展。
2. 在开放词汇分割（LeRF-OVS、ScanNet数据集）和指代表达式地面定位（Ref-LeRF数据集）两个任务上，均取得优于现有方法的一致性改进。
3. 在严格的零样本设置下，指代表达式定位的mIoU提升达16.7%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法针对特定任务（3D高斯场景的开放词汇与指代分割）有显著性能提升，且关键设计（利用2D检测器替代CLIP）具有启发性。但该方法不涉及通用计算机视觉或新范式突破，适合该方向的从业者阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their bottom-up grouping strategies. Furthermore, the reliance on CLIP restricts semantic understanding to simple noun phrases, preventing complex spatial reasoning and referential expression grounding. We present GaussDet, a method that circumvents the need for dense CLIP features by leveraging discrete, open-vocabulary 2D object detectors with referring expression capabilities. We learn instance features for individual Gaussians to decompose the scene into 3D instance groups. By rendering these groups and aggregating semantic votes from multi-view 2D detections, we generate a robust View-Aggregated Semantic Label Distribution (VASD) for each 3D instance. This view-aggregation strategy acts as a strong regularizer, attenuating spurious labels caused by low-quality instance grouping. Our approach enables a straightforward, zero-shot extension from simple language queries to complex referential grounding. Extensive evaluations across two key tasks -- open-vocabulary segmentation (LeRF-OVS, ScanNet) and referring expression grounding (Ref-LeRF) -- demonstrate that GaussDet achieves consistent improvements over existing methods. Most notably, we achieve a substantial 16.7% mIoU improvement in referential grounding within a strict zero-shot setting.

</details>

#### 2026-06-29 - RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering

**Authors:** Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu
**Links:** [abs](https://arxiv.org/abs/2606.30380) - [pdf](https://arxiv.org/pdf/2606.30380)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering
- 作者：Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu
- 出版日期：2026-06-29
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.30380

### 一句话总结
RenderFormer++ 是一个可扩展且具有物理基础的前馈神经渲染框架，通过引入物理启发的传输引导和层级化物体中心标记化，解决了现有 Transformer 渲染方法在物理一致性和可扩展性上的不足。

### 研究问题
现有基于 Transformer 的前馈神经渲染方法（如 RenderFormer）虽能实现跨场景泛化，但受限于三角形级标记化的二次注意力复杂度，导致物理一致性不足和可扩展性差。核心问题是如何在保持泛化能力的同时，实现物理一致的全局光照渲染，并降低计算与内存开销。

### 核心思路/方法
1. **物理启发的传输引导（PITG）**：将渲染等式的归纳偏置嵌入注意力机制中，并施加传输一致性损失，从而实现物理一致的光传输建模。
2. **层级化物体中心标记化（HOCT）**：通过可学习查询与三角形级特征进行交叉注意力，将三角形级特征聚合成紧凑的物体级标记，在保留几何与辐射度信息的同时显著降低计算和内存成本。

### 主要贡献
- 提出了 PITG，将物理先验融入 Transformer 注意力，提升光照传输的物理一致性。
- 提出了 HOCT，实现从三角形级到物体级标记的层级聚合，大幅提升可扩展性。
- 实验表明，RenderFormer++ 在复杂大规模场景下实现了可扩展、稳定且泛化能力强的前馈全局光照渲染，相比先前方法提升了物理精度和效率。

### 局限性
摘要未提供足够信息。

### 阅读优先级：高
**理由**：该研究直接针对现有 Transformer 神经渲染方法（如 RenderFormer）的物理一致性和可扩展性瓶颈提出解决方案，属于生成式场景表示与渲染领域的核心进展。方法具有明确的物理基础，且实验验证了在复杂大规模场景中的优越性能，对关注可扩展物理渲染的研究者和工程师具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We present RenderFormer++, a scalable and physically grounded feed-forward neural rendering framework for global illumination in mesh scenes. Existing Transformer-based neural rendering methods such as RenderFormer achieve promising cross-scene generalization, but suffer from limited physical consistency and poor scalability due to the quadratic attention complexity of triangle-level tokenization. To address these issues, we introduce Physics-Informed Transport Guidance (PITG), which embeds rendering-equation inductive biases into the attention mechanism and enforces transport consistency loss, enabling physically consistent light transport modeling. We further propose Hierarchical Object-Centric Tokenization (HOCT), which aggregates triangle-level features into compact object-level tokens via cross-attention with learnable queries, substantially reducing computational and memory costs while preserving geometric and radiometric information. Extensive experiments demonstrate that RenderFormer++ achieves scalable, stable, and generalizable feed-forward global illumination rendering across complex large-scale scenes with improved physical accuracy and efficiency over prior neural rendering methods.

</details>

#### 2026-06-29 - Walking in the Implicit: Interactive World Exploration via Neural Scene Representation

**Authors:** Zhiqi Li, Chengrui Dong, Zhenhua Du, Hangning Zhou, Cong Qiu, Hailong Qin, Mu Yang, Dongxu Wei, Peidong Liu
**Links:** [abs](https://arxiv.org/abs/2606.30045) - [pdf](https://arxiv.org/pdf/2606.30045)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation, neural scene representation, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Walking in the Implicit: Interactive World Exploration via Neural Scene Representation
- 作者：Zhiqi Li, Chengrui Dong, Zhenhua Du, Hangning Zhou, Cong Qiu, Hailong Qin, Mu Yang, Dongxu Wei, Peidong Liu
- 出版日期：2026-06-29
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2606.30045

### 一句话总结
提出一种基于固定长度隐式场景表示（NIS）的交互式视频生成范式，将状态演进与渲染分离，实现长程一致的高效世界探索。

### 研究问题
在交互式视频生成中，如何打破传统逐帧隐变量滚动导致的观测合成与状态转换耦合，以提升长程一致性和推理效率。

### 核心思路/方法
1. 提出场景中心范式，将滚动变量从帧隐变量改为固定长度的可渲染隐式状态（NIS），将生成分解为场景状态的随机转移和给定状态下的姿态条件渲染。
2. 实例化为NeuWorld框架：使用Transformer VAE从稀疏带位姿帧学习局部锚定的NIS；扩散Transformer基于未来相机轨迹和几何感知历史状态来演进NIS。
3. 复用VAE编码器作为统一条件器，将相机、参考图像和历史线索映射到同一NIS模态，避免外部异构编码器。

### 主要贡献
- 提出一种解耦状态转移与观测渲染的新范式，通过固定长度隐式场景表示替代逐帧隐变量滚动。
- 实现NeuWorld系统，仅从公开带位姿视图数据训练，无需预训练视频骨干或辅助3D重建器。
- 在长程一致性和推理效率上取得优势。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：针对交互式世界探索任务提出了创新的场景中心范式，有效解决长程一致性问题，且完全基于公开数据训练，对生成式神经渲染和交互式视频领域具有启示价值。

</details>

<details>
<summary>Abstract</summary>

Interactive video generation systems for camera-controlled world exploration roll out growing sequences of latent video frames, entangling state transition with high-frequency observation synthesis. We propose Walking in the Implicit, a scene-centric paradigm that changes the rollout variable from frame latents to a fixed-length, renderable implicit state, termed Neural Implicit Scene (NIS). This factorizes interactive generation into stochastic transition of a compact scene state and deterministic pose-conditioned rendering given the sampled state. We instantiate this paradigm as NeuWorld: a transformer VAE learns locally anchored NIS from sparse posed frames, and a diffusion transformer evolves NIS conditioned on future camera trajectories and geometry-aware retrieved history. By reusing the VAE encoder as a unified conditioner, NeuWorld maps camera, reference-image, and history cues into the same NIS modality, avoiding external heterogeneous encoders. Trained from scratch on public posed-view data without pretrained video backbones or auxiliary 3D reconstructors, NeuWorld achieves strong long-horizon consistency with favorable inference efficiency.

</details>

#### 2026-06-29 - IBRSteG: Learning a Generalizable Steganography Framework for 3D Gaussian Splatting

**Authors:** Fanye Kong, Hongyu Xia, Yu Zheng, Boyang Gong, Jie Zhou, Jiwen Lu
**Links:** [abs](https://arxiv.org/abs/2606.30024) - [pdf](https://arxiv.org/pdf/2606.30024)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IBRSteG: Learning a Generalizable Steganography Framework for 3D Gaussian Splatting
- 作者：Fanye Kong, Hongyu Xia, Yu Zheng, Boyang Gong, Jie Zhou, Jiwen Lu
- 出版日期：2026-06-29 (基于摘要URL推测，摘要本身未明确提供)
- 分类：Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2606.30024；PDF: https://arxiv.org/pdf/2606.30024

### 一句话总结
本文提出IBRSteG，一个可泛化的3D高斯泼溅隐写框架，通过一种场景无关的高斯属性嵌入网络，将秘密场景隐蔽地植入覆盖场景中，无需针对每个场景进行微调。

### 研究问题
如何设计一个可泛化的3D高斯泼溅隐写方法，能够将有意义的3D场景内容（秘密场景）隐蔽地嵌入到另一个3D场景（覆盖场景）中，同时保证高视觉质量和安全性，且无需针对每个新场景重新优化。

### 核心思路/方法
核心是提出GAS（Gaussian Attributes Steganographer）网络，它学习一个场景无关的嵌入函数。该函数将秘密3D高斯点的属性注入到覆盖场景中，直接重建隐写场景，避免了传统的逐场景微调或优化。通过将3D高斯转换为结构化属性，这些属性兼容于2D学习范式，从而增强了对未见3DGS场景的泛化能力。

### 主要贡献
1. 提出了IBRSteG，一个通用且可泛化的3D高斯泼溅隐写框架。
2. 设计了GAS网络，实现场景无关的嵌入过程，无需逐场景优化。
3. 通过将3D高斯转换为结构化属性，提升了方法的泛化能力。
4. 实验表明，该方法在隐藏不同场景时具有高视觉质量、高容量和高安全性。

### 局限性
摘要未提供足够信息。例如，未提及计算复杂度、对复杂场景或极端压缩的鲁棒性、以及不同秘密场景大小对性能的具体影响。

### 阅读优先级
**中**
理由：该工作针对3D场景隐写这一特定技术问题提出了新颖的泛化框架，思路具有创新性。但摘要未提供具体的定量实验结果细节（如与基线方法的数值对比），且属于较新的应用方向，若非直接相关领域，优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

Recent advances in deep learning have notably improved steganographic message hiding. However, designing a generalizable steganographic approach for 3D Gaussian Splatting (3DGS) that can embed meaningful 3D scene content remains challenging. In this paper, we propose IBRSteG, a generalizable framework for 3DGS steganography that enables undetectable concealment of secret scenes within a steganographic scene. Unlike existing approaches whose parameter generation is rigidly coupled with the specific scene, we formulate 3D steganography as a feed-forward 3D Gaussian embedding process that generalizes across different 3DGS scenes. To realize this, we introduce GAS (Gaussian Attributes Steganographer), a network that learns a scene-independent embedding function by injecting the attributes of secret 3D Gaussian points into a cover scene, thereby directly reconstructing the steganographic scenes without per-scene finetuning or optimization. By transforming 3D Gaussian into these structured attributes, these attributes are compatible with 2D learning paradigms and benefit from their structured nature, thereby enhancing generalization to unseen 3DGS scenes. Extensive experiments on established datasets demonstrate that IBRSteG can effectively conceal different scenes with high visual quality, and achieves superior capacity and security. Code is available at https://github.com/LingXiang2023/IBRSteG.

</details>

#### 2026-06-29 - Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting

**Authors:** Xiaobiao Du, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Xin Yu
**Links:** [abs](https://arxiv.org/abs/2606.30017) - [pdf](https://arxiv.org/pdf/2606.30017)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting
- 作者：Xiaobiao Du, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Xin Yu
- 出版日期：2026-06-29T09:21:57Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.30017

### 一句话总结
本文提出Flux-GS，一种针对移动平台的实时3D高斯泼溅方法，通过蒙特卡洛能量聚合和属性增强模块显著降低存储和计算开销，同时保持高保真渲染。

### 研究问题
如何在资源受限的移动平台上实现实时、高保真的3D高斯泼溅渲染，同时减少高阶球谐函数（SH）带来的巨大推理和存储开销。

### 核心思路/方法
1. **蒙特卡洛镜面能量聚合器**：通过采样三阶辐射残差并将镜面能量聚合到紧凑的隐空间，保留低阶频段中的视觉显著光照特征，避免昂贵的蒸馏或预训练。
2. **属性条件SH增强模块**：基于高斯内在属性预测偏移量，用以增强一阶SH表示，在推理前完成提升而不增加额外推理成本。
3. **多视图Alpha密度优化和剪枝策略**：利用多视图指导，确保多视图结构一致性并精确移除冗余高斯图元，解决单视图梯度驱动密度化产生的过多高斯和过拟合问题。

### 主要贡献
- 提出了蒙特卡洛能量聚合器，实现了高阶SH辐射残差的高效压缩。
- 设计了无需额外推理代价的SH增强模块，补偿压缩过程中丢失的高频细节。
- 提出了多视图Alpha密度优化和剪枝策略，提升多视图一致性并减少冗余高斯数量。
- 实验表明该方法在显著减少参数量的同时保持了有竞争力的视觉质量，适用于实时移动渲染。

### 局限性
摘要未提供足够信息：论文未明确讨论在极端低算力设备上的性能表现、训练时间成本，或与现有移动渲染方法的定量对比细节。

### 阅读优先级
**高**。理由：该工作直接针对移动平台的实时3D渲染瓶颈问题，提出了轻量化的能量聚合和增强机制，并开源了代码。对于关注高效神经渲染、边缘部署和3D高斯泼溅在移动端落地的研究者具备较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D Gaussian Splatting have demonstrated unprecedented success in novel view synthesis. However, the substantial inference and storage overhead driven by high-order Spherical Harmonics (SH) are primary bottlenecks for mobile platforms. In this paper, we present Flux-GS, a real-time Gaussian Splatting method designed to achieve high-fidelity rendering with significantly reduced overhead for resource-constrained mobile platforms. We first propose a Monte Carlo Specular Energy Aggregator, sampling third-order radiance residuals and aggregating specular energy into a compact latent space. In this way, our method effectively preserves visually salient lighting features in lower-order bands without expensive distillation or pre-training. To mitigate the high-frequency details lost during compression, we introduce an Attribute-Conditioned SH Enhancement module. This module predicts Gaussian-aware offsets based on intrinsic Gaussian attributes, which enhance the first-order SH representation prior to inference, without extra inference costs. Furthermore, the original single-view gradient-based densification is prone to producing excessive Gaussians and overfitting to a certain view. We address these limitations by proposing a Multi-view Alpha-based Densification and Pruning strategy. By leveraging multi-view guidance, we ensure multi-view structure consistency and the precise removal of redundant primitives. Extensive experiments demonstrate that Flux-GS achieves substantial parameter reduction while maintaining competitive visual quality, offering a robust and scalable solution for real-time mobile rendering. Code: \textcolor{magenta}{\href{https://xiaobiaodu.github.io/flux-gs-project/}{https://xiaobiaodu.github.io/flux-gs-project/}}.

</details>

#### 2026-06-29 - Shell-Supervised Gaussian Splatting for Urban Real-to-Sim Reconstruction

**Authors:** Yuan Yang, Peijun Lu, Fangzhou Lu, Sai Fan, Siqi Yan, Chenyuan Zhang, Haobo Liang, Yichen Wang
**Links:** [abs](https://arxiv.org/abs/2606.30014) - [pdf](https://arxiv.org/pdf/2606.30014)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** video reconstruction, 3D reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting, embodied AI

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Shell-Supervised Gaussian Splatting for Urban Real-to-Sim Reconstruction
- 作者：Yuan Yang, Peijun Lu, Fangzhou Lu, Sai Fan, Siqi Yan, Chenyuan Zhang, Haobo Liang, Yichen Wang
- 出版日期：2026-06-29
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.30014

### 一句话总结
本文提出一种外壳监督高斯溅射方法，利用外部建筑结构壳作为几何监督，改善城区立面视频三维重建中的表面几何稳定性，同时保持新视角渲染质量。

### 研究问题
如何从城市近景立面视频重建出几何稳定、可用于具身智能（碰撞推理、导航、交互）的三维场景，同时避免玻璃、反射、重复窗户和弱纹理区域导致的表面几何不稳定问题。

### 核心思路/方法
- 将外部立面结构壳（facade structural shell）作为轻量几何监督。
- 将外壳对齐到视频重建帧，渲染每视角深度、相机空间法线和有效掩码图。
- 通过掩码门控损失（mask-gated losses）在3D高斯优化过程中约束这些几何线索，仅作用于外壳支持的可见立面区域。
- 保留RGB驱动的外观优化，仅正则化外壳覆盖区域，平衡外观逼真度与几何稳定性。

### 主要贡献
- 提出外壳监督框架，无需密集标注即可改善城区立面几何重建质量。
- 设计掩码门控损失机制，在保持渲染质量的同时提升立面朝向和可见表面点云一致性。
- 在匿名的近景城区立面场景上，相对于仅照片、单目线索和面向表面的高斯基线方法，展示了更好的几何一致性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。
理由：该方法针对城市立面视频重建的特定几何问题，对于从事具身智能、城市三维重建或高斯溅射领域的研究者具有参考价值。但该方法高度依赖外部结构壳的先验，且实验数据为匿名场景，普适性需进一步验证。若研究方向不涉及城市立面几何约束，则优先级较低。

</details>

<details>
<summary>Abstract</summary>

Real-to-sim reconstruction for embodied AI requires geometry that is useful for collision reasoning, navigation, and agent-environment interaction, not only photorealistic novel-view synthesis. However, close-range urban facades are difficult for video-to-3D reconstruction: glass, reflections, repeated windows, and weak texture can produce visually plausible renderings with unstable surface geometry. We introduce shell-supervised Gaussian Splatting, a reconstruction-stage framework that uses an external facade structural shell as lightweight geometric supervision for video-driven Gaussian reconstruction. The method aligns an exterior shell to the video reconstruction frame, renders per-view depth, camera-space normal, and valid-mask maps, and applies these cues through mask-gated losses during Gaussian optimization. This design preserves RGB-driven appearance while regularizing only visible shell-supported facade regions. Experiments on anonymized close-range urban facade scenes show improved facade orientation and visible-surface point-cloud consistency over photo-only, monocular-cue, and surface-oriented Gaussian baselines, while maintaining comparable held-out rendering quality.

</details>

#### 2026-06-29 - UniTriSplat: A Unified 3D Gaussian Splatting Framework with Uniform Spherical Rasterization for Universal Cameras

**Authors:** Yipeng Zhu, Huajian Huang, Tristan Braud, Sai-Kit Yeung
**Links:** [abs](https://arxiv.org/abs/2606.29794) - [pdf](https://arxiv.org/pdf/2606.29794)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniTriSplat: A Unified 3D Gaussian Splatting Framework with Uniform Spherical Rasterization for Universal Cameras
- 作者：Yipeng Zhu, Huajian Huang, Tristan Braud, Sai-Kit Yeung
- 出版日期：2026-06-29
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.29794

### 一句话总结
UniTriSplat 在单位球面上用 HEALPix 离散化统一了多种相机模型（如透视、鱼眼、全景）的 3D 高斯泼溅渲染，解决了跨相机模型的采样不一致和性能下降问题。

### 研究问题
现有 3D 高斯泼溅（3DGS）框架依赖于特定相机的光栅化，导致在不同相机模型（如透视、鱼眼、全景）之间，立体角采样不一致，且渲染性能下降。

### 核心思路/方法
- **统一框架**：在单位球面上重新定义高斯泼溅，使用 HEALPix 离散化构造球形采样网格，该网格与输入图像的角分辨率对齐，并具有等面积属性。
- **直接球形弧度域优化**：在高斯的正向渲染和梯度传播中，直接在球形弧度域进行推导，使得从窄视场图像到 360 度全景的优化行为一致。
- **损失函数**：引入基于 HEALPix 的 SSIM 损失（HEALPix-aware SSIM loss），尊重球面邻域结构，以提升感知重建质量。

### 主要贡献
- 提出了一个统一的 3DGS 框架 UniTriSplat，适用于包括透视、鱼眼和全景在内的通用相机。
- 通过 HEALPix 等面积离散化，实现了从窄视场到 360 度全景的均匀优化行为。
- 引入了尊重球面邻域结构的 HEALPix 感知 SSIM 损失，提升感知重建质量。
- 实验表明，UniTriSplat 在多种相机模型上一致地提升了跨相机泛化能力，同时保持了几何保真度和渲染质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作解决了 3DGS 在多相机模型（如鱼眼、全景）下的核心痛点，提出了基于 HEALPix 的通用统一框架，具有理论创新和实用价值。适用于对神经渲染、新视图合成、全景/鱼眼相机建模感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

Existing 3D Gaussian Splatting (3DGS) frameworks rely on camera-specific rasterization, suffering from inconsistent solid-angle sampling and degraded performance across heterogeneous camera models (e.g., perspective, fisheye, omnidirectional). To address this limitation, we propose UniTriSplat, a unified 3DGS framework for universal cameras that reformulates Gaussian splatting on the unit sphere via HEALPix discretization. Leveraging the equal-area property of HEALPix, we construct a spherical sampling grid aligned with the angular resolution of input images. We derive the forward rendering and gradient propagation of Gaussians directly in the spherical radian domain, yielding uniform optimization behavior from narrow-FoV images to full 360-degree panoramas. To enhance perceptual reconstruction quality, we additionally introduce a HEALPix-aware SSIM loss that respects spherical neighborhood structure. Extensive experiments across diverse camera models demonstrate that UniTriSplat consistently improves cross-camera generalization while preserving geometric fidelity and rendering quality.

</details>

#### 2026-06-29 - Graph-GSReg: Leveraging 3D Scene Graphs for Gaussian Splatting Registration

**Authors:** Jaewon Lee, Mangyu Kong, Euntai Kim
**Links:** [abs](https://arxiv.org/abs/2606.29782) - [pdf](https://arxiv.org/pdf/2606.29782)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D mapping, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Graph-GSReg: Leveraging 3D Scene Graphs for Gaussian Splatting Registration
- 作者：Jaewon Lee, Mangyu Kong, Euntai Kim
- 出版日期：2026-06-29T04:58:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2606.29782) | [PDF](https://arxiv.org/pdf/2606.29782)

### 一句话总结
本文提出Graph-GSReg，通过将3D高斯泼溅场景转化为3D场景图，将多场景配准问题转化为图配准问题，并引入自监督测试时优化来合并场景以减少伪影。

### 研究问题
如何高效且准确地合并多个3D高斯泼溅（3DGS）场景，形成一个统一的大尺度高斯表示，同时克服现有方法依赖大规模数据集训练或昂贵初始化的局限。

### 核心思路/方法
1. **构建3D场景图**：从每个3DGS及其渲染图像中提取语义和结构信息，构造高阶的场景图表示，将3DGS配准重新定义为图配准问题。
2. **全局一致性理解**：场景图提供全局一致的语义和结构上下文，辅助实现更精确的配准。
3. **自监督测试时优化**：合并两个高斯场景后，通过优化减少遮挡伪影（如空洞和漂浮物），保持原始场景与合并场景之间的视觉一致性。

### 主要贡献
- 提出将3DGS配准转化为图配准问题的新范式，利用3D场景图实现高阶表示。
- 引入无需外部标注的自监督测试时优化，改善合并场景的视觉质量。
- 在真实和合成基准上验证了方法，在配准精度和合并场景渲染质量上具有竞争力。

### 局限性
摘要未提供足够信息。未提及方法在计算效率、对场景复杂度或噪声的鲁棒性、以及场景图构建失败时的应对策略等方面的局限性。

### 阅读优先级
**中**  
理由：该方法在3D场景合并领域提出了新颖的图配准视角，自监督优化设计具有实用价值，适合关注神经场景表示与配准融合的研究者。但摘要未提供具体定量结果或与现有方法的对比细节，需要进一步阅读论文以评估实际改进程度。

</details>

<details>
<summary>Abstract</summary>

Merging multiple 3D Gaussian Splatting (3DGS) scenes into a single unified Gaussian representation is essential for large-scale 3D mapping and long-term map management. Despite its importance, this area remains underexplored, and existing solutions exhibit several limitations. Learning-based methods attempt direct correspondence between Gaussian primitives and require training on large 3DGS datasets. Image-based optimization methods depend heavily on coarse initialization from generic foundation models and often incur expensive refinement. We present \ourmodel. Our method constructs a 3D scene graph from a 3DGS and its rendered images, \textit{reformulating 3DGS registration as a graph registration problem}. The proposed 3D scene graph represents each 3DGS at a higher-level representation, enabling a globally consistent understanding of semantic information and structural context for accurate registration. To further construct a seamless unified scene, we introduce a Self-Supervised Test-Time Optimization. Naively merging two 3D Gaussian scenes often suffers from occlusion artifacts such as hollows and floaters. To alleviate this issue, we refine the merged Gaussians to preserve visual consistency between the original scenes and the merged scene. We evaluate our method on real and synthetic benchmarks, demonstrating competitive registration accuracy and merged scene rendering quality.

</details>

#### 2026-06-28 - Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from Unposed Views

**Authors:** Mijin Yoo, In Cho, Subin Jeon, Jiwoo Lee, Eunbyung Park, Seon Joo Kim
**Links:** [abs](https://arxiv.org/abs/2606.29513) - [pdf](https://arxiv.org/pdf/2606.29513)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, novel view synthesis, view synthesis, differentiable rendering, rendering, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from Unposed Views  
- 作者：Mijin Yoo, In Cho, Subin Jeon, Jiwoo Lee, Eunbyung Park, Seon Joo Kim  
- 出版日期：2026-06-28  
- 分类：Neural Scene Representations & Rendering  
- 链接：[摘要](https://arxiv.org/abs/2606.29513) | [PDF](https://arxiv.org/pdf/2606.29513)  

### 一句话总结
本文提出一种前馈式框架，直接从无位姿多视图图像中分解出实例结构的3D令牌组，实现联合重建、分割和物体级操作，无需3D标注。

### 研究问题
如何从无位姿多视图图像中直接获取实例级别的3D场景表示，使物体实例成为原生接口而非后处理产物，从而支持重建、分割和编辑。

### 核心思路/方法
- 设计一种实例结构的3D令牌组（token group），每组包含一个实例令牌（捕捉实体级身份）和多个锚点令牌（编码局部几何与外观）。  
- 令牌组通过可微渲染学习，联合使用重建和分割监督，无需3D标注。  
- 解码时将令牌组转换为3D高斯集合，实现两层分解（identity vs. local appearance），使实例成为表示的原生组成部分。

### 主要贡献
- 提出从无位姿视图直接生成实例结构3D令牌组的前馈方法，无需后处理分割。  
- 实现类无关实例分割超越场景级优化基线，同时在新型视角合成上保持竞争力。  
- 令牌组天然支持实例级场景编辑（移除、平移、插入物体）和高效开放词汇3D实例检索（复杂度与实例数而非图元数相关）。

### 局限性
摘要未提供足够信息，例如：方法在极端遮挡或高复杂度场景下的鲁棒性、令牌组数量的预设机制、跨场景泛化性能的具体限制等。

### 阅读优先级
**高**  
理由：该工作提出一种新颖的“实例即原生接口”范式，直接解决3D表示中物体级结构缺失的关键问题，且在分割与编辑任务上展示出显著优势，对神经场景表示和3D理解领域具有较强启发性，适合深入阅读。

</details>

<details>
<summary>Abstract</summary>

A 3D scene is understood through its objects, not the primitives that compose them. Yet feed-forward reconstruction methods output dense, unstructured sets of points or Gaussians, leaving object-level structure to be recovered after the fact. We propose a feed-forward framework that decomposes a scene into instance-structured 3D token groups directly from unposed multi-view images -- compact object-centric units from which reconstruction, segmentation, and manipulation all follow. Each token group pairs an instance token capturing entity-level identity with anchor tokens that encode local geometry and appearance, which are decoded into a set of 3D Gaussians. This two-level factorization decouples object identity from local appearance, making object instances a native interface of the representation rather than a derived product. The token groups are learned through differentiable rendering with joint reconstruction and segmentation supervision, requiring no 3D annotations. Our feed-forward model surpasses per-scene optimization baselines in class-agnostic instance segmentation while remaining competitive in novel view synthesis. Beyond these metrics, the same token groups directly unlock instance-level scene editing -- removing, translating, or inserting objects by operating on their groups -- as well as efficient open-vocabulary 3D instance retrieval, where retrieval complexity scales with the number of instances rather than primitives.

</details>

#### 2026-06-28 - Rectifying Mask via Entropy for Distractor-Free 3DGS in Ambiguous Scenarios

**Authors:** Wongi Park, Jiyeon Lim, Minjae Lee, Myeongseok Nam, Seongjun Choi, Jungwoo Kim, Soomok Lee, William J. Beksi, SangHyun Lee
**Links:** [abs](https://arxiv.org/abs/2606.29496) - [pdf](https://arxiv.org/pdf/2606.29496)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3DGS, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rectifying Mask via Entropy for Distractor-Free 3DGS in Ambiguous Scenarios
- 作者：Wongi Park, Jiyeon Lim, Minjae Lee, Myeongseok Nam, Seongjun Choi, Jungwoo Kim, Soomok Lee, William J. Beksi, SangHyun Lee
- 出版日期：2026-06-28
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.29496

### 一句话总结
本文提出RefineSplat框架，利用熵感知自适应掩码方法处理三维高斯泼溅中因颜色或语义模糊导致难以区分的干扰物问题，实现无干扰的新视角合成，并在一个包含18个模糊场景的新数据集上取得最优性能。

### 研究问题
现有方法在辨别静态场景与瞬态干扰物时，常因颜色或语义相似性（即模糊场景）而失效。本文旨在解决如何系统性地识别和去除这些模糊干扰物，以提升三维重建的鲁棒性。

### 核心思路/方法
1. **熵感知自适应掩码**：结合熵和实例掩码来捕捉模糊干扰物，而非仅依赖颜色或语义线索。
2. **熵感知密度控制**：针对模糊场景，利用熵感知的位置梯度对高斯体进行自适应调整，以对齐三维场景中的模糊区域。
3. 构建并公开了一个包含18个场景的“Ambiguous wild”数据集，专门评估颜色或语义相似场景下的干扰物去除性能。

### 主要贡献
- 提出RefineSplat系统框架，有效生成暂态掩码以识别多种模糊干扰物。
- 对现有方法的局限性进行了定性和定量分析，并提出基于熵的适应性掩码方法。
- 引入熵感知密度控制机制，提升高斯体在模糊场景中的对齐能力。
- 创建并公开了首个针对模糊场景的基准数据集（Ambiguous wild），包含18个挑战性场景。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的计算效率、对极端模糊情况的鲁棒性上限、或在不同场景类型（如室内/室外）下的泛化性。

### 阅读优先级
高  
理由：该方法针对3DGS领域尚未充分解决但又很实际的模糊干扰物问题，提出了全新的熵感知策略，并提供了专用数据集和SOTA性能，对从事三维重建与新视角合成方向的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

We present RefineSplat, a systematic framework that effectively constructs transient masks to identify diverse ambiguous distractors. To do this, we qualitatively and quantitatively analyze issues and propose a novel entropy-aware adaptive masking method. Unlike existing approaches that struggle to distinguish transient elements from static scenes due to color or semantic ambiguity, RefineSplat captures ambiguous distractors leveraging entropy and instance masks. Furthermore, we propose a simple yet effective entropy-aware density control to align Gaussians in ambiguous scenarios considering Entropy-aware positional gradients. Additionally, to rigorously validate our method, we first create and release the Ambiguous wild dataset, including 18 scenes where distractors and static scenes are hard to distinguish due to color or semantic resemblances. Experimental results on various datasets demonstrate that RefineSplat shows state-of-the-art performance, showing distractor-free novel view synthesis.

</details>

#### 2026-06-28 - Resonant Brane Splatting for Arbitrary-Scale Super-Resolution

**Authors:** Giulio Federico, Giuseppe Amato, Claudio Gennaro, Fabio Carrara, Marco Di Benedetto
**Links:** [abs](https://arxiv.org/abs/2606.29453) - [pdf](https://arxiv.org/pdf/2606.29453)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Resonant Brane Splatting for Arbitrary-Scale Super-Resolution
- 作者：Giulio Federico, Giuseppe Amato, Claudio Gennaro, Fabio Carrara, Marco Di Benedetto
- 出版日期：2026-06-28
- 分类： Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.29453

### 一句话总结
本文提出 Resonant Brane Splatting (RBS) 方法，通过引入更富表达力的“Brane”原语替代传统高斯泼溅，用于任意尺度超分辨率重建，在保持高质量的同时显著提升渲染速度。

### 研究问题
如何解决任意尺度超分辨率（ASR）任务中，基于高斯泼溅（GS）的方法因使用平滑的低通原语而需要大量重叠原语来建模边缘与纹理，导致光栅化效率瓶颈的问题。

### 核心思路/方法
1.  **原语设计**：用“Brane”原语替换传统的高斯原语。Brane 在标准高斯包络上叠加多个内部高斯-埃尔米特模式，每个模式赋予一个独立的颜色系数，从而能在单个原语覆盖区域内表达局部对比与复杂纹理。
2.  **参数预测**：直接从低分辨率特征预测 Brane 参数（包括模式系数）。
3.  **高效光栅化**：基于经典量子转折点设计一种精确的剔除策略，可安全跳过贡献可忽略的区域，大幅减少渲染计算量。整个光栅化过程可微分。

### 主要贡献
- 提出 Resonant Brane Splatting 框架，用于前馈任意尺度超分辨率。
- 设计了 Brane 原语，其数学形式比简单高斯更丰富，能在更少的重叠原语条件下实现高质量重建。
- 实现了带有精确剔除策略的高效可微分光栅化器，显著降低渲染开销。
- 在标准 ASR 基准上，相对于隐式方法和传统高斯泼溅基线，均取得了更好的重建质量与更优的速度-质量权衡。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对任意尺度超分辨率任务中高斯泼溅方法的瓶颈（原语重叠导致渲染效率低）提出了一种新颖的原语改进方案（Brane），并通过理论推导与实验结果展示了质量与速度的双重提升，对计算机视觉中的高效渲染与超分辨率领域有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Arbitrary-Scale Super-Resolution (ASR) reconstructs images at continuous magnification factors. Recent methods accelerate inference by replacing computationally heavy implicit neural decoders with explicit 2D Gaussian Splatting (GS). However, since standard Gaussians are smooth low-pass primitives, modeling edges and fine textures requires multiple overlapping, well-aligned splats, which creates severe bottlenecks during rasterization. To address this, we introduce Resonant Brane Splatting (RBS), a feed-forward ASR framework. RBS replaces flat Gaussians with Branes: expressive primitives that emit spatially varying colors to natively model local contrast and complex textures within a single footprint. We achieve this by augmenting the standard Gaussian envelope with internal Gaussian-Hermite modes, assigning a distinct color coefficient to each. The zero-order mode recovers standard GS, while higher-order modes capture high frequencies. We predict Brane parameters directly from low-resolution features. Because Branes provide a mathematically richer formulation than simple Gaussians, far fewer primitives need to overlap to reconstruct a given target pixel. To exploit this, we introduce an efficient fully differentiable rasterizer with a precise culling strategy based on the classical quantum turning point. This allows us to safely skip negligible regions, drastically reducing the rendering overhead. Experiments on standard ASR benchmarks show that RBS improves reconstruction quality over implicit and GS baselines, while achieving superior speed-quality trade-off than prior GS methods.

</details>

#### 2026-06-28 - DR-GS: Physically-Based Deformable and Relightable 2D Gaussians

**Authors:** Jiaxin Li, Tong Wu, Yi Wei, Tailin Wu, Li Zhang
**Links:** [abs](https://arxiv.org/abs/2606.29379) - [pdf](https://arxiv.org/pdf/2606.29379)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, inverse rendering, relighting, rendering, splatting, manipulation, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DR-GS: Physically-Based Deformable and Relightable 2D Gaussians
- 作者：Jiaxin Li, Tong Wu, Yi Wei, Tailin Wu, Li Zhang
- 出版日期：2026-06-28T13:03:13Z
- 分类：Neural Scene Representations & Rendering（主），Embodied / Robotics / AR Applications（次）
- 链接：摘要：https://arxiv.org/abs/2606.29379，PDF：https://arxiv.org/pdf/2606.29379

### 一句话总结
DR-GS 提出一个统一的高斯泼溅框架，通过显式解耦几何、光照和材质，实现对可变形物体的物理合理渲染、重光照和编辑，解决了现有方法在动态变形和光照变化下的外观不一致问题。

### 研究问题
现有基于高斯泼溅的可变形物体方法存在两个关键局限性：1）光照被错误烘焙到纹理中，导致动态变形和光照变化下外观物理不一致；2）基于快照的重建限制了重建后的材质编辑。

### 核心思路/方法
将物理基逆渲染、重光照和变形感知操作整合到一个统一的高斯泼溅框架中，通过显式解耦几何、光照和材质表示，克服静态快照的限制，实现变化场景下的真实外观及后重建参数编辑。

### 主要贡献
1. 提出DR-GS框架，首次在高斯泼溅中统一了物理基逆渲染、重光照和变形感知操作。
2. 显式解耦几何、光照和材质表示，解决了静态快照的限制，使外观在动态变形和光照变化下保持物理一致。
3. 建立了完全解耦的几何-光照-材质管线，支持高质量3D资产创建和全面的后编辑。
4. 实验表明DR-GS在静态重建、动态变形和重光照中均达到领先视觉效果，可靠保留光泽表面的反射和高光。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。
理由：该方法直接针对可变形物体的重光照和编辑这一热门且具有挑战性的问题，提出了一个统一的物理基框架，在VR/AR和数字内容创作领域有重要应用潜力。论文来自知名研究机构，实验表现领先，且代码和论文均已公开，适合相关方向研究者跟进。

</details>

<details>
<summary>Abstract</summary>

Gaussian splatting (GS) has garnered significant attention in VR/AR and digital content creation due to its explicit parameterization and efficient rendering capabilities. However, existing GS-based methods for deformable objects face two key limitations: (i) illumination is erroneously baked into textures, causing physically inconsistent responses under dynamic deformations and lighting changes; (ii) snapshot-based reconstruction restricts post-reconstruction material editing. To address these challenges, we propose Deformable and Relightable GS (DR-GS), a unified Gaussian framework that integrates physically-based inverse rendering, relighting, and deformation-aware manipulation. Through explicitly disentangling geometry, illumination, and material representations, DR-GS overcomes the limitations of static snapshots, resolving unrealistic appearance under varying conditions while enabling post-reconstruction parameter editing. Extensive experiments show that DR-GS achieves leading visual quality across static reconstruction, dynamic deformation, and relighting, reliably preserving reflections and specular highlights on glossy surfaces. It further establishes a fully decoupled geometry-illumination-material pipeline, enabling high-quality 3D asset creation and comprehensive post-editing.

</details>

#### 2026-06-28 - RAGA: Real Time Ray Traced Gaussian Shadow Casting for 3DGS Avatar-Scene Interaction

**Authors:** Aymen Mir, Riza Alp Guler, Jian Wang, Peter Wonka, Bing Zhou, Gerard Pons-Moll
**Links:** [abs](https://arxiv.org/abs/2606.29329) - [pdf](https://arxiv.org/pdf/2606.29329)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** mesh reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RAGA: Real Time Ray Traced Gaussian Shadow Casting for 3DGS Avatar-Scene Interaction
- 作者：Aymen Mir, Riza Alp Guler, Jian Wang, Peter Wonka, Bing Zhou, Gerard Pons-Moll
- 出版日期：2026-06-28
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.29329

### 一句话总结
本文提出一种名为RAGA的实时光线追踪高斯阴影投射方法，能够在无需网格重建的前提下，为3D高斯泼溅（3DGS）虚拟化身与场景交互场景生成物理合理的阴影。

### 研究问题
如何在3DGS场景中为单个或多个动画化身及其与物体的交互生成物理合理、时序稳定且无需网格重建的实时阴影。

### 核心思路/方法
- 完全在高斯空间中进行阴影计算，避免网格重建。
- 基于精确的射线-高斯线积分，对每个遮挡高斯体沿阴影射线积分不透明度剖面，并用理论最大值归一化，得到描述射线如何穿过遮挡体的权重，而非仅判断是否相交。
- 针对动画化身服装形变引起的时序方差，引入化身代理表示以稳定阴影投射，同时保持视觉保真度。
- 使用自定义CUDA内核集成NVIDIA OptiX框架实现，达到约50 FPS的实时性能。

### 主要贡献
- 提出首个完全在高斯空间内进行阴影计算的方法，无需网格重建。
- 引入基于确切射线-高斯线积分的阴影投射公式。
- 设计化身代理表示以减少动画形变带来的时序不稳定性。
- 通过自定义CUDA+OptiX实现达到约50 FPS的实时阴影渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法针对3DGS动态场景中阴影这一视觉关键问题，提出无网格的实时解决方案，在单/多化身及物体交互场景下验证了阴影的真实性和稳定性，对于从事3DGS实时渲染、虚拟人或交互式图形学的研究者有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We study the problem of physically plausible shadow casting when animating 3D Gaussian Splatting (3DGS) avatars, either individually or in multi-avatar and object-interaction scenarios, within existing 3DGS scenes. In contrast to prior methods that rely on binary hit tests and mesh-based shadow casters, our method performs shadow computation entirely in Gaussian space, without requiring any mesh reconstruction. We introduce RAGA, a Ray-Traced Gaussian Shadow Casting formulation based on exact ray-Gaussian line integrals. For each occluding Gaussian, we integrate the opacity profile along the shadow ray and normalize by the theoretical maximum integral, producing a weight that captures how the ray traverses the occluder rather than merely whether an intersection occurred. To reduce temporal variance from clothing deformations in animated avatars, we further introduce an avatar proxy representation that stabilizes shadow casting while preserving visual fidelity. We implement RAGA using custom CUDA kernels integrated with the NVIDIA OptiX framework; as such, our shadow tracer runs at rates of about 50 FPS. We evaluate on single-avatar, multi-avatar, and avatar-object interaction scenarios across multiple datasets, demonstrating substantially improved shadow realism, temporal stability, and scene coherence. Our project page is available at https://miraymen.github.io/raga/.

</details>

#### 2026-06-28 - Occlusion-Robust Multi-Object Decoupling for Physics-Based Interaction

**Authors:** Xin Dong, Wenfeng Deng, Yansong Tang
**Links:** [abs](https://arxiv.org/abs/2606.29303) - [pdf](https://arxiv.org/pdf/2606.29303)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** geometric reasoning, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Occlusion-Robust Multi-Object Decoupling for Physics-Based Interaction  
- 作者：Xin Dong, Wenfeng Deng, Yansong Tang  
- 出版日期：2026-06-28  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2606.29303  

### 一句话总结
提出一种无需掩码的稀疏、遮挡视图下的多物体3D重建方法，结合3D高斯泼溅与联合得分蒸馏采样，生成可用于物理模拟的完整物体。

### 研究问题
如何从稀疏、存在遮挡的真实世界视图中对多个物体进行无掩码的、无损的3D重建，并使其能用于基于物质点法的物理交互模拟。

### 核心思路/方法
1. **多物体解耦建模**：将多物体因遮挡和视角有限导致的“耦合”问题，形式化为稀疏视图重建问题。  
2. **基础表示与实例分割**：以3D高斯泼溅为基础表示，利用SAM2训练的分割场获取粗略的实例划分。  
3. **联合得分蒸馏采样**：集成参考视图监督与新颖视图合成，结合2D/3D扩散先验指导纹理保真度和3D一致性，无需依赖掩码重建碎片化几何。  
4. **几何先验正则化**：引入物体内和物体间相似性等几何感知先验，约束几何推理过程。

### 主要贡献
- 提出一种无掩码、对遮挡鲁棒的多物体3D重建方法，可从稀疏视角生成完整、可直接用于物理模拟的物体。
- 通过联合得分蒸馏采样方法替代传统掩码依赖，同时利用扩散先验保持纹理和几何一致性。
- 在合成与真实数据集上验证了方法能实现逼真的动态交互。

### 局限性
摘要未提供足够信息，无法判断该方法的局限性（如计算开销、对极端遮挡的处理效果等）。

### 阅读优先级
**高**  
理由：该方法针对多物体稀疏视图重建与物理交互这一实际挑战，提出无掩码的创新方案，结合了扩散先验与几何正则化，在计算机视觉与物理模拟交叉领域具有潜在应用价值。摘要实验部分提到在合成与真实数据集上验证效果，表明有一定实用性。

</details>

<details>
<summary>Abstract</summary>

We propose a mask-free method for lossless multi-object 3D reconstruction from sparse and occluded real-world views, enabling physically plausible interaction via Material Point Method (MPM) simulation. Our key insight is that object coupling stems from occlusion and limited viewpoints, which we address by formulating multi-object decoupling as a sparse-view reconstruction problem. Using 3D Gaussian Splatting as base representation, we first obtain coarse instance partitions with a SAM2-trained segmentation field. Rather than relying on masks, we reconstruct fragmented geometries by leveraging a joint Score Distillation Sampling (SDS) process, which integrates reference-view supervision with novel-view synthesis guided by 2D and 3D diffusion priors to enforce both texture fidelity and 3D consistency. Furthermore, we incorporate geometry-aware priors such as intra-object and inter-object similarity to regularize geometric reasoning. Experimental results demonstrate that our method produces complete, simulation-ready 3D objects without requiring manual masks, enabling realistic dynamic interactions on both synthetic and real-world datasets.

</details>

#### 2026-06-28 - MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments

**Authors:** Qixin Xiao
**Links:** [abs](https://arxiv.org/abs/2606.29237) - [pdf](https://arxiv.org/pdf/2606.29237)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** SLAM, Gaussian Splatting, scene representation, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments
- 作者：Qixin Xiao
- 出版日期：2026-06-28T06:51:17Z
- 分类：主类别：神经场景表示与渲染；次类别：具身/机器人/AR应用
- 链接：摘要：https://arxiv.org/abs/2606.29237；PDF：https://arxiv.org/pdf/2606.29237

### 一句话总结
MoPe通过引入“运动持久性”原则，利用历史动态先验与当前帧证据的贝叶斯融合，改进了单目高斯SLAM在动态环境中的地图鲁棒性，减少了鬼影伪影。

### 研究问题
现有单目高斯溅射SLAM方法将动态区域视为逐帧观测，导致表示无记忆性；当动态对象减速、停顿或重新出现时，地图会吸收动态内容并产生持久鬼影伪影。核心问题是如何在场景表示中保持动态状态的时序一致性。

### 核心思路/方法
1. 提出“运动持久性”原则：对象的动态身份应跨时间持久，而非每帧独立重新判定。
2. 实现内存感知不确定性滤波器（MoPe）：将历史动态后验通过几何一致的SE(3)变换传播，并与当前帧证据使用有界贝叶斯对数几率更新融合。
3. 生成的持久后验用于引导跟踪、建图、动态感知高斯插入以及高斯级后清理。

### 主要贡献
1. 从表征层面指出动态性不是瞬时外观属性，而是由运动历史定义的时序属性。
2. 提出MoPe，一种基于运动持久性的内存感知不确定性滤波器，将动态状态的历史信息集成到表示中。
3. 在Wild-SLAM、Bonn和TUM序列上验证了MoPe提高了跟踪鲁棒性并减少了鬼影残留，尤其在动态人体场景中效果最显著。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：本文针对动态环境下单目高斯SLAM的鬼影问题提出了一种新颖的时序融合机制，具有明确的理论创新（运动持久性原理）和实验验证，对从事SLAM、动态场景重建的研究者有一定参考价值；但读者若仅关注纯静态场景或实时性要求极高的应用，优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

Robust robot autonomy depends on scene representations that remain stable enough to support localization, navigation, and downstream decision making in dynamic environments. Monocular Gaussian Splatting SLAM provides high-fidelity mapping, but current uncertainty-aware methods still treat dynamic regions largely as per-frame observations. This makes the representation effectively memoryless: when a pedestrian slows, pauses, or reappears after occlusion, the current frame may look static, allowing dynamic content to be absorbed into the map and leaving persistent ghosting artifacts. We argue that this failure reflects a representation-level mismatch. Dynamic-ness is not an instantaneous appearance property, but a temporal property defined by motion history. Building on this view, we introduce Motion Permanence: the principle that an object's dynamic identity should persist over time rather than be re-decided from each frame independently. We realize this principle in MoPe, a memory-aware uncertainty filter for monocular Gaussian mapping. MoPe propagates the historical dynamic posterior through geometry-consistent SE(3) warping and fuses it with current-frame evidence using bounded Bayesian log-odds updates. The resulting persistent posterior guides tracking, mapping, dynamic-aware Gaussian insertion, and Gaussian-level post-cleanup. On Wild-SLAM, Bonn, and TUM sequences, MoPe improves tracking robustness and reduces residual ghosting, with the strongest gains on dynamic-human scenes that most directly violate the memoryless assumption. These results show that maintaining temporal dynamic state inside the scene representation is a practical step toward more reliable representation-centric autonomy in changing real-world environments.

</details>

#### 2026-06-26 - StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views

**Authors:** Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie
**Links:** [abs](https://arxiv.org/abs/2606.28321) - [pdf](https://arxiv.org/pdf/2606.28321)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views
- 作者：Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie
- 出版日期：2026-06-26
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.28321

### 一句话总结
StructSplat提出了一个无需相机参数的前馈式可泛化3D高斯重建框架，通过结构化表征分离几何、语义与纹理线索，在稀疏视图场景下显著提升渲染质量。

### 研究问题
如何在不依赖相机标定或场景级优化的前提下，从未标定的稀疏多视图图像中高效、高保真地重建可泛化的3D高斯辐射场。

### 核心思路/方法
1. **结构化表征**：将几何、语义和纹理线索赋予明确角色，组织为结构化表示，避免在统一骨干网络中纠缠。
2. **像素对齐特征注入**：从2D观测中提取像素对齐特征，实现精确的纹理建模。
3. **语义感知先验**：引入语义先验以增强全局一致性。
4. **相机对齐策略**：设计防止信息泄漏的相机对齐机制，提升跨场景泛化能力。

### 主要贡献
- 首个在无相机参数条件下实现前馈式可泛化3D高斯重建的框架。
- 提出结构化表征方法，将几何、语义与纹理线索解耦并显式建模。
- 在DL3DV基准上PSNR达28.045，超越AnySplat（22.377）5.67 dB；跨数据集评测中，在ACID和RealEstate10K上分别比AnySplat高1.94 dB和1.72 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该方法解决了现有可泛化新视角合成方法对相机参数和场景级优化的依赖，在稀疏无标定视图场景下取得显著性能提升（DL3DV上+5.67 dB PSNR），且具备跨数据集泛化能力，对3D场景理解与渲染领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We present StructSplat, a feed-forward and generalizable 3D Gaussian reconstruction framework that operates directly on uncalibrated images without requiring camera parameters. Existing methods either rely on per-scene optimization or assume known camera poses, and often entangle geometry and appearance within a unified backbone, limiting reconstruction fidelity and generalization. Our key idea is to adopt a structured representation that organizes geometry, semantic, and texture cues with explicit roles in the reconstruction process. Specifically, we introduce a pixel-aligned feature injection mechanism to enable accurate texture modeling from 2D observations, incorporate semantic-aware priors to improve global consistency, and design a camera alignment strategy to prevent information leakage and improve generalization. Experiments show that our method significantly outperforms prior approaches on challenging benchmarks. On DL3DV, our method achieves 28.045 PSNR, surpassing AnySplat (22.377) by +5.67 dB. In cross-dataset evaluation, our method achieves +1.94 dB over AnySplat on ACID and +1.72 dB on RealEstate10K. Project page: https://structsplat.github.io Code: https://github.com/J-C-Zhao/StructSplat

</details>

#### 2026-06-25 - Sculpting NeRF Geometry: Human-Preference Fine-Tuning of a 3D-Aware Face GAN

**Authors:** Archer Moore, Mingming Gong, Liam Hodgkinson
**Links:** [abs](https://arxiv.org/abs/2606.27305) - [pdf](https://arxiv.org/pdf/2606.27305)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sculpting NeRF Geometry: Human-Preference Fine-Tuning of a 3D-Aware Face GAN
- 作者：Archer Moore, Mingming Gong, Liam Hodgkinson
- 出版日期：2026-06-25
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.27305

### 一句话总结
本文提出直接从人类偏好学习的奖励信号微调预训练3D感知生成对抗网络（EG3D）的NeRF密度场，无需网格或形状先验，即可改善人脸几何质量。

### 研究问题
如何在无外部网格、形状先验或文本条件的情况下，仅通过人类偏好反馈直接优化隐式3D表示（NeRF）的几何结构。

### 核心思路/方法
1. 基于预训练的3D感知人脸GAN（EG3D）进行微调。
2. 奖励模型直接从NeRF的连续密度场（σ值）学习，无需预训练，仅需少量偏好样本。
3. 使用密度一致性约束保持2D外观相似性，几何调整仅由密度场的奖励信号驱动。
4. 作为概念验证，仅使用单个标注者的偏好进行训练。

### 主要贡献
1. 首次直接对NeRF密度场进行人类偏好微调，避免转换为网格或其他显式表示。
2. 奖励模型简单易训练，无需预训练，在小样本偏好数据上有效。
3. 在无条件3D人脸GAN上验证方法，用户偏好比较中胜率74.4%，同时量化了分布代价（FID-50k从4.09升至6.66）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法提出了一种新颖的、无需网格/文本条件的3D几何优化框架，直接通过人类偏好调整NeRF密度场，具备实际应用潜力（如3D内容创作），且实验验证了用户偏好显著提升。尽管存在分布代价，但全文对NeRF社区和生成模型微调领域有参考价值。

</details>

<details>
<summary>Abstract</summary>

Reinforcement learning from human feedback (RLHF) for 3D generation is now established across a number of works, but most existing pipelines optimise explicit surface representations, often by converting radiance fields into meshes and training heavily on surface-supervised data. We instead fine-tune a pretrained 3D-aware generative model directly from a learned reward over radiance-field density ($σ$) values, with no externally supplied mesh or shape prior. The reward model requires no pretraining, trains easily on a small set of preference samples, and yields robust improvement in 3D geometry. Working on an unconditional 3D-aware face GAN (EG3D), our reward reads the continuous 3D density field of the neural radiance field (NeRF) directly and supplies a geometry-only learning signal, requiring neither text conditioning, mesh extraction, nor multi-view rendering. A density-consistency constraint keeps the 2D appearance qualitatively similar while the geometry is reshaped, at a measurable but bounded distributional cost (FID-50k rises from 4.09 to 6.66): the fine-tuned generator, trained from the preferences of a single annotator as a proof of concept, produces face geometries preferred by users in 74.4% of pairwise comparisons.

</details>

#### 2026-06-25 - Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction

**Authors:** Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung
**Links:** [abs](https://arxiv.org/abs/2606.26985) - [pdf](https://arxiv.org/pdf/2606.26985)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction
- 作者：Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung
- 出版日期：2026-06-25
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.26985；PDF：https://arxiv.org/pdf/2606.26985

### 一句话总结
Vis4GS是一个用于3D高斯溅射重建的多视图可视化分析工具，通过连接伪影、高斯属性、视角覆盖度与训练历程，支持基元级别的重建故障诊断，并经过用户研究验证其易用性与理解能力优于原始3DGS查看器。

### 研究问题
3D高斯溅射（3DGS）虽支持快速训练与实时渲染，但其优化过程难以解释。现有查看器主要展示最终重建场景，无法解释高斯属性如何导致可见伪影或如何在训练过程中演变。

### 核心思路/方法
基于原始3DGS查看器与训练框架，构建了四个相互关联的可视化视图：
1. 交互式高斯分析视图：支持高斯选择与伪影评分。
2. 属性时间线视图：展示高斯属性随时间变化。
3. 高斯稠密化树视图：可视化复制、分裂、剪枝等谱系事件。
4. 日志与控制面板。
系统还集成了视角覆盖度分析与多尺度谱系探索，通过将场景级伪影与基元级证据及优化历史相连，提供结构化诊断流程。

### 主要贡献
1. 提出Vis4GS工具，首次在基元级别对3DGS重建伪影进行可视化诊断。
2. 设计四个联动视图，覆盖伪影评分、属性演化、稠密化谱系与视角覆盖度。
3. 用户研究表明Vis4GS在可用性与伪影理解上优于原始3DGS查看器。
4. 提供超越最终图像检查与全局指标的故障诊断工作流。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工具主要服务于3DGS实践中的调试与诊断，对关注3DGS内部分析或可视化系统设计的读者有参考价值；但摘要未提供定量性能比较或技术实现细节，理论贡献有限，适合中等优先级阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) supports fast training and real-time rendering, but its optimization process remains difficult to interpret. Existing viewers mainly expose the final reconstructed scene and offer limited support for explaining how Gaussian properties contribute to visible artifacts or evolve during training. We present Vis4GS, a multi-view visual analytics tool for primitive-level diagnosis of 3DGS reconstruction artifacts. Built on the original 3DGS viewer and training framework, Vis4GS links rendered artifacts to Gaussian properties, View Coverage, training progress, and Gaussian genealogy through four linked views: an interactive Gaussian analysis view, a property timeline view, a Gaussian densification tree view, and a log and control panel. The system supports Gaussian selection, blur and needle-like artifact scoring, View Coverage analysis, and multiscale genealogy exploration of clone, split, prune, and clone-split events. By connecting scene-level artifacts with primitive-level evidence and optimization history, Vis4GS enables a structured workflow for diagnosing reconstruction failures beyond final-image inspection and global metrics. A user study also shows that Vis4GS provides stronger support for usability and artifact understanding than the original 3DGS viewer.

</details>

#### 2026-06-25 - Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting

**Authors:** Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang
**Links:** [abs](https://arxiv.org/abs/2606.26754) - [pdf](https://arxiv.org/pdf/2606.26754)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feature matching, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting
- 作者：Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang
- 出版日期：2026-06-25T08:36:50Z（注：日期在论文输入中标记为2026年，可能为录入错误或未来日期，但按原信息输出）
- 分类：Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2606.26754；PDF: https://arxiv.org/pdf/2606.26754

### 一句话总结
本文提出一种基于最优运输的容量控制框架，通过半平衡最优运输问题约束风格特征的列容量，从而改善3D Gaussian Splatting的多视角风格化一致性与稳定性。

### 研究问题
如何在不牺牲场景语义结构的前提下，使3DGS在不同视角下稳定分配风格特征，避免多对一特征重用和跨视角不一致的问题。

### 核心思路/方法
1. 将局部风格匹配重新表述为半平衡最优运输问题，引入可调强度的显式列容量约束，以缓解多对一匹配并实现可控的风格特征分配。
2. 提出新颖的跨视角匹配引导机制，约束场景内容与风格模式之间的对应关系，增强跨视角连贯性。
3. 引入若干几何正则化方法改进基础3DGS，使其在风格化过程中能表示更精细的纹理。

### 主要贡献
1. 提出基于最优运输的容量控制框架，通过列容量约束实现多视角稳定的风格化。
2. 设计跨视角匹配引导机制，提升风格化在视图间的一致性。
3. 引入几何正则化增强3DGS，使其在风格化时保留细粒度纹理与语义结构。

### 局限性
摘要未提供足够信息，未讨论方法的计算开销、场景复杂度的适用边界，或可能的失败案例。

### 阅读优先级
中。理由：该方法针对3D风格化中多视角一致性的痛点提出了理论新颖的解决方案（最优运输+容量控制），但属于特定任务优化，对于不从事3D神经渲染或风格化的读者相关性较低；且摘要未提供定量比较或实验细节，需进一步阅读正文评估有效性。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting (3DGS) provides an efficient and explicit representation for novel view synthesis, enforcing stylistic coherence across viewpoints remains challenging. Existing 3D stylization methods typically apply 2D feature-matching losses independently per rendered view, which leads to unstable style allocation, many-to-one feature reuse, and limited cross-view consistency. We propose a capacity-controlled framework for multi-view stylization of 3DGS, grounded in optimal transport. Specifically, we reformulate local style matching as a semi-balanced optimal transport problem. By introducing explicit column-capacity constraints with tunable strength, our formulation mitigates many-to-one matching and enables controllable allocation of style features. This transport-based objective provides a principled mechanism for balancing feature coverage and stylistic diversity while maintaining stable correspondences across viewpoints. To further enhance cross-view coherence, we incorporate a novel cross-view matching guidance to constrain correspondences between scene content and style patterns. In addition, we introduce several geometric regularizations to enhance the vanilla 3DGS, thereby enabling optimized Gaussian primitives to represent finer-grained textures during stylization. Extensive experiments demonstrate that our approach significantly improves multi-view stylistic consistency and produces stable, expressive 3D stylizations while preserving the core semantic structure of the scene.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-30 - DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation

**Authors:** Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang
**Links:** [abs](https://arxiv.org/abs/2606.31918) - [pdf](https://arxiv.org/pdf/2606.31918)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, autonomous driving, driving scene, simulation

<details>
<summary>Abstract</summary>

A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes. This process enhances scene diversity and facilitates the creation of various corner cases for testing and improving autonomous driving models. However, existing methods often rely on pre-reconstructed 3D assets, which frequently lead to lighting inconsistencies between the inserted foreground and the background. Moreover, the reliance on limited, manually-curated 3D assets hinders large-scale deployment. To address these challenges, we propose DriveWeaver, a novel framework for controllable vehicle insertion in autonomous driving simulation. Specifically, for a masked target insertion area, DriveWeaver performs video inpainting conditioned on vehicle point clouds to generate high-quality, temporally consistent vehicles. This video-inpainting-based approach ensures seamless blending between the foreground and background, while the readily available point cloud conditions enable superior generalization. To support long-term generation, we further design a global-to-local hierarchical inpainting strategy, ensuring the consistent identity and appearance of the inserted vehicles. Meanwhile, we extract explicit 3D Gaussian representations of the inserted vehicles through an urban reconstruction pipeline to enable real-time rendering for autonomous driving simulation. Extensive experiments across diverse datasets demonstrate that our method outperforms existing baselines in visual realism and geometric consistency, providing a robust tool for scalable autonomous driving scene augmentation.

</details>

#### 2026-06-30 - MV-GEL: Language-Driven Multi-View Geometric Entity Localization on Meshes

**Authors:** Kartik Bali, Roland Aydin
**Links:** [abs](https://arxiv.org/abs/2606.31533) - [pdf](https://arxiv.org/pdf/2606.31533)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, simulation

<details>
<summary>Abstract</summary>

Identifying and grounding precise geometric entities, such as edges, planar regions, and curved surfaces within 3D objects, is foundational to computer-aided design (CAD), robotic manipulation, and scientific simulation. Although modern Vision Language Models (VLMs) have advanced referring segmentation (RIS) in the image domain, extending such language-driven localization to structured 3D geometry is substantially harder. The 3D object appearance is highly sensitive to viewpoints; a single perspective may render a target entity clearly observable, while another may suffer from severe occlusion or foreshortening. In this work, we attempt to solve these challenges with MV-GEL (Multi-View Geometric Entity Localization), a framework for localizing fine-grained geometric entities on polygon meshes from natural language queries. Our key insight is that reliable CAD entity (i.e., faces, edges or solids) localization depends on selecting views that make the queried entity maximally interpretable. We introduce GELviews, a prompt-conditioned ranking module that prioritizes viewpoints based on language prompted observability of geometric CAD entities. Selected views are processed by a VLM-based reasoning segmentation backbone, and predicted masks are lifted to the corresponding meshes via geometry-aware ray casting. Our framework is completely CAD agnostic and relies only on 3D meshes. Experiments show up to a 1.7X improvement in face-level IoU and over 4.5X gains in edge-level F1 compared to vanilla baselines, substantially outperforming CLIP-based and random view sampling, particularly for thin and view-sensitive structures.The dataset, code and trained checkpoints are available at https://github.com/kbali1297/MV-GEL.

</details>

#### 2026-06-29 - Knowledge-Driven Dimension Estimation from a Single Image -3D Asset Generation Technology for Digital Twin Construction

**Authors:** Hidenori Sakaniwa, Akihito Akai, Akihiko Hyodo
**Links:** [abs](https://arxiv.org/abs/2606.30896) - [pdf](https://arxiv.org/pdf/2606.30896)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, digital twin, simulation

<details>
<summary>Abstract</summary>

In the verification of in-vehicle cameras, simulation technology using virtual spaces has advanced, enabling pre-evaluation of false detections and missed detections in various scenarios. However, discrepancies in the scale of the object being verified between the virtual and real environments can lead to a decrease in camera recognition performance. For traffic signs installed at high altitudes, distance measurement using LiDAR or stereo cameras is difficult, requiring size estimation from monocular images. This paper proposes a method for estimating the scale of an object by decomposing it into multiple structural elements and integrating external knowledge regarding design rules, geometric relationships, and conventional dimensions. Specifically, this method detects each component from a monocular image and estimates the size of each component by considering its structural relationships and dimensional consistency with surrounding elements. Furthermore, it generates a 3D asset of the object by reconstructing the estimated components. This method makes it possible to place 3D assets with a scale approximating the real environment within a digital twin space and is expected to contribute to improving the verification accuracy of in-vehicle cameras for autonomous driving in virtual environments.

</details>

#### 2026-06-29 - UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image

**Authors:** Mohamed el Amine Boudjoghra, Ivan Laptev, Angela Dai
**Links:** [abs](https://arxiv.org/abs/2606.30608) - [pdf](https://arxiv.org/pdf/2606.30608)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image
- 作者：Mohamed el amine boudjoghra, Ivan Laptev, Angela Dai
- 出版日期：2026-06-29T17:44:53Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要URL: https://arxiv.org/abs/2606.30608；PDF: https://arxiv.org/pdf/2606.30608

### 一句话总结
本文提出首个基于辩论驱动智能体方法的零样本关节3D物体重建框架，能够从文本或图像输入中推断关节结构并重构完整几何，包括隐藏内部和运动一致的状态。

### 研究问题
如何从稀疏观测（文本或单张图像）中零样本重建任意关节3D物体的完整结构、关节运动、隐藏几何及内部结构。

### 核心思路/方法
采用双层智能体辩论机制：高层智能体利用视觉语言和视频模型推理物体语义与运动；低层智能体估计关节参数与交互点。通过两轮结构化辩论：第一轮利用全局-局部不一致性触发讨论，第二轮将智能体锚定在自由生成的视频中。最终，基于协商一致的关节信息，驱动视频先验让每个部件沿运动路径暴露原本不可见的遮挡内部与几何。

### 主要贡献
1. 首次提出辩论驱动的智能体方法解决零样本关节3D物体重建问题。
2. 联合推理关节参数与完整几何，无需监督数据或预训练先验。
3. 利用自由生成的视频先验，恢复高保真几何、内部结构及运动一致的状态，超越直接可见表面。

### 局限性
摘要未提供足够信息。无法从摘要中确认方法在复杂关节类型、极端遮挡或计算效率方面的具体限制。

### 阅读优先级
**高**。理由：该工作解决了具身智能、机器人和虚拟现实中的核心难题——零样本、无监督的关节物体重建，方法具有创新性（辩论智能体+视频生成先验），且发表于2026年，代表前沿方向，对相关领域研究者有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging. Existing approaches remain largely constrained by lack of supervised data or lack the priors needed to reliably recover articulation, hidden geometry, and internal object structure. We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry revealed under articulation. High-level agents reason about object semantics and motion using knowledge from vision-language and video models, while low-level agents estimate articulation parameters and interaction points; together, they engage in a two-round structured debate that first exploits global--local disagreement and then grounds the agents in freely generated video. The same video prior, conditioned on the agreed articulation, then drives each part through its motion to expose occluded interiors and geometry that cannot be inferred from a single static view. By combining agentic reasoning with a video generative prior, our approach jointly infers articulation and reconstructs complete 3D articulated objects, producing high-fidelity geometry, internal structure, and motion-consistent states beyond directly observed surfaces.

</details>

#### 2026-06-29 - CSAR: Containerized System Architecture for Robotics

**Authors:** Ambrosio-Cestero, Gregorio, Galindo Andrades, Cipriano, Gonzalez-Jimenez, Javier, Ruiz-Sarmiento, Jose-Raul
**Links:** [abs](https://arxiv.org/abs/2606.30293) - [pdf](https://arxiv.org/pdf/2606.30293)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, robotics, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CSAR: Containerized System Architecture for Robotics
- 作者：Ambrosio-Cestero, Gregorio, Galindo Andrades, Cipriano, Gonzalez-Jimenez, Javier, Ruiz-Sarmiento, Jose-Raul
- 出版日期：2026-06-29
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.30293

### 一句话总结
本文提出CSAR，一种专为机器人团队设计的基于容器的架构，通过系统容器化、ROS 2通信和三层边缘基础设施，在分布式环境中实现依赖隔离、资源共享和可复现的实验。

### 研究问题
如何解决多用户机器人软件开发中面临的依赖隔离、兼容性、可复现性、专用硬件共享以及在异构环境（包括边缘-云连续体）中部署等挑战。

### 核心思路/方法
提出一种以容器为中心的架构（CSAR），结合了LXC/LXD系统容器化、ROS 2/DDS通信以及三层边缘基础设施（包括基础设施核心层、平台与多用户编排层、计算与加速层），将计算组织为硬件亲和、持久的执行环境，并与实验工作负载的解耦。

### 主要贡献
- 提出CSAR架构，为机器人团队提供强隔离、受控资源共享和拓扑感知网络。
- 通过真实学术机器人实验室的部署以及边缘卸载3D SLAM和GPU加速语义映射等代表性用例，验证了该架构的有效性。
- 结果表明CSAR简化了软件集成，提升了共享计算资源的利用率，并有利于安全原型设计、可复现及协作实验。
- 提供了开源实现，包括部署模板、配置文件和文档。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对机器人软件开发中实际且紧迫的集成与部署问题（依赖隔离、可复现性等），提出了一个完整且经过实际部署验证的容器化架构。对于从事机器人系统开发、分布式系统或边缘计算的研究者与工程师具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Robotic applications increasingly rely on distributed computational infrastructures that combine embedded devices, edge servers, and cloud resources. This evolution, together with the collaborative nature of robotics projects, has made the development, integration, deployment, and long-term operation of robotic systems significantly more complex. In practice, multi-user robotics software teams face persistent challenges related to dependency isolation, compatibility, reproducibility, efficient sharing of specialized hardware, and deployment across heterogeneous environments. In this paper, we present CSAR (Containerized System Architecture for Robotics), a container-centric architectural framework designed specifically for robotics teams and the edge-cloud continuum. CSAR combines LXC/LXD-based system containerization, ROS 2/DDS-based communication, and a three-layer edge infrastructure to organize computation into hardware-affine, persistent execution environments that remain decoupled from the volatility of experimental workloads. Through its Infrastructure Core, Platform and Multi-User Orchestration, and Compute and Acceleration layers, CSAR provides strong isolation, controlled resource sharing, and topology-aware networking for distributed robotic applications. To demonstrate its validity, we describe a real deployment of CSAR in an academic robotics laboratory and evaluate it through representative use cases involving edge-offloaded 3D SLAM and GPU-accelerated semantic mapping. The results indicate that CSAR simplifies software integration, improves the utilization of shared computational resources, and facilitates safe prototyping, as well as reproducible and collaborative experimentation in robotics teams. The implementation described in this paper, including deployment templates, configuration files, and documentation, is available at https://github.com/goyoambrosio/CSAR.

</details>

#### 2026-06-29 - Learning Cross-view Correspondences for Geo-localization on Planetary Surfaces

**Authors:** Hong Minh Nguyen, Marcus Märtens, Tat-Jun Chin
**Links:** [abs](https://arxiv.org/abs/2606.29821) - [pdf](https://arxiv.org/pdf/2606.29821)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Cross-view Correspondences for Geo-localization on Planetary Surfaces
- 作者：Hong Minh Nguyen, Marcus Märtens, Tat-Jun Chin
- 出版日期：2026-06-29
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2606.29821 ； PDF：https://arxiv.org/pdf/2606.29821

### 一句话总结
本文为行星表面跨视角地理定位构建了一个新基准数据集，并验证了基于Transformer的定位方法在该领域的有效性。

### 研究问题
如何在没有卫星定位系统的行星表面，通过匹配地表全景图与轨道俯视图来实现全局位置感知。

### 核心思路/方法
1. 构建数据集：基于高分辨率月球地形模型，物理渲染生成了包含10,438个地面360°全景图与精确对齐的俯视图的基准，并提供重叠瓦片用于研究偏离中心定位。
2. 方法验证：使用基于Transformer的现有跨视角地理定位方法，从头开始训练并在该数据集上报告检索准确率。

### 主要贡献
- 提出了一个专门用于行星表面跨视角地理定位的新基准数据集，包含配对的360°全景图与俯视图。
- 实验证明了基于学习的跨视角定位方法可成功应用于行星表面领域，为无卫星导航提供了视觉替代方案。

### 局限性
摘要未提供足够信息（未讨论方法的失败案例、计算代价、泛化到其他行星或光线条件的表现等）。

### 阅读优先级
中
理由：该工作主要贡献在于数据集构建和基准验证，方法上未提出新架构，但对行星探索领域的视觉定位问题有直接应用价值。

</details>

<details>
<summary>Abstract</summary>

Maintaining global position awareness is a fundamental challenge for planetary surface exploration, since satellite-based positioning systems are unavailable and onboard odometry drifts over time. Although orbital mapping products, such as overhead imagery and terrain-derived maps, provide global context, aligning them with surface observations is challenging due to large viewpoint differences, low texture, repetitive terrain, and drastic changes in appearance caused by varying illumination and topography. We introduce a new cross-view geo-localization benchmark built from physically rendered surface panoramas and overhead tiles derived from a high-resolution lunar terrain model. Our dataset contains 10438 ground views rendered as 360$^\circ$ surface panoramas with matching overhead images precisely centered at the same location. Additionally, a set of overlapping tiles is provided to study off-center localization with multiple plausible candidates per panorama. We study the performance of a state-of-the-art transformer-based geo-localization method on our data, by training it from scratch and reporting retrieval accuracy. Our results demonstrate that learning-based cross-view localization methods can be successfully applied to the domain of planetary surfaces, providing a vision-based alternative to global navigation satellite systems.

</details>

#### 2026-06-27 - Flow Matching in Feature Space for Stochastic World Modeling

**Authors:** Francois Porcher, Nicolas Carion, Karteek Alahari, Shizhe Chen
**Links:** [abs](https://arxiv.org/abs/2606.29059) - [pdf](https://arxiv.org/pdf/2606.29059)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Flow Matching in Feature Space for Stochastic World Modeling
- 作者：Francois Porcher, Nicolas Carion, Karteek Alahari, Shizhe Chen
- 出版日期：2026-06-27
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.29059

### 一句话总结
本文提出FlowWM，一种在预训练高维特征空间（如DINOv3）中执行流匹配的随机世界模型，通过可微分一步投影机制解决高维特征上的训练与推理困难，提升了感知性能与未来预测的多样性。

### 研究问题
如何在高维预训练特征空间中构建随机世界模型，使得模型既能准确预测多模态未来，又能保留对下游感知任务有用的信息？

### 核心思路/方法
1. 在预训练特征空间（如DINOv3）中直接进行流匹配（Flow Matching），替代传统的VAE低维重建潜在空间或确定性预测器。
2. 针对高维特征空间设计适合的扩散/流匹配配方，克服标准扩散方案在此场景下的次优性。
3. 提出可微分的一步投影机制（differentiable one-step projection），实现兼具时间一致性和任务驱动目标的高效训练。

### 主要贡献
- 提出FlowWM，首个在高维预训练特征空间执行流匹配的随机世界模型，兼顾预测准确性与多样性。
- 探索并验证了特征空间流匹配所需的关键设计选择。
- 在合成基准和真实世界基准FuturePerception上，证明了FlowWM在感知性能、模态覆盖率和时间鲁棒性上的提升。

### 局限性
摘要未提供足够信息。仅提及了模型架构、训练目标（时间一致性、任务驱动）与评估基准，未说明具体失败案例、计算资源需求、对特征空间类型的依赖性或与强基线（如VAE模型、确定性预测器）的定量对比细节。

### 阅读优先级
高  
理由：该工作针对世界模型中的核心矛盾——预测准确性与多样性——提出了新颖的路径（特征空间流匹配），并在真实和合成基准上验证了有效性。对于关注随机世界建模、特征空间生成以及机器人/AR应用的研究者具有较高参考价值。摘要中方法描述清晰且贡献点明确。

</details>

<details>
<summary>Abstract</summary>

World modeling requires forecasting uncertain futures while preserving information useful for downstream perception. Existing visual world models often struggle to satisfy both goals: VAE-based stochastic models operate in low-dimensional reconstruction latents, which can limit perception performance, while deterministic predictors using strong pretrained features collapse multimodal futures into a single blurry mean. In this work, we propose FlowWM, a stochastic world model that performs flow matching directly within pretrained feature space (e.g., DINOv3). This is challenging because pretrained features are substantially high-dimensional, making standard diffusion recipes suboptimal. To address this, we investigate the design choices needed for feature-space flow matching and introduce a differentiable one-step projection mechanism that enables efficient training with temporal consistency and task-driven objectives. We evaluate FlowWM on two benchmarks: a synthetic benchmark for systematic evaluation of accuracy and diversity, and a real-world benchmark FuturePerception. FlowWM improves perception performance, mode coverage, and horizon robustness, validating our proposed design for stochastic world modeling in high-dimensional feature spaces.

</details>

#### 2026-06-25 - EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting

**Authors:** Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, Zhe Liu, Hengshuang Zhao
**Links:** [abs](https://arxiv.org/abs/2606.27277) - [pdf](https://arxiv.org/pdf/2606.27277)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting
- 作者：Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, Zhe Liu, Hengshuang Zhao
- 出版日期：2026-06-25
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.27277

### 一句话总结
EO-WM 提出了一种物理信息引导的视频扩散Transformer模型，实现了在变化气象条件下对地球观测的多光谱概率预测，并通过两个诊断基准验证了其天气响应预测的准确性。

### 研究问题
如何在不完全观测、天气驱动的地球观测预测任务中，构建能捕捉预测不确定性并对气象强迫变化做出正确响应的世界模型。

### 核心思路/方法
1. **视角转换**：将EO预测视为部分观测、天气驱动的世界建模问题，气象信号作为条件，但由于观测稀疏和地表状态不可观测而存在不确定性。
2. **物理信息条件框架**：将气象强迫分解为气候基线、天气异常和累积物理应力（如持续热浪或干旱应力）信号，并通过不同的条件路径注入模型。
3. **模型架构**：采用视频扩散Transformer（Video Diffusion Transformer）作为基础，结合上述条件信号生成概率性多光谱预测。
4. **诊断基准**：设计了极端夏季基准（评估极端天气下植被退化预测的严重程度感知）和季节匹配对基准（测试不同天气强迫下的响应保真度）。

### 主要贡献
1. 提出了EO-WM模型，将物理信息条件框架引入视频扩散Transformer，实现概率性EO预测。
2. 引入两个新基准来评估模型对气象变化的正确响应行为，超越传统重建精度指标。
3. 实验显示，在预测NDVI下降幅度误差上相对降低5.63%，方向命中率相对提升7.80%，同时保持标准像素级指标的竞争力。

### 局限性
摘要未提供关于计算资源、数据依赖、模型泛化性、失败案例或潜在偏差等信息。未能基于摘要确定模型在无极端天气或低质量数据下的表现。

### 阅读优先级
**高**
理由：该论文针对地球观测预测中一个关键但未被充分建模的问题（天气驱动的不确定性响应），提出了有理论依据的方法和评估基准，并在核心指标上取得显著提升，对遥感与气候应用领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Earth Observation (EO) forecasting aims to predict future Earth surface dynamics from satellite observations under changing meteorological conditions. In this paper, we view this task as a partially observed, weather-driven world modeling problem, in which weather acts as a conditioning signal, while forecasting remains uncertain due to sparse observations and unobserved land-surface states. However, existing methods do not fully capture this setting: deterministic models collapse uncertainty into a single future prediction, while diffusion-based methods typically treat weather variables as undifferentiated conditioning signals, and existing benchmarks focus mainly on reconstruction accuracy rather than whether forecasts respond correctly to changed weather forcing.We introduce EO-WM, a video diffusion transformer for multispectral EO forecasting. EO-WM incorporates a physically informed conditioning framework that represents meteorological forcing through a climatological baseline, weather anomalies, and cumulative physical stress signals. Specifically, it separates baseline and anomaly through distinct conditioning pathways, and accumulates anomalous forcing over time to capture sustained heat and drought stress. To evaluate weather-response behavior beyond standard metrics, we introduce two diagnostic benchmarks: an Extreme Summer Benchmark for severity-aware prediction of vegetation degradation under extreme weather, and a Seasonal Matched-Pair Benchmark for testing response fidelity under changed weather forcing. Experiments show that EO-WM reduces the error in predicted Normalized Difference Vegetation Index (NDVI) decline amplitude by a relative 5.63% and improves directional hit rate by a relative 7.80%, while remaining competitive on standard pixel-level metrics. The benchmarks and model will be made open-source at https://github.com/Luo-Z13/EO-WM.

</details>

#### 2026-06-25 - UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping

**Authors:** Feng Pan, Chunran Zheng, Bing Xue, Yukang Cui, Jiayu Wen, Zhiyu Chen, Wei Wang
**Links:** [abs](https://arxiv.org/abs/2606.26928) - [pdf](https://arxiv.org/pdf/2606.26928)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, mapping, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping
- 作者：Feng Pan, Chunran Zheng, Bing Xue, Yukang Cui, Jiayu Wen, Zhiyu Chen, Wei Wang
- 出版日期：2026-06-25T12:03:29Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2606.26928, PDF: https://arxiv.org/pdf/2606.26928

### 一句话总结
本文提出一种利用RTK对准和不确定性感知因子图的多会话无人机点云地图粗到细优化系统，以解决大范围地图合并中长距离漂移与局部几何精度难以兼顾的问题。

### 研究问题
如何在大规模多会话无人机点云地图合并中，同时抑制长距离漂移并保持局部几何精度。

### 核心思路/方法
1. **初始合并**：基于场景图对多会话地图进行粗对齐。
2. **RTK时空对齐**：使用动态时间规整（DTW）估计时间偏移，并利用多输出高斯过程（MOGP）在不完整采样和帧丢失下恢复连续RTK约束。
3. **不确定性感知因子图**：将RTK约束与不确定性信息整合到统一的因子图中。
4. **局部优化**：通过迭代平面因子优化提升局部几何精度。

### 主要贡献
- 提出一种面向无人机场景的多会话点云地图合并系统，结合RTK对准与粗到细优化。
- 引入DTW和MOGP处理RTK数据的时空对齐问题，提升长距离稳定性。
- 利用不确定性感知因子图和平面因子细化同时提高全局一致性与局部精度。

### 局限性
- 摘要未提供具体的实验场景参数（如数据集大小、飞行时长、对比基线等），也未详细说明失败案例或假设条件，因此局限性信息不足。

### 阅读优先级
阅读优先级：中。  
理由：该方法针对无人机大范围地图合并的实用技术问题，思路明确且包含多种创新模块（如DTW、MOGP、不确定性因子图），适合对多传感器融合或地图建图感兴趣的读者；但摘要中未提供详细实验结果，若需深入评估效果需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Large-scale point cloud maps are essential for robotics and spatial intelligence tasks. UAVs provide an efficient means for large-scale map acquisition; however, due to limited flight endurance and onboard storage, mapping a large-scale scene within a single flight remains difficult. Existing multi-session map merging methods can extend the mapping range, yet in UAV scenarios they still struggle to simultaneously suppress long-range drift and preserve local geometric accuracy. To address this issue, an uncertainty-aware multi-session point cloud map merging and coarse-to-fine optimization system is proposed. The proposed method first performs initial multi-session map merging based on a scene graph, and then incorporates RTK observations through an RTK spatiotemporal alignment module, where temporal offsets are estimated using Dynamic Time Warping (DTW), and continuous RTK constraints are recovered using Multi-Output Gaussian Processes (MOGP) under incomplete sampling and frame dropouts. On this basis, a unified uncertainty-aware factor graph is constructed, and local geometric accuracy is further improved through iterative plane-factor refinement. Experiments on real-world datasets validate the effectiveness and robustness of the proposed method. To facilitate further research and development in the community, our code and dataset will be publicly released.

</details>

#### 2026-06-25 - OSC2Runner: OpenSCENARIO 2.x Compliant High-Fidelity AV Simulation in CARLA

**Authors:** Thoshitha Gamage, Lasanthi Gamage
**Links:** [abs](https://arxiv.org/abs/2606.26533) - [pdf](https://arxiv.org/pdf/2606.26533)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OSC2Runner: OpenSCENARIO 2.x Compliant High-Fidelity AV Simulation in CARLA
- 作者：Thoshitha Gamage, Lasanthi Gamage
- 出版日期：2026-06-25
- 分类：具身/机器人/AR应用
- 链接：arXiv abs: https://arxiv.org/abs/2606.26533

### 一句话总结
OSC2Runner是首个能在CARLA仿真器中原生执行OpenSCENARIO v2.x DSL的编排框架，通过多遍转译器将场景描述编译为行为树，实现了精确的确定性仿真。

### 研究问题
现有连续仿真框架缺乏对新兴ASAM OpenSCENARIO v2.x DSL的原生支持，导致基于场景的测试在运行v2.x逻辑时出现时空漂移、异步事件延迟及人工运动突变等问题，亟需一种能高保真执行v2.x场景的仿真方法。

### 核心思路/方法
该框架将场景翻译形式化为编译流水线，采用多遍转译器架构，将类型安全的抽象语法树直接合成为动态确定性行为树（基于py_trees），并将其原生映射到CARLA的原子API，从而绕过静态轨迹回放，实现实时交互式执行。

### 主要贡献
1. 提出首个原生映射OpenSCENARIO v2.x DSL到CARLA的编排框架，填补v2.x执行空白。
2. 设计多遍转译器架构，实现从DSL到行为树的确定性编译。
3. 在高并发对抗工况实验中验证了逐刻确定性、精确的空间触发评估及100.0毫秒级跨参与者黑板同步，且运动学分析证实严格遵循连续环境边界。

### 局限性
摘要未提供足够信息：未明确讨论框架的计算开销、对复杂场景的扩展性、与OpenSCENARIO其他版本或第三方仿真器的兼容性，以及未提供可复现性的详细实验配置。

### 阅读优先级
低。理由：论文聚焦于自动驾驶仿真工具链的特定执行一致性问题（OpenSCENARIO v2.x与CARLA集成），对于非该领域（如场景测试工具开发或高保真仿真技术）的读者，其技术贡献的泛化性有限；且摘要未提供充分的性能对比基准或开放实现细节，难以评估其实用价值。

</details>

<details>
<summary>Abstract</summary>

Scenario-Based Testing predominantly relies on the legacy ASAM OpenSCENARIO 1.x XML standard because existing continuous simulation frameworks lack native execution support for the recently matured v2.x Domain-Specific Language (DSL). Adapting legacy interpreters to evaluate v2.x logic introduces spatiotemporal drift, asynchronous event latencies, and artificial kinematic snapping. Addressing this execution gap, OSC2Runner introduces the first orchestration framework capable of natively mapping the OpenSCENARIO v2.x DSL to CARLA. The framework achieves this by formalizing scenario translation as a compilation pipeline through a multi-pass transpiler architecture. Bypassing static trajectory playback, the architecture synthesizes type-safe Abstract Syntax Trees directly into dynamic deterministic behavior trees (py_trees) natively mapped to CARLA's atomic APIs. Empirical validation in highly concurrent adversarial case studies demonstrates tick-by-tick determinism, exact spatial trigger evaluation, and 100.0 ms cross-actor blackboard synchronization. Kinematic analysis proves the strict adherence to continuous environmental boundaries. This architecture transitions Scenario-Based Testing from approximate behavioral interpretation to mathematically rigorous execution, establishing the deterministic backend required for co-simulation, hardware-in-the-loop testing, and automated LLM-driven generation pipelines.

</details>

#### 2026-06-24 - KRVF: A Source-Aware Semantic Voxel World Representation for Edge Mobile Manipulation

**Authors:** Runfeng Ling
**Links:** [abs](https://arxiv.org/abs/2606.26321) - [pdf](https://arxiv.org/pdf/2606.26321)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KRVF: A Source-Aware Semantic Voxel World Representation for Edge Mobile Manipulation
- 作者：Runfeng Ling
- 出版日期：2026-06-24T19:07:42Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接 https://arxiv.org/abs/2606.26321；PDF链接 https://arxiv.org/pdf/2606.26321

### 一句话总结
本文提出了KRVF，一种面向边缘端移动机械臂的、具有来源感知的语义体素世界表示方法，用于在线构建任务导向的机器人记忆。

### 研究问题
如何在边缘计算约束下，为移动机械臂构建一个当前、可查询、具有语义意义且可用于任务操作的世界模型，特别是解决传统重建导向方法在语义推理和传感器失效场景下的不足。

### 核心思路/方法
KRVF将局部世界状态表示为任务导向的体素，每个体素编码占用情况、颜色、语义证据、时间新鲜度和证据来源。该表示分离了测量占用与语义先验假设，实现了对深度失效敏感的物体推理，同时避免破坏持久几何。此外，KRVF通过渲染地图先验深度来修复缺失数据，形成建图与感知间的反馈回路，并暴露语义物体与抓取候选的任务级查询算子。

### 主要贡献
1. 提出了KRVF表示法，将体素明确记录证据来源（source-aware），区分了测量与语义先验，支持深度失效感知的物体推理。
2. 设计了建图-感知反馈回路，通过地图先验深度修复提升感知鲁棒性。
3. 提供了任务级查询接口，直接支持语义物体搜索与抓取候选生成。
4. 在ROS 2中实现了在线RGB-D观测到任务导向机器人记忆的转换系统。

### 局限性
摘要未提供足够信息，未讨论实验验证、数据集、性能指标或与现有方法的定量对比。

### 阅读优先级
低。理由：该技术报告仅形式化提出了KRVF表示与系统设计，但摘要中缺乏实验评估和基线对比，无法判断方法在实际任务中的有效性与效率。若对边缘端机器人语义建图感兴趣可作参考，但需等待后续验证。

</details>

<details>
<summary>Abstract</summary>

Mobile manipulators need world models that are current, queryable, semantically meaningful, and usable under edge-compute constraints. This technical report presents KRVF, a source-aware semantic voxel world representation for edge mobile manipulation. Unlike reconstruction-centric mapping pipelines that primarily optimize global geometric fidelity, KRVF represents local world state as task-oriented voxels that encode occupancy, color, semantic evidence, temporal freshness, and evidence source. The representation separates measured occupancy from semantic-prior hypotheses, enabling depth-failure-aware object reasoning without silently corrupting persistent geometry. KRVF also closes a feedback loop between mapping and sensing by rendering map-prior depth for repair, and exposes task-level query operators for semantic objects and grasp candidates. The report formalizes the KRVF representation and documents a ROS 2 implementation that turns online RGB-D observations into a task-facing robot memory.

</details>

#### 2026-06-24 - RoboAtlas: Contextual Active SLAM

**Authors:** Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
**Links:** [abs](https://arxiv.org/abs/2606.26046) - [pdf](https://arxiv.org/pdf/2606.26046)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, mapping, simulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoboAtlas: Contextual Active SLAM
- 作者：Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
- 出版日期：2026-06-24
- 分类：Embodied / Robotics / AR Applications（主要），3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要 [https://arxiv.org/abs/2606.26046](https://arxiv.org/abs/2606.26046) | PDF [https://arxiv.org/pdf/2606.26046](https://arxiv.org/pdf/2606.26046)

### 一句话总结
RoboAtlas是一个上下文感知的主动SLAM框架，通过结合几何探索、全局语义地图推理和基于VLM的自我中心推理，并利用上下文多臂赌博机在探索与语义导航之间动态切换，实现了大规模真实场景下高效、鲁棒的语义导航任务。

### 研究问题
如何在大规模、多语义实例的真实环境中，使机器人自适应地平衡几何探索与语义推理，以实现基于上下文感知的高效主动SLAM？

### 核心思路/方法
1. **系统框架**：RoboAtlas结合了前沿探索、全局语义地图推理（基于OpenRoboVox 3D语义映射系统）和基于VLM的自我中心推理。
2. **决策机制**：通过一个**上下文多臂赌博机**（contextual multi-armed bandit）来动态调整行为：当场景理解不足时偏向探索，随着语义理解提升，逐渐过渡到语义引导的导航。
3. **评估**：在仿真和真实Unitree Go2机器人上测试（环境超过1800 m²，约3万语义实例），并在GOAT-Bench“Val Unseen”基准上对比，验证了高性能。

### 主要贡献
1. 提出了RoboAtlas，一种上下文主动SLAM框架，能自适应平衡几何探索与语义推理。
2. 在GOAT-Bench“Val Unseen”基准上，使用GPT-4o时达到**90.6%的成功率（SR）**，比先前最强基线提升17.8个百分点；即使使用更小的Qwen2.5-VL-7B模型（88.8% SR），仍优于所有使用GPT-4o的基线，**揭示了3D语义映射框架带来的信息增益比单纯替换基础模型更为重要**。
3. 在真实大规模环境（1800 m²，约3万语义实例）中实现**100%任务成功率**，验证了系统在现实世界中的鲁棒性和效率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作在主动SLAM领域提出了创新的上下文自适应框架，并在标准基准和大规模真实场景上取得了显著优于现有方法的性能（特别是揭示了语义地图框架对基础模型性能的关键提升作用），对机器人导航、语义推理领域的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We present RoboAtlas, a contextual Active SLAM framework that adaptively balances geometric exploration and semantic reasoning using a scalable 3D semantic mapping system, OpenRoboVox. RoboAtlas integrates frontier exploration, global semantic-map reasoning, and egocentric VLM-based reasoning through a contextual multi-armed bandit that transitions from exploration to semantically guided navigation as scene understanding improves. We evaluate the system in simulation and on a Unitree Go2 robot in large-scale real-world environments exceeding 1800 m2 with approx. 30k mapped semantic instances, achieving a 100% task success rate. On the GOAT-Bench "Val Unseen" benchmark, RoboAtlas achieves state-of-the-art performance with highest reported success rate (SR) of 90.6%, using GPT-4o, improving over the strongest prior baseline by 17.8 percentage points in SR. Using the much smaller Qwen2.5-VL-7B model, it still achieves 88.8% SR, outperforming all baselines using GPT-4o in SR, and revealing the importance of the information gained by our semantic mapping framework over simply replacing the underlying foundation model. The results demonstrate that grounding foundation models with large-scale 3D semantic maps enables robust and efficient contextual Active SLAM.

</details>

#### 2026-06-24 - From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response

**Authors:** Samuel Tovey, Stefan Prestel, Hiroshi Yamauchi
**Links:** [abs](https://arxiv.org/abs/2606.25957) - [pdf](https://arxiv.org/pdf/2606.25957)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response
- 作者：Samuel Tovey, Stefan Prestel, Hiroshi Yamauchi
- 出版日期：2026-06-24
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.25957

### 一句话总结
本文提出利用无人机搭载量子磁力计，通过仿真与主动采样重建坍塌建筑内部磁性结构，以辅助灾后搜救。

### 研究问题
如何在灾后72小时黄金救援期内，通过无人机搭载量子磁力计，有效感知坍塌建筑（钢混结构）内部的磁性结构，定位幸存者或空洞。

### 核心思路/方法
1. **仿真管道**：使用Unreal Engine生成钢混停车库坍塌场景，通过每个三角形的偶极子近似计算诱导磁场，验证在屋顶上方约1米处可恢复亚pT到亚nT量级的磁信号。
2. **传感器部署**：评估不同传感器阵列（重点为三传感器阵列）在梯度分辨率与无人机载荷约束间的权衡。
3. **主动重建**：采用高斯过程回归作为后端，结合贝叶斯主动采样策略，从稀疏多传感器样本中重建空间磁场结构，并用多个独立坍塌实例验证管道有效性。

### 主要贡献
1. 提出将量子级磁力计作为灾后搜救的补充传感模态，并构建完整的“坍塌仿真→传感器部署→主动重建”管道。
2. 通过仿真证明，在约1米距离外可检测到有意义的磁性结构（亚pT至亚nT范围）。
3. 三传感器阵列可在梯度分辨率与载荷约束间取得最优平衡，且主动采样在约100个样本点内达到峰值结构相关性。

### 局限性
摘要未提供足够信息。具体局限性包括但不限于：仿真环境与真实倒塌场景的差异、量子磁力计在户外实际部署的鲁棒性、对不同类型建筑废墟的适应性以及算法计算复杂度等均未在摘要中提及。

### 阅读优先级
**高**。理由：本文针对灾害救援这一紧迫应用场景，提出新颖的量子磁力计+主动采样方案，方法设计完整（仿真→部署→重建），且结果量化明确（三传感器最优、100样本收敛）。对于关注量子传感、搜救机器人或主动感知的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Locating survivors of building collapses within the first 72 hours is a critical challenge in disaster response, and existing sensing modalities provide only partial information about the structure beneath the rubble. This paper proposes drone-based quantum magnetometry as a complementary modality and develops a simulation pipeline spanning rubble physics, sensor-array deployment, and active spatial reconstruction. We use Unreal Engine to generate a steel-reinforced concrete parking-garage collapse and compute the induced magnetic field via a per-triangle dipole approximation, establishing that meaningful magnetic structure is recoverable in the sub-pT to sub-nT range from roughly 1 m above the roofline. Then, we feed sparse multi-sensor samples into a Gaussian Process Regression back-end driven by Bayesian active sampling and validate the pipeline across multiple independent collapse realizations; a three-sensor array optimizes the trade-off between gradient resolution and UAV payload constraints, and active sampling reaches peak structural correlation in roughly $100$ samples. Together, these results indicate that quantum-grade sensing could become a useful tool for drone-based structural analysis and potentially void detection in collapsed buildings.

</details>

#### 2026-06-24 - DSP-SLAM++: A Unified Framework for Multi-Class, High-Fidelity Object SLAM in the Wild

**Authors:** Ahmad Kourani, Ghina Daoud, Daniel Asmar, Imad Elhajj
**Links:** [abs](https://arxiv.org/abs/2606.25953) - [pdf](https://arxiv.org/pdf/2606.25953)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, manipulation, autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DSP-SLAM++: A Unified Framework for Multi-Class, High-Fidelity Object SLAM in the Wild
- 作者：Ahmad Kourani, Ghina Daoud, Daniel Asmar, Imad Elhajj
- 出版日期：2026-06-24
- 分类：Embodied / Robotics / AR Applications（主类），3D Reconstruction & Multi-view Geometry（次类）
- 链接：摘要网址：https://arxiv.org/abs/2606.25953；PDF网址：https://arxiv.org/pdf/2606.25953

### 一句话总结
DSP-SLAM++ 通过异步建图流水线和传感器融合适配，在保持实时性的同时支持多类物体高保真建模，将物体SLAM推向实际应用。

### 研究问题
现有面向物体的SLAM系统在实时性能、多类别支持和高保真语义连贯物体模型生成之间存在权衡，缺乏统一的解决方案。

### 核心思路/方法
- 扩展 DSP-SLAM 框架，引入异步建图流水线，实现实时性能。
- 针对单目鱼眼-激光雷达（monocular fisheye-LiDAR）组合进行专用传感器融合适配。
- 通过异步处理消除建图线程瓶颈，显著降低物体处理延迟。

### 主要贡献
1. 提出统一框架DSP-SLAM++，同时支持多类别物体高保真建模和实时运行。
2. 设计了异步建图流水线，将最大物体处理延迟相比现有最优基线降低70%，支持25Hz多类别数据集的鲁棒实时运行。
3. 针对单目鱼眼-激光雷达传感器套件进行适配，使高保真多类物体SLAM在自动驾驶等室外场景中更实用，并开源代码。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对物体SLAM领域的关键权衡问题（实时性、多类支持、高保真度）提出了改进方案，量化指标明确（延迟降低70%，支持25Hz数据集），且开源代码，对从事机器人、自动驾驶等实际应用的读者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing object-aware SLAM systems force a trade-off between real-time performance, multi-class support, and the generation of high-fidelity, semantically coherent object models. To address this trade-off, we present DSP-SLAM++, which extends the DSP-SLAM framework with an asynchronous mapping pipeline for real-time performance and dedicated sensor fusion adaptations for a monocular fisheye-LiDAR suite. Experiments demonstrate that our system generates fine-grained, geometrically-complete shapes for multiple object classes while eliminating severe mapping thread bottlenecks by reducing maximum object processing latency by up to 70\% compared to the state-of-the-art baseline, enabling robust, real-time performance on a challenging 25 Hz multi-class datasets. This work makes high-fidelity, multi-class object SLAM more practical for real-world applications like autonomous driving and robotic manipulation by enabling its use on platforms with common fisheye-LiDAR sensor setups. The open-source code is available at: [github.com/AUBVRL/DSP-SLAMpp].

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
