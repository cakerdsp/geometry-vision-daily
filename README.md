# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：72
- 分类分布：
  - Neural Scene Representations & Rendering: 23
  - 3D Reconstruction & Multi-view Geometry: 21
  - Embodied / Robotics / AR Applications: 15
  - Geometry Foundation Models: 7
  - Dynamic / 4D Reconstruction: 6
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **紧凑化、高效化的场景表示成为显性竞争维度。**  
   Honeycomb-Surfels 用更大的六边形平面基元配合一阶空间颜色场替代密集小基元，GeoGSplat 用非像素对齐的固定数量高斯减少"分辨率—基元数"耦合，GAWM 则把世界—动作模型压缩到 1 亿参数以内。三者共同指向同一目标：在不牺牲质量的前提下降低基元数量、显存占用与推理时延，而不是单纯提升峰值指标。

2. **几何先验与显式几何求解被重新"接回"生成式与学习式管线。**  
   GeoGSplat 显式引入 Anchors/Triplane 与射线—深度约束来纠正非像素对齐高斯的位置漂移；LingGS 用冻结流式 3D 基础模型提供深度、再用显式几何求解器估计位姿；SG^2SLAM 用块级度量先验统一监督跟踪与建图；GPA-VGGT 甚至以"保持几何"为名设计免训练加速。这说明社区对纯注意力/纯学习的几何精度仍不放心，倾向于"学习先验 + 显式几何"的混合路线。

3. **3D Gaussian Splatting 正从"重建即终点"转向"可编辑、可组合、可交互的场景底座"。**  
   GraftRay 做网格对象的物理一致插入与联合路径追踪，ClusterSplat 做 3DGS 内的指代表达定位，DomeGS 补全无界户外场景地平线，CTBakeGS 把 CT 体渲染免训练烘焙成 splats 以便在弱设备上查看。3DGS 的角色由"新视角合成表示"扩展为承载编辑、语义查询、VR 呈现与医学可视化的通用载体。

4. **数据与仿真瓶颈被单独当作研究问题处理。**  
   GameVerse 指出长时程交互式世界模型的瓶颈是缺少分钟级数据而非模型容量；Event 仿真工作干脆放弃渲染，直接从几何与自运动解析合成事件流，把训练加速三个数量级；UMI-Loc-Bench-v1 与 QuadSyn 则分别补上手持采集定位与四足机器人位姿的评测空白。数据集、基准与模拟器正在成为与算法并列的一等贡献。

5. **多模态传感融合（事件、卫星、触觉）用于补足单目/RGB 的失效模式。**  
   4D Reconstruction with Events & RGB 以最小侵入方式给 Monst3R 加事件分支；事件航天器位姿估计把极性—时间交互与可靠性加权串成级联；GroundControl 用卫星图约束户外外推布局；ActiveAlign 用主动挥手与触摸做 real2sim 对齐。共同逻辑是：承认 RGB 单模态在高速运动、外推和接触精度上的固有缺陷，用互补信号而非更大模型来补。

#### 技术路线观察

- **几何基础模型（VGGT 系）**：重点从"能不能前馈出几何"转为"长序列下的效率与几何保真能否兼得"。GPA-VGGT 走免训练的结构替换（早期块帧注意力 + 共享跨帧 K/V，后期只合并 K/V 保留全部 query），LingGS 走"冻结基础模型当虚拟 RGB-D 传感器 + 显式求解器"，两者都把基础模型当作可复用的先验模块而非端到端替代品。这提示几何基础模型的分工正在细化：预测几何、跟踪位姿、加速推理被拆成可替换组件。

- **3D/4D 重建**：分成两条明显不同的路线。一条是前馈、免优化的高效重建（GeoGSplat 的非像素对齐 + 几何接地、CTBakeGS 的免训练烘焙、SceneEvolve 的代码化组合重建）；另一条是带显式优化与在线系统的 SLAM 式重建（LingGS、SG^2SLAM、RAVEN）。前者追求单次前向的速度与泛化，后者追求误差传播可控与在线一致性。4D 方向目前仍偏初步（事件 + RGB 只是给 Monst3R 加分支的初步研究），尚无以事件为主导的完整 4D 管线。

- **神经场景表示与渲染**：基元层面的创新集中在"支撑域形状"和"每基元表达能力"两个自由度上——Hexels 改支撑域为六边形并加一阶颜色场，GeoGSplat 改基元放置方式为非像素对齐，DomeGS 把天空穹顶并入表示本身。渲染层面则出现物理化倾向：GraftRay 用路径追踪统一 Gaussians 与网格、显式建模面光源，说明 3DGS 的"渲染正确性"（阴影、互反射、多视角一致）开始被当作硬指标而非后处理问题。

- **机器人/AR 应用**：应用侧论文普遍把"部署可行性"写进贡献——GAWM 强调 <100M 参数与无需机器人/视频预训练，事件仿真强调 17 微秒/帧与 30 分钟收敛，OpenJaws 强调全开源硬件与低成本立体相机，ActiveAlign 强调在真实 Unitree G1 上的毫米级操作。研究重心从"刷 benchmark"向"降低数据采集、标定、算力与硬件门槛"迁移。

#### 值得优先阅读的论文

1. **GPA-VGGT（2610.37000）**  
   免训练加速几何基础模型，且明确以"保留几何精度"为设计约束（摘要称保留 >99% 位姿精度）。对任何以 VGGT 为骨干的下游工作都有直接复用价值，方法论（早期块结构替换 + 后期 K/V 合并 + 注意力质量恢复）也可迁移到其他二次复杂度模型。

2. **GraftRay（2610.37036）**  
   把 3DGS 场景与网格对象的联合路径追踪、面光源显式建模、扩散先验恢复材质法线整合进一个统一框架。这是 3DGS 走向"可用内容创作管线"的关键一环，且对 AR 合成数据生成有直接意义。

3. **LingGS（2610.36853）**  
   "冻结前馈几何模型 + 显式几何跟踪 + 流式高斯建图"的解耦范式，摘要明确给出"显式几何跟踪优于学习式相机预测"的结论，并声称跨骨干适用。对单目 SLAM 与在线重建路线的选型有参考价值。

4. **GeoGSplat（2610.36760）**  
   直接针对非像素对齐前馈高斯的中心错位问题给出几何接地方案，是"高效前馈 GS"与"几何正确性"之间张力的代表性工作，与 Honeycomb-Surfels 可对照阅读以理解基元效率与几何约束的权衡。

5. **GameVerse（2610.37257）**  
   把长时程世界模型的瓶颈归因于数据而非容量，并给出分钟级、带时序稳定相机轨迹与事件对齐字幕的数据集。若关注交互式世界模型或视频生成的长时程一致性，这是当前窗口内最直接的数据侧资源。

#### 可能的研究机会

- **把"紧凑基元"与"几何接地"合并**：Hexels 的六边形支撑域 + 一阶颜色场与 GeoGSplat 的锚点/Triplane 几何先验尚未结合。能否在非像素对齐框架下使用带局部颜色场的更大基元，同时用射线—深度约束保证中心正确？这是效率与几何保真之间尚未被同时占据的位置。

- **事件模态与前馈几何基础模型的系统化融合**：当前 4D 事件工作只是给 Monst3R 加输入分支的初步研究。事件流能否作为 VGGT 类模型的额外输入或监督信号，用于高速运动下的位姿与深度估计？事件航天器位姿论文中的"可靠性加权"思路也可迁移到一般 4D 重建的观测加权中。

- **3DGS 场景中的物理交互闭环**：GraftRay 解决了插入与光照一致，但插入对象后的场景在被机器人操作、被触觉修改时如何更新表示尚未涉及。ActiveAlign 的触觉对齐与 GraftRay

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-28T14:23:12-04:00
**Total number of papers:** 72
**Number of papers added in the latest update:** 23
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

#### 2026-10-27 - GPA-VGGT: Geometry-Preserving Acceleration of VGGT

