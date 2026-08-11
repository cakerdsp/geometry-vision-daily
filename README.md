# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：46
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 15
  - Neural Scene Representations & Rendering: 13
  - Embodied / Robotics / AR Applications: 12
  - Geometry Foundation Models: 4
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**趋势一：紧凑化与高效化成为神经策略与场景表征的核心追求**
多篇论文不约而同地转向小型化、轻量化模型，试图在保持性能的同时摆脱对大规模骨干网络和重型计算管线的依赖。SLIM-0.5B（2608.09771）用仅0.5B参数的潜在交互策略替代大型多模态VLA骨干网络；EvTrajGS（2608.08585）通过连续时间轨迹参数化避免了计算昂贵的SLAM式增量跟踪流水线；View-Adaptive Renderer（2608.09110）则拒绝使用扩散模型SDS重监督，仅凭借光度渲染损失和轻量注意力正则化实现高质量重建。这一趋势背后是"够用即好"的工程哲学——与其堆参数、堆计算，不如针对任务本质设计紧凑有效的归纳偏置。

**趋势二：稀疏传感器与部分信息条件下的位姿求解成为新的算法竞技场**
当感知输入不再是"全而准"时，如何从极少量信息中恢复几何或运动，成为多条工作线的交汇点。Height-Constrained 2-Point Minimal Solver（2608.09520）利用机载IMU提供的倾角和高度信息，将传统PnP对标记点数量的需求从3个降为2个；Tether-Inertial Localization（2608.09515）更是绕开视觉与GNSS，仅靠系绳长度和角度实现厘米级定位；MH-NFPG（2608.09579）则直面雷达点云稀疏性导致的多模态歧义问题。这些工作共同表明：求解算法的设计正在从"信息充足假设"转向"信息匮乏条件下的最优化"。

**趋势三：4D/动态重建从"离散帧预测"走向"连续时间建模"**
Uni4R（2608.09613）将最优传输与常微分方程结合学习连续速度场，使得4D重建与点跟踪能够在任意时间戳下进行；ERF-GS（2608.08531）利用事件相机的高帧率特性补偿传统帧式视频在快速运动场景中的不足。与此同时，事件相机在本批次中多次出现（2608.09520、2608.08585、2608.08531），表明这一传感器正在从"小众硬件"转变为"解决动态与极端光照问题的关键工具"。

**趋势四：压缩伪影与输入质量不均被显式建模，而非隐式容忍**
JSGS（2608.08659）直接利用JPEG文件中的量化表构建视角特定的观测算子，对混合质量输入下的3DGS训练进行频率带加权监督；RayLift（2608.08476）则将立体深度估计的不确定性显式建模为射线证据而非确定性约束。两篇论文的共同逻辑是：输入噪声不是"无关紧要的干扰"，而是应当被系统建模并纳入优化过程的结构化信息。

**趋势五：世界模型理念跨越视频生成进入策略学习与感知恢复**
Sekai2（2608.09449）强调从"世界探索"走向"交互式世界建模"，提供长视频、相机轨迹与时间对齐语义三者兼备的数据集；MotionCraft（2608.08553）将视频超分视为"运动感知的潜在状态预测"，借用世界模型范式；SLIM（2608.09771）同样采用预测性潜在表征建模动作引发的状态转移。世界模型的"预测-交互"循环范式正在从纯生成任务外溢到策略学习和感知恢复任务。


#### 技术路线观察

- **几何基础模型**：本批次呈现出两条对立的路线。其一是在极简条件下追求闭式解解析求解——Height-Constrained 2-Point Solver（2608.09520）推导了闭式解和线性最小二乘解并分析退化配置；其二是用统计模型补偿解析模型的盲区——Tether-Inertial Localization（2608.09515）用高斯过程补偿悬链线模型的系统残差。ROEVO（2608.09112）代表第三条路线，将边缘像素组织为序列化簇用作特征表示，是一种"结构化中间表示"的尝试。

- **3D/4D重建**：核心分歧在于"是否需要显式运动学先验"。Uni4R（2608.09613）将最优传输+流匹配作为速度场的归纳偏置；EvTrajGS（2608.08585）用连续时间轨迹与时间耦合位姿保证时序一致性；ERF-GS（2608.08531）则把事件信息注入3DGS的优化和致密化两个阶段，提出与RGB解耦的事件分支学习。值得注意的是，相比往日常见的"扩散模型统一解决多模态歧义"路线，本批论文更倾向于流匹配与ODE等确定性+可控生成范式。

- **神经场景表示**：3DGS的生态位继续扩张，但监督方式趋于精细化——JSGS（2608.08659）挑战了"所有输入图像忠实采样场景辐射"的隐含假设，从JPEG元数据中提取量化表构造域匹配的观测算子。DoRF++（2608.08381）则将NeRF的思想跨界引入Wi-Fi感知，将Doppler速度投影建模为虚拟相机视角，这是NeRF作为"可微投影模型"这一底层逻辑的又一次迁移。

- **机器人/AR应用**：两条主线清晰可辨。其一是**接触丰富的灵巧操作**——VIDP（2608.06210）从多样演示中提取任务参数化的方向感知混合模型，映射为刚度轮廓，实现无需力传感器的变阻抗控制；SLIM（2608.09771）用自监督掩码轨迹预测学习动作锚定的预测性潜在表征。其二是**非结构化/极端环境下的自主系统**——UnsDrive（2608.09098）针对矿区场景显式建模occupied/free/unknown三种空间，Tether-Inertial Localization（2608.09515）面向行星探测无人机的系绳定位。


#### 值得优先阅读的论文

1. **Uni4R**（2608.09613）——最优传输与ODE的组合在4D重建与点跟踪的连续时间建模中显示出独特的运动学一致性优势，其积分一致性训练策略解决了分数帧缺乏真实值监督的痛点，框架设计有启发意义，值得优先精读。

2. **SLIM-0.5B**（2608.09771）——在VLA大模型主导的趋势下，反其道而行之。其自监督掩码轨迹预测、动作重建+未来潜在预测双重目标、以及流匹配训练的组合逻辑，为紧凑型机器人策略提供了可复现的完整技术栈。

3. **VIDP**（2608.06210）——变阻抗控制是接触丰富操作从"位置控制"走向"柔顺控制"的关键一环。TP-DAMM从运动学数据中区分"几何适应"与"有意顺应"的思路，解决了模仿学习中隐藏变量推断的核心困难，对具身操作方向参考价值高。

4. **JSGS**（2608.08659）——挑战了3DGS一个未被充分审视的假设：输入图像忠实采样场景辐射。利用JPEG量化表构造观测算子的思路优雅且工程上可行，对多源混合质量输入的3D重建工作有直接的借鉴意义。

5. **EvTrajGS**（2608.08585）——在事件流重建中绕开SLAM式高计算管线，用连续时间轨迹参数化实现位姿-场景联合优化，在保持精度的同时显著降低计算负担，是"精度-效率"权衡框架下的代表性方案。


#### 可能的研究机会

1. **"压缩感知即先验"——将编码元数据引入三维重建的通用框架**。JSGS（2608.08659）启示了一个更大的方向：JPEG量化表仅是输入元数据的一种，EXIF信息、视频编码参数（H.264/H.265码率、GOP结构）、传感器响应曲线等均可作为"压缩观测模型"纳入重建监督。目前这一思路仅覆盖静态3DGS，推广到动态4D重建或事件-帧混合输入是自然延伸。

2. **"最小信息量位姿求解"的系统化扩展**。Height-Constrained 2-Point Solver（2608.09520）展示了利用机载传感器先验缩减标记点需求的可行性。更进一步：是否能结合IMU预积分、轮速计

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-11T09:40:22-04:00
**Total number of papers:** 46
**Number of papers added in the latest update:** 19
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

#### 2026-08-10 - Marrying Optimal Transport and ODEs for Unified Continuous-Time 4D Reconstruction and Tracking

