# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：56
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 27
  - Embodied / Robotics / AR Applications: 14
  - Neural Scene Representations & Rendering: 8
  - Dynamic / 4D Reconstruction: 4
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的科研趋势综合分析报告。

---

#### 今日主要趋势

1.  **3D 高斯泼溅（3DGS）进入”效率与泛化”深水区**：3DGS 已不再满足于单场景过拟合优化，而是全面转向前馈式、可泛化、高效率和自适应的新范式。具体表现在：
    -   **前馈预测**：如 `HyperGS` 提出免优化直接预测视频的高斯表示。
    -   **非对称架构**：如 `AsySplat` 解耦几何与外观分支以节省长序列计算资源。
    -   **自适应复杂度**：如 `DP-Splat` 引入贝叶斯非参数先验，让高斯数量自动适应场景复杂度。
    -   **在线/增量重建**：`GeoGS-SLAM` 和 `Incremental Online Scene Reconstruction` 将 3DGS 与 SLAM 管线深度结合，追求实时、在线、可更新的重建能力。

2.  **”几何基础模型”成为稀疏/困难场景重建的破局点**：依靠纯2D光度损失难以解决深度歧义和几何退化问题，论文越来越倾向于引入预训练的几何基础模型来提供强几何先验或对应关系。
    -   `MAC-Splat` 利用 `MASt3R` 模型获得高质量3D对应关系作为几何锚点。
    -   `GeoGS-SLAM` 使用前馈视觉几何模型预测相机和场景先验。
    -   `GHOST` 利用视觉基础模型解决透明物体的几何退化问题。

3.  **从静态场景到动态/4D世界模型的统一建模**：科研趋势正从处理静态场景，转向构建可交互、可探索的动态世界模型，且输入模态趋于多模态化（文本、图像、视频）。
    -   `ABot-3DWorld 0` 构建了一个通用的“世界模型”，将任何输入转化为可探索的3D世界，并支持锚定到地理兴趣点。
    -   `OmniX` 将动态运动与静态几何解耦，实现大视角变化下的任意时刻4D重建。
    -   `Grassmannian Splatting` 提出了一种全新的运动表示单元，无需学习变形场即可渲染动态场景。

4.  **具身智能与机器人操作向“预训练基础模型 + 任务统一”发展**：机器人操作不再依赖单一任务训练，而是向着大规模、多任务、统一的预训练模型演进。
    -   `Xiaomi-Robotics-U0` 是一个380亿参数的多模态自回归模型，统一了从图像生成到具身场景、迁移和视频生成的全流程。
    -   `SegDiff` 则展示了如何将扩散模型与模仿学习结合，实现更稳定、自适应的长程操作策略。

#### 技术路线观察

| 方向 | 技术侧重点 | 代表论文 |
| :--- | :--- | :--- |
| **几何基础模型** | 强调从预训练模型中提取强几何先验（点云、深度、法线、对应关系），以弥补纯光度损失的不足。这些模型作为“几何锚点”被引入，而非端到端从头训练。 | `MAC-Splat`, `GeoGS-SLAM`, `GHOST` |
| **3D/4D 重建** | - **传统方法改进**：如 `IBPA` 改进经典BPA算法以适应实时增量场景。<br>- **3DGS优化**：关注效率 (`AsySplat`, `DP-Splat`)、泛化性 (`HyperGS`)、在线性 (`Incremental Online`)。<br>- **动态场景**：走向端到端的前馈轨迹场 (`OmniX`) 或新图元设计 (`Grassmannian Splatting`)。 | `IBPA`, `AsySplat`, `HyperGS`, `OmniX`, `Grassmannian Splatting` |
| **神经场景表示** | 3DGS 已成为绝对主流。当前路线图已从“如何优化”转向“如何更好地生成、组织和管理高斯体”。这催生了前馈网络 (`HyperGS`)、非参数先验 (`DP-Splat`) 和新参数化 (`Grassmannian Splatting`)。 | `HyperGS`, `DP-Splat`, `Grassmannian Splatting` |
| **机器人/AR应用** | - **具身生成**：关注点在于如何将视觉生成模型（文生图、视频）的泛化能力，适配到具身任务中，关键是保持多视角一致性和几何连贯性 (`Xiaomi-Robotics-U0`)。<br>- **SLAM与导航**：焦点是鲁棒性和效率，如利用CSI信号增强SLAM (`CSI-Assisted Edge SLAM`)，或轻量级描述符增强 (`Desc++`)。<br>- **操作策略**：`SegDiff` 展现了利用扩散模型处理多模态、长时域动作分布的潜力。 | `Xiaomi-Robotics-U0`, `SegDiff`, `CSI-Assisted Edge SLAM`, `Desc++` |

#### 值得优先阅读的论文

1.  **`Xiaomi-Robotics-U0`**：**理由**：它代表了具身智能领域“大模型”路线的最新实践。380亿参数、统一多任务、开源模型 `pi_0.5` 成功率的大幅提升，都是里程碑式的成果，对整个领域有标杆意义。
2.  **`OmniX`**：**理由**：它解决了前馈式4D重建的一个关键瓶颈（大视角变化下的运动建模），且自带一个100K级别的大规模自动生成数据集，对动态场景重建和4D内容创作有极大推动。
3.  **`DP-Splat`**：**理由**：这是对3DGS底层理论的一次重要修正和提升。它用严格的贝叶斯非参数方法取代了启发式的密度控制，解决了 “场景需要多少个高斯体” 这个根本问题，为更智能、更鲁棒的3DGS系统奠定基础。
4.  **`HyperGS`**：**理由**：它首次实现了真正免优化的、前馈式高斯视频表示。编码速度提升4-5个数量级，这打开了3DGS在实时视频应用（如直播、视频会议、动态内容生成）中的大门。
5.  **`SalientGS`**：**理由**：它统一了SfM和3DGS的流程，提出了一个基于MCMC的重要性引导高斯分配机制。这使得端到端重建更优雅、更快捷，是简化3D重建管线的重要一步。

#### 可能的研究机会

1.  **3DGS的先验融合与本质表征**：`MAC-Splat` 和 `GeoGS-SLAM` 证明了几何基础模型对稀疏视图的重要性。未来可研究如何将更多的先验（如语义、物理属性、材质）无缝嵌入到3DGS的优化和前馈过程中。`Grassmannian Splatting` 则提供了一个全新的参数化方向，可探索其他低维流形或拓扑结构作为3DGS的基本单元。
2.  **世界模型与下游任务的桥接**：`ABot-3DWorld 0` 构建了通用世界模型，但如何将生成的“世界”高效用于机器人策略学习、具身导航或交互式AR体验？可以研究如何将此3D世界作为强化学习环境的低成本生成器，或作为LLM的感知后端。
3.  **动态场景的“零-shot”泛化**：`OmniX` 和 `Grassmannian Splatting` 在动态场景上取得了进展，但普遍依赖特定场景的训练或优化。能否像 `HyperGS` 那样，实现对全新动态视频的“零-shot”泛化，直接预测其4D结构？
4.  **计算资源与精度的帕累托最优**：`AsySplat` 和 `DP-Splat` 都指向资源效率。未来的机会在于设计自适应的计算图谱，即在复杂区域（如动态对象、高纹理区域）自动分配更多计算资源，而在简单区域（如平坦地面）降低计算量，实现资源与精度的最优权衡。

#### 风险和不确定性

-   **全量验证依赖附录和代码**：多篇论文的

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-07-15T10:07:33-04:00
**Total number of papers:** 49
**Number of papers added in the latest update:** 11
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

#### 2026-07-14 - X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras

