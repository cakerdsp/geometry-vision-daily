# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：44
- 分类分布：
  - Embodied / Robotics / AR Applications: 17
  - Neural Scene Representations & Rendering: 15
  - 3D Reconstruction & Multi-view Geometry: 7
  - Geometry Foundation Models: 3
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的今日科研趋势综合分析。

---

#### 今日主要趋势

1.  **从“场景优化”到“前馈泛化”的加速迁移**：传统的新视角合成与3D重建方法多依赖于针对单个场景的密集优化，而今日的多篇论文集中展示了向“前馈式”、“可泛化”框架的转变。这些方法试图在单一前向传播中直接生成3D表示，无需针对新场景进行重复优化。代表工作如 **StructSplat** 实现了无需相机参数的前馈3D高斯重建；**PRISM** 则通过几何扭曲-残差建模，实现了单图到多视图的纯前馈重建，避免了扩散模型的迭代采样。这表明，社区正在努力消除3D重建与渲染中的“优化瓶颈”，以追求更高的实时性与可部署性。

2.  **稀疏输入与极端条件下的鲁棒3D感知**：大量论文致力于解决传感器数据稀疏、退化或存在几何歧义等极端场景下的重建与定位问题。 **PanoImager** 和 **StructSplat** 均针对极稀疏视图 (sparse views) 下的不稳定重建；**Rolling Shutter Relative Pose Estimation** 解决了消费级卷帘快门相机在几何计算中的低效问题；而 **UAV-MapFusion** 和 **MIL-LC** 则专注于在GNSS拒止、几何重复或无纹理环境中的鲁棒定位与建图。这反映了研究正从理想实验环境转向更具挑战性的实际应用场景。

3.  **对3D表示“可解释性”与“结构性”的追求**：尽管3D高斯泼溅 (3DGS) 表现出色，但其优化过程的“黑箱”特性及与显式几何的割裂正受到关注。**Vis4GS** 直接开发可视化分析工具，试图解释高斯属性与伪影的成因，提升了模型的可诊断性。**StructSplat** 和 **FLAT** 则从模型结构入手，前者通过结构化表征解耦几何、语义与纹理，后者则直接从潜在空间解码出更显式的**三角形泼溅** (triangle splats) 而非体素化的高斯，旨在生成具有明确表面的、更适合下游仿真与图形应用的几何资产。

4.  **传感器融合与多模态协同的深化**：机器人与AR领域的论文不再依赖单一传感器，而是通过精巧的框架融合多种互补模态。**DSP-SLAM++** 融合了单目鱼眼和LiDAR；**MIL-LC** 则引入了环境磁场作为几何/纹理特征的补充模态以提升定位鲁棒性。此外，**fARfetch** 和 **RoboAtlas** 将视觉-语言模型 (VLM) 与传统的建图、规划框架深度融合，前者用于自适应调整AR虚拟内容，后者则用于引导语义导航。这种跨模态、跨层次的融合策略正成为解决复杂环境问题的关键。

#### 技术路线观察

| 方向 | 技术侧重点 | 代表论文 |
| :--- | :--- | :--- |
| **几何基础模型 (SfM/SLAM/位姿)** | 放弃传统的SfM/SLAM流程，转而使用前馈网络直接回归位姿和深度；利用代数方法（如仿射对应）减少RANSAC迭代所需的最小样本量；利用不变卡尔曼滤波处理多IMU的关节运动系统。 | **StructSplat**, **PanoImager**, **Rolling Shutter Relative Pose Estimation**, **Invariant Kalman filtering** |
| **3D/4D 重建与场景生成** | 从单图/稀疏视图直接生成3D表示，包括3D高斯和三角形泼溅；利用视频扩散模型的隐空间作为强先验，并通过几何扭曲、残差学习等轻量级方式替代昂贵的迭代采样；强调几何精度和显式表面表征。 | **PRISM**, **FLAT**, **StructSplat**, **PanoImager** |
| **神经场景表示与渲染** | 对3DGS的“黑箱”特性进行可视化诊断；将3DGS的风格化问题转化为最优传输问题以提升一致性；从人类偏好反馈中直接优化NeRF的密度场；针对特定应用（如胃镜）提供标准化评估基准。 | **Vis4GS**, **Capacity-Controlled Multi-View Stylization**, **Sculpting NeRF Geometry**, **Gastroendoscopy View Synthesis** |
| **机器人/AR应用** | 构建主动SLAM框架，在几何探索与语义导航间自适应切换；提出能够处理大尺度、视觉多样环境的AR-HRC系统；融合磁力计、惯性、LiDAR等多模态信号实现鲁棒定位；设计面向边缘计算的、任务导向的语义体素表示。 | **RoboAtlas**, **fARfetch**, **MIL-LC**, **KRVF**, **UAV-MapFusion** |

#### 值得优先阅读的论文

1.  **StructSplat** (高优先级): **理由**：它成功解耦了“无相机参数”和“前馈泛化”两大挑战，代表了可泛化3D重建的前沿。在DL3DV基准上5.67 dB的PSNR提升是极具说服力的性能指标，对于研究稀疏视图重建和可泛化渲染的学者来说是必读文献。
2.  **PRISM** (高优先级): **理由**：它巧妙地将单图3D重建任务分解为“几何扭曲”+“残差学习”，从而规避了扩散模型的采样速度瓶颈。这种方法上的创新为快速、高质量的3D内容生成开辟了新路径，对3D生成领域的研究者具有重要启发。
3.  **FLAT** (高优先级): **理由**：该工作首次从扩散模型潜在码中解码出**三角形泼溅**，这是一个关键的表示创新。它将隐式或体素化的3D表示推向与标准图形管线兼容的显式网格表示，对于连接计算机视觉与计算机图形学的研究具有重要意义。
4.  **Rolling Shutter Relative Pose Estimation Made Practical** (高优先级): **理由**：解决了一个长期存在的“实用”瓶颈。通过引入仿射对应将最小匹配点从20降低到7，使卷帘快门相机的RS-aware位姿估计从“理论可行”变为“实用”，对SLAM和SfM领域具有直接且重要的推动作用。
5.  **Sculpting NeRF Geometry: Human-Preference Fine-Tuning of a 3D-Aware Face GAN** (高优先级): **理由**：探索了将人类偏好直接作用于隐式NeRF密度场进行微调的新颖范式。虽然可能带来分布外代价，但这种方法为不使用网格或文本先验的3D几何优化提供了强大的反馈机制，对生成模型和3D内容创作领域具有启发性。

#### 可能的研究机会

