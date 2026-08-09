# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：64
- 分类分布：
  - Neural Scene Representations & Rendering: 23
  - 3D Reconstruction & Multi-view Geometry: 20
  - Embodied / Robotics / AR Applications: 10
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **3D Gaussian Splatting (3DGS) 生态的分化与深化**：今日列表中有超过六篇论文涉及 3DGS 或其衍生表示，但已从早期"如何渲染更好"转向"如何压缩、蒸馏、注入先验并扩展其物理功能"。G²ARD-GS（压缩蒸馏）、CDSeg（标签载体）、AV-MSF（声学模态扩展）、ESVR（体渲染范式改写）、RORA（关节运动与仿真资产）等共同表明，3DGS已从纯粹的渲染工具演变为**多用途场景表示基础设施**。

2. **几何先验与置信度信息成为重建质量的关键杠杆**：多篇论文将外部几何先验（深度、法线、点云、控制点）注入重建或定位流程。Confidence matters 明确发现多视图预测配合**置信度图**显著改善重建；Dense Metric Depth Completion 依赖合成 dToF 仿真管线驱动的深度引导 Transformer；Differential 6-DOF Pose Estimation 则利用已知 3D 控制点的几何约束实现标定误差免疫。先验的**来源、置信度估计和注入方式**正在成为新的研究焦点。

3. **从"重建静态场景"走向"重建可交互、可仿真资产"**：RORA 提出从单段静态视频重建带准确关节的仿真就绪资产；AV-MSF 将冲击声音场作为对象属性重建；VIDP 则将可变阻抗控制策略与运动学演示结合。这表明社区正加速将重建结果用于**机器人学习、物理仿真和交互任务**，而非仅用于逼真渲染。

4. **生成式模型与显式几何的融合成为大基线/稀疏输入重建的主流解法**：UniWorld-View 将显式 3D 引导与视频扩散模型耦合，解决大基线新视图合成；Engram-E2VID 通过"外观印记"与扩散先验结合实现事件到视频重建。生成式先验被用来**补全显式几何无法覆盖的区域**，成为稀疏观测下重建的新范式。

5. **数据资产化：领域专用基准和多模态数据集的密集涌现**：OmniMech（百万级工业 CAD 基准）、EventKitchen（立体事件相机厨房数据集）、EgoAffordance（204K 片段人类操作可供性数据集）及 VIDP 的多样演示数据共同显示，**构建高质量、大规模、领域专用的数据资产是当前推动 3D 重建与机器人学习前进的关键瓶颈和突破口**。

---

#### 技术路线观察

- **几何基础模型**：今日相关论文侧重将几何先验（深度、法线、点云）作为条件信息注入 Transformer 或 GS 框架。Dense Metric Depth Completion 采用双分支 ViT 编码器加掩码联合注意力；Confidence matters 则验证了多视图基础模型（VGGT）输出的置信度图对重建质量的增益。核心思路是"以几何引导视觉、以置信度约束几何"。

- **3D/4D 重建**：细分明显。一类走**稀疏向稠密**路线（dToF 深度补全、单次结构光重建）；另一类走**大基线生成式路线**（UniWorld-View）；还有一类聚焦**度量精度与标定鲁棒性**（Beyond Reprojection Error、Differential 6-DOF）。重建的评估标准也正在从 PSNR/SSIM 扩展到几何精度、配准成功率甚至交互可用性。

- **神经场景表示**：3DGS 依然是绝对主流，但方向分化明显。G²ARD-GS 做压缩蒸馏，ESVR 改椭球原语并直接学习原始体数据，FlaRe 将高斯原语与"可光线追踪的显式几何"结合以实现反射/折射，CDSeg 将高斯基元用作标签载体。概括而言：**原语的几何可解释性、显式可寻址性、跨域复用性日益重要**，纯隐式神经辐射场讨论减少。

- **机器人/AR 应用**：核心矛盾从感知精度转向**物理可靠性与任务适配**。VIDP 解决变阻抗控制的隐式顺应性推断；VLAff 将可供性（视觉/抓取/轨迹）从人类第一人称视频中提取；RORA 生成带关节的仿真资产；腹腔镜单次深度感知则逼近实时手术引导需求。这些工作共同指向"重建结果必须服务于后续的决策、交互和闭环控制"。

---

#### 值得优先阅读的论文

1. **G²ARD-GS: Geometry-Guided Anchor-Regularized Gaussian Splatting Distillation**（2608.05704）— 直接解决 3DGS 大规模应用的最大瓶颈（百万级原语、存储/渲染成本），在 5×-30× 压缩下仍提升 PSNR 3.2-6.8 dB，且保留几何复用能力。对整个 3DGS 实用化方向具有直接指导意义。

2. **VIDP: Variable Impedance Diffusion Policy**（2608.06210）— 将扩散策略与变阻抗控制结合，并解决"顺应性作为隐藏变量"这一根本难点。对接触丰富的机器人操作具有很强的方向引领性。

3. **OmniMech**（2608.05539）— 百万级工业机械设计基准，覆盖四个任务（CAD 程序合成、图到 3D 推理、标注引导推理、工具使用）。该基准很可能成为评估 VLM 细粒度几何理解能力的标准平台，值得提前熟悉。

4. **UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models**（2608.04701）— 结合显式 3D 引导与视频扩散模型解决大基线新视图合成，是"生成+重建"融合范式的代表性工作，且支持输出多视图视频用于下游动态 3DGS 重建。

5. **Floating Radiance Networks (FlaRe)**（2608.05920）— 将可光线追踪的显式几何（平面高斯原语）与连续辐射场统一，支持反射、折射、透明、阴影和原语级编辑。其"表达力+可操作性"兼顾的设计思路可能与未来神经渲染与图形工作流融合的方向高度相关。

---

#### 可能的研究机会

- **"压缩蒸馏 + 置信度引导"的 3DGS 一体化方案**：G²ARD-GS 与 Confidence matters 各自解决压缩和先验注入问题，但目前没有统一框架在压缩过程中同时利用几何先验及其置信度图来引导原语合并和外观恢复。此类组合可能在保持几何精度的同时进一步突破压缩比上限。

- **将变阻抗学习从操作器推广到全身移动操作**：VIDP 证明了从运动学数据提取刚度分布的可行性，但仅限于操作器层面。推广到包含移动底盘、双臂协调的场景，并引入多模态观测（力觉、触觉）与 TP-DAMM 结合，是自然的延伸方向。

- **面向交互重放的高斯关节资产自动生成**：RORA 的关节重建依赖人工分组和确认，效率仍有瓶颈。结合 VLAff 提取的抓取/轨迹可供性与 OmniMech 的机械结构先验，可能实现关节结构的自动化建议乃至端到端生成。

- **事件相机在大基线/动态场景中的重建潜力**：EventKitchen 提供了立体事件数据，Engram-E2VID 展示了事件+参考帧的生成式重建。但两者的结合点（如用立体事件驱动大基线新视图合成）尚未被直接探索，尤其在厨房这类高动态、快速互动物体场景。

- **测度级标定与重建的统一评估框架**：Beyond Reprojection Error 指出现有标定评估指标的误导性，Differential 6-DOF 又提供了标定误差免疫的估计方法。构建一套基于光线/射线的统一评估体系，贯穿标定-重建-定位全链路，可能大幅推动重建精度的可量化提升。

---

#### 风险和不确定性

- **摘要不足以确认泛化能力**：G²ARD-GS 的实验主要基于 MatrixCity 和 Cambridge 数据集；VIDP 只报告了真实世界实验的相对优劣，未给出失败模式；FlaRe 的定量结果在摘要中未提及具体数值。这些都需要通读全文或复

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-07T09:36:40-04:00
**Total number of papers:** 56
**Number of papers added in the latest update:** 10
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

### 2026-08

#### 2026-08-06 - Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction

