# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：60
- 分类分布：
  - Neural Scene Representations & Rendering: 20
  - 3D Reconstruction & Multi-view Geometry: 18
  - Embodied / Robotics / AR Applications: 15
  - Dynamic / 4D Reconstruction: 4
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，以下是对今天论文列表的科研趋势综合分析。

#### 今日主要趋势

基于今日论文，以下概括出五条主要趋势：

1.  **3D高斯泼溅（3DGS）向工程化与专业化应用纵深发展：** 多个工作不再停留于通用的静态场景重建，而是针对具体应用场景进行深度优化，并解决部署中的核心工程问题。这包括针对驾驶场景的即时与高效重建（`Instant NuRec`）、面向自动驾驶道路表面的特定表示与优化（`RoGS`）、以及利用GPU硬件特性进行压缩以降低内存占用（`Compression of 3D Gaussian Splatting Data`）。这表明3DGS正从纯学术研究转向解决实际部署中的效率、规模和专业性问题。

2.  **从“学习”到“推理”，几何与物理先验回归舞台中央：** 多篇论文显示出对抗纯“端到端”数据驱动方法高计算成本、低泛化性的趋势，转而将可微几何、物理模型等先验知识融入神经网络。例如，`G²SR`利用多视图几何的解析解从2D对应关系直接推导3D高斯，绕开了重型Transformer网络。`Volumetric Inverse Rendering`通过微分形式的辐射传输方程（RTE）作为残差约束来强制执行全局光照，替代了可微蒙特卡洛光传输模拟。这种“轻量级网络 + 强先验知识”的混合范式有望在实时性和鲁棒性上取得突破。

3.  **“世界-动作模型（WAM）”加速具身智能与控制的结合：** 出现了将大规模视频扩散模型应用于机器人控制的先驱工作。`AeroAct`首次将世界-动作模型实例化到真实世界的四旋翼飞行中，利用视频扩散Transformer预测动作轨迹，并创新性地将未来视觉帧作为密集训练监督。这标志着从纯视觉感知、导航到利用生成模型进行闭环控制的范式转变，为更通用的机器人学习提供了新思路。

4.  **数据驱动方法的“数据集-基准-模型”闭环构建成为主流：** 为克服特定领域的瓶颈，大型基准数据集及其配套评估协议（Benchmark）和基础模型正被有组织地提出。例如，在全身人体重建（`Human4K`）、具身操作（`Open-AoE`）、仿真就绪3D资产（`UniPhysGen`）等领域，都遵循了“构建高质量数据集 -> 设计评估基准 -> 提出强基线模型”的完整闭环。这表明，在解决特定复杂问题时，系统性的数据基建是推动领域发展的关键。

5.  **重视输入形态与通信效率，向“去序”、“低带宽”、“非结构”场景拓展：** 多个工作关注于更贴近实际应用的复杂输入。`Immediate 3D Gaussian Splat Reconstruction`首次处理无序（out-of-order）输入并保持全局一致性。`Communication-Efficient Relative Pose Estimation`专为短暂相遇、低带宽的协作感知设计。`JADE-GS`利用事件相机（Event Camera）的高时间分辨率信号来辅助模糊图像的3D重建。这些工作反映了社区正从理想化输入（连续、有序、大带宽）向更具挑战性的真实世界输入条件演进。

#### 技术路线观察

- **几何基础模型与3D重建**：今日论文中，该方向呈现出两条并行的技术路线。一是**前馈式重建**，如`MAGiSt3R`和`Instant NuRec`，追求极致的推理速度，但需要大量数据预训练或特定的模型架构。另一条是**几何/优化根基**的路线，如`G²SR`和`RoGS`，通过解析几何或结构感知的优化策略，追求更高的几何精度和更低的计算/内存成本。二者正趋于融合。
- **神经场景表示与渲染**：**3DGS**是绝对主流，但正从单一的“泼溅”向更精细化的表示进化，例如`RoGS`的2D网格高斯、`Bake It Till You Make It`的纹理图集烘焙与稀疏性优化。同时，**新维度**被引入，如`JADE-GS`结合事件相机处理动态模糊，`Volumetric Inverse Rendering`处理体渲染（Volume Rendering）的逆问题。这些工作共同推动了场景表示在动态、模糊、物理属性等复杂条件下的鲁棒性。
- **具身/机器人/AR应用**：技术路线呈现高度定制化。**自动驾驶**方面，`Instant NuRec`和`RoGS`为URBAN场景的快速在线建图和模拟提供了解决方案。**人机交互**方面，`Dynamic Manipulation Hypergraphs`和`S-squared-VLA`分别从高阶关系推理和语义空间解耦角度，研究如何让智能体理解并执行复杂的操作。**底层基础设施**方面，`Open-AoE`和`UniPhysGen`专注数据与资产供给，为上层算法提供“燃料”。

#### 值得优先阅读的论文

1.  **`G²SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction`**：本文提出的“轻量学习 + 解析几何”混合范式，代表了3DGS从纯学习转向先验驱动的关键转变。其极致的速度（高达89 FPS）和内存效率（203 MB）为在移动平台上进行实时表面重建打开了可能，是理解未来轻量化3D重建方向的重要论文。

2.  **`AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight`**：这是将视频扩散模型（Video Diffusion Transformer）用于真实世界机器人控制的代表性工作，且跨领域地实现了语言指令到连续飞行动作映射。其提出的“未来视频帧作为密集监督”的训练策略是重大创新，对整个具身智能和机器人领域具有前瞻性指导意义。

3.  **`Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency`**：该论文首次解决了辐射场重建中“无序输入”这个长期被忽视但实际中普遍存在的问题。如果能有效解决，将极大提升3DGS在用户随手拍摄、图像聚合等场景下的实用性和鲁棒性。其提出的共可见性图+聚类闭环方法也颇具工程巧思。

4.  **`JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting`**：本文巧妙地结合了事件相机（Event Camera）的互补优势，利用其微秒级运动信号辅助模糊图像的3D重建。其设计的“像素自适应路由门”和“双向闭环”机制有效融合了物理先验与学习先验，为处理快速运动场景下的高质量重建提供了新思路，是极具启发性的交叉方向。

5.  **`UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets`**：对于从事具身AI和机器人仿真的研究者而言，本文提供的系统性解决方案（从数据到模型）极具价值。它解决了现有3D资产“物理语义缺失”的关键瓶颈，提出的`UniPhysGen`模型有望成为仿真环境构建的基础设施。论文思路清晰，实用价值高。

#### 可能的研究机会

1.  **3DGS的物理属性解耦与重建**：现有工作如`Bake It Till You Make It`解耦了外观的几何与纹理，`RoGS`解耦了道路的几何与语义。但一个更大的机会是将材质的**物理属性（如粗糙度、金属度、BRDF）**与几何显式解耦，并利用神经渲染或优化方法从多视图图像中联合重建。这能直接受益于`Volumetric Inverse Rendering`的思路，但将其移植到离散的2D高斯或3D高斯表示上，有望实现真正的“物理可编辑”数字孪生。

2.  **基于“世界-动作模型”的通用操控策略生成**：`AeroAct`在四旋翼飞行器上取得了成功。一个自然的延伸是，将这种方法推广到机械臂操作等其他控制领域。可以研究如何将`AeroAct`中的未来帧监督与`Dynamic Manipulation Hypergraphs`中的高阶交互关系建模相结合，生成既能预测物理后果，又能理解复杂操作语义的精准备策略。

3.  **通信极度受限环境下的“去中心化”协同重建**：`CERPE`为多机器人协作感知提供了通信高效的位姿估计方案。结合本文中多

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-17T10:01:09-04:00
**Total number of papers:** 55
**Number of papers added in the latest update:** 14
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

#### 2026-07-16 - MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos

**Authors:** Ziren Gong, Xiaohan Li, Fabio Tosi, Ninghui Xu, Stefano Mattoccia, Jianfei Cai, Matteo Poggi
**Links:** [abs](https://arxiv.org/abs/2607.15211) - [pdf](https://arxiv.org/pdf/2607.15211)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** point map, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos
- 作者：Ziren Gong, Xiaohan Li, Fabio Tosi, Ninghui Xu, Stefano Mattoccia, Jianfei Cai, Matteo Poggi
- 出版日期：2026-07-16
- 分类：Geometry Foundation Models（主分类），3D Reconstruction & Multi-view Geometry（副分类）
- 链接：摘要页 https://arxiv.org/abs/2607.15211 | PDF https://arxiv.org/pdf/2607.15211

### 一句话总结
本文提出MAGiSt3R，一个基于多智能体（multi-agent）前馈流水线的单目RGB视频三维重建框架，能以接近10 FPS的速度同时完成重建和相机跟踪。

### 研究问题
如何从单目RGB视频中高效、准确地进行前馈式三维重建和相机跟踪，尤其是解决前馈流水线中累积的相机漂移问题？

### 核心思路/方法
1.  **基础模块**：采用来自3R系列的前馈模型处理RGB视频并回归局部点图（local point maps）。
2.  **融合模型**：提出MAGMA，在智能体内（intra-agent）和智能体间（inter-agent）两个层级上融合局部点图，以生成最终全局点图。
3.  **优化策略**：进行姿态图优化（pose graph optimization），以减轻前馈流水线中累积的相机漂移。

### 主要贡献
- 提出了一个多智能体前馈三维重建框架，实现了从单目RGB视频到全局点图的快速重建（近10 FPS）。
- 设计了MAGMA融合模型，能有效合并多智能体生成的局部点图。
- 通过姿态图优化缓解了前馈流水线中的累积相机漂移问题。
- 在合成和真实数据集上均取得了优于现有技术的重建和相机跟踪精度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  

**理由**：本文提出了一个新颖的多智能体前馈式三维重建框架，在效率（近10 FPS）和精度上均有提升，且方法思路清晰。但摘要未提供具体实验量化对比、局限性及方法细节（如智能体数量、网络结构等），因此对于需要深度复现或评估方法普适性的读者，阅读优先级可定为中等。若用户仅需了解该方向的最新进展，可考虑阅读。

</details>

<details>
<summary>Abstract</summary>

This paper presents MAGiSt3R, a multi-agent 3D reconstruction framework performing reconstruction and camera tracking for monocular RGB videos at almost 10 FPS. MAGiSt3R relies on a feed-forward model from the 3R family to process RGB videos and regress local point maps, and on a merging model, MAGMA, that combines local maps at both intra-agent and inter-agent levels to obtain the final global point map. Furthermore, MAGiSt3R performs pose graph optimization to mitigate cumulative camera drift occurring along the feed-forward pipeline. We evaluate MAGiSt3R on both synthetic and real-world datasets, demonstrating its superior reconstruction and camera tracking accuracy compared to state-of-the-art approaches.

</details>

#### 2026-07-14 - X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras

**Authors:** Heng Zhou, Shuhong Liu, Yonghao He, Bohao Zhang, Fa Fu, Chenhui Hou, Xianbao Hou, Lijun Han, Wei Sui
**Links:** [abs](https://arxiv.org/abs/2607.12993) - [pdf](https://arxiv.org/pdf/2607.12993)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras
- 作者：Heng Zhou, Shuhong Liu, Yonghao He, Bohao Zhang, Fa Fu, Chenhui Hou, Xianbao Hou, Lijun Han, Wei Sui
- 出版日期：2026-07-14
- 分类：Geometry Foundation Models（基础几何模型）; 3D Reconstruction & Multi-view Geometry（三维重建与多视图几何）
- 链接：https://arxiv.org/abs/2607.12993

### 一句话总结
X-Lens 是一个紧凑的前馈模型，通过几何感知的异构相机公式（可学习校准令牌和雅可比参数化的畸变偏置），从可变数量的鱼眼和针孔视图实时估计度量深度，在极低参数量下实现高帧率与高精度。

### 研究问题
如何从不同类型的相机（鱼眼和针孔）混合配置中实时估计度量深度，同时保证跨相机一致性和全局度量尺度。

### 核心思路/方法
1. **几何感知的异构相机公式**：包含两个关键组件。
   - **可学习校准令牌**：在鱼眼和针孔投影空间之间提供粗略对齐。
   - **雅可比参数化的畸变偏置**：注入交叉注意力中，对局部投影变化建模，促进跨相机一致性。
2. **紧凑前馈架构**：模型仅0.04B参数，运行速度高达41 FPS。
3. **端到端度量深度预测**：直接输出稠密深度及全局度量尺度，避免使用辅助重建目标造成计算和优化负担。
4. **大规模训练数据**：在多个公共数据集以及自研的OmniScene（约266K同步六视图帧、1.7M单张图像、103个室内外场景）上训练，实现跨相机泛化。

### 主要贡献
- 提出X-Lens，首个支持实时、异构相机混合输入的度量深度估计模型。
- 提出可学习校准令牌和雅可比参数化畸变偏置，有效处理鱼眼与针孔视图的几何差异。
- 在OmniScene-Full上相比最强基线将AbsRel降低25.4%，同时参数减少88.9%。
- 在常规鱼眼/针孔单设置上也达到竞争性性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作聚焦于实用且具有挑战性的异构相机混合场景（鱼眼+针孔），在保持极低参数量和实时性（41 FPS）的同时显著提升度量深度精度，并公开大规模合成数据集，对多相机感知系统研发具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We present X-lens, a compact feed-forward model for metric depth estimation from a variable number of calibrated fisheye and pinhole views. To support real-time downstream perception, X-lens is built around a geometry-aware heterogeneous camera formulation with two key components. Learnable calibration tokens provide a coarse alignment between fisheye and pinhole projective spaces, while a Jacobian-parameterized distortion bias injected into cross-attention models local projection changes and promotes cross-camera consistency, enabling robust generalization with only 0.04B parameters and up to 41 FPS. The model predicts dense depth together with a global metric scale, avoiding auxiliary reconstruction targets that increase computation and optimization complexity. To learn such cross-camera generalization at scale and depth, X-lens is trained on multiple public datasets and OmniScene, our newly released large-scale synthetic dataset containing approximately 266K synchronized six-view frames, 1.7M individual images, and 103 indoor and outdoor scenes. Extensive experiments on both real-world and synthetic indoor and outdoor datasets demonstrate superior heterogeneous-camera metric depth accuracy, reducing AbsRel by 25.4\% on OmniScene-Full over the strongest baseline while using 88.9\% fewer parameters, with competitive performance on conventional fisheye-only and pinhole-only settings.

</details>

#### 2026-07-12 - MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction

**Authors:** Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia
**Links:** [abs](https://arxiv.org/abs/2607.10792) - [pdf](https://arxiv.org/pdf/2607.10792)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** MASt3R, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction
- 作者：Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia
- 出版日期：2026-07-12
- 分类：Geometry Foundation Models (主); Neural Scene Representations & Rendering (辅)
- 链接：摘要链接 https://arxiv.org/abs/2607.10792；PDF链接 https://arxiv.org/pdf/2607.10792

### 一句话总结
MAC-Splat 提出一种基于多属性一致性损失（MAC loss）的训练框架，通过引入高质量3D对应关系作为几何锚点，显式正则化匹配高斯的空间位置、形状和外观，以解决稀疏视角重建中的几何伪影问题。

### 研究问题
从稀疏视角重建高保真3D场景时，现有可泛化3D高斯泼溅（3DGS）方法仅依赖2D光度损失监督，无法解决深度与对应关系歧义，导致几何伪影。

### 核心思路/方法
1. **骨干网络**：采用MASt3R几何骨干网络和冻结的DINOv3编码器，获取语义引导的2D对应关系，作为3D监督的几何锚点。
2. **多属性一致性损失（MAC loss）**：基于上述锚点，强制匹配高斯体在公共世界坐标系下对齐其位置、形状和外观三种属性，以正则化3D高斯属性。
3. **鲁棒性设计**：损失函数对异常值具有鲁棒性，并尊重协方差矩阵的几何结构，从而在稀疏视角条件下实现稳定训练。

### 主要贡献
- 提出直接面向3D属性一致性监督的训练框架MAC-Splat，可有效缓解稀疏视角下的几何伪影。
- 设计多属性一致性损失（MAC loss），联合正则化匹配高斯的空间、形状和外观属性。
- 在ScanNet++数据集上，MAC-Splat在重叠率等变化场景下均显著超越基线（如相较于Splatt3R，PSNR提升超4.5 dB，LPIPS降低），且在相机姿态间距增大时仍保持性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对稀疏视角下3D重建的核心难题（几何伪影），提出创新的直接3D一致性监督方法，并在公开基准上取得大幅性能提升（PSNR超4.5 dB），方法清晰且实验结果突出，对神经渲染和3DGS领域具有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing high-fidelity 3D scenes from sparse-views remains a central problem in generalizable neural rendering. Existing generalizable 3D Gaussian Splatting (3DGS) methods often exhibit geometric artifacts in sparse-view settings, since supervision based solely on 2D photometric losses cannot resolve depth and correspondence ambiguities. To address this issue, we propose MAC-Splat, a training framework built around direct 3D consistency supervision. MAC-Splat builds on the MASt3R geometric backbone and a frozen DINOv3 encoder to obtain semantically informed 2D correspondences, which serve as geometric anchors for 3D supervision. Using these anchors, we define the Multi-Attribute Consistency (MAC) loss. This objective jointly regularizes the 3D attributes of matched Gaussians, including their position, shape, and appearance, by enforcing agreement in a common world coordinate frame. The formulation is robust to outliers and respects the geometry of covariance matrices, which leads to stable training under sparse-view conditions. Experiments on ScanNet++ show that MAC-Splat outperforms strong baselines, with particularly large gains under different overlap regimes. In particular, it improves average PSNR over Splatt3R by more than 4.5 dB, reduces LPIPS, and maintains performance as the camera pose gap increases. These results indicate that a direct, multi-attribute 3D consistency objective, when combined with high-quality correspondences, is effective for addressing the ill-posed sparse-view reconstruction problem.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

#### 2026-07-15 - Human4K: A Large-Scale 4K Multi-View Mocap Dataset for Whole-Body 3D Human Reconstruction

**Authors:** Tianshun Han, Ziyu Shi, Lijian Liu, Ajian Liu, Benjia Zhou, Hugo Jair Escalante, Yanyan Liang, Sergio Escalera, Zhen Lei, Jun Wan
**Links:** [abs](https://arxiv.org/abs/2607.13646) - [pdf](https://arxiv.org/pdf/2607.13646)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** human reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Human4K: A Large-Scale 4K Multi-View Mocap Dataset for Whole-Body 3D Human Reconstruction
- 作者：Tianshun Han, Ziyu Shi, Lijian Liu, Ajian Liu, Benjia Zhou, Hugo Jair Escalante, Yanyan Liang, Sergio Escalera, Zhen Lei, Jun Wan
- 出版日期：2026-07-15
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2607.13646

### 一句话总结
本文提出了Human4K，一个包含超600万张4K多视角图像、配备动作捕捉精确SMPL-X标注的大规模全身人体重建数据集，旨在提升复杂真实场景下的3D人体重建鲁棒性。

### 研究问题
现有3D人体重建模型在最具挑战性的真实场景（如深度模糊、自遮挡、肢体关节复杂动作）中表现不佳，关键原因在于已有数据集缺乏高分辨率图像、高精度标注和多样化全身动作的组合。

### 核心思路/方法
1. **数据集构建**：使用八视角高分辨率相机系统配合专业Vicon动作捕捉设备，采集11位受试者执行复杂、高度关节化且强自遮挡的全身运动，获得超600万张4K图像。
2. **标注处理**：通过“动作重定向与精炼模块”（MRRM）处理所有序列，确保全身及四肢的精确定位。
3. **实验验证**：在标准基准上使用Human4K进行训练，结果显示全身重建性能持续提升，尤其在手、脚和深度模糊肢体构型方面表现显著。

### 主要贡献
- 提供了首个大规模、4K分辨率、多视角、带动作捕捉精确SMPX-X标注的全身人体重建数据集（Human4K），覆盖复杂全身运动。
- 使用MRRM模块实现高质量动作标注对齐。
- 实验证明该数据集能有效提升标准基准上的全身重建质量，尤其改善手脚及深度模糊肢体构型的重建效果。

### 局限性
摘要未提供足够信息。未提及数据集的潜在偏差、是否涵盖不同体型或运动模式，以及模型在旋转或极端光照下的表现等。

### 阅读优先级
**高**  
理由：该数据集直接针对当前3D人体重建中的关键瓶颈（复杂真实场景下的不稳定几何与肢体关节不精确），且提供了大规模、高分辨率、高精度标注的资源，对提升相关模型性能具有重要实践价值，适合从事人体重建、动作捕捉或多视角三维视觉的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D human reconstruction have improved overall performance, yet current models still fail in the most challenging real-world scenarios. They often produce unstable geometry, inaccurate limb articulation and unreliable predictions under depth ambiguity or self-occlusion. A key reason is that existing datasets still lack the combination of high-resolution images, high-precision annotations and diverse whole-body motions required to support robust reconstruction. To address this gap, we present Human4K, a large-scale 4K multi-view whole-body human reconstruction dataset with mocap-accurate SMPL-X annotations. Human4K contains over six million 4K images captured by an eight-view high-resolution camera system synchronized with a professional Vicon motion capture setup, covering 11 subjects performing complex, highly articulated and strongly self-occluded full-body motions. All sequences are processed by a Motion-Retargeting and Refinement Module (MRRM) to ensure precise alignment for the full body and extremities. Experimental results show that training with Human4K consistently improves whole-body reconstruction on standard benchmarks, with particularly large gains for hands, feet and depth-ambiguous limb configurations.

</details>

#### 2026-07-14 - Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements

**Authors:** Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun
**Links:** [abs](https://arxiv.org/abs/2607.12362) - [pdf](https://arxiv.org/pdf/2607.12362)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements
- 作者：Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun
- 出版日期：2026-07-14
- 分类：Dynamic / 4D Reconstruction（主分类），Neural Scene Representations & Rendering（副分类）
- 链接：摘要页 https://arxiv.org/abs/2607.12362；PDF https://arxiv.org/pdf/2607.12362

### 一句话总结
本文提出 SPIN-4DGS，通过时空位置隐式网络从显式收集的时空位置学习高斯属性，解决了现有4DGS方法在帧间大位移快速运动场景下重建失败的问题。

### 研究问题
现有4D高斯泼溅（4DGS）方法在处理快速运动且帧间位移较大的场景时，高斯属性的训练效果差，常导致快速运动物体在重建中丢失。

### 核心思路/方法
核心思路是用显式收集的时空位置替代对时间位移的建模，以避免因位移大导致的训练困难。具体方法：
1. 构建一个轻量级前馈网络，该网络从所有时空位置显式收集的输入中预测高斯属性，而非直接优化每个位置。
2. 网络基于光栅化重建损失训练，从而学习所有高斯点间的共享表征，捕获时空一致性。
3. 这避免了显式优化所有时空位置带来的巨大内存开销，同时提升了快速运动下的稳定性和质量。

### 主要贡献
1. 提出了 SPIN-4DGS 框架，能在大帧间位移的快速运动中实现更忠实的高斯泼溅。
2. 通过轻量级前馈网络预测高斯属性，降低了内存开销并保持了时空一致性。
3. 在 CMU Panoptic 数据集的高难度体育场景上，SPIN-4DGS 在 PSNR 和 SSIM 上显著优于现有方法，例如在 Basketball 场景中比最强基线 D3DGS 高出 +1.83 PSNR。

### 局限性
摘要未提供足够信息。例如，文中未讨论该方法在极端复杂场景（如严重遮挡、光照剧变）下的表现，也未提及计算开销或推理速度等具体局限性。

### 阅读优先级
高  
理由：该工作针对4D重建中快速运动这一实际痛点，提出了新颖的隐式网络方法，且在公开数据集的体育场景上取得了明显量化提升（如PSNR提升+1.83），属于动态场景重建方向的前沿进展，对相关领域研究有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent 4D Gaussian Splatting (4DGS) methods often fail under fast motion with large inter-frame displacements, where Gaussian attributes are poorly learned during training, and fast-moving objects are often lost from the reconstruction. In this work, we introduce Spatiotemporal Position Implicit Network for 4DGS, coined SPIN-4DGS, which learns Gaussian attributes from explicitly collected spatiotemporal positions rather than modeling temporal displacements, thereby enabling more faithful splatting under fast motions with large inter-frame displacements. To avoid the heavy memory overhead of explicitly optimizing attributes across all spatiotemporal positions, we instead predict them with a lightweight feed-forward network trained under a rasterization-based reconstruction loss. Consequently, SPIN-4DGS learns shared representations across Gaussians, effectively capturing spatiotemporal consistency and enabling stable high-quality Gaussian splatting even under challenging motions. Across extensive experiments, SPIN-4DGS consistently achieves higher fidelity under large displacements, with clear improvements in PSNR and SSIM on challenging sports scenes from the CMU Panoptic dataset. For example, SPIN-4DGS notably outperforms the strongest baseline, D3DGS, by achieving +1.83 higher PSNR on the Basketball scene.

</details>

#### 2026-07-12 - OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields

**Authors:** Yanqin Jiang, Tengfei Wang, Zhengwei Wang, Chenjie Cao, Junta Wu, Wenhan Luo, Weiming Hu, Jin Gao, Chunchao Guo
**Links:** [abs](https://arxiv.org/abs/2607.10840) - [pdf](https://arxiv.org/pdf/2607.10840)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 4D reconstruction, camera pose estimation, pose estimation, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields
- 作者：Yanqin Jiang, Tengfei Wang, Zhengwei Wang, Chenjie Cao, Junta Wu, Wenhan Luo, Weiming Hu, Jin Gao, Chunchao Guo
- 出版日期：2026-07-12
- 分类：Dynamic / 4D Reconstruction（主分类），3D Reconstruction & Multi-view Geometry（次分类）
- 链接：摘要页 https://arxiv.org/abs/2607.10840，PDF https://arxiv.org/pdf/2607.10840

### 一句话总结
本文提出OmniX，一种前馈式4D重建框架，通过预测稠密3D点轨迹，在大视角变化视频中实现任意视角和任意时间的动态场景重建。

### 研究问题
现有前馈式4D重建方法存在两个主要限制：一是按帧预测静态点云，忽略了前景运动；二是估计点云轨迹时仅支持小相机运动，无法在大视角变化下聚合时间观测，难以重建完整的动态场景。

### 核心思路/方法
1. **解耦动态运动建模与静态几何预测**：将运动表示从静态几何中分离，用一组紧凑的动态令牌（dynamic tokens）编码运动。
2. **利用3D运动的稀疏和低秩结构**：通过动态令牌为所有图像的所有像素生成轨迹场，同时高效保持全局交互。
3. **自动数据引擎与大规模数据集**：构建基于UE5的自动4D数据生成引擎，产出包含80K场景和1.28M多视角视频的全几何标注数据集，用于训练。

### 主要贡献
- 提出OmniX框架，能够从大相机运动视频中预测稠密3D点轨迹，实现任意视角和任意时间的4D重建。
- 提出解耦的动态运动建模方法，利用稀疏和低秩运动结构生成轨迹场。
- 构建了大规模自动生成的4D数据集（80K场景，1.28M多视角视频），带有完整几何标注。
- 在稠密3D点轨迹预测和3D点跟踪任务上达到当前最优性能，在视频深度估计和相机位姿估计上也获得有竞争力的结果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对前馈式4D重建在大视角变化下的核心局限提出解决方案，并构建了大规模训练数据，在多项任务上取得最优或接近最优性能。对于关注动态3D重建、4D场景理解及新视角合成的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Previous feed-forward 4D reconstruction methods either predict per-frame static point clouds, ignoring foreground motion, or estimate point cloud trajectories while being limited to small camera motions. This restricts their ability to aggregate observations over time and reconstruct complete dynamic scenes under large viewpoint changes. To address this limitation, we propose OmniX, a feed-forward 4D reconstruction framework that predicts dense 3D point trajectories for every pixel from videos with large camera motion. OmniX decouples dynamic motion modeling from static geometry prediction and represents motion using a compact set of dynamic tokens. By leveraging the sparse and low-rank structure of 3D motion, these tokens generate trajectory fields for all pixels across all images while efficiently preserving global interactions. To facilitate training, we further build an automatic UE5-based 4D data engine and introduce a large-scale dataset containing 80K scenes and 1.28M multi-view videos with full geometric annotations. OmniX achieves state-of-the-art performance on dense 3D point trajectory prediction and 3D point tracking, while also demonstrating competitive results on video depth estimation and camera pose estimation.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-16 - Communication-Efficient Relative Pose Estimation with Vision Foundation Models for Ephemeral Collaborative Perception

**Authors:** Qihang Li, Jo-Hao Huang, Jiewen Liu, Suyoung Kang, Hao Zhang, Peng Gao
**Links:** [abs](https://arxiv.org/abs/2607.14539) - [pdf](https://arxiv.org/pdf/2607.14539)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Communication-Efficient Relative Pose Estimation with Vision Foundation Models for Ephemeral Collaborative Perception
- 作者：Qihang Li, Jo-Hao Huang, Jiewen Liu, Suyoung Kang, Hao Zhang, Peng Gao
- 出版日期：2026-07-16
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.14539 | PDF: https://arxiv.org/pdf/2607.14539

### 一句话总结
提出CERPE系统框架，利用视觉基础模型实现通信高效的相对位姿估计，专为短暂协作感知场景设计。

### 研究问题
如何解决多机器人系统在短暂相遇、有限带宽、间歇性或缺失视觉重叠条件下的通信高效相对位姿估计问题。

### 核心思路/方法
1. 使用连续共享的固定大小描述符（而非原始观测数据）进行事件触发式的原始图像请求，减少通信冗余。
2. 针对无视觉重叠场景，通过度量的尺度化自运动传播机器人间相对位姿，维持估计连续性。
3. 整体框架协调视觉基础模型，联合估计自运动与机器人间相对位姿。

### 主要贡献
1. 提出CERPE系统框架，在短暂协作感知中显著降通信开销。
2. 设计独立于位姿估计的固定大小描述符门控机制，实现事件触发的原始图像传输。
3. 通过自运动传播处理非重叠相遇场景，保持相对位姿估计稳定性。
4. 仿真与真实机器人实验表明CERPE在6-DoF相对位姿估计上优于所选基线方法。

### 局限性
摘要未提供实验细节，因此无法分析具体局限性，如是否依赖特定视觉基础模型、对极端遮挡或快速运动的鲁棒性、实际通信带宽节省比例等。（摘要未提供足够信息）

### 阅读优先级
高
理由：该研究针对多机器人协作感知中的通信与视觉重叠瓶颈，提出实用框架，且结合了视觉基础模型的近期进展；实验涵盖仿真与真实场景，具有应用潜力。对于从事多机器人系统或协作感知的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Relative pose estimation is a fundamental capability for collaborative perception and coordination in multi-robot systems. However, robots encountering each other in real-world environments often operate in short interaction windows and must operate under limited communication bandwidth with intermittent or missing visual overlap caused by occlusions or limited fields of view. Existing approaches typically rely on global reference frames, assume sustained view overlap, or incur prohibitive communication costs, thereby limiting their applicability to ephemeral collaborative perception. To address these challenges, we introduce communication-efficient relative pose estimation (CERPE), a system-level framework that coordinates vision foundation models to jointly estimate ego-motion and inter-robot relative pose. CERPE reduces unnecessary raw-observation exchange by using continuously shared fixed-size descriptors to gate event-triggered raw-image requests independently of pose estimation. Non-overlapping encounters are handled by propagating inter-robot relative poses through metrically scaled ego-motion, thus maintaining relative pose estimates even in the absence of visual overlap. Experiments in simulation and real-world robots show that CERPE improves 6-DoF relative pose estimation over selected baselines in ephemeral collaborative perception.

</details>

#### 2026-07-16 - G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction

**Authors:** Dasong Gao, Vivienne Sze, Sertac Karaman
**Links:** [abs](https://arxiv.org/abs/2607.14470) - [pdf](https://arxiv.org/pdf/2607.14470)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G²SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction
- 作者：Dasong Gao, Vivienne Sze, Sertac Karaman
- 出版日期：2026-07-16
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.14470

### 一句话总结
G²SR提出一种结合轻量级神经网络前端与解析几何后端的混合方法，用于从少量视角的RGB图像中快速、内存高效地进行高斯散点表面重建，在多个数据集上达到或超越现有方法精度，并大幅降低计算开销。

### 研究问题
如何从少量视角的RGB图像中，实现快速、几何精确且内存占用小的3D高斯散点表面重建，以减少“浮动伪影”并提升在线移动平台的适用性。

### 核心思路/方法
该方法将任务分解为两步：1）使用轻量级神经网络前端检测并跟踪图像平面上的2D高斯散点对应关系；2）利用解析几何后端，基于多视角几何原理将这些2D对应点三角化重建为公制尺度的3D高斯散点。整个流程避免了传统端到端方法中大型Transformer网络的使用。

### 主要贡献
1. 提出G²SR框架，利用多视角几何中的解析关系从2D对应点直接推得3D散点，降低了问题的病态性。
2. 在ScanNet、Replica和DTU数据集上，几何精度匹配或超越当前最先进的端到端方法。
3. 在2-3视角、384×512分辨率输入下，实现每秒69-89次重建速度，且GPU内存仅需203 MB（较对比方法低5-107倍），显著提升内存效率和速度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该论文针对少视角表面重建中的实时性和内存限制问题，提出了一种混合几何与轻量学习的创新方案，实验效率指标突出（速度提升与内存降低数十倍），且与现有方法精度相当，对移动机器人在线3D重建具有实际参考价值。

</details>

<details>
<summary>Abstract</summary>

Few-view surface reconstruction recovers the visible surfaces of a scene from a few posed RGB images, providing the 3D models that robots need to explore and interact online. On mobile platforms, the reconstruction must be fast and geometrically accurate while keeping a small memory footprint to ensure safe and efficient operation. 3D Gaussian Splatting (3DGS) offers a high-fidelity scene representation, but building it from a few views is ill-posed, as many distinct surfaces reproduce the same images, making traditional photometric methods prone to "floater" artifacts. End-to-end methods resolve the ambiguity by regressing splats with large, usually Transformer-based, networks that require heavy compute and memory while generalizing poorly to new scenes. We propose G2SR, which exploits a well-posed core of the task: given cross-view 2D splat correspondences, 3D splats follow analytically from multi-view geometry. G2SR employs a lightweight neural frontend to detect and track 2D Gaussian splats on the image plane and an analytic backend to triangulate each into a metric-scale 3D splat. On ScanNet, Replica, and DTU, G2SR matches or exceeds the geometric accuracy of state-of-the-art end-to-end methods while running at 69-89 reconstructions per second within 203 MB of GPU memory (5-107x less) for 2- and 3-view inputs at 384 x 512 resolution, offering a practical path to online Gaussian-based surface reconstruction.

</details>

#### 2026-07-15 - COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction

**Authors:** Phu Pham, Damon Conover, Aniket Bera
**Links:** [abs](https://arxiv.org/abs/2607.13524) - [pdf](https://arxiv.org/pdf/2607.13524)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction
- 作者：Phu Pham, Damon Conover, Aniket Bera
- 出版日期：2026-07-15
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2607.13524) | [PDF](https://arxiv.org/pdf/2607.13524)

### 一句话总结
本文提出COLMAR，一个基于共享策略学习的多智能体协同视点规划框架，通过重建感知目标优化主动三维重建的质量与覆盖。

### 研究问题
多智能体主动三维重建中，因协调不足（如冗余观测、空间聚类）导致重建质量下降，如何设计有效的协同视点政策以在有限传感预算下提升重建精度与覆盖。

### 核心思路/方法
1. 将视点分配建模为基于地图中心观测的**共享策略优化**问题。
2. 引入**重建感知目标函数**，包含重叠感知覆盖、团队级新区域发现、碰撞安全探索三项指标。
3. 利用增量重建更新生成密集反馈，将探索行为与下游几何质量对齐。
4. 采用参数共享的**近端策略优化（PPO）**训练策略，部署时各智能体独立执行动作，基于融合团队地图决策，无需智能体间消息传递。
5. 选定视点通过**3D高斯泼溅（3DGS）**重建，实现高保真光度评估。

### 主要贡献
- 提出多智能体协同视点学习框架COLMAR，通过重建感知目标优化协调策略。
- 设计无需在线通信的共享策略机制，降低部署复杂度。
- 在GLEAM和Replica数据集上，相比启发式和非协同基线，在相同传感预算下实现高达**54%的重建精度提升**和**49%的覆盖增加**。

### 局限性
摘要未提供足够信息（如失败场景、计算开销、泛化至复杂场景的瓶颈等）。

### 阅读优先级
**高**  
理由：该工作针对多智能体主动三维重建中的关键协调难题，提出了结合强化学习与3DGS的新框架，实验提升显著（精度/覆盖均超50%），且属于近期的前沿方向（2026年发表）。适合关注多机器人重建、视点规划及神经渲染的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Active 3D reconstruction requires selecting informative viewpoints under limited sensing budgets. In multi-agent settings, coordination inefficiencies such as redundant observations and spatial clustering can significantly reduce reconstruction quality. We present COLMAR, a cooperative view policy learning framework for multi-agent active 3D reconstruction. COLMAR formulates viewpoint allocation as a shared policy optimization over map-centric observations and introduces a reconstruction-aware objective that promotes overlap-aware coverage, team-level discovery, and collision-safe exploration. Dense feedback derived from incremental reconstruction updates aligns exploration behavior with downstream geometric quality. The policy is trained using parameter-sharing Proximal Policy Optimization (PPO) with independent per-agent action selection at deployment, conditioned on a fused team map and without inter-agent message passing for decision making. Selected viewpoints are then reconstructed with 3D Gaussian Splatting (3DGS) for high-fidelity photometric evaluation. Experiments on GLEAM and Replica demonstrate consistent improvements over heuristic and non-cooperative baselines, achieving up to 54% higher reconstruction accuracy and 49% greater coverage under matched sensing budgets.

</details>

#### 2026-07-15 - CASA-SDF: Curriculum-Aware Spatial Adaptation with Curvature-Guided Density for Neural Implicit Surface Reconstruction

**Authors:** Lei Yang, Weiqing Li, Zhiyong Su, Liang Xiao
**Links:** [abs](https://arxiv.org/abs/2607.13492) - [pdf](https://arxiv.org/pdf/2607.13492)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CASA-SDF: Curriculum-Aware Spatial Adaptation with Curvature-Guided Density for Neural Implicit Surface Reconstruction
- 作者：Lei Yang, Weiqing Li, Zhiyong Su, Liang Xiao
- 出版日期：2026-07-15
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.13492 | PDF: https://arxiv.org/pdf/2607.13492

### 一句话总结
本文提出CASA-SDF框架，通过课程感知的空间自适应监督和曲率引导的密度变换，同时提升室内场景中平面区域的平滑性和薄结构的细节重建精度。

### 研究问题
室内场景由于几何异质性（大面积无纹理平面与精细薄结构并存），现有隐式神经表示方法难以同时实现平面平滑（避免高频伪影）和薄结构细节保留（克服MLP的光谱偏置），通常导致过平滑或伪影。

### 核心思路/方法
1. **混合空间自适应不确定度退火（SAUA）**：融合语义和光度不确定度，构建像素级课程，在训练初期抑制不可靠的单目先验监督，保留可靠区域的正则化，后期允许数据驱动的光度优化。
2. **曲率感知局部自适应密度变换（CALADT）**：通过曲率代理逐步调节SDF到密度的映射锐度，增强对薄结构的表示能力，同时不破坏平面稳定性。

### 主要贡献
- 提出了统一框架CASA-SDF，通过监督和表示能力的空间自适应互补适配，解决室内重建中几何异质性的挑战。
- 设计SAUA策略，基于像素级不确定度实现单目先验的课程式监督，平衡可靠性和灵活性。
- 设计CALADT机制，利用曲率代理动态调整密度变换锐度，改善高频结构的表示。
- 在基准室内数据集上验证，相比现有方法提高了表面完整性和高频结构细节恢复，且未牺牲平面稳定性。

### 局限性
摘要未提供足够信息，例如对极端噪声/缺失区域的鲁棒性、计算开销或与其他方法的定量对比细节。

### 阅读优先级
高
- 理由：该工作直接针对室内场景重建中的核心难点（平面与薄结构平衡），提出创新的监督和表示适应机制（SAUA和CALADT），实验证明有显著提升。对于从事3D重建、隐式表示或室内场景理解的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Neural implicit representations have emerged as a powerful paradigm for 3D reconstruction. However, high-fidelity indoor surface reconstruction remains a significant challenge, primarily due to the pronounced \emph{geometric heterogeneity} of indoor scenes. Large texture-less planar regions typically require stronger regularization to suppress high-frequency artifacts, while thin structures demand sharper, more adaptive representations to mitigate the spectral bias of multi-layer perceptrons (MLPs) and prevent over-smoothing. Existing approaches often rely on spatially indiscriminate prior supervision and a scene-global SDF-to-density transformation, which constrains their ability to balance planar smoothness and detail preservation. In this paper, we propose CASA-SDF (Curriculum-Aware Spatial Adaptation for SDF), a unified framework that addresses this challenge via complementary adaptations of supervision and representation capacity. Specifically, Hybrid Spatially-Adaptive Uncertainty Annealing (SAUA) fuses semantic and photometric uncertainties to construct a pixel-wise curriculum for monocular prior supervision. This strategy maintains regularization in reliable regions while attenuating unreliable supervision early in training to enable data-driven photometric refinement. Meanwhile, Curvature-Aware Locally Adaptive Density Transformation (CALADT) progressively modulates the sharpness of the SDF-to-density mapping via a curvature proxy to enhance the representation of thin structures. Extensive experiments on benchmark indoor datasets demonstrate that CASA-SDF improves surface completeness and detail recovery on high-frequency structures, without compromising the stability of planar surfaces.

</details>

#### 2026-07-15 - Topology-Agnostic Mesh Reconstruction of Deformable Objects from Sparse Touch

**Authors:** Everest Yang
**Links:** [abs](https://arxiv.org/abs/2607.13479) - [pdf](https://arxiv.org/pdf/2607.13479)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Topology-Agnostic Mesh Reconstruction of Deformable Objects from Sparse Touch
- 作者：Everest Yang
- 出版日期：2026-07-15T06:17:35Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.13479

### 一句话总结
论文提出一种拓扑无关的单一估计器，仅通过少量触觉信号（无视觉）即可重建可变形物体的完整网格，并利用深度集成不确定性指导触觉采样位置以降低重建误差。

### 研究问题
如何在无视觉条件下（如黑暗、遮挡等场景），仅依赖稀疏的触觉接触点重建可变形物体的完整三维网格形状，并优化触觉采样策略以提升重建精度。

### 核心思路/方法
- 使用**单一置换不变交叉注意力架构**，统一处理1D绳索、2D布料和3D体积软体三种拓扑结构，无需针对不同拓扑分别设计模型。
- 训练**深度集成估计器**，从少量触觉输入直接输出物体完整网格，并产生不确定性估计。
- 利用不确定性估计指导下一次触觉采样位置（主动触觉策略），在给定触觉预算下降低误差。

### 主要贡献
- 提出第一个拓扑无关的稀疏触觉网格重建方法，单一架构适用于绳索、布料、体积软体。
- 相比非学习的几何网格补全和高斯过程曲面基线，重建误差降低约三分之二。
- 基于深度集成的不确定性主动采样策略在低预算下优于随机触摸和高斯过程主动基线，尤其在自遮挡和误差尾部分表现更明显。
- 当视觉可用时，触觉采样位置影响不大，凸显无视觉场景的研究价值。

### 局限性
摘要未提供足够信息（如对高度自变形、多物体交互或真实物理接触数据的测试结果，以及计算复杂度等）。

### 阅读优先级
**中**：该工作针对无视觉环境下的可变形物体重建问题，方法新颖（拓扑无关、主动触觉），但领域较为专精，适合从事触觉感知、机器人操作或非刚性重建的研究者阅读。对于通用3D重建社区，参考价值相对有限。

</details>

<details>
<summary>Abstract</summary>

Estimating the full shape of a deformable object is especially challenging when vision is unavailable: in the dark, inside an opaque bag, behind the manipulating hand, or under heavy self-occlusion. Touch is the natural sensor in these settings, but touches are sparse and local. We present a single topology-agnostic estimator that reconstructs the full mesh of a deformable object from only a few touches and no vision, using one permutation-invariant cross-attention architecture that handles a 1D rope, a 2D cloth, and a 3D volumetric soft body. The learned estimator reduces reconstruction error by roughly two-thirds relative to non-learned geometric mesh completion and a Gaussian-process surface baseline, and it outperforms a simpler global-pool set encoder, with the gap growing as more touches are observed. We then show that the estimator's deep-ensemble uncertainty can be used to learn where to touch next, which lowers error further and beats both random touching and a Gaussian-process active baseline at sparse budgets. This gain is modest on average but grows with self-occlusion and on the error tail. When vision is also available, where to touch barely matters, motivating the vision-free setting we study.

</details>

#### 2026-07-15 - DreamSat-Pose: Spacecraft Pose Estimation from Single-View 3D Reconstructions and Learned 2D-3D Feature Matching

**Authors:** Josiane Uwumukiza, Jocelyn Zhao, Giovanni Lavezzi, Giacomo Battaglia, Paolo Panicucci, Minduli C. Wijayatunga, Victor Rodriguez-Fernandez, Richard Linares
**Links:** [abs](https://arxiv.org/abs/2607.13449) - [pdf](https://arxiv.org/pdf/2607.13449)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DreamSat-Pose: Spacecraft Pose Estimation from Single-View 3D Reconstructions and Learned 2D-3D Feature Matching
- 作者：Josiane Uwumukiza, Jocelyn Zhao, Giovanni Lavezzi, Giacomo Battaglia, Paolo Panicucci, Minduli C. Wijayatunga, Victor Rodriguez-Fernandez, Richard Linares
- 出版日期：2026-07-15T05:12:48Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.13449

### 一句话总结
本文提出DreamSat-Pose框架，通过单张图像重建未知航天器的3D形状模型并学习2D-3D对应关系，实现6自由度姿态估计，在SPE3R数据集上达到0.157度的平均指向误差。

### 研究问题
如何在未知目标航天器的情况下，通过单张图像同时实现目标三维形状重建和准确的6自由度姿态估计。

### 核心思路/方法
1. **单视图三维重建**：首先从单张输入图像重建目标的3D形状模型（点云）。  
2. **特征提取与匹配**：使用冻结的DINOv3视觉Transformer提取图像特征，用可训练的动态图卷积神经网络（DGCNN）编码器从重建点云中提取几何特征。  
3. **双流Transformer匹配器**：通过交替自注意力和交叉注意力机制精炼描述符，生成软对应关系。  
4. **姿态恢复**：将软对应关系输入Perspective-n-Point求解器，计算最终6自由度姿态。

### 主要贡献
1. 提出一个端到端框架，联合实现未知航天器的单视图三维重建与6自由度姿态估计。  
2. 设计双流Transformer匹配器，通过交替注意力机制实现2D-3D特征匹配。  
3. 在SPE3R数据集上验证了有效性，仅使用单张图像和重建几何即可达到0.157度平均指向误差，展现了良好的泛化能力。

### 局限性
摘要未提供足够信息：未提及具体失败案例、计算复杂度、对遮挡或光照变化的鲁棒性分析，以及重建几何质量对姿态估计精度的直接影响。

### 阅读优先级
**高**。理由：该研究针对航天器自主交会中的关键问题（未知目标形状与姿态联合估计），方法设计新颖（融合视觉Transformer、图神经网络和双流匹配器），且实验指标（0.157度指向误差）具有吸引力，对3D重建与姿态估计领域具有参考价值。

</details>

<details>
<summary>Abstract</summary>

6-DoF pose estimation is a critical task in autonomous rendezvous and proximity operations. In the case of an unknown target, this task becomes challenging as it shall be paired with the reconstruction of the target shape model. In this article, we propose a novel framework for single-shot shape and pose estimation of unknown spacecraft objects. Given a single image, we first reconstruct a 3D shape model of the target, then estimate the relative six-degrees-of-freedom pose by learning dense 2D-3D correspondences. The image features are extracted using a frozen DINOv3 vision transformer, while the geometric features are computed from the reconstructed point cloud using a trainable dynamic graph convolutional neural network encoder. A dual-stream transformer matcher refines descriptors through alternating self- and cross-attention, producing soft correspondences that are passed to a Perspective-$n$-Point solver for pose recovery. We evaluate the method on the SPE3R dataset and consider FoundationPose as a representative baseline for current state-of-the-art capabilities. Results show reliable pose estimates achieving 0.157 degrees mean pointing error using only a single image and reconstructed geometry, demonstrating strong generalization to unseen spacecraft.

</details>

#### 2026-07-14 - ARDepth: Auto-regressive Monocular Depth Estimation with Progressive Visual Conditioning

**Authors:** Zijie Wang, Wei Zhang, Weiming Zhang, Xiao Tan, Weikai Chen, Xiaoxu Li, Guanbin Li
**Links:** [abs](https://arxiv.org/abs/2607.12433) - [pdf](https://arxiv.org/pdf/2607.12433)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ARDepth: Auto-regressive Monocular Depth Estimation with Progressive Visual Conditioning
- 作者：Zijie Wang, Wei Zhang, Weiming Zhang, Xiao Tan, Weikai Chen, Xiaoxu Li, Guanbin Li
- 出版日期：2026-07-14
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[Abstract](https://arxiv.org/abs/2607.12433) | [PDF](https://arxiv.org/pdf/2607.12433)

### 一句话总结
提出ARDepth方法，将单目深度估计重构为一种跨空间尺度的自回归生成过程，通过渐进式视觉条件注入和语义引导，在保持全局结构一致性的同时捕捉细粒度局部细节。

### 研究问题
现有扩散模型进行单目深度估计时，通常假设深度可通过全局迭代去噪恢复为平滑场，但这种方法未能显式建模场景几何的逐段平滑性和跨尺度的层次化组织特性。

### 核心思路/方法
1. 将深度估计建模为结构化自回归生成：随着空间分辨率增加，逐步构建深度表示，而非通过全局细化恢复深度。
2. Scale-Progressive Conditioning (SPC)：在每一个生成阶段注入多尺度视觉特征。
3. Semantic-Aware Guidance (SAG)：提供场景级语义先验，增强全局结构一致性。

### 主要贡献
1. 提出ARDepth，一种将单目深度估计形式化为结构化的自回归生成的新范式。
2. 设计渐进式视觉条件注入机制（SPC）和语义感知引导机制（SAG），分别用于多尺度特征融合和全局结构约束。
3. 实验表明该方法在保持跨尺度结构一致的深度预测方面具有强性能，验证了自回归生成作为几何建模替代范式的潜力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作提出了单目深度估计的新范式（自回归生成替代扩散模型），并设计了针对性的条件注入和引导模块，对几何建模方法创新有参考价值。

</details>

<details>
<summary>Abstract</summary>

Diffusion models have recently become the dominant paradigm for monocular depth estimation (MDE). However, they implicitly assume that depth can be recovered as a globally smooth field through iterative denoising, which does not explicitly reflect the piecewise and scale-dependent organization of scene geometry. In practice, geometric structure emerges progressively across spatial scales, where coarse layout, surfaces, and boundaries are constructed in a hierarchical manner. Motivated by this observation, we introduce ARDepth, which formulates depth estimation as structured auto-regressive generation. Instead of recovering depth through global refinement, ARDepth progressively constructs depth representations as spatial resolution increases. To support this generative process, we introduce Scale-Progressive Conditioning (SPC) to inject multi-scale visual features at each generation stage, and Semantic-Aware Guidance (SAG) to provide scene-level semantic priors that enhance global structural consistency. Together, these designs enable the model to capture fine-grained local details while maintaining coherent global geometry. Empirical results demonstrate that our approach achieves strong performance and produces structurally consistent depth predictions across scales, validating auto-regressive generation as a promising alternative paradigm for geometric modeling.

</details>

#### 2026-07-14 - DiffRadar: Differentiable Physics-Aware Radar SLAM with Gaussian Fields

**Authors:** Gaurav Bagwe, Xiaoyong Yuan, Yongji Wu, Lan Zhang
**Links:** [abs](https://arxiv.org/abs/2607.12265) - [pdf](https://arxiv.org/pdf/2607.12265)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, pose estimation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DiffRadar: Differentiable Physics-Aware Radar SLAM with Gaussian Fields
- 作者：Gaurav Bagwe, Xiaoyong Yuan, Yongji Wu, Lan Zhang
- 出版日期：2026-07-14
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.12265

### 一句话总结
DiffRadar 是一种利用可微分高斯场建模雷达观测的实时SLAM系统，通过联合优化位姿与场景结构，在多种恶劣条件下实现了比传统方法更稳定、更一致的轨迹和地图重建。

### 研究问题
现有雷达SLAM系统通常对离散化的雷达热图进行扫描匹配，破坏了几何连续性且无法捕捉关键的雷达感知特性（如多普勒效应），导致在特征匮乏或动态环境中位姿估计不稳定、地图质量下降。

### 核心思路/方法
- 使用各向异性高斯基元表示场景，并通过可微分的雷达前向模型在距离-方位角和多普勒-方位角空间渲染雷达测量值。
- 将雷达观测建模为可微分的、物理感知的高斯场，而非离散扫描，从而实现对机器人位姿和场景结构的联合优化。

### 主要贡献
- 提出了一种将雷达观测直接建模为可微分高斯场的SLAM方法，避免了离散化带来的几何断裂。
- 在商用FMCW雷达硬件上实现，并在Radarize基准测试和自建压力测试集上验证。
- 在基准测试中大幅降低了轨迹误差（尤其在特征匮乏的走廊运动中），地图一致性提升超过一倍，同时保持实时性能（70 FPS）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。
理由：该方法在雷达SLAM这一实际应用方向（无人车、移动机器人）中提出了新颖的可微分高斯场建模思路，且在极端场景下显著提升了鲁棒性和一致性，同时保持了实时性，具有较高的技术价值和潜在影响力。

</details>

<details>
<summary>Abstract</summary>

Radar sensing is increasingly used in mobile systems because it operates reliably under poor lighting, adverse weather, and privacy-sensitive settings where cameras and LiDAR often fail. However, most existing radar SLAM systems estimate motion through scan matching on discretized radar heatmaps, which breaks geometric continuity and fails to capture key radar sensing properties, often leading to unstable pose estimation and degraded mapping in regenerate or dynamically changing environments. We present DiffRadar, a real-time radar SLAM system that models radar observations as a differentiable, physics-aware Gaussian field rather than discrete scans. DiffRadar represents the scene as anisotropic Gaussian primitives and renders radar measurements in range-azimuth and Doppler-azimuth spaces through a differentiable radar forward model, enabling joint optimization of robot pose and scene structure directly from radar measurements. We implement DiffRadar on commodity FMCW radar hardware and evaluate it on both the public Radarize benchmark and a controlled stress-test suite that targets common radar SLAM failure modes, including corridor degeneracy, motion regime transitions, dynamic clutter, and long-horizon loop closures. DiffRadar achieves substantial reductions in trajectory error on the benchmark, with especially large gains under feature-poor corridor motion, while more than doubling map consistency and maintaining real-time performance at 70 FPS. These results show that modeling radar observations directly in the signal domain enables substantially more robust and consistent radar-only SLAM for mobile platforms.

</details>

#### 2026-07-13 - IBPA: Real-time Free-form Manifold Mesh Reconstruction via Incremental Ball Pivoting with Integrated Hole Detection

**Authors:** Mauhing Yip, Mohit Singh, Kostas Alexis, Christian Schellewald, Annette Stahl
**Links:** [abs](https://arxiv.org/abs/2607.11627) - [pdf](https://arxiv.org/pdf/2607.11627)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction, surface reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IBPA: Real-time Free-form Manifold Mesh Reconstruction via Incremental Ball Pivoting with Integrated Hole Detection
- 作者：Mauhing Yip, Mohit Singh, Kostas Alexis, Christian Schellewald, Annette Stahl
- 出版日期：2026-07-13T14:45:46Z
- 分类：3D Reconstruction & Multi-view Geometry（主要类别）
- 链接：[摘要](https://arxiv.org/abs/2607.11627) | [PDF](https://arxiv.org/pdf/2607.11627)

### 一句话总结
本文提出增量式球体旋转算法（IBPA），一种能够在水下机器人实时获取点云数据时，逐步构建无需预定义结构假设的自由形式流形网格，并集成孔洞检测功能的方法。

### 研究问题
针对水下机器人（ROV/AUV）作业中，传统方法（如数字地形模型DTM）无法表达悬垂、垂直结构等复杂拓扑，且现有增量重建方法（如DTM）表达能力有限的问题，文中提出了如何实时、增量地重建自由形式流形网格并检测不完整区域的研究问题。

### 核心思路/方法
- 将原始球体旋转算法（BPA）改造为增量版本（IBPA），使其能实时处理流式点云数据，无需依赖点云重叠或分布假设。
- 方法逐块构建可定向流形网格，并集成孔洞检测机制，以识别并高亮显示未完全重建的网格区域。

### 主要贡献
1. 提出IBPA算法，实现从流式点云中增量式构建自由形式流形网格，支持复杂表面拓扑（如悬垂、垂直结构）。
2. 集成孔洞检测机制，可视化标识不完整网格区域，帮助操作者实时感知覆盖质量。
3. 提供了参考实现的源代码（开源链接见摘要），便于复现和比较。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：论文针对水下机器人实时3D重建的实际工程问题，提出了一个增量式的自由形式网格重建方法，并集成了孔洞检测功能。方法新颖（改进经典BPA），且开源实现，对于从事实时3D重建、水下导航测绘或点云处理的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Both Remotely Operated underwater Vehicles (ROVs) and Autonomous Underwater Vehicles (AUVs) are frequently deployed to acquire geometric bathymetric data. However, it is often discovered post-survey that the acquired data coverage is incomplete. Given the high operational cost associated with underwater deployments, it is essential to incrementally visualize surface coverage in real-time to support informed decision-making by both the operators of ROVs and the AUVs during data collection. In addition, traditional incremental surface reconstruction methods, such as Digital Terrain Models (DTMs), are inherently limited in expressiveness: they represent surfaces as height fields, allows only one elevation value per $(x, y)$ coordinate and thus cannot capture overhangs or vertical structures. To overcome these limitations, we adapt the original Ball Pivoting Algorithm (BPA) into an incremental, real-time, and free-form surface reconstruction method, referred to as Incremental BPA (IBPA). Our method incrementally constructs an orientable, manifold mesh from streaming point cloud data without imposing assumptions regarding point cloud overlap or spatial distribution. Furthermore, we introduce a hole detection mechanism that identifies and highlights incomplete mesh regions. Compared to existing approaches, our method supports more complex surface topologies without prior structural assumptions. The source code of our reference implementation is available: https://github.com/Mauhing/Incremental-BPA

</details>

#### 2026-07-13 - SalientGS: Unified SfM-to-3DGS with Importance-Guided MCMC Gaussian Allocation

**Authors:** Tianyu Xiong, Rui Li, Suning Ge, Jiaqi Yang
**Links:** [abs](https://arxiv.org/abs/2607.11285) - [pdf](https://arxiv.org/pdf/2607.11285)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, SfM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SalientGS: Unified SfM-to-3DGS with Importance-Guided MCMC Gaussian Allocation
- 作者：Tianyu Xiong, Rui Li, Suning Ge, Jiaqi Yang
- 出版日期：2026-07-13
- 分类：3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
- 链接：摘要URL (https://arxiv.org/abs/2607.11285), PDF (https://arxiv.org/pdf/2607.11285)

### 一句话总结
SalientGS 提出了一种基于重要性引导的马尔可夫链蒙特卡洛（MCMC）高斯分布分配方法，将传统的结构运动恢复（SfM）和3D高斯泼溅（3DGS）过程统一为端到端管道，在15分钟内实现高质量3D场景重建。

### 研究问题
从无序图像进行3D场景重建时，传统方法受限于昂贵的SfM预处理和冻结的位姿接口，导致流程割裂且效率低下。本文旨在解决这一瓶颈，实现SfM与3DGS的端到端统一。

### 核心思路/方法
核心方法是重要性引导的MCMC高斯分布分配。其流程为：
1. **聚合多视图残差**：计算每个高斯体的欠拟合和冗余信号。
2. **定义重要性加权采样分布**：基于上述信号，构建平滑的重要性采样分布，倾向于引导高斯体的新生（birth）和重定位（relocation）到欠拟合区域。
3. **重新分配容量**：在保持随机梯度朗之万动力学（SGLD）不变的前提下，将高斯体从拟合良好的区域重新分配至需要更多细节的区域。

### 主要贡献
1. 提出了**统一的SfM-to-3DGS端到端管道**，简化了3D重建流程。
2. 设计了**重要性引导的MCMC高斯分配机制**，通过聚合多视图残差自动识别并修复欠拟合区域，同时减少冗余高斯体。
3. 实验表明，该方法能够在**15分钟内**完成端到端重建，并达到**最先进的感知质量**（通过LPIPS等指标验证）。

### 局限性
摘要未提供充分信息，仅提到附录中包含了失败案例的分析，但未在摘要中明确列出具体的局限性或失败模式。

### 阅读优先级
**高**  
理由：该方法提出了一个创新的统一框架（融合SfM和3DGS），并引入了一种新的重要性引导分配机制，直接解决了该领域内由SfM预处理造成的效率瓶颈。实验在感知质量上达到先进水平，且代码已开源，对从事3D重建、神经渲染的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing 3D scenes from unordered images remains bottlenecked by expensive Structure-from-Motion (SfM) preprocessing and frozen pose interfaces. We present SalientGS, a unified SfM-to-3D Gaussian Splatting (3DGS) pipeline. Its central contribution is importance-guided Markov Chain Monte Carlo (MCMC) Gaussian allocation, which aggregates multi-view residuals into per-Gaussian underfit and redundancy signals. These signals define a smooth importance-weighted sampling distribution that biases both birth and relocation toward underfit regions. This reallocates capacity from well-fit areas without altering the underlying stochastic gradient Langevin dynamics (SGLD). SalientGS achieves end-to-end reconstruction in 15 minutes with state-of-the-art perceptual quality. The supplementary material provides dedicated sections for Per-Scene Qualitative Comparisons and Per-Image Learned Perceptual Image Patch Similarity (LPIPS) Analysis, including failure cases. Code and evaluation scripts are available at https://github.com/Six-Bit-TX/SalientGS.

</details>

#### 2026-07-13 - GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors

**Authors:** Ruilan Gao, Letian Jin, Yu Zhang
**Links:** [abs](https://arxiv.org/abs/2607.11184) - [pdf](https://arxiv.org/pdf/2607.11184)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** SLAM, dense reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors
- 作者：Ruilan Gao, Letian Jin, Yu Zhang
- 出版日期：2026-07-13
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：abstract_url: https://arxiv.org/abs/2607.11184; pdf_url: https://arxiv.org/pdf/2607.11184

### 一句话总结
GeoGS-SLAM提出一种结合3D高斯溅射（3DGS）与学习几何先验的单目在线稠密重建系统，通过从RGB输入和几何先验中采样高斯基元、联合优化光度与几何损失，以及引入闭环检测，实现了优于现有方法的渲染质量和跟踪精度。

### 研究问题
如何在不依赖外部深度传感器的情况下，利用单目RGB输入实现高精度的在线稠密SLAM重建，同时避免因丢弃RGB信息导致的重建质量下降。

### 核心思路/方法
1. 使用前馈视觉几何模型从未标定RGB输入预测相机和场景几何先验。
2. 通过直接从RGB输入和几何先验中采样高斯基元来扩展高斯场景图。
3. 采用从粗到细的策略联合优化相机位姿和场景图，最小化光度损失和几何损失。
4. 引入在线闭环检测与位姿图优化以保持全局一致性。

### 主要贡献
1. 提出一种结合3DGS地图表示与学习几何先验的单目稠密重建SLAM系统。
2. 通过从RGB和几何先验中采样高斯基元的方式，避免优化过程中丢失RGB信息。
3. 在室内外基准测试中，实现了优于现有方法的渲染质量与跟踪精度，且保持在线实时性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法在单目SLAM和稠密重建领域提出了整合几何先验与3DGS的实用方案，性能有提升，但属于对现有范式的改进而非颠覆性创新；适合对SLAM或神经渲染方向有基础了解的读者参考。

</details>

<details>
<summary>Abstract</summary>

SLAM methods based on 3D Gaussian Splatting (3DGS) have demonstrated impressive tracking and mapping performance, but typically require additional geometric information from external depth sensors. Meanwhile, recent SLAM systems that leverage geometric priors from pre-trained feed-forward models enable real-time dense reconstruction, yet often discard original RGB information during optimization, thus degrading overall reconstruction quality. We present GeoGS-SLAM, an online monocular dense reconstruction system that combines the 3DGS-based map representation with learned geometric priors. Given uncalibrated RGB input, we first employ a feed-forward visual geometry model to predict camera and scene priors. The Gaussian scene map is then expanded by directly sampling Gaussian primitives from both RGB input and geometric priors. Camera poses and the scene map are jointly optimized through a coarse-to-fine strategy that minimizes both photometric and geometric losses. To ensure global consistency, we further incorporate online loop closure detection and pose graph optimization. Extensive experiments across indoor and outdoor benchmarks demonstrate that GeoGS-SLAM achieves superior rendering quality and tracking accuracy compared to state-of-the-art methods while maintaining online real-time performance. Project page: https://rlgao.github.io/geogs_slam.

</details>

#### 2026-07-13 - GHOST: Geometry-Guided Hallucination of Opaque Surface Textures

**Authors:** Langxu Zhao, Zuan Gu, Tianhan Gao
**Links:** [abs](https://arxiv.org/abs/2607.11118) - [pdf](https://arxiv.org/pdf/2607.11118)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GHOST: Geometry-Guided Hallucination of Opaque Surface Textures  
- 作者：Langxu Zhao, Zuan Gu, Tianhan Gao  
- 出版日期：2026-07-13  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：[摘要](https://arxiv.org/abs/2607.11118) | [PDF](https://arxiv.org/pdf/2607.11118)

### 一句话总结
提出一个几何引导的预处理框架GHOST，通过视觉基础模型将透明物体表面转化为不透明、结构一致的RGB纹理，以提升现有深度估计与3D重建模型的精度。

### 研究问题
透明物体因违反朗伯体假设，导致深度估计和3D重建中的几何退化问题。

### 核心思路/方法
提出一个预处理流水线，包含四个模块：  
1. **TransDINO** 和 **TransDecomp**：分别用于解耦透明区域的掩膜和透明度物理属性。  
2. **DAF-Net**：恢复表面法线先验以编码几何曲率。  
3. **GeoSemTransNet**：整合上述多模态线索，合成为保持3D结构的不透明RGB纹理图像。  
该方法无需重新训练下游模型即可直接增强其输入质量。

### 主要贡献
1. 提出一种新框架，通过几何引导的纹理生成解决透明物体的几何恢复难题。  
2. 设计了四个专用模块（TransDINO、TransDecomp、DAF-Net、GeoSemTransNet）协同工作。  
3. 实验表明，该方法能显著提升现有深度估计和重建模型在透明物体上的精度。

### 局限性
摘要未提供足够信息：未提及计算开销、对极端透明或复杂光照场景的鲁棒性，以及是否依赖大量标注数据。

### 阅读优先级
**高**。理由：该文针对3D重建中的透明物体难题提供了新颖的预处理思路，且不依赖下游模型重训练，具有较强实用价值；同时发表于2026年，内容前沿。

</details>

<details>
<summary>Abstract</summary>

Transparent objects pose a fundamental challenge for depth estimation and 3D reconstruction due to their violation of Lambertian assumptions, leading to severe geometry degradation in downstream tasks. To address this, we propose a novel geometry-guided preprocessing framework \textbf{GHOST} that leverages visual foundation models to transform transparent regions into opaque, structurally consistent representations without requiring downstream model retraining. Specifically, our pipeline utilizes (1) \textbf{TransDINO} and (2) \textbf{TransDecomp} to disentangle masks and transparency physical properties, while (3) \textbf{DAF-Net} recovers surface normal priors to encode geometric curvature. Subsequently, (4) \textbf{GeoSemTransNet} integrates these multi-modal cues to synthesize a texture-rich opaque RGB image that preserves the transparent object's 3D structure. Extensive experiments demonstrate that our method significantly enhances the accuracy of state-of-the-art depth estimation and reconstruction models on transparent objects by restoring essential photometric cues.

</details>

#### 2026-07-13 - Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems

**Authors:** Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
**Links:** [abs](https://arxiv.org/abs/2607.11099) - [pdf](https://arxiv.org/pdf/2607.11099)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems
- 作者：Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
- 出版日期：2026-07-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.11099, PDF: https://arxiv.org/pdf/2607.11099

### 一句话总结
提出一种轻量级描述符增强模块Desc++，在保持原始维度与匹配接口的前提下，通过混合全局注意力与几何感知序列建模提升现有视觉SLAM系统的数据关联性能。

### 研究问题
现有视觉SLAM系统中，手工描述符在光照与视角变化下性能下降，而基于学习的替换前端计算开销大；当前描述符增强方法受限于简化注意力机制，上下文建模能力不足，导致匹配质量受限。

### 核心思路/方法
提出Desc++模块，该模块联合编码描述符表示与关键点几何信息，并通过混合架构聚合空间上下文：结合顺序无关的全局注意力与几何感知的序列建模，在线性时间内实现高效增强。增强后的描述符保留原始维度和匹配接口，可直接集成到现有SLAM系统的管线上。

### 主要贡献
- 提出Desc++，一种轻量级描述符增强模块，在保持原始格式的前提下提升匹配精度。
- 引入混合架构，融合全局注意力与几何感知建模，提高上下文表达效率。
- 在描述符匹配、对应关系分析及四个不同SLAM系统的系统级基准上，验证了相比现有增强方法在匹配精度与轨迹估计稳定性上的提升，并实现了精度与效率的平衡。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工作聚焦于提升现有视觉SLAM系统的数据关联鲁棒性，提供了一种不修改管线即可集成的轻量级方案，对工程落地有较好参考价值。但摘要未披露具体性能数值或对比细节，需要进一步阅读全文评估实际提升幅度。

</details>

<details>
<summary>Abstract</summary>

Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically require replacing the extraction-and-matching pipeline and introduce substantial computational overhead. Descriptor enhancement offers a compromise by refining existing descriptors within their original format, yet current methods rely on simplified attention mechanisms whose limited contextual modeling constrains the achievable matching quality. To resolve this trade-off between contextual expressiveness and efficiency, we propose Desc++, a lightweight enhancement module that jointly encodes descriptor representations and keypoint geometry and aggregates spatial context through a hybrid architecture that combines order-agnostic global attention with geometry-aware sequential modeling in linear time. The enhanced descriptors retain their original dimensionality and matching interface, enabling integration into deployed V-SLAM systems without modifying the pipeline. Experiments across descriptor matching, correspondence analysis, and system-level benchmarks with four different V-SLAM systems demonstrate that Desc++ improves matching accuracy over the state-of-the-art enhancement method, translates these gains into more accurate and stable trajectory estimation, and achieves a favorable balance between accuracy and efficiency for practical integration into existing real-time V-SLAM pipelines.

</details>

#### 2026-07-13 - WiFi-JEPA: Self-supervised Learning for WiFi-CSI 3D Human Pose Estimation

**Authors:** Doeon Kim, Jungyoon Lee, Seongsin Kim, Seong-heum Kim
**Links:** [abs](https://arxiv.org/abs/2607.11064) - [pdf](https://arxiv.org/pdf/2607.11064)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WiFi-JEPA: Self-supervised Learning for WiFi-CSI 3D Human Pose Estimation
- 作者：Doeon Kim, Jungyoon Lee, Seongsin Kim, Seong-heum Kim
- 出版日期：2026-07-13
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.11064 ; PDF: https://arxiv.org/pdf/2607.11064

### 一句话总结
WiFi-JEPA 是一个自监督学习框架，通过预测掩码潜在嵌入而非重建原始CSI信号，并在无标注的射线追踪仿真数据上预训练，从而提升WiFi-CSI 3D人体姿态估计在环境变化下的鲁棒性与性能。

### 研究问题
现有基于WiFi的3D人体姿态估计方法在环境变化时容易失效，且严重依赖昂贵的相机标注数据来训练，限制了其规模化应用。如何设计一种无需人工标注、能泛化至新环境的WiFi-CSI姿态估计方法？

### 核心思路/方法
1. **自监督预训练目标**：采用掩码潜在嵌入预测（类似JEPA），而不是重建原始CSI信号，以避免学习硬件相关的噪声和伪影。
2. **CSI特定的结构化掩码**：针对信道、时间、链路（C,T,L）三维张量，提出CSI tokenization和链路掩码——通过掩码整个发射-接收天线链路，迫使模型从其他链路预测该链路的嵌入，从而学习跨链路相关性和3D空间结构。
3. **仿真数据生成**：使用射线追踪模拟，从随机几何体生成多样化的无标注CSI数据，无需任何姿态标注即可提供大规模预训练素材。

### 主要贡献
1. 提出了CSI特定的tokenization和链路掩码策略，有效捕获空间结构信息。
2. 构建了射线追踪CSI仿真管道，可规模化生成无标注预训练数据。
3. 在Person-in-WiFi-3D数据集上，WiFi-JEPA在单人和多人3D姿态估计任务上均超越了以往WiFi-CSI基线方法；仿真数据与真实数据的结合能互补预训练信号；而四种视觉原生自监督目标在CSI任务上性能下降甚至不如从头训练，WiFi-JEPA则持续提升下游姿态估计效果。

### 局限性
摘要未提供足够信息。例如：未讨论模型在不同环境之间的具体迁移效果、对遮挡或极端姿态的鲁棒性、仿真与真实数据之间的域差异程度、训练计算成本或推理速度等。

### 阅读优先级
**高**。理由：该工作提出了在难以标注的模态（WiFi-CSI）中结合仿真数据与自监督学习的有效方案，在3D姿态估计任务上取得了SOTA结果，且对视觉SSL方法不适用WiFi模态的现象给出了直接对比，对同类无监督跨模态感知研究具有参考价值。

</details>

<details>
<summary>Abstract</summary>

WiFi Channel State Information (CSI) enables privacy-preserving human pose sensing in camera-denied environments, but existing WiFi-based pose estimators often fail under environment shifts and rely on costly camera-based annotation pipelines that limit scale. We propose WiFi-JEPA, a self-supervised framework that learns CSI-native representations by predicting masked latent embeddings instead of reconstructing raw CSI signals that may contain hardware-specific artifacts. WiFi-JEPA makes three contributions: (i) CSI-specific tokenization and link masking tailored to the CSI tensor over channel, time, and link (C,T,L); masking entire Tx-Rx antenna links forces the model to predict one spatial link view from others, capturing cross-link correlations informative of 3D spatial structure. (ii) A ray-tracing CSI simulation pipeline that generates diverse unlabeled CSI from randomized geometric primitives, providing scalable pre-training data without pose annotations. (iii) State-of-the-art results on Person-in-WiFi-3D: WiFi-JEPA outperforms prior WiFi-CSI baselines on both single- and multi-person 3D pose estimation under the same evaluation protocol. We also show that simulated CSI provides complementary pre-training signal to real CSI, and that four vision-native SSL objectives degrade performance below training from scratch, whereas WiFi-JEPA consistently improves downstream pose estimation.

</details>

#### 2026-07-12 - Mapping Pamir: Multi-Session Visual-Inertial SLAM and 3D Reconstruction of an Underwater Shipwreck

**Authors:** Michalis Chatzispyrou, Luke Horgan, Hyunkil Hwang, Harish Sathishchandra, Chinmay Burgul, Monika Roznere, Alberto Quattrini Li, Philippos Mordohai, Ioannis Rekleitis
**Links:** [abs](https://arxiv.org/abs/2607.10925) - [pdf](https://arxiv.org/pdf/2607.10925)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, structure from motion, SfM, SLAM, dense reconstruction, sparse reconstruction, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mapping Pamir: Multi-Session Visual-Inertial SLAM and 3D Reconstruction of an Underwater Shipwreck
- 作者：Michalis Chatzispyrou, Luke Horgan, Hyunkil Hwang, Harish Sathishchandra, Chinmay Burgul, Monika Roznere, Alberto Quattrini Li, Philippos Mordohai, Ioannis Rekleitis
- 出版日期：2026-07-12
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2607.10925) | [PDF](https://arxiv.org/pdf/2607.10925)

### 一句话总结
本文提出一个利用低成本运动相机和开源框架的多会话水下环境映射管线，成功实现了对巴巴多斯海域一艘沉船外部和内部首次联合的3D重建。

### 研究问题
如何利用低成本设备和开源框架，实现水下沉船的多会话视觉-惯性SLAM与稠密三维重建。

### 核心思路/方法
1. 使用低成本运动相机采集视觉-惯性数据，并辅以潜水电脑的水深记录。
2. 采用开源VI-SLAM框架SVIn2为每个数据会话生成轨迹和稀疏重建。
3. 从SVIn2提取关键帧与估计的相机位姿，再使用SfM框架COLMAP进行全局优化，并生成目标环境的稠密重建。
4. 当存在固定位置的标定目标时，利用其估计不同会话之间的坐标变换，将所有会话统一到同一坐标系下。
5. 通过三个会话对沉船进行映射：两个会话覆盖沉船外部和内部，第三个会话使用两个不同视场的相机。

### 主要贡献
- 提出一个多会话水下环境映射管线，结合了VI-SLAM和SfM，仅使用低成本运动相机和开源软件。
- 首次实现了对巴巴多斯海域沉船“Pamir”外部与可进入内部的联合三维映射。
- 展示了多会话数据融合及利用标定目标实现坐标对齐的实用性。

### 局限性
摘要未提供足够信息。未提及系统在缺乏标定目标时的对齐精度、光照条件对重建质量的影响、计算资源需求或大规模环境下的可扩展性。

### 阅读优先级
中
**理由**：本文针对水下沉船场景提出了一种实际可行的多会话映射方案，技术路线清晰且结合了低成本硬件与开源工具，对水下机器人或考古应用有参考价值。但方法创新主要集中在流程整合与应用演示，而非算法理论突破，优先级中等。

</details>

<details>
<summary>Abstract</summary>

This paper presents a framework for multi-session mapping of underwater environments utilizing an affordable action camera. The Visual-Inertial data are augmented by water depth recordings from a dive computer. SVIn2, an open-source VI-SLAM framework, is utilized to generate a trajectory and a sparse reconstruction for each session. Utilizing the keyframes extracted from SVIn2 and the estimated camera poses, a Structure-from-Motion (SfM) framework, COLMAP, is employed for global optimization and to produce a dense reconstruction of the target environment. The presence of calibration targets at fixed locations, when available, is used to estimate the coordinate transformation between different data collection sessions, thus transforming the different sessions into the same coordinate frame. The proposed pipeline is employed for the mapping of a shipwreck off the coast of Barbados. For the first time, both the exterior and the accessible interior parts of the wreck were mapped in two sessions, while a third session employed two cameras with different fields of view.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-16 - Online Neural Space Time Memory for Dynamic Novel View Synthesis

**Authors:** Baback Elmieh, Lynn Tsai, Zeman Li, Srinivas Kaza, Tiancheng Sun, Gabor Csapo, Ali Behrouz, Yuan Deng, Stephen Lombardi, Steven M. Seitz, Xuan Luo
**Links:** [abs](https://arxiv.org/abs/2607.15271) - [pdf](https://arxiv.org/pdf/2607.15271)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Online Neural Space Time Memory for Dynamic Novel View Synthesis
- 作者：Baback Elmieh, Lynn Tsai, Zeman Li, Srinivas Kaza, Tiancheng Sun, Gabor Csapo, Ali Behrouz, Yuan Deng, Stephen Lombardi, Steven M. Seitz, Xuan Luo
- 出版日期：2026-07-16
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2607.15271 | PDF：https://arxiv.org/pdf/2607.15271

### 一句话总结
本文提出了一种在线神经时空记忆方法，通过解耦记忆更新与应用的频率，并引入记忆损失和缓存策略，实现了动态场景的实时新颖视角合成。

### 研究问题
在线新颖视角合成中存在持久记忆（用于重建暂时遮挡区域）与实时约束之间的根本权衡：传统测试时训练模型需在每帧进行梯度更新，计算成本高且长上下文不稳定。

### 核心思路/方法
- 将记忆更新与记忆应用解耦：周期性更新记忆，但每帧都应用当前记忆。
- 应用记忆时使用跨视角注意力处理上一记忆状态与当前帧之间的形变。
- 引入两个关键机制：辅助记忆损失（强制内化场景历史）和记忆缓存策略（正则化当前权重，防止灾难性漂移）。

### 主要贡献
- 提出了解耦记忆更新频率的方法，使得在实时条件下仍能维持长期记忆。
- 设计了记忆损失和记忆缓存两种机制以锁定历史上下文。
- 在动态人体运动场景和分钟级记忆任务上实现了实时且当前最优的性能。

### 局限性
摘要未提供足够信息。未说明方法在极快速运动或严重遮挡场景下的性能边界，也未提及与其他非实时方法的定量比较细节。

### 阅读优先级
高。理由：该论文解决了动态场景在线新颖视角合成中的核心实时性难题，方法设计新颖（解耦更新与应用、双重记忆约束），且声称达到实时和SOTA性能，对新视角渲染领域的研究者具有较强的参考价值。

</details>

<details>
<summary>Abstract</summary>

Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes. The computational cost of heavy memory updates precludes real-time application and can lead to instability over long contexts. Given that memory updates are more demanding than memory application and video content is largely redundant, we propose to decouple the frequencies of these two processes. Our approach performs periodic memory updates while applying the memory on a per-frame basis, using cross-view attention to manage deformations between the prior memory state and the current frame. To lock in the historical context, we introduce two critical mechanisms: an auxiliary Memory Loss that forces persistent internalization of the scene, and a Memory Caching strategy that regularizes active weights against catastrophic drift. Our method demonstrates real-time, state-of-the-art performance on scenes with dynamic human motion as well as minute-scale online memorization.

</details>

#### 2026-07-16 - AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight

**Authors:** Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang
**Links:** [abs](https://arxiv.org/abs/2607.14997) - [pdf](https://arxiv.org/pdf/2607.14997)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight
- 作者：Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang
- 出版日期：2026-07-16T13:46:00Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.14997

### 一句话总结
AeroAct 是首个在真实世界四旋翼飞行中实例化的世界-动作模型，通过视频扩散Transformer预测动作轨迹，并在语言指令下实现平滑、动态可行的飞行控制。

### 研究问题
如何为语言控制的四旋翼飞行设计一个模型，使其能利用未来视觉信息作为密集监督信号，输出平滑且动态可行的控制参考，并解决现有方法（如离散动作或瞬时速度指令）对未来观测变化监督不足的问题。

### 核心思路/方法
- 提出行动中心的世界-动作模型（WAM），基于预训练视频扩散Transformer，从第一人称视觉历史、本体感知和语言指令中预测局部轨迹-动作块。
- 训练时使用未来第一人称帧作为密集后果监督；推理时直接解码动作，不生成未来视频。
- 构建基于DiffAero的数据生成管道，结合Isaac Lab和3D高斯泼溅渲染器，获取对齐的视觉、状态、语言和动态可行动作数据。
- 引入低成本手持采集设备，耦合相机观测与运动估计以重建飞行式第一人称轨迹，并通过自引导程序改善重叠轨迹块的时间一致性。

### 主要贡献
1. 首个在真实世界四旋翼飞行中实例化并演示的世界-动作模型（WAM）。
2. 提出利用未来视频帧作为密集监督信号的新训练范式，同时保持推理时无视频生成的高效性。
3. 开发了完整的数据管道（DiffAero、仿真渲染器和手持采集设备），支持大规模对齐数据获取。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工作聚焦于四旋翼飞行与语言指令结合的具体应用场景，创新点在于首次将WAM引入实际飞行任务，并解决了数据获取和训练监督问题。如果读者关注具身智能、无人机导航或视觉语言动作模型，则具有较高参考价值；但如果领域关联不紧密，则优先级可降为中。

</details>

<details>
<summary>Abstract</summary>

Language-conditioned quadrotor flight requires a policy to ground semantic goals, anticipate the visual consequences of ego-motion, and output control references that remain smooth and dynamically executable under rapidly changing first-person views. Existing aerial vision-language navigation and vision-language-action methods commonly use discrete actions, high-level waypoints, or instantaneous velocity commands, which provide limited supervision about how flight actions change future observations. We present AeroAct, an action-centered world-action model (WAM) for quadrotor navigation. To the best of our knowledge, AeroAct is the first WAM instantiated and demonstrated for real-world aerial flight. The model adapts a pretrained video diffusion Transformer to predict local trajectory-action chunks from egocentric visual history, proprioception, and language. Future first-person frames are used during training as dense consequence supervision, while deployment directly decodes actions without generating future video. To obtain aligned visual, state, language, and dynamically feasible action data, we build a DiffAero-based pipeline with complementary Isaac Lab and 3D Gaussian splatting renderers. We further introduce a low-cost handheld collection device that couples camera observations with motion estimates to recreate flight-like egocentric trajectories, and a self-guidance procedure that improves temporal consistency across overlapping trajectory chunks. Closed-loop simulation and real-world experiments show that temporal visual context improves target tracking and object-search performance, and that WAM-based policies can be executed on a physical quadrotor.

</details>

#### 2026-07-16 - JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting

**Authors:** Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao
**Links:** [abs](https://arxiv.org/abs/2607.14990) - [pdf](https://arxiv.org/pdf/2607.14990)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting
- 作者：Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao
- 出版日期：2026-07-16
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页：https://arxiv.org/abs/2607.14990；PDF：https://arxiv.org/pdf/2607.14990

### 一句话总结
JADE-GS通过事件相机提供的微秒级运动信号，在3D高斯泼溅框架中实现联合交替去模糊，并借助双向闭环机制将二维图像恢复器转化为几何感知预测器。

### 研究问题
快速相机运动导致的曝光期间模糊破坏了三维模型所需的清晰场景信息，而事件相机虽能捕获精确运动信号，但其在三维监督中存在两个障碍：1）物理先验和网络先验各有缺陷（漂移积累或边界失真）；2）现有流水线为单向，导致事件噪声或固定伪标签误差直接传递到几何重建中。

### 核心思路/方法
1. **像素自适应路由门**：融合互补的物理事件积分先验（保留边缘但漂移）和学习网络先验（恢复纹理但边界失真）。  
2. **双向闭环耦合**：将二维图像恢复器与3D高斯泼溅学生模型连接，通过解耦的多视角一致渲染图和基于物理的重模糊约束来正则化恢复器，将固定预处理器变为几何感知预测器。

### 主要贡献
1. 提出一种自适应门控机制，有效结合事件驱动的物理先验和深度学习先验进行去模糊。  
2. 设计双向闭环训练策略，使2D恢复器受3D几何约束，避免噪声与偏置单向传递。  
3. 在合成和真实基准上取得最佳感知质量（LPIPS和CLIP-IQA领先），PSNR和SSIM具有竞争力，训练时间约1小时、显存低于5 GB，且支持实时渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法解决了事件引导的3D场景重建中的核心缺陷（先验矛盾与单向误差），并在通用基准上获得感知质量领先，同时在单GPU上实现高效训练和实时渲染，对从事神经渲染、事件视觉或多传感器融合的研究者具有明显参考价值。

</details>

<details>
<summary>Abstract</summary>

When a camera moves fast during exposure, blur destroys the intra-exposure motion a 3D model needs to recover the sharp scene, while event cameras capture exactly this signal at microsecond resolution. Turning them into reliable 3D supervision faces two obstacles. First, the two restoration priors fail in opposite ways: physics-based event-integration priors preserve edges but accumulate drift; learned networks recover texture but distort boundaries. Second, existing pipelines run in one direction only, so raw event noise or the biases of fixed 2D pseudo-labels pass uncorrected into the geometry. JADE-GS addresses both: a pixel-adaptive routing gate fuses the complementary priors, and the resulting 2D restorer is coupled to a 3D Gaussian Splatting student in a bidirectional loop, where detached, multi-view-consistent renders and a physics-based reblurring constraint regularize the restorer, turning a fixed preprocessor into a geometry-aware predictor. Across synthetic and real benchmarks, JADE-GS attains the best perceptual quality, leading LPIPS and CLIP-IQA on both benchmarks with competitive PSNR and SSIM, and trainsin about one hour under 5 GB on a single consumer GPU while preserving real-time rendering.

</details>

#### 2026-07-16 - Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding

**Authors:** Amir Said, Randall Rauwendaal
**Links:** [abs](https://arxiv.org/abs/2607.14513) - [pdf](https://arxiv.org/pdf/2607.14513)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding
- 作者：Amir Said, Randall Rauwendaal
- 出版日期：2026-07-16
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2607.14513；PDF：https://arxiv.org/pdf/2607.14513

### 一句话总结
本文提出利用GPU硬件加速的纹理压缩方案（如BC1和BC7）来高效压缩3D高斯泼溅中的球谐系数，并通过局部分组与重排序提升压缩效率，同时保持并行解码与随机访问能力。

### 研究问题
如何在不牺牲GPU并行渲染性能的前提下，有效压缩3D高斯泼溅（3DGS）中由大量球谐系数导致的大内存占用问题。

### 核心思路/方法
- 利用专门设计用于GPU并行解码且具备硬件加速的纹理压缩格式（BC1、BC7），对3DGS的球谐颜色系数进行压缩。
- 通过将基元按颜色局部分组和重排序，使纹理压缩比直接应用于2D纹理更高效。
- 引入一种比特率控制策略，保留随机访问能力，从而支持大规模并行化而不影响渲染性能。

### 主要贡献
- 提出一种将GPU友好纹理压缩方案应用于3DGS球谐系数压缩的方法，利用硬件加速实现高效并行解码。
- 通过局部基元分组和重排序，显著提升纹理压缩效率。
- 设计比特率控制策略，在保持随机访问和并行化的前提下，实现可忽略或不可察觉的渲染质量损失（基于BC1和BC7格式的实验验证）。

### 局限性
摘要未提供足够信息。未说明不同场景下的压缩率范围、与其它3DGS压缩方法的定量比较，以及解码速度的具体指标。

### 阅读优先级
**高**  
理由：3DGS是当前新颖视图合成的前沿方法，其内存瓶颈是实际部署的关键问题。本文提出的利用GPU原生纹理压缩的思路具备高效、硬件兼容的实用潜力，且实验表明视觉质量损失可忽略，对实时应用和系统优化有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Techniques for modeling 3D scenes from image collections, such as 3D Gaussian Splatting (3DGS), are capable of generating high-quality novel views by leveraging graphics primitives with view-dependent appearance. In 3DGS, spherical harmonic (SH) are employed to model view-dependent color, resulting in a large number of SH coefficients per primitive and large memory requirements. While compression approaches have been proposed to mitigate this problem, they do not exploit the capabilities of modern Graphics Processing Units (GPUs) for parallel decoding and rendering. In this paper, we propose a method for compressing SH color coefficients using texture compression schemes specifically designed for efficient parallel GPU decoding and supported by dedicated hardware acceleration. It is shown that those methods can compress color coefficients more effectively than 2D textures by exploiting the fact that primitives can be locally grouped and reordered according to color. Furthermore, we introduce a bit-rate control strategy that preserves random access, enabling large-scale parallelization without compromising rendering performance. Experimental results using BC1 and BC7 texture compression formats show that GPU-based decompression can be achieved with negligible or imperceptible degradation in the visual quality of rendered 3DGS scenes.

</details>

#### 2026-07-16 - Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency

**Authors:** Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2607.14481) - [pdf](https://arxiv.org/pdf/2607.14481)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** structure from motion, SLAM, radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency
- 作者：Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis
- 出版日期：2026-07-16
- 分类：Neural Scene Representations & Rendering；3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2607.14481，PDF: https://arxiv.org/pdf/2607.14481

### 一句话总结
本文提出首个能够处理无序输入图像序列、提供即时反馈且保持全局一致性的3D高斯泼溅（3DGS）重建方法。

### 研究问题
如何在无序（非连续）图像捕获场景中，实现即时（无需等待全部输入）的3DGS重建，同时保证全局一致性。

### 核心思路/方法
1. **快速无序匹配**：利用视觉地点识别模型和共可见性图，实现无序图像序列的快速匹配，并高效找到高关联关键帧。
2. **局部快速重建**：结合GPU优化和精细的高斯基元放置，在辐射场重建中实现快速局部重建。
3. **基于聚类的闭环**：再次利用共可见性图，提出无需序列输入的聚类闭环方法，保证全局一致性。
4. **渐进式层级结构**：为处理大规模场景，设计渐进式层级方案，使方法可扩展至大型环境。

### 主要贡献
1. 首个为辐射场捕获提供即时反馈且保持全局一致性的方案。
2. 提出针对无序序列的快速匹配方法（重新利用视觉地点识别模型和共可见性图）。
3. 提出基于共可见性图的高效聚类闭环方法，无需依赖顺序输入。
4. 引入渐进式层级结构，使方法能够扩展到包含数千张图像的大场景。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作解决了3DGS实践中常见的无序输入与即时重建的核心矛盾，提出了完整的解决方案（匹配、闭环、可扩展性），且实验结果表明在多种数据集上达到良好视觉质量，对实时3D场景重建具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become the method of choice for reconstructing and real-time rendering of captured scenes. To capture a scene with good visual quality, continuous image sequences are usually combined with out-of-order shots for better scene coverage. Structure from motion can reconstruct such captures, but only after they are all available and often with high computational cost. Incremental reconstruction methods -- often derived from SLAM solutions -- provide immediate feedback, but cannot handle the out-of-order capture we require. We provide the first immediate feedback solution for such radiance field capture that provides global consistency. We first introduce a method for fast matching in out-of-order sequences, by repurposing visual place recognition models and a covisibility graph, and provide an efficient way to find highly connected keyframes, improving quality even for ordered sequences. We show how these steps -- together with GPU optimization and careful Gaussian primitive placement -- provide fast local reconstruction, in our challenging radiance field reconstruction case. We then introduce a novel cluster-based method, again using the covisibility graph, to provide efficient loop closure that does not require sequential input. Finally, to handle large scenes in our context, we introduce a progressive hierarchy that allows our method to scale to large environments, without compromising efficiency. Our results show we provide immediate feedback 3DGS reconstruction with good visual quality in several datasets, with up to thousands of input images.

</details>

#### 2026-07-15 - Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation

**Authors:** NVIDIA, :, Jiahui Huang, Jiawei Ren, Michal Tyszkiewicz, Bjoern Haefner, Michael Shelley, Xin Kang, Seung Wook Kim, Ning Xu, Qi Wu, Janick Martinez Esturo, Shengyu Huang, Nick Schneider, Laura Leal-Taixe, Zan Gojcic, Sanja Fidler
**Links:** [abs](https://arxiv.org/abs/2607.14203) - [pdf](https://arxiv.org/pdf/2607.14203)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, autonomous driving, driving scene, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation
- 作者：NVIDIA, Jiahui Huang, Jiawei Ren, Michal Tyszkiewicz, Bjoern Haefner, Michael Shelley, Xin Kang, Seung Wook Kim, Ning Xu, Qi Wu, Janick Martinez Esturo, Shengyu Huang, Nick Schneider, Laura Leal-Taixe, Zan Gojcic, Sanja Fidler
- 出版日期：2026-07-15
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）；Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：摘要链接 - https://arxiv.org/abs/2607.14203；PDF链接 - https://arxiv.org/pdf/2607.14203

### 一句话总结
Instant NuRec是一种前馈式神经网络重建模型，能够将短时多视角驾驶日志通过单次前向传播快速转化为可模拟的3D高斯场景。

### 研究问题
如何加速神经驾驶场景模拟的3D重建过程，避免现有方法（如NuRec）所需的逐场景调优和较慢的重建速度。

### 核心思路/方法
- 采用前馈式（feed-forward）神经网络架构，直接从校准的多视角相机输入中，一次前向生成包含静态与动态3D高斯层、天空立方体贴图以及每相机ISP校正的分层输出。
- 通过3DGUT原生支持非针孔相机模型。
- 模型深度集成于NuRec框架中，并兼容AlpaSim闭环仿真系统。

### 主要贡献
1. 提出Instant NuRec，实现驾驶场景的快速3D高斯重建（10-20秒多相机场景约1.5秒完成）。
2. 在Waymo Open Dataset上，PSNR比最强基线方法高出2.01 dB。
3. 支持非针孔相机模型，并输出分层场景表示（静态/动态层、天空、ISP校正）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该方法在自动驾驶仿真领域实现了显著的速度提升（单次前向传播）和性能增益（PSNR提升2.01 dB），且解决了现有方法需逐场景调优的痛点，对于从事神经重建、自动驾驶仿真的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

3D simulation platforms are critical for autonomous driving because they enable end-to-end policy evaluation, thereby reducing development costs and improving safety. In recent years, neural simulation has become predominant, with methods such as NuRec playing a central role; however, these methods remain relatively slow and typically require per-scene tuning. In this work, we present Instant NuRec, a feed-forward neural reconstruction model that turns a short multi-view driving log into a fully simulatable 3D Gaussian Splatting (3DGS) world in a single forward pass. The model accepts multi-view input from a calibrated camera rig and emits a layered output consisting of static and dynamic 3DGS layers, a sky cubemap, and per-camera ISP corrections, while providing native support for non-pinhole camera models via 3DGUT. It reconstructs a 10-20-second multi-camera scene in roughly 1.5 seconds and achieves a PSNR on the Waymo Open Dataset that is 2.01 dB above the strongest evaluated baseline. Instant NuRec is deeply integrated into NuRec and is compatible with AlpaSim for closed-loop simulation.

</details>

#### 2026-07-15 - Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting

**Authors:** Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann
**Links:** [abs](https://arxiv.org/abs/2607.13808) - [pdf](https://arxiv.org/pdf/2607.13808)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting
- 作者：Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann
- 出版日期：2026-07-15T13:12:31Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.13808

### 一句话总结
本文提出一种将高频纹理烘焙到紧凑纹理图集的快速渲染方法，通过解耦低频几何与高频外观，在保持高视觉保真度的同时将3DGS渲染速度提升至5倍，并支持60 FPS的4K实时渲染。

### 研究问题
如何克服3D高斯泼溅（3DGS）在基于哈希网格的外观参数化中片段渲染阶段的高计算开销，同时保持高频纹理细节和实时渲染速度。

### 核心思路/方法
1. 采用解耦的辐射表示：用2D surfels建模低频几何和视角相关外观特征，通过视角无关的空间哈希网格表示高频纹理。
2. 将空间哈希网格“烘焙”成一个紧凑的纹理图集（texture atlas）。
3. 引入稀疏性增强优化：惩罚半透明度和每个原语的衰减，从而激进地剪枝不重要的surfels，实现比先前工作更快、更稀疏的重建。
4. 利用几何稀疏性和高效GPU纹理映射来加速渲染。

### 主要贡献
- 提出一种解耦辐射表示，分离低频几何/视角相关外观与高频纹理，并采用烘焙纹理图集技术。
- 通过稀疏性增强优化显著减少surfels数量，实现更快的重建和更稀疏的表示。
- 相比3DGS获得高达5倍的渲染速度提升，同时保持最先进的视觉保真度，在消费级硬件上实现60 FPS的4K实时渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：论文显著提升了3DGS的渲染速度（最高5倍），且直接展示了4K 60 FPS的实时性能，在神经渲染领域具有实际应用潜力；方法结构清晰（解耦表示+烘焙纹理图集+稀疏优化），是近期工作方向中针对效率瓶颈的直观改进，值得深入参考。

</details>

<details>
<summary>Abstract</summary>

Recent extensions of 3D Gaussian Splatting (3DGS) capture fine color details using hash-grid-based appearance parameterization but incur high computational cost during fragment rendering. We introduce a decoupled radiance representation that models low-frequency geometry and view dependent appearance features with 2D surfels while representing high-frequency textures via a view-independent spatial hash grid that is baked into a compact texture atlas. By including sparsity-enhancing optimizations that penalize semi-transparency and per-primitive falloff, our method aggressively prunes insignificant surfels and achieves significantly faster and sparser reconstructions than prior work. Exploiting geometric sparsity and efficient GPU texture mapping, our approach achieves up to a fivefold speedup over 3DGS while preserving state-of-the-art visual fidelity, enabling real-time 4K rendering at 60 FPS on consumer hardware.

</details>

#### 2026-07-15 - Volumetric Inverse Rendering via Neural Radiative Transfer

**Authors:** Ntumba Elie Nsampi, Adarsh Djeacoumar, Hans-Peter Seidel, Tobias Ritschel, Thomas Leimkühler
**Links:** [abs](https://arxiv.org/abs/2607.13695) - [pdf](https://arxiv.org/pdf/2607.13695)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Volumetric Inverse Rendering via Neural Radiative Transfer  
- 作者：Ntumba Elie Nsampi, Adarsh Djeacoumar, Hans-Peter Seidel, Tobias Ritschel, Thomas Leimkühler  
- 出版日期：2026-07-15  
- 分类：Neural Scene Representations & Rendering  
- 链接：arXiv:2607.13695 (摘要: https://arxiv.org/abs/2607.13695, 论文: https://arxiv.org/pdf/2607.13695)

### 一句话总结
本文提出一种基于神经辐射传输的体积逆渲染方法，通过联合优化神经网络场表示的光学属性和光场，并利用辐射传输方程的局部微分形式作为残差目标来强制执行全局光照，从而实现从多视图图像中重建参与介质的散射、吸收和相位函数参数。

### 研究问题
如何从多视图图像中高效且准确地恢复参与介质的体光学属性（如散射、吸收和相位函数），同时兼顾物理完整的全局光照建模与通用神经优化的简便性。

### 核心思路/方法
- 将介质的光学属性和完整光场表示为**神经场**（neural fields）。  
- 通过**联合优化过程**同时估计光学参数和光场。  
- 利用**辐射传输方程（RTE）的局部微分形式**构建残差目标，以强制模型满足全局光照约束。  
- 沿主视角光线添加**体渲染项**以缓解低频偏差。  
- 最终从多视图图像中重建**空间变化、颜色分辨的散射、吸收和相位函数参数**。

### 主要贡献
- 提出一种**兼顾物理完整性与通用神经优化的体逆渲染框架**，无需依赖可微分随机光传输模拟的复杂算法。  
- 通过微分形式的RTE残差目标**实现全局光照建模**，同时利用体渲染项抑制低频偏差。  
- 支持从多视图图像重建**空间变化的散射、吸收和相位函数**，并可用于学习具有物理光学属性的生成模型。

### 局限性
摘要未提供任何关于实验局限性的信息。

### 阅读优先级
**中**。理由：该工作聚焦于体渲染中的逆问题，方法上结合了神经场与辐射传输方程，对从事神经渲染、体积光学属性重建或物理仿真领域的研究者有参考价值；但由于摘要未提供实验对比或性能数据，且属于较新的预印本（出版于2026年），实用性尚待验证。非相关领域读者可暂缓阅读。

</details>

<details>
<summary>Abstract</summary>

Volumetric inverse rendering seeks to recover the optical properties of participating media from images. Existing approaches either rely on differentiable stochastic light transport simulation, which require substantial algorithmic effort, or use simplified models that fail to capture global illumination. We propose a formulation that reconciles physically complete light transport with general-purpose neural optimization. The optical properties of the medium and the full light field are represented as neural fields and estimated through a joint optimization process. Global illumination is enforced via a residual objective derived from the Radiative Transfer Equation in local differential form, complemented by a volume rendering term along primary viewing rays to mitigate \rev{low-frequency} bias. We demonstrate reconstruction of spatially varying, color-resolved scattering, absorption, and phase function parameters from multi-view images. Beyond reconstruction, the same framework supports learning generative models of participating media with physical optical properties under global illumination.

</details>

#### 2026-07-15 - FreeLit: Paired-Free Indoor Relighting via Physics-Guided Diffusion

**Authors:** Chi-En Yen, Duy-Khanh Ngo, Wen-Wei Tang, Huu-Phu Do, Wen-Hsiao Peng, Ching-Chun Huang
**Links:** [abs](https://arxiv.org/abs/2607.13656) - [pdf](https://arxiv.org/pdf/2607.13656)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FreeLit: Paired-Free Indoor Relighting via Physics-Guided Diffusion
- 作者：Chi-En Yen, Duy-Khanh Ngo, Wen-Wei Tang, Huu-Phu Do, Wen-Hsiao Peng, Ching-Chun Huang
- 出版日期：2026-07-15
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2607.13656 | PDF: https://arxiv.org/pdf/2607.13656

### 一句话总结
FreeLit 提出了一种无需配对训练数据的室内场景重打光框架，通过物理引导的扩散模型和内在稳定性策略，实现对光源位置、颜色和强度的可控调整，尤其在低照度场景中表现鲁棒。

### 研究问题
如何在不依赖昂贵的配对多光照数据集的情况下，实现对室内场景的可控重打光（包括光源位置、颜色和强度的显式操控），并提升在低照度等挑战条件中的稳定性和物理一致性。

### 核心思路/方法
1. **无配对框架**：利用物理先验构建照明先验，从内在场景属性生成结构化的光照图（lightmap）和伪重打光图像。
2. **物理引导扩散**：以上述光照图和伪图像作为引导信号，驱动扩散模型合成最终重打光结果。
3. **重打光引导的内在稳定性策略**：针对内在属性估计在低光场景中的不稳定性，通过结构感知蒸馏和一致性约束，强制保持反射率在光照变化下的不变性。
4. **可控制性评估指标**：提出新的评价指标，量化重打光结果与用户指定光照颜色和强度的对齐程度。

### 主要贡献
- 提出了无需配对监督的可控室内重打光框架 FreeLit。
- 设计了物理引导的扩散合成流程，利用内在属性构建照明先验。
- 提出重打光引导的内在稳定化策略，提升低光场景下内在估计的鲁棒性。
- 引入面向可控性的评估指标，用以衡量与用户光照参数的一致性。

### 局限性
摘要未提供足够信息，因此未说明实验中的具体局限性（如计算开销、对极端几何的适应性等）。

### 阅读优先级
中  
理由：该方法针对室内重打光中配对数据稀缺和低光鲁棒性问题，提出了一套无监督且物理约束的解决方案，对从事图像合成、神经渲染或照明估计的研究者有一定参考价值。但摘要未详细介绍与现有方法的定量对比或消融实验细节，需阅读全文验证其有效性。若您关注扩散模型与物理先验结合的重打光方向，可优先阅读。

</details>

<details>
<summary>Abstract</summary>

Image-based indoor scene relighting remains challenging due to the complex interplay between cluttered geometry and local illumination, requiring precise modeling of light position, color, and intensity. Existing data-driven methods implicitly learn this relationship via paired multi-illumination datasets. Nevertheless, this data is costly and fails to scale, which is essential for accurate light-source-level control. Conversely, inverse-rendering methods reduce the data dependency by incorporating physical priors; however, they lack the robustness of intrinsic estimation in challenging conditions. In this paper, we present FreeLit, a paired-free framework for controllable indoor relighting that explicitly manipulates light-source location, color, and intensity. Instead of relying on paired supervision, we construct a physics-guided illumination prior from intrinsic scene properties, generating a structured lightmap along with a pseudo-relit image to guide diffusion-based synthesis. To address instability in intrinsic estimation, especially in low-light scenes, we introduce a relighting-guided intrinsic stabilization strategy that enforces illumination-invariant reflectance through structure-aware distillation and consistency constraints. Furthermore, we propose controllability-oriented evaluation metrics to quantify alignment with user-specified illumination color and intensity. Experimental results demonstrate that FreeLit achieves stable, physically consistent, and controllable relighting, with improved robustness in low-light indoor scenes, without requiring paired supervision.

</details>

#### 2026-07-15 - Learning Physics-Guided Residual Dynamics for Deformable Object Simulation

**Authors:** Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali, Svetlana Lazebnik, Yunzhu Li
**Links:** [abs](https://arxiv.org/abs/2607.13451) - [pdf](https://arxiv.org/pdf/2607.13451)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Physics-Guided Residual Dynamics for Deformable Object Simulation
- 作者：Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali, Svetlana Lazebnik, Yunzhu Li
- 出版日期：2026-07-15T05:15:43Z
- 分类：主要类别：神经场景表示与渲染；次要类别：具身/机器人/AR应用
- 链接：摘要：https://arxiv.org/abs/2607.13451 ；PDF：https://arxiv.org/pdf/2607.13451

### 一句话总结
提出物理引导残差动力学（PGRD）混合框架，将可优化的弹簧-质点物理模拟器与学习残差校正的神经网络结合，在真实世界可变形物体模拟中取得比纯物理或纯学习方法更准确的结果。

### 研究问题
如何准确模拟可变形物体的动力学行为，克服纯物理方法精度不足和纯学习方法泛化性弱的局限。

### 核心思路/方法
1. **混合框架**：以可优化的弹簧-质点模拟器作为基础物理骨干，叠加一个学习残差校正的神经网络。
2. **速度基础公式**：采用基于速度的公式确保模拟稳定性。
3. **滑动窗口Transformer**：使用滑动窗口Transformer架构捕捉时间依赖性。
4. **应用扩展**：将PGRD用于基于模型预测控制的操控规划（包括语言条件设置下的目标图像生成），以及通过3D高斯喷溅进行动作条件视频预测的交互式模拟。

### 主要贡献
- 提出了PGRD混合模拟框架，融合物理模拟与学习残差校正。
- 在多种真实世界可变形物体上展示了优于纯物理和纯学习方法的准确性。
- 展示了PGRD在操控规划（含语言条件）和交互式模拟两个应用中的实用价值。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对机器人操控中可变形物体模拟这一关键难题，提出了新颖且实用的混合方法，并在真实数据上验证了有效性，同时展示了在语言条件操控等前沿应用场景的潜力。

</details>

<details>
<summary>Abstract</summary>

Simulating deformable objects is essential for a wide range of robotic manipulation applications, yet accurately predicting their dynamics remains challenging. We propose Physics-Guided Residual Dynamics (PGRD), a hybrid simulation framework that combines the advantages of physics-based and learning-based approaches. Specifically, PGRD combines an optimizable spring-mass simulator as a backbone with a learned neural network that predicts residual corrections to the physics-based predictions. We adopt a velocity-based formulation to ensure stable simulation and a sliding-window transformer architecture to capture temporal dependencies. We show that PGRD produces more accurate results than both purely physics-based and learning-based methods on a set of diverse real-world deformable objects. We further demonstrate the utility of PGRD in two applications: manipulation planning via Model Predictive Control, including a language-conditioned setting with a generated goal image; and interactive simulation via action-conditioned video prediction by 3D Gaussian Splatting.

</details>

#### 2026-07-14 - Differentiable Polarized Path Tracing

**Authors:** Pramod Rao, Jérémy Riviere, Xilong Zhou, Abhijeet Ghosh, Abhimitra Meka, Thabo Beeler, Marc Habermann, Christian Theobalt, Delio Vicini
**Links:** [abs](https://arxiv.org/abs/2607.13265) - [pdf](https://arxiv.org/pdf/2607.13265)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, inverse rendering, differentiable rendering, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Differentiable Polarized Path Tracing  
- 作者：Pramod Rao, Jérémy Riviere, Xilong Zhou, Abhijeet Ghosh, Abhimitra Meka, Thabo Beeler, Marc Habermann, Christian Theobalt, Delio Vicini  
- 出版日期：2026-07-14  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2607.13265  

### 一句话总结  
本文提出一种基于偏振感知的可微分路径追踪方法，通过结合路径回放与局部缓存估计无偏梯度，解决了偏振算子导致的数值不稳定问题，从而支持复杂场景下的材质与光照逆渲染。

### 研究问题  
现有基于物理的可微分渲染方法大多忽略偏振信息，而偏振线索能约束场景几何与材质属性，但偏振算子（如线性偏振器、漫反射）的秩亏特性破坏了标准梯度估计器（如路径回放反向传播）的可逆性假设，导致数值不稳定。

### 核心思路/方法  
- 采用基于Mueller-Stokes微分的偏振光前向仿真方法。  
- 在反向传播中，通过路径回放与局部缓存相结合的方案估计无偏梯度，避免偏振算子秩亏导致的算法失效，实现稳定优化。

### 主要贡献  
1. 提出一种鲁棒、偏振感知的可微分路径追踪算法。  
2. 解决了偏振光反向扩散中梯度估计的数值不稳定问题。  
3. 扩展了基于物理的逆渲染在复杂材质与光照优化中的适用性。

### 局限性  
摘要未提供足够信息（如实验设置、计算开销、对场景或偏振类型的限制等）。

### 阅读优先级  
**高**。理由：该工作填补了可微分渲染中偏振信息利用的空白，针对关键数值稳定性问题提出新方案，对逆渲染领域（如3D重建、材质估计）具有潜在实用价值，且方法描述清晰。

</details>

<details>
<summary>Abstract</summary>

Physically based differentiable rendering has proven to be a powerful tool for inverse rendering problems (e.g., 3D reconstruction, reflectance estimation, lighting estimation). However, most existing methods operate solely on radiometric intensity, discarding valuable polarization cues that constrain scene geometry and material properties. While forward simulation of polarized light is well-defined via Mueller-Stokes calculus, extending reverse-mode differentiation to this domain presents significant challenges. The rank-deficient nature of common polarimetric operators, such as linear polarizers and diffuse reflections, violates the invertibility assumptions of standard gradient estimators like path replay backpropagation and results in numerical instability. We address this by proposing a robust, polarization-aware differentiable path tracing method. Our approach estimates unbiased gradients through a combination of path replay and local caching. This formulation enables efficient and stable optimization of material and lighting parameters in complex scenes, broadening the applicability of physically based inverse rendering. Project page: https://vcai.mpi-inf.mpg.de/projects/DPPT/

</details>

#### 2026-07-14 - Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation

**Authors:** Lingxiao Guo, Huanyu Li, Guanya Shi
**Links:** [abs](https://arxiv.org/abs/2607.13154) - [pdf](https://arxiv.org/pdf/2607.13154)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation
- 作者：Lingxiao Guo, Huanyu Li, Guanya Shi
- 出版日期：2026-07-14
- 分类：Neural Scene Representations & Rendering (主要), Embodied / Robotics / AR Applications (次要)
- 链接：摘要: https://arxiv.org/abs/2607.13154 ; PDF: https://arxiv.org/pdf/2607.13154

### 一句话总结
本文提出WANDA，一个从单次人类演示中合成大规模训练数据的数据引擎，通过重建场景与轨迹、重排交互片段、纠正状态扩展和跨环境合成，使机器人能从一次演示学习具备空间泛化、长时程鲁棒性和跨环境泛化的开放世界移动操作策略。

### 研究问题
如何用最少的人类演示数据（单次演示）为开放世界移动操作策略提供足够量的训练数据，以实现空间泛化、长时程鲁棒性和跨场景泛化，同时避免传统遥操作和UMI方法的高人力成本。

### 核心思路/方法
1. **场景与轨迹重建**：从单次RGBD观测中重建背景高斯溅射（Gaussian splats）和机器人-物体交互轨迹，作为后续规划和渲染的世界基质。
2. **轨迹重排与扩展**：将交互片段按多种空间配置重新排列，利用全身运动规划将它们连接成新轨迹；并通过纠正状态扩展（Corrective State Expansion）增加机器人和物体在不同移动操作阶段的状态多样性。
3. **跨环境合成**：基于日常照片生成多样化的3D世界，在此类世界中合成新轨迹，解锁跨环境泛化能力。
4. **观测合成**：通过将渲染的机器人/物体网格与高斯溅射背景合成，生成逼真的观测数据。

### 主要贡献
1. 提出WANDA数据引擎，仅需一次人类演示即可大规模合成训练数据，显著降低数据收集成本。
2. 方法在仿真和真实任务中验证，使策略达到长时程鲁棒性、广泛空间泛化和跨环境泛化。
3. 自然支持跨形态数据生成，通过零样本部署到不同形态的移动操作机器人得到验证。

### 局限性
摘要未提供足够信息。例如：未说明在不同场景中的具体性能指标、真实世界实验的失败案例、计算开销或与基线方法的量化对比等。

### 阅读优先级
**高**
理由：该论文针对开放世界移动操作中的数据瓶颈问题，提出从单次演示合成大量数据的创新方法，同时涉及神经场景表示、机器人学习和跨场景泛化等前沿领域，对低数据驱动机器人研究具有重要启发。结果在仿真和真实任务中均得到验证，且展示了跨形态迁移能力，实用性较强。

</details>

<details>
<summary>Abstract</summary>

Learning open-world mobile manipulation policies requires vast data to achieve spatial generalization, long-horizon robustness, and scene generalization. Current prevailing data collection paradigms, teleoperation and UMI, demand prohibitive human effort and cost at scale. To scale beyond the limits of manual data collection, we seek to maximize the value of each human demonstration by scalable data generation. To this end, we introduce WANDA: learning open-World mobile mANipulation from one demonstration via a synthetic DAta engine. WANDA first reconstructs background Gaussian splats and robot-object interaction trajectories from source RGBD observations, as a world substrate for later planning and rendering. It then rearranges contact-rich robot-object interaction segments into extensive spatial configurations, utilizing whole-body motion planning to chain them into new trajectories. To enhance long-horizon robustness, it applies Corrective State Expansion to increase the robot and object state diversity at different stages of mobile manipulation. To unlock cross-environment generalization, trajectories are synthesized on diverse generated 3D worlds from everyday photos. Furthermore, we synthesize photo-realistic observations by compositing rendered robot and object meshes with Gaussian splatting backgrounds. We evaluate our approach on extensive simulation and real-world tasks in various scenes. Experiments show that policies trained with WANDA achieve long-horizon robustness, broad spatial generalization and cross-environment generalization from one real demonstration. Moreover, WANDA naturally supports cross-embodiment data generation, validated by zero-shot deployment on another mobile manipulator with a distinct morphology.

</details>

#### 2026-07-14 - ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting

**Authors:** Cheng-Tai Hsieh, Jiwei Shan, Han Fang, Jianshu Hu, Tao Ni, Lijun Han, Yutong Ban, Shing Shin Cheng, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2607.12785) - [pdf](https://arxiv.org/pdf/2607.12785)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, neural rendering, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting  
- 作者：Cheng-Tai Hsieh, Jiwei Shan, Han Fang, Jianshu Hu, Tao Ni, Lijun Han, Yutong Ban, Shing Shin Cheng, Hesheng Wang  
- 出版日期：2026-07-14  
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）  
- 链接：[arXiv:2607.12785](https://arxiv.org/abs/2607.12785)  

### 一句话总结
ExtraGS 通过引导扩散模型生成伪观测数据并采用置信度加权微调，增强了基于 3D 高斯溅射的内窥镜视图外推能力，显著减少了外推伪影。

### 研究问题
如何在机器人辅助微创手术中，利用有限的观察数据（内窥镜视频）实现高质量的视图外推（extrapolation），即合成训练轨迹之外的新视角，并减少伪影。

### 核心思路/方法
1. **初始重建**：使用 3D 高斯溅射（3D Gaussian Splatting）从内窥镜视频进行初始场景重建。  
2. **不确定性引导的虚拟相机采样**：主动探索观察盲区，最大化信息增益，生成可能包含未知区域的虚拟视角。  
3. **扩散模型细化**：使用扩散模型对虚拟视角的渲染结果进行精细化，恢复合理的解剖结构，产生“伪观测”数据。  
4. **置信度加权微调**：在将伪观测数据融入优化时，采用置信度加权策略，避免生成内容退化已有可靠区域。

### 主要贡献
- 提出了 ExtraGS 框架，结合 3D 高斯溅射与扩散模型，用于增强内窥镜视图外推。  
- 设计了不确定性引导的虚拟相机采样策略，以主动探索盲区。  
- 实现了置信度加权的微调策略，在引入伪观测时保持可靠区域的质量。  
- 在多个公开内窥镜数据集上达到了最先进的新视图合成性能，显著减少了外推伪影。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作聚焦于手术机器人内窥镜感知这一实际医疗应用，提出了一种结合 3D 高斯溅射与扩散模型的创新思路，增强了视图外推能力。摘要明确展示了问题定义、方法设计和实验验证，且实现了 state-of-the-art 性能，对手术场景中的神经渲染研究有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of the surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating beyond the training trajectory. In this work, we propose ExtraGS, a framework for enhancing endoscopic view extrapolation through diffusion-guided 3D Gaussian Splatting. Starting from an initial reconstruction, we introduce an uncertainty-guided virtual camera sampling strategy to actively explore blind spots and maximize information gain. The rendered views from these sampled locations are refined using a diffusion model to recover plausible anatomical structures, producing pseudo-observations that guide further optimization. To prevent the generated content from degrading reliable regions, we adopt a confidence-weighted fine-tuning strategy when incorporating these pseudo-observations. Extensive experiments on multiple public endoscopic datasets demonstrate that ExtraGS significantly reduces extrapolation artifacts and achieves state-of-the-art performance in endoscopic novel view synthesis.

</details>

#### 2026-07-14 - GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR

**Authors:** Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu
**Links:** [abs](https://arxiv.org/abs/2607.12641) - [pdf](https://arxiv.org/pdf/2607.12641)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR
- 作者：Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu
- 出版日期：2026-07-14T11:19:16Z
- 分类：主要：Neural Scene Representations & Rendering；次要：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2607.12641；PDF：https://arxiv.org/pdf/2607.12641

### 一句话总结
提出一个面向无线空中VR的几何感知跨层框架GeoFovea-GS，通过联合优化3DGS渲染与通信资源分配，在传输成本大幅降低的同时提升沉浸式渲染质量。

### 研究问题
现有无线空中VR在带宽、延迟和功率受限下难以生成高质量视图，且3DGS的几何误差会导致VR质量严重下降；此外，现有信道感知或像素级资源分配方案无法捕捉几何敏感的失真，因此需要一种能兼顾几何误差与通信效率的跨层优化方法。

### 核心思路/方法
1. 开发了一种**注视点几何感知失真度量**，统一表征光度渲染误差、几何不一致性和视图依赖的感知重要性。
2. 基于该度量，将纯姿态3DGS渲染与图像/瓦片纠正传输的联合选择，表述为**无线约束下的跨层优化问题**。
3. 设计了一个**轻量级信息价值调度器**，将通信资源优先分配给既几何关键又感知重要的区域。

### 主要贡献
- 提出了首个几何感知的跨层框架GeoFovea-GS，用于通信高效的无线空中VR。
- 设计了统一形式的注视点几何感知失真度量，联合考虑光度、几何和感知因素。
- 实现了在真实3DGS场景中，以显著降低的传输成本获得更优的沉浸式渲染质量。

### 局限性
摘要未提供关于框架在实时性、计算开销、不同场景泛化能力或与现有系统集成方面的局限性信息。

### 阅读优先级
**高**  
理由：该工作针对无线VR中渲染与通信的联合优化这一实际瓶颈，提出了新颖的几何感知跨层方法，且实验在真实3DGS场景上取得显著效果。对于从事神经渲染、VR通信、无线资源分配方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Wireless aerial virtual reality (VR) aims to provide immersive access to large-scale scenes, but high-resolution view generation and delivery are jointly constrained by limited bandwidth, latency, and power. 3D Gaussian Splatting (3DGS) can reduce the payload by rendering views from compact pose information, yet its geometry errors may cause severe VR quality degradation. Existing channel-aware or pixel-level resource allocation schemes fail to capture such geometry-sensitive distortion. To address this issue, this paper proposes GeoFovea-GS as a geometry-aware cross-layer framework for communication-efficient wireless aerial VR. A foveated geometry-aware distortion metric is developed to characterize photometric rendering error, geometric inconsistency, and view-dependent perceptual importance in a unified form. Based on this metric, the joint selection of pose-only 3DGS rendering and image/tile correction transmission is formulated as a cross-layer optimization problem under wireless constraints. A lightweight value-of-information scheduler is further developed to allocate communication resources to regions that are both geometry-critical and perceptually important. Experiments on real-world 3DGS scenes demonstrate that GeoFovea-GS achieves superior immersive rendering quality with substantially reduced transmission cost.

</details>

#### 2026-07-14 - Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots

**Authors:** Yanghe Hao, Martin Huber, Christos Bergeles, Tom Vercauteren
**Links:** [abs](https://arxiv.org/abs/2607.12604) - [pdf](https://arxiv.org/pdf/2607.12604)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** pose estimation, differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots
- 作者：Yanghe Hao, Martin Huber, Christos Bergeles, Tom Vercauteren
- 出版日期：2026-07-14
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.12604

### 一句话总结
本文通过优化立体可微渲染框架，实现了无标记、实时的外科手术机器人跟踪，速度达30 fps，精度与基于标记的方法相当。

### 研究问题
如何在无标记条件下，实现手术机器人实时、高精度的三维位姿跟踪，以克服传统基于标记的方法在杂乱手术室中易被遮挡的缺点。

### 核心思路/方法
在标记无关位姿估计框架roboreg基础上，引入两项改进：
1. 序列优化：通过运动自适应超参数调优，在帧间传播位姿估计。
2. CUDA流并行化：并行执行分割与优化，并用CUDA-graph加速分割过程。
最终实现立体可微渲染的在线动态跟踪。

### 主要贡献
- 实现了实时1080p、30 fps的跟踪速度（原框架仅14 fps），与相机帧率匹配。
- 静态精度达1.7 cm / 0.6度（与静态真值对比），动态参考下平均3D误差为1.2 cm（27,460帧）。
- 在遮挡场景下（1,242帧）平均误差为1.53 cm。
- 相比FoundationPose基线，动态估计提升11%（遮挡下提升63%），静态估计提升250%，且推理速度快6倍。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法解决了手术机器人无标记跟踪中的实时性与精度权衡问题，性能显著优于已有基线，且速度达到实际应用要求，对机器人辅助手术领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Purpose: Marker-based tracking of surgical robots is occlusion-prone in cluttered operating rooms. We evaluate stereo differentiable rendering for marker-free, real-time robot pose tracking, potentially improving safety, reducing setup time, and enabling multi-robot interaction. Methods: We extend the markerless pose estimation framework roboreg to online dynamic tracking via (i) sequential optimisation that propagates pose estimates across frames with motion-adaptive hyperparameter tuning, and (ii) CUDA stream parallelisation of segmentation and optimisation, combined with CUDA-graph accelerated segmentation. We evaluate on 38 unobstructed and 5 occluded displacement sequences with static start/end ground-truth calibrations and dynamic marker-based reference tracking. Results: We achieve real-time 1080p tracking at 30 fps (up from 14 fps for vanilla roboreg), matching the camera frame rate. Accuracy reaches 1.7 cm / 0.6 deg against static ground truth and 1.2 cm mean 3D error over 27,460 frames against the marker-based reference (1.53 cm over 1,242 occluded frames). Our method outperforms FoundationPose by 11% in dynamic estimation (63% under occlusion) and 250% in static estimation, with 6x faster inference. Conclusions: Stereo differentiable rendering enables real-time, high-resolution marker-free surgical robot tracking, on par with marker-based approaches and surpassing foundation-model baselines.

</details>

#### 2026-07-13 - MetaView: Monocular Novel View Synthesis with Scale-Aware Implicit Geometry Priors

**Authors:** Yufei Cai, Xuesong Niu, Hao Lu, Kun Gai, Kai Wu, Guosheng Lin
**Links:** [abs](https://arxiv.org/abs/2607.12000) - [pdf](https://arxiv.org/pdf/2607.12000)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** metric depth, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MetaView: Monocular Novel View Synthesis with Scale-Aware Implicit Geometry Priors  
- 作者：Yufei Cai, Xuesong Niu, Hao Lu, Kun Gai, Kai Wu, Guosheng Lin  
- 出版日期：2026-07-13  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2607.12000  

### 一句话总结
本文提出MetaView，一种基于扩散模型的单目新视角合成框架，通过结合隐式几何先验和度量深度线索，在保持几何一致性的同时实现大幅视点变化下的可控渲染。

### 研究问题
如何在单张图像输入下，实现大幅视角变化下的新视角合成，同时兼顾几何一致性、精确相机控制和高泛化能力。

### 核心思路/方法
- 引入隐式几何先验：利用前馈几何感知网络提取结构化约束，不依赖显式的重建管线。  
- 显式度量深度锚定：将生成过程锚定到度量尺度，增强精确控制能力。  
- 整体设计：融合隐式几何建模与最小必要的显式3D线索，在扩散框架下实现灵活性与约束的平衡。

### 主要贡献
- 提出了MetaView框架，在单目大幅视角变化下显著优于现有方法。  
- 展示出优越的泛化性能（摘要未提供具体数值或实验细节）。  
- 代码开源。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对视觉生成中空间结构感知这一关键问题提出创新解决方案，结合隐式几何先验与度量深度，方法设计合理且有明显性能提升，开源代码便于复现，适合对神经场景表示和生成式新视角合成感兴趣的读者。

</details>

<details>
<summary>Abstract</summary>

Current visual generation models are capable of producing high-quality content, yet they lack a coherent perception of the spatial structure. Existing generative novel view synthesis methods typically introduce explicit geometry priors, which enforce spatial consistency but inherently restrict generalization in large view changes. In contrast, recent interactive generative methods favor implicit scene modeling, offering greater flexibility at the cost of precise camera control and geometry consistency. In this paper, we propose MetaView, a diffusion-based monocular novel view synthesis framework that enables rendering under large view changes from a single image. Our key insight is to combine implicit geometry modeling with minimal yet essential explicit 3D cues: we incorporate implicit geometry priors from a feed-forward geometry perception network to regularize structure without imposing restrictive reconstruction pipelines, while leveraging metric depth to anchor the generation to a metric scale. This design allows MetaView to achieve both geometry consistency and precise controllability. Extensive experiments demonstrate that, under challenging monocular large viewpoint changes, MetaView significantly outperforms existing methods and exhibits superior generalization. Our code is publicly available at https://github.com/KlingAIResearch/MetaView.

</details>

#### 2026-07-13 - ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space

**Authors:** Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan
**Links:** [abs](https://arxiv.org/abs/2607.11673) - [pdf](https://arxiv.org/pdf/2607.11673)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** video reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space
- 作者：Mingchao Sun, Luyang Tang, Yu Liu 等34位作者
- 出版日期：2026-07-13
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）；具身/机器人/增强现实应用（Embodied / Robotics / AR Applications）
- 链接：[摘要](https://arxiv.org/abs/2607.11673) | [PDF](https://arxiv.org/pdf/2607.11673)

### 一句话总结
提出一个通用多模态3D世界模型，将文本、图像、视频输入转化为高保真、可探索的3D场景，并通过统一的空间生成基元（SGP）实现高效的3D空间描述。

### 研究问题
如何将多种输入模态（文本、图像、视频）转化为一致、高保真的可探索3D世界，并支持从稀疏输入（单张图片或句子）到丰富输入（多视图集、随意视频）的通用构建。

### 核心思路/方法
核心是“空间生成基元（SGP）”——一个包含高质量全景图与空间点云的紧凑元组。流程分三步：
1. **输入提升**：将多模态输入映射为SGP。丰富输入通过几何严格恢复实现场景重建；单图像或句子则通过生成式方法创造新世界。
2. **3D一致全景视频生成**：沿规划轨迹探索SGP，生成连续的3D一致全景视频。
3. **全景视频重建引擎**：将生成视频转换为清晰的逼真3D高斯泼溅（3DGS）世界。此外，支持将生成的世界锚定到地理兴趣点，实现地图原生的空间探索。

### 主要贡献
1. 提出通用多模态3D世界模型，统一处理文本、图像、视频输入。
2. 引入紧凑的空间生成基元（SGP），高效描述任意3D空间。
3. 在高质量全景图与点云基础上，通过全景视频生成与3DGS重建，实现高保真场景。
4. 在稀疏输入（单图像/句子）上支持创造性生成，在丰富输入上实现几何严格恢复。
5. 将生成世界锚定到地理兴趣点，具备消费级地图原生探索能力。
6. 实验表明，在丰富多模态输入下，该方法在开源方法中达到最优，场景保真度优于Marble。

### 局限性
摘要未提供充分信息。例如未讨论多视图一致性、生成速度、对复杂场景的鲁棒性、训练数据依赖或失败模式。

### 阅读优先级
中  
理由：该方法在3D场景生成领域具有新颖性，提出统一的SGP基元并支持地理锚定，适合关注多模态3D内容创作的研究者。但由于发布时间为2026年，方法细节和实验仅基于摘要概要，可先阅读全文评估实用性与局限性。对纯应用或工程导向的读者优先级可降低。

</details>

<details>
<summary>Abstract</summary>

We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds. At the heart of our framework is a unified Spatial Generative Primitive (SGP), a compact tuple of a high-quality panorama and a spatial point cloud that delivers an efficient description of any 3D space. Multimodal inputs are first lifted into this primitive; a 3D-consistent panoramic video generator then explores the primitive along a planned trajectory; finally, our panoramic video reconstruction engine converts the generated video into a clean, photorealistic 3D Gaussian Splatting (3DGS) world. This pipeline covers two regimes: rich inputs (multi-view sets, casual video) are lifted into the SGP through a geometry-rigorous recovery that mirrors the observed scene, while a single image or sentence is completed generatively into a creative world. The result is one low-barrier engine for general 3D content creation that further anchors generated worlds to geographic points of interest, enabling map-native spatial exploration at consumer scale. Experiments show that ABot-3DWorld 0 sets the state of the art among open-source methods and demonstrates stronger scene fidelity than Marble under rich multimodal inputs.

</details>

#### 2026-07-13 - HyperGS: Fast and Generalizable Gaussian Video Representation

**Authors:** Fatimah Zohra, Chen Zhao, Shuming Liu, Yahya Al Malallah, Bernard Ghanem
**Links:** [abs](https://arxiv.org/abs/2607.11500) - [pdf](https://arxiv.org/pdf/2607.11500)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HyperGS: Fast and Generalizable Gaussian Video Representation
- 作者：Fatimah Zohra, Chen Zhao, Shuming Liu, Yahya Al Malallah, Bernard Ghanem
- 出版日期：2026-07-13
- 分类：Neural Scene Representations & Rendering
- 链接：abstract: https://arxiv.org/abs/2607.11500, pdf: https://arxiv.org/pdf/2607.11500

### 一句话总结
HyperGS 提出一种前馈式、免优化的高斯视频表示方法，通过因子化时空Transformer和可学习查询Transformer直接从视频预测高斯参数，实现极快编码与跨视频的零样本泛化。

### 研究问题
现有基于高斯泼溅的视频表示方法依赖逐视频优化，导致编码速度慢且难以跨视频泛化。HyperGS 旨在解决如何在不执行逐视频优化的前提下，快速生成可泛化的高斯视频表示。

### 核心思路/方法
1. **前馈预测架构**：设计一个因子化时空Transformer从输入视频提取token，再通过一个基于可学习查询的Transformer为每一帧预测8参数的高斯表示。
2. **秩几何正则化**：针对直接预测时出现的“针状退化”导致训练崩溃的问题，提出一种自适应强度动态调整的秩基几何正则化器，稳定优化过程。
3. **零样本高分辨率渲染**：模型能直接泛化到未见过的分布及720p视频，无需重新编码即可进行更高分辨率渲染。

### 主要贡献
- 提出第一个前馈式、免优化高斯视频表示方法，实现编码速度相比逐视频优化提升4到5个数量级（10^4–10^5×），同时保持匹配的重建质量。
- 在K400、SSv2、UCF101等基准上，以更小的视频表示尺寸，将PSNR提升+2.9–3.1 dB（相比此前视频编码器）。
- 展示了高斯泼溅在前馈预测下的泛化能力，结合了快速灵活渲染与前馈预测的速度和通用性。

### 局限性
摘要未提供关于模型在处理超长视频、内存消耗、或对复杂动态场景（如剧烈遮挡、快速运动）的具体表现细节。摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法显著加快了高斯视频表示的编码速度（数个数量级），并通过零样本泛化支持高分辨率视频，性能在多个基准上大幅优于此前方法，对于追求实时或可泛化视频表示的研究与应用有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has emerged as an effective representation for video, but existing methods rely on per-video optimization. This leads to slow encoding and limits generalization across videos. To amortize this optimization, we propose HyperGS, a feedforward, optimization-free approach that directly predicts Gaussian representations from any video in a single forward pass, speeding up encoding and decoding by orders of magnitude while generalizing to out-of-distribution videos at higher resolutions. In HyperGS, we design a factorized spatiotemporal Transformer to extract tokens from video, and a learnable query-based Transformer to obtain 8-parameter Gaussian representations for each video frame. We find that naively predicting Gaussians across diverse videos induces a needle-like degeneration that collapses training, and address this with a rank-based geometric regularizer whose strength adapts dynamically to stabilize optimization. HyperGS achieves encoding at $10^4$--$10^5\times$ the speed of per-video Gaussian optimization at matched reconstruction quality while generalizing zero-shot to $720p$ video, enabling higher-resolution rendering without re-encoding. HyperGS improves PSNR by +2.9--3.1 dB over the prior video encoders on K400, SSv2, and UCF101 at a smaller video representation size. By predicting explicit 2D Gaussians in a single forward pass, HyperGS combines the fast, flexible rendering of Gaussian Splatting with the speed and generalization of feedforward prediction, advancing Gaussians as a practical direction for fast and generalizable video representation.

</details>

#### 2026-07-13 - AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling

**Authors:** Yingji Zhong, Dave Zhenyu Chen, Fuzhao Ou, Youyu Chen, Zhihao Li, Lanqing Hong, Dan Xu
**Links:** [abs](https://arxiv.org/abs/2607.10995) - [pdf](https://arxiv.org/pdf/2607.10995)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling
- 作者：Yingji Zhong, Dave Zhenyu Chen, Fuzhao Ou, Youyu Chen, Zhihao Li, Lanqing Hong, Dan Xu
- 出版日期：2026-07-13
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.10995

### 一句话总结
本文提出一种非对称的3D高斯泼溅架构，通过分离几何与外观建模来减少计算冗余，在长序列新视角合成任务中实现效率大幅提升。

### 研究问题
如何减少现有可泛化3D高斯泼溅模型在长序列新视角合成中的冗余计算，同时保持或提升渲染质量。

### 核心思路/方法
基于两个观察：（i）高质量NVS不严格要求高精度几何；（ii）外观学习通常比几何恢复更容易。因此设计非对称架构，将几何建模和外观建模解耦：
- 几何分支：使用粗粒度token和大部分参数进行多视图重建。
- 外观分支：使用细粒度token和显著更少的参数捕捉细节。
- 两个分支通过双边连接交互，实现任务间的相互指导。

### 主要贡献
1. 提出任务感知的非对称架构，有效减少计算冗余并更合理地分配计算资源。
2. 在32视图960P输入下，模型匹配优化方法的质量，同时实现近800倍加速。
3. 超越现有可泛化模型的零样本性能，参数更少、训练/推理开销更低，整体效率提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该工作针对长序列场景建模中计算冗余的关键问题，提出了清晰且新颖的非对称架构设计，在效率（800倍加速）和性能（匹配优化方法）上均有显著突破，对NeRF/3D高斯泼溅领域的研究者和实践者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent generalizable 3D Gaussian Splatting models have advanced long-sequence novel view synthesis (NVS), but at the cost of substantial redundant computation. We identify that the redundancy can be mitigated based on two observations: (i) high-precision geometry is not strictly required for high-quality NVS; (ii) appearance learning is generally easier than geometry recovery. Motivated by these insights, we propose an asymmetric architecture that decouples geometry and appearance modeling. The geometry branch processes coarse-grained tokens with most of the parameters for multi-view reconstruction, while the appearance branch operates on fine-grained tokens to capture details using significantly fewer parameters. The two branches interact through bilateral connections, enabling mutual guidance for their respective tasks. This task-aware asymmetry reduces the computational redundancy and allocates the computation more judiciously, thereby increasing parameter efficiency and enabling smaller models to achieve strong performance. On 32-view 960P inputs, our model matches optimization-based methods while delivering nearly 800x speedup, and surpasses the zero-shot performance of state-of-the-art generalizable models with markedly fewer parameters and reduced training/inference overhead, achieving an overall efficiency improvement.

</details>

#### 2026-07-12 - DP-Splat: Bayesian Nonparametric Complexity Control for Gaussian Splatting

**Authors:** Aqi Dong
**Links:** [abs](https://arxiv.org/abs/2607.10912) - [pdf](https://arxiv.org/pdf/2607.10912)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DP-Splat: Bayesian Nonparametric Complexity Control for Gaussian Splatting
- 作者：Aqi Dong
- 出版日期：2026-07-12
- 分类：神经场景表示与渲染
- 链接：https://arxiv.org/abs/2607.10912

### 一句话总结
本文提出DP-Splat，通过引入截断狄利克雷过程先验（截断stick-breaking）和稀疏过拟合有限狄利克雷先验，使3D高斯溅射中高斯成分的数量能够自适应场景复杂度，同时保持闭式坐标上升更新。

### 研究问题
3D高斯溅射中，高斯成分数量K通常由启发式的密度控制或用户上限设定，缺乏基于数据自适应调整的理论基础。现有变分贝叶斯方法（如VBGS）虽将溅射拟合转为共轭变分推断，但K仍固定不变。

### 核心思路/方法
1. 将有限对称狄利克雷先验替换为截断stick-breaking狄利克雷过程先验，以及作为理论替代的稀疏过拟合有限狄利克雷先验，使被占用的成分数量自适应数据。
2. 所有更新保持闭式坐标上升步骤；提出自然梯度随机变体，使得每步计算成本与数据点数无关。
3. 给出了精确单调性保证、严格的截断误差界（纠正了常见大α近似中过于保守的问题），并对拟合的成分数量估计含义进行诚实分析。

### 主要贡献
1. 理论贡献：提供了精确单调性证明、严格的截断误差界，并区分了变分实践与后验渐近理论之间的差距（在N三个数量级范围内证实）。
2. 实验贡献：
   - 有效复杂度K^自适应场景复杂度，在分离良好的合成数据上恢复真实K（误差±1）。
   - 在解混淆比较中，DP先验的贡献主要来自复杂度选择而非逐成分效率：在匹配预算下，收敛的DP拟合超过单次固定K的VBGS +2.7 dB，而与同样收敛的固定K基线持平；在3D场景中，DP-Splat以5.9-7.6倍更少的成分达到或超过VBGS的保留颜色预测。
   - 后验预测颜色方差在模型匹配的合成数据上校准良好。
   - 在均场坐标上升下，DP先验抵抗过度分裂而稀疏有限混合达到截断饱和，揭示了变分实践与后验渐近之间的差异。

### 局限性
摘要未提供任何关于方法局限性、潜在失败场景或计算资源需求的信息。

### 阅读优先级
高。
理由：该方法从贝叶斯非参数角度解决了高斯溅射中成分数量自动选择的核心问题，具有理论保证（单调性、截断误差界）和明确的实验优势（成分数量减少5.9-7.6倍且性能匹配/超越基线）。对神经场景表示和变分推断领域均有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting represents scenes as finite mixtures of anisotropic Gaussians whose number of components $K$ is set by heuristic density control or user caps. Variational Bayes Gaussian Splatting (VBGS) recast splat fitting as conjugate variational inference, but $K$ remains fixed. We replace the finite symmetric Dirichlet over mixture weights with a truncated stick-breaking Dirichlet-process prior -- and, as a theory-backed alternative, a sparse overfitted finite Dirichlet -- so that the number of occupied components adapts to the data while every update remains a closed-form coordinate-ascent step; a natural-gradient stochastic variant makes the per-step cost independent of the number of points. We give an exact monotonicity guarantee, a rigorous truncation-error bound correcting an anti-conservative large-$α$ approximation in common use, and an honest account of what the fitted number of components estimates. Empirically: (i) the effective complexity $\hat{K}$ adapts to scene complexity and recovers the true $K$ within $\pm 1$ on well-separated synthetic data with regime-appropriate concentration; (ii) a deconfounded comparison shows the DP prior's contribution is complexity selection, not per-component efficiency -- converged DP fits exceed single-pass fixed-$K$ VBGS by +2.7 dB at matched budgets yet tie an equally converged fixed-$K$ baseline, and on 3D scenes DP-Splat matches or exceeds VBGS's held-out color prediction with 5.9-7.6x fewer components; (iii) the posterior-predictive color variance is well calibrated on model-matched synthetic data; and (iv) the ordering suggested by exact-posterior asymptotics reverses under mean-field coordinate ascent: the DP prior resists over-splitting while the sparse finite mixture saturates its truncation, a gap between variational practice and posterior asymptotics documented across three orders of magnitude in $N$.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-16 - RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping

**Authors:** Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2607.15048) - [pdf](https://arxiv.org/pdf/2607.15048)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** surface reconstruction, autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping
- 作者：Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang
- 出版日期：2026-07-16
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.15048

### 一句话总结
该论文提出一种基于自适应网格高斯表示的鲁棒大规模道路表面建图框架ROADGS-T，通过将2D高斯曲面片布置在网格上，并结合道路结构感知的自适应策略和轨迹一致性姿态优化，提升重建质量和效率。

### 研究问题
如何在大规模驾驶场景下，克服现有基于网格的道路表面重建方法存在的重建质量有限和优化成本高的问题，实现高精度、高效的道路表面建图。

### 核心思路/方法
1. **网格高斯表示**：将2D高斯曲面片（surfels）放置于网格上，每个曲面片显式存储颜色、语义和几何信息，相比于传统网格表示和3D高斯基元，更匹配道路薄表面特性，减少冗余基元和重叠。
2. **道路结构感知自适应网格策略**：对几何或语义复杂区域（如车道标记、道路边界、高度变化处）分配更密的高斯曲面片，在平坦区域保持紧凑表示。
3. **轨迹一致性引导的姿态鲁棒优化**：不依赖单一最近车辆姿态，而是从多个邻近姿态估计局部表面先验，并根据几何一致性自适应加权姿态引导的高度正则化。

### 主要贡献
1. 提出基于自适应网格高斯的道路表面建图框架ROADGS-T。
2. 设计网格高斯表示，兼顾道路的薄表面属性和存储效率。
3. 开发道路结构感知自适应网格分配策略，提升复杂区域重建保真度。
4. 提出轨迹一致性引导的姿态鲁棒优化，减少对单一姿态的依赖。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶中道路建图这一关键方向，提出结合自适应网格和高斯表示的新方法，并解决了大规模场景下的效率与质量权衡问题，方法新颖且实用性强。

</details>

<details>
<summary>Abstract</summary>

Road surface mapping plays a crucial role in autonomous driving, supporting high-definition map generation, lane-level perception, and automatic road annotation. Recent mesh-based road surface reconstruction methods have shown promising results, but they still suffer from limited reconstruction quality and high optimization cost, especially in large-scale driving scenarios. To address these limitations, we propose ROADGS-T, a robust and efficient large-scale road surface mapping framework based on adaptive meshgrid Gaussian representation. Specifically, we model the road surface by placing 2D Gaussian surfels on a meshgrid, where each surfel explicitly stores color, semantic, and geometric information. Compared with conventional mesh-based representations and 3D Gaussian primitives, the proposed meshgrid Gaussian representation better matches the thin-surface property of roads while significantly reducing redundant primitives and overlap during optimization. To further improve representation efficiency and structural fidelity, we introduce a road-structure-aware adaptive meshgrid strategy, which allocates denser Gaussian surfels to geometrically or semantically complex regions, such as lane markings, road boundaries, and height discontinuities, while maintaining a compact representation in flat road areas. Moreover, instead of relying on a single nearest vehicle pose, we design a trajectory-consistency-guided pose-robust refinement strategy, which estimates local surface priors from multiple neighboring poses and adaptively weights pose-guided height regularization according to their geometric consistency.

</details>

#### 2026-07-16 - Rotational Motion-Induced Error Compensation for Phase-Shifting Profilometry-Based Eye Reconstruction

**Authors:** Seong-Jin An, Sanghoon Jeon, Yatong An, Jae-Sang Hyun
**Links:** [abs](https://arxiv.org/abs/2607.14876) - [pdf](https://arxiv.org/pdf/2607.14876)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** dynamic 3D, surface reconstruction, AR, augmented reality, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rotational Motion-Induced Error Compensation for Phase-Shifting Profilometry-Based Eye Reconstruction  
- 作者：Seong-Jin An, Sanghoon Jeon, Yatong An, Jae-Sang Hyun  
- 出版日期：2026-07-16  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.14876  

### 一句话总结
本文提出了一种基于旋转运动补偿的框架，用于消除相位偏折轮廓术（PSP）在动态人眼重建中因眼球旋转导致的测量误差。

### 研究问题
如何补偿眼球旋转引起的帧间运动误差，从而提高基于PSP的动态三维眼部重建的准确性和稳定性。

### 核心思路/方法
1. **运动估计**：从图像运动线索中，利用用户特定的三维眼球模型在球坐标系下估计相对眼球旋转。  
2. **误差补偿**：根据估计的运动，补偿因帧间旋转导致的相机像素错位和相位偏移误差。  
3. **区域优化**：引入分区域优化策略，对不同眼部区域独立调整补偿强度，以减少残余伪影。

### 主要贡献
- 提出了一种专门针对眼球旋转运动误差的补偿框架，显著抑制了运动引起的变形，提升了重建精度。  
- 通过旋转假眼实验验证了方法的有效性，并在非球形刚体实验中表明补偿原理不局限于球形眼球几何结构。  
- 为未来沉浸式环境中的高精度动态眼动追踪提供了实用基础。

### 局限性
摘要未提供足够信息。具体局限性包括：实验仅使用旋转假眼和非球形刚体，未提及真实人眼测试结果；未说明计算效率或实时性要求；未讨论不同旋转速度或复杂运动模式下的性能边界。

### 阅读优先级
**高**  
理由：该工作直接面向VR/AR中的高精度眼动追踪需求，针对动态三维重建中的核心运动误差问题提出了创新性解决方案，且通过实验验证了有效性。对于从事沉浸式显示、计算机视觉或精密测量领域的研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

With the proliferation of immersive Head-Mounted Displays (HMDs) for Virtual and Augmented Reality (VR/AR), reliable and high-precision eye tracking has become increasingly important. Conventional 2D image-based methods offer low system complexity but remain limited in stability, accuracy, and robustness. Three-dimensional ocular surface reconstruction can provide richer geomet-ric information, and structured light profilometry is particularly attractive because it enables dense and accurate surface measurement. However, Phase-Shifting Profilometry (PSP), which estimates phase from sequentially acquired fringe images, is highly susceptible to motion-induced errors when the eye rotates between frames. This study proposes a rotational motion compensation framework for PSP-based dynamic 3D eye reconstruction. Relative eye rotation is estimated from image-based motion cues using a user-specific 3D eye model in a spherical-coordinate domain. The estimated motion is then used to compensate for camera-pixel mismatch and phase-shift errors caused by inter-frame rotation. A region-wise optimization strategy is further introduced to reduce residual artifacts by inde-pendently refining the compensation strength in different ocular regions. Experiments with a rotating fake eye under non-uniform motion demonstrate that the proposed method substantially suppresses motion-induced deformation and improves reconstruction accuracy. An additional experiment with a non-spherical rigid object indicates that the compensation principle is not restricted to spherical eye geometry. These results establish a practical basis for stable PSP-based dynamic 3D eye reconstruction toward future high-precision eye tracking in immersive environments.

</details>

#### 2026-07-16 - Variational Inference for Bird's Eye View Segmentation in Autonomous Driving

**Authors:** Jingyue Shi, Huaicheng Li, Junhui Zhao, Yanxiang Jiang
**Links:** [abs](https://arxiv.org/abs/2607.14710) - [pdf](https://arxiv.org/pdf/2607.14710)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Variational Inference for Bird‘s Eye View Segmentation in Autonomous Driving
- 作者：Jingyue Shi, Huaicheng Li, Junhui Zhao, Yanxiang Jiang
- 出版日期：2026-07-16
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.14710

### 一句话总结
该论文提出了一种基于变分推理和Transformer的鸟瞰图分割网络TVB，通过条件变分自编码器和归一化流来生成多个候选BEV地图，并利用注意力机制进行融合，在nuScenes和OPV2V数据集上取得了优越性能。

### 研究问题
如何有效融合多相机传感器数据，解决自动驾驶中复杂外部环境下鸟瞰图分割的难题。

### 核心思路/方法
1. 将BEV分割问题重构成变分推理框架。
2. 提出Transformer-based变分流变换网络（TVB），以条件变分自编码器（CVAE）为骨干网络，利用后验BEV监督隐式学习多相机视图到统一BEV地图的映射。
3. 在BEV地图生成过程中集成归一化流，以构建更复杂、更具表达力的概率分布，增强生成地图的真实性。
4. 设计BEV-注意力融合（BAF）模块，利用注意力机制自适应地融合多个候选BEV地图。

### 主要贡献
- 首次将变分推理框架引入BEV分割任务。
- 提出了TVB网络，结合CVAE、归一化流和注意力融合机制。
- 在nuScenes和OPV2V两个数据集上的实验表明，该方法在多相机BEV分割和车道环境感知中达到了优越性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由是：该工作针对自动驾驶中的BEV分割这一重要问题提出了新颖的变分推理框架，方法涉及CVAE、归一化流和注意力融合，具有技术亮点，且实验在两个数据集上验证。但由于摘要未提供详细定量对比结果，且缺乏对局限性、计算开销等关键信息的描述，因此优先级别设为中等，适合对BEV分割或变分方法感兴趣的读者进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

The bird's eye view (BEV) has emerged as a pivotal approach for environmental perception in autonomous driving, providing a unified spatial representation for vehicles. Nevertheless, despite BEV's significance in addressing the challenges inherent to autonomous driving, effectively fusing data from multiple camera sensors and operating in complex external driving environments remains a considerable challenge. To mitigate this issue, we recast the BEV segmentation problem within a variational inference framework. In this paper, we propose a novel transformer-based variational flow transformation network for BEV segmentation, denoted as TVB. Our architecture implicitly learns the mapping from multiple camera views to a unified canonical BEV map during training by exploiting posterior BEV supervision. TVB employs a conditional variational auto encoder (CVAE) as its backbone and produces multiple BEV map candidates. To augment the realism of the generated BEV maps, we integrate normalizing flows into the map generation process, enabling the construction of more complex and expressive probability distributions. Furthermore, we design a BEV-attention fusion (BAF) module that harnesses attention mechanisms to adaptively integrate the multiple candidate BEV maps. Experimental results, evaluated on both the nuScenes and OPV2Vdatasets, demonstrate that our proposed method achieves superior performance in multi-camera view BEV segmentation and lane environment perception.

</details>

#### 2026-07-15 - Dynamic Manipulation Hypergraphs for HAR: Beyond Pairwise Relations: Dynamic Manipulation Hypergraphs for Vision-Based Human Activity Recognition

**Authors:** Fatemeh Ziaeetabar
**Links:** [abs](https://arxiv.org/abs/2607.14350) - [pdf](https://arxiv.org/pdf/2607.14350)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dynamic Manipulation Hypergraphs for HAR: Beyond Pairwise Relations: Dynamic Manipulation Hypergraphs for Vision-Based Human Activity Recognition  
- 作者：Fatemeh Ziaeetabar  
- 出版日期：2026-07-15  
- 分类：Embodied / Robotics / AR Applications  
- 链接：摘要: https://arxiv.org/abs/2607.14350 ; PDF: https://arxiv.org/pdf/2607.14350  

### 一句话总结
本文提出一种动态操作超图框架，将人手、物体、工具和支撑面等多实体交互建模为高阶关系单元，通过超图推理网络和时序注意力机制，在细粒度操作识别任务上显著超越传统成对图或静态超图方法。

### 研究问题
如何通过建模随时间变化的多实体高阶关系（而非仅成对边），提升基于视觉的细粒度人机操作活动识别（如手与物体、工具、支撑面的交互）性能。

### 核心思路/方法
1. **超图构建**：在每个时间步，将实体（手、物体、工具、支撑面）用外观、空间、运动和语义角色特征编码，并基于邻近性、接触和运动耦合谓词生成候选超边，通过排序得到高阶关系单元。  
2. **超图推理网络**：执行节点到超边以及超边到节点的消息传递，捕捉多实体间的结构化交互。  
3. **时序注意力**：对演化的交互结构施加时序注意力机制，聚焦关键时间区间。  
4. **评估协议**：在EPIC-KITCHENS-100/VISOR和Assembly101上使用注释辅助的实体定位协议，并与视频/实体基线、成对图、静态超图进行对照。  
5. **定性分析**：在ARCTIC数据集上展示高排名超边与接触密集操作区间的对应关系。

### 主要贡献
1. 提出动态操作超图框架，将多实体交互表示为随时间变化的高阶关系单元，替代传统成对图。  
2. 在EPIC-KITCHENS-100/VISOR上，HO-F1指标比配对的成对图提升6.9个百分点，比静态超图提升4.4个百分点；在Assembly101上分别提升9.5和5.8个百分点。  
3. 提供类无关的超边重要性分数，可识别模型强调的实体配置和时间区间，但不作为因果解释。  
4. 在ARCTIC上的定性分析验证了高阶关系与接触密集操作间的对应性。

### 局限性
摘要未提供足够信息，如计算复杂度、对实体检测或注释的依赖程度、在无注释条件下的性能、或对噪声实体识别的鲁棒性等。

### 阅读优先级
**高**  
理由：该工作针对细粒度人机操作识别的关键难点（多实体动态高阶关系），提出有结构创新的超图框架，在多个数据集上取得显著性能提升（6.9-9.5个百分点），且定性分析直观。对从事活动识别、人机交互、具身智能研究的读者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Fine-grained manipulation recognition requires modeling evolving relations among hands, objects, tools, and supporting surfaces. Conventional graph-based methods use pairwise edges that can fragment a coordinated event into disconnected binary relations. We propose a dynamic manipulation hypergraph framework that represents multi-entity configurations as higher-order relational units. At each temporal step, relevant entities are encoded using appearance, spatial, motion, and semantic-role features. Hyperedge candidates are instantiated and ranked using proximity, contact, and motion-coupling predicates. A hypergraph reasoning network performs node-to-hyperedge and hyperedge-to-node message passing, followed by temporal attention over the evolving interaction structure. The framework provides class-agnostic hyperedge-importance scores that identify entity configurations and temporal intervals emphasized by the model without treating them as causal explanations. Quantitative evaluation is conducted on EPIC-KITCHENS-100/VISOR and Assembly101 under an annotation-assisted entity-localization protocol. Video-only and entity-based methods provide contextual comparisons, while a matched pairwise graph and a static hypergraph serve as the principal controlled baselines because they use identical entity inputs and comparable relational settings. The proposed method improves HO-F1 over the matched pairwise graph by 6.9 percentage points on EPIC-KITCHENS-100/VISOR and 9.5 points on Assembly101, and exceeds the static hypergraph by 4.4 and 5.8 points, respectively. Qualitative analysis on ARCTIC further shows correspondence between highly ranked hyperedges and contact-rich manipulation intervals. These results demonstrate the value of time-varying higher-order relational modeling for fine-grained manipulation activity recognition.

</details>

#### 2026-07-15 - S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving

**Authors:** Jianguo Yu, Rukang Wang, Duanfeng Chu, Chen Wang, Renju Feng, Liping Lu
**Links:** [abs](https://arxiv.org/abs/2607.13926) - [pdf](https://arxiv.org/pdf/2607.13926)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving
- 作者：Jianguo Yu, Rukang Wang, Duanfeng Chu, Chen Wang, Renju Feng, Liping Lu
- 出版日期：2026-07-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.13926

### 一句话总结
本文提出S-squared-VLA框架，通过解耦视觉-语言-动作模型中的语义流与空间流，缓解了传统VLA模型因空间表征崩溃导致的低层级控制精度不足问题，在NAVSIM闭环基准上取得新最优性能。

### 研究问题
传统视觉-语言-动作（VLA）模型在自动驾驶中因离散语言标记与连续轨迹规划之间的语义-物理鸿沟，导致空间表征崩溃，从而难以生成精确的低层级控制动作。如何有效解耦语义与空间信息流，提升VLA模型的细粒度空间感知与轨迹规划能力。

### 核心思路/方法
1. **双流解耦架构**：显式分离语义流与空间流。
   - 语义流：采用层级桥接提取多尺度VLM特征，用于鲁棒的意图推理。
   - 空间流：独立绕过自回归语言瓶颈，直接保留来自视觉编码器的未压缩空间特征，并引入辅助感知监督以增强几何先验。
2. **双流规划适配器**：通过级联注意力机制融合高层语义意图与精确空间约束，生成最终控制动作。

### 主要贡献
- 提出S-squared-VLA，首次在VLA模型中显式解耦语义与空间流，解决空间表征崩溃问题。
- 在NAVSIM闭环基准上，S-squared-VLA在纯监督微调（SFT）设置下达到PDMS 87.1，创下VLA模型新最优；No Collision（NC）率达到98.4，超越所有评估方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文直面自动驾驶VLA模型的关键瓶颈（空间表征崩溃），提出新颖的显式解耦架构，并在标准闭环基准上取得显著领先性能。对于从事自动驾驶、视觉-语言动作模型或多模态控制的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action (VLA) architectures attempt to bridge this gap by unifying perception and control into a single policy, this entanglement creates a new bottleneck. Standard VLAs experience a severe spatial representation collapse, which irreversibly degrades the fine-grained spatial and geometric priors essential for safe, boundary-aware navigation. To address this limitation, we propose the S-squared-VLA, which explicitly decouples the semantic and spatial streams in Vision-Language-Action models. The semantic stream leverages hierarchical bridging to extract multi-scale VLM features for robust intent reasoning. In parallel, an independent spatial stream bypasses the autoregressive language bottleneck, directly preserving uncompressed spatial features from the visual encoder. By integrating auxiliary perception supervision, this stream explicitly equips the model with rich spatial and geometric priors. Finally, a dual-stream planning adapter fuses high-level semantic intent with precise spatial constraints via cascaded attention mechanisms. Evaluations on the NAVSIM closed-loop benchmark show that S-squared-VLA achieves a Predictive Driver Model Score (PDMS) of 87.1, establishing a new state-of-the-art for VLA models under a purely supervised fine-tuning (SFT) setting. By mitigating the spatial representation collapse of traditional VLMs, our framework significantly outperforms baselines, achieving the highest No Collision (NC) rate of 98.4 among all evaluated methods.

</details>

#### 2026-07-15 - Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning

**Authors:** Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen, Qingze Guan, Zhengxing Wu, Wanke Zhan, Yang Sun, Zhiyi Huang, Zitong Shan, Zhenchao Jin, Jiadong Hong, Taowen Wang, Yushi Feng, You Liu, Yibo Wang, Yifan Yang, Zhaowen Zhou, Man Luo, Hao Cheng, Bo Zhang, Jianshu Li, Jiansheng Cai, Guocai Yao, Jize Zhang, Chenhao Lin, Renjing Xu, Lequan Yu, Chao Shen, Chunhua Shen, Zhe Li
**Links:** [abs](https://arxiv.org/abs/2607.14183) - [pdf](https://arxiv.org/pdf/2607.14183)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning
- 作者：Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen, Qingze Guan, Zhengxing Wu, Wanke Zhan, Yang Sun, Zhiyi Huang, Zitong Shan, Zhenchao Jin, Jiadong Hong, Taowen Wang, Yushi Feng, You Liu, Yibo Wang, Yifan Yang, Zhaowen Zhou, Man Luo, Hao Cheng, Bo Zhang, Jianshu Li, Jiansheng Cai, Guocai Yao, Jize Zhang, Chenhao Lin, Renjing Xu, Lequan Yu, Chao Shen, Chunhua Shen, Zhe Li
- 出版日期：2026-07-15
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2607.14183 | PDF：https://arxiv.org/pdf/2607.14183

### 一句话总结
Open-AoE是一个面向具身学习的开放、社区导向的自我中心操作数据集与工具链，包含约2000小时的自然环境人体操作视频及从数据采集到模型训练的完整流水线。

### 研究问题
当前缺乏一种结合低成本连续采集、操作级结构化标注和可复用工具的具身智能资源，以支持从人类视频到机器人学习的高效转化。

### 核心思路/方法
1. **数据集构建**：利用500+名贡献者使用400+部智能手机在自然环境中采集约2000小时的自我中心操作视频。
2. **结构化标注**：为视频提供文本描述、基于MANO的手部姿态、相机轨迹以及时间上局域化的原子动作标注。
3. **数据处理流水线**：包含时间动作分割、语义标注、手部重建和相机轨迹重建，将原始录像转化为结构化样本。
4. **下游工具链**：支持可视化、跨本体重新定位、特定模型数据转换，并提供VLA策略、WAMs和世界模型的训练方案。

### 主要贡献
1. 提供了一个大规模（约2000小时）、低成本、由社区贡献的自我中心操作数据集。
2. 建立了一套从智能手机采集到模型训练、具有完整标注和工具链的开放基础设施。
3. 整合了可扩展数据采集、结构化处理和下游适应，降低了数据贡献与复用的门槛。

### 局限性
摘要未提供足够信息。未提及数据集的具体覆盖动作类型、标注质量验证、训练模型性能评估结果或与现有数据集的对比分析细节。

### 阅读优先级
高。该工作为具身学习领域提供了大规模、开放且实用的基础设施，并结合了从数据到模型训练的全流程工具链，对需要低成本数据资源的研究者或从事人机迁移、世界模型研究的团队具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning. We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training. Its first release contains approximately 2,000 hours of manipulation video collected in natural environments by 500+ contributors using 400+ smartphones. The dataset provides text annotations, MANO-based hand poses, camera trajectories, and temporally localized atomic actions. Open-AoE further includes a data processing pipeline that transforms raw recordings into structured samples through temporal action segmentation, semantic annotation, hand reconstruction, and camera trajectory reconstruction. Meanwhile, we provide a separate downstream toolchain supports visualization, cross-embodiment retargeting, model-specific data conversion, and training recipes for VLA policies, WAMs, and World Models. By integrating scalable capture, structured processing, and downstream adaptation, Open-AoE reduces the barriers to both data contribution and reuse, providing practical open infrastructure for embodied model training, human-to-robot transfer, and world modeling.

</details>

#### 2026-07-15 - UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets

**Authors:** Xian Li, Rong Wei, Lujie Yang, Haolin Huang, Junyuan Fang, Siliang Tang, Jun Xiao, Rui Tang, Juncheng Li
**Links:** [abs](https://arxiv.org/abs/2607.13586) - [pdf](https://arxiv.org/pdf/2607.13586)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets
- 作者：Xian Li, Rong Wei, Lujie Yang, Haolin Huang, Junyuan Fang, Siliang Tang, Jun Xiao, Rui Tang, Juncheng Li
- 出版日期：2026-07-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.13586

### 一句话总结
本文提出UniPhysGen框架，利用UniPhys方法自动将原始3D资产转换为具备统一物理语义（关节语义与内在物理属性）的仿真就绪资产，并构建了大规模数据集与基准。

### 研究问题
如何使现有3D资产自动获得统一的物理语义（包括关节语义和内在物理属性），从而支持具身AI与机器人仿真中的真实交互。

### 核心思路/方法
- 提出UniPhys，一个可扩展的框架，用于自动将原始3D资产转换为具有统一物理语义的仿真就绪资产。
- 基于UniPhys构建了大规模物理语义数据集UniPhys-40K和验证基准UniPhys-Bench。
- 引入UniPhysGen模型，联合推理关节语义和内在物理属性。
- 通过几何鲁棒的关节语义推理，减轻异质部件分解下的几何捷径偏差。

### 主要贡献
1. 提出UniPhys框架，自动化将原始3D资产转换为具备统一物理语义的仿真就绪资产。
2. 构建大规模物理语义数据集UniPhys-40K及验证基准UniPhys-Bench。
3. 提出UniPhysGen模型，在关节语义推理和内在物理属性估计任务上达到最优性能，所得资产可直接部署在机器人仿真环境中。

### 局限性
摘要未提供有关局限性或失败案例的足够信息。

### 阅读优先级
高  
理由：该工作针对具身AI和机器人仿真中3D资产物理语义缺失的关键问题，提供了自动化、可扩展的解决方案，并构建了大规模数据集与基准，实验性能达到最优。对于从事仿真、机器人学或3D场景理解的读者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Physically grounded 3D assets are increasingly important for embodied AI and robotic simulation. However, most existing 3D assets lack unified physical semantics, including articulation semantics and intrinsic physical properties, required for realistic interaction. Current approaches either treat these semantics independently or rely on canonicalized object structures, limiting robustness across heterogeneous 3D assets. We present UniPhys, a scalable framework for automatically transforming raw 3D assets into simulation-ready assets with unified physical semantics. Based on UniPhys, we construct UniPhys-40K, a large-scale physically grounded dataset, together with UniPhys-Bench, a carefully verified benchmark for unified physical grounding evaluation. We further introduce UniPhysGen, a unified physical grounding model that jointly reasons over articulation semantics and intrinsic physical properties. UniPhysGen incorporates geometry-robust articulation grounding to mitigate geometric shortcut bias under heterogeneous part decompositions. Extensive experiments demonstrate state-of-the-art performance across articulation grounding and intrinsic physical property estimation tasks, while the resulting assets can be directly deployed in robotic simulation environments for realistic physical interaction. Our code and dataset will be available at https://github.com/breezexian/UniPhysGen.

</details>

#### 2026-07-15 - GPOcc++: Unified Sparse Gaussian Occupancy Prediction with Visual Geometry Priors

**Authors:** Changqing Zhou, Yueru Luo, Yulan Guo, Bing Wang, Jie Qin, Changhao Chen
**Links:** [abs](https://arxiv.org/abs/2607.13481) - [pdf](https://arxiv.org/pdf/2607.13481)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GPOcc++: Unified Sparse Gaussian Occupancy Prediction with Visual Geometry Priors
- 作者：Changqing Zhou, Yueru Luo, Yulan Guo, Bing Wang, Jie Qin, Changhao Chen
- 出版日期：2026-07-15
- 分类：Embodied / Robotics / AR Applications
- 链接：abstract: https://arxiv.org/abs/2607.13481, pdf: https://arxiv.org/pdf/2607.13481

### 一句话总结
GPOcc++提出一种统一稀疏高斯占用预测框架，利用视觉几何先验，将表面中心输出转化为体素占用感知表示，并在室内外场景中实现高效、泛化强的占用预测。

### 研究问题
如何利用视觉几何先验（其输出本质是表面中心）来补全视觉观测中遮挡和未观察区域的3D占用（需要推理体素内部和自由空间），实现准确的3D场景理解。

### 核心思路/方法
- **GPOcc基础**：将视觉几何先验转换为占用感知的稀疏高斯表示，用于高效表达体场景建模。
- **GPOcc++扩展**：将多视角观测和时间序列以统一框架建模，使用相同表示处理空间和时间证据。
- **场景延伸**：从室内场景扩展至室外占用预测。
- **验证**：在室内外基准上对多视角和时间设置进行实验，验证性能、效率和泛化性。

### 主要贡献
1. 引入GPOcc，将视觉几何先验转化为占用感知的稀疏高斯表示，弥合表面中心输出与体占用推理之间的差距。
2. 提出GPOcc++，在多视角和时间序列设置下实现统一框架，支持空间和时间证据的同表示处理。
3. 将方法从室内扩展到室外占用预测，并在多个基准上展示一致强性能、效率和泛化性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文研究了3D占用预测中的关键挑战（从表面到体积的转换），并提出统一、高效的框架，适用于室内外场景，且实验显示跨设置一致性表现。对于致力于3D场景理解、自动驾驶和具身智能的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate 3D scene understanding is fundamental to embodied intelligence and autonomous driving, where 3D occupancy provides a unified representation of objects, structures, and free space. However, recovering such a complete volumetric representation from visual observations remains challenging, particularly in occluded and unobserved regions. Visual geometry priors offer strong and generalizable geometric cues for addressing this challenge, but their outputs are inherently surface-centric, whereas occupancy prediction requires reasoning about volumetric interiors and free space. To bridge this gap, we introduce GPOcc, which transforms visual geometry priors into occupancy-aware sparse Gaussian representations for efficient and expressive volumetric scene modeling. Building on GPOcc, GPOcc++ models multi-view observations and temporal sequences within a unified framework, allowing spatial and temporal evidence to be handled through the same representation. We further extend GPOcc++ from indoor scenes to outdoor occupancy prediction. Extensive experiments on both indoor and outdoor benchmarks demonstrate consistently strong performance across both multi-view and temporal settings, together with favorable efficiency and generalization. Code will be released at https://github.com/JuIvyy/GPOcc.

</details>

#### 2026-07-15 - Marker-free deformable registration and fusion for augmented reality-guided positive margin localization during tumor resection surgery

**Authors:** Yue Yang, Annie Benson, Matthieu Chabanas, Jason Slagle, Thomas Myles, Matthew B. Weinger, Jon S. Heiselman, Michael I. Miga, Michael Topf, Jie Ying Wu
**Links:** [abs](https://arxiv.org/abs/2607.13343) - [pdf](https://arxiv.org/pdf/2607.13343)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization, AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Marker-free deformable registration and fusion for augmented reality-guided positive margin localization during tumor resection surgery
- 作者：Yue Yang, Annie Benson, Matthieu Chabanas, Jason Slagle, Thomas Myles, Matthew B. Weinger, Jon S. Heiselman, Michael I. Miga, Michael Topf, Jie Ying Wu
- 出版日期：2026-07-15T00:06:52Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.13343

### 一句话总结
本文提出了一种无标记增强现实(AR)工作流，用于在头颈肿瘤切除手术中，将样本切片的阳性边缘定位映射到患者切除床，并在尸体实验中展示了比传统口头指导更低的定位误差。

### 研究问题
如何在没有外部标记物的情况下，将标本病理切片上的阳性边缘标记准确映射到手术切除床，并配合AR显示减小定位误差，改善头颈肿瘤手术中阴阳性边缘的定位精度。

### 核心思路/方法
该方法结合了多个步骤：
1. 对切除后的三维标本扫描进行轮廓约束变形。
2. 将变形后的标本与切除床的深度扫描进行残差对齐。
3. 通过无标记表面配准将信息融合到头戴显示器中。
4. 目标投影到重建的切除床上。利用缝合线对应点估计标本变形；患者与显示器的融合不依赖外部标记。
5. 在尸体实验中将本方法与口头指导、口头指导加标本检查进行对比，评估变形误差、融合误差和端到端边缘定位误差。

### 主要贡献
- 提出并验证了一个无标记的AR工作流，成功将阳性边缘从标本扫描映射到患者切除床。
- 在尸体实验中，端到端边缘定位误差从口头指导的21.40 mm和标本检查的16.09 mm显著降低至AR指导的6.19 mm（p < 0.001）。
- 无标记融合误差为2.15 ± 0.87 mm，与有标记方法无显著差异；在线融合仅需5.23秒。
- 展示了该工作流在更精确肿瘤切除方面的临床潜力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。
理由：该方法直接解决临床头颈肿瘤手术中阳性边缘定位的痛点，实验结果（误差降低至6.19 mm）显示出显著改进，且无标记设计增强了临床应用便利性。属于应用导向的优质工作，对于从事AR手术导航、医学图像配准和肿瘤外科研究的读者具有高参考价值。

</details>

<details>
<summary>Abstract</summary>

Positive margins in head and neck oncologic surgery require mapping specimen-side pathology findings to the patient resection bed. This is challenging because pathologists identify the positive margin on slices of the resected, deformed specimen, while surgeons must relocate the corresponding site on the resection bed using only verbal descriptions and no visual guidance. We present a marker-free augmented reality (AR) workflow for mapping a margin label from a three-dimensional specimen scan to the resection bed. The method combines contour-constrained deformation, residual alignment to a depth scan, surface-based fusion to a head-mounted display, and target projection onto the reconstructed bed. Bead-suture correspondences estimate specimen deformation, whereas patient-to-display fusion does not require external fiducial markers. Following formative experiments, five residents and surgeons performed cadaveric cheek and scalp re-resection tasks under verbal guidance, verbal guidance with specimen examination, and AR guidance. Deformation target errors were $7.63 \pm 3.74$ mm for the cheek and $3.72 \pm 1.02$ mm for the scalp; residual specimen-to-bed distances were $2.43 \pm 2.15$ mm and $2.19 \pm 1.06$ mm, respectively. Fusion error did not differ significantly between marker-free and marker-based methods on either cadaver; overall marker-free fusion error was $2.15 \pm 0.87$ mm. End-to-end margin localization error decreased from $21.40 \pm 3.84$ mm with verbal guidance and $16.09 \pm 4.30$ mm with specimen examination to $6.19 \pm 1.79$ mm with AR guidance ($p < 0.001$). Online fusion required $5.23 \pm 0.34$ s. These results demonstrate effective marker-free AR guidance for positive-margin localization and support more precise tumor resection.

</details>

#### 2026-07-14 - TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

**Authors:** Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee, Tim Wang, Wei Zhan
**Links:** [abs](https://arxiv.org/abs/2607.13028) - [pdf](https://arxiv.org/pdf/2607.13028)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale
- 作者：Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee, Tim Wang, Wei Zhan
- 出版日期：2026-07-14
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.13028

### 一句话总结
TerraZero 是一个程序化生成驾驶场景的模拟器及自博弈训练框架，能在无人类示范和无后备规划器的情况下，从头训练出直接部署到多城市数据集、并在长尾和常规驾驶基准上达到顶尖安全表现的完全学习型驾驶策略。

### 研究问题
如何构建一个模拟器，使其兼具大规模强化学习所需的运行速度、基于真实地图结构的保真度，以及能覆盖安全关键长尾场景的多样性，从而训练出零人类示范、零后备规划器的鲁棒自动驾驶策略。

### 核心思路/方法
- **模拟器设计**：采用基于 C 引擎的配置式架构，在 CPU 上运行仿真，通过零拷贝路径在 GPU 上执行策略推理，实现每秒 130 万代理步长的速度。同时保持高保真度（异质代理、多种动力学模型、完整交通规则）。
- **场景生成**：仅利用日志数据提供真实世界地图几何信息，每个地图上随机生成基于规则的交通参与者、信号控制器，并随机化代理动力学、奖励和尺寸，从而每张地图产生无限多样化场景。
- **训练范式**：通过仅依赖强化学习的自博弈配方，在多个 GPU 上从零开始训练策略，全程无人类示范和推理时的后备规划器。

### 主要贡献
- 提出首个完全学习型策略 TerraZero，在 InterPlan 长尾基准上超越更大规模学习规划器，位列第一。
- 在常规驾驶基准 val14 上，此策略在碰撞及碰撞时间指标上取得最佳成绩，被认为最安全。
- 在 Waymo Open Sim Agents 真实性评估中，该配方优于其他无示范方法，并与最强的参考锚定自博弈方法竞争。
- 策略展现出零样本跨城市和数据集泛化能力，包括在无显式监督下涌现左侧行驶能力。
- 同一框架可同时训练驾驶策略（支持不同动力学的小车和卡车）和模拟代理（控制车辆、行人、自行车手）。

### 局限性
摘要未提供足够信息来描述该方法的局限性，例如在哪些极端场景下可能失效、计算资源需求、或与传统基于规则的模拟器在特定任务上的对比失败案例。

### 阅读优先级
**高**  
理由：该工作提出了一个在速度和多样性上都有显著提升的驾驶模拟器，并在长尾和常规基准上取得了领先的性能和安全性，同时展现了零样本泛化能力，对自动驾驶领域的大规模强化学习研究具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per second on a single server-grade GPU, far faster than existing object-level simulators, while keeping fidelity lighter single-agent systems omit: heterogeneous agents, multiple dynamics models, and full traffic-rule enforcement. TerraZero treats logged data only as a source of real-world map geometry, populating each map with randomized rule-based road users and signal controllers and randomizing agent dynamics, rewards, and sizes per episode, so a map yields an unbounded set of scenarios. Every reported policy trains from scratch by reinforcement learning alone on a compute-efficient self-play recipe across GPUs, with zero human demonstrations and no fallback planner at inference. Policies generalize zero-shot across cities and datasets, including emergent left-hand-traffic driving without explicit supervision. As an ego policy, TerraZero is the first fully learned policy to top the InterPlan long-tail benchmark, ahead of larger learned planners; on routine-driving val14 it ranks among the best approaches and is the safest, posting the best collision and time-to-collision scores. On Waymo Open Sim Agents realism the same recipe outperforms other demonstration-free methods and is competitive with the strongest reference-anchored self-play method. One stack serves both roles: driving policies across dynamics for cars and trucks, and sim agents that jointly control vehicles, pedestrians, and cyclists.

</details>

#### 2026-07-14 - More Than Where You Are: Learning Semantics, Structure, and Geometry from Cross-View Localization

**Authors:** Mao Chen, Xiangkai Zhang, Zhiyong Liu, Chuankai Liu, Xu Yang
**Links:** [abs](https://arxiv.org/abs/2607.12429) - [pdf](https://arxiv.org/pdf/2607.12429)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reasoning, pose estimation, localization, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：More Than Where You Are: Learning Semantics, Structure, and Geometry from Cross-View Localization
- 作者：Mao Chen, Xiangkai Zhang, Zhiyong Liu, Chuankai Liu, Xu Yang
- 出版日期：2026-07-14
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.12429

### 一句话总结
本文提出CROSS框架，将跨视角定位问题重新定义为不仅仅是位姿估计，而是学习跨极端视角变化的稳定语义、可靠结构和可迁移几何。

### 研究问题
如何克服现有跨视角定位方法在极端视角变化下缺乏3D基础、依赖严格点匹配削弱语义一致性、以及绝对目标对几何推理指导有限等局限性，以建立一致的跨视角理解能力。

### 核心思路/方法
提出CROSS统一框架，通过三个关键组件来解决上述局限性：
1. **3D基础对齐（3D-grounded alignment）**：引入明确的3D基础，使结构学习成为内在需求。
2. **结构感知匹配（structure-aware matching）**：替代严格点匹配，鼓励语义表示保持稳定。
3. **假设排序（hypothesis ranking）**：提供更灵活的几何推理指导，使模型获得可迁移的几何能力。

### 主要贡献
1. 重新定义了跨视角定位的目标，即学习跨视角的稳定语义、可靠结构和可迁移几何，而不仅是位姿估计。
2. 识别并克服了现有方法的三大关键局限性。
3. 提出CROSS框架，在KITTI和VIGOR数据集上达到跨视角定位的最新性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文直接回应了跨视角定位在极端视角变化下的核心挑战，提出统一框架并在多个数据集取得最优结果，对空间智能、机器人及增强现实应用具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Consistent cross-view understanding under extreme viewpoint changes is essential for spatial intelligence, as it enables models to recognize the same scene across extreme viewpoint gaps. Cross-view localization naturally provides a promising pathway toward this ability, as it requires a model to align ground-view imagery with geo-referenced satellite-view imagery despite drastic appearance changes to estimate camera poses. Recent visual foundation models have made this long-standing localization problem increasingly feasible by providing rich 2D representations for cross-view matching. However, we argue that cross-view localization should not be viewed merely as 2D matching or pose estimation. In this work, we revisit cross-view localization as more than pose estimation and investigate how it can help the model develop consistent cross-view understanding under extreme viewpoint changes, including stable semantics, reliable structure, and transferable geometry. We identify three key limitations of existing methods that prevent them from achieving this. They usually lack explicit 3D grounding, rely on strict point-wise matching that can weaken semantic consistency, and learn from an absolute objective that provides limited guidance for geometric reasoning. To address these limitations, we propose CROSS, a unified cross-view localization framework built upon 3D-grounded alignment, structure-aware matching, and hypothesis ranking. This formulation makes structure learning an intrinsic requirement, encourages semantic representations to remain stable, and enables the model to acquire transferable geometry. Extensive experiments on the KITTI and VIGOR datasets show that CROSS achieves state-of-the-art performance in cross-view localization. More importantly, CROSS effectively learns stable semantics, reliable structure, and transferable geometry across extremely different viewpoints.

</details>

#### 2026-07-14 - VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation

**Authors:** Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang
**Links:** [abs](https://arxiv.org/abs/2607.12356) - [pdf](https://arxiv.org/pdf/2607.12356)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation
- 作者：Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang
- 出版日期：2026-07-14
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.12356

### 一句话总结
VistaVLA提出一种两阶段框架，通过将多视图视觉-语言特征提升为3D高斯基元并压缩为紧凑语义令牌，使VLA模型获得几何与语义感知的3D认知表示，显著提升机器人操作任务的成功率。

### 研究问题
现有的视觉-语言-动作（VLA）模型缺乏显式的场景级3D表示，难以对空间布局和几何约束进行推理；仅引入深度图或点云等方法虽增强了几何感知，但缺少3D空间中的高层语义信息，限制了机器人与物理世界的交互认知能力。

### 核心思路/方法
1. **3D高斯基元构建**：将多视图视觉-语言特征投影到3D高斯基元中，形成几何锚定的语义令牌，建立与视图一致的3D空间映射与2D视觉特征空间的联系。
2. **Merge-then-Query（MtQ）令牌压缩**：设计一种令牌摘要机制，将密集的3D高斯基元压缩为一组高度紧凑的空间信息令牌，实现99%的令牌缩减，同时保留与动作相关的3D布局和语义上下文。
3. **两阶段框架**：第一阶段构建几何与语义感知的3D认知表示，第二阶段将该表示作为紧凑的上下文令牌输入VLA策略学习网络。

### 主要贡献
- 提出首个构建几何与语义感知3D认知表示的VLA框架，用于机器人操作任务。
- 设计MtQ机制，实现密集3D高斯基元到紧凑令牌的高效压缩，显著降低计算开销。
- 在仿真和真实世界环境中验证有效性：真实场景下，在7个任务上平均成功率提升22.8%，在分布外任务上比VLA-Adapter基线提升30.0%。

### 局限性
摘要未提供关于模型泛化能力、计算复杂度、失败模式分析或更多实验设置（如训练数据规模、实时性）的详细信息。

### 阅读优先级
**高**  
理由：该工作在VLA模型领域引入了创新的3D认知表示方法，并结合高效的令牌压缩技术，在真实环境中取得了明显的性能提升，对机器人操作与具身智能研究具有较强的参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions. However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints. While recent efforts incorporate explicit 3D cues, such as depth maps or point clouds, to improve geometric awareness, they primarily capture low-level structures and lack high-level semantic grounding in 3D space. In human cognition, interaction with the physical world relies on a 3D semantic cognitive map - an internal mental model that integrates spatial layouts with semantic context to enable persistent, viewpoint-invariant reasoning. In light of this, we present VistaVLA, a novel two-stage framework that constructs a geometry- and semantics-aware 3D cognitive representation from 3D Gaussian primitives and grounds it as compact context tokens for VLA policy learning. Specifically, VistaVLA lifts multi-view vision-language features into 3D Gaussian primitives, forming geometry-anchored semantic tokens that align view-consistent spatial grounding with 2D visual feature spaces. To make this 3D representation computationally tractable for effective VLA control, we introduce Merge-then-Query (MtQ), a token summarization mechanism. MtQ compresses dense Gaussian primitives into a highly compact set of spatially informative tokens, achieving a 99% token reduction while preserving action-relevant 3D layouts and semantic context. Extensive evaluations in both simulated and real-world environments demonstrate the effectiveness of VistaVLA. Notably, in real-world scenarios, VistaVLA improves success rates by 22.8% across seven real-world tasks and by 30.0% over the VLA-Adapter baseline on challenging out-of-distribution tasks.

</details>

#### 2026-07-13 - Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model

**Authors:** Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li
**Links:** [abs](https://arxiv.org/abs/2607.11643) - [pdf](https://arxiv.org/pdf/2607.11643)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model
- 作者：Xinghang Li, Jun Guo, Qiwei Li 等
- 出版日期：2026-07-13
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.11643

### 一句话总结
本文介绍了一个380亿参数的多模态自回归模型，将基础图像/视频生成统一扩展到具身场景生成、具身迁移和具身视频生成，在单步与序列生成任务上达到最先进效果，并在真实世界操作任务中显著提升了策略的成功率。

### 研究问题
如何将大规模预训练的基础图像与视频生成模型的泛化能力和可控性，有效地迁移到具身场景中，同时满足多视角一致性、几何连贯性和机器人本体约束。

### 核心思路/方法
- 构建一个380亿参数的多模态自回归模型（Xiaomi-Robotics-U0）。
- 将具身生成视为基础图像与视频生成的扩展，统一优化文本到图像生成、图像编辑、具身场景生成、具身迁移和具身视频生成五个任务。
- 采用统一框架，在保留预训练世界基础模型泛化能力的同时，使其适应具身设定。
- 支持跨多种机器人本体的高质量多视角场景生成，并引入结构化、可控的具身迁移，实现细粒度编辑并保持多视角一致性与交互动态。

### 主要贡献
- 第一个支持多种机器人本体的高质量多视角场景生成的模型。
- 引入结构化、可控的具身迁移，实现细粒度编辑并保持多视角一致性。
- 在单步和序列生成任务上达到最先进结果：人类评估中在具身场景生成与迁移上优于GPT-Image-2.0；具身视频生成在World Arena排名第一；在真实世界操作任务中将 pi_0.5 的分布外成功率从36.9%提升至63.2%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作在具身智能建模中首次实现了多任务统一的巨大参数模型，并在多个任务上取得了显著的性能提升和实际部署验证，对具身场景生成、机器人数据引擎构建有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent foundation image and video generation models offer strong generalization and controllability, but their direct application to embodied scenarios is limited by requirements for multi-view consistency, geometric coherence, and robot embodiment constraints. Existing methods typically adapt foundation models with limited robot data, often sacrificing visual knowledge acquired during large-scale pre-training. We present Xiaomi-Robotics-U0, a 38-billion-parameter multimodal autoregressive model for unified embodied synthesis. It treats embodied generation as an extension of foundation image and video generation and jointly optimizes text-to-image generation, image editing, embodied scene generation, embodied transfer, and embodied video generation. This unified framework preserves the generalization of the pre-trained world foundation model while adapting it to embodied settings. Xiaomi-Robotics-U0 is the first model to support high-quality multi-view scene generation across multiple robot embodiments and to introduce structured, controllable embodied transfer for fine-grained editing while preserving multi-view consistency and interaction dynamics. It achieves state-of-the-art results on single-step and sequential generation tasks, outperforming GPT-Image-2.0 in human evaluations of embodied scene generation and transfer, ranking first on World Arena for embodied video generation, and improving the out-of-distribution success rate of pi_0.5 from 36.9% to 63.2% on challenging real-world manipulation tasks. These results show that foundation world models can serve both as embodied world models and scalable data engines for embodied intelligence. Code and checkpoints are available at https://robotics.xiaomi.com/xiaomi-robotics-u0.html.

</details>

#### 2026-07-13 - SegDiff: Segmented Trajectory Diffusion for Consistent and Adaptive Robot Manipulation

**Authors:** Haidong Cao, Wenjun Cao, Quanhao Li, Sicheng Xie, Zhiying Du, Jiaqi Leng, Zuxuan Wu, Yu-Gang Jiang
**Links:** [abs](https://arxiv.org/abs/2607.11027) - [pdf](https://arxiv.org/pdf/2607.11027)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SegDiff: Segmented Trajectory Diffusion for Consistent and Adaptive Robot Manipulation
- 作者：Haidong Cao, Wenjun Cao, Quanhao Li, Sicheng Xie, Zhiying Du, Jiaqi Leng, Zuxuan Wu, Yu-Gang Jiang
- 出版日期：2026-07-13
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页面 https://arxiv.org/abs/2607.11027 | PDF https://arxiv.org/pdf/2607.11027

### 一句话总结
本文提出SegDiff，一种结合连续轨迹预测与关键位姿预测优点的闭环视觉运动策略，利用扩散模型和DDIM反演实现长时间范围内的稳定、自适应的机器人操作。

### 研究问题
现有模仿学习方法分为两类：预测短视界连续动作序列（易累积误差且难以处理多模态动作分布）和预测离散关键位姿（需外部规划器，限制实时性）。本文旨在解决这两类方法各自的局限，实现既能长期预测又能实时自适应、控制稳定的操作策略。

### 核心思路/方法
1. **分段轨迹扩散**：将演示分解为关键位姿之间的运动片段，学习从当前状态到下一个关键位姿的连续轨迹预测，从而实现长视界预测并支持实时精化。
2. **动态时间集成机制**：利用扩散模型和DDIM反演的能力，提出一种机制，使策略能够高效响应动态环境，同时缓解因多模态采样不一致导致的轨迹不连续问题。整体策略为闭环视觉运动策略。

### 主要贡献
1. 提出SegDiff框架，集成连续轨迹与关键位姿两种范式的优势，提升长时依赖推理与实时适应性。
2. 引入动态时间集成机制，借助扩散模型与DDIM反演，增强对动态环境的响应能力并减少轨迹不连续性。
3. 在多个模拟和真实场景中，SegDiff相比现有方法取得了显著性能提升，验证了其在长期时间依赖推理、实时适应性和控制稳定性方面的优势。

### 局限性
摘要未提供足够信息：未明确讨论实验的失败案例、对特定任务/场景的局限性、计算成本、模型泛化边界或与其他方法的详细对比数据。

### 阅读优先级
**高**：理由：该论文针对机器人模仿学习中的核心矛盾（长视界预测与实时性、连续/离散预测的权衡）提出了创新性的融合方案，且方法在模拟和真实场景中均验证有效，对具身智能和机器人操作领域的研究具有潜在重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Imitation learning enables robots to acquire manipulation skills from demonstrations by mapping observations to actions. Existing approaches predict either short-horizon continuous action sequences or discrete keyposes. However, continuous prediction methods suffer from compounding errors due to short prediction horizons and struggle with multi-modal action distributions, whereas keypose-based methods necessitate an external planner, constraining real-time applicability. To address these challenges, we introduce SegDiff, a closed-loop visuomotor policy that integrates the strengths of both paradigms. SegDiff decomposes demonstrations into motion segments between keyposes and learns to predict the continuous trajectory from the current state to the next keypose, enabling long-horizon prediction with real-time refinement. Furthermore, we leverage the capability of diffusion models and DDIM inversion to propose a Dynamic Temporal Ensembling mechanism, which allows the policy to efficiently respond to dynamic environments and mitigate discontinuities caused by inconsistent multi-modal sampling. SegDiff demonstrates significant performance gains over existing approaches across various simulated and real-world scenarios, indicating its strong ability to reason over extended temporal dependencies while maintaining real-time adaptability and control stability.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
