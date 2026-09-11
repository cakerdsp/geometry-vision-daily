# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：48
- 分类分布：
  - Embodied / Robotics / AR Applications: 17
  - 3D Reconstruction & Multi-view Geometry: 15
  - Neural Scene Representations & Rendering: 12
  - Geometry Foundation Models: 2
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **前馈式重建正从“场景级几何”走向“对象级可交互资产”。**
   FIRE3D、Point4D、RoMa-$\Omega$ 共同指向一个方向：用一次前向推理直接输出可用于下游任务的显式表示，而不是依赖每场景优化。FIRE3D 强调对象级解耦与仿真就绪，Point4D 强调长程 4D 轨迹的前馈推断，RoMa-$\Omega$ 则把前馈 3D 模型的表征直接迁移到匹配任务。三者分别从场景资产、动态轨迹、匹配表征三个层面削弱了“测试时优化”的必要性。

2. **神经场景表示的“可信度与可压缩性”成为独立研究议题。**
   VSCP、LinearMask-GS、CVT-GS、RouteBridge、PIC 五篇都围绕 3DGS/NeRF/INR 展开，但关注点不在渲染质量本身，而在覆盖率保证、剪枝稳定性、后处理压缩、跨表示蒸馏路由和编码速度。这说明该方向正从“如何重建得更像”转向“如何让已有表示更可信、更小、更快、更可组合”。

3. **几何基础模型的角色正在被重新定义：从特征抽取器变为匹配与位姿估计的可复用底座。**
   RoMa-$\Omega$ 直接检验前馈 3D 模型对匹配的“知识”，并用 VGGT-$\Omega$ 替换 DINO 骨干；PROSE 用多模态基础特征做无先验相对 6D 位姿；GoDeep 把视觉-语言模型仅当作“翻译器”，在纯语言空间做 3D 语义理解。三者都减少了对专用 3D 编码器或对象先验的依赖，倾向于复用通用基础模型。

4. **机器人/具身方向出现“仿真—真实—生成”三者的闭环缝合。**
   RealSimLoop 用视觉反馈做在线 real-to-sim 参数自适应；Grounding Generated Video Plans 把生成 HOI 视频作为仿真跟踪器的参考运动；SyncWorld 用视觉校准片段把世界模型变成零样本模拟器；Rethinking Learned Occupancy 则揭示占用精度与闭环覆盖并非单调关系。这些工作共同表明：仿真不再只是训练环境，而是与真实观测、生成模型、规划器在线耦合的中间层。

5. **球面/鱼眼/多相机等非标准成像几何重新受到关注。**
   Spheriverse 构建球面图像-LiDAR 数据集并处理球面-笛卡尔表示差异；MFVINS 用多鱼眼相机+IMU 提升 VINS 鲁棒性；Field Converter 则依赖已标定足球转播的相机与球场几何。这些工作说明，在标准针孔视角之外，全向、鱼眼、体育转播等成像条件正成为 3D 理解与位姿估计的独立子问题。

#### 技术路线观察

- **几何基础模型方向**：核心问题从“预训练特征是否通用”转向“前馈 3D 模型内部到底编码了什么”。RoMa-$\Omega$ 通过零样本匹配、点图直接匹配、表征上训练匹配器三种场景做诊断；PROSE 则把多模态基础特征用于无 CAD/模板/参考图的相对 6D 位姿。技术侧重点在于：减少任务特定监督、减少对象先验、利用环一致性等几何约束做全局细化。

- **3D/4D 重建方向**：FIRE3D 走对象级组合表示，输出 6-DoF 位姿、包围框、网格、纹理，强调仿真就绪与物理解耦；Point4D 走长程逐点 3D 轨迹，用 3D query 解码器把轨迹预测与图像平面可见性解耦；Learning Global Camera Poses 走视图图聚合，用置换等变边条件 GNN 从噪声相对位姿回归全局外参，训练不依赖真值。三者共同趋势是：不再只输出点云或隐式场，而是输出结构化、可组合、可长程追踪的中间表示。

- **神经场景表示与渲染方向**：VSCP 把新视图合成视为结构化回归，要求视图级覆盖率保证；LinearMask-GS 和 CVT-GS 都针对 3DGS 基元冗余，前者在训练时用线性增量激活稳定掩码排序，后者在训练后做免优化 CVT 聚类合并；RouteBridge 按光线选择 NeRF↔3DGS 蒸馏方向或弃权；PIC 则把 INR 图像编码推向 20 FPS 编码、2000 FPS 解码。技术侧重点从“更高 PSNR”转向覆盖率有效性、剪枝稳定性、后处理兼容性、蒸馏可靠性、编解码速度。

- **机器人/AR 应用方向**：RealSimLoop 在降阶神经子空间内做可微仿真，用可微渲染反传梯度在线更新材料参数；Grounding Generated Video Plans 用生成视频提供多物体多轨迹参考，再在仿真中学习 HOI 跟踪器；SyncWorld 用视觉校准片段在上下文中指定 action-visual mapping；Rethinking Learned Occupancy 则直接质疑“占用越准，主动建图越好”的假设，提出观测门控滤波。技术侧重点在于：在线自适应、零样本迁移、闭环规划接口的在线修正。

- **交叉观察**：Field Converter、ArmPoser、MFVINS 分别代表体育转播、可穿戴 IMU、多鱼眼 VINS 三种“非标准输入”的位姿估计路线。它们共同说明，当输入模态或成像几何偏离标准设定时，几何初始化、物理约束和传感器融合仍是提升鲁棒性的关键手段。

#### 值得优先阅读的论文

1. **Point4D: Long-range 4D Motion Reconstruction**
   理由：直接针对 4D 重建中“最多几十帧”的公认瓶颈，提出 3D query 解码器将轨迹预测与可见性解耦，并在超过 200 帧的基准上取得领先。对动态场景理解、长视频追踪、4D 表示学习都有直接参考价值。

2. **RoMa-$\Omega$: What Feed-Forward 3D Models Know About Image Matching**
   理由：它不只是提出一个新匹配器，而是系统诊断前馈 3D 模型在匹配任务中的表征能力，并用 VGGT-$\Omega$ 替换 DINO 骨干。对理解几何基础模型的内部能力边界、以及匹配与重建的融合趋势都很关键。

3. **FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute**
   理由：把单图/视频到仿真就绪对象级资产的流程压缩到一分钟内，且无需测试时优化。对游戏、交互应用、机器人仿真资产生成都有直接落地意义，代表前馈重建走向对象级可交互表示的方向。

4. **VSCP: View-Structured Conformal Prediction for 3D Gaussian Splatting**
   理由：3DGS 的不确定性量化目前仍不成熟，该工作把覆盖率保证从像素级边际提升到视图级有效，并给出有限样本有效性分析。对需要安全保证的渲染、规划、决策下游任务有较高参考价值。

5. **RealSimLoop: Online Real-to-Sim Adaptation via Differentiable Reduced-Order Simulation with Vision Feedback**
   理由：同时触及可微仿真、降阶神经子空间、可微渲染、在线材料参数自适应四个技术点，且强调准实时和时变材料跟踪。对机器人操作、可变形物体建模、real-to-sim 方向有较强组合启发。

#### 可能的研究机会

- **前馈重建与可信度保证的结合**：FIRE3D、Point4D 等前馈模型输出结构化资产，但摘要未讨论其不确定性。VSCP 的视图级共形预测思路能否迁移到对象级位姿、网格或 4D 轨迹的覆盖率保证，是一个自然组合方向。

- **3DGS 压缩与蒸馏的联合优化**：LinearMask-GS 关注训练时掩码稳定性，CVT-GS 关注训练后免优化合并，RouteBridge 关注 NeRF↔3DGS 双向蒸馏。三者可以组合成“

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-11T12:26:17-04:00
**Total number of papers:** 53
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

### 2026-09

#### 2026-09-10 - SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views