1.  **可泛化表示的“编辑性”与“控制性”研究**：当前的可泛化前馈模型（如StructSplat, FLAT）主要聚焦于重建的保真度。如何在保持其泛化能力的同时，引入更强的编辑能力（如语义级别的物体替换、属性修改）是一个空白。可以将**Optimal Transport (OT)**（来自**Capacity-Controlled Stylization**）与可泛化框架结合，或在**FLAT**的三角网格基础上开发参数化的编辑算子。
2.  **为“Narrative-Grounded”类方法重建更丰富的环境表示**：**Look-Before-Move** 强调了生成动态相机轨迹的语义需求。其性能高度依赖于底层的3D场景表示。一个潜在的方向是，将今日论文中提升的几何精度（如FLAT的显式表面）与**Narrative-Grounded**的语义规划相结合，从而在更高保真度的动态世界中实现更精确的叙事驱动相机运动。
3.  **在真实物理引擎中验证量子传感重构结果**：**From Rubble Simulation to Active Magnetic Mapping** 的工作完全基于仿真。与DSP-SLAM++等真实世界系统结合，或与机器人操纵框架（如KRVF）对接，在实际废墟场景中部署类似的主动量子磁力计测绘系统，是极具挑战但非常有价值的研究机会。
4.  **构建面向特定医学应用的、赋予物理约束的渲染框架**：**Gastroendoscopy View Synthesis** 提供了真实医学数据集。可以结合该数据集，探索 **

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-30T10:42:28-04:00
**Total number of papers:** 66
**Number of papers added in the latest update:** 39
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

#### 2026-06-29 - AerialMetric: Benchmarking and Adapting UAV Monocular Metric Depth Estimation in the Real World