**Authors:** Heng Zhou, Shuhong Liu, Yonghao He, Bohao Zhang, Fa Fu, Chenhui Hou, Xianbao Hou, Lijun Han, Wei Sui
**Links:** [abs](https://arxiv.org/abs/2607.12993) - [pdf](https://arxiv.org/pdf/2607.12993)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, depth estimation

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

#### 2026-07-10 - What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility

**Authors:** Filippo Ziliotto, Luciano Serafini, Lamberto Ballan, Tommaso Campari
**Links:** [abs](https://arxiv.org/abs/2607.09503) - [pdf](https://arxiv.org/pdf/2607.09503)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, SfM, SLAM, scene representation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility  
- 作者：Filippo Ziliotto, Luciano Serafini, Lamberto Ballan, Tommaso Campari  
- 出版日期：2026-07-10  
- 分类：Geometry Foundation Models（主），3D Reconstruction & Multi-view Geometry（次）  
- 链接：摘要 https://arxiv.org/abs/2607.09503 | PDF https://arxiv.org/pdf/2607.09503  

### 一句话总结
本文发现VGGT内部表征隐式编码了共可见性（co-visibility），并通过引入轻量级逐层混合专家头（Co-VGGT）在Co-VisiON基准上超越人类标注基线，性能提升超过25%。

### 研究问题
如何利用几何基础模型VGGT的内部表征，在没有显式监督的情况下，判断图像对之间是否存在共可见重叠区域（尤其在低重叠场景中）？

### 核心思路/方法
1. 通过探针实验揭示VGGT的层级结构：早期层构建3D感知场景表征，晚期层（特别是L17层）充当共可见性推理器，且层L17对非共可见对具有一致路由行为。  
2. 提出Co-VGGT：冻结VGGT，仅训练一个小于7.5M参数的逐层混合专家头（layer-wise MoE），将每层视为一个专家，根据输入对自适应加权每层的几何抽象，以便从单张RGB图像中分类共可见性。  
3. 在Co-VisiON基准上评估，并与先前方法及人类标注基线对比。

### 主要贡献
1. 首次证明VGGT能够隐式编码共可见性，其内部表征呈现类似LLM的层级结构，且存在问题导向的层级专化证据（负锚点层L17）。  
2. 提出Co-VGGT方法，仅训练轻量级MoE头，以分类RGB图像对的共可见性。  
3. 在Co-VisiON基准上，Co-VGGT的成对预测和多重视图预测分别超越先前最佳方法25%以上和10%，并且超过人类标注基线。  
4. 成对预测校准良好（ECE=0.030），可直接作为可见性图的边权重用于下游SfM和SLAM流水线，无需后处理纠正。

### 局限性
摘要未提供足够信息，例如方法在极端场景下的性能、对错误预测的鲁棒性、计算效率的详细分析，以及是否依赖特定训练数据集等。

### 阅读优先级：高  
理由：该工作首次揭示VGGT的共可见性推理能力，基于此设计的轻量头方法显著超越现有技术和人类基线，性能提升幅度大（>25%）。方法直接服务于3D重建与SLAM的实际下游任务，且提供代码和数据，实用性强。

</details>

<details>
<summary>Abstract</summary>

A fundamental challenge in 3D reconstruction and robotic localization is co-visibility: determining which image pairs share overlapping visible surfaces, particularly in scenarios with minimal overlap. We demonstrate that VGGT implicitly encodes co-visibility as an emergent behavior: without any supervision for this task, its internal representations exhibit a clear hierarchical structure mirroring that of large language models, i.e. early layers build a 3D-aware scene representation, while late layers act as dedicated co-visibility reasoners. In particular, we identify layer L17 as a negative anchor that consistently routes non-co-visible pairs for this backbone, regardless of the evaluation setting, providing task-grounded evidence of layer specialization in a geometry-grounded foundation model. Building on this, we introduce Co-VGGT, which freezes VGGT and trains only a lightweight layer-wise mixture-of-experts head (less than 7.5M parameters) to classify co-visibility from RGB alone, treating each layer as a specialized expert whose geometric abstraction is adaptively weighted per input pair. On the Co-VisiON benchmark, Co-VGGT surpasses the human annotation baseline and improves over prior work by more than 25% pairwise and 10% multiview. Pairwise predictions are well-calibrated (ECE=0.030), enabling direct use as edge weights in visibility graphs for downstream SfM and SLAM pipelines without post-hoc correction. Code and data are available.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

#### 2026-07-14 - Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements

**Authors:** Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun
**Links:** [abs](https://arxiv.org/abs/2607.12362) - [pdf](https://arxiv.org/pdf/2607.12362)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

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

#### 2026-07-11 - Grassmannian Splatting I: Moving rank-2 Spacetime Surfels for Dynamic Scene Rendering

**Authors:** Aaron Maurice Berman, Shantanu Dave
**Links:** [abs](https://arxiv.org/abs/2607.10489) - [pdf](https://arxiv.org/pdf/2607.10489)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene representation, 4D Gaussian, Gaussian Splatting, 3DGS, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Grassmannian Splatting I: Moving rank-2 Spacetime Surfels for Dynamic Scene Rendering
- 作者：Aaron Maurice Berman, Shantanu Dave
- 出版日期：2026-07-11
- 分类：Dynamic / 4D Reconstruction; Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2607.10489 ; PDF: https://arxiv.org/pdf/2607.10489

### 一句话总结
该论文提出一种基于时序-空间四维Grassmannian splatting的动态场景表示方法，利用秩-2时空surfels实现无需变形场的高效动态渲染，在HyperNeRF数据集上训练速度最快且质量排名第二。

### 研究问题
如何用一种简洁、封闭形式的运动表示，替代现有4D Gaussian splatting方法中通过学习变形场或使用全秩四维协方差来渲染动态场景的方式，从而降低训练开销并保持高质量渲染。

### 核心思路/方法
1. 表示设计：每个图元是一个在四维时空中由高斯函数支持的三维平面（即均匀运动的二维空间表面），其协方差矩阵由单位法向量\(n\)和自由矩阵\(L\)参数化，保证在时间切片后得到秩-2的surfel（带速度信息）。
2. 运动建模：封闭形式，无需学习变形场；运动参数（法线方向、沿法线速度、磁盘形状和中心切向漂移）直接从参数中读出。
3. 硬件兼容：秩-2磁盘通过预计算协方差接口直接输入标准3DGS光栅化器，无需自定义CUDA。
4. 静态-动态统一：使用软夹钳（Schur分母中的正则化）使静态秩-3图元和动态秩-2图元连续，形成统一参数族。

### 主要贡献
- 提出一种新型动态场景图元（Grassmannian splatting），在四维时空上实现秩-2 surfel，每个图元对应一个均匀运动的二维空间表面。
- 运动模型是封闭形式的，无需变形场或额外网络，降低了训练复杂度。
- 不需要自定义CUDA内核，可直接利用预计算协方差接口和标准3DGS光栅化器。
- 在MonoDyGauBench的17个HyperNeRF场景上，训练速度比最优质基线快4.9–5.6倍，并在PSNR、MS-SSIM和LPIPS上排名第二。

### 局限性
摘要未提供足够信息：未提及多视角处理、动态场景中复杂遮挡或拓扑变化、以及在大规模场景或非HyperNeRF类数据集上的表现。

### 阅读优先级
**高**  
理由：该方法在动态场景渲染领域实现了显著的训练速度提升（4.9–5.6倍），同时保持了顶级质量（第二），且避免了自定义CUDA和变形场，工程实现简洁；摘要显示其发布在2026年（即使时间戳存疑），但内容新颖，对关注动态辐射场高效表示的读者有较高价值。

</details>

<details>
<summary>Abstract</summary>

We introduce Grassmannian splatting, a dynamic scene representation whose primitives are Gaussians supported on 3-planes in spacetime $\R^4$: generically, spatial 2-planes in uniform translation along their normals. Each primitive carries a unit normal $n \in \mathbb S^3/\{\pm 1\} \cong \mathrm{Gr}(3,4)$ and an unconstrained factor $L \in \mathbb R^{4 \times 3}$, with covariance \[ Σ_{4\mathrm{D}} = (P_n L)(P_n L)^T, \qquad P_n = I - n n^T. \] For generic $L$ and $n \neq \pm e_0$, conditioning on time returns a rank-2 surfel at every frame. The normal of the disk and its velocity along that normal are read off from $n$; the disk shape and the tangential drift of its center are set by $L$. Existing native 4D Gaussian splatting methods [\it{Yang et. al. 2023,Duan et. al. 2024}] slice full-rank spacetime covariances, so their per-frame primitive is a volumetric ellipsoid; since conditioning lowers rank by exactly one, a rank-2 surfel in the slice requires a rank-3 spacetime covariance, and the parameterization above realizes exactly these. The motion model is closed form, i.e. no deformation field is learned, and no custom CUDA is required: the conditioned disk feeds a standard 3DGS rasterizer through its precomputed-covariance interface. A soft clamp in the Schur denominator regularizes the static orientation and continuously bridges rank-3 static and rank-2 dynamic behavior, so static and moving primitives form a single continuous family. On the 17 HyperNeRF scenes of MonoDyGauBench, training is fastest among all compared methods (4.9 to 5.6 times faster than the strongest quality baselines), while ranking second in PSNR, MS-SSIM, and LPIPS. Code: https://github.com/PaulCelanCoding/grassmannian-splatting

</details>

#### 2026-07-09 - LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models

**Authors:** Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, Yu-Lun Liu
**Links:** [abs](https://arxiv.org/abs/2607.08770) - [pdf](https://arxiv.org/pdf/2607.08770)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models
- 作者：Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, Yu-Lun Liu
- 出版日期：2026-07-09
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2607.08770

### 一句话总结
本文提出LongE2V，利用预训练视频扩散模型，通过自回归展开、自适应上下文切换和重编码对齐等技术，统一实现事件数据的高质量视频重建、预测和帧插值，尤其在长时序列中保持稳定性。

### 研究问题
如何从稀疏事件流中恢复高质量、长时稳定的视频，并同时解决重建、预测和帧插值三个任务中的纹理模糊、时间漂移和双向一致性问题。

### 核心思路/方法
1. **预训练视频扩散先验**：微调基础视频模型，利用其生成先验实现高数据效率和优越感知质量。
2. **自回归展开与自适应上下文切换**：通过逐步展开生成并动态切换上下文，缓解极长序列中的时间漂移。
3. **重编码对齐与交叉残差校正**：在帧插值任务中，通过对齐隐空间编码和残差校正，确保精确的双向一致性。
4. **事件体素密度增强**：增强对不同传感器分辨率的鲁棒性。

### 主要贡献
- 首个统一处理事件视频重建、预测和帧插值的扩散方法，实现三任务协同。
- 提出自回归展开和自适应上下文切换，解决长序列时间漂移问题。
- 提出重编码对齐与交叉残差校正，提升帧插值的双向一致性。
- 提出事件体素密度增强，提高模型对不同传感器分辨率的泛化性。
- 在真实世界基准上，三个任务均超越现有方法，表现出优异的时间一致性和零样本泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作首次将视频扩散模型统一应用于三个关键事件视觉任务，且重点解决了长时序列稳定性这一核心挑战，方法设计系统（多个原创模块），实验结果全面，理论基础与工程实践价值均较高，适合关注事件相机、视频生成和时序建模的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recovering high-quality video from sparse event streams is a challenging task. Regression methods often blur textures, while existing generative models struggle with long-term stability. We propose LongE2V, a novel approach that leverages pre-trained video diffusion priors to jointly handle event-based video reconstruction, prediction, and frame interpolation. By fine-tuning a foundational video model, our approach achieves high data efficiency and superior perceptual quality. We introduce Autoregressive Unrolling and Adaptive Context Switching to mitigate temporal drift in extremely long sequences. We also propose Reencoding Alignment with Cross Residual Correction to ensure precise bidirectional consistency during frame interpolation. Furthermore, Event Voxel Density Augmentation ensures robustness across varying sensor resolutions. Extensive experiments on real-world benchmarks demonstrate that LongE2V outperforms state-of-the-art methods across all three tasks, exhibiting exceptional temporal coherence and zero-shot generalization. Project page: https://cdfan0627.github.io/LongE2V-page/

</details>

#### 2026-07-09 - On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting

**Authors:** In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong
**Links:** [abs](https://arxiv.org/abs/2607.08250) - [pdf](https://arxiv.org/pdf/2607.08250)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting
- 作者：In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong
- 出版日期：2026-07-09
- 分类：Dynamic / 4D Reconstruction（主要）、Neural Scene Representations & Rendering（次要）
- 链接：摘要页 https://arxiv.org/abs/2607.08250 ；PDF https://arxiv.org/pdf/2607.08250

### 一句话总结
本文从混合专家（MoE）视角出发，研究了动态3D高斯表示中多变形建模的设计问题，提出了两种不同集成约束下的变形专家组合策略：MoDE（联合优化）和MoE-GS（独立优化后经路由组合）。

### 研究问题
如何有效设计多变形模型，以提升动态3D高斯表示在多样化动态场景下的鲁棒性和泛化能力。

### 核心思路/方法
- 基于混合专家（MoE）框架，将多变形建模视为在统一3D表示中组合多个专用变形专家。
- 提出两种方案：
    - **MoDE（Mixture of Deformation Experts）**：多个变形专家与可变形高斯泼溅管线联合优化，作用于共享的规范高斯表示，不引入额外训练阶段。
    - **MoE-GS**：变形专家独立优化，通过独立的路由阶段进行组合，专家交互发生在非规范高斯表示上。
- 两种方案对比揭示了不同集成约束如何塑造动态3D表示中变形专家的设计与行为。

### 主要贡献
- 从MoE视角系统研究了动态3D高斯表示中的多变形建模问题。
- 提出两种互补的集成策略（MoDE和MoE-GS），分别对应不同的专家交互时机与表示形式。
- 为动态场景重建中如何灵活部署多变形模型提供了设计空间分析。

### 局限性
摘要未提供足够信息，无法判断具体实验局限性（如计算成本、场景规模限制等）。

### 阅读优先级
**高**
- **理由**：
    - 主题前沿：动态场景重建和3D高斯泼溅是当前热门的视觉研究方向。
    - 方法新颖：将MoE思想系统性地引入多变形建模，并明确提出两种差异化设计方案，具有方法论贡献。
    - 作者团队公布了代码，便于复现与扩展。

</details>

<details>
<summary>Abstract</summary>

Dynamic scene reconstruction remains challenging due to the heterogeneous and spatially varying nature of real-world motion. Although recent 3D Gaussian Splatting methods have introduced diverse deformation formulations for dynamic novel view synthesis, each method typically relies on a single deformation model within its representation, which limits robustness across diverse dynamic scenarios. In this work, we study a fundamental problem-multi-deformation modeling for dynamic 3D Gaussian representations-under two distinct integration constraints that differ in when and how multiple deformation experts interact during training. From a Mixture-of-Experts (MoE) perspective, we view multi-deformation modeling as the problem of combining multiple specialized deformation models within a unified 3D representation. We first introduce Mixture of Deformation Experts (MoDE), which integrates multiple deformation experts directly into the deformable Gaussian Splatting pipeline through joint optimization. In MoDE, experts operate on a shared canonical Gaussian representation, enabling multi-deformation modeling without introducing additional training stages or modifying the original optimization schedule. In contrast, we further present Mixture of Experts for Dynamic Gaussian Splatting (MoE-GS) under a different integration constraint, where deformation experts are optimized independently and combined through a separate routing stage. As a result, expert interaction occurs over non-canonical Gaussian representations after individual optimization. Together, these two approaches provide alternative strategies for multi-deformation modeling, clarifying how integration constraints shape the design and behavior of deformation experts in dynamic 3D Gaussian representations. Our code is available at: https://github.com/cvsp-lab/MoE-GS-studio.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-14 - ARDepth: Auto-regressive Monocular Depth Estimation with Progressive Visual Conditioning

**Authors:** Zijie Wang, Wei Zhang, Weiming Zhang, Xiao Tan, Weikai Chen, Xiaoxu Li, Guanbin Li
**Links:** [abs](https://arxiv.org/abs/2607.12433) - [pdf](https://arxiv.org/pdf/2607.12433)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

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

#### 2026-07-12 - TriCons-Pose: Triangle-Invariant Geometric Consistency Learning for Category-Level Object Pose Estimation

**Authors:** Zuzhi Yang, Shuai Wang, Mounir Kaaniche, Ziwei Li, Zhiming Cheng, Zhidong Zhao, Chenggang Yan
**Links:** [abs](https://arxiv.org/abs/2607.10754) - [pdf](https://arxiv.org/pdf/2607.10754)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TriCons-Pose: Triangle-Invariant Geometric Consistency Learning for Category-Level Object Pose Estimation
- 作者：Zuzhi Yang, Shuai Wang, Mounir Kaaniche, Ziwei Li, Zhiming Cheng, Zhidong Zhao, Chenggang Yan
- 出版日期：2026-07-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.10754

### 一句话总结
本文提出了一种基于三角形不变几何一致性学习的类别级物体姿态估计方法，通过检测结构一致的关键点并聚合姿态不变特征，在REAL275、CAMERA25和HouseCat6D数据集上验证了有效性。

### 研究问题
现有基于关键点对应范式的类别级物体姿态估计方法，往往依赖更强的特征学习，却忽视了所建立对应关系在不同扰动下的几何稳定性，导致在类内形状变化和遮挡场景下姿态恢复不稳健。

### 核心思路/方法
- 提出三角形不变几何一致性学习框架。
- 设计结构一致关键点检测器（SCKD），通过归一化成对距离匹配强制跨视角结构一致性，以定位稳健关键点。
- 提出姿态不变几何聚合器（PIGA），通过将基于三角形的姿态不变描述子注入局部到全局注意力机制，增强关键点表示。
- 在标准目标函数基础上，额外引入几何一致性损失进行训练。

### 主要贡献
- 开发了TriCons-Pose框架，通过三角形不变几何一致性学习获得可靠的关键点和姿态不变线索，从而实现精确的规范映射和姿态估计。
- 提出SCKD和PIGA两个核心模块，分别用于稳定关键点检测和姿态不变特征聚合。
- 在REAL275、CAMERA25和HouseCat6D三个数据集上进行实验，证明了方法的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对类别级物体姿态估计中的几何稳定性问题，方法设计具有明确的理论动机（三角形不变性），且在多个基准数据集上验证了性能。适合从事3D视觉、姿态估计相关领域的研究者阅读，但对于不涉及该方向的研究者则优先级不高。

</details>

<details>
<summary>Abstract</summary>

Category-level object pose estimation is a crucial yet challenging task in both academia and industry, and has achieved remarkable success by leveraging keypoint-based correspondence paradigms. However, most existing methods increasingly rely on stronger feature learning while overlooking whether the established correspondences are geometrically stable across diverse perturbations. This often results in fragile pose recovery under intra-class shape variations and occlusions. To tackle this challenge, we develop a novel Triangle-Invariant Geometric Consistency Learning for Category-Level Object Pose Estimation (TriCons-Pose) to anchor stable keypoints and aggregate pose-invariant cues, yielding reliable canonical mapping and accurate pose estimation. Specifically, a Structure-Consistent Keypoint Detector (SCKD) is designed to identify robust keypoints by enforcing cross-view structural consistency via normalized pairwise distance matching. Moreover, we propose a Pose-Invariant Geometric Aggregator (PIGA) to augment keypoint representations by injecting triangle-based pose-invariant descriptors into a local-to-global attention mechanism. The proposed framework is optimized using standard objective functions while incorporating an additional geometry consistency loss. Extensive experiments on REAL275, CAMERA25, and HouseCat6D datasets demonstrate the effectiveness of the proposed approach.

</details>

#### 2026-07-12 - Incremental Online Scene Reconstruction by 3D Gaussian Triangulation

**Authors:** Yanjin Zhu, Shaofan Liu, Jianke Zhu
**Links:** [abs](https://arxiv.org/abs/2607.10690) - [pdf](https://arxiv.org/pdf/2607.10690)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Incremental Online Scene Reconstruction by 3D Gaussian Triangulation  
- 作者：Yanjin Zhu, Shaofan Liu, Jianke Zhu  
- 出版日期：2026-07-12  
- 分类：3D Reconstruction & Multi-view Geometry / Neural Scene Representations & Rendering  
- 链接：[摘要](https://arxiv.org/abs/2607.10690) | [PDF](https://arxiv.org/pdf/2607.10690)

### 一句话总结
本文提出一种在线增量式重建框架，直接对三维高斯点集进行三角化，以同时实现高质量渲染和增量式表面网格重建。

### 研究问题
现有的三维高斯泼溅方法多依赖离线将优化后的高斯转化为隐式场来提取网格，无法与下游任务无缝集成。本文旨在解决如何在线、增量地重建并更新高保真显式网格的问题。

### 核心思路/方法
- 设计一种密集几何高斯表示，通过直接三角化该表示来重建显式网格，支持增量更新与高质量渲染。
- 提出一种直接网格化算法，从高斯集中高效提取并更新网格。
- 引入基于平面的牵引约束，动态将三维高斯基元对齐到近似局部表面，以提高网格精度。
- 通过动态冻结已充分优化的历史区域，降低长序列处理中的内存与计算开销。

### 主要贡献
- 提出一种新颖的在线框架，能增量重建并更新高保真显式网格，避免离线隐式转换。
- 实现直接网格化算法，从高斯表示中高效提取和更新网格。
- 引入平面牵引约束以保证网格准确性。
- 在公共数据集上，该方法在渲染质量和重建精度上均优于传统基于高斯的方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对3D高斯泼溅在在线增量重建中的关键瓶颈（必须离线转换隐式场）提出了直接三角化显式网格的新思路，方法创新性较强，且公开实验结果显示性能领先，对实时场景重建和下游任务集成有潜在应用价值。

</details>

<details>
<summary>Abstract</summary>

Incremental scene reconstruction is essential for real-world applications. Although 3D Gaussian Splatting shows strong potential, most existing approaches require offline conversion of the optimized Gaussians into an intermediate implicit field for explicit mesh extraction, which hinders seamless integration with downstream tasks. To address this limitation, we propose a novel online framework that incrementally reconstructs and updates high-fidelity explicit meshes by directly triangulating a dense geometric Gaussian representation, which supports both high-quality rendering and incremental surface reconstruction. Moreover, we present a direct meshing algorithm that efficiently extracts and updates the mesh from the Gaussian set. To ensure mesh accuracy, we enforce a plane-based pulling constraint that dynamically aligns 3D Gaussian primitives to the approximated local surface. Furthermore, our framework significantly reduces memory and computational overhead during long-sequence processing by dynamically freezing fully optimized historical regions. Experiments on public datasets demonstrate that our method outperforms conventional Gaussian-based methods on both rendering quality and reconstruction accuracy.

</details>

#### 2026-07-11 - CSI-Assisted Edge SLAM Testbed Platform for 5G Connected Unmanned Autonomous Vehicles

**Authors:** Boris Radovanovic, Sasa Talosi, Srdjan Sobot, Dejan Vukobratovic
**Links:** [abs](https://arxiv.org/abs/2607.10394) - [pdf](https://arxiv.org/pdf/2607.10394)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, robotics, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CSI-Assisted Edge SLAM Testbed Platform for 5G Connected Unmanned Autonomous Vehicles
- 作者：Boris Radovanovic, Sasa Talosi, Srdjan Sobot, Dejan Vukobratovic
- 出版日期：2026-07-11
- 分类：3D Reconstruction & Multi-view Geometry (主要), Embodied / Robotics / AR Applications (次要)
- 链接：arXiv:2607.10394

### 一句话总结
本文设计并实现了一个集成5G O-RAN、CSI辅助的Edge SLAM测试平台，用于评估面向6G的机器人系统在通信与感知融合中的性能与挑战。

### 研究问题
如何构建一个端到端的、支持CSI（信道状态信息）数据暴露与融合的Edge SLAM测试平台，以在5G URLLC环境下实现通信感知协同，并揭示其在延迟、同步和系统集成方面的关键难题。

### 核心思路/方法
- 构建一个集成的测试平台：包含自定义无人地面车（UGV）、基于ROS2的SLAM框架，以及5G O-RAN（开放无线接入网）系统。
- 提供端到端的跨层视图，让ROS2传感器数据流经5G网络传输，并明确将CSI作为额外感知模态暴露并集成到SLAM流水线中。
- 分析ROS2 DDS（数据分发服务）通信、RTPS（实时发布订阅协议）分包及5G用户面传输，探讨通过O-RAN组件提取和交付CSI的机制。

### 主要贡献
- 设计并实现了首个整合UGV、ROS2 SLAM与5G O-RAN的CSI辅助Edge SLAM测试平台。
- 提供了完整的端到端、跨层数据流分析，涵盖从ROS2层到5G用户面的传输细节。
- 揭示了通信感知SLAM在实际系统中的关键挑战，包括延迟、数据流、同步及跨系统集成，为未来6G机器人平台提供了实验洞察。

### 局限性
摘要未提供足够信息（例如未讨论测试规模、具体性能指标或是否存在试验结果中的失败案例）。

### 阅读优先级
中
理由：该论文侧重于系统架构设计与平台实现，核心价值在于工程整合与实验观察，而非提出全新算法。对于关注5G/6G与机器人SLAM交叉领域、需要构建类似测试平台的读者具有直接参考意义，但对纯算法或理论研究者价值相对有限。

</details>

<details>
<summary>Abstract</summary>

The evolution from 5G towards 6G reinforces interest in connected robotics, where mobile robots offload compute-intensive tasks to edge servers over ultra-reliable low-latency communication (URLLC) links. Simultaneous localization and mapping (SLAM), a fundamental yet demanding robotics function, is increasingly considered for edge deployment within mobile edge computing (MEC) frameworks. In parallel, integrated sensing and communications (ISAC) enables the use of radio channel information, such as channel state information (CSI), as an additional sensing modality in radio-based SLAM. In this paper, we design and implement a CSI-assisted Edge SLAM testbed integrating a custom unmanned ground vehicle (UGV), a ROS2-based SLAM framework, and a 5G Open Radio Access Network (O-RAN) system. The proposed architecture provides an end-to-end, cross-layer view of ROS2 sensor data streaming over 5G, explicitly enabling CSI exposure and integration into the SLAM pipeline. We analyze ROS2 DDS communication, RTPS packetization, and 5G user-plane transport, and discuss mechanisms for CSI extraction and delivery via O-RAN components. The platform enables realistic experimentation with communication-aware SLAM and reveals key challenges related to latency, data streaming, synchronization, and cross-system integration, providing insights for future 6G-enabled robotic platforms.

</details>

#### 2026-07-10 - DGSfM: Depth-Guided Scale-Aware Global Structure-from-Motion

**Authors:** Sithu Aung, Viktor Kocur, Yaqing Ding, Torsten Sattler, Zuzana Kukelova
**Links:** [abs](https://arxiv.org/abs/2607.09507) - [pdf](https://arxiv.org/pdf/2607.09507)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM, bundle adjustment, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DGSfM: Depth-Guided Scale-Aware Global Structure-from-Motion
- 作者：Sithu Aung, Viktor Kocur, Yaqing Ding, Torsten Sattler, Zuzana Kukelova
- 出版日期：2026-07-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.09507

### 一句话总结
DGSfM 是一种深度感知的全局运动恢复结构（SfM）流水线，通过引入单目深度图作为先验，将传统尺度模糊的对极几何约束转换为尺度感知的约束，并结合视图图过滤与深度一致性剪枝，显著提升了位姿精度。

### 研究问题
全局 SfM 方法依赖尺度模糊的对极几何，易受噪声基线估计和弱视图图约束的影响，同时视觉模糊对之间的假边会降低重建质量。本文旨在解决这些鲁棒性和尺度模糊性问题。

### 核心思路/方法
1. **深度感知相对位姿求解器**：对每对图像，利用深度图将尺度模糊的对极约束转换为尺度感知的相对位姿约束。
2. **视图图过滤与深度一致性剪枝**：通过视图图过滤和基于深度一致性的对应点剪枝，抑制仅在对极几何下看似合理的假边和误匹配。
3. **全局尺度平均与深度引导初始化**：进行全局尺度平均，并用深度引导的位姿-点初始化将单目深度图对齐到公共重建尺度，为全局位姿估计和光束法平差提供稳定初始化。

### 主要贡献
- 提出一种深度感知的全局 SfM 流水线 DGSfM，利用单目深度图作为可扩展先验，同时保持显式多视图优化。
- 通过深度引导的位姿求解、视图图过滤和对应剪枝，在稀疏和稠密匹配前端均显著提升位姿精度。
- 在 ETH3D 和 IMC2021 数据集上，优于强全局 SfM 基线方法。

### 局限性
摘要未提供足够信息。摘要未提及模型对深度图质量的敏感度、计算开销、在极端场景（如纹理缺失或动态场景）下的表现等局限性。

### 阅读优先级
**高**。理由：该工作针对全局 SfM 中的核心尺度模糊和鲁棒性问题，提出了简洁有效的深度引导方案，在标准数据集上取得了明显改进，且代码已开源。对于从事 3D 重建、多视图几何研究的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Global Structure-from-Motion (SfM) is an efficient paradigm for recovering camera poses and sparse 3D structure from unordered images. However, its reliance on scale-ambiguous epipolar geometry makes global positioning sensitive to noisy baseline estimates and weak view-graph constraints, while false edges from visually ambiguous pairs can further degrade reconstruction. We propose DGSfM, a depth-aware global SfM pipeline that uses monocular depth maps as a scalable prior while preserving explicit multi-view optimization. For each image pair, we use a depth-aware relative pose solver to convert scale-ambiguous epipolar constraints into scale-aware relative pose constraints. We further improve robustness through view-graph filtering and depth-consistency-based correspondence pruning, which suppress false edges and matches that remain plausible under epipolar geometry alone. Finally, global scale averaging and depth-guided pose-point initialization align monocular depth maps into a common reconstruction scale and provide stable initialization for global positioning and bundle adjustment. Experiments on ETH3D and IMC2021 show that DGSfM consistently improves over strong global SfM baselines across sparse and dense matching front-ends, achieving substantial gains in pose accuracy. Code is available at https://github.com/sithu31296/DGSfM.

</details>

#### 2026-07-09 - Wat3R: Underwater 3D Geometry Learning without Annotations

**Authors:** Jiangwei Ren, Xingyu Jiang, Zijie Song, Wei Xu, Hongkai Lin, Dingkang Liang, Xiang Bai
**Links:** [abs](https://arxiv.org/abs/2607.08772) - [pdf](https://arxiv.org/pdf/2607.08772)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, depth estimation, point cloud reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wat3R: 无标注水下3D几何学习
- 作者：Jiangwei Ren, Xingyu Jiang, Zijie Song, Wei Xu, Hongkai Lin, Dingkang Liang, Xiang Bai
- 出版日期：2026-07-09
- 分类：3D重建与多视图几何
- 链接：arXiv:2607.08772

### 一句话总结
本文提出一个名为Wat3R的半监督学习框架，无需任何水下标注数据，仅利用无标注水下视频，通过教师-学生架构适应空气到水下场景的前馈3D重建模型。

### 研究问题
如何在水下环境（存在光衰减、散射及缺少大规模高质量3D标注）中，有效估计3D几何结构。

### 核心思路/方法
1. 构建一个交叉域半监督学习框架，采用教师-学生架构，无需任何标注水下数据。
2. 利用大量无标注真实水下视频，让模型学习鲁棒的几何表示。
3. 设计跨视图一致性损失函数：从其他视图提取几何线索，补偿当前视图因水衰减和散射导致的信息退化。
4. 构建了用于几何评估的Water3D数据集，涵盖多样水体与水下场景。

### 主要贡献
1. 提出了首个无需水下标注数据的交叉域半监督3D重建方法（Wat3R）。
2. 设计了跨视图一致性损失，有效缓解水下信息退化问题。
3. 构建了Water3D数据集，填补水下几何评估基准的空白。
4. 在水下多视图深度估计和点云重建任务上，Wat3R超越了当前最优方法。

### 局限性
- 摘要未提供具体局限性信息（如对极暗水体、强浑浊环境的鲁棒性，或训练计算成本等）。

### 阅读优先级
**高**。理由：该工作解决了水下3D重建中标注数据稀缺的关键痛点，提出的无标注半监督学习思路具有较强创新性和实用性，且包含了新构建的评估基准数据集。若您关注水下视觉、无监督/半监督3D重建领域，该论文有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Estimating 3D geometry in underwater environments presents unique challenges due to light attenuation, scattering, and the absence of large-scale, high-quality 3D annotations. Pioneering methods rely on massive dense annotations that are impractical in underwater settings. In this paper, we propose Wat3R, a cross-domain semi-supervised learning framework designed to adapt feed-forward 3D reconstruction models from air to underwater scenes. Uniquely, our method eliminates the need for any annotated underwater data following a teacher-student architecture, that learns robust geometry representations merely on abundant unlabeled real underwater video footage. We also design a cross-view consistency loss that leverages geometric cues from other views to compensate for the information degradation in the current view caused by water attenuation and scattering. Furthermore, considering the lack of comprehensive evaluation benchmarks, we construct Water3D, a diverse dataset covering various water bodies and underwater scenarios, designed for geometric task evaluation. Experimental results demonstrate that Wat3R outperforms current state-of-the-art methods in underwater multi-view depth estimation and point cloud reconstruction. The dataset and code are available at https://github.com/LSXI7/Wat3R .

</details>

#### 2026-07-09 - ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device

**Authors:** Fabio Tosi, Luca Bartolomei, Matteo Poggi, Stefano Mattoccia
**Links:** [abs](https://arxiv.org/abs/2607.08771) - [pdf](https://arxiv.org/pdf/2607.08771)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device
- 作者：Fabio Tosi, Luca Bartolomei, Matteo Poggi, Stefano Mattoccia
- 出版日期：2026-07-09
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.08771

### 一句话总结
ZipDepth是一种仅6.1M参数、可在各类设备上实时运行的轻量级零样本单目深度估计网络，通过高效编码器-解码器与大规模知识蒸馏，在零样本精度与部署效率间取得了最佳平衡。

### 研究问题
如何构建一种轻量级、能在嵌入式和移动平台上实时运行，同时具备零样本泛化能力（即应对跨领域场景）的单目深度估计模型。

### 核心思路/方法
- 设计一个可重参数化的高效编码器-解码器架构。
- 利用大规模多域训练集，从基础模型（foundation model）中执行大规模知识蒸馏，将庞大模型的知识迁移至紧凑网络。

### 主要贡献
- 提出了ZipDepth网络，仅包含6.1M参数，可在从服务器GPU到功耗受限设备上以实时速率运行。
- 在五个基准测试上，ZipDepth在轻量级模型中实现了零样本准确度与部署效率之间的最佳权衡。
- 显著缩小了与参数多50倍的基础模型在精度上的差距。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高 — 该工作直接面向嵌入式/移动设备上的实时零样本深度估计，具有明确的部署价值，且方法简洁有效，适合关注轻量级计算机视觉和移动端部署的研究者。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation has seen remarkable progress through foundation models achieving robust zero-shot generalization, yet their computational demands place them far beyond the reach of embedded and mobile platforms. Lightweight alternatives exist, but have been developed almost exclusively within single-domain, self-supervised paradigms, failing silently under domain shift. We present ZipDepth, a compact monocular depth network that bridges this gap by combining an efficient reparameterizable encoder-decoder with large-scale knowledge distillation from a foundation model over a large multi-domain training set. Comprising just 6.1M parameters, ZipDepth runs at real-time rates from server GPUs to power-constrained devices, achieving the best trade-off between zero-shot accuracy and deployment efficiency among lightweight models across five benchmarks, taking a significant step towards the accuracy of foundation models with 50x more parameters.

</details>

#### 2026-07-09 - Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction

**Authors:** Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi
**Links:** [abs](https://arxiv.org/abs/2607.08769) - [pdf](https://arxiv.org/pdf/2607.08769)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, monocular depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction
- 作者：Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi
- 出版日期：2026-07-09
- 分类：3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.08769

### 一句话总结
本工作提出了PanoLOG，一个结合几何与梯度启发的分区策略（G²PS），专门用于基于全景图像的大规模室外场景3D高斯溅射重建，在保证渲染质量的同时实现可扩展的块并行训练。

### 研究问题
如何高效地将3D高斯溅射（3DGS）扩展到大型室外场景重建，特别是当使用全景图像（ERP格式）时，解决其全向可见性导致现有局部相机视锥分区策略失效、块优化退化为全局训练的问题。

### 核心思路/方法
提出一个两阶段粗到细框架PanoLOG：1）全局粗阶段：利用天球建模和全景单目深度监督获得可靠的初始几何。2）细化阶段：采用G²PS分区策略，通过视差驱动的不确定性构建自适应包围体，并基于梯度的重要性评分分配相机，从而实现块并行优化。

### 主要贡献
1. 提出了PanoLOG，首个针对大规模全景室外场景3DGS重建的两阶段框架。
2. 设计了G²PS分区策略，解决了全景图像全向可见性带来的分区困难。
3. 构建了Pano360，第一个大规模室外场景重建的全景数据集。
4. 实验表明G²PS在保持可扩展块并行训练的同时，取得了最先进的渲染质量；代码、模型和数据集已公开。

### 局限性
摘要未提供足够信息。未提及计算资源需求、对极端光照或动态物体的处理能力、以及分割边界处的伪影或一致性评价等。

### 阅读优先级
高。理由：该工作针对全景图像在大规模室外重建中的关键挑战（分区退化）提出了原创性方法，并贡献了首个专用数据集，方法在渲染质量和可扩展性上均表现优异，对全景3D重建领域有重要推进意义。

</details>

<details>
<summary>Abstract</summary>

Scaling 3D Gaussian Splatting (3DGS) to large outdoor scenes is costly in both data acquisition and computation. Adopting panoramic images with equirectangular projection (ERP) can reduce capture effort via their full $360^{\circ}$ field of view, yet the resulting omnipresent visibility invalidates existing partitioning strategies that rely on local camera frustums, causing block-wise optimization to degenerate into global training. Thus, we propose PanoLOG, a two-stage coarse-to-fine framework equipped with a Geometry and Gradient-based Partitioning Strategy tailored for large-scale panoramic 3DGS reconstruction. In the global coarse stage, PanoLOG leverages sky-sphere modeling and panoramic monocular depth supervision for reliable geometry, while in the refinement stage, G$^2$PS builds adaptive bounding volumes via parallax-driven uncertainty and assigns cameras via gradient-based importance scoring. Furthermore, we construct Pano360, the first benchmark on large-scale panoramic dataset for outdoor scene reconstruction. Extensive experiments demonstrate that G$^2$PS achieves state-of-the-art rendering quality while maintaining scalable, block-parallel training. Our models, training code, and dataset are publicly available.

</details>

#### 2026-07-09 - LTM: Large-scale Terrain Model for Wildfire-prone Landscapes

**Authors:** Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan
**Links:** [abs](https://arxiv.org/abs/2607.08711) - [pdf](https://arxiv.org/pdf/2607.08711)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LTM: Large-scale Terrain Model for Wildfire-prone Landscapes
- 作者：Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan
- 出版日期：2026-07-09
- 分类：3D Reconstruction & Multi-view Geometry（3D重建与多视图几何）
- 链接：摘要页 https://arxiv.org/abs/2607.08711 | PDF https://arxiv.org/pdf/2607.08711

### 一句话总结
该文提出一种多模态重建框架，利用过时数字高程模型（DEM）作为几何先验，通过物理驱动的像素-像素对齐，实现野火易发区域大尺度地形的低成本、高保真三维重建。

### 研究问题
如何利用低成本的图像数据，并结合过时的数字高程模型，高效准确地重建野火易发区域的大尺度三维地形，以克服传统方法成本高、更新慢或视觉特征稀疏的问题。

### 核心思路/方法
提出一种多模态重建框架，核心创新在于：采用物理驱动的像素-像素对齐方法，将图像与数字高程模型（DEM）数据直接对齐，从而跳过昂贵且易失败的图像间特征匹配步骤，大幅降低计算复杂度。该框架以DEM作为几何先验，为基于图像的三维重建提供约束，最终生成高保真深度图。

### 主要贡献
1. 提出了一种基于多模态（图像+DEM）的框架，用于大尺度野火易发地形的高效重建。
2. 创新性地引入物理驱动的像素-像素对齐，无需显式特征匹配，显著降低计算开销。
3. 构建了一个基于真实野火区域的大尺度地形仿真器，用于生成包含真实场景的图像数据，支撑算法评估。
4. 实验表明，在给定有姿态图像和过时DEM的情况下，方法在重建精度和计算效率上均显著优于现有技术，且支持实时性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作面向野火应急场景下的大规模地形重建，具有明确的应用价值。核心方法（物理驱动像素对齐替代特征匹配）在计算效率和精度上展现出优势，且通过仿真器进行了系统验证。对于从事3D重建、遥感与应急响应研究的读者，具有直接参考意义。

</details>

<details>
<summary>Abstract</summary>

Accurate 3D terrain maps are essential for emergency response when assessing wildfire hazards. However, wildfire-prone regions often span vast areas where conventional reconstruction methods underperform. Airborne LiDAR systems provide high-resolution terrain data, but they are expensive and infrequently updated. Image-based methods offer a lower-cost alternative, but struggle due to sparse visual features and limited image overlap. We propose a multi-modal reconstruction framework leveraging outdated Digital Elevation Models (DEMs) as geometric priors for image-based 3D reconstruction. Our key innovation is physics-based pixel-pixel alignment between images and DEM data, dramatically reducing computational complexity by eliminating expensive feature matching procedures. To validate our approach, we developed a large-terrain simulator based on a real wildfire-prone area, generating realistic images enabling a comprehensive evaluation. Given posed images and legacy DEMs, our method produces high-fidelity depth maps while maintaining real-time performance. We find significant improvements in reconstruction accuracy and computational efficiency over existing techniques, offering a scalable solution for wildfire response.

</details>

#### 2026-07-09 - HoloTetSphere: Unified TetSphere Mesh Reconstruction for Physical Simulations

**Authors:** YaQiao Dai, Renjiao Yi, Zhirui Gao, Wei Chen, Kai Xu, Chenyang Zhu
**Links:** [abs](https://arxiv.org/abs/2607.08398) - [pdf](https://arxiv.org/pdf/2607.08398)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mesh reconstruction, rendering, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HoloTetSphere: Unified TetSphere Mesh Reconstruction for Physical Simulations
- 作者：YaQiao Dai, Renjiao Yi, Zhirui Gao, Wei Chen, Kai Xu, Chenyang Zhu
- 出版日期：2026-07-09
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.08398

### 一句话总结
本文提出HoloTetSphere，一种通过端到端拓扑与几何优化直接构建统一且拓扑连贯的四面体网格的方法，旨在替代传统易出错的表面重建加四面体化流程，以支持物理仿真。

### 研究问题
现有物理仿真就绪的三维重建方法主要依赖分离的两阶段范式（先提取表面几何，再进行易出错的四面体化），而近期Lagrangian方法如TetSphere Splatting虽尝试直接优化体积基元，但其同胚约束限制了拓扑自适应优化，导致生成不连贯的离散四面体，无法用于进一步的物理仿真。本文致力于解决如何直接重建拓扑连贯、统一的四面体网格，且适用于物理仿真的问题。

### 核心思路/方法
1. **拓扑自适应优化框架**：通过端到端的拓扑和几何优化实现整体四面体网格重建。
2. **可微分元素剪枝**：将高斯球与四面体元素耦合，并利用边连接关系估计连续不透明度场，以实现可微分的元素剪枝。
3. **交替几何细化**：联合最小化网格平滑能量与多视图高斯渲染误差，驱动交替的几何细化，同时保持拓扑自适应性。
4. **输出**：构建统一的、拓扑连贯的四面体网格，绕过传统表面网格四面体化步骤。

### 主要贡献
- 提出了一种拓扑自适应的框架，直接从多视图输入重建四面体网格，克服了传统方法拓扑固定且产生离散元素的问题。
- 通过可微元素剪枝与交替几何优化，在保持拓扑适应性的同时实现了几何精度提升。
- 实验表明，该方法在几何精度上超越现有技术，并生成连贯、单一连接的四面体网格，从而简化下游物理仿真流程。

### 局限性
摘要未提供足够信息。摘要中未讨论方法在复杂拓扑、计算效率、鲁棒性或在极端稀疏视图条件下的表现，也未提及任何失败的案例或潜在的应用限制。

### 阅读优先级
**高**  
理由：该方法直接解决三维重建到物理仿真流程中的关键瓶颈（传统四面体化易出错、Lagrangian方法拓扑不连贯），且通过端到端优化实现了拓扑自适应的四面体网格重建，在几何精度和网格连贯性上超越现有技术，对计算机图形学与物理仿真领域具有重要潜在价值。

</details>

<details>
<summary>Abstract</summary>

Standard pipelines for physics-ready 3D reconstruction rely on a decoupled two-stage paradigm: extracting surface geometry followed by an error-prone tetrahedralization process. While recent Lagrangian methods like TetSphere Splatting attempt to bypass this by directly optimizing volumetric primitives, their homeomorphic constraints prevent topology-adaptive optimization. Consequently, they produce disjoint tetrahedra rather than a single connected mesh, rendering the structures unsuitable for further physical simulations. To address this, we propose a topology-adaptive framework for holistic tetrahedral mesh reconstruction through end-to-end topological and geometric optimization. First, by coupling Gaussian spheres to tetrahedral elements and leveraging edge connections, we estimate a continuous opacity field for differentiable element pruning. Next, jointly minimizing mesh smoothing energy and multi-view Gaussian rendering error drives alternating geometric refinement while preserving topological adaptivity. Consequently, our approach effectively constructs a unified and topologically coherent tetrahedral mesh. Extensive experiments demonstrate that our method outperforms state-of-the-art techniques by achieving superior geometric accuracy and producing coherent, single-connected tetrahedral meshes, thereby effectively bypassing the error-prone conventional tetrahedralization step for reconstructed surface meshes and streamlining downstream physical simulation.

</details>

#### 2026-07-08 - 3D Reconstruction of deciduous Trees using low-cost UAV- and Crane-based Photogrammetry for Monitoring Shoot Elongation across entire Canopies

**Authors:** Stephan Nebiker, Micha Tschanz, Nando Amport, Frederik Baumgarten
**Links:** [abs](https://arxiv.org/abs/2607.07905) - [pdf](https://arxiv.org/pdf/2607.07905)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, photogrammetry

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D Reconstruction of deciduous Trees using low-cost UAV- and Crane-based Photogrammetry for Monitoring Shoot Elongation across entire Canopies  
- 作者：Stephan Nebiker, Micha Tschanz, Nando Amport, Frederik Baumgarten  
- 出版日期：2026-07-08  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2607.07905  

### 一句话总结
本文探索利用低成本无人机（UAV）和吊车多相机系统进行摄影测量，以重建落叶乔木三维模型，从而监测整个树冠的枝条伸长（初级生长）。

### 研究问题
如何通过低成本摄影测量技术（UAV与CraneCam）在真实条件下获取落叶乔木高精度、高完整性的三维点云，以支持整个生长季内枝条伸长的连续监测。

### 核心思路/方法
1. 使用重量不足250g的消费级UAV和一套多相机CraneCam系统，在整个生长季内采集两个研究区的数据。  
2. 采用摄影测量数据采集与处理策略，重点分析三维点云的精度、分辨率和完整性。  
3. 引入一种创新的3D打印“地面真值”枝条，用于评估重建细部结构（如细枝条）的能力。  

### 主要贡献
1. 证明了消费级UAV（<250g）即可实现整棵树5-6 mm的点云精度。  
2. 不同无人机型号的三维重建完整性达到92%至98%。  
3. 提出了利用3D打印人造枝条作为基准，评估对细薄枝条等精细结构的重建效果。  
4. 探讨了基于摄影测量点云进行整树骨架化的初步实验与操作挑战。  

### 局限性
摘要未提供足够信息，无法明确说明该方法的适用场景限制、无法重建的枝条类型、不同天气或季节的影响，以及与其他传感器（如激光雷达）的对比结果。

### 阅读优先级
中  
**理由**：该研究针对树木初级生长监测这一特定生态学需求，方法上具有创新性（低成本、轻量化设备、高精度），并展示了实用结果。但摘要未涉及算法细节、实验对比或后续骨架化方法的具体效果，对于非生态遥感领域或无硬件部署计划的研究者可能参考价值有限。

</details>

<details>
<summary>Abstract</summary>

Tree growth determines how much CO2 is sequestered from the atmosphere and temporarily stored in woody biomass. At the same time tree growth is affected by increasing temperatures, more frequent drought periods, late frosts and other extreme events associated with climate change. While continuous measurements of radial (secondary) tree growth using dendrometers are well established, monitoring of shoot elongation (primary growth) has largely been neglected because suitable measurement techniques are lacking. As a result, the effects of climate change on primary tree growth remain insufficiently understood. This work aims at reconstructing native deciduous trees in 3D as a basis for measuring and monitoring shoot elongation over entire tree canopies. Here we explored the use of low-cost UAV photogrammetry and of a multi-camera CraneCam system under real-world conditions. Data were collected in two study areas over an entire growing season. We present sensor evaluations, photogrammetric data acquisition and processing strategies. A special focus is placed on the analysis of the resulting photogrammetric 3D point clouds in terms of accuracy, resolution and completeness. Results demonstrate 3D point accuracies of 5-6 mm for entire trees using consumer-grade UAVs weighing less than 250 g and a 3D reconstruction completeness between 92% and 98% depending on the UAV type. The paper introduces a novel 3Dprinted ground-truth branch to evaluate the capability to reconstructing fine-detail structures such as thin tree shoots. Finally, we discuss operational challenges and initial experiments towards a skeletonization of entire trees based on photogrammetric point clouds.

</details>

#### 2026-07-08 - Monocular Vision Based Control Framework for Grasping

**Authors:** Shail Jadav, Dongheui Lee
**Links:** [abs](https://arxiv.org/abs/2607.07897) - [pdf](https://arxiv.org/pdf/2607.07897)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Monocular Vision Based Control Framework for Grasping
- 作者：Shail Jadav, Dongheui Lee
- 出版日期：2026-07-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[论文摘要页](https://arxiv.org/abs/2607.07897) | [PDF](https://arxiv.org/pdf/2607.07897)

### 一句话总结
本文提出一种仅使用单目RGB视觉和位置控制夹爪的统一抓取框架，通过语言估计物体刚度并适应性地抓取软硬物体，在真实实验中验证了对多种食品及家庭物品的稳定抓取。

### 研究问题
如何在非结构化环境中，仅依靠单目视觉（无需触觉、物体模型或专用夹爪）实现对软性（可变形）和刚性物体的统一抓取控制。

### 核心思路/方法
框架融合多项计算机视觉技术：开放词汇目标检测、图像分割、边界感知点分配、实时点跟踪、单目深度估计，以及一个基于语言描述的刚度估计模型。该模型利用物体的语义信息预判其柔顺性，从而在接触前选择抓取策略。对于可变形物体，使用Procrustes距离（基于跟踪关键点）作为形变视觉代理来调整抓取；对于刚性物体，则通过跟踪点距离的缩放调节夹爪宽度。全部控制仅依赖RGB输入和位置控制夹爪。

### 主要贡献
1. 提出一个统一的单目视觉抓取框架，能同时处理软性（可变形）和刚性物体，无需专用传感器或物体模型。
2. 引入语言基础刚度估计模型，从物体语义推断其预期柔顺性，提供接触前的抓取策略先验。
3. 针对可变形物体设计基于Procrustes度量的抓取自适应方法，作为形变的视觉代理信号。
4. 在真实Franka Emika Research 3臂上，用多种软硬物体（生菜、马苏里拉奶酪、牛角包、纸巾、硬塑料瓶）验证了框架的有效性和泛化性。

### 局限性
摘要未提供足够信息评估局限性，例如在极端光照、遮挡、高速运动或完全透明物体上的表现。

### 阅读优先级
中  
理由：该方法将视觉与语言结合实现软硬物体统一抓取，具有传感器高效性和实际应用潜力，尤其适合食品处理等场景。但实验物体种类有限，且未评估极端情况下的鲁棒性，对于追求工程落地的读者可能有参考价值，理论创新性为中等。

</details>

<details>
<summary>Abstract</summary>

Grasping in unstructured environments requires handling objects with widely different mechanical properties, from soft and deformable items to rigid everyday objects. Most existing approaches address these categories separately and often rely on tactile sensing, object-specific models, or specialized grippers. In this paper, we present a unified monocular vision-based grasping framework that targets both soft and rigid objects within a single control pipeline, using only RGB input and a position-controlled gripper. The proposed system combines open-vocabulary object detection, image segmentation, boundary-aware point assignment, real-time point tracking, and monocular depth estimation to recover object motion and geometry from visual observations. A key component of the framework is a language-based stiffness estimation model that infers an object's expected compliance from its semantic description and provides an object-level prior for selecting the grasping strategy before contact. For deformable objects, grasp adaptation is governed by a Procrustes-based dissimilarity measure computed from tracked keypoints, which acts as a visual proxy for deformation. For rigid objects, the gripper width is regulated through the scaling of tracked point distances. We validate the proposed method in real-world pick-and-place experiments on a Franka Emika Research 3 arm using objects with substantially different mechanical properties, including lettuce, fresh mozzarella cheese, croissants, paper towels, and hard plastic bottles. Results demonstrate that the framework achieves stable grasping across both soft and rigid objects using visual feedback alone, highlighting a practical, sensor-efficient, and generalizable approach for food handling and household manipulation.

</details>

#### 2026-07-08 - Time-to-Collision Based Dynamic Obstacle Avoidance Using Pretrained Vision Models for Robots in Unstructured Environments

**Authors:** Erik Jagnandan, Mulugeta Haile, Gregory Barber, Pratik Chaudhari
**Links:** [abs](https://arxiv.org/abs/2607.07885) - [pdf](https://arxiv.org/pdf/2607.07885)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** bundle adjustment, depth estimation, monocular depth, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Time-to-Collision Based Dynamic Obstacle Avoidance Using Pretrained Vision Models for Robots in Unstructured Environments
- 作者：Erik Jagnandan, Mulugeta Haile, Gregory Barber, Pratik Chaudhari
- 出版日期：2026-07-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.07885

### 一句话总结
本文提出一种基于碰撞时间（TTC）的视觉动态避障方法，利用预训练深度估计和特征匹配模型，无需训练即可实现非结构化环境中的机器人避障，并在真实数据集上验证了数据高效性和可解释性。

### 研究问题
如何在非结构化户外环境中实现动态障碍物避障，同时避免大规模机器人专用训练数据和仿真策略带来的数据效率低、仿真到现实迁移困难等问题。

### 核心思路/方法
- 利用预训练单目深度估计模型 UniDepth 从 RGB 视频生成稠密深度图，无需立体相机或激光雷达。
- 扩展 SuperPoint 和 SuperGlue 特征匹配管线，在长帧序列中跟踪关键点，并通过相机内参和预测深度将2D像素投影到3D。
- 对3D关键点进行束调整（bundle adjustment）以优化位姿，计算每个关键点的碰撞时间（TTC）。
- 在地平面选择2D运动基元，使机器人远离最小TTC关键点的最近接近点。

### 主要贡献
1. 提出一种完全基于真实世界数据、无需模型训练的视觉动态避障方法，避免了仿真到现实的迁移问题。
2. 利用预训练模型（UniDepth、SuperPoint、SuperGlue）实现数据高效性，仅需74秒数据用于超参数调优，无需数千小时训练数据。
3. 在M3ED数据集上验证性能：识别TTC<1秒帧的精确率0.49、召回率0.38；正确避障方向生成率为84%；对22个物理障碍中的20个检测到至少一个TTC<1秒的帧。
4. 方法保持可解释性和泛化性，适用于多种障碍物类型。

### 局限性
摘要未提供足够信息。未提及方法在复杂场景（如密集障碍物、高速运动）下的鲁棒性、实时性表现，或对光照、纹理等环境因素的敏感性。

### 阅读优先级
**高**
理由：本文针对动态避障这一机器人领域核心难题，提出了一种无需训练、数据高效的解决方案，并使用了预训练视觉模型，具有较强的实用价值和可迁移性。实验结果在真实数据集上表现合理，且方法可解释性强，适合关注自主导航、避障与计算机视觉交叉研究的读者。

</details>

<details>
<summary>Abstract</summary>

Dynamic obstacle avoidance in unstructured outdoor environments remains a critical challenge for autonomous mobile robots, particularly when large-scale robot-specific training data and simulation-based policies are impractical. We present a data-efficient, interpretable method for vision-based dynamic obstacle avoidance that operates entirely on real-world data, avoiding the sim-to-real transfer problem inherent in simulation-trained policies. Our approach leverages UniDepth, a large pretrained monocular depth estimation model, to produce dense depth maps from RGB video without requiring stereo cameras or LiDAR at inference time. Dynamic obstacle avoidance is achieved by extending the SuperPoint and SuperGlue feature correspondence pipeline to track keypoints across long frame sequences, projecting their 2D pixel-space positions into 3D using camera intrinsics and predicted depth, running bundle adjustment initialized from these 3D keypoints, and computing per-keypoint time-to-collision (TTC). A 2D motion primitive in the ground plane is then selected to move the robot away from the closest point of approach of the minimum-TTC keypoint. Evaluated on real-world data from the M3ED dataset, our pipeline achieves a precision of 0.49 and a recall of 0.38 in identifying frames with a ground truth TTC below 1 second, and correctly generates the evasive motion direction in 84\% of true positive detections. Crucially, it detects at least one frame with TTC less than 1 second for 20 out of 22 unique physical obstacles present in our test sequences. Unlike end-to-end learned methods that demand thousands of hours of robot-specific training data, our approach eliminates model training entirely, requiring only 74 seconds of data for hyperparameter tuning. This demonstrates exceptional data efficiency while preserving interpretable and generalizable behavior across diverse obstacle types.

</details>

#### 2026-07-08 - GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

**Authors:** Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang
**Links:** [abs](https://arxiv.org/abs/2607.07452) - [pdf](https://arxiv.org/pdf/2607.07452)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, SLAM, visual SLAM, geometric reconstruction, Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, robotics, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM
- 作者：Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang
- 出版日期：2026-07-08T14:22:05Z
- 分类：3D Reconstruction & Multi-view Geometry (主要), Neural Scene Representations & Rendering (次要)
- 链接：https://arxiv.org/abs/2607.07452

### 一句话总结
本文提出了一种仅利用高斯分布的空间参数进行纯几何重建的SLAM方法GeoGS-SLAM，通过简化表征和配套的优化框架，在在线建图效率和几何重建质量上优于现有方法。

### 研究问题
现有基于3D高斯泼溅的密集SLAM框架同时关注外观和几何建模，但SLAM下游任务（如导航、避障）更依赖于精确的几何信息而非逼真渲染。因此，研究问题为：**是否可能仅通过3D高斯泼溅进行场景几何重建，而不进行外观建模？**

### 核心思路/方法
1. **纯几何高斯泼溅（GeoGS）**：仅保留高斯原语的空间参数（如位置、协方差等），完全舍弃颜色等外观参数，将每个原语的参数数量降低超过80%。
2. **训练框架**：通过单视图和多视图的几何与光度监督来优化高斯原语，并利用**局部平面驱动初始化**使原语更好地对齐局部结构，加速几何收敛。
3. **地图更新策略**：针对回环检测，提出一种全局变换高斯地图的策略，使其与校正后的位姿估计对齐，避免因视角不一致的位姿校正导致的地图撕裂。

### 主要贡献
1. 提出纯几何高斯泼溅表征（GeoGS），显著减少原语参数数量并提高几何收敛速度。
2. 构建基于该表征的密集单目SLAM系统GeoGS-SLAM，并设计有效的单/多视图几何-光度监督训练框架。
3. 提出一种回环地图更新策略，解决现有方法中的地图撕裂问题。
4. 在合成和真实世界基准上，证明该方法在在线建图效率和几何重建质量方面均优于当前最先进方法。

### 局限性
摘要未提供足够信息。文中未提及该方法的潜在局限性，例如对动态场景的鲁棒性、计算资源需求或在大规模场景下的扩展性。

### 阅读优先级
**高**。
理由：该工作针对SLAM领域核心的几何建图需求，提出了一种简化但高效的高斯泼溅变体，实验表明在效率和精度上均有提升。对于从事密集SLAM或3D高斯泼溅应用的研究者有较强参考价值，且方法创新点清晰。

</details>

<details>
<summary>Abstract</summary>

Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoidance, rely primarily on accurate spatial geometry rather than photorealistic rendering. This observation raises a natural question: Is it feasible for 3DGS to perform 3D reconstruction without scene appearance modeling? Motivated by this, we propose Geometry-only Gaussian Splatting (GeoGS), which directly reconstructs scene geometry, and further present GeoGS-SLAM, a dense visual SLAM system built upon this representation. Specifically, GeoGS retains only spatial parameters to reduce the number of per-primitive parameters by over 80%. In contrast to existing 3DGS methods, GeoGS focuses solely on geometric reconstruction, which significantly reduces the number of Gaussian primitives, accelerates geometric convergence, and enhances robustness to illumination variations. In addition, we present an effective training framework that optimizes the Gaussian primitives via single-view and multi-view geometric and photometric supervision, and speeds up geometry convergence with a local-plane driven initialization that better aligns primitives with local structures. Furthermore, we introduce a map update strategy for loop closure that globally transforms the Gaussian map to align it with the corrected pose estimates, thereby preventing map tearing caused by inconsistent per-viewpoint pose corrections in existing methods. Extensive experiments on synthetic and real-world benchmarks demonstrate that our method outperforms SOTA methods in terms of online mapping efficiency and geometric reconstruction quality.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-14 - ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting

**Authors:** Cheng-Tai Hsieh, Jiwei Shan, Han Fang, Jianshu Hu, Tao Ni, Lijun Han, Yutong Ban, Shing Shin Cheng, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2607.12785) - [pdf](https://arxiv.org/pdf/2607.12785)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, neural rendering, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating beyond the training trajectory.In this work, we propose ExtraGS, a framework for enhancing endoscopic view extrapolation via diffusion-guided 3D Gaussian Splatting. Starting from an initial reconstruction, we introduce an uncertainty-guided virtual camera sampling strategy to actively explore blind spots and maximize information gain. The rendered views from these sampled locations are refined using a diffusion model to recover plausible anatomical structures, producing pseudo observations that guide further optimization. To prevent the generated content from degrading reliable regions, we adopt a confidence-weighted fine-tuning strategy when incorporating these pseudo observations.Extensive experiments on multiple public endoscopic datasets demonstrate that ExtraGS significantly reduces extrapolation artifacts and achieves state-of-the-art performance in endoscopic novel view synthesis.

</details>

#### 2026-07-14 - GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR

**Authors:** Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu
**Links:** [abs](https://arxiv.org/abs/2607.12641) - [pdf](https://arxiv.org/pdf/2607.12641)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, VR, virtual reality

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

#### 2026-07-09 - Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery

**Authors:** Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos
**Links:** [abs](https://arxiv.org/abs/2607.08408) - [pdf](https://arxiv.org/pdf/2607.08408)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, scene representation, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery
- 作者：Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos
- 出版日期：2026-07-09
- 分类：Neural Scene Representations & Rendering；3D Reconstruction & Multi-view Geometry
- 链接：摘要：https://arxiv.org/abs/2607.08408 ；PDF：https://arxiv.org/pdf/2607.08408

### 一句话总结
Track2Map是一种在线、可变形3D高斯溅射SLAM管线，能够从手术视频中联合优化相机轨迹与三维可变形场景，无需依赖机器人运动学先验。

### 研究问题
如何在机器人辅助微创手术（RAMIS）中，从手术视频在线进行稠密、可变形三维解剖重建，并在缺少或带有噪声的相机轨迹先验下实现鲁棒的定位与建图（SLAM）。

### 核心思路/方法
1. **在线联合优化**：构建一个在线3D高斯溅射管线，同时优化相机轨迹和三维可变形场景。
2. **轨迹锚定变形初始化**：使用密集的二维点轨迹进行变形初始化，以稳定存在组织运动和模糊视觉线索时的优化过程。
3. **运动感知位姿优化**：利用点轨迹统计信息，通过检测静态相机时期来分离相机运动与场景变形，并在增量建图过程中减少漂移。

### 主要贡献
- 提出Track2Map，一种在线的可变形SLAM方法，能直接从未知或带噪的相机轨迹先验的术中视频中联合优化相机位姿和场景。
- 引入轨迹锚定变形初始化策略，利用密集2D点轨迹稳定优化。
- 利用点轨迹统计实现运动感知位姿优化，有效分离相机运动与组织变形，减少漂移。
- 在StereoMIS数据集上的实验表明，Track2Map在重建质量和相机轨迹估计上优于现有SLAM方法，甚至可与使用轨迹先验的非SLAM方法竞争。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对手术机器人视觉中的核心问题（缺少相机先验时的在线可变形SLAM）提出了新颖的联合优化管线，并展示了优于现有方法的实验性能。对于从事手术机器人、SLAM或可变形场景重建的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian splatting is the current state-of-the-art for dense, deformable 3D anatomy reconstruction in robot-assisted minimally invasive surgery (RAMIS); however, most pipelines are offline and depend on accurate camera trajectory priors (often from robotic kinematics), limiting applicability when priors are missing or noisy. To address these limitations, we propose Track2Map, an online 3D Gaussian Splatting pipeline that jointly optimizes camera trajectory and 3D deformable scene representation directly from surgical video. Track2Map is therefore capable of robust 3D reconstructions when camera trajectory priors are either absent or noisy, and due to its online nature it effectively works as a Simultaneous Localisation and Mapping (SLAM) method. To stabilize optimization in the presence of tissue motion and ambiguous visual cues, we introduce a track-anchored deformation initialization using dense 2D point tracks. Track statistics are further utilized to disentangle camera motion from scene deformation by detecting static camera periods and reducing drift during incremental mapping. Experiments on StereoMIS show improved reconstruction quality and camera trajectory against competing SLAM methods, as well as compared to non-SLAM methods that utilize camera trajectory priors. The code is available at https://track2map.github.io/.

</details>

#### 2026-07-09 - LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting

**Authors:** Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan
**Links:** [abs](https://arxiv.org/abs/2607.08016) - [pdf](https://arxiv.org/pdf/2607.08016)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting
- 作者：Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan
- 出版日期：2026-07-09
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.08016

### 一句话总结
LightCrafter 提出一种混合流水线，通过将视频重光照转化为对基于物理渲染（PBR）代理视频的翻译，利用视频扩散模型精细调整以实现可控且时间一致的重光照。

### 研究问题
如何在长视频中实现既保持时间一致性、又符合物理光照规律（如全局光照）的可控重光照，同时克服传统逆渲染方法噪声大、生成式方法控制受限的缺陷。

### 核心思路/方法
核心思路是构建一个混合流水线：不为直接从输入视频翻译到目标光照下的视频，而是先通过逆渲染和PBR生成输入视频在目标光照下的代理渲染视频，然后使用经过合成视频对和真实无配对视频微调的CogVideoX扩散模型，将该PBR代理视频翻译为最终的重光照结果。这样，光照目标已被“烘培”进PBR代理中，扩散模型无需学习环境映射等光照概念，从而提升控制精度和长时一致性。

### 主要贡献
1. 提出LightCrafter混合流水线，结合PBR渲染和视频扩散模型，实现可控且一致的重光照。
2. 通过将光照目标嵌入PBR代理，简化扩散模型的输入空间，增强光照控制灵活性并自然保持长时间一致性。
3. 在现有真实世界重光照基准上超越此前最优方法，并贡献了用于进一步分析的合成基准。
4. 将公开发布数据集、基准、评估指标和代码。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对视频重光照中的关键难题（时间一致性与物理真实性）提出了新颖的混合方法，在基准上取得超越结果，且涉及当前热门的扩散模型与物理渲染结合，方法具有实用潜力。

</details>

<details>
<summary>Abstract</summary>

Video relighting requires balancing long-form temporal consistency with a physically grounded understanding of light transport, which depends on accurate estimation of intrinsic scene properties such as materials, geometry, and illumination. Existing methods follow two paradigms: (1) reconstruct a video's photometric properties via inverse rendering and relight them to a target illumination via forward rendering, using physically-based rendering (PBR) or a neural renderer; these suffer from noisy reconstructions and struggle with hard-to-model effects such as global illumination. (2) Frame the task as generative video-to-video translation conditioned on relighting targets (a target environment map or text); this limits relighting control and temporal stability, since diffusion models struggle to translate long-form videos, and is constrained by the availability of input/relit training pairs. We propose LightCrafter, a hybrid pipeline that reformulates video relighting as video translation of a proxy video: rather than translating the input video directly to the target, we translate a PBR rendering of the input under the target illumination to the final target. This bakes illumination targets into the PBR proxy, removing the need to teach the diffusion model illumination concepts like environment maps, and enables more intricate lighting control while naturally providing long-form temporal consistency. We show PBR renders alone already outperform some prior art but struggle with effects like global illumination; to capture these, we leverage photometric priors in video generation models by post-training CogVideoX on synthetic video pairs and real-world unpaired videos. We outperform prior state-of-the-art on existing real-world relighting benchmarks and contribute a synthetic benchmark for further analysis. We will release our dataset, benchmark, metrics, and code.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-14 - TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

**Authors:** Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee, Tim Wang, Wei Zhan
**Links:** [abs](https://arxiv.org/abs/2607.13028) - [pdf](https://arxiv.org/pdf/2607.13028)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

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

#### 2026-07-11 - PrismAD: Decoupled Planning via Semantic Mixture-of-Planners for End-to-End Autonomous Driving

**Authors:** Kang Ding, Zhigui Lin, Hongsong Wang, Jie Gui, Qi Liu, Zhe Wang, Luqi Tang, Lei He
**Links:** [abs](https://arxiv.org/abs/2607.10336) - [pdf](https://arxiv.org/pdf/2607.10336)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PrismAD: Decoupled Planning via Semantic Mixture-of-Planners for End-to-End Autonomous Driving
- 作者：Kang Ding, Zhigui Lin, Hongsong Wang, Jie Gui, Qi Liu, Zhe Wang, Luqi Tang, Lei He
- 出版日期：2026-07-11
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.10336

### 一句话总结
PrismAD 提出一种基于语义混合规划器的解耦式端到端自动驾驶框架，通过将场景token按语义分组并分配给独立专家，提升运动规划和自我规划效果。

### 研究问题
现有端到端规划器将异构场景token聚合到耦合表示空间，迫使单一规划分支联合建模智能体交互、道路几何和驾驶意图，这削弱了各因素具体推理能力，并模糊了不同规划线索的贡献。

### 核心思路/方法
- 将场景token划分为交互、几何、意图三组，分别分配给参数独立但架构相同的专家。
- 每个专家学习特定规划子任务（运动预测或自我规划）的表示。
- 引入语义感知路由器，自适应地为运动预测和自我规划分配不同的路由权重，聚合专家预测。
- 采用稀疏Top-K激活和噪声门控，提升路由鲁棒性并减少不必要的专家计算。

### 主要贡献
- 提出解耦规划范式，通过语义分组和独立专家增强各规划线索的专用推理。
- 设计混合专家路由机制，在运动预测和自我规划间动态分配权重，实现自适应聚合。
- 在nuScenes开放循环数据集和NeuroNCAP闭合循环基准上展示出竞争性能。

### 局限性
摘要未提供关于模型局限性、失败案例或计算复杂度的具体信息。

### 阅读优先级
中。理由：该工作聚焦端到端自动驾驶规划中的表示解耦问题，方法设计清晰（混合专家架构），但性能仅描述为“竞争性”，未给出量化对比细节；同时摘要长度较短，缺少充分的实验验证说明，适合对解耦规划范式感兴趣的读者初步了解，但需阅读全文才能评估实际效果优势。

</details>

<details>
<summary>Abstract</summary>

This letter presents PrismAD, a decoupled end-to-end autonomous driving framework based on a Semantic Mixture-of-Planners. Existing planners usually aggregate heterogeneous scene tokens into a coupled representation space, forcing a single planning branch to jointly model agent interaction, road geometry, and driving intention. Such coupling may weaken factor-specific reasoning and obscure the contribution of different planning cues. To address this limitation, PrismAD partitions scene tokens into interaction, geometry, and intent groups, and assigns them to independent planning experts with the same architecture but separate parameters. Each expert learns a specialized motion-planning representation, while a semantics-aware router adaptively aggregates expert predictions with separate routing weights for motion prediction and ego planning. Sparse top-$K$ activation with noisy gating is further introduced to improve routing robustness and reduce unnecessary expert computation. Extensive experiments on the nuScenes open-loop dataset and NeuroNCAP closed-loop benchmark demonstrate that PrismAD exhibits competitive performance. Our code will be released soon.

</details>

#### 2026-07-09 - DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

**Authors:** Yunchao Yao, Zhuxiu Xu, Tianqi Zhang, Zixian Liu, Sikai Li, Zhenyu Wei, Feng Chen, Dihong Huang, Kechang Wan, Chenyang Ma, Shuqi Zhao, Shenghua Gao, Masayoshi Tomizuka, Yi Ma, Mingyu Ding
**Links:** [abs](https://arxiv.org/abs/2607.08751) - [pdf](https://arxiv.org/pdf/2607.08751)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation
- 作者：Yunchao Yao, Zhuxiu Xu, Tianqi Zhang, Zixian Liu, Sikai Li, Zhenyu Wei, Feng Chen, Dihong Huang, Kechang Wan, Chenyang Ma, Shuqi Zhao, Shenghua Gao, Masayoshi Tomizuka, Yi Ma, Mingyu Ding
- 出版日期：2026-07-09
- 分类：具身智能/机器人/AR应用
- 链接：https://arxiv.org/abs/2607.08751

### 一句话总结
该论文提出了DexVerse，一个大规模模块化灵巧操作基准，包含100项任务、多种机器人构型、可配置视觉变化和3,180条演示数据，并评测了多种代表性方法，揭示了任务泛化和视觉运动鲁棒性方面的显著挑战。

### 研究问题
现有灵巧操作基准在任务多样性、数据覆盖范围、机器人构型支持以及可控视觉变化方面存在局限，难以系统性地评估策略在跨任务和跨构型下的泛化能力。

### 核心思路/方法
构建一个模块化基准，具体包括：
1. 集成100项涵盖抓取、重定位、交互式物体操作、工具使用、双手协调、非抓取控制、接触丰富行为、多目标执行以及长时多阶段任务等多种技能的任务。
2. 支持3种机器人臂和6种灵巧手，并具备可扩展性。
3. 提供可配置的纹理、背景、光照和相机视角等视觉变化，用于评估视觉运动泛化。
4. 提供一个基于VR的遥操作接口，并收集3,180条包含本体感受、RGB、深度、点云和状态观测的同步演示数据。
5. 选取Diffusion Policy、DP3、OpenVLA和π₀.₅四种代表性方法在19项任务上进行基准测试。

### 主要贡献
1. 提出了一个大规模、模块化的灵巧操作基准DexVerse，包含丰富的任务、构型及视觉变化。
2. 提供了3,180条多模态同步演示数据及VR遥操作接口，便于获取高质量演示。
3. 在19项任务上对多种代表性方法进行了系统基准测试，揭示了跨任务泛化与视觉运动鲁棒性方面的显著挑战，验证了DexVerse作为通用灵巧操作测试平台的价值。

### 局限性
摘要未提供关于DexVerse基准在真实机器人部署、计算成本、任务难度分布、数据收集成本以及所测试方法在其他任务上的性能上限等具体实验细节或局限性信息。

### 阅读优先级
中
理由：该论文提供了一个综合性的基准和评测结果，对于研究灵巧操作泛化问题、需要多任务多构型评估资源的领域具有直接参考价值；但摘要未深入分析算法性能差异或具体实验结果，故优先级设为中等。

</details>

<details>
<summary>Abstract</summary>

Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering studies of cross-task and cross-embodiment generalization. We present DexVerse, a large-scale and modular benchmark for dexterous manipulation. DexVerse includes 100 tasks spanning a broad range of manipulation skills, including object grasping and relocation, articulated-object interaction, functional tool use, bimanual coordination, non-prehensile control, contact-rich behaviors, multi-goal execution, and long-horizon multi-stage task completion. It supports 3 robot arms and 6 dexterous hands, and is extensible to new tasks, assets, and embodiments. To evaluate visuomotor generalization, DexVerse provides configurable visual variations in textures, background, lighting, and camera viewpoints. We further provide a VR-based teleoperation interface and 3,180 demonstrations with synchronized proprioceptive, RGB, depth, point-cloud, and state observations. We benchmark representative methods, including Diffusion Policy, DP3, OpenVLA, and $π_{0.5}$, across 19 tasks. Results reveal substantial challenges in task generalization and visuomotor robustness, establishing DexVerse as a promising testbed for general-purpose dexterous manipulation. Project page: https://ycyao216.github.io/DexVerse.site

</details>

#### 2026-07-09 - WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving

**Authors:** Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, Jia Hu, Binyang Song
**Links:** [abs](https://arxiv.org/abs/2607.08375) - [pdf](https://arxiv.org/pdf/2607.08375)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, autonomous driving, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving
- 作者：Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, Jia Hu, Binyang Song
- 出版日期：2026-07-09
- 分类：Embodied / Robotics / AR Applications（主要类别）；未提供次要类别
- 链接：摘要链接: https://arxiv.org/abs/2607.08375；PDF链接: https://arxiv.org/pdf/2607.08375

### 一句话总结
本文提出WCog-VLA，一种双层次世界认知视觉-语言-动作模型，通过结合语义世界预测与生成世界演化，在NAVSIM基准上实现PDMS评分92.9的领先性能，推动端到端自动驾驶从被动驾驶向主动驾驶转变。

### 研究问题
现有视觉-语言-动作（VLA）模型在端到端自动驾驶中缺乏全面的世界认知，或存在碎片化的世界预见能力，导致模型只能进行被动驾驶（reactive driving），无法实现主动驾驶（proactive driving）。

### 核心思路/方法
- **双层次世界认知框架（Dual-Level World-Cognitive）**：
  - **语义层次**：通过集成3D空间感知和注入代理令牌（agent tokens）来捕捉世界动态，并实现面向博弈论链式思考（Game-theoretic Chain-of-Thought, Game-CoT）推理，统一世界认知与推理。
  - **生成层次**：引入对齐的解耦扩散Transformer（Aligned Decoupled Diffusion Transformer, ADDT）作为生成世界模型，合成物理上合理的多智能体联合轨迹；通过场景表示对齐减少去噪步骤，显著加速推理。
- **数据集构建**：创建包含85,000个Game-CoT注释的大规模数据集，支持策略推理训练。
- **实验验证**：在NAVSIM基准上进行了广泛实验，结果达到SOTA（PDMS评分92.9）。

### 主要贡献
1. 提出WCog-VLA，首个将语义世界预测与生成世界演化结合的双层次世界认知VLA框架，实现主动驾驶。
2. 提出Game-CoT推理机制，将博弈论思想融入视觉-语言推理链。
3. 提出ADDT生成模型，通过场景表示对齐减少去噪步骤，加速推理。
4. 构建包含85k Game-CoT注释的大规模数据集，促进策略推理研究。
5. 在NAVSIM基准上取得SOTA性能（PDMS评分92.9）。

### 局限性
摘要未提供足够信息（例如未提及模型的计算开销、在不同场景下的泛化能力、对异常或边缘情况的鲁棒性等）。

### 阅读优先级
**高**  
理由：该论文针对自动驾驶中VLA模型缺乏世界认知的核心问题，提出了兼具语义推理与生成预测的双层次框架，并在权威基准上取得SOTA结果。方法创新性较强（如Game-CoT、ADDT对齐策略），且附带大规模数据集，对主动驾驶和端到端自动驾驶领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-VLA unifies world cognition and reasoning by incorporating 3D spatial perception and injecting agent tokens to capture the world dynamics, while concurrently enabling Game-theoretic Chain-of-Thought (Game-CoT) reasoning. At the generative level, we introduce the Aligned Decoupled Diffusion Transformer (ADDT) as a powerful generative world model that synthesizes physically-plausible joint multi-agent trajectories. Through scene representation alignment, ADDT reduces the number of denoising steps required and thus significantly accelerates inference. To facilitate strategic reasoning, we further construct a large-scale dataset featuring 85k Game-CoT annotations. Extensive experiments on the NAVSIM benchmark demonstrate that WCog-VLA achieves a State-Of-The-Art (SOTA) PDMS score of 92.9.

</details>

#### 2026-07-08 - CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis

**Authors:** Kaicong Huang, Meng Ma, Ruimin Ke
**Links:** [abs](https://arxiv.org/abs/2607.07601) - [pdf](https://arxiv.org/pdf/2607.07601)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis
- 作者：Kaicong Huang, Meng Ma, Ruimin Ke
- 出版日期：2026-07-08T16:20:19Z（摘要标注日期）
- 分类：Embodied / Robotics / AR Applications（主要分类）
- 链接：https://arxiv.org/abs/2607.07601（PDF: https://arxiv.org/pdf/2607.07601）

### 一句话总结
本文提出CARLA-GS，一个模块化的自动驾驶边缘案例合成框架，通过解耦视觉表示、语义推理与物理执行，并利用多智能体LLM和CARLA仿真器，生成逼真、时空一致且物理可行的极端场景视频。

### 研究问题
如何在统一的框架中生成自动驾驶中的罕见、安全关键型边缘案例（corner cases），同时确保视觉逼真度、时空一致性以及物理运动可行性？现有方法或孤立处理场景/轨迹组件，或端到端生成但难以兼顾一致性。

### 核心思路/方法
提出CARLA-GS模块化流水线，具体包括：
1. **视觉表示**：从真实驾驶数据重建可编辑的3D高斯场景，并增加几何一致性约束。
2. **语义推理**：使用多智能体大语言模型（LLM）进行场景级推理，识别危险交互并生成意图级航点轨迹。
3. **物理执行**：将低层运动控制委托给CARLA仿真器，利用PID控制器确保运动学与动力学可行性。
4. **渲染输出**：将模拟的车辆状态重新投影到高斯场景中，生成以自我为中心的逼真视频。

### 主要贡献
- 提出了一个解耦的模块化管线，统一了视觉表示、语义推理与物理仿真。
- 实现了可控的边缘案例生成，生成视频在逼真度、时空一致性与物理可行性上表现良好（在Waymo Open Dataset上经定量和定性验证）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文针对自动驾驶安全评估中的核心挑战——边缘案例合成，提出了将LLM推理、物理仿真与3D场景重建相结合的创新模块化方案，且在Waymo数据集上验证了效果。对于关注自动驾驶安全验证、仿真生成及多模态融合的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Safety evaluation for autonomous driving is dominated by rare, safety-critical interactions, motivating simulators that can deliberately synthesize corner cases with photorealistic observations. Corner-case generation is inherently a multi-source problem spanning visual representation, scene reasoning, and vehicle trajectory generation and control. Prior knowledge- and model-based approaches typically focus on scene or trajectory components in isolation, while diffusion-based methods attempt end-to-end generation but still struggle to ensure spatiotemporal consistency and physical realism. To unify these aspects within a single framework, we propose CARLA-GS, a modular corner-case synthesis pipeline that decouples visual representation, semantic reasoning, and physics-based execution while maintaining tight cross-module coupling. Starting from real driving data, we reconstruct an editable gaussian scene with additional geometry-consistent constraints. A multi-agent LLM then performs scene-level reasoning to identify risky interactions and generate intent-level waypoint trajectories, while the low-level motion control is delegated to CARLA, where a PID controller ensures kinematic and dynamic feasibility. The simulated vehicle states are finally re-projected into the gaussian scene for ego-centric rendering. This design enables high-level semantic reasoning, low-level physically executable motion, and photorealistic corner-case generation within a unified pipeline. Experiments on the Waymo Open Dataset show, both quantitatively and qualitatively, that our framework enables controllable corner-case generation and produces photorealistic, spatiotemporally consistent videos aligned with semantic intent and physically feasible motion.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