**Authors:** Langxu Zhao, Zuan Gu, Yingdan Zhang, Pengfei Zhao, Tianhan Gao
**Links:** [abs](https://arxiv.org/abs/2609.11279) - [pdf](https://arxiv.org/pdf/2609.11279)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** DUSt3R, robotics, AR, VR

<details>
<summary>Abstract</summary>

With the rising demand to decouple objects from 3D scenes, we propose SAMV-DUSt3R, an end-to-end model that injects SAM2 2D masks into MV-DUSt3R reconstruction. A Cross Flow Mask Block uses these masks to steer the network toward the target instance, jointly improving shape accuracy and achieving object-level disentanglement without multi-stage pipelines. To ensure reconstruction stability, a lightweight Spatial RankGNN selects the optimal reference view with a selection accuracy of 73.5\%. Extensive experiments demonstrate that our method boosts average reconstruction precision by 11\% across various metrics compared to state-of-the-art baselines. These results reveal a strong instance-disentanglement capability and clear benefits for driving, robotics, AR/VR, and heritage digitisation.

</details>

#### 2026-09-08 - RoMa-$Ω$: What Feed-Forward 3D Models Know About Image Matching

**Authors:** David Nordström, Xinyue Zhang, Thibaut Loiseau, Vincent Lepetit, Fredrik Kahl
**Links:** [abs](https://arxiv.org/abs/2609.09507) - [pdf](https://arxiv.org/pdf/2609.09507)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, MASt3R, feed-forward reconstruction, image matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoMa-$Ω$: What Feed-Forward 3D Models Know About Image Matching
- 作者：David Nordström, Xinyue Zhang, Thibaut Loiseau, Vincent Lepetit, Fredrik Kahl
- 出版日期：2026-09-08T22:50:46Z
- 分类：Geometry Foundation Models（主）；3D Reconstruction & Multi-view Geometry（次）
- 链接：[摘要页](https://arxiv.org/abs/2609.09507)｜[PDF](https://arxiv.org/pdf/2609.09507)

### 一句话总结
该工作系统分析了前馈式三维重建模型在图像匹配任务中的表征能力，并基于分析结论用 VGGT-$Ω$ 替换 RoMa v2 的 DINO 骨干，得到在多个基准上超越当前先进匹配器的 RoMa-$Ω$。

### 研究问题
匹配器（如 RoMa，其鲁棒性常被归因于冻结的 DINO 特征）与前馈式重建模型（如 VGGT，在大规模数据上训练以回归稠密三维点图与相机位姿）之间的界限因 MASt3R、VGGT-$Ω$ 等引入匹配损失而日益模糊。作者据此提出核心问题：前馈式三维模型究竟“知道”多少关于图像匹配的信息？

### 核心思路/方法
论文通过三种场景来分析前馈式三维模型在匹配方面的能力：
1. patch 特征的零样本匹配；
2. 三维点预测的直接匹配；
3. 在学习到的表征之上训练完整匹配器。

基于上述分析结论，作者以 VGGT-$Ω$ 替换 RoMa v2 的 DINO 骨干，重新训练得到模型 RoMa-$Ω$。

### 主要贡献
- 给出对前馈式三维重建模型匹配能力的系统分析，覆盖零样本 patch 特征匹配、三维点预测直接匹配、以及在其表征上训练完整匹配器三种场景。
- 发现：前馈式重建模型在零样本匹配（尤其在较深层）表现不佳，但其表征对线性探测与完整匹配流程具有很强的可用性。
- 发现：即使不经过任何训练，其原始预测单独即可实现有竞争力的匹配，但仅在中等视角变化与模态差异条件下成立。
- 基于这些洞察重训 RoMa v2（替换骨干为 VGGT-$Ω$），所得 RoMa-$Ω$ 在广泛基准上超越当前先进匹配器，例如在 WxBS 上相较 RoMa v2 提升 +8.1 mAA。

### 局限性
- 摘要仅指出未训练的原始预测实现有竞争力匹配“仅在中等视角变化与模态差异下成立”，暗示其在更大视角变化或更大模态差异下的适用性受限。
- 具体的实验基准范围、失败案例、计算开销与训练成本等细节，摘要未提供足够信息。
- 分析所覆盖的前馈式三维模型种类、VGGT-$Ω$ 的具体结构与训练配置等，摘要未提供足够信息。

### 阅读优先级
中。理由：选题位于匹配与前馈式三维重建的交叉前沿，对理解“三维基础模型表征是否可用于匹配”这一开放问题有直接价值，且提出的 RoMa-$Ω$ 报告了明确的基准提升（如 WxBS +8.1 mAA）；但摘要未给出具体基准列表、消融与失败情形的细节，是否与自身研究方向强相关需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

Learned image matching has experienced significant progress in recent years, culminating in robust and accurate matchers such as RoMa, whose robustness is often attributed to its use of frozen DINO features. In a parallel development, feed-forward reconstruction models, such as VGGT, have been trained on ever-growing datasets to accurately regress dense 3D point maps and camera poses. The distinction between matchers and feed-forward reconstruction models has become increasingly blurred with the introduction of matching losses in models such as MASt3R and VGGT-$Ω$. This raises a natural question: what do feed-forward 3D models know about image matching? In this work, we answer this question by analyzing three scenarios: (i) zero-shot matching of patch features, (ii) direct matching of 3D point predictions, and (iii) training a full matcher on top of the learned representations. We find that, despite performing poorly in zero-shot matching, especially in later layers, feed-forward reconstruction models provide strong representations for linear probing and full matching pipelines. We further show that, even without any training, their raw predictions alone enable competitive matching, albeit only under moderate viewpoint changes and modality gaps. Based on these insights, we retrain RoMa v2 by replacing its DINO backbone with VGGT-$Ω$. Our resulting model, \ours, outperforms state-of-the-art matchers on a wide range of benchmarks, e.g. +8.1 mAA compared to RoMa v2 on WxBS.

</details>

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-08 - Point4D: Long-range 4D Motion Reconstruction

**Authors:** Minsik Jeon, Jay Karhade, Deva Ramanan, Shubham Tulsiani
**Links:** [abs](https://arxiv.org/abs/2609.09145) - [pdf](https://arxiv.org/pdf/2609.09145)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, motion reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Point4D: Long-range 4D Motion Reconstruction
- 作者：Minsik Jeon, Jay Karhade, Deva Ramanan, Shubham Tulsiani
- 出版日期：2026-09-08
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2609.09145

### 一句话总结
Point4D 提出了一种前馈式4D重建模型，能够对数百帧的长视频序列进行稠密的逐点3D轨迹推断，突破了现有方法仅能处理几十帧短窗口的限制。

### 研究问题
如何实现长视频序列（多百帧级别）的稠密4D运动重建，克服现有4D方法受限于短输入窗口（至多几十帧）的瓶颈。

### 核心思路/方法
- 核心创新是一种灵活的基于3D查询的运动解码器，将轨迹预测与图像平面可见性解耦。
- 预测得到的3D端点可以在下一个时间块中直接被重新查询，无需重新投影或特征匹配。
- 在提取视觉描述符时，不限于源patch，而是从任意可见该点的帧中提取并复用描述符，实验证明该方法优于仅依赖源patch的方案。

### 主要贡献
- 提出Point4D，一种面向长视频的前馈式4D重建模型，可处理跨数百帧的序列。
- 提出基于3D查询的运动解码器，实现轨迹预测与可见性解耦。
- 证明跨帧复用视觉描述符的有效性。
- 在多个跨度超过200帧的长视频追踪基准上达到最先进性能，显著优于此前的前馈4D方法。

### 局限性
摘要未提供足够信息。摘要中未讨论模型的计算复杂度、推理时间、对遮挡或快速运动场景的鲁棒性等潜在局限。

### 阅读优先级
**高**。理由：该工作直接解决了4D重建中长序列处理的公认瓶颈，提出了简洁而创新的解码机制，在多个长视频基准上取得领先结果，对动态场景理解和视频追踪方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce Point4D, a feed-forward model for 4D reconstruction of long-range video sequences. Point4D is able to reliably infer dense per-point 3D trajectories across multi-hundred-frame videos, unlike existing 4D methods that are limited to short input windows of at most a few dozen frames. A key innovation that enables this is our flexible 3D query-based motion decoder that decouples trajectory prediction from image-plane visibility. The predicted 3D endpoints are then directly re-queried in the next chunk without re-projection or matching. Furthermore, we show that extracting and reusing a visual descriptor from an arbitrary frame where the point is visible leads to better performance than relying solely on the source patch. Overall, Point4D achieves state-of-the-art performance across diverse long-video tracking benchmarks spanning over 200 frames and largely outperforms previous feed-forward 4D method. Project page: https://point-4d.github.io

</details>

#### 2026-09-08 - EdMCGS: Event-Driven Markov Chain Gaussian Splatting for Extreme-Low-Frame-Rate Dynamic Scene Reconstruction

**Authors:** Yuzhong Wang, Wenmin Wang, Xinxing Yu
**Links:** [abs](https://arxiv.org/abs/2609.08332) - [pdf](https://arxiv.org/pdf/2609.08332)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, scene reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EdMCGS: Event-Driven Markov Chain Gaussian Splatting for Extreme-Low-Frame-Rate Dynamic Scene Reconstruction
- 作者：Yuzhong Wang, Wenmin Wang, Xinxing Yu
- 出版日期：2026-09-08
- 分类：动态/4D重建（主分类）；3D重建与多视角几何、神经场景表征与渲染（副分类）
- 链接：https://arxiv.org/abs/2609.08332

### 一句话总结
本文提出EdMCGS，一种端到端方法，利用事件流将极低帧率RGB动态场景建模为事件驱动的马尔可夫链，实现对任意中间时刻的3D场景重建与渲染。

### 研究问题
如何从极低帧率RGB图像（帧间信息严重缺失）配合事件流，高质量重建动态3D场景并渲染任意中间时刻，避免仅依赖RGB时产生的伪影。

### 核心思路/方法
- 将场景运动建模为**事件驱动的马尔可夫链**：稀疏RGB帧作为状态锚点，区间内记录的事件驱动状态转移。
- 转移过程在推理时仍保持活跃，直接从事件产生3D高斯中间运动，而非通过插值（区别于仅将事件用于训练监督的先前工作）。
- 状态由一组紧凑的控制点承载，每个控制点由其图像投影邻域内采样的事件驱动。
- 引入**时间局部等距约束**，确保传播运动局部刚性。
- 实验显示该方法在合成与真实场景上优于基于RGB和基于事件的基线，且实时渲染所需高斯数量远少于最强事件基线。

### 主要贡献
- 提出事件驱动马尔可夫链高斯溅射（EdMCGS），实现极低帧率下的动态场景重建。
- 推理阶段直接从事件生成帧间运动，而非训练后插值。
- 使用紧凑控制点和局部等距约束保持运动刚性与效率。
- 在合成与真实场景上超越RGB基线与事件基线，并以更少高斯数实现实时渲染。
- 发布源码与新数据集（GitHub链接已提供）。

### 局限性
摘要未提供足够信息（未明确讨论失败场景、边界条件、对噪声/事件稀疏性的鲁棒性等）。

### 阅读优先级
**中**。理由：方法新颖（事件驱动马尔可夫链+高斯溅射），针对极低帧率重建这一实际痛点，且展示出明显效率与质量优势；但若您不关注动态/4D重建或事件相机方向，则该工作相关性不高。建议该领域研究者阅读。

</details>

<details>
<summary>Abstract</summary>

We present EdMCGS (Event-driven Markov chain Gaussian Splatting), an end-to-end method for reconstructing dynamic 3D scenes from extreme-low-frame-rate RGB together with an event stream, which can then be rendered at any intermediate timestamp. Methods relying solely on RGB images generate numerous artifacts due to the lack of evidence from between consecutive frames. To supply this missing evidence, we model the scene motion as an event-driven Markov chain, in which the sparse RGB frames anchor the state at their own timestamps while the events recorded within an interval drive the transition across it. Since the transition reads the events of the current interval, it remains active at inference and produces the in-between motion of the 3D Gaussians directly from the events rather than by interpolation, which sets our method apart from prior work that uses events only as training-time supervision. The state is carried by a compact set of control points, each driven by the events sampled in the neighborhood of its own image projection, and a temporal local isometry term keeps the propagated motion locally rigid. Experiments on synthetic and real-world scenes show that EdMCGS outperforms both RGB-based and event-based baselines, while rendering in real time with far fewer Gaussians than the strongest event-based baseline. We release our source code and a new dataset at https://github.com/joseclipse/EdMCGS.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-10 - Visual-SLAM for the detection of hidden tomatoes in greenhouses by Hierarchical Localization and GLOMAPfor robotized harvesting

**Authors:** Fernando Cañadas-Aránega, José C. Moreno, José L. Blanco-Claraco, Francisco Rodríguez
**Links:** [abs](https://arxiv.org/abs/2609.11766) - [pdf](https://arxiv.org/pdf/2609.11766)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** structure from motion, SLAM, visual SLAM, mapping, localization

<details>
<summary>Abstract</summary>

Advanced crop monitoring inside greenhouses is becoming one of the primary objectives of research centers. High-performance sensors, such as LiDAR or stereo cameras, have traditionally been employed for this purpose, though these often have a high cost. This work proposes a Visual-SLAM system using a monocular camera, which is significantly more cost-effective and specifically tailored for agricultural applications, such as mapping tomato crops in a greenhouse. Tests were carried out on a real tomato bunch, located in the Agroconnect experimental greenhouse. A ROS 2 Humble node was developed to run on the robot in order to capture images of these crops, which were then stored for offline processing. To generate a 3D mapped model for the crop in the greenhouse, the GLOMAP mapper, based on Structure-From-Motion, was integrated with the Hierarchical Localization toolbox. This initial mapping is a foundation for future, more advanced algorithms to analyze growth patterns, and optimize agricultural management. The system leverages a hierarchical localization paradigm based on a coarse-to-fine strategy: it first performs global retrieval to generate location hypotheses, then combines local features within the identified candidate regions. The results show a correct identification of the tomato cluster, correctly characterising the tomato that is occluded and inaccessible by classical vision technologies. The reconstructed 3D model was further validated against manual ground-truth measurements of fruit size, centroid position, and orientation, confirming the geometric accuracy of the proposed low-cost monocular pipeline.

</details>

#### 2026-09-10 - RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting

**Authors:** Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen
**Links:** [abs](https://arxiv.org/abs/2609.11079) - [pdf](https://arxiv.org/pdf/2609.11079)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, depth estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, robot perception, localization

<details>
<summary>Abstract</summary>

Render--match--PnP relocalization establishes correspondences between query image pixels and 3D map points for camera pose recovery, but their potential to support dense depth estimation is often overlooked. To exploit this geometric information, we present RIDE, which estimates dense metric depth from a robot's RGB stream. Given a metrically scaled 3D Gaussian Splatting (3DGS) model, RIDE combines sparse metric depth observations derived from PnP-RANSAC inlier correspondences with the geometric prior of a pretrained video-depth model. To handle uneven and intermittent observations, it integrates global and local depth correction with temporal memory, supporting depth estimation through short observation gaps after metric scale initialization. Trained on public RGB-D videos, RIDE is evaluated on robot sequences without fine tuning. Experiments show improved depth accuracy and temporal consistency over scale-only calibration, demonstrating how localization geometry can support both pose recovery and dense robot perception.

</details>

#### 2026-09-09 - GRADE: Single-Frame Generative Radar Depth Estimation Under Visual Degradation

**Authors:** Bin Zhao, Patrick Chiou, Nakul Garg
**Links:** [abs](https://arxiv.org/abs/2609.10756) - [pdf](https://arxiv.org/pdf/2609.10756)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation

<details>
<summary>Abstract</summary>

Dense 3D depth perception fails under smoke, fog, and darkness because optical sensors cannot penetrate airborne particulates. mmWave radar remains usable and measures range accurately under these conditions, but its small aperture limits angular resolution. We present GRADE, which grounds a pretrained generative prior in single-frame radar geometry to estimate high-fidelity metric depth. GRADE first maps raw 4D radar spectra to coarse metric depth. A latent diffusion backbone then recovers structural detail while conditioning every denoising step on this estimate. A pixel-space adapter uses residual camera cues when available and is trained across clear, smoke-degraded, and occluded inputs so the full output approaches the radar-conditioned path as visibility degrades. Trained and evaluated on ~95K frames across 12 buildings with real smoke, GRADE achieves an MAE of 0.303 m in clear scenes and 0.313 m under smoke, outperforming existing baselines. Code and datasets are available at https://phi-lab-rice.github.io/GRADE.

</details>

#### 2026-09-09 - Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts

**Authors:** Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte
**Links:** [abs](https://arxiv.org/abs/2609.10498) - [pdf](https://arxiv.org/pdf/2609.10498)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts
- 作者：Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte
- 出版日期：2026-09-09T17:35:16Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.10498) / [PDF](https://arxiv.org/pdf/2609.10498)

### 一句话总结
该论文提出 Field Converter，通过相机与球场几何初始化球员根节点，并利用时序残差修正，实现从已标定足球转播中估计共享世界坐标系下的 3D 球员姿态。

### 研究问题
从单目体育转播中恢复 3D 人体姿态时，难点不仅在于相对自身身体的姿态重建，还在于需要将球员定位到共享的度量世界坐标系中。论文聚焦于从已标定的足球转播视频中进行世界坐标下的 3D 球员姿态估计。

### 核心思路/方法
- 使用相机和球场几何信息，通过射线-地面相交来初始化球员根节点。
- 在几何初始化基础上，预测时序残差修正。
- 残差预测使用姿态、图像、相机和几何线索。
- 在匹配不重叠的评估序列上，比较了不同时序骨干：逐帧 MLP、TCN 和 Transformer。

### 主要贡献
- 提出 Field Converter，一个几何初始化与时序残差修正结合的世界坐标 3D 球员姿态估计框架。
- 利用相机和球场几何进行根节点初始化，并通过时序残差修正降低根节点误差。
- 报告中，几何单独使根误差为 49cm，逐帧 MLP 降至 14cm，TCN 降至 10cm，Transformer 达到可比的 11cm；世界空间 MPJPE 达到 13.2cm。
- 消融显示，残差预测明显优于直接全局根节点回归；时序上下文比具体时序骨干更重要。
- 失败分析指出，空中动作是基于地面几何初始化的主要局限。

### 局限性
- 摘要明确指出失败分析发现空中动作是基于地面几何初始化的主要限制。
- 除空中动作外，其他局限性摘要未提供足够信息。
- 实验细节、数据集规模、跨场景泛化能力、计算成本等信息摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对足球转播中的世界坐标 3D 人体姿态估计，问题设定明确，且给出了根误差、MPJPE 和消融结论；如果关注体育视频分析、单目 3D 人体姿态或几何初始化方法，具有参考价值。但摘要未提供完整实验设置、数据规模和更广泛的泛化分析，是否高优先级取决于读者对足球转播场景的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Recovering 3D human pose from monocular sports broadcasts remains challenging when players must be localized in a shared metric world coordinate system rather than only reconstructed relative to their own body. We introduce Field Converter, a geometry-initialized temporal residual framework for world-grounded 3D player pose estimation from calibrated soccer broadcasts. Our method first uses camera and pitch geometry to initialize the player root through ray-ground intersection, then predicts a temporal residual correction from pose, image, camera, and geometric cues. On match-disjoint evaluation sequences, residual refinement reduces root error from 49cm with geometry alone to 14cm with a frame-wise MLP and 10cm with a TCN, while a Transformer achieves a comparable 11cm. The resulting world-space MPJPE reaches 13.2cm, and ablations show that residual prediction clearly outperforms direct global-root regression while temporal context matters more than the specific temporal backbone. Failure analysis further identifies airborne motion as the main limitation of the ground-based geometric initialization.

</details>

#### 2026-09-08 - Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion

**Authors:** Fadi Khatib, Meirav Galun, Ronen Basri
**Links:** [abs](https://arxiv.org/abs/2609.09491) - [pdf](https://arxiv.org/pdf/2609.09491)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, camera pose estimation, pose estimation, bundle adjustment, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion
- 作者：Fadi Khatib, Meirav Galun, Ronen Basri
- 出版日期：2026-09-08T22:14:03Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.09491

### 一句话总结
本文提出了一种基于可学习视图图聚合的深度全局 Structure-from-Motion 框架，用置换等变、边条件图神经网络从带噪相对位姿回归全局一致的相机外参。

### 研究问题
相机位姿估计是三维重建与视图合成流程中的关键步骤。论文关注如何从带噪声的视图图（view-graph）中学习全局相机位姿，以提升结构从运动（Structure from Motion）中位姿估计的精度、鲁棒性和效率。

### 核心思路/方法
方法核心是学习视图图聚合的深度、全局 Structure-from-Motion 框架：
- 使用置换等变、边条件图神经网络；
- 输入为带噪声的成对相对位姿；
- 输出为全局一致的相机外参；
- 训练不依赖真值监督，仅使用相对位姿一致性目标；
- 后续接三维点三角化和鲁棒 bundle adjustment。

### 主要贡献
- 提出基于学习视图图聚合的深度全局 Structure-from-Motion 框架。
- 设计置换等变、边条件图神经网络，从带噪相对位姿输出全局一致的相机外参。
- 无需真值监督，仅依赖相对位姿一致性目标进行训练。
- 方法高效、可扩展到超过一千张图像，并且对图密度鲁棒。
- 在 MegaDepth、1DSfM、Strecha 和 BlendedMVS 上评估，显示在旋转和平移精度上优于以深度轨迹为中心的方法，同时在许多场景中注册更多图像；与最先进的经典流程相比具有竞争力且速度更快。

### 局限性
摘要未提供足够信息。摘要未说明方法在何种场景或数据条件下会失败，未给出计算复杂度、内存占用、超参数敏感性、对极端噪声或异常值的具体限制，也未提供与经典流程比较的完整实验细节。

### 阅读优先级
高。理由：该论文直接面向三维重建与多视图几何中的核心问题，提出结合图神经网络与全局 Structure-from-Motion 的方法，并声称在多个标准数据集上取得精度、鲁棒性和速度优势；若研究兴趣涉及 SfM、相机位姿估计或图神经网络在三维视觉中的应用，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera pose estimation is a key step in 3D reconstruction and view-synthesis pipelines. We present a deep, global Structure-from-Motion framework based on learned view-graph aggregation. Our method employs a permutation-equivariant, edge-conditioned graph neural network that takes noisy pairwise relative poses as input and outputs globally consistent camera extrinsics. The network is trained without ground-truth supervision, relying solely on a relative-pose consistency objective. This is followed by 3D point triangulation and robust bundle adjustment. Our approach is efficient, scalable to more than a thousand images, and robust to graph density. We evaluate our method on MegaDepth, 1DSfM, Strecha, and BlendedMVS. These experiments demonstrate that our method achieves superior rotation and translation accuracy compared to deep track-centric methods while registering more images across many scenes, and competitive results compared to state-of-the-art classical pipelines, while being much faster.

</details>

#### 2026-09-08 - Prior-free relative 6D pose estimation of multiple object instances

**Authors:** Behdad Khodabandehloo, Andrea Caraffa, Davide Boscaini, Fabio Poiesi
**Links:** [abs](https://arxiv.org/abs/2609.08949) - [pdf](https://arxiv.org/pdf/2609.08949)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Prior-free relative 6D pose estimation of multiple object instances
- 作者：Behdad Khodabandehloo, Andrea Caraffa, Davide Boscaini, Fabio Poiesi
- 出版日期：2026-09-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08949

### 一句话总结
本文提出一种完全无需对象先验（无需CAD模型、模板或参考图像）的多实例未知对象相对6D姿态估计方法PROSE，利用多模态基础特征建立实例间对应关系并估计相对姿态。

### 研究问题
如何在没有任何对象特定先验的前提下，在同一图像中估计未知对象多个实例之间的相对6D姿态。

### 核心思路/方法
- 提出新方法PROSE：利用多模态基础特征在对象实例之间寻找粗略对应关系，无需训练。
- 通过跨实例元组的环一致性约束来细化对应关系，使对应关系全局一致。
- 利用细化后的全局一致对应关系估计任意实例对之间的相对6D姿态。
- 设计新基准PRENCH：基于三个多实例BOP数据集构建，并增补任务特定元数据以支持系统评估。

### 主要贡献
- 提出“prior-free相对6D姿态估计”这一新设定，去除了“知道场景中待估姿态的目标对象”这一假设。
- 提出无需训练、无需对象先验的PROSE方法，采用多模态基础特征与环一致性细化实现相对姿态估计。
- 构建了PRENCH基准，用于该新任务的系统评估。
- 在基准上，PROSE一致优于将现有单图像方法适配到该设定所得的基线，且无需任务特定监督或额外学习组件。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作将6D姿态估计推向“零先验”新范式，具有方向性创新意义；方法无需训练，结合基础模型特征，实用性强；并配套新基准，适合关注姿态估计、少样本/零样本视觉任务或基础模型应用的读者。

</details>

<details>
<summary>Abstract</summary>

Object 6D pose estimation formulations have progressively reduced reliance on object-specific priors, evolving from explicit 3D models to multi-view object captures to single reference images. We take this progression to its extreme by introducing prior-free relative 6D pose estimation, which lifts the assumption of knowing which object is to be posed within the scene. This novel setting aims to estimate the relative poses of multiple instances of an unknown object within the same image, without requiring CAD models, templates, or reference images. We solve this by formulating a novel method (PROSE) that finds coarse correspondences between object instances using multimodal foundation features, thus requiring no training. We refine these correspondences by imposing cycle consistency across tuples of instances, and leverage the resulting globally consistent correspondences to estimate the relative 6D pose between any pair of instances. To enable systematic evaluation, we design a novel benchmark (PRENCH) built from three multi-instance BOP datasets and enriched with task-specific metadata. PROSE consistently outperforms baselines obtained by adapting state-of-the-art single-image methods to the proposed setting, while requiring neither task-specific supervision nor additional learned components. Project website: https://tev-fbk.github.io/PROSE/

</details>

#### 2026-09-08 - FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute

**Authors:** Hongchi Xia, Tianhang Cheng, Wei-Chiu Ma, Shenlong Wang
**Links:** [abs](https://arxiv.org/abs/2609.08848) - [pdf](https://arxiv.org/pdf/2609.08848)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, scene representation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute
- 作者：Hongchi Xia, Tianhang Cheng, Wei-Chiu Ma, Shenlong Wang
- 出版日期：2026-09-08T15:01:49Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08848

### 一句话总结
FIRE3D 提出一个前馈端到端统一框架，可在一分钟内将单张 RGB 图像或随意 RGB 视频转化为面向游戏和交互应用的、仿真就绪的 3D 场景资产。

### 研究问题
如何在不进行测试时优化的前提下，快速（一分钟内）从单目 RGB 输入（单图或视频）重建出对象级完整、物理上可交互的仿真就绪 3D 场景。

### 核心思路/方法
- 以单个前馈端到端网络为核心，从输入的 RGB 采集数据中估计有姿态的 RGB-D 观测。
- 网络预测组合式场景表示，为每个对象输出 6-DoF 姿态、包围框、网格和纹理。
- 将场景建模为离散实体集合，从而生成“模态完整”（amodally complete）且仿真就绪的环境，其中的对象在物理上是解耦的、可直接交互。
- 无需测试时优化，直接前馈推理。

### 主要贡献
- 提出统一的单阶段前馈框架，可同时处理单张图像和视频输入。
- 相比先前的交互就绪方法，速度提升数个数量级，且无需测试时优化。
- 相比现有前馈 3D 方法，提供对象级别的完整性（模态完整），而非仅有场景级表面。
- 在多个数据集上，姿态精度、几何完整性和纹理质量达到具有竞争力或最优的结果，同时速度大幅领先。

### 局限性
摘要未提供足够信息（未明确讨论失败案例、输入约束、内存占用、对复杂场景或遮挡的鲁棒性等具体局限）。

### 阅读优先级
**高**。理由：该工作针对交互式 3D 场景重建这一活跃方向，提出了统一的端到端前馈方案，同时解决速度（分钟级）、对象级完整性和无测试时优化三个关键痛点，并声称在多个指标上达到先进水平。摘要中结果和效率优势明确，适合从事 3D 重建、仿真环境生成或交互应用相关研究的读者优先关注。

</details>

<details>
<summary>Abstract</summary>

We present FIRE3D, a unified framework that takes a single RGB image or casual RGB video and transforms it into simulation-ready 3D scene assets for games and interactive applications in under a minute. At the core of FIRE3D is a feed-forward, end-to-end network that predicts a compositional scene representation from posed RGB-D observations estimated from the RGB capture, including the 6-DoF pose, bounding box, mesh, and texture for every object. By modeling the scene as a collection of discrete entities, FIRE3D produces amodally complete and simulation-ready environments where objects are physically decoupled and ready for interaction. Our framework requires no test-time optimization, runs orders of magnitude faster than prior interaction-ready methods, and provides object-level completeness beyond existing feed-forward 3D approaches. We demonstrate competitive or state-of-the-art results across pose accuracy, geometry completeness, and texture quality across various datasets while being orders of magnitudes faster. Project page: https://xiahongchi.github.io/Fire3D/

</details>

#### 2026-09-08 - ArmPoser: Real-Time, Calibration-Free Arm Pose Estimation from Smartwatch IMU

**Authors:** Bishnu Dev, Vasco Xu, Xi-Aan Loh, Chenfeng Gao, Henry Hoffmann, Karan Ahuja
**Links:** [abs](https://arxiv.org/abs/2609.08806) - [pdf](https://arxiv.org/pdf/2609.08806)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ArmPoser: Real-Time, Calibration-Free Arm Pose Estimation from Smartwatch IMU
- 作者：Bishnu Dev, Vasco Xu, Xi-Aan Loh, Chenfeng Gao, Henry Hoffmann, Karan Ahuja
- 出版日期：2026-09-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08806

### 一句话总结
ArmPoser 提出一种无需用户校准、直接在智能手表原始 IMU 参考坐标系下训练的单手表手臂姿态估计系统，在公开基准与自采实验中匹配或超越需校准的基线方法。

### 研究问题
如何消除智能手表 IMU 手臂姿态估计中对用户校准（如校准姿势、骨偏移校准）的依赖，并避免因坐标变换和传感器漂移引入的误差，以支持日常场景下的稳定部署。

### 核心思路/方法
- **核心创新**：直接在消费级智能手表 IMU 数据固有的参考坐标系（设备原生轴）下训练模型，不再将原始测量量转换为标准化训练格式，从而省去坐标变换、显式对齐和骨偏移校准。
- **训练增强**：在训练中引入基于物理的腕表放置位置变化和手臂形态差异，以覆盖用户的个性化差异。
- **佩戴配置模块**：额外设计一个模块用于推断前臂朝向前/后（内外侧）以及表冠朝向，以辅助姿态估计。
- **评估方式**：在公开基准和一项包含 10 名参与者、30 项活动的真实实验（覆盖 watchOS 和 Android 智能手表）中验证系统性能。

### 主要贡献
1. 提出第一个无需校准的单智能手表 IMU 手臂姿态估计系统 ArmPoser。
2. 证明直接在设备原生参考坐标系训练模型可消除对校准流程和预处理管线的依赖。
3. 通过物理增强训练数据（腕表位置、手臂形态变化）提升对用户差异的鲁棒性。
4. 提出佩戴配置（前臂朝向与表冠方向）推断模块。
5. 在多项真实环境下与需校准的基线方法对比，ArmPoser 达到匹配或更优的性能。

### 局限性
摘要未提供足够信息，未明确说明系统在极端遮挡、快速运动或不同环境下的性能下降情况，也未提及计算成本、模型大小或电池消耗等部署细节。摘要未明确公开基准的具体名称、对比方法的配置及统计显著性分析。

### 阅读优先级
**高**。理由：该工作针对可穿戴 IMU 姿态估计中普遍存在的校准痛点，提出了一种直接贴合实际部署数据的训练范式，具有较强的实用价值；方法新颖性明确，且实验结果（含跨平台真实测试）为无校准方案的可行性提供了直接证据。发表于 2026 年，时效性高，适合对该方向感兴趣的研究者快速追踪前沿。

</details>

<details>
<summary>Abstract</summary>

Arm pose estimation enables applications in fitness, extended reality input, rehabilitation, and life logging. Prior smartwatch-based approaches rely on calibration poses and preprocessing pipelines that transform raw IMU measurements into standardized training formats. These steps hinder deployment in everyday settings and introduce errors due to imperfect calibration and sensor drift. We present ArmPoser, a calibration-free arm pose estimation system using a single smartwatch IMU. Our central contribution is training models directly in the reference frame native to consumer smartwatches, aligning learning with how IMU data is produced by deployed devices. By operating on device-native axes, ArmPoser removes the need for coordinate transformations, explicit alignment, and bone-offset calibration used in prior work. We further augment training with physically grounded variations in watch placement and arm morphology to account for user-specific variability. ArmPoser also includes a wear-configuration module that infers anterior or posterior forearm placement and crown orientation. We evaluate pose estimation on public benchmarks and on a 10-participant, 30-activity study using watchOS and Android smartwatches, where ArmPoser matches or exceeds calibrated baselines without any user calibration.

</details>

#### 2026-09-08 - MFVINS: Multiple Fisheye Camera-Based Visual Inertial System

**Authors:** Eunseong Jang, YuJin Chung, Sang Jun Lee, Jihyun Yoon, HyungGi Jo
**Links:** [abs](https://arxiv.org/abs/2609.08626) - [pdf](https://arxiv.org/pdf/2609.08626)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, bundle adjustment, depth estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MFVINS: Multiple Fisheye Camera-Based Visual Inertial System
- 作者：Eunseong Jang, YuJin Chung, Sang Jun Lee, Jihyun Yoon, HyungGi Jo
- 出版日期：2026-09-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08626

### 一句话总结
本文提出了一种基于多个鱼眼相机与IMU融合的视觉惯性系统MFVINS，通过IMU辅助的特征追踪、归一化平面去畸变外点过滤及带物理约束的重投影误差设计，提升了SLAM在遮挡与低纹理环境下的鲁棒性，并保持实时性。

### 研究问题
传统VINS仅使用单一相机作为视觉输入，在遮挡、光照变化和低纹理环境下容易出现误差累积，导致位姿估计精度下降。本文旨在利用多个鱼眼相机提升视觉惯性系统的鲁棒性，同时控制计算开销以实现实时运行。

### 核心思路/方法
- 构建多鱼眼相机+IMU的融合框架，扩展视野以应对遮挡和低纹理区域。
- 提出IMU辅助的FAST特征追踪器，用于多相机下的高效特征提取与鲁棒匹配。
- 在归一化图像平面上过滤由鱼眼畸变引起的外点。
- 提出带有物理有效性约束的新型重投影误差，并结合基于学习的深度估计用于束调整（bundle adjustment）。

### 主要贡献
- 提出了MFVINS，一个新颖的多鱼眼相机视觉惯性系统，兼顾鲁棒性与实时性。
- 设计了IMU辅助的多相机FAST特征追踪方法，提升特征提取与匹配效率。
- 在归一化图像平面上去除鱼眼畸变导致的外点，改善匹配质量。
- 引入带物理有效性约束的重投影误差用于束调整，并集成学习式深度估计。
- 在多种场景下与先前VINS方法比较，验证了方法的有效性，并实现了实时运行。

### 局限性
摘要未提供具体实验中的失败场景、计算资源需求、传感器配置细节（如鱼眼相机数量与布局）以及与其他方法的量化性能差异。摘要亦未提及方法在极端动态环境或大规模场景下的表现，因此这些方面的局限性无法判断。

### 阅读优先级
**中**  
理由：该研究面向多相机+IMU的SLAM系统，在鲁棒性设计（多鱼眼、畸变处理、深度学习深度融合）上有明确的新意，且强调实时性，对从事视觉惯性导航或多目SLAM的研究者有一定参考价值。然而，摘要缺乏定量实验对比细节，且发表于2026年，实际可用性和行业影响力仍需后续全文验证，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

A simultaneous localization and mapping (SLAM) method using a monocular camera and a low-cost inertial measurement unit (IMU) sensor is an effective way to fulfill a low-cost sensor configuration. Using this sensor configuration, visual-inertial system (VINS) focuses on fusing data from a camera and an IMU sensor to estimate the six degrees-of-freedom (DOF) of the sensor pose. Typically, VINS uses only a single camera as visual input, which lead to problems such as error accumulation due to occlusion, various illumination, and textureless environments. In this paper, we propose a new multiple fisheye camera-based visual-inertial system called MFVINS. We present an IMU-aided FAST feature tracker for multiple cameras that enables efficient extraction and robust matching of local features. Then, the proposed method filters out outliers caused by fisheye distortion on the normalized image plane. Subsequently, a new reprojection error with physical validity constraints is proposed for bundle adjustment using learning-based depth estimation. The proposed method is applied to various scenarios, and its effectiveness is demonstrated by comparing previous VINS methods. In particular, MFVINS is implemented in real-time process to leverage the advantages of using multiple cameras -- robustness against occlusion and textureless regions -- while reducing the computational burden.

</details>

#### 2026-09-08 - AURORA: Active Uncertainty-Driven Re-Orientation for In-Hand Reconstruction

**Authors:** Feiyu Zhao, Yuetong Li, Chenxi Xiao
**Links:** [abs](https://arxiv.org/abs/2609.08493) - [pdf](https://arxiv.org/pdf/2609.08493)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, geometric reconstruction, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AURORA: Active Uncertainty-Driven Re-Orientation for In-Hand Reconstruction
- 作者：Feiyu Zhao, Yuetong Li, Chenxi Xiao
- 出版日期：2026-09-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08493

### 一句话总结
AURORA是一个主动3D重建框架，通过在线重建与手内重定向的闭环控制，基于不确定性驱动选择下一次最佳观察视角以提高被遮挡物体的重建质量。

### 研究问题
机器人手抓取物体时存在严重的视觉遮挡，现有手内操作策略多依赖预定义或开环的重定向方式，未显式针对未被充分观察的区域。因此需要一种主动的视角选择与重建策略，在收据新观测数据的同时引导手部旋转，以高效完成物体重建。

### 核心思路/方法
- 提出主动在环框架，连接在线目标中心重建与手内重定向过程。
- 核心模块为Ray-GPIS，它沿候选观察光线估计各方向的重建不确定性，并利用“不确定性-新颖性”目标函数选择下一次最佳观察视角。
- 所选视角通过条件于轴的手内旋转策略执行。
- 新获得的RGB-D观测基于无CAD模型的6D位姿跟踪和轻量级几何重建进行增量融合。

### 主要贡献
- 提出主动闭环的AURORA框架，将重建不确定性直接驱动手内重定向决策。
- 设计Ray-GPIS，支持基于光线的方向性不确定性估计与高效主动视角规划。
- 实验表明AURORA相对于非主动旋转策略，在重建质量和信息获取效率方面均有提升。
- Ray-GPIS在重建性能、动作排序质量和规划效率上优于主动视角规划的基线方法。
- 针对手部遮挡和位姿误差等扰动进行了消融验证，表明系统具有一定鲁棒性。

### 局限性
摘要未提供足够信息，无法获取作者在计算开销、实时性能、物体类别范围、硬件依赖或失败模式等方面的局限分析。

### 阅读优先级
**高**
理由：该工作将主动感知与手内操作闭环结合，面向机器人抓取中实际且棘手的遮挡重建问题；方法兼具不确定性建模与视角规划的创新性，实验验证了相对基线的多方面提升，对机器人操纵、主动视觉与3D重建交叉方向具有较广泛参考价值。

</details>

<details>
<summary>Abstract</summary>

Observing objects grasped by a robot hand is challenging due to severe visual occlusions. Although in-hand manipulation can expose hidden surfaces, existing approaches often rely on predefined or open-loop reorientation strategies that do not explicitly target under-observed regions. We propose AURORA, an active 3D reconstruction framework that closes the loop between online object-centric reconstruction and in-hand reorientation. At its core, Ray-GPIS estimates direction-wise reconstruction uncertainty along candidate viewing rays and selects next-best-view targets using an uncertainty--novelty objective, which are realized through an axis-conditioned in-hand rotation policy. The resulting RGB-D observations are fused incrementally using CAD-free 6D pose tracking and lightweight geometric reconstruction. Experiments demonstrate that AURORA improves reconstruction quality and information-acquisition efficiency over non-active rotation strategies, while Ray-GPIS also outperforms active view-planning baselines in reconstruction performance, action-ranking quality, and planning efficiency. Targeted ablations further validate its robustness to hand occlusion and pose errors. The project webpage is available at https://aurorahand.github.io/

</details>

#### 2026-09-08 - Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation

**Authors:** Igor Pavlovic, Thiemo Wandel, Anton Obukhov, Luca Bartolomei, Andrey Davydov, Fabio Tosi, Matteo Poggi, Sabine Süsstrunk, Dengxin Dai
**Links:** [abs](https://arxiv.org/abs/2609.08084) - [pdf](https://arxiv.org/pdf/2609.08084)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, depth estimation, monocular depth, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation
- 作者：Igor Pavlovic, Thiemo Wandel, Anton Obukhov, Luca Bartolomei, Andrey Davydov, Fabio Tosi, Matteo Poggi, Sabine Süsstrunk, Dengxin Dai
- 出版日期：2026-09-08
- 分类：3D重建与多视角几何
- 链接：https://arxiv.org/abs/2609.08084

### 一句话总结
本文提出Marigold V2，通过改进训练策略和损失函数，将扩散Transformer（DiT）模型高效转化为高性能的单目深度估计器，在泛化性、细节清晰度和多任务适用性上超越此前最优方法。

### 研究问题
如何在保持模型容量和运行效率的前提下，将预训练的图像生成/编辑扩散模型（基于DiT架构）重新用于单目深度估计，并解决现有方法在分布外泛化和深度图细节质量上的不足。

### 核心思路/方法
- 基于Marigold已有技术框架，提出针对DiT架构的改进配方，支持从预训练多步流匹配模型进行单步推理，并在需要时引入量化，以降低运行成本。
- 分析朴素训练产生的伪影，提出两种有效修正：一是将模型内部表示与从真值中提取的语义特征对齐；二是采用两阶段微调协议，并引入新颖的基于Sinkhorn的损失函数。

### 主要贡献
- 提出Marigold V2的全套技术方案，显著提升单目深度估计的分布外泛化能力和输出质量。
- 在KITTI和ETH3D基准上，AbsRel指标较此前最优提升16-26%。
- 定性上能恢复毛发、树叶、发丝级细边缘等此前模型难以处理的细节。
- 该方法可迁移至其他密集回归任务（如表面法线估计和固有图像分解），并取得最优结果。

### 局限性
摘要未提供足够信息。文中未明确讨论计算资源需求、失败案例、对极端输入的限制、训练数据依赖性或与其他方法在同等条件下的完整对比细节。

### 阅读优先级
**高**。理由：该方法在核心基准上带来显著量化提升（16-26%），并展示跨任务泛化能力；面向单目深度估计乃至密集预测任务的研究者具有直接参考价值，且基于扩散模型的高效推理方案也具有实用意义。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation is a ubiquitous yet highly ill-posed computer vision task, with downstream applications in scene reconstruction, computational photography, and robotics, among others. Despite the field's maturity, recent models still struggle to generalize to out-of-distribution inputs and to produce sharp and detailed depth maps. In this paper, we revisit Marigold, a set of techniques for repurposing modern image generation and editing models, powered by the diffusion transformer (DiT) architecture, into state-of-the-art monocular depth estimators. Our recipes target single-step inference from pretrained multi-step flow-matching models, with quantization where needed, preserving model capacity while remaining cheap to run. We analyze the artifacts of naive training and identify two effective remedies: aligning the model's internal representations with semantic features extracted from ground-truth, and adopting a 2-stage fine-tuning protocol built around a novel Sinkhorn-based loss. The results are crisper, cleaner depth maps that generalize well out-of-distribution, with 16-26% improvement in AbsRel over the previous best on KITTI and ETH3D. Qualitatively, our model resolves fur, foliage, and hair-thin edges that have eluded prior models. Furthermore, Marigold V2 achieves state-of-the-art results when applied to other dense regression tasks, such as surface normals estimation and intrinsic image decomposition. Project website: https://hf.co/spaces/huawei-bayerlab/marigold-v2-web

</details>

#### 2026-09-07 - A Black-Box Adversarial Attack on Human Pose Estimation and Keypoint-Based Action Recognition Models

**Authors:** Kacper Mroczek, Michal Kepski
**Links:** [abs](https://arxiv.org/abs/2609.08013) - [pdf](https://arxiv.org/pdf/2609.08013)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Black-Box Adversarial Attack on Human Pose Estimation and Keypoint-Based Action Recognition Models
- 作者：Kacper Mroczek, Michal Kepski
- 出版日期：2026-09-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08013

### 一句话总结
该论文提出一种基于OKS（Object Keypoint Similarity）反馈信号的决策级黑盒对抗攻击方法OKS Attack，用于针对人体姿态估计及基于关键点的动作识别模型，并在Penn Action数据集上验证其有效性。

### 研究问题
人体姿态估计和基于关键点的动作识别模型容易受到对抗攻击，但现有黑盒攻击方法多采用边界框重叠度量（如IoU）作为反馈，而姿态估计输出关键点结构而非包围框，导致框级相似度不适合衡量姿态退化。因此，研究如何设计一种直接针对人体姿态空间结构的黑盒对抗攻击方法。

### 核心思路/方法
提出OKS Attack，一种基于决策的黑盒对抗攻击方法。其核心是利用对象关键点相似度（OKS）替代IoU作为攻击反馈信号，从而直接度量并优化姿态估计结果的退化程度。攻击过程无需模型内部梯度信息，仅依赖查询得到的预测关键点反馈。

### 主要贡献
- 首次（摘要暗示）将OKS作为黑盒攻击反馈信号用于姿态估计任务，弥补框级相似度在关键点场景下的不适配问题。
- 在Penn Action数据集上的实验表明，OKS Attack能持续降低多个姿态估计器的姿态质量（平均OKS下降0.0802至0.1494）。
- 在跨数据集的下游动作识别评估中，攻击使识别准确率下降6.18至13.86个百分点，且优于查询匹配的随机噪声扰动。
- 攻击在自上而下和单阶段两种姿态估计模型上均有效。
- 将公开源代码（GitHub链接已在摘要中提供）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该研究填补了姿态估计任务在黑盒对抗攻击方面的空白，方法定义清晰且实验实证效果显著，对视频理解安全领域有一定参考价值；但创新点集中于攻击反馈信号的选择（OKS替换IoU），属于对既有黑盒攻击框架的适配性调整，可能对纯攻击方法学研究者吸引力更大，对交叉领域读者优先级中等。

</details>

<details>
<summary>Abstract</summary>

Human pose estimation and keypoint-based action recognition models are increasingly deployed as components of video understanding pipelines, yet their vulnerability to adversarial attacks remains insufficiently studied. Temporally coherent black-box attacks have been previously studied in visual object tracking, where the attack feedback can be defined using bounding-box overlap measures such as Intersection over Union (IoU). However, human pose estimation produces keypoint configurations rather than enclosing boxes, making box-level similarity poorly suited for measuring pose degradation. We propose OKS Attack, a decision-based black-box attack that uses Object Keypoint Similarity (OKS) as the attack feedback signal, directly targeting the spatial structure of human poses rather than their enclosing boxes. Experiments on the Penn Action dataset show that OKS Attack consistently reduces pose quality across evaluated pose estimators, with mean OKS decreases ranging from 0.0802 to 0.1494. In a downstream cross-dataset action-recognition evaluation, the attack reduces accuracy by 6.18 to 13.86 percentage points and outperforms query-matched random-noise perturbations. The attack is effective across both top-down and single-stage pose estimation models. The source code will be made publicly available at https://github.com/KacperM33/OKS_attack

</details>

#### 2026-09-07 - Are Image Generators Zero-Shot Perceivers? A Rigorous Evaluation

**Authors:** Shangzhe Di, Zhaokai Wang, Weidi Xie
**Links:** [abs](https://arxiv.org/abs/2609.07884) - [pdf](https://arxiv.org/pdf/2609.07884)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Are Image Generators Zero-Shot Perceivers? A Rigorous Evaluation
- 作者：Shangzhe Di, Zhaokai Wang, Weidi Xie
- 出版日期：2026-09-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.07884

### 一句话总结
本文提出ProbeGen基准，系统评估了20个图像生成器在零样本条件下执行深度估计、分割和计数等视觉感知任务的性能，发现其具备一定感知能力但与传统专家模型存在清晰权衡。

### 研究问题
预训练图像生成器在零样本设置下，能在多大程度上完成多种公开的视觉感知基准任务（如单目深度估计、指称/推理分割和目标计数）？它们的表现相对于专用感知模型和多模态大语言模型（MLLM）如何？

### 核心思路/方法
- 构建ProbeGen基准：将视觉感知任务（深度估计、分割、计数）转化为基于文本提示的条件生成任务，以便在统一的生成式框架下评估。
- 在11个已发表的基准上，总计比较20个模型，涵盖专有和开源权重的图像生成器、专用感知模型以及多模态大语言模型。
- 在零样本条件下评估各类模型的感知能力，并分析不同模型族群的表现差异。

### 主要贡献
- 提出ProbeGen，一个专门用于零样本生成式感知评估的基准，覆盖三类视觉感知任务。
- 首次对20个模型（包括多种生成器、专用模型和MLLM）进行系统性跨基准比较。
- 实证发现：预训练图像生成器展现出可测量的零样本感知能力，但存在明显权衡——专用模型在分布内准确性和效率上更强，而生成模型在分布漂移下更鲁棒，并更擅长组合语义推理。
- 为“零样本生成式感知”这一研究方向提供实证基础和未来研究框架。

### 局限性
摘要未提供足够信息用以说明具体实验限制（如任务划分细节、评估偏差、模型特定失败案例等）。仅能从摘要推断：该研究聚焦于零样本设定，可能未涵盖微调/适配后的生成器性能，且具体任务定义依赖文本条件化，可能无法完全等价于传统感知任务。其他局限性（如计算成本、基准覆盖范围）摘要未提及，需要阅读全文确认。

### 阅读优先级
**高**  
理由：该工作首次系统评估图像生成器的零样本感知能力，提出了统一的基准ProbeGen并覆盖多类任务和20个主流模型，主题处于生成与感知交叉的前沿，对理解生成模型的下游潜力具有重要参考价值。若你对视觉生成、多模态理解和基准构建感兴趣，此文值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent work, such as Vision Banana, shows that lightweight instruction tuning can enable an image generator to achieve state-of-the-art performance across multiple visual perception tasks. Motivated by this perspective, we ask how far image generators can go on public visual perception benchmarks in a zero-shot setting. We introduce ProbeGen, a benchmark for zero-shot generative perception that casts monocular depth estimation, referring/reasoning segmentation, and object counting as conditional generation tasks specified through text prompts, and compares 20 models in total---including proprietary and open-weight image generators, specialist perception models, and MLLMs---across 11 published benchmarks. We observe that pretrained image generators show measurable zero-shot perceptual competence, but with a clear trade-off: specialist models remain stronger for in-distribution accuracy and efficiency, while generative models are often more robust under distribution shift and better at compositional semantic reasoning. We hope this study helps establish zero-shot generative perception as a meaningful research direction and provides a useful foundation for future work at the intersection of visual generation and understanding.

</details>

#### 2026-09-07 - Functional-SLAM: Interaction-Aware Mapping with Online Functional Scene Graphs

**Authors:** Xinggang Hu, Chenyangguang Zhang, Zihan Zhu, Ruida Zhang, Xiangkui Zhang, Xiangyang Ji
**Links:** [abs](https://arxiv.org/abs/2609.07497) - [pdf](https://arxiv.org/pdf/2609.07497)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, pose estimation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Functional-SLAM: Interaction-Aware Mapping with Online Functional Scene Graphs
- 作者：Xinggang Hu, Chenyangguang Zhang, Zihan Zhu, Ruida Zhang, Xiangkui Zhang, Xiangyang Ji
- 出版日期：2026-09-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.07497

### 一句话总结
Functional-SLAM 提出首个在线递归维护功能场景图的 SLAM 框架，将功能关系建模融入实时建图过程，以支持细粒度机器人交互。

### 研究问题
现有 SLAM 系统缺乏对功能关系的建模，无法支撑细粒度的机器人交互；而现有的功能 3D 场景图方法依赖离线重建，难以用于真实场景中的实时交互探索。因此目标是在线实时构建并维护功能场景图。

### 核心思路/方法
- 将功能场景图作为在线 SLAM 状态，持续递归地维护节点与边。
- 结合 anchor-keyframe 几何与功能上下文约束，实现持久节点维护。
- 通过时间关系累积多帧证据，提交稳定功能边。
- 在视觉回环检测中，利用功能拓扑作为补充线索，处理外观重复或纹理退化场景。

### 主要贡献
- 提出 Functional-SLAM，首个在线持续维护功能场景图的 SLAM 框架。
- 相比离线方法显著提升运行效率，同时保持较高精度。
- 在几何回环基础上引入功能拓扑辅助，进一步提升位姿估计精度。
- 提供公开代码。

### 局限性
摘要未提供足够信息，无法确认方法在动态物体、大规模场景、计算资源消耗或长期漂移等方面的具体局限性。

### 阅读优先级
**高**。理由：该工作首次将功能场景图纳入在线 SLAM 状态，直接填补了实时交互建图与功能语义建模之间的空白，对机器人交互与 SLAM 交叉方向具有较强的新颖性和应用价值，且已在精度与效率上报告了正面结果。

</details>

<details>
<summary>Abstract</summary>

Existing SLAM systems lack modeling of the functional relations required for fine-grained robotic interaction. Functional 3D scene graphs can represent relations between objects and interaction elements, but existing methods rely on offline reconstruction, making them inadequate for real-time interaction in real-world exploration. To address this limitation, we propose Functional-SLAM, the first framework that continuously and recursively maintains a functional scene graph as an online SLAM state. The framework combines anchor-keyframe geometry with functional-context constraints for persistent node maintenance, accumulates multi-frame evidence through temporal relations to commit stable functional edges, and supplements visual loop-closure candidates with functional topology in scenes with repetitive appearance or degraded texture. Experiments show that Functional-SLAM efficiently constructs stable functional maps online, substantially improving runtime over offline methods while maintaining highly competitive accuracy. Compared with peer SLAM systems, it further improves pose estimation accuracy through functional-topology-assisted loop closure. The code is publicly available at https://github.com/Hbelief1998/Functional-SLAM-CoRL_2026.

</details>

#### 2026-09-07 - Generalizable 6D Pose Estimation of Textureless Objects with Planar-based Gaussian Splatting

**Authors:** Jie Lu, Hengtan Zhang, Li Gong, Pengpeng Wang, Xianjia Yu, Jinxiang Deng, Tomi Westerlund, Zhongxue Gan, Lirong Zheng, Zhuo Zou
**Links:** [abs](https://arxiv.org/abs/2609.07231) - [pdf](https://arxiv.org/pdf/2609.07231)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** pose estimation, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Generalizable 6D Pose Estimation of Textureless Objects with Planar-based Gaussian Splatting
- 作者：Jie Lu, Hengtan Zhang, Li Gong, Pengpeng Wang, Xianjia Yu, Jinxiang Deng, Tomi Westerlund, Zhongxue Gan, Lirong Zheng, Zhuo Zou
- 出版日期：2026-09-07T08:49:10Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：[摘要](https://arxiv.org/abs/2609.07231) | [PDF](https://arxiv.org/pdf/2609.07231)

### 一句话总结
PG-Pose 利用基于平面约束的高斯泼溅重建和几何驱动的位姿优化，在无 CAD 模型条件下实现了对无纹理物体的高精度、可泛化的 6D 位姿估计。

### 研究问题
如何在没有 CAD 模型且物体缺乏纹理特征的条件下，实现可泛化的 6D 位姿估计——现有通用方法在低纹理物体上精度不足，主要受限于底层表示的几何约束不充分。

### 核心思路/方法
整体框架分为两个阶段：**离线表示提取阶段**，利用多视角 RGB 参考图和已知位姿提取三种对象表示，通过 3D 高斯泼溅重建并渲染高保真深度图后反投影生成 3D 点云；**在线位姿推理阶段**，先在输入图像与重建的 3D 点云之间进行 2D-3D 对应匹配估计初始位姿，再由 PGS-Refiner 执行迭代位姿优化。

### 主要贡献
- 提出 PG-Pose：结合基于平面的高斯泼溅（PGS）重建与几何驱动位姿优化的几何感知框架，用于无纹理物体的可泛化 6D 位姿估计。
- 在 OnePose-LowTexture 数据集上，PG-Pose 达到 94.2% 的平均 ADD(S)@0.1d 精度，较 SOTA 高斯泼溅类方法平均精度提升 2.1%。
- 在双机械臂工业机器人上完成实际部署，成功实现对未见物体的抓取任务，验证了实用价值。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法在极端光照、严重遮挡、大规模工业场景中的性能上限，也未提及计算开销或实时性限制，以及解算失败或精度下降的具体边界条件。

### 阅读优先级
**高**。理由：本文针对无纹理物体 6D 位姿估计这一实际工业痛点，在无 CAD 模型条件下将高斯泼溅与几何优化结合，在数据集上取得 SOTA 提升，并在真实双机械臂抓取任务中得到验证，同时覆盖重建、渲染、位姿优化与机器人应用多个维度，对于从事三维视觉、机器人操作及可泛化感知的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Estimating the 6D pose of textureless objects without prior CAD models remains a critical challenge due to the lack of appearance features. While recent generalizable approaches alleviate the dependence on object-specific models, their performance on low-texture objects is often limited by insufficient geometric constraints in the underlying representations. In this work, we propose PG-Pose, a geometry-aware framework combining Planar-based Gaussian Splatting (PGS) reconstruction and Geometry-driven pose optimization. In the offline representation extraction stage, three distinct representations of the object are extracted from multi-view reference RGB images with known poses. PG-Pose reconstructs a 3D Gaussian representation and renders high-fidelity depth maps to generate 3D point clouds through back projection. In the online pose inference stage, the initial pose of the input image is estimated by 2D-3D correspondence matching between the input image and the reconstructed 3D point clouds, followed by a PGS-Refiner for iterative pose optimization. Evaluations on the OnePose-LowTexture datasets, PG-Pose achieves an average accuracy of 94.2% ADD(S)@0.1d, with a 2.1% improvement average accuracy compared with the state-of-the-art (SOTA) GS-based approach. To further demonstrate the effectiveness of PG-Pose for industrial robots in grasping tasks, we deploy it on a dual-arm industrial robot and successfully realize the grasping task on an unseen object.

</details>

#### 2026-09-06 - Back to the Feature: Zero-Shot 6DoF Pose Estimation via Dense Local Features

**Authors:** Ali Rafiaei, Michael Greenspan
**Links:** [abs](https://arxiv.org/abs/2609.06726) - [pdf](https://arxiv.org/pdf/2609.06726)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, feature matching, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Back to the Feature: Zero-Shot 6DoF Pose Estimation via Dense Local Features  
- 作者：Ali Rafiaei, Michael Greenspan  
- 出版日期：2026-09-06  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2609.06726  

### 一句话总结
提出B2TFPose，一种仅依赖冻结DINOv3视觉Transformer提取稠密局部特征、无需训练的零样本6DoF姿态估计方法，在BOP基准上达到训练无关RGB方法的最优性能。

### 研究问题
如何在无需针对特定物体微调或额外训练的情况下，仅利用RGB图像对未见物体进行准确的6DoF姿态估计，并跨越合成到真实的域差距。

### 核心思路/方法
- 使用单个冻结的DINOv3视觉Transformer作为唯一预训练组件，提取可跨合成-真实域泛化的稠密patch级特征，回归经典局部特征匹配范式。  
- 三项关键技术：  
  1. 测地线非极大值抑制（geodesic NMS）选取视角多样的模板集，进行粗到细的对应匹配。  
  2. 渲染引导的再对应（RRC）：在估计姿态处合成物体特定视角，重新建立稠密2D-3D对应以锐化初始估计，无需额外学习参数。  
  3. 多掩膜假设选择策略：联合评分多个分割候选以解决分割歧义。

### 主要贡献
- 提出完全无需训练的零样本6DoF姿态估计方法B2TFPose。  
- 三项技术（测地线NMS模板选择、RRC细化、多掩膜假设选择）共同推动训练无关方法的最优水平。  
- 在BOP Benchmark七个核心数据集上，无细化时平均AR为40.7，细化后达56.4，超越训练方法GigaPose和GenFlow，且推理速度有竞争力。

### 局限性
摘要未提供足够信息（未提及失败案例、对遮挡/纹理缺失物体的表现、对DINOv3特征的依赖范围或计算资源需求等具体局限）。

### 阅读优先级
**高**  
理由：该方法在零样本训练无关RGB姿态估计上达到最先进水平，并超越了若干有训练方法，具备较强的实用性和新颖性；结合基础模型特征与经典匹配范式的研究方向具有启发意义，适合计算机视觉、机器人操作与增强现实相关研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

We present B2TFPose, a training-free zero-shot method for 6DoF pose estimation of unseen objects from RGB images. Using a single frozen DINOv3 vision transformer as its only pretrained component within the pose estimation pipeline, B2TFPose extracts dense patch-level features that generalize across the synthetic-to-real domain gap without any task-specific fine-tuning, revisiting the classical local feature matching paradigm through the lens of large-scale self-supervised foundation models. Three contributions advance the training-free state of the art. A geodesic non-maximum suppression strategy retrieves a viewpoint-diverse template set for coarse-to-fine correspondence matching. Render-guided Re-Correspondence (RRC) synthesizes object-specific views at the estimated pose and re-establishes dense 2D-3D correspondences to sharpen the initial estimate without additional learned parameters. A multi-mask hypothesis selection strategy jointly scores competing segmentation candidates to resolve segmentation ambiguity. On the seven core datasets of the BOP Benchmark, B2TFPose achieves 40.7 mean AR without refinement and 56.4 with refinement, establishing state-of-the-art performance among training-free RGB methods and outperforming trained counterparts including GigaPose and GenFlow, at competitive inference speed.

</details>

#### 2026-09-04 - CrossDepth: Geometry-Constrained Attention for Generalizable Multi-View Surround Depth Estimation

**Authors:** Samer Abualhanud, Max Mehltretter
**Links:** [abs](https://arxiv.org/abs/2609.05397) - [pdf](https://arxiv.org/pdf/2609.05397)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CrossDepth: Geometry-Constrained Attention for Generalizable Multi-View Surround Depth Estimation
- 作者：Samer Abualhanud, Max Mehltretter
- 出版日期：2026-09-04
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.05397

### 一句话总结
CrossDepth 提出一种基于几何约束注意力的多视角环视深度估计方法，通过相机感知射线嵌入与跨图像注意力提升深度精度与跨图像一致性，并在 DDAD 和 nuScenes 上优于现有自监督方法。

### 研究问题
在多视角环视相机系统中，相邻图像重叠极小，导致大多数像素的深度需要依赖单目外观线索推断；然而这些线索在不同图像间可能表现不一致（受相机内参差异和每张图像感受野有限影响），从而造成跨图像深度估计不一致。

### 核心思路/方法
- 针对相机内参差异：在特征上引入逐像素的相机感知射线嵌入，让网络适应相机相关的外观线索变化。
- 针对感受野有限：通过几何约束的跨图像注意力机制，将每个像素的上下文扩展到自身图像之外，仅关注由标定系统导出的几何合理区域。
- 训练方式：全自监督，基于光度一致性（photometric consistency）进行训练。

### 主要贡献
- 提出相机感知射线嵌入，以缓解不同相机内参导致的单目线索解释差异。
- 设计几何约束的跨图像注意力，在标定约束下扩展像素上下文，提升跨图像深度一致性。
- 在 DDAD 和 nuScenes 上的域内与跨域评估中，整体深度精度和跨图像一致性均优于现有自监督方法。
- 代码已公开。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法面向自动驾驶环视深度估计，提出可泛化的跨图像一致性改进思路，属于应用导向的增量创新；但摘要未给出具体数值比较或消融细节，适用性与改进幅度需进一步阅读原文验证。若您关注多视角几何或自监督深度估计方向，可考虑优先阅读。

</details>

<details>
<summary>Abstract</summary>

Reliable 3D understanding of the surrounding environment is a core requirement for autonomous driving. Multi-view surround camera rigs provide broad scene coverage, but the spatially adjacent images typically overlap only minimally. Consequently, the depth of most pixels must be inferred from monocular appearance cues. These cues can appear differently across images and may therefore be interpreted differently by the depth estimation model. We target two main sources of cross-image inconsistency: differences in camera intrinsics and the limited receptive field of each image. We address the former by conditioning the features on per-pixel camera-aware ray embeddings, enabling the network to account for camera-dependent variations in monocular cues. We address the latter by extending each pixel's context beyond its own image through cross-image attention constrained to geometrically plausible regions, derived from the calibrated rig setup. The model is trained in a fully self-supervised manner based on photometric consistency. Evaluations on DDAD and nuScenes show improved overall depth accuracy and cross-image depth consistency over state-of-the-art self-supervised methods under in-domain and cross-domain evaluation. Code is available at https://abualhanud.github.io/CrossDepthPage/.

</details>

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-10 - 3D Point Splatting for mmWave Radar Novel View Synthesis

**Authors:** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar
**Links:** [abs](https://arxiv.org/abs/2609.11894) - [pdf](https://arxiv.org/pdf/2609.11894)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-view optimization NVS demands. Optical-NVS ports of NeRF, hash grids, and 3D Gaussians train fast but discard phase and replace explicit material modeling with opaque learned features, restricting them to power-only range-azimuth (RA) magnitudes. We propose 3D Point Splatting (3DPS), the first differentiable point renderer for radar, derived directly from the standard solid-angle form of the radar equation. Each oriented 3D point carries an ITU-R P.2040 material model, evaluated in closed form, with the resulting complex phasor splatted into range bins through a precomputed point spread function (PSF). The complex-valued output makes the renderer product-agnostic. The same optimized scene yields analog-to-digital converter (ADC), complex range profile (CRP), and RA outputs through standard fast Fourier transform (FFT) pipelines without retraining for each format. On six outdoor ColoRadar scenes, 3DPS reaches 0.587 mean Pearson correlation on held-out RA images. This is between 1.7x and 5.2x the three optical-NVS baselines (RadarSplat, Radar Fields, DART). Training takes approximately 3 minutes per scene on a single RTX 4090.

</details>

#### 2026-09-10 - Hologram Representation via Quadratic Phase Gaussian Splatting

**Authors:** Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu
**Links:** [abs](https://arxiv.org/abs/2609.11434) - [pdf](https://arxiv.org/pdf/2609.11434)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

We introduce Complex-Valued Quadratic Phase Gaussian (CVQPG), a novel hologram representation method that replaces standard 2D Gaussian representations used in 2D Gaussian Splatting with 2D quadratic phase functions. CVQPG incorporates additional learnable parameters to control the curvature of these bases. We evaluate our approach against state-of-the-art methods, exceeding the visual quality by +0.19 dB (RGB) and +0.33 dB (grayscale) on average in holographic reconstructions. Specifically, our equal parameter count evaluations show that modulating the primitive's wavefront is an effective and lightweight enhancement for hologram representations. In addition, our frequency domain analysis illustrates that CVQPG has successfully preserved the mid-to-high frequency band of natural images.

</details>

#### 2026-09-10 - Tri-DehazeGS: Scene--Medium Decoupled Gaussian Splatting with Transmittance-Aware Optimization

**Authors:** Kui Jiang, Yang Gu, Jiacheng Liu, Shiyu Liu, Youyu Chen, Hui Liu
**Links:** [abs](https://arxiv.org/abs/2609.11223) - [pdf](https://arxiv.org/pdf/2609.11223)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

Recovering clean 3D scenes from hazy multi-view images is challenging because haze attenuates scene radiance and introduces atmospheric scattering. Recent scattering-aware Gaussian Splatting methods introduce physical haze models into reconstruction, but they often apply degradation in image space or bind medium-related variables to Gaussian primitives, which can entangle clean scene radiance with atmospheric effects. Moreover, low-transmittance regions provide weakened supervision for Gaussian optimization, causing distant or dense-haze areas to be under-reconstructed. We argue that clean reconstruction under haze requires both scene--medium disentanglement and transmittance-aware optimization rebalancing. To this end, we propose Tri-DehazeGS, a scene--medium decoupled Gaussian Splatting framework. It represents the clean scene with Gaussian primitives, models the participating medium using an independent view-shared tri-plane field, and composes hazy observations through a physical scattering model. We further introduce Medium-Decoupled Transmittance Gradient Compensation (MD-TGC), which compensates haze-suppressed gradients after medium freezing without altering forward rendering. Experiments on real and synthetic haze benchmarks show that Tri-DehazeGS improves clean novel-view reconstruction. Code is available at https://github.com/aptx46/Tri-DehazeGS.

</details>

#### 2026-09-09 - View-Structured Conformal Prediction for 3D Gaussian Splatting

**Authors:** Junzheng Chu, Bin Pan, Zhenwei Shi
**Links:** [abs](https://arxiv.org/abs/2609.10307) - [pdf](https://arxiv.org/pdf/2609.10307)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：View-Structured Conformal Prediction for 3D Gaussian Splatting
- 作者：Junzheng Chu, Bin Pan, Zhenwei Shi
- 出版日期：2026-09-09T15:16:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.10307 ；PDF https://arxiv.org/pdf/2609.10307

### 一句话总结
论文提出视图结构化的共形预测方法 VSCP，将新视图合成的 RGB 预测框覆盖率问题建模为结构化回归，通过把预校准尺度分解为空间形状与可迁移的视图难度因子，在跨场景迁移下实现有限样本有效的视图级覆盖率保证。

### 研究问题
3D Gaussian Splatting 能实时渲染新视图，但仅给出不确定性热图并不能证明渲染视图满足特定预测覆盖率。论文要求：以至少 \(1-\alpha\) 的概率，RGB 预测框覆盖新视图中至少 \(1-\beta\) 比例的像素。摘要指出，按像素汇总校准在 90% 目标下像素级边际覆盖可达 89.9%，但视图事件覆盖率仅 61.4%，说明需要视图级有效的校准方法。

### 核心思路/方法
论文将新视图合成视为结构化回归，并提出 View-Structured Conformal Prediction（VSCP）。方法把预校准尺度拆分为两部分：来自渲染器的空间形状，以及可迁移的视图难度因子，后者用于预测该形状所需的最小视图级乘数。随后在视图上使用留出分位数（View-CP），即使在迁移到新场景时也能提供有限样本有效性。同一分解还使分析精确化：一致性分数是 oracle 视图难度与预测视图难度的比值，超额宽度可分解为测试侧项和校准侧项。

### 主要贡献
- 提出 VSCP，将新视图合成建模为结构化回归，并给出视图级覆盖的共形预测框架。
- 通过空间形状与可迁移视图难度因子的分解，结合视图上的留出分位数，实现跨新场景迁移时的有限样本有效性。
- 给出精确分析：一致性分数为 oracle 与预测视图难度之比，超额宽度分解为测试侧与校准侧两项。
- 在 13 个真实场景中，View-CP 达到 91.7–92.0% 视图事件覆盖率，而像素汇总校准仅 61.4%（90% 目标下）。
- 在匹配覆盖率下，VSCP 相对常数尺度将宽度减少 22.1%，并以每场景单模型、每次查询四次光栅化匹配十模型集成 21.0% 的宽度缩减；相对最接近的单模型基线 3DGS-U 提升 4.7 个点（\(p=0.0225\)）。
- 视图预测器可从有界源族迁移到全部九个无界 Mip-NeRF 360 场景；完整尺度在全部九个场景上相对常数尺度节省 20.7% 宽度，在不同稠密化骨干下仍保持 18.3% 节省，并在 RTX 4090 上以 216–280 FPS 运行。

### 局限性
摘要未提供足够信息说明方法在更广泛数据集、不同 \(\alpha\) 与 \(\beta\) 组合、极端场景或计算资源受限条件下的表现；摘要未提供足够信息说明其失败情形或与更多基线方法的全面比较。摘要未提供足够信息说明理论假设的完整边界与潜在违反条件。

### 阅读优先级
高。理由：该论文针对 3DGS 新视图合成中的不确定性认证问题提出视图级共形预测方法，直接回应像素级校准与视图级覆盖之间的差距；摘要给出了明确的覆盖率目标、跨场景迁移结果、宽度缩减、与基线比较、运行速度以及不同骨干下的表现，问题重要且结果信息量较大，适合优先阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) renders novel views in real time, but an uncertainty heatmap does not certify that a rendered view meets a certain prediction coverage. We treat novel-view synthesis as structured regression and ask that, with probability at least $1-α$, RGB prediction boxes cover at least a $1-β$ fraction of pixels in a new view. We propose View-Structured Conformal Prediction (VSCP). It splits the pre-calibration scale into a spatial shape from the renderer and a transferable view-difficulty factor, which predicts the smallest view-wise multiplier that shape needs. A held-out quantile over views (View-CP) then gives finite-sample validity even when transferring to new scenes. The same factorization makes the analysis exact: a conformity score is the ratio of oracle to predicted view difficulty, and excess width separates into a test-side and a calibration-side term. Across 13 real scenes, pixel-pooled calibration reaches 89.9\% marginal pixel coverage but only 61.4\% view-event coverage at a 90\% target, while View-CP reaches 91.7--92.0\%. At matched coverage VSCP cuts width by 22.1\% against a constant scale, and matches a ten-model ensemble's 21.0\% reduction using only one model per scene and four rather than ten rasterization passes per query. VSCP also improves on the closest single-model baseline, the 3DGS-U field, by 4.7 points ($p=0.0225$). The view predictor transfers from bounded source families to all nine unbounded Mip-NeRF~360 scenes. There the full scale beats the constant scale with 20.7\% width saving on all nine scenes. It also keeps an 18.3\% saving under a different densification backbone and runs at 216--280 FPS on an RTX~4090.

</details>

#### 2026-09-09 - LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting

**Authors:** Donghun Ryu, Minhyeok Lee
**Links:** [abs](https://arxiv.org/abs/2609.10095) - [pdf](https://arxiv.org/pdf/2609.10095)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting
- 作者：Donghun Ryu, Minhyeok Lee
- 出版日期：2026-09-09T12:19:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.10095) / [PDF](https://arxiv.org/pdf/2609.10095)

### 一句话总结
论文指出已有学习掩码剪枝方法因 Gumbel-Sigmoid 激活过陡而在掩码训练窗口内过早形成双峰分布、破坏重要性排序，提出用线性增量激活替代，使掩码保持中间置信区间并形成稳定单峰分布，从而实现更紧凑的 3D Gaussian Splatting。

### 研究问题
3D Gaussian Splatting（3DGS）虽支持实时新视角合成，但通过自适应致密化会产生数百万个基元，带来显著存储开销。已有学习掩码剪枝方法（如 LP-3DGS）为每个 Gaussian 分配可学习掩码以识别并剪除冗余基元，但论文识别出该范式的局限：Gumbel-Sigmoid 激活的陡峭斜率会在较短的掩码训练窗口内把掩码值推向极端，此时重要性排序尚未稳定，从而产生尖锐的双峰分布，导致排序无法再被可靠恢复。

### 核心思路/方法
提出 LinearMask-GS，用线性增量激活（linear increment activation）替代 Gumbel-Sigmoid。该激活在整个掩码训练过程中将掩码值保持在“中等置信度”区间，产生稳定、单峰的掩码分布，使掩码排序能够跟踪重要性。

### 主要贡献
- 识别并指出现有学习掩码剪枝（Gumbel-Sigmoid 范式）的关键局限：掩码训练窗口内过早双峰化，重要性排序不稳定。
- 提出 LinearMask-GS，以线性增量激活替代 Gumbel-Sigmoid，获得稳定单峰掩码分布。
- 在 Mip-NeRF 360 上，相比 3DGS 实现 3.6 倍、相比 LP-3DGS 实现 1.6 倍的 Gaussian 数量缩减，同时保持或提升渲染质量。
- 在户外场景实现 1.6 倍缩减（从 2.18M 到 1.36M），并在 PSNR（+0.38 dB）、SSIM（+0.025）、LPIPS（-0.029）上有明显提升。

### 局限性
摘要未提供足够信息。摘要中未说明方法在室内场景、其他数据集或不同压缩率下的表现，也未讨论线性增量激活是否需要额外的超参数调优、训练成本变化或与其他剪枝范式的兼容性。

### 阅读优先级
中。理由：论文针对 3DGS 存储开销这一明确痛点，指出现有掩码剪枝范式的具体机制缺陷并提出简洁替代方案，报告了压缩率与渲染质量指标，主题与 Neural Scene Representations & Rendering 直接相关且思路清晰；但摘要仅覆盖 Mip-NeRF 360 与户外场景的有限结果，未提供方法细节、消融或更广泛验证，因此对需要深入方法评估的读者优先级为中等。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel view synthesis but produces millions of primitives through adaptive densification, leading to significant storage overhead. Learned-mask pruning methods such as LP-3DGS address this by assigning each Gaussian a learnable mask to identify and prune redundant primitives. However, we identify a limitation of this paradigm: the steep slope of the Gumbel-Sigmoid activation drives mask values to the extremes within the short mask-training window, before the importance ranking has stabilized, producing a sharply bimodal distribution from which that ranking can no longer be reliably recovered. We propose LinearMask-GS, which replaces Gumbel-Sigmoid with a linear increment activation that keeps mask values in a mid-confidence regime throughout mask training, producing a stable, unimodal mask distribution whose ranking tracks importance. On Mip-NeRF 360, our method achieves 3.6x and 1.6x Gaussian reductions over 3DGS and LP-3DGS, respectively, while maintaining or improving rendering quality. For outdoor scenes, it yields a 1.6x reduction (from 2.18M to 1.36M) with notable gains in PSNR (+0.38 dB), SSIM (+0.025), and LPIPS (-0.029).

</details>

#### 2026-09-09 - RealSimLoop: Online Real-to-Sim Adaptation via Differentiable Reduced-Order Simulation with Vision Feedback

**Authors:** Zhihao Cen, Chuhua Xian, Hailin Sun, Yuliang Liufu, Zhen Zhang, Xiangyu Chu, Hongmin Cai, Yunbo Zhang, Guoxin Fang
**Links:** [abs](https://arxiv.org/abs/2609.09828) - [pdf](https://arxiv.org/pdf/2609.09828)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, differentiable rendering, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RealSimLoop: Online Real-to-Sim Adaptation via Differentiable Reduced-Order Simulation with Vision Feedback
- 作者：Zhihao Cen, Chuhua Xian, Hailin Sun, Yuliang Liufu, Zhen Zhang, Xiangyu Chu, Hongmin Cai, Yunbo Zhang, Guoxin Fang
- 出版日期：2026-09-09T07:33:40Z
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2609.09828 ；PDF https://arxiv.org/pdf/2609.09828

### 一句话总结
RealSimLoop 提出一种以视觉为物理反馈、在降阶神经子空间内做可微仿真的在线 real-to-sim 自适应框架，旨在准实时地细化材料刚度等物理参数并跟踪时变材料属性。

### 研究问题
论文关注的是：对可变形物体的真实观测往往稀疏或仅限表面，而下游任务需要内部形变、应力场、交互力等隐藏物理量；基于物理的仿真虽可恢复这些量，但在线 real-to-sim 自适应面临三大困难——全空间优化代价高昂、反馈有限、材料属性随时间变化。摘要未提供足够信息说明这些困难在具体场景中的量化表现。

### 核心思路/方法
- 在降阶神经子空间中执行可微仿真，以大幅加速优化循环，从而实现准实时性能。
- 将高效动力学模型与可微渲染耦合，使梯度可直接反向传播，并利用高保真像素数据细化材料刚度等物理参数。
- 采用滑动窗口目标函数，实现稳健的在线自适应，使系统能够跟踪时变材料属性，并弥合由模型降阶或未建模动力学带来的 real-to-sim 差距。

### 主要贡献
- 提出 RealSimLoop，一个以视觉数据作为物理反馈的可微在线 real-to-sim 自适应框架。
- 通过在降阶神经子空间内进行可微仿真，实现准实时的优化性能。
- 将高效动力学模型与可微渲染结合，支持直接梯度回传，以像素数据细化物理参数。
- 通过滑动窗口目标函数支持在线自适应，以跟踪时变材料属性并缩小 real-to-sim 差距。
- 摘要称大量实验表明该方法优于传统离线方法，并验证了其在下游应用中的通用性，包括外力预测、三维应力场重建与新视角合成。具体实验设置、对比指标和数值结果摘要未提供足够信息。

### 局限性
摘要未提供足够信息说明方法的具体局限，例如降阶子空间的近似误差边界、对训练数据或视觉观测条件的依赖、计算资源需求、失败情形以及实验覆盖范围等均未在摘要中展开。

### 阅读优先级
中。理由：该工作面向可变形物体在线 real-to-sim 自适应，结合可微降阶仿真、可微渲染与视觉反馈，问题设定和下游应用（外力预测、应力场重建、新视角合成）具有明确交叉价值；但摘要未给出实验细节、定量结果与局限讨论，是否值得优先精读需进一步查看正文与实验部分后再判断。

</details>

<details>
<summary>Abstract</summary>

Real-world observations of deformable objects are often sparse or surface-level, while downstream tasks require hidden physical quantities such as internal deformation, stress fields, and interaction forces. Physics-based simulation can recover these quantities, but online real-to-sim adaptation remains challenging due to costly full-space optimization, limited feedback, and time-varying material properties. To address these challenges, we propose RealSimLoop, a differentiable framework for online real-to-sim adaptation using vision data as physical feedback. Our approach achieves quasi-real-time performance by executing differentiable simulation within a reduced-order neural subspace, drastically accelerating the optimization loop. We couple this efficient dynamics model with differentiable rendering, enabling direct gradient backpropagation that leverages high-fidelity pixel data to refine physical parameters such as material stiffness. Furthermore, by employing a sliding-window objective function, RealSimLoop enables robust online adaptation, allowing the system to track time-varying material properties and effectively bridge the real-to-sim gap arising from model reduction or unmodeled dynamics. Extensive experiments demonstrate that our method outperforms conventional offline methods, and we validate the framework's versatility in downstream applications, including external force prediction and 3D stress field reconstruction with novel view synthesis.

</details>

#### 2026-09-09 - RouteBridge: Reliability-Routed Bidirectional Distillation Between Neural Radiance Fields and 3D Gaussian Splatting

**Authors:** YuanHang Wang, Xin Cao
**Links:** [abs](https://arxiv.org/abs/2609.09606) - [pdf](https://arxiv.org/pdf/2609.09606)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RouteBridge: Reliability-Routed Bidirectional Distillation Between Neural Radiance Fields and 3D Gaussian Splatting
- 作者：YuanHang Wang, Xin Cao
- 出版日期：2026-09-09T02:00:17Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.09606) / [PDF](https://arxiv.org/pdf/2609.09606)

### 一句话总结
RouteBridge 提出一种按光线自适应选择教师方向的双向蒸馏框架，在 NeRF 与 3DGS 之间进行可靠监督路由或弃权，以缓解全局固定教师带来的局部重建误差传播。

### 研究问题
NeRF 与 3DGS 具有互补的归纳偏置，但现有跨表示蒸馏通常将某一种表示固定为整个场景的教师。摘要指出，全局固定的教师会传播局部重建误差。因此，论文关注的核心问题是：如何避免单一固定教师方向带来的误差传播，并在两种表示之间实现更可靠的跨表示监督。

### 核心思路/方法
- 提出 RouteBridge，一个双向蒸馏框架，为每条光线选择教学方向。
- 可靠性估计器结合光度残差与表示特定的几何证据。
- 路由监督有三种可能：从 NeRF 到 3DGS、从 3DGS 到 NeRF，或弃权。
- 使用与渲染器无关的接口传递颜色、不透明度和归一化深度。
- 该接口不依赖共享特征或点对应关系。

### 主要贡献
- 提出按光线进行可靠性路由的双向蒸馏框架，而不是全局固定教师。
- 设计可靠性估计器，融合光度残差与表示特定的几何证据，用于选择监督方向或弃权。
- 提供渲染器无关的接口，传递颜色、不透明度和归一化深度，无需共享特征或点对应。
- 在 mip-NeRF 360 上，NeRF 与 3DGS 导出分别达到 28.56 dB 和 28.77 dB；3DGS 导出相比 3DGS 提升 1.56 dB，相比 NeRF-GS 提升 0.45 dB，并将 LPIPS 降至 0.207。
- 在静态三视图 DTU 上达到 21.12 dB。
- 消融表明，自适应路由和几何光线目标都对改进有贡献。

### 局限性
摘要未提供足够信息。摘要未说明失败场景、对特定数据集的依赖、计算开销、超参数敏感性、对动态场景的适用性，也未提供与更多基线方法的完整比较。

### 阅读优先级
高。理由：该论文针对 NeRF 与 3DGS 跨表示蒸馏中固定教师导致误差传播的问题提出双向路由方案，问题明确，方法具有针对性，且在 mip-NeRF 360 和 DTU 上给出了定量结果与消融支持；如果关注神经场景表示、跨表示蒸馏或 3DGS 与 NeRF 结合，优先级较高。

</details>

<details>
<summary>Abstract</summary>

Neural radiance fields (NeRFs) and 3D Gaussian Splatting (3DGS) encode a scene with complementary inductive biases, but existing cross-representation distillation typically fixes one representation as teacher for the entire scene. A globally fixed teacher can propagate local reconstruction errors. We present RouteBridge, a bidirectional framework that selects the teaching direction for each ray. Its reliability estimator combines photometric residuals with representation-specific geometric evidence and routes supervision from NeRF to 3DGS, from 3DGS to NeRF, or abstains. A renderer-independent interface transfers color, opacity, and normalized depth without shared features or point correspondence. On mip-NeRF 360, the NeRF and 3DGS exports reach 28.56 and 28.77 dB, respectively. The 3DGS export improves over 3DGS by 1.56 dB and over NeRF-GS by 0.45 dB while reducing LPIPS to 0.207. On static three-view DTU, RouteBridge obtains 21.12 dB. Ablations show that both adaptive routing and geometric ray targets contribute to the improvement.

</details>

#### 2026-09-08 - PIC: Revisiting INR for Image Coding with Fast Encoding and Sub-Millisecond Decoding

**Authors:** Xiang Liu, Jinxiang Wang, Bin Chen, Zimo Liu, Mingyao Hong, Jiawei Li, Yaowei Wang, Shu-tao Xia
**Links:** [abs](https://arxiv.org/abs/2609.09020) - [pdf](https://arxiv.org/pdf/2609.09020)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PIC: Revisiting INR for Image Coding with Fast Encoding and Sub-Millisecond Decoding
- 作者：Xiang Liu, Jinxiang Wang, Bin Chen, Zimo Liu, Mingyao Hong, Jiawei Li, Yaowei Wang, Shu-tao Xia
- 出版日期：2026-09-08T16:52:00Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.09020

### 一句话总结
本文提出了一种前馈式隐式神经表示图像编码架构PIC，在保持实用编码速度的同时实现了超低延迟解码，并首次达到与JPEG在率失真性能和解码速度上同时可比或更优的学习型图像编解码器水平。

### 研究问题
如何克服基于隐式神经表示（INR）的图像编码方法中编码速度慢和解码效率利用不足的问题，使其具备实际应用可行性。

### 核心思路/方法
- 提出前馈式INR图像编码架构PIC：通过单次前向传播计算INR网络所需的全部信息，实现20 FPS的编码速度。
- 设计高度优化的解码器：达到2000 FPS解码速度，显著超过JPEG。
- 在率失真（RD）性能与JPEG相当的前提下，实现解码速度的超越。

### 主要贡献
- 提出PIC编码架构，将INR图像编码的编码速度提升至20 FPS（实时可用级别）。
- 实现亚毫秒级（2000 FPS）超高速解码，显著超越JPEG解码速度。
- 据作者所述，这是首个在RD性能和解码速度上同时优于或可比JPEG，且保持实用编码速度的学习型图像编解码器。
- 开源代码：https://github.com/actcwlf/PIC

### 局限性
摘要未提供足够信息。具体局限性评估（如与更多现代学习型编解码器的对比、泛化性、不同分辨率/内容类型的表现等）未在摘要中说明。

### 阅读优先级
**高**
理由：该工作首次声称在学习型图像编码中同时突破编码速度、解码速度和RD性能三重瓶颈，且直接与JPEG基准对比，对神经表示用于实际图像压缩的方向具有重要参考价值；同时公开代码，便于复现和进一步研究。

</details>

<details>
<summary>Abstract</summary>

Implicit neural representation (INR) has achieved remarkable progress in novel view synthesis and image/video coding in recent years.Compared to conventional end-to-end image codecs, INR-based compressors demonstrate significant advantages in decoding complexity. However, their practical application has been hindered by the inferior encoding speed and underutilized decoding efficiency.In this work, we propose a feedforward INR image coding architecture, Practical INR Image Codec (PIC), that computes all the necessary information for INR network in a single forward pass, achieving an encoding speed of 20 FPS. Additionally, we implement a highly optimized decoder that reaches 2000 FPS decoding speed, significantly surpassing JPEG's performance at comparable rate-distortion (RD) performance. To the best of our knowledge, this work presents the first learning-based image codec that simultaneously outperforms or is comparable with JPEG in both RD performance and decoding speed while maintaining practical encoding speed. Code is available at https://github.com/actcwlf/PIC.

</details>

#### 2026-09-08 - CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation

**Authors:** Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang
**Links:** [abs](https://arxiv.org/abs/2609.08730) - [pdf](https://arxiv.org/pdf/2609.08730)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, novel view synthesis, view synthesis, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation
- 作者：Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang
- 出版日期：2026-09-08T13:26:32Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.08730

### 一句话总结
本文提出CVT-GS，一种无需优化的后处理框架，通过对已训练的3D高斯泼溅场景进行几何感知的质心Voronoi剖分和轻量神经单元合并，实现上百倍高斯点压缩且保持渲染质量。

### 研究问题
如何在不重新训练、不修改架构的前提下，直接压缩已训练好的3D高斯泼溅（3DGS）场景，以降低存储与计算开销，同时保持视觉保真度。

### 核心思路/方法
- 使用几何感知的质心Voronoi剖分（CVT）在高斯中心上构建空间连贯的单元。
- 设计轻量神经单元合并器，在可微渲染监督下为每个单元预测一个具有高度代表性的高斯原语。
- 将场景简化建模为感知渲染的多对一合并过程，而非朴素剪枝；输出仍为标准3DGS格式，可直接在现有渲染器中使用。

### 主要贡献
- 提出首个面向已训练3DGS场景的免训练后处理简化框架，无需侵入式训练或逐场景微调。
- 引入CVT聚类+神经合并的两阶段设计，兼顾几何空间结构感知与渲染质量。
- 在多种数据集上验证有效性；在将高斯点数压缩100倍时，处理速度比SOTA快12倍，PSNR提升1.3 dB。

### 局限性
摘要未提供足够信息：未说明方法对不同类型的场景（如复杂几何/高频纹理）的适应性，未提及可能的伪影、超参敏感性，也未报告在极低压缩比下或大场景中的具体性能边界。

### 阅读优先级
**高**。理由：该工作针对3DGS存储开销大的核心痛点提出免训练的通用后处理压缩方案，应用价值高；技术路线（CVT+神经合并）具有新颖性；实验显示在100倍压缩下仍有速度与质量上的显著优势，适合从事神经渲染、三维场景压缩等相关方向的研究者优先关注。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting (3DGS) has emerged as a powerful representation for real-time novel view synthesis, rendering high-fidelity scenes often relies on a massive number of Gaussian primitives, incurring substantial storage and computational overhead. Existing simplification techniques are largely intrusive, requiring training-time pruning, architectural modifications, or computationally expensive per-scene fine-tuning. These drawbacks limit their deployment on off-the-shelf pretrained models. In this paper, we propose CVT-GS, a novel optimization-free post-hoc simplification framework that directly compresses trained 3DGS scenes without sacrificing visual fidelity. Our approach first constructs spatially coherent cells over Gaussian centers via a geometry-aware Centroidal Voronoi Tessellation (CVT). Subsequently, a lightweight neural cell merger predicts the geometry and appearance of a single, highly representative Gaussian primitive for each cell under differentiable rendering supervision. By formulating simplification as a rendering-aware many-to-one merging process rather than naive primitive pruning, CVT-GS outputs a standard 3DGS scene that is seamlessly compatible with existing renderers. Experiments on various datasets demonstrate the superiority of our method. Notably, when achieving a 100-fold reduction in Gaussian points, our method operates 12 times faster than state-of-the-art methods while improving the PSNR by 1.3 dB.

</details>

#### 2026-09-07 - TV-SGS: Gaussian Splatting with Geometric Information Propagation via Tensor Voting under sparse views

**Authors:** Harish N Sathishchandra, Philippos Mordohai
**Links:** [abs](https://arxiv.org/abs/2609.07734) - [pdf](https://arxiv.org/pdf/2609.07734)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TV-SGS: Gaussian Splatting with Geometric Information Propagation via Tensor Voting under sparse views
- 作者：Harish N Sathishchandra, Philippos Mordohai
- 出版日期：2026-09-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.07734

### 一句话总结
本文提出一种基于张量投票的3D几何损失，使3D高斯溅射中的各个高斯在稀疏视图下能够直接通信，从而提升重建场景的几何精度与渲染质量。

### 研究问题
在稀疏视图条件下，现有高斯溅射方法中各高斯之间仅通过像素投影间接相互影响，缺乏直接的结构通信，导致重建的3D几何结构不够精确。本文旨在解决这一几何监督不足的问题。

### 核心思路/方法
- 引入经典张量投票（Tensor Voting）方法，其原本用于从噪声输入中推断结构，本文将其改造为测试时优化过程中的几何监督信号。
- 提出一类不依赖于渲染的新型3D损失，用于直接对各高斯形成的3D结构进行约束。
- 该3D损失可与文献中几乎所有已有损失组合使用，并易于集成到多种现有高斯溅射骨干网络（backbone）中。
- 在测试优化阶段，通过张量投票促进不同高斯之间的直接信息传播，从而提升整体场景几何的一致性与准确性。

### 主要贡献
- 提出一种使各高斯能够直接通信的新机制，增强了它们在3D空间中形成的几何结构。
- 首次将张量投票适配为高斯溅射中测试时优化的几何监督工具，实现更精确的场景几何。
- 引入一类通用的、无需渲染的3D损失，能够与主流现有损失兼容并插入多种骨干。
- 在DTU和Tanks-and-Temples数据集上的实验表明，相比骨干方法，TV-SGS改善了输出几何，同时保持或提升了渲染质量。

### 局限性
摘要提供了实验的整体结论，但未提供以下信息：具体的基线方法细节、各数据集上的定量指标（如PSNR/SSIM数值）、不同视图稀疏程度的实验设置、计算开销、张量投票在训练/推理各阶段的详细实现，以及该方法在极稀疏（如仅2-3视图）情况下的表现边界。以上均属于摘要未提供足够信息。

### 阅读优先级
**高**
- 理由：稀疏视图下的三维重建是当前神经渲染领域中的活跃难点，本文提出一种不依赖渲染的3D损失，具有较好的通用性和可插拔性，方法思路新颖（张量投票与高斯溅射结合），且实验覆盖多个公开数据集，对从事三维几何优化或神经渲染的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has been effective in inferring scene representations that excel in novel view synthesis. Multiple splats cooperate seamlessly to synthesize the pixels of novel views and are jointly optimized even though they only affect each other indirectly, via pixels they project to in common. We present an approach that enables direct communication among splats to enhance the geometric structures they form in 3D. This is accomplished by Tensor Voting, which was originally designed to infer structures from noisy inputs and has been adapted here to provide supervision during test-time optimization, leading to more accurate scene geometry. We introduce a new class of 3D losses that do not rely on rendering and can be combined with essentially all losses previously reported in the literature. Our 3D losses are especially effective when the input views are sparse and geometric regularization is essential due to limited supervision from the images. Our method is easy to integrate with a diverse set of backbones, and our experiments on the DTU and Tanks-and-Temples datasets demonstrate that TV-SGS improves the geometry of the outputs compared to the backbone, while maintaining or improving rendering quality.

</details>

#### 2026-09-07 - Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat

**Authors:** Simone Foti, Caner Korkmaz, Stefanos Zafeiriou, Tolga Birdal
**Links:** [abs](https://arxiv.org/abs/2609.07557) - [pdf](https://arxiv.org/pdf/2609.07557)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat
- 作者：Simone Foti, Caner Korkmaz, Stefanos Zafeiriou, Tolga Birdal
- 出版日期：2026-09-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.07557

### 一句话总结
本文提出一种基于热核（Heat Kernel）的纹理表示方法 HKTex，在三角网格曲面上直接定义各向异性热核作为高斯核的测地线等价物，以消除 UV 映射的弊端并降低显存占用。

### 研究问题
如何设计一种无需 UV 展开、直接在任意三角网格曲面上定义的新型纹理表示，克服 UV 映射中存在的空间浪费、接缝、形变、顶点复制和分辨率不均等问题，同时降低内存占用。

### 核心思路/方法
- 受 3D Gaussian Splatting 启发，将“纹理”从传统的 UV 贴图重新定义为定义在网格曲面上的热核纹理。
- 基于离散黎曼几何，在任意以三角网格离散化的流形曲面上，使用各向异性热核作为高斯核的测地线等价物。
- 核的位置优化与自适应致密化策略全部重新设计，直接在待纹理化对象的曲面表面上进行。
- 与基于物理的渲染器完全集成，可从现有纹理或多视角图像进行优化。

### 主要贡献
- 提出 HKTex，一种全新的纹理表示，完全消除 UV 展开过程及其相关缺陷。
- 将热核作为测地线高斯核引入纹理建模，形成与曲面几何直接关联的表示。
- 在曲面表面而非参数域上重新定义优化与自适应致密化策略。
- 表示与物理渲染器集成，支持从已有纹理或多视图图像优化。

### 局限性
摘要未提供足够信息。文中未报告定量实验、对比基线、具体性能指标或失败场景等局限性内容。

### 阅读优先级
中。该工作将 3DGS 思想引入纹理领域，创新点明确且具有实用性潜力，但摘要中未给出实验证据；建议对纹理映射、几何处理或 3DGS 扩展方向感兴趣的读者优先阅读，否则可延后。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has recently revolutionised novel view synthesis as well as many other 3D vision methods and applications. Drawing inspiration from this representation, we now rethink textures to overcome the main issues of UV mapping while considerably lowering their memory footprint. Heat Kernel Textures (HKTex) eliminate UV unwrapping as well as their persistent issues of wasted UV space, seams, distortions, vertex-duplication, and varying resolution. Grounded in discrete Riemannian geometry and intrinsically defined on any manifold surface discretised as a triangular mesh, HKTex uses anisotropic heat kernels as geodesic equivalents to Gaussians. Like our kernels, also the optimisation of their position and the adaptive densification strategies were redefined to operate on the surface of the object to be textureised. Our novel representation is also fully integrated with a physically based renderer and can be optimised either from existing textures or multi-view images. Our project page and code are available at circle-group.github.io/research/HeatKernelTextures.

</details>

#### 2026-09-07 - RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting

**Authors:** Hejun Wang, Jinxi Li, Junwei Jiang, Shiwei Mao, Hu Cheng, Shouwang Huang, Bo Yang
**Links:** [abs](https://arxiv.org/abs/2609.07414) - [pdf](https://arxiv.org/pdf/2609.07414)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting
- 作者：Hejun Wang, Jinxi Li, Junwei Jiang, Shiwei Mao, Hu Cheng, Shouwang Huang, Bo Yang
- 出版日期：2026-09-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.07414

### 一句话总结
本文提出一种基于视频基础模型改进的前馈生成式Transformer——RelightFormer，直接从单视图或多视图输入预测目标光照下的物体重打光结果，不依赖显式的逆渲染或固有属性估计，并构建了大规模LOD数据集以支撑训练与泛化。

### 研究问题
传统图像重打光依赖复杂的逆渲染流程，存在病态优化问题；而单图像生成模型缺乏多视图线索，难以理解3D几何与材质交互。因此，本文旨在直接实现单/多视图前馈重打光，绕过显式固有属性分解。

### 核心思路/方法
- 采用前馈生成式Transformer架构，从视频基础模型适配而来，支持直接、前馈式的单/多视图图像重打光。
- 设计**潜在光照模块**（latent illumination module），通过交叉注意力将目标环境贴图动态注入空间特征中。
- 使用**置换不变的位置编码**，以对称方式处理无序多视图输入，避免顺序偏差。
- 构建大规模数据集**Laval Objaverse Dataset (LOD)**，包含90K个物体和39K种不同光照环境，用于训练数据驱动模型。

### 主要贡献
- 提出首个完全绕过显式固有属性估计的前馈生成Transformer，统一处理单视图和多视图重打光。
- 引入动态光照注入的潜在光照模块与置换不变编码机制，提升多视图处理的鲁棒性。
- 构建大规模多视图重打光数据集LOD（90K物体，39K光照）。
- 实验证明在视觉质量、真实感重打光效果以及单视图、多视图、新视角重打光任务的零样本泛化方面均达到当前最优水平。

### 局限性
- 摘要说明了方法的优点和数据集构建，但未提供训练/推理耗时、内存消耗等效率信息。
- 未提及模型对极端光照、复杂材质或输入遮挡等边缘情况的失败案例或边界条件分析。
- 零样本泛化能力虽有展示，但尚未报告对真实世界拍摄图像的验证结果。
- 摘要未提供足够信息以评估该方法与传统优化方法在鲁棒性上的定量对比细节。

### 阅读优先级
**高**

理由：该论文瞄准图像重打光中的核心痛点（逆渲染病态性、单视图信息不足），提出了一种绕过显式分解的全新前馈生成框架，结合大规模自建数据集并展示多任务SOTA及零样本泛化表现。研究价值和技术新颖性均较强，对3D视觉、生成模型和光照编辑领域的研究者有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

Image relighting is traditionally tackled via complex inverse rendering pipelines, which suffer from ill-posed optimization, or single-image generative models that ignore crucial multi-view cues necessary for understanding 3D geometry and material interactions. To address these limitations, we introduce a feed-forward generative Transformer for direct single- and multi-view image relighting that entirely bypasses explicit intrinsic property estimation. Adapted from a video foundation model, our architecture features a latent illumination module that dynamically injects target environment maps into spatial features via cross-attention. Furthermore, we employ permutation-invariant positional encodings to symmetrically process unordered multi-view inputs without sequential bias. To train this robust data-driven model, we construct the massive Laval Objaverse Dataset (LOD), comprising 90K objects and 39K unique illuminations. Extensive experiments demonstrate state-of-the-art visual quality, photorealistic relighting quality, and strong zero-shot generalization across single-view, multi-view, and novel-view relighting tasks.

</details>

#### 2026-09-07 - From Explicit References to Scene Manifolds: Distributional Fidelity and Realism for Radiance Field Quality Assessment

**Authors:** Saeed Mahmoudpour, Gi-Mun Um, Hyon-Gon Choo, Peter Schelkens
**Links:** [abs](https://arxiv.org/abs/2609.07346) - [pdf](https://arxiv.org/pdf/2609.07346)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Explicit References to Scene Manifolds: Distributional Fidelity and Realism for Radiance Field Quality Assessment
- 作者：Saeed Mahmoudpour, Gi-Mun Um, Hyon-Gon Choo, Peter Schelkens
- 出版日期：2026-09-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.07346

### 一句话总结
本文提出SCODA——一种轻量级、场景条件化的无参考质量评估方法，将辐射场（如3DGS、NeRF）的质量评估从显式图像对比转向场景流形建模，通过深度特征空间中的分布保真度与弱监督判别器给出的真实性信号联合打分。

### 研究问题
如何在不依赖对齐参考图像、且无法稳定选取近邻参考视角的情况下，对辐射场（3D Gaussian Splatting、NeRF等）生成的新视角图像进行可靠的感知质量评估，尤其是在宽基线、任意轨迹和姿态的评估场景中。

### 核心思路/方法
- 抛弃逐图像的比较范式，转向场景级建模：将每个场景的高质量观测表示为深度特征空间中的多元高斯分布，构造“语义保真度”分数，度量测试视图偏离该分布的程度。
- 引入一个弱监督的、面向失真的补丁鉴别器，提供互补的“真实性”信号。
- 通过无监督有界融合策略将以上两种线索结合为最终质量分数。
- 方法为轻量级且场景条件化，不要求对齐参考图，也无需固定的近邻参考视角选择。

### 主要贡献
- 提出SCODA框架，将辐射场质量评估从显式图像对比范式转化为场景流形建模范式。
- 设计基于场景分布的语义保真度指标与弱监督失真感知真实性指标的互补组合，并通过无监督方式融合。
- 在多个基准上验证了该方法与人类主观判断的高度一致性，以及在GS和NeRF生成视图与轨迹上的泛化性（摘要提供总体结论，未提供具体数值）。
- 开源代码（https://gitlab.com/saeedmp/scoda）。

### 局限性
摘要未提供足够信息。（未给出实验数据集规模、失败案例、计算开销对比或对无场景先验时的退化分析等。）

### 阅读优先级
**中。** 该工作针对辐射场质量评估这一较新但专门的方向，提出了范式转变（从参考对比到场景分布建模），对从事3DGS/NeRF渲染质量评测或感知优化研究的读者有参考价值；但摘要未展示具体实验数据和与SOTA的量化对比，影响对其性能的直观判断。若不在该细分领域则可暂缓阅读。

</details>

<details>
<summary>Abstract</summary>

Radiance field representations such as 3D Gaussian Splatting (3DGS) enable high-quality novel view synthesis but can introduce complex, view-dependent artifacts from reconstruction, rendering, and compression. Reliable perceptual quality assessment (QA) is thus essential for evaluating rendered views and guiding the design of perceptually faithful scene representations. Existing full-reference QA metrics require an aligned reference image, while recent cross-reference metrics relax this requirement by comparing a test view with non-aligned references. However, under wide-baseline radiance field settings, selecting a reliable nearby reference can be difficult, particularly when evaluating views along arbitrary trajectories and poses. We propose SCODA, a lightweight scene-conditioned objective QA method that shifts QA from explicit image-to-image comparison to scene-manifold modeling. High-quality observations of each scene are represented as a multivariate Gaussian distribution in deep feature space, producing a semantic fidelity score that measures deviation from the scene distribution. A weakly-supervised distortion-aware patch discriminator provides a complementary realism signal, and both cues are combined through an unsupervised bounded fusion strategy. Experiments on multiple benchmarks show strong agreement with human judgments and robust generalization across GS- and NeRF-generated views and trajectories. Code is publicly available at https://gitlab.com/saeedmp/scoda.

</details>

#### 2026-09-07 - LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure

**Authors:** Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü
**Links:** [abs](https://arxiv.org/abs/2609.07274) - [pdf](https://arxiv.org/pdf/2609.07274)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure
- 作者：Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü
- 出版日期：2026-09-07T09:37:03Z
- 分类：神经场景表示与渲染（主）；三维重建与多视角几何（副）
- 链接：https://arxiv.org/abs/2609.07274

### 一句话总结
LightSplat 提出一种混合表征的 RGB-D SLAM 框架，通过稀疏特征加速追踪与双线程稠密高斯子图构建，实现支持回环检测的高保真实时三维高斯建图。

### 研究问题
现有 3D Gaussian Splatting（3DGS）SLAM 系统在实际部署中面临运行性能不足和地图可适应性差的问题，难以满足真实场景对实时性与重建质量的双重需求。

### 核心思路/方法
- 采用混合表征：局部稀疏特征用于快速稳健的追踪，双线程后端渐进构建稠密高斯子图。
- 实现在线回环检测：通过特征加速的 3DGS 配准，并利用位姿图优化来修正整体地图一致性。
- 最终在线重建高保真高斯地图，面向实际相机运动场景运行。

### 主要贡献
- 提出 LightSplat，一种兼顾追踪速度与稠密重建精度的 RGB-D SLAM 框架。
- 首次（据摘要所述）在 3DGS SLAM 中实现基于特征加速的在线回环闭合与位姿图优化。
- 在多个数据集和真实机器人平台上验证，重建质量接近当前最优水平，能适应实际相机运动，平均帧率达 8 FPS。

### 局限性
摘要未提供足够信息（例如：未提及对计算资源的具体需求、在极端运动或大场景下的退化情况、与最先进方法的具体量化差距等）。

### 阅读优先级
**高**。理由：该工作面向 3DGS SLAM 中关键的实时性与回环闭合问题，提出了工程上可行的混合架构与在线优化方案，实验覆盖多数据集与真实平台，对从事神经渲染与实时稠密建图的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

SLAM systems based on 3D Gaussian Splatting (3DGS) have recently demonstrated promising reconstruction accuracy for dense 3D scene representations. However, current 3DGS systems struggle to meet the strict demands of real-world deployments due to severe limitations in operational performance and map adaptability. To this end, we propose LightSplat, a hybrid-representation RGB-D SLAM framework. It synergizes local sparse features for robust and fast tracking with a dual-thread backend that progressively constructs dense Gaussian submaps. Crucially, we enable online loop closure through feature-accelerated 3DGS registration, refining overall map consistency through pose graph optimization. Ultimately, LightSplat achieves the online reconstruction of high-fidelity Gaussian map. Extensive experiments on multiple datasets and real-world robotic platform demonstrate that our method achieves near state-of-the-art reconstruction quality and the capability to accommodate practical camera motions, maintaining an average framerate of 8 FPS. Overall, LightSplat provides an efficient and robust foundation for deploying high-fidelity 3DGS in real-world environments.

</details>

#### 2026-09-07 - PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis

**Authors:** Sipeng He, Jialei Chen, Zhen Fang, Dongchun Ren, Feng Zhao
**Links:** [abs](https://arxiv.org/abs/2609.06948) - [pdf](https://arxiv.org/pdf/2609.06948)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3DGS, neural rendering, view synthesis, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis
- 作者：Sipeng He, Jialei Chen, Zhen Fang, Dongchun Ren, Feng Zhao
- 出版日期：2026-09-07T02:34:51Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.06948

### 一句话总结
PRG-Fusion 提出一种融合重建证据与生成先验的驾驶视图合成框架，通过区域划分策略（保留、修复、生成）来实现沿新轨迹的高保真视频生成。

### 研究问题
如何在自动驾驶场景中沿指定新轨迹合成逼真的驾驶视频，同时兼顾重建方法的几何一致性与生成方法的视觉真实感与灵活性。

### 核心思路/方法
- 融合两类方法优势：重建类方法（如神经渲染）几何一致但容易产生伪影和内容缺失；生成类方法可沿任意轨迹生成真实视图，但难以保证时间与几何一致性。
- 从重建驾驶场景中提取逐区域“退化证据”，将不同区域划分为三类标签：Preserve（保留）、Repair（修复）、Generate（生成）。
- 推理阶段，上述标签作为统一路由策略，指导三种区域分治处理：3DGS 外观保持（Preserve）、LiDAR 引导的结构修正（Repair）、视频先验驱动的内容补全（Generate）。
- 两阶段训练：第一阶段利用稀疏 LiDAR 投影建立几何控制，第二阶段学习基于稠密 3DGS 渲染的外观控制。

### 主要贡献
- 提出 PRG-Fusion 框架，以重建证据统一编排生成先验，兼顾几何一致性与视觉真实性。
- 设计区域级路由策略（Preserve/Repair/Generate），按场景局部退化情况自适应选择合成方式。
- 提出两阶段训练范式，先几何后外观，实现对 LiDAR 结构与渲染外观的分步控制。
- 在 Waymo 数据集上实验表明，PRG-Fusion 在新轨迹视频合成任务中综合性能最优，视觉质量与几何保真度更好，并在大幅轨迹偏移下保持有竞争力的视图一致性。

### 局限性
摘要未提供足够信息，例如对不同场景类型（如天气、光照变化）、计算开销、训练数据规模需求以及失败案例的具体分析均未提及。

### 阅读优先级
**中**
理由：该工作针对自动驾驶仿真中的视图合成问题，方法设计较完整且实验结果积极，涉及多模态融合（LiDAR、3DGS、视频先验）与区域路由机制，适合关注自动驾驶仿真或新视角合成的研究者阅读；但若与自身研究方向的直接关联不强，为非紧急优先文献。

</details>

<details>
<summary>Abstract</summary>

Synthesizing photorealistic driving videos along specified trajectories is essential for scalable closed-loop simulation. Reconstruction-based methods leverage neural rendering to synthesize geometrically consistent views, but often exhibit diverse artifacts and missing content when the viewpoint deviates from the training trajectory. In contrast, generative models can synthesize realistic views along arbitrary trajectories from vehicle sensor data, yet often struggle to maintain temporal and geometric consistency across frames. To combine the strengths of both, we propose PRG-Fusion, a framework for driving view synthesis that uses reconstruction evidence to orchestrate generative priors across regions. Specifically, we extract region-wise degradation evidence from reconstructed driving scenes and convert it into Preserve, Repair, and Generate (PRG) labels. At inference, these labels serve as a unified routing policy for region-aware spatiotemporal synthesis, orchestrating 3DGS appearance preservation, LiDAR-guided structural correction, and video-prior-driven content completion across Preserve, Repair, and Generate regions, respectively. We then follow a two-stage training paradigm, first establish geometric control from sparse LiDAR projections and subsequently learning appearance control from dense 3DGS renderings. Extensive experiments on Waymo demonstrate that PRG-Fusion achieves state-of-the-art overall performance in novel trajectory video synthesis, with superior visual quality and geometric fidelity while maintaining competitive view consistency under large trajectory shifts.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-10 - Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection

**Authors:** Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie, Gang Liu, Hongjie Yan, Wei Zhou
**Links:** [abs](https://arxiv.org/abs/2609.11225) - [pdf](https://arxiv.org/pdf/2609.11225)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** stereo depth, robot navigation, mapping, localization, scene understanding

<details>
<summary>Abstract</summary>

Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

</details>

#### 2026-09-09 - Grounding Generated Video Plans in Simulation Towards Versatile Dexterous Controllers

**Authors:** Tianyue Wu, Boyuan An, Shuqi Zhao, Heyu Guo, Wanli Xing, Yi Ma, Kaifeng Zhang, Ruihai Wu, Masayoshi Tomizuka
**Links:** [abs](https://arxiv.org/abs/2609.10050) - [pdf](https://arxiv.org/pdf/2609.10050)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Grounding Generated Video Plans in Simulation Towards Versatile Dexterous Controllers
- 作者：Tianyue Wu, Boyuan An, Shuqi Zhao, Heyu Guo, Wanli Xing, Yi Ma, Kaifeng Zhang, Ruihai Wu, Masayoshi Tomizuka
- 出版日期：2026-09-09T11:26:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.10050) / [PDF](https://arxiv.org/pdf/2609.10050)

### 一句话总结
将生成的手-物交互视频作为运动参考，通过仿真中的 HOI grounding 训练多物体、多轨迹的灵巧操作跟踪器，并在部署时由视频模型生成运动计划交由该跟踪器执行。

### 研究问题
生成式 HOI 视频能提供可控的操作运动提议，而基于仿真的 HOI 跟踪可把运动学参考转化为可行的底层控制，但其可扩展性受限于缺乏可靠的参考运动。论文要解决的是如何高效、可扩展地获取可靠参考运动，并把生成视频中的运动计划真正落地到仿真与真实控制中。

### 核心思路/方法
论文将生成视频与基于仿真的 HOI grounding 结合：训练阶段，用生成视频提供多样化的运动参考，学习一个多物体、多轨迹的 HOI 跟踪器；部署阶段，由视频模型产生运动计划，再由学到的跟踪器执行。为支持可扩展的参考生成，作者提出通过 HOI 重建、以最小人工干预生成参考数据的方法，并在仿真中成功 grounding 了超过 1,500 个生成视频。

### 主要贡献
- 提出结合生成视频与仿真 HOI grounding 的框架，用于学习多物体、多轨迹的 HOI 跟踪器。
- 提出以最小人工干预、通过 HOI 重建实现可扩展参考生成的方法。
- 在仿真中成功 grounding 超过 1,500 个生成视频，并在基于仿真的训练中取得比基线高出 25 个百分点以上的成功率。
- 在真实世界闭环实验中实现多样化抓取，包括功能性抓取、非抓取式操作以及抓取后物体位姿跟踪。

### 局限性
摘要未提供足够信息。例如未说明真实世界实验的具体任务范围、成功率、失败模式、泛化边界，也未给出仿真与真实环境之间的差距分析、计算成本或数据规模上限等细节。

### 阅读优先级
高。理由：论文聚焦生成视频到仿真 grounding 再到真实灵巧控制的完整链路，并报告了仿真训练中超过基线 25 个百分点以上的成功率提升以及真实闭环中的多类操作能力；若关注具身智能、灵巧操作、视频生成驱动机器人控制等方向，该工作与核心问题直接相关。

</details>

<details>
<summary>Abstract</summary>

Generated hand-object interaction (HOI) videos provide a controllable way to propose manipulation motions. Simulation-based HOI tracking can translate such kinematic references into feasible low-level control, but its scalability is limited by the lack of reliable reference motions. We therefore combine generated videos with simulation-based HOI grounding: during training, generated videos provide diverse motion references for learning a multi-object, multi-trajectory HOI tracker, and at deployment, the video model produces motion plans that are executed by the learned tracker. In particular, we propose a method that enables scalable reference generation by HOI reconstruction with minimal manual intervention and successfully grounds more than 1,500 generated videos in simulation, achieving success rates over 25 percentage points higher than those of baselines during simulation-based training. In real-world closed-loop experiments, it achieves diverse grasps, including functional grasps, non-prehensile manipulation, and post-grasp object-pose tracking. Videos and code are available at https://boyuan-an.github.io/GALATEA/.

</details>

#### 2026-09-08 - Agentic AI-enabled Semantic Commissioning of a Cognitive Digital Twin for Reconfigurable Manufacturing

**Authors:** Yangyang Liu, Xun Xu, Jan Polzer
**Links:** [abs](https://arxiv.org/abs/2609.09503) - [pdf](https://arxiv.org/pdf/2609.09503)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reconstruction, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Agentic AI-enabled Semantic Commissioning of a Cognitive Digital Twin for Reconfigurable Manufacturing
- 作者：Yangyang Liu, Xun Xu, Jan Polzer
- 出版日期：2026-09-08T22:34:38Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.09503 ；PDF https://arxiv.org/pdf/2609.09503

### 一句话总结
论文提出一种基于智能体与 AI 驱动的自动化工作流，用于认知数字孪生的端到端调试与语义化部署，以应对可重构制造中快速定制化部署的难题。

### 研究问题
可重构制造中，认知数字孪生的快速定制化部署是一大挑战。传统数字孪生构建方法主要关注几何重建，往往忽视自主推理所需的深层语义集成与功能互操作性。

### 核心思路/方法
论文提出一种基于智能体、由 AI 驱动的工作流，用于自动化端到端认知数字孪生调试。系统以 LangGraph 作为多智能体编排引擎，实现双路径合成：
- 语义路径：使用检索增强生成（RAG）从非结构化文档中抽取技术规格；
- 功能路径：使用模型上下文协议（MCP）自主发现并绑定实时工业遥测数据。

### 主要贡献
- 提出面向认知数字孪生自动调试的智能体化、AI 驱动工作流。
- 采用 LangGraph 作为多智能体编排引擎，实现语义路径与功能路径的双路径合成。
- 语义路径利用 RAG 从非结构化文档中抽取技术规格。
- 功能路径利用 MCP 自主发现并绑定实时工业遥测数据。
- 在机器人加工单元中进行实验验证：感知平均精度（mAP）达到 97.2%，部署周期从数周缩短至平均 2 小时，体现从手动脚本向自主编排的范式转变。

### 局限性
摘要未提供足够信息。摘要未说明该方法的适用边界、失败情形、对特定工业协议或文档质量的依赖、实验样本规模、可扩展性或与其他方法的对比局限。

### 阅读优先级
高。理由：该论文聚焦可重构制造与认知数字孪生的自动化部署，问题明确且具有工程价值；摘要给出的验证结果（mAP 97.2%、部署周期从数周降至平均 2 小时）量化显著，并涉及 LangGraph、RAG、MCP 等当前受关注的技术组合。若读者关注具身智能、机器人制造、数字孪生或智能体编排，该论文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Rapid bespoke commissioning of the Cognitive Digital Twin (CDT) is a major challenge in reconfigurable manufacturing. Traditional digital twin (DT) construction methods primarily focus on geometric reconstruction, often neglecting the deep semantic integration and functional interoperability necessary for autonomous reasoning. This paper proposes an agent-based, AI-driven workflow to automate end-to-end CDT debugging. The system utilises LangGraph as a multi-agent orchestration engine to achieve dual-path synthesis: the semantic path extracts technical specifications from unstructured documents using Retrieval Augmented Generation (RAG), while the functional path autonomously discovers and binds to real-time industrial telemetry data using Model Context Protocol (MCP). Experimental validation in a robotic machining cell demonstrates that the system achieves a mean average accuracy (mAP) of 97.2% in perception and reduces the deployment cycle from several weeks to an average of 2 hours, marking a paradigm shift from manual scripting to autonomous orchestration.

</details>

#### 2026-09-08 - SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators

**Authors:** Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang, Junyi Cao, Haoyu Zhen, Yilun Du, Chuang Gan
**Links:** [abs](https://arxiv.org/abs/2609.09155) - [pdf](https://arxiv.org/pdf/2609.09155)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, mapping, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators
- 作者：Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang, Junyi Cao, Haoyu Zhen, Yilun Du, Chuang Gan
- 出版日期：2026-09-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.09155

### 一句话总结
SyncWorld 提出一种利用“视觉校准片段”在上下文中指定动作-视觉映射的动作条件世界模型，无需额外训练即可作为零样本模拟器，在未见环境中预测动作结果并支持测试时策略改进。

### 研究问题
如何使世界模型作为机器人策略回环中的想象环境时，在未见环境（不同视觉环境、相机视角、机器人位置或形态）下实现细粒度、可靠且零样本的动作模拟？核心障碍在于动作并非像素空间的通用语言——相同数值动作在不同设置下的视觉表现不一致，导致混合训练监督冲突和泛化脆弱。

### 核心思路/方法
- 引入 SyncWorld，一种动作条件世界模型，作为跨未见环境的零样本模拟器。
- 利用“视觉校准片段”（visual calibration episode，包含成对的帧与动作，展示所有可控自由度）在上下文中指定特定设置的“动作-视觉映射”（Action–Visual Mapping）。
- 在训练时加入视觉校准上下文，使模型学会通过视觉证据解释动作；当显式校准不可用时，模型可利用交互历史进行推断。
- 该方法无需任何额外训练即可在推理时利用模拟出的 rollout 进行测试时策略改进。

### 主要贡献
- 提出 SyncWorld，首次将动作条件世界模型构建为零样本模拟器，可在未见环境中直接应用。
- 提出利用视觉校准片段在上下文中编码设置相关的动作-视觉映射，解决跨环境动作语义不一致问题。
- 训练策略使模型既能利用显式校准上下文，也能在缺乏校准时依赖交互历史。
- 实验表明 SyncWorld 能准确模拟未见设置中的动作结果，并可在无需训练的情况下实现测试时策略提升。

### 局限性
摘要未提供足够信息。摘要仅提及实验证明其模拟准确性与策略改进能力，但未给出具体实验设置、基线对比、失败案例或对校准片段长度与质量的敏感性分析等细节。

### 阅读优先级
**高**。理由：该工作针对世界模型在机器人策略-回环应用中因动作跨环境泛化差而难以扩展的关键瓶颈，提出新颖的零样本模拟器框架，解决了机器人领域普遍存在的动作非通用语言问题；方法上利用上下文校准而非重训练，具有实用价值，且显示可用于测试时策略改进，对 Embodied AI 与机器人学习方向研究者有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment. We introduce SyncWorld, an action-conditioned world model that serves as a zero-shot simulator across unseen environments without any additional training. SyncWorld leverages a visual calibration episode---paired frames and actions that showcase all the controllable degrees of freedom---to specify the setup-specific Action--Visual Mapping in context. Training with visual calibration contexts teaches the model to interpret actions through visual evidence and to leverage interaction history when explicit calibration is unavailable. Experiments show that SyncWorld can accurately simulate action outcomes in previously unseen settings, and that its capability of simulating rollouts enables test-time policy improvement without training.

</details>

#### 2026-09-08 - GoDeep: Annotation-Free Open-Vocabulary 3D Scene Understanding via Language-Space Lifting

**Authors:** Thodoris Betsas, Anastasios Doulamis, Andreas Georgopoulos
**Links:** [abs](https://arxiv.org/abs/2609.09082) - [pdf](https://arxiv.org/pdf/2609.09082)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GoDeep: Annotation-Free Open-Vocabulary 3D Scene Understanding via Language-Space Lifting
- 作者：Thodoris Betsas, Anastasios Doulamis, Andreas Georgopoulos
- 出版日期：2026-09-08T17:31:51Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.09082

### 一句话总结
GoDeep 提出一种无需 2D-3D 标注、也无需 3D 训练语料库或专用 3D 编码器的开放词汇 3D 场景理解方法，通过将视觉-语言模型仅用作“翻译器”，直接在纯语言嵌入空间中完成实体级描述的地面化、投影与聚合。

### 研究问题
如何在不依赖 3D 训练语料、专用 3D 编码器及任何 2D-3D 标注的前提下，实现开放词汇的 3D 语义分割，并克服 CLIP 嵌入在组合任务上存在的“词袋”式表现（即无法有效区分物体的存在与缺失，且对词汇外物体定位能力弱）？

### 核心思路/方法
- 将视觉-语言模型（如 CLIP）仅作为翻译器，而非 3D 特征提取器：对每张带位姿的图像生成结构化、实体级别的自然语言描述。
- 将这些描述进行地面化（grounding）、投影（projection）与聚合（aggregation），直接在通用的、仅含语言的嵌入空间中完成 3D 场景理解，不训练 3D 编码器，也不需要 3D 训练语料库。
- 所有表示均为离散文本，因此点级预测具有可解释性。
- 提出一种启发式加权聚合策略作为概念验证，该策略偏好“精确但非频繁”的观测，并利用 GoDeep 的可解释性以强化对更细粒度元素的定位。

### 主要贡献
- 提出一种无需标注、无需 3D 训练语料库/编码器的开放词汇 3D 分割管线，利用语言空间提升实现。
- 在 ScanNet++ 上，与使用 ScanNet 训练的强大无标注基线方法表现相当。
- 在含 5 栋建筑的文化遗产基准上，原始分数偏向 CLIP 变体，但一次系统性词汇修正即可逆转排名；该效应在另一类不同对象上通过独立的第二次修正得到验证，表明语言空间嵌入比 CLIP 嵌入更忠实地追踪物理内容。
- 在 ScanNet++ 上对真正的词汇外（OOV）对象展现出更强的“存在”与“缺失”区分能力，且无需任何 2D-3D 标注即可定位这些 OOV 对象。
- 因所有表示均为离散文本，预测在点级别可解释。

### 局限性
摘要未提供足够信息。摘要中未明确讨论方法的显式局限性（如计算开销、对描述质量的依赖、在更大规模场景上的扩展性、失败模式等），也未报告定量实验配置细节。

### 阅读优先级
**中**。理由：该方法在方法论上有明显创新（将 VLM 纯作翻译器、在语言空间中完成 3D 理解），并展示了在词汇外对象定位和可解释性上的优势，对于开放词汇 3D 感知方向有参考价值。但其发表于 2026 年，归档时间较早（预印本），且摘要未提供充分的实验对比与定量细节，需要读者自行谨慎评估其可复现性与实际效果强度，故给出中等优先级。

</details>

<details>
<summary>Abstract</summary>

Open vocabulary 3D semantic segmentation methods typically lift CLIP features into 3D. This embeds points in a joint vision-language space known to behave like a bag-of-words on compositional tasks. Furthermore, even annotation free variants often require a large 3D training corpus and a dedicated 3D encoder per domain. Instead we use a vision-language model purely as a translator. It produces structured, entity-level descriptions of each posed image. These descriptions are grounded, projected, and aggregated directly in a general-purpose, language-only embedding space, with no 3D training corpus or encoder required. On ScanNet++, our pipeline is competitive with strong annotation free baselines trained on ScanNet. On a 5-building cultural heritage benchmark, raw scores initially favor a CLIP-based variant, but a single systematic vocabulary correction reverses this ranking. An effect confirmed by a second, independent correction on a different class, indicating that language-space embeddings track physical content more faithfully. This fidelity extends to genuinely out-of-vocabulary (OOV) objects on ScanNet++ proving that language-space embeddings separate presence from absence objects far more sharply than CLIP-based embeddings do. GoDeep also localize these OOV objects within the scene, all without any 2D-3D annotation. Because every representation remains discrete text, predictions are also explainable at the point level. Finally, exploiting both a heuristic weighting, that favors precise over merely frequent observations and GoDeep's explainability property, we propose an aggregation strategy, as a proof of concept, that favors finer elements localization.

</details>

#### 2026-09-08 - Rethinking Learned Occupancy in Autonomous Active Mapping with Observation-Gated Filtering

**Authors:** Jiahui Zhang, Bonian Han, Gongbo Liang, Yu Zhang
**Links:** [abs](https://arxiv.org/abs/2609.09069) - [pdf](https://arxiv.org/pdf/2609.09069)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rethinking Learned Occupancy in Autonomous Active Mapping with Observation-Gated Filtering
- 作者：Jiahui Zhang, Bonian Han, Gongbo Liang, Yu Zhang
- 出版日期：2026-09-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.09069

### 一句话总结
本文通过受控闭环基准实验揭示占用预测精度与主动建图覆盖性能之间不存在单调关系，并提出一种观测门控滤波器以在线修正规划器使用的占用几何。

### 研究问题
在自主三维主动建图中，学习式占用补全同时充当两个规划角色——打分期望表面增益与约束无碰撞运动，导致不准确的预测可能同时扭曲观测决策与可通行性判断。核心研究问题为：占用补全精度与闭环覆盖绩效之间是否存在一致的促进关系，以及如何在不重新训练或使用真值的情况下改进该耦合接口。

### 核心思路/方法
- 构建受控闭环基准，固定主动建图系统，仅改变规划器面对的占用条件：仅观测（observation-only）、学习式（learned）、Oracle校正（oracle-corrected）、真值（ground-truth）。
- 对比不同条件下的闭环覆盖率与收敛速度。
- 基于诊断结果设计观测门控滤波器：在欠观测区域保留补全预测；仅当预测区域经历多次视锥暴露却缺乏附近RGB-D支持时，抑制该预测。

### 主要贡献
1. 揭示占用精度提升并不单调改进闭环覆盖：与学习式基线相比，使用真值占用平均提前12.7步达到70%最终覆盖率，但最终覆盖率仅提升0.031。
2. 提出不依赖重训练或真值的观测门控滤波方法，显著改善针对性失败启动场景。
3. 结果表明自主任务应在通信间隔期间对规划器面向的几何进行在线修订。

### 局限性
- 摘要提及当前研究假设基准RGB-D观测和足够精确的位姿估计，行星感知条件与累积定位漂移的影响尚未评估。
- 观测门控滤波器在多种场景下的平均性能提升幅度、失败类型覆盖范围等具体数值摘要未提供足够信息。
- 与其它占用学习方法或滤波策略的横向对比摘要未提供足够信息。
- 受控基准之外的泛化性（真实平台部署等）摘要未提供足够信息。

### 阅读优先级
**中**。理由：该文关注主动建图中占用预测与规划耦合的诊断性发现，并对现有学习占用方法提出一个务实的轻量修正策略。对从事机器人主动感知、占用建图或规划交互的研究者有启发性，但方法针对性较窄且实验以受控基准为主，普适性尚未验证；若您专注于闭环自主感知系统设计，建议优先阅读。

</details>

<details>
<summary>Abstract</summary>

Autonomous 3D active mapping requires a space robot to choose where to sense while building the geometry needed for navigation. Learned occupancy completion extends spatial context beyond the current field of view, but one predicted map often serves two planning roles: it scores expected surface gain and constrains collision-free motion. Unsupported occupancy can therefore distort both where the robot looks and where it believes it can travel. We study this coupled interface in a controlled closed-loop benchmark by holding the active-mapping system fixed and varying only its planner-facing occupancy across observation-only, learned, oracle-corrected, and ground-truth conditions. Improving occupancy accuracy does not monotonically improve closed-loop coverage: across 25 starts, planning with ground-truth occupancy reaches 70% of the learned baseline's final coverage 12.7 steps earlier on average, while increasing final coverage by only 0.031. Guided by this diagnosis, we introduce an observation-gated filter that retains completion in insufficiently observed regions and suppresses predictions only after repeated frustum exposure without nearby RGB-D support. The filter improves both targeted failure-prone starts without retraining or ground truth. These results motivate online revision of planner-facing geometry during autonomous intervals between communication windows. The current study assumes benchmark RGB-D observations and sufficiently accurate pose estimates; planetary sensing conditions and accumulated localization drift remain to be evaluated.

</details>

#### 2026-09-08 - Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild

**Authors:** Fei Teng, Sheng Wu, Mengfei Duan, Guoqiang Zhao, Junhui Ma, Kai Luo, Siyu Li, Hao Shi, Zhiyong Li, Kailun Yang
**Links:** [abs](https://arxiv.org/abs/2609.09012) - [pdf](https://arxiv.org/pdf/2609.09012)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild
- 作者：Fei Teng, Sheng Wu, Mengfei Duan, Guoqiang Zhao, Junhui Ma, Kai Luo, Siyu Li, Hao Shi, Zhiyong Li, Kailun Yang
- 出版日期：2026-09-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.09012

### 一句话总结
本文提出Spheriverse数据集与SphereOcc框架，通过球面-笛卡尔空间建模与语义证据检索，提升球面观测下的3D场景理解（语义占用、语义建图、3D检测）性能。

### 研究问题
球面观测图像与笛卡尔坐标物理世界之间存在跨空间表示差异，导致几何对应和语义证据聚合困难，影响3D场景理解精度。

### 核心思路/方法
- 构建Spheriverse数据集：含64,400对时间对齐的球面图像-LiDAR数据，组织为644个序列，覆盖多样场景、光照和天气，带细粒度语义类别。
- 建立基准：针对语义占用预测、语义建图、3D物体检测三个任务，评估30余种方法。
- 提出SphereOcc占用框架：
  - 笛卡尔-球面表示重塑（CSRR）：将球面距离-方位角几何融入笛卡尔体素特征，通过区域调制实现。
  - 球面证据重查询（SER）：以体素内容及距离-高度-方位角几何为条件，自适应地从源球面图像特征中检索相关语义证据。

### 主要贡献
- 提出大规模球面图像-LiDAR数据集Spheriverse（644个序列、64,400对），覆盖多样野外场景。
- 建立三个任务（语义占用、语义建图、3D检测）的基准，统一评估30+方法（总量/分场景对比）。
- 提出SphereOcc框架，结合球面几何建模与语义证据检索，在语义占用任务上达到13.91% mIoU和24.65% GeoIoU，分别超过TPVFormer与SurroundOcc各1.70和2.10个百分点。
- 在所有五个场景中均排名第一，并在不同空间划分及减小的视场下保持优势。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文同时提供新的大规模数据集与新方法，覆盖多个3D感知任务，实验结果在多个指标上明显优于现有方法，且发布于该领域主流方向（Embodied/Robotics/AR），对球面-笛卡尔跨空间建模和3D语义感知研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Spherical observations provide global visual context for 3D scene understanding. However, visual information is encoded in an angular domain, whereas the physical world is represented in Cartesian coordinates. This cross-space representation gap complicates geometric correspondence and semantic evidence aggregation. To delve into this challenge, we introduce Spheriverse, comprising $64,400$ temporally aligned spherical image-LiDAR pairs organized into 644 sequences. The dataset spans diverse scenes, illumination, and weather conditions, with fine-grained semantic classes. We further establish benchmarks for semantic occupancy prediction, semantic mapping, and 3D object detection, evaluating 30+ methods through overall and scene-wise comparisons. For dense prediction, we propose SphereOcc, an occupancy framework that couples spherical geometry modeling with semantic evidence retrieval. Cartesian-Spherical Representation Remodeling (CSRR) incorporates spherical range-azimuth geometry into Cartesian voxel features through region-wise modulation. Spherical Evidence Re-querying (SER) then conditions queries on voxel content and range-height-azimuth geometry to adaptively retrieve relevant semantic evidence from source spherical image features. SphereOcc achieves 13.91% mIoU and 24.65% GeoIoU, outperforming the respective best-performing methods, TPVFormer and SurroundOcc, by 1.70 and 2.10 percentage points. It also ranks first in both metrics across all five scenes, with consistent advantages across the evaluated spatial partitions and reduced fields of view. The established benchmark and source code will be available at https://feit-feiteng.github.io/Spheriverse.

</details>

#### 2026-09-08 - RoboCousin: Build Your Own Simulation Playground for Robust Bimanual Robotic Manipulation

**Authors:** Jingxuan Zhu, Jingyi Li, LiangLiang Chen, Zhiyuan Jing, Jidong Zhang, Hongming Li
**Links:** [abs](https://arxiv.org/abs/2609.08339) - [pdf](https://arxiv.org/pdf/2609.08339)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoboCousin: Build Your Own Simulation Playground for Robust Bimanual Robotic Manipulation
- 作者：Jingxuan Zhu, Jingyi Li, LiangLiang Chen, Zhiyuan Jing, Jidong Zhang, Hongming Li
- 出版日期：2026-09-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.08339

### 一句话总结
RoboCousin 是一个可扩展的仿真数据生成平台，可将用户提供的物体观测自动转化为可复用资产、场景和专家轨迹，用以高效合成大规模双臂操纵训练数据。

### 研究问题
如何降低仿真中新增物体或环境所需的构造成本，从而规模化生成高质量的双臂操纵训练数据？

### 核心思路/方法
- 基于 RoboTwin 2.0 构建，将物体图像自动转换为仿真就绪资产（含视觉与碰撞几何、语义与物理元数据、自动生成的抓取接触候选）。
- 构建“数字表亲”（digital cousins）：在保持任务相关功能与空间关系不变的前提下，对物体、背景、布局和语言指令进行多样化变体生成。
- 同一资产系统支持桌面级与房间级场景构建，并带有碰撞感知的基座控制，支持超出固定工作空间的任务交互。
- 释放 RoboCousin-OBD 数据集（3000+ 标注物体、50 个背景环境），并生成超过 100 万条跨 50 个任务的专家轨迹。

### 主要贡献
- 提出 RoboCousin 平台，将观测数据到可执行仿真任务的全流程自动化。
- 构建大规模公开数据集 RoboCousin-OBD，含物体标注与背景环境。
- 生成超过 100 万条双臂操纵专家轨迹。
- 实验表明：自动生成交互标注与人工标注相当；生成资产有效支持 sim-to-real；桌面级变体可提升在单一重建场景之外的任务迁移能力。

### 局限性
摘要未提供足够信息（例如：未提及方法在哪些任务或场景下失效、计算成本、对特定物体类别或复杂环境的覆盖限制、仿真与真实之间的剩余差距等）。

### 阅读优先级
**高**
理由：该工作涉及双臂操纵、仿真数据生成与 sim-to-real 迁移，属于机器人学习中的热点方向；平台化思路具有较强实用潜力，且公开了大规模数据集与专家轨迹，便于后续复现与扩展；摘要提供的实验证据较为具体且积极。若你的研究关注仿真到真实的泛化或双臂操纵策略训练，该论文值得精读。

</details>

<details>
<summary>Abstract</summary>

Bimanual manipulation policies require large and diverse training datasets, yet collecting demonstrations on physical robots is expensive and difficult to scale. Simulation can generate data efficiently, but existing pipelines typically operate within closed asset libraries and predefined scenes: adding a newly observed object or environment still requires substantial effort to reconstruct geometry, specify physical and semantic properties, annotate interactions, and integrate the result into executable tasks. We present RoboCousin, an extensible simulation-based data-generation platform that turns user-provided observations into reusable assets, scenes, and expert trajectories for bimanual manipulation. Built on RoboTwin~2.0, RoboCousin converts object images into simulation-ready assets with visual and collision geometry, semantic and physical metadata, and automatically generated grasp-contact candidates. It further constructs digital cousins that vary compatible objects, backgrounds, layouts, and language instructions while preserving task-relevant affordances and spatial relations. The same asset system supports tabletop and room-level scene construction, with collision-aware base control for interaction beyond a fixed workspace. We release RoboCousin-OBD, containing more than 3,000 annotated object instances and 50 background environments, and use RoboCousin to generate over one million expert trajectories across 50 tasks. Simulation and real-robot experiments show that the automatically generated interaction annotations are comparable to curated annotations, generated assets provide effective sim-to-real supervision, and tabletop cousins can improve transfer beyond training on a single reconstructed scene. RoboCousin therefore provides a practical path for expanding both the scale and coverage of synthetic bimanual manipulation data.

</details>

#### 2026-09-07 - Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction

**Authors:** Ruoqu Chen, Feixiang Ruan, Liu Cao, Zihao Wang, Botian Xu, Shiqin Tong, Jiajun Liu, Mingzhi Pei, Chenyu Zhang, Wanli Xing, Kaifeng Zhang, Mengdi Xu
**Links:** [abs](https://arxiv.org/abs/2609.07747) - [pdf](https://arxiv.org/pdf/2609.07747)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction
- 作者：Ruoqu Chen, Feixiang Ruan, Liu Cao, Zihao Wang, Botian Xu, Shiqin Tong, Jiajun Liu, Mingzhi Pei, Chenyu Zhang, Wanli Xing, Kaifeng Zhang, Mengdi Xu
- 出版日期：2026-09-07T16:47:39Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07747

### 一句话总结
Dex-X 提出利用仿真作为“触觉补全引擎”，从人类单目视频中重建手物交互过程，生成触觉监督，从而训练可在真实机器人上零样本部署的视觉-触觉灵巧操作策略。

### 研究问题
人类视频缺乏触觉信息，那么能否在没有机器人端数据采集的情况下，仅从人类视频演示中学习可部署的视觉-触觉灵巧操作策略？

### 核心思路/方法
- 核心洞察：仿真可作为触觉补全引擎，为人类视频中缺失的物理触觉信息提供监督。
- 流程：从单目人类演示视频中，在仿真中重建手-物交互，利用仿真中物理接地接触动力学产生触觉监督信号。
- 利用恢复出的触觉信息，训练视觉-触觉操作策略，并蒸馏为可使用点云观测和触觉传感的可部署策略。
- 验证方式：在灵巧手-手臂平台上进行零样本 sim-to-real 迁移，覆盖抓取和接触丰富的工具使用任务。

### 主要贡献
- 提出 DEX-X 框架，首次实现从人类视频（无机器人数据采集）经仿真学习可部署的视觉-触觉灵巧操作策略。
- 仿真中重建交互并产生触觉监督，弥补人类视频缺失的物理接触信息。
- 策略蒸馏为基于点云和触觉感知的部署形式，支持零样本真实世界迁移。
- 实验显示：六类任务上教师策略平均成功率为 65.9%；蒸馏后的视觉-触觉策略在真实立方体抓取上成功率 93%，具有挑战性的桌面清洁任务上为 53%；物体抓取任务中观察到对未见物体几何的零样本泛化。

### 局限性
摘要未提供足够信息。摘要仅报告了跨任务的成功率，未提供失败模式分析、对视频质量或多样性的敏感性、仿真域偏移的具体影响、以及真实环境中其他任务的具体表现细节。

### 阅读优先级
**高**
理由：该工作聚焦于从人类视频学习灵巧操作这一重要且活跃的方向，提出以仿真补全触觉的新颖范式，模型可在真实机器人上零样本部署并显示泛化能力，对机器人学习与具身智能研究人员有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Human videos are an abundant source of dexterous manipulation behaviors, but they lack tactile information that is crucial for contact-rich interaction. This raises a fundamental question: can robots learn deployable visual-tactile dexterous manipulation policies from human video demonstrations without robot-side data collection? We present DEX-X, a framework for learning visual-tactile dexterous manipulation from human videos through simulation. Our key insight is that simulation can serve as a tactile completion engine. Given monocular human demonstrations, DEX-X reconstructs hand-object interactions in simulation, where physically grounded contact dynamics provide tactile supervision unavailable in the original videos. Leveraging this recovered tactile information, we train visual-tactile dexterous manipulation policies and distill them into deployable policies operating on point-cloud observations and tactile sensing. We demonstrate zero-shot sim-to-real transfer on a dexterous hand-arm platform across diverse grasping and contact-rich tool-use tasks. The teacher policy achieves 65.9% average success across six task categories in simulation, while the distilled visual-tactile policy achieves 93% success on real-world cube picking and 53% on the challenging table-cleaning task. Zero-shot generalization to unseen object geometries is also observed on object-picking tasks. Our results suggest that simulated interaction is a key bridge between human videos and deployable dexterous manipulation policies, providing the missing physical supervision needed for scalable robot skill learning from Internet-scale human video data.

</details>

#### 2026-09-07 - Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection

**Authors:** Pu Luo, Cong Xu, Yumei Li, Kexin Zhang, Licheng Jiao, Wenping Ma, Lingling Li
**Links:** [abs](https://arxiv.org/abs/2609.07608) - [pdf](https://arxiv.org/pdf/2609.07608)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection
- 作者：Pu Luo, Cong Xu, Yumei Li, Kexin Zhang, Licheng Jiao, Wenping Ma, Lingling Li
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07608

### 一句话总结
本文提出一种多源协同训练与类别感知融合框架，通过整合多类仿真数据源并采用专家分支与融合路径，在UrbanTwin V2X-Real隐藏测试集上实现Sim2Real路侧LiDAR 3D检测的较好性能（综合得分0.7421）。

### 研究问题
如何弥合路侧LiDAR三维目标检测中仿真到现实的差距，该差距涉及场景几何、采样密度、回波模式与行人尺度等多重耦合不一致问题。

### 核心思路/方法
- 构建统一训练池：将数字孪生扫描、扩散重绘扫描、密度稳定扫描和行人形态对齐样本纳入同一个训练池，各数据源发挥互补作用。
- 多源协同训练：在统一的DSVT检测框架下，为不同数据源分别设置源专属专家分支，各分支针对同一检测目标进行优化，同时保留各自角色。
- 类别感知融合推理：采用预定义的类别感知融合路径——几何稳定与标定感知分支用于车辆，采样互补分支用于卡车，形态一致证据用于行人。
- 无标签点云中心混合：在推理阶段进一步通过无标签的点云中心混合操作细化几何定位。

### 主要贡献
- 提出多源协同训练与类别感知融合的统一框架，以稳定、可解释的方式组织多类仿真数据源协同工作。
- 在UrbanTwin V2X-Real隐藏测试集上取得综合得分0.7421，3D mAP@0.5为0.4518，真实感得分为0.8871。
- 实验结果表明，数据源之间的稳定、可解释协作优于模型输出的无约束聚合。

### 局限性
摘要未提供足够信息——包括对失败案例的分析、各模块的消融实验细节、不同数据源的具体贡献量化、方法的计算开销与推理效率等，摘要均未涉及。

### 阅读优先级
**中**。理由：该工作面向路侧LiDAR的Sim2Real特定赛道任务，方法框架完整且在公开隐藏测试集上给出了量化结果，对从事仿真到现实迁移、路侧感知或多源融合检测的研究者有一定参考价值。但摘要中未给出足够的组件级消融与泛化分析，通用方法论贡献的显著性较难评估，适合对该赛道或相关方向有具体需求的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Bridging the simulation-to-reality gap in roadside LiDAR requires addressing several coupled discrepancies, including scene geometry, sampling density, return patterns, and pedestrian scale. This report presents a multi-source collaborative training and class-aware fusion framework for Sim2Real 3D detection. The method organizes digital-twin scans, diffusion-redrawn scans, density-stabilized scans, and pedestrian morphology-aligned samples into a unified training pool with complementary roles. Within a common DSVT detection formulation, source-specialized expert branches preserve those roles while optimizing for the same detection objective. At inference, a predefined class-aware fusion pathway integrates geometry-stable and calibration-aware branches for vehicles, sampling-complementary branches for trucks, and morphology-consistent evidence for pedestrians. A label-free point-cloud center blend then refines geometric localization. On the UrbanTwin V2X-Real hidden test set, the unified system achieves a combined score of 0.7421, with 3D mAP@0.5 of 0.4518 and a realism score of 0.8871. The results indicate that a stable, interpretable collaboration among data sources is more valuable than unconstrained aggregation of model outputs.

</details>

#### 2026-09-07 - CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements

**Authors:** Hongxiang Zhao, Mutian Xu, Zeyu Jin, Yiming Hao, Shuguang Cui, Xiaoguang Han
**Links:** [abs](https://arxiv.org/abs/2609.07498) - [pdf](https://arxiv.org/pdf/2609.07498)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements
- 作者：Hongxiang Zhao, Mutian Xu, Zeyu Jin, Yiming Hao, Shuguang Cui, Xiaoguang Han
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07498

### 一句话总结
本文提出一个大规模手到夹爪演示数据集 CosmoH2G 及一套两阶段基线方法，旨在将从人手演示中学习到的复杂空间操作动作迁移到机器人夹爪上。

### 研究问题
如何将人手操作演示有效迁移到机器人夹爪，尤其是在涉及旋转、翻转等复杂空间运动的操作场景中。现有方法多局限于简单平面任务，难以处理复杂空间轨迹。

### 核心思路/方法
- 采用隐式、数据驱动的思路，以细粒度手部姿态运动为引导。
- 构建可扩展的数据采集流程，通过手持夹爪进行动作模仿，按运动复杂度协议收集配对手-夹爪演示数据。
- 提出两阶段框架：第一阶段预测稀疏的夹爪关键帧（初始和终止状态），以简化映射目标；第二阶段在关键帧条件下生成完整连续动作序列。
- 为缓解累积漂移，夹爪方向通过模型学习，而平移部分基于抓取启发式和运动学一致性进行后优化。

### 主要贡献
- 提出了大规模配对数据集，包含 6,189 个片段，覆盖 1,254 个不同物体，空间复杂度显著高于现有基准。
- 设计了可扩展的数据采集流程和协议，以优先保证运动复杂度。
- 提出两阶段生成框架并结合平移后优化策略，在仿真和真实机器人实验中优于传统基线方法。

### 局限性
摘要未提供足够信息。摘要仅提及实验在仿真和真实机器人上进行并优于基线，但未详述失败案例、泛化边界、对遮挡或物体类别变化的适用性等局限。

### 阅读优先级
**中**。理由：该工作在数据规模和空间运动复杂度上提供新资源，对机器人操作学习领域有一定参考价值；但方法细节与对比均在摘要中概括性描述，缺少具体量化结果，若需评估方法有效性需进一步阅读全文。若兴趣集中于手-夹爪迁移或操作数据集建设，可优先深入阅读。

</details>

<details>
<summary>Abstract</summary>

Transferring human hand demonstrations to robotic grippers has recently emerged as a cost-effective solution for robot learning. However, existing methods are largely confined to simple, planar tasks and fail to handle complex spatial movements (e.g., intricate trajectories involving rotations or flips) that are essential for robot manipulation. Motivated by this gap, we adopt an implicit, data-driven approach guided by fine-grained hand-pose motions. To this end, we introduce a scalable acquisition pipeline to collect hand-gripper paired demonstrations, governed by a rigorous protocol that prioritizes motion complexity and leverages a handheld gripper for seamless action mimicry. This yields a large-scale paired dataset comprising 6,189 episodes across 1,254 unique objects, exhibiting significantly higher spatial complexity than existing benchmarks. However, learning such complex mappings remains challenging. We observe that naive end-to-end generation of full gripper pose sequences is insufficient, as minor trajectory deviations compound rapidly under intricate dynamics. To address this, we propose a two-stage framework: Stage I predicts sparse gripper keyframes (initial and terminal) to simplify the mapping objective, while Stage II generates the full continuous action sequence conditioned on these keyframes. Furthermore, to mitigate cumulative drift, we keep the gripper's orientation being learned while post-optimizing its translation based on the grasping heuristic and kinematic consistency. In both simulation and real-robot experiments, our framework enables stable and precise hand-to-gripper transfer of complex spatial manipulations, significantly outperforming traditional baselines. Project page: https://cosmoh2g.github.io.

</details>

#### 2026-09-07 - PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout

**Authors:** Haozhuang Chi, Jingsong Liang, Ziying Song, Lei Yang, Shihao Li, Haoruo Zhang, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2609.07328) - [pdf](https://arxiv.org/pdf/2609.07328)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout
- 作者：Haozhuang Chi, Jingsong Liang, Ziying Song, Lei Yang, Shihao Li, Haoruo Zhang, Chen Lv
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07328

### 一句话总结
PV-WM 提出一种仅依赖历史轨迹的异构微观-宏观世界模型，将行人关节运动与车辆刚体状态同步滚动预测，以统一框架完成行人-车辆协同未来推演。

### 研究问题
现有行人-车辆预测方法割裂处理两类对象：道路代理预测器通常忽略行人关节细节，而姿态预测器又不覆盖车辆未来状态。如何在一个统一的递归模型中同步预测行人的根运动与15关节姿态，以及车辆的刚体运动状态，是本文要解决的核心问题。

### 核心思路/方法
- 构建历史观测驱动的世界模型（history-only），在同步异构状态空间中进行递归推进。
- 递归更新三部分：行人根运动、15关节姿态、车辆运动学状态。
- 生成的“行人块”和“车辆块”构成下一层递归的边界条件。
- 车辆边界框由预测的中心与朝向（结合观测到的尺寸）重建；每个转移步后重新计算行人-车辆（P-V）之间的几何关系。
- 所有道路代理共享同一网络，而非分模块专家系统。

### 主要贡献
1. 提出首个能协同滚动预测行人与车辆的异构世界模型，涵盖行人关节与车辆刚体两种动力学。
2. 相比匹配的一次性完整状态预测器，递归执行将 Root ADE 降低 12.7%、MPJPE 降低 14.8%。
3. 反馈干预实验表明，后序预测依赖所生成关节内容、时间顺序及行人身份。
4. 在 824 个对齐的 Waymo 场景（其中 797 个有有效车辆未来支持）中，相比验证集精选的 Modular Specialist，Root ADE 降低 5.2%、MPJPE 降低 7.6%、P-V 距离误差降低 11.9%、定向框最近距离误差降低 5.8%。
5. 模型架构更高效：参数量减少 57.1%，平均 FLOPs 降低 96.5%，实测 p95 延迟降低 25.5%。

### 局限性
摘要未提供关于失败模式、泛化边界、不同路况或极端场景表现的具体信息，因此该部分摘要未提供足够信息。另未提及对遮挡、检测噪声或长时递归误差积累的处理说明，亦属摘要未覆盖范围。

### 阅读优先级
**高**。理由：该工作同时解决行人关节预测与车辆预测之间的割裂问题，具有明显跨子领域整合价值；在 Waymo 基准上相对模块化专家系统有一致且多指标的增益，效率收益也很突出；对于多智能体仿真、自动驾驶规划与具身智能研究均有借鉴意义。

</details>

<details>
<summary>Abstract</summary>

Local pedestrian-vehicle forecasting spans heterogeneous physical scales: pedestrians combine root locomotion with articulated motion, whereas vehicles are rigid bodies described by kinematic state and oriented extent. Existing road-agent forecasters typically omit pedestrian articulation, while pose forecasters leave vehicle futures outside the learned rollout. We introduce PV-WM, a history-only world model over structured post-perception tracks. It recurrently advances pedestrian root motion, 15-joint articulation, and learned vehicle states within a synchronized heterogeneous state. The generated pedestrian and vehicle chunks supply the next recurrent boundary; vehicle boxes are reconstructed from predicted center and heading with observed extent, and P-V geometry is recomputed after every transition. Relative to a matched one-shot complete-state predictor, recurrent execution reduces Root ADE by 12.7% and MPJPE by 14.8%. Feedback interventions show that later predictions depend on the content, temporal order, and pedestrian identity of generated articulation. Across 824 aligned Waymo contexts, with 797 providing valid future vehicle support, PV-WM reduces Root ADE by 5.2%, MPJPE by 7.6%, P-V distance error by 11.9%, and oriented-box closest-approach error by 5.8% relative to a validation-selected Modular Specialist. The single-network model uses 57.1% fewer parameters, 96.5% lower average FLOPs per local scene, and 25.5% lower measured p95 latency. PV-WM unifies this heterogeneous future state while preserving type-specific pedestrian and vehicle dynamics.

</details>

#### 2026-09-07 - KODAMA: Multimodal Digital Twin Reconstruction for Urban RF Propagation Modelling

**Authors:** Maximiliano Wardle, A. Ryo Koblitz
**Links:** [abs](https://arxiv.org/abs/2609.07298) - [pdf](https://arxiv.org/pdf/2609.07298)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 3D reconstruction, photogrammetry, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KODAMA: Multimodal Digital Twin Reconstruction for Urban RF Propagation Modelling
- 作者：Maximiliano Wardle, A. Ryo Koblitz
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：https://arxiv.org/abs/2609.07298

### 一句话总结
KODAMA 是一种全自动的城市射频数字孪生（RFDT）重建管线，无需现场勘测或校准，仅凭公开地理空间数据即可生成可用于光线追踪的城市场景，其非校准预测误差与手工校准模型接近。

### 研究问题
如何在无需现场勘测与人工校准的前提下，自动构建城市场景中面向射频传播建模（RFDT）的、可直接用于光线追踪的三维重建结果，使通信信道行为与真实世界一致。

### 核心思路/方法
- 核心思想：以射频行为而非几何或视觉保真度为重建目标，自动构建"光线追踪可用"的RFDT。
- 输入数据：仅依赖现成的多模态地理空间数据——航拍影像、LiDAR、摄影测量以及街景图像。
- 技术流程：
  - 由航拍影像、LiDAR 与摄影测量生成地形和水密建筑网格；
  - 通过街景图像的曝光加权多视角融合，恢复立面细节、电磁材料属性以及杂波（clutter）。
- 输出：全自动、无校准的城市级RFDT，用于射频传播预测。

### 主要贡献
- 提出一种自动化管线，可在城市规模上由现成地理空间数据重建光线追踪就绪的RFDT，无需现场勘测或校准。
- 在3个站点（覆盖3.6–28 GHz频段）验证中，KODAMA的非校准预测达到个位数的RMSE；
- 与自动基线相比，点对点误差最多降低5.35 dB；
- 与手工构建且经测量校准的RFDT相比，误差仅相差0.22 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作在无校准条件下实现了接近手工校准模型的射频预测精度，且误差显著优于自动基线，方法上同时涉及多模态三维重建与射频建模，对城市级数字孪生和无线信道预测方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D reconstruction typically strives for geometric fidelity or visual plausibility. Radio frequency digital twins (RFDT) are instead judged by whether communication channels behave in them as they do in the real world. RFDTs promise site-specific channel prediction but current practice forces a choice between coarse automated scenes and hand-built, measurement-calibrated models that take weeks to construct per-site. We present KODAMA, an automated pipeline that reconstructs ray tracing-ready RFDTs at city scale from off-the-shelf geospatial data alone: aerial imagery, LiDAR, and photogrammetry yield terrain and watertight building meshes, while exposure-weighted multi-view fusion of street-level imagery recovers façade relief, electromagnetic materials, and clutter---all without site visits or calibration. Across three sites spanning 3.6 to 28 GHz, KODAMA's uncalibrated predictions achieve single-digit RMSE, reducing point-to-point error by up to 5.35 dB over automated baselines and coming within 0.22 dB of a measurement-calibrated, hand-built RFDT.

</details>

#### 2026-09-07 - SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem

**Authors:** Soohyun Ryu, Sohee Kim, Eunho Yang
**Links:** [abs](https://arxiv.org/abs/2609.07064) - [pdf](https://arxiv.org/pdf/2609.07064)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem
- 作者：Soohyun Ryu, Sohee Kim, Eunho Yang
- 出版日期：2026-09-07T05:41:13Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07064

### 一句话总结
本文提出通过合成积木堆叠任务数据集 SpatialBlock-15k 训练大型视觉语言模型（LVLMs），以提升其从2D图像推断3D结构信息的“空间智能”。

### 研究问题
大型视觉语言模型从2D图像中重建并推理场景3D结构的能力（即空间智能）存在不足；现有利用真实场景空间问答数据集的方法依赖密集几何标注，成本高、耗时长且因外部感知模块而产生噪声。

### 核心思路/方法
受人类认知发展启发，提出通过结构化积木操作任务来学习基础空间技能。具体构建了包含15,000个积木堆叠问题的合成数据集 SpatialBlock-15k，覆盖3D到2D投影、视角变换和结构组合三类任务。数据集中引入受控颜色调制作为视觉线索，以鼓励模型在视觉复杂条件下进行基于锚点（anchor-based）的推理。训练方式包括直接回答和基于推理链的预测两种范式。

### 主要贡献
1. 提出一种新的训练范式，通过合成积木堆叠问题提升LVLMs的空间智能，而非依赖真实场景标注数据集。
2. 构建并发布 SpatialBlock-15k 合成数据集，覆盖多种空间推理子任务，并包含颜色调制作为辅助视觉线索。
3. 实验表明，在该合成数据集上训练的LVLMs显著优于基线，并能泛化到真实世界空间任务，尽管数据集本身为合成且规模紧凑。
4. 公开代码与数据。

### 局限性
摘要未提供足够信息，未说明模型在何种具体真实任务上的泛化程度、最大性能上限、数据规模增长的效果以及颜色调制策略在不同模型架构上的通用性。也未见对失败案例或训练计算成本的详细讨论。

### 阅读优先级
**高**。理由：该工作针对LVLMs空间智能这一重要缺陷，提出合成数据驱动的低成本训练范式，且在真实任务上展示泛化能力。对于研究空间推理、合成数据训练或LVLMs能力增强的读者具有直接参考价值，且作者公开代码与数据，易于复现和延伸。

</details>

<details>
<summary>Abstract</summary>

Large Vision-Language Models (LVLMs) have achieved strong performance on diverse visual tasks, yet their ability to reconstruct and reason about the 3D structure of the scene depicted in 2D images -- referred to as spatial intelligence -- remains limited. Existing approaches attempt to address this gap by using real-scene spatial question answering datasets that require dense geometric annotations. However, constructing such labels is costly, time-consuming, and often noisy due to reliance on external perception modules. In this work, we propose a novel paradigm inspired by human cognitive development: learning foundational spatial skills through structured block-manipulation tasks. We introduce SpatialBlock-15k, a synthetic dataset of 15,000 block-stacking problems covering 3D-to-2D projection, viewpoint transformation, and structural combination. The dataset further incorporates controlled color modulation as visual cues to encourage anchor-based reasoning in visually complex conditions. Experiments demonstrate that LVLMs trained on our dataset through either direct answering or reasoning-based prediction significantly outperform baselines and generalize to real-world spatial tasks, despite the dataset's synthetic and compact nature. Code and data are available at https://github.com/rsoohyun/SpatialBlock.

</details>

#### 2026-09-07 - WM-Craftnet: World Synesthesia Model for Generalizable and Robust Dexterous In-Hand Manipulation

**Authors:** Jie Yin, Zeyuan Zhao, Xiaojing Tan, Yang Liu, Chiyu Wang, Xinyang Gu
**Links:** [abs](https://arxiv.org/abs/2609.07002) - [pdf](https://arxiv.org/pdf/2609.07002)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WM-Craftnet: World Synesthesia Model for Generalizable and Robust Dexterous In-Hand Manipulation
- 作者：Jie Yin, Zeyuan Zhao, Xiaojing Tan, Yang Liu, Chiyu Wang, Xinyang Gu
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07002

### 一句话总结
本文提出WM-Craftnet，一种以世界模型为条件框架的灵巧手内操作策略，利用多模态潜动力学提升多物体旋转的泛化性与抗扰动能力。

### 研究问题
如何利用部分且有噪声的多模态观测（本体感觉、深度、触觉）推断物体位姿、几何、接触与滑动，以实现泛化且鲁棒的灵巧手内操作策略。

### 核心思路/方法
- 学习紧凑的动作条件潜动力学模型，输入来自本体感觉、深度、触觉和动作，由多模态重建和奖励预测信号监督。
- 并非将世界模型用于潜在想象或策略优化，而是将其学到的“World Synesthesia Model (WSM)”作为非对称Actor-Critic策略的循环任务上下文。
- WSM专门训练从带噪深度输入重建干净的深度目标，为真实机器人部署提供去噪的几何状态。
- 在9个z轴物体上预训练WSM，作为后续49个物体下游策略学习的可复用先验。

### 主要贡献
- 提出以世界模型为条件、用于灵巧手内操作的框架WM-Craftnet。
- 设计将WSM作为策略循环上下文而非用于想象的机制。
- 通过干净深度监督实现去噪几何状态，支持sim-to-real迁移。
- 预训练WSM可跨物体泛化，提升多物体旋转性能。
- 通过消融实验验证预测性世界建模、清洁深度监督和触觉接触线索对所学状态的作用。

### 局限性
摘要未提供足够信息，未明确说明失败的场景、计算开销、对传感噪声的鲁棒性边界，或与SOTA方法的定量对比细节。

### 阅读优先级
**中**
理由：该工作关注灵巧操作中的多模态融合与领域泛化，方法上有一定新颖性（世界模型作为上下文而非规划器），且展示了跨物体迁移与真实部署证据；但摘要中未给出与现有方法的直接性能比较，实验细节有限，适合对该方向有具体兴趣的读者作为参考，而非紧急必读。

</details>

<details>
<summary>Abstract</summary>

Generalizable and robust dexterous in-hand manipulation requires a policy to infer object pose, geometry, contact, and potential slip from partial and noisy observations. Although recent tactile and visuotactile RL methods achieve strong in-hand rotation in controlled settings, their robustness often degrades under pose shifts, force disturbances, and object variation. We propose WM-Craftnet, a world-model-conditioned framework that learns compact action-conditioned latent dynamics from proprioception, depth, tactile sensing, and actions, supervised by multimodal reconstruction and reward prediction. Rather than using the world model for latent imagination or policy optimization, WM-Craftnet uses the learned World Synesthesia Model (WSM) as recurrent task context for an asymmetric actor--critic policy. Importantly, WSM is trained to reconstruct clean depth targets from noisy depth inputs, providing a denoised geometric state for real-robot deployment. Ablations over recurrent baselines, auxiliary heads, tactile masking, and WSM modality heads show that predictive world modeling, clean-depth supervision, and tactile contact cues all shape the learned state. A WSM pretrained on nine \(z\)-axis objects serves as a reusable prior for \(49\)-object downstream policy learning. This context improves multi-object rotation, with quantitative and qualitative evidence for unseen-object, perturbation-recovery, and sim-to-real transfer.

</details>

#### 2026-09-06 - Diagnosing and Dynamically Filtering Occupancy World Models for Active Mapping

**Authors:** Jiahui Zhang, Gongbo Liang, Yu Zhang
**Links:** [abs](https://arxiv.org/abs/2609.06820) - [pdf](https://arxiv.org/pdf/2609.06820)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Diagnosing and Dynamically Filtering Occupancy World Models for Active Mapping
- 作者：Jiahui Zhang, Gongbo Liang, Yu Zhang
- 出版日期：2026-09-06
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.06820

### 一句话总结
本文诊断占用世界模型误差对主动建图规划的影响，发现单纯校正假阳性或假阴性并不总能提升覆盖率，并提出一种动态过滤策略以改善视点选择。

### 研究问题
占用世界模型（occupancy world models）中的预测误差如何影响主动建图（active mapping）中的视点规划与最终建图覆盖率？具体地，单独去除假阳性或恢复假阴性是否能提升规划性能，以及当几何模型准确时，规划和可达性是否仍是性能瓶颈？

### 核心思路/方法
- 固定规划器不变，仅改变提供给它的占用表示，构造五种条件进行对比：无补全、学习占用模型、经真值 oracle 去除假阳性、经 oracle 恢复假阴性、以及真值占用。
- 通过对比这些条件下的最终覆盖率和覆盖率效率，分析占用误差与下游规划性能之间的关联。
- 基于诊断结果，提出一种动态过滤策略：保留未探索空间中的预测，同时利用在线观测抑制被反复证伪的占用预测。

### 主要贡献
- 系统地诊断了占用世界模型误差对主动建图规划的影响，并指出占用准确性与规划性能之间存在差距。
- 发现真值占用对覆盖率效率的提升远大于对最终覆盖率的提升，说明规划和可达性即使在世界模型准确时仍是重要瓶颈。
- 提出一种动态过滤策略，初步实验表明其能将视点选择引向可达且原本会被遗漏的表面。

### 局限性
摘要未提供足够信息（如动态过滤策略的具体触发条件、定量实验对比结果、多种场景下的泛化性等均未披露）。

### 阅读优先级
**中**。理由：该文聚焦于主动建图与占用世界模型的诊断分析，方法新颖性一般，但研究问题针对当前基于学习完成模型的规划缺陷，结论具有实际参考价值；不过摘要显示实验规模为“初步示例”，定量深度有限，建议对相关方向感兴趣者阅读。

</details>

<details>
<summary>Abstract</summary>

Active mapping requires a robot to select camera viewpoints that efficiently reconstruct an unknown 3D scene. To reason about unobserved regions, recent systems use pretrained occupancy networks as world models that complete missing geometry. The predicted structure contributes to expected coverage gain and constrains feasible robot motion. Consequently, occupancy errors can change both what the robot chooses to explore and where it is able to move. We diagnose these effects by holding the planner fixed and varying only the occupancy representation provided to it. We consider planning without completion, with learned occupancy, with false positives removed by a ground truth oracle, with false negatives restored by an oracle, and with ground truth occupancy. Our experiments show that correcting false positives or false negatives alone does not consistently improve final coverage. This finding reveals a gap between occupancy accuracy and downstream planning performance. Ground truth occupancy provides a much larger improvement in coverage efficiency than in endpoint coverage, suggesting that planning and reachability remain important bottlenecks even when the geometric world model is accurate. Based on these findings, we introduce a dynamic filtering strategy that preserves predictions in unexplored space while suppressing repeatedly unsupported occupancy using online observations. Preliminary examples show that this strategy can redirect viewpoint selection toward reachable surfaces that would otherwise remain unobserved.

</details>

#### 2026-09-04 - WorldSculpt: Generating Compositional Worlds from Grounded Videos

**Authors:** Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
**Links:** [abs](https://arxiv.org/abs/2609.05416) - [pdf](https://arxiv.org/pdf/2609.05416)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3DGS, robotics, AR, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WorldSculpt: Generating Compositional Worlds from Grounded Videos
- 作者：Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
- 出版日期：2026-09-04
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.05416

### 一句话总结
本文提出WorldSculpt方法，通过将强单物体3D生成先验扩展为多视角条件路径，仅用单物体数据微调即可生成包含数百个物体、严重遮挡场景的组合式3D网格表示。

### 研究问题
如何从多视角视频中生成由数百个独立物体网格组成的、处于共享世界坐标系下的组合式3D场景表示，尤其是在密集遮挡、单个视角仅能观测到部分几何的复杂场景下准确重建每个物体的完整形状。

### 核心思路/方法
采用"将强单物体3D生成先验适配到多视角观测"的范式：以Pixal3D为基础，扩展多视角条件路径，使模型在生成每个物体时能利用多个带位姿的观测信息进行grounding。关键设计是，模型仅在规范空间的单物体数据上微调，无需场景级训练即可泛化到包含严重遮挡的大规模场景。

### 主要贡献
- 提出WorldSculpt范式，证明复杂数百物体场景可通过适配单物体生成先验实现组合式生成，无需场景级训练。
- 引入UE-MeshyScene基准：包含密集杂乱场景、数百物体、逐物体标注和真值网格，用于评估此类任务。
- 在单物体、受控多物体及UE-MeshyScene上均优于先前方法，且场景越复杂、遮挡越严重，性能优势越明显。
- 展示将现有3DGS世界（如Marble、HY-World 2.0）转换为组合式网格场景的适用性。

### 局限性
摘要未提供足够信息，无法得知方法在实时性、内存开销、物体数量上限、泛化到未见场景类型等方面的局限。

### 阅读优先级
**高**
理由：该工作针对"密集遮挡场景的组合式3D生成"这一具挑战且具实际应用价值的问题，提出无需场景级训练的可扩展范式，并配套新基准，适合从事三维重建、生成模型及具身智能/AR应用的研究者关注。

</details>

<details>
<summary>Abstract</summary>

We study the problem of generating a compositional 3D representation of a cluttered scene containing hundreds of objects. The goal is to represent the scene as a collection of individual object meshes placed in a shared world frame, as required by downstream applications such as gaming, AR/VR, simulation, and robotics. This task is challenging in densely cluttered scenes, where objects heavily occlude one another and each view reveals only a fraction of their geometry. Geometry-based approaches typically reconstruct the scene as a single representation and leave incomplete geometry in occluded regions, while existing compositional methods with generative priors are largely limited to relatively simple scenes. We show that complex scenes with hundreds of objects can instead be generated compositionally by adapting a strong single-object 3D generative prior to multi-view observations. We instantiate this paradigm with Pixal3D, extending it with a multi-view conditioning pathway that grounds object generation in multiple posed observations. Although the model is finetuned entirely on single objects in canonical space, it generalizes to large scenes with severe occlusion without any scene-level training, demonstrating the feasibility and scalability of this paradigm. We further introduce UE-MeshyScene, a photorealistic benchmark of densely cluttered scenes with hundreds of objects, per-object annotations, and ground-truth meshes. Across single-object, controlled multi-object, and UE-MeshyScene evaluations, our method consistently outperforms prior approaches, with larger gains as scene complexity and occlusion increase. Finally, we demonstrate broader applicability by converting generated 3DGS worlds, such as Marble and HY-World 2.0, into compositional mesh scenes.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