**Authors:** Muyeol Sung, Jangwon Kim, Jongwoo Lim
**Links:** [abs](https://arxiv.org/abs/2610.37000) - [pdf](https://arxiv.org/pdf/2610.37000)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GPA-VGGT: Geometry-Preserving Acceleration of VGGT
- 作者：Muyeol Sung, Jangwon Kim, Jongwoo Lim
- 出版日期：2026-10-27T10:46:52Z
- 分类：Geometry Foundation Models
- 链接：[摘要](https://arxiv.org/abs/2610.37000) / [PDF](https://arxiv.org/pdf/2610.37000)

### 一句话总结
GPA-VGGT 是一种免训练加速方法，它针对 VGGT 中开销很大的全局注意力做结构替换与 K/V 合并，目标是在获得与既有加速方法相当的加速比的同时，仍保留精确几何估计所需的信息。

### 研究问题
VGGT 这类前馈几何模型能在单次前向中从一到数百个视图恢复相机参数、深度图和点图，但它的全局注意力开销随帧数呈二次增长，并在长序列上主导端到端运行时间。已有的免训练效率方法（如 token merging）会带来精度下降，因此难以直接替代 VGGT。

### 核心思路/方法
- 在早期 block 中，用“帧注意力 + 共享的跨帧 K/V 集合”替代全局注意力。
- 在其余 block 中，只合并 keys 和 values，保留所有 queries。
- 恢复每个被合并 key 所代表 token 的注意力质量。
- 将匹配度量随机投影到 128 维，以降低匹配成本。
- 方法定位为 training-free（免训练）。

### 主要贡献
- 提出 GPA-VGGT，一种用于加速 VGGT 的免训练方法。
- 通过早期 block 的注意力替换与后续 block 的 K/V 合并策略，在获得与先前工作相当的加速比的同时，保留精确几何估计所需信息。
- 摘要称，在 AUC@3 指标下保留超过 99% 的 VGGT 位姿精度。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集、序列长度范围、绝对运行时间、与其他方法逐项精度对比、内存开销，也未说明随机投影或注意力质量恢复的消融结果与失败情形。

### 阅读优先级
中。理由：该工作直接针对 VGGT 长序列推理效率与几何精度保持之间的权衡，且声称免训练、位姿精度保留超过 99%，对该方向读者有参考价值；但当前仅有摘要，缺乏实验细节与完整对比，需阅读全文后再判断其通用性与稳健性。

</details>

<details>
<summary>Abstract</summary>

Feed-forward geometry models such as VGGT recover camera parameters, depth maps, and point maps from one to hundreds of views in a single forward pass, making them powerful backbones for multi-view 3D perception. However, VGGT's global attention is quadratic in the number of frames and dominates end-to-end runtime on long sequences, which has motivated a range of training-free efficiency methods such as token merging. These methods, however, come with a drop in accuracy that makes them hard to use in place of VGGT. We propose GPA-VGGT, a training-free acceleration method that replaces global attention in early blocks with frame attention augmented by a shared cross-frame K/V set. In the remaining blocks, we merge only keys and values while preserving all queries, restore the attention mass of the tokens each merged key represents, and randomly project the matching metric to 128 dimensions to reduce matching cost. Across diverse multi-view geometry tasks, GPA-VGGT provides training-free acceleration at speedups comparable to prior work while preserving the information required for precise geometric estimation, retaining over 99% of VGGT's pose accuracy under AUC@3.

</details>

#### 2026-10-26 - Does VGGT Know What It Does Not Know?

**Authors:** Adityan Thirumani Srinivasan, David Nordström
**Links:** [abs](https://arxiv.org/abs/2610.35806) - [pdf](https://arxiv.org/pdf/2610.35806)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, point map, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Does VGGT Know What It Does Not Know?
- 作者：Adityan Thirumani Srinivasan, David Nordström
- 出版日期：2026-10-26T17:37:39Z
- 分类：Geometry Foundation Models（主分类）；二级分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2610.35806) / [PDF](https://arxiv.org/pdf/2610.35806)

### 一句话总结
论文探究前馈式三维重建模型 VGGT 是否在其冻结特征中隐含对相机位姿预测失败的自知能力，并表明线性探针可对此进行高精度预测。

### 研究问题
VGGT 等前馈式三维重建模型在单次前向传播中回归相机与几何，但不报告相机位姿的不确定性，错误相对位姿与正确位姿在外观上无差别。论文追问：冻结的 VGGT 模型是否“知道”自己的位姿何时出错。

### 核心思路/方法
- 构建 HardMatch 基准，包含 1,000 对刻意困难的图像对，VGGT 在其中 35% 的图像对上失败。
- 在 VGGT 冻结特征上训练线性探针，用于预测位姿失败，并在留出类别上评估。
- 与 VGGT 自身的点图置信度、以及在 VGGT 全部输出上训练的分类器进行比较。
- 分析该知识在模型中的位置：比较逐图像编码器与融合双视角的层。
- 将探针不重新训练地迁移到 PhotoTourism 与 ScanNet-1500 的旋转失败检测，并与共视性解释进行比较。
- 在第二个模型 $π^3$ 上验证类似现象。

### 主要贡献
- 提出 HardMatch 基准，用于评估困难图像对上的位姿失败。
- 发现冻结 VGGT 特征上的线性探针预测位姿失败的 ROC-AUC 为 93.5%，高于 VGGT 自身点图置信度的 79.7% 和基于全部输出分类器的 77.7%。
- 表明探针能捕捉 VGGT 高置信却失败的案例，可支持下流系统对不信任的图像对弃权。
- 展示探针无需重新训练即可迁移到 PhotoTourism 和 ScanNet-1500 的旋转失败检测，且超出共视性所能解释的范围。
- 定位该知识不在逐图像编码器中，而是在融合双视角的层的中途计算得到；$π^3$ 也呈现相同情况。
- 总结为：VGGT 对自身失败的了解多于其报告的内容。

### 局限性
- 摘要未提供足够信息说明 HardMatch 的构建细节、数据来源与类别划分方式。
- 摘要未提供足够信息说明线性探针的具体结构、训练设置与统计显著性。
- 摘要未提供足够信息说明与共视性比较的具体方法和定量结果。
- 摘要未提供足够信息说明在 $π^3$ 上的实验规模与完整结果。
- 摘要未提供足够信息说明方法在更多模型、更多任务或真实部署场景中的泛化性。

### 阅读优先级
中。理由：论文聚焦前馈三维重建模型的失败自感知与不确定性报告问题，提出可解释性探针和可迁移的失败预测方法，对几何基础模型的可信部署有参考价值；但摘要未提供实验细节与完整局限性，需阅读全文才能判断其普适性。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models such as VGGT regress cameras and geometry in a single forward pass, but they report no uncertainty for the camera poses they predict: an incorrect relative pose looks no different from a correct one. We ask whether the frozen model nonetheless knows when its pose is wrong. On HardMatch, a benchmark of 1,000 deliberately difficult image pairs on which VGGT fails on 35% of pairs, a linear probe on VGGT's frozen features predicts pose failure on held-out categories with ROC-AUC 93.5%, compared with 79.7% for VGGT's own point-map confidence and 77.7% for a classifier trained on all of VGGT's outputs. The probe catches failures VGGT is confident about, lets a downstream system abstain on the pairs it distrusts, and transfers without retraining to rotation failures on PhotoTourism and ScanNet-1500, beyond what co-visibility explains. This knowledge is absent from the per-image encoder: it is computed partway through the layers that fuse the two views, and the same holds for a second model, $π^3$. In essence, we find that VGGT knows more about its own failures than it reports.

</details>

#### 2026-10-26 - E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling

**Authors:** X-Era AI Lab Team, :, Jianhao Lai, Zhihao Zhan, Zhiquan Liao, Qichang Li, Shubin Chen, Zhiyuan Liu, Hongsen Lei, Jianman Lin, Xiaoxin Lin, Ke Gong, Baiyue Gu, Shiming Chen, Junlin He, Longqi Yang, Junrong Xiao, Haolin Luo, Xiaojuan Su, Jianfeng Li, Yu Luo, Xu Sun, Likui Zhang, Jusheng Zhang, Qinhan Lyu, Tianshui Chen, Liang Lin, Guangrun Wang
**Links:** [abs](https://arxiv.org/abs/2610.36011) - [pdf](https://arxiv.org/pdf/2610.36011)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling
- 作者：X-Era AI Lab Team, Jianhao Lai, Zhihao Zhan, Zhiquan Liao, Qichang Li, Shubin Chen, Zhiyuan Liu, Hongsen Lei, Jianman Lin, Xiaoxin Lin, Ke Gong, Baiyue Gu, Shiming Chen, Junlin He, Longqi Yang, Junrong Xiao, Haolin Luo, Xiaojuan Su, Jianfeng Li, Yu Luo, Xu Sun, Likui Zhang, Jusheng Zhang, Qinhan Lyu, Tianshui Chen, Liang Lin, Guangrun Wang
- 出版日期：2026-10-26T17:00:09Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.36011 ；PDF https://arxiv.org/pdf/2610.36011

### 一句话总结
E0.5 提出一种以 3D 基础模型为主干、原生以 3D 几何为世界表示并显式预测未来 3D 状态与动作的世界-动作模型，在 RoboTwin 2.0 与真实机器人操作任务上验证了其效果。

### 研究问题
摘要指出，世界-动作模型（WAMs）对具身智能具有前景，但主流方法以视频基础模型或视觉-语言模型（VLM）为中心；即使引入 VGGT 等 3D 模型提取的几何特征，这些特征通常也只是作为辅助输入或预测目标送入视频模型或 VLM，3D 几何并未成为世界建模的原生基础。论文要解决的问题是：能否将 3D 基础模型本身作为世界-动作建模的主干，使几何成为世界建模与动作预测的原生表示。

### 核心思路/方法
E0.5 是一个直接构建在 3D 基础模型之上的“几何原生”世界-动作模型，包含两项关键创新：
1. 采用 3D 基础模型作为主骨干，使 3D 几何成为世界建模和动作预测的原生表示，而非辅助输入。
2. 显式地联合预测未来 3D 状态与动作，从而捕捉超越“仅动作建模”或“未来视频预测”的几何世界动态。
摘要还提到，E0.5 在 AgiBotWorld-Beta 的超过 160k 条机器人轨迹上进行具身预训练，在预训练的 3D 基础模型内联合学习机器人动作与未来几何；E0.5 是 VWA 系列世界-动作模型的成员。

### 主要贡献
- 提出 E0.5，一种以 3D 基础模型为主干的几何原生世界-动作模型，将 3D 几何作为世界建模与动作预测的原生表示。
- 显式联合预测未来 3D 状态与动作，使模型能够建模几何世界动态。
- 在 RoboTwin 2.0 上，未经具身数据预训练即取得 clean 设置 89.90%、randomized 设置 50.09% 的成功率。
- 在 AgiBotWorld-Beta 的 160k+ 机器人轨迹上进行具身预训练后，在 AgileX Piper 和 Zerith H1 上的真实世界操作平均成功率分别提升约 15 和 7 个百分点。
- 结果表明几何原生基础模型具备获取机器人交互知识并迁移到物理操作任务的潜力。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、计算成本、推理速度、随机化设置成功率偏低的原因、预训练数据规模之外的其他训练细节，也未与其他方法进行系统性对比或消融分析。

### 阅读优先级
中。理由：论文提出“以 3D 基础模型为主干、显式预测未来 3D 状态与动作”的几何原生 WAM 思路，并给出 RoboTwin 2.0 与两个真实机器人平台的结果，对具身智能与 3D 基础模型交叉方向有参考价值；但摘要未提供方法细节、消融、对比与失败分析，需阅读全文才能判断其技术严谨性与可复现性。

</details>

<details>
<summary>Abstract</summary>

World-action models (WAMs) offer a promising framework for embodied intelligence, yet mainstream approaches remain centered on video foundation models or vision-language models. Even when geometric features extracted by 3D models such as VGGT are incorporated, they are typically passed into a video model or VLM that serves as the primary backbone, leaving 3D geometry as an auxiliary input or prediction target rather than the native foundation for world modeling. We present E0.5, a geometry-native world-action model built directly on 3D foundation models. E0.5 introduces two key innovations. First, it adopts a 3D foundation model as the primary backbone, making 3D geometry the native representation for both world modeling and action prediction. Second, it explicitly predicts future 3D states together with actions, enabling the model to capture geometric world dynamics beyond action-only modeling or future video prediction. Experiments on RoboTwin 2.0 first demonstrate the effectiveness of E0.5 without embodied-data pretraining, achieving success rates of 89.90\% and 50.09\% under clean and randomized settings, respectively. Building on these results, we further pretrain E0.5 on more than 160k robot trajectories from AgiBotWorld-Beta, jointly learning robot actions and future geometry within the pretrained 3D foundation. This embodied pretraining improves mean real-world manipulation success rates by approximately 15 and 7 percentage points on AgileX Piper and Zerith H1, respectively. Together, these results demonstrate the potential of geometry-native foundations to acquire robot interaction knowledge and transfer it to physical manipulation. E0.5 embodies this geometry-native approach as a member of the VWA family of world-action models.

</details>

#### 2026-10-26 - PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry

**Authors:** Yihang Chen, Bin Tan, Yujun Shen, Yinghao Xu, Nan Xue
**Links:** [abs](https://arxiv.org/abs/2610.34845) - [pdf](https://arxiv.org/pdf/2610.34845)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, DUSt3R, 3D reconstruction, SfM, SLAM, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PosePlaner: Denoising Any Feed-Forward Pose Predictor from Pairwise Planar Geometry
- 作者：Yihang Chen, Bin Tan, Yujun Shen, Yinghao Xu, Nan Xue
- 出版日期：2026-10-26T04:55:36Z
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（次分类）
- 链接：[摘要](https://arxiv.org/abs/2610.34845) / [PDF](https://arxiv.org/pdf/2610.34845)

### 一句话总结
PosePlaner 通过 flow matching 把位姿精化建模为条件生成问题，以粗几何匹配与初始位姿为条件，并将多个位姿假设融合为单一精化估计，从而在测试阶段为前馈位姿预测器提供基于几何证据的纠正机制。

### 研究问题
摘要指出，近期多视角 Transformer（如 DUSt3R、VGGT）将特征提取、匹配和位姿估计等经典 SfM/SLAM 流程子步骤合并为单次前馈推理，但这种“包含”隐藏了流水线各阶段之间的接口：对应关系、几何与位姿在单次前向中被纠缠在一起。由此带来的问题是：改进主要依赖有监督微调，且在测试阶段缺乏利用几何证据纠正预测的机制。

### 核心思路/方法
- 恢复对应关系与位姿之间的经典耦合，通过 flow matching 将位姿精化视为条件生成问题。
- 输入条件为粗几何匹配与初始位姿，输出为融合后的单一精化位姿估计。
- 该机制被描述为 RANSAC 投票的连续、数据驱动类比。
- 方法在两视角数据上高效训练，但可作为流式 n 视角位姿估计器的周期性精化器使用，且无需重新训练。

### 主要贡献
- 提出 PosePlaner，为前馈位姿预测器补充测试时可用的几何证据纠正机制。
- 将位姿精化表述为基于粗几何匹配和初始位姿的条件生成，并融合位姿假设。
- 在训练上仅使用两视角数据，却能服务于流式 n 视角位姿估计且无需重训练。
- 摘要报告的实验效果包括：纠正前馈预测器的失败、显著改进基于对应关系的求解器、减少长流式序列中的累积漂移。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集、定量指标、失败案例、计算开销或方法适用边界等细节，因此无法基于所给信息进一步判断局限性。

### 阅读优先级
中。理由：该工作针对前馈多视角位姿预测缺乏测试时几何纠正机制的问题，提出可插拔的周期性精化思路，并与经典几何求解器及流式长序列漂移问题相关；但摘要未提供定量结果与实现细节，是否值得优先精读取决于读者对前馈位姿估计、flow matching 位姿精化或流式 3D 重建方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Recent multi-view Transformers (e.g., DUSt3R and VGGT) have advanced 3D reconstruction by scaling training data and model capacity from two views to many views and long sequences, subsuming the classical SfM/SLAM pipeline of feature extraction, matching, and pose estimation in a single feed-forward pass. Yet this subsumption hides the interfaces between pipeline stages---correspondences, geometry, and pose are entangled in a single forward pass, leaving supervised fine-tuning as the major path to improvement and offering no mechanism to correct predictions from geometric evidence at test time. We propose PosePlaner to close this gap by reviving the classical coupling between correspondences and pose via flow matching, treating pose refinement as a conditional generation problem that takes coarse geometric matches and initial pose as input condition and fuses the resulting pose hypotheses into a single refined estimate, providing a continuous, data-driven analog of RANSAC voting. Our method is trained efficiently on two-view data, yet serves as a periodic refiner for streaming n-view pose estimators with no retraining. Empirically, it corrects failures of feed-forward predictors, substantially improves correspondence-based solvers, and reduces accumulated drift in long streaming sequences.

</details>

#### 2026-10-25 - Fovea-JEPA: Overcoming Geometric Blind Spots in V-JEPA for Camera Motion Recognition

**Authors:** Xiangkun Shi, Hanhui Li, Shiyue Zhang, Chang Liu, Junwen Pan, Zhenbang Sun, Xiaodan Liang
**Links:** [abs](https://arxiv.org/abs/2610.34033) - [pdf](https://arxiv.org/pdf/2610.34033)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fovea-JEPA: Overcoming Geometric Blind Spots in V-JEPA for Camera Motion Recognition
- 作者：Xiangkun Shi, Hanhui Li, Shiyue Zhang, Chang Liu, Junwen Pan, Zhenbang Sun, Xiaodan Liang
- 出版日期：2026-10-25T03:54:24Z
- 分类：主分类 Geometry Foundation Models；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.34033)｜[PDF](https://arxiv.org/pdf/2610.34033)

### 一句话总结
论文提出 Fovea-JEPA，用 VGGT 作为几何专家识别并弥补 V-JEPA 在相机运动识别中的“几何盲点”，通过介入伪标签和 token 级响应图实现视觉与几何特征的自适应融合。

### 研究问题
相机运动识别需要将相机平移、旋转或缩放造成的视角变化与物体运动、场景动态区分开。摘要指出，视频-语言模型常依赖语义线索，难以提供该任务所需的几何证据；V-JEPA 等联合嵌入预测架构虽具有较强时空表示，但实验显示其在部分区域对几何线索表示不足。摘要将这类区域称为“几何盲点”，并指出在时间反转监督下，V-JEPA 总体提升但在若干运动类别上退化，而一个较弱的、面向几何的 VGGT 预测器却在所有运动类别上均有提升。

### 核心思路/方法
- 以 V-JEPA 为基础模型，以 VGGT 作为几何专家。
- 根据二者的预测误差构造“介入伪标签”，用于弱监督一个盲点预测器。
- 盲点预测器输出 token 级响应图，并聚合为片段级介入分数。
- 使用该介入分数指导视觉特征与几何特征的自适应融合，以选择性引入互补几何信息，同时保留可靠的视觉预测。

### 主要贡献
- 识别并形式化 V-JEPA 在相机运动识别中的“几何盲点”问题。
- 提出 Fovea-JEPA，通过介入伪标签、盲点预测器和自适应融合机制，选择性引入 VGGT 的几何信息。
- 摘要报告在 CameraMotionDataset、CameraBench 和 ShotBench 上分别相对此前报告的最优基线提升 9.67、8.67 和 24.38 个百分点。

### 局限性
- 摘要未提供足够信息说明方法在不同相机运动类别上的细粒度表现、失败案例或计算开销。
- 摘要未提供足够信息说明“介入伪标签”的构造细节、盲点预测器的具体结构及训练稳定性。
- 摘要未提供足够信息说明三个数据集上的完整实验设置、消融结果与统计显著性。
- 代码与模型“录用后发布”，摘要未提供当前可复现性信息。

### 阅读优先级
高。理由：该论文直接针对 V-JEPA 的几何表示不足提出可操作的选择性融合方法，并在三个相机运动相关基准上报告了较大幅度提升；若关注视频几何表示、相机运动识别或基础模型互补融合，值得优先阅读。但需注意当前判断仅基于摘要，实验细节与可复现性信息尚不充分。

</details>

<details>
<summary>Abstract</summary>

Camera motion recognition requires separating viewpoint changes caused by camera translation, rotation, or zoom from object motion and scene dynamics. Video-language models often rely on semantic cues and struggle with the geometric evidence needed for this task. Joint-Embedding Predictive Architectures such as V-JEPA offer strong spatio-temporal representations, but our experiments suggest that they underrepresent geometric cues in some regions. Under temporal-reversal supervision, V-JEPA improves overall but degrades on several motion families, whereas a weaker geometry-oriented VGGT predictor improves across all families. We refer to these geometrically underrepresented regions as geometric blind spots and propose Fovea-JEPA to identify and address them. Using V-JEPA as the base model and VGGT as a geometry expert, we construct intervention pseudo-labels from their prediction errors to weakly supervise a blind-spot predictor. The predictor produces token-wise response maps, which are aggregated into a clip-level intervention score to guide adaptive fusion of visual and geometric features. This selective intervention introduces complementary geometric information while preserving reliable visual predictions. Experiments on CameraMotionDataset, CameraBench, and ShotBench demonstrate the effectiveness of Fovea-JEPA, with gains of 9.67, 8.67, and 24.38 percentage points over previously reported state-of-the-art baselines, respectively. Code and models will be released upon acceptance.

</details>

#### 2026-10-22 - MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model

**Authors:** Xinyang Lu, Shengzhe Wei, Sheng Tang, Weiqi Zhang, Juntong Fang, Zesong Li
**Links:** [abs](https://arxiv.org/abs/2610.31321) - [pdf](https://arxiv.org/pdf/2610.31321)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** geometry foundation model, VGGT, structure from motion, feature matching, NeRF, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model
- 作者：Xinyang Lu, Shengzhe Wei, Sheng Tang, Weiqi Zhang, Juntong Fang, Zesong Li
- 出版日期：2026-10-22T14:12:02Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.31321) / [PDF](https://arxiv.org/pdf/2610.31321)

### 一句话总结
MVLoMa 将稀疏局部特征匹配从图像对扩展到以中心图像和多个邻域图像构成的星形图，并借助冻结的多视图几何基础模型注入跨视角几何上下文，实现一次前向完成中心图像与所有邻域图像的匹配。

### 研究问题
论文指出，局部特征匹配通常按图像对建模，但 structure-from-motion 和视觉定位常需要将一幅参考图像与多个检索或共视邻域图像匹配。若独立地对每条中心—邻域边运行成对匹配器，会重复参考侧计算，且无法利用其余观测提供的互补多视图几何证据。

### 核心思路/方法
- 提出 MVLoMa，一种稀疏星形图匹配器，将 LoMa 从图像对扩展到多视图。
- 首先使用冻结的多视图几何模型联合描述星形图中的所有图像，并将得到的跨视角几何上下文注入局部描述子。
- 随后通过逐视图自注意力和双向中心—邻域交叉注意力，在一次前向中完成中心图像与所有邻域图像的匹配。
- 监督方面，仅从深度有效且相互可见的稠密 warp 中推导正对应，并显式惩罚违反极几何的高置信匹配。
- 摘要称同一设计支持四种冻结几何编码器：DA3、$π^3$、VGGT 和 VGGT-$Ω$；其中 DA3-Giant 在所有报告的编码器消融指标上表现最好。

### 主要贡献
- 将稀疏局部特征匹配从成对形式扩展到多视图星形图形式，减少中心—邻域边逐对独立匹配的重复计算。
- 利用冻结的多视图几何基础模型为局部描述子提供跨视角几何上下文。
- 设计一次前向的多视图匹配机制，结合逐视图自注意力与双向中心—邻域交叉注意力。
- 提出基于深度有效、相互可见稠密 warp 的正对应监督，并加入违反极几何的负监督。
- 摘要报告在 HyperSim、ScanNet++、Mip-NeRF 360 和 Tanks and Temples 的 25 视图星形图上，三个阈值下的 macro-average relative-pose AUC 均为 58.65/85.41/90.99，且匹配器比顺序评估 24 条中心—邻域边快 2.20 倍。
- 通过受控消融隔离几何感知描述子、可见性过滤、几何负监督和联合多视图推理的作用。

### 局限性
- 摘要未提供足够信息说明方法在非星形图结构、动态场景或大规模视图数量下的表现。
- 摘要未提供足够信息说明对几何基础模型冻结权重的依赖程度、推理显存开销及失败案例。
- 摘要未提供足够信息给出完整实验设置、数据集划分、基线细节和消融的具体数值。
- 摘要未提供足够信息讨论实际部署中的鲁棒性、实时性边界和泛化范围。

### 阅读优先级
高。理由：该论文直接针对多视图局部特征匹配中的重复计算与多视图几何证据利用问题，问题定义清晰；摘要给出了明确的速度提升和位姿 AUC 结果，并涉及多种冻结几何基础模型的适配与消融，对 3D 重建、视觉定位和多视图几何方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Local feature matching is typically formulated for image pairs, although structure-from-motion and visual localization commonly match one reference image against many retrieved or covisible neighbours. Applying a pairwise matcher independently to these centre-neighbour edges duplicates reference-side computation and prevents the matcher from exploiting complementary multi-view geometric evidence from the remaining observations. To address these limitations, we introduce MVLoMa, a sparse star-graph matcher that extends LoMa from image pairs to multiple views. MVLoMa first uses a frozen multi-view geometry model to jointly describe all images in a star, then injects the resulting cross-view geometric context into local descriptors. It then matches the centre image to all neighbours in a single forward pass through per-view self-attention and bidirectional centre-neighbour cross-attention. For supervision, we derive positive correspondences only from depth-valid, mutually visible dense warps and explicitly penalize high-confidence matches that violate epipolar geometry. On 25-view star graphs from HyperSim, ScanNet++, Mip-NeRF 360, and Tanks and Temples, MVLoMa obtains the best macro-average relative-pose AUC among the compared methods at all three thresholds (58.65/85.41/90.99). Its matcher is 2.20 times faster than sequential evaluation of the 24 centre-neighbour edges. The same design supports four tested frozen geometry encoders -- DA3, $π^3$, VGGT, and VGGT-$Ω$ -- with DA3-Giant performing best on all reported encoder-ablation metrics. Controlled ablations further isolate the effects of geometry-aware descriptors, visibility filtering, geometric negative supervision, and joint multi-view inference.

</details>

#### 2026-10-22 - WildDepth-v2: A Synchronized RGB--LiDAR--Radar Dataset and Benchmark for Metric Depth, Motion, and Tracking of Wildlife

**Authors:** Muhammad Aamir, Sangyun Shin, Naoya Muramatsu, Matthew Wijers, Amir Patel, Andrew Loveridge, Andrew Markham
**Links:** [abs](https://arxiv.org/abs/2610.31123) - [pdf](https://arxiv.org/pdf/2610.31123)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** metric depth, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WildDepth-v2: A Synchronized RGB--LiDAR--Radar Dataset and Benchmark for Metric Depth, Motion, and Tracking of Wildlife
- 作者：Muhammad Aamir, Sangyun Shin, Naoya Muramatsu, Matthew Wijers, Amir Patel, Andrew Loveridge, Andrew Markham
- 出版日期：2026-10-22T11:40:54Z
- 分类：主分类 Geometry Foundation Models；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.31123) / [PDF](https://arxiv.org/pdf/2610.31123)

### 一句话总结
论文发布 WildDepth-v2 数据集，在同步 RGB--LiDAR 野生动物数据基础上加入成像雷达，并提供用于度量深度、运动与跟踪的基准与评测。

### 研究问题
摘要指出，野生动物距离与运动（以米制单位）的测量是丰度估计、形态测量和运动生态学的基础；但单目视频缺乏度量尺度，现有野生动物数据集也缺乏度量真值。论文在此基础上进一步关注：如何利用雷达与 LiDAR 等信息提升野生动物度量距离、深度补全、3D 轨迹与运动分析的精度。

### 核心思路/方法
- **数据扩展**：在同步 RGB--LiDAR 的 WildDepth 数据集基础上，新增 37 个 RGB--LiDAR--4D 雷达序列（19,716 帧），包含逐点多普勒速度与测量误差预算，摘要称其为首批成像雷达野生动物记录。
- **基准评测**：构建冻结、带校验和的隐藏测试集，用于 RGB-only 距离估计与 RGB+稀疏 LiDAR 深度补全，并分别在动物像素与背景像素上评估。
- **运动与跟踪**：利用 LiDAR、雷达或单目深度将 2D 轨迹提升为度量 3D 轨迹，比较不同标定与提升方式的效果。

### 主要贡献
- 发布带成像雷达的同步 RGB--LiDAR--4D 雷达野生动物数据集，包含逐点多普勒速度与测量误差预算。
- 提供隐藏测试集与评测设置，覆盖 RGB-only 距离估计和 RGB+稀疏 LiDAR 深度补全，并区分动物与背景像素。
- 在 48,723 个动物帧上表明：对象级雷达标定可改善单目深度（AbsRel 0.120 对场景级 LiDAR 标定的 0.198），且推理时无需 LiDAR；但动物级 LiDAR 标定仍更准确（0.052）。
- 在 431 条轨迹上表明：每条轨迹一次的雷达缩放可将 3D 位置误差从 2.20 m 降至 0.58 m（约四倍），并将距离采样检测函数偏差从 -13% 降至 -2%，与每条轨迹一次的 LiDAR 标定相当。
- 将雷达多普勒迁移到 LiDAR 可生成更密集的运动掩码（密度为单独雷达的 3.7 倍，精度 72%），降低运动动物 LiDAR 累积误差 37%，并估计径向速度（r = 0.60），但存在约 50% 低估。

### 局限性
- 摘要明确给出部分方法仍存在误差：雷达迁移运动掩码精度为 72%；径向速度估计虽相关（r = 0.60）但约低估 50%；对象级雷达标定的单目深度精度仍低于动物级 LiDAR 标定。
- 关于数据采集地点、物种范围、传感器具体型号、标注协议、计算成本、泛化到其他物种或环境的表现等，**摘要未提供足够信息**。

### 阅读优先级
**中**。理由：论文涉及野生动物度量深度、3D 跟踪与 RGB--LiDAR--雷达多模态数据，且提供隐藏测试集与多项定量基准；若关注多模态深度估计、雷达辅助标定或生态监测中的度量视觉，具有参考价值。但摘要未提供数据规模之外的采集细节与泛化评估，是否高优先级取决于读者对野生动物场景或多模态基准的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Measuring animal distance and motion in metric units underpins abundance estimation, morphometrics, and movement ecology, yet monocular video lacks metric scale and wildlife datasets lack metric ground truth. We present WildDepth 2, extending the synchronized RGB-LiDAR WildDepth dataset in three directions. (i) Imaging radar: 37 RGB-LiDAR-4D-radar sequences (19,716 frames) with per-point Doppler velocity and a measured error budget, to our knowledge the first imaging-radar wildlife recordings. (ii) Benchmarking: a frozen, checksummed hidden test set for RGB-only distance estimation and RGB+sparse-LiDAR depth completion, evaluated separately on animal and background pixels. (iii) Motion and tracking: metric 3D trajectories obtained by lifting 2D tracks using LiDAR, radar, or monocular depth. Across 48,723 animal frames, object-level radar calibration improves monocular depth over scene-level LiDAR calibration without requiring LiDAR at inference (AbsRel 0.120 vs. 0.198), although animal-level LiDAR remains more accurate (0.052). Across 431 tracks, once-per-track radar scaling reduces 3D position error four-fold (2.20 to 0.58 m) and distance-sampling detection-function bias from -13% to -2%, matching once-per-track LiDAR calibration. Transferring radar Doppler onto LiDAR produces motion masks 3.7 times denser than radar alone at 72% precision, reduces moving-animal LiDAR accumulation error by 37%, and estimates radial speed (r = 0.60), albeit with approximately 50% underestimation.

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-27 - 4D Reconstruction with Events & RGB

**Authors:** Dulanga Weerakoon, Darshana Rathnayake, Van Minh Do, Hemanth Sabbella, Kaichen Zhou, Fangneng Zhan, Alok Prakash, Sanjay E. Sarma, Archan Misra, Paul Pu Liang
**Links:** [abs](https://arxiv.org/abs/2610.36610) - [pdf](https://arxiv.org/pdf/2610.36610)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, dynamic 3D, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4D Reconstruction with Events & RGB
- 作者：Dulanga Weerakoon, Darshana Rathnayake, Van Minh Do, Hemanth Sabbella, Kaichen Zhou, Fangneng Zhan, Alok Prakash, Sanjay E. Sarma, Archan Misra, Paul Pu Liang
- 出版日期：2026-10-27T04:11:39Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.36610 ；PDF https://arxiv.org/pdf/2610.36610

### 一句话总结
该初步研究在现有纯 RGB 的 4D 重建模型 Monst3R 上增加一个事件相机输入分支，其余架构不变，在 3 个基准数据集上相对纯 RGB 基线平均降低 Abs Rel 3.4%，且改进随相机与物体运动幅度增大而更明显。

### 研究问题
从单一运动相机重建随时间变化的动态 3D 场景（4D 重建）对机器人与 AR/VR 应用很重要，但现有前馈方法仅依赖 RGB 帧，因而继承传统相机的失效模式，包括快速或非均匀相机与物体运动下的运动模糊和时间混叠。事件相机以微秒分辨率异步报告逐像素亮度变化，提供互补信号且基本不受上述伪影影响；问题是能否在不做完整架构重设计的情况下，把这一模态纳入现有基于 RGB 的 4D 重建流程。

### 核心思路/方法
论文进行一项初步研究，采用最小扩展：在已有的纯 RGB 4D 重建模型 Monst3R 上增加一个额外的事件相机输入分支，并保持架构其余部分不变。摘要将其描述为简单的 RGB-事件融合，并在 3 个基准数据集上评估。

### 主要贡献
- 提出并验证一种轻量、非侵入式的事件数据融合方式：仅为 Monst3R 增加事件输入分支，其余架构不变。
- 在 3 个基准数据集上，相对纯 RGB 的 Monst3R 基线，Abs Rel 平均降低 3.4%。
- 敏感性分析显示改进随相机和物体运动幅度增大而增长，在纯 RGB 重建退化最严重的高物体运动条件下增益最大。
- 作者据此认为，即使是轻量、非侵入式的事件数据融合也能实质提升 4D 重建鲁棒性，并以此动机推动未来更系统的架构研究。

### 局限性
- 摘要明确称其为 preliminary study（初步研究），并非完整架构探索。
- 仅报告 Abs Rel 平均降低 3.4% 及敏感性趋势；其他指标、数据集名称、具体实验设置与统计细节摘要未提供足够信息。
- 方法仅为在 Monst3R 上增加事件分支的最小扩展，未进行架构重设计；更系统的架构研究被留作未来工作。
- 事件相机数据采集条件、事件与 RGB 的同步/对齐方式、失败案例分析等摘要未提供足够信息。

### 阅读优先级
中。理由：主题属于动态/4D 重建与机器人、AR/VR 应用交叉方向，问题明确且事件相机与 RGB 融合的思路直接；但摘要定位为初步研究，方法为最小扩展，定量结果仅给出 Abs Rel 平均 3.4% 的相对改进，实验细节与架构创新有限。对关注事件相机用于 4D 重建或希望了解轻量融合可行性的读者有参考价值，对追求完整方法或充分实验对比的读者优先级较低。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic 3D scenes over time (4D reconstruction) from a single moving camera is central to robotics and AR/VR applications, yet state-of the-art feed-forward methods rely solely on RGB frames and therefore inherit the failure modes of conventional cameras, including motion blur and temporal aliasing under fast or non-uniform camera and object motion. Event cameras report per-pixel brightness changes asynchronously at microsecond resolution, offering a complementary signal that is largely immune to these artifacts, but whether this modality can be incorporated into existing RGB based 4D reconstruction pipelines without a full architectural redesign remains an open question. In this preliminary study, we investigate a minimal extension: we augment Monst3R, an existing RGB-only 4D reconstruction model, with an additional event-camera input branch, leaving the rest of the architecture unchanged. Across 3 benchmark datasets, this simple RGB-event fusion reduces Abs Rel by 3.4% on average relative to the RGB-only Monst3R baseline, and a sensitivity analysis shows that the improvement grows with the magnitude of camera and object motion, with the largest gains observed under high object motion conditions where RGB-only reconstruction degrades most. These early results suggest that even a lightweight, non-invasive fusion of event data can meaningfully improve 4D reconstruction robustness, motivating a more thorough architectural investigation in future work.

</details>

#### 2026-10-26 - GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting

**Authors:** Tom Yachil, Andrei Sharf
**Links:** [abs](https://arxiv.org/abs/2610.35224) - [pdf](https://arxiv.org/pdf/2610.35224)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting
- 作者：Tom Yachil, Andrei Sharf
- 出版日期：2026-10-26T11:14:09Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.35224) / [PDF](https://arxiv.org/pdf/2610.35224)

### 一句话总结
该论文提出 GaussianSpline，用自适应的非均匀分段三次 Bézier 样条建模每个高斯的运动，并联合学习控制点与时间分段，以提升高度动态场景的 4D Gaussian Splatting 重建质量。

### 研究问题
现有动态 4D Gaussian Splatting 方法常基于全局形变、固定阶多项式或均匀参数化样条，摘要指出这些方式难以同时兼顾复杂快速运动与近静态区域的紧凑表示；论文关注如何在每个高斯的轨迹表示中实现全局平滑与局部自适应。

### 核心思路/方法
- 对每个高斯使用自适应、非均匀的分段三次 Bézier 样条建模运动。
- 联合学习 Bézier 控制点与每个高斯轨迹的时间划分，而非采用全局形变、固定阶多项式或均匀参数化样条。
- 该自适应表示将更多时间容量分配给高度动态区域，同时让近静态区域保持紧凑轨迹。
- 使用基于控制点反射的约束，在相邻 Bézier 段之间施加 \(G^1\) 连续性，以兼顾全局平滑运动与局部自适应。
- 摘要称由此获得平滑、完全可微的轨迹，同时保留非均匀时间参数化的灵活性。

### 主要贡献
- 提出 GaussianSpline：一种基于自适应非均匀分段三次 Bézier 样条逐高斯运动的动态 4D Gaussian Splatting 方法。
- 联合学习 Bézier 控制点和每个高斯轨迹的时间分区，实现动态区域与近静态区域之间的时间容量自适应分配。
- 通过反射式控制点约束实现相邻 Bézier 段间的 \(G^1\) 连续性，支持平滑且完全可微的轨迹。
- 摘要报告在 Neural 3D Video benchmark、Google Immersive dataset 以及合成场景上的实验表明：在高度非均匀和困难动态场景中重建质量显著提升，同时在一般动态场景上与先进 4D Gaussian Splatting 方法保持有竞争力的性能。

### 局限性
- 摘要未提供足够信息说明方法的具体计算开销、训练时间或内存占用。
- 摘要未提供足够信息说明 Bézier 段数量、时间分区策略的超参数敏感性或失败案例。
- 摘要未提供足够信息说明在极端运动、遮挡或稀疏视角下的具体表现。
- 摘要未提供足够信息说明与各基线方法的完整定量对比细节。

### 阅读优先级
中。理由：该论文聚焦 4D Gaussian Splatting 中逐高斯自适应样条运动表示，问题和方法描述较清晰，且摘要声称在高度动态场景上有明显改进；但当前仅有摘要与元数据，缺少定量结果和实现细节，适合作为动态/4D 重建方向的候选阅读，需进一步查看全文后再判断优先级是否提升。

</details>

<details>
<summary>Abstract</summary>

We present GaussianSpline, a dynamic 4D Gaussian Splatting method that models per-Gaussian motion using adaptive, non-uniform piecewise cubic Bézier splines. Unlike approaches based on global deformations, fixed-order polynomials, or uniformly parameterized splines, GaussianSpline jointly learns the Bézier control points and the temporal partition of each Gaussian's trajectory. This adaptive representation allocates greater temporal capacity to highly dynamic regions while maintaining compact trajectories for near-static regions, enabling high-fidelity reconstruction of complex and rapidly changing motion. To jointly achieve globally smooth motion and local adaptivity, we enforce $G^1$ continuity between consecutive Bézier segments using a reflection-based constraint on their control points. This produces smooth, fully differentiable trajectories while preserving the flexibility of non-uniform temporal parameterization. Experiments on the Neural 3D Video benchmark, the Google Immersive dataset, as well as on synthetic scenes demonstrate that GaussianSpline substantially improves reconstruction quality in scenes with highly non-uniform and challenging dynamics, while maintaining competitive performance on general dynamic scenes compared with state-of-the-art 4D Gaussian Splatting methods.

</details>

#### 2026-10-26 - DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction

**Authors:** Beizhen Zhao, Nanjie Yao, Boyi Fu, Qingsong Yan, Haofan Ren, Kaiyong Zhao, Hao Wang
**Links:** [abs](https://arxiv.org/abs/2610.35002) - [pdf](https://arxiv.org/pdf/2610.35002)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction
- 作者：Beizhen Zhao, Nanjie Yao, Boyi Fu, Qingsong Yan, Haofan Ren, Kaiyong Zhao, Hao Wang
- 出版日期：2026-10-26T08:14:00Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.35002 ；PDF https://arxiv.org/pdf/2610.35002

### 一句话总结
论文提出 DUET4D，一个面向稀疏视角 4D 高斯泼溅的自校正耦合引导框架，用当前 4D 表示反向引导生成先验，以提供时空一致的监督，并抑制冗余基元与漂浮伪影。

### 研究问题
稀疏视角 4D 重建在仅有少量相机时高度欠约束。摘要指出：生成先验可恢复缺失外观，但视频模型用于迭代重建在计算上不现实，而单视图模型产生的伪观测在时间上不一致；此外，将不确定的生成输出直接吸收进高斯优化，常导致冗余基元与漂浮伪影。

### 核心思路/方法
- 总体框架：DUET4D 是用于稀疏视角 4D 高斯泼溅的自校正耦合引导框架。
- 自校正循环：4D 表示引导生成先验，生成先验再为 4D 表示提供时空一致的监督。
- 具体步骤一：从当前高斯证据构建序列对齐，用于引导潜空间恢复。
- 具体步骤二：使用 Sequential Fidelity Resampling 将生成监督提升到高斯空间，以选择性区分被重复支持的基元。
- 循环机制：校正后的表示再为下一轮恢复提供更可靠的高斯证据。
- 摘要未提供足够信息说明网络结构细节、损失函数形式、训练数据与具体实现参数。

### 主要贡献
- 提出 DUET4D，将稀疏视角 4D 重建表述为“4D 表示—生成先验”耦合的自校正引导过程。
- 设计从当前高斯证据到潜空间恢复的序列对齐机制，以引导生成先验。
- 提出 Sequential Fidelity Resampling，将生成监督提升到高斯空间并筛选被重复支持的基元，以缓解冗余基元与漂浮伪影。
- 摘要称大量实验表明该方法显著提升渲染质量与渲染效率；具体数据集、指标与对比方法摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法对相机数量下限、视角分布、动态复杂度或生成先验质量的敏感性。
- 摘要未提供足够信息说明计算开销、迭代轮数、收敛性及失败案例。
- 摘要未提供足够信息说明与视频模型、单视图模型及其他稀疏视角 4D 方法的定量对比细节。
- 摘要未提供足够信息说明 Sequential Fidelity Resampling 的阈值设计、消融实验与统计显著性。

### 阅读优先级
中。理由：该论文聚焦稀疏视角 4D 重建中生成先验与高斯优化的耦合问题，问题定义清晰，方法包含自校正循环与重采样筛选，对动态 4D 重建与神经渲染方向有潜在参考价值；但摘要未给出定量结果、数据集与实现细节，需阅读全文后才能判断其实际效果与可复现性。

</details>

<details>
<summary>Abstract</summary>

Sparse-view 4D reconstruction is highly under-constrained when only a few cameras are available. Generative priors can recover missing appearances, but video models are computationally impractical for iterative reconstruction, whereas single-view models produce temporally inconsistent pseudo-observations. Moreover, directly absorbing uncertain generative outputs into Gaussian optimization often creates redundant primitives and floating artifacts. To address these challenges, we propose DUET4D, a self-corrective coupled guidance framework for sparse-view 4D Gaussian splatting. The core of our approach is a self-corrective framework where the 4D representation guides generative prior for spatio-temporal consistent supervisions. We first construct sequential alignments from current Gaussian evidence to steer the latent restoration. Then we use Sequential Fidelity Resampling to lift generative supervisions into Gaussian space to selectively distinguish repeatedly supported primitives. The corrected representation then provides more reliable Gaussian evidence for the next restoration cycle. Extensive experiments demonstrate that DUET4D significantly improves rendering quality and rendering efficiency.

</details>

#### 2026-10-26 - DimFlow: Bidirectional Grid-Expert Learning for Dynamic Gaussian Reconstruction

**Authors:** Gabriel Adineera, Jinoh Kim
**Links:** [abs](https://arxiv.org/abs/2610.34952) - [pdf](https://arxiv.org/pdf/2610.34952)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, NeRF, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DimFlow: Bidirectional Grid-Expert Learning for Dynamic Gaussian Reconstruction
- 作者：Gabriel Adineera, Jinoh Kim
- 出版日期：2026-10-26T07:20:03Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.34952 ；PDF https://arxiv.org/pdf/2610.34952

### 一句话总结
DimFlow 通过多分辨率网格与坐标专家分支的双向交互学习动态高斯重建所需的紧凑场景特征，并在 D-NeRF、HyperNeRF、DAVIS 的汇总比较中报告 39.73 dB PSNR、85 FPS 与 18.9 MB 模型体积。

### 研究问题
动态高斯重建需要紧凑的场景特征来支持几何与外观的协同变化。分解式网格能提供高效的局部查询，但仅靠准确的插值并不能保证所得动态属性在空间和时间上保持兼容。论文要解决的是：如何学习这类特征，使其在空间与时间维度上具有兼容性，并支撑后续动态高斯渲染。

### 核心思路/方法
DimFlow 让多分辨率网格与基于坐标的专家分支进行双向交互来学习特征。具体包括：
- 特征级对抗对齐：连接网格与专家分支的特征分布；
- 自适应融合：传递互补信息；
- 激活掩码残差反馈：在训练过程中细化网格；
- 四个属性专家：分别组织形变、旋转、不透明度与时间信息，再进入高斯渲染。

### 主要贡献
- 提出 DimFlow 框架，以网格—专家分支的双向交互学习动态高斯重建特征。
- 引入特征级对抗对齐、自适应融合与激活掩码残差反馈，用于连接分布、传递互补信息并在训练中细化网格。
- 设计四个属性专家，分别组织形变、旋转、不透明度与时间信息。
- 在 D-NeRF、HyperNeRF、DAVIS 的汇总比较中报告 39.73 dB PSNR，较 4D-GS 提升 1.92 dB，并匹配其报告的 85 FPS 渲染速度；模型体积 18.9 MB，4D-GS 为 18.3 MB。
- 组件与属性专家消融显示特征对齐、自适应交换与时间处理的互补贡献。

### 局限性
- 摘要仅给出汇总比较结果，未提供各数据集上的逐项指标、训练设置、运行环境与误差分析；“摘要未提供足够信息”。
- 摘要未说明特征级对抗对齐、自适应融合与激活掩码残差反馈的具体实现细节与超参数；“摘要未提供足够信息”。
- 摘要未给出失败案例、边界条件或与其他方法在内存、训练时间等方面的完整对比；“摘要未提供足够信息”。
- 摘要提到模型体积 18.9 MB 略高于 4D-GS 的 18.3 MB，但未讨论该差异的影响；“摘要未提供足够信息”。

### 阅读优先级
中。理由：论文聚焦动态/4D 高斯重建中的网格—专家双向特征学习，报告了 PSNR、FPS 与模型体积的汇总结果，并包含组件与属性专家消融，与动态高斯重建和神经场景表示方向直接相关；但摘要未提供逐数据集细节、训练配置与完整局限性分析，需阅读全文才能判断方法稳健性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Dynamic Gaussian reconstruction requires compact scene features to support coordinated changes in geometry and appearance. A factorized grid provides efficient local queries, but accurate interpolation alone does not ensure that the resulting dynamic attributes remain compatible across space and time. We introduce DimFlow, a framework that learns these features through bidirectional interaction between a multi-resolution grid and a coordinate-based expert branch. Feature-level adversarial alignment connects their distributions, adaptive fusion transfers complementary information, and activation-masked residual feedback refines the grid during training. Four attribute experts organize deformation, rotation, opacity, and temporal information before Gaussian rendering. In the aggregate comparison across D-NeRF, HyperNeRF, and DAVIS, DimFlow achieves 39.73 dB PSNR, improving on 4D-GS by 1.92 dB while matching its reported 85 FPS rendering speed. The model occupies 18.9 MB, compared with 18.3 MB for 4D-GS. Component and attribute-expert ablations reveal complementary contributions from feature alignment, adaptive exchange, and temporal processing.

</details>

#### 2026-10-22 - Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention

**Authors:** Wei Zhang, Ying Feng, Mengtong Wu, Shiqiang Gong, Huaqi Zhang, Qi Zhang
**Links:** [abs](https://arxiv.org/abs/2610.31320) - [pdf](https://arxiv.org/pdf/2610.31320)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 4D reconstruction, scene reconstruction, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention
- 作者：Wei Zhang, Ying Feng, Mengtong Wu, Shiqiang Gong, Huaqi Zhang, Qi Zhang
- 出版日期：2026-10-22T14:11:34Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 3D Reconstruction & Multi-view Geometry
- 链接：abstract_url: https://arxiv.org/abs/2610.31320；pdf_url: https://arxiv.org/pdf/2610.31320

### 一句话总结
Stream4D 提出一种无需训练的流式 4D 重建框架，利用因果注意力 KV 缓存中的时序运动线索生成动态掩码，并通过软键掩码抑制动态区域干扰，以改善相机位姿估计和长序列重建中的鬼影问题。

### 研究问题
现有流式 4D 重建方法通常假设场景是静态的，因此在包含动态物体的长序列中，会出现位姿漂移和鬼影伪影。论文关注的问题是如何在不重新训练模型的前提下，将静态区域与动态区域解耦，并提升流式重建对动态场景的鲁棒性。

### 核心思路/方法
论文提出 Stream4D，一个无需训练、运动解耦的流式重建框架，可直接集成到因果 Transformer 主干（如 StreamVGGT、Stream3R）中。其核心观察是因果注意力在 KV 缓存中隐式编码了丰富的时序运动线索。方法从多个注意力层和时间窗口中自适应聚合这些线索，并与深度先验融合，以处理遮挡和无纹理区域等困难情况，从而生成精确的动态掩码，实现静态与动态区域解耦。随后采用软键掩码方案，利用动态掩码抑制因果注意力中动态区域的干扰，以提高相机位姿估计精度。Stream4D 继承了因果注意力的效率，并与现有流式架构保持兼容。

### 主要贡献
- 提出无需训练的 Stream4D 流式 4D 重建框架，可直接集成到因果 Transformer 主干中。
- 利用因果注意力 KV 缓存中的时序运动线索，并结合多注意力层、多时间窗口聚合与深度先验，生成动态掩码以解耦静态和动态区域。
- 引入软键掩码方案，利用动态掩码抑制动态区域对因果注意力的干扰，从而改善相机位姿估计。
- 摘要称在多种动态场景基准上显著提升相机位姿估计和静态场景重建质量，生成可靠动态掩码，并有效缓解长序列鬼影。

### 局限性
摘要未提供足够信息。论文未在摘要中给出具体实验设置、数据集规模、定量指标、失败案例或计算开销等细节，因此无法基于摘要进一步判断其局限性。

### 阅读优先级
高。理由：该论文直接针对流式 4D 重建中动态场景处理的关键问题，提出无需训练且可兼容现有因果 Transformer 架构的方法，若摘要所述效果成立，对动态 / 4D 重建与多视图几何方向具有较高参考价值；但需注意摘要未提供定量实验细节，阅读时应重点核查实验验证与适用边界。

</details>

<details>
<summary>Abstract</summary>

4D scene reconstruction requires robust handling of dynamic objects, yet existing streaming methods commonly assume static scenes, leading to pose drift and ghosting artifacts over long sequences. We introduce Stream4D, a training-free, motion-decoupled streaming reconstruction framework that can be directly integrated into causal Transformer backbones (e.g., StreamVGGT, Stream3R). Our key observation is that causal attention implicitly encodes rich temporal motion cues within the KV cache. We adaptively aggregate these cues from multiple attention layers and across temporal windows, and fuse them with depth priors to handle challenging cases such as occlusions and textureless regions, producing precise dynamic masks that decouple static and dynamic regions. We then apply a soft key masking scheme that leverages these dynamic masks to suppress interference from dynamic regions in causal attention, thereby improving camera pose estimation accuracy. Stream4D inherits the efficiency of causal attention and remains compatible with existing streaming architectures. On diverse dynamic-scene benchmarks, Stream4D significantly improves camera pose estimation and static-scene reconstruction quality, yields reliable dynamic masks, and effectively mitigates long-sequence ghosting.

</details>

#### 2026-10-21 - R4DGS: Referring Segmentation in 4D Gaussian Splatting

**Authors:** Bangpu Chen, Yaxuan Li, Shirui Peng, Xiangtian Si, Liuxin Chu, Xitong Cao, Hongbo Jin, Jiayu Ding
**Links:** [abs](https://arxiv.org/abs/2610.30326) - [pdf](https://arxiv.org/pdf/2610.30326)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：R4DGS: Referring Segmentation in 4D Gaussian Splatting
- 作者：Bangpu Chen, Yaxuan Li, Shirui Peng, Xiangtian Si, Liuxin Chu, Xitong Cao, Hongbo Jin, Jiayu Ding
- 出版日期：2026-10-21T18:42:09Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.30326 ；PDF https://arxiv.org/pdf/2610.30326 ；项目页 https://chenbangpu.github.io/R4DGS/

### 一句话总结
论文提出 Referring 4D Gaussian Splatting（R4DGS）任务及配套基准 R4D-Bench-QA，并提出无需场景特定语义优化的统一框架 ReferGaussian，用于动态 4D 场景中基于自然语言指代的定位与分割。

### 研究问题
现有基于 4D Gaussian Splatting（4DGS）的动态表示在重建与渲染方面表现较强，但在动态场景中支持复杂自然语言指代方面仍有限。已有 4D Gaussian 方法主要面向渲染导向的动态建模，而语义扩展往往依赖场景特定的语义优化，或在相对简单的查询设置下评估。论文关注的问题包括：在动态 4D 场景中处理随时间变化、多目标或推理密集型、零目标或干扰项表达式的指代定位。

### 核心思路/方法
论文将任务定义为 Referring 4D Gaussian Splatting（R4DGS），并构建 R4D-Bench-QA 基准，提供结构化查询标注。方法上提出 ReferGaussian 统一框架：以 4DGS 为基础，将低层动态 Gaussians 转换为持久、可由语言寻址的实体；通过 EntityBank 组织带 mask 支持的 Gaussian 实体；利用多模态大语言模型（MLLMs）将复杂查询分解为可跟踪的对象短语与结构化指代约束；执行约束感知的 grounding，且不依赖场景特定语义优化，实现训练无关的指代推理。

### 主要贡献
- 提出并研究 R4DGS 任务，覆盖动态场景中时间变化、多目标或推理密集型、零目标或干扰项等自然语言指代设置。
- 构建 R4D-Bench-QA 基准，提供结构化查询标注以支持该任务评估。
- 提出 ReferGaussian 统一框架，将动态 Gaussians 组织为语言可寻址实体，并结合 MLLM 查询分解与约束感知 grounding，实现无需场景特定语义优化的指代推理。
- 在 R4D-Bench-QA 与 4D LangSplat 协议上的实验表明，时间目标选择有所改进，并在无场景特定语义训练条件下取得有竞争力的时空 grounding 表现。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、计算开销、对 MLLM 或 mask 质量的依赖程度、基准规模与标注细节，也未给出定量实验结果和对比方法细节。

### 阅读优先级
中。理由：该论文提出新任务、新基准与新框架，问题定义清晰，且强调训练无关与免场景特定语义优化，对 4D 动态场景理解与语言 grounding 方向具有参考价值；但当前信息仅来自摘要，缺少定量结果、实现细节与局限性分析，需阅读全文后再判断其方法有效性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Dynamic representations based on 4D Gaussian Splatting (4DGS) have shown strong capabilities in reconstruction and rendering, yet current methods remain limited in supporting complex natural-language referring in dynamic scenes. Existing 4D Gaussian methods are primarily designed for rendering-oriented dynamic modeling, while current semantic extensions often rely on scene-specific semantic optimization or are evaluated on relatively simple query settings. In this paper, we study Referring 4D Gaussian Splatting (R4DGS), a task for grounding temporally varying, multi-target or reasoning-intensive, and zero-target or distractor expressions in dynamic 4D scenes. To support this task, we introduce R4D-Bench-QA, a benchmark with structured query annotations. We further present ReferGaussian, a unified framework built upon 4DGS that converts low-level dynamic Gaussians into persistent, language-addressable entities for training-free referring inference. ReferGaussian organizes mask-supported Gaussian entities in an EntityBank, uses Multimodal Large Language Models (MLLMs) to decompose complex queries into trackable object phrases and structured referring constraints, and performs constraint-aware grounding without scene-specific semantic optimization. Experiments on R4D-Bench-QA and the 4D LangSplat protocol demonstrate improved temporal target selection and competitive spatiotemporal grounding without scene-specific semantic training. Project resources are available at https://chenbangpu.github.io/R4DGS/.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-27 - Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction

**Authors:** Prakhar Kaushik, Soumava Paul, Alan Yuille
**Links:** [abs](https://arxiv.org/abs/2610.37668) - [pdf](https://arxiv.org/pdf/2610.37668)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, surface reconstruction, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction
- 作者：Prakhar Kaushik, Soumava Paul, Alan Yuille
- 出版日期：2026-10-27T17:59:59Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37668) / [PDF](https://arxiv.org/pdf/2610.37668)

### 一句话总结
论文提出一种平面六边形表面基元“Hexels”，它使用带一阶空间颜色场的更少、更大的基元来表示 2D 图像与 3D 场景，以改善内存和计算受限场景下的质量-效率权衡。

### 研究问题
新视角合成与 3D 重建虽因辐射场和 splatting 快速发展，但内存与计算需求限制了它们在资源受限环境中的使用。论文关注：如何用更紧凑的表面基元，在降低内存和计算开销的同时，保持或提升场景渲染与重建质量。

### 核心思路/方法
- 提出称为 **Hexels** 的平面六边形表面元素，并为每个基元引入 **一阶空间颜色场**，用于高效表示 3D 场景与 2D 图像。
- 利用局部平面区域及平滑变化的外观，采用**更少、更大**的基元。
- 六边形支撑域被描述为面积和边界高效的域，局部颜色场用于捕捉单个基元内部的外观变化。
- 摘要称其作为通用基元，也可改进 2D 图像表示。

### 主要贡献
- 提出 Hexels 这种紧凑六边形表面基元，并用于高效 3D 场景和 2D 图像表示。
- 在 34 个场景上，与内存匹配的 2DGS 相比，Hexels 在不同数据集上 PSNR 提升 **4.53–7.38 dB**，且训练 VRAM 更低。
- 消融显示：按每个基元比较，Hexels 相比 2DGS 最高提升 **4.74 dB**，训练 VRAM 更低，FPS 快 **2.31 倍**。
- 在 15 个 DTU 扫描上，与内存匹配的 2DGS 相比，3D 表面重建误差降低 **28.9%**。
- 在 6 个 Tanks and Temples 表面场景上，Hexels 取得对比方法中最高的平均 F1（**34.38%**，2DGS 为 **31.72%**）。
- 摘要还称 Hexels 在 2D 图像表示上优于 Image-GS，并推动表面对齐基元在质量-效率权衡上的 Pareto 前沿。

### 局限性
- 摘要未提供足够信息说明具体数据集名称、训练时长、参数量、推理内存等完整实验细节。
- 摘要未提供足够信息说明方法在不同尺度、非平面区域、复杂反射或透明材质等困难场景下的失效情况。
- 摘要未提供足够信息说明六边形基元初始化、优化稳定性及实现复杂度等工程限制。
- 摘要未提供足够信息说明与更多类型基元或方法的系统性对比范围。

### 阅读优先级
**高**。理由：论文直接针对表面基元表示的质量-效率权衡，摘要给出了多数据集、多任务的定量结果，并声称在渲染质量、训练内存、FPS 和表面重建误差上均有改进；对关注高效神经场景表示、3D 重建与渲染的读者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis and 3D reconstruction have advanced rapidly with radiance fields and splatting, yet their memory and computational demands limit their use in resource-constrained settings. We introduce Hexels: novel planar hexagonal surface elements with a first-order spatial color field for efficient 3D scene and 2D image representation. Hexels exploit locally planar regions with smoothly varying appearance using fewer, larger primitives. Their hexagonal support provides an area- and boundary-efficient domain, while the local color field captures appearance variation within each primitive. Across 34 scenes, Hexels improve PSNR over memory-matched 2DGS by 4.53-7.38 dB across datasets while requiring lower training VRAM. We further ablate Hexels by showing that per primitive, Hexels outperform 2DGS by upto 4.74 dB while using lower training VRAM and having 2.31 times faster FPS. Even in unconstrained settings, Hexels offers complementary quality-memory trade-offs. For efficient 3D surface reconstruction, Hexels reduce error by 28.9% compared with memory-matched 2DGS across 15 DTU scans. On 6 Tanks and Temples surface scenes, Hexels achieves the highest mean F1 among compared methods (34.38%, versus 31.72% for 2DGS). We further also show that Hexels, as a general primitive, improves 2D image representation over Image-GS. Hexels push the Pareto frontier on the quality-efficiency trade-off of surface-aligned primitives.

</details>

#### 2026-10-27 - GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling

**Authors:** Kang He, Wenshuo Peng, Chuanhao Li, Zihui Gao, Xiaojie Xu, Zhengyuan Lin, Yuzhe Ding, Donghong Ji, Kaipeng Zhang, Yongtao Ge
**Links:** [abs](https://arxiv.org/abs/2610.37257) - [pdf](https://arxiv.org/pdf/2610.37257)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** camera pose estimation, pose estimation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling
- 作者：Kang He, Wenshuo Peng, Chuanhao Li, Zihui Gao, Xiaojie Xu, Zhengyuan Lin, Yuzhe Ding, Donghong Ji, Kaipeng Zhang, Yongtao Ge
- 出版日期：2026-10-27T13:53:14Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.37257) / [PDF](https://arxiv.org/pdf/2610.37257)

### 一句话总结
论文提出分钟级游戏玩法视频数据集 GameVerse，用于缓解长时程交互式世界建模中长时程训练数据稀缺的问题。

### 研究问题
当前交互式世界模型在约一分钟 rollout 之后难以保持连贯性；作者认为该限制的根源在于长时程训练数据稀缺，而非模型容量不足。现有游戏视频数据集通常由不足十秒的片段构成，且字幕以粗粒度、未区分整体的文本描述整个片段，不足以支撑可控的长时程生成。

### 核心思路/方法
构建面向长时程交互式世界建模的分钟级游戏玩法视频数据集 GameVerse，并采用统一处理流程：场景一致性分割、质量过滤、相机位姿估计、基于事件的字幕标注。每个片段配有在数分钟内保持时间稳定的相机轨迹，以及将静态场景上下文与动态前景事件分离、并对齐事件边界而非固定时间窗口的字幕。

### 主要贡献
- 提出 GameVerse 数据集：包含 69.7K 片段，覆盖 1,655 小时、3.496 亿帧，涵盖多种第一人称与第三人称游戏玩法。
- 包含 1,358 小时的连续两分钟序列，规模比先前数据集长一个数量级。
- 设计统一数据处理流程，包括场景一致性分割、质量过滤、相机位姿估计与事件字幕标注。
- 每个片段配有时间稳定的相机轨迹，以及区分静态场景上下文与动态前景事件、对齐事件边界的字幕。
- 摘要称综合分析显示 GameVerse 在规模、多样性和标注质量上超过现有公开数据集；实验表明在其上训练可显著延长交互式世界模型的时间跨度。

### 局限性
- 摘要未提供足够信息说明具体的实验设置、对比基线、评价指标及定量结果。
- 摘要未提供足够信息说明数据集在游戏类型、视觉风格或平台上的具体覆盖范围与潜在偏差。
- 摘要未提供足够信息说明标注流程的人工参与程度、标注一致性评估或质量控制细节。
- 摘要未提供足够信息说明相机位姿估计与场景一致性分割的具体方法及其误差影响。
- 摘要未提供足够信息说明数据集的许可、伦理审查或使用限制。

### 阅读优先级
中。理由：该论文聚焦长时程交互式世界建模的数据瓶颈，数据集规模与序列长度在摘要中有明确量化描述，并与 3D 重建、多视角几何及具身/机器人/AR 应用相关；但若关注具体模型训练效果、评测协议或数据构建细节，需进一步阅读全文，摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Recent advances in interactive world models have made it possible to generate controllable, dynamic environments from action inputs. Yet current models struggle to maintain coherence beyond roughly one minute of rollout, a limitation rooted not in model capacity but in the scarcity of long-horizon training data. Existing gameplay video datasets typically consist of clips under ten seconds, with captions that describe whole clips in coarse and undifferentiated text, which is insufficient for controllable long-horizon generation. We address this with GameVerse, a minute-scale gameplay video dataset purpose-built for long-horizon interactive world modeling. GameVerse contains 69.7K clips spanning 1,655 hours and 349.6 million frames across diverse first- and third-person gameplay, including 1,358 hours of continuous two-minute sequences, an order of magnitude longer than prior datasets. Clips pass through a unified pipeline of scene-consistent segmentation, quality filtering, camera pose estimation, and event-based caption annotation. Each clip is paired with a temporally stable camera trajectory that remains coherent across minutes, together with captions that separate static scene context from dynamic foreground events and align to event boundaries rather than fixed time windows. Comprehensive analysis shows that GameVerse surpasses existing public datasets in scale, diversity, and annotation quality. Experiments further demonstrate that training on GameVerse substantially extends the temporal horizon of interactive world models.

</details>

#### 2026-10-27 - RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty

**Authors:** Xinyi Chen, Yichen Zhang, Chenxing Jiang, Shaojie Shen
**Links:** [abs](https://arxiv.org/abs/2610.37111) - [pdf](https://arxiv.org/pdf/2610.37111)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty
- 作者：Xinyi Chen, Yichen Zhang, Chenxing Jiang, Shaojie Shen
- 出版日期：2026-10-27T12:08:37Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.37111 ；PDF https://arxiv.org/pdf/2610.37111

### 一句话总结
RAVEN 是一个面向四旋翼飞行器的统一主动 SLAM 框架，在定位不确定性下联合权衡探索未知区域与主动回环，并通过感知感知导航生成平滑执行轨迹。

### 研究问题
论文关注主动 SLAM 中的核心矛盾：一方面需要探索未知空间以扩大覆盖，另一方面需要利用已访问区域执行主动回环以维持定位精度。摘要指出，已有工作多面向地面机器人；空中机器人机动性强但传感器配置受限，面临更显著的定位漂移，因此需要专门的主动 SLAM 规划。此外，如何形成一种能根据任务特定优先级自适应调整性能的统一策略，仍是开放问题。

### 核心思路/方法
摘要给出的方法流程包括：
1. 识别前沿（frontiers）与主动回环候选；
2. 基于这些候选生成全局巡回候选（global tour candidates）；
3. 使用一个“效用向量”分别量化探索效率与定位精度，并依据取值在 [0,1] 的优先级参数选择最终巡回；
4. 由感知感知导航规划器基于在线 Fisher 信息场生成平滑执行轨迹，以最小化视觉状态估计误差。

整体上，RAVEN 将“探索—回环”的权衡显式参数化，并把定位不确定性纳入规划与轨迹生成过程。

### 主要贡献
摘要明确提到的贡献包括：
- 提出面向四旋翼的统一主动 SLAM 框架 RAVEN，系统性地考虑定位不确定性；
- 通过效用向量分别量化探索效率与定位精度，并支持由优先级参数调节最终巡回选择；
- 使用在线 Fisher 信息场进行感知感知导航规划，生成平滑执行轨迹以降低视觉状态估计误差；
- 基准评估显示其优于现有主动 SLAM 方法，并能在不同优先级下产生一系列性能表现；
- 使用定制立体惯性四旋翼完成全机载现场实验，验证在挑战性环境中的实际适用性；
- 摘要称将开源源代码。

### 局限性
摘要未提供足够信息说明以下方面：具体实验环境与规模、基准测试的完整设置与对比指标细节、失败案例或边界条件、计算资源与实时性开销、优先级参数选择的敏感性分析，以及现场实验的定量结果。因此无法基于摘要对这些局限作出可靠判断。

### 阅读优先级
中。理由：该工作面向空中机器人主动 SLAM，明确处理定位不确定性与探索—回环权衡，并声称有基准比较与全机载现场实验；若关注空中机器人自主探索、主动 SLAM 或感知感知规划，具有较高相关性。但摘要未提供实验细节与定量结果，需阅读全文后才能判断其方法新颖性与验证充分性。

</details>

<details>
<summary>Abstract</summary>

Active simultaneous localization and mapping (SLAM) addresses the problem of planning robot motion to build complete and accurate maps of unknown environments through efficient exploration while maintaining high localization accuracy. This raises a dilemma between exploring unknown spaces to expand coverage and exploiting visited regions to perform active loop closures. Despite numerous prior works on ground robots, aerial robots with high agility and constrained sensor suites face more significant localization drift and thereby demand dedicated active SLAM planning. Moreover, a unified strategy that adapts performance based on task-specific priorities remains an open question. In this article, we introduce RAVEN, a unified active SLAM framework for Rapid Autonomous Visual ExploratioN using quadrotors, which systematically accounts for localization uncertainty. The framework starts with identifying frontiers and active loop closure candidates, from which global tour candidates are generated. These candidates are evaluated using a utility vector that separately quantifies exploration efficiency and localization accuracy, and the final tour is selected according to a prioritization parameter ranging from $[0,1]$. Finally, a perception-aware navigation planner generates smooth execution trajectories that minimize visual state estimation error based on the online Fisher information field that provides visual localization information in real-time. Benchmark evaluations demonstrate that RAVEN outperforms state-of-the-art active SLAM methods, highlighting its advantages in producing a spectrum of performance across prioritizations. Fully onboard field experiments with a customized stereo-inertial quadrotor further validate its practical applicability in challenging environments. The source code will be released to benefit the community.

</details>

#### 2026-10-27 - Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction

**Authors:** Haoyu Yao, Chenguo Lin, Ruize Du, Yadong Mu
**Links:** [abs](https://arxiv.org/abs/2610.37046) - [pdf](https://arxiv.org/pdf/2610.37046)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction
- 作者：Haoyu Yao, Chenguo Lin, Ruize Du, Yadong Mu
- 出版日期：2026-10-27T11:15:41Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.37046) / [PDF](https://arxiv.org/pdf/2610.37046)

### 一句话总结
SceneEvolve 将 3D 场景表示为可执行代码，通过围绕小型开源智能体演化“harness”（执行框架/脚手架），在固定模型参数、动作语义与执行后端的前提下，提升从真实图像重建可编辑、组合式 3D 场景的能力。

### 研究问题
论文关注从单张真实图像重建可编辑、组合式 3D 场景的问题。该任务需要同时推理几何、物体结构与空间关系。摘要指出，现有设定下需要探索如何利用较小开源模型完成此类重建，并在不更新参数的情况下获得可复用的重建流程。

### 核心思路/方法
SceneEvolve 的核心是将 3D 场景表示为可执行代码，并围绕小型开源智能体演化 harness。方法包含两个组成部分：
- SceneAct：组合式语义动作接口，基于参数化基元、分层组合与语义空间关系构建。
- SceneHarness-RSI：利用更强的教师智能体，基于开发集重建反馈迭代演化 harness。

在整个 harness 演化过程中，模型参数、动作语义和执行后端保持不变。演化得到的 harness 形成可复用的重建过程，使小型开源模型无需参数更新或教师辅助即可重建未见场景。

### 主要贡献
- 提出 SceneEvolve 框架，将 3D 场景表示为可执行代码，并通过 harness 演化改进组合式 3D 重建。
- 提出 SceneAct 组合式语义动作接口，结合参数化基元、分层组合与语义空间关系。
- 提出 SceneHarness-RSI，利用教师智能体与开发集重建反馈迭代演化 harness，且保持模型参数、动作语义和执行后端固定。
- 摘要报告：在两个域内数据集和一个域外数据集上，使用较紧凑的 Qwen3.8-27B 模型时，四项重建指标均提升，平均推理时间相对基模型减少 47.0%。
- 摘要报告：尽管使用显著更小的模型，SceneEvolve 的重建质量比大型专有模型 GPT-5.6-Sol 高 32.3%，同时平均等效部署成本降低 59.8%。
- 摘要报告：使用 Qwen3.8-27B 演化得到的 harness 可泛化到 Kimi-K3，并取得与 GPT-6-Astra 可比的重建性能。

### 局限性
摘要未提供足够信息说明方法局限性、失败场景、对教师智能体或开发集质量的依赖程度，以及具体实验设置与指标定义。摘要未提供足够信息说明 harness 演化过程的计算开销、可复现性细节与跨更多模型/数据集的泛化边界。

### 阅读优先级
中。理由：论文主题属于组合式 3D 重建与智能体框架交叉方向，摘要给出了较明确的性能与效率对比，具有一定参考价值；但当前仅有摘要与元数据，缺少实验细节、局限讨论与方法实现信息，适合作为后续按兴趣深入阅读的候选。

</details>

<details>
<summary>Abstract</summary>

Reconstructing editable and compositional 3D scenes from a real image requires jointly reasoning about geometry, object structure, and spatial relationships. We introduce SceneEvolve, a framework that represents 3D scenes as executable code and improves reconstruction by evolving the harness around a small open-source agent. SceneEvolve combines SceneAct, a compositional semantic action interface built on parameterized primitives, hierarchical composition, and semantic spatial relations, with SceneHarness-RSI, which leverages a stronger teacher agent to iteratively evolve the harness using feedback from development-set reconstructions. Throughout harness evolution, the model parameters, action semantics, and execution backend remain fixed. The resulting harness provides a reusable reconstruction procedure that enables the small open-source model to reconstruct unseen scenes without parameter updates or teacher assistance. Across two in-domain datasets and one out-of-domain dataset, SceneEvolve with the comparatively compact Qwen3.8-27B model improves all four evaluated reconstruction metrics while reducing mean inference time by 47.0% relative to the base model. More notably, despite relying on a substantially smaller model, SceneEvolve achieves 32.3% higher reconstruction quality than the large proprietary GPT-5.6-Sol model, while reducing mean equivalent deployment cost by 59.8%. Furthermore, the harness evolved using Qwen3.8-27B also generalizes to Kimi-K3, achieving comparable reconstruction performance to GPT-6-Astra. The project page is https://haoyu-agent.github.io/SceneEvolve.

</details>

#### 2026-10-27 - LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM

**Authors:** Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel
**Links:** [abs](https://arxiv.org/abs/2610.36853) - [pdf](https://arxiv.org/pdf/2610.36853)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** camera prediction, SLAM, depth estimation, Gaussian Splatting, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM
- 作者：Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel
- 出版日期：2026-10-27T08:51:00Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.36853 ；PDF https://arxiv.org/pdf/2610.36853

### 一句话总结
LingGS 将前馈几何预测与相机跟踪解耦：由冻结的流式 3D 基础模型提供深度，再由显式几何求解器估计相机运动，并配合流式高斯建图，以提升单目 RGB 高斯泼溅 SLAM 在有限优化预算下的重建质量与跟踪效率。

### 研究问题
论文面向单目 RGB 高斯泼溅 SLAM，在有限优化预算下同时实现高质量重建与响应式相机跟踪仍然困难。摘要指出，该工作关注如何结合学习到的几何先验与显式几何相机跟踪，并比较其相对于学习式相机预测在跟踪精度上的表现。

### 核心思路/方法
- 使用冻结的流式 3D 基础模型作为虚拟 RGB-D 传感器，从单目视频提供深度估计。
- 使用显式几何求解器通过特征重投影估计相机运动。
- 使用流式高斯映射器将得到的观测整合为稠密场景表示。
- 摘要还指出，几何跟踪在代表性流式几何骨干上可提升相机位姿精度，说明方法具有更广的适用性。

### 主要贡献
- 提出一种在线系统，将学习到的几何先验与显式几何相机跟踪结合，用于单目 RGB 高斯泼溅 SLAM。
- 将前馈几何预测与相机跟踪解耦，并表明显式几何相机跟踪在跟踪精度上可显著优于学习式相机预测。
- 展示几何跟踪可跨代表性流式几何骨干提升相机位姿精度。
- 在室内和户外数据集上的大量实验表明，该方法相较现有方法显著提升重建质量；在单张 RTX 4090 上约达到 7 FPS，吞吐量为所评估的先前 SLAM 系统的 2–3 倍。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、对冻结 3D 基础模型深度质量的依赖程度、极端光照或快速运动下的表现、内存占用、长期漂移等细节。

### 阅读优先级
高。理由：论文直接针对单目 RGB 高斯泼溅 SLAM 中重建质量、跟踪精度与效率的权衡，提出解耦前馈几何预测与显式几何跟踪的在线方案，并报告了明确的精度、重建质量和吞吐量收益；对 3D 重建、多视图几何与神经场景表示相关方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Achieving high-quality reconstruction and responsive camera tracking remains challenging for monocular RGB Gaussian splatting SLAM under a limited optimization budget. We present an online system that addresses this challenge by combining learned geometric priors with explicit geometric camera tracking, which can substantially outperform learned camera prediction in terms of tracking accuracy. A frozen streaming 3D foundation model serves as a virtual RGB-D sensor, providing depth estimation from monocular video. An explicit geometric solver then estimates camera motion through feature reprojection, and a streaming Gaussian mapper integrates the resulting observations into a dense scene representation. We further show that geometric tracking improves camera pose accuracy across representative streaming geometry backbones, demonstrating the broader applicability of our approach. Extensive experiments on indoor and outdoor datasets show that our method significantly improves reconstruction quality over existing approaches, achieving about 7 FPS on a single RTX 4090 and delivering 2-3 times the throughput of the evaluated prior SLAM systems.

</details>

#### 2026-10-27 - Polarity--Time Interaction and Multi-Level Reliability for Event-Based Spacecraft Pose Estimation

**Authors:** Yonglong Zhang, Zongwu Xie, Yang Liu
**Links:** [abs](https://arxiv.org/abs/2610.36625) - [pdf](https://arxiv.org/pdf/2610.36625)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Polarity--Time Interaction and Multi-Level Reliability for Event-Based Spacecraft Pose Estimation
- 作者：Yonglong Zhang, Zongwu Xie, Yang Liu
- 出版日期：2026-10-27T04:29:19Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.36625) / [PDF](https://arxiv.org/pdf/2610.36625)

### 一句话总结
论文提出一种可靠性感知框架，将极性—时间定位、几何恢复、事件—CAD 细化与轨迹优化串联起来，用于基于事件的航天器位姿估计。

### 研究问题
稀疏事件响应会导致关键点误差不均匀，而这些误差对航天器位姿的影响取决于对应几何关系以及连续观测的可靠性。论文关注如何在这种条件下进行可靠的事件相机航天器位姿估计。

### 核心思路/方法
- 构建可靠性感知框架，连接极性—时间定位、几何恢复、事件—CAD 细化与轨迹优化。
- 采用三分支表示，结合正事件、负事件和近期事件时间信息，并通过跨分支注意力与门控，随后进行时空聚合。
- 使用有序语义点头估计相对对应精度，用于几何约束下的位姿恢复。
- 利用事件边缘与 CAD 投影一致性，在关键点几何保护机制下指导局部位姿细化。
- 在序列层面构造十维描述符，结合热图形状、重投影一致性和几何条件，设置时间对齐的观测尺度。

### 主要贡献
- 提出面向事件航天器位姿估计的多级可靠性框架。
- 在官方 SPADES 挑战测试集上，完整系统取得 0.0474 的组合位姿分数，摘要称约比 PASAN+IRIS 低 5.4%。
- 消融结果显示：基础定位配合均匀 PnP 的分数为 0.0772，完整级联降至 0.0514；在相同单帧观测下，质量加权将常数权重优化的 0.0549 降至 0.0514。
- 摘要强调质量加权在相同单帧观测下带来分数下降。

### 局限性
摘要未提供足够信息说明计算开销、实时性、不同事件噪声条件下的鲁棒性、数据集规模与训练细节，也未给出与 PASAN+IRIS 比较的完整实验设置和统计显著性。

### 阅读优先级
中。理由：论文针对事件相机航天器位姿估计中的稀疏关键点可靠性问题，给出较完整的级联框架和官方挑战集结果；但摘要未提供充分的实验细节与泛化验证信息，适合作为相关方向的方法参考而非立即精读优先。

</details>

<details>
<summary>Abstract</summary>

Sparse event responses produce uneven keypoint errors whose effects on spacecraft pose depend on correspondence geometry and the reliability of successive observations. We present a reliability-aware framework connecting polarity--time localization, geometric recovery, event--CAD refinement, and trajectory optimization. A three-branch representation combines positive events, negative events, and recent-event timing through cross-branch attention and gating, followed by spatiotemporal aggregation. An ordered semantic-point head estimates relative correspondence precision for geometrically constrained pose recovery. Event-edge and CAD-projection agreement then guide local pose refinement under keypoint-geometry safeguards. At the sequence level, a ten-dimensional descriptor combines heatmap shape, reprojection consistency, and geometric conditioning to set time-aligned observation scales. On the official SPADES challenge test set, the complete system achieves a combined pose score of 0.0474, approximately 5.4\% below PASAN+IRIS. Validation ablations reduce the score from 0.0772 for base localization with uniform PnP to 0.0514 for the complete cascade; on identical single-frame observations, quality weighting reduces the score from 0.0549 with constant-weight optimization to 0.0514.

</details>

#### 2026-10-27 - Camera-to-Quadruped Robot Pose Estimation from Sequential Images

**Authors:** Seobin Hwang, Ji-Seong Beom, Yeong-Jun Cho
**Links:** [abs](https://arxiv.org/abs/2610.36599) - [pdf](https://arxiv.org/pdf/2610.36599)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Camera-to-Quadruped Robot Pose Estimation from Sequential Images
- 作者：Seobin Hwang, Ji-Seong Beom, Yeong-Jun Cho
- 出版日期：2026-10-27T03:59:43Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.36599) / [PDF](https://arxiv.org/pdf/2610.36599)

### 一句话总结
该论文提出 QuadPose，从单目视频序列估计四足机器人全身 18 自由度姿态（6-DoF 基座位姿 + 12-DoF 关节角度），并发布首个相机到四足机器人姿态基准 QuadSyn。

### 研究问题
四足机器人常用于灾害响应、设施巡检等危险环境，需要外部相机监控以保障安全运行。但四足机器人是多关节系统，腿部关节随时间变化、腿部对称且自遮挡频繁，导致关键点对应关系不明确；同时缺少公开基准，难以进行定量比较。论文即针对上述姿态估计与评测基准缺失问题展开。

### 核心思路/方法
论文提出 QuadPose，从单目视频序列中估计四足机器人全身 18-DoF 姿态，包括 6-DoF 基座位姿和 12-DoF 关节角度。为支持定量比较，论文同时构建并引入 QuadSyn，这是首个相机到四足机器人姿态基准。摘要未提供 QuadPose 的具体网络结构、训练策略或损失函数等实现细节。

### 主要贡献
- 提出 QuadPose，用于从单目视频序列估计四足机器人全身 18-DoF 姿态（6-DoF 基座位姿 + 12-DoF 关节角度）。
- 引入 QuadSyn，定位为首个相机到四足机器人机器人姿态基准，用于缓解该任务缺少公开基准的问题。
- 在 QuadSyn 上报告了定量结果：PCK@2.5px 为 92.18%，PCK-AUC 为 95.54%，ADD@20cm 为 85.94%，ADD-AUC 为 66.98%，平均关节角度误差为 3.65 度，运行速度约 33 FPS。

### 局限性
- 摘要未提供足够信息说明 QuadPose 在真实场景、跨域数据或不同于 QuadSyn 的数据上的泛化表现。
- 摘要未提供足够信息说明 QuadSyn 的采集方式、规模、标注方式与数据多样性。
- 摘要未提供足够信息说明方法对严重自遮挡、腿部对称歧义等挑战的具体处理机制与消融结果。
- 摘要未提供足够信息说明与现有其他方法的定量对比细节。
- 摘要未提供足够信息说明 33 FPS 所对应的硬件平台与运行条件。

### 阅读优先级
中。理由：该工作同时提出方法与首个相关基准，并给出较完整的定量指标，对四足机器人外部监控与姿态估计方向具有参考价值；但摘要未展开方法细节与基准构建细节，是否优先精读取决于读者对四足机器人姿态估计或多关节目标姿态估计的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Quadruped robots are increasingly deployed in hazardous environments such as disaster response and facility inspection, where external-camera monitoring is essential for safe operation. This setting is challenging because quadrupeds are articulated systems with time-varying leg joints, leg symmetry, and frequent self-occlusions, which make keypoint correspondence ambiguous. Moreover, no public benchmark exists, making quantitative comparison difficult. To address these challenges, we propose QuadPose, which estimates the full-body 18-DoF pose (6-DoF base pose + 12-DoF joint angles) from monocular video sequences, and introduce QuadSyn, the first camera-to-quadruped robot pose benchmark. On QuadSyn, QuadPose achieves 92.18% PCK@2.5px, 95.54% PCK-AUC, 85.94% ADD@20cm, 66.98% ADD-AUC, and 3.65 degree mean joint-angle error at approximately 33 FPS.

</details>

#### 2026-10-26 - Any3R: Feedforward 3D Reconstruction from Any Camera Type

**Authors:** Jingong Chen, Qingwen Zhang, Youming Deng, Chulwoo Pack, Olaf Wysocki, Boris Jutzi, Kwanghee Won, Kyle Gao
**Links:** [abs](https://arxiv.org/abs/2610.36150) - [pdf](https://arxiv.org/pdf/2610.36150)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Any3R: Feedforward 3D Reconstruction from Any Camera Type
- 作者：Jingong Chen, Qingwen Zhang, Youming Deng, Chulwoo Pack, Olaf Wysocki, Boris Jutzi, Kwanghee Won, Kyle Gao
- 出版日期：2026-10-26T18:53:14Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.36150) · [PDF](https://arxiv.org/pdf/2610.36150) · [项目页](https://jingong-chen.github.io/Any3R/)

### 一句话总结
Any3R 是一个前馈三维重建模型，通过用稠密光线场对位置编码和训练损失进行条件化，使其无需按镜头类型重新训练即可处理任意中心相机。

### 研究问题
现有几何基础模型虽能以前馈网络从多张图像恢复相机位姿和稠密几何，但其假设输入为针孔图像；这一假设深入骨干网络内部——位置编码和训练损失都将图像位置绑定到空间方向，且二者依赖镜头。因此，模型难以直接适用于非针孔或异构相机图像。

### 核心思路/方法
论文提出用稠密光线场（每个像素对应的单位方向）同时对位置编码和训练损失进行条件化，该表示可描述任意中心相机，而无需镜头类型、畸变系数或视场角限制。
- **角度坐标**：为旋转编码提供每个 patch 的实测光线角度，并按视图评估。
- **立体角加权**：用每个像素在球面上覆盖的面积缩放点损失。
这样编码与监督均不依赖镜头，模型可接受任意中心相机，并对同一场景混合多种相机类型具有鲁棒性，且无需针对每种镜头重新训练。

### 主要贡献
- 提出 Any3R，一个可接受任意中心相机的前馈三维重建模型。
- 将位置编码与训练损失从针孔假设中解耦，改为基于稠密光线场条件化，并引入角度坐标旋转编码与立体角加权点损失。
- 支持同一场景混合多种相机类型且无需按镜头重训练。
- 在三个数据集、十三种中心相机的基准上，各方法均使用自身预测的相机位姿进行重建时，Any3R 被描述为最 consistently 准确的方法。
- 面向异构众包与档案图像集合的可扩展三维重建。

### 局限性
- 具体网络架构、训练数据规模与训练细节：摘要未提供足够信息。
- 基准数据集的构成、评价指标定义及定量结果：摘要未提供足够信息。
- 对非中心相机（如非中心投影或特殊成像模型）的适用性：摘要未提供足够信息。
- 计算开销、推理速度与内存需求：摘要未提供足够信息。
- 失败案例与鲁棒性边界：摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接针对几何基础模型中“针孔假设”这一基础性限制，方法思路清晰且具有通用性；若关注多视图三维重建、异构相机或前馈几何模型，摘要显示其问题定义与贡献具有较高相关性。但需注意，摘要未给出定量实验细节，深入评估需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Geometry foundation models recover camera poses and dense geometry from a set of images with a feed-forward network, but they expect pinhole images. That assumption is inside the backbone too: the positional encoding and the training loss both bind an image position to a direction in space, and both depend on the lens. We condition both on the dense ray field, the unit direction through every pixel, which describes any central camera without a lens type, distortion coefficients or a bound on field of view. Angular coordinates give the rotary encoding the measured ray angle of each patch, evaluated per view, and solid-angle weighting scales the point loss by the area each pixel covers on the sphere, so neither the encoding nor the supervision depends on the lens. Any3R is therefore a feed-forward model that takes any central camera, and is robust to mixing many camera types per scene, with no retraining per lens. On a benchmark of thirteen central cameras across three datasets, where every method reconstructs with its own predicted camera poses, it is the most consistently accurate method. Any3R enables scalable 3D reconstruction from heterogeneous crowdsourced and archival imagery collections sourced across diverse camera types. Project page: https://jingong-chen.github.io/Any3R/

</details>

#### 2026-10-26 - Metric Scale for Insta360 Structure-from-Motion from the Camera's Embedded IMU

**Authors:** Davide Cuttini, Diego Di Tommaso, Alessio Antoniacomi, Luca Simonetti
**Links:** [abs](https://arxiv.org/abs/2610.35554) - [pdf](https://arxiv.org/pdf/2610.35554)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, structure from motion, SfM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Metric Scale for Insta360 Structure-from-Motion from the Camera's Embedded IMU
- 作者：Davide Cuttini, Diego Di Tommaso, Alessio Antoniacomi, Luca Simonetti
- 出版日期：2026-10-26T14:57:37Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.35554) / [PDF](https://arxiv.org/pdf/2610.35554)

### 一句话总结
论文评估用 Insta360 X5/X6 内置 IMU（1 kHz）替代手机 ARKit/ARCore 位姿，为双鱼眼 SfM 恢复公制尺度，并在多组测量中与 LiDAR、标定板及手机尺度对比。

### 研究问题
消费级 360 度相机双鱼眼视频的 SfM 只能恢复到相似变换，缺少公制尺度。现有流程依赖同步采集的智能手机 ARKit/ARCore 位姿提供尺度。论文要回答：能否仅用相机内置 IMU 实现自包含的公制尺度恢复，以及其精度与手机尺度相比如何。

### 核心思路/方法
- 对 Insta360 X5/X6 内置 IMU 进行传感器表征：噪声密度、相机-IMU 同步、加速度计尺度因子、偏置稳定性。
- 从数据中估计相机-IMU 旋转与帧时间关系。
- 在整段测量的 SfM 位姿上做线性视觉-惯性对齐以恢复尺度。
- 指出标准做法（整段共享重力与加速度计偏置）平均高估尺度 3.4%；改为逐连续段独立估计再平均可消除该偏差。
- 补充窗口构建消融实验，并与单目公制深度网络比较。

### 主要贡献
- 提出并评估一种不依赖手机 AR 位姿、仅用相机内置 IMU 的 SfM 公制尺度恢复方案。
- 给出该 IMU 的表征结果与相机-IMU 旋转、帧时间估计方法。
- 发现并修正整段共享重力/偏置导致的尺度高估偏差。
- 在九组与 LiDAR 同机采集的测量中，惯性尺度平均绝对误差 0.81%，手机尺度为 1.94%；在打印基准标记上两者均在目标 1% 不确定度内一致。
- 在公开基准三十条参考轨迹（尺度 1/40、1、40）上，尺度恢复平均误差 -0.07%，标准差 1.28%。
- 在五十组仅以手机为参考的生产测量中，两种尺度标准差 2.3%，惯性尺度平均低 0.3%；差异与运行长度不相关、随手机锚点范围增大而增大，且无法归因于任一参考。

### 局限性
- 摘要未提供足够信息说明 IMU 表征的具体数值、实验环境条件与失败案例。
- 摘要未提供足够信息说明窗口构建消融与单目公制深度网络比较的具体结果。
- 摘要提到五十组生产测量中两种尺度差异“无法归因于任一参考”，但未给出最终尺度真值判定方法。
- 摘要未提供足够信息说明方法在非 Insta360 相机或其他 IMU 上的泛化性。

### 阅读优先级
中。理由：论文针对 360 相机 SfM 的公制尺度这一明确工程问题，给出了多组定量对比与偏差修正，对使用 Insta360 做三维重建的读者有直接参考价值；但主题较专门，且摘要未展开消融与深度网络对比细节，非该方向读者的普适性有限。

</details>

<details>
<summary>Abstract</summary>

Structure-from-motion (SfM) from the dual-fisheye video of a consumer 360-degree camera recovers geometry only up to a similarity transform; in the pipeline considered here, metric scale is obtained from smartphone ARKit or ARCore poses captured alongside the camera. This paper evaluates a self-contained alternative: the IMU embedded in the Insta360 X5 and X6, recorded at 1 kHz. The sensor is characterised (noise density, camera-IMU synchronisation, accelerometer scale factor, bias stability), the camera-IMU rotation and frame timing are estimated from the data, and the scale is recovered by a linear visual-inertial alignment over the SfM poses of a whole survey. The standard formulation, with gravity and accelerometer bias shared across the survey, overestimates the scale by 3.4% on average; estimating each contiguous segment independently and averaging removes the bias. On nine surveys with a co-mounted LiDAR scanner the inertial scale deviates from the LiDAR by 0.81% in mean absolute error, against 1.94% for the smartphone scale; on printed fiducial markers both agree within the 1% uncertainty of the target. On the reference trajectories of thirty sequences of a public benchmark, brought to scales of 1/40, 1 and 40, the estimator recovers the metric scale with a mean error of -0.07% and a standard deviation of 1.28%. On fifty production surveys where the smartphone is the only reference, the two scales agree to a standard deviation of 2.3%, the inertial scale being 0.3% lower on average; the difference is uncorrelated with run length, grows with the extent of the smartphone anchor, and cannot be attributed to either reference. An ablation over window construction and a comparison with monocular metric-depth networks complete the study.

</details>

#### 2026-10-26 - Generative Structure from Motion with Native 3D Diffusion

**Authors:** Haobin Duan, Binbin Huang, Mochu Xiang, Yiqun Zhao, Zibo Zhao, Yi Ma, Shenghua Gao
**Links:** [abs](https://arxiv.org/abs/2610.35522) - [pdf](https://arxiv.org/pdf/2610.35522)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Generative Structure from Motion with Native 3D Diffusion
- 作者：Haobin Duan, Binbin Huang, Mochu Xiang, Yiqun Zhao, Zibo Zhao, Yi Ma, Shenghua Gao
- 出版日期：2026-10-26T14:40:40Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.35522) | [PDF](https://arxiv.org/pdf/2610.35522)

### 一句话总结
GenSfM 将基于图像的 3D 重建与原生 3D 扩散模型结合，在共享自注意力下联合去噪形状潜变量与逐视图位姿潜变量，从少量未标定视图同时恢复物体 3D 结构与相机运动。

### 研究问题
论文关注从少量未标定视图恢复物体的 3D 结构与相机运动这一计算机视觉基础问题。摘要指出：经典 Structure-from-Motion 方法能恢复与输入图像一致的 3D 几何，但无法恢复未观测区域；原生生成方法能生成看似合理的 3D 物体，但与输入图像的相关性不一定忠实。简单地将重建与生成串联会导致误差在两个阶段间级联，难以得到同时符合数据分布与输入图像的 3D 物体。

### 核心思路/方法
摘要给出的方法要点如下：
- 提出 GenSfM，将基于图像的 3D 重建与原生 3D 扩散模型集成。
- 使用多模态扩散 Transformer，在共享自注意力机制下联合去噪形状潜变量与逐视图位姿潜变量，使生成几何以观测视图为条件，并利用物体级先验推断未观测区域。
- 采用紧凑的 3D 原生 UV-volume tokenization，使视图增加时联合序列仍保持较小规模。
- 使用位姿感知阶段，在恢复的相机位姿下采样逐体素图像特征，以细化几何与纹理。

### 主要贡献
- 提出 GenSfM，将图像 3D 重建与原生 3D 扩散模型结合，以联合去噪方式处理形状与位姿，而非简单串联重建与生成。
- 引入多模态扩散 Transformer 的共享自注意力联合去噪机制，使生成几何同时受观测视图约束并利用物体级先验。
- 提出紧凑的 3D 原生 UV-volume tokenization，控制多视图联合序列规模。
- 设计位姿感知细化阶段，在恢复位姿下采样逐体素图像特征以细化几何与纹理。
- 摘要报告在 Toys4k 与 GSO 上、使用 4 个未标定视图时，相较强原生 3D 生成基线，新视角 PSNR 提升 3.2–4.5 dB，中位 Chamfer 距离降低 2.8–3.8 倍；输入视图位姿恢复达到 96% 以上 Acc@5°，且无需外部位姿估计骨干、事后优化或已知内参。

### 局限性
摘要未提供足够信息。摘要未说明方法失败场景、计算开销、对视图数量或物体类别的敏感性、与重建类基线的完整对比，也未给出消融实验细节。

### 阅读优先级
中。理由：该论文面向少视图未标定条件下的 3D 重建与位姿恢复，试图统一重建与生成并避免两阶段误差级联，且摘要给出明确的定量提升与无需外部位姿骨干的特点；但摘要未提供方法细节、失败案例与完整实验设置，需阅读全文才能判断其适用边界与可复现性。

</details>

<details>
<summary>Abstract</summary>

Recovering an object's 3D structure and camera motion from a few uncalibrated views is a fundamental problem in computer vision. Classical structure from motion methods recover 3D geometry consistent with the input images but cannot recover unseen regions; native generation methods produce plausible 3D objects which are related but not necessarily faithful to the input images. Methods simply concatenating reconstruction and generation allow error to cascade across the two stages, instead of producing a 3D object consistent with both the distribution and the input. We propose GenSfM, which integrates image-based 3D reconstruction with a native 3D diffusion model. In particular, we use a multi-modal diffusion transformer to jointly denoise the shape latent and per-view pose latents under shared self-attention, grounding generated geometry in the observed views while using object-level priors to infer unobserved regions. A compact 3D-native UV-volume tokenization keeps the joint sequence small as views are added, and a pose-aware stage refines geometry and texture by sampling per-voxel image features at the recovered camera poses. On Toys4k and GSO, for $4$ uncalibrated views, GenSfM improves novel-view PSNR by $3.2$-$4.5$ dB and reduces median Chamfer distance by $2.8$-$3.8\times$ over a strong native-3D generation baseline, while recovering input-view poses over $96\%$ Acc@$5^\circ$ without any external pose-estimation backbone, post-hoc optimization, or known intrinsics. Project page: https://dotb1ue.github.io/GenSfm/.

</details>

#### 2026-10-26 - Learning Scene Coordinate Reconstruction from Unposed Images via Pose Graph Optimization

**Authors:** Tze Ho Elden Tse, Jizong Peng, Angela Yao
**Links:** [abs](https://arxiv.org/abs/2610.35501) - [pdf](https://arxiv.org/pdf/2610.35501)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** geometric reasoning, structure from motion, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Scene Coordinate Reconstruction from Unposed Images via Pose Graph Optimization
- 作者：Tze Ho Elden Tse, Jizong Peng, Angela Yao
- 出版日期：2026-10-26T14:29:13Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.35501 ；PDF https://arxiv.org/pdf/2610.35501

### 一句话总结
该论文在无需真值监督的 ACE-Zero 类学习式 structure-from-motion 流程中引入位姿图优化，并利用极线与光流一致性估计置信度，以缓解相机位姿漂移和错误精化问题。

### 研究问题
论文关注的是：基于学习的 structure-from-motion 方法（如 ACE-Zero）虽然能够从无序图像集合中估计相机位姿和场景坐标，且不依赖真值监督，但 ACE-Zero 缺少全局和多视图一致性约束，因此在复杂或歧义场景中容易出现位姿漂移与错位。作者希望在不改变学习式推理主体的前提下，增强位姿估计的鲁棒性和准确性。

### 核心思路/方法
论文提出一个混合框架，将位姿图优化（PGO）集成到 ACE-Zero 中，用于精化相机位姿并抑制错误的精化结果。具体做法包括：
1. 直接从 ACE-Zero 的输出构建位姿图，通过预测的场景坐标提取相对位姿约束；
2. 引入不确定性感知的优化策略，利用几何先验估计置信度分数，包括跨视图的极线一致性和光流一致性；
3. 通过上述全局几何推理对学习式推理进行补充，以提升 structure-from-motion 中的位姿估计表现。

### 主要贡献
- 提出将位姿图优化与 ACE-Zero 结合的混合框架，用于从无序、无位姿图像中精化相机位姿。
- 设计从 ACE-Zero 预测场景坐标中提取相对位姿约束并构建位姿图的方式。
- 引入基于几何先验（极线一致性与光流一致性）的不确定性感知优化策略，以抑制不可靠的精化。
- 论证全局几何推理可以有效补充学习式 structure-from-motion 推理。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集、评价指标、定量实验结果、计算开销、实时性分析，也未说明方法在何种场景或失败模式下的具体边界。

### 阅读优先级
中。理由：该论文针对学习式 structure-from-motion 中位姿漂移和多视图一致性问题提出明确的混合优化思路，问题定位清晰，方法组合具有参考价值；但摘要未提供定量结果和实验细节，是否显著优于现有方法尚无法从给定信息判断。若关注无位姿图像的三维重建、位姿图优化与学习式 SfM 结合，建议优先阅读；若仅需结论性性能对比，则需进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

Learning-based structure-from-motion methods such as ACE-Zero have demonstrated strong performance in estimating cameraposes and scene coordinates from unordered image collections without requiring ground truth supervision. However, the lack of global and multi-view consistency constraints in ACE-Zero can lead to pose drift and misalignment, particularly in complex or ambiguous scenes. In this work, we propose a hybrid framework that integrates pose graph optimization (PGO) into ACE-Zero to refine camera poses and suppress incorrect refinements. We construct pose graphs directly from ACE-Zero outputs by extracting relative pose constraints from predicted scene coordinates. Furthermore, we introduce an uncertainty-aware optimization strategy by estimating confidence scores using geometric priors, including epipolar and optical flow consistencies across views. Our approach improves the robustness and accuracy of pose estimation, demonstrating that global geometric reasoning can effectively complement learning-based inference in structure-from-motion.

</details>

#### 2026-10-26 - SG-Splat: Stable Geometry Learning under Pose Uncertainty for Pose-Free 3D Gaussian Splatting

**Authors:** Xiaohan Lu, Jiaqi Zhang, Weijia Jiang, Siwei Ma
**Links:** [abs](https://arxiv.org/abs/2610.35361) - [pdf](https://arxiv.org/pdf/2610.35361)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, pose estimation, bundle adjustment, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SG-Splat: Stable Geometry Learning under Pose Uncertainty for Pose-Free 3D Gaussian Splatting
- 作者：Xiaohan Lu, Jiaqi Zhang, Weijia Jiang, Siwei Ma
- 出版日期：2026-10-26T12:50:21Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Neural Scene Representations & Rendering（次分类）
- 链接：[摘要](https://arxiv.org/abs/2610.35361) ｜ [PDF](https://arxiv.org/pdf/2610.35361)

### 一句话总结
SG-Splat 是一个无位姿前馈 3D Gaussian Splatting 框架，通过解耦几何估计与高斯属性预测、引入由粗到细的位姿与几何修正流程，以及混合真实与预测位姿的双路径训练策略，提升对残余位姿误差的鲁棒性并稳定高斯基元学习。

### 研究问题
现有无位姿前馈 3DGS 方法直接从无位姿输入图像重建高斯表示，但仍对残余位姿误差敏感：位姿误差会扰动规范空间中的高斯变换，从而给几何与属性学习引入噪声监督。论文旨在解决这一位姿不确定性下的几何学习不稳定问题。

### 核心思路/方法
- 将几何估计与高斯属性预测解耦为两个专用分支，以减少位姿敏感的几何误差与高斯属性之间的误差耦合。
- 引入由粗到细的修正流程：
  - Flow-Guided Pose Refinement（FGPR）：利用基于光流的相关特征与可微 bundle adjustment 精化相机位姿。
  - Residual-Guided Geometry Correction（RGC）：利用 FGPR 得到的深度残差修正初始点图，从而获得更可靠的高斯中心。
- 训练稳定化：采用双路径策略，混合真实位姿与预测位姿进行规范变换，为高斯属性提供干净监督，同时提升几何对残余位姿误差的鲁棒性。

### 主要贡献
- 提出 SG-Splat，一个面向位姿不确定性的无位姿前馈 3DGS 框架，提升对残余位姿误差的鲁棒性并稳定高斯基元学习。
- 设计几何估计与高斯属性预测的双分支解耦结构，降低误差耦合。
- 提出 FGPR 与 RGC 组成的由粗到细修正流程，在高斯属性重建前改善几何对齐。
- 引入混合真实位姿与预测位姿的双路径训练策略，为高斯属性提供干净监督并增强几何鲁棒性。
- 摘要称在 DL3DV 与 RealEstate10K 上于新视角合成与位姿估计两项任务均达到 state-of-the-art 性能。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、计算开销、对真实位姿监督的依赖程度、分支解耦的具体代价，以及在不同位姿噪声水平下的定量退化分析等细节。

### 阅读优先级
高。理由：该论文直接针对无位姿前馈 3DGS 中位姿误差传播导致几何学习不稳定的关键问题，方法上同时涉及解耦架构、可微位姿精化与训练策略，且摘要声称在新视角合成与位姿估计上均达到 state-of-the-art；对 3D 重建、多视角几何与神经渲染交叉方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become a promising representation for real-time novel view synthesis and 3D scene reconstruction. For practical deployment, recent studies have explored pose-free feed-forward 3DGS, which reconstructs Gaussian representations directly from unposed input images. However, these methods remain sensitive to residual pose errors, which perturb canonical-space Gaussian transformation, introducing noisy supervision for geometry and attribute learning. To address this problem, we present SG-Splat, a pose-free feed-forward 3DGS framework that improves robustness to pose uncertainty and stabilizes the learning of Gaussian primitives. SG-Splat decouples geometry estimation and Gaussian attribute prediction into two dedicated branches, reducing error coupling between pose-sensitive geometry and Gaussian attributes. We further introduce a coarse-to-fine refinement pipeline, consisting of Flow-Guided Pose Refinement (FGPR) and Residual-Guided Geometry Correction (RGC), to improve geometric alignment before Gaussian attribute reconstruction. Specifically, FGPR refines camera poses with flow-based correlation features and differentiable bundle adjustment. RGC then corrects initial point maps using depth residuals derived from FGPR, producing more reliable Gaussian centers. To stabilize training, we introduce a dual-path strategy that mixes ground-truth and predicted poses for canonical transformation. It provides clean supervision for Gaussian attributes while improving geometry robustness to residual pose errors. Extensive experiments on DL3DV and RealEstate10K show that SG-Splat achieves state-of-the-art performance in both novel view synthesis and pose estimation.

</details>

#### 2026-10-26 - CVTSplat: Multi-view Reconstruction Using an Adaptive Centroidal Voronoi Tessellation

**Authors:** Briac Toussaint, Diego Thomas, Jean-Sébastien Franco, Edmond Boyer, Christian Theobalt
**Links:** [abs](https://arxiv.org/abs/2610.35347) - [pdf](https://arxiv.org/pdf/2610.35347)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CVTSplat: Multi-view Reconstruction Using an Adaptive Centroidal Voronoi Tessellation
- 作者：Briac Toussaint, Diego Thomas, Jean-Sébastien Franco, Edmond Boyer, Christian Theobalt
- 出版日期：2026-10-26T12:39:58Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.35347) | [PDF](https://arxiv.org/pdf/2610.35347)

### 一句话总结
CVTSplat 提出使用自适应质心 Voronoi 剖分（CVT），在多视图重建中兼顾自适应空间划分与形状较规则的单元，以提高优化过程中的剖分与渲染效率。

### 研究问题
摘要指出，Voronoi 剖分已被用于从多视图图像进行形状与外观重建的自适应空间划分离散化；但常规 Voronoi 产生的不规则单元会使优化过程中反复重建剖分的代价较高。论文关注的问题是如何在保持自适应性的同时，使单元更规则、便于高效计算与重建。

### 核心思路/方法
论文探索自适应质心 Voronoi 剖分（CVT）：在标准 CVT 基础上引入非均匀单元尺寸，同时保留规则、形状良好的单元。CVTSplat 中，单元尺寸由不断演化的 signed distance field 调制，使站点（sites）集中在零水平集附近，同时保持单元接近质心化。由于单元具有规则性，作者对整个流程进行专门化，包括用于最近邻查询与近似 Voronoi 构建的 GPU 算法，以及面向小型、近似各向同性单元的 rasterizer。摘要称，在这一情形下其 Voronoi 构建比通用替代方案快 5 至 10 倍。

### 主要贡献
- 提出 CVTSplat，将自适应 CVT 用于多视图重建，以非均匀单元尺寸适配 signed distance field，同时保持单元接近质心化与规则形状。
- 针对该规则单元特性专门化流程，包括 GPU 最近邻查询、近似 Voronoi 构建以及面向小型近各向同性单元的 rasterizer。
- 摘要报告其 Voronoi 构建在此情形下比通用方案快 5 至 10 倍。
- 在 DTU 与 BlendedMVS 上，摘要称其几何精度可与最佳 Gaussian-splatting 表面方法竞争，且单 GPU 训练约 2.5 分钟。

### 局限性
摘要未提供足够信息。摘要未说明方法在复杂拓扑、大尺度场景、内存开销、对初始化或超参数的敏感性、与其他方法训练时间的完整对比，也未给出失败案例或定量误差细节。

### 阅读优先级
中。理由：该工作聚焦多视图重建中的自适应空间划分与效率问题，摘要给出了明确的加速与训练时间主张，并与 Gaussian-splatting 表面方法进行精度对比；但摘要未提供足够实验细节与局限性信息，是否优先精读取决于读者对 Voronoi 离散化、GPU 重建流程或快速多视图表面重建的关注程度。

</details>

<details>
<summary>Abstract</summary>

Voronoi tessellations have recently emerged as an adaptive, space-partitioning discretization for shape and appearance reconstruction from multi-view images. However, the irregular cells they produce make the repeated reconstruction of the tessellation during optimization costly. We therefore explore adaptive centroidal Voronoi tessellations (CVTs), which extend standard CVTs with non-uniform cell sizes while preserving the regular, well-shaped cells that make them efficient to compute. In CVTSplat, cell size is modulated by the evolving signed distance field, concentrating sites near the zero level set while keeping cells nearly centroidal. This regularity lets us specialize the whole pipeline, with GPU algorithms for nearest-neighbor queries and approximate Voronoi construction, and a rasterizer tailored to small, nearly isotropic cells. Our Voronoi construction is 5 to 10 times faster than general-purpose alternatives in this regime. On DTU and BlendedMVS, CVTSplat reaches geometric accuracy competitive with the best Gaussian-splatting surface methods while training in about 2.5 minutes on a single GPU.

</details>

#### 2026-10-26 - Zero-Shot Monocular Depth Estimation for Visual Perception in Lower-Limb Prostheses

**Authors:** Ishi Vijayvergiya, Marc Hölle, Youssef Dawoud, Amir El-Ghoussani, Michele De Vita, Rohan Asthana, Philipp Beckerle, Vasileios Belagiannis
**Links:** [abs](https://arxiv.org/abs/2610.35018) - [pdf](https://arxiv.org/pdf/2610.35018)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Zero-Shot Monocular Depth Estimation for Visual Perception in Lower-Limb Prostheses
- 作者：Ishi Vijayvergiya, Marc Hölle, Youssef Dawoud, Amir El-Ghoussani, Michele De Vita, Rohan Asthana, Philipp Beckerle, Vasileios Belagiannis
- 出版日期：2026-10-26T08:30:31Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.35018) / [PDF](https://arxiv.org/pdf/2610.35018)

### 一句话总结
论文面向下肢假肢的视觉感知场景，构建了模拟膝部假肢视角的 LP 数据集，并对四个先进单目深度估计基础模型的零样本表现进行系统评测。

### 研究问题
单目深度估计基础模型已在多样视觉域中表现出较强的零样本泛化能力，但这类模型能否用于下肢假肢的视觉感知尚缺乏系统研究。假肢使用者在楼梯、不平整地形等复杂环境中导航时，需要可靠的深度感知，因此有必要评估从假肢视角出发的深度估计性能。

### 核心思路/方法
论文提出 Lower-Limb Prosthesis（LP）数据集，作为从模拟膝部假肢视角评估深度感知的基准；在该数据集上对四个先进的单目深度估计基础模型进行评测，以分析这些模型在假肢视角下的零样本深度估计表现。

### 主要贡献
- 引入 LP 数据集，用于从模拟膝部假肢视角评测深度感知。
- 基于该数据集对四个先进的单目深度估计基础模型进行评估。
- 提供首个从假肢视角开展的单目深度估计性能系统基准，并揭示基础模型在假肢感知系统中部署的挑战与潜力。

### 局限性
- 摘要未提供足够信息说明所评测的四个模型具体名称、评测指标、定量结果及误差分析。
- 摘要未提供足够信息说明 LP 数据集的规模、采集方式、场景构成与标注细节。
- 摘要未提供足够信息说明模拟膝部假肢视角的具体构建方式及其与真实假肢感知系统的差异。
- 摘要未提供足够信息说明是否包含真实假肢使用者实验或临床验证。

### 阅读优先级
中。理由：该论文将零样本单目深度估计基础模型与下肢假肢视觉感知这一具体应用场景结合，并提出新基准数据集，对计算机视觉在辅助感知中的应用研究具有参考价值；但摘要未给出具体模型、实验设置和定量结论，是否值得深入阅读需结合全文实验细节进一步判断。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation has advanced rapidly with the development of foundation models that demonstrate strong zero-shot generalisation across diverse visual domains. However, the applicability of these models to visual perception for lower-limb prosthetics remains largely unexplored. Reliable depth perception is particularly important for prosthesis users, who often experience significant challenges when navigating stairs, uneven terrain, and other complex environments. To address this gap, we introduce the Lower-Limb Prosthesis (LP) dataset, a benchmark designed to evaluate depth perception from an emulated knee-level prosthetic viewpoint. Using this dataset, we evaluate four state-of-the-art monocular depth estimation foundation models. Our results provide the first systematic benchmark of monocular depth estimation performance from a prosthetic viewpoint, while highlighting both the challenges and the potential of deploying foundation models in prosthetic perception systems. The code and dataset are available at https://github.com/Ishivijay/lp_dataset.

</details>

#### 2026-10-25 - Hybrid Mamba-Transformer Network for Single-Shot 3D Reconstruction from Fringe Patterns

**Authors:** Xinjie Zhou, XiaoLei Li
**Links:** [abs](https://arxiv.org/abs/2610.33988) - [pdf](https://arxiv.org/pdf/2610.33988)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hybrid Mamba-Transformer Network for Single-Shot 3D Reconstruction from Fringe Patterns
- 作者：Xinjie Zhou, XiaoLei Li
- 出版日期：2026-10-25T01:58:48Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2610.33988 ；PDF https://arxiv.org/pdf/2610.33988

### 一句话总结
提出一种基于 Swin U 形架构的 Mamba-Transformer 混合网络，用于从单张条纹图回归高度，在公开 FPP 数据集上以 MAE、RMSE、绝对相对误差和 SSIM 优于 hNet、SwinConvUNet、UHRNet 与 HiDNet。

### 研究问题
论文关注基于条纹投影轮廓术（FPP）的单帧 3D 重建：如何从单张高频条纹图像中恢复准确表面高度。摘要指出难点在于同时保持长程空间一致性与精细几何细节。卷积网络在建模长程依赖方面受限，而基于窗口的 Transformer 只能随深度增加逐步建立全局交互。

### 核心思路/方法
- 任务形式：条纹到高度（fringe-to-height）回归。
- 总体架构：采用基于 Swin 的 U 形架构，并在中间分辨率的编码器阶段引入视觉状态空间建模。
- 关键模块：提出轴向与膨胀视觉状态空间（ADVSS）块，通过局部、膨胀和轴向深度卷积增强预扫描特征编码，同时保留四方向选择性扫描。
- 设计目标：结合线性复杂度的长程建模与方向感知的局部条纹结构保持能力。

### 主要贡献
- 提出用于单帧 FPP 条纹到高度回归的混合 Mamba-Transformer 网络。
- 在 Swin U 形架构的中间分辨率编码器阶段引入视觉状态空间建模。
- 设计 ADVSS 块，以局部、膨胀、轴向深度卷积增强预扫描特征编码，并保留四方向选择性扫描。
- 在公开 FPP 数据集上与 hNet、SwinConvUNet、UHRNet、HiDNet 对比，在 MAE、RMSE、绝对相对误差和 SSIM 上均取得更优结果。
- 仅使用一张变形条纹图时，报告 RMSE 为 0.548 mm、SSIM 为 0.9985；相对 UHRNet 与 HiDNet，RMSE 分别降低 65.2% 与 59.6%。

### 局限性
- 摘要仅给出在公开 FPP 数据集上的整体指标对比，未提供数据集名称、训练细节、参数量、推理速度或跨数据集泛化结果。
- 摘要未提供消融实验的完整设置与逐项结果，因此各模块（如 ADVSS）的独立增益无法从摘要中确认。
- 摘要未讨论方法在高频条纹、噪声、遮挡或非理想成像条件下的失效情形。
- 上述未提及内容均属于“摘要未提供足够信息”。

### 阅读优先级
中。理由：论文面向单帧 FPP 3D 重建这一明确任务，给出可量化的 RMSE 与 SSIM 改进，并与多个基线对比，主题与 3D 重建分类直接相关；但摘要未提供数据集名称、消融细节、效率指标与泛化实验，若需评估方法可复现性或实际部署价值，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Deep learning facilitates rapid single shot three dimensional (3D) reconstruction using fringe projection profilometry (FPP), but recovering accurate surface height from a single high frequency fringe image remains challenging because both long-range spatial consistency and fine geometric details must be preserved. Convolutional networks are limited in modeling long range dependencies, whereas window-based Transformers establish global interactions only progressively with increasing depth. To address these limitations, a hybrid Mamba Transformer network is proposed for fringe to height regression. The network adopts a Swin based U shaped architecture and introduces visual state space modeling at the intermediate resolution encoder stage. An axial and dilated vision state space (ADVSS) block is further developed to enhance prescan feature encoding through local, dilated, and axial depthwise convolutions while retaining four directional selective scanning. This design combines linear complexity long range modeling with direction aware preservation of local fringe structures. Experiments on a publicly available FPP dataset show that the proposed method outperforms hNet, SwinConvUNet, UHRNet, and HiDNet in mean absolute error(MAE), root mean square error (RMSE), absolute relative error, and structural similarity index measure (SSIM). Using only one deformed fringe image, the proposed method achieves an RMSE of 0.548 mm and an SSIM of 0.9985, reducing RMSE by 65.2% and 59.6% relative to UHRNet and HiDNet, respectively. These results demonstrate the effectiveness of combining selective state space modeling with hierarchical window based attention for accurate single-shot FPP reconstruction.

</details>

#### 2026-10-22 - OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields

**Authors:** Namitha Guruprasad, Abhay Yadav, Cheng Peng, Rama Chellappa, Anand Bhattad
**Links:** [abs](https://arxiv.org/abs/2610.31645) - [pdf](https://arxiv.org/pdf/2610.31645)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields
- 作者：Namitha Guruprasad, Abhay Yadav, Cheng Peng, Rama Chellappa, Anand Bhattad
- 出版日期：2026-10-22T17:55:30Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供。
- 链接：摘要页 https://arxiv.org/abs/2610.31645 ；PDF 链接 https://arxiv.org/pdf/2610.31645

### 一句话总结
OmniRay 是一个前馈式单目 3D 重建模型，通过由单调径向基、球谐残差和自由形式残差组成的复合射线场，在不同相机几何下预测逐像素射线方向与尺度未知的径向距离，从而在推理时无需相机信息即可恢复 3D 点云。

### 研究问题
摘要指出，多数单目 3D 重建模型假设针孔相机，因此在鱼眼、全景等广角镜头图像上会产生扭曲的几何；相机感知模型虽通过预测逐像素射线场来摆脱针孔假设，却用单一固定基同时表示整体相机投影与更细变化。论文要解决的问题是如何更有效地表示多样相机几何，并实现与相机无关的单目 3D 重建。

### 核心思路/方法
论文提出将相机几何视为具有层次复杂性的射线表示，并设计 OmniRay 的前馈模型，其 Ray Module 由三部分组成：
1. 单调径向基，用于捕捉径向对称结构；
2. 球谐残差，用于表示相对于径向基的平滑偏差；
3. 自由形式残差，用于表示剩余的局部变化。
这些组件以球面上的连续旋转方式组合，使表示能够适应多样相机几何。给定单张图像，OmniRay 为每个像素预测射线方向和尺度未知的径向距离，并由此恢复 3D 点云，推理时不需要相机信息。

### 主要贡献
- 提出 OmniRay，一个与相机无关的单目前馈 3D 重建模型。
- 设计复合射线场表示，将射线表示拆分为单调径向基、球谐残差和自由形式残差，并以球面连续旋转组合。
- 在推理时无需相机信息，即可从单张图像预测逐像素射线方向和尺度未知径向距离，进而恢复 3D 点云。
- 摘要称在不同相机配置上的广泛实验表明，OmniRay 在相机无关单目 3D 重建上建立了新的 state-of-the-art。

### 局限性
摘要未提供足够信息说明局限性。摘要未给出具体实验数据集、评价指标、定量结果、失败案例、计算开销或对不同相机类型的覆盖范围等细节；这些信息摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对相机无关单目 3D 重建中的相机几何表示问题，提出层次化复合射线场，并声称在多种相机配置下达到新的 state-of-the-art；若关注广角、鱼眼或全景图像的单目 3D 重建，该工作与问题设定高度相关。但需注意，摘要未提供实验细节，阅读全文前应保持对结论范围和适用条件的审慎判断。

</details>

<details>
<summary>Abstract</summary>

Monocular models recover 3D geometry from a single image in one pass, but most assume a pinhole camera and produce distorted geometry on the wide-angle imagery produced by fisheye and panoramic lenses. Camera-aware models remove this assumption by predicting a per-pixel ray field. However, they represent different camera geometries using a single fixed basis to capture both the overall camera projection and its finer variations. We argue that camera geometry can be viewed as having a hierarchy of complexity for representing rays. We present OmniRay, a feed-forward model whose Ray Module is composed of three components: a monotone radial base that captures radially symmetric structure, a spherical-harmonic residual for smooth deviations from it, and a free-form residual for remaining local variation. These components are composed as successive rotations on the sphere, allowing the representation to accommodate diverse camera geometries. Given a single image, OmniRay predicts a ray direction and an up-to-scale radial distance for every pixel, from which a 3D point cloud is recovered without needing camera information at inference time. Extensive experiments across different camera configurations demonstrate that OmniRay establishes a new state-of-the-art in camera-agnostic monocular 3D reconstruction.

</details>

#### 2026-10-22 - HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction

**Authors:** Zunnan Xu, Shangchen Zhou, Yihang Luo, Chen Change Loy
**Links:** [abs](https://arxiv.org/abs/2610.31635) - [pdf](https://arxiv.org/pdf/2610.31635)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction
- 作者：Zunnan Xu, Shangchen Zhou, Yihang Luo, Chen Change Loy
- 出版日期：2026-10-22T17:51:10Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.31635) / [PDF](https://arxiv.org/pdf/2610.31635)

### 一句话总结
HiP3R 提出分层位姿图：先用块级 Sim(3) 图建立全局布局与尺度，再固定布局、按帧估计共享 SE(3) 相机，以缓解长视频分块重建中的全局一致性与局部修正之间的权衡。

### 研究问题
前馈模型可对短视频窗口准确估计相机运动与 3D 几何，但计算和内存成本使其无法直接处理数千帧序列。长视频因此被切分为重叠块，产生坐标帧不一致、共享相机重复估计的独立局部重建。要实现全局一致性，需要跨相邻重叠和远距离重访传播约束，这自然指向位姿图优化；但图层级选择存在权衡：块级图能高效处理尺度漂移和大回环，却无法用刚体变换修正内部误差或冲突的帧预测；帧级优化提供局部灵活性，但全局扩展计算昂贵且可能破坏度量尺度。

### 核心思路/方法
HiP3R 使用分层位姿图解决上述权衡。首先优化一个鲁棒的块级 Sim(3) 图，以建立全局布局和尺度；随后固定该布局，为每一帧估计一个共享的 SE(3) 相机，将重叠窗口预测转化为单一轨迹。该方法可应用于基于块和流式的后端，且无需额外训练或微调。

### 主要贡献
- 提出分层位姿图 HiP3R，用于长时序 3D 重建中的全局一致性优化。
- 通过块级 Sim(3) 图建立全局布局与尺度，再固定布局进行帧级共享 SE(3) 相机估计，以结合块级效率与帧级局部灵活性。
- 摘要称在多个基准上验证了方法在改善相机轨迹和 3D 重建方面的有效性。
- 方法适用于基于块和流式的后端，无需额外训练或微调，并提供代码链接。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集规模、计算开销、失败案例或定量对比细节；分层优化的具体鲁棒性边界、对极端尺度漂移或严重冲突预测的表现也摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对长视频 3D 重建中“分块独立重建导致全局不一致”的关键问题，提出清晰的分层位姿图方案，问题动机和方法权衡描述较明确；但摘要未提供定量实验结果与实现细节，是否优先精读取决于读者对长时序重建、位姿图优化或流式后端的直接兴趣。

</details>

<details>
<summary>Abstract</summary>

Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distant revisits across the sequence. This requirement naturally motivates pose graph optimization. However, the choice of graph level creates a trade-off. Chunk-level graphs efficiently resolve scale drift and close large loops. Yet, their rigid transformations cannot correct internal errors or conflicting frame predictions. Conversely, frame-level optimization offers local flexibility, but scaling it globally is computationally expensive and can break metric scale. HiP3R resolves this trade-off using a hierarchical pose graph. HiP3R first optimizes a robust chunk-level $\mathrm{Sim}(3)$ graph to establish the global layout and scale. It then holds this layout fixed and estimates one shared $\mathrm{SE}(3)$ camera per frame, turning overlapping window predictions into a single trajectory. Experiments across multiple benchmarks demonstrate the effectiveness of HiP3R in improving camera trajectories and 3D reconstruction. Our method applies to both chunk-based and streaming backends without additional training or fine-tuning. The codes are available at https://kkakkkka.github.io/HiP3R.

</details>

#### 2026-10-22 - F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation

**Authors:** Jinyu Zhang, Haitao Lin, Jiashu Hou, Xiangyang Xue, Yanwei Fu
**Links:** [abs](https://arxiv.org/abs/2610.31623) - [pdf](https://arxiv.org/pdf/2610.31623)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation
- 作者：Jinyu Zhang, Haitao Lin, Jiashu Hou, Xiangyang Xue, Yanwei Fu
- 出版日期：2026-10-22T17:43:34Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2610.31623) / [PDF](https://arxiv.org/pdf/2610.31623)

### 一句话总结
F2G-Pose 提出一种实时、直接、单次前向的类别级 RGB-D 物体姿态估计框架，通过将稠密视觉基础特征提升到部分点云并结合几何与专家混合 Transformer，在一次前向中预测姿态、度量尺寸和相机坐标系下的补全形状。

### 研究问题
论文研究类别级 RGB-D 物体姿态估计：在没有实例特定 CAD 模型或参考视图的情况下，恢复物体的 3D 旋转与平移。该任务因类内差异、对称性和部分观测而高度模糊。摘要指出，现有方法难以兼顾可靠性与效率：基于中间结构的方法容易产生误差传播，扩散模型则存在推理延迟高和后处理候选提取复杂的问题。

### 核心思路/方法
F2G-Pose 是一个实时、直接、单次前向的框架，从单次 RGB-D 观测中预测类别级姿态、度量尺寸和相机坐标系下的补全形状。方法将稠密视觉基础特征提升到部分点云上，使用 DGCNN tokenization 编码局部几何，并通过 Mixture-of-Experts Transformer 整合物体级结构。联合的尺寸预测与相机坐标系形状补全通过稠密几何监督促进度量一致性。其任务特定网络仅在带姿态标注的合成 SOPE 数据上训练，冻结的 RADIO 主干为外部预训练。

### 主要贡献
- 提出 F2G-Pose，一个实时、直接、单次前向的类别级 RGB-D 物体姿态估计框架，同时预测姿态、度量尺寸和相机坐标系补全形状。
- 设计将稠密视觉基础特征提升到部分点云、结合 DGCNN tokenization 与 Mixture-of-Experts Transformer 的几何感知方法。
- 通过联合尺寸预测与形状补全及稠密几何监督，促进度量一致性。
- 摘要报告其在 SOPE 和 ROPE 上达到 state-of-the-art 精度，仅姿态推理运行速度为 28 FPS，并在 HouseCat6D 上展示相机坐标系几何能力、在 HANDAL 上展示真实物体迁移能力。
- 摘要还提到对延迟、鲁棒性、形状补全和 GenPose++ 候选行为的分析，以及真实世界操作实验展示部署潜力；项目页面、代码和预训练模型已公开。

### 局限性
摘要未提供足够信息说明明确局限性。仅能从摘要中看到：任务特定网络仅在带姿态标注的合成 SOPE 数据上训练；真实世界实验基于分割后的 RGB-D 输入；摘要未给出失败案例、泛化边界或计算资源需求的详细讨论。

### 阅读优先级
高。理由：该论文针对类别级 RGB-D 物体姿态估计中可靠性与效率的权衡问题，提出单次前向实时框架，摘要声称在 SOPE 和 ROPE 上达到 state-of-the-art，并报告 28 FPS 姿态推理速度，同时涉及形状补全、真实物体迁移和真实操作实验，与该方向的研究和部署关注点高度相关。

</details>

<details>
<summary>Abstract</summary>

This paper studies category-level RGB-D object pose estimation, which recovers an object's 3D rotation and translation without instance-specific CAD models or reference views. This task is highly ambiguous due to intra-class variations, symmetries, and partial observations. Current solutions struggle to balance reliability and efficiency: methods based on intermediate structures are prone to error propagation, while diffusion models suffer from high inference latency and complex post-hoc candidate extraction. To address this, we present F2G-Pose, a real-time direct, single-pass framework that predicts category-level pose, metric size, and camera-frame completed shape from a single RGB-D observation in one feed-forward pass. F2G-Pose lifts dense visual foundation features to partial point clouds, encodes local geometry with DGCNN tokenization, and integrates object-level structure with a Mixture-of-Experts Transformer. Joint size prediction and camera-frame shape completion encourage metric consistency through dense geometric supervision. With its task-specific network trained only on pose-annotated synthetic SOPE data and its frozen RADIO backbone externally pretrained, F2G-Pose achieves state-of-the-art accuracy on SOPE and ROPE while running at 28 FPS for pose-only inference, and further demonstrates strong camera-frame geometry on HouseCat6D and real-object transfer on HANDAL. Analyses of latency, robustness, shape completion, and GenPose++ candidate behavior further demonstrate the efficiency and reliability of F2G-Pose, with real-world manipulation experiments demonstrating deployment potential under segmented RGB-D inputs. The project page, code, and pretrained models are made available at https://jrryzh.github.io/F2G-Pose/.

</details>

#### 2026-10-22 - H-2DGS: Height-Field Gaussian Splatting for Sharp and Deformable Neurosurgical Surface Reconstruction

**Authors:** Zhang Zichuan, Bart Brouwers, Rembrandt Bakker, Maud Landers, Geert-Jan Rutten, Maxime Chamberland
**Links:** [abs](https://arxiv.org/abs/2610.30910) - [pdf](https://arxiv.org/pdf/2610.30910)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：H-2DGS: Height-Field Gaussian Splatting for Sharp and Deformable Neurosurgical Surface Reconstruction
- 作者：Zhang Zichuan, Bart Brouwers, Rembrandt Bakker, Maud Landers, Geert-Jan Rutten, Maxime Chamberland
- 出版日期：2026-10-22T08:33:14Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.30910 ；PDF https://arxiv.org/pdf/2610.30910

### 一句话总结
论文提出 H-2DGS，一种三阶段的高度场 2D 高斯泼溅流程，用于在神经外科场景中获得尖锐、可变形且能与 MRI 和扩散示踪路径共同可视化的皮层表面重建。

### 研究问题
神经外科导航通常以 2D MRI 切片呈现信息，难以将切片中的解剖结构与手术显微镜下观察到的皮层表面对应起来。论文希望构建一个共同的 3D 可视化，将肿瘤手术中暴露皮层的照片级真实重建、全脑 MRI 背景以及扩散示踪路径结合起来。该任务要求重建的皮层形成清晰的解剖边界，而不是模糊、会遮挡内部结构的弥散体积。传统 3D Gaussian Splatting 虽能复现观察视角，但在手术视角覆盖有限时，可能将不透明度分布到较厚且几何含糊的带状区域中。

### 核心思路/方法
论文提出 height-field 2D Gaussian Splatting（H-2DGS），包含三个阶段：
1. 进行稳健的 3DGS 重建；
2. 将其深度融合到共享的截断符号距离场（TSDF）表面中；
3. 用弯曲的、面向表面的 Gaussian 基元表示该表面。

方法中分别使用高度、颜色和不透明度基来表示局部几何与外观，并通过邻居过渡目标协调重叠 patch。显式表面还支持术后对齐：由 MRI 导出的深度使重建发生变形，而带跟踪的颜色监督与交替优化用于保持外观。

### 主要贡献
- 提出 H-2DGS 三阶段流程，将 3DGS 重建、TSDF 表面融合与面向表面的 2D Gaussian 表示结合，以缓解有限手术视角下传统 3DGS 不透明度弥散和几何含糊的问题。
- 通过高度、颜色、不透明度分离基以及邻居过渡目标，建模局部几何与外观并协调重叠 patch。
- 利用显式表面支持术后对齐，包括 MRI 深度驱动的形变和带跟踪颜色监督的交替优化。
- 在五个真实神经外科案例中报告了较低的多视角深度不一致性、紧凑的 7.97MB 表示，以及每帧 29--42ms 的交互式渲染。
- 摘要称所得尖锐、可变形表面可与示踪路径和 MRI 解剖清晰整合，并包括术后切除腔。

### 局限性
摘要未提供足够信息来说明方法的局限性、失败案例、适用范围边界或更全面的定量对比结果。摘要仅提到五个真实神经外科案例及部分指标，未提供数据规模细节、统计显著性、基线完整对比或临床验证信息。

### 阅读优先级
高。理由：论文聚焦神经外科导航中的 3D 可视化与皮层表面重建，问题明确；方法将 3DGS、TSDF 与可变形表面表示结合，并给出真实病例、表示大小和交互渲染时间等摘要级结果；对多视角几何、神经渲染及医学图像引导重建方向具有较高相关性。但摘要未提供完整实验细节和局限性，深入判断仍需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Neurosurgical navigation commonly presents magnetic resonance imaging (MRI) as 2D slices, making it difficult to relate the anatomy in those slices to the cortical surface observed through the surgical microscope. We seek a common 3D visualization that combines a photorealistic reconstruction of the exposed cortex during tumor surgery with whole-brain MRI context and diffusion tractography pathways. This requires the reconstructed cortex to form a clear boundary around the brain anatomy rather than a diffuse volume that obscures internal structures. Conventional 3D Gaussian Splatting (3DGS) can reproduce observed views but, under limited surgical view coverage, may distribute opacity through a thick and geometrically ambiguous band. We introduce height-field 2D Gaussian Splatting (H-2DGS), a three-stage pipeline that concentrates a robust 3DGS reconstruction, fuses its depth into a shared truncated signed distance field (TSDF) surface, and represents that surface with curved, surface-oriented Gaussian primitives. Separate height, color, and opacity bases provide local geometry and appearance, while a neighbor-transition objective coordinates overlapping patches. The explicit surface further supports postoperative alignment: MRI-derived depth deforms the reconstruction, and tracked-color supervision with alternating optimization preserves its appearance. Across five real neurosurgical cases, H-2DGS gives low multi-view depth inconsistency, a compact 7.97MB representation, and interactive rendering at 29--42ms per frame. The resulting sharp, deformable surface integrates clearly with tractography and MRI anatomy, including a postoperative resection cavity.

</details>

#### 2026-10-22 - WovenAnchor Matcher: Specialized Intra- and Inter-Image Context Modeling for Feature Matching

**Authors:** Zhiyang Li, Ruijiang Jin, Thibaut Klenke, Yusuke Sekikawa, Nakamasa Inoue
**Links:** [abs](https://arxiv.org/abs/2610.30799) - [pdf](https://arxiv.org/pdf/2610.30799)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WovenAnchor Matcher: Specialized Intra- and Inter-Image Context Modeling for Feature Matching
- 作者：Zhiyang Li, Ruijiang Jin, Thibaut Klenke, Yusuke Sekikawa, Nakamasa Inoue
- 出版日期：2026-10-22T06:24:39Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.30799 ；PDF https://arxiv.org/pdf/2610.30799

### 一句话总结
论文提出 WovenAnchor Matcher（WAM），一种基于“角色专门化上下文聚合”的半稠密特征匹配框架，分别用 WovenMamba 做图内聚合、AnchorCrossAttention 做图间聚合，并在 MegaDepth 上报告了相对 JamMa 基线的姿态估计提升。

### 研究问题
半稠密局部特征匹配通常在进行由粗到细的对应估计之前聚合上下文信息。论文指出，图内聚合与图间聚合承担不同角色：图内聚合应在每幅图像内传播空间证据并保留结构化的二维依赖；图间聚合应从可能对应的区域收集信息，同时限制无关位置带来的噪声。论文关注的是：如何为这两类聚合设计角色专门化的建模方式。

### 核心思路/方法
WAM 是一个基于角色专门化上下文聚合的半稠密匹配框架，引入两个互补算子：
- WovenMamba：通过“先水平、后垂直”的状态空间传播进行图内聚合，使垂直更新作用于已经过水平上下文化的特征，从而鼓励形成结构化的二维感受野偏置。
- AnchorCrossAttention：通过交叉注意力进行图间聚合，从图像对中可能对应的区域收集上下文；该交换在局部代表锚点上进行，而这些锚点聚合每个窗口内的特征证据。
整体流程位于半稠密局部特征匹配的“先聚合上下文、再由粗到细估计对应”的框架之下。

### 主要贡献
- 提出 WAM，一个基于角色专门化上下文聚合的半稠密匹配框架，明确区分图内聚合与图间聚合的不同职责。
- 提出 WovenMamba，以水平后垂直的状态空间传播实现图内聚合，鼓励结构化的二维感受野偏置。
- 提出 AnchorCrossAttention，基于局部代表锚点进行交叉注意力图间聚合，以从可能对应区域收集信息并限制无关位置噪声。
- 在 MegaDepth 上报告 66.1 pose AUC@5°，在相同评估设置下较 JamMa 基线提升 2.0 AUC 点。
- 消融显示移除或替换任一专门化组件都会降低精度，为图内传播与图间检索受益于角色专门化聚合设计提供证据。
- 代码与预训练权重已公开于 https://github.com/mmaiLab/WovenAnchorMatcher。

### 局限性
摘要未提供足够信息。摘要未说明计算开销、参数量、推理速度、内存占用、训练数据规模与训练细节、除 MegaDepth 外其他数据集的表现、失败场景或方法适用范围等局限相关信息。

### 阅读优先级
中。理由：论文聚焦半稠密特征匹配中的图内/图间上下文聚合角色区分，问题界定清晰，方法由两个职责明确的算子组成，并在 MegaDepth 上给出相对 JamMa 基线的定量提升与组件消融证据；对于关注特征匹配、多视图几何与 3D 重建中上下文建模的研究者有直接相关性。但摘要仅覆盖单一数据集上的姿态 AUC 与消融结论，未提供效率、泛化到其他基准或局限性的信息，若需要全面评估方法适用性，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Semi-dense local feature matching commonly aggregates contextual information before coarse-to-fine correspondence estimation. However, intra-image and inter-image aggregation serve different roles: the former should propagate spatial evidence within each image while retaining structured two-dimensional dependencies, whereas the latter should gather information from plausible corresponding regions while limiting noise from unrelated locations. We propose WovenAnchor Matcher (WAM), a semi-dense matching framework based on role-specialized context aggregation. WAM introduces two complementary operators. WovenMamba performs intra-image aggregation through horizontal-then-vertical state-space propagation, allowing vertical updates to operate on horizontally contextualized features and thereby encouraging a structured two-dimensional receptive-field bias. AnchorCrossAttention performs inter-image aggregation by using cross-attention to gather context from plausible corresponding regions across the image pair. It performs this exchange over local representative anchors that aggregate feature evidence within each window. On MegaDepth, WAM achieves 66.1 pose AUC@5$^\circ$, improving on the JamMa baseline by 2.0 AUC points under the same evaluation setup. Ablations show that removing or replacing either specialized component reduces accuracy, providing evidence that intra-image propagation and inter-image retrieval benefit from role-specific aggregation designs. Code and pretrained weights are available at https://github.com/mmaiLab/WovenAnchorMatcher.

</details>

#### 2026-10-22 - Evaluation of Front-End Feature Matching for Lunar Visual SLAM

**Authors:** Guillem Casadesus Vila, Grace Gao
**Links:** [abs](https://arxiv.org/abs/2610.30774) - [pdf](https://arxiv.org/pdf/2610.30774)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, visual SLAM, feature matching, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evaluation of Front-End Feature Matching for Lunar Visual SLAM
- 作者：Guillem Casadesus Vila, Grace Gao
- 出版日期：2026-10-22T05:52:13Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.30774) / [PDF](https://arxiv.org/pdf/2610.30774)

### 一句话总结
该论文在九个月球合成数据、月球试验台和地球类比数据集上，对十一种经典与学习型检测-匹配器组合及一个特征跟踪器，进行两两位姿精度和视觉里程计轨迹误差的基准评测。

### 研究问题
月球车在导航卫星服务部署前主要依赖相机定位，之后仍需要相机进行相对导航、危险检测和地表操作。视觉里程计（VO）和同步定位与建图（SLAM）大多通过帧间特征匹配估计运动，但现有特征匹配器多在城市、室内和驾驶场景中开发；行星研究或在轨道配准中比较匹配器，或在完整 SLAM 系统中比较，且带有参考位姿的真实月球图像稀缺。因此，在低纹理、光照严苛的月球地形上，月球车帧间匹配的表现及其对 VO 的影响尚未得到比较。

### 核心思路/方法
- 基准评测十一种经典与学习型检测器-匹配器组合，以及一个特征跟踪器。
- 使用九个月球合成、月球试验台和地球类比数据集。
- 评价指标包括：两两位姿精度（与基线比较）以及所得 VO 的轨迹误差。
- 在仅旋转度量下比较匹配器；并联合旋转与平移方向进行评分。
- 在立体 VO 中评估各配对能否持续跟踪全部八个序列数据集。
- 分析光照条件（如低聚光灯与漫射光）对经典检测器配对和 SuperPoint 的影响。
- 报告学习型组合的速度，并讨论 DINOv2 检索提案是否仍需几何验证。

### 主要贡献
- 在月球相关场景下系统比较经典与学习型特征检测-匹配组合，而非仅依赖城市、室内或驾驶场景结论。
- 指出在仅旋转度量下，SuperPoint 配对在两个月球试验台和一个类比站点上优于使用比率检验 FLANN 匹配的 SIFT；但在合成数据上差异较小或未解决。
- 指出当联合评分旋转与平移方向时，该 SIFT 配对在四个合成数据集上超过两个 SuperPoint 配对，说明仅凭合成结果不能确定真实月球车图像上的相对性能。
- 发现在立体 VO 中 SuperPoint 配对并不始终比 SIFT 更准确，但只有它们能在全部八个序列数据集上保持跟踪。
- 发现经典检测器配对依赖光照，而 SuperPoint 变化较小；同一试验台视图下低聚光灯使经典配对比漫射光更准确，这与更高对比度和检测到更多关键点一致。
- 报告 SuperPoint 与 LightGlue 是最快的学习型组合（每帧 16 ms），并指出 DINOv2 检索提案仍需要几何验证。

### 局限性
- 摘要未提供足够信息说明各数据集的规模、具体序列数量（除八个序列数据集外）、场景多样性及采集条件细节。
- 摘要未提供足够信息说明 VO 系统实现细节、基线定义、评价指标的具体计算方式与统计显著性。
- 摘要未提供足够信息说明 DINOv2 检索提案的具体实验配置及其几何验证需求的程度。
- 摘要未提供足够信息说明结论在真实月球任务环境中的泛化能力。
- 摘要未提供足够信息说明除 SuperPoint、SIFT、LightGlue、DINOv2 外其余检测-匹配组合的具体表现。

### 阅读优先级
高。理由：该论文直接面向月球视觉 SLAM 前端特征匹配这一关键但缺乏真实月球图像比较的问题，提供了跨合成、试验台和地球类比数据的基准结果，并明确指出合成结果与真实场景性能之间的差异，对月球车视觉定位与 VO 研究具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However, feature matchers are developed on urban, indoor and driving scenes, planetary studies compare them on orbital registration or within complete SLAM systems, and real lunar imagery with reference poses is scarce, so matching between rover frames on low-texture, harshly lit terrain, and its effect on VO, has not been compared. We benchmark eleven classical and learned detector-matcher combinations on nine synthetic, lunar-testbed, and terrestrial-analogue datasets, and a feature tracker, scoring pairwise pose accuracy against baseline and the trajectory error of the resulting VO. Under a common rotation-only metric, the SuperPoint pairings outperform SIFT with ratio-tested FLANN matching on both lunar testbeds and one analogue site, with smaller or unresolved differences on synthetic data. When rotation and translation direction are scored jointly, this SIFT pairing exceeds both SuperPoint pairings on four synthetic datasets, so synthetic results alone do not establish relative performance on real rover imagery. In stereo VO, the SuperPoint pairings are not consistently more accurate than SIFT, but only they keep tracking on all eight sequential datasets. Pairings with classical detectors depend on lighting while SuperPoint changes little: a low spotlight makes them more accurate than diffuse light on the same testbed views, consistent with more contrast and detected keypoints. SuperPoint with LightGlue is the fastest learned combination (16 ms per frame), and DINOv2 retrieval proposals still need geometric verification.

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-27 - GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis

**Authors:** Akshay Krishnan, Matias Turkulainen, Jamie Wynn, Zawar Qureshi, Mohamed Sayed, Guillermo Garcia-Hernando, Sara Vicente, James Hays, Michael Firman, Daniyar Turmukhambetov
**Links:** [abs](https://arxiv.org/abs/2610.37545) - [pdf](https://arxiv.org/pdf/2610.37545)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis
- 作者：Akshay Krishnan, Matias Turkulainen, Jamie Wynn, Zawar Qureshi, Mohamed Sayed, Guillermo Garcia-Hernando, Sara Vicente, James Hays, Michael Firman, Daniyar Turmukhambetov
- 出版日期：2026-10-27T16:56:45Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要 https://arxiv.org/abs/2610.37545 ；PDF https://arxiv.org/pdf/2610.37545

### 一句话总结
提出一种以卫星图像作为额外条件的多视图扩散模型，用于户外稀疏街景的新视角合成，以缓解外推时空间布局幻觉，且无需三维重建。

### 研究问题
多视图或视频扩散模型在稀疏图像集合的新视角合成中效果突出，但在输入视角之外（场景外推）合成时容易产生不真实的空间布局幻觉。论文聚焦户外场景，试图利用卫星图像提供额外场景布局信息来约束生成。

### 核心思路/方法
将卫星图像与街景输入图像共同作为条件，构建卫星条件化的多视图扩散模型；采用基于交叉注意力的条件注入方式，以保留预训练多视图扩散先验，在生成新视角时同时贴合卫星图像所见的场景布局；方法不依赖三维场景重建，仅使用带位姿的街景与卫星视图。

### 主要贡献
- 面向户外外推场景，提出使用卫星图像作为多视图生成模型的额外条件来源。
- 提出卫星条件化多视图扩散模型，结合卫星图像与街景输入图像进行新视角生成。
- 通过交叉注意力条件注入保留预训练多视图扩散先验，生成无缝、真实的新视角并遵循卫星图像中的场景布局。
- 方法不进行三维场景重建，仅依赖带位姿的街景和卫星视图。
- 摘要称在户外数据集实验中优于卫星条件化或街景条件化的基线，尤其在目标视角与源视角重叠很少的困难情形下。

### 局限性
摘要未提供足够信息。摘要未给出计算开销、对卫星图像时效性或对齐质量的敏感性、失败案例、定量指标细节及数据集规模等限制性信息。

### 阅读优先级
中。理由：选题针对稀疏街景外推中的布局幻觉，且用卫星图像做条件、无需三维重建，具有明确的问题意识与应用潜力；但当前仅有摘要信息，缺少定量结果、实验设置与局限性细节，需阅读全文后再判断其方法稳健性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Multi-view or video diffusion models have recently emerged as state-of-the-art approaches for novel-view synthesis from sparse image collections. While they can produce high quality images, they tend to hallucinate unrealistic spatial layouts when synthesizing views outside the input views (scene extrapolation). We propose to address this challenge for outdoor scenes by using satellite images as an additional information source to condition the multi-view generative model. We introduce a new satellite-conditioned multi-view diffusion model that combines conditioning from a satellite image and street-level input images when generating novel-views. Our cross-attention based conditioning allows us to retain pretrained multi-view diffusion priors to generate seamless, realistic, novel views from a handful of source views, while also adhering to the scene layout as seen from satellite images. Our model does not use 3D scene reconstruction, and only relies on posed street and satellite views. Our experiments on outdoor datasets show that our model is better than both satellite-conditioned or street-view conditioned baselines on novel-view synthesis, especially on challenging cases where target views have very little overlap with source views. Project page: https://nianticspatial.github.io/groundcontrol

</details>

#### 2026-10-27 - CTBakeGS: training-free baking of photorealistic CT volume renderings into 3D Gaussian splats

**Authors:** Haruki Fukuda, Constantin Lux, Wolf Schweitzer, Tadashi Hosoya, Lars Ebert
**Links:** [abs](https://arxiv.org/abs/2610.37406) - [pdf](https://arxiv.org/pdf/2610.37406)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CTBakeGS: training-free baking of photorealistic CT volume renderings into 3D Gaussian splats
- 作者：Haruki Fukuda, Constantin Lux, Wolf Schweitzer, Tadashi Hosoya, Lars Ebert
- 出版日期：2026-10-27T15:21:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37406) / [PDF](https://arxiv.org/pdf/2610.37406)

### 一句话总结
该论文提出一种无需训练的“烘焙”方法，将 CT 体渲染结果直接转换为 3D Gaussian splats 模型，从而在普通设备上实时展示照片级 CT 渲染。

### 研究问题
CT 体渲染能直观呈现解剖结构，但依赖 CT 数据、专用软件和强大 GPU。现有医学 3DGS 方法需要为每个场景训练数分钟到数小时。论文要解决的问题是：能否不经过训练，直接把 CT 体渲染转换为可实时显示的 3DGS 模型。

### 核心思路/方法
- 将 splats 放置在毫米级单元格的自适应八叉树上。
- 在 GPU 上利用渲染器的光照计算 splat 的颜色和不透明度。
- 将单元格不透明度解析地转换为 splat 不透明度。
- 对低于标准 3DGS 光栅器 1/255 不透明度下限的微弱 splat，采用随机方式保留。
- 在 6 个公开 CT 扫描（1.5-mm 体素）上，使用三种传递函数进行转换，并与收敛参考比较 PSNR、结构相似性和学习感知指标。

### 主要贡献
- 提出无需训练的 CT 体渲染到 3DGS 的直接转换流程。
- 给出基于自适应八叉树、GPU 光照计算、解析不透明度转换和随机保留微弱 splat 的具体方法。
- 报告转换后的模型可在普通计算机上实时渲染：200 万 splat 模型在骨、对比增强血管、皮肤与骨三类设置下分别达到 PSNR 32.6 ± 0.9 dB、30.1 ± 1.0 dB、32.3 ± 1.5 dB。
- 报告转换效率：一次转换通常在笔记本电脑上耗时 4–30 秒，在配备 4-GB 显卡的台式机上耗时 9–60 秒；笔记本电脑上 800 × 800 像素渲染达到 68 fps。

### 局限性
- 摘要仅报告 6 个公开 CT 扫描、1.5-mm 体素和三种传递函数，未说明更大规模或更多样化数据的泛化表现。
- 摘要称保真度“足以用于交互式查看”，但未提供临床诊断或定量医学任务上的验证。
- 摘要未提供与训练型医学 3DGS 方法在同等条件下的系统对比细节。
- 摘要未说明方法对低不透明度 splat 随机保留可能带来的时域稳定性或感知一致性问题。
- 摘要未提供代码、数据或复现细节。

### 阅读优先级
中。理由：该方法针对医学 CT 体渲染的实时可视化，提出无需训练的 3DGS 转换流程，问题明确且报告了转换速度与渲染帧率；但摘要显示评估范围有限，主要面向交互式查看，若关注临床验证、泛化性或与训练型方法的系统比较，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Photorealistic volume rendering of computed tomography (CT) may convey anatomy intuitively, but it needs the CT data, dedicated software and a powerful graphics processor. Three-dimensional Gaussian splatting (3DGS) displays photorealistic scenes in real time on less powerful devices, but existing medical approaches train each scene for minutes to hours. We aimed to convert a CT volume rendering directly into a 3DGS model without training. Splats were placed on an adaptive octree of millimetre-sized cells. Their colour and opacity were computed on the graphics processor with the renderer's lighting, cell opacity was converted analytically into splat opacity, and faint splats were retained stochastically above the 1/255 opacity floor of standard 3DGS rasterisers. Six public CT scans (1.5-mm voxels) were converted with three transfer functions and compared with converged references by peak signal-to-noise ratio (PSNR), structural similarity and a learned perceptual metric. Two-million-splat models reached a PSNR of 32.6 +/- 0.9 dB for bone, 30.1 +/- 1.0 dB for contrast-enhanced vessels and 32.3 +/- 1.5 dB for skin and bone. A conversion pass (usually two or three per model) took 4-30 s on a current laptop and 9-60 s on a desktop with a 4-GB graphics card. On the laptop, the models rendered at 68 frames per second at 800 x 800 pixels. Training-free conversion produced real-time 3DGS models of photorealistic CT renderings in about a minute or less per conversion pass on ordinary computers, with fidelity that we consider sufficient for interactive viewing.

</details>

#### 2026-10-27 - DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality

**Authors:** Anastasiya Pechko, Agata Szymańska, Piotr Borycki, Joanna Szelewska, Michał Mnich, Sławomir Tadeja, Przemysław Spurek
**Links:** [abs](https://arxiv.org/abs/2610.37172) - [pdf](https://arxiv.org/pdf/2610.37172)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality
- 作者：Anastasiya Pechko, Agata Szymańska, Piotr Borycki, Joanna Szelewska, Michał Mnich, Sławomir Tadeja, Przemysław Spurek
- 出版日期：2026-10-27T12:58:16Z
- 分类：Neural Scene Representations & Rendering；次要分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.37172)｜[PDF](https://arxiv.org/pdf/2610.37172)

### 一句话总结
论文提出 DomeGS，将传统 VR 中的“天空穹顶”概念融入 3D Gaussian Splatting 重建场景本身，以补全无界户外场景中不完整的地平线背景，并通过用户实验表明其在空间临场感与真实感上优于天空盒基线。

### 研究问题
摘要指出，VR 对高质量 3D 内容需求旺盛，3DGS 是有前景的高保真场景生成方法；但用 3DGS 重建无界户外场景时，由于数据缺失或缺少远景几何约束，地平线可能不完整，破坏 VR 的沉浸感。传统 VR 常用纹理立方体（skybox）或球体（skydome）营造远景背景，但这些方法与重建的 3DGS 几何难以无缝融合。论文即针对这一背景补全与融合问题展开。

### 核心思路/方法
DomeGS 框架的核心是将 skydome 概念从“平坦的背景外壳”转变为“重建的 Gaussian Splatting 3D 场景的一部分”。通过把地平线与天空整合进 3DGS 表示，方法旨在提供一个统一、场景一致的环境，使前景与背景相衔接，从而提升真实感。摘要未提供足够信息说明具体的网络结构、训练策略、损失函数或数据采集细节。

### 主要贡献
- 提出 DomeGS 框架，将天空穹顶作为 3DGS 场景的组成部分而非独立背景壳，用于无界户外场景的背景补全。
- 通过将地平线与天空纳入 3DGS 表示，构建前景与背景统一、场景一致的环境，以增强 VR 真实感。
- 开展 N=36 的用户实验评估：相比 skybox 基线，DomeGS 显著提升空间临场感（p=0.042）与真实感（p=0.042）。

### 局限性
摘要未提供足够信息说明方法在计算开销、不同场景泛化性、几何一致性定量指标、用户实验设计细节及统计效力等方面的局限；也未提供失败案例或边界条件。

### 阅读优先级
中。理由：该工作聚焦 3DGS 在无界户外 VR 场景中的背景补全与感知一致性，问题明确且有人类用户实验支持（N=36，两项指标显著），对 3DGS/VR 内容生成方向有参考价值；但摘要未披露方法细节与更全面的定量评估，是否需要优先精读取决于读者对 3DGS 背景补全或 VR 感知评估的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

The growing need for high-quality 3D content remains among the most prevalent challenges in virtual reality (VR). Recently, novel view synthesis techniques have enabled rapid content creation, with 3D Gaussian Splatting (3DGS) emerging as one of the most promising methods for generating high-fidelity 3D scenes. However, using 3DGS to reconstruct unbounded outdoor scenes can leave horizons incomplete due to missing data or a lack of distant geometric constraints. Such incompleteness can break immersion, compromising VR's core characteristic. A typical workaround in traditional VR systems is a textured cube (skybox) or sphere (skydome) surrounding the environment to create the illusion of a distant background. However, these approaches struggle to blend seamlessly with the reconstructed 3DGS geometry. To address these issues, we introduce the DomeGS framework, which incorporates the skydome concept not as a flat background shell, but as a part of the reconstructed Gaussian Splatting 3D scene. By integrating the horizon and sky into the 3DGS representation, our method provides a unified, scene-consistent environment bridging foregrounds and backgrounds for greater realism. Experimental evaluation with N=36 users demonstrates that DomeGS significantly increases spatial presence (p=0.042) and realism (p=0.042) compared to the skybox baseline.

</details>

#### 2026-10-27 - GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing

**Authors:** Jinxin Ai, Matthias Niessner
**Links:** [abs](https://arxiv.org/abs/2610.37036) - [pdf](https://arxiv.org/pdf/2610.37036)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing
- 作者：Jinxin Ai, Matthias Niessner
- 出版日期：2026-10-27T11:11:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37036) / [PDF](https://arxiv.org/pdf/2610.37036)

### 一句话总结
GraftRay 提出一种统一方法，将网格对象以物理一致的方式插入由 2DGS/3DGS 表示的室内场景中，通过显式建模空间扩展光源并联用路径追踪，实现视角一致的着色、互反射与软阴影。

### 研究问题
将虚拟物体插入通过 2D 或 3D Gaussian Splatting 重建的场景，是内容创作、AR 和合成数据生成的关键能力。真实感插入要求物体被场景光照并反之在场景上投射物理合理的阴影。现有方法要么在图像空间协调外观而牺牲多视角一致性，要么用插入点处的环境贴图近似场景光照，无法表示窗户、灯具等主导室内照明的近场面光源。

### 核心思路/方法
- 面向由 2D 或 3D Gaussians 表示的室内场景，实现网格对象的物理一致插入。
- 利用扩散先验恢复场景材质与表面法线。
- 显式建模空间扩展发光体，并以闭式解求解其辐射亮度。
- 采用混合渲染器，对场景 Gaussians 与插入网格进行联合路径追踪，产生视角一致的着色、互反射与软阴影。

### 主要贡献
- 提出 GraftRay，一种将网格对象物理一致地插入 2D/3D Gaussian 室内场景的统一方法。
- 通过扩散先验恢复材质与法线，并显式建模空间扩展光源、闭式求解其辐射亮度，以弥补环境贴图无法表示近场面光源的不足。
- 混合渲染器联合路径追踪场景 Gaussians 与插入网格，生成视角一致着色、互反射和软阴影。
- 在 FIPT 上取得新的 state of the art，在渲染保真度与阴影准确性上优于 ComGS、EAG-PT 等近期基线，同时保持很有竞争力的渲染效率。

### 局限性
摘要未提供足够信息。摘要未给出方法的具体失败情形、适用场景边界、计算开销数值或对非室内场景的泛化表现等细节。

### 阅读优先级
中。理由：该工作针对 Gaussian Splatting 场景中物理一致插入这一明确且实用的问题，提出显式近场面光源建模与联合路径追踪的方案，并在 FIPT 上报告了优于 ComGS、EAG-PT 的结果；但摘要未提供实验规模、定量指标、效率数据和局限分析，是否值得深入阅读需结合全文的实验细节与自身对 Gaussian Splatting 编辑/渲染方向的兴趣判断。

</details>

<details>
<summary>Abstract</summary>

Inserting virtual objects into scenes reconstructed via 2D or 3D Gaussian Splatting (2DGS/3DGS) is a key capability for content creation, AR, and synthetic data generation. However, realistic insertion requires the object to be seamlessly lit by the scene and, conversely, to cast physically plausible shadows onto it. Existing approaches either harmonize appearance in image space, sacrificing multi-view consistency, or approximate scene illumination with an environment map at the insertion point, which cannot represent near-field area lights such as windows and lamps that dominate indoor lighting. To address this, we present GraftRay, a unified method for physically consistent insertion of mesh objects into indoor scenes represented by either 2D or 3D Gaussians. We recover scene materials and surface normals with diffusion-based priors, and explicitly model spatially-extended emitters, solving their radiance in closed form. A hybrid renderer then jointly path-traces the scene Gaussians and inserted meshes, producing view-consistent shading, interreflections, and soft shadows. On FIPT, GraftRay sets a new state of the art, outperforming recent baselines such as ComGS and EAG-PT in rendering fidelity and shadow accuracy, while maintaining highly competitive rendering efficiency.

</details>

#### 2026-10-27 - GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting

**Authors:** Jiale Wang, Chen Zhao, Haoyang Zhang, Yanhao Wu, Fei He, Yanhu Shan, Rui Wu, Wei Ke, Tong Zhang
**Links:** [abs](https://arxiv.org/abs/2610.36760) - [pdf](https://arxiv.org/pdf/2610.36760)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting
- 作者：Jiale Wang, Chen Zhao, Haoyang Zhang, Yanhao Wu, Fei He, Yanhu Shan, Rui Wu, Wei Ke, Tong Zhang
- 出版日期：2026-10-27T07:15:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2610.36760 ；PDF 链接 https://arxiv.org/pdf/2610.36760 ；项目页 https://comedy0913.github.io/projects/geogsplat

### 一句话总结
GeoGSplat 是一种几何先验驱动的非像素对齐前馈高斯泼溅模型，通过显式引入几何约束来缓解非像素对齐方法中高斯中心错位和大幅视角变化下的渲染伪影问题。

### 研究问题
论文关注前馈高斯泼溅中的两个问题：一是像素对齐预测会使高斯基元数量随图像分辨率和视角数量增长，带来冗余和计算成本上升；二是非像素对齐方法虽能预测固定数量的高斯，但在缺乏显式射线和深度约束时，高斯中心位置不准确，导致在大视角变化下出现渲染伪影。论文旨在保持非像素对齐框架低冗余优势的同时，提升几何准确性和新视角合成质量。

### 核心思路/方法
GeoGSplat 在非像素对齐框架中显式加入几何先验。方法包含双分支编码器：分别构建 Anchors 和 Triplane，用于捕获粗略 3D 结构和细粒度场景特征。随后使用分层解码器逐步解码密集 3D 点和高斯基元，从而同时支持 3D 重建和新视角合成。

### 主要贡献
- 提出 GeoGSplat，将几何先验显式融入非像素对齐前馈高斯泼溅框架。
- 设计双分支编码器，通过 Anchors 和 Triplane 分别建模粗略 3D 结构与细粒度场景特征。
- 采用分层解码器逐步解码密集 3D 点与高斯基元，用于重建和新视角合成。
- 摘要称其在 DTU 和 NRGBD 上的新视角合成与重建性能超过像素对齐和非像素对齐的先进高斯泼溅方法；并指出当目标视角远离输入相机时优势更明显，表现出对大幅视角变化更强的泛化能力。

### 局限性
摘要未提供足够信息说明计算开销、推理速度、内存占用、训练数据规模、对不同场景类型的泛化边界或失败案例。摘要未提供足够信息说明方法在动态场景、极端稀疏视角或更复杂真实场景中的表现。

### 阅读优先级
高。理由：论文针对前馈高斯泼溅中“非像素对齐但几何不准确”的关键矛盾提出明确方法，且摘要声明在 DTU 和 NRGBD 上同时优于像素对齐与非像素对齐方法，并强调大视角变化下的泛化优势；这些信息对关注神经场景表示、前馈重建与新视角合成的研究者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Feed-forward Gaussian Splatting enables efficient novel view synthesis, but pixel-aligned prediction makes the primitive count grow with image resolution and view count, leading to substantial redundancy and increased computational cost. Non-pixel-aligned methods address this limitation by predicting a fixed number of Gaussians. Without explicit ray and depth constraints, these methods yield misplaced Gaussian centers, causing rendering artifacts under large viewpoint changes. To address this issue, we introduce GeoGSplat, a geometry-grounded feed-forward model that explicitly incorporates geometric priors into the non-pixel-aligned framework. A dual-branch encoder constructs Anchors and Triplane to capture coarse 3D structure and fine-grained scene features, respectively. Subsequently, a hierarchical decoder progressively decodes dense 3D points and Gaussian primitives, enabling 3D reconstruction and novel view synthesis. GeoGSplat surpasses both state-of-the-art pixel-aligned and non-pixel-aligned Gaussian Splatting methods on DTU and NRGBD in terms of novel view synthesis and reconstruction. The advantage of our geometry-grounded paradigm further increases as target viewpoints move farther from the input cameras, demonstrating stronger generalization to large viewpoint changes. Project Page: https://comedy0913.github.io/projects/geogsplat

</details>

#### 2026-10-27 - ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting

**Authors:** Jaesung Lee, Hyeontaek Hwang, Gabriel Manalu, Daeyoung Kim
**Links:** [abs](https://arxiv.org/abs/2610.36462) - [pdf](https://arxiv.org/pdf/2610.36462)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting
- 作者：Jaesung Lee, Hyeontaek Hwang, Gabriel Manalu, Daeyoung Kim
- 出版日期：2026-10-27T01:12:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.36462 ；PDF https://arxiv.org/pdf/2610.36462 ；项目页 https://jaesung8.github.io/clustersplat/

### 一句话总结
ClusterSplat 将 3D Gaussian Splatting 中的 3D 视觉定位从“对稠密基元相关性分数做启发式阈值/比例筛选”改为“在场景自适应簇候选上做簇级选择”，并让被选簇同时定义显式 3D 目标与渲染 2D 掩码。

### 研究问题
论文研究 3D Gaussian Splatting（3DGS）中的 3D 视觉定位：给定指代表达，需要同时输出渲染的 2D 掩码和一组显式 3D Gaussians 作为目标对象。摘要指出，现有方法通常对稠密基元级相关性分数施加启发式阈值或 top-ratio 过滤来提取 3D 目标；但这些分数在不同场景和提示之间常显著变化，使启发式筛选敏感且导致定位不稳定。

### 核心思路/方法
- 将 3D 目标选择重新表述为：在场景自适应候选上进行簇级选择，而非依赖基元级分数阈值。
- 学习实例感知的 Gaussian 特征。
- 形成特征感知的种子体素。
- 当描述长度准则下降时，合并相邻种子体素，从而生成场景特定的簇候选集合。
- 给定指代表达，使用轻量 MLP 作为查询条件化的簇评分器，对簇候选排序。
- 被选中的簇直接定义显式 3D 目标；其簇分数用于渲染 2D 掩码。
- 摘要报告的评测包括 ScanRefer、Ref-LERF 和 ScanNet v2 类名查询；具体实验设置、训练细节和消融结果摘要未提供足够信息。

### 主要贡献
- 提出 ClusterSplat，将 3DGS 中的 3D 视觉定位目标选择从基元级启发式筛选转为簇级选择。
- 设计场景自适应簇候选构建流程：实例感知 Gaussian 特征、特征感知种子体素、基于描述长度准则的相邻种子体素合并。
- 使用查询条件化的轻量 MLP 簇评分器排序候选，并统一支持显式 3D 目标与 2D 掩码渲染。
- 摘要声称在 ScanRefer 上，相比所比较的 3DGS 基线，取得最佳渲染 2D 分割和显式 3D 目标指标；在 Ref-LERF 上取得最佳平均分数；在 ScanNet v2 类名查询上取得最强渲染 2D 结果和最高 3D 匹配准确率，同时保持有竞争力的 3D IoU。具体数值和对比基线列表摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明计算开销、推理延迟或簇候选构建的复杂度。
- 摘要未提供足够信息说明对描述长度准则的敏感性、超参数选择及失败案例分析。
- 摘要未提供足够信息说明训练数据规模、监督形式、模型泛化到未见场景或开放词汇设置的表现。
- 摘要未提供足够信息说明与更多非 3DGS 方法或更强基线的系统比较。
- 摘要未提供足够信息说明 2D 掩码与显式 3D 目标之间一致性误差的定量分析。

### 阅读优先级
高。理由：该论文直接针对 3DGS 中 3D 视觉定位的稳定性问题，提出明确的簇级选择范式，并在摘要中报告了 ScanRefer、Ref-LERF 和 ScanNet v2 类名查询上的多类指标优势；若关注 3DGS 场景理解、指代定位或 2D-3D 一致目标选择，该工作具有较强相关性。但摘要未给出实验细节和数值，需阅读全文核实贡献强度。

</details>

<details>
<summary>Abstract</summary>

We study 3D visual grounding in 3D Gaussian Splatting (3DGS), where a referring expression should identify a target object as both a rendered 2D mask and a set of explicit 3D Gaussians. Prior methods typically extract 3D targets by applying heuristic thresholding or top-ratio filtering to dense primitive-level relevance scores. However, these scores often vary substantially across scenes and prompts, making such heuristics sensitive and leading to unstable targeting. ClusterSplat addresses this by reframing 3D target selection as cluster-level selection over scene-adaptive candidates. The method first learns instance-aware Gaussian features, forms feature-aware seed voxels, and merges neighboring seed voxels when a description-length criterion decreases, producing a scene-specific set of cluster candidates. Given a referring expression, a query-conditioned cluster scorer ranks the cluster candidates with a lightweight MLP, and the selected cluster directly defines the explicit 3D target while its cluster score is rendered for the 2D mask. On ScanRefer, ClusterSplat achieves the best rendered 2D segmentation and explicit 3D target metrics among the compared 3DGS baselines. It also obtains the best average Ref-LERF scores, supporting the same trend under fine-grained referring descriptions. On ScanNet v2 class name queries, ClusterSplat achieves the strongest rendered 2D results and the highest 3D matching accuracy, while maintaining competitive 3D IoU. Our project page is available at https://jaesung8.github.io/clustersplat/ .

</details>

#### 2026-10-26 - SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation

**Authors:** Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou
**Links:** [abs](https://arxiv.org/abs/2610.36312) - [pdf](https://arxiv.org/pdf/2610.36312)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation
- 作者：Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou
- 出版日期：2026-10-26T21:34:06Z
- 分类：Neural Scene Representations & Rendering（主分类）；3D Reconstruction & Multi-view Geometry（次分类）
- 链接：[摘要](https://arxiv.org/abs/2610.36312)｜[PDF](https://arxiv.org/pdf/2610.36312)

### 一句话总结
SG^2SLAM 针对单目户外导航，将流式空间几何与光线条件化的 3D Gaussian Splatting 内核结合，以块级度量先验替代逐帧跨维对应，联合优化空间几何与位姿，从而提升跟踪与建图的一致性。

### 研究问题
摘要指出，单目户外导航需要稳健的相机运动估计与稠密、可导航地图；3D Gaussian Splatting SLAM 通过显式可微参数化与闭式投影服务于该任务。但通常几何重建依赖 2D 像素与 3D 点的关联，模块化 SLAM 系统会把跟踪误差吸收进地图，导致级联退化。论文即针对这一误差传播与几何—位姿一致性问题展开。

### 核心思路/方法
- 提出 SG^2SLAM，将**流式空间几何**与**光线条件化的 3DGS 内核**耦合。
- **流式空间几何**：用块级度量先验替代逐帧跨维对应，由同一来源监督跟踪与建图。
- **光线条件化内核**：为每个基元扩展一个视角方向子空间，以感知单目相机视角。
- **联合优化**：对空间几何与位姿进行联合优化，以获得全局一致的地图与轨迹结果。
- 摘要称在 KITTI 与 Waymo Open 数据集上，该方法在单目户外导航任务中优于逐帧关联基线。

### 主要贡献
1. 提出 SG^2SLAM，面向单目户外导航的 3D Gaussian Splatting SLAM 框架。
2. 引入流式空间几何，以块级度量先验统一监督跟踪与建图，替代逐帧跨维对应。
3. 设计光线条件化 3DGS 内核，为基元增加视角方向子空间以感知单目相机视角。
4. 通过空间几何与位姿的联合优化提升地图与轨迹的全局一致性。
5. 在 KITTI 与 Waymo Open 上报告优于逐帧关联基线的结果；代码将在接收后公开。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性、内存占用与大规模场景可扩展性。
- 摘要未提供足够信息说明失败模式、对极端光照/动态物体/无纹理区域的鲁棒性。
- 摘要未提供足够信息说明与更多 SLAM 或 3DGS 基线方法的完整定量对比与消融细节。
- 摘要未提供足够信息说明块级度量先验的块大小选择、超参数敏感性及跨数据集泛化边界。

### 阅读优先级
**中**。理由：论文主题聚焦单目户外导航中的 3DGS SLAM 与几何—位姿一致性问题，问题定义清晰，且涉及 KITTI、Waymo Open 上的验证；但摘要仅给出方法要点与相对基线的结论，未提供足够的定量结果、消融与实时性信息。若读者关注 3DGS SLAM、单目户外建图或几何先验监督，可列为中高关注；若需要立即判断工程可用性，则需等待全文与代码。

</details>

<details>
<summary>Abstract</summary>

Monocular outdoor navigation requires robust camera motion estimation and a dense, navigable map, where 3D Gaussian Splatting SLAM serves this task through an explicit differentiable parameterization and closed-form projection. However, typically, the geometry is recovered by associating 2D pixels with 3D points, so a modular SLAM system absorbs tracking error into the map, leading to cascading degradation. To address these gaps, we present SG^2SLAM, which couples streaming spatial geometry with a ray-conditioned 3DGS kernel. Streaming spatial geometry replaces the per- frame cross-dimensional correspondence with a chunk-level metric prior that supervises tracking and mapping from one source. A ray-conditioned kernel extends each primitive with a viewing-direction subspace that senses the monocular camera viewpoints. The joint optimization over spatial geometry and poses ensures a globally consistent map and trajectory outcome. Experiments on the KITTI and Waymo Open datasets show that our SG^2SLAM surpasses the per-frame association baselines in the monocular outdoor navigation task. Code will be made publicly available upon acceptance.

</details>

#### 2026-10-26 - PrinGS: Privacy Preservation in Gaussian Splatting

**Authors:** Gaurav Behera, Abhinav Raundhal, Archisha Panda, Saumya Balina, Gargi Shroff, Ponnurangam Kumaraguru
**Links:** [abs](https://arxiv.org/abs/2610.36168) - [pdf](https://arxiv.org/pdf/2610.36168)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PrinGS: Privacy Preservation in Gaussian Splatting
- 作者：Gaurav Behera, Abhinav Raundhal, Archisha Panda, Saumya Balina, Gargi Shroff, Ponnurangam Kumaraguru
- 出版日期：2026-10-26T19:02:22Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.36168

### 一句话总结
该论文提出 PrinGS，通过表示层面的匿名化框架，在训练后的 3D Gaussian Splatting 表示中定位并匿名化敏感区域，并扩展出隐私保护训练策略，以避免敏感内容在优化过程中被嵌入表示。

### 研究问题
3D Gaussian Splatting 已成为高保真新视角合成与三维场景重建的常用表示，但其学习到的表示会编码人脸、车牌、文档和电脑屏幕等敏感视觉信息；当训练好的 splat 被共享或部署时，会带来隐私风险。论文关注的问题是：如何在 Gaussian Splatting 表示层面实现隐私保护，使敏感信息不出现在后续渲染的新视角中，同时保持整体场景几何与视觉保真度。摘要指出，这是一个尚未被充分探索的问题。

### 核心思路/方法
论文提出一个表示层面的匿名化框架，直接对已训练好的 splat 进行匿名化。给定一个训练好的 splat 和一张用户提供的、用于标识敏感内容的参考视图，方法在底层三维表示中定位对应区域并直接匿名化这些区域，从而确保敏感信息不会出现在后续渲染的新视角中，同时保留整体场景几何和视觉保真度。摘要称这种训练后匿名化可在不到 1 秒内完成。

此外，论文将该框架扩展为一种“隐私设计”训练策略，在优化过程中阻止敏感内容被嵌入表示，从而能够直接从训练图像生成隐私保护 splat。

### 主要贡献
1. 针对 Gaussian Splatting 中尚未被充分探索的隐私保护问题，提出表示层面的匿名化框架，可直接匿名化训练好的 splat。
2. 方法基于用户提供的参考视图定位敏感内容，并在底层三维表示中直接匿名化对应区域，使敏感信息在后续新视角渲染中缺失，同时保持场景几何与视觉保真度。
3. 实现快速训练后匿名化，摘要称耗时少于 1 秒。
4. 扩展出隐私设计训练策略，防止敏感内容在优化过程中被嵌入表示，从而直接从训练图像生成隐私保护 splat。
5. 摘要报告的量化结果包括：Face Similarity Measure（FSM）低至 9.79%，在保留 Face Detection Rate（FDR）为 39.47% 的情况下；敏感文本完全不可读，OCR Character Error Rate 为 1.00。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法对哪些场景类型或敏感内容类别存在失效情况，也未说明计算开销、内存需求、不同数据规模下的表现，以及隐私保护与视觉质量之间的详细权衡。摘要未提供足够信息以判断其泛化能力、对参考视图质量的依赖程度，或与现有隐私保护方法的全面对比。

### 阅读优先级
中。理由：该论文聚焦 3D Gaussian Splatting 的隐私保护这一较新且具有实际部署意义的问题，提出了训练后匿名化与隐私设计训练两种路径，并给出明确的量化隐私指标；但摘要未提供充分的实验设置、对比基线和局限性信息，适合作为了解该方向研究思路的入口，若需评估方法稳健性与通用性，还需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has rapidly become the preferred representation for high-fidelity novel view synthesis and 3D scene reconstruction. However, the learned representation encodes sensitive visual information including human faces, license plates, documents, and computer screens, raising significant privacy concerns when trained splats are shared or deployed. In this work, we address the underexplored problem of privacy preservation in Gaussian Splatting by proposing a representation-level anonymization framework that directly anonymizes a trained splat. Given a trained splat and a user-provided reference view identifying sensitive content, our method localizes the corresponding regions in the underlying 3D representation and directly anonymizes them, ensuring that the sensitive information is absent from all subsequently rendered novel views while preserving the overall scene geometry and visual fidelity. We achieve this post-training anonymization in less than 1 second. Furthermore, we extend our framework with a privacy-by-design training strategy that prevents sensitive content from being embedded into the representation during optimization, enabling the generation of privacy-preserving splats directly from training images. Our method achieves a remarkably low Face Similarity Measure (FSM) of 9.79% at a retained Face Detection Rate (FDR) of 39.47% and makes sensitive text completely unreadable with an OCR Character Error Rate of 1.00. Our work aims to serve as the primary stepping stone towards privacy-aware 3D representations and motivates further research along these directions.

</details>

#### 2026-10-26 - FL4N: Feed-forward Latent Model for 4D Novel View Synthesis

**Authors:** Eunbeen Hong, Hyeonseo Yu, Honggyu An, Jooho Son, Hyunah Ko, Soowon Son, Chaehyun Kim, Jahyeok Koo, Jisoo Kim, Junhwa Hur, Seungryong Kim
**Links:** [abs](https://arxiv.org/abs/2610.35854) - [pdf](https://arxiv.org/pdf/2610.35854)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FL4N: Feed-forward Latent Model for 4D Novel View Synthesis
- 作者：Eunbeen Hong, Hyeonseo Yu, Honggyu An, Jooho Son, Hyunah Ko, Soowon Son, Chaehyun Kim, Jahyeok Koo, Jisoo Kim, Junhwa Hur, Seungryong Kim
- 出版日期：2026-10-26T17:58:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.35854) / [PDF](https://arxiv.org/pdf/2610.35854)

### 一句话总结
FL4N 提出首个前馈式隐式 4D 新视角合成模型，将 4D 场景先验编码为跨空间与时间的统一隐式表示，避免显式 4D 基元带来的时序不一致与渲染伪影。

### 研究问题
4D 新视角合成需要同时推断三维结构与时间动态，即在任意视角与时间戳下渲染动态场景。现有单目前馈方法多依赖显式 4D 高斯表示，摘要指出其易出现时序不一致与严重渲染伪影。摘要未提供足够信息说明现有方法的具体失效场景或定量问题。

### 核心思路/方法
- 不依赖显式 4D 基元，而是将 4D 场景先验编码为跨空间与时间的统一隐式表示。
- 核心洞见：在预训练静态隐式先验之上，将时间动态学习为残差，从而在动态训练数据有限时仍能有效建模 4D。
- 引入轻量动态编码器，利用静态场景特征将物体运动与相机视差解耦。
- 仅以图像合成目标训练，摘要称其达到当前最优 4D 新视角合成质量并支持实时渲染。

### 主要贡献
- 提出首个前馈式隐式 4D 新视角合成模型 FL4N。
- 以统一隐式表示替代显式 4D 基元，针对时序不一致与渲染伪影问题。
- 提出“静态先验 + 动态残差”的学习范式，并设计轻量动态编码器解耦物体运动与相机视差。
- 仅用图像合成目标训练即可实时渲染，且隐式表示可泛化到真实视频并解耦视角与时间。
- 摘要未提供足够信息说明具体数据集、评价指标、消融实验与定量对比结果。

### 局限性
- 摘要未提供足够信息说明方法在不同动态复杂度、遮挡或长时序场景下的失效情况。
- 摘要未提供足够信息说明“动态训练数据有限”的具体规模及对性能的影响。
- 摘要未提供足够信息说明实时渲染的分辨率、帧率与硬件条件。
- 摘要未提供足够信息说明与显式 4D 高斯方法在计算开销与内存占用上的对比。

### 阅读优先级
中。理由：该论文面向 4D 动态新视角合成，提出前馈隐式表示与静态先验残差建模思路，并声称实时渲染与真实视频泛化，主题具有参考价值；但摘要未给出数据集、指标、消融与定量结果，需阅读全文才能判断其实际效果与可复现性。

</details>

<details>
<summary>Abstract</summary>

4D novel view synthesis (NVS) aims to render dynamic scenes across viewpoints and timestamps, which requires jointly inferring 3D structure and temporal dynamics. Existing monocular feed-forward methods often rely on explicit 4D Gaussian representations, which are prone to temporal inconsistency and severe rendering artifacts. We present FL4N, the first feed-forward latent 4D NVS model. Instead of relying on explicit 4D primitives, FL4N encodes a 4D scene prior into a unified latent representation across space and time. Our core insight is that learning temporal dynamics as residuals on top of a pretrained static latent prior enables effective 4D modeling with limited dynamic training data. To this end, we introduce a lightweight dynamic encoder that leverages static scene features to disentangle object motion from camera-induced parallax. Trained solely with an image synthesis objective, FL4N achieves state-of-the-art 4D NVS quality while rendering in real time. Its learned latent representation generalizes to real-world videos and disentangles viewpoint from time.

</details>

#### 2026-10-26 - VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion

**Authors:** Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang
**Links:** [abs](https://arxiv.org/abs/2610.35756) - [pdf](https://arxiv.org/pdf/2610.35756)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion
- 作者：Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang
- 出版日期：2026-10-26T17:03:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.35756) | [PDF](https://arxiv.org/pdf/2610.35756)

### 一句话总结
VidEdit3D 将文本引导的 3D 高斯场景编辑重新表述为基于相机轨迹的视频编辑任务，借助预训练视频扩散模型的时空先验提升多视角一致性与结构编辑灵活性，并通过轨迹引导渲染、流对齐视频编辑和区域选择性 3DGS 精化实现编辑传播与背景泄漏抑制。

### 研究问题
摘要指出，现有文本引导 3D 编辑方法（尤其基于 3D Gaussian Splatting 的方法）仍不如 2D 编辑工具灵活。核心矛盾在于：方法难以同时兼顾多视角一致性与允许结构修改；基于图像编辑器的方案在从异常角度观察对象时，也可能难以将预期编辑正确施加到对象上。论文旨在缓解这一权衡问题。

### 核心思路/方法
- 将静态 3D 场景中的相机运动类比为视频中的时间动态，把 3D 场景编辑转化为轨迹驱动的视频编辑任务，以利用预训练 Video Diffusion Models 的时空先验，促进跨视角的语义与结构一致性。
- **Trajectory-Guided Rendering (TGR)**：选择有信息量的关键帧，并构建与 VDM 输入要求对齐的平滑视频片段。
- **Flow-Aligned Video Editing (FAVE)**：一个免训练框架，包含 **Editing Consistency Guidance (ECG)** 机制，将编辑从锚点视角传播到上述视频片段。ECG 在共享潜在状态上对比源图像与编辑后图像条件，并通过调度式源图像增强，在保持原始场景上下文的同时加强对编辑参考的遵循。
- **Region-Selective 3DGS Refinement (RS-GS)**：将几何与外观更新严格限制在目标基元上，以减少背景属性泄漏。

### 主要贡献
- 提出 VidEdit3D 框架，将 3D 场景编辑重构为轨迹式视频编辑任务，并利用视频扩散模型的时空先验增强跨视角一致性。
- 提出 TGR，用于选择关键帧并构建符合 VDM 输入要求的平滑视频片段。
- 提出免训练的 FAVE 框架及 ECG 机制，实现从锚点视角到视频片段的编辑传播，并平衡编辑遵循与原始场景上下文保持。
- 提出 RS-GS，将 3DGS 的几何与外观更新限制在目标基元，减少背景属性泄漏。
- 摘要称实验显示该方法相比基线具有更强的指令对齐和更好的多视角一致性。

### 局限性
- 摘要仅给出方法概述与结论性表述，未提供具体实验设置、数据集、评价指标、定量结果或失败案例分析；这些信息摘要未提供足够信息。
- 摘要未说明方法对视频扩散模型质量的依赖程度、计算开销、编辑类型覆盖范围及极端视角下的具体表现；摘要未提供足够信息。
- 摘要未提供与基线方法的完整对比细节及消融实验信息；摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文面向文本引导 3DGS 编辑中“多视角一致性 vs. 结构修改灵活性”的关键权衡，提出轨迹式视频编辑重构及 TGR、FAVE/ECG、RS-GS 等完整组件，问题定义和方法组合具有较强针对性；若关注 3D 场景编辑、视频扩散先验迁移或 3DGS 精化，值得优先阅读。但摘要未给出定量实验细节，实际效果需进一步查阅全文验证。

</details>

<details>
<summary>Abstract</summary>

Recent advancements in text-guided 3D editing, particularly with 3D Gaussian Splatting (3DGS), have shown promise but still lag behind the flexibility of 2D editing tools. Existing methods face a critical trade-off between preserving multi-view consistency and allowing structural modifications. Image-based editors can also struggle to apply the intended edit to objects viewed from unusual angles. To address these limitations, we introduce VidEdit3D, a framework that reformulates 3D scene editing as a trajectory-based video editing task. By drawing a parallel between camera movement in static 3D scenes and temporal dynamics in video, we leverage the robust spatiotemporal priors of pre-trained Video Diffusion Models (VDMs) to encourage semantic and structural coherence across views. Specifically, we propose Trajectory-Guided Rendering (TGR) to select informative keyframes and construct smooth video clips aligned with VDM input requirements. To propagate edits from an anchor view to these clips, we develop Flow-Aligned Video Editing (FAVE), a training-free framework incorporating an Editing Consistency Guidance (ECG) mechanism. ECG contrasts source and edited image conditions at a shared latent state, using scheduled source-image amplification to strengthen adherence to the edited reference while maintaining original scene context. Finally, we introduce Region-Selective 3DGS Refinement (RS-GS) to strictly confine geometric and appearance updates to target primitives, reducing background attribute leakage. Experiments demonstrate stronger instruction alignment and better multi-view consistency than the baselines.

</details>

#### 2026-10-26 - Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies

**Authors:** Zuoxu Wang, Xiao Liang
**Links:** [abs](https://arxiv.org/abs/2610.35626) - [pdf](https://arxiv.org/pdf/2610.35626)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies
- 作者：Zuoxu Wang, Xiao Liang
- 出版日期：2026-10-26T15:40:03Z
- 分类：主分类为 Neural Scene Representations & Rendering；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.35626 ；PDF https://arxiv.org/pdf/2610.35626

### 一句话总结
论文提出一种基于 3D Gaussian Splatting 的数据生成流程，用机器人对齐位姿渲染腕部相机观测，并为 VLA 策略提供视觉-动作监督；同时加入指令条件化的到达验证器，用于电子废弃物拆解中的精确预接触到达。

### 研究问题
摘要指出，VLA 策略学习面临机器人数据采集效率瓶颈，尤其是需要精确末端执行器定位和相机-动作对齐的任务。电子废弃物拆解场景中，零件密集、外观相似且存在薄、反光或机械结构复杂的部件，完整数字孪生仿真难以获得准确的对象级网格和接触模型。论文聚焦预接触到达阶段，研究如何为腕部相机 VLA 策略适配提供机器人对齐的数据与监督。

### 核心思路/方法
- 使用 3D Gaussian Splatting（3DGS）重建真实工作空间。
- 从机器人对齐位姿渲染多样化的腕部相机观测。
- 将渲染观测与平滑、结构化的到达轨迹配对，形成机器人对齐的视觉-动作监督，用于 VLA 微调。
- 为 VLA 策略增加指令条件化的 reach verifier，用于估计目标接近程度，并在物理交互前提供可靠终止判断。
- 实验场景为主板拆解，目标是在仅使用腕部相机观测、不使用外部侧视相机的条件下实现精确 VLA 到达。

### 主要贡献
- 提出面向腕部相机 VLA 适配的 3DGS 数据生成管线，通过机器人对齐位姿渲染观测并与结构化到达轨迹配对。
- 引入指令条件化的 reach verifier，用于预接触阶段的接近估计与可靠终止。
- 在主主板拆解实验中报告：使用 π0.5 时，1,500 条生成轨迹在三个目标上达到 80.0% 精确到达成功率；相比 150 条遥操作演示的 58.7% 更高，且主动人类采集时间少于 10 分钟（上述数值均来自摘要）。
- 摘要称实验展示了仅依靠腕部相机观测即可实现精确 VLA 到达，无需外部侧视相机。

### 局限性
- 论文聚焦预接触到达，摘要未说明其是否覆盖接触后操作或完整拆解流程。
- 实验主要在主板拆解场景中验证，摘要未提供跨更多任务或对象的泛化结果。
- 摘要未提供 3DGS 重建质量、渲染与真实观测差异、验证器误判率等定量分析。
- 摘要未提供生成轨迹规模、遥操作演示数量与成功率之间更细粒度的消融实验信息。
- 摘要未提供计算成本、训练时间、硬件配置和安全性评估细节。
- 摘要未说明 1,500 条生成轨迹与 150 条遥操作演示在数据采集成本之外的可比条件细节。
- 其他未在摘要中出现的信息：摘要未提供足够信息。

### 阅读优先级
中。理由：论文主题涉及 3DGS 用于机器人数据生成、腕部相机 VLA 与预接触精确到达，和神经场景表示及具身机器人应用均相关；摘要给出了明确的问题动机和量化结果。但若关注完整拆解操作、广泛泛化或详细实验设计，摘要信息不足以判断，需要阅读全文进一步确认。

</details>

<details>
<summary>Abstract</summary>

Efficient robotic data collection remains a major bottleneck for vision-language-action (VLA) policy learning, especially for tasks requiring accurate end-effector positioning and camera-action alignment. This challenge is particularly severe in electronic-waste disassembly, where robots operate in cluttered assemblies of densely packed, visually similar components. Full digital-twin simulation is difficult because many parts are thin, reflective, or mechanically complex, making accurate object-level meshes and contact models difficult to obtain. In this work, we focus on pre-contact reaching and propose a 3D Gaussian Splatting (3DGS)-based data generation pipeline for wrist-camera VLA adaptation. Our method reconstructs the real workspace with 3DGS and renders diverse wrist-camera observations from robot-aligned poses. These observations are paired with smooth, structured reaching trajectories to provide robot-aligned visual-action supervision for VLA fine-tuning. We further augment the VLA policy with an instruction-conditioned reach verifier that estimates target proximity and provides reliable termination before physical interaction. Experiments in motherboard disassembly demonstrate precise VLA-based reaching using wrist-camera observations alone, without an external side-view camera. With $π$0.5, 1,500 generated trajectories achieve 80.0\% precise-reaching success across three targets, compared with 58.7\% using 150 teleoperated demonstrations, while requiring less than 10 minutes of active human capture. Project website: https://001-wang.github.io/PrecisionReach-GS/

</details>

#### 2026-10-26 - Complexity-guided Regularization for Generalizable Human Gaussian Splatting

**Authors:** Gun Ryu, Gi-Mun Um, Won-Sik Cheong, Wonjun Kim
**Links:** [abs](https://arxiv.org/abs/2610.35152) - [pdf](https://arxiv.org/pdf/2610.35152)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Complexity-guided Regularization for Generalizable Human Gaussian Splatting
- 作者：Gun Ryu, Gi-Mun Um, Won-Sik Cheong, Wonjun Kim
- 出版日期：2026-10-26T10:18:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.35152 ；PDF https://arxiv.org/pdf/2610.35152 ；代码与模型 https://github.com/DCVL-3D/CGR-GS_release

### 一句话总结
论文提出一种由复杂度引导的正则化方案，利用基于局部熵的复杂度先验约束高斯放置并引导局部块采样，以改善可泛化人体高斯泼溅在复杂几何与纹理区域的细节重建。

### 研究问题
现有可泛化人体高斯泼溅方法在多视角图像合成未见人体新视角方面已有进展，但仍难以表示人体对象的细粒度细节，而这些细节本身具有较高的几何与纹理复杂度。摘要指出，原因在于以往方法未对高斯放置的密集程度施加约束，导致复杂区域渲染结果常出现模糊。

### 核心思路/方法
论文提出复杂度引导的正则化方案，核心是使用由穿衣人体几何与纹理特征的局部熵计算得到的复杂度先验。该先验用于两方面：一是防止高斯在复杂区域被粗放放置，从而促进对精细结构的忠实重建；二是依据该复杂度先验，主要从复杂区域采样局部块，使模型能够被局部细节充分监督。

### 主要贡献
- 提出复杂度引导的正则化方案，用于可泛化人体高斯泼溅。
- 利用穿衣人体几何与纹理特征的局部熵构造复杂度先验，约束高斯在复杂区域的放置密度，缓解复杂区域渲染模糊。
- 依据复杂度先验从复杂区域优先采样局部块，增强对局部细节的监督。
- 摘要称在基准数据集上取得最先进性能，同时保持可泛化人体高斯泼溅的实时推理速度。
- 公开代码与模型。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、适用范围限制、计算开销细节、对复杂度先验超参数的敏感性，以及在不同数据集或极端人体姿态/遮挡条件下的表现。摘要仅概括性报告基准数据集上的最先进性能和实时推理速度，未给出实验设置、对比方法、指标数值和消融细节。

### 阅读优先级
中。理由：该论文聚焦可泛化人体高斯泼溅中的细节重建与高斯放置约束问题，问题定义清晰，方法思路简洁，且摘要声称保持实时推理并公开代码，适合关注人体新视角合成与高斯泼溅正则化方向的研究者阅读；但摘要未提供定量实验细节与局限性信息，是否构成重要突破需进一步阅读全文验证。

</details>

<details>
<summary>Abstract</summary>

Recent studies on generalizable human Gaussian splatting have achieved the notable progress in synthesizing novel views of unseen human subjects from multi-view images. Despite this progress, existing methods still struggle to represent fine-grained details of human subjects, which inherently involve high geometric and textural complexity. This is because previous methods do not impose a constraint on how densely Gaussians are placed, which often leads to blurry rendering results in complex regions. To address this problem, we propose a complexity-guided regularization scheme. The key idea is to leverage a complexity prior computed via the local entropy in geometric and textural characteristics of a clothed human. This effectively prevents Gaussians from being coarsely placed in complex regions, which facilitates the faithful reconstruction of intricate structures. Furthermore, we sample local patches predominantly from complex regions according to this complexity prior, which allows the model to be sufficiently supervised by local details. Experimental results on benchmark datasets demonstrate that our method delivers state-of-the-art performance while maintaining the real-time inference speed in generalizable human Gaussian splatting. The code and model are publicly available at https://github.com/DCVL-3D/CGR-GS_release.

</details>

#### 2026-10-26 - SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments

**Authors:** Luke Hollis, Tianxing Fan, Heng Yang
**Links:** [abs](https://arxiv.org/abs/2610.34745) - [pdf](https://arxiv.org/pdf/2610.34745)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** photogrammetry, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments
- 作者：Luke Hollis, Tianxing Fan, Heng Yang
- 出版日期：2026-10-26T02:45:35Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.34745) / [PDF](https://arxiv.org/pdf/2610.34745)

### 一句话总结
SceneAgent 是一个智能体流水线，通过基于模拟器的视觉检查与修复，将多种 3D/4D 视觉采集转换为可交互的仿真环境，并支持策略学习。

### 研究问题
视觉采集能提供详细的场景外观，但将其转换为交互式仿真环境时，需要完成物体重建、物理建模以及中间错误的修正；摘要指出这些步骤存在中间错误，SceneAgent 要解决的问题就是如何协调并纠错，完成从采集到仿真环境的转换。

### 核心思路/方法
- 构建一个 agentic pipeline（智能体流水线），通过基于模拟器的视觉检查与修复来协调各步骤。
- 可处理的输入包括：3D Gaussian Splatting (3DGS)、摄影测量、LiDAR 采集、AI 生成的 3DGS 场景，以及动态场景的 4D 视频。
- 流水线组合了物体分割、物理参数估计、部件分解、铰接建模与可变形仿真。
- 为支持策略学习，生成多样化的物体变体（“digital sisters”）和脚本化的演示数据。

### 主要贡献
- 提出 SceneAgent 智能体流水线，将 3D/4D 采集转换为仿真环境，并通过模拟器视觉检查与修复中间错误。
- 在 GraspClutter6D 的杂乱箱体场景中，对于每个具备可评分输出的编码智能体，SceneAgent 均提升了 1 cm 阈值下的 F1；无论是否使用其 skills 均如此。
- 其重建结果优于 SimFoundry：所有智能体配置的 F1 均超过 SimFoundry，最佳为 60.75% 对 6.9%。
- 在 4DCodeBench 的三个动态场景上，将 Gemini 4 Argon 的平均动态 IoU 从 0.86% 提升到 99.09%。
- 进一步展示了多样化的模拟交互，以及初步的策略向真实机器人迁移。

### 局限性
- 摘要未提供足够信息说明方法在各步骤中的具体技术细节与失败条件。
- 摘要未提供足够信息说明真实机器人策略迁移的量化结果、实验规模与评测设置。
- 摘要未提供足够信息说明计算开销、运行时间或对输入采集质量的敏感性。
- 摘要未提供足够信息说明在 GraspClutter6D 与 4DCodeBench 之外的泛化能力。

### 阅读优先级
高。理由：该工作直接面向从真实/生成 3D 与 4D 采集到可交互仿真环境的自动化转换，涉及场景表示、物理建模与机器人策略学习，摘要给出了明确的量化对比（F1 与动态 IoU 的显著提升）和真实机器人迁移的初步验证，与主次分类均高度相关。

</details>

<details>
<summary>Abstract</summary>

Visual captures provide detailed scene appearance, but converting them into interactive simulation environments requires object reconstruction, physical modeling, and correction of intermediate errors. We present SceneAgent, an agentic pipeline that coordinates these steps through simulator-based visual inspection and repair. The pipeline processes 3D Gaussian Splatting (3DGS), photogrammetry, LiDAR captures, AI-generated 3DGS scenes, and 4D videos of dynamic scenes, and combines object segmentation, physical parameter estimation, part decomposition, articulation, and deformable simulation. To support policy learning, SceneAgent generates diverse object variants ("digital sisters") and scripted demonstrations. On a cluttered bin scene from GraspClutter6D, SceneAgent raises F1 at 1 cm for every coding agent with scorable outputs both with and without its skills, and its reconstructions are better than SimFoundry: all agent configurations exceed SimFoundry's F1 score, with a best of 60.75% versus 6.9%. On three dynamic scenes from 4DCodeBench, SceneAgent raises the mean dynamic IoU of Gemini 4 Argon from 0.86% to 99.09%. We further demonstrate diverse simulated interactions and preliminary policy transfer to a real robot.

</details>

#### 2026-10-25 - RIDE-Splat: Reflection Removal for In-the-Wild Driving Environments

**Authors:** Kevin David Hayes, Alex Hanson, Allen Tu, Pranav Asthana, Matthias Zwicker, Tom Goldstein
**Links:** [abs](https://arxiv.org/abs/2610.34632) - [pdf](https://arxiv.org/pdf/2610.34632)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RIDE-Splat: Reflection Removal for In-the-Wild Driving Environments
- 作者：Kevin David Hayes, Alex Hanson, Allen Tu, Pranav Asthana, Matthias Zwicker, Tom Goldstein
- 出版日期：2026-10-25T23:11:47Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.34632) / [PDF](https://arxiv.org/pdf/2610.34632)

### 一句话总结
RIDE-Splat 提出一种从带位姿的真实驾驶视频中去除挡风玻璃反射、重建无反射 3D 场景的两阶段 3D Gaussian Splatting 流程，无需干净图像、反射掩码或预训练网络。

### 研究问题
通过挡风玻璃拍摄的驾驶视频会违反 3D Gaussian Splatting（3DGS）所假设的世界空间一致性：道路场景呈现视差，而车内反射附着于相机。这导致标准 3DGS 将反射内容嵌入重建场景中。论文要解决的是：在没有干净图像、反射掩码和预训练网络条件下，如何从带位姿驾驶视频实现无反射的三维重建。

### 核心思路/方法
- 将世界一致的挡风玻璃透射分配给 3DGS 场景，将主要相机附着反射建模为一张共享的有符号 RGB 图像。
- 采用两阶段训练：
  1. 第一阶段学习 3D 几何与有符号反射图像，该图像同时表示附加辐射和透射衰减；
  2. 第二阶段使用去反射后的训练图像拟合干净的 3DGS 模型。
- 推理时丢弃反射图像，保持标准 3DGS 渲染路径。

### 主要贡献
- 提出 RIDE-Splat 流程，实现无需干净图像、反射掩码或预训练网络的驾驶视频无反射三维重建。
- 将反射建模为相机附着的共享有符号 RGB 图像，并使其与 3DGS 场景中的世界一致透射分离。
- 提出 RIDE-Splat Dataset，摘要称其为首个用于驾驶视频去反射三维重建的基准，包含真实驾驶场景、训练视图中的物理挡风玻璃反射，以及单独采集的无反射评估图像。
- 在 RIDE-Splat Dataset、XLD 和 Wayve 上，摘要称 RIDE-Splat 在全部九项聚合指标上优于 3DGS、DC-Gaussian 和 RobustSplat，PSNR 最高提升 3.59 dB，LPIPS 最高降低 0.0876；在 42 项逐场景比较中取得 38 项最高指标。

### 局限性
摘要未提供足够信息。摘要未说明方法对反射类型、相机运动、训练数据规模或计算成本的适用边界与失效情形。

### 阅读优先级
高。理由：该论文直接针对 3DGS 在真实驾驶视频中的世界空间一致性破坏问题，提出无需额外监督输入的反射分离与两阶段重建方案，并给出新基准与多数据集定量对比；对神经渲染、自动驾驶场景重建和反射去除方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Driving video captured through a windshield violates the world-space consistency assumed by 3D Gaussian Splatting (3DGS): the road scene exhibits parallax while cabin reflections remain attached to the camera, causing standard 3DGS to embed reflected content into the reconstructed scene. We introduce RIDE-Splat, a pipeline for reflection-free 3D reconstruction from posed driving video without clean images, reflection masks, or pretrained networks. RIDE-Splat assigns world-consistent transmission through the windshield to a 3DGS scene and the dominant camera-attached reflection to one shared, signed RGB image. It builds the clean reconstruction in two passes. First, it learns the 3D geometry and the signed reflection image, representing both added radiance and transmission attenuation. Then, it uses the reflection-removed training images to fit a clean 3DGS model. At inference, the reflection image is discarded, preserving the standard 3DGS rendering path. We also introduce the RIDE-Splat Dataset, the first 3D reconstruction benchmark for reflection removal from driving video -- with real driving scenes, physical windshield reflections in training views, and separately captured non-reflective evaluation images. Across the RIDE-Splat Dataset, XLD, and Wayve, RIDE-Splat outperforms 3DGS, DC-Gaussian, and RobustSplat on all nine aggregate metrics, improving PSNR by up to 3.59 dB and reducing LPIPS by up to 0.0876. We achieve the highest metrics in 38 out of 42 per-scene comparisons and removes windshield reflections that remain visible in the baselines while preserving the transmitted scene.

</details>

#### 2026-10-25 - Birth-Death Structural Learning for 3D Gaussian Splatting

**Authors:** Quan Tran Hong, Long Nguyen-Chi, Binh T. Nguyen
**Links:** [abs](https://arxiv.org/abs/2610.34344) - [pdf](https://arxiv.org/pdf/2610.34344)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Birth-Death Structural Learning for 3D Gaussian Splatting
- 作者：Quan Tran Hong, Long Nguyen-Chi, Binh T. Nguyen
- 出版日期：2026-10-25T14:56:56Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.34344)｜[PDF](https://arxiv.org/pdf/2610.34344)

### 一句话总结
论文提出一种基于重建损失一阶变分的“出生—死亡”结构控制分数，用来替代 3DGS 自适应密度控制中的代理启发式信号，指导新高斯点的分配与低价值基元的剪枝。

### 研究问题
3DGS 的质量—效率权衡高度依赖自适应密度控制，但现有克隆、分裂、剪枝规则使用的代理信号（位置梯度、不透明度、图像空间误差）并不能直接回答结构控制的核心问题：应在何处新增高斯点以降低多视角重建损失，以及哪些现有基元可以以最小惩罚被剪除。摘要指出，这些代理信号在实践中有效，但并非直接针对重建损失的结构决策依据。

### 核心思路/方法
论文提出用于 3DGS 的一阶变分出生—死亡控制（first-variation birth-death control）。在每次结构更新时，冻结当前高斯种群，为每个基元附加辅助“质量坐标”，并对多视角损失关于这些坐标求导。作者说明该分数是 Splat Regression Model 一阶变分的坐标，从而为出生—死亡移动提供严格的局部下降替代量：高分高斯被选为出生位置，低分且低不透明度的高斯被选为移除对象。摘要还提到，将该分数集成到 3DGS-MCMC 中。

### 主要贡献
- 提出以重建损失的一阶变分分数替代 3DGS 密度控制中的代理启发式信号，用于出生与死亡的结构决策。
- 给出理论说明：该分数是 Splat Regression Model 一阶变分的坐标，可作为出生—死亡移动的局部下降替代量。
- 摘要称在标准 3DGS 基准上，将该分数集成到 3DGS-MCMC 后取得 state-of-the-art 重建质量，并在紧高斯预算下带来最显著增益。
- 摘要称其结果为“基于梯度的变分度量可作为 3DGS 中代理启发式的原则性替代”提供了有力证据。

### 局限性
摘要未提供足够信息说明计算开销、辅助质量坐标的具体实现细节、实验基准与对比方法的完整列表、紧预算的具体设定、消融实验规模，以及方法在动态场景或非标准场景中的适用性。摘要未提供足够信息。

### 阅读优先级
中。理由：论文主题直接针对 3DGS 自适应密度控制的关键结构问题，且摘要声称在标准基准上取得 state-of-the-art 并在紧预算下增益最大，具有较高相关性；但仅凭摘要无法核验实验细节、计算成本与泛化性，需阅读全文后再判断其实际影响。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become a standard representation for real-time novel-view synthesis. Yet, its quality-efficiency trade-off still relies heavily on adaptive density control. Existing cloning, splitting, and pruning rules use proxy signals, such as position gradients, opacity, and image-space error. Although effective in practice, these signals do not directly answer the structural question behind density control: where should new Gaussians be allocated to reduce the multi-view reconstruction loss, and which existing primitives can be pruned with minimal penalty. To address this, we propose first-variation birth-death control for 3DGS, a principled approach that replaces heuristic structural decisions with a variational score derived from the reconstruction loss. At each structural update, we freeze the current Gaussian population, attach auxiliary mass coordinates to each primitive, and differentiate the multiview loss with respect to these coordinates. We demonstrate that this score is a coordinate of the first variation of the Splat Regression Model, giving a rigorous local descent surrogate for birth-death moves: high-score Gaussians are selected as birth sites, while low-score, low-opacity Gaussians are selected for removal. Across standard 3DGS benchmarks, integrating this score into 3DGS-MCMC yields state-of-the-art reconstruction quality and outperforms existing methods, delivering the most significant gains under tight Gaussian budgets. Ultimately, our work provides compelling evidence that gradient-based variational metrics offer a principled alternative to proxy heuristics in 3DGS.

</details>

#### 2026-10-25 - RacerGS: Residual-Autoregressive Context for 3D Gaussian Splatting Compression

**Authors:** Wenqing Wang, Huimin Zeng, Yun Fu
**Links:** [abs](https://arxiv.org/abs/2610.34263) - [pdf](https://arxiv.org/pdf/2610.34263)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RacerGS: Residual-Autoregressive Context for 3D Gaussian Splatting Compression
- 作者：Wenqing Wang, Huimin Zeng, Yun Fu
- 出版日期：2026-10-25T12:49:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.34263) / [PDF](https://arxiv.org/pdf/2610.34263)

### 一句话总结
RacerGS 是一种面向 3D Gaussian Splatting 的压缩框架，通过哈希投影、FiLM 调制的自回归 GRU 上下文模型及锚点属性残差熵编码，在保持渲染质量的同时显著降低存储规模。

### 研究问题
3D Gaussian Splatting 能实现快速、高质量的新视角渲染，但其参数量大，成为存储和传输的瓶颈。论文关注如何在尽量保持保真度的前提下，显著压缩 3DGS 的存储规模。

### 核心思路/方法
- 设计哈希投影模型，将锚点哈希编码投影为紧凑的上下文特征，以获得紧凑且空间连贯的特征表示。
- 引入 FiLM 调制的自回归 GRU 上下文模型，利用锚点特征组之间的因果依赖，并用循环隐藏状态细化熵模型参数，以提升比特率效率。
- 对量化后的锚点-属性残差，相对于其上下文预测均值进行自适应熵编码，利用空间一致性降低符号熵。

### 主要贡献
- 提出 RacerGS 紧凑 3DGS 压缩框架，在显著降低存储尺寸的同时保持保真度并完成场景重建。
- 设计哈希投影模型生成紧凑、空间连贯的上下文特征。
- 引入 FiLM 调制的自回归 GRU 上下文模型，利用因果依赖和循环隐藏状态改进熵建模。
- 对量化锚点-属性残差进行自适应熵编码，利用空间一致性降低符号熵。
- 摘要称 RacerGS 相对原始 3DGS 实现超过 150 倍压缩，相对 Scaffold-GS 实现 28 倍压缩，并提供可比渲染质量；在五个数据集上的实验表明其在存储缩减和率失真性能上优于先前 3DGS 压缩方法。

### 局限性
- 摘要未提供足够信息说明计算复杂度、编码/解码耗时或内存开销。
- 摘要未提供足够信息说明各模块的消融实验细节与各自增益。
- 摘要未提供足够信息说明五个数据集的具体名称、场景类型及评测协议。
- 摘要未提供足够信息说明失败案例、极端场景表现或对不同 3DGS 变体的泛化性。
- 摘要未提供足够信息说明与更多基线方法的逐项定量对比。

### 阅读优先级
中。理由：该论文聚焦 3DGS 存储与传输瓶颈，压缩幅度声称显著，且方法组合具有明确的技术针对性；但当前仅有摘要信息，缺少实验细节、复杂度与消融结果，适合作为 3DGS 压缩方向的候选跟踪论文，待全文可获取后再决定是否深入研读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as a promising approach for fast, high-quality novel-view rendering. However, its large parameter size remains a bottleneck for storage and transmission. We propose RacerGS, a compact 3DGS compression framework that achieves scene reconstruction at significantly reduced storage sizes with preserved fidelity. To obtain compact and spatially coherent features, we design a hash projection model that projects the anchor hash encodings into compact context features. Additionally, we introduce a FiLM-modulated autoregressive GRU context model that utilizes causal dependencies among anchor feature groups and uses recurrent hidden states to refine entropy-model parameters, improving bitrate efficiency. Furthermore, we adaptively entropy-code quantized anchor-attribute residuals relative to their context-predicted means, leveraging spatial consistency to reduce symbol entropy. Overall, RacerGS achieves more than 150x compression over vanilla 3DGS and 28x over Scaffold-GS, while providing comparable rendering quality. Extensive experiments across five datasets demonstrate that RacerGS outperforms prior 3DGS compression methods in both storage reduction and rate-distortion performance.

</details>

#### 2026-10-25 - ParetoGS: High-Quality Continuous-Budget 3D Gaussian Splatting with Sparse Adapted Anchors

**Authors:** Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu
**Links:** [abs](https://arxiv.org/abs/2610.34235) - [pdf](https://arxiv.org/pdf/2610.34235)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ParetoGS: High-Quality Continuous-Budget 3D Gaussian Splatting with Sparse Adapted Anchors
- 作者：Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu
- 出版日期：2026-10-25T12:05:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.34235) / [PDF](https://arxiv.org/pdf/2610.34235)

### 一句话总结
ParetoGS 通过少量“预算锚点”和残差图谱，把高预算 3D Gaussian Splatting 模型解码为连续预算表示，在减少高斯数量的同时尽量保持渲染质量。

### 研究问题
可扩展 3D Gaussian Splatting 希望用同一场景表示服务不同的 Gaussian 数量预算，但其质量—预算曲线可能落后于针对每个预算单独优化的模型。摘要指出，减少 Gaussian 数量会同时改变被选成员及其承担的重建任务，而直接从高预算模型继承的参数可能不适合低预算表示。

### 核心思路/方法
- 用一小组经过适配的预算锚点描述成员变化与参数演化，并在解码时生成中间预算，而不必对每个请求数量单独优化。
- 交替进行剪枝与固定成员适配，构建具有持久身份标识的嵌套锚点。
- 将各锚点相对完整模型的参数变化编码为紧凑的残差图谱。
- 解码时对共享成员状态进行插值，并逐步引入新成员的渲染贡献，从而把稀疏锚点连接为连续预算表示。

### 主要贡献
- 提出面向连续预算的 ParetoGS 框架，以稀疏适配锚点和残差图谱支持中间预算解码。
- 在 13 个场景上，于各方法自身完整模型 10% 的预算处，以更少 Gaussian 取得更好的平均 PSNR、SSIM 和 LPIPS。
- 从共享完整模型出发，在训练预算 1%、5%、10% 上优于 FlexGS-imp，在 1% 和 0.1% 预算上优于 NanoGS-imp。
- 在 Garden 场景上，非锚点质量在较高保留比例下接近独立优化 GNS 模型的经验参考，并在部分更低预算点超过该参考。
- 编码将 13 个场景的平均额外状态从 390.0 MB 降至 85.7 MB，平均 PSNR 变化为 0.01 dB。

### 局限性
摘要未提供足够信息说明计算开销、训练时间、内存峰值、更多场景或数据集上的泛化表现，也未给出失败案例或方法适用边界。

### 阅读优先级
高。理由：该论文直接针对连续预算 3D Gaussian Splatting 的质量与状态开销问题，摘要给出了多场景定量结果、与近期方法的比较以及明确的压缩收益，适合关注高效神经场景表示与渲染的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Scalable 3D Gaussian Splatting allows one scene representation to serve different Gaussian-count budgets, yet its quality-budget curve may lag behind models optimized separately for each budget. Reducing the number of Gaussians changes both the selected members and the reconstruction tasks carried by the survivors; parameters inherited from a high-budget model may fit a low-budget representation poorly. We propose ParetoGS, which describes member changes and parameter evolution with a small set of adapted budget anchors and decodes intermediate budgets without separate optimization at every requested count. ParetoGS alternates pruning and fixed-member adaptation to build nested anchors with persistent identities, and encodes their parameter changes relative to the full model in a compact residual atlas. At decoding, it interpolates the states of shared members and gradually introduces the rendering contributions of new members, connecting sparse anchors into a continuous-budget representation. Across 13 scenes, ParetoGS attains better average PSNR, SSIM, and LPIPS with fewer Gaussians than the compared prefix methods at 10% of each method's own full model. From a shared full model, it also outperforms FlexGS-imp at its trained 1%, 5%, and 10% budgets and NanoGS-imp at the 1% and 0.1% budgets. On Garden, its non-anchor quality approaches an empirical reference from independently optimized GNS models at higher retention ratios and exceeds it at some lower-budget points. Across 13 scenes, encoding reduces mean additional state from 390.0 to 85.7 MB with an average PSNR change of 0.01 dB. Project page: https://xiaobin2001.github.io/ParetoGS-Web/

</details>

#### 2026-10-25 - BoundedGS: Memory-Efficient High-Resolution Training for 3D Gaussian Splatting

**Authors:** Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu
**Links:** [abs](https://arxiv.org/abs/2610.34233) - [pdf](https://arxiv.org/pdf/2610.34233)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BoundedGS: Memory-Efficient High-Resolution Training for 3D Gaussian Splatting
- 作者：Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu
- 出版日期：2026-10-25T12:00:20Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.34233) / [PDF](https://arxiv.org/pdf/2610.34233) / [项目页](https://xiaobin2001.github.io/BoundedGS-Web/)

### 一句话总结
针对高分辨率 3D Gaussian Splatting 训练中光栅化缓存随像素与高斯-瓦片相交数增长而导致峰值显存膨胀的问题，BoundedGS 通过分离反向传播、限制局部光栅化工作集并压缩梯度与投影存储，在保持重建质量的同时显著降低显存占用。

### 研究问题
高分辨率 3D Gaussian Splatting 训练会提高像素与 Gaussian-tile 的相交计数，使光栅化缓存扩张，并与投影和梯度状态在峰值内存处共存，形成显存压力。论文关注的是：如何在完整视图更新语义下，控制高分辨率训练和渲染过程中的峰值工作集，同时不显著损害重建质量与训练效率。

### 核心思路/方法
- 利用“完整视图更新”的性质：梯度可跨视图聚合，因此每个区域在前向与反向中的缓存可在其贡献被收集后释放。
- 将光栅化与投影的反向传播过程分离，并根据实测负载限制活跃的局部光栅化工作集。
- 采用候选索引的投影表示与紧凑梯度存储，处理该改变所暴露的视图级峰值。
- 在渲染之外，使用 CPU 辅助的结构重建与有界图像供给来管理资源。
- 摘要给出的机制描述集中在显存边界控制、缓存释放与状态压缩；具体实现细节与完整算法流程需参见原文。

### 主要贡献
- 提出 BoundedGS，面向高分辨率 3D Gaussian Splatting 训练的内存高效方法。
- 在约 6M Gaussian 的固定数量下进行分辨率扫描，测得渲染工作集在 1K 到 16K 范围内保持在 1.073–1.077 GiB。
- 在 11K 分辨率下，预热通过耗时 19.79 秒，对比全帧执行的 21.76 秒。
- 在五个原生 5K 室外场景上，完整训练将平均渲染工作集从 9.97 GiB 降至 1.76 GiB（降低 82.3%），保持相近的重建质量，并将训练时间从 36.7 分钟缩短至 33.9 分钟。
- 摘要报告了显存、时间与重建质量方面的结果；更细粒度的消融、不同场景逐项指标与失败案例分析：摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法在非室外场景、不同高斯数量或更高分辨率下的泛化表现。
- 摘要未提供足够信息说明“相近重建质量”的具体量化指标、评价协议与统计显著性。
- 摘要未提供足够信息说明 CPU 辅助结构重建与有界图像供给的开销、硬件依赖及对训练稳定性的影响。
- 摘要未提供足够信息说明与其它显存优化方法的直接对比。
- 摘要未提供足够信息说明代码、数据与复现实验的完整细节。

### 阅读优先级
高。理由：该论文直接针对高分辨率 3D Gaussian Splatting 训练的显存瓶颈，摘要给出了明确的工作集边界、时间与质量保持结果，且涉及反向传播分离、缓存释放与状态压缩等可复用的系统级思路；对关注三维重建训练效率与显存优化的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

High-resolution 3D Gaussian Splatting training increases pixel and Gaussian-tile intersection counts, expanding rasterization caches that coexist with projection and gradient state at peak memory. A complete-view update aggregates gradients across the view; each region's forward and backward caches can be released after its contribution is collected. BoundedGS separates rasterization and projection backward passes and bounds the active local rasterization working set according to its measured load. Candidate-indexed projection and compact gradient storage address the view-level peaks exposed by this change, while CPU-assisted structure rebuilding and bounded image supply manage resources outside rendering. In a resolution sweep at a fixed count of about 6M Gaussians, the measured rendering working set stays within 1.073-1.077 GiB from 1K to 16K; at 11K, a warm pass takes 19.79 seconds versus 21.76 for full-frame execution. Across five native 5K outdoor scenes, full training reduces the mean rendering working set from 9.97 to 1.76 GiB (82.3%), retains similar reconstruction quality, and shortens training time from 36.7 to 33.9 minutes. Project page: https://xiaobin2001.github.io/BoundedGS-Web/

</details>

#### 2026-10-24 - RelateGS: Reliable Semantic and Relational Evidence for 3D Scene Understanding with Gaussian Splatting

**Authors:** Seongjun Choi, Sangyoun Lee
**Links:** [abs](https://arxiv.org/abs/2610.33868) - [pdf](https://arxiv.org/pdf/2610.33868)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RelateGS: Reliable Semantic and Relational Evidence for 3D Scene Understanding with Gaussian Splatting
- 作者：Seongjun Choi, Sangyoun Lee
- 出版日期：2026-10-24T19:20:57Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.33868) / [PDF](https://arxiv.org/pdf/2610.33868)

### 一句话总结
RelateGS 提出一种结构化的语言感知 3D 高斯表示，通过筛选不可靠语义观测并补全观测不足的物体关系证据，提升三维视觉定位中的目标消歧能力。

### 研究问题
语言感知的 3D 高斯泼溅已能将语义与关系线索融入重建场景，但关系感知的定位不仅依赖信息表示，还取决于场景侧证据是否可靠和充分。多视角语义聚合可能引入弱观测；同时，现有相机轨迹下物体关系可能观测不足，导致目标消歧时证据模糊。论文针对这两个证据可靠性问题展开研究。

### 核心思路/方法
- 在语义特征提升过程中抑制不可靠观测。
- 将多视角物体观测整合为持久的三维图结构。
- 利用该图识别观测不足的物体关系，并指导对已有信息帧进行定向重新查询，以补全关系证据。
- 面向三维视觉定位，选择性精炼语义与关系证据。

### 主要贡献
- 提出 RelateGS，一种结构化的语言感知高斯表示，用于选择性精炼三维视觉定位所需的语义和关系证据。
- 针对语义提升中的不可靠观测进行抑制，并通过持久三维图整合多视角物体观测。
- 通过三维图识别观测不足的对象关系，并引导对现有帧的定向重查询以补充证据。
- 在 Sr3D+ 与 Nr3D 上报告了有竞争力的三维定位性能；按摘要，在 Acc@0.25 上分别较此前最佳提升 7.9 和 1.7 个百分点。

### 局限性
摘要未提供足够信息说明方法的具体失效条件、计算开销、对相机轨迹质量的敏感程度，以及在不同数据集或场景类型上的泛化边界。摘要亦未提供消融实验细节与错误案例分析。

### 阅读优先级
高。理由：该工作直接针对语言感知 3DGS 中关系证据可靠性与观测不足问题，问题定义清晰，且摘要报告了在 Sr3D+ 和 Nr3D 上的明确性能提升；同时涉及具身/机器人/AR 应用方向，具有较高的相关性与跟踪价值。

</details>

<details>
<summary>Abstract</summary>

Language-aware 3D Gaussian Splatting (3DGS) has advanced language-driven 3D scene understanding by incorporating semantic and relational cues into reconstructed scenes. However, relation-aware grounding depends not only on representing such information, but also on whether the underlying scene-side evidence is reliable and sufficient. Multi-view semantic aggregation can incorporate weak observations, while object relations can remain under-observed along the available camera trajectory, leading to ambiguous evidence for target disambiguation. We present RelateGS, a structured language-aware Gaussian representation that selectively refines semantic and relational evidence for 3D visual grounding. RelateGS suppresses unreliable observations during semantic feature uplifting and consolidates multi-view object observations into a persistent 3D graph. The graph further identifies under-observed object relations and guides targeted re-querying of informative existing frames to complement their evidence. Experiments on Sr3D+ and Nr3D demonstrate competitive 3D grounding performance, improving the previous best by 7.9 and 1.7 percentage points at Acc@0.25, respectively.

</details>

#### 2026-10-22 - RecallGS: Geometry-Grounded Recall for Online Semantic Gaussian Splatting

**Authors:** Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran
**Links:** [abs](https://arxiv.org/abs/2610.31293) - [pdf](https://arxiv.org/pdf/2610.31293)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RecallGS: Geometry-Grounded Recall for Online Semantic Gaussian Splatting
- 作者：Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran
- 出版日期：2026-10-22T13:55:31Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.31293 ；PDF https://arxiv.org/pdf/2610.31293

### 一句话总结
RecallGS 提出一种轻量、免训练的“召回—几何校验—融合”机制，从智能体历史观测中以非参数方式恢复几何—语义证据，用于在线语义 3D Gaussian Splatting，避免额外学习 3D 网络。

### 研究问题
在线语义 3D Gaussian Splatting（3DGS）可从流式观测中进行开放词汇场景理解。现有方法通常借助额外学习的 3D 网络来恢复图像语义特征中缺失的几何上下文，但会带来额外训练和运行时开销。论文关注的问题是：这类几何—语义证据是否已存在于智能体的观测历史中，能否通过“检索”而非“学习”获得。

### 核心思路/方法
论文观察到几何—语义证据可能已存在于智能体的观测历史中，因此将过去观测视为非参数化的几何—语义先验，提出 RecallGS。其流程为“recall–ground–fuse”：
1. 使用 CLIP 检索相关观测；
2. 利用 alpha 合成权重识别具有几何支撑的视角；
3. 在每个 Gaussian 的渲染覆盖区域上聚合这些视角的语义特征。
该机制被描述为轻量、免训练。

### 主要贡献
- 提出 RecallGS，一种轻量、免训练的机制，将历史观测作为非参数几何—语义先验，用于在线语义 3DGS。
- 设计“召回—几何校验—融合”流程：CLIP 检索、alpha 合成权重筛选几何支撑视角、按 Gaussian 渲染覆盖区域聚合语义特征。
- 在 ScanNet 和 ScanNet++ 上取得较强的语义分割性能，并以 2.48 FPS 运行，表明无需额外学习 3D 分支即可从观测历史中有效恢复几何—语义上下文。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、对检索质量的敏感性、内存或存储开销、与更多基线方法的完整比较，以及 2.48 FPS 对应的硬件配置等细节。

### 阅读优先级
中。理由：该工作针对在线语义 3DGS 中额外学习 3D 网络的开销问题，提出免训练的检索式替代思路，问题明确且方法流程清晰；摘要报告了 ScanNet/ScanNet++ 上的语义分割表现与 2.48 FPS 运行速度。但摘要未提供与现有方法的完整定量对比、消融实验和实现细节，是否值得优先精读需结合全文实验部分进一步判断。

</details>

<details>
<summary>Abstract</summary>

Online semantic 3D Gaussian Splatting (3DGS) enables open-vocabulary scene understanding from streaming observations. However, existing methods recover geometric context missing from image-derived semantic features using an additionally learned 3D network, incurring extra training and runtime overhead. We observe that such geometric-semantic evidence may already exist in the agent's observation history and can be retrieved rather than learned. Based on this insight, we introduce RecallGS (Geometry-Grounded Recall for Online Semantic Gaussian Splatting), a lightweight, training-free mechanism that treats past observations as a non-parametric geometric-semantic prior. RecallGS follows a recall-ground-fuse pipeline: CLIP retrieves relevant observations, alpha-compositing weights identify geometrically supported views, and aggregate their semantic features over each Gaussian's rendered footprint. On ScanNet and ScanNet++, RecallGS achieves strong semantic segmentation performance at 2.48 FPS, demonstrating that geometric-semantic context can be effectively recovered from observation history without an additional learned 3D branch.

</details>

#### 2026-10-22 - GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis

**Authors:** Henglei Lv, Bailin Deng, Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang, Lin Gao
**Links:** [abs](https://arxiv.org/abs/2610.30619) - [pdf](https://arxiv.org/pdf/2610.30619)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, relighting, rendering, radiance, AR, augmented reality, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis
- 作者：Henglei Lv, Bailin Deng, Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang, Lin Gao
- 出版日期：2026-10-22T02:31:54Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.30619 ；PDF https://arxiv.org/pdf/2610.30619 ；项目页 http://www.geometrylearning.com/GSHeadRelight/

### 一句话总结
论文提出 GSHeadRelight，面向 3D Gaussian 人头合成，设计基于统一神经辐射传输表示的光照模型，并借助 in-the-wild 图像实现重光照与更快渲染。

### 研究问题
论文关注人像的重光照与新视角合成，应用场景包括人像摄影、VR 和 AR。摘要指出，3D-aware 人像重光照仍具挑战，原因在于同时需要照片级真实渲染、实时性能和对外观未见过受试者的泛化能力。现有工作要么依赖有限且昂贵的光照棚采集数据做监督，要么结果不理想；不少方法基于生成式 NeRF，存在 3D 一致性差和实时性能低的问题。

### 核心思路/方法
论文利用生成式 3D Gaussian 的进展，设计一个基于统一神经辐射传输表示的光照模型，该表示对入射光呈线性响应。方法仅使用 in-the-wild 图像进行训练或建模，摘要未提供更具体的数据设置与实现细节。

### 主要贡献
- 面向 3D Gaussian 人头合成提出 GSHeadRelight，以提升重光照能力与速度。
- 设计基于统一神经辐射传输表示、对入射光线性响应的光照模型。
- 仅使用 in-the-wild 图像，摘要声称达到当时最优的重光照结果。
- 摘要声称相较此前 3D-aware 人像重光照研究，渲染速度显著更快（×12）。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、泛化边界、数据依赖范围、计算资源需求及定量实验设置；仅在 abstract 中提及不依赖昂贵光照棚监督并使用 in-the-wild 图像，但未展开其限制。

### 阅读优先级
中。理由：论文主题与 3D Gaussian 人头合成、重光照和实时渲染直接相关，摘要给出明确的速度提升与 SOTA 声称，适合关注人像重光照、VR/AR 与神经渲染的读者进一步核查；但摘要未提供实验细节和局限性说明，需阅读全文后再判断结论强度。

</details>

<details>
<summary>Abstract</summary>

Relighting and novel view synthesis of human portraits are essential in applications such as portrait photography, virtual reality (VR), and augmented reality (AR). Despite recent progress, 3D-aware portrait relighting remains challenging due to the demands for photorealistic rendering, real-time performance, and generalization to unseen subjects. Existing works either rely on supervision from limited and expensive light stage captured data or produce suboptimal results. Moreover, many works are based on generative NeRFs, which suffer from poor 3D consistency and low real-time performance. We resort to recent progress on generative 3D Gaussians and design a lighting model based on a unified neural radiance transfer representation, which responds linearly to incident light. Using only in-the-wild images, our method achieves state-of-the-art relighting results and a significantly faster rendering speed ($\times12$) compared to previous 3D-aware portrait relighting research. Project page: http://www.geometrylearning.com/GSHeadRelight/.

</details>

#### 2026-10-21 - SplatLab: Autonomous Scientific Discovery for 3DGS Research

**Authors:** Seemandhar Jain, Manmohan Chandraker
**Links:** [abs](https://arxiv.org/abs/2610.30468) - [pdf](https://arxiv.org/pdf/2610.30468)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatLab: Autonomous Scientific Discovery for 3DGS Research
- 作者：Seemandhar Jain, Manmohan Chandraker
- 出版日期：2026-10-21T21:30:32Z
- 分类：主分类 Neural Scene Representations & Rendering；次级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.30468 ；PDF https://arxiv.org/pdf/2610.30468

### 一句话总结
SplatLab 是面向 3D Gaussian Splatting 的自主研究系统，可在给定研究提示、目标论文链接或无输入的情况下，复现基线、提出扩展、训练与消融、撰写论文，并把每个报告数值绑定到已记录的训练运行。

### 研究问题
摘要指出，复现一篇已发表的 3DGS 论文需要数周专家工程工作，之后才能提出扩展；既有自主研究系统受限于短固定模板、低可执行性和弱可追溯性，且尚未在活跃的计算机视觉子领域中端到端展示。SplatLab 旨在解决这些限制。

### 核心思路/方法
摘要给出五个设计选择：
1. 候选方法从“已验证复现的骨架”出发，以插件形式变异，并与已发表基线匹配；
2. 在八个“岛”上运行级联加权 Elo 锦标赛，用实测 GPU PSNR 评分候选，并结合语言梯度反馈；
3. 设置常驻“证伪器”，失败时扣减 Elo，把压力测试存活情况纳入选择；
4. 每个报告数值绑定到已记录训练运行，且只要存在未支撑的主张，运行就不能终止；
5. 用七类 3DGS 分类法将 EVOLVE-BLOCK 标记包裹在领域对齐脚手架中，可跨 3DGS 仓库迁移。

系统流程包括：复现已发表基线、提出扩展、在 Mip-NeRF 360 和 LLFF 上训练与消融、撰写手稿、绑定数值到训练日志。

### 主要贡献
- 提出面向 3DGS 的自主研究系统 SplatLab，覆盖复现、扩展、训练、消融、写作与数值追溯的端到端流程。
- 给出五项设计选择：插件式候选变异、级联加权 Elo 锦标赛、常驻证伪器、数值与训练运行绑定、七类 3DGS 分类法脚手架。
- 在 PSNR 目标运行中，摘要称其手稿相对复现目标提升 +0.18 至 +3.78 dB，其中包括天体摄影星云渲染的 +3.78 dB，并称此前不存在该任务的 3DGS 方法。
- 摘要称研究周期从数月研究生时间压缩到数天、以自主计算为主；代码、手稿、实验账本和跨运行论文库见项目页。

### 局限性
摘要未提供足够信息说明以下内容：实验的完整设置与统计显著性、与其他人自主研究系统的定量对比、失败案例与适用范围、人工干预程度、计算资源开销、跨仓库分类法脚手架的泛化验证细节、LLFF 与 Mip-NeRF 360 上的逐项结果，以及“无输入”模式的具体表现。摘要仅给出 PSNR 目标运行的总体提升区间和一个星云渲染案例，未提供完整实验细节。

### 阅读优先级
中。理由：该工作涉及 3DGS 与自主科研系统交叉，摘要提供了较清晰的方法框架和可追溯性设计，并对活跃视觉子领域做端到端演示；但摘要未给出完整实验细节、对比基线和失败分析，是否值得深入阅读取决于读者对自主研究流程、3DGS 自动化实验或数值可追溯机制的关注程度。

</details>

<details>
<summary>Abstract</summary>

Reproducing a published 3DGS paper takes weeks of expert engineering before any extension can be proposed. Prior autonomous-research systems read papers, draft hypotheses, and write code, but are limited by short fixed templates, low executability, and weak traceability, and none has been demonstrated end-to-end in a live computer-vision subfield with intense activity. SplatLab is an autonomous research system for 3D Gaussian Splatting that addresses these limitations. Given a research prompt, a target-paper URL, or no input at all, it reproduces a published baseline, proposes an extension, trains and ablates across Mip-NeRF 360 and LLFF, writes the manuscript, and binds every reported number to a logged training run. Five design choices distinguish it: (i) candidates mutate plugins from a verified-reproduction backbone matched to published baselines; (ii) a cascade-weighted Elo tournament across eight islands scores candidates on measured GPU PSNR with verbal-gradient feedback; (iii) a standing falsifier subtracts Elo on failure, integrating stress-test survival into selection; (iv) every reported number is bound to a logged training run, and the run cannot terminate while any claim is unbacked; (v) a seven-category 3DGS taxonomy wraps EVOLVE-BLOCK markers in domain-aligned scaffolds transferable across 3DGS repositories. On PSNR-targeted runs, SplatLab's manuscripts beat their reproduced targets by +0.18 to +3.78 dB, including +3.78 dB on astrophotographic nebula rendering, for which no prior 3DGS method exists. The research cycle compresses from months of graduate-student time to days of mostly autonomous compute. Code, all manuscripts, experiment ledgers, and the cross-run paper store are available on the project page.

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-27 - Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation

**Authors:** Dequan Ou, Austin Lopez, Quentin Missinne, Christophe De Wagter, Guido C. H. E. de Croon
**Links:** [abs](https://arxiv.org/abs/2610.37543) - [pdf](https://arxiv.org/pdf/2610.37543)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** rendering, robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation
- 作者：Dequan Ou, Austin Lopez, Quentin Missinne, Christophe De Wagter, Guido C. H. E. de Croon
- 出版日期：2026-10-27T16:56:18Z
- 分类：Embodied / Robotics / AR Applications；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.37543) / [PDF](https://arxiv.org/pdf/2610.37543)

### 一句话总结
论文提出一种无需图像渲染、直接从场景几何与自运动合成事件流的解析事件模拟器，用于加速事件相机自主机器人导航的强化学习训练，并验证了策略在仿真和真实小型无人机上的迁移与部署。

### 研究问题
现有事件相机仿真器通常先渲染照片级图像再转换为事件，导致大规模强化学习训练非常慢。论文关注的问题是：能否绕开视觉渲染，直接根据事件相机本质上测量的运动对比边缘来合成事件流，从而显著加速事件相机导航策略的端到端强化学习训练，并实现真实机器人部署。

### 核心思路/方法
论文提出解析事件模拟器，利用事件相机 fundamentally 测量“运动对比边缘”这一特性，直接从场景几何和自运动合成事件流，而不进行视觉渲染。该模拟器在单 GPU 上生成 64x64 事件观测仅需 17 微秒，摘要称其比最先进的渲染管线快 400 倍以上。基于该模拟器，论文进行目标导向避障的端到端强化学习训练，使训练在 30 分钟内收敛。策略还被量化为 1.2 MB 的 int8 网络，并部署在搭载 Prophesee GenX320 事件相机和 OpenMV N6 微控制器板的 56 克 Crazyflie 上。

### 主要贡献
- 提出一种无需渲染的解析事件模拟器，直接从场景几何与自运动合成事件流。
- 该模拟器生成 64x64 事件观测耗时 17 微秒，摘要称比最先进渲染管线快 400 倍以上。
- 使目标导向避障的端到端强化学习在 30 分钟内收敛，摘要称比在渲染事件上训练快三个数量级。
- 策略零样本迁移到基于物理的事件仿真（ray-traced Isaac Sim）。
- 在训练中未见的杂乱赛道中达到 83% 成功率（中等难度，可通行概率约 0.57），平均目标速度 2.4 m/s；在模拟纹理密集室内大厅中保持 70% 成功率。
- 将策略量化为 1.2 MB int8 网络，完全机载运行于 56 克 Crazyflie；无需微调、外部处理或定位，在三条难度递增的真实障碍赛道中平均成功率为 82%（5/5、5/6、4/6 次飞行）。

### 局限性
- 摘要未提供足够信息说明模拟器对复杂光照、运动模糊、噪声模型或非理想事件相机特性的覆盖程度。
- 摘要未提供足够信息说明真实实验的完整统计显著性、失败模式分析或更广泛环境下的泛化边界。
- 摘要未提供足够信息说明训练所用场景分布、奖励设计细节及与其他强化学习方法的系统对比。
- 摘要未提供足够信息说明机载计算功耗、延迟分布及长期运行稳定性。

### 阅读优先级
高。理由：论文直击事件相机仿真训练慢这一关键瓶颈，提出无需渲染的解析事件模拟器，并给出从训练加速、零样本仿真迁移到 56 克 Crazyflie 机载真实飞行的完整验证链条；对事件相机机器人导航与高效强化学习训练具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Event cameras offer low latency, high dynamic range, and milliwatt-level power consumption, making them ideal for agile robots such as tiny drones navigating through cluttered environments. However, existing simulators generally render photorealistic images before converting them into events, making large-scale reinforcement learning prohibitively slow. We propose an analytic event simulator that exploits what event cameras fundamentally measure - moving contrast edges - to synthesize event streams directly from scene geometry and ego-motion without visual rendering. Our simulator generates a 64x64 event observation in 17 microseconds on a single GPU - over 400x faster than a state-of-the-art rendering pipeline - enabling end-to-end reinforcement learning for goal-directed obstacle avoidance to converge in under 30 minutes - three orders of magnitude faster than training on rendered events. Policies transfer zero-shot to physically based event simulations (ray-traced Isaac Sim). Our policy reaches 83% success in cluttered courses unseen during training (mid-difficulty, traversability probability approx. 0.57), at 2.4 m/s average goal velocity, and retains 70% in a simulated texture-dense indoor hall. Furthermore, we quantized the policy to a 1.2 MB int8 network running fully onboard a 56-gram Crazyflie equipped with a Prophesee GenX320 event camera and an OpenMV N6 microcontroller board. Without any fine-tuning, external processing, or positioning, the policy achieves an average success rate of 82% (5/5, 5/6, 4/6 flights) across three real-world obstacle courses of increasing difficulty. Code: https://github.com/tudelft/rendering-free-event-nav

</details>

#### 2026-10-27 - GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation

**Authors:** Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu, Xiang Gao
**Links:** [abs](https://arxiv.org/abs/2610.37091) - [pdf](https://arxiv.org/pdf/2610.37091)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation
- 作者：Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu, Xiang Gao
- 出版日期：2026-10-27T11:55:31Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.37091)｜[PDF](https://arxiv.org/pdf/2610.37091)

### 一句话总结
GAWM 是一个参数少于 1 亿、无需机器人或视频预训练的紧凑多任务世界-动作模型，在冻结 DINOv3 编码器的潜空间中预测未来观测，并在多个基准和真机任务上取得与十亿参数级模型可比或更优的表现。

### 研究问题
现有世界-动作模型（WAMs）大多依赖十亿参数级的视觉-语言或视频生成骨干网络，导致训练成本高、推理延迟大。论文关注的问题是：能否用紧凑模型在潜空间中完成未来观测预测，从而降低训练与推理开销，同时保持多任务机器人操作性能。

### 核心思路/方法
- 在冻结的 DINOv3 编码器潜空间中预测未来观测，而非生成像素或依赖大型视频生成骨干。
- 将每个相机视角的特征压缩为少量 token。
- 使用轻量预测器，以任务为条件、而非以动作为条件，预测两个未来时间视野的 token。
- 预测以未来帧的稠密 patch 特征进行监督，促使模型编码未来场景的空间布局。
- 动作解码器直接从当前 token 与预测 token 回归未来动作块。

### 主要贡献
- 提出 GAWM，一个参数少于 100M、无需机器人或视频预训练的多任务世界-动作模型。
- 在 RoboTwin 2.0 上优于十亿参数级 WAMs，在 LIBERO 上与十亿参数级 VLAs 表现相当。
- 在双臂机器人上，于留出演示数据上取得比微调的十亿参数 VLA 更低的动作预测误差，且推理延迟显著更低。
- 消融研究表明，在训练数据或训练时间受限时，潜空间世界模型能显著提升性能。
- 代码已公开。

### 局限性
- 摘要未提供足够信息说明模型在更多任务类型、真实场景多样性或长期任务上的泛化边界。
- 摘要未提供足够信息说明失败案例、安全性或部署约束。
- 摘要未提供足够信息说明与基线在训练成本、显存占用和能耗方面的完整对比细节。
- 摘要未提供足够信息说明消融实验的具体设置与完整数值。

### 阅读优先级
高。理由：该论文直接针对世界-动作模型“大参数、高成本、高延迟”的核心痛点，提出紧凑替代方案，并在多个基准和真机任务上给出与十亿参数模型可比或更优的结果；同时涉及潜空间世界模型监督、任务条件预测和动作块回归等可复用设计，对机器人操作与高效具身策略学习具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

World-action models (WAMs) incorporate the prediction of future observations into robot policy learning. However, most WAMs build on billion-parameter vision-language or video-generation backbones, which incur high training cost and inference latency. In this letter, we present GAWM (Geometry-Aware World Model), a compact multi-task WAM that predicts future observations in the latent space of a frozen DINOv3 encoder. GAWM compresses the features of each camera view into a small set of tokens. A lightweight predictor, conditioned on the task rather than on actions, forecasts these tokens at two future horizons. The forecast is supervised with the dense patch features of future frames, which requires it to encode the spatial layout of the future scene. An action decoder directly regresses a chunk of future actions from the current and predicted tokens. With fewer than 100M parameters and no robot or video pretraining, GAWM outperforms billion-parameter WAMs on RoboTwin 2.0 and performs comparably to billion-parameter VLAs on LIBERO. On a dual-arm robot, it achieves lower action-prediction error on held-out demonstrations than a fine-tuned billion-parameter VLA, with substantially lower inference latency. Ablation studies show that the latent world model substantially improves performance when training data or training time is limited. Code is available at https://github.com/gaoxiang12/ga-wm.

</details>

#### 2026-10-27 - ActiveAlign: Aligning Egocentric Manipulation via Active Perception

**Authors:** Ri-Zhao Qiu, Bowen Wen, Yifeng Jiang, Chen Tessler, Eric Heiden, Xue Bin Peng, Xiaolong Wang, Stan Birchfield, Erwin Coumans
**Links:** [abs](https://arxiv.org/abs/2610.36859) - [pdf](https://arxiv.org/pdf/2610.36859)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** differentiable rendering, rendering, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ActiveAlign: Aligning Egocentric Manipulation via Active Perception
- 作者：Ri-Zhao Qiu, Bowen Wen, Yifeng Jiang, Chen Tessler, Eric Heiden, Xue Bin Peng, Xiaolong Wang, Stan Birchfield, Erwin Coumans
- 出版日期：2026-10-27T08:54:27Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.36859 ；PDF https://arxiv.org/pdf/2610.36859

### 一句话总结
提出 ActiveAlign 框架，用主动感知（挥手做手眼标定、触摸做物体对齐）缩小 Real2Sim2Real 中被动观测带来的 real2sim 差距，并在真实 Unitree G1 上展示毫米级精细操作。

### 研究问题
现有 Real-to-Sim-to-Real 方法多依赖被动感知，因观测不完美而产生 real2sim 差距。论文关注如何通过主动交互而非被动观测来对齐这一差距，尤其是机器人操作场景下的手眼标定与物体对齐问题。

### 核心思路/方法
受人类通过动作主动感知的启发，ActiveAlign 将主动感知用于 Real2Sim2Real 对齐，包含两个互补模块：
- ActiveAlign-Waving：利用主动手部运动与可微渲染进行手眼标定。
- ActiveAlign-Touching：通过触觉反馈细化物体对齐，达到毫米级精度。
二者结合用于实现较强的 real2sim 对齐；摘要还指出 ActiveAlign-Waving 可用于为开源未标定机器人操作数据集整理仿真环境。

### 主要贡献
- 提出 ActiveAlign 框架，以主动感知对齐 Real2Sim2Real 差距，区别于被动感知路线。
- 设计 ActiveAlign-Waving（主动手部运动 + 可微渲染做手眼标定）与 ActiveAlign-Touching（触觉反馈细化物体对齐，毫米级精度）两个互补模块。
- 展示 ActiveAlign-Waving 可用于为开源未标定机器人操作数据集构建/整理仿真环境。
- 在真实 Unitree G1 机器人上演示毫米级物体精细操作，如按按钮和移动滑块。

### 局限性
摘要未提供足够信息。具体实验规模、成功率、基线对比、触觉传感器配置、可微渲染细节、失败案例与泛化边界均未在摘要中说明。

### 阅读优先级
中。理由：论文聚焦 Real2Sim2Real 对齐与主动感知，方法模块清晰且给出真实机器人毫米级操作演示，对具身操作与仿真对齐方向有参考价值；但摘要未提供定量结果与对比细节，需阅读全文后才能判断其效果与适用范围。

</details>

<details>
<summary>Abstract</summary>

Real-to-Sim-to-Real (Real2Sim2Real) enables structured world representations for planning, interpretability, and safe execution. Most existing approaches rely on passive perception, which creates real2sim gaps due to imperfect observation. Inspired by how humans perceive actively through actions, we propose ActiveAlign, a framework that leverages active perception to align the Real2Sim2Real gap from interactions. ActiveAlign introduces two complementary modules: (i) ActiveAlign-Waving, which performs hand-eye calibration by exploiting active hand motions and differentiable rendering, and (ii) ActiveAlign-Touching, which refines object alignment through tactile feedback to achieve millimeter-level precision. Together, these capabilities enable strong real2sim alignment. We demonstrate that ActiveAlign-Waving can be used to curate simulation environments for open-sourced uncalibrated robot manipulation datasets, and demonstrate on a real Unitree G1 robot that ActiveAlign enables fine manipulation of millimeter-scale objects such as pressing buttons and moving sliders.

</details>

#### 2026-10-27 - OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation

**Authors:** Adithyavairavan Murali, Yash Oza, Karanbir Chahal, Neel Jawale, Silas De Vries, Hesam Rabeti, Erwin Coumans, Balakumar Sundaralingam, Stan Birchfield
**Links:** [abs](https://arxiv.org/abs/2610.36598) - [pdf](https://arxiv.org/pdf/2610.36598)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation
- 作者：Adithyavairavan Murali, Yash Oza, Karanbir Chahal, Neel Jawale, Silas De Vries, Hesam Rabeti, Erwin Coumans, Balakumar Sundaralingam, Stan Birchfield
- 出版日期：2026-10-27T03:58:54Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.36598) / [PDF](https://arxiv.org/pdf/2610.36598)

### 一句话总结
OpenJaws 是一个完全开源、以低成本立体相机改进 UMI 手持数据采集定位精度的软硬件框架，并配套提出定位精度基准。

### 研究问题
手持数据采集接口（如 UMI）可以在没有机器人参与的情况下在野外采集操作演示，但其动作标签质量受视觉定位精度限制。现有系统使用单目视觉惯性里程计恢复末端执行器位姿，存在尺度模糊和漂移问题；或依赖闭源模块和外部基础设施，重新引入成本与部署负担。

### 核心思路/方法
- 提出 OpenJaws：面向传感器化 UMI 的完全开源硬件与软件框架，旨在改进定位并简化跨机器人平台部署。
- 硬件上，将模块化 3D 打印夹爪（带标准化 ISO 适配器）与低成本立体相机配对，用于恢复度量尺度的相机轨迹。
- 提出 UMI-Loc-Bench-v1：用于量化手持数据采集设备真实世界定位精度的基准。
- 摘要称立体定位显著优于单目替代方案，并展示用 OpenJaws 采集数据训练的策略可在真实机器人上跨多个任务部署。

### 主要贡献
- 开源硬件与软件框架 OpenJaws，面向传感器化 UMI，采用立体相机进行度量定位。
- 模块化 3D 打印夹爪与标准化 ISO 适配器设计。
- 提出 UMI-Loc-Bench-v1 定位精度基准。
- 摘要报告立体定位显著优于单目方案。
- 展示基于 OpenJaws 数据训练的策略可在真实机器人多任务部署。
- 硬件、软件和数据以商业宽松许可证发布。

### 局限性
- 摘要未提供足够信息说明具体任务数量、机器人平台类型、策略类型及定量成功率。
- 摘要未提供足够信息说明立体定位与单目方案的具体精度数值、基准规模与评测设置。
- 摘要未提供足够信息说明硬件成本、计算需求、实时性及在不同环境下的鲁棒性。
- 摘要未提供足够信息说明与闭源或外部基础设施方案的直接对比细节。

### 阅读优先级
中。理由：该工作聚焦 UMI 数据采集中的定位精度与开源部署问题，并发布基准与开源资源，对具身操作数据采集方向有参考价值；但摘要未给出定量实验细节，需阅读全文才能判断实际精度提升幅度与部署效果。

</details>

<details>
<summary>Abstract</summary>

Handheld data-collection interfaces such as the Universal Manipulation Interface (UMI) allow manipulation demonstrations to be gathered in the wild without a robot in the loop, but the quality of the resulting action labels is bounded by the accuracy of vision-based localization. Existing systems recover end-effector pose from monocular visual-inertial odometry, which is subject to scale ambiguity and drift, or delegate tracking to closed-source modules and external infrastructure that reintroduce cost and setup burden. We present OpenJaws, a fully open hardware and software framework for sensorized UMI that improves localization and simplifies deployment across robot platforms. OpenJaws pairs a modular, 3D-printed gripper exposing a standardized ISO adapter with a low-cost stereo camera to recover metric camera trajectories. We further introduce UMI-Loc-Bench-v1, a benchmark quantifying real-world localization accuracy for handheld data-collection devices, and show that stereo localization substantially outperforms monocular alternatives. Finally, we demonstrate that policies trained on data collected with OpenJaws can be deployed on a real robot across multiple tasks. Hardware, software, and data are released under a commercially permissive license. Code, data, and videos are available at https://open-jaws.github.io/

</details>

#### 2026-10-26 - Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data

**Authors:** Dianyi Yang, Mengya Liu, Zhumei Wang, Yu Liu, Xiaochen Zhang, Yixuan Li, Le Ma, Yuhang Yang, Weiqi Huang, Wei Liang, Baoxiong Jia, Siyuan Huang
**Links:** [abs](https://arxiv.org/abs/2610.35075) - [pdf](https://arxiv.org/pdf/2610.35075)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data
- 作者：Dianyi Yang, Mengya Liu, Zhumei Wang, Yu Liu, Xiaochen Zhang, Yixuan Li, Le Ma, Yuhang Yang, Weiqi Huang, Wei Liang, Baoxiong Jia, Siyuan Huang
- 出版日期：2026-10-26T09:20:31Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.35075 ；PDF https://arxiv.org/pdf/2610.35075 ；项目页 https://young-bit.github.io/zero-hlm/

### 一句话总结
Zero-HLM 提出一个 real-to-sim-to-real 框架，将智能手机采集与仿真源示范转化为可扩展的人形 loco-manipulation 训练数据，并声称无需真实机器人数据即可实现零样本迁移。

### 研究问题
论文关注人形机器人 loco-manipulation 的可泛化学习受限于昂贵真实世界示范的问题。摘要指出，仿真虽然提供了可扩展替代方案，但需要视觉逼真、物理就绪的场景以及可执行全身运动；论文即围绕如何构建这样的仿真训练数据并实现零样本迁移展开。

### 核心思路/方法
摘要给出的方法要点包括：
1. **Real-to-sim-to-real 框架**：将智能手机采集和仿真源示范转化为人形 loco-manipulation 的可扩展训练数据。
2. **Gaussian-guided agentic real-to-sim reconstruction**：用于对齐视觉场景与物理场景。
3. **Motion-environment co-adaptation**：利用 rollout 反馈修正全身参考运动与交互几何。
4. **数据生成与训练**：生成 4,800 条经过物理验证的示范，用于三个 Unitree G1 任务的零样本迁移；仿真训练的 GR00T N1.7 被用于评估。

### 主要贡献
摘要明确给出的贡献包括：
- 提出 Zero-HLM 这一 real-to-sim-to-real 框架，面向无需真实机器人数据的人形 loco-manipulation 训练。
- 通过高斯引导的 agentic real-to-sim 重建对齐视觉与物理场景，并通过 rollout 反馈进行运动-环境协同适配。
- 生成 4,800 条物理验证示范，并报告在三个 Unitree G1 任务上的零样本迁移结果。
- 报告仿真训练的 GR00T N1.7 平均全任务成功率为 66.7%，而真实数据训练为 46.7%。
- 在泛化配置上，扩展仿真训练将 pooled success 从基于真实数据策略的 23% 提升到 69%，且不增加真实示范。

### 局限性
- 摘要未提供足够信息说明真实机器人实验的具体设置、任务定义、评估协议与统计显著性。
- 摘要未提供足够信息说明智能手机采集的规模、质量要求及失败案例。
- 摘要未提供足够信息说明 real-to-sim 重建与运动-环境协同适配的计算成本、人工介入程度和泛化边界。
- 摘要未提供足够信息说明与其它基线方法的完整对比及消融实验细节。

### 阅读优先级
**高**。理由：论文直接针对人形 loco-manipulation 中真实数据昂贵这一关键瓶颈，提出无需真实机器人数据的 real-to-sim-to-real 数据生成与零样本迁移框架，并给出明确的成功率对比与泛化配置结果；若关注人形机器人学习、仿真到现实迁移或可扩展示范生成，该摘要信息具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Learning generalizable humanoid loco-manipulation remains bottlenecked by costly real-world demonstrations. Simulation provides a scalable alternative, but requires visually faithful, physics-ready scenes and executable whole-body motions. We present Zero-HLM, a real-to-sim-to-real framework that transforms smartphone captures and simulated source demonstrations into scalable training data for humanoid loco-manipulation. Gaussian-guided agentic real-to-sim reconstruction aligns visual and physical scenes; motion-environment co-adaptation uses rollout feedback to correct whole-body references and interaction geometry. We generate 4,800 physically validated demonstrations for zero-shot transfer across three Unitree G1 tasks. Simulation-trained GR00T N1.7 achieves 66.7% mean full-task success, versus 46.7% with real-data training. On generalized configurations, expanded simulation training raises pooled success from 23% for base-trained real-data policies to 69%, without additional real demonstrations. Project page: https://young-bit.github.io/zero-hlm/

</details>

#### 2026-10-25 - How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder: A Hierarchical, Matched Sim-Real Benchmark for Physical Interaction

**Authors:** Haibao Yu, Jiaqi Meng, Zijian Zhang, Bowen Jing, Lei Yang, Yue Hu, Chenchen Ge, Yiming Hou, Chenbo Xin, Dawen Ye, Haifang Qin, Jin Li, Weitao Zhou, Jianing Qiu, Jiankai Sun, Dandan Zhang, Zaiqing Nie, Ping Luo, Ding Zhao
**Links:** [abs](https://arxiv.org/abs/2610.34527) - [pdf](https://arxiv.org/pdf/2610.34527)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder: A Hierarchical, Matched Sim-Real Benchmark for Physical Interaction
- 作者：Haibao Yu, Jiaqi Meng, Zijian Zhang, Bowen Jing, Lei Yang, Yue Hu, Chenchen Ge, Yiming Hou, Chenbo Xin, Dawen Ye, Haifang Qin, Jin Li, Weitao Zhou, Jianing Qiu, Jiankai Sun, Dandan Zhang, Zaiqing Nie, Ping Luo, Ding Zhao
- 出版日期：2026-10-25T19:41:02Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.34527 ；PDF https://arxiv.org/pdf/2610.34527

### 一句话总结
论文提出 PhysLadder——一个面向富接触操作、物理与视觉匹配的层级式 Sim-Real 基准，并用 16 个家务任务评估 GPT-6 Astra 零样本表现，发现其成功率随交互层级升高而显著下降，在 L3 上降至 0.0%。

### 研究问题
如何系统评估模型在富接触操作中的物理交互能力，尤其是接触选择、持续接触下的力调节，以及协调的接触重构与力调节；以及匹配的仿真环境能否作为可重复、可扩展的测试平台来研究这些能力边界。

### 核心思路/方法
构建 PhysLadder 层级式 Sim-Real 基准：16 个家务任务分为三个累积层级——L1 接触选择与几何对齐、L2 持续接触中的力调节、L3 协调的接触重构与力调节。每个任务在物理和视觉匹配的仿真与真实环境中实例化，并共享任务定义与成功标准。对 GPT-6 Astra 进行零样本评估，每个任务在每个环境中试验三次。

### 主要贡献
- 提出 PhysLadder：包含 16 个家务任务、三层累积难度的层级式 Sim-Real 基准，强调物理与视觉匹配及共享任务定义和成功标准。
- 提供 GPT-6 Astra 的零样本评测结果：真实环境成功率从 L1 的 80.0% 降至 L2 的 47.6%、L3 的 0.0%；仿真环境对应为 66.7%、47.6%、0.0%。
- 报告 Sim-Real 一致性观察：16 个任务中有 10 个在两种环境下的成功次数相同，其余 6 个相差一次成功（三次试验中）。
- 归纳反复出现的困难：空间推理、接触选择、力调节与协调，常使局部物理进展无法累积为任务完成。

### 局限性
- 摘要仅报告 GPT-6 Astra 的零样本结果，每个任务每环境仅三次试验；未提供其他模型、训练方法或更大规模试验的信息。
- 摘要未提供任务的具体构成、成功判定的细节、仿真与真实环境匹配程度的定量指标，以及误差分析或统计显著性信息。
- 摘要未提供关于基准可扩展性、任务多样性覆盖或真实环境实验设置的具体信息。
- 摘要未提供足够信息以判断结论对其他模型或更广泛富接触任务的泛化性。

### 阅读优先级
高。理由：该工作直接给出富接触操作中分层能力边界的实证结果，并强调匹配 Sim-Real 的可重复评测设计；对关注具身智能评测、物理交互与仿真到现实一致性的研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce PhysLadder, a hierarchical Sim-Real benchmark for evaluating physical interaction capabilities in contact-rich manipulation. Its 16 household tasks span three cumulative levels: contact selection and geometric alignment (L1), force regulation within sustained contact (L2), and coordinated contact reconfiguration and force regulation (L3). Each task is instantiated in physically and visually matched simulated and real-world environments, with shared task definitions and success criteria. We evaluate GPT-6 Astra zero-shot with three trials per task in each environment. Real-world success rates decline from 80.0% at L1 to 47.6% at L2 and 0.0% at L3, with corresponding simulation rates of 66.7%, 47.6%, and 0.0%. Ten of the 16 tasks have identical success counts across environments; the remaining six differ by one success out of three trials. Across both environments, recurring difficulties in spatial reasoning, contact selection, force regulation, and coordination often prevent local physical progress from accumulating into task completion. These findings characterize Astra's observed capability boundary across increasing interaction demands and, for this model, support matched simulation as a repeatable, scalable testbed for studying the sustained, coordinated physical interactions that limit reliable manipulation.

</details>

#### 2026-10-25 - AuRA: From Atoms to Bits through Autonomous Robot Interaction

**Authors:** Xinchen Yu, Yoonkyo Jung, Haoran Chen, Zikui Cai, Aayush Talreja, Seungjae Lee, Hyunjin Kim, Furong Huang
**Links:** [abs](https://arxiv.org/abs/2610.34452) - [pdf](https://arxiv.org/pdf/2610.34452)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AuRA: From Atoms to Bits through Autonomous Robot Interaction
- 作者：Xinchen Yu, Yoonkyo Jung, Haoran Chen, Zikui Cai, Aayush Talreja, Seungjae Lee, Hyunjin Kim, Furong Huang
- 出版日期：2026-10-25T17:10:27Z
- 分类：主分类 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.34452 ；PDF https://arxiv.org/pdf/2610.34452

### 一句话总结
AuRA 通过自主机器人交互与数据准备流程，减少数字孪生重建中对人工操作和标注的依赖，并在 13 个可变形物体上降低人工投入与采集时间。

### 研究问题
仿真可支持规模化机器人学习实验，但获取符合物理规律的数字孪生往往需要人工操作和手动标注记录到的交互数据。论文关注如何减少数字孪生重建过程中对人类劳动的依赖。

### 核心思路/方法
AuRA 是一个自动化机器人交互与数据准备的系统，用于数字孪生重建。摘要给出的方法组成包括：
- 执行感知的抓取选择；
- 从机器人状态推导夹爪运动测量；
- 使用配准后的交互前几何与外观先验。

这些设计旨在支持自主采集、避免依赖视觉夹爪跟踪，并恢复被机器人遮挡的物体信息。

### 主要贡献
- 提出 AuRA 系统，自动化机器人交互和数据准备，以支持数字孪生重建。
- 在 13 个可变形物体上，相对基线将每个成功重建资产的主动人工劳动减少 88.5%，实际采集时间减少 55.4%。
- 与人工采集的 PhysTwin 基线相比，在已知夹爪运动的未来预测任务中，9 项指标中有 7 项改善，其中单向 \(L_1\) Chamfer 距离降低 28.1%。
- 在所评估的未见交互下，取得相近的平均轮廓 IoU 和 Chamfer 距离。
- 结果表明自主机器人交互有潜力支持更高效的数字孪生获取，并保持可比的重建质量。

### 局限性
摘要未提供足够信息说明局限性与失败情形。摘要未提供足够信息说明方法在更多物体类别、真实部署条件、不同机器人平台或更广泛交互场景下的适用性。摘要未提供足够信息说明“未见交互”的具体定义、评估规模及统计细节。

### 阅读优先级
中。理由：论文主题涉及机器人学习、数字孪生获取与自主数据采集，摘要给出了明确的人工劳动与采集时间降幅及重建指标对比；但摘要篇幅有限，未展开方法细节、实验设置和局限性。若关注可变形物体数字孪生或机器人自主数据采集，可优先阅读全文进一步核验。

</details>

<details>
<summary>Abstract</summary>

Simulation enables robot-learning experiments at scale, but acquiring physics-informed digital twins often requires human manipulation and manual annotation of recorded interactions. To reduce this reliance on human effort, we present AuRA, a system that automates robot interaction and data preparation for digital-twin reconstruction. AuRA combines execution-aware grasp selection, gripper-motion measurements derived from robot states, and registered pre-interaction geometry and appearance priors. These choices enable autonomous collection, avoid reliance on visual gripper tracking, and recover object information obscured by the robot. Across 13 deformable objects, AuRA reduces active human labor and wall-clock collection time per successfully reconstructed asset by 88.5% and 55.4%, respectively. Relative to the human-collected PhysTwin baseline, AuRA improves seven of nine metrics for future prediction under known gripper motion, including a 28.1% reduction in one-way $L_1$ Chamfer distance. It also achieves similar mean silhouette IoU and Chamfer distance under the evaluated unseen interactions. These results highlight the potential of autonomous robot interaction to support more efficient digital-twin acquisition with comparable reconstruction quality.

</details>

#### 2026-10-25 - On Distributed Sensing and Adversarial Localization of Narrowband Acoustic Sources for Offshore Data Center Monitoring

**Authors:** Adnan Abdullah, David Blow, Harsha Gundala Sureshbabu, Dongyoon Joung, Sara Rampazzi, Md Jahidul Islam
**Links:** [abs](https://arxiv.org/abs/2610.34393) - [pdf](https://arxiv.org/pdf/2610.34393)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：On Distributed Sensing and Adversarial Localization of Narrowband Acoustic Sources for Offshore Data Center Monitoring
- 作者：Adnan Abdullah, David Blow, Harsha Gundala Sureshbabu, Dongyoon Joung, Sara Rampazzi, Md Jahidul Islam
- 出版日期：2026-10-25T15:54:02Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2610.34393 ；PDF https://arxiv.org/pdf/2610.34393

### 一句话总结

针对海上数据中心面临的窄带对抗性声源威胁，论文提出一种结合移动接收器锚点约束与粒子滤波的分布式声学定位与跟踪框架，以缓解稀疏传感器下 TDOA 混叠导致的定位模糊问题。

### 研究问题

论文关注海上数据中心监测场景中的被动声学监视问题，具体是定位并跟踪具有威胁性的窄带对抗性声源。摘要指出，传统声源定位方法依赖宽带信号和紧凑接收阵列，而该场景具有两个关键困难：一是声源为窄带发射，二是传感器稀疏。在此条件下，观测到的 TDOA 测量会发生混叠，产生多解的模糊解空间，使传统定位方法失效。因此，核心问题是：在窄带、稀疏传感器、接收器位置不确定和感知噪声条件下，如何约束可行解空间并实现稳定的声源定位与跟踪。

### 核心思路/方法

论文提出一种两阶段流水线：

1. **锚点约束的初始位置估计**：引入一个移动接收器，使其与选定的固定接收器临时组成锚点对，从而对可行的解空间施加约束，缓解窄带 TDOA 混叠带来的模糊性。
2. **粒子滤波联合跟踪**：在获得初始源位置后，初始化粒子滤波，联合跟踪声源的位置与速度；跟踪过程使用一个实时锚点测量，并结合质量自适应的固定接收器对测量。

方法整体面向稀疏传感器与窄带发射条件下的分布式声学感知，强调通过移动锚点与测量质量自适应来提升定位与跟踪的可行性。

### 主要贡献

- 提出面向海上数据中心声学监视的窄带对抗性声源定位与跟踪框架。
- 针对窄带发射与稀疏传感器导致的 TDOA 混叠和多解模糊问题，设计移动接收器临时锚点对约束解空间的两阶段方法。
- 将初始锚点约束估计与粒子滤波联合位置—速度跟踪结合，并引入质量自适应的固定接收器对测量。
- 通过蒙特卡洛声学仿真、ROS-Gazebo 机器人演示和开放水域现场实验进行评估；摘要报告仿真中定位成功率为 91%，10 次现场试验中有 9 次在接收器位置不确定与感知噪声条件下跟踪误差低于 2 m。

### 局限性

摘要未提供足够信息说明方法的具体失败模式、计算开销、可扩展性、不同窄带条件与传感器稀疏程度下的系统性能边界，也未提供现场实验中未成功试验的原因分析。此外，摘要未提供足够信息说明与现有基线方法的定量对比细节、实验规模和数据采集条件。

### 阅读优先级

**中**。理由：该论文面向海上数据中心基础设施的被动声学监视，问题设定明确，结合移动锚点约束与粒子滤波的思路对窄带稀疏传感定位具有针对性，且包含仿真、机器人演示与开放水域实验等多层验证。但摘要未给出与现有方法的详细对比和充分局限性分析；若读者关注窄带 TDOA 混叠、稀疏阵列定位或基础设施声学监视，优先级可视为中偏高；若仅关注通用声源定位方法，则为中等。

</details>

<details>
<summary>Abstract</summary>

This report investigates an acoustic surveillance framework for localizing and tracking narrowband adversarial acoustic sources that threaten offshore data centers. Unlike conventional sound source localization (SSL) methods that rely on broadband signals and compact receiver arrays, the considered scenario involves narrowband emissions and sparse sensors. In such scenarios, the observed time-difference-of-arrival (TDOA) measurements are aliased and produce an ambiguous solution space, rendering conventional localization methods ineffective. To address this challenge, we integrate a mobile receiver that temporarily forms anchor pairs with selected fixed receivers, constraining the feasible solution space. The proposed two-stage pipeline first estimates the initial source position using anchor constraints, then initializes a particle filter that jointly tracks source position and velocity using one live anchor measurement and quality-adaptive fixed-pair measurements. We evaluate the proposed method through Monte Carlo acoustic simulations, ROS-Gazebo robotic demonstrations, and open-water field experiments. Our framework achieves a localization success rate of 91% in simulation, while 9 of 10 field trials show tracking error below 2m under receiver-position uncertainty and noisy sensing conditions. These findings demonstrate the feasibility of passive acoustic surveillance for protecting large-scale infrastructure against acoustic threats.

</details>

#### 2026-10-25 - From Presence Labels to Bounding Boxes: Can Multimodal Large Language Models Scale Surgical Instrument Localization?

**Authors:** Mohamed Hamdy, Muraam Abdel-Ghani, Fatmaelzahraa Ahmed, Sifna Nasar, Mariam Ahmed, Khalid Al-Jalham, Abdulaziz Al-Ali, Shidin Balakrishnan
**Links:** [abs](https://arxiv.org/abs/2610.34218) - [pdf](https://arxiv.org/pdf/2610.34218)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Presence Labels to Bounding Boxes: Can Multimodal Large Language Models Scale Surgical Instrument Localization?
- 作者：Mohamed Hamdy, Muraam Abdel-Ghani, Fatmaelzahraa Ahmed, Sifna Nasar, Mariam Ahmed, Khalid Al-Jalham, Abdulaziz Al-Ali, Shidin Balakrishnan
- 出版日期：2026-10-25T11:18:07Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.34218) | [PDF](https://arxiv.org/pdf/2610.34218)

### 一句话总结
论文提出并评估一个基于多模态大语言模型（MLLM）的可扩展标注框架，将手术帧与已有的器械存在性标签转换为器械边界框，并在 Cholec80 腹腔镜胆囊切除术数据上系统分析其可靠性、成本与设计敏感性。

### 研究问题
手术器械的空间定位依赖边界框标注，是手术场景理解的基础，但现有标注往往只覆盖部分帧、视频子集或数据集变体，而非完整手术流程；人工扩展标注耗时且依赖专家。弱监督方法和基于检测器的伪标签又需要任务特定训练，且可能不精确。因此论文关注：能否利用 MLLM 将已有器械存在性标签规模化地转换为准确边界框，并系统评估其可靠性、成本与设计敏感性。

### 核心思路/方法
- 设计一个基于 MLLM 的可扩展标注框架，将手术帧和已有的器械存在性标签转换为边界框。
- 在 Cholec80 的腹腔镜胆囊切除术数据上实例化该框架，使用六个 MLLM 及一种多调用配置。
- 采用精心设计的分层方案，由两名标注者独立标注 1,000 帧，并由一名专家外科医生审核其中一组标注以建立参考。
- 比较不同模型和调用配置的识别与定位表现，并分析结构化多阶段标注流程的效果。

### 主要贡献
- 提出将器械存在性标签转换为边界框的 MLLM 标注框架，并系统分析其可靠性、成本和设计敏感性。
- 实验显示器械集合识别 F1 为 88.2 至 92.7，而 mIoU 为 0.180 至 0.735，表明相近的识别表现可能掩盖较大的定位差异。
- 结构化多阶段标注流程达到 0.784 mIoU，高于最佳单次调用基线的 0.735，接近人-人一致性的 0.814。
- 使用最佳准确率流程创建并公开发布 Cholec80 的空间扩展：覆盖 80 个视频的全部 184,498 个已标注帧，共 285,977 个边界框；标注与人工参考已在 GitHub 公开。

### 局限性
- 论文仅在 Cholec80 的腹腔镜胆囊切除术数据上实例化框架，摘要未提供在其他手术类型或数据集上的验证信息。
- 摘要未提供六种 MLLM 的具体名称、多调用配置的细节、成本分析的具体结果，以及设计敏感性分析的具体维度与结论。
- 人工参考仅由专家外科医生审核两名标注者中的一组标注集，摘要未说明另一组标注是否也经过专家审核。
- 摘要未提供推理成本、运行时间或计算资源需求的具体数据。
- 摘要未提供失败案例、误差来源或框架在低质量存在性标签下的表现。

### 阅读优先级
中。理由：该工作直接针对手术数据边界框标注的可扩展性问题，并公开发布大规模 Cholec80 空间扩展标注，对手术场景理解、检测与视觉-语言应用有实用价值；同时揭示了识别指标与定位指标之间的显著差异，具有方法学警示意义。但摘要未提供跨数据集验证和详细成本结果，若读者关注特定 MLLM 选型、标注成本或非胆囊切除术场景，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Spatial localization of surgical instruments through bounding-box annotations is a foundational component of surgical scene understanding, supporting detection, tracking, interaction analysis, and grounded vision-language applications. Yet existing annotations often cover selected frames, video subsets, or dataset variants rather than complete procedures. Manual extension is time-consuming and expert-dependent. Additionally, weakly supervised and detector-based pseudo-labels require task-specific training and may be imprecise. In this study, we design a scalable MLLM-based annotation framework that converts surgical frames and existing instrument-presence labels into accurate bounding boxes, and systematically analyze its reliability, cost, and design sensitivity. We instantiate the framework using six MLLMs and a multi-call configuration on laparoscopic cholecystectomy in Cholec80. Using a carefully designed stratification scheme, two annotators independently label 1,000 frames, and an expert surgeon reviews one annotation set to establish the reference. Results show that instrument-set F1 ranges from 88.2 to 92.7,whereas mIoU ranges from 0.180 to 0.735, showing that comparable recognition can conceal large localization differences. A structured multi-stage annotation pipeline achieves 0.784 mIoU, compared with 0.735 for the best single-call baseline and 0.814 human-human agreement. Using the best accuracy pipeline, we create and publicly release a spatial extension of Cholec80 comprising 285,977 bounding boxes across all 184,498 annotated frames from the 80 videos. The annotations and human references are made available on GitHub

</details>

#### 2026-10-25 - PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy

**Authors:** Mengdi Li, Boxian Yao, Xiyu Zhu, Yifan Yang, Yunfan Lou, Xuan Han, Tao Liu, Zhibo Pang
**Links:** [abs](https://arxiv.org/abs/2610.34147) - [pdf](https://arxiv.org/pdf/2610.34147)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PS-DLO: Property- and Spatially Aware Deformable Linear Object Manipulation Policy
- 作者：Mengdi Li, Boxian Yao, Xiyu Zhu, Yifan Yang, Yunfan Lou, Xuan Han, Tao Liu, Zhibo Pang
- 出版日期：2026-10-25T08:29:58Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.34147 ；PDF https://arxiv.org/pdf/2610.34147

### 一句话总结
PS-DLO 提出一种结合物体物理属性先验与未来空间监督信息的可变形线性物体操作策略，并在真实单臂/双臂多任务及视觉变化条件下验证其有效性。

### 研究问题
论文关注可变形线性物体（DLO）操作中的耦合感知与控制难题：一方面，细长几何形态导致精确定位困难；另一方面，形变依赖物体特定的物理属性。摘要指出，需要同时应对定位困难与属性相关形变的问题。

### 核心思路/方法
- 使用对比式图像—文本学习，将初始观测映射为 DLO 属性的类别化描述，为动作生成提供显式的物理与结构先验。
- 使用 SAM3 从未来观测中提取掩码引导特征，并将这些特征蒸馏到策略的动作专家中，以编码任务相关的 DLO 区域及其后续构型。
- 在单臂和双臂平台上分别训练共享多任务策略，并在九个真实世界任务上评估。

### 主要贡献
- 提出 PS-DLO 策略，将物体属性先验与未来空间监督结合用于 DLO 操作。
- 在九个真实世界任务、单臂与双臂平台上评估，每个 embodiment 训练共享多任务策略；平均成功率为 68.9%，比最强基线高 20.0 个百分点。
- 在蝴蝶结解结任务的泛化实验中，于七种视觉偏移条件中的六种取得高于基线的成功率，表明对视觉变化具有更好的鲁棒性。

### 局限性
- 摘要未提供足够信息说明方法在更广泛 DLO 类型、任务分布或真实部署条件下的适用边界。
- 摘要未提供足够信息说明对比式图像—文本学习所依赖的属性类别描述范围及其标注需求。
- 摘要未提供足够信息说明 SAM3 未来观测特征蒸馏的具体实现细节、计算开销与失败模式。
- 摘要未提供足够信息说明未取得优势的那一种视觉偏移条件的具体原因。
- 摘要未提供足够信息说明与最强基线之外的更多基线比较情况。

### 阅读优先级
高。理由：摘要明确给出真实世界多任务评估结果、相对最强基线的定量提升以及视觉泛化实验结论，且问题设定聚焦 DLO 操作中的感知—控制耦合难点；若关注机器人操作策略、物体属性先验或未来空间监督，该文具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Deformable linear objects (DLO) pose a coupled perception and control challenge: their slender geometry makes precise localization difficult, while their deformations depend on object-specific physical properties. To address this challenge, we propose PS-DLO, a property- and spatially aware DLO manipulation policy. First, contrastive image-text learning maps the initial observation to categorical descriptions of DLO properties, providing explicit physical and structural priors for action generation. Second, SAM3 extracts mask-guided features from future observations, which are distilled into the policy's action expert to encode task-relevant DLO regions and their subsequent configurations. We evaluate PS-DLO on nine real-world tasks across single-arm and bimanual platforms, training a shared multi-task policy for each embodiment. PS-DLO achieves an average success rate of 68.9%, exceeding the strongest baseline by 20.0 percentage points. In generalization experiments, PS-DLO achieves higher success rates than the baseline in six of seven visual-shift conditions on butterfly-knot untying. These results demonstrate that combining object-property priors with future spatial supervision improves multi-task DLO manipulation and robustness to visual variation.

</details>

#### 2026-10-25 - Enabling Motion-Induced WiFi-CSI Sensing in Multi-Robot Systems: A Simulation Framework

**Authors:** Brendan Dijkstra, Ninad Jadhav, Maurice Stoffijn, Stephanie Gil, Bahar Haghighat
**Links:** [abs](https://arxiv.org/abs/2610.34034) - [pdf](https://arxiv.org/pdf/2610.34034)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Enabling Motion-Induced WiFi-CSI Sensing in Multi-Robot Systems: A Simulation Framework
- 作者：Brendan Dijkstra, Ninad Jadhav, Maurice Stoffijn, Stephanie Gil, Bahar Haghighat
- 出版日期：2026-10-25T03:55:16Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.34034 ；PDF https://arxiv.org/pdf/2610.34034

### 一句话总结
该论文提出一个开源仿真框架，将 WiFi Sensor for Robotics（WSR）传感流程集成进 Gazebo，以生成具有较真实物理信号特性的合成 WiFi-CSI 测量，用于多机器人系统中运动诱导的感知、方位估计与定位研究。

### 研究问题
论文关注的问题是：WSR 方法虽已表明，机器人运动过程中采集的 WiFi-CSI 测量结合里程计可合成虚拟天线阵列，并实现运动诱导的方位估计，但其部署仍面临困难，主要原因是与标准机器人工具的集成有限，以及依赖已过时的 WiFi-CSI 采集硬件。因此，作者希望降低 WiFi-CSI 传感在多机器人系统中的使用门槛。

### 核心思路/方法
论文的核心方法是构建一个开源仿真框架，将 WSR 传感流程集成到机器人仿真器 Gazebo 中。该框架生成具有较真实物理信号特性的合成 WiFi-CSI 测量，并利用运动诱导传感及下游定位所需的较真实机器人运动。框架还支持处理仿真和真实 WiFi-CSI 数据，以便直接比较和验证。作者使用 TurtleBot3 机器人，通过比较仿真实验与真实世界实验来验证框架，并展示其在方位估计和机器人定位中的用途。

### 主要贡献
- 提出一个开源仿真框架，将 WSR 传感流程集成进 Gazebo。
- 生成具有较真实物理信号特性的合成 WiFi-CSI 测量。
- 利用较真实的机器人运动支持运动诱导传感和下游定位。
- 支持处理仿真与真实 WiFi-CSI 数据，用于直接比较和验证。
- 通过 TurtleBot3 机器人的仿真与真实实验比较验证框架，并展示其在方位估计和机器人定位中的应用。
- 旨在使 WSR 风格传感成为机器人研究中可访问的模块化传感模态，为将 WiFi-CSI 传感与多模态感知结合用于定位和协调提供基础。

### 局限性
摘要未提供足够信息说明该框架在信号模型精度、仿真与真实数据差距、可扩展性、计算开销、硬件依赖或更广泛场景下的局限。摘要也未提供足够信息说明实验规模、定量性能指标和失败案例。

### 阅读优先级
中。理由：该工作面向多机器人 WiFi-CSI 传感的仿真与开源工具，问题明确且对相关机器人感知研究有实用价值；但摘要未给出定量实验结果和详细局限，是否优先阅读取决于读者对 WiFi-CSI 传感、Gazebo 仿真或多机器人定位工具链的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

WiFi Channel State Information (CSI) enables fine-grained sensing of spatial relationships between wireless devices. The WiFi Sensor for Robotics (WSR) toolbox demonstrated that WiFi-CSI measurements collected during robot motion, combined with odometry, can be used to synthesize virtual antenna arrays, enabling motion-induced bearing estimation in multi-robot experiments. However, deploying the WSR approach has remained challenging due to its limited integration with standard robotics tools and reliance on deprecated WiFi-CSI acquisition hardware. This work presents an open-source simulation framework that integrates the WSR sensing pipeline within the robotic simulator Gazebo. The framework generates synthetic WiFi-CSI measurements with realistic physical signal properties and leverages realistic robot motion required for motion-induced sensing and downstream localization. It further supports processing both simulated and real WiFi-CSI data for direct comparison and validation. Our aim is to make WSR-style sensing accessible as a modular sensing modality for robotic research. We validate our framework by comparing simulated and real-world experiments using TurtleBot3 robots, and demonstrate its use for bearing estimation and robot localization. This work lowers the barrier to entry for WiFi-CSI-based sensing in multi-robot systems and provides a foundation for integrating WiFi-CSI sensing with multi-modal perception for localization and coordination. All code and experimental details are publicly available at https://github.com/baharhaghighat/DARS_2026_Dijkstra_et_al

</details>

#### 2026-10-22 - Skeleton-Grounded Latent Action Model for Robot World Models

**Authors:** Qi Lv, Jiayi Lin, Yuxin Jiang, Jianzong Wang, Xiang Deng, Mike Shou Zheng
**Links:** [abs](https://arxiv.org/abs/2610.31474) - [pdf](https://arxiv.org/pdf/2610.31474)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** video reconstruction, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Skeleton-Grounded Latent Action Model for Robot World Models
- 作者：Qi Lv, Jiayi Lin, Yuxin Jiang, Jianzong Wang, Xiang Deng, Mike Shou Zheng
- 出版日期：2026-10-22T16:01:33Z
- 分类：Embodied / Robotics / AR Applications（主分类）；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.31474 ；PDF https://arxiv.org/pdf/2610.31474

### 一句话总结
SkeLAM 提出用机器人骨架监督把潜在动作分解为运动学分量与残差分量，以改善机器人世界模型中潜在动作与机器人控制之间的对应关系，并支持从当前观测和机器人动作生成未来观测。

### 研究问题
机器人世界模型需要模拟环境如何随机器人动作演化。潜在动作模型可以从视频中通过把视觉变化编码为代理动作来学习动力学，但摘要指出：由重建驱动的潜在动作会把机器人运动与物体响应及其他场景变化混在一起，使其难以与机器人控制对应。SkeLAM 针对的正是这一“潜在动作与机器人控制对应不清”的问题，目标是在可控机器人世界建模中让潜在动作更具运动学可解释性和可控制性。

### 核心思路/方法
- 将潜在动作分解为两部分：由机器人骨架监督锚定的运动学分量，以及保留互补视觉动态的残差分量。
- 采用跨模态交换重建，鼓励 RGB 导出的运动学表示与骨架导出的运动学表示在视频重建过程中可以互换。
- 世界模型通过两条独立的条件通路分别引入上述两个分量，并使用 branch dropout 降低模型对未来导出的残差信息的依赖。
- 使用轻量适配器把机器人动作映射到运动学空间，再通过世界模型微调使生成适应这些预测条件。
- 推理时，模型根据当前观测和机器人动作生成未来观测。
- 摘要报告在 DROID 上相较 DreamDojo，末端执行器 ADE 降低 19.5%，LPIPS 降低 11.1%；运动探测支持运动学专门化；定性结果显示生成 rollout 中具备零样本人类到机器人运动迁移；策略评估显示预测成功率与真实机器人执行测得成功率一致。

### 主要贡献
- 提出 SkeLAM：一种骨架引导的潜在动作模型，用于可控机器人世界建模。
- 通过骨架监督将潜在动作拆分为运动学分量与残差分量，缓解重建驱动潜在动作混合机器人运动与场景变化的问题。
- 引入跨模态交换重建，促进 RGB 与骨架两种来源的运动学表示在视频重建中可互换。
- 在世界模型中以独立条件通路整合两类分量，并用 branch dropout 减少对未来残差信息的依赖。
- 使用轻量适配器连接机器人动作与运动学空间，并通过微调适配预测条件。
- 摘要给出的实证包括：DROID 上相较 DreamDojo 的 ADE 与 LPIPS 改善、运动探测支持运动学专门化、零样本人类到机器人运动迁移的定性结果，以及策略评估中预测成功率与真实机器人执行成功率一致。

### 局限性
- 摘要未提供足够信息说明方法在 DROID 之外的泛化能力。
- 摘要未提供足够信息说明骨架监督的获取方式、标注成本或对骨架质量波动的敏感性。
- 摘要未提供足够信息说明跨模态交换重建的具体实现细节与消融结果。
- 摘要未提供足够信息说明 branch dropout 的具体设置及其对其他任务的影响。
- 摘要未提供足够信息说明零样本人类到机器人运动迁移的定量范围与失败情形。
- 摘要未提供足够信息说明策略评估的规模、统计显著性与真实机器人执行条件。
- 摘要未提供足够信息说明计算开销、推理时延与训练资源需求。

### 阅读优先级
高。理由：该论文聚焦机器人世界模型中“潜在动作与机器人控制对应不清”的关键问题，提出骨架监督分解与跨模态交换重建等明确方法设计；摘要同时给出 DROID 上的定量改善、运动探测、零样本人类到机器人运动迁移和真实机器人策略评估一致性等多类证据，与具身智能/机器人世界模型方向高度相关。但摘要未展开实现细节与局限，适合作为优先阅读并进一步核查全文实验与消融的候选论文。

</details>

<details>
<summary>Abstract</summary>

Robot world models simulate how environments evolve in response to robot actions. Latent action models enable learning dynamics from videos by encoding visual transitions as proxy actions. However, reconstruction-driven latent actions mix robot motion with object responses and other scene changes, complicating their correspondence with robot controls. We propose SkeLAM, a skeleton-guided latent action model for controllable robot world modeling. SkeLAM decomposes latent actions into a kinematic component grounded by robot skeleton supervision and a residual component retaining complementary visual dynamics. Cross-modal swap reconstruction encourages RGB-derived and skeleton-derived kinematic representations to be interchangeable during video reconstruction. The world model incorporates both components through separate conditioning pathways, while branch dropout reduces its dependence on future-derived residual information. A lightweight adapter maps robot actions to the kinematic space, and subsequent world-model fine-tuning adapts generation to these predicted conditions. At inference, the model generates future observations from the current observation and robot actions. On DROID, SkeLAM reduces end-effector ADE by 19.5% and LPIPS by 11.1% compared with DreamDojo. Motion probing supports kinematic specialization, while qualitative results demonstrate zero-shot human-to-robot motion transfer in generated rollouts. Policy evaluation shows agreement between predicted success rates and those measured in real robot executions.

</details>

#### 2026-10-22 - Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

**Authors:** Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
**Links:** [abs](https://arxiv.org/abs/2610.31166) - [pdf](https://arxiv.org/pdf/2610.31166)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation
- 作者：Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
- 出版日期：2026-10-22T12:24:25Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2610.31166 ；PDF https://arxiv.org/pdf/2610.31166

### 一句话总结
论文提出面向人形机器人全身视觉-语言-动作策略的对象引导预历史记忆机制 WholeBodyMem，并构建人形记忆基准 HuMeGo，以解决动态场景中任务对象线索随时间消失导致的非马尔可夫问题。

### 研究问题
论文指出，动态场景中的人形机器人移动操作具有非马尔可夫性质：对象变化、被遮挡，或随着机器人转身和行走而离开视野时，相关线索会消失；而现有的全身视觉-语言-动作（VLA）策略只感知当前时刻。因此，论文关注的核心问题是：如何让全身 VLA 策略在动作前保留并利用目标对象此前出现过的视觉历史信息。

### 核心思路/方法
- 提出 WholeBodyMem，一种对象引导的感知记忆，用于保留机器人在执行目标动作之前所见对象事件的预历史。
- 使用 SAM3 跟踪任务对象。
- 对象事件以因果方式在自适应预算内选择关键帧。
- 动作专家通过交叉注意力读取这些关键帧，并结合编码外观、几何和时间的对象 token。
- 强调“保留正确的帧”而非“保留更多帧”。
- 构建 HuMeGo 人形记忆基准，包含六个仿真和六个真实世界 Unitree G1 任务。

### 主要贡献
- 提出 WholeBodyMem 对象引导感知记忆机制，将预历史对象事件引入全身 VLA 策略。
- 设计基于 SAM3 跟踪、对象事件因果选帧和对象 token（外观、几何、时间）的记忆读取方式。
- 构建 HuMeGo 基准，覆盖六个仿真与六个真实世界 Unitree G1 任务。
- 摘要报告：相比无记忆和均匀记忆基线，WholeBodyMem 将基础策略成功率从仿真 29.1% 提升至 72.6%，真实机器人从 36.7% 提升至 88.3%；标准 SIMPLE 任务从 70.2% 提升至 86.9%。

### 局限性
- 摘要未提供足够信息说明方法在不同对象类别、遮挡时长、光照变化或复杂动态场景下的泛化边界。
- 摘要未提供足够信息说明 HuMeGo 基准的任务多样性细节、评价指标细节和统计显著性。
- 摘要未提供足够信息说明计算开销、实时性、自适应预算的具体设定及其敏感性。
- 摘要未提供足够信息说明失败案例、与更多基线方法的系统比较以及消融实验的完整结果。

### 阅读优先级
高。理由：论文直接针对全身 VLA 人形移动操作中的非马尔可夫感知问题，提出记忆机制并构建仿真与真实机器人基准，且摘要给出了较大的成功率提升；对具身智能、机器人操作和 VLA 策略记忆方向具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert reads by cross-attention together with object tokens encoding appearance, geometry and time. We also contribute HuMeGo, a humanoid memory benchmark with six simulated and six real-world Unitree G1 tasks. Keeping the right frames rather than more frames, WholeBodyMem surpasses memoryless and uniform-memory baselines, raising its base policy's success from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, while also improving the standard SIMPLE tasks (70.2% to 86.9%).

</details>

#### 2026-10-22 - In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations

**Authors:** Hengyi Sim, Quentin Rouxel, Dennis Hong, Darwin Caldwell, Fei Chen
**Links:** [abs](https://arxiv.org/abs/2610.30988) - [pdf](https://arxiv.org/pdf/2610.30988)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations
- 作者：Hengyi Sim, Quentin Rouxel, Dennis Hong, Darwin Caldwell, Fei Chen
- 出版日期：2026-10-22T09:34:18Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.30988；PDF https://arxiv.org/pdf/2610.30988

### 一句话总结
论文提出一种基于 Transformer 的“软物体世界模型”，通过可变长度部分点云历史进行上下文学习以推断形状与材料潜变量，并进行生成式全状态估计与动作条件动力学预测，再与目标条件动作规划器结合，用于双臂软衣物折叠。

### 研究问题
软物体（如衣物）的鲁棒操作是服务与家庭机器人需要具备的关键能力，但由于状态空间维度高且形变依赖材料属性而具有挑战性。人类可通过“心理世界模型”从部分观测中想象形状与材料属性并预测动作对未来状态的影响。论文关注如何让机器人嵌入类似世界模型以提升对多种衣物的泛化能力，同时应对学习世界模型通常需要大量难以采集的真实世界数据、以及需要推断支配动力学的潜属性这两个问题。

### 核心思路/方法
论文提出 Soft-Object World Model，使用 Transformer 骨干网络在大规模模拟软物体交互数据上训练，执行生成式全状态估计和动作条件动力学预测，并采取缓解模拟到现实差距的措施。模型通过对可变长度部分点云历史进行上下文学习，学习推断潜在的形状与材料线索，从而在无需权重更新的情况下泛化到不同机器人形态、材料参数、衣物类型与形状以及操作协调模式。随后，该世界模型与目标条件动作规划器集成以进行运动合成。摘要称在仿真和真实世界中验证了双臂衣物折叠，并报告了重建保真度、预测准确性和任务成功率的提升。

### 主要贡献
- 提出 Soft-Object World Model，用于软物体的生成式全状态估计与动作条件动力学预测。
- 使用 Transformer 骨干并在大规模模拟软物体交互上训练，同时包含缓解模拟到现实差距的措施。
- 通过可变长度部分点云历史的上下文学习推断潜在形状与材料线索，实现无需权重更新的跨机器人形态、材料参数、衣物类型与形状、操作协调模式泛化。
- 将世界模型与目标条件动作规划器集成用于运动合成。
- 在仿真和真实世界中验证双臂衣物折叠，并报告重建保真度、预测准确性和任务成功率方面的改进。

### 局限性
- 摘要未提供足够信息说明模拟到现实差距缓解措施的具体内容与效果边界。
- 摘要未提供足够信息说明真实世界实验规模、衣物种类数量、成功率数值及对比基线细节。
- 摘要未提供足够信息说明模型在非折叠类软物体任务或其他操作任务上的适用性。
- 摘要未提供足够信息说明训练数据规模、计算需求及推理实时性。
- 摘要未提供足够信息说明失败案例与安全风险。

### 阅读优先级
中。理由：论文聚焦软物体双臂操作中的世界模型与部分观测泛化，问题定义和方法组合（上下文学习、点云历史、动作条件动力学、目标条件规划）对具身操作与软物体 manipulation 方向有参考价值；但摘要未给出具体实验数值、基线对比和真实世界规模，若需评估方法有效性需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations. Humans address this challenge by using mental world models that "imagine" the shape and material properties from partial observations, which enables them to predict how actions affect future states. As such, embedding such world models in robots allows for better generalization in manipulating a wide variety of garments in the real world. However, learned world models typically require large amounts of real world data that is strenuous to collect, and a mechanism to infer latent properties that govern dynamics. We present a Soft-Object World Model that performs generative full-state estimation and action-conditioned dynamics prediction using a transformer backbone trained on large-scale simulated soft object interactions, with measures to mitigate the sim-to-real gap. By learning to infer latent shape and material cues through in-context learning over a variable-length partial point-cloud history, the model generalizes across robot embodiments, material parameters, garment types and shapes, and manipulation coordination modes without weight updates. The world model is then integrated with a Goal-Conditioned action planner for motion synthesis. We validate the approach in simulation and real world for bimanual garment folding, reporting improvements in reconstruction fidelity, prediction accuracy, and task success.

</details>

#### 2026-10-21 - Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation

**Authors:** Xiongbo Shi, Shihang Du, Zongyou Yu, Ao Zhou, Xudong Zhang, Ziyu Lin, Haodong Zhang, Junqiao Zhao, Guang Chen
**Links:** [abs](https://arxiv.org/abs/2610.30540) - [pdf](https://arxiv.org/pdf/2610.30540)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation
- 作者：Xiongbo Shi, Shihang Du, Zongyou Yu, Ao Zhou, Xudong Zhang, Ziyu Lin, Haodong Zhang, Junqiao Zhao, Guang Chen
- 出版日期：2026-10-21T23:54:17Z
- 分类：Embodied / Robotics / AR Applications（主分类）；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.30540 ；PDF https://arxiv.org/pdf/2610.30540

### 一句话总结
论文提出 Spatiotemporal Retargeting（STR），利用关键帧和关键身体部位分配优化资源，并结合 Mechanics-Aware Contact Anchoring（MCA）与 Spatiotemporal Reinforcement Learning（STRL），以改善人形机器人物体交互动作重定向的计算效率和接触保真度。

### 研究问题
摘要指出，人形机器人动作重定向需要把人类示范转换为全身控制和 loco-manipulation 的参考轨迹。对于物体交互任务，成功执行依赖于在关键阶段准确保留身体—物体关系；但统一的逐帧迭代预算没有考虑这些局部化的精度需求，从而限制了重定向的计算效率。论文即针对这一“局部精度需求与统一计算预算不匹配”的问题展开。

### 核心思路/方法
论文提出 Spatiotemporal Retargeting（STR），其核心是按时空重要性分配优化努力：
- 使用视觉语言模型选择相关运动信号和身体部位；
- 根据所选信号的变化识别关键帧；
- 对关键帧分配更多求解器迭代，对所选身体部位赋予更高的交互权重；
- 引入 Mechanics-Aware Contact Anchoring（MCA），利用近似物体力旋量模型细化物体表面接触位置，同时保留所选表面方向；
- 在所得参考轨迹基础上，提出 Spatiotemporal Reinforcement Learning（STRL），结合自适应关键阶段采样，以及基于目标接近度和物体接触力的接触奖励，用于下游控制。

### 主要贡献
- 提出 STR，通过关键帧和关键身体部位的空间—时间偏好来分配重定向优化资源，以应对局部精度需求。
- 引入 MCA，用近似物体力旋量模型细化物体表面接触位置，以提升接触保真度。
- 提出 STRL，将自适应关键阶段采样与基于目标接近度和物体接触力的接触奖励结合，用于下游控制。
- 摘要报告：在 Unitree G1 仿真实验和 Unitree R1 真实世界实验中，STR 以更低计算成本提升几何接触覆盖和连续性，所得参考轨迹改善多种物体交互动作的下游任务完成情况。

### 局限性
- 摘要未提供足够信息说明方法在更多机器人平台、更多物体类别或更复杂接触场景中的泛化能力。
- 摘要未提供足够信息说明关键帧识别、视觉语言模型选择及 MCA 近似模型失败时的鲁棒性。
- 摘要未提供足够信息给出计算成本、接触覆盖、连续性及下游任务完成率的具体量化指标和统计显著性。
- 摘要未提供足够信息说明真实世界实验的规模、任务数量和评价协议。
- 摘要未提供足够信息讨论对视觉语言模型依赖、物体模型精度或力旋量近似误差的敏感性。

### 阅读优先级
中。理由：论文主题聚焦人形机器人动作重定向与 loco-manipulation，方法上把关键帧/关键部位选择、接触锚定和强化学习控制结合起来，并与摘要中提到的仿真和真实机器人实验相关；但当前仅依据摘要，缺少具体量化结果、实验规模和失败案例分析，适合作为相关方向的重点候选阅读，而非仅凭摘要即可判定为高优先级必读。

</details>

<details>
<summary>Abstract</summary>

Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration budgets do not account for these localized accuracy requirements, limiting the computational efficiency of retargeting. To address this limitation, we present Spatiotemporal Retargeting (STR), which uses keyframes and key body parts to allocate optimization effort. Specifically, a vision-language model selects relevant motion signals and body parts, and keyframes are identified from changes in the selected signals. Based on these selections, STR assigns additional solver iterations to keyframes and higher interaction weights to the selected parts. To further improve contact fidelity, we introduce Mechanics-Aware Contact Anchoring (MCA) to refine object-surface contact positions using an approximate object-wrench model while retaining the selected surface directions. Building on the resulting references, we develop Spatiotemporal Reinforcement Learning (STRL), which combines adaptive key-stage sampling with a contact reward based on target proximity and object contact forces for downstream control. Simulation experiments on a Unitree G1 and real-world experiments on a Unitree R1 demonstrate that STR improves geometric contact coverage and continuity at lower computational cost, while the resulting references improve downstream task completion across diverse object-interaction motions.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
