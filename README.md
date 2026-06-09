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

**Last updated:** 2026-06-09T11:26:48-04:00
**Total number of papers:** 42
**Number of papers added in the latest update:** 17
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

#### 2026-06-03 - Unpaired RGB-Thermal Gaussian-Splatting Using Visual Geometric Transformers

**Authors:** Jean Cordonnier, Chenghao Xu, Olga Fink, Malcolm Mielle
**Links:** [abs](https://arxiv.org/abs/2606.05491) - [pdf](https://arxiv.org/pdf/2606.05491)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Unpaired RGB-Thermal Gaussian-Splatting Using Visual Geometric Transformers  
- 作者：Jean Cordonnier, Chenghao Xu, Olga Fink, Malcolm Mielle  
- 出版日期：2026-06-03  
- 分类：Geometry Foundation Models / Neural Scene Representations & Rendering  
- 链接：[摘要](https://arxiv.org/abs/2606.05491) | [PDF](https://arxiv.org/pdf/2606.05491)

### 一句话总结
提出一种无需配对校准的RGB-热成像新视角合成方法，利用视觉几何变换器（VGGT）独立估计各模态相机位姿，并通过Procrustes算法对齐，最终以多模态3D高斯泼溅实现联合渲染。

### 研究问题
如何在不依赖精确配对的RGB-热成像图像对或立体设备的情况下，实现多模态新视角合成，既保证热成像视图合成质量，又维持RGB渲染的保真度，并确保跨模态场景重建的一致性。

### 核心思路/方法
1. **位姿独立估计**：使用3D前馈变换器架构VGGT，分别从RGB和热成像图像独立估算每组图像的相机位姿。  
2. **跨模态对齐**：通过跨模态特征匹配器提取对应点，再运用Procrustes算法将两个模态的位姿集映射到同一坐标系，实现无配对校准的联合注册。  
3. **多模态高斯泼溅**：在对齐基础上，提出直接从未配对RGB和热成像图像中学习的3D高斯泼溅方法，实现联合场景表示与新视角渲染。  
4. **基准评估框架**：设计专门评估单模态图像合成质量与跨模态重建一致性的基准测试。

### 主要贡献
- 首次解决无配对RGB-热成像新视角合成问题，消除对精确校准或立体设置的依赖。  
- 利用VGGT与Procrustes对齐实现跨模态位姿联合估计，拓展了多模态场景重建的实用性与可扩展性。  
- 提出多模态3D高斯泼溅方法，在保持RGB渲染质量的同时实现热成像视图合成。  
- 引入评估框架，可严格度量单模态合成效果与重建场景的多模态一致性。

### 局限性
摘要未提供足够信息：未提及方法对极端环境（如光照、温度变化）的鲁棒性、计算开销或跨模态特征匹配的失败案例分析。

### 阅读优先级
**高**  
理由：该工作针对多模态新视角合成中的实际瓶颈（缺乏配对数据）提出创新性方案，结合前沿的VGGT与3D高斯泼溅，在理论框架与评估方法上均有特色，对几何基础模型与场景渲染方向的研究者具有直接参考价值。同时，其公开的基准评估框架可能成为后续相关工作的标准。

</details>

<details>
<summary>Abstract</summary>

Multi-modal novel view synthesis (NVS) combining RGB and thermal imagery enables precise 3D scene reconstruction with visual and thermal information. However, existing methods typically rely on precisely calibrated RGB-thermal image pairs or stereo setups, limiting scalability and practical deployment. To address this, we introduce a framework for unpaired RGB-thermal NVS that leverages VGGT, a 3D feed-forward transformer architecture, to independently estimate camera poses for each modality. The pose sets are then aligned using the Procrustes algorithm with a cross-modal feature matcher, enabling joint registration without paired calibration. Building on this alignment, we further propose a multi-modal 3D Gaussian Splatting approach that learns directly from unpaired RGB and thermal images. Experiments on diverse scenes demonstrate that our method achieves competitive performance in thermal view synthesis while maintaining RGB fidelity. Moreover, we show that existing reconstruction approaches can produce modality-specific reconstructions that lack cross-modal consistency. We thus introduce a benchmarking framework to rigorously evaluate both per-modality image synthesis and the multi-modal coherence of reconstructed scenes.

</details>

#### 2026-06-03 - Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping

**Authors:** Peilin Tao, Chong Cheng, Yuansen Du, Caiwei Song, Zhengqing Chen, Xiaoyang Guo, Wei Yin, Weiqiang Ren, Qian Zhang, Hainan Cui, Shuhan Shen
**Links:** [abs](https://arxiv.org/abs/2606.05035) - [pdf](https://arxiv.org/pdf/2606.05035)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** pointmap, feed-forward reconstruction, feed-forward 3D reconstruction, 3D reconstruction, dense reconstruction, robot perception, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping
- 作者：Peilin Tao, Chong Cheng, Yuansen Du, Caiwei Song, Zhengqing Chen, Xiaoyang Guo, Wei Yin, Weiqiang Ren, Qian Zhang, Hainan Cui, Shuhan Shen
- 出版日期：2026-06-03T16:00:13Z
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications（副分类）
- 链接：摘要：https://arxiv.org/abs/2606.05035，PDF：https://arxiv.org/pdf/2606.05035

### 一句话总结
Anchor3R提出一种基于瞬态锚点的流式三维重建框架，通过将重建视为当前帧坐标系下的局部相对测量预测，避免了固定坐标系带来的漂移和注意力偏差，适用于长时程在线视觉地图构建。

### 研究问题
现有流式前馈三维重建模型通常将预测固定在第一个帧或持久场景记忆的坐标系中，导致训练-测试不匹配、对早期锚点的注意力偏置以及在远长于训练序列的长序列上累积漂移。核心问题是：如何设计对长时程在线视觉映射鲁棒的流式三维重建方法，且不依赖全局固定坐标系。

### 核心思路/方法
- 将前馈三维重建视为“当前帧为中心”的局部测量预测，而非持久全局坐标回归。
- 在每个时间步，Anchor3R预测窗口内相对相机姿态和当前帧坐标系下的局部点图（pointmap）。
- 将流式重建转化为相对姿态测量生成，支持在线姿态更新。
- 通过闭环重插入和运动平均对齐轨迹，并将局部点图转换为一致的全局重建。

### 主要贡献
- 提出了Anchor3R框架，采用瞬态锚点设计，将流式重建任务转化为当前帧局部的相对测量预测。
- 解决了固定坐标系方法在长序列上的漂移和注意力偏置问题。
- 在室内、室外、驾驶和RGB-D基准上，相比现有流式基线，提升了长时程姿态精度和密集重建质量，并支持有界内存在线推理。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文针对机器人视觉映射中长时程流式重建的漂移问题提出新颖的瞬态锚点框架，实验覆盖多种场景和传感器类型，且强调有界内存在线推理，对三维重建、机器人感知及实时SLAM领域具有直接借鉴价值。

</details>

<details>
<summary>Abstract</summary>

Long-horizon online visual mapping is a core capability for robot perception, requiring continuous camera-motion and scene-geometry estimation from visual streams under bounded memory and computation. Recent feed-forward 3D reconstruction models provide strong geometric priors, but their streaming variants often predict poses in a fixed coordinate system tied to the first frame or a persistent scene memory. This fixed-gauge design leads to train--test mismatch, attention bias toward early anchors, and accumulated drift on sequences much longer than those seen during training. We propose \emph{Anchor3R}, a streaming 3D reconstruction framework that treats feed-forward reconstruction as current-centric local measurement prediction rather than persistent global-gauge regression. At each time step, Anchor3R predicts window-relative poses and a local pointmap in the current-frame coordinate system, turning streaming reconstruction into relative-pose measurement generation. These measurements support online pose updates, while loop-closure reinsertion and motion averaging align the trajectory and transform local pointmaps into a coherent global reconstruction. Experiments on indoor, outdoor, driving, and RGB-D benchmarks show that Anchor3R improves long-horizon pose accuracy and dense reconstruction quality over existing streaming baselines, while supporting bounded-memory online inference.

</details>

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-04 - GS-NFS: Bandwidth-adaptive Streaming of Dynamic Gaussian Splats and Point Clouds

**Authors:** Rajrup Ghosh, Haodong Wang, Haoran Hong, Eduardo Pavez, Amartya Chaudhuri, Weiwu Pang, Harsha V. Madhyastha, Antonio Ortega, Ramesh Govindan
**Links:** [abs](https://arxiv.org/abs/2606.05650) - [pdf](https://arxiv.org/pdf/2606.05650)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-NFS: Bandwidth-adaptive Streaming of Dynamic Gaussian Splats and Point Clouds
- 作者：Rajrup Ghosh, Haodong Wang, Haoran Hong, Eduardo Pavez, Amartya Chaudhuri, Weiwu Pang, Harsha V. Madhyastha, Antonio Ortega, Ramesh Govindan
- 出版日期：2026-06-04
- 分类：Dynamic / 4D Reconstruction（主类），Neural Scene Representations & Rendering（副类）
- 链接：摘要地址 https://arxiv.org/abs/2606.05650 | PDF地址 https://arxiv.org/pdf/2606.05650

### 一句话总结
GS-NFS 提出了一套基于GPU的高效并行压缩与解压缩方法，使得动态3D高斯泼溅（3DGS）帧的编解码速度达到实时帧率，同时保持与现有技术相当的压缩性能和渲染质量。

### 研究问题
动态3D高斯泼溅（3DGS）帧的压缩与解压缩速度过慢，无法满足实时流媒体应用的需求；现有压缩技术难以在GPU上高效加速。

### 核心思路/方法
开发了针对高斯元素位置和属性的新型GPU并行化版本，对现有编解码算法进行加速，使得动态3DGS帧的编码和解码能够在GPU上以全帧率运行。

### 主要贡献
- 提出GS-NFS系统，将动态3DGS帧的编解码速度提升至实时帧率。
- 在编码和解码速度上，比现有最先进方法快1-2个数量级。
- 在压缩性能和渲染质量方面，与现有技术具有竞争力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接解决了动态3DGS流媒体中的关键瓶颈（编解码速度），且性能提升显著（1-2个数量级），对于实时4D重建和神经场景表示领域的研究者或工程实践者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (3DGS) holds great promise as a 3D video streaming technology since it can represent complex 3D scenes with high fidelity. In this approach, every frame in a 3D video represents the environment as a collection of Gaussians with position and other attributes such as scale, rotation, opacity, and color. Frames capture fine details, permit views from any arbitrary perspective, but are an order of magnitude, or more, larger than 2D video frames. A line of recent work has explored how to compress dynamic 3DGS frames, but these approaches are often slow, in part because their compression techniques are not amenable to efficient acceleration. GS-NFS accelerates dynamic 3DGS compression and decompression on a GPU, to the point where it can encode and decode at full frame rate. It achieves this by developing novel GPU-based parallelizations of existing algorithms for encoding both positions and attributes of Gaussians. As a result, it is 1-2 orders of magnitude faster than the state-of-the-art in encoding and decoding a frame, while offering competitive compression performance and rendering quality.

</details>

#### 2026-06-03 - 4D Reconstruction from Sparse Dynamic Cameras

**Authors:** Kazuki Ozeki, Shun Kenney, Yuto Shibata, Eisuke Takeuchi, Takuya Narihira, Kazumi Fukuda, Ryosuke Sawata, Yuki Mitsufuji, Yoshimitsu Aoki
**Links:** [abs](https://arxiv.org/abs/2606.04593) - [pdf](https://arxiv.org/pdf/2606.04593)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, dynamic 3D, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4D Reconstruction from Sparse Dynamic Cameras
- 作者：Kazuki Ozeki, Shun Kenney, Yuto Shibata, Eisuke Takeuchi, Takuya Narihira, Kazumi Fukuda, Ryosuke Sawata, Yuki Mitsufuji, Yoshimitsu Aoki
- 出版日期：2026-06-03
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要: https://arxiv.org/abs/2606.04593; PDF: https://arxiv.org/pdf/2606.04593

### 一句话总结
本文针对稀疏动态相机（多台独立移动相机）的4D重建任务，提出了一种通过跨相机特征匹配与单相机点跟踪结合实现的3D轨迹初始化方法，并引入噪声鲁棒的深度排序正则化损失与时空多样批次采样策略，同时发布了新数据集LetCamsGo，在动态区域重建质量上优于现有基线方法。

### 研究问题
如何从少量独立移动的稀疏动态相机（如体育、音乐会等实际视频制作场景）中，实现高质量的4D（动态3D）重建，克服现有方法无法处理复杂时空不一致性的局限。

### 核心思路/方法
1. 提出一种简单有效的3D轨迹初始化方法，通过集成跨相机的特征匹配（inter-camera feature matching）与单相机内的点跟踪（intra-camera point tracking），来保证时空一致性。
2. 引入噪声鲁棒的深度排序正则化损失（noise-robust depth-ordering regularization loss）和时空多样批次采样策略（spatiotemporally diverse batch sampling strategy），以提升优化稳定性与跨视角泛化能力。
3. 为解决缺少标准基准的问题，构建了新真实世界视频数据集LetCamsGo，包含5个序列、4种不同环境，由3台独立移动相机和1台固定相机记录。

### 主要贡献
- 识别了现有单目或密集固定相机方法在处理稀疏动态相机设置时的不足，并通过实验验证其失败原因。
- 提出针对稀疏动态相机的4D重建框架，核心创新在于3D轨迹初始化方法及配套的正则化与采样策略。
- 提供了全新的真实世界数据集LetCamsGo，为后续研究建立了标准化基准。
- 在LetCamsGo上的全面基准测试表明，所提框架在动态区域的重建质量优于基线方法，推动了低成本野外4D重建的发展。

### 局限性
摘要未提供足够信息（例如未讨论方法对相机数量、运动幅度或计算成本的限制，也未明确说明失败案例或改进空间）。

### 阅读优先级
**高**。理由：该工作聚焦于一个实际且低成本的4D重建设定（稀疏动态相机），并提供了完整的方法、新数据集和量化改进结果，对于研究动态场景重建或多视角视频处理的读者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Although dynamic 3D (i.e., 4D) reconstruction from a monocular dynamic camera has recently advanced, it remains fundamentally limited by depth ambiguity. In this paper, we focus on an alternative practical way, i.e., sparse dynamic camera setup, where a handful of independently moving cameras capture the same subjects. While keeping capture costs low, this setup introduces multi-view constraints and remains practical for real-world video production such as sports, concerts, and TV shows. Despite its potential, our experiments show that naive extensions of existing monocular or dense-fixed camera-based methods are insufficient since they fail to resolve the complex spatiotemporal inconsistencies across views and time. To fill this gap, we propose a simple yet effective 3D track initialization method designed to ensure spatiotemporal consistency by integrating inter-camera feature matching with intra-camera point tracking. Additionally, we incorporate a noise-robust depth-ordering regularization loss and a spatiotemporally diverse batch sampling strategy to enhance optimization stability and cross-view generalization. Furthermore, to address the lack of standardized benchmarks for this task, we introduce LetCamsGo, a new real-world video dataset with 5 sequences across 4 diverse environments, recorded by three independently moving cameras and one fixed camera. Comprehensive benchmarking on LetCamsGo demonstrated that our proposed framework improves 4D reconstruction quality in dynamic regions compared with baselines, paving the way for a low-cost 4D reconstruction paradigm in the wild.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

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

#### 2026-06-06 - G2G: Exploiting Intra-Group Geometry for Inter-Group Pose Estimation

**Authors:** Yufei Wei, Shuhao Ye, Chenxiao Hu, Yiyuan Pan, Dongyu Feng, Rong Xiong, Yue Wang, Yanmei Jiao
**Links:** [abs](https://arxiv.org/abs/2606.08284) - [pdf](https://arxiv.org/pdf/2606.08284)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, simulation

<details>
<summary>AI 简析</summary>

好的，以下是基于您提供的论文元数据和摘要的简体中文简要分析。

### Metadata
- 标题：G2G: Exploiting Intra-Group Geometry for Inter-Group Pose Estimation
- 作者：Yufei Wei, Shuhao Ye, Chenxiao Hu, Yiyuan Pan, Dongyu Feng, Rong Xiong, Yue Wang, Yanmei Jiao
- 出版日期：2026-06-06
- 分类：3D Reconstruction & Multi-view Geometry (三维重建与多视角几何)
- 链接：摘要地址: https://arxiv.org/abs/2606.08284 | PDF地址: https://arxiv.org/pdf/2606.08284

### 一句话总结
本文提出G2G方法，通过冻结预训练多视角骨干网络，并仅添加三个轻量级可训练模块（总参数量约32M，占全模型6%以下），实现了两幅图像组之间的精确6自由度相对位姿估计。

### 研究问题
如何高效地估计两个图像组（每个组内已知其几何结构）之间的相对6自由度位姿，以支持跨序列重定位和多相机系统里程计等任务。现有方法将所有视角视为无序集合，缺乏组间的推理能力。

### 核心思路/方法
核心思路是保持预训练的多视角骨干网络完全冻结，仅添加三个轻量级可训练“桥接”模块来连接两个图像组：
1.  **感知器重采样器 (Perceiver Resampler)**：用于处理图像特征。
2.  **交叉组桥接模块 (Cross-group bridge with merged self-attention)**：通过融合自注意力机制实现组间的信息交互。
3.  **多帧位姿头 (Multi-frame pose head)**：用于输出位姿估计。
模型仅使用相对位姿作为监督信号进行训练。

### 主要贡献
1.  提出了一个新颖的G2G框架，能够在不微调预训练骨干网络的情况下，有效利用组内几何信息进行组间位姿估计。
2.  方法在室内/室外模拟、真实跨季节捕获、零样本模拟到真实迁移等多个数据集上，在两项任务（相对位姿估计）中均达到了最先进的精度。
3.  所有基线方法都在完整原始监督下重新训练，而G2G模型仅在相对位姿监督下训练，表明了方法的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

**理由：**
该论文针对计算机视觉中一个明确且实用的定位与位姿估计问题（组间位姿估计）提出了一个新颖的轻量化方案，通过在保持预训练大模型不变的情况下加入少量可训练模块，在多个数据集上取得了最先进结果。这种方法在效率和效果上均表现出优势，且代码已开源，对从事相关领域（如SLAM、多相机系统、视觉定位）的研究人员和工程师具有较高的参考和复现价值。

</details>

<details>
<summary>Abstract</summary>

Recovering the relative 6-DoF pose between two image groups underlies cross-sequence relocalization and multi-camera rig odometry. Each group carries known intra-group geometry from visual odometry or rig calibration, and pretrained multi-view backbones already fuse such geometry into visual features. Yet current models treat all views as an unstructured set, leaving cross-group reasoning as the missing piece. We introduce \ours{}, which keeps the foundation model entirely frozen and adds three lightweight trainable modules to bridge the two groups: a perceiver resampler, a cross-group bridge with merged self-attention, and a multi-frame pose head. The trainable footprint totals about 32M parameters, under 6\% of the full model, and is supervised only by relative poses. Across four datasets that span indoor and outdoor simulation, real-world cross-season capture, and zero-shot sim-to-real transfer, \ours{} attains state-of-the-art accuracy on both tasks, while every baseline is retrained with its full original supervision. Code is available at https://github.com/WeiYuFei0217/G2G.

</details>

#### 2026-06-04 - LiAuto-GeoX: Efficient Grounded Driving Transformer

**Authors:** Jiawei Lian, Haoyi Sun, Yang Wu, Lifu Mu, Siyuan Wang, Le Hui, Ning Mao, Tao Wei, Pan Zhou, Kun Zhan, Jian Yang
**Links:** [abs](https://arxiv.org/abs/2606.05774) - [pdf](https://arxiv.org/pdf/2606.05774)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, dense reconstruction, autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LiAuto-GeoX: Efficient Grounded Driving Transformer
- 作者：Jiawei Lian, Haoyi Sun, Yang Wu, Lifu Mu, Siyuan Wang, Le Hui, Ning Mao, Tao Wei, Pan Zhou, Kun Zhan, Jian Yang
- 出版日期：2026-06-04
- 分类：3D Reconstruction & Multi-view Geometry / Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2606.05774) | [PDF](https://arxiv.org/pdf/2606.05774)

### 一句话总结
LiAuto-GeoX 是一个用于自动驾驶的高效、可部署的接地驾驶Transformer，它通过蒸馏大容量几何模型为紧凑的155M参数模型，实现了实时（KITTI上220 FPS）的稠密3D重建，并展示了该几何表示在多项下游任务中的显著性能。

### 研究问题
如何在自动驾驶场景中实现一种实时、高保真、且具有远距离几何准确性和环视一致性的自车中心稠密3D重建表示，并将其作为可扩展的基础几何表示服务于下游任务。

### 核心思路/方法
1. **学习大容量驾驶几何模型**：利用大规模环视数据，并结合稀疏LiDAR先验，在模糊或结构稀疏区域提供鲁棒的几何基础。
2. **几何保持蒸馏框架**：将大容量模型的能力蒸馏到一个155M参数的紧凑车载模型中。该框架包含两项关键蒸馏技术：
   - **掩码引导的深度感知蒸馏**：通过强调几何信息丰富的区域来保留精细度量结构。
   - **相对位姿关系蒸馏**：通过位姿诱导的几何关系强制学习跨视图的空间一致性。

### 主要贡献
1. 提出了LiAuto-GeoX，一个用于自动驾驶的高效、可部署的接地驾驶Transformer，能够进行实时稠密3D重建。
2. 设计了一个新颖的几何保持蒸馏框架，成功将大容量几何模型压缩至155M参数的紧凑模型，同时维持重建质量。
3. 在KITTI上实现了220 FPS的高效运行，证明其实时部署潜力。
4. 展示了学到的几何表示可无缝迁移至下游任务，并在轨迹预测、占用预测和未来帧预测上取得了先进性能（分别为90.6 PDMS、24.63 mIoU和47.67 IoU）。

### 局限性
摘要未提供足够信息。未提及模型的失败案例、对极端天气或光照条件的鲁棒性、以及蒸馏过程是否引入特定精度损失等局限性。

### 阅读优先级
**高**。理由：论文针对自动驾驶中稠密3D重建的实时部署这一核心挑战，提出了明确且创新的方法（蒸馏+几何保持）。实验表明其在高速度运行同时显著提升了多项下游任务性能，对于自动驾驶感知和几何表示的研究者具有重要的参考价值。

</details>

<details>
<summary>Abstract</summary>

Dense 3D reconstruction has demonstrated immense potential for spatial understanding, yet its viability as a real-time, onboard representation for autonomous driving remains an open challenge. Existing large-scale visual geometry models typically require substantial computational resources and lack the long-range geometric fidelity, surround-view consistency, and real-time efficiency demanded by dynamic driving environments. To bridge this gap, we present \textbf{LiAuto-GeoX}, an efficient grounded driving transformer designed for deployable, ego-centric 3D scene understanding. Our approach begins by learning a high-capacity driving geometry model from large-scale surround-view data, utilizing sparse LiDAR priors to provide robust geometric grounding in distant, ambiguous, or structure-sparse regions. We then instantiate this capability into a highly compact 155M-parameter onboard model through a novel geometry-preserving distillation framework. This framework employs mask-guided depth-aware distillation to retain fine-grained metric structures by emphasizing geometrically informative regions, and relative-pose relational distillation to enforce cross-view spatial consistency through pose-induced geometric relations. Extensive evaluations reveal that \textbf{LiAuto-GeoX} runs at 220 FPS on KITTI while maintaining high-fidelity dense reconstruction, enabling real-time deployment. The learned geometry transfers seamlessly to downstream autonomy tasks, achieving 90.6 PDMS in trajectory prediction, 24.63 mIoU in occupancy prediction, and 47.67 IoU in future-frame prediction. These all demonstrate that efficient dense 3D reconstruction can transcend its traditional role as a perception target to serve as a scalable, foundational geometric representation for next-generation autonomous driving.

</details>

#### 2026-06-03 - CIPER: A Unified Framework for Cross-view Image-retrieval and Pose-estimation

**Authors:** Yurim Jeon, Dongseong Seo, Seung-Woo Seo
**Links:** [abs](https://arxiv.org/abs/2606.05011) - [pdf](https://arxiv.org/pdf/2606.05011)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CIPER: A Unified Framework for Cross-view Image-retrieval and Pose-estimation
- 作者：Yurim Jeon, Dongseong Seo, Seung-Woo Seo
- 出版日期：2026-06-03
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：arXiv:2606.05011

### 一句话总结
本文提出CIPER，一个统一框架，通过共享Transformer编码器和任务特定令牌，同时实现跨视图地理定位中的城市级图像检索和精确3自由度位姿估计。

### 研究问题
现有跨视图地理定位方法要么侧重宽范围检索但精度低，要么侧重高精度位姿估计但搜索空间窄；级联两种管道会导致误差传播和特征表示不一致。因此，如何同时实现大规模检索和高精度位姿估计是一个开放挑战。

### 核心思路/方法
- 使用共享Transformer编码器，并引入任务特定令牌（task-specific tokens）来分离全局检索特征和空间定位线索。
- 设计双向Transformer位姿解码器（two-way transformer pose decoder），利用地面特征作为空间查询进行双向交叉注意，弥合地面与空中视图之间的域差距。
- 采用集合预测策略（set prediction）实现统一的3自由度回归，在单一多任务目标下优化。

### 主要贡献
- 首次将跨视图地理定位形式化为同时需要城市级检索和精确3自由度位姿估计的统一问题。
- 提出CIPER架构，通过共享特征学习和任务解耦令牌实现检索与位姿估计的联合执行。
- 在VIGOR、KITTI和Ford Multi-AV数据集上展示了竞争性能，尤其在有限视场角和任意朝向条件下表现突出。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：本文针对跨视图地理定位中检索和位姿估计分离的痛点，提出了统一框架，思路清晰且方法具有创新性。实验在多个基准数据集上验证了性能优势，适合关注地理定位、3D重建或多视图几何方向的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Cross-view geo-localization estimates the geographic location of a ground image by matching it against an aerial image database. Existing methods tackle this through either large-scale retrieval or precise pose estimation, but not both: retrieval-based methods enable wide-area search at the cost of localization accuracy, while pose estimation methods achieve high precision within only a narrow search space. Naively cascading these pipelines introduces error propagation and inconsistent feature representations. We formulate cross-view geo-localization as a unified problem requiring simultaneous city-scale retrieval and precise 3-DoF pose estimation. We propose CIPER (Cross-view Image-retrieval and Pose-estimation transformER), a single architecture that jointly performs both tasks through mutually beneficial feature learning. CIPER uses a shared transformer encoder with task-specific tokens to disentangle global retrieval features from spatial localization cues. To bridge the large domain gap between ground and aerial views, we introduce a two-way transformer pose decoder that uses ground features as spatial queries for bidirectional cross-attention. A set prediction strategy further enables stable 3-DoF regression under a unified multi-task objective. Experiments on VIGOR, KITTI, and Ford Multi-AV demonstrate competitive performance, especially under limited field-of-view and arbitrary orientation conditions. Code is available at https://github.com/yurimjeon1892/CIPER.

</details>

#### 2026-06-03 - Multi-Camera AR Guidance System for Surgical Instrument Handling and Assembly: Investigating Workload and Efficiency

**Authors:** Shiyu Li, Julian Kreimeier, Hannah Schieber, Dirk Müller, Bernhard Kainz, Rüdiger von Eisenhart-Rothe, Daniel Roth
**Links:** [abs](https://arxiv.org/abs/2606.04992) - [pdf](https://arxiv.org/pdf/2606.04992)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, camera calibration, localization, AR, augmented reality, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-Camera AR Guidance System for Surgical Instrument Handling and Assembly: Investigating Workload and Efficiency
- 作者：Shiyu Li, Julian Kreimeier, Hannah Schieber, Dirk Müller, Bernhard Kainz, Rüdiger von Eisenhart-Rothe, Daniel Roth
- 出版日期：2026-06-03T15:13:05Z
- 分类：3D Reconstruction & Multi-view Geometry（主）；Embodied / Robotics / AR Applications（次）
- 链接：摘要：https://arxiv.org/abs/2606.04992 / PDF：https://arxiv.org/pdf/2606.04992

### 一句话总结
本文提出一种结合多相机6D位姿估计和头戴式AR显示的手术器械引导系统，能显著降低器械护士的认知负荷并缩短任务完成时间。

### 研究问题
如何通过无标记的多相机AR引导系统，降低手术器械（尤其是陌生器械）处理与组装过程中器械护士的高认知负荷，并提升操作效率。

### 核心思路/方法
- 系统结合多相机6D位姿估计与头戴式AR就地可视化（无需额外标记）。
- 位姿估计与相机标定通过已知物体实现；6D位姿估计网络仅使用合成数据训练，以提升泛化性和真实世界适用性。
- AR引导显示工具尖端定位提示和逐步装配动画，用户通过注视选择和脚踏板在术中切换步骤。
- 在膝关节置换手术模拟中，对29名器械护士进行用户研究，与纸质手册对比，评估工作负荷、完成时间、错误频率和定性反馈。

### 主要贡献
1. 提出无标记多相机AR引导系统，改善了手术器械操作的主观与客观表现。
2. 技术评估中，该方法在6D位姿估计上优于现有方法。
3. 用户研究显示：AR引导显著降低感知工作负荷；客观上将任务完成时间缩短21.3%（4.76分钟）；尤其对不熟悉器械的护士获益明显；错误频率与对照条件相当；定性反馈显示过程清晰度提升、信息过载减少及感知独立性增强。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接针对真实手术场景中器械护士的认知负担问题，结合多视角计算机视觉与AR技术，并通过大规模用户研究（29名专业人员）验证了系统在降低负荷和提升效率方面的效果，具有较强的实际应用潜力和研究价值。

</details>

<details>
<summary>Abstract</summary>

The handling and assembly of instruments during surgery imposes high cognitive demands on scrub nurses, particularly when instruments are unfamiliar. We present a supporting guidance system for surgical instrumentation that combines multi-camera 6D pose estimation with augmented reality in-situ visualization on a head-mounted display without the requirement for additional markers. Pose estimation and consecutive camera calibration are achieved through known objects. The 6D pose estimation network is trained purely on synthetic data, aiming for better generalizability and real-world applicability. The AR guidance displays tooltip localization cues and step-wise assembly animations. Via gaze-based selection and a foot pedal, users can switch between assembly steps in intraoperative use. In a technical evaluation, our approach outperforms state-of-art 6D pose estimation. A user study with 29 scrub nurses was conducted in a surgical simulation of knee arthroplasty, comparing the system against a paper manual. AR guidance significantly reduced the perceived workload compared. Objectively, AR guidance reduced task completion time by 21.3\% (4.76 minutes). Specifically, scrub nurses less experienced with the instrument set benefited when using the system. Error frequencies were comparable between conditions. Qualitative feedback highlighted improved process clarity, reduced information overload, and perceived independence. To summarize, our marker-free multi-camera AR guidance approach for surgical instruments can, subjectively and objectively, improve intraoperative instrumentation performance, particularly for untrained scrub nurses.

</details>

#### 2026-06-03 - Hierarchical Space Partition for Surface Reconstruction

**Authors:** Minjie Tang, Xiangfei Li
**Links:** [abs](https://arxiv.org/abs/2606.04891) - [pdf](https://arxiv.org/pdf/2606.04891)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** surface reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hierarchical Space Partition for Surface Reconstruction  
- 作者：Minjie Tang, Xiangfei Li  
- 出版日期：2026-06-03T13:52:36Z  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：abstract: https://arxiv.org/abs/2606.04891 | pdf: https://arxiv.org/pdf/2606.04891  

### 一句话总结
提出一种基于层级空间分割的平面组装策略，通过恢复点云中缺失的细节并保持模型紧凑性，生成水密多边形网格。

### 研究问题
如何从存在信息缺失（如LiDAR扫描的视野限制和遮挡）的点云中，生成紧凑且准确恢复缺失细节的二维多边形表面模型。

### 核心思路/方法
1. 将场景中提取的所有平面分为三类：高度可见、几乎不可见、不可见。  
2. 通过场景结构分析恢复“不可见”平面，以指示缺失细节。  
3. 三类平面对应三种生长优先级，依据优先级逐步生长，实现层级空间分割。  
4. 基于分割结果，通过最小割优化生成水密多边形网格。

### 主要贡献
1. 提出一种平面组装策略，能有效恢复点云中的缺失信息。  
2. 引入基于三类平面优先级的层级空间分割方法。  
3. 通过最小割优化生成水密多边形网格，并在公共数据集上验证了方法的有效性和优越性。

### 局限性
摘要未提供足够信息，例如未说明方法的计算效率、对噪声或异常点的鲁棒性，以及在不同场景类型（如大规模户外或室内）下的具体表现。

### 阅读优先级
**中**。  
理由：该方法针对点云表面重建中的信息缺失问题提出了创新性的层级分割和缺失恢复策略，但摘要未提供详细实验对比或局限性分析，若对表面重建或点云处理感兴趣可进一步阅读。

</details>

<details>
<summary>Abstract</summary>

Generating compact polygonal models from point clouds is a key problem in 3D vision and computer graphics. However, due to inherent limitations of LiDAR scanning (e.g. range constraints and occlusions), critical scene information is often missing, leading to degraded reconstruction accuracy. To address this, we propose a plane assembling strategy that effectively recovers missing details while maintaining model compactness. We classify all the planes extracted from the scene into three categories: highly visible, barely visible, and invisible. The invisible planes, which are recovered by scene structure analysis, indicate the missing details. The three types of planes correspond to the three growth priorities. Each plane grows according to the priority level, and the space is partitioned progressively, namely, the hierarchical partition. Subsequently, we generate a watertight polygonal mesh from the partition via a min-cut-based optimization. Finally, comparisons on public datasets show the effectiveness and superiority of our method against mainstream approaches. The project page is available at https://hsr-3dv.github.io/.

</details>

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
- 分类：3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2606.03994

### 一句话总结
提出SimuScene，一种从单张图像重建物理稳定的组合式3D场景的管道，其核心创新在于利用物理仿真引擎作为诊断工具，在生成过程中反馈修正形状与布局误差，而非仅作为后处理。

### 研究问题
如何从单张图像重建出可直接用于物理仿真（无穿透、悬空、下沉等物理不稳定现象）的组合式3D场景，克服现有单图提升方法在生成后因形状和布局误差导致的仿真崩溃问题。

### 核心思路/方法
1. **物理在环（Physics-in-the-Loop）**：将物理引擎（如重力仿真）用于生成过程中的诊断，而非仅仅作为后处理布局修正。
2. **诊断性仿真**：对重建的物体施加重力进行仿真，将穿透和支撑失效等物理不稳定现象量化为校正信号。
3. **迭代反馈**：基于校正信号驱动重力轴上的拉伸和全图（amodal）形状重采样，从而在形状和布局估计阶段纳入物理约束，减少累积误差，最终输出稳定的仿真就绪场景。

### 主要贡献
1. 提出一种新的组合式3D重建方法，在形状和布局估计中融入物理约束（而非仅后处理）。
2. 利用物理引擎作为诊断测量工具，将物理不稳定转化为定量信号指导生成过程。
3. 在物理稳定性和几何对齐基准上达到最先进性能，并通过人形控制和机械臂操作任务展示了实际应用价值。

### 局限性
摘要未提供关于方法局限性的信息，例如对物体类别、输入图像质量、计算复杂度或极端物理场景（如复杂关节或可变形物体）的适应性等细节。

### 阅读优先级
高。理由：该工作针对机器人操作和物理仿真中的关键瓶颈（单图场景重建的物理稳定性），提出了创新的“物理在环”反馈框架，方法新颖且实验验证了在稳定性基准和具体任务上的有效性，对3D重建与具身智能交叉领域有显著参考价值。

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

### Metadata
- 标题：PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation
- 作者：Shinjeong Kim, Ignacio Alzugaray, Callum Rhodes, Paul H. J. Kelly, Andrew J. Davison
- 出版日期：2026-06-02T17:59:22Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2606.03989；PDF: https://arxiv.org/pdf/2606.03989；项目页面: https://www.shinjeongkim.com/pixvod/

### 一句话总结
本文提出一种完全可并行化的像素级视觉里程计与深度估计方法PixVOD，通过高斯置信传播（GBP）在传感器像素间分布式计算，并引入关键帧锚定机制以保证优化稳定性。

### 研究问题
如何设计一种可在传感器像素间完全并行化运行的视觉里程计与深度估计方法，以降低从传感器传输冗余像素数据的开销，并利用像素级计算为高层视觉任务提供更丰富的输入。

### 核心思路/方法
- 提出完全可并行化的视觉里程计和深度估计范式，使传感器处理器中的每个像素都能独立参与计算。
- 采用高斯置信传播（GBP）在像素间交换信息，以协同估计相机运动，并从每个像素的光度观测和表面法线先验中推断深度。
- 引入类似关键帧的锚定机制，调节帧间有效基线，从而在优化过程中保持几何稳定性，实现一致的相机运动与深度更新。

### 主要贡献
1. 提出首个基于GBP的像素级分布式视觉里程计与深度估计框架。
2. 设计了关键帧锚定机制，有效维持了像素级分布式优化中的几何稳定性。
3. 在真实数据集上验证了该方法在传感器处理器上实现分布式计算的可行性。

### 局限性
摘要未提供足够信息（未提及量化误差分析、计算复杂度、对传感器硬件的具体依赖或失败案例等）。

### 阅读优先级
中。理由：该方法在传感器计算和分布式视觉领域具有新颖性，适合对焦平面处理或片上视觉系统感兴趣的读者；但摘要未展示与传统方法的定量对比性能，实验细节有限，可能对需要直接对比方法的读者价值中等。

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
- 标题：Multi-Robot Bearing-only Pose Estimation via Angle Rigidity
- 作者：J. Francisco Presenza, Leonardo J. Colombo, Ignacio Mas, Juan I. Giribet
- 出版日期：2026-06-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.03931

### 一句话总结
本文提出了一种基于角度刚性的分布式方位仅位姿估计方法，仅利用机器人间的方位测量和更弱的拓扑条件（角度刚性），可实现时变多机器人系统的位置和方向估计。

### 研究问题
如何在没有方向信息且拓扑条件更弱的分布式多机器人系统中，仅利用方位测量来估计机器人的三维位置和方向。

### 核心思路/方法
- 利用机器人本体坐标系中的方位角计算出的角度，估计机器人在 \(\mathbb{R}^3\) 中的位置。
- 从估计位置、方位及其导数恢复出机器人在 \(\mathrm{SO}(3)\) 中的方向。
- 要求感知拓扑满足“角度刚性”条件，该条件弱于常用的方位刚性。
- 在部分机器人的运动持续激励假设下，建立了观测器的局部一致指数稳定性。

### 主要贡献
1. 提出了一种新的分布式方位仅姿态估计器，适用于时变多机器人系统。
2. 将所需的拓扑条件从传统方位刚性放宽为更弱的“角度刚性”。
3. 通过理论分析证明了观测器的局部一致指数稳定性。
4. 通过仿真验证了方案的有效性和实用性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**
理由：该论文在分布式机器人状态估计领域提出了新的理论条件（角度刚性），并给出了稳定性证明，对相关方向的研究者有一定参考价值。但由于未提供与现有方法的定量对比结果，且缺乏实验细节，实用性评估有限。建议有具体兴趣的读者进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

This letter proposes a novel distributed bearing-based pose estimator for time-varying multi-robot systems. The method uses angles computed from body-frame bearings to estimate the robots' positions in $\mathbb{R}^3$ without knowledge of their orientations. The orientations in $\mathrm{SO}(3)$ are recovered from the estimated positions, the bearings, and the bearing derivatives. The proposed observer only requires the (directed) sensing topology to be \textit{angle-rigid}, a weaker condition than the commonly used ones like bearing rigidity. Local uniform exponential stability of the proposed observer is established under the assumption of persistently exciting motions for a subset of robots. Simulations are presented and discussed to evaluate the scheme's effectiveness and practicality.

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

#### 2026-06-05 - UniSHARP: Universal Sharp Monocular View Synthesis

**Authors:** Meixi Song, Dizhe Zhang, Hao Ren, Ruiyang Zhang, Bo Du, Ming-Hsuan Yang, Lu Qi
**Links:** [abs](https://arxiv.org/abs/2606.07514) - [pdf](https://arxiv.org/pdf/2606.07514)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniSHARP: Universal Sharp Monocular View Synthesis
- 作者：Meixi Song, Dizhe Zhang, Hao Ren, Ruiyang Zhang, Bo Du, Ming-Hsuan Yang, Lu Qi
- 出版日期：2026-06-05
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.07514

### 一句话总结
UniSHARP通过统一的全方位潜在空间对齐，将经典的针对针孔相机的视图合成方法SHARP扩展至支持透视、广角、鱼眼及全景等连续相机系统的单目渲染。

### 研究问题
如何克服SHARP方法对针孔相机模型的特定假设，使其能适用于多种不同相机系统（从常规透视到广角、鱼眼和全景）的通用单目视图合成。

### 核心思路/方法
核心思想是将不同图像统一到一个全方位的潜在空间进行隐式对齐。具体包括：
- 在特征空间和高斯空间中进行隐式对齐。
- 基于射线的通用表示，沿射线和径向距离排列高斯原语。
- 利用UniK3D启发的编码器提取2D语义和3D空间特征，共同解码生成完整的高斯云。

### 主要贡献
- 提出了UniSHARP，将SHARP扩展为适用于连续相机系统的通用单目渲染方法。
- 构建了一个覆盖多种成像系统和场景的基准测试，并按视场角分层以精细评估通用单目渲染任务。
- 在提出的基准上，UniSHARP大幅优于其他对比方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。
理由：该方法将流行的视图合成技术SHARP从针孔相机推广到鱼眼、全景等广泛相机系统，解决了单目渲染领域的通用性问题，并构建了分层基准进行系统评估。实验表现显著优于现有方法，具有重要的应用和学术价值。

</details>

<details>
<summary>Abstract</summary>

In this work, we focus on extending SHARP, the popular photorealistic view synthesis method, for universal monocular rendering across a continuum of camera systems, from conventional perspective cameras to wide-field-of-view, fisheye and omnidirectional panoramic settings. To overcome the pinhole-specific assumptions of SHARP, our key idea is to align various images in a unified omnidirectional latent space. Thus, we propose UniSHARP, which performs implicit alignment in both feature and Gaussian spaces. Specifically, Gaussian primitives are arranged along rays and radial distances in a ray-based universal representation, while 2D semantic and 3D spatial features extracted from UniK3D-inspired encoders are jointly decoded to generate the complete Gaussian cloud. To comprehensively evaluate our method, we construct a benchmark covering diverse imaging systems across various scenes. The benchmark is further stratified by field of view (FoV) to enable fine-grained assessment of the universal monocular rendering task. Extensive experiments on the proposed benchmark demonstrate the effectiveness of UniSHARP, outperforming alternative methods by a large margin. The project page can be found at: https://insta360-research-team.github.io/Unisharp-website/

</details>

#### 2026-06-04 - Texture-preserving implicit neural representation for Cone beam CT truncated reconstruction

**Authors:** Genyuan Zhang, Junyao Wang, Haoran Lan, Chuandong Tan, Songtao Zhu, Fenglin Liu
**Links:** [abs](https://arxiv.org/abs/2606.06039) - [pdf](https://arxiv.org/pdf/2606.06039)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, scene representation, neural scene representation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Texture-preserving implicit neural representation for Cone beam CT truncated reconstruction
- 作者：Genyuan Zhang, Junyao Wang, Haoran Lan, Chuandong Tan, Songtao Zhu, Fenglin Liu
- 出版日期：2026-06-04T11:33:21Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.06039

### 一句话总结
提出一种自监督的3D神经场景表示框架，结合物理迭代细化模块，在CBCT截断重建中同时实现无伪影外推与高频纹理保留。

### 研究问题
CBCT数据截断会导致严重伪影并限制有效视野，现有深度学习方法依赖有监督真值且无法处理连续3D空间截断变化，如何实现自监督、鲁棒的截断重建并保留高频纹理细节。

### 核心思路/方法
1. 采用自监督的3D神经场景表示框架，直接由空间坐标映射到辐射密度，在投影监督下训练，避免传统滤波反投影操作，从而消除截断引起的环状伪影并实现连续3D数据外推。
2. 针对坐标网络的频谱偏差导致高频纹理丢失，引入基于物理的迭代细化模块：以神经网络的伪影自由外推体素为初始值，从原始投影中逐步重提取并注入高频结构信息。

### 主要贡献
- 提出首个自监督3D神经场景表示框架用于CBCT截断重建（据摘要描述）。
- 通过神经网络结构从根本上消除截断导致的环状伪影，并实现鲁棒的连续3D外推。
- 引入物理迭代细化模块，在保持神经网络伪影抑制和外推优势的同时，恢复高频纹理细节。
- 在模拟和真实数据集上验证了该方法统一神经网络的伪影抑制能力与迭代算法的高保真细节保留能力。

### 局限性
摘要未提供足够信息：未具体说明在极端截断、噪声水平或计算时间等方面的局限性，也未给出定量实验结果或与基线方法的对比细节。

### 阅读优先级
**高**。理由：该工作针对CBCT截断重建这一真实临床难题，提出了创新性结合神经隐式表示与物理迭代细化的自监督方案，且在模拟和真实数据上验证了效果，对医学成像和神经渲染方向均有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Cone-beam computed tomography (CBCT) frequently suffers from data truncation, which introduces severe artifacts and limits the effective field of view (FOV). Existing deep learning methods for truncated cone-beam computed tomography (CBCT) reconstruction suffer from serious limitations, including a strict reliance on supervised ground truth and a failure to account for continuous 3D spatial truncation variations. To address these challenges, we introduce a self-supervised 3D reconstruction framework based on neural scene representations. By directly mapping spatial coordinates to radiodensity under projection supervision, our approach inherently bypasses traditional filtering and backprojection operations, thereby fundamentally eliminating truncation-induced ring artifacts while enabling robust continuous 3D data extrapolation. However, coordinate networks are susceptible to an inherent spectral bias, which leads to a severe loss of clinically vital high-frequency textures. To resolve this bottleneck, we further incorporate a physics-based iterative refinement module into the neural scene representation architecture. Leveraging the artifact-free, extrapolated volume from the coordinate network as an optimal initialization, this module progressively re-extracts and injects high-frequency structural information from the original projections back into the volume. Extensive experiments on both simulated and real-world datasets demonstrate that our method successfully unifies the exceptional artifact suppression and extrapolation capabilities of neural networks with the high-fidelity detail preservation of iterative algorithms.

</details>

#### 2026-06-03 - Geometry Gaussians: Decoupling Appearance and Geometry in Gaussian Splatting

**Authors:** Hongyu Zhou, Zorah Lähner
**Links:** [abs](https://arxiv.org/abs/2606.05124) - [pdf](https://arxiv.org/pdf/2606.05124)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry Gaussians: Decoupling Appearance and Geometry in Gaussian Splatting
- 作者：Hongyu Zhou, Zorah Lähner
- 出版日期：2026-06-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.05124

### 一句话总结
本文发现标准3D高斯溅射无法同时良好表达纹理与几何，并通过为每个溅射增加一个独立的几何不透明度参数，实现了外观与几何的解耦，提升了渲染与几何重建性能。

### 研究问题
如何改进3D高斯溅射方法，使其在保持高质量外观渲染的同时，能够准确地提取几何表面信息，尤其是处理透明物体等复杂场景。

### 核心思路/方法
1.  首先通过使用完整真值纹理和几何信息进行训练，论证了默认的3D高斯溅射形式天然不适合同时表示纹理和几何。
2.  提出一种简单解决方案：为每个高斯溅射引入一个额外的“几何不透明度”参数，并可选配一个由透明度引导的优化流程。

### 主要贡献
1.  通过实验论证了标准3D高斯溅射设计存在无法同时表征纹理和几何的内在缺陷。
2.  提出仅增加一个几何不透明度参数的简单改进方案，实现了外观与几何的解耦。
3.  在多种数据集上通过实验证明该改进能提升渲染和几何性能，尤其在包含透明物体的复杂场景中效果显著。

### 局限性
摘要未提供关于该方法在特定场景下的失败案例、计算开销或潜在负影响的足够信息。

### 阅读优先级
高。理由：该工作直接指出当前主流3DGS框架的固有缺陷，并提供了一个极其轻量的解决方案，对神经渲染与几何重建领域具有潜在的重要实用价值，且实验结果覆盖多样场景和透明物体，说服力强。

</details>

<details>
<summary>Abstract</summary>

After the success of 3D Gaussian Splatting (3DGS) for novel view synthesis, many works have explored how to also use it for geometric surface representation. However, extracting accurate geometric information directly from 3DGS remains challenging and can often reduce the appearance rendering quality. In this work, we show that 3DGS in its default form is inheritedly unsuited to represent texture and geometry at the same time, by training with complete ground-truth texture and geometry information. We also propose a simple solution by applying a single additional geometry opacity parameter to each splat, together with an optional transparency-curated optimization pipeline. Our experiments, both with ground-truth and vision foundation model geometric input, show that this change leads to improved rendering and geometry performance on a wide variety of dataset, and especially complex scenes with transparent objects benefit significantly from our method.

</details>

#### 2026-06-03 - ZipSplat: Fewer Gaussians, Better Splats

**Authors:** Alexander Veicht, Sunghwan Hong, Dániel Baráth, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2606.05102) - [pdf](https://arxiv.org/pdf/2606.05102)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ZipSplat: Fewer Gaussians, Better Splats
- 作者：Alexander Veicht, Sunghwan Hong, Dániel Baráth, Marc Pollefeys
- 出版日期：2026-06-03
- 分类：Neural Scene Representations & Rendering
- 链接：[https://arxiv.org/abs/2606.05102](https://arxiv.org/abs/2606.05102)

### 一句话总结
ZipSplat 提出了一种基于 token 的前馈式 3D 高斯泼溅模型，通过聚类将高斯数量与像素网格解耦，在显著减少高斯使用量的同时提升渲染质量，并在多个基准上达到最优性能。

### 研究问题
如何通过前馈式 3D 高斯泼溅方法，在保持或提升渲染质量的前提下，减少高斯数量，从而将表示预算与场景复杂度而非相机分辨率对齐。

### 核心思路/方法
- 设计一个 token 基的前馈模型，使用多视图骨干网络提取稠密视觉 token，并通过 k-means 聚类将这些 token 压缩为紧凑的场景 token 集。
- 利用交叉注意力和自注意力对场景 token 进行细化，随后通过轻量级 MLP 将每个 token 解码为一组 3D 位置不受约束的高斯体。
- 聚类过程在推理时执行，因此单个训练好的模型无需重新训练即可沿质量-效率曲线进行调节。

### 主要贡献
- 提出了 ZipSplat，一种将高斯放置与像素网格解耦的 token 基前馈模型。
- 在无真实姿态或内参的情况下，仅使用约像素对齐方法 1/6 的高斯数量，便在 DL3DV 和 RealEstate10K 上超越最佳无姿态基线，PSNR 分别提升 2.1dB 和 1.2dB。
- 零样本泛化至 Mip-NeRF360 和 ScanNet++ 数据集，且优于所有可比基线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文在减少高斯数量的同时显著提升了渲染质量，在前馈式 3D 高斯泼溅这一当前热门方向上取得了新的最佳结果，且方法设计巧妙（推理时聚类实现质量-效率平衡），对从事神经场景表示与渲染的研究者有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting methods reconstruct a scene from posed or pose-free images in a single forward pass, yet current approaches predict one Gaussian per input pixel, tying the representation budget to camera resolution rather than scene complexity. A flat wall and a richly textured object thus produce equally many Gaussians despite very different geometric needs. We propose ZipSplat, a token-based feed-forward model that decouples Gaussian placement from the pixel grid. A multi-view backbone extracts dense visual tokens, and k-means clustering compresses them into a compact set of scene tokens. Cross- and self-attention refine these tokens, and a lightweight MLP decodes each into a group of Gaussians with unconstrained 3D positions. Because clustering is applied at inference, a single trained model spans the quality-efficiency curve without retraining. ZipSplat operates without ground-truth poses or intrinsics, yet sets a new state of the art on DL3DV and RealEstate10K with ${\sim}6{\times}$ fewer Gaussians than pixel-aligned methods, surpassing the best pose-free baseline by 2.1dB and 1.2dB PSNR, respectively. It further generalizes zero-shot to Mip-NeRF360 and ScanNet++, outperforming all comparable baselines. Our project page is at ${\href{https://veichta.com/zipsplat}{https://veichta.com/zipsplat}}$.

</details>

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
- 链接：摘要：https://arxiv.org/abs/2606.03909；PDF：https://arxiv.org/pdf/2606.03909

### 一句话总结
SparseStreet提出一种针对街景的3D高斯溅射压缩框架，通过可学习的节点剪枝和背景压缩，在几乎不降低质量的前提下实现高达80%的压缩率，并保持动态物体高保真度。

### 研究问题
现有3D高斯溅射在街景重建中需要使用大量高斯元来捕捉细节，导致存储成本高和渲染速度慢，需要一种能够减少冗余、提升效率的方法。

### 核心思路/方法
1. **节点可学习剪枝策略**：系统性地移除贡献度低的高斯元，同时保留视觉关键区域。
2. **背景压缩**：在场景表示稳定后，进一步减少静态区域的冗余。
3. 核心目标是保留动态物体（如车辆、行人）的几何和外观，同时显著降低高斯元总数。

### 主要贡献
- 提出一种专为街景设计的通用压缩框架SparseStreet。
- 在Waymo和nuScenes数据集上实现高达80%的压缩率，且质量退化极小。
- 实现资源高效、高保真的动态场景重建。

### 局限性
摘要未提供足够信息：未讨论方法在极端场景（如大量快速运动物体或复杂光照）下的表现，也未提及与现有方法在计算时间上的对比细节。

### 阅读优先级
**高**。理由：该工作针对街景实时仿真的实际部署需求，提出显著的压缩效率（80%），且已在两个主流数据集验证；如果读者关注自动驾驶、场景重建或实时渲染的资源优化，该论文具有较高参考价值。

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
- 出版日期：2026-06-02T16:46:16Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03877

### 一句话总结
MLP-Splatting提出用多个紧凑的局部MLP作为“神经基元”来替代传统高斯基元或全局辐射场，实现物体级别可分解的、快速的逼真新视图合成。

### 研究问题
现有3D表示方法（如3D高斯泼溅和NeRF）在实现逼真合成的同时难以自然分解场景中的物体，通常需要额外的分割或分组才能进行物体级操作。

### 核心思路/方法
该方法将每个场景基元建模为一个独立的紧凑MLP，该MLP具有局部的空间支持，能够预测辐射度和不透明度。渲染时通过稀疏的体素合成（沿射线与基元的交互）高效进行。基元仅通过RGB监督即可学习，自动对应于局部场景区域（通常为物体或物体部件），从而无需分割掩码即可通过选择少量基元实现交互式物体级编辑。

### 主要贡献
1. 提出MLP-Splatting，使用少量表达力强的神经基元实现场景分解，同时保持逼真的新视图合成。
2. 相比底层高斯基元或单个全局辐射场，神经基元在保持局部性的同时提供更强的表达能力。
3. 通过可选的语义特征蒸馏，支持开放词汇的场景交互和开放集实例分割。
4. 实验表明，与语义3DGS方法相比，内存使用量显著降低（1/15×），渲染速度提升（3×）。

### 局限性
摘要未提供足够信息。未提及该方法在基元数量、训练效率、复杂场景鲁棒性等方面的具体局限。

### 阅读优先级
**高**。理由：该方法在基于神经辐射场的物体级分解与高效渲染方面提出了创新方案，与当前热门的3D高斯泼溅和NeRF范式直接相关，且展示了明显的性能优势（内存和速度）。同时支持开放词汇交互，具有广泛的应用前景。

</details>

<details>
<summary>Abstract</summary>

3D representations are fundamental to scene rendering, understanding, and interaction. Recent approaches, such as 3D Gaussian Splatting and Neural Radiance Fields, achieve impressive photorealistic novel-view synthesis, but lack the ability to easily decompose scene elements into a few primitives, requiring additional segmentation or grouping for object-level manipulation. We present MLP-Splatting, a method that enables scene decomposition via a few expressive light-field primitives while providing photorealistic novel-view synthesis. MLP-Splatting models each primitive as an independent compact MLP with localized spatial support that predicts radiance and opacity. In contrast to low-level Gaussian primitives or a single global radiance field, our neural primitives provide greater expressive capacity while remaining spatially localized. Rendering is performed through efficient sparse volumetric compositing over ray-primitive interactions. Our primitives are supervised using RGB supervision alone, which yields primitives that represent local scene regions often corresponding to objects or object parts, enabling interactive object-level editing without segmentation masks by selecting a handful of primitives. Our method, augmented with optional semantic feature distillation, enables open-vocabulary scene interaction and open-set instant segmentation. Compared to state-of-the-art methods, we achieve substantially lower memory usage (1/15$\times$) and faster rendering (3$\times$), as we show in our experiments compared to semantic 3DGS methods. Project Page: https://shinjeongkim.com/mlp-splatting

</details>

## Embodied / Robotics / AR Applications

### 2026-06

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

#### 2026-06-07 - RGB-S: Image-Aligned Tactile Saliency for Robust Dexterous Manipulation

**Authors:** Shengcheng Luo, Kefei Wu, Xiaoying Zhou, Wanlin Li, Ziyuan Jiao, Chenxi Xiao
**Links:** [abs](https://arxiv.org/abs/2606.08765) - [pdf](https://arxiv.org/pdf/2606.08765)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** camera calibration, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RGB-S: Image-Aligned Tactile Saliency for Robust Dexterous Manipulation
- 作者：Shengcheng Luo, Kefei Wu, Xiaoying Zhou, Wanlin Li, Ziyuan Jiao, Chenxi Xiao
- 出版日期：2026-06-07
- 分类：具身/机器人/AR应用
- 链接：https://arxiv.org/abs/2606.08765

### 一句话总结
本文提出RGB-S框架，通过将触觉传感器位置投影到RGB图像平面并生成力调制高斯显著性图，实现显式视觉-触觉对齐，显著提升机器人在视觉遮挡下的灵巧操作鲁棒性。

### 研究问题
如何有效对齐稀疏、异质的触觉测量与密集视觉表征，以提升机器人在视觉观测不可靠或被遮挡时的灵巧操作能力？

### 核心思路/方法
1. 利用机器人正向运动学和相机标定，将触觉传感器位置直接投影到RGB图像平面上。
2. 渲染力调制高斯显著性图，以建模由运动学和标定误差引起的空间不确定性。
3. 通过零初始化条件架构将这些2D空间锚点注入标准视觉骨干网络，同时保留预训练的视觉表征。

### 主要贡献
1. 提出显式触觉-视觉对齐机制，将物理接触先验嵌入图像域，克服了隐式对齐方法的数据低效和泛化差问题。
2. 引入力调制高斯显著性图，处理了运动学和标定误差带来的空间不确定性。
3. 在六项灵巧操作任务（仿真和真实世界）中，在严重视觉遮挡下，真实世界操作成功率比最强的隐式视觉-触觉基线提升26.7个百分点，验证了方法的空间推理能力和遮挡鲁棒性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该工作针对机器人操作中视觉-触觉融合的核心难题，提出了显式空间对齐的创新方法，并在真实环境中证明了显著性能提升，对具身智能和机器人操作领域具有实用价值。

</details>

<details>
<summary>Abstract</summary>

Effective visuo-tactile integration is critical for robotic dexterous manipulation, especially when visual observations are unreliable or occluded. However, robustly aligning sparse, heterogeneous tactile measurements with dense visual representations remains a fundamental challenge. Most existing approaches require policies to learn cross-modal correspondences implicitly from limited demonstrations, without leveraging geometric priors. As a result, they are often data-inefficient and generalize poorly when visual observations are degraded. To address this limitation, we propose a framework that explicitly grounds physical contacts in the image domain. Using robot forward kinematics and camera calibration, we project tactile sensor locations directly onto the RGB image plane. We then render force-modulated Gaussian saliency maps to model spatial uncertainty arising from kinematic and calibration errors. By integrating these 2D spatial anchors through a zero-initialized conditioning architecture, our method injects physical contact priors into standard visual backbones while preserving pre-trained visual representations. We evaluate our method on six dexterous manipulation tasks in both simulation and the real world under severe visual occlusions. Real-world experiments show that explicit RGB-S grounding in the image domain improves real-world occluded manipulation success rates by $26.7$ percentage points over the strongest implicit visuo-tactile baseline, suggesting its improved spatial reasoning and robustness to occlusion. Project page: touch-as-saliency.github.io

</details>

#### 2026-06-07 - MB-Loc: Multi-planar Bird's-eye-view Localization in outdoor LiDAR scenes

**Authors:** Ayaan Choudhury, Preet Savalia, Anirudh Pydah, Avinash Sharma
**Links:** [abs](https://arxiv.org/abs/2606.08744) - [pdf](https://arxiv.org/pdf/2606.08744)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MB-Loc: Multi-planar Bird's-eye-view Localization in outdoor LiDAR scenes
- 作者：Ayaan Choudhury, Preet Savalia, Anirudh Pydah, Avinash Sharma
- 出版日期：2026-06-07
- 分类：Embodied / Robotics / AR Applications
- 链接：[https://arxiv.org/abs/2606.08744](https://arxiv.org/abs/2606.08744)

### 一句话总结
本文提出MB-Loc，一种轻量级且对视角鲁棒的场景坐标回归（SCR）框架，通过将LiDAR点云投影为多平面鸟瞰图（BEV），利用2D CNN实现高效全局定位，并在NCLT数据集上达到实时推理速度和优于现有方法的精度。

### 研究问题
如何解决传统3D SCR方法在户外LiDAR全局定位中存在的两个瓶颈：处理原始3D几何导致的计算效率低下，以及不同传感器视角下的性能显著下降。

### 核心思路/方法
1. **多平面BEV表示**：将输入LiDAR点云沿Z轴切片，将有符号深度映射到离散的2D平面，形成2.5D多平面鸟瞰图，保留3D几何结构的同时利用标准2D CNN进行计算。
2. **KL正则化潜在瓶颈**：引入KL散度正则化的隐空间瓶颈，显式建模空间不确定性，而不引入随机噪声，以处理户外LiDAR的固有稀疏性。
3. **3D空间数据增强**：在平面投影前应用3D空间增强（如旋转），迫使网络隐式学习视角不变特征，确保旋转鲁棒性。

### 主要贡献
- 提出MB-Loc框架，将3D LiDAR定位转化为2D BEV表示上的高效SCR任务。
- 设计KL正则化瓶颈来建模稀疏点云的不确定性，提升鲁棒性。
- 在NCLT公开数据集上，方法以实时推理速度超越当前最优方法，并在计算效率上显著优于传统3D-SCR架构。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文针对户外LiDAR定位的实际瓶颈（效率和视角鲁棒性）提出了新型轻量级方案，且在公开数据集上达到实时性能并超越SOTA，对自动驾驶和机器人导航等应用场景具有明确价值。方法创新点清晰（多平面BEV+KL瓶颈+数据增强），适合快速了解该方向前沿进展。

</details>

<details>
<summary>Abstract</summary>

Global LiDAR localization is a fundamental task for autonomous navigation systems. Recent methods perform Scene Coordinate Regression (SCR) and achieve superior accuracy over Absolute Pose Regression (APR) solutions by predicting dense 3D world coordinates. However, SCR approaches introduce two major bottlenecks: severe computational inefficiency from processing raw 3D geometries and significant performance degradation under varying sensor viewpoints. To address these limitations, we present MB-Loc, a lightweight and viewpoint-robust SCR framework. Instead of relying on heavy 3D convolutions, we project the input LiDAR scan into a 2.5D Multi-planar Bird's-Eye View (BEV) representation. By slicing the point-cloud along the Z-axis and mapping signed depths into discrete 2D planes, MB-Loc retains essential 3D geometric structures while exploiting the computational tractability of standard 2D CNNs. To handle the inherent sparsity of outdoor LiDAR, we introduce a KL-regularized latent bottleneck that explicitly models spatial uncertainty without injecting stochastic noise. Finally, to ensure rotation robustness, we apply 3D spatial augmentations prior to planar projection, forcing the network to implicitly learn viewpoint-invariant features. We perform extensive experiments on the publicly available NCLT dataset and demonstrate that our proposed method outperforms the current state-of-the-art. Operating at real-time inference speeds, MB-Loc significantly outperforms traditional 3D-SCR architectures in computational efficiency.

</details>

#### 2026-06-07 - Latent Diffusion Policy: Shaping Latent Spaces for Diffusion-Based Robotic Manipulation

**Authors:** Zhexuan Zhou, Yichen Lai, Jinhao Zhang, Huizhe Li, Youmin Gong, Jie Mei
**Links:** [abs](https://arxiv.org/abs/2606.08657) - [pdf](https://arxiv.org/pdf/2606.08657)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Latent Diffusion Policy: Shaping Latent Spaces for Diffusion-Based Robotic Manipulation
- 作者：Zhexuan Zhou, Yichen Lai, Jinhao Zhang, Huizhe Li, Youmin Gong, Jie Mei
- 出版日期：2026-06-07
- 分类：具身/机器人/AR应用（Embodied / Robotics / AR Applications）
- 链接：https://arxiv.org/abs/2606.08657

### 一句话总结
该论文提出一种两阶段扩散策略（Latent Diffusion Policy, LDP），通过在精心塑造的潜空间中执行流匹配，将场景理解与轨迹生成解耦，从而简化多臂协调任务的模仿学习。

### 研究问题
如何降低基于扩散的视觉运动策略在原始动作空间中学习时的复杂性——该空间会混叠场景理解与轨迹生成，导致速度场需同时编码场景信息和生成精确轨迹，尤其限制了多臂时序协调任务的表现。

### 核心思路/方法
1. **两阶段框架**：第一阶段利用基于观测条件的CVAE编码器吸收场景理解，将每帧观测的条件分布压缩到潜空间；第二阶段在预压缩的潜空间中进行流匹配生成，使得流模型无需隐式解析场景依赖结构，速度场更平滑。
2. **时序依赖建模**：采用逐token扩散强制（per-token diffusion forcing）训练，并通过阶梯推理采样（staircase inference sampling）解决训练与推理之间的分布不匹配。
3. **轻量代理指标**：提出重建FID（rFID），仅基于潜空间统计预测下游任务成功率。

### 主要贡献
1. 提出LDP框架，通过解耦场景理解与轨迹生成，简化了复杂协调任务的学习。
2. 在RoboTwin 2.0的协调密集型任务上，LDP大幅优于DP3基线。
3. 在真实双机械臂部署中验证了策略的有效迁移能力。
4. 引入rFID作为无需执行即可评估潜空间质量的轻量代理指标。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对扩散策略在复杂机器人操作任务（尤其是多臂协调）中的关键瓶颈，提出了结构清晰的解耦方法，在标准基准和真实场景上均展示了显著改进，且创新点（潜空间塑造、流匹配简化）具有较强启发性。适合关注具身智能、扩散模型应用及模仿学习的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

Diffusion-based visuomotor policies operating directly in raw action spaces conflate scene comprehension with trajectory generation within a single denoising process. The resulting velocity field must simultaneously encode scene information and generate precise trajectories, increasing learning complexity and limiting performance on tasks demanding precise temporal coordination across multiple arms. To simplify this joint learning problem, we introduce Latent Diffusion Policy (LDP), a two-stage framework performing flow matching in a deliberately shaped latent space. By absorbing scene understanding into an observation-conditioned CVAE encoder, LDP concentrates the conditional distribution of each observation. Consequently, the flow model avoids implicitly resolving scene-dependent structures; instead, it generates within a pre-concentrated distribution featuring a smoother velocity field, simplifying learning from limited demonstrations. Furthermore, to capture temporal dependencies among latent tokens, LDP trains with per-token diffusion forcing and employs staircase inference sampling to resolve the resulting distributional mismatch. We also propose reconstruction FID (rFID) as a lightweight proxy predicting downstream task success solely from latent space statistics. On coordination-intensive tasks from RoboTwin 2.0, LDP outperforms DP3 by a substantial margin and transfers effectively to real-world bimanual deployments.

</details>

#### 2026-06-07 - Real-IKEA: Physical Fidelity is the Prerequisite for Robust Manipulation

**Authors:** Kunqi Xu, Zhenhao Huang, Siyuan Luo, Ziqiu Zeng, Fan Shi
**Links:** [abs](https://arxiv.org/abs/2606.08564) - [pdf](https://arxiv.org/pdf/2606.08564)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-IKEA: Physical Fidelity is the Prerequisite for Robust Manipulation
- 作者：Kunqi Xu, Zhenhao Huang, Siyuan Luo, Ziqiu Zeng, Fan Shi
- 出版日期：2026-06-07T10:41:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2606.08564；PDF：https://arxiv.org/pdf/2606.08564

### 一句话总结
该论文通过构建高物理真实度的数据集与仿真框架强调：真实接触和动态物理特性是提升机器人操控策略鲁棒性的前提。

### 研究问题
机器人操控策略在从简化仿真环境迁移到真实阻力场景时，因物理模型与真实环境之间存在“物理差距”而失效，如何通过提升仿真中的物理保真度（包括接触几何精确性和动力学真实感）来增强操控策略的鲁棒性。

### 核心思路/方法
1. **数据集与仿真框架构建**：基于 83 个真实宜家手柄/旋钮，经过六步精细物理流程处理，得到 1,079 种可调关联配置资产。
2. **接触几何精度度量**：提出双向表面偏差指标来量化碰撞网格的精确性。
3. **动力学真实感建模**：建立可调节阻尼和摩擦力的阻力校准配置。
4. **强化学习验证**：使用高保真资产训练强化学习策略，自动发现更依赖机械杠杆效应（而非摩擦拉动）的稳健“钩取”和“撬动”策略。

### 主要贡献
1. 提出高度物理保真的数据集 Real-IKEA（1,079 种关联配置），强调物理真实感是鲁棒操控的前提。
2. 引入双向表面偏差指标，用于量化接触网格的几何精度。
3. 证实高保真物理资产能够促使强化学习学到更稳健的操控策略，从而弥合仿真与现实间的物理差距。

### 局限性
摘要未提供足够信息。具体局限性包括但不限于：数据集的资产类别局限于宜家手柄和旋钮，未见结论推广至其他铰接物体的评估；摘要未提及感知模块或真实机器人部署验证；未报告策略在大规模变体上的泛化误差。

### 阅读优先级
**高**。理由：该工作直接针对仿真-现实物理迁移这一核心难点，提出可量化且分步的物理保真构建流程并经过强化学习验证，对从事铰接物体操控、仿真到现实迁移、以及动力学建模的研究人员有直接参考价值。论文发表日期较新（2026年6月），方法设计紧凑。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation robustness often founders on the physics gap between simplified simulations and the resistance-laden real world. In this work, we emphasize that physical realism in articulated interaction is an important ingredient for robust policy learning. We present Real-IKEA, a dataset and simulation framework designed with physical accuracy as a first-class goal. Real-IKEA provides 1,079 articulated asset configurations, derived from 83 authentic IKEA handles and knobs processed through a meticulous six-step physical workflow. For contact-geometry accuracy, we introduce a bidirectional surface-deviation metric to quantify collision meshes. For dynamics realism, we establish resistance-calibrated configurations that vary damping and friction. Crucially, we demonstrate through a Reinforcement Learning (RL) policy that high-fidelity assets enable the discovery of robust "hooking" and "levering" strategies that prioritize mechanical advantage over fragile friction-pulling. Together, these results position Real-IKEA as a critical benchmark for developing manipulation policies capable of human-level robustness in articulated object tasks.

</details>

#### 2026-06-07 - GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation

**Authors:** Yuan Zhang, Shiqi Zhang, Yedong Shen, Shuai Dong, Jiajun Deng, Xin Zhang, Yuxuan Gao, Jiajia Wu, Xin Nie, Zhiyuan Cheng, Jianmin Ji, Yanyong Zhang, Xingyi Zhang, Jia Pan
**Links:** [abs](https://arxiv.org/abs/2606.08530) - [pdf](https://arxiv.org/pdf/2606.08530)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GEAR-VLA: Learning Geometry-Aware Action Representations for Generalizable Robotic Manipulation  
- 作者：Yuan Zhang, Shiqi Zhang, Yedong Shen, Shuai Dong, Jiajun Deng, Xin Zhang, Yuxuan Gao, Jiajia Wu, Xin Nie, Zhiyuan Cheng, Jianmin Ji, Yanyong Zhang, Xingyi Zhang, Jia Pan  
- 出版日期：2026-06-07  
- 分类：Embodied / Robotics / AR Applications  
- 链接：摘要 https://arxiv.org/abs/2606.08530 | PDF https://arxiv.org/pdf/2606.08530  

### 一句话总结  
GEAR-VLA 是一个面向通用机器人操作的视觉-语言-动作框架，通过粗到细的动作学习、语义对齐的3D特征集成和具身标准化，学习统一的几何感知动作表征，以提升对未见物体、背景变化和不同机器人形态的泛化能力。

### 研究问题  
现有视觉-语言-动作（VLA）模型在基准测试中表现良好，但在真实世界部署中面对未见物体、背景变化和不同机器人形态时泛化能力不足。作者认为根本原因是缺乏统一的几何感知操作表征，导致低层轨迹监督、3D特征错位和具身差异问题。

### 核心思路/方法  
1. **粗到细动作学习**：多源具身预训练使视觉语言模型获得具身推理和离散动作理解能力，随后通过潜在动作标记将动作语义连接到梯度解耦的DiT连续动作专家模块。  
2. **语义对齐的3D集成**：在冻结原始视觉-语言模型对齐的视觉通路的同时，训练一个可学习的3D空间主干网络，使其表征与VLA表征语义对齐。  
3. **具身标准化**：通过具身感知状态和具身不变动作将机器人差异限制在低层接口层面，从而在不同机器人之间共享表征。  

### 主要贡献  
- 提出GEAR-VLA框架，学习统一的几何感知动作表征，提升机器人操作的泛化性。  
- 在多个仿真和真实基准上取得领先结果：LIBERO、零样本LIBERO-Plus和RoboTwin 2.0上达到最先进性能；AgileX成功率85.9%，未预训练的LDT-01具身上达81.0%；在包含212个未见物体的6,360次通用抓取基准上成功率达90.1%。  
- 代码和模型将开源（摘要提供链接但未在文中明确释放日期）。  

### 局限性  
摘要未提供足够信息，未提及任何局限性或失败案例。

### 阅读优先级  
**高**  
理由：该论文针对机器人操作中的核心泛化问题提出新框架，在多个具身任务上取得显著性能提升（如零样本泛化、不同机器人形态迁移），且方法包含几何感知、粗到细学习等创新点，对具身智能和VLA领域研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve strong benchmark performance but still struggle in real-world deployment with unseen objects, background shifts, and different robot embodiments. We argue that this stems from the lack of a unified geometry-aware manipulation representation, leaving existing VLAs vulnerable to low-level trajectory supervision, misaligned 3D features, and embodiment differences. To address this, we propose GEAR-VLA, a VLA framework for learning unified geometry-aware action representations for generalizable robotic manipulation. GEAR-VLA adopts coarse-to-fine action learning, where multi-source embodied pretraining equips the VLM with embodied reasoning and discrete action understanding before latent action tokens connect action semantics to a gradient-decoupled DiT continuous action expert. It further performs semantic-aligned 3D integration by aligning a trainable 3D spatial backbone with the VLA representation while freezing the original VLM-aligned visual pathway. To share this representation across robots, GEAR-VLA uses embodiment canonicalization, where embodiment-aware states and embodiment-invariant actions confine robot differences to the low-level interface. Extensive simulation and real-world experiments demonstrate strong generalization: GEAR-VLA achieves state-of-the-art performance on LIBERO, zero-shot LIBERO-Plus, and RoboTwin 2.0, reaches 85.9% success on AgileX and 81.0% on the pretraining-unseen LDT-01 embodiment, and obtains 90.1% success on a 6,360-trial universal grasping benchmark with 212 unseen objects. Code and models will be released at https://github.com/babynabeauty/GEAR-VLA.

</details>

#### 2026-06-04 - Meridian: Metric-Semantic Primitive Matching for Cross-View Geo-Localization Beyond Urban Environments

**Authors:** Mason Peterson, Qingyuan Li, Yixuan Jia, Fernando Cladera, Carlos Nieto-Granda, Camillo Jose Taylor, Jonathan P. How
**Links:** [abs](https://arxiv.org/abs/2606.06312) - [pdf](https://arxiv.org/pdf/2606.06312)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Meridian: Metric-Semantic Primitive Matching for Cross-View Geo-Localization Beyond Urban Environments
- 作者：Mason Peterson, Qingyuan Li, Yixuan Jia, Fernando Cladera, Carlos Nieto-Granda, Camillo Jose Taylor, Jonathan P. How
- 出版日期：2026-06-04
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2606.06312) | [PDF](https://arxiv.org/pdf/2606.06312)

### 一句话总结
Meridian是一种无需针对特定区域训练或微调、通过匹配度量-语义基元实现跨视角全局定位的方法，在多样化环境（包括无GNSS的野外区域）中平均轨迹误差为2.4米。

### 研究问题
如何在GNSS受限且缺乏结构化特征的户外自然环境中，实现跨视角（航空图像与地面机器人RGB-D数据）的精确且泛化的全局定位？

### 核心思路/方法
- 方法链：从航空图像和地面机器人RGB-D数据中提取高层度量-语义基元（如几何形状与语义标签的组合）。
- 匹配机制：设计新型一致性度量，用于估计机器人子图位置的分布。
- 优化步骤：在鲁棒位姿图优化中剔除异常假设，从而获得准确的机器人轨迹估计。
- 关键特点：无需在特定区域数据上进行训练或算法微调，直接泛化到不同环境。

### 主要贡献
1. 提出了首个无需区域特定训练、能在多样化非城市环境（含野外地形）中实现跨视角全局定位的方法。
2. 设计了一致性度量来评估子图位姿分布，并集成到鲁棒位姿图优化中以剔除错误匹配。
3. 在自动驾驶数据集、公园校园区域和野外营地三种环境、总计19公里地面路径上，平均优化轨迹误差仅2.4米，验证了泛化性与准确性。

### 局限性
摘要未提供足够信息。具体包括：未提及方法在极端光照、动态场景或高遮挡环境下的表现；未说明计算效率或实时性；未讨论对基元提取精度的依赖性以及失败案例。

### 阅读优先级
**高**。理由：该方法直接解决了户外非结构化环境下的跨视图定位难题，且无需训练即可泛化，对于机器人自动化、野外探测等应用具有显著实用价值。实验覆盖多种环境且误差指标明确，具有较高的参考意义。

</details>

<details>
<summary>Abstract</summary>

Successful robot automation requires accurate global localization to support repeatability, task planning, goal specification, and safe operation. However, reliable localization in GNSS-denied environments remains an open problem. Overhead aerial imagery offers a promising solution, but existing approaches primarily target structured urban environments and have been rarely demonstrated in unstructured natural terrain. Limitations of the state-of-the-art include a reliance on models trained for specific environments, as well as difficulty handling repetitive geometries and featureless landscapes commonly found in natural outdoor areas. To overcome these challenges, we present Meridian, a method for matching high-level metric-semantic primitives across aerial images and ground robot RGB-D camera data that achieves accurate global localization and generalizes well across diverse environments, all without any training or algorithmic fine-tuning on area-specific data. We formulate novel consistency metrics to estimate a distribution over robot submap poses and to reject outlier hypotheses in a robust pose graph optimization step for accurate robot trajectory estimation. We demonstrate that our algorithm can localize a ground robot across a wide variety of environments, including an autonomous driving dataset, a park and campus area, and a wilderness camp, with an average optimized trajectory error of 2.4 m over 19 km of ground traversal.

</details>

#### 2026-06-04 - RadiusFPS: Efficient Farthest Point Sampling on CPUs and GPUs via Spherical Voxel Pruning

**Authors:** Ziyang Yu, Xiang Li, Qiong Chang, Jun Miyazaki
**Links:** [abs](https://arxiv.org/abs/2606.06255) - [pdf](https://arxiv.org/pdf/2606.06255)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** simultaneous localization and mapping, SLAM, autonomous driving, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RadiusFPS: Efficient Farthest Point Sampling on CPUs and GPUs via Spherical Voxel Pruning
- 作者：Ziyang Yu, Xiang Li, Qiong Chang, Jun Miyazaki
- 出版日期：2026-06-04
- 分类：Embodied / Robotics / AR Applications（主要），3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要: https://arxiv.org/abs/2606.06255, PDF: https://arxiv.org/pdf/2606.06255

### 一句话总结
本文提出RadiusFPS，一种基于球体体素剪枝的Farthest Point Sampling加速框架，在CPU和GPU上大幅降低计算延迟和内存占用，同时保持标准FPS的采样质量，适用于资源受限的机器人视觉系统。

### 研究问题
经典Farthest Point Sampling（FPS）时间复杂度高，难以匹配现代3D传感器每秒百万点的高速率，成为机器人感知流水线（如自动驾驶、SLAM）中的延迟瓶颈，且与实时性和有限板上计算资源冲突。

### 核心思路/方法
1. **球体体素剪枝（Spherical Voxel Pruning）**：用球体体素索引点云，推导保守几何边界，在每次迭代中剪枝冗余的距离计算。
2. **坐标维度点跳跃测试（Coordinate-wise Point-Skip Test）**：补充剪枝策略，移除残余的更新操作，进一步减少计算。
3. **RadiusFPS-G（GPU实现）**：基于warp级别的GPU实现，将体素选择、剪枝和距离更新融合为内存合并的内核，消除昂贵的全局内存往返。

### 主要贡献
- 提出RadiusFPS框架，在相同初始化和断链策略下保留标准FPS更新规则，同时显著加速。
- 在室内（S3DIS, ScanNet）和室外LiDAR（SemanticKITTI）基准上，RadiusFPS-G相比GPU的FPS实现获得高达2.5倍加速，且内存使用约为QuickFPS的一半，分割精度相当。
- 与基于学习的FastPoint采样器结合时，实现了所有评估配置中最快的端到端推理。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接解决机器人感知中实时性关键瓶颈FPS的加速问题，提供了明确的加速比（2.5倍）和内存节省优势，且已在主流室内外数据集上验证。对于从事自动驾驶、SLAM或实时点云处理的科研或工程人员，具有直接应用价值。

</details>

<details>
<summary>Abstract</summary>

Point clouds are a primary sensory representation for robotic perception, underpinning LiDAR-based autonomous driving, simultaneous localization and mapping (SLAM), and navigation. Within these pipelines, Farthest Point Sampling (FPS) is the most well-known downsampling operator, as its uniform coverage preserves the geometric structure on which downstream perception relies. However, the large time complexity of classical FPS scales poorly with the million-point-per-second rates of modern 3D sensors, making it a dominant latency bottleneck that conflicts with the real-time and limited onboard compute budgets of robotic systems. Therefore, we propose RadiusFPS, an FPS acceleration framework based on spherical voxel pruning that preserves the standard FPS update rule under the same initialization and tie-breaking policy. By indexing the point cloud with spherical voxels, RadiusFPS derives a conservative geometric bound that prunes redundant distance computations in each iteration, complemented by a coordinate-wise point-skip test that removes residual updates. We further introduce RadiusFPS-G, a warp-level GPU implementation that fuses voxel selection, pruning, and distance update into memory-coalesced kernels, eliminating costly global-memory round-trips. On indoor (S3DIS, ScanNet) and outdoor LiDAR (SemanticKITTI) benchmarks, RadiusFPS-G attains up to 2.5x speedup over GPU-based FPS and matches or exceeds QuickFPS among the evaluated methods while using roughly half its GPU memory, with comparable segmentation accuracy. When coupled with the learning-based FastPoint sampler, the resulting pipeline achieves the fastest End-to-End inference among all evaluated configurations. These properties make high-quality FPS-style sampling practical for latency- and memory-constrained robotic vision.

</details>

#### 2026-06-04 - CLEAR: Cognition and Latent Evaluation for Adaptive Routing in End-to-End Autonomous Driving

**Authors:** Yining Xing, Zehong Ke, Zhiyuan Liu, Yanbo Jiang, Wenhao Yu, Jianqiang Wang
**Links:** [abs](https://arxiv.org/abs/2606.06219) - [pdf](https://arxiv.org/pdf/2606.06219)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CLEAR: Cognition and Latent Evaluation for Adaptive Routing in End-to-End Autonomous Driving
- 作者：Yining Xing, Zehong Ke, Zhiyuan Liu, Yanbo Jiang, Wenhao Yu, Jianqiang Wang
- 出版日期：2026-06-04
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.06219

### 一句话总结
提出CLEAR框架，通过在VAE潜空间中进行单步条件漂移替代扩散模型的多步去噪，并结合大语言模型驱动的自适应调度与交叉注意力评优，实现高效且多样化的端到端自动驾驶规划。

### 研究问题
端到端自动驾驶模型在生成多模态驾驶行为时，扩散模型的高延迟无法满足安全关键场景的实时推理约束。

### 核心思路/方法
1. 使用Drive-JEPA作为视觉编码器，在VAE潜空间中采用单步条件漂移（引入调节系数平衡多样性与专家精度）替代扩散模型的多步去噪过程。
2. 在驾驶问答对（QA pairs）上微调Qwen 3.5-0.8B模型，提取场景感知的隐藏状态。
3. 利用上述隐藏状态驱动两个模块：
   - 自适应调度器（Adaptive Scheduler）：从离散预定义方案中选择调节系数α和样本数量N。
   - 交叉注意力评分器（cross-attention scorer）：从候选轨迹中挑选最优轨迹。

### 主要贡献
- 提出一种超快生成规划与深度语义推理结合的框架CLEAR，无需密集几何标注或迭代采样即可实现高保真多模态规划。
- 在NAVSIM v1基准上达到93.7 PDMS（当前最佳性能）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该工作针对端到端自动驾驶中扩散模型延迟高的核心痛点，提出了一种新颖的潜空间单步生成方案，并结合大模型进行自适应路由，在标准基准上取得了领先结果。对于关注自动驾驶实时规划、生成式模型效率优化以及大模型在具身智能中应用的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

End-to-end autonomous driving models often struggle to balance multi-modal maneuver generation with real-time inference constraints. While diffusion models successfully capture diverse driving behaviors, their iterative denoising process incurs unacceptable latency for safety-critical deployment. To address this, we propose CLEAR (Cognition and Latent Evaluation for Adaptive Routing), a framework that combines ultra-fast generative planning with deep semantic reasoning. CLEAR employs Drive-JEPA as the visual encoder and replaces the multi-step denoising chain with a single-step conditional drift in a VAE latent space, introducing a conditioning coefficient to balance diversity and expert precision. Meanwhile, we fully fine-tune Qwen~3.5~0.8B on driving QA pairs to extract scene-aware hidden states. These states guide both an Adaptive Scheduler, which selects the conditioning coefficient $α$ and sample count $N$ from a discrete set of predefined schemes, and a cross-attention scorer that selects the optimal trajectory from candidates. On the NAVSIM v1 benchmark, CLEAR achieves a state-of-the-art PDMS of 93.7. Our results demonstrate that high-fidelity, multi-modal planning can be executed efficiently without dense geometric annotations or iterative sampling.

</details>

#### 2026-06-04 - AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding

**Authors:** Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
**Links:** [abs](https://arxiv.org/abs/2606.06155) - [pdf](https://arxiv.org/pdf/2606.06155)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reasoning, manipulation, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding
- 作者：Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
- 出版日期：2026-06-04T13:28:51Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.06155

### 一句话总结
该文提出AffordanceVLA框架，通过引入结构化可供性预测作为中间表示，弥合视觉-语言模型与机器人操控策略之间的语义空间差异，提升指令跟随操控的精确性。

### 研究问题
如何解决视觉-语言模型（VLM）语义空间与具身控制策略之间的结构不匹配问题，从而学习更精确的感知-动作映射。

### 核心思路/方法
- 引入任务导向的**结构化可供性预测**（affordance forecasting）作为中间表示，建立精确且鲁棒的感知-动作映射。
- 通过三个互补组件渐进建模操控先验：
  1. **Which2Act**：通过视觉潜在预测实现以物体为中心的定位，抑制干扰；
  2. **Where2Act**：通过可供性图估计进行2D交互定位；
  3. **How2Act**：通过3D几何推理指导操控策略。
- 将上述模块集成到**混合Transformer（MoT）**架构中，使用专门专家模块，并采用**三阶段训练策略**以及渐进式数据课程。
- 开发了一个**自动数据增强流水线**，以缓解机器人数据集中密集可供性标签稀缺的问题。

### 主要贡献
- 提出统一框架AffordanceVLA，通过结构化可供性预测作为中间表示，桥接视觉、语言与动作。
- 设计了三个互补模块（Which2Act、Where2Act、How2Act），分别负责物体定位、交互点定位及3D几何推理。
- 采用MoT架构与三阶段训练策略，以及自动数据增强流水线，提升模型在模拟与真实环境的多样操作场景下的性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接针对视觉-语言-动作（VLA）模型在机器人操控中的关键瓶颈（感知-动作映射不精确）提出结构化解决方案，方法设计系统（三组件+MoT+三阶段训练），且经过仿真与真实实验验证，对具身智能领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models leverage the rich world knowledge of pretrained vision-language models (VLMs) to enable instruction-following robotic manipulation. However, the structural mismatch between VLM semantic spaces and embodied control policies often hinders the learning of precise perception--action mappings. To address this challenge, we propose \textbf{AffordanceVLA}, a unified framework that introduces structured affordance forecasting as a task-oriented intermediate representation to establish a more precise and robust perception--action mapping. Specifically, we progressively model manipulation priors through three complementary components: 1) \textbf{Which2Act} for object-centric grounding via visual latent prediction to suppress distractions; 2) \textbf{Where2Act} for 2D interaction localization via affordance map estimation; and 3) \textbf{How2Act} for 3D geometric reasoning to guide manipulation policies. These affordance cues provide spatially grounded, semantically conditioned, and action-coupled intermediate representations, thereby naturally bridging vision, language and action. We integrate these modules into a Mixture-of-Transformer (MoT) architecture with specialized experts and train the model using a three-stage training strategy with a progressive data curriculum. To overcome the scarcity of dense affordance labels in robotic datasets, we also develop a robust automated data augmentation pipeline. Extensive experiments on simulation and real-world demonstrate that AffordanceVLA achieves strong performance across diverse manipulation scenarios.

</details>

#### 2026-06-04 - Towards Realistic 3D Sonar Simulation

**Authors:** Youssef Attia, Davide Costa, Francesco Wanderlingh, Filippo Campagnaro, Enrico Simetti
**Links:** [abs](https://arxiv.org/abs/2606.06130) - [pdf](https://arxiv.org/pdf/2606.06130)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, rendering, robotics, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Realistic 3D Sonar Simulation
- 作者：Youssef Attia, Davide Costa, Francesco Wanderlingh, Filippo Campagnaro, Enrico Simetti
- 出版日期：2026-06-04T13:16:32Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.06130

### 一句话总结
本文提出一种结合GPU加速图形引擎与物理声学传播原理的模块化架构，用于实现更真实的三维声纳仿真，并在NVIDIA Isaac Sim环境中集成到水下仿真框架中。

### 研究问题
如何提升三维声纳仿真的物理真实性，使其超越当前基于几何渲染的简化模拟，从而更好地支持水下机器人感知与自主导航算法开发。

### 核心思路/方法
- 设计模块化架构，将GPU加速图形引擎与基于物理的声学传播原理（如折射、多路径干扰、相位依赖信号形成）相结合。
- 在NVIDIA Isaac Sim环境中实现一个体素化的三维声纳模型，以Water Linked 3D-15传感器为原型。
- 通过硬件在环配置验证系统：在NVIDIA Jetson Orin Nano上运行修改后的FastLIO2 SLAM流水线，融合合成三维声纳、DVL、IMU和压力数据。
- 将仿真输出与港口板桩检测的真实世界数据进行定性比较，分析仿真到现实的差距。

### 主要贡献
- 提出一种模块化三维声纳仿真架构，克服了现有基于几何渲染方法的声学简化不足。
- 在NVIDIA Isaac Sim中实现了体素化三维声纳模型，并将其融入完整水下仿真框架。
- 通过硬件在环SLAM实验和真实数据对比，定性表征了仿真与现实之间的差距。

### 局限性
摘要未提供具体局限性信息，仅指出存在“仿真到现实的差距”，但未量化其影响或分析具体来源。摘要未提供实验的定量结果、对比基线或误差分析细节。

### 阅读优先级
中
理由：该方法针对水下声纳仿真中的物理真实性问题提出了具体技术路径，并提供了定性验证，但缺乏实验定量指标和与现有方法的系统比较（摘要未提供更多细节），适合对水下感知或仿真框架有专业兴趣的读者参考。

</details>

<details>
<summary>Abstract</summary>

As underwater robotics research increasingly addresses complex 3D perception and autonomous navigation, the fidelity of sonar simulation has become a key factor in algorithm development. Current simulation frameworks typically rely on geometry-driven rendering, approximating 3D sonar as an underwater equivalent to LiDAR, which fails to account for fundamental acoustic phenomena such as refraction, multi-path interference, and phase-dependent signal formation. This paper proposes a modular architecture for realistic 3D sonar simulation that integrates GPU-accelerated graphics engines with physically grounded acoustic propagation principles. We implement a volumetric 3D sonar model within the NVIDIA Isaac Sim environment, modeled after the Water Linked 3D-15 sensor, and integrate it into a comprehensive underwater simulation framework. The system is validated through a hardware-in-the-loop configuration, where a modified FastLIO2 SLAM pipeline, executed on an NVIDIA Jetson Orin Nano, performs sensor fusion using synthetic 3D sonar, DVL, IMU, and pressure data. Finally, a qualitative comparison between simulated outputs and real-world data from harbor sheet-pile inspections is provided, characterizing the remaining sim-to-real gap and establishing a roadmap toward fully acoustics-driven volumetric sensing.

</details>

#### 2026-06-03 - Impostor: An Agent-Curated Benchmark for Realistic AIGC Manipulation Localization

**Authors:** Zhenliang Li, Yutao Hu, Qixiong Wang, Wenpeng Du, Hongxiang Jiang, Jiasong Wu, Xiaolong Jiang, Jungong Han
**Links:** [abs](https://arxiv.org/abs/2606.04545) - [pdf](https://arxiv.org/pdf/2606.04545)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Impostor: An Agent-Curated Benchmark for Realistic AIGC Manipulation Localization
- 作者：Zhenliang Li, Yutao Hu, Qixiong Wang, Wenpeng Du, Hongxiang Jiang, Jiasong Wu, Xiaolong Jiang, Jungong Han
- 出版日期：2026-06-03
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.04545

### 一句话总结
该论文提出了一个名为Impostor的高质量AI编辑图像篡改定位基准数据集（含10万张篡改图像），并设计了CraftAgent自动构建框架和PANet检测网络，实验表明该基准对现有方法构成显著挑战，且PANet性能优越。

### 研究问题
现有图像篡改检测与定位基准在视觉真实性、篡改多样性和生成器覆盖范围上存在局限，难以反映最新图像篡改趋势，亟需更全面、真实的基准来评估和推动AIGC篡改定位方法。

### 核心思路/方法
1. **数据集构建**：采用CraftAgent——一种闭环智能体框架，集成了场景感知、编辑规划、篡改执行、质量验证和迭代反思，自动生成多样且视觉真实的篡改图像。
2. **数据集特性**：包含由7个近期AIGC模型生成的图像，涵盖3种篡改类型，并包含多个篡改区域。
3. **检测方法**：提出PhaseAware-Net（PANet），一种语义-取证框架，引入局部相位建模和语义-取证一致性学习，以更好地定位语义合理但取证异常的被篡改区域。

### 主要贡献
1. 发布了Impostor基准数据集：包含10万张高真实度AI编辑图像，具有更丰富的篡改多样性、更广的生成器覆盖和多个篡改区域。
2. 提出了CraftAgent自动构建框架：通过闭环智能体流程实现高效、可控的数据生成。
3. 设计了PANet检测网络：通过局部位相建模和语义-取证一致性学习提升篡改定位精度。
4. 实验表明：Impostor对现有大型视觉语言模型和专用IMDL方法构成显著挑战，PANet在Impostor和多个公开基准上取得优越性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：论文提出了一个大规模、高质量的篡改定位基准数据集，并同时给出了先进检测方法，对图像取证和AIGC安全领域有重要参考价值，实验部分也验证了其挑战性和有效性。

</details>

<details>
<summary>Abstract</summary>

Recent advances in generative image editing have improved the realism and controllability of localized image manipulation, raising new challenges for image manipulation detection and localization (IMDL). However, existing IMDL benchmarks still have limitations in visual realism, manipulation diversity, and generator coverage, making it difficult to reflect recent trends in image manipulation. To address these limitations, we introduce Impostor, a high-quality AI-edited image manipulation localization dataset containing 100K manipulated images. Impostor is constructed by CraftAgent, a closed-loop agent framework that integrates scene perception, editing planning, manipulation execution, quality validation, and iterative reflection to automatically generate diverse and visually realistic manipulated images. Moreover, Impostor contains images generated by seven recent AIGC models across three manipulation types and includes multiple manipulated regions, providing a more comprehensive benchmark for AIGC-based IMDL. Furthermore, we propose PhaseAware-Net (PANet), a semantic-forensic framework that introduces local phase modeling and semantic-forensic consistency learning to better localize semantically plausible yet forensically disrupted manipulated regions. Extensive experiments show that Impostor poses significant challenges to existing large vision-language models (LVLMs) and specialized IMDL methods, while PANet achieves superior performance on Impostor and multiple public benchmarks.

</details>

#### 2026-06-03 - MAD: Mapping-Aware World Models for Agile Quadrotor Flight

**Authors:** Xinhong Zhang, Runqing Wang, Yunfan Ren, Ding Yu, Boyu Zhou, Jian Sun, Fang Deng, Jie Chen, Gang Wang
**Links:** [abs](https://arxiv.org/abs/2606.04534) - [pdf](https://arxiv.org/pdf/2606.04534)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MAD: 面向敏捷四旋翼飞行的地图感知世界模型
- 作者：Xinhong Zhang, Runqing Wang, Yunfan Ren, Ding Yu, Boyu Zhou, Jian Sun, Fang Deng, Jie Chen, Gang Wang
- 出版日期：2026-06-03
- 分类：具身智能/机器人/AR应用
- 链接：摘要URL: https://arxiv.org/abs/2606.04534

### 一句话总结
本文提出一种名为MAD的地图感知世界模型，通过学习重构机器人中心占用与可见性网格图，使四旋翼无人机能在视觉导航与竞速任务中实现更高效、安全的自主飞行。

### 研究问题
如何在杂乱场景下利用有限的感知（深度图像）和低延迟要求，赋予四旋翼无人机对已观测区域、邻近占用空间进行记忆与推理的能力，以提升敏捷飞行的成功率与速度。

### 核心思路/方法
1. **模型设计**：提出Mapping-Aware Dreamer（MAD），一种几何感知的世界模型。其核心是学习循环潜在动力学，该动力学不以原始图像重建为自监督目标，而是重构机器人中心的占用网格图、可见性网格图以及本体感受状态。
2. **训练机制**：在DiffAero模拟器中利用GPU并行的地图构建模块提供高吞吐量的占用与可见性监督信号。
3. **策略学习**：将学习到的表示用于三种策略学习模式：基于想象力的MAD-Dreamer，以及基于PPO和SHAC的特征提取器变体。

### 主要贡献
- 提出了MAD，一种将地图感知直接融入世界模型潜在表示的设计，迫使潜在状态编码与避障直接相关的局部几何、可见性历史与自运动。
- 在视觉导航与竞速任务中，基于MAD的智能体相比纯视觉基线实现了更高的成功率、更快的飞行速度以及更好的跨任务迁移能力。
- 从深度观测中产生了可解释的地图预测和准确的自运动估计。
- 在实际四旋翼上部署了学习策略（使用Intel RealSense D435i），在模拟中达到9.66 m/s，在真实森林实验中达到5.05 m/s，证明了在有限感知下进行安全的室内外飞行。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作将地图感知与世界模型学习相结合，在四旋翼敏捷飞行任务上取得了显著的性能提升（包括在真实世界中的实验），同时提出了可解释的中间表示（占用与可见性网格）。对于从事具身智能、机器人导航或端到端学习方向的读者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Agile quadrotor flight in cluttered scenes requires more than a reactive mapping from a depth image to a control command: the vehicle must remember which regions have been observed, infer nearby occupied space, and act under partial visibility and tight latency. In this paper, we present Mapping-Aware Dreamer (MAD), a geometry-aware world model for vision-based quadrotor flight. Instead of using raw-image reconstruction as the main self-supervised objective, MAD learns recurrent latent dynamics that reconstruct robocentric occupancy and visibility grid maps together with proprioceptive states. This design forces the latent state to encode local geometry, visibility history, and ego-motion in a form that is directly relevant to collision avoidance. MAD is trained in DiffAero using a GPU-parallel map-construction module that provides high-throughput supervision for occupancy and visibility. The learned representation is used in three policy-learning modes: imagination-based MAD-Dreamer and feature-extractor variants based on PPO and SHAC. Across visual navigation and racing tasks, MAD-based agents achieve higher success rates, faster flight, and better cross-task transfer than corresponding vision-only baselines. The model also produces interpretable map predictions and accurate ego-motion estimates from depth observations. We further deploy the learned policy on a physical quadrotor with an Intel RealSense D435i and demonstrate safe indoor and outdoor flight under limited sensing, reaching 9.66 m/s in simulation and 5.05 m/s in real-world forest experiments. These results show that mapping-aware world models provide a practical middle ground between modular aerial navigation and end-to-end learning.

</details>

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
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications
- 链接：abstract: https://arxiv.org/abs/2606.03890, pdf: https://arxiv.org/pdf/2606.03890

### 一句话总结
本文提出一个名为 OVO-S-Bench 的层次化基准，用于评估多模态大语言模型在连续自我中心视频流中实时推理空间结构的能力。

### 研究问题
现有基准要么在完整视频上离线评估，要么针对事件而非空间结构；缺乏专为流式空间智能设计的测试。本文旨在填补这一空白，系统评估多模态大语言模型在仅看到查询时间点之前视频前缀的条件下，对空间布局和关系的实时推理能力。

### 核心思路/方法
- 构建包含 1,680 道题目、348 个源视频的完全人工标注基准。标注过程涉及 12 名训练有素的标注员，每人同时担任盲审交叉审阅者，总耗时约 804 人小时进行多轮质量保证。
- 每个问题附带一个查询时间戳和一个证据区间，评估时模型只能看到查询点之前的视频前缀。
- 问题分为四个抽象层次：瞬时自我中心感知、时空上下文追踪、空间模拟与推理，以及异中心映射。
- 在 38 个专有和开源多模态大语言模型上进行评估，并与人类专家表现对比。

### 主要贡献
- 引入 OVO-S-Bench，一个专注于流式空间智能的完全人工标注基准，包含多层次问题。
- 评估结果表明，最佳模型 Gemini-3.1-Pro 得分为 59.2，与人类专家的 86.6 分仍有 27 分的差距，其中异中心映射是主要瓶颈。
- 发现流式与空间微调的多模态大语言模型表现甚至不如其基础模型。
- 发现链式思维推理在缺乏流式空间依据时会放大空间错误。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文直面多模态智能体在机器人、增强现实和自动驾驶中的核心挑战——流式空间推理，并构建了首个专用层次化基准，揭示了现有模型与人类专家的显著差距，对相关领域的研究和实践具有重要指导意义。

</details>

<details>
<summary>Abstract</summary>

Multimodal agents in robotics, AR, and autonomous driving must reason about places and layouts from continuous egocentric streams, often using evidence outside the current view. Existing benchmarks either evaluate offline over full videos or target events rather than spatial structure. We introduce OVO-S-Bench, a fully human-annotated benchmark for streaming spatial intelligence, comprising 1,680 questions over 348 source videos. Annotation involves 12 trained annotators, each also serving as a blind cross-reviewer, across roughly 804 person-hours of multi-round quality assurance. Each question carries a query timestamp and an evidence interval, and at evaluation, the model sees only the prefix preceding the query. Questions span four levels of increasing abstraction: instantaneous egocentric perception, spatiotemporal context tracking, spatial simulation and reasoning, and allocentric mapping. Across 38 proprietary and open-source MLLMs, Gemini-3.1-Pro trails human experts by 27 points, 59.2 vs. 86.6, with allocentric mapping as the dominant bottleneck. Notably, streaming and spatially fine-tuned MLLMs underperform their own backbones. We further find that chain-of-thought reasoning amplifies spatial errors when ungrounded in the stream. By exposing these limitations, OVO-S-Bench establishes a demanding testbed for next-generation streaming spatial MLLMs.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