**Authors:** Zhongqiang Song, Guanying Chen, Yuqi Zhang, Yin Zou, Chuanyu Fu, Zhiyuan Yuan, Chuan Huang, Shuguang Cui, Xiaochun Cao
**Links:** [abs](https://arxiv.org/abs/2606.29716) - [pdf](https://arxiv.org/pdf/2606.29716)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** depth prediction, metric depth, depth estimation, photogrammetry

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
<summary>Abstract</summary>

Gaze target estimation aims to predict the semantic object an observer fixates upon within an image, a task deeply rooted in the object-oriented nature of human gaze. Observers tend to select a specific semantic entity as the attentional target, rather than responding randomly across arbitrary regions of the image. However, existing methods typically model this task as a direct mapping from global features to gaze heatmaps, essentially treating it as a pixel-level regression problem. This approach fails to explicitly represent the gazed object as a distinct entity, making it difficult to produce stable and semantically consistent predictions in complex scenes. To address this, we propose a two-stage gaze estimation framework guided by object semantics, reformulating gaze target estimation as a hierarchical reasoning process. Our method incorporates object-level representations during feature encoding to align image features with discrete semantic entities, then introduces multi-scale feature fusion and geometric constraints from head pose and gaze direction for fine-grained localization and object-level discrimination. Extensive experiments on GazeFollow, VideoAttentionTarget, ChildPlay, and GOO-Real demonstrate that our method achieves AUC of 0.961, 0.948, 0.987, and 0.977 respectively, delivering strong performance across all benchmarks while maintaining a compact parameter size of 7.1M.

</details>

#### 2026-06-23 - GeoT2V-Bench: Benchmarking 3D Consistency in Text-to-Video Models via 3D Reconstruction

**Authors:** Chenrui Fan, Paolo Favaro
**Links:** [abs](https://arxiv.org/abs/2606.24829) - [pdf](https://arxiv.org/pdf/2606.24829)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoT2V-Bench: Benchmarking 3D Consistency in Text-to-Video Models via 3D Reconstruction
- 作者：Chenrui Fan, Paolo Favaro
- 出版日期：2026-06-23
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要页 https://arxiv.org/abs/2606.24829 | PDF https://arxiv.org/pdf/2606.24829

### 一句话总结
本文提出一个基于3D重建的诊断基准GeoT2V-Bench，用于评估相机提示的文本生成视频模型所生成片段是否具备支持刚性3D重建的几何一致性。

### 研究问题
如何客观、细粒度地评估相机提示的文本生成视频模型输出的3D几何一致性，即生成的帧能否作为同一静态3D场景的多视角证据进行有效重建。

### 核心思路/方法
构建一个重建驱动的诊断管线：先使用VGGT风格几何估计法估算每帧相机内参和姿态，再通过DeformableGS拟合动态场景，并利用时序中值聚合获得静态MedianGS代理。最后沿估计相机路径重渲染该代理。基准不返回单一合格/不合格标签或分数，而是输出一个连续重建画像，涵盖表观图像运动、估计轨迹行为、MedianGS静态渲染误差、静态渲染流一致性以及灵活拟合与静态拟合之间的差距。实验基于12个开源模型配置、80个GeCo-Eval静态场景提示和4种种子，共完成3,840次重建。

### 主要贡献
1. 提出GeoT2V-Bench基准，专门用于诊断相机提示T2V模型在3D一致性方面的缺陷。
2. 提供多维度的连续重建画像指标，能捕获可见运动、静态渲染误差、流一致性和灵活vs静态行为之间可能存在的分歧。
3. 揭示生成视频在被测试为全局静态场景采集时涌现的互补失败模式。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文针对3D生成领域的关键评估问题提出系统性诊断方案，方法设计新颖且指标多元，对关注文本生成视频模型几何一致性的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera-prompted text-to-video (T2V) models are increasingly used to synthesize virtual camera captures, such as orbiting objects or moving through static scenes. For these outputs, visual plausibility is insufficient: the generated frames should also provide coherent multi-view evidence for a single static 3D scene. We introduce GeoT2V-Bench, a reconstruction-based diagnostic benchmark for evaluating whether camera-prompted T2V clips can support explicit rigid 3D reconstruction. Our pipeline estimates per-frame camera intrinsics and poses with VGGT-style geometry estimation, fits DeformableGS, derives a static MedianGS proxy by temporal-median aggregation, and renders this proxy along the estimated camera path. Instead of producing a pass/fail label or a single scalar score, GeoT2V-Bench reports a continuous reconstruction profile covering apparent image motion, estimated trajectory behavior, MedianGS static rendering error, static-render flow agreement, and the gap between flexible and static fits. On a fair-format four-seed evaluation with 3,840 completed reconstructions from 12 open-weight model configurations and 80 GeCo-Eval static-scene prompts, we find that visible motion, static rendering error, flow agreement, and flexible-vs-static behavior often disagree. GeoT2V-Bench therefore captures complementary failure modes that emerge when generated videos are tested as global static-scene acquisitions.

</details>

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-29 - FFAvatar: Feed-Forward 4D Head Avatar Reconstruction from Sparse Portrait Images

**Authors:** Jianjiang Yao, Ke Xian, Renxiang Dai, Robert Caiming Qiu
**Links:** [abs](https://arxiv.org/abs/2606.30347) - [pdf](https://arxiv.org/pdf/2606.30347)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** avatar reconstruction, rendering

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

#### 2026-06-29 - Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation

**Authors:** Siddhant Bansal, Zhifan Zhu, Shashank Tripathi, Jiahe Zhao, Michael J. Black, Dima Damen
**Links:** [abs](https://arxiv.org/abs/2606.30598) - [pdf](https://arxiv.org/pdf/2606.30598)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

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

#### 2026-06-24 - PRISM: Feed-Forward Single-Image 3D Reconstruction via Geometric Warp-Residual Modeling

**Authors:** Zhijie Zheng, Xinhao Xiang, Jiawei Zhang
**Links:** [abs](https://arxiv.org/abs/2606.25430) - [pdf](https://arxiv.org/pdf/2606.25430)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, robotics, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PRISM: Feed-Forward Single-Image 3D Reconstruction via Geometric Warp-Residual Modeling
- 作者：Zhijie Zheng, Xinhao Xiang, Jiawei Zhang
- 出版日期：2026-06-24
- 分类：主类别：3D Reconstruction & Multi-view Geometry；次类别：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.25430

### 一句话总结
本文提出PRISM，一种无需扩散采样、仅通过前馈几何扭曲和残差校正的单图三维重建框架，在保持与扩散方法相当的重建质量的同时大幅降低推理时间。

### 研究问题
如何从单张图像高效且高质量地重建三维场景，克服现有基于扩散模型的方法因迭代采样而推理慢的部署难题。

### 核心思路/方法
1. 观察到几何前向扭曲（geometric forward warping）即可覆盖目标视图的大部分内容，仅留下少量残差需要校正。
2. 提出PRISM：将多视角潜在（latent）预测分解为**参数无关的几何先验**与**学习的残差校正**，推理时无需扩散采样。
3. 设计两阶段训练策略：先通过潜在监督蒸馏（latent supervised distillation）学习几何泛化，再通过感知微调（perceptual fine-tuning）优化外观质量。

### 主要贡献
1. 提出纯前馈框架PRISM，实现从单图到多视图的快速三维重建，无需迭代扩散采样。
2. 利用几何扭曲-残差建模分解任务，使大部分视图内容直接由几何变换完成，降低编码器负担。
3. 设计两阶段训练策略，使模型能够在纯合成数据上泛化，并兼顾几何准确度与外观保真度。
4. 在三个基准上达到与扩散方法可比的性能，同时将每个场景的推理时间大幅降至36秒。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对三维重建中扩散模型推理慢的显著痛点，提出了一种高效的纯前馈替代方案，并在多个基准上验证了速度-质量的权衡优势。秒级推理时间（36秒/场景）对机器人、VR等实时或近实时应用具有重要意义，且两阶段训练策略对合成数据泛化有启发价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing 3D scenes from a single image is a fundamental challenge in computer vision, with broad applications in virtual reality, robotics, and content creation. Recent methods achieve outstanding performance by leveraging camera-controlled video diffusion models, but rely on iterative diffusion sampling, which greatly limits their practical deployment. We observe that geometric forward warping alone can cover the majority of a target view directly from the input image, with only a compact residual left for the encoder to correct. Motivated by this observation, we propose PRISM, a feed-forward framework that decomposes multi-view latent prediction into a parameter-free geometric prior and a learned residual correction, with no diffusion sampling required at inference. To enable generalization from purely synthetic training data, we devise a two-stage training strategy combining latents supervised distillation for geometric generalization and perceptual fine-tuning for appearance quality optimization. Extensive experiments on three benchmarks demonstrate that PRISM achieves competitive reconstruction quality compared with diffusion-based methods, while reducing inference time dramatically to only 36 seconds per scene.

</details>

#### 2026-06-23 - Invariant Kalman filtering for extended pose estimation in multi-IMU articulated rigid-body systems

**Authors:** Sven Goffin, Cédric Schwartz, Silvère Bonnabel, Olivier Brüls, Pierre Sacré
**Links:** [abs](https://arxiv.org/abs/2606.25083) - [pdf](https://arxiv.org/pdf/2606.25083)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Invariant Kalman filtering for extended pose estimation in multi-IMU articulated rigid-body systems  
- 作者：Sven Goffin, Cédric Schwartz, Silvère Bonnabel, Olivier Brüls, Pierre Sacré  
- 出版日期：2026-06-23  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2606.25083  

### 一句话总结
本文提出一种基于不变卡尔曼滤波（IEKF）的迭代方法，用于多IMU铰接刚体系统的扩展位姿估计（方向、速度、位置），通过引入相对L-扩展位姿的Lie群表示，将关节运动学约束以不变形式融入滤波，显著提升估计精度与收敛性。

### 研究问题
如何为多IMU构成的铰接刚体系统（如机器人和人体）实现具有收敛保证和一致性的扩展位姿估计，同时处理跨刚体的位姿耦合与关节约束问题。

### 核心思路/方法
1. 定义**相对L-扩展位姿**（relative L-extended pose）作为运动链系统的Lie群表示，使系统动态具有群仿射性质。  
2. 将关节运动学约束建模为**无噪声伪测量**，并嵌入迭代不变扩展卡尔曼滤波（IterIEKF）框架中，从而保留不变滤波的收敛性和一致性保证。  
3. 在UR5e机器人和人体腿部数据集上验证，与标准EKF、迭代EKF及绝对位姿IterIEKF进行对比。

### 主要贡献
- 首次将不变卡尔曼滤波的收敛与一致性保证扩展至多IMU铰接系统；  
- 提出一种将关节约束以不变形式显式融入滤波的有效方案；  
- 实验显示，提出方法在所有场景中均取得最低RMSE，相比次优滤波器至少降低50%，且收敛更快、运行间变异性更低。

### 局限性
摘要未提供具体局限性信息（如传感器噪声假设、计算复杂度、对非线性约束的适应性等）。

### 阅读优先级
**高**  
理由：该方法针对机器人运动跟踪与人体动作分析中的核心问题，提出理论严谨且实验效果显著的创新方案（RMSE降低50%以上），对从事滤波、位姿估计与惯性导航的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate extended pose estimation (orientation, velocity, and position) for IMU-instrumented articulated rigid-body systems is a key challenge in robotics and human motion analysis. The invariant extended Kalman filter (IEKF) addresses this problem for a single rigid body with convergence guarantees and consistency under unobservability, but extending these properties to articulated systems is nontrivial: inter-body pose coupling prevents a direct application, and incorporating joint kinematic constraints within the invariant framework remains an open problem. To address this gap, we introduce the relative L-extended pose, a Lie group representation for kinematic-tree systems. With one IMU per body, it yields group-affine dynamics and allows joint constraints to be expressed in invariant form. We incorporate these constraints as noise-free pseudo-measurements within an iterated IEKF (IterIEKF), thereby preserving the convergence and consistency guarantees of invariant filtering. Validated on both a UR5e robot and a human leg, the proposed IterIEKF outperforms all EKF, IterEKF, and absolute-pose IterIEKF baselines. It converges faster, exhibits lower run-to-run variability, and consistently achieves the lowest RMSE, with reductions of at least 50% compared to the second-best filter across all scenarios considered in this work.

</details>

#### 2026-06-23 - Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM

**Authors:** Leshu Li, Jie Peng, Yang Zhao
**Links:** [abs](https://arxiv.org/abs/2606.24796) - [pdf](https://arxiv.org/pdf/2606.24796)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM
- 作者：Leshu Li, Jie Peng, Yang Zhao
- 出版日期：2026-06-23T16:48:58Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.24796

### 一句话总结
该论文提出了一种面向渲染区域的剪枝策略，在不牺牲定位与建图精度的前提下，显著降低3DGS-SLAM在自动驾驶等大规模场景中的内存消耗并提升帧率。

### 研究问题
3DGS-SLAM在大尺度场景（如自动驾驶）中运行时，高斯点随建图过程持续累积，导致内存消耗不断增长，从而限制了其在大规模场景下的应用。

### 核心思路/方法
提出一种“渲染区域感知剪枝”策略：根据高斯点对有效渲染区域的贡献程度（而非仅依赖不透明度或梯度幅值等单点启发式指标）来选择性移除冗余高斯点，从而直接针对内存冗余的来源进行剪枝。

### 主要贡献
- 提出了一种渲染区域感知的剪枝方法，从渲染区域贡献角度解决3DGS-SLAM的内存冗余问题。
- 在EuRoC和KITTI数据集上的实验证明，该方法在大型室外场景中一致优于现有剪枝方法。
- 实现了超过60%的内存降低和2倍以上的FPS提升，同时保持定位与建图精度。
- 项目代码已开源。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该工作针对3DGS-SLAM在大尺度场景中的内存瓶颈问题提出了有效解决方案，实验指标（60%+内存减少、2倍FPS提升）显著，且代码已公开，对自动驾驶等实时应用场景具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views. For SLAM in large-scale scenes, such as autonomous driving, 3DGS-SLAM faces a critical limitation: memory consumption increases continuously over time as Gaussian points accumulate, leading to poor memory efficiency and limiting its applicability. In this work, we propose a rendering-area-aware pruning strategy that selectively removes Gaussians based on their contribution to the effective rendering area, rather than solely relying on Gaussian-level heuristics such as opacity or gradient magnitude. This perspective directly targets the sources of memory redundancy, effectively reducing the peak memory footprint of 3DGS-SLAM during runtime. Evaluations on the EuRoC and KITTI datasets demonstrate that our method consistently outperforms existing pruning approaches in large-scale outdoor scenes, achieving over 60% memory reduction and more than 2 times FPS improvement while preserving localization and mapping accuracy. These results highlight rendering-area-aware pruning as a promising direction for scaling 3DGS-SLAM to real-world autonomous driving scenarios. Our code is publicly available at https://github.com/UMN-ZhaoLab/Pocket-SLAM.git.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-29 - VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes

**Authors:** Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu
**Links:** [abs](https://arxiv.org/abs/2606.30645) - [pdf](https://arxiv.org/pdf/2606.30645)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, manipulation, mapping

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

#### 2026-06-24 - Gastroendoscopy View Synthesis: A New Real Dataset and Evaluation

**Authors:** Masaki Minai, Yusuke Monno, Masatoshi Okutomi, Sho Suzuki
**Links:** [abs](https://arxiv.org/abs/2606.25427) - [pdf](https://arxiv.org/pdf/2606.25427)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, radiance, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gastroendoscopy View Synthesis: A New Real Dataset and Evaluation
- 作者：Masaki Minai, Yusuke Monno, Masatoshi Okutomi, Sho Suzuki
- 出版日期：2026-06-24
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：摘要链接 https://arxiv.org/abs/2606.25427 ; PDF链接 https://arxiv.org/pdf/2606.25427

### 一句话总结
本文发布了首个用于胃内窥镜新型视角合成（NVS）的真实数据集GastroNVS，并基于多种3D高斯泼溅（3DGS）方法进行了评估，指出了该应用场景下的挑战。

### 研究问题
现有胃内窥镜场景下的新型视角合成研究缺乏足够的真实数据集，无法有效评估和推动相关方法（如NeRF和3DGS）在该领域的应用。

### 核心思路/方法
1. 创建并发布首个真实胃内窥镜NVS数据集GastroNVS，包含胃镜图像、相机位姿和点云数据。
2. 利用该数据集，对多种3D高斯泼溅方法进行定量和定性评估，以验证数据集的适用性并分析当前方法的不足。

### 主要贡献
- 提出了首个用于胃内窥镜新型视角合成的真实数据集GastroNVS。
- 基于该数据集对现有3DGS方法进行了系统评估，揭示了胃内窥镜场景下NVS的具体挑战，为未来研究提供基准和方向。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：本文针对胃内窥镜这一特定医学应用，提供了首个真实NVS数据集，填补了现有数据资源的空白。对于从事医学影像分析、神经渲染或内窥镜图像处理的研究者具有直接参考价值，且数据集可申请获取，便于后续复现与拓展。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis (NVS) is an active research topic in computer vision, owing to the success of neural radiance field (NeRF) and 3D Gaussian splatting (3DGS) methods. While NVS opens the door to potential applications in gastroendoscopy, such as extending the field of view of endoscopic images and enabling digital twins for 3D archiving and endoscopist manipulation training, the dataset is insufficient to evaluate NVS for gastroendoscopy. In this paper, we present the first real gastroscopy dataset for NVS, namely the GastroNVS dataset, which contains a set of gastroscopic images, camera poses, and a point cloud for real gastroendoscopy inspection. To assess the suitability of the GastroNVS dataset, we evaluate several 3DGS methods and discuss the challenges for future development. The dataset is available on request from our project page.

</details>

#### 2026-06-23 - FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation

**Authors:** Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari
**Links:** [abs](https://arxiv.org/abs/2606.24876) - [pdf](https://arxiv.org/pdf/2606.24876)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3DGS, rendering, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FLAT: 前馈潜在三角形泼溅技术用于几何精确的场景生成
- 作者：Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari
- 出版日期：2026-06-23T17:53:41Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.24876

### 一句话总结
本文首次证明可以从视频扩散潜在码中直接解码出三角形泼溅（triangle splats）作为显式表面基元，通过射线居中旋转参数化和乘积窗函数解决了梯度流问题，从而在保持视觉质量的同时显著提升了3D场景几何精度。

### 研究问题
如何从单张图像的压缩视频扩散潜在码中，直接在单个前馈过程中解码出表面对齐的显式几何基元（三角形泼溅），以替代现有的体素化3D高斯表示，从而获得具有良好定义表面的可渲染场景。

### 核心思路/方法
1.  提出FLAT方法，从视频扩散潜在码直接解码三角形泼溅。
2.  **射线居中的旋转参数化（ray-centered rotation parameterization）**：用于三角形回归，降低对基元朝向的敏感性。
3.  **乘积窗函数（product window function）**：一种新颖的可微分三角形渲染中的窗口函数，改善梯度流，使得训练时梯度能更有效地回传到三角形参数上。
4.  轻量级测试时精化步骤（test-time refinement step）：将预测的三角形“汤”转换成完全不透明、可用于游戏引擎的表示，支持实时渲染。
5.  在相同训练设定下系统比较了3D高斯泼溅、2D高斯泼溅和三角形泼溅的表示权衡。

### 主要贡献
- 首次证明可以从视频扩散潜在码中直接解码三角形泼溅作为显式表面基元。
- 提出了射线居中旋转参数化和乘积窗函数，有效解决了三角形泼溅训练中梯度流不畅的难题。
- 在标准基准测试上，相比最先进的前馈基线方法，FLAT在保持竞争性视觉质量的同时实现了显著更好的几何精度。
- 提供了首个关于前馈场景生成中不同基元表示（3DGS、2DGS、三角形泼溅）权衡的系统性分析。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作首次将显式三角形泼溅与前馈视频扩散潜在码解码相结合，解决了几何精度和表面定义的瓶颈，并提供了系统的基元表示对比分析。这对于3D场景生成、神经渲染和计算机图形学领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Generating explorable 3D scenes from a single image requires strong generative priors and accurate geometric representations suitable for downstream use. Current video diffusion models offer high-quality generation and implicitly encode multi-view geometric structure in latent space. However, existing feedforward latent scene decoders typically output volumetric 3D Gaussians that lack a well-defined surface, limiting their use in simulation or standard graphics pipelines. This motivates decoding surface-aligned primitives that are not only renderable but also closer to explicit geometric assets. We ask whether compressed video diffusion latents can be mapped directly to explicit surface primitives in a single pass. To this end, we introduce FLAT and, for the first time, show that triangle splats can be decoded directly from video diffusion latents. Compared with decoding 3D Gaussians, predicting flat primitives is notoriously more challenging due to high sensitivity to primitive orientations, oftentimes leading to poor gradient flow. FLAT solves with two key ingredients: a ray-centered rotation parameterization for triangle regression and a novel product window function that improves gradient flow during differentiable triangle rendering. On standard benchmarks, FLAT achieves significantly better geometric accuracy while maintaining competitive visual quality compared to state-of-the-art feedforward baselines. We further show that a lightweight test-time refinement step converts the predicted triangle soup into a fully opaque, game-engine-ready representation that supports real-time rendering. By evaluating 3DGS, 2DGS, and triangle splatting variants under an identical training setup, we provide the first systematic analysis of representation tradeoffs in feedforward scene generation. The project page is available at https://flat-splat.github.io

</details>

#### 2026-06-23 - FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation

**Authors:** Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo
**Links:** [abs](https://arxiv.org/abs/2606.24874) - [pdf](https://arxiv.org/pdf/2606.24874)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation  
- 作者：Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
- 出版日期：2026-06-23  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2606.24874  

### 一句话总结
FLUX3D 提出了一种基于扩散对齐稀疏表示的图像到3D高斯泼溅生成框架，通过改进特征表示和跨模态对齐，显著提升了生成3D资产的外观保真度。

### 研究问题
当前基于稀疏体素表示的图像到3DGS生成方法，在保持输入图像的高频视觉细节方面存在两个瓶颈：1）使用用于语义抽象的判别式2D特征构建稀疏体素潜伏表示，抑制了重建线索，导致表示瓶颈；2）在生成阶段，标准扩散变换器缺乏有效机制来对齐密集2D图像标记与稀疏3D体素潜伏表示，导致跨模态对应瓶颈。

### 核心思路/方法
1. **表示学习改进**：提出扩散对齐结构化潜伏表示（DA-SLAT），重新审视稀疏体素3D表示学习中的2D特征选择，并配合仅解码器架构，提升3DGS重建保真度。  
2. **跨模态对齐改进**：设计稀疏结构感知扩散框架，包括稀疏结构多模态扩散变换器（SMDiT）和模态感知旋转位置嵌入（MARoPE），实现与几何无关的2D-3D对齐。

### 主要贡献
1. 提出DA-SLAT方法，优化稀疏体素表示的2D特征选择，提高3DGS重建细节。  
2. 设计SMDiT和MARoPE机制，解决生成阶段稀疏与密集模态的对应问题。  
3. 实验表明FLUX3D在生成高质量3DGS资产的外观保真度上显著优于所有现有最先进方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文针对图像到3DGS生成领域的关键保真度瓶颈，提出了系统性的架构改进，且在基准测试中全面超越现有方法，对高精度3D内容生成方向有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Sparse voxel representation has emerged as a scalable foundation for image-to-3D Gaussian Splatting (3DGS) generation, yet current methods struggle to preserve high-frequency visual details of input images due to two structural bottlenecks. First, they adopt discriminative 2D features optimized for semantic abstraction to construct sparse voxel latents, which suppress reconstructive cues and induce a representation bottleneck. Second, in the generation stage, standard diffusion transformers lack effective mechanisms to align dense 2D image tokens with sparse 3D voxel latents, resulting in a cross-modal correspondence bottleneck. To address these issues, we propose FLUX3D, a scalable image-to-3DGS framework that boosts both representation learning and cross-modal alignment during generation. We first revisit 2D feature selection for sparse-voxel-based 3D representation learning, propose Diffusion-Aligned Structured Latents (DA-SLAT) and couple it with a decoder-only architecture to improve 3DGS reconstruction fidelity. We also design a sparse-structure-aware diffusion framework, which integrates the Sparse-structure Multimodal Diffusion Transformer (SMDiT) and Modal-Aware Rotary Positional Embedding (MARoPE) to achieve geometry-agnostic 2D-3D alignment. Extensive benchmark experiments demonstrate that FLUX3D yields substantial improvements in appearance fidelity and significantly outperforms all state-of-the-art (SOTA) methods in generating high-quality 3DGS assets.

</details>

#### 2026-06-23 - OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis

**Authors:** Chenrui Fan, Paolo Favaro
**Links:** [abs](https://arxiv.org/abs/2606.24799) - [pdf](https://arxiv.org/pdf/2606.24799)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis
- 作者：Chenrui Fan, Paolo Favaro
- 出版日期：2026-06-23
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2606.24799；PDF链接 https://arxiv.org/pdf/2606.24799

### 一句话总结
OrbitForge 通过冻结的文本到视频模型与逐提示的3D高斯泼溅重建优化，将单次文本生成的视频转化为完整的闭环轨道3D场景，无需多视图微调或分数蒸馏优化。

### 研究问题
如何利用现有文本到视频模型生成高质量、覆盖完整的3D场景，同时克服视频中相机运动难控、视图覆盖不全及帧间不一致的问题。

### 核心思路/方法
1. **初始重建**：从首段生成的视频出发，通过可变形高斯泼溅（使用稳健的MedianGS代理）获得初步3D重建。
2. **缺失视图检测**：沿预设轨道渲染视图，识别未覆盖的视角区域。
3. **补全与重构**：仅使用文本到视频模型补全缺失视图，再将完整的轨道渲染结果重建为最终的高斯泼溅场景。整个流程无需任务特定视频或多视图微调、也无需逐提示的分数蒸馏或逐步生成视图。

### 主要贡献
- 提出一种无需多视图微调或分数蒸馏优化的文本到3D场景生成框架。
- 通过3D重建作为锚点，改善生成视频的3D一致性。
- 引入重建设计中考虑覆盖率评估的必要性：仅依赖局部平滑度会奖励那些从未尝试完整轨道的生成方法。
- 在T3Bench派生测试集（300个提示）上，OrbitForge重建的平均覆盖中位数为359.0度，将MedianGS单独重建的Q10 ImageReward值从8.07提升至16.36，并在覆盖率-质量上接近VideoMV。

### 局限性
摘要未提供关于运行时间、计算资源消耗、对复杂场景（如动态物体或细粒度纹理）的适用性、或与更强基线方法（如多视图扩散模型）的对比等具体局限性信息。

### 阅读优先级
高。理由：该工作提出了一种直接利用现有文本到视频模型生成高质量3D场景的实用方案，克服了视图覆盖不足和一致性问题，且无需特定微调；在覆盖率评估和性能提升上有明确、可量化的贡献（如359度轨道覆盖和ImageReward提升），对神经场景表示与渲染领域的从业者极具参考价值。

</details>

<details>
<summary>Abstract</summary>

Generic text-to-video models can be used as rich open-world scene priors. Despite the high quality of today's generated videos, they do not directly yield reliable 3D assets: camera motion is difficult to control, view coverage is partial, and frames often contain inconsistencies across time. We introduce OrbitForge, an adapter built from frozen video priors and per-prompt Gaussian Splatting reconstruction optimization that converts a single text-generated video into a canonical closed-orbit 3D Gaussian Splatting scene. We use 3D reconstruction as an anchor to improve the 3D consistency of the generated video. We obtain a preliminary 3D reconstruction from a first generated video via Deformable Gaussian Splatting with a robust MedianGS proxy. We render views from a prescribed orbit to detect missing viewpoints. OrbitForge uses the text-to-video model to complete only the missing views, and reconstructs the completed orbit into a final Gaussian Splatting scene. This design requires no task-specific video or multiview fine-tuning, avoids per-prompt score-distillation optimization, and does not progressively generate views one step at a time. We further argue that this setting demands coverage-aware evaluation: local smoothness alone rewards methods that never attempt a full orbit. On a frozen 300-prompt T3Bench-derived audit, OrbitForge reconstruction attains a 359.0-degree measured median span, raises originally unsupported-bin Q10 ImageReward from 8.07 to 16.36 relative to MedianGS-only reconstruction, while remaining competitive with VideoMV on the coverage-quality.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-29 - UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image

**Authors:** Mohamed el amine boudjoghra, Ivan Laptev, Angela Dai
**Links:** [abs](https://arxiv.org/abs/2606.30608) - [pdf](https://arxiv.org/pdf/2606.30608)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, virtual reality

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

#### 2026-06-24 - MIL-LC: A Robust Magnetometer-Inertial-LiDAR Fusion Multimodal Localization Framework

**Authors:** Qiyang Lyu, Zhenyu Wu, Wei Wang, Hongming Shen, Danwei Wang
**Links:** [abs](https://arxiv.org/abs/2606.25796) - [pdf](https://arxiv.org/pdf/2606.25796)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MIL-LC: A Robust Magnetometer-Inertial-LiDAR Fusion Multimodal Localization Framework
- 作者：Qiyang Lyu, Zhenyu Wu, Wei Wang, Hongming Shen, Danwei Wang
- 出版日期：2026-06-24
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.25796

### 一句话总结
本文提出了一种磁力计-惯性-LiDAR融合的多模态定位框架MIL-LC，旨在解决GNSS拒止、几何重复或纹理缺失环境中自主移动机器人的鲁棒定位问题，通过引入环境磁场作为补充模态，在LiDAR退化或长期部署中磁场变化时仍能保持可靠定位。

### 研究问题
如何实现自主移动机器人在挑战性环境（如GNSS拒止、几何重复、纹理缺失的办公室、酒店、地下停车场）中的鲁棒定位，克服单模态传感器限制以及现有多模态融合框架对几何/纹理特征或基础设施信标的过度依赖。

### 核心思路/方法
提出MIL-LC框架，融合磁力计、惯性测量单元和LiDAR数据，并采用自定义传感器套件。利用环境磁场（AMF）作为不依赖几何/纹理特征、无需额外基础设施的互补模态，解决LiDAR几何退化或长期部署中磁图变化时的定位问题。通过仿真和真实环境实验验证框架的鲁棒性和准确性。

### 主要贡献
1. 提出首个面向自主移动机器人的磁力计-惯性-LiDAR融合定位框架MIL-LC，填补了该场景下AMF融合研究的空白。
2. 设计自定义传感器套件，使框架在LiDAR几何退化或长期部署中磁图变化时仍能提供可靠定位。
3. 通过仿真和真实环境实验证明MIL-LC框架的鲁棒且准确的定位性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦于机器人定位领域的实际工程难题（几何退化、磁图变化），方法新颖（AMF融合），但摘要中实验细节和性能量化数据不足，限于具体应用场景（AMR），对跨领域读者启发性有限。

</details>

<details>
<summary>Abstract</summary>

Localization in challenging environments, such as GNSS-denied, geometrically repetitive, or textureless scenes commonly found in offices, hotels, and underground parking facilities, remains an open problem for reliable autonomous mobile robot (AMR) deployment. Single-modality localization methods are inherently limited by the constraints of individual sensors. Although multimodal fusion frameworks have shown improved robustness, most existing approaches still rely heavily on geometric or texture features, or on infrastructure-based beacons, which increase installation and maintenance costs while reducing deployment flexibility. Recently, ambient magnetic field (AMF)-based localization has attracted growing attention because it does not depend on geometric or texture features, nor does it require additional infrastructure, making it a promising complementary modality for AMR localization. However, existing studies have only explored such fusion in pedestrian scenarios using smartphone-mounted sensor suites, and practical solutions for AMR systems remain largely unexplored. To address this gap, this article proposes a magnetometer-inertial-LiDAR fused multimodal localization framework with a custom-designed sensor suite, termed MIL-LC, which provides reliable localization even when LiDAR suffers from geometric degeneration or when the magnetic map changes during long-term deployment. Extensive experiments in both simulation and real-world environments demonstrate that the proposed MIL-LC framework achieves robust and accurate localization performance.

</details>

#### 2026-06-23 - fARfetch: Enabling Collocated AR-HRC in Large Visually Diverse Environments with VLM-Driven AR Content Adaptation

**Authors:** Christian Fronk, Hanting Ye, David Hunt, Miroslav Pajic, Maria Gorlatova
**Links:** [abs](https://arxiv.org/abs/2606.25162) - [pdf](https://arxiv.org/pdf/2606.25162)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：fARfetch: Enabling Collocated AR-HRC in Large Visually Diverse Environments with VLM-Driven AR Content Adaptation
- 作者：Christian Fronk, Hanting Ye, David Hunt, Miroslav Pajic, Maria Gorlatova
- 出版日期：2026-06-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.25162

### 一句话总结
fARfetch 是一个面向大型、视觉多样环境的增强现实-人机协作（AR-HRC）系统，通过语义地图、缩微世界表示和视觉语言模型（VLM）驱动的AR内容自适应，显著提升了户外大空间内协作任务的效率和内容可读性。

### 研究问题
如何在大型、视觉多样（如户外）环境中，解决增强现实人机协作（AR-HRC）中因长距离和视线受阻导致的交互困难与虚拟内容可读性下降问题。

### 核心思路/方法
系统集成了三个关键组件：
1. **共享语义环境地图**：AR头显与机器人共同构建并可视化检测到的地标，支持基于地标的“前往”指令。
2. **上下文感知的缩微世界表示**：为精细路径规划提供共环境的小型化、全景式抽象视图。
3. **VLM驱动的AR视图管理**：联合调整虚拟内容的颜色、大小和方向，以在大型视觉多样环境中保持内容可读性。

系统基于Meta Quest 3头显和Unitree Go2四足机器人实现，并在真实户外大尺度（30.5米）巡检任务中开展了12名用户的受试者内实验。

### 主要贡献
- 提出一套完整的AR-HRC系统，整合了语义地图、缩微世界和VLM内容自适应，适用于大型、视觉多样环境。
- 通过用户实验验证：相比无AR基线，fARfetch显著提升任务完成时间（快66%），并降低了脑力负荷（-43%）、时间需求（-34%）和挫败感（-66%）。
- 定制可读性调查表明，系统在大尺度户外环境中能有效保持虚拟内容的可读性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对实际户外大空间人机协作的明确痛点（内容可读性、交互效率），提出了新颖的VLM驱动自适应方法，并附有显著量化的用户实验证据，对AR-HRC领域的研究者和从业者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Augmented Reality (AR) can improve collocated human-robot collaboration by making robot state and intent visible and enabling intuitive control, yet large, visually diverse environments like the outdoors challenge both interaction and content legibility, especially at long distances and beyond visual line of sight. We present fARfetch, an AR-HRC system that integrates (i) shared semantic environment mapping across an AR headset and robot that visualizes detected landmarks in AR to support landmark-grounded go-to commands, (ii) a context-aware world-in-miniature representation of the shared environment for fine-grained path authoring, and (iii) vision-language-model driven AR view management that jointly adapts virtual content color, size, and orientation to maintain legibility in large visually diverse environments. We implement fARfetch with a Meta Quest 3 headset and Unitree Go2 quadruped robot, and conduct a within-subjects user study (N=13) on a real-world large-scale (30.5m) outdoor inspection task. fARfetch yielded significantly faster completion times than a non-AR baseline (66%) and significantly lower workload in mental demand (-43%), temporal demand (-34%), and frustration (-66%). A custom legibility survey indicated fARfetch effectively maintained virtual content legibility in the large outdoor environment.

</details>

#### 2026-06-23 - Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics

**Authors:** Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
**Links:** [abs](https://arxiv.org/abs/2606.24814) - [pdf](https://arxiv.org/pdf/2606.24814)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
- 作者：Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
- 出版日期：2026-06-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.24814

### 一句话总结
本文提出了一种结合SLAM、SAM、实例聚类和VLM多视角推理的管道，用于在内部物流环境中生成包含几何结构、物体类别和可移动性信息的上下文语义地图，无需任务特定训练。

### 研究问题
如何使仅依赖几何地图的自主移动机器人获得对物体及其上下文属性（如可移动性）的语义理解，并构建支持上下文感知过滤的语义地图。

### 核心思路/方法
- 结合SLAM（同步定位与地图构建）进行几何建图，SAM（分割一切模型）进行实例分割，实例聚类对同一物体进行聚合，以及VLM（视觉-语言模型）多视角推理。
- 通过聚合多视角观测并在零样本、开放词汇设置下查询VLM，推断物体上下文属性（本文以可移动性为例）。
- 采用两种提示策略评估三种VLM，并进行组件级分析。

### 主要贡献
- 提出一种无需任务特定训练或预定义物体类别的上下文语义地图构建管道。
- 在语义分类上达到98.93%的mIoU，在物体可移动性估计上达到89.17%的mAcc。
- 通过组件分析揭示了VLM推理是上下文理解的主要瓶颈，实例聚类是全景性能的主要限制。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该研究针对内部物流中移动机器人的实际需求，提出了一种结合SLAM、SAM和VLM的创新管道，取得了非常高的语义分类性能（98.93% mIoU），并提供了详细的组件瓶颈分析，对机器人语义建图领域有直接参考价值。论文发表于2026年，技术方法新颖。

</details>

<details>
<summary>Abstract</summary>

Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present a contextual semantic mapping pipeline that combines SLAM-based geometric mapping, SAM-based instance segmentation, instance clustering, and VLM multi-view reasoning to produce a contextual semantic map representation encoding geometric structure, object class, and object movability. By aggregating observations across multiple viewpoints and querying a VLM in a zero-shot, open-vocabulary setting, the pipeline infers contextual object properties--here demonstrated through movability--without requiring task-specific training or predefined object categories. We evaluate three VLMs under two prompting strategies and conduct a component-wise analysis of the pipeline. The proposed pipeline achieves 98.93 % mIoU for semantic classification and 89.17 % mAcc for object movability estimation. Component analysis identifies VLM reasoning as the primary bottleneck for contextual understanding and instance clustering as the main limitation for panoptic performance. The resulting semantic map supports context-aware filtering and robust navigation in dynamic intralogistics environments.

</details>

#### 2026-06-23 - Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization

**Authors:** Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, Haocheng Peng, Yujun Shen, Hujun Bao, Guofeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.24767) - [pdf](https://arxiv.org/pdf/2606.24767)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** pose estimation, embodied AI, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization
- 作者：Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, Haocheng Peng, Yujun Shen, Hujun Bao, Guofeng Zhang
- 出版日期：2026-06-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.24767

### 一句话总结
本文提出OpenReLoc，一种利用开放词汇语义理解的紧凑目标级表示进行室内视觉重定位的系统，通过结合多模态语义匹配、目标参考框架和形状引导的损失函数实现高精度相机定位。

### 研究问题
如何组织场景中的丰富的对象信息（包括语义、布局和几何），构建结构化地图表示，并仅使用对象单元驱动相机重定位任务，同时提升场景理解能力和定位精度。

### 核心思路/方法
1. 利用预训练基础模型，引入多模态机制融合开放词汇语义知识，实现有效的2D-3D对象匹配。
2. 设计面向对象的参考框架作为位置先验，并基于Distance-IoU（DIOU）提出参考框架选择策略，支持可扩展场景。
3. 提出双路径2D迭代最近像素损失（Iterative Closest Pixel loss），并利用对象形状指导，确保稳定准确的位姿优化。

### 主要贡献
1. 首次探索仅使用对象单元构建结构化地图表示并驱动相机重定位任务。
2. 提出OpenReLoc系统，结合开放词汇语义理解与目标级表示，增强可解释性和实用性。
3. 在多个数据集上验证了重定位召回率和精度的优越性能。

### 局限性
摘要未提供足够信息。

- 缺少关于计算效率、实时性、泛化能力或失败案例的具体分析。
- 未提及对复杂场景（如光照变化、动态目标）的鲁棒性评估。
- 未说明开放词汇模型的具体选择、训练细节或消融实验结果。

### 阅读优先级
中

理由：该工作聚焦室内视觉重定位任务，结合了开放词汇语义理解与目标级表示，思路新颖且实验结果优秀。但论文仍在预印本阶段（2026年6月发布），摘要简洁，未提供可复现的细节，需待公开代码和完整论文以评估其实用价值。对相关领域研究者而言具有参考意义，但非紧急必读。

</details>

<details>
<summary>Abstract</summary>

Indoor visual relocalization plays a critical role in emerging spatial and embodied AI applications. However, prior research was predominantly devoted to low-level vision schemes, struggling to perceive scene semantics and compositions, which limits both interpretability and applicability. In this paper, we explore the issue of how to organize rich object information in a scene, including semantics, layout, and geometry, into a structured map representation, thereby utilizing object units exclusively to drive the camera relocalization task. To this end, we propose OpenReLoc, a camera relocalization system designed to provide scene understanding and accurate pose estimation capabilities. Leveraging recent foundation models, we first introduce a multi-modal mechanism to integrate open-vocabulary semantic knowledge for effective 2D-3D object matching. Additionally, we design object-oriented reference frames as position priors, paired with a reference frame selection strategy based on the Distance-IoU (DIOU), enabling extension to scalable scenes. Moreover, to ensure stable and accurate pose optimization, we also propose a dual-path 2D Iterative Closest Pixel loss guided by object shape. Experimental results demonstrate that OpenReLoc achieves superior relocalization recall and accuracy across various datasets. Our source code will be released upon acceptance.

</details>

#### 2026-06-23 - UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving

**Authors:** Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth, Stephen Law, Yun Ye
**Links:** [abs](https://arxiv.org/abs/2606.24759) - [pdf](https://arxiv.org/pdf/2606.24759)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, driving scene, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving  
- 作者：Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth, Stephen Law, Yun Ye  
- 出版日期：2026-06-23  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2606.24759  

### 一句话总结  
UniDrive提出了一种融合时间推理与高分辨率感知的统一视觉-语言框架，用于自动驾驶中的可解释风险理解，在DRAMA-Reasoning基准上取得了最优性能，并展现了良好的小目标定位与零样本泛化能力。

### 研究问题  
现有自动驾驶场景理解方法在时间推理（处理多帧动态）与空间精度（定位细粒度风险目标）之间存在权衡，导致对小型、远处或部分遮挡的危害识别不足，且语言驱动的模型解释缺乏接地证据。

### 核心思路/方法  
- 设计双分支架构：**时间推理分支**从多帧输入建模场景动态；**高分辨率感知分支**从最新帧保留细粒度空间细节。  
- 通过**门控交叉注意力融合模块**整合两个分支，将动态上下文与精确空间证据对齐。  
- 基于融合表示，联合生成自然语言风险描述和风险对象的接地边界框输出。

### 主要贡献  
- 提出UniDrive统一框架，同时实现时间语义与高分辨率感知的显式结合。  
- 在DRAMA-Reasoning验证集上取得最优整体性能，在小目标定位中表现突出。  
- 零样本泛化到NuScenes和BDD100K数据集，且获得人类评级的可解释性与可信度提升。

### 局限性  
摘要未提供足够信息，未说明框架的计算开销、失败案例或性能边界（如极端天气、密集交通等场景下的表现）。

### 阅读优先级  
**高**  
理由：该工作直接针对自动驾驶中可解释风险理解的核心难点（时空权衡），提出明确的双分支融合方案，实验展示了多基准优势与零样本泛化能力，代码已开源，适合希望跟进统一视觉-语言 grounding 框架的研究者或工程实践者。

</details>

<details>
<summary>Abstract</summary>

Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and spatial precision. Models that rely on single-frame or low-resolution inputs often miss small, distant, or partially occluded hazards, while language-centric driving models frequently provide limited grounded evidence for their explanations. To address this gap, we propose UniDrive, a unified visual-language and grounding framework for interpretable risk understanding in autonomous driving. UniDrive combines a temporal reasoning branch that models scene dynamics from multi-frame visual input with a high-resolution perception branch that preserves fine-grained spatial details from the latest frame. The two branches are integrated through a gated cross-attention fusion module, enabling dynamic context to be aligned with precise spatial evidence. Based on the fused representation, UniDrive jointly generates natural-language risk descriptions and grounded bounding-box outputs for risk objects. Experiments on the DRAMA-Reasoning benchmark show that UniDrive outperforms representative image-based and video-based baselines in both captioning and risk-object grounding. In particular, UniDrive achieves the best overall performance on the validation split and demonstrates clear advantages in small-object localization, zero-shot generalization to NuScenes and BDD100K, and human-rated interpretability and trustworthiness. These results suggest that explicitly combining temporal semantics and high-resolution perception provides a stronger foundation for interpretable and safety-oriented autonomous driving systems. The code is available at https://github.com/pixeli99/unidrive-dev.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
