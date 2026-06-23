# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：61
- 分类分布：
  - Embodied / Robotics / AR Applications: 20
  - 3D Reconstruction & Multi-view Geometry: 16
  - Neural Scene Representations & Rendering: 12
  - Dynamic / 4D Reconstruction: 9
  - Geometry Foundation Models: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的今日科研趋势综合分析。

#### 今日主要趋势

1.  **动态场景重建技术路径集中爆发，并向“物理感知”与“抗干扰”两个方向深度分化。** 本日发表的动态4D重建论文（如Lift4D、MeGAS、Ocean4D、Temporally Aware Densification、MotionMAR）数量显著增多，且技术路线不再局限于单纯提升渲染质量。一方面开始引入**物理先验**（如MeGAS的热力学、Ocean4D的水介质模型），另一方面则着力解决实际场景中的**非理想条件**，如野外大形变/遮挡（Lift4D）、动态场景中的短寿命高斯问题（Temporally Aware Densification）。

2.  **机器人/具身AI领域研究重心从“感知几何”转向“理解交互与物理动力学”。** 相比积累3D几何数据，今日多篇论文（LaST-HD、IMAGIN-4D、From Pixels to Concepts、Humanoid-OmniOcc）更关注机器人如何**理解**和**执行**物理交互。这体现在：通过人类演示数据对齐物理动力学（LaST-HD）、利用参考图像具体化人-物交互生成（IMAGIN-4D）、构建富含开放语义关系的场景图（From Pixels to Concepts），以及发布面向全身感知的全新占据数据集（Humanoid-OmniOcc），显示出从“静态地图”到“动态、可交互世界模型”的转变。

3.  **3D/4D重建基础模型进入“去理想化”阶段，专门应对真实世界中的不一致与挑战。** 已有方法常假设无干扰的静态场景。本日的多篇论文（G-MASt3R-SfM、VGTW、Projection-Volume Fidelity Divergence）专门致力于处理真实世界的**鲁棒性问题**。这包括处理图像匹配中的错误对应（G-MASt3R-SfM）、移除瞬时遮挡物对多视图重建的干扰（VGTW），以及诊断和解决稀疏视角重建中的优化漂移（PVFD）。这表明领域共识正在向“为失败模式设计”转变。

4.  **稀疏表示与组合式架构成为平衡效率与复杂场景需求的核心方法论。** 面对大规模动态场景（如驾驶场景）或维度较高的任务（如6D姿态估计），直接使用稠密表示或端到端回归变得低效或不准确。今日多篇论文采用**稀疏表示**（如DrivingVoxels的稀疏体素、Flow6D的分层流匹配中的离散隐空间）或**组合式架构**（如CanonicalGS的规范潜在世界融合、Lift4D的因果潜在条件、MotionMAR的多尺度自回归），通过先寻找一个紧凑、稳定的中间表示，再进行精细优化，以降低搜索空间，提升计算效率与最终性能。

#### 技术路线观察

| 研究方向 | 技术侧重点 | 代表论文 |
| :--- | :--- | :--- |
| **几何基础模型** | 关注SfM管线的鲁棒性与抗干扰能力，通过图结构剪枝、多阶段优化或显式干扰物训练策略，提升在非理想多视图输入下的重建质量。 | G-MASt3R-SfM, VGTW |
| **3D/4D重建** | 从通用动态场景重建向**物理感知**（热力学、水下介质）和**稀疏/野外**场景深入。主流框架为3DGS及其变体，但核心瓶颈转向如何有效处理时间维度上的**监督不足**（短寿命高斯）、**数据稀缺**（4D数据）和**病态逆问题**（稀疏视角CT）。 | Lift4D, MeGAS, Ocean4D, Temporally Aware Densification |
| **神经场景表示** | 强调**稳定且可扩展**的表示学习。前馈式模型（CanonicalGS）通过不确定性感知融合构建规范表示，优于纯视图依赖预测。同时，开始系统性地诊断和解释表示在优化过程中的失效模式（PVFD），并提出针对性的轻量级控制器。 | CanonicalGS, Projection-Volume Fidelity Divergence |
| **机器人/AR应用** | 重点在于**人-机-环境交互**。技术路线包括：从人类数据学习物理动力学（LaST-HD）、通过图像精确控制交互生成（IMAGIN-4D）、开放语义场景理解（From Pixels to Concepts）、发布面向新形态机器人（人形、异构）的专用数据集和仿真器（Humanoid-OmniOcc, HERCULES）。同时，也开始审视现有几何方法在新应用场景（如旋转相机）下的失败案例（Can Single-View Mesh...）。 | LaST-HD, IMAGIN-4D, Humanoid-OmniOcc, HERCULES |

#### 值得优先阅读的论文

1.  **Lift4D**: 其**将单视图3D估计结合测试时优化解决4D重建数据稀缺与野外场景问题**的思路极具启发性。因果潜在条件保证了时序一致性，是解决动态重建中“先验”与“观察”结合的优秀范例。
2.  **MeGAS**: 代表了**神经渲染与物理仿真融合的最前沿**。首次将热力学相变引入3DGS，不仅展示了视觉效果，更开启了“可编辑、可预测”的场景表示新范式，对VFX和虚拟世界创造有革命性意义。
3.  **Flow6D**: 其**离散-连续分层流匹配**策略为解决高维连续空间中的精确估计和实时性矛盾提供了优雅的解决方案，在6D姿态估计这一关键任务上取得了突破性进展（70 FPS），值得相关领域借鉴。
4.  **Temporally Aware Densification (VAD)**: 该工作**直击当前动态3DGS的一个核心痛点**——静态密集化策略不适用于动态场景。其提出的VAD模块作为即插即用组件，具有极高的实用价值和可迁移性，对推动整个动态GS领域进步有直接帮助。
5.  **Humanoid-OmniOcc**: 这是**为新兴技术方向（人形机器人）构建基础设施的工作**。发布的全景立体占据数据集和提出的Real2Sim2Real范式，很可能会成为该领域后续研究的基准，具有前瞻性和战略价值。

#### 可能的研究机会

1.  **融合物理先验与抗干扰方法**: 将MeGAS的热力学、Ocean4D的介质模型等物理先验，与Lift4D、VGTW等抗干扰框架结合，有望构建出在真实复杂（水下、火灾、高温）环境中依然鲁棒的通用4D重建模型。
2.  **面向仿人操作的交互生成研究**: 基于IMAGIN-4D的精细交互控制，结合LaST-HD的跨形态动力学对齐，可以研究如何让机器人**根据单一参考图像，学习并模仿人手的精细操作技能**，并泛化到未知物体，这将是机器人学习领域极具潜力的方向。
3.  **利用扩散模型作为4D重建的通用先验**: Lift4D使用了扩散先验补全未知区域，可进一步探索将扩散模型**显式地用作动态场景的生成式先验**。例如，用扩散模型预测被遮挡物体的未来状态或内部结构，从而改进动态重建与编辑。
4.  **稀疏组合式架构在更多任务上的应用**: 借鉴DrivingVoxels的稀疏组合想法，可将复杂场景分解为多个独立的动态实体（物体、人物），由独立的子网络（或子表示）负责，然后在渲染阶段进行联合光栅化。这种方法有望更好地处理包含大量独立运动物体的“野外观测”场景。

#### 风险和不确定性

-   **性能与泛化评估**: 许多论文（如MeGAS、Ocean4D、VGTW）的结论主要基于特定数据集（PandaSet, ETH3D等）。**其域泛化能力在完全不同的场景、光照、传感器配置下是否依然成立，需要阅读全文的消融实验和讨论部分来确认。**
-   **计算开销**: 论文摘要通常侧重展示方法带来的性能提升，**但计算成本（训练/推理速度、内存占用）往往被简化或隐藏**。例如，测试时优化框架（Lift4D）、物理求解器（MeGAS）或大语言模型推理（From

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-23T11:23:53-04:00
**Total number of papers:** 61
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

### 2026-06

#### 2026-06-22 - Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views

