# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：44
- 分类分布：
  - Neural Scene Representations & Rendering: 18
  - 3D Reconstruction & Multi-view Geometry: 10
  - Dynamic / 4D Reconstruction: 8
  - Embodied / Robotics / AR Applications: 6
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**趋势一：从“静态重建”全面迈向“动态/4D 场景理解”**
今日论文最显著的趋势是研究重心从静态三维重建转向动态场景（时间维度）的重建与理解。该方向集中了 8 篇论文，且研究维度从早期的“如何重建出动态几何”延伸至“如何压缩流式传输”“如何用物理约束动态重建”“如何用统一框架耦合动态重建与感知”等更高层次。典型代表包括：`Depth Anything V4`（将黎曼流匹配用于 4D 高斯溅射参数）、`Stream4D`（为流式自回归视频模型引入 4D 一致性奖励）、`DyG²T`（以粒子图 Transformer 建模物体动力学）、`QuARC-GS` 与 `S²GS`（动态场景的紧凑流式传输）、`USR-Drive`（统一动态几何重建与实例级检测）、`Gallileo-4D`（零训练动态 4D 重建集成方案）、`RVLoss`（自监督动态场景流估计的刚性约束损失设计）。

**趋势二：3D 高斯溅射（3DGS）成为核心表示，但正在与“几何学派”加速碰撞融合**
3DGS 已从最初的渲染工具演变为一个开放的研究平台，今日论文几乎覆盖了 3DGS 的各个生命周期阶段：初始化（`CoMVS-GS`）、参数空间建模（`Depth Anything V4`）、压缩编码（`QuARC-GS`）、流式传输（`S²GS`）、作为机器人策略的观测适配模块（`GS-VLA`）。更值得注意的是，本轮论文显示 3DGS 正在与经典几何方法深度融合：`CoMVS-GS` 将 MVS（多视角立体几何）与 3DGS 相互监督，`USR-Drive` 将 3D 框（几何/语义感知）与 3DGS（渲染）联合去噪。这表明“渲染最优”与“几何精确”之间的鸿沟正被主动弥合。

**趋势三：单目/稀疏输入条件下的重建与生成成为共同挑战**
多条技术路线（4D 重建、重拍摄、视频生成等）都在聚焦“如何从极稀疏或单目输入中恢复高保真 4D/3D 结构”。代表性工作包括：`4DAnyone`（从随意单目视频重建 4D 人体）、`Depth Anything V4`（单目视频 -> 动态 4D 场景）、`Point-Based 3D Reconstruction from Sparse Views`（已知光照下稀疏视角重建）、`ReX-Shot`（单张图像重拍摄）。这背后反映的共性问题是：如何在观测严重不足时，用先验（物理先验、生成先验、几何先验）弥补信息缺失。

**趋势四：重建/感知框架与“下游应用”的耦合日益紧密**
论文不再仅仅追求重建精度，而是明确面向机器人、AR/VR、自动驾驶、手术等应用场景进行联合设计。典型代表：`USR-Drive`（面向自动驾驶的“重建+检测”统一生成框架）、`GS-VLA`（面向机器人 VLA 策略的视角鲁棒性适配）、`LT-Mem`（面向长期作业机器人的场景记忆演化）、`Transferable Tool-Tissue Contact Detection`（面向手术机器人的接触检测）、`SceneGTMM`（面向定位导航的地图匹配）。这反映“重建即服务”的思路——重建结果需服务于更高层的决策与交互任务。

**趋势五：蒸馏/冻结骨干 + 推理时策略成为低资源场景下的务实选择**
`Gallileo-4D` 通过冻结骨干网络，在推理时融合三种解码配置，以零训练成本取得挑战赛第三名，并揭示了一个重要现象：当评估集分布与训练集不一致时，微调反而会损伤预训练特征的泛化能力。`GS-VLA` 同样采用“冻结 VLA 策略 + 即插即用模块”的思路，在不重训练策略的条件下恢复视角偏移带来的性能损失。这一趋势对资源受限场景（边缘设备、不具微调条件的部署环境）具有现实价值。


#### 技术路线观察

| 方向 | 代表性论文 | 技术侧重点 |
|------|-----------|-----------|
| **4D重建/动态重建** | Depth Anything V4, Stream4D, Gallileo-4D, DyG²T | 从单目/多视角视频恢复动态几何与运动；倾向于把流匹配、扩散模型、粒子图 Transformer 等生成/概率模型引入 4DGS 参数空间；对“动态”的建模方式多样（参数流匹配、重建奖励、物体动力学图）。 |
| **稀疏视角/单目重建** | 4DAnyone, Point-Based 3D Reconstruction, ReX-Shot | 依赖强先验（多视角一致性生成、物理光照传输、基础模型特征）来弥补观测不足；普遍采用“先合成中间视角/特征，再重建”的管线。 |
| **神经场景表示与渲染（3DGS为主）** | QuARC-GS, S²GS, CoMVS-GS, GS-VLA | 3DGS 的生命周期问题（初始化、压缩、流式传输、物理约束）是核心；在保留 3DGS 高效渲染优势的同时，通过引入几何先验（MVS、八叉树）、量化编码、门控机制来提升几何精度与压缩率。 |
| **几何基础模型/经典几何与学习融合** | Gravity-aware Absolute Pose, CoMVS-GS, Evaluation of Monocular SLAM, Evaluation of Image Matching | 经典几何（特征、位姿求解器、SLAM）仍具竞争力，但正在与深度特征/基础模型结合；本轮出现了“基础模型特征用于位姿求解”“MVS 与 3DGS 相互监督”等融合范式；同时也有对现有基础模型（DROID-SLAM、MASt3R-SLAM）在极端场景（无人机俯视）下的批判性评估。 |
| **机器人/AR/自动驾驶应用** | USR-Drive, GS-VLA, LT-Mem, SceneGTMM, Tool-Tissue Contact | 强调感知/重建与其他模态（语言指令、时间历史、接触力）的耦合；关注点从“重建得准”转向“在任务中好用”，例如视角鲁棒性、跨会话身份一致性、跨区域迁移能力。 |


#### 值得优先阅读的论文

1. **Depth Anything V4（2608.18388）**：该文将黎曼流匹配（RFM）直接应用于 4DGS 参数空间，并通过受控实验严格分离了 RFM 的独立贡献（F-score +0.044）。这对“如何将概率生成模型用于非欧几何参数空间”具有方法论层面的示范意义，值得精读其实验设计。

2. **USR-Drive（2608.19036）**：以统一条件生成框架同时恢复动态几何（3DGS）与实例级布局（3D 框），将两类过去分离的任务置于共享的扩散去噪框架下。这一思路可能重塑自动驾驶场景表示学习的范式，值得关注其模态对齐的具体实现。

3. **QuARC-GS（2608.18285）** & **S²GS（2608.19639）**：两者都面向动态场景的流式传输，但技术路线截然不同（量化锚定残差编码 vs 结构化稀疏高斯流）。对比阅读有助于理解“动态 4D 表示压缩”这一前沿问题的不同解法，且对边缘部署有直接参考价值。

4. **4DAnyone（2608.20335）**：系统性地诊断并形式化了视频扩散模型在多视角生成中的“有界注意力上下文”问题，拆解为参考上下文与目标上下文两个耦合瓶颈，并分别设计了解决方案。其对问题本质的分析值得借鉴。

5. **CoMVS-GS（2608.18413）**：展示了“经典几何（MVS、PatchMatch）”与“现代表示（3DGS）”如何通过相互监督实现互惠。对于关注 3DGS 几何质量提升问题的读者，这篇文章提供了一个新颖且务实的融合范式。


#### 可能的研究机会

- **4D 重建的“保真-紧凑”联合优化

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-24T09:11:26-04:00
**Total number of papers:** 41
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

### 2026-08

#### 2026-08-19 - Evaluation of Monocular SLAM Systems on High-Altitude Nadir UAV Footage

