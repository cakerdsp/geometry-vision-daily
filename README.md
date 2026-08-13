# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：47
- 分类分布：
  - Embodied / Robotics / AR Applications: 16
  - Neural Scene Representations & Rendering: 14
  - 3D Reconstruction & Multi-view Geometry: 12
  - Geometry Foundation Models: 4
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**1. 3D 高斯泼溅（3DGS）从“表示”走向“计算基础设施”**
今日论文中，3DGS 已不再仅仅是新视角合成的工具，而是被深度用作各类高层任务的“共享 3D 空间”。Seed2GS 在冻结的 3DGS 场景上做物体提取；COGENT 在高斯参数空间而非体素空间生成医学影像反事实解释；WildFireGS 直接在语义增强的 3DGS 森林场景上运行基于物理的野火模拟；Embodied Multimodal Grounding 则用 Semantic-3DGS 作为具身操作的统一接口（感知、定位、动作条件化）。这表明 3DGS 正成为一种可编辑、可模拟、可推理的通用 3D 数据中枢。

**2. 三维视觉基础模型的“测试时自适应”与“即插即用”成为刚需**
预训练的三维几何基础模型（如 VGGT、DUSt3R 类模型）虽然泛化能力强，但缺乏显式多视图几何一致性。Self-Geometry 提出无需真值的即插即用测试时自适应（TTA）管线，直接用 2D 像素对应作为伪真值施加显式约束；VGGD 则将 VGGT 的几何先验注入单帧环视驾驶重建的前端。这说明领域正在从“训练更大的基础模型”转向“如何低成本地适配既有基础模型到特定任务/传感器/场景”。

**3. 可解释性（XAI）与推理能力向显式 3D 表征迁移**
可解释性研究不再满足于 2D 热力图或体素空间归因。CAM 综述系统梳理了从 CNN 到 Transformer 再到基础模型时代的类激活映射演进；COGENT 将反事实解释直接定义在高斯基元参数空间；CausalSplat 则定义了“推理式 3D 高斯分割”这一新任务，要求模型处理常识、空间、功能与反事实推理。可解释性与高层次语义/因果推理正在与显式场景表示深度融合。

**4. 跨视角、跨模态、跨传感器的“统一化”与“几何-语义解耦”**
跨视角特征匹配综述指出领域正从任务特化走向统一可泛化对应模型；STAR 通过空间拓扑感知的路由解决跨传感器模态（激光雷达、RGB-D 等）的 3D 理解统一问题；RGB-HS 将 RGB 基础模型的知识迁移到热成像深度估计。同时，多个工作强调将几何信息与语义/外观信息解耦（如 VGGD 的双路径颈部、MVRD 只蒸馏几何关系而非特征、CausalSplat 将显式结构感知与隐式逻辑推理解耦），这种解耦正成为处理多模态、多任务的核心设计模式。

**5. 具身智能与自动驾驶的“仿真-现实”边界加速融合，且更注重时序与物理极限**
RoadWeaver 从零生成大规模车道级 HD 地图用于驾驶仿真；WildFireGS 从观测数据构建真实世界野火数字孪生；World-Model-Centric Autonomous Racing Agent 用真实极端工况数据训练世界模型探索认知-物理极限；Cross-View Sequential Visual Localization 通过循环跨帧模块利用时序上下文显著提升定位精度。仿真数据生成、数字孪生与现实世界之间的鸿沟正在被系统性地弥合。


#### 技术路线观察

| 方向 | 代表论文 | 技术侧重点 |
|------|----------|------------|
| **几何基础模型（Geometry Foundation Models）** | Map-Det3D、Self-Geometry、VGGD | 将预训练的几何先验作为骨干或前端；用显式几何约束（像素对应、多视图一致性）替代隐式自一致性；关注跨域迁移与测试时优化，而非重新训练大模型 |
| **3D 重建与多视角几何** | HSTGFormer、GS-CPE、Gaussian Sculpting、Cross-View Feature Matching | 重建框架普遍采用“粗到细”（coarse-to-fine）策略；传统重建任务（姿态估计、表面重建）正在与 3DGS 深度融合；Transformer/图模型与几何约束结合解决时空耦合问题 |
| **神经场景表示与渲染** | Seed2GS、COGENT、CausalSplat、Compact Feed-Forward 3DGS、WildFireGS | 3DGS 的“可编辑性”和“语义可操作性”成为核心卖点；关注在冻结场景上的后处理（提取、解释、模拟），以及紧凑化表示（原语合并、显著性引导）；高斯参数空间成为新的“语义操作界面” |
| **机器人 / AR / 具身智能** | Embodied Multimodal Grounding、RoadWeaver、World-Model Racing、Cross-View Loc | 强调“多模态对齐”（语言-视觉-3D-动作）；语义 3D 表示作为机器人感知与动作策略之间的接口；仿真数据生成（HD 地图）和世界模型成为评价与训练的关键；关注从单帧感知走向时序/序列建模 |
| **可解释性（跨领域）** | CAM Survey、COGENT | 解释目标从“可视化”走向“因果/反事实”；从 2D 像素级归因走向 3D 结构级归因；综述类工作开始系统化整理方法分类学（CAM 综述），反映领域成熟度提升 |