**Authors:** Liying Yang, Hao Mo, Jialun Liu, Chen Liu, Xinxing Yu, Chenhao Guan, Hui Ma, Xiao Cao, Ajian Liu, Yanyan Liang
**Links:** [abs](https://arxiv.org/abs/2608.09613) - [pdf](https://arxiv.org/pdf/2608.09613)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Marrying Optimal Transport and ODEs for Unified Continuous-Time 4D Reconstruction and Tracking
- 作者：Liying Yang, Hao Mo, Jialun Liu, Chen Liu, Xinxing Yu, Chenhao Guan, Hui Ma, Xiao Cao, Ajian Liu, Yanyan Liang
- 出版日期：2026-08-10
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2608.09613

### 一句话总结
本文提出Uni4R框架，通过最优传输与常微分方程的协同，学习连续速度场，统一实现任意时间戳下的4D重建与点跟踪。

### 研究问题
现有统一4D重建与点跟踪方法依赖启发式插值或仅在整数时间戳预测，缺乏运动学一致性，无法建模任意时间戳的动态。本文旨在解决这一问题，实现统一的连续时间4D重建与点跟踪。

### 核心思路/方法
- 提出Uni4R框架，学习连续速度场作为运动学先验，同时服务于4D重建与点跟踪。
- 提出Flow Matching Guided Decoder（FMGD）：全局速度分支提取锚点特征，捕捉序列全局动态状态；利用Flow Matching理论，在锚点特征流形上构建由最优传输定义的概率路径，实例化为FM引导的速度特征，用于速度预测，形成稳健的运动学归纳偏置。
- 点重建分支提供几何特征；局部速度预测模块结合上述特征与时间嵌入，解码任意时间戳的速度。
- 提出积分一致性训练策略：针对分数帧缺乏高质量真实速度的问题，使用ODE求解器对速度积分以恢复目标点图，使模型可直接从整数时间戳进行端到端监督。

### 主要贡献
- 提出Uni4R，首次将最优传输与ODE结合，实现连续时间下的统一4D重建与点跟踪。
- 设计FMGD模块，利用Flow Matching理论建立运动学归纳偏置，提升动态建模能力。
- 提出积分一致性训练策略，解决分数帧速度监督缺失问题。
- 实验表明Uni4R在4D重建与点跟踪上达到SOTA，并在新提出的连续时间运动学感知基准上取得SOTA。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：本文针对统一4D重建与点跟踪这一前沿任务，提出新颖的最优传输+ODE融合方案，并解决了连续时间建模与训练监督的关键难题，实验达到SOTA。对于从事动态场景重建、点跟踪及相关方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing unified 4D reconstruction and point tracking approaches typically rely on heuristic interpolations or just predict at integer timestamps, lacking kinematic coherence and failing to model dynamics at any arbitrary timestamp. In this paper, we propose Uni4R, a framework that unifies these tasks by learning continuous velocity fields through the synergy of Optimal Transport (OT) and Ordinary Differential Equation (ODE). Importantly, this continuous velocity field acts as a kinematic prior that mutually benefits both 4D reconstruction and point tracking. Specifically, we propose the Flow Matching Guided Decoder (FMGD). A global velocity branch first extracts anchor features that capture the global dynamic state of the sequence. Then, FMGD leverages Flow Matching (FM) theory to formulate a probability path defined by OT on the anchor feature manifold, instantiating it as FM-guided velocity features for velocity prediction. This establishes a robust kinematic inductive bias. Meanwhile, a point reconstruction branch provides geometric features. The local velocity prediction module then joint above features and time embeddings, to decode velocities at arbitrary timestamps. To overcome the absence of high-quality ground-truth velocities in fractional frames, we propose an integral-consistency training strategy. This strategy uses an ODE solver to integrate velocities to recover target pointmaps, enabling the model to be supervised end-to-end directly from integer timestamps. Experimental results demonstrate that Uni4R achieves SOTA performance in both 4D reconstruction and point tracking, and achieves SOTA in our new kinematics-aware benchmark at continuous time.

</details>

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

## 3D Reconstruction & Multi-view Geometry

### 2026-08

#### 2026-08-10 - A Semantic Communication Approach to Fiducial Marker Processing in 5G-Enabled Edge SLAM

**Authors:** Boris Radovanovic, Vukan Ninkovic, Katarina Vidojevic, Buda Bajic Papuga, Dejan Vukobratovic
**Links:** [abs](https://arxiv.org/abs/2608.09620) - [pdf](https://arxiv.org/pdf/2608.09620)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Semantic Communication Approach to Fiducial Marker Processing in 5G-Enabled Edge SLAM
- 作者：Boris Radovanovic, Vukan Ninkovic, Katarina Vidojevic, Buda Bajic Papuga, Dejan Vukobratovic
- 出版日期：2026-08-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.09620

### 一句话总结
本文提出一种基于语义通信的标定标记（fiducial marker）处理框架，将深度网络在机器人与边缘服务器之间进行分割推理，并集成到5G使能的边缘SLAM系统中，以实现通信感知的任务卸载。

### 研究问题
如何在5G边缘SLAM场景下，通过语义通信实现标定标记检测任务的通信高效分割与部署，克服传统检测流水线难以进行有效任务划分的问题。

### 核心思路/方法
受DeepTag启发的卷积神经网络被分割部署在机器人端和边缘服务器端，中间层特征表示作为面向任务的语义信息通过无线链路传输。整个框架集成于ROS2机器人架构中，并在真实5G通信测试平台上进行性能评估。

### 主要贡献
- 提出面向标定标记处理的语义分割推理框架，支持任务导向的语义信息无线传输。
- 将框架集成到ROS2架构中，并在真实5G测试平台上完成验证。
- 通过实验展示关键点估计精度及其对下游位姿估计的影响。
- 量化不同分割点下的通信–计算权衡，为通信感知的深度视觉感知部署提供实践指导。

### 局限性
摘要未提供足够信息：摘要未明确提及具体局限性，例如对不同网络条件、多机器人协作场景或系统鲁棒性的讨论。

### 阅读优先级
**中**。理由：该工作面向机器人边缘计算与5G语义通信的交叉方向，具有较好的应用价值，但更偏向系统集成与权衡分析，而非提出全新的算法突破。若读者关注通信感知推理或边缘SLAM实践，可优先阅读；若仅关注视觉基础方法，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Autonomous robots increasingly rely on edge computing to offload computationally intensive perception tasks while maintaining real-time operation over 5G networks. However, conventional fiducial marker detection pipelines provide limited opportunities for efficient task partitioning, making them poorly suited for communication-aware edge deployment. This paper proposes a semantic split inference framework for fiducial marker processing in 5G-enabled Edge SLAM. A DeepTag-inspired convolutional neural network is partitioned between the robot and the edge server, where intermediate feature representations serve as task-oriented semantic information transmitted over the wireless link. The framework is integrated into a ROS2-based robotic architecture and characterized over a real 5G communication testbed. Experimental results demonstrate accurate keypoint estimation, illustrate the impact on downstream pose estimation, and quantify the communication--computation trade-offs associated with different split points, providing practical insights for communication-aware deployment of deep visual perception in connected robotic systems.

</details>

#### 2026-08-10 - You Only Flow Once: Calibrated and Real-Time Radar Pose Estimation with Multi-Hypothesis Normalizing Flows

**Authors:** Jonas Leo Mueller, Sebastian Hoefler, Dario Zanca, Naga Venkata Sai Jitin Jami, Thomas Altstidl, Bjoern M. Eskofier
**Links:** [abs](https://arxiv.org/abs/2608.09579) - [pdf](https://arxiv.org/pdf/2608.09579)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：You Only Flow Once: Calibrated and Real-Time Radar Pose Estimation with Multi-Hypothesis Normalizing Flows
- 作者：Jonas Leo Mueller, Sebastian Hoefler, Dario Zanca, Naga Venkata Sai Jitin Jami, Thomas Altstidl, Bjoern M. Eskofier
- 出版日期：2026-08-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.09579

### 一句话总结
本文提出基于条件归一化流的多假设雷达姿态估计方法MH-NFPG，在保持校准不确定性的同时实现实时推理，性能超越扩散模型。

### 研究问题
稀疏且含噪的毫米波雷达点云通常对应多种合理的人体姿态，导致确定性姿态估计存在本质上的不适定性；现有雷达方法多为确定性估计，无法处理多模态歧义，而扩散模型虽能建模多假设分布但推理成本高且缺乏校准的不确定性。

### 核心思路/方法
将条件归一化流与时空Transformer骨干结合：Transformer提取雷达点云时空特征，条件归一化流将Laplace基分布变换为表达力强的后验分布，通过单次前向传播并行生成多个姿态假设，从而以低推理成本获得多模态分布并支持校准的不确定性估计。

### 主要贡献
- 提出MH-NFPG：首个面向雷达姿态估计的多假设归一化流方法，兼具多模态建模与单次前向推理效率。
- 在三个雷达基准（MM-Fi、mmRadPose、mRI）上超越扩散模型的校准性能，并在两个数据集上提升姿态精度，第三个数据集精度持平。
- 推理速度比扩散模型快20倍以上，校准误差最高降低85%。
- 发现扩散模型在校准上显著退化，而基于流的方法在跨环境设置下仍保持可靠覆盖率。

### 局限性
摘要未提供足够信息。例如：未提及方法在极端噪声、遮挡或训练数据规模有限时的表现，也未讨论模型参数量、显存开销或失败案例。

### 阅读优先级
**优先级：中**。理由：该方法在雷达姿态估计任务上展示了归一化流对扩散模型的计算效率与校准优势，对关注实时不确定性感知姿态估计的研究者有参考价值；但若你不是该子领域（毫米波雷达人体姿态估计）从业者，或更关注通用生成模型方法论，则与本工作的直接相关性有限。

</details>

<details>
<summary>Abstract</summary>

Sparse and noisy millimeter-wave radar point cloud observations often correspond to multiple plausible human poses, making deterministic pose estimation fundamentally ill-posed. Yet existing radar methods remain deterministic, collapsing this ambiguity into a single estimate. Diffusion-based alternatives can model multi-hypothesis distributions but require costly sequential denoising for each distribution sample and lack calibrated uncertainty. We propose Multi-Hypothesis Normalizing Flow Pose Generator (MH-NFPG), which models pose distributions from radar point clouds using a conditional normalizing flow. Specifically, we combine a spatiotemporal transformer backbone with a normalizing flow that transforms a Laplace base distribution into an expressive posterior, generated in parallel through a single forward pass. Leveraging this efficiency, we outperform diffusion-based alternatives in calibration across three radar benchmarks (MM-Fi, mmRadPose, mRI), improve pose accuracy on two, and match it on the third, while achieving over 20x faster inference for applications and reducing calibration error by up to 85%. We find that calibration degrades substantially for diffusion models, whereas our flow-based approach maintains reliable coverage, also in cross-environment settings. These results demonstrate normalizing flows as a practical alternative to diffusion models for real-time, uncertainty-aware radar pose estimation. Our code will be made publicly available.

</details>

#### 2026-08-10 - A Height-Constrained 2-Point Minimal Solver for Pose Estimation from Active LED Markers with Event Cameras

**Authors:** Runze Yuan, Alexander Kappler, Jun Zhang, Kuangyi Chen, Fabio Morbidi, Pascal Vasseur, Cédric Demonceaux, Friedrich Fraundorfer
**Links:** [abs](https://arxiv.org/abs/2608.09520) - [pdf](https://arxiv.org/pdf/2608.09520)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Height-Constrained 2-Point Minimal Solver for Pose Estimation from Active LED Markers with Event Cameras
- 作者：Runze Yuan, Alexander Kappler, Jun Zhang, Kuangyi Chen, Fabio Morbidi, Pascal Vasseur, Cédric Demonceaux, Friedrich Fraundorfer
- 出版日期：2026-08-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.09520

### 一句话总结
本文提出一种利用事件相机和主动LED标记，结合已知倾角和相机高度信息，仅用两个标记点即可求解相机位姿的最小解算器，并在合成与真实数据上验证了其精度优于现有P2P方法。

### 研究问题
在空间受限场景中，如何利用事件相机与主动LED标记，在仅有两个标记点可用的情况下，结合机载传感器（如IMU或高度计）提供的倾角与高度信息，实现稳健且精确的相机位姿估计。

### 核心思路/方法
- 将已知的倾斜角（重力方向）和相机高度作为约束引入位姿估计问题。
- 推导出仅需两个LED标记点的最小解算公式，提供闭式解和线性最小二乘解两种形式。
- 对退化配置进行分析，明确高度信息在何种条件下无法对旋转估计产生贡献。
- 构建了一个基于事件相机的主动标记系统，使用动作捕捉系统提供真实值进行实际数据评估。

### 主要贡献
- 提出了一种仅使用两个LED标记的位姿估计最小解算器，突破了传统PnP方法对标记点数量的依赖。
- 推导了闭式解与线性最小二乘解两种求解途径。
- 分析了退化配置，给出了高度信息失效的条件。
- 在合成与真实数据上验证了方法，精度优于现有P2P求解器，与P3P方法性能相当。

### 局限性
摘要未提供足够信息。摘要未提及方法在极端退化情况下的具体表现、对传感器噪声的敏感度、计算开销对比，以及方法在动态场景或标记遮挡情况下的鲁棒性。

### 阅读优先级
**中**。理由：该工作针对特定硬件配置（事件相机+主动LED标记）下的位姿估计问题提出了新颖的最小解算器，在方法上有理论贡献和实验验证，适合关注事件相机位姿估计或主动标记定位系统的研究者阅读。但由于应用场景较为垂直，且未涉及更广泛通用视觉任务，对一般视觉研究者而言优先级为中。

</details>

<details>
<summary>Abstract</summary>

In many autonomous applications requiring real-time localization, active marker-based systems are preferred due to their low latency and ease of deployment compared to computationally demanding feature-based methods. Event~\mbox{cameras} offer high temporal resolution and minimal delay and are commonly used with active LED markers for robust real-time localization. Existing methods typically rely on Perspective-n-Point (PnP) solvers for pose estimation. However, structured marker layouts can be challenging to deploy in space-constrained scenarios, while partial self-motion information (e.g., gravity direction and altitude) is readily available from onboard sensors. We derive a robust and accurate minimal solver that estimates camera pose from only two LED markers by incorporating known tilt angle and camera height measured by an onboard sensor, such as an IMU or an altimeter. The proposed formulation uniquely determines the camera pose through both a closed-form and a linear least-squares solution. We further analyze degenerate configurations and characterize the conditions under which height information does not contribute to rotation estimation. For evaluation, we developed an event-based active marker system to collect real-world data with ground truth from a motion capture system. Experiments on both synthetic and real data demonstrate improved accuracy over the state-of-the-art P2P solver and competitive performance relative to P3P.

</details>

#### 2026-08-10 - CableDex: Cable Length Estimation on Industrial Reels Using a Handheld Device

**Authors:** Francisco Guillén, Ricardo Almeida, Bruno Silva, João C. Neves
**Links:** [abs](https://arxiv.org/abs/2608.09392) - [pdf](https://arxiv.org/pdf/2608.09392)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CableDex: Cable Length Estimation on Industrial Reels Using a Handheld Device
- 作者：Francisco Guillén, Ricardo Almeida, Bruno Silva, João C. Neves
- 出版日期：2026-08-10T10:19:52Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.09392

### 一句话总结
CableDex 是一个基于手机单张照片的计算机视觉系统，通过相机标定、实例分割、姿态估计和体积计算，在多种工业卷轴上自动估算电缆长度，平均绝对百分比误差为 4.90%。

### 研究问题
如何利用手持设备（手机）拍摄的单张照片，快速且准确地估算工业卷轴上电缆的长度，以替代耗时且不准确的人工测量方式。

### 核心思路/方法
系统流程包含四个关键步骤：相机标定、实例分割、姿态估计和体积计算。具体而言，使用基于 1,000 张人工标注图像训练的实例分割模型（推理时间 5.66 ms/张，mAP50 为 99.5%），结合标定与姿态信息，对五种卷轴类型和多种电缆尺寸进行长度估计。最终以移动应用形式呈现端到端流程，包括卷轴标签扫描、图像采集、分割和长度估算。

### 主要贡献
1. 提出了一个从单张手机照片估计工业卷轴电缆长度的完整视觉系统。
2. 系统覆盖五种卷轴类型和多种电缆尺寸，具备一定的通用性。
3. 在 75 个卷轴上的评估中，MAPE 达到 4.90%，满足工业界普遍接受的 10% 误差容忍范围。
4. 提供了可运行的移动应用端到端演示流程。

### 局限性
摘要未提供足够信息。具体局限性（如对光照、遮挡、极端卷轴类型的鲁棒性，以及不同手机型号的泛化能力）在摘要中未提及。

### 阅读优先级
**中**。理由：该工作面向特定工业场景（电缆长度测量），方法组合了多个成熟计算机视觉组件（分割、姿态、标定），创新点可能集中在系统集成与工程应用层面；对于从事工业视觉测量或移动端部署的读者有一定参考价值，但若关注底层算法突破，优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

CableDex is a computer vision system that addresses the time-consuming and inaccurate manual measurement of cable length on industrial reels from a single photograph captured with a mobile phone. The system combines camera calibration, instance segmentation, pose estimation, and volumetric calculation to estimate the cable length across five different reel types and various cable sizes. This system is based on an instance segmentation model trained on 1,000 manually annotated images, achieving 99.5\% mAP50 with an inference time of 5.66 ms per image. Evaluated on 75 reels across five reel types, the system achieves a MAPE of 4.90\%, within the 10\% error tolerance commonly accepted in industrial cable-reel measurement. The demonstration presents the end-to-end pipeline, from reel label scanning and image capture to segmentation and length estimation, through the mobile application.

</details>

#### 2026-08-10 - Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

**Authors:** Tianchen Deng, Chongdi Wang, Nailin Wang, Lei Zhao, Ziqi Ma, Tianjun Zhang, Zhe Liu, Danwei Wang, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2608.09146) - [pdf](https://arxiv.org/pdf/2608.09146)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, SLAM, pose estimation, NeRF, radiance, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction（基于多子图与局部到全局回环检测的大规模场景重建隐式神经SLAM）
- 作者：Tianchen Deng, Chongdi Wang, Nailin Wang, Lei Zhao, Ziqi Ma, Tianjun Zhang, Zhe Liu, Danwei Wang, Hesheng Wang
- 出版日期：2026-08-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2608.09146 ；PDF https://arxiv.org/pdf/2608.09146

### 一句话总结
本文提出一种基于多子图架构和双层回环检测机制的大规模神经SLAM系统，通过渐进式映射、光流跟踪和跨子图在线蒸馏，在保持内存可控的同时提升重建质量与定位鲁棒性。

### 研究问题
如何将基于NeRF的神经SLAM方法从适用于小规模场景扩展到大规模、复杂环境，解决现有方法面临的灾难性遗忘和轨迹累积漂移问题。

### 核心思路/方法
- 采用多子图架构，通过渐进式映射策略动态分配神经子图，在保持高保真重建的同时避免内存爆炸。
- 集成基于光流的跟踪模块，增强对剧烈运动的位姿估计鲁棒性。
- 设计局部到全局的闭环框架，利用基础模型提取全局描述子，提升不同视角下的重定位精度。
- 在后端优化阶段设计跨子图在线蒸馏算法，强制重叠子图边界在几何和外观上保持一致。

### 主要贡献
- 提出一种可扩展的大规模神经SLAM系统，采用多子图架构以解决大规模场景中的灾难性遗忘与累积漂移。
- 设计渐进式映射策略实现动态子图分配，在不导致内存爆炸的前提下维持高保真场景表示。
- 引入基于光流跟踪的鲁棒位姿估计模块，适用于剧烈运动场景。
- 提出局部到全局的双层回环机制，借助基础模型提升跨视角重定位精度。
- 提出跨子图在线蒸馏算法，保障重叠子图边界处的几何与外观一致性。
- 开发了定制手持机电平台，并在公开基准及自建大规模室内外数据集上验证系统有效性，包括在板载计算单元上的直接部署。

### 局限性
摘要未提供足够信息。摘要未明确说明方法的失败案例、对计算资源的具体需求、不同场景下的性能边界或与其他方法对比的量化差距。

### 阅读优先级
**高**

理由：该工作针对神经SLAM领域的关键瓶颈（大规模场景的可扩展性与全局一致性）提出系统性解决方案，涉及多子图架构、回环检测、在线蒸馏等多个新颖模块，并通过自建平台与多种数据集验证，同时承诺开源代码，对从事3D重建、SLAM和机器人感知的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture and a dual-tier loop closure mechanism. Specifically, we propose a progressive mapping strategy that dynamically allocates neural submaps to maintain high-fidelity representations without memory explosion. For robust pose estimation, an optical-flow-based tracking module is integrated to handle aggressive motions. To address global consistency, we introduce a local-to-global loop closure framework leveraging the foundation model for high-performance global descriptor extraction, significantly enhancing relocalization accuracy under varying viewpoints. Furthermore, an inter-submap online distillation algorithm is designed during back-end optimization to enforce geometric and appearance consistency across overlapping submap boundaries. To validate the system, we developed a customized handheld mechatronic platform and conducted extensive evaluations on both public benchmarks and our large-scale indoor-outdoor datasets. Experimental results, including direct deployment on an onboard computing unit, demonstrate that our approach outperforms state-of-the-art neural SLAM methods in reconstruction quality and localization robustness, providing a scalable solution for real-world robotic perception and digital twinning. We will release the code publicly on \href{https://github.com/dtc111111/MSN-SLAM}{https://github.com/dtc111111/MSN-SLAM} .

</details>

#### 2026-08-10 - ROEVO: Robust Organized Edge Feature-based Visual Odometry Using RGB-D Cameras

**Authors:** Mingrui Liu, Xingxing Zuo, Renlang Huang, Minglei Zhao, Jiming Chen, Liang Li
**Links:** [abs](https://arxiv.org/abs/2608.09112) - [pdf](https://arxiv.org/pdf/2608.09112)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, bundle adjustment, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ROEVO: Robust Organized Edge Feature-based Visual Odometry Using RGB-D Cameras
- 作者：Mingrui Liu, Xingxing Zuo, Renlang Huang, Minglei Zhao, Jiming Chen, Liang Li
- 出版日期：2026-08-10
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.09112

### 一句话总结
本文提出一种仅依赖边缘特征的RGB-D视觉里程计系统ROEVO，通过将分散边缘像素组织为“有序边缘”簇，实现跨帧边缘级关联与联合优化，在室内场景中达到或超越现有最先进方法的精度与鲁棒性。

### 研究问题
如何更有效地利用图像边缘特征进行视觉里程计估计，以克服现有基于边缘的VO方法对纹理和结构信息利用不充分的问题。

### 核心思路/方法
- 提出“有序边缘”（organized edges）特征表示，将分散的边缘像素转化为序列化簇，保留更丰富的纹理与结构信息。
- 利用有序边缘的跨帧边缘级关联，构建共视图（co-visibility graph）。
- 跟踪阶段：采用边缘级（而非像素级）残差进行帧间配准，提升鲁棒性与精度。
- 联合优化：提出保形边缘拟合方法及基于有序边缘的Bundle Adjustment（BA），将传统BA分解为拟合与配准两个子问题，保持结构完整性。
- 基于上述技术构建仅使用有序边缘特征的完整VO系统，实现高效跟踪与精确局部建图。

### 主要贡献
- 提出“有序边缘”这一新颖特征表示，提升边缘特征的利用效率。
- 实现边缘级跨帧关联与共视图构建。
- 设计边缘级残差跟踪方法、保形边缘拟合方法及有序边缘BA，显著提升位姿估计精度与效率。
- 开发了完整的、仅依赖边缘特征的VO系统，并在室内环境中验证其准确性与鲁棒性（代码已公开）。

### 局限性
摘要未提供足够信息。摘要仅提及实验在室内环境验证，未说明户外、动态场景、光照变化等条件下的表现，也未给出计算开销、运行时间或具体误差数据。

### 阅读优先级
**中**。理由：该方法在边缘特征表示和优化策略上有明确创新，且代码开源，适合从事视觉里程计或SLAM的研究者参考；但摘要未提供定量实验结果，实际性能需通过论文正文或代码进一步验证，故优先级为中。

</details>

<details>
<summary>Abstract</summary>

This work presents a visual odometry (VO) system that leverages image edge features. Edges are spatially expressive cues commonly present across diverse environments, offering rich textural and structural information. However, existing edge-based VO methods often fail to fully exploit this potential. To this end, we introduce a novel feature representation termed \textit{organized edges}, which transforms disjoint edge pixels into sequentialized clusters, enabling more effective retention and utilization of the underlying textural and structural information. Another nice property of this formulation is that organized edges can perform edge-level association across multiple frames, enabling the establishment of a co-visibility graph. To achieve precise and efficient pose estimation, we propose a range of particularly designed tracking and joint optimization methods based on the characteristics of organized edges. For tracking, we formulate edge-wise rather than pixel-wise residuals to achieve robust and accurate inter-frame registration. For joint optimization, we introduce a novel shape-preserving edge-fitting method and an organized edge-based Bundle Adjustment (BA) approach, which decomposes the traditional BA problem into fitting and registration to preserve the structural integrity. Based on these novel techniques, we develop a complete VO system that exclusively employs organized edge features, achieving efficient tracking and precise local mapping. Extensive experiments demonstrate its accuracy and robustness in indoor environments, outperforming or achieving comparable performance to state-of-the-art methods. The source code is publicly available at https://github.com/liumingrui814/ROEVO

</details>

#### 2026-08-09 - EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams

**Authors:** Zixuan Chen, Jiakai Zhang, Junhao Dong, Guangcong Wang, Jianhuang Lai, Yew-Soon Ong, Xiaohua Xie
**Links:** [abs](https://arxiv.org/abs/2608.08585) - [pdf](https://arxiv.org/pdf/2608.08585)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, SLAM, pose estimation, geometric reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams
- 作者：Zixuan Chen, Jiakai Zhang, Junhao Dong, Guangcong Wang, Jianhuang Lai, Yew-Soon Ong, Xiaohua Xie
- 出版日期：2026-08-09
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：https://arxiv.org/abs/2608.08585

### 一句话总结
本文提出EvTrajGS框架，通过将相机运动参数化为连续时间轨迹并借助损失重加权的事件采样策略，实现了从无位姿事件流中进行高精度、高效率的3D高斯重建与位姿联合优化。

### 研究问题
如何在不使用SLAM式增量跟踪与建图流水线（计算开销大）的前提下，仅从无位姿（unposed）事件流中实现高精度且高计算效率的3D重建与相机位姿估计，以解决传统方法中位姿初始化不准确导致累积重建误差的问题。

### 核心思路/方法
- 以连续时间轨迹参数化相机运动，轨迹由离散相机位姿初始化，统一表示位姿优化。
- 将相邻轨迹状态聚合为时间耦合位姿，在联合优化中促进时间一致的位姿更新。
- 引入损失重加权的事件采样策略，自适应强调时间上重建不足的区间。
- 整体框架从粗略位姿先验出发进行可靠的位姿-场景联合优化，无需SLAM式管线。

### 主要贡献
- 提出EvTrajGS，一个面向无位姿事件流的准确且高效的3D高斯溅射框架。
- 利用连续时间轨迹联合表示与优化位姿与场景，避免SLAM式高计算开销。
- 提出时间耦合位姿聚合与损失重加权事件采样策略，提升重建质量与位姿精度。
- 在合成与真实数据集上，相较SOTA方法，PSNR提升3.8 dB，SSIM提升0.1，ATE RMSE降低超40%，同时保持高计算效率。

### 局限性
摘要未提供足够信息（如对高动态范围、极端光照、内存占用、大规模场景适应性、失败案例或对初始位姿质量的敏感性等均未说明）。

### 阅读优先级
**高**

理由：该工作针对事件相机3D重建中长期存在的“精度-效率”权衡问题，提出了不依赖SLAM管线的联合优化方案，在重建质量和位姿精度上均有显著提升（PSNR和ATE指标的大幅改进），且属于2026年较新的论文。题目与摘要均显示方法创新点明确、实验验证充分，适合关注事件相机、3D高斯溅射或神经场景表示的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Event cameras, with high temporal resolution, high dynamic range, and asynchronous sensing characteristics, have shown great potential for dense 3D reconstruction. Traditional reconstruction methods based on off-the-shelf pose estimates achieve high efficiency but produce low-fidelity results, as inaccurate pose initialization introduces cumulative reconstruction errors. In contrast, recent SLAM-style methods stabilize joint pose-scene optimization through incremental tracking and mapping, yielding higher reconstruction fidelity at the expense of considerable computational overhead. To address this trade-off, this paper presents EvTrajGS, an accurate and efficient 3D Gaussian Splatting framework for unposed event streams. Our method enables reliable joint pose-scene optimization initialized from coarse pose priors, eliminating the need for computationally expensive SLAM-style pipelines. EvTrajGS parameterizes camera motion as a continuous-time trajectory initialized from discrete camera poses, providing a unified representation for pose refinement. We then aggregate adjacent trajectory states into a temporally coupled pose, promoting temporally consistent pose updates during joint optimization. Additionally, we introduce a loss-reweighted event sampling strategy to adaptively emphasize temporally under-reconstructed intervals. Extensive experiments on both synthetic and real-world datasets demonstrate that EvTrajGS outperforms state-of-the-art methods in terms of both geometric reconstruction quality and pose estimation accuracy, achieving 3.8 dB higher PSNR, 0.1 higher SSIM, and over 40\% lower ATE RMSE while retaining high computational efficiency.

</details>

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

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-10 - View-Adaptive Renderer for View-Consistent 2D-to-3D Generation

**Authors:** U-Chae Jun, Jaeeun Ko, Jiwoo Kang
**Links:** [abs](https://arxiv.org/abs/2608.09110) - [pdf](https://arxiv.org/pdf/2608.09110)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, NeRF, neural radiance field, radiance field, neural rendering, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：View-Adaptive Renderer for View-Consistent 2D-to-3D Generation
- 作者：U-Chae Jun, Jaeeun Ko, Jiwoo Kang
- 出版日期：2026-08-10
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.09110

### 一句话总结
本文提出一种视图自适应神经渲染框架，通过视图自适应渲染器和自注意力融合模块，在部分不一致的多视图输入下实现鲁棒且高效的3D重建，无需依赖扩散模型SDS监督。

### 研究问题
从单张图像重建3D形状时，传统方法先合成多视图再进行NeRF重建，但视图间的投影歧义会导致生成视角不连续，进而影响重建精度。现有解决方案要么计算开销大，要么无法充分解决合成视图间的实际不一致性问题。

### 核心思路/方法
- 提出**视图自适应神经渲染器**：独立修正各视图的视角相关误差，同时共享全局特征骨干以保持结构一致性。
- 设计**自注意力融合模块**：自适应整合多视图信息，确保几何一致性，避免依赖间接正则化或高计算量方法。
- 训练主要依靠**光度渲染损失**和轻量注意力正则化，而非扩散模型的SDS监督。

### 主要贡献
- 提出一种新型视图自适应渲染框架，能够应对部分不一致的多视图输入。
- 通过视图自适应渲染器与全局特征共享机制，兼顾局部修正与全局结构保持。
- 引入自注意力融合模块，在不需要重型正则化的情况下提升几何一致性。
- 实验表明在重建保真度上持续改进，且以较低计算成本达到接近当前最优的性能。

### 局限性
摘要未提供足够信息：未提及具体实验数据集、与其他方法的定量对比细节、失败案例、计算资源需求、以及框架对输入不一致程度的具体鲁棒性边界。

### 阅读优先级
**中**。理由：该工作针对2D到3D重建中视图不一致这一具体痛点，提出了轻量化的解决方案，对NeRF/3D生成方向有一定参考价值。但摘要未给出充分的实验细节和新颖性证明，且未与主流SDS类方法直接对比，因此优先级设为中等。若您专注于高效3D重建或无扩散监督方法，可适当上调关注。

</details>

<details>
<summary>Abstract</summary>

Reconstructing 3D shapes from a single image remains a fundamental yet challenging problem in computer vision. Traditional monocular 3D generation pipelines typically synthesize multiple views from a single input image before applying Neural Radiance Field (NeRF)-based reconstruction. However, inherent projective ambiguities often produce visual discontinuities across generated viewpoints, leading to inaccuracies in reconstructed 3D models. Current solutions either incur significant additional computational burdens or fail to adequately resolve practical inconsistencies between synthesized views. To address these limitations, we propose a novel viewpoint-adaptive neural rendering framework that enables robust 3D reconstruction even when given partially inconsistent multi-view inputs. Our approach introduces view-adaptive neural renderers that independently correct viewpoint-dependent errors while simultaneously sharing a global feature backbone to preserve structural coherence. Furthermore, we propose a self-attention fusion module that adaptively integrates multi-view information, ensuring geometric consistency without relying heavily on indirect regularizations or computationally intensive methods. Through extensive experiments, we demonstrate that our method consistently improves 3D reconstruction fidelity. Importantly, our approach achieves near state-of-the-art performance without diffusion-based SDS supervision, relying primarily on photometric rendering loss with lightweight attention regularizers. This balance between accuracy and efficiency makes the proposed framework highly practical for real-world applications.

</details>

#### 2026-08-09 - JSGS: JPEG State-Guided Supervision for 3D Gaussian Splatting from Mixed-Quality Views

**Authors:** Jinhua Cui, Anhong Wang, Kai Hu, Donghan Bu, Peihao Li, Tammam Tillo, Hao Jing, Shiao Xu
**Links:** [abs](https://arxiv.org/abs/2608.08659) - [pdf](https://arxiv.org/pdf/2608.08659)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JSGS: JPEG State-Guided Supervision for 3D Gaussian Splatting from Mixed-Quality Views
- 作者：Jinhua Cui, Anhong Wang, Kai Hu, Donghan Bu, Peihao Li, Tammam Tillo, Hao Jing, Shiao Xu
- 出版日期：2026-08-09
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.08659

### 一句话总结
JSGS提出利用JPEG文件中的量化表构建视角特定的JPEG观测算子，为混合质量视图下的3D高斯泼溅提供状态引导监督，从而在保持实时渲染的同时提升重建质量。

### 研究问题
标准3D高斯泼溅（3DGS）假设所有输入图像真实采样场景辐射，但混合质量的JPEG图像因压缩产生的块效应和振铃伪影会破坏跨视图共享高斯的更新。研究问题是如何在混合JPEG质量输入下，有效抑制压缩伪影对3DGS训练的干扰并提升重建质量。

### 核心思路/方法
- 利用每个JPEG文件中的亮度和色度量化表，构造视角特定的JPEG观测算子。
- 该算子对每个渲染视图进行编码-解码，使其与对应的解码输入图像在域上匹配比较。
- 亮度量化表在固定的中频带内提供连续权重；低频损失锚定粗糙结构，加权中频损失在所选DCT坐标上重新分配监督。
- 块不一致性还引导高斯控制器在分歧区域正则化具有高不透明度的小图元。

### 主要贡献
- 提出JPEG状态引导监督框架（JSGS），利用JPEG量化表构造域匹配的观测算子。
- 设计了结合低频锚定和中频加权损失的监督机制，有效应对混合质量JPEG输入。
- 在7个场景、3种混合质量计划下，均取得最低平均LPIPS和最高平均SSIM，同时渲染速度约为150 FPS。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对3DGS在实际应用中常见的混合质量JPEG输入问题提出专门解决方案，实验在多个场景和计划下表现一致优异，方法具有明确实用价值，且开源代码，可作为相关方向的重要参考。

</details>

<details>
<summary>Abstract</summary>

Standard 3D Gaussian Splatting (3DGS) assumes that every input image faithfully samples scene radiance. However, mixed-quality JPEG images violate this assumption because compression-induced blocking and ringing artifacts can corrupt updates to Gaussians shared across views. To address this problem, we propose JPEG State-Guided Supervision for 3D Gaussian Splatting from Mixed-Quality Views (JSGS). JSGS uses luminance and chrominance quantization tables stored in each JPEG file to construct a view-specific JPEG observation operator. This operator encodes and decodes each rendered view for domain-matched comparison with the corresponding decoded input image. The luminance quantization table supplies continuous weights within a fixed middle frequency band. A loss in the low frequency band anchors coarse structure, while the weighted middle frequency loss redistributes supervision among the selected DCT coordinates. The resulting block disagreement also guides the Gaussian Controller to regularize small primitives with high opacity in disagreement regions. Across seven scenes and three mixed-quality schedules, JSGS achieves the lowest mean LPIPS and the highest mean SSIM under every schedule while rendering at approximately 150 FPS. Code: https://github.com/Jayden-Cui/JSGS.

</details>

#### 2026-08-09 - ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints

**Authors:** Xiaoyang Bai, Zhenyang Li, Weiwei Xu, Edmund Y. Lam, Yifan Peng
**Links:** [abs](https://arxiv.org/abs/2608.08531) - [pdf](https://arxiv.org/pdf/2608.08531)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic 3D, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints
- 作者：Xiaoyang Bai, Zhenyang Li, Weiwei Xu, Edmund Y. Lam, Yifan Peng
- 出版日期：2026-08-09
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.08531

### 一句话总结
提出一种将事件相机信息融入3D高斯泼溅优化与致密化阶段的融合框架，用于从稀疏、模糊的RGB与事件数据中重建快速运动场景。

### 研究问题
基于传统帧式视频的动态三维重建方法在处理快速运动物体时性能受限，如何在事件相机辅助下，从低帧率、严重运动模糊且RGB与事件视角不重合的真实场景中重建快速运动。

### 核心思路/方法
提出ERF-GS框架，将事件信息同时集成到3D高斯泼溅的优化阶段和致密化阶段中。事件传感器提供高帧率信息，且在训练中实现事件分支与RGB输入解耦，即事件学习不依赖RGB分支。模型基于现实仿真设置开发，适用于布局复杂、低帧率和强运动模糊的自然视频。

### 主要贡献
- 提出事件-RGB融合高斯泼溅框架，将事件信息整合进优化和致密化两个核心环节。
- 实现事件分支学习与RGB输入解耦，拓展了方法在自然视频中的适用性，而不仅限于合成数据。
- 在Neu3D和Nvidia数据集的不同变体上（含模糊RGB帧和不重合的RGB-事件视角）优于4DGS基线和同期E-D3DGS方法。

### 局限性
摘要未提供足够信息（未具体说明失败场景、对事件传感器分辨率/同步的依赖程度、计算开销等）。

### 阅读优先级
**中**。理由：该方法针对动态场景重建中快速运动这一具体难点，且在与同期方法对比中表现更好，并公开代码，对从事事件视觉或动态三维重建的研究者有一定参考价值；但应用场景相对聚焦，且摘要中未给出充分的性能细节和局限讨论，非该领域读者可暂缓精读。

</details>

<details>
<summary>Abstract</summary>

Deep learning-driven representations such as neural radiance fields (NeRFs) and 3D Gaussian splatting (3DGS) have revolutionized the field of dynamic 3D scene reconstruction with improved visual precision and scalability. However, the reconstruction of fast-moving objects remains a challenge; existing methods based on conventional frame-based videos often struggle in scenarios such as sports events and animal videography. We propose an event-RGB fusion Gaussian splatting (ERF-GS) framework that integrates event information into both optimization and densification stages of the Gaussian splatting pipeline, taking advantage of novel event sensors with high frame-rate. Unlike many other event-assisted scene reconstruction methods, ERF-GS was developed using realistic simulation settings and realizes event-based learning detached from RGB inputs. This design enables its application beyond straightforward synthetic data into the realm of natural video with complex layout, low frame rates and severe motion blur. Our experiments show that ERF-GS outperforms both the 4DGS baseline and the concurrent E-D3DGS on different variants of the Neu3D and Nvidia datasets which include blurry RGB frames and disjoint RGB-event viewpoints. Our code is available at https://github.com/andrewbxy/ERF-GS.

</details>

#### 2026-08-09 - DoRF++: Spherical Representation Learning over Doppler Radiance Fields for Robust Wi-Fi Sensing

**Authors:** Navid Hasanzadeh, Shahrokh Valaee
**Links:** [abs](https://arxiv.org/abs/2608.08381) - [pdf](https://arxiv.org/pdf/2608.08381)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DoRF++: Spherical Representation Learning over Doppler Radiance Fields for Robust Wi-Fi Sensing
- 作者：Navid Hasanzadeh, Shahrokh Valaee
- 出版日期：2026-08-09T00:23:55Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.08381

### 一句话总结
本文将神经辐射场（NeRF）思想引入Wi-Fi感知，提出DoRF++方法，通过球面表示学习对Doppler速度投影建模，实现跨用户鲁棒的手势识别。

### 研究问题
如何提升Wi-Fi信道状态信息（CSI）驱动的无设备人体活动识别（HAR）在真实世界跨用户、跨场景条件下的泛化鲁棒性，尤其是针对困难手势的识别准确率。

### 核心思路/方法
- 从Wi-Fi CSI中提取多普勒速度投影，将其视为人体运动的稀疏、多样“虚拟相机视图”；
- 引入**Doppler Radiance Fields (DoRF)**，推断潜在3D运动序列，其沿学习到的有效多普勒方向的投影能解释CSI-derived多普勒观测；
- 将恢复的运动投影到单位球面上的等角方向网格，生成球面运动表示；
- 提出**DoRF++**，使用球面Transformer对该球面表示进行分类，完成活动识别。

### 主要贡献
- 首次将NeRF概念引入Wi-Fi感知，提出DoRF框架，将CSI多普勒观测建模为虚拟相机投影；
- 提出球面表示学习方法DoRF++，结合球面Transformer实现活动分类；
- 在自采手势数据集上，跨用户泛化准确率显著优于现有Wi-Fi HAR方法，尤其在单多天线接收AP条件下对困难手势表现突出。

### 局限性
摘要未提供足够信息。摘要仅报告了在自采数据集上的实验结果，未提及方法在更多样环境、更多用户规模、不同硬件配置下的验证情况，也未讨论计算开销、实时性等实际部署因素。

### 阅读优先级
**高**
理由：该工作将NeRF从视觉领域迁移至无线感知，方法新颖且针对IEEE 802.11bf标准化背景下的实际痛点（跨用户泛化）提出解决方案，并展示了显著性能提升，对Wi-Fi感知和神经场景表示交叉领域的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Motivated by the IEEE 802.11bf effort to standardize advanced WLAN sensing, interest in Wi-Fi Channel State Information (CSI) for passive, device-free, and privacy-preserving activity and gesture recognition has grown rapidly. Recent studies have shown that Doppler velocity projections extracted from CSI, which directly reflect human-motion velocity, enable more robust human activity recognition (HAR) and stronger generalization across users and unseen conditions. Nevertheless, reliable generalization under real-world variability remains a major challenge, hindering the adoption of Wi-Fi sensing in real-world applications. To address this challenge, we introduce Doppler Radiance Fields (DoRF), bringing the concept of neural radiance fields (NeRF) from computer vision into Wi-Fi sensing. DoRF models Doppler velocity projections extracted from Wi-Fi CSI as sparse and diverse virtual-camera views of human motion. It then infers a latent 3D motion sequence whose projections along learned effective Doppler directions explain the CSI-derived Doppler observations. The recovered motion is subsequently projected onto an equiangular grid of directions on the unit sphere, producing a spherical representation of the underlying motion. Since DoRF naturally defines the Doppler representation on spheres, we further introduce DoRF++, a spherical-learning design that applies spherical Transformers for activity classification. Experiments on our collected hand-gesture dataset show that DoRF++ significantly outperforms state-of-the-art Wi-Fi-based HAR methods in cross-user generalization accuracy, especially for difficult gestures in settings with a single multi-antenna receiver access point (AP).

</details>

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

## Embodied / Robotics / AR Applications

### 2026-08

#### 2026-08-10 - SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation

**Authors:** Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen, Jingjiao Zhao, Xiansheng Chen, Pengwei Wang, Lemao Liu, Dejing Dou
**Links:** [abs](https://arxiv.org/abs/2608.09771) - [pdf](https://arxiv.org/pdf/2608.09771)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation
- 作者：Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen, Jingjiao Zhao, Xiansheng Chen, Pengwei Wang, Lemao Liu, Dejing Dou
- 出版日期：2026-08-10T15:58:39Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.09771

### 一句话总结
本文提出一种仅0.5B参数的紧凑型机器人操作策略SLIM，通过自监督学习动作相关的潜在动态表征，在减少计算资源的同时匹配或超越大型VLA基线的性能。

### 研究问题
如何在不依赖大规模多模态骨干网络和额外具身预训练的情况下，学习紧凑且有效的动作相关潜在表征，以支持语言条件下的机器人连续操作。

### 核心思路/方法
- 提出SLIM（Self-supervised Latent Interaction Model），一种0.5B参数的潜在交互策略。
- 学习“动作锚定的预测性潜在表征”（action-grounded predictive latents），同时捕获动作条件化的未来状态转移，以及能够解释观测变化的动作。
- 采用自监督掩码轨迹预测，结合动作重建与未来潜在预测两个目标进行表征学习。
- 使用紧凑的Mixture-of-Transformers（MoT）骨干网络建模观测潜在与动作token之间的交互。
- 最终策略通过流匹配（flow matching）训练，实现语言条件下的动作生成。

### 主要贡献
- 提出一种紧凑的0.5B参数潜在交互策略，避免大型多模态骨干网络带来的计算开销。
- 设计自监督掩码轨迹预测方法，使模型学习动作与观测变化之间的因果关系。
- 在仿真基准和真实机器人评估中，以更少的参数、更低的推理延迟和GPU内存占用，匹配或超越代表性大型VLA和世界动作模型基线，且无需额外具身预训练。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法的适用边界、失败案例、泛化场景限制或计算复杂度对比的具体数值。

### 阅读优先级
**高**。理由：该工作针对视觉-语言-动作策略计算开销大的痛点，提出紧凑高效的替代方案，在保持性能的同时大幅降低资源需求，对资源受限的机器人部署具有实际意义；且仿真与真实实验均验证了有效性，值得关注。

</details>

<details>
<summary>Abstract</summary>

Vision-language-action policies rely on large multimodal backbones to jointly perform perception, language conditioning, and action generation at every control step. Much of this capacity supports open-domain semantics, whereas continuous robot manipulation primarily requires compact representations of observations, actions, and the transitions induced by actions. Pixel-level world models provide another route, but predicting visual details irrelevant to control can be unnecessarily expensive. We propose SLIM (Self-supervised Latent Interaction Model), a compact 0.5B-parameter latent interaction policy. SLIM learns action-grounded predictive latents that capture both action-conditioned future transitions and the actions that explain observed changes. SLIM learns these representations through self-supervised masked trajectory prediction, combining action reconstruction with future-latent prediction. A compact Mixture-of-Transformers (MoT) backbone models interactions between observation latents and action tokens. The resulting policy is trained with flow matching for language-conditioned action generation. Across simulation benchmarks and real-world evaluation, SLIM matches or exceeds representative large-scale VLA and world-action-model baselines with fewer parameters, no additional embodied pretraining, lower inference latency, and substantially lower GPU memory usage.

</details>

#### 2026-08-10 - Tether-Inertial Localization for Planetary Drones

**Authors:** Dielof van Loon, Anton Bredenbeck, Lennart Puck, Martin Azkarate, Salua Hamaza
**Links:** [abs](https://arxiv.org/abs/2608.09515) - [pdf](https://arxiv.org/pdf/2608.09515)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tether-Inertial Localization for Planetary Drones（面向行星无人机的系绳-惯性定位）
- 作者：Dielof van Loon, Anton Bredenbeck, Lennart Puck, Martin Azkarate, Salua Hamaza
- 出版日期：2026-08-10
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.09515

### 一句话总结
本文提出一种利用系绳长度与角度测量进行无人机定位的方法，结合解析悬链线模型与高斯过程残差补偿，在系绳无人机上实现了厘米级定位精度。

### 研究问题
如何在系绳无人机（TUAV）上实现不依赖视觉或GNSS、且计算高效的定位方法，以克服行星探测中载荷和计算资源受限的问题。

### 核心思路/方法
- 利用系绳（tether）作为定位媒介，通过测量系绳长度和角度估算无人机相对基站的位姿。
- 采用计算高效的解析悬链线模型进行初始位置估计。
- 引入高斯过程（GP）对系统传感器误差和模型局限造成的残差进行补偿，提升定位精度。
- 实验中仅使用系绳位置估计作为反馈，验证了该方法的有效性。

### 主要贡献
- 提出了一种新颖的Tether-Inertial Localization框架，将系绳测量与惯性信息结合用于行星无人机定位。
- 将悬链线模型与高斯过程残差补偿相结合，兼顾计算效率与精度。
- 实验验证覆盖圆形、三角形和8字形轨迹，系绳长度达4.5米，总计飞行37分钟。
- 纯系绳定位平均RMSE为7.4厘米，经GP补偿后降至5.2厘米，较现有技术提升一个数量级。
- 论证了该方法可作为视觉和GNSS定位的实用替代方案。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**
理由：该论文面向行星探测无人机这一特定应用场景，方法具有明确的创新性（系绳定位+GP补偿），且实验精度数据有说服力。但对于不从事无人机或行星探测定位研究的读者，其相关性有限；摘要中也未提及方法在更长系绳、动态扰动或复杂环境下的表现，因此作为一般性定位技术参考的价值中等。

</details>

<details>
<summary>Abstract</summary>

Recent developments in planetary exploration have shown the potential of Unmanned Aerial Vehicles (UAVs), such as the Ingenuity helicopter that provided valuable mapping data. However, limited payload capabilities constrain the flight times and compute available for localization, which restrict their applicability. By providing a tethered connection, issues such as battery and computational constraints are offloaded to the base rover. At the same time, the cable can be exploited for non-drifting localization. This work presents a novel Tether-Inertial Localization approach that uses tether length and angle measurements to estimate the UAV position relative to its base. The method combines a computationally efficient analytical catenary model with a Gaussian Process (GP) residual error compensation. This accounts for systematic sensor inaccuracies and model limitations. Experimental validation across circular, triangular, and figure-eight trajectories with tether lengths up to 4.5 m and a total flight time of 37 minutes demonstrates the effectiveness of the proposed approach. Using only tether-based position estimates for feedback, the analytical catenary model achieves an average RMSE of 7.4 cm, which is further reduced to 5.2 cm through GP-based residual compensation, one order of magnitude better than the state-of-the-art. These results establish Tether-Inertial Localization as a practical alternative to vision- and GNSS-based localization for Tethered Unmanned Aerial Vehicles (TUAVs).

</details>

#### 2026-08-10 - Sekai2: From World Exploration to Interactive World Modeling

**Authors:** Kang He, Wenshuo Peng, Zihui Gao, Jiaming Tan, Kaipeng Zhang, Yongtao Ge
**Links:** [abs](https://arxiv.org/abs/2608.09449) - [pdf](https://arxiv.org/pdf/2608.09449)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sekai2: From World Exploration to Interactive World Modeling
- 作者：Kang He, Wenshuo Peng, Zihui Gao, Jiaming Tan, Kaipeng Zhang, Yongtao Ge
- 出版日期：2026-08-10
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.09449

### 一句话总结
本文提出 Sekai2，一个大规模多源真实世界视频数据集，每段视频均配有相机轨迹和按时间对齐的分层语义标注，旨在支持长时程视频生成、相机可控合成与交互式世界模型预训练。

### 研究问题
视频世界模型需要理解场景如何随时间与视角变化，但现有语料难以同时提供长视频、相机轨迹和时间对齐语义标注。本文试图构建一个同时具备这三者的真实世界视频数据集，以支撑长时程生成与相机控制建模。

### 核心思路/方法
- 从 Sekai 的“世界探索”素材出发，构建多源真实世界视频数据集。
- 数据集包含 128,892 个片段，总计 2,826 小时，来自 113 个国家/地区的 10,428 个源视频。
- 特意偏向持续观察：以 120 秒为统一分解单位，43,594 个片段达到完整 2 分钟，占全部片段的 51.4%。
- 每个片段均提供相机轨迹和分层标注，区分主体运动、环境动态、静态场景内容和相机行为，共 649,597 个时间对齐片段。
- 引入 982 个沿非线性轨迹（含回路与重访）采集的全景序列，通过重访同一地点获得跨时间与视角的重复观测，为学习持久场景表征、长期空间记忆和几何一致的世界模型提供监督信号。

### 主要贡献
- 提出 Sekai2，一个大规模真实世界视频数据集，兼具长时程、相机轨迹和时序语义标注。
- 引入含回路与重访的全景序列，提供同一场景的多次观测，支持持续场景建模。
- 通过语料级分析展示数据集的完整位姿—字幕覆盖、地理与语义多样性、多样化相机轨迹以及高度非冗余的时间描述。

### 局限性
摘要未提供足够信息。摘要未提及数据集在评测基准上的下游任务结果、与现有数据集的定量对比，也未讨论潜在偏差、数据采集伦理或计算成本等限制。

### 阅读优先级
**高**。理由：该工作直接面向视频世界模型训练的核心数据瓶颈，数据集规模大（2,826 小时，含相机轨迹与时间对齐语义），并特别设计全景重访序列以支持长期场景一致性建模，对视频生成、相机控制与世界模型预训练方向的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Video world models must capture how scenes evolve over time and across viewpoints. Training them for long-horizon generation and camera control therefore benefits from long videos paired with camera trajectories and temporally grounded semantics. Existing corpora rarely offer the three together: large-scale web video provides broad visual diversity but no trajectories or time-aligned text, while pose-annotated datasets are typically short-range or reconstruction-oriented. We introduce Sekai2, a multi-source real-world video dataset that carries the world-exploration footage of Sekai toward interactive world modeling. The release contains 128,892 clips totaling 2,826 hours from 10,428 source videos across 113 countries or regions, and is deliberately weighted toward sustained observation: under a common 120-second decomposition, 43,594 segments reach the full two minutes and account for 51.4% of all footage. Every clip includes a released camera trajectory and hierarchical annotations disentangling subject motion, environment dynamics, static scene content, and camera behavior, resulting in 649,597 temporally grounded segments. Crucially, we further introduce 982 panoramic sequences captured along non-linear trajectories with loops and revisits. These revisits provide repeated observations of the same locations across time and viewpoints, offering essential supervision for learning persistent scene representations, long-term spatial memory, and geometrically consistent world models. Corpus-scale analyses demonstrate complete pose-and-caption coverage, broad geographic and semantic diversity, varied camera trajectories, and highly non-redundant temporal descriptions. Together, these properties make Sekai2 a scalable resource for long-horizon video generation, camera-controllable synthesis, and interactive world-model pre-training.

</details>

#### 2026-08-10 - Beyond the Plane: Coupling Planar Vehicle Dynamics with Three-Dimensional Road Geometry

**Authors:** Simon Sagmeister, Phillip Pitschi, Nico Haja, Markus Lienkamp
**Links:** [abs](https://arxiv.org/abs/2608.09402) - [pdf](https://arxiv.org/pdf/2608.09402)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond the Plane: Coupling Planar Vehicle Dynamics with Three-Dimensional Road Geometry
- 作者：Simon Sagmeister, Phillip Pitschi, Nico Haja, Markus Lienkamp
- 出版日期：2026-08-10
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.09402

### 一句话总结
本文提出一种将二维平面车辆动力学模型与三维真实道路几何耦合的新方法，在保持平面模型简单性的同时，引入道路几何带来的力和力矩，以提升仿真的准确性。

### 研究问题
传统二维车辆动力学模型无法准确反映三维道路几何（如倾斜弯道）对车辆行为的影响（例如正常轮胎力可增加66%以上），而现有三维动力学方案复杂且计算昂贵，因此需要一种在保留平面模型优势的前提下弥补其与真实三维道路差距的方法。

### 核心思路/方法
作者提出将平面车辆模型的状态转换到三维空间中的对应表示，并计算由道路几何诱导的力和力矩，将其反馈到平面车辆模型中。方法在真实高速赛车于拉斯维加斯赛车场（banked road）的数据上进行了验证，并在合成赛道上测试了边界情况。

### 主要贡献
- 提出一种新颖的耦合方法，将平面车辆动力学模型与三维道路几何结合。
- 通过真实高速数据和合成赛道验证了方法的准确性，包括边界情况。
- 证明了在不放弃简单平面模型的情况下，可以弥合二维仿真与真实三维道路之间的差距。
- 提供开源实现（github.com/TUMFTM/3d-road-geometry-coupling），便于采用。

### 局限性
摘要未提供足够信息（未提及方法的计算开销、适用车型范围、对极端地形（如颠簸或起伏路面）的具体表现，以及与传统三维模型在精度和速度上的定量对比等）。

### 阅读优先级
**高**。理由：该工作解决了自动驾驶仿真中平面车辆模型与三维道路几何之间的实用痛点，方法保持简单模型的同时提升准确性，且提供开源实现，对于从事车辆动力学仿真、自动驾驶定位与控制算法开发的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Simulation is crucial for developing and testing autonomous driving systems. In particular, the development of localization and control algorithms relies on an accurate vehicle dynamics simulation. However, most vehicle dynamics models are two-dimensional while real-world roads are three-dimensional. For example, effects from the three-dimensional road geometry on the Las Vegas Motor Speedway can increase the normal forces on the tires by more than 66% compared to the nominal load at standstill. As a result, even highly detailed planar vehicle dynamics models struggle to accurately reproduce the real vehicle's behavior. While solutions for three-dimensional vehicle dynamics exist, they are rarely adopted, computationally expensive, and complex. To address this issue, we present a novel method to couple planar vehicle dynamics models with real-world three-dimensional road geometry. We transform the planar vehicle state from the vehicle model's two-dimensional plane to its corresponding representation in three-dimensional space. Additionally, we calculate road-geometry-induced forces and moments and apply them to the planar vehicle model. We validate our approach using high-speed data recorded with a full-scale race car on the banked Las Vegas Motor Speedway. Furthermore, on synthetic tracks, we show that our method yields accurate results even in edge cases. Together, our results demonstrate that the gap between planar simulation and real-world three-dimensional roads can be closed without abandoning simpler planar models. To simplify adoption of our method, we provide the implementation as open-source software on github.com/TUMFTM/3d-road-geometry-coupling.

</details>

#### 2026-08-10 - UnsDrive: Towards Robust End-to-End Autonomous Driving in Unstructured Scenes

**Authors:** Nanxin Zeng, Ruiqi Song, Xiangyu Guo, Baiyong Ding, Yunfeng Ai
**Links:** [abs](https://arxiv.org/abs/2608.09098) - [pdf](https://arxiv.org/pdf/2608.09098)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UnsDrive: Towards Robust End-to-End Autonomous Driving in Unstructured Scenes
- 作者：Nanxin Zeng, Ruiqi Song, Xiangyu Guo, Baiyong Ding, Yunfeng Ai
- 出版日期：2026-08-10
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.09098

### 一句话总结
本文提出 UnsDrive，一种面向非结构化矿区场景的端到端自动驾驶规划器，通过显式建模未知空间并采用流匹配规划器生成多模态轨迹，在开环与闭环实验中显著提升了轨迹精度、避撞能力和长时程鲁棒性。

### 研究问题
现有端到端规划方法主要针对结构化城市道路设计，在矿区等非结构化场景中泛化能力差。此类场景存在道路结构弱、地形遮挡、能见度下降以及大面积未观测区域等问题，使得安全规划极具挑战。核心研究问题为：如何在部分可观测、非结构化的矿区环境中实现鲁棒且安全的端到端驾驶规划。

### 核心思路/方法
- 构建**未知感知占用表示**：利用多帧可见性线索，显式区分并建模占用（occupied）、自由（free）与未知（unknown）三类空间。
- **流匹配规划器**：基于上述占用表示进行条件生成，输出多模态未来轨迹。
- **安全增强机制**：引入占用轨迹一致性损失（occupancy trajectory consistency loss）与不确定性感知轨迹评分器（uncertainty-aware trajectory scorer），对进入不可通行或未观测区域的轨迹进行惩罚。
- **MineLoop 仿真器**：开发面向矿区的闭环仿真环境，涵盖不规则道路几何、退化能见度、重型车辆交互及矿业专属运行约束。

### 主要贡献
1. 提出 UnsDrive，首个（据摘要所述）专门针对非结构化矿区场景设计的端到端规划器。
2. 引入显式未知空间建模的占用表示，并据此条件化流匹配规划器，实现多模态轨迹生成。
3. 设计两种安全机制（一致性损失与不确定性感知评分器），有效抑制轨迹进入危险区域。
4. 开发 MineLoop 矿区闭环仿真平台，为不规则道路与矿区约束下的自动驾驶评估提供工具。
5. 在开环与闭环实验中，UnescapeDrive 在轨迹精度、避撞性能及长时程鲁棒性上均优于强基线方法。

### 局限性
摘要未提供足够信息。具体包括：未提及方法在极端天气或传感器故障下的表现、计算复杂度与实时性要求、基线方法的具体名称与数量、实验场景的规模与多样性，以及该方法是否依赖高精度地图或特定传感器配置等细节均未在摘要中说明。

### 阅读优先级
**高**

理由：该工作聚焦于自动驾驶中较少被研究的非结构化矿区场景，提出了显式未知空间建模与流匹配规划器相结合的方案，并附带专用闭环仿真平台，学术价值与应用潜力明确。摘要展示了完整的“问题-方法-验证”链条，实验结果明确优于基线，适合从事自动驾驶规划、机器人导航或仿真平台构建的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

End-to-end planning has shown strong promise for autonomous driving, but most existing methods are designed for structured urban roads and generalize poorly to unstructured mining environments. In such settings, weak road structure, terrain-induced occlusions, degraded visibility, and large unobserved regions make safe planning particularly challenging. To address these challenges, we propose UnsDrive, an end-to-end planner designed for unstructured mining scenes. UnsDrive builds an unknown-aware occupancy representation that explicitly models occupied, free, and unknown space using multi-frame visibility cues, and conditions a flow-matching planner on this representation to generate multimodal future trajectories. To improve safety under partial observability, we further introduce an occupancy trajectory consistency loss and an uncertainty-aware trajectory scorer that penalize trajectories entering non-traversable or unobserved regions. We also present MineLoop, a mining-oriented closed-loop simulator for evaluating autonomous driving under irregular road geometry, degraded visibility, heavy-vehicle interactions, and mining-specific operational constraints. Experiments in both open-loop and closed-loop settings show that UnsDrive consistently outperforms strong baselines in trajectory accuracy, collision avoidance, and long-horizon driving robustness. These results demonstrate the value of explicit unknown-space reasoning for autonomous driving in unstructured mining environments.

</details>

#### 2026-08-09 - MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling

**Authors:** Rong Fu, Chunlei Meng, Yangchen Zeng, Xiaowen Ma, Yongtai Liu, Wangyu Wu, Shuo Yin, Zijian Zhang, Sicheng Li, Yingrui Ji, Chenhao Wang, Simon Fong
**Links:** [abs](https://arxiv.org/abs/2608.08553) - [pdf](https://arxiv.org/pdf/2608.08553)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling
- 作者：Rong Fu, Chunlei Meng, Yangchen Zeng, Xiaowen Ma, Yongtai Liu, Wangyu Wu, Shuo Yin, Zijian Zhang, Sicheng Li, Yingrui Ji, Chenhao Wang, Simon Fong
- 出版日期：2026-08-09
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.08553

### 一句话总结
MotionCraft 是一个基于潜在世界模型与自适应稀疏注意力的可控视频超分辨率框架，兼顾局部细节、长程时空建模、感知真实感与效率。

### 研究问题
如何在高计算约束下实现高质量、时间一致的视频超分辨率，同时允许用户在时间平滑度与重建保真度之间进行可预测的权衡。

### 核心思路/方法
- 将视频超分重建视为“运动感知的潜在状态预测”，引入世界模型思想。
- 构建潜在世界变换器，平衡局部交互与有选择的非局部交互。
- 采用自适应稀疏注意力降低长程建模的计算成本。
- 集成鲁棒运动融合模块与紧凑条件解码器。
- 提供显式用户可控接口，支持时间平滑度与重建保真度的可调权衡。

### 主要贡献
- 提出一种新的可控VSR框架，将世界模型范式融入潜在空间超分重建。
- 结合稀疏注意力实现高效长程时空建模。
- 引入显式控制接口，使时间一致性与重建质量可调节。
- 实验表明在重建性能和感知性能上均取得较强表现。

### 局限性
摘要未提供足够信息来明确说明方法的局限（如失败案例、计算开销具体数值、泛化性边界等）。

### 阅读优先级
**中**  
理由：属于视频超分领域的应用型工作，方法上有一定新颖性（世界模型+稀疏注意力+可控接口），但摘要未提供定量实验细节，且该方向相对专门，若非从事超分或视频生成相关研究的读者可降低优先级；若关注可控生成或高效注意力机制可提升优先级。

</details>

<details>
<summary>Abstract</summary>

Video super-resolution (VSR) aims to recover high-fidelity high-resolution videos from low-resolution inputs and is central to applications ranging from mobile capture to streaming and archival restoration. Existing approaches trade off among local-detail fidelity, long-range spatio-temporal modeling, perceptual realism, and efficiency: convolutional alignment techniques preserve local structure but suffer when motion is large or degradations are complex; transformer-based methods capture long-range dependencies yet require architectural or algorithmic adaptations to remain computationally feasible; and recent latent or diffusion-based generators synthesize rich texture but require specialized temporal constraints to maintain coherence. We present MotionCraft, a controllable VSR framework that formulates restoration as motion-aware latent state prediction inspired by world models and integrates adaptive sparse attention with an explicit user-accessible control interface. MotionCraft combines robust motion fusion, a Latent World Transformer that balances locality and targeted non-local interactions, and a compact conditional decoder to deliver temporally consistent, high-quality reconstructions under streaming constraints. Empirical evaluations show that MotionCraft achieves strong reconstruction and perceptual performance while enabling predictable trade-offs between temporal smoothness and reconstruction fidelity.

</details>

#### 2026-08-09 - RayLift: Lifting Complementary Ray-Wise Evidence with 3D Geometry Priors for Semantic Scene Completion

**Authors:** Meng Wang, Hongxia Yu, Wenzhe He, Xingdong Song, Huilong Pi, Jiapeng Zhang, Ruihui Li
**Links:** [abs](https://arxiv.org/abs/2608.08476) - [pdf](https://arxiv.org/pdf/2608.08476)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** stereo depth, robotics, autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RayLift: Lifting Complementary Ray-Wise Evidence with 3D Geometry Priors for Semantic Scene Completion
- 作者：Meng Wang, Hongxia Yu, Wenzhe He, Xingdong Song, Huilong Pi, Jiapeng Zhang, Ruihui Li
- 出版日期：2026-08-09
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.08476

### 一句话总结
RayLift 提出一种以立体几何为度量参考、结合互补射线证据的相机三维语义场景补全框架，通过显式建模深度不确定性与空间支持来提升场景结构恢复的可靠性。

### 研究问题
相机三维语义场景补全中，现有方法将立体深度估计视为确定性几何约束，导致深度不确定性和局部对应误差直接传播到体素表示中，影响场景结构的恢复质量。

### 核心思路/方法
RayLift 包含三个关键模块：
1. Complementary Context Encoder：从冻结的 3D 视觉基础模型中提取几何感知先验，丰富场景上下文。
2. Depth Ray Evidence Lifter：联合建模几何不相似性、深度置信度和空间不确定性，沿每条相机射线自适应采样并加权候选表面位置。
3. Semantic-Aware Voxel Integrator：通过显式建模射线证据的空间支持，将射线证据注入体素特征中。

整体上，立体几何仅作为度量参考，而互补的射线证据用于自适应恢复可靠的 3D 结构。

### 主要贡献
- 提出 RayLift 框架，将立体几何作为度量参考并引入互补射线证据，缓解深度不确定性对体素表示的负面影响。
- 设计三个模块分别实现几何先验提取、射线证据自适应采样与加权、以及语义感知的体素特征注入。
- 在 SemanticKITTI 和 SSCBench-KITTI-360 上取得具有竞争力的性能，并一致优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对相机三维语义场景补全中深度不确定性的核心难题，提出了全新的射线级证据建模思路，结合 3D 基础模型先验，实验覆盖两大主流基准且性能领先，对自动驾驶和机器人感知方向具有较强参考价值。摘要结构清晰，方法框架完整，适合精读。

</details>

<details>
<summary>Abstract</summary>

Camera-based 3D semantic scene completion (SSC) provides comprehensive scene understanding for autonomous driving and robotics. However, existing methods often treat stereo depth estimates as deterministic geometric constraints, causing depth uncertainty and local correspondence errors to propagate directly into voxel representations. To address this issue, we propose RayLift, a framework that uses stereo geometry as a metric reference while incorporating complementary ray evidence to recover reliable 3D structures adaptively. RayLift first employs a Complementary Context Encoder that extracts geometry-aware priors from a frozen 3D vision foundation model, thereby enriching the scene context. It then introduces a Depth Ray Evidence Lifter module that jointly models geometric dissimilarity, depth confidence, and spatial uncertainty to adaptively sample and weight candidate surface locations along each camera ray. Finally, a Semantic-Aware Voxel Integrator injects the resulting ray evidence into voxel features by explicitly modeling their spatial support. Extensive experiments on SemanticKITTI and SSCBench-KITTI-360 demonstrate that RayLift achieves competitive performance and consistently outperforms existing methods.

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
