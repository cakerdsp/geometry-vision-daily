# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：69
- 分类分布：
  - Neural Scene Representations & Rendering: 26
  - 3D Reconstruction & Multi-view Geometry: 17
  - Embodied / Robotics / AR Applications: 15
  - Dynamic / 4D Reconstruction: 6
  - Geometry Foundation Models: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **3D Gaussian Splatting 从“能重建”转向“可部署、可查询、可协同”**
   本批论文中 3DGS 相关研究密集出现，但关注点不再是纯渲染质量，而是部署侧能力：ClunoGS 针对 Language 3DGS 的存储压缩与语义保持；KoalaGS 针对连续细节层次（LoD）下的计算预算收缩；AirPlayground 用 94 个 3DGS 环境构建空中导航基准；AOV-GS 用 3DGS 做主动开放词汇语义建图；CoGaussian 用稀疏高斯坦任多智能体协同语义占据的通信表示；甚至变化检测也以 3DGS 自动编辑作为监督来源。这表明 3DGS 正被当作一种“可编辑、可压缩、可传输、可语义化的场景中间表示”，而非单一渲染器。

2. **几何基础模型走向“长序列效率”与“工程可验证性”**
   BlazeVGGT 直接针对 VGGT 全对全注意力的二次复杂度，用相机 token 的“先拓扑后几何”演化做免训练键值稀疏化；DewHand 以单阶段联合手-相机运动替代多阶段管线；VeriCalib 把 LiDAR-相机外参标定重构为“可验证估计”问题，输出标定状态而非单一 RMSE。三者共同反映：几何基础模型的热点正从“能否重建”转向“长序列是否可算、误差是否可诊断、结果是否可接受”。

3. **具身智能中的几何表示强调“紧凑任务相关抽象”而非完整重建**
   GeoMem-VLA 明确主张动作生成需要的是可持续更新的紧凑几何抽象，而不是每步完整可渲染的 3D 重建，并把 3D 监督内化为几何 token 时间记忆；RangeNav 用 183k 参数的 LiDAR 距离图像编码器替代内存沉重的点云编码器以适配并行 RL 仿真；COWBOY 用向量化环境感知全身控制器加局部 RL 专家再蒸馏为单一视觉策略；CoGaussian 用稀疏高斯做多智能体通信。这一组论文共享同一取向：为具身/机器人场景设计“轻量、可累积、可复用”的几何表示。

4. **生成式模型与显式 3D/4D 表示加速融合**
   AEON 在视频潜空间中生成 4D Gaussian Splatting，试图统一视频世界模型的真实感与 3D 世界模型的几何一致性；Latent Bridge 直接在视频生成潜空间与几何特征空间之间建桥，绕过 RGB 解码与重编码；MindView 则从评测端指出，十一个生成器在语言引导的多视图空间一致生成上仍有明显不足。这说明“视频生成潜空间 + 显式几何表示”正成为世界模型的一条主路线，同时评测缺口也被同步暴露。

5. **仿真就绪与物理一致性成为 3D 资产的新验收标准**
   SceneRig 强调仅视觉相似不够，必须在物理仿真器中通过编辑—验证循环达到物理稳定；AutoPhyX 用文本条件预测空间变化物理属性，并指出纯视觉输入存在“橡胶刚度不可辨”的固有歧义；AirPlayground 为 3DGS 环境对齐碰撞几何并自动采集飞行演示。三篇论文共同把“物理可仿真、参数可接地”推为场景重建的前置条件，而不仅是下游后处理。

#### 技术路线观察

**几何基础模型方向**
- 效率路线：BlazeVGGT 是免训练、即插即用的稀疏化，不更新参数，靠相机 token 相似性与贪心 DPP 选择互补视图，路线偏“推理期加速”。
- 建模路线：DewHand 用单阶段统一模型加 flow matching 处理遮挡与尺度歧义，路线偏“用生成式建模吸收不确定性”。
- 可靠性路线：VeriCalib 走结构化协方差与两级外参补偿，路线偏“估计理论 + 可诊断性”，与前两者的“性能导向”形成互补。
- 三者的共同点是都不再孤立优化某一指标，而是分别从计算、不确定性建模和结果可验证性切入几何基础模型的实际可用性。

**3D/4D 重建方向**
- 稀疏视角 NeRF 侧，DriftNeRF 把问题归因到渲染损失逐射线独立、缺少跨射线密度一致性，用漂移场正则项补目标函数缺口，属于“诊断—正则化”路线。
- 单目动态重建侧，RayCo4D 显式分离视觉测量与潜在 3D 运动状态，用 SE(3) 节点加白噪声加速度先验做连续时间插值，再用局部残差捕捉非刚性形变，属于“连续状态空间建模”路线。
- 单图到仿真场景侧，SceneRig 把几何、视觉、物理工具组合成智能体编辑—验证循环，属于“工具编排 + 物理闭环”路线。
- 三条路线分别对应：改进优化目标、改进运动表示、改进重建后处理与物理落地。

**神经场景表示方向**
- 压缩与容量分配是主线：ClunoGS 用语义感知稀疏化与向量量化统一优化，KoalaGS 用图像复杂度先验引导高斯重定位与重要性评分，二者都把“哪些基元保留容量”作为核心问题，但切入点分别是语义监督与图像复杂度先验。
- 语义化是第二条主线：AOV-GS 与 CoGaussian 都用冻结基础模型（SAM/CLIP）赋予高斯开放词汇语义，前者面向主动建图，后者面向多智能体协同，说明高斯表示的语义层正从离线标注转向基础模型对齐。
- 可编辑性是第三条主线：变化检测论文用 3DGS 自动编辑生成带标签训练视图，KoalaGS 的 LoD 也隐含编辑/裁剪需求，3DGS 正被当作可编程场景资产使用。

**机器人/AR 应用方向**
- 表示轻量化：RangeNav 明确定位“内存沉重点云编码器不适合大规模并行 RL 仿真”，选择距离图像与各向异性卷积；GeoMem-VLA 选择几何 token 而非完整重建；COWBOY 用局部 RL 专家复用而非全场景 RL。
- 数据规模化：AirPlayground 提供 94K 演示与 46.5M 同步样本，COWBOY 强调零样本迁移到数百物体，说明该方向瓶颈正从算法转向“可规模化训练/评测基础设施”。
- 评测缺口：MindView 显示生成式多视图空间智能仍有较大提升空间，并指出扩展上下文下所有被测生成器得分下降，提示现有模型对额外多视图证据利用不足。

#### 值得优先阅读的论文

1. **BlazeVGGT（2610.29454）**
   理由：免训练、即插即用、给出 2000 帧约 13 倍加速且 Chamfer Distance 从 0.41 降至 0.32 的具体数字，方法动机（相机 token 先拓扑后几何）清晰，对长序列几何基础模型的推理成本问题有直接复用价值，且不依赖重新训练，验证成本低。

2. **GeoMem-VLA（2610.29866）**
   理由：其核心论点“动作生成需要紧凑、可更新的几何抽象而非完整重建”对本批多篇具身论文具有统摄性，且训练用冻结几何基础模型监督几何 token、推理不调用教师模型的设计，是理解几何基础模型如何进入 VLA 流水线的关键样本。

3. **ClunoGS（2610.30013）**
   理由：直击 Language 3DGS 的存储膨胀问题，并指出“仅按渲染质量剪枝会不可逆删除语义重要高斯”这一顺序压缩的结构性缺陷，统一约束目标与交替优化的设计对 3DGS 压缩与语义保持的交叉方向有代表性。

4. **AEON（2610.28631）**
   理由：同时触及视频世界模型与 3D 世界模型两条主线的融合，提出在视频潜空间生成 4DGS 的显式世界表示，并与 Latent Bridge 形成可对照的技术组合，适合作为判断“生成式

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-22T13:07:28-04:00
**Total number of papers:** 69
**Number of papers added in the latest update:** 13
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

### 2026-10

#### 2026-10-21 - DewHand: Direct Metric World-Space Hand Motion Reconstruction from Egocentric Videos