**Authors:** Hongyu Zhou, Zorah Lähner
**Links:** [abs](https://arxiv.org/abs/2608.06117) - [pdf](https://arxiv.org/pdf/2608.06117)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** visual geometry grounded transformer, VGGT, structure from motion, geometric reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction
- 作者：Hongyu Zhou, Zorah Lähner
- 出版日期：2026-08-06
- 分类：Geometry Foundation Models（主要），3D Reconstruction & Multi-view Geometry、Neural Scene Representations & Rendering（次要）
- 链接：https://arxiv.org/abs/2608.06117

### 一句话总结
本文研究将多视图几何先验（预测法线和深度图）融入3D高斯泼溅（3DGS）框架以提升重建质量，并发现多视图预测及其置信度图能显著改善效果，尤其在含高光物体的复杂场景中。

### 研究问题
如何利用几何先验改进基于3DGS的重建质量，特别是针对高光物体等几何重建不佳的情况，并分析不同先验来源（单视图 vs. 多视图）及置信度信息的作用。

### 核心思路/方法
- 将预测的法线图和深度图作为几何先验集成到3DGS框架中。
- 对比单视图预测与多视图预测（如近期视觉几何基础变换器VGGT）作为先验来源的效果。
- 利用多视图模型附带生成的置信度图，对每个预测进行加权，以增强先验的有效性。
- 在标准基准上进行实验评估。

### 主要贡献
- 系统分析了几何先验（法线、深度）在GS类方法中的集成效果。
- 发现多视图预测优于单视图预测，且多视图模型生成的置信度图是关键因素，可显著提升先验利用效率。
- 实验表明该方法在标准基准上持续改善重建质量，在高光物体的复杂场景中获得显著增益。

### 局限性
摘要未提供足够信息。摘要未提及方法在极端场景下的失败案例、计算开销、对置信度图质量的依赖程度或与其他优化方法的兼容性等局限性。

### 阅读优先级
**高**。理由：本文针对3DGS的热门问题（几何重建不鲁棒）提出利用多视图几何先验及置信度加权的方案，并给出清晰的对比分析（单视图 vs. 多视图），实验结果有显著提升。该方向与几何基础模型、三维重建及神经渲染高度相关，对研究人员有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian splatting (3DGS) has emerged as a widely-used tool for novel view synthesis, offering real-time rendering in a sparse representation. However, the method's reliance on structure-from-motion initialization and photometric optimization can lead to suboptimal geometric reconstruction, particularly for objects with high specularity. In this work, we investigate the integration of geometric priors, in the form of predicted normal and depth maps, into the 3DGS framework to improve the reconstruction quality. We analyze the effect of incorporating these priors into GS-based methods and our evaluation reveals that multi-view predictions, as they are done by the recent visual geometry grounded transformer (VGGT), outperform single-view alternatives. A major factor is the existence of a confidence map for the estimations, which comes as a by-product of multi-view models and which can significantly improve the effectiveness of priors by weighting each prediction appropriately. Extensive experiments on standard benchmarks show consistent improvement in reconstruction quality and significant gains in complex scenes including specular objects.

</details>

#### 2026-08-05 - Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors

**Authors:** Hakyeong Kim, Ruicheng Wang, Chengtang Yao, Jiaolong Yang, Min H. Kim
**Links:** [abs](https://arxiv.org/abs/2608.04737) - [pdf](https://arxiv.org/pdf/2608.04737)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, robotics, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dense Metric Depth Completion from Sparse Direct Time-of-Flight Sensors
- 作者：Hakyeong Kim, Ruicheng Wang, Chengtang Yao, Jiaolong Yang, Min H. Kim
- 出版日期：2026-08-05
- 分类：Geometry Foundation Models（主要），Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.04737

### 一句话总结
本文提出了一个基于深度引导双分支视觉Transformer的通用框架，用于从稀疏直接飞行时间（dToF）传感器测量中完成稠密公制深度补全，并借助合成数据模拟管线在多种真实设备上实现零样本泛化。

### 研究问题
如何从稀疏、低分辨率、含噪的dToF传感器深度测量中，生成稠密、准确的公制深度图，且适用于不同传感器类型、稀疏程度和噪声条件；同时解决真实配对训练数据稀缺的问题。

### 核心思路/方法
- 采用**深度引导的双分支视觉Transformer编码器**，分别处理RGB图像与稀疏dToF深度测量。
- 引入**掩码联合注意力模块**，使深度token可靠地引导图像特征，但避免被图像特征覆盖。
- 使用**轻量级解码器**高效重建稠密公制深度，不依赖扩散式或精炼式后处理。
- 构建**全面的dToF仿真管线**，再现闪光式、亚VGA闪光式及旋转式传感器的硬件损伤、不规则稀疏性和真实噪声分布。
- 模型完全在合成数据上训练，实现零样本泛化。

### 主要贡献
- 提出一个**可泛化的稀疏dToF稠密深度补全框架**，可跨传感器类型、稀疏程度和噪声条件工作。
- 设计**深度引导双分支Transformer与掩码联合注意力模块**，有效融合模态信息。
- 开发**dToF仿真数据管线**，缓解配对训练数据稀缺问题。
- 在**6个数据集和3个真实dToF设备**上实现强零样本泛化，在精度和计算效率上均优于现有方法。
- 公开代码和模型。

### 局限性
摘要未提供足够信息。摘要仅提及该方法在合成数据上训练并实现零样本泛化，但未明确讨论方法在极端稀疏/噪声条件下的失效边界、对传感器标定误差的敏感性、模型推理速度的具体数值，以及仿真与真实数据之间的残余域差距等问题。

### 阅读优先级
**高**
理由：该工作针对dToF传感器稀疏深度补全这一实际应用难题，提出通用框架并展示跨多数据集和真实设备的零样本泛化能力，同时兼顾精度与效率，对VR/XR、机器人及三维感知领域具有较强参考价值；且摘要明确报告了开源代码与模型，便于复现与进一步研究。

</details>

<details>
<summary>Abstract</summary>

Direct Time-of-Flight (dToF) sensors provide highly accurate metric depth and are more robust than indirect ToF systems in challenging real-world conditions. However, their high manufacturing cost and limited photodiode array size produce depth maps that are extremely sparse, low-resolution, and noisy, making them unsuitable for VR/XR, robotics, and 3D perception tasks that require dense metric depth. Existing monocular and depth completion methods struggle to handle the unique sampling patterns and hardware artifacts of dToF devices, and their performance often deteriorates significantly under severe sparsity or noise. We present a generalizable framework for dense metric depth completion from sparse dToF measurements, capable of operating across diverse sensor types, sparsity levels, and noise conditions. Our model employs a depth-guided dual-branch Vision Transformer encoder that processes RGB images and sparse dToF measurements separately, while a masked joint attention module allows depth tokens to reliably guide image features without being overwritten by them. A lightweight decoder reconstructs dense metric depth efficiently, without diffusion-based or refinement-heavy post-processing. To address the scarcity of paired training data, we introduce a comprehensive dToF simulation pipeline that reproduces the characteristics of flash, sub-VGA flash, and rotating sensors, including hardware-induced degradation, irregular sparsity, and realistic noise distributions. Trained entirely on synthetic data, our model achieves strong zero-shot generalization across 6 datasets and 3 real dToF devices, outperforming state-of-the-art approaches in both accuracy and computational efficiency. This establishes a robust and practical solution for dense metric depth completion from sparse direct ToF sensors. Our code and models are open-sourced. See https://vclab.kaist.ac.kr/cvpr2026p3.

</details>

#### 2026-08-05 - Mind-VLA: Instruction-Aware Spatial Representation Alignment for Vision-Language-Action Models

**Authors:** Xingyu Ding, Yuzhong Zhao, Yang Wu, Chaoyang Zhao, Chunhai Zhao, Yifan Zhang, Jian Cheng
**Links:** [abs](https://arxiv.org/abs/2608.04633) - [pdf](https://arxiv.org/pdf/2608.04633)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mind-VLA: Instruction-Aware Spatial Representation Alignment for Vision-Language-Action Models
- 作者：Xingyu Ding, Yuzhong Zhao, Yang Wu, Chaoyang Zhao, Chunhai Zhao, Yifan Zhang, Jian Cheng
- 出版日期：2026-08-05
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2608.04633

### 一句话总结
Mind-VLA 提出一种指令感知的空间表征对齐方法，通过将 VLA 模型的潜在表征与语言指令指定的目标对象的 3D 特征对齐，提升精细操作和遮挡场景下的表现。

### 研究问题
现有 VLA 方法虽然通过与 3D 场景几何对齐提升了泛化性，但对齐过程与语言指令无关——整个场景被统一对齐，忽略指令指定目标对象的 3D 几何信息，导致在精细操作和目标遮挡任务中失败。本文针对“如何让 VLA 模型获得指令感知的 3D 理解”这一核心问题展开。

### 核心思路/方法
1. **目标识别**：首先从语言指令中定位指定的目标对象。
2. **多视角特征提取**：为目标对象生成三视图（tri-view），并提取对应的 VAE 和 VGGT 特征。
3. **表征对齐**：将 VLA 模型的潜在表征与上述提取的指令相关特征进行对齐，从而实现指令感知的 3D 理解。

### 主要贡献
- 提出指令感知的空间表征对齐方法，弥补现有 VLA 方法在“整个场景统一对齐”上的指令盲区。
- 在 LIBERO 上达到 93.9%，CALVIN 上达到 4.47，且仅使用 345M 参数的紧凑骨干网络。
- 在真实机器人目标遮挡任务中平均成功率 54%，比最优的指令无关方法高出 32 个百分点。
- 代码将公开。

### 局限性
摘要未提供足够信息，如方法的计算开销、对复杂指令的鲁棒性、失败案例分析、以及在不同真实场景下的泛化边界等均未提及。

### 阅读优先级
**高**。理由：该方法针对 VLA 中的关键缺陷（指令无关的对齐）提出直接改进，在仿真和真实机器人遮挡任务上均有显著提升，且模型体积紧凑，具有实际部署潜力。摘要数据充分，适合机器人操作与多模态大模型交叉方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent Vision-Language-Action (VLA) methods improve generalization by aligning their representations with 3D scene geometry. However, these methods are fundamentally instruction-agnostic: the representations align the entire scene uniformly, neglecting the 3D geometry of the specific target object designated by the language instruction. This causes failures on fine-grained manipulation and target occlusion tasks, where success depends on accurate 3D understanding of the target object rather than the entire scene. To address this, we present Mind-VLA, an instruction-aware spatial representation alignment method for VLA models. Specifically, Mind-VLA first obtains the target object specified by the language instruction, then prepares its target-object tri-view and extracts the corresponding VAE and VGGT features. Finally, the latent representation of the VLA model is aligned with these features to enable instruction-aware 3D understanding. Mind-VLA reaches 93.9% on LIBERO and 4.47 on CALVIN with a compact 345M-parameter backbone. On real-robot tasks with target occlusion, Mind-VLA reaches 54% average success, outperforming the best-performing instruction-agnostic method in real-robot comparison by 32 percentage points. Code will be publicly available.

</details>

#### 2026-08-04 - LiteMVS: Efficient Multi-View Stereo with Foundation Distillation and Expert Aggregation

**Authors:** Tianbao Zhang, Zeyu Liu, Shuyu Wu, Fanxing Li, Zhaoxin Fan, Wenjun Wu, Danping Zou
**Links:** [abs](https://arxiv.org/abs/2608.03851) - [pdf](https://arxiv.org/pdf/2608.03851)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** depth prediction, geometric reasoning, 3D reconstruction, multi-view stereo, MVS, depth estimation, monocular depth, robotics, manipulation, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LiteMVS: Efficient Multi-View Stereo with Foundation Distillation and Expert Aggregation
- 作者：Tianbao Zhang, Zeyu Liu, Shuyu Wu, Fanxing Li, Zhaoxin Fan, Wenjun Wu, Danping Zou
- 出版日期：2026-08-04
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry、Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.03851

### 一句话总结
LiteMVS 提出一种轻量级多视图立体深度估计模型，通过将单目语义/结构先验蒸馏注入多视图立体框架，并采用专家混合（MoE）聚合，实现了高质量且高效的深度预测与三维重建。

### 研究问题
现有 MVS 方法依赖几何对应，在无纹理或重复区域容易失效；而单目深度模型虽有图像级先验，但缺乏多视图几何约束。如何在保持效率的前提下，将单目强先验高效融入 MVS 框架，以获得结构感知更强且利于时空扩展的深度估计？

### 核心思路/方法
- 将轻量级分割模型和大型视觉基础模型提取的高层单目知识注入 MVS 框架，具体做法包括：
  - 用语义描述符丰富代价体（cost volume）；
  - 采用 Mixture-of-Experts（MoE）公式，在深度假设间实现自适应几何聚合；
  - 通过蒸馏视觉基础模型的几何先验加强单目引导，且不增加推理成本。
- 整体设计兼顾静态场景深度/重建质量的提升，同时为后续时间建模与 4D 表示学习提供更可靠的几何基础。

### 主要贡献
1. 提出 LiteMVS 轻量级 MVS 模型，集成平面扫描几何推理与单目语义/结构先验。
2. 将语义描述符注入代价体、采用 MoE 进行自适应深度聚合，有效提升深度估计与三维重建质量。
3. 通过基础模型蒸馏注入几何先验而不增加推理开销。
4. 在 ScanNetv2 和 7-Scenes 上验证了高质量深度预测与重建效果，同时保持有竞争力的效率。

### 局限性
摘要未提供足够信息（如具体失败场景、对噪声/遮挡的鲁棒性、不同硬件条件下的效率数据等均未提及）。

### 阅读优先级
**高**。理由：该工作面向机器人、AR 与具身智能等热门应用场景，直接针对 MVS 在无纹理/重复区域的痛点，并提出将基础模型先验与多视图几何高效结合的轻量级方案，方法设计新颖且兼顾效率与质量，实验在公开基准上验证有效，对相关领域研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-time 3D perception is crucial for robotics, augmented reality, and embodied intelligence applications. Existing multi-view stereo (MVS) methods primarily rely on geometric correspondences, which often fail in textureless or repetitive regions, while monocular depth models leverage strong image-level priors but lack robust multi-view geometric constraints. More importantly, in robotics and embodied manipulation scenarios, high-quality 3D geometry is not only essential for static reconstruction, but also serves as a critical foundation for learning temporally consistent 4D representations. To obtain visual representations with stronger structural awareness and greater potential for spatiotemporal extension, we present LiteMVS, a lightweight multi-view depth estimation model that integrates plane-sweep geometric reasoning with strong monocular semantic and structural priors. The central idea of LiteMVS is to efficiently inject high-level monocular knowledge, obtained from lightweight segmentation models and large-scale vision foundation models, into a multi-view stereo framework. In particular, LiteMVS enriches the cost volume with semantic descriptors and employs a Mixture-of-Experts (MoE) formulation to enable adaptive geometric aggregation across depth hypotheses. Moreover, geometric priors distilled from vision foundation models further strengthen monocular guidance without increasing inference cost. Through this design, LiteMVS not only improves depth estimation and 3D reconstruction quality in static scenes, but also provides a more reliable geometric foundation for subsequent temporal modeling and 4D representation learning. Experiments on ScanNetv2 and 7-Scenes demonstrate that LiteMVS achieves high-quality depth prediction and 3D reconstruction while maintaining competitive efficiency.

</details>

## Dynamic / 4D Reconstruction

### 2026-08

#### 2026-08-06 - Engram-E2VID: Reference-Based Event-to-Video Reconstruction via Generative Activation of Appearance Engrams

**Authors:** Feiyu Ji, Xiang Li, Hao Ma, Tianxiang Huang, Qingxin Lu, Mengqi Ji, Lei Han, Xiaokang Yang, Xiaoyun Yuan
**Links:** [abs](https://arxiv.org/abs/2608.05728) - [pdf](https://arxiv.org/pdf/2608.05728)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Engram-E2VID: Reference-Based Event-to-Video Reconstruction via Generative Activation of Appearance Engrams
- 作者：Feiyu Ji, Xiang Li, Hao Ma, Tianxiang Huang, Qingxin Lu, Mengqi Ji, Lei Han, Xiaokang Yang, Xiaoyun Yuan
- 出版日期：2026-08-06
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2608.05728

### 一句话总结
Engram-E2VID 提出一种基于参考帧和事件流的视频重建框架，通过在扩散模型中生成式激活“外观印记”将事件派生的结构信息与参考帧外观关联，从而提升重建质量。

### 研究问题
如何从参考帧和参考到目标时间段内的事件流中恢复目标 RGB 帧。核心挑战在于事件只提供稀疏、异步的对数亮度变化而非绝对外观，尤其在复杂运动和长时间间隔下，如何将事件派生的目标时刻结构与参考帧中的相关外观信息正确关联。

### 核心思路/方法
- 将参考帧编码为 token 空间中的“外观印记”（appearance engrams）。
- 将事件流与参考上下文转换为目标时刻的“运动-结构支架”（motion-structure scaffold），捕获运动边界和事件引发的结构变化。
- 在单步扩散骨干中，支架派生的结构 token 跨层逐步交互并激活相关的外观印记。
- 这种 token 空间关联避免依赖直接的像素级对应，同时扩散先验用于补充不确定或新显露的区域。

### 主要贡献
- 提出结构引导的参考式事件到视频重建框架。
- 在三个基准上，对比最强的同输入基线，PSNR 最高提升 3.29 dB，LPIPS 最多降低 0.08。
- 随着重建间隔增加，性能下降更缓慢，显示对长间隔的鲁棒性。

### 局限性
摘要未提供足够信息。摘要未说明方法在极端复杂场景（如剧烈遮挡、光照突变）下的表现，也未提供计算开销或实时性分析，也未提及失败案例或对训练数据依赖性的讨论。

### 阅读优先级
**高**  
理由：该方法在事件驱动视频重建任务上取得了显著的量化提升（PSNR +3.29 dB），并明确针对复杂运动和长间隔这一核心难点提出创新性的 token 空间关联方案，适合对该方向的研究者作为重要参考。

</details>

<details>
<summary>Abstract</summary>

Reference-based event-to-video reconstruction aims to recover target RGB frames from a reference frame and the event stream captured over the reference-to-target interval. Although events provide fine-grained temporal cues, they encode sparse and asynchronous log-intensity changes rather than absolute appearance, making faithful reconstruction intrinsically challenging. The central challenge lies in associating event-derived target-time structures with relevant appearance information from the reference frame, especially under complex motion and long temporal intervals. In this work, we propose Engram-E2VID, a structure-guided framework that reconstructs target frames through the generative activation of appearance engrams. Specifically, the reference frame is encoded into token-space appearance engrams, while the event stream and reference context are transformed into a target-time motion-structure scaffold that captures motion boundaries and event-induced structural changes. Within a one-step diffusion backbone, scaffold-derived structural tokens progressively interact with and activate relevant appearance engrams across layers. This token-space association allows target structures to access reference appearance without relying on direct pixel-wise correspondence, while the diffusion prior complements uncertain or newly revealed regions. Across three benchmarks, Engram-E2VID improves PSNR by up to 3.29 dB and reduces LPIPS by up to 0.08 over the strongest same-input baseline, while degrading more slowly as the reconstruction interval increases.

</details>

#### 2026-08-03 - ASTRA: Asynchronous Spatio-Temporal Reconstruction via Trajectory Alignment

**Authors:** Junyu Zhu, Hao Zhu, Xinzhuo Zhang, Hongdong Li, Zhan Ma, Xun Cao
**Links:** [abs](https://arxiv.org/abs/2608.02006) - [pdf](https://arxiv.org/pdf/2608.02006)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, dynamic 3D, spatio-temporal reconstruction, temporal reconstruction, motion trajectories, dynamic Gaussian, scene reconstruction, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ASTRA: Asynchronous Spatio-Temporal Reconstruction via Trajectory Alignment
- 作者：Junyu Zhu, Hao Zhu, Xinzhuo Zhang, Hongdong Li, Zhan Ma, Xun Cao
- 出版日期：2026-08-03T10:06:45Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02006

### 一句话总结
ASTRA 提出利用 2D 运动轨迹作为显式、与纹理无关的监督信号，通过轨迹对齐联合优化时间偏移与动态 3D 表示，以解决多相机异步动态场景重建中的运动模糊与几何伪影问题。

### 研究问题
在真实场景中，多相机采集设备之间存在时间异步，导致动态 3D 场景重建出现严重运动模糊与几何伪影。现有异步重建方法依赖光度监督估计时间偏移，但在大偏移和复杂运动下，外观匹配提供的时间线索很弱，其瓶颈包括：低纹理区域的“纹理诱导坍缩”（对齐信号近乎消失）以及“变形诱导耦合”（时间误差被吸收进扭曲的几何或运动而非被显式纠正）。

### 核心思路/方法
ASTRA 以 2D 运动轨迹作为显式的、纹理无关的监督信号，替代仅依赖渲染颜色残差进行相机同步的做法。具体地，它将重建 3D 点投影后的运动与观测到的 2D 轨迹进行对齐，联合优化时间偏移和动态 3D 表示；同时使用动态与确定性掩码（dynamic and certainty masking）抑制不可靠的轨迹约束。

### 主要贡献
- 提出 ASTRA 框架，将 2D 运动轨迹引入异步动态重建作为显式监督，缓解纹理缺失和大偏移下的同步困难。
- 在多个动态 Gaussian Splatting 骨干网络上验证了方法的通用性。
- 实验表明：在高达 25 帧偏移的严重异步下，ASTRA 保持高频空间细节和强鲁棒性，PSNR 提升约 1.4 dB，时间偏移 MAE 降低 54.0%，同步成功率提升近 4 倍。

### 局限性
摘要未提供足够信息（未提及方法在极端遮挡、轨迹长度不足、计算开销或失败案例等方面的局限）。

### 阅读优先级
**高**  
理由：该工作针对动态重建中实际且棘手的时间异步问题，提出了新的监督范式（轨迹对齐），在多个骨干上取得显著提升（PSNR、MAE、成功率均有量化改善），对 4D 重建、神经表示与渲染方向的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D scene reconstruction has achieved remarkable success under the assumption of strictly synchronized multi-camera inputs. However, in real-world scenarios, temporal asynchrony among capturing devices remains a critical challenge, leading to severe motion blur and geometric artifacts. Existing asynchronous reconstruction methods typically estimate temporal offsets through photometric supervision, but appearance matching provides weak temporal cues under large offsets and complex motions. We attribute this limitation to two major bottlenecks: texture-induced collapse, where low-texture regions provide nearly vanishing alignment signals, and deformation-induced coupling, where temporal errors are absorbed into distorted geometry or motion rather than being explicitly corrected. To address these issues, we propose ASTRA (Asynchronous Spatio-Temporal Reconstruction via Trajectory Alignment), a framework that introduces 2D motion trajectories as explicit, texture-agnostic supervision for asynchronous dynamic reconstruction. Instead of synchronizing cameras solely through rendered color residuals, ASTRA jointly optimizes temporal offsets and dynamic 3D representations by aligning the projected motion of reconstructed 3D points with observed 2D trajectories, while using dynamic and certainty masking to suppress unreliable trajectory constraints. Extensive experiments on different dynamic Gaussian Splatting backbones show that ASTRA preserves high-frequency spatial details and sustains strong robustness even under severe asynchrony with up to 25-frame offsets, achieving approximately 1.4 dB PSNR improvement, reducing temporal-offset MAE by 54.0\%, and nearly quadrupling the synchronization success rate.

</details>

#### 2026-08-03 - FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis

**Authors:** Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma
**Links:** [abs](https://arxiv.org/abs/2608.01958) - [pdf](https://arxiv.org/pdf/2608.01958)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, 4D Gaussian, 3D reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis
- 作者：Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma
- 出版日期：2026-08-03
- 分类：Dynamic / 4D Reconstruction（主）；Neural Scene Representations & Rendering（次）
- 链接：https://arxiv.org/abs/2608.01958

### 一句话总结
本文提出一种基于傅里叶运动建模的频率感知时空高斯泼溅方法（FAST-GS），通过将运动分解为频域正弦分量，同时捕捉低频全局轨迹与高频局部细节，以提升动态场景重建的复杂运动拟合精度与长期时间一致性。

### 研究问题
现有4D高斯泼溅（4DGS）方法使用单一多项式建模运动，在含高频运动分量的复杂动态场景中性能受限，且因累积轨迹漂移难以保证长期稳定性。

### 核心思路/方法
- 提出**傅里叶运动建模模块**：将运动分解为基于频率的正弦分量，分别捕捉低频全局轨迹和高频局部细节，以准确建模复杂运动模式，同时保持4DGS的实时渲染能力。
- 在损失函数中集成**运动感知正则化策略**：使用与频率相关的权重抑制高频抖动，同时保持低频运动的连贯性。

### 主要贡献
- 提出傅里叶运动建模范式，改进复杂运动拟合能力与长期时序一致性。
- 引入频率相关的运动感知正则化，在抑制高频噪声的同时维持低频运动连贯性。
- 在N3V和Google Immersive数据集的多场景实验中验证了方法有效性。

### 局限性
摘要未提供足够信息（如具体数值结果、与基线方法的定量对比细节、失败案例或计算开销等均未说明）。

### 阅读优先级
**高**。理由：该工作直接针对4DGS在复杂动态场景中的核心瓶颈（运动建模能力不足与轨迹漂移）提出新颖的频域分解方案，属于动态新视角合成方向的重要方法论改进；且实验覆盖多个公开数据集，若该方向与读者兴趣相关，值得精读。

</details>

<details>
<summary>Abstract</summary>

4D Gaussian Splatting (4DGS) excels in dynamic 3D reconstruction and real-time novel view synthesis via efficient 4D Gaussian representations and parallelizable rendering. However, existing 4DGS approaches rely on a single polynomial to model motion, which limits performance in complex dynamic scenes where high-frequency motion components are prevalent, and fails to ensure long-term stability due to cumulative trajectory drift. To address these issues, we propose a Fourier Motion Modeling module: this paradigm decomposes motion into frequency-based sinusoidal components, capturing both low-frequency global trajectories and high-frequency local details to model complex motion patterns accurately. It retains the real-time rendering capability of 4DGS while improving complex motion fitting and long-term coherence. Additionally, we integrate a motion-aware regularization strategy into the loss function: it uses frequency-dependent weights to suppress high-frequency jitter while preserving low-frequency motion coherence. Extensive experiments on N3V and Google Immersive datasets from multiple scenarios demonstrate the effectiveness of our method.

</details>

#### 2026-08-03 - D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting

**Authors:** Jijian Zhao
**Links:** [abs](https://arxiv.org/abs/2608.01588) - [pdf](https://arxiv.org/pdf/2608.01588)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, 4D Gaussian, monocular depth, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting
- 作者：Jijian Zhao
- 出版日期：2026-08-03
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01588

### 一句话总结
本文提出一种基于双源深度先验引导的稀疏相机动态4D高斯泼溅方法，通过融合单目深度与多视角几何深度，在减少输入视角的同时提升动态场景重建的质量与一致性。

### 研究问题
如何在稀疏相机输入下，缓解动态4D高斯泼溅因几何监督不足而导致的结构缺失和漂浮高斯伪影问题。

### 核心思路/方法
- 利用双源深度先验（单目深度与多视角几何深度）的互补性：单目深度提供稠密但尺度模糊、局部有偏的结构；多视角几何深度提供与重建坐标系一致但不完整的锚点。
- 将单目深度估计与有效的多视角几何深度对齐，并通过一致性验证筛选出可靠的几何锚点。
- 可靠锚点用于一致性感知剪枝和深度监督；经验证的几何深度和对齐后的单目深度共同为欠重建区域提供候选几何，以支持稠密化。
- 采用RGB-D联合优化，在稀疏视角监督下提升外观保真度与几何一致性。

### 主要贡献
- 提出D^2-4DGS框架，首次在稀疏相机动态4D高斯泼溅中系统性地融合双源深度先验。
- 设计基于一致性验证的几何锚点筛选机制，有效支持剪枝、深度监督和稠密化。
- 通过RGB-D联合优化，在稀疏视角下同时改善外观质量与几何一致性。
- 在全部9个数据集-视角设置中取得最高PSNR，平均较各设置最佳对比方法提升1.33 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法针对稀疏相机动态重建这一具体问题，提出了双源深度融合的可行方案，并在量化指标上有明显提升，对从事动态场景重建或高斯泼溅相关研究的读者有参考价值；但摘要未给出方法复杂度、运行效率或失败案例分析，尚不足以判断其在实际应用中的普适性。

</details>

<details>
<summary>Abstract</summary>

Dynamic 4D Gaussian Splatting has emerged as an efficient representation for dynamic novel view synthesis through explicit scene modeling and real-time rendering. However, existing methods typically require dense multi-view videos for sufficient geometric constraints, making capture expensive and limiting sparse-camera deployment. Reducing input views lowers acquisition cost but weakens geometry supervision, often causing missing structures and floating Gaussians. Depth priors provide geometric cues, yet no single source offers both dense coverage and reliable geometry. Monocular depth provides dense structure but is scale-ambiguous and locally biased, whereas multi-view geometric depth provides incomplete anchors consistent with the reconstruction coordinate system. To exploit their complementarity, we propose D$^2$-4DGS, a sparse-camera dynamic 4D Gaussian Splatting framework guided by dual-source depth priors. We align monocular estimates with valid multi-view geometric depths and verify their consistency to identify reliable geometric anchors. These verified anchors support consistency-aware pruning and depth supervision, while verified geometric depths and aligned mono-only estimates provide candidate geometry for densification in under-reconstructed regions. Finally, RGB-D joint optimization improves appearance fidelity and geometric consistency under sparse-view supervision. Across all nine dataset--view settings, D$^2$-4DGS achieves the highest PSNR, improving by 1.33 dB on average over the best competing method in each setting.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-08

#### 2026-08-06 - OmniMech: All-in-one Multimodal Mechanical Benchmark for 3D Reconstruction

**Authors:** Taiting Lu, Runze Liu, Ziwei Dong, Sisong Bei, Jingying Zeng, Mingjia Wang, Zhenghao Li, Kaiyuan Lin, Yi-Shan Wu, Yangshoudu Zheng, Hongxing Pan, Kai Zhang, Guoliang Shi, Ling Ma, Yifan Yang, Jiaying Lu, Qi He, Sung-Liang Chen, Yi-Chao Chen, Yincheng Jin, Mahanth Gowda
**Links:** [abs](https://arxiv.org/abs/2608.05539) - [pdf](https://arxiv.org/pdf/2608.05539)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniMech: All-in-one Multimodal Mechanical Benchmark for 3D Reconstruction
- 作者：Taiting Lu, Runze Liu, Ziwei Dong, Sisong Bei, Jingying Zeng, Mingjia Wang, Zhenghao Li, Kaiyuan Lin, Yi-Shan Wu, Yangshoudu Zheng, Hongxing Pan, Kai Zhang, Guoliang Shi, Ling Ma, Yifan Yang, Jiaying Lu, Qi He, Sung-Liang Chen, Yi-Chao Chen, Yincheng Jin, Mahanth Gowda
- 出版日期：2026-08-06
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.05539

### 一句话总结
OmniMech 是一个百万级规模的工业机械设计多模态基准，用于评估视觉语言模型从工程图纸生成可执行 CAD 程序及细粒度 3D 重建的能力。

### 研究问题
现有视觉语言模型（VLMs）虽然能从图像生成可执行的 CAD 程序，但主要针对粗粒度、通用性的 3D 物体，难以满足工业机械设计中细粒度几何和毫米级公差的要求。本文旨在构建一个工业制造数据上的基准，系统评估 VLMs 在可执行 CAD 生成方面的能力。

### 核心思路/方法
作者构建了 OmniMech 基准，包含超过 251,000 张带完整尺寸和公差的 2D 正交工程图，并配套原生 CAD 模型、多视图渲染、网格、STEP、B-rep 表示以及丰富的语义标注。基准设计了四个任务：1）从工程图合成参数化 CAD 程序；2）图到 3D 推理（保证几何和结构一致性）；3）基于标注的尺寸、符号、特征标注和制造约束推理；4）使用可视化、测量、CAD 执行和验证工具的工具增强智能体推理。

### 主要贡献
- 提出了 OmniMech，首个百万级规模的工业制造数据基准，用于评估 VLMs 在可执行 CAD 生成上的表现。
- 基准包含多种数据表示（2D 图纸、CAD 模型、多视图渲染、网格、STEP、B-rep）和丰富的语义标注。
- 设计了覆盖从程序合成到智能体推理的四项基准任务。
- 实验表明当前 VLMs 和 CAD 专用模型在可执行程序合成、细粒度 3D 重建以及尺寸/公差可靠执行方面仍存在明显不足。
- 将发布基准数据、评估代码和工具接口以支持未来研究。

### 局限性
摘要未提供足够信息，未明确讨论该基准的局限性（如数据覆盖范围、任务难度设置、评估指标可能存在的偏差等）。

### 阅读优先级
**高**。理由：该工作提出了首个百万级规模的工业机械 CAD 生成基准，填补了现有 VLM 评估在细粒度工业场景中的空白，且数据规模和任务设计（四个任务，涵盖程序合成到智能体推理）对 3D 重建、CAD 生成和 VLM 评估方向的研究者具有较高的参考价值。实验结果揭示了现有模型的明显短板，有利于推动后续方法改进。

</details>

<details>
<summary>Abstract</summary>

Recent vision-language models (VLMs) can generate executable CAD programs from images, but existing methods mainly target coarse, general-purpose 3D objects and rarely address the fine-grained geometry and millimeter-level tolerances required in industrial mechanical design. We introduce OmniMech, the first million-scale benchmark for evaluating VLMs on executable CAD generation from industrial manufacturing data. OmniMech contains more than 251,000 fully dimensioned and toleranced 2D orthographic drawings, paired with native CAD models, multi-view renderings, mesh, STEP and B-rep representations, and rich semantic annotations. The benchmark includes four tasks: (1) parametric CAD program synthesis from engineering drawings; (2) diagram-to-3D reasoning for geometrically and structurally consistent reconstruction; (3) annotation-grounded reasoning over dimensions, symbols, feature callouts, and manufacturing constraints; and (4) tool-augmented agentic reasoning using visualization, measurement, CAD execution, and verification tools. Experiments show that current VLMs and CAD-specialized models still struggle with executable program synthesis, fine-grained 3D reconstruction, and reliable enforcement of dimensions and tolerances. We will release the benchmark data, evaluation code, and tool interfaces to support future research.

</details>

#### 2026-08-05 - AI-based single-shot structured-light depth reconstruction for real-time laparoscopic surgical guidance

**Authors:** Wayne Wonseok Rodgers, Xiangyi Le, Seonghoon Jang, Shuwen Wei, Justin Opfermann, Michael Kam, Axel Krieger, Jin U. Kang
**Links:** [abs](https://arxiv.org/abs/2608.05109) - [pdf](https://arxiv.org/pdf/2608.05109)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AI-based single-shot structured-light depth reconstruction for real-time laparoscopic surgical guidance
- 作者：Wayne Wonseok Rodgers, Xiangyi Le, Seonghoon Jang, Shuwen Wei, Justin Opfermann, Michael Kam, Axel Krieger, Jin U. Kang
- 出版日期：2026-08-05
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.05109

### 一句话总结
本文提出一种基于LED照明二进制掩膜和VQ-VAE潜在空间深度重建的免同步单次拍摄深度感知平台，用于实时腹腔镜手术引导，在体模数据上实现了26.0 Hz的推理速度和3.70 mm的平均绝对误差。

### 研究问题
如何在不依赖投影仪-相机同步、多次采集和DMD投影等复杂机制的条件下，实现紧凑腹腔镜系统中准确且实时的术中深度估计，以支持自主/半自主机器人腹腔镜手术。

### 核心思路/方法
- 硬件层面：采用无源LED照明的二进制掩膜投影模块，耦合到双通道腹腔镜的一个通道；另一通道拍摄条纹照射目标，因此无需同步和数字微镜器件。
- 深度参考：使用Zivid 3D相机对722对体模图像获取参考深度，并将Zivid深度图重投影到SSLE图像坐标系用于监督训练和评估。
- 网络架构：VQ-VAE将输入编码为离散潜在表征，在潜在空间中用自定义U-Net预测深度，无需单独的分割或掩膜预测分支。
- 对比基线：与双U-Net的MaskNet+DepthNet基线以及现成的单目深度模型进行比较。

### 主要贡献
- 提出一种免同步、单次拍摄的深度感知平台，结合LED二进制掩膜投影和潜在空间深度重建，实现视频级端到端深度估计。
- 在体模数据集上，模型MAE为3.70 mm，AbsRel为0.0326，delta=1.1精度为0.962，delta=1.1²精度为0.970，优于基线方法。
- 在NVIDIA A100 GPU上达到26.0 Hz的推理速度，满足实时手术引导需求。
- 结果表明，无需显式分割阶段即可实现Zivid参考的体模重建，同时强调了数据集规模和SSLE-Zivid标定精度的重要性。

### 局限性
摘要未提供足够信息。摘要未提及泛化到真实手术场景、不同体模类型或活体组织的表现；未报告对投影掩膜遮挡、运动伪影或照明变化的鲁棒性分析；未讨论数据规模对性能的具体影响阈值，也未提供标定误差的量化评估。训练/验证/测试划分的细节（如体模多样性）也无从得知。

### 阅读优先级
**高**。理由：该工作在实时腹腔镜深度感知这一具有明确临床需求的方向上提出了新颖的免同步单次拍摄方案，结合VQ-VAE潜在空间重建在速度和精度上均展示了有竞争力的结果（26 Hz、MAE 3.70 mm），且与机器人手术辅助直接相关。对于从事手术视觉、深度估计或结构光三维重建的研究者，该论文具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Significance. Accurate intraoperative depth perception is important for autonomous and semi-autonomous robotic laparoscopic surgery. Conventional fringe projection profilometry can achieve millimeter-scale accuracy but often requires multi-shot acquisition, digital-micromirror-device projection, and projector-camera synchronization, complicating integration into compact laparoscopic systems. Aim. To develop a synchronization-free, single-shot depth-sensing platform using a passive LED-illuminated binary mask and a VQ-VAE prior with a custom U-Net depth head. Approach. A compact projection module was coupled to one channel of a dual-channel laparoscope, while the second channel imaged the fringe-illuminated target. A Zivid 3D camera acquired reference depth for 722 paired phantom images. Zivid depth maps were reprojected into the SSLE image frame for supervised training and evaluation. The VQ-VAE encoded each input into a discrete latent representation, and a latent-space U-Net predicted depth without a separate mask-prediction branch. Results. Using a fixed train/validation/test split, the proposed model achieved an MAE of 3.70 mm, AbsRel of 0.0326, delta=1.1 accuracy of 0.962, and delta=1.1^2 accuracy of 0.970. It achieved lower MAE than the dual U-Net MaskNet + DepthNet baseline and outperformed off-the-shelf monocular depth models in MAE, AbsRel, and threshold accuracy. The pipeline operated at 26.0 Hz over 301 consecutive frames on an NVIDIA A100 GPU. Conclusions. The LED-illuminated binary-pattern platform with latent-space depth reconstruction enables synchronization-free, video-rate endoscopic depth estimation. Results demonstrate Zivid-referenced phantom reconstruction without an explicit segmentation stage, while emphasizing the importance of dataset size and SSLE-Zivid calibration accuracy.

</details>

#### 2026-08-05 - Beyond Reprojection Error: Camera Calibration with 3D Targets

**Authors:** Dennis Ruppel, Hasan Kutlu, Kai A. Neumann, Martin Knuth, Pedro Santos, Andreas Weinmann, Arjan Kuijper
**Links:** [abs](https://arxiv.org/abs/2608.05066) - [pdf](https://arxiv.org/pdf/2608.05066)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Reprojection Error: Camera Calibration with 3D Targets
- 作者：Dennis Ruppel, Hasan Kutlu, Kai A. Neumann, Martin Knuth, Pedro Santos, Andreas Weinmann, Arjan Kuijper
- 出版日期：2026-08-05
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.05066

### 一句话总结
该论文提出一种基于预测场景射线的相机标定框架，引入新的评估指标与二十面体标定靶，旨在提升三维重建中的标定精度并指出重投影误差作为评估指标的局限性。

### 研究问题
传统的相机标定依赖二维平面靶标和重投影误差，该方法在三维重建场景中可能不够准确或具有误导性。该论文研究如何设计更适用于三维重建的标定框架，包括标定对象、检测器以及评估指标。

### 核心思路/方法
- 提出基于预测场景射线（scene rays）的标定框架，替代传统的二维平面标定方法。
- 引入两种新指标：重建误差（reconstruction error）和相交误差（intersection error），二者均从预测的场景射线推导而来。
- 结合自举（bootstrapping）程序，对不同的标定对象和标定流程（涵盖内参和外参）进行统计评估。
- 设计了一个二十面体（icosahedron）标定靶，并配套基于环形特征（ring-feature）的检测器，用于丰富三维重建的标定信息。

### 主要贡献
- 提出一个面向三维重建的相机标定框架，基于场景射线预测，提升了标定的灵活性和与现代相机模型的兼容性。
- 证明广义畸变模型能更真实地反映物理相机效应，从而提升标定精度。
- 指出重投影误差可能误导三维精度的评估，提出的基于射线的指标能提供更全面的评估。
- 设计并评估了二十面体标定靶，在合成数据上相比基线实现了约40%更低的平均相交误差，且自举试验中标定稳定性更高。

### 局限性
- 摘要提到真实数据（real-data）性能对制造公差要求非常严格，暗示实际使用中可能受限于物理制造精度。
- 其他局限性（如方法适用范围、计算成本、对噪声的鲁棒性等）摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该工作针对相机标定中的评估指标和标定靶设计提出了新见解，对三维重建相关研究有一定参考价值。但由于其框架和指标的新颖性尚需更多验证，且真实数据性能受限，不构成该领域的核心突破性工作，建议按需阅读，无需优先精读。

</details>

<details>
<summary>Abstract</summary>

In 3D reconstruction, camera calibration is an essential element for achieving high fidelity and accuracy of the reconstructed geometry. While existing approaches rely upon 2D planar calibration, this work proposes a framework tailored for 3D reconstruction that is based on predicting scene rays, which adds flexibility to the reconstruction pipeline and enables the use of recent advances in camera models. Novel metrics, reconstruction and intersection error, derived from predicted scene rays are employed in combination with a bootstrapping procedure that statistically evaluates different calibration objects and calibration pipelines for both intrinsic and extrinsic camera parameters. The results show that the generalized distortion model more faithfully captures physical camera effects and yields an improvement in calibration accuracy. Reprojection error is shown to be a potentially misleading indicator of 3D accuracy, and the proposed ray-based metrics provide a more holistic assessment. An icosahedron calibration target is designed to enrich calibration information for 3D reconstruction together with a ring-feature-based detector. The icosahedral target yields approximately 40% lower mean intersection and more stable calibration across bootstrap trials on synthetic data, while real-data performance demands very tight fabrication tolerances.

</details>

#### 2026-08-05 - Promptable Animal Pose Tracking Across Species

**Authors:** Le Li, Daniela Ivanova, Nicolas Pugeault
**Links:** [abs](https://arxiv.org/abs/2608.04995) - [pdf](https://arxiv.org/pdf/2608.04995)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Promptable Animal Pose Tracking Across Species（跨物种的可提示动物姿态追踪）
- 作者：Le Li, Daniela Ivanova, Nicolas Pugeault
- 出版日期：2026-08-05
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.04995

### 一句话总结
本文提出利用视觉基础模型，以无监督和监督两种模式实现跨物种动物姿态追踪，在有限标注数据下兼顾精度与泛化能力。

### 研究问题
如何在标注数据稀少、物种形态差异大的条件下，实现准确且跨物种泛化的动物姿态估计与追踪。

### 核心思路/方法
- 利用在大规模数据上训练的视觉基础模型，减少对动物标注数据的依赖。
- 提出两个模型：
  - **监督模型**：通过关键点提示编码器（keypoint prompt encoder），从参考帧显式注入结构先验到特征匹配中，提升追踪精度。
  - **无监督模型**：利用基础模型的多样化特征进行免训练对应匹配，增强跨物种鲁棒性。
- 在 APTv2 和 TigDog 基准上评估，追求精度与泛化之间的平衡。

### 主要贡献
- 证明视觉基础模型可有效用于有限标注下的动物姿态追踪。
- 提出监督与无监督两种互补方案，分别侧重精确度和跨物种鲁棒性。
- 在多个挑战性基准上取得强性能，为真实动物行为分析与保护研究提供实用方案。

### 局限性
- 摘要未提供消融实验、失败案例、计算成本或具体性能数值等细节。
- 摘要未说明两种模型在何种条件下分别表现更优，也未讨论标注数据的最小需求量。
- 摘要未提供对不同物种类别（如哺乳类、鸟类等）的细分表现分析。

### 阅读优先级
**中**  
理由：研究主题（跨物种动物姿态追踪）具有一定应用价值，且方法结合了无监督与监督两种路径，思路有启发性；但摘要未给出具体性能指标或深入实验细节，对于需要快速判断方法有效性的读者来说，信息密度有限。若从事动物行为分析或姿态追踪相关研究，值得一读；否则优先级可下调。

</details>

<details>
<summary>Abstract</summary>

Animal pose estimation and tracking is important for wildlife monitoring and conservation research, and with limited expert time for labelling automated approaches are imperative. While human pose estimation and tracking has seen rapid progress thanks to large annotated datasets, animal pose remain challenging, due to large morphological and behavioural differences between species and limited annotated data. Existing approaches either optimise generic keypoint localisation from annotated datasets (such as APTv2) with poor generalisation, or track custom keypoints using visual tracking, at the cost of performance. In this paper, we demonstrate that vision foundation models trained on large datasets can be used effectively to track animal pose with limited labelled data. We propose two models, one unsupervised and the other supervised, to track user-selected keypoints in videos. The supervised approach delivers superior tracking accuracy by employing a keypoint prompt encoder to explicitly inject structural priors from a reference frame into feature matching. In parallel, the unsupervised route provides strong cross-species robustness by leveraging diverse foundation-model features for training-free correspondence matching. Extensive evaluation on challenging animal video benchmarks APTv2 and TigDog demonstrates that our framework achieves strong performance while maintaining an effective balance between accuracy and generalisation, offering a practical solution for real-world animal behaviour analysis and conservation applications.

</details>

#### 2026-08-05 - Cooking beyond Frames: A Stereo Event Camera Dataset in the Kitchen

**Authors:** Chengming Feng, Hesam Araghi, Liming Zheng, Julien Dupeyroux, Xucong Zhang, Jan van Gemert, Nergis Tömen
**Links:** [abs](https://arxiv.org/abs/2608.04865) - [pdf](https://arxiv.org/pdf/2608.04865)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, stereo depth, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cooking beyond Frames: A Stereo Event Camera Dataset in the Kitchen
- 作者：Chengming Feng, Hesam Araghi, Liming Zheng, Julien Dupeyroux, Xucong Zhang, Jan van Gemert, Nergis Tömen
- 出版日期：2026-08-05
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.04865

### 一句话总结
本文提出EventKitchen，一个大规模、无脚本、以自我为中心视角采集的厨房烹饪立体事件相机基准数据集，用于推动事件视觉在自然人类日常活动中的研究。

### 研究问题
现有事件相机数据集多聚焦于自动驾驶和无人机场景，而人类日常活动场景（尤其厨房烹饪）代表性不足；且已有事件人类活动数据集多采用脚本化动作录制，难以反映真实自然行为。因此需要构建一个覆盖自然、真实人类活动的立体事件相机基准数据集。

### 核心思路/方法
- 采集方式：10名参与者在13个不同厨房中佩戴集成多种传感器的头盔，以自我为中心视角自然进行烹饪活动，无任何脚本化动作。
- 数据模态：5.5小时立体事件记录，并同步采集RGB、深度和IMU数据。
- 标注：提供10,762个动作片段和13,482个边界框的人类标注。
- 基线任务：在数据集上训练基线模型，完成动作识别、目标检测和立体深度估计三个事件视觉任务。

### 主要贡献
- 构建EventKitchen数据集，覆盖大规模、立体、自然的人类烹饪活动，填补事件视觉在人类中心日常场景中的空白。
- 数据集包含多模态同步数据（事件、RGB、深度、IMU）和丰富人工标注。
- 提供多任务基线基准（动作识别、目标检测、立体深度估计），为后续研究建立评测参考。

### 局限性
- 摘要未提供数据集在场景分布、参与者多样性、光照条件变化等方面的详细局限性分析。
- 未报告基线模型的具体性能数值或对比结果。
- 摘要未提供关于数据采集设备规格、标注一致性校验等实现细节。
- 摘要未提及数据集在任务难度、失败案例或潜在偏差方面的讨论。

### 阅读优先级
**高**。理由：该工作展示了一个大规模、场景新颖（厨房烹饪）、自然行为采集的立体事件数据集，填补了事件视觉在人类日常活动中的空白，且包含多任务基线和丰富标注，对于从事事件相机、行为识别、多模态感知的研究者有较强的参考价值。

</details>

<details>
<summary>Abstract</summary>

Event cameras, also known as neuromorphic cameras, have gained significant attention in recent years due to their high temporal resolution, high dynamic range, and low power consumption. While many studies and datasets in neuromorphic vision have focused on automotive and drone applications, human-centric daily-life scenarios remain largely underrepresented, despite their importance for developing and benchmarking event-based perception systems. Moreover, the few existing event-based human activity datasets are typically recorded with scripted human actions, limiting their ability to capture natural human behaviors. In this paper, we introduce EventKitchen, a large-scale stereo event camera benchmark dataset of human cooking activities in the kitchen. EventKitchen is egocentrically collected from 10 participants in 13 diverse kitchens, where the participants wear a helmet with multiple sensors and naturally perform cooking activities, without any scripted actions. EventKitchen comprises 5.5 hours of stereo event recordings with synchronized RGB, depth, and IMU data. We provide human annotations for 10,762 action segments and 13,482 bounding boxes. We train baseline models on EventKitchen to perform multiple event-based tasks, including action recognition, object detection, and stereo depth estimation. By capturing natural, real-world human activities, EventKitchen establishes a challenging benchmark for neuromorphic vision beyond autonomous driving.

</details>

#### 2026-08-05 - Differential 6-DOF Pose Estimation with Provable First-Order Immunity to Camera Calibration Errors

**Authors:** Yueqiang Zhang, Liang Deng, Yi Zhang, Baoqiong Wang, Wenjun Chen, Shuixin Pan, Yulan Guo, Qifeng Yu
**Links:** [abs](https://arxiv.org/abs/2608.04673) - [pdf](https://arxiv.org/pdf/2608.04673)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, camera calibration, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Differential 6-DOF Pose Estimation with Provable First-Order Immunity to Camera Calibration Errors
- 作者：Yueqiang Zhang, Liang Deng, Yi Zhang, Baoqiong Wang, Wenjun Chen, Shuixin Pan, Yulan Guo, Qifeng Yu
- 出版日期：2026-08-05
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.04673

### 一句话总结
本文提出一种基于帧间图像位移和已知3D控制点的差分6自由度姿态估计方法，从理论上证明其对相机外参标定误差具有一阶免疫性，并在精度、鲁棒性和效率上优于现有PnP类方法。

### 研究问题
如何在不依赖逐帧绝对姿态估计的情况下，直接、鲁棒且高效地恢复平台6自由度微运动，特别是在存在相机外参标定误差时。

### 核心思路/方法
- 对透视投影方程进行差分，利用深度不变近似，并在SE(3)上建模运动，从而直接恢复平台运动，避免独立绝对姿态估计。
- 理论上证明平移外参误差可精确抵消，旋转误差仅引入有界扰动，扰动大小由标定误差、运动幅度和观测几何决定。
- 推导了可观测性条件、Cramér-Rao下界以及偏差消除的一致估计器，并刻画了近似成立的极限条件。
- 支持单目和多相机系统。

### 主要贡献
- 提出差分姿态估计方法，从根本上绕开绝对姿态估计带来的标定误差累积问题。
- 给出外参误差影响的理论证明（平移误差精确抵消、旋转误差有界）。
- 推导可观测性条件、CRB和一致估计器，提供理论保障。
- 在合成和真实实验中，相比代表性PnP和广义PnP方法，在精度、标定鲁棒性和计算效率上均达到新最优水平。
- 提供具体性能数据：单目（5个控制点，0.5像素噪声）旋转RMSE 10.09 arcsec、平移RMSE 3.70 mm、运行时间0.34 ms；双目对应分别为10.58 arcsec、3.91 mm、0.27 ms。

### 局限性
摘要未提供足够信息，无法判断该方法在更大控制点数量、更高噪声、极端运动幅度或动态场景中的表现，也未提及深度不变近似的具体失效条件及其工程影响。

### 阅读优先级
**高**。理由：论文提出一种新颖的差分姿态估计框架，兼具理论证明（外参误差免疫性、可观测性、CRB）和显著实验优势（精度、鲁棒性、效率），对机器人、自主系统和结构监测等领域的6自由度微运动估计具有直接应用价值，且代码将开源，便于复现和验证。

</details>

<details>
<summary>Abstract</summary>

Accurate six-degree-of-freedom (6-DOF) motion estimation is essential for robotic manipulation, autonomous systems, and structural displacement monitoring. Conventional 3D-2D methods estimate absolute camera poses independently at each time and recover platform motion through camera-to-platform extrinsics, making them sensitive to extrinsic calibration errors, especially for micromotion. We present a differential pose estimation method that directly recovers platform motion from inter-frame image displacements and known 3D control points. By differencing perspective projection equations, using a depth-invariance approximation, and modeling motion on SE(3), the method avoids independent absolute-pose estimation and supports both monocular and multi-camera systems. We prove that translational extrinsic errors cancel exactly, while rotational errors induce a bounded perturbation determined by calibration error, motion magnitude, and observation geometry. We also derive generic observability conditions, a Cramer-Rao lower bound, and a bias-eliminated consistent estimator, and characterize the validity limits of the approximations. Extensive synthetic and real-world experiments establish a new state of the art for 6-DOF platform micromotion estimation, outperforming representative PnP and generalized-PnP methods in accuracy, calibration robustness, and computational efficiency. With five control points and 0.5-pixel image noise, the monocular solver obtains a combined pitch-yaw rotation RMSE of 10.09 arcsec, a translation RMSE of 3.70 mm, and a runtime of 0.34 ms. The binocular solver achieves a rotation RMSE of 10.58 arcsec, a translation RMSE of 3.91 mm, and a runtime of 0.27 ms. Code will be released upon publication at https://github.com/zyoungszu/pami2026.

</details>

#### 2026-08-05 - VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances

**Authors:** Jihoon Oh, Kento Kawaharazuka, Kei Okada
**Links:** [abs](https://arxiv.org/abs/2608.05215) - [pdf](https://arxiv.org/pdf/2608.05215)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, mesh reconstruction, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances
- 作者：Jihoon Oh, Kento Kawaharazuka, Kei Okada
- 出版日期：2026-08-05
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.05215

### 一句话总结
本文提出VLAff，一个基于视觉-语言模型的统一基础模型，从人类第一人称视频中提取视觉、抓取和轨迹三类可操作可供性，并将其转化为机器人可直接执行的操纵动作。

### 研究问题
如何利用人类视频学习与机器人本体无关（embodiment-agnostic）的物体中心可操作可供性，以缓解机器人与人类之间的形态差异，从而支持可扩展的机器人技能学习。

### 核心思路/方法
- 利用第一人称人类视频，结合最先进的3D运动恢复结构（Structure-from-Motion）和手部网格重建技术，提取三类可操作可供性：
  - 视觉可供性（visual affordance）：指示“在哪里交互”；
  - 抓取可供性（grasp affordance）：指示“如何抓取”；
  - 轨迹可供性（trajectory affordance）：指示“如何移动”。
- 构建大规模数据集EgoAffordance，包含204K个片段、560万视觉可供性标注和1160万抓取及轨迹可供性标注。
- 提出VLAff，这是一个基于大规模视觉-语言模型（VLM）的统一基础模型，学习所有可操作可供性之间的跨模态相关性。
- 给定视觉观察和指令，VLAff生成视觉可供性热图、抓取姿态和轨迹，并利用3D场景信息将其转换为可直接执行的动作。

### 主要贡献
- 提出从人类视频中提取统一可操作可供性（视觉、抓取、轨迹）的框架。
- 构建大规模数据集EgoAffordance（204K片段，560万视觉可供性、1160万抓取和轨迹可供性）。
- 引入VLAff，一个基于大视觉-语言模型的统一基础模型，用于跨模态可供性学习。
- 实验表明VLAff在视觉可供性预测上达到最先进性能，并能有效应用于真实机器人场景，包括零样本操纵和可供性引导的机器人学习。

### 局限性
摘要未提供足够信息。例如，未提及数据集的具体场景多样性、模型计算开销、跨物体泛化能力上限，以及零样本操作的成功率或失败模式等具体实验细节。

### 阅读优先级
**高**

理由：该工作面向机器人学习中的核心挑战（人-机形态差异），提出了统一的可供性建模框架，并构建了大规模数据集和基于视觉-语言模型的基础模型，兼具数据、方法和应用验证，对具身智能、机器人操纵和视觉-语言模型交叉领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Learning manipulation skills from human videos is promising for scalable robot learning. However, the embodiment mismatch between humans and robots makes this challenging. One promising solution is to learn object-centric actionable affordances that are embodiment-agnostic. In this work, we propose a framework that leverages egocentric human videos with state-of-the-art 3D Structure-from-Motion and hand mesh reconstruction to extract actionable affordances such as visual, grasp, and trajectory affordances that explicitly encode where to interact, how to grasp, and how to move. We construct EgoAffordance, a large-scale dataset comprising 204K episodes with 5.6M visual affordances and 11.6M grasp and trajectory affordances. Building on this, we introduce VLAff, a large vision-language model-based unified foundation model that learns cross-modal correlations across all actionable affordances. Given a visual observation and instruction, VLAff generates visual affordance heatmaps, grasp poses, and trajectories, which are then converted into directly executable actions by utilizing 3D scene information. Through extensive experiments, we demonstrate that VLAff not only achieves state-of-the-art performance on visual affordance prediction, but can also be effectively applied to real robot applications such as zero-shot manipulation and affordance-guided robot learning.

</details>

#### 2026-08-04 - XiDepth: a Lightweight and Efficient Network for Self-supervised Monocular Depth Estimation

**Authors:** Elena Izzo, Riccardo Toniolo, Lamberto Ballan
**Links:** [abs](https://arxiv.org/abs/2608.03666) - [pdf](https://arxiv.org/pdf/2608.03666)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：XiDepth: a Lightweight and Efficient Network for Self-supervised Monocular Depth Estimation
- 作者：Elena Izzo, Riccardo Toniolo, Lamberto Ballan
- 出版日期：2026-08-04T13:42:41Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.03666

### 一句话总结
XiDepth 是一个基于 XiNet 算子模块的轻量级自监督单目深度估计网络，在 KITTI 数据集上以仅 0.8M 参数达到先进性能，并在嵌入式设备上显著降低 FLOPs 和能耗。

### 研究问题
如何在保持自监督单目深度估计性能的前提下，设计资源高效、适用于嵌入式环境的轻量级神经网络，同时避免依赖高能耗的深度卷积和注意力机制。

### 核心思路/方法
- 提出基于 XiNet 算子模块的轻量级架构 XiDepth，用于增强特征提取。
- 通过 XiNet 模块在保持低计算复杂度和低能耗的同时提升特征提取能力。
- 在 KITTI 数据集上评估精度，并在 Raspberry Pi 4 上进行嵌入式实际部署测试。

### 主要贡献
- 提出 XiDepth 轻量级网络架构，以 0.8M 参数在 KITTI 上达到最先进性能。
- 相比领先方法，在嵌入式设备上减少 40% FLOPs 和 35% 能耗。
- 验证了所提方法在真实嵌入式环境中的适用性，缓解了深度卷积与注意力机制在嵌入式平台上的兼容性问题。

### 局限性
摘要未提供足够信息，如具体精度数值、与其他方法的详细对比实验、不同场景下的泛化性测试，以及 XiNet 模块设计的内部细节均未披露。

### 阅读优先级
**中**  
理由：该工作针对嵌入式场景下的轻量级深度估计具有实际应用价值，且提供了参数规模、能耗降低等关键指标，实验结论清晰。但摘要未给出具体精度数值和详细对比，且主题相对专一，若你不是专门从事单目深度估计或嵌入式模型压缩方向，可暂缓精读。

</details>

<details>
<summary>Abstract</summary>

Self-supervised monocular depth estimation has emerged as an appealing solution to design lightweight and effective models for deployment on computationally constrained devices due to its reduced reliance on expensive depth sensors. By eliminating the need for ground-truth annotations and leveraging the simplicity of monocular camera setups, this approach facilitates cost-effective data collection and broad applicability across fields such as computer vision and robotics. A critical challenge is achieving resource-efficient neural networks without compromising the overall performance. State-of-the-art models generally adopt depth-wise convolutions and attention mechanisms; however, these functions often incur high energy costs and face compatibility issues in embedded environments. To address this, we propose XiDepth, a lightweight architecture based on the XiNet operator block, designed to enhance feature extraction while maintaining low computational complexity and energy demand. On the KITTI dataset, XiDepth achieves state-of-the-art performance with only 0.8M parameters. Tests on a Raspberry Pi 4 further confirm its suitability for real-world embedded applications, reducing FLOPs by 40% and energy consumption by 35% compared to leading methods.

</details>

#### 2026-08-04 - Detecting Pose Estimation Failures via Keypoint Self-Consistency

**Authors:** Robin Chan
**Links:** [abs](https://arxiv.org/abs/2608.03516) - [pdf](https://arxiv.org/pdf/2608.03516)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Detecting Pose Estimation Failures via Keypoint Self-Consistency
- 作者：Robin Chan
- 出版日期：2026-08-04
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.03516

### 一句话总结
本文提出利用手工设计的几何特征（如关键点对间距离、重投影一致性、渲染与掩码一致性）来检测基于关键点的位姿估计失败，并验证了简单逻辑回归分类器在检测可靠性上优于依赖关键点不确定性的置信度方法。

### 研究问题
如何通过检查2D关键点之间的空间位置关系（即关键点自一致性），来识别不准确的位姿估计结果，从而提升位姿估计在下游任务中的可靠性。

### 核心思路/方法
- 核心观察：旋转保持物体形状，但现有基于关键点的位姿估计方法通常独立预测各关键点，忽略了这一几何约束。
- 方法：提出一组手工设计的几何特征，用于捕捉关键点预测的自一致性，具体包括：关键点两两之间的距离、重投影一致性、渲染与掩码一致性。
- 检测模型：在这些特征上训练一个逻辑回归分类器，用于判断位姿估计是否失败。
- 对比基线：与基于置信度的方法（如符合性关键点预测，仅依赖关键点不确定性）进行对比。

### 主要贡献
- 提出利用关键点自一致性（而非仅关键点不确定性）来检测位姿估计失败的新思路。
- 设计了一组简单但有效的几何特征（距离、重投影、渲染/掩码一致性）。
- 实验表明，基于这些特征的逻辑回归分类器能够可靠检测位姿估计失败，并优于置信度基线方法。

### 局限性
摘要未提供足够信息，未说明方法在极端遮挡、对称物体、关键点标注噪声等场景下的表现，也未提及特征计算的额外计算开销或对不同数据集/位姿估计器（如PnP求解器）的泛化能力。

### 阅读优先级
**中**。理由：该工作聚焦于位姿估计的可靠性检测，方法简单且实验上有明显改进，但摘要未给出具体实验规模与量化结果（如准确率提升幅度、数据集范围），对追求实际应用的读者有一定参考价值，但对纯算法创新者可能吸引力有限。

</details>

<details>
<summary>Abstract</summary>

One common approach to pose estimation involves predicting object keypoints in an image, followed by using Perspective-n-Point algorithms to compute the object's rotation and translation relative to the camera. While rotations preserve object shapes, this property is often neglected in keypoint-based pose estimation methods, where keypoints are typically predicted independently from each other. As imprecise keypoint predictions negatively affects pose estimation accuracy, it also limits its reliability in downstream tasks. In this work, we explore whether such inaccurate pose estimates can be identified by simply examining spatial locations between 2D keypoints. We propose a set of hand-crafted geometric features that capture the self-consistency of keypoint predictions, including pairwise distances, reprojection consistency, as well as render and mask consistency. Despite its simplicity, a logistic regression classifier trained on these features reliably detects pose estimation failures, outperforming confidence-based approaches like conformal keypoint predictions that rely solely on keypoint uncertainty.

</details>

#### 2026-08-04 - SLAMFormer-$\infty$: Infinite SLAM Transformer for Unbounded Frontend and Backend Processing

**Authors:** Zhijian Fang, Weicheng Zheng, Yijun Yuan, Weibang Wang, Zhuoguang Chen, Chang Sun, Junhao Huang, Kenan Li, Minghui Qin, Hang Zhao
**Links:** [abs](https://arxiv.org/abs/2608.03429) - [pdf](https://arxiv.org/pdf/2608.03429)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SLAMFormer-$\infty$: Infinite SLAM Transformer for Unbounded Frontend and Backend Processing
- 作者：Zhijian Fang, Weicheng Zheng, Yijun Yuan, Weibang Wang, Zhuoguang Chen, Chang Sun, Junhao Huang, Kenan Li, Minghui Qin, Hang Zhao
- 出版日期：2026-08-04T10:19:27Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.03429

### 一句话总结
本文提出SLAMFormer-$\infty$，一个无需显式距离界限、可同时支持长距离前端与后端处理的几何Transformer，并能在超过17公里长的轨迹上运行。

### 研究问题
如何设计一个不依赖首帧锚定（first-frame-anchored）公式、且能无界处理长距离前端和后端任务的几何Transformer，以实现全局一致的轨迹估计与场景重建。

### 核心思路/方法
- 使用“记忆条件”（memory conditions）定义输入帧的灵活坐标系与尺度，替代传统首帧锚定公式，从而实现更富表达力的结构条件化。
- 前端部分保持高效局部计算，后端部分则联合优化长距离轨迹与场景几何，确保全局一致性。
- 基于上述公式构建Transformer架构，使其在无显式距离边界条件下同时支持前端与后端处理。

### 主要贡献
- 提出首个能支持长距离前端与后端处理且无显式距离界限的几何Transformer（SLAMFormer-$\infty$）。
- 引入记忆条件机制，实现灵活的坐标系与尺度定义，增强结构条件表达能力。
- 实验表明，该方法在大型数据集的轨迹估计与场景重建上达到优越或极具竞争力的性能。
- 验证了极长轨迹泛化能力，成功运行超过17公里的序列。

### 局限性
摘要未提供足够信息（未具体说明失败场景、计算资源需求、对数据集规模的依赖或与其他方法的定量对比细节）。

### 阅读优先级
**高**
理由：该工作针对SLAM中长距离无界处理这一关键难题提出新架构，且展示出超过17公里的实际泛化能力，对视觉定位与重建方向具有潜在重要价值；方法核心创新点（记忆条件替代首帧锚定）表述清晰，值得关注。

</details>

<details>
<summary>Abstract</summary>

We introduce the Infinite SLAM Transformer (SLAMFormer-$\infty$), the first geometric transformer capable of supporting both long-range frontend and backend processing without an explicit distance bound. Instead of relying on a first-frame-anchored formulation, SLAMFormer-$\infty$ employs memory conditions to define flexible coordinate systems and scales for input frames, enabling more expressive structural conditioning. Built upon this formulation, the frontend preserves efficient local computation, while the backend jointly optimizes long-range trajectories and scene geometry in a globally consistent manner. Experimental results demonstrate that SLAMFormer-$\infty$ achieves superior or highly competitive performance in both trajectory estimation and scene reconstruction across large-scale datasets. Notably, SLAMFormer-$\infty$ generalizes to extremely long trajectories, successfully operating on sequences exceeding $17\mathrm{km}$.

</details>

#### 2026-08-04 - SGFormer: Structure-Guided Transformer for Robust Local Feature Matching

**Authors:** Runyu Zhu
**Links:** [abs](https://arxiv.org/abs/2608.03423) - [pdf](https://arxiv.org/pdf/2608.03423)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, photogrammetry, feature matching, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SGFormer: Structure-Guided Transformer for Robust Local Feature Matching
- 作者：Runyu Zhu
- 出版日期：2026-08-04
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.03423

### 一句话总结
本文提出结构引导的Transformer（SGFormer），通过引入三重生结构注意力模块增强对重叠区域显著结构的关注，以缓解局部特征匹配中的注意力发散问题。

### 研究问题
现有免检测器匹配方法（如LoFTR）利用无约束注意力机制获取全局特征，但在大视角变化场景下，模型对显著结构的注意力不足，导致部分高置信度匹配落在有效重叠区域之外（作者将其定义为“注意力发散”），降低了匹配可靠性。

### 核心思路/方法
- 采用半稠密coarse-to-fine匹配流程。
- 在骨干网络中引入新的Triple-Structure-Attention（TSA）模块。
- TSA利用网络浅层提取的局部特征来增强显著结构附近的表示，引导后续Transformer阶段在全局范围内加大对显著结构区域的关注。
- 通过强化视觉一致区域的注意力、抑制非重叠区域的影响，缓解注意力发散。

### 主要贡献
- 首次定义并分析了特征匹配中的“注意力发散”现象。
- 提出SGFormer结构感知匹配网络，可自适应更新显著结构附近特征的注意力。
- 设计TSA模块，将浅层局部结构信息融入Transformer注意力更新过程。
- 实验表明该方法显著缓解注意力发散并提升匹配精度（具体实验数值摘要未提供）。

### 局限性
摘要未提供足够信息以评估具体局限（如计算开销、泛化边界、失败场景等）。

### 阅读优先级
**中**。理由：该论文针对LoFTR类方法的注意力发散问题提出明确改进方案，方法有清晰动机和新模块设计，适合关注局部特征匹配、三维重建及免检测器匹配的读者。但摘要未提供具体实验结果对比，无法判断实际性能提升幅度，且论文发布时间较远（2026年），需要进一步看全文实验部分才能评估其实际价值。

</details>

<details>
<summary>Abstract</summary>

Local feature matching is a fundamental component of photogrammetry, enabling accurate image correspondence critical for tasks such as 3D reconstruction, stereo mapping, and visual localization. While recent detector-free matching methods, like LoFTR, have advanced the field, the global features obtained by leveraging the global-range modeling capacity of the unconstrained attention mechanism compromise the model's attention to the salient structures in certain scenarios. This limitation leads to a phenomenon we define as attention divergence, wherein a portion of high-confidence matches are distributed outside the valid matching region (overlapping region), especially in scenes with large viewpoint variations. This occurs because similar features in irrelevant regions may receive equal weighting and consideration within the standard Transformer, limiting matching reliability in challenging photogrammetric environments. To address this issue in feature matching, we propose SGFormer (Structure-Guided Transformer), a novel structure-aware matching network that adaptively updates attention on features near salient structure in overlapping regions. SGFormer employs a semi-dense coarse-to-fine pipeline and incorporates the proposed Triple-Structure-Attention (TSA) module into the backbone net for extracting distinctive features. The TSA module utilizes shallow local features from early network layers to enhance the representation around salient structure, guiding subsequent transformer stages to intensify the model's focus on regions with salient structure across the global scope. SGFormer, thereby reinforcing attention to visually consistent areas while mitigating the influence of non-overlapping regions. Extensive experiments show that SGFormer significantly mitigates attention divergence and improves matching accuracy.

</details>

#### 2026-08-04 - Kitchen Robotic Manipulation utilizing Foundation Models

**Authors:** Myung-Hwan Jeon, Sankalp Yamsani, Joohyung Kim
**Links:** [abs](https://arxiv.org/abs/2608.04042) - [pdf](https://arxiv.org/pdf/2608.04042)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, pose estimation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Kitchen Robotic Manipulation utilizing Foundation Models
- 作者：Myung-Hwan Jeon, Sankalp Yamsani, Joohyung Kim
- 出版日期：2026-08-04
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.04042

### 一句话总结
本文提出了一种模块化的机器人厨房操作感知流水线，通过整合多个视觉和几何基础模型，在碗碟处理任务中实现了无需环境特定再训练的6D姿态估计与抓取规划。

### 研究问题
如何构建一个既鲁棒又自适应、能在真实家庭厨房环境中完成碗碟操作任务的机器人感知系统，并且无需针对特定环境进行重新训练。

### 核心思路/方法
采用模块化感知流水线设计，包含以下核心组件：
- 开放词汇目标检测
- 多视角分割
- 实例感知的3D重建
- 2D-3D特征融合策略，用于6D姿态估计和抓取规划

由于流水线是模块化的，可以系统性地替换多种视觉和几何基础模型，从而通过评估找到最佳配置。最佳配置为 LLMDet + SAMv2 + DINOv2 + GeoTransformer，并在自定义厨房数据集上进行了评估。

### 主要贡献
- 提出了一种模块化、可替换的机器人厨房操作感知流水线框架。
- 通过系统性组合和评估，确定了一个最佳配置（LLMDet + SAMv2 + DINOv2 + GeoTransformer），在20场景厨房基准（含杂乱和遮挡条件）上达到89.12%的ADI。
- 在真实机器人上验证了最佳配置的可部署性，无需环境特定再训练，成功执行了水池到洗碗机的转移和杯子堆叠等任务。
- 证明该流水线对家庭机器人系统具有适应性和可扩展性，并公开了代码和补充材料。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文面向家庭机器人操作这一实际应用场景，采用模块化基础模型组合的思路具有较强工程实用价值；提供了定量基准（89.12% ADI）和真实机器人演示验证，结果可信度较高；且公开代码和补充材料，便于复现和进一步研究。对于从事机器人感知、6D姿态估计或基础模型应用的研究者，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Deploying robots in everyday human environments requires perception systems that are both robust and adaptable to diverse, dynamic conditions. In this work, we present a modular perception pipeline for household manipulation tasks, with a focus on dishware handling in kitchen environments. The pipeline integrates open-vocabulary object detection, multi-view segmentation, instance-aware 3D reconstruction, and a 2D-3D feature fusion strategy for 6D pose estimation and grasp planning. Its modular design enables systematic substitution of multiple visual and geometric foundation models, allowing us to identify the best-performing configuration through extensive evaluation on a custom kitchen dataset. The best-performing configuration (LLMDet + SAMv2 + DINOv2 + GeoTransformer) achieves an ADI of 89.12\% on the 20-scene kitchen benchmark with cluttered and occluded conditions. Furthermore, real-world demonstrations confirm that the best configuration can be deployed on physical robots without environment-specific retraining, successfully executing tasks such as sink-to-dishwasher transfer and cup stacking. It validates the adaptability and scalability of the pipeline and highlights its potential as a practical framework for household robotic systems. Our code and supplementary materials are available at https://raivlab.github.io/FM_kitchen .

</details>

#### 2026-08-03 - CalibBEV: LiDAR-Camera Calibration via BEV Alignment

**Authors:** Filippo D'Addeo, Lorenzo Cipelli, Adriano Cardace, Emanuele Ghelfi, Andrea Zinelli, Massimo Bertozzi
**Links:** [abs](https://arxiv.org/abs/2608.02309) - [pdf](https://arxiv.org/pdf/2608.02309)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CalibBEV: LiDAR-Camera Calibration via BEV Alignment
- 作者：Filippo D'Addeo, Lorenzo Cipelli, Adriano Cardace, Emanuele Ghelfi, Andrea Zinelli, Massimo Bertozzi
- 出版日期：2026-08-03
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.02309

### 一句话总结
CalibBEV 提出了一种基于鸟瞰图（BEV）特征对齐的两步式 LiDAR-相机标定方法，通过隐式粗对齐和显式精对齐实现高效、鲁棒的跨模态标定，在 KITTI 和 nuScenes 数据集上显著优于现有方法。

### 研究问题
如何利用 BEV 空间的统一表征，实现 LiDAR 与相机之间高精度、鲁棒的自动标定，从而替代传统的点对像素匹配方法。

### 核心思路/方法
1. **统一空间表征**：将 LiDAR 和相机数据分别映射到共享的 3D BEV 空间中，提取各自的 BEV 特征。
2. **两步对齐流程**：
   - **隐式对齐（第一步）**：直接从 BEV 特征回归一个粗标定矩阵。
   - **显式对齐（第二步）**：利用 BEV 公式将一种模态的特征与另一种模态对齐，细化粗估计为精准的标定矩阵。
3. **语义一致性约束**：引入受 CLIP 启发的对比损失，迫使两个模态的 BEV 特征在空间中语义一致，引导网络学习统一特征空间。

### 主要贡献
- 提出新颖的 BEV 对齐标定框架，统一了 LiDAR 与相机的空间表征。
- 设计两步对齐机制（隐式+显式），兼顾粗定位与精细化。
- 采用对比损失实现跨模态语义一致性，提升特征融合质量。
- 在 KITTI 和 nuScenes 基准上大幅超越先前方法：RRE 分别降低 51% 和 68%，RTE 分别降低 80% 和 91%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法在标定精度上取得了大幅度提升（RRE/RTE 相对降低 51%~91%），且采用两步对齐+对比学习的思路具有创新性，对多传感器融合与自动驾驶领域有重要参考价值。摘要提供了清晰的性能对比，展示了显著优势。

</details>

<details>
<summary>Abstract</summary>

We present CalibBEV, a novel Bird's Eye View (BEV) alignment approach for LiDAR-camera calibration. Our method unifies LiDAR and camera data into a shared 3D spatial representation, enabling accurate and robust cross-modal calibration. CalibBEV extracts sensor-wise BEV features from each modality using domain-specific architectures and estimates the calibration matrix through a two-step alignment process. First, we perform an implicit alignment by regressing a coarse calibration matrix directly from the BEV features. To ease this alignment, we enforce semantic consistency between BEV representations across modalities using a contrastive loss inspired by CLIP, guiding both networks toward a unified feature space. In the second step, we leverage our BEV formulation to explicitly align the features of one modality with the other, refining the initial coarse estimate into a final, more accurate calibration matrix. CalibBEV significantly outperforms prior point-to-pixel matching methods, achieving state-of-the-art calibration accuracy. On the KITTI and nuScenes benchmarks, our method reduces the Relative Rotation Error (RRE) by 51% and 68%, and the Relative Translation Error (RTE) by 80% and 91%, respectively, compared to previous methods.

</details>

#### 2026-08-03 - TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction

**Authors:** Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang
**Links:** [abs](https://arxiv.org/abs/2608.02304) - [pdf](https://arxiv.org/pdf/2608.02304)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction
- 作者：Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang
- 出版日期：2026-08-03T14:30:20Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02304

### 一句话总结
本文提出将主动场景重建视为遍历覆盖问题，通过核遍历水平规划器在线生成与当前地图信息分布匹配的传感器轨迹，以替代贪婪的逐次最优视点选择。

### 研究问题
现有基于高斯泼溅地图的主动重建系统采用贪心策略，每步仅优化单个下一个最佳视角（NBV），并用短视路径连接已选视角。这种贪婪解耦方式忽略场景信息的全局结构，产生低效轨迹，在视角之间浪费感知能力。因此，研究问题是如何设计考虑全局信息分布的轨迹优化方法。

### 核心思路/方法
- 将主动重建形式化为遍历覆盖问题：要求传感器轨迹的时间平均空间统计量匹配由当前地图导出的目标信息分布。
- 目标信息分布在线由不确定性和可见性推导得到。
- 通过核遍历水平规划器（kernel-ergodic horizon planner）计算遍历轨迹，结合梯度流和足迹耗尽（footprint depletion）机制。
- 在映射与轨迹优化之间形成闭环。

### 主要贡献
- 提出新的主动重建范式：从贪心NBV转向全局遍历轨迹优化。
- 设计在线推导目标信息分布的方法（基于不确定性和可见性）。
- 开发核遍历水平规划器，带有梯度流与足迹耗尽机制，实现映射与轨迹优化的闭环集成。
- 在Replica数据集上相较于NBV基线，将PSNR提升1.5 dB。

### 局限性
摘要未提供足够信息（未提及计算开销、对动态环境适应能力、真实场景测试结果、与更多基线对比的细节、算法收敛性保证等）。

### 阅读优先级
**高**。理由：该工作针对主动重建中贪心策略效率低下的核心问题，提出全局遍历优化的新视角，方法上有闭环设计，并在公开基准上取得定量提升（PSNR +1.5 dB），对该领域研究者具有参考价值。此外提供了开源代码，便于复现和扩展。

</details>

<details>
<summary>Abstract</summary>

Existing active reconstruction systems with Gaussian-splatting maps select observations greedily, optimizing a single next-best-view (NBV) at each step and connecting the chosen views by short-horizon path planning. This greedy decoupling disregards the global structure of scene information, producing inefficient trajectories that waste sensing capacity in transit between selected views. In this work, we study active reconstruction as an ergodic coverage problem: the time-averaged spatial statistics of the sensor trajectory should match a target information distribution induced by the current map. Our approach derives this target distribution online from uncertainty and visibility, and calculates ergodic trajectories via a kernel-ergodic horizon planner with gradient flow and footprint depletion, closing the loop between mapping and trajectory optimization. We thoroughly evaluate TRACE on the Replica dataset against the Next-Best-View (NBV) baselines, improving PSNR by 1.5 dB. Code: https://github.com/spikelab-jhu/trace-active-reconstruction.

</details>

#### 2026-08-03 - UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction

**Authors:** Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan
**Links:** [abs](https://arxiv.org/abs/2608.02145) - [pdf](https://arxiv.org/pdf/2608.02145)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction
- 作者：Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan
- 出版日期：2026-08-03T12:31:12Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02145

### 一句话总结
UniqueSplat提出一种基于视图条件的三维高斯泼溅前馈模型，通过动态调整高斯分布来适应不同查询视角，提升通用三维重建的精度与泛化能力。

### 研究问题
现有前馈三维重建方法（如pixelSplat和MVSplat）为每个场景生成固定的三维高斯表示，无法根据目标视角动态调整，导致对特定视点的适应能力不足。研究问题是如何将目标视角信息融入高斯预测过程，实现视图自适应的三维重建。

### 核心思路/方法
提出一种双分支视图条件超网络（view-conditioned hyperNetwork），同时学习视图无关的嵌入表示（共享知识）和视图特定的知识（适应具体视角），将目标视角信息作为先验注入网络参数，使高斯分布能随查询视角动态调整，从而在测试时为不同视图定制化重建辐射场。

### 主要贡献
- 提出UniqueSplat，一种视图条件的前馈三维高斯泼溅模型，支持按查询视角动态生成高斯表示。
- 设计双分支视图条件超网络，同时建模视图共享与视图特定信息。
- 在RealEstate10K、ACID和DTU数据集上超越现有最先进方法，并在跨数据集评估中表现出更强的泛化能力。

### 局限性
摘要未提供足够信息（未提及计算开销、推理速度、对输入视图数量的敏感性、失败案例或潜在限制）。

### 阅读优先级
**高**。理由：针对三维高斯泼溅前馈重建中的视角自适应问题提出了新的解决方案，创新性明确，并在多个主流数据集及跨数据集评估中验证了性能提升，对从事通用三维重建和神经场景表示研究的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

In this paper, we propose UniqueSplat, a view-conditioned feed-forward 3D Gaussian Splatting model to reconstruct customized 3D radiance fields for each view query. Existing feed-forward methods such as pixelSplat and MVSplat aim to generate fixed Gaussians across all views of each scene by minimizing the error between rendered views and ground-truth images. However, such fixed Gaussians generally render images from all views and lack the ability to adapt to specific viewpoints, as they do not incorporate target view information when predicting Gaussians. To address this, our UniqueSplat learns the view-conditioned information as a prior and incorporates this knowledge into network parameters, so that Gaussians are dynamically adjusted in accordance with different views. Specifically, we propose a two-branch view-conditioned hyperNetwork to simultaneously learn view-agnostic embeddings and view-specific knowledge, which not only explores the shareable knowledge from various views, but also adapts the model to specific views at test time. Extensive experiments on widely-used datasets including RealEstate10K, ACID and DTU demonstrate the superiority of UniqueSplat over the state-of-the-art methods. Moreover, UniqueSplat encouragingly outperforms existing methods in cross-dataset evaluation, showing its notable generalization ability.

</details>

#### 2026-08-03 - GIFT: Geometry-Invariant Fine-Tuning for Non-Lambertian Monocular Depth Estimation

**Authors:** Xianghui Fan, Zhaoyu Chen, Bingqian Wu, Dayu Li, Xin Zeng, Huanran Cui, Guangzhen Xu, Xiangru Huang, Hang Yang
**Links:** [abs](https://arxiv.org/abs/2608.02068) - [pdf](https://arxiv.org/pdf/2608.02068)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GIFT: Geometry-Invariant Fine-Tuning for Non-Lambertian Monocular Depth Estimation（GIFT：面向非朗伯单目深度估计的几何不变微调）
- 作者：Xianghui Fan, Zhaoyu Chen, Bingqian Wu, Dayu Li, Xin Zeng, Huanran Cui, Guangzhen Xu, Xiangru Huang, Hang Yang
- 出版日期：2026-08-03
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.02068

### 一句话总结
GIFT 提出一种无需深度标签的参数高效微调框架，利用非朗伯表面在表观变化下几何不变的特性，抑制单目深度基础模型在镜面和透明物体上的深度幻觉。

### 研究问题
单目深度基础模型在非朗伯表面（如镜子、玻璃）上会产生深度幻觉——估计的是反射或透射内容的位置，而非物理表面的实际深度。由于传统深度传感器在此类区域同样不可靠，如何在不依赖实测深度标签的情况下，适应真实世界非朗伯场景成为难题。

### 核心思路/方法
- **关键观察**：非朗伯表面的外观会随反射或透射环境变化，但其底层几何（物理表面位置）保持不变。
- **方法框架**：在保持相机与目标几何固定的条件下，采集多组受控外观变化的 RGB 图像；利用这些观测之间的几何不变性作为监督信号，进行参数高效的模型微调（后训练阶段），从而抑制非朗伯深度幻觉，同时保持基础模型泛化能力。
- **评测方式**：构建受控基准，评估非朗伯深度恢复、外观变化鲁棒性，以及在其余区域的性能保持情况。

### 主要贡献
1. 提出基于几何不变性的无标签微调框架（GIFT），用于非朗伯场景深度估计，无需实测深度标签。
2. 设计受控的数据采集方案（外观变化、几何固定）以利用几何不变性。
3. 构建专门的非朗伯深度恢复基准，涵盖深度恢复质量、外观变化鲁棒性及性能保留三个维度。
4. 在基准和独立真实数据集上验证，GIFT 能改善镜面与透明物体深度预测，同时大体保持基础模型原有性能。

### 局限性
摘要未提供足够信息（如方法对极端表观变化、复杂多非朗伯物体共存场景的处理能力、微调计算成本具体数值、失效边界等均未提及）。

### 阅读优先级
**中**
理由：该工作针对单目深度估计中非朗伯表面这一明确痛点，思路新颖（利用几何不变性替代深度标签），且提供了低成本、实用的解决方案，对从事深度估计、三维重建的研究者有参考价值。但当前摘要未给出量化性能对比细节，若需判断方法优越性，还需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Monocular depth foundation models, benefiting from large-scale synthetic training data, have demonstrated strong generalization. However, they often hallucinate depth on non-Lambertian surfaces, estimating reflected content in mirrors or transmitted content behind glass rather than the physical surface itself. Adapting these models with real-world data is challenging because conventional depth sensors are also unreliable in such regions. We observe that while the appearance of a non-Lambertian surface varies with its reflected or transmitted environment, its underlying geometry remains unchanged. Based on this observation, we propose GIFT (Geometry-Invariant Fine-Tuning), a parameter-efficient post-training framework that requires no measured depth labels. We collect groups of RGB images under controlled appearance changes while keeping the camera and target geometry fixed. GIFT exploits geometric invariance across these observations to suppress non-Lambertian depth hallucinations while retaining general depth estimation capability. We further construct a controlled benchmark that evaluates non-Lambertian depth recovery, robustness to appearance changes, and performance retention in other regions. Experiments on our benchmark and an independent real-world dataset demonstrate that GIFT improves depth prediction for mirrors and transparent objects while largely preserving the base model's performance, providing a practical and low-cost approach for adapting monocular depth foundation models to non-Lambertian scenes.

</details>

#### 2026-08-03 - CHOW-SLAM: Compact Hybrid Representation with Complementary Overlap Window Optimization for RGB-D SLAM

**Authors:** Wenxuan Ji, Jin Xiao, Xiaoguang Hu, Jiaqi Shi, Zichong Jia, Baochang Zhang
**Links:** [abs](https://arxiv.org/abs/2608.01914) - [pdf](https://arxiv.org/pdf/2608.01914)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, simultaneous localization and mapping, SLAM, pose estimation, bundle adjustment, NeRF, neural rendering, rendering, radiance, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CHOW-SLAM: Compact Hybrid Representation with Complementary Overlap Window Optimization for RGB-D SLAM
- 作者：Wenxuan Ji, Jin Xiao, Xiaoguang Hu, Jiaqi Shi, Zichong Jia, Baochang Zhang
- 出版日期：2026-08-03
- 分类：3D Reconstruction & Multi-view Geometry（次要分类：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.01914

### 一句话总结
本文提出CHOW-SLAM，一种通过紧凑混合场景表示与互补重叠窗口优化策略，同时构建空间和时间约束，以提升RGB-D神经SLAM系统重建质量与跟踪精度的方法。

### 研究问题
现有基于NeRF的SLAM系统在有限在线资源下，难以同时构建两类约束：来自场景表示的紧凑且可区分的空间约束，以及来自历史观测的持续时间约束。如何平衡并有效利用这两类约束是本文要解决的核心问题。

### 核心思路/方法
- **空间约束**：提出紧凑的参数化哈希（P-H）混合表示，基于平面和网格在不同尺度上组织P与H分支组件；使用统一多输出解码器对齐TSDF与密度诱导的射线终止分布，在紧凑参数预算下保持几何和外观。
- **时间约束**：提出互补重叠窗口策略，在固定预算内保留近期帧、选择高重叠局部帧，并引入时间分布的历史关键帧，避免优化被短期重叠或弱相关历史观测主导。
- **优化调度**：采用损失感知的关键帧插入和捆绑调整调度，使优化适应跟踪质量。
- **位姿初始化**：使用ORB特征跟踪和几何位姿估计进行初始化，随后通过神经渲染优化提升跟踪稳定性。

### 主要贡献
1. 提出显式构建互补空间与时间约束的密集RGB-D SLAM框架CHOW-SLAM。
2. 设计紧凑的参数化哈希混合表示，结合统一多输出解码器，在紧凑参数下保持重建质量。
3. 提出互补重叠窗口策略及损失感知的调度机制，提升优化稳定性与效率。
4. 在多个数据集上验证，重建质量和跟踪精度均优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对神经SLAM中空间与时间约束难以兼顾的关键挑战，提出了兼具表示创新（P-H混合表示）和优化策略创新（互补重叠窗口）的完整框架，实验结果在重建质量和跟踪精度上均优于SOTA，且提供了开源代码，对RGB-D神经SLAM方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Simultaneous localization and mapping (SLAM) based on Neural Radiance Fields (NeRF) enables dense, continuous scene reconstruction. However, existing systems operating with limited online resources struggle to simultaneously construct two types of constraints, namely, compact yet discriminative spatial constraints derived from scene representations and persistent temporal constraints derived from historical observations. To address this challenge, we propose CHOW-SLAM, a dense RGB-D SLAM framework that explicitly constructs these complementary spatial and temporal constraints. Spatially, we propose a compact parametric-hash (P-H) hybrid representation that organizes components based on planes and grids across scales in P and H branches. A unified multi-output decoder further aligns the ray termination distributions induced by TSDF and density, preserving geometry and appearance under a compact parameter budget. Temporally, we propose a complementary overlap-window strategy to prevent optimization from being dominated by short-term overlap or weakly related historical observations. Within a fixed budget, the strategy retains recent frames, selects high-overlap local frames, and introduces temporally distributed historical keyframes. Loss-aware keyframe insertion and bundle adjustment scheduling further adapt optimization to tracking quality. In addition, ORB-based tracking and geometric pose estimation are used for pose initialization, followed by neural rendering optimization to improve tracking stability. Extensive evaluations on multiple datasets demonstrate that CHOW-SLAM outperforms state-of-the-art methods in both scene reconstruction quality and camera tracking accuracy. The source code is available at https://github.com/jinjidexiaohuoban/CHOW-SLAM.

</details>

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-06 - Floating Radiance Networks

**Authors:** Krzysztof Byrski, Rafał Tobiasz, Grzegorz Wilczyński, Mikołaj Zieliński, Dawid Baran, Dominik Belter, Jacek Tabor, Przemysław Spurek
**Links:** [abs](https://arxiv.org/abs/2608.05920) - [pdf](https://arxiv.org/pdf/2608.05920)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, neural rendering, novel view synthesis, view synthesis, scene representation, neural scene representation, rendering, radiance, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Floating Radiance Networks (FlaRe)
- 作者：Krzysztof Byrski, Rafał Tobiasz, Grzegorz Wilczyński, Mikołaj Zieliński, Dawid Baran, Dominik Belter, Jacek Tabor, Przemysław Spurek
- 出版日期：2026-08-06T11:50:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.05920

### 一句话总结
Floating Radiance Networks (FlaRe) 是一种将可光线追踪的显式几何与连续神经辐射函数相结合的神经场景表示，通过浮动的平面高斯原语实现交互式渲染、光线追踪、几何变形与外观编辑的统一。

### 研究问题
现有神经场景表示方法大多紧密耦合于单一渲染范式，限制了其通用性以及与常规图形工作流的集成能力。本文旨在提出一种同时具备显式可寻址结构与神经场表达能力的统一场景表示方法。

### 核心思路/方法
- 场景由浮动的平面广义高斯原语表示，每个原语携带一个紧凑的局部辐射场潜在描述符。
- 共享的轻量解码器将该描述符、局部表面坐标和观察方向映射为颜色与不透明度。
- 通过硬件加速的原语求交实现交互式渲染和递归光线追踪（包括反射、折射、透明和阴影）。
- 同一表示支持原语级变形、网格提取以及直接在潜在描述符空间中进行外观风格化。

### 主要贡献
- 提出 FlaRe，一种结合显式光线追踪几何与连续神经辐射函数的统一神经场景表示。
- 实现显式可寻址结构，支持高效查询和操作，突破单一渲染范式限制。
- 支持交互式渲染、递归光线追踪（反射、折射、透明、阴影）以及原语级变形、网格提取和外观风格化。
- 在标准重建基准上展示有竞争力的渲染质量，且仅使用紧凑的原语集。

### 局限性
摘要未提供足够信息（未提及具体实验配置、定量评估细节、失败案例或计算开销等局限）。

### 阅读优先级
**高**  
理由：该工作提出了一种统一的神经场景表示，同时支持高质量神经渲染、传统光线追踪、几何操作与外观编辑，解决现有方法渲染范式单一的问题。研究内容具有较强的方法创新性和实际应用潜力（如交互式渲染和图形学工作流集成），适合关注神经渲染、场景表示和图形学交叉方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent advances in neural scene representations enable photorealistic novel-view synthesis, yet most methods remain tightly coupled to a single rendering paradigm, limiting their versatility and integration with conventional graphics workflows. We introduce Floating Radiance Networks (FlaRe), a neural scene representation combining explicit ray-traceable geometry with continuous neural radiance functions. A scene is represented by floating planar generalized Gaussian primitives, each carrying a compact latent descriptor of a local radiance field. A lightweight decoder shared across the scene maps this descriptor, local surface coordinates, and viewing direction to color and opacity. This formulation preserves the expressiveness of neural fields while providing an explicitly addressable structure that can be efficiently queried and manipulated. Hardware-accelerated primitive intersections enable interactive rendering and recursive ray-tracing, including reflections, refractions, transparency, and shadows. The same representation further supports primitive-level deformation, mesh extraction, and appearance stylization directly in its learned descriptor space. Experiments across standard reconstruction benchmarks demonstrate competitive rendering quality while using a compact set of primitives. Together, these results establish FlaRe as a versatile representation that brings high-fidelity neural rendering, ray-tracing, geometric manipulation, and appearance editing into a unified scene model. Source code is available online. Source code can be found at: https://github.com/KByrski/FlaRe

</details>

#### 2026-08-06 - G$^2$ARD-GS: Geometry-Guided Anchor-Regularized Gaussian Splatting Distillation

**Authors:** Puyuan Zhang, Jianming Huang, Wenkai Ye, Wei Dong
**Links:** [abs](https://arxiv.org/abs/2608.05704) - [pdf](https://arxiv.org/pdf/2608.05704)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G²ARD-GS: Geometry-Guided Anchor-Regularized Gaussian Splatting Distillation
- 作者：Puyuan Zhang, Jianming Huang, Wenkai Ye, Wei Dong
- 出版日期：2026-08-06
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.05704

### 一句话总结
本文提出一种几何引导的蒸馏方法，将稠密高斯先验压缩为紧凑表示，在不增加或删除原语的前提下恢复外观，实现高效的三维高斯渲染与几何复用。

### 研究问题
如何在不牺牲新视角合成质量和几何可用性的前提下，将稠密彩色LiDAR地图转换的3D高斯表示（含数百万个原语）大幅压缩为紧凑、可复用且可稳定渲染的表示。

### 核心思路/方法
- 将稠密高斯先验（可来自无训练的LiDAR点云提升或已训练的3DGS模型）通过几何引导的蒸馏方法逐步合并为表面感知的代表性原语。
- 在构造阶段固定紧致拓扑之后，仅在构造时锚点约束下恢复外观，恢复过程中不增加或删除任何原语。
- 在有限监督条件下，采用几何感知的视角选择策略来分配可用的视角预算。

### 主要贡献
- 提出G²ARD-GS，一种几何引导的蒸馏框架，将稠密高斯先验压缩为紧凑、可复用的表示。
- 在MatrixCity数据集上，在5×–30×压缩预算下取得最佳PSNR、SSIM和LPIPS，PSNR比PUP高3.2–6.8 dB。
- 当紧致模型作为冻结几何复用时，在偏离轨迹的外观适配上比PUP 3D-GS提升3.7–4.9 dB，并在30×压缩下保持Cambridge KingsCollege上的图像到模型配准精度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：本文针对3DGS大规模应用中的存储和渲染成本问题提出系统化压缩蒸馏方案，实验在多个指标和压缩倍率下显著优于现有方法，且涉及几何复用与配准等实用性验证，对神经场景表示与渲染方向的研究者和工程实践者均有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Dense colored LiDAR maps provide accurate city-scale geometry, but lifting them into 3D Gaussian Splatting (3DGS) retains millions of primitives, making the resulting models costly to store, transmit, render, and adapt. Aggressive primitive reduction alleviates this burden, but can remove the local surface support needed for stable novel-view synthesis and downstream geometric use. We introduce G$^2$ARD-GS, a geometry-guided distillation method that converts a dense Gaussian prior instantiated either as a training-free point-cloud lift or a trained GS model into a compact, reusable representation. G$^2$ARD-GS progressively consolidates the prior into surface-aware representatives, then recovers appearance on the resulting fixed topology under construction-time anchor constraints, with no primitives added or removed during recovery. Under limited supervision, geometry-aware view selection allocates the available view budget. On MatrixCity, G$^2$ARD-GS achieves the best PSNR, SSIM, and LPIPS across matched $5\times$--$30\times$ compression budgets, outperforming PUP by $3.2$--$6.8$,dB in PSNR. When reused as frozen geometry, the compact model improves off-trajectory appearance adaptation by $3.7$--$4.9$,dB over PUP 3D-GS and preserves image-to-model registration accuracy on Cambridge KingsCollege at $30\times$ compression. Project page: https://patrick1159.github.io/gardGS-page/.

</details>

#### 2026-08-06 - ESVR: 3D Ellipsoid-based Sparse Volume Rendering via Structure-aware Primitive Learning and Per-primitive Ray Sampling

**Authors:** Suemin Jeon, Youjin Kim, Jungwoo Park, Kyungryun Lee, Won-Ki Jeong
**Links:** [abs](https://arxiv.org/abs/2608.05564) - [pdf](https://arxiv.org/pdf/2608.05564)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ESVR: 3D Ellipsoid-based Sparse Volume Rendering via Structure-aware Primitive Learning and Per-primitive Ray Sampling
- 作者：Suemin Jeon, Youjin Kim, Jungwoo Park, Kyungryun Lee, Won-Ki Jeong
- 出版日期：2026-08-06
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.05564

### 一句话总结
ESVR提出了一种基于椭球体稀疏体渲染框架，直接从三维体积数据学习紧致椭球基元，实现大面积稀疏数据的高压缩比与实时渲染。

### 研究问题
大型稀疏体数据的高效表示与渲染问题——有意义结构仅占空间域一小部分，传统直接体渲染（DVR）的计算与内存开销随数据规模增长而急剧扩大，而现有基于3DGS的方法从渲染图像而非原始体积学习，导致信息损失并限制交互式传输函数控制。

### 核心思路/方法
- 提出椭球体稀疏体渲染框架（ESVR），直接在三维空间学习并渲染体数据。
- 使用具有有界支撑的可微椭球基元表示体积场景。
- 引入结构感知的基元学习与互补剪枝策略，提升基元对结构的表达能力。
- 设计逐基元光线采样策略，实现快速、准确的传输函数映射。
- 为支持大规模数据集，提出基于块（chunk）的优化方案，并引入“幽灵椭球”（ghost ellipsoids）以提供训练时边界上下文。

### 主要贡献
- 提出首个无需依赖DVR渲染图像、直接对原始体数据进行学习的椭球体稀疏渲染框架。
- 结合结构感知基元学习、逐基元光线采样与块式优化，实现高效表示与灵活传输函数控制。
- 在大型稀疏数据集上实现高达四个数量级的压缩比，并以43–223 FPS实时渲染，同时保持有竞争力的重建质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向科学可视化中的大规模稀疏体数据渲染，提出直接基于原始体积的学习方案，弥补了现有3DGS方法的信息损失问题，具有一定创新性；但摘要未提供与现有方法的定量对比细节或消融实验，应用场景偏专业领域，适合对体渲染、科学可视化感兴趣的读者重点阅读。

</details>

<details>
<summary>Abstract</summary>

Efficient representation and rendering of large-scale sparse volumetric data remain challenging in scientific visualization, as meaningful structures often occupy only a small fraction of the spatial domain. While direct volume rendering (DVR) provides high-quality visualization, its computational and memory costs scale poorly with data size. Recent advances in 3D Gaussian Splatting (3DGS) address this challenge by representing volumetric scenes with compact geometric primitives, enabling efficient, high-fidelity rendering. However, existing 3DGS-based methods learn from DVR rendered images rather than raw volumes, leading to information loss and limiting flexible transfer function control for interactive exploration. To address these limitations, we propose ESVR, an ellipsoid-based sparse volume rendering framework that directly learns and renders volumetric data in 3D space. Our method combines differentiable ellipsoidal primitives with bounded support, structure-aware primitive learning with complementary pruning, and a per-primitive ray sampling strategy for fast and accurate transfer function mapping. To support large-scale datasets, we further introduce a chunk-based optimization scheme with ghost ellipsoids, providing boundary context during training. Across large sparse datasets, ESVR achieves up to four orders of magnitude compression and real-time rendering at 43-223 FPS while maintaining competitive reconstruction quality.

</details>

#### 2026-08-06 - CDSeg: A Renderable Gaussian Carrier for Image-to-3D Label Transfer

**Authors:** Wentao Sun, Yiping Chen, Zhengsen Xu, Jonathan Li, John S. Zelek
**Links:** [abs](https://arxiv.org/abs/2608.05482) - [pdf](https://arxiv.org/pdf/2608.05482)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CDSeg: A Renderable Gaussian Carrier for Image-to-3D Label Transfer
- 作者：Wentao Sun, Yiping Chen, Zhengsen Xu, Jonathan Li, John S. Zelek
- 出版日期：2026-08-06
- 分类：Neural Scene Representations & Rendering
- 链接：
  - 摘要：https://arxiv.org/abs/2608.05482
  - PDF：https://arxiv.org/pdf/2608.05482

### 一句话总结
CDSeg 利用高斯溅射（Gaussian Splatting）基元作为可渲染的标签载体，将外部二维掩码标签跨视图迁移到三维场景（点云或高斯场景）中，无需任务特定的三维分割训练。

### 研究问题
如何将图像域中现成的二维分割掩码（如提示式、自动实例、语义及 LiDAR 设置）可靠地传递到三维空间中的对应位置，而不需要为每个任务训练专门的三维分割网络。

### 核心思路/方法
- 将每个输入点补全为一个高斯基元（保留其索引），或复用已优化高斯场景中的原生基元，构成“可渲染的标签载体”。
- 在渲染过程中记录像素与高斯基元之间的关联，通过渲染器导出的可见性决定哪些三维基元接收标签。
- 对多视角掩码进行投票融合，并应用局部滤波以提升标签一致性。
- 标签结果可返回原始点、保留在高斯场景上，或渲染到其他视图。

### 主要贡献
- 提出 CDSeg，一个跨域标签迁移接口，覆盖点云、高斯场景和图像视图，无需任务特定的三维分割网络。
- 支持多种掩码来源（提示式、自动实例、语义、LiDAR），并可处理数百万基元的大规模场景，处理时间仅需数秒。
- 实验验证：在 DesktopObjects-360 上达到 92.35% mIoU，在 NeRDS-360 上达到 95.89%，在完整 ScanNet-v2 验证集上使用提供的二维语义标注达到 65.77% mIoU。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法统一了二维掩码到三维标签迁移的流程，无需训练三维分割网络，在多个基准上取得较高精度，并支持多种任务类型和大规模场景，对视觉与三维场景理解交叉领域有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Modern image models provide strong cues about \emph{what} should be segmented in each view, but their masks do not by themselves determine \emph{where} those labels should persist in 3D. We present Cross-Domain Segmentation via Gaussian Splatting (CDSeg), a label-transfer interface that requires no task-specific 3D segmentation training and uses Gaussian primitives as a renderable label carrier. An external mask source supplies the labels, while renderer-derived visibility determines which 3D primitives receive them. The carrier is instantiated either by completing each input point into one Gaussian, preserving its index, or by reusing the native primitives of an optimized Gaussian scene. CDSeg records pixel--primitive associations during rendering and fuses multi-view masks through voting and a local filter. The resulting labels can be returned to the original points, retained on the native Gaussian scene, or rendered into other views. CDSeg covers promptable, automatic instance, semantic, and LiDAR settings and processes scenes with millions of primitives in seconds. It obtains 92.35\% mIoU on DesktopObjects-360, 95.89\% on NeRDS-360, and 65.77\% on the full ScanNet-v2 validation split using the provided 2D semantic annotations. CDSeg thereby provides one interface for reusing 2D masks across point clouds, Gaussian scenes, and image views without a task-specific 3D segmentation network.

</details>

#### 2026-08-05 - Objects as Audio-Visual Modal Sound Fields

**Authors:** Zisen Shao, Zihao Wei, Derong Jin, Ruohan Gao
**Links:** [abs](https://arxiv.org/abs/2608.05145) - [pdf](https://arxiv.org/pdf/2608.05145)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Objects as Audio-Visual Modal Sound Fields
- 作者：Zisen Shao, Zihao Wei, Derong Jin, Ruohan Gao
- 出版日期：2026-08-05
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.05145

### 一句话总结
本文提出一种基于多视角图像和少量冲击声音录音的对象级声学表示方法（AV-MSF），利用3D高斯溅射与模态参数实现少样本冲击声音渲染。

### 研究问题
如何在不依赖昂贵物理仿真或大规模数据集的情况下，从视觉与少量声音样本中重建对象冲击声音场，以补充3D重建中缺失的声学信息。

### 核心思路/方法
- 构建对象级“视听模态声场”（AV-MSF）表示。
- 基于3D高斯溅射（3D Gaussian Splatting），并集成密集3D视觉特征作为几何感知先验。
- 使用紧凑且物理上有意义的模态参数表示冲击声场，以实现鲁棒的少样本重建。
- 输入仅需多视角图像和少量冲击声音录音。

### 主要贡献
- 提出AV-MSF，一种新的对象级声学表示，可从多视角图像和少量冲击录音中重建。
- 结合3D高斯溅射与密集3D视觉特征，提供强几何先验。
- 在两个真实世界数据集上达到最先进的冲击声音渲染效果，优于基于物理仿真和数据驱动的基线方法。
- 展示了表示带来的下游应用：接触定位和对象声音编辑。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向视听学交叉的3D场景重建与声学渲染，方法新颖且实验上有明确优势，适合相关方向研究者参考；但若读者主要关注纯视觉重建或传统音频建模，可能相关性较低。摘要未提供算法复杂度或实时性等细节，故优先级定为中。

</details>

<details>
<summary>Abstract</summary>

While modern 3D reconstruction excels at modeling object geometry and appearance, it largely ignores the rich acoustic cues revealed through physical interaction. Object impact sounds convey material, stiffness, and structural properties that complement vision, yet existing impact sound modeling approaches either rely on expensive physics-based simulation or require large datasets to generalize in a purely data-driven manner. We introduce Audio-Visual Modal Sound Field (AV-MSF), a novel object-level acoustic representation reconstructed from multi-view images and only a few impact sound recordings. AV-MSF builds on 3D Gaussian Splatting integrated with dense 3D visual feature to provide a strong geometry-aware prior, and represents the impact sound field using compact, physically meaningful modal parameters, enabling robust few-shot reconstruction. Experiments on two real-world datasets show that AV-MSF achieves state-of-the-art impact sound rendering, outperforming both physics-based and data-driven baselines. Furthermore, we demonstrate downstream applications enabled by our representation, including contact localization and object sound editing.

</details>

#### 2026-08-05 - RORA: Realistic Object Reconstruction with Articulation

**Authors:** Hyesung Lee, Youngseon Lee, Kyutae Lee, Dongjun Lee, Yongseok Lee
**Links:** [abs](https://arxiv.org/abs/2608.04842) - [pdf](https://arxiv.org/pdf/2608.04842)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RORA: Realistic Object Reconstruction with Articulation
- 作者：Hyesung Lee, Youngseon Lee, Kyutae Lee, Dongjun Lee, Yongseok Lee
- 出版日期：2026-08-05
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.04842

### 一句话总结
本文提出首个从单段静态物体视频输入、通过人机交互建议流程端到端重建带准确关节运动、且可直接用于仿真与机器人学习的物体资产管道。

### 研究问题
如何从单个静态物体视频中，重建具备准确关节结构（articulation）且可仿真就绪（simulation-ready）的物体资产，以克服现有方法在复杂多关节结构上成功率低、且需要动态运动扫描的重建流程复杂问题。

### 核心思路/方法
- 采用人机交互（human-in-the-loop）的端到端管道，以建议（suggestion）方式引导用户完成关节资产重建。
- 重建输出为混合表示：结合3D Gaussian Splatting（3DGS）用于逼真渲染，与基于网格（mesh）的几何用于物理交互。
- 流程步骤：先进行凸分解（convex decomposition），再由用户分组实现直观的部件分割；随后将3D高斯绑定到对应网格部件上。
- 提出自动关节建议算法（Automatic Joint Suggestion Algorithm），从局部边界几何计算候选关节轴，呈现给用户以供高效确认。

### 主要贡献
- 首次提出从单一静态视频输入重建带准确关节结构的仿真就绪资产的端到端管道。
- 设计混合表示（3DGS + 网格），同时支持高保真渲染与物理交互。
- 提出自动关节建议算法，降低人工标注关节的复杂度。
- 在PartNet-Mobility-v0数据集和真实物体上验证了关节重建精度；并在Unreal Engine与NVIDIA Isaac Sim中展示了用于机器人灵巧手操作任务的潜力。

### 局限性
摘要未提供足够信息，如方法对复杂关节类型的具体精度数值、失败案例分析、对输入视频长度/质量的要求、以及人机交互环节的时间成本等均未说明。

### 阅读优先级
**高**。理由：该工作将神经渲染（3DGS）与结构化关节重建结合，直接面向机器人仿真与sim-to-real问题，且提出了首个单视频端到端关节重建管道，对具身智能与神经场景表示领域均有较强参考价值；同时展示在真实仿真平台（Isaac Sim）上的应用，实用性突出。

</details>

<details>
<summary>Abstract</summary>

Replicating real-world environments into simulation by realistic visual representation like NeRF and 3D Gaussian Splatting (3DGS) has emerged as an effective strategy to reduce the sim-to-real gap in robot learning. However, implementing object articulation during the real-to-sim process is still a challenging task. Existing motion tracking or learning based articulation methods shows low success rates on complex kinematic structures having multiple joints. Furthermore, those methods require scan of dynamic motion of objects, which makes reconstruction process much complicated. In this work, we propose the first end-to-end pipeline that reconstructs simulation-ready assets with accurate articulation from a single static object video input through suggestion based human-in-the-loop process. Our approach exports a hybrid representation combining 3DGS for photorealistic rendering and mesh-based geometry for physical interaction. In the reconstruction process, our pipeline performs convex decomposition followed by user grouping for intuitive part segmentation, subsequently binding 3D Gaussians to the corresponding mesh parts. An Automatic Joint Suggestion Algorithm then calculates candidate joint axes from local boundary geometries and presents them to users for efficient articulated asset reconstruction. We have shown that our method achieves precise articulation results on partnet-mobility-v0 dataset and real objects. Additionally we presented a potential usage of our framework on robot learning, deploying the reconstructed assets in Unreal Engine and NVIDIA Isaac Sim, demonstrating real-time dexterous hand manipulation tasks.

</details>

#### 2026-08-05 - UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models

**Authors:** Haiyang Zhou, Wangbo Yu, Chaoran Feng, Xunyu Zhou, Yonghong Tian, Li Yuan
**Links:** [abs](https://arxiv.org/abs/2608.04701) - [pdf](https://arxiv.org/pdf/2608.04701)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models
- 作者：Haiyang Zhou, Wangbo Yu, Chaoran Feng, Xunyu Zhou, Yonghong Tian, Li Yuan
- 出版日期：2026-08-05
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.04701

### 一句话总结
UniWorld-View 是一个通过结合显式3D几何引导与视频扩散模型，实现从单目输入生成大基线新视角的统一框架。

### 研究问题
如何在输入覆盖极其稀疏（大基线、极端相机运动）的条件下，生成照片级真实且几何一致的新视角，同时保持精确的相机控制。

### 核心思路/方法
- 将显式3D引导与生成式扩散建模集成到一个统一框架中，实现精确相机控制和几何一致的视图生成。
- 通过一种遮挡感知的点云渲染策略获得几何引导，该策略解决可见性歧义，为基于扩散的合成提供准确先验。
- 将该渲染策略与强大的视频扩散骨干网络耦合，支持大基线和宽基线变化下的高保真新视图生成，并可进一步输出多视图视频用于下游动态3DGS重建。

### 主要贡献
- 提出UniWorld-View，一个面向单目输入的可控大基线新视图合成统一框架。
- 设计遮挡感知点云渲染策略，显式处理遮挡并提供准确的几何先验。
- 在WorldScore基准和零样本NVS基准上的实验表明，该方法在可控性、几何一致性和视觉保真度方面有效。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对稀疏输入下大基线新视图合成这一具有挑战性的实际问题，结合显式3D引导与扩散生成模型，方法新颖且实验验证了有效性，对神经场景表示与渲染、生成式视图合成方向有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

The abundance of casually captured monocular videos and images on social media provides a valuable source for immersive content creation, where generating novel views from such sparse observations can greatly enhance user experiences. However, producing photorealistic and geometrically consistent views with precise camera control remains challenging when input coverage is extremely limited. Reconstruction-based approaches such as NeRF and 3D Gaussian Splatting (3DGS) deteriorate severely under sparse inputs and fail to explicitly handle occlusions. Generative methods ease data requirements but still struggle with large-baseline view synthesis due to inaccurate or implicit geometric guidance. To overcome these limitations, we introduce UniWorld-View, a unified framework for controllable large-baseline novel view synthesis from monocular inputs. UniWorld-View integrates explicit 3D guidance with generative diffusion modeling to enable precise camera control and geometrically consistent view generation. The geometric guidance is obtained through an occlusion-aware point cloud rendering strategy that resolves visibility ambiguities and provides accurate priors for diffusion-based synthesis. By coupling this rendering strategy with powerful video diffusion backbones, UniWorld-View achieves high-fidelity novel view generation even under extreme camera motions and wide-baseline changes, and can further provide multi-view videos for downstream dynamic 3DGS reconstruction. Experiments on the WorldScore benchmark and zero-shot NVS benchmarks demonstrate the effectiveness of UniWorld-View in controllability, geometric consistency, and visual fidelity.

</details>

#### 2026-08-05 - ACA-GS: Adaptive-Capacity Anchored Gaussian Splatting for Compact Dynamic Radiance Fields

**Authors:** Seunghyeon Song, Joo Chan Lee, Chanung Park, Jun Young Jeong, Minseo Lee, Eunbyung Park, Jong Hwan Ko
**Links:** [abs](https://arxiv.org/abs/2608.04581) - [pdf](https://arxiv.org/pdf/2608.04581)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ACA-GS: Adaptive-Capacity Anchored Gaussian Splatting for Compact Dynamic Radiance Fields
- 作者：Seunghyeon Song, Joo Chan Lee, Chanung Park, Jun Young Jeong, Minseo Lee, Eunbyung Park, Jong Hwan Ko
- 出版日期：2026-08-05T08:47:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.04581

### 一句话总结
本文提出一种自适应容量的锚点式4D高斯泼溅框架，根据局部时空复杂度动态分配神经高斯数量与特征通道，在保持渲染质量的同时显著提升存储压缩率。

### 研究问题
现有的锚点式4D高斯泼溅方法采用刚性均匀参数化，即每个锚点固定神经高斯数量和特征预算，导致为实现足够保真度而过度增加锚点密度，造成内存浪费。核心问题是如何在不牺牲视觉质量的前提下，更高效地分配表示容量以实现紧凑的动态辐射场。

### 核心思路/方法
该方法包含两个并行的自适应机制：
1. **自适应锚点基数（Adaptive Anchor Cardinality）**：动态调整每个锚点对应的神经高斯数量，在几何或运动复杂度高的区域集中更多图元，同时抑制冗余图元。
2. **自适应锚点特征掩蔽（Adaptive Anchor Feature Masking）**：调制锚点级别的特征通道，为复杂区域分配丰富特征，为简单区域分配轻量表示。

两者共同根据局部时空需求灵活分配表示容量，替代固定的均匀参数化。

### 主要贡献
- 提出自适应容量的锚点式框架，突破固定参数化限制，动态分配神经高斯数量与特征容量。
- 在MPEG、Panoptic Sports和N3DV数据集上验证了存储压缩的有效性，且不损失视觉质量。
- 在具有复杂运动的挑战性MPEG序列上，压缩率比最先进的锚点式方法最高提升1.5倍，同时保持可比的视觉质量水平。

### 局限性
摘要未提供足够信息，未涉及方法在极端复杂场景下的性能边界、计算开销变化或与其他非锚点式方法的对比细节。

### 阅读优先级
**高**。理由：针对4D高斯泼溅的存储效率这一关键瓶颈，提出自适应容量分配方案，并在复杂运动场景下取得显著压缩提升（最高1.5倍），对动态场景渲染和压缩领域有实用价值；且发表在视觉表示与渲染方向，实验结果来自多个公开数据集，可信度较高。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 4D Gaussian Splatting (4DGS) enable high-fidelity, real-time spatiotemporal rendering, but expose a fundamental trade-off between motion expressiveness and storage efficiency. While anchor-based designs achieve compactness through anchor-level parameter sharing, their rigid uniform parametrization enforces fixed Neural Gaussian counts and feature budgets per anchor. Consequently, insufficient fidelity is addressed by excessive anchor density, rather than lightweight, targeted increases in Neural Gaussian count or feature capacity, resulting in memory waste. To overcome this rigidity, we introduce an adaptive-capacity anchor-based framework that dynamically allocates the representational capacity based on local spatiotemporal demands. Adaptive Anchor Cardinality varies the number of Neural Gaussians per anchor, concentrating primitives in regions of high geometric or motion complexity while suppressing redundancy. In parallel, Adaptive Anchor Feature Masking modulates anchor-level feature channels, assigning rich features to complex regions and lightweight representations to simpler ones. Experiments on MPEG, Panoptic Sports, and N3DV datasets demonstrate substantial storage reduction without degrading visual quality. Notably, on challenging MPEG sequences with complex motion, our method achieves up to 1.5x higher compression than state-of-the-art anchor-based methods while preserving comparable quality.

</details>

#### 2026-08-05 - OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes

**Authors:** Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen
**Links:** [abs](https://arxiv.org/abs/2608.04560) - [pdf](https://arxiv.org/pdf/2608.04560)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes
- 作者：Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen
- 出版日期：2026-08-05T07:54:22Z
- 分类：Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.04560

### 一句话总结
本文提出面向无人机户外场景的3D语言高斯泼溅方法OutLangSplat，通过双分支特征表示与训练无关的聚合策略，解决遮挡和远距离视角下的语义激活错误问题，并提供了首个面向无人机户外场景的开放词汇3D场景理解数据集。

### 研究问题
现有3D语言高斯泼溅方法在室内或小规模场景有效，但在无人机户外场景中，严重遮挡与远距离视角常导致错误的语义激活和缺失的目标响应，如何提升此类场景下的开放词汇语义理解能力是核心问题。

### 核心思路/方法
- **特征表示**：设计2D-3D双分支表示，通过区域级对齐与融合提升空间一致性，减少目标响应不完整和背景误激活。
- **特征聚合**：提出免训练的贡献与一致性感知聚合策略，利用像素贡献可靠性与跨视角语义一致性，抑制来自嘈杂视角的不可靠响应。
- **数据集构建**：在四个真实公开无人机户外场景数据集上，手动标注多种物体，提供首个开放词汇3D场景理解的无人机户外数据集。

### 主要贡献
- 提出OutLangSplat，将语言高斯表示适配到无人机户外场景，改善特征表示与聚合可靠性。
- 设计2D-3D双分支表示及区域级对齐融合机制。
- 引入免训练的贡献与一致性感知高斯特征聚合策略。
- 首次提供可公开获取的无人机户外开放词汇3D场景理解数据集（包含四个真实场景数据的手动标注）。
- 在开放词汇语义分割与实例定位任务上超越现有最优方法（定量评估与消融实验支持）。

### 局限性
摘要未提供足够信息。未提及具体失败案例、计算开销、对极端天气/光照的鲁棒性，也未说明标注数据的规模、类别数量及标注质量评估等细节。

### 阅读优先级
**高**。理由：该工作针对无人机户外场景这一实际应用需求，提出新的表示与聚合方法，并开源首个相关数据集，对场景理解、机器人/AR应用有直接参考价值；方法创新点明确且有定量结果支持。

</details>

<details>
<summary>Abstract</summary>

3D Language Gaussian Splatting embeds open-vocabulary language features into 3D Gaussian Splatting, providing an efficient explicit representation for text-driven 3D scene understanding. However, existing methods are limited to indoor or small-scale scenes, and tend to fail in Unmanned Aerial Vehicle (UAV) outdoor scenes, where severe occlusions and long distance viewpoints often lead to incorrect semantic activations and missing target responses. In this paper, we present OutLangSplat which adapts language Gaussian representations to UAV outdoor scenes by improving feature representation and aggregation reliability. For the feature representation, a 2D-3D dual-branch representation with region-based alignment and fusion is designed to improve spatial consistency, reducing incomplete target responses and background misactivations. For the feature aggregation, we introduce a training-free contribution and consistency-aware Gaussian feature aggregation strategy that leverages pixel contribution reliability and cross-view semantic consistency to suppress unreliable responses from noisy viewpoints. A new dataset is provided by manually annotating various objects on four real-world public UAV outdoor scene datasets. To the best of our knowledge, it is the first accessible dataset of open-vocabulary 3D scene understanding for UAV outdoor scenes. Quantitative evaluations and ablation studies demonstrate that OutLangSplat outperforms SOTA methods on both open-vocabulary semantic segmentation and instance localization tasks. The datasets and codes will be open-sourced.

</details>

#### 2026-08-04 - 3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment

**Authors:** Yuke Xing, Jiarui Wang, William Gordon, Zhu Li, Guangtao Zhai, Yiling Xu
**Links:** [abs](https://arxiv.org/abs/2608.03279) - [pdf](https://arxiv.org/pdf/2608.03279)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment
- 作者：Yuke Xing, Jiarui Wang, William Gordon, Zhu Li, Guangtao Zhai, Yiling Xu
- 出版日期：2026-08-04
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.03279

### 一句话总结
本文提出面向压缩3D高斯泼溅（3DGS）图像质量评估的大规模多维数据集3DGS-IEval-15K+，并基于大多模态模型（LMM）构建了能够同时预测整体、几何与颜色三个质量维度的统一评估框架3DGSI-Assessor。

### 研究问题
现有图像质量评估（IQA）指标无法有效捕捉3DGS训练与压缩过程中引入的表示特有失真（如浮动伪影、表面散射），且几何与颜色属性的独立压缩产生解耦的分维度失真，而现有指标仅输出单一总分，缺乏针对3DGS压缩场景的多维度质量评估方法及配套数据集。

### 核心思路/方法
- 构建大规模多维IQA数据集3DGS-IEval-15K+：包含10个场景、15,200张图像，由6种代表性3DGS算法在系统设计的压缩级别下生成，从20个策略性选择的视角（含训练视角与挑战性新视角）渲染，带有45,600个平均意见分数（MOS），覆盖整体、几何、颜色三个质量维度。
- 提出3DGSI-Assessor框架：在大型多模态模型（LMM）中集成全局语义特征与分维度局部特征，通过单次前向传播同时预测整体、几何和颜色三个质量分数。

### 主要贡献
- 发布了首个面向压缩3DGS的大规模多维度IQA数据集3DGS-IEval-15K+，包含多算法、多压缩级别、多视角的精细标注。
- 提出3DGSI-Assessor，一个基于LMM的统一3DGS图像质量评估框架，可同时预测三个质量维度。
- 在3DGS-IEval-15K+上达到最先进性能，并在其他新视角合成（NVS）基准上展现出有竞争力的泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作填补了压缩3DGS场景下多维度图像质量评估数据集与方法的空白，提出的数据集规模大（15K+图像、45K+分数）且覆盖多算法与多视角，同时采用LMM架构进行多维度联合预测，对3DGS压缩与渲染质量评估方向具有较强的实用价值和参考意义，尤其适合从事3D表示学习、压缩和感知质量评估研究的人员阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become a dominant representation for real-time novel view synthesis (NVS), yet its storage footprint makes compression indispensable for practical deployment. 3DGS training and compression introduce representation-specific distortions such as floating artifacts and surface scattering, which conventional image quality assessment (IQA) metrics fail to capture. Moreover, the independent compression of geometric and color attributes may lead to decoupled dimension-specific distortions that must be diagnosed separately, yet existing metrics report only a single overall score. To address these gaps, we present 3DGS-IEval-15K+, a large-scale, multi-dimensional IQA dataset for compressed 3DGS, comprising 15,200 images from 10 diverse scenes, produced by 6 representative 3DGS algorithms at systematically designed compression levels and rendered from 20 strategically selected viewpoints spanning both training views and challenging novel views, annotated with 45,600 mean opinion scores (MOSs) across overall, geometry, and color quality. Based on 3DGS-IEval-15K+, we propose 3DGSI-Assessor, an all-in-one 3DGS IQA framework that integrates global semantic and dimension-specific local features within a large multimodal model (LMM), predicting all three dimensions in a single forward pass. 3DGSI-Assessor achieves state-of-the-art performance on 3DGS-IEval-15K+, and exhibits competitive generalization on other NVS benchmarks. Dataset and code will be released at https://github.com/YukeXing/3DGSI-Assessor.

</details>

#### 2026-08-04 - Bridging Online and Offline Handwriting via Differentiable Physical Rendering

**Authors:** Seonmi Park, Seunghyun Shin, Vihaan Misra, Dongmin Shin, Ukcheol Shin, Jean Oh, Hae-Gon Jeon
**Links:** [abs](https://arxiv.org/abs/2608.03198) - [pdf](https://arxiv.org/pdf/2608.03198)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Bridging Online and Offline Handwriting via Differentiable Physical Rendering
- 作者：Seonmi Park, Seunghyun Shin, Vihaan Misra, Dongmin Shin, Ukcheol Shin, Jean Oh, Hae-Gon Jeon
- 出版日期：2026-08-04T06:39:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.03198

### 一句话总结
本文提出一个通过可微分物理渲染模块统一在线笔迹轨迹生成与离线笔迹图像合成的手写生成框架，兼顾结构动力学与视觉外观。

### 研究问题
如何统一在线手写轨迹生成与离线手写图像合成两个独立范式，即同时获取笔迹的运动结构（轨迹与笔顺）和像素级真实外观，并克服缺乏物理模型与配对轨迹-图像数据集的挑战。

### 核心思路/方法
提出一个紧凑的物理画笔模型连接笔画动力学与视觉外观，并开发一个可微分渲染模块将笔画轨迹转换为风格化图像。整体框架包含四个核心模块：
1. 文本到笔画生成器：根据给定文本和风格图像预测目标笔画；
2. 画笔参数观测器：从风格参考中提取画笔模型参数；
3. 可微分画笔渲染器：将笔画序列和物理画笔参数映射为手写图像；
4. 零样本图像精化器：通过扩散模型细化和精化渲染图像。

### 主要贡献
1. 提出一个物理画笔模型，桥接笔迹运动学与像素级外观；
2. 设计可微分渲染模块，支持运动域与外观域之间的端到端学习；
3. 构建统一在线-离线手写生成框架，整合四个核心模块；
4. 通过广泛实验和真实机器人书法演示验证方法在结构与视觉保真度上的效果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作提出了一个从物理模型到可微分渲染再到扩散精化的完整统一框架，同时解决了在线与离线手写生成之间的核心挑战（物理建模与配对数据缺失），并进行了真实机器人书法验证，方向新颖且应用价值高，适合对生成模型、神经渲染和手写合成感兴趣的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Realistic handwritten text generation plays an important role in numerous applications, such as font design, biometric authentication, and robotic calligraphy. Existing methods are typically divided into two independent paradigms: online approaches that estimate handwriting trajectories and offline approaches that synthesize realistic handwriting images. While online models capture structural and temporal dynamics, they often lack fine-grained textures, whereas offline models reproduce realistic appearance but discard stroke order. However, unifying online and offline models remains challenging due to (1) the lack of an explicit physical model linking stroke kinematics to pixel-level appearance and (2) the absence of paired trajectory-image datasets. Moreover, enabling end-to-end learning requires a differentiable rendering process across motion and appearance domains. To address these challenges, we propose a compact physical brush model that bridges stroke dynamics and visual appearance, together with a differentiable rendering module that converts stroke trajectories into stylized images. By integrating these components, we propose a unified online-offline handwriting generation framework via differentiable brush rendering. The proposed framework consists of four core modules: 1) a text-to-stroke generator that predicts the target stroke conditioned on the given text and style image, 2) a brush parameter observer that extracts brush model parameters from style references, 3) a differentiable brush renderer that maps a stroke sequence and physical brush parameters into a handwritten image, and 4) a zero-shot image refiner that refines rendered images via diffusion models. Extensive experiments and real-world robotic calligraphy demonstrations validate our approach, achieving both structural and visual fidelity.

</details>

#### 2026-08-03 - InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthesis

**Authors:** Jiawei Wang, Hao Yu, Yongzhen Hu, Xinyi Yang, Tao Ni, Xin Zhan, Junbo Chen, Xiaowei Zhou, Ruizhen Hu, Sida Peng
**Links:** [abs](https://arxiv.org/abs/2608.02437) - [pdf](https://arxiv.org/pdf/2608.02437)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, view synthesis, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthesis
- 作者：Jiawei Wang, Hao Yu, Yongzhen Hu, Xinyi Yang, Tao Ni, Xin Zhan, Junbo Chen, Xiaowei Zhou, Ruizhen Hu, Sida Peng
- 出版日期：2026-08-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02437

### 一句话总结
InfiniSplat 提出一种从像素对齐转向表面对齐的单图前馈 3D 高斯泼溅框架，通过几何引导采样和隐式解码器提升大基线视角合成下的结构一致性。

### 研究问题
现有单图像前馈 3DGS 方法依赖像素对齐表示，即从固定图像网格位置预测高斯原语，导致高斯与场景表面耦合弱，在大视角偏移下难以保持连贯结构，限制了跨视角新视角合成质量。

### 核心思路/方法
1. **表面对齐表示**：抛弃固定像素网格的高斯预测方式，改为根据深度诱导的局部表面结构进行几何引导采样，放置 2D 支撑点。
2. **隐式解码器**：使用查询条件隐式解码器，从这些支撑点处的图像特征预测高斯属性，将高斯预测与固定像素中心解耦。
3. **训练与泛化**：在 Hypersim 合成数据训练，测试时零样本迁移到开放世界复杂场景。

### 主要贡献
- 提出从像素对齐到表面对齐的表示转变，改善高斯布局对场景表面的贴合度，减少网格离散化导致的散射原语。
- 在多个跨数据集新视角合成评估中，相比单图前馈基线达到最先进性能。
- 验证了从合成室内（Hypersim）训练到开放世界场景的零样本泛化能力。

### 局限性
摘要未提供足够信息（未提及计算开销、推理速度、对深度估计误差的敏感性、多物体或遮挡场景的详细表现等局限性）。

### 阅读优先级
**高**  
理由：该工作针对单图前馈 3DGS 的像素对齐瓶颈提出明确替代方案，且跨数据集实验显示性能领先和零样本泛化，对神经场景表示与渲染方向研究者具有直接参考价值；方法设计（几何引导采样+隐式解码）具有可复现启发意义。

</details>

<details>
<summary>Abstract</summary>

Single-image feed-forward 3D Gaussian Splatting (3DGS) aims to directly generate a renderable 3D scene representation from one input image, avoiding the cost of multi-view capture and per-scene optimization. However, existing methods are often constrained by a pixel-aligned representation, where Gaussians are predicted from fixed image-grid locations. Such pixel-aligned primitives can produce promising nearby-view renderings, but they remain weakly coupled to underlying scene surfaces and struggle to preserve coherent structures under large viewpoint shifts. We present InfiniSplat, a feed-forward single-image 3DGS framework that moves from a pixel-aligned representation toward a surface-aligned representation. InfiniSplat constructs this representation by first using geometry-guided sampling to place 2D supports according to depth-induced local surface structure, and then applying a query-conditioned implicit decoder to predict Gaussian attributes from the image features queried at these supports. By grounding support locations in geometry while decoupling Gaussian prediction from fixed pixel centers, InfiniSplat produces Gaussian layouts that better follow scene surfaces and reduce scattered primitives caused by grid discretization. Across multiple cross-dataset NVS evaluations, InfiniSplat achieves state-of-the-art performance compared with single-image feed-forward baselines, and demonstrates zero-shot generalization from Hypersim indoor synthetic training to complex open-world scenes. Project page: https://zju3dv.github.io/InfiniSplat.

</details>

#### 2026-08-03 - CLEAR: Conflict-aware Learning via Evidence-guided Adaptive Routing for Unified Sparse-View 3D Gaussian Super-Resolution

**Authors:** Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan
**Links:** [abs](https://arxiv.org/abs/2608.02206) - [pdf](https://arxiv.org/pdf/2608.02206)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CLEAR: Conflict-aware Learning via Evidence-guided Adaptive Routing for Unified Sparse-View 3D Gaussian Super-Resolution
- 作者：Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan
- 出版日期：2026-08-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02206

### 一句话总结
CLEAR 提出首个统一单阶段稀疏视角 3D 高斯超分框架，通过冲突感知优化与证据引导路由机制，在单一高斯表示中联合优化低分辨率观测与高分辨率先验，显著提升渲染质量和几何保真度。

### 研究问题
稀疏视角 3D 高斯泼溅超分面临的核心挑战：稀疏且低分辨率的输入缺乏足够的几何与高频信息，现有两阶段管线（先低分辨率重建、再高分辨率细化）会引入阶段间高斯迁移与重建误差累积。论文旨在解决如何在一个统一框架中避免误差累积并同时恢复高频细节。

### 核心思路/方法
- 提出统一单阶段框架 CLEAR，在单个高斯表示中联合优化真实低分辨率观测与外部高分辨率先验。
- **高斯级冲突感知优化策略**：将低分辨率梯度视为可靠锚点，仅对严重高分辨率冲突施加基于证据条件的软校正，以缓解稀疏监督带来的梯度冲突。
- **证据引导的 Patch-to-Gaussian 路由机制**：估计 patch 可靠性与细节需求，将其提升至高斯空间，并选择性路由高频梯度与致密化操作。
- 采用共享高斯丢弃（shared Gaussian dropout）与分离的中途训练锚定（detached mid-training anchoring）增强训练鲁棒性。

### 主要贡献
- 首次提出稀疏视角 3D 高斯泼溅超分的统一单阶段框架，避免两阶段误差累积。
- 提出高斯级冲突感知优化策略，以低分辨率梯度为锚进行条件性软校正。
- 设计证据引导的 Patch-to-Gaussian 路由机制，针对性恢复高频细节。
- 在合成与真实世界 4× 超分基准上达到最先进渲染质量与几何保真度。

### 局限性
摘要未提供足够信息。具体局限性（如计算开销、对不同稀疏程度输入的敏感性、失败案例等）在摘要中未提及。

### 阅读优先级
**高**
理由：该工作面向稀疏视角 3D 超分这一活跃方向，提出单阶段统一框架替代传统两阶段管线，思路具有创新性；同时涉及冲突感知优化与证据引导路由等机制，对神经渲染与 3D 重建研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Sparse-view 3D Gaussian Splatting Super-resolution is highly challenging since the sparse and low-resolution (LR) inputs lack sufficient geometric and high-frequency information for accurate reconstruction. To achieve high-quality reconstruction, existing sparse-view super-resolution methods adhere to two-stage pipeline that performs LR Gaussian reconstruction and then high-resolution (HR) Gaussian refinement, which directly results in stage-wise Gaussian transfer and reconstruction error accumulation. To this end, we propose CLEAR, a Conflict-aware Learning via Evidence-guided Adaptive Routing, as the first unified single-stage framework for Sparse-view 3D Gaussian Splatting Super-resolution. Specifically, CLEAR performs joint the optimization of authentic LR observations and external HR priors within a unified Gaussian representation. To mitigate the gradient conflicts introduced by sparse supervision during training, we propose a Gaussian-wise conflict-aware optimization strategy that regards the LR gradient as a reliable anchor and applies evidence-conditioned soft correction only to severe HR conflicts. Moreover, to recover high-frequency details, we introduce an evidence-guided Patch-to-Gaussian routing mechanism which estimates patch reliability and detail demand, lifts them into Gaussian space, and selectively routes high-frequency gradients and densification. Finally, we employ shared Gaussian dropout and a detached mid-training anchoring to enhance the robustness of training framework. Extensive experiments on both synthetic and real-world $4\times$ super-resolution benchmarks demonstrate that CLEAR consistently achieves state-of-the-art rendering quality and superior geometric fidelity.

</details>

#### 2026-08-03 - DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views

**Authors:** Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen
**Links:** [abs](https://arxiv.org/abs/2608.02191) - [pdf](https://arxiv.org/pdf/2608.02191)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting, embodied AI, autonomous driving, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views
- 作者：Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen
- 出版日期：2026-08-03
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.02191

### 一句话总结
DerainSplat 提出了一种前馈式 3D 高斯泼溅框架，能够仅从少量雨景视角直接重建干净的 3D 场景，并通过预测天气因子实现去雨与几何增强。

### 研究问题
如何从稀疏的雨景多视图输入中，以前馈方式重建干净的 3D 场景，以解决现有前馈 3DGS 方法在雨景条件下性能崩溃的问题。

### 核心思路/方法
- 构建大规模多视角去雨数据集：通过四阶段合成流程依次建模阴天光照、深度相关雾霾、雨条纹和镜头雨滴，生成带特权天气因子的数据。
- 引入天气网络：从雨景上下文中预测天气因子，并生成两种支持图（场景支持与辐射支持）。
- 场景支持：用于调制跨视图代价体匹配，增强几何估计。
- 辐射支持：用于驱动深度对齐的外观融合，填补被雨损坏的像素。
- 几何证据调节：利用推导出的几何证据衰减高斯不透明度，减少虚假结构。
- 雨景循环一致性：使用预测的天气因子重渲染干净视图，并与雨景输入对齐，形成自监督约束。

### 主要贡献
- 提出首个面向稀疏雨景输入的前馈式干净 3D 场景重建框架 DerainSplat。
- 构建了大规模多视角去雨数据集，包含分层天气建模的合成管线。
- 设计天气网络与双支持图机制，分别作用于几何匹配和外观融合。
- 引入雨景循环一致性损失，增强去雨重建的一致性。
- 在多个数据集（RealEstate10K、ACID、Mip-NeRF360）及真实雨景场景上验证了优于现有方法的表现，并具备跨数据集泛化能力。

### 局限性
摘要未提供足够信息。未提及具体失败场景、对极端雨况的鲁棒性边界、计算开销、实时性要求或对非雨景输入的退化表现等。

### 阅读优先级
**高**。理由：该工作针对空间智能应用（如具身 AI 和自动驾驶）中稀疏雨景 3D 重建这一关键痛点，提出了完整的前馈框架、数据集与自监督机制，兼具方法创新与实际应用价值，且跨数据集验证了泛化性，值得重点阅读。

</details>

<details>
<summary>Abstract</summary>

Although image deraining has advanced substantially, existing methods mainly focus on 2D image restoration. As spatial intelligence applications such as embodied AI and autonomous driving continue to emerge, reconstructing clean 3D scenes from sparse rainy views in a feed-forward manner becomes increasingly important. Existing feed-forward 3D Gaussian Splatting (3DGS) methods often assume clean inputs and collapse under rainy conditions. To this end, we present \textbf{\textit{DerainSplat}}, a feed-forward framework that reconstructs clean 3D scenes from only a few rainy views. To support this task, we build a large-scale multi-view derain dataset through a four-stage synthesis pipeline that sequentially models overcast illumination, depth-dependent haze, rain streaks, and lens raindrops, producing privileged weather factors. We introduce a weather net that predicts the weather factors from rainy context and yields two support maps. Scene support modulates cross-view cost-volume matching, while radiance support drives depth-aligned appearance fusion to fill corrupted pixels. The derived geometry evidence further attenuates Gaussian opacity to reduce spurious structures. A rainy cycle consistency re-renders clean views using the predicted factors and aligns them with rainy inputs. Extensive experiments show that \textbf{\textit{DerainSplat}} outperforms existing methods on various datasets, including RealEstate10K, ACID, Mip-NeRF360, and real-world rainy scenes, with strong cross-dataset generalization.

</details>

#### 2026-08-03 - GSRAIN: Physically Calibrated High-/Low-Frequency Rainfall Synthesis for 3D Gaussian Driving Scenes

**Authors:** Fanyu Wang, Longgao Zhang, Junyi Chen
**Links:** [abs](https://arxiv.org/abs/2608.02177) - [pdf](https://arxiv.org/pdf/2608.02177)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GSRAIN: Physically Calibrated High-/Low-Frequency Rainfall Synthesis for 3D Gaussian Driving Scenes
- 作者：Fanyu Wang, Longgao Zhang, Junyi Chen
- 出版日期：2026-08-03T12:57:44Z
- 分类：Neural Scene Representations & Rendering（次要：Embodied / Robotics / AR Applications）
- 链接：https://arxiv.org/abs/2608.02177

### 一句话总结
GSRAIN 提出一种基于 3D 高斯泼溅（3DGS）的高/低频降雨合成方法，通过融合物理校准的雨滴模型与扩散模型生成的雨景外观，实现对自动驾驶场景降雨强度的可控渲染。

### 研究问题
现有面向自动驾驶的降雨仿真方法在物理可控性和多视角一致性方面存在局限，缺乏能够支持可控降雨强度且与闭环测试兼容的场景生成手段。

### 核心思路/方法
- 构建高频雨滴模型：基于实测降雨数据生成高频雨滴效果。
- 生成低频降雨外观：使用几何感知的单步扩散模型生成低频雨景外观。
- 统一融合：将高、低频两种效果融合到统一的 3DGS 场景中，实现 0–13 mm/h 范围的降雨强度控制。

### 主要贡献
- 提出 GSRAIN 方法，实现物理校准的高/低频降雨合成，兼顾可控性与多视角一致性。
- 在 3DGS 驾驶场景中支持降雨强度的连续控制（0–13 mm/h）。
- 定量评估：FID 达到 149.09，优于 CycleGAN-Turbo（155.71）和 WeatherEdit（157.94）。
- 目标检测与闭环驾驶实验表明，生成的场景能暴露算法在可控降雨下的场景相关性能变化，证明其可用于构建物理可控、可重复且闭环兼容的雨景测试场景。

### 局限性
摘要未提供足够信息，未提及方法在极端降雨强度、真实感上限、计算开销、泛化到其他天气类型或场景外推等方面的局限性。

### 阅读优先级
**高**
理由：该工作针对自动驾驶仿真中的物理可控降雨生成问题，提出基于 3DGS 的新方法，在定量指标上优于现有方法，并验证了其在闭环测试中的实用性。对于从事神经场景渲染、自动驾驶仿真或鲁棒性测试的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing rainfall simulation methods for autonomous driving remain limited in physical controllability and multi-view consistency. This paper presents GSRAIN, a high-/low-frequency rainfall synthesis method for 3D Gaussian Splatting (3DGS) driving scenes. GSRAIN constructs a high-frequency raindrop model from measured rainfall data and generates low-frequency rainy appearance using a geometry-aware single-step diffusion model. The two effects are then fused in a unified 3DGS scene, enabling rainfall-intensity control over the range of 0--13~mm/h. The proposed method achieves a Fréchet Inception Distance (FID) of 149.09, outperforming CycleGAN-Turbo (155.71) and WeatherEdit (157.94). Object-detection and closed-loop driving experiments further show that the generated scenes expose scene-dependent performance changes of the evaluated algorithms under controllable rainfall. These results indicate that GSRAIN provides an effective approach for constructing physically controllable, repeatable, and closed-loop-compatible rainy-weather test scenes for autonomous driving.

</details>

#### 2026-08-03 - DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization

**Authors:** Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng
**Links:** [abs](https://arxiv.org/abs/2608.02099) - [pdf](https://arxiv.org/pdf/2608.02099)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization
- 作者：Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng
- 出版日期：2026-08-03T11:59:51Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.02099

### 一句话总结
DeGS提出一种解耦工作负载解析与重组的可扩展3DGS硬件架构，通过将传统渲染中耦合的检查与混合流程分离，显著提升并行处理单元利用率与吞吐量。

### 研究问题
现有3DGS加速器存在架构可扩展性差的问题：增加处理单元（PE）数量时渲染性能提升有限。根因是“边检查边混合”（checking-while-blending）的紧耦合数据流，导致不规则的Gaussian覆盖（空间冗余）和异步像素终止（时间冗余）下PE利用率低下。

### 核心思路/方法
- 将标准渲染过程中耦合的α检查、透射率检查和α混合操作解耦，重构为三个连续阶段：工作负载解析（parsing）、重组（reorganization）和混合（blending）。
- 在混合之前将碎片化、长度可变且依赖时序的工作负载重组为紧凑、无冲突且密集的工作负载，从而提高并行混合阶段的PE利用率。
- 在28nm工艺下实现，并与现有最先进加速器（GSCore、GBU、GCC）对比。

### 主要贡献
- 提出解耦数据流设计，系统性消除渲染固有的空间和时间冗余。
- 实现高可扩展性：从16扩展到1024个PE时，在高分辨率下维持超过80%的PE利用率。
- 在多样场景和分辨率（720p至8K）下，相比现有加速器获得2.36倍–7.25倍吞吐量、1.82倍–6.02倍端到端加速，以及1.59倍–4.42倍能效提升。

### 局限性
摘要未提供足够信息，例如具体功耗/面积开销、对不同场景类型的泛化失败案例、与传统GPU的对比结果等。

### 阅读优先级
**高**。理由：该工作直接针对3DGS硬件加速的核心可扩展性瓶颈，提出结构化的解耦方案，具有明确的性能与能效数据支撑，且覆盖从720p到8K的多种分辨率，对实时渲染和神经渲染硬件设计领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as a leading technique for real-time novel view synthesis, yet existing 3DGS accelerators suffer from poor architectural scalability: increasing the number of PEs leads to marginal performance improvement during rendering. We identify that the root cause is the tightly coupled ``checking-while-blending'' dataflow, which exacerbates PE underutilization caused by spatial redundancy from irregular Gaussian coverage and temporal redundancy from asynchronous pixel-wise termination under parallel execution. To address this issue, we propose DeGS, a scalable architecture for efficient 3DGS inference. To systematically eliminate the redundancies inherent in rendering, DeGS exploits a decoupled dataflow, restructuring the coupled $α$-checking, transmittance checking, and $α$-blending of the standard rendering process into consecutive workload parsing, reorganization, and blending stages. This allows the fragmented, length-variable, and temporal-dependent workloads to be reorganized into compact, conflict-free, and dense workloads prior to blending, thereby significantly improving PE utilization during parallel blending. Implemented in 28 nm technology, DeGS achieves 2.36$\times$--7.25$\times$ throughput, 1.82$\times$--6.02$\times$ end-to-end speedup, and 1.59$\times$--4.42$\times$ energy efficiency over state-of-the-art 3DGS accelerators (GSCore, GBU, GCC) across diverse scenes and resolutions (720p to 8K). Moreover, scaling from 16 to 1024 PEs, DeGS maintains over 80\% PE utilization at high resolutions, significantly outperforming existing accelerators.

</details>

#### 2026-08-03 - LiveLight: Real-time Streaming Video Relighting with Interactive Control

**Authors:** Yue Ma, Jiangming Wang, Yucheng Wang, Xilai Wang, Zhiyuan Li, Xinyu Wang, Hongyu Liu, Ruofan Liang, Songchun Zhang, Yuxuan Xue, Qifeng Chen
**Links:** [abs](https://arxiv.org/abs/2608.01771) - [pdf](https://arxiv.org/pdf/2608.01771)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic 3D, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LiveLight: Real-time Streaming Video Relighting with Interactive Control
- 作者：Yue Ma, Jiangming Wang, Yucheng Wang, Xilai Wang, Zhiyuan Li, Xinyu Wang, Hongyu Liu, Ruofan Liang, Songchun Zhang, Yuxuan Xue, Qifeng Chen
- 出版日期：2026-08-03T06:45:00Z
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：https://arxiv.org/abs/2608.01771

### 一句话总结
LiveLight 是首个基于扩散模型的实时流式视频重照明框架，支持交互式 3D 光照控制，在极低推理步数下实现高质量、时间稳定的重照明效果。

### 研究问题
如何构建一个既能实时处理流式视频、又支持交互式 3D 光照控制，同时保持高保真重照明质量的扩散模型框架？具体需要解决三个关键挑战：有效注入动态 3D 光照信息、在极低 NFE（函数评估次数）预算下维持生成质量以达成实时速度、以及支持任意长度视频的连续流式交互控制。

### 核心思路/方法
论文提出三项核心设计：
1. **光照注入**：设计一个轻量级适配器，将多平面光辐照度（MPLI）条件——即编码 3D 光照几何的深度感知辐照度图——直接送入扩散主干网络。
2. **低 NFE 质量保持**：引入几何引导反馈分支，在训练时使用冻结的几何估计器强制深度与法线一致的重照明，确保几何合理的着色效果，且不增加推理开销。
3. **流式交互**：开发渐进式滚动窗口策略，维护不同噪声水平的潜变量块去噪阶梯，通过传播中间状态保证时间一致性，支持任意长度视频重照明及逐帧参考刷新。

### 主要贡献
- 首次提出面向实时流式视频重照明的扩散框架，支持交互式 3D 光照控制。
- 提出轻量适配器实现 MPLI 条件的高效光照注入。
- 提出几何引导反馈分支，在极低 NFE 下保持几何一致的渲染质量。
- 设计渐进式滚动窗口策略，实现时间一致的无限长度流式重照明。
- 在真实与合成基准上达到最先进的重照明质量，同时实现实时速度；在时间稳定性、光照可控性和用户偏好上显著优于离线基线。
- 将公开模型、训练数据及合成数据生成器以促进相关研究。

### 局限性
摘要未提供足够信息，未讨论方法的失败案例、计算资源需求、对输入视频质量的依赖、光照控制的范围限制，或与其他方法的定量对比细节等潜在局限性。

### 阅读优先级
**高**。理由：该工作针对视频重照明这一活跃研究方向，首次将扩散模型、实时速度与交互式 3D 光照控制结合起来，具有较强的创新性和实用价值；同时作者计划开源模型与数据，便于复现和后续研究，值得高优先级关注。

</details>

<details>
<summary>Abstract</summary>

We present LiveLight, the first diffusion-based framework for real-time streaming video relighting with interactive 3D lighting control. Achieving this is non-trivial, as it requires overcoming three critical challenges: effectively injecting dynamic 3D lighting into a diffusion model, maintaining high-fidelity generation under an extremely low NFE (Number of Function Evaluations) budget for real-time speed, and facilitating continuous streaming for interactive control. To address these pain points, we propose three key designs. First, for accurate lighting injection, we propose a lightweight adapter that feeds Multi-Plane Light Irradiance (MPLI) conditions-depth-aware irradiance maps encoding 3D lighting geometry-directly into the diffusion backbone. Second, to prevent rendering quality degradation at low NFEs towards real-time distillation, we introduce a geometry-guided feedback branch. This training-time constraint leverages a frozen geometry estimator to enforce depth- and normal-consistent relighting, ensuring geometrically plausible shading without adding inference overhead. Finally, to enable streaming interaction, we develop a progressive rolling-window strategy that maintains a denoising ladder of latent chunks at varying noise levels. By propagating intermediate states, this strategy guarantees temporal coherence and supports arbitrarily long video relighting with per-frame reference refresh. Extensive experiments on real-world and synthetic benchmarks demonstrate that LiveLight achieves state-of-the-art relighting quality while running at real-time speed, significantly outperforming offline baselines in temporal stability, lighting controllability, and user preference. To foster real-time interactive relighting research, we will publicly release our models, training data, and synthetic data generator.

</details>

#### 2026-08-03 - DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing

**Authors:** Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi
**Links:** [abs](https://arxiv.org/abs/2608.01761) - [pdf](https://arxiv.org/pdf/2608.01761)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, relighting, rendering, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing
- 作者：Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi
- 出版日期：2026-08-03
- 分类：神经场景表示与渲染（主）；具身/机器人/AR应用（次）
- 链接：https://arxiv.org/abs/2608.01761

### 一句话总结
本文提出一种解耦式3D高斯泼溅（3DGS）框架，将大场景拆分为静态背景与可操控动态智能体，以支持端到端自动驾驶算法的高保真、可交互、实时的闭环测试。

### 研究问题
现有端到端自动驾驶测试环境（游戏引擎或静态神经渲染方法）难以同时兼顾高视觉保真度、强交互性与实时性能，尤其在动态场景组合方面存在不足，无法满足大规模闭环评估需求。

### 核心思路/方法
采用基于对象中心的规范表示（object-centric canonical representation），从根本上将场景分解为：
- 高保真静态背景；
- 可操控的动态智能体。

为解决分解带来的表征冲突，引入三个针对性模块：
1. **资产压缩**：通过感知剪枝和向量量化（vector quantization）实现实时交通渲染；
2. **地图引导的几何配准**：利用语义拓扑严格对齐轨迹；
3. **代理式重光照**：迁移环境光照以实现无缝的光度合成。

### 主要贡献
- 提出面向大规模端到端自动驾驶评估的解耦式3DGS框架；
- 设计三个模块解决静态背景与动态智能体分解后的表征冲突；
- 实验表明该方法在保真度与效率之间取得平衡，提升了指标一致性和光度一致性；
- 构建了实用的闭环传感器仿真平台，用于端到端自动驾驶评估。

### 局限性
摘要未提供足够信息。摘要未提及对极端天气、遮挡处理、大规模场景内存占用、计算资源需求等具体局限性，也未提供详细实验对比数据。

### 阅读优先级
**中**

理由：该工作面向自动驾驶闭环测试这一特定应用场景，技术上结合了3DGS、神经渲染与仿真，对相关领域研究者有一定参考价值。但摘要未提供足够定量实验细节，难以判断其相对既有方法的实际优势幅度，建议根据是否需要3DGS仿真框架来决定是否精读原文。

</details>

<details>
<summary>Abstract</summary>

End-to-end (E2E) autonomous driving algorithms require rigorous closed-loop validation in simulation environments offering high visual fidelity, strong interactivity, and real-time performance. Existing approaches, from game engines to static neural rendering, inherently trade off these requirements and struggle with the dynamic scene composition essential for E2E testing. To bridge this gap, we propose a novel decoupled 3D Gaussian Splatting (3DGS) framework tailored for large-scale E2E evaluation. We fundamentally decompose scenes into a high-fidelity static background and manipulable dynamic agents using an object-centric canonical representation. To resolve resulting representational conflicts, we introduce three targeted modules: (1) asset compression via perceptual pruning and vector quantization for real-time traffic rendering; (2) map-guided geometric registration leveraging semantic topology to strictly align trajectories; and (3) proxy-based relighting transferring ambient illumination for seamless photometric integration. Extensive experiments demonstrate that DecoupleGS achieves a balanced fidelity-efficiency trade-off, improves metric and photometric consistency, and provides a practical closed-loop sensor simulation platform for E2E autonomous driving evaluation.

</details>

#### 2026-08-03 - G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors

**Authors:** Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou
**Links:** [abs](https://arxiv.org/abs/2608.01726) - [pdf](https://arxiv.org/pdf/2608.01726)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors
- 作者：Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou
- 出版日期：2026-08-03（注：该日期异常，建议核实）
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01726

### 一句话总结
G-Skin 提出一种生成式蒙皮框架，利用2D视觉基础模型蒸馏运动先验作为伪引导，为3D高斯表示学习拓扑无关的蒙皮权重，实现高保真动画化。

### 研究问题
如何在没有高质量3D高斯蒙皮数据集的情况下，为任意骨架拓扑的3D高斯资产实现灵活且高保真的蒙皮绑定，同时克服前馈方法缺乏训练数据、以及基于网格迁移方法泛化性差的问题。

### 核心思路/方法
1. 利用骨架可控的图像生成模型，借助2D视觉基础模型，将强大的运动先验蒸馏为伪引导（pseudo-guidance），以缓解3D数据稀缺问题。
2. 在该伪引导下，设计包含几何感知正则化的优化管线，以稳定学习过程并确保蒙皮权重平滑且结构连贯。
3. 框架可灵活扩展到3D高斯表示的增强变体，用于缓解动画引起的渲染伪影。

### 主要贡献
- 提出G-Skin，一种面向3D高斯表示的新型生成式蒙皮框架，支持表达丰富、高保真的动画。
- 引入基于2D视觉基础模型的骨架可控图像生成方案，为解决3D蒙皮数据稀缺提供了新途径。
- 设计了结合几何感知正则化的优化流程，保证蒙皮权重的平滑性和结构一致性。
- 通过大量实验验证了方法有效性，并表明相对于现有最先进方法具有明显优势。

### 局限性
摘要未提供足够信息，无法得知该方法在极端拓扑、实时性能、多物体交互、以及蒙皮权重质量量化指标等方面的具体限制。

### 阅读优先级
**高**。理由：3D高斯泼溅是当前神经渲染与动态场景建模的热点方向，而蒙皮绑定是其动画化的关键瓶颈；该工作提出了一种绕开昂贵3D数据采集的生成式方案，思路新颖且声称超越现有方法，对从事3D内容生成与动画渲染的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has achieved remarkable success in photorealistic and efficient rendering, leading to a rapid increase in 3D assets represented by 3D Gaussian primitives. Directly rigging these assets with arbitrary skeleton topologies is highly desirable. However, training a feed-forward skinning framework is infeasible due to the lack of high-quality 3D Gaussian rigging datasets. An alternative solution is to transfer mesh-based techniques to 3D Gaussian-based representation, but 3D Gaussian primitives are not restricted to the surface and lack explicit topological connectivity. Moreover, this kind of method suffers from poor generalization to unseen data due to its strong dependence on training data, while acquiring high-quality rigging data is prohibitively expensive. To address this challenging problem, we propose G-Skin, a novel generative skinning framework designed for expressive and high-fidelity animation with 3D Gaussian representation. To overcome this 3D data scarcity, we introduce a skeleton-controllable image generation model leveraging 2D vision foundation models to distill powerful motion priors into pseudo-guidance. Guided by these priors, we formulate an optimization pipeline incorporating geometry-aware regularizations, which stabilizes the learning process and ensures smooth, structurally coherent skinning weights. G-Skin also generalizes flexibly to the augmented variants of 3D Gaussian representation designed to mitigate animation-induced rendering artifacts. Extensive experiments validate the effectiveness of our approach, demonstrating clear advantages over state-of-the-art methods. Project page: https://yaoyx689.github.io/GSkin.html.

</details>

#### 2026-08-03 - StreamSplat: Streaming Feed-Forward 3D Gaussian Splatting

**Authors:** Changhao Song, Yuxuan Wang, Qibiao Li, Youcheng Cai, Ligang Liu
**Links:** [abs](https://arxiv.org/abs/2608.01659) - [pdf](https://arxiv.org/pdf/2608.01659)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StreamSplat: Streaming Feed-Forward 3D Gaussian Splatting
- 作者：Changhao Song, Yuxuan Wang, Qibiao Li, Youcheng Cai, Ligang Liu
- 出版日期：2026-08-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01659

### 一句话总结
StreamSplat 提出了一种流式前馈 3D 高斯泼溅框架，通过体素对齐的因果缓存和几何锚定机制，实现在线顺序输入场景下的增量式新视角合成，并支持超长输入流。

### 研究问题
现有前馈 3D 高斯泼溅方法通常假设一组固定的上下文视图并联合处理，无法适应校准视图按顺序到达、场景需因果更新的在线场景；且固定视图方法在长输入流中会内存溢出。本文旨在解决流式环境下高效、稳定地进行新视角合成的问题。

### 核心思路/方法
- 提出 StreamSplat，一个流式前馈 3DGS 框架，增量维护一个持续的、基于几何的场景状态，并在每个输入块后解码为可渲染的 3D 高斯。
- 核心组件为 **Voxel-Aligned Causal Cache (VACC)**：在内存有界的体素结构中存储历史 3D token，使内存随探索的场景几何增长而非流长度增长。
- 引入 **History-Projected Depth Anchoring (HPDA)**：将缓存几何投影为当前代价体估计的深度引导。
- 引入 **Cache-Guided Feature Injection (CGFI)**：将缓存中的潜在证据注入高斯 token 回归过程。

### 主要贡献
- 提出首个面向流式输入的前馈 3DGS 框架，支持因果更新而不依赖未来视图或全场景上下文。
- 设计 VACC 缓存机制，使内存消耗与场景几何规模相关而非输入流长度。
- 通过 HPDA 和 CGFI 有效复用历史信息，实现在稀疏因果输入下与 SOTA 方法竞争力相当的性能。
- 在 DL3DV、RealEstate10K 和 ScanNet 上验证，能够扩展至 256、512、1024 视图的长流输入，且新视角质量随观测增多持续提升。

### 局限性
摘要未提供足够信息（如具体失败场景、计算开销、对高度动态场景的适用性、实际运行时效率等均未提及）。

### 阅读优先级
**高**
理由：该工作针对在线/流式新视角合成这一实际需求，解决了现有前馈 3DGS 方法无法处理长序列和因果更新的关键瓶颈；提出的缓存机制与几何锚定方法具有较强通用性，且实验覆盖多个数据集和超长输入规模，对从事实时三维重建、机器人感知、流媒体渲染等方向的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting enables efficient novel-view synthesis without per-scene optimization, but most existing methods assume a fixed set of context views and process them jointly. This limits their applicability to online scenarios where calibrated views arrive sequentially and the scene must be updated causally. We present \emph{StreamSplat}, a streaming feed-forward 3DGS framework that incrementally maintains a persistent geometry-grounded scene state and decodes it into renderable 3D Gaussians after each input chunk. StreamSplat centers on a \textbf{Voxel-Aligned Causal Cache (VACC)}, which stores historical 3D tokens in a memory-bounded voxel structure so that memory grows with explored scene geometry rather than stream length. To better reuse history during causal prediction, we introduce \textbf{History-Projected Depth Anchoring (HPDA)} to project cached geometry as depth guidance for current cost-volume estimation, and \textbf{Cache-Guided Feature Injection (CGFI)} to inject cached latent evidence into Gaussian-token regression. Experiments on DL3DV, RealEstate10K, and ScanNet show that StreamSplat remains competitive with state-of-the-art feed-forward 3DGS methods under sparse causal inputs, despite not using future views or full-scene context. More importantly, it scales to long input streams with 256, 512, and 1024 views where fixed-view baselines run out of memory, yielding sustained improvements in novel-view synthesis quality as more observations arrive. The code will be made publicly available upon acceptance.

</details>

#### 2026-08-02 - GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization

**Authors:** Baihan Yang, Tiexin Li, Yuheng Liu, Xin Lin, Xinke Li, Xiaohui Xie, Truong Nguyen
**Links:** [abs](https://arxiv.org/abs/2608.01492) - [pdf](https://arxiv.org/pdf/2608.01492)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization
- 作者：Baihan Yang, Tiexin Li, Yuheng Liu, Xin Lin, Xinke Li, Xiaohui Xie, Truong Nguyen
- 出版日期：2026-08-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.01492

### 一句话总结

提出一种无需训练的3D高斯泼溅交互式物体选择框架，利用稀疏视角和稀疏涂鸦，通过图优化实现轻量级的高质量物体分割。

### 研究问题

在3D场景编辑和具身交互中，如何以最小用户交互成本，从重建的3D高斯场景中准确选择完整物体，同时降低对密集视角和大量计算资源的依赖。

### 核心思路/方法

- 直接在原生3D高斯原语上操作，无需重新训练或标注嵌入。
- 将密集高斯体粗化为几何一致的超点，并利用外观和空间信息构建带连续性权重的图。
- 将稀疏用户涂鸦通过可见性感知的透射率覆盖提升至3D空间。
- 将物体选择建模为全局图割能量最小化问题，传播稀疏标注以覆盖完整3D物体。
- 支持多轮交互式细化，用户可从额外视角迭代纠正选择结果。

### 主要贡献

- 提出训练免费的交互式3D物体选择框架，支持稀疏视角输入和稀疏涂鸦引导。
- 引入基于超点和连续性权重图的图割优化方法，有效传播稀疏用户证据。
- 设计了可见性感知的透射率覆盖机制，将2D涂鸦准确提升到3D空间。
- 天然支持多轮细化交互，逐步提升选择质量。
- 实验表明在较少交互视角和大幅降低计算开销的条件下，达到与基于多视角SAM方法相当的选择质量。

### 局限性

摘要未提供足够信息，无法得知在极端稀疏视角下的性能边界、对不同场景类型的适应能力、与SAM方法的具体质量差异数值、以及用户交互轮次对性能的详细影响。摘要也未提及方法在复杂拓扑物体或遮挡严重场景下的表现。

### 阅读优先级

**高**

理由：该方法针对3DGS物体选择中计算开销大、依赖密集视角的实际痛点，提出无需训练的轻量级解决方案，兼具实用性和创新性。而且其交互式多轮细化设计贴合真实部署场景，对3D场景编辑和资产提取方向的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Selecting a complete 3D object from a reconstructed scene with minimal user effort is essential for practical scene editing and embodied interaction. Existing 3DGS-based methods either retrain the Gaussian representation to embed per-object labels, or build dense multi-view SAM observations, both requiring heavy computation and dense viewpoint coverage that is rarely available in practice. We present GaussianSelector, a training-free framework for interactive 3D object selection from sparse views and sparse scribble guidance. Operating directly on native Gaussian primitives, we coarsen dense Gaussians into geometrically coherent superpoints and construct a continuity-weighted graph using appearance and spatial cues. Sparse user scribbles are lifted into 3D via visibility-aware transmittance coverage, and selection is solved as a global graph-cut energy minimization that propagates sparse evidence to a complete 3D object. This design naturally supports multi-round refinement, where users iteratively correct the selection from additional viewpoints to progressively improve the result. Experiments demonstrate that GaussianSelector achieves competitive selection quality against state-of-the-art multi-view SAM-based methods, while requiring significantly fewer interaction views and substantially lower computational overhead. These properties make it well suited for human-in-the-loop 3D scene editing and 3D asset extraction in real-world deployment scenarios.

</details>

## Embodied / Robotics / AR Applications

### 2026-08

#### 2026-08-06 - VIDP: Variable Impedance Diffusion Policy for Compliant Robot Manipulation from Diverse Demonstrations

**Authors:** Hisham Khalil, Neil Fernandes, Thomas M. Kwok, Hsiu-Chin Lin, Yue Hu
**Links:** [abs](https://arxiv.org/abs/2608.06210) - [pdf](https://arxiv.org/pdf/2608.06210)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VIDP: Variable Impedance Diffusion Policy for Compliant Robot Manipulation from Diverse Demonstrations
- 作者：Hisham Khalil, Neil Fernandes, Thomas M. Kwok, Hsiu-Chin Lin, Yue Hu
- 出版日期：2026-08-06
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.06210

### 一句话总结
本文提出一种基于模仿学习的变阻抗扩散策略（VIDP），通过任务参数化的方向感知混合模型从多样演示中提取刚度分布，使机器人无需力传感器即可同时预测位姿动作与任务顺应性。

### 研究问题
如何在缺少力传感器的情况下，从运动学演示数据中学习可变阻抗控制策略，以提高接触丰富操作任务的成功率并降低交互力，同时避免静态顺应性无法适应多变接触约束的问题。

### 核心思路/方法
- 提出VIDP框架，将变阻抗控制与模仿学习结合。
- 利用任务参数化的方向感知混合模型（TP-DAMM）从多样演示中提取物理上一致的轨迹分布。
- 将该分布映射为刚度轮廓（stiffness profiles），使策略能联合预测位姿动作与任务顺应性。
- 该方法无需力传感器，仅基于运动学数据推断隐式顺应性。

### 主要贡献
- 提出一种无需力传感器的变阻抗控制学习框架（VIDP），解决了顺应性作为隐藏变量难以从运动学数据中直接推断的问题。
- 引入TP-DAMM用于从多样演示中提取物理一致的轨迹分布，避免了将几何适应误判为有意顺应性的问题。
- 真实世界实验表明，VIDP在任务成功率上显著优于固定阻抗基线，同时相对于高刚度控制器降低了交互力，相对于低刚度基线降低了跟踪误差。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该研究针对接触丰富操作中变阻抗控制的关键难点（无传感器条件下推断顺应性），提出了联合预测动作与顺应性的新框架，并给出了真实实验的成功率、交互力和跟踪误差对比，对机器人学习与控制方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Contact-rich manipulation requires precise tracking and mechanical compliance, where variable impedance control can improve robustness in task success, whereas static compliance cannot adapt to varying contact constraints. Variable impedance skills can be learned from demonstrations, avoiding complex modeling, but compliance is a hidden variable in force-agnostic kinematic data. While existing methods infer compliance from trajectory variations, these variations may reflect geometric adaptation and not intentional compliance when subject to changing spatial layouts. Therefore, this letter introduces Variable Impedance Diffusion Policy (VIDP), an imitation learning-based variable impedance control framework leveraging a Task-Parameterized Directionality-Aware Mixture Model (TP-DAMM) to extract physically consistent trajectory distributions from diverse demonstrations. By mapping distributions to stiffness profiles, VIDP jointly predicts pose actions and task compliance without force sensors. Real-world experiments show that VIDP significantly outperforms fixed-impedance baselines in task success rate while reducing interaction forces with respect to high stiffness controllers and tracking errors with respect to low stiffness baselines.

</details>

#### 2026-08-06 - Topometric Autonomous Vehicle Localization by Combining Visual Embeddings and Feed-Forward 3D Models

**Authors:** Eulogio Quemada-Torres, Alberto Jaenal, Francisco-Angel Moreno, Javier Gonzalez-Jimenez
**Links:** [abs](https://arxiv.org/abs/2608.06021) - [pdf](https://arxiv.org/pdf/2608.06021)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** pose estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Topometric Autonomous Vehicle Localization by Combining Visual Embeddings and Feed-Forward 3D Models
- 作者：Eulogio Quemada-Torres, Alberto Jaenal, Francisco-Angel Moreno, Javier Gonzalez-Jimenez
- 出版日期：2026-08-06
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.06021

### 一句话总结
本文提出一种融合视觉嵌入（VPR）与前馈神经3D几何（FF3D）测姿的拓扑度量定位框架，在保留外观变化鲁棒性的同时提升定位精度。

### 研究问题
如何将视觉位置识别（VPR）的低度量精度限制，与基于前馈神经3D模型（FF3D）的精确局部轨迹估计相结合，实现兼顾鲁棒性和精度的顺序外观定位。

### 核心思路/方法
- 提出一个拓扑度量（topometric）定位框架，迭代结合概率VPR与FF3D度量位姿估计。
- 设计自动离线建图工具，建模场景不同区域的“位姿-外观”交互关系（拓扑度量图）。
- 在线阶段采用粒子滤波器，融合里程计、地点置信度，并驱动FF3D推理，将神经度量估计纳入概率外观定位。
- 框架具备模块化设计，描述子提取器和FF3D模型可互换。

### 主要贡献
- 提出将VPR与FF3D度量估计结合进统一概率定位框架的新方法。
- 引入自动离线建图工具，显式建模拓扑度量中的位姿-外观关系。
- 在三个公开基准上进行了广泛评估，显著优于现有基于外观的方法。
- 模块化架构支持组件替换；分析表明顺序置信度可缓解感知混淆（perceptual aliasing）下的严重失败。

### 局限性
摘要未提供足够信息：未提及具体失败模式、计算开销、实时性能、对极端动态场景的适应性，或对FF3D模型失效时的处理策略等局限性。

### 阅读优先级
**中**。理由：该工作针对VPR度量精度不足这一明确痛点提出创新融合方案，并展示了基准上的显著提升，对从事视觉定位、机器人和AR的研究者有参考价值。但摘要未给出与主流局部特征/神经表征方法的定量对比细节，且无实验细节支撑其声称的“显著提升”程度，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Effective Visual Localization (VL) requires a map of the environment that combines compactness for efficient scalability with robustness against visual appearance changes and metric precision. Through low-dimensional image embeddings, Visual Place Recognition (VPR) is able to successfully meet the first two requirements, but its low metric accuracy makes it less suitable than standard VL approaches based on local features or neural representations. This limitation can be overcome by integrating VPR with the accurate local trajectory estimates produced by feed-forward neural 3D geometry (FF3D) models. In this paper, we address sequential appearance-based localization through a topometric framework that iteratively combines probabilistic VPR with FF3D metric pose estimation in controlled image sets. Our approach proposes an automatic offline mapping tool that models the topometric pose-appearance interaction in the different parts of the scene. This map is later employed by an online particle filter that estimates the pose from odometry and belief over places for FF3D inference, successfully incorporating neural metric estimation into probabilistic appearance-based localization. We extensively evaluate the framework on three known benchmarks, demonstrating substantial improvements over existing appearance-based methods. The modularity of our approach allows the descriptor extractor and FF3D model to remain interchangeable, and a focused analysis further shows that sequential belief can mitigate severe failures under perceptual aliasing.

</details>

#### 2026-08-05 - SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding

**Authors:** Yue Zhang, Yingzhao Jian, Yunqiu Xu, Xiaoxiao Sun, Hehe Fan
**Links:** [abs](https://arxiv.org/abs/2608.05137) - [pdf](https://arxiv.org/pdf/2608.05137)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding
- 作者：Yue Zhang, Yingzhao Jian, Yunqiu Xu, Xiaoxiao Sun, Hehe Fan
- 出版日期：2026-08-05T17:56:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.05137

### 一句话总结
SmartMage提出了一种动态模态编排的多模态大语言模型，通过按查询自适应选择相关模态并引导专家激活，从而提升3D场景理解性能。

### 研究问题
现有3D场景理解多模态大语言模型通常使用固定模态组合，忽略了不同查询对模态需求的差异性，导致引入无关模态的语义噪声、未充分利用高信息量模态，造成计算浪费和推理质量下降。论文旨在解决如何根据查询动态编排异构模态的问题。

### 核心思路/方法
SmartMage包含两个核心模块：
1. **语义引导的模态自适应路由模块（SMART）**：利用语义先验、文本-模态对齐和模态质量信号，为每个查询选择任务相关模态。
2. **模态感知门控专家模块（MAGE）**：利用模态先验引导专家激活，实现多模态推理中的自适应专业化。

通过这两个模块，SmartMage实现了语义感知的3D场景理解，即根据查询内容动态决定使用哪些模态并分配对应的专家处理。

### 主要贡献
- 提出SmartMage，一个支持动态模态编排的统一多模态大语言模型，克服了固定模态组合的局限。
- 设计SMART模块实现语义引导的模态选择，以及MAGE模块实现模态感知的专家激活。
- 在五个3D场景理解基准上取得最先进性能，并在RGB-only视频理解基准上获得有竞争力的结果。
- 构建诊断基准ScanFacet，将任务划分为细粒度语义类别，揭示不同语义类型偏好的模态组合模式，验证了SmartMage的有效性。

### 局限性
摘要未提供足够信息。摘要中未讨论模型的失败案例、计算开销细节、对不同模态缺失的鲁棒性，或各模块的消融实验结果等局限性内容。

### 阅读优先级
**高**。理由：该论文针对多模态大语言模型在3D场景理解中的固定模态组合痛点，提出动态模态编排的新思路，方法设计具有系统性（路由+门控专家），并在多个基准上验证了有效性。对从事3D理解、具身智能或多模态大语言模型研究的读者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Understanding 3D scenes is fundamental to embodied intelligence, requiring joint reasoning over heterogeneous information from multiple modalities, including visual and geometric cues. However, the relevance of these modalities often varies across queries. Existing Multimodal Large Language Models (MLLMs) typically rely on fixed modality combinations, overlooking query-dependent modality needs. Such a rigid design can introduce semantic noise from irrelevant modalities while underutilizing more informative ones, leading to wasted computation and diluted reasoning. To address these challenges, this paper proposes SmartMage, a unified MLLM that dynamically orchestrates heterogeneous modalities for semantic-aware 3D scene understanding. Specifically, SmartMage incorporates: (1) a Semantic-guided Modality Adaptive RouTng (SMART) module that selects task-relevant modalities using semantic priors, text-modality alignment, and modality quality; and (2) a Modality-Aware Gating Expert (MAGE) module that leverages modality priors to guide expert activation, fostering adaptive specialization in multimodal reasoning. Empirically, SmartMage achieves state-of-the-art performance across five 3D scene understanding benchmarks, and attains competitive results on RGB-only video understanding benchmarks. In our diagnostic benchmark ScanFacet, tasks are divided into fine-grained semantic categories, enabling analysis of modality combinations preferred by each semantic type. The observed modality-semantic patterns provide further evidence of SmartMage's effectiveness. Project page: https://yuecheong.github.io/SmartMage/.

</details>

#### 2026-08-05 - HiSC: Hierarchical Spatial Clustering Token Compression for Efficient 3D Scene Understanding

**Authors:** Jiuhe Qu, Yingping Liang, Ying Fu
**Links:** [abs](https://arxiv.org/abs/2608.04610) - [pdf](https://arxiv.org/pdf/2608.04610)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HiSC: Hierarchical Spatial Clustering Token Compression for Efficient 3D Scene Understanding
- 作者：Jiuhe Qu, Yingping Liang, Ying Fu
- 出版日期：2026-08-05
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.04610

### 一句话总结
HiSC 是一种无需训练的分层空间聚类 token 压缩框架，通过将 token 压缩从 token 级提升到聚类级，在保持 3D 场景理解性能的同时实现超过 90% 的视觉 token 缩减。

### 研究问题
3D 视觉-语言模型（3D VLMs）在多视角场景中因重复观察和大量无信息区域导致 token 冗余严重，计算成本高昂。现有视觉 token 压缩方法（多用于 2D VLMs）无法捕捉 3D 场景的结构化特性，导致空间覆盖不完整和细粒度细节丢失。

### 核心思路/方法
HiSC 将 token 压缩从 token 级选择提升为聚类级处理，利用几何与语义联合线索将 token 组织为空间上有依据的聚类。具体包含两个阶段：
1. **空间图合并策略（SGraM）**：在 LLM 推理前，将跨视角冗余建模为空间连通性，合并物理上一致的区域，有效去除极端相似的冗余 token。
2. **空间聚类剪枝范式（SCluP）**：在 LLM 推理内部执行，对聚类间和聚类内进行分层压缩，在保留目标实例完整性的同时，为重要区域保留细粒度细节。

### 主要贡献
- 提出 HiSC，一个无需训练的分层空间聚类 token 压缩框架，专为 3D VLMs 设计。
- 引入基于空间图的合并策略（SGraM），利用几何与语义线索实现跨视角冗余 token 的高效合并。
- 提出基于空间聚类的剪枝范式（SCluP），在 LLM 推理过程中实现分层压缩，兼顾实例完整性与细粒度细节。
- 在多种 3D 推理基准上验证了有效性，尤其是在高 token 剪枝率下；可实现超过 90% 的 token 缩减且性能损失极小。

### 局限性
摘要未提供足够信息，未具体说明在不同任务类型下的性能边界、高剪枝率下的性能下降幅度细节、计算开销对比等实验细节。

### 阅读优先级
**高**。理由：该工作针对 3D VLMs 的高计算成本问题提出无需训练的压缩方案，在 token 缩减率上取得了显著结果（>90%），且与当前具身/机器人/AR 应用领域紧密相关。方法具有明确的通用性潜力，对从事 3D 场景理解与多模态模型效率优化研究的读者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D vision-language models (3D VLMs) enable spatial reasoning over multi-view scenes but suffer from substantial token redundancy due to duplicated observations and large uninformative regions, leading to high computational cost. Although visual token compression has shown promise in accelerating 2D VLMs, it fails to capture the structured nature of 3D scenes and leads to incomplete spatial coverage and loss of fine-grained details. In this paper, we propose \textbf{HiSC}, a training-free framework for hierarchical spatial clustering token compression in 3D VLMs. HiSC lifts token compression from token-level selection to cluster-level processing by organizing tokens into spatially grounded clusters using joint geometric and semantic cues. Specifically, we first introduce a \textbf{spatial graph-based merging (SGraM) strategy} that models cross-view redundancy as spatial connectivity and consolidates physically consistent regions, effectively merging extremely similar redundant tokens prior to LLM inference. We then propose a \textbf{spatial clustering-based pruning (SCluP) paradigm} within LLM inference, which performs hierarchical compression across clusters and within clusters, preserving object instance completeness while retaining fine-grained details for important regions. Extensive experiments on diverse 3D reasoning benchmarks show validate the effectiveness of HiSC, particularly under high visual token pruning ratios. Besides, HiSC achieves over 90\% token reduction with minimal performance degradation. Code is accessible at https://github.com/elecreak/HiSC.

</details>

#### 2026-08-05 - Talk2Sensors: 3D Visual Grounding in Autonomous Driving via Sensor-Adaptive Physical Cue Matching

**Authors:** Runwei Guan, Di Tian, Ningwei Ouyang, Ruixiao Zhang, Shaofeng Liang, Haocheng Zhao, Lianqing Zheng, Xiaokai Bai, Guotao Wang, Daizong Liu, Henghui Ding, Hui Xiong
**Links:** [abs](https://arxiv.org/abs/2608.04568) - [pdf](https://arxiv.org/pdf/2608.04568)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Talk2Sensors: 3D Visual Grounding in Autonomous Driving via Sensor-Adaptive Physical Cue Matching
- 作者：Runwei Guan, Di Tian, Ningwei Ouyang, Ruixiao Zhang, Shaofeng Liang, Haocheng Zhao, Lianqing Zheng, Xiaokai Bai, Guotao Wang, Daizong Liu, Henghui Ding, Hui Xiong
- 出版日期：2026-08-05
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.04568

### 一句话总结
本文提出首个基于相机、LiDAR和4D雷达的多传感器3D视觉定位数据集Talk2Sensors及统一框架TSFormer，通过语言路由的物理线索匹配实现自动驾驶场景下的查询自适应定位。

### 研究问题
现有3D视觉定位（3DVG）研究主要局限于室内RGB-D或点云输入，户外扩展也多依赖单目图像，未能充分利用真实户外场景中异构传感器所捕获的互补物理属性（如视觉纹理、3D几何、物体运动学），导致查询自适应的灵活鲁棒定位能力不足。

### 核心思路/方法
- 构建多传感器数据集Talk2Sensors：基于相机、LiDAR和4D雷达，包含8,682条语言指令和20,558个被指对象，提示与传感器特定物理线索显式对齐。
- 提出TSFormer统一Transformer框架，采用从粗到细的属性感知融合策略：
  - Language-Routed Property Sampler：先用查询级语言线索调制传感器采样权重，进行粗粒度文本条件特征检索。
  - Sparse-Preserving Modality Arbiter：再执行细粒度模态仲裁和文本引导细化，确定精确的被指空间位置。
- 该设计根据每个提示的语义需求动态路由外观、几何和运动线索，防止密集模态淹没稀疏但关键传感器信号。

### 主要贡献
- 提出首个多传感器（相机+LiDAR+4D雷达）3D视觉定位数据集Talk2Sensors。
- 提出TSFormer统一框架，实现传感器自适应物理线索匹配的粗到细融合。
- 实验表明TSFormer在Talk2Sensors上比最强基线提升8.05 mAP，并在单目Mono3DRefer基准上达到53.05% Acc@0.5，取得SOTA性能。

### 局限性
摘要未提供足够信息（未提及数据集规模细节的局限、传感器标定/同步要求、计算开销、失败案例分析或对特定场景（如恶劣天气）的鲁棒性评估）。

### 阅读优先级
**高**。理由：该工作首次将3D视觉定位拓展到多传感器自动驾驶场景，提出新数据集和统一框架，且性能提升显著（+8.05 mAP），对多模态感知、 embodied AI和自动驾驶语言交互方向具有较强参考价值；实验跨两个基准验证了泛化能力。

</details>

<details>
<summary>Abstract</summary>

As a key capability for embodied intelligence, 3D visual grounding (3DVG) has been predominantly studied in indoor scenes with RGB-D or point-cloud inputs, while existing outdoor extensions largely rely on monocular images alone. Both settings fall short of real-world outdoor perception, where heterogeneous sensors capture complementary yet distinct physical properties, such as visual texture, 3D geometry, and object kinematics, that are indispensable for flexible and robust query-adaptive grounding but remain under-exploited. To bridge this gap, we introduce Talk2Sensors, the first multi-sensor 3D visual grounding dataset built upon camera, LiDAR, and 4D radar. It contains 8,682 language instructions and 20,558 referred objects, with diverse prompts explicitly aligned with sensor-specific physical cues. Furthermore, we propose TSFormer, a unified Transformer-based framework for language-guided 3D visual grounding in autonomous driving. TSFormer adopts a coarse-to-fine property-aware fusion strategy: the Language-Routed Property Sampler first performs coarse text-conditioned feature retrieval by modulating sensor sampling weights with query-level linguistic cues, while the subsequent Sparse-Preserving Modality Arbiter module conducts fine-grained modality arbitration and text-guided refinement to determine the precise referred spatial location. This design enables dynamic routing of appearance, geometry, and motion cues according to the semantic requirements of each prompt, preventing dense modalities from overwhelming sparse but critical sensor signals. Extensive experiments demonstrate that TSFormer achieves state-of-the-art performance across multiple benchmarks: it improves over the strongest baseline by 8.05 mAP on Talk2Sensors, and transfers to the monocular Mono3DRefer benchmark with 53.05\% Acc@0.5.

</details>

#### 2026-08-04 - CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction

**Authors:** Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren
**Links:** [abs](https://arxiv.org/abs/2608.03211) - [pdf](https://arxiv.org/pdf/2608.03211)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction
- 作者：Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren
- 出版日期：2026-08-04
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.03211

### 一句话总结
本文提出 CrossScope，一种角色不对称的双流手术视频预测世界模型，用于 Mother-Child 内镜逆行胰胆管造影（ERCP）中双内镜协作场景的未来动态预测。

### 研究问题
如何对多个独立运动观察者组成的协作系统进行未来视频预测，具体聚焦于 Mother-Child ERCP 中两个柔性内镜提供互补且角色依赖视图的场景，且这些视图之间没有标定的立体关系。

### 核心思路/方法
- 将问题形式化为“角色不对称双内镜未来预测”：根据预测目标和空间需求，选择性地跨视图传递证据，而非对称信息交换。
- 提出 CrossScope，一个双流手术世界模型，保留各视图专属专家，并通过几何引导的残差交互实现目标特定的证据路由。
- 学习两个互补通信方向：Mother 视图的几何运动线索指导 Child 视图未来动态；仅在建立有效空间对应时，位姿对齐的 Child 外观辅助 Mother 视图预测。
- 构建配对双内镜基准，包含同步的体模和真实 ERCP 数据，评估视觉保真度、结构保留、目标定位和运动一致性。

### 主要贡献
- 首次提出角色不对称双内镜未来预测问题，区别于传统假设对称信息交换的多视图融合方法。
- 提出 CrossScope 模型，实现视图特定表示保留与目标特定证据路由的兼顾。
- 建立包含体模和真实数据的配对双内镜基准，用于验证多观察者视觉世界建模方法。

### 局限性
摘要未提供足够信息。摘要中未包含关于模型计算成本、训练数据规模、失败案例分析或对临床实践适用性等局限性的讨论。

### 阅读优先级
**中**。理由：该工作针对手术视觉预测这一专业子领域，问题设定（Mother-Child ERCP）较为特殊，方法上提出的角色不对称路由思想具有一定新颖性；若读者专注于多观察者视频预测或手术机器人视觉建模，则价值较高；否则可作一般关注。摘要未提供定量性能细节，难以评估其相较基线优势的实际幅度。

</details>

<details>
<summary>Abstract</summary>

Visual world models typically learn future dynamics from a single observation stream, limiting their ability to model cooperative systems with multiple independently moving observers. We investigate this challenge in Mother--Child endoscopic retrograde cholangiopancreatography (ERCP), where two flexible scopes provide complementary yet role-dependent views without a calibrated stereo relationship. Unlike conventional multi-view fusion that assumes symmetric information exchange, we formulate \textbf{role-asymmetric dual-scope future prediction}, where cross-view evidence is selectively transferred according to the prediction target and its underlying spatial requirements. We propose \textbf{CrossScope}, a dual-stream surgical world model that preserves view-specific experts while enabling target-specific evidence routing through geometry-guided residual interactions. CrossScope learns two complementary communication directions: geometric motion cues from the Mother view guide Child-view future dynamics, while pose-aligned Child appearance supports Mother-view prediction only when valid spatial correspondence is established. This design allows each scope to contribute task-relevant evidence without compromising its view-specific representation. To evaluate this problem, we establish a paired dual-scope benchmark comprising synchronized phantom and real-world ERCP episodes, with evaluations assessing visual fidelity, structural preservation, target localization, and motion consistency. Experiments demonstrate that CrossScope consistently outperforms strong surgical video generation baselines, validating the importance of role-aware evidence routing for multi-observer visual world modeling.

</details>

#### 2026-08-03 - RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models

**Authors:** Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang, Mingkun Chan, Jichang Li, Guanbin Li
**Links:** [abs](https://arxiv.org/abs/2608.02953) - [pdf](https://arxiv.org/pdf/2608.02953)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models
- 作者：Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang, Mingkun Chan, Jichang Li, Guanbin Li
- 出版日期：2026-08-03
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.02953

### 一句话总结
RealWeather 提出了一种基于驾驶世界模型的全新天气转换方法，通过渐进式数据精炼与奖励驱动的强化学习优化，在真实视频上实现既真实又保持场景结构一致的天气转换。

### 研究问题
如何在无需大规模配对真实视频数据的前提下，实现既保持天气真实感又严格维持驾驶场景结构完整性的天气转换，尤其适用于自动驾驶系统的开发与评测。

### 核心思路/方法
RealWeather 的核心思路是直接从真实世界视频中学习真实天气动态，包含两个关键策略：
1. **渐进式真实感引导（Progressive Realism Bootstrapping）**：一种迭代式数据精炼策略，先用辅助的 Pseudo-Clear Generation 流水线生成伪风格条件视频作为初始训练数据，随着训练推进，逐步替换为模型自身生成的越来越真实的视频，从而弥合伪到真实域的差距，支持清晰的“晴-恶劣天气”双向转换。
2. **场景保真强化学习优化（Scene-Fidelity RL Optimization）**：一种奖励驱动的策略优化方法，显式惩罚对安全关键驾驶元素的改变，以严格保持结构完整性并抑制幻觉。

### 主要贡献
- 提出 RealWeather，一个用于真实且场景保真的天气转换的驾驶世界模型。
- 提出渐进式真实感引导的数据精炼策略，有效弥合伪到真实域差距。
- 提出场景保真强化学习优化，显式保护安全关键驾驶元素。
- 实验表明该方法在视觉真实感和结构保持上显著优于现有方法，并支持长尾天气场景生成和强零样本分布外泛化。

### 局限性
摘要未提供足够信息。例如，未提及具体数据集规模、计算资源需求、失败案例、局限场景（如极端天气的覆盖范围），以及与其他方法在定量指标上的具体数值对比。

### 阅读优先级
**高**。理由：该工作面向自动驾驶场景下的天气转换任务，提出的方法同时解决真实感与场景保真两大核心挑战，设计思路（渐进式精炼与强化学习结合）具有较强创新性，摘要声称在多项指标上大幅超越现有方法且具备零样本泛化能力，对自动驾驶仿真、感知鲁棒性研究等领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Realistic weather translation is valuable for developing and evaluating autonomous driving systems, yet collecting paired videos of the same scenes under different weather conditions at scale is impractical. Existing methods therefore rely on synthetic data, 3D weather editing, or geometry-conditioned generation, often compromising weather realism or scene fidelity. We propose RealWeather, a driving world model for both realistic and scene-faithful weather translation. Our key idea is to learn authentic weather dynamics directly from real-world videos. Specifically, RealWeather employs Progressive Realism Bootstrapping, an iterative data-refinement strategy. Assisted by an auxiliary Pseudo-Clear Generation pipeline, training initially starts with pseudo-style conditioning videos. As training proceeds, these inputs are progressively replaced with increasingly realistic videos generated by the model itself. This strategy bridges the pseudo-to-real domain gap, allowing the model to adapt seamlessly to real-world input distributions and naturally support bidirectional clear adverse translation. Furthermore, to strictly enforce structural integrity and suppress hallucinations, we introduce Scene-Fidelity RL Optimization, a reward-driven policy optimization strategy that explicitly penalizes alterations to safety-critical driving elements. Extensive experiments demonstrate that RealWeather significantly outperforms existing methods in visual realism and structural preservation, while enabling robust long-tail weather scenario generation and strong zero-shot out-of-distribution generalization.

</details>

#### 2026-08-03 - Contact-Driven Localization in a Freeform Robotic Self-Assembled Structure

**Authors:** Mohammadali Rashidioun, Michael Sosa, Petras Swissler
**Links:** [abs](https://arxiv.org/abs/2608.02895) - [pdf](https://arxiv.org/pdf/2608.02895)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Contact-Driven Localization in a Freeform Robotic Self-Assembled Structure
- 作者：Mohammadali Rashidioun, Michael Sosa, Petras Swissler
- 出版日期：2026-08-03
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.02895

### 一句话总结
该论文提出一种仅依赖机器人间二元接触信息的虚拟力框架，实现模块化自重构机器人的无外部设施定位，并支持自由形态自组装。

### 研究问题
如何在无需外部追踪设施或高成本传感器的条件下，使自重构机器人系统在组装过程中准确识别相对位置，以实现多样结构的可扩展、自由形态自组装。

### 核心思路/方法
- 利用机器人间的本地通信，仅获取二元接触信息（两个机器人是否物理连接）。
- 构建虚拟力框架：机器人迭代优化自身位姿，对已连接的邻居施加吸引，对未连接的邻居施加排斥。
- 整个方法不依赖外部基础设施，仅使用最小化的机载感知能力。

### 主要贡献
- 首次提出仅基于二元接触信息进行接触驱动的定位方法，替代传统外部追踪或高成本传感器方案。
- 引入虚拟力框架将接触信息转化为位姿优化的驱动力。
- 通过塔状和悬臂结构的组装仿真，验证了该方法可支持准确、可扩展、自由形态的自组装。

### 局限性
摘要未提供足够信息：论文未提及方法对感知噪声的鲁棒性、通信范围限制、计算复杂度、扩展至大规模群体的性能、以及与现有方法的定量对比等细节。

### 阅读优先级
**中**。该论文针对自重构机器人定位问题提出了新颖的低成本方案，方法思路简洁且具有实用潜力，适合对群机器人自组装、无外部设施定位感兴趣的读者。但摘要中缺少实验细节和性能对比，若需要深入评估方法效果或复现，需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Accurate localization remains a key challenge in swarm robotics, particularly for self-reconfigurable systems that must identify relative positions to form diverse structures. Most existing approaches rely on external tracking infrastructure or high-cost sensors, which limit scalability and deployment in unstructured environments. In this paper, we propose a novel contact-driven localization method for modular robots that leverages only local communication through binary contact information (whether two robots are physically connected or not). To exploit these contact cues, we introduce a virtual-force framework in which robots iteratively refine their poses attracting toward dock-connected neighbors and repelling from non-connected ones. The method requires no external infrastructure and relies only on minimal onboard sensing. Simulations show effective localization during the assembly of towers and cantilevers, enabling accurate, scalable, free-form self-assembly.

</details>

#### 2026-08-03 - DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation

**Authors:** Jiaming Chen, Guoan Xu, Aoshen Huang, Haozhuo Zhang, Yang Li, Wei Pan
**Links:** [abs](https://arxiv.org/abs/2608.02428) - [pdf](https://arxiv.org/pdf/2608.02428)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DF³: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation
- 作者：Jiaming Chen, Guoan Xu, Aoshen Huang, Haozhuo Zhang, Yang Li, Wei Pan
- 出版日期：2026-08-03T16:08:59Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.02428

### 一句话总结
本文提出一种完全在潜空间内进行未来状态预测、无需解码器的世界建模框架 DF³，面向自动驾驶中的感知与控制任务，实现高效率和灵活部署。

### 研究问题
如何在不依赖像素级生成或解码器的情况下，高效预测视频序列中的未来状态，并将其直接用于自动驾驶中的下游任务（如感知与控制），以降低计算开销并提升系统灵活性。

### 核心思路/方法
- 提出 Decoder-Free Feature Forecasting（DF³）框架，完全在潜空间内建模世界演化，直接生成任务输出，彻底移除了解码器。
- 具体做法：向冻结的视觉基础模型的末端模块注入可学习的空间查询（spatial queries），直接提取未来状态表征。
- 设计轻量化的 Motion-Aware Context Fusion（MACF）机制，将粗粒度光流扭曲与细粒度潜空间互相关相结合，使查询与历史 token 表示交互，显式对齐并预测下一帧的特征。
- 随后使用一组专门的任务查询（task queries）对这些预测特征进行探测，以支撑下游任务。

### 主要贡献
- 首次提出完全无解码器的未来特征预测框架，消除解码器带来的计算瓶颈。
- 设计了可学习的空间查询与轻量级运动感知上下文融合机制，实现高效且准确的未来状态表征预测。
- 在公开基准和机器人模拟器的零样本部署实验中，表明该方法在达到与最先进方法相当性能的同时，具备更优的效率和灵活性，适用于集成感知与控制系统。

### 局限性
摘要未提供足够信息。摘要中未明确讨论方法的失败场景、潜在的信息丢失问题、对冻结视觉基础模型的依赖限制、亦未给出定量对比的细节或消融研究。

### 阅读优先级
**中**。理由：该工作针对自动驾驶中世界建模的计算瓶颈提出了一种新颖的去解码器思路，方法设计具有创新性，且强调效率与灵活性，可能与具身智能与机器人方向相关；但如果读者不关注潜空间预测或无解码器架构，则优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

Forecasting future states from video sequences is a critical challenge for autonomous robotic systems and a fundamental objective of world modeling. Prior generative methods operating at the pixel level inevitably overemphasize task-irrelevant details, leading to prohibitive computational overhead. While latent-based approaches attempt to mitigate this by predicting features directly, the persistent reliance on heavy decoders for state-to-task mapping remains a computational bottleneck. In this work, we propose Decoder-Free Feature Forecasting (DF$^3$), a novel framework that models world evolution entirely within the latent space and directly derives task outputs, completely eliminating the need for a decoder. Specifically, DF$^3$ injects learnable spatial queries into the terminal blocks of a frozen vision foundation model to extract future state representations directly. By employing a lightweight, unified Motion-Aware Context Fusion (MACF) mechanism that seamlessly integrates coarse flow warping with fine-grained latent cross-correlation, these queries interact with historical token representations to explicitly align and forecast the feature of the next frame. Subsequently, a specialized set of task queries probes these forecasted features for the downstream task. Extensive experiments on public benchmarks and zero-shot deployment in a robotic simulator demonstrate that DF$^3$ achieves performance comparable to state-of-the-art methods while offering superior efficiency and flexibility for integrated perception and control.

</details>

#### 2026-08-02 - SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space

**Authors:** Ruiteng Zhao, Zhengshen Zhang, Yue Su, Wenshuo Wang, Jiahui Li, Zhiyuan Yang, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu
**Links:** [abs](https://arxiv.org/abs/2608.01397) - [pdf](https://arxiv.org/pdf/2608.01397)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space
- 作者：Ruiteng Zhao, Zhengshen Zhang, Yue Su, Wenshuo Wang, Jiahui Li, Zhiyuan Yang, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu
- 出版日期：2026-08-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.01397

### 一句话总结
本文提出 SG-WAM，一种在策略派生的表征空间中自监督学习几何感知的动作条件动力学模型，通过联合优化潜在未来预测、几何约束和流匹配动作生成，在 LIBERO 基准上取得 98.5% 平均成功率。

### 研究问题
现有世界动作模型（WAM）在动作生成中耦合未来状态预测，但对未来动力学的建模空间存在不足：要么使用感知密集的观测空间目标，要么使用辅助潜在空间，难以同时满足动作相关性和几何感知性。本文旨在解决如何构建一个既与动作生成对齐又具备几何感知的未来建模空间这一问题。

### 核心思路/方法
- 提出 SG-WAM 框架，在策略派生的表征空间中直接学习几何感知、动作条件的动力学模型。
- 引入可学习的动力学令牌（learnable dynamics tokens）和自引导世界预测器（Self-Guided World Predictor），在机器人动作干预下预测这些令牌的未来潜在状态。
- 预测目标由同一策略骨干网络（policy backbone）的指数移动平均（EMA）副本生成，为动作专家所使用的表征族提供稳定监督。
- 通过几何监督（geometric supervision）对策略图像令牌表征进行结构化，为动力学令牌提供空间上有依据的上下文，从而构建一个既动作相关又几何感知的未来对齐空间。
- 将潜在未来预测、几何接地和流匹配动作生成在统一框架中端到端联合优化。

### 主要贡献
- 提出 SG-WAM，一种自引导世界建模框架，在策略表征空间中联合学习几何感知的动作条件动力学。
- 采用 EMA 副本作为预测目标来源，实现在动作专家表征族内的稳定自监督。
- 通过几何监督强化图像令牌表征的空间结构，使未来对齐空间兼具动作相关性与几何感知性。
- 基于 0.9B 参数模型（无大规模具身预训练），在 LIBERO 上达到 98.5% 平均成功率、LIBERO-Plus 上达到 73%，并在分布内和分布外的真实世界评估中优于强基线方法。

### 局限性
摘要未提供足够信息，无法获知该方法的失败场景、计算开销、泛化边界或伦理影响等局限性细节。

### 阅读优先级
**高**。理由：该方法在 LIBERO 基准上取得接近完美的成功率（98.5%），且在分布外真实世界评估中优于强基线，同时模型规模仅 0.9B 且无需大规模具身预训练，对于机器人操作领域的世界建模与动作生成研究具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

World Action Models (WAMs) couple action generation with prediction of future states. Their effectiveness depends on whether future dynamics are modeled in a space that is both aligned with action generation and sufficiently geometry-aware to capture where and how actions change the scene. Existing WAMs typically satisfy only part of this requirement, relying on either perceptually heavy observation-space targets or auxiliary latent spaces that are not jointly structured for action relevance and geometry. We propose SG-WAM, a self-guided framework that learns geometry-aware action-conditioned dynamics directly in the policy-derived representation space. SG-WAM introduces learnable dynamics tokens and a Self-Guided World Predictor that forecasts their future latent states conditioned on intervening robot actions. Prediction targets are generated by an exponential moving average copy of the same policy backbone, providing stable supervision within the representation family used by the action expert. Geometric supervision further structures the policy image-token representations, providing spatially grounded context for the dynamics tokens and yielding a future-alignment space that is both action-relevant and geometry-aware. Latent future prediction, geometric grounding, and flow-matching action generation are jointly optimized end-to-end in a unified framework. Built on a 0.9B model without large-scale embodied pretraining, SG-WAM achieves 98.5% average success on LIBERO and 73% on LIBERO-Plus, while outperforming strong baselines in both in-distribution and out-of-distribution real-world evaluations.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
