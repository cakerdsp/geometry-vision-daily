# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：44
- 分类分布：
  - Embodied / Robotics / AR Applications: 16
  - Neural Scene Representations & Rendering: 12
  - 3D Reconstruction & Multi-view Geometry: 11
  - Dynamic / 4D Reconstruction: 3
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的科研趋势综合分析。

---

#### 今日主要趋势

1.  **从“适用特定场景”向“通用性与泛化性”全面演进**：当前研究不再满足于在特定、受控环境下表现良好的方法，而是致力于开发能够直接处理多种复杂、非结构化场景的通用模型。例如，**Meridian** 针对非城市环境的跨视角定位，**UniSHARP** 的通用相机模型渲染，以及 **CIPER** 统一检索与位姿估计的任务，都鲜明地体现了这种趋势。这背后是对模型泛化能力、鲁棒性和零样本部署能力前所未有的强调。

2.  **神经隐式/显式表示与物理/几何先验的深度融合**：无论是3D高斯泼溅（3DGS）还是神经辐射场（NeRF），研究者正试图将更明确的几何、物理或声学知识引入神经表示中。**Geometry Gaussians** 通过增加几何不透明度参数解耦外观与几何；**SimuScene** 把物理引擎作为诊断工具引入重建流程；**Towards Realistic 3D Sonar Simulation** 则将声学传播原理融入仿真。这表明纯数据驱动的“黑盒”表示正在向融合先验知识的“灰盒”进化，以提升表示的真实性和可编辑性。

3.  **高效、实时与流式处理成为核心瓶颈与突破口**：随着模型复杂度和输入数据速率的提升，实时性要求变得极为苛刻。多个工作直接以此为出发点：**RadiusFPS** 通过算法剪枝加速点云降采样；**CLEAR** 用单步潜空间漂移替代扩散模型的多步去噪；**LiAuto-GeoX** 通过知识蒸馏获得高效紧凑的模型；**GS-NFS** 和 **Anchor3R** 分别针对动态3DGS的流传输和长时序在线建图提出并行加速与流式架构。这显示领域正在从“能跑就行”转向“快而稳地跑”。

4.  **多模态感知与融合的实用化探索**：从简单的RGB-D融合扩展到更复杂的传感器组合（如RGB-热成像、相机-IMU-声纳），并且开始解决数据模态间不对齐、不配对等实际问题。**Unpaired RGB-Thermal Gaussian-Splatting** 解决了无配对校准的跨模态新视角合成；**CLEAR** 融合视觉与大语言模型（LLM）进行驾驶规划。此外，**Impostor** 与 **Multi-Camera AR Guidance**等应用也体现了多视角/多传感器在实际系统中的集成趋势。

5.  **从“重建”到“可交互/可操作”的范式转变**：三维重建的最终目的不仅仅是得到几何模型，更要服务于下游的机器人操作、仿真或分析。**SimuScene** 明确以“物理仿真就绪”为目标；**AffordanceVLA** 和 **CLEAR** 直接通过视觉-语言-动作模型指导机器人/车辆的行为。这表明学界正更主动地将感知、重建、理解和动作生成串联为端到端的认知闭环。

#### 技术路线观察

| 方向 | 技术侧重点 | 代表论文 |
| :--- | :--- | :--- |
| **几何基础模型** | 强调零样本泛化、长时序流式处理和几何一致性。多采用Transformer架构，结合稀疏先验（如LiDAR）或局部测量预测。 | **Meridian** (度量-语义基元匹配), **Anchor3R** (瞬态锚点流式重建), **LiAuto-GeoX** (蒸馏与几何先验) |
| **3D/4D 重建** | 从静态场景扩展到动态/4D场景，并关注稀疏数据、长时序和实时性问题。 包括表面重建与体素表示。 | **4D Reconstruction from Sparse Dynamic Cameras** (3D轨迹初始化), **Hierarchical Space Partition** (面片组装), **GS-NFS** (动态GS压缩), **SimuScene** (物理感知重建) |
| **神经场景表示与渲染** | 核心技术路线为3DGS的扩展，包括：适应非常规相机、解耦外观与几何、减少高斯基元数量、以及引入多模态数据。 | **UniSHARP** (通用相机), **Geometry Gaussians** (几何解耦), **ZipSplat** (基元稀疏化), **Unpaired RGB-Thermal GS** (多模态无对齐) |
| **机器人/AR应用** | 侧重于提升感知效率、融合高级语义（LLM/可供性）和实现真实世界的交互与控制。强调端到端、低延迟和实际部署。 | **RadiusFPS** (加速采样), **CLEAR** (LLM指导规划), **AffordanceVLA** (可供性中间表示), **MAD** (地图感知世界模型), **Multi-Camera AR Guidance** (AR交互) |

#### 值得优先阅读的论文

1.  **Geometry Gaussians: Decoupling Appearance and Geometry in Gaussian Splatting**：**优先级极高**。该文直指当前主流3DGS框架（同时表示纹理和几何）的固有缺陷，并提出了一个极其简洁（仅增加一个参数）且有效的解决方案。对于所有从事3DGS相关研究的学者，理解这一缺陷和解决方案是基础性的。阅读全文以确认其在不同场景下的量化对比。
2.  **Meridian: Metric-Semantic Primitive Matching for Cross-View Geo-Localization Beyond Urban Environments**：**优先级高**。该工作在之前专注于城市环境的跨视角定位领域，首次在非结构化自然环境中展示了无需特定区域训练的鲁棒定位能力。这对于户外机器人、自动驾驶等应用具有重要的启发性。阅读全文确认其在不同野外环境下的失败案例和泛化边界。
3.  **ZipSplat: Fewer Gaussians, Better Splats**：**优先级高**。该文提出的前馈式方法能够仅用1/6的高斯数量即达到或超越基线性能，实现了表示预算与场景复杂度的匹配。这对降低存储、传输和渲染开销具有重要意义，是提升3DGS实用性的关键步骤。需要仔细阅读其聚类策略和推理时的质量控制机制。
4.  **LiAuto-GeoX: Efficient Grounded Driving Transformer**：**优先级高**。该文展示了如何将大规模、高容量的几何模型通过知识蒸馏，变成一个足以在车端实时运行（KITTI上220 FPS）的紧凑模型。其提出的蒸馏框架（掩码引导深度感知+相对位姿关系）值得深入研究，是连接学术前沿与实际部署的典范。
5.  **Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping**：**优先级高**。该文精准指出了当前流式前馈重建方法在长序列下的漂移问题，并基于“当前帧为中心”的局部测量思想提出了新颖有效的解决方案。对于SLAM和在线建图领域的研究者具有重要参考价值。建议阅读全文以评估其在极端长序列上的漂移程度。

