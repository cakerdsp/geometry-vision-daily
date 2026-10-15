# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：72
- 分类分布：
  - Embodied / Robotics / AR Applications: 25
  - Neural Scene Representations & Rendering: 16
  - 3D Reconstruction & Multi-view Geometry: 15
  - Geometry Foundation Models: 11
  - Dynamic / 4D Reconstruction: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **生成式重建从“小物体/单场景”走向“大规模世界”，并强调可更新、可操作的状态表示。**
   代表论文：WorldRecon（大规模无位姿多视角网格重建）、CityCode（稀疏航拍生成实例级参数化 3D 城市）、4LC（4D 潜在缓存支持动态世界建模）。这三者共同点是把重建结果视为可持续维护的“世界状态”，而非一次性渲染资产：WorldRecon 用全局点云作支架并分块生成，CityCode 强调持久实体身份与版本化更新，4LC 强调复用已有视觉表示避免重复渲染编码。

2. **3DGS 正从“渲染质量竞赛”分化为系统化工程问题：压缩、误差界、real-to-sim 评估与实时流水线。**
   代表论文：PLEDGE（误差有界渐进压缩）、YUBI-Real2Sim（3DGS 场景用于策略评估的质量验证）、Gaussian Splatting 综述（方法、系统与权衡）、PUGS（水下动态 3DGS 不确定性）。趋势是关注点从“能否重建/渲染”转向“能否可控地压缩、可靠地用于下游决策、能否在有物理歧义的环境下稳定工作”。

3. **不确定性、不完整性与可见性约束被显式建模，而非用正则化“掩盖”。**
   代表论文：Perception Beyond the Visible（不完整性感知场景理解研究愿景）、PUGS（水下物理不确定性作为信号）、Surface Reconstruction from Range Scans（显式利用传感器位置与可见性约束）、CoSMO（共形预测提供覆盖率保证）。这些工作共享一个方法论转向：把噪声、遮挡、传感器退化、分布偏移当作一等公民来建模，而不是当作需要被平滑掉的误差。

4. **“人类数据/网络视频 → 机器人”的跨域迁移成为具身智能的重要数据扩展路径。**
   代表论文：EgoExplorer（100 小时视觉-运动-触觉人类 loco-manipulation 观测）、DR-VLA（第一人称网络视频迁移到四足导航）、Cross-Embodiment Affordance Transfer（人类 affordance 标注转机器人可执行预测）、LynxScenes（真实轮腿机器人多任务基准）。核心矛盾是：机器人演示昂贵，人类数据丰富但存在视角/运动/形态差异；上述论文分别从观测系统、域不变表示、机器人条件化 affordance 等角度应对。

5. **力/触觉与接触动力学开始进入“世界模型”框架，与视觉动态联合建模。**
   代表论文：ForceWAM（解耦未来预测与力响应学习）、EgoExplorer（触觉观测与全身运动对齐）、Thinker-WM（RGB、度量深度、动作共享表示）。趋势是从纯视觉世界模型扩展为“视觉-力-动作”联合动力学，尤其针对接触丰富操作。

#### 技术路线观察

- **几何基础模型方向**：WorldRecon、CityCode、4LC 都在试图建立可复用的“全局几何支架”。WorldRecon 依赖重建模型估计的粗糙点云与相机位姿作为 scaffold，CityCode 从单张航拍图恢复度量尺度与道路拓扑，4LC 用共享几何与运动绑定多编码器表示。共同技术侧重点：如何在不完美先验下保持几何忠实性，同时允许生成式补全。

- **3D/4D 重建方向**：两条明显分支。其一是**鲁棒性与物理约束**，如 Surface Reconstruction 显式利用可见性约束、PUGS 将水下成像物理不确定性参数化为概率分布；其二是**动态表示与缓存**，如 4LC 的 4D latent cache、PUGS 的随机形变优化。整体看，4D 重建正从“确定性形变场”转向“概率化/不确定性感知”的动力学。

- **神经场景表示与渲染方向**：3DGS 继续作为主流表示，但研究重心明显下沉到系统层：PLEDGE 关注逐图元误差界与渐进码流，综述则明确区分“渲染吞吐”与“构建/更新/维护开销”。YUBI-Real2Sim 把 3DGS 质量与 VLA 策略评估可靠性直接挂钩，属于表示质量与下游任务性能的因果验证。

- **机器人/AR 应用方向**：可归纳为三类。感知安全类：CoSMO 用共形预测做开放世界语义导航；数据/基准类：EgoExplorer、LynxScenes、DR-VLA 的 EgoLynx；操作与迁移类：ForceWAM、Cross-Embodiment Affordance Transfer、Thinker-WM。应用侧越来越强调**开放世界、跨形态、接触丰富**这三个此前被回避的设定。

#### 值得优先阅读的论文

1. **WorldRecon**：大规模无位姿多视角生成式网格重建是当前 3D 重建的硬骨头，其“粗糙点云作全局支架 + 分块生成 + 邻域感知因果世界生成”的路线可能定义一类新范式，且与 4LC、CityCode 形成可比较的技术谱系。

2. **ForceWAM**：把世界模型从视觉扩展到六轴力/力矩，并解耦“任务兼容结果”与“局部力响应”，直接回应接触丰富操作的数据瓶颈。若方法成立，可能影响后续力-视觉联合世界模型的设计。

3. **CoSMO**：共形预测 + VLM + 动态危险词表，是“安全关键规划需要校准不确定度”这一论点的具体落地。对做机器人导航、开放世界感知的读者优先级高，且摘要给出了形式化覆盖保证与真实机器人覆盖率结果。

4. **PUGS**：水下动态 3DGS 的不确定性建模具有方法迁移价值——将物理歧义参数化为概率分布、再用退火与自一致性蒸馏转回确定性重建，这套思路可迁移到其他低质量/高散射成像场景。

5. **DR-VLA 与 LynxScenes 二选一（视兴趣）**：若关注跨域数据迁移选 DR-VLA（域不变场景表示 + 流匹配动作专家 + 10000 小时网络视频预训练）；若关注真实机器人多任务基准选 LynxScenes（833.6 小时、3294.7 公里、20.82M 有向 3D 框）。两者共同说明具身数据正从“小规模遥操作”走向“大规模真实采集 + 网络视频利用”。

#### 可能的研究机会

- **大规模重建的“可更新性”与“误差界”结合**：WorldRecon 与 CityCode 都强调持久状态与更新，PLEDGE 提供逐图元误差界。可探索：在大规模生成式重建中引入类似 PLEDGE 的可声明容差机制，使分块生成与增量更新具有可验证的几何误差保证。

- **力/触觉世界模型与人类观测数据的对接**：EgoExplorer 提供视觉-运动-触觉对齐的人类数据，ForceWAM 提供力-视觉-动作解耦框架。一个自然空白是：能否用 EgoExplorer 式的触觉观测来预训练 ForceWAM 式的力世界模型，从而减少机器人力数据需求。

- **不完整性感知与共形预测的系统化结合**：Perception Beyond the Visible 提出三类不完整挑战，CoSMO 给出共形预测在语义导航中的一种落地。可跟进：把 belief-centric 4D 表示与共形覆盖集合结合，形成对“证据不完整 + 传感器可靠性不完整”同时有覆盖率保证的规划框架。

- **3DGS 质量与下游策略可靠性的量化关系**：YUBI-Real2Sim 已开始量化重建质量对 VLA 策略评估排序的影响，但摘要只给出“九项中八项复现排序”。可跟进：建立 3DGS 伪影类型（空洞、漂浮物）与策略失败模式的映射，并据此设计面向策略评估的重建质量标准，而非面向人眼的质量标准。

- **跨形态 affordance 与跨域导航表示的统一**：Cross-Embodiment Affordance Transfer 以机器人几何/约束为条件转换人类 affordance，DR-VLA 用域不变场景表示

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-15T12:57:09-04:00
**Total number of papers:** 68
**Number of papers added in the latest update:** 26
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

#### 2026-10-13 - 4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling

**Authors:** Jianhui Zhang, Zuyao Lin, Pengxin Xu, Jingdong Wang, Xingyu Chen
**Links:** [abs](https://arxiv.org/abs/2610.17625) - [pdf](https://arxiv.org/pdf/2610.17625)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, novel view synthesis, view synthesis, rendering, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling
- 作者：Jianhui Zhang, Zuyao Lin, Pengxin Xu, Jingdong Wang, Xingyu Chen
- 出版日期：2026-10-13T02:47:58Z
- 分类：主分类 Geometry Foundation Models；次分类 Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.17625 ；PDF https://arxiv.org/pdf/2610.17625

### 一句话总结
论文提出 4LC，一种绑定多视觉编码器表示到共享几何与运动的 4D 潜在缓存，通过灵活的时空访问接口直接复用动静内容的视觉表示，从而避免逐请求的 RGB 渲染与重编码，并以此构建 4LC-Video 支持多类视频生成任务。

### 研究问题
动态世界建模中的视频生成，需要把已观测的静态与动态内容高效复用于不同时间与视角下的重复生成条件。摘要指出存在的问题是：条件获取效率不足，以及如何为多样下游任务提供统一的、可控制的条件形式。

### 核心思路/方法
4LC 的设计包含三方面：
1. **作为潜在缓存**：直接复用静态与动态内容的视觉表示来提供生成条件，避免逐请求的 RGB 渲染与重新编码。
2. **作为复合缓存**：将来自多个视觉编码器（如 VAE、DINO、V-JEPA、VGGT）的视觉表示绑定到共享的几何与运动上，使复合表示能以丰富信息描述动态世界。
3. **灵活时空接口**：可在独立指定的时间与视角直接读取缓存，并组合跨观测的读出结果，为多样下游任务提供统一的条件格式。

在此之上构建 4LC-Video，通过源观测、时空请求与历史复用三者的不同配置来覆盖多种视频生成任务，包括相机控制、时间控制、新视角合成、场景重访与长期生成。

### 主要贡献
- 提出 4LC 这一 4D 潜在缓存，兼具潜在缓存与复合缓存双重角色，直接复用视觉表示以替代 RGB 渲染与重编码。
- 设计将多编码器表示绑定到共享几何与运动的机制，使复合表示能更丰富地描述动态世界。
- 设计灵活的时空访问接口，支持在独立指定的时间与视角读取并组合缓存读出，形成统一条件格式。
- 基于 4LC 构建 4LC-Video，用同一模型、无需任务特定微调即可处理相机控制、时间控制、新视角合成、场景重访与长期生成等任务。
- 摘要报告实验显示：条件获取更高效、时空可控性有效、跨任务场景一致性良好。

### 局限性
摘要未提供足够信息。摘要未给出方法的失败情形、计算或存储开销的定量边界、所依赖的编码器或数据集范围、评测指标细节与消融结论，也未说明长期生成中的误差累积或一致性维持上限。

### 阅读优先级
中。理由：论文属于动态世界建模与视频生成的交叉方向，核心思路（4D 潜在缓存 + 多编码器复合表示 + 统一时空接口）对场景表示、渲染与具身/机器人应用相关研究有潜在参考价值；但摘要未提供实验细节与定量结果，且发表于 2026 年，实际影响与可复现性需进一步核实，因此不宜直接列为高优先级。

</details>

<details>
<summary>Abstract</summary>

For video generation in dynamic world modeling, observed static and dynamic content should be efficiently reused to provide conditions for repeated generation at different times and viewpoints. We introduce 4LC, a 4D latent cache with composite visual representations and a flexible spatiotemporal access interface. As a latent cache, 4LC directly reuses visual representations of static and dynamic content to provide generation conditions, avoiding per-request RGB rendering and re-encoding. As a composite cache, 4LC binds visual representations from multiple visual encoders (e.g., VAE, DINO, V-JEPA, VGGT) to shared geometry and motion, allowing the composite representations to describe the dynamic world with rich information. Besides, we design a flexible spatiotemporal interface, which directly reads the cache at independently specified times and viewpoints and combines readouts across observations, providing a common conditioning format for diverse downstream tasks. Building on 4LC, we develop 4LC-Video to address multiple video generation tasks through different configurations of source observations, spatiotemporal requests, and historical reuse, including camera control, temporal control, novel-view synthesis, scene revisits, and long-term generation. Our experiments show more efficient condition acquisition, effective spatiotemporal controllability, and scene consistency across tasks using a single 4LC-Video model without task-specific fine-tuning.

</details>

#### 2026-10-12 - The Midas Touch for Metric Depth: Interpretable Metricization for Generalizable Depth Perception

**Authors:** Mengtan Zhang, Yu Ma, Shiqi Jiang, Yi Feng, Wei Ye, Xieyuanli Chen, Hanli Wang, Qijun Chen, Rui Fan
**Links:** [abs](https://arxiv.org/abs/2610.16749) - [pdf](https://arxiv.org/pdf/2610.16749)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Midas Touch for Metric Depth: Interpretable Metricization for Generalizable Depth Perception
- 作者：Mengtan Zhang, Yu Ma, Shiqi Jiang, Yi Feng, Wei Ye, Xieyuanli Chen, Hanli Wang, Qijun Chen, Rui Fan
- 出版日期：2026-10-12T13:18:40Z
- 分类：主分类为 Geometry Foundation Models；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.16749 ；PDF https://arxiv.org/pdf/2610.16749

### 一句话总结
论文提出 MTDv2，一个结合显式深度度量化和数据驱动度量深度细化的混合框架，用于从单目相对深度估计中恢复具有泛化能力的度量深度。

### 研究问题
单目相对深度估计的基础模型在泛化性上已有显著提升，但从中恢复准确的度量深度仍然困难，主要受尺度模糊和局部度量尺度不一致影响。现有方法要么使用显式全局仿射变换算法，无法适应空间变化的相对深度到度量深度关系；要么使用隐式数据驱动深度补全网络，对稀疏观测分布敏感，并且可能无法充分利用可泛化的相对深度先验。

### 核心思路/方法
论文在先前工作 MTD 基础上提出 MTDv2，采用混合度量深度感知框架，将显式深度度量化和数据驱动度量深度细化结合。显式深度度量ization 通过分段仿射变换恢复空间变化的度量尺度，同时保留相对深度的几何结构；随后进行逐像素深度细化，沿累积几何变化最小的路径传播度量观测。数据驱动深度细化进一步将显式单路径深度传播扩展为可学习的多路径形式，并保持其可解释性。

### 主要贡献
- 提出 MTDv2，一个结合显式深度度量化和数据驱动度量深度细化的混合度量深度感知框架。
- 设计显式深度度量ization 过程：通过分段仿射变换恢复空间变化度量尺度，并保留相对深度几何结构。
- 引入逐像素深度细化，沿最小累积几何变化路径传播度量观测。
- 将显式单路径深度传播扩展为可学习的多路径形式，同时保持可解释性。
- 在 16 个公开数据集上进行大量实验，展示 MTDv2 在不同稀疏观测来源和不同深度估计范式下的鲁棒、可泛化深度尺度恢复能力，以及对下游 3D 感知任务的广泛适用性。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算开销、对特定数据类型的依赖、多路径学习带来的额外复杂性或实验中的负面结果。摘要仅提及了现有方法的问题和本方法的优势，未系统讨论自身局限。

### 阅读优先级
高。理由：该论文聚焦单目相对深度到度量深度的泛化恢复问题，属于几何基础模型与 3D 感知的重要方向；摘要明确给出方法设计、可解释性动机、16 个公开数据集实验以及下游任务适用性，信息密度较高，适合优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent foundation models have drastically improved the generalization of monocular relative depth estimation, yet recovering accurate metric depth from their estimates for depth perception tasks remains challenging due to scale ambiguity and local metric-scale inconsistency. Existing approaches recover metric depth from sparse observations using either explicit global affine transformation algorithms or implicit data-driven depth completion networks. The former cannot accommodate spatially varying relative-to-metric relationships, while the latter are sensitive to the distribution of sparse observations and may not fully exploit generalizable relative depth priors. To simultaneously address these issues, this study extends our previous work MTD and proposes MTDv2, a hybrid metric depth perception framework that combines explicit depth metricization with data-driven metric depth refinement. The explicit depth metricization process performs segment-wise affine transformations to recover spatially varying metric scales while preserving the geometric structure of relative depth, followed by pixel-wise depth refinement that propagates metric observations along paths with minimal accumulated geometric variation. The data-driven depth refinement process subsequently extends the explicit single-path depth propagation to a learnable multi-path formulation while preserving its interpretability. Extensive experiments conducted on 16 public datasets demonstrate the robust and generalizable depth scale recovery capability of MTDv2 across diverse sources of sparse observations and different depth estimation paradigms, as well as its broad applicability to downstream 3D perception tasks. Code will be publicly available at https://mias.group/MTD upon publication.

</details>

#### 2026-10-12 - Dense Endoluminal Mapping and Localisation from Monocular Bronchoscopy

**Authors:** Salvatore Esposito, Matias Mattamala, Daniel Rebain, Liang Zhao, Kev Dhaliwal, Mohsen Khadem, Subramanian Ramamoorthy
**Links:** [abs](https://arxiv.org/abs/2610.16570) - [pdf](https://arxiv.org/pdf/2610.16570)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** MASt3R, SLAM, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dense Endoluminal Mapping and Localisation from Monocular Bronchoscopy
- 作者：Salvatore Esposito, Matias Mattamala, Daniel Rebain, Liang Zhao, Kev Dhaliwal, Mohsen Khadem, Subramanian Ramamoorthy
- 出版日期：2026-10-12T10:50:30Z
- 分类：主分类 Geometry Foundation Models；次分类：摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2610.16570 ；PDF https://arxiv.org/pdf/2610.16570

### 一句话总结
本文提出一种仅依赖单目 RGB 视频的单目 SLAM 系统，用于支气管镜尖端定位与气道表面重建，无需电磁跟踪器或术前 CT。

### 研究问题
支气管镜检查通过气道插入相机以诊断腔内疾病。摘要指出，沿气道定位相机通常需要额外设备，例如电磁跟踪器和术前 CT 扫描。本文研究的问题是：能否仅利用单目相机视频流来定位支气管镜，而不依赖额外传感设备。

### 核心思路/方法
论文提出一个单目 SLAM 系统，仅从 RGB 视频定位支气管镜尖端并重建其周围气道表面。方法包含以下要点：
- 使用 Depth Anything 3 作为骨干网络，并在超过一百万张真实感气道渲染图上进行微调，输出度量级逐像素深度，且该深度是系统唯一的尺度来源。
- 使用 DINOv3 特征，经自定义交叉注意力匹配器，在经典描述子失效的黏膜区域提供亚像素对应。
- 将上述视觉因素与来自投影迭代最近点（ICP）配准的稠密约束一起放入因子图；该 ICP 配准针对系统自身正在运行的建图结果，从而利用表面证据稳定视觉因素弱可观测的方向。

### 主要贡献
- 提出一种无需额外传感、仅用单目 RGB 视频的支气管镜定位与气道表面重建方案。
- 构建了以微调 Depth Anything 3 提供唯一尺度来源、以 DINOv3 交叉注意力匹配器提供黏膜亚像素对应、并结合针对自身运行重建的投影 ICP 稠密约束的因子图系统。
- 在六个由患者 CT 扫描渲染的气道上进行评估：系统达到 26.1 mm 平均绝对轨迹误差和 77.5% 平均表面 F-score；其平均表面精度超过五个近期单目 SLAM 与前馈基线。
- 与 MASt3R-SLAM 相比：后者对真值拟合自由尺度，平均轨迹误差更低（22.0 mm）。
- 与 ORB-SLAM3 相比：后者仅完成六条气道中的两条，而本系统完成全部六条，并额外重建了两个离体样本。

### 局限性
- 摘要未提供足够信息说明方法对真实临床环境、不同设备或不同患者的泛化能力。
- 摘要未提供足够信息说明系统在非渲染真实视频上的表现；评估主要在六个由患者 CT 扫描渲染的气道上进行。
- 摘要未提供足够信息说明计算成本、实时性或内存需求。
- 摘要未提供足够信息说明对深度骨干微调数据与真实气道域差异的敏感性。
- 摘要提到 MASt3R-SLAM 的平均轨迹误差更低（22.0 mm），但未提供足够信息说明该比较在尺度处理上的公平性细节。
- 摘要未提供足够信息说明离体样本重建的定量结果。

### 阅读优先级
中。理由：该工作聚焦单目支气管镜定位与稠密气道重建，问题明确，方法组合具有针对性，且在摘要中给出了轨迹误差、表面 F-score 以及与多个基线的比较；但若关注真实临床部署、实时性能或非渲染数据验证，摘要未提供足够信息，需要进一步阅读全文才能判断。

</details>

<details>
<summary>Abstract</summary>

Bronchoscopy inserts a camera through the airways to diagnose endoluminal disease. Locating the camera along the airway usually requires additional equipment, such as an electromagnetic tracker and a preoperative CT scan. In this paper, we investigate the use of the monocular camera stream to localise the bronchoscope without requiring additional sensing. We introduce a monocular SLAM system that localises the tip of a bronchoscope and reconstructs the airway surface around it from RGB video alone. A Depth Anything 3 backbone, fine-tuned on over a million photorealistic airway renderings, returns metric per-pixel depth and is the system's only source of scale. DINOv3 features routed through a custom cross-attention matcher supply sub-pixel correspondences on mucosa where classical descriptors fail. Both enter a factor graph alongside a dense constraint from projective iterative closest point (ICP) registration against the system's own running reconstruction, so surface evidence stabilises the directions the visual factors leave weakly observable. On six airways rendered from patient CT scans, the system reaches 26.1 mm mean absolute trajectory error and 77.5% mean surface F-score. Its mean surface accuracy exceeds that of five recent monocular SLAM and feed-forward baselines. MASt3R-SLAM, which fits a free scale to the ground truth, has a lower mean trajectory error (22.0 mm). ORB-SLAM3 completes only two of the six airways, whereas our system completes all six and also reconstructs two ex vivo specimens.

</details>

#### 2026-10-12 - Recovering from Pose-Selection Failures in Repeated Visual Localization

**Authors:** Jaehyun Kim, Wonseok Kang, Tae-Wan Kim
**Links:** [abs](https://arxiv.org/abs/2610.16409) - [pdf](https://arxiv.org/pdf/2610.16409)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** MASt3R, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Recovering from Pose-Selection Failures in Repeated Visual Localization
- 作者：Jaehyun Kim, Wonseok Kang, Tae-Wan Kim
- 出版日期：2026-10-12T08:45:21Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.16409 ；PDF https://arxiv.org/pdf/2610.16409

### 一句话总结
针对重复结构导致视觉定位选错位姿候选的问题，论文提出 History-Guided Pose Reselection（HPR），利用最多五次历史定位输出所做的粗略位置预测，来在相互分离的当前查询候选之间重新选择，从而在不做位姿精修的前提下挽回部分失效。

### 研究问题
重复结构可能使错误位姿候选获得比正确候选更多的内点支持，导致视觉定位系统选中错误位姿。论文关注的是这种“位姿选择失败”的恢复问题，而非直接改进候选生成或位姿精修。

### 核心思路/方法
HPR 使用最多五次过去定位输出得到的粗略位置预测，来区分当前查询中彼此分离较好的候选。最佳拟合预测提出一个替代候选；仅当所有拟合良好的预测都明显更接近该替代候选、而非定位器原本给出的位姿时，HPR 才接受该替代。HPR 不依赖里程计，且返回所选候选本身而不改变它，即用预测做“选择”而非“位姿精修”。

### 主要贡献
- 提出 History-Guided Pose Reselection（HPR），利用历史定位输出进行候选重新选择，以恢复重复结构引发的位姿选择失败。
- HPR 无需里程计，且不修改候选位姿，仅做选择层面的干预。
- 在 Hierarchical Localization（HLoc）、基于 MASt3R 的位姿生成和基于 JIST 的检索共 12 个主要配置中，使用一个开发集阈值，HPR 在 5 米和 10 度内提升召回，且在不到 0.4% 的查询上损失成功案例。
- 在 NAVER Gangnam B1 上，HPR 纠正 97 个 HLoc 失败并损失 6 个成功案例；在三个 HLoc 测试集上，增益在 0.25 米和 2 度内持续存在。
- HLoc 候选上的 HPR 运行时间中位数低于 1 毫秒（不含位姿生成）。

### 局限性
- 恢复效果在定位频率较低时会减弱。
- 摘要未提供足够信息说明在非重复结构、其他数据集或更复杂场景下的表现。
- 摘要未提供足够信息说明 HPR 对历史输出质量、初始定位失败模式或超参数选择的敏感性。
- 摘要未提供足够信息说明运行时间在不同候选生成方法上的完整对比或端到端系统开销。

### 阅读优先级
高。理由：该工作直接针对视觉定位中重复结构导致的位姿选择失败，方法轻量（无需里程计、不修改候选、运行时间中位数低于 1 毫秒），且在多个主要配置和真实场景上报告了召回提升与较低成功损失，对机器人、AR 等具身应用中的鲁棒定位具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Repetitive structures can give an incorrect pose candidate more inlier support than an accurate one, causing visual localization to select it. History-Guided Pose Reselection (HPR) uses coarse position forecasts from up to five past localization outputs to distinguish well-separated current-query candidates. The best-fitting forecast proposes an alternative; HPR accepts it only if every well-fitting forecast is much closer to it than to the localizer's pose. HPR needs no odometry and returns the selected candidate unchanged, using prediction for selection rather than pose refinement. With one development-set threshold, HPR improves recall within 5 meters and 10 degrees in all 12 main configurations of Hierarchical Localization (HLoc), MASt3R-based pose generation, and JIST-based retrieval, losing successes on fewer than 0.4 percent of queries. On NAVER Gangnam B1, HPR corrects 97 HLoc failures and loses six successes; gains persist within 0.25 meters and 2 degrees on all three HLoc test sets. Median HPR runtime on HLoc candidates is below one millisecond, excluding pose generation. Recovery weakens under less frequent localization.

</details>

#### 2026-10-12 - Graph3R: Unifying View Graph Initialization with Feed-Forward Reconstruction

**Authors:** Jingwen Yu, Hengli Wang, Jianhao Jiao, Zhonghang Liu, Ping Tan, Hong Zhang
**Links:** [abs](https://arxiv.org/abs/2610.16272) - [pdf](https://arxiv.org/pdf/2610.16272)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, pose estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Graph3R: Unifying View Graph Initialization with Feed-Forward Reconstruction
- 作者：Jingwen Yu, Hengli Wang, Jianhao Jiao, Zhonghang Liu, Ping Tan, Hong Zhang
- 出版日期：2026-10-12T06:50:08Z
- 分类：主分类为 Geometry Foundation Models；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.16272 ；PDF https://arxiv.org/pdf/2610.16272

### 一句话总结
Graph3R 通过共享多视图几何表征，将视图图初始化与馈送式重建统一起来，从而在未筛选图像集合中区分不同场景并分别重建，同时提升视图关联与重建质量。

### 研究问题
论文关注的问题是：馈送式重建通常假设输入图像来自单一场景，但实际中未筛选的图像集合可能包含来自互不相干场景的视图。若将这些视图联合重建，会破坏相机位姿和几何结果。已有流程一般在最终重建前以独立阶段处理视图关联，导致视图图初始化与重建推断之间耦合较弱。

### 核心思路/方法
Graph3R 的核心是用共享几何表征统一视图图初始化与馈送式重建。方法使用一个轻量验证头，从 $π^3$ 的多视图特征中预测成对共视性，从而构建视图图。该图将输入视图分类为不同场景组。对于每个组，在解码相机位姿和稠密几何之前，对共享特征进行掩码处理。由于复用了多视图特征，Graph3R 可以用单次主干前向传播分别重建互不相干的场景。

### 主要贡献
- 提出 Graph3R，将视图图初始化与馈送式重建通过共享几何表征统一起来。
- 设计轻量验证头，从 $π^3$ 的多视图特征预测成对共视性并构建视图图，用于将输入视图分为场景组。
- 在每个场景组内通过掩码共享特征后再解码相机位姿和稠密几何，实现单次主干传播下对多个互不相干场景的分别重建。
- 在三个基准上，相比基线，在 100% 精确率下的平均最大召回率提升最多 8.99 个百分点，并改善混合场景输入的重建质量。
- 在多会话建图任务中，改善跨会话定位，取得有竞争力的位姿估计精度，并在重建查询组时相对基线实现约 35.9 倍运行时加速。

### 局限性
摘要未提供足够信息。摘要未说明方法在何种场景类型、图像规模、噪声条件或计算资源限制下的失败情况，也未提供消融实验、误差来源或泛化边界的详细信息。

### 阅读优先级
高。理由：该论文针对未筛选图像集合中多场景混合导致重建失败的实际问题，提出将视图关联与重建推断更紧密耦合的统一框架；摘要报告了在多个基准、多会话建图任务以及运行时效率上的改进，主题与几何基础模型和馈送式重建方向高度相关，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward reconstruction recovers camera poses and dense geometry from image sets whose views are assumed to come from a single scene. In practice, uncurated image collections often contain views from disjoint scenes, and reconstructing these views jointly can corrupt camera poses and geometry. Existing pipelines typically resolve view associations in separate stages before final reconstruction, leaving view graph initialization and reconstruction inference only loosely coupled. We introduce Graph3R, which unifies view graph initialization with feed-forward reconstruction through a shared geometric representation. A lightweight verification head predicts pairwise covisibility from the multi-view features of $π^3$ to construct a view graph. This graph classifies the input views into scene groups. For each group, we mask the shared features before decoding camera poses and dense geometry. Reusing the multi-view features allows Graph3R to reconstruct disjoint scenes separately with a single backbone pass. Across three benchmarks, Graph3R improves average maximum recall at 100% precision by upto 8.99 percentage points over the baseline, while improving reconstruction quality on mixed-scene inputs. Regarding the multi-session mapping task, Graph3R improves cross-session localization and achieves competitive pose estimation accuracy, while delivering a runtime speedup of approximately $35.9\times$ over the baseline when reconstructing the query group. By integrating learned view association with geometric inference, our approach takes a step toward end-to-end reconstruction from uncurated image collections.

</details>

#### 2026-10-12 - All-St3R SLAM: Real-time RGB Dynamic SLAM with Pixel-wise Motion Masking

**Authors:** Yewon Kim, Paul Hongsuck Seo, Sang Chul Ahn
**Links:** [abs](https://arxiv.org/abs/2610.16143) - [pdf](https://arxiv.org/pdf/2610.16143)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** DUSt3R, simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：All-St3R SLAM: Real-time RGB Dynamic SLAM with Pixel-wise Motion Masking
- 作者：Yewon Kim, Paul Hongsuck Seo, Sang Chul Ahn
- 出版日期：2026-10-12T04:04:33Z
- 分类：Geometry Foundation Models（主）；3D Reconstruction & Multi-view Geometry（次）
- 链接：[摘要](https://arxiv.org/abs/2610.16143)｜[PDF](https://arxiv.org/pdf/2610.16143)

### 一句话总结
论文提出一种仅依赖 RGB 输入的实时动态 SLAM 框架，通过结合 DUSt3R 的自运动预测与 All-Tracker 的点跟踪，在像素级上剔除真正运动的像素，以缓解现有动态 SLAM 的过度移除与高计算成本问题。

### 研究问题
动态环境下的 SLAM 具有重要实用价值，但现有动态 SLAM 方法存在若干局限：过度移除（over-removal）与较高的计算成本。论文旨在解决这些问题。

### 核心思路/方法
- 提出一个实时 RGB 动态 SLAM 框架，在像素级精确移除运动物体，且不依赖预定义标签或分割模型。
- 系统结合由 DUSt3R 基于自运动（ego-motion）预测的像素运动，以及来自 All-Tracker 的点跟踪。
- 通过分析这两种运动来源之间的差异，仅移除实际正在运动的像素。
- 与对象级掩码方法不同，该方法只剔除当前正在运动的区域，使暂时静止的部分仍可用于跟踪。
- 系统运行速度约为 10 FPS；通过对 30 FPS 标准视频流每 3 帧进行子采样，实现实时性能。
- 仅依赖 RGB 输入。

### 主要贡献
- 提出一种不依赖预定义标签或分割模型的像素级运动掩码动态 SLAM 框架。
- 通过融合 DUSt3R 自运动预测与 All-Tracker 点跟踪的差异，实现只移除实际运动像素。
- 相较当前最先进的密集动态 SLAM 方法（0.5–3 FPS），显著提升运行速度（约 10 FPS），提供更具实用性的方案。
- 仅使用 RGB 输入，避免额外模态依赖。

### 局限性
- 摘要未提供足够信息：具体的定位与建图精度指标、在各类动态场景下的定量对比结果、失败案例或适用边界。
- 摘要未提供足够信息：子采样策略（每 3 帧）对精度与鲁棒性的具体影响。
- 摘要未提供足够信息：对 DUSt3R 与 All-Tracker 误差的敏感性分析或消融实验。
- 摘要未提供足够信息：与基线方法在计算资源、内存占用等方面的详细比较。

### 阅读优先级
高。理由：该论文聚焦动态 SLAM 中的过度移除与高计算成本两个实际痛点，提出像素级运动掩码且仅用 RGB 输入，报告约 10 FPS 的实时性能，明显优于摘要所述的最先进密集动态 SLAM（0.5–3 FPS）；同时涉及 DUSt3R 与 All-Tracker 的组合，属于几何基础模型与 3D 重建交叉方向，具有较高的实践与方法参考价值。

</details>

<details>
<summary>Abstract</summary>

SLAM (Simultaneous Localization and Mapping) is a core technology in autonomous systems that enables them to estimate their own position and build a map of unknown environments simultaneously. SLAM systems in dynamic environments are of great practical importance. However, existing dynamic SLAM approaches still have several limitations like over-removal and high computational costs. To address these limitations, we propose a real-time RGB Dynamic SLAM framework that precisely removes moving objects at the pixel level without relying on predefined labels or segmentation models. Our system combines pixel motion predicted by ego-motion using DUSt3R with point tracking from All-Tracker, removing only actually moving pixels by analyzing discrepancies between the two motion sources. Unlike object-level masking methods, our approach eliminates only currently moving regions, allowing temporarily static parts to be utilized for tracking. Operating at approximately 10 FPS, the system achieves real-time performance on standard 30 FPS video streams by subsampling every 3 frames. Relying solely on RGB inputs, this significantly improves upon state-of-the-art dense dynamic SLAM approaches (0.5-3 FPS), presenting a highly practical solution.

</details>

#### 2026-10-08 - Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching

**Authors:** Luping Liu, Bingyi Kang, Yifan Wang, Dong Xu
**Links:** [abs](https://arxiv.org/abs/2610.12421) - [pdf](https://arxiv.org/pdf/2610.12421)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** dense correspondence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching
- 作者：Luping Liu, Bingyi Kang, Yifan Wang, Dong Xu
- 出版日期：2026-10-08T17:53:04Z
- 分类：Geometry Foundation Models
- 链接：摘要链接 https://arxiv.org/abs/2610.12421 ；PDF 链接 https://arxiv.org/pdf/2610.12421

### 一句话总结
论文提出 FreeMatching，一个结合生成式与语义基础表示、并使用异构监督的稠密对应匹配框架，旨在突破传统时空先验假设，在保持视觉身份的变换下实现可泛化的对应匹配。

### 研究问题
稠密对应匹配长期受限于简化时空先验，例如平滑运动和刚性几何。这些假设对经典任务是有效的，但在图像编辑和参考引导生成（IEG）中会失效，因为这类变换可能保持视觉身份却破坏物理连续性。论文关注的核心问题是：如何在上述变换下建立保持身份的对应关系。

### 核心思路/方法
论文提出 FreeMatching，一个可泛化框架，其核心组成包括：
- 结合生成式和语义基础表示；
- 使用来自经典数据集、跟踪视频和合成场景的异构监督；
- 通过教师引导的迭代细化，在 IEG 场景中无需稠密对应标注即可改进对应匹配。

### 主要贡献
- 提出 FreeMatching，用于跨破坏物理连续性的变换建立保持身份的稠密对应匹配。
- 融合生成式与语义基础表示，并利用经典数据集、跟踪视频和合成场景的异构监督。
- 引入教师引导的迭代细化机制，使模型在 IEG 中无需稠密对应标注也能提升对应质量。
- 实验表明，单一 FreeMatching 模型在具有挑战性的 IEG 图像对上显著提升对应质量，同时在经典基准上保持有竞争力的性能。
- 展示其可作为评估身份保持的定量指标，且得分与人类判断相关。
- 代码已公开：https://github.com/luping-liu/FreeMatching 。

### 局限性
摘要未提供足够信息。摘要中未说明方法在何种条件下失败、计算成本、对特定数据分布或任务类型的依赖、以及定量指标与人类判断相关性的具体程度等局限。

### 阅读优先级
中。理由：该论文关注稠密对应匹配在图像编辑与参考引导生成中的泛化问题，问题设定明确，并提出无需稠密对应标注的教师引导迭代细化与统一评估指标，具有一定方法与评测价值；但摘要未给出具体实验细节、数据集构成与定量结果，是否值得深入阅读取决于读者对 IEG 对应匹配、基础模型结合或身份保持评估的兴趣。

</details>

<details>
<summary>Abstract</summary>

Dense correspondence matching has historically been bounded by simplifying spatio-temporal priors, such as smooth motion and rigid geometry. While effective for classical tasks, these assumptions break down in image editing and reference-guided generation (IEG), where transformations can preserve visual identity while breaking physical continuity. To establish identity-preserving correspondence across such transformations, we introduce FreeMatching, a generalizable framework combining generative and semantic foundation representations with heterogeneous supervision from classical datasets, tracked videos, and synthetic scenes. Teacher-guided iterative refinement further improves correspondence in IEG without dense correspondence annotations. Experimentally, a single FreeMatching model substantially improves correspondence quality on challenging IEG image pairs while retaining competitive performance on classical benchmarks. Furthermore, we demonstrate its utility as a quantitative metric for evaluating identity preservation, with scores that correlate with human judgment. The code is available at https://github.com/luping-liu/FreeMatching.

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-14 - DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning

**Authors:** Qihang Cao, Haoyuan Li, Zihan Guo, Sensen Gao, Zihui Gao, Huixin Zhang, Fan He, Jianhua Han, Hang Xu, Xiaodan Liang, Jia-Wang Bian
**Links:** [abs](https://arxiv.org/abs/2610.20598) - [pdf](https://arxiv.org/pdf/2610.20598)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 4D, spatial intelligence

<details>
<summary>Abstract</summary>

Achieving general spatial intelligence requires a unified understanding of both static 3D and dynamic 4D. However, we find that existing models struggle to excel at both: 3D post-training can weaken dynamic understanding, while 4D-specialized models often lack strong static 3D reasoning. Our analysis reveals that this spatial--dynamic interference is highly non-uniform across parameter groups, with the balance between static and dynamic capabilities particularly sensitive to changes in late-layer MLPs. To address this interference, we propose DynThinker, a unified framework for jointly strengthening static and dynamic spatial reasoning. Decoupled Exponential Moving Average (D-EMA) applies configurable group-wise averaging to constrain drift in interference-sensitive pretrained parameters while preserving flexibility for capability enhancement. Spatial-Dynamic Fusion (SDF) complements D-EMA by selectively integrating spatial and temporal priors from a dynamic geometry encoder into intermediate VLM representations under semantic guidance. Across ten metrics spanning nine static 3D and dynamic 4D benchmarks, DynThinker achieves the highest average score among all evaluated models. Notably, DynThinker achieves 56.0 on ReVSI, 67.2 on DSR-Bench, and 51.2 and 40.1 under the sample-wise and group-wise evaluation protocols of DSI-Bench, respectively, setting new state-of-the-art results among the compared open-source models across all four evaluations within a unified model.

</details>

#### 2026-10-14 - DD-GBP: Anytime Multi-Arm Planning and Continuous Execution via Distributed Dynamic Gaussian Belief Propagation

**Authors:** Zhao Jin, Fengyi Dai, Yuetong Yin, Yunan Wang, Wenjie Chen, Chuxiong Hu
**Links:** [abs](https://arxiv.org/abs/2610.20460) - [pdf](https://arxiv.org/pdf/2610.20460)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian

<details>
<summary>Abstract</summary>

Safely executing long-horizon multi-arm tasks online in complex dynamic environments remains challenging. We propose a new distributed dynamic Gaussian belief propagation (DD-GBP) method that directly plans joint-space trajectories through parallel local inference. A unified Gaussian-process (GP) parameterization connects adaptive planning horizons, interpolation-time factors, and continuous execution. Each robot maintains a local tree-structured factor graph and exchanges messages asynchronously over active inter-arm links. Dynamic subnet reconstruction and event-triggered updates reduce communication and inference costs while responding to moving obstacles. We also provide theoretical analyses of local inference accuracy, anytime early stopping, triggered-replanning consistency, and GP-consistent execution. In 50 long-horizon, multi-target four-arm scenes with moving obstacles, DD-GBP achieves $92.5\%$ collision-free all-target completion and the highest success rate among six representative baselines. Scenario ablations demonstrate long-horizon safety and robustness to communication impairment and extreme conditions; success remains $86.0\%$ under $90\%$ packet loss. Execution results further show substantially suppressed extreme velocity and acceleration peaks relative to Syn-GBP. On one workstation, obstacle-free tests with 30 coexisting arms retain $99.87\%$ success and a $15.80$ ms mean warm solve, exceeding 60 Hz and outperforming the compared methods in scalability. Dual-arm transport experiments under dynamic interference demonstrate online response and practical deployability. To the best of our knowledge, these results establish a new state of the art for online long-horizon multi-arm planning in dynamic scenes.

</details>

#### 2026-10-13 - Perceptual Characterization of Scan-induced Artifacts in Dynamic 3D Meshes

**Authors:** Huong Hoang, Truong Nguyen, Pamela Cosman
**Links:** [abs](https://arxiv.org/abs/2610.19173) - [pdf](https://arxiv.org/pdf/2610.19173)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D

<details>
<summary>Abstract</summary>

Dynamic meshes reconstructed from real-world scenes often exhibit scan-induced artifacts such as surface jitter and missing geometry, which strongly impact perceived visual quality. Objective assessment remains challenging due to the absence of artifact-free ground truth and limited perceptual understanding of artifact interactions. This paper presents a systematic and controlled perceptual study of scan-induced artifacts in dynamic meshes, focusing on surface jitter and holes. To enable systematic analysis, we introduce a physically grounded artifact synthesis framework in which holes are synthesized using a reconstruction uncertainty model derived from multi-view geometry. The study reveals asymmetric cross-artifact interactions, non-additive integration, and motion-dependent temporal masking. Based on these findings, we propose a compact, perceptually grounded no-reference quality assessment framework that encodes the observed perceptual mechanisms.

</details>

#### 2026-10-13 - PUGS: Physics-Guided Uncertainty Modeling for Underwater Dynamic 3D Gaussian Splatting

**Authors:** Tingjun Li, Yuxi Wang, Guoqiang Zhong, Zhaoxiang Zhang
**Links:** [abs](https://arxiv.org/abs/2610.17936) - [pdf](https://arxiv.org/pdf/2610.17936)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PUGS: Physics-Guided Uncertainty Modeling for Underwater Dynamic 3D Gaussian Splatting
- 作者：Tingjun Li, Yuxi Wang, Guoqiang Zhong, Zhaoxiang Zhang
- 出版日期：2026-10-13T08:21:10Z
- 分类：Dynamic / 4D Reconstruction（主类）；Neural Scene Representations & Rendering（次类）
- 链接：[摘要](https://arxiv.org/abs/2610.17936) / [PDF](https://arxiv.org/pdf/2610.17936)

### 一句话总结
PUGS 将水下成像引入的物理不确定性显式建模为概率化形变，用于水下动态 3D Gaussian Splatting 的重建。

### 研究问题
现有动态 3DGS 方法大多使用确定性的形变场，假设每个高斯随时间遵循确定的几何轨迹。摘要指出，这一假设在水下环境中失效：光散射、折射、海洋雪和低能见度会在拍摄图像中造成显著的物理歧义，使得确定性形变建模不再适用。

### 核心思路/方法
- 学习水下图像形成过程所诱导的固有不确定性，并将其作为物理信号用于动态场景建模。
- 不估计单一确定性位移，而是将每个高斯的运动参数化为概率分布，包含期望形变与物理不确定性。
- 采用随机形变优化，通过局部重参数化（local reparameterization）采样高斯轨迹，在训练中探索多个物理上合理的解。
- 提出不确定性随机退火（uncertainty stochastic annealing）与双路径自一致性蒸馏（dual-path self-consistency distillation）目标，将随机探索转化为确定性重建，同时保持时间一致性。

### 主要贡献
- 提出 PUGS，一个面向水下动态 3DGS 的物理引导不确定性模型。
- 将高斯运动从确定性位移扩展为带期望形变与物理不确定性的概率分布。
- 引入随机形变优化、局部重参数化采样、不确定性随机退火与双路径自一致性蒸馏目标。
- 摘要报告在水下动态数据集与物理感知基准上取得更优的渲染质量、时间一致性与重建鲁棒性；在 UVEB 上较最强基线提升 1.16 dB PSNR，在 DRUVA 上提升 3.99 dB。

### 局限性
摘要未提供足够信息。摘要未说明方法的计算开销、对水下成像参数或物理模型的依赖程度、在非水下场景的适用性，也未给出失败案例或消融实验的完整细节。

### 阅读优先级
高。理由：该工作针对水下动态 3DGS 中确定性形变假设失效这一明确问题，提出概率化不确定性与物理引导建模，并在摘要中给出具体定量提升；对动态/4D 重建与神经场景表示方向具有直接相关性。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (3DGS) provides an efficient framework for dynamic scene reconstruction. Most existing approaches model scene dynamics with deterministic deformation fields, assuming each Gaussian follows a distinct geometric trajectory over time. This assumption breaks down underwater, where light scattering, refraction, marine snow and low visibility create substantial physical ambiguity in captured images. We present PUGS, a physics-guided uncertainty model for underwater dynamic 3DGS. PUGS learns inherent uncertainty induced by underwater image formation and leverages it as a physical signal for dynamic scene modeling. Rather than estimating a single deterministic displacement, it parameterizes each Gaussian's motion as a probability distribution with expected deformation and physical uncertainty. We adopt stochastic deformation optimization to sample Gaussian trajectories via local reparameterization, exploring multiple physically plausible solutions during training. We further propose uncertainty stochastic annealing and a dual-path self-consistency distillation objective, converting stochastic exploration to deterministic reconstruction while preserving temporal coherence. Extensive experiments on underwater dynamic datasets and physics-aware benchmarks demonstrate superior rendering quality, temporal consistency and reconstruction robustness. Our method achieves 1.16 dB PSNR gain over the strongest baseline on UVEB and 3.99 dB on DRUVA.

</details>

#### 2026-10-12 - Act4R: Action-conditioned 4D reconstruction for kinematics-free control

**Authors:** Zhaoliang Zhang, Chenhao Yu, Zhimin Shao, Xijun Liu, Cheng Peng
**Links:** [abs](https://arxiv.org/abs/2610.17462) - [pdf](https://arxiv.org/pdf/2610.17462)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, scene flow, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Act4R: Action-conditioned 4D reconstruction for kinematics-free control
- 作者：Zhaoliang Zhang, Chenhao Yu, Zhimin Shao, Xijun Liu, Cheng Peng
- 出版日期：2026-10-12T22:21:16Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2610.17462) / [PDF](https://arxiv.org/pdf/2610.17462)

### 一句话总结
Act4R 提出一种以动作信号为条件的 4D 重建框架，基于 3D 基础模型预测机器人 3D 场景流，并借此实现无需运动学建模的逆控制。

### 研究问题
论文关注如何精确控制不同机器人本体的运动。摘要指出，复杂机器人结构建模通常需要大量时间、专用传感器和人工标注；作者试图探索能否利用从 2D 观测提升得到的 4D 特征，根据动作信号稠密映射机器人的空间运动。

### 核心思路/方法
Act4R 建立在 3D 基础模型之上，用于在给定任意动作时预测机器人的 3D 场景流。方法包含一个 Spatial-Action Encoder，将当前 2D 机器人状态及其动作信号编码为表示未来机器人 3D 状态的嵌入；随后将当前和未来的空间嵌入解码为点图，以估计动作条件下的场景流。为学习动作与未来状态之间的映射，Act4R 在其基于 Transformer 的编码器中引入 spatial-action fusion，并采用 spatial alignment loss 引导编码器进行未来流预测。在给定本体的部分样本上训练后，Act4R 可通过优化信号来实现期望场景流，从而执行逆控制。

### 主要贡献
- 提出 Act4R 框架，基于 3D 基础模型预测给定动作条件下的机器人 3D 场景流。
- 设计 Spatial-Action Encoder，将当前 2D 机器人状态与动作信号编码为未来 3D 状态的嵌入，并解码为点图以估计场景流。
- 在 Transformer 编码器中引入 spatial-action fusion，并使用 spatial alignment loss 引导未来流预测。
- 训练后可通过优化信号执行逆控制，以达成期望的场景流。
- 在公开真实世界数据集和模拟器合成数据上评估，涉及多种机器人平台；摘要称其在场景流预测上优于先前 SoTA，并在逆控制的动作精度指标和模拟闭环控制中表现更好。

### 局限性
摘要未提供足够信息。
（具体局限、失败案例、计算开销、对不同本体的泛化边界、真实世界闭环控制细节、训练样本量要求等均未在摘要中说明。）

### 阅读优先级
中。理由：该工作将 4D 重建、动作条件场景流与无运动学控制联系起来，任务设定清晰，并声称在场景流预测和逆控制上优于先前 SoTA；但摘要未给出具体实验设置、定量结果、真实机器人闭环验证细节与局限性，若关注机器人控制或 4D 表示学习的实际可用性，需要进一步阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

Precise control of movement across various robotic embodiments is a longstanding challenge. Modeling complex robotic structures requires significant time, dedicated sensors, and manual labeling. Recent advancements in 4D representation learning offer an interesting alternative: can we leverage 4D features lifted from 2D observations to densely map a robot's spatial movement based on the action signal? To this end, we propose Act4R, a framework that builds on 3D foundation model to predict a robot's 3D scene flow with any given action. Act4R introduces a Spatial-Action Encoder, which encodes the current 2D robot state and its action signals into embeddings that represent future robot state in 3D. Then, both the current and future spatial embeddings are decoded into point maps to estimate action-conditioned scene flow. To effectively learn the mapping between action and future state, Act4R introduces spatial-action fusion in its transformer-based encoder, and a spatial alignment loss that guides the encoder for future flow prediction. After training on some samples of a given embodiment, Act4R can perform inverse control by optimizing the signal to achieve the desired scene flow. We evaluate Act4R on a public real-world dataset and synthetic data collected in simulator. Experiments on various robotic platforms show that Act4R outperforms the previous SoTA in scene flow prediction. Our method also performs better in inverse control, both on the action accuracy metric and in closed-loop control in simulation.

</details>

#### 2026-10-12 - Physical SLAM: Physics-aware Simultaneous Localisation and Mapping

**Authors:** Guangming Wang, Zhishuo Liu, Haibing Wu, Wanli Ma, Yixiong Jing, Olaf Wysocki, Brian Sheil
**Links:** [abs](https://arxiv.org/abs/2610.17260) - [pdf](https://arxiv.org/pdf/2610.17260)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** dynamic Gaussian, 4D Gaussian, SLAM, rendering, radiance, manipulation, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Physical SLAM: Physics-aware Simultaneous Localisation and Mapping
- 作者：Guangming Wang, Zhishuo Liu, Haibing Wu, Wanli Ma, Yixiong Jing, Olaf Wysocki, Brian Sheil
- 出版日期：2026-10-12T18:18:47Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.17260) / [PDF](https://arxiv.org/pdf/2610.17260)

### 一句话总结
该论文提出 Physical SLAM，一种物理感知的 SLAM 方法，通过将场景分解为静态背景高斯场与由弹簧-质量物理模型驱动的动态物体高斯场，从 RGB-D 图像序列重建可形变物体的 4D 高斯场，并支持在外力作用下的未来状态预测。

### 研究问题
如何从运动相机拍摄的单目视频（摘要中具体实验使用 RGB-D 图像序列）中，联合重建动态高斯辐射场并推断其背后的物理动力学，从而构建物理世界的预测性 4D 表示。具体而言，需要解决视觉观测与物理动力学之间的融合问题，避免模拟节点位置被突兀替换，并使重构出的动力学与观测对齐，同时将外观、几何与物理耦合起来。

### 核心思路/方法
- 场景分解：将场景分为用于相机定位的静态背景高斯场，以及由弹簧-质量物理模型驱动的动态物体高斯场，该物理模型包含弹性形变、惯性和阻尼。
- 虚拟观测力：引入虚拟观测力，逐步将模拟表面节点拉向观测到的深度点，而非突然替换模拟节点位置，从而整合视觉观测与物理动力学。
- 物理参数更新：基于完整重建观测窗口内聚合的模拟误差，更新弹簧-质量模型的物理参数，使重建动力学与观测对齐。
- 物理感知高斯变换与表面对齐：设计物理感知的高斯变换和表面对齐策略，动态高斯沿弹簧-质量模型的形变物理表面进行变换，并在基于渲染的优化过程中被约束为保持与表面一致。
- 输出能力：所得表示支持观测帧渲染和动作条件仿真，将 SLAM 地图扩展为可描述可形变物体如何响应操作。

### 主要贡献
- 提出 Physical SLAM，一种物理感知的 SLAM 方法，用于构建可形变物体的 4D 高斯场并在外部动作下预测其未来状态。
- 设计虚拟观测力机制，实现视觉观测与物理动力学的渐进式融合。
- 通过重建观测窗口聚合模拟误差来更新弹簧-质量模型物理参数。
- 提出物理感知高斯变换与表面对齐策略，耦合外观、几何与物理。
- 在 PhysTwin 基准上，重建和预测 PSNR 分别比 PhysTwin 提升 10.4% 和 11.0%；在 TUM RGB-D 基准上，相比 4DGS-SLAM 平均相机跟踪误差降低 20.6%，SSIM 提升 3.6%，LPIPS 降低 8.3%。

### 局限性
摘要未提供足够信息。仅从摘要无法判断方法在非弹性形变、拓扑变化、实时性能、泛化能力或计算开销等方面的局限。

### 阅读优先级
高。理由：该论文将 SLAM 与物理仿真、可形变物体 4D 高斯表示相结合，并给出在 PhysTwin 和 TUM RGB-D 基准上的定量提升，对动态/4D 重建、神经场景表示及具身/机器人应用方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

To reconstruct a predictive 4D representation of the physical world from monocular video captured by a moving camera, we jointly reconstruct dynamic Gaussian radiance fields and infer their underlying physical dynamics. This paper proposes \emph{Physical SLAM}, a physics-aware method for constructing 4D Gaussian fields of deformable objects and predicting their future state when subjected to external actions, given a sequence of RGB-D images. Our method separates the scene into a static background Gaussian field for camera localization and a dynamic object Gaussian field driven by a spring--mass physical model of elastic deformation, inertia, and damping. To integrate visual observations with physical dynamics, we introduce virtual observation forces that gradually pull simulated surface nodes toward observed depth points, avoiding abrupt replacement of simulated node positions. Meanwhile, the physical parameters of the spring--mass model are updated from simulation errors aggregated over the full reconstruction observation window, enabling the reconstructed dynamics to align with observations. To couple appearance, geometry, and physics, we further design a physics-aware Gaussian transformation and surface alignment strategy, where dynamic Gaussians are transformed along the deforming physical surface of the spring--mass model and constrained to remain aligned with the surface during rendering-based optimization. The resulting representation supports observed-frame rendering and action-conditioned simulation, extending SLAM maps to describe how deformable objects respond to manipulation. On the PhysTwin benchmark, our method improves reconstruction and prediction PSNR over PhysTwin by 10.4\% and 11.0\%, respectively. On the TUM RGB-D benchmark, it reduces average camera tracking error by 20.6\%, improves SSIM by 3.6\%, and reduces LPIPS by 8.3\% compared with 4DGS-SLAM.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-14 - Smart Fusion for Adaptive Visual-IMU Weighting in cuVSLAM Sparse Bundle Adjustment

**Authors:** Wonju Lee, Dara Molloy, Abhilash Nand Kumar, Onias Castelo, Petar Trslic, David Adley, Conor Ferguson, Hesam Rabeti
**Links:** [abs](https://arxiv.org/abs/2610.20226) - [pdf](https://arxiv.org/pdf/2610.20226)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** bundle adjustment

<details>
<summary>Abstract</summary>

In cuVSLAM, visual and inertial measurement unit (IMU) residuals are fused in sparse bundle adjustment (SBA) with a weighting fixed by pre-calibrated noise covariances, leaving no mechanism to adapt the visual-inertial balance at runtime. We introduce a scalar $α\geq1$ that upscales the visual information matrix relative to the IMU preintegration constraint. Across the candidate set $\{1.0,2.0,5.0,10.0,20.0\}$, the resulting trajectories form two empirical performance regimes. The IMU-TRUST regime contains $α\in\{1,2\}$ near the calibrated baseline, while the VISION-TRUST regime contains $α\in\{10,20\}$. The intermediate value $α=5$ is treated as a transition case. Differences within each regime are small relative to those observed between the regimes. This structure motivates reducing $α$-selection to a binary decision. We train a lightweight Visual Quality Estimator (VQE), implemented as a multilayer perceptron with 914 trainable parameters. It maps a 10-dimensional visual quality feature vector assembled from statistics already maintained by the tracker to a per-SBA regime prediction. The proposed method reduces mean RMSE APE by $27.7\%$ and by $14.9\%$ under leave-one-out cross-validation (LOOCV) on EuRoC MAV and TUM-VI Room, respectively.

</details>

#### 2026-10-14 - Why 3D Reconstruction Breaks Down on Under-Ice AUV Video, and How to Predict It

**Authors:** Ana-Ştefania Kogălniceanu, Klára Orbán, Ashwin Nedungadi, Stefan Lüdtke, Kuderna-Iulian Benţa
**Links:** [abs](https://arxiv.org/abs/2610.19993) - [pdf](https://arxiv.org/pdf/2610.19993)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, SfM, feature matching, splatting

<details>
<summary>Abstract</summary>

Reconstruction of 3D structures using under-ice AUV video footage has been inaccurate, although it is not certain whether this is due to shortcomings in the methods or an inherent deficiency of the capture system. We test four different models for reconstruction on the same Antarctic under-ice AUV video (Icefin, Kamb Ice Stream): classical feature matching SfM, differentiable photometric splatting, volumetric depth fusion, and a pose-free feed-forward foundation model. All four fail, each in a distinct way: near-total registration yielding almost no structure, geometrically broken output despite healthy photometric metrics, a persistent coverage artifact, and unstable cross-chunk scale. We show that all four are consistent with the same capture regime, a small camera-baseline-to-scene-depth ratio. Following our analysis, we propose a detection system that flags this type of failure in minutes, rather than hours of wasted compute.

</details>

#### 2026-10-14 - MicroSDF: Microfacet-Driven Hybrid Neural SDFs for Mixed-Reflectance Surface Reconstruction

**Authors:** Lejia Ye, Yuhua Xu, Yulan Guo, Lian Xu, Xiaohu Zhang
**Links:** [abs](https://arxiv.org/abs/2610.19681) - [pdf](https://arxiv.org/pdf/2610.19681)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction, NeRF

<details>
<summary>Abstract</summary>

Accurate 3D reconstruction in real-world environments remains a significant challenge due to the coexistence of reflective and non-reflective surfaces, which pose distinct modeling demands. Existing methods often treat these surface types separately, limiting their generalizability and physical plausibility. To bridge this gap, we propose MicroSDF, a novel neural implicit framework that facilitates geometry and reflectance modeling through microfacet theory. Our approach incorporates three core innovations: (i) a microfacet-guided geometry model that extracts multi-scale surface normals (macroscopic and microfacet) from a signed distance field (SDF), regularized by a proposed microfacet normal consistency loss to enforce physically plausible surface orientations; (ii) an enhanced dual-branch color model, where the specular branch leverages the microfacet normals to model high-frequency reflectance, and the vanilla branch, unlike prior works, uses reflection direction (instead of viewing direction) to better model diffuse and low-frequency specular components; and (iii) a detection-guided color blending strategy that adaptively fuses the color outputs based on reflection priors, providing more physically intuitive blending than implicitly learned blending weights. Combined with a tailored multi-stage optimization scheme, the proposed MicroSDF achieves robust and high-fidelity reconstruction across reflective and non-reflective surfaces. Extensive experiments on DTU, Shiny Blender, Ref-NeRF, and DeepVoxels datasets demonstrate state-of-the-art performance, establishing a new direction for physically grounded neural reconstruction.

</details>

#### 2026-10-14 - Remember, Revisit, Revise: Scaffold Memory for Long-Horizon 3D Geometry

**Authors:** Soumick Sarker, Mengmi Zhang
**Links:** [abs](https://arxiv.org/abs/2610.19674) - [pdf](https://arxiv.org/pdf/2610.19674)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, simultaneous localization and mapping, SLAM, camera pose estimation, pose estimation, depth estimation, point cloud reconstruction, novel view synthesis, view synthesis, mapping, localization

<details>
<summary>Abstract</summary>

Geometry foundation models estimate camera poses and 3D scene structure from video sequences, but maintaining consistent reconstructions over long horizons remains challenging. Feed-forward models process long sequences as independent, fixed-length frame windows and align their predictions, causing pose and reconstruction errors to accumulate across windows. Streaming models retain information from past frames to inform future predictions, but cannot revise earlier estimates when later observations reveal errors. To address this, we introduce Scaffold MemOry for Revision (SMORE), a framework equipping frozen geometry foundation models with a revisable external memory for long-horizon inference. Inspired by hippocampal associative memory in biological brains, which links spatial context with sensory experience, SMORE associates where an observer is with what it observes, enabling past observations to be stored, retrieved, verified against new evidence, and revised when inconsistencies are detected. We evaluate SMORE with eight competitive geometry models on five datasets spanning camera pose estimation, multi-view depth estimation, 3D point-cloud reconstruction, simultaneous localization and mapping (SLAM), and novel view synthesis. Across all evaluated models, SMORE consistently improves long-sequence pose estimation, reduces multi-view depth error by up to 58%, reduces Chamfer distance for 3D point-cloud reconstruction by up to 43%, and achieves average trajectory error as low as 2.9 cm in long-horizon SLAM. By retaining corrected poses and observations, SMORE further improves the fidelity and spatial consistency of large-scale 3D scene reconstruction. These results establish revisable external memory as a flexible interface for extending pretrained geometry models beyond fixed-context prediction toward iterative, error-correcting inference over long visual sequences.

</details>

#### 2026-10-14 - Robust Real-Time Monocular Human Pose Estimation with Insole-Based Sensor Fusion

**Authors:** Liang Yu, Tao Zhu, Xiangqing Lu, Wenjian Luo, Liming Chen
**Links:** [abs](https://arxiv.org/abs/2610.19494) - [pdf](https://arxiv.org/pdf/2610.19494)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Real-time monocular human pose estimation is an important sensing component for human-centered intelligent systems. While recent camera-based methods have achieved impressive accuracy, fundamental challenges persist, particularly when visual observations are incomplete, such as during lower-body occlusion or short out-of-frame intervals. In these challenging but common scenarios, vision-only systems often struggle to reconstruct physically plausible lower-limb motion and reliable foot-ground contact. Due to the highly unobtrusive and wearable nature of smart insoles, this paper investigates whether simple plantar pressure and acceleration sensors can effectively resolve these visually induced limitations. To systematically investigate this, we first collect a synchronized multimodal dataset and then propose a part-decoupled temporal fusion framework. The proposed model fuses foot-sensing features into the lower-body branch to compensate for incomplete visual evidence, while a lightweight coordinator exchanges information between the upper- and lower-body temporal representations to maintain whole-body consistency. The framework is evaluated with three representative real-time visual backbones based on 2D keypoints, 3D landmarks, and SMPL-based human mesh recovery. We evaluate our framework on three representative real-time visual backbones. Quantitative experiments demonstrate that incorporating simple foot sensors consistently improves pose accuracy, motion smoothness, and gait-related measurements over vision-only baselines, with the most significant gains observed under occlusion and short visual-dropout conditions. Ultimately, our results demonstrate that unobtrusive foot sensing provides vital and complementary physical observability when camera observations are temporarily unavailable.

</details>

#### 2026-10-13 - Benchmarking 3D Reconstruction for Under-Ice Robotic Perception in Arctic Environments

**Authors:** Klára Orbán, Ashwin Nedungadi, Ana-Ştefania Kogălniceanu, Bianca-Marcela Sava, Bastian Cieply, Raul-Alexandru Simon, Kuderna-Iulian Benţa, Stefan Lüdtke
**Links:** [abs](https://arxiv.org/abs/2610.19097) - [pdf](https://arxiv.org/pdf/2610.19097)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, SfM, depth estimation, monocular depth, robotics, mapping

<details>
<summary>Abstract</summary>

As the Arctic transitions toward a seasonally ice-free state, capturing the complex morphology of submerged sea ice is crucial for advancing models of ocean-ice-atmosphere heat exchange and monitoring under-ice habitats. Currently, sub-surface ice mapping is predominantly achieved through acoustic sensors such as multibeam sonar. While sonar provides robust large-scale geometry, it lacks spectral and high-resolution textural information required to record fine morphological features - a critical limitation in under-ice environments, where sparse visual features and degraded sensing conditions challenge the capture of detailed structural and optical surface properties. We present a benchmark for vision-based under-ice 3D reconstruction using real-world data from the MOSAiC expedition and synthetic data generated in an Unreal Engine-based underwater robotics simulator. The benchmark evaluates Structure-From-Motion (SfM) and monocular depth estimation, with quantitative comparison enabled through cross-modal registration to upward-looking multibeam sonar.

</details>

#### 2026-10-13 - WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World

**Authors:** Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
**Links:** [abs](https://arxiv.org/abs/2610.18846) - [pdf](https://arxiv.org/pdf/2610.18846)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, mesh reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World
- 作者：Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
- 出版日期：2026-10-13T17:57:58Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；次要分类：摘要未提供足够信息
- 链接：摘要链接 https://arxiv.org/abs/2610.18846 ；PDF 链接 https://arxiv.org/pdf/2610.18846 ；项目页 https://kszpxxzmc.github.io/WorldRecon-website/

### 一句话总结
WorldRecon 是一个面向大规模场景的生成式多视角网格重建框架，利用由输入图像估计出的粗糙全局点云与相机位姿作为全局支架，并通过分块生成与邻域感知的因果式世界生成流程，从无位姿 RGB 图像中恢复完整、连贯的大规模三维场景网格。

### 研究问题
论文关注的任务是：从**无位姿（unposed）多视角 RGB 图像**中重建大规模场景的**完整、高质量网格**。该任务的核心难点在于，既要保持可靠的几何 grounding，又需要合理地补全未被观测或仅被稀疏捕获的表面。摘要指出，这需要在几何忠实性与生成补全能力之间取得平衡，并将多视角生成式重建扩展到大规模场景。

### 核心思路/方法
- 整体框架：WorldRecon 是一个生成式多视角重建框架，用于从无位姿 RGB 图像恢复完整的大规模三维场景网格。
- 全局支架：使用由重建模型从输入图像估计出的**粗糙、带噪声的全局点云和相机位姿**作为整个场景生成的全局支架，并将其划分为**重叠的空间块（overlapping spatial blocks）**。
- 条件生成架构：为稳健利用这些不完美的几何先验，作者为原生三维生成模型 **TRELLIS.2** 配备了专门基于重建的条件架构，使每个块能够基于其**局部点云裁剪（local point-cloud crop）** 和**与该块相关的图像观测**进行生成，产出稀疏结构、详细几何以及 PBR 材质。
- 场景级一致性：为保持场景级连贯性，提出**邻域感知的 latent inpainting** 以及**因果式世界生成流程（causal world-generation procedure）**，在重叠块之间传播结构、几何与材质上下文。
- 效果定位：上述设计共同将多视角生成式重建扩展到大规模场景，得到连贯、统一的网格。

### 主要贡献
- 提出 WorldRecon，一个从无位姿 RGB 图像恢复完整、大规模三维场景网格的生成式多视角重建框架。
- 设计以粗糙噪声全局点云与相机位姿作为全局支架、并划分重叠空间块的大规模生成策略。
- 为 TRELLIS.2 引入专门基于重建的条件架构，使每个块可利用局部点云裁剪与块相关图像观测生成稀疏结构、细节几何和 PBR 材质。
- 引入邻域感知 latent inpainting 与因果式世界生成流程，跨重叠块传播结构、几何与材质上下文，以维持场景级一致性。
- 摘要报告实验显示其达到 state-of-the-art 重建性能：在合成与真实室内场景上，相较最强基线，Chamfer distance 分别降低 14.9% 与 43.1%，F-score 分别提升 17.3% 与 12.0%，并展现出较强的 sim-to-real 泛化能力。

### 局限性
- 摘要未提供足够信息说明方法在极端稀疏视角、严重遮挡或动态场景下的具体失效情形。
- 摘要未提供足够信息说明对初始粗糙点云与相机位姿估计误差的敏感程度及失败边界。
- 摘要未提供足够信息说明计算开销、运行时间、显存需求或可扩展场景规模上限。
- 摘要未提供足够信息说明真实世界实验的完整设置、评价协议与消融细节。
- 摘要未提供足够信息说明 PBR 材质生成的质量评估方式及其局限性。

### 阅读优先级
高。理由：该论文面向无位姿多视角大规模场景网格重建这一重要且困难的问题，提出结合全局支架、分块生成、邻域感知 latent inpainting 与因果式世界生成的完整框架，并在摘要中报告了相对最强基线的定量提升与 sim-to-real 泛化结果，对三维重建、多视角几何与生成式三维建模方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing complete, high-quality meshes of large-scale scenes from unposed multi-view images requires faithful geometric grounding while plausibly completing surfaces that are unobserved or only sparsely captured. We present WorldRecon, a generative multi-view reconstruction framework for recovering complete, large-scale 3D scene meshes from unposed RGB images. WorldRecon uses a coarse, noisy global point cloud and camera poses estimated from the input images by a reconstruction model as a global scaffold for whole-scene generation and partitions it into overlapping spatial blocks. To robustly leverage these imperfect geometric priors, we equip the native 3D generative model TRELLIS.2 with a dedicated reconstruction-based conditioning architecture that generates each block from its local point-cloud crop and block-relevant image observations, producing sparse structure, detailed geometry, and PBR materials. To maintain scene-level coherence, we introduce neighbour-aware latent inpainting and a causal world-generation procedure that propagates structural, geometric, and material context across overlapping blocks. Together, these designs scale multi-view generative reconstruction to large-scale scenes, yielding coherent, unified meshes. Extensive experiments demonstrate that WorldRecon achieves state-of-the-art reconstruction performance, reducing Chamfer distance by 14.9% and 43.1% while improving F-score by 17.3% and 12.0% over the strongest baselines on synthetic and real-world indoor scenes, respectively, thereby demonstrating faithful and complete generative reconstruction as well as strong sim-to-real generalization. Project page: https://kszpxxzmc.github.io/WorldRecon-website/.

</details>

#### 2026-10-13 - Augmenting Real-time Visualization in Minimally Invasive Surgery with Particle Filtering and Depth-Aware Occlusion Handling

**Authors:** Anuska Sarkar, Partha Acharya, Vishnu Nandury, Kaustav Basu, Subhamoy Mandal
**Links:** [abs](https://arxiv.org/abs/2610.18422) - [pdf](https://arxiv.org/pdf/2610.18422)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, depth estimation, monocular depth, stereo depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Augmenting Real-time Visualization in Minimally Invasive Surgery with Particle Filtering and Depth-Aware Occlusion Handling
- 作者：Anuska Sarkar, Partha Acharya, Vishnu Nandury, Kaustav Basu, Subhamoy Mandal
- 出版日期：2026-10-13T14:01:01Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.18422

### 一句话总结
该论文提出一种融合增强YOLO检测、粒子滤波与单目深度估计（MiDaS）的实时混合框架，用于微创手术中器械遮挡的检测与深度感知跟踪，以提升可视化效果。

### 研究问题
微创手术中，手术器械造成的遮挡常会遮蔽感兴趣区域（ROI），影响手术精度。论文旨在解决该场景下的遮挡处理与深度感知跟踪问题，并实现实时可视化。

### 核心思路/方法
- 采用增强的YOLO进行器械检测；
- 引入粒子滤波（PF）进行跟踪；
- 使用单目深度估计网络MiDaS进行深度估计；
- 通过器械与ROI之间基于距离的阈值来判定遮挡事件；
- 整体构成一个实时混合框架。

### 主要贡献
- 提出融合YOLO、粒子滤波与MiDaS的实时混合框架，用于微创手术中的遮挡处理与深度感知跟踪；
- 实现稳健的器械检测，置信度得分为0.85；
- 有效处理遮挡事件，遮挡检测准确率为81.95%；
- 深度预测达到MAE 0.34 cm、RMSE 0.53 cm；
- 基于体模的独立验证（对照立体深度测量）达到MAE 0.65 cm、RMSE 0.66 cm；
- 保持38.7 FPS的实时性能；
- 初步外科医生反馈表明该可视化框架具有临床相关性，并有望用于未来术中图像引导导航与决策支持。

### 局限性
- 摘要仅提及“初步外科医生反馈”，未提供反馈规模、评价方式或统计细节，摘要未提供足够信息；
- 摘要未说明数据集规模、器械种类、手术类型或场景多样性，摘要未提供足够信息；
- 摘要未提供与更多基线方法的系统性对比，摘要未提供足够信息；
- 摘要未说明失败案例、遮挡误检/漏检的具体情形，摘要未提供足够信息；
- 体模验证虽独立对照立体深度，但未提供活体或临床实际场景的验证结果，摘要未提供足够信息。

### 阅读优先级
中。理由：该论文聚焦微创手术实时可视化中的遮挡处理与深度感知，给出了明确的量化指标与实时性能，并包含初步临床反馈，对相关方向有参考价值；但摘要未展示与多种基线的系统对比、数据集与临床验证细节，且分类为3D重建与多视角几何，与该工作的手术可视化主题存在一定跨度，因此优先级评为中。

</details>

<details>
<summary>Abstract</summary>

We present a real-time, hybrid framework for occlusion handling and depth-aware tracking in minimally invasive surgeries (MIS). Occlusions caused by surgical instruments often obscure the region of interest (ROI), affecting surgical precision. To address this, our approach integrates enhanced You Only Look Once (YOLO) based detection, Particle Filtering (PF), and monocular depth estimation using Multiple Depth Estimation Accuracy with Single Network (MiDaS). Occlusion is detected using a distance-based threshold between instruments and ROI. Experimental results demonstrate robust instrument detection with a confidence score of 0.85, effective occlusion event handling, and accurate depth prediction with an MAE of 0.34 cm and RMSE of 0.53 cm. Independent phantom-based validation against stereo depth measurements yielded an MAE of 0.65 cm and RMSE of 0.66 cm. The framework further achieved an occlusion detection accuracy of 81.95\% while maintaining real-time performance at 38.7 FPS. Preliminary surgeon feedback indicates that the proposed visualization framework is clinically relevant and holds promise for future intraoperative image-guided navigation and decision support in MIS.

</details>

#### 2026-10-13 - SchemaPose: RGB-Based Category-Level Pose Estimation with Parametric Category Schema

**Authors:** Shuang Wu, Jiude Wei, Cewu Lu, Jianhua Sun
**Links:** [abs](https://arxiv.org/abs/2610.18374) - [pdf](https://arxiv.org/pdf/2610.18374)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SchemaPose: RGB-Based Category-Level Pose Estimation with Parametric Category Schema
- 作者：Shuang Wu, Jiude Wei, Cewu Lu, Jianhua Sun
- 出版日期：2026-10-13T13:29:04Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.18374 ；PDF https://arxiv.org/pdf/2610.18374

### 一句话总结
SchemaPose 提出一种以“参数化类别 schema”为引导的框架，用于纯 RGB 输入的类别级 9D 位姿估计，通过显式建模类别共性与结构化实例差异来指导位姿预测。

### 研究问题
论文针对的是基于 RGB 的类别级 9D 位姿估计问题。该任务要求单目系统在未见过的物体实例上泛化，同时联合推断 3D 平移、3D 旋转和 3D 尺寸。与实例级位姿估计不同，类别级设定要求网络同时学习同一类别内物体共享的特征以及个体实例在结构上的变化。摘要指出，在仅有 RGB 的设定下，位姿线索、类别级共性和实例特异性变化在外观中相互纠缠，且缺乏直接几何约束，使现有框架难以学到真正与类别级估计目标对齐的表示。

### 核心思路/方法
论文提出 SchemaPose，一个 schema 引导的 RGB 类别级位姿估计框架。其核心是为估计流程配备一个显式的参数化 schema，用于建模类别级规律以及结构化的实例变化，并利用推断出的 schema 变量在端到端的 query-based 框架中引导与位姿相关的预测。摘要还提到，同一套形式化方法可以在统一框架内支持模板实例化、合成标注和位姿学习。

### 主要贡献
- 提出 SchemaPose，一个用于 RGB 类别级位姿估计的 schema 引导框架。
- 引入显式参数化类别 schema，用于建模类别级规律与结构化实例变化。
- 使用推断出的 schema 变量在端到端 query-based 框架中引导位姿相关预测。
- 同一形式化方法支持模板实例化、合成标注与位姿学习的统一处理。
- 摘要称在合成和真实数据上的实验表明，SchemaPose 在基于 RGB 的类别级 9D 位姿估计方法中达到 state-of-the-art 性能。

### 局限性
摘要未提供足够信息。未提供具体实验设置、数据集名称、评价指标细节、消融实验、失败案例或方法适用边界等信息。

### 阅读优先级
中。理由：该论文聚焦 RGB-only 类别级 9D 位姿估计，问题设定明确，且摘要声称在 RGB 方法中达到 state-of-the-art，并以参数化类别 schema 作为核心设计，具有一定新颖性；但摘要未给出具体实验细节与量化结果，是否值得深入阅读需结合后续对方法细节和实验部分的核查。

</details>

<details>
<summary>Abstract</summary>

RGB-based category-level 9D pose estimation remains highly challenging because a monocular system must generalize across unseen object instances while jointly inferring 3D translation, 3D rotation, and 3D size. Unlike instance-level pose estimation, the category-level setting requires the network to learn both what is shared across objects within a category and how individual instances vary in structure. This challenge is amplified in the RGB-only setting, where pose cues, category-level commonality, and instance-specific variation are entangled in appearance without direct geometric constraints, making it difficult for existing frameworks to learn a representation that is truly aligned with the category-level estimation objective. To address this problem, we propose SchemaPose, a schema-guided framework for RGB-based category-level pose estimation. SchemaPose equips the estimation pipeline with an explicit parametric schema for modeling category-level regularities together with structured instance variation, and uses the inferred schema variables to guide pose-related prediction in an end-to-end query-based framework. The same formulation also supports template instantiation, synthetic annotation, and pose learning within a unified framework. Experiments on synthetic and real data show that SchemaPose achieves state-of-the-art performance among RGB-based methods for category-level 9D pose estimation.

</details>

#### 2026-10-13 - CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations

**Authors:** Jiahui Sun, Ran Bi, Yifei Liu, Xiaolong Zhou, Yishuo Xu, Yuanqi Li, Congcong Zhu, Lei Yang, Yanwen Guo, Zhihang Zhong, Hongjie Zhang
**Links:** [abs](https://arxiv.org/abs/2610.18342) - [pdf](https://arxiv.org/pdf/2610.18342)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation, dense reconstruction, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations
- 作者：Jiahui Sun, Ran Bi, Yifei Liu, Xiaolong Zhou, Yishuo Xu, Yuanqi Li, Congcong Zhu, Lei Yang, Yanwen Guo, Zhihang Zhong, Hongjie Zhang
- 出版日期：2026-10-13T13:14:17Z
- 分类：primary_category: 3D Reconstruction & Multi-view Geometry；secondary_categories: 摘要未提供足够信息
- 链接：abstract_url: https://arxiv.org/abs/2610.18342；pdf_url: https://arxiv.org/pdf/2610.18342

### 一句话总结
论文提出 CityCode 与 Air2Code，旨在从每个区域一张低空航拍 RGB 图像及已知相机参数出发，生成大规模、实例级参数化、可被智能体操作且支持持续更新与历史恢复的 3D 城市表示。

### 研究问题
摘要指出，城市空间智能需要智能体能够在连续任务中对 3D 城市进行测量、解释和修改。若要将这种城市作为持久、基于代码的状态来维护，就需要轻量级获取方式，并支持一致的状态更新，而不必反复进行密集重建。因此，论文提出一个新的设定：从每个区域一张低空航拍 RGB 图像和已知相机参数中，生成大规模、实例级参数化 3D 城市，同时恢复具有度量尺度的建筑以及显式道路几何与连通性。

### 核心思路/方法
论文提出 CityCode 作为可被智能体操作的表示，通过持久实体身份统一度量几何、城市拓扑、视觉语义和 3D 资产，并采用依赖感知的版本化执行来支持经过验证的更新与历史恢复。为构建该表示，论文进一步提出 Air2Code，将视觉结构提取与适配的度量深度估计相结合。针对遮挡和不完整覆盖问题，方法利用恢复的结构和观测外观引导生成式补全，并进行后续的结构感知 3D 生成，以生成建筑和背景。

### 主要贡献
- 提出新的问题设定：从每个区域一张低空航拍 RGB 图像和已知相机参数生成大规模、实例级参数化 3D 城市，并恢复度量尺度建筑与显式道路几何和连通性。
- 提出 CityCode：一种可被智能体操作的表示，通过持久实体身份统一度量几何、城市拓扑、视觉语义和 3D 资产，并支持依赖感知的版本化执行、经过验证的更新和历史恢复。
- 提出 Air2Code：结合视觉结构提取与适配的度量深度估计来构建上述表示，并利用恢复结构与观测外观引导生成式补全和结构感知 3D 生成，以应对遮挡与不完整覆盖。
- 摘要称在 CitySample-Aerial 和 UrbanScene3D 上，相比所评估的基线，方法在度量结构恢复准确性上明显更好，并在目标城市的视觉保真度上更优。
- 摘要称在 50 条任务链、每条 50 步的设置下，CityCode 支持在不断演进的城市状态上进行持续查询、编辑、规划和历史恢复。

### 局限性
- 摘要未提供足够信息说明方法在何种条件下会失败，或对相机参数、图像质量、区域规模等因素的敏感程度。
- 摘要未提供足够信息说明实验基线的具体构成、评价指标的细节、消融实验以及计算开销。
- 摘要未提供足够信息说明生成式补全与结构感知 3D 生成可能引入的误差或不确定性。
- 摘要未提供足够信息说明“经过验证的更新”的具体验证机制及其可靠性边界。

### 阅读优先级
高。理由：该论文面向从稀疏航拍观测构建持久、可被智能体操作的 3D 城市，问题设定与“城市空间智能”“长时程任务链”“可更新与可恢复状态”直接相关；摘要明确给出新表示、构建方法、任务链验证以及两个数据集上的实验结果，对 3D 重建、城市建模和智能体操作城市表示方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Urban spatial intelligence calls for 3D cities that agents can measure, interpret, and modify across successive tasks. Maintaining such cities as persistent, code-based states requires lightweight acquisition and support for consistent state updates without repeated dense reconstruction. We therefore formulate a new setting for grounded urban world construction: generating large-scale, instance-level parameterized 3D cities from one low-altitude aerial RGB image per region and known camera parameters, while recovering metrically scaled buildings and explicit road geometry and connectivity. We introduce CityCode, an agent-operable representation that unifies metric geometry, urban topology, visual semantics, and 3D assets through persistent entity identities, with dependency-aware versioned execution for validated updates and historical restoration. We further develop Air2Code to construct this representation by combining visual structure extraction with adapted metric depth estimation. To address occlusion and incomplete coverage, recovered structure and observed appearance guide generative completion and subsequent structure-aware 3D generation for buildings and backgrounds. Experiments on CitySample-Aerial and UrbanScene3D demonstrate substantially more accurate metric structure recovery and superior visual fidelity to the target cities compared with the evaluated baselines. Across 50 task chains of 50 steps each, CityCode supports continued querying, editing, planning, and historical restoration over evolving city states. Together, CityCode and Air2Code turn sparse aerial observations into persistent, agent-operable urban worlds for long-horizon urban spatial intelligence.

</details>

#### 2026-10-13 - Surface Reconstruction from Range Scans Under Visibility Constraints

**Authors:** Gabriel Lenain, Edmond Boyer, Jean Ponce
**Links:** [abs](https://arxiv.org/abs/2610.18005) - [pdf](https://arxiv.org/pdf/2610.18005)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** surface reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Surface Reconstruction from Range Scans Under Visibility Constraints
- 作者：Gabriel Lenain, Edmond Boyer, Jean Ponce
- 出版日期：2026-10-13T09:05:23Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.18005

### 一句话总结
该论文将表面重建表述为沿每条采集射线的预测首次表面交点相对其测量深度的稳健回归问题，在可见性约束下实现对噪声与离群点的鲁棒重建。

### 研究问题
基于距离扫描的表面重建在存在噪声与离群点时具有挑战性，因为需要在忠实于观测数据与对测量误差保持敏感度之间取得平衡。摘要指出，大多数神经方法丢弃了传感器位置及对应的可见性信息，转而通过几何先验或正则化项来补偿这种信息损失。

### 核心思路/方法
- 将表面重建表述为稳健回归问题：沿每条采集射线，将预测的首次表面交点回归到其测量深度。
- 该回归对位于传感器与观测点之间线段内的预测表面交点施加惩罚（体现可见性约束）。
- 用 1-Lipschitz 多层感知机的零水平集表示表面，从而可使用线性收敛的球面追踪（sphere tracing）计算首次命中。
- 采用稳健的 Huber 损失进行回归。
- 该表述不需要有向法线、采样的离表面点，也不需要 eikonal 损失。

### 主要贡献
- 提出在可见性约束下、基于射线上首次表面交点稳健回归的表面重建表述，显式利用传感器位置与可见性信息，而非将其丢弃。
- 使用 1-Lipschitz MLP 零水平集表示表面，并利用线性收敛的球面追踪计算首次命中，配合 Huber 稳健损失。
- 该方法无需有向法线、离表面采样点或 eikonal 损失。
- 摘要称在合成与真实数据、不同噪声与离群点污染水平下与当前最优方法比较，在干净数据上具有竞争性表现，在中等程度污染下忠实度与鲁棒性显著提升。
- 分析进一步确认了忠实度与鲁棒性之间的权衡：更强的拟合能力在干净情况下提升数据忠实度，但增加对真实采集中固有测量误差的敏感度，折中点通常出现在中等容量处。

### 局限性
- 摘要未提供足够信息说明具体的数据集名称、评价指标、网络结构与训练细节。
- 摘要未提供足够信息说明方法在极端噪声或高比例离群点下的表现边界。
- 摘要未提供足够信息说明计算开销、运行时间或与各对比方法的具体量化差距。
- 摘要未提供足够信息说明该方法对传感器类型、扫描视角覆盖范围等的适用条件与失效情形。

### 阅读优先级
高。理由：该论文聚焦距离扫描重建中的噪声与离群点鲁棒性问题，明确指出现有神经方法丢弃传感器可见性信息的不足，并提出无需有向法线、离表面采样点与 eikonal 损失的替代表述；其关于忠实度与鲁棒性权衡的分析对 3D 重建与多视图几何方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Surface reconstruction from range scans is challenging in the presence of noise and outliers, as fidelity to observations must be balanced against sensitivity to measurement errors. Yet, most neural approaches discard the sensor positions and corresponding visibility information, compensating for this loss with geometric priors or regularization terms. We instead formulate surface reconstruction as robust regression of the predicted first surface intersection along each acquisition ray against its measured depth, which penalizes predicted surface intersections within the segment between the sensor and the observed point. We represent the surface as the zero set of a 1-Lipschitz multi-layer perceptron, allowing the use of linearly convergent sphere tracing to compute the first hit, and use a robust Huber loss for regression. Our formulation requires neither oriented normals, sampled off-surface points, nor an eikonal loss. Comparisons with the state of the art on synthetic and real data with varying levels of noise and outlier contamination demonstrate competitive performance on clean data and much improved fidelity and robustness under even moderate corruption. Our analysis further confirms a trade-off between fidelity and robustness: greater fitting capacity improves data fidelity in the clean case but increases sensitivity to the measurement errors inherent in real acquisitions, with a sweet spot typically emerging at intermediate capacity.

</details>

#### 2026-10-13 - Smartphone-Based, Field-Deployed AI Inspection System for Power Distribution Infrastructure

**Authors:** Sampath Balaji Masabathula, Srija Vanapalli, Gangadhar Kanchi, Sreenivasa Rao V. A. N, Vijaya Lalitha, Sasank Chilamkurthy
**Links:** [abs](https://arxiv.org/abs/2610.17620) - [pdf](https://arxiv.org/pdf/2610.17620)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Smartphone-Based, Field-Deployed AI Inspection System for Power Distribution Infrastructure
- 作者：Sampath Balaji Masabathula, Srija Vanapalli, Gangadhar Kanchi, Sreenivasa Rao V. A. N, Vijaya Lalitha, Sasank Chilamkurthy
- 出版日期：2026-10-13T02:42:13Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.17620 ；PDF https://arxiv.org/pdf/2610.17620

### 一句话总结
该工作提出并实地部署了一套基于智能手机的配电基础设施 AI 巡检系统，通过多阶段工作流对现场图像进行质量控制与多类缺陷评估，并在实际馈线上完成缺陷识别、整改跟踪与验证。

### 研究问题
配电基础设施的地理分布广泛，传统人工巡检难以一致、大规模地执行。论文关注的问题是如何利用现场人员用智能手机拍摄的图像，对配电基础设施的特定状态进行 AI 辅助检查，并将识别、记录、整改跟踪和验证纳入实际巡检维护流程。

### 核心思路/方法
论文提出一套面向现场操作的多阶段巡检工作流。该流程将图像质量与拍摄视角验证，与 AI 辅助评估相结合，评估对象包括：电杆倾斜、横担和顶部线夹倾斜、电压等级、植被净空风险以及配电变压器（DTR）对地净空。技术层面，系统整合了深度学习模型、单目深度估计、几何分析和基于规则的处理，构成统一的巡检流程。系统在 APEPDCL 的五个选定配电馈线上进行了试点部署。

### 主要贡献
- 提出一套基于智能手机的 AI 巡检系统，用于从现场人员拍摄的图像中评估目标配电基础设施状态。
- 构建了多阶段巡检工作流，将图像质量与视角验证、AI 辅助评估、深度估计、几何分析和规则处理整合到实际现场操作中。
- 在 APEPDCL 的五个配电馈线上开展试点部署，识别出 1,222 个缺陷实例，并通过整改与验证流程进行跟踪，研究期间记录到 84 个缺陷实例完成整改。
- 公开释放了一个经过整理的多模块现场拍摄数据集 PD-Defect，以支持配电基础设施巡检的可复现研究。
- 实地部署展示了将基于智能手机的 AI 辅助巡检整合到现场巡检与维护活动中的可行性，提供了对目标缺陷进行系统识别、记录、整改跟踪和验证的机制。

### 局限性
- 馈线级中断记录虽在研究期间被检查，但摘要明确指出，可用观测不足以证明所提系统带来了可靠性提升。
- 摘要未提供足够信息说明系统的检测精度、各类缺陷的分别表现、误报漏报情况、模型泛化能力、不同拍摄条件或设备差异下的稳健性。
- 摘要未提供足够信息说明试点部署的持续时间、五个馈线的选择标准、1,222 个缺陷实例的类别分布，以及未整改缺陷的原因。
- 摘要未提供足够信息说明 PD-Defect 数据集的具体规模、标注方式、模块组成和数据采集协议。
- 摘要未提供足够信息说明与人工巡检或其他方法的对比实验结果。

### 阅读优先级
高。理由：该论文面向真实电力配电基础设施巡检场景，包含智能手机端 AI 系统、多阶段现场工作流、实际试点部署、缺陷整改跟踪以及公开数据集释放，问题和落地路径明确；同时摘要也如实指出可靠性提升证据不足，适合关注现场部署、基础设施视觉巡检和 AI 辅助运维的研究与应用人员阅读。

</details>

<details>
<summary>Abstract</summary>

Routine inspection of power distribution infrastructure remains challenging for utilities operating geographically dispersed networks, where conventional manual inspection can be difficult to perform consistently and at scale. This work presents a smartphone-based AI inspection system for assessing targeted distribution-infrastructure conditions from images captured by field personnel. The proposed workflow integrates image-quality and viewing-perspective validation with AI-assisted assessment of pole lean, crossarm and top-cleat tilt, voltage level, vegetation-clearance risk, and distribution-transformer (DTR)-ground clearance. The system integrates deep-learning models with monocular depth estimation, geometric analysis, and rule-based processing within a common multi-stage inspection workflow designed for practical field operation. The system was pilot deployed across five selected distribution feeders within the Eastern Power Distribution Company of Andhra Pradesh Ltd. (APEPDCL), where 1,222 defect instances were identified across the assessed categories and subsequently tracked through a rectification and verification workflow, with 84 defect instances recorded as rectified during the study period. Feeder-level interruption records were also examined over the study period; however, the available observations do not provide sufficient evidence to establish a reliability improvement attributable to the proposed system. A curated multi-module field-captured dataset, PD-Defect, is also publicly released to support reproducible research in distribution-infrastructure inspection. The field deployment demonstrates the practical integration of smartphone-based AI-assisted inspection into field inspection and maintenance activities, providing a mechanism for systematic identification, documentation, rectification tracking, and verification of targeted distribution-infrastructure defects.

</details>

#### 2026-10-13 - Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs

**Authors:** Ashim Dahal, Rabab Abdelfattah, Nick Rahimi
**Links:** [abs](https://arxiv.org/abs/2610.17513) - [pdf](https://arxiv.org/pdf/2610.17513)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, scene reconstruction, simultaneous localization and mapping, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, scene representation, rendering, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs
- 作者：Ashim Dahal, Rabab Abdelfattah, Nick Rahimi
- 出版日期：2026-10-13T00:20:10Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；副分类为 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.17513) / [PDF](https://arxiv.org/pdf/2610.17513)

### 一句话总结
这是一篇关于 3D Gaussian Splatting（3DGS）实时场景重建的综述，梳理了五类相互重叠的研究方向，并强调需区分“仅渲染吞吐”与构建、更新、维护场景本身的开销，进而识别跨类别的质量、延迟、内存与更新成本权衡。

### 研究问题
摘要指出，尽管 3DGS 能够实现高质量实时新视角合成与实时渲染，但“渲染一个已有表示”与“构建、更新或维护场景本身”是不同的任务。论文关注的核心问题是：在 3DGS 自 2023 年提出后，其显式且高度可配置的场景表示已被扩展到稀疏视角生成、动态重建、效率与压缩、流式传输、SLAM 等方向；当前文献中这些方向的方法、系统与工具之间关系如何，如何通向端到端流水线，以及在不同任务下存在怎样的质量、延迟、内存和更新成本权衡。

### 核心思路/方法
论文采用综述方式，综合当前文献并进行分类，将 GS 场景重建划分为五个相互重叠的家族：
1. single-shot generation（单次生成）
2. dynamic representations（动态表示）
3. efficiency and compression（效率与压缩）
4. streaming and immersive systems（流式与沉浸式系统）
5. Gaussian Splatting SLAM

作者强调区分 render-only throughput 与任务特定的场景生成、更新、跟踪、建图与优化成本，并将受控稀疏视角基准测试与原生评估相结合，以识别跨家族的质量、延迟、内存和更新成本权衡。摘要还提到其目标是连接当前方法与工具，指向一个端到端流水线。

### 主要贡献
- 对 3DGS 场景重建相关当前文献进行综合与分类。
- 明确将 GS 场景重建划分为五个相互重叠的家族：单次生成、动态表示、效率与压缩、流式与沉浸式系统、Gaussian Splatting SLAM。
- 区分“仅渲染吞吐”与任务特定的场景生成、更新、跟踪、建图及优化成本。
- 结合受控稀疏视角基准测试与原生评估，识别跨家族在质量、延迟、内存和更新成本方面的权衡。
- 将当前方法与工具联系起来，面向端到端流水线。

### 局限性
摘要未提供足够信息说明该综述的文献覆盖范围、检索与筛选标准、具体基准数据集、实验设置、定量结果细节、所提出分类的验证方式，以及作者对开放问题或未来方向的完整讨论。摘要也未提供足够信息说明其是否存在方法偏见、评估协议局限或可复现性方面的限制。

### 阅读优先级
高。理由：该文是面向 3DGS 实时场景重建的综述，明确覆盖单次生成、动态表示、效率与压缩、流式系统与 SLAM 等多个关键方向，并聚焦质量、延迟、内存与更新成本之间的权衡；对于希望快速建立 3DGS 场景重建研究版图、理解“渲染”与“场景构建/维护”差异、并寻找端到端流水线连接点的读者，具有较高的入口价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) allows for high-quality real-time novel-view synthesis. Since its inception in 2023, its explicit and highly configurable scene representation has been extended toward sparse-view generation, dynamic reconstruction, efficiency and compression, streaming, and simultaneous localization and mapping (SLAM). Although Gaussian Splatting can provide real-time rendering, rendering an existing representation is distinct from constructing, updating, or maintaining the scene itself. In this survey, we synthesize current literature, categorize them and provide a connection of current approaches and tools towards an end-to-end pipeline. Explicitly, we categorize GS scene reconstruction into five overlapping families: single-shot generation, dynamic representations, efficiency and compression, streaming and immersive systems, and Gaussian Splatting SLAM. We distinguish render-only throughput from task-specific scene generation, update, tracking, mapping, and optimization costs, and combine controlled sparse-view benchmarking with native evaluations to identify cross-family quality, latency, memory, and update-cost trade-offs.

</details>

#### 2026-10-12 - CopyQuad: Quadrupedal Skill Transfer from a Single Side-View Video Without a Depth Model

**Authors:** Mohamad H. Danesh, Raina Hu, Mengxue Xu, Hsiu-Chin Lin
**Links:** [abs](https://arxiv.org/abs/2610.16737) - [pdf](https://arxiv.org/pdf/2610.16737)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CopyQuad: Quadrupedal Skill Transfer from a Single Side-View Video Without a Depth Model
- 作者：Mohamad H. Danesh, Raina Hu, Mengxue Xu, Hsiu-Chin Lin
- 出版日期：2026-10-12T13:06:33Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类；摘要未提供其他次级分类信息）
- 链接：https://arxiv.org/abs/2610.16737 ；PDF：https://arxiv.org/pdf/2610.16737

### 一句话总结
CopyQuad 提出去掉视频到四足机器人模仿流程中常用的深度估计或逐片段三维重建环节，将侧视相机无法观测的缺失轴固定为机器人自身站姿宽度，从而用冻结的 2D 关键点检测器和固定解析重定向实现单段未标定视频的零样本技能迁移。

### 研究问题
现有四足机器人视频模仿流程为了恢复侧视相机看不到的那一个轴，通常需要插入一个学习得到的提升阶段，例如单目深度模型或逐片段三维重建。本文关注的问题是：在矢状面主导运动、肢体运动几乎完全位于图像平面的侧视视频设定下，是否可以省略这一阶段，以及省略该轴会带来什么代价。

### 核心思路/方法
CopyQuad 省略深度模型或逐片段三维重建，把缺失的轴固定为机器人自身站姿宽度。其设定是侧视拍摄的矢状面主导运动，肢体运动几乎完全在图像平面内。方法使用冻结的 2D 关键点检测器和固定的解析重定向，将单个未标定视频片段转换为机器人参考，并保证足部目标按构造可达，因此不需要逐片段轨迹优化。学习阶段使用一个按相位索引的奖励结构，其唯一的按行为自由度是来自共享扫描的三个标量。该结构学习了狗步、马步、马小跑和两个非周期性手势，并全部零样本部署到硬件上。

### 主要贡献
- 提出 CopyQuad，在侧视、矢状面主导运动且无需深度模型的设定下，从单个未标定视频进行四足技能迁移。
- 使用冻结的 2D 关键点检测器与固定解析重定向，使足部目标按构造可达，避免逐片段轨迹优化。
- 采用相位索引奖励结构，仅用三个来自共享扫描的标量作为按行为自由度，学习狗步、马步、马小跑和两个非周期手势，并零样本部署到硬件。
- 测量省略该轴的成本：在无需训练的刚性测试中，视频深度模型使动物髋部间距离变化达到其自身均值的 40% 到 107%，单图像度量模型使其变化达到 22% 到 58%，而该距离本不能移动。运动捕捉显示狗步真实横向爪部行程峰峰值为 4.5 cm，平均偏差约 1.4 cm，而策略已留下的横向足部误差为 3.5 cm，因此被丢弃的轴低于流程分辨率。深度修复到可行后从未优于常数，而未修复的估计会使机器人倒地。

### 局限性
摘要未提供足够信息说明该方法在非侧视视角、非矢状面主导运动、其他动物步态或非周期行为之外场景中的适用性。摘要未提供足够信息说明硬件平台细节、训练数据规模、训练时长、失败案例分布以及与其他基线方法的完整定量对比。摘要未提供足够信息说明三个标量的具体含义、共享扫描的具体过程以及相位索引奖励结构的完整定义。

### 阅读优先级
高。理由：该论文直接挑战视频到四足机器人模仿中“必须插入深度模型或三维重建”的常见假设，并给出省略该轴的成本测量；如果其结论成立，可能显著简化四足技能迁移流程，并影响后续对侧视视频模仿中缺失轴处理方式的研究。

</details>

<details>
<summary>Abstract</summary>

Video-to-robot pipelines for quadrupedal imitation insert a learned lifting stage, either a monocular depth model or a per-clip 3D reconstruction, to recover the one axis a side-view camera cannot see. We present CopyQuad, which omits that stage and pins the missing axis to the robot's own stance width instead. The setting is side-view footage of sagittally dominated motion, where limb motion is almost entirely in the image plane. A frozen 2D keypoint detector and a fixed analytic retargeting then turn a single uncalibrated clip into a robot reference whose foot targets are reachable by construction, so no per-clip trajectory optimization is needed. One phase-indexed reward structure, whose only per-behavior freedom is three scalars from a shared sweep, learns a dog walk, a horse walk, a horse trot and two non-periodic gestures, all deployed zero-shot on hardware. We then measure what omitting the axis costs. In a training-free rigidity test, a video depth model varies the distance between the animal's hips by $40$ to $107\%$ of its own mean and a single-image metric model by $22$ to $58\%$, though that distance cannot move. Motion capture puts the true lateral paw travel of a dog walk at $4.5$ cm peak to peak, a mean deviation near $1.4$ cm against the $3.5$ cm of lateral foot error our policies already leave, so the discarded axis sits below the pipeline's resolution. Depth repaired to feasibility never beats the constant, and the unrepaired estimates put the robot on the ground.

</details>

#### 2026-10-12 - 3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification

**Authors:** William Grolleau, Astrid Sabourin, Guillaume Lapouge, Catherine Achard
**Links:** [abs](https://arxiv.org/abs/2610.16692) - [pdf](https://arxiv.org/pdf/2610.16692)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mesh reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification
- 作者：William Grolleau, Astrid Sabourin, Guillaume Lapouge, Catherine Achard
- 出版日期：2026-10-12T12:29:06Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供
- 链接：abs: https://arxiv.org/abs/2610.16692；pdf: https://arxiv.org/pdf/2610.16692

### 一句话总结
论文提出 3D-VITAL，利用单视图 3D 网格重建生成新视角训练数据，并通过可见性图进行几何一致性过滤与注意力监督，以提升跨视角物体重识别的泛化能力。

### 研究问题
论文关注跨视角物体重识别（Cross-View Object Re-Identification, ReID），即在差异极大的视角之间匹配同一身份。具体聚焦于单视角空对地重识别（Single-View Aerial-Ground ReID, SV AG-ReID）：模型在一个视角上训练，在推理时需要泛化到另一个视角。为弥合视角差距，相关工作总结是使用生成模型从源图像合成新视角作为额外训练数据。论文试图解决这种合成新视角数据中存在的两类不可靠问题：一是重建失败导致几何错误的网格，使渲染新视角严重损坏；二是即使几何正确，渲染新视角在源图像不可见区域仍包含幻觉纹理。

### 核心思路/方法
论文利用大规模单视图 3D 网格重建的进展，将源图像提升为带纹理网格，并从新视角渲染。该流程会产生不可靠数据，但重建网格携带一个逐像素划分：区分从源视角可见的区域与重建模型必须幻觉生成的区域；该划分可作为渲染的确定性副产物获得。论文引入这一逐像素可见性图，并设计两阶段方法：

1. Cross-View Consistency Filtering (CVCF)：通过在可见块上确保源视角与新视角之间的多视角一致性，丢弃几何不正确的网格。
2. Visibility-Aware Attention Supervision (VAAS)：利用可见性图在训练中引导模型注意力朝向渲染视角中的可靠区域。

两者结合使 3D-VITAL 更好地利用来自单视图 3D 网格重建的合成信号。论文称 3D-VITAL 在三个 SV AG-ReID 基准上取得新的最优结果。代码和数据将在 https://github.com/TurtleSmoke/3D-VITAL 发布。

### 主要贡献
- 提出 3D-VITAL 方法，用于跨视角物体重识别中的单视角空对地场景。
- 指出现有“生成新视角作为训练数据”流程中两类不可靠性：几何错误网格导致的渲染损坏，以及源视角不可见区域中的幻觉纹理。
- 引入重建网格渲染副产物中的逐像素可见性图，并将其用于两阶段设计。
- 提出 Cross-View Consistency Filtering (CVCF)，通过可见块的多视角一致性过滤几何不正确网格。
- 提出 Visibility-Aware Attention Supervision (VAAS)，利用可见性图指导模型关注渲染视角中的可靠区域。
- 摘要称在三个 SV AG-ReID 基准上取得新的 state-of-the-art。

### 局限性
- 摘要未提供足够信息说明实验设置、数据集规模、消融实验细节和具体指标数值。
- 摘要未提供足够信息说明方法对重建失败率、幻觉纹理程度或不同 3D 重建模型质量的敏感性。
- 摘要未提供足够信息说明计算成本、训练开销或推理效率。
- 摘要未提供足够信息说明与基于生成模型合成新视角方法的详细定量对比。
- 摘要未提供足够信息说明可见性图在非单视图空对地重识别任务上的泛化能力。
- 摘要未提供足够信息说明代码和数据发布前的可复现性细节。

### 阅读优先级
高。理由：论文针对跨视角重识别中合成新视角数据不可靠这一具体问题，提出利用 3D 重建副产物可见性图进行过滤与注意力监督的两阶段方法，并声称在三个 SV AG-ReID 基准上取得新的最优结果；若关注 3D 重建与重识别交叉、合成数据可靠性或可见性感知训练，该论文具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

We address the Cross-View Object Re-Identification (ReID) task, aiming to match identities across drastically different viewpoints. We focus on Single-View Aerial-Ground ReID (SV AG-ReID), where models train on one viewpoint and must generalize to another at inference. To bridge this viewpoint gap, related work employs generative models to synthesize novel views from source images as additional training data. We leverage recent advances in large-scale single-view 3D mesh reconstruction to lift source images into textured meshes and to render them from new viewpoints. However, this pipeline produces unreliable data in two distinct ways. First, the reconstruction may fail and produce geometrically incorrect meshes, resulting in severe corruption in rendered novel views. Second, even when the geometry is correct, the rendered novel views contain hallucinated textures in regions not visible in the source image. The reconstructed mesh carries a per-pixel partition between regions visible from the source view and regions that the reconstruction model had to hallucinate, available as a deterministic byproduct of rendering. We introduce this per-pixel visibility map and exploit it in a two-stage design. Cross-View Consistency Filtering (CVCF) discards geometrically incorrect meshes by ensuring multi-view consistency between source and novel views over visible patches. Visibility-Aware Attention Supervision (VAAS) leverages the visibility map to guide the model's attention toward reliable regions of the rendered view during training. Combined, these two components enable our method, 3D-VITAL, to better leverage the synthetic signal from single-view 3D mesh reconstruction. 3D-VITAL sets a new state-of-the-art on three SV AG-ReID benchmarks. Code and data will be released at https://github.com/TurtleSmoke/3D-VITAL.

</details>

#### 2026-10-12 - BAT3R: Robust Online 3D Reconstruction with Bayesian Adaptive State Updates

**Authors:** Lijian Li, Yuanpeng He, Yudian Zheng, Chung-ju Huang, Linyu Li, Dongming Jin, Wenpin Jiao, Zhi Jin, Chi-Man Pun
**Links:** [abs](https://arxiv.org/abs/2610.16330) - [pdf](https://arxiv.org/pdf/2610.16330)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BAT3R: Robust Online 3D Reconstruction with Bayesian Adaptive State Updates
- 作者：Lijian Li, Yuanpeng He, Yudian Zheng, Chung-ju Huang, Linyu Li, Dongming Jin, Wenpin Jiao, Zhi Jin, Chi-Man Pun
- 出版日期：2026-10-12T07:47:47Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.16330

### 一句话总结
BAT3R 提出一种免训练的贝叶斯自适应状态更新框架，通过 SIG 与 BASU 两个模块缓解流式在线 3D 重建在长序列中的误差累积问题。

### 研究问题
前馈 Transformer 模型虽在 3D 视觉中取得进展，但其二次复杂度使其难以处理长视频序列。流式 3D 重建以恒定内存逐帧处理来缓解该瓶颈，但现有循环架构在长序列中会不可避免地逐渐退化。摘要指出，其原因是未能考虑观测的内在可靠性以及历史状态的累积置信度，从而导致严重的误差累积。

### 核心思路/方法
BAT3R 是一个免训练的贝叶斯自适应框架，包含两个协同模块：

- **State Innovation Gating (SIG)**：作为分布正则化器，将状态演化锚定到其几何初始化上，从而在长期推理中抑制表示漂移。
- **Bayesian-guided Adaptive State Updating (BASU)**：将状态更新重构为卡尔曼滤波框架内的递归贝叶斯推断过程。它通过信息论增益建模观测的时间可靠性，并通过交叉注意力图建模空间相关性，实现非对称的时空状态融合：已充分巩固的历史区域受到保护，避免冗余更新；而真正新颖的场景内容则被积极纳入。

### 主要贡献
- 提出 BAT3R，一个免训练的贝叶斯自适应框架，用于鲁棒的在线 3D 重建。
- 设计 SIG 模块，作为分布正则化器锚定状态演化，抑制长期推理中的表示漂移。
- 设计 BASU 模块，在卡尔曼滤波框架下将状态更新形式化为递归贝叶斯推断，结合时间可靠性与空间相关性实现非对称时空融合。
- 在 7-Scenes、TUM、ScanNet、KITTI 等标准基准上进行大量实验，摘要称 BAT3R 持续优于当前最先进的在线 3D 重建方法，且在长序列和复杂场景中增益最显著。

### 局限性
摘要未提供足够信息。摘要未提及具体失败案例、计算开销、对特定传感器或数据类型的依赖、超参数敏感性等局限。

### 阅读优先级
**高**。理由：该工作针对在线 3D 重建中长序列误差累积这一明确痛点，提出免训练框架并声称在多个标准基准上持续超越当前最优方法，且长序列与复杂场景增益最明显。若关注流式/在线 3D 重建、贝叶斯状态更新或长序列鲁棒性，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward transformer models have driven remarkable progress in 3D vision,yet their quadratic complexity renders them impractical for long video sequences. Streaming 3D reconstruction addresses this bottleneck by processing frames sequen?tially with constant memory. However, existing recurrent architectures inevitably suffer from progressive degradation over long sequences, as they fail to account for the intrinsic reliability of observations and the accumulated confidence of the historical state, leading to severe error accumulation. To address these issues, we introduce BAT3R, a training-free Bayesian adaptation framework comprising two synergistic modules: State Innovation Gating (SIG) and Bayesian-guided Adaptive State Updating (BASU). SIG acts as a distributional regularizer that anchors state evolution to its geometric initialization, effectively arresting representational drift during long-term inference. Building on this, BASU reformulates state update as a recursive Bayesian inference process within a Kalman filtering framework. By jointly modeling the temporal reliability of observations via information-theoretic gain and spatial relevance via cross-attention maps, BASU achieves an asymmetric spatio-temporal state fusion: well-consolidated historical regions are protected from redundant updates, while genuinely novel scene content is aggressively incor?porated. Extensive experiments on standard benchmarks (7-Scenes, TUM, ScanNet, KITTI, etc.) demonstrate that BAT3R consistently outperforms state-of-the-art online 3D reconstruction methods, with the most significant gains observed on long sequences and complex scenes.

</details>

#### 2026-10-12 - 3D Gaussian Splatting for Fine-grained Urban Scene Reconstruction via Semantic-guided Density Control and Loss Design

**Authors:** Yueling Liao, San Jiang, Xing Zhang, Zhongwen Hu
**Links:** [abs](https://arxiv.org/abs/2610.16292) - [pdf](https://arxiv.org/pdf/2610.16292)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D Gaussian Splatting for Fine-grained Urban Scene Reconstruction via Semantic-guided Density Control and Loss Design
- 作者：Yueling Liao, San Jiang, Xing Zhang, Zhongwen Hu
- 出版日期：2026-10-12T07:17:45Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.16292 ；PDF https://arxiv.org/pdf/2610.16292

### 一句话总结
该研究提出语义引导的 3DGS 方法 SG-GS，将 SAM 语义分割引入高斯密度控制与损失函数设计，以改善复杂城市场景中的细粒度结构重建。

### 研究问题
3D Gaussian Splatting（3DGS）虽具备高保真渲染效果与高效率优势，但在重建复杂城市场景中的细粒度结构时，仍受限于粗糙的密度控制和语义盲的损失函数。论文关注的问题是如何通过语义信息约束，提升城市场景细粒度结构重建质量，并缓解线性结构伪影和边界模糊。

### 核心思路/方法
论文提出 SG-GS，一种语义引导的 3DGS 方法，用于细粒度结构重建。其核心是将 Segment Anything Model（SAM）推导出的语义分割作为约束，系统性地整合进高斯密度控制与损失函数设计：

1. **语义约束的自适应密度控制机制**：动态为场景中不同语义区域分配梯度阈值，并引入额外的边界增强致密化策略，使新增高斯被引导至结构关键区域。
2. **多特征引导损失函数**：设计多特征引导损失，并通过分阶段渐进式训练策略逐步引入细粒度监督信号，以缓解基础损失中缺乏语义约束所导致的伪影。

### 主要贡献
- 提出 SG-GS，将 SAM 语义分割作为约束，系统性地融入 3DGS 的高斯密度控制与损失函数设计。
- 构建语义约束的自适应密度控制机制，动态分配不同语义区域的梯度阈值，并加入边界增强致密化策略。
- 设计多特征引导损失函数，结合分阶段渐进式训练策略，逐步引入细粒度监督信号。
- 在三个数据集上的实验表明，所提方法持续提升重建精度；相比原始 3DGS，PSNR 提升约 2.7% 至 5.2%，并有效缓解线性结构伪影与边界模糊。

### 局限性
摘要未提供足够信息。摘要未说明方法对 SAM 分割质量的依赖程度、失败案例、计算开销、实时性影响、数据集具体构成、消融实验细节或泛化能力限制。

### 阅读优先级
**中**。理由：该论文聚焦 3DGS 在城市场景细粒度重建中的密度控制与损失设计问题，并明确报告了 PSNR 提升和伪影缓解效果，对关注 3DGS 改进、语义引导重建和城市三维重建的研究者具有参考价值；但摘要未提供足够信息以判断其在大规模场景、实时性能、分割依赖和泛化性方面的实际表现，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has been becoming a promising 3D reconstruction technique because of its advantage of high-fidelity rendering effect with high efficiency. However, it still suffers from coarse density control and semantically blind loss functions when reconstructing the fine-grained structures in complex urban scenes. Thus, this study proposes SG-GS, a semantic-guided 3DGS method for fine-grained structure reconstruction. It takes the semantic segmentation deduced by the Segment Anything Model (SAM) as a constraint and systematically integrates it into both Gaussian density control and loss function design. On the one hand, a semantic-constrained adaptive density control mechanism is constructed, which dynamically allocates gradient thresholds to different semantic regions of the scene and introduces an additional boundary-enhanced densification strategy, so that new Gaussians are directed to structurally critical regions. On the other hand, a multi-feature guided loss function is designed, and fine-grained supervision signals are gradually introduced through a phased progressive training strategy, alleviating the artifacts caused by the lack of semantic constraints in the basic loss. Experiments on three datasets show that the proposed method consistently improves reconstruction accuracy. Compared with the original 3DGS, the PSNR increases by approximately 2.7% to 5.2%, while artifacts on linear structures and boundary blurring are effectively mitigated. The method can serve the fine-grained 3D reconstruction of urban scenes.

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-14 - Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting

**Authors:** Seungmi Choi, Ji-Hyoun Choi, Suhyun Jo, Tae-Gwon Park, Hui Yong Kim
**Links:** [abs](https://arxiv.org/abs/2610.20590) - [pdf](https://arxiv.org/pdf/2610.20590)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) methods enable efficient reconstruction of 3D scenes from sparse multi-view images in a single forward pass, without scene-specific optimization. However, existing feed-forward scene-coding pipelines first generate a complete Gaussian representation and then encode its geometry and appearance attributes separately, often involving non-differentiable operations. The resulting 'generate-then-compress' pipeline requires complex attribute-specific codec designs and limits rate-distortion performance by restricting the exploitation of cross-attribute redundancy. We propose multi-view feature coding for Gaussian splatting (MFGS), an end-to-end feed-forward framework for scene coding. Instead of compressing an explicit Gaussian representation, MFGS extracts multi-view features from the input images and encodes them into a compact bitstream. Through end-to-end rate-distortion training, MFGS learns compact multi-view features that jointly represent geometry and appearance, enabling the receiver to predict Gaussian attributes from the decoded features. We further introduce importance-guided Gaussian selection to accommodate different rendering budgets, allowing the receiver to adjust the number of Gaussians used for rendering from the same bitstream. Across RE10K, ACID, and DL3DV, MFGS achieves 99.76-99.86% bitrate savings over the generate-then-compress pipeline, as measured by BD-rate, while reducing total GMACs by 52-55% and providing an approximately 12 times end-to-end speedup.

</details>

#### 2026-10-14 - Where Should the Gaussians Go? Reusable Label-Aware Allocation for Budget-Constrained Gaussian Splatting of Cinematic CT

**Authors:** Bowen Xiang, Dingjie Su, Jon S. Heiselman, Michael I. Miga
**Links:** [abs](https://arxiv.org/abs/2610.20397) - [pdf](https://arxiv.org/pdf/2610.20397)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Anatomical labels help 3D Gaussian splatting preserve vessels in cinematic renderings of CT, but the representation is still found by optimising each patient's scene, where densification decides where Gaussians go, while real-time displays cap their number. We address one part of this process: deciding where a fixed budget of B Gaussians should be placed. We propose a reusable, labelaware allocation front end that maps a patient's CT, labels and transfer function to a density over 2mm cells and draws exactly B positions from it without per-patient optimisation; the other Gaussian attributes are still fitted per patient. The front end is learned once from per-patient optimised scenes and implemented as a population-trained neural prior and an interpretable seven-parameter visibility-aware closed form (VACF). With identical attribute fitting on 20 held-out patients at 10K-100K Gaussians, both raise vessel-masked PSNR over uniform allocation by 4.5-7.1dB and over pruning a dense voxel-aligned model by 1.6-3.3dB. The neural prior does not differ significantly from per-patient optimised allocation at any budget, and VACF is within 0.6dB of it on vessels; on 19 external patients the neural prior again matches it on vessels and VACF is within 0.7dB. As an initialisation for position optimisation, VACF allocation beats per-patient densification on vessels at 10K Gaussians and, at 25K, reaches a higher vessel PSNR after 118s of optimisation than densification after 248s. Under altered rendering presets, VACF transfers to new colours and lighting but not to a label-free transfer function, whereas the neural prior shows the opposite pattern.

</details>

#### 2026-10-14 - GLoD-LVSM: Learning Geometry-Grounded Continuous-LoD Scene Representations for Large View Synthesis Models

**Authors:** Weikai Lin, Nicholas Milef, Carl S Marshall, Grant Kaijuin Yang, Todd Keeler, Yuhao Zhu
**Links:** [abs](https://arxiv.org/abs/2610.20254) - [pdf](https://arxiv.org/pdf/2610.20254)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** view synthesis, scene representation, rendering

<details>
<summary>Abstract</summary>

Large view synthesis models (LVSMs) reconstruct scenes from sparse views and render novel views quickly, but they incur unnecessary storage and rendering costs due to token redundancy. We present GLoD-LVSM, a compact, geometry-grounded scene representation for LVSMs with continuous levels of detail. First, instead of learning a fixed set of scene anchor initializations, GLoD-LVSM learns a continuous field that initializes a flexible number of anchors to match the desired budget. A condenser then aggregates scene information into these anchors, with both the field and condenser trained end-to-end. Second, the condenser infers reference-token and anchor geometry to guide compression through geometry-grounded attention, improving rendering quality and enabling frustum culling during decoding. Compared with existing LVSM scene-compression baselines, GLoD-LVSM achieves the best trade-off between rendering quality and scene token count. Compared with the uncompressed base model, GLoD-LVSM reduces the scene-token count by 33.4% and accelerates rendering by $1.23\times$ with no quality loss. Under a relaxed quality-loss budget, the reduction increases to 85.5%, with $3.00\times$ rendering speedup. Further analysis reveals that view-synthesis supervision yields emergent scene depth and self-organized anchors that align with surfaces and adapt their density to local texture complexity. Beyond rendering, we further show that our scene representation also supports scene-semantic understanding, highlighting its potential for broader downstream tasks.

</details>

#### 2026-10-14 - VisibilitySplat: Ray-Traced Occlusion for Relighting with 3D Gaussian Splatting

**Authors:** Sven Kluge, Oliver Staadt
**Links:** [abs](https://arxiv.org/abs/2610.19847) - [pdf](https://arxiv.org/pdf/2610.19847)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, inverse rendering, relighting, rendering, radiance, splatting

<details>
<summary>Abstract</summary>

We address inverse rendering with 3D Gaussian Splatting (3DGS) by introducing explicit visibility modeling for relighting as well as material and light decomposition. Our approach augments the standard rasterized 3DGS pipeline with a sparse visibility oracle that estimates transmittance-weighted occlusion for Gaussian primitives from sampled lighting directions. This oracle is implemented using a point-based ray tracer accelerated by a bounding volume hierarchy (BVH) and queried sparsely within the inverse-rendering objectives, while the original 3DGS loop is retained for training efficiency, interactive visualization, and tooling compatibility. Shading follows a physically based rendering (PBR) formulation with a principled microfacet bidirectional reflectance distribution function (BRDF) and low-resolution high-dynamic-range (HDR) environment maps. We evaluate our method on the TensoIR synthetic dataset against baselines based on neural radiance fields (NeRFs), tensor representations, and 3DGS. The results show competitive performance and improvements over several earlier baselines for novel-view synthesis (NVS), albedo reconstruction, and relighting. Ablations indicate that explicit visibility modeling is an important contributor to relighting and material-illumination disentanglement, while pure PBR supervision can favor appearance fitting in NVS. Overall, the findings suggest that sparse, point-based visibility queries effectively complement rasterized splatting for inverse rendering while preserving the practical advantages of the 3DGS ecosystem.

</details>

#### 2026-10-14 - HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration

**Authors:** Annie Bhalla, Dennis Rotondi, Riccardo Giubilato, Kai O. Arras, Wolfgang Stuerzl
**Links:** [abs](https://arxiv.org/abs/2610.19742) - [pdf](https://arxiv.org/pdf/2610.19742)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping

<details>
<summary>Abstract</summary>

Autonomous navigation of planetary rovers is challenged by visually repetitive, featureless terrain. SLAM systems based on 3D Gaussian Splatting (3DGS) offer dense mapping but rely on RGB appearance descriptors that degrade under perceptual aliasing - a common failure mode in extraterrestrial environments where physically distinct locations appear visually identical. This paper presents HyperLoop, the first framework integrating hyperspectral imaging (HSI) into the loop closure module of a 3DGS-based SLAM system. Hyperspectral descriptors encode material-level spectral signatures complementing RGB features, providing robustness to illumination changes and visual repetitiveness. Two HSI descriptor families are introduced: Bag-of-Spectral-Words (BoSW), encoding spectral material distributions via TF-IDF weighted histograms, and PCA-K VLAD (PCAK-VLAD), capturing first-order residual statistics of PCA-compressed spectral signatures. Both are evaluated with SIFT-VLAD and NetVLAD RGB descriptors under Strict-AND and Weighted fusion strategies on a custom dataset from the Moon-Mars Outdoor Test Site (MMOTS) at DLR, comprising synchronized RGB-D and hyperspectral sequences across four planetary analog traverses (65.5 m total). A key finding is that the sensor's Red-NIR range (600-860 nm) provides limited discriminability for rock terrain: the best HSI fusion (SIFT-VLAD + BoSW, Strict-AND) achieves 5.04 cm ATE RMSE, within 1.8% of SIFT-VLAD alone (4.95 cm). The gain over NetVLAD (8.81 cm) is attributable to SIFT-VLAD, not HSI fusion. This motivates future adoption of SWIR sensors capturing diagnostic mineral absorption features absent from the 600-860 nm range for planetary SLAM missions.

</details>

#### 2026-10-14 - GS-PRM: Gaussian Visual Roadmap for Image-Goal Navigation

**Authors:** Ashraf Siddique, Kyung Min Han, Young J. Kim
**Links:** [abs](https://arxiv.org/abs/2610.19541) - [pdf](https://arxiv.org/pdf/2610.19541)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Image-goal navigation requires a global planner that connects visually specified endpoints while providing observations that a local policy can follow. Three-dimensional Gaussian Splatting (3DGS) provides map-registered RGB, opacity, and depth renderings, but does not explicitly encode navigable topology. We introduce \method, a Gaussian visual roadmap whose milestones, local connections, and visual references are constructed directly through 3DGS rendering without deriving an occupancy grid or signed distance field. We define render-based collision-free (RC-free) configurations and paths. Panoramic depth supplies conservative clearance for milestone validation and adaptive coverage, while edge-aligned orthographic rendering tests the robot's swept volume. We establish conditional soundness and sufficient conditions for deterministic query completeness and probabilistic construction completeness of GS-PRM. To validate the performance of GS-PRM, we conduct experiments in both simulated and real-world environments, demonstrating long-horizon navigation using goal-conditioned policies guided by GS-PRM. Compared with a state-of-the-art 3DGS-based navigation system, our GS-PRM-based navigation system achieves up to a twice higher average success rate and reduces travel time by up to 57.2% when both systems complete the navigation task.

</details>

#### 2026-10-14 - RDCompGS: Rate-Distortion Optimization for Compression of 3D Gaussian Splatting with Image Codecs

**Authors:** Huiping Ren, Shuai Wan, Luqian Bai, Zhang Chen, Fuzheng Yang
**Links:** [abs](https://arxiv.org/abs/2610.19538) - [pdf](https://arxiv.org/pdf/2610.19538)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables high-quality, real-time novel view synthesis but requires significant storage and transmission resources. Mapping Gaussian attributes to 2D representations enables efficient compression using mature image codecs. However, Gaussian representations that achieve comparable rendering quality are generally treated similarly during optimization, despite substantial differences in coding rate, leading to limited rate-distortion (R-D) performance after compression. To address this limitation, we propose RDCompGS, a 3DGS compression method that enables overall R-D optimization of Gaussian representations with respect to subsequent coding. A differentiable estimate of the coding rate is incorporated into the R-D optimization with rendering distortion. The rate constraint adjustment model further regulates the R-D trade-off across different compression conditions. Extensive experiments on three benchmark datasets demonstrate that RDCompGS achieves average Bjøntegaard Delta Rate reductions of 37.84% and 49.31% with H.265/HEVC and JPEG XL, respectively. The estimated rate also shows a strong correlation with the actual bit-rate under different compression conditions.

</details>

#### 2026-10-14 - Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence

**Authors:** Yuanyuan Gao, Zhirui Liu, Yuning Gong, Yifei Liu, Yifan Zhan, Kuixuan Jiao, Xiaolong Zhou, Yifan Yang, Hongjie Zhang, Xue Yang, Dan Xu, Zhihang Zhong
**Links:** [abs](https://arxiv.org/abs/2610.19502) - [pdf](https://arxiv.org/pdf/2610.19502)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, spatial intelligence

<details>
<summary>Abstract</summary>

Spatial intelligence requires scalable 3D environments that are both photorealistic and semantically grounded, yet existing indoor datasets are dominated by room-scale captures and costly LiDAR acquisition. Online real-estate platforms offer abundant panoramas of diverse multi-room homes, but sparse viewpoints and texture-poor regions make reconstruction severely under-constrained. We introduce Holi-Spatial 360, a generative reconstruction and data curation framework for converting these panoramas into annotated multi-room 3D environments. Because reconstruction quality bounds subsequent generation, our Correspondence-Guided Geometric Optimization converts feed-forward reconstruction priors into reliable cross-view constraints and builds a coherent 3D Gaussian Splatting representation as 3D spatial memory. Adapted single-image and video priors then restore appearance and complete continuous trajectories while preserving observed content. The reconstructed scenes support arbitrary RGB-D rendering and an automated curation pipeline that combines end-to-end 3D grounding with VLM-based verification. Holi360 contains over 1K multi-room 3DGS scenes, more than 100K instance annotations, and 2M spatial question-answer pairs. We also introduce the Holi360 benchmark to evaluate the spatial understanding of VLMs in real-world, multi-room indoor environments. Experiments demonstrate superior reconstruction and curation quality under sparse panoramic inputs, while fine-tuning VLMs on Holi360 substantially improves spatial reasoning capabilities.

</details>

#### 2026-10-13 - DoReMe: Dual optimization of Reconstruction and Motion estimation for self-navigated free-breathing abdominal MRI using Gaussian Splatting

**Authors:** Majd Helo, Dominik Nickel, Thomas Kuestner
**Links:** [abs](https://arxiv.org/abs/2610.19120) - [pdf](https://arxiv.org/pdf/2610.19120)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Purpose: Free-breathing abdominal MRI is limited by respiratory motion, which introduces image artifacts and k-space inconsistencies. Existing reconstruction approaches often depend on pre-estimated motion fields or external respiratory surrogate signals. We propose a coupled reconstruction-motion estimation algorithm for self-navigated free-breathing acquisition, in which motion is represented by compact Gaussian primitives and jointly refined with the image estimates during iterative reconstruction. Methods: An iterative reconstruction that alternates between data consistency updates and motion modelling was proposed. Respiratory motion was represented using Gaussian primitives. A Gaussian splatting was integrated into the reconstruction algorithm. The method was evaluated on self-navigated free-breathing Cartesian gradient-echo (GRE) acquisition in four healthy volunteers, including retrospective scan shortening experiments, and was compared with regularized compressed sensing (CS) reconstruction. Results: Respiratory motion states were reconstructed in approximately 1.5 min. Compared with CS, the proposed method improved visual image quality, particularly in coronal liver views, and better preserved anatomical structures in retrospectively shortened acquisitions. These findings provide proof of concept for the proposed method. Conclusion: The proposed coupled reconstruction-motion estimation algorithm improved visual image quality compared with CS alone. Gaussian primitives provided a compact and sufficiently flexible representation of nonrigid respiratory motion with practical runtime, supporting further scanner integration and validation in larger cohorts.

</details>

#### 2026-10-13 - CoTL: Compact Token Learning for 3D Scene Representation

**Authors:** Han Liang, Sibo Wu, Anpei Chen, Rüdiger Westermann
**Links:** [abs](https://arxiv.org/abs/2610.18446) - [pdf](https://arxiv.org/pdf/2610.18446)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, scene representation, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoTL: Compact Token Learning for 3D Scene Representation
- 作者：Han Liang, Sibo Wu, Anpei Chen, Rüdiger Westermann
- 出版日期：2026-10-13T14:17:30Z
- 分类：Neural Scene Representations & Rendering（次要分类：未提供）
- 链接：[摘要](https://arxiv.org/abs/2610.18446) / [PDF](https://arxiv.org/pdf/2610.18446)

### 一句话总结
CoTL 从无位姿多视角图像中学习一组紧凑的隐式 token，以保留场景几何与外观，并通过基于查询的高斯解码器重建可渲染的 3D 高斯场景。

### 研究问题
如何从无位姿（unposed）多视角图像中学习一个紧凑的场景表示，使其既能保留场景的几何与外观信息，又能随可用观测的增多而扩展容量，并支撑新视角合成乃至生成式任务。

### 核心思路/方法
- 编码器将输入图像压缩为每个视角的小规模隐式 token 集合，这些 token 跨视角聚合信息，形成视角一致的场景表示。
- 每增加一个视角，仅以少量且与分辨率无关的 token 扩展表示，使表示容量可随观测增加而增长。
- 为迫使该紧凑瓶颈保留足够场景信息，使用基于查询的高斯解码器：以场景无关的查询关注学习到的 token，恢复出显式、可渲染的 3D 高斯基元集合。
- 通过新视角渲染监督，经由重建的高斯场景对紧凑表示进行端到端训练。

### 主要贡献
- 提出 CoTL 框架，从无位姿多视角图像学习紧凑 token 集合以表示场景几何与外观。
- 设计的表示以少量、分辨率无关的 token 随视角扩展，形成紧凑且非结构化的 token 集合。
- 通过基于查询的高斯解码器与渲染监督，将 3D 高斯重建作为紧凑场景表示学习的有效目标。
- 在（摘要中提及的）ACID 等数据集上的实验表明，该紧凑 token 集合支持有竞争力的新视角合成，并可充当 3D 高斯场景生成的生成模型隐式空间，为 3D 视觉下游任务提供基础。

### 局限性
- 摘要未提供足够信息说明方法的具体失败情形或适用边界。
- 摘要未提供足够信息说明计算开销、训练时间或 token 数量的具体上限。
- 摘要未提供足够信息说明对无位姿设置的依赖程度及位姿估计误差的影响。
- 摘要未提供足够信息说明生成式下游任务的具体形式与定量结果。

### 阅读优先级
中。理由：该工作将紧凑 token 表示与 3D 高斯重建、生成式隐空间相连接，主题处于神经场景表示与渲染的活跃方向；但摘要仅给出方法概览与数据集名称，未提供定量对比与实现细节。若关注紧凑场景表示、3D 高斯重建或生成式 3D 场景，可优先阅读；若仅需一般性了解，可暂缓。

</details>

<details>
<summary>Abstract</summary>

We present CoTL, a framework that learns a compact set of tokens that preserves scene geometry and appearance from unposed multi-view images. Our encoder compresses the input images into small per-view sets of latent tokens that aggregate information across views to form a view-consistent scene representation. Each additional view expands the representation with only a small, resolution-independent set of tokens, allowing its capacity to grow with the available observations. To force this compact bottleneck to retain sufficient scene information, a query-based Gaussian decoder uses scene-independent queries to attend to the learned tokens and recover an explicit, renderable set of 3D Gaussian primitives. Novel-view rendering supervision trains the compact representation end to end through the reconstructed Gaussian scene. Experiments on RealEstate10K and ACID show that the resulting compact, unstructured token set supports competitive novel-view synthesis and can serve as the latent space of a generative model for 3D Gaussian scene generation. Together, these results show that 3D Gaussian reconstruction is an effective objective for compact scene representation learning and the learned token space provides a basis for broader downstream tasks in 3D vision.

</details>

#### 2026-10-13 - PLEDGE: Progressive Lossy Error-Bounded Compression of 3D Gaussian Splatting

**Authors:** Mingze Xia, Yuxiao Li, Baixi Sun, Wenbo Li, Pu Jiao, Sheng Di, Franck Cappello, Hanqi Guo, Xin Liang
**Links:** [abs](https://arxiv.org/abs/2610.17605) - [pdf](https://arxiv.org/pdf/2610.17605)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PLEDGE: Progressive Lossy Error-Bounded Compression of 3D Gaussian Splatting
- 作者：Mingze Xia, Yuxiao Li, Baixi Sun, Wenbo Li, Pu Jiao, Sheng Di, Franck Cappello, Hanqi Guo, Xin Liang
- 出版日期：2026-10-13T02:25:08Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.17605 / https://arxiv.org/pdf/2610.17605

### 一句话总结
PLEDGE 是一种免训练的、渐进的、误差有界的 3D Gaussian Splatting 压缩编解码器，将用户声明的四类容差转化为逐图元的量化上界，并组织为带显式误差界的渐进码流。

### 研究问题
现有 3D Gaussian Splatting 编解码器只在压缩后报告重建质量，用户对单个图元的失真几乎没有控制权。论文希望解决：如何让用户以可声明的容差方式控制压缩失真，并在包括未见视角在内的相机域内保持误差有界。

### 核心思路/方法
PLEDGE 是免训练、渐进、误差有界的编解码器。它将四类用户声明的容差转化为逐图元的量化边界：
1. 屏幕空间位置；
2. 由旋转和缩放引起的足迹（footprint）变形；
3. 视角相关颜色；
4. 不透明度。

这些边界在声明的相机域内适用，包括此前未见的视角。位置和不透明度被直接约束；足迹变形在光栅化器的仿射投影模型下被约束；颜色在所有观察方向上被约束。PLEDGE 将量化残差组织为渐进比特流，并为每个有效前缀提供显式误差界。

### 主要贡献
- 提出 PLEDGE：免训练、渐进、误差有界的 3DGS 编解码器。
- 将四类用户容差（位置、足迹变形、视角相关颜色、不透明度）转化为逐图元量化边界，并在声明相机域内（含未见视角）生效。
- 采用分机制的有界策略：位置与不透明度直接有界，足迹变形在仿射投影模型下有界，颜色在所有观察方向上有界。
- 将量化残差组织为渐进比特流，且每个有效前缀都有显式误差界。
- 在十三场景上验证了所有声明的逐机制边界，并展示了有竞争力的率失真性能；同时表明四类容差带来显著不同的码率开销，用户可按应用需求分配码率。

### 局限性
摘要未提供足够信息。摘要未说明具体数据集构成、基线对比对象、运行时间或内存开销、压缩比数值、是否支持动态场景，也未说明在声明相机域之外的误差行为。

### 阅读优先级
高。理由：该工作直接针对 3DGS 压缩中“用户可控失真”和“未见视角下误差有界”两个关键问题，提出免训练、渐进、误差有界的编解码框架，并声称在十三场景验证了逐机制边界与率失真性能；对关注 3DGS 压缩、渐进传输与误差可控表示的研究者有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Existing 3D Gaussian Splatting (3DGS) codecs report reconstruction quality after compression, and give users little control over the distortion of individual primitives. We present PLEDGE, a training-free, progressive, error-bounded codec that translates four user-declared tolerances into per-primitive quantization bounds: screen-space position, footprint deformation due to rotation and scale, view-dependent color, and opacity. The bounds apply throughout a declared camera domain, including previously unseen viewpoints. Position and opacity are bounded directly; footprint deformation is bounded under the rasterizer's affine projection model, and color is bounded over all viewing directions. PLEDGE organizes quantized residuals into a progressive bitstream with explicit error bounds for every valid prefix. Experiments across thirteen scenes verify all declared per-mechanism bounds and demonstrate competitive rate-distortion performance. The four tolerances incur substantially different rate costs, so users can spend rate where their application needs it.

</details>

#### 2026-10-13 - YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation

**Authors:** Hiroki Nishizawa, Takehiko Ohkawa, Nicola Scianca, Tatsuya Matsushima, Shigeo Morishima, Kei Ota
**Links:** [abs](https://arxiv.org/abs/2610.17521) - [pdf](https://arxiv.org/pdf/2610.17521)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation
- 作者：Hiroki Nishizawa, Takehiko Ohkawa, Nicola Scianca, Tatsuya Matsushima, Shigeo Morishima, Kei Ota
- 出版日期：2026-10-13T00:33:21Z
- 分类：Neural Scene Representations & Rendering（secondary_categories 未提供）
- 链接：摘要链接 https://arxiv.org/abs/2610.17521 ；PDF 链接 https://arxiv.org/pdf/2610.17521 ；项目页 https://yubi-real2sim.airoa.io

### 一句话总结
论文提出 YUBI-Real2Sim，一个基于 3D Gaussian Splatting（3DGS）的场景重建与 real-to-sim 策略评估统一框架，用于在双鱼眼腕部视角下量化重建质量对 VLA 策略评估可靠性的影响。

### 研究问题
在真实机器人上评估 VLA（Vision-Language-Action）策略成本高、耗时且难以复现，因此需要 real-to-sim 仿真来实现可扩展评估。3DGS 能快速生成 real-to-sim 场景，但用于可靠策略评估所需的重建质量尚未被量化。尤其依赖腕部鱼眼相机的策略容易受到广角视角中的视觉伪影（如空洞、漂浮物）影响，从而直接降低任务表现。

### 核心思路/方法
论文提出 YUBI-Real2Sim 统一框架，用于在双鱼眼腕部视角下进行基于 3DGS 的场景重建与 real-to-sim 策略评估。其集成流程结合了 200 度鱼眼相机采集、3DGS 训练、用于物体建模的 3D 基础模型以及基于 MuJoCo 的物理仿真。该框架在九项场景-任务对比中的八项复现了真实世界中的策略排序。论文进一步构建了覆盖两个双臂机器人平台、三个场景、三个任务和两个基于 pi0.5 的策略的基准，系统测量 real-to-sim 的排序一致性，并评估策略对反事实 3DGS 伪影（天花板空洞、漂浮物、扭曲）和采集扰动的敏感性。此外，论文在场景留出评估协议下分析了新视角质量分数能否指示策略排序的可靠性。

### 主要贡献
- 提出 YUBI-Real2Sim，一个面向双鱼眼腕部视角的 3DGS 场景重建与 real-to-sim 策略评估统一框架。
- 构建集成流程：200 度鱼眼采集、3DGS 训练、3D 基础模型物体建模和 MuJoCo 物理仿真。
- 在九项场景-任务对比中的八项复现了真实世界策略排序。
- 构建覆盖两个双臂机器人平台、三个场景、三个任务和两个基于 pi0.5 策略的基准。
- 系统测量 real-to-sim 排序一致性，并评估策略对反事实 3DGS 伪影和采集扰动的敏感性。
- 分析基于质量分数的策略排序可靠性预测能力，指出其任务依赖性与局限性。

### 局限性
- 摘要明确指出结果尚未建立通用可靠的场景接受规则。
- 基于质量分数的可靠性预测存在任务依赖性表现和局限性。
- 仅涵盖两个双臂机器人平台、三个场景、三个任务和两个基于 pi0.5 的策略，具体泛化能力摘要未提供足够信息。
- 未在九项对比中复现全部真实世界策略排序（八项中成功）。
- 摘要未提供足够信息：具体实验量化指标、伪影严重程度分级、计算开销、失败案例细节等。

### 阅读优先级
中。理由：该论文关注 real-to-sim 策略评估中一个具体且重要的问题——3DGS 重建质量对评估可靠性的影响，并给出了多平台多任务的基准与伪影敏感性分析。对从事机器人策略评估、3DGS 场景重建或 sim-to-real/real-to-sim 的研究者有参考价值。但摘要明确表示尚未建立通用可靠的场景接受规则，且实验规模有限，因此不是必须立即精读的突破性结论型工作，适合作为该方向的方法与基准参考。

</details>

<details>
<summary>Abstract</summary>

Evaluating VLA policies on real robots is costly, time-consuming, and difficult to reproduce, making real-to-sim simulation essential for scalable evaluation. While 3D Gaussian Splatting (3DGS) enables rapid real-to-sim scene generation, the reconstruction quality required for reliable policy evaluation remains unquantified. In particular, policies relying on wrist-mounted fisheye cameras (e.g., YUBI handheld gripper data) are heavily exposed to visual artifacts (holes, floaters) in wide-angle views, directly degrading task performance. To address this, we present YUBI-Real2Sim, a unified framework for 3DGS-based scene reconstruction and real-to-sim policy evaluation under dual fisheye wrist views. We develop an integrated pipeline combining 200-degree fisheye camera capture, 3DGS training, 3D foundation models for object modeling, and MuJoCo-based physical simulation, reproducing the observed real-world policy ordering in eight of nine scene-task comparisons. Using this framework, we construct a benchmark across two bimanual robot platforms, three scenes, three tasks, and dual pi0.5-based policies. This systematically measures real-to-sim rank agreement and evaluates policy sensitivity against counterfactual 3DGS artifacts (ceiling holes, floaters, warping) and capture disturbances. We further analyze whether novel-view quality scores can indicate policy-ranking reliability under a scene-held-out evaluation protocol. The results show task-dependent performance and limitations of quality-based reliability prediction, highlighting the need to assess reconstruction quality when using Real2Sim for policy evaluation. These results do not yet establish a generally reliable scene-acceptance rule. Project Page: https://yubi-real2sim.airoa.io.

</details>

#### 2026-10-12 - WorldRoPE: Probabilistic World-Centric Rotary Embedding for Multi-View Attention

**Authors:** Mijeong Kim, Kyujin Lim, Bohyung Han
**Links:** [abs](https://arxiv.org/abs/2610.16337) - [pdf](https://arxiv.org/pdf/2610.16337)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** depth estimation, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WorldRoPE: Probabilistic World-Centric Rotary Embedding for Multi-View Attention
- 作者：Mijeong Kim, Kyujin Lim, Bohyung Han
- 出版日期：2026-10-12T07:56:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.16337

### 一句话总结
WorldRoPE 提出一种以世界坐标系为中心的概率化旋转位置编码，通过将每个 patch token 映射为共享世界坐标系下的体积高斯原语，使多视角注意力机制能够处理跨视角坐标不一致和深度不确定性。

### 研究问题
在多视角 Transformer 中，RoPE 被广泛用于编码相对位置。然而，多视角场景下每个图像的 patch 坐标是独立定义的：同一个 3D 点在不同视角下会具有不同坐标，因此这些独立坐标不足以建立跨视角对应关系。论文旨在解决多视角注意力中由于坐标定义不一致和深度不确定性导致的跨视角位置编码困难。

### 核心思路/方法
WorldRoPE 是一种用于多视角注意力的概率化、世界坐标系中心的旋转位置编码。其核心做法是：在每一层，将每个 patch token 反投影为一组位于共享世界坐标系中的体积高斯原语。这些原语表示该 token 的多个可能 3D 支撑区域，联合捕捉替代深度假设、深度不确定性以及其 patch 视锥的有限空间范围。

当一个 key token 的支撑被投影到 query 视角时，会在 query 图像中诱导出一个关于该 key 可能出现位置的分布。WorldRoPE 以闭式形式在这个分布上对旋转算子进行积分，根据混合权重组合投影原语中心处的旋转，并施加依赖协方差的衰减。这使得注意力对 query 视角中不确定的 key 位置不那么敏感，且无需栅格化或 warp token 特征。当支撑坍缩为一个点时，该公式退化为确定性 RoPE。跨层之间，预测的几何引导跨视角注意力，而更新后的特征又反过来精化下一层使用的几何。

### 主要贡献
- 提出 WorldRoPE，一种以世界坐标系为中心的概率化旋转位置编码，用于多视角注意力。
- 通过将 patch token 反投影为共享世界坐标系中的体积高斯原语，联合建模替代深度假设、深度不确定性和 patch 视锥的空间范围。
- 以闭式形式在投影位置分布上积分旋转算子，组合投影原语中心处的旋转并按混合权重加权，同时引入协方差相关衰减，使注意力对不确定 key 位置更鲁棒。
- 该方法在支撑坍缩为点时退化为确定性 RoPE。
- 跨层实现几何与特征的相互引导与精化：预测几何引导跨视角注意力，更新特征精化下一层几何。
- 在新视角合成、深度估计和 3D 几何重建任务上验证了 WorldRoPE 对多视角 Transformer 的有效性。

### 局限性
摘要未提供足够信息。摘要中未给出具体实验设置、对比基线、失败案例、计算开销、原语数量选择、消融细节或适用边界等局限相关信息。

### 阅读优先级
高。理由：该工作针对多视角 Transformer 中位置编码与跨视角对应这一基础问题提出概率化世界中心建模，方法思路具有通用性，且摘要声称在新视角合成、深度估计和 3D 几何重建三类任务上验证有效；对神经场景表示、多视角注意力及相关几何感知 Transformer 方向的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Rotary Positional Embedding (RoPE) is widely used to encode relative positions in Transformers. In multi-view settings, however, patch coordinates are defined independently in each image: the same 3D point can therefore have different coordinates across views, making them insufficient for establishing cross-view correspondences. We introduce WorldRoPE, a probabilistic world-centric RoPE for multi-view attention. At each layer, WorldRoPE back-projects each patch token into a set of volumetric Gaussian primitives in a shared world frame. These primitives represent multiple plausible 3D supports for a token, jointly capturing alternative depth hypotheses, depth uncertainty, and the finite spatial extent of its patch frustum. When a key token's support is projected into a query view, it induces a distribution over where that key may appear in the query image. WorldRoPE integrates the rotary operator over this distribution in closed form, combining rotations at the projected primitive centers according to their mixture weights with covariance-dependent attenuation. This makes attention less sensitive to uncertain key locations in the query view, without rasterizing or warping token features. The formulation reduces to deterministic RoPE when the support collapses to a point. Across layers, the predicted geometry guides cross-view attention, while the updated features refine the geometry used at the next layer. Experiments on novel view synthesis, depth estimation, and 3D geometry reconstruction demonstrate the effectiveness of WorldRoPE for multi-view Transformers.

</details>

#### 2026-10-12 - DIGS: Distribution-Informed Gaussian Splatting for Training-Free Open-Vocabulary 3D Segmentation

**Authors:** Zhifan Zeng, Wenbo Xiao, Arcot Sowmya, Changming Sun
**Links:** [abs](https://arxiv.org/abs/2610.16177) - [pdf](https://arxiv.org/pdf/2610.16177)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DIGS: Distribution-Informed Gaussian Splatting for Training-Free Open-Vocabulary 3D Segmentation
- 作者：Zhifan Zeng, Wenbo Xiao, Arcot Sowmya, Changming Sun
- 出版日期：2026-10-12T04:52:38Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.16177 ；PDF：https://arxiv.org/pdf/2610.16177

### 一句话总结
DIGS 是一种无需训练的开词汇 3D 高斯分割框架，通过为每个高斯基元维护显式的 top-M 标签分布，并结合类无关建图与多模态实例编码，缓解边界高斯的硬判定问题，从而提升分割与渲染边界的稳定性。

### 研究问题
论文关注开放词汇 3D 高斯分割中的核心问题：现有方法通常为每个高斯基元绑定单一语义特征（通过逐场景梯度训练或闭式蒸馏），导致跨越多个 2D 实例的边界高斯被迫做出硬决策，进而降低检索准确率，并在渲染时产生不稳定的掩码边界。

### 核心思路/方法
DIGS 是一个无需训练的框架，包含两个阶段：类无关建图（class-agnostic mapping）与多模态编码（multi-modal encoding），将实例发现与语言命名解耦。
- 高斯层面：提出分布信息表示（distribution-informed representation），为每个基元维护显式的 top-M 标签分布，并使用 tempered Dirichlet 规则更新。边界基元保留多峰标签分布，使后期 argmax 渲染器能够恢复干净的实例边界。
- 建图层面：使用双向状态机将这些分布聚合为持久的类无关实例本体（instance ontology）。
- 实例编码层面：融合每个实例孤立 3D footprint 的 CLIP 视觉嵌入与 LLM 生成属性描述的 CLIP 文本嵌入，以区分视觉相似的实例。

### 主要贡献
- 提出无需训练的 DIGS 框架，将实例发现与语言命名解耦。
- 引入分布信息的高斯基元表示，用 top-M 标签分布与 tempered Dirichlet 更新替代单一特征绑定，保留边界多峰分布以改善边界恢复。
- 设计双向状态机，将基元分布聚合为持久的类无关实例本体。
- 在实例级编码中融合 CLIP 视觉嵌入与 LLM 生成属性描述的 CLIP 文本嵌入，缓解视觉相似实例的歧义。
- 实验表明：在单张 A100 上，DIGS 在 LERF-OVS 上每场景完成建图与实例编码耗时 1.0–3.2 分钟（取决于是否启用 LLM 融合），原生 3D 查询耗时 5.4 ms；在 LERF-OVS 上达到 71.95% 平均 mIoU，优于无需训练的 SFS 和基于训练的 LaGa 基线；在 LERF-Mask 与 3D-OVS 上取得最高平均 mIoU，并在 Replica 上按各自评估协议超过 Gaga 与 ObjectGS。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、适用范围限制、对特定数据集或硬件的依赖边界，也未讨论超参数敏感性、LLM 生成描述的质量影响或方法在更复杂场景中的可扩展性。

### 阅读优先级
高。理由：该论文针对开放词汇 3D 高斯分割中边界高斯硬判定这一明确问题，提出无需训练且效率较高的框架，并在多个基准上报告了优于训练/无需训练基线的结果；若关注 3D 高斯分割、开放词汇理解或无需训练方法，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Open-vocabulary 3D Gaussian segmentation typically binds semantic features to the per-Gaussian state via per-scene gradient training (1-4 h) or the more recent closed-form distillation. Both commit each primitive to a single feature; therefore, boundary Gaussians spanning multiple 2D instances are forced into a hard decision that degrades retrieval accuracy and yields unstable mask boundaries at render time. We present DIGS, a training-free framework with two stages, class-agnostic mapping and multi-modal encoding, that decouples instance discovery from linguistic naming. At the Gaussian level, our distribution-informed representation maintains an explicit top-$M$ label distribution per primitive, updated by a tempered Dirichlet rule; preservation of multi-peaked label distributions at boundary primitives allows a late-argmax renderer to recover clean instance boundaries. A bidirectional state machine aggregates these distributions into a persistent class-agnostic instance ontology. The instance-level encoding stage then fuses the CLIP visual embedding of each instance's isolated 3D footprint with the CLIP-text embedding of an LLM-generated attribute description, disambiguating visually similar instances. On a single A100, DIGS completes mapping and instance encoding on LERF-OVS in 1.0-3.2 min per scene, depending on whether LLM fusion is enabled, and serves native 3D queries in 5.4 ms. It reaches 71.95% mean mIoU on LERF-OVS, outperforming both the training-free SFS and training-based LaGa baselines. DIGS also achieves the highest mean mIoU on LERF-Mask and 3D-OVS and surpasses Gaga and ObjectGS on Replica under their respective evaluation protocols. Code is available at https://github.com/ZephyrZos/DIGS.

</details>

#### 2026-10-08 - OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs

**Authors:** You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu
**Links:** [abs](https://arxiv.org/abs/2610.12461) - [pdf](https://arxiv.org/pdf/2610.12461)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs
- 作者：You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu
- 出版日期：2026-10-08T17:59:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.12461

### 一句话总结
OuroWorld 提出了一个无掩码框架，将任意静态 3D Gaussian Splatting 场景转化为可从任意视角无缝循环播放、具有多样动态的 3D 电影图（3D cinemagraph）。

### 研究问题
现有 3D 世界模型虽能生成照片级真实、可探索的场景，但这些场景在时间上是冻结的（"remain frozen in time"），缺乏动态。论文旨在让任意静态 3D 场景"活起来"，产生生动、多样且能无缝循环的动态效果。

### 核心思路/方法
- 采用无掩码（mask-free）框架，将静态 3D Gaussian Splatting 场景转化为 3D cinemagraph。
- 使用视觉-语言模型（VLM）推断合理的动态，并引导视频模型合成一段参考视频。
- 将该参考视频提升（lift）并补全为多视角视频。
- 针对上述不完美监督，提出 **Inconsistency-Robust Periodic 4DGS**：
  - 使用傅里叶级数变形场（Fourier-series deformation field），从构造上保证循环性。
  - 使用锚定在参考视角的 Grounded Drift Field，吸收跨视角不一致性。
- 与先前仅限于类流体运动的欧拉方法不同，该方法可捕捉一般形变、物体运动和光照变化。
- 引入无需真值（ground-truth-free）的评估，覆盖生动性、自然性、循环接缝连贯性和场景质量。

### 主要贡献
- 提出 OuroWorld 无掩码框架，可将任意静态 3DGS 场景转为多视角、无缝循环的 3D cinemagraph。
- 提出 Inconsistency-Robust Periodic 4DGS，通过傅里叶级数变形场保证循环性，并通过 Grounded Drift Field 处理跨视角不一致。
- 方法可处理一般形变、物体运动与光照变化，突破先前欧拉方法限于类流体运动的限制。
- 提出无需真值的评估体系，涵盖生动性、自然性、循环接缝连贯性与场景质量。
- 在 39 个重建与生成场景上，OuroWorld 优于所有基线，并在用户研究中赢得 70.8%–99.0% 的对比。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作面向 3D 场景动态化与无缝循环这一具体且具应用价值的问题，提出了构造性保证循环的变形场与跨视角一致性处理机制，并给出多维度评估与用户研究结果，方法与评估设计均有较明确的创新点，值得关注 3D 场景表示与渲染方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we lift and complete into multi-view videos. To learn from this imperfect supervision, we propose Inconsistency-Robust Periodic 4DGS: a Fourier-series deformation field guarantees looping by construction, while a Grounded Drift Field anchored at the reference view absorbs cross-view inconsistency. Unlike prior Eulerian methods limited to fluid-like motion, we capture general deformation, object motion, and illumination change. We introduce a ground-truth-free evaluation covering vividness, naturalness, loop seam coherence, and scene quality. On 39 reconstructed and generated scenes, OuroWorld outperforms all baselines and wins 70.8%-99.0% of user-study comparisons. Project page: https://ouroworld.userwei.com

</details>

#### 2026-10-08 - LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation

**Authors:** Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim
**Links:** [abs](https://arxiv.org/abs/2610.12442) - [pdf](https://arxiv.org/pdf/2610.12442)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, rendering, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation
- 作者：Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim
- 出版日期：2026-10-08T17:58:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.12442) / [PDF](https://arxiv.org/pdf/2610.12442)

### 一句话总结
LEGO 提出一种免于“提升到点云”的跨视角视频生成条件方案：用一个学习式视角合成器直接渲染自我中心视角，为视频扩散模型提供更利于结构对齐的条件。

### 研究问题
从单段外视角（exocentric）视频生成自我中心视角（egocentric）视频，属于新视角合成中的困难情形：两相机重叠区域很小，目标视角中大量内容未被观测到。

摘要指出，当前最先进方法通过显式重建场景来处理该问题——估计深度、将视频提升为点云，再从自我中心相机重新渲染，以此作为视频扩散模型的条件。但这种确定性映射会把每个像素指派到唯一的重投影位置：纹理得以保留，深度误差却会转化为内容错位。

因此论文追问：视频扩散模型究竟应当接收什么样的条件？

### 核心思路/方法
- 提出“免提升”（lifting-free）方案：不依赖深度、点云或重投影，而是使用一个学习式视角合成器（LVSM 风格的 transformer），经微调后直接渲染自我中心视角，在内部解决跨视角对应关系。
- 与显式方法的确定性映射不同，该合成器采用概率式映射：依据学习到的对应分布，将每个区域在候选源位置间做平均。其效果是保留结构，但细纹理会被平均掉。
- 论文论证这一权衡适合扩散生成器：扩散模型的去噪训练本就擅长恢复细节，因此有效的条件应优先保证结构对齐，而非锐利度。
- 该分布的集中程度还可导出逐区域置信度，用于两方面：掩蔽低置信度区域；在早期形成布局的去噪步骤中，引导生成器关注高置信度区域。

### 主要贡献
- 提出免提升的 exocentric-to-egocentric 视频生成思路，用学习式视角合成器替代“深度估计—点云提升—重渲染”的显式管线。
- 论证概率式视角合成所导致的“结构保留、纹理模糊”特性与扩散生成器的去噪能力互补，从而明确条件设计应以结构对齐为先。
- 利用对应分布的集中度获得逐区域置信度，并用于掩蔽与早期去噪引导。
- 摘要声称该方法持续优于最先进的显式管线，且无需重新训练即可泛化到其他数据集。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集名称、评价指标与定量结果。
- 摘要未提供足够信息说明合成器的训练细节、微调数据需求与计算开销。
- 摘要未提供足够信息说明置信度阈值选择、掩蔽策略的具体实现及其失败情形。
- 摘要未提供足够信息说明“泛化到其他数据集”的具体范围与验证条件。
- 摘要未提供足够信息说明该方法在极端视角差异或严重遮挡下的表现边界。

### 阅读优先级
高。理由：该论文针对跨视角视频生成中“显式重建条件是否最优”这一基础问题提出明确的反思路线，并用扩散模型与视角合成的能力分工来支撑设计选择；同时声称优于 SOTA 且具备免重训练泛化能力，属于值得优先核验方法与实验细节的工作。

</details>

<details>
<summary>Abstract</summary>

Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This deterministic mapping assigns each pixel to a single reprojected location, which preserves texture but translates depth errors into misplaced content. We ask what a video diffusion model should receive as its condition and propose a lifting-free answer: a learned view synthesizer, an LVSM-style transformer fine-tuned to render the egocentric view directly without depth, point clouds, or reprojection, resolving cross-view correspondence internally. In contrast, its probabilistic mapping averages each region over candidate source locations according to a learned correspondence distribution, preserving structure while fine texture is averaged away. We argue that this trade-off suits a diffusion generator, whose denoising training excels at restoring detail, so an effective condition should prioritize structural alignment over sharpness. This distribution's concentration also yields a per-region confidence, used both to mask low-confidence regions and to guide the generator toward high-confidence areas during early layout-forming denoising steps. Our approach consistently outperforms the state-of-the-art explicit pipeline and generalizes to other datasets without retraining. The synthesizer thus supplies view structure, and the diffusion model its detail.

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-14 - GeoThinker-$F$: Endogenous Predictive World Representations for Fast Spatial Intelligence

**Authors:** Haoyuan Li, Qihang Cao, Huanyuan Zhou, Xin Hu, Sijia Chen, Zihan Guo, Kun Xiang, Yunshuang Nie, Tao Tang, Xinlong Zheng, Jia-Wang Bian, Xianming Liu, Xiaodan Liang
**Links:** [abs](https://arxiv.org/abs/2610.20592) - [pdf](https://arxiv.org/pdf/2610.20592)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>Abstract</summary>

Existing geometry-aware Multimodal Large Language Models (MLLMs) increasingly rely on external 3D encoders to provide structural priors, but executing these additional encoder paths at inference introduces substantial latency and computational overhead. We propose GeoThinker-$F$, an efficient framework that internalizes spatiotemporal perception by transforming causal MLLM hidden states into predictive latent world representations. Our key insight is that intermediate semantic representations contain sufficient information to predict useful representations of current geometry and future semantics, without requiring an exact reproduction of features from a dedicated 3D encoder. To realize this idea, GeoThinker-$F$ adopts a decoupled two-stage training strategy. In the first stage, the MLLM backbone is frozen while lightweight Latent Frame Prediction (LFP) heads learn from an offline 3D geometry expert and next-frame semantic targets. In the second stage, the external expert is removed, and the model is jointly optimized to generate and selectively integrate its self-predicted priors through a specialized Spatial-Grounded Temporal (SGT) Fusion module. Extensive evaluations show that GeoThinker-$F$ eliminates runtime dependence on external 3D geometry encoders while maintaining competitive performance across diverse spatial intelligence benchmarks. It achieves up to a $3.6\times$ inference speedup, reducing latency from $1.45\,\mathrm{s}$ to $0.40\,\mathrm{s}$ while retaining strong spatial reasoning performance.

</details>

#### 2026-10-14 - Feasibility of a Patient-Specific Digital Twin for Ventriculoperitoneal Shunt Trajectory Planning

**Authors:** Kritsanavis Chongsrid, Vich Yindeedej, Supaporn Konmun, Xulei Yang, Si Yong Yeo
**Links:** [abs](https://arxiv.org/abs/2610.20074) - [pdf](https://arxiv.org/pdf/2610.20074)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** digital twin

<details>
<summary>Abstract</summary>

Catheter obstruction is the commonest cause of shunt failure; freehand insertion at Keen's point leaves the tip free in cerebrospinal fluid in only one case in ten. We built a digital twin that reconstructs skull, scalp, ear and ventricles from preoperative CT by deterministic geometry, searches every entry around Keen's point for the perpendicular trajectory with the longest intraventricular length under safety constraints, and returns the plan as two ruler measurements from the ear and two depths. Executed freehand in 11 consecutive adults (IDEAL Stage 2a), it achieved Hayhurst Grade 1 placement in 10 of 11 against 22 of 213 historically (p = 9 x 10^-9), median entry and angular deviations 2.5 mm and 5.9 degrees, 1.4 cm more intraventricular catheter than Keen's point, and no intraoperative complication. The technique was unchanged; the gain came from choosing entry and depth per patient. Whether it lowers revision is the next stage's hypothesis.

</details>

#### 2026-10-14 - FOMI: A Force-Feedback Manipulation Interface for Teaching Contact-Rich Manipulation

**Authors:** Yishu Shen, Yiming Luo, Ruilin Wang, Bowen Yang, Shuai Yang, Fangyi Xu, Yujun Shen, Fu Zhang, Boyu Zhou, Yinghao Xu
**Links:** [abs](https://arxiv.org/abs/2610.19839) - [pdf](https://arxiv.org/pdf/2610.19839)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>Abstract</summary>

Robot-free collection with handheld interfaces enables scalable acquisition of human demonstrations for policy learning. However, existing handheld interfaces often provide limited intuitive force feedback, making contact-rich demonstration collection challenging for human operators. To address this, we present FOMI, a force-feedback manipulation interface with a scissor-shaped mechanism, which transmits object interaction forces directly to the operator's hands through actuation links without force sensors. This intuitive force feedback supports real-time action adjustment during robot-free collection of contact-rich demonstrations. Around FOMI, we build a demonstration collection system that integrates sensor calibration, data acquisition, and synchronization for robot-free collection. By further mapping pose changes and gripper opening of FOMI to robot end-effector poses and gripper commands, the system also supports teleoperation. Across four contact-rich tasks, FOMI improves collection efficiency by approximately 29% and 18% over the best baselines in robot-free collection and teleoperation, respectively. Demonstrations collected with FOMI in both modes enable policies to perform challenging contact-rich manipulation tasks with high success rates.

</details>

#### 2026-10-14 - What Matters for World Modeling in Vision-Language-Action Models?

**Authors:** Qisen Ma, Yixiang Chen, Yuan Xu, Peiyan Li, Jiabing Yang, Kai Wang, Jianhua Yang, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang
**Links:** [abs](https://arxiv.org/abs/2610.19825) - [pdf](https://arxiv.org/pdf/2610.19825)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world model, world modeling

<details>
<summary>Abstract</summary>

Integrating world models into Vision-Language-Action models (VLAs) has emerged as a promising direction, enabling policies to anticipate future dynamics beyond reactive observation-to-action mapping. However, existing approaches vary simultaneously in their world representations, integration paradigms, and policy backbones, making it difficult to determine what truly matters for effective world model integration. To disentangle these factors, we categorize existing efforts into four representative paradigms, namely Implicit Future Alignment, Explicit Future Query, MoT Future Expert, and External World Predictor. We instantiate each within a unified framework and systematically evaluate these paradigms with diverse world representations and policy backbones across in-domain, out-of-domain, long-horizon, dynamic, few-shot, and real-world settings. Our study yields four main findings: 1) world representation effectiveness is paradigm-dependent, whereas 2D semantic representations offer robust, cross-paradigm gains; 2) no single paradigm is universally optimal, yet the decoupled MoT Future Expert offers competitive overall performance, particularly in OOD robustness; 3) world modeling consistently benefits policies built on standard VLMs, while decoupled designs exhibit greater compatibility with pretrained VLAs; and 4) world modeling improves performance over action-only baselines across multiple settings, with notable gains on long-horizon and dynamic tasks. Project page and video demonstrations are available at https://dylanmqs.github.io/WM-in-VLAs/.

</details>

#### 2026-10-14 - FPV-CRASH: A Dataset for Offline Crash Moment Localization in Drone First-Person-View Videos

**Authors:** Jifan Zhang, Tingyu Wang, Qian Liu, Zhedong Zheng
**Links:** [abs](https://arxiv.org/abs/2610.19785) - [pdf](https://arxiv.org/pdf/2610.19785)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization

<details>
<summary>Abstract</summary>

Crash Moment Localization aims to localize the major physical impact that interrupts controlled flight in an onboard first-person-view (FPV) video recorded by a drone, thereby providing a temporal reference for retrospective crash analysis in aerial robotics. However, existing crash-video datasets predominantly target surveillance or dash-camera footage, and their annotation schemes and task formulations are not designed for temporal localization of the major physical impact in UAV onboard FPV videos. To address this gap, we present FPV-CRASH, a dataset and fixed-protocol reference evaluation for offline Crash Moment Localization in drone FPV videos. FPV-CRASH contains 1,052 drone FPV clips (526 Crash and 526 Normal); each Crash clip has a single-frame reference annotation for the Crash Moment, and every clip is paired with four English captions automatically generated from sampled frames and the known Crash/Normal label. Normal clips carry no timestamp target and provide training-time background supervision. The captions support an auxiliary Text-to-Video Retrieval task, whereas localization inference remains video-only. We further provide a heatmap-based reference model that estimates a continuous Crash Moment timestamp from sparsely sampled frames. Under the fixed, non-source-disjoint clip-level protocol, the reference model reduces MAE from 1.12 s for the strongest fixed timing-prior baseline to 0.56 s (a 50% relative reduction) and achieves a median absolute error (MedAE) of 0.33 s; the fraction of clips localized within 0.5 s rises from 37.14% to 65.71%. The release includes annotations, available source video identifiers and URLs, clipping metadata, fixed split lists, and preprocessing code so that the reportable portion can be reconstructed without redistributing source footage. At submission time, all source-compilation URLs remained accessible.

</details>

#### 2026-10-14 - $S^3$-Nav: Structured Spatial-Semantic Decision Making for Language-Guided Robot Navigation

**Authors:** Chaemin Lee, Hae Min Cho
**Links:** [abs](https://arxiv.org/abs/2610.19431) - [pdf](https://arxiv.org/pdf/2610.19431)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>Abstract</summary>

This paper presents $S^3$-Nav, a structured spatial-semantic decision-making framework for language-guided robot navigation under partial observability. Rather than assuming a complete environment representation in advance, $S^3$-Nav incrementally constructs persistent spatial-semantic state while exposing only a capacity-controlled, task-conditioned view to the high-level policy. This separation decouples what the robot must retain from what the policy needs to inspect, allowing decision complexity to be controlled without discarding grounded evidence required for subsequent reasoning and validation. High-level navigation outputs remain provisional and are independently grounded and validated against persistent semantic evidence and current geometric observations before physical execution or task termination. Evaluations across multiple environments and object- and relation-goal tasks demonstrate that separating persistent state, decision-facing evidence, and execution authority improves closed-loop navigation reliability while reducing policy reasoning cost.

</details>

#### 2026-10-14 - A VR Training System for Robot-Assisted Vascular Intervention with Dual-Mode Control and Model-Based Interaction Response

**Authors:** Yining Shang, Shuxiang Guo, Sheng Cao, Pengcheng Li, Bin Wang, Mingchao Ding
**Links:** [abs](https://arxiv.org/abs/2610.19413) - [pdf](https://arxiv.org/pdf/2610.19413)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, VR, virtual reality

<details>
<summary>Abstract</summary>

Virtual reality training for robot-assisted vascular intervention requires accurate robotic control and effective feedback on guidewire--vessel interactions. This paper presents a VR training system combining asynchronous dual-mode command mapping with sensorless interaction estimation. The system supports velocity-controlled navigation and position-driven incremental manipulation. Guidewire deformation and a Hunt--Crossley-type contact response are combined and temporally filtered to estimate interaction intensity, while trajectory-based visualization supports post-procedure review. Tests confirmed distinct command-dispatch patterns across three velocity gears and the position mode. During hybrid-scene navigation, the estimated response remained low during straight insertion and increased as the guidewire bent within the vascular model. Trajectory analysis yielded a model-derived cumulative trauma work (CTW) value of 15.166 in normalized units and localized regions of elevated interaction. In a preliminary study with 15 novices, physical-phantom task success increased from 53.3% to 93.3% after VR training, while mean completion time decreased from 132.4 s to 96.7 s. These results demonstrate the system's dual-mode operation, deformation-sensitive feedback, and potential to improve subsequent physical-phantom task performance.

</details>

#### 2026-10-13 - Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors

**Authors:** Henry Che, Xuanchi Ren, Sanja Fidler, Shenlong Wang, Laura Leal-Taixé, Shengyu Huang
**Links:** [abs](https://arxiv.org/abs/2610.19201) - [pdf](https://arxiv.org/pdf/2610.19201)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>Abstract</summary>

We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors. Existing LiDAR simulators largely follow one of two complementary paradigms: reconstruction-based methods preserve the geometry of a captured scene but require lengthy per-scene optimization, whereas generative methods amortize learning across data but lack the consistency needed for long-horizon rollouts. LidarVerse brings both paradigms into a single, unified conditional generative framework. A universal tokenizer maps LiDAR range sequences into a shared latent space, where a bidirectional teacher learns a common interface for conditioning on a LiDAR prefix, an HD-Map, a persistent spatial cache, and optionally, text. Varying the available scene evidence turns the same model into a generator of new worlds, a point-cloud forecaster, or a generalizable resimulator of observed scenes without per-scene optimization. We distill the teacher into a four-step autoregressive causal student and maintain both a rolling temporal K/V cache and a world-aligned spatial cache, enabling persistent long-horizon rollouts with real-time inference at 11 FPS on a single H100 GPU. LidarVerse achieves state-of-the-art performance on most reported metrics across all three evaluation protocols, while its tokenizer supports 32-, 64-, and 128-beam LiDAR and generalizes to an unseen scanning pattern. These results demonstrate that generative and reconstruction-grounded LiDAR simulation can be realized within one model, providing the core capabilities for future closed-loop sensor simulation.

</details>

#### 2026-10-13 - EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

**Authors:** Yunsong Zhou, Xuekun Jiang, Haiqi Shen, Hangxu Liu, Chaojian Shi, Yujie Liu, Jingyuan Li, Haoran Yang, Jiafei Cao, Dongzhan Zhou, Dong Wang, Yao Mu, Chunhua Shen, Weinan Zhang
**Links:** [abs](https://arxiv.org/abs/2610.18872) - [pdf](https://arxiv.org/pdf/2610.18872)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ
- 作者：Yunsong Zhou, Xuekun Jiang, Haiqi Shen, Hangxu Liu, Chaojian Shi, Yujie Liu, Jingyuan Li, Haoran Yang, Jiafei Cao, Dongzhan Zhou, Dong Wang, Yao Mu, Chunhua Shen, Weinan Zhang
- 出版日期：2026-10-13T17:59:55Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.18872) / [PDF](https://arxiv.org/pdf/2610.18872)

### 一句话总结
本文提出 EgoExplorer——一个基于可穿戴系统、时长 100 小时的视觉—运动—触觉人类 loco-manipulation 观测数据集，并配套提出 Calibrate-Complete-Constrain 流程，以在稀疏体感条件下重建全身运动与手部精细动作。

### 研究问题
- 从人类演示中学习人形机器人的 loco-manipulation，需要观察移动、姿态与物体交互如何随任务展开而共同演化。
- 要在多种环境中扩大采集规模，需要轻量、便携的采集系统。
- 摘要指出，现有数据集只能提供这种协调过程的部分视图，缺乏对上述多模态协同的完整覆盖。

### 核心思路/方法
- 构建 EgoExplorer：一个 100 小时的视觉—运动—触觉人类 loco-manipulation 观测系统，采用可穿戴系统采集，侧重专业活动场景。
- 数据内容：连续记录将第一视角视频与重建的全身运动、细粒度手指关节动作、触觉观测对齐，并附有 step-level（步骤级）描述。
- 针对稀疏体感条件下的覆盖问题，提出 Calibrate-Complete-Constrain 流程：
  - 可复用标定：在运动推断前固定参与者几何结构与传感器佩戴方式，从而将安装偏移与关节动作解耦。
  - 时间先验：补全未观测的关节运动。
  - 分层约束：促进测量一致性、时间连续性与几何一致性——摘要指出这些性质仅靠运动合理性并不能保证。
- 初步研究探索了多模态生成与条件化，以及在仿真中结合全身控制的人形重定向。

### 主要贡献
- 提出 EgoExplorer，一个 100 小时、以专业活动为重点、基于可穿戴系统的视觉—运动—触觉人类 loco-manipulation 观测数据集，将第一视角视频与全身运动、手指精细动作、触觉观测及步骤级描述对齐。
- 提出 Calibrate-Complete-Constrain 流程，用于在稀疏体感条件下实现上述覆盖。
- 实验结果表明：相较于最强基线，该方法在身体点误差上降低 71.9%（以 tracker 拟合结果为参考）；匹配评估还显示手部稳定性与接触估计有所提升。
- 初步研究探索了多模态生成与条件化，以及仿真中结合全身控制的人形重定向。

### 局限性
- 摘要未提供足够信息说明数据集的具体规模分布、参与者数量、场景多样性及任务类型覆盖范围。
- 摘要未提供足够信息说明标定方法对传感器配置变化的敏感性与泛化能力。
- 摘要未提供足够信息说明手部稳定性与接触估计提升的具体数值与评估协议。
- 摘要未提供足够信息说明多模态生成、条件化与人形重定向初步研究的定量结果。
- 摘要未提供足够信息说明可穿戴系统在真实采集中的舒适性、遮挡与长时间佩戴带来的影响。

### 阅读优先级
- 优先级：中
- 理由：该工作面向人形机器人从人类演示中学习 loco-manipulation 的数据瓶颈，提出的 100 小时多模态数据集与稀疏体感重建流程具有一定针对性，且摘要给出了身体点误差降低 71.9% 的量化结果。但摘要未披露数据集规模细节、评估协议与初步研究的定量验证，是否与具体研究需求匹配需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer, a 100-hour vision-motion-touch observatory of human loco-manipulation built with a wearable system. With an emphasis on professional activities, its continuous recordings align egocentric video with reconstructed whole-body motion, fine-grained finger articulation, and tactile observations, accompanied by step-level descriptions. To achieve this coverage with sparse body sensing, we develop the Calibrate-Complete-Constrain pipeline. Concretely, reusable calibration fixes participant geometry and sensor attachments before motion inference to disentangle mounting offsets from articulation. A temporal prior then completes unobserved joint motion, while layered constraints promote measurement agreement, temporal continuity, and geometric consistency, properties that motion plausibility alone does not guarantee. Against tracker-fitted references, the method reduces body-point error by 71.9% relative to the strongest baseline; matched evaluations also show gains in hand stability and contact estimation. Preliminary studies explore multimodal generation and conditioning alongside humanoid retargeting with whole-body control in simulation.

</details>

#### 2026-10-13 - ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation

**Authors:** Zijun Xu, Wendi Chen, Xinkai Wang, Jiachen Zou, Hongjin Chen, Hairuo Liu, Bokai Lin, Shihao Ma, Ke Ma, Zhiwei Zhang, Zhuohao Yan, Ke Wu, Haoming Song, Xueqi Li, Chuan Wen, Jieru Zhao, Wenchao Ding, Cewu Lu, Lixin Yang
**Links:** [abs](https://arxiv.org/abs/2610.18852) - [pdf](https://arxiv.org/pdf/2610.18852)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation
- 作者：Zijun Xu, Wendi Chen, Xinkai Wang, Jiachen Zou, Hongjin Chen, Hairuo Liu, Bokai Lin, Shihao Ma, Ke Ma, Zhiwei Zhang, Zhuohao Yan, Ke Wu, Haoming Song, Xueqi Li, Chuan Wen, Jieru Zhao, Wenchao Ding, Cewu Lu, Lixin Yang
- 出版日期：2026-10-13T17:58:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.18852) / [PDF](https://arxiv.org/pdf/2610.18852)

### 一句话总结
ForceWAM 将“任务兼容的交互结果预测”与“局部动作如何改变接触”这两类知识解耦，分别通过世界模型和逆动力学模型从示范数据与任务无关的 play 数据中学习，以提升接触丰富操作的成功率。

### 研究问题
接触丰富任务中，专家示范能展示如何完成任务，但对“不同动作下交互力如何响应”的覆盖有限；任务无关的 play 数据虽包含更广泛的接触动力学经验，却不指定任务目标。论文关注如何同时利用这两类数据，以支撑接触丰富操作中的力调节执行。

### 核心思路/方法
论文提出 ForceWAM，一种 force world action model，将知识拆分为两部分：
1. 世界模型从成功示范中学习，联合预测未来视频与六轴力/力矩轨迹；这些未来共同描述任务中运动与接触的预期演化。
2. 独立的逆动力学模型（IDM）从任务数据与 play 数据中学习，将当前观测和记录的视觉-力/力矩未来映射为对应机器人动作；play 数据由此提供面向目标执行的力响应知识。
部署时，IDM 反应式地将生成的未来转化为动作，并在世界模型更新之间结合新鲜力/力矩反馈复用这些未来。

### 主要贡献
- 提出 ForceWAM，将任务兼容的交互结果知识与局部动作改变接触的知识进行解耦。
- 设计世界模型从成功示范中联合预测未来视频与六轴力/力矩轨迹。
- 设计独立 IDM，同时从任务与 play 数据中学习，使 play 数据提供力响应知识以服务目标导向执行。
- 在真实机器人力调节滑动、有/无扰动的盒子翻转以及圆环放置任务中，报告 85%–95% 平均成功率，超过世界建模与反应式基线。
- 实验显示，加入任务无关 play 数据可将成功率提升 15–45 个百分点，体现其对学习接触丰富执行的价值。

### 局限性
摘要未提供足够信息。摘要未给出失败模式、方法假设、计算开销、泛化边界或 play 数据质量影响等细节。

### 阅读优先级
高。理由：该论文直接处理接触丰富操作中示范数据覆盖不足与任务无关 play 数据利用的问题，提出解耦式世界模型与逆动力学框架，并在多个真实机器人任务上报告了明确的成功率提升；对机器人力控制、世界模型和机器人学习方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Expert demonstrations show how to complete contact-rich tasks, but provide limited coverage of how interaction forces respond to different actions. Task-agnostic play provides broader experience of contact dynamics without specifying task goals. To fully leverage these two types of data, we introduce ForceWAM, a force world action model that decouples knowledge of task-compatible interaction outcomes from knowledge of how local actions change contact. A world model learns from successful demonstrations to jointly predict future video and six-axis force/torque trajectories. Together, these futures describe the expected evolution of motion and contact during the task. A separate inverse dynamics model (IDM) learns from both task and play, mapping current observations and recorded visual-wrench futures to their associated robot actions. Play data thus provide knowledge of force responses for goal-directed execution. At deployment, the IDM reactively translates generated futures into actions, reusing them with fresh wrench feedback between world-model updates. Across real-robot force-regulated sliding, box flipping with and without disturbances, and ring placement, ForceWAM achieves $85$-$95\%$ mean success, surpassing world-modeling and reactive baselines. Our experiments further show that adding task-agnostic play data improves success by $15$-$45$ percentage points, demonstrating its value for learning contact-rich execution. Project page and code are available at https://force-wam.github.io/.

</details>

#### 2026-10-13 - Perception Beyond the Visible: Incompleteness-Aware Scene Understanding for Robot Autonomy

**Authors:** Rohit Mohan
**Links:** [abs](https://arxiv.org/abs/2610.18670) - [pdf](https://arxiv.org/pdf/2610.18670)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Perception Beyond the Visible: Incompleteness-Aware Scene Understanding for Robot Autonomy
- 作者：Rohit Mohan
- 出版日期：2026-10-13T16:29:25Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.18670 ；PDF https://arxiv.org/pdf/2610.18670

### 一句话总结
本文提出一个面向机器人自主性的“不完整性感知场景理解”研究愿景，围绕证据不完整、知识不完整与传感器可靠性不完整三类挑战，规划从现有感知贡献到以信念为中心的 4D 场景表示与主动感知的研究路线。

### 研究问题
论文关注机器人自主性中的可靠感知问题。摘要指出，许多感知系统只建模可见场景区域、依赖固定的语义类别，并假设传感器测量可靠；这些假设在遮挡、新物体出现和传感器退化时会失效。因此，核心问题是：机器人如何在部分且带噪声的观测条件下，对世界进行可靠推理。

### 核心思路/方法
作者提出“不完整性感知场景理解”（incompleteness-aware scene understanding）的研究愿景，并将其组织为三个基本挑战：
1. 不完整的证据（incomplete evidence）；
2. 不完整的知识（incomplete knowledge）；
3. 不完整的传感器可靠性（incomplete sensor reliability）。

摘要中提到，作者围绕这些挑战讨论了其在以下方向的研究贡献：amodal perception（非模态感知）、semantic occupancy forecasting（语义占据预测）、open-world scene understanding（开放世界场景理解）、label-efficient learning（标签高效学习）以及 uncertainty-guided multi-modal fusion（不确定性引导的多模态融合）。

在此基础上，作者进一步提出未来研究方向：面向以信念为中心的 4D 场景表示（belief-centric 4D scene representations），旨在联合建模几何、语义、运动和不确定性；并讨论主动感知（active sensing）与安全自适应策略（safe adaptation strategies），使机器人能够通过交互降低不确定性。最终目标是形成经过校准且可操作的场景表示，以支持动态开放世界环境中的可靠自主性。

### 主要贡献
- 提出一个关于“不完整性感知场景理解”的研究愿景，明确围绕证据、知识和传感器可靠性三类不完整性挑战进行组织。
- 梳理了作者在多个相关方向上的研究贡献，包括非模态感知、语义占据预测、开放世界场景理解、标签高效学习和不确定性引导的多模态融合。
- 提出未来研究方向：以信念为中心的 4D 场景表示，联合建模几何、语义、运动和不确定性。
- 讨论通过主动感知与安全自适应策略，让机器人通过交互降低不确定性，并指向校准且可操作的场景表示。

### 局限性
摘要未提供足够信息说明具体实验设置、数据集、定量结果、方法细节、与基线方法的比较，以及所提出未来方向的实际验证情况。论文属于研究愿景类摘要，摘要未提供足够信息以评估其技术实现的完整性与泛化能力。

### 阅读优先级
高。理由：该文聚焦机器人自主性中遮挡、新物体和传感器退化等关键感知失效场景，问题定位明确；同时提出从现有贡献到以信念为中心的 4D 场景表示与主动感知的整合路线，若后续有完整方法或实验支撑，对具身智能、机器人感知和多模态融合方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Reliable robot autonomy requires reasoning about the world from partial and noisy observations. However, many perception systems model only visible scene regions, rely on fixed semantic categories, and assume reliable sensor measurements. These assumptions break under occlusion, novel object encounters, and sensor degradation. In this paper, I present a research vision for incompleteness-aware scene understanding. I organize this vision around three fundamental challenges: incomplete evidence, incomplete knowledge, and incomplete sensor reliability. I discuss my research contributions toward addressing these challenges through amodal perception, semantic occupancy forecasting, open-world scene understanding, label-efficient learning, and uncertainty-guided multi-modal fusion. Building on these contributions, I outline future research directions toward belief-centric 4D scene representations. These representations aim to jointly model geometry, semantics, motion, and uncertainty. I also discuss active sensing and safe adaptation strategies that allow robots to reduce uncertainty through interaction. The goal is to develop calibrated and actionable scene representations that support reliable autonomy in dynamic, open-world environments.

</details>

#### 2026-10-13 - Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence

**Authors:** Thinker Team, Peng Gao, Jichao Jiao, Chen Liao, Daqin Luo, Yiming Ma, Baiyu Pan, Hailin Shi, Jiyuan Wang, Xiangming Xu, Xiongwei Zhao
**Links:** [abs](https://arxiv.org/abs/2610.18447) - [pdf](https://arxiv.org/pdf/2610.18447)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, embodied AI, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence
- 作者：Thinker Team, Peng Gao, Jichao Jiao, Chen Liao, Daqin Luo, Yiming Ma, Baiyu Pan, Hailin Shi, Jiyuan Wang, Xiangming Xu, Xiongwei Zhao
- 出版日期：2026-10-13T14:18:47Z
- 分类：Embodied / Robotics / AR Applications（二级分类摘要未提供信息）
- 链接：摘要页 https://arxiv.org/abs/2610.18447 ；PDF https://arxiv.org/pdf/2610.18447

### 一句话总结
Thinker-WM 提出一个统一的多模态世界模型，通过共享的 Unified Dynamics Transformer 与模态专用编解码器，在表示层面联合建模并生成 RGB、度量深度与机器人动作，从而在同一套参数下支持多种具身世界模型功能。

### 研究问题
现有世界模型系统在建模的模态与支持的功能上往往相互割裂：视觉动态、几何结构与可执行动作通常通过分离的接口或下游模块耦合，而不是在共享的动力学模型中被联合表示与演化。论文关注的核心问题是：能否在表示层面将外观、几何与动作统一为一个共同的动态表示，并由共享参数联合演化，同时保留各自不同的输出结构，进而支撑多种具身任务功能。

### 核心思路/方法
- 提出 Thinker-WM：一个统一的多模态世界模型，联合建模并生成 RGB、度量深度和机器人动作。
- 结构上采用共享中间模块 Unified Dynamics Transformer，并配备模态专用编码器与解码器。
- 多模态统一发生在表示层面：外观、几何、动作被转换为共同的动态表示，由共享参数联合演化，同时保留各自不同的输出结构。
- 同一套参数化支持多种功能：联合视频-动作生成、世界预测、策略推断、动作条件生成、视频到动作生成、逆动力学。
- 为检验共享表示是否包含动作相关信息，引入轻量级 motion probe，结果显示冻结的视觉表示中包含可恢复的运动信息。
- 训练数据为异构语料：约 20K 小时第一人称视频、10K 小时真实机器人数据、1K 小时仿真数据，其中约 4K 小时真实机器人数据带对齐深度监督。

### 主要贡献
- 提出以共享动态表示为核心的统一多模态世界模型 Thinker-WM，在表示层面统一视觉动态、几何结构与可执行动作。
- 用同一套参数化支持多种具身世界模型功能，包括联合视频-动作生成、世界预测、策略推断、动作条件生成、视频到动作生成与逆动力学。
- 引入 lightweight motion probe，验证冻结视觉表示中包含可恢复的运动信息。
- 构建并利用大规模异构训练语料（约 20K 小时第一人称视频、10K 小时真实机器人数据、1K 小时仿真数据，含约 4K 小时带对齐深度监督的真实机器人数据）。
- 实验中在 EWMBench、WorldOlympiad 与 WorldArena 上排名第一，并通过受控研究展示动作条件、几何交互与多任务训练在共享表示下的收益。

### 局限性
摘要未提供足够信息。论文摘要未提及模型规模、推理效率、失败案例、数据偏差、具体评测指标数值或真实机器人部署限制等局限相关内容。

### 阅读优先级
高。理由：该工作针对具身智能世界模型中模态与功能割裂这一关键问题，提出在表示层面统一 RGB、深度与动作的共享动力学建模方案，并在多个具身世界模型评测中报告排名第一，同时通过 motion probe 与受控研究验证共享表示的有效性，对具身智能、机器人策略学习与世界模型方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support. In particular, visual dynamics, geometric structure, and executable action are commonly coupled through separate interfaces or downstream modules rather than being jointly represented and evolved within a shared dynamics model. In this work, we present Thinker-WM, a unified multimodal world model that jointly models and generates RGB, metric depth, and robot action through a shared intermediate Unified Dynamics Transformer with modality-specific encoders and decoders. The model performs multimodal unification at the representation level: appearance, geometry, and action are transformed into a common dynamic representation and jointly evolved by shared parameters, while their distinct output structures are preserved. The same parameterization supports multiple functions, including joint video-action generation, world prediction, policy inference, action-conditioned generation, video-to-action generation, and inverse dynamics. To examine whether the shared representation captures action-related information, we introduce a lightweight motion probe that shows the frozen visual representation contains recoverable motion information. Thinker-WM is trained on a heterogeneous corpus comprising approximately 20K hours of egocentric video, 10K hours of real-robot data, and 1K hours of simulation data, including approximately 4K hours of real-robot data with aligned depth supervision. Extensive experiments demonstrate strong performance across embodied world-model evaluations. Thinker-WM ranks first on EWMBench, WorldOlympiad and WorldArena, while controlled studies further demonstrate the benefits of action conditioning, geometric interaction, and multi-function training within the shared representation.

</details>

#### 2026-10-13 - DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations

**Authors:** Jun Tian, Yingjie Niu, Ruo Chen, Hongyi Lin, Chao Li
**Links:** [abs](https://arxiv.org/abs/2610.18373) - [pdf](https://arxiv.org/pdf/2610.18373)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, robot navigation, autonomous driving, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations
- 作者：Jun Tian, Yingjie Niu, Ruo Chen, Hongyi Lin, Chao Li
- 出版日期：2026-10-13T13:28:59Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.18373) / [PDF](https://arxiv.org/pdf/2610.18373)

### 一句话总结
DR-VLA 提出一种基于 Mixture-of-Transformers 的框架，通过域不变场景表示（DISR）将第一人称网络视频中的人类导航经验迁移到四足机器人，并结合视觉语言理解、潜在世界建模与流匹配动作专家来预测可执行轨迹。

### 研究问题
四足机器人在户外配送中需要理解复杂场景、预判变化并以符合社会规范的方式导航，但机器人演示数据的大规模采集成本高昂，难以支撑泛化。第一人称网络视频虽然包含丰富的人类导航经验，却因视角和运动差异难以直接迁移到机器人。论文要解决的核心问题是：如何利用第一人称网络视频中的人类导航经验，服务于四足机器人的户外导航。

### 核心思路/方法
论文提出 DR-VLA，一个 Mixture-of-Transformers 框架，通过域不变场景表示（DISR）实现人类导航经验向机器人的迁移。框架结合了视觉语言理解、潜在世界建模与一个流匹配动作专家。
论文构建了 EgoLynx 数据集，包含 10,000 小时精选第一人称网络视频（EgoLynx-Web）和 2,000 段在真实配送中采集的遥操作机器人导航片段（EgoLynx-Robot）。
训练流程为：先在无动作标签的 EgoLynx-Web 上预训练理解专家和世界专家，再将模型适配到机器人观测，并在 EgoLynx-Robot 上训练动作专家以预测可执行轨迹。
论文还提出四足导航评分（QNS），一个融合安全性、指令遵从性、舒适性和进展性的伪闭环指标。

### 主要贡献
- 提出 DR-VLA 框架，利用域不变场景表示从第一人称网络视频迁移人类导航经验到四足机器人导航。
- 构建 EgoLynx 数据集，包括 10,000 小时第一人称网络视频 EgoLynx-Web 和 2,000 段真实配送遥操作机器人导航片段 EgoLynx-Robot。
- 提出四足导航评分 QNS，综合安全性、指令遵从性、舒适性和进展性。
- 在 EgoLynx-Robot 留出测试集上，DR-VLA 相较该指标下最佳竞争结果，QNS 提升约 5%，开环最终朝向误差（FHE）降低 14.6%。
- 消融实验表明网络视频预训练提升了泛化能力，且模型关键组件对性能有贡献。
- 作为未来预测目标，DISR 优于五种通用视觉表示，并在无需专门几何标签或点云构建目标的情况下，性能接近任务特定 3D 感知。
- 在 NAVSIM v1 上不经网络视频预训练单独训练，DR-VLA 达到 92.1 PDMS，提示该框架也适用于自动驾驶。

### 局限性
- 摘要未提供足够信息说明模型在真实户外配送场景中的闭环部署表现。
- 摘要未提供足够信息说明 EgoLynx 数据集的具体采集成本、标注质量与覆盖场景范围。
- 摘要未提供足够信息说明 DISR 的具体构造方式及其域不变性的验证细节。
- 摘要未提供足够信息说明 QNS 指标的设计细节、权重与验证方式。
- 摘要未提供足够信息说明与更多基线方法的全面比较结果。
- 摘要未提供足够信息说明 92.1 PDMS 在 NAVSIM v1 上的具体实验设置与对比基线。

### 阅读优先级
高。理由：该论文针对四足机器人户外导航中真实数据稀缺与人类视频迁移这一关键问题，提出了完整框架、大规模数据集与新评价指标，并报告了多任务（四足导航与自动驾驶）上的量化收益，且摘要中明确给出消融与表示对比结论，对该方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways. Robot demonstrations are costly to collect at the scale needed for generalization. Egocentric web videos offer abundant human navigation experience, but differences in viewpoint and motion make this experience difficult to transfer to robots. We introduce DR-VLA, a Mixture-of-Transformers framework that transfers human navigation experience through a domain-invariant scene representation (DISR). The framework combines vision-language understanding and latent world modeling with a flow-matching action expert. We introduce EgoLynx, comprising 10,000 hours of curated egocentric web video (EgoLynx-Web) and 2,000 clips of teleoperated robot navigation collected during real-world deliveries (EgoLynx-Robot). We pretrain the understanding and world experts on EgoLynx-Web without action labels, then adapt the model to robot observations and train the action expert on EgoLynx-Robot to predict executable trajectories. We also propose the Quadruped Navigation Score (QNS), a pseudo-closed-loop metric combining safety, instruction compliance, comfort, and progress. On the held-out EgoLynx-Robot test split, DR-VLA improves QNS by approximately 5% and reduces open-loop final heading error (FHE) by 14.6%, each relative to the best competing result for that metric. Ablations show that web-video pretraining improves generalization and that the model's key components contribute to performance. As a future-prediction target, DISR outperforms five generic visual representations and yields performance close to task-specific 3D perception without dedicated geometric labels or point clouds for target construction. Trained separately on NAVSIM v1 without web pretraining, DR-VLA achieves 92.1 PDMS, suggesting that the framework also applies to autonomous driving.

</details>

#### 2026-10-13 - CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation

**Authors:** Shuqi Wang, Yiwei Zheng, Pingrui Zhang, Yue Gao, Xiang Yin
**Links:** [abs](https://arxiv.org/abs/2610.18321) - [pdf](https://arxiv.org/pdf/2610.18321)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation
- 作者：Shuqi Wang, Yiwei Zheng, Pingrui Zhang, Yue Gao, Xiang Yin
- 出版日期：2026-10-13T13:01:20Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.18321

### 一句话总结
CoSMO 将视觉语言模型嵌入与共形预测结合，构建可随危险类别动态扩展且带覆盖保证的语义安全地图，用于开放世界下的机器人安全导航。

### 研究问题
安全自主导航不仅需要几何避障，还需要语义感知：不同物体类别需要不同的安全间隙，且机器人探索新环境时相关类别集合会动态扩展。视觉语言模型虽能提供丰富的语义表示，但其置信度校准差，原始预测难以直接用于安全关键规划；现有共形预测方法假设固定标签集与平稳数据，难以适用于开放世界场景。

### 核心思路/方法
提出 CoSMO 语义安全地图框架，将 VLM 嵌入转换为校准后的覆盖集合与安全感知的障碍物膨胀，并在动态扩展的危险词表上运作，即使在分布偏移下也适用。方法引入共形预测以提供覆盖保证，并处理延迟专家反馈的情形。

### 主要贡献
- 提出面向开放世界安全机器人导航的共形语义地图框架 CoSMO，支持动态扩展的危险词表。
- 将 VLM 嵌入转化为校准覆盖集合与安全感知障碍物膨胀，在分布偏移下仍可用。
- 在 Matterport3D 数据集上，相比仅几何基线减少 61.6% 的语义碰撞，并在延迟专家反馈下维持形式化覆盖保证。
- 四足机器人真实实验达到 90.73% 的长期经验覆盖率，目标为 90%。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性表现。
- 摘要未提供足够信息说明对 VLM 类型或规模的依赖性与敏感性。
- 摘要未提供足够信息说明危险词表扩展机制的具体触发条件与更新频率。
- 摘要未提供足够信息说明真实实验的环境规模、任务复杂度与失败案例。

### 阅读优先级
高。理由：该论文针对开放世界机器人安全导航中 VLM 置信度不可靠与共形预测固定标签假设之间的关键矛盾，提出带形式化覆盖保证的语义安全地图，并在标准数据集与真实四足机器人上验证，问题重要且方法具有明确的安全保障属性。

</details>

<details>
<summary>Abstract</summary>

Safe autonomous navigation requires not only geometric obstacle avoidance but also semantic awareness. Different object categories demand different safety clearances, and the set of relevant categories may expand as the robot explores novel environments. Vision-language models (VLMs) offer rich semantic representations for building maps of unknown scenes, yet their confidence scores are poorly calibrated, making raw predictions unreliable for safety-critical planning. Conformal prediction (CP) can provide coverage guarantees, but existing methods assume a fixed label set and stationary data, limiting their use in open-world settings. We propose Conformal Semantic Mapping for Open-World Safe Robot Navigation (CoSMO), a semantic safety mapping framework that transforms VLM embeddings into calibrated coverage sets and safety-aware obstacle dilations over a dynamically expanding hazard vocabulary, even under distribution shift. Experiments on the Matterport3D (MP3D) dataset show that CoSMO reduces semantic collisions by 61.6% relative to a geometry-only baseline, while maintaining formal coverage guarantees even under delayed expert feedback. Real-world experiments on a quadruped robot further demonstrate generalization by achieving long-run empirical coverage of 90.73% against the 90% target. Project website: https://yangming911.github.io/cosmo-page/.

</details>

#### 2026-10-13 - Cross-Embodiment Affordance Transfer for Robotic Manipulation

**Authors:** Sawera Yaseen, Serge Thill, Rekha Raja
**Links:** [abs](https://arxiv.org/abs/2610.18194) - [pdf](https://arxiv.org/pdf/2610.18194)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cross-Embodiment Affordance Transfer for Robotic Manipulation
- 作者：Sawera Yaseen, Serge Thill, Rekha Raja
- 出版日期：2026-10-13T11:31:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.18194 ；https://arxiv.org/pdf/2610.18194

### 一句话总结
该论文提出一个框架，将面向人类手的 affordance 标注转化为以机器人几何与物理约束为条件的、机器人可执行的 affordance 预测。

### 研究问题
机器人操作系统的 affordance 通常从人类标注数据集中学习，这类标注反映的是人手可交互的可能性，而非特定机器人的物理约束。例如，人手认为可抓取的物体表面区域，对机器人而言可能在几何上不可达或机械上不可行。摘要指出，这种不匹配很少被显式处理。因此，论文关注的问题是：如何将人类 affordance 标注转化为机器人可执行的 affordance 预测，并且使预测依赖于具体机器人的物理属性。

### 核心思路/方法
论文提出的框架将人类 affordance 标注转化为机器人可执行的 affordance 预测，并以机器人物理属性为条件。网络输入包括物体的 3D 点云，以及编码机器人几何和约束的描述符；输出是物体表面哪些区域对该机器人物理上可执行。模型训练时使用人类标注的 affordance，并结合仿真中多次采样接近试验的机器人执行结果，由执行结果决定哪些区域对机器人可执行。评估在家庭物体数据集上进行，使用 UR5e 机械臂上的两种平行夹爪配置。框架优于不接收机器人信息的模型。

### 主要贡献
- 提出将人类 affordance 标注转化为机器人可执行 affordance 预测的框架，且预测以机器人物理属性为条件。
- 网络结合物体 3D 点云与编码机器人几何和约束的描述符，预测机器人可执行的物体表面区域。
- 利用仿真中多次采样接近试验的执行结果，与人类 affordance 标注共同训练模型。
- 在家庭物体数据集上、UR5e 机械臂与两种平行夹爪配置下评估，结果表明所提框架优于不接收机器人信息的模型。
- 实验说明 affordance 预测必须以机器人为条件，仅靠人类标注不足以学习机器人可执行的 affordance 表示。

### 局限性
摘要未提供足够信息说明以下方面：真实机器人实验情况；仿真到现实的迁移效果；对更多机器人本体、夹爪类型或物体类别的泛化能力；对标注噪声、点云质量或执行试验采样数量的敏感性；计算成本与推理效率；失败案例或方法在何种条件下不适用。

### 阅读优先级
高。理由：该论文聚焦机器人操作中一个明确且重要的问题，即人类 affordance 标注与具体机器人物理约束之间的不匹配；摘要给出了清晰的方法框架、训练信号来源和评估设置，并报告了相对基线的性能优势。对关注机器人 affordance、跨本体迁移、操作学习和以机器人为条件的学习方法的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation systems commonly learn object affordances from human-annotated datasets, which reflect interaction possibilities for a human hand rather than the physical constraints of a specific robot. For example, a surface region of an object identified as graspable by a human annotator may be geometrically unreachable or mechanically infeasible for a robot, yet this mismatch is rarely addressed explicitly. To tackle this challenge, we proposed a framework that translates human affordance annotations into robot-executable affordance predictions conditioned on the physical properties of the robot. The network predicts which surface regions of an object are physically executable by the robot, given a 3D point cloud of an object and a descriptor encoding the robot's geometry and constraints. The model was trained using human-annotated affordances together with robotic execution outcomes from multiple sampled approach trials in simulation, where execution outcomes determined which regions are executable for the robot. The evaluation was performed on a household objects dataset using two parallel-jaw gripper configurations on a UR5e robot arm. The framework outperformed a model that does not receive information about the robot. The experimental results demonstrated that affordance prediction must be conditioned on the robot and that human annotations alone are insufficient for learning robot-executable affordance representations.

</details>

#### 2026-10-13 - LynxScenes: A Large-Scale Real-World Benchmark for Outdoor Wheel-Legged Robot Perception, Navigation, Imagination and Reconstruction

**Authors:** Jun Tian, Hao Wu, Ruo Chen, Yili Liao, Hongyi Lin, Jincheng Yu, Chao Li, Yingjie Niu
**Links:** [abs](https://arxiv.org/abs/2610.18093) - [pdf](https://arxiv.org/pdf/2610.18093)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, robot perception, robot navigation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LynxScenes: A Large-Scale Real-World Benchmark for Outdoor Wheel-Legged Robot Perception, Navigation, Imagination and Reconstruction
- 作者：Jun Tian, Hao Wu, Ruo Chen, Yili Liao, Hongyi Lin, Jincheng Yu, Chao Li, Yingjie Niu
- 出版日期：2026-10-13T10:12:55Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.18093 ，PDF https://arxiv.org/pdf/2610.18093

### 一句话总结
LynxScenes 是一个基于 LYNX M20 轮腿机器人采集的大规模真实户外数据集与基准，用于统一支持轮腿机器人在人机共享户外空间中的感知、导航、未来场景预测与场景重建任务。

### 研究问题
论文关注的是：轮腿机器人在与人类共享的户外空间中运行时，需要同时具备准确感知、符合社会规范的导航、未来场景推理以及场景重建能力；但现有数据集通常只孤立地支持其中某一类能力，且很少在真实轮腿机器人平台上提供密集的空间与行为级监督。因此，论文试图构建一个能够同时覆盖上述多类能力、并提供丰富真实标注的大规模基准。

### 核心思路/方法
论文提出 LynxScenes，一个使用 LYNX M20 轮腿机器人采集的大规模真实世界数据集与基准。其数据规模包括约 100K 个 30 秒导航片段，总计 833.6 小时、3,294.7 公里，以及 3.0M 标注帧。同步记录包含四个鱼眼相机、双 LiDAR、IMU、里程计和机器人状态。标注包括 27 个类别下的 20.82M 有向 3D 框、13.89M 道路结构标注，以及组织为三层的 20 条导航指令，并与连续未来轨迹对齐。LynxScenes 支持四个互补任务：指令条件下的轨迹预测、基于 BEV 的 3D 物体与道路结构感知、未来场景预测和多视角场景重建。针对轨迹预测，论文还引入基于日志回放的伪闭环评估器，用于衡量安全性、进展性和指令遵循性，而不仅限于轨迹模仿。论文对代表性导航、感知、世界模型和重建方法进行了广泛评估，结果显示近距离户外机器人导航仍存在显著挑战。数据集与评估工具包计划公开发布。

### 主要贡献
- 提出 LynxScenes：一个使用 LYNX M20 轮腿机器人采集的大规模真实户外数据集与基准。
- 提供大规模真实数据：约 100K 个 30 秒导航片段、833.6 小时、3,294.7 公里、3.0M 标注帧。
- 提供多传感器同步记录：四个鱼眼相机、双 LiDAR、IMU、里程计和机器人状态。
- 提供密集标注：20.82M 有向 3D 框、27 个类别、13.89M 道路结构标注，以及三层 20 条导航指令并与连续未来轨迹对齐。
- 统一支持四类互补任务：指令条件下的轨迹预测、基于 BEV 的感知、未来场景预测、多视角场景重建。
- 针对轨迹预测提出基于日志回放的伪闭环评估器，用于衡量安全性、进展性和指令遵循性。
- 对代表性导航、感知、世界模型和重建方法进行评估，揭示近距离户外机器人导航仍面临显著挑战。

### 局限性
摘要未提供足够信息。摘要中未说明数据集采集的具体地理范围、天气与光照多样性、标注质量控制流程、伦理与隐私处理方式、与现有数据集的定量对比细节、各任务的具体评价指标数值，以及数据集和工具包的确切公开发布时间与许可协议。

### 阅读优先级
高。理由：该论文提出的是大规模真实世界轮腿机器人数据集与基准，覆盖感知、导航、未来场景预测和场景重建四类任务，并包含多传感器同步记录、密集 3D 与道路结构标注、导航指令及伪闭环评估器；对于关注户外机器人感知、具身导航和多任务基准的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Wheel-legged robots operating in outdoor spaces shared with humans require accurate perception, socially compliant navigation, future-scene reasoning, and scene reconstruction. However, existing datasets typically support these capabilities in isolation and rarely provide dense spatial and behavior-level supervision on real wheel-legged platforms. We introduce LynxScenes, a large-scale real-world dataset and benchmark collected with a LYNX M20 wheel-legged robot. It contains approximately 100K 30-s navigation clips spanning 833.6 h and 3,294.7 km, with 3.0M annotated frames. The synchronized recordings include four fisheye cameras, dual LiDARs, IMU, odometry, and robot states. Annotations comprise 20.82M oriented 3D boxes across 27 categories, 13.89M road-structure annotations, and 20 navigation instructions organized into three layers and aligned with continuous future trajectories. LynxScenes supports four complementary tasks: instruction-conditioned trajectory prediction, BEV-based perception of 3D objects and road structures, future scene prediction, and multi-view scene reconstruction. For trajectory prediction, we further introduce a log-replay-based pseudo-closed-loop evaluator that measures safety, progress, and instruction compliance beyond trajectory imitation. Extensive evaluations across representative navigation, perception, world-model, and reconstruction methods reveal substantial remaining challenges in close-range outdoor robot navigation. The dataset and evaluation toolkit are planned for public release.

</details>

#### 2026-10-12 - ConDenseDrive: Knowledge-Dense, Token-Sparse Visual Encoder for End-to-End Autonomous Driving

**Authors:** Shengzhen Li, Yongkang Li, Hao Gao, Chenxi Wu, Yajing Sun, Lu Hou, Wenyu Liu, Xinggang Wang
**Links:** [abs](https://arxiv.org/abs/2610.16908) - [pdf](https://arxiv.org/pdf/2610.16908)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ConDenseDrive: Knowledge-Dense, Token-Sparse Visual Encoder for End-to-End Autonomous Driving
- 作者：Shengzhen Li, Yongkang Li, Hao Gao, Chenxi Wu, Yajing Sun, Lu Hou, Wenyu Liu, Xinggang Wang
- 出版日期：2026-10-12T14:56:31Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.16908

### 一句话总结
ConDenseDrive 提出一种“知识密集、token 稀疏”的视觉编码器，用于端到端自动驾驶，通过三阶段框架在提升规划性能的同时实现 2.0 倍推理加速。

### 研究问题
端到端驾驶需要在严格延迟约束下支持场景理解与轨迹规划，要求丰富的时空表征。然而，现有大多数系统从通用图像预训练初始化视觉编码器，并对每个相机视角和输入帧的所有 patch token 进行稠密处理，这限制了表征质量与推理效率。

### 核心思路/方法
论文提出 ConDenseDrive，一个知识密集且 token 稀疏的视觉编码器，采用三阶段框架：
1. **知识密集化**：从三个视觉基础模型中蒸馏互补的视觉、语义和几何知识，使编码器具备密集知识。
2. **多帧适应与时空上下文整合**：将蒸馏后的编码器适应到多帧端到端驾驶场景，并将时空上下文整合到 register token 中用于规划。
3. **token 稀疏化**：通过 register 引导的 token 压缩，减少冗余 patch 计算，实现 2.0 倍加速，同时提升规划性能。

### 主要贡献
- 提出 ConDenseDrive，一种知识密集、token 稀疏的视觉编码器，用于端到端自动驾驶。
- 设计三阶段框架：知识蒸馏、多帧适应与 register token 时空整合、register 引导的 token 压缩。
- 在 NAVSIM v1 上达到 94.5 PDMS，在 NAVSIM v2 上达到 90.8 EPDMS，在 HUGSIM 零样本评估中达到 37.4 HD-Score。
- 实现 2.0 倍推理加速，同时提升规划性能。
- 大量实验与定性分析表明，视觉编码器设计是通往可靠且高效端到端驾驶的有效路径。

### 局限性
摘要未提供足够信息。摘要中未说明方法的具体失败案例、适用边界、计算资源需求细节、不同场景下的泛化限制或消融实验的完整结果。

### 阅读优先级
**高**。理由：该论文聚焦端到端自动驾驶中视觉编码器的效率与表征质量问题，提出明确的三阶段方法，并在 NAVSIM v1/v2 和 HUGSIM 上报告了具体指标与 2.0 倍加速效果，属于该领域较有代表性的系统设计工作；且发表于 Embodied / Robotics / AR Applications 分类，对相关方向研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

End-to-end driving requires rich spatiotemporal representations to support scene understanding and trajectory planning under strict latency constraints. However, most systems initialize their visual encoders from generic image pretraining and densely process all patch tokens for each camera view and input frame, limiting both representation quality and inference efficiency. To address these challenges, we present ConDenseDrive, a knowledge-dense and token-sparse visual encoder for end-to-end autonomous driving. Our three-stage framework first makes the encoder knowledge-dense by distilling complementary visual, semantic, and geometric knowledge from three vision foundation models. It then adapts the distilled encoder to multi-frame end-to-end driving and integrates spatiotemporal context into register tokens for planning. Finally, it makes the encoder token-sparse by applying register-guided token compression, reducing redundant patch computation and yielding a 2.0$\times$ speedup while improving planning performance. ConDenseDrive achieves 94.5 PDMS on NAVSIM v1 and 90.8 EPDMS on NAVSIM v2, and reaches 37.4 HD-Score in zero-shot evaluation on HUGSIM. Extensive experiments and qualitative analyses demonstrate that visual encoder design provides an effective route to reliable and efficient end-to-end driving.

</details>

#### 2026-10-12 - Learning Reachability-Based Safety Representations for Real-Time Robot Navigation in Unknown and Dynamic Environments

**Authors:** Bojan Derajić
**Links:** [abs](https://arxiv.org/abs/2610.16522) - [pdf](https://arxiv.org/pdf/2610.16522)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Reachability-Based Safety Representations for Real-Time Robot Navigation in Unknown and Dynamic Environments
- 作者：Bojan Derajić
- 出版日期：2026-10-12T10:10:45Z
- 分类：Embodied / Robotics / AR Applications（无二级分类信息）
- 链接：[摘要](https://arxiv.org/abs/2610.16522) / [PDF](https://arxiv.org/pdf/2610.16522)

### 一句话总结
该博士论文提出离线训练神经网络隐式表示 Hamilton–Jacobi 可达性值函数（仅学习其中非负的动力学修正项），使基于优化的控制器能够实时获得安全可达性信息，从而在未知、动态环境中实现优于几何与手工基线避障效果。

### 研究问题
在未知、动态环境中的安全机器人导航，仅靠几何碰撞检测是不够的：即使机器人距离障碍物尚远，也可能因自身速度、朝向或障碍物运动而无法避免碰撞。HJ 可达性分析可用值函数的符号区分“存在安全延续”与“碰撞不可避免”的状态，但针对每个新观测环境在线计算该值函数代价过高，难以实时使用。

### 核心思路/方法
- 离线训练神经网络隐式表示，学习可达性解，从而让基于优化的控制器实时获取该信息。
- 关键观察：值函数不超过约束，因此它等于“直接计算的约束（如符号距离）减去一个非负的动力学修正项”。只学习这一修正项，可在存在近似误差的情况下仍保证所表示的障碍物位于预测安全集之外。
- 论文共提出五种方法：
  1. 前两种：将学习到的函数作为模型预测控制（MPC）的终端约束，分别用于静态局部环境和预测障碍物运动。
  2. 第三、四种：将其作为控制屏障函数（CBF）安全滤波器中的屏障候选，分别用于静态环境，以及通过相对坐标下的成对屏障应对数量可变的运动障碍物。
  3. 第五种：替代限制前四种方法于低维模型的基于网格的离线求解器。针对控制仿射动力学与多面体输入，HJ Hamiltonian 在顶点处取最大，因此可用可并行的顶点输入树搜索生成训练标签；结合 HJ 变分不等式损失，这些标签可为状态维数最高 13 的系统生成屏障候选。

### 主要贡献
- 提出只学习可达性值函数中动力学修正项的表示方式，在近似误差下仍保持安全集性质。
- 给出将学习到的安全表示接入 MPC 终端约束与 CBF 安全滤波器的五类方法，覆盖静态环境、预测障碍物运动与数量可变的运动障碍物。
- 在地面与空中机器人上进行了仿真与硬件实验，报告其避障效果优于几何和手工设计的基线，尤其在短预测时域和运动障碍物场景下。
- 第五种方法通过顶点输入树搜索与 HJ 变分不等式损失，摆脱基于网格的离线求解器对低维模型的限制，扩展到最高 13 个状态的系统。

### 局限性
摘要未提供足够信息（未说明具体失败情形、计算开销上限、实机实验规模、维数扩展的边界条件或与更多基线方法的对比细节）。

### 阅读优先级
中。理由：该工作针对实时安全导航这一实用问题，兼顾理论结构（可达性值函数的修正项表示）与多种控制器集成方式，并有仿真和硬件验证，对机器人安全控制方向有参考价值；但作为博士论文摘要，具体实验设置、定量结果与失败案例分析均未展开，需阅读全文才能判断方法在自身场景中的适用性。

</details>

<details>
<summary>Abstract</summary>

Safe robot navigation in unknown, dynamic environments requires more than geometric collision checking: a robot still far from an obstacle may be unable to avoid it because of its speed, orientation, or the obstacle's motion. Hamilton--Jacobi (HJ) reachability analysis captures this in a value function whose sign separates states that admit a safe continuation from those where collision is unavoidable, but computing it online for every newly observed environment is too expensive. This dissertation trains neural implicit representations offline on reachability solutions to give optimization-based controllers this information in real time. Since the value function never exceeds the constraint, it equals a directly computed constraint, such as a signed distance, minus a nonnegative dynamics correction. Learning only this correction keeps represented obstacles outside the predicted safe set despite approximation errors. The first two of five methods use the learned function as a terminal constraint in model predictive control, for static local environments and predicted obstacle motion. The next two use it as a barrier candidate in control barrier function safety filters, for static environments and, through pairwise barriers in relative coordinates, for a varying number of moving obstacles. Simulations and hardware experiments on ground and aerial robots show better collision avoidance than geometric and hand-designed baselines, especially for short horizons and moving obstacles. The fifth method replaces the grid-based offline solver, which limits the first four to low-dimensional models. For control-affine dynamics with polytopic inputs, the HJ Hamiltonian is maximized at a vertex, so a parallelizable tree search over vertex inputs can generate training labels. With a loss from the HJ variational inequality, these labels yield barrier candidates for systems with up to 13 states.

</details>

#### 2026-10-12 - Directional Pullback Regularization for Long-Horizon Rollout of Latent World Models in Autonomous Driving

**Authors:** Shatadal Mishra, Ahmadreza Moradipari, Nejib Ammar
**Links:** [abs](https://arxiv.org/abs/2610.16139) - [pdf](https://arxiv.org/pdf/2610.16139)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Directional Pullback Regularization for Long-Horizon Rollout of Latent World Models in Autonomous Driving
- 作者：Shatadal Mishra, Ahmadreza Moradipari, Nejib Ammar
- 出版日期：2026-10-12T03:59:30Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.16139 ；PDF https://arxiv.org/pdf/2610.16139

### 一句话总结
论文提出方向性拉回正则化（DPR），通过在解码状态空间定义运动学感知的各向异性黎曼度量并经由解码器雅可比拉回到潜在流形，在不改变编码器-动力学-解码器主干的前提下提升自动驾驶潜在世界模型的长期 rollout 质量。

### 研究问题
论文关注自动驾驶中学习到的世界模型长期潜在 rollout 建模问题。摘要指出，这类模型在无约束潜在空间中运行，但其代表的物理系统受严格非完整约束：地面车辆无法实现瞬时纯横向运动。作者提出的问题是：能否通过为潜在转移赋予运动感知几何，而不是重新设计预测器架构，来改善 rollout 质量。

### 核心思路/方法
论文从无约束潜在 rollout 基线出发，提出 Directional Pullback Regularization（DPR），一种训练时方法。其做法是在解码后的状态空间中定义运动学感知的各向异性黎曼度量，并通过解码器雅可比将其拉回到潜在流形。得到的潜在空间度量会对解码为车辆横向运动的潜在方向赋更高代价，同时保留原有的编码器-动力学-解码器主干。摘要提到由此形成三组对比：无约束潜在 rollout 模型（ULR）、欧几里得拉回正则化消融（EPR）以及完整方向性方法（DPR）。

### 主要贡献
摘要中明确给出的贡献包括：提出 DPR 这一训练时正则化方法，为潜在转移引入运动学感知的各向异性黎曼度量；在保留编码器-动力学-解码器主干的情况下，使潜在空间度量对横向运动方向赋更高代价；构建 ULR、EPR 与 DPR 的三方对比；在统一的 10 秒测试时域上进行开环自运动 rollout 评估，并使用 1、3、5、10 步的训练 rollout 长度。结果显示，在所有四种训练设置下，DPR 的 10 秒最终位移误差均低于 ULR 和 EPR；在 3 步 rollout 监督训练下相对 ULR 的最终位移误差降低约 44%；在更长 rollout 训练模型（尤其是 10 步）上，DPR 在位移误差、横向运动一致性和前向运动保持方面同时优于 ULR 和 EPR。

### 局限性
摘要未提供足够信息说明该方法的计算开销、对解码器雅可比质量的依赖程度、在不同数据集或驾驶场景下的泛化能力、闭环控制性能，以及除 10 秒开环自运动 rollout 和位移误差、横向运动一致性、前向运动保持之外的评价指标。摘要也未提供足够信息说明 EPR 与 DPR 之外的其他消融、基线模型细节或失败案例。

### 阅读优先级
高。理由：该论文直接针对自动驾驶潜在世界模型长期 rollout 中的运动学约束问题，提出不改变主干架构的训练时正则化方案，并在多种训练 rollout 长度下报告了明确的误差降低与运动一致性改善；对于关注潜在世界模型、长期预测和驾驶运动学约束的研究者具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Learned world models for autonomous driving operate in unconstrained latent spaces, yet the physical systems they represent are governed by strict non-holonomic constraints: ground vehicles cannot realize instantaneous pure lateral motion. We study long-horizon latent rollout modeling for autonomous driving and ask whether rollout quality can be improved by assigning a motion-aware geometry to latent transitions, rather than by redesigning the predictor architecture. Starting from an unconstrained latent rollout baseline, we introduce Directional Pullback Regularization (DPR), a training time method that defines a kinematics-aware anisotropic Riemannian metric in decoded state space and pulls it back through the decoder Jacobian to the latent manifold. The resulting latent-space metric assigns higher cost to latent directions that decode to lateral vehicle motion, while preserving the original encoder-dynamics-decoder backbone. This yields a clean three-way comparison among an Unconstrained Latent Rollout model (ULR), an Euclidean Pullback Regularization ablation (EPR), and the full directional method (DPR). We evaluate all models on open-loop ego-motion rollout over a common 10-second test horizon, using training rollout lengths of 1, 3, 5, and 10 steps. Across all four training regimes, DPR achieves lower 10-second final displacement error than both ULR and EPR. The strongest relative accuracy gain appears for models trained with 3-step rollout supervision, where DPR reduces the 10-second final displacement error by approximately 44 percent relative to ULR. The strongest overall control-relevant tradeoff is obtained for longer rollout-trained models, especially at 10 steps, where DPR simultaneously improves displacement error, lateral motion consistency, and forward motion preservation relative to both ULR and EPR.

</details>

#### 2026-10-12 - Adversarial Robustness of Camera-Radar Sensor Fusion for Autonomous Driving

**Authors:** Ce Zhou, Yubo Wu, Khang Nguyen, Liyang Xiao, Thomas Hou, Qiben Yan
**Links:** [abs](https://arxiv.org/abs/2610.16012) - [pdf](https://arxiv.org/pdf/2610.16012)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Adversarial Robustness of Camera-Radar Sensor Fusion for Autonomous Driving
- 作者：Ce Zhou, Yubo Wu, Khang Nguyen, Liyang Xiao, Thomas Hou, Qiben Yan
- 出版日期：2026-10-12T00:21:21Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.16012 ；https://arxiv.org/pdf/2610.16012

### 一句话总结
本文在 nuScenes 数据集上系统评测了相机-雷达传感器融合在对抗扰动下的鲁棒性，发现相机扰动会显著破坏 3D 目标检测与深度估计，而雷达扰动影响较小且依赖任务，表明传感器融合本身并不天然保证鲁棒性。

### 研究问题
自动驾驶依赖多传感器感知来理解周围环境，但相机-雷达融合在对抗条件下的鲁棒性仍 largely unexplored。论文关注的问题是：在相机图像与雷达点云分别受到扰动时，相机-雷达融合算法在 3D 目标检测和深度估计任务上的性能会如何变化，以及融合系统是否天然具备对抗鲁棒性。

### 核心思路/方法
论文构建了一个统一的评测流水线，在 nuScenes 数据集上模拟对两种感知模态的攻击：包括八种相机图像扰动和三种雷达点云扰动。随后评估五种相机-雷达融合算法，覆盖 3D 目标检测和深度估计两个感知任务，并使用标准指标量化其在干净输入与受攻击输入下的性能。基于评测结果，论文进一步分析融合系统鲁棒性差异的来源，并据此提出面向未来鲁棒相机-雷达融合的设计启示，包括模态特定可靠性估计、跨模态一致性检查、自适应融合以及严重传感器退化下的优雅降级。

### 主要贡献
- 在 nuScenes 数据集上构建统一评测流水线，同时模拟相机图像扰动与雷达点云扰动。
- 评估五种相机-雷达融合算法在两个感知任务（3D 目标检测、深度估计）上的干净与受攻击性能。
- 揭示融合系统鲁棒性的明显不对称性：相机扰动显著降低目标检测和深度估计性能，中等攻击强度即可造成严重退化；雷达扰动影响较小且依赖任务，目标检测模型退化尤其有限。
- 将差异归因于现有融合架构对密集相机特征的强依赖，以及针对稀疏雷达测量常用的过滤、关联和置信度加权机制。
- 基于四项实证发现，提出面向未来鲁棒相机-雷达融合的测量引导设计启示。

### 局限性
摘要未提供足够信息说明实验的具体数据集划分、攻击实现细节、各融合算法名称、标准指标的具体数值、统计显著性检验、雷达扰动为何影响较小的更细粒度消融实验，以及所提设计启示是否经过实际验证。此外，摘要未提供足够信息说明该方法在真实世界部署、其他数据集或更多传感器配置下的泛化能力。

### 阅读优先级
高。理由：该论文直接针对自动驾驶中相机-雷达融合的对抗鲁棒性这一关键且相对未被充分探索的问题，提供了跨五种融合算法和两个感知任务的系统评测，并给出具有实践指向的设计启示；对关注多传感器融合安全、自动驾驶感知鲁棒性和对抗攻击的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous driving (AD) relies on multi-sensor perception to interpret the surrounding environment. However, the robustness of camera--radar fusion under adversarial conditions remains largely unexplored. This paper presents a systematic measurement study of the robustness of camera--radar sensor fusion in AD. We construct a unified evaluation pipeline on the nuScenes dataset that simulates attacks on both sensing modalities, including eight camera-image perturbations and three radar point-cloud perturbations. We evaluate five camera--radar fusion algorithms across two perception tasks, 3D object detection and depth estimation, and quantify their performance under clean and attacked inputs using standard metrics. Our evaluation reveals a clear asymmetry in the robustness of fusion systems. Camera perturbations substantially degrade both object detection and depth estimation, and moderate attack strengths are already sufficient to cause severe performance degradation. In contrast, the evaluated radar perturbations produce smaller and task-dependent effects, with object-detection models showing particularly limited degradation. Our analysis attributes this difference to the strong dependence of existing fusion architectures on dense camera features, together with the filtering, association, and confidence-weighting mechanisms commonly applied to sparse radar measurements. These results demonstrate that sensor fusion does not inherently guarantee robustness and that the contribution and reliability of each sensing modality must be explicitly considered under adversarial conditions. Based on four empirical findings, we derive measurement-guided design implications for future robust camera--radar fusion, including modality-specific reliability estimation, cross-modal consistency checking, adaptive fusion, and graceful failover under severe sensor degradation.

</details>

#### 2026-10-08 - DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training

**Authors:** Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang
**Links:** [abs](https://arxiv.org/abs/2610.12468) - [pdf](https://arxiv.org/pdf/2610.12468)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training
- 作者：Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang
- 出版日期：2026-10-08T17:59:51Z
- 分类：Embodied / Robotics / AR Applications（无二级分类信息）
- 链接：[摘要](https://arxiv.org/abs/2610.12468) / [PDF](https://arxiv.org/pdf/2610.12468) / [项目页](https://brave-eai.github.io/DreamTrue)

### 一句话总结
DreamTrue 是一个多视角、跨本体（cross-embodiment）的机器人世界模型，通过将动作轨迹渲染为图像空间条件并结合反事实后训练，提升动作遵循能力与交互结果的物理合理性。

### 研究问题
在现有机器人数据集上训练机器人世界模型面临两个障碍：
1. 标定不精确会损害模型对动作的遵循（action following）；
2. 数据对不成功交互的覆盖有限，会使预测偏向成功结果。

论文的目标是构建一个能够在多视角、跨本体条件下进行动作忠实且物理合理的视频预测的世界模型。

### 核心思路/方法
- **动作条件构造与对齐**：为提升跨本体的动作遵循，将动作轨迹渲染为图像空间条件，并引入离线几何标定（offline geometric calibration）使这些条件与目标视频对齐。
- **反事实后训练（counterfactual post-training）**：修改已记录的动作轨迹，在更广范围的动作与接触配置下生成未来视频，以拓宽交互覆盖。
- **奖励模型与强化学习后训练**：由于这些预测没有配对的真实未来视频，作者构建了一个人类标注的视频数据集，覆盖机器人、物体和交互缺陷，并用于训练具身视频奖励模型（embodied video reward model）。其分数引导强化学习后训练，使交互结果更符合物理合理性。

### 主要贡献
- 提出 DreamTrue，一个多视角、跨本体的机器人世界模型，用于动作忠实且物理合理的视频预测。
- 通过图像空间动作条件渲染与离线几何标定，改善跨本体的动作遵循。
- 提出反事实后训练，扩展动作与接触配置的覆盖范围。
- 构建人类标注的缺陷视频数据集并训练具身视频奖励模型，用于在无配对真实未来的情况下提供反馈，并指导强化学习后训练。
- 在 AgiBot 上取得 state-of-the-art 的动作遵循表现，并将人工评估的交互缺陷率从 48.12% 降至 6.25%。
- 在 AgiBot World Challenge 2026 的世界模型赛道中排名第一。

### 局限性
摘要未提供足够信息。摘要未提及模型的具体失效场景、计算成本、对特定本体或数据集的依赖程度、奖励模型的泛化边界，也未说明反事实后训练可能引入的偏差或负面效果。

### 阅读优先级
**高**。理由：该工作针对机器人世界模型中的动作忠实性与物理合理性两个核心问题，提出了较完整的方法链路（动作条件对齐、反事实后训练、奖励模型引导强化学习），并在摘要中报告了明确的量化改进与竞赛排名，对具身智能、机器人视频预测和世界模型方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction. Training such a model on existing robot datasets faces two obstacles: imprecise calibration can impair action following, while limited coverage of unsuccessful interactions can bias predictions toward successful outcomes. To improve action following across embodiments, we render action trajectories into image-space conditions and introduce offline geometric calibration to align these conditions with the target videos. To broaden interaction coverage, we introduce counterfactual post-training, modifying recorded action trajectories and generating future videos under a wider range of actions and contact configurations. To provide feedback on these predictions without paired ground-truth futures, we construct a human-annotated video dataset covering robot, object, and interaction defects and use it to train an embodied video reward model. Its scores guide reinforcement-learning post-training toward more physically plausible interaction outcomes. On AgiBot, DreamTrue attains state-of-the-art action following, while reducing the human-assessed interaction defect rate from from 48.12% to 6.25%. Notably, our model ranks first in the world model track of the AgiBot World Challenge 2026. The project page can be found at https://brave-eai.github.io/DreamTrue.

</details>

#### 2026-10-08 - GLIO2: A GPU-Parallelized Tightly-Coupled LiDAR-Inertial-GNSS System for Robust and Real-Time Global Localization and Mapping

**Authors:** Qi Zhang, Xikun Liu, Qijun Qin, Xiangru Wang, Junzhe Wang, Naigui Xiao, Jianhao Jiao, Weisong Wen
**Links:** [abs](https://arxiv.org/abs/2610.12411) - [pdf](https://arxiv.org/pdf/2610.12411)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GLIO2: A GPU-Parallelized Tightly-Coupled LiDAR-Inertial-GNSS System for Robust and Real-Time Global Localization and Mapping
- 作者：Qi Zhang, Xikun Liu, Qijun Qin, Xiangru Wang, Junzhe Wang, Naigui Xiao, Jianhao Jiao, Weisong Wen
- 出版日期：2026-10-08T17:49:33Z
- 分类：Embodied / Robotics / AR Applications（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2610.12411) / [PDF](https://arxiv.org/pdf/2610.12411)

### 一句话总结
GLIO2 提出一种 GPU 并行化的紧耦合 LiDAR-惯性-GNSS 系统，将扫描-多扫描 LiDAR、IMU 预积分与原始 GNSS 测量在单一滑窗因子图中联合优化，以解决退化环境下的漂移与误差不可恢复问题，并在多个公开基准及自采数据上取得最优整体精度。

### 研究问题
论文关注大规模、感知退化环境中的全局一致、实时状态估计问题，这对自动驾驶车辆和空中机器人至关重要，需要融合 LiDAR、惯性和 GNSS 测量。

摘要指出，现有融合方法共享一种“扫描到地图”的前端，并存在两种失败模式：
1. 每次扫描都与增量构建的地图对齐，而该地图在退化条件下会漂移；一旦估计发散，误差便不可恢复。
2. 即使不发散，由动态物体或错误对应关系导致的配准偏差，会作为单一位姿约束以过度自信的协方差传播，其对应关系无法供 GNSS 重新加权或重新线性化。

### 核心思路/方法
GLIO2 的核心是一个 GPU 并行的前端，在单一滑窗因子图中联合优化三类测量：
- 扫描-多扫描 LiDAR
- IMU 预积分
- 原始 GNSS 测量

该前端可在边缘硬件上维持实时运行。此外，系统配有一个互补的离线后端，复用相同的缓存因子对整个轨迹进行批量精化，摘要称其可在约 24 秒内完成 30 分钟、4.51 公里的 UrbanNav Whampoa 序列。

### 主要贡献
- 提出 GLIO2，一个紧耦合的 LiDAR-惯性-GNSS 系统，其 GPU 并行前端在单一滑窗因子图中联合优化扫描-多扫描 LiDAR、IMU 预积分和原始 GNSS 测量，并可在边缘硬件上实时运行。
- 设计互补的离线后端，复用同一批缓存因子对整条轨迹进行批量精化，摘要报告在 UrbanNav Whampoa 序列上约 24 秒完成处理。
- 在三个公开基准（UrbanNav、MARS-LVIG、M3DGR）以及自采 UAV 与车辆数据上，摘要称 GLIO2 在所评估系统中取得最佳整体精度。
- 在一条 5.66 公里、最高时速 96 公里的桥梁场景中，摘要称所有对比基线在 LiDAR 退化下均发散，而 GLIO2 保持 1.6 米水平精度。
- 在 NVIDIA Jetson Orin NX 上，摘要称完整流水线以约 25 Hz（每扫描 39.60 毫秒）运行。
- 摘要声明源代码与数据集将会发布。

### 局限性
- 摘要未提供足够信息说明该方法在其他类型退化场景（如非 LiDAR 退化主导的场景）中的表现。
- 摘要未提供足够信息说明离线后端与在线前端之间精度差异的定量对比。
- 摘要未提供足够信息说明 GPU 并行前端在非 NVIDIA 边缘硬件或不同算力平台上的可移植性与性能。
- 摘要未提供足够信息说明该方法对 GNSS 信号长时间缺失或严重多路径场景的鲁棒性边界。
- 摘要未提供足够信息说明因子图规模增长对内存占用的影响。
- 摘要未提供足够信息说明与基线方法在计算资源消耗上的完整对比。

### 阅读优先级
高。理由：该论文针对 LiDAR-惯性-GNSS 融合中“退化导致漂移且误差不可恢复”与“配准偏差以过度自信协方差传播”这两个明确失败模式提出系统级解决方案，涉及 GPU 并行前端、滑窗因子图联合优化与离线批量精化，并在多个公开基准和自采数据上报告了精度与实时性结果，还声明将开源代码与数据集；对从事多传感器融合、机器人定位建图与边缘实时部署的研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Globally consistent, real-time state estimation in large-scale, perceptually degraded environments is essential for autonomous vehicles and aerial robots, and requires fusing LiDAR, inertial, and GNSS measurements. Existing fusion methods, however, share a scan-to-map front-end with two failure modes. First, each scan is aligned to an incrementally built map that drifts under degeneracy, and once the estimate diverges the error is irrecoverable. Second, even without divergence, a registration biased by dynamic objects or wrong correspondences is propagated as a single pose constraint with an over-confident covariance, leaving its correspondences unavailable for GNSS to re-weight or relinearize. We propose GLIO2, a tightly-coupled LiDAR-Inertial-GNSS system whose GPU-parallel front-end jointly optimizes scan-to-multiscan LiDAR, IMU pre-integration, and raw GNSS measurements in a single sliding-window factor graph, sustaining real-time operation on edge hardware. A complementary offline back-end reuses the same cached factors to refine the entire trajectory in batch, completing the 30-min, 4.51-km UrbanNav Whampoa sequence in about 24 s. Across three public benchmarks (UrbanNav, MARS-LVIG, M3DGR) and self-collected UAV and vehicle data, GLIO2 attains the best overall accuracy among evaluated systems. On a 5.66-km bridge traversed at up to 96 km/h, where every competing baseline diverges under LiDAR degeneracy, it maintains 1.6 m horizontal accuracy. On an NVIDIA Jetson Orin NX, the full pipeline runs at about 25 Hz (39.60 ms per scan). The source code and datasets will be released.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