**Authors:** Gašper Spagnolo, Matej Dobrevski, Danijel Skočaj
**Links:** [abs](https://arxiv.org/abs/2608.18632) - [pdf](https://arxiv.org/pdf/2608.18632)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** MASt3R, SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evaluation of Monocular SLAM Systems on High-Altitude Nadir UAV Footage
- 作者：Gašper Spagnolo, Matej Dobrevski, Danijel Skočaj
- 出版日期：2026-08-19
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.18632

### 一句话总结
该论文在无惯导/GNSS辅助条件下，对五种单目SLAM系统在无人机俯视视频上的性能进行了基准评测，发现现有方法在垂直定位和大范围轨迹保持上仍不足，难以仅凭视觉实现可靠空中导航。

### 研究问题
单目SLAM系统在无人机高空俯视（nadir）视频这一弱几何约束、强感知混淆场景下的视觉定位精度与轨迹一致性表现如何？是否足以支持纯视觉空中导航？

### 核心思路/方法
- 选取五种单目SLAM系统，在三种数据集上评测：本地无人机飞行、合成城市尺度图像、长距离空中序列。
- 为隔离视觉性能，不提供惯性测量单元（IMU）或全球导航卫星系统（GNSS）辅助。
- 通过均值水平绝对误差（MAE）占参考路径长度比例等指标，比较各系统在不同环境和轨迹尺度下的表现。

### 主要贡献
- 提供了单目SLAM在无人机高空俯视视频场景下的系统性基准测试。
- 发现MASt3R-SLAM在五条DJI飞行序列上取得最低水平MAE（0.53%参考路径长度）。
- 整体而言，DROID-SLAM平均表现最佳（完成运行的平均误差为2.88%参考路径长度）。
- 指出当前单目SLAM在长距离空中序列上无法保持全局轨迹形状，且垂直定位精度普遍较差。

### 局限性
- 摘要明确指出，所有系统在长距离序列上轨迹扭曲严重，垂直方向定位不佳，即便有回环能力也无法修复。
- 结论认为现有单目SLAM方法本身不足以实现可靠的纯视觉空中导航。
- 摘要未提供足够信息：各系统具体运行环境、计算资源需求、失败案例细节、数据集构建方式等均未提及。

### 阅读优先级
**中**。理由：该论文属于系统评测类工作，对本领域（单目SLAM、无人机视觉导航）有参考价值，但结论偏向否定性（现有方法不足），且摘要未提供具体实验细节（如序列数量、处理时长、失败率等）。若关注SLAM在航空场景的适用性，可阅读；若追求方法创新或详细对比，则需进一步查阅全文。

</details>

<details>
<summary>Abstract</summary>

Aerial nadir video combines weak geometric constraints with severe perceptual aliasing, making it a difficult regime for monocular SLAM. We benchmark five monocular SLAM systems on local UAV flights, synthetic city-scale imagery, and long-range aerial sequences. To isolate visual performance, we provide no inertial or GNSS aiding. Performance varies strongly with environment and trajectory scale: MASt3R-SLAM achieves the lowest mean horizontal MAE on the five DJI flights (0.53\% of reference path length), whereas no system consistently preserves global trajectory shape on the long GES and ALTO sequences. Overall, DROID-SLAM performs best, averaging 2.88\% of reference path length across completed runs. Vertical position remains poor, and large-area trajectories remain highly distorted despite loop-closure capability. Current monocular SLAM methods are by themselves therefore insufficient for reliable visual-only aerial navigation.

</details>

#### 2026-08-19 - Evaluation of Image Matching Methods for Visual Odometry on UAVs

**Authors:** Gašper Spagnolo, Luka Čehovin Zajc, Matej Dobrevski
**Links:** [abs](https://arxiv.org/abs/2608.18624) - [pdf](https://arxiv.org/pdf/2608.18624)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** image matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evaluation of Image Matching Methods for Visual Odometry on UAVs（无人机视觉里程计图像匹配方法评估）
- 作者：Gašper Spagnolo, Luka Čehovin Zajc, Matej Dobrevski
- 出版日期：2026-08-19T07:17:48Z
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：https://arxiv.org/abs/2608.18624

### 一句话总结
本文在自制合成数据集上，以向下相机配置的无人机位置跟踪为场景，评估了多种最新深度学习方法与传统SIFT特征在视觉里程计图像匹配任务中的表现，发现RoMa匹配器效果最佳，但SIFT特征仍能胜过部分最新方法。

### 研究问题
当GNSS信号不可用或受干扰时，无人机导航如何可靠地利用视觉里程计（VO）进行位置跟踪？具体而言，最近提出的多种基于深度学习的图像匹配方法在面向无人机的VO任务中表现如何，是否优于传统特征方法？

### 核心思路/方法
- 将视觉里程计（VO）作为GNSS失效时的关键导航组件进行探索。
- 构建无人机向下相机配置场景，使用合成数据集作为评估基准。
- 选取近期多种state-of-the-art的（主要基于深度学习的）图像匹配方法，在VO位置跟踪任务中进行系统性对比评估。
- 同时纳入传统SIFT特征方法作为基线，与深度学习方法进行性能比较。

### 主要贡献
- 在无人机专用场景（向下相机、合成数据）下，首次系统评估了多种最新图像匹配方法在VO任务中的适用性。
- 发现RoMa匹配器在当前测试中取得最佳结果，验证了其在该任务中的领先优势。
- 揭示了传统SIFT特征方法仍具有竞争力，能够超越部分最新的深度学习方法，为VO方案选型提供了实用参考。

### 局限性
摘要未提供足够信息。摘要中未提及数据集规模、具体评估指标、实验细节、与真实世界数据的差异、计算开销对比、鲁棒性分析等局限信息。

### 阅读优先级
**中**。理由：该论文聚焦于特定应用场景（无人机VO）的方法基准对比，对从事视觉里程计或无人机导航的研究者有参考价值，但本质上是评估性工作，创新性主要体现在实验设计与结论，而非方法提出。若读者关注最新的图像匹配方法（如RoMa）在具体任务中的实用性，则优先级可提升至中高；若仅关注VO算法设计，优先级为中低。

</details>

<details>
<summary>Abstract</summary>

Unmanned aerial vehicles (UAVs) are becoming a powerful tool for many environmental monitoring and transport applications. Yet, their reliance on Global Navigation Satellite System (GNSS) technology for navigation makes them susceptible to catastrophic failures in scenarios where the positioning signal is unavailable or disrupted. This work explores Visual Odometry (VO) as a crucial navigation component. Recently, numerous deep-learning-based methods for image matching have been proposed that are yet to be implemented in a fully-fledged VO system. In this paper, we evaluate recent state-of-the-art image matching methods for the task of VO for UAV position tracking, with a downwards-facing camera, on our synthetic dataset, and find that while the best results are generated by the recent RoMa matcher, SIFT features can outperform some recent state-of-the-art.

</details>

## Dynamic / 4D Reconstruction

### 2026-08

#### 2026-08-20 - Gallileo-4D: Frozen Backbone Ensemble for Dynamic 4D Reconstruction

**Authors:** Nicolò Savioli
**Links:** [abs](https://arxiv.org/abs/2608.19743) - [pdf](https://arxiv.org/pdf/2608.19743)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, dynamic 4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gallileo-4D: Frozen Backbone Ensemble for Dynamic 4D Reconstruction
- 作者：Nicolò Savioli
- 出版日期：2026-08-20
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2608.19743

### 一句话总结
本文提出了一种零训练成本的冻结骨干网络集成方法，在PhysAI动态4D重建挑战赛中取得第三名，通过推理时融合三种解码配置，比冻结基线提升+0.041 APD。

### 研究问题
如何在预训练4D骨干网络微调效果不佳的情况下，通过不更新梯度（零训练）的方式提升动态4D重建性能。研究发现基准测试中仅25%的评估数据与训练数据分布一致，导致微调反而损害预训练特征在剩余75%数据上的表现。

### 核心思路/方法
- 冻结预训练4D骨干网络，不进行任何梯度更新
- 在推理阶段融合三种解码配置：时间步长-3、水平翻转测试时增强、密集步长-1
- 使用凸权重对三种解码结果进行加权融合
- 该集成方法在冻结基线上获得+0.041 APD提升，超过了所有13种微调配置的效果

### 主要贡献
- 提出一种零训练成本的推理时集成策略，在动态4D重建挑战赛中获得第三名（27个队伍中，最终APD为0.58356）
- 揭示了一个反直觉现象：在训练数据分布与评估数据分布不一致的基准下，微调反而会损害模型在大部分评估数据上的性能
- 证明了冻结骨干+推理时集成的有效性，且训练成本为零

### 局限性
摘要未提供足够信息：未提及方法在非该基准场景下的泛化能力、计算资源消耗、推理时间等具体细节；也未说明参与挑战赛的其他候选方法细节。

### 阅读优先级
**中**。理由：该方法思路简洁且实用，揭示了分布不匹配下微调失效的重要现象，对4D重建和迁移学习领域有一定启发意义。但摘要未提供方法细节和消融实验，适用性有限，适合对推理时集成或该挑战赛感兴趣的读者快速浏览。

</details>

<details>
<summary>Abstract</summary>

We describe our entry to the PhysAI Dynamic 4D Reconstruction Challenge, which placed third of 27 teams at 0.58356 APD on the final leaderboard, without a single gradient update. This was not the plan: of thirteen fine-tuning configurations of a pre-trained 4D backbone, twelve degraded the challenge score, and eleven of those twelve improved local validation at the same time. We trace this inversion to the structure of the benchmark: only 25% of the evaluation set belongs to the data variant released for training, so updates that fit the available data damage the pre-trained features the remaining 75% relies on. Our system therefore freezes the backbone and spends its budget at inference time, fusing three decoding configurations -- temporal stride-3, horizontal-flip test-time augmentation, and dense stride-1 -- under a convex weighting. The ensemble recovers +0.041 APD over the frozen baseline, more than any training run achieved, at zero training cost.

</details>

#### 2026-08-20 - S$^2$GS: Structured Sparse Gaussian Streaming for Efficient Free-Viewpoint Video Reconstruction on Edge-IoT Devices

**Authors:** Yiwei Li, Jiannong Cao, Weixun Gao, Rui Cao, Songye Zhu, Yinfeng Cao, Mingjin Zhang
**Links:** [abs](https://arxiv.org/abs/2608.19639) - [pdf](https://arxiv.org/pdf/2608.19639)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction, rendering, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S$^2$GS: Structured Sparse Gaussian Streaming for Efficient Free-Viewpoint Video Reconstruction on Edge-IoT Devices
- 作者：Yiwei Li, Jiannong Cao, Weixun Gao, Rui Cao, Songye Zhu, Yinfeng Cao, Mingjin Zhang
- 出版日期：2026-08-20T05:12:53Z
- 分类：Dynamic / 4D Reconstruction（动态/4D重建）
- 链接：https://arxiv.org/abs/2608.19639

### 一句话总结
本文提出S$^2$GS框架，通过结构感知的时空稀疏性选择性更新高斯残差，在边缘物联网设备上实现高效且低存储的自由视角视频流式重建。

### 研究问题
现有自由视角视频（FVV）流式重建方法在资源受限的边缘物联网设备上面临每帧优化时间长、存储占用大的问题，难以部署。

### 核心思路/方法
- **空间域**：采用流式八叉树（streaming octree）层级组织高斯残差，捕获空间相关性以指导残差更新。
- **时间域**：设计结构化门控机制，包含层级特征传播（HFP）和Gumbel-Sigmoid采样，将层级动态线索转化为可微优化下的稀疏残差更新决策。
- **多级离散方案**：提供对残差更新的细粒度控制，同时保留复杂动态细节。
- 整体框架在消费者GPU、工业边缘IoT设备和物理远程呈现测试平台上验证。

### 主要贡献
- 提出S$^2$GS框架，利用结构感知的时间稀疏性实现高效FVV流式重建，兼顾视觉保真度。
- 设计空间八叉树与时间门控机制相结合的残差更新策略。
- 在RTX 4090上相比QUEEN，每帧优化时间降低59%、存储成本降低85%。
- 在Jetson AGX Orin上实现60+ FPS的最高渲染吞吐量和最低能耗，展示资源受限系统的部署潜力。

### 局限性
摘要未提供足够信息，无法说明该方法的潜在局限性（如特定场景退化、极端动态下的表现、八叉树内存开销等）。

### 阅读优先级
**高**。理由：该工作针对边缘IoT设备上的FVV流式重建这一实际问题，提出了兼顾效率与质量的新颖稀疏化框架，且提供了跨多种硬件平台的量化对比结果（如59%时间降低、85%存储降低、60+ FPS），对动态重建与边缘计算交叉领域的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Streaming reconstruction of Free-Viewpoint Videos (FVVs) supports immersive Internet of Things (IoT) services, such as telepresence and digital twin visualization. Existing methods suffer from high per-frame optimization time and large storage footprints, limiting deployment on resource-constrained Edge-IoT devices. To address these challenges, we propose Structured Sparse Gaussian Streaming (S$^2$GS), an FVV reconstruction framework that exploits structure-aware temporal sparsity to selectively update Gaussian residuals, enabling efficient streaming without compromising visual fidelity. In the spatial domain, a streaming octree hierarchically organizes Gaussian residuals, capturing spatial correlations that guide residual updates. In the temporal domain, a structured gating mechanism, comprising hierarchical feature propagation (HFP) and Gumbel-Sigmoid sampling, converts hierarchical dynamic cues into sparse residual update decisions under differentiable optimization. A multi-level discrete scheme is further adopted to provide fine-grained control over residual updates while preserving intricate dynamic details. Extensive experiments across consumer GPUs, industrial edge IoT devices, and a physical telepresence testbed demonstrate that S$^2$GS consistently reduces per-frame optimization time and storage footprint while maintaining competitive visual quality. Compared with QUEEN, S$^2$GS reduces per-frame optimization time by 59% and storage costs by 85% on an RTX 4090 GPU. On the Jetson AGX Orin, S$^2$GS delivers the highest rendering throughput (60+ FPS) and the lowest energy consumption among the evaluated methods, demonstrating its potential for deployment in resource-constrained systems.

</details>

#### 2026-08-20 - Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models

**Authors:** Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh
**Links:** [abs](https://arxiv.org/abs/2608.19556) - [pdf](https://arxiv.org/pdf/2608.19556)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, scene flow, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models
- 作者：Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh
- 出版日期：2026-08-20
- 分类：Dynamic / 4D Reconstruction（次要分类：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.19556

### 一句话总结
Stream4D 提出用前馈式 4D 重建奖励替代静态 3D 重建批评器，为流式自回归扩散视频模型提供显式场景动态建模，从而改善长时程视频生成中的几何漂移与运动退化问题。

### 研究问题
流式自回归扩散视频模型在长时程生成中，因训练目标仅优化局部帧预测，导致世界几何与动态不一致，出现累积几何漂移和运动趋于静态或非自然的问题。已有双向方法依赖 3D 高斯泼溅重建的奖励信号，但单一刚性 3D 重建无法建模动态场景，会误将真实物体运动视为重建误差，且该批评器在自回归设置下可能被“冻结视频”这一捷径所利用。

### 核心思路/方法
- 用前馈式 4D 重建奖励替换静态 3D 重建批评器，显式建模场景动态，使连贯运动获得高一致性奖励。
- 增加一个运动先验项，奖励自然的场景流幅度，同时惩罚抖动和非刚性伪影，以引导运动幅度与质量。
- 将上述两项与一个轻量级感知锚点（perceptual anchor）组合成最终训练配方。

### 主要贡献
- 提出 Stream4D 方法，将静态 3D 批评器替换为前馈式 4D 重建奖励，解决静态重建对动态场景的误导。
- 引入运动先验，显式奖励自然场景流幅度并抑制抖动与非刚性伪影。
- 在多种自回归视频骨干网络和不同生成时长下，Stream4D 提升了 4D 重建质量、更有效地保持运动，并获得更高的人类对齐偏好。

### 局限性
摘要未提供足够信息，未明确提及具体的失败案例、计算开销、训练稳定性或对特定场景类型的限制。

### 阅读优先级
**高**。理由：该工作针对流式自回归视频生成中的核心动态一致性问题提出新训练奖励方案，结合 4D 重建与运动先验，方法新颖且适用于多种骨干网络，实验宣称在多项指标上取得改进，对视频生成与 4D 重建交叉领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Streaming autoregressive diffusion models enable real-time, long-horizon video generation, but their training objectives optimize local frame prediction rather than the geometry and dynamics of a coherent world: long rollouts accumulate geometric drift and degrade into static or unnatural motion. Recent bidirectional approaches address this problem using rewards signals built upon 3D Gaussian-Splatting reconstruction. However, a single rigid 3d reconstruction cannot model a dynamic scene, so this critic penalizes genuine object motion as reconstruction error and is maximized by freezing the video. This shortcut is especially detrimental in the AR setting, where each chunk can propagate an already-static configuration. In this work, we propose Stream4D, which replaces the static critic with a feed-forward 4D reconstruction reward that explicitly models scene dynamics, allowing coherent motion to receive high consistency rewards. To further guide motion magnitude and quality, we add a motion prior that rewards natural scene-flow magnitude while penalizing jitter and non-rigid artifacts. Our final recipe combines these two terms with a lightweight perceptual anchor. Across various autoregressive video backbones and various generation horizons, Stream4D improves 4D reconstruction quality, preserves motion more effectively, and achieves higher human-aligned preference. Project page: https://banyuanhao.github.io/Stream4D/

</details>

#### 2026-08-19 - RVLoss: Runoff Vote Loss for Self-Supervised LiDAR Scene Flow Estimation

**Authors:** Shiming Wang, Liangliang Nan, Julian Kooij, Holger Caesar, Yancong Lin
**Links:** [abs](https://arxiv.org/abs/2608.18864) - [pdf](https://arxiv.org/pdf/2608.18864)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** scene flow

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RVLoss: Runoff Vote Loss for Self-Supervised LiDAR Scene Flow Estimation
- 作者：Shiming Wang, Liangliang Nan, Julian Kooij, Holger Caesar, Yancong Lin
- 出版日期：2026-08-19
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2608.18864

### 一句话总结
本文提出RVLoss，一种通过两阶段 runoff vote 机制将运动刚性约束融入损失设计的自监督LiDAR场景流估计方法，在Argoverse2 2026挑战赛中相比基线损失设计提升20%。

### 研究问题
LiDAR场景流估计中，现有自监督方法（如Chamfer损失）仅依赖最近邻距离，不强制运动刚性，导致物体实例内部（尤其是大物体）的流场一致性不足。尽管已有方法加入正则化项，但点间流一致性仍有限。

### 核心思路/方法
- 关键观察：由最近邻搜索计算的逐点运动，可通过投票（top-k voting）聚合成少量主导流候选；当用这些候选补偿源点云时，最能代表底层刚性运动的流在第二次投票（top-1 voting）后获得最高共识。
- 方法：基于上述两阶段 runoff vote 机制设计损失，生成 cluster-wise 刚性流和自由形态流作为自监督学习的伪标签。
- 特性：RVLoss可直接集成到现有前馈架构中，无需额外正则化项。

### 主要贡献
1. 提出RVLoss，一种通过设计固有地融入运动刚性约束的自监督损失函数。
2. 引入两阶段 runoff vote 机制，有效识别主导刚体运动候选。
3. 在Argoverse2 2026挑战赛中达到自监督方法最优性能，相比替代损失设计基线提升20%。
4. 跨数据集评估显示在四个额外数据集上均有一致性能提升。
5. 代码将在论文接收后发布。

### 局限性
摘要未提供足够信息。具体局限性（如计算开销、对极端场景的鲁棒性、参数敏感性等）未在摘要中说明。

### 阅读优先级
**高**
理由：该论文针对自监督场景流估计中运动一致性这一核心难题，提出一种新颖且可即插即用的损失设计，在多个数据集上取得显著性能提升（20%），且无需修改网络架构。对从事LiDAR场景流、自监督学习、4D重建方向的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

LiDAR scene flow estimates point-wise motion between two consecutive scans, referred to as the source and target. Leading self-supervised methods typically minimize the Chamfer loss, the nearest neighbor distance between the flow-compensated source and the target. However, nearest-neighbor search does not enforce motion rigidity, often leading to inconsistent flows within object instances. Existing approaches address this issue with additional regularization terms, but flow consistency among points remains limited, especially for large objects. We propose RVLoss, a self-supervised loss that incorporates motion rigidity by design through a runoff vote mechanism. Our key observation is that the point-wise motion, calculated from nearest neighbor search, can often be grouped into a small set of dominant flow candidates by voting (top-k voting). Furthermore, when compensating the source by these candidates, the flow that best represents the underlying rigid motion often yields the highest consensus after a second voting (top-1 voting). Based on this insight, we incorporate the two-stage runoff vote into loss design and create cluster-wise rigid flows and free-form flows as pseudo-labels for self-supervised learning. RVLoss can be seamlessly integrated into existing feedforward architectures. Experiments on the Argoverse2 2026 Challenge show that models trained with RVLoss achieve state-of-the-art performance among self-supervised approaches, outperforming baseline models trained with alternative loss designs by 20%. Moreover, cross-dataset evaluations demonstrate consistent performance improvements across four additional datasets. Code will be released upon acceptance.

</details>

#### 2026-08-19 - DyG$^2$T: Modeling Object Dynamics with 3D Gaussian Temporal-Spatial Particle Graph Transformer

**Authors:** Yansong Wang, Zhaobo Qi, Xinyan Liu, Beichen Zhang, Shuhui Wang, Weigang Zhang, Qingming Huang
**Links:** [abs](https://arxiv.org/abs/2608.18498) - [pdf](https://arxiv.org/pdf/2608.18498)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion trajectory, motion trajectories

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DyG²T: Modeling Object Dynamics with 3D Gaussian Temporal-Spatial Particle Graph Transformer
- 作者：Yansong Wang, Zhaobo Qi, Xinyan Liu, Beichen Zhang, Shuhui Wang, Weigang Zhang, Qingming Huang
- 出版日期：2026-08-19
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2608.18498

### 一句话总结
本文提出DyG²T框架，通过空间补全、时间判别与多尺度粒子图交互建模，改进物体运动轨迹预测和外观预测的准确性。

### 研究问题
如何从有限的视觉观测中准确建模物体动力学，实现精确的运动轨迹预测。现有方法将重建的粒子表征压缩为稀疏关键点并用局部约束交互建模，导致细粒度局部细节丢失、跨时空判别性交互建模不清晰，引发轨迹漂移和外观预测不准。

### 核心思路/方法
- 空间维度：每个关键点聚合邻近原始粒子位置以恢复局部细节，并显式编码关键点间相对偏移以增强几何结构感知。
- 时间维度：引入时间解缠网络（TDN）在潜空间中识别主导的跨帧变化并放大帧间差异，得到时间判别表征，再经时间注意力聚合捕捉逐帧时间演化线索。
- 交互建模：粒子图Transformer利用全局注意力保留关键点间判别性长程依赖，缓解局部约束建模带来的表征同质化问题。

### 主要贡献
1. 提出空间补全与时间判别相结合的关键点表征增强策略，兼顾局部细节与帧间差异。
2. 引入时间解缠网络（TDN）提升表征的时间判别性。
3. 设计基于全局注意力的粒子图Transformer，实现多尺度长程交互建模。
4. 在合成和真实数据集上验证了精确动力学建模与跨物体及真实场景泛化能力。

### 局限性
摘要未提供足够信息，未明确提及现有方法的失败案例、计算成本、实时性限制或特定场景失效情况等局限性内容。

### 阅读优先级
**中等**。理由：该工作面向具身交互场景下的动力学建模与轨迹预测任务，方法设计较系统（空间、时间、图交互三线并进），且声称在合成与真实数据上均有验证，对从事4D重建或动态场景理解的读者有参考价值。但摘要未给出量化实验结果对比，无法判断其相对现有方法的优势幅度，因此优先级别定为中等。

</details>

<details>
<summary>Abstract</summary>

Modeling object dynamics from limited visual observations is a fundamental problem for enabling accurate motion trajectory prediction in embodied interaction scenarios. Existing dynamics modeling methods first compress reconstructed particle representations into sparse Key Points and model their evolution using locally constrained interactions, thereby discarding fine-grained local details and obscuring discriminative interaction modeling across spatial and temporal scales, leading to drifting trajectories and inaccurate appearance prediction. To tackle these issues, we propose DyG$^2$T, a dynamics modeling framework that infers object motion trajectories by spatially completing and temporally discriminating Key Point representations and modeling multi-scale interaction over particle graphs. Spatially, DyG$^2$T enriches each Key Point by aggregating neighboring raw particle positions to recover fine-grained local details, while explicitly encoding relative offsets among Key Points to enhance geometric structure perception. Temporally, we introduce a Temporal Disentangling Network (TDN) to identify dominant cross-frame variations in latent space and amplify inter-frame differences, yielding temporally discriminative representations that are subsequently aggregated via Temporal Attention to capture frame-wise temporal evolution cues. For comprehensive interaction modeling, a Particle Graph Transformer leverages global attention to preserve discriminative long-range dependencies among Key Points, mitigating representation homogenization induced by locality-constrained modeling and providing a robust basis for accurate trajectory prediction. Experiments on both synthetic and real-world datasets demonstrate that DyG$^2$T achieves accurate dynamics modeling and reasoning, and exhibits strong cross-object and real-world generalization.

</details>

#### 2026-08-18 - Depth Anything V4: Dynamic 4D Scene Reconstruction via Riemannian Flow Matching on 4D Gaussian Splatting

**Authors:** Jiaming Fan, Jian Lu, Jinling Jia, Chenbin Zhang
**Links:** [abs](https://arxiv.org/abs/2608.18388) - [pdf](https://arxiv.org/pdf/2608.18388)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, dynamic 4D, 4D Gaussian, scene reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Depth Anything V4: Dynamic 4D Scene Reconstruction via Riemannian Flow Matching on 4D Gaussian Splatting
- 作者：Jiaming Fan, Jian Lu, Jinling Jia, Chenbin Zhang
- 出版日期：2026-08-18
- 分类：Dynamic / 4D Reconstruction；3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.18388

### 一句话总结
本文提出Depth Anything V4（DAV4）框架，将黎曼流匹配（RFM）应用于4D高斯溅射参数，从单目视频实现动态4D场景重建，并通过受控实验分离并量化了RFM的独立贡献。

### 研究问题
如何从单目视频进行高质量动态4D场景重建，且不依赖人工标注深度标签作为训练损失。

### 核心思路/方法
- 将**黎曼流匹配（RFM）**直接应用于4D高斯溅射的参数空间（尺度、旋转、不透明度），在非欧几里得流形上定义概率路径，从而保证所有中间状态的有效性。
- 通过**受控实验**将RFM的贡献与测试时优化（TTO）和预训练过程解耦，以独立评估RFM带来的性能增益。
- 使用确定性MLP基线（相同数据、架构和TTO）进行对比，以量化RFM的独立贡献。
- 采用**负高斯对数似然**和**期望校准误差**对不确定性进行量化。

### 主要贡献
- 提出DAV4框架，将RFM创新性地用于4D高斯溅射参数，实现在非欧流形上的概率路径构造。
- 通过受控实验证明RFM的独立贡献：RFM F-score为0.806，同条件下的MLP基线为0.762，即**+0.044的增益来自RFM本身**。
- 提供了修正的计算成本分析：预训练需360 GPU-hours，在超过10,000场景的大规模部署中可摊销。
- 在动态重建和新视角合成任务上，DAV4优于先前的Depth Anything系列模型以及逐场景4D-GS方法。
- 全程不使用人工标注的深度标签作为训练损失。

### 局限性
摘要未提供足够信息：摘要未提及DAV4在极端动态场景、遮挡、光照变化等条件下的表现，也未给出与其他SOTA方法在多个数据集上的详细对比指标（仅提及F-score），未报告运行效率或显存占用等实用限制。

### 阅读优先级
**高**。理由：该工作将流匹配扩展到非欧几里得流形并应用于4D高斯溅射，属于方法创新且提供了清晰的受控消融实验来分离贡献，对动态场景重建和生成式3D表示方向的读者具有较高参考价值；同时公开了计算成本分析，有助于评估实际部署可行性。

</details>

<details>
<summary>Abstract</summary>

We present Depth Anything V4 (DAV4), a framework for dynamic 4D scene reconstruction from monocular video. Our key contribution is the application of Riemannian Flow Matching (RFM) to 4D Gaussian Splatting parameters, defining probability paths directly on non-Euclidean manifolds (scale, rotation, opacity), ensuring all intermediate states are valid. Through controlled experiments, we isolate RFM's contribution from test-time optimization (TTO) and pre-training. A deterministic MLP baseline with the same data, architecture, and TTO achieves F-score 0.762; RFM achieves 0.806 - the +0.044 gain is RFM's isolated contribution. We provide corrected computational cost analysis: pre-training is 360 GPU-hours, amortizing for large-scale deployment (over 10,000 scenes). Uncertainty is quantified via Negative Gaussian Log-Likelihood and Expected Calibration Error. DAV4 outperforms prior Depth Anything models and per-scene 4D-GS on dynamic reconstruction and novel-view synthesis, while using no human-annotated depth labels as training losses.

</details>

#### 2026-08-18 - QuARC-GS: Quantized Anchored Residual Coding for Compact Dynamic Scene Streaming with Gaussian Splatting

**Authors:** Vu Trung Nghia Nguyen, Yuchen Wang, Kyung Chul Lee, Kevin C. Zhou
**Links:** [abs](https://arxiv.org/abs/2608.18285) - [pdf](https://arxiv.org/pdf/2608.18285)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, scene reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, scene representation, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：QuARC-GS: Quantized Anchored Residual Coding for Compact Dynamic Scene Streaming with Gaussian Splatting
- 作者：Vu Trung Nghia Nguyen, Yuchen Wang, Kyung Chul Lee, Kevin C. Zhou
- 出版日期：2026-08-18
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.18285

### 一句话总结
提出一种基于量化锚定残差编码的4D场景优化框架，用于动态场景的在线重建与流式传输，在保持重建质量和速度的同时，将每帧存储需求相比最先进方法降低最高11倍。

### 研究问题
如何实现对动态3D场景的高压缩率、低存储占用的在线自由视角视频流式传输，同时兼顾重建质量和速度，特别是针对较长视频的场景。

### 核心思路/方法
- 使用单一规范帧（canonical frame）加高度压缩的逐帧残差（per-frame residuals）来表示动态场景。
- 对残差采用两种互补压缩策略，分别针对运动、外观和稠密化过程。
- 引入**量化感知锚定变形**（quantization-aware anchor deformation）：抑制不显著的运动更新，同时保留有意义的变形，在低存储流式传输下维持重建质量。
- 设计**变化门控稠密化策略**（change-gated densification）：仅在存在真实时间变化的区域分配新的高斯体，消除冗余外观更新并降低存储开销。

### 主要贡献
- 提出量化感知的4D场景优化框架，实现超高压缩率的在线动态场景流式传输。
- 引入锚定残差编码和双策略压缩机制，覆盖运动、外观和稠密化。
- 设计变化门控稠密化策略，仅在变化区域新增高斯体，减少冗余。
- 在广泛使用的数据集上的实验表明，相比最先进方法，每帧存储最高可削减11倍，同时保持有竞争力的重建质量和训练速度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对动态场景高斯泼溅的存储瓶颈提出了量化和残差编码的联合优化方案，压缩比提升显著（最高11倍），且同时兼顾速度与质量，对于在线自由视角视频流式传输这一实际应用场景具有较强价值。摘要中提供了清晰的技术路线和实验结论，适合重点关注。

</details>

<details>
<summary>Abstract</summary>

3D scene representation techniques such as neural radiance fields (NeRFs) and Gaussian splatting have made substantial progress in novel view synthesis, achieving high-quality renderings from arbitrary view angles. More recently, such techniques have been extended to dynamic 3D scenes; however, achieving sustainable online free-viewpoint video (FVV) streaming remains challenging, especially for longer videos, due to significant storage demands of detailed scene representations and high reconstruction/rendering speed needs. To address these challenges, we propose Quantized Anchored Residual Coding Gaussian Streaming (QuARC-GS), a quantization-aware 4D scene optimization framework for online dynamic scene reconstruction that achieves ultra-high compression while maintaining reconstruction speed and quality. QuARC-GS represents a scene using a single canonical frame and highly compressed per-frame residuals. Specifically, we compress each residual through two complementary strategies targeting motion, appearance, and densification. We introduce quantization-aware anchor deformation, which suppresses insignificant motion updates while preserving meaningful deformations, maintaining reconstruction quality under low-storage streaming. Furthermore, we design a change-gated densification strategy that allocates new Gaussians only in regions exhibiting genuine temporal changes, effectively eliminating redundant appearance updates and reducing storage overhead. Extensive experiments on widely used datasets demonstrate that QuARC-GS enables competitive reconstruction quality and training speed while cutting per-frame storage by up to 11$\times$ compared to the state-of-the-art.

</details>

#### 2026-08-18 - UniQuery4R: Unified 4D Scene Reconstruction from a Single Query

**Authors:** Tiancheng Chen, Sheng Tang, Wenhua Jin, Weiqi Zhang, Juntong Fang, Junsheng Zhou, Zesong Li
**Links:** [abs](https://arxiv.org/abs/2608.17283) - [pdf](https://arxiv.org/pdf/2608.17283)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** dynamic 4D, scene flow, scene reconstruction, dense reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniQuery4R: Unified 4D Scene Reconstruction from a Single Query
- 作者：Tiancheng Chen, Sheng Tang, Wenhua Jin, Weiqi Zhang, Juntong Fang, Junsheng Zhou, Zesong Li
- 出版日期：2026-08-18
- 分类：Dynamic / 4D Reconstruction（次要：3D Reconstruction & Multi-view Geometry）
- 链接：https://arxiv.org/abs/2608.17283

### 一句话总结
本文提出UniQuery4R，一种基于查询条件的统一4D场景重建框架，通过对多帧片段进行一次性编码并在解码时按需选择源视图、目标视图与坐标，实现高效且可复用的动态场景重建。

### 研究问题
现有的前馈式动态4D场景重建方法通常需要预测密集的任务特定映射，或独立处理源-目标图像对，导致在稀疏查询场景下产生不必要的计算，且在不同帧对之间特征复用有限。本文旨在解决这一问题。

### 核心思路/方法
UniQuery4R采用查询条件化框架，具体步骤为：
1. 将多帧片段一次性编码为共享表示；
2. 在解码阶段，通过源到目标的交叉注意力，仅需指定源视图、目标视图和连续的源图像坐标即可生成查询；
3. 每个查询同时预测目标对应关系、目标时刻的三维位置、场景流以及源深度，并逐视图估计相机参数；
4. 编码后的片段可跨任意源-目标选择重复使用，支持通过批量查询实现稀疏推理和密集重建，且无需依赖固定片段长度的学习型时间嵌入；
5. 引入场景流的“方向-幅度”参数化，并对运动点和静态点进行分离监督。

### 主要贡献
1. 提出查询条件化的统一4D重建框架，实现编码特征的跨帧对复用，减少冗余计算；
2. 支持任意源-目标视图选择，统一支持稀疏查询推理与密集重建；
3. 提出场景流的“方向-幅度”参数化及运动/静态点分离监督策略；
4. 在WorldTrack数据集上，该方法在场景流估计和动态点重建两项任务中均取得最优宏平均结果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作针对动态4D重建中的计算效率和特征复用问题提出了新颖的框架设计，技术上较为完整，且实验指标在WorldTrack上领先。但摘要未涵盖与更广泛方法（如逐对处理基线）的详细对比效率数据、运行时间或局限性分析，因此适合对4D重建/动态场景理解方向感兴趣的读者精读，若仅关注其他子领域可暂缓。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic 4D scenes requires jointly estimating correspondence, geometry, object motion, and camera motion. Existing feed-forward methods typically predict dense task-specific maps or independently process source-target pairs, leading to unnecessary computation for sparse queries and limited feature reuse across different frame pairs. We present UniQuery4R, a query-conditioned framework that encodes a multi-frame clip once and selects the source view, target view, and continuous source-image coordinate only at decoding time via source-to-target cross-attention. Each query jointly predicts target correspondence, target-time 3D position, and scene flow, along with source depth, while camera parameters are estimated per view. This design allows the encoded clip to be reused across arbitrary source-target selections and supports both sparse inference and dense reconstruction through batched queries, without learned temporal embeddings tied to a fixed clip length. We further introduce a direction-magnitude parameterization of scene flow with separate supervision for moving and static points. Among the evaluated methods, UniQuery4R achieves the best macro-average results on WorldTrack for both scene-flow estimation and dynamic-point reconstruction.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-08

#### 2026-08-20 - HandMvNet: Real-Time 3D Hand Pose Estimation Using Multi-View Cross-Attention Fusion

**Authors:** Muhammad Asad Ali, Nadia Robertini, Didier Stricker
**Links:** [abs](https://arxiv.org/abs/2608.20093) - [pdf](https://arxiv.org/pdf/2608.20093)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HandMvNet: Real-Time 3D Hand Pose Estimation Using Multi-View Cross-Attention Fusion
- 作者：Muhammad Asad Ali, Nadia Robertini, Didier Stricker
- 出版日期：2026-08-20T14:24:35Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.20093

### 一句话总结
HandMvNet 是一种基于多视图交叉注意力融合的实时 3D 手部姿态与形状估计方法，在无需相机参数输入的情况下，实现了比单目方法更准确、比现有多视图方法更快的推理。

### 研究问题
如何从多视图相机图像中实时、准确地估计 3D 手部姿态和形状，同时克服单目方法中的尺度-深度模糊问题，并减少对相机参数的依赖。

### 核心思路/方法
采用多视图注意力融合机制，从多个视角图像中有效整合特征，以学习一致的绝对手部姿态和形状。与先前需要输入相机参数的多视图方法不同，该方法无需相机参数即可学习 3D 几何，从而简化输入并降低推理开销，实现实时性能。

### 主要贡献
- 提出 HandMvNet，据摘要所述为最早的多视图实时 3D 手部姿态与形状估计方法之一。
- 通过多视图注意力融合机制，获得比单目方法更一致的绝对手部姿态和形状。
- 消除了多视图方法对相机参数输入的需求。
- 相比现有方法，显著降低推理时间并保持竞争力的结果。
- 在公开数据集上的定性和定量评估中，在相同设置下优于先前方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法针对多视图 3D 手部姿态估计的实时性问题提出了新方案，兼具无需相机参数和低推理延迟的特点，对相关领域的研究者和工程应用具有较高参考价值。不过由于摘要未披露网络结构细节和实验基准的具体内容，阅读时应结合论文正文验证其声称的性能。

</details>

<details>
<summary>Abstract</summary>

In this work, we present HandMvNet, one of the first real-time method designed to estimate 3D hand motion and shape from multi-view camera images. Unlike previous monocular approaches, which suffer from scale-depth ambiguities, our method ensures consistent and accurate absolute hand poses and shapes. This is achieved through a multi-view attention-fusion mechanism that effectively integrates features from multiple viewpoints. In contrast to previous multi-view methods, our approach eliminates the need for camera parameters as input to learn 3D geometry. HandMvNet also achieves a substantial reduction in inference time while delivering competitive results compared to the state-of-the-art methods, making it suitable for real-time applications. Evaluated on publicly available datasets, HandMvNet qualitatively and quantitatively outperforms previous methods under identical settings. Code is available at github.com/pyxploiter/handmvnet.

</details>

#### 2026-08-20 - Gravity-aware partially calibrated absolute pose estimation from affine- or rotation-covariant features

**Authors:** Marcus Valtonen Örnhag, Alberto Jaenal, Stefan Adalbjörnsson
**Links:** [abs](https://arxiv.org/abs/2608.20056) - [pdf](https://arxiv.org/pdf/2608.20056)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gravity-aware partially calibrated absolute pose estimation from affine- or rotation-covariant features
- 作者：Marcus Valtonen Örnhag, Alberto Jaenal, Stefan Adalbjörnsson
- 出版日期：2026-08-20
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.20056

### 一句话总结
本文利用IMU提供的重力向量与特征描述符蕴含的局部几何信息，提出两种新的高效求解器，用于联合估计绝对位姿与焦距的部分标定绝对位姿估计问题。

### 研究问题
如何利用IMU重力先验和特征诱导的局部几何信息，以更少的对应点数量和更低计算成本，实现对绝对位姿与焦距的联合估计，从而在部分标定场景下提升定位精度与效率。

### 核心思路/方法
- 从IMU数据获取重力向量，并结合特征描述符（如SIFT）中嵌入的局部几何信息，
- 推导出新的约束条件，用于联合估计绝对位姿和焦距。
- 基于这些约束构建两个求解器：
  - UP1PfAC：仅需单个仿射对应（affine correspondence）即可求解；
  - UP2PfORI：需要两个旋转协变特征（rotation-covariant features）。
- 与传统需要四个点对应的半标定绝对位姿方法相比，本文方法所需样本更少、计算成本更低，便于集成到现代RANSAC类鲁棒估计框架中。

### 主要贡献
- 首次将特征诱导的局部几何信息应用于部分标定绝对位姿估计，填补了该方向的研究空白；
- 推导了结合重力向量与特征局部几何的新约束，并据此设计两个高效求解器（UP1PfAC和UP2PfORI）；
- 在公开大规模数据集上验证了方法在定位精度和速度上的有效性，相较于现有最优方法表现出色，同时能准确估计焦距。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对部分标定绝对位姿估计提出了更高效的求解器（最少仅需1个仿射对应或2个旋转协变特征），显著减少了传统方法所需的对应点数量，并利用IMU的普及性，方法适用性广。摘要明确表明在两个大规模公开数据集上进行了验证且效果优于现有方法，且结果涉及实际应用常用的RANSAC框架，对视觉定位、SLAM、XR等领域具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Inertial measurement units (IMUs) are now standard in most consumer devices, such as smartphones, drones, and extended reality (XR) headsets. By fusing visual and inertial data, localization systems gain significantly in speed and robustness compared to vision-only or IMU-only approaches. However, traditional pose estimation methods fail to utilize the local geometric information embedded in feature descriptors like SIFT. Recent work has proved the advantages of leveraging this information for relative and absolute pose estimation, but its application to partially calibrated absolute pose estimation remains unexplored. In this paper, we derive novel constraints for joint estimation of absolute pose and focal length, making use of a gravity vector obtained from IMU data and the feature-induced local geometry, which we use to construct two efficient solvers: UP1PfAC, that operates given a single affine correspondence and UP2PfORI, which requires two orientation-covariant features. Unlike traditional, semi-calibrated absolute pose methods requiring four point correspondences, our solvers benefit from fewer samples and lower computational cost, simplifying robust estimation in modern RANSAC-like frameworks. We evaluate the proposed solvers against the state-of-the-art on large-scale public datasets and demonstrate that our method achieves fast and accurate localization and focal length estimation.

</details>

#### 2026-08-20 - Point-Based 3D Reconstruction from Sparse Views under Known Illumination

**Authors:** Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad, Markus Worchel, J. Andreas Bærentzen, Thomas B. Moeslund
**Links:** [abs](https://arxiv.org/abs/2608.20000) - [pdf](https://arxiv.org/pdf/2608.20000)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Point-Based 3D Reconstruction from Sparse Views under Known Illumination（已知光照下基于点的稀疏视角三维重建）
- 作者：Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad, Markus Worchel, J. Andreas Bærentzen, Thomas B. Moeslund
- 出版日期：2026-08-20T13:15:27Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：https://arxiv.org/abs/2608.20000

### 一句话总结
本文提出一种基于不透光beta surfel的可微点渲染方法，在已知光照条件下利用物理光传输约束实现稀疏视角下的紧凑三维重建，以平均仅267个surfel即可超越现有基于点的基线方法。

### 研究问题
如何在已知光照的稀疏视角条件下，以更少的图元数量实现高精度的基于点的三维表面重建？现有方法（如神经隐式表面或密集点云/高斯溅射）通常需要大量图元，本文试图探索一种更紧凑的表示方案。

### 核心思路/方法
- 采用基于**不透明beta surfel**的可微点渲染框架，以椭圆/圆盘状图元表示表面。
- 设计了一种**显式伴随光传输（adjoint light transport）**公式，用于计算surfel几何和外观参数的梯度。
- 通过将**基于物理的光传输**纳入优化过程，使重建受到光照物理约束的引导，从而在直接光照受控场景中提升表面恢复精度。

### 主要贡献
- 提出了一种仅依赖少量图元（平均267个surfel）即可完成高质量重建的点基方法。
- 在5个合成物体、10个视角的重建实验中，取得了所有评估基线中**最低的平均对称Chamfer距离**。
- 相较于最强点基基线，**平均Chamfer距离相对降低28.5%**，且所用图元数减少约161个（约为基线数量的极小比例）。
- 定向Chamfer指标显示，该方法在**精度**上表现更优，在**完整性**上与相关点基方法竞争力相当。

### 局限性
摘要未提供足够信息。具体包括：未提及方法在真实场景或非受控光照下的表现、对光照估计误差的鲁棒性、计算开销、训练时间，以及与其他非点基方法（如神经隐式表面）的详细对比数据。此外，实验仅涉及合成物体，未见真实数据验证。

### 阅读优先级
**高**。理由：本文在稀疏视角重建领域提出了一个在效率和精度上均有显著改进的紧凑点基解决方案，实验结果显示图元数量大幅减少且误差显著降低，对关注点云/表面重建、可微渲染和光传输建模的研究者具有直接参考价值。其方法思路（物理约束+紧凑表示）也可能对相关下游任务有启发意义。

</details>

<details>
<summary>Abstract</summary>

Sparse view 3D reconstruction is commonly addressed with neural implicit surfaces or dense point-based representations such as Gaussian splatting. Surface-aware splatting methods improve extracted geometry through oriented primitives and regularization, while RadiosityGS incorporates differentiable light transport through a radiosity inspired finite-element surfel formulation. We propose a differentiable point rendering method based on opacity-bearing beta surfels. An opacity explicit adjoint light transport formulation provides gradients for surfel geometry and appearance parameters, allowing physically based light transport to constrain reconstruction. Across five synthetic objects reconstructed from ten posed views, our method achieves the lowest mean symmetric Chamfer distance among the evaluated baselines and reduces mean Chamfer distance by 28.5% relative to the strongest point-based baseline while using only 267 surfels on average, approximately ~161 fewer primitives. Directional Chamfer results further show improved accuracy and competitive completion relative to related point-based methods. These results show that, in the controlled direct illumination setting, compact beta surfels combined with transport-based optimization can recover surfaces without relying on the tens to hundreds of thousands of primitives used by the evaluated baselines.

</details>

#### 2026-08-19 - CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction

**Authors:** Shihan Chen, Junjing Zhang, Qingsong Yan, Haibing Liu, Haofan Ren, Fei Deng
**Links:** [abs](https://arxiv.org/abs/2608.18413) - [pdf](https://arxiv.org/pdf/2608.18413)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** multi-view stereo, structure from motion, mesh reconstruction, surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction
- 作者：Shihan Chen, Junjing Zhang, Qingsong Yan, Haibing Liu, Haofan Ren, Fei Deng
- 出版日期：2026-08-19
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.18413

### 一句话总结
CoMVS-GS 提出一种结合多视角立体与三维高斯泼溅的通用表面重建框架，通过几何先验初始化、相互监督机制和 Delaunay 图割网格化流程，提升弱观测与遮挡区域的重建精度与网格紧凑性。

### 研究问题
3D Gaussian Splatting 在弱观测和遮挡区域中，高斯基元可能生长为不稳定或几何不一致的结构，导致难以生成精确的网格表面。论文旨在解决这一问题，同时保持高效的新视角合成能力。

### 核心思路/方法
- 从稠密多视角立体点云初始化高斯基元，并赋予预展平尺度与法向对齐方向，相比稀疏 SfM 初始化提供更强的几何先验，减少早期优化歧义。
- 引入 PatchMatch-3DGS 相互监督：高斯渲染的深度与法向用于初始化 PatchMatch 细化，而细化后的 PatchMatch 深度反过来监督高斯优化，以改善弱约束区域的几何。
- 表面提取阶段，用 Delaunay 图割网格化流程替代传统 TSDF 体素融合，降低对体素分辨率的敏感性，同时保留可见性一致的表面证据。

### 主要贡献
1. 提出 CoMVS-GS，一个通用表面重建框架，有效结合多视角立体与三维高斯泼溅。
2. 设计稠密 MVS 点云初始化策略，为高斯基元提供更强的几何先验。
3. 提出 PatchMatch-3DGS 相互监督机制，改善弱约束区域的几何质量。
4. 引入 Delaunay 图割网格化管线替代 TSDF 融合，提升网格紧凑性并降低分辨率敏感性。
5. 在 DTU、GauU-Scene V2 和 MatrixCity 数据集上验证，在物体级重建上保持竞争力，在室外场景中提升几何精度与网格紧凑性，同时维持高渲染质量。

### 局限性
摘要未提供足够信息：摘要未具体说明在哪些类型场景下方法仍存在不足，也未提及计算开销、运行时间或与现有方法的具体量化对比细节，以及方法对输入图像数量或重叠度的敏感性等限制。

### 阅读优先级
**高**
理由：该工作针对 3D Gaussian Splatting 在表面重建中的关键痛点（弱观测区域几何不稳定）提出了系统性的解决方案，涵盖初始化、监督机制和网格化三个环节；实验覆盖物体级与户外场景等多个数据集，方法具有较高的通用性。对于从事三维重建、神经渲染或 MVS 相关研究的读者，这项工作具有较强的参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting enables efficient novel view synthesis, but accurate mesh reconstruction remains difficult in weakly observed and occluded regions, where Gaussian primitives may grow into unstable or geometrically inconsistent structures. We propose CoMVS-GS, a general surface reconstruction framework that combines Multi-View Stereo with Gaussian splatting. CoMVS-GS initializes Gaussian primitives from dense multi-view stereo points with pre-flattened scales and normal-aligned orientations, providing stronger geometric priors than sparse structure-from-motion initialization and reducing ambiguity during early optimization. It further introduces PatchMatch-3DGS Mutual Supervision, where Gaussian-rendered depths and normals initialize PatchMatch refinement, and refined PatchMatch depths supervise Gaussian optimization to improve weakly constrained geometry. For surface extraction, CoMVS-GS replaces truncated signed distance field voxel fusion with a Delaunay graph-cut meshing pipeline, reducing sensitivity to voxel resolution while preserving visibility-consistent surface evidence. Experiments on DTU, GauU-Scene V2, and MatrixCity show that CoMVS-GS remains competitive on object-level reconstruction and improves geometric accuracy and mesh compactness in outdoor scenes while maintaining high rendering quality.

</details>

#### 2026-08-18 - Transferable Tool-Tissue Contact Detection from Stereo Depth in Robot-Assisted Surgery

**Authors:** Mingyeung Wu, Zhonghao Zhang, Hao Yang, Alan Kuntz, Jie Ying Wu
**Links:** [abs](https://arxiv.org/abs/2608.18270) - [pdf](https://arxiv.org/pdf/2608.18270)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** stereo depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Transferable Tool-Tissue Contact Detection from Stereo Depth in Robot-Assisted Surgery
- 作者：Mingyeung Wu, Zhonghao Zhang, Hao Yang, Alan Kuntz, Jie Ying Wu
- 出版日期：2026-08-18
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.18270

### 一句话总结
本文提出利用立体视觉生成的深度图，通过工具-组织间最小距离信号结合隐马尔可夫模型进行可迁移的器械-组织接触检测，在跨任务与跨模型场景中显著优于基于RGB的方法。

### 研究问题
如何在机器人辅助手术中实现跨场景、可迁移的工具-组织接触检测，克服现有基于RGB外观的方法泛化能力差的问题。

### 核心思路/方法
- 使用立体相机生成的深度图替代RGB外观，为接触检测提供更直接的几何信息。
- 在每个深度帧中，定位工具边界周围的空间支撑最小距离块，并将其约简为单一标量（−log₁₀|d|），该信号随真实接触状态升降。
- 将该观察形式化为全监督的两状态隐马尔可夫模型（HMM）。
- 在6次触诊会话上使用六折留一会话（LOSO）集成拟合模型，阈值从池化的折外预测中选取。
- 在4个保留会话上评估，包含三种类别：同任务同模型、同任务不同模型、不同任务不同模型。

### 主要贡献
- 提出使用深度图像及最小距离信号作为接触检测的强鲁棒线索，替代易过拟合的RGB外观特征。
- 形式化基于HMM的全监督接触检测模型，并采用LOSO集成训练。
- 在保留会话上达到宏F1 0.927、AUPRC 0.980。
- 与复现的RGB基线相比，RGB方法在同类任务上F1达0.965，但跨任务/跨模型时宏F1骤降至0.320，而所提方法保持稳定，表明深度距离信号具备强可迁移性。

### 局限性
摘要未提供足够信息。摘要未提及对完全未见手术场景、真实组织（非硅胶模型）的验证情况，也未讨论深度图像质量退化或遮挡对方法的鲁棒性影响。

### 阅读优先级
**高**。理由：该工作针对手术机器人中接触检测的泛化瓶颈，提出基于深度几何信号的简洁有效方案，实验显示跨任务跨模型大幅优于RGB基线，且指标表现优秀（F1 0.927 / AUPRC 0.980），对手术交互感知和力估计方向有参考价值。

</details>

<details>
<summary>Abstract</summary>

Reliable tool--tissue contact detection can support interaction-aware control and downstream force estimation in robot-assisted surgery. Most existing methods learn a contact classifier from RGB appearance, which is hard to generalize. In this work, we use the depth image generated from a stereo pair to give more information about tool--tissue contact. For each depth frame, we localize a spatially supported minimum-distance patch around the tool boundary and reduce it to a single scalar, $-\log_{10}|d|$; this signal rises and falls in step with ground-truth contact. We formalize this observation with a fully supervised two-state hidden Markov model. We fit this model as a six-fold leave-one-session-out (LOSO) ensemble on six palpation sessions against a single silicone cup-like phantom, with the decision threshold selected from the pooled out-of-fold predictions. It is evaluated on four held-out sessions of three categories: 1. same task on same phantom; 2. same task on different phantom; 3. different task on different phantom. This model reaches held-out macro F1 $0.927$ and AUPRC $0.980$. We further compare against a reproduction of an RGB-based contact classifier from prior work. This RGB-based model achieves high performance on the first category (F1 $0.965$), but substantially lower performance on the other two, resulting in macro F1 $0.320$ across all four sessions. These results indicate that the tool--tissue distance is a strong, transferable cue for contact detection in robot-assisted surgery.

</details>

#### 2026-08-18 - Initialization-Free Bundle Adjustment Revisited: A Controlled Experimental Study

**Authors:** Simon Weber, Mateo de Mayo, Je Hyeong Hong, Carl Olsson, Daniel Cremers, Ronald Clark
**Links:** [abs](https://arxiv.org/abs/2608.18028) - [pdf](https://arxiv.org/pdf/2608.18028)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Initialization-Free Bundle Adjustment Revisited: A Controlled Experimental Study
- 作者：Simon Weber, Mateo de Mayo, Je Hyeong Hong, Carl Olsson, Daniel Cremers, Ronald Clark
- 出版日期：2026-08-18T17:23:06Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.18028

### 一句话总结
本文通过统一评估框架和受控实验，揭示了无初始化束调整（InitFree BA）中“低目标函数值不等于有效重建”的优化-重建鸿沟，指出获得可可靠度量升级的射影重建才是核心挑战。

### 研究问题
现有InitFree BA评估主要关注优化是否成功（即能否降低目标函数值），但未明确低目标函数值是否保证有效的度量三维重建。因此，本文旨在通过受控实验重新审视InitFree BA，探究从随机相机配置出发的射影解在度量升级后是否产生有效的欧氏重建，以及哪些因素决定重建成功。

### 核心思路/方法
构建统一评估框架，包含两部分：
1. 现有OSE（Object-Space Error）公式的C++实现；
2. 基于Blender的数据集生成器，提供精确真值并可控相机配置和观测密度。

在此框架下，对InitFree BA进行受控实验，观察不同条件下的优化行为和最终重建质量。

### 主要贡献
- 揭示了此前被忽视的“优化-重建鸿沟”：OSE值相近的射影解在度量升级后可能得到显著不同的欧氏重建。
- 识别了影响重建成功的关键因素：初始化先验、地标观测密度和度量升级稳定性。
- 提出结论：InitFree BA的主要挑战不仅是最小化OSE目标函数，更在于获得能可靠进行度量升级的射影重建。
- 公开了基准、实现和分析（提供项目页面链接），为未来研究奠定实验基础。

### 局限性
摘要未提供足够信息。摘要仅提及“难以获得可靠度量升级的射影重建”是主要挑战，但未明确给出该方法或实验本身的局限性（如计算复杂度、数据集覆盖面、OSE公式适用范围等）。

### 阅读优先级
**高**。理由：该论文针对无初始化束调整这一较新方向，提出了受控实验基准和关键发现（优化-重建鸿沟），并公开代码和数据集，对从事三维重建、SLAM和多视图几何的研究者有直接参考价值；且识别出不同于传统评价指标的核心问题，可能影响该领域未来的评估标准。

</details>

<details>
<summary>Abstract</summary>

Initialization-free bundle adjustment (InitFree BA) aims to recover camera poses and scene structure directly from image observations, avoiding the geometric initialization stages of conventional structure-from-motion pipelines. Recent methods based on Object-Space Error (OSE) formulations and Variable Projection (VarPro) show encouraging optimization behavior from random camera configurations. However, existing evaluations primarily measure optimization success, leaving unclear whether a low OSE objective yields a valid metric 3D reconstruction. We revisit InitFree BA experimentally through a unified evaluation framework combining a C++ implementation of existing OSE formulations with a Blender-based dataset generator providing exact ground truth and controlled camera configurations and observation densities. Our experiments reveal a previously overlooked optimization--reconstruction gap: projective solutions with similarly low OSE values can lead to substantially different Euclidean reconstructions after metric upgrade. We identify initialization priors, landmark observation density, and metric-upgrade stability as key factors governing reconstruction success. Overall, our results suggest that the main challenge of InitFree BA is not merely minimizing OSE objectives, but obtaining projective reconstructions that admit reliable metric upgrade. We believe that the proposed benchmark, implementation, and analysis establish stronger experimental foundations for future research on initialization-free bundle adjustment, a problem largely unexplored within the computer vision community. Project page is available at https://github.com/simonwebertum/InitFreeBA.git.

</details>

#### 2026-08-18 - Scalix: Uncertainty-Aware Scale-Consistent Monocular SLAM

**Authors:** Sebastian Barbas Laina, Tianyi Zhang, Panagiotis Petropoulakis, Simon Schaefer, Simon Boche, Jaehyung Jung, Cedric Le Gentil, Stefan Leutenegger
**Links:** [abs](https://arxiv.org/abs/2608.17553) - [pdf](https://arxiv.org/pdf/2608.17553)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, monocular depth, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Scalix: Uncertainty-Aware Scale-Consistent Monocular SLAM
- 作者：Sebastian Barbas Laina, Tianyi Zhang, Panagiotis Petropoulakis, Simon Schaefer, Simon Boche, Jaehyung Jung, Cedric Le Gentil, Stefan Leutenegger
- 出版日期：2026-08-18
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.17553

### 一句话总结
提出一个名为 Scalix 的实时单目 SLAM 框架，通过将带不确定性建模的学习式深度线索集成到概率因子图中，实现度量尺度的状态估计和尺度一致性。

### 研究问题
单目 SLAM 存在固有的尺度模糊问题。常见的多模态方案（如视觉惯性系统）在机器人匀速运动时尺度不可观，而基于深度学习的方法虽然引入几何基础模型，但其深度图往往包含噪声且跨帧尺度不一致。因此，如何利用学习式深度线索实现准确、鲁棒且实时运行的度量尺度单目 SLAM 是本文的核心问题。

### 核心思路/方法
Scalix 将学习到的深度线索集成到一个概率因子图公式中。具体来说，它给现有的单目深度模型增加了两类不确定性建模：
1. **逐像素深度不确定性**
2. **逐帧尺度不确定性**

通过将尺度预测视为优化中的独立测量，并利用多视图数据关联，Scalix 能够提升尺度一致性，从而获得度量尺度的状态估计。

### 主要贡献
- 提出 Scalix，一种实时的单目 SLAM 框架，可实现度量尺度状态估计；
- 将深度线索以概率方式（包含像素级深度不确定性和帧级尺度不确定性）集成到因子图优化中；
- 通过多视图数据关联提升了尺度一致性；
- 在大型室外和室内场景的实验中，在度量尺度基准和 up-to-scale 基准上均达到最优性能，同时保持实时性和泛化能力。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法的局限性，例如对训练数据分布的依赖、极端光照或动态场景下的表现、计算资源的具体需求等，均未提及。

### 阅读优先级
**中**。理由：该工作针对单目 SLAM 的尺度模糊这一实际问题，提出了结合深度模型不确定性的因子图方案，实验表明在多个基准上达到 SOTA 且保持实时性，对机器人感知领域有一定参考价值。但摘要中未提供方法细节（如具体网络结构、优化策略、实验配置），若需要深入了解需阅读全文。对于非单目 SLAM 或非几何方向的研究者，优先级可相应降低。

</details>

<details>
<summary>Abstract</summary>

Cameras are ubiquitous sensors in robotics due to their compact form factor and the perceptual richness captured through visual information. Monocular SLAM enables robots to understand the environment with a minimum setup, however, it inherently suffers from scale ambiguity. A common solution is to provide multi-modal sensor configurations, such as visual-inertial systems, where scale is observable unless the robot navigates under a constant-velocity motion, a common scenario in mobile robotics. With the advent of deep-learning, geometric foundation models have been used to address this problem, but the depths maps are often noisy and scale-inconsistent across frames. In this paper, we propose Scalix, a real-time monocular SLAM framework that achieves metric-scale state estimation by integrating learned depth cues into a probabilistic factor-graph formulation. By augmenting existing monocular depth models with both per-pixel depth uncertainty and per-frame scale uncertainty, Scalix treats scale predictions as independent measurements within its optimization, leading to improved scale consistency through multi-view data associations. Experiments in large-scale outdoor and indoor environments demonstrate state-of-the-art performance on both metric and up-to-scale benchmarks while maintaining real-time operation and generalization.

</details>

#### 2026-08-18 - GeoWeaver: Accurate Long-Sequence 3D Reconstruction via Hierarchical Geometric Assembly

**Authors:** Tinghao Jiang, Sheng Tang, Shengzhe Wei, Juntong Fang, Weiqi Zhang, Junsheng Zhou, Zesong Li
**Links:** [abs](https://arxiv.org/abs/2608.17389) - [pdf](https://arxiv.org/pdf/2608.17389)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoWeaver: Accurate Long-Sequence 3D Reconstruction via Hierarchical Geometric Assembly
- 作者：Tinghao Jiang, Sheng Tang, Shengzhe Wei, Juntong Fang, Weiqi Zhang, Junsheng Zhou, Zesong Li
- 出版日期：2026-08-18T05:29:31Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.17389

### 一句话总结
GeoWeaver 提出一个由几何先验模型和测试时自适应组成的统一框架，通过分层几何组装实现精确的长序列三维重建。

### 研究问题
从 RGB 视频进行长序列三维重建时，现有前馈模型受限于内存无法联合推理长序列；分块处理虽提升可扩展性，但独立预测的分块存在尺度漂移、位姿误差和点云错位问题。

### 核心思路/方法
- 构建统一框架 GeoWeaver，包含两个核心组件：
  1. **几何先验模型（GPM）**：逐块预测深度、置信度和相机参数，作为可调整的几何先验。
  2. **测试时自适应（TTA）**：依次执行顺序初始化、全局分块级 Sim(3) 对齐、以及相机位姿/仿射深度修正/内参的由粗到细优化。
- 利用稠密对应关系提供相邻块、跨块和长距离约束。
- 采用鲁棒的 CDF 风格目标函数，联合优化加权二维重投影残差和三维一致性残差。

### 主要贡献
- 提出 GeoWeaver 统一框架，在保持局部几何精度的同时校正累积的位姿、尺度、深度和标定误差。
- 在多个长序列基准上验证了相机精度、全局一致性和点云质量的提升。
- 消融实验证实每个自适应阶段均有贡献；将相同 TTA 流程应用于不同几何先验模型均能一致改善轨迹估计，表明方法与特定 GPM 无关。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作聚焦长序列三维重建这一核心难题，提出结合几何先验与测试时自适应的通用框架，且方法不依赖特定先验模型，具有较强泛化潜力。对于从事三维重建、SLAM 和多视角几何的研究人员而言，具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Long-sequence 3D reconstruction from RGB videos requires both accurate local geometry and globally consistent camera motion. Feed-forward models provide strong depth and pose predictions, but their memory cost prevents joint inference over long sequences. Chunk-wise processing improves scalability, yet independently predicted chunks often exhibit scale drift, pose errors, and point-cloud misalignment. We present GeoWeaver, a unified framework comprising a Geometric Prior Model (GPM) and Test-Time Adaptation (TTA). The GPM predicts chunk-wise depth, confidence, and camera parameters as adjustable geometric priors. TTA then performs sequential initialization, global chunk-level Sim(3) alignment, and coarse-to-fine refinement of camera poses, affine depth corrections, and intrinsics. Dense correspondences provide adjacent, cross-chunk, and long-range constraints, while a robust CDF-style objective jointly optimizes weighted 2D reprojection and 3D consistency residuals. This design preserves local geometric accuracy while correcting accumulated pose, scale, depth, and calibration errors. Experiments across diverse long-sequence benchmarks demonstrate improved camera accuracy, global consistency, and point-cloud quality. Ablations verify the contribution of each adaptation stage, and applying the same TTA procedure to different geometric prior models consistently improves their trajectory estimates, demonstrating that GeoWeaver is not tied to a specific GPM.

</details>

#### 2026-08-17 - PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation

**Authors:** Zhiyuan Yuan, Guanying Chen, Lingteng Qiu, Ruimao Zhang, Shuguang Cui, Xiaochun Cao
**Links:** [abs](https://arxiv.org/abs/2608.16984) - [pdf](https://arxiv.org/pdf/2608.16984)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation
- 作者：Zhiyuan Yuan, Guanying Chen, Lingteng Qiu, Ruimao Zhang, Shuguang Cui, Xiaochun Cao
- 出版日期：2026-08-17T18:00:02Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.16984

### 一句话总结
PXDepth提出一种将全局上下文建模与像素级深度预测分离的单目深度估计模型，通过像素空间变换器块保持高分辨率空间表征，以在零样本基准上同时改善结构保持和深度精度。

### 研究问题
现有单目深度估计器在零样本泛化上表现良好，但常难以保持细粒度结构和物体边界，作者认为其原因在于大块ViT编码器与卷积解码器的组合中，粗粒度token化削弱了像素级线索，且上采样难以完整恢复这些信息。

### 核心思路/方法
- 将深度估计分解为两个部分：全局上下文建模和像素级深度预测。
- 使用大块ViT捕获全局场景上下文。
- 引入像素空间预测器，由“Context-Modulated Pixel Transformer”块构成，在整个深度估计过程中维持高分辨率空间表征。
- 该设计旨在保留精细结构与锐利边界，同时不牺牲全局深度一致性。

### 主要贡献
- 提出PXDepth，一种判别式单目深度模型，明确分离全局上下文建模与像素级深度预测。
- 设计像素空间预测器（含Context-Modulated Pixel Transformer块）以保持高分辨率空间信息。
- 在多样零样本基准上，PXDepth在保持局部几何结构的同时获得有竞争力的全局深度精度，且推理高效。
- 公开代码和模型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该论文针对当前单目深度估计中结构保持的明确痛点（ViT粗粒度token化与上采样信息丢失）提出新的架构分离方案，具备清晰的动机和设计创新，且涉及零样本泛化与效率，对深度估计、3D重建领域研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent monocular depth estimators achieve strong zero-shot generalization, yet often struggle to preserve fine-grained structures and object boundaries. We attribute this limitation to the prevalent combination of large-patch ViT encoders and convolutional decoders, as coarse tokenization can weaken pixel-level cues that upsampling cannot fully recover. To address this issue, we propose PXDepth, a discriminative monocular depth model that separates global context modeling from pixel-level depth prediction. Specifically, a large-patch ViT captures global scene context, while a pixel-space predictor composed of Context-Modulated Pixel Transformer blocks maintains high-resolution spatial representations throughout depth estimation. This design preserves fine structures and sharp boundaries without sacrificing global depth consistency. Across diverse zero-shot benchmarks, PXDepth combines faithful local geometry with competitive global depth accuracy while remaining efficient at inference. Our code and model are available at https://yuanzhy29.github.io/PXDepth-Page/.

</details>

#### 2026-08-17 - Binarized High-Efficiency RAW Video Restoration and Beyond

**Authors:** Tianyu Zhu, Ying Fu, Hesong Li, Gengchen Zhang, Xin Yuan, Yulun Zhang
**Links:** [abs](https://arxiv.org/abs/2608.16756) - [pdf](https://arxiv.org/pdf/2608.16756)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Binarized High-Efficiency RAW Video Restoration and Beyond
- 作者：Tianyu Zhu, Ying Fu, Hesong Li, Gengchen Zhang, Xin Yuan, Yulun Zhang
- 出版日期：2026-08-17T16:03:50Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.16756

### 一句话总结
本文提出BinRVR，一种面向RAW视频恢复的二值化神经网络框架，在降低约96%计算量和参数量的同时，仅带来约4%的性能损失，并支持多比特量化以实现精度与效率的灵活权衡。

### 研究问题
二值化神经网络（BNNs）虽能实现轻量级高效部署，但在视频场景下对时序连贯性和激活值分布的建模能力不足，导致RAW视频恢复任务中性能受限。

### 核心思路/方法
- 提出二值化信息交互模块（BIIM），以统一且高效的方式联合建模空间与时间信息。
- 开发分布感知二值化卷积（DAB-Conv），利用全精度激活值的统计信息来缓解量化误差。
- 框架支持多比特量化，可在不同硬件约束下灵活调整精度与效率。

### 主要贡献
- 首次提出针对RAW视频恢复的二值化框架BinRVR，大幅降低计算与参数量（约96%）的同时仅损失约4%性能。
- 设计BIIM模块，有效解决二值化模型在视频场景中的时序建模问题。
- 提出DAB-Conv，利用激活值分布统计信息减少量化误差。
- 支持多比特量化，提供精度-效率的灵活权衡。
- 在低光增强、去噪、去模糊和超分辨率等多个RAW视频恢复任务上验证了方法的有效性，并探索了在下游任务（目标检测、单目深度估计）上的潜力。

### 局限性
摘要未提供足够信息，例如：未提及与其他非二值化方法的具体性能对比细节、未给出不同比特量化下的具体精度/效率数值、未讨论方法的训练成本或推理速度实测数据。

### 阅读优先级
**高**
理由：该工作针对RAW视频恢复这一基础性重要任务，提出高压缩率的二值化方案，同时兼顾性能与效率，且覆盖多种恢复任务及下游应用，对于关注轻量化视频处理和模型部署的研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

RAW video restoration is fundamental to high-quality low-level perception and serves as the basis for a wide range of downstream vision applications. While binary neural networks (BNNs) enable efficient lightweight deployment for image enhancement, their deficiencies in modeling temporal coherence and activation value distributions hinder their effectiveness when applied to video scenarios. In this paper, we propose BinRVR, a binarized RAW video restoration framework that reduces computation and parameters by approximately 96% while incurring only about 4% performance degradation. Specifically, we present a Binarized Information Interaction Module (BIIM) to jointly model spatial and temporal information in an efficient and unified manner. Moreover, we develop a Distribution-Aware Binarized Convolution (DAB-Conv) that leverages the statistics of full-precision activations to mitigate quantization errors. The proposed framework further supports multi-bit quantization, enabling flexible accuracy-efficiency trade-offs across different hardware constraints. Extensive experiments demonstrate that our BinRVR achieves competitive performance compared with state-of-the-art binarized methods on RAW video restoration tasks, including low-light enhancement, denoising, deblurring, and super-resolution. We further explore the potential of our method on downstream video applications, including object detection and monocular depth estimation.

</details>

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-20 - 4DAnyone: Create Anyone in 4D from a Casual Monocular Video

**Authors:** Yudong Jin, Tao Xie, Qihang Zhang, Zehong Shen, Zhen Xu, Yujun Shen, Hujun Bao, Xiaowei Zhou, Yinghao Xu
**Links:** [abs](https://arxiv.org/abs/2608.20335) - [pdf](https://arxiv.org/pdf/2608.20335)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4DAnyone: Create Anyone in 4D from a Casual Monocular Video
- 作者：Yudong Jin, Tao Xie, Qihang Zhang, Zehong Shen, Zhen Xu, Yujun Shen, Hujun Bao, Xiaowei Zhou, Yinghao Xu
- 出版日期：2026-08-20T17:59:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.20335

### 一句话总结
本文提出4DAnyone框架，通过生成多视角一致的视频并将其提升为4D高斯泼溅，实现从随意单目视频重建4D人体，并解决了视频扩散模型在多视角扩展时的上下文瓶颈问题。

### 研究问题
如何从未标定的单目视频中重建4D人体，尤其是如何解决现有相机控制视频扩散模型在目标视角数量增加（需数十个视角以支撑4DGS重建）时无法保持多视角一致性的问题。

### 核心思路/方法
- 将问题拆解为两个耦合瓶颈：参考上下文方面（所有已生成视角的条件信息呈O(N)增长，削弱跨视角外观指导）和目标上下文方面（分组后不连续的目标视角组之间无法直接交换信息，导致全局结构漂移）。
- 设计**Reference Context Packing (RCP)**：将不断增长的参考视角压缩为固定长度的混合分辨率上下文，将参考上下文复杂度降至O(1)。
- 设计**Target Context Routing (TCR)**：在去噪过程中轮换目标视角的分组方式，高噪声步时跨组共享上下文，低噪声步时稳定细节。
- 使用自研游戏引擎构建MVGameHuman数据集，并与光舞台及野外视频数据集结合进行训练。

### 主要贡献
- 提出4DAnyone框架，实现从随意单目视频到4D人体的重建。
- 识别并形式化了视频扩散模型在多视角生成中的“有界注意力上下文”问题，指出其两个耦合瓶颈。
- 提出RCP和TCR两种互补设计，分别解决参考上下文增长和目标上下文隔离问题。
- 在DNA-Rendering和DyMVHumans上验证方法有效性，在novel-view视频质量和4DGS重建方面均优于此前方法，并展示野外泛化鲁棒性。

### 局限性
摘要未提供足够信息。摘要中未明确讨论方法的失败案例、计算成本、训练数据规模对性能的影响，也未提及在复杂遮挡、极端姿态或户外真实场景下的具体限制。

### 阅读优先级
**高**。理由：该工作在4D人体重建方向提出明确的框架和方法论贡献，针对视频扩散模型的实际瓶颈提出了工程上可行的解决方案，并在公开数据集上取得了显著提升，且附带项目页面和开源代码。对于从事神经渲染、4D重建、人体数字化等方向的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

We present 4DAnyone, a framework for reconstructing 4D humans from an uncalibrated monocular video by generating reconstruction-grade multiview-consistent videos and lifting them into 4D Gaussian Splatting (4DGS). Existing camera-controlled video diffusion models synthesize plausible novel-view videos but fail to maintain consistency when scaled to the tens of target views required for 4DGS reconstruction. We identify this failure as a bounded-attention-context problem: when target views exceed the capacity of a single DiT forward pass, they must be split into groups, exposing two coupled bottlenecks. On the reference-context side, conditioning on all previously generated views grows as $O(N)$, weakening cross-view appearance guidance. On the target-context side, disjoint groups cannot directly exchange information, causing global structural drift. 4DAnyone addresses both bottlenecks with two complementary designs: Reference Context Packing (RCP) compresses growing reference views into a fixed-length mixed-resolution context with $O(1)$ reference-context complexity, while Target Context Routing (TCR) rotates target-view groupings during denoising to share context across groups at high-noise steps and stabilize details at low-noise steps. We further build the MVGameHuman dataset using our in-house game engine and combine it with light-stage and in-the-wild video datasets for training. Experiments on DNA-Rendering and DyMVHumans show that 4DAnyone outperforms prior methods in both novel-view video quality and downstream 4DGS reconstruction, with robust in-the-wild generalization. See our project page for video results and source code: https://4danyone.github.io.

</details>

#### 2026-08-19 - GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting

**Authors:** Yechan Park, HyunJin Kim
**Links:** [abs](https://arxiv.org/abs/2608.19066) - [pdf](https://arxiv.org/pdf/2608.19066)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting
- 作者：Yechan Park, HyunJin Kim
- 出版日期：2026-08-19
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.19066

### 一句话总结
本文提出一种轻量级即插即用模块，利用3D高斯场景表示将观测视角归一化，从而在不重新训练策略的前提下增强冻结的视觉-语言-动作（VLA）策略对视角变化的鲁棒性。

### 研究问题
VLA策略在训练与部署时相机配置不一致（视角偏移）会导致性能显著下降，现有应对方法（大规模微调或生成式数据增强）计算成本高且存在灾难性遗忘风险。本文旨在解决如何在不重训练策略的条件下，高效恢复VLA策略在视角偏移下的性能损失。

### 核心思路/方法
- 将视角偏移重新建模为局部化新视角合成问题。
- 基于“局部性假设”（相机扰动相对于工作空间保持在较小有界范围内），将视角归一化转化为场景无关、策略无关的遮挡补全（disocclusion）任务。
- 实现方式：在冻结的VLA策略前接入一个仅含400万参数的3D高斯canonicalizer模块，该模块负责将观测图像进行视角规范化处理，不修改策略任何权重。

### 主要贡献
- 首次直接将3D高斯新视角合成用于VLA策略的观测空间适配。
- 提出轻量级即插即用框架GS-VLA，无需策略重训练即可提升对视角变化的鲁棒性。
- 在三个正交维度上验证了方法有效性：不同策略架构、未见任务套件、不同扰动尺度。
- 实验表明，该方法能恢复视角偏移下丢失的大部分性能，而无需修改策略权重。

### 局限性
摘要未提供足够信息，包括但不限于：具体实验设置细节、基线对比方法的完整列表、计算资源需求、在真实物理机器人上的验证情况、3D高斯模块的推理延迟或额外开销、对极端视角偏移或非局部性扰动的适应性边界等。

### 阅读优先级
**高**。理由：该论文针对VLA策略部署中实际存在的视角敏感性问题，提出一种轻量且无需重训练的解决方案，实验显示在LIBERO基准上极端情况下可恢复从约10%到接近原始90%的性能损失，具有较强实用价值；且方法新颖（首次将3D高斯渲染用于VLA观测适配），对具身智能领域的研究者和工程师均有参考意义。

</details>

<details>
<summary>Abstract</summary>

This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displacement of the camera mount can reduce the success rate on the LIBERO benchmark from about 90% to about 10% in the worst case. Prior approaches, such as large-scale fine-tuning or generative data augmentation, are computationally expensive and risk catastrophic forgetting. To address this, viewpoint shifts are reformulated as a localized novel-view synthesis problem. Under a Locality assumption, that camera perturbations remain within a small bounded region relative to the workspace, viewpoint normalization reduces to a scene- and policy-independent disocclusion task. Our work implements this idea with a 4M-parameter 3D-Gaussian canonicalizer prepended to a frozen VLA policy. Without modifying policy weights, GS-VLA improves performance across three orthogonal axes: (1) Policy architectures, (2) Unseen task suites, and (3) Perturbation scales. These results show that a lightweight visual module can recover a large fraction of the performance lost under viewpoint shift, without policy retraining.

</details>

#### 2026-08-19 - USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes

**Authors:** Li-Heng Chen, Haokai Pang, Chengye Su, Jiarun Liu, Qifeng Chen, Ziqian Ni, Jianxin Huang, Shi-Sheng Huang, Hongbo Fu, Sheng Yang
**Links:** [abs](https://arxiv.org/abs/2608.19036) - [pdf](https://arxiv.org/pdf/2608.19036)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** dynamic reconstruction, scene representation, rendering, autonomous driving, driving scene, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes
- 作者：Li-Heng Chen, Haokai Pang, Chengye Su, Jiarun Liu, Qifeng Chen, Ziqian Ni, Jianxin Huang, Shi-Sheng Huang, Hongbo Fu, Sheng Yang
- 出版日期：2026-08-19T15:29:06Z
- 分类：Neural Scene Representations & Rendering；次要分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.19036

### 一句话总结
USR-Drive提出一个统一的生成式框架，通过联合去噪3D高斯与3D边界框，在一个共享场景表示中同时恢复动态几何和实例级目标布局，实现动态重建与3D检测的相互增强。

### 研究问题
如何将自动驾驶中的动态场景重建（密集几何）与实例级感知（3D检测）从分离的任务统一为一个共享的生成式框架，使两者相互约束、互补提升，而不是像以往那样将边界框仅作为外部条件或使用解耦模块预测。

### 核心思路/方法
- 将密集3D高斯原语和稀疏3D边界框表示为两个对齐的潜在token流；
- 使用统一的多模态扩散Transformer对二者进行联合去噪；
- 提出统一位置编码（Unified Positional Encoding, UPE），将异构token对齐到共享的度量时空坐标系中；
- 两种模态互为约束：几何为框预测提供密集度量证据，框为几何提供实例级结构先验，减少时序3D几何表示中的歧义并保持空间一致性。

### 主要贡献
- 提出统一的生成式条件框架，仅需带位姿的多视角驾驶视频即可联合恢复动态几何与实例级布局；
- 将3D高斯与3D边界框建模为相互约束的状态变量而非外部条件，区别于以往解耦范式；
- 设计统一位置编码以对齐异构多模态token；
- 在nuScenes和VKitti数据集上，动态重建与3D检测均取得最优结果。

### 局限性
摘要未提供足够信息（未提及失败案例、计算开销、对极端场景的鲁棒性、训练数据需求或与SOTA的量化差距等具体局限）。

### 阅读优先级
**高**
理由：该工作直接针对自动驾驶中“重建-感知”割裂的瓶颈问题，提出统一生成式框架，且同时覆盖动态重建与3D检测两个核心任务，方法设计新颖（联合去噪+统一位置编码），并在两个公开数据集上取得SOTA，对场景表示学习、扩散模型应用和自动驾驶感知方向均有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial representation learning for autonomous driving aims to map raw visual signals into structured 3D scene representations, where object-centric bounding boxes and rendering-oriented 3D primitives (\eg, 3D Gaussians) serve as two distinct yet highly complementary levels for scene understanding. Existing methods typically treat dynamic reconstruction and instance-level perception as separate tasks, despite their shared goal of estimating the underlying 3D world state. As a result, dynamic reconstruction is under-constrained while 3D detection lacks geometric grounding. To address this gap, we propose USR-Drive, a unified conditional generative framework that, given only posed multi-view driving videos, jointly recovers dense dynamic geometry and instance-level object layouts within a shared scene representation. Specifically, USR-Drive represents dense Gaussian primitives and sparse 3D bounding boxes as two aligned latent token streams and jointly denoises them with a unified multi-modal diffusion Transformer. Unlike prior paradigms that use boxes as external conditions or predict them with detached modules, USR-Drive treats them as mutually constrained state variables with a Unified Positional Encoding (UPE) that aligns heterogeneous tokens within a shared metric spatiotemporal coordinate. Via such unified representation and generative framework, the two modalities reinforce each other: geometry supplies dense metric evidence for box prediction, while boxes provide instance-level structural priors that help preserve spatial consistency and reduce ambiguity in sequential 3D geometric representation. Our approach successfully delivers state-of-the-art results for both dynamic reconstruction and 3D detection on the nuScenes and VKitti datasets.

</details>

#### 2026-08-19 - ReX-Shot: Single-Image Rephotography via Geometry- and Camera-Grounded Generation

**Authors:** Ruiqi Zhang, Hao Zhu, Wenhao Zhang, Qi Zhang, Junqi Shi, Ming Lu, Xun Cao, Zhan Ma
**Links:** [abs](https://arxiv.org/abs/2608.18593) - [pdf](https://arxiv.org/pdf/2608.18593)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReX-Shot: Single-Image Rephotography via Geometry- and Camera-Grounded Generation
- 作者：Ruiqi Zhang, Hao Zhu, Wenhao Zhang, Qi Zhang, Junqi Shi, Ming Lu, Xun Cao, Zhan Ma
- 出版日期：2026-08-19
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.18593

### 一句话总结
ReX-Shot 是一个基于几何和相机约束的生成式框架，首次从单张图像中联合控制视角、焦距和参数化摄影效果，实现近实时的单图像重拍摄。

### 研究问题
现有单图像重拍摄方法通常分别处理视角、焦距和摄影效果，在联合控制下表现不佳：新视角合成在焦距变化时可能引入几何畸变，而超分辨率和指令引导编辑局限于2D，无法可靠地将细节恢复或外观控制扩展到新视角。

### 核心思路/方法
- 使用隐式变换的基础模型特征提供鲁棒的目标视角引导，以减少几何误差导致的投影偏差。
- 将焦距放大建模为几何引导的超分辨率问题，利用生成式细节先验恢复稀疏3D重采样中丢失的细节。
- 基于3D感知生成主干，将摄影效果控制从2D滤波提升为3D感知外观编辑，保持跨视角和跨焦距的内容一致性。

### 主要贡献
- 提出 ReX-Shot，据作者所述是首个从单张图像中统一控制视角、焦距和参数化摄影效果的框架。
- 将焦距放大重新定义为几何引导的超分辨率问题，并利用生成先验恢复细节。
- 将摄影效果控制从2D提升到3D感知层面，确保跨视角和焦距的内容一致性。
- 实验表明 ReX-Shot 在三种控制任务上均优于代表性基线，并支持近实时交互式重拍摄。

### 局限性
摘要未提供足够信息（未提及具体失败场景、计算资源需求、数据依赖或与其他方法的详细对比限制）。

### 阅读优先级
**高**。理由：该工作提出首个统一控制视角、焦距和摄影效果的单图像重拍摄框架，问题定义清晰，方法具有明确的模块化创新（几何引导超分、3D感知外观编辑），且实验声称优于基线并支持近实时交互，对生成式渲染和图像编辑方向有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-image rephotography aims to synthesize new shots of a scene from a single reference image with specified viewpoints, focal lengths, and photographic effects, which are intrinsically coupled in imaging. Existing methods typically treat these factors separately and struggle under joint control: novel-view synthesis may introduce geometric distortions under focal-length changes, while super-resolution and instruction-guided editing remain confined to 2D and cannot reliably extend detail restoration or appearance control to novel viewpoints. We attribute these limitations to imperfect single-image 3D reconstruction and the sampling limit of continuous focal-length enlargement. To reduce projection bias from geometric errors, we use implicitly transformed foundation-model features for robust target-view guidance. We further formulate focal-length enlargement as a geometry-guided super-resolution problem and exploit generative detail priors to recover details lost during sparse 3D resampling. Built on this 3D-aware generative backbone, we lift photographic-effect control from 2D filtering to 3D-aware appearance editing, preserving content consistency across viewpoints and focal lengths. These components form ReX-Shot, a geometry- and camera-grounded generative framework for single-image rephotography. To our knowledge, ReX-Shot is the first unified framework to jointly control viewpoint, focal length, and parameterized photographic effects from a single image. Experiments show that ReX-Shot outperforms representative baselines across all three controls while enabling near-real-time interactive rephotography.

</details>

#### 2026-08-18 - LumiTokens: 3D Relighting via Token-Space Lighting Transformation

**Authors:** Yiwen Chen, Matheus Gadelha, Huaizu Jiang
**Links:** [abs](https://arxiv.org/abs/2608.18215) - [pdf](https://arxiv.org/pdf/2608.18215)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LumiTokens: 3D Relighting via Token-Space Lighting Transformation
- 作者：Yiwen Chen, Matheus Gadelha, Huaizu Jiang
- 出版日期：2026-08-18
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.18215

### 一句话总结
LumiTokens 提出一种直接在潜在场景 token 上进行光照变换的 3D 重光照框架，将光照信号（环境图、点光源、面光源）统一参数化为 Plücker ray tokens，并与场景 token 通过自注意力联合处理，从而实现无需显式物理分解的多视图一致重光照和渐进式光照编辑。

### 研究问题
如何在不进行显式材质分解或无物理渲染方程的情况下，直接在潜在场景表示中对 3D 场景进行重光照，并支持多种光照类型和渐进式、可组合的光照编辑。

### 核心思路/方法
- 利用无固定物理语义的潜在场景 token 作为重光照操作空间，将 3D 重光照转化为对潜在场景 token 的直接变换。
- 设计一个 Scene Token Editor，将场景 token 与光照 ray token 通过自注意力联合处理，输出更新后的 token，再解码为多视图一致的 3D 重光照图像。
- 所有光照类型（环境图、点光源、面光源）统一参数化为 Plücker ray tokens，该表示不携带显式空间结构，但支持原生 3D 用户交互。
- 支持渐进式重光照：编辑器的输出与输入处于同一潜在空间，用户可逐光源逐步叠加光照效果，每次编辑在 token 空间中组合。

### 主要贡献
- 提出一种新的 3D 重光照范式：直接在潜在场景 token 上进行光照变换，无需显式 3D 表示、渲染方程或物理分解。
- 引入 Scene Token Editor，通过自注意力联合建模场景 token 与光照 ray token，实现多视图一致的重新光照。
- 将多种光照类型统一参数化为 Plücker ray tokens，提供统一的用户交互接口，支持原生 3D 光照操作。
- 利用 token 空间的闭合性，实现渐进式、可组合的光照编辑，用户可逐光源增量构建光照效果。
- 实验表明该方法在重光照质量上达到与现有方法相当或更优的水平，并支持渐进式、可组合的光照编辑。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法提出了一种全新的 3D 重光照范式，绕开传统显式物理分解，直接在潜在 token 空间中进行光照变换，概念上具有较高创新性；同时支持多类型光照统一表示与渐进式编辑，对交互式 3D 内容创作和光照编辑应用有潜在价值。摘要中显示实验质量与现有方法相当或更优，但未提供具体对比细节，建议阅读原文以评估实际效果。

</details>

<details>
<summary>Abstract</summary>

Existing 3D relighting methods operate through either explicit material decomposition, diffusion-based view-space generation, or a combination of both, requiring full recomputation for each new lighting condition. We observe that recent latent scene representations, which encode multi-view images into a set of compact tokens with no fixed physical semantics, open up a novel design space for relighting. We present LumiTokens, a framework that formulates 3D relighting as a direct transformation on latent scene tokens, without explicit 3D representations, rendering equations, or physics-based decomposition. Our model introduces a Scene Token Editor that processes scene tokens jointly with light-ray tokens through self-attention, producing updated tokens that can be decoded into multi-view-consistent relit images. To support diverse lighting types through a unified interface, all lighting signals, including environment maps, point lights, and area lights, are parameterized as Plucker ray tokens, enabling native 3D user interaction with a representation that carries no explicit spatial structure. Crucially, this design supports progressive relighting: because the editor's output remains in the same latent space as its input, a user can incrementally build up illumination one light source at a time, with each edit composing in token space. Experiments demonstrate that LumiTokens achieves comparable or superior relighting quality to other methods and supports progressive, composable lighting edits. Project page: https://neu-vi.github.io/LumiTokens/

</details>

#### 2026-08-18 - GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation

**Authors:** Ming Qian, Zijian Wang, Minchao Sun, Jincheng Xiong, Hang Zhang, Mu Xu, Chi Wang, Baoquan Chen
**Links:** [abs](https://arxiv.org/abs/2608.17988) - [pdf](https://arxiv.org/pdf/2608.17988)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation
- 作者：Ming Qian, Zijian Wang, Minchao Sun, Jincheng Xiong, Hang Zhang, Mu Xu, Chi Wang, Baoquan Chen
- 出版日期：2026-08-18
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.17988

### 一句话总结
GS-Voxel 提出了一种无需逐场景拟合的稀疏体素化结构化潜空间框架，用于大规模航拍 3DGS 场景的生成，潜变量容量随占用体素数增长。

### 研究问题
如何为大规模、无序且基元数量不固定的预优化 3DGS 重建结果，构建可扩展的结构化潜表示，以支持高效的场景生成。

### 核心思路/方法
- 将兼容的预优化 3DGS 重建结果确定性地转换为稀疏激活体素，无需额外的逐场景优化，同时保留基元的亚体素位置和渲染属性。
- 设计一个面向 3DGS 的因子化 VAE，分别编码体素几何和局部高斯属性，形成稀疏 3D 潜变量；潜变量大小随占用体素数增长，而非受固定全局基元数限制。
- 在该潜空间上训练以图像为条件的流模型，用于生成航拍 3DGS 场景。
- 支持重叠感知的平铺推理，使得生成可扩展到单个训练裁剪区域之外，并基于卫星视角图像进行条件生成。

### 主要贡献
- 提出拟合自由的稀疏体素化框架 GS-Voxel，将预优化 3DGS 重建转换为结构化的稀疏潜表示。
- 证明该潜表示容量随占用体素数增长，适用于大规模场景生成。
- 实现了基于卫星图像条件的大面积航拍 3DGS 场景生成，支持平铺式扩展推理。

### 局限性
摘要未提供足够信息，未明确讨论方法的局限性（如体素化精度损失、推理效率、对输入重建质量的依赖等）。

### 阅读优先级
**中**。理由：该工作聚焦于大规模 3DGS 生成的表示与扩展性问题，方法上有一定创新（拟合自由 + 稀疏结构化），但摘要未提供定量结果或与现有方法的直接对比，适合相关方向研究者阅读，非该领域者优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Many scalable latent 3D generators operate on structured tensors, whereas pre-optimized 3D Gaussian Splatting (3DGS) reconstructions are unordered, spatially irregular, and vary widely in primitive count. We present GS-Voxel, a fitting-free structured latent framework, and evaluate it for large-scale aerial 3D Gaussian scene generation. GS-Voxel deterministically converts a compatible pre-optimized 3DGS reconstruction into sparse active voxels without additional per-scene optimization, retaining the sub-voxel positions and rendering attributes of the selected primitives. A GS-specific factorized VAE then separately encodes voxel geometry and local Gaussian attributes into sparse 3D latents whose size grows with the number of occupied voxels rather than being limited by a fixed scene-wide primitive count. We train image-conditioned flow models in the GS-Voxel latent space to generate aerial 3DGS scenes. A key application enabled by GS-Voxel is large-area scene generation: overlap-aware tiled inference extends synthesis beyond a single training crop conditioned on satellite-view images. Our results show that GS-Voxel provides structured latents for pre-optimized aerial 3DGS reconstructions, with latent capacity that grows with the number of occupied voxels.

</details>

#### 2026-08-18 - MetaSapiens v2: Advancing Real-Time Foveated Neural Rendering via Foveation-Aware Pruning and Stereo Warping

**Authors:** Weikai Lin, Yu Feng
**Links:** [abs](https://arxiv.org/abs/2608.17969) - [pdf](https://arxiv.org/pdf/2608.17969)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural rendering, rendering, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MetaSapiens v2: Advancing Real-Time Foveated Neural Rendering via Foveation-Aware Pruning and Stereo Warping
- 作者：Weikai Lin, Yu Feng
- 出版日期：2026-08-18
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.17969

### 一句话总结
本文提出MetaSapiens v2，一种面向VR/AR设备的点基神经渲染（PBNR）系统，通过结合效率感知剪枝、注视点渲染、选择性立体扭曲和专用加速器设计，在保持人类视觉质量的同时实现实时渲染，并获得数量级的加速。

### 研究问题
如何在VR/AR设备上实现实时的高质量点基神经渲染（PBNR），以克服现有PBNR模型在实时性方面的不足。

### 核心思路/方法
MetaSapiens v2整合了四项关键技术：
1. **效率感知剪枝**：优化渲染速度的剪枝技术。
2. **注视点渲染（FR）**：利用人眼外周视觉敏锐度较低的特性，在PBNR中引入高效的注视点渲染原语，放松外周区域的渲染质量以提升速度。
3. **选择性立体扭曲**：利用双眼视觉之间的冗余，通过选择性扭曲方法降低双目渲染的计算开销。
4. **加速器设计**：针对双目注视点渲染的专用加速器，解决基于FR的PBNR中存在的负载不均衡问题，并支持高效的双目渲染扭曲操作。

### 主要贡献
- 提出了一个完整、高效的PBNR系统，实现VR/AR设备上的实时神经渲染。
- 首次将效率感知剪枝与注视点渲染结合，适配PBNR场景。
- 提出选择性立体扭曲方法，利用双眼冗余进一步削减计算量。
- 设计了专用加速器架构，解决FR-PBNR的负载不均衡问题并支持扭曲操作。
- 实验表明，相较于现有PBNR模型，MetaSapiens v2在保持视觉质量的同时达到数量级的速度提升。

### 局限性
摘要未提供足够信息，未说明具体的数据集、基线对比细节、硬件平台、视觉质量评估指标、剪枝率与质量权衡的定量结果，以及加速器实现的能耗或面积开销。

### 阅读优先级
**中**。理由：该工作面向AR/VR实时渲染，有明确的工程和系统设计贡献（含硬件加速器），适合对神经渲染效率优化和端侧部署感兴趣的读者；但摘要未提供充分的实验细节和对比基准，若需要严格评估方法有效性，需阅读全文。若读者关注点基渲染或注视点渲染算法本身，优先级可适度提高。

</details>

<details>
<summary>Abstract</summary>

Point-Based Neural Rendering (PBNR) is emerging as a promising class of rendering techniques, which are permeating all aspects of society, driven by a growing demand for real-time, photorealistic rendering in AR/VR and digital twins. However, achieving real-time PBNR on VR/AR devices is challenging. This paper proposes MetaSapiens v2, a PBNR system that delivers real-time neural rendering on VR/AR devices while maintaining human visual quality. MetaSapiens v2 combines four techniques. First, we present an efficiency-aware pruning technique to optimize rendering speed. Second, we introduce a Foveated Rendering (FR) method with an efficient primitive for PBNR, leveraging humans' low visual acuity in peripheral regions to relax rendering quality and improve rendering speed. Third, we leverage the redundancy between the two eyes and propose a selective warping method to further reduce the computation overhead in AR/VR binocular rendering. Finally, we propose an accelerator design for binocular FR, addressing the load imbalance issue in (FR-based) PBNR and supporting warping for efficient binocular rendering. Our evaluation shows that MetaSapiens v2 achieves an order of magnitude speedup over existing PBNR models while maintaining the visual quality.

</details>

#### 2026-08-18 - GenRec: Knowing Where to Reconstruct and Where to Generate

**Authors:** Ata Çelen, Jaewoo Jung, Federico Tombari, Marc Pollefeys, Sunghwan Hong, Michael Niemeyer, Daniel Barath
**Links:** [abs](https://arxiv.org/abs/2608.17832) - [pdf](https://arxiv.org/pdf/2608.17832)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** monocular depth, NeRF, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GenRec: Knowing Where to Reconstruct and Where to Generate
- 作者：Ata Çelen, Jaewoo Jung, Federico Tombari, Marc Pollefeys, Sunghwan Hong, Michael Niemeyer, Daniel Barath
- 出版日期：2026-08-18T14:31:19Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.17832

### 一句话总结
GenRec 提出一种多视角流匹配模型，通过观测掩码显式区分“重建”与“生成”区域，在观测像素上保持几何保真度，在未观测区域保留生成多样性，从而同时提升重建精度与感知质量。

### 研究问题
现有生成式新视角合成方法对所有像素施加统一的损失，混淆了“可唯一重建的观测区域”与“存在多种合理补全的未观测区域”，导致几何保真与生成幻觉之间的界限模糊。如何将重建—生成的划分直接融入模型架构、监督信号与梯度流，是本工作的核心问题。

### 核心思路/方法
- 构建一个多视角流匹配模型，将重建与生成的区分内置于架构、监督和梯度流中。
- 利用由源相机和单目深度估计器导出的观测掩码，引导流匹配主干联合去噪所有目标视角的 RGB 与场景坐标图。
- 在像素空间增加细化阶段，用于恢复观测像素上的高频细节。
- 同一掩码同时控制监督信号，避免回归损失污染生成先验。

### 主要贡献
- 首次将重建—生成划分显式构建到模型架构、监督与梯度流中，而非仅依赖统一损失。
- 在 RealEstate10K、DL3DV-10K 和 Mip-NeRF 360 上，单视角外推与双视角插值设置下，观测区域的重建保真度达到最佳，同时未观测区域的感知质量超越纯生成基线。
- 证明通过掩码门控监督可以同时优化两个互为冲突的目标（重建与生成）而不互相干扰。

### 局限性
摘要未提供足够信息，无法获知该方法在极端稀疏视角、动态场景、计算开销或失败案例等方面的具体限制。

### 阅读优先级
**高**。理由：该工作针对生成式新视角合成中重建与生成冲突这一核心问题，提出了架构级解决方案，并在多个基准数据集上同时改善重建与感知指标，且发表于 2026 年，方法新颖、实验广泛，值得深入阅读。

</details>

<details>
<summary>Abstract</summary>

Generative novel view synthesis from sparse input images is rarely all reconstruction or all generation: pixels visible in some source view have a unique correct value modulated only by view-dependent shading, while pixels in disocclusions or beyond the captured volume admit a distribution of plausible completions. Existing generative novel-view-synthesis methods conflate these regimes under a single uniform loss, blurring the line between geometric fidelity and creative hallucinations even when scene geometry is injected through warped point clouds or projected depth. We introduce GenRec, a multi-view flow matching model that builds the reconstruction--generation split directly into its architecture, supervision, and gradient flow. Guided by an observation mask derived from the source cameras and a monocular depth estimator, a flow matching backbone jointly denoises RGB and scene-coordinate maps across all target views, while a pixel-space refinement stage restores high-frequency detail on observed pixels; the same mask gates supervision so regression signals do not contaminate the generative prior. Across RealEstate10K, DL3DV-10K, and Mip-NeRF~360, in both single-view extrapolation and two-view interpolation, GenRec attains the best reconstruction fidelity in observed regions while also surpassing purely generative baselines on perceptual quality in unobserved ones, showing the effectiveness of our approach.

</details>

#### 2026-08-18 - Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds

**Authors:** Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl
**Links:** [abs](https://arxiv.org/abs/2608.17682) - [pdf](https://arxiv.org/pdf/2608.17682)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds
- 作者：Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl
- 出版日期：2026-08-18
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.17682

### 一句话总结
本文提出VoroTracing，一种可微Voronoi光线追踪渲染器，通过场景表示、优化与GPU执行的协同设计，在保持重建质量的同时超越光栅化方法的速度，并自然支持多种非针孔相机效果。

### 研究问题
如何在保持光线追踪表达灵活性的前提下，使其渲染速度超越基于光栅化的实时新视角合成方法？具体而言，作者分析了可微Voronoi光线追踪中影响吞吐量的关键因素，并探索如何系统性降低这些成本。

### 核心思路/方法
1. **瓶颈分析**：识别出遍历长度、每单元计算量（per-cell work）和内存局部性为决定吞吐量的三个主要因素。
2. **协同设计**：VoroTracing同时优化场景表示、优化过程和GPU执行：
   - 紧凑的八面体外观纹理减少内存流量；
   - 表面集中的不透明度分布促进光线及早终止；
   - 固定预算的表示无需剪枝或稠密化；
   - GPU实现针对连贯遍历（coherent traversal）设计。
3. **效果支持**：通过光线生成和采样直接支持鱼眼、卷帘快门、运动模糊和景深效果，无需专门的光栅化扩展。

### 主要贡献
- 提出VoroTracing，首个在速度上超越光栅化方法（3D Gaussian Splatting）的基于光线追踪的可微渲染器，在RTX 5090上达到623 FPS，比最快的既有光线追踪方法快3.2倍，比3DGS快2.8倍，同时保持有竞争力的重建质量（在Mip-NeRF 360上评估）。
- 提供了对可微Voronoi光线追踪吞吐量决定性因素的清晰分析。
- 展示了光线追踪的灵活性（多种非针孔效果）可以与实时吞吐量同时实现。
- 开源代码。

### 局限性
摘要未提供足够信息：未提及方法的显式局限性（如场景规模限制、特定效果下的性能下降、与某些重建质量指标的绝对差距等）。

### 阅读优先级
**高**
理由：该方法在渲染领域具有突破性意义——首次展示了基于光线追踪的可微渲染在速度上超越当前主流的光栅化方法（3DGS），同时保留了光线追踪的效果灵活性。对于神经渲染、实时图形学和非针孔成像相关研究者，该工作可能改变技术路线选择。发表时间为2026年，属于较新工作，建议优先阅读。

</details>

<details>
<summary>Abstract</summary>

Real-time novel view synthesis is dominated by rasterized explicit primitives. These projection-based pipelines provide high throughput but require specialized extensions for non-pinhole effects such as distortion, rolling shutter, and depth of field. Ray-based rendering expresses these effects naturally but is generally assumed too slow for competitive real-time rendering. We analyze the factors governing throughput in differentiable Voronoi ray tracing and identify traversal length, per-cell work, and memory locality as principal determinants. Guided by this, we introduce VoroTracing, which co-designs the scene representation, optimization, and GPU execution to reduce these costs. Compact octahedral appearance textures reduce memory traffic, while surface-concentrated opacity promotes early termination. The fixed-budget representation is optimized without pruning or densification and rendered with a GPU implementation designed for coherent traversal. On Mip-NeRF 360, VoroTracing renders at 623 FPS on an RTX 5090, providing $3.2\times$ the throughput of the fastest prior ray-based method and $2.8\times$ that of 3D Gaussian Splatting, while maintaining competitive reconstruction quality. Our renderer supports fisheye, rolling-shutter, motion-blur, and depth-of-field effects through ray generation and sampling, requiring no specialized rasterization. These results show that real-time throughput can be achieved with the flexibility of ray-based rendering. We release our source code, see https://research.zenseact.com/publications/vorotracing

</details>

#### 2026-08-18 - GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting

**Authors:** Qijian Tian, Zimeng Wu, Xuhong Wang, Lizhuang Ma, Xin Tan
**Links:** [abs](https://arxiv.org/abs/2608.17535) - [pdf](https://arxiv.org/pdf/2608.17535)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting
- 作者：Qijian Tian, Zimeng Wu, Xuhong Wang, Lizhuang Ma, Xin Tan
- 出版日期：2026-08-18
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.17535

### 一句话总结
本文提出GroupForward模型，通过实例分组的前馈3D高斯泼溅重建可引用的3D场景，并配套引用场景推理框架（RSRF）实现复杂3D指代分割。

### 研究问题
现有前馈语义3D高斯泼溅方法缺乏显式实例判别能力，主要支持基于类别或短语的语义查询，无法完成复杂的指代性场景推理（如根据自然语言指代表达定位特定实例）。

### 核心思路/方法
- 提出GroupForward，一种实例分组的前馈高斯泼溅模型，能从稀疏、无位姿、无标定的多视图图像中重建几何、外观、实例结构和语义。
- 不同于现有方法为每个高斯附加高维语义特征，GroupForward学习紧凑的实例嵌入，将高斯分组为跨视图一致的3D实例，将前馈语义3DGS从逐高斯语义特征渲染重构为实例级语义聚合与传播。
- 基于实例分组，进一步提出引用场景推理框架（RSRF）：构建实例分组的3D场景图，对给定指代表达检索候选实例，再由视觉-语言模型基于结构化实例证据和多视图观测进行推理，从候选中识别所指实例。

### 主要贡献
- 提出实例分组的前馈3D高斯泼溅模型，实现跨视图一致的3D实例重建与语义聚合。
- 提出引用场景推理框架（RSRF），将语言交互从简单语义查询扩展至复杂指代场景推理。
- 在语义重建和指代推理实验上验证了实例分组重建与推理框架的有效性（摘要提及实验结果，但未提供具体数值）。

### 局限性
摘要未提供足够信息（未讨论模型在遮挡、实例数量、计算开销、泛化能力等方面的限制）。

### 阅读优先级
**中**。理由：该工作针对前馈语义3DGS的实例级判别和指代推理这一具体问题，属于领域内细化改进，适合对3D场景理解、高斯泼溅与多模态推理交叉方向感兴趣的读者；但摘要未提供量化实验结果，需进一步阅读正文评估其实际性能与适用场景。

</details>

<details>
<summary>Abstract</summary>

Simultaneously reconstructing and understanding 3D environments is essential for embodied agents. Toward this goal, feed-forward semantic 3D Gaussian Splatting (3DGS) efficiently constructs semantic scene representations from sparse multi-view observations. However, existing methods lack explicit instance discrimination and mainly support category- or phrase-based semantic queries. To this end, we propose GroupForward, an instance-grouped feed-forward Gaussian splatting model that reconstructs geometry, appearance, instance structure, and semantics from sparse, unposed, and uncalibrated multi-view images. Unlike existing methods that attach high-dimensional semantic features to each Gaussian, GroupForward learns compact instance embeddings that group Gaussians into cross-view consistent 3D instances, reformulating feed-forward semantic 3DGS from per-Gaussian semantic feature rendering to instance-level semantic aggregation and propagation. Building on these instance groups, we further propose a Referential Scene Reasoning Framework (RSRF) for complex 3D referring segmentation. RSRF constructs an instance-grouped 3D scene graph and retrieves candidate instances for a given referring expression. A vision-language model then reasons over structured instance evidence and multi-view observations to identify the referred instance among the candidates. RSRF thereby extends language interaction from simple semantic querying to complex referential scene reasoning. Experiments on semantic reconstruction and referential reasoning demonstrate the effectiveness of our instance-grouped reconstruction and reasoning framework.

</details>

#### 2026-08-18 - NGS-Marker: Robust Native Watermarking for 3D Gaussian Splatting

**Authors:** Hao Qin, Yukai Sun, Luyuan Chen, Mengxu Lu, Feng Zhang, Ming Kong, Zhenhong Du, Qiang Zhu
**Links:** [abs](https://arxiv.org/abs/2608.17447) - [pdf](https://arxiv.org/pdf/2608.17447)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NGS-Marker: Robust Native Watermarking for 3D Gaussian Splatting
- 作者：Hao Qin, Yukai Sun, Luyuan Chen, Mengxu Lu, Feng Zhang, Ming Kong, Zhenhong Du, Qiang Zhu
- 出版日期：2026-08-18T07:28:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.17447

### 一句话总结
NGS-Marker 是一种面向 3D 高斯泼溅（3DGS）的原生水印框架，通过渐进式注入策略实现全场景覆盖，从而抵御局部侵权（partial infringement）攻击。

### 研究问题
现有 3DGS 水印技术主要依赖预训练解码器保护渲染图像，但无法有效保护底层 3D 高斯基元本身，尤其当攻击者仅提取和重用部分高斯子集时（即局部侵权），现有方法失效。NGS-Marker 旨在解决这一版权保护漏洞。

### 核心思路/方法
- 提出原生水印框架 NGS-Marker，将水印注入器与消息解码器联合训练；
- 采用基于梯度的渐进式注入策略，确保水印覆盖整个场景；
- 使所有权解码可从任意局部区域稳健进行；
- 扩展了混合保护模式（原生水印与间接水印结合）以及多模态水印支持。

### 主要贡献
- 提出首个面向 3DGS 的原生水印框架，直接保护 3D 高斯基元而非仅渲染图像；
- 渐进式注入策略保证全场景覆盖，实现对局部侵权的鲁棒防御；
- 提供混合保护与多模态水印扩展，增强了实际部署中的灵活性。

### 局限性
摘要未提供足够信息来评估局限性，例如对非局部侵权攻击的鲁棒性、水印对渲染质量的影响、计算开销或实验对比细节等均未在摘要中说明。

### 阅读优先级
**高**

理由：3DGS 是当前神经渲染领域的热门方向，版权保护是实际部署中的关键问题。该文针对现有方法无法防御局部侵权的明确缺陷提出了新的原生水印方案，具有较强的问题针对性和应用价值，值得优先关注。

</details>

<details>
<summary>Abstract</summary>

With the rapid development and adoption of 3D Gaussian Splatting (3DGS), the need for effective copyright protection has become increasingly critical. Existing watermarking techniques for 3DGS mainly focus on protecting rendered images via pre-trained decoders, leaving the underlying 3D Gaussian primitives vulnerable to misuse. In particular, they are ineffective against Partial Infringement, where an adversary extracts and reuses only a subset of Gaussians. In this paper, we propose NGS-Marker, a novel native watermarking framework for 3DGS. It integrates a jointly trained watermark injector and message decoder, and employs a gradientbased progressive injection strategy to ensure full-scene coverage. This enables robust ownership decoding from any local region. We further extend NGS-Marker with hybrid protection (combining native and indirect watermarks) and support for multimodal watermarking. Extensive experiments demonstrate that NGS-Marker effectively defends against partial infringement while offering practical flexibility for real-world deployment.

</details>

#### 2026-08-18 - SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering

**Authors:** Gen Li, Shu Han, Yun Xi Qiao, Hua Chen, Xuyang Dai, Bohan Li, Hao Zhao, Chaojian Li
**Links:** [abs](https://arxiv.org/abs/2608.17420) - [pdf](https://arxiv.org/pdf/2608.17420)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving, driving scene, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering
- 作者：Gen Li, Shu Han, Yun Xi Qiao, Hua Chen, Xuyang Dai, Bohan Li, Hao Zhao, Chaojian Li
- 出版日期：2026-08-18
- 分类：Neural Scene Representations & Rendering（次要分类：Embodied / Robotics / AR Applications）
- 链接：https://arxiv.org/abs/2608.17420

### 一句话总结
SPVC 提出一种基于结构化与全景式视频修复的统一框架，用于跨数据集驾驶场景渲染中的伪影消除与前景-背景对齐。

### 研究问题
驾驶场景重建与渲染（尤其是基于 3D Gaussian Splatting）在外推轨迹或场景编辑下容易出现模糊结构、时间闪烁以及前景-背景错位等问题，现有修复方法通常局限于特定设置（如图像级新视角修复或物体编辑校正），缺乏统一且跨数据集适用的修复方案。

### 核心思路/方法
- 提出四个设计原则：
  1. **结构化修复**：显式使用相机位姿、3D 边界框和高精地图等空间条件引导修复，减少不可控幻觉。
  2. **全景式修复**：同时修正背景渲染伪影（如道路、建筑、车道线畸变）和前景车辆编辑引入的外观不一致伪影。
  3. **视频级修复**：在驾驶序列上进行修复而非孤立帧，利用时间线索辅助伪影校正。
  4. **跨数据集修复**：单一共享网络在多个驾驶数据集上训练和应用，避免数据集/场景特定的修复器。
- 具体实现：通过模拟欠约束 3DGS 渲染和前景车辆插入伪影，构建配对退化-干净训练数据；训练一个两阶段可控视频扩散模型，先处理视频级外观，再用结构化控制细化场景布局。

### 主要贡献
- 提出首个面向跨数据集驾驶场景渲染的结构化与全景视频修复框架，整合空间条件、全景伪影修复、时间一致性和跨数据集泛化。
- 设计了配对数据构造策略，模拟真实渲染劣化与前景编辑伪影，用于训练统一修复模型。
- 采用两阶段可控视频扩散模型，分别处理外观修复与结构化布局细化，提升修复可控性。

### 局限性
摘要未提供实验评估细节、定量指标、与基线方法对比结果、具体性能边界或失败模式分析，因此无法判断该方法在真实部署中的具体局限；摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对自动驾驶仿真中 3DGS 渲染的核心痛点（外推轨迹下的伪影与编辑不一致），提出统一修复框架并强调跨数据集泛化，对神经场景表示和驾驶仿真方向具有较强实用价值；且方法设计（结构化+全景式+视频级+跨数据集）具备系统性，适合关注驾驶渲染和扩散修复的读者精读。

</details>

<details>
<summary>Abstract</summary>

Driving scene reconstruction and rendering, especially with 3D Gaussian Splatting, has become an important component of autonomous driving simulation. However, rendered views often degrade under extrapolated ego trajectories and scene edits, producing blurry structures, temporal flicker, and foreground-background misalignment. Existing refinement methods are commonly designed for a specific setting, such as image-level novel-view repair or object-editing correction. In this paper, we introduce SPVC, a structured and panoptic video fixing framework for cross-dataset driving scene rendering. The name summarizes four design principles. (1) Structured fixing denotes the use of explicit spatial conditions, including camera pose, 3D bounding boxes, and HD maps, to guide the repair process and reduce uncontrolled hallucination. (2) Panoptic fixing refers to correcting both background rendering artifacts, such as distorted roads, buildings, and lanes, and foreground vehicle artifacts introduced by scene editing, such as inconsistent object appearance. (3) Video fixing means that the model operates on driving sequences rather than isolated frames, allowing temporal cues to be used during artifact correction. (4) Cross-dataset fixing means that a single shared network is trained and applied across multiple driving datasets, reducing the need for dataset-specific or scene-specific fixers. Concretely, we construct paired degraded-clean training data by simulating under-constrained 3DGS rendering and foreground vehicle insertion artifacts, and train a two-stage controllable video diffusion model that first addresses video-level appearance and then refines scene layout with structured controls.

</details>

#### 2026-08-18 - Scanline-Aware Animatable Gaussian Avatars from Rolling-Shutter Videos

**Authors:** Youxiang Wang
**Links:** [abs](https://arxiv.org/abs/2608.17314) - [pdf](https://arxiv.org/pdf/2608.17314)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Scanline-Aware Animatable Gaussian Avatars from Rolling-Shutter Videos
- 作者：Youxiang Wang
- 出版日期：2026-08-18
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.17314

### 一句话总结
RS-Avatar 通过将渲染流程中的模糊算子替换为按扫描线合成的卷帘快门模型，直接从卷帘快门视频重建清晰、无畸变且可动画化的 3D 高斯人体化身。

### 研究问题
现有可动画人体化身重建方法假设每帧所有像素在同一瞬间观测到身体运动，但卷帘快门传感器逐行曝光，导致单帧内不同扫描线对应不同姿态，且多相机各自读取时序不一，破坏了重建所需的多视角一致性，从而在重建结果中引入畸变（如剪切和抖动）。

### 核心思路/方法
核心思路极为简洁：利用可动画化身已有的亚帧级渲染能力——该渲染器能在多个子帧时刻生成身体图像——将传统的模糊模型（对子帧渲染结果做平均）替换为卷帘快门模型（按扫描线对各子帧渲染结果进行拼接合成）。仅改变这一合成算子，即可直接从未经矫正的卷帘快门视频中重建清晰且可动画化的高斯化身。

### 主要贡献
1. 提出了 RS-Avatar，一个能直接从卷帘快门视频重建清晰、无畸变、可动画化的 3D 高斯化身的框架。
2. 阐明了核心洞见：亚帧渲染机制可以复用，但合成算子必须从“平均”改为“按扫描线拼接”。
3. 构建了 RS-ZJU 基准（基于 ZJU-MoCap），并在每个测试对象上证实了所提方法优于将视频当作瞬时帧进行训练的基线。
4. 对比实验显示，基于相同亚帧机制的模糊模型无法迁移到卷帘快门场景，性能甚至低于忽略快门效应的基线，说明合成算子的选择至关重要。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作针对卷帘快门视频下可动画人体化身重建这一具体实际问题，提出了一个极简且有效的解决方案，并提供了对比实验验证。对于从事人体重建、神经渲染或卷帘快门成像相关研究的读者有较高参考价值；但若不在上述领域，其影响力相对有限。由于摘要未披露训练数据量、推理速度、与现有最先进方法的定量对比等细节，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Animatable human avatars are routinely reconstructed from multi-view video under a silent assumption: that every pixel of a frame observes the same instant of the body's motion. Rolling-shutter (RS) sensors expose image rows sequentially, so within one frame the head and the feet of a moving person are separated by tens of milliseconds of articulated motion, and every scanline sees a different pose. Feeding such video to a state-of-the-art avatar bakes the distortion into the canonical representation, where it survives as shear and wobble under novel views and novel poses. Worse, every camera in a rig follows its own readout schedule, so the multi-view consistency that drives the reconstruction is violated even when the geometry is correct. We present RS-Avatar, which reconstructs a sharp, undistorted, animatable 3D Gaussian avatar directly from RS video. The formulation is minimal: a motion-aware avatar already renders the body at several sub-frame instants, and where a blur model averages those renderings, a rolling-shutter model composites them scanline by scanline. Changing that operator is the only modification required. On RS-ZJU, a benchmark we build from ZJU-MoCap, this improves novel-view synthesis over training as if the frames were instantaneous, on every subject. A motion-aware blur model built on the same sub-frame machinery does not transfer, and in fact falls below the shutter-oblivious baseline: the machinery is reusable, the operator is not.

</details>

#### 2026-08-18 - 3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation

**Authors:** Laurent Vit, Oliver Batchelor, Richard Green
**Links:** [abs](https://arxiv.org/abs/2608.17298) - [pdf](https://arxiv.org/pdf/2608.17298)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation
- 作者：Laurent Vit, Oliver Batchelor, Richard Green
- 出版日期：2026-08-18T02:50:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.17298

### 一句话总结
本文提出3DGART训练框架，通过将光线追踪高斯渲染的反向传播从像素视角重组为基元视角，显著加速了训练过程，使全光线追踪高斯训练在速度上可与光栅化管线竞争。

### 研究问题
高斯光线追踪虽能解决3D高斯溅射中基于光栅化的屏幕空间近似带来的视角排序和次级光线效果（反射、折射、阴影）问题，但其训练成本高昂，主要瓶颈在于像素中心的反向传播中大量线程并发累积梯度到同一基元参数，造成严重原子争用和线程串行化。因此，如何加速高斯光线追踪的训练过程是本文研究的核心问题。

### 核心思路/方法
核心思想是将反向传播从“以像素为中心”重新组织为“以基元为中心”。具体方法包括：利用保守的透视校正屏幕空间边界，构建紧凑的中间缓冲区和“瓦片-基元”映射，使每个线程在瓦片内累积一个基元覆盖像素的贡献。这使梯度计算从竞争密集的“散射”操作转变为结构化的“聚集”过程，从而消除原子争用和线程串行化。

### 主要贡献
- 识别出高斯光线追踪训练的主要瓶颈并非光线遍历本身，而是像素中心反向传播中的原子争用和线程串行化。
- 提出3DGART框架，通过基元中心的反向传播重组，将梯度计算从散射式转变为聚集式，有效提升训练效率。
- 在Mip-NeRF 360数据集上，相比逐像素基线获得约3-3.5倍的原始训练加速，相比3DGRT获得约4倍加速，同时质量得到提升。
- 使全光线追踪高斯训练变得实用，运行时间可与光栅化管线竞争，同时保留光线追踪的优势。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对高斯光线追踪训练效率这一实际瓶颈，提出了一种明确的加速机制，并在多个基线比较中显示出显著加速和质量提升。研究结果使光线追踪高斯渲染在实用性与光栅化管线竞争，对神经场景表征与渲染领域具有较大的潜在应用价值，适合优先阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has made Gaussian primitives a highly efficient representation for real-time novel view synthesis, but its rasterisation-based formulation relies on screen-space approximations that limit accurate view-dependent ordering and the integration of secondary ray effects such as reflections, refractions, and shadows. Gaussian ray tracing addresses these limitations by evaluating explicit ray-primitive intersections, yet it remains costly to train. We observe that the main bottleneck is not ray traversal alone, but the pixel-centric backward propagation, where many threads concurrently accumulate gradients into the same primitive parameters, causing severe atomic contention and thread serialisation. We present 3DGART, a practical training framework for ray-traced Gaussian rendering. Our key idea is to reorganise backward propagation around primitives rather than pixels. Using conservative perspective-correct screen-space bounds, we build a compact intermediate buffer and a tile-primitive mapping that allows each thread to accumulate the contribution of one primitive over its covered pixels within a tile. This transforms gradient computation from a contention-heavy scatter operation into a structured gather-like process. On Mip-NeRF 360, 3DGART achieves an $\approx 3-3.5\times$ raw training speedup over per-pixel baseline and $\approx4 \times$ over 3DGRT on Mip-NeRF 360 while improving quality. More importantly, 3DGART makes fully ray-traced Gaussian training practical, reaching runtimes competitive with rasterisation-based pipelines while preserving benefits of ray tracing.

</details>

#### 2026-08-17 - SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis

**Authors:** Yejun Zhang, Zihan Wang, Xu Ji, Yihao Wang, Yuxin Hou, Junyuan Fang, Juho-Matti Kilpeläinen, Arno Solin, Hamed Rezazadegan Tavakoli, Esa Rahtu, Juho Kannala
**Links:** [abs](https://arxiv.org/abs/2608.16863) - [pdf](https://arxiv.org/pdf/2608.16863)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, 3DGS, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis
- 作者：Yejun Zhang, Zihan Wang, Xu Ji, Yihao Wang, Yuxin Hou, Junyuan Fang, Juho-Matti Kilpeläinen, Arno Solin, Hamed Rezazadegan Tavakoli, Esa Rahtu, Juho Kannala
- 出版日期：2026-08-17
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.16863

### 一句话总结
SplatGuide 通过将单个 3D 高斯场景复用于三种互补信号（渲染图像、逐高斯可见性投票图、重建 token），弥合了前馈 3DGS 重建与多视角扩散之间的信息断层，实现了无需位姿的最新视图合成。

### 研究问题
如何在不使用相机位姿的情况下，利用 3D 高斯重建中的几何先验（包括可渲染几何、可见性线索和学到的特征）来提升新视图合成的质量，特别是解决现有管线仅提取单一信号而忽略其他信号的问题。

### 核心思路/方法
- 核心策略：在一个前馈 3DGS 重建过程中，同时复用同一场景产生三种信号：
  1. **渲染图像**：提供像素对齐的几何条件。
  2. **逐高斯源视角索引投票图**：渲染到目标视图，用于遮挡感知的参考视图选择。
  3. **重建 token**：通过交叉注意力提供特征级引导。
- 所有三种信号均来自同一次重建前向传播，无需额外计算开销。
- 与多视角扩散模型结合，实现从无位姿图像生成逼真新视图。

### 主要贡献
- 指出并解决现有管线中“信息断开”问题（即重建的几何、可见性信息和特征未被充分利用）。
- 提出 SplatGuide 方法，将单个 3DGS 场景用于三种互补角色，系统性提取几何先验。
- 在 RealEstate10K、DL3DV、Tanks-and-Temples 和 Mip-NeRF 360 上实现最先进的无需位姿新视图合成性能。
- 在 RealEstate10K 上，使用中等数量输入视图时，超越了使用真实位姿的基线方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该方法提出了明确的创新点（复用 3DGS 场景产生三种互补信号），针对无位姿新视图合成这一重要问题，在多个基准上达到最先进效果，甚至超越有真值位姿的基线，对神经场景表示与渲染领域具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Generating photorealistic novel views from unposed images requires both 3D geometric understanding and the ability to synthesize unseen content. A natural strategy combines feed-forward 3DGS reconstruction with multi-view diffusion. Yet prior pipelines extract at most one signal from the reconstruction, either pixel rendering or learned features, while none exploits per-Gaussian visibility for occlusion-aware reference selection. This *information disconnect* leaves renderable geometry, visibility cues, and learned features unused. SplatGuide closes this disconnect by reusing a single 3DGS scene across three complementary roles. Rendered images provide pixel-aligned geometric conditioning. Per-Gaussian source-view indices are rendered into a target-view voting map for occlusion-aware reference selection. Reconstruction tokens supply feature-level guidance via cross-attention. All three signals derive from the same reconstruction forward pass. Across RealEstate10K, DL3DV, Tanks-and-Temples, and Mip-NeRF 360, SplatGuide achieves state-of-the-art pose-free novel view synthesis. On RealEstate10K, with a moderate number of input views, it surpasses the ground-truth-pose baseline.

</details>

## Embodied / Robotics / AR Applications

### 2026-08

#### 2026-08-21 - Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding

**Authors:** Jie Xu, Na Zhao
**Links:** [abs](https://arxiv.org/abs/2608.21136) - [pdf](https://arxiv.org/pdf/2608.21136)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>Abstract</summary>

Recently, open-vocabulary zero-shot 3D scene understanding using vision foundation models has emerged as a promising alternative to data-intensive supervised methods. However, deploying these models in real-world scenarios is severely hindered by their inability to efficiently handle streaming RGB-D inputs and their inherent vulnerability to noise 2D segmentation masks. To address these critical limitations, we propose Stream3Dv2, a novel training-free framework designed for robust streaming 3D perception. Stream3Dv2 processes sequential data through an original nested local-to-historical architecture, capturing multi-view consistency while circumventing the high computational overhead so as to support timely responses. At its core, we introduce a comprehensive geometric-semantic fusion mechanism that resolves geometric noise and semantic ambiguity by explicitly utilizing semantic guidance and formulating 3D segmentation as solving point-and-set merging and partitioning problems. Furthermore, we present an innovative manifold-distance-based point cloud refinement strategy. This approach leverages local manifold graphs for point-to-manifold optimization that mitigates the boundary delineation failures caused by Euclidean-distance metrics, and employs geometric bounding boxes to dynamically activate and update historical instances for achieving rapid manifold-to-manifold refinement. Extensive experiments on public datasets demonstrate that Stream3Dv2 consistently outperforms existing baselines in foundational open-vocabulary streaming 3D segmentation and detection. Finally, we show that integrating our framework with an LLM-based agent enables advanced language-driven 3D scene understanding, underscoring its potential for open-world embodied intelligence. Code will be updated at https://github.com/SubmissionsIn/Stream3D.

</details>

#### 2026-08-19 - SceneGTMM: A Conformal Mapping-based Scene-Aware Transferable GNN-Transformer Dual-Graph Interaction Framework for Map Matching

**Authors:** Yongliang Zhang, Feng Song, Ji Chen, Lishuai Guo, Yong Deng, Yue Zheng, Tianyi Liu, Zhixiong Chen, Qixin Zhang
**Links:** [abs](https://arxiv.org/abs/2608.19298) - [pdf](https://arxiv.org/pdf/2608.19298)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SceneGTMM: A Conformal Mapping-based Scene-Aware Transferable GNN-Transformer Dual-Graph Interaction Framework for Map Matching
- 作者：Yongliang Zhang, Feng Song, Ji Chen, Lishuai Guo, Yong Deng, Yue Zheng, Tianyi Liu, Zhixiong Chen, Qixin Zhang
- 出版日期：2026-08-19
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.19298

### 一句话总结
本文提出了一种基于共形映射场景相对策略的GNN-Transformer双图交互框架SceneGTMM，用于实现高精度、可跨区域迁移的地图匹配方法。

### 研究问题
地图匹配技术在噪声鲁棒性、跨区域迁移和可解释性方面存在挑战，现有方法在局部-全局融合、动态路网适应以及对黑盒模型的依赖上存在局限。

### 核心思路/方法
论文提出SceneGTMM框架，包含三个主要技术模块：
1. 基于共形映射的场景相对策略：构建以轨迹为中心的局部坐标系，减少对训练路网的依赖，从而支持跨区域迁移和动态路网更新；
2. GNN-Transformer双图交互架构：GNN建模路网图以捕获局部拓扑约束，Transformer建模轨迹图以捕获全局时序依赖，并通过跨图注意力实现噪声抑制和语义对齐；
3. CRF增强的结构化预测：将Transformer的全局上下文与CRF的拓扑转移约束结合，提升路径连通性和鲁棒性。

### 主要贡献
- 提出共形映射场景相对策略，降低对训练路网的依赖，支持跨区域迁移；
- 设计GNN-Transformer双图交互架构，融合局部拓扑约束与全局时序依赖，并通过跨图注意力实现噪声抑制；
- 引入CRF增强的结构化预测，提升路径连通性和鲁棒性；
- 实验表明该方法在多种源轨迹和不同定位误差条件下均优于基线方法，并通过注意力与相对坐标可视化增强可解释性。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的计算复杂度、实时性能、对极端场景（如严重遮挡或信号丢失）的适应能力，以及在不同道路类型（如城市密集路网与乡村稀疏路网）上的具体表现差异。

### 阅读优先级
**中**
- 理由：该工作面向地图匹配这一具体应用场景，方法新颖性较高（结合共形映射、GNN、Transformer与CRF），并有定量改进数据支撑。但该领域相对垂直，且论文发表于2026年，研究时效性尚需验证；若您的研究方向涉及轨迹数据挖掘、智能交通或自动驾驶路径规划，则值得精读，否则可暂缓。

</details>

<details>
<summary>Abstract</summary>

Map matching is a key technology connecting positioning data with high precision road networks, but it faces challenges in noise robustness, cross regional transfer, and interpretability. To addr ess the limitations of existing methods in local global fusion, dynamic road network adaptation, and reliance on black box mod els, this paper proposes SceneGTMM, a transferable GNN Transformer dual graph interaction map matching framework based on a conformal mapping based scene relative strategy. 1) Conformal mapping based scene relative strategy: constructs trajectory centric local coordinate systems to reduce dependence on the training road network, supporting cross regional transfer and dynamic road network updates; 2) GNN Transformer dual graph interaction architecture: a GNN modeled road graph captures local topological constraints, while a Transformer modeled trajectory graph captures global temporal dependencies, and cross graph attention achieves noise suppression and semantic alignment; 3) CRF enhanced structured prediction: combines the global context of the Transformer with the topological transition constraints of CRF to improve path connectivity and robustness. Experiments show that SceneGTM achieves over 80% accuracy on multi source trajectories with positioning errors of 16 50 meters, representing a 5.3% improvement over HMM. In cross city transfer scenarios, it outperforms MTrajRec, GraphMM, and TMM, and enhances interpretability through attention and relative coordinate visualization. This study provides a new paradigm for high precision, transferable map matching for real time traffic perception and autonomous driving path planning.

</details>

#### 2026-08-19 - LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding

**Authors:** Yumin Lee, Hyoseok Ju, Giseop Kim
**Links:** [abs](https://arxiv.org/abs/2608.19059) - [pdf](https://arxiv.org/pdf/2608.19059)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding
- 作者：Yumin Lee, Hyoseok Ju, Giseop Kim
- 出版日期：2026-08-19
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.19059

### 一句话总结
LT-Mem提出了一种基于易变性感知的时空记忆框架，通过三层记忆结构（Live、Delta、Meta）和波动性调节策略，实现对长期场景中对象跨会话历史的持续理解与推理。

### 研究问题
长期运行的机器人在动态演化环境中面临“时间性失忆”问题：现有系统要么覆盖历史以维持最新地图，要么存储语义快照但缺乏跨会话一致的对象身份，导致无法回答如“绿色椅子在所有会话中出现在哪些位置？”这类需要对象历史信息的问题。

### 核心思路/方法
1. **多会话SLAM骨干**：提供跨会话空间对齐的逐对象观测数据。
2. **推理层（易变性感知策略）**：通过确定性证据评分保持跨会话身份一致性，并基于每个对象的动态特征，在“覆盖（overwrite）”、“保持（hold）”和“多假设（multi-hypothesis）”三种动作中进行选择。
3. **Tri-Memory结构**：包含Live（当前状态）、Delta（变化信息）和Meta（事件历史）三个部分，同时保留当前状态与事件历史，支持纵向对象中心推理。
4. **评估数据集LT-VQA**：包含多会话记录、持久身份标注和时间问答对，用于系统评估。

### 主要贡献
- 提出了LT-Mem，一个将空间对齐的实例级3D感知与易变性条件时间推理相统一的记忆演化框架。
- 设计了Tri-Memory结构，解决了跨会话对象身份一致性与历史信息保留的兼顾问题。
- 引入了LT-VQA数据集和评估套件，包含多会话记录、持久身份标注和时间QA对。
- 实验表明LT-Mem在所有指标上持续优于基线，且消耗的token数量少一个数量级；消融实验确认性能提升来自结构化记忆架构而非LLM容量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接面向机器人长期场景理解中对象历史遗忘这一实际痛点，提出了新颖的三层记忆架构与易变性感知策略，并配套了专门的数据集。其在效率和性能上均有显著优势声明，对持续学习、场景理解及具身智能方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Long-term robot operation in evolving environments requires object-level understanding that persists across repeated revisits. Existing systems either overwrite history to maintain an up-to-date map or store semantic snapshots without consistent cross-session object identity, resulting in temporal amnesia: the systematic loss of object history that prevents answering queries such as "Where has the green chair been across all sessions?" We propose LT-Mem, a volatility-aware memory evolution framework that unifies spatially aligned instance-level 3D perception with volatility-conditioned temporal reasoning. First, a multi-session SLAM backbone provides spatially aligned per-object observations across sessions. Second, a reasoning layer governs how object memory evolves: deterministic evidence scoring preserves cross-session identity, and a volatility-aware policy selects among overwrite, hold, and multi-hypothesis actions based on each object's dynamics. Third, the resulting Tri-Memory structure (Live, Delta, Meta) preserves both current states and event histories, enabling longitudinal object-centric reasoning. We further introduce LT-VQA, a dataset and evaluation suite comprising multi-session recordings, persistent identity annotations, and temporal QA pairs. Experiments show that LT-Mem consistently outperforms baselines across all metrics while consuming an order of magnitude fewer tokens, and ablations confirm that gains are driven by the structured memory architecture rather than LLM capacity.

</details>

#### 2026-08-18 - GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction

**Authors:** Ziyang Cheng, Tianshu Tang, Jinxin Lan, Xinze Chen, Yuhan Gong, Zhichao Liu, Changzhong Wu, Yahao Mao, Zongyan Deng, Mingxuan Ma, Huasen Xi, Yilong Liu, Yutong Wu, Xiaofeng Wang, Yang Wang, Yun Ye, Guan Huang, Xiaojie Jin, Zheng Zhu, Jiwen Lu
**Links:** [abs](https://arxiv.org/abs/2608.18234) - [pdf](https://arxiv.org/pdf/2608.18234)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GigaBrain-WBC-0.5：用于与环境交互的鲁棒全身控制行为世界模型
- 作者：Ziyang Cheng, Tianshu Tang, Jinxin Lan, Xinze Chen, Yuhan Gong, Zhichao Liu, Changzhong Wu, Yahao Mao, Zongyan Deng, Mingxuan Ma, Huasen Xi, Yilong Liu, Yutong Wu, Xiaofeng Wang, Yang Wang, Yun Ye, Guan Huang, Xiaojie Jin, Zheng Zhu, Jiwen Lu
- 出版日期：2026-08-18（arXiv 发布时间）
- 分类：Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：https://arxiv.org/abs/2608.18234

### 一句话总结
本文提出首个用于人形机器人全身控制的行为世界模型（BWM）GigaBrain-WBC-0.5，通过联合预测动作、状态和潜在行为命令分布，使机器人能够在地形交互、不合理命令和跌倒扰动等场景下保持鲁棒运动控制。

### 研究问题
现有全身运动跟踪策略仅在平坦地面上有效——在空场景中训练，未学习地形与物体接触对动力学的影响；且试图通过不断扩充参考动作库来平衡任意命令，但当可行行为依赖于环境时该方法失效。本文旨在解决人形机器人在复杂环境交互下如何保持鲁棒全身控制的问题。

### 核心思路/方法
- 提出行为世界模型（BWM）：训练一个因果Transformer，联合预测下一步动作、下一步状态以及下一步潜在行为命令的分布，使"执行动作的网络"同时建模环境对其可行行为的影响，而非纯粹的反应式跟踪器。
- 自动地形标注流程：从重定向动作中恢复完整3D接触几何信息，实现与现有动作数据集规模相当的地形标注。
- 部署时重用预测分布：在线检测不合理命令并将其"收回"到已学习的行为上，使机器人以"尽力而为"的方式尝试任务。

### 主要贡献
- 首次提出用于人形全身控制的行为世界模型（BWM），统一策略能实时响应命令、与环境交互，并对不合理命令、跌倒和扰动保持鲁棒。
- 提出自动地形标注流水线，可在大规模动作数据集上恢复3D接触几何。
- 实验表现：地形交互成功率达81.3%（为最强基线的4.3倍），不合理命令下83.1%，跌倒恢复99.3%（最强基线的16.8倍），在所有四个场景中均超过三个大规模跟踪基线。
- 硬件验证：在缺失支撑和扰动下表现出鲁棒交互；Unitree G1检查点通过简单微调迁移至Maker L01机器人。

### 局限性
摘要未提供足够信息。摘要未涉及模型的计算开销、训练数据规模细节、失败案例分析、方法在其他机器人平台上的泛化程度、以及是否在真实复杂地形（如非规则地面）上验证等信息。

### 阅读优先级
**高**。理由：该工作针对人形机器人全身控制中的核心挑战（环境交互与鲁棒性），提出了新的建模思想（行为世界模型），在多个任务上大幅超越基线（有些指标为基线的4–16倍），并包含真实硬件验证，具较强实用价值与创新性。适合机器人控制、具身智能相关研究者深入阅读。

</details>

<details>
<summary>Abstract</summary>

Whole-body motion tracking policies turn a humanoid into a robust control interface: the teleoperator---or an upstream model---only supplies a coarse movement intent, while the low-level policy keeps the robot balanced and physically feasible. Existing trackers deliver this interface only on flat ground: trained in empty scenes, they never learn how contact with terrain and objects reshapes their dynamics, and they attempt to teach the policy to balance under any command by continually enlarging the reference-motion corpus, which stops working once feasible behaviors become environment-dependent. We present GigaBrain-WBC-0.5, the first Behavior World Model (BWM) for humanoid whole-body control. Rather than a purely reactive tracker, we train a causal Transformer to jointly predict its next action, next state, and the distribution over its next latent behavior command, so the network that acts also models how the environment shapes what it can do next. An automatic terrain-annotation pipeline recovers full 3D contact geometry from retargeted motion, enabling terrain annotation at the scale of existing motion datasets. The predicted distribution is reused at deployment to detect implausible commands online and retract them onto learned behaviors, so the robot attempts tasks in a "best-effort" manner. The result is a unified policy that takes real-time command, interacts with environment, and stays robust to implausible commands, falls, and disturbances. GigaBrain-WBC-0.5 achieves the highest success rate across all four regimes among three large-scale tracker baselines: 81.3% on terrain interaction (4.3x the strongest baseline), 83.1% under implausible commands, and 99.3% fall recovery (16.8x the strongest baseline). Hardware trials show robust interaction under missing supports and disturbances; the Unitree G1 checkpoint transfers to the Maker L01 robot with simple fine-tuning.

</details>

#### 2026-08-17 - Mask What Matters: Saliency-Guided Video Self-Supervised Learning for Autonomous Driving

**Authors:** Christopher Lang, Alexander Braun, Abhinav Valada
**Links:** [abs](https://arxiv.org/abs/2608.17178) - [pdf](https://arxiv.org/pdf/2608.17178)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mask What Matters: Saliency-Guided Video Self-Supervised Learning for Autonomous Driving
- 作者：Christopher Lang, Alexander Braun, Abhinav Valada
- 出版日期：2026-08-17
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.17178

### 一句话总结
本文提出了一种基于显著性引导的掩码策略（V-JEPA4A），用于自动驾驶场景下的视频自监督预训练，通过优先保留和预测语义与时间上重要的区域，提升了下游感知任务的性能。

### 研究问题
现有的视频自监督学习通常采用随机掩码策略，忽略了区域在语义和时间上的重要性。在自动驾驶的第一视角视频中，安全关键目标（如行人、车辆、车道边界）仅占画面小部分，随机掩码会削弱预训练信号，如何设计更有效的掩码策略以提升表征学习质量是本文的核心问题。

### 核心思路/方法
作者提出了V-JEPA4A，一种针对自动驾驶领域专门化的V-JEPA变体。其核心创新在于一种新颖的显著性驱动的掩码策略，该策略根据区域的语义重要性和时间相关性来决定保留和预测的上下文，从而在保持掩码预测效率的同时，引导模型学习更富信息量的特征表示。

### 主要贡献
- 提出了适用于自动驾驶视频预训练的显著性驱动掩码策略，替代随机掩码。
- 在公开驾驶视频上预训练了领域专用模型V-JEPA4A。
- 在四个驾驶基准（跟踪、语义分割、深度估计）上验证了有效性：在BDD100k MOT上相比随机掩码V-JEPA减少25%的身份切换，Cityscapes上达到73.2 mIoU，KITTI-2015深度上达到3.75 RMSE，预训练迭代开销仅增加约14%。

### 局限性
摘要未提供关于方法局限性讨论、消融实验细节、失败案例分析或计算资源具体要求的信息。

### 阅读优先级
**高**
理由：该工作针对自动驾驶这一重要应用场景，直接改进自监督预训练的核心掩码策略，并在多个下游任务上展现了显著提升，且增量成本可控；对于从事自动驾驶感知、自监督学习或视频表征学习的研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Video self-supervised learning through masked spatiotemporal prediction has emerged as a promising paradigm for learning feature representations from unlabeled data. However, existing methods typically rely on random masking, which indiscriminately removes regions irrespective of their semantic or temporal relevance. In ego-centric driving videos, this can weaken the pretext signal since safety-critical cues such as pedestrians, vehicles, lane boundaries, and dynamic interactions often occupy only a small portion of the frame, yet are central to downstream perception. We introduce V-JEPA4A, a domain-specialized variant of V-JEPA for autonomous driving that is pre-trained on publicly available driving videos with a novel saliency-driven masking policy. It accounts for semantically and temporally relevant context. The proposed policy preserves and predicts context according to semantic importance and temporal relevance, yielding more informative representation learning while retaining the efficiency of masked prediction. We evaluate the resulting encoders on four driving benchmarks spanning tracking, semantic segmentation, and depth estimation. The results demonstrate that V-JEPA4A reduces identity switches on BDD100k MOT by 25% over V-JEPA with random masking, achieves 73.2 mIoU on Cityscapes, and 3.75 RMSE on KITTI-2015 depth, while incurring only ~14% additional pre-training iteration overhead.

</details>

#### 2026-08-17 - ViHaTeleop: A Low-Cost, Lightweight Visual-Haptic Teleoperation System for Dexterous Manipulation Learning

**Authors:** Fucai Zhu, Yanhou Lai, Paul Maestre, Koichi Hashimoto
**Links:** [abs](https://arxiv.org/abs/2608.16572) - [pdf](https://arxiv.org/pdf/2608.16572)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ViHaTeleop: A Low-Cost, Lightweight Visual-Haptic Teleoperation System for Dexterous Manipulation Learning
- 作者：Fucai Zhu, Yanhou Lai, Paul Maestre, Koichi Hashimoto
- 出版日期：2026-08-17
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.16572

### 一句话总结
本文提出了一种低成本、轻量级的视觉-触觉遥操作系统 ViHaTeleop，通过引入指级振动触觉反馈，显著提升了接触关键型灵巧操作任务的示教质量与成功率。

### 研究问题
如何以低成本硬件实现高质量的接触关键型灵巧操作示教数据采集，即解决低成本遥操作硬件难以采集接触关键演示数据的问题。

### 核心思路/方法
- 构建轻量（0.7 kg）低成本（$550）的视觉-触觉遥操作系统，融合 SLAM 腕部追踪、相机手部追踪以及基于线性谐振致动器（LRA）的指级振动触觉反馈。
- 引入若干设计选择：LED 照明、鱼眼手部相机、触觉感知重定向约束。
- 在真实环境（Franka + LEAP Hand + 9DTact）与仿真环境（Isaac Sim）中部署系统，并集成基于深度相机的轻量触觉代理，实现从多模态示教采集到视觉-触觉策略训练的完整流程。

### 主要贡献
- 首次提出结合低成本视觉追踪与指级振动触觉反馈的遥操作系统，并通过消融实验验证触觉反馈的有效性。
- 在六项接触关键任务、九名参与者的匹配实验中，触觉反馈使所有任务的成功率提升（+2.2～+15.6 个百分点），主观评分在触觉清晰度和抓取信心方面有显著提升（Wilcoxon 符号秩检验，p<0.05）。
- 提供从多模态示教采集到视觉-触觉策略训练的完整管线，初步下游验证表明触觉线索对接触关键子任务（如插销入孔）有显著增益（相较纯视觉提升 +17 个百分点）。

### 局限性
摘要未提供足够信息；未报告硬件耐久性、系统延迟、大规模任务泛化能力、参与者多样性等细节。

### 阅读优先级
**高**。理由：该工作直击灵巧操作示教学习中接触关键数据采集困难的核心痛点，系统成本低、重量轻，且提供了真实与仿真环境下的多任务验证以及消融实验，对遥操作硬件设计和触觉反馈在人机交互中的价值均有明确的数据支撑，适合机器人操作、示教学习与人机交互方向的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

Learning from demonstration is a promising approach for dexterous manipulation, but collecting high-quality contact-critical demonstrations remains difficult with low-cost teleoperation hardware. We present ViHaTeleop, a lightweight (0.7 kg), low-cost (\$550) visual-haptic teleoperation system with SLAM-based wrist tracking, camera-based hand tracking, and finger-wise vibrotactile feedback through Linear Resonant Actuators (LRA). The system includes several design choices (LED illumination, fisheye hand camera, and tactile-aware retargeting constraints) and is deployed on Franka + LEAP Hand + 9DTact in both real and simulated environments. Under matched with/without-haptic conditions with nine participants across six contact-critical tasks, haptics improved success rates across all tasks (+2.2 to +15.6 percentage points), while completion-time effects were task-dependent. Subjective ratings showed significant gains in contact clarity and grasp confidence in both simulation and real-world settings (Wilcoxon signed-rank, $p<0.05$). We also integrate a lightweight depth-camera-based tactile proxy in Isaac Sim, enabling a full pipeline from multi-modal demonstration collection to visual-tactile policy training. Preliminary downstream validation by training visual-tactile policies from collected demonstrations shows tactile cues benefit contact-critical subtasks (peg-in-hole: +17 percentage points over vision-only).

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