#### 可能的研究机会

1.  **结合“几何解耦”与“高效表示”**：**ZipSplat**解决的是高斯数量冗余问题，**Geometry Gaussians**解决的是几何表达力不足问题。将两者的思想结合，即设计一个既能根据场景复杂度自适应分配高斯数量、又能同时高质量表达外观和几何的框架，是一个很有潜力的方向。
2.  **为通用相机模型设计高效的物理-神经融合表示**：**UniSHARP**实现了对不同全局相机模型的通用渲染，可以引入**SimuScene**的思想，在这种通用表示中内嵌物理仿真引擎，实现“一次重建，处处仿真”，尤其适用于需要模拟多种传感器（如全景+深度）的虚拟环境构建。
3.  **基于基元匹配的自主导航闭环**：**Meridian**展示了基于度量-语义基元的零样本跨视角定位能力，而**MAD**展示了环境地图感知的飞行控制。将两者结合，利用**Meridian**为无人机/机器人提供无GPS的全球定位初始化，然后由**MAD**进行局部敏捷导航和地图更新，可以形成一个稳健的完全自主导航闭环。
4.  **融合可供性预测的流式场景重建**：**AffordanceVLA**提出了可供性预测作为感知-动作的中间桥梁，而**Anchor3R**专注于

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-08T12:21:33-04:00
**Total number of papers:** 44
**Number of papers added in the latest update:** 1
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

#### 2026-06-02 - PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting

**Authors:** Adrian Ramlal, John S. Zelek
**Links:** [abs](https://arxiv.org/abs/2606.03479) - [pdf](https://arxiv.org/pdf/2606.03479)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, 4D Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting
- 作者：Adrian Ramlal, John S. Zelek
- 出版日期：2026-06-02
- 分类：Dynamic / 4D Reconstruction（主要），Neural Scene Representations & Rendering（次要）
- 链接：摘要页 https://arxiv.org/abs/2606.03479 | PDF https://arxiv.org/pdf/2606.03479

### 一句话总结
PersistGS 通过将可微刚体动力学仿真与3D高斯泼溅相结合，在物体完全被遮挡期间恢复其持久性，从而提升动态场景重建的物理保真度。

### 研究问题
动态3D高斯泼溅方法在运动物体被多相机视频完全遮挡时，物体对应的3D高斯失去光度监督梯度信号，导致高斯退化，无法正确重建物体的动态行为。如何在没有视觉信号的遮挡期间，保持物体的持久性并生成物理上准确的轨迹？

### 核心思路/方法
1. **场景分解**：将场景分解为每个物体的高斯表示和碰撞网格。
2. **可微物理仿真**：从观测到的遮挡前轨迹中，通过可微仿真估计摩擦系数和速度。
3. **轨迹预测**：利用可微刚体动力学方程预测遮挡期间的SE(3)轨迹，该轨迹能够捕捉弹跳、摩擦减速和方向变化等接触事件。
4. **损失函数**：引入质心轮廓损失，将位置梯度与外观噪声分离，使轨迹误差比光度监督降低40%。
5. **评估方式**：使用留出的、观察到物体遮挡过程的相机进行测试。

### 主要贡献
1. 提出PersistGS方法，首次将可微刚体物理仿真与3D高斯泼溅结合，解决了遮挡下的物体持久性问题。
2. 通过可微仿真预测的轨迹满足刚体动力学方程，能够建模运动学外推无法模拟的接触事件（如弹跳、摩擦减速）。
3. 在合成场景实验中，PersistGS相较于匀速外推在PSNR上提升+2.46dB，且与真实轨迹上界仅差0.19dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法针对动态场景重建中遮挡这一关键难题，提出了将物理仿真与神经渲染结合的新范式，且实验指标提升显著（+2.46dB PSASNR），并接近理想上界。对于关注4D重建、物理感知渲染的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (3DGS) methods reconstruct time-varying scenes from synchronized multi-camera video using photometric supervision. When a moving object becomes fully occluded from all training cameras, this supervision vanishes: the Gaussians representing it receive no gradient signal and degrade. Existing approaches to incomplete observations in neural reconstruction rely on learned generative priors that prioritize visual plausibility over physical correctness. We propose $\textbf{PersistGS}$, a method that restores object permanence during occlusion by coupling differentiable rigid body simulation with 3D Gaussian Splatting. Our approach decomposes the scene into per-object Gaussians and collision meshes, estimates friction and velocity from the observed pre-occlusion trajectory via differentiable simulation, and uses the resulting SE(3) trajectory to position object Gaussians throughout the occlusion period. Because the predicted trajectory satisfies the governing equations of rigid body dynamics, it faithfully captures contact events (bounces, friction-based deceleration, direction changes) that kinematic extrapolation cannot model. We introduce a centroid silhouette loss that isolates positional gradients from appearance noise, yielding 40% lower trajectory error than photometric supervision. We evaluate using cameras withheld from training that observe the object during its occlusion. Experiments on synthetic scenes show that PersistGS outperforms constant velocity extrapolation by +2.46dB PSNR and comes within 0.19dB of a ground-truth trajectory upper bound.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

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

#### 2026-06-02 - SAMatcher: Co-Visibility Modeling with Segment Anything for Robust Feature Matching

**Authors:** Xu Pan, Qiyuan Ma, Mingyue Dong, He Chen, Wei Ji, Xianwei Zheng
**Links:** [abs](https://arxiv.org/abs/2606.03406) - [pdf](https://arxiv.org/pdf/2606.03406)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** image matching, structure from motion, feature matching, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAMatcher: Co-Visibility Modeling with Segment Anything for Robust Feature Matching
- 作者：Xu Pan, Qiyuan Ma, Mingyue Dong, He Chen, Wei Ji, Xianwei Zheng
- 出版日期：2026-06-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2606.03406；PDF: https://arxiv.org/pdf/2606.03406

### 一句话总结
SAMatcher提出了一种基于“共同可见性建模”的特征匹配框架，利用Segment Anything Model（SAM）通过预测跨视图的共可见区域掩码和边界框作为结构先验，来提升大视角和尺度变化下的鲁棒特征匹配性能。

### 研究问题
如何通过显式建模跨视图的“共同可见区域”来改进特征匹配的鲁棒性，尤其是在大视角和尺度变化较大的场景下。

### 核心思路/方法
1.  **共可见性建模**：不直接进行局部特征匹配，而是先预测跨视图共同可见区域的掩码（mask）和边界框（bounding box），作为后续匹配的结构先验。
2.  **基于SAM的交互机制**：内置对称的跨视图交互机制，实现双向特征交换和跨视图语义对齐。
3.  **统一监督方案**：联合优化掩码预测、边界框回归以及掩码-边界框一致性约束三个目标。

### 主要贡献
1.  提出了SAMatcher，一个通过共可见性建模来估计对应关系的特征匹配框架。
2.  展示了原本用于单目分割的基础模型（SAM）可以通过显式的共可见性建模，扩展应用于多视图对应关系推理。
3.  在多个挑战性基准上，方法在存在大视角和尺度变化的情况下，显著优于现有匹配管道。

### 局限性
摘要未提供足够信息。摘要中未提及任何关于计算复杂度、失败案例或具体应用场景限制的局限性讨论。

### 阅读优先级
**高**
理由：该工作首次系统地将SAM大模型引入特征匹配任务，通过显式共可见性建模提供了一个新的解决思路，并且实验证明在大视角变化场景下具有显著优势。这对于三维重建、视觉定位等下游应用具有重要潜在价值，属于将基础模型拓展到新任务领域的创新性工作。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：BA-T: An Iterative Transformer for Two-View Bundle Adjustment
- 作者：Ganlin Zhang, Weirong Chen, Daniel Cremers, Xi Wang
- 出版日期：2026-06-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.03287

### 一句话总结
BA-T 提出一种基于迭代Transformer的轻量级网络，通过模拟经典束调整（BA）的结构化更新过程，在隐式token空间内逐步优化双视图位姿与几何重建，以较小的解码器参数量实现媲美大模型的精度。

### 研究问题
现有前馈3D重建模型依赖深层交叉注意力解码器进行信息交换，但缺乏几何精化机制，导致多视图一致性差。如何设计一种轻量、结构化的迭代方法来替代深度解码器堆叠，同时提升位姿和重建精度？

### 核心思路/方法
- 将经典束调整（BA）视为位姿与局部几何之间迭代信息传播的过程，并将其抽象为隐式token空间中的可重复层（repeatable layer）。
- 提出BA-T：一个迭代Transformer，每一层利用潜在残差（latent residual）执行类似BA的结构化更新，而非依赖深层注意力堆叠。
- 采用单一轻量级层代替深度解码器，通过多次迭代逐步精化预测结果。

### 主要贡献
1. 提出BA-T，一种将束调整风格的结构化更新引入Transformer迭代框架的方法，实现隐式特征空间的几何精化。
2. 在仅使用传统模型16%解码器参数的情况下，达到或超越更大规模模型的性能，展现极佳的参数效率。
3. 实验证明BA-T能随迭代次数稳步提升位姿与重建精度，并增强跨视图一致性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对多视图几何与3D重建中的一个核心瓶颈（解码器深度与多视图一致性），提出了一种结构紧凑的迭代方案，具有显著参数效率提升，且公开代码。对于关注轻量级、高效Transformer在几何任务中应用的读者，有直接参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting
- 作者：Yanchen Wang, Lenny Aharon, Wangshu Zhu, Kyle Daruwalla, Linghua Zhang, Jiaru Zou, Selmaan Chettih, Helen Hou, Liam Paninski, Matthew R Whiteway
- 出版日期：2026-06-01T22:34:14Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：摘要页 https://arxiv.org/abs/2606.02937 ；PDF https://arxiv.org/pdf/2606.02937

### 一句话总结
BEAST3D是一个自监督预训练框架，通过可微渲染预测3D高斯溅射（Gaussian splats）从无标签多视角视频中学习3D视觉表示，并用于动物行为分析与神经编码。

### 研究问题
如何从实验室场景中的稀疏多视角视频（仅4个视角）中，无需人工标注即可提取丰富的3D动物行为表示，并有效应用于下游任务（新视角合成、姿态估计、神经编码）。

### 核心思路/方法
- 采用自监督预训练框架：在未标记的、标定过的多视角视频上训练。
- 使用视觉Transformer预测3D高斯溅射，并通过可微渲染重建被遮蔽的视角（held-out views）。
- 在训练过程中同时分割动物与背景。
- 直接利用已知相机参数实现稀疏视角（最少4个视角）下的3D结构重建，避免像通用模型那样需依赖密集重叠视角来估计相机几何。

### 主要贡献
1. 提出BEAST3D自监督框架，可从无标签多视角视频中学习视角不变的3D表示。
2. 实现了在稀疏视角（如4个视角）下的3D结构重建，解决了通用模型在实验室场景中因视角不足而失效的问题。
3. 在四个物种的数据集上展示框架的有效性，涵盖三个下游任务：新视角合成（验证3D表示质量）、多视角姿态估计（提供稀疏关键点轨迹）、以及神经编码（将3D行为特征与神经活动关联）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：本工作面向动物行为分析与神经编码领域，方法上融合了自监督学习、3D高斯溅射和多视角几何，对于从事计算神经科学、动物行为量化或3D场景理解的研究者有一定参考价值。但若读者不涉及该领域，或更关注通用3D重建方法，则阅读优先级较低。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Modeling Depth Ambiguity: A Mixture-Density Representation for Flying-Point-Free Depth Estimation
- 作者：Siyuan Bian, Congrong Xu, Jun Gao
- 出版日期：2026-06-01T17:50:28Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要链接：https://arxiv.org/abs/2606.02552；PDF链接：https://arxiv.org/pdf/2606.02552

### 一句话总结
本文提出一种混合密度表示法（MDA），让模型为每个像素预测多个深度假设及其概率，从而消除深度估计中物体边界处的“飞点”伪影。

### 研究问题
深度估计模型在物体边界处常产生“飞点”（flying points），即在空空间中预测虚假的3D点。原因是标准做法为每个像素只分配单个深度假设，导致边界像素的深度被拉向前景和背景之间的中间值，而非任何真实表面。

### 核心思路/方法
采用混合密度表示（Mixture-Density Representation, MDA），使模型为每个像素预测多个深度假设及其关联概率。在边界处，不同假设可与不同表面对齐，解码时从这些假设中选择一个深度，而非在空空间中插值。该方法还自然扩展到透明物体（预测多个深度层）和天空区域（用专用组件分离无限远天空与有限深度区域）。

### 主要贡献
- 指出“飞点”伪影源于单深度假设建模，并分析其成因。
- 提出MDA混合密度表示法，通过多假设预测消除边界飞点。
- 实验证实该方法在不同骨干网络上显著改善边界重建，在强烈输入模糊下仍有效去除飞点，且运行时开销可忽略不计。
- 展示该框架可扩展至透明物体和天空区域，实现无飞点的天际线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作解决了深度估计中一个持久且关键的失败模式（飞点伪影），方法直接且验证有效，同时关注了透明物体和天空等实际挑战，对3D场景理解和重建领域具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Despite advances in depth estimation, flying points remain a persistent failure mode: near object boundaries, depth estimators often predict spurious 3D points in the empty space between foreground and background surfaces. We trace this artifact to a standard modeling choice: assigning each pixel a single depth hypothesis. At boundaries, a pixel can straddle a foreground and a background surface, so its true depth is ambiguous between the two. A model that predicts a single depth cannot keep both possibilities, so training instead pulls the prediction toward an intermediate depth that lies on neither surface. We address this with MDA, a mixture-density representation that lets the model predict multiple depth hypotheses and their associated probabilities for each pixel. Near boundaries, different hypotheses can align with different surfaces, and the decoded depth is selected from one of these hypotheses rather than placed in the empty space between them. Across different backbones, MDA substantially improves boundary reconstruction and largely removes flying-point artifacts even under severe input blur, while adding negligible runtime overhead. The same mixture-density framework naturally extends to transparent objects, where it predicts multiple depth layers at transparent pixels, and to sky regions, where a dedicated component separates the unbounded sky from finite-depth regions, producing flying-point-free skylines. Project Page: https://biansy000.github.io/mda-site/.

</details>

## Neural Scene Representations & Rendering

### 2026-06

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

#### 2026-06-02 - GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation

**Authors:** Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li
**Links:** [abs](https://arxiv.org/abs/2606.03682) - [pdf](https://arxiv.org/pdf/2606.03682)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation
- 作者：Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03682

### 一句话总结
本文提出GN0，一个统一的数据、模拟与学习框架，通过大规模数据集、高保真仿真平台和强化学习驱动的导航基础模型，在视觉语言导航任务上达到超越现有方法的性能。

### 研究问题
视觉语言导航（VLN）系统中，导航数据的可用性和质量有限，导致模型的泛化能力和长程任务执行能力不足。

### 核心思路/方法
1. **数据生成**：策展多样化3D场景，并开发自动化管线，构建大规模GN-Matrix数据集。
2. **仿真平台**：基于3D高斯泼溅（3DGS）引擎，搭建支持交互漫游和碰撞感知导航的高保真模拟平台。
3. **基准评估**：提出首个基于鸟瞰图（BEV）的基准GN-Bench，集成动态3DGS虚拟角色用于人机交互评估。
4. **模型训练**：采用强化学习驱动的导航基础模型BAE（Break and Establish）。先进行监督学习，再通过DAgger算法让模型接触 rollout 状态，打破狭窄的专家分布，并支持下游RL探索。
5. **表示学习**：GN-BAE将高保真3DGS渲染的BEV表示作为紧凑记忆，以解锁视觉语言模型中的潜在空间推理。

### 主要贡献
1. 提出GN-Matrix数据集，涵盖大规模多样化3D场景和自动化的导航数据生成管线。
2. 构建高保真仿真平台，支持交互式漫游和碰撞感知导航。
3. 引入首个基于BEV的基准GN-Bench，具备动态3DGS虚拟角色的人机交互评估能力。
4. 开发RL驱动的导航基础模型BAE，通过监督学习与DAgger算法结合，提升模型在分布外状态下的探索能力。
5. 统一了基于地图和无地图的任务（如指令跟随、人跟随、目标导航），并在GN-Bench和VLN-CE上达到超越现有最优方法的表现。

### 局限性
摘要未提供足够信息。摘要未提及模型的计算开销、对特定场景或任务的失败案例、数据集的潜在偏差、仿真到真实场景的迁移效果，以及动态3DGS虚拟角色的真实性局限。

### 阅读优先级
中  
理由：该工作提出了一个涵盖数据、仿真、评估和学习的统一框架，在VLN领域具有系统性的创新，适合对具身智能、导航和强化学习感兴趣的研究者阅读。但摘要未提供详细的定量实验结果或深入的方法消融分析，优先程度中等。

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
- 标题：UnsOcc: 3D Semantic Occupancy Prediction in Unstructured Scene via Rendering Fusion
- 作者：Ye Wu, Ruiqi Song, Baiyong Ding, Nanxin Zeng, Junjie Cheng, Yunfeng Ai
- 出版日期：2026-06-02T12:50:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03581

### 一句话总结
本文提出UnsOcc，一种针对非结构化场景（如露天矿场）的多模态3D语义占用预测框架，通过渲染融合模块和基于高斯泼溅的细节感知辅助监督，提升模型在稀疏场景下的预测鲁棒性。

### 研究问题
非结构化场景（如不规则障碍物、稀疏布局）中，直接应用3D语义占用预测时面临两个困难：场景稀疏性阻碍有效的跨模态融合，以及长尾分布问题导致预测性能下降。

### 核心思路/方法
- 构建一个专用的露天矿场非结构化场景数据集。
- 提出渲染融合模块（RenderFusion），通过双向渲染监督增强跨模态特征对齐。
- 提出细节感知辅助监督方法（GSRefinement），基于高斯泼溅（Gaussian Splatting）将稀疏3D占用预测投影为密集2D语义分割图，从而对长尾类别进行有效监督。

### 主要贡献
- 提出UnsOcc，一个针对非结构化场景的多模态3D语义占用预测框架。
- 引入RenderFusion模块，通过双向渲染监督改进跨模态融合。
- 提出GSRefinement方法，利用高斯泼溅生成密集2D语义图以辅助长尾类别监督。
- 在露天矿场数据集和nuScenes数据集上，所提方法显著优于现有最先进方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对自动驾驶中非结构化场景这一有挑战性的实际应用问题（如矿场），提出了新颖的渲染融合与高斯泼溅辅助监督方法，并在两个数据集上验证了有效性。目标读者若关注多模态融合、3D语义占用预测或非标准场景处理，则该论文具有较强参考价值。

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
本文提出了Poison-3DGS基准，系统地研究了3DGS重建管线中不同阶段对攻击痕迹的可检测性差异。

### 研究问题
在3DGS面临多种投毒攻击（如幻影物体注入、计算成本放大、后验水印）的背景下，如何从检测角度理解不同攻击在不同重建阶段（多视图图像、几何、训练动态、高斯参数）留下的可检测信号特性？

### 核心思路/方法
1. 构建Poison-3DGS基准：涵盖多种场景和攻击类型，收集并利用多阶段中间表示（多视图图像、几何、训练动态、高斯参数）作为检测特征。
2. 进行系统性的阶段依赖性可检测性分析：比较不同攻击在不同阶段留下的取证信号强度，评估检测效果随阶段变化的情况。

### 主要贡献
- 提出了首个用于阶段化检测特性分析的标准基准Poison-3DGS。
- 揭示了可检测性在不同阶段存在显著变化，且没有一个阶段在所有攻击类型中始终最优。
- 指出后期阶段（如训练动态、高斯参数统计）能提供早期阶段无法捕获的强检测线索。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦于3DGS安全防御中的检测问题，针对性强，但属于基准构建与特性分析类研究，适合对3DGS安全或可解释性感兴趣的专业研究者阅读；对一般读者或应用导向需求者优先级不高。

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
<summary>AI 简析</summary>

### Metadata
- 标题：FreeStreamGS: Online Feed-forward 3D Gaussian Splatting from Unposed Streaming Inputs
- 作者：Ruiyang Chen, Feiran Li, Chu Zhou, Zonglin Li, Zhanyu Ma, Heng Guo
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03254

### 一句话总结
该论文提出一种名为FreeStreamGS的在线前馈框架，能够在无位姿的流式输入下实现高效、高质量的新视角合成（NVS），其渲染质量可与依赖未来帧的离线前馈3DGS方法相媲美。

### 研究问题
如何从无位姿的流式图像输入中，在线进行高效、高质量的新视角合成，克服传统前馈3DGS方法在流式场景下因多视图一致性要求而出现的渲染退化问题。

### 核心思路/方法
1. 提出一个在线前馈框架，不依赖未来帧信息。
2. 引入**解耦内参恢复头**：用于消除累积的相机内参偏置，防止长时间流式处理中的场景尺度抖动。
3. 引入**动态点细化偏移策略**：通过放松刚性反投影约束，来修正耦合的位姿-深度漂移。

### 主要贡献
1. 首次提出了一个健壮的在线前馈框架，用于从无位姿流式输入中高效、高质量地实现新视角合成。
2. 设计了解耦内参恢复头和动态点细化偏移机制，分别解决了内参累积偏置与位姿-深度耦合漂移问题。
3. 实验表明，该方法能获得与最先进离线前馈3DGS方法竞争的渲染质量，且无需访问未来帧。

### 局限性
摘要未提供足够信息，未提及该方法在极端快速运动、严重遮挡、低纹理区域或计算资源受限条件下的具体表现。

### 阅读优先级
**高**  
理由：该工作针对在线流式新视角合成这一实际应用场景中的核心难点（多视图一致性退化），提出了明确且创新的解决方案，并能与离线方法竞争，对3DGS实时应用具有重要参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis
- 作者：Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy
- 出版日期：2026-06-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.03120

### 一句话总结
本文提出KC-3DGS，通过在3DGS训练中引入基于小波域的自然图像统计约束（峰度、跨频带协方差等），改善视角合成的感知质量，尤其在稀疏视图场景下缓解过平滑和结构伪影。

### 研究问题
标准3DGS使用像素空间损失（L1、SSIM）仅约束整体重建误差，导致误差在不同频率尺度上重新分布，造成过平滑和结构伪影，在稀疏视图设置中尤为严重。本文旨在解决这一频率细节缺失问题。

### 核心思路/方法
提出KC-3DGS，在3DGS的可微渲染管道中增加三个小波域约束：
1. 多尺度小波系数对齐损失：显式惩罚缺失的高频细节。
2. 有监督峰度集中损失：鼓励渲染图像匹配真实图像的重尾频率统计特性。
3. 跨频带协方差惩罚：促进频率特化。
理论分析表明，像素空间损失允许一类在小波重分布下不可区分的扰动，而联合目标函数排除了退化解。

### 主要贡献
- 提出结合自然图像统计的小波域监督，增强3DGS的感知保真度。
- 理论证明像素损失存在小波重分布下的不可区分扰动，并验证联合目标可排除退化解。
- 实验在MipNeRF360、Tanks&Temples、MVImgNet、DeepBlending及WRIVA-ULTRRA等数据集上展示了一致的感知质量提升。在WRIVA-ULTRRA上DreamSim提升9.48%，同时在PSNR、SSIM、LPIPS上也有改进。稀疏视图（12张训练图像）下PSNR提升至0.5 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法作为即插即用正则化策略，可直接集成到现有3DGS管线中，显著提升感知质量，并在稀疏视图等困难场景中表现优异。对于从事神经渲染、视角合成或3D场景重建的研究者具有直接参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset  
- 作者：Richard Schwarzkopf, Fabian Immel, Alexander Blumberg, Jonas Merkert, Nils Rack, Kaiwen Wang, Fabian Konstantinidis, Julian Truetsch, Carlos Fernandez, Annika Bätz, Kevin Rösch, Marlon Steiner, Willi Poh, Yinzhe Shen, Royden Wagner, Felix Hauser, Dominik Strutz, Jaime Villa, Gleb Stepanov, Holger Caesar, Ömer Şahin Taş, Frank Bieder, Jan-Hendrik Pauls, Christoph Stiller  
- 出版日期：2026-06-01  
- 分类：神经场景表示与渲染（主要），具身/机器人/AR应用（次要）  
- 链接：abstract: https://arxiv.org/abs/2606.02956; pdf: https://arxiv.org/pdf/2606.02956  

### 一句话总结  
KITScenes Multimodal 是一个高保真、多模态的欧洲自动驾驶数据集，提供首个公开的完整3D交通元素HD地图，并引入四项空间学习基准。

### 研究问题  
现有自动驾驶数据集在传感器精度、地图完整性和地理多样性方面存在不足，限制了场景理解与空间学习的发展。

### 核心思路/方法  
- 构建一套完全同步的高保真传感器套件，包括高分辨率全局快门相机、超过400米探测距离的激光雷达、4D成像雷达和冗余GNSS/INS定位系统。  
- 制作目前公开传感器数据集中最完整的HD地图：首次将所有驾驶相关交通元素（如交通灯）以3D形式映射，达到重投影精确级别，并包含完整拓扑连接。  
- 数据集在街道布局不规则和混合交通模式的城市中采集，以补充现有数据集的地理多样性。  
- 提出四个基准任务：在线HD地图构建、远距离深度估计、新颖视角合成和端到端驾驶，旨在推进具身AI的空间学习。

### 主要贡献  
- 提供了一个高保真、多模态的自动驾驶数据集，传感器性能优于现有数据集。  
- 公开了首个具备完整3D交通元素和拓扑连接的高清地图。  
- 通过采集欧洲不规则街道布局的城市数据，增强了地理多样性。  
- 引入四个促进空间学习的基准任务，覆盖建图、深度估计、视图合成和驾驶控制。

### 局限性  
摘要未提供足够信息：未提及数据集规模（如样本数、序列长度）、具体传感器规格、标注成本、潜在偏差（如天气或光照条件覆盖）或与现有数据集的定量对比结果。

### 阅读优先级  
**高**  
理由：该数据集在传感器精度、地图完整性和基准多样性方面具有显著创新，尤其适用于研究高保真场景理解、空间学习及端到端自动驾驶的学者和工程师。

</details>

<details>
<summary>Abstract</summary>

Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity. We present KITScenes Multimodal, a European dataset built around high-fidelity sensors and maps. Our fully synchronized sensor suite combines high-resolution global-shutter cameras, long-range lidar beyond 400m, 4D imaging radar, and redundant GNSS/INS localization. Our HD maps are, to our knowledge, the most complete of any sensor dataset, validated through autonomous driving trials on open-source software. For the first time in a public dataset, all driving-relevant traffic elements, such as traffic lights, are mapped in 3D to a reprojection-accurate level with full topological connectivity. Recorded in cities with irregular street layouts and mixed traffic modes, our dataset complements existing datasets by broadening the available geographic diversity. We also introduce four benchmarks, each advancing spatial learning for embodied AI: online HD map construction, long-range depth estimation, novel view synthesis, and end-to-end driving. Project page: https://kitscenes.com/

</details>

## Embodied / Robotics / AR Applications

### 2026-06

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

#### 2026-06-02 - A 3D Isovist World Model -- Revealing a City's Unseen Geometry and Its Emergent Cross-City Signature

**Authors:** Xuhui Lin, Stephen Law, Nanjiang Chen, Kunyao Li, Tao Yang
**Links:** [abs](https://arxiv.org/abs/2606.03609) - [pdf](https://arxiv.org/pdf/2606.03609)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A 3D Isovist World Model – Revealing a City’s Unseen Geometry and Its Emergent Cross-City Signature
- 作者：Xuhui Lin, Stephen Law, Nanjiang Chen, Kunyao Li, Tao Yang
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03609

### 一句话总结
本文提出一种以3D isovist（球面可见深度图）为预测目标的世界模型，仅通过几何信息学习城市可导航空间动态，并发现该模型在训练于多个城市时能自发产生可区分城市身份的时空特征。

### 研究问题
现有具身智能体的世界模型通常预测场景外观（如RGB图像）或简化的俯视占用网格，忽略了三维空间中的可导航几何结构（如架空层、多层空间），难以准确建模智能体实际移动的负空间（建筑物之间的开放体积）。研究目标是：如何仅基于几何信息、无需外观特征，预测智能体在移动中周围可导航空间的变化。

### 核心思路/方法
1. **预测目标设计**：将3D isovist（球面可见深度图）作为世界模型的预测目标，记录每个方向上到最近表面的距离，从而编码开放体积的几何结构。
2. **预测机制**：模型基于短历史isovist序列和当前动作，预测下一个isovist的深度残差（使解码器保留建筑边缘锐利性）。
3. **训练策略**：采用自展开调度采样（self-rollout scheduled sampling），在训练中向模型提供带有几何流形扰动的上下文，使其适应预测偏差。
4. **持久空间记忆**：引入隐式俯视鸟瞰空间图（persistent latent BEV spatial map），实现跨路径的一致性保持。
5. **跨城市实验**：在曼哈顿和巴黎两个城市数据上训练单一模型，并测试其在不同城市路径上的表现。

### 主要贡献
- 提出一种不依赖外观信息、仅基于三维几何的轻量级世界模型预测框架（3D isovist）。
- 发现跨城市空间特征：单一模型在不同城市中产生线形可解码的城市身份信号，且该信号存在于学习到的动态中而非单帧外观中。
- 提供了开放数据集和可复现的流水线，可用于具身AI、机器人导航和城市分析。

### 局限性
摘要未提供足够信息：未提及模型在复杂城市环境（如非网格状道路、密集植被遮挡）中的鲁棒性、对传感器噪声的容忍度、多源数据集下的泛化边界，以及与现有外观预测基线的量化对比实验细节。

### 阅读优先级
**高**  
理由：本文提出了一种新颖的几何世界模型范式，聚焦于智能体导航中“可走空间”而非“场景外观”，方向具有实用价值；且发现的跨城市空间特征具有启发性。摘要结构清晰、方法描述完整，适合对具身智能、城市空间分析感兴趣的读者深入阅读。

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
<summary>AI 简析</summary>

### Metadata
- 标题：TASE: Truncation-Aware Semantic Embeddings for 3D Scene Understanding and Editing
- 作者：Tim-Felix Faasch, Jochen Kall, Lucas Nunes, Jens Behley, Cyrill Stachniss
- 出版日期：2026-06-02T08:25:53Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03314

### 一句话总结
TASE 提出一种通过截断感知嵌入空间实现灵活可控的3D场景编辑方法，支持文本驱动编辑并可调节编辑强度。

### 研究问题
如何实现高保真、可编辑且具备可控性的3D语义场景表征，以支持大规模几何修改的文本驱动编辑。

### 核心思路/方法
1. 将预训练的2D语义特征投影到截断感知的嵌入空间，并显式优化该特征空间：减少特征通道数时产出更抽象的语义表示，保留更多通道则保留细粒度细节。
2. 利用尺度和平移等变性损失提高特征的多视图一致性。
3. 编辑时可通过截断策略控制修改与原始场景内容的贴合程度，实现比现有方法更强的大规模修改。
4. 对编辑扩散模型进行微调，以缓解几何变化带来的伪影。

### 主要贡献
- 提出截断感知嵌入空间，实现特征通道数控制下的语义抽象粒度调节。
- 通过尺度和平移等变性损失提升多视图特征一致性。
- 实现文本驱动的3D场景编辑，支持显式控制编辑强度，尤其在大几何修改任务上显著优于现有方法。

### 局限性
摘要未提供足够信息，无法明确提及具体局限性，如方法在不同场景下的泛化能力、计算开销或对特定编辑任务的适用边界等。

### 阅读优先级
高。理由：该方法在3D场景编辑任务上实现了优于现有技术的大几何修改能力，且具备可控性，适用于机器人、自动驾驶、仿真等前沿应用场景，摘要所示方法设计（截断感知嵌入）具有创新性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GeoSem-WAM: Geometry- and Semantic-Aware World Action Models
- 作者：Fulong Ma, Daojie Peng, Wenjun Yue, Jiahang Cao, Bintao Wang, Qiang Zhang, Jun Ma
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03188

### 一句话总结
该论文提出一种结构化世界建模框架GeoSem-WAM，通过在RGB未来预测之外引入几何与语义辅助预测分支，增强世界动作模型的潜在表征，从而在不依赖显式测试时推演的前提下提升具身决策中的动作预测准确性和场景理解鲁棒性。

### 研究问题
现有世界动作模型（WAM）主要依赖基于RGB的未来预测，缺乏对复杂环境的结构和空间理解；此外，其有效性究竟源于显式未来想象还是表征学习尚不明确。论文试图通过结构化监督来增强潜在表征，以解决上述结构性与语义理解不足的问题。

### 核心思路/方法
提出GeoSem-WAM框架，在现有WAM的RGB未来预测主干基础上，增加两个辅助预测分支：未来几何表征分支和未来语义表征分支。通过联合优化这三个分支，模型在统一的潜在空间中同时捕获场景动态、空间几何与语义上下文。推理时避免了显式的未来展开或视频生成，保持高效。

### 主要贡献
1. 提出一种结合几何与语义监督的结构化世界建模框架，用于增强WAM的潜在表征。
2. 引入两个辅助预测分支（几何与语义），在训练中提供结构化世界监督，而测试时不增加额外计算开销。
3. 实验表明结构化世界监督一致地提升了动作预测准确性、场景理解能力和在挑战性具身场景下的鲁棒性。

### 局限性
摘要未提供足够信息，包括对潜在表征可解释性、计算开销对比、未覆盖的场景类型或失败案例的讨论。

### 阅读优先级
中  
理由：该工作针对具身智能中世界模型的结构化表征问题提出了明确的改进方向，方法设计清晰且实验展示了收益，适合对具身决策、世界模型或结构化表示学习感兴趣的读者。但摘要未包含对基线方法的详细对比或消融实验的具体数据，且发表年份较远（2026年），可能需要结合完整论文评估其实际效果与创新程度。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation
- 作者：NVIDIA, :, Aarti Basant, Amlan Kar, Despoina Paschalidou, Fangyin Wei, Francesco Ferroni, Guillermo Garcia Cobo, Haithem Turki, Huan Ling, Jaewoo Seo, James Lucas, Jay Zhangjie Wu, Jialiang Wang, Jonathan Lorraine, Jun Gao, Kai He, Katarina Tothova, Kevin Xie, Michał Tyszkiewicz, Qi Wu, Riccardo de Lutio, Ruilong Li, Sanja Fidler, Seung Wook Kim, Tianchang Shen, Tianshi Cao, Tobias Pfaff, William Lew, Xindi Wu, Xuanchi Ren, Yifan Lu, Yuxuan Zhang, Zan Gojcic, Zian Wang
- 出版日期：2026-06-02T05:11:05Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.03159

### 一句话总结
OmniDreams是一个基于Cosmos扩散模型进行中训练和后训练的实时生成式世界模型，用于在闭环自动驾驶仿真中根据驾驶动作自回归生成动作条件化视频，以模拟极端天气等长尾场景。

### 研究问题
如何在闭环自动驾驶仿真中克服传统重建式神经模拟器对初始捕获数据的依赖，并生成难以捕捉的动态或新颖场景（如极端天气和不可预测的智能体行为），以实现安全、全面的驾驶策略评估。

### 核心思路/方法
- 从Cosmos扩散模型出发，利用其丰富的视觉先验，对OmniDreams进行中训练和后训练（使用21k小时驾驶场景数据）。
- 模型自回归地将过去帧、当前模拟器状态和即时驾驶动作作为条件，生成逼真的传感器观测视频。
- 在闭环系统中与Alpamayo 1策略模型和AlpaSim编排器集成，使OmniDreams作为响应式的环境。
- 额外验证了世界-动作模型（WAM）在NuRec数据集上超越VLA基线的潜力。

### 主要贡献
1. 提出了OmniDreams，一个能够实时自回归生成动作条件化视频的生成式世界模型。
2. 通过中训练和后训练，使模型能够合成传统模拟器难以捕捉的复杂、未观测现象（如极端天气和动态智能体行为）。
3. 展示了在闭环自动驾驶仿真中作为响应式环境的部署效果。
4. 初步结果表明，基于OmniDreams后训练的世界-动作模型（WAM）在NuRec数据集上优于VLA-based Alpamayo 1.5政策模型，且参数量仅为其1/5。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该工作针对自动驾驶仿真中长尾场景生成这一关键瓶颈，提出了基于扩散模型的实时生成式世界模型，方法新颖且具有实际应用价值。初步实验显示出参数效率优势，适合关注自动驾驶仿真与世界模型的研究者阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MARIO: Motion-Augmented Real-Time Multi-Sensor Inertial Odometry
- 作者：Yiquan Li, Taeyoung Yeon, Chenfeng Gao, Vasco Xu, Xuanyou Liu, Karan Ahuja
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications（体现/机器人/AR应用）
- 链接：摘要链接（https://arxiv.org/abs/2606.02996）| PDF链接（https://arxiv.org/pdf/2606.02996）

### 一句话总结
本文提出MARIO，一种通过学习IMU推断的姿势先验并结合多传感器融合（磁力计、气压计、辅助IMU）来提升惯性里程计位置漂移性能的方法，在Nymeria数据集上漂移降低高达42%。

### 研究问题
惯性里程计（仅使用IMU）在人体运动跟踪中仍然存在漂移和噪声问题，尤其是当应用于日常活动数据集（如Nymeria）时，现有学习方法未能显式捕捉人体运动动力学。

### 核心思路/方法
1. 先验姿势学习：通过学习一个IMU推断的姿势先验，将惯性里程计建立在人体运动学基础上，提供物理一致的运动约束。
2. 集成到现有IO架构：将姿势先验集成到现有的惯性里程计架构中，在Nymeria数据集上将位置漂移降低高达36%。
3. 多传感器融合框架：进一步融合商用AR眼镜已有的轻量传感器（磁力计、气压计、辅助IMU），将位置漂移降低高达42%，提升不同运动条件下的鲁棒性和泛化性。

### 主要贡献
1. 引入基于人体运动学的IMU推断姿势先验，提升惯性里程计的物理一致性。
2. 在挑战性Nymeria数据集（比以往工作大5倍）上减少位置漂移最高36%。
3. 提出多传感器融合框架，利用商用AR眼镜现有传感器进一步减少漂移最高42%。
4. 为无相机的精确人体跟踪设立了新基准。

### 局限性
摘要未提供足够信息。未讨论方法在计算开销、实时性限制、不同传感器失效场景下的表现，也未提及数据隐私或传感器校准等潜在问题。

### 阅读优先级
中。理由：该工作针对AR/可穿戴设备中的惯性定位漂移问题提出了一个有明确改进的方案（姿势先验+多传感器融合），在较大数据集上取得了显著效果，适合对IMU跟踪、人机交互或多传感器融合方向的研究者参考。但具体技术细节（如模型架构、训练流程、实时性验证等）需要阅读全文才能判断其可复现性和实际价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion
- 作者：Oskar Natan, Jun Miura
- 出版日期：2026-06-02
- 分类：Embodied / Robotics / AR Applications
- 链接：论文摘要 https://arxiv.org/abs/2606.02979 ; PDF https://arxiv.org/pdf/2606.02979

### 一句话总结
提出一个紧凑型多任务深度学习模型，通过自适应损失加权和中间传感器融合，在单次前向传播中同时处理语义分割、深度估计、激光雷达分割和鸟瞰图投影等多种自动驾驶感知任务，且参数量更少、推理更快。

### 研究问题
如何处理自动驾驶中多种感知任务（如语义分割、深度估计、激光雷达分割、鸟瞰图投影）的联合学习，并解决多任务训练中因任务数量过多导致的学习不平衡问题，同时融合RGB相机、动态视觉传感器（DVS）和激光雷达等多模态输入。

### 核心思路/方法
1. **紧凑型多任务学习模型**：设计一个单一的深度学习模型，无需其他模型支持，即可在单次前向传播中完成多种视图的感知任务（语义分割、深度估计、激光雷达分割、鸟瞰图投影）。
2. **自适应损失加权算法**：针对多个任务造成的学习不平衡问题，提出一种自动调整各任务损失权重的算法，以平衡训练过程。
3. **数据预处理与中间传感器融合**：通过对RGB相机、DVS和激光雷达的数据进行预处理和中间层融合，使模型能处理并合并多种输入模态，实现多位置传感器的信息整合。

### 主要贡献
1. 提出了一种紧凑型多任务感知模型，能以更少参数保持或提升性能，推理速度更快，GPU内存占用更低。
2. 设计自适应损失加权算法，缓解多任务学习中的不平衡问题。
3. 通过数据预处理和中间传感器融合技术，实现了RGB相机、DVS和激光雷达多模态输入的有效整合。
4. 在3个CARLA仿真数据集和1个真实世界nuScenes-lidarseg数据集上取得了稳定一致的表现，并公开代码以支持后续研究。

### 局限性
摘要中未明确提及模型的局限性（如复杂环境下的可靠性、计算资源需求、未测试的场景等）。此外，所有实验均在仿真和单一真实数据集进行，摘要未提供足够信息说明在更复杂真实场景下的泛化能力。

### 阅读优先级
**高**  
理由：该研究针对自动驾驶感知中的多任务学习和传感器融合核心问题，提出了紧凑且高效的解决方案，并显著减少了参数量和计算资源消耗，符合当前自动驾驶系统对实时性和节能的需求。同时，实验结果在多个数据集上表现一致，代码公开，适合相关领域研究人员快速验证和借鉴。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data
- 作者：Teng Hu, Mingchun Lu, Yating Wang, Jiangning Zhang, Jinkun Hao, Ye Pan, Ran Yi, Lizhuang Ma, Dacheng Tao
- 出版日期：2026-06-01
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2606.02753；PDF: https://arxiv.org/pdf/2606.02753

### 一句话总结
MetaWorld 提出了一种从单视角视频数据扩展至多智能体视频世界模型的新框架，通过单目世界状态展开、智能体感知生成器和世界状态对齐技术，解决了多视角数据稀缺和跨视角状态一致性两大问题。

### 研究问题
如何从大规模单视角视频（而非昂贵的多视角录制数据）中构建多智能体视频世界模型，并保证不同视角生成的视频流在共享物理环境和事件演化上具有一致性。

### 核心思路/方法
1. **Monocular World-State Unrolling (MWSU)**：将单目视频显式分解为相机操作者的自运动和可见主体的空间轨迹，从单个视角中提取同步的多智能体运动数据，绕过多相机配置需求。
2. **Subject-Aware World Generator**：基于每智能体身份图像进行外观驱动的模拟，实现对视频中特定主体的视觉控制。
3. **World-State Alignment (WSA)**：在视频DiT的每个Transformer层中插入帧间跨分支交叉注意力机制，联合同步去噪过程，同时保证静态几何一致性和动态运动一致性。

### 主要贡献
1. 提出了从单视角视频扩展至多智能体视频世界模型的框架，解决了数据可扩展性问题。
2. 设计了单目世界状态展开方法，无需多相机设置即可获得同步的多智能体运动数据。
3. 引入世界状态对齐机制，确保不同视角的视频流在共享物理环境和事件演化上保持一致。
4. 实验证明MetaWorld在跨视角一致性和身份保真度上优于现有方法。

### 局限性
摘要未提供足够信息（未讨论可能的失败案例、对复杂场景的适用边界、计算开销或对视频数据质量的依赖等）。

### 阅读优先级
**高**  
理由：该工作针对多智能体视频世界模型的核心瓶颈（数据获取困难和跨视角对齐）提出了新颖且可扩展的解决方案，方法设计完整（包含分解、生成、对齐三个关键模块），涉及重要应用场景（具身AI、元宇宙），且论文发表于2026年，具有方向引导性。

</details>

<details>
<summary>Abstract</summary>

Video world models are a foundational generative technology for embodied AI and the Metaverse, yet existing approaches are inherently limited to a single agent observing from a single perspective. Extending these models to multi-agent settings introduces two critical challenges: data scarcity (coordinated multi-view recordings are prohibitively expensive to collect for general open-domain scenarios) and world state alignment (independently generated video streams cannot ensure that shared physical environments and events evolve consistently across views). To address these challenges, we propose MetaWorld, a novel framework that scales multi-agent video world models to open-domain environments directly from single-view videos. First, we introduce Monocular World-State Unrolling (MWSU) to explicitly decompose monocular footage into the camera operator's ego-motion and the visible subject's spatial trajectory. This camera-trajectory decomposition naturally extracts synchronized multi-agent motion data within a shared 3D space, completely bypassing the need for multi-camera setups. Second, for precise visual control, we develop the Subject-Aware World Generator to enable appearance-driven simulation conditioned on per-agent identity images. Finally, to ensure both views are grounded in the identical physical reality, we propose World-State Alignment, a per-frame inter-branch cross-attention mechanism inserted at every transformer layer of the video DiT. By jointly synchronizing the denoising process, WSA enforces both static geometric consistency and dynamic motion consistency, encouraging that the shared 3D environment and physical events remain well-aligned across both egocentric views. Extensive experiments demonstrate that MetaWorld achieves superior cross-view consistency and identity fidelity, establishing a highly scalable, physics-driven paradigm for multi-agent video world modeling.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