**总体观察**：3DGS 与几何基础模型两条技术线正在交汇。3DGS 提供可操作、可编辑的显式场景结构，几何基础模型提供强泛化的先验知识，二者的结合点（如“基础模型先验 + 高斯场景适配”）是当前最活跃的探索地带。


#### 值得优先阅读的论文

**1. CausalSplat（arXiv:2608.11150）** — 高优先级
理由：定义了“推理式 3D 高斯分割”这一新任务，并配套构建了两个基准（Causal-LERF、Causal-ScanNet），同时给出框架。既做任务定义又做基准又给方法，是该方向研究者不可绕过的起点，对具身智能和开放词汇 3D 理解有直接推动。

**2. Self-Geometry（arXiv:2608.10708）** — 高优先级
理由：首个直接施加显式多视图几何约束的测试时自适应方法，区别于此前依赖隐式一致性的工作。该思路对任何使用 3D VFM 的下游任务（重建、定位、检测）都有潜在适配价值，且即插即用的设计使其易于复现和推广。

**3. Cross-View Feature Matching 综述（arXiv:2608.11093）** — 高优先级
理由：领域正处于从任务特化向统一模型转型的关键期，该综述提供了统一分类体系和同协议基准测试，且专门分析了视觉基础模型的影响。对需要快速建立领域全局图景、确定研究切入点的读者价值很高。

**4. Map-Det3D（arXiv:2608.12179）** — 中高优先级
理由：将前馈式度量 3D 重建模型作为几何骨干，绕开“2D 检测 + 3D 提升”的脆弱范式，直接在建好的度量 3D 空间中做检测。对自动驾驶和机器人视觉定位/检测方向的范式转换具有代表性和启发意义。

**5. Seed2GS（arXiv:2608.11928）** — 中高优先级
理由：在无原始相机、无场景训练的情况下达到最高 LERF-MASK 精度，且延迟仅 9.3 秒。该方法为 3DGS 场景的轻量级交互编辑提供了实用标杆，其对“目标身份”与“3D 覆盖”解耦的思考也有方法论价值。


#### 可能的研究机会

**1. 显式几何约束的“无监督/自监督”测试时优化框架推广**
Self-Geometry 证明了用像素对应作伪真值可提升 3D VFM 的几何一致性。这一思路可推广到其他任务（如 3DGS 场景的在线位姿修正、动态场景的几何一致渲染），或探索更鲁棒的伪对应生成方式（结合光流、特征匹配）以避免对噪声对应的敏感

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-13T09:44:45-04:00
**Total number of papers:** 47
**Number of papers added in the latest update:** 8
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

#### 2026-08-12 - Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs

**Authors:** Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò, Sunghwan Hong, Denis Rozumny, Johannes Schönberger, Zuria Bauer, Hermann Blum, Peter Kontschieder, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2608.12179) - [pdf](https://arxiv.org/pdf/2608.12179)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs
- 作者：Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò, Sunghwan Hong, Denis Rozumny, Johannes Schönberger, Zuria Bauer, Hermann Blum, Peter Kontschieder, Marc Pollefeys
- 出版日期：2026-08-12
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.12179

### 一句话总结
Map-Det3D 将前馈式度量 3D 重建模型作为几何骨干，将多视角 3D 物体检测直接引入重建出的度量 3D 空间中，从而从单目视频流中实现稳定的度量级 3D 检测。

### 研究问题
如何在缺乏深度传感器的情况下，从单目视频流中实现可靠的度量级 3D 物体检测，尤其是克服单张图像中深度和绝对尺度欠约束带来的检测不稳定性，以及在相机、运动或环境发生域偏移时的泛化问题。

### 核心思路/方法
- 设计在线多视角 3D 检测模型 Map-Det3D，将短时间窗口内的多视图映射为输入，使用前馈度量 3D 重建模型作为几何骨干，并调整其面向物体的能力。
- 直接在重建出的度量 3D 空间中预测 3D 检测框，绕过常用的 2D 检测后提升至 3D（2D-to-3D lifting）的范式。
- 在多个基准上验证了在线性能和鲁棒的跨域迁移能力。

### 主要贡献
- 提出 Map-Det3D，将检测直接融入从 RGB 重建的 3D 空间中，避免 2D 到 3D 提升的脆弱性。
- 展示了将重建先验训练用于检测是获得单目视频稳定度量 3D 检测的实用路径。
- 验证了该设计在多个基准上的强在线性能及无需适应的鲁棒迁移能力，并开源代码与模型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目 3D 检测中尺度欠约束的核心难题，提出了一种新颖的“重建-检测”一体化范式，且实验显示跨域迁移能力强，对面向具身智能的视觉感知研究具有较高参考价值。摘要中虽未给出定量结果细节，但问题动机清晰、方法路径创新，建议优先精读。

</details>

<details>
<summary>Abstract</summary>

Metric 3D object detection is a core capability for embodied agents, yet most reliable systems lean on depth sensors, trading away cost, power, and integration simplicity. This motivates monocular 3D detection, which avoids additional constraints, yet it faces a major obstacle: from a single image, depth, and especially absolute scale, are underconstrained. As a result, the prevailing pattern of detecting in 2D and then predicting 3D attributes is often brittle, since modest range errors can dominate 3D localization, and the learned scale prior can fail when cameras, motion, or environments undergo domain shifts. To address this, we propose Map-Det3D, an online multi-view 3D object detection model that brings detection directly into a 3D space reconstructed from RGB. We map a short temporal window into multiple views and repurpose a feed-forward metric 3D reconstruction model as our geometric backbone while tuning its object-aware capabilities. Building on this representation, Map-Det3D directly predicts boxes in metric 3D space, without the widely used 2D-to-3D lifting. Experiments across different benchmarks show that this design supports strong online performance and robust transfer without adaptation, suggesting that training reconstruction priors for detection is a practical route to stable metric 3D detection from monocular video. Code and models are available at https://royyang0714.github.io/Map-Det3D.

</details>

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

## 3D Reconstruction & Multi-view Geometry

### 2026-08

#### 2026-08-12 - HSTGFormer: Hyper Spatial-Temporal Graph Transformer for 3D Human Pose Estimation

**Authors:** Ruochen Li, Shuang Chen, Wenke E, Farshad Arvin, Amir Atapour-Abarghouei
**Links:** [abs](https://arxiv.org/abs/2608.12187) - [pdf](https://arxiv.org/pdf/2608.12187)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HSTGFormer: Hyper Spatial-Temporal Graph Transformer for 3D Human Pose Estimation
- 作者：Ruochen Li, Shuang Chen, Wenke E, Farshad Arvin, Amir Atapour-Abarghouei
- 出版日期：2026-08-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.12187

### 一句话总结
本文提出一种图增强的Transformer框架HSTGFormer，通过超时空图将空间与时间推理耦合成局部图聚合，实现高效且精度高的单目3D人体姿态估计。

### 研究问题
现有基于Transformer的3D人体姿态估计方法通常将空间和时间推理分为两个独立阶段，这可能导致对动作中固有的统一时空依赖建模不足，并在时间建模之前压缩了帧级结构信息。本文旨在解决这一问题，构建更统一的时空关联推理方式。

### 核心思路/方法
- 提出**Hyper Spatial-Temporal Graph (HSTG)**：将每帧的骨架图扩展到时间邻域，将全局时空推理分解为围绕每个“关节点-时间”节点的局部时空感受野，实现结构感知的耦合推理，同时保留局部结构运动信息。
- 引入**Adaptive Dual-Scale Temporal Graph (ADSTG)**：在互补的短窗口和长窗口内捕获关节点特定的时间依赖。
- 设计轻量级的**节点级融合模块**：自适应地整合两种图表示，用于每个“关节点-时间”节点。

### 主要贡献
- 提出将时空推理重新表述为“关节点-时间”节点上的局部耦合图聚合，替代传统分离式时空建模。
- 设计HSTG实现局部结构感知的耦合时空推理，并保留局部结构运动信息。
- 引入ADSTG与节点级融合模块，增强跨尺度时间依赖建模。
- 在Human3.6M和MPI-INF-3DHP数据集上验证了强精度与高计算效率（摘要提供实验范围，具体数值未给出）。

### 局限性
摘要未提供足够信息，具体局限性（如对遮挡、极端姿态的鲁棒性、长序列效率等）未在摘要中说明。

### 阅读优先级
**高**  
理由：该工作针对3D人体姿态估计中时空建模分离的核心问题提出了统一的耦合图推理框架，并声称在主要基准上取得强精度与高效率，方法设计具有新意，对关注人体姿态估计和时空建模的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Transformer-based methods have achieved strong performance in monocular 3D human pose estimation, but most existing approaches organise spatial and temporal reasoning as separate stages, which may weaken unified spatial-temporal interdependencies inherent in human motion and compress frame-level structural information before temporal modelling. In this paper, we propose HSTGFormer, a graph-enhanced Transformer framework that reformulates spatial-temporal reasoning as localised coupled graph aggregation over joint-time nodes. Specifically, HSTGFormer introduces a Hyper Spatial-Temporal Graph (HSTG), which decomposes global spatial-temporal reasoning into local spatial-temporal receptive fields around individual joint-time nodes by extending per-frame skeleton graphs into temporal neighbourhoods, thereby enabling structure-aware coupled reasoning while preserving local structural motion information. It further incorporates an Adaptive Dual-Scale Temporal Graph (ADSTG) to capture joint-specific temporal dependencies over complementary short- and long-range windows. A lightweight node-wise fusion module further adaptively integrates the two graph representations for each joint-time node. Experiments on Human3.6M and MPI-INF-3DHP show that HSTGFormer achieves strong accuracy with high computational efficiency.

</details>

#### 2026-08-12 - Repurposing RGB-based Foundation Model for Depth Estimation on Thermal Images Using Hierarchical Supervision

**Authors:** Jie Hong, Tingtian Li, Xuesong Li, Xiao Li
**Links:** [abs](https://arxiv.org/abs/2608.11564) - [pdf](https://arxiv.org/pdf/2608.11564)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Repurposing RGB-based Foundation Model for Depth Estimation on Thermal Images Using Hierarchical Supervision
- 作者：Jie Hong, Tingtian Li, Xuesong Li, Xiao Li
- 出版日期：2026-08-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.11564

### 一句话总结
本文提出RGB-HS框架，通过从RGB基础模型向热成像编码器施加层级监督，以提升热成像深度估计性能。

### 研究问题
如何更充分地利用RGB基础模型在热成像深度估计任务中的表征能力，尤其是其编码器中蕴含的层级结构信息。

### 核心思路/方法
- 将热成像编码器替换为RGB基础模型，并引入同架构的RGB分支作为教师网络。
- 在两个编码器的多个层级之间进行token对齐，使热成像学生分支同时获得结构精度与语义抽象信息。
- 引入验证机制，根据RGB图像质量对教师分支的token进行加权，优化对齐过程。

### 主要贡献
- 提出RGB-HS框架，利用层级监督从RGB基础模型迁移知识到热成像深度估计。
- 通过在多个层级进行token对齐，更全面地利用基础模型的层级表征。
- 引入基于RGB图像质量的验证机制，细化对齐过程。
- 在公开基准上验证了该方法的竞争力，表明其能更有效地挖掘RGB基础模型的表征能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向热成像深度估计这一特定应用场景，方法核心在于层级监督与跨模态对齐，思路有一定新颖性，但摘要未给出定量结果或与现有方法的详细对比，读者若从事多模态深度估计或基础模型迁移研究可关注，否则优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

Depth estimation from thermal images is highly valuable for robotic applications in adverse conditions, such as nighttime and rainy weather. Recent studies have sought to transfer knowledge from RGB-based foundation models to thermal modalities, yet the rich hierarchical representations these models encode remain underutilized. To address this limitation, we propose RGB-HS, a novel framework for thermal-image depth estimation that leverages hierarchical supervision from an RGB-based foundation model. Specifically, we first replace the baseline thermal encoder with a foundational model and introduce a parallel RGB branch that also employs a foundational model as an encoder of the same architecture, taking RGB images as input. The alignment is then performed across multiple levels between the tokens of the two encoders, allowing the thermal student branch to capture both structural precision and semantic abstraction from the RGB teacher branch. Furthermore, we introduce verification to refine the alignment process by weighting tokens from the RGB branch based on RGB image quality. Extensive experiments on the popular benchmark demonstrate that RGB-HS achieves competitive performance and more effectively exploits the representational capacity of RGB-based foundation models for depth estimation on thermal images.

</details>

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

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-12 - Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding

**Authors:** Zongjian Ding, Yudong Gao, Jiale Liu, Xinglin Yu, Junxing Ren, Dong Wei, Yajing Chen, Shan Huang, Mingjun Cheng, Min Li
**Links:** [abs](https://arxiv.org/abs/2608.11928) - [pdf](https://arxiv.org/pdf/2608.11928)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding
- 作者：Zongjian Ding, Yudong Gao, Jiale Liu, Xinglin Yu, Junxing Ren, Dong Wei, Yajing Chen, Shan Huang, Mingjun Cheng, Min Li
- 出版日期：2026-08-12
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.11928

### 一句话总结
Seed2GS提出一种无需原始重建相机、无需场景特定训练的目标物体提取方法，从3D高斯溅射场景中通过单参考视图标注实现对目标的高精度分割，在LERF-MASK上达到92.1% mIoU。

### 研究问题
如何从预构建的3D高斯溅射(3DGS)场景中高效且准确地提取目标物体，同时不依赖原始重建相机信息，也不需要针对每个场景进行耗时的表示训练。

### 核心思路/方法
核心思想是将“目标身份识别”与“3D覆盖范围”分离处理。具体方法包括：
- 利用QD-SAM3从多个开放词汇候选掩码中选出唯一可靠的参考掩码，一次性固定目标身份；
- 通过种子提升(Seed lift)和可见性自适应虚拟轨道(visibility-adaptive virtual orbits)从新视角暴露物体；
- 使用跟踪传播种子，避免重复检测；
- 场景保持冻结，掩码仅用于监督每个高斯分布的单一临时前景logit。

### 主要贡献
- 在不使用原始重建相机、不进行场景特定表示训练的条件下，达到当前最高的LERF-MASK分割精度（92.1% mIoU）；
- 测量计算延迟仅9.3秒，比最强的场景训练基线高3.7个百分点，比最接近的无相机基线高7.6个百分点；
- 在固定单个测试参考视图时，完整流程仍保持91.1% mIoU；
- 使用真实掩码替换预测种子仅提升0.72个百分点，说明种子预测已接近上限；
- 在3D-OVS数据集上达到95.7% mIoU。

### 局限性
摘要未提供足够信息。具体包括：未提及该方法对复杂场景、遮挡情况、多目标场景的鲁棒性，未说明不同数据集间的泛化表现差异原因，未讨论失败案例或常见错误模式，也未提供与其他方法在运行时间、内存占用等方面的详细对比数据。

### 阅读优先级
**高**。理由：该方法在无需原始相机且无需训练的条件下，显著提升了3DGS目标提取的精度（LERF-MASK 92.1% mIoU），同时计算延迟极低（9.3秒），具有实际应用价值；且其“分离身份与覆盖范围”的方法设计具有新颖性，对交互式3D编辑和场景理解领域有参考意义。

</details>

<details>
<summary>Abstract</summary>

Extracting a target object from a pre-built 3D Gaussian Splatting (3DGS) scene enables interactive 3D editing. Existing methods either train for tens of minutes per scene, sacrifice accuracy, or require original reconstruction cameras that pre-built assets may not include. We present Seed2GS, which achieves the highest reported LERF-MASK accuracy without original reconstruction cameras or scene-specific representation training. Its key insight is to separate target identity from 3D coverage. QD-SAM3 selects one reliable reference mask from several open-vocabulary candidates, fixing identity once. Seed lift and visibility-adaptive virtual orbits then expose the object from new viewpoints, while tracking propagates the seed without repeated detection. Because the scene remains frozen, these masks supervise only one temporary foreground logit per Gaussian. On LERF-MASK, Seed2GS reaches 92.1% mean intersection over union (mIoU) with a measured compute-only latency of 9.3 seconds, 3.7 points above the strongest scene-trained baseline and 7.6 points above the closest camera-free baseline. With one fixed test reference per scene, the complete pipeline retains 91.1% mIoU; replacing its predicted seed with a ground-truth mask improves mIoU by only 0.72 points. On 3D-OVS, Seed2GS reaches 95.7% mIoU.

</details>

#### 2026-08-11 - COGENT: Counterfactual Gaussian Explanations for Volumetric Medical Images

**Authors:** Dorian Rząsa, Bartosz Zabdyr, Krzysztof Piekarz, Jakub Grzywaczewski, Bartlomiej Sobieski, Przemyslaw Biecek, Żaneta Świderska-Chadaj, Olga Śliwicka, Przemysław Spurek, Joanna Świebocka-Więk
**Links:** [abs](https://arxiv.org/abs/2608.11422) - [pdf](https://arxiv.org/pdf/2608.11422)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation, differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：COGENT: Counterfactual Gaussian Explanations for Volumetric Medical Images
- 作者：Dorian Rząsa, Bartosz Zabdyr, Krzysztof Piekarz, Jakub Grzywaczewski, Bartlomiej Sobieski, Przemyslaw Biecek, Żaneta Świderska-Chadaj, Olga Śliwicka, Przemysław Spurek, Joanna Świebocka-Więk
- 出版日期：2026-08-11
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.11422

### 一句话总结
COGENT 提出一种在三维高斯体素表征参数空间中生成反事实解释的新框架，用于体素级医学影像（如肺部 CT）的可解释性分析。

### 研究问题
如何在三维体素医学影像（如肺 CT）中生成既保持解剖一致性、又具有空间局部性的反事实解释，以替代传统逐像素/逐体素归因方法。

### 核心思路/方法
- 基于 MedGS 和 Sybil 肺癌风险预测模型构建框架。
- 在基于高斯的体素表征参数空间中优化选定的高斯基元（Gaussian primitives），而非在体素空间操作。
- 通过可微渲染管线传递下游预测器的梯度，识别对模型决策影响最大的表征组件。
- 将可解释性问题形式化为显式三维场景表示上的反事实优化问题，生成稀疏、局部化且解剖一致的解释。

### 主要贡献
- 提出首个在高斯参数空间中生成反事实解释的框架（COGENT）。
- 将可解释性从体素空间扩展到显式三维场景表征，改变了传统归因范式。
- 在肺 CT 上结合定量比较和医学专家定性分析，验证了解释的临床意义和有效性。

### 局限性
摘要未提供足够信息——未提及方法的计算开销、对不同三维表示或任务类型的泛化性、反事实生成的时间成本或潜在失败模式等细节。

### 阅读优先级
**中**。理由：该工作结合了三维场景表征与医学影像可解释性，视角新颖，对从事体绘可解释性、三维医学影像诊断的读者有参考价值；但摘要中实验细节有限，且仅针对单一任务（肺癌风险预测）验证，若需深入评估需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Explainability is essential for deploying deep learning models in high-stakes medical applications. Existing explainability methods for volumetric imaging predominantly operate in voxel space, overlooking the structured representations introduced by recent advances in 3D scene modeling. We present COGENT (Counterfactual Gaussian Explanations), a framework that generates counterfactual explanations directly in the parameter space of Gaussian-based volumetric representations. Built upon MedGS and the Sybil lung cancer risk prediction model, COGENT optimizes selected Gaussian primitives through a differentiable rendering pipeline, enabling gradients from the downstream predictor to identify representation components that most influence model decisions. Unlike conventional pixel- or voxel-level attribution methods, our approach formulates explainability as a counterfactual optimization problem over an explicit 3D scene representation, producing sparse and spatially localized explanations while preserving anatomical consistency. We evaluate COGENT on lung CT scans using quantitative comparisons with existing explainability methods together with qualitative analysis by medical experts. The results demonstrate that representation-space counterfactual optimization provides clinically meaningful explanations while offering a new perspective on interpreting volumetric deep learning models.

</details>

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

## Embodied / Robotics / AR Applications

### 2026-08

#### 2026-08-12 - Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations

**Authors:** AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini, AmirMohsen Eshghi, Siavash Arjomand Bigdel
**Links:** [abs](https://arxiv.org/abs/2608.12299) - [pdf](https://arxiv.org/pdf/2608.12299)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations
- 作者：AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini, AmirMohsen Eshghi, Siavash Arjomand Bigdel
- 出版日期：2026-08-12T17:45:03Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.12299

### 一句话总结
本文对2016年以来57篇以方法为中心的类激活映射（CAM）相关论文进行系统综述，提出了按归因机制、架构依赖和评估目标划分的分类法，总结了该领域从单一CNN层向多层、概率化、令牌感知及基础模型感知解释的演进趋势。

### 研究问题
类激活映射（CAM）作为可解释人工智能中广泛使用的视觉解释方法家族，其研究现状和发展趋势如何？具体包括：不同CAM方法如何归类和区分、各方法的主要贡献与遗留问题是什么，以及当前评估协议是否统一。

### 核心思路/方法
作者严格筛选了2016年以来57篇以方法为中心的论文，构建了一个分类法，从三个维度对CAM方法进行划分：（1）归因机制（gradient-based vs. gradient-free vs. hybrid）；（2）架构依赖（CNN、Transformer、基础模型等）；（3）评估目标（忠实性、定位、鲁棒性、计算成本、人类信任等）。在此基础上，分三类综述了梯度式CAM、近期与混合CAM风格方法，以及基于模型或架构感知的方法，并检视了每种方法留下的未解决缺口及后续方法的补足尝试。

### 主要贡献
1. 提供了一个严格的、以方法为中心的57篇论文综述语料库。
2. 构建了新的CAM分类法，按归因机制、架构依赖和评估目标实现多维划分。
3. 系统梳理了CAM从经典CNN场景到Transformer、基础模型时代的演进路径。
4. 明确指出评估协议碎片化问题，并分析了各方法在忠实性、定位、鲁棒性、成本和人类信任等维度上的贡献与缺口。

### 局限性
摘要未提供足够信息：未提及关于语料库选择的具体排除/纳入标准、各方法的定量对比结果、以及评估协议碎片化的具体表现或标准化建议。摘要也未报告综述过程中的偏倚控制方法或对未来研究方向的详细建议。

### 阅读优先级
**中**。理由：该文是一篇综述论文，对所涉领域（可解释视觉、CAM方法）有系统梳理价值，适合该方向研究者了解宏观脉络和分类框架。但由于其分类为“Embodied / Robotics / AR Applications”，与纯计算机视觉方向略有距离，且摘要未提供具体的实证对比结论，对于追求具体方法细节或实验复现的读者优先级略低。若读者正从事视觉可解释性研究或需要CAM方向的全景认知，则值得一读。

</details>

<details>
<summary>Abstract</summary>

Class activation mapping (CAM) is one of the most widely used visual explanation families in explainable artificial intelligence. Its purpose is intuitive: it converts internal model evidence into a heatmap that highlights the image regions, convolutional channels, tokens, or patches that support a target class or concept. Since the first CAM formulation in 2016, the field has moved far beyond global-average-pooled CNN classifiers. CAM-style methods now include gradient-based post-hoc explanations, gradient-free score and ablation methods, high-resolution upscaling, weakly supervised localization and segmentation, transformer token attribution, causal and debiasing methods, and foundation-model-era approaches that use CLIP, DINO, SAM, or feature-distribution comparisons. This review synthesizes a strict corpus of 57 method-centered papers published from 2016 onward. The paper develops a taxonomy that separates methods by attribution mechanism, architectural dependence, and evaluation objective. It then reviews gradient-based CAMs, recent and hybrid CAM-style methods, and model-based or architecture-aware methods. Across the corpus, the main trend is clear: the field is shifting from explaining one class score in one low-resolution CNN layer toward comparative, multi-layer, probabilistic, token-aware, and foundation-model-aware explanations. At the same time, evaluation remains fragmented. Faithfulness, localization, robustness, computational cost, and human trust are often measured with different protocols. The review therefore emphasizes not only what each method contributes, but also which gap it leaves open and which later methods attempt to close that gap.

</details>

#### 2026-08-12 - STAR: A Spatial-Topology Aware Routing Framework for Generalizable 3D Scene Understanding

**Authors:** Mingwei Xing, Xinliang Wang, Yifeng Shi
**Links:** [abs](https://arxiv.org/abs/2608.11699) - [pdf](https://arxiv.org/pdf/2608.11699)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：STAR: A Spatial-Topology Aware Routing Framework for Generalizable 3D Scene Understanding
- 作者：Mingwei Xing, Xinliang Wang, Yifeng Shi
- 出版日期：2026-08-12
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.11699

### 一句话总结
STAR 提出一种空间拓扑感知的路由框架，通过引入多属性自监督预训练和域感知专家路由机制，解决跨传感器模态3D场景理解中专家分配困难的问题。

### 研究问题
如何克服不同传感器模态之间的拓扑差异，构建统一的3D场景理解模型？具体而言，在语义一致性与几何异质性共存时，传统的基于特征仅使用MoE路由器难以有效分配专家，导致性能受限。

### 核心思路/方法
- 提出STAR（Spatial-Topology Aware Routing Framework）框架，包含两个主要分支：
  1. **多属性自监督预训练分支**：覆盖拓扑和纹理变化，用于锚定跨域结构先验。
  2. **域感知专家分支**，包含两个机制：
     - **Domain-Spatial-Guided Routing (DSR)**：从空间上下文捕获局部拓扑变化。
     - **Entropy-controlled Dynamic Allocation (EDA)**：根据路由不确定性调整激活专家数量。
- 两个分支结合，实现稳定的跨域表示学习与自适应专家分配。

### 主要贡献
- 提出STAR框架，将空间拓扑信息纳入MoE路由决策，改善跨域3D场景理解。
- 设计多属性自监督预训练分支，增强跨域结构先验的学习。
- 引入DSR和EDA两种机制，分别解决局部拓扑建模和动态专家分配问题。
- 实验结果表明STAR在ScanNet验证集达到80.1% mIoU，在S3DIS达到77.2% mIoU，优于强基线模型。

### 局限性
摘要未提供足够信息。摘要未明确提及方法的失败案例、计算开销、对特定传感器类型的敏感性或扩展性限制。

### 阅读优先级
**中**  
理由：该工作针对3D场景理解中的跨模态泛化问题提出系统性框架，并给出明确性能提升数据，对从事3D理解或多模态融合研究的读者有参考价值。但摘要未提供详细的实验对比和消融信息，方法的普适性和局限性难以全面评估，故优先级为中。

</details>

<details>
<summary>Abstract</summary>

Constructing a unified 3D scene understanding model has long been hindered by the topological discrepancies across sensor modalities. While applying the Mixture-of-Experts (MoE) architecture is a flexible approach for multi-domain 3D understanding, we observe that conventional feature-only MoE routers may underrepresent local sampling topology under semantic supervision, making expert allocation difficult when semantic consistency coexists with geometric heterogeneity. To overcome this challenge, we propose STAR (Spatial-Topology Aware Routing Framework). Specifically, we introduce a multi-attribute self-supervised pre-training branch, covering topological and textural variations, to anchor cross-domain structural priors. Building upon this, we design a domain-aware expert branch with two mechanisms: Domain-Spatial-Guided Routing (DSR), which captures local topological variations from spatial context, and Entropy-controlled Dynamic Allocation (EDA), which adjusts the number of activated experts according to routing uncertainty. Together, these branches combine stable cross-domain representation learning with adaptive expert allocation. Extensive experiments across various tasks, encompassing both indoor and outdoor scenes, demonstrate the effectiveness of STAR. It achieves 80.1% mIoU on the ScanNet validation set and 77.2% mIoU on S3DIS, consistently improving over strong baselines. Code is available at our project page (https://xmw666.github.io/STAR/).

</details>

#### 2026-08-12 - RoadWeaver: Large-Scale Lane-Level HD Map Generation from Scratch for Autonomous Driving Simulation

**Authors:** Yueyuan Li, Zexi Chen, Weijie Xi, Mingyang Jiang, Songan Zhang, Hanyang Zhuang, Ming Yang
**Links:** [abs](https://arxiv.org/abs/2608.11580) - [pdf](https://arxiv.org/pdf/2608.11580)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoadWeaver: Large-Scale Lane-Level HD Map Generation from Scratch for Autonomous Driving Simulation
- 作者：Yueyuan Li, Zexi Chen, Weijie Xi, Mingyang Jiang, Songan Zhang, Hanyang Zhuang, Ming Yang
- 出版日期：2026-08-12
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.11580

### 一句话总结
RoadWeaver 提出了一种从零生成大规模车道级高清地图的粗到细框架，可在数秒内生成拓扑一致、可直接用于自动驾驶仿真的完整地图。

### 研究问题
如何从零（无需真实地图或人工设计）生成大规模、多样化且拓扑一致的车道级高清地图，以支撑自动驾驶仿真中的长距离闭环评估。

### 核心思路/方法
采用粗到细的三阶段框架：
1. 合成全局道路布局；
2. 将布局扩展为连通的道路网络；
3. 构建车道级几何，并保证车道连接关系的拓扑一致性。

### 主要贡献
- 提出 RoadWeaver，首个从零生成大规模完整车道级 HD 地图的框架；
- 相比现有 SOTA 生成方法，端点对齐误差降低 94.4%；
- 生成时间仅需 1.39–3.50 秒，满足仿真场景的快速构建需求；
- 生成的地图可直接部署至驾驶模拟器，支撑闭环评估；
- 将开源训练代码与开箱即用实现。

### 局限性
摘要未提供足够信息，未明确讨论方法在极端复杂路网（如环岛、多层立交）、地图语义丰富度、泛化到不同城市风格或真实路网一致性方面的潜在局限；也未报告与真实地图数据分布差异的定量分析。

### 阅读优先级
**高**。理由：该工作针对自动驾驶仿真中高清地图生成的关键瓶颈，提出完整且可扩展的解决方案，量化指标突出（99.8%可达性、低死端率、亚米级对齐误差），且代码即将开源，对仿真平台构建和闭环评测研究具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous driving simulation requires diverse and scalable lane-level HD maps to support long-horizon evaluation across complex road networks. Existing approaches either rely on handcrafted or reconstructed real-world maps, which limits scalability, or generate only local road structures rather than complete HD maps. We present RoadWeaver, a coarse-to-fine framework for from-scratch generation of diverse, large-scale HD maps. RoadWeaver first synthesizes a global road layout, expands it into a connected road network, and then constructs lane-level geometry with topologically consistent lane connectivity. Experimental results show that RoadWeaver achieves a 99.8\% reachability, a 10.7\% dead-end ratio, and an endpoint alignment error of 0.24 m. Compared with SOTA generation methods, it reduces endpoint alignment error by 94.4\% while generating complete HD maps in 1.39--3.50 s. The generated maps can be directly deployed in driving simulators, providing scalable simulation environments for future closed-loop evaluation of autonomous driving systems. The training code and an out-of-the-box implementation of RoadWeaver will be released upon acceptance.

</details>

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
本文提出PBD-AG框架，通过将稳定环境基线（baseline）与可更新的动态物体事件（delta）解耦，为长时程服务机器人构建可追溯、可修订的持久世界模型。

### 研究问题
长时程服务机器人在未见环境中自主建图并动态更新任务相关物体状态时，现有方法存在定位与观测误差累积、静态场景表示无法捕捉物体持续变化、以及缺乏可验证3D几何证据的视觉-语言整体预测等问题。本文旨在解决如何构建既稳定又能够随物体变化而修订的持久世界模型这一核心问题。

### 核心思路/方法
- 提出**持久基线-增量活动图（Persistent Baseline-Delta Active Graph）**框架，将机器人已验证的稳定固定设施（fixtures）与可修订的动态物体事件解耦。
- 机器人通过机载探索**自主引导**结构基线，并检查发现的固定设施以构建分层物体信念。
- 维护带可靠性权重的物体状态，涵盖几何、语义、身份、存在性及支撑关系。
- 引入**几何可见性门控**（geometric visibility gate）机制，减少遮挡导致的错误删除。
- 采用**图条件化策略**选择检查视点，综合权衡目标覆盖、移动成本、碰撞风险与冗余观测。

### 主要贡献
- 提出一种将稳定基线与动态变化解耦的持久世界模型框架，支持长时程自主建图与修订。
- 设计可靠性加权物体状态表示与几何可见性门控，提升物体存在性判断的鲁棒性。
- 提出图条件化主动检查视点选择策略，均衡覆盖、成本与风险。
- 在多种仿真环境及受控动态评估中，相比能力匹配的对照方法，在粗固定设施F1、身份连续性和事件召回率上取得更好表现。
- 通过物理机器人定性演示，验证了与机载感知集成的可行性，提供可追溯的世界模型。

### 局限性
摘要未提供足够信息，未明确讨论方法在真实复杂场景中的计算开销、扩展性、长期运行稳定性极限、失败模式或对感知噪声的敏感度等局限性。

### 阅读优先级
**高**。理由：论文面向服务机器人长期自主感知这一实际重要挑战，提出的基线-增量解耦思想与不确定性感知检查机制具有明确的方法创新性，且同时提供仿真定量评估与实物定性验证，对从事机器人建图、主动感知和世界模型研究的人员具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Long-horizon service robots require persistent world models that can be built autonomously in unseen environments and revised as task-relevant objects change. Existing methods rely on online mapping, which accumulates localization and observation errors, static scene representations that cannot capture persistent object changes, or holistic vision-language predictions that lack verifiable 3D geometric evidence. We present PBD-AG, a persistent baseline-delta active graph framework that decouples robot-verified stable fixtures from revisable dynamic object events. Under our framework, the robot autonomously bootstraps the structural baseline from onboard exploration and inspects discovered fixtures to ground hierarchical object beliefs. PBD-AG maintains reliability-weighted object states over geometry, semantics, identity, existence, and support relations, utilizing a geometric visibility gate to mitigate false deletions under occlusion. Inspection viewpoints are selected by a graph-conditioned policy that balances target coverage, travel cost, collision risk, and redundant observation. Simulation experiments in multiple environments and under controlled dynamic evaluation show higher aggregate coarse-fixture F1 than capability-matched controls, as well as stronger identity continuity and event recall. A qualitative physical-robot demonstration further illustrates integration with onboard sensing, providing a traceable world model for long-horizon robotic perception. The project page of PBD-AG is available at https://shuobao214.github.io/PBD-AG/

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