**Authors:** Jiho Choi, Seonho Lee, Seojeong Park, Hyunjung Shim
**Links:** [abs](https://arxiv.org/abs/2606.23557) - [pdf](https://arxiv.org/pdf/2606.23557)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views
- 作者：Jiho Choi, Seonho Lee, Seojeong Park, Hyunjung Shim
- 出版日期：2026-06-22
- 分类：Geometry Foundation Models
- 链接：摘要: https://arxiv.org/abs/2606.23557, PDF: https://arxiv.org/pdf/2606.23557

### 一句话总结
本文提出DR-MV3D框架，通过密集且可验证的奖励来监督多视图3D问答中的推理过程，从而改善多模态大模型在跨视图推理和视角选择上的不一致与脆弱性问题。

### 研究问题
多视图3D视觉问答（MV3D-VQA）任务中，当前多模态大模型通常只使用稀疏的、答案级别的监督信号进行训练，这导致了推理过程中跨视图推理不一致和视角选择不稳健。

### 核心思路/方法
- 将MV3D-VQA分解为三个可学习的中间步骤：异中心全局地图构建、基于问题的视图轨迹规划、以及用于答案预测的自中心定位。
- 引入两种密集奖励，使中间步骤无需人工标注即可学习：
  - **全局一致性奖励**：将预测的地图与来自冻结的3D视觉基础模型（如VGGT + SAM3）的几何一致性伪目标进行对齐。
  - **局部轨迹奖励**：监督有序的视角选择。
- 使用轨迹级别的策略优化方法（GRPO）对整个流程进行优化。

### 主要贡献
- 提出了DR-MV3D，一个基于地图的学习框架，利用密集、可验证的奖励来监督MV3D-VQA的推理过程。
- 通过分解任务并引入全局和局部两种密集奖励，使中间推理步骤变得可学习且无需人工标注。
- 在MindCube、VSI-Bench和BLINK (MV)三个基准上的实验表明，DR-MV3D相比强多图像基线方法有持续改进，验证了过程级密集监督对多视图3D推理的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：本文针对多视图3D推理中的监督稀疏性问题提出了一个创新且可行性高的密集奖励框架，实验覆盖多个基准且有显著提升，对几何基础模型和多模态大模型的结合研究有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Multi-view 3D Visual Question Answering (MV3D-VQA) requires integrating partial observations into a coherent 3D scene representation and selecting informative viewpoints for multi-step spatial reasoning. However, current multimodal LLMs are typically trained with sparse, answer-level supervision, which often yields inconsistent cross-view reasoning and brittle view selection. We present DR-MV3D (Dense Reward for MV3D-VQA), a map-grounded learning framework that provides dense, verifiable rewards to supervise the reasoning process. Our approach decomposes MV3D-VQA into (i) allocentric global map construction, (ii) question-conditioned view-trajectory planning, and (iii) egocentric grounding for answer prediction. To make intermediate steps learnable without manual annotations, we introduce two rewards: a global consistency reward that aligns the predicted map with geometry-consistent pseudo targets from frozen 3D vision foundation models (e.g., VGGT + SAM3), and a local trajectory reward that supervises ordered viewpoint selection. We optimize the full pipeline with trajectory-level policy optimization (GRPO). Experiments on MindCube, VSI-Bench, and BLINK (MV) show that DR-MV3D consistently improves over strong multi-image baselines, supporting the effectiveness of process-level dense supervision for multi-view 3D reasoning.

</details>

#### 2026-06-22 - G-MASt3R-SfM: Graph-based View Pruning and Multi-stage Optimization for Robust SfM

**Authors:** Toshiki Watanabe, Shintaro Ito, Natsuki Takama, Koichi Ito, Takafumi Aoki
**Links:** [abs](https://arxiv.org/abs/2606.22856) - [pdf](https://arxiv.org/pdf/2606.22856)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** MASt3R, image matching, 3D reconstruction, structure from motion, SfM, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G-MASt3R-SfM：基于图的视角剪枝与多阶段优化的鲁棒SfM
- 作者：Toshiki Watanabe, Shintaro Ito, Natsuki Takama, Koichi Ito, Takafumi Aoki
- 出版日期：2026-06-22
- 分类：Geometry Foundation Models（主要），3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要：https://arxiv.org/abs/2606.22856，PDF：https://arxiv.org/pdf/2606.22856

### 一句话总结
本文提出G-MASt3R-SfM，通过基于图的视角剪枝和多阶段优化两大模块，提升了基于MASt3R匹配的SfM管线在困难条件下的鲁棒性和精度。

### 研究问题
现有基于MASt3R的SfM方法（如MASt3R-SfM）存在一个关键缺陷：MASt3R在进行全景匹配时，会为无重叠的图像对生成错误对应关系，这些不可靠匹配被直接用于优化，导致姿态估计精度显著下降。因此，如何有效抑制非重叠图像对引入的噪声，提升SfM的鲁棒性成为核心问题。

### 核心思路/方法
该论文提出G-MASt3R-SfM管线，包含两个核心模块：
1. **基于图的视角剪枝（GVP）模块**：利用匹配置信度构建场景图，从几何一致性角度剪除离群视角（即产生大量错误匹配的视图）。
2. **多阶段优化（MSO）模块**：通过逐步扩展优化范围——从局部一致性优化到全局一致性优化——渐进式地精细化相机参数，避免早期就引入全局全局错误。

### 主要贡献
- 提出了一种新的SfM管线，能有效处理MASt3R在非重叠图像对上产生的误匹配问题。
- 设计了GVP模块，用图结构来识别和修剪离群视角，提升输入匹配的可靠性。
- 设计了MSO模块，通过局部到全局的渐进式优化策略，稳定地恢复相机参数。
- 在ETH3D数据集上的实验表明，该方法在相机姿态估计和3D重建精度上均达到了当前最优水平。

### 局限性
摘要未提供足够信息。例如未明确讨论在更大规模场景或不同数据集上的泛化能力，也未提及剪枝策略可能丢失有效视角的风险，以及多阶段优化带来的计算开销。

### 阅读优先级
**高**。理由：
1. 该工作直接针对当前基于学习匹配的SfM方法（如MASt3R-SfM）的核心缺陷——非重叠对误匹配——进行了系统性改进，具有明确的实用价值。
2. 提出的GVP和MSO模块思路清晰，实验验证在ETH3D上取得SOTA，适合对此方向感兴趣的研究者快速了解当前前沿进展。
3. 文章发表于2026年，且出自日本团队，属于较新成果，对从事三维重建、视觉定位的研究者有较强参考意义。

</details>

<details>
<summary>Abstract</summary>

Structure from Motion (SfM) is essential for multi-view 3D reconstruction, however, its accuracy heavily relies on the accuracy of image matching. While the recent correspondence matching method, MASt3R, enables robust matching even under challenging conditions, it tends to generate incorrect correspondences for non-overlapping image pairs. Consequently, existing SfM methods using MASt3R, such as MASt3R-SfM, suffer from significant degradation in pose estimation accuracy as they incorporate these unreliable matches directly into optimization. To address this issue, we propose G-MASt3R-SfM, a novel SfM pipeline that enhances robustness through two key modules. First, the Graph-based View Pruning (GVP) module constructs a scene graph from matching confidence and geometrically prunes outlier views. Second, the Multi-Stage Optimization (MSO) module progressively refines camera parameters by expanding the optimization scope from local consistency to the global consistency. Experiments on the ETH3D dataset demonstrate that our method achieves state-of-the-art accuracy in both camera pose estimation and 3D reconstruction, effectively suppressing noise caused by outliers.

</details>

#### 2026-06-18 - Evaluation of Image Matching for Art Skills Assessment

**Authors:** Asaad Alghamdi, Michael Poor, Trung-Nghia Le, Tam V. Nguyen
**Links:** [abs](https://arxiv.org/abs/2606.20199) - [pdf](https://arxiv.org/pdf/2606.20199)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** image matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evaluation of Image Matching for Art Skills Assessment
- 作者：Asaad Alghamdi, Michael Poor, Trung-Nghia Le, Tam V. Nguyen
- 出版日期：2026-06-18
- 分类：Geometry Foundation Models (主要) / 3D Reconstruction & Multi-view Geometry (次要)
- 链接：https://arxiv.org/abs/2606.20199

### 一句话总结
本文提出通过图像匹配（SIFT特征与孪生网络）来评估手绘与模板之间的相似度，以衡量绘画技能水平。

### 研究问题
如何利用计算机视觉技术，通过比较手绘图像与原始模板的相似度，客观、高效地评估绘画技能。

### 核心思路/方法
1.  将手绘图像与原始模板进行匹配。
2.  实现并对比两种图像相似度度量方法：基于SIFT特征的关键点匹配，以及基于孪生网络的方法。
3.  通过分析特征匹配结果来推断绘画技能水平。

### 主要贡献
1.  提出了一种基于图像匹配的绘画技能评估方法，旨在简化传统繁琐的评估流程。
2.  实验比较了SIFT特征与孪生网络在衡量手绘与模板图像相似度上的表现。
3.  实验结果表明，SIFT特征的关键点匹配在检测绘画技能方面更为有效，从而验证了该方法评估艺术技能水平的可行性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：方法具有实际应用价值，且比较了经典（SIFT）与前沿（孪生网络）技术，但摘要未提供具体实验结果、评估指标、数据集规模等关键细节，且发表于未来时间，需谨慎核实。

</details>

<details>
<summary>Abstract</summary>

While some individuals possess a natural talent for drawing, mastering this skill requires dedicated training and practice. Determining one's skill in the art of drawing requires proper comprehensive assessment. In this paper, we propose a method to measure drawing skill by by matching the hand-drawn image with the original template. Existing techniques often involve complex processes. However, advancements in computer vision allow us to train computers to perform these comparisons at a human-like level, thereby resolving the tedious and overwhelming traditional process. Using computer vision applications, determining image similarity involves identifying the level of similarities in an image with a reference image. We have implemented and analyzed the SIFT feature and Siamese network to measure image similarity. Our results indicate that it is feasible to assess art skill levels. Through feature analysis, we found that SIFT-based key point matching provides a more effective means of detecting drawing skills.

</details>

#### 2026-06-16 - RegimeVGGT: Layer-Wise Spatially Preserving Redundancy Removal for Visual Geometry Grounded Transformer

**Authors:** Jinhao You, Shuo Lyu, Zhuohang Lyu, Tanxuan Li, Zibo Zhao, Jiaxiang Hu, Kai Tang, Yichen Guo
**Links:** [abs](https://arxiv.org/abs/2606.18439) - [pdf](https://arxiv.org/pdf/2606.18439)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** visual geometry grounded transformer, VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RegimeVGGT: Layer-Wise Spatially Preserving Redundancy Removal for Visual Geometry Grounded Transformer
- 作者：Jinhao You, Shuo Lyu, Zhuohang Lyu, Tanxuan Li, Zibo Zhao, Jiaxiang Hu, Kai Tang, Yichen Guo
- 出版日期：2026-06-16
- 分类：Geometry Foundation Models
- 链接：摘要：https://arxiv.org/abs/2606.18439；PDF：https://arxiv.org/pdf/2606.18439

### 一句话总结
RegimeVGGT 提出一种无训练的分层加速方法，通过识别 VGGT 网络中三层不同的冗余模式并对其进行修剪，实现了6.7倍加速且不降低重建质量。

### 研究问题
如何在不经过额外训练的前提下，减少 VGGT 中二次交叉帧注意力的计算开销，同时保持多视图场景三维重建的准确性？

### 核心思路/方法
1. **诊断性分析**：通过频谱、探针和因果分析，发现 VGGT 网络中存在三种不同的层级行为模式（regime）——浅层缺乏跨视图结构、中层驱动跨视图对齐、深层对密集几何冗余但对姿态重要。
2. **分轴压缩**：沿两层维度（token 空间和特征通道/时序维度）应用层级的 U 形压缩策略：
   - **Saliency-Guided Banded Merging**：保护几何和边缘显著 token 的完整性。
   - **Selectively Protected K/V Downsampling**：通过相位偏移空间网格、参考帧锚点和未压缩的相机/注册 token，保留跨帧空间覆盖和姿态关键路径。

### 主要贡献
- 揭示了 VGGT 网络中跨层冗余的非均匀分布，识别出三种不同的冗余处理机制。
- 提出无训练、分层的 U 形压缩方法，同时沿两个轴线（token 和 K/V）进行选择性保留与压缩。
- 实验表明，在匹配原始 VGGT* 重建质量的条件下，实现 6.7 倍速度提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该方法针对当前视觉几何基础模型（VGGT）的核心效率瓶颈提出解决方案，且无需重新训练，实用性较强；分层冗余分析视角具有理论启发性。对关注点云重建、多视图几何或高效 Transformer 部署的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Visual Geometry Grounded Transformer (VGGT) recovers dense 3D scene structure from multi-view images in one forward pass, but quadratic cross-frame attention limits its scalability. Existing training-free accelerators reduce computation uniformly along one axis, missing layer heterogeneity. Our spectral, probing, and causal analyses reveal three regimes: shallow layers lack cross-view structure, middle layers drive cross-view alignment, and deep layers are redundant for dense geometry yet their cross-frame attention remains essential for pose. RegimeVGGT applies layer-wise U-shaped compression along two axes: Saliency-Guided Banded Merging protects geometry- and edge-salient tokens, while Selectively Protected K/V Downsampling preserves cross-frame spatial coverage and the pose-critical path through a phase-shifted spatial grid, a reference-frame anchor, and uncompressed camera/register tokens. Training-free, RegimeVGGT achieves a 6.7x speedup over VGGT* at matched reconstruction quality.

</details>

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-22 - Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild

**Authors:** Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani
**Links:** [abs](https://arxiv.org/abs/2606.23688) - [pdf](https://arxiv.org/pdf/2606.23688)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild  
- 作者：Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani  
- 出版日期：2026-06-22T17:59:54Z  
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering  
- 链接：摘要：https://arxiv.org/abs/2606.23688，PDF：https://arxiv.org/pdf/2606.23688  

### 一句话总结  
Lift4D 提出了一种测试时优化框架，通过因果潜在条件生成时间一致的单帧3D重建作为初始化，并结合遮挡感知优化和扩散先验，从单目视频中高质量重建动态非刚体4D场景，尤其适用于野外复杂场景。

### 研究问题  
如何从单目野外视频中重建动态非刚体对象的4D表示，克服现有方法在缺乏4D训练数据、依赖初始先验后仅靠视频监督、以及处理大形变和严重遮挡时的局限性。

### 核心思路/方法  
1. **时间一致的3D初始化**：采用现有单视图3D重建模型，通过因果潜在条件（causal latent conditioning）使其生成时间上连续的逐帧预测，为可变形3D高斯泼溅表示提供一致性初始化。  
2. **遮挡感知优化与雕塑**：通过遮挡感知优化，使该表示与输入视频对齐，忠实恢复可见表面细节；同时利用视图条件扩散先验补全未观察区域，完成对表示的精炼（“雕塑”）。  
3. **测试时优化**：整个框架在测试时自适应优化，无需额外的4D训练数据。

### 主要贡献  
- 提出一种结合单视图3D估计与测试时优化的框架，解决4D重建中数据稀缺和野外复杂场景的挑战。  
- 通过因果潜在条件实现时间一致的逐帧3D预测，初始化可变形表示。  
- 引入遮挡感知优化与扩散先验，在恢复可见细节的同时合理补全遮挡区域。  
- 在存在严重遮挡和非刚体运动的野外序列上，显著优于先前4D重建方法。

### 局限性  
摘要未提供足够信息，如对计算效率、具体失败案例、泛化到不同动态类型（如拓扑变化）或对输入视频质量的要求等未提及。

### 阅读优先级  
高。理由：该工作针对单目4D重建中的核心难点（大形变、严重遮挡、数据稀缺）提出了新的框架，并在野外场景上取得显著改进，对动态重建领域具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic non-rigid objects from monocular video requires integrating visual cues from direct observations with data-driven priors over geometry and appearance. Prior approaches either learn to directly predict 4D representations from visual input or initialize a 3D representation that is subsequently deformed and refined based on video evidence. However, the former are constrained by the scarcity of 4D training data, while the latter leverage priors only for the initial reconstruction and rely solely on video supervision thereafter; neither handles complex in-the-wild scenarios with large deformations and occlusions well. We present Lift4D, a test-time optimization framework that addresses both limitations. First, we adapt an existing single-view 3D reconstruction model to yield temporally consistent per-frame predictions via causal latent conditioning, providing a coherent initialization for a deformable 3D Gaussian Splatting representation. We then ``sculpt'' this representation to match the input video through an occlusion-aware optimization that faithfully recovers visible surface details while completing unobserved regions using a view-conditioned diffusion prior. We demonstrate that Lift4D clearly improves over prior 4D reconstruction methods, particularly on challenging in-the-wild sequences with severe occlusions and non-rigid motion.

</details>

#### 2026-06-22 - MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing

**Authors:** Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
**Links:** [abs](https://arxiv.org/abs/2606.23455) - [pdf](https://arxiv.org/pdf/2606.23455)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing
- 作者：Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
- 出版日期：2026-06-22T15:05:59Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.23455；PDF: https://arxiv.org/pdf/2606.23455

### 一句话总结
MeGAS是一个将热力学相变动力学融入3D高斯溅射的框架，实现了对热物理现象（如熔化、凝固）的物理一致且逼真的场景编辑与渲染。

### 研究问题
如何将温度这一隐形物理因素融入神经渲染框架，以合成和编辑涉及热力学相变的物理现象，弥合真实感场景重建与基于物理的动画之间的差距。

### 核心思路/方法
1. **热力学动态高斯表示**：在3D高斯溅射（3DGS）基础上增加温度属性，构建新的表示。
2. **物理求解器**：采用热对流-扩散求解器，并耦合物质点法（MPM）动力学与相变模型，驱动高斯的演化。
3. **拓扑自适应渲染策略**：针对极端变形导致的裂缝和漂浮物问题，提出新的高斯渲染策略以保持拓扑一致性。

### 主要贡献
1. 首次将热力学相变动力学与3D高斯溅射结合，提出MeGAS框架。
2. 设计了带温度属性的热力学动态高斯表示及对应的物理求解器。
3. 提出拓扑自适应高斯渲染策略，提升极端变形下的渲染质量。
4. 实验证明MeGAS在保持物理一致性的同时，能生成高保真度真实感渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作创新性地将温度这一关键物理因素引入3D高斯溅射，弥补了现有物理驱动神经渲染方法仅关注机械动力学的不足。对于从事动态场景重建、物理仿真与神经渲染交叉领域的研究人员具有较高参考价值，且应用场景（如热物理现象编辑）具有独特吸引力。

</details>

<details>
<summary>Abstract</summary>

Recent advances integrate physically grounded Newtonian dynamics with neural rendering frameworks, narrowing the gap between photorealistic scene reconstruction and physics-based animation. However, existing approaches focus on mechanically driven dynamics while neglecting temperature, a fundamental yet invisible physical factor underlying phenomena such as melting, solidification, and other thermomechanical processes. In this paper, we propose MeGAS, a novel framework that incorporates thermomechanical phase-change dynamics into 3D Gaussian Splatting (3DGS). Specifically, we propose a new thermomechanical dynamic Gaussian Splatting representation that augments 3DGS with temperature attributes and employs a heat advection-diffusion solver with MPM dynamics incorporating phase transitions, enabling physically plausible and visually realistic synthesis of thermophysical phenomena. Furthermore, a new topology-adaptive Gaussian rendering strategy is proposed to mitigate cracking and floaters under extreme deformation. Extensive experiments demonstrate that MeGAS produces physically consistent thermomechanical behavior while maintaining high-fidelity photorealistic rendering, advancing toward physics-integrated world models.

</details>

#### 2026-06-22 - Ocean4D: Generative Underwater 4D Reconstruction via Medium-Aware Video Diffusion

**Authors:** Yuqiang Huang, Yuxi Wang, Junyu Dong, Zhaoxiang Zhang
**Links:** [abs](https://arxiv.org/abs/2606.23298) - [pdf](https://arxiv.org/pdf/2606.23298)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Ocean4D: Generative Underwater 4D Reconstruction via Medium-Aware Video Diffusion
- 作者：Yuqiang Huang, Yuxi Wang, Junyu Dong, Zhaoxiang Zhang
- 出版日期：2026-06-22
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2606.23298

### 一句话总结
该论文提出名为Ocean4D的生成式框架，通过结合4D几何一致性条件生成与介质感知去噪扩散，实现从单目视频到水下动态场景的4D重建。

### 研究问题
现有水下4D重建方法多基于空气环境假设，未显式建模水下介质对光的吸收和散射，且近静态假设对动态干扰（如漂移粒子）敏感，导致几何不稳定和跨视角不一致。本研究旨在解决这些耦合挑战。

### 核心思路/方法
- **4D-GCC**：构建4D几何一致性的条件模块，改进跨帧覆盖范围，为目标轨迹生成提供全局结构约束。
- **Medium-Aware Block**：在潜在扩散过程中执行隐式介质感知去噪，专门稳定水下吸收和散射造成的外观退化。
- 输入单目视频和目标相机轨迹，生成沿目标路径的一致视频，同时保留全局结构和跨视角一致性。

### 主要贡献
1. 提出首个专门面向水下环境的生成式4D重建框架Ocean4D。
2. 设计4D几何一致性条件（4D-GCC）和介质感知去噪模块，解决水下光线退化与动态变化的耦合问题。
3. 在动态和静态水下基准上达到最先进性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文针对水下4D重建这一特殊且困难的任务，提出了完整的生成式框架，并在公开基准上取得领先结果，对相关领域（水下视觉、动态场景重建）有明确参考价值。

</details>

<details>
<summary>Abstract</summary>

Underwater 4D reconstruction remains challenging due to the coupling between degraded light transport in participating media and dynamic water variations. Most existing Methods are developed under in-air assumptions and do not explicitly account for underwater absorption and backscatter. Additionally, near-static assumptions make these approaches sensitive to drifting particles and dynamic distractors , leading to unstable geometry and inconsistent cross-view results. To address these issues, we propose a generative framework for underwater 4D reconstruction, named Ocean4D, which is built on two complementary components. Specifically, 4D-GCC constructs 4D geometrically consistent conditioning with improved cross-frame coverage, while the Medium-Aware Block performs implicit medium-aware denoising in the latent diffusion process to stabilize underwater appearance under absorption and scattering. Given a monocular video and target cameras, our method generates videos along the target trajectories while preserving global structure and cross-view consistency. Extensive experiments on both dynamic and static underwater benchmarks demonstrate state-of-the-art performance on underwater reconstruction.

</details>

#### 2026-06-22 - Temporally Aware Densification for Dynamic 3D Gaussian Splatting

**Authors:** Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan
**Links:** [abs](https://arxiv.org/abs/2606.23212) - [pdf](https://arxiv.org/pdf/2606.23212)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, dynamic 3D, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Temporally Aware Densification for Dynamic 3D Gaussian Splatting
- 作者：Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan
- 出版日期：2026-06-22
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.23212

### 一句话总结
本文提出一个时间感知的密集化框架，通过结合时间可见性、自适应阈值和变形偏移策略，改善动态3D高斯泼溅中动态区域的重建质量。

### 研究问题
现有动态3D高斯泼溅方法沿用静态场景的密集化策略，忽视了时间连续性，导致动态区域因高斯短暂存在、监督稀疏而出现重建不充分和模糊问题。

### 核心思路/方法
1. **Visibility-Aware Densification (VAD)**：将时间可见性集成到密集化过程中，使高斯单元根据其实际时间存在情况被精细化。
2. **Temporally-Adaptive Thresholding (TAT)**：根据每个高斯单元的时间寿命动态调整密集化阈值，促进静态和动态区域的平衡优化。
3. **Temporal Offset Warping (TOW)**：围绕时间中心增强变形能力，延长高度动态高斯单元的寿命，促进更有效的密集化。

### 主要贡献
- 揭示了动态3D高斯泼溅中静态密集化策略的缺陷，并指出其对动态区域重建的负面影响。
- 提出VAD框架作为即插即用模块，可泛化应用于多种动态3D高斯泼溅方法。
- 在三个动态多视角基准数据集上，动态区域的视觉质量显著优于现有方法。

### 局限性
摘要未提供足够信息：未提及计算开销、训练/推理速度变化、对极端动态场景的鲁棒性，或现有基准数据集之外的泛化能力限制。

### 阅读优先级
**高**。理由：该工作直击动态场景重建中一个被忽视的关键问题（密集化策略与时间不兼容），提出的方法具有即插即用性，且实验在多个基准上取得显著改进，对从事动态/4D重建的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Despite modeling temporal motion, dynamic 3D Gaussian Splatting (3DGS) methods still inherit a static densification strategy that is ill-suited for dynamic scenes. This neglect of temporal behavior leads to under-reconstructed and blurry dynamic regions, as short-lived Gaussians receive sparse supervision and fail to densify effectively. We propose a Visibility-Aware Densification (VAD) framework that integrates temporal visibility into the densification process, ensuring that Gaussians are refined based on their actual temporal presence. A Temporally-Adaptive Thresholding (TAT) mechanism further adjusts each Gaussian's densification threshold according to its temporal lifespan, promoting balanced refinement of both static and dynamic regions. Finally, a Temporal Offset Warping (TOW) design enhances deformation capacity around temporal centers, extending the lifespan of highly dynamic Gaussians and facilitating more effective densification. Our approach achieves substantial improvements in the visual quality of dynamic regions, outperforming existing methods across three dynamic multi-view benchmark datasets. Moreover, the proposed VAD module generalizes across diverse dynamic 3DGS methods, consistently improving dynamic reconstruction as a plug-and-play component.

</details>

#### 2026-06-22 - MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations

**Authors:** Yuhua Luo, Junsheng Zhang, Mengyin Liu, Xincheng Lin, Ming Yan, Zhudi Chen, Chenglu Wen, Lan Xu, Siqi Shen, Cheng Wang
**Links:** [abs](https://arxiv.org/abs/2606.23000) - [pdf](https://arxiv.org/pdf/2606.23000)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations
- 作者：Yuhua Luo, Junsheng Zhang, Mengyin Liu, Xincheng Lin, Ming Yan, Zhudi Chen, Chenglu Wen, Lan Xu, Siqi Shen, Cheng Wang
- 出版日期：2026-06-22
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2606.23000

### 一句话总结
本文提出MotionMAR，一种基于多尺度自回归的粗到细框架，从稀疏观测中重建人体运动，并通过在AMASS数据集上的实验取得了最先进精度。

### 研究问题
如何从稀疏观测（sparse observations）中准确、结构一致地重建完整的人体运动序列，特别是处理运动中的时间层次结构（从低频全局轨迹到高频细节）。

### 核心思路/方法
采用粗到细的渐进式重建框架，包含四个集成组件：
1. **Temporal Multi-scale Tokenization (TMT) VQ-VAE**：对运动数据进行多时间尺度编码，将语义运动与微小抖动分离。
2. **Motion Autoregressive Network (MAN)**：在潜在空间中跨尺度运行，先通过粗索引建立全局结构，再生成细索引恢复具体细节。
3. **Scale-Aware Control (SAC)**：集成稀疏跟踪数据，确保生成输出与实际观测对齐。
4. **Motion Refinement Network (MRN)**：对连续姿态进行平滑并消除量化伪影。

### 主要贡献
- 提出一种结构感知的、粗到细的多尺度自回归框架，用于从稀疏观测中重建人体运动。
- 设计了TMT VQ-VAE、MAN、SAC和MRN四个协同组件，分别处理多尺度编码、自回归预测、观测对齐和细节平滑。
- 在AMASS数据集上取得了当前最先进的运动重建精度。
- 开源了代码（http://www.lidarhumanmotion.net/motionmar/）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文提出了一种新颖的粗到细多尺度自回归框架，解决从稀疏观测重建人体运动的实际问题，并在标准数据集AMASS上实现了最先进结果。对于从事人体运动捕捉、4D重建或时间序列预测的研究者具有直接参考价值，且代码已开源，可复现性强。

</details>

<details>
<summary>Abstract</summary>

Human motion follows a temporal hierarchical structure, transitioning from low-frequency global trajectories to high-frequency details. Inspired by the success of multi-level autoregressive models in computer vision, we propose MotionMAR, a coarse-to-fine framework for motion reconstruction from sparse observations. It first estimates the global trajectory of human motion and then gradually refines the temporal details. This architecture consists of four integrated components. The Temporal Multi-scale Tokenization (TMT) VQ-VAE encodes the data at multiple temporal resolutions, separating semantic motion from minor jitters. The Motion Autoregressive Network (MAN) operates in this latent space, predicting motion across scales. It first establishes the global structure through coarse indices and then generates finer indices to recover specific details. Meanwhile, the Scale-Aware Control (SAC) module integrates sparse tracking data to ensure the generated output aligns with actual observations. The Motion Refinement Network (MRN) subsequently smooths consecutive poses and eliminates quantization artifacts. Experiments show that MotionMAR achieves state-of-the-art accuracy on the AMASS dataset, providing a reliable and structure-aware approach for motion reconstruction. The source code is publicly available at http://www.lidarhumanmotion.net/motionmar/.

</details>

#### 2026-06-20 - Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation

**Authors:** Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt
**Links:** [abs](https://arxiv.org/abs/2606.22197) - [pdf](https://arxiv.org/pdf/2606.22197)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic Gaussian, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation
- 作者：Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt
- 出版日期：2026-06-20
- 分类：动态/4D重建；神经场景表示与渲染
- 链接：https://arxiv.org/abs/2606.22197

### 一句话总结
Multi4D提出一种基于多级竞争分配机制的动态高斯泼溅框架，通过将建模能力分配给静态结构、持久动态几何和瞬态外观基元三个层级，在减少动态基元数量的同时实现了高保真渲染质量和实时性能，且支持高效的4D语义分割。

### 研究问题
如何解决动态3D高斯泼溅中运动一致性与视觉保真度之间的根本矛盾——即基于变形的方法会过度平滑高频动态，而4D基元方法则导致对象身份丢失和存储开销过大。

### 核心思路/方法
提出“多级竞争分配”（Multi-Level Competitive Allocation）框架，放弃单一表示，将建模能力分发给三个结构化层级：
- **静态结构基元**：负责不动的背景部分。
- **持久动态几何基元**：负责长期运动的主体结构。
- **瞬态外观基元**：负责快速变化的细节。
通过共享光栅化和残差驱动的优化机制，这些层级动态竞争以解释光度误差，从而实现自适应分工，无需预先分解场景。

### 主要贡献
1. 提出多级竞争分配机制，同时保持了长期运动一致性和精细动态细节，以更少的动态基元实现最先进的渲染质量和实时性能。
2. 通过显式追踪紧凑持久高斯体，支持后续嵌入语义特征，从而实现一个数量级加速的最先进4D语义分割精度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对动态场景重建中的一个典型矛盾提出了新颖的分配策略，结构清晰且效果突出（SOTA渲染+实时+高效分割），但用户未明确表达对动态重建或4D分割的特定兴趣，因此优先级设为中等。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian splatting faces a fundamental tension between motion consistency and visual fidelity. Deformation-based approaches preserve temporal correspondence but suffer from motion over-factorization, oversmoothing high-frequency dynamics. In contrast, 4D-primitive methods capture fine visual details yet incur temporal overparameterization, breaking object identity and leading to severe storage overhead. To resolve this, we introduce Multi4D, a framework for high-fidelity dynamic Gaussian Splatting based on multi-level competitive allocation. Instead of a monolithic representation, we distribute modeling capacity across three structured levels: static structure, persistent dynamic geometry, and transient appearance primitives. Through shared rasterization and residual-driven optimization, these levels dynamically compete to explain photometric error, enabling adaptive specialization without pre-assigned decomposition. This allocation preserves long-term motion consistency while capturing fine dynamic detail, achieving state-of-the-art rendering quality and real-time performance with significantly fewer dynamic primitives. Furthermore, because our representation explicitly tracks compact persistent Gaussians over time, semantic features can be embedded afterward, enabling Multi4D to achieve state-of-the-art 4D segmentation accuracy with an order-of-magnitude speedup. Project page: https://batfacewayne.github.io/Multi4D.io/

</details>

#### 2026-06-17 - Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos

**Authors:** Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon
**Links:** [abs](https://arxiv.org/abs/2606.19156) - [pdf](https://arxiv.org/pdf/2606.19156)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic 4D, Gaussian Splatting, 3D Gaussian Splatting, splatting, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos
- 作者：Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon
- 出版日期：2026-06-17
- 分类：Dynamic / 4D Reconstruction, Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.19156, PDF: https://arxiv.org/pdf/2606.19156

### 一句话总结
本文提出Hand-4DGS，首个从第一人称视频中实现前馈式动态4D手部重建的框架，通过网格引导表示和时间卷积，在无需3D标注的情况下达到约60 FPS的推理速度与强泛化能力。

### 研究问题
从第一人称视频中重建动态4D手部，现有方法面临头部快速运动、手部剧烈动态、严重遮挡以及单视角观测固有的歧义性等挑战。

### 核心思路/方法
1. 采用前馈式（feed-forward）3D高斯泼溅（Gaussian Splatting）框架，直接从输入视频重建动态4D手部。
2. 引入网格引导（mesh-guided）表示来提供结构先验，增强几何准确性。
3. 使用时间卷积（temporal convolutions）建模手部的动态运动，处理时序变化。
4. 利用高斯泼溅的可微渲染实现2D图像监督，从而避免依赖昂贵的3D手部姿态真值标注。

### 主要贡献
1. 首个前馈式动态4D手部重建框架，支持从第一人称视频中快速（~60 FPS）且泛化性强的推理。
2. 提出网格引导表示与时间卷积相结合的方法，有效应对遮挡和动态歧义。
3. 在H2O和ARCTIC两个挑战性数据集上取得优于基线的显著改进。

### 局限性
摘要未提供足够信息来明确指出方法的具体局限性。

### 阅读优先级
高  
理由：该方法解决了第一人称视频中动态手部重建这一关键难题，同时实现了实时推理速度和良好泛化性，且无需3D标注，对AR/VR和AI眼镜等应用具有重要参考价值。论文发表在知名团队工作（含Marc Pollefeys）上，方法新颖且实效性经过数据集验证。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D hand reconstruction from egocentric videos is essential for next-generation computing platforms such as AR/VR and AI glasses. Despite its importance, most prior works focus either on multi-view 3D hand reconstruction or on 4D human body reconstruction. Egocentric 4D hand reconstruction remains challenging due to fast head motion, rapid hand dynamics, severe occlusions, and inherent ambiguity from single-view observations. To address these challenges, we introduce Hand-4DGS, the first feed-forward framework for reconstructing dynamic 4D hands directly from egocentric videos, enabling both fast (~60 FPS) inference and strong generalization. Our approach incorporates a mesh-guided representation for structural priors and temporal convolutions to model dynamic motion. We evaluate our framework on two challenging egocentric datasets, H2O and ARCTIC, and demonstrate significant improvements over baselines. Our method benefits from the generalization capability of feed-forward networks and effective 2D image supervision through Gaussian splatting, without requiring expensive 3D hand pose ground-truth annotations.

</details>

#### 2026-06-17 - Intrinsic 4D Gaussian Segmentation from Scene Cues

**Authors:** Hasan Yazar, Mohamed Rayan Barhdadi, Erchin Serpedin, Mehmet Tuncel, Hasan Kurban
**Links:** [abs](https://arxiv.org/abs/2606.18623) - [pdf](https://arxiv.org/pdf/2606.18623)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic 4D, 4D Gaussian, Gaussian Splatting, rendering, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Intrinsic 4D Gaussian Segmentation from Scene Cues
- 作者：Hasan Yazar, Mohamed Rayan Barhdadi, Erchin Serpedin, Mehmet Tuncel, Hasan Kurban
- 出版日期：2026-06-17
- 分类：动态/4D重建；神经场景表示与渲染
- 链接：摘要页 https://arxiv.org/abs/2606.18623；PDF https://arxiv.org/pdf/2606.18623

### 一句话总结
本文提出Intrinsic-GS，一种无需训练和掩码监督的动态4D高斯分割方法，仅从高斯原语自身的外观、方向、尺度、变形轨迹和渲染边界线索构建稀疏亲和图，通过社区划分实现对象分割。

### 研究问题
如何在无需外部基础模型（如SAM）生成的2D掩码的情况下，仅从4D高斯表示本身恢复场景中的对象级结构，实现高效、鲁棒的动态场景分割。

### 核心思路/方法
1. 从4D高斯原语中提取五种内在线索：外观、方向、尺度、变形轨迹和非学习的渲染边界。
2. 基于这些线索构建稀疏亲和图，将高斯原语之间的相似性编码为图边权重。
3. 应用Leiden社区检测算法对图进行划分，得到对象分组。
4. 整个过程无需任何掩码监督或学习特征场，是训练无关、掩码无关的。

### 主要贡献
- 提出了Intrinsic-GS，首个不依赖外部掩码或特征场的学习的动态4D高斯分割方法。
- 在Neu3D基准上以仅几何线索的变体达到0.902 mIoU，与受SAM监督的TRASE方法持平；在HyperNeRF上达到0.575 mIoU。
- 在HyperNeRF上比基于掩码监督的管线快12.5倍，显著降低了计算开销。
- 证明了4D高斯表示本身已编码了大量分割信号，为高效、鲁棒的动态分割提供了新方向。

### 局限性
摘要未提供足够信息（如对复杂运动或遮挡场景的适应性、社区检测参数敏感性、分割细粒度上限等）。

### 阅读优先级
高。理由：本文提出了一种新颖的无监督/无掩码的动态3D分割方法，在保持较高准确性的同时大幅提升效率（12.5倍加速），对计算机视觉中动态场景理解、编辑、运动分析等领域具有重要参考价值，且方法简洁、可复现性强。

</details>

<details>
<summary>Abstract</summary>

Dynamic 4D Gaussian Splatting reconstructs deforming scenes with high fidelity and is increasingly adopted as a representation for dynamic 3D scenes. Putting such a scene to use, for editing, manipulation or motion analysis, first requires segmenting it: grouping the Gaussian primitives into coherent objects. Current pipelines obtain this grouping by importing 2D masks from foundation models such as SAM and lifting or distilling them into the Gaussian representation. In dynamic scenes these masks must be generated across many frames and views, which is costly, and the resulting segmentation can depend strongly on the quality and consistency of those external masks. We ask how much object-level structure can instead be recovered from the Gaussians themselves, and propose Intrinsic-GS, a training-free, mask-free method that builds a sparse affinity graph over Gaussian primitives from appearance, orientation, scale, deformation-trajectory and non-learned rendered-boundary cues. The graph is partitioned with Leiden community detection, requiring no foundation model and no learned feature field. On the standard 4D Gaussian segmentation benchmarks, Neu3D and HyperNeRF, Intrinsic-GS recovers substantial object structure without mask supervision, reaching 0.746 mIoU on Neu3D and 0.575 on HyperNeRF; on Neu3D, a geometry-only variant reaches 0.902 mIoU, matching SAM-supervised TRASE. On HyperNeRF, Intrinsic-GS runs 12.5x faster than the mask-generation and feature-rendering stages used by mask-supervised pipelines. These results suggest that much of the segmentation signal is already encoded in the Gaussians themselves, offering a fast, mask-free direction for 3D and 4D Gaussian segmentation that may also point toward more generalizable, robust segmentation in settings where external masks are unreliable or expensive.

</details>

#### 2026-06-16 - Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion

**Authors:** Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab, Federico Tombari, Stefano Gasperini
**Links:** [abs](https://arxiv.org/abs/2606.18250) - [pdf](https://arxiv.org/pdf/2606.18250)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** dynamic 3D, 3D reconstruction, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion
- 作者：Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab, Federico Tombari, Stefano Gasperini
- 出版日期：2026-06-16
- 分类：Dynamic / 4D Reconstruction, 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.18250

### 一句话总结
本文提出FR3D，一种将场景3D演化与智能体运动解耦的世界模型，用于从单目观测进行未来动态3D重建，可在2秒后保持几何一致性。

### 研究问题
如何从单目视频预测动态环境的未来演化，同时解决2D视频合成中因自运动与世界运动混淆导致的物体变形或消失等物理不一致性问题，并实现长期几何一致性。

### 核心思路/方法
1. **解耦建模**：显式地将场景的3D演化与智能体轨迹分离，将推断的自我运动作为潜在的动作代理，从而消除自运动与世界运动之间的歧义。
2. **教师-学生蒸馏**：利用现成基础模型的空间“常识”（如深度、尺寸等）进行蒸馏，以增强模型在未见场景上的零样本泛化能力。
3. **持久3D潜在表示**：维护一个持续更新的潜在3D表示，用于预测未来动态场景，而非仅依赖逐帧图像特征。

### 主要贡献
- 提出FR3D，首个实现未来动态3D重建（即使2秒后）并保持几何一致性的世界模型。
- 通过解耦自我运动和场景运动，解决了传统基于图像特征的预测方法中存在的物理不一致问题。
- 引入教师-学生蒸馏策略，利用基础模型的空间知识提升零样本泛化性能。
- 在多个数据集上的实验证明了该方法对未来动态3D重建的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该工作聚焦于动态3D重建与未来预测，方法新颖（解耦自运动与世界运动），对自主智能体相关研究有参考价值。但摘要未提供量化性能数据或与现有方法的具体对比，读者需进一步阅读论文正文以评估实际效果。若研究领域为3D/4D重建或具身智能，则优先级可提升至高。

</details>

<details>
<summary>Abstract</summary>

Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. Unlike prior works that treat the world as a sequence of image-based features, FR3D explicitly decouples the 3D evolution of the scene from the agent's trajectory, treating the inferred ego-motion as a latent proxy for action. This disentanglement resolves the ambiguities between self-motion and world-motion, ensuring geometric consistency into the future. Furthermore, we introduce a teacher-student distillation strategy that leverages the spatial "common sense" of off-the-shelf foundation models, leading to robust zero-shot generalization. Extensive experiments demonstrate FR3D's strong performance for future dynamic 3D reconstruction from monocular observations across multiple datasets, even 2 seconds into the future. Project page: https://fr3d-wm.github.io.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

#### 2026-06-22 - Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation

**Authors:** Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao, Huiliang Shen, Zaixing He
**Links:** [abs](https://arxiv.org/abs/2606.23293) - [pdf](https://arxiv.org/pdf/2606.23293)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, embodied AI, manipulation, localization, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation
- 作者：Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao, Huiliang Shen, Zaixing He
- 出版日期：2026-06-22
- 分类：3D Reconstruction & Multi-view Geometry (主分类), Embodied / Robotics / AR Applications (副分类)
- 链接：https://arxiv.org/abs/2606.23293

### 一句话总结
Flow6D提出一种两级分层流匹配框架，通过先离散后连续的策略，在保持实时推理速度（70 FPS）的同时，提升类别级6D姿态估计的精度，并自然扩展到铰接物体。

### 研究问题
如何解决类别级6D姿态估计中，高维连续空间直接回归带来的精度受限（噪声和局部最优）和搜索效率低（阻碍实时性）两个关键挑战。

### 核心思路/方法
提出一种两阶段分层流匹配框架：
1. **离散隐空间定位**：先将旋转和平移参数离散化为箱子，使用离散流匹配模型锁定真实姿态附近的隐空间，降低搜索复杂度。
2. **连续姿态回归**：在隐空间中采样后，使用连续流匹配模型预测局部姿态残差，优化估计并回归到精确姿态。

### 主要贡献
- 提出Flow6D框架，结合离散到连续的两阶段流匹配，同时提升效率和精度。
- 在合成和真实数据集上超越现有最优方法，并实现实时推理（70 FPS）。
- 框架自然扩展至铰接物体姿态估计，无需额外设计。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法为类别级6D姿态估计提供了新颖的分层流匹配思路，在精度和实时性（70 FPS）上均取得突破，且对铰接物体有扩展性，对计算机视觉和机器人操作领域具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

6D pose estimation is a key task in computer vision and embodied AI, widely used in robotic manipulation, augmented reality, etc. Existing methods directly regress in a high-dimensional continuous space, facing two key challenges in category-level pose estimation: limited accuracy due to noise and local optima, and inefficient search over an infinite space that hinders real-time performance. This paper proposes Flow6D, a hierarchical flow matching framework with a two-stage discrete latent space localization-continuous pose regression strategy. Rotation and translation parameters are first discretized into bins, with a discrete flow matching model locking the latent space around the true pose to reduce search complexity. Then, by sampling in the latent space, a continuous flow matching model predicts local pose residuals to optimize the estimate and regress to an accurate pose. The framework also naturally extends to articulated objects, outperforming state-of-the-art methods on synthetic and real datasets with real-time inference at 70 FPS. Project website: https://flow6d.github.io/.

</details>

#### 2026-06-22 - DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction

**Authors:** Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi
**Links:** [abs](https://arxiv.org/abs/2606.23031) - [pdf](https://arxiv.org/pdf/2606.23031)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, driving scene

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction
- 作者：Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi
- 出版日期：2026-06-22T08:42:16Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次分类）
- 链接：[摘要](https://arxiv.org/abs/2606.23031) | [PDF](https://arxiv.org/pdf/2606.23031)

### 一句话总结
DrivingVoxels 提出一种基于组合式稀疏体素光栅化的动态驾驶场景重建框架，通过多独立八叉树联合光栅化实现高效几何表示与训练加速。

### 研究问题
如何高效地重建动态驾驶场景中的无界环境与多个动态物体，同时克服现有稀疏体素方法局限于静态场景、以及3D高斯泼溅方法训练耗时且内存不可控的不足。

### 核心思路/方法
- 采用组合式稀疏体素表示：为每个刚体动态物体定义局部八叉树，并独立建模；另用独立静态八叉树表示静止背景。
- 在单次渲染过程中联合光栅化多个八叉树中的稀疏体素，实现统一渲染。
- 采用完全显式、无神经网络的表示，结合LiDAR引导的结构初始化，高效捕捉场景几何结构。

### 主要贡献
- 提出DrivingVoxels框架，针对动态驾驶场景设计组合式稀疏体素渲染方法。
- 在PandaSet基准上，该方法在新视角合成（NVS）和重建的感知指标上与现有方法持平，在结构指标上更优。
- 因基于强LiDAR先验的高效优化流程，训练时间短于基于3D高斯泼溅的方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对动态驾驶场景重建中的效率与表示问题提出新颖的组合式显式体素方法，实验显示训练速度优势；但摘要未提供与其他动态方法（如4D重建或神经辐射场）的详细对比，且未讨论内存消耗具体数值，建议对时序重建或自动驾驶场景视觉感兴趣时阅读。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic urban scenes remains challenging due to the unbounded nature of driving environments and the presence of multiple dynamic objects. Currently, potentially faster sparse voxel methods are mainly designed for static scenarios. On the other hand, dynamic approaches based on 3D Gaussian Splatting, despite their high-fidelity, are often time-consuming for driving scenarios and exhibit uncontrollable memory growth in large scenes. To address these limitations, we present DrivingVoxels, a compositional sparse voxel rendering framework for dynamic driving scenes. Our method jointly rasterizes sparse voxels from multiple independent octrees within a single rendering pass. Each rigid dynamic object is represented by an octree defined in its local coordinate frame, while a separate static octree models the stationary background. DrivingVoxels adopts a fully explicit, neural-free representation together with a LiDAR-guided structural initialization that efficiently captures scene geometry. We evaluate our framework on the PandaSet benchmark, demonstrating that DrivingVoxels performs on par on perceptual metrics and better on structural metrics for NVS and reconstruction while requiring shorter training times than previous 3DGS-base methods to an efficient optimization workflow anchored by a strong LiDAR prior.

</details>

#### 2026-06-22 - Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?

**Authors:** Yu Zhan, Guangcheng Chen, Hanjing Ye, Zhiqin Cheng, Zanjia Tong, Wenjun Xu, Hong Zhang
**Links:** [abs](https://arxiv.org/abs/2606.22987) - [pdf](https://arxiv.org/pdf/2606.22987)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, monocular depth, mesh reconstruction, manipulation, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?
- 作者：Yu Zhan, Guangcheng Chen, Hanjing Ye, Zhiqin Cheng, Zanjia Tong, Wenjun Xu, Hong Zhang
- 出版日期：2026-06-22
- 分类：3D Reconstruction & Multi-view Geometry (primary); Embodied / Robotics / AR Applications (secondary)
- 链接：arXiv: 2606.22987

### 一句话总结
本文系统评估了单视图网格重建方法在机器人相机旋转下的泛化能力，发现现有方法对相机转动鲁棒性差，并提出基于重力先验的优化方法可显著降低布局方向误差。

### 研究问题
当前单视图网格重建模型依赖于视角先验，当机器人相机在操作和导航过程中发生旋转（即分布外旋转）时，模型是否仍然能够输出一致的3D网格、空间布局和物理合理的结果？

### 核心思路/方法
1. 提出一种带有受控轴向滚转、俯仰和偏航扫描的评估协议，用于追踪单目深度估计、规范对象网格、相机空间布局和物理合理性中的误差链。
2. 在Aria Digital Twin数据集和真实Franka腕部相机序列上进行实验，分析旋转对MDE、布局漂移和碰撞穿透的影响。
3. 比较两阶段流水线（SAM3D+FoundationPose）与单阶段前馈布局预测的鲁棒性。
4. 提出“Gravity-Aware Refinement”方法，利用重力线索修正布局方向。

### 主要贡献
1. 首次系统评估单视图网格重建在机器人相机旋转下的泛化失败模式（3D不一致、错误布局、物理约束违反）。
2. 实验表明：相机旋转会导致MDE失真、布局漂移和碰撞穿透，而规范网格预测相对稳定。
3. 两阶段流水线（SAM3D+FoundationPose）比单阶段前馈预测更鲁棒。
4. 提出的重力感知细化将单阶段ICP布局方向误差降低47.1%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接回应机器人视觉中相机旋转这一实际部署难题，揭示了现有方法在分布外旋转下的严重退化，并提供了量化改进（误差降低47.1%），对从事3D重建、机器人感知和数字孪生研究的人员具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-view mesh reconstruction predicts object meshes and spatial layouts from a single observation, making it attractive for fast robot spatial reasoning and real-to-sim digital twins. However, robot-mounted cameras naturally rotate during manipulation and navigation, while learned single-view reconstruction models often rely on view-dependent priors and may generalize poorly to out-of-distribution camera rotations. Such rotations can introduce 3D inconsistencies, incorrect layouts, and violations of physical constraints, but this failure mode remains under-evaluated. We introduce an evaluation protocol with controlled axis-wise roll, pitch, and yaw sweeps to trace errors in monocular depth estimation (MDE), canonical object meshes, camera-space layout, and physical plausibility within a representative SAM3D-style pipeline. On the Aria Digital Twin dataset and a real Franka wrist-camera sequence, camera rotations induce MDE distortion, layout drift, and collision penetration, while canonical mesh predictions remain relatively stable. A two-stage SAM3D+FoundationPose pipeline is more robust than one-stage feed-forward layout prediction, and our Gravity-Aware Refinement reduces one-stage pairwise ICP-based layout-orientation error by 47.1$\%$. Our evaluation reveals that current single-view mesh reconstruction methods generalize poorly to robot camera rotation, and suggests that explicit gravity cues are important for reliable robotic single-view mesh reconstruction.

</details>

#### 2026-06-22 - Visual Geometry Transformer in the Wild: Distractor-Free 3D Reconstruction

**Authors:** Tianbo Pan, Xingyi Yang, Shizun Wang, Xinchao Wang
**Links:** [abs](https://arxiv.org/abs/2606.22787) - [pdf](https://arxiv.org/pdf/2606.22787)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visual Geometry Transformer in the Wild: Distractor-Free 3D Reconstruction  
- 作者：Tianbo Pan, Xingyi Yang, Shizun Wang, Xinchao Wang  
- 出版日期：2026-06-22  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2606.22787  

### 一句话总结
本文提出VGTW，一个端到端的多视图3D重建框架，通过抑制跨视图不一致的干扰物（如瞬时遮挡物），从存在干扰的真实场景中鲁棒地重建出干净点云。

### 研究问题
现有端到端多视图3D重建方法依赖“无干扰、完美几何一致性”的静态假设，无法处理真实场景中常见的瞬时遮挡、干扰物等不一致视图，导致重建失败。本文旨在解决在存在干扰物的情况下，如何从不一致的多视图图像中实现鲁棒的3D重建。

### 核心思路/方法
1. **Distractor-aware Training (DAT) 策略**：在注意力机制中，将每个视图的干净特征与受干扰物污染的特征分离，同时强制跨视图的特征一致性。  
2. **辅助掩码预测头**：使用新收集的、带有像素级干扰物掩码的数据集进行监督训练，使模型学会识别干扰物区域。  
3. **前馈架构**：训练后的VGTW可直接输出干净、无干扰的点云，无需额外的3D监督，且保持计算效率，兼容现有pipeline。

### 主要贡献
- 提出VGTW，首个能处理真实场景中干扰物和遮挡的端到端多视图3D重建框架。  
- 提出Distractor-aware Training策略，通过分离干扰特征与一致特征提升鲁棒性。  
- 收集并公开了带有像素级干扰物掩码的新数据集，用于辅助干扰感知训练。  
- 实验表明，VGTW在多样化真实场景中达到最先进性能，且具有良好的泛化能力。

### 局限性
摘要未提供足够信息。具体局限性（如对复杂干扰类型的鲁棒性边界、数据集规模约束、或对极端遮挡的处理能力）未在摘要中提及。

### 阅读优先级
**高**  
理由：该工作针对当前多视图3D重建方法在真实场景中的关键瓶颈（干扰物和遮挡），提出了实用的端到端解决方案，且无需额外3D监督，对推动该领域从理想环境走向实用化有重要意义。方法新颖、实验结果明确，值得精读。

</details>

<details>
<summary>Abstract</summary>

Current end-to-end multi-view 3D reconstruction methods achieve impressive results, but rely on a restrictive static assumption: the scenes is entire distractor-free with perfect cross-view geometry. This reliance on idealized inputs causes even the most advanced methods to fail in real-world settings, where transient distractors and occlusions present. To address this, we propose Visual Geometry Transformer in the Wild (VGTW), an end-to-end framework for robust reconstruction from inconsistent views. At its core, we isolate and suppress distractor-affected regions while preserving the consistent components across views. Specifically, we introduce a Distractor-aware Training (DAT) strategy that separates clean features from distractor-contaminated ones in the attention mechanism while enforcing feature consistency across images. To enable this, we train the model with an auxiliary mask prediction head, using supervision from a new dataset we collected with pixel-level distractor masks. The resulting VGTW model is a feed-forward network that directly outputs clean, distractor-free point clouds. Remarkably, it requires no additional 3D supervision, remains computationally efficient, and is compatible with existing pipelines. Extensive experiments validate our approach, demonstrating state-of-the-art performance and robust generalization in diverse, real-world scenarios.

</details>

#### 2026-06-20 - Geometric Reconstruction of Extrinsic Contact Trajectories using Tactile Sensing and Proprioception for Tool Manipulation

**Authors:** Seojung Min, Yoonjin Kim, Jeong-Jung Kim, Jung Kim
**Links:** [abs](https://arxiv.org/abs/2606.22251) - [pdf](https://arxiv.org/pdf/2606.22251)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, geometric reconstruction, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometric Reconstruction of Extrinsic Contact Trajectories using Tactile Sensing and Proprioception for Tool Manipulation
- 作者：Seojung Min, Yoonjin Kim, Jeong-Jung Kim, Jung Kim
- 出版日期：2026-06-20T22:28:16Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类）；Embodied / Robotics / AR Applications（次要分类）
- 链接：摘要URL：https://arxiv.org/abs/2606.22251；PDF：https://arxiv.org/pdf/2606.22251

### 一句话总结
本文提出了一种利用触觉传感和机器人本体感觉，通过几何推理方法在线重建工具末端在操作过程中与环境的接触轨迹的技术。

### 研究问题
如何在工具操作任务中，利用远离工具末端的、位于手爪处的触觉传感器，以及机器人本体感觉，重建移动的、难以直接感知的工具末端与环境之间的接触轨迹。

### 核心思路/方法
1.  **问题建模**：将工具末端轨迹重建建模为单点接触假设下的几何推理问题。
2.  **两步重建**：
    - **全局定位**：利用一个专门设计的校准段（该段近似固定点行为）来估计工具末端初始接触位置在世界坐标系中的大致位置。
    - **轨迹合成**：基于连续接触下由触觉标志物观测到的相对工具运动，合成完整的轨迹。

### 主要贡献
1.  提出一种利用手爪处触觉传感和机器人本体感觉，在线重建工具末端接触轨迹的方法。
2.  在包含多种轨迹、工具、手腕姿势和抓取配置的51次试验中，该方法实现了世界坐标系下8.59 ± 2.41 mm的轨迹RMSE和5.96 ± 1.16 mm的形状RMSE，运行频率可达14.00 ± 4.11 Hz。
3.  实验表明，工具末端轨迹的几何形状可以从抓取级触觉感知中稳定恢复，且在不同工具、手腕姿势和抓取配置下保持稳定。

### 局限性
摘要未提供足够信息。摘要未提及任何局限性。

### 阅读优先级
**中**。理由：该研究针对工具操作中利用触觉传感器间接重建末端接触轨迹这一具体问题，提出了有效的几何推理方法，在机器人操作领域具有一定应用价值。但摘要未深入讨论方法的原理细节（如具体几何模型公式）或实验对比，建议作为相关方向的技术参考，而非必读重点。

</details>

<details>
<summary>Abstract</summary>

Tactile sensing enables robots to perceive rich contact information at the grasp, supporting tasks such as object recognition, in-hand pose estimation, and slip detection. However, in many tool-mediated manipulation tasks, the interaction that determines task success occurs at the tool tip, away from the tactile sensor, making direct sensing of tool-environment contact difficult, particularly when the contact moves during interaction. In this work, we reconstruct the trajectory of extrinsic tool-tip contact using tactile sensing and robot proprioception. We formulate tool-tip trajectory reconstruction as a geometric inference problem under a single-point contact assumption. Our method first estimates the global tool-tip contact location from a calibration segment designed to approximate fixed-point behavior, and then reconstructs the full trajectory by composing relative tool motion estimated from tactile marker observations under continuous contact. Across n=51 trials with multiple trajectories, tools, wrist poses, and grasp configurations, the proposed pipeline achieves a trajectory RMSE of 8.59 +/- 2.41 mm in the world frame and a shape RMSE of 5.96 +/- 1.16 mm, while operating online at 14.00 +/- 4.11 Hz. Overall, the results show that extrinsic tool-tip trajectory geometry can be recovered consistently from grasp-level tactile sensing, with trajectory shape remaining stable across variations in tools, wrist poses, and grasp configurations.

</details>

#### 2026-06-18 - CalTennis: Large Multi-View Tennis Video Dataset and Benchmark of Monocular-to-3D Pose Estimation

**Authors:** Ilona Demler, Xinran Xie, Blake Werner, Anna Szczuka, Pietro Perona
**Links:** [abs](https://arxiv.org/abs/2606.20542) - [pdf](https://arxiv.org/pdf/2606.20542)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CalTennis: Large Multi-View Tennis Video Dataset and Benchmark of Monocular-to-3D Pose Estimation
- 作者：Ilona Demler, Xinran Xie, Blake Werner, Anna Szczuka, Pietro Perona
- 出版日期：2026-06-18
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.20542

### 一句话总结
CalTennis是一个大规模、多视角网球视频数据集与基准，用于评估野外从单目到三维的人体姿态估计，提供了比现有数据集大数倍的数据量，并揭示了模型在深度和足部接触方面的持续缺陷。

### 研究问题
如何构建一个大规模、低成本、可标准化的多视角视频基准，以评估和揭示单目到三维姿态估计方法在真实运动场景中的表现与不足。

### 核心思路/方法
- 收集超过1100万帧（51小时）的网球训练与比赛视频，覆盖40名选手，使用2-6台同步相机以60 Hz拍摄。
- 提出简单标准化的数据采集协议，无需专用设备或专业知识，并实现全自动视频标定与同步。
- 利用多视角设置实现低成本、无标签的评估，对比当前最先进的单目到三维姿态方法。
- 引入两个新性能指标（footwork和stability），并从定性的身体形状不一致性角度分析失败模式。

### 主要贡献
1. 发布大规模多视角网球视频数据集CalTennis，比现有野外人体运动视频数据集大10倍，比有动作捕捉真值的数据集大3倍。
2. 提供首个大规模同步多视角记录专业运动员动作的基准。
3. 通过基准测试发现当前模型在深度估计和足部接触一致性方面普遍存在困难。
4. 提出新的评估指标（footwork和stability），揭示之前未被充分探索的失败模式。

### 局限性
摘要未提供足够信息，无法明确描述该研究的具体局限性。

### 阅读优先级
高。理由：该工作贡献了显著超越现有规模的数据集和基准，针对单目到三维姿态估计这一活跃领域，揭示了现有模型的通用弱点并提出新评估指标，对后续研究和算法改进有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

The Caltech Tennis Dataset (CalTennis) is a large-scale video benchmark for evaluating monocular-to-3D pose estimation in the wild. CalTennis comprises over 11 million frames (51 hours) of tennis practice and match play from 40 players, captured with 2-6 synchronized cameras at 60 Hz. It is 10 times larger than existing in-the-wild human motion video datasets and 3 times larger than existing MOCAP-ground-truthed datasets, and it is the first large-scale benchmark to provide synchronized multi-view recordings of expert athletic motion. The multi-view setup enables inexpensive, label-free evaluation of monocular-to-3D pose estimation algorithms. We describe a simple, standardized protocol that enables data collection without specialized equipment or expertise, along with fully automated video calibration and synchronization. Benchmarking state-of-the-art monocular-to-3D pose methods on CalTennis, we find that while 3D joint angle recovery is now quite accurate, all models struggle to estimate depth and foot contact consistently. We further propose two novel performance metrics, footwork and stability, as well as qualitatively study body shape inconsistency. These metrics expose previously underexplored failure modes and point to concrete opportunities for improvement in pose estimation and action analysis.

</details>

#### 2026-06-18 - Towards 3D karst underwater scene reconstruction from rotating sonar data

**Authors:** Georgios Evangelos Margaritis, Lionel Lapierre, Simon Rohou, Zhi Yan, Andreas Nüchter, François Goulette
**Links:** [abs](https://arxiv.org/abs/2606.20322) - [pdf](https://arxiv.org/pdf/2606.20322)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, scene reconstruction, SLAM, surface reconstruction, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards 3D karst underwater scene reconstruction from rotating sonar data  
- 作者：Georgios Evangelos Margaritis, Lionel Lapierre, Simon Rohou, Zhi Yan, Andreas Nüchter, François Goulette  
- 出版日期：2026-06-18  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：摘要 https://arxiv.org/abs/2606.20322 | PDF https://arxiv.org/pdf/2606.20322  

### 一句话总结
本文提出了一套从旋转声纳数据重建水下岩溶三维场景的流水线，结合连续时间SLAM校正轨迹漂移与两阶段深度学习方法生成可漫游的3D网格。

### 研究问题
如何从稀疏、有噪声的声纳数据以及存在漂移的导航估计中，重建复杂且结构未知的水下岩溶管道的三维几何。

### 核心思路/方法
1. **轨迹校正**：采用连续时间SLAM方法纠正声纳探测过程中的轨迹漂移。  
2. **表面重建**：提出一种新颖的两阶段深度学习方法，从校正后的稀疏点云生成沉浸式、可导航的3D网格。  

### 主要贡献
- 构建了一套完整的水下岩溶场景重建流水线，将SLAM与深度学习表面重建相结合。  
- 提出两阶段深度学习方法，专门用于从稀疏声纳数据生成可用的3D网格。  

### 局限性
摘要未提供足够信息（例如：未说明方法在极端噪声或大规模场景下的表现，未提及与现有方法的定量对比结果，未分析实时性要求或计算成本）。

### 阅读优先级
**中**  
理由：该方法针对特定应用场景（水下岩溶探测）具有实际价值，且结合了SLAM与深度学习，技术上具有一定创新性。但摘要未提供实验对比与量化指标，缺乏对方法性能的直接评估，故优先级适中。

</details>

<details>
<summary>Abstract</summary>

Karst aquifers provide critical freshwater resources but pose significant hazards due to their complex and poorly understood subsurface geometry. Mapping these environments is challenging because sonar data from underwater exploration is sparse and noisy, while navigation estimates suffer from drift limiting standard 3D reconstruction methods. We present a pipeline for reconstructing underwater karst conduits from a sonar profiler. We combine a continuous-time SLAM approach to correct trajectory drift with a novel two-stage deep learning method for surface reconstruction, producing an immersive and navigable 3D mesh for hydrogeological analysis.

</details>

#### 2026-06-18 - MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM

**Authors:** Fan Zhu, Ziyu Chen, Peichen Liu, Yifan Zhao, Zhisong Xu, Hui Zhu, Hongxing Zhou, Sixun Liu, Chunmao Jiang
**Links:** [abs](https://arxiv.org/abs/2606.19874) - [pdf](https://arxiv.org/pdf/2606.19874)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, simultaneous localization and mapping, SLAM, visual SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM
- 作者：Fan Zhu, Ziyu Chen, Peichen Liu, Yifan Zhao, Zhisong Xu, Hui Zhu, Hongxing Zhou, Sixun Liu, Chunmao Jiang
- 出版日期：2026-06-18
- 分类：3D Reconstruction & Multi-view Geometry; Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.19874 ; PDF: https://arxiv.org/pdf/2606.19874

### 一句话总结
MMD-SLAM 是一种基于 3D 高斯泼溅的结构增强视觉 SLAM 框架，通过引入亚特兰大世界假设与多元高斯表征，在跟踪精度和建图质量上超越了现有方法（如 MonoGS）。

### 研究问题
现有 3DGS 驱动的视觉 SLAM 系统未能充分利用场景底层结构信息，导致渲染质量受限且建图结果不一致。

### 核心思路/方法
1. 采用亚特兰大世界假设，提取场景中的主导方向作为结构先验。
2. 设计多元高斯表征，显式编码结构先验。
3. 引入点-线融合策略进行位姿优化，利用 3D 线段提升跟踪鲁棒性并提供映射约束。
4. 提出高斯演化策略，使高斯体适应场景几何，并将结构线索融入全局优化。

### 主要贡献
- 提出点-线融合策略，增强位姿优化与映射约束。
- 设计基于亚特兰大世界假设的多元高斯表征，显式编码结构先验。
- 提出高斯演化策略，动态适应场景几何并参与全局优化。
- 在 ScanNet 上 ATE RMSE 降低 48.56%，在 Replica 上 PSNR 提升 5.71%，达到 SOTA 性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：论文在视觉 SLAM 与神经渲染交叉方向有明确创新点（结构增强与多高斯表征），且在公开数据集上取得显著性能提升。适合对该方向感兴趣的读者跟进，但对纯 SLAM 或纯渲染从业者而言，需进一步阅读原文评估方法的普适性。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has significantly boosted novel view synthesis and high-fidelity scene reconstruction, expanding the potential of 3DGS-based Visual Simultaneous Localization and Mapping (SLAM) methods. However, most existing systems fail to fully exploit the underlying structural information, which limits rendering quality and often leads to inconsistent maps. To address these limitations, we propose MMD-SLAM, a structure-enhanced Visual SLAM framework that leverages the Atlanta World (AW) assumption to guide a Multi-Meta Gaussian representation for photorealistic mapping. First, we introduce a point-line fusion strategy for pose optimization, where 3D line segments are incorporated to improve tracking robustness and provide additional constraints for mapping. Second, we design a Multi-Meta Gaussian representation with dominant directions, explicitly encoding structural priors from the AW hypothesis. Finally, we propose a Gaussian evolution strategy that adapts to scene geometry and incorporates structural cues into global optimization. Extensive experiments demonstrate that these innovations enable MMD-SLAM to achieve state-of-the-art performance in both tracking accuracy and mapping quality. e.g., our method achieves a 48.56% reduction in ATE RMSE on ScanNet and a 5.71% improvement in PSNR on Replica, compared with MonoGS.

</details>

#### 2026-06-18 - TIDY: Thermal Infrared Image Denoising via Wavelet Domain Entropy and Directional Stripe Index

**Authors:** Tai Hyoung Rhee, Dong-Guw Lee, Ayoung Kim
**Links:** [abs](https://arxiv.org/abs/2606.19813) - [pdf](https://arxiv.org/pdf/2606.19813)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TIDY: Thermal Infrared Image Denoising via Wavelet Domain Entropy and Directional Stripe Index
- 作者：Tai Hyoung Rhee, Dong-Guw Lee, Ayoung Kim
- 出版日期：2026-06-18T05:42:50Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要: https://arxiv.org/abs/2606.19813 ，PDF: https://arxiv.org/pdf/2606.19813

### 一句话总结
TIDY是一种轻量级的小波域热红外图像去噪方法，通过在真实数据上训练并引入小波熵和方向条纹指数作为损失项，在保持高推理速度（约34Hz）的同时实现了鲁棒的去噪效果，并提升了下游机器人任务（如热惯性里程计和单目深度估计）的性能。

### 研究问题
现有的热红外图像去噪方法存在精度与效率的权衡问题：要么因速度慢而无法满足机器人任务的在线部署需求，要么对严重噪声（尤其室内低热对比度下）鲁棒性不足，且通常依赖合成噪声进行训练。

### 核心思路/方法
1. 设计轻量级小波域去噪网络，在小波域中显式地将噪声与结构内容分离，从而降低空间复杂度并提升推理速度。
2. 提出两个新的度量指标**小波熵**（Wavelet Entropy）和**小波方向条纹指数**（Wavelet Directional Stripe Index）作为互补的损失项，分别用于抑制随机噪声和条纹伪影。
3. 使用真实的热红外清洁-配对数据（而非合成噪声）进行训练，并在室内严重退化场景与零样本设置下评估鲁棒性。

### 主要贡献
1. 提出轻量级小波域去噪器TIDY，在真实TIR数据上训练，推理速度达约34Hz，适合在线部署。
2. 引入小波熵和方向条纹指数作为损失项，实现针对随机噪声和条纹噪声的显式抑制。
3. 在室内严重退化及零样本场景下，验证了TIDY在下游机器人任务（热惯性里程计、单目深度估计）中的一致性提升。
4. 开源了代码和数据集。

### 局限性
摘要未提供足够信息，例如在极端噪声水平、不同传感器类型或更长序列上的表现；也未提及对计算资源的具体需求或潜在的泛化限制。

### 阅读优先级
中。理由：该方法针对热红外图像去噪在机器人应用中的效率与鲁棒性瓶颈，提出了轻量级且创新的小波域解决方案，但摘要未提供与现有方法的详细数值对比，且作为2026年发表的工作，当前时效性一般。若读者关注机器人感知或热红外成像，可阅读；若对去噪通用方法更感兴趣，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Thermal infrared (TIR) imaging has been a popular choice for field robotics due to its robust perception capability under low light visual degradation, but it suffers from severe stochastic and fixed-pattern noise that breaks downstream estimation. This noise is intensified indoors due to low thermal contrast and uniform temperature distributions, contributing to the relative lack of indoor TIR deployments. Existing TIR denoising methods exhibit a poor accuracy-efficiency tradeoff, either too slow for online deployment required in robotics or insufficiently robust to severe degradation, while typically being trained on synthetic noise. Addressing these problems, we propose TIDY, a lightweight wavelet-domain denoiser trained on real clean-noisy TIR data. By reformulating TIR denoising in the wavelet domain, TIDY explicitly disentangles noise from structural content, enabling targeted suppression with reduced spatial complexity, significantly improving inference speed over prior methods (~34Hz). TIDY introduces two new metrics, Wavelet Entropy and Wavelet Directional Stripe Index, as complementary loss terms to explicitly suppress stochastic noise and stripe artifacts. Across severe indoor corruption and zero-shot settings, TIDY improves robustness and yields consistent gains in downstream robotics tasks including thermal inertial odometry and monocular depth estimation. Code and dataset is available at: https://github.com/williamrheeth/TIDY

</details>

#### 2026-06-17 - Hardware- and Vision-in-the-Loop Validation of Deep Monocular Pose Estimation for Autonomous Maritime UAV Flight

**Authors:** Maneesha Wickramasuriya, Beomyeol Yu, Jaden Shin, Mason Huslig, Taeyoung Lee, Murray Snyder
**Links:** [abs](https://arxiv.org/abs/2606.19176) - [pdf](https://arxiv.org/pdf/2606.19176)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hardware- and Vision-in-the-Loop Validation of Deep Monocular Pose Estimation for Autonomous Maritime UAV Flight
- 作者：Maneesha Wickramasuriya, Beomyeol Yu, Jaden Shin, Mason Huslig, Taeyoung Lee, Murray Snyder
- 出版日期：2026-06-17T15:18:11Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.19176

### 一句话总结
本文提出一个硬件与视觉在环的验证框架，将逼真海事渲染视图输入深度单目位姿估计器，并结合延迟卡尔曼滤波与IMU数据融合，实现了面向自主海航UAV飞行的闭环室内测试。

### 研究问题
在船舶甲板上执行自主无人机起降时，如何规避高成本、受天气影响且风险大的实海验证，通过硬件在环手段可靠地测试基于视觉的相对位姿估计及闭环控制性能。

### 核心思路/方法
1. **硬件与视觉在环框架**：搭建全自主室内飞行环境，同时生成逼真（photorealistic）海事背景的渲染视图。
2. **深度单目位姿估计**：在无人机上运行基于Transformer架构的单目位姿估计器，处理渲染视图。
3. **延迟融合与控制**：利用延迟卡尔曼滤波器将滞后的视觉测量与高频IMU数据融合，为几何控制提供一致的状态估计。
4. **实验验证**：开展自主起飞、轨迹跟踪与着陆实验，展示稳定闭环飞行。

### 主要贡献
- 提出了一个兼顾硬件与视觉在环的验证框架，能捕捉纯仿真中缺失的感知延迟、异步更新和计算约束等嵌入式效应。
- 为发展海事UAV自主性提供了安全且硬件真实的中间测试阶段，降低了实际舰载部署前的验证风险。

### 局限性
摘要未提供关于方法在非海事场景或更复杂气象条件下的泛化能力、估计器精度量化、以及具体计算资源开销等信息。

### 阅读优先级
**中**。  
理由：该方法面向特定场景（海事UAV）的软硬件联合验证，创新在于验证框架而非核心算法本身。若研究领域涉及无人机自主着陆、硬件在环仿真或视觉-惯性融合，则有参考价值；否则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Autonomous UAV operations on ships require reliable vision-based relative pose estimation, yet at-sea validation is costly, weather-dependent, and risky. This paper presents a hardware-validated vision-in-the-loop framework that enables fully autonomous indoor flight while emulating photorealistic maritime environments. Rendered maritime views are processed onboard by a deep transformer-based monocular pose estimator. Delayed vision measurements are fused with high-rate IMU data using a delayed Kalman filter to provide consistent state estimates for geometric control. The system captures critical embedded effects, including perception latency, asynchronous updates, and computational constraints, that are absent in pure simulation. Autonomous takeoff, trajectory tracking, and landing experiments demonstrate stable closed-loop flight. The results establish a safe and hardware-realistic intermediate stage for developing maritime UAV autonomy prior to shipboard deployment.

</details>

#### 2026-06-17 - Sensor Configuration Matters: A Systematic Evaluation of Multimodal SLAM on Quadruped Robots

**Authors:** Roberto Corlito, Fabian Schmidt, Nils Seibert, Markus Enzweiler, Abhinav Valada, Arne Roennau
**Links:** [abs](https://arxiv.org/abs/2606.19067) - [pdf](https://arxiv.org/pdf/2606.19067)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sensor Configuration Matters: A Systematic Evaluation of Multimodal SLAM on Quadruped Robots
- 作者：Roberto Corlito, Fabian Schmidt, Nils Seibert, Markus Enzweiler, Abhinav Valada, Arne Roennau
- 出版日期：2026-06-17
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.19067

### 一句话总结
本文系统评估了不同硬件传感器配置（摄像头类型、快门技术、惯性传感器等级）对四足机器人多模态SLAM性能的影响，发现立体配置优于单目和RGB-D，全局快门优于卷帘快门，且标准惯性集成在激烈足式运动下反而可能降低视觉SLAM性能。

### 研究问题
四足机器人在激烈运动（如足部冲击震动、高频机械振动、快速角旋转）带来的独特传感器挑战下，硬件级别的传感器配置如何影响视觉、视觉-惯性及LiDAR-视觉-惯性SLAM方法的定位精度、算法鲁棒性和计算资源利用？

### 核心思路/方法
利用ANYmal D四足机器人上录制的GrandTour数据集，对不同状态最先进的视觉、视觉-惯性和LiDAR-视觉-惯性SLAM方法进行系统评估。通过隔离和量化摄像头模态（单目、立体、RGB-D）、快门技术（全局快门、卷帘快门）以及惯性传感器等级的影响，分析它们在定位精度、算法鲁棒性和计算资源利用方面的权衡。

### 主要贡献
1. 首次针对四足机器人激进运动动力学引发的传感器挑战，系统评估硬件传感器配置对多模态SLAM性能的影响。
2. 实验揭示：立体配置显著优于单目和RGB-D；全局快门相机显著减少运动引发的跟踪失败；标准的惯性集成在激烈足式运动下可能降低基于视觉系统的性能。
3. 为在敏捷四足系统上设计定制传感器负载以实现可靠感知，提供了具体的设计指南。

### 局限性
摘要未提供足够信息。摘要未提及实验范围之外的局限，例如是否在多种地形上验证、是否考虑不同四足机器人型号、是否存在计算资源或传感器成本方面的约束等。

### 阅读优先级
高。理由：该研究针对四足机器人领域的SLAM关键实际问题——传感器硬件配置对性能的影响进行系统评估，结果具有直接工程应用价值，可为实际机器人系统设计提供具体指导。

</details>

<details>
<summary>Abstract</summary>

Autonomous navigation of quadrupedal robots in diverse environments fundamentally relies on resilient Simultaneous Localization and Mapping (SLAM). While visual-inertial SLAM has matured across wheeled, handheld, and aerial platforms, a critical evaluation gap remains regarding how hardware-level sensor configurations affect performance under the aggressive dynamics of legged locomotion. Quadrupeds introduce distinct embodiment-induced sensory challenges, including foot-impact shocks, high-frequency mechanical vibrations, and rapid angular rotations, which degrade standard perception pipelines. To address this gap, we present a systematic evaluation of state-of-the-art visual, visual-inertial, and LiDAR-visual-inertial SLAM methods using the GrandTour dataset recorded on an ANYmal D quadruped. We isolate and quantify the impacts of camera modalities, shutter techniques, and inertial sensor tiers, analyzing their trade-offs across localization accuracy, algorithmic robustness, and computational resource utilization. Our empirical findings demonstrate that hardware selection has substantial influence on system resilience: stereo configurations consistently outperform monocular and RGB-D modalities, global shutter cameras significantly mitigate motion-induced tracking failures compared to rolling shutter cameras, and, crucially, standard inertial integration can degrade the performance of primarily vision-based frameworks under harsh legged locomotion. These insights additionally offer concrete design guidelines for tailoring custom sensor payloads to achieve dependable perception on agile legged systems.

</details>

#### 2026-06-17 - TactSpace: Learning a Physics-enriched Shared Latent Space for Tactile Sim-to-Real Transfer

**Authors:** Arunim Joarder, Arjun Bhardwaj, René Zurbrügg, Mayank Mittal, Florin Püntener, Sira Bielefeldt, Cosmin Roman, Vaishakh Patil, Marco Hutter
**Links:** [abs](https://arxiv.org/abs/2606.18959) - [pdf](https://arxiv.org/pdf/2606.18959)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** shape reconstruction, geometric reconstruction, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TactSpace: Learning a Physics-enriched Shared Latent Space for Tactile Sim-to-Real Transfer
- 作者：Arunim Joarder, Arjun Bhardwaj, René Zurbrügg, Mayank Mittal, Florin Püntener, Sira Bielefeldt, Cosmin Roman, Vaishakh Patil, Marco Hutter
- 出版日期：2026-06-17
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.18959

### 一句话总结
本文提出一个多模态表示学习框架，通过对齐模拟与真实触觉信号（如模拟穿透深度和真实电容）到一个共享潜在空间，实现零样本触觉模拟到真实迁移，并显著降低力预测和形状重建误差。

### 研究问题
当前模拟器无法精确建模触觉传感器的复杂形变和传导机制，阻碍了机器人学习中的触觉模拟到真实迁移。

### 核心思路/方法
构建一个多模态表示学习框架，使用模态特定编码器将异质触觉观测（如模拟穿透深度、真实电容）投影到一个共享潜在空间。训练时结合自重建、交叉重建目标和对比对齐，鼓励生成模态不变且信息丰富的表示。

### 主要贡献
1. 提出一种无需精确原始信号模拟的触觉模拟到真实迁移方法，仅需对齐共享潜在空间。
2. 在压头形状识别、力预测和几何重建任务上实现了零样本模拟到真实迁移。
3. 相比基线，力预测误差降低16.7%，形状重建误差降低45.8%。
4. 发布一个基于Warp的、适用于Isaac Lab的惩罚性触觉模拟模型，支持可扩展触觉数据生成。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文提出了一种解决触觉模拟到真实迁移瓶颈的新框架，具有明确的跨模态对齐策略和显著的性能提升（如力预测和形状重建误差降低），且附带开源模拟工具，对机器人操控和触觉学习领域有实际应用价值。

</details>

<details>
<summary>Abstract</summary>

Tactile sensing provides direct measurements of contact interactions that are essential for robotic manipulation. However, current simulators lack the fidelity to faithfully model the complex deformation and transduction mechanics of tactile sensors, severely hindering sim-to-real transfer in robot learning pipelines. To address this challenge, we propose a multi-modal representation learning framework that aligns heterogeneous tactile modalities within a shared latent space, eliminating the need for accurate raw-signal simulation while preserving relevant contact information. Our approach employs modality-specific encoders to project diverse tactile observations, such as simulated penetration depth and real-world capacitance, into a common embedding space. The model is trained using self- and cross-reconstruction objectives alongside contrastive alignment, encouraging modality-invariant yet information-rich representations. We evaluate the learned embeddings on indenter shape identification, force prediction, and geometric reconstruction tasks, training exclusively in simulation and testing directly on real sensor measurements. Our results demonstrate zero-shot sim-to-real transfer across physically dissimilar representations. Furthermore, incorporating multi-physics simulation modalities yields more informative embeddings that transfer across diverse downstream tasks, demonstrating a 16.7% reduction in force prediction error and a 45.8% reduction in shape reconstruction error. Finally, we release an efficient Warp-based implementation of a penalty-based tactile simulation model for Isaac Lab, enabling scalable tactile data generation.

</details>

#### 2026-06-17 - Learned Radius Estimation for UDF-Based Point Cloud Reconstruction

**Authors:** Eito Ogawa, Hiroshi Watanabe
**Links:** [abs](https://arxiv.org/abs/2606.18787) - [pdf](https://arxiv.org/pdf/2606.18787)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** point cloud reconstruction, surface reconstruction, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learned Radius Estimation for UDF-Based Point Cloud Reconstruction
- 作者：Eito Ogawa, Hiroshi Watanabe
- 出版日期：2026-06-17
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.18787

### 一句话总结
提出一个基于学习的逐查询点支持半径选择器，用于提升局部补片无符号距离场（UDF）方法在点云重建中的精度。

### 研究问题
局部补片UDF方法依赖“支持半径”来定义每个点的局部邻域范围，传统上该半径为固定值或通过一维曲率启发式选取，无法适应局部几何变化，导致重建精度受限。

### 核心思路/方法
提出一个可学习的逐查询点半径选择器，该选择器预测连续的支持半径，并作为插件接入冻结的LoSF-UDF骨干网络。训练时，通过抛物线插值缓存UDF误差曲线，获取离网格的目标半径作为监督信号。

### 主要贡献
- 首次针对UDF点云重建提出可学习的支持半径估计方法。
- 设计了一个可插拔的半径选择器，无需重新训练骨干网络。
- 提出基于抛物线插值的离网格监督方式，从缓存UDF误差曲线获得目标半径。
- 实验证明该方法在提高精细尺度重建精度方面的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该工作聚焦于UDF重建中的具体参数（支持半径）优化，属于技术改进型研究，对从事点云重建或隐式表面学习的读者有一定参考价值；但摘要未给出定量实验对比或消融结果，需进一步阅读全文评估实际增益。

</details>

<details>
<summary>Abstract</summary>

Surface reconstruction from point clouds is important for consumer-grade 3D capture, including AR/VR and indoor scanning. Local-patch Unsigned Distance Field (UDF) methods are lightweight and generalizable, but their accuracy depends on the support radius, traditionally fixed or selected by a one-dimensional curvature heuristic that cannot capture heterogeneous local geometry. We propose a learned per-query radius selector that predicts a continuous support radius and plugs into a frozen LoSF-UDF backbone. The selector is trained using off-grid target radii obtained by parabolic interpolation of cached UDF error curves. Experiments show improved fine-scale reconstruction accuracy.

</details>

#### 2026-06-17 - Splaxel: Efficient Distributed Training of 3D Gaussian Splatting for Large-scale Scene Reconstruction via Pixel-level Communication

**Authors:** Wenqi Jia, Zhewen Hu, Ying Huang, Yu Gong, Stavros Kalafatis, Yuke Wang, Wei Niu, Chengming Zhang, Ang Li, Sheng Di, Yuede Ji, Bo Fang, Miao Yin
**Links:** [abs](https://arxiv.org/abs/2606.18588) - [pdf](https://arxiv.org/pdf/2606.18588)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Splaxel: Efficient Distributed Training of 3D Gaussian Splatting for Large-scale Scene Reconstruction via Pixel-level Communication
- 作者：Wenqi Jia, Zhewen Hu, Ying Huang, Yu Gong, Stavros Kalafatis, Yuke Wang, Wei Niu, Chengming Zhang, Ang Li, Sheng Di, Yuede Ji, Bo Fang, Miao Yin
- 出版日期：2026-06-17
- 分类：3D Reconstruction & Multi-view Geometry（主分类）; Neural Scene Representations & Rendering（次分类）
- 链接：摘要页 https://arxiv.org/abs/2606.18588 ；PDF https://arxiv.org/pdf/2606.18588

### 一句话总结
Splaxel 提出基于像素级通信的分布式3D高斯泼溅（3DGS）训练框架，通过局部渲染与全局合成避免高斯同步，在百万级高斯规模场景下实现最高7.6倍加速，同时保持高重建质量。

### 研究问题
现有分布式3DGS训练方法存在两大难题：要么将场景分割为孤立区域导致全局不一致，要么依赖全局高斯级交换导致通信量随场景规模急剧增长，迭代时间被通信主导。如何实现通信高效且数学一致的分布式大规模场景3DGS训练？

### 核心思路/方法
- **像素级局部渲染与全局合成**：每个GPU渲染自己负责的局部高斯子集，仅交换部分像素值，而非同步高斯参数。
- **通信成本稳定**：该机制使得通信开销不随场景中高斯数量增加而增长。
- **冗余减少策略**：通过几何与透射可见性预测（geometric and transmittance visibility prediction）降低像素级冗余。
- **冲突避免的相机视角合并**：采用conflict-free camera-view consolidation提升GPU利用率。

### 主要贡献
1. 首次提出基于像素级通信的分布式3DGS训练框架Splaxel，避免高斯级同步带来的通信瓶颈。
2. 在数学一致性的前提下，保持通信成本与场景规模无关，实现了可扩展的分布式训练。
3. 融合可见性预测与视角合并的优化，进一步减少像素冗余并提升GPU利用效率。
4. 在包含多达1.2亿个高斯的大规模数据集上，相比现有最优分布式3DGS框架获得最高7.6倍加速，且重建质量接近。

### 局限性
摘要未提供足够信息，未说明该方法在哪些场景或条件下效果不佳、内存消耗、收敛稳定性或对相机数量/视角分布的敏感性。

### 阅读优先级
**高**  
理由：该工作直接针对分布式3DGS训练的关键瓶颈——通信效率，提出新颖的像素级通信范式，实验显示显著加速，适用于大规模场景重建，对相关领域研究者和工程人员具有明确参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables high-fidelity and real-time 3D scene reconstruction, but scaling training to large-scale scenes requires optimizing hundreds of millions of Gaussians across multiple GPUs. Existing distributed approaches either partition scenes into isolated regions, causing global inconsistency, or rely on global Gaussian-level exchanges, which lead to substantial growth in inter-GPU communication and quickly dominate iteration time. We propose Splaxel, a communication-efficient distributed 3DGS training framework based on pixel-level local rendering and global composition. Instead of synchronizing Gaussians, each GPU renders its local subset and exchanges only partial pixel values, maintaining mathematical consistency while keeping communication cost stable as the scene size increases. Splaxel further reduces pixel-level redundancy through geometric and transmittance visibility prediction and improves GPU utilization via conflict-free camera-view consolidation. Evaluated on large-scale datasets with up to 120M Gaussians, Splaxel achieves up to 7.6$\times$ speedup over the state-of-the-art distributed 3DGS framework while preserving high reconstruction quality.

</details>

#### 2026-06-16 - SP-TransientBench: A Real-Captured Single Photon Perception Benchmark

**Authors:** Hongzhou Dong, Zili Zhang, Ziting Wen, Yiheng Qiang, Runrong Deng, Wenle Dong, Ziwen Jiang, Xinyang Li, Rui Lu, Shuoyao Sun, Wenyu Wang, Ziyi Xia, Haitao Zheng, Guodong Shi, Xiaoqiang Ren
**Links:** [abs](https://arxiv.org/abs/2606.18952) - [pdf](https://arxiv.org/pdf/2606.18952)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, depth estimation, geometric reconstruction, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SP-TransientBench: A Real-Captured Single Photon Perception Benchmark
- 作者：Hongzhou Dong, Zili Zhang, Ziting Wen, Yiheng Qiang, Runrong Deng, Wenle Dong, Ziwen Jiang, Xinyang Li, Rui Lu, Shuoyao Sun, Wenyu Wang, Ziyi Xia, Haitao Zheng, Guodong Shi, Xiaoqiang Ren
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.18952

### 一句话总结
本文提出了一个名为SP-TransientBench的真实拍摄单光子感知多任务基准测试集，包含10个场景、10297个视图，并提供了完整的飞行时间直方图、校准相机位姿和3D语义标注，旨在系统评估单光子LiDAR在深度估计、多视图重建和3D语义理解等难题上的性能。

### 研究问题
现有单光子感知研究多基于模拟数据或小规模受控采集，缺乏对真实世界单光子感知（包括深度估计、多视图重建和3D语义理解）的系统性评估基准。

### 核心思路/方法
构建一个真实采集的多任务基准测试集：
1. 使用固态单光子LiDAR（分辨率为256×192）采集10个多样化场景，共10297个视图。
2. 为每个视图提供包含多返回行为的完整飞行时间直方图、标准化元数据以及用于多视图评估的校准相机位姿。
3. 为选定场景提供13类3D语义标注。
4. 针对每个任务提供专用数据划分和评估协议，以实现可复现的基准测试。

### 主要贡献
1. 提出了第一个真实采集、面向多任务（深度估计、多视图重建、3D语义理解）的单光子感知基准测试集。
2. 提供了覆盖10个场景、10297个视图的完整飞行时间直方图和多返回行为数据。
3. 提供了校准相机位姿和13类3D语义标注，支持标准化和可复现的评估。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该基准测试直接填补了单光子感知领域缺乏真实世界系统性评估基准的空白，提供了大规模、多任务、标注完整的数据集，对从事单光子LiDAR、3D重建和语义理解的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-photon LiDAR (SPL) based on single-photon avalanche diode (SPAD) sensing enables time-resolved photon measurements with extreme sensitivity, offering unique potential for active 3D perception in photon-starved scenarios.However, real-world single photon perception remains fundamentally challenging due to unique measurement noise and complex multi-return transient phenomena, which jointly complicate geometric reconstruction and semantic scene understanding. Despite growing interest in SPAD-based sensing, existing studies are largely limited to simulated data or small-scale controlled captures. As a result, systematic evaluation of real-world single photon perception across depth estimation, multi-view reconstruction, and 3D semantic understanding remains underexplored. To bridge this gap, we introduce SP-TransientBench (STB), a real-captured multi-task benchmark for single photon perception. SP-TransientBenc comprises 10 diverse scenes and 10,297 views captured using a solid-state single-photon LiDAR at $256\times192$ resolution. Each view provides full time-of-flight histograms with multi-return behavior,standardized metadata, and calibrated camera poses for multi-view evaluation. We further provide 13-class 3D semantic annotations for selected scenes. By providing dedicated data splits and evaluation protocols for each task, STB enables consistent and reproducible benchmarking of real-world single photon perception across multiple 3D vision problems. The dataset and code will be released upon acceptance.

</details>

#### 2026-06-16 - Neural Tree Reconstruction for the Open Forest Observatory

**Authors:** Marissa Ramirez de Chanlatte, Arjun Rewari, Trevor Darrell, Derek J. N. Young
**Links:** [abs](https://arxiv.org/abs/2606.18153) - [pdf](https://arxiv.org/pdf/2606.18153)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, NeRF, radiance, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Neural Tree Reconstruction for the Open Forest Observatory  
- 作者：Marissa Ramirez de Chanlatte, Arjun Rewari, Trevor Darrell, Derek J. N. Young  
- 出版日期：2026-06-16  
- 分类：3D 重建与多视角几何  
- 链接：摘要：https://arxiv.org/abs/2606.18153；PDF：https://arxiv.org/pdf/2606.18153  

### 一句话总结
本文探索将神经辐射场（NeRF）引入开放森林观测站（OFO）数据集，以提升森林三维地图的重建质量，并指出其对气候应用的重要性。

### 研究问题
如何克服现有基于运动恢复结构（SfM）方法在森林三维重建中产生的伪影、细节缺失及林下可见性受限等问题，从而提升 OFO 数据集的质量。

### 核心思路/方法
利用神经辐射场（NeRF）等先进三维重建技术替代经典 SfM 方法，因其能够产生更高质量、更鲁棒的重建结果，并对稀疏视图和先验知识有更好的支持。

### 主要贡献
- 提出了将 NeRF 整合到 OFO 数据集中的探索性思路。
- 概述了未来支持更先进三维视觉模型的工作方向。
- 强调了高质量三维重建对于林业应用（如再造林优先、野火隐患减少、碳汇监测）的重要性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
低。理由：本文目前仅停留在“探索思路”和“未来工作展望”阶段，未给出具体实验或定量结果，缺乏实质性技术贡献。对于关注成熟方法的读者而言，参考价值有限。

</details>

<details>
<summary>Abstract</summary>

The Open Forest Observatory (OFO) is a collaboration across universities and other partners to make low-cost forest mapping accessible to ecologists, land managers, and the general public. The OFO is building both a database of geospatial forest data as well as open-source methods and tools for forest mapping by uncrewed aerial vehicle. Such data are useful for a variety of climate applications including prioritizing reforestation efforts, informing wildfire hazard reduction, and monitoring carbon sequestration. In the current iteration of the OFO's forest map database, 3D tree maps are created using classical structure-from-motion techniques. This approach is prone to artifacts, lacks detail, and has particular difficulty on the forest floor where the input data (overhead imagery) has limited visibility. These reconstruction errors can potentially propagate to the downstream scientific tasks (e.g. a wildfire simulation.) Advances in 3D reconstruction, including methods like Neural Radiance Fields (NeRF), produce higher quality results that are more robust to sparse views and support data-driven priors. We explore ways to incorporate NeRFs into the OFO dataset, outline future work to support even more state-of-the-art 3D vision models, and describe the importance of high-quality 3D reconstructions for forestry applications.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-22 - Learning Stable Canonical Worlds for Novel View Synthesis and Beyond

**Authors:** Xiaoyu Xu, Jian Zou, Sheyang Tang, Zhihua Wang, Jing Liao, Kede Ma
**Links:** [abs](https://arxiv.org/abs/2606.23027) - [pdf](https://arxiv.org/pdf/2606.23027)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Stable Canonical Worlds for Novel View Synthesis and Beyond
- 作者：Xiaoyu Xu, Jian Zou, Sheyang Tang, Zhihua Wang, Jing Liao, Kede Ma
- 出版日期：2026-06-22
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.23027；PDF：https://arxiv.org/pdf/2606.23027

### 一句话总结
本文提出CanonicalGS，一种前馈式高斯泼溅管道，通过将杂乱的视图证据融合到稳定的规范潜在世界中，实现了更鲁棒的新视图合成，并能迁移到下游视觉感知任务。

### 研究问题
当前前馈式高斯泼溅（FFGS）方法依赖视图依赖预测，当输入视图增加时，会积累噪声或冗余证据，而无法收敛到稳定的场景表示。如何将多视图观测映射为稳定、以场景为中心的表示是主要研究问题。

### 核心思路/方法
- 首先从深度、语义特征和不确定性估计中提取每视图的证据。
- 然后利用不确定性感知融合，将这些证据在规范潜在世界中聚合。
- 通过强调可靠观测并抑制不确定或冗余证据，得到可扩展的场景表示。

### 主要贡献
- 提出CanonicalGS管道，将杂乱多视图观测转化为稳定的规范场景表示。
- 在新视图合成上，峰值信噪比提升最高达2.5 dB。
- 在语义分割等下游任务上，准确率提升11%。
- 表明该方法能更有效地随输入视图增加而扩展。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直接面向新视图合成这一核心问题，并显示了明确且可量化的性能提升（2.5 dB PSNR和11%语义分割准确率），同时具备跨任务迁移能力，对神经场景表示与渲染方向的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward Gaussian splatting (FFGS) facilitates real-time novel view synthesis, yet current methods often remain tied to view-dependent predictions. As more input views are added, they may accumulate noisy or redundant evidence instead of converging to a stable scene representation. In this paper, we introduce CanonicalGS, a feed-forward pipeline that maps cluttered multi-view observations into a stable, scene-centric representation. CanonicalGS first extracts view-centric evidence from depth, semantic features, and uncertainty estimates, and then aggregates this evidence in a canonical latent world using uncertainty-aware fusion. By emphasizing reliable observations while suppressing uncertain or redundant ones, CanonicalGS produces representations that scale more effectively for novel view synthesis and transfer to downstream visual perception tasks. Experiments show up to a $2.5$ dB improvement in peak signal-to-noise ratio for synthesizing novel views and an $11\%$ gain in semantic segmentation accuracy.

</details>

#### 2026-06-21 - Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography

**Authors:** Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang
**Links:** [abs](https://arxiv.org/abs/2606.22525) - [pdf](https://arxiv.org/pdf/2606.22525)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography
- 作者：Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang
- 出版日期：2026-06-21
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.22525

### 一句话总结
本文发现稀疏视角三维高斯断层重建中存在投影质量提升但体积重建恶化的“投影-体积保真度发散”问题，并提出名为LADES的无真值优化控制器来解决该漂移。

### 研究问题
稀疏视角计算机断层扫描重建是一个严重病态逆问题，近期3D高斯喷射方法提供了高效显式表示。但研究发现，在投影域优化可能产生误导：渲染投影可能不断改善，而重建的体积却在退化。如何诊断和控制这种表示层面的优化漂移？

### 核心思路/方法
1. 识别故障模式：提出投影-体积保真度发散（PVFD），一种由各向异性高斯变形和稀疏Radon约束下视图特定基元共适应引起的优化漂移。
2. 诊断指标：引入几何和体积层级的诊断方法，测量针状高斯退化和体素化密度场的稳定性。
3. 控制器LADES：包含两个无真值组件——线性退火丢弃（在早期训练时施加强随机掩蔽，破坏过早的基元共适应，再逐步恢复全容量进行结构巩固）和结构感知早停（根据高斯种群增长饱和而非验证PSNR来终止稠密化）。

### 主要贡献
- 识别并形式化了稀疏视角高斯层析中的投影-体积保真度发散（PVFD）故障模式。
- 引入几何和体积层级的诊断工具，用于量化高斯退化与体密度场稳定性。
- 提出无真值优化控制器LADES，能够提高体积保真度、抑制结构退化、大幅减少训练时间，同时保持有竞争力的投影精度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该工作直接针对稀疏视角3D高斯重建中核心的优化漂移问题，提出新颖的诊断与无真值控制方案，实验显示在体积保真度、训练效率方面有显著改进。对于从事断层重建、神经场景表示或逆向渲染的研究者具有较重要的参考价值，且问题陈述清晰、方法简洁有力。

</details>

<details>
<summary>Abstract</summary>

Sparse-view computed tomography is a severely ill-posed inverse problem, where recent 3D Gaussian Splatting methods offer an efficient explicit representation for tomographic reconstruction. However, we find that projection-domain optimization can be misleading in this setting: the rendered projections may continue to improve while the reconstructed volume deteriorates. We identify this failure mode as Projection-Volume Fidelity Divergence (PVFD), a representation-level optimization drift caused by anisotropic Gaussian deformation and view-specific primitive co-adaptation under sparse Radon constraints. To characterize this behavior, we introduce geometry- and volume-level diagnostics that measure needle-like Gaussian degeneration and the stability of the voxelized density field. Based on these observations, we propose LADES, a ground-truth-free optimization controller for sparse-view Gaussian tomography. LADES combines Linearly Annealed Dropout, which applies strong stochastic masking in early training to disrupt premature primitive co-adaptation and gradually restores full capacity for structural consolidation, with Structure-Aware Early Stopping, which terminates densification according to the saturation of Gaussian population growth rather than validation PSNR. Experiments on sparse-view CT reconstruction show that LADES improves volumetric fidelity, suppresses structural degeneration, and substantially reduces training time while maintaining competitive projection accuracy. These results suggest that robust Gaussian-based tomography requires monitoring and controlling volumetric structure, rather than optimizing projection fit alone.

</details>

#### 2026-06-21 - Lighting-Consistent Object Transfer Across Radiance Fields

**Authors:** Nicolás Violante, George Kopanas, Linus Franke, Julien Philip, George Drettakis
**Links:** [abs](https://arxiv.org/abs/2606.22481) - [pdf](https://arxiv.org/pdf/2606.22481)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lighting-Consistent Object Transfer Across Radiance Fields
- 作者：Nicolás Violante、George Kopanas、Linus Franke、Julien Philip、George Drettakis
- 出版日期：2026-06-21
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.22481

### 一句话总结
本文提出了一种利用扩散模型对跨辐射场对象迁移中的光照不一致性进行调和的方法，并通过后优化步骤将调和后的多视角结果整合为一致的3D高斯泼溅表示。

### 研究问题
如何将对象从一个3DGS场景迁移到另一个场景时，消除因光照条件不同导致的视觉不真实感。

### 核心思路/方法
1. 用户从源场景提取对象并合成到目标场景，生成光照不一致的多视角合成图像。
2. 使用一个扩散模型对每张不一致的合成图像进行调和（即将其修饰为光照一致的输出）。
3. 对调和后的所有视角执行后优化步骤，最终巩固为一个完整的3DGS表示。
4. 扩散模型采用混合数据集训练，该数据集由成对的（不一致合成输入，一致输出）图像组成，混合了合成数据、生成数据和真实数据。

### 主要贡献
- 提出一个完整的3D解决方案，支持用户从源场景提取对象并合成到目标场景。
- 引入一个专用于调和光照不一致合成图像的扩散模型。
- 在跨场景对象迁移任务上，与先前方法相比显著提高了视觉质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：问题具有实际应用价值（如VFX、室内设计），方法结合了扩散模型与3DGS后优化，思路清晰；但未提供定量实验细节或消融研究，需阅读全文评估方法的稳健性与局限性。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) is widely used to capture and render real scenes. Compositing objects from one capture into another has applications in many domains, such as VFX, architecture and interior design, or marketing. However, extracting an object from a source scene and naively pasting it into a target scene will fail to produce realistic results due to the different lighting conditions between the two scenes. To address this problem, we introduce a diffusion model that harmonizes naively composited images with inconsistent lighting. The model is trained with a heterogeneous dataset of image pairs (inconsistent composite input, consistent output), combining synthetic, generated, and real data. Our complete 3D solution allows a user to extract an object from the source scene and composite it into the target scene. From this, the (inconsistent) views of the target scene with the composite object are rendered. Our diffusion model harmonizes each one of these views, which are finally consolidated in a 3DGS representation with a post-optimization step. Our method provides visually compelling results, making object transfer between 3DGS easy to use and significantly improving quality compared to previous methods.

</details>

#### 2026-06-18 - VisDom: Sparse Novel View Synthesis with Visible Domain Constraint

**Authors:** Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers
**Links:** [abs](https://arxiv.org/abs/2606.20531) - [pdf](https://arxiv.org/pdf/2606.20531)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VisDom: Sparse Novel View Synthesis with Visible Domain Constraint
- 作者：Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers
- 出版日期：2026-06-18
- 分类：Neural Scene Representations & Rendering
- 链接：论文摘要 https://arxiv.org/abs/2606.20531 | PDF https://arxiv.org/pdf/2606.20531

### 一句话总结
VisDom 提出一种无需学习的几何约束（可见域约束），通过最小多视图可见性要求，从稀疏输入中改进新视角合成的几何一致性。

### 研究问题
稀疏新视角合成（NVS）中，从少量输入视图恢复3D几何存在模糊性，现有NeRF和Gaussian Splatting方法在稀疏设置下易过拟合，产生漂浮伪影和不一致几何；仅使用轮廓一致性作为正则化仍不足够，因为轮廓一致区域可能超出真实物体几何。

### 核心思路/方法
- 定义“可见域”为至少被K个视图观测到的3D子空间，并将其作为额外过滤标准，叠加在标准基于轮廓的重建之上，以提供更强的空间先验。
- 将VisDom集成到隐式（NeRF）和显式（GS）管线中，通过限制体素采样和指导高斯点优化时的放置。
- 该方法无需学习参数，仅需轮廓图，作为简单补充组件。

### 主要贡献
1. 提出一种无学习的几何约束（可见域），增强经典视觉外壳重建，有效缓解稀疏视图下的几何模糊。
2. 展示VisDom可无缝集成到NeRF和Gaussian Splatting两类管线中，提升稀疏NVS质量。
3. 在三个挑战性数据集上，从仅4张输入图像实现高质量物体中心重建，并能在GaussianObject之上以22倍更低训练成本达到或超越其性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法简洁（无学习参数、仅需轮廓图）且效果显著（在多个数据集和两种主流管线中稳定提升性能），对从事稀疏视图3D重建和新视角合成的研究者具有较高的实用参考价值。

</details>

<details>
<summary>Abstract</summary>

Sparse novel view synthesis (NVS) remains challenging due to the ambiguity of recovering 3D geometry from few input views. While NeRF- and Gaussian Splatting (GS)-based methods perform well with dense supervision, they often overfit in sparse settings, producing floating artifacts and inconsistent geometry. Silhouette consistency is commonly used as a regularizer, but it remains insufficient, as silhouette-consistent regions can extend beyond the true object geometry. We introduce VisDom, a learning-free geometric constraint that augments classical carving-based visual hull reconstruction by enforcing a minimum multi-view visibility requirement. Specifically, we define a visible domain as the subset of 3D space observed by at least $K$ views and use it as an additional filtering criterion on top of standard silhouette-based reconstruction. This provides a stronger spatial prior in sparse-view settings. We integrate VisDom into both implicit (NeRF) and explicit (GS) pipelines by restricting volumetric sampling and guiding Gaussian placement during optimization. Experiments on three challenging datasets show consistent improvements in sparse-view NVS, enabling high-quality object-centric reconstruction from as few as four input images. Our method is domain-agnostic, requires only silhouettes, and introduces no learned parameters, making it a simple complement to existing approaches. Applying VisDom on top of GaussianObject further improves performance on Omni3D and MipNeRF360, while matching or surpassing it at 22 $\times$ lower training cost.

</details>

#### 2026-06-18 - LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping

**Authors:** Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui
**Links:** [abs](https://arxiv.org/abs/2606.20424) - [pdf](https://arxiv.org/pdf/2606.20424)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** bundle adjustment, Gaussian Splatting, neural rendering, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping
- 作者：Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui
- 出版日期：2026-06-18
- 分类：Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2606.20424；PDF：https://arxiv.org/pdf/2606.20424

### 一句话总结
LIT-GS 提出一种融合 LiDAR、惯性和热成像数据的高斯泼溅建图框架，通过注入 LiDAR 平面几何约束来克服光照变化和低纹理场景下的结构漂移与渲染退化问题。

### 研究问题
现有的 LiDAR-惯性-视觉（LIV）高斯建图方法依赖 RGB 光度线索，在光照变化大或纹理缺乏的环境中脆弱易失效。本文旨在利用热成像通道替代视觉信息，解决弱光/无纹理条件下的几何精度和渲染质量下降问题。

### 核心思路/方法
1. **跨模态锚定**：将 LIV 视觉地图点作为置信度感知的跨模态锚点，建立可靠的热成像-LiDAR 关联。
2. **联合光束法平差**：在弱热监督下，将加权 LiDAR 点到平面残差加入光束法平差中，联合优化相机位姿和 3D 点。
3. **LiDAR 平面正则化渲染**：在优化后的结构基础上，引入 LiDAR 平面正则化的可微泼溅目标，约束渲染出的 3D 点与局部观测平面对齐，减少低对比度热成像中的表面增厚和结构漂移。

### 主要贡献
- 提出首个融合 LiDAR、惯性、热成像的高斯泼溅建图框架，增强对光照变化的鲁棒性。
- 设计置信度感知的跨模态热成像-LiDAR 关联机制及 LiDAR 平面正则化的可微约束。
- 在自有序列和公开数据集上，相比现有 LIV 高斯泼溅基线，在几何精度和渲染质量上取得一致提升，尤其在高挑战光照条件下表现突出。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对现有 LIV 高斯泼溅方法在弱光和低纹理场景下的关键瓶颈提出了创新性融合方案，实验证明了显著提升，对机器人、自动驾驶及 AR 领域的视觉建图与渲染具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has enabled real-time neural rendering, yet existing LiDAR-inertial-visual (LIV) Gaussian mapping pipelines remain fragile under illumination changes and texture-deficient scenes due to their reliance on RGB photometric cues. We present LIT-GS, a LiDAR-inertial-thermal Gaussian Splatting framework that injects LiDAR-derived plane geometry as an explicit constraint in both pose/structure refinement and Gaussian optimization. Specifically, we exploit LIV visual map points as confidence-aware cross-modal anchors to establish reliable thermal-LiDAR associations, and incorporate weighted LiDAR point-to-plane residuals into bundle adjustment to jointly refine camera poses and 3D points under weak thermal supervision. Building on the refined structure, we further introduce a LiDAR-plane-regularized differentiable splatting objective that constrains rendered 3D points to align with locally observed planes, mitigating surface thickening and structural drift in low-contrast thermal imagery. Experiments on proprietary sequences and public datasets demonstrate that LIT-GS consistently improves geometric accuracy and rendering quality over state-of-the-art LIV-based Gaussian Splatting baselines, particularly in challenging lighting conditions.

</details>

#### 2026-06-18 - Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration

**Authors:** Kyoleen Kwak, Daeho Kim, Jeong Woon Lee, Hyoseok Hwang
**Links:** [abs](https://arxiv.org/abs/2606.20103) - [pdf](https://arxiv.org/pdf/2606.20103)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** camera calibration, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration
- 作者：Kyoleen Kwak, Daeho Kim, Jeong Woon Lee, Hyoseok Hwang
- 出版日期：2026-06-18
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.20103

### 一句话总结
本文提出一种在3D高斯溅射框架中保留度量几何信息的方法，通过密集深度监督和阻止光度梯度更新高斯空间参数，提升了激光雷达与相机的外参标定精度。

### 研究问题
现有基于3D高斯溅射（3DGS）的激光雷达-相机无目标外参标定方法中，由于3DGS本身是为新视角合成设计的，代理几何结构容易偏离真实的激光雷达度量结构，导致标定精度受限。

### 核心思路/方法
1. 通过聚合多视角激光雷达观测数据，提供密集的深度监督，以保持高斯代理的度量几何一致性。
2. 阻断来自光度（图像）重建的梯度对高斯空间参数的更新，从而防止渲染质量优先导致的几何漂移。

### 主要贡献
- 提出一种几何保持框架，确保3D高斯代理的度量结构与真实激光雷达结构一致。
- 在公开驾驶数据集上，所提方法在标定精度上持续优于现有无目标标定方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦于自动驾驶中多模态传感器的标定问题，对从事激光雷达-相机融合感知的研究者具有直接参考价值；但需要读者对3D高斯溅射和标定框架有一定基础，非通用视觉论文。

</details>

<details>
<summary>Abstract</summary>

Accurate LiDAR-camera calibration is essential for robust multi-modal perception. Targetless approaches avoid manual setup but remain limited by the scarcity of discriminative cross-modal features. Recent methods address this by reconstructing the scene within a differentiable model, enabling extrinsic optimization through dense photometric supervision. Among these, 3D Gaussian Splatting (3DGS) has been widely adopted as a geometric proxy that bridges LiDAR and camera within a single differentiable framework. However, since 3DGS was originally designed for novel view synthesis, existing methods tend to prioritize rendering quality, causing the proxy geometry to drift from the true LiDAR structure. We propose a framework that preserves the metric geometry of the Gaussian proxy by aggregating multi-view LiDAR observations for dense depth supervision and blocking photometric gradients from updating the Gaussian spatial parameters. We validate our method on public driving datasets, where it consistently outperforms existing targetless methods in calibration accuracy.

</details>

#### 2026-06-17 - Building Drift: Documenting On-Site Construction Adaptations Across Material Lifecycles

**Authors:** Ritik Batra, Martin Tamke, Tom Svilans, Jan Hüls, Amritansh Kwatra, Steven J. Jackson, Thijs Roumen, Mette Ramsgaard Thomsen
**Links:** [abs](https://arxiv.org/abs/2606.19609) - [pdf](https://arxiv.org/pdf/2606.19609)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Building Drift: Documenting On-Site Construction Adaptations Across Material Lifecycles
- 作者：Ritik Batra, Martin Tamke, Tom Svilans, Jan Hüls, Amritansh Kwatra, Steven J. Jackson, Thijs Roumen, Mette Ramsgaard Thomsen
- 出版日期：2026-06-17
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：摘要: https://arxiv.org/abs/2606.19609 | PDF: https://arxiv.org/pdf/2606.19609

### 一句话总结
本文提出“建筑漂移”（building drift）概念，描述回收材料建筑在现场施工中物理状态与数字模型的偏差，并开发了基于视频和3D高斯泼溅的文档工具Pentimento，用于记录和呈现现场适应过程以支持材料循环利用。

### 研究问题
如何系统性地记录、表征和传递回收材料建筑在现场施工中因不可预测性产生的物理适配（即“建筑漂移”），从而为材料在多个生命周期中的评估、传承和再利用提供必要信息。

### 核心思路/方法
1. **案例研究**：通过回收木材展馆ReShelter的建造实践，归纳出现场适应的分类法（Tending the Site, Foraging for Fit, Interpreting the Material, Marking Measurements, Coordinating Across Communities）。
2. **工具开发**：提出名为Pentimento的文档工具，利用视频文档和3D高斯泼溅技术，在空间、时间和语义三个维度上，将现场适应与设计模型相关联，使各利益相关方能导航材料历史。

### 主要贡献
1. 提出“建筑漂移”概念，系统刻画回收材料建筑在生命周期中的物理状态与数字模型间的集体偏差。
2. 建立建筑漂移的分类法，涵盖现场适应、材料解读、社区协调等五个关键类别。
3. 开发Pentimento工具，将视频与3D高斯泼溅结合，实现现场适应的空间、时间与语义化记录，降低材料再利用障碍。

### 局限性
摘要未提及方法在规模扩展性、计算效率、不同材料类型或建筑场景下的适用性评估；也未说明工具对协作流程的量化影响或用户验证结果。

### 阅读优先级
**中**  
理由：该工作聚焦可持续建筑中的材料记录与数字孪生，核心创新在于将计算机视觉技术（3D高斯泼溅）应用于建筑现场适应的文档化。若对循环经济、建筑信息建模或现场施工协作感兴趣，该文具有启发价值；但若需具体技术实现细节或实验评估，摘要内容有限。

</details>

<details>
<summary>Abstract</summary>

In a circular economy for construction, reclaimed materials carry prior lives of use and go on to have post-lives in future buildings. Yet working with such materials introduces unpredictability that requires on-site improvisation, making their reuse challenging to document and scale across building lifetimes. Without documentation, the on-site adaptations that make construction with reclaimed materials possible leave collaborators, evaluators, and inheritors without the information they need to continue, assess, and reuse materials. We call the collective deviation of the physical state from the digital model through these adaptations "building drift." Through a case study, ReShelter, a reclaimed timber pavilion constructed in the forest, we develop a taxonomy for building drift that characterizes the collective deviation across building lifetimes: Tending the Site, Foraging for Fit, Interpreting the Material, Marking Measurements, and Coordinating Across Communities. To put our taxonomy for building drift into practice, we present Pentimento, a documentation tool that leverages video documentation and 3D Gaussian Splatting to spatially, temporally, and semantically represent on-site adaptations in relation to the designed model. Pentimento enables each stakeholder to navigate material histories in ways that reduce barriers to material reuse. Together, these contributions open pathways towards computational tools that support the on-site improvisation essential to construction with reclaimed materials, enabling more sustainable cycles of recovery, repair, and reuse.

</details>

#### 2026-06-17 - One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies

**Authors:** Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song
**Links:** [abs](https://arxiv.org/abs/2606.19586) - [pdf](https://arxiv.org/pdf/2606.19586)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies
- 作者：Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song
- 出版日期：2026-06-17T20:41:13Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.19586

### 一句话总结
本文提出一种数据增强框架，通过生成逼真的鱼眼图像序列和物理可行的动作轨迹，提升视觉运动策略在操作任务中的成功率和泛化能力。

### 研究问题
如何利用少量真实世界演示数据，生成增强的视觉和动作数据，以减轻视觉运动策略对初始配置和未见过障碍物的分布外失败问题。

### 核心思路/方法
1. 使用便携式平行夹爪和单个鱼眼相机捕获真实世界“眼在手”演示。
2. 引入适用于大视场鱼眼相机的新型高斯溅射公式，重建并编辑包含未见过物体的3D场景。
3. 通过轨迹优化生成平滑、无碰撞、利于视图渲染的动作轨迹，并从对应新视角渲染视觉观察。

### 主要贡献
提出一种有效的数据增强框架，无需大量数据收集，通过生成视觉真实的鱼眼图像序列和对应物理可行的动作轨迹，改善了同一场景和包含障碍物的增强场景下多种操作任务的成功率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该工作针对视觉运动策略的分布外泛化问题提出了一种数据增强方法，创新性较强，但摘要未详述实验设置、基线对比和优势量化，因此适合对数据增强或场景理解方向感兴趣的读者进一步参考，但优先级中等。

</details>

<details>
<summary>Abstract</summary>

Visuomotor policies for manipulation have demonstrated remarkable potential in modeling complex robotic behaviors, yet minor alterations in the robot's initial configuration and unseen obstacles easily lead to out-of-distribution observations. Without extensive data collection effort, these result in catastrophic execution failures. In this work, we introduce an effective data augmentation framework that generates visually realistic fisheye image sequences and corresponding physically feasible action trajectories from real-world eye-in-hand demonstrations, captured with a portable parallel gripper with a single fisheye camera. We introduce a novel Gaussian Splatting formulation, adapted to wide FoV fisheye cameras, to reconstruct and edit the 3D scene with unseen objects. We utilize trajectory optimization to generate smooth, collision-free, view-rendering-friendly action trajectories and render visual observations from corresponding novel views. Comprehensive experiments in simulation and the real world show that our augmentation framework improves the success rate for various manipulation tasks in both the same scene and the augmented scene with obstacles requiring collision avoidance.

</details>

#### 2026-06-17 - 3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning

**Authors:** Ellina Zhang, Madhaven Iyengar, Amir Zadeh, Chuan Li, Deepak Pathak, David Held, Tal Daniel
**Links:** [abs](https://arxiv.org/abs/2606.19451) - [pdf](https://arxiv.org/pdf/2606.19451)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning
- 作者：Ellina Zhang, Madhaven Iyengar, Amir Zadeh, Chuan Li, Deepak Pathak, David Held, Tal Daniel
- 出版日期：2026-06-17T18:00:08Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.19451

### 一句话总结
本文提出3D-DLP模型，是一种自监督的3D以物体为中心的场景表示学习方法，通过将RGB-D或体素观测分解为可解释的3D潜粒子，实现场景重构和下游操控任务性能提升。

### 研究问题
如何从3D场景观测（RGB-D或体素）中学习一种以物体为中心、可解释且可控的潜表示，同时避免对密集3D输入的高内存消耗，并提升下游机器人操控任务的表现。

### 核心思路/方法
基于Deep Latent Particles (DLP)框架扩展至3D，将场景级RGB-D或体素观测分解为一组3D潜粒子。每个粒子编码解耦的属性，包括3D关键点位置、包围框尺寸和外观特征，代表场景中的一个不同实体。模型通过端到端的自监督重构目标学习每个粒子的可解释分割图。

### 主要贡献
1. 提出3D-DLP，一种自监督的3D以物体为中心的场景表示学习模型，能够将场景解耦为一组3D潜粒子。
2. 每个潜粒子编码解耦的3D属性（位置、尺寸、外观），并学习可解释的逐粒子分割图。
3. 在模拟和真实数据集上证明，通过操纵粒子位置和重构可生成新场景配置。
4. 将紧凑的3D潜粒子用于下游机器人操控任务，性能优于缺乏明确3D信息或使用无物体结构密集3D输入的基线方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作结合了自监督学习、3D场景表示和机器人操控，但摘要中实验细节和量化结果（如具体性能提升幅度）未披露，仅通过定性描述展示优势。若读者对物体中心表示或自监督3D理解感兴趣，值得阅读；若需严格对比基线，需查阅全文。

</details>

<details>
<summary>Abstract</summary>

We introduce 3D-DLP, a self-supervised object-centric representation learning model that decomposes scene-level RGB-D or voxel observations into a set of 3D latent particles. Building on the Deep Latent Particles (DLP) framework, each particle encodes disentangled attributes, including 3D keypoint position, bounding box dimensions, and appearance features, and represents a distinct entity in the scene. The model learns interpretable per-particle segmentation maps through an end-to-end self-supervised reconstruction objective. We demonstrate on both simulated and real-world datasets that the learned latent space is interpretable and controllable: by manipulating particle positions and decoding, we can generate novel scene configurations. Furthermore, we show that leveraging these compact 3D latent particles for downstream robotic manipulation improves performance over baselines that either lack explicit 3D information or rely on memory-intensive dense 3D inputs without object-centric structure. Code and videos are available at https://eubooks3003.github.io/3d-dlp.

</details>

#### 2026-06-17 - NeuMesh++: Towards Versatile and Efficient Volumetric Editing with Disentangled Neural Mesh-based Implicit Field

**Authors:** Chong Bao, Yuan Li, Bangbang Yang, Yujun Shen, Hujun Bao, Zhaopeng Cui, Yinda Zhang, Guofeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.19316) - [pdf](https://arxiv.org/pdf/2606.19316)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, neural radiance field, radiance field, neural rendering, novel view synthesis, view synthesis, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NeuMesh++: Towards Versatile and Efficient Volumetric Editing with Disentangled Neural Mesh-based Implicit Field
- 作者：Chong Bao, Yuan Li, Bangbang Yang, Yujun Shen, Hujun Bao, Zhaopeng Cui, Yinda Zhang, Guofeng Zhang
- 出版日期：2026-06-17T17:39:21Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.19316

### 一句话总结
本文提出一种基于网格顶点的解耦神经隐式场表示（NeuMesh++），通过在网格顶点上编码几何、纹理和语义信息，实现多种高效的体积编辑功能。

### 研究问题
现有神经渲染方法在编辑方面功能有限（如仅支持刚性变换或类别特定编辑），缺乏支持几何、纹理语义等综合且高效编辑的统一表示。

### 核心思路/方法
1. **表示设计**：在网格顶点上解耦编码神经辐射场的几何、纹理和语义代码。
2. **关键技术**：
   - 局部空间参数化：提升渲染质量和训练稳定性。
   - 顶点可学习修改颜色：改善纹理编辑的真实感。
   - 空间感知优化策略：实现精确纹理编辑。
   - 语义辅助区域选择：简化隐式场编辑所需的人工标注。
3. **编辑功能**：支持网格引导的几何编辑、指定纹理编辑（纹理交换、填充和涂绘）以及语义引导的编辑。

### 主要贡献
1. 提出一种新的基于网格的表示，将几何、纹理和语义解耦编码在网格顶点上，支持多种编辑操作。
2. 开发了多种专用技术（局部空间参数化、可学习修改颜色、空间感知优化、语义辅助区域选择）以增强编辑效果与效率。
3. 在真实与合成数据集上展示了该方法在表示质量和编辑能力上的优越性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法面向神经隐式场编辑这一重要应用场景，提出了一种解耦表示并实现了多种高效编辑功能，且附带多技术改进。对于关注3D场景编辑、神经渲染应用的读者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recently neural implicit rendering techniques have evolved rapidly and demonstrated significant advantages in novel view synthesis and 3D scene reconstruction. However, existing neural rendering methods for editing purposes offer limited functionalities, e.g., rigid transformation and category-specific editing. In this paper, we present a novel mesh-based representation by encoding the neural radiance field with disentangled geometry, texture, and semantic codes on mesh vertices, which empowers a set of efficient and comprehensive editing functionalities, including mesh-guided geometry editing, designated texture editing with texture swapping, filling and painting operations, and semantic-guided editing. To this end, we develop several techniques including a novel local space parameterization to enhance rendering quality and training stability, a learnable modification color on vertex to improve the fidelity of texture editing, a spatial-aware optimization strategy to realize precise texture editing, and a semantic-aided region selection to ease the laborious annotation of implicit field editing. Extensive experiments and editing examples on both real and synthetic datasets demonstrate the superiority of our method on representation quality and editing ability. Project page: https://zju3dv.github.io/neumeshplusplus/

</details>

#### 2026-06-17 - FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity

**Authors:** Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer
**Links:** [abs](https://arxiv.org/abs/2606.19019) - [pdf](https://arxiv.org/pdf/2606.19019)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity
- 作者：Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer
- 出版日期：2026-06-17T12:42:09Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.19019

### 一句话总结
FlowObject提出了一种无训练引导框架，通过双空间引导策略和3D高斯泼溅（3DGS）优化，融合流匹配模型的生成先验与观测一致性，实现了从稀疏视角图像到完整3D对象的高质量重建。

### 研究问题
如何从少量随意拍摄的图像中恢复完整的3D物体表示，同时平衡生成先验（用于补全未见区域）与重建保真度（保持与真实观测一致）之间的矛盾。

### 核心思路/方法
1. 将稀疏视角3D重建重新定义为无训练的引导逆问题，通过双空间引导策略控制流匹配模型的常微分方程（ODE）轨迹。
2. 利用生成先验补全被遮挡或未观测的区域，同时强制输出与真实观测严格一致。
3. 引入3DGS精炼阶段，减少生成输出的“合成感”，弥合生成结果与逼真重建之间的差距。

### 主要贡献
- 提出首个将稀疏视角重建作为训练-free引导逆问题的框架，有效融合生成先验与观测一致性。
- 引入双空间引导策略，在几何完整性和外观保真度之间取得平衡。
- 在合成和真实数据集上，显著优于现有生成模型和优化方法，尤其在严重遮挡场景下表现更优。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：针对稀疏视角3D重建的核心难题（生成先验与观测一致性冲突）提出了新颖的引导框架，方法简洁且性能显著优于现有方法，对计算机视觉领域的3D表征与渲染方向具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering complete 3D representations of objects from few casual image captures remains a significant challenge. Recent 3D generative models, particularly those based on Flow-Matching (FM), can synthesize high-quality textured assets; however, they often suffer from ''synthetic bias'' where learned priors override observational evidence, alongside a lack of alignment with the observed instance. Conversely, optimization-based methods like 3D Gaussian Splatting (3DGS) provide high fidelity on visible surfaces but fail to reason about unobserved geometry. In this paper, we present FlowObject, a framework that reformulates sparse-view 3D reconstruction as a training-free, guided inverse problem. Our approach applies a dual-space guidance strategy to steer the Ordinary Differential Equation (ODE) trajectory of a flow-matching model, enabling the completion of unseen regions through learned generative priors while enforcing strict consistency with real-world observations. By integrating a 3DGS refinement stage, FlowObject further bridges the gap between ''synthetic-looking'' generative outputs and photorealistic reconstructions. Comprehensive benchmarks on synthetic and real-world datasets demonstrate that current state-of-the-art methods often struggle to achieve geometric completeness and observational consistency simultaneously, especially under severe occlusions. In contrast, our method significantly outperforms state-of-the-art generative models and optimization-based frameworks in both geometric completeness and view-dependent appearance fidelity.

</details>

#### 2026-06-17 - EDoF-NeRF: extended depth-of-field neural radiance fields using a coded aperture camera

**Authors:** Yoshiyuki Shirasaki, Ryoichi Horisaki
**Links:** [abs](https://arxiv.org/abs/2606.18826) - [pdf](https://arxiv.org/pdf/2606.18826)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EDoF-NeRF: extended depth-of-field neural radiance fields using a coded aperture camera
- 作者：Yoshiyuki Shirasaki, Ryoichi Horisaki
- 出版日期：2026-06-17
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.18826

### 一句话总结
本文提出EDoF-NeRF方法，通过在相机瞳孔处放置编码光圈来扩展景深，从而构建高保真的神经辐射场。

### 研究问题
传统相机在采集NeRF所需的多视角图像时，存在景深与光通量之间的固有矛盾，导致NeRF渲染的视图在景深外区域保真度下降。

### 核心思路/方法
1. 在相机瞳孔处引入编码光圈，以在散焦条件下保留空间频率成分。
2. 设计一种将编码光圈纳入NeRF的相机模型，使编码图像可直接输入网络。
3. 通过该模型，网络能够从编码图像中学习并生成具有扩展景深的新视图。

### 主要贡献
1. 提出EDoF-NeRF，首次将编码光圈与NeRF结合以扩展景深。
2. 开发了兼容编码图像的相机模型，直接处理编码图像输入。
3. 通过仿真和实验验证，EDoF-NeRF在扩展景深的新视图渲染上优于传统光圈相机。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。
理由：该方法从硬件（编码光圈）和模型（相机模型）两方面优化NeRF的景深问题，具有一定新颖性；但摘要未提供具体性能指标或典型场景对比，需要查看全文评估实际效果与复杂度。

</details>

<details>
<summary>Abstract</summary>

We propose a method for extending the depth-of-field (DoF) to construct high-fidelity neural radiance fields (NeRF) -- an emerging technique for rendering photorealistic novel views from a dataset of images captured at different viewpoints, based on implicit neural representations. The trade-off between DoF and light quantity is inherent not only in conventional cameras but also in NeRF, since the datasets used by NeRF are captured by these cameras. To address this issue, we introduce a coded aperture placed at the camera pupil, preserving spatial frequency components under defocused conditions. We develop a camera model incorporating coded apertures into NeRF, allowing direct input of coded images and enabling the generation of novel views with an extended DoF. We validate the proposed method, termed extended DoF-NeRF (EDoF-NeRF), through simulations and experiments, demonstrating its superior performance compared to conventional aperture cameras.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-22 - LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation

**Authors:** Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, Jiawei Chen, Qingpo Wuwu, Xiaoqi Li, Nuowei Han, Yiming Zhang, Xuheng Zhang, Yang Yue, Yeqing Yang, Lei Wang, Peng Jia, Hao Tang, Shanghang Zhang
**Links:** [abs](https://arxiv.org/abs/2606.23685) - [pdf](https://arxiv.org/pdf/2606.23685)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation
- 作者：Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, Jiawei Chen, Qingpo Wuwu, Xiaoqi Li, Nuowei Han, Yiming Zhang, Xuheng Zhang, Yang Yue, Yeqing Yang, Lei Wang, Peng Jia, Hao Tang, Shanghang Zhang
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.23685

### 一句话总结
LaST-HD提出一种新的机器人学习范式，通过对齐人体手部与机器人演示在共享潜在推理空间中的物理动力学，使机器人能从可扩展的人类手部数据中学习高效的物理操作行为。

### 研究问题
如何使机器人从大规模、低成本采集的人类手部演示数据中，有效学习适用于不同机械结构的物理操作技能，并提升对新颖物体、场景和位置的泛化能力。

### 核心思路/方法
1. **对齐潜在推理空间**：在“先推理后动作”的VLA框架下，利用未配对的人手与机器人轨迹训练一个辅助的动作条件世界模型，生成统一的潜在目标，对齐不同形态的表示。
2. **低成本数据采集**：开发Out-of-Lab (OOL) Glove，一种专用于人手数据采集的低成本动作捕捉手套，提供精确关键点并可作为通用动作监督信号。
3. **渐进式混合训练**：采用混合人-机器人协同训练和人手在线矫正后训练两步法，先通过混合共训练提升泛化性，再利用在线矫正适应新环境。

### 主要贡献
1. 提出LaST-HD，一种通过对齐跨形态潜在动力学实现人类到机器人动作学习的新范式。
2. 开发OOL Glove低成本数据采集设备，并展示其采集的人手数据可作为不同机械手（夹爪、灵巧手）的通用监督。
3. 验证渐进式混合训练方法，仅用20分钟OOL手套数据即可在新环境中达到90%以上的准确率，并显著提升对新型物体、场景和位置的泛化能力。

### 局限性
摘要未提供足够信息。摘要未提及具体实验失败案例、对特殊工况（如极端光照、物体变形）的鲁棒性、或该方法在更复杂操作任务（如精密装配）上的表现。

### 阅读优先级
**高**  
理由：该工作提出了一种新颖的、基于潜在空间对齐的人-机器人动作学习范式，结合低成本数据采集设备，在仅需少量数据的情况下获得了高准确率和强泛化性。对于关注机器人模仿学习、人机交互、低成本数据采集和技能迁移的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Human-hand demonstrations provide a direct and scalable source of physical interaction data for robot learning. While manual retargeting is indispensable for establishing kinematic action correspondence across different morphologies, robust transfer requires going beyond geometry to address the underlying alignment of physical dynamics between human and robot manipulation. To address this, we introduce LaST-HD, a novel human-to-robot action learning paradigm that extends reasoning-before-acting VLA by aligning human-hand and robot demonstrations in a shared latent reasoning space. Rather than mimicking human kinematics, LaST-HD trains an auxiliary action-conditioned world model on unpaired human-hand and robot trajectories to synthesize unified latent targets. After aligning cross-embodiment representations in this shared forward-dynamics space, these targets supervise LaST-HD's latent reasoning process, enabling it to internalize shared physical dynamics and drive efficient human-hand action learning. Moreover, we develop Out-of-Lab (OOL) Glove, a low-cost motion-capture glove tailored to LaST-HD for human-hand data collection. The captured human data provide precise keypoints and serve as universal action supervision across grippers and dexterous hands. Armed with the aligned latent space and high-fidelity human-hand data, we develop a progressive mixed-to-human training recipe comprising mixed human-robot co-training and human-hand online correction post-training. Through mixed co-training, LaST-HD improves generalization to novel objects, scenes, and positions using only human-hand demonstrations. With online correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy using only 20 minutes of OOL glove data.

</details>

#### 2026-06-22 - IMAGIN-4D: Image-Guided Controllable Interaction Generation

**Authors:** Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch, Tomas Hodan, Michael J. Black, Dimitrios Tzionas, Shreyas Hampali
**Links:** [abs](https://arxiv.org/abs/2606.23675) - [pdf](https://arxiv.org/pdf/2606.23675)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, embodied AI, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IMAGIN-4D: Image-Guided Controllable Interaction Generation
- 作者：Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch, Tomas Hodan, Michael J. Black, Dimitrios Tzionas, Shreyas Hampali
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2606.23675；PDF：https://arxiv.org/pdf/2606.23675

### 一句话总结
提出一种基于扩散模型的人-物交互生成方法IMAGIN-4D，利用参考图像作为空间和时间条件，通过分解图像特征实现对交互姿态、轨迹和接触的精细控制。

### 研究问题
现有的人-物交互生成方法依赖文本、物体几何和稀疏路径点，但这些信号无法唯一指定交互细节（如抓取方式、接近方向、身体姿势等），导致生成结果存在歧义。本研究旨在利用参考图像提供更明确的交互视觉规范，并解决单一图像特征混淆不同时空条件的问题。

### 核心思路/方法
1. **空间解耦条件**：从参考图像中提取“交互状态令牌”（interaction-state tokens），分别编码身体姿态、物体姿态、身体-物体接触及空间关系。
2. **时间解耦条件**：对每个生成帧，从图像中查询与帧相关的“帧感知令牌”（frame-aware tokens），使不同帧段能关注同一图像中不同的视觉线索。
3. **角色感知条件融合**：文本、路径点和交互状态令牌使用独立的AdaLN（自适应层归一化）流，帧感知令牌则通过交叉注意力与运动令牌交互，以平衡图像、文本和路径点条件。
4. **数据与评估**：由于缺乏配对图像，构建了从运动到图像的合成渲染流程（基于FullBodyManipulation数据集），并引入图像-运动对齐度量，用于评估生成运动与参考快照是否匹配。

### 主要贡献
1. 提出IMAGIN-4D，首个通过参考图像实现精细交互控制的扩散模型。
2. 设计了时空解耦的图像条件方法，避免单一图像特征对交互细节的混淆。
3. 构建了合成运动到图像的渲染流程及图像-运动对齐度量，填补了缺少配对图像数据的空白。
4. 在FBM和BEHAVE数据集上，相比单令牌或均匀图像条件的基线方法，IMAGIN-4D在保持路径点跟踪和运动质量的同时，显著提升了交互控制的细粒度。

### 局限性
摘要未提供足够信息，例如模型对复杂遮挡、未见物体类型或长序列生成的鲁棒性未提及。

### 阅读优先级
**高**  
理由：该工作解决了人-物交互生成中歧义性的关键问题，提出了创新的时空解耦图像条件机制，且实验在多个数据集上验证了有效性。对从事角色动画、机器人交互、AR/VR及具身AI的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Generating human-object interactions (HOI) is central to character animation, robotics, AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text, object geometry, and sparse waypoints, controlling action semantics and object trajectories. However, these signals underspecify interaction: the same prompt and trajectory can produce different grasps, approach directions, body poses, object poses, contacts, and body-object layouts. We address this ambiguity with a reference image as a visual specification of the desired interaction snapshot. However, a single global image representation conflates distinct cues and conditions all frames on identical visual evidence. We therefore introduce IMAGIN-4D, a diffusion-based HOI generator that decomposes image conditioning spatio-temporally. For spatial conditioning, IMAGIN-4D extracts supervised interaction-state tokens for body pose, object pose, body-object contact, and spatial relationships at the depicted frame. For temporal conditioning, it computes frame-aware tokens by querying image patches per generated frame, allowing sequence segments to attend to different visual cues from the same image. To balance image, text, and waypoint cues, IMAGIN-4D uses role-aware conditioning: text, waypoints, and interaction-state tokens use separate AdaLN streams, while frame-aware visual tokens cross-attend with motion tokens. Since HOI motion datasets lack paired images, we build a synthetic motion-to-image rendering pipeline from FullBodyManipulation (FBM) and introduce an image-adherence metric to evaluate whether generated motions match the reference snapshot. Experiments on FBM and BEHAVE show that IMAGIN-4D improves fine-grained interaction control over single-token and uniformly image-conditioned baselines while preserving waypoint-following and motion quality. Code and models will be released at https://imagin4d.github.io.

</details>

#### 2026-06-22 - From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models

**Authors:** David Oberacker, Meike Deitersen, Niklas Spielbauer, Tristan Schnell, Georg Heppner, Arne Roennau
**Links:** [abs](https://arxiv.org/abs/2606.23312) - [pdf](https://arxiv.org/pdf/2606.23312)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, scene understanding, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models
- 作者：David Oberacker, Meike Deitersen, Niklas Spielbauer, Tristan Schnell, Georg Heppner, Arne Roennau
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.23312

### 一句话总结
本文提出一种利用视觉语言模型（VLM）和大语言模型（LLM）构建包含开放语义关系的3D场景图森林的方法，以提升机器人的场景理解与任务执行能力。

### 研究问题
现有3D场景图方法通常局限于预定义的刚性关系类别，忽略了语义连接（如因果联系或环境上下文），导致无法支持复杂的真实世界环境理解需求。本文研究如何利用基础模型构建具有开放语义关系的3D场景图森林，以改善场景理解和机器人任务执行。

### 核心思路/方法
1. **节点与关系提取**：先用VLM识别实例特定的概念节点和关系，再用LLM通过推理扩展出更广泛、更抽象的概念节点和关系。
2. **图森林构建**：将物体节点、概念节点及关系组装成层次化的3D场景图森林，并引入概念节点表示抽象概念。
3. **评估**：在uHumans2和ScanNet室内数据集上验证生成关系的准确性和相关性；通过开放词汇物体检索任务（基于ScanNet数据及Boston Dynamics Spot实际室内部署）展示在机器人应用中的下游适用性。

### 主要贡献
- 利用基础模型构建更富表达力、语义更深的3D层次化场景图。
- 提出开放语义关系的场景图森林，突破预定义关系类别的限制。
- 在真实室内环境和公开数据集上验证了方法在机器人语义理解与环境感知中的潜力。

### 局限性
摘要未提供足够信息，无法推断具体的局限性（如计算开销、泛化能力边界等）。

### 阅读优先级
**高**  
理由：研究面向机器人场景理解核心难点，结合VLM和LLM构建层次化场景图的方法具有创新性，且在真实机器人平台（Boston Dynamics Spot）上进行了验证，对从事具身智能、3D感知及机器人操作的研究者具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Operating in complex real-world environments requires robots to understand their surroundings on a functional semantic level. This demands a detailed multi-layer world model capturing the complex relations of its surroundings. Hierarchical 3D scene graphs address this challenge by integrating geometric, semantic, and relational data within a unified spatial framework. However, current 3D scene graph approaches often restrict themselves to rigid structures of pre-determined relationship classes, mostly neglecting important semantic connections, like causal connections or environmental contexts. This paper explores the potential of foundation models to build forests of 3D scene graphs with open semantic relationships to improve scene understanding and robotic task execution. We propose a method where instance-specific concept-nodes and relationships are first identified by a VLM and extended upon by a LLM, inferring broader, more abstract concept-nodes and relationships through reasoning. These object-nodes, concept-nodes, and relationships are then assembled into a forest of hierarchical 3D scene graphs, enhanced with concept-nodes to represent abstract concepts. Evaluations were conducted on the uHumans2 and ScanNet indoor dataset, validating the accuracy and relevance of the generated relationships. Downstream suitability of scene-graph forests for robotics applications is demonstrated in an open-vocabulary object-retrieval task utilizing both ScanNet data and a real-world indoor deployment using a Boston Dynamics Spot. This paper leverages foundation models to create more expressive, semantically deep 3D hierarchical scene graphs and demonstrates their potential to advance semantic and environmental understanding in robotics.

</details>

#### 2026-06-22 - Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI

**Authors:** Xianda Guo, Bohao Zhang, Chenwei Huang, Shiyuan Chen, Ruilin Wang, Yiqun Duan, Cong Yang, Qin Zou, Wei Sui
**Links:** [abs](https://arxiv.org/abs/2606.22971) - [pdf](https://arxiv.org/pdf/2606.22971)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI
- 作者：Xianda Guo, Bohao Zhang, Chenwei Huang, Shiyuan Chen, Ruilin Wang, Yiqun Duan, Cong Yang, Qin Zou, Wei Sui
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22971

### 一句话总结
本文提出了一个面向人形机器人的全景立体占据数据集Humanoid-OmniOcc，并基于Real2Sim2Real闭环范式设计了相应的占据预测模型。

### 研究问题
现有占据预测数据集主要面向自动驾驶场景（前向相机、远场几何、静态道路先验），不适用于人形机器人在复杂室内环境中的全身感知。

### 核心思路/方法
1. **数据集构建**：包含15个模拟室内场景和5个真实环境，采集超过155K样本，采用全景立体（panoramic stereo）相机配置。
2. **Real2Sim2Real闭环**：真实传感器参数驱动物理准确仿真，仿真生成大规模带标注训练数据，模型在仿真训练后直接在真实数据上评测，实现迭代优化。
3. **模型设计**：提出Humanoid-OmniOcc模型，利用鲁棒的深度先验进行精确的2D到3D提升（lifting）。

### 主要贡献
1. 发布了首个面向人形机器人的大规模全景立体占据数据集，覆盖多样场景和风格。
2. 提出了Real2Sim2Real闭环框架，弥合仿真到真实的鸿沟。
3. 设计了基于立体深度先验的占据预测模型，在仿真和真实场景中均优于单目基线方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对人形机器人感知这一前沿方向，提出了新颖的全景立体数据集和Real2Sim2Real闭环框架，实验验证了跨场景泛化能力，对具身AI和机器人研究具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Occupancy prediction at voxel-level granularity is essential for safe robotic navigation and interaction in complex environments. Existing occupancy datasets, however, are predominantly designed for autonomous driving with vehicle-centric biases -- forward-facing cameras, far-field geometry, and static road priors -- limiting their applicability to embodied humanoid perception. We present Humanoid-OmniOcc, a large-scale panoramic stereo-based occupancy dataset tailored for humanoid robots. The dataset encompasses 15 diverse simulated indoor scenes and 5 real-world environments, yielding over 155K samples with broad scene and style diversity. Importantly, the dataset is designed around a Real2Sim2Real closed-loop paradigm: real sensor specifications drive physically accurate simulation, simulation produces large-scale annotated training data, and models trained in simulation are directly evaluated on real-world captures -- enabling iterative refinement of the sim-to-real pipeline. We further propose \textbf{H}umanoid \textbf{S}urround \textbf{S}tereo-guided \textbf{Occ}upancy model (Humanoid-OmniOcc) that exploits robust depth priors for accurate 2D-to-3D lifting. Extensive experiments show that Humanoid-OmniOcc consistently outperforms monocular baselines and generalizes well to both unseen simulated test scenes and real-world environments, validating the effectiveness of the Real2Sim2Real design. Code and data will be available upon acceptance at https://d-robotics-ai-lab.github.io/humanoid-omniocc.

</details>

#### 2026-06-22 - HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration

**Authors:** Sandilya Sai Garimella, Daniel Chase Butterfield, Sean Wilson, Lu Gan
**Links:** [abs](https://arxiv.org/abs/2606.22756) - [pdf](https://arxiv.org/pdf/2606.22756)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, robotics, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration
- 作者：Sandilya Sai Garimella, Daniel Chase Butterfield, Sean Wilson, Lu Gan
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications；3D Reconstruction & Multi-view Geometry
- 链接：[abstract](https://arxiv.org/abs/2606.22756) | [pdf](https://arxiv.org/pdf/2606.22756)

### 一句话总结
HERCULES是一个基于Unreal Engine 5的开源仿真框架，专为异构多机器人（UAV-UGV）SLAM、协同感知与探索设计，支持大规模动态环境下的被动数据采集与主动闭环规划。

### 研究问题
如何解决现有仿真工具在异构多机器人（UAV-UGV）协同操作中的架构限制，实现大规模、高保真、动态环境下的SLAM、协同感知与探索任务开发与评估。

### 核心思路/方法
1. 基于Unreal Engine 5的AirSim和Cosys-AirSim构建，修复了先前框架的架构缺陷。
2. 新增UGV控制器以匹配UAV控制接口，提供共享导航栈（地图、可通行性分析、规划、控制）。
3. 扩展传感器套件：物理长波红外相机、可配置夜视模式。
4. 集成智能体（行人、交通、野生动物）与高保真动态现象（火灾、洪水、作物病害传播）。
5. 提供轻量级API、ROS 2封装、硬件级时间同步。
6. 支持两种运行模式：离线被动回放轨迹生成多模态数据集，以及在线主动闭环规划。

### 主要贡献
- 开源了首个面向异构多机器人（UAV-UGV）的高保真仿真与数据采集框架。
- 解决了现有框架在并发操作、传感器同步和大规模动态环境中的架构限制。
- 提供了异构多机器人SLAM基准数据集（双UAV+双UGV，覆盖沙漠、森林、城市千米级场景），并公开源码、文档与实验代码。

### 局限性
摘要未提供局限性信息。

### 阅读优先级
中。理由：框架工具性较强，直接贡献在于开源仿真基准和数据集，但摘要未给出与传统方法的定量对比或性能突破，对关注异构多机器人SLAM与协同感知的读者有参考价值，但对追求方法论创新的读者帮助有限。

</details>

<details>
<summary>Abstract</summary>

We present HERCULES, an open-source simulator and data-collection pipeline for heterogeneous multi-robot autonomy. Built upon the Unreal Engine 5 (UE5)-based simulators AirSim and Cosys-AirSim, HERCULES resolves key architectural limitations of prior frameworks to enable concurrent unmanned aerial and ground vehicle (UAV-UGV) operation in large-scale, photorealistic, dynamic environments. It introduces a new waypoint-tracking UGV controller that mirrors existing UAV control interfaces, and provides a shared navigation stack for mapping, traversability analysis, planning, and control across heterogeneous platforms. Expanding inherited sensor suites, it adds physics-based long-wave infrared (LWIR) cameras and configurable night-vision modes for degraded visual environments. HERCULES provides lightweight APIs, ROS 2 wrappers, and rigorous time synchronization across sensors and platforms, and brings state-of-the-art game-engine capabilities into robotics simulation, integrating intelligent agents such as pedestrians, traffic, and wildlife with high-fidelity dynamic phenomena, including fire, flooding, and crop disease spread. HERCULES runs in two modes: passively, replaying offline-designed trajectories to generate reproducible multi-modal datasets, and actively, running an online planner in closed loop from live observations. Our experiments in heterogeneous multi-robot SLAM, collaborative perception, and exploration, using both HERCULES-generated data and active closed-loop execution, demonstrate its utility for advancing heterogeneous multi-robot autonomy. We publicly release our source code, experiment code, documentation, and datasets, including a heterogeneous multi-robot SLAM benchmark collected with two UAVs and two UGVs across kilometer-scale desert, forest, and city environments, at https://lunarlab-gatech.github.io/HERCULES-website.

</details>

#### 2026-06-21 - MAPS: Multi-Anchor Projection Similarity for Joint Vision-Language Geo-Localization

**Authors:** Yutong Hu, Siyuan Tan, Shaocheng Yan, Pengcheng Shi, Qingwu Hu, Jiayuan Li
**Links:** [abs](https://arxiv.org/abs/2606.22543) - [pdf](https://arxiv.org/pdf/2606.22543)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MAPS: Multi-Anchor Projection Similarity for Joint Vision-Language Geo-Localization
- 作者：Yutong Hu, Siyuan Tan, Shaocheng Yan, Pengcheng Shi, Qingwu Hu, Jiayuan Li
- 出版日期：2026-06-21
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22543

### 一句话总结
本文提出一种名为 MAPS 的多锚点投影相似度方法，通过将视觉-语言联合地理定位问题建模为多锚点几何对齐，利用锚点平面上的投影长度作为新的相似度度量，实现了该任务上的领先性能。

### 研究问题
当前跨视图、跨模态地理定位模型主要基于点对点对齐，无法有效处理视觉与文本线索联合定义语义子空间的查询场景。因此，研究如何针对联合图像-文本查询（Vision-Language Geo-Localization, VLGL）设计更有效的对齐与相似度度量方法。

### 核心思路/方法
- 将 VLGL 视为多锚点几何对齐问题：利用视觉和文本查询特征在高维空间构建一个锚点平面（anchor plane）。
- 提出 MAPS 距离度量：通过目标特征在该锚点平面上的投影长度来衡量相似度，替代传统余弦相似度。
- 设计基于 MAPS 的对比损失：训练时驱使目标特征朝向对应的锚点平面，使学习到的表示与几何对齐一致。

### 主要贡献
- 首次将联合图像-文本查询的地理定位形式化为多锚点几何对齐问题。
- 提出 MAPS 相似度度量，能够捕获目标特征与联合查询子空间之间的几何一致性，比点对点余弦相似度更具判别力。
- 提出 MAPS 对比损失，使表示学习与检索几何对齐协同优化。
- 在 VLGL 任务上取得当时最优性能（状态达到最新技术水平）。

### 局限性
摘要未提供足够信息（例如实验设定、数据集、失败案例、计算开销、模型鲁棒性等）。

### 阅读优先级
中  
理由：该工作针对视觉-语言联合查询这一特定地理定位问题，提出了几何视角下的新度量与训练目标，方法创新性较强。但摘要未提供具体实验细节和结果数值，无法全面评估其实用性和复现难度，适合对该子方向感兴趣的读者关注。

</details>

<details>
<summary>Abstract</summary>

Humans localize places by integrating perceptual cues from vision with semantic reasoning from language, forming a scene understanding that is both intuitive and structured. Although existing geo-localization models have made substantial progress in cross-view and cross-modal settings, they are largely built upon point-to-point alignment, which is insufficient for joint vision-language queries. In such queries, visual and textual cues do not simply act as independent references, but jointly define a semantic subspace for locating the target. In this paper, we formulate vision-language geo-localization (VLGL) with joint image-text queries as a multi-anchor geometric alignment problem and propose a unified framework for this setting. To realize this formulation, we propose Multi-Anchor Projection Similarity (MAPS), a new metric which constructs an anchor plane from visual and textual query features in a high-dimensional space and measures similarity by the projection length of the target feature onto this plane. Unlike cosine similarity which evaluates isolated pairwise relations, MAPS captures the geometric consistency between the target feature and the joint query subspace, providing a more discriminative ranking criterion during retrieval. To make the learned representation consistent with this geometry, we further introduce a MAPS-based contrastive loss that drives target features toward the corresponding anchor plane. The proposed framework, similarity metric, and training objective jointly yield state-of-the-art performance in VLGL.

</details>

#### 2026-06-21 - Reference-Free Assessment of Physical Consistency in World Model-based Video Generation

**Authors:** Yun Oh, Sukmin Yun
**Links:** [abs](https://arxiv.org/abs/2606.22363) - [pdf](https://arxiv.org/pdf/2606.22363)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, localization, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reference-Free Assessment of Physical Consistency in World Model-based Video Generation
- 作者：Yun Oh, Sukmin Yun
- 出版日期：2026-06-21T07:17:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22363

### 一句话总结
提出一种无需参考视频的物理一致性评估方法，通过结合相对与绝对评估指标，改善视频生成中的物理保真度，并缩小仿真与真实环境的差距。

### 研究问题
如何在不依赖人工投票或地面真值参考的情况下，自动评估基于世界模型生成的视频的物理一致性，并提升其在实际物理任务中的表现。

### 核心思路/方法
结合两种无需参考的度量方式：
- **相对一致性评估**：利用DROID-SLAM和SEA-RAFT量化物理不一致性，从而筛选出更一致的视频，使任务成功率提升超过8%。
- **绝对评估**：通过时空定位，可视化生成视频中物理瑕疵发生的时间和位置。

### 主要贡献
1. 提出参考免费的物理一致性评估框架（相对与绝对相结合），减少对昂贵人工评估（如Elo评分）或不可得参考（如FVD所需）的依赖。
2. 证明通过相对一致性筛选可有效提升VLA模型在生成视频环境中的任务成功率，缩小仿真到现实的差距。
3. 绝对评估支持时空定位，帮助识别具体物理不一致的时空位置。

### 局限性
摘要未提供足够信息。未论述该方法在不同视频生成模型或更复杂物理场景下的泛化能力，也未提及计算开销或对SLAM/RAFT误差的鲁棒性。

### 阅读优先级
**高**  
理由：该工作针对视频生成中物理一致性的自动评估这一关键难点，提出了无需参考的实用方案，尤其在机器人仿真领域具有直接应用价值，对降低评估成本、提升模型实用性有重要启发。

</details>

<details>
<summary>Abstract</summary>

We introduce reference-free measures for evaluating the physical consistency of generated videos, combining relative and absolute approaches to assess fidelity. Although tools like WorldGym or WorldEval enable robotic simulation via video generation, physical fidelity gaps often prevent these environments from accurately reproducing real-world task success rates of VLA models. Unlike existing evaluation methods, which require costly human voting (Elo) or unavailable ground-truth references (FVD), our approach utilizes DROID-SLAM and SEA-RAFT to quantify physical inconsistencies, motivated by WorldScore. Videos filtered using our relative consistency assessment show an improvement in task success rates of over 8%, effectively narrowing the simulation-to-reality gap. Furthermore, our absolute assessment enables spatio-temporal localization, providing visualization of when and where physical artifacts occur.

</details>

#### 2026-06-21 - Any-Body Guard: Universal Safeguarding for Manipulation Policies via Action Masking

**Authors:** Alex Beaudin, Hanna Krasowski, Kartik Nagpal, Sanjit A. Seshia, Murat Arcak, Negar Mehr
**Links:** [abs](https://arxiv.org/abs/2606.22278) - [pdf](https://arxiv.org/pdf/2606.22278)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Any-Body Guard: Universal Safeguarding for Manipulation Policies via Action Masking
- 作者：Alex Beaudin, Hanna Krasowski, Kartik Nagpal, Sanjit A. Seshia, Murat Arcak, Negar Mehr
- 出版日期：2026-06-21
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22278

### 一句话总结
本文提出一种基于配置空间推理的通用安全防护方法 X-Safe，通过动作遮蔽为不同形态的机器人操作策略提供形式化概率碰撞避免保证，无需额外数据或工程适配。

### 研究问题
如何设计一种无需大量手动工程、可跨机器人和场景迁移的通用安全防护方法，为学习型操作策略提供形式化的碰撞避免保证。

### 核心思路/方法
- 直接在机器人配置空间中推理，利用基于物体的准静态场景表示和前向运动学模型。
- 通过动作遮蔽（action masking）机制实现安全性，提供形式化的概率碰撞避免保证。
- 方法不依赖额外数据或针对不同形态或场景的工程调整，实现跨实体迁移。

### 主要贡献
- 提出了通用的安全防护方法 X-Safe，可迁移至不同机器人形态和操作策略。
- 提供了形式化的概率碰撞避免保证，不依赖启发式或复杂前置评估。
- 在仿真和硬件实验中，任务性能退化小于现有最优防护方法，硬件实验零碰撞，且经验验证了形式化保证。

### 局限性
摘要未提供足够信息：未讨论方法在动态场景、非准静态假设下的表现，也未提及计算开销的具体数值或失败案例。

### 阅读优先级
**中**
理由：该方法为机器人操作安全防护提供了形式化保证和跨实体迁移能力，具有理论和实践价值；但未涉及动态环境细节，且截至2026年的预印本尚需验证实际部署可行性。

</details>

<details>
<summary>Abstract</summary>

Ensuring safety of learning-enabled robotic manipulation across diverse embodiments and tasks still requires significant manual engineering. Existing approaches typically rely on heuristically designed fallback controllers or complex forward invariance assessments. These methods are often too conservative for task success, too computationally expensive for real-time execution, too heuristic to provide useful safety guarantees, or too engineering-heavy to transfer between setups. In this paper, we propose a universal safeguarding approach, X-Safe, which reasons directly in the robot's configuration space to provide formal probabilistic guarantees for collision avoidance. By operating in the configuration space, our method transfers across embodiments while relying solely on an object-based, quasi-static scene representation and a forward kinematics model of the robotic manipulator. Thus, X-Safe provides useful formal safety guarantees without requiring additional data, or engineering effort for different embodiments or scenes. We demonstrate X-Safe for diverse embodiments and policies, both in simulation and on hardware. We observe less degradation in task performance compared to state-of-the-art safeguarding, no collisions on hardware experiments, and empirically corroborate our formal guarantees.

</details>

#### 2026-06-20 - Physics-Informed Eikonal Caging for Whole-Arm Manipulation Planning

**Authors:** Yan Zhang, Yiming Li, Yifei Dong, Florian T. Pokorny, Sylvain Calinon
**Links:** [abs](https://arxiv.org/abs/2606.22143) - [pdf](https://arxiv.org/pdf/2606.22143)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Physics-Informed Eikonal Caging for Whole-Arm Manipulation Planning
- 作者：Yan Zhang, Yiming Li, Yifei Dong, Florian T. Pokorny, Sylvain Calinon
- 出版日期：2026-06-20T16:49:17Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22143

### 一句话总结
本文提出一种基于物理信息Eikonal方程的“笼形”（caging）方法，将机器人对物体的几何包围质量转化为连续可微的逃逸时间场，并用于全臂操作规划，以提升对接触模型误差的鲁棒性。

### 研究问题
如何利用几何围笼概念，在全臂操作规划中实现鲁棒性，避免因复杂接触动力学建模不准确导致的规划失败。

### 核心思路/方法
1. 将传统“笼形”约束重新定义为最小时间逃逸问题：物体从机器人几何包围中逃脱所需的最短时间。
2. 证明该逃逸时间场满足Eikonal方程，因此可通过物理信息神经网络（PINN）近似求解，得到平滑可微的表示。
3. 将该可微表示直接嵌入操作规划的目标函数中，使得规划器倾向于选择能阻止物体逃逸的机器人构型，从而容忍简化的接触模型（如准动态近似和简化物体几何）。

### 主要贡献
- 提出一种全新的连续化笼形定义（逃逸时间场），并证明其满足Eikonal方程。
- 利用物理信息神经网络实现该场的可微近似，使其可直接嵌入基于优化的操作规划。
- 通过仿真和真实实验证明，该方法在面对干扰和接触模型失配时优于基线方法，表明几何围笼可作为全臂操作的实用鲁棒性基元。

### 局限性
摘要未提供足够信息，具体局限性（如计算成本、对非凸物体的适用性、实时性能等）未提及。

### 阅读优先级
**高**
理由：该方法创新性地将经典几何笼形概念与连续优化相结合，解决了接触密集型操作规划中的鲁棒性问题，且提供了仿真和实物实验验证，对从事机器人操作、接触规划或物理信息学习的读者具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Planning contact-rich whole-arm manipulation is challenging because interactions that involve extended robot geometry give rise to complex contact dynamics that are difficult to model accurately. This creates a need for planning principles that do not rely heavily on precise contact models. Caging offers one such geometric notion of robustness to modeling inaccuracy by restricting object escape through geometrically enclosing the object. However, existing caging formulations are difficult to incorporate into continuous optimization-based manipulation planning. We reformulate caging as a minimum-time escape problem in which the object seeks to leave an enclosing robot geometry in the shortest time. This yields a continuous escape-time field that measures the robot's enclosure quality and we show it satisfies an eikonal equation. We therefore can approximate this field using a physics-informed neural network, producing a smooth differentiable representation that can be embedded directly into manipulation planning. The resulting objective supports whole-arm manipulation planning to favor robot configurations resisting object escape. This improves the manipulation robustness to contact model mismatch, thus enabling planning with simplified contact models, including quasi-dynamic approximations and simplified object geometry. Across simulation and real-world experiments, we show improved robustness to disturbances and contact-model mismatch relative to baselines. These results suggest that geometric enclosure can serve as a practical robustness primitive for whole-arm manipulation. A supplementary video, which includes an intuitive overview of our method and experiment video results, is available on our project webpage.

</details>

#### 2026-06-20 - Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data

**Authors:** Yangtao Chen, Zixuan Chen, Peiyang Wang, Yong-Lu Li, Jing Huo, Jieqi Shi, Yang Gao
**Links:** [abs](https://arxiv.org/abs/2606.22136) - [pdf](https://arxiv.org/pdf/2606.22136)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** motion reconstruction, manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data
- 作者：Yangtao Chen, Zixuan Chen, Peiyang Wang, Yong-Lu Li, Jing Huo, Jieqi Shi, Yang Gao
- 出版日期：2026-06-20
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22136

### 一句话总结
Wh0 利用生成式视频世界模型构建大规模第一人称人手操作数据集，通过手部运动重建和视觉编辑将其转化为机器人可用的训练信号，显著提升了预训练灵巧操作模型的零样本泛化能力。

### 研究问题
如何解决现有灵巧操作数据在规模与场景/具身对齐之间的权衡问题，特别是如何从低成本的第一人称视频中获得与机器人部署对齐的大规模训练数据？

### 核心思路/方法
提出 Wh0 框架，核心包含三个步骤：
1. **数据生成**：使用生成式视频世界模型，基于语言、物体和场景条件，生成包含 5 万条第一人称人手-物体交互视频的数据集 WM-H。
2. **训练信号转换**：通过手部运动重建和视觉编辑，将生成的视频转换成可用于机器人训练的控制信号。
3. **联合训练**：将 WM-H 数据与有限的真实机器人数据共同训练，使预训练的视觉-语言-动作（VLA）模型适配到灵巧操作任务。

### 主要贡献
- 提出使用生成式视频世界模型作为灵巧操作数据的可扩展来源，突破了传统数据收集的规模与对齐矛盾。
- 构建了 WM-H 数据集（5 万条第一人称交互视频），并提供从视频到机器人可训练监督的转换方法。
- 在 18 个真实世界灵巧操作任务中，Wh0 将模型在未见任务上的零样本成功率为从 8.3% 提升至 38.9%。
- 消融实验表明，可扩展生成和场景/具身对齐是性能提升的关键因素。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对灵巧操作数据稀缺这一核心挑战，提出了新颖的生成式世界模型数据源方案，并在多个真实任务上取得了显著的零样本泛化提升（从 8.3% 到 38.9%），对机器人学习和具身智能领域具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Scaling dexterous manipulation requires generalization across objects, scenes, and tasks, yet existing data sources face a trade-off between scale and scene/embodiment alignment: teleoperation data is well aligned with robot deployment but expensive to collect; simulation is scalable but limited by the sim-to-real gap; and real egocentric videos scale effectively but remain misaligned with robot deployment. We propose Wh0, a framework that uses generative video world models as scalable and controllable sources of egocentric human-hand manipulation data to unlock the manipulation capabilities of pretrained dexterous VLA models. Conditioned on language, objects, and scenes, Wh0 uses a generative world model to produce WM-H, a 50k-episode dataset of egocentric human-object interaction videos. Wh0 then converts the generated videos into robot-trainable supervision through hand motion reconstruction and visual editing. Co-trained with a limited amount of real robot data, WM-H adapts pretrained VLA models to dexterous manipulation deployment. Across 18 real-world dexterous manipulation tasks, compared with a model post-trained only on robot data, Wh0 improves zero-shot success on unseen tasks from 8.3% to 38.9%. Ablation studies further show that scalable generation and scene/embodiment alignment are key drivers of performance gains. Videos and open-source code can be found on our project website: https://chenyt31.github.io/wh0.github.io/.

</details>

#### 2026-06-20 - DeformX: A Versatile Co-Simulation Framework for Deformable Linear Objects

**Authors:** Yi Yang, Xiang Fei, Lehong Wang, Chenhao Li, Zilin Dai, Henry Kou, Lu Li, Howie Choset
**Links:** [abs](https://arxiv.org/abs/2606.22116) - [pdf](https://arxiv.org/pdf/2606.22116)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DeformX: A Versatile Co-Simulation Framework for Deformable Linear Objects
- 作者：Yi Yang, Xiang Fei, Lehong Wang, Chenhao Li, Zilin Dai, Henry Kou, Lu Li, Howie Choset
- 出版日期：2026-06-20T15:57:29Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22116

### 一句话总结
DeformX 是一个将 Cosserat 杆物理引擎与 NVIDIA Isaac Sim 集成的联合仿真框架，能够对可变形线性物体（DLO）进行兼具物理真实性与视觉真实感的仿真，并支持机器人学习流水线。

### 研究问题
现有仿真方法在模拟可变形线性物体（如线缆、绳索）时存在不足：视觉仿真缺乏物理变形基础，而基于物理的仿真又因简化建模（如使用刚性链或通用软体）无法准确捕捉细长弹性结构的弯曲、扭转和剪切力学行为。

### 核心思路/方法
将专用的 Cosserat 杆物理引擎集成到 NVIDIA Isaac Sim 中：Cosserat 引擎负责模拟 DLO 的动力学、自碰撞以及与任意自由形态网格的接触交互；通过网格蒙皮技术将离散的杆变形映射到导入的 CAD 模型上，实现高保真可视化。

### 主要贡献
1. 提出了 DeformX，据称是首批将真实可视化、原理性物理与机器人学习流水线兼容性统一起来的 DLO 仿真框架。
2. 支持合成数据生成和策略学习，并在真实实验中验证了视觉和物理保真度。
3. 在 DeformX 生成数据上微调 Segment Anything Model 3，使真实图像线缆分割的 mAP@75 提升 10.2%；在 DeformX 中完全训练的绳索摆动策略，在 UR5e 机械臂真实实验中的平均目标命中误差为 6.6 厘米，展现出强大的 sim-to-real 迁移能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：本文针对仿真领域常见但棘手的可变形线性物体问题，提出了一个融合物理准确性与视觉真实感的联合仿真框架，且在机器人策略学习的 sim-to-real 迁移上给出了明确的定量结果（如 6.6 cm 命中误差），对从事机器人操作、仿真环境构建或 sim-to-real 研究的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Deformable linear objects (DLOs) such as wires, cables, and ropes are common in robotic manipulation tasks, yet simulating them with both visual realism and physical accuracy remains challenging. Existing visual simulation methods typically rely on procedural geometric primitives that lack physically grounded deformation behavior, while physics-based approaches with robot learning support often approximate DLOs as rigid-link chains or generic soft bodies, failing to accurately capture the bending, twisting, and shear mechanics of slender elastic structures. In this work, we introduce DeformX, a co-simulation framework that integrates a dedicated Cosserat rod physics engine with NVIDIA Isaac Sim, enabling DLO simulations that are both physically faithful and visually realistic. Our Cosserat rod engine simulates the dynamics and self-collisions of DLOs, and contact interactions with arbitrary free-form meshes. To achieve high-fidelity visualization, we employ mesh skinning to map discrete rod deformations onto imported CAD models. To the best of our knowledge, DeformX is the one of the first frameworks for DLO simulation that unifies realistic visualization, principled physics, and compatibility with robot learning pipelines. We demonstrate its versatility across synthetic data generation and policy learning for DLO manipulation, and validate visual and physical fidelity through comparisons against real-world experiments. Notably, fine-tuning Segment Anything Model 3 (SAM3) on DeformX-generated data yields a 10.2% mAP@75 improvement in real-image wire segmentation, and a rope-swinging policy trained entirely in DeformX achieves a mean target-hitting error of 6.6 cm on a UR5e manipulator in real-world trials, highlighting its strong sim-to-real transfer capability.

</details>

#### 2026-06-18 - S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence

**Authors:** Yalun Dai, Hao Li, Shulin Tian, Runmao Yao, Yuhao Dong, Fangzhou Hong, Zhaoxi Chen, Fangfu Liu, Baoliang Tian, Dingwen Zhang, Tao Wang, Kim-Hui Yap, Ziwei Liu
**Links:** [abs](https://arxiv.org/abs/2606.20515) - [pdf](https://arxiv.org/pdf/2606.20515)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence
- 作者：Yalun Dai, Hao Li, Shulin Tian, Runmao Yao, Yuhao Dong, Fangzhou Hong, Zhaoxi Chen, Fangfu Liu, Baoliang Tian, Dingwen Zhang, Tao Wang, Kim-Hui Yap, Ziwei Liu
- 出版日期：2026-06-18
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2606.20515) | [PDF](https://arxiv.org/pdf/2606.20515)

### 一句话总结
本文提出 **S-Agent**，一种空间工具使用智能体范式，将空间推理建模为时空证据累积过程，通过层次化工具和记忆机制显著提升多视图和视频空间推理性能，并基于其生成的轨迹微调出紧凑型空间智能体S-Agent-8B。

### 研究问题
现有视觉语言模型(VLM)和工具增强智能体大多依赖静态、无状态推理，无法对持续演进的3D世界进行空间推理。本文试图解决如何实现连续多视图图像和视频中的空间智能问题。

### 核心思路/方法
1. **任务重定义**：将空间推理从孤立帧级预测重塑为**时空证据累积**的场景级理解。
2. **语义规划与工具层级**：VLM作为语义规划器决定需何种证据；层次化空间工具和专家将2D对象提升为3D几何证据，并聚合为高级空间知识（如计数、测量、朝向、相对位置）。
3. **时间记忆机制**：包括**场景记忆**（维护持续演进的场景状态）和**智能体记忆**（累积推理上下文），以跨帧和推理步骤整合证据。
4. **训练与微调**：无训练地增强开源和闭源VLM；进一步对S-Agent生成的空间轨迹（S-300K）进行监督微调，得到紧凑模型S-Agent-8B。

### 主要贡献
1. 提出 **S-Agent** 范式，将空间推理转化为证据累积过程，突破静态推理限制。
2. 引入层次化空间工具和双记忆机制（场景记忆+智能体记忆），实现跨时空证据整合。
3. 在多项多视图和视频空间推理基准上，无需额外训练即可一致提升开源/闭源VLM性能。
4. 通过微调S-Agent生成的轨迹，得到紧凑模型 **S-Agent-8B**，性能超越同尺度基线（如Qwen3-VL-8B），媲美先进闭源模型（如GPT-5.4、Gemini 3）。

### 局限性
摘要未提供足够信息，无法评估具体局限性（如计算开销、泛化边界、失败案例等）。

### 阅读优先级
**高**
理由：该工作聚焦空间推理这一具身智能/机器人领域核心挑战，提出新颖的“证据累积+工具层级+记忆”范式，实验结果表明其既能无训练增强现有模型，又能通过微调获得紧凑高效模型，实用性和创新性均显著，对从事空间感知、VLM增强和多模态推理的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-world spatial intelligence requires reasoning over a continuous and evolving 3D world, yet existing VLMs and tool-augmented agents largely remain tied to static, stateless inference from isolated visual observations. We introduce \textbf{\textsc{S-Agent}}, a spatial tool-use agentic paradigm for understanding and reasoning over continuous multi-view images and videos. By formulating spatial reasoning as spatio-temporal evidence accumulation rather than isolated frame-level prediction, \textsc{S-Agent} reshapes spatial perception into scene-centric understanding beyond frame-centric recognition. Specifically, \textsc{S-Agent} casts the VLM as a semantic planner that decides what evidence is needed, while a hierarchy of spatial tools and experts grounds objects in 2D, lifts them into 3D geometric evidence, and aggregates this evidence into high-level spatial knowledge (\textit{e.g.}, counting, measurement, orientation, and relative position). Additionally, a temporal memory mechanism, including Scene Memory for maintaining the evolving scene state and Agent Memory for accumulating reasoning context, enables evidence integration across frames and reasoning steps. Comprehensive experiments on multi-view and video spatial reasoning benchmarks show that \textsc{S-Agent} consistently improves both open-source and closed-source VLMs in a training-free manner. Beyond inference-time augmentation, supervised fine-tuning (SFT) on \textsc{S-Agent}-generated spatial trajectories \textsc{S-300K} yields \textsc{S-Agent-8B}, a compact spatial agent that significantly surpasses similar-scale baselines (e.g., Qwen3-VL-8B) and performs comparably to advanced closed-source models (e.g., GPT-5.4 and Gemini 3).

</details>

#### 2026-06-18 - TaCauchy: An Extensible FEM Framework for Vision-Based Tactile Simulation

**Authors:** Hengfei Zhao, Yifan Xie, Junhao Gong, Yue Sun, Kai Zhu, Weihua He, Shoujie Li, Haohuan Fu, Wenbo Ding
**Links:** [abs](https://arxiv.org/abs/2606.20426) - [pdf](https://arxiv.org/pdf/2606.20426)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TaCauchy: An Extensible FEM Framework for Vision-Based Tactile Simulation
- 作者：Hengfei Zhao, Yifan Xie, Junhao Gong, Yue Sun, Kai Zhu, Weihua He, Shoujie Li, Haohuan Fu, Wenbo Ding
- 出版日期：2026-06-18
- 分类：具身/机器人/增强现实应用（Embodied / Robotics / AR Applications）
- 链接：https://arxiv.org/abs/2606.20426

### 一句话总结
TaCauchy是一个基于有限元法（FEM）的视觉触觉仿真框架，通过集成到Isaac Sim平台中，从第一性原理直接计算柯西应力张量以提供精准的力学场，并支持多种触觉传感器的快速集成。

### 研究问题
如何在高性能GPU加速的机器人仿真平台（如Isaac Sim）中，提供准确且物理一致的机械应力场，以支持基于视觉的触觉传感器的高保真仿真和强化学习任务。

### 核心思路/方法
- 基于统一增量势能接触（UIPC）求解器，利用超弹性本构定律直接计算柯西应力张量。
- 将应力张量投影至接触表面，从而获取接触力矢量与压力分布，避免依赖经验估计。
- 实现自动化网格生成（含几何感知自适应细化）和模块化传感器接口，支持GelSight Mini、DIGIT、9DTact等多种触觉传感器的快速扩展与配置。

### 主要贡献
1. 提出TaCauchy框架，首次将基于物理的有限元力计算无缝集成到Isaac Sim中，提供第一性原理的力学真值。
2. 在单环境仿真中达到33.40 FPS，60个并行环境聚合吞吐量达555 FPS，且应力提取开销低于1毫秒，验证了实时性与可扩展性。
3. 物理验证实验显示，在1.2556 N至4.7332 N的力范围内，模拟与真实触觉响应的结构相似性指数（SSIM）高于0.93，证明框架能够为下游机器人操作任务提供准确、物理基础的力监督信号。

### 局限性
摘要未提供足够信息。具体实验局限性（如特定材料模型的适用范围、网格细化对复杂几何的误差、或对超弹性本构参数的敏感度等）未在摘要中提及。

### 阅读优先级
高  
理由：该工作解决了视觉触觉仿真中力学场准确性这一关键瓶颈，且提供了可直接部署在主流机器人仿真平台（Isaac Sim）上的开源自适应框架，对从事触觉传感、机器人操作和仿真到现实迁移的研究者具有较高的实用价值和参考意义。

</details>

<details>
<summary>Abstract</summary>

Vision-based tactile sensors require high-fidelity simulation for reinforcement learning, yet existing approaches struggle to provide accurate mechanical stress fields within GPU-accelerated robotics platforms. We present TaCauchy, an extensible Finite Element Method (FEM) framework that integrates rigorous physics-based force computation into Isaac Sim. Built on the Unified Incremental Potential Contact (UIPC) solver, TaCauchy directly computes Cauchy stress tensors from hyperelastic constitutive laws and projects them onto contact surfaces to obtain traction forces and pressure distributions, providing mechanical ground truth from first principles rather than empirical estimation. Our framework features automatic mesh generation with geometry-aware adaptive refinement and a modular sensor interface enabling rapid integration of diverse sensors (GelSight Mini, DIGIT, 9DTact) with minimal configuration. Performance benchmarks demonstrate 33.40 FPS for single environments and 555 FPS aggregate throughput across 60 parallel environments, with stress extraction overhead under 1 ms. Physical validation experiments show strong agreement between simulated and real tactile responses across force ranges from 1.2556 N to 4.7332 N, achieving SSIM above 0.93, confirming the framework's capability to provide accurate, physically-grounded force supervision for downstream robotic manipulation tasks.

</details>

#### 2026-06-18 - Holo-World: Unified Camera, Object and Weather Control for Video World Model

**Authors:** Xiangchen Yin, Wenzhang Sun, Jiahui Yuan, Zijie Liu, Yinda Chen, Wei Li, Dachun Kai, Chunfeng Wang, Xiaoyan Sun
**Links:** [abs](https://arxiv.org/abs/2606.20083) - [pdf](https://arxiv.org/pdf/2606.20083)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Holo-World: Unified Camera, Object and Weather Control for Video World Model
- 作者：Xiangchen Yin, Wenzhang Sun, Jiahui Yuan, Zijie Liu, Yinda Chen, Wei Li, Dachun Kai, Chunfeng Wang, Xiaoyan Sun
- 出版日期：2026-06-18T11:01:34Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.20083

### 一句话总结
Holo-World 提出了一种统一的视频世界模型，能够从单张图像出发，通过相机、物体控制和天气指令，生成保持世界状态或转换到目标天气状态的视频。

### 研究问题
如何从单张图像出发，实现统一的相机、物体和天气控制，并能够根据指令生成保持原始世界或转移到目标天气状态的视频。

### 核心思路/方法
1. 构建 HoloStateData 数据集：将多样的视频转换为统一的控制样本，提供相机、物体和天气的监督信号。
2. 设计 Holo-World 模型：包含统一的场景适配器（Unified Scene Adapter），将世界保持和天气转移分解为不同的参数子空间，利用渲染背景、几何缓冲区和物体控制来维持场景结构，同时建模天气相关的表观和粒子效果。
3. 提出 Scene-Weather Decomposed CFG：分别引导场景和天气残差，增强目标天气效果而不过度放大整个条件。

### 主要贡献
1. 提出首个从单张图像出发、支持相机、物体和天气统一控制的视频世界模型 Holo-World。
2. 构建了 HoloStateData 数据集，用于大规模监督学习。
3. 在保持精确相机和物体控制及场景结构的同时，能够将场景转移到多样目标天气状态，在天气状态生成上优于视频到视频的天气编辑基线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该工作聚焦于视频世界模型在统一控制（相机、物体、天气）方面的创新，对于研究可控视频生成、世界模型或多模态控制的研究者有一定参考价值。但摘要未提供详尽的实验对比结果和具体性能数据，实用性评估需进一步阅读原文。

</details>

<details>
<summary>Abstract</summary>

Video world models are moving toward preserving an observed world under controllable camera and object motion while allowing its environmental state to change. Yet these controls remain isolated, and weather generation typically relies on a source video or reconstructed scene that already specifies future structure. We study a first-frame-anchored source-to-state setting, where the model starts from a single image and follows explicit camera and object controls and an optional weather instruction, then generates a video that either preserves the source world or transfers it to a target weather state. To address these challenges, we first build HoloStateData, a state video dataset that turns diverse videos into unified control samples for camera, object, and weather supervision. Second, we introduce Holo-World, a unified controllable video world model that jointly controls scene from a single image. Its Unified Scene Adapter factorizes world preservation and weather transfer into distinct parameter subspaces, using rendered background, geometry buffers, and object controls to maintain controlled scene structure while modeling weather-dependent appearance and particle effects. Additionally, Scene-Weather Decomposed CFG guides scene and weather residuals separately, strengthening target weather effects without over-amplifying the full condition. Quantitative and qualitative experiments demonstrate that Holo-World maintains precise camera and object control with consistent scene structure while transferring scenes into diverse target weather state, outperforming video-to-video weather editing baselines on weather-state generation. Our project page is available at \url{https://xiangchenyin.github.io/Holo-World/}.

</details>

#### 2026-06-18 - SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour

**Authors:** Kaixin Lan, Ze Wang, Hongyi Li, Lei Jiang, Chaojie Fu, Chengkai Su, Choi Lam Wong, Yongbin Jin, Hongtao Wang
**Links:** [abs](https://arxiv.org/abs/2606.19928) - [pdf](https://arxiv.org/pdf/2606.19928)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour
- 作者：Kaixin Lan, Ze Wang, Hongyi Li, Lei Jiang, Chaojie Fu, Chengkai Su, Choi Lam Wong, Yongbin Jin, Hongtao Wang
- 出版日期：2026-06-18
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.19928

### 一句话总结
本文提出一种内置对称等变性的端到端世界模型框架SWAP，使四足机器人在真实世界中完成破纪录的2.13米跨越和1.63米攀爬，并展现了良好的几何泛化和零样本迁移能力。

### 研究问题
如何通过结构先验（对称等变性）减少纯数据驱动潜世界模型在极端跑酷中冗余学习左右对称交互模式的负担，提升潜空间效率并增强下游策略的几何泛化能力。

### 核心思路/方法
将对称等变性直接嵌入世界模型和演员-评论家网络中。通过在模型架构层面显式编码左右对称的几何结构约束，使模型不必独立学习对称模式，从而更高效地捕获几何规律。在真实世界四足机器人跑酷任务上进行验证。

### 主要贡献
1. 提出SWAP框架，将对称等变性嵌入端到端的潜世界模型和策略网络。
2. 在真实世界测试中，机器人实现跨越2.13米间隙和攀爬1.63米平台，创造四足机器人跑酷纪录。
3. 展示了对未见镜像地形的强几何泛化能力，以及在多样化户外环境中的优异零样本迁移能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该论文在四足机器人跑酷任务上取得了显著的实证突破（破纪录性能），并引入对称等变形作为结构先验，思路具有一定的启发性。但摘要未涉及方法细节、训练流程、实验设置等，需要阅读全文才能评估其技术贡献的完整性和可复现性。如果您关注机器人运动控制中的几何先验应用，可优先阅读。

</details>

<details>
<summary>Abstract</summary>

While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns. This inflates the learning burden and hinders the capture of geometric regularities, restricting the latent space's efficiency for downstream policies. To address this, we propose SWAP, an end-to-end equivariant symmetric world model. This framework embeds symmetry directly into both the world model and the actor-critic networks. In real-world tests, the robot leaps across a 2.13 m gap and climbs a 1.63 m platform, breaking records for quadruped parkour. Furthermore, the framework exhibits robust geometric generalization to unseen mirrored terrains and exceptional zero-shot transferability across diverse outdoor environments. These results demonstrate that symmetry equivariance is an effective structural prior for pushing the physical boundaries of learned legged locomotion.

</details>

#### 2026-06-18 - Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding

**Authors:** Jianing Li, Zhou Fang, Yijiang Liu, Li Du
**Links:** [abs](https://arxiv.org/abs/2606.19776) - [pdf](https://arxiv.org/pdf/2606.19776)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding
- 作者：Jianing Li, Zhou Fang, Yijiang Liu, Li Du
- 出版日期：2026-06-18
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2606.19776) | [PDF](https://arxiv.org/pdf/2606.19776)

### 一句话总结
Occ-VLM提出了一种仅依赖RGB图像和单个2D视觉编码器的3D场景理解框架，通过重建3D占用作为几何先验，实现无需显式3D输入的视觉-语言联合推理。

### 研究问题
现有3D视觉语言模型往往需显式3D输入（如点云、RGB-D序列）或引入额外的3D几何编码器，导致3D几何感知与2D视觉语言预训练之间的结构性解耦，阻碍了统一的3D视觉语言表示。本文旨在仅用2D图像实现3D场景的几何感知与语言推理的融合。

### 核心思路/方法
1. **输入**：仅使用带位姿的RGB图像，并采用单一2D视觉编码器。
2. **3D占用重建**：作为辅助几何先验，从2D图像中重建3D场景占用信息。
3. **空间关联**：利用3D占用将前景2D标记与3D空间进行空间关联。
4. **语言解码**：关联后的标记由大语言模型（LLM）解码，实现统一的场景理解任务。

### 主要贡献
- 提出Occ-VLM，仅用2D图像输入即可实现3D几何感知与视觉语言推理的统一框架。
- 在多视图占用预测任务上达到当前最优性能。
- 在3D视觉问答（VQA）和3D密集描述基准上，性能与采用3D输入的VLM持平。

### 局限性
摘要未提供足够信息：未提及在极端遮挡、大尺度场景或实时推理能力上的局限性，也未讨论对训练数据规模或标注成本的要求。

### 阅读优先级
**中**。理由：该工作聚焦于3D室内场景理解，在仅用2D图像的情况下实现了与3D输入VLM相当的性能，且在多视图占用预测上达到SOTA，对嵌入式智能和机器人视觉领域有参考价值。但摘要未提供详细的实验设置和消融分析，约束了对其实际效果的全面评估。

</details>

<details>
<summary>Abstract</summary>

Recently, vision-language models (VLMs) have made significant progress in 3D scene understanding, driving advances in applications such as embodied intelligence and robotic vision. However, existing approaches typically either rely directly on explicit 3D inputs (e.g., point clouds or RGB-D sequences), or introduce an additional 3D geometry encoder to derive 3D-aware visual tokens from 2D images. Such designs structurally decouple 3D geometric perception from the rich 2D semantics learned via vision-language pre-training, hindering the development of a unified 3D vision-language representation. In this work, we propose Occ-VLM, a novel framework for 3D scene understanding that operates purely on posed RGB images and employs a single 2D vision encoder. Specifically, Occ-VLM reconstructs 3D scene occupancy as an auxiliary geometric prior, which is utilized to spatially associate foreground 2D tokens with 3D space. These tokens are then decoded by a Large Language Model (LLM) for unified scene understanding. Extensive experiments demonstrate that Occ-VLM achieves both accurate geometric perception and robust vision-language reasoning: it attains state-of-the-art performance on multi-view occupancy prediction, while performing on par with 3D-input VLMs on 3D Visual Question Answering (VQA) and 3D dense captioning benchmarks.

</details>

#### 2026-06-17 - Modeling Branches for Active Manipulation using Iterative Parameter Estimation

**Authors:** Madhav Rijal, Rashik Shrestha, Trevor Smith, Yu Gu
**Links:** [abs](https://arxiv.org/abs/2606.19314) - [pdf](https://arxiv.org/pdf/2606.19314)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Modeling Branches for Active Manipulation using Iterative Parameter Estimation
- 作者：Madhav Rijal, Rashik Shrestha, Trevor Smith, Yu Gu
- 出版日期：2026-06-17
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.19314

### 一句话总结
本文提出一种通过迭代估计材料参数来建模植物分支的方法，以支持精细的分支操作；实验表明，该方法在路径长度略有增加的情况下，显著减少了形变能量。

### 研究问题
如何对形态各异的植物分支进行精确建模，以支持农业机器人中精细、低损伤的分支操作（如重定位、稳定、清除视觉障碍）。

### 核心思路/方法
1. **分支建模**：从点云数据构建四面体分支模型，并利用有限元方法模拟其行为。
2. **参数估计**：基于真实观测的形变数据，通过迭代估计分支的材料参数。
3. **运动规划**：结合形变感知的运动规划器，计算最优路径以移动并稳定分支，使分支处于另一机器人的视野内。

### 主要贡献
- 提出了一种结合点云建模、有限元仿真和迭代参数估计的植物分支建模方法。
- 通过30次不同几何和材料属性的分支试验验证：该方法平均减少形变能量35.69%，同时平均增加路径长度8.10%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法针对农业机器人中精细分支操作这一具体场景，结合了建模、仿真与规划，结果量化且有效。但该方法仅基于摘要无法判断其泛化能力或实现复杂度，对机器人操作领域研究者有一定参考价值；若对植物建模或软体操作不感兴趣，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

This study presents a method for modeling diverse plant branches by iteratively estimating material parameters to support delicate branch manipulation. Branch manipulation is necessary in agricultural robotics for plant repositioning, stabilizing, and clearing visual obstructions in dense foliage. The proposed method builds a tetrahedral branch model from point-cloud data and simulates its behavior using the finite element method. Using real observed deformation data, it iteratively estimates branch parameters and then computes an optimal path with a deformation-aware motion planner to move and stabilize branches within another robot's field of view. Across 30 trials on branches with varying geometries and material properties, the proposed method reduced the deformation energy by 35.69% while increasing the path length by 8.10% on average.

</details>

#### 2026-06-17 - OneCanvas: 3D Scene Understanding via Panoramic Reprojection

**Authors:** Bartłomiej Baranowski, Dave Zhenyu Chen, Matthias Nießner
**Links:** [abs](https://arxiv.org/abs/2606.19253) - [pdf](https://arxiv.org/pdf/2606.19253)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OneCanvas: 3D Scene Understanding via Panoramic Reprojection
- 作者：Bartłomiej Baranowski, Dave Zhenyu Chen, Matthias Nießner
- 出版日期：2026-06-17
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.19253

### 一句话总结
OneCanvas 提出一种全景画布表示方法，将所有视角的图像块特征投影到单一等距柱面画布上，使预训练视觉语言模型无需复杂几何编码器即可直接理解3D场景，并在多个基准上取得最优结果。

### 研究问题
如何在不依赖复杂几何编码器和大量训练预算的情况下，让视觉语言模型（VLM）具备对3D场景的空间推理能力，同时支持从特定视角进行情境化推理（如机器人和具身AI所需）。

### 核心思路/方法
- **全景画布投影**：将每个视角的图像块特征，利用其深度和相机姿态反投影到3D世界坐标，再根据画布原点观察该点的连续经纬度放置到等距柱面画布上，不进行光栅化或跨视图特征聚合。
- **3D位置嵌入**：在每个图像块特征中加入其度量坐标的3D位置嵌入，以恢复将世界坐标压缩到角度坐标时丢失的深度信息。
- **无需模型修改**：所有帧的块特征共享同一个空间坐标系，无需对VLM骨干网络进行融合或重大架构修改，预训练VLM直接将其作为普通图像处理。
- **空间预训练课程**：在空画布上从真实图像中提取物体块特征，程序化地放置在选定的3D世界位置，生成覆盖多种空间推理任务的即时监督，并控制答案分布以减少空间推理捷径。

### 主要贡献
1. 提出一种无需复杂几何编码器或大量训练修改的3D场景表示方法，使VLM能像处理普通图像一样理解3D场景。
2. 引入空间预训练课程，通过程序化生成多样化的空间推理训练样本，减少推理捷径。
3. 在SQA3D、VSI-Bench和SPBench上达到最先进精度，且训练计算量比最强竞争对手低一个数量级。

### 局限性
摘要未提供足够信息（如方法在动态场景或复杂光照下的表现、对深度和姿态精度的依赖程度、画布分辨率与场景规模的可扩展性等）。

### 阅读优先级
**高**
理由：该方法在保持较高空间推理精度的同时显著降低了训练计算成本，且直接兼容现有预训练VLM，对具身智能、机器人等领域的3D场景理解具有重要实用价值。摘要中提到的创新性全景画布表示和预训练课程设计新颖，实验结果（SOTA）具有说服力。

</details>

<details>
<summary>Abstract</summary>

Existing approaches to 3D scene understanding in Vision-Language Models (VLMs) either rely on complex, model-specific geometry encoders or large training budgets in pursuit of spatial reasoning. Instead, OneCanvas aggregates patch features from all views onto a single equirectangular panoramic canvas. Namely, each patch is unprojected to a 3D world coordinate using its depth and camera pose, then placed on the canvas at the continuous longitude and latitude of that point as seen from the canvas origin, with no rasterization or aggregation across overlapping views. A 3D position embedding of the patch's metric coordinates is added to its feature, restoring the depth lost when collapsing the world position to an angular canvas coordinate. Patches from all frames thus share one spatial coordinate system with no fusion or major architectural modifications of the backbone. The pretrained VLM consumes this representation as if it were an ordinary image. Because the canvas can be centered on any pose of interest, the same representation directly supports situated reasoning from a specific viewpoint, a common requirement in robotics and embodied AI. Thanks to this representation, we can also introduce a spatial pretraining curriculum: by procedurally placing patch features of objects, drawn from real images, at chosen 3D world positions on an otherwise empty canvas, we generate on-the-fly supervision spanning a broad range of spatial reasoning tasks, with answer distributions controlled to reduce spatial reasoning shortcuts. OneCanvas achieves state-of-the-art accuracy on SQA3D and VSI-Bench, and generalizes to out-of-distribution data on SPBench, using an order of magnitude less training compute than the strongest competing methods.

</details>

#### 2026-06-17 - Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation

**Authors:** Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, Weiming Li, Dong Wang, Huchuan Lu, Xu Jia
**Links:** [abs](https://arxiv.org/abs/2606.18960) - [pdf](https://arxiv.org/pdf/2606.18960)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, manipulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation
- 作者：Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, Weiming Li, Dong Wang, Huchuan Lu, Xu Jia
- 出版日期：2026-06-17
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2606.18960, PDF: https://arxiv.org/pdf/2606.18960

### 一句话总结
提出记忆增强的世界模型 Mem-World，通过4D腕部视角表面元索引记忆（W-VMem）解决机器人持续操作任务中场景细节遗忘和幻觉问题，提升长时程预测与策略评估性能。

### 研究问题
在持续操作世界中模型的预测中，末端执行器频繁遮挡和腕部相机快速运动导致当前观测不足以预测未来视角，模型容易遗忘或幻觉先前帧的场景细节，而现有记忆检索策略难以在动态操作场景中识别信息丰富的历史帧。

### 核心思路/方法
提出 Mem-World，核心组件为 W-VMem——一种以腕部视角为中心的4D表面元索引记忆结构，将历史观测锚定到随时间演变的表面元素上。通过显式建模场景元素被观测的时间与空间位置，基于未来动作条件进行几何感知的历史帧检索。生成时，利用表面元渲染与评分策略选择信息丰富且不冗余的历史帧作为预测上下文。

### 主要贡献
1. 提出 Mem-World，一种记忆增强的多视图动作条件世界模型，实现复杂操作场景的持续预测。
2. 提出 W-VMem，一种4D腕部视角表面元索引记忆，支持几何感知的历史帧检索。
3. 实验表明：相比 Ctrl-World，Mem-World 在长短时程任务中生成更可靠的持续 rollout，策略评估的 Pearson 相关系数提升14.5%；通过合成数据增强，长时程任务成功率从58%提升至72%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对机器人操作中世界模型预测的持续性问题（遮挡与运动导致的遗忘/幻觉），提出创新的4D记忆结构，在策略评估和策略改进任务上均有显著量化提升（相关系数增长14.5%，成功率提升14个百分点），对具身智能领域有较大借鉴价值。

</details>

<details>
<summary>Abstract</summary>

Action-conditioned world models have emerged as a promising paradigm for robot learning, offering a scalable alternative to costly real-world experimentation by generating action-consistent video rollouts. However, persistent world modeling remains challenging in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the current observation insufficient for predicting future views, causing models to forget or hallucinate scene details seen in earlier frames. Existing memory retrieval strategies often fail to identify informative history in dynamic manipulation scenarios. To address this limitation, we propose Mem-World, a memory-augmented multi-view action-conditioned world model. At its core, we present W-VMem, a 4D wrist-view-centered surfel-indexed memory that anchors historical observations to temporally evolving surface elements. By explicitly modeling when and where scene elements are observed, W-VMem enables geometry-aware retrieval of relevant history frames conditioned on future actions. During generation, relevant history frames are selected via surfel-based rendering and scoring, providing informative and non-redundant context for prediction. Extensive experiments show that Mem-World generates persistent rollouts in complex manipulation scenarios, enables more reliable policy evaluation than Ctrl-World, improving the Pearson correlation with real-world performance by 14.5\%, and supports effective policy improvement through synthetic data generation, increasing success rates from 58\% to 72\% on long-horizon tasks.

</details>

#### 2026-06-17 - A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks

**Authors:** Kui Yang, Xianlei Long, Haoxuan Li, Yan Ding, Chao Chen
**Links:** [abs](https://arxiv.org/abs/2606.18646) - [pdf](https://arxiv.org/pdf/2606.18646)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks  
- 作者：Kui Yang, Xianlei Long, Haoxuan Li, Yan Ding, Chao Chen  
- 出版日期：2026-06-17  
- 分类：具身智能 / 机器人学 / AR应用  
- 链接：https://arxiv.org/abs/2606.18646  

### 一句话总结
本文提出了BestMan，一个可扩展的“真实-仿真-真实”具身智能平台，通过自动化场景生成、仿真引导的任务形式化与技能学习架构、以及硬件无关的统一中间件，解决家庭移动操作任务在真实与仿真环境之间无缝迁移的关键挑战。

### 研究问题
如何在非结构化的家庭环境中，实现真实到仿真再到真实的低成本、高保真、可兼容的无缝迁移，从而高效开发、集成和部署移动操作策略。

### 核心思路/方法
1. **自动化场景生成模块**：从真实观测自动重建高保真仿真场景。  
2. **仿真引导的任务形式化与技能学习架构**：支持在仿真中灵活集成和规模化评估混合技能策略。  
3. **硬件无关的统一中间件**：确保跨异构移动操作机器人的兼容性，实现仿真到真实的无缝迁移。

### 主要贡献
- 提出BestMan平台，首次在真实-仿真-真实全周期中实现可扩展的无缝迁移。  
- 设计自动化场景生成模块，降低仿真场景重建成本。  
- 提出仿真引导的任务形式化与技能学习架构，支持混合策略的灵活集成与大规模评估。  
- 开发硬件无关的统一中间件，提升真实部署的可扩展性与兼容性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该研究直面具身智能领域“真实-仿真-真实”迁移的核心瓶颈，提出的三大模块（自动化场景生成、仿真引导学习、硬件无关中间件）具有明确的工程创新和实用价值，且实验证明其在标准基准测试中表现优异。适合关注具身智能、机器人仿真迁移及家庭操作任务的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Mobile manipulation is a fundamental capability in embodied intelligence robotics. The growing demand for robust and generalizable manipulation in unstructured household environments has driven rapid progress in embodied intelligence platforms. However, achieving a seamless transfer across the real-to-sim-to-real cycle faces three key challenges, including costly high-fidelity simulation scenes reconstruction, the complexity of systematic strategy evaluation in simulation, and incompatible real-world deployments. To address these challenges, we develop BestMan, a scalable and seamless real-to-sim-to-real platform that bridges the gap between the simulation and the real world, enabling effective strategy development, integration, and deployment for household mobile manipulation. Specifically, we design a novel Automated Scene Generation (ASG) module to reconstruct realistic simulations from real observations. Then, we propose a simulation-guided task formalization and skill learning architecture that supports the flexible integration and large-scale evaluations of hybrid skill strategies in simulation. Finally, to enhance the real-world scalability, we develop a Hardware-agnostic and Unified Middleware (HUM) to ensure seamless and compatible sim-to-real transfer across heterogeneous mobile manipulators for real deployments. Experimental results demonstrate the superior performance of our proposed platform in establishing standardized benchmarks and facilitating promising research in the field of mobile manipulation.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