**Authors:** Naru Suzuki, Satoshi Ikehata, Takehiko Ohkawa, Yoichi Sato, Shuhei Kurita
**Links:** [abs](https://arxiv.org/abs/2610.29936) - [pdf](https://arxiv.org/pdf/2610.29936)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Dynamic / 4D Reconstruction
**Matched keywords:** VGGT, motion reconstruction, motion trajectories, SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DewHand: Direct Metric World-Space Hand Motion Reconstruction from Egocentric Videos
- 作者：Naru Suzuki, Satoshi Ikehata, Takehiko Ohkawa, Yoichi Sato, Shuhei Kurita
- 出版日期：2026-10-21T16:08:38Z
- 分类：主分类 Geometry Foundation Models；次分类 Dynamic / 4D Reconstruction
- 链接：abstract_url: https://arxiv.org/abs/2610.29936；pdf_url: https://arxiv.org/pdf/2610.29936

### 一句话总结
DewHand 提出一个单阶段统一模型，从第一视角视频直接联合重建世界坐标系中的手部与相机运动，并借助场景几何特征、度量监督与流匹配生成式建模应对尺度歧义及遮挡/出视野问题。

### 研究问题
论文关注从第一视角视频恢复度量世界空间中的手部运动，以支持理解人类交互并迁移到具身智能体。摘要指出三项挑战：
1. 多阶段流程会传播来自独立估计的手部运动与相机运动的误差；
2. 单目观测导致物理尺度歧义；
3. 遮挡与手部出视野会带来多种可能运动轨迹。
摘要还指出，该任务需要同时处理手部运动、相机运动、尺度以及遮挡/出视野下的不确定性。

### 核心思路/方法
- 采用单阶段统一模型，在共享世界坐标系中联合预测手部运动与相机运动，以避免多阶段估计的误差累积。
- 为缓解度量尺度歧义，结合来自 VGGT-$Ω$ 的场景级几何特征与度量空间监督；同时使用手部特定特征保留细粒度关节运动。
- 将重建表述为带 flow matching 的条件运动生成，以处理遮挡和出视野手部；摘要称在同一架构下，该生成式形式仅用两步采样即在准确性和时间平滑性上优于直接回归。
- 摘要提到在 HOT3D 与 ARCTIC 上实验，并报告相对 StableHand 的刚性对齐世界空间误差从 32.9 mm 降至 28.4 mm（HOT3D），从 76.2 mm 降至 36.2 mm（ARCTIC）；在 HOT3D 上三分之二片段相机尺度恢复误差在 10% 以内，而 SLAM 约为四分之一。零样本评估在 HoloAssist、H2O、TACO 上均取得最低刚性对齐世界空间误差（WA-MPJPE）。

### 主要贡献
- 提出 DewHand，一个用于从第一视角视频直接联合重建世界空间手部与相机运动的统一单阶段模型。
- 针对度量尺度歧义，结合场景级几何特征与度量空间监督，并保留手部细粒度特征。
- 将遮挡与出视野下的手部重建建模为条件运动生成，使用 flow matching，并报告仅两步采样即可优于直接回归。
- 在 HOT3D 与 ARCTIC 上报告世界空间准确性与时间一致性优于现有方法，并给出具体误差与相机尺度恢复指标。
- 在 HoloAssist、H2O、TACO 上报告零样本评估取得最低 WA-MPJPE。

### 局限性
摘要未提供足够信息说明方法局限性、失败场景、计算成本、对特定数据或设备的依赖、生成式建模的潜在风险，以及各模块的消融细节。摘要也未提供训练数据规模、推理速度、超参数敏感性或更细粒度的实验设置。

### 阅读优先级
高。理由：该论文直接针对第一视角世界空间手部运动重建中的误差累积、度量尺度歧义与遮挡/出视野三项核心挑战，提出单阶段联合重建与生成式建模思路；摘要给出了明确的定量改进、跨数据集零样本结果，并与几何基础模型分类相关，具备较强的问题针对性与方法参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering metric world-space hand motion from egocentric video supports understanding human interactions and transferring them to embodied agents. Three challenges complicate this task: multi-stage pipelines propagate errors from independently estimated hand and camera motion; monocular observations leave physical scale ambiguous; and occlusion and out-of-view hands admit multiple plausible motion trajectories. We present DewHand, a unified model for direct joint reconstruction of world-space hand and camera motion. To avoid compounding errors from multi-stage estimation, DewHand jointly predicts hand and camera motion in a shared world coordinate system within a single-stage pipeline. To resolve metric-scale ambiguity, it combines scene-level geometric features from VGGT-$Ω$ with metric-space supervision, while hand-specific features preserve fine-grained articulation. To handle occlusion and out-of-view hands, we formulate reconstruction as conditional motion generation with flow matching. Under the same architecture, this generative formulation outperforms direct regression in both accuracy and temporal smoothness with only two sampling steps. Experiments on HOT3D and ARCTIC demonstrate improved world-space accuracy and temporal consistency over state-of-the-art methods. DewHand reduces rigid-aligned world-space error relative to StableHand from 32.9 to 28.4 mm on HOT3D and from 76.2 to 36.2 mm on ARCTIC. It also recovers camera scale within 10% on two thirds of HOT3D clips, versus about a quarter for SLAM. Moreover, in zero-shot evaluations on HoloAssist, H2O, and TACO, captured with different devices, DewHand achieves the lowest rigid-aligned world-space error (WA-MPJPE) on each dataset.

</details>

#### 2026-10-21 - GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models

**Authors:** Qinfan Zhang, Yifan Luo, Haoyuan Shi, Guanlin Liu, Han Dong, Haozhe Shan, Yong Dai, Xiangcong Ren, Xiaozhu Ju
**Links:** [abs](https://arxiv.org/abs/2610.29866) - [pdf](https://arxiv.org/pdf/2610.29866)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** geometry foundation model, point map, 3D reconstruction, manipulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models
- 作者：Qinfan Zhang, Yifan Luo, Haoyuan Shi, Guanlin Liu, Han Dong, Haozhe Shan, Yong Dai, Xiangcong Ren, Xiaozhu Ju
- 出版日期：2026-10-21T15:23:18Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.29866) / [PDF](https://arxiv.org/pdf/2610.29866)

### 一句话总结
GeoMem-VLA 将显式 3D 几何监督内化到可学习的几何 token 中，并作为时间记忆用于动作生成，使推理阶段无需调用 3D 教师模型或显式重建场景。

### 研究问题
摘要指出，几何结构对机器人操作和理解 3D 世界至关重要；多数 VLA 模型依赖当前观测的 2D 表示，而几何感知方法往往需要额外 3D 信息。与此同时，从单次观测独立推断的几何通常被丢弃，未能累积为持续的任务表示。论文要解决的问题是：如何让动作生成获得紧凑、任务相关且可持续更新的几何抽象，而不是每一步都依赖完整可渲染的 3D 重建。

### 核心思路/方法
论文提出 GeoMem-VLA 框架，将显式 3D 监督内化到专门的几何 token 中，并把这些 token 维护为用于动作生成的时间记忆。其做法不是直接将 VLM 原生视觉嵌入与教师特征空间对齐。

训练阶段，冻结的几何基础模型通过几何流匹配目标监督可学习的 GeoPlan token；该目标定义在当前场景点图和未来末端执行器轨迹上。这些 token 与观测表示的记忆集成：历史信息被检索、与当前观测自适应融合，并随着任务推进进行整合，以保留事件帧。

推理阶段，策略检索历史表示，并将其与当前工作表示融合以预测动作，不调用 3D 教师模型，也不显式重建场景。摘要还提到，方法经过基准特定的下游适配后取得相应结果。

### 主要贡献
- 提出 GeoMem-VLA，将显式 3D 监督内化为几何 token，并作为时间记忆用于 VLA 动作生成。
- 设计以冻结几何基础模型监督可学习 GeoPlan token 的训练机制，监督目标为当前场景点图与未来末端执行器轨迹上的几何流匹配。
- 将几何 token 与观测表示记忆结合，支持历史信息检索、与当前观测的自适应融合及任务推进中的记忆整合。
- 推理阶段无需调用 3D 教师模型或显式重建场景。
- 摘要报告的结果：经基准特定下游适配后，LIBERO 平均成功率 98.9%；RoboTwin 干净/随机化设置分别为 91.10% / 91.24%；五个真实世界任务平均成功率 78.0%。

### 局限性
- 摘要未提供足够信息说明几何流匹配目标的具体形式、网络结构、训练数据规模与训练成本。
- 摘要未提供足够信息说明“基准特定下游适配”的具体做法及其对各结果的影响程度。
- 摘要未提供足够信息说明时间记忆的容量、更新频率、遗忘机制及长时序任务中的表现。
- 摘要未提供足够信息说明与基线方法的完整对比、消融实验和失败案例分析。
- 摘要未提供足够信息说明真实世界五个任务的具体设置、评价协议与统计显著性。
- 摘要未提供足够信息说明方法对几何基础模型质量、传感器噪声或视角变化的敏感性。

### 阅读优先级
中。理由：该论文聚焦 VLA 中 3D 几何理解的内化与时间记忆，问题定位清晰，且摘要给出了多个基准和真实任务的成功率结果；但当前仅有摘要与元数据，缺少方法细节、基线对比和消融信息。若读者关注机器人操作中的几何表示、时间记忆或 VLA 架构，值得进一步阅读全文；若仅需快速了解结论，摘要信息已较集中。

</details>

<details>
<summary>Abstract</summary>

Geometric structure is essential for robotic manipulation and understanding the 3D world. Most VLA models rely on 2D representations of current observations, while geometry-aware approaches often require additional 3D information. However, geometry inferred independently from individual observations is often discarded rather than accumulated into a persistent task representation. Our key insight is that action generation needs a compact, task-relevant geometric abstraction that can be continuously updated, rather than a complete, renderable 3D reconstruction at every step. We introduce GeoMem-VLA, a VLA framework that internalizes explicit 3D supervision into dedicated geometric tokens and maintains them as temporal memory for action generation, without directly aligning the VLM's native visual embeddings with the teacher feature space. During training, a frozen geometry foundation model supervises learnable GeoPlan tokens through a geometric flow-matching objective over the current scene point map and future end-effector tracks. These tokens are integrated with the memory of observation representations, where historical information is retrieved, adaptively fused with current observations, and consolidated to retain event frames as the task progresses. At inference, the policy retrieves historical representations and fuses them with the current working representation to predict actions, without invoking the 3D teacher or explicitly reconstructing the scene. After benchmark-specific downstream adaptation, GeoMem-VLA achieves 98.9% average success on LIBERO and 91.10% / 91.24% on RoboTwin's clean/randomized settings. Across five real-world tasks, GeoMem-VLA achieves 78.0% average success. These results suggest that internalizing and remembering 3D scene understanding is a promising approach to robot control.

</details>

#### 2026-10-21 - BlazeVGGT: 13x Faster VGGT at 2,000 Frames via Camera Token without Training

**Authors:** Shujun Yao, Junhui Lin, Congying Han, Tiande Guo, Ziwen Liu, Bonan Li
**Links:** [abs](https://arxiv.org/abs/2610.29454) - [pdf](https://arxiv.org/pdf/2610.29454)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, multi-view reconstruction, camera pose estimation, pose estimation, point cloud reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BlazeVGGT: 13x Faster VGGT at 2,000 Frames via Camera Token without Training
- 作者：Shujun Yao, Junhui Lin, Congying Han, Tiande Guo, Ziwen Liu, Bonan Li
- 出版日期：2026-10-21T09:11:19Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.29454 ；PDF https://arxiv.org/pdf/2610.29454

### 一句话总结
BlazeVGGT 提出一种无需训练的即插即用方法，利用 VGGT 相机 token 的相似性做视图级键值稀疏化，在保留全部帧作为查询的同时减少跨视图冗余计算，摘要称在 2,000 帧时推理约快 13 倍，并将 Chamfer Distance 从 0.41 降至 0.32。

### 研究问题
摘要指出，以 VGGT 为代表的前馈视觉几何模型通过稠密全局注意力实现多视图重建，但全对全跨视图计算随输入视图数量呈二次增长；由于高度重叠观测之间存在显著帧级冗余，长序列推理成本尤其高。论文关注的问题是如何在不训练、不更新参数的前提下，降低 VGGT 长序列推理中的冗余跨视图计算。

### 核心思路/方法
- 观察：摘要称 VGGT 相机 token 呈现“先拓扑、后几何”的演化，浅层 token 能可靠捕获局部视图邻域，深层 token 逐步编码全局组织的视图间几何。
- 方法：提出 BlazeVGGT，一种无需训练的结构感知帧级 key–value 稀疏化框架。
- 具体机制：在每个全局注意力块中，基于相机 token 关系构建视图级相似性核，并使用贪心行列式点过程（DPP）推断选择一组相互补充的紧凑视图。
- 注意力设计：被选视图构成 key–value 上下文，而所有输入帧保留为 query，形成非对称注意力，以维持稠密的逐帧预测并消除冗余跨视图计算。
- 集成方式：可直接作为即插即用模块集成到预训练 VGGT 中，无需参数更新。

### 主要贡献
- 揭示 VGGT 相机 token 的“拓扑优先、几何随后”演化现象，并据此设计帧级稀疏化。
- 提出无需训练的 BlazeVGGT，通过相机 token 相似性与贪心 DPP 选择互补视图，构建非对称 key–value 注意力。
- 摘要报告在 2,000 帧时相比 VGGT 推理约快 13 倍，Chamfer Distance 从 0.41 降至 0.32。
- 摘要称实验覆盖点云重建与相机位姿估计的精度—效率权衡，并与 FastVGGT、LiteVGGT 等现有加速器兼容，且可迁移到 StreamVGGT 和 PAGE-4D 等基于 VGGT 的模型。
- 代码已公开。

### 局限性
- 摘要未提供足够信息说明方法在非高度重叠视图、极端视角变化或不同序列长度下的具体表现边界。
- 摘要未提供足够信息说明贪心 DPP 选择带来的额外计算开销及其对端到端加速比的影响。
- 摘要未提供足够信息说明在更多数据集、更多基线或完整消融实验中的细节。
- 摘要未提供足够信息说明方法对相机 token 质量或 VGGT 特定结构的依赖程度。
- 摘要未提供足够信息说明与 FastVGGT、LiteVGGT 组合时的具体加速与精度数值。

### 阅读优先级
高。理由：该论文直接针对 VGGT 类前馈视觉几何模型长序列推理的二次复杂度瓶颈，提出无需训练、即插即用的加速方案，并给出 2,000 帧约 13 倍加速及 Chamfer Distance 改善的摘要级结果；若关注多视图重建、3D 重建效率或 VGGT 加速，具有较高阅读价值。但具体实验细节与局限性需以全文为准。

</details>

<details>
<summary>Abstract</summary>

Feed-forward visual geometry models, exemplified by VGGT, have demonstrated strong multi-view reconstruction capabilities through dense global attention. However, the resulting all-to-all cross-view computation scales quadratically with the number of input views, making long-sequence inference particularly expensive due to substantial frame-level redundancy among highly overlapping observations. We uncover a topology-first, geometry-later evolution in VGGT camera tokens: shallow-layer tokens reliably capture local view neighborhoods, whereas deeper-layer tokens progressively encode globally organized inter-view geometry. Motivated by this observation, we introduce BlazeVGGT, a training-free framework for structure-aware frame-level key--value sparsification. At each global-attention block, BlazeVGGT constructs a view-level similarity kernel from camera-token relations and employs greedy determinantal point process inference to select a compact set of mutually complementary views. The selected views constitute the key--value context, while all input frames are retained as queries. This asymmetric attention design preserves dense per-frame predictions while eliminating redundant cross-view computation, allowing our method to be directly integrated into pretrained VGGT as a plug-and-play module without parameter updates. Its advantages become increasingly pronounced with sequence length: at 2,000 frames, BlazeVGGT achieves approximately 13$\times$ faster inference than VGGT while reducing the Chamfer Distance from 0.41 to 0.32. Extensive experiments demonstrate a favorable accuracy--efficiency trade-off in point-cloud reconstruction and camera-pose estimation, compatibility with existing VGGT accelerators such as FastVGGT and LiteVGGT, and transferability to VGGT-based models including StreamVGGT and PAGE-4D. Codes are publicly available at https://github.com/MagiciannnY/BlazeVGGT.git.

</details>

#### 2026-10-20 - EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation

**Authors:** Diwen Liu, Yiyang Shao, Borui Wang, Chi Zhang, Yunhui Liu
**Links:** [abs](https://arxiv.org/abs/2610.27616) - [pdf](https://arxiv.org/pdf/2610.27616)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation
- 作者：Diwen Liu, Yiyang Shao, Borui Wang, Chi Zhang, Yunhui Liu
- 出版日期：2026-10-20T04:31:18Z
- 分类：主分类 Geometry Foundation Models；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.27616 ；PDF https://arxiv.org/pdf/2610.27616

### 一句话总结
EchoNav 通过短 RGB 序列预测具有证据置信度的 BEV 占据表示，并结合历史残差提议完成遮挡区域的结构恢复，用于杂乱环境中的视觉导航。

### 研究问题
论文关注杂乱环境中的视觉导航问题：机器人需要恢复先前观察到的结构，并推断仍被遮挡的障碍物与可通行空间。摘要指出，该任务要求从短 RGB 序列中获得具有时序聚合和占据补全能力的表示，以支持后续导航。

### 核心思路/方法
- 使用短 RGB 序列预测具有证据（evidential）形式的鸟瞰图（BEV）表示，将时序聚合与占据补全结合。
- 解码器适配冻结的 VGGT-Omega 特征，并结合历史残差提议，通过逐单元权重和可学习的“不更新”选项进行融合。
- BEV 预测器在最新自车坐标系下生成局部地图，摘要明确说明其不使用深度或相机位姿输入，也不进行显式几何变换。
- 证据模型将已观测自由空间单独处理，并在其余支持区域内预测占据及其关联置信度。
- 训练使用模拟 RGB 序列，并配对完整占据标注与可见性掩码占据标注。

### 主要贡献
- 提出一种从历史观测进行证据 BEV 补全的框架，用于视觉导航中的遮挡结构与障碍/自由空间推断。
- 设计了解码器适配冻结 VGGT-Omega 特征，并通过逐单元权重与可学习“不更新”选项融合历史残差提议。
- 在不使用深度、相机位姿输入或显式几何变换的条件下，从短 RGB 序列预测最新自车坐标系下的局部 BEV 地图。
- 采用证据建模，将已观测自由空间与其余支持区域的占据预测及置信度分开处理。
- 摘要报告了仿真与轮式机器人实验，并提及其他机器人平台的演示；在模拟顺序双目标导航中达到 89.6% 成功率，比最强评估基线高 32.5 个百分点；在 20 个场景的 60 次轮式机器人试验中成功率为 73.3%，最强评估基线为 33.3%。

### 局限性
- 摘要未提供足够信息说明方法在非模拟训练数据上的泛化能力。
- 摘要未提供足够信息说明失败案例、计算开销、实时性或在更复杂动态环境中的表现。
- 摘要未提供足够信息说明“最强评估基线”的具体方法构成与对比公平性细节。
- 摘要未提供足够信息说明四足与类人机器人演示的具体规模与定量结果。

### 阅读优先级
中。理由：论文主题与几何基础模型、BEV 表示和视觉导航相关，摘要给出了明确的性能提升；但当前仅有摘要与元数据，缺少方法细节、基线定义和实验设置，适合在需要了解证据 BEV 补全与历史观测融合导航思路时进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Visual navigation in cluttered environments requires robots to recover previously observed structure and infer obstacles and free space that remain occluded. We present a framework that combines temporal aggregation and occupancy completion in an evidential bird's-eye-view (BEV) representation predicted from short RGB sequences. A decoder adapts frozen VGGT-Omega features and combines historical residual proposals using cellwise weights and a learned no-update option. The BEV predictor produces a local map in the latest ego frame without depth or camera-pose inputs or explicit geometric warping. The evidential model treats observed free space separately and predicts occupancy with associated confidence across the remaining supported region. We train the predictor on simulated RGB sequences paired with complete and visibility-masked occupancy annotations. Our experiments evaluate navigation in simulation and on a wheeled robot, with additional demonstrations on quadruped and humanoid robots. In simulated sequential two-goal navigation, our system achieves 89.6% success, outperforming the strongest evaluated baseline by 32.5 percentage points. Across 60 wheeled-robot trials in 20 scenes, it achieves 73.3% success, compared with 33.3% for the strongest evaluated baseline.

</details>

#### 2026-10-18 - ReDT: Resolution-Decoupled Visual Geometry Transformer

**Authors:** Abteen Arab, Guile Wu, Dongfeng Bai
**Links:** [abs](https://arxiv.org/abs/2610.25517) - [pdf](https://arxiv.org/pdf/2610.25517)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, multi-view reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReDT: Resolution-Decoupled Visual Geometry Transformer
- 作者：Abteen Arab, Guile Wu, Dongfeng Bai
- 出版日期：2026-10-18T20:17:29Z
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.25517) / [PDF](https://arxiv.org/pdf/2610.25517) / [项目网站](https://redt.github.io)

### 一句话总结
ReDT 是一种前馈视觉几何 Transformer，通过将多视图重建的内部注意力表示与输入分辨率解耦，使高分辨率（HD/2K）多视图重建在质量和计算效率上均优于现有方法。

### 研究问题
现有视觉几何 Transformer 通常在固定标准定义（SD）分辨率上训练，面对高输入分辨率时重建质量下降、计算扩展性差。已有高效架构主要降低帧间注意力复杂度，但帧内注意力与编码器注意力的高昂开销仍未解决，导致 HD 重建在现有架构下不切实际。

### 核心思路/方法
ReDT 的核心是分辨率解耦：先将每个视图映射为固定大小的基元 token 集合，在这个紧凑、恒定大小的基元空间中计算对应关系，再将输出投影回原始分辨率进行稠密预测。由于注意力阶段的内部表示与输入分辨率解耦，高分辨率 3D 重建的计算成本大幅降低，同时模型在各分辨率下的性能得到改善。

### 主要贡献
- 提出 ReDT，一种面向高分辨率输入扩展的前馈视觉几何 Transformer。
- 通过固定大小基元 token 空间进行对应计算，解耦内部表示与输入分辨率，缓解帧内与编码器注意力的高开销。
- 在 SD 到 FHD（2K）的多个数据集上取得优于现有视觉几何 Transformer 的重建质量与计算效率。
- 摘要给出的具体结果：在 ETH3D（2K）上相对 VGGT-$Ω$ 实现 $16\times$ 加速、峰值 GPU 内存降低 $34\%$、chamfer distance 降低 $33\%$。

### 局限性
摘要未提供足够信息。未说明方法在极低分辨率、稀疏视图、动态场景或训练数据分布外场景下的表现；未提供消融实验细节、失败案例或计算成本的具体测量条件。

### 阅读优先级
高。理由：该工作直接针对视觉几何 Transformer 在高分辨率多视图重建中的计算瓶颈，提出分辨率解耦的架构思路，并在摘要中给出明确的效率与精度改进数据，与 3D 重建和多视图几何方向高度相关。

</details>

<details>
<summary>Abstract</summary>

We introduce ReDT, a feed-forward visual geometry transformer designed to scale multi-view reconstruction to high-definition (HD) inputs. Existing visual geometry transformers are typically trained at fixed, standard definition (SD) resolutions and exhibit degraded reconstruction quality and poor computational scaling to high input resolutions. While recent efficient architectures reduce the complexity of inter-frame attention, expensive intra-frame and encoder attention remain largely unaddressed, making HD reconstruction impractical with existing architectures. ReDT addresses both limitations with a resolution-aware architecture designed to scale to high-resolution inputs. The key idea of ReDT is to first map each view to a fixed-size set of basis tokens, compute correspondences in this compact constant-size basis space, and then project the outputs back to the original resolution for dense prediction. By decoupling the internal representation from input resolution during attention, ReDT substantially reduces the computational cost of high-resolution 3D reconstruction and improves model performance at all resolutions. Extensive experiments on multiple datasets spanning SD to FHD (2K) show that ReDT outperforms state-of-the-art visual geometry transformers in both reconstruction quality and computational efficiency. For instance, on the ETH3D (2K) dataset, ReDT achieves a $16\times$ speedup, a $34\%$ reduction in peak GPU memory usage, and a $33\%$ reduction in chamfer distance over VGGT-$Ω$. \href{https://redt.github.io}{Project Website.}

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-20 - AEON: Unifying Video and 3D World Models

**Authors:** Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou
**Links:** [abs](https://arxiv.org/abs/2610.28631) - [pdf](https://arxiv.org/pdf/2610.28631)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, 4D Gaussian, Gaussian Splatting, rendering, splatting, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AEON: Unifying Video and 3D World Models
- 作者：Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou
- 出版日期：2026-10-20T17:59:51Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.28631)｜[PDF](https://arxiv.org/pdf/2610.28631)｜[项目页](https://weiqi-zhang.github.io/AEON)

### 一句话总结
AEON 提出一个统一视频生成式世界模型与 3D 生成式世界模型的框架，在文本或图像条件视频潜空间中生成可渲染的 4D Gaussian Splatting（4DGS）作为显式世界表示，以兼顾真实感与 3D 一致性。

### 研究问题
摘要指出，当前面向显式世界模拟的世界模型主要沿两条路径发展：（1）视频生成模型（如 Sora）能模拟真实外观，但无法保持 3D 一致性；（2）3D 生成模型（如 Marble）能生成几何一致的场景，但往往产生静态、真实感较弱的观测。论文旨在弥合这两类世界模型，并结合二者优势。

### 核心思路/方法
AEON 的关键思路是构建一个生成模型，使其在文本或图像条件视频的潜空间中运行，同时产可渲染的 4D 图形基元，具体为 4D Gaussian Splatting（4DGS），作为显式世界表示。方法上包括：
- 训练一个 4D 重建模型，从单目视频中预测 4DGS 与相机位姿，作为初始化的 4D 解码器；
- 设计域适配器，通过在视频 VAE 上的蒸馏过程，将生成式视频潜变量转换为重建式 4D 潜变量；
- 通过在预测的相机轨迹上渲染 4DGS，自然支持基于视频的世界建模，并构建具有场景动态的持久 4D 环境。

### 主要贡献
基于摘要可确认的贡献包括：
- 提出统一框架 AEON，桥接基于视频与基于 3D 的世界模型，结合两者优势；
- 在条件视频潜空间中生成可渲染的 4DGS 显式世界表示；
- 训练单目视频的 4D 重建模型以预测 4DGS 和相机位姿，并作为 4D 解码器初始化；
- 设计域适配器，通过视频 VAE 上的蒸馏将生成式视频潜变量转为重建式 4D 潜变量；
- 支持基于视频的世界建模与具有场景动态的持久 4D 环境构建，并在标准基准上取得摘要所称的 state-of-the-art 性能。

### 局限性
摘要未提供足够信息。摘要仅给出高层方法与性能声明，未说明具体实验设置、基准名称、评价指标、失败情形、计算开销或适用范围限制，因此无法基于给定内容可靠总结局限性。

### 阅读优先级
中。理由：该论文涉及视频世界模型与 3D/4D 显式表示的融合，主题与 Dynamic / 4D Reconstruction、神经场景表示与渲染、具身/机器人/AR 应用相关，问题定位清晰；但摘要未提供实验细节与定量结果，是否值得深入阅读需结合全文的实验严谨性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consistency; and (2) 3D generative models (e.g., Marble), which generate geometrically consistent scenes but often yield static, less realistic observations. We present AEON, a unified framework that bridges video-based and 3D-based world models and combines the benefits of both. The key insight of AEON lies in a generative model that operates within the text- or image-conditioned video latent space while producing renderable 4D graphics primitives---specifically, 4D Gaussian Splatting (4DGS)---as the explicit world representation. We train a 4D reconstruction model to predict both 4DGS and camera poses from monocular videos, serving as our initialized 4D decoder. Furthermore, we design a domain adapter that translates generative video latents into reconstructive 4D latents through a distillation process on the video VAE. AEON naturally supports video-based world modeling by rendering 4DGS at predicted camera trajectories, and constructs a persistent 4D environment with scene dynamics for realistic world simulation. Consequently, AEON empowers a diverse range of world modeling applications and achieves state-of-the-art performance on standard benchmarks. Project Page: https://weiqi-zhang.github.io/AEON

</details>

#### 2026-10-20 - RayCo4D: Ray-Conditioned Continuous Motion Model for Monocular 4D Dynamic Reconstruction

**Authors:** Yuanxiang Ni, Xianliang Huang, Ruihan Hou, Feng Xie, Hao Zhang
**Links:** [abs](https://arxiv.org/abs/2610.28351) - [pdf](https://arxiv.org/pdf/2610.28351)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic reconstruction, dynamic 3D, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RayCo4D: Ray-Conditioned Continuous Motion Model for Monocular 4D Dynamic Reconstruction
- 作者：Yuanxiang Ni, Xianliang Huang, Ruihan Hou, Feng Xie, Hao Zhang
- 出版日期：2026-10-20T15:17:29Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.28351 ；PDF https://arxiv.org/pdf/2610.28351

### 一句话总结
RayCo4D 提出一种以射线为条件的连续运动模型，用于单目视频的动态 4D 重建，核心是把图像与深度观测同潜在 3D 运动状态显式分离，并借助长时间断断续续的轨迹约束共享的连续运动序列。

### 研究问题
论文针对从单目视频重建动态 3D 场景的问题：运动需要从有噪声、间歇可见的观测中推断。摘要指出，长距离轨迹能提供有价值的几何约束，但如何把其碎片化的时间覆盖整合进共享、连续的运动表示仍然困难。摘要未提供足够信息来说明现有方法在具体误差类型或失败模式上的量化表现。

### 核心思路/方法
- 显式分离视觉测量与潜在 3D 运动状态：每条轨迹关联一个参考时刻的 3D 查询，该查询被约束在其相机射线上；轨迹的图像与深度观测通过局部多对多关联约束共享的潜在运动节点。
- 运动节点表示：每个节点在稀疏支撑时刻维护一个 SE(3) 位姿与体坐标系速度。
- 连续时间建模：采用加速度白噪声过程先验耦合相邻状态，并定义连续时间插值，使不同可见区间内的观测能共同约束同一潜在状态序列。
- 运动传递与细节补偿：推断出的共享运动通过双四元数混合传递到高斯基元；同时以参考锚定的局部 SE(3) 残差捕捉共享骨架之外的细尺度非刚性形变。
- 摘要提到支持连续时间渲染，但未给出具体渲染管线或实现细节。

### 主要贡献
- 提出 RayCo4D，一种射线条件化的连续运动模型，用于单目 4D 动态重建。
- 将轨迹观测与潜在 3D 运动状态分离，并通过局部多对多关联让碎片化轨迹共同约束共享连续运动。
- 使用带加速度白噪声先验的 SE(3) 状态序列与连续时间插值，建模跨可见区间的共享运动。
- 通过双四元数混合将共享运动转移到高斯基元，并用参考锚定的局部 SE(3) 残差补充细尺度非刚性形变。
- 摘要称在多样单目动态场景上取得有竞争力的新视角合成质量，并在快速运动与不完整轨迹下改善结构与时序一致性，同时支持连续时间渲染；具体实验指标与对比数值摘要未提供足够信息。

### 局限性
摘要未提供足够信息来说明方法的局限性、失败场景、计算开销、对深度观测质量的敏感性或适用范围边界。摘要仅提及问题本身涉及噪声与间歇可见观测，但未明确列出 RayCo4D 的受限条件。

### 阅读优先级
中。理由：该论文聚焦单目 4D 动态重建中“碎片化长轨迹如何约束连续共享运动”这一明确问题，方法要素（射线条件查询、SE(3) 连续状态、双四元数混合、局部残差）与主分类和次分类均直接相关；但摘要未给出量化结果、对比基线细节与局限性，若需要判断实际性能或复现价值，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic 3D scenes from monocular video requires inferring motion from noisy and intermittently visible observations. Long-range tracks provide valuable geometric constraints, but integrating their fragmented temporal coverage into shared, continuous motion remains challenging. We introduce RayCo4D, a ray-conditioned continuous motion model for monocular 4D reconstruction that explicitly separates visual measurements from latent 3D motion states. Each track is associated with a reference-time 3D query constrained to its camera ray, and its image and depth observations constrain shared latent motion nodes through local many-to-many associations. Each node maintains an $\mathrm{SE}(3)$ pose and body-frame velocity at sparse support times. A white-noise-on-acceleration process prior couples neighboring states and defines continuous-time interpolation, allowing observations across visibility intervals to jointly constrain the same latent state sequence. The inferred shared motion is transferred to Gaussian primitives through dual-quaternion blending, while reference-anchored local $\mathrm{SE}(3)$ residuals capture fine-scale non-rigid deformation beyond the shared scaffold. Experiments on diverse monocular dynamic scenes show that RayCo4D achieves competitive novel-view synthesis quality, improves structural and temporal consistency under rapid motion and incomplete tracks, and supports continuous-time rendering.

</details>

#### 2026-10-20 - SplatFlux: Feed-Forward 4D Gaussian Reconstruction and Generation from Video Latents

**Authors:** Runmin Zhang, Binglin Ren, Zhu Yu, Fudong Wang, Jiangke Lin, Yichun Shentu, Si-Yuan Cao, Yi Yuan, Hui-Liang Shen
**Links:** [abs](https://arxiv.org/abs/2610.28257) - [pdf](https://arxiv.org/pdf/2610.28257)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic Gaussian, 4D Gaussian

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatFlux: Feed-Forward 4D Gaussian Reconstruction and Generation from Video Latents
- 作者：Runmin Zhang, Binglin Ren, Zhu Yu, Fudong Wang, Jiangke Lin, Yichun Shentu, Si-Yuan Cao, Yi Yuan, Hui-Liang Shen
- 出版日期：2026-10-20T14:12:53Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.28257) / [PDF](https://arxiv.org/pdf/2610.28257)

### 一句话总结
SplatFlux 提出一个前馈的“潜变量到 4D 高斯”框架，将基于视频的 4D 重建与条件 4D 生成统一为同一预训练视频潜空间中的解码任务。

### 研究问题
论文关注如何以紧凑且时间一致的方式，从视频潜表示出发，同时支持 4D 重建与条件 4D 生成。摘要指出，其关键观察是观测视频与条件生成内容可以表示在同一预训练视频潜空间中，因此两类任务都可被表述为 latent-to-4DGS 解码问题。

### 核心思路/方法
- 提出 SplatFlux，一个前馈的 latent-to-4DGS 框架，用于视频驱动的 4D 重建与条件 4D 生成。
- 引入静态-动态解耦的 4D 高斯表示，显式预测高斯基元的动态概率，从而分离静态场景结构与运动区域。
- 通过静态聚合与动态运动插值，以纯前馈方式完成完整 4D 场景构建。
- 为避免昂贵的标注，设计辅助蒸馏策略，提供伪动态掩码与光流线索，用于学习静态-动态分解及动态高斯运动。
- 摘要声称在 3D 与 4D 重建和生成任务上进行了广泛实验，并达到 state-of-the-art 性能。

### 主要贡献
- 统一视角：将视频 4D 重建与条件 4D 生成统一为同一预训练视频潜空间中的 latent-to-4DGS 解码任务。
- 表示设计：提出静态-动态解耦的 4D 高斯表示，显式预测高斯基元的动态概率，以构建紧凑且时间一致的 4D 场景。
- 前馈构建：通过静态聚合与动态运动插值，前馈完成 4D 场景构建。
- 无需昂贵标注的学习策略：提出辅助蒸馏策略，利用伪动态掩码与光流线索学习静态-动态分解和动态高斯运动。
- 实验层面：摘要称在 3D/4D 重建与生成上达到 state-of-the-art，但具体实验设置、数据集与指标摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法的具体失败情形或适用边界。
- 摘要未提供足够信息说明伪动态掩码与光流线索的质量对最终结果的影响程度。
- 摘要未提供足够信息说明计算开销、推理速度、显存需求等效率相关细节。
- 摘要未提供足够信息说明实验所用数据集、评价指标、基线方法与消融实验细节。
- 摘要未提供足够信息说明“state-of-the-art”结论的具体定量依据。

### 阅读优先级
中。理由：该论文将视频 4D 重建与条件 4D 生成统一到视频潜空间到 4D 高斯的解码框架，并引入静态-动态解耦表示与辅助蒸馏策略，主题与动态/4D 重建及神经场景表示相关，具备方法参考价值；但当前仅提供摘要与元数据，缺少实验细节、效率分析与局限性说明，是否值得深入阅读需待正文中的实验设置、定量结果和消融分析进一步确认。

</details>

<details>
<summary>Abstract</summary>

This work presents SplatFlux, a feed-forward latent-to-4DGS framework for both video-based 4D reconstruction and conditional 4D generation. Our key observation is that observed videos and conditionally generated content can be represented in the same pretrained video latent space, allowing both tasks to be formulated as latent-to-4DGS decoding. To construct compact and temporally coherent 4D scenes, SplatFlux introduces a static-dynamic decoupled 4D Gaussian representation that explicitly predicts dynamic probabilities for Gaussian primitives. This representation separates static scene structures from moving regions, enabling complete 4D scene construction in a feed-forward manner through static aggregation and dynamic motion interpolation. To learn static-dynamic decomposition and dynamic Gaussian motion without costly annotations, we further develop an auxiliary distillation strategy that provides pseudo dynamic masks and optical-flow cues. Extensive experiments across 3D and 4D reconstruction and generation demonstrate that SplatFlux achieves state-of-the-art performance.

</details>

#### 2026-10-20 - Causal Spatiotemporal State Evolution for Monocular 4D Reconstruction

**Authors:** Qiaowei Miao, Yijing Guo, Lipei Zhang, Qifeng Cheng, Yuru Xiao, Ziqian Ni, Sheng Yang
**Links:** [abs](https://arxiv.org/abs/2610.27594) - [pdf](https://arxiv.org/pdf/2610.27594)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, dynamic 4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Causal Spatiotemporal State Evolution for Monocular 4D Reconstruction
- 作者：Qiaowei Miao, Yijing Guo, Lipei Zhang, Qifeng Cheng, Yuru Xiao, Ziqian Ni, Sheng Yang
- 出版日期：2026-10-20T04:00:48Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2610.27594) / [PDF](https://arxiv.org/pdf/2610.27594)

### 一句话总结
该论文提出一种面向单目视频的前馈式因果 4D 视觉几何学习框架，通过具有方向性的时空状态传播与统一的运动监督来提升动态场景 4D 表示的时间一致性。

### 研究问题
论文针对单目动态 4D 场景重建中的两个问题：一是现有方法多采用无序时间聚合，缺乏物理时间的方向性结构；二是现有监督常将几何与运动视为彼此分离的目标，未利用二者的物理耦合，因而缺少统一约束来有效监督时间状态转移，导致 4D 场景表示不一致。

### 核心思路/方法
论文提出一个前馈框架，从单目视频学习因果 4D 视觉几何。核心组件包括：
- **Causal Spatiotemporal Mamba（CSM）**：在时间聚合中引入方向性状态传播，通过互补的 Temporal-Spatial 与 Spatial-Temporal Scans，使几何感知状态跨帧持续传播，以建模时空演化。
- **Unified Motion Supervision（UMS）**：不将运动作为独立目标，而是利用相机头与深度头的几何感知预测构建与底层 3D 结构一致的前向运动场，以该几何为基础显式约束帧间状态转移，促进跨帧稳定状态传播。

### 主要贡献
- 提出面向单目视频的因果 4D 视觉几何学习前馈框架。
- 设计 Causal Spatiotemporal Mamba，以方向性状态传播和互补扫描建模时空演化。
- 提出 Unified Motion Supervision，利用相机与深度预测构建统一前向运动场，对帧间状态转移施加几何一致的监督。
- 摘要称在动态基准上的视频深度、相机位姿与光流估计取得 state-of-the-art 表现，并显著减少时间漂移、增强时空一致性。

### 局限性
摘要未提供足够信息。包括具体实验设置、数据集细节、计算开销、失败案例、消融实验规模及与其他方法的定量对比细节，摘要均未提供足够信息。

### 阅读优先级
**中**。理由：论文主题聚焦单目动态 4D 重建中的因果时序建模与几何—运动联合监督，问题定位清晰，方法要点明确；但摘要未给出可核验的定量结果、实验细节与局限性信息，是否值得优先精读需结合全文实验部分进一步判断。

</details>

<details>
<summary>Abstract</summary>

While feed-forward models excel in static 3D geometry estimation, extending them to dynamic 4D scenes requires modeling visual geometry as a causally evolving state. Current methods typically rely on unordered temporal aggregation, which lacks the directional structure of physical time. Furthermore, existing supervision often treats geometry and motion as disjoint objectives, failing to exploit their inherent physical coupling. Consequently, they lack a unified constraint to effectively supervise temporal state transitions, leading to inconsistent 4D scene representations. To address this, we propose a feed-forward framework for causal 4D visual geometry learning from monocular videos. At its core, Causal Spatiotemporal Mamba augments temporal aggregation with directional state propagation. Through complementary Temporal-Spatial and Spatial-Temporal Scans, CSM continuously propagates geometry-aware states across frames to model spatiotemporal evolution. To align this causal state evolution with observable dynamics, we introduce Unified Motion Supervision. Rather than treating motion as an independent objective, UMS leverages geometry-aware predictions from the camera and depth heads to construct a unified forward motion field that is consistent with the underlying 3D structure. This geometry-grounded supervision explicitly constrains inter-frame state transitions, enabling stable states propagation across frames. Extensive evaluations on dynamic benchmarks demonstrate state-of-the-art performance across video depth, camera pose, and optical flow estimation. These results validate that the synergy between the directional state propagation of Causal Spatiotemporal Mamba and Unified Motion Supervision effectively captures continuous scene evolution, significantly reducing temporal drift and reinforcing spatial-temporal consistency in 4D representation learning.

</details>

#### 2026-10-19 - Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos

**Authors:** Tong Zhao, Zhiyuan Han, Lin Chen, Bowen Xie, Yunxi Qiao, Bohan Li, Weiqing Xiao, Gen Li, Shu Han, Xuyang Dai, Cheng Bi, Hao Zhao, Chaojian Li
**Links:** [abs](https://arxiv.org/abs/2610.26585) - [pdf](https://arxiv.org/pdf/2610.26585)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** metric depth, dynamic 4D, 4D Gaussian, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos
- 作者：Tong Zhao, Zhiyuan Han, Lin Chen, Bowen Xie, Yunxi Qiao, Bohan Li, Weiqing Xiao, Gen Li, Shu Han, Xuyang Dai, Cheng Bi, Hao Zhao, Chaojian Li
- 出版日期：2026-10-19T15:34:28Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.26585；PDF https://arxiv.org/pdf/2610.26585

### 一句话总结
Drive2Gauss 提出一种前馈框架，将从参考多视角图像与未来控制信号联合生成的 RGB、度量深度和动态流转换为动态 4D 高斯场景，从而避免逐序列优化。

### 研究问题
生成可复用的驾驶环境需要：既可控制未来观测，又要有支持不同视角渲染的显式表示。然而现有方法仍需针对每条生成 RGB 视频逐序列优化来恢复显式场景，效率与可复用性受限。论文即针对这一“生成视频到显式动态场景”的重建问题展开。

### 核心思路/方法
方法由两部分构成：
1. **多模态视频生成器**：从参考多视角图像和未来控制信号预测 RGB、度量深度和动态流三种模态；
2. **高斯查询解码器**：用深度初始化稀疏 3D 查询，用动态流在时间维度关联查询，并通过时空特征聚合与迭代查询细化融合外观信息。

重建阶段以单次前馈完成，无需针对每个场景做优化。

### 主要贡献
- 提出 Drive2Gauss 前馈框架，把联合生成的 RGB、度量深度与动态流转换为动态 4D 高斯场景。
- 设计高斯查询解码器，利用深度初始化稀疏 3D 查询、利用动态流建立跨时间关联，并结合时空特征聚合与迭代细化。
- 重建不再依赖逐场景优化，实现单次前馈推理。
- 在 nuScenes 上报告：未来 RGB 生成 FID 6.38、FVD 12.43；重建其生成观测的 PSNR 为 29.91 dB；并支持横向相机偏移下的直接渲染与下游视频修复。

### 局限性
摘要未提供足够信息。摘要未说明方法在更多数据集上的泛化性、失败案例、计算开销、对生成模态质量的敏感性，也未给出与逐序列优化方法的系统性对比细节。

### 阅读优先级
**中**。理由：该工作与“生成式驾驶视频驱动的 4D 重建”直接相关，核心思路（多模态生成 + 前馈高斯查询解码）清晰，且有 nuScenes 上的量化结果；若关注动态 4D 重建或驾驶场景生成，值得阅读。但摘要未提供与优化式方法的对比细节和泛化性证据，且兴趣方向未额外指定，因此不列为高优先级。

</details>

<details>
<summary>Abstract</summary>

Generating reusable driving environments requires both controllable future observations and an explicit representation that supports rendering from different viewpoints, yet existing methods still recover explicit scenes from generated RGB videos through optimization for each sequence. To overcome these limitations, we present Drive2Gauss, a feedforward framework that converts jointly generated RGB, metric depth, and dynamic flow into dynamic 4D Gaussian scenes. A Multimodal Video Generator predicts the three modalities from reference multiview images and future control signals. Furthermore, we introduce a Gaussian Query Decoder that uses depth to initialize sparse 3D queries and flow to associate the queries across time, and integrates appearance information through spatiotemporal feature aggregation and iterative query refinement. The reconstruction stage operates in a single feedforward pass without optimization for each scene. Extensive results on nuScenes demonstrate that our approach attains an FID of 6.38 and an FVD of 12.43 for future RGB generation, a PSNR of 29.91 dB when reconstructing its generated observations, and supports both direct rendering under lateral camera shifts and downstream video fixing. Code and more visualizations are available at https://zttt04. github.io/Drive2Gauss_page/.

</details>

#### 2026-10-18 - Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion

**Authors:** Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
**Links:** [abs](https://arxiv.org/abs/2610.25276) - [pdf](https://arxiv.org/pdf/2610.25276)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion
- 作者：Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
- 出版日期：2026-10-18T13:47:01Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.25276)｜[PDF](https://arxiv.org/pdf/2610.25276)

### 一句话总结
Holo4D 将前馈 4D 重建得到的 3D 轨迹投影到目标视角，作为几何与外观的条件引导预训练视频扩散模型，实现单目视频的新相机轨迹重拍。

### 研究问题
从新相机轨迹合成单目视频，需要同时保持已观测场景的几何与运动，并补全新变为可见的区域。前馈 4D 重建器能恢复观测场景结构，视频扩散模型提供生成先验；论文关注如何将两者结合，以重建立足生成、以生成补全未观测区域。

### 核心思路/方法
提出名为 Holo4D 的视频重拍框架：将重建的 3D 轨迹作为整体性的源视角 4D 脚手架（scaffold）；把这些轨迹投影到请求的目标视角，并编码其几何与源外观，用于引导预训练视频扩散模型。结合源视频与目标相机，脚手架使生成以重建观测为依据，而未支持区域交由生成先验补全。框架可适配不同的 4D 重建器，无需重新训练视频生成器。

### 主要贡献
- 提出以重建 3D 轨迹作为整体源视角 4D 脚手架来条件化视频扩散模型的视频重拍框架。
- 将轨迹投影到目标视角并编码几何与源外观，以引导预训练视频扩散模型。
- 实验表明基于轨迹的条件化对相机控制和新视角合成具有价值。
- 框架可容纳不同 4D 重建器且无需重训视频生成器，从而有望受益于源重建的后续进展。

### 局限性
摘要未提供足够信息（未给出失败情形、计算开销、重建器依赖程度或评测细节等具体局限）。

### 阅读优先级
高。理由：论文聚焦 4D 重建与视频扩散的结合，以重建轨迹作为几何控制，且强调无需重训生成器即可适配不同重建器；对动态/4D 重建与神经场景表示渲染方向具有直接相关性。

</details>

<details>
<summary>Abstract</summary>

Synthesizing a monocular video from a new camera trajectory requires preserving the observed scene geometry and motion while completing regions that become newly visible. Feed-forward 4D reconstructors recover the structure of the observed scene, whereas video diffusion models provide a generative prior for completing unseen content. We introduce Holo4D, a video reshooting framework that uses reconstructed 3D trajectories as a holistic source-view 4D scaffold. We project these trajectories into the requested views and encode their geometry and source appearance to guide a pretrained video diffusion model. Together with the source video and target cameras, the scaffold grounds generation in reconstructed observations while leaving unsupported regions to the generative prior. Experiments demonstrate the value of trajectory-based conditioning for camera control and novel-view synthesis. The framework accommodates different 4D reconstructors without retraining the video generator, allowing it to benefit from future advances in source reconstruction. More details can be found in our project page.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-20 - Depth-guided Geometric Adaptation for Few-shot Image Classification

**Authors:** Zhiqi Miao, Estefanía Talavera, Weichuan Zhang, Jiapan Guo
**Links:** [abs](https://arxiv.org/abs/2610.28856) - [pdf](https://arxiv.org/pdf/2610.28856)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** monocular depth, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Depth-guided Geometric Adaptation for Few-shot Image Classification
- 作者：Zhiqi Miao, Estefanía Talavera, Weichuan Zhang, Jiapan Guo
- 出版日期：2026-10-20T19:29:42Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.28856 ；PDF https://arxiv.org/pdf/2610.28856

### 一句话总结
论文提出 DAFIC 框架，将单目深度引入少样本图像分类的表征学习、episodic adaptation 和密集支持集-查询集匹配，以缓解背景杂波与 RGB 外观相似导致的视觉歧义。

### 研究问题
少样本图像分类（FSIC）在数据稀缺条件下容易受到视觉歧义影响：背景杂波和 RGB 外观相似性会妨碍判别性特征匹配。论文旨在缓解这一问题。

### 核心思路/方法
DAFIC 是一个几何引导框架，包含三个要点：
1. 通过 RGB-D 自监督预训练学习几何感知的 token 表征；
2. 使用 Depth-guided Geometric Adaptation（DGA）模块，以深度导出的几何信息细化 patch 表征，引入几何丰富的类别上下文，同时抑制背景干扰；
3. 使用 Spatial Bidirectional Patch Matching（SBiM）对细化后的特征进行双向密集匹配，以降低对虚假对应和背景杂波的敏感性。

### 主要贡献
- 提出 DAFIC，将单目深度纳入少样本图像分类的表征学习、episodic adaptation 与密集支持集-查询集匹配。
- 提出 DGA 模块，利用深度几何细化 patch 表征并抑制背景干扰。
- 提出 SBiM，对细化特征进行双向密集匹配，降低对虚假对应和背景杂波的敏感性。
- 摘要称在四个基准上进行了大量实验，DAFIC 相较现有方法取得较强性能；消融与鲁棒性分析支持将几何条件化的 episodic adaptation 与双向匹配结合用于少样本视觉识别的有效性。

### 局限性
- 摘要未提供足够信息说明具体数据集名称、实验设置、量化指标和对比方法细节。
- 摘要未提供足够信息说明计算开销、推理效率或对深度质量/可用性的依赖程度。
- 摘要未提供足够信息说明失败案例、适用范围限制或是否存在明显性能瓶颈。

### 阅读优先级
中。理由：论文主题聚焦少样本图像分类中的视觉歧义与背景干扰，方法将单目深度与双向密集匹配结合，问题明确且模块设计清晰；但摘要仅给出总体性能结论，未提供具体实验数据与细节，需阅读全文后才能判断其实际效果与适用性。

</details>

<details>
<summary>Abstract</summary>

Few-shot image classification (FSIC) frequently suffers from visual ambiguity, where background clutter and RGB appearance similarities hinder discriminative feature matching in data-scarce settings. To mitigate this, we propose DAFIC, a geometry-guided framework that incorporates monocular depth into representation learning, episodic adaptation, and dense support-query matching. DAFIC first learns geometry-aware token representations through RGB-D self-supervised pre-training. Subsequently, the Depth-guided Geometric Adaptation (DGA) module uses depth-derived geometry to refine patch representations with geometry-enriched class context while suppressing background interference. Spatial Bidirectional Patch Matching (SBiM) then performs bidirectional dense matching on the refined features, reducing sensitivity to spurious correspondences and background clutter. Extensive experiments on four benchmarks show that DAFIC achieves strong performance against existing methods, with ablation and robustness analyses supporting the effectiveness of coupling geometry-conditioned episodic adaptation with bidirectional matching for few-shot visual recognition.

</details>

#### 2026-10-20 - VeriCalib: Verifiable Target-Based LiDAR-Camera Calibration

**Authors:** Xiangcheng Hu, Xieyuanli Chen, Feiyi Chen, Shengli Ren, Shiyang Chen, Guoqiang Ye, Hao Wang, Ping Tan, Steven L. Waslander, Fuchun Sun, Jin Wu
**Links:** [abs](https://arxiv.org/abs/2610.28791) - [pdf](https://arxiv.org/pdf/2610.28791)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VeriCalib: Verifiable Target-Based LiDAR-Camera Calibration
- 作者：Xiangcheng Hu, Xieyuanli Chen, Feiyi Chen, Shengli Ren, Shiyang Chen, Guoqiang Ye, Hao Wang, Ping Tan, Steven L. Waslander, Fuchun Sun, Jin Wu
- 出版日期：2026-10-20T18:21:00Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类）；次要分类：摘要未提供足够信息
- 链接：abstract_url: https://arxiv.org/abs/2610.28791；pdf_url: https://arxiv.org/pdf/2610.28791

### 一句话总结
该论文提出 VeriCalib，将基于标靶的 LiDAR-相机外参标定表述为可验证估计问题，并通过结构化协方差、方向精度解耦、一致性检查以及最小可检测偏差，输出可用于判断是否接受结果或如何采集数据的“标定状态”。

### 研究问题
论文指出，基于标靶的外参标定通常用拟合残差的均方根误差评估结果，但该标量误差在同一批观测上计算，因此无法说明应当接受结果，还是重新提取、重新采集或增加观测。论文希望解决的核心问题是：如何让外参标定结果具备可验证性，并能指示估计是否可靠以及数据采集应如何改进。

### 核心思路/方法
论文的关键观察是一个“两级外参补偿机制”：在残差层面，外参补偿每个观测误差中的刚性部分；在参数层面，旋转与平移相互补偿。因此，拟合残差既不能揭示观测与模型之间的不一致，也不能说明估计外参在每个方向上是否可靠。

为此，VeriCalib 采用结构化协方差评估标定，该协方差联合传播相机与 LiDAR 标靶特征的不确定性，并引入已知几何先验；其尺度作为方差分量从残差中估计。在该协方差基础上，方法解耦旋转与平移，以分析各方向精度，并引导数据采集朝向最弱方向。由于精度分析假设观测一致，论文进一步提出视图内检查与跨视图检查，分别检验内部残差和观测间刚性差异，并使用在未知噪声水平下仍保持显著性水平的阈值。论文还将最小可检测偏差扩展到外参，以界定各方向上可检测故障的下界。上述准则共同构成标定状态。

### 主要贡献
- 将基于标靶的外参标定表述为可验证估计问题，并输出标定状态，用于指示是否接受结果或如何采集数据。
- 揭示两级外参补偿机制导致拟合残差无法同时反映观测-模型不一致性与各方向可靠性。
- 提出结构化协方差方法，联合传播相机与 LiDAR 标靶特征不确定性并利用已知几何先验，且从残差估计方差分量尺度。
- 在协方差上解耦旋转与平移，以分析各方向精度并指导数据采集。
- 提出视图内与跨视图一致性检查，并给出在未知噪声水平下保持显著性水平的阈值。
- 将最小可检测偏差扩展到外参，以界定各方向最小可检测故障。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集、对比方法、定量结果、实时性、适用范围或失败案例等细节；因此无法基于摘要判断方法在真实场景中的精度、鲁棒性和计算开销。

### 阅读优先级
中。理由：该论文针对 LiDAR-相机外参标定的结果可验证性与数据采集指导提出明确问题，并给出协方差分析、一致性检查和最小可检测偏差等方法框架，对做多传感器标定与可信估计的研究者有参考价值；但摘要未提供实验验证细节与定量结果，是否值得优先精读需结合全文实验部分进一步判断。

</details>

<details>
<summary>Abstract</summary>

Target-based extrinsic calibration estimates the rigid transform between sensors from a few observations of a known target, and its result is commonly assessed by the root-mean-square error of the fitted residuals. However, this scalar error is computed on the same observations and therefore cannot indicate whether to accept the result, re-extract, recollect or add observations. This paper presents VeriCalib, which formulates extrinsic calibration as a verifiable estimation problem and reports a calibration state. The key insight is a two-level extrinsic compensation mechanism, in which the extrinsic compensates the rigid part of each observation error at the residual level, and rotation and translation compensate each other at the parameter level. Consequently, the fitted residual can reveal neither an inconsistency between the observations and the model nor whether the estimated extrinsic is reliable in every direction. Accordingly, we assess the calibration through a structured covariance that jointly propagates the uncertainty of the camera and LiDAR board features with a known-geometry prior, and estimate its scale as a variance component from the residuals. On this covariance, we decouple rotation and translation to resolve the precision along each direction and guide data collection toward the weakest one. Since this precision presumes consistent observations, we further develop within-view and cross-view checks that examine the internal residual and the rigid discrepancy between observations, respectively, with thresholds that hold their significance level under an unknown noise level. We also extend the minimal detectable bias to the extrinsic to bound the smallest detectable fault along each direction. These criteria form a calibration state that indicates whether to accept the result or how to collect the data...

</details>

#### 2026-10-20 - SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images

**Authors:** Rundong Luo, Yunong Liu, Di Cao, Matthew Tancik, Shyamal Buch, Colton Stearns, Wenqi Xian
**Links:** [abs](https://arxiv.org/abs/2610.28585) - [pdf](https://arxiv.org/pdf/2610.28585)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, robotics, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images
- 作者：Rundong Luo, Yunong Liu, Di Cao, Matthew Tancik, Shyamal Buch, Colton Stearns, Wenqi Xian
- 出版日期：2026-10-20T17:39:42Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.28585) | [PDF](https://arxiv.org/pdf/2610.28585)

### 一句话总结
SceneRig 是一个“智能体式”系统，从单张图像重建可编辑、可直接用于仿真的三维场景，并通过在物理仿真器中进行编辑—验证循环，保证物体放置与物理稳定性。

### 研究问题
论文针对的是：机器人仿真需要大规模、多样的“仿真就绪”场景，但构建成本高；单图三维重建虽然是有希望的替代方案，但仅追求视觉相似性不够，还必须正确恢复物体、准确放置并满足物理落地。现有依赖“事后物理沉降”的方法常把物体放错位置，导致场景“看着对、操作起来表现差”。

### 核心思路/方法
SceneRig 将几何、视觉与物理工具结合起来，重建忠实的三维场景；随后由一个智能体（agent）在物理仿真器内部执行“编辑—验证”循环，以达到物理稳定性。摘要强调其目标是得到可编辑、仿真就绪的场景，而非仅视觉相似的重建结果。

### 主要贡献
- 提出 SceneRig：一个将单张图像转为可编辑、仿真就绪场景的智能体式系统。
- 方法上结合几何、视觉和物理工具，并引入智能体在物理仿真器中进行编辑—验证循环以实现物理稳定。
- 摘要报告：在多样输入上，SceneRig 改善了实例分割、以物体为中心的外观和三维放置，同时保持重建场景的物理稳定。
- 下游机器人有效性：摘要称其场景比基线方法更准确地预测真实机器人策略结果，并且更可靠地支持录制操作的回放而无需轨迹适配。

### 局限性
摘要未提供足够信息。摘要未给出失败案例、适用输入范围、计算成本、对特定仿真器或物体类别的依赖，也未提供定量实验设置与指标细节。

### 阅读优先级
高。理由：论文同时涉及单图三维重建、物理落地与机器人仿真下游验证，且摘要明确声称在实例分割、物体外观、三维放置和真实机器人策略预测上优于基线；若关注“重建结果可直接用于仿真与操作”的问题，该工作与主题高度相关。但需注意：摘要未提供实验细节与局限性信息，深入判断仍需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Simulation is a powerful tool for robotics, but building diverse, simulation-ready scenes at scale remains difficult. Reconstructing scenes from single images is a promising alternative, but visual similarity alone is insufficient: objects must also be recovered, accurately placed, and physically grounded. Existing methods that rely on post-hoc physics settling often misplace objects, producing scenes that look correct but behave poorly under manipulation. We present SceneRig, an agentic system that turns a single image into an editable, simulation-ready scene. SceneRig combines geometric, visual, and physical tools to reconstruct a faithful 3D scene. An agent then performs edit-and-validate loops inside a physics simulator to achieve physical stability. Across diverse inputs, SceneRig improves instance segmentation, object-centric appearance, and 3D placement while keeping the reconstructed scenes physically stable. Furthermore, SceneRig is effective for downstream robotics: its scenes predict real-robot policy outcomes more accurately than the baseline method and more reliably support replay of recorded manipulations without trajectory adaptation.

</details>

#### 2026-10-20 - Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment

**Authors:** Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen, Ruohong Mei, Shaoyu Chen, Weiqiang Ren, Hui Sun, Qian Zhang, Wenyu Liu, Xinggang Wang
**Links:** [abs](https://arxiv.org/abs/2610.28521) - [pdf](https://arxiv.org/pdf/2610.28521)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, geometric reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment
- 作者：Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen, Ruohong Mei, Shaoyu Chen, Weiqiang Ren, Hui Sun, Qian Zhang, Wenyu Liu, Xinggang Wang
- 出版日期：2026-10-20T16:57:49Z
- 分类：3D Reconstruction & Multi-view Geometry（次要分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2610.28521 ；PDF https://arxiv.org/pdf/2610.28521

### 一句话总结
论文提出 Latent Bridge，将视频生成模型的潜空间与几何特征空间对齐，从而直接从视频潜变量预测相机、深度和3D点云，省去中间 RGB 解码与视觉重编码流程。

### 研究问题
视频生成与前馈3D重建通常使用彼此独立的表示；要从生成的视频潜变量中恢复几何信息，往往需要先解码为 RGB、再进行视觉重编码。论文关注的问题是：能否不经过中间 RGB 通路，直接从视频生成潜空间预测3D几何，并让同一潜空间同时支持 RGB 解码与几何预测。

### 核心思路/方法
- 提出 Latent Bridge，用于连接视频生成潜空间与几何特征空间，直接由视频潜变量预测3D几何。
- 针对 Wan2.1 与 V-RAE 分别开发表示特定的 bridge，实现相机、深度和3D点云的前馈预测，无需中间 RGB 路径。
- 每个 bridge 通过特征蒸馏在 RGB 视频上训练；训练时视频编码器与几何模型保持冻结。
- 训练既不需要真实几何标注，也不需要执行下游几何聚合器或预测头。
- 推理时，同一视频潜变量既可支持 RGB 解码，也可支持几何预测；同一训练好的 bridge 可在相同视频潜空间内复用于图生视频与文生视频生成，无需重新训练 bridge。

### 主要贡献
- 建立视频生成潜空间与几何特征空间之间的直接连接，避免从生成潜变量恢复几何时的 RGB 解码与视觉重编码。
- 为 Wan2.1 和 V-RAE 提供表示特定的 bridge，并给出无需真实几何、无需执行下游几何聚合器或预测头的特征蒸馏训练方式。
- 在推理阶段让同一视频潜变量同时服务 RGB 解码与几何预测，并支持同一潜空间内的图生视频、文生视频复用同一 bridge。
- 在 Co3Dv2 与 WildRGB-D 上报告了具有竞争力的几何重建质量、高效的端到端生成与重建，以及更快的潜变量到几何解码；强调潜空间对齐可作为视频生成与3D重建之间实用且可复用的接口。

### 局限性
- 摘要未提供足够信息来说明方法在失败案例、极端视角、稀疏视角或复杂场景下的具体表现。
- 摘要未提供足够信息来给出定量指标细节、消融实验规模、训练数据规模与计算成本。
- 摘要未提供足够信息来说明 bridge 对未见视频生成模型或不同潜空间表示的泛化能力。
- 摘要未提供足够信息来讨论对真实几何标注的完全独立性在训练与评估中的具体边界。

### 阅读优先级
中。理由：论文聚焦视频生成潜空间与3D几何之间的直接对齐接口，问题定义清晰，且涉及免 RGB 中间通路、冻结模型、特征蒸馏与跨任务复用等较有吸引力的设计；但摘要仅给出高层方法与数据集层面的结论，缺少定量细节与充分局限性讨论。若关注视频生成与3D重建的表示对齐、端到端高效几何预测，值得进一步阅读全文；若仅需成熟基准对比结论，则需查看正文实验部分。

</details>

<details>
<summary>Abstract</summary>

Video generation and feed-forward 3D reconstruction typically use separate representations, requiring RGB decoding and visual re-encoding to recover geometry from generated latents. We propose Latent Bridge, which connects video generative latent spaces with geometric feature spaces to directly predict 3D geometry from video latents. We develop representation-specific bridges for Wan2.1 and V-RAE, enabling feed-forward prediction of cameras, depth, and 3D point clouds without the intermediate RGB pathway. Each bridge is trained on RGB videos through feature distillation, while the video encoder and geometry model remain frozen. Training requires neither ground-truth geometry nor execution of the downstream geometric aggregator or prediction heads. At inference, the same video latents support both RGB decoding and geometry prediction. The same trained bridge can be reused for image-to-video and text-to-video generation within the same video latent space, without bridge retraining. Experiments on Co3Dv2 and WildRGB-D demonstrate competitive geometric reconstruction quality, efficient end-to-end generation and reconstruction, and faster latent-to-geometry decoding, highlighting latent alignment as a practical and reusable interface between video generation and 3D reconstruction. Our code is available at: https://github.com/hustvl/Latent-Bridge.

</details>

#### 2026-10-20 - CrossFit-GS: Out-of-Fold Pose Estimation for COLMAP-Free 3D Gaussian Splatting

**Authors:** Zijian Wu, Jinliang Wang, Mingfeng Jiang, Zidian Lin, Ying Song, Ziqian Lu
**Links:** [abs](https://arxiv.org/abs/2610.28190) - [pdf](https://arxiv.org/pdf/2610.28190)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, SfM, camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CrossFit-GS: Out-of-Fold Pose Estimation for COLMAP-Free 3D Gaussian Splatting
- 作者：Zijian Wu, Jinliang Wang, Mingfeng Jiang, Zidian Lin, Ying Song, Ziqian Lu
- 出版日期：2026-10-20T13:29:26Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.28190 ；PDF https://arxiv.org/pdf/2610.28190

### 一句话总结
CrossFit-GS 提出一种“延迟提交”的渐进式无位姿 3DGS 框架，通过交错子图与交叉精化位姿，缓解累积轨迹漂移和错误地图的自增强传播。

### 研究问题
论文针对无位姿（pose-free）3D Gaussian Splatting 中绕过 SfM、直接从无位姿图像序列重建场景的任务，重点解决两个问题：累积轨迹漂移，以及扭曲地图误差传播形成的自增强循环。

### 核心思路/方法
摘要给出的方法要点如下：
- 将输入序列划分为交错的子集，并维护两个互补的子图。
- 对每个候选位姿，使用一个“冻结的”对侧子图进行交叉精化；该对侧子图从未使用目标帧优化过，从而为位姿估计提供独立几何参考。
- 采用棋盘格验证（checkerboard validation）和空间覆盖保障（spatial coverage safeguards）拒绝不可靠更新。
- 仅将经验证的位姿提交到其所属子图。
- 轨迹精化完成后，丢弃中间子图，并使用固定的精化位姿从头训练最终全局表示。

### 主要贡献
- 提出 CrossFit-GS，一个延迟提交的渐进式无位姿 3DGS 框架。
- 通过交错子图与冻结对侧子图的交叉精化机制，为位姿估计提供独立几何参考。
- 引入棋盘格验证与空间覆盖保障，用于拒绝不可靠的位姿更新。
- 在最终阶段丢弃中间子图，并以固定精化位姿从头训练全局表示。
- 摘要声称在多个基准上可显著减少累积轨迹漂移，并在相机位姿估计和新视角合成上稳定优于现有方法；具体基准、指标与数值摘要未提供足够信息。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、基准数据集名称、定量指标、运行开销、失败案例或方法适用边界；因此无法基于所给材料判断其局限性与适用范围。

### 阅读优先级
中。理由：该工作与无位姿 3DGS、无 COLMAP 重建和多视图几何直接相关，方法机制（交错子图、冻结对侧子图交叉精化、延迟提交）具有明确的问题针对性；但摘要未提供定量结果、基准细节和实现开销，若需评估实际收益与可复现性，应进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Pose-free 3D Gaussian Splatting (3DGS) aims to bypass cumbersome Structure-from-Motion (SfM) by directly reconstructing scenes from unposed image sequences. In this work, we present CrossFit-GS, a deferred-commitment progressive framework that mitigates cumulative trajectory drift and breaks the self-reinforcing loop of distorted-map error propagation. Specifically, we partition the input sequence into interleaved subsets and maintain two complementary submaps. Each candidate pose is cross-refined against a frozen opposite submap that has never been optimized using the target frame, thereby providing an independent geometric reference for pose estimation. Checkerboard validation and spatial coverage safeguards further reject unreliable updates, and only verified poses are committed to their corresponding owner submap. Once the trajectory has been refined, the intermediate submaps are discarded and the final global representation is trained from scratch using the fixed refined poses. Extensive evaluations across multiple benchmarks demonstrate that CrossFit-GS substantially reduces cumulative trajectory drift and consistently improves both camera pose estimation and novel-view synthesis over existing methods.

</details>

#### 2026-10-20 - Real-Time Ground Normal Vector Estimation for Spherical Mobile 3D Mapping using LiDAR-Inertial Odometry

**Authors:** Tim Schubert, Fabian Arzberger, Andreas Nüchter
**Links:** [abs](https://arxiv.org/abs/2610.28701) - [pdf](https://arxiv.org/pdf/2610.28701)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, 3D mapping, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-Time Ground Normal Vector Estimation for Spherical Mobile 3D Mapping using LiDAR-Inertial Odometry
- 作者：Tim Schubert, Fabian Arzberger, Andreas Nüchter
- 出版日期：2026-10-20T11:30:56Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.28701 ；PDF https://arxiv.org/pdf/2610.28701

### 一句话总结
针对球形移动建图系统在快速旋转和地面覆盖有限条件下的地面法向量估计问题，论文提出两种基于 RANSAC 的方法，并说明基于 LiDAR-惯性里程计的全局地图估计在精度和鲁棒性上优于单次扫描方法。

### 研究问题
球形移动建图系统在运动过程中存在快速旋转与地面覆盖受限的问题，而准确的地面平面法向量估计对该系统的里程计至关重要。论文关注如何在上述挑战下实现地面法向量估计，并评估不同估计方式的效果。

### 核心思路/方法
论文提出两种基于 RANSAC 的地面法向量估计方法：
1. 单次扫描估计：采用法向量打分与多步验证；
2. 基于 LiDAR-惯性里程计（LIO）的估计：利用全局三维地图进行估计。

摘要指出，方法在多样化的真实世界数据集上，以地面激光扫描仪提供的地面真值进行评估；结果表明显式基于 LIO 的估计在准确性和鲁棒性上显著优于单次扫描方法。此外，将地面法向量估计整合进运动模型可改善位姿估计。

### 主要贡献
- 提出两种基于 RANSAC 的地面法向量估计方法，分别面向单次扫描与基于 LIO 的全局地图。
- 在多样化的真实世界数据集上，以地面激光扫描仪地面真值进行评估，表明显式基于 LIO 的估计在准确性和鲁棒性上优于单次扫描方法。
- 表明将地面法向量估计整合进运动模型能够改善位姿估计，并支持在挑战性和危险环境中的自主导航。

### 局限性
摘要未提供足够信息。仅从摘要无法获知具体数据集规模、计算实时性指标、失败场景、参数敏感性、单次扫描方法与 LIO 方法的具体误差数值，以及“挑战性和危险环境”的具体范围与验证细节。

### 阅读优先级
中。理由：论文主题明确指向球形移动建图系统的地面法向量估计与 LIO 结合，且摘要给出了清晰的比较结论；但摘要未提供具体实验数据、实时性能与实现细节，是否值得优先精读取决于读者对球形移动建图、LiDAR-惯性里程计或地面约束位姿估计的具体关注程度。

</details>

<details>
<summary>Abstract</summary>

Accurate ground plane normal estimation is essential for odometry in spherical mobile mapping systems (SMMS), which face challenges from rapid rotations and limited ground coverage. We propose two RANSAC-based approaches: single-scan estimation with normal vector scoring and multi-step validation, and LiDAR-inertial odometry (LIO)-based estimation using a global 3D map. Evaluated across diverse real-world datasets against terrestrial laser scanner ground truth, results show that LIO-based estimation significantly outperforms single-scan methods in accuracy and robustness. Integrating ground normal estimates into the motion model improves pose estimation, supporting autonomous navigation in challenging and hazardous environments.

</details>

#### 2026-10-20 - Radar-Based 3D Human Pose Estimation via Motion-Aware Pose Initialization and Observation-Guided Refinement

**Authors:** Woo-Jin Jung, Chan-Bin Lim, Seung-Hyun Kong
**Links:** [abs](https://arxiv.org/abs/2610.27774) - [pdf](https://arxiv.org/pdf/2610.27774)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Radar-Based 3D Human Pose Estimation via Motion-Aware Pose Initialization and Observation-Guided Refinement
- 作者：Woo-Jin Jung, Chan-Bin Lim, Seung-Hyun Kong
- 出版日期：2026-10-20T07:38:04Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.27774) / [PDF](https://arxiv.org/pdf/2610.27774)

### 一句话总结
论文提出两阶段框架 I2R-Pose，通过运动感知的姿态初始化和观测引导的修正，缓解毫米波雷达 3D 人体姿态估计中关节信息不足与反射重叠的问题。

### 研究问题
室内场景（如智能家居）中的 3D 人体姿态估计需要分析人体运动与状态。毫米波雷达对光照变化鲁棒，也不会采集人体外观图像，适合此类任务；但雷达观测对某些身体部位提供的信息不足，并且多个身体部位的反射可能重叠，从而限制 3D 关节定位的准确性。

### 核心思路/方法
论文提出 Initialization-to-Refinement Pose Framework（I2R-Pose），包含两个阶段：
1. **Motion-Aware Pose Initialization**：结合连续雷达观测之间的时间关系与人体骨架结构，学习逐关节特征，以补偿不足的关节信息，并估计初始 3D 姿态序列。
2. **Observation-Guided Refinement**：使用单独提取的雷达观测特征预测逐关节的位置修正，对初始姿态进行细化，生成最终姿态序列。

该框架支持 time-Doppler/time-range（TD/TR）图与雷达点云（PCs）的单独输入及融合输入。为评估室内活动中的性能，论文构建了 RaMoS-Pose 数据集，提供同步的 TD/TR 图、雷达点云与 3D 关节真值。在 RaMoS-Pose 和公开的 MVDoppler-Pose 数据集上的评估显示，与各自数据集上表现最佳的现有方法相比，融合输入下 I2R-Pose 在 MVDoppler-Pose 上将 MPJPE 降低 39.50%，在 RaMoS-Pose 上降低 15.13%。

### 主要贡献
- 提出两阶段框架 I2R-Pose，将运动感知的姿态初始化与观测引导的细化相结合，用于雷达 3D 人体姿态估计。
- 在初始化阶段利用连续雷达观测的时间关系与人体骨架结构学习逐关节特征，以补偿关节信息不足。
- 在细化阶段利用单独提取的雷达观测特征预测逐关节位置修正。
- 框架支持 TD/TR 图与雷达点云的单独及融合输入。
- 构建 RaMoS-Pose 数据集，包含同步的 TD/TR 图、雷达点云和 3D 关节真值。
- 在 RaMoS-Pose 与 MVDoppler-Pose 上报告了相比现有最佳方法的 MPJPE 降低结果。

### 局限性
- 摘要未提供足够信息说明 I2R-Pose 在不同雷达配置、不同受试者或更复杂多人场景下的泛化能力。
- 摘要未提供足够信息说明两阶段各自对最终性能提升的贡献比例，也未提供消融实验细节。
- 摘要未提供足够信息说明 RaMoS-Pose 数据集的规模、受试者数量、动作类别分布及采集环境细节。
- 摘要未提供足够信息说明方法对计算开销、实时性或模型参数量的影响。
- 摘要未提供足够信息说明在非融合输入（仅 TD/TR 图或仅点云）下的具体性能表现。

### 阅读优先级
**中**。理由：该论文针对毫米波雷达 3D 人体姿态估计中的信息不足与反射重叠问题提出明确的两阶段方法，并构建了新数据集，且摘要给出了与现有方法的定量比较；但摘要未提供足够的实验细节、消融结果和泛化性信息，是否值得深入阅读取决于读者对雷达感知、人体姿态估计或室内智能家居应用的兴趣。

</details>

<details>
<summary>Abstract</summary>

3D Human Pose Estimation (3D HPE) is used in indoor environments, such as smart homes, to analyze human movement and monitor human states. Millimeter-wave (mmWave) radar is suitable for this task because it is robust to lighting variations and does not capture images of human appearance. However, radar observations often provide insufficient information about certain body parts or contain overlapping reflections from multiple body parts, limiting accurate 3D joint localization. To address these limitations, we propose the Initialization-to-Refinement Pose Framework (I2R-Pose), comprising two stages: Motion-Aware Pose Initialization and Observation-Guided Refinement. In the first stage, joint-wise features are learned by incorporating temporal relationships across consecutive radar observations and human skeletal structure to compensate for insufficient joint information and estimate an initial 3D pose sequence. In the second stage, separately extracted radar observation features predict joint-wise positional corrections that refine the initial pose and generate the final pose sequence. The framework supports individual and fused inputs of time-Doppler/time-range (TD/TR) maps and radar point clouds (PCs). To evaluate performance across indoor activities, we construct the Radar Motion and Spatial Information for 3D Human Pose Estimation (RaMoS-Pose) dataset, providing synchronized TD/TR maps, radar PCs, and 3D joint ground truth (GT). Evaluations on RaMoS-Pose and the publicly available MVDoppler-Pose dataset show that I2R-Pose reduces mean per-joint position error (MPJPE) by 39.50% on MVDoppler-Pose and by 15.13% on RaMoS-Pose with fused inputs, compared with the best-performing existing methods evaluated on each dataset.

</details>

#### 2026-10-20 - SynCalib: Breaking Dataset Shortcuts in LiDAR-Camera Calibration via Extrinsic-Controllable Synthesis

**Authors:** Huihua Zhu, Shuyang Zhang, Dongqing Chen, Zhuo Yu, Jianhao Jiao, Yilong Zhu, Siyu Teng, Xiaopin Zhong, Zongze Wu
**Links:** [abs](https://arxiv.org/abs/2610.27547) - [pdf](https://arxiv.org/pdf/2610.27547)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SynCalib: Breaking Dataset Shortcuts in LiDAR-Camera Calibration via Extrinsic-Controllable Synthesis
- 作者：Huihua Zhu, Shuyang Zhang, Dongqing Chen, Zhuo Yu, Jianhao Jiao, Yilong Zhu, Siyu Teng, Xiaopin Zhong, Zongze Wu
- 出版日期：2026-10-20T02:59:14Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.27547 ；PDF https://arxiv.org/pdf/2610.27547

### 一句话总结
论文指出现有基于深度学习的LiDAR-相机标定方法因训练数据缺乏外参多样性而存在“数据集捷径”问题，并提出一个可在严格外参约束下合成多模态标定数据的生成框架，以提升模型的泛化性与鲁棒性。

### 研究问题
在线LiDAR-相机标定是机器人领域的基础且具有挑战性的任务。现有数据驱动的深度学习方法虽具备高精度、无靶标标定能力，但其训练数据中外参配置缺乏多样性，导致网络易过拟合到固定的标称外参配置，形成“数据集捷径”现象，从而在真实部署中性能严重下降、泛化能力差。论文旨在缓解该问题。

### 核心思路/方法
论文提出一个面向LiDAR-相机标定网络训练的高泛化性数据生成框架。该框架利用已有的、带有深度真值标注的全向图像数据集，在严格的外参约束下合成多模态标定数据，以打破训练数据中外参多样性不足造成的捷径问题。摘要未提供足够信息说明合成流程的具体步骤、约束形式、网络结构或损失设计。

### 主要贡献
- 指出现有学习型LiDAR-相机标定方法存在由训练数据外参多样性不足引发的“数据集捷径”问题，并分析其导致过拟合与泛化退化的机制。
- 提出一个通用的数据生成框架，基于带深度真值的全向图像数据集，在外参可控/受约束的条件下合成多模态标定数据。
- 摘要称大量实验表明该流程生成的数据显著提升了典型学习型标定网络的泛化性与鲁棒性，并在多种相机-LiDAR配置上进行了真实世界评估，验证了仅用合成数据训练模型的零样本迁移能力。
- 摘要声明将公开数据生成代码、预训练模型和在线基准数据集。

### 局限性
摘要未提供足够信息说明方法的具体技术细节、合成数据与真实数据的分布差异、计算开销、对全向图像数据集深度真值质量的依赖程度，以及定量实验结果和对比基线。论文是否在所有场景和配置下均有效，摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对学习型LiDAR-相机标定中训练数据外参多样性不足这一明确问题，提出数据合成层面的解决思路，并声称验证了零样本迁移能力，且承诺公开代码、模型与基准数据，对相关研究方向具有参考价值；但摘要未给出具体方法细节与定量结果，需阅读全文才能判断其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Online LiDAR-camera calibration remains a fundamental yet challenging task in the field of robotics. Recently, deep learning-based data-driven approaches have emerged, offering high-precision, targetless calibration capabilities. However, existing methods often suffer from a critical dataset shortcut phenomenon due to the lack of extrinsic diversity in their training data. Networks tend to overfit to fixed nominal extrinsic configurations, leading to severe performance degradation and poor generalization in real-world deployments. To address this limitation, we propose a highly generalizable data generation framework tailored for training LiDAR-camera calibration networks. Our framework leverages existing omnidirectional image datasets annotated with depth ground truth to synthesize multi-modal calibration data under rigorous extrinsic constraints. Extensive experiments demonstrate that the data generated by our pipeline significantly enhances the generalization and robustness of typical learning-based calibration networks. Furthermore, we conduct comprehensive real-world evaluations across various camera-LiDAR configurations, validating the zero-shot transfer capability of models trained exclusively on our synthetic data. To facilitate future research and community use, the code for data generation, the pre-trained models, and online benchmark datasets will be made publicly available.

</details>

#### 2026-10-20 - OmniVLoc: Topo-metric Visual Localization for Omnidirectional Cameras

**Authors:** Zhuo Yu, Shuyang Zhang, Huihua Zhu, Wenjia Ouyang, Zuo Zuo, Jianhao Jiao, Yilong Zhu, Xiaopin Zhong, Zongze Wu
**Links:** [abs](https://arxiv.org/abs/2610.27522) - [pdf](https://arxiv.org/pdf/2610.27522)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** bundle adjustment, depth estimation, monocular depth, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniVLoc: Topo-metric Visual Localization for Omnidirectional Cameras
- 作者：Zhuo Yu, Shuyang Zhang, Huihua Zhu, Wenjia Ouyang, Zuo Zuo, Jianhao Jiao, Yilong Zhu, Xiaopin Zhong, Zongze Wu
- 出版日期：2026-10-20T02:35:56Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.27522) / [PDF](https://arxiv.org/pdf/2610.27522)

### 一句话总结
该论文提出 OmniVLoc，一种面向全景相机的拓扑-度量视觉定位系统，通过融合全局场景识别与单目深度估计、求解尺度感知位姿图并进行球面光束法平差，以提升场景内容变化和光照外观变化下的定位精度与鲁棒性。

### 研究问题
传统视觉定位系统受视场角限制，而全景相机虽能提供环视信息，但现有定位系统未能充分利用全景相机特性，在场景内容变化与光照引起的外观变化下难以实现准确、鲁棒的定位。论文旨在解决全景相机下的环视视觉定位问题。

### 核心思路/方法
论文提出基于拓扑-度量框架的环视定位系统 OmniVLoc。方法上集成当前先进的全局场景识别与单目深度估计方法，引入多约束视觉定位范式；通过求解尺度感知位姿图并执行精确的球面光束法平差，恢复每个查询帧的度量级位姿；同时设计分层验证机制，在不同阶段过滤错误输出，以增强系统整体鲁棒性。

### 主要贡献
- 提出 OmniVLoc，一种基于拓扑-度量框架的全景环视视觉定位系统。
- 集成全局场景识别与单目深度估计，构建多约束视觉定位范式。
- 通过尺度感知位姿图求解与球面光束法平差，恢复查询帧的度量级位姿。
- 设计分层验证机制，在不同阶段过滤错误输出以提升鲁棒性。
- 在公开数据集与自建数据集上进行实验，摘要称验证了系统的精度与可靠性；并声明论文发表后将公开源代码与数据集。

### 局限性
摘要未提供足够信息。摘要未给出具体实验指标、对比基线细节、失败场景分析、计算开销或实时性表现；自建数据集规模与构成、分层验证机制的具体阈值与实现细节亦未提供。

### 阅读优先级
中。理由：该论文面向全景相机视觉定位，涉及拓扑-度量框架、尺度感知位姿图与球面光束法平差，与 3D 重建、多视图几何及机器人/AR 应用相关；但仅凭摘要无法判断实验充分性、性能提升幅度与实际部署可行性，建议在需要全景视觉定位或相关几何优化方法时进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Omnidirectional cameras provide surround-view information, significantly overcoming the field-of-view constraints for traditional visual localization systems. However, existing localization systems fail to fully exploit the characteristics of omnidirectional cameras, struggling to deliver accurate and robust localization performance amidst scene content variations and illumination-induced appearance changes. In this work, we propose OmniVLoc, a surround-view localization system based on a topo-metric framework. By integrating state-of-the-art global place recognition and monocular depth estimation methods, we introduce a multi-constrained visual localization paradigm. By solving a scale-aware pose graph and performing precise spherical bundle adjustment, we accurately recover the metric-level pose for each query frame.Furthermore, a hierarchical verification mechanism is designed to filter out erroneous outputs across different stages, effectively bolstering the overall system robustness. Extensive experiments on both public and our custom datasets validate the superior accuracy and reliability of OmniVLoc. To benefit the community, our source code and dataset will be made publicly available upon publication.

</details>

#### 2026-10-19 - MatchCityLoc: Aerial Localization in LoD City Models via Surface Normal Matching

**Authors:** Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier, Marc Pollefeys, Daniel Cremers, Olaf Wysocki
**Links:** [abs](https://arxiv.org/abs/2610.27110) - [pdf](https://arxiv.org/pdf/2610.27110)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, feature matching, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MatchCityLoc: Aerial Localization in LoD City Models via Surface Normal Matching
- 作者：Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier, Marc Pollefeys, Daniel Cremers, Olaf Wysocki
- 出版日期：2026-10-19T18:10:59Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.27110 ；PDF https://arxiv.org/pdf/2610.27110

### 一句话总结
MatchCityLoc 提出用表面法向匹配替代 2D 轮廓重叠评分，在无纹理 LoD 城市模型上从含噪 6-DoF 先验出发实现无人机视觉定位。

### 研究问题
城市环境中 UAV 自主导航需要精确位姿估计，而 GNSS 信号常不可靠，视觉定位成为重要补充。无纹理的 LoD 城市模型虽轻量且保护隐私，但针对抽象几何进行定位很困难；现有流程通常对 2D 轮廓重叠进行评分，可能遭受严重的几何歧义。

### 核心思路/方法
论文将定位范式从轮廓重叠评分转为直接特征匹配，并从一个含噪 6-DoF 位姿先验出发。方法利用零样本基础模型从查询图像中提取表面法向，并将其与渲染的 LoD 法向进行匹配，从而建立显式的 3D-to-2D 对应关系。这些对应关系支持 Perspective-n-Point（PnP）位姿求解，并通过 render-and-match 循环迭代优化。

### 主要贡献
- 提出 MatchCityLoc 框架，将基于 LoD 城市模型的航空定位从 2D 轮廓重叠评分转向表面法向的直接特征匹配。
- 使用零样本基础模型提取查询图像表面法向，并与渲染 LoD 法向匹配，建立显式 3D-to-2D 对应以支持 PnP 位姿求解。
- 通过 render-and-match 循环对位姿进行迭代优化。
- 摘要称实验在所评估的现成 LoD 方法中表现出较强的位姿召回率以及准确的平移和旋转，且渲染次数很少。
- 摘要称该方法弥合了航空影像与无纹理几何之间的模态差距，可利用轻量、隐私保护的城市模型实现准确定位。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集、评价指标数值、失败案例、计算开销细节或方法在不同城市场景下的适用范围；也未说明对先验噪声程度、LoD 精度和基础模型性能的敏感性。

### 阅读优先级
中。理由：该论文聚焦 UAV 城市视觉定位与轻量隐私保护 LoD 模型，问题明确且方法路径清晰（表面法向匹配 + PnP + 迭代优化），与 3D 重建、多视图几何及机器人应用相关；但摘要未提供实验细节和定量结果，是否值得优先精读需结合全文的实验充分性与基线对比再判断。

</details>

<details>
<summary>Abstract</summary>

Autonomous Unmanned Aerial Vehicle (UAV) navigation in urban environments requires precise pose estimation. Because Global Navigation Satellite System (GNSS) signals are often unreliable in cities, visual localization serves as a crucial complement. Within this domain, textureless Level-of-Detail (LoD) city models provide a lightweight and privacy-preserving substitute for heavy 3D textured meshes. However, localizing against abstract geometry is challenging. Existing pipelines typically score 2D silhouette overlaps, which can suffer from severe geometric ambiguities. We present MatchCityLoc, a framework that shifts this paradigm to direct feature matching from a noisy 6-DoF pose prior. By extracting surface normals from the query image using a zero-shot foundation model and matching them against rendered LoD normals, we establish explicit 3D-to-2D correspondences. This enables a Perspective-n-Point (PnP) pose solve, which we iteratively refine through a render-and-match loop. Experiments demonstrate strong pose recall and accurate translation and rotation among the evaluated off-the-shelf LoD-based methods with very few renderings. By bridging the modality gap between aerial imagery and texture-free geometry, MatchCityLoc enables accurate localization using lightweight, privacy-preserving city models.

</details>

#### 2026-10-19 - SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?

**Authors:** Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li
**Links:** [abs](https://arxiv.org/abs/2610.26659) - [pdf](https://arxiv.org/pdf/2610.26659)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D mapping, camera calibration, mapping, localization, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?
- 作者：Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li
- 出版日期：2026-10-19T16:17:48Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.26659) / [PDF](https://arxiv.org/pdf/2610.26659) / [代码](https://github.com/JesseZZZZZ/SpatialScout)

### 一句话总结
论文提出 SpatialScout 基准，用于评估视觉语言模型（VLM）智能体在主动探索室内场景时构建对象级三维度量地图的能力，并揭示当前前沿模型在精确定位与目标覆盖上的显著不足。

### 研究问题
摘要指出，空间智能要求智能体主动获取视觉证据，并将观测整合为对三维世界的一致表示；然而，现有的空间问答任务难以充分证明模型能否通过自主探索构建准确的度量地图。论文因此关注：VLM 智能体能否在有限交互预算下主动探索场景，并在统一坐标系中估计目标物体中心，从而完成对象级三维建图。

### 核心思路/方法
- 构建 SpatialScout 基准，包含 80 个多样室内场景和 3,140 个目标物体。
- 任务输入包括目标物体清单、RGB 观测、相机标定和相机位姿；智能体控制相机探索场景，并估计各目标物体中心在共享坐标系中的位置。
- 任务要求智能体协调视角选择、跨视角关联、几何估计和地图修正，且交互预算有限。
- 评估同时衡量定位精度与目标覆盖度，采用对象尺度重叠分数并对遗漏预测进行惩罚。
- 论文对前沿 VLM 进行实验评估。

### 主要贡献
- 提出面向主动对象级三维建图的 VLM 智能体基准 SpatialScout，强调通过自主探索构建度量地图，而非仅回答空间问题。
- 设计了结合定位精度与目标覆盖度的评估方式，使用对象尺度重叠分数并惩罚遗漏预测。
- 通过实验揭示当前前沿 VLM 的明显局限：最强评估模型 Claude Opus 5.5 的平均重叠分数为 41.71%，仅 47.23% 的目标超过 IoU 0.5，超过 IoU 0.9 的目标仅 3.25%。
- 指出模型在恢复粗略物体布局与构建完整、精确度量地图之间存在显著差距，并提供可量化测试平台与代码链接。

### 局限性
- 摘要未提供足够信息说明基准场景的具体来源、数据采集方式及场景多样性细节。
- 摘要未提供足够信息说明交互预算的具体数值、相机控制接口或动作空间设计。
- 摘要未提供足够信息说明除 Claude Opus 5.5 外参与评估的完整模型列表及各自详细结果。
- 摘要未提供足够信息说明失败模式分析、消融实验或方法改进建议。
- 摘要未提供足够信息说明评估指标的具体计算细节及与真实标注的匹配方式。

### 阅读优先级
高。理由：该论文直接针对 VLM 智能体主动三维感知与建图能力提出新基准，任务定义和评估指标明确，且摘要给出了量化结果与显著能力差距；对三维重建、多视角几何、具身智能和机器人应用方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploration. We introduce SpatialScout, a benchmark for evaluating vision-language model (VLM) agents on active object-level 3D mapping. SpatialScout comprises 80 diverse indoor scenes containing 3,140 target objects. Given an object inventory, RGB observations, camera calibration, and camera poses, agents control a camera to explore each scene and estimate object centers in a shared coordinate frame. The task requires coordinating viewpoint selection, cross-view association, geometric estimation, and map revision under bounded interaction budgets. Evaluation jointly measures localization accuracy and target coverage through object-scale overlap scores that penalize missing predictions. Experiments with frontier VLMs reveal substantial limitations: the strongest evaluated model, Claude Opus 5.5, achieves a mean overlap score of 41.71%, with 47.23% of targets exceeding an intersection-over-union (IoU) threshold of 0.5 and only 3.25% exceeding 0.9. These results reveal a substantial gap between recovering coarse object layouts and constructing complete, precise metric maps. SpatialScout provides a quantitative testbed for developing agents that build reliable 3D spatial representations through active perception. Code is available at https://github.com/JesseZZZZZ/SpatialScout.

</details>

#### 2026-10-19 - EgoRayFormer: Ray-Space Stereo Refinement for Egocentric 3D Human Pose Estimation

**Authors:** Haozhe Wang, Songyuan Wu, Jihai Xu, Jie Zhao
**Links:** [abs](https://arxiv.org/abs/2610.26641) - [pdf](https://arxiv.org/pdf/2610.26641)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoRayFormer: Ray-Space Stereo Refinement for Egocentric 3D Human Pose Estimation
- 作者：Haozhe Wang, Songyuan Wu, Jihai Xu, Jie Zhao
- 出版日期：2026-10-19T16:03:20Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；未提供二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.26641) / [PDF](https://arxiv.org/pdf/2610.26641)

### 一句话总结
EgoRayFormer 面向头戴式双目鱼眼相机下的第一人称 3D 人体姿态估计，在射线空间中耦合双目特征采样与几何细化，以引入显式双目约束，并在几何约束较弱时保留学习式更新的灵活性。

### 研究问题
头戴式双目鱼眼相机能提供穿戴者身体的紧凑视角，但强畸变、部分可见性和短基线使 3D 姿态估计困难。摘要指出现有细化解码器在各视图中独立采样图像特征，不要求这些采样对应共同的 3D 假设，因而缺少显式双目几何约束。论文即针对这一问题提出改进。

### 核心思路/方法
论文提出因果姿态估计器 EgoRayFormer，将双目特征采样与几何细化耦合在射线空间中。对每个关节，解码器沿其视线射线并在射线周围，把共享的 3D 假设投影到两幅图像中；随后几何分支校正投影后的关节位置，并对所得射线进行相交；一个学习到的门控将几何估计与学习到的姿态更新融合。该形式化方法引入显式双目约束，同时在射线提供弱深度约束时保留灵活性。

### 主要贡献
- 提出 EgoRayFormer，在射线空间中耦合双目特征采样与几何细化，用于第一人称 3D 人体姿态估计。
- 通过将共享 3D 假设沿/绕观测射线投影到双视图，并对校正后的射线求交，引入显式双目约束；再用学习门控融合几何估计与学习姿态更新。
- 摘要报告在官方设备相对测试划分上的本地评估结果：UnrealEgo2 上三随机种子平均 MPJPE 为 17.64 mm，UnrealEgo-RW 上为 49.55 mm，使用 UnrealEgo2 预训练后提升至 47.57 mm。
- 配对验证消融显示，在两种输入分辨率下移除几何分支均使三个随机种子的 MPJPE 增加。
- 在相同 ResNet-18 编码器和输入分辨率下，相较设备相对的 EgoPoseFormer 基线，将 RW 测试 MPJPE 降低 9.09 mm。
- 另有一项协议分析量化设备相对评估与 oracle-root 评估之间的差异。

### 局限性
摘要未提供足够信息说明方法在真实场景泛化、计算开销、对极端遮挡或强畸变的失败模式等方面的局限；也未提供跨数据集以外的完整实验细节。仅从摘要可知，部分结果来自本地评估与特定测试划分，且预训练依赖 UnrealEgo2。

### 阅读优先级
中。理由：该论文聚焦第一人称双目鱼眼 3D 人体姿态估计中的显式双目几何约束与射线空间细化，问题定义和方法动机较清晰，并报告了 MPJPE 改进与消融结果；但摘要未提供真实场景验证、计算成本及更广泛失败模式的信息，是否高优先级取决于读者对第一人称姿态估计或多视图几何细化的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Head-mounted stereo fisheye cameras provide a compact view of the wearer's body, but strong distortion, partial visibility and a short baseline make 3D pose estimation difficult. Existing refinement decoders sample image features independently in each view, without requiring the samples to correspond to a common 3D hypothesis. We introduce EgoRayFormer, a causal pose estimator that couples stereo feature sampling and geometric refinement in ray space. For each joint, the decoder projects shared 3D hypotheses along and around its viewing ray into both images. A geometric branch then corrects the projected joint locations and intersects the resulting rays; a learned gate blends this geometric estimate with a learned pose update. This formulation introduces an explicit stereo constraint while retaining flexibility when the rays provide weak depth constraints. In local evaluations on the official device-relative test splits, EgoRayFormer achieves three-seed mean MPJPEs of 17.64 mm on UnrealEgo2 and 49.55 mm on UnrealEgo-RW, improving to 47.57 mm with UnrealEgo2 pre-training. In paired validation ablations, removing the geometric branch increases MPJPE in all three seeds at both input resolutions. With a common ResNet-18 encoder and input resolution, our system reduces RW test MPJPE by 9.09 mm relative to the device-relative EgoPoseFormer baseline. A separate protocol analysis quantifies the difference between device-relative and oracle-root evaluation.

</details>

#### 2026-10-19 - CAOS-SLAM: Class-Agnostic Object-Aware Real-Time vSLAM for Dynamic Environments

**Authors:** Gaia Borghi, João Carlos Virgolino Soares, Angelo Bratta, Shahab Heshmati-Alamdari, Claudio Semini
**Links:** [abs](https://arxiv.org/abs/2610.26633) - [pdf](https://arxiv.org/pdf/2610.26633)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CAOS-SLAM: Class-Agnostic Object-Aware Real-Time vSLAM for Dynamic Environments
- 作者：Gaia Borghi, João Carlos Virgolino Soares, Angelo Bratta, Shahab Heshmati-Alamdari, Claudio Semini
- 出版日期：2026-10-19T16:00:00Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.26633) | [PDF](https://arxiv.org/pdf/2610.26633)

### 一句话总结
CAOS-SLAM 在 ORB-SLAM3 基础上引入混合感知流程，实时检测、跟踪并过滤语义已知与未见过的运动物体，以减少动态特征对定位与建图的干扰。

### 研究问题
动态环境中的运动物体会引入错误观测，破坏地图重建并降低定位精度。现有 vSLAM 方法常依赖预定义语义类别或昂贵的逐像素分类，限制了其在真实场景中的鲁棒性或适用性。论文旨在解决对语义已知和此前未见运动物体的实时检测、跟踪与动态特征剔除问题。

### 核心思路/方法
论文提出 CAOS-SLAM，一个动态 vSLAM 框架，扩展 ORB-SLAM3 并加入混合感知流程，用于实时检测、跟踪和过滤语义已知及此前未见过的运动物体。方法包括：按需执行全景分割用于物体发现；通过未分类区域的深度聚类实例化候选未知物体；在全景分割更新之间，利用可用的轻量检测或基于世界坐标系 Kalman 预测、深度一致性和外观相似性的时序掩码传播来更新持续物体轨迹；随后利用估计的物体运动从 SLAM 流程中剔除动态特征。

### 主要贡献
- 提出 CAOS-SLAM 动态 vSLAM 框架，扩展 ORB-SLAM3，支持对语义已知和未见运动物体的实时检测、跟踪与过滤。
- 设计混合感知流程：按需全景分割、基于深度聚类的未知物体实例化，以及结合轻量检测或时序掩码传播的持续物体跟踪。
- 利用估计的物体运动剔除动态特征，提升动态环境下的定位表现。
- 摘要称在多个动态 RGB-D 数据集和真实实验上优于现有动态 vSLAM 方法：未知动态物体场景定位误差最高降低 59%，严重遮挡场景最高降低 88%，在笔记本电脑上达到 30 FPS 的中位处理速率。
- 跟踪模块提供物体轨迹和速度估计，摘要称可支持动态环境下感知、导航和运动规划等潜在应用。

### 局限性
摘要未提供足够信息说明方法在极端场景、计算资源受限平台、长期运行稳定性或失败模式方面的局限。摘要提到代码和数据集将在接收后发布，但未提供具体实验细节、数据集名称或消融结果。

### 阅读优先级
高。理由：该论文直接针对动态环境下 vSLAM 的鲁棒性与实时性问题，提出类无关物体感知与动态特征剔除框架，并给出定位误差降低和 30 FPS 的摘要级结果；对动态 SLAM、机器人感知与导航相关研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Robust visual Simultaneous Localization and Mapping (vSLAM) in dynamic environments faces challenges due to the presence of moving objects that may introduce erroneous observations, corrupt the map reconstruction and overall degrade localization accuracy. Existing vSLAM approaches often rely on predefined semantic classes or costly pixel-wise classification, limiting their robustness or applicability in real-world scenarios. This paper presents CAOS-SLAM, a dynamic vSLAM framework that extends ORB-SLAM3 with a hybrid perception pipeline to detect, track, and filter both semantically known and previously unseen moving objects in real-time. On-demand panoptic segmentation is performed for object discovery, with candidate unknown objects instantiated through depth-based clustering of unclassified regions. Between panoptic updates, persistent object tracks are updated using lightweight detection when available or temporal mask propagation based on world-frame Kalman prediction, depth consistency, and appearance similarity. The estimated object motion is then used to reject dynamic features from the SLAM pipeline. Experimental results on multiple dynamic RGB-D datasets and real-world experiments demonstrate improved localization accuracy over state-of-the-art dynamic vSLAM approaches, achieving up to 59% lower localization error in scenes characterized by unknown dynamic objects and up to 88% lower error in heavily occluded scenes, while achieving a median processing rate of 30 FPS on a laptop. Furthermore, the tracking module provides estimates of object trajectories and velocities, supporting potential future applications in perception, navigation, and motion-planning tasks in dynamic environments. Code and dataset will be released upon acceptance.

</details>

#### 2026-10-19 - PnP-Transformer: A Neural Pose Solver for Zero-Shot 6D Object Pose Estimation

**Authors:** Emirkan Burak Yilmaz, Yakup Genc
**Links:** [abs](https://arxiv.org/abs/2610.26096) - [pdf](https://arxiv.org/pdf/2610.26096)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, mapping, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PnP-Transformer: A Neural Pose Solver for Zero-Shot 6D Object Pose Estimation
- 作者：Emirkan Burak Yilmaz, Yakup Genc
- 出版日期：2026-10-19T09:57:44Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.26096 ；PDF https://arxiv.org/pdf/2610.26096 ；代码与预训练模型 https://github.com/ebylmz/pnp-transformer

### 一句话总结
提出一种无需迭代、可微的神经位姿求解器 PnP-Transformer，将其作为经典 PnP-RANSAC 的替代，集成到零样本 6D 物体位姿估计流程中，并报告了精度与延迟之间的权衡。

### 研究问题
论文关注 6D 物体位姿估计中的求解环节：经典 PnP-RANSAC 算法存在迭代与不可微的特点，作者希望探索一种无迭代、可微的神经位姿求解器，并在零样本 6D 位姿估计流程中评估其实用性。

### 核心思路/方法
PnP-Transformer 是一种神经位姿求解器，作为经典 PnP-RANSAC 的“无迭代、可微”替代方案。它通过处理预测得到的半稠密 2D-3D 对应场及其置信度分数来回归 6D 物体位姿，并将几何输入映射到连续潜在空间。论文将其集成到一个零样本 6D 位姿估计流程中，其中对应模块与位姿求解器分别训练；并与将位姿求解器替换为 EPnP-RANSAC（保持对应模块不变）的方案进行对比。

### 主要贡献
- 提出 PnP-Transformer：一种无迭代、可微的神经位姿求解器，用于处理半稠密 2D-3D 对应场与置信度分数并回归 6D 位姿。
- 将其集成到零样本 6D 位姿估计流程中，对应模块与位姿求解器分开训练。
- 在七个核心 BOP 基准数据集上报告平均 AR 为 41.2%，延迟为 0.46 s/obj，称其超过除 Co-op（58.4% AR）之外的所有先前基线（例如 RayPose 为 39.1% AR）。
- 通过替换为 EPnP-RANSAC 的对照实验揭示精度—延迟权衡：RANSAC 替代方案在七个数据集中的六个上更优，平均 AR 为 52.2%，但每个物体额外增加 60 ms。

### 局限性
- 摘要仅给出平均 AR 与平均延迟等汇总结果，未提供各数据集的分项结果、消融实验、训练细节与失败案例分析；这些信息摘要未提供足够信息。
- 摘要显示 PnP-Transformer 的平均 AR（41.2%）低于 Co-op（58.4%），且在保持对应模块不变、改用 EPnP-RANSAC 后，后者在七个数据集中的六个上更优（52.2% 平均 AR），说明其在精度上并非全面占优，主要优势体现在低延迟。
- 摘要未说明在何种硬件与实验条件下测得 0.46 s/obj 与额外 60 ms 的延迟，相关实验设置摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对 6D 位姿估计中的求解器环节提出可微替代方案，并给出在七个 BOP 数据集上的定量对比与明确的精度—延迟权衡结论，对关注零样本 6D 位姿估计与 PnP 求解的研究者有参考价值；但摘要显示其精度不及 Co-op 及 EPnP-RANSAC 对照方案，核心卖点主要在低延迟，是否深入阅读取决于读者对速度优先方案的关注程度。

</details>

<details>
<summary>Abstract</summary>

We present PnP-Transformer, a neural pose solver designed as an iterative-free, differentiable alternative to classical PnP-RANSAC algorithms. PnP-Transformer regresses the 6D object pose by processing predicted semi-dense 2D-3D correspondence fields alongside confidence scores, while mapping geometric inputs into a continuous latent space. To evaluate its practical utility, we integrate PnP-Transformer into a zero-shot 6D pose estimation pipeline, where the correspondence module and pose solver are trained separately. PnP-Transformer achieves a 41.2% mean AR score with low latency (0.46 s/obj) on seven core BOP benchmark datasets, surpassing all prior baselines (such as RayPose with 39.1% AR) but one (Co-op with 58.4% AR). When the pose solver is replaced with EPnP-RANSAC (similar to Co-op) while keeping the correspondence module unchanged, the RANSAC alternative outperforms PnP-Transformer on six of the seven datasets by reaching 52.2% mean AR at a cost of an additional 60 ms per object, revealing an accuracy-latency trade-off. Code and pretrained models are available at https://github.com/ebylmz/pnp-transformer.

</details>

#### 2026-10-19 - OV-PEAR: Observation-Verified Pose-Scale Estimation and Reconstruction for Unknown Industrial Manipulation Objects

**Authors:** Guoqin Tang, Qingxuan Jia, Yichen Tan, Zihang Lv, Ruiquan Wang, Zeyuan Huang, Gang Chen
**Links:** [abs](https://arxiv.org/abs/2610.25840) - [pdf](https://arxiv.org/pdf/2610.25840)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, pose estimation, manipulation, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OV-PEAR: Observation-Verified Pose-Scale Estimation and Reconstruction for Unknown Industrial Manipulation Objects
- 作者：Guoqin Tang, Qingxuan Jia, Yichen Tan, Zihang Lv, Ruiquan Wang, Zeyuan Huang, Gang Chen
- 出版日期：2026-10-19T05:51:41Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要页](https://arxiv.org/abs/2610.25840)｜[PDF](https://arxiv.org/pdf/2610.25840)

### 一句话总结
OV-PEAR 面向未知工业操作物体，提出一个经观测验证的三阶段框架，同时完成物体级 3D 重建和位姿-尺度估计，以摆脱对 CAD 模型、物体专用训练数据或稳定工作单元的依赖。

### 研究问题
精细工业机器人操作需要 6D 位姿、尺度以及可直接用于操作的 3D 模型。摘要指出，现有工业位姿估计依赖 CAD 模型、物体专用训练数据或稳定工作单元，因此难以用于未见物体；零样本方法则受单视角遮挡、生成偏差和尺度不确定性影响。论文要解决的问题是：对未知工业物体，如何在不依赖上述先验或假设的情况下，获得可用的 3D 模型以及位姿和尺度估计。

### 核心思路/方法
论文提出 OV-PEAR，一个以物体为中心、包含三个阶段并经观测验证的流水线：

1. 分割 RGB-D 实例，并生成物体级 3D 假设；
2. 通过外观感知的视角检索、显式尺度搜索和可见性敏感配准，将假设锚定到机器人坐标系；
3. 将多视角 RGB-D 证据反投影到物体规范坐标系，验证体素占用、抑制幻觉，并生成可复用的可信物体模型。

摘要还提到，模型库和位姿-尺度日志支持短期的物体级状态维护。

### 主要贡献
- 提出 OV-PEAR 框架，用于未知工业物体的 3D 重建与位姿-尺度估计，并以观测验证作为核心机制。
- 设计三阶段物体中心流水线，涵盖实例分割与 3D 假设生成、机器人坐标系锚定、多视角体素占用验证与可信模型生成。
- 在 BOP-Industrial 上报告平均 AR 为 0.657，并在真实场景中改善位姿与体素级几何一致性。
- 在真实机器人连接器装配任务中报告 99.67% 抓取成功率和 84.00% 装配成功率。
- 模型库与位姿-尺度日志支持短期的物体级状态维护，报告速度为 0.02 ms/frame。

### 局限性
- 摘要未提供足够信息说明方法对极端遮挡、严重传感器噪声或高度透明/反光工业物体的具体表现。
- 摘要未提供足够信息说明三阶段各模块的消融实验、失败案例和计算资源需求。
- 摘要未提供足够信息说明 BOP-Industrial 上的评测协议细节、对比方法完整列表，以及真实场景实验规模。
- 摘要未提供足够信息说明“短期物体级状态维护”的时间范围、适用边界与长期稳定性。
- 摘要未提供足够信息说明方法对机器人坐标系标定误差、视角检索失败或尺度搜索失败的鲁棒性。

### 阅读优先级
中。理由：该论文与未知物体 6D 位姿、尺度估计、机器人操作和 3D 重建直接相关，且摘要给出了量化结果和真实机器人验证；但摘要未展开方法细节、消融与失败分析。若关注零样本工业物体位姿估计、观测验证式重建或机器人装配，优先级可提高至高；若仅关心通用 6D 位姿跟踪或大规模场景重建，则优先级为中等。

</details>

<details>
<summary>Abstract</summary>

Fine industrial robotic manipulation requires 6D pose, scale, and an operation-ready 3D model. Existing industrial pose estimation relies on CAD models, object-specific training data, or stable workcells, limiting use with unseen objects; zero-shot methods suffer from single-view occlusion, generative bias, and scale uncertainty. We present OV-PEAR, an observation-verified framework for 3D reconstruction and pose-scale estimation of unknown industrial objects. Its three-stage object-centric pipeline: (1) segments RGB-D instances and generates object-level 3D hypotheses; (2) anchors them to the robot frame via appearance-aware view retrieval, explicit scale search, and visibility-sensitive registration; (3) back-projects multi-view RGB-D evidence into the object-canonical frame to verify voxel occupancy, suppress hallucinations, and produce reusable trusted object models. On BOP-Industrial, OV-PEAR achieves 0.657 average AR and improves pose and voxel-level geometric consistency in real scenes; real-robot connector assembly reaches 99.67% grasp and 84.00% assembly success. The model library and pose-scale log enable short-term object-level state maintenance at 0.02 ms/frame.

</details>

#### 2026-10-19 - Recurrent Vision Transformers for Event-Based Spacecraft Pose Estimation Under Slow Relative Motions

**Authors:** Sofia McLeod, Mohsi Jawaid, Carl Seubert, Tat-Jun Chin
**Links:** [abs](https://arxiv.org/abs/2610.25622) - [pdf](https://arxiv.org/pdf/2610.25622)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Recurrent Vision Transformers for Event-Based Spacecraft Pose Estimation Under Slow Relative Motions
- 作者：Sofia McLeod, Mohsi Jawaid, Carl Seubert, Tat-Jun Chin
- 出版日期：2026-10-19T00:52:34Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.25622 ；PDF https://arxiv.org/pdf/2610.25622

### 一句话总结
论文提出用循环视觉 Transformer（RVT）处理慢速相对运动下事件相机航天器位姿估计中事件率低、信噪比差的问题，并在真实慢速运动事件数据上验证了位姿估计精度与稳定性优于逐事件帧或固定时间窗方法。

### 研究问题
基于视觉的航天器位姿估计对交会与近距离操作（RPO）很重要，事件相机因高动态范围在轨道强光照条件下具有鲁棒性。但基于事件的航天器位姿估计（EBSPE）在追踪器与目标相对运动很慢时表现变差：事件率显著下降，数据信噪比低；而真实 RPO 轨迹出于安全常包含慢速相对运动，例如低至 1 mm/s；低照度还会加剧该问题。因此，如何处理慢速相对运动是提升 EBSPE 实用性的关键。

### 核心思路/方法
论文提出将循环视觉 Transformer（RVT）用于 EBSPE。核心思想是利用循环记忆在稀疏事件流中捕捉更长时程信息，并从完整轨迹中学习时间注意力跨度，而不是固定时间窗口。作者开发了一个基于 RVT 的热图回归器，用于产生位姿估计所需的 2D-3D 对应关系，并在代表 RPO 轨迹的慢速相对运动条件下采集的真实事件数据上进行验证。

### 主要贡献
- 针对慢速相对运动导致事件率低、信噪比差的问题，提出使用 RVT 进行基于事件的航天器位姿估计。
- 利用循环记忆捕捉稀疏事件流中的长期信息，并学习时间注意力跨度而非固定时间窗。
- 构建基于 RVT 的热图回归器以生成 2D-3D 对应关系用于位姿估计。
- 在慢速相对运动的真实事件数据上验证，结果显示相较此前逐事件帧或固定时间窗的 EBSPE 方法，位姿估计精度和稳定性更优。

### 局限性
摘要未提供足够信息。仅能看出验证基于真实事件数据，但具体数据集规模、轨迹范围、光照条件覆盖、计算开销、实时性、失败案例等均未在摘要中说明；也未给出定量指标数值和与基线方法的详细对比设置。

### 阅读优先级
高。理由：该论文直接针对 EBSPE 在真实 RPO 慢速运动场景下的关键失效模式，问题定义明确且具有实际应用背景；方法上引入 RVT 的循环记忆与可学习时间注意力跨度，针对稀疏事件流的时程建模；摘要声称在真实慢速运动事件数据上优于逐事件帧和固定时间窗方法。若关注事件相机位姿估计、航天器 RPO 或稀疏事件流时序建模，该论文值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Vision-based object pose estimation is vital for conducting spacecraft rendezvous and proximity operations (RPO). Recent research has demonstrated the robustness of event cameras against the harsh lighting conditions that often occur in orbit, thanks to the extremely high dynamic range of event sensors. However, event-based spacecraft pose estimation (EBSPE) suffers when the relative motion between the chaser and target is slow, since the event rate drops significantly, leading to data with low signal-to-noise ratio. Unfortunately, for safety reasons, real RPO trajectories often involve slow relative motions (e.g., down to 1 mm/s), and operating under low illumination exacerbates the problem. Addressing slow relative motions is thus crucial to raise the practicality of EBSPE. To this end, we propose using recurrent vision transformers (RVT) for EBSPE. The key idea is to exploit recurrent memory to capture longer-term information across sparse event streams, and to learn the temporal attention span from full trajectories rather than fixing the time window. We developed an RVT-based heatmap regressor to produce 2D-3D correspondences for pose estimation, which was validated on real event data collected under slow relative motions representative of RPO trajectories. Results indicate the superior pose estimation accuracy and stability of our RVT-based method, relative to previous per-event-frame-based or fixed-time-window EBSPE methods.

</details>

#### 2026-10-15 - Gen4P: Video Generators are 4D Perceivers

**Authors:** Yitong Xia, Zeren Jiang, Chuanxia Zheng
**Links:** [abs](https://arxiv.org/abs/2610.22371) - [pdf](https://arxiv.org/pdf/2610.22371)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gen4P: Video Generators are 4D Perceivers
- 作者：Yitong Xia, Zeren Jiang, Chuanxia Zheng
- 出版日期：2026-10-15T17:59:48Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.22371

### 一句话总结
Gen4P 提出将预训练视频生成器改造为无需迭代去噪的前馈式 4D 感知器，从单目视频中统一恢复 4D 几何与运动。

### 研究问题
如何从单目视频中恢复 4D 几何与运动，并利用预训练视频生成器的能力实现统一、前馈式的 4D 感知，而非依赖迭代去噪过程。

### 核心思路/方法
- 将预训练视频生成器重新利用为前馈式 4D 感知器，无需迭代去噪。
- 基于按需查询（on-demand querying），Gen4P 在单次编码器前向中处理干净的视频 latent，并通过轻量级 cross-attention 解码器预测所请求的 4D 属性。
- 按需查询形式支持灵活的空间采样；提出的连续时间查询进一步提供时间灵活性。
- 为增强几何知识，提出一种简单的插件式方案：将预训练的视频-深度 LoRA 作为冻结的几何先验引入，在不增加额外可训练参数的情况下提升整体性能。

### 主要贡献
- 提出 Gen4P，一个从单目视频恢复 4D 几何与运动的统一框架。
- 展示预训练视频生成器可被改造为前馈式 4D 感知器，且无需迭代去噪。
- 通过按需查询与连续时间查询，分别实现灵活的空间采样与时间灵活性。
- 提出将预训练视频-深度 LoRA 作为冻结几何先验的插件式方案，在不增加可训练参数的情况下提升性能。
- 在 3D 点跟踪、视频深度和相机位姿估计任务上取得 state-of-the-art 或具竞争力的性能；在野外视频上的定性结果展示其跟踪复杂运动并保持精细结构的能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作将视频生成预训练与统一 4D 感知结合，涉及 3D 点跟踪、视频深度和相机位姿估计等多任务，并声称达到 state-of-the-art 或具竞争力性能，对 3D 重建与多视图几何方向有参考价值；但摘要未给出具体实验细节、量化结果与失败情形，需进一步阅读原文确认适用范围与局限。

</details>

<details>
<summary>Abstract</summary>

We introduce Gen4P, a unified framework for recovering 4D geometry and motion from monocular video. We show that a pretrained video generator can be repurposed into a feed-forward 4D perceiver without iterative denoising. Building on on-demand querying, Gen4P processes clean video latents in a single encoder pass and predicts the requested 4D attributes through a lightweight cross-attention decoder. The on-demand query formulation enables flexible spatial sampling, and our proposed continuous-time queries further provide temporal flexibility. To strengthen geometric knowledge, we propose a straightforward plug-in solution by incorporating a pretrained video-depth LoRA as a frozen geometry prior, improving overall performance without adding extra trainable parameters. Gen4P achieves state-of-the-art or competitive performance on tasks of 3D point tracking, video depth and camera pose estimation. Qualitative results on in-the-wild videos illustrate its capability of tracking complex motion while maintaining the delicate structure. Together, these results demonstrate the potential of video generative pretraining for unified 4D perception. See https://gen4p.github.io for more visual results.

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-21 - ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization

**Authors:** Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin
**Links:** [abs](https://arxiv.org/abs/2610.30013) - [pdf](https://arxiv.org/pdf/2610.30013)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization
- 作者：Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin
- 出版日期：2026-10-21T16:43:53Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.30013；PDF https://arxiv.org/pdf/2610.30013

### 一句话总结
ClunoGS 提出一个面向 Language 3D Gaussian Splatting 的紧凑化框架，通过语义感知的高斯稀疏化与向量量化统一优化，在压缩模型存储的同时尽量保持开放词汇语义预测能力。

### 研究问题
Language 3DGS 通过为高斯基元关联语言特征来支持开放词汇场景理解，但这些语义属性会增加模型存储。现有 3DGS 压缩方法主要面向 RGB 渲染质量；若顺序执行稀疏化和量化，仅依据渲染质量剪枝可能删除 RGB 贡献小但对语义预测重要的高斯，且被删除后的语义信息无法由后续量化恢复。因此，问题是如何在压缩 Language 3DGS 时同时兼顾渲染质量、语义准确性和紧凑性，避免语义无关剪枝与顺序压缩造成语义表示退化。

### 核心思路/方法
论文将语义感知的高斯稀疏化与向量量化结合为一个统一的约束目标，并在稀疏化过程中使用语义监督。该统一目标同时考虑渲染质量、语义准确性和紧凑性，并通过交替进行原始变量更新、稀疏化、量化和对偶更新来优化。方法的核心是避免“先按渲染质量剪枝、再量化”的顺序式压缩，因为这种语义无关的稀疏化会不可逆地丢失对语义预测重要但 RGB 贡献较小的高斯信息。

### 主要贡献
- 提出 ClunoGS，一个面向 Language 3DGS 的紧凑框架，将语义感知高斯稀疏化与向量量化纳入统一约束目标。
- 在稀疏化中引入语义监督，使剪枝不只依据渲染质量，从而减少对语义重要高斯的误删。
- 设计交替优化流程，联合更新原始变量、稀疏化、量化和对偶变量。
- 在 LERF 和 ScanNet-10 基准上评估开放词汇定位与分割；摘要称在激进压缩下，该统一语义感知表述显著缓解了顺序压缩和语义无关稀疏化导致的语义表示退化。
- 消融结果显示，联合协调稀疏化与量化比独立应用二者更能保持语义准确率。

### 局限性
摘要未提供足够信息说明计算开销、训练时间、压缩率与存储节省的具体数值、不同压缩强度下的完整定量结果、对语言特征类型的依赖、超参数敏感性，以及方法在其他 3DGS 变体或更大场景上的泛化表现。摘要未提供足够信息给出与具体基线方法的逐项数值对比细节。

### 阅读优先级
中。理由：该论文关注 Language 3DGS 的存储压缩与语义保持之间的冲突，问题定义清晰，统一优化和语义感知剪枝的思路对 3DGS 压缩与开放词汇场景理解交叉方向有参考价值；但摘要仅给出任务级评估和消融结论，缺少具体压缩率、精度数值和效率数据，是否值得优先精读需结合全文实验细节再判断。

</details>

<details>
<summary>Abstract</summary>

Language 3D Gaussian Splatting enables open-vocabulary scene understanding by associating Gaussian primitives with language features. These semantic attributes increase model storage, while most existing 3DGS compression methods are designed mainly to preserve RGB rendering quality. One straightforward approach is to apply sparsification and quantization sequentially. However, pruning based only on rendering quality can remove Gaussians that have small RGB contributions but are important for semantic prediction. Once removed, their semantic information cannot be recovered by later quantization. We propose ClunoGS, a compact framework for Language 3DGS that combines semantics-aware Gaussian sparsification and vector quantization in a unified constrained objective. Semantic supervision is used during sparsification, and the objective jointly considers rendering quality, semantic accuracy, and compactness. We optimize the unified objective with alternating primal, sparsification, quantization, and dual updates. We evaluate ClunoGS on open-vocabulary localization and segmentation using the LERF and ScanNet-10 benchmarks. Under aggressive compression, our unified, semantics-aware formulation substantially alleviates the degradation of semantic representations caused by sequential compression and semantics-agnostic Gaussian sparsification. Ablations further show that jointly coordinating sparsification and quantization better preserves semantic accuracy than applying them independently.

</details>

#### 2026-10-21 - AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments

**Authors:** Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Mingsheng Li, Qingsong Yan, Chao Yan, Yuhang Zhang, Mir Feroskhan
**Links:** [abs](https://arxiv.org/abs/2610.29699) - [pdf](https://arxiv.org/pdf/2610.29699)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments
- 作者：Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Mingsheng Li, Qingsong Yan, Chao Yan, Yuhang Zhang, Mir Feroskhan
- 出版日期：2026-10-21T13:13:00Z
- 分类：主分类为 Neural Scene Representations & Rendering；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.29699 ；PDF https://arxiv.org/pdf/2610.29699

### 一句话总结
论文提出 AirPlayground，一个面向空中导航策略训练与评估的统一基准，包含 94 个真实感重建环境、自动化专家飞行数据采集流程、可扩展 API，以及多范式基线在已见/未见环境中的闭环评测。

### 研究问题
现有大规模空中资源在两方面存在局限：（1）缺少面向不同策略形式的密集采样飞行演示；（2）缺少覆盖广泛环境、可用于标准化闭环评估的资源。论文希望解决空中导航策略训练数据与标准化闭环评测环境不足的问题。

### 核心思路/方法
论文构建 94 个真实感 3D Gaussian Splatting（3DGS）环境，覆盖室内、城市户外和植被场景，并配有对齐的碰撞几何。基于这些环境，论文开发场景自适应流程自动采集专家飞行数据，得到 94K 演示和 46.5M 同步的观测-状态-动作样本，频率为 50 Hz。论文还提供可扩展 API，支持在共享语料上训练不同策略形式，并在对应环境中按统一协议评估。论文在三种导航设置、已见和未见环境中对四类策略范式的七个基线进行基准测试，并进一步考察 ACT 的规模扩展行为；同时分析离线预测误差与闭环结果之间的关系。

### 主要贡献
- 构建 94 个真实感 3DGS 空中导航环境，覆盖室内、城市户外和植被场景，并提供对齐碰撞几何。
- 提出场景自适应自动化专家飞行采集流程，产出 94K 演示和 46.5M 同步观测-状态-动作样本（50 Hz）。
- 提供可扩展 API，支持不同策略形式的训练与统一协议下的闭环评估。
- 建立跨三种导航设置、四类策略范式、七个基线的已见/未见环境基准测试。
- 给出 ACT 的规模扩展结果：训练语料从 5 个场景扩展到 70 个场景，已见和未见环境的中位成功率分别从 30.6% 和 16.8% 提升到 41.2% 和 29.4%。
- 分析离线预测误差、执行协议和场景交互对闭环性能的作用。

### 局限性
摘要未提供足够信息。摘要未说明环境重建精度、数据采集成本、基线覆盖范围之外的泛化性、真实世界部署差距或计算资源需求等局限。

### 阅读优先级
中。理由：该论文聚焦空中导航基准、3DGS 重建环境、大规模专家演示与闭环评估，问题定义和资源贡献较明确；但摘要未提供具体方法细节、基线配置和局限分析，是否适合深入阅读取决于读者对空中导航基准、3DGS 场景资源或闭环策略评估的兴趣。

</details>

<details>
<summary>Abstract</summary>

Large-scale aerial resources provide a foundation for learning navigation across diverse environments. However, existing resources remain limited in providing (1) densely sampled flight demonstrations for learning different policy formulations and (2) broad environment coverage for standardized closed-loop evaluation. To address these limitations, we introduce AirPlayground, a unified benchmark for training and evaluating aerial navigation policies across diverse environments. We first construct 94 photorealistic 3D Gaussian Splatting (3DGS) environments spanning indoor, urban outdoor, and vegetation settings, with aligned collision geometry. Building on these environments, we develop a scene-adaptive pipeline for automated expert flight collection, yielding 94K demonstrations and 46.5M synchronized observation-state-action samples at 50 Hz. We further provide an extensible API that supports training different policy formulations on this shared corpus and evaluating them under unified protocols in the corresponding environments. We benchmark seven baselines spanning four policy paradigms across three navigation settings in seen and unseen environments, and further examine scaling behavior with ACT. Scaling ACT's training corpus from 5 to 70 scenes raises median success rates on seen and unseen environments from 30.6% and 16.8% to 41.2% and 29.4%, respectively. Through this shared training and evaluation framework, AirPlayground supports analysis of how offline prediction errors relate to closed-loop outcomes. Our analyses highlight the roles of prediction errors, execution protocols, and scene interactions in closed-loop performance.

</details>

#### 2026-10-21 - AutoPhyX: Automatic Text-Condition Physics Property Generation

**Authors:** Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang
**Links:** [abs](https://arxiv.org/abs/2610.29517) - [pdf](https://arxiv.org/pdf/2610.29517)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AutoPhyX: Automatic Text-Condition Physics Property Generation
- 作者：Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang
- 出版日期：2026-10-21T10:05:23Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.29517 ；PDF https://arxiv.org/pdf/2610.29517

### 一句话总结
AutoPhyX 是一个文本条件驱动的框架，用于预测空间变化的物理属性，以支持高保真 4D 物理仿真中的物理参数分配。

### 研究问题
论文针对高保真 4D 物理仿真中“准确物理参数分配”的难题。摘要指出已有方法存在两个瓶颈：一是依赖计算密集的逐场景优化；二是仅从纯视觉输入预测参数，存在固有歧义，例如仅凭橡胶外观无法区分其刚度。因此，研究问题是如何在避免上述瓶颈的情况下，为多样化材质属性生成与语义和物理一致的参数分配。

### 核心思路/方法
摘要给出的核心思路包括：
1. 提出文本条件框架 AutoPhyX，用于预测空间变化的物理属性。
2. 由于训练稳健的前馈模型需要细粒度监督，作者首先引入一种“部件可控的数据生成流程”，将复杂 3D 资产分解为语义上不同的组件，并为它们配对物理上合理、多样的参数及对应文本描述。
3. 基于该数据，AutoPhyX 采用跨模态调制机制，使文本特征动态调制视觉特征，以实现精确的物理 grounding。
4. 方法将属性预测构建在体素场中，从而兼容多种 3D 表示，包括网格、点云、Gaussian Splatting 和 NeRF。
5. 摘要称实验表明该方法可在单次前向传播中实现物理上合理、文本驱动的参数分配，并对野外物体具有较高准确率和稳健泛化能力。

### 主要贡献
- 提出 AutoPhyX，一个文本条件驱动的空间变化物理属性预测框架。
- 引入部件可控的数据生成流程，用于生成带细粒度监督的 3D 资产、物理参数与文本描述配对数据。
- 设计跨模态调制机制，利用文本特征动态调制视觉特征以进行物理 grounding。
- 将属性预测表述在体素场中，以兼容多种 3D 表示形式。
- 摘要声称方法支持单次前向传播的文本驱动参数分配，并具备较高准确率和对野外物体的泛化能力。

### 局限性
摘要未提供足够信息。论文摘要未说明方法的具体失败情形、数据生成流程的适用范围、计算成本、对文本描述质量的敏感性，也未给出实验设置、定量指标和对比基线的细节。

### 阅读优先级
中。理由：该论文关注文本条件物理属性预测与 4D 物理仿真参数分配，问题定义清晰，且提出数据生成与跨模态调制思路；但当前仅有摘要和元数据，缺少实验细节与定量结果，是否值得优先精读需结合全文中的实验充分性与实际应用价值进一步判断。

</details>

<details>
<summary>Abstract</summary>

High-fidelity 4D physical simulation requires accurate physical parameter assignments that align with diverse material properties. Previous methods struggle with critical bottlenecks: they either rely on computationally intensive per-scene optimization or predict parameters from purely visual inputs. The latter suffers from inherent ambiguity, e.g., the inability to distinguish the stiffness of rubber from its appearance alone. To bridge this gap, we propose AutoPhyX, a text-conditioned framework for predicting spatially-varying physical properties. Since training robust feed-forward models requires fine-grained supervision, we first introduce a novel part-controllable data generation pipeline that decomposes complex 3D assets into semantically distinct components and pairs them with physically plausible, diverse parameters and corresponding text descriptions. Leveraging this dataset, AutoPhyX employs a cross-modal modulation mechanism where text features dynamically modulate visual features for precise physical grounding. By formulating property prediction within a voxel field, AutoPhyX ensures compatibility with diverse 3D representations, including meshes, point clouds, Gaussian Splatting, and NeRF. Experiments demonstrate that our method enables physically plausible, text-driven parameter assignment in a single forward pass. It achieves high accuracy and robust generalization to in-the-wild objects, paving the way for future physics-intensive embodied and robotic applications.

</details>

#### 2026-10-21 - AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting

**Authors:** Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin
**Links:** [abs](https://arxiv.org/abs/2610.29374) - [pdf](https://arxiv.org/pdf/2610.29374)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting
- 作者：Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin
- 出版日期：2026-10-21T08:02:14Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.29374) / [PDF](https://arxiv.org/pdf/2610.29374)

### 一句话总结
AOV-GS 是一个基于 3D Gaussian Splatting 的主动建图系统，借助冻结的 SAM 与 CLIP 基础模型，把探索过程引向语义信息更丰富的视角，并在离线拟合轻量语言场后支持新视角上的开放词汇文本查询分割。

### 研究问题
论文面向部署在人类环境中的机器人建图需求：地图既要支持几何导航，也要支持超出固定标签集的开放词汇语义查询。关键挑战在于，如何在不依赖人工标注分割掩码、也不依赖闭集语义类别的情况下，为地图补充语义信息。摘要指出，现有几何驱动的主动建图只最大化覆盖，语义只是采集轨迹的被动副产品；而主动语义建图通常依赖有监督语义分割。

### 核心思路/方法
- 使用冻结的基础模型引导探索：SAM 提供实例分割掩码，CLIP 提供与语言对齐的嵌入。
- 在粗探索阶段，对几何上有前景的候选视角，根据 CLIP 掩码嵌入的新颖性重新排序，使探索偏向语义信息丰富的区域。
- 建图全过程由冻结的 SAM 和 CLIP 提供实例掩码与语言对齐嵌入。
- 离线拟合一个轻量、场景特定的语言场，直接拟合已采集的 CLIP 嵌入，而不依赖人工标注掩码，从而在新视角上实现开放词汇文本查询分割。
- 在受控比较中，使用相同的 SAM-CLIP 感知栈，与仅几何的主动规划对比。

### 主要贡献
- 提出 AOV-GS：一个主动 3D Gaussian 建图系统，用冻结基础模型引导探索，并构建开放词汇语义地图。
- 将主动探索从单纯几何覆盖转向语义信息新颖性：用 SAM 实例分割和 CLIP 掩码嵌入计算候选视角的语义新颖性并重排序。
- 以离线拟合场景特定语言场的方式，把 CLIP 嵌入转化为可文本查询的分割能力，避免人工标注掩码。
- 摘要报告：在 Replica 八个场景上，语言场平均 mIoU 较仅几何主动规划提升 1.3 个百分点，达到 34.6%；在 Matterport3D 五个场景上提升 1.8 个百分点，达到 23.1%。使用 CorrCLIP 时，Replica 上达到 35.6%，比匹配的 Geometry-based + CorrCLIP 基线高 2.0 个百分点。两个数据集上新视角 PSNR 与仅几何基线相当，Replica 上深度 L1 改善。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性或在线部署约束。
- 摘要未提供足够信息说明对 SAM/CLIP 失败情形、掩码噪声或开放词汇范围外查询的鲁棒性。
- 摘要未提供足够信息说明除 Replica 与 Matterport3D 外的泛化表现，也未说明真实机器人平台实验。
- 摘要未提供足够信息说明语言场离线拟合所需时间、数据规模及超参数敏感性。
- 摘要未提供足够信息说明与依赖有监督语义分割的主动语义建图方法的直接对比。

### 阅读优先级
中。理由：论文主题同时涉及 3D Gaussian Splatting、主动建图与开放词汇语义，和主分类及机器人应用次分类直接相关；摘要给出了明确的受控对比与量化增益，方法路线清晰。但增益幅度相对有限，摘要层面的分析更偏系统整合与探索重排序；若关注开放词汇机器人建图或主动语义探索，值得阅读；若只关注大幅性能突破，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Robots deployed in human-centered environments need maps that support both geometric navigation and open-vocabulary semantic queries beyond a fixed label set. A key challenge is enriching such maps with semantic information without relying on manually annotated segmentation masks or closed-set semantic categories. Existing geometry-driven active mapping maximizes coverage but treats semantics as a passive by-product of the collected trajectory, whereas active semantic mapping typically depends on supervised semantic segmentation. We present AOV-GS, an active 3D Gaussian mapping system that guides exploration using frozen foundation models. During coarse exploration, AOV-GS re-ranks geometrically promising candidate views according to CLIP mask-embedding novelty computed from SAM instance segmentation, biasing exploration toward semantically informative regions. Frozen SAM and CLIP provide instance masks and language-aligned embeddings throughout mapping, while a lightweight scene-specific language field is fitted offline directly to the collected CLIP embeddings rather than manually annotated masks, enabling open-vocabulary text-query segmentation on novel views. In a controlled comparison using the same SAM-CLIP perception stack, AOV-GS improves average language-field mIoU over geometry-only active planning by 1.3 percentage points on Replica (34.6% on eight scenes) and by 1.8 points on Matterport3D (23.1% on five scenes). With CorrCLIP, AOV-GS reaches 35.6% on Replica, 2.0 points above the matched Geometry-based + CorrCLIP baseline. Novel-view PSNR remains comparable to the geometry-only baseline on both datasets while depth L1 improves on Replica. Code is available at https://github.com/OptimusFaber/AOV-GS.

</details>

#### 2026-10-21 - DriftNeRF: Cross-Ray Density Drifting for Sparse-View Neural Radiance Fields

**Authors:** Juntang Wang, Yihan Wang, Sheng'en Li, Hao Wu, Dongmian Zou, Shixin Xu
**Links:** [abs](https://arxiv.org/abs/2610.29106) - [pdf](https://arxiv.org/pdf/2610.29106)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DriftNeRF: Cross-Ray Density Drifting for Sparse-View Neural Radiance Fields
- 作者：Juntang Wang, Yihan Wang, Sheng'en Li, Hao Wu, Dongmian Zou, Shixin Xu
- 出版日期：2026-10-21T02:49:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.29106) / [PDF](https://arxiv.org/pdf/2610.29106)

### 一句话总结
论文指出稀疏视角下 NeRF 的渲染损失逐射线独立求和、缺少跨射线密度一致性约束，并提出即插即用的 DriftNeRF 正则项，通过跨射线密度漂移场抑制无支撑的密度分歧。

### 研究问题
NeRF 在稠密图像集合下可合成逼真新视角，但在可用视角很少时质量急剧下降。作者将这一缺陷归因于优化目标本身：渲染损失是对独立射线的求和，不包含比较不同射线对同一空间区域所赋予密度的项，因此邻近 3D 点可能在每个训练像素都被正确重建的同时收敛到相互矛盾的密度。论文关注的核心问题是：能否显式度量并约束这种跨射线密度不一致，从而提升稀疏视角 NeRF 的表现。

### 核心思路/方法
作者在训练中直接测量“跨射线密度不一致”（cross-ray density disagreement），并报告其在原始 NeRF 中保持较高、在基于频率的正则化下仅偶然下降、且在稀疏情形下与留出集质量同向变化。基于此，论文提出 DriftNeRF：一个在密度采样上实例化“漂移场”（drifting-field）模板的即插即用正则项。具体地，一个带掩码的指数核将其他射线上邻近点的密度聚合为 stop-gradient 的共识目标，由此得到的漂移场惩罚缺乏支撑的密度分歧，同时保留已被一致认同的边界。该正则项只读取采样位置、射线标识和预测密度，因此不需要预训练模型、外部几何或额外图像，并可跨场参数化迁移。

### 主要贡献
- 将稀疏视角 NeRF 的一个具体、可度量的缺陷归因于渲染目标：逐射线独立求和，缺少跨射线密度比较项。
- 在训练中显式度量跨射线密度不一致，并观察其在原始 NeRF 中较高、在频率正则化下仅偶然下降、且与稀疏情形下的留出质量同向变化。
- 提出 DriftNeRF 正则项：以掩码指数核聚合邻近其他射线密度，形成 stop-gradient 共识目标，惩罚无支撑分歧并保留一致边界。
- 该正则项无需预训练模型、外部几何或额外图像，且可跨场参数化迁移。
- 摘要报告：在 NeRF-Synthetic 上将残余分歧降低一个数量级；在 NeRF-Synthetic、DTU、LLFF 上，3 视角 PSNR 相比最强 MLP-NeRF 基线提升 0.42–0.65 dB；在匹配协议下与稀疏视角 Gaussian 流程相比具有竞争力，且不使用其深度、光流或共视预处理。

### 局限性
- 摘要未提供足够信息说明计算开销、训练时间或显存占用的具体影响。
- 摘要未提供足够信息说明核函数尺度、掩码阈值等超参数的选择与敏感性分析。
- 摘要未提供足够信息说明在视角数进一步减少（如 2 视角或单视角）时的表现。
- 摘要未提供足够信息说明与 Gaussian 流程比较时“匹配协议”的具体定义及公平性细节。
- 摘要未提供足够信息说明在动态场景、大尺度场景或非合成数据上的泛化边界。
- 摘要未提供足够信息说明失败案例或与频率正则化组合时的相互作用。

### 阅读优先级
高。理由：论文将稀疏视角 NeRF 的性能缺陷明确归因于渲染目标缺少跨射线密度一致性项，并给出可度量指标与即插即用正则项；摘要报告了数量级的分歧下降和一致的 PSNR 增益，且方法不依赖预训练模型、外部几何或额外图像，问题定位清晰、方法约束少，对稀疏视角神经渲染方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Neural Radiance Fields (NeRF) synthesize photorealistic novel views from dense image collections, but degrade sharply when few views are available. We attribute a specific, measurable defect to the objective itself: the rendering loss is a sum over independent rays and contains no term comparing densities that different rays assign to the same region of space, so nearby 3D points can settle on contradictory densities while every training pixel is reproduced correctly. We make this quantity explicit by measuring cross-ray density disagreement directly during training, and show that it stays high in vanilla NeRF, falls only incidentally under frequency-based regularization, and moves together with held-out quality in the sparse regime. We then close the gap with DriftNeRF, a drop-in regularizer that instantiates the drifting-field template on density samples: a masked exponential kernel aggregates densities from nearby points on other rays into a stop-gradient consensus target, and the resulting drifting field penalizes unsupported disagreement while leaving agreed-upon boundaries intact. The regularizer reads only sampled positions, ray identifiers, and predicted densities, so it requires no pretrained model, external geometry, or additional images, and transfers across field parameterizations. On NeRF-Synthetic it reduces residual disagreement by an order of magnitude, and across NeRF-Synthetic, DTU, and LLFF it improves 3-view PSNR over the strongest MLP-NeRF baseline by 0.42-0.65 dB and remains competitive with sparse-view Gaussian pipelines under a matched protocol without their depth, flow, or covisibility preprocessing.

</details>

#### 2026-10-20 - KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting

**Authors:** Radu Beche, Raoul de Charette
**Links:** [abs](https://arxiv.org/abs/2610.28615) - [pdf](https://arxiv.org/pdf/2610.28615)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting
- 作者：Radu Beche, Raoul de Charette
- 出版日期：2026-10-20T17:55:06Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.28615) / [PDF](https://arxiv.org/pdf/2610.28615)

### 一句话总结
KoalaGS 面向 3D Gaussian Splatting 的连续细节层次（LoD）场景，利用优化前由输入视图计算出的图像复杂度先验，引导训练中的高斯重定位，并借助基元重要性评分支持低容量推理，以改善不同计算预算下的渲染质量与过渡平滑性。

### 研究问题
论文关注在计算预算逐步缩小时，训练好的 3D Gaussian Splatting 场景如何用同一组基元在小前缀渲染下仍保持有效。核心问题是：随着预算降低，应决定哪些高斯保留容量。摘要指出，在 3DGS-MCMC 重建上的初步研究表明，图像复杂度可以预测重建误差在图像和 3D 空间中的集中位置；同时，简单区域包含过多高斯，且在较低预算下与复杂区域一样退化，尽管其本身更易表示。

### 核心思路/方法
方法基于一个复杂度先验：该先验由优化前的输入视图计算图像复杂度得到，用于预测重建误差集中区域。在 KoalaGS 训练中，利用该复杂度先验将重定位偏向重建较差的区域，同时确保跨 LoD 的平滑退化。随后使用基元重要性评分，使推理能够在低容量下进行，并保持场景结构。

### 主要贡献
- 提出面向连续 LoD 的复杂度感知方法，将输入视图计算的图像复杂度作为先验，用于指导训练中的高斯重定位。
- 引入基元重要性评分，以支持低容量推理并保持场景结构。
- 摘要称在三个数据集上测试，KoalaGS 在保持有竞争力的全容量质量的同时，显著改善整个预算范围内的质量，产生更平滑的 LoD 过渡，并支持更快的渐进式流式传输。
- 摘要提及初步研究发现简单区域高斯过多且低预算下退化明显，这一观察构成方法动机的一部分。

### 局限性
- 摘要未提供足够信息说明三个数据集的具体构成、规模与评测协议。
- 摘要未提供足够信息说明复杂度先验的具体计算方式、基元重要性评分的定义与实现细节。
- 摘要未提供足够信息说明与哪些基线方法进行了定量比较，以及具体指标数值。
- 摘要未提供足够信息说明训练开销、推理开销和渐进式流式传输的详细实验设置。
- 摘要未提供足够信息说明方法在何种失败场景或边界条件下可能受限。

### 阅读优先级
中。理由：该论文聚焦 3D Gaussian Splatting 在变化计算预算下的连续 LoD 与低容量推理问题，问题定义清晰，且摘要给出了复杂度先验与重要性评分相结合的方法线索，对神经场景表示与渲染方向有相关性；但摘要未提供充分的实验细节、基线对比和定量结果，是否值得优先精读需进一步查看全文的实验与实现部分。

</details>

<details>
<summary>Abstract</summary>

Deploying a trained 3D Gaussian Splatting scene under shrinking compute budgets requires one primitive set to remain effective when rendered at smaller prefixes. In this continuous level of detail (LoD) setting, the challenge is to decide which Gaussians should retain capacity as the budget decreases. A pilot study on 3DGS-MCMC reconstructions shows that image complexity, computed from the input views before optimization, predicts where reconstruction error concentrates in image and 3D space. It also reveals that simple regions contain too many Gaussians and degrade as much as complex ones at lower budgets, despite being inherently cheaper to represent. Subsequently, in KoalaGS, during training we use this complexity prior to bias relocation toward poorly reconstructed areas while ensuring smooth degradation across LoDs. A primitive importance score then enables inference at low-capacity, while preserving the scene structure. Tested across three datasets, KoalaGS maintains competitive full-capacity quality while significantly improving quality across the budget spectrum, yielding smoother transitions across LoDs, and enabling faster progressive streaming.

</details>

#### 2026-10-20 - Learning from Automatic 3D Gaussian Splatting Edits for Online Bayesian Scene Change Detection

**Authors:** Changrui Zhu, Simon Julier
**Links:** [abs](https://arxiv.org/abs/2610.28490) - [pdf](https://arxiv.org/pdf/2610.28490)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning from Automatic 3D Gaussian Splatting Edits for Online Bayesian Scene Change Detection
- 作者：Changrui Zhu, Simon Julier
- 出版日期：2026-10-20T16:36:39Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.28490) / [PDF](https://arxiv.org/pdf/2610.28490)

### 一句话总结
该论文提出一种在线场景变化检测方法：通过对参考 3D Gaussian Splatting（3DGS）模型进行自动编辑，离线生成带标签训练视图，学习场景特定的证据模型与先验/响应统计，并用广义贝叶斯证据融合在在线阶段更新累积的 3D Gaussian 场，最终由物体引导细化得到变化掩码。

### 研究问题
论文关注在线场景变化检测：随着新图像到达，需要判断哪些区域相对参考场景发生了变化。摘要指出四个关键困难：
1. 变化先验概率和证据模型事先未知；
2. 数值贝叶斯推断可能代价高昂；
3. 在线预测需要融合当前观测与历史支持；
4. 需要在不依赖人工标注的情况下获得监督信号。

### 核心思路/方法
- **离线监督生成**：对参考 3DGS 模型进行自动编辑，生成带标签的训练视图，无需人工标注；这些视图与未变化的参考观测一起，为学习场景特定证据模型、估计有效像素先验和响应统计提供监督。
- **在线贝叶斯融合**：使用广义贝叶斯证据融合，将当前证据与历史支持结合，更新变化信念。
- **闭式局部 Bayes 因子**：用学习到的响应统计参数化闭式局部 Bayes 因子，更新累积的 3D Gaussian 场。
- **最终掩码细化**：通过物体引导的细化（object-guided refinement）产生最终变化掩码。

### 主要贡献
1. 提出从自动 3DGS 编辑中离线学习场景特定证据模型与响应统计，避免人工标注。
2. 将学习到的响应统计用于闭式局部 Bayes 因子，并在在线阶段更新累积 3D Gaussian 场，结合当前证据与历史支持。
3. 给出完整的在线变化检测流程，并报告在 PASLCD 与 CCS3D 上的 mIoU 分别为 67.64% 和 75.82%，在 PASLCD 完整查询序列上达到 17.2 FPS，为所评估在线方法中最快。
4. 摘要声称该方法在 PASLCD 和 CCS3D 上取得 state-of-the-art 精度。

### 局限性
- 摘要未提供足够信息说明自动 3DGS 编辑的具体生成方式、编辑质量对监督信号的影响。
- 摘要未提供足够信息说明方法对参考 3DGS 模型质量、场景类型或动态程度的依赖与失效情形。
- 摘要未提供足够信息说明训练成本、离线学习所需数据规模或超参数敏感性。
- 摘要未提供足够信息说明与所有对比方法在精度与速度上的完整权衡细节。
- 摘要未提供足够信息说明物体引导细化对分割/物体先验的依赖程度。

### 阅读优先级
**中**。理由：论文主题属于在线场景变化检测与 3DGS/贝叶斯融合的交叉方向，摘要给出了明确的问题、方法框架和量化结果（mIoU 与 FPS），对相关方向有参考价值；但由于摘要未展开自动编辑监督的细节、实验设置和局限性，是否精读取决于读者对 3DGS 场景变化检测或在线贝叶斯证据融合的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Online scene change detection requires integrating incoming observations to determine which regions have changed relative to a reference scene. We update change beliefs as new images arrive using generalised Bayesian evidence fusion. However, the prior probability of change and evidence models are unknown beforehand, and numerical Bayesian inference can be costly. We address these challenges by learning offline from automatic edits to a reference 3D Gaussian Splatting (3DGS) model. These edits generate labelled training views without manual annotations. Together with unchanged reference observations, they provide supervision for learning scene-specific evidence models and estimating the effective pixel prior and response statistics. Online prediction combines current evidence with historical support, while closed-form local Bayes factors, parameterized by the learned response statistics, update an accumulated 3D Gaussian field. Object-guided refinement produces the final change masks. Our method achieves state-of-the-art accuracy on PASLCD and CCS3D, with $67.64\%$ and $75.82\%$ mIoU, respectively. On PASLCD, the complete pipeline runs at $17.2$\,FPS over complete query sequences, the fastest among the evaluated online methods.

</details>

#### 2026-10-20 - HRoPE: Homography Relative Positional Encoding

**Authors:** Huachen Gao, Yang Yang, Xiaoqian Liang, Xingyu Chen, Youjia Zhang, Qi Zhang, Baorui Ma, Anpei Chen, Wei Yang
**Links:** [abs](https://arxiv.org/abs/2610.28284) - [pdf](https://arxiv.org/pdf/2610.28284)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view stereo, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HRoPE: Homography Relative Positional Encoding
- 作者：Huachen Gao, Yang Yang, Xiaoqian Liang, Xingyu Chen, Youjia Zhang, Qi Zhang, Baorui Ma, Anpei Chen, Wei Yang
- 出版日期：2026-10-20T14:36:51Z
- 分类：Neural Scene Representations & Rendering（二级分类：摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2610.28284) / [PDF](https://arxiv.org/pdf/2610.28284)

### 一句话总结
论文提出 HRoPE，将每个 patch 的局部几何建模为倾斜 3D 平面，并把由平面诱导的 token 级单应性作为相对变换注入注意力，从而在多视图 Transformer 中引入面向物理表面的几何位置编码。

### 研究问题
现有几何相对位置编码主要基于相机层面的视锥或光线步进深度，以传感器几何描述 token “从何处被观测”，但未充分刻画 token 所描绘场景区域的表面几何。论文关注如何将 patch token 显式锚定到物理表面几何上，以改善跨视角特征对齐与透视畸变校正。

### 核心思路/方法
HRoPE 沿用经典多视图立体中的倾斜支撑窗口假设，将每个 patch 的局部几何表示为一个倾斜 3D 平面。基于该平面，方法构造 token 级、平面诱导的单应性，并作为相对变换注入注意力机制。该编码不需要真实几何：平面参数可在仅使用视图合成目标的情况下端到端预测，或从基础模型导出。

### 主要贡献
- 提出面向表面的位置编码思路，将 patch token 与物理表面几何关联，而非仅依赖传感器几何。
- 设计 HRoPE，以倾斜 3D 平面表示 patch 局部几何，并将平面诱导的单应性作为注意力中的相对变换。
- 使 Transformer 获得用于校正透视畸变、跨视角对齐 patch 特征的几何先验。
- 方法无需真实几何监督，支持端到端预测平面参数或从基础模型获取。
- 在 RealEstate10K、CO3Dv2、DL3DV 上报告：最佳 HRoPE 变体在新视图合成中持续优于所评估的几何位置编码，并通过消融与分析验证有效性。

### 局限性
摘要未提供足够信息。摘要未给出计算开销、平面参数预测失败情形、对基础模型依赖程度、不同数据集上的具体指标或泛化边界的详细说明。

### 阅读优先级
高。理由：该工作直接针对多视图 Transformer 中几何位置编码的“传感器中心”局限，提出可端到端训练的表面感知替代方案，并在三个新视图合成数据集上报告一致增益；若关注多视图注意力几何先验、新视图合成或端到端平面几何建模，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Geometric Relative Positional Encoding has become the primary mechanism for injecting spatial inductive biases into multi-view transformers. Existing designs condition attention on camera-level frustums or ray-marched depth, associating cross-view tokens through the sensor geometry. Such sensor-centric formulations, however, describe only where a token is observed from, leaving the rich surface geometry of the scene region depicted by the token. In this paper, we advocate a shift toward surface-aware positional encoding that explicitly grounds patch tokens in the geometry of physical surfaces. We introduce HRoPE, which represents the local geometry of each patch as a slanted 3D plane, following the slanted support-window assumption of classical multi-view stereo. We inject token-level, plane-induced homographies into attention as relative transformations. This equips the transformer with a geometric prior for rectifying perspective distortions and aligning patch features across viewpoints. Our encoding requires no ground-truth geometry: the plane parameters can be predicted end-to-end under a view-synthesis objective alone, or derived from foundation models. Extensive experiments on RealEstate10K, CO3Dv2, and DL3DV show that our best variant of HRoPE consistently outperforms the evaluated geometric positional encodings for novel view synthesis. Extensive ablations and analysis show the effectiveness of the proposed encoding. Please refer to our project page at: https://gaohchen.github.io/HRoPE

</details>

#### 2026-10-20 - OV-Foam: How 3D Representations Shape Semantic Feature Lifting

**Authors:** Yousef Rajeh, Alejandra Esparza Pelcastre, Ivan Viola, Dominik Engel
**Links:** [abs](https://arxiv.org/abs/2610.28131) - [pdf](https://arxiv.org/pdf/2610.28131)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OV-Foam: How 3D Representations Shape Semantic Feature Lifting
- 作者：Yousef Rajeh, Alejandra Esparza Pelcastre, Ivan Viola, Dominik Engel
- 出版日期：2026-10-20T12:38:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.28131) | [PDF](https://arxiv.org/pdf/2610.28131)

### 一句话总结
论文指出，在 3D Gaussian splatting 中，基元重叠会显著影响开放词汇分割的特征反投影效果；为此，作者提出采用 PowerFoam 作为底层表示的 OV-Foam，通过无重叠的空间划分简化特征提升，并取得更接近最优的特征分配。

### 研究问题
现有开放词汇分割的特征提升方法依赖简单的反投影，将特征分配给基元。在 3D Gaussian splatting 重建中，基元重叠严重，每条射线对应大量基元，导致重建效果不理想。摘要进一步指出，只有在没有两个基元共享同一条射线时，反投影才能化为可精确求解的最小二乘问题；因此，论文关注的是：3D 表示方式如何影响语义特征提升，以及能否通过改变表示来缓解重叠带来的问题。

### 核心思路/方法
论文提出 OV-Foam，使用 PowerFoam 作为底层表示。PowerFoam 通过 power diagram 对场景进行划分，使基元之间零重叠，并显著减少每条射线上的基元数量。摘要认为，这会简化特征提升问题，使特征分配更接近最优。论文还表示，OV-Foam 的空间划分基元能够达到接近最优的分配，并在实验中显示出相比 Gaussian 基线的开放词汇分割改进。

### 主要贡献
- 指出现有特征提升方法在 3D Gaussian splatting 中因基元重叠而受限，并给出“反投影在无基元共享射线时才化为可精确求解的最小二乘问题”的观察。
- 提出 OV-Foam，采用 PowerFoam 的 power-diagram 场景划分，实现基元零重叠并减少每条射线上的基元数量。
- 表明 OV-Foam 的空间划分基元可达到接近最优的特征分配。
- 摘要称实验显示其开放词汇分割优于 Gaussian 基线。

### 局限性
摘要未提供足够信息说明具体实验设置、数据集、评估指标、计算开销、与更多基线方法的比较，以及 PowerFoam 表示在其他任务或场景中的适用性。摘要也未提供足够信息说明零重叠表示是否存在精度或表达能力方面的代价。

### 阅读优先级
中。理由：论文主题与神经场景表示、开放词汇分割和特征提升相关，核心观察清晰，方法路线明确；但当前仅基于摘要，无法判断实验规模、对比充分性和实际收益幅度。若关注 3D 表示对语义特征提升的影响，或关注 Gaussian splatting 的替代表示，可优先阅读全文；否则可作为中等优先级跟进。

</details>

<details>
<summary>Abstract</summary>

Existing feature lifting approaches for open-vocabulary segmentation rely on simple backprojection to assign features to primitives. In the case of 3D Gaussian splatting reconstruction, the primitives overlap heavily, leading to suboptimal reconstructions, governed by many primitives per ray. Backprojection, however, reduces to a least-squares solvable problem, exactly when no two primitives share a ray. Motivated by this insight, we propose OV-Foam, which uses PowerFoam as the underlying representation. This representation uses a power-diagram to partition the scene, resulting in zero overlap between primitives and a substantial reduction in primitives per ray, which ultimately simplifies the lifting problem and allows for closer-to-optimal feature assignment. We show that the space partitioning primitives of OV-Foam reach near-optimal assignment, and our experiments demonstrate improved open-vocabulary segmentation over Gaussian baselines.

</details>

#### 2026-10-20 - Differentiable Task-Driven Coded Aperture Camera Design with 3D Gaussian Scene Representations

**Authors:** Chengyang Yan, Donald G. Dansereau
**Links:** [abs](https://arxiv.org/abs/2610.28004) - [pdf](https://arxiv.org/pdf/2610.28004)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** depth estimation, Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Differentiable Task-Driven Coded Aperture Camera Design with 3D Gaussian Scene Representations
- 作者：Chengyang Yan, Donald G. Dansereau
- 出版日期：2026-10-20T10:48:08Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.28004) / [PDF](https://arxiv.org/pdf/2610.28004)

### 一句话总结
论文提出一个可微分框架，将复杂相机系统与下游感知任务联合设计，并用 3D Gaussian Splatting 表示真实拍摄重建的场景，以端到端优化编码孔径掩膜、相机参数和深度估计网络。

### 研究问题
相机设计通常由领域专家通过高成本实验完成，且与相机所服务的任务相隔离。现有联合设计方法存在两类限制：一类依赖仅限预采集 2D 图像的可微分仿真，因而只能用于光学或图像处理管线设计；另一类使用不可微相机仿真器，配合无导数或强化学习方法优化，但随着设计参数数量增加，扩展性差。论文关注的问题是：如何构建可微分框架，使复杂相机系统与下游感知任务能够联合、端到端地设计与优化。

### 核心思路/方法
论文提出一个可微分框架，用于联合设计复杂相机系统和下游感知任务。该框架使用从真实世界拍摄中重建的 3D Gaussian Splatting 表示场景，为基于梯度的优化提供可微分图像形成过程，从而在先前可微分方法难以处理的设计空间上进行优化。

作者用该框架设计两个编码孔径深度从散焦（depth-from-defocus）相机：一个单目配置和一个立体配置。优化过程联合优化编码孔径掩膜、相机参数和深度估计网络，采用端到端方式。

### 主要贡献
- 提出一个可微分框架，用于联合设计复杂相机系统与下游感知任务。
- 使用 3D Gaussian Splatting 表示从真实拍摄重建的场景，提供可微分图像形成过程，支持对较大设计空间进行基于梯度的优化。
- 将该框架用于设计单目和立体两种编码孔径 depth-from-defocus 相机，联合优化掩膜、相机参数与深度估计网络。
- 摘要称结果表明，该可微分方法优于现有编码孔径设计和不可微相机设计基线。

### 局限性
- 摘要未提供足够信息说明实验数据集规模、训练细节、评价指标和定量对比结果。
- 摘要未提供足够信息说明 3D Gaussian Splatting 重建误差对设计优化和最终任务性能的影响。
- 摘要未提供足够信息说明框架在更复杂相机系统、更多设计参数或其他感知任务上的泛化能力。
- 摘要未提供足够信息说明计算成本、优化收敛性和实际硬件制造约束。

### 阅读优先级
中。理由：该论文关注可微分相机设计与下游任务联合优化，并将 3D Gaussian Splatting 引入相机设计流程，主题与神经场景表示和渲染分类相关，具有一定方法创新性；但摘要未给出定量实验细节和充分局限性说明，是否值得深入阅读需结合对可微分相机设计、编码孔径或 depth-from-defocus 的具体兴趣进一步判断。

</details>

<details>
<summary>Abstract</summary>

Camera design heavily influences perception task performance, yet cameras are typically designed by domain experts through costly experimentation, in isolation from the tasks they serve. Existing joint-design methods either rely on differentiable simulation limited to pre-captured 2D images, restricting them to optics or image-processing pipeline design, or use non-differentiable camera simulators optimised with derivative-free or reinforcement-learning methods that scale poorly with the number of design parameters. We present a differentiable framework for jointly designing complex camera systems and downstream perception tasks. We use it to design two coded-aperture depth-from-defocus cameras, a monocular and a stereo configuration, by jointly optimising the coded aperture mask, camera parameters, and a depth estimation network end-to-end. Our framework represents scenes with 3D Gaussian Splatting reconstructed from real-world captures, providing a differentiable image formation process for gradient-based optimisation over design spaces intractable for prior differentiable approaches. Results demonstrate that our differentiable method improves over existing coded aperture design and non-differentiable camera design baselines, offering a step forward in automated and principled camera design for autonomous systems.

</details>

#### 2026-10-20 - Geometry Regularization for Vanilla NeRF via Self-Supervised Cross-Ray Consistency

**Authors:** Zongji Wang
**Links:** [abs](https://arxiv.org/abs/2610.27776) - [pdf](https://arxiv.org/pdf/2610.27776)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, radiance field, novel view synthesis, view synthesis, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry Regularization for Vanilla NeRF via Self-Supervised Cross-Ray Consistency
- 作者：Zongji Wang
- 出版日期：2026-10-20T07:40:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.27776) / [PDF](https://arxiv.org/pdf/2610.27776)

### 一句话总结
该论文为原始 NeRF（vanilla NeRF）增加一个基于自监督跨射线一致性的几何优化分支，在不使用真值深度或表面法线监督的情况下约束隐式几何，并在八个 Replica 场景上将平均 Chamfer 距离相比 vanilla NeRF 降低 30.8%。

### 研究问题
原始 NeRF 的密度场编码的几何可能噪声较大且不准确，因为不同的形状与辐射组合可能解释同一组输入图像，存在几何与辐射的歧义。论文旨在减少这种歧义，提升 vanilla NeRF 的隐式几何质量。

### 核心思路/方法
- 为 vanilla NeRF 增加一个几何优化分支，基于自监督跨射线一致性。
- 该分支从密度场中采样候选表面点，并从不同方向生成在这些点相交的虚拟射线，再用 NeRF 网络渲染其外观。
- 基于这些射线之间经可见性加权的颜色一致性，约束隐式几何。
- 进一步对隐式几何进行正则化：对表观预测不一致的候选点惩罚不透明度，并鼓励局部法线平滑。
- 这些几何约束均来自 NeRF 预测，不需要真值深度或表面法线监督。

### 主要贡献
- 提出一种面向 vanilla NeRF 的自监督跨射线一致性几何优化分支，用于缓解形状与辐射之间的歧义。
- 引入基于可见性加权颜色一致性的几何约束，并结合不透明度惩罚与局部法线平滑正则化。
- 所提几何约束无需真值深度或表面法线监督。
- 在八个 Replica 场景上，相比 vanilla NeRF 将平均 Chamfer 距离降低 30.8%。

### 局限性
摘要未提供足够信息。摘要未说明方法在其他数据集或真实场景上的表现、计算开销、训练时间、对稀疏视角或复杂材质的适用性，也未给出除 Chamfer 距离外的其他定量指标或消融实验细节。

### 阅读优先级
中。理由：该工作聚焦 vanilla NeRF 的几何质量提升，方法思路清晰且报告了明确的 Chamfer 距离改进；但摘要仅提供八个 Replica 场景上的单一主要指标，缺少更广泛的实验与局限性信息。若关注 NeRF 几何正则化与自监督一致性方向，可优先阅读；若需要全面评估其泛化性与效率，则需进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

Neural Radiance Fields (NeRF) achieve high-quality novel-view synthesis by representing a scene as a continuous volumetric radiance field. However, the geometry encoded by the density field of vanilla NeRF can be noisy and inaccurate, since different combinations of shape and radiance may explain the same input images. To reduce this ambiguity, we augment vanilla NeRF with a geometry-optimization branch based on self-supervised cross-ray consistency. Specifically, this branch samples candidate surface points from the density field, generates virtual rays that intersect at each point from different directions, and renders their appearance using the NeRF network. Based on the visibility-weighted color consistency across these rays, we constrain the implicit geometry. We further regularize the implicit geometry by penalizing opacity at candidates with inconsistent appearance predictions and encouraging local normal smoothness. These geometric constraints are derived from the NeRF predictions and require no ground-truth depth or surface-normal supervision. Experiments on eight Replica scenes show that the proposed method reduces the mean Chamfer distance by 30.8% compared with vanilla NeRF.

</details>

#### 2026-10-20 - World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation

**Authors:** Jiushu Li, Haoran Wang, Yumeng Liu, Zhiyang Dou, Yuan Liu, Yuexin Ma, Cheng Lin
**Links:** [abs](https://arxiv.org/abs/2610.27725) - [pdf](https://arxiv.org/pdf/2610.27725)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, embodied AI, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation
- 作者：Jiushu Li, Haoran Wang, Yumeng Liu, Zhiyang Dou, Yuan Liu, Yuexin Ma, Cheng Lin
- 出版日期：2026-10-20T06:43:51Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.27725) / [PDF](https://arxiv.org/pdf/2610.27725)

### 一句话总结
该论文提出 World2HOSI，一个多专家编排框架（harness），可从 3D Gaussian Splatting 场景和自然语言指令生成连续的长时程人-物-场景交互（HOSI）数据。

### 研究问题
长时程人-物-场景交互（HOSI）需要同时具备多类交互能力。现有的人-物交互（HOI）模型和人-场景交互（HSI）模型在各自领域表现良好，但单独任何一类都无法覆盖需要多种交互技能的任务。训练统一的 HOSI 模型又受限于数据稀缺且获取成本高。因此核心问题是如何在缺乏统一 HOSI 训练数据的情况下，生成连续、物理合理且多样化的长时程 HOSI 数据。

### 核心思路/方法
论文的关键观点是：长时程 HOSI 的瓶颈不在于单一模型是否更强，而在于多专家的编排（orchestration）。World2HOSI 围绕一个持久化场景状态构建闭环：该场景状态由解耦的背景资产和物体资产构成，并基于 3DGS 场景与自然语言指令驱动。一个 harness 在该状态上规划动作阶段，通过各专家原生的条件接口调用已有专家模型，并将每个动作的效果写回场景状态，使每次调用都基于不断演化的世界状态。为减少物理伪影，方法分别采用有界残差优化（bounded residual optimization）和接触驱动的物理仿真（contact-driven physics simulation）来提升人体运动与物体操作的物理合理性，同时保留交互意图。

### 主要贡献
- 提出 World2HOSI，一个面向长时程 HOSI 生成的多专家编排框架，可从 3DGS 场景和自然语言指令生成连续 HOSI 数据。
- 提出以持久化、结构化的场景状态为核心的闭环编排机制：规划动作阶段、调用专家、写回动作效果。
- 通过有界残差优化和接触驱动物理仿真分别改善人体运动与物体操作的物理合理性。
- 摘要称实验和感知用户研究表明，在评估的 HOSI 任务上取得最佳任务完成度和交互质量，并生成更多样化的数据。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、评估指标细节、基线对比范围、失败案例或计算开销等信息，因此无法基于摘要判断其方法在哪些场景下可能失效或存在何种限制。

### 阅读优先级
中。理由：该工作聚焦长时程 HOSI 数据生成与多专家编排，问题定位清晰，方法思路（持久场景状态 + 专家编排 + 物理约束）对具身智能、动画与场景交互方向有参考价值；但由于摘要未提供实验细节与定量结果，是否值得深入精读需结合全文的实验规模、基线设置和可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Long-horizon human-object-scene interaction (HOSI) is central to embodied AI, animation, and game development. Existing human-object interaction (HOI) and human-scene interaction (HSI) models excel in their respective domains, but none alone covers tasks requiring multiple interaction skills. Training unified HOSI models is hindered by scarce and costly data. We introduce World2HOSI, a multi-expert orchestration harness that generates continuous HOSI data from 3D Gaussian Splatting (3DGS) scenes and natural language instructions. Our key insight is that long-horizon HOSI hinges not on a stronger single model but on orchestration. Given a shared, structured scene state and an orchestration harness grounded in it, existing experts can jointly accomplish tasks beyond the reach of any of them alone. World2HOSI realizes this insight as a closed loop around a persistent scene state built from decoupled background and object assets. A harness plans action stages over this state, invokes experts via their native conditioning interfaces, and writes each action's effects back, so that every invocation is grounded in the evolving world. To reduce physical artifacts, bounded residual optimization and contact-driven physics simulation further ensure the physical plausibility of human motion and object manipulation, respectively, while preserving interaction intent. Experiments and a perceptual user study show that World2HOSI achieves the best task completion and interaction quality on the evaluated HOSI tasks, while generating more diverse data.

</details>

#### 2026-10-20 - RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting

**Authors:** Injae Kim, Minseok Joo, Jihwan Park, Sehyung Kim, Minseong Bae, Hyunwoo J. Kim
**Links:** [abs](https://arxiv.org/abs/2610.27712) - [pdf](https://arxiv.org/pdf/2610.27712)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting
- 作者：Injae Kim, Minseok Joo, Jihwan Park, Sehyung Kim, Minseong Bae, Hyunwoo J. Kim
- 出版日期：2026-10-20T06:30:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.27712) / [PDF](https://arxiv.org/pdf/2610.27712)

### 一句话总结
RLSplat 提出一种资源线性可扩展的前馈 3D Gaussian Splatting 框架，使表示规模、推理延迟和峰值内存都随高斯预算降低而线性下降。

### 研究问题
现有预算可控的前馈 3D Gaussian Splatting（FF3DGS）方法虽然能在推理时调整高斯数量以满足存储或渲染延迟约束，但忽略了推理本身的成本：它们先预测稠密高斯集合，再进行剪枝或选择，因此无论预算多少，延迟和峰值内存几乎保持不变。

### 核心思路/方法
RLSplat 不再采用先稠密预测再剪枝或选择的方案，而是学习一个高斯分配策略，将预算分配到局部场景区域，从而精确生成所请求数量的高斯。随后，这些高斯通过“资源线性高斯解码”进行细化：每个高斯仅关注通过高效分层邻居搜索找到的附近高斯，使解码成本随高斯数量减少而线性降低。

### 主要贡献
- 提出 RLSplat，一个资源线性的预算可控 FF3DGS 框架，使表示大小、推理延迟和峰值内存均随高斯预算减少而线性下降。
- 以学习高斯分配策略替代剪枝或选择，直接按预算生成精确数量的高斯。
- 设计资源线性高斯解码，结合高效分层邻居搜索，使每个高斯仅与邻近高斯交互。
- 在零样本评估中，RLSplat 在每个预算下均优于先前预算可控方法；在低预算下，用少 4 倍高斯仍超过最强基线，同时运行速度最高快 4.1 倍、峰值内存少 9.6 倍。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集、训练细节、失败案例或适用场景限制。

### 阅读优先级
高。理由：该工作直接针对预算可控 FF3DGS 中被忽视的推理成本问题，提出资源线性框架，并在摘要中报告了明确的性能、速度和内存优势；对关注 3D Gaussian Splatting 效率与资源受限部署的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (FF3DGS) reconstructs 3D scenes from images in a single forward pass, making it well-suited to applications that must operate within limited resource budgets. To further improve its practicality, recent budget-controllable FF3DGS methods allow the number of Gaussians to be adjusted at inference, so that the output meets a given storage limit or rendering-latency constraint. However, these methods overlook the cost of inference itself: to produce a representation with the target number of Gaussians, they first predict a dense set of Gaussians and then prune or select from it, requiring nearly constant latency and peak memory regardless of the budget. We therefore propose RLSplat, a resource-linear budget-controllable FF3DGS framework whose representation size, inference latency, and peak memory all decrease linearly as the Gaussian budget is reduced. Instead of pruning or selection, RLSplat learns a Gaussian allocation policy that distributes the budget across local scene regions, so that exactly the requested number of Gaussians is generated. These Gaussians are then refined through resource-linear Gaussian decoding, in which each Gaussian attends only to nearby Gaussians found via an efficient hierarchical neighbor search, so that the decoding cost decreases linearly with fewer Gaussians. In zero-shot evaluation, RLSplat outperforms prior budget-controllable methods at every budget, surpassing the strongest baseline even with 4$\times$ fewer Gaussians, while running up to 4.1$\times$ faster with 9.6$\times$ less peak memory at low budgets.

</details>

#### 2026-10-20 - PanoGraphGS: Unifying Panoptic Segmentation and Hierarchical 3D Scene Graphs with Gaussian Splatting

**Authors:** Jinghan Gao, Siyu Wang, Dongyu Feng, Yiyuan Pan, Rong Xiong
**Links:** [abs](https://arxiv.org/abs/2610.27696) - [pdf](https://arxiv.org/pdf/2610.27696)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, scene representation, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PanoGraphGS: Unifying Panoptic Segmentation and Hierarchical 3D Scene Graphs with Gaussian Splatting
- 作者：Jinghan Gao, Siyu Wang, Dongyu Feng, Yiyuan Pan, Rong Xiong
- 出版日期：2026-10-20T06:15:59Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.27696) / [PDF](https://arxiv.org/pdf/2610.27696)

### 一句话总结
PanoGraphGS 将全景 3D 高斯表示学习与分层 3D 场景图构建统一到一个框架中，并发布了真实世界全景场景理解数据集 NaviGS。

### 研究问题
构建支持语言引导导航的 3D 场景图，需要一种能在不同视角下一致区分语义区域和物体实例的场景表示。论文关注如何将全景分割与分层 3D 场景图构建统一起来。

### 核心思路/方法
- 在共享的高斯几何上学习语义特征与实例特征。
- 采用基于原型的语义学习和基于关联的实例学习，以产生跨视角一致的全景预测。
- 学习到的表示支持新视角全景分割和直接的高斯级全景解码。
- 引入语义感知场景图模块，恢复“楼层—房间—背景物（stuff）—物体”的层级结构以及包含关系与空间关系。
- 发布真实世界数据集 NaviGS，提供 3DGS、网格、RGB、语义和深度数据。

### 主要贡献
- 提出统一框架 PanoGraphGS，将全景 3D 高斯表示学习与分层 3D 场景图构建相结合。
- 通过原型语义学习和关联实例学习，实现跨视角一致的全景预测，并支持新视角全景分割与高斯级全景解码。
- 设计语义感知场景图模块，构建具有包含与空间关系的楼层—房间—stuff—物体层级。
- 发布真实世界全景场景理解数据集 NaviGS。
- 摘要报告：在 Replica 和 NaviGS 上，物体节点准确率平均超过最强评估基线 50 个百分点以上；在评估方法中取得 2D 全景分割的最先进性能。

### 局限性
- 摘要未提供足够信息说明方法在计算开销、实时性、大规模场景扩展性方面的表现。
- 摘要未提供足够信息说明失败案例、对标注数据依赖程度及跨数据集泛化能力的细节。
- 摘要未提供足够信息说明 NaviGS 数据集的规模、采集条件与标注质量控制。
- 摘要未提供足够信息说明与基线比较的完整实验设置和消融结果。

### 阅读优先级
高。理由：论文将全景分割、3D 高斯表示与分层 3D 场景图构建统一，并发布新数据集，摘要报告了显著的物体节点准确率提升和 2D 全景分割的先进性能，对 3D 场景理解与语言引导导航相关研究具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

3D scene graphs support language-guided navigation by organizing physical entities and their containment and spatial relations into hierarchical maps. Building such structured maps requires a scene representation that consistently distinguishes semantic regions and object instances across viewpoints. To this end, we present PanoGraphGS, a unified framework that integrates panoptic 3D Gaussian representation learning with hierarchical 3D scene graph construction. The framework learns semantic and instance features on shared Gaussian geometry. Prototype-based semantic learning and association-based instance learning produce consistent panoptic predictions across viewpoints. The learned representation supports novel-view panoptic segmentation and direct Gaussian-level panoptic decoding. A semantic-aware scene graph module further recovers a floor-room-stuff-object hierarchy with containment and spatial relations. We further release NaviGS, a real-world dataset for panoramic scene understanding. The dataset provides 3DGS, mesh, RGB, semantic, and depth data. For 3D scene graph identification, PanoGraphGS outperforms the strongest evaluated baseline in object-node accuracy by more than 50\% points on average across Replica and NaviGS. PanoGraphGS also achieves state-of-the-art performance among the evaluated methods in 2D panoptic segmentation. These results demonstrate the effectiveness of PanoGraphGS in both hierarchical 3D scene understanding and 2D panoptic segmentation. The project website is available at: https://github.com/gaojh0333/PanoGraphGS.

</details>

#### 2026-10-19 - Counting Contributions, Not Views: Occlusion-Aware Densification for 3D Gaussian Splatting

**Authors:** Marcel Rogge, René Schuster, Didier Stricker
**Links:** [abs](https://arxiv.org/abs/2610.27108) - [pdf](https://arxiv.org/pdf/2610.27108)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Counting Contributions, Not Views: Occlusion-Aware Densification for 3D Gaussian Splatting
- 作者：Marcel Rogge, René Schuster, Didier Stricker
- 出版日期：2026-10-19T18:09:10Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.27108) / [PDF](https://arxiv.org/pdf/2610.27108)

### 一句话总结
论文指出 3D Gaussian Splatting 的自适应密度控制在统计高斯可见性时忽略了遮挡，导致被完全遮挡的高斯仍被计为“已观测”，从而稀释梯度信号；为此作者提出遮挡感知的统计过滤与“平均贡献”归一化，以更准确地决定何时致密化。

### 研究问题
摘要指出的核心问题是：3D Gaussian Splatting 的 adaptive density control（ADC）依赖渲染过程中收集的每个高斯统计量，但这些统计量经过的视锥可见性过滤对遮挡不敏感——完全被遮挡的高斯仍被算作被观测到。这会稀释平均梯度信号，并在几何被遮挡的位置抑制致密化。也就是说，现有密度控制“数的是视图数”，而不是高斯是否真正对渲染有贡献。

### 核心思路/方法
- 用**遮挡感知过滤器**替换原本对遮挡不敏感的可见性过滤，使致密化统计只纳入高斯真正产生贡献的视图。
- 将密度控制判据中的**原始视图计数归一化器**替换为**平均贡献归一化器**，即不再按“被多少个视图看到”计数，而按“实际贡献多少”来归一化。
- 方法集成到基于 **StopThePop** 的框架中。
- 摘要强调这两项改动共同作用，而非单独消融：遮挡感知过滤 + 平均贡献归一化。

### 主要贡献
- 揭示并纠正了 3D Gaussian Splatting 密度控制中“遮挡盲”的统计偏差：被完全遮挡的高斯不应被计为已观测。
- 提出遮挡感知的致密化统计过滤，以及以平均贡献替代视图计数的归一化方式。
- 在遮挡严重的场景上，相对遮挡盲基线提升**每一项图像质量指标**，LPIPS 最多降低 **6%**，且所需高斯数量不到视图计数归一化器的一半。
- 在大场景所需的更长训练调度下，高斯计数保持有界，而多数判据会发散；在较小基准上，方法以竞争者数量的一小部分保持竞争力。

### 局限性
- 摘要仅报告了相对基线的指标提升与数量对比，未提供具体数据集名称、场景类别构成、训练时长、硬件配置或完整定量表格；这些细节**摘要未提供足够信息**。
- 摘要称在“遮挡严重场景”上提升每一项图像质量指标，但未列出具体指标集合与各指标数值；**摘要未提供足够信息**。
- 摘要提到“多数判据会发散”和“竞争者”，但未说明对比方法的具体清单与公平性设置；**摘要未提供足够信息**。
- 方法基于 StopThePop 框架，是否适用于其他 3DGS 变体、是否需要额外计算开销，摘要未说明；**摘要未提供足够信息**。

### 阅读优先级
**高**。理由：该工作针对 3D Gaussian Splatting 密度控制中一个具体且可复现的统计偏差（遮挡盲的可见性计数），提出的改动明确、可集成，且摘要给出了 LPIPS 最多 6% 改善与高斯数量不到基线一半的量化信号；对关注 3DGS 致密化策略、渲染效率与遮挡处理的读者具有直接参考价值。但需注意，摘要未提供数据集与完整实验细节，精读时应重点核查实验设置与消融是否支撑其主张。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting grows a dense scene from a sparse initialization through adaptive density control (ADC), driven by per-Gaussian statistics gathered during rendering. These statistics pass a frustum-based visibility filter blind to occlusion: fully occluded Gaussians still count as observed, diluting the averaged gradient signal and suppressing densification precisely where geometry is occluded. We correct this with an occlusion-aware filter that restricts densification statistics to views in which a Gaussian actually contributes, and replace the criterion's raw view-count normalizer with an average-contribution one. Integrated into a StopThePop-based framework, the two together improve every image-quality metric over the occlusion-blind baseline on occlusion-heavy scenes (up to 6% lower LPIPS), at less than half the Gaussians a view-count normalizer requires. Under the longer schedules these large scenes require, the count stays bounded where most criteria diverge, and on smaller benchmarks our method stays competitive at a fraction of the competitors' count.

</details>

#### 2026-10-19 - Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision

**Authors:** Wencan Feng, Bailing Tian, Yulin Hui, Zhiyu Li, Junjie Lu
**Links:** [abs](https://arxiv.org/abs/2610.26508) - [pdf](https://arxiv.org/pdf/2610.26508)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision
- 作者：Wencan Feng, Bailing Tian, Yulin Hui, Zhiyu Li, Junjie Lu
- 出版日期：2026-10-19T14:44:16Z
- 分类：主分类 Neural Scene Representations & Rendering；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.26508) / [PDF](https://arxiv.org/pdf/2610.26508)

### 一句话总结
该论文提出一种面向单目 MAV 飞行的几何感知规划框架，通过将深度专家学习到的规划相关特征跨模态蒸馏到 RGB 规划器中，在不显式重建深度的前提下实现避障规划，并声称在仿真中训练后可零微调迁移到真实环境。

### 研究问题
现有 MAV 高速导航系统多依赖深度相机、立体视觉或 LiDAR 获取显式几何信息，而单目相机更轻量、低成本。但单目飞行仍面临挑战：RGB 图像不提供直接度量线索，且视觉外观在不同环境中变化显著。论文旨在解决如何让单目 RGB 规划器获得与规划相关的几何信息，从而支持避障飞行的问题。

### 核心思路/方法
论文提出一个几何感知的单目视觉规划框架，输入为两帧图像、它们的相对位姿以及 MAV 状态，输出轨迹。方法不显式重建深度，而是通过跨模态蒸馏，将特权深度专家学习到的、与规划相关的表示迁移到 RGB 规划器，以特征级几何监督补充下游规划目标。框架训练流程为：首先训练基于深度的几何专家；然后利用成对 RGB-D 观测，将其规划特征蒸馏到单目分支；最后使规划器适配下游轨迹规划目标。该设计促使策略学习与规划相关的几何特征，从而支持避障。数据收集、成对 RGB-D 监督和仿真评估使用 3D Gaussian Splatting（3DGS）模拟器渲染视觉观测。仿真中训练的规划器随后部署到真实环境，无需真实世界微调，并声称实现最高 6.5 m/s 速度下的避障。

### 主要贡献
- 提出一种几何感知单目视觉规划框架，从两帧图像、相对位姿和 MAV 状态预测轨迹，不显式重建深度。
- 引入跨模态蒸馏：先训练深度几何专家，再将其规划相关特征通过成对 RGB-D 观测蒸馏到单目分支，最后适配下游轨迹规划目标。
- 使用 3DGS 模拟器进行视觉观测渲染、数据收集、成对 RGB-D 监督和仿真评估。
- 声称仿真训练的规划器可零真实世界微调部署，并在最高 6.5 m/s 速度下实现避障。

### 局限性
摘要未提供足够信息说明方法在真实环境中的泛化边界、失败案例、计算开销、对不同场景或光照条件的敏感性，以及定量评估指标和对比基线细节。摘要未提供足够信息说明 3DGS 模拟器与真实环境之间域差异的具体影响。摘要未提供足够信息说明蒸馏过程中特征对齐的假设与限制。

### 阅读优先级
中。理由：该论文关注单目 MAV 高速避障与跨模态蒸馏规划表示，问题明确且方法路线清晰，并声称零微调真实部署；但摘要未给出定量结果、对比基线和详细实验设置，是否值得深入阅读需结合全文实验部分判断。

</details>

<details>
<summary>Abstract</summary>

Existing high-speed navigation systems for micro aerial vehicles (MAVs) commonly rely on depth cameras, stereo vision, or LiDAR to obtain explicit geometric information, while monocular cameras offer a lighter and lower-cost alternative. However, monocular flight remains challenging because RGB images offer no direct metric cues and visual appearance varies considerably across environments. We propose a geometry-aware monocular visual planning framework that predicts trajectories from two image frames, their relative pose, and the MAV state. Without explicitly reconstructing depth, the proposed method complements the downstream planning objective with feature-level geometric supervision by transferring the planning-relevant representation learned by a privileged depth expert to the RGB planner through cross-modal distillation. The framework first trains a depth-based geometric expert, then distills its planning features into a monocular branch using paired RGB-D observations, and finally adapts the planner to the downstream trajectory planning objective. This design encourages the policy to learn planning-relevant geometric features, enabling collision avoidance. We further use a 3D Gaussian Splatting (3DGS) simulator to render visual observations for data collection, paired RGB-D supervision, and simulation evaluation. The planner trained in simulation is then deployed in real-world environments without real-world fine-tuning, achieving obstacle avoidance at speeds of up to 6.5 m/s.

</details>

#### 2026-10-19 - Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention

**Authors:** Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang
**Links:** [abs](https://arxiv.org/abs/2610.25887) - [pdf](https://arxiv.org/pdf/2610.25887)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, novel view synthesis, view synthesis, splatting, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention
- 作者：Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang
- 出版日期：2026-10-19T06:44:19Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页面 https://arxiv.org/abs/2610.25887 ；PDF https://arxiv.org/pdf/2610.25887

### 一句话总结
论文将稀疏视角 3D Gaussian Splatting 重新建模为少样本学习问题，把每个高斯基元视为神经元，并借助深度学习正则化思路，从数据监督增强与训练时正则化两方面抑制过拟合。

### 研究问题
稀疏视角新视角合成在 AR/VR 与实时通信中很重要，但从有限视角重建 3D 场景仍然困难。3DGS 在稠密视角下表现好，在稀疏输入下却容易出现 overfitting 与 geometry degradation。现有方法多从局部入手，分别处理数据质量或训练正则化，缺少统一且可解释的系统改进框架。

### 核心思路/方法
论文提出新的视角：从 few-shot learning 出发重新审视稀疏视角 3DGS，把每个 Gaussian primitive 当作 neuron，并利用深度学习正则化技术。在该统一框架下，通过两种策略从稀少观测中生成更有效的监督：
1. 数据相关监督增强：optical flow-guided pseudo-view synthesis 与 joint camera-scene optimization；
2. 训练时正则化：motion-aware dropout 与 early stopping，用于抑制过拟合并保持动态场景稳定性。

### 主要贡献
- 提出将稀疏视角 3DGS 视为少样本学习问题的新视角，并把高斯基元类比为神经元，借助深度学习正则化形成统一框架。
- 设计数据相关监督增强策略：optical flow-guided pseudo-view synthesis 与 joint camera-scene optimization。
- 设计训练时正则化策略：motion-aware dropout 与 early stopping，以抑制过拟合并保持动态场景稳定性。
- 在 SIGGRAPH Asia 2025 volumetric video challenge sparse-view dataset 上取得显著改进，作者称系统在该挑战赛 sparse-view track 中获得第一名。

### 局限性
摘要未提供足够信息。摘要未给出具体失败场景、计算开销、对光流质量或相机优化的敏感性、消融实验细节、与各基线的定量差距，也未说明方法在非挑战数据或更极端稀疏条件下的泛化表现。

### 阅读优先级
高。理由：该工作针对稀疏视角 3DGS 的过拟合问题提出统一且可解释的少样本学习框架，并声称在 SIGGRAPH Asia 2025 相关挑战赛稀疏视角赛道获得第一，问题重要且结果信号较强；但摘要未提供实验细节，阅读全文时需重点核查方法假设、消融与泛化证据。

</details>

<details>
<summary>Abstract</summary>

Sparse-view novel view synthesis (NVS) is essential for AR/VR and real-time communication applications, yet remains challenging when reconstructing 3D scenes from limited viewpoints. While 3D Gaussian Splatting (3DGS) excels in dense-view scenarios, it suffers from overfitting and geometry degradation under sparse inputs. Current approaches often tackle these problems from a local perspective, addressing either data quality or training regularization individually, lacking a unified and interpretable framework for systematic improvement. We introduce a new perspective that reframes sparse-view 3DGS from a few-shot learning viewpoint, treating each Gaussian primitive as a neuron and leveraging deep learning regularization techniques. Under this unified framework, our approach generates more effective supervision from scarce observations through two strategies: (1) data-related supervision enrichment via optical flow-guided pseudo-view synthesis and joint camera-scene optimization; and (2) training-time regularization via motion-aware dropout and early stopping, which suppress overfitting while preserving dynamic-scene stability. Extensive experiments on the SIGGRAPH Asia 2025 volumetric video challenge sparse-view dataset demonstrate significant improvements over state-of-the-art optimization-based and feed-forward baselines. Our system won first place in the sparse-view track of the SIGGRAPH Asia 2025 challenge.

</details>

#### 2026-10-19 - RxGS: Relightable Gaussian Stylization via BRDF Decomposition

**Authors:** Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li
**Links:** [abs](https://arxiv.org/abs/2610.25681) - [pdf](https://arxiv.org/pdf/2610.25681)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feature matching, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, inverse rendering, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RxGS: Relightable Gaussian Stylization via BRDF Decomposition
- 作者：Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li
- 出版日期：2026-10-19T02:31:17Z
- 分类：主分类为 Neural Scene Representations & Rendering；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.25681 ；PDF https://arxiv.org/pdf/2610.25681

### 一句话总结
RxGS 提出一种基于 BRDF 感知 3D 高斯表示的可重光照 3D 场景风格化框架，通过仅优化逆渲染得到的漫反射反照率场，使风格化后的场景仍可在不同光照条件下重新渲染。

### 研究问题
论文关注基于参考图像的 3D 场景风格化问题：将参考图像的外观迁移到重建的 3D 场景上，同时保持场景几何。现有方法通常优化 NeRF 或 3DGS 等神经场景模型的 RGB 外观表示，而单点颜色混合了材质反射率、环境光照、着色效果以及观察方向等因素。当风格化修改这种混合颜色时，风格化过程中的光照效果会被“烘焙”进存储的外观中，导致风格化场景无法在不同光照下重新渲染。论文旨在解决这一限制。

### 核心思路/方法
RxGS 构建在 BRDF 感知的 3D 高斯表示之上，而不是修改逐点 RGB 颜色。方法仅优化通过逆渲染恢复的漫反射反照率场，同时保持粗糙度、金属度、表面法线以及估计的环境光照不变。这样，风格化场景除被编辑的反照率外，仍保留基于物理渲染器所需的其他组件，因此仍可重光照。在优化反照率场时，RxGS 使用最近邻特征匹配损失，并对高斯中心施加空间平滑先验。评估方面，论文采用基于光流扭曲误差的 Geometry Consistency Cost（GCC）。

### 主要贡献
- 提出 RxGS，一个可重光照的 3D 场景风格化框架，基于 BRDF 感知的 3D 高斯表示。
- 与修改逐点 RGB 颜色的做法不同，仅优化逆渲染得到的漫反射反照率场，保留粗糙度、金属度、表面法线和估计环境光照不变，从而支持风格化后的重光照。
- 使用最近邻特征匹配损失与高斯中心上的空间平滑先验优化反照率场。
- 采用基于光流扭曲误差的 GCC 进行评估；摘要称 RxGS 在所有评估的 NeRF-Synthetic 场景上取得最低 GCC，并在真实拍摄场景上保持竞争力，同时支持现有基于参考的 3D 场景风格化方法不具备的可重光照风格化能力。

### 局限性
摘要未提供足够信息。仅从摘要无法确定方法在计算开销、训练时间、对逆渲染质量的依赖、真实场景泛化能力、重光照一致性的定量评估以及失败案例等方面的具体局限。

### 阅读优先级
中。理由：论文聚焦 3D 场景风格化与可重光照表示的交叉问题，提出通过 BRDF 分解仅编辑反照率以保留重光照能力的思路，对神经场景表示与渲染方向具有相关性；但摘要未提供充分的实验细节、定量重光照评估和局限性信息，是否需要优先精读取决于读者对 3DGS、逆渲染或可重光照风格化的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Reference-based 3D scene stylization transfers the appearance of a reference image onto a reconstructed 3D scene while preserving scene geometry. Recent methods perform this transfer by optimizing the appearance representation of neural scene models including Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). These methods optimize an RGB appearance representation, in which a single per-point colour combines the effects of material reflectance, environment illumination, together with the shading it produces, and the viewing direction. When stylization modifies this combined colour, the illumination effects present during stylization are baked into the stored appearance, so the stylized scene cannot be rendered under different illumination. To address this limitation, we present RxGS, a relightable 3D scene stylization framework built on a Bidirectional Reflectance Distribution Function (BRDF)-aware 3D Gaussian representation. Rather than modifying a per-point RGB colour, RxGS optimizes only the diffuse albedo field recovered by inverse rendering, while leaving roughness, metallicity, surface normals, and the estimated environment lighting unchanged. As a result, the stylized scene keeps all the components a physically-based renderer needs other than the edited albedo, and can therefore still be relit. RxGS optimizes the albedo field using a nearest-neighbour feature matching loss together with a spatial smoothness prior over Gaussian centres. We evaluate the method using a Geometry Consistency Cost (GCC) based on optical-flow warping error. RxGS achieves the lowest GCC on all evaluated NeRF-Synthetic scenes and remains competitive on real-captured scenes, while additionally supporting relightable stylization, which existing reference-based 3D scene stylization methods do not provide.

</details>

#### 2026-10-19 - SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering

**Authors:** Jianheng Liu, Yunfei Wan, Fangming Cheng, Xiangyu Hong, Zuhao Zou, Haotian Li, Longji Yin, Chunran Zheng, Jiarong Lin, Fu Zhang
**Links:** [abs](https://arxiv.org/abs/2610.25665) - [pdf](https://arxiv.org/pdf/2610.25665)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** rendering, radiance, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering
- 作者：Jianheng Liu, Yunfei Wan, Fangming Cheng, Xiangyu Hong, Zuhao Zou, Haotian Li, Longji Yin, Chunran Zheng, Jiarong Lin, Fu Zhang
- 出版日期：2026-10-19T02:12:26Z
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2610.25665；PDF https://arxiv.org/pdf/2610.25665

### 一句话总结
SpaRV 是一种稀疏辐射体素地图，通过可微光线步进进行渲染，并用不规则 LiDAR 扫描与图像共同监督，以在机器人采集数据条件下实现几何一致、可扩展的 LiDAR-视觉建图与渲染。

### 研究问题
论文针对从机器人数据构建辐射场时面临的三个挑战：1）机器人轨迹服务于任务而非重建，少量视角导致几何约束不足；2）相机位姿与内参的残余误差使地图模糊；3）地图的 GPU 内存随场景规模增长，限制大场景中的细节水平。目标是同时获得照片级真实感和几何准确的地图，并支持大规模场景。

### 核心思路/方法
- 使用稀疏辐射体素地图，并以可微光线步进进行渲染。
- 让不规则 LiDAR 扫描与图像共同监督该地图；LiDAR 深度和占据信息用于锚定约束不足的几何，法向与平滑正则项用于保持 LiDAR 点之间的平滑性。
- 为校正相机误差，SpaRV 交替进行地图训练与对相机位姿和焦距的光度优化。
- 为限制训练和渲染中的 GPU 内存，SpaRV 同时仅以一个子图保持全分辨率，其余子图保持在较粗的八叉树层级。

### 主要贡献
- 提出 SpaRV：稀疏辐射体素地图，结合可微光线步进渲染，并利用不规则 LiDAR 扫描与图像共同监督。
- 利用 LiDAR 深度与占据锚定几何，并用正则项保持 LiDAR 点间平滑。
- 通过交替地图训练与相机位姿、焦距的光度优化来校正相机误差。
- 通过“一个子图全分辨率、其余子图粗八叉树层级”的策略约束 GPU 内存。
- 摘要报告：SpaRV 在远离采集轨迹处保持几何一致，并通过优化相机参数锐化纹理；在单张 24 GB GPU 上重建了由 63,582 张图像捕获的大学校园，并模拟其他相机和 LiDAR。

### 局限性
摘要未提供足够信息。摘要未给出定量精度、运行时间、内存占用对比、失败案例或与其他方法的系统比较等细节。

### 阅读优先级
中。理由：该工作面向机器人建图与渲染中的几何一致性、相机参数优化和大场景内存可扩展性问题，与 Neural Scene Representations & Rendering 及机器人应用相关；摘要给出了明确的问题、方法要点和大规模重建结果，但未提供定量实验细节。是否优先精读取决于读者对 LiDAR-视觉联合辐射场、可扩展建图或机器人仿真/导航/巡检应用的兴趣；仅就摘要信息而言，定为中。

</details>

<details>
<summary>Abstract</summary>

Robotic simulation, navigation, and inspection need photorealistic and geometrically accurate maps. Radiance fields achieve photorealism, but building them from robot data raises three challenges. A robot's trajectory serves its task, not reconstruction, so images from few viewpoints leave the geometry under-constrained. Residual errors in camera poses and intrinsics blur the map. The map's GPU memory grows with scene size, which limits its level of detail in large scenes. We present \textbf{SpaRV}, a \textbf{Spa}rse \textbf{R}adiance \textbf{V}oxel map rendered by differentiable ray marching, which lets irregular LiDAR scans supervise it alongside images. LiDAR depth and occupancy anchor the under-constrained geometry, and normal and smoothness regularizers keep it smooth between LiDAR points. To correct camera errors, SpaRV alternates map training with photometric optimization of the camera poses and focal lengths. To bound GPU memory in training and rendering, SpaRV holds one submap at a time at full resolution and the rest at coarser octree levels. Experiments show that SpaRV keeps the geometry consistent away from the captured trajectory and sharpens textures by optimizing the camera parameters. On one 24\,GB GPU, SpaRV reconstructs a university campus captured in 63{,}582 images and simulates other cameras and LiDARs. Our code will be released at \url{https://github.com/hku-mars/SpaRV}.

</details>

#### 2026-10-18 - MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes

**Authors:** Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao
**Links:** [abs](https://arxiv.org/abs/2610.25345) - [pdf](https://arxiv.org/pdf/2610.25345)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, splatting, driving scene

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes
- 作者：Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao
- 出版日期：2026-10-18T15:40:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.25345) / [PDF](https://arxiv.org/pdf/2610.25345)

### 一句话总结
MCSplat 是一个面向驾驶场景的前馈高斯泼溅框架，通过构建规范外观空间解耦几何与相机外观，并用基于 Fisher 信息的不确定性自适应加权几何自监督，以提升多视角光度一致性与几何可靠性。

### 研究问题
论文针对稀疏多视角图像前馈高斯泼溅重建驾驶场景中的两个挑战：
1. **跨相机光度不一致**：曝光、ISP 和光照变化导致的多相机光度差异，可能被错误地吸收进高斯几何中。
2. **局部几何监督不可靠**：在深度不连续区域附近，基于法向的约束提供的局部几何监督不可靠。

### 核心思路/方法
- 从深度引导的多相机对应关系构建**规范外观空间**，将几何学习与相机特定外观解耦。
- 提出**多尺度双边网格 Transformer**，从规范渲染结果恢复原始相机外观，从而在光度监督时不污染高斯几何。
- 从光度敏感性估计**基于 Fisher 信息的不确定性**，并用其自适应加权面向表面的自监督，以提升局部几何可靠性。

### 主要贡献
- 提出 MCSplat：一个多视角一致的前馈高斯泼溅框架，面向驾驶场景。
- 构建规范外观空间以解耦几何学习与相机特定外观，缓解跨相机光度不一致对几何的污染。
- 设计多尺度双边网格 Transformer 恢复原始相机外观，支持不污染几何的光度监督。
- 引入基于 Fisher 信息的不确定性，自适应加权表面朝向自监督，改善局部几何可靠性。
- 摘要称实验显示重建质量和跨驾驶数据集泛化性提升，几何评估显示跨视角深度一致性和局部表面法向一致性增强，定性结果显示几何伪影更少、重叠视角结构更连贯。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集名称、实验设置、计算开销、实时性、失败案例或定量指标细节。

### 阅读优先级
**中**。理由：该论文聚焦驾驶场景稀疏多视角前馈高斯泼溅中的光度一致性与几何监督可靠性，问题定义清晰且方法组合有针对性；但摘要未提供具体实验细节与量化结果，是否适合优先精读取决于读者对驾驶场景重建、前馈高斯泼溅或多相机光度一致性方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors. First, cross-camera photometric inconsistency, caused by variations in exposure, ISP, and illumination, can be incorrectly absorbed into Gaussian geometry. Second, unreliable local geometric supervision arises from normal-based constraints near depth discontinuities. To address these issues, we present \textbf{MCSplat}, a multi-view consistent feed-forward Gaussian splatting framework for driving scenes. MCSplat constructs a canonical appearance space from depth-guided multi-camera correspondences to decouple geometry learning from camera-specific appearance. A multi-scale Bilateral Grid Transformer restores raw camera appearance from canonical renderings, enabling photometric supervision without contaminating Gaussian geometry. To improve local geometric reliability, we estimate Fisher-information-based uncertainty from photometric sensitivity and use it to adaptively weight surface-oriented self-supervision. Extensive experiments demonstrate improved reconstruction quality and generalization across driving datasets. Geometry-oriented evaluations further reveal enhanced cross-view depth consistency and local surface-normal agreement, while qualitative results show fewer geometric artifacts and more coherent structures across overlapping views.

</details>

#### 2026-10-18 - GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation

**Authors:** Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger
**Links:** [abs](https://arxiv.org/abs/2610.25261) - [pdf](https://arxiv.org/pdf/2610.25261)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, splatting, robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation
- 作者：Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger
- 出版日期：2026-10-18T13:31:50Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25261 ；PDF https://arxiv.org/pdf/2610.25261 ；代码 https://github.com/Bennnoo/GOFusion ；补充视频 https://youtu.be/pLQKbxQvb6I

### 一句话总结
GOFusion 是一种面向自主机器人导航的实时视觉建图系统，将 3D 高斯原语锚定到局部占据地图上，并利用栅格化集成的 Fisher 近似实现在线敏感度量化，以支持高斯剪枝和下一最佳视角规划。

### 研究问题
论文关注自主机器人导航中的实时视觉建图问题：如何同时提供用于路径规划的空间感知能力与高保真外观信息，并在位姿校正、GPU 内存受限和大规模场景下保持几何与视觉一致性。摘要还指出需要一种在线不确定性/敏感度度量，作为信息驱动的高斯剪枝与下一最佳视角规划启发式。

### 核心思路/方法
- 从视觉-惯性 SLAM 获得的位姿估计与局部占据地图构建 3D 高斯地图，并将高斯原语锚定到局部占据地图。
- 支持位姿校正，以维持几何与视觉一致性。
- 将 3D Gaussian Splatting 优化限制在活跃子图（active submaps）内，以约束 GPU 内存使用。
- 提出栅格化集成的 Fisher 近似，在线量化每个高斯原语的敏感度，并将其作为信息驱动启发式用于高斯剪枝和下一最佳视角规划。
- 在公共数据集和真实无人机飞行中进行评估，并展示利用 Fisher 启发式的全自主无人机探索以细化高斯地图。

### 主要贡献
- 提出 GOFusion 实时视觉建图系统，将高斯原语锚定到局部占据地图，兼顾路径规划所需的空间感知与高保真外观。
- 设计基于活跃子图的 3D Gaussian Splatting 优化，以限制 GPU 内存占用。
- 引入栅格化集成的 Fisher 近似，在线量化逐原语敏感度，并用于高斯剪枝与下一最佳视角规划。
- 摘要称其在建图质量上优于若干基线，并实现实时、高保真、不确定性感知的大规模建图。
- 展示使用 Fisher 信息启发式的全自主无人机探索与高斯地图细化。

### 局限性
摘要未提供足够信息。摘要未给出具体失败场景、计算开销细节、对 SLAM 位姿质量的依赖程度、不同数据集上的定量局限，也未说明 Fisher 近似在何种条件下可能失效。

### 阅读优先级
高。理由：该论文直接面向自主机器人导航中的实时建图、内存约束、不确定性感知与主动探索规划，且提供代码与补充视频；摘要明确声称在公共数据集和真实无人机飞行中验证，并展示全自主无人机探索，适合关注神经场景表示与机器人/具身应用交叉方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

In this letter, we present GOFusion, a real-time visual mapping system for autonomous robot navigation that anchors Gaussian primitives to local occupancy maps, providing both spatial awareness for path planning and high-fidelity appearance that enables information-driven robot navigation. GOFusion builds 3D Gaussian maps from pose estimates and local occupancy maps obtained via visual-inertial SLAM and enables pose corrections to maintain both geometric and visual consistency. Furthermore, it restricts the 3D Gaussian Splatting optimization to active submaps to bound GPU memory usage. Building on the appearance-rich Gaussian map, we introduce a rasterizer-integrated Fisher approximation that quantifies per-primitive sensitivity online, serving as an information-driven heuristic for Gaussian pruning and next-best-view planning. We evaluate GOFusion on public datasets and in real-world drone flights. It not only outperforms several baselines in mapping quality, but also achieves real-time, high-fidelity and uncertainty-aware mapping at scale. Finally, we demonstrate fully autonomous drone exploration for Gaussian map refinement using the proposed Fisher-informed heuristic. Code is available at https://github.com/Bennnoo/GOFusion. We provide a supplementary video demonstration at https://youtu.be/pLQKbxQvb6I.

</details>

#### 2026-10-18 - GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation

**Authors:** Yuchen Xi, Yuhan Guo, Chenwei Hou, Zixu Liu, Jin Fang, Jason Liu, Ruigang Yang
**Links:** [abs](https://arxiv.org/abs/2610.25245) - [pdf](https://arxiv.org/pdf/2610.25245)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, autonomous driving, driving scene, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation
- 作者：Yuchen Xi, Yuhan Guo, Chenwei Hou, Zixu Liu, Jin Fang, Jason Liu, Ruigang Yang
- 出版日期：2026-10-18T13:05:08Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25245 ；PDF https://arxiv.org/pdf/2610.25245 ；项目页 https://xiyuche.github.io/GeoV2V/

### 一句话总结
GeoV2V 是一个以几何为约束的视频到视频扩散框架，旨在沿新轨迹合成时序一致的驾驶场景视频，并配套提出 Para4D 合成数据集以提供跨车道变换的同步多轨迹监督。

### 研究问题
论文关注轨迹变化下的新视角合成，尤其是外推到车道偏移等未见视角时，现有方法难以生成一致视频的问题。摘要指出两类现有方法存在不足：基于重建的方法几何一致但在大视角变化下视觉质量下降；先重建后修复的方法帧视觉上看似合理，但存在几何与时序不一致。核心挑战在于真实数据集缺乏同步多轨迹监督，使跨车道变换学习困难。

### 核心思路/方法
GeoV2V 被描述为一个几何锚定的视频到视频扩散框架：它将 LiDAR 与深度导出的几何先验，与 Wan 2.1 骨干中的全视频条件相结合，用于沿新轨迹合成时序一致的驾驶视频。为缓解跨车道变换监督不足，论文引入 Para4D 合成数据集，捕获动态场景中同步的多车道驾驶视频，为车道偏移生成提供显式监督，并作为几何一致视角合成的训练先验。

### 主要贡献
- 提出 GeoV2V：几何锚定的视频到视频扩散框架，在 Wan 2.1 骨干中融合 LiDAR 和深度几何先验与全视频条件，面向新轨迹驾驶视频生成。
- 识别并针对真实数据缺乏同步多轨迹监督的问题，提出 Para4D 合成数据集，提供车道偏移生成的显式监督。
- 摘要称在 Waymo、nuScenes 和 Para4D 上的实验显示出在视觉质量、几何一致性以及大轨迹偏移下复杂光照动态鲁棒性方面的最先进性能。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、计算成本、对 LiDAR/深度先验质量的依赖程度、Para4D 与真实数据分布差异的量化影响，也未提供各数据集上的详细指标与消融结果。

### 阅读优先级
中。理由：该论文聚焦自动驾驶仿真中的新轨迹视角合成，问题定义清晰，且同时提出方法与大轨迹偏移监督数据集；摘要声称在 Waymo、nuScenes 与 Para4D 上取得最先进表现。但仅凭摘要无法判断实验细节、复现难度与实际部署成本，因此优先级定为中，适合关注驾驶场景生成、几何一致视频扩散与仿真数据构建的读者进一步阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis under trajectory changes is essential for autonomous driving simulation, yet existing methods struggle to generate consistent videos when extrapolating to unseen viewpoints such as lane shifts. Reconstruction-based approaches maintain geometric consistency but degrade in visual quality under large viewpoint changes, while reconstruct-then-restore methods often produce visually plausible frames yet suffer from geometric and temporal inconsistencies. We present GeoV2V, a geometry-grounded video-to-video diffusion framework that synthesizes temporally coherent driving videos along novel trajectories by integrating LiDAR and depth-derived geometric priors with full-video conditioning in the Wan 2.1 backbone. A key challenge in learning cross-lane transformations is the lack of synchronized multi-trajectory supervision in real-world datasets. To address this, we also introduce Para4D, a synthetic dataset capturing synchronized multi-lane driving videos within dynamic scenes, which provides explicit supervision for lane-shift generation and serves as a strong training prior for geometry-consistent view synthesis. Experiments on Waymo, nuScenes, and Para4D demonstrate state-of-the-art performance in visual quality, geometric consistency, and robustness to complex lighting dynamics under large trajectory shifts. Project page: https://xiyuche.github.io/GeoV2V/

</details>

#### 2026-10-18 - Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots

**Authors:** Que Haohua, Mingkai Liu, Handong Yao
**Links:** [abs](https://arxiv.org/abs/2610.25068) - [pdf](https://arxiv.org/pdf/2610.25068)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** SfM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots
- 作者：Que Haohua, Mingkai Liu, Handong Yao
- 出版日期：2026-10-18T07:18:24Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.25068) / [PDF](https://arxiv.org/pdf/2610.25068)

### 一句话总结
LENS 在 AMD KR260 低功耗 FPGA/ARM 平台上协同设计 SCR 定位加速器与定点 3DGS 渲染器，将 ACEsplat 风格场景记忆工作负载带到边缘设备。

### 研究问题
资源受限的机器人与自动驾驶车辆需要能在无桌面 GPU 条件下定位相机并渲染附近视图的场景记忆。SCR 与 3DGS 因无需 SfM 阶段而适用，但 ACEsplat 风格流水线以 GPU 为中心，迁移到边缘 FPGA 存在困难：SCR 对位姿敏感，3DGS 渲染不规则且对容量敏感。

### 核心思路/方法
论文提出 LENS，一个运行于 AMD KR260 的边缘场景记忆加速系统，将 ACEsplat 风格工作负载带到低功耗 FPGA/ARM 平台。作者不提出新的场景模型，而是将两个主导内核与板级数据通路协同设计：一是保持位姿精度的 INT16 SCR 加速器；二是位精确定点有序 3DGS 渲染器，将 alpha 透射率改写为 log-sum-exp 递推，并剔除可证明无用的流式高斯。摘要称所有 LENS 延迟、功耗与质量结果均为板级实测。

### 主要贡献
- 提出 LENS 边缘场景记忆加速系统，在 AMD KR260 上实现 ACEsplat 风格工作负载。
- 设计 INT16 SCR 加速器，保持 DSAC* 定位精度，延迟为 25.42 ms。
- 设计位精确定点有序 3DGS 渲染器，采用 log-sum-exp 递推表达 alpha 透射率，并移除可证明无用的流式高斯。
- 板载渲染器在 Cambridge 上达到 34.11 dB，高于 ACEsplat 的 33.20；RealEstate10K 新视图合成达到 27.84 dB，高于 26.11；全部十个 Wayspots 场景达到 ACEsplat 渲染目标。
- 与 Jetson Orin NX 相比，LENS 在每个部署任务上性能功耗比更优，提升 1.9x 至 5.7x，功耗约为其四分之一，并在定位与 Wayspots 渲染上绝对延迟更快。
- 设备端训练达到 ACEsplat 级质量，但未达到 GPU 的时间或能耗水平，作者将其标记为未来训练加速器的剩余边界。

### 局限性
- 设备端训练在时间或能耗上未达到 GPU 水平，摘要未提供具体差距数值。
- 摘要未提供功耗绝对值、FPGA 资源占用、散热或部署环境细节。
- 摘要未提供失败案例、泛化范围或更多数据集的定量结果。
- 摘要未提供与除 Jetson Orin NX 外其他边缘平台的比较。
- 摘要未提供训练加速器设计或时间表。

### 阅读优先级
中。理由：该论文聚焦边缘 FPGA 上的场景记忆加速，涉及 SCR 定位与 3DGS 渲染的协同设计，对机器人、AR 与边缘视觉系统读者有参考价值；摘要给出了板级实测的延迟、质量与性能功耗比结果，但未提供功耗绝对值、资源占用与训练差距细节，是否高优先级取决于读者对 FPGA 部署与 3DGS 边缘加速的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Resource-constrained robots and autonomous vehicles need scene memories that localize a camera and render nearby views without a desktop GPU. Scene-coordinate regression (SCR) and 3D Gaussian splatting (3DGS) fit because they avoid an SfM stage, but ACEsplat-style pipelines are GPU-centered, and moving them to an edge FPGA is hard because SCR is pose-sensitive and 3DGS rendering is irregular and capacity-sensitive. We present LENS, an edge scene-memory acceleration system on the AMD KR260 that brings an ACEsplat-style workload to a low-power FPGA/ARM platform. Rather than proposing a new scene model, LENS co-designs the two dominant kernels with the board data path: an INT16 SCR accelerator that preserves pose accuracy, and a bit-exact fixed-point ordered 3DGS renderer that rewrites alpha transmittance as a log-sum-exp recurrence and removes provably useless streamed Gaussians. All LENS latency, power, and quality results are board-measured. The SCR engine preserves DSAC* localization accuracy at 25.42 ms, the on-board renderer reaches 34.11 dB on Cambridge against ACEsplat's 33.20, novel-view synthesis on RealEstate10K reaches 27.84 dB against 26.11, and all ten Wayspots scenes reach the ACEsplat rendering target. LENS wins performance per watt over a Jetson Orin NX on every deployment task, by 1.9x to 5.7x at about a quarter of the power, and is faster in absolute latency on localization and Wayspots rendering. On-device training reaches ACEsplat-level quality but not the GPU's time or energy, marking the remaining boundary for a future training accelerator.

</details>

#### 2026-10-18 - FineSplat: Fine Patches, Local Groups, Detailed Splats

**Authors:** Hyebin Kim, Hwasik Jeong, Joonhyuk Park, Gyeongjin Kang, Jungwoo Kim, Younghyun Kim, Eunbyung Park
**Links:** [abs](https://arxiv.org/abs/2610.25011) - [pdf](https://arxiv.org/pdf/2610.25011)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FineSplat: Fine Patches, Local Groups, Detailed Splats
- 作者：Hyebin Kim, Hwasik Jeong, Joonhyuk Park, Gyeongjin Kang, Jungwoo Kim, Younghyun Kim, Eunbyung Park
- 出版日期：2026-10-18T04:44:10Z
- 分类：Neural Scene Representations & Rendering（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2610.25011) / [PDF](https://arxiv.org/pdf/2610.25011)

### 一句话总结
FineSplat 是一个围绕细粒度图像块构建的前馈式 3D Gaussian Splatting 框架，通过双重分组策略、重建误差反馈和紧凑高斯生成，在保持效率与紧凑性的同时恢复更丰富的几何与外观细节。

### 研究问题
前馈式 3D Gaussian Splatting 虽然有望实现即时场景重建与高质量新视角合成，但在细粒度几何和外观的恢复上仍然困难。作者因此重新审视前馈模型如何表示、聚合与精炼细节视觉信息。具体而言，当图像块分辨率很高、token 数量很大时，全局多视图注意力代价过高，需要更高效的局部交互机制；同时，单次前馈预测在细节恢复上存在局限。

### 核心思路/方法
论文提出 FineSplat，其核心设计包括：
1. **以细粒度图像块为基础**：框架围绕 fine-grained image patches 构建，以提升细节表达能力。
2. **双重分组策略**：由于高 token 分辨率下全局多视图注意力过于昂贵，方法结合两种互补的局部性——按视图分组（view-wise grouping）使邻近视图间高效交互；3D 空间分组则将几何相关的 token 提升到 3D 场景空间中重新连接，这些 token 在视图分组下可能从未交互。
3. **重建误差作为直接反馈**：利用重建误差提供显式的、基于渲染的信号，以恢复细粒度结构和外观，从而克服单次前馈预测的限制。
4. **紧凑高斯生成方案**：在享受细粒度特征收益的同时，避免不必要地增加高斯基元数量。

### 主要贡献
- 提出 FineSplat 前馈式 3DGS 框架，围绕细粒度图像块进行细节表示与聚合。
- 设计双重分组策略，在视图局部性与 3D 空间局部性之间互补，缓解高分辨率 token 下全局注意力的开销问题。
- 引入基于重建误差的显式渲染反馈，弥补单次前馈预测在细粒度结构恢复上的不足。
- 提出紧凑高斯生成方案，在不显著增加基元数量的前提下保留细粒度特征优势。
- 摘要声称在相同或更小的高斯预算下，以较大幅度取得 state-of-the-art 结果，同时保持效率与紧凑性。

### 局限性
- 摘要未提供足够信息说明方法的具体失败场景或适用范围限制。
- 摘要未提供足够信息说明双重分组策略在不同场景规模、视图数量或分辨率下的敏感性。
- 摘要未提供足够信息说明重建误差反馈的具体计算方式、训练成本或收敛行为。
- 摘要未提供足够信息说明“state-of-the-art by a substantial margin”所对应的数据集、指标与定量结果。
- 摘要未提供足够信息说明紧凑高斯生成方案对基元数量的具体控制机制与压缩程度。

### 阅读优先级
**高**。理由：该论文聚焦前馈式 3DGS 中细粒度几何与外观恢复这一明确难题，提出的双重分组、渲染误差反馈与紧凑高斯生成均属于方法层面的实质性设计；且摘要声称在相同或更小高斯预算下显著优于现有方法。若关注前馈 3D 重建、3D Gaussian Splatting 的效率与细节平衡，该论文具有较高阅读价值。但需注意，摘要未给出实验细节，定量结论需查阅正文验证。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) promises instant scene reconstruction with high-quality novel-view synthesis. Yet, fine-grained geometry and appearance remain difficult to recover, motivating us to revisit how feed-forward models represent, aggregate, and refine detailed visual information. We introduce FineSplat, a feed-forward 3DGS framework built around fine-grained image patches. Since global multi-view attention becomes prohibitively expensive at such high token resolutions, we develop a dual-grouping strategy that combines two complementary forms of locality: view-wise grouping enables efficient interaction among neighboring views, while 3D spatial grouping reconnects geometrically related tokens that may never have interacted under view-wise grouping by lifting them into the 3D scene space. We further leverage reconstruction error as direct feedback, providing an explicit rendering-based signal to recover fine-grained structures and appearance, thereby overcoming the limitations of one-pass feed-forward prediction. Finally, a compact Gaussian generation scheme preserves the benefits of fine-grained features without unnecessarily increasing the number of primitives. Together, these designs enable FineSplat to recover richer geometry and appearance while remaining efficient and compact, achieving state-of-the-art results by a substantial margin, under the same or smaller Gaussian budgets than existing methods.

</details>

#### 2026-10-17 - SwitchSplat: Learning Discrete Object States from Casually Captured Scenes

**Authors:** Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi
**Links:** [abs](https://arxiv.org/abs/2610.24812) - [pdf](https://arxiv.org/pdf/2610.24812)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SwitchSplat: Learning Discrete Object States from Casually Captured Scenes
- 作者：Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi
- 出版日期：2026-10-17T18:35:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.24812) | [PDF](https://arxiv.org/pdf/2610.24812)

### 一句话总结
SwitchSplat 提出一种基于 3D Gaussian Splatting 的“基础 + 槽位”分解表示，用于从随性拍摄视频中学习可交互物体的离散二值状态，并支持在推理时自由组合状态进行新视角渲染。

### 研究问题
现有 3D Gaussian Splatting 表示假设世界是静态的，无法建模随性拍摄中用户与环境交互（如开门、拨动开关、移动物体）带来的离散状态变化。时间条件动态方法（如 4DGS）将“状态被观察到的时间”与“场景处于何种状态”混为一谈，只能回放已见序列，难以组合任意物体配置。

### 核心思路/方法
论文提出 base+slot 分解：一个共享的静态 base 捕捉不变场景，每个可交互物体对应一个 slot，独立持有该物体的两种二值状态（on/off）。由于高斯到 slot 的分配完全可微，模型可直接从视频中发现各状态的几何，无需人工标注。推理时用户可自由组合各 slot 状态，并从任意视角渲染结果场景。

### 主要贡献
- 提出 SwitchSplat，据摘要称为首个通过 base+slot 分解处理离散物体状态变化的 3DGS 表示。
- 实现无需人工标注的可微状态几何发现。
- 支持推理时自由组合 slot 状态，渲染捕捉时从未见过的状态组合。
- 在新随性拍摄数据集上验证，并在新视角合成质量上优于静态与动态基线。

### 局限性
摘要未提供足够信息（未说明方法对非二值状态、复杂拓扑变化、遮挡或大规模场景的适用性，也未给出计算开销、数据集规模与失败案例等细节）。

### 阅读优先级
中。理由：该工作针对 3DGS 静态假设与动态表示状态混淆的问题，提出可组合离散状态的表示，问题定义清晰且与可交互场景重建相关；但摘要未提供定量结果、数据集细节与局限分析，需阅读全文后才能判断其实际效果与适用范围。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has made high-fidelity 3D reconstruction fast and accessible, yet existing representations assume a static world. This assumption breaks down in casual captures, where a user naturally interacts with the environment -- opening doors, toggling switches, or moving objects -- introducing discrete state changes that no current framework can model. Time-conditioned dynamic methods such as 4DGS conflate when a state was observed with what state the scene is in, limiting them to replaying seen sequences rather than composing arbitrary object configurations. We present SwitchSplat, the first 3DGS representation to address this gap via a base+slot decomposition: a shared static base captures the invariant scene, while each slot independently holds the two binary states (on/off) of one interactable object. Because the assignment of Gaussians to slots is fully differentiable, the model discovers the geometry of each state directly from video, without manual annotation. At inference, the user can freely combine slot states and render the resulting scene from any viewpoint. We validate SwitchSplat on a new casual-capture dataset and show that it outperforms static and dynamic baselines in novel-view synthesis quality, while uniquely supporting rendering of state combinations never seen during capture. Project page: https://switchsplat.github.io

</details>

#### 2026-10-17 - Directionally Factorized Illumination with Spherical Harmonic Rotation

**Authors:** Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer
**Links:** [abs](https://arxiv.org/abs/2610.24811) - [pdf](https://arxiv.org/pdf/2610.24811)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, neural rendering, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Directionally Factorized Illumination with Spherical Harmonic Rotation
- 作者：Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer
- 出版日期：2026-10-17T18:35:02Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.24811) / [PDF](https://arxiv.org/pdf/2610.24811)

### 一句话总结
论文提出可插入任意新视角合成管线的 DaFISH，将逐点发射颜色分解为表面反照率与球谐表示的光照因子，以缓解相机与光源刚性同装导致的姿态相关光照问题。

### 研究问题
许多真实采集场景中，主动光源（如相机闪光灯、水下载具灯、内窥镜或腹腔镜光源）与相机刚性连接；相机移动时光源随之移动，造成每个表面点的光照方向随视角变化。NeRF、Gaussian Splatting 等神经渲染方法会把这种姿态相关光照编码为表面颜色，从而产生外观不一致，并增加恢复底层场景的难度。

### 核心思路/方法
- 提出 **DaFISH**，可插入任意新视角合成（NVS）管线（如 NeRF）。
- 将逐点发射颜色分解为**表面反照率**与**球谐（SH）表示的光照因子**。
- 训练时直接评估 SH 光照，从而稳定地联合优化反照率、光照与几何。
- 基于闭式 SH 到辐照度的转换，训练流程从 SH 评估到体渲染完全可微。
- 提供解析式光照泛化到任意相机姿态的能力，无需重新训练。

### 主要贡献
- 针对相机同装主动光源导致的姿态相关光照问题，提出可插拔的光照分解方案 DaFISH。
- 将反照率与 SH 光照因子分解，并实现从 SH 评估到体渲染的完全可微训练。
- 支持对任意相机姿态的解析式光照泛化，无需重训练。
- 摘要在五个场景的留出帧上报告：DaFISH 在所有对比方法中取得最佳平均 PSNR（38.91 dB）、SSIM（0.9613）与 LPIPS（0.0582），并优于最强的 splatting 基线及最接近的 NeRF 基线；相较先前方法能跨视角更一致地恢复场景。

### 局限性
- 摘要未提供足够信息说明方法在非刚性光源、多光源或复杂全局光照条件下的适用性。
- 摘要未提供足够信息说明计算开销、训练时间与显存需求。
- 摘要未提供足够信息说明五个场景的具体构成、数据规模及基线方法的完整列表。
- 摘要未提供足够信息说明对极端相机姿态或稀疏视角的鲁棒性。

### 阅读优先级
**中**。理由：该工作针对相机同装主动光源这一明确且具有实际采集意义的场景，方法可插入现有 NVS 管线，并给出定量指标；但摘要仅概述核心分解与结果，未展开实验细节与适用边界，适合作为该方向的方法参考而非必须优先精读的综述性文献。

</details>

<details>
<summary>Abstract</summary>

Many real-world capture scenarios involve an active light source rigidly attached to the camera: camera flashes for dark-environment imaging, underwater vehicle lights, and endoscopic/laparoscopic medical procedures. As the camera moves, the co-mounted light moves with it, causing the illumination direction at each surface point to change across views. Neural rendering methods (NeRF, Gaussian Splatting) encode this pose-dependent illumination as surface coloration, producing appearance inconsistencies and making it harder to recover the underlying scene. We present \textbf{DaFISH}, which can be plugged into any novel-view synthesis (NVS) pipeline such as NeRF. It factorizes per-point emitted color into surface albedo and a spherical harmonic (SH)-represented illumination factor. During training, the SH illumination is evaluated directly, enabling stable joint optimization of albedo, lighting, and geometry. \textbf{DaFISH} provides analytical generalization of illumination to arbitrary camera poses without retraining. Building on the closed-form SH-to-irradiance conversion, the training pipeline is fully differentiable from SH evaluation through volume rendering. Averaged over the held-out frames of the five scenes, \textbf{DaFISH} attains the best mean PSNR (38.91\,dB), SSIM (0.9613), and LPIPS (0.0582) among all compared methods. It improves over the strongest splatting baseline as well as the closest NeRF-based baseline, while recovering the scene consistently across views compared to prior methods.

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-21 - RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation

**Authors:** Samuel Foo Enze, Manthan Patel, Fan Yang, Linus Kramer, Pascal Roth, Marco Hutter, Cesar Cadena
**Links:** [abs](https://arxiv.org/abs/2610.29845) - [pdf](https://arxiv.org/pdf/2610.29845)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation
- 作者：Samuel Foo Enze, Manthan Patel, Fan Yang, Linus Kramer, Pascal Roth, Marco Hutter, Cesar Cadena
- 出版日期：2026-10-21T15:06:08Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.29845) | [PDF](https://arxiv.org/pdf/2610.29845)

### 一句话总结
RangeNav 提出一种仅用合成数据预训练、参数量约 183k 的紧凑 LiDAR 距离图像编码器，并以导航对齐的多任务目标预训练后冻结用于策略学习，以缓解稀疏奖励下 RL 表示学习样本效率低和 3D 点云预训练编码器内存开销大的问题。

### 研究问题
论文面向在密集人群和杂乱场地中运行的自主移动机器人：这类机器人需要 360° 感知以应对周边风险；全景 LiDAR 虽能提供全向覆盖，但在稀疏奖励下用强化学习（RL）学习表示样本效率低，而现有 3D 预训练点云编码器对大规模并行 RL 仿真而言内存负担过重。摘要未提供更细化的任务设定、机器人平台通用性范围或对比方法清单。

### 核心思路/方法
- 输入形式：使用 LiDAR 距离图像（range image）而非点云编码器，以降低内存开销并适配并行 RL 仿真。
- 网络设计：采用各向异性卷积（anisotropic convolutions）与循环填充（circular padding），以处理距离图像的极端宽高比和方位角接缝问题。
- 预训练数据：完全在合成数据上预训练。
- 预训练目标：使用与导航对齐的目标，组合距离重建、语义分割与鸟瞰图（BEV）预测。
- 策略学习方式：预训练后将编码器冻结，用于策略学习。
- 模型规模：紧凑模型，约 183k 参数。

### 主要贡献
- 提出 RangeNav：一个紧凑（183k 参数）、完全基于合成数据预训练的 LiDAR 距离图像编码器，面向机器人导航。
- 针对距离图像的极端宽高比与方位角接缝，引入各向异性卷积和循环填充的网络设计。
- 提出导航对齐的预训练目标，联合距离重建、语义分割与 BEV 预测，并在预训练后冻结编码器用于策略学习。
- 摘要报告：在仿真中，相较仅重建基线，加入语义与 BEV 监督在程序化生成的训练环境和分布外真实感测试环境中，分别平均提升成功率 32.03 和 23.73 个百分点。
- 摘要报告：在 Unitree B2-W 四足机器人上进行零样本真实世界部署，在密集人群、低光环境和施工区域中表现出稳健导航能力，而有限视场深度策略在这些场景中表现困难。
- 摘要声明代码与模型将开源。

### 局限性
- 摘要未提供足够信息说明预训练合成数据与真实世界分布差异的具体范围、零样本部署的定量指标、失败案例或安全边界。
- 摘要未提供足够信息说明与现有 3D 预训练编码器在内存、训练效率或成功率上的完整对比细节。
- 摘要未提供足够信息说明方法在其他机器人形态、传感器配置或任务类型上的泛化能力。
- 摘要未提供足够信息说明消融实验的完整设置、统计显著性或计算成本细节。
- 摘要未提供足够信息说明开源许可证、代码与模型的具体发布状态。

### 阅读优先级
中。理由：该工作与 embodied/robotics 中 LiDAR 导航、预训练表示和 RL 仿真效率直接相关，且摘要给出了明确的成功率提升与真实机器人零样本部署结果；但摘要篇幅有限，未提供完整实验细节、对比基线细节与局限性讨论，适合作为相关方向的重点跟踪论文，而非仅凭摘要即可全面评估的综述性材料。

</details>

<details>
<summary>Abstract</summary>

Autonomous mobile robots operating in dense crowds and cluttered sites require $360^\circ$ perception to react to surrounding hazards. While panoramic LiDAR offers full-surround coverage, learning representations within reinforcement learning (RL) is sample-inefficient under sparse rewards, and existing 3D pretrained point-cloud encoders are too memory-heavy for massively parallel RL simulation. We present RangeNav, a compact (183k parameters) LiDAR range-image encoder pretrained entirely on synthetic data. RangeNav uses anisotropic convolutions and circular padding to handle the extreme aspect ratio and azimuthal seam of range images. We pretrain the network using a navigation-aligned objective combining range reconstruction, semantic segmentation, and bird's-eye-view (BEV) prediction, then freeze it for policy learning. In simulation, adding semantic and BEV supervision increases success rates over a reconstruction-only baseline by an average of 32.03 and 23.73 percentage points (pp) in procedurally generated training and out-of-distribution realistic test environments, respectively. Zero-shot real-world deployments on a Unitree B2-W quadruped demonstrate robust navigation through dense crowds, low-light settings, and construction zones where limited-field-of-view depth policies struggle. Code and models will be open-sourced.

</details>

#### 2026-10-20 - COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation

**Authors:** Jiahui Yang, Jason Jingzhou Liu, Ray Muxin Liu, Andrew E. Wang, Kenneth Shaw, Deepak Pathak, Ruslan Salakhutdinov
**Links:** [abs](https://arxiv.org/abs/2610.28948) - [pdf](https://arxiv.org/pdf/2610.28948)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation
- 作者：Jiahui Yang, Jason Jingzhou Liu, Ray Muxin Liu, Andrew E. Wang, Kenneth Shaw, Deepak Pathak, Ruslan Salakhutdinov
- 出版日期：2026-10-20T21:59:10Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.28948 ；PDF https://arxiv.org/pdf/2610.28948

### 一句话总结
COWBOY 提出一种可扩展的仿真到现实（sim-to-real）框架，通过“向量化环境感知全身控制器 + 局部强化学习专家 + 蒸馏为单一视觉策略”的组合，让移动机械臂根据物体与场景空间上下文自适应地完成全身灵巧抓取。

### 研究问题
移动机械臂不仅要适应物体本身，还要适应物体出现的空间上下文：底座应放在哪里、如何操作、在绕行周围场景几何时应看向何处。论文关注如何学习这种“上下文感知的全身操作”，并使其能够从仿真迁移到真实世界、扩展到大量物体与多样场景。

### 核心思路/方法
- 不直接在仿真中用强化学习（RL）学习场景适应，而是设计一个向量化的、环境感知的全身控制器（WBC），在上千个场景中通过协调底座—机械臂运动、避障和主动视觉来完成到达。
- 在局部场景中训练用于物体交互的局部 RL 专家，这些专家可跨数千个完整场景布局复用。
- 将组合后的 WBC-RL 教师策略蒸馏为一个单一的视觉策略；该策略从点云观测出发，控制移动底座、机械臂、灵巧手和可驱动相机。
- 得到的策略表现出上下文全身行为：根据观测到的场景与物体几何，自动调整底座位置、相机视角、机械臂轨迹和抓取策略。

### 主要贡献
- 提出 COWBOY：面向上下文全身操作的可扩展 sim-to-real 框架。
- 在全身灵巧抓取任务上，COWBOY 零样本迁移到数百个物体和多样野外场景，包括杂乱桌面、架子、抽屉及其他非结构化环境（摘要所述）。
- 提出将向量化环境感知 WBC 与可复用的局部 RL 专家结合，并蒸馏为单一视觉策略的路线，避免直接在仿真中用 RL 学习场景适应。
- 策略能够从点云观测同时控制移动底座、机械臂、灵巧手和可驱动相机，并展现自适应的底座放置、视角选择、轨迹与抓取策略。

### 局限性
- 摘要未提供足够信息说明真实世界实验的规模、成功率、失败模式与定量对比。
- 摘要未提供足够信息说明方法对未见物体类别、极端杂乱或动态环境的泛化边界。
- 摘要未提供足够信息说明 WBC、局部 RL 专家与蒸馏策略各自的训练成本、仿真依赖程度及 sim-to-real 差距的具体来源。
- 摘要未提供足够信息说明安全性、碰撞保证或主动视觉在真实部署中的鲁棒性。

### 阅读优先级
高。理由：该论文聚焦移动机械臂的上下文感知全身灵巧操作与可扩展 sim-to-real，方法路线（WBC + 局部 RL 专家 + 蒸馏视觉策略）对具身智能与机器人操作研究具有较强参考价值；且摘要声称零样本迁移到数百物体与多样非结构化场景，若属实具有较高影响力。但需注意：上述判断仅基于摘要与元数据，具体实验证据需阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Mobile manipulators must adapt not only to objects, but also to the spatial context in which they appear: where to position the base, how to manipulate, and where to look while navigating surrounding scene geometry. To address this, we present COWBOY, a scalable sim-to-real framework for learning such contextual whole-body manipulation. On whole-body dexterous grasping, COWBOY transfers zero-shot to hundreds of objects and diverse in-the-wild scenes, spanning cluttered tabletops, shelves, drawers, and other unstructured settings. Rather than learning scene adaptation directly with RL in simulation, a vectorized environment-aware whole-body controller (WBC) handles reaching in thousands of scenes by coordinating base-arm motion, collision avoidance, and active vision. Then, local RL experts are trained in local scenes for object interaction and can be reused across thousands of full-scene layouts. We distill these composed WBC-RL teachers into a single vision policy that controls the mobile base, arm, dexterous hand, and actuated camera from point-cloud observations. The resulting policy exhibits contextual whole-body behavior, automatically adapting base placement, camera viewpoint, arm trajectory, and grasp strategy to observed scene and object geometry. Videos are available at https://cowboy-manip.com

</details>

#### 2026-10-20 - MindView: Benchmarking Generative Multi-View Spatial Intelligence

**Authors:** Yanbo Wang, Siqi Luo, Siyu Zhang, Chenming Zhu, Wenzhao Zheng, Qian Yu, Juncheng Yan, Bin Fu, Tai Wang, Yu Qiao, Yihao Liu, Jiwen Lu
**Links:** [abs](https://arxiv.org/abs/2610.28622) - [pdf](https://arxiv.org/pdf/2610.28622)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MindView: Benchmarking Generative Multi-View Spatial Intelligence
- 作者：Yanbo Wang, Siqi Luo, Siyu Zhang, Chenming Zhu, Wenzhao Zheng, Qian Yu, Juncheng Yan, Bin Fu, Tai Wang, Yu Qiao, Yihao Liu, Jiwen Lu
- 出版日期：2026-10-20T17:58:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.28622

### 一句话总结
MindView 是一个面向生成式多视图空间智能的基准，包含来自 513 个场景的 1,500 个样本、七项任务，用于评估模型在部分多视图观测下生成空间一致视图的能力。

### 研究问题
论文关注语言引导下、从部分多视图观测生成空间一致视图的任务。摘要指出，现有空间智能评估已涉及空间接地的图像编辑等生成任务，但上述多视图生成问题仍未被充分探索。此外，摘要还考察在扩展上下文（expanded context）下模型能否有效利用额外的多视图证据。

### 核心思路/方法
- 构建 MindView 基准：包含 1,500 个样本，来自三个室内数据集的 513 个场景。
- 设置七项任务，分为两类：
  - 几何主导任务：指定相机位置和朝向的变化；
  - 语义主导任务：通过 grounding 被指对象、解释空间关系与参考系线索，推断目标视角。
- 评估十一个生成器，并进行配对上下文分析。
- 在 MindView 训练数据集上微调 BAGEL，以检验任务特定监督能否提升目标视图生成。
- 提出 MindCue：一种无需训练、由目标视图假设引导的空间证据选择器，用于改善扩展上下文下的证据利用。

### 主要贡献
- 提出 MindView 基准，用于生成式多视图空间智能评估，覆盖几何主导与语义主导两类共七项任务。
- 对十一个生成器进行评估，发现 MindView 上仍有显著改进空间；配对上下文分析显示，十一个生成器在扩展上下文设置下总体得分均更低。
- 通过微调 BAGEL，使其总体得分提升 24.3 分，并在全部七项 MindView 任务上取得增益。
- 微调后的模型在三个空间理解基准上得分更高，且未使用这些基准的标注进行训练，摘要据此提示学习生成空间接地视图可能有益于空间理解。
- 提出 MindCue，在扩展上下文下逆转总体得分下降，并超过标准上下文基线。

### 局限性
- 摘要未提供足够信息说明 MindView 在真实机器人或 AR 应用中的部署验证。
- 摘要未提供足够信息说明三个室内数据集的具体名称、数据规模分布及采样细节。
- 摘要未提供足够信息说明十一个生成器的具体名单与逐项任务结果。
- 摘要未提供足够信息说明微调 BAGEL 的超参数、训练成本与消融实验细节。
- 摘要未提供足够信息说明 MindCue 的具体实现细节、选择策略与失败案例分析。
- 摘要未提供足够信息说明空间理解基准的具体名称及评估协议。

### 阅读优先级
高。理由：该论文提出面向生成式多视图空间智能的新基准与七项任务，给出十一个生成器的评估结果、微调增益以及无需训练的证据选择方法，问题定义与评测设计对多视图生成和空间智能评估具有直接参考价值；但需注意摘要未提供实验细节，需阅读原文核实。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets. Its seven tasks form two families: geometry-dominant tasks specify changes in camera position and orientation, while semantics-dominant tasks require inferring target viewpoints by grounding referred objects and interpreting spatial relations and reference-frame cues. Evaluation of eleven generators reveals substantial room for improvement on MindView. A paired context analysis further shows that all eleven generators obtain lower overall scores under the expanded context setting. These findings motivate us to investigate whether task-specific supervision can improve target-view generation and whether models can use additional multi-view evidence effectively. We therefore fine-tune BAGEL on the MindView training dataset, improving its overall score by 24.3 points and yielding gains across all seven MindView tasks. Beyond these generation gains, the fine-tuned model also yields higher scores on three spatial-understanding benchmarks without training on their annotations, suggesting that learning to generate spatially grounded views may benefit spatial understanding. To improve evidence utilization under expanded context, we propose MindCue, a training-free spatial evidence selector guided by a target-view hypothesis. MindCue reverses the drop in overall score under expanded context and outperforms the standard-context baseline. Overall, MindView provides a concrete testbed for generative multi-view spatial intelligence.

</details>

#### 2026-10-20 - CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding

**Authors:** Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan
**Links:** [abs](https://arxiv.org/abs/2610.28530) - [pdf](https://arxiv.org/pdf/2610.28530)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding
- 作者：Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan
- 出版日期：2026-10-20T17:04:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.28530

### 一句话总结
CoGaussian 提出一种基于稀疏 3D 高斯、支持开放词汇的协同语义占据预测框架，用对齐基础模型的紧凑高斯表示在多智能体间通信并融合几何与语义信息。

### 研究问题
现有协同语义占据方法依赖密集 3D 体素标注，且只能识别预定义语义类别内的目标；论文旨在解决协同场景理解中的密集标注依赖与封闭语义类别限制问题。

### 核心思路/方法
将场景表示为与基础模型对齐的稀疏 3D 高斯集合，并以此作为多智能体之间传递和融合几何与语义信息的紧凑表示，从而进行开放词汇的协同语义占据预测。

### 主要贡献
提出 CoGaussian——一个开放词汇、基于高斯的协同语义占据预测框架；在 Semantic-OPV2V 基准上优于现有开放词汇单智能体方法，体现开放词汇协同场景理解的有效性。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、计算与通信开销、对基础模型依赖程度、失败案例或跨数据集泛化等细节；也未说明稀疏高斯表示在协同通信中的具体压缩率与鲁棒性表现。

### 阅读优先级
中。理由：论文聚焦协同感知与开放词汇 3D 场景理解，问题明确且与具身/机器人应用相关；但摘要仅报告在单一基准上优于开放词汇单智能体方法，未提供与协同基线对比、消融及系统开销等细节，需阅读全文后才能判断其方法稳健性与实际部署价值。

</details>

<details>
<summary>Abstract</summary>

Collaborative perception enables agents to retrieve the scene semantics and geometry beyond the field of view of any individual agent. This broader scene understanding enhances transportation safety and improves efficiency in multi-robot systems. However, existing collaborative semantic occupancy methods rely on dense 3D voxel annotations and are limited to recognizing objects within a predefined set of semantic classes. To overcome these limitations, we present CoGaussian, an open-vocabulary Gaussian-based collaborative semantic occupancy prediction framework. CoGaussian represents a scene as a set of foundation model-aligned sparse 3D Gaussians, which serve as a compact representation for communicating and fusing geometric and semantic information across multiple agents. On the Semantic-OPV2V benchmark, our method outperforms existing open-vocabulary single-agent approaches, highlighting the effectiveness of open-vocabulary collaborative scene understanding.

</details>

#### 2026-10-20 - Decoupling Action from Egocentric Observation for World Simulation

**Authors:** Yue Ma, Pengjie Song, Xinyu Wang, Yi He, Zeqian Long, Fangneng Zhan, Kaichen Zhou, Hongyu Liu, Hongfa Wang, Peihao Li, Haoyang Huang, Nan Duan, Qifeng Chen
**Links:** [abs](https://arxiv.org/abs/2610.27946) - [pdf](https://arxiv.org/pdf/2610.27946)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Decoupling Action from Egocentric Observation for World Simulation
- 作者：Yue Ma, Pengjie Song, Xinyu Wang, Yi He, Zeqian Long, Fangneng Zhan, Kaichen Zhou, Hongyu Liu, Hongfa Wang, Peihao Li, Haoyang Huang, Nan Duan, Qifeng Chen
- 出版日期：2026-10-20T09:52:46Z
- 分类：Embodied / Robotics / AR Applications（二级分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2610.27946 ；PDF https://arxiv.org/pdf/2610.27946

### 一句话总结
论文提出 EgoACT，一种在视频扩散模型去噪过程中实现第一人称动作迁移的测试时框架，通过结构锚定与稀疏对应校准，在没有额外几何估计器的条件下提升手-物交互的物理合理性与时序一致性，并建立了 EgoActionBench 基准。

### 研究问题
论文关注“第一人称动作迁移”：目标是将语义动作从第一人称观测中解耦出来，并在新的视觉场景中复现，以支持可扩展的世界模拟、具身策略学习和机器人数据生成。现有条件引导视频生成方法依赖显式几何控制（如手部姿态或网格），会引入几何估计误差，导致迁移到新场景时难以保持物理合理的交互；而直接提取运动模式的运动迁移方法，仅靠运动级特征无法编码丰富的接触动力学，常导致严重的手部结构崩坏和不合理的接触布局。

### 核心思路/方法
论文提出 EgoACT，一个测试时框架，直接作用于视频扩散模型的去噪过程，不需要额外的几何估计器。方法包含两个组件：
1. **Velocity-guided Structure Anchoring**：在去噪早期阶段稳定与参考一致的手-物结构；
2. **Sparse Correspondence Calibration**：在去噪中后期阶段细化可靠的局部对应关系。
二者共同用于在保持可迁移动作语义的同时，改善时序连贯性和交互真实感。论文还建立了 EgoActionBench，用于在多样第一人称操作场景中评估动作保持、视觉质量和手-物合理性。

### 主要贡献
- 提出 EgoACT，一种无需额外几何估计器、在视频扩散模型去噪过程中执行第一人称动作迁移的测试时框架。
- 设计 Velocity-guided Structure Anchoring 与 Sparse Correspondence Calibration 两个组件，分别作用于去噪早期和中后期，以稳定手-物结构并细化局部对应。
- 建立 EgoActionBench 基准，用于评估动作保持、视觉质量和手-物合理性。
- 摘要称实验表明 EgoACT 相比强基线生成更连贯、物理更合理的交互视频；具体实验设置与数值结果摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法在不同场景、不同扩散模型或不同动作类别上的泛化能力。
- 摘要未提供足够信息说明计算开销、推理效率或测试时框架的实时性。
- 摘要未提供足够信息说明 EgoActionBench 的规模、数据来源、标注方式与评价指标细节。
- 摘要未提供足够信息说明与基线对比的具体定量结果、消融实验及失败案例。
- 摘要未提供足够信息说明方法对遮挡、快速运动、复杂手-物接触等困难情形的鲁棒性。

### 阅读优先级
中。理由：该论文面向第一人称动作迁移与世界模拟，问题定义清晰，方法针对现有几何控制与运动迁移两类路线的明确缺陷提出去噪过程内的改进，并配套建立基准，对具身智能、机器人数据生成和视频生成方向有参考价值；但当前仅有摘要与元数据，缺少定量结果、基准细节和实现信息，是否值得深入精读需结合全文实验与开源情况进一步判断。

</details>

<details>
<summary>Abstract</summary>

Egocentric action transfer aims to decouple the semantic action from egocentric observations and reproduce them in new visual contexts, enabling scalable world simulation, embodied policy learning, and robotic data generation. Existing approaches to transferring actions rely on condition-guided video generation, which converts the observation video into explicit geometric controls (e.g., hand poses or meshes) to drive synthesis. However, these methods introduce geometric estimation errors, making it difficult to preserve physically plausible interactions when transferred to new scenes. Alternatively, motion transfer methods directly extract motion patterns from the observation video, yet motion-level features alone cannot encode rich contact dynamics, frequently leading to severe hand structural collapse and implausible contact layout. To address both limitations, we present EgoACT, a test-time framework for egocentric action transfer that operates directly on the denoising process of video diffusion models without requiring additional geometric estimators. EgoACT uses Velocity-guided Structure Anchoring to stabilize reference-consistent hand-object structure in the early denoising stage, and Sparse Correspondence Calibration to refine reliable local correspondences in the mid-to-late denoising stages. Together, these two components preserve transferable action semantics while improving temporal coherence and interaction realism. We further establish EgoActionBench, a benchmark for evaluating action preservation, visual quality, and hand-object plausibility across diverse egocentric manipulation scenarios. Experiments show that EgoACT generates more coherent and physically plausible interaction videos than strong baselines.

</details>

#### 2026-10-20 - VEOcc++: Learning Persistent Voxel Feature Maps for Embodied Online Semantic Occupancy Mapping and Offline Refinement

**Authors:** Ruoyu Wang, Jiahan Li, Yong Liu, Kexin Zhang
**Links:** [abs](https://arxiv.org/abs/2610.27704) - [pdf](https://arxiv.org/pdf/2610.27704)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VEOcc++: Learning Persistent Voxel Feature Maps for Embodied Online Semantic Occupancy Mapping and Offline Refinement
- 作者：Ruoyu Wang, Jiahan Li, Yong Liu, Kexin Zhang
- 出版日期：2026-10-20T06:21:40Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.27704

### 一句话总结
VEOcc++ 提出以持久稀疏体素特征图为核心的统一框架，将具身探索中的在线增量语义占用建图与探索后的离线全局地图精化连接起来。

### 研究问题
语义占用建图在具身感知场景中同时存在两类互补需求：一是在因果约束下进行在线增量建图，维护最新的全局地图；二是在探索结束后利用额外计算进行离线全局地图精化，以改善完整场景表示。论文旨在统一处理这两个阶段。

### 核心思路/方法
- 以持久稀疏体素特征图作为连接在线与离线阶段的中心表示。
- 在线探索阶段：地图随新观测区域扩展，并通过可靠性引导的更新整合对齐后的局部特征；上下文感知解码产生当前的语义占用地图。
- 离线阶段：将缓存的局部特征整合为补充证据，并与已完成的在线表示结合，进行多尺度空间精化。
- 在线建图管线在局部预测器固定的条件下，与 VEOcc 融合方法进行对比。

### 主要贡献
- 提出 VEOcc++ 统一体素中心框架，通过持久稀疏体素特征图连接在线增量语义占用建图与离线全局地图精化。
- 在线建图在 EmbodiedOcc-ScanNet 上达到 67.12% IoU 和 58.40% mIoU，摘要称其建立了在线增量建图的新 state-of-the-art。
- 在局部预测器固定时，在线建图管线相比 VEOcc 融合提升 3.70 IoU 和 3.74 mIoU，摘要将其归因于全局建图设计的显著收益。
- 离线全局地图精化仅使用探索期间获得的观测，将完整地图提升至 67.79% IoU 和 59.37% mIoU。
- 在移动机器人上的零样本部署展示了向未见环境的迁移能力、车载可行性和大规模室内建图的可扩展性。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性指标或在线更新的具体延迟。
- 摘要未提供足够信息说明离线精化的额外计算成本及其与在线阶段的定量权衡。
- 摘要未提供足够信息说明失败案例、传感器配置、环境类型覆盖范围或零样本部署的定量评测细节。
- 摘要未提供足够信息说明与更多基线方法的完整对比结果。

### 阅读优先级
高。理由：该论文直接面向具身机器人与语义占用建图，提出在线增量建图与离线精化的统一框架，并在摘要中报告了明确的 IoU/mIoU 指标、相对 VEOcc 的消融式对比以及移动机器人零样本部署，和具身感知与机器人建图任务高度相关。

</details>

<details>
<summary>Abstract</summary>

Semantic occupancy mapping supports embodied perception during exploration and detailed scene understanding afterward, giving rise to two complementary requirements: online incremental mapping for maintaining an up-to-date global map under causal constraints, and offline global map refinement for improving the completed scene representation with additional computation. We present VEOcc++, a unified voxel-centric framework that connects both stages through a persistent sparse voxel feature map. During exploration, the map expands with newly observed regions and integrates aligned local features through reliability-guided updates, while context-aware decoding produces the current semantic occupancy map. After exploration, cached local features are consolidated as complementary evidence and combined with the completed online representation for multi-scale spatial refinement. On EmbodiedOcc-ScanNet, VEOcc++ achieves 67.12\% IoU and 58.40\% mIoU, establishing new state-of-the-art performance for online incremental mapping. With the local predictor fixed, our online mapping pipeline outperforms VEOcc fusion by 3.70 IoU and 3.74 mIoU points, demonstrating substantial gains from the proposed global mapping design. Offline global map refinement further improves the completed map to 67.79% IoU and 59.37% mIoU using only the observations acquired during exploration. Zero-shot deployment on a mobile robot further demonstrates transferability to unseen environments, onboard feasibility, and scalability to large-scale indoor mapping. Project page: https://wryzju.github.io/VEOccpp/.

</details>

#### 2026-10-20 - Provisioning Robust and Efficient LiDAR Perception for Autonomous Driving

**Authors:** Tingxu Han, Zijie Shen, An Guo, Lyuke Wang, Chunrong Fang, Zhenyu Chen, Wei Song
**Links:** [abs](https://arxiv.org/abs/2610.27617) - [pdf](https://arxiv.org/pdf/2610.27617)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Provisioning Robust and Efficient LiDAR Perception for Autonomous Driving
- 作者：Tingxu Han, Zijie Shen, An Guo, Lyuke Wang, Chunrong Fang, Zhenyu Chen, Wei Song
- 出版日期：2026-10-20T04:31:30Z
- 分类：主分类 Embodied / Robotics / AR Applications；无次要分类
- 链接：[摘要](https://arxiv.org/abs/2610.27617)｜[PDF](https://arxiv.org/pdf/2610.27617)

### 一句话总结
该论文将 LiDAR 感知部署形式化为“在推理延迟与峰值 GPU 内存约束下，构建对点云损坏仍保持准确”的检测器供给问题，并通过构造损坏样本、按扰动敏感性排序样本训练、以及基于离线邻域密度测量缩减网络与采样规模来同时提升鲁棒性与资源效率。

### 研究问题
基于 LiDAR 的 3D 目标检测是自动驾驶的核心感知服务，但部署时既需要应对点云损坏的鲁棒性，又需要满足延迟和内存要求。摘要指出，现有方法将鲁棒性与资源效率分开处理，导致紧凑检测器在损坏下脆弱，而鲁棒检测器部署成本仍然较高。因此论文要解决的问题是：如何构建一个在点云损坏下仍准确、同时满足推理延迟与峰值 GPU 内存约束的检测器。

### 核心思路/方法
- **问题形式化**：将 LiDAR 感知供给表述为在点云损坏下保持准确，并满足推理延迟与峰值 GPU 内存约束的检测器构建问题。
- **鲁棒性方面**：
  - 首先构造模拟极端天气条件的损坏样本；
  - 然后离线训练候选检测器时，按扰动敏感性对干净样本和损坏样本排序，使检测器从困难的损坏样本中学习更多；
  - 扰动敏感性通过由七个异构 3D 检测器组成的集成来估计，跟踪置信度变化、BEV 重叠和未匹配检测的变化。
- **效率方面**：缩窄网络，并使用离线邻域密度测量来决定每个采样阶段处理多少点和邻居。
- **评估指标**：干净与损坏条件下的 AP（Average Precision）、推理延迟、峰值已分配 GPU 内存。

### 主要贡献
- 将 LiDAR 感知的鲁棒性与资源效率统一为带延迟和峰值 GPU 内存约束的检测器供给问题。
- 提出通过模拟极端天气的损坏样本、基于七检测器集成估计扰动敏感性、并按敏感性排序样本进行离线训练，以提升损坏条件下的检测精度。
- 提出通过缩窄网络和离线邻域密度测量确定采样阶段点数与邻居数，以降低推理延迟和峰值 GPU 内存。
- 摘要报告的结果包括：在 KITTI 的 Car 检测上使用 PointRCNN，损坏条件下 Moderate AP 相比原始检测器提升 3.32 点，同时平均延迟降低 19.8%、峰值已分配 GPU 内存降低 53.9%；跨两个数据集、两种检测器架构和三个目标类别，损坏条件下 AP 平均提升 4.03 点，平均推理延迟和峰值已分配 GPU 内存分别降低 14.4% 和 38.0%。
- 摘要提供了代码链接。

### 局限性
- 摘要未提供足够信息说明七个异构 3D 检测器集成的具体组成、集成估计扰动敏感性的计算开销及其对最终部署成本的影响。
- 摘要未提供足够信息说明损坏样本构造的具体类型、强度范围以及与真实极端天气分布的一致性验证。
- 摘要未提供足够信息说明延迟与内存约束在训练或网络缩窄过程中的具体建模方式与约束满足保证。
- 摘要未提供足够信息说明跨数据集、跨架构、跨类别实验的完整设置、失败案例与消融结果。
- 摘要未提供足够信息说明方法在更广泛 LiDAR 感知任务（如分割、跟踪）上的适用性。

### 阅读优先级
高。理由：该论文直接面向自动驾驶 LiDAR 3D 检测的部署问题，同时处理损坏鲁棒性与延迟/内存约束，并给出跨数据集、跨架构、跨类别的量化结果；若关注鲁棒感知或资源受限部署，摘要所示贡献与评估维度具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

LiDAR-based 3D object detection is a core perception service for autonomous driving, but deployment requires robustness to point-cloud corruption while meeting latency and memory requirements. Existing approaches address robustness and resource efficiency separately, resulting in compact detectors that are fragile under corruption or robust detectors that remain costly to deploy. We therefore formulate LiDAR perception provisioning as constructing a detector that remains accurate under point-cloud corruptions while meeting constraints on inference latency and peak GPU memory. To achieve robustness, we first craft corrupted samples that mimic extreme weather conditions. Then we train candidate detectors offline by ordering clean and corrupted samples by perturbation sensitivity, through which detectors learn more from hard corrupted samples. We estimate perturbation sensitivity using an ensemble of seven heterogeneous 3D detectors by tracking changes in confidence, BEV overlap, and unmatched detections. To improve efficiency, we narrow the network and use offline neighborhood-density measurements to determine how many points and neighbors each sampling stage processes. We evaluate our method using AP (Average Precision) under clean and corrupted conditions, inference latency, and peak allocated GPU memory. On KITTI for Car detection with PointRCNN, our method improves Moderate AP under corruption by 3.32 points over the original detector while reducing mean latency by 19.8% and peak allocated GPU memory by 53.9%. Across two datasets, two detector architectures, and three object classes, our method improves AP under corruption by 4.03 points on average over the corresponding original detectors, while reducing mean inference latency and peak allocated GPU memory by 14.4% and 38.0%, respectively. Our code is available at https://github.com/drunklibai/robust-efficient-lidar-perception.

</details>

#### 2026-10-19 - Tactile In-Hand Object Rotation: A Comparative Study of Hand Morphology in Simulation and Hardware

**Authors:** Wenhao He, Max Yang, Chenghua Lu, Yijiong Lin, David A. W. Barton, Nathan F. Lepora
**Links:** [abs](https://arxiv.org/abs/2610.26759) - [pdf](https://arxiv.org/pdf/2610.26759)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tactile In-Hand Object Rotation: A Comparative Study of Hand Morphology in Simulation and Hardware
- 作者：Wenhao He, Max Yang, Chenghua Lu, Yijiong Lin, David A. W. Barton, Nathan F. Lepora
- 出版日期：2026-10-19T17:18:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.26759 ；PDF https://arxiv.org/pdf/2610.26759

### 一句话总结
该论文比较两种低成本 LEAP Hand 手指布局（拟人化与对称式）在配备 TacTip 视触觉传感器、共享强化学习框架下的在手物体连续旋转表现，并结合仿真与硬件实验分析触觉信息、手指参与度和指尖载荷之间的关系。

### 研究问题
论文关注连续在手旋转中接触维持与接触更新如何协调，并探究手部几何结构（手指排布）与触觉反馈分别如何影响操作表现。具体比较拟人化与对称式手指布局在旋转进展、手指参与和指尖载荷上的差异，同时考察不同触觉观测条件对仿真任务表现的影响。

### 核心思路/方法
- 使用两种版本的 LEAP Hand：拟人化手指布局与对称式手指布局。
- 两种手均集成 TacTip 视触觉传感器，并采用共享的强化学习框架。
- 仿真中在 12 个未见物体上评估三种观测条件：完整触觉、二值接触、仅本体感觉。
- 硬件实验中在 10 个物体、多种手部朝向下评估完整触觉策略。
- 分析指标包括旋转进展、手指参与度、指尖载荷与操作持续时间；硬件中还记录接触测量与力数据。

### 主要贡献
- 在仿真中显示，完整触觉观测相比仅本体感觉可提高每回合平均归一化旋转量：拟人化手提高 94.8%，对称手提高 66.9%，同时平均回合持续时间更长、平均总指尖载荷更低。
- 硬件接触测量显示，拟人化手的手指参与更差异化，而对称手各手指的累积载荷分布更均匀。
- 报告对称手取得更高的平均旋转次数（高 32.0%）、更高的总体旋转速率（高 25.8%）以及更长操作持续时间。
- 额外硬件力记录显示，该对称布局的平均总指尖载荷低 19.9%。
- 将手指排布与接触组织、载荷分担联系起来，并表明更丰富的触觉信息在两种仿真本体上均支持更大的任务进展与更低的平均载荷。

### 局限性
- 摘要未提供足够信息说明仿真中不同触觉观测条件在硬件上的对应验证范围；硬件实验主要评估完整触觉策略。
- 摘要未提供足够信息说明 12 个未见物体与 10 个硬件物体的具体类别、形状分布或难度划分。
- 摘要未提供足够信息说明强化学习框架的网络结构、训练细节、奖励设计及统计显著性检验。
- 摘要未提供足够信息说明 TacTip 传感器的具体配置、校准方式及硬件力测量的完整实验协议。
- 摘要未提供足够信息说明不同手部朝向对结果的单独影响，以及仿真与硬件结果差异的系统性原因。

### 阅读优先级
中。理由：该论文涉及触觉感知、手部形态与强化学习在手内旋转中的比较研究，主题对具身操作与触觉机器人研究者有参考价值；摘要给出了明确的定量比较结果，但未提供实验细节与统计信息。若关注低成本触觉手、手指布局设计或仿真到硬件比较，可优先阅读；若仅需一般性了解，摘要已覆盖主要结论。

</details>

<details>
<summary>Abstract</summary>

Continuous in-hand rotation requires coordinated contact maintenance and renewal, linking manipulation performance to both hand geometry and tactile feedback. We investigate these relationships through rotational progress, finger participation, and fingertip loading on two versions of the low-cost LEAP Hand with anthropomorphic and symmetric finger arrangements. Both hands are integrated with TacTip vision-based tactile sensors and use a shared reinforcement learning framework. Simulation evaluates full tactile, binary touch, and proprioception-only observations on 12 unseen objects; hardware experiments evaluate full tactile policies on ten objects under multiple hand orientations. In simulation, full tactile observations increase mean normalized rotation per episode over proprioception alone by 94.8% for the anthropomorphic hand and 66.9% for the symmetric hand, with longer mean episode durations and lower mean total fingertip loads. Hardware contact measurements reveal more differentiated finger participation in the anthropomorphic hand, while cumulative loading is more evenly distributed across the symmetric hand's fingers. Overall, the symmetric hand achieves a 32.0% higher mean rotation count and a 25.8% higher aggregate rotation rate, together with longer manipulation duration. Additional hardware force recordings show a 19.9% lower mean total fingertip load for this layout. These findings relate finger arrangement to contact organization and load sharing, and show that richer tactile information supports greater task progress at lower mean loading in both simulated embodiments.

</details>

#### 2026-10-19 - Robot Learning with Vision-Language-Action Models for Agricultural Manipulation

**Authors:** Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi
**Links:** [abs](https://arxiv.org/abs/2610.26717) - [pdf](https://arxiv.org/pdf/2610.26717)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robot Learning with Vision-Language-Action Models for Agricultural Manipulation
- 作者：Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi
- 出版日期：2026-10-19T16:49:17Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.26717) / [PDF](https://arxiv.org/pdf/2610.26717)

### 一句话总结
该论文构建了一个面向农业到达与抓取任务的仿真到真实机器人学习框架，先在基于 MuJoCo 的农业仿真环境中采集专家演示，并对 Octo 与 π_{0.5} 两个预训练通用机器人策略进行适配，随后在真实 Franka Research 3 机械臂上进一步微调与评估。

### 研究问题
论文关注农业机器人操作中的困难：植物几何结构变化、遮挡以及相机视角变化。预训练视觉-语言-动作（VLA）模型和通用机器人策略有望通过多模态观测与语言指令学习操作行为来应对这些挑战，但将其适配到农业任务需要领域特定演示，而在真实机器人上采集这些演示成本高、耗时长。因此，论文研究如何通过仿真到真实的机器人学习框架，将预训练通用策略适配到农业到达与抓取任务。

### 核心思路/方法
论文提出一个面向农业到达与抓取的仿真到真实机器人学习框架，整合任务特定演示采集与预训练策略适配。具体包括：
- 构建基于 MuJoCo 的农业环境，包含多样化的番茄植株结构，用于支持演示采集与受控评估；
- 通过操纵杆遥操作采集专家演示，并使用低层控制器执行机器人动作；
- 使用仿真演示对两个预训练通用机器人策略 Octo 和 π_{0.5} 进行适配；
- 随后在真实 Franka Research 3 机械臂上使用真实机器人演示进一步微调；
- 在仿真中评估适配策略在分布内、视角/空间偏移和分布外条件下的表现，并进行真实机器人实验；
- 还研究了本体感知信息对策略性能的影响。

### 主要贡献
- 提出了一个用于农业到达与抓取的仿真到真实机器人学习框架，结合任务特定演示采集与预训练策略适配；
- 开发了基于 MuJoCo 的农业环境，包含多样化番茄植株结构，支持演示采集与受控评估；
- 将 Octo 和 π_{0.5} 两个预训练通用机器人策略适配到农业操作任务，并在仿真与真实 Franka Research 3 机械臂上进行评估；
- 比较了两种策略在分布内、视角/空间偏移和分布外条件下的表现，并考察了本体感知信息对策略性能的影响；
- 摘要报告的结果显示，π_{0.5} 的任务性能得分高于 Octo，且在分布偏移下退化更小。

### 局限性
- 摘要仅提到在仿真中评估分布内、视角/空间偏移和分布外条件，并进行了真实机器人实验，但未提供真实机器人实验的具体规模、任务数量或统计细节；
- 摘要未提供演示采集数量、训练时长、硬件配置、评估指标定义等实验细节；
- 摘要未说明该方法在更广泛农业任务、不同作物或更复杂自然环境中的泛化能力；
- 摘要未提供失败案例分析或方法在真实农业场景中部署的限制；
- 摘要未提供足够信息说明仿真环境与真实环境之间的差距及其对结果的具体影响；
- 其他未在摘要中提及的实验细节、消融设置和定量结果：摘要未提供足够信息。

### 阅读优先级
中。理由：该论文聚焦于 VLA/通用机器人策略在农业操作中的仿真到真实适配，问题明确且与农业机器人操作相关；摘要给出了框架、策略比较和主要结果，但未提供详细实验数据与真实部署规模。对于关注机器人学习、VLA 策略适配和农业操作的研究者具有参考价值；若需要具体实验细节或复现信息，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation in agricultural environments remains challenging due to variations in plant geometry, occlusion, and camera viewpoints. Pretrained vision-language-action (VLA) and generalist robot policies offer a promising approach to addressing these challenges by learning manipulation behaviors from multimodal observations and language instructions. However, adapting these policies to agricultural tasks requires domain-specific demonstrations, which are costly and time-consuming to collect on physical robots. In this work, we develop a simulation-to-real robot-learning framework for agricultural reaching and grasping that integrates task-specific demonstration collection and pretrained policy adaptation. A MuJoCo-based agricultural environment is developed with diverse tomato plant structures to support demonstration collection and controlled evaluation. Expert demonstrations are collected through joystick teleoperation, with a low-level controller used to execute robot actions. Two pretrained generalist robot policies, Octo and $π_{0.5}$, are adapted using simulated demonstrations, followed by further fine-tuning on a physical Franka Research 3 manipulator using real-robot demonstrations. The adapted policies are evaluated under in-distribution, viewpoint/spatial-shift, and out-of-distribution conditions in simulation, followed by physical-robot experiments. The influence of proprioceptive information on policy performance is also investigated. Results show that $π_{0.5}$ achieves higher task-performance scores than Octo and exhibits less degradation under distribution shifts. These findings demonstrate the potential of integrating pretrained generalist policies with task-specific demonstration learning for agricultural manipulation.

</details>

#### 2026-10-19 - ForagerSim: Evaluating Embodied Map-Based Reasoning in Large-Scale Dynamic Worlds

**Authors:** Tomáš Musil, Martin Kotík, Michal Vavrečka, Karla Štěpánová, Sebastian Scherer, Martin Saska
**Links:** [abs](https://arxiv.org/abs/2610.26395) - [pdf](https://arxiv.org/pdf/2610.26395)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ForagerSim: Evaluating Embodied Map-Based Reasoning in Large-Scale Dynamic Worlds
- 作者：Tomáš Musil, Martin Kotík, Michal Vavrečka, Karla Štěpánová, Sebastian Scherer, Martin Saska
- 出版日期：2026-10-19T13:40:47Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.26395

### 一句话总结
论文提出 ForagerSim，一个用于评估具身智能体在大规模动态世界中进行“基于地图的推理”的跨学科仿真平台，并通过对比强化学习基线、工程化机器人栈和人类玩家，指出复杂场景中地图式推理可能是性能瓶颈。

### 研究问题
当前具身 AI 系统要么依赖手工设计的建图流程（在未建模动态下易失效且局限于度量空间），要么依赖很少形成地图式表示的学习策略；同时，缺少真正要求“基于地图推理”的具身 AI 基准，导致难以发展能像动物一样灵活构建和使用地图式表示的架构。论文试图提供这样的评估环境。

### 核心思路/方法
ForagerSim 是一个高度模块化的研究平台与仿真环境，聚焦需要地图式推理的具身任务，场景覆盖移动机器人搜救、复杂迷宫与广阔甚至可能无限的开放区域中的动物觅食等。平台允许独立调节多个难度轴：感知（从抽象 2D 感知到完整 RGB 或 LiDAR）、尺度（房间级到多公里级）、拓扑（开放场地到复杂迷宫）、动态（烟雾、碎片、感知运动故障等）以及任务（从简单 2D 覆盖到受觅食启发的井交替任务）。论文在 8 个示例世界上比较了强化学习基线、简单工程化机器人栈和人类玩家，以观察不同难度轴对现有方法的影响。

### 主要贡献
- 提出 ForagerSim：一个面向“基于地图推理”的具身任务仿真平台，具有跨学科定位。
- 提供多维度可独立调节的难度设计，涵盖感知、尺度、拓扑、动态和任务。
- 在 8 个示例世界上对比强化学习基线、工程化机器人栈与人类玩家，分析不同难度轴对方法表现的影响。
- 报告发现：当感知简化为 2D 时，学习策略在简单拓扑中的多目标搜索和井交替任务上表现 surprisingly well，但在更大或拓扑更复杂的环境中低于人类表现，而基于地图的基线表现良好，提示地图式推理是这些场景的瓶颈。

### 局限性
摘要未提供足够信息说明具体实验规模、统计显著性、各难度轴的系统消融细节、工程化机器人栈与人类玩家的具体配置，以及平台在真实机器人上的部署验证情况。摘要也未提供足够信息说明 ForagerSim 的开源许可、计算开销与可复现性细节。

### 阅读优先级
中。理由：该工作与具身 AI、机器人导航和地图式表示学习评估直接相关，且明确指出现有学习策略在复杂拓扑和大尺度场景中的瓶颈，对基准设计有参考价值；但摘要仅给出 8 个示例世界的对比结果，缺少更细的实验与可复现信息，需阅读全文后才能判断其方法深度与结论稳健性。

</details>

<details>
<summary>Abstract</summary>

Animals build cognitive maps of vast environments, use them to perform map-based navigation, and might even be reusing the same circuitry used in spatial reasoning for creating and using maps of arbitrary task-spaces. In contrast, current embodied AI systems either rely on hand-engineered mapping pipelines, which break in the presence of unmodeled dynamics and are restricted to metric space, or on learned policies that rarely form map-like representations at all. Developing architectures that could learn to build and use map-like representations as flexibly as animals is, however, difficult because few embodied AI benchmarks actually require map-based reasoning. To address this, we present ForagerSim --- an interdisciplinary research platform and simulation environment focused on embodied tasks that require map-based reasoning, with scenarios ranging from mobile-robot search and rescue to animal foraging in both complex mazes and vast, potentially infinite open areas. ForagerSim is highly modular and allows modifying independent axes of difficulty related to perception (abstract 2D sensing to full RGB or LiDAR), scale (room-scale to multi-km scale), topology (open-fields to complex mazes), dynamics (smoke, debris, sensorimotor failures and others) and tasks (from simple 2D coverage to foraging-inspired well-alternation tasks). We compare reinforcement learning baselines with a simple engineered robotics stack and a human player on 8 example worlds which show how different difficulty axes affect existing methods. Our results show that, when sensing is simplified to 2D, learned policies can perform multi-object search and well-alternation tasks surprisingly well in simple topologies, but they fall short of human performance in larger or more complex-topology environments where map-based baselines perform well, suggesting that map-based reasoning is the bottleneck in these scenarios.

</details>

#### 2026-10-19 - Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving

**Authors:** Jie Wang, Guang Li, Zhijian Huang, Jinlong Li, Chenxu Dang, Hangjun Ye, Yahong Han, Long Chen
**Links:** [abs](https://arxiv.org/abs/2610.25734) - [pdf](https://arxiv.org/pdf/2610.25734)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving
- 作者：Jie Wang, Guang Li, Zhijian Huang, Jinlong Li, Chenxu Dang, Hangjun Ye, Yahong Han, Long Chen
- 出版日期：2026-10-19T03:37:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25734 ；PDF https://arxiv.org/pdf/2610.25734

### 一句话总结
论文提出“Think Densely, Act Sparsely”的驾驶智能范式及 LECDrive 框架，通过在 VLA 模型内嵌入由任务特定潜在 token 承载的渐进式“潜在专家认知链”，让模型在保持高效推理的同时内化稠密视觉、语义与几何知识。

### 研究问题
现有 Vision-Language-Action（VLA）自动驾驶模型通常以稀疏监督（如语言指令或轨迹信号）训练，而自动驾驶本质上需要稠密理解视觉、语义和几何信息。摘要指出，从稠密视觉观察到稀疏表示的直接映射会迫使模型压缩甚至丢弃对安全驾驶至关重要的场景信息。作者认为该限制并非源于模型容量不足，而是缺乏显式机制来鼓励在潜在空间中形成稠密世界表示。

### 核心思路/方法
论文提出“Think Densely, Act Sparsely”范式，并实例化为 LECDrive 框架。其核心是模仿人类分层感知过程，在 VLA 模型中嵌入一条渐进式的潜在专家认知链。具体而言，方法注入一小组任务特定的潜在 token 作为载体，使模型能够从基础视觉模型内化稠密知识，包括视觉表示（DINOv3）、语义结构（SAM3）和空间几何（DepthAnything3），同时保持高效推理。该相互依赖的认知链遵循课程学习原则，监督信号从表示到语义再到几何逐步结构化。

### 主要贡献
- 提出“Think Densely, Act Sparsely”的驾驶智能范式，主张通过显式机制在潜在空间中构建稠密世界表示，而非仅依赖稀疏监督的直接映射。
- 提出 LECDrive 框架，将渐进式潜在专家认知链嵌入 VLA 模型，并以任务特定潜在 token 作为载体，内化来自 DINOv3、SAM3、DepthAnything3 的视觉、语义和几何知识。
- 设计遵循课程学习原则的监督结构，使认知链从表示到语义再到几何逐步组织，并强调保持高效推理。
- 摘要称大量实验表明 LECDrive 在多个自动驾驶基准上持续提升基础 VLM 的性能，覆盖物体感知、状态预测和轨迹规划等关键任务。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集规模、基线细节和定量结果。
- 摘要未提供足够信息说明潜在 token 的数量选择、课程学习各阶段的具体监督形式及训练成本。
- 摘要未提供足够信息说明“高效推理”的具体效率指标或与其它方法的计算开销对比。
- 摘要未提供足够信息说明方法在不同基础 VLM 或不同驾驶场景下的泛化边界与失败案例。

### 阅读优先级
中。理由：该论文针对 VLA 自动驾驶中“稠密感知与稀疏监督”的矛盾提出明确范式，方法思路清晰，且涉及视觉、语义、几何三类基础模型知识的潜在空间整合，与具身智能/机器人视觉语言动作方向相关。但当前仅依据摘要，缺少实验细节与定量证据，是否值得深入精读需结合全文的实验充分性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Autonomous driving fundamentally demands dense understanding of visual, semantic, and geometric information, yet existing Vision-Language-Action (VLA) models are typically trained with sparse supervision such as language instructions or trajectory signals. This direct mapping from dense visual observations to sparse representations forces the model to compress or even discard critical scene information essential for safe driving. We argue that this limitation does not stem from insufficient model capacity, but from the lack of explicit mechanisms that encourage the formation of dense world representations in the latent space. In this spirit, we propose a novel paradigm for driving intelligence, Think Densely, Act Sparsely, and instantiate it with an efficient and interpretable framework, LECDrive (Latent Expert Cognitive Chains for Vision-Language-Action autonomous Driving). The core idea is to mimic the hierarchical perception process of humans by embedding a progressive chain of latent expert cognition within the VLA model. Concretely, we inject a compact set of task-specific latent tokens as carriers, enabling the model to internalize dense knowledge from foundational vision models, including visual representations (DINOv3), semantic structures (SAM3), and spatial geometry (DepthAnything3), while maintaining efficient inference. This interdependent cognitive chain follows a curriculum learning principle, where supervision is progressively structured from representation to semantics and geometry. Extensive experiments demonstrate that LECDrive consistently improves the performance of base VLMs across multiple autonomous driving benchmarks, covering key tasks such as object perception, state prediction, and trajectory planning. These findings suggest that constructing dense world models through structured latent expert chains is a promising direction for VLA-based autonomous driving.

</details>

#### 2026-10-18 - Preserving the Manifold: Frozen Expert Alignment for Label-Efficient SAR Scene Understanding

**Authors:** Eli A. Underwood, I. Taylor McKechnie, Leslie M. Collins
**Links:** [abs](https://arxiv.org/abs/2610.25429) - [pdf](https://arxiv.org/pdf/2610.25429)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Preserving the Manifold: Frozen Expert Alignment for Label-Efficient SAR Scene Understanding
- 作者：Eli A. Underwood, I. Taylor McKechnie, Leslie M. Collins
- 出版日期：2026-10-18T17:43:57Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次级分类
- 链接：[摘要](https://arxiv.org/abs/2610.25429)｜[PDF](https://arxiv.org/pdf/2610.25429)

### 一句话总结
该论文提出一种“冻结专家”框架：保持 SAR 编码器与 CLIP 文本编码器均冻结，只学习一个轻量、受约束且保持结构的残差桥接模块，以缓解 SAR—文本跨模态对齐中的模态失配与“物理遗忘”，并在标签高效设定下提升零样本 SAR 场景分类表现。

### 研究问题
论文指出 SAR 图像与自然语言跨模态对齐面临两类失败：
1. **模态失配**：在光学图像上预训练的文本编码器（如 CLIP）难以高效迁移到 SAR；主动微波后向散射与被动光学反射在物理上不兼容，且现有 SAR 描述数据集规模比所需小几个数量级，难以在不显著破坏已学语义流形的情况下弥合差距。
2. **物理遗忘**：在大规模自监督目标上预训练的 SAR 编码器编码了雷达物理特性，但在有限描述数据上为文本对齐而微调编码器时，这些特性会被逐步抹除。

### 核心思路/方法
- **单一设计原则**：保持两个编码器冻结，仅学习一个受约束、保持结构的桥接模块。
- **Frozen Expert 框架**：将冻结的 CROMA SAR 编码器与冻结的 CLIP 文本编码器通过轻量级“受约束残差桥”对齐。
- **物理遗忘的形式化**：通过 Procrustes disparity 定义物理遗忘，并报告其桥接方法比微调更好地保持 SAR 几何（disparity：0.210 对 0.351）。
- **泛化验证**：摘要称在多种 SAR 骨干与文本编码器上验证了通用性。

### 主要贡献
- 提出冻结双专家、仅学习受约束残差桥的 SAR—文本对齐框架。
- 用 Procrustes disparity 形式化“物理遗忘”，并给出桥接优于微调的几何保持证据。
- 在零样本 SAR 场景分类上，以最多少 8 倍训练数据超过微调基线：
  - DFC2020：+10.3% R@1，+15.5% mAP
  - EuroSAT-SAR：+15.7% R@1，+12.2% mAP
  - BigEarthNet-MM：+14.7% R@1
- 将“冻结流形对齐”定位为高差异跨模态设定下相对微调的原则性、数据高效替代方案。

### 局限性
- 摘要未提供足够信息说明桥接模块的具体结构、参数量与训练细节。
- 摘要未提供足够信息说明各数据集的划分、训练数据规模绝对值、基线配置与统计显著性。
- 摘要未提供足够信息说明方法在非分类任务（如检索、描述生成、分割）上的表现。
- 摘要未提供足够信息说明失败案例、计算开销或对 SAR 成像条件变化的鲁棒性。
- 摘要未提供足够信息说明“物理遗忘”Procrustes disparity 的完整定义与计算协议。

### 阅读优先级
**中**。理由：论文聚焦 SAR—文本跨模态对齐中的模态失配与物理遗忘，提出冻结双编码器加轻量桥接的数据高效方案，并给出零样本分类的量化提升，问题定义清晰、方法原则简洁；但摘要未展开桥接结构、训练细节与更广泛任务验证，是否适合精读取决于读者对 SAR 跨模态对齐、冻结骨干适配或标签高效场景理解的兴趣。

</details>

<details>
<summary>Abstract</summary>

Cross-modal alignment of synthetic aperture radar (SAR) imagery to natural language is constrained by two distinct failures. The first is modality mismatch: text encoders pre-trained on optical imagery, such as CLIP, cannot be efficiently fine-tuned on SAR, because active microwave backscatter is physically incompatible with passive optical reflectance and the available SAR caption datasets are orders of magnitude too small to bridge this gap without substantially degrading the learned semantic manifold. The second is physical forgetting: SAR encoders pre-trained on large-scale self-supervised objectives encode radar physics that are progressively erased when the encoder is fine-tuned for text alignment on limited caption data. A single design principle addresses both failures: keep both encoders frozen and learn only a constrained, structure-preserving bridge. Our Frozen Expert framework aligns a frozen CROMA SAR encoder with a frozen CLIP text encoder via a lightweight constrained residual bridge. We formally define physical forgetting via Procrustes disparity and show our bridge preserves SAR geometry significantly better than fine-tuning (disparity: 0.210 vs. 0.351). We validate generality across multiple SAR backbones and text encoders. On zero-shot SAR scene classification, our approach outperforms fine-tuned baselines using up to 8x less training data: DFC2020 (+10.3% R@1, +15.5% mAP), EuroSAT-SAR (+15.7% R@1, +12.2% mAP), BigEarthNet-MM (+14.7% R@1). These results establish frozen manifold alignment as a principled, data-efficient alternative to fine-tuning in high-disparity cross-modal settings.

</details>

#### 2026-10-18 - Learning Lane-Structured Conditioning Fields for Online HD Mapping

**Authors:** Andrea Bertogalli, Anthony Dell'Eva, Marcello Ceresini, Federico Pirazzoli, Lorenzo Cipelli, Filippo D'Addeo, Nicola Marinello, Massimo Bertozzi
**Links:** [abs](https://arxiv.org/abs/2610.25284) - [pdf](https://arxiv.org/pdf/2610.25284)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Lane-Structured Conditioning Fields for Online HD Mapping
- 作者：Andrea Bertogalli, Anthony Dell'Eva, Marcello Ceresini, Federico Pirazzoli, Lorenzo Cipelli, Filippo D'Addeo, Nicola Marinello, Massimo Bertozzi
- 出版日期：2026-10-18T14:04:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.25284) / [PDF](https://arxiv.org/pdf/2610.25284)

### 一句话总结
论文提出一种与 BEV 对齐的密集“Lane Field”表示来编码局部车道结构，并基于该表示构建即插即用框架，通过 BEV 特征调制和可变形注意力引导来提升在线高清地图构建。

### 研究问题
在线高清地图构建中，现有方法常依赖外部先验来提升精度与鲁棒性，但先验表示存在权衡：密集栅格易集成却忽略某些地图几何属性；稀疏向量保留几何结构却需要专用编码器、难以接入现有架构。此外，外部先验可能不准确、获取成本高或难以维护。论文希望找到一种既能提供几何引导、又可学习且广泛适用的结构表示。

### 核心思路/方法
论文提出 Lane Field：一种密集的、与 BEV 对齐的几何表示，在每个空间位置编码局部车道结构，并可由车载观测预测，或由外部地图先验构建。在此基础上，作者设计了一个即插即用框架，通过两种互补机制增强在线高清地图构建：
1. BEV 特征调制：将车道结构线索注入潜在 BEV 特征；
2. 可变形注意力引导：将查询采样引导至底层车道几何。

论文主要在 OpenLane-V2 上评估，摘要称该方法能持续改进现有方法，并在车道段感知上达到 state-of-the-art。

### 主要贡献
- 提出 Lane Field，一种密集 BEV 对齐的局部车道结构表示，可由观测预测或由外部地图先验构建。
- 提出基于 Lane Field 的即插即用框架，通过 BEV 特征调制和可变形注意力引导增强在线高清地图构建。
- 在 OpenLane-V2 上评估，摘要报告其方法持续改进现有方法，并在车道段感知上取得 state-of-the-art 性能。

### 局限性
摘要未提供足够信息说明计算开销、实时性、不同数据集上的泛化能力、对不准确外部先验的鲁棒性，以及失败案例或消融实验细节。摘要也未提供足够信息说明该框架在非车道类地图元素上的适用性。

### 阅读优先级
中。理由：该论文关注在线高清地图构建中的先验表示与即插即用增强，问题定义清晰，且摘要声称在 OpenLane-V2 上取得 state-of-the-art；但摘要未提供足够实验细节与局限性信息。是否优先阅读取决于读者对 BEV 表示、车道段感知或可变形注意力引导的兴趣。

</details>

<details>
<summary>Abstract</summary>

High-definition maps provide critical structural information for downstream autonomous driving tasks. Recent methods increasingly rely on external priors to improve prediction accuracy and robustness. Yet, existing prior representations expose a trade-off: dense rasters are easy to integrate but ignore certain map geometric properties, while sparse vectors preserve geometric structure but require dedicated encoders and are difficult to plug into existing architectures. Moreover, external priors can be inaccurate, costly to acquire, or difficult to maintain, motivating a structural representation that can provide geometric guidance while remaining learnable and broadly applicable. We address this limitation with the Lane Field, a dense BEV-aligned geometric representation that encodes local lane structure at each spatial location and can be either predicted from onboard observations or constructed from external map priors. Building on this representation, we introduce a plug-and-play framework that enhances online HD mapping through two complementary mechanisms: BEV feature modulation, which injects lane-structured cues into latent BEV features, and deformable attention guidance, which steers query sampling toward the underlying lane geometry. We primarily evaluate our method on OpenLane-V2, showing that conditioning BEV features and guiding deformable attention with local lane geometry enables our framework to consistently improve existing methods and achieve state-of-the-art performance on lane segment perception. Project page: https://andberto.github.io/LaneField/

</details>

#### 2026-10-15 - GeoState: Learning View-Decoupled Geometry States for 3D World Modeling

**Authors:** Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
**Links:** [abs](https://arxiv.org/abs/2610.22343) - [pdf](https://arxiv.org/pdf/2610.22343)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoState: Learning View-Decoupled Geometry States for 3D World Modeling
- 作者：Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
- 出版日期：2026-10-15T17:56:18Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.22343 ；PDF：https://arxiv.org/pdf/2610.22343 ；项目页：https://hongchang-liu.github.io/GeoState-project-page/

### 一句话总结
GeoState 提出一种视角解耦的几何表示，将场景状态演化与相机相关观测分离，以提升预测式 3D 世界建模的稳定性与跨视角查询一致性。

### 研究问题
现有 3D 世界模型常将几何基础模型（GFM）的特征作为预测用的世界状态，但这些特征具有视角依赖性，会把场景动态与相机引起的变化纠缠在一起，使状态演化更难预测。论文试图解决由此带来的视角依赖与预测困难问题。

### 核心思路/方法
GeoState 将场景状态演化与相机相关观测分离。具体而言，一个场景 tokenizer 将多视角 GFM 特征聚合为视角解耦的场景状态；一个几何解码器使用相机射线对该状态进行查询；随后，一个自回归世界模型预测未来场景状态，而相机运动被单独建模。预测出的状态可以在预测相机或外部指定相机下解码，并在整个 rollout 中保持来自单一上下文的尺度，无需逐帧尺度对齐。

### 主要贡献
- 提出 GeoState，一种用于预测式 3D 世界建模的视角解耦几何表示，将场景状态演化与相机相关观测分离。
- 设计场景 tokenizer 聚合多视角 GFM 特征为视角解耦场景状态，并用相机射线通过几何解码器查询。
- 采用自回归世界模型预测未来场景状态，同时单独建模相机运动。
- 支持在预测或外部指定相机下解码预测状态，并在 rollout 中保持单一上下文尺度，无需逐帧尺度对齐。
- 实验表明 GeoState 在 Waymo 上优于先前 3D 世界模型，支持几何一致的跨视角查询，并零样本泛化到 KITTI 和 nuScenes。

### 局限性
摘要未提供足够信息。摘要未提供关于失败案例、计算开销、具体限制条件或方法适用范围之外不足的详细信息。

### 阅读优先级
高。理由：该论文针对 3D 世界模型中视角依赖导致状态预测困难的关键问题，提出明确的解耦建模思路，并在 Waymo 上报告优于先前方法、支持跨视角查询且零样本泛化到 KITTI 和 nuScenes；若关注 3D 世界模型、具身智能或自动驾驶场景建模，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent 3D world models increasingly use features from geometry foundation models (GFMs) as predictive world states, benefiting from their rich geometric priors. However, the view dependence of these features entangles scene dynamics with camera-induced variation, making the resulting state evolution harder to predict. We propose GeoState, a view-decoupled geometry representation for predictive 3D world modeling that separates scene-state evolution from camera-dependent observation. Specifically, a scene tokenizer aggregates multi-view GFM features into a view-decoupled scene state, which a geometry decoder queries using camera rays. An autoregressive world model then predicts future scene states, while camera motion is modeled separately. The predicted states can therefore be decoded under either predicted or externally specified cameras, while retaining a single context-derived scale throughout the rollout without per-frame scale alignment. Experiments show that GeoState outperforms prior 3D world models on Waymo, supports geometrically consistent cross-view querying, and generalizes zero-shot to KITTI and nuScenes. Project page: https://hongchang-liu.github.io/GeoState-project-page/

</details>

#### 2026-10-15 - Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

**Authors:** Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye, Chenze Yu, Wenxuan Zhu, Eric J. Chen, Yan Qin, Yue Chen, Tongyu Wu, Junhao Gong, Kai-Chong Lei, Jiahao Zhang, Kailun Su, Qiwei Liang, Renjing Xu, Ping Luo, Wenbo Ding
**Links:** [abs](https://arxiv.org/abs/2610.22342) - [pdf](https://arxiv.org/pdf/2610.22342)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation
- 作者：Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye, Chenze Yu, Wenxuan Zhu, Eric J. Chen, Yan Qin, Yue Chen, Tongyu Wu, Junhao Gong, Kai-Chong Lei, Jiahao Zhang, Kailun Su, Qiwei Liang, Renjing Xu, Ping Luo, Wenbo Ding
- 出版日期：2026-10-15T17:56:17Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接 https://arxiv.org/abs/2610.22342 ；PDF 链接 https://arxiv.org/pdf/2610.22342 ；项目网站 https://xsparkai.com/Spark-0

### 一句话总结
Spark-0 提出一种空间对齐的视觉-触觉-语言-动作（VTLA）模型，将触觉既作为预训练监督信号又作为策略输入，用于提升机器人在接触密集的灵巧操作任务中的表现。

### 研究问题
通用机器人策略从大规模视觉预训练中获益，但在接触密集的灵巧操作中往往表现不佳，因为力、柔顺性和早期滑动难以仅从图像中观测。论文关注的核心问题是：如何利用触觉信息，既改善视觉运动预训练，又作为部署时的策略条件，从而提升灵巧操作能力。

### 核心思路/方法
Spark-0 以两种互补方式使用触觉：
1. **预训练阶段**：由触觉手套导出的图像空间接触图（image-space contact maps）与冻结的 3D 几何教师（frozen 3D geometry teacher）特征共同监督视觉 token；这些监督目标在推理阶段被移除。
2. **并行触觉通路**：编码区域力历史（regional force histories）与 3D taxel 状态，用于条件化动作专家（action expert）。
因此，单个检查点（single checkpoint）可同时支持纯视觉部署和触觉条件化部署。

为扩展这种监督，论文构建了 **HumanTouch**：一个 1,000 小时的全手触觉人类操作数据集，并将 Spark-0 与自我中心视频、机器人数据、仿真数据一起预训练。论文还发布了 **SparkArena**，在同一灵巧本体（one dexterous embodiment）上配对纯视觉仿真任务与触觉条件化真实机器人任务。

### 主要贡献
- 提出 Spark-0，一种空间对齐的 VTLA 模型，将触觉同时用作可扩展的预训练监督信号和部署时的策略输入。
- 构建 HumanTouch，1,000 小时全手触觉人类操作数据集，用于规模化触觉预训练。
- 发布 SparkArena，在同一灵巧本体上配对纯视觉仿真任务与触觉条件化真实机器人任务。
- 实验结果表明：Spark-0 在 SparkArena 两个赛道上均取得最高平均成功率，并在 Ego Humanoid Manipulation Benchmark 的全部八项聚合指标上排名第一。
- 关键对比：在相同数据与计算量下，相比丢弃触觉的纯视觉预训练，保留 1,000 小时 HumanTouch 触觉使 Ego Humanoid 上的纯视觉成功率从 52.5% 提升至 71.7%，使 SparkArena-Real（部署时也使用触觉）成功率从 44.0% 提升至 52.0%，说明触觉不仅是策略输入，也是灵巧视觉运动预训练的可扩展监督。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败案例、计算成本细节、触觉硬件泛化性、仿真到真实迁移的具体限制，也未提供与更多基线方法的全面对比或消融实验细节。

### 阅读优先级
**高**。理由：该工作同时涉及触觉预训练规模化、VTLA 模型、大规模数据集（1,000 小时 HumanTouch）与基准（SparkArena），并给出触觉监督显著提升视觉运动预训练效果的定量证据，对灵巧操作、多模态机器人策略和触觉学习方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, image-space contact maps derived from tactile gloves, together with features from a frozen 3D geometry teacher, supervise the visual tokens; these objectives are removed at inference. In parallel, a tactile pathway encodes regional force histories and 3D taxel states to condition the action expert. A single checkpoint therefore supports both vision-only and tactile-conditioned deployment. To scale this supervision, we build HumanTouch, a 1,000-hour dataset of full-hand tactile human manipulation, and pretrain Spark-0 on it together with egocentric video, robot data, and simulation. We also release SparkArena, which pairs vision-only simulated tasks with tactile-conditioned real-robot tasks on one dexterous embodiment. Spark-0 achieves the highest mean success rate on both SparkArena tracks and ranks first on all eight aggregate metrics of the Ego Humanoid Manipulation Benchmark. Compared with vision-only pretraining on the same data and compute with touch discarded, retaining the touch of 1,000 hours of HumanTouch raises vision-only success on Ego Humanoid from 52.5% to 71.7%, and success on SparkArena-Real, where touch is also used at deployment, from 44.0% to 52.0%, indicating that touch serves not only as a policy input but also as scalable supervision for dexterous visuomotor pretraining. The Website is available at: https://xsparkai.com/Spark-0.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
