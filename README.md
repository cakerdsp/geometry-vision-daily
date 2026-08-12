# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：52
- 分类分布：
  - Neural Scene Representations & Rendering: 17
  - 3D Reconstruction & Multi-view Geometry: 15
  - Embodied / Robotics / AR Applications: 15
  - Geometry Foundation Models: 3
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**趋势一：3DGS 正从“重建工具”升级为“推理与任务执行平台”**
多篇论文不再将 3D Gaussian Splatting 仅视为新视角合成的工具，而是将其作为承载高层认知任务的统一场景表示。典型代表包括 CausalSplat（将 VLM 与 3D 场景图集成于 3DGS 以实现因果/常识推理）、LEGO（在 3DGS 上构建层级化语言场景图以支撑空间推理）、Embodied Multimodal Grounding（将语义 3DGS 作为移动操作机器人从感知到动作的共享接口）。这一趋势表明 3DGS 正从感知层向认知-决策层延伸。

**趋势二：几何基础模型（VFMs）成为训练时的“免费”监督信号源**
与直接微调或特征拼接不同，今日多篇论文将几何基础模型作为**训练阶段**的监督器或先验注入器，避免推理阶段引入额外开销。代表性工作包括：4D-WAM（利用几何基础模型输出定义 4D 一致性损失，监督世界模型预测）、VGGD（借助 VGGT 的先验 tokens 增强前馈几何建模）、Self-Geometry（测试时直接施加显式多视图几何约束）。这一趋势呼应了“基础模型作为可插拔教师”的范式转型。

**趋势三：极端稀疏视角与退化输入下的鲁棒重建成为焦点**
多篇论文聚焦于在实际采集条件中常见的退化情景——视角极少（CasDeblurGS：仅两张模糊图像）、训练-推理分布不匹配（TRACE-GS：稀疏视角导致去噪轨迹偏差）、前馈方法产生冗余原语（Compact Feed-Forward 3D Gaussians）。这些工作共同指向一个核心问题：如何在信息严重不足或分布偏移时保持几何与外观的稳定性，而非在理想条件下继续“刷分”。

**趋势四：空间推理能力成为 VLM 与具身智能的共同瓶颈突破点**
从视觉语言模型的空间推理（MVRD：多视角关系蒸馏）、到自动驾驶的跨视角时序定位（Cross-View Sequential Visual Localization）、再到 4D 世界模型的一致性（4D-WAM），空间理解已从“能不能看见”转向“能不能想清楚”。MVRD 明确指出现有 VLM 的视觉-空间表征“几何上脆弱”，而跨视角定位则利用时序上下文补偿单帧信息不足——两条路线共同表明空间推理是当前多模态与具身智能的主要短板。

**趋势五：面向物理极限与真实世界部署的“高保真”模拟成为前沿探索方向**
WildFireGS 将 GPU 场景直接用于基于物理的野火传播模拟（粒子燃烧模型原生运行于高斯表示），而 Autonomous Racing Agent 则在 256 km/h 的真实车辆极限工况下训练世界模型。这两项工作将神经场景表示从“数字孪生观赏”推向“数字孪生用于物理预测与决策”，代表着场景表示与物理学/控制论的交叉融合。


#### 技术路线观察

| 方向 | 技术侧重 | 代表论文 |
|------|---------|---------|
| 几何基础模型 | 作为训练时监督（4D-WAM）、先验注入（VGGD）、测试时自适应（Self-Geometry）、关系蒸馏（MVRD） | 4D-WAM, VGGD, Self-Geometry, MVRD |
| 3D/4D 重建 | 表面与高斯联合优化（Gaussian Sculpting）、稀疏视角恢复（CasDeblurGS, TRACE-GS）、原语压缩（Compact Feed-Forward） | Gaussian Sculpting, CasDeblurGS, TRACE-GS |
| 神经场景表示 | 语义层级化（LEGO, CausalSplat）、语义-物理融合（WildFireGS）、预测式缓存（Amulet） | LEGO, CausalSplat, WildFireGS, Amulet |
| 机器人/AR 应用 | 语义 3DGS 作为完整闭环共享接口（Embodied Grounding）、持久世界模型（PBD-AG）、紧凑动作潜在模型（SLIM）、边缘-云分割推理（Edge SLAM） | Embodied Grounding, PBD-AG, SLIM, 5G Edge SLAM |

**路线交叉观察**：
- 几何基础模型正从“最终输出的预测器”转变为“中间监督信号的提供者”，即从替代人工标注走向替代工程化的几何约束。
- 3DGS 的应用边界显著拓宽——从纯感知（重建）到认知（推理/分割/问答）再到物理（火灾模拟、车辆动力学）。
- 机器人端存在两条路线：一条是“重表示”路线（Embodied Grounding 依赖语义 3DGS 做多阶段共享表示），另一条是“轻模型”路线（SLIM 用 0.5B 参数避开大规模 VLA 骨干）——二者对计算资源的取舍形成鲜明对比。


#### 值得优先阅读的论文

1. **CausalSplat（2608.11150）** — 定义了“推理式 3D 高斯分割”这一新任务并提供了基准与框架，是了解 3DGS 从感知走向推理的关键文献。对具身智能、开放词汇 3D 理解研究者具有直接参考价值。

2. **TRACE-GS（2608.10286）** — 直击扩散模型训练-推理分布不匹配的根本性问题。其在线策略轨迹蒸馏+特权几何信息的范式，可能对未来所有基于扩散先验的 3D 重建工作产生范式影响。

3. **MVRD（2608.10864）** — 为 VLM 空间推理提供了一个轻量、有效且不破坏视觉-语言对齐的蒸馏方案。该结果挑战了“几何接地必须增加模型大小”的假设，对于机器人 VLA 策略的轻量化设计有直接启发。

4. **Embodied Multimodal Grounding（2608.10756）** — 提供了完整的从语言到 3D 接地再到动作执行的实机验证（50 次试验），对比了 PointVLA 与 DexVLA。对于具身操作研究者，这是一份难得含真实机器人评估数据的近期参考。

5. **4D-WAM（2608.10107）** — 将几何基础模型用作世界模型的 4D 一致性监督，开辟了“用几何约束训练时序生成模型”的路线，且在 NAVSIM 基准上取得 SOTA。自动驾驶世界模型方向的必读。


#### 可能的研究机会

- **“时空-语义-因果”三维一体的场景图构建**：CausalSplat 做因果推理、LEGO 做语义层级、PBD-AG 做持久场景变化——三者在不同抽象层次上各自建立场景图。将它们统一为一个能够同时编码时空演化、语义层级和因果关系的综合场景图，是一个明显但尚未被占领的交叉点。

- **物理引擎与神经场景表示的深度融合**：WildFireGS 展示了高斯原语可以原生承载粒子燃烧模型。将其推广到其他物理过程（流体、形变、碰撞）并与具身决策联动，可能催生“物理-感知联合数字孪生”新方向。

- **前馈/稀疏视角重建的效率优化新国界**：Compact Feed-Forward 3D Gaussians 将原语压缩至 1/20，TRACE-GS 解决了训练-推理分布不匹配。将两者结合——即在压缩表示上训练在线策略蒸馏——可能产出极高效且鲁棒的稀疏视角重建系统。

- **测试时自适应的轻量化部署**：Self-Geometry 提出无需真值的测试时几何自适应（LoRA + 显式约束），SLIM 则展示了 0.5B 参数的紧凑 VLA 策略。将 Self-Geometry 的测试时自适应能力与 SLIM 的轻量架构结合，可实现“低成本 + 动态环境适应”的机器人视觉策略。

- **极端输入条件下的语义-几何协同**：CasDeblurGS 在“两张模糊图”下重建，TRACE-GS 在稀疏视角下修复，而 LEGO/CausalSplat 需要较完整的输入进行语义层级构建。如何将语义先验融入极端退化输入的重建过程（用语义知识补偿几何缺失），是一个值得探索的空白。


#### 风险和不确定性

- **性能声明

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-12T09:43:56-04:00
**Total number of papers:** 52
**Number of papers added in the latest update:** 18
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

#### 2026-08-11 - Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically Consistent 3D Vision Foundation Models

**Authors:** Seokhyun Youn, Dahyeon Kye, Sung-Ho Bae, Jihyong Oh
**Links:** [abs](https://arxiv.org/abs/2608.10708) - [pdf](https://arxiv.org/pdf/2608.10708)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, pointmap, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically Consistent 3D Vision Foundation Models
- 作者：Seokhyun Youn, Dahyeon Kye, Sung-Ho Bae, Jihyong Oh
- 出版日期：2026-08-11
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2608.10708

### 一句话总结
本文提出一种无需真值、即插即用的测试时自适应方法Self-Geometry，通过显式多视图几何约束直接提升三维视觉基础模型的位姿与几何估计一致性。

### 研究问题
现有三维视觉基础模型（VFMs）在单次前向传播中预测深度、相机位姿和点图，虽泛化能力强，但因训练时未施加显式多视图几何一致性约束（如光束平差法计算成本过高），导致推理时存在几何不一致。如何在不依赖真值的前提下，通过测试时自适应提升模型的几何一致性？

### 核心思路/方法
- 核心思想：与先前工作利用模型输出的隐式自一致性（如点图、特征）不同，本文直接用2D像素对应关系作为伪真值，显式引入多视图几何约束。
- **几何解耦优化（Geometric Disentanglement Optimization）**：联合多视图一致性损失与对极一致性损失，并引入梯度解耦以阻止梯度冲突。
- **帧角邻居（Frame Angular-Neighbor）**：基于SO(3)测地距离的视图采样器，以轻量方式施加上述约束。
- **轻量测试时自适应（Lightweight TTA）**：通过LoRA适配基础模型。

### 主要贡献
- 提出首个直接施加显式多视图几何约束的测试时自适应方法，而非依赖隐式一致性信号。
- 设计几何解耦优化策略，避免多视图与对极一致性损失之间的梯度冲突。
- 提出基于SO(3)测地距离的视图采样方法，实现轻量约束施加。
- 在6种VFMs（VGGT、π³、DA3-Giant/Large/Base/Small）和4个基准（7Scenes、ETH3D、ScanNet++、HiRoom）上，位姿和几何估计均取得一致提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作聚焦于3D视觉基础模型的关键痛点——几何不一致性，提出无需真值、即插即用的测试时自适应方案，且验证模型和基准覆盖面广（6种VFMs、4个基准），对三维视觉与基础模型研究均有较强参考价值。方法设计层面（梯度解耦、SO(3)视图采样）也有一定创新性。

</details>

<details>
<summary>Abstract</summary>

Recent Vision Foundation Models (VFMs) predict depth, camera pose, and pointmap in a single forward pass without per-scene optimization, achieving strong generalization. However, enforcing explicit multi-view geometric consistency, e.g., through bundle adjustment, is computationally costly and is thus not imposed during VFM pretraining, so such inconsistency can arise. To address this, implicit self-consistency derived from model outputs (e.g., pointmaps, features), though enforced at test-time in prior work, delivers inherently limited performance gain, especially on scenes where the pretrained VFM is highly inaccurate. In contrast to this implicit signal, we propose Self-Geometry, a plug-and-play test-time adaptation pipeline that directly imposes explicit multi-view geometric constraints using 2D pixel correspondences as pseudo ground-truth. Our proposed Self-Geometry consists of Geometric Disentanglement Optimization, which combines Multi-View Consistency and Epipolar Consistency losses with Gradient Disentanglement to prevent gradient conflict; Frame Angular-Neighbor, a view sampler based on SO(3) geodesic distances for lightly imposing these constraints; and Lightweight TTA, which adapts VFMs via LoRA. Our method achieves consistent improvements in both pose and geometry estimation across six VFMs (VGGT, $π^3$, DA3-Giant/Large/Base/Small) and four benchmarks (7Scenes, ETH3D, ScanNet++, HiRoom).

</details>

#### 2026-08-11 - Visual Geometry Foundation-Aware Gaussians for Single-Frame Surround-View Driving Reconstruction

**Authors:** Junhong Lin, Jinlong Wang, Xianda Guo, Yanlun Peng, Wei Zheng, Guoqing Liu, Hanli Wang, Tiesong Zhao, Wei Gao
**Links:** [abs](https://arxiv.org/abs/2608.10682) - [pdf](https://arxiv.org/pdf/2608.10682)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visual Geometry Foundation-Aware Gaussians for Single-Frame Surround-View Driving Reconstruction
- 作者：Junhong Lin, Jinlong Wang, Xianda Guo, Yanlun Peng, Wei Zheng, Guoqing Liu, Hanli Wang, Tiesong Zhao, Wei Gao
- 出版日期：2026-08-11T09:04:33Z
- 分类：Geometry Foundation Models（主分类）；Neural Scene Representations & Rendering（次分类）
- 链接：https://arxiv.org/abs/2608.10682

### 一句话总结
本文提出VGGD框架，利用预训练视觉几何基础模型的先验知识，增强单帧环视驾驶场景重建中的几何稳定性和渲染质量。

### 研究问题
单帧环视重建因相机间重叠区域极小，面临严重的几何不稳定和渲染伪影问题；现有方法依赖复杂解码器或辅助线索，但受限于上游特征几何能力不足。

### 核心思路/方法
- 核心主张：利用预训练视觉几何先验增强上游表征，缓解稀疏环视视角下的几何歧义。
- 具体流程：
  1. 使用VGGT生成可迁移的多视角几何先验token；
  2. 引入双路径颈部结构，解耦几何一致表征与外观相关表征，改善弱观测区域的外观补全；
  3. 应用尺度预热策略，稳定早期几何学习并抑制自我姿态变化下的尺度漂移；
  4. 使用混合像素-体素高斯解码器，生成可渲染的3D高斯场景用于新视角合成。

### 主要贡献
- 提出VGGD框架，将几何建模前移至前端，并适配基础模型先验到驾驶相机设置；
- 引入双路径颈部以解耦几何与外观表征；
- 提出尺度预热策略提升训练稳定性；
- 在nuScenes单帧基准上取得最佳整体渲染质量，并改善了相对几何一致性。

### 局限性
摘要未提供足够信息，未提及明确的局限性、失败案例或性能边界分析。

### 阅读优先级
**高**。理由：该工作面向单帧环视驾驶重建这一实际应用场景，结合了视觉几何基础模型与3D高斯泼溅这一当前热门技术路线，并在公开基准（nuScenes）上报告了领先效果；对从事自动驾驶场景重建、新视角合成或多视角几何建模的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-frame surround-view reconstruction faces severe geometric instability and rendering artifacts due to minimal inter-camera overlap. While existing methods rely on complex decoders or auxiliary cues, they remain bottlenecked by the weak geometric capacity of upstream features. We argue that leveraging pretrained visual geometry priors strengthens upstream representations and alleviates the geometric ambiguity in sparse surround views. To this end, we propose VGGD, a visual geometry foundation-aware 3D Gaussian Splatting framework for feed-forward surround-view driving reconstruction, which shifts geometric modeling to the frontend and adapts foundation priors to the driving camera setting. First, VGGD leverages VGGT to provide transferable multi-view geometric prior tokens. Next, we introduce a Dual-Path Neck to decouple geometry-consistent and appearance-aware representations, improving appearance completion in weakly observed regions. We further apply Scale Warmup to stabilize early geometry learning and suppress scale drift under ego-pose changes. Finally, we use a hybrid pixel--volume Gaussian decoder to produce a renderable 3D Gaussian scene for novel-view synthesis. Experiments on the nuScenes single-frame benchmark show that VGGD achieves the best overall rendering quality among the compared methods and improves relative geometric consistency.

</details>

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

#### 2026-08-11 - Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives

**Authors:** Songlin Du, Xiaoyong Lu, Zeyu Wu, Xiaobo Lu, Guobao Xiao, Bin Fan, Jiayi Ma, Takeshi Ikenaga
**Links:** [abs](https://arxiv.org/abs/2608.11093) - [pdf](https://arxiv.org/pdf/2608.11093)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives（跨视角特征匹配：综述、基准测试与基础模型视角）
- 作者：Songlin Du, Xiaoyong Lu, Zeyu Wu, Xiaobo Lu, Guobao Xiao, Bin Fan, Jiayi Ma, Takeshi Ikenaga
- 出版日期：2026-08-11
- 分类：3D重建与多视角几何
- 链接：https://arxiv.org/abs/2608.11093

### 一句话总结
本文是对跨视角特征匹配领域的系统性综述，构建了统一分类体系并对代表性方法进行了同协议基准测试，着重分析了视觉基础模型对该领域的影响与未来方向。

### 研究问题
跨视角特征匹配领域存在以下核心问题：问题定义、模型架构、训练范式和评估协议高度分散，缺乏统一理解框架；该领域正从任务特化模型向统一化、可泛化对应模型演进，但演进脉络尚不清晰；视觉基础模型（VFMs）的出现带来了新机遇，但缺乏系统分析。

### 核心思路/方法
- 提出一个结构化分类体系（taxonomy），涵盖五个维度：特征提取、单类型特征匹配器、多类型特征匹配器、基于视觉基础模型（VFM）的方法、训练策略与鲁棒估计。
- 梳理近年进展，提炼关键设计原则，重点阐明领域向统一化和可泛化对应模型转变的趋势。
- 在统一评估协议下，对代表性最先进方法进行实验基准测试，实现公平全面的性能对比。

### 主要贡献
1. 提出了一个统一的跨视角特征匹配分类体系，为领域内方法提供结构化分析与比较框架。
2. 系统梳理了该领域十年来的演进历程，总结了从任务特化到统一可泛化模型转变的关键设计原则。
3. 在一致协议下提供了多方法基准测试结果，实现公平的性能对比。
4. 讨论了开放挑战与未来方向，包括效率、极端条件下的鲁棒性以及跨域泛化问题。

### 局限性
摘要未提供具体实验设置、数据集规模、性能数值等细节，也未提及综述纳入的论文数量范围。关于基准测试的具体结果、局限性和失败案例，摘要未提供足够信息。

### 阅读优先级
**高**。理由如下：
1. 本文具备综述+基准测试双重属性，是获取领域全景和横向对比的关键资源。
2. 作者团队来自多所机构（如东南大学、武汉大学、早稻田大学等），且该方向处于视觉基础模型与几何匹配的交叉热点，引用概率高。
3. 统一分类体系对后续做系统定位和实验对照有直接参考价值。若读者只需单一算法细节，可跳读对应章节。

</details>

<details>
<summary>Abstract</summary>

Cross-view feature matching aims to establish reliable correspondences across images with large viewpoint variations. Over the past decade, the field has evolved from task-specific models toward increasingly unified and generalizable correspondence models, with recent progress further driven by the emergence of vision foundation models (VFMs). Despite these advances, existing studies remain highly diverse in their problem formulations, model architectures, training paradigms, and evaluation protocols, making it difficult to obtain a unified understanding of the field. In this survey, we present a unified review of cross-view feature matching. We first introduce a structured taxonomy covering feature extraction, single-type feature matcher, multi-type feature matcher, VFMs based methods, training strategy and robust estimation, providing a coherent framework for analysis and comparison. We further examine recent advances, distilling key design principles and highlighting the shift toward unified and generalizable correspondence models. We also provide a unified experimental benchmarking of representative state-of-the-art methods under consistent protocols, enabling fair and comprehensive performance comparisons. In addition, we discuss open challenges and future directions, including efficiency, robustness under extreme conditions, and cross-domain generalization. This survey aims to provide a comprehensive and structured reference for understanding the evolution, current landscape, and future development of cross-view feature matching in the era of vision foundation models.

</details>

#### 2026-08-11 - GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting

**Authors:** Huaiyuan Weng, Chul Min Yeum, Su-Min Kang
**Links:** [abs](https://arxiv.org/abs/2608.10938) - [pdf](https://arxiv.org/pdf/2608.10938)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, rendering, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting
- 作者：Huaiyuan Weng, Chul Min Yeum, Su-Min Kang
- 出版日期：2026-08-11T14:06:51Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10938

### 一句话总结
GS-CPE 提出一种基于 3D 高斯泼溅的粗到细框架，将几何粗姿态估计与 3DGS 重渲染优化结合，实现统一且高精度的 6 自由度相机姿态估计。

### 研究问题
如何在保持鲁棒泛化能力的同时，提高视觉定位中 6 自由度相机姿态估计的精度，解决传统方法在准确性和泛化性之间难以兼顾的问题。

### 核心思路/方法
- 采用粗到细（coarse-to-fine）的两阶段框架。
- 粗阶段：通过检索引导（retrieval-guided）的几何姿态估计，在 3D 高斯泼溅（3DGS）场景表示上获得初始粗略姿态。
- 细阶段：通过最小化一个可见性感知的掩码 RGB 重投影（warping）目标函数，在多尺度优化框架中进行姿态细化，并引入自适应重渲染（adaptive re-rendering）机制。

### 主要贡献
- 提出 GS-CPE，一个统一了基于几何的粗姿态估计与基于 3DGS 重投影的细姿态优化的 6-DoF 姿态估计框架。
- 引入可见性感知的掩码 RGB 重投影目标函数及多尺度优化策略，配合自适应重渲染进行精细化。
- 在多个室内外基准（7Scenes、Cambridge Landmarks、FAST-LIVO2）及自建数据集上取得领先的准确性与泛化性能。

### 局限性
摘要未提供足够信息，无法判断具体局限性（如计算开销、对动态场景的适应性、对初始姿态的敏感度等）。

### 阅读优先级
**高**。理由：该工作提出了一种结合 3DGS 的粗到细姿态估计统一框架，涉及新颖的可见性感知优化目标，且在多个基准上报告了先进的准确性与泛化能力。研究主题面向视觉定位与神经场景表示的前沿交叉，对相关领域研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Despite substantial progress in visual localization, from scene coordinate regression to direct camera pose regression, achieving both robust generalization and high accuracy remain challenging. This study introduces GS-CPE (Gaussian Splatting based Camera Pose Estimation), a coarse-to-fine framework for 6-DoF camera pose estimation that unifies geometry-based coarse pose estimation with robust 3D Gaussian Splatting (3DGS) warping based pose refinement. GS-CPE first estimates a coarse pose via retrieval-guided geometric pose estimation on a 3DGS scene representation, then refines it by minimizing a visibility aware masked RGB warping objective in a multi-scale optimization framework, with adaptive re-rendering. Extensive experiments on indoor and outdoor benchmarks including 7Scenes, Cambridge Landmarks, FAST-LIVO2 datasets, and a custom dataset demonstrate state-of-the-art performance, consistently outperforming in both accuracy and generalization.

</details>

#### 2026-08-11 - Gaussian Sculpting: End-to-End Controllable Surface Reconstruction via Field Optimization

**Authors:** Ke Jiaxin, Juncheng Liu, Yi Wang, Zhouhui Lian, Bin Liu, Shengfa Wang, Xiangjia He
**Links:** [abs](https://arxiv.org/abs/2608.10602) - [pdf](https://arxiv.org/pdf/2608.10602)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Sculpting: End-to-End Controllable Surface Reconstruction via Field Optimization
- 作者：Ke Jiaxin, Juncheng Liu, Yi Wang, Zhouhui Lian, Bin Liu, Shengfa Wang, Xiangjia He
- 出版日期：2026-08-11T07:42:24Z
- 分类：3D Reconstruction & Multi-view Geometry（次要：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.10602

### 一句话总结
本文提出 Gaussian Sculpting，一种将3D高斯原语锚定在可微表面上、通过双层训练策略联合优化有符号距离场（SDF）与高斯参数，以实现端到端可控高质量表面重建的框架。

### 研究问题
3D高斯溅射（3DGS）在有限视角下难以恢复准确表面，且高斯原语的不规则性导致几何误差难以手动修正。如何实现高质量、可控且端到端的表面重建是该文要解决的核心问题。

### 核心思路/方法
- 将高斯原语锚定在一个演化的可微表面上，使它们引导SDF优化，而非仅在后期处理中提取表面。
- 设计双层训练策略：外层循环优化SDF表示的几何，内层循环固定几何并更新高斯参数，以实现稳定梯度隔离。
- 对高斯参数施加约束，确保其与底层表面的一致性，提升几何与外观保真度。
- 引入基于八叉树类划分的多分辨率细分方案，保留细节同时降低内存消耗。

### 主要贡献
- 提出完全可微的端到端框架Gaussian Sculpting，用于高质量表面重建。
- 设计双层训练策略实现几何与高斯的联合优化与梯度隔离。
- 通过对高斯参数的约束增强几何-外观一致性。
- 提出多分辨率细分方案，兼顾细节保留与内存效率。
- 在物体级场景实验中有效去除冗余表面、恢复有限视角下缺失结构，并在较低分辨率下仍实现良好重建质量。

### 局限性
摘要未提供足够信息。摘要未提及方法的失败案例、对大规模场景的适应性、训练/推理时间成本、与已有方法的定量对比细节，以及多分辨率方案在极端复杂几何下的表现等潜在局限。

### 阅读优先级
**高**。理由：该方法针对3DGS在表面重建中的核心痛点（有限视角、几何误差、手动修正困难）提出了端到端可微框架和双层优化策略，思路明确且有物体级实验支撑，对从事三维重建、神经渲染和几何优化方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has recently enabled real-time novel view synthesis with impressive quality. However, it struggles to recover accurate surfaces under limited viewpoints and due to the inherent irregularity of Gaussian primitives. The resulting geometric errors are notoriously difficult to correct manually. To address these issues, we propose Gaussian Sculpting, a fully differentiable end-to-end framework for high-quality surface reconstruction. Our key insight is to anchor Gaussians onto an evolving differentiable surface, allowing them to guide signed distance field (SDF) optimization instead of extracting the surface only during post-processing. To enable stable gradient isolation during joint optimization, we design a bi-level training strategy in which the outer loop optimizes the geometry represented by the SDF, while the inner loop updates the Gaussians with the geometry fixed. We further impose constraints on Gaussian parameters to ensure consistency with the underlying surface, thereby improving both geometric and appearance fidelity during optimization. In addition, we introduce a multi-resolution subdivision scheme based on octree-like partitioning to preserve fine details while reducing memory consumption. Experiments on object-level scenes demonstrate that our method effectively removes redundant surfaces, recovers missing structures caused by limited viewpoints, and achieves strong reconstruction quality even at relatively low resolutions.

</details>

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

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-11 - CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting

**Authors:** Jiayu Ding, Meilu Song, Yun Chen, Wei Gao, Ge Li
**Links:** [abs](https://arxiv.org/abs/2608.11150) - [pdf](https://arxiv.org/pdf/2608.11150)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting
- 作者：Jiayu Ding, Meilu Song, Yun Chen, Wei Gao, Ge Li
- 出版日期：2026-08-11T17:09:49Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.11150

### 一句话总结
本文提出CausalSplat框架，将视觉语言模型与3D场景图结合，以解决3D高斯泼溅在隐含意图、空间约束和常识推理等层次化推理任务上的不足。

### 研究问题
现有3D高斯泼溅（3DGS）开放词汇场景理解方法仅支持显式查询，难以处理实际具身交互中所需的隐含意图、复杂空间约束和常识推理（如因果、空间、功能与反事实推理）。本文定义并研究"推理式3D高斯分割"这一新任务。

### 核心思路/方法
- 构建两个基准：**Causal-LERF**和**Causal-ScanNet**，系统评估常识、空间、功能和反事实推理能力。
- 提出**CausalSplat**框架：将**视觉语言模型**与**3D场景图**集成，将显式结构感知与隐式逻辑推理解耦，以分层方式完成推理式分割。

### 主要贡献
1. 首次定义并引入"推理式3D高斯分割"任务。
2. 构建两个推理基准（Causal-LERF、Causal-ScanNet），覆盖四类推理能力。
3. 提出CausalSplat框架，结合视觉语言模型与3D场景图实现解耦推理。
4. 实验表明CausalSplat在推理基准上达到最优性能，并在标准指代与开放词汇3D分割任务上表现出强泛化性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作定义了3D场景理解领域的新任务（推理式分割），并同时提供基准与新型框架，对具身智能和开放词汇3D理解研究方向具有直接参考价值；且实验覆盖推理基准与标准任务，验证了方法的有效性与泛化性，属于方法+数据集双重贡献的综合性工作。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting (3DGS) has advanced open vocabulary scene understanding, existing methods remain confined to explicit queries. They struggle to interpret implicit intents, complex spatial constraints, and commonsense reasoning required for practical embodied interactions. To address this gap, we introduce the task of reasoning 3D Gaussian segmentation and construct two benchmarks, Causal-LERF and Causal-ScanNet. These benchmarks systematically evaluate commonsense, spatial, affordance, and counterfactual reasoning. Evaluations reveal that current state of the art methods perform poorly on these reasoning challenges. Therefore, we propose CausalSplat, a framework that integrates vision-language models with 3D scene graphs to disentangle explicit structural perception from implicit logical inference. Extensive experiments demonstrate that CausalSplat achieves state of the art performance on our reasoning benchmarks while showing strong generalizability on standard referring and open vocabulary 3D segmentation tasks. Project Page: https://jiayuding031020.github.io/CausalSplat

</details>

#### 2026-08-11 - WildFireGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes

**Authors:** Nienke Driessen, Joris Rijsdijk, Sören Pirk, Wojtek Palubicki, Dominik L. Michels, Michael Weinmann
**Links:** [abs](https://arxiv.org/abs/2608.11100) - [pdf](https://arxiv.org/pdf/2608.11100)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WildFireGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes
- 作者：Nienke Driessen, Joris Rijsdijk, Sören Pirk, Wojtek Palubicki, Dominik L. Michels, Michael Weinmann
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.11100

### 一句话总结
本文提出 WildFireGS，一种直接在语义增强的大规模 3D 高斯泼溅森林重建场景上运行的基于物理的野火模拟框架，无需显式网格或体素转换即可模拟点火、传热、燃烧和火焰传播。

### 研究问题
现有基于物理的野火模型虽然逼真度高，但主要局限于具有完整理想化森林结构知识的合成环境，难以直接应用于由航空影像重建的真实世界场景。本文旨在弥合学习式场景重建与环境模拟之间的鸿沟，实现基于观测数据的真实世界野火数字孪生。

### 核心思路/方法
- 在 3D 高斯泼溅森林重建中，为高斯原语附加语义和材料属性，以编码植被类型和燃料特征。
- 引入一种基于粒子的燃烧模型，原生运行在高斯表示上，无需转换为显式网格或体素网格，即可模拟点火、传热、燃烧及火焰在复杂森林结构中的传播。
- 通过基于能量汇过程的降雨驱动冷却机制展示框架的模块化，用于模拟火势遏制。

### 主要贡献
- 提出 WildFireGS，一种直接在大规模、语义增强的 3D 高斯泼溅森林重建上运行的基于物理的野火模拟框架。
- 通过粒子燃烧模型实现高斯表示上的原生火灾行为模拟，避免网格/体素转换。
- 在合成场景和真实航空森林采集数据上验证，显示物理一致的野火行为，包括随植被密度、风速和地形坡度变化的传播特性。
- 通过新型防火隔离带实验和生物质损失估计进行模型验证。

### 局限性
摘要未提供足够信息（未明确讨论方法的计算开销、对场景重建质量的依赖程度、实时性能或特定失效模式等局限性）。

### 阅读优先级
**高**  
理由：该工作将最新的 3D 高斯泼溅场景表示与物理模拟结合，直接面向真实世界野火数字孪生，跨越了神经渲染与物理仿真两个热点领域；且摘要展示了完整的模拟管线与多场景验证，方法新颖性强、应用潜力大，对从事场景表示、物理仿真或环境应用的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Climate-driven environmental change is driving an increase in both the frequency and severity of wildfire events, making accurate simulation and prediction critical for effective risk mitigation and landscape management. While recent physics-based wildfire models achieve high realism by explicitly simulating combustion, heat transfer, and fuel dynamics, they remain largely restricted to synthetic environments with complete and idealized knowledge of forest structure, limiting their applicability to real-world environments captured via aerial imagery. To provide a pathway toward real-world wildfire digital twins derived directly from observational data, we present WildFireGS, a physics-based wildfire simulation framework operating directly on large-scale, semantics-enriched 3D Gaussian Splatting forest reconstructions. Our approach bridges learning-based scene reconstruction and environmental simulation by augmenting Gaussian primitives with semantics and material properties that encode vegetation type and fuel characteristics. We introduce a particle-based combustion model that operates natively on Gaussian representations, simulating ignition, heat transfer, combustion, and flame propagation across complex forest structures. This enables direct physics-based simulation of fire behavior on reconstructed real-world environments, without requiring conversion to explicit meshes or volumetric grids. We demonstrate the modularity of WildFireGS through a rain-driven cooling mechanism in terms of an energy-sink process to realistically model fire containment. Evaluations on synthetic scenes and real aerial forest captures show physically consistent wildfire behavior, reproducing characteristic dynamics including propagation scaling with vegetation density, wind velocity, and terrain slope. In addition, we validate our model through novel firebreak experiments and biomass loss estimation.

</details>

#### 2026-08-11 - Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting

**Authors:** Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji
**Links:** [abs](https://arxiv.org/abs/2608.10756) - [pdf](https://arxiv.org/pdf/2608.10756)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting
- 作者：Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji
- 出版日期：2026-08-11T10:16:30Z
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.10756

### 一句话总结
本文提出一种基于语义3D高斯泼溅的具身多模态对齐框架，通过显式可刷新的3D语义接地提升开放词汇移动操作在杂乱、遮挡与视角变化下的鲁棒性。

### 研究问题
如何让具身移动操作机器人将语言指令、视觉观察、三维场景结构与动作可行性在执行前有效对齐，从而在本地家庭工作空间中实现开放词汇目标接地与少样本操作。

### 核心思路/方法
- 构建任务驱动的局部语义3D高斯泼溅（Semantic-3DGS）作为共享接口，统一主动多视角感知、语言条件3D定位、障碍感知场景推理、基座准备与动作模型语义条件化。
- 引入可达性感知的基座定位，确保操作姿态可行。
- 采用扩散式视觉-语言-动作（VLA）策略，并将3D语义线索仅注入动作专家网络的后期模块，以保留预训练动作先验。

### 主要贡献
- 提出一个将Semantic-3DGS作为多阶段共享表示的具身多模态接地框架，覆盖从主动感知到动作生成的完整链路。
- 通过仅在动作模型后期注入语义，避免破坏预训练动作先验。
- 在50次真实机器人试验中，长时程任务成功率60%，优于PointVLA（40%）与DexVLA（28%）；高杂乱操作成功率74%，优于单视角变体（52%）与PointVLA（46%）。
- 在75厘米高度偏移下保持75%成功率，并消除了照片引起的错误抓取。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法涉及具身智能、语义3D场景表示与VLA策略的交叉，且提供了真实机器人上的多维度对比实验（成功率、杂乱场景、高度偏移、误抓消除），对从事机器人操作与神经场景表示研究的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Embodied mobile manipulation requires language, visual observations, three-dimensional scene structure, and action feasibility to be aligned before execution. We study open-vocabulary target grounding with few-shot manipulation in local household workspaces and present an embodied multimodal grounding framework that integrates active multi-view Semantic 3D Gaussian Splatting (Semantic-3DGS), reachability-aware base positioning, and a diffusion-based vision-language-action policy. A task-driven local Semantic-3DGS serves as a shared interface across active sensing, language-conditioned 3D localization, obstacle-aware scene reasoning, base preparation, and semantic conditioning of the action model. To preserve pretrained action priors, the 3D semantic cues are injected only into the late action-expert blocks. In expanded 50-trial real-robot evaluations against representative vision-language-action (VLA) approaches, the full system achieves 60% long-horizon success compared with 40% for PointVLA and 28% for DexVLA, and reaches 74% success in heavily cluttered manipulation compared with 52% for the single-view variant and 46% for PointVLA. It also maintains 75% success under a 75 cm height shift and eliminates photo-induced false grasps. These results indicate that explicit, refreshable 3D semantic grounding can improve robustness under clutter, occlusion, viewpoint variation, and embodiment constraints.

</details>

#### 2026-08-11 - Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging

**Authors:** Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss
**Links:** [abs](https://arxiv.org/abs/2608.10712) - [pdf](https://arxiv.org/pdf/2608.10712)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging
- 作者：Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10712

### 一句话总结
本文提出一种基于显著性引导的原始高斯合并流水线，将逐像素的高斯原语压缩为紧凑的内容自适应表示，在保留视觉质量的同时将高斯数量减少至约1/20。

### 研究问题
如何将前馈式3D高斯泼溅方法生成的冗余逐像素原语，转化为更紧凑且高效的表示，同时保持渲染质量。

### 核心思路/方法
- 采用结构感知的合并流水线，通过自适应超像素分割对空间连续、外观相似的高斯进行聚类，聚类粒度由显著性图引导——纹理区域细分，均匀区域粗分。
- 每个聚类通过学习的编码器压缩为紧凑的潜在表示。
- 在不同视图之间基于几何重叠和特征相似性，通过学习的合并器匹配并整合表示。
- 使用细节层次（level-of-detail）解码器以可控分辨率生成最终高斯，支持推理时的质量-效率灵活权衡。
- 作为后处理模块，该方法与骨干网络无关，可兼容任意前馈方法。

### 主要贡献
- 提出一种骨干无关的显著性引导高斯合并流水线，可将前馈方法输出的逐像素高斯压缩至约1/20数量。
- 通过自适应超像素分割和显著性引导，实现内容自适应的紧凑表示。
- 通过可学习的编码器、合并器和细节层次解码器，支持可控分辨率的灵活质量-效率权衡。
- 与已有减少原语数量的方法相比，在更紧凑表示下实现了更好且更稳健的视觉质量。

### 局限性
摘要未提供足够信息。摘要未涉及方法在特定场景下的失败案例、计算开销、内存占用、对不同输入视图数量的鲁棒性边界、以及与其他方法的定量对比实验细节。

### 阅读优先级
**中**。理由：该工作针对3D高斯泼溅表示冗余的问题提出了一种通用后处理压缩方案，对关注神经场景表示和渲染效率的研究者具有参考价值。但摘要未给出关键定量结果和实验对比细节，且方法链路较复杂（编码器、合并器、解码器均需学习），在未看到实验验证前其实际效果和适用性需要进一步评估。

</details>

<details>
<summary>Abstract</summary>

3D scene reconstruction, modeling, and rendering are highly relevant for numerous tasks, and 3D Gaussian splatting has become a standard choice in this context. Its feed-forward variants provide fast reconstruction from sparse input views but often produce per-pixel primitives, leading to highly redundant and thus inefficient representations. We present a structure-aware merging pipeline that takes per-pixel primitives from any feed-forward method and consolidates them into a compact, content-adaptive Gaussian set while largely retaining visual quality at just $\frac{1}{20}^\text{th}$ of the Gaussians of a per-pixel method. We group spatially coherent Gaussians of similar appearance into variable-size clusters via adaptive superpixel segmentation guided by a saliency map, which allocates fine segments to textured regions and coarse segments to homogeneous areas. We compress each cluster into a compact latent representation through a learned encoder, then match and consolidate representations across views based on geometric overlap and feature similarity via a learned merger. A level-of-detail decoder then produces the final Gaussians at a controllable resolution, enabling a flexible quality-efficiency trade-off at inference. As a post-processing module, the pipeline is backbone-agnostic, leveraging the strengths of existing feed-forward methods. This leads to better and more robust quality than achieved by previous approaches that target a reduction in primitive count, while providing a highly compact representation, that can be rendered efficiently.

</details>

#### 2026-08-11 - Amulet: Frame Extrapolation Through Sparse Layered Scene Representation and Adaptive Shading

**Authors:** Sebastian Künzel, Fabian Schmierer, Sergej Geringer, Guido Reina, Daniel Weiskopf, Dieter Schmalstieg
**Links:** [abs](https://arxiv.org/abs/2608.10423) - [pdf](https://arxiv.org/pdf/2608.10423)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Amulet: Frame Extrapolation Through Sparse Layered Scene Representation and Adaptive Shading
- 作者：Sebastian Künzel, Fabian Schmierer, Sergej Geringer, Guido Reina, Daniel Weiskopf, Dieter Schmalstieg
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10423

### 一句话总结
Amulet 提出了一种基于稀疏分层图像空间缓存的自适应着色方法，通过将低频着色率外推至高刷新率显示，实现无神经网络的精确多帧外推渲染。

### 研究问题
如何在不依赖神经网络或重投影的前提下，以显式且非幻觉的方式实现高频帧外推，尤其是在处理新出现遮挡区域和动态场景时保持高质量渲染。

### 核心思路/方法
- 将场景转换为稀疏、分块、分层的中间表示（缓存），并显式光栅化潜在可见几何体。
- 缓存以预测方式提前填充未来视图的着色信息，并在多帧之间摊销成本。
- 新视图合成通过从前到后层级遍历缓存完成，对过期或缺失的着色进行实时细化。
- 使用基于梯度的预测调度器为每个分块分配生命周期，实现运动与动态光照下的自适应着色更新。
- 将光栅化与着色频率从显示刷新率中解耦，从而允许单个着色帧支撑多个外推帧。

### 主要贡献
- 提出一种稀疏分层图像空间缓存，支持预测式填充分层场景表示，用于高频帧外推。
- 设计了自适应的梯度驱动调度器，以控制分块生命周期和着色更新。
- 实现了显式处理新遮挡区域的非神经多帧外推，避免幻觉。
- 在4K分辨率下可达250 Hz，在多项指标上与DLSS和神经流方法等现有帧生成技术竞争。

### 局限性
摘要未提供足够信息。摘要未提及方法在极端动态场景、复杂光照或性能退化条件下的具体局限，也未给出与对比方法的详细定量失败案例或资源开销分析。

### 阅读优先级
**高**。理由：该工作针对帧生成与外推这一热点方向提出了非神经的显式表示方案，具备高刷新率（250 Hz @4K）和与DLSS等工业级方法竞争的能力，方法和贡献描述清晰，适合渲染与帧生成领域研究者阅读。

</details>

<details>
<summary>Abstract</summary>

We introduce Amulet, a rendering method that transforms a scene into a sparse, tiled and layered intermediate scene representation (cache) for high-frequency frame extrapolation. In contrast to reprojection-based techniques, Amulet explicitly rasterizes and stores potentially visible geometry in its layered image-space cache, allowing accurate shading and inpainting of newly disoccluded regions without hallucination. Our key contribution is a cache that is predictively filled with shading information for future views, amortized over multiple current frames. Novel views are synthesized by hierarchically traversing the cache front to back and refining stale or missing shading on the fly. Using a predictive, gradient-based scheduler that assigns lifetimes for each tile, we enable adaptive shading updates under motion and dynamic lighting. Amulet decouples the rasterization and shading rate from the refresh rate of the display. In many scenarios, our cache can use a single shaded frame to synthesize multiple extrapolated frames with only a few localized updates. In a typical application, we extrapolate a 60 Hz shading rate to a 240 Hz display. Amulet achieves up to 250 Hz at 4K resolution and is competitive with state-of-the-art frame generation methods, including DLSS and neural-flow approaches, in multiple metrics. Amulet explores the design space of sparse layered image-space representation. It enables accurate, non-neural multi frame extrapolation with explicit handling of disocclusions. Our findings show that Amulet can extrapolate many more frames than contemporary methods with high quality, rivaling latency-bound frame interpolation methods with similar quality in many scenes.

</details>

#### 2026-08-11 - CasDeblurGS: Cascaded 2D-to-3D Multi-View Consistency for 3D Gaussian Splatting from Two Blurry Images

**Authors:** Haeyun Choi, Minhyuk Jang, I-Gil Kim
**Links:** [abs](https://arxiv.org/abs/2608.10345) - [pdf](https://arxiv.org/pdf/2608.10345)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, neural rendering, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CasDeblurGS: Cascaded 2D-to-3D Multi-View Consistency for 3D Gaussian Splatting from Two Blurry Images
- 作者：Haeyun Choi, Minhyuk Jang, I-Gil Kim
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10345

### 一句话总结
本文提出一种级联框架，仅从两张已知内参的运动模糊图像中重建连贯的3D场景，通过先建立局部2D对应再聚合为全局3D引导，实现无需位姿和额外辅助的3D高斯泼溅重建与高质量新视角合成。

### 研究问题
在仅有**两张运动模糊图像**、已知相机内参、但**无输入视角位姿、无辅助清晰图像、无逐场景测试时优化**的严格条件下，如何重建连贯的3D场景并进行新视角合成。现有模糊感知神经渲染方法通常依赖多视角冗余、精确相机位姿或昂贵的逐场景优化，难以应对该实际设置。

### 核心思路/方法
提出级联框架 CasDeblurGS，分两阶段由局部到全局逐步恢复可靠的跨视角信息：
- **Stage 1**：通过**遮挡感知的对应关系过滤**构建局部可靠的引导信息。
- **Stage 2**：聚合中间恢复结果，构建**无需位姿的临时3D高斯表示**；该表示的输入视角重渲染结果提供密集的全局引导，用于最终的恢复。
- 最终得到的视角支持更连贯的3D表示与更高质量的新视角合成。

### 主要贡献
- 提出一种新的级联框架，针对仅两张模糊图像、无位姿的极端稀疏视角场景进行3D高斯泼溅重建。
- 设计遮挡感知的对应过滤与临时3D高斯引导机制，实现从局部2D对应到全局3D引导的渐进式信息恢复。
- 在真实世界和合成 Deblur-NeRF 场景上均取得一致性提升，PSNR 分别提高 1.19 dB 和 2.11 dB。
- 通过渐进式消融、跨视角对应可视化和相机重投影分析，验证了渲染质量与多视角几何一致性的改进。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对“仅两张模糊图像、无位姿”这一极具挑战性和实际意义的设置，提出了级联的解决方案，在稀疏视角与模糊退化两个难点上均有创新，且实验结果显著（PSNR提升超过2dB）。对于从事3D重建、神经渲染和图像去模糊交叉方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Free-viewpoint 3D scene media is increasingly important for immersive applications, yet practical capture often suffers from severe view sparsity and motion blur. Although neural rendering has advanced sparse-view synthesis, existing blur-aware methods typically require substantial multi-view redundancy, accurate camera poses, or costly per-scene optimization. We address a stringent yet practical setting: reconstructing a coherent 3D scene from only two motion-blurred images with known intrinsics, without input-view poses, auxiliary sharp images, or per-scene test-time optimization. To this end, we propose CasDeblurGS, a cascaded framework that progressively recovers reliable cross-view information from local 2D correspondences to global 3D guidance. Stage 1 constructs locally reliable guidance through occlusion-aware correspondence filtering, while Stage 2 aggregates the intermediate restorations into a provisional pose-free 3D Gaussian representation whose input-view re-renders provide dense global guidance for final restoration. The resulting views enable a more coherent 3D representation and higher-quality novel-view synthesis. Experiments on real-world and synthetic Deblur-NeRF scenes show consistent gains over strong baselines, improving PSNR by 1.19 dB and 2.11 dB, respectively. Progressive ablations, cross-view correspondence visualization, and camera reprojection analysis further demonstrate improvements in both rendering quality and multi-view geometric consistency.

</details>

#### 2026-08-10 - TRACE-GS: On-Policy Trajectory Distillation with Privileged Geometric Conditioning for Sparse-View 3DGS Restoration

**Authors:** Linlian Jiang, Yuchen Xi, Sadman Rakib Pinon, Ruigang Yang, Yang Wang, Xinxin Zuo
**Links:** [abs](https://arxiv.org/abs/2608.10286) - [pdf](https://arxiv.org/pdf/2608.10286)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRACE-GS: On-Policy Trajectory Distillation with Privileged Geometric Conditioning for Sparse-View 3DGS Restoration
- 作者：Linlian Jiang, Yuchen Xi, Sadman Rakib Pinon, Ruigang Yang, Yang Wang, Xinxin Zuo
- 出版日期：2026-08-10T22:43:06Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.10286

### 一句话总结
TRACE-GS 提出一种利用训练时特权几何信息进行在线轨迹蒸馏的框架，用于稀疏视角 3D 高斯泼溅（3DGS）重建，使扩散先验适应稀疏视角场景并显著提升重建质量与泛化能力。

### 研究问题
现有基于扩散模型的稀疏视角 3DGS 重建方法存在根本性局限：在独立噪声状态下进行的监督无法覆盖推理时实际到达的状态。由于稀疏视角下几何约束不足，去噪过程从一开始就产生偏差，且这些偏差沿轨迹逐步累积，导致重建效果不佳。本文旨在解决这一训练-推理分布不匹配问题。

### 核心思路/方法
TRACE-GS 采用在线策略轨迹蒸馏（on-policy trajectory distillation）策略：
- 在训练阶段，一个以额外训练视角提供的更丰富几何信息为条件的教师模型，为稀疏视角学生模型自身采样轨迹上的每个状态提供监督目标。
- 该方法在每个访问状态上对齐去噪方向与跨视角响应，使训练分布贴合推理分布。
- 该训练时使用的额外几何信息属于学习使用特权信息（LUPI）范式；部署时仅保留稀疏视角学生模型，其修复后的渲染结果作为伪观测用于 3DGS 精化。

### 主要贡献
1. 首次将在线策略监督与特权几何信息相结合，用于稀疏视角 3DGS 重建任务。
2. 提出一种新的训练范式，在训练时利用丰富几何条件引导扩散先验适应稀疏输入，而非设计更复杂的重建网络结构。
3. 在多个数据集和多种稀疏视角设置下取得一致性能提升，并展现出良好的泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对稀疏视角 3DGS 重建这一活跃研究方向的根本性训练-推理分布不匹配问题，提出了概念新颖的在线轨迹蒸馏与特权信息学习框架，且报告了跨数据集和多种稀疏设置的一致提升，对相关领域研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

We present TRACE-GS, an on-policy trajectory distillation framework that leverages privileged geometric conditioning at training time, thereby adapting a diffusion prior to sparse-view 3D Gaussian Splatting (3DGS) restoration. Rather than pursuing increasingly sophisticated restoration architectures, we identify a more fundamental limitation shared by existing diffusion-based approaches: supervision at independently noised states does not cover those reached during inference. In sparse-view 3DGS, under-constrained geometry biases denoising from the outset, and the resulting deviations compound along the rollout. TRACE-GS instead performs on-policy trajectory distillation: a teacher conditioned on richer geometry from additional training views supplies targets along the sparse-view student's own rollout, aligning denoising directions and cross-view responses at each visited state. This training-only geometry places TRACE-GS in the learning using privileged information (LUPI) setting. At deployment, only the sparse-view student is retained, and its restored renderings serve as pseudo-observations for 3DGS refinement. To the best of our knowledge, TRACE-GS is the first to derive on-policy supervision from privileged geometry for sparse-view 3DGS restoration, achieving consistent gains and strong generalization across datasets and sparse-view settings.

</details>

#### 2026-08-10 - LEGO: Leveled Language Gaussian Splatting

**Authors:** Yuning Peng, Haiping Wang, Yuan Liu, Yipeng Lu, Zhen Dong, Bisheng Yang
**Links:** [abs](https://arxiv.org/abs/2608.10057) - [pdf](https://arxiv.org/pdf/2608.10057)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LEGO: Leveled Language Gaussian Splatting
- 作者：Yuning Peng, Haiping Wang, Yuan Liu, Yipeng Lu, Zhen Dong, Bisheng Yang
- 出版日期：2026-08-10
- 分类：Neural Scene Representations & Rendering（神经场景表征与渲染）
- 链接：https://arxiv.org/abs/2608.10057

### 一句话总结
LEGO 通过将多视图 SAM 产生的易变粒度自动重分级为统一的 3D 一致层级，并结合 CLIP 与空间关系构建层级化语言场景图，实现了先进的开放词汇 3D 场景理解与空间推理。

### 研究问题
如何超越基础概念识别，在 3D 场景中捕捉并建模内在的语义层级结构（如“花盆→花束→花蕾→花瓣”），并支持开放词汇的跨视图一致的层级化分割与空间推理。

### 核心思路/方法
- 利用基础模型（如 SAM）可在 2D 中识别多粒度结构，但其划分严格受视角限制、缺乏跨视图一致性。
- LEGO 提出自适应性重新分级机制，将多视图下不稳定的 SAM 粒度统一为 3D 一致的层级结构，为 3D 场景的多层级分割提供精确监督。
- 将各层级分割结果与 CLIP 嵌入对齐，恢复开放词汇的跨层级语义逻辑。
- 通过引入空间关系，将分割结果提升为层级化的语言场景图，使大语言模型能够进行复杂的上下文感知空间推理和精确视觉定位。

### 主要贡献
- 提出 LEGO 框架，实现先进的开放词汇 3D 场景理解，核心创新在于捕获场景内在语义层级。
- 自动将多视图 SAM 粒度重分级为 3D 一致的统一层级，解决跨视图一致性问题。
- 结合 CLIP 与空间关系，构建层级语言场景图，支持大语言模型驱动的空间推理与视觉定位。
- 实验表明，在 promptable 和开放词汇 3D 分割基准上均达到新的最先进性能。

### 局限性
摘要未提供足够信息，例如：方法在复杂/遮挡场景下的鲁棒性、不同规模场景的扩展性、运行时开销、对 SAM/CLIP 基础模型依赖的具体限制等均未提及。

### 阅读优先级
**高**。理由：该论文发表于 2026 年，针对开放词汇 3D 场景理解这一热门方向提出了从 2D SAM 粒度到 3D 层级结构的新颖融合思路，并声称在多个基准上达到 SOTA，且涉及大语言模型的空间推理能力，对神经场景表征与渲染领域的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce LEGO for advanced open-vocabulary scene understanding. Beyond basic concept recognition, its core innovation lies in capturing the intrinsic semantic hierarchies within the scene, such as the "flowerpot -> bouquet -> bud -> petal" lineage. While foundation models like SAM can identify multi-granular structures in 2D, their partitions are strictly perspective-bound and lack cross-view consensus. LEGO self-adaptively re-grades volatile multi-view SAM granularities into a unified, 3D-consistent hierarchy. This provides precise supervision for the structurally coherent, multi-level segmentation of 3D scenes. By grounding these segments with CLIP embeddings, LEGO recovers open-vocabulary semantic logic across hierarchical levels. Furthermore, by incorporating spatial relationships, we elevate these segments into level-wise language scene graphs, effectively empowering Large Language Models to perform complex, context-aware spatial reasoning and precise visual grounding. Experimental results demonstrate that LEGO establishes new state-of-the-art performance across both promptable and open-vocabulary 3D segmentation benchmarks, exhibiting advanced hierarchical scene decomposition and context-aware spatial reasoning.

</details>

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

## Embodied / Robotics / AR Applications

### 2026-08

#### 2026-08-11 - Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models

**Authors:** Kiet T. Nguyen, Hanbo Shim, Jinwoo Kim, Seunghoon Hong
**Links:** [abs](https://arxiv.org/abs/2608.10864) - [pdf](https://arxiv.org/pdf/2608.10864)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models
- 作者：Kiet T. Nguyen, Hanbo Shim, Jinwoo Kim, Seunghoon Hong
- 出版日期：2026-08-11
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.10864

### 一句话总结
本文提出多视角关系蒸馏（MVRD），通过蒸馏跨视角的patch级余弦相似度而非教师特征本身，在保持视觉-语言对齐的同时提升视觉语言模型的空间推理能力。

### 研究问题
视觉语言模型（VLM）的视觉-空间表征在几何上较为脆弱，导致其在具身AI、机器人和自动驾驶所需的空间推理任务中表现不佳。现有方法（如直接在空间问答上微调或融合几何基础视觉模型特征）分别存在伪相关表征或推理时模型规模过大的问题。

### 核心思路/方法
MVRD不直接匹配几何基础教师模型的多视角特征，而是蒸馏跨视角的patch-wise余弦相似度。这些关系编码了几何对应信息，足以支持空间理解，同时对学生表征的约束是欠定的，使其能够保持在预训练的视觉-语言空间附近，从而不破坏原有的视觉-文本对齐。

### 主要贡献
- 提出多视角关系蒸馏（MVRD）方法，用于增强VLM的空间推理能力。
- 在多个代表性VLM上，MVRD优于监督微调和特征蒸馏，性能接近特征融合方法但参数量更少、延迟更低。
- 实验表明MVRD使视觉表征更具几何性，同时保持语言对齐。
- 方法可泛化到3D场景理解任务，包括物体定位、密集描述和问答。

### 局限性
摘要未提供足够信息（未具体说明失败案例、计算资源需求、蒸馏对教师模型依赖程度等局限性）。

### 阅读优先级
**高**

理由：该工作针对VLM空间推理这一关键瓶颈，提出了一种轻量且有效的蒸馏范式，在性能接近高开销特征融合方法的同时大幅降低推理成本，且已展示到3D场景理解的泛化能力。对从事具身AI、机器人、自动驾驶及多模态表征学习的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have achieved strong image and video understanding, yet their visual-spatial representations remain geometrically fragile, leading to failures in spatial reasoning needed for embodied AI, robotics, and autonomous driving. Prior approaches to geometry grounding either fine-tune VLMs on spatial question answering, which can perpetuate spurious visual representations, or fuse features from large geometry-grounded vision models, which substantially increases model size at inference. Knowledge distillation from geometry-grounded vision models offers an alternative, but directly matching multi-view teacher features can disrupt the pretrained alignment between visual and textual representations, degrading object- and language-semantic capabilities. We propose multi-view relational distillation (MVRD), which distills patch-wise cosine similarities across views instead of the teacher features themselves. These relations encode geometric correspondences adequate for spatial understanding, while leaving the student representation underdetermined, allowing it to remain close to its pretrained vision- language space. Across representative VLMs, MVRD improves visual-spatial reasoning, outperforming supervised fine-tuning and feature distillation while approaching feature fusion methods with considerably fewer added parameters and lower latency. We show that MVRD makes visual representations more geometric while retaining language alignment, and generalizes to 3D scene understanding tasks such as object grounding, dense captioning, and question answering.

</details>

#### 2026-08-11 - Cross-View Sequential Visual Localization with Spatio-Temporal Context Modeling for Autonomous Driving

**Authors:** Jiaping Wang, Shaobo Li, Zhen Wang
**Links:** [abs](https://arxiv.org/abs/2608.10660) - [pdf](https://arxiv.org/pdf/2608.10660)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cross-View Sequential Visual Localization with Spatio-Temporal Context Modeling for Autonomous Driving
- 作者：Jiaping Wang, Shaobo Li, Zhen Wang
- 出版日期：2026-08-11T08:44:42Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.10660

### 一句话总结
本文提出一种基于时空上下文建模的跨视角序列视觉定位框架，通过循环跨帧模块聚合历史信息，显著提升自动驾驶场景下跨视角定位的精度与鲁棒性。

### 研究问题
现有跨视角视觉定位方法大多逐帧独立处理，未充分利用时序信息，在动态遮挡、光照变化和重复纹理等场景下精度受限。本文旨在通过时序上下文增强来解决这一问题。

### 核心思路/方法
- 提出时间上下文增强的跨视角序列视觉定位框架。
- 设计循环跨帧模块，从上一状态聚合历史上下文，增强当前帧的粗粒度地面特征。
- 增强后的特征用于卫星候选区域分类，同时利用层次化细粒度特征进行精确的局部偏移估计。

### 主要贡献
- 提出一种循环跨帧模块以聚合历史时序信息，增强当前帧特征表达。
- 在CVIS数据集上将平均定位误差从3.80 m降至1.57 m，R@1 m从8.14%提升至40.22%。
- 在KITTI-CVL数据集上直接迁移平均误差为2.61 m，目标域微调后降至2.27 m。
- 真实车辆零样本实地实验平均误差为2.84 m，R@5 m达到96.86%，验证了方法的泛化能力与实用性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶跨视角定位的时序信息利用问题提出了明确且有效的解决方案，在公开基准和真实场景上均获得显著精度提升，实验结果量化且具说服力。对从事视觉定位、自动驾驶感知相关研究的人员具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Continuous and reliable localization is essential for autonomous driving. Cross-view visual localization matches ground images with satellite maps, providing complementary localization cues for pipelines that depend on Global Navigation Satellite System (GNSS) signals and high-definition (HD) maps. Most existing cross-view visual localization methods process each frame independently, leaving temporal information underused and limiting accuracy under dynamic occlusion, illumination variation, and repetitive textures. This study proposes a temporal-context-enhanced framework for cross-view sequence visual localization. The proposed recurrent cross-frame module aggregates historical context from the previous state to enhance the coarse ground feature of each current frame. These enhanced features facilitate satellite candidate-region classification, while hierarchical fine-grained features enable precise local offset estimation. On the CVIS dataset, the proposed method reduces mean localization error from 3.80 m to 1.57 m and increases R@1 m from 8.14% to 40.22%. Direct transfer to KITTI-CVL achieves a mean error of 2.61 m, with target-domain fine-tuning further reducing the mean error to 2.27 m. Zero-shot field experiments on a real-world vehicle achieve a mean error of 2.84 m and R@5 m of 96.86%. These results demonstrate that temporal context enhancement significantly improves cross-view localization accuracy and supports robust deployment on public benchmarks and real-world roads.

</details>

#### 2026-08-11 - Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent

**Authors:** Zitong Shan, Baichuan Lou, Yanxin Zhou, Shuge Wu, Xianqi He, Bolin Zhao, Sheng Zhao, Zhouheng Li, Chee Kiong Ong, King Ho Holden Li, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2608.10618) - [pdf](https://arxiv.org/pdf/2608.10618)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent
- 作者：Zitong Shan, Baichuan Lou, Yanxin Zhou, Shuge Wu, Xianqi He, Bolin Zhao, Sheng Zhao, Zhouheng Li, Chee Kiong Ong, King Ho Holden Li, Chen Lv
- 出版日期：2026-08-11T08:01:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要页](https://arxiv.org/abs/2608.10618) | [PDF](https://arxiv.org/pdf/2608.10618)

### 一句话总结
该研究提出一种以世界模型为中心的自动驾驶赛车智能体，通过在真实车辆和仿真环境中联合探索认知与物理极限，实现高速交互场景下的高成功率自主驾驶。

### 研究问题
具身智能系统在极端条件下（如高速、近饱和动力学、对抗性交互）的能力边界尚未被充分理解；现有系统虽能实现高速性能，但很少联合建模和优化认知极限与物理极限。

### 核心思路/方法
- 构建以世界模型为中心的闭环学习框架，从接近极限的成功与失败样本中学习预测世界模型，以捕获交互演化、自车动力学和可行运动边界。
- 将世界状态构建、未来感知推理和近极限控制整合在一个闭环优化过程中。
- 训练数据来自真实车辆自动驾驶赛车（最高速度256.3 km/h，峰值横向加速度26.8 m/s²），并在全尺寸仿真环境中进行验证和泛化测试。
- 通过世界模型与策略的闭环细化，提升极限利用率、失败模式恢复和跨场景泛化能力。

### 主要贡献
- 提出一种边界感知方法，使具身智能体能够表示、预测并持续细化自身能力边界。
- 在真实车辆极端工况下采集训练数据，验证了系统在高速和高峰值加速度下的鲁棒定位与感知能力。
- 在全尺寸仿真中达到88.3%的交互成功率，并展示了对不同场景和未知赛道的泛化能力。
- 实例化了一种将认知与物理极限联合探索的自主赛车智能体范式。

### 局限性
摘要未提供足够信息：未说明仿真与真实世界的差距、失败模式的具体类型、计算资源要求、对比基线方法、消融实验细节以及安全保证机制。

### 阅读优先级
**高**。理由：该工作将世界模型与自主赛车结合，直指具身智能在极端动态条件下的能力边界问题，且包含真实高速数据（256.3 km/h）和仿真验证（88.3%成功率），兼具理论深度与应用价值，对自动驾驶、具身智能和机器人控制领域有重要参考意义。

</details>

<details>
<summary>Abstract</summary>

Embodied artificial intelligence aims to develop agents that perceive, reason, and act through continuous interaction with the physical world. However, most embodied systems are still evaluated within conservative safety margins or moderate interaction regimes, leaving their capability boundaries under extreme conditions insufficiently understood. Autonomous racing provides a stringent testbed by combining high-frequency localization and perception, adversarial interaction, near-saturated vehicle dynamics, and strict safety constraints. Existing systems push high-speed performance but rarely model and refine cognitive and physical limits jointly. Here we show that a world-model-centric autonomous racing agent provides a concrete step toward exploring these coupled limits. The framework learns predictive world models from near-limit successes and failures to capture interaction evolution, ego dynamics, and feasible-motion boundaries, coupling world-state construction, future-aware reasoning, and near-limit control in a closed-loop refinement process. Training data were collected from real-vehicle autonomous racing, where the onboard system maintained robust localization and perception at speeds up to 256.3 km/h and peak lateral acceleration of 26.8 m/s$^2$. In full-scale simulated racing, the well trained world-model-centric agent achieves an 88.3% interaction success rate across various challenging simulated racing scenarios. Closed-loop refinement of the world model and policy further improved utilization of cognitive-physical limits, recovery from failure modes, and generalization across varying conditions and unseen circuits. These results suggest a boundary-aware methodology in which world models help embodied agents represent, predict, and continually refine their capability boundaries for safer real-world deployment.

</details>

#### 2026-08-11 - PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots

**Authors:** Shuo Bao, Wei Dong, Shuyue Zhang, Ming Shang, Yuchen Huang, Han Yu, Chengjie Xu, Yiheng Bi, Kai Sun, Fuchun Sun, Xinzhou Wang
**Links:** [abs](https://arxiv.org/abs/2608.10449) - [pdf](https://arxiv.org/pdf/2608.10449)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots
- 作者：Shuo Bao, Wei Dong, Shuyue Zhang, Ming Shang, Yuchen Huang, Han Yu, Chengjie Xu, Yiheng Bi, Kai Sun, Fuchun Sun, Xinzhou Wang
- 出版日期：2026-08-11
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.10449

### 一句话总结
本文提出PBD-AG框架，一种用于长时程服务机器人的持久基线-增量主动图结构，通过解耦稳定的固定设施与可更新的动态对象事件，实现自主构建、修订和可靠的世界模型。

### 研究问题
长时程服务机器人如何在未知环境中自主构建持久的世界模型，并在任务相关对象发生变化时进行有效修订，同时避免现有方法中在线建图误差累积、静态场景无法捕捉对象变化、以及高层视觉-语言预测缺乏可验证3D几何证据等问题。

### 核心思路/方法
- 提出“持久基线-增量主动图”（PBD-AG）框架，将机器人已验证的稳定固定设施（基线）与可修订的动态对象事件（增量）进行解耦。
- 机器人通过机载探索自主建立结构基线，并对发现的固定设施进行检测，以构建分层对象信念。
- 维护带有可靠性权重的对象状态，涵盖几何、语义、身份、存在性和支撑关系。
- 引入几何可见性门控机制，减少遮挡导致的错误删除。
- 使用图条件策略选择检测视点，综合考虑目标覆盖率、移动代价、碰撞风险和冗余观测。

### 主要贡献
- 提出PBD-AG框架，将持久世界模型分解为稳定基线与可修订动态事件，支持长期自主感知。
- 设计可靠性加权的对象状态表示，涵盖多维度属性及支撑关系。
- 引入几何可见性门控以缓解遮挡条件下的误删问题。
- 提出图条件视点选择策略，平衡多种检测目标。
- 在多种仿真环境及受控动态评估中，相比能力匹配的对照组，取得更高的聚合粗粒度固定设施F1分数，以及更强的身份连续性和事件召回。
- 提供物理机器人定性演示，展示与机载感知的集成，以及可追溯世界模型的可行性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对服务机器人长时程感知中世界模型持久性与动态更新的核心挑战，提出了结构清晰的框架（基线-增量解耦、可靠性权重、几何门控、主动视点选择），并在仿真与物理机器人上均有验证，方法设计完整且具有实际应用价值，适合机器人感知与主动SLAM方向的研究者关注。

</details>

<details>
<summary>Abstract</summary>

Long-horizon service robots require persistent world models that can be built autonomously in unseen environments and revised as task-relevant objects change. Existing methods rely on online mapping, which accumulates localization and observation errors, static scene representations that cannot capture persistent object changes, or holistic vision-language predictions that lack verifiable 3D geometric evidence. We present PBD-AG, a persistent baseline-delta active graph framework that decouples robot-verified stable fixtures from revisable dynamic object events. Under our framework, the robot autonomously bootstraps the structural baseline from onboard exploration and inspects discovered fixtures to ground hierarchical object beliefs. PBD-AG maintains reliability-weighted object states over geometry, semantics, identity, existence, and support relations, utilizing a geometric visibility gate to mitigate false deletions under occlusion. Inspection viewpoints are selected by a graph-conditioned policy that balances target coverage, travel cost, collision risk, and redundant observation. Simulation experiments in multiple environments and under controlled dynamic evaluation show higher aggregate coarse-fixture F1 than capability-matched controls, as well as stronger identity continuity and event recall. A qualitative physical-robot demonstration further illustrates integration with onboard sensing, providing a traceable world model for long-horizon robotic perception.The project page of PBD-AG is available at https://shuobao214.github.io/PBD-AG/

</details>

#### 2026-08-10 - 4D-WAM: 4D Consistent World Modeling for Autonomous Driving

**Authors:** Jiacheng Fu, Yibo Yuan, Meng Tian, Yue Li, Jiangtong Zhu, Jianhua Han, Yueyi Zhang, Jianwu Fang, Jianru Xue, Hang Xu, Zhiwei Xiong
**Links:** [abs](https://arxiv.org/abs/2608.10107) - [pdf](https://arxiv.org/pdf/2608.10107)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric foundation model, autonomous driving, driving scene, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4D-WAM: 4D Consistent World Modeling for Autonomous Driving
- 作者：Jiacheng Fu, Yibo Yuan, Meng Tian, Yue Li, Jiangtong Zhu, Jianhua Han, Yueyi Zhang, Jianwu Fang, Jianxue Xue, Hang Xu, Zhiwei Xiong
- 出版日期：2026-08-10T18:14:52Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.10107

### 一句话总结
4D-WAM 通过引入几何基础模型在训练阶段提供 4D 一致性监督，使自动驾驶世界模型能够预测物理一致的 4D 场景演化，从而提升轨迹规划性能。

### 研究问题
现有世界-动作模型（WAM）仅基于视频（2D 投影）训练，缺乏对底层 4D 驾驶场景结构的理解，导致生成视觉上合理但 4D 不一致的未来预测，进而误导下游规划任务。

### 核心思路/方法
- 将 WAM 预测的未来帧输入到几何基础模型中，利用其输出的 4D 感知响应定义 4D 一致性损失，在训练时监督模型理解并预测物理一致的 4D 场景，且不增加推理成本。
- 识别出 WAM 的“早期决策”现象，并提出面向决策的时间步采样策略，重点关注早期高噪声阶段（此时驾驶决策主要形成），将 4D 监督传播到该关键阶段以进一步改进轨迹规划。

### 主要贡献
- 提出 4D-WAM，一种利用几何基础模型进行训练时监督、实现 4D 一致世界建模的方法。
- 提出决策导向的时间步采样策略，针对 WAM 的早期决策现象强化关键阶段监督。
- 在 NAVSIM-v1 和 NAVSIM-v2 基准上取得最先进性能，有效建模 4D 一致的场景演化。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶中世界模型的核心缺陷（4D 不一致）提出新颖且低成本的解决思路（训练时监督+决策导向采样），并在两个挑战性基准上达到 SOTA，对自动驾驶感知与规划交叉领域具有较强参考价值。摘要提供了完整的方法动机和验证结论，适合目标研究者深入阅读。

</details>

<details>
<summary>Abstract</summary>

Emerging World-Action Models (WAMs) have demonstrated promising performance in autonomous driving by jointly modeling future driving scene evolution and trajectory planning. However, existing WAMs are typically trained with video data, which is only 2D projections of the underlying 4D driving scene. Consequently, WAMs fail to understand and capture the structure of 4D scenes and thus generate visually plausible yet 4D inconsistent future predictions that mislead downstream planning. To alleviate this issue, we present 4D-WAM, a model that leverages geometric foundation models for training-time supervision to enable 4D consistent world modeling. Specifically, we feed WAM-predicted future frames into a geometric foundation model, and use 4D-aware responses to define a 4D consistency loss. This loss encourages the model to understand, represent, and predict physically consistent 4D scenes during training, without additional inference cost. Moreover, we identify an early-decision phenomenon in WAMs and propose a decision-oriented timestep sampling strategy that emphasizes supervision at early, high-noise stages, where driving decisions are primarily formed. By propagating 4D supervision to this critical decision-formation phase, the proposed strategy further improves trajectory planning. Extensive experiments demonstrate that 4D-WAM effectively models 4D consistent scene evolution and achieves state-of-the-art performance on challenging NAVSIM-v1 and NAVSIM-v2 benchmarks.

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
