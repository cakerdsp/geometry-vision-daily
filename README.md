# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：53
- 分类分布：
  - Embodied / Robotics / AR Applications: 19
  - Neural Scene Representations & Rendering: 17
  - 3D Reconstruction & Multi-view Geometry: 8
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **几何基础模型从“特征提取器”升级为“可复用的重建/配准骨干”**
   本批论文中，VGGT 及其同类视觉几何基础模型被反复用作可插拔骨干，而非仅做特征表示。PointVGGT 提出“先基础、后精化”范式，用 VGGT 直接恢复度量一致的全局位姿；CoCam4D 用 VGGT 前馈网络生成带不确定性估计的 3D 高斯场景表示，用于多车协同感知。这一趋势表明，几何基础模型正在成为下游 3D/4D 任务的计算底座，而非单独的预训练产物。

2. **“无位姿 / 无提升 / 免训练”成为 3D 重建与编辑的显式设计目标**
   多篇论文主动脱离传统标定与显式重建流程：FreeInpaint 强调无需相机位姿，直接从带掩码的无位姿多视角图像做 3D 补全；LEGO 提出免“提升到点云”的跨视角视频生成条件；Slot3R 以免训练、集合关联式的改造冻结 Point3R 主干；FlyMark 以免训练隐形水印写入已发布参数。共同逻辑是：把预处理、标定与训练依赖从部署链路中剥离，换取在野场景的可用性与可移植性。

3. **世界模型开始分化出“预测什么”和“如何用预测”两条并行问题线**
   PLaW-VLA 与 DreamTrue 都属世界模型方向，但关注点不同。PLaW-VLA 追问应在何种表征空间建模未来状态（预测导向表征而非像素重建），并强调用结构化因果注意力把预测未来条件化到动作生成；DreamTrue 追问如何让动作条件在多视角、跨本体下真正被遵循（动作轨迹渲染为图像空间条件 + 离线几何标定 + 反事实后训练）。世界模型正从“能否预测未来”转为“预测的未来表示是否对控制有用”。

4. **4D/动态场景表示在“循环性、外观适配、实时性”等工程约束上持续细化**
   OuroWorld 用傅里叶级数变形场从构造上保证无缝循环，并用 Grounded Drift Field 吸收跨视角不一致；PAM-ToD 以即插即用方式在冻结 3DGS 参数下学习跨时段颜色修正；LVS 用相对位姿引导的 RGB-D 图像重用加残差修正减少邻近视角重复渲染。这些工作共同指向：动态/神经场景表示正从“能生成”走向“在特定渲染与交互约束下可控”。

5. **机器人系统层出现“感知间歇性”与“同构体识别”两类真实部署瓶颈**
   ALONE 研究共享传感器被其他任务占用时的间歇感知导航，提出仅在可靠性不足时才请求新观测；同批另一篇多机器人相对定位工作用 LiDAR+UWB+里程计解决同构机器人外观相似导致的匿名簇关联问题。这说明具身智能研究正在从“传感器齐全、标识清晰”的理想设定，转向资源受限、身份模糊的真实约束。

#### 技术路线观察

- **几何基础模型方向**：FreeMatching、PointVGGT、CoCam4D 代表三种用法——FreeMatching 结合生成式与语义基础表示做稠密对应，目标是突破平滑运动与刚性几何先验；PointVGGT 把基础模型当零样本配准骨干，用度量深度接地尺度；CoCam4D 则把基础模型输出转为带不确定性的高斯表示用于协同。共同点是基础模型不再只输出特征，而是输出可被下游几何/概率操作消费的结构化表示。

- **3D/4D 重建方向**：Slot3R 与 FreeInpaint 都在“部分观测”下做重建，但切入点不同。Slot3R 针对流式重建中的记忆融合策略，主张位置决定地址而非是否合并，避免过早平均掉互补证据；FreeInpaint 针对无位姿带掩码输入，强调掩码会破坏跨视图对应推理进而退化位姿估计。两者都指向同一技术判断：重建管线中“不确定性与未观测区域的显式建模”比单纯提升渲染保真度更关键。

- **神经场景表示与渲染方向**：本批论文覆盖多种表示形态——3DGS（PAM-ToD、FlyMark、2DGS-Planner、LVS）、4DGS（OuroWorld）、神经辐射缓存（Neural Caching of Prefiltered Radiance）。技术侧重从“表示能力”转向“表示的可操作性”：水印写入参数、路径规划从栅格化读取几何、局部视图用 RGB-D 重用替代重复渲染。即表示本身不新，但对表示的读取、写入与复用方式成为创新点。

- **机器人/AR 应用方向**：DreamTrue、PLaW-VLA、ALONE、LIVIN、USDCraft、DVD、2DGS-Planner、多机器人相对定位构成较大集群。可细分为：世界模型与策略（DreamTrue、PLaW-VLA）、导航与定位（ALONE、多机器人相对定位、2DGS-Planner）、仿真资产与基准（USDCraft、LIVIN）、感知接口效率（DVD）。整体上，应用侧论文更关注“部署约束”（标定误差、通信带宽、传感器共享、外观相似）而非单纯算法精度。

#### 值得优先阅读的论文

1. **PLaW-VLA**：直接回答“世界模型预测什么表征才对策略有用”这一核心问题，并在 RoboTwin 与 LIBERO-Plus 上给出量化对比（+11.8pp / +1.77pp）。对关心 VLA 与世界模型交叉的研究者，这是本批中最具方法论指向性的一篇。

2. **DreamTrue**：与 PLaW-VLA 互补，聚焦“动作忠实性”与“反事实后训练”。其问题设定（标定不精确、失败交互覆盖不足）是机器人世界模型训练的真实痛点，值得优先读以理解动作条件构造与对齐的工程细节。

3. **PointVGGT**：代表几何基础模型作为零样本配准骨干的新范式，且明确用度量深度接地解决基础模型的尺度模糊。对做多视图配准、RGB-D 对齐或基础模型复用的人，是路线级参考。

4. **Slot3R**：问题洞察锐利——“共址不等于状态同一”，且以免训练改造冻结主干实现，方法成本低、可迁移性强。对做流式重建或空间记忆设计的研究者优先级高。

5. **OuroWorld**：把任意静态 3DGS 变为无缝循环 3D cinemagraph，涉及 VLM 推断动态、多视角补全与不一致性鲁棒 4DGS。对动态场景表示与生成式 3D 交叉方向，是较完整的系统级案例。

#### 可能的研究机会

- **几何基础模型 + 不确定性传播的组合**：CoCam4D 已展示带不确定性高斯表示的协同感知，但 PointVGGT 的位姿恢复尚未显式输出不确定性。可将基础模型的位姿/深度预测与概率表示结合，用于多机器人或车路协同中的鲁棒融合。

- **世界模型表征选择与策略学习的联合设计**：PLaW-VLA 选了预测导向表征，DreamTrue 选了图像空间动作条件。两者尚未交叉。可探索“在预测导向潜空间中做反事实动作条件”的组合，既降低预测负担又提升动作忠实性。

- **间歇感知与主动观测的规划耦合**：ALONE 的可靠性触发观测机制可与 2DGS-Planner 的间隙场缓存结合，形成“何时看、看哪里、如何用缓存几何规划”的统一框架。

- **无位姿/无标定设定下的 3D 编辑闭环**：FreeInpaint 解决无位姿补全，LEGO 解决无提升跨视角生成，但两者未处理编辑后场景的持续一致性。可研究在无位姿条件下做多次编辑并保持 3D 一致的机制。

- **程序化资产生成与基准的对接**：USDCraft 生成仿真就绪铰接资产，LIVIN 提供真实住宅数字孪生基准。可将 USDCraft 的 LLM 程序

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-14T13:07:21-04:00
**Total number of papers:** 72
**Number of papers added in the latest update:** 37
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

#### 2026-10-08 - PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors

**Authors:** Haobo Jiang, Liang Yu, Jianmin Zheng
**Links:** [abs](https://arxiv.org/abs/2610.11612) - [pdf](https://arxiv.org/pdf/2610.11612)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, metric depth, 3D reconstruction, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors
- 作者：Haobo Jiang, Liang Yu, Jianmin Zheng
- 出版日期：2026-10-08T09:54:56Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.11612) / [PDF](https://arxiv.org/pdf/2610.11612)

### 一句话总结
提出 PointVGGT，一种基于“先基础、后精化”（foundation-then-refinement）范式的零样本多视图 RGB-D 点云配准框架，利用视觉几何基础模型（如 VGGT）作为计算骨干，无需成对估计即可恢复全局一致位姿并进行精化。

### 研究问题
论文针对无序 RGB-D 扫描的多视图点云配准，目标是估计全局刚性位姿并在度量一致的坐标系中对齐。摘要指出，传统“先成对、后全局”的范式存在三个问题：成对配准易陷入局部最优、误差严重传播、计算负担高。此外，现有方法通常仅将 RGB 数据视为辅助匹配线索，而忽视了图像序列中编码的整体几何先验（如相机位姿和 3D 模型）。

### 核心思路/方法
PointVGGT 采用零样本框架，基于“foundation-then-refinement”范式，系统性地利用视觉几何基础模型（如 VGGT）作为计算骨干，实现鲁棒、免训练的多视图 RGB-D 配准。

- 基础阶段（foundation stage）：直接恢复度量一致的全局位姿，无需任何成对估计；通过将基础模型输出的尺度模糊位姿预测与度量深度观测进行“接地”（grounding），解决尺度歧义。
- 精化阶段（refinement stage）：引入高效体素化空间哈希机制，利用基础模型诱导的全局一致 3D 重建作为共享空间锚点，在近线性时间内实现密集多视图对应。在此基础上，使用基于 IRLS 的鲁棒 motion-only bundle adjustment，配合共轭梯度求解器，联合最小化对应残差和重投影残差以精化多视图位姿。

### 主要贡献
- 提出 PointVGGT，一个零样本多视图 RGB-D 点云配准框架，采用“foundation-then-refinement”新范式。
- 在基础阶段，无需成对估计，直接通过度量深度观测对基础模型的尺度模糊位姿预测进行接地，恢复全局度量一致位姿。
- 在精化阶段，提出体素化空间哈希机制，利用全局一致的 3D 重建作为共享空间锚点，实现近线性时间的密集多视图对应。
- 引入基于 IRLS 的鲁棒 motion-only bundle adjustment，使用共轭梯度求解器联合优化对应与重投影残差。
- 摘要声称在室内、物体中心、室外数据集上的大量实验验证了所提方法出色的零样本配准精度和计算效率。

### 局限性
- 摘要未提供足够信息说明具体实验细节、数据集名称、评价指标、与哪些方法对比、消融实验等。
- 摘要未提供足够信息说明方法对基础模型（如 VGGT）的依赖程度、失败案例、对深度观测质量的敏感性等潜在局限。
- 摘要未提供足够信息说明“近线性时间”的具体复杂度分析或实际运行时间数据。
- 摘要未提供足够信息说明零样本设定下是否完全无需任何训练或微调，以及是否对特定场景类型有假设限制。

### 阅读优先级
高。理由：该论文聚焦多视图 RGB-D 点云配准这一重要问题，提出利用视觉几何基础模型先验的零样本新范式，并声称在精度和效率上均有突出表现；分类属于 Geometry Foundation Models 与 3D Reconstruction & Multi-view Geometry 交叉方向，对关注基础模型在 3D 几何任务中应用的研究者具有较高参考价值。但具体实验细节需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

This paper addresses multiview RGB-D point cloud registration, aiming to estimate global rigid poses for unordered RGB-D scans and align them in a metrically consistent coordinate frame. The conventional pairwise-then-global paradigm suffers from locally optimized pairwise registration, severe error propagation and high computational burden. In particular, existing methods typically treat RGB data as a mere auxiliary matching cue and overlook the holistic geometric priors (e.g., camera poses and 3D models) encoded across image sequences. This paper introduces PointVGGT, a zero-shot framework built upon a novel \emph{foundation-then-refinement} paradigm that systematically leverages visual geometry foundation models (e.g., VGGT) as the computational backbone for robust, training-free multiview RGB-D registration. In the foundation stage, we directly recover metrically consistent global poses (without any pairwise estimation) by grounding the scale-ambiguous pose predictions of the foundation model against metric depth observations. In the refinement stage, we introduce an efficient voxelized spatial hashing mechanism that exploits the globally coherent 3D reconstruction (induced by the foundation model) as a shared spatial anchor, enabling dense multiview correspondences in near-linear time. On top of this, an IRLS-based robust motion-only bundle adjustment is performed using a conjugate gradient solver to jointly minimize the correspondence and reprojection residuals for multiview pose refinement. Extensive experiments on indoor/object-centric/outdoor datasets verify the outstanding zero-shot registration accuracy and computational efficiency of our proposed method.

</details>

#### 2026-10-08 - CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving

**Authors:** Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya
**Links:** [abs](https://arxiv.org/abs/2610.11577) - [pdf](https://arxiv.org/pdf/2610.11577)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, depth estimation, monocular depth, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving
- 作者：Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya
- 出版日期：2026-10-08T09:31:28Z
- 分类：primary: Geometry Foundation Models；secondary: 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.11577 ；PDF https://arxiv.org/pdf/2610.11577

### 一句话总结
CoCam4D 是一个面向纯相机自动驾驶的贝叶斯协同感知框架，通过共享带不确定性估计的 3D 高斯场景表示来降低单目深度估计的不确定性，并采用紧凑表示支持车联网通信。

### 研究问题
自动驾驶车辆常因遮挡、盲区、有限传感器范围和复杂环境而感知受限。多智能体协同感知可通过共享感官信息协同重建场景来应对这些挑战，但纯相机感知仍受距离相关的单目深度估计不确定性限制。

### 核心思路/方法
- 提出 CoCam4D，一个显式建模几何不确定性的贝叶斯协同感知框架。
- 使用基于 VGGT 的前馈网络生成带不确定性估计的 3D 高斯场景表示，使多个车辆或智能体能够高效融合观测。
- 通过共享紧凑的高斯图元，一个智能体的可靠观测可降低另一智能体的深度不确定性，且无需 LiDAR 传感器。
- 为支持实际部署，引入 Dynamic Object Primitives (DOPs)，一种为高效 C-V2X 通信设计的 35 字节紧凑表示。

### 主要贡献
- 提出显式建模几何不确定性的贝叶斯协同感知框架 CoCam4D。
- 采用 VGGT 前馈网络生成带不确定性估计的 3D 高斯场景表示，支持多智能体高效融合观测。
- 通过共享高斯图元实现无需 LiDAR 的跨智能体深度不确定性降低。
- 提出 35 字节的 DOPs 紧凑表示以支持高效 C-V2X 通信。
- 实验表明该方法持续优于近期纯视觉方法，在 OPV2V+ 上提升 11.48%，在 DAIR-V2X-C 上提升 10.62%。

### 局限性
- 具体的网络结构细节、不确定性建模方式、训练策略与消融实验：摘要未提供足够信息。
- DOPs 的具体构造方式、编码解码流程与通信开销分析：摘要未提供足够信息。
- 实验设置、基线方法细节、评估指标与数据集划分：摘要未提供足够信息。
- 实际部署验证、实时性、通信延迟与失效场景分析：摘要未提供足够信息。

### 阅读优先级
高。理由：该论文聚焦纯相机协同感知中的关键瓶颈——单目深度不确定性，并提出贝叶斯几何建模与紧凑通信表示，且摘要报告了在 OPV2V+ 和 DAIR-V2X-C 上的明确提升，与纯视觉自动驾驶、多智能体协同感知和 3D 高斯表示等方向高度相关。

</details>

<details>
<summary>Abstract</summary>

Autonomous vehicles often suffer from limited perception due to occlusions, blind spots, limited sensor range, and the complex nature of surrounding environments. Multi-agent collaborative perception (CP) addresses these challenges by allowing vehicles to share sensory information and reconstruct the scene cooperatively. However, camera-only perception remains fundamentally limited by the uncertainty of distance-dependent monocular depth estimation. We propose CoCam4D, a Bayesian framework for collaborative perception that explicitly models geometric uncertainty. It uses a VGGT-based feedforward network to generate 3D Gaussian scene representations with associated uncertainty estimates, enabling multiple vehicles or agents to efficiently combine their observations. By sharing compact Gaussian primitives, reliable observations from one agent can reduce the depth uncertainty of another without requiring LiDAR sensors. To support real-world deployment, we introduce Dynamic Object Primitives (DOPs), a compact 35-byte representation designed for efficient C-V2X communication. Extensive experiments show that our proposed method consistently outperforms recent vision-only methods, achieving improvements of 11.48% on OPV2V+ and 10.62% on DAIR-V2X-C, demonstrating the potential of geometrically grounded collaborative perception for LiDAR-free autonomous driving.

</details>

#### 2026-10-08 - VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving

**Authors:** Zhaoyang Liu, Kun Jiang, Ziying Song, Diange Yang
**Links:** [abs](https://arxiv.org/abs/2610.11161) - [pdf](https://arxiv.org/pdf/2610.11161)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving
- 作者：Zhaoyang Liu, Kun Jiang, Ziying Song, Diange Yang
- 出版日期：2026-10-08T03:20:48Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.11161；PDF https://arxiv.org/pdf/2610.11161

### 一句话总结
论文提出 VGGTWorld-VLA，通过在 VGGT-World 基础上引入意图与动作条件，使自动驾驶中的未来 3D 几何演化预测能够随自车动作变化而生成不同的未来结果。

### 研究问题
摘要指出，VGGT 能够从视觉观测中恢复统一 3D 场景几何，为以几何为中心的世界模型提供基础；近期扩展已实现时间维度上的 3D 预测，但其未来演化对驾驶意图和动作的条件约束较弱，限制了建模“同一观测场景在不同自车动作下产生多种可能未来”的能力。论文关注的问题即为：如何让基于 VGGT 的 3D 世界演化预测受到驾驶意图与动作的可控条件约束。

### 核心思路/方法
论文提出 VGGTWorld-VLA，作为 VGGT-World 的意图条件化扩展，用于自动驾驶中可控的 3D 世界演化。方法包含两个主要部分：
1. 动作—语义条件机制：将互补的驾驶语义和自车运动表示注入未来 token 流，使得在相同观测场景下，面对不同自车动作时能够预测不同的未来几何。
2. 几何—语言—动作桥接：将历史几何、VLA 语义特征以及机动与轨迹表示进行适配，用于联合条件化未来几何预测。

### 主要贡献
- 提出 VGGTWorld-VLA，将 VGGT-World 扩展为意图条件化的可控 3D 世界演化模型，面向自动驾驶场景。
- 引入动作—语义条件机制，使未来几何预测能够随不同自车动作而变化。
- 构建几何—语言—动作桥接，联合利用历史几何、VLA 语义特征、机动与轨迹表示来条件化未来几何预测。
- 在 NAVSIM 上评估未来几何预测，并通过条件消融考察语义和动作信息的贡献；摘要称相比基线方法展现出有竞争力的几何预测性能，消融研究支持语义与动作条件化的有效性。

### 局限性
摘要未提供足够信息说明方法的失败案例、计算开销、对特定数据集或传感器配置的依赖、安全性验证细节，以及消融实验的具体设置和数值结果。摘要也未提供足够信息说明其在真实驾驶场景中的泛化能力与部署限制。

### 阅读优先级
中。理由：该论文处于几何基础模型与自动驾驶世界模型的交叉方向，问题设定明确，即让未来 3D 几何预测受驾驶意图和动作条件控制，具有一定研究价值；但摘要仅给出方法框架和总体结论，未披露具体实验数值、消融细节与局限分析。若关注 VGGT 扩展、动作条件化世界模型或自动驾驶中的可控未来预测，可优先阅读；若需要完整实验证据或工程落地评估，则需进一步查看全文。

</details>

<details>
<summary>Abstract</summary>

VGGT provides a strong foundation for geometry-centric world models by recovering unified 3D scene geometry from visual observations. Although recent extensions enable temporal 3D prediction, their future evolution remains weakly conditioned on driving intentions and actions, limiting their ability to model alternative action-dependent futures. We propose VGGTWorld-VLA, an intention-conditioned extension of VGGT-World for controllable 3D world evolution in autonomous driving. First, we introduce an action--semantic conditioning mechanism that injects complementary driving semantics and ego-motion representations into the future-token stream, enabling different future geometry predictions for the same observed scene under alternative ego actions. Second, we develop a geometry--language--action bridge that adapts historical geometry, VLA semantic features, and maneuver and trajectory representations for joint conditioning of future geometry prediction. We evaluate future geometry prediction on NAVSIM, while conditioning ablations further examine the contributions of semantic and action information. Compared with the baseline, our method demonstrates competitive geometry prediction performance. Ablation studies further support the effectiveness of semantic and action conditioning. These results demonstrate the potential of semantic and action conditioning for controllable VGGT-based world prediction in autonomous driving.

</details>

#### 2026-10-07 - LVSPM: Long Sequence View Synthesis and Pose Estimation Model

**Authors:** Xi Chen, Yachi Zhang, Linghao Chen, Minghua Liu, Hao Su, Zexiang Xu, Xiaoshuai Zhang
**Links:** [abs](https://arxiv.org/abs/2610.10960) - [pdf](https://arxiv.org/pdf/2610.10960)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** VGGT, pose estimation, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LVSPM: Long Sequence View Synthesis and Pose Estimation Model
- 作者：Xi Chen, Yachi Zhang, Linghao Chen, Minghua Liu, Hao Su, Zexiang Xu, Xiaoshuai Zhang
- 出版日期：2026-10-07T22:26:35Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.10960 ；PDF https://arxiv.org/pdf/2610.10960

### 一句话总结
LVSPM 是一个从无标定图像集合中联合估计相机位姿并合成新视角的可泛化模型，借助仅在 RGB 图像与位姿监督下训练以及测试时训练（TTT）层，可扩展到数百个输入视角，并在多个数据集上取得领先的位姿估计与无位姿新视角合成效果。

### 研究问题
论文关注的问题是在无标定（uncalibrated）图像集合上，同时完成相机位姿估计与新视角合成，并且需要具备可泛化性与对长序列（数百个输入视角）的可扩展性。摘要指出，其目标还在于避免依赖稠密 3D 真值，仅使用 RGB 图像与位姿监督进行训练，并解决随场景规模增长时基线方法崩溃的问题。

### 核心思路/方法
- 提出 LVSPM 模型，联合进行相机位姿估计和新视角合成，输入为无标定图像集合。
- 训练仅使用 RGB 图像与位姿监督，避免稠密 3D 真值。
- 采用测试时训练（TTT）层，使模型能够无缝扩展到数百个输入视角。
- 在 RealEstate10k、Co3Dv2 和 DL3DV 上进行评估；位姿估计方面在 16–256 视角设置下超过 VGGT，在严格阈值下优势尤其明显。
- 新视角合成方面，在一个“更多视角覆盖更大场景”的实际协议下，实现无位姿条件下的最优质量，PSNR 甚至超过依赖位姿的模型，并且随场景尺度增大仍保持高质量，而基线方法崩溃。

### 主要贡献
- 提出 LVSPM，一个可泛化的联合位姿估计与新视角合成模型，仅需 RGB 图像和位姿监督，无需稠密 3D 真值。
- 通过测试时训练层实现对数百个输入视角的可扩展性。
- 在 RealEstate10k、Co3Dv2、DL3DV 上，于 16–256 视角范围内位姿估计超过 VGGT，且在严格阈值下提升幅度尤其大。
- 在实际协议下实现无位姿新视角合成的当前最优质量，PSNR 超过依赖位姿的模型，并在场景尺度增大时保持高质量，而基线方法崩溃。
- 代码已公开，链接为 https://burningdust21.github.io/Projects/LVSPM 。

### 局限性
- 摘要未提供足够信息说明计算开销、推理速度或训练成本方面的限制。
- 摘要未提供足够信息说明在极端视角数量、动态场景或非静态场景下的表现。
- 摘要未提供足够信息说明对训练数据分布之外场景的泛化边界。
- 摘要未提供足够信息说明失败案例或与基线相比的具体定量差距细节。

### 阅读优先级
高。理由：该论文同时涉及位姿估计与新视角合成两个核心任务，强调无需稠密 3D 真值、可扩展到数百视角，并在多个数据集上报告了超过 VGGT 及依赖位姿模型的合成质量；对多视图几何、3D 重建与神经渲染方向具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

We present LVSPM, a generalizable model that jointly estimates camera poses and synthesizes novel views from uncalibrated image collections. Trained with only RGB images and pose supervision, LVSPM avoids dense 3D ground truth and employs test-time training (TTT) layers to scale seamlessly to hundreds of input views. On RealEstate10k, Co3Dv2, and DL3DV, LVSPM surpasses VGGT in pose estimation across 16-256 views, with especially large margins at strict thresholds. For novel view synthesis under a practical protocol where more views cover larger scenes, LVSPM achieves state-of-the-art pose-free quality---surpassing even pose-dependent models in PSNR---and still maintains high quality as scene scale grows, while baselines collapse. The code is available at https://burningdust21.github.io/Projects/LVSPM .

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-13 - PUGS: Physics-Guided Uncertainty Modeling for Underwater Dynamic 3D Gaussian Splatting

**Authors:** Tingjun Li, Yuxi Wang, Guoqiang Zhong, Zhaoxiang Zhang
**Links:** [abs](https://arxiv.org/abs/2610.17936) - [pdf](https://arxiv.org/pdf/2610.17936)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

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
<summary>Abstract</summary>

To reconstruct a predictive 4D representation of the physical world from monocular video captured by a moving camera, we jointly reconstruct dynamic Gaussian radiance fields and infer their underlying physical dynamics. This paper proposes \emph{Physical SLAM}, a physics-aware method for constructing 4D Gaussian fields of deformable objects and predicting their future state when subjected to external actions, given a sequence of RGB-D images. Our method separates the scene into a static background Gaussian field for camera localization and a dynamic object Gaussian field driven by a spring--mass physical model of elastic deformation, inertia, and damping. To integrate visual observations with physical dynamics, we introduce virtual observation forces that gradually pull simulated surface nodes toward observed depth points, avoiding abrupt replacement of simulated node positions. Meanwhile, the physical parameters of the spring--mass model are updated from simulation errors aggregated over the full reconstruction observation window, enabling the reconstructed dynamics to align with observations. To couple appearance, geometry, and physics, we further design a physics-aware Gaussian transformation and surface alignment strategy, where dynamic Gaussians are transformed along the deforming physical surface of the spring--mass model and constrained to remain aligned with the surface during rendering-based optimization. The resulting representation supports observed-frame rendering and action-conditioned simulation, extending SLAM maps to describe how deformable objects respond to manipulation. On the PhysTwin benchmark, our method improves reconstruction and prediction PSNR over PhysTwin by 10.4\% and 11.0\%, respectively. On the TUM RGB-D benchmark, it reduces average camera tracking error by 20.6\%, improves SSIM by 3.6\%, and reduces LPIPS by 8.3\% compared with 4DGS-SLAM.

</details>

#### 2026-10-08 - MATE4D: Matrix-Guided Editable 4D Generation from a Single Image

**Authors:** Xiaotian Chen, Dongfu Yin
**Links:** [abs](https://arxiv.org/abs/2610.11181) - [pdf](https://arxiv.org/pdf/2610.11181)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** dynamic 3D, dynamic 4D, manipulation, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MATE4D: Matrix-Guided Editable 4D Generation from a Single Image
- 作者：Xiaotian Chen, Dongfu Yin
- 出版日期：2026-10-08T03:40:14Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.11181) / [PDF](https://arxiv.org/pdf/2610.11181)

### 一句话总结
MATE4D 通过构建带文本引导背景编辑的时空多视图图像矩阵，为单图生成可编辑动态 4D 内容提供一致的视角、外观与运动监督，并据此优化可动画化的 3D 高斯表示。

### 研究问题
从单张图像生成真实且时序稳定的 4D 内容仍然困难：单一视角提供的结构线索有限，运动证据薄弱。论文旨在解决单图输入条件下 4D 内容的结构保真、时序平滑、背景编辑一致性以及上下文歧义与运动伪影等问题。

### 核心思路/方法
- 将单张输入图像转化为可编辑的动态 4D 内容。
- 构建时空多视图图像矩阵，并引入文本引导的背景操作，从而在视角、外观和运动上提供连贯监督。
- 利用这些合成观测优化 3D 高斯图元（3D Gaussian primitives）。
- 通过轻量级形变模块对高斯表示进行动画化，形成 4D 表示。
- 摘要称该方法使生成场景更忠实保留几何、时序行为更平滑、背景编辑更一致，并减少上下文歧义与运动伪影。

### 主要贡献
- 提出 MATE4D 框架，实现从单图到可编辑动态 4D 内容的生成。
- 设计时空多视图图像矩阵与文本引导背景操作，为视角、外观和运动提供连贯监督。
- 将合成观测用于优化 3D 高斯图元，并通过轻量级形变模块实现 4D 动画化。
- 在 Objaverse-XL 和 Diffusion4D 上的实验表明，MATE4D 在视觉质量、效率和可控性方面优于强基线，并支持实际 AR/VR 内容创作。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败模式、适用输入限制、计算资源需求、评估指标细节、用户研究结果或对极端运动/复杂遮挡场景的表现。

### 阅读优先级
中。理由：该工作聚焦单图 4D 生成、可编辑性与 3D 高斯表示，与动态 4D 重建和 AR/VR 应用相关；摘要给出了清晰的动机、方法框架和实验数据集，但未展开关键实现与定量结果。若关注单图到 4D、可编辑内容生成或高斯表示动画化，值得进一步阅读全文；若仅需概览，则摘要信息已覆盖主要脉络。

</details>

<details>
<summary>Abstract</summary>

Generative models have rapidly pushed content creation be-yond 2D imagery toward dynamic 3D and 4D scene synthesis. Yet pro-ducing realistic and temporally stable 4D content from a single image is still difficult because one view provides limited structural cues and weak motion evidence. We introduce MATE4D, a framework that converts one input image into editable dynamic 4D content. Our method constructs a spatio-temporal multi-view image matrix with text-guided background manipulation, delivering coherent supervision over viewpoint, appear-ance, and motion. These synthesized observations are used to optimize 3D Gaussian primitives, which are then animated through a lightweight deformation module to form a 4D representation. The resulting scenes preserve geometry more faithfully, maintain smoother temporal behavior, and keep background edits more consistent, reducing context ambiguity and motion artifacts. Experiments on Objaverse-XL and Diffusion4D show that MATE4D outperforms strong baselines in visual quality, effi-ciency, and controllability, supporting practical AR/VR content creation.

</details>

#### 2026-10-07 - MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting

**Authors:** Jiuming Liu, Jianing Li, Mengmeng Liu, Hongyang He, Hesheng Wang, Per Ola Kristensson
**Links:** [abs](https://arxiv.org/abs/2610.10759) - [pdf](https://arxiv.org/pdf/2610.10759)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** scene flow

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting
- 作者：Jiuming Liu, Jianing Li, Mengmeng Liu, Hongyang He, Hesheng Wang, Per Ola Kristensson
- 出版日期：2026-10-07T18:23:30Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2610.10759) / [PDF](https://arxiv.org/pdf/2610.10759)

### 一句话总结
MESSENGER 通过记忆缓冲存储历史场景流与隐状态，并以自回归“预测下一帧”的方式初始化当前帧场景流，同时用不确定性感知重加权模块抑制不可靠检索与累积误差，在 nuScenes 和 Argoverse 2 的长时域外推上取得领先性能。

### 研究问题
- 早期双帧场景流估计器仅依赖瞬时两帧运动，缺乏长期时间相关性，未来预测的外推能力较差。
- 近期部分多帧序列到序列方法虽然尝试建模多帧场景流，但存在两个问题：输入帧数增加导致计算开销沉重；运动传播无效导致长时域预测性能退化。
- 因此，论文关注如何在连续序列中充分挖掘长期时间依赖，同时控制计算开销并缓解长时域预测退化。

### 核心思路/方法
- 提出 MESSENGER，一种记忆增强的序列场景流估计流程。
- 设计记忆缓冲，显式存储多个历史流估计和隐状态，用于挖掘连续序列中自然存在的长期时间依赖。
- 对每个输入帧，将时间上存储的流与状态进行关联和检索，以“下一帧预测”的方式预测当前帧的初始化流。
- 开发不确定性感知重加权模块，用于过滤不可靠的检索结果，并缓解累积误差。
- 采用自回归预测范式，使网络基于历史观测逐步学习下一帧分布。

### 主要贡献
- 提出记忆增强的序列场景流估计框架 MESSENGER，通过记忆缓冲显式存储历史流估计与隐状态，以建模长期时间依赖。
- 引入自回归下一帧预测范式，用历史存储的流与状态关联检索来预测当前帧初始化流。
- 设计不确定性感知重加权模块，过滤不可靠检索并缓解累积误差。
- 在 nuScenes 和 Argoverse 2 上进行大量实验，长时域未来外推中 EPE3D 分别降低 71.6% 和 67.7%，达到 state-of-the-art 性能。
- 作者指出性能优势可归因于所设计的自回归预测范式，该范式自然迫使网络基于历史观测逐步学习下一帧分布；代码将在指定 GitHub 链接发布。

### 局限性
- 摘要未提供足够信息说明方法的具体失败场景或边界条件。
- 摘要未提供足够信息说明记忆缓冲的存储开销、推理延迟或内存增长情况。
- 摘要未提供足够信息说明不确定性感知重加权模块在极端噪声或检索完全失败时的表现。
- 摘要未提供足够信息说明除 nuScenes 和 Argoverse 2 外，方法在其他数据集或传感器配置上的泛化能力。
- 摘要未提供足够信息说明消融实验细节、各模块单独贡献以及超参数敏感性。

### 阅读优先级
高。理由：该论文直接针对序列场景流估计中的长期时间建模、计算开销与长时域预测退化问题，提出记忆增强与自回归下一帧预测的组合方案，并在 nuScenes 和 Argoverse 2 上报告了显著的长时域外推 EPE3D 降低，属于 Dynamic / 4D Reconstruction 方向中问题明确、指标提升突出的工作。

</details>

<details>
<summary>Abstract</summary>

Scene flow can capture low-level 3D motion displacements in dynamic scenarios. Early pairwise estimators relying on instantaneous two-frame motion lack long-term temporal correlation and also struggle with poor extrapolation ability in future prediction. Although some recent methods attempt to explore multi-frame scene flow estimation in a sequence-to-sequence manner, they typically suffer from heavy computational overhead with increasing input frames and long-horizon prediction degradation due to ineffective motion propagation. To address these problems, we propose a novel memory-enhanced sequential scene flow pipeline, called MESSENGER. To sufficiently mine long-term temporal dependencies naturally within consecutive sequences, a memory buffer is designed by explicitly storing multiple history flow estimates and latent states. For each input frame, the temporally stored flows and states are correlated and retrieved to predict the current initialized flow in a next-frame forecasting manner. Furthermore, we develop an uncertainty-aware reweighting module to filter unreliable retrievals and mitigate accumulated errors. Extensive experiments on nuScenes and Argoverse 2 demonstrate state-of-the-art performance of our MESSENGER, reducing EPE3D by 71.6% on nuScenes and 67.7% on Argoverse 2 in long-horizon future extrapolation. This superiority can be attributed to our designed autoregressive forecasting paradigm, which naturally forces the network to progressively learn the next-frame distribution based on history observations. Code will be released at https://github.com/liujiuming123/Messenger.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-13 - WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World

**Authors:** Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
**Links:** [abs](https://arxiv.org/abs/2610.18846) - [pdf](https://arxiv.org/pdf/2610.18846)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, mesh reconstruction

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
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has been becoming a promising 3D reconstruction technique because of its advantage of high-fidelity rendering effect with high efficiency. However, it still suffers from coarse density control and semantically blind loss functions when reconstructing the fine-grained structures in complex urban scenes. Thus, this study proposes SG-GS, a semantic-guided 3DGS method for fine-grained structure reconstruction. It takes the semantic segmentation deduced by the Segment Anything Model (SAM) as a constraint and systematically integrates it into both Gaussian density control and loss function design. On the one hand, a semantic-constrained adaptive density control mechanism is constructed, which dynamically allocates gradient thresholds to different semantic regions of the scene and introduces an additional boundary-enhanced densification strategy, so that new Gaussians are directed to structurally critical regions. On the other hand, a multi-feature guided loss function is designed, and fine-grained supervision signals are gradually introduced through a phased progressive training strategy, alleviating the artifacts caused by the lack of semantic constraints in the basic loss. Experiments on three datasets show that the proposed method consistently improves reconstruction accuracy. Compared with the original 3DGS, the PSNR increases by approximately 2.7% to 5.2%, while artifacts on linear structures and boundary blurring are effectively mitigated. The method can serve the fine-grained 3D reconstruction of urban scenes.

</details>

#### 2026-10-08 - Slot3R: Set-Associative Spatial Memory for Streaming 3D Reconstruction

**Authors:** Xiyuan Zhang, Yanming Yang, Kaiyuan Xu, Ruibo Li, Chi Zhang
**Links:** [abs](https://arxiv.org/abs/2610.12282) - [pdf](https://arxiv.org/pdf/2610.12282)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Slot3R: Set-Associative Spatial Memory for Streaming 3D Reconstruction
- 作者：Xiyuan Zhang, Yanming Yang, Kaiyuan Xu, Ruibo Li, Chi Zhang
- 出版日期：2026-10-08T16:39:39Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.12282) / [PDF](https://arxiv.org/pdf/2610.12282)

### 一句话总结
Slot3R 提出一种免训练、集合关联式的空间记忆改造方案，使新观测与已有记忆条目共享地址但可保留多个状态，从而在流式 3D 重建中避免因空间邻近而错误融合互补证据。

### 研究问题
流式 3D 重建需要在线处理不断扩展的场景，同时保留每一帧的信息。空间记忆按重建出的 3D 位置组织历史，是自然的方案。但 Point3R 同时使用空间邻近性来关联新观测与已有记忆条目，并决定是否融合二者，从而混淆了“共址”与“状态身份”。由于指针汇总的是图像块，邻近的指针可能编码不同表面、视角或可见性条件；将它们平均会在后续帧有机会消歧之前破坏互补证据。论文主张：位置应决定地址，而不应决定观测是否必须合并。

### 核心思路/方法
- 核心原则：位置用于确定记忆地址，而非强制观测融合。
- 实现为 Slot3R，一种免训练、集合关联式的改造方案：允许多个状态在同一地址下共存。
- 保持预训练的 Point3R 主干冻结。
- 使用有界稀疏读出，进一步解耦持久存储与逐帧解码器访问。

### 主要贡献
- 提出 Slot3R，以集合关联式空间记忆改造 Point3R，在不重新训练的前提下支持同一地址多状态共存。
- 在 300-500 采样帧设置下，将 Point3R 的点云精度误差（Acc）在 7Scenes 上降低 57.1%-63.1%，在 NeuralRGBD 上降低 64.0%-72.0%。
- 在三个位姿基准上降低 Sim(3) 对齐的绝对轨迹误差（ATE）。
- 在视频深度估计上保持竞争力。
- 在相同协议下，600 到 1000 采样帧的所有评估设置中约以 19 FPS 完成，而 Point3R 与 InfiniteVGGT 在 800 帧及以后出现内存不足。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、适用场景限制、未评估的基准或具体资源消耗细节。

### 阅读优先级
高。理由：该工作针对流式 3D 重建中空间记忆的关键设计缺陷提出免训练改造，并在多个基准上报告了显著的精度提升与内存可扩展性优势，同时保持实时速度，对相关方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Streaming 3D reconstruction must preserve evidence from each frame while processing an expanding scene online. Spatial memory is a natural fit because it organizes history by reconstructed 3D location. Yet Point3R uses spatial proximity both to associate a new observation with an existing memory entry and to decide whether to fuse it, conflating co-location with state identity. Because pointers summarize image patches, nearby pointers may encode distinct surfaces, viewpoints, or visibility conditions; averaging them can destroy complementary evidence before later frames disambiguate it. We argue that location should determine address, not whether observations must merge. Slot3R realizes this principle as a training-free, set-associative retrofit that lets multiple states coexist at a shared address while keeping the pretrained Point3R backbone frozen. A bounded sparse readout further decouples persistent storage from per-frame decoder access. At 300-500 sampled frames, Slot3R reduces Point3R's point-cloud accuracy error (Acc) by 57.1%-63.1% on 7Scenes and 64.0%-72.0% on NeuralRGBD, lowers Sim(3)-aligned absolute trajectory error (ATE) on all three pose benchmarks, and remains competitive on video-depth estimation. It completes all evaluated settings from 600 to 1000 sampled frames at about 19 FPS under the same protocol, whereas Point3R and InfiniteVGGT run out of memory at 800 frames and beyond.

</details>

#### 2026-10-08 - Pose-Free Feed-Forward 3D Inpainting via Learnable Mask Attention and Support Token Refinement

**Authors:** Jingyi Pan, Dan Xu, Qiong Luo
**Links:** [abs](https://arxiv.org/abs/2610.11857) - [pdf](https://arxiv.org/pdf/2610.11857)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Pose-Free Feed-Forward 3D Inpainting via Learnable Mask Attention and Support Token Refinement
- 作者：Jingyi Pan, Dan Xu, Qiong Luo
- 出版日期：2026-10-08T12:38:48Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类；次要分类未提供）
- 链接：abs: https://arxiv.org/abs/2610.11857；pdf: https://arxiv.org/pdf/2610.11857；项目页：https://rorisis.github.io/FreeInpaint/

### 一句话总结
FreeInpaint 是一个无需相机位姿的前馈式 3D 场景补全框架，直接从未标定位姿的多视角带掩码图像生成完整且 3D 一致的场景，并通过可学习掩码注意力与支持 Token 精化应对掩码带来的位姿估计退化和严重遮挡下的外观证据不足问题。

### 研究问题
3D 场景补全旨在恢复编辑后 3D 场景中缺失或被遮挡的区域，同时保证几何与纹理一致性。现有方法通常需要精确标定的相机位姿，这限制了其在随意拍摄、真实野外场景中的适用性，并带来额外的预处理开销。论文要解决的问题是：如何在不依赖预先计算相机位姿的情况下，从带掩码的多视角图像直接完成 3D 一致性的场景补全。

### 核心思路/方法
论文提出 FreeInpaint，一个前馈框架，将 3D 基础模型扩展用于带掩码输入，把参考视图中的掩码区域传播到其他无位姿视图，从而在保留模型原生恢复相机位姿与场景几何能力的同时，连接 3D 重建与场景补全。

针对适配过程中的两个关键挑战，论文提出两项机制：
1. **可学习掩码注意力（Learnable Mask Attention）**：掩码区域会破坏跨视图对应关系推理，进而降低位姿估计与几何恢复质量。该机制保持可靠观测的空间锚定，同时让掩码区域在更深层逐步吸收有用上下文。
2. **支持 Token 精化（Support Token Refinement）**：在严重遮挡下，单次前向传播往往缺乏足够的外观证据以实现高保真补全。该策略注入扩散生成的支持证据，作为置信度加权的辅助 Token 来精化欠观测区域，同时保持原始空间锚定。

### 主要贡献
- 提出 FreeInpaint，一个无需相机位姿的前馈式 3D 场景补全框架，可直接从无位姿多视角带掩码图像生成完整、3D 一致的场景。
- 提出可学习掩码注意力机制，缓解掩码区域对跨视图对应推理的破坏，保护位姿估计与几何恢复。
- 提出支持 Token 精化策略，利用扩散生成的支持证据以置信度加权辅助 Token 形式精化严重遮挡下的欠观测区域。
- 摘要称在多个数据集上的大量实验表明，FreeInpaint 取得更优的补全质量，消除对预计算相机位姿的依赖，并保持较快推理速度。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、方法适用边界、对扩散支持证据生成质量的依赖程度、计算资源需求或定量指标细节，因此无法基于所给信息判断其局限性。

### 阅读优先级
中。理由：该论文针对“无需相机位姿的 3D 场景补全”这一明确痛点，提出前馈框架与两项针对性机制，主题与 3D 重建及多视角几何方向高度相关；但摘要未提供定量结果、数据集名称与实验设置细节，若需评估其实际性能与可复现性，需进一步阅读正文。

</details>

<details>
<summary>Abstract</summary>

3D scene inpainting aims to recover missing or occluded regions in edited 3D scenes, while ensuring geometric and textural consistency. Existing approaches, however, typically require accurately calibrated camera poses, which restricts their applicability in casual, in-the-wild scenarios and introduces additional preprocessing overhead. To overcome this limitation, we present FreeInpaint, a novel feed-forward framework that generates complete and 3D-consistent scenes directly from unposed multi-view images with masked regions. At its core, FreeInpaint extends a 3D foundation model to propagate masked regions from a reference view to other unposed views, bridging 3D reconstruction and scene inpainting while preserving the model's native ability to recover camera poses and scene geometry. Our method addresses two key challenges in adapting feed-forward 3D foundation models to masked inputs. First, masked regions can corrupt cross-view correspondence reasoning, degrading pose estimation and geometry recovery. To address this, we introduce a Learnable Mask Attention mechanism that preserves the spatial anchoring of reliable observations while allowing masked regions to progressively absorb useful context in deeper layers. Second, under severe occlusions, a single forward pass often lacks sufficient appearance evidence for high-fidelity completion. Therefore, we propose a Support Token Refinement strategy, which injects diffusion-generated support evidence as confidence-weighted auxiliary tokens to refine under-observed regions while preserving the original spatial anchor. Extensive experiments across diverse datasets demonstrate that FreeInpaint achieves superior inpainting quality, eliminating the reliance on pre-computed camera poses while keeping a fast inference speed. The project page is https://rorisis.github.io/FreeInpaint/.

</details>

#### 2026-10-08 - TAP3D: Thermal-Assisted 3D Human Point Clouds

**Authors:** Xie Zhang, Chengxiao Li, Xuan Liu, Chenshu Wu
**Links:** [abs](https://arxiv.org/abs/2610.11241) - [pdf](https://arxiv.org/pdf/2610.11241)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, sparse reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TAP3D: Thermal-Assisted 3D Human Point Clouds
- 作者：Xie Zhang, Chengxiao Li, Xuan Liu, Chenshu Wu
- 出版日期：2026-10-08T04:42:25Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.11241 ；PDF https://arxiv.org/pdf/2610.11241

### 一句话总结
TAP3D 提出利用低成本热阵列传感器从人体热特征重建 3D 人体点云，并声称这是首个此类系统，在成本、密度、人体敏感性与隐私方面具有优势。

### 研究问题
论文关注现有人体点云获取方式（LiDAR、雷达、深度相机等）在高成本、稀疏重建和隐私方面的固有问题，试图探索用低成本热阵列实现 3D 人体点云重建。其核心挑战包括深度估计、热干扰以及多人分离。

### 核心思路/方法
论文提出一种物理信息驱动的设计，将前向热物理模型与两个模块结合：
1. 多基元估计（multi-primitive estimation）：用于深度和其他热属性的自监督联合恢复；
2. 几何透视融合（geometric perspective fusion）：用于抑制干扰并分离多人。

系统使用单个商用热阵列传感器实现，并构建了一个大规模数据集用于评估，包含 160K 样本、8 个环境、11 位用户。

### 主要贡献
- 提出 TAP3D，摘要称其为首个从人体热特征重建 3D 人体点云的系统。
- 针对深度估计、热干扰和多人分离挑战，提出结合前向热物理模型、多基元估计与几何透视融合的物理信息设计。
- 使用单个商用热阵列传感器实现系统，并构建大规模数据集（160K 样本、8 环境、11 用户）进行评估。
- 在密集点云生成上达到较高精度，并支持下游任务：跌倒检测 91.46%、室内跟踪 21.86 cm MAE、人体网格恢复 4.87 cm 误差。
- 开源地址为 https://github.com/aiot-lab/TAP3D。

### 局限性
摘要未提供足够信息。摘要未说明传感器具体型号、环境条件限制、计算开销、实时性、对遮挡或极端姿态的鲁棒性、数据集标注方式与偏差，也未给出与其他方法的完整对比实验细节。

### 阅读优先级
高。理由：该论文提出从热特征重建 3D 人体点云的新范式，强调隐私优先与完全被动人体感知，并报告了多个下游任务结果；若研究兴趣涉及人体感知、3D 重建、隐私保护感知或低成本传感，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Human body point clouds are a versatile representation for AI-enabled human sensing. However, existing methods using LiDAR, radar, and depth cameras suffer from inherent drawbacks in high cost, sparse reconstruction, and privacy concerns, etc. In this paper, we exploit low-cost thermal arrays and present TAP3D, the first system to reconstruct 3D human point clouds from body heat signatures, offering significant advantages in cost, density, human sensitivity, and privacy. To overcome major challenges in depth estimation, thermal interference, and multi-person separation, we propose a novel physics-informed design, which integrates a forward thermal physics model with two distinct modules: multi-primitive estimation for self-supervised joint recovery of depth and other thermal properties, and geometric perspective fusion for suppressing interference and disentangling multiple people. We implement TAP3D using a single commodity thermal array sensor and build a large-scale dataset (160K samples, 8 environments, 11 users) for evaluation. TAP3D achieves remarkable accuracy for dense point cloud generation, enabling downstream tasks like fall detection (91.46%), indoor tracking (21.86 cm MAE), and human mesh recovery (4.87 cm error). By transforming body heat into point clouds for the first time, TAP3D pioneers a new paradigm for privacy-first, fully passive human sensing for many applications. TAP3D is open-sourced at https://github.com/aiot-lab/TAP3D.

</details>

#### 2026-10-07 - Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies

**Authors:** Yihan Li, Yating Feng, Shengjiu Sun, Jianing Chen, Hao Ren, Bowen Yang, Weisheng Xu, Qiwei Wu, Hui Cheng, Renjing Xu
**Links:** [abs](https://arxiv.org/abs/2610.10479) - [pdf](https://arxiv.org/pdf/2610.10479)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies
- 作者：Yihan Li, Yating Feng, Shengjiu Sun, Jianing Chen, Hao Ren, Bowen Yang, Weisheng Xu, Qiwei Wu, Hui Cheng, Renjing Xu
- 出版日期：2026-10-07T17:37:20Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry（3D 重建与多视角几何）；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.10479 ；PDF https://arxiv.org/pdf/2610.10479

### 一句话总结
Agentic RSR 是一个通过同一操作任务把场景重建、策略开发与真实机器人执行串联起来的 Real-to-Sim-to-Real 框架，借助智能体迭代优化仿真场景并由编码智能体生成可执行策略，使仿真中习得的策略迁移到真机后仍保留大部分性能。

### 研究问题
论文关注的核心问题是：真实机器人工作空间的仿真必须保留任务相关的交互，而仿真中开发的策略又必须能基于真实机器人可获得的观测运行；然而场景重建与策略开发在实践中常被分开处理。Agentic RSR 试图弥合这一割裂，使重建、策略开发与真机执行围绕同一操作任务形成闭环。

### 核心思路/方法
给定工作空间视频、任务描述和已知机器人模型，框架让一个智能体恢复度量尺度，利用视觉反馈迭代精化场景，并在 MuJoCo 中检查任务相关交互。随后由编码智能体开发可执行策略，策略从特权物体位姿逐步推进到视觉观测和随机化仿真。该策略在一次调用中可交错执行多个观测与动作，智能体则依据执行反馈决定继续、重试或修改方案。一个共享的任务级接口把策略和累积经验带到真实机器人，由新观测和安全检查指导执行。

### 主要贡献
- 提出 Agentic RSR 框架，通过同一操作任务将场景重建、策略开发与真机执行连接起来。
- 在场景重建中引入智能体式的度量尺度恢复、视觉反馈迭代精化与 MuJoCo 中的任务相关交互检查。
- 由编码智能体开发可执行策略，支持策略在单次调用中交错多个观测与动作，并利用执行反馈进行继续、重试或修改。
- 通过共享任务级接口把策略与累积经验迁移到真实机器人，并结合新观测与安全检查执行。
- 在 18 个重建场景、两种机器人上给出四视角 Depth MAE 均值 0.1057 m、Lab ΔE76 均值 11.04、灰度 SSIM 均值 0.6990；真机实验中总体任务成功率达到仿真任务成功率的 80%。

### 局限性
摘要未提供足够信息说明该框架在更广泛任务、物体类别、光照或动态环境下的适用性；摘要未提供足够信息说明真机实验中未成功案例的具体失败模式；摘要未提供足够信息说明重建质量指标与下游策略成功率之间的定量关系；摘要未提供足够信息说明安全检查和人工干预的具体机制与成本；摘要未提供足够信息说明计算资源、运行时间或数据规模方面的限制。

### 阅读优先级
高。理由：该论文把场景重建与机器人策略开发统一到 Real-to-Sim-to-Real 闭环中，属于 3D 重建与机器人操作交叉方向；摘要同时给出了重建指标和真机成功率，且声明代码与重建场景数据将公开，便于后续复现与比较。

</details>

<details>
<summary>Abstract</summary>

A simulation of a real robot workspace must preserve task-relevant interactions, while policies developed in it must operate on observations available to the real robot. Yet scene reconstruction and policy development are often treated separately. We present Agentic Real-to-Sim-to-Real (Agentic RSR), a framework that links scene reconstruction, policy development, and real-robot execution through the same manipulation task. Given a workspace video, a task description, and a known robot model, an agent recovers metric scale, iteratively refines the scene using visual feedback, and checks task-relevant interactions in MuJoCo. A coding agent then develops an executable policy, progressing from privileged object poses to visual observations and randomized simulation. The policy can interleave multiple observations and actions within one invocation, while the agent uses execution feedback to continue, retry, or revise its approach. A shared task-level interface carries the policy and accumulated experience to the real robot, where fresh observations and safety checks guide execution. Across 18 reconstructed scenes involving two robots, the mean four-view Depth MAE against reference depth estimates is 0.1057 m, the mean Lab $ΔE_{76}$ is 11.04, and the mean grayscale SSIM is 0.6990. In real-robot experiments, the aggregate task success rate reaches 80% of the simulation task success rate, indicating substantial retention of simulated performance on hardware. Code and reconstructed scene data will be made publicly available.

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-13 - CoTL: Compact Token Learning for 3D Scene Representation

**Authors:** Han Liang, Sibo Wu, Anpei Chen, Rüdiger Westermann
**Links:** [abs](https://arxiv.org/abs/2610.18446) - [pdf](https://arxiv.org/pdf/2610.18446)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, scene representation, rendering

<details>
<summary>Abstract</summary>

We present CoTL, a framework that learns a compact set of tokens that preserves scene geometry and appearance from unposed multi-view images. Our encoder compresses the input images into small per-view sets of latent tokens that aggregate information across views to form a view-consistent scene representation. Each additional view expands the representation with only a small, resolution-independent set of tokens, allowing its capacity to grow with the available observations. To force this compact bottleneck to retain sufficient scene information, a query-based Gaussian decoder uses scene-independent queries to attend to the learned tokens and recover an explicit, renderable set of 3D Gaussian primitives. Novel-view rendering supervision trains the compact representation end to end through the reconstructed Gaussian scene. Experiments on \retenk{} and ACID show that the resulting compact, unstructured token set supports competitive novel-view synthesis and can serve as the latent space of a generative model for 3D Gaussian scene generation. Together, these results show that 3D Gaussian reconstruction is an effective objective for compact scene representation learning and the learned token space provides a basis for broader downstream tasks in 3D vision.

</details>

#### 2026-10-13 - PLEDGE: Progressive Lossy Error-Bounded Compression of 3D Gaussian Splatting

**Authors:** Mingze Xia, Yuxiao Li, Baixi Sun, Wenbo Li, Pu Jiao, Sheng Di, Franck Cappello, Hanqi Guo, Xin Liang
**Links:** [abs](https://arxiv.org/abs/2610.17605) - [pdf](https://arxiv.org/pdf/2610.17605)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

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

#### 2026-10-08 - LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views

**Authors:** Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong
**Links:** [abs](https://arxiv.org/abs/2610.12127) - [pdf](https://arxiv.org/pdf/2610.12127)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, view synthesis, rendering, splatting, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views
- 作者：Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong
- 出版日期：2026-10-08T15:19:58Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.12127

### 一句话总结
论文提出一种按场景构建的局部视图合成框架 LVS，通过复用已有视图并结合相对相机位姿进行 RGB-D 图像重用与残差修正，减少邻近视角下重复渲染的开销。

### 研究问题
交互式场景探索需要频繁更新视图，但小幅相机运动下可见内容大量重叠。常规 3D Gaussian Splatting 仍然对每个目标视图重新渲染，未利用这种图像重叠。仅靠几何 warp 无法恢复新暴露内容，且对深度误差敏感。

### 核心思路/方法
- 以相对位姿引导的 RGB-D 图像重用，替代邻近视图的重复场景渲染。
- 使用深度和相对位姿将源内容通过几何 warp 传输。
- 用一个轻量级多尺度网络预测 RGB 残差，以修正伪影并推断缺失外观。
- 缓存源特征，减少重复计算。

### 主要贡献
- 提出将场景渲染与局部视图更新分离的按场景框架，用于邻近视图的 RGB-D 图像重用。
- 结合几何 warp 与轻量多尺度残差网络，修正 warp 伪影并补全缺失外观。
- 在 GS-render 上，残差细化相比纯 warp 将 PSNR 提升约 0.72 dB。
- 在采集场景与渲染场景上的评估显示较低查询延迟，支持响应式场景探索，并可能应用于增强现实与虚拟现实。

### 局限性
摘要未提供足够信息。未提供关于失败案例、深度误差敏感性是否完全解决、泛化到更大幅度相机运动的能力、数据集规模、运行时具体数值、内存占用及与完整渲染方法的全面对比等细节。

### 阅读优先级
中。理由：该工作关注 3D Gaussian Splatting 在交互式探索中的渲染复用与延迟优化，问题明确且方法路线清晰；但摘要仅给出有限量化结果，是否具有广泛适用性需依赖正文实验细节，因此对相关方向研究者优先级较高，对一般读者为中等。

</details>

<details>
<summary>Abstract</summary>

Interactive scene exploration requires frequent view updates, although small camera motions preserve much of the visible content. Conventional 3D Gaussian Splatting nevertheless renders each target view, leaving this image overlap unexploited. Reusing rendered images offers an alternative. Geometric warping alone cannot recover newly exposed content and remains sensitive to depth errors. We propose a per-scene framework that replaces repeated scene rendering for nearby views with relative-pose-guided RGB-D image reuse. Geometric warping uses depth and relative pose to transport source content, while a lightweight multiscale network predicts RGB residuals to correct artifacts and infer missing appearance. Cached source features further reduce repeated computation. On GS-render, residual refinement improves PSNR by 0.72~dB over pure warping; evaluations on captured and rendered scenes demonstrate low query latency. This separation of scene rendering from local view updates supports responsive scene exploration, with potential applications in augmented and virtual reality.

</details>

#### 2026-10-08 - 2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map

**Authors:** Jiwon Park, Dong-Uk Seo, Hyun Myung
**Links:** [abs](https://arxiv.org/abs/2610.11752) - [pdf](https://arxiv.org/pdf/2610.11752)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, scene representation, rendering, splatting, robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map
- 作者：Jiwon Park, Dong-Uk Seo, Hyun Myung
- 出版日期：2026-10-08T11:41:38Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.11752

### 一句话总结
论文提出 2DGS-Planner，一种面向地面机器人的路径规划器，它通过栅格化从 2D Gaussian Splatting 地图中读取规划相关几何，而不是把单个高斯基元直接当作障碍物。

### 研究问题
论文关注的是：虽然 Gaussian splatting 提供了显式且可高效栅格化的场景表示，但由于高斯基元是通过有限重建视角下的 alpha 合成渲染联合优化得到的，因此单个高斯基元可能无法可靠地表示障碍物。基于这一背景，论文希望解决在 2D Gaussian Splatting 地图上进行地面机器人路径规划时，如何获得更可靠的规划相关几何与障碍表达。

### 核心思路/方法
论文提出 2DGS-Planner，其核心思路是通过栅格化从 2D Gaussian Splatting 地图中读取规划相关几何，而不是将单个高斯基元视为障碍物。

在离线路线图构建阶段，方法使用多视角归因，将由重建视角支持的非地面盘片的渲染法线离散度转换为结构分数。这些分数用于指导地面上的自适应节点采样。路径对齐的正交查询用于验证候选边，而圆柱查询用于估计局部间隙场，并将其缓存到边上。在线规划阶段，图搜索用于初始化路线，路径细化在考虑机器人尺寸和地面约束的同时复用缓存的间隙场。

### 主要贡献
- 提出 2DGS-Planner，一种基于栅格化的地面机器人路径规划器，可直接在 2D Gaussian Splatting 地图上读取规划相关几何。
- 使用多视角归因，将渲染法线离散度转化为结构分数，用于指导地面自适应节点采样。
- 使用路径对齐正交查询验证候选边，并使用圆柱查询估计局部间隙场，且将间隙场缓存到边上。
- 在线阶段结合图搜索初始化路线，并通过路径细化复用缓存间隙场，同时考虑机器人尺寸和地面约束。
- 摘要称实验显示，与所测试基线相比，方法在路线图连通性、间隙估计准确性和规划成功率方面有所提升。

### 局限性
- 摘要未提供足够信息说明具体实验设置、对比基线、数据集、评价指标细节和定量结果。
- 摘要未提供足够信息说明方法在复杂动态环境、不同机器人形态或大规模场景中的适用性。
- 摘要未提供足够信息说明离线路线图构建和在线路径细化的计算开销、实时性能或内存占用。
- 摘要未提供足够信息说明 2DGS 地图重建质量对规划性能的影响程度。
- 摘要未提供足够信息说明失败案例、安全性保证或与真实机器人部署相关的限制。

### 阅读优先级
中。理由：该论文将 Gaussian Splatting 场景表示与地面机器人路径规划结合，重点在于通过栅格化查询几何而非直接使用高斯基元作障碍，问题设定和方法流程较清晰，适合关注神经场景表示、机器人导航和路径规划交叉方向的研究者阅读。但当前仅提供摘要和元数据，缺少实验细节、基线和定量结果，无法据此判断其实际性能优势的强度，因此优先级评为中。

</details>

<details>
<summary>Abstract</summary>

Gaussian splatting provides an explicit and efficiently rasterizable scene representation for robot navigation. However, individual Gaussian primitives may not reliably represent obstacles as they are jointly optimized through alpha-composited rendering from a finite set of reconstruction views. We propose 2DGS-Planner, a path planner for ground robots that reads planning-relevant geometry from a 2D Gaussian splatting (2DGS) map through rasterization, rather than treating individual Gaussian primitives as obstacles. During offline roadmap construction, multi-view attribution converts rendered normal dispersion into structural scores for non-ground disks supported by the reconstruction views. These scores guide adaptive node sampling on the ground. Path-aligned orthographic queries validate candidate edges, while cylindrical queries estimate local clearance fields that are cached on the edges. During online planning, graph search initializes a route, and path refinement reuses the cached fields while accounting for the robot's dimensions and ground constraints. Experiments demonstrate improved roadmap connectivity, more accurate clearance estimation, and higher planning success compared with the tested baselines. These results support rasterization as an effective geometric query interface for planning directly on Gaussian maps. Code and data are available at https://2dgs-planner.github.io/

</details>

#### 2026-10-08 - Neural Caching of Prefiltered Radiance for Specular Lighting

**Authors:** Dmitrii Klepikov, Vladimir Frolov
**Links:** [abs](https://arxiv.org/abs/2610.11702) - [pdf](https://arxiv.org/pdf/2610.11702)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Neural Caching of Prefiltered Radiance for Specular Lighting
- 作者：Dmitrii Klepikov, Vladimir Frolov
- 出版日期：2026-10-08T11:09:13Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.11702) / [PDF](https://arxiv.org/pdf/2610.11702)

### 一句话总结
该论文提出了一种面向镜面光照的神经辐射缓存变体，通过反射方向参数化与粗糙度相关的辐射目标，让网络预测表面点上的预滤波入射辐射，并结合预计算 BRDF 积分图与 split-sum 近似来估计出射辐射。

### 研究问题
神经辐射缓存（NRC）为实时光线追踪提供场景光照的在线神经表示，但摘要指出该文关注的是如何将其适配到镜面光照场景。具体而言，论文试图解决镜面光照下 NRC 的表现问题，并声称在 Bunny 与 Specular Sponza 上相比所评估的 NRC 基线，能更快收敛到累积路径追踪参考并改善镜面光照质量。

### 核心思路/方法
- 提出一种 NRC 变体，专门面向镜面光照。
- 采用反射方向参数化。
- 使用粗糙度相关的辐射目标（roughness-dependent radiance target）。
- 网络预测单个表面点上的预滤波入射辐射。
- 将预测结果与预计算的 BRDF 积分图结合，通过 split-sum 近似估计出射辐射。
- 方法为在线训练，能够在渲染过程中自适应调整缓存，并保持实时性能。

### 主要贡献
- 提出了一种针对镜面光照的 NRC 变体，引入反射方向参数化与粗糙度相关辐射目标。
- 将网络预测的预滤波入射辐射与预计算 BRDF 积分图及 split-sum 近似结合，用于出射辐射估计。
- 在 Bunny 和 Specular Sponza 上报告了与所评估 NRC 基线的比较，显示更快收敛到累积路径追踪参考并改善镜面光照质量。
- 方法为在线训练，能够在渲染过程中适应缓存并维持实时性能。

### 局限性
- 摘要未提供足够信息说明方法在非镜面或复杂材质场景下的表现。
- 摘要未提供足够信息说明实验设置、基线细节、定量指标与消融实验。
- 摘要未提供足够信息说明实时性能的具体数值、硬件条件或训练开销。
- 摘要未提供足够信息说明该方法是否存在伪影、稳定性或泛化性方面的限制。

### 阅读优先级
高。理由：该论文聚焦实时光线追踪中的神经辐射缓存与镜面光照这一具体问题，提出了明确的参数化与目标设计，并报告了在标准测试场景上的收敛速度与质量改善；对于关注神经渲染、实时全局光照与镜面反射建模的读者具有直接相关性。

</details>

<details>
<summary>Abstract</summary>

Neural Radiance Caching (NRC) provides an online neural representation of scene illumination for real-time path tracing. This paper presents an NRC variant tailored to specular lighting through a reflection-direction parameterization and a roughness-dependent radiance target. Our network predicts prefiltered incoming radiance at individual surface points, which is combined with a precomputed BRDF integration map using the split-sum approximation to estimate outgoing radiance. On Bunny and Specular Sponza, the reported comparisons indicate faster convergence to the accumulated path-tracing reference and improved specular-lighting quality relative to the evaluated NRC baselines. Our online-trained method maintains real-time performance while adapting its cache during rendering.

</details>

#### 2026-10-08 - PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting

**Authors:** Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi
**Links:** [abs](https://arxiv.org/abs/2610.11572) - [pdf](https://arxiv.org/pdf/2610.11572)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting
- 作者：Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi
- 出版日期：2026-10-08T09:27:17Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.11572) / [PDF](https://arxiv.org/pdf/2610.11572)

### 一句话总结
PAM-ToD 是一个轻量级即插即用模块，在固定预训练 3DGS 参数的前提下，用少量目标时段锚点图像学习颜色修正，实现跨时段的外观适配。

### 研究问题
如何将预训练的 3D Gaussian Splatting（3DGS）道路场景适配到新的时段：既要仅用少量锚点图像学习外观变化，又要保持一致的实时渲染能力。

### 核心思路/方法
- 保持预训练 3DGS 参数不变，仅学习颜色修正，属于轻量级 plug-in 方案。
- 对每个 Gaussian 的既有颜色进行缩放以建模光照变化，并加入加性项表达额外亮度变化（例如夜间路灯开启）。
- 在简化成像模型下，从源外观与目标外观的关系中消去不变的表面反照率，从而无需单独估计反照率和光照即可学习这些修正。
- 修正覆盖全场景，但允许按位置和按 Gaussian 变化；同时抑制修正的突变以引导从少量锚点图像中学习。

### 主要贡献
- 提出 PAM-ToD：即插即用的轻量外观建模模块，在冻结预训练 3DGS 参数的情况下进行颜色修正学习。
- 利用简化成像模型消去反照率的思路，避免显式分解反照率与光照。
- 引入 CARLA-ToD 基准，具有跨三个时段匹配的几何、相机位姿和运动物体轨迹。
- 在静态与动态设置下，PAM-ToD 相比基线取得更高 PSNR 和更低 LPIPS；即使锚点图像来自多相机单次同步采集也有效。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败情形、对锚点数量的敏感度、计算开销、泛化到 CARLA 之外真实数据的表现，以及与其他需要微调 3DGS 参数的方法相比的具体限制。

### 阅读优先级
中。理由：论文聚焦 3DGS 的跨时段外观适配，提出即插即用、冻结参数的轻量方案，并给出新基准 CARLA-ToD，对实时道路场景渲染与外观编辑方向有参考价值；但未提供额外兴趣方向，且摘要中的实验结论较为概括，是否深入阅读取决于是否关注 3DGS 外观建模、跨域渲染或自动驾驶场景仿真。

</details>

<details>
<summary>Abstract</summary>

Adapting a pre-trained 3D Gaussian Splatting (3DGS) road scene to a new time of day requires learning appearance changes from a few anchor images while preserving consistent, real-time rendering. We propose PAM-ToD, a lightweight plug-in that learns color corrections while keeping the pre-trained 3DGS parameters fixed. PAM-ToD scales each Gaussian's existing color to model illumination changes and uses an additive term for additional brightness, such as when street lamps turn on at night. Under a simplified image formation model, unchanged surface albedo can be eliminated from the relation between source and target appearances, allowing us to learn these corrections without separately estimating albedo and illumination. The model corrects colors across the scene while allowing the corrections to vary by location and by Gaussian. To guide learning from a few anchor images, it discourages abrupt spatial changes in these corrections. We also introduce CARLA-ToD, a benchmark with matching geometry, camera poses, and moving-object trajectories across three times of day. A few target-time anchor images are used to train each plug-in, while separate views are used for evaluation. Across the static and dynamic settings, PAM-ToD achieves higher PSNR and lower LPIPS than the baselines, even when the anchor images come from a single synchronized capture across multiple cameras.

</details>

#### 2026-10-08 - FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome

**Authors:** Ziyuan Luo, Haoliang Li, Renjie Wan
**Links:** [abs](https://arxiv.org/abs/2610.11364) - [pdf](https://arxiv.org/pdf/2610.11364)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome
- 作者：Ziyuan Luo, Haoliang Li, Renjie Wan
- 出版日期：2026-10-08T06:56:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.11364) / [PDF](https://arxiv.org/pdf/2610.11364)

### 一句话总结
FlyMark 提出一种免训练的 3D Gaussian Splatting 隐形水印方法，直接把带密钥的消息写入已发布参数中的零阶颜色，并以果蝇连接组感光器导出的载体方向作为固定几何基，从而在不改动几何与高阶外观参数的前提下实现可长期检验的所有权证据。

### 研究问题
3DGS 场景训练完成后以可移植参数数组的形式发布，可被复制、剪枝、重新量化或在训练管线之外重打包。因此，所有权证据最理想的存在形式是“驻留在发布参数中、且在嵌入工具消失后仍可检验”。

现有 3DGS 水印通常把嵌入或提取绑定到场景优化、学习式解码器或渲染视图上，导致证据只能与第二个训练产物共存。论文要解决的问题是：如何在不依赖训练、学习解码器和渲染视图的情况下，把水印写进 3DGS 文件本身的参数中，并保持可提取性。

### 核心思路/方法
- 载体方向来自已发表连接组的感光器，是一个可引用的版本化产物，穷尽地固定了几何，无需按场景调参。
- 虚拟观察者从存储的中心、颜色和不透明度出发，沿场景归一化轨道读取锥体表观亮度。
- 使用带密钥的抖动量化索引调制码，把每个消息比特复制到这些观测上。
- 通过一次稀疏有界最小二乘求解，在每通道线性 RGB 硬边界下，对已有零阶颜色施加非彩色偏移来实现目标。
- 所有几何与高阶外观参数按位保持不变；提取只需要锥体查询、取整和多数投票。
- 在模型域威胁模型下，于合成和真实场景上评估。

### 主要贡献
- 提出免训练的 3DGS 隐形水印框架 FlyMark，将密钥消息写入发布参数而非依赖第二个训练产物。
- 利用果蝇连接组感光器导出载体方向，提供固定、可引用、无需逐场景调参的几何基。
- 设计基于虚拟观察者的锥体亮度读取、抖动量化索引调制与稀疏有界最小二乘写入流程，并保持几何与高阶外观参数按位不变。
- 提取阶段仅需锥体查询、取整和多数投票。
- 在合成与真实场景的模型域威胁模型下，报告了高干净比特准确率与视觉保真度，并能清晰区分匹配密钥与错误密钥。

### 局限性
- 摘要未提供足够信息说明该方法对剪枝、重新量化、重打包等具体攻击的鲁棒性细节。
- 摘要未提供足够信息说明计算开销、参数规模影响或实际部署成本。
- 摘要未提供足够信息说明提取是否需要原始场景的特定元数据（如轨道定义、归一化方式）才能复现。
- 摘要未提供足够信息说明在非模型域威胁模型（如渲染视图攻击、几何编辑攻击）下的表现。
- 摘要未提供足够信息说明与现有 3DGS 水印方法在相同条件下的定量对比。

### 阅读优先级
中。理由：该工作针对 3DGS 所有权保护这一明确问题，提出免训练、参数内嵌、不依赖学习解码器的技术路线，并引入连接组感光器作为固定载体方向，思路较有辨识度；摘要已给出方法框架与模型域威胁模型下的定性结果。但摘要未披露鲁棒性、开销和对比细节，是否适合深入阅读取决于读者对 3DGS 水印、参数级嵌入或生物结构启发式设计的兴趣。

</details>

<details>
<summary>Abstract</summary>

A trained 3D Gaussian Splatting (3DGS) scene ships as a portable parameter array that can be copied, pruned, requantized, or repackaged outside its training pipeline, so ownership evidence is most useful when it lives in the released parameters and remains checkable long after the embedding tooling is gone. Existing 3DGS watermarks typically tie embedding or extraction to scene optimization, a learned decoder, or rendered views, so the evidence survives only as long as a second trained artifact does. FlyMark instead writes a keyed message into the parameters a 3DGS file already stores. Its carrier directions are derived from the photoreceptors of a published connectome, a citable versioned artifact that fixes the geometry exhaustively and leaves nothing to tune per scene. A virtual observer reads cone-wise apparent luminance along a scene-normalized orbit from stored centers, colors, and opacities; a keyed dithered quantization-index-modulation code replicates each message bit across these observations; and one sparse bounded least-squares solve realizes the targets through achromatic shifts of existing degree-zero colors under a hard per-channel linear-RGB bound. All geometry and higher-order appearance parameters are preserved bit-identically, and extraction needs only cone queries, rounding, and majority voting. Under a model-domain threat model on synthetic and real scenes, FlyMark attains high clean bit accuracy and visual fidelity while cleanly separating matched from wrong keys.

</details>

#### 2026-10-08 - IntrinSync: Joint Intrinsic Decomposition and Reciprocal Rendering

**Authors:** Zheng Gu, Rui Huang, Xilu Zhang, Jingbo Zhang, Min Lu, Zhida Sun, Dani Lischinski, Daniel Cohen-Or, Hui Huang
**Links:** [abs](https://arxiv.org/abs/2610.11138) - [pdf](https://arxiv.org/pdf/2610.11138)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, rendering, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IntrinSync: Joint Intrinsic Decomposition and Reciprocal Rendering
- 作者：Zheng Gu, Rui Huang, Xilu Zhang, Jingbo Zhang, Min Lu, Zhida Sun, Dani Lischinski, Daniel Cohen-Or, Hui Huang
- 出版日期：2026-10-08T03:05:47Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.11138

### 一句话总结
该论文提出统一框架 IntrinSync，通过联合通道建模与逆向—正向渲染互惠机制，实现内在属性分解与正向渲染的协同。

### 研究问题
逆向渲染旨在将图像分解为外观、光照、几何、材质等内在属性，但这些属性本身相互依赖。摘要指出，现有方法要么单独建模各内在通道，要么将逆向渲染与正向渲染视为分离过程，因而未能充分利用这种相互依赖关系。可靠分解应不仅使各内在映射单独合理，还应彼此兼容以共同解释图像。

### 核心思路/方法
论文提出 IntrinSync，一个统一框架，通过两个层面捕捉上述相互依赖：
- 通道层面：以 1 对 N 映射，将输入 RGB 联合分解为 albedo、shading、表面法线、roughness、metallic 五种映射，使生成过程中通道间可进行信息交换。
- 过程层面：通过双循环一致性目标建立逆向—正向渲染的互惠关系，使闭环中对应预测相互对齐。

### 主要贡献
- 提出 IntrinSync 统一框架，联合建模内在通道并建立逆向—正向渲染互惠。
- 在通道层面使用 1 对 N 映射进行联合分解，促进通道间信息交换。
- 在过程层面引入双循环一致性目标，对齐闭环中的对应预测。
- 在三个数据集上实验，摘要称该方法取得有竞争力的内在估计与正向渲染性能，并提升连贯性与物理一致性。
- 除分解外，提供面向图像编辑的物理基础接口，可显式操控内在属性并渲染回 RGB 图像。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败情形、适用边界、计算开销、对特定数据分布的依赖，也未给出与基线的完整定量对比细节或消融分析。

### 阅读优先级
中。理由：该工作聚焦逆向渲染中内在属性相互依赖这一核心问题，提出通道联合建模与逆向—正向循环一致性的统一框架，并涉及图像编辑接口，主题具有明确的研究价值；但摘要仅给出方向性描述与“三个数据集上有竞争力”的结论，未提供具体实验设置、量化结果或局限性讨论。是否优先精读取决于读者对内在分解、可重光照编辑或循环一致性训练的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Inverse rendering decomposes an image into intrinsic properties such as appearance, illumination, geometry, and material, yet these properties are inherently interdependent. A reliable decomposition should produce intrinsic maps that are not only individually plausible, but also mutually compatible in explaining the image. However, existing methods either model intrinsic channels in isolation or treat inverse and forward rendering as separate processes, leaving the interdependence underexploited. In this paper, we introduce IntrinSync, a unified framework that captures this interdependence through joint-channel modeling and reciprocal inverse-forward rendering. At the channel level, we jointly decompose an input RGB into albedo, shading, surface normal, roughness, and metallic maps through a 1-to-N mapping, enabling information exchange across channels throughout generation. At the process level, we establish inverse-forward reciprocity through a dual cycle-consistent objective that aligns corresponding predictions across a closed loop. Experiments on three datasets demonstrate that our method achieves competitive intrinsic estimation and forward rendering performance, improving coherence and physical consistency. Beyond decomposition, IntrinSync provides a physically grounded interface for image editing, allowing intrinsic properties to be explicitly manipulated and rendered back into RGB images.

</details>

#### 2026-10-08 - Rendering-Free Lookahead for Question-Guided Active Vision

**Authors:** Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi
**Links:** [abs](https://arxiv.org/abs/2610.11039) - [pdf](https://arxiv.org/pdf/2610.11039)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rendering-Free Lookahead for Question-Guided Active Vision
- 作者：Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi
- 出版日期：2026-10-08T00:45:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.11039) / [PDF](https://arxiv.org/pdf/2610.11039)

### 一句话总结
论文提出 Rendering-Free Lookahead（RFL），一种通过预测未来视角“可回答性”来选择相机运动策略的方法，使机器人主动视觉在部署时无需渲染未来视图即可进行视角选择。

### 研究问题
主动机器人视觉需要控制相机以揭示当前视角下隐藏的任务相关信息。例如，要判断盒子里有什么，可能需要抬高相机并向下看。对于依赖视角的问答任务，挑战在于选择能够暴露回答问题所需视觉证据的相机运动。虽然视觉语言模型（VLM）可以解释已观察到的图像，但选择此类运动需要预判未见视角的有用性。

### 核心思路/方法
论文将“有用性”量化为 answerability，即 VLM 对某个视角是否足以回答问题的估计，并提出 RFL，一种通过预测未来 answerability 来对候选相机运动排序的视角选择策略。RFL 将视觉前瞻从部署阶段转移到离线训练阶段。训练时，特权教师使用 3D Gaussian Splatting（3DGS）场景渲染候选未来视角，并使用冻结的 VLM 计算一步和两步 answerability 目标。通过两阶段蒸馏，学生模型学习从问题、近期视觉观察和候选相机运动中预测这些动作价值。部署时，RFL 使用这些预测值选择相机运动，而无需渲染未来视角。

### 主要贡献
- 提出将视角有用性量化为 VLM 的 answerability 估计。
- 提出 RFL，一种无需渲染未来视角即可预测候选相机运动未来 answerability 的视角选择策略。
- 通过两阶段蒸馏，将基于 3DGS 渲染的特权教师前瞻能力迁移到学生模型。
- 在 377 个 E3VS-Bench 测试回合、未见环境中，相比使用相同 VLM 的直接动作基线，RFL 将平均评判分数提升 43%。

### 局限性
摘要未提供足够信息。例如，方法对 3DGS 场景质量的依赖程度、蒸馏训练成本、在真实机器人平台上的泛化能力、失败案例或计算开销等均未在摘要中说明。

### 阅读优先级
高。理由：该论文聚焦于视角依赖问答中的主动视觉与相机控制，结合 VLM、3DGS 和蒸馏训练，问题定义清晰，且在摘要中报告了明确的量化提升；对主动视觉、机器人感知和视觉语言模型交叉方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Active robot vision requires controlling the camera to reveal task-relevant information that is hidden from the current viewpoint. For example, determining what is inside a box may require raising the camera and looking down into it. For viewpoint-dependent question answering, the challenge is to select camera motions that expose the visual evidence needed to answer the question. Although vision-language models (VLMs) can interpret observed images, selecting such motions requires anticipating the usefulness of unseen views. We quantify this usefulness as answerability, a VLM's estimate that a view suffices to answer the question, and present Rendering-Free Lookahead (RFL), a viewpoint-selection policy that ranks candidate camera motions by predicted future answerability. RFL transfers visual lookahead from deployment to offline training. At training, a privileged teacher renders candidate future views in 3D Gaussian Splatting (3DGS) scenes and uses a frozen VLM to compute one- and two-step answerability targets. Through two-stage distillation, a student learns to predict these action values from the question, recent visual observations, and a candidate camera motion. At deployment, RFL uses these predicted values to select camera motions without rendering future views. On 377 E3VS-Bench test episodes in unseen environments, RFL improves the mean judge score by 43\% over a direct-action baseline using the same VLM. These results support learning camera-control policies from privileged visual lookahead for viewpoint-dependent question answering.

</details>

#### 2026-10-07 - PCAsplat: Gaussian Splatting with Local PCA Regularization

**Authors:** Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama, João Paulo Lima, Márcus Lobo, Gordon Wetzstein, Leonidas Guibas, Afonso Paiva, Tiago Novello
**Links:** [abs](https://arxiv.org/abs/2610.11011) - [pdf](https://arxiv.org/pdf/2610.11011)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, NeRF, Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PCAsplat: Gaussian Splatting with Local PCA Regularization
- 作者：Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama, João Paulo Lima, Márcus Lobo, Gordon Wetzstein, Leonidas Guibas, Afonso Paiva, Tiago Novello
- 出版日期：2026-10-07T23:49:39Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.11011) / [PDF](https://arxiv.org/pdf/2610.11011)

### 一句话总结
PCAsplat 提出基于可微局部 PCA 的几何感知正则化框架，通过对高斯中心邻域施加特征值与法向约束，缓解高斯泼溅中因弱梯度导致的漂浮物问题，使高斯更贴合底层表面。

### 研究问题
现有高斯泼溅方法主要依赖基于光栅化的损失进行优化，只对参与采样相机光线的高斯进行监督；被遮挡或对当前视角贡献很小的高斯因此获得很弱甚至没有几何梯度，可能偏离底层表面，产生不希望出现的漂浮物（floaters）。

### 核心思路/方法
- 引入 PCAsplat，一个面向高斯泼溅的几何感知正则化框架，基于可微局部主成分分析（PCA）。
- PCA 正则化器直接作用于高斯中心的邻域，因此可以更新那些对当前训练视角没有贡献的高斯。
- 对 PCA 特征值进行正则化，鼓励高斯移动到 underlying surface，并具有各向同性的切平面覆盖。
- 将每个高斯的法向与 PCA 估计的邻域法向对齐，以强制方向一致性。

### 主要贡献
- 提出基于可微局部 PCA 的几何感知正则化框架 PCAsplat，能够更新当前训练视角之外的高斯。
- 通过正则化 PCA 特征值，促使高斯贴近底层表面并形成各向同性切平面覆盖。
- 通过将高斯法向与 PCA 估计的邻域法向对齐，增强方向一致性。
- 在 DTU、Tanks and Turamples（原文为 Tanks and Temples）和 NeRF Synthetic 上的实验表明，PCAsplat 生成的 splats 更好地近似参考表面样本，并显著减少漂浮物。
- 表面对齐的 splats 支持下游几何处理任务，包括点云分割和直接泊松重建；同时在常规新视角合成和网格提取任务上保持竞争力。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败场景、计算开销、对特定数据分布的敏感性或超参数影响等具体限制。

### 阅读优先级
高。理由：该论文针对高斯泼溅中弱监督高斯的几何漂移与漂浮物问题提出明确的正则化思路，且摘要声称在多个基准上提升表面近似质量、减少漂浮物，并支持点云分割与泊松重建等下游任务，同时在新视角合成和网格提取上保持竞争力；对关注三维重建、神经渲染与几何处理的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian splatting has emerged as a flexible representation for 3D reconstruction from posed images. However, existing methods are optimized primarily using rasterization-based losses, which supervise a splat only when it contributes to sampled camera rays. Gaussians that are occluded or contribute little to the sampled view therefore receive weak or no geometric gradients and may drift away from the underlying surface, producing undesired floaters. We introduce PCAsplat, a geometry-aware regularization framework for Gaussian splatting based on differentiable local principal component analysis (PCA). Our PCA regularizer acts directly on neighborhoods of Gaussian centers and can therefore update Gaussians that do not contribute to the current training view. We regularize the PCA eigenvalues to encourage Gaussians to move to the underlying surface with isotropic tangent-plane coverage. We also align each Gaussian normal with the PCA-estimated neighborhood normal to enforce consistent orientation. Experiments on DTU, Tanks and Temples, and NeRF Synthetic show that the splats produced by PCAsplat better approximate samples of the reference surface while substantially reducing undesired floaters. These surface-aligned splats enable downstream geometry-processing tasks, including point cloud segmentation, and direct Poisson reconstruction. Additionally, PCAsplat remains competitive under conventional novel view synthesis and mesh extraction tasks. Code will be released.

</details>

#### 2026-10-07 - Sensitivity as an Arbitrary Output Variable for Differentiable Rendering

**Authors:** Linas Beresna, Eugene Fiume
**Links:** [abs](https://arxiv.org/abs/2610.10852) - [pdf](https://arxiv.org/pdf/2610.10852)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sensitivity as an Arbitrary Output Variable for Differentiable Rendering
- 作者：Linas Beresna, Eugene Fiume
- 出版日期：2026-10-07T19:57:43Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.10852

### 一句话总结
论文提出“sensitivity AOV”（敏感性任意输出变量），将可微渲染中目标函数对场景参数的导数组织为可供人类检视、可复用的渲染输出，从而把导数输出提升为与原始图像并列的一等渲染产物。

### 研究问题
可微渲染器能够给出任意标量目标对每个场景参数的导数，但与原始图像不同——经过数十年各类任意输出变量（AOVs）的发展，原始图像已被很好地分解、检视与合成——这些导数目前缺乏既定的表示方式，无法供人类检视。论文关注的问题正是：如何为可微渲染的导数建立可检视的输出表示。

### 核心思路/方法
- 提出 sensitivity AOV：一种携带目标对影响它的场景参数之敏感性的渲染输出。
- 单次反向模式（reverse-mode）遍历即可填充覆盖场景参数层级的敏感性缓冲区，之后可从中读取多种视图，而无需重新求导，这一思路直接类比于延迟着色（deferred shading）。
- 可读取的视图包括：对象粒度与参数类型粒度的图像空间敏感性；从任意检视视角对可自由导航场景的投影；对于空间变化参数，则通过纹理坐标将逐 texel 场携带到表面。
- 将定义目标的固定相机与用于检视结果的自由相机分离。
- 将反向模式归因与其对偶的前向模式进行对照定位。
- 作者强调其目标不是单一算法，而是一个脚手架（scaffolding），用以将导数输出确立为与原始图像并列的一等渲染产物。

### 主要贡献
- 引入 sensitivity AOV，作为可微渲染导数的可检视输出表示。
- 通过单次反向模式遍历填充场景参数层级上的敏感性缓冲区，支持多种视图的读取而非重复求导。
- 给出多种敏感性视图形式：图像空间敏感性（对象与参数类型粒度）、任意检视视角的场景投影、以及经纹理坐标传递到表面的逐 texel 场。
- 分离固定相机（定义目标）与自由相机（检视结果），并将反向模式归因与前向模式对偶进行对照。
- 提出将导数输出建立为与原始图像并列的一等渲染产物的整体框架思路。

### 局限性
摘要未提供足够信息。摘要未报告实验设置、定量结果、方法的具体实现细节、计算开销评估或适用范围的限制。

### 阅读优先级
中。理由：论文提出的 sensitivity AOV 是一个面向可微渲染导数表示与检视的新概念框架，与渲染输出范式（AOV、延迟着色类比）和可微渲染调试/分析相关，具有潜在启发性；但摘要明确表示其目标是“脚手架”而非单一算法，且未提供实验验证信息，因此对追求具体方法或实证结果的读者优先级相对有限。

</details>

<details>
<summary>Abstract</summary>

Differentiable renderers expose the derivative of any scalar objective with respect to every scene parameter, yet unlike the primal image, which decades of arbitrary output variables (AOVs) have taught us to decompose, inspect, and composite, these derivatives have no established representation for human inspection. We introduce the sensitivity AOV, a render output carrying the sensitivity of an objective to the scene parameters that influence it. A single reverse-mode pass populates a sensitivity buffer over the scene's parameter hierarchy, from which many views are read rather than re-differentiated, in direct analogy to deferred shading: image-space sensitivity at object and parameter-type granularity, projections onto a freely navigable scene from any inspection viewpoint, and, for spatially varying parameters, per-texel fields carried to the surface through texture coordinates. We separate the fixed camera that defines the objective from the free camera used to inspect the result, and position reverse-mode attribution against its forward-mode dual. Our aim is not a single algorithm but a scaffolding that establishes derivative outputs as first-class render products alongside the primal image.

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-13 - EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

**Authors:** Yunsong Zhou, Xuekun Jiang, Haiqi Shen, Hangxu Liu, Chaojian Shi, Yujie Liu, Jingyuan Li, Haoran Yang, Jiafei Cao, Dongzhan Zhou, Dong Wang, Yao Mu, Chunhua Shen, Weinan Zhang
**Links:** [abs](https://arxiv.org/abs/2610.18872) - [pdf](https://arxiv.org/pdf/2610.18872)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

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

#### 2026-10-08 - PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies

**Authors:** Yu Liu, Hetian Guo, Tianlv Huang, Ziyi Cai, Wudi Chen, Hantang Wang, Qiutong Liu, Yingzhi Peng, Wei Han, Peijun Tang, Jianan Wang, Zipei Fan, Zhiyuan Zha, Xuan Song
**Links:** [abs](https://arxiv.org/abs/2610.12285) - [pdf](https://arxiv.org/pdf/2610.12285)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies
- 作者：Yu Liu, Hetian Guo, Tianlv Huang, Ziyi Cai, Wudi Chen, Hantang Wang, Qiutong Liu, Yingzhi Peng, Wei Han, Peijun Tang, Jianan Wang, Zipei Fan, Zhiyuan Zha, Xuan Song
- 出版日期：2026-10-08T16:41:11Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.12285

### 一句话总结
PLaW-VLA 通过在预训练的预测导向表征空间中建模任务相关的未来状态，并以结构化因果注意力将预测未来状态与观测历史、任务语义共同用于动作生成，从而提升长程控制与分布偏移下的泛化能力。

### 研究问题
如何让视觉-语言-动作（VLA）策略获得预测性上下文以支持长程控制，关键问题在于：建模何种未来表征，以及如何将未来状态条件化到动作生成过程中。论文指出，其有效性取决于所建模的未来表示形式以及条件化动作生成的方式。

### 核心思路/方法
- 在预训练的预测导向表征空间中建模任务相关的未来状态，以减少对与控制无关的视觉细节的预测需求。
- 基于 Mixture-of-Transformers 架构。
- 通过结构化因果注意力，将动作生成条件化于观测历史、当前任务语义以及预测的未来状态。

### 主要贡献
- 提出 PLaW-VLA，在预测导向表征空间中建模任务相关未来状态，避免低层视觉重建，从而降低未来预测负担。
- 在 RoboTwin Hard Horizon III 上相比反应式策略取得 +11.8 个百分点的提升。
- 在零样本 LIBERO-Plus 上相比重建导向的潜在预测取得 +1.77 个百分点的提升，支持分布偏移下的泛化改善。
- 实现轻量级潜在世界模型，支持并行未来预测，并在可比策略性能下达到约 1/19 的生成式世界-动作建模推理延迟。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集规模、基线细节、消融实验以及失败案例。
- 摘要未提供足够信息说明方法在不同任务类型或真实机器人场景中的适用性边界。
- 摘要未提供足够信息讨论潜在世界模型的训练成本、数据需求或超参数敏感性。

### 阅读优先级
高。理由：该工作聚焦 VLA 策略的长程控制与泛化问题，提出了结合预测性潜在世界建模与结构化条件化动作生成的方法，并在多个基准上报告了明确的性能提升与推理效率优势；对具身智能与机器人操作方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and how it conditions action generation. We introduce PLaW-VLA, which models task-relevant future states in a pretrained prediction-oriented representation space, reducing the need to predict control-irrelevant visual details. Built on a Mixture-of-Transformers architecture, PLaW-VLA conditions action generation on observation history, current task semantics, and predicted future states through structured causal attention. Experiments show a +11.8 percentage-point (pp) gain over reactive policies on RoboTwin Hard Horizon III and a +1.77 pp gain over reconstruction-oriented latent prediction on zero-shot LIBERO-Plus, supporting improved long-horizon control and generalization under distribution shift, respectively. By avoiding low-level visual reconstruction, PLaW-VLA lowers the burden of future prediction, enabling a lightweight latent world model with parallel future prediction and about 1/19 the inference latency of generative world-action modeling at comparable policy performance.

</details>

#### 2026-10-08 - DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception

**Authors:** Jinghua Hou, Zhe Liu, Hengshuang Zhao
**Links:** [abs](https://arxiv.org/abs/2610.12266) - [pdf](https://arxiv.org/pdf/2610.12266)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception
- 作者：Jinghua Hou, Zhe Liu, Hengshuang Zhao
- 出版日期：2026-10-08T16:32:28Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.12266) | [PDF](https://arxiv.org/pdf/2610.12266)

### 一句话总结
论文提出动态向量解码方法 DVD，将 2D/3D 感知输出统一转换为 1D 向量序列并映射为紧凑离散 token，以缓解基于 MLLM 的感知中坐标表示 token 开销大、固定范围量化受限的问题。

### 研究问题
现有基于 MLLM 的感知方法主要依赖两类表示方式：一是基于文本的坐标表示，存在过高的 token 开销；二是固定范围量化，受范围和精度约束，尤其在空间范围无界且定位精度要求高的 3D 场景中问题突出。论文旨在解决这些表示与效率上的限制。

### 核心思路/方法
论文提出名为 DVD 的动态向量解码方法，统一 2D 与 3D 感知任务的表示。具体做法是：首先将多样的感知表示（2D 边界框、2D 掩码、3D 边界框）转换为 1D 向量序列，再映射到高维空间中的紧凑离散 token；随后通过一个轻量级 de-tokenizer，将输出 token 解码回原始 2D 和 3D 感知表示，从而与 MLLM 无缝集成。

### 主要贡献
- 提出动态向量解码方法 DVD，统一 2D 和 3D 感知任务的表示。
- 将 2D 边界框、2D 掩码、3D 边界框转化为 1D 向量序列，并映射为高维空间中的紧凑离散 token。
- 设计轻量级 de-tokenizer，实现输出 token 到原始 2D/3D 感知表示的解码，并与 MLLM 集成。
- 在 RefCOCO 系列、SUN-RGBD、KITTI、Hypersim、nuScenes 等 2D 与 3D 感知基准上进行了实验；摘要称 DVD 在 2D 和 3D 任务上取得更优性能，并显著降低 token 开销和推理延迟。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败场景、适用范围限制、消融实验细节或误差来源。

### 阅读优先级
中。理由：该论文针对 MLLM 感知中的表示效率与 3D 定位精度问题提出统一 2D/3D 的紧凑 token 方案，主题与具身智能、机器人、自动驾驶等应用相关，且摘要声称在多个 2D/3D 基准上同时提升性能并降低 token 开销与推理延迟；但摘要未给出具体实验数值、方法细节和局限分析，需进一步阅读正文才能判断其实际效果与通用性。

</details>

<details>
<summary>Abstract</summary>

Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, which suffers from excessive token overhead, or fixed-range quantization, which suffers from range and precision constraints, especially for 3D domains with unbounded spatial range and high localization accuracy requirements. To address these challenges, we propose a dynamic vector decoding method named DVD, which unifies the representation of 2D and 3D perception tasks. Specifically, we first transform diverse perceptual representation (i.e., 2D bounding boxes, 2D masks, and 3D bounding boxes) into 1D vector sequences, which are then mapped to compact discrete tokens in the high-dimensional space. Then, a lightweight de-tokenizer enables seamless integration with MLLMs by decoding output tokens back to original 2D and 3D perceptual representations. Extensive experiments on 2D and 3D perception benchmarks including RefCOCO series, SUN-RGBD, KITTI, Hypersim, nuScenes demonstrate that DVD achieves superior performance in 2D and 3D tasks and reduces significantly the token overhead and inference latency. DVD provides an efficient and general framework for integrating perception capabilities into MLLMs, overcoming the inherent limitations of existing methods.

</details>

#### 2026-10-08 - LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes

**Authors:** Peijun Xu, Chuansen Nie, Yiyang He, Yinuo Bai, Jingyang Liu, Kuixiang Shao, Yuyang Jiao, Kuanhao Xia, Jiayi Zhu, Zitian Yang, Yanqi Zhang, Tianye Tan, Shuwei Di, Junyi Xu, Jingyi Yu, Jiayuan Gu
**Links:** [abs](https://arxiv.org/abs/2610.12069) - [pdf](https://arxiv.org/pdf/2610.12069)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, embodied AI, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes
- 作者：Peijun Xu, Chuansen Nie, Yiyang He, Yinuo Bai, Jingyang Liu, Kuixiang Shao, Yuyang Jiao, Kuanhao Xia, Jiayi Zhu, Zitian Yang, Yanqi Zhang, Tianye Tan, Shuwei Di, Junyi Xu, Jingyi Yu, Jiayuan Gu
- 出版日期：2026-10-08T14:47:30Z
- 分类：Embodied / Robotics / AR Applications（未提供二级分类）
- 链接：摘要页 https://arxiv.org/abs/2610.12069 ；PDF https://arxiv.org/pdf/2610.12069

### 一句话总结
LIVIN 是一个基于 30 个真实“有人居住”住宅数字孪生构建的空间与具身智能基准，用于评估 3D 检测、3D 重建、导航和移动操作四类任务。

### 研究问题
现实的家庭仿真不仅需要多样环境，还需要保留“被居住”后的物体摆放与空间约束，因为这些因素会影响机器人运动与交互。现有资源往往在规模、真实世界对应性和交互可用性之间取舍，缺少对真实住宅实际布置方式的高保真、可交互复刻。论文即针对这一空白提出 LIVIN。

### 核心思路/方法
- 构建数字孪生：基于 30 个多样化的“有人居住”住宅，保留观测到的房间布局、家具配置和日常物品摆放。
- 构建流程：设计 human-in-the-loop 工作流，包括实例识别、建筑重建、物体生成与放置；每个阶段的中间结果都由人对照原始观测进行审核与修正。
- 评测任务：在 LIVIN 上评估四个任务——3D 检测、3D 重建、导航和 loco-manipulation（移动操作）。

### 主要贡献
- 提出 LIVIN 基准，建立在 30 个真实“有人居住”住宅数字孪生之上，强调保留实际房间布局、家具配置与日常物品。
- 设计并采用包含实例识别、建筑重建、物体生成与放置的人类在环构建流程，并在各阶段引入人工审核修正。
- 在该基准上定义并评估 3D 检测、3D 重建、导航和 loco-manipulation 四类任务。
- 实验评估表明，当前方法在真实住宅中的密集物体摆放、遮挡、有限自由空间和受限交互区域等条件下仍面临挑战。

### 局限性
摘要未提供足够信息。仅摘要可知，当前方法在密集布置、遮挡、有限自由空间和受限交互区域等真实住宅条件下仍受挑战，但未给出具体方法失败模式、数据规模细节、评测指标、基线列表或消融结论。其他潜在局限摘要未提供足够信息。

### 阅读优先级
中。理由：该工作与具身智能、机器人仿真和真实家庭环境中的空间理解相关，且提出了面向“有人居住住宅”的数字孪生基准和多任务评测，问题设定具有明确应用价值；但摘要未提供具体实验数值、基线对比和方法细节，是否值得深入阅读需依赖全文中的数据集规模、评测协议与结果充分性。

</details>

<details>
<summary>Abstract</summary>

Realistic household simulation must capture not only diverse environments but also the lived-in object arrangements and spatial constraints that shape robot motion and interaction. Existing resources often trade off scale, real-world correspondence, and interaction readiness, leaving a gap in faithful, interactive replicas of how real homes are actually arranged. To this end, we introduce LIVIN, a benchmark for spatial and embodied intelligence built on digital twins of 30 diverse lived-in homes. These replicas preserve observed room layouts, furniture configurations, and everyday belongings. To construct them, we design a human-in-the-loop workflow comprising instance recognition, architectural reconstruction, and object generation and placement, with intermediate results reviewed and corrected by humans against the source observations at each stage. We evaluate four tasks in LIVIN: 3D detection, 3D reconstruction, navigation, and loco-manipulation. Our evaluations show that current methods remain challenged by the dense object arrangements, occlusions, limited free space, and constrained interaction regions found in realistic lived-in homes. We hope LIVIN will help advance embodied AI in real-world homes, from spatial understanding to robotic interaction, and ultimately bring embodied intelligence into everyday home environments.

</details>

#### 2026-10-08 - Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception

**Authors:** Feihong Yang, Xiang Long, Jincheng Yu, Jianfei Zhang, Guangjun Ge, Chao Wang, Yu Wang
**Links:** [abs](https://arxiv.org/abs/2610.11591) - [pdf](https://arxiv.org/pdf/2610.11591)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception
- 作者：Feihong Yang, Xiang Long, Jincheng Yu, Jianfei Zhang, Guangjun Ge, Chao Wang, Yu Wang
- 出版日期：2026-10-08T09:42:02Z
- 分类：Embodied / Robotics / AR Applications（primary_category）；secondary_categories 未提供
- 链接：abs: https://arxiv.org/abs/2610.11591；pdf: https://arxiv.org/pdf/2610.11591

### 一句话总结
论文提出 ALONE——一个贝叶斯空间世界模型，用于在感知间歇（共享传感器被其他任务临时占用）条件下，依靠内部空间信念执行导航，并仅在必要时请求新观测。

### 研究问题
机器人导航通常依赖宽覆盖、高频率的感知来降低部分可观测性；但当共享传感器被另一任务临时重定向时，导航相关观测会被中断。论文研究的问题是：在间歇感知条件下，如何从内部空间信念出发行动，并只在执行确实需要新观测时才重新“看”，从而在执行导航观测的间隙把共享传感器释放给其他任务。

### 核心思路/方法
- ALONE 以贝叶斯空间世界模型的形式，用已执行动作传播结构化空间信念，并用选择性获取的观测对其进行校正。
- 通过关于常见几何结构的学习先验，从已有观测历史推断未观测结构。
- 将信念解码为供运动规划模块使用的空间估计，并预测一张可靠性图，表达对该估计准确性的置信度。
- 仅当可靠性不足以致妨碍导航，且新证据应能使相关区域的空间信息更可靠时，ALONE 才请求一次观测；否则继续基于传播后的信念行动。
- 论文以无人机导航为实例化场景，感知形式为间歇的单目相机深度图像。

### 主要贡献
- 提出 ALONE，一个面向间歇感知导航的贝叶斯空间世界模型，将“行动”与“何时观测”解耦：行动基于内部空间信念，观测按需触发。
- 引入可靠性图来显式表达空间估计的置信度，并以此作为是否请求新观测的决策依据。
- 在两类模拟场景族中验证：10 Hz 决策率下闭环成功率分别为 98% 与 97%；在成功试验中，需要新深度观测的决策步数中位比例分别仅为 0.9% 与 1.3%，表明在显著降低观测需求的同时保持高导航成功率。
- 真实世界室内飞行实验进一步验证了间歇深度观测下的导航，10 次试验全部成功。

### 局限性
- 摘要未提供足够信息说明方法在更复杂场景、不同传感器模态或更长时程任务中的泛化能力。
- 摘要未提供足够信息说明可靠性图的标定质量、误触发/漏触发观测的定量分析。
- 摘要未提供足够信息说明与基线方法的对比细节、消融实验以及失败案例。
- 摘要未提供足够信息说明真实实验的规模（仅提及 10 次试验全部成功）、场景复杂度与传感器配置细节。
- 摘要未提供足够信息说明计算开销、实时性约束的具体数值，以及共享传感器被其他任务占用时的调度机制。

### 阅读优先级
高。理由：该论文直接针对“感知间歇/传感器共享”这一在具身机器人与多任务系统中具有实际约束意义的问题，提出了明确的贝叶斯世界模型方案，并在仿真与真实飞行上给出闭环成功率与观测需求比例的量化结果；对关注机器人导航、部分可观测性、主动感知与传感器资源调度的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Robot navigation commonly uses wide-coverage, high-frequency sensing to reduce partial observability; this reliance becomes restrictive when another task temporarily redirects a shared sensor from navigation, interrupting navigation-relevant observations. We study navigation under intermittent perception: acting from an internal spatial belief and looking again only when execution needs a new observation, potentially freeing the shared sensor for other tasks between navigation observations. ALONE, a Bayesian spatial world model, propagates a structured spatial belief using executed actions and corrects it with selectively acquired observations; learned priors over common geometric structures infer unobserved structure from available observation history. It decodes the belief into a spatial estimate for the motion-planning module and predicts a reliability map expressing confidence in the estimate's accuracy. ALONE requests an observation only if insufficient reliability hinders navigation and new evidence should make relevant-region spatial information more reliable; otherwise, it continues acting from the propagated belief. We instantiate ALONE for drone navigation with intermittent single-camera depth images. Across two simulated scene families, it achieves 98% and 97% closed-loop success at a 10 Hz decision rate. Among successful trials, median fractions of decision steps requiring a new depth observation are only 0.9% and 1.3%, respectively, demonstrating high navigation success with substantially reduced observation demand. Real-world indoor flight experiments further validate navigation under intermittent depth observations, with all 10 trials successful.

</details>

#### 2026-10-08 - USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation

**Authors:** Chuanrui Zhang, Zaijia Yang, Duomin Wang, Lu Shi, Daquan Zhou, Ruihua Zhang, Ziwei Wang
**Links:** [abs](https://arxiv.org/abs/2610.11322) - [pdf](https://arxiv.org/pdf/2610.11322)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation
- 作者：Chuanrui Zhang, Zaijia Yang, Duomin Wang, Lu Shi, Daquan Zhou, Ruihua Zhang, Ziwei Wang
- 出版日期：2026-10-08T06:23:24Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.11322 ；PDF: https://arxiv.org/pdf/2610.11322

### 一句话总结
USDCraft 将铰接式 3D 资产的建模形式化为以部分几何证据为基础的程序化建模，由预训练 LLM 编写和修订可执行程序，生成可直接载入 Isaac Sim 的铰接式 USD 资产，无需任务特定训练。

### 研究问题
面向 real-to-sim 机器人操作，几何忠实且具备功能性的铰接式 3D 资产至关重要，因为仿真中训练的策略需要迁移到物理对象上。现有基于网格的方法从带标注的 3D 资产中学习推断铰接关系，但当真实世界物体超出训练分布，或其网格不完整、损坏时，部署仍然困难。论文旨在解决这些局限下的铰接式资产重建问题。

### 核心思路/方法
论文将铰接式资产重建表述为基于部分几何证据的程序化建模，并提出 USDCraft 框架：由预训练 LLM 编写并修订可执行程序，以生成面向仿真的铰接式资产，且不需要任务特定训练。方法包含两项关键机制：
- 源几何分析：将源网格转换为度量化的文本描述，区分已观测表面与未知空间。
- 迭代几何重检查：将每个候选以相同表示重新编码，使差异指向程序编辑，而未观测区域保持开放以待补全。
此外，建模过程还结合视觉反馈与物理创作指导，最终产出带有显式物理属性的铰接式 USD 资产，可无需手动调整载入 Isaac Sim。

### 主要贡献
- 将铰接式资产重建形式化为基于部分几何证据的程序化建模问题。
- 提出 USDCraft 框架，利用预训练 LLM 编写和修订可执行程序，生成仿真就绪的铰接式资产，无需任务特定训练。
- 提出源几何分析，将源网格转为区分已观测表面与未知空间的度量文本描述。
- 提出迭代几何重检查，通过统一表示重编码候选，使差异用于指导程序编辑，并保留未观测区域的补全空间。
- 结合视觉反馈与物理创作指导，生成带显式物理属性、可直接载入 Isaac Sim 的铰接式 USD 资产。
- 摘要称实验在两个基准上取得领先的铰接恢复效果，并验证 USDCraft 在 real-to-sim-to-real 机器人操作中的有效性。

### 局限性
- 具体实验设置、基准名称、对比方法和定量指标：摘要未提供足够信息。
- 方法对源网格质量、部分几何证据完整程度的敏感性与失败情形：摘要未提供足够信息。
- 生成资产在真实机器人操作中的具体任务、成功率和迁移条件：摘要未提供足够信息。
- LLM 程序生成与迭代修订的计算成本、耗时与稳定性：摘要未提供足够信息。
- 视觉反馈与物理创作指导的具体实现方式：摘要未提供足够信息。

### 阅读优先级
高。理由：该论文位于 real-to-sim 机器人操作、铰接式 3D 资产建模与 LLM 程序化生成交叉方向，问题设定明确针对现有网格方法在分布外与网格不完整/损坏时的部署困难，且摘要声称无需任务特定训练即可生成可直接载入 Isaac Sim 的铰接式 USD 资产，并涉及 real-to-sim-to-real 验证；对关注仿真资产生成与机器人操作迁移的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Geometrically faithful and functional articulated 3D assets are essential for real-to-sim robot manipulation, where policies trained in simulation must transfer to physical objects. Recent mesh-based methods learn to infer articulation from annotated 3D assets, but deployment remains challenging when real-world objects fall outside the training distribution or their meshes are incomplete or corrupted. To address these limitations, we formulate articulated asset reconstruction as programmatic modeling grounded in partial geometric evidence and introduce USDCraft, a framework in which a pretrained LLM writes and revises executable programs for simulation-ready articulated assets without task-specific training. We propose source geometry analysis, which converts the source mesh into a metric textual description that distinguishes observed surface from unknown space, and iterative geometric rechecking, which re-encodes each candidate in the same representation so that discrepancies point to program edits while unobserved regions remain open to completion. Visual feedback and physical authoring guidance complete the modeling process, which produces articulated USD assets with explicit physical properties that load into Isaac Sim without manual adjustment. Experiments demonstrate leading articulation recovery on two benchmarks and validate USDCraft's effectiveness for real-to-sim-to-real robot manipulation.

</details>

#### 2026-10-08 - Distributed Relative Localization for Homogeneous Multi-Robot Systems through UWB Ranging and Limited Communications

**Authors:** Zhiqiang Cao, Ran Liu, Billy Pik Lik Lau, Chau Yuen, U-Xuan Tan
**Links:** [abs](https://arxiv.org/abs/2610.11308) - [pdf](https://arxiv.org/pdf/2610.11308)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** pose estimation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Distributed Relative Localization for Homogeneous Multi-Robot Systems through UWB Ranging and Limited Communications
- 作者：Zhiqiang Cao, Ran Liu, Billy Pik Lik Lau, Chau Yuen, U-Xuan Tan
- 出版日期：2026-10-08T06:13:36Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.11308

### 一句话总结
该论文提出一种完全分布式的相对位姿估计方法，融合 LiDAR、UWB 和里程计，使同构多机器人系统中的每个机器人无需外部基础设施即可持续定位队友。

### 研究问题
多机器人应用（如探索、搜索和救援）需要准确可靠的相对定位。基于 LiDAR 的方案虽能高精度定位周围物体，但同构机器人外观相似、缺乏独特识别特征，难以区分。论文旨在解决同构多机器人系统中匿名队友的可靠识别与持续相对定位问题，并尽量减少通信需求。

### 核心思路/方法
论文提出一种完全分布式的相对位姿估计方法，融合 LiDAR、UWB 和里程计测量。具体流程包括：
1. 通过动态跟踪器对 LiDAR 扫描中潜在的匿名队友机器人簇进行跟踪；
2. 使用联合匹配策略从被跟踪的匿名簇中识别队友机器人，确保机器人与簇之间可靠的数据关联；
3. 结合对应的 LiDAR 观测、UWB 测距和里程计测量，使每个机器人精确地定位其他机器人，同时最小化数据交换。
系统仅需通过机载 UWB 交换里程计数据，无需 WiFi 路由器或 mesh 网络等额外通信基础设施。

### 主要贡献
- 提出一种仅依赖 LiDAR、UWB 和里程计、无需外部基础设施的完全分布式相对位姿估计方法。
- 针对同构机器人外观相似导致的识别困难，设计了动态跟踪与联合匹配策略来实现匿名簇与队友机器人的可靠数据关联。
- 在最小化数据交换的前提下实现精确相对定位，仅需通过机载 UWB 交换里程计数据。
- 摘要称通过大量仿真和真实世界实验验证了方法的有效性与可靠性（具体实验设置与指标摘要未提供足够信息）。

### 局限性
- 摘要未提供足够信息说明方法在何种规模、何种环境复杂度或何种机器人数量下的表现。
- 摘要未提供足够信息说明对 LiDAR 视场遮挡、UWB 非视距或多径等具体挑战的处理能力。
- 摘要未提供足够信息说明实时性、计算开销、定位精度指标或与其他方法的定量对比。
- 摘要未提供足够信息说明仿真与真实实验的具体平台、场景和评价标准。

### 阅读优先级
高。理由：该论文聚焦同构多机器人系统在无外部基础设施条件下的分布式相对定位，融合 LiDAR、UWB 与里程计并强调有限通信，问题明确且对搜索救援、探索等机器人应用具有直接相关性；但具体实验细节和定量结果需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Accurate and reliable relative localization is crucial for multi-robot applications like exploration, search, and rescue missions. LiDAR-based solutions offer high accuracy in localizing surrounding objects; however, distinguishing homogeneous robots with similar appearances remains challenging due to the lack of distinctive identification features. In this paper, we propose a fully distributed relative pose estimation approach by integrating LiDAR, UWB, and odometry measurements, allowing each robot to accurately and continuously localize its teammates without external infrastructure. Specifically, potential anonymous teammate robot clusters from LiDAR scans are tracked by a dynamic tracker. We then identify teammate robots from these tracked anonymous clusters using a joint matching strategy, ensuring reliable data association between robots and clusters. Finally, by combining the corresponding LiDAR observations, UWB ranging, and odometry measurements, each robot precisely localizes others while minimizing data exchange. The system requires only odometry data exchange through onboard UWB, eliminating the need for additional communication infrastructure like WiFi routers or mesh networks. Extensive simulation and real-world experiments demonstrate the effectiveness and reliability of the proposed relative localization approach.

</details>

#### 2026-10-08 - SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation

**Authors:** Kyoungin Baik, Youngwoon Lee
**Links:** [abs](https://arxiv.org/abs/2610.11248) - [pdf](https://arxiv.org/pdf/2610.11248)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation
- 作者：Kyoungin Baik, Youngwoon Lee
- 出版日期：2026-10-08T04:52:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.11248) / [PDF](https://arxiv.org/pdf/2610.11248)

### 一句话总结
SimVLA 提出一个完全基于合成仿真数据、无需遥操作的端到端 VLA 训练框架，用于移动操作，并实现零样本仿真到真实世界的迁移。

### 研究问题
面向机器人的 VLA 模型受限于真实世界数据采集的成本与复杂性。虽然仿真提供了可扩展的替代方案，但其在移动操作 sim-to-real VLA 学习中的潜力仍未被充分探索。论文关注的核心问题是：能否仅用仿真数据训练 VLA，并零样本迁移到真实世界的移动操作任务中。

### 核心思路/方法
SimVLA 是一个端到端框架，完全在合成仿真数据上训练 VLA，且不依赖遥操作。其训练分两个阶段：
1. **预训练**：使用两个互补的仿真数据集：
   - **SimAction**：大规模机器人动作数据集，覆盖 35 个多样化移动操作任务，通过组合原子技能生成；
   - **SimVQA**：利用仿真器特权状态提供空间、几何和子任务级别的视觉-语言监督。
2. **后训练**：在 SimAction 与 **SimDeploy** 的混合数据上进行。SimDeploy 是从多种仿真环境中的策略 rollout 收集的数据集。

论文在补货、倒水和清洁等任务上评估 SimVLA，并展示其向真实世界移动操作（包括真实家庭环境）的零样本迁移能力。

### 主要贡献
- 提出 SimVLA，一个完全基于仿真数据、无需遥操作的端到端 VLA 训练框架，面向移动操作。
- 构建并利用两个互补的仿真数据集 SimAction 和 SimVQA 进行预训练，其中 SimVQA 借助特权仿真状态提供空间、几何和子任务级视觉-语言监督。
- 在后训练阶段结合 SimAction 与从多仿真环境策略 rollout 收集的 SimDeploy 数据集。
- 在补货、倒水、清洁等任务上评估，并展示零样本迁移到真实世界移动操作，包括真实家庭环境。
- 报告 SimVLA 优于使用 50 个域内真实世界演示训练的策略，表明仿真可以支持可扩展的 sim-to-real 移动操作，并说明多种互补监督形式对有效利用仿真的价值。

### 局限性
- 摘要未提供足够信息说明 SimVLA 的具体模型架构、参数规模或训练计算资源。
- 摘要未提供足够信息说明真实世界评估的样本量、统计显著性或失败案例。
- 摘要未提供足够信息说明 SimAction、SimVQA、SimDeploy 的具体数据规模、采集细节或任务分布覆盖范围。
- 摘要未提供足够信息说明零样本迁移在真实家庭环境中的具体条件、机器人平台或安全机制。
- 摘要未提供足够信息说明与真实世界演示策略对比时的具体任务、评价指标和实验设置。

### 阅读优先级
**高**。理由：该论文直接针对 VLA 在移动操作中真实数据成本高的问题，提出完全基于仿真、无需遥操作的零样本 sim-to-real 框架，并声称优于使用真实演示训练的策略；主题处于具身智能与机器人学习的关键方向，且摘要给出了明确的任务覆盖与真实环境迁移结果，值得优先阅读以核实方法与实验细节。

</details>

<details>
<summary>Abstract</summary>

Large-scale, diverse datasets have driven the success of LLMs and VLMs. But VLAs for robotics remain limited by the cost and complexity of real-world data collection. While simulation offers a scalable alternative, its potential for sim-to-real VLA learning in mobile manipulation remains largely underexplored. We introduce SimVLA, an end-to-end framework that trains VLAs entirely on synthetic simulation data without teleoperation for mobile manipulation. SimVLA is first pre-trained on two complementary simulation-derived datasets: SimAction, a large-scale robot action dataset spanning 35 diverse mobile manipulation tasks, generated by composing atomic skills, and SimVQA, which leverages privileged simulator state to provide spatial, geometric, and subtask-level visual-language supervision. We further post-train SimVLA on a mixture of SimAction and SimDeploy, a dataset collected from policy rollouts across diverse simulated environments. We evaluate SimVLA on tasks including restocking, pouring, and cleaning, and show zero-shot transfer to real-world mobile manipulation, including real home environments. SimVLA outperforms policies trained on 50 in-domain real-world demonstrations, suggesting that simulation can enable scalable sim-to-real mobile manipulation. We further demonstrate the value of multiple complementary forms of supervision for effectively leveraging simulation in VLA training.

</details>

#### 2026-10-08 - Towards Path-Creative Navigation: Robot Navigation through Embodied Interaction

**Authors:** Haoyu Xi, Siwei Cheng, Xiangyuan Liu, Brenda Li, Wei Zhang
**Links:** [abs](https://arxiv.org/abs/2610.11072) - [pdf](https://arxiv.org/pdf/2610.11072)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Path-Creative Navigation: Robot Navigation through Embodied Interaction
- 作者：Haoyu Xi, Siwei Cheng, Xiangyuan Liu, Brenda Li, Wei Zhang
- 出版日期：2026-10-08T01:30:53Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.11072

### 一句话总结
论文提出“路径创造性导航”（PCN）这一新范式，让机器人在遇到阻碍时通过与环境的具身交互恢复自由空间，并用一个无地图框架解决其中一类任务。

### 研究问题
传统自主导航通常假设环境固定，只在现有自由空间内寻找路径。但实际中，路径可能被铰接结构、可移动物体或行人阻断，因此到达目标可能需要机器人与环境进行适当的具身交互。论文要解决的问题是：机器人如何在杂乱和受限环境中，通过协调移动与具身交互来恢复自由空间并完成导航。

### 核心思路/方法
论文将上述问题形式化为 Path-Creative Navigation（PCN），即机器人通过协调运动与具身交互来恢复自由空间的导航范式，并针对其中一类 PCN 任务提出一个无地图框架。

该框架为视觉-LiDAR-里程计框架，通过统一的导航系统整合局部观测、障碍物几何信息和机器人状态估计，为导航与交互提供稳定的语义和几何信息。

其可通行性感知决策方法利用视觉和 LiDAR 距离信息，判断阻塞是否可操作、是否可以安全绕过，从而使机器人仅在必要时进行交互，并支持推动铰接结构、推动可移动物体、避障和向行人请求让路等行为。

### 主要贡献
- 提出 Path-Creative Navigation（PCN）这一导航范式，强调通过协调移动与具身交互来恢复自由空间。
- 针对一类 PCN 任务提出一个无地图框架，整合视觉、LiDAR 和里程计信息。
- 提出可通行性感知决策方法，利用视觉与 LiDAR 距离信息判断阻塞是否可操作、是否可安全绕过。
- 支持多种具身交互行为，包括推动铰接结构、推动可移动物体、避障和向行人请求让路。
- 设计仿真场景，并在仿真和两个仅靠传统导航无法完成的真实世界任务中评估不同方法，结果表明该框架通过协调导航与交互，在杂乱和受限环境中取得比基线方法更高的任务完成率。

### 局限性
摘要未提供足够信息。摘要未说明框架在更广泛 PCN 任务类别上的适用性、仿真与真实实验的具体规模与指标细节、失败案例、计算开销、安全性边界或对不同机器人与环境的泛化能力。

### 阅读优先级
高。理由：该论文提出新的导航问题设定 PCN，并给出结合视觉、LiDAR、里程计与具身交互的无地图框架，涉及机器人在杂乱受限环境中主动改变可通行空间的能力；摘要同时声称在仿真和两个传统导航无法完成的真实任务上优于基线，若关注机器人导航与具身交互交叉方向，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Autonomous navigation in cluttered and constrained environments typically assumes a fixed environment and searches only for paths within existing free space. However, a route can be blocked by an articulated structure, a movable object, or a pedestrian, and reaching the goal may therefore require appropriate embodied interaction with the environment. This paper formulates Path-Creative Navigation (PCN), a navigation paradigm in which the robot recovers free space by coordinating locomotion and embodied interaction, and addresses one class of PCN tasks with a mapless framework. The vision-LiDAR-odometry framework integrates local observations, obstacle geometry, and robot-state estimates through a unified navigation system, providing stable semantic and geometric information for navigation and interaction. The traversability-aware decision method utilizes visual and LiDAR distance information to determine whether a blockage is actionable and whether it can be safely bypassed, enabling the robot to interact only when necessary while supporting articulated structure pushing, movable object pushing, obstacle avoidance, and pedestrian requests. We design simulation scenarios and evaluate different methods in both simulation and two real-world tasks that cannot be completed by conventional navigation alone without embodied interaction. These results demonstrate that our framework achieves higher task completion than the baseline methods by coordinating navigation and interaction in cluttered and constrained environments. Code is available at:{https://anonymous.4open.science/r/path-creative-navigation/}.

</details>

#### 2026-10-08 - AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding

**Authors:** Tianhui Cai, Xinglong Sun, Chao Fang, Zhenxin Li, Rui Song, Jose M. Alvarez, Yunxiang Mao, Jiaqi Ma, Langechuan Liu
**Links:** [abs](https://arxiv.org/abs/2610.11060) - [pdf](https://arxiv.org/pdf/2610.11060)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding
- 作者：Tianhui Cai, Xinglong Sun, Chao Fang, Zhenxin Li, Rui Song, Jose M. Alvarez, Yunxiang Mao, Jiaqi Ma, Langechuan Liu
- 出版日期：2026-10-08T01:16:38Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：https://arxiv.org/abs/2610.11060 ；PDF：https://arxiv.org/pdf/2610.11060

### 一句话总结
AffordDrive3D 是一个面向自动驾驶的“可负担性 + 几何”世界-动作模型，在统一框架中联合预测未来可行驶区域、碰撞关键区域与未来几何结构，以支持轨迹规划。

### 研究问题
现有 world-action 模型虽已能联合学习未来场景预测与轨迹生成，但多数主要通过 RGB 外观建模未来；部分近期工作引入几何预测以增强空间理解。然而，密集几何只描述整个场景的空间布局，并不指示哪些区域与自车动作最相关。对驾驶而言，模型还需要识别并预判哪里可以安全行驶、哪些区域可能带来碰撞风险。因此，问题在于：如何将“与动作相关的区域”和“未来几何”联合建模，从而为策略同时提供驾驶相关线索及其对应空间结构。

### 核心思路/方法
- 提出 AffordDrive3D，一个同时具备 affordance 感知与几何感知的 world-action 模型。
- 联合学习未来“动作相关区域”和“空间结构”。
- 为捕捉驾驶 affordance 预测所需的场景语义与驾驶上下文，模型构建在 VLM 骨干之上。
- 通过该 VLM 骨干预测可行驶区域和碰撞关键区域，这些区域会直接影响自车运动。
- 未来几何则从 RGB world-model 的 latent 中预测。
- 在 NAVSIM 上报告结果为 91.3 PDMS 与 89.9 EPDMS。

### 主要贡献
- 提出 AffordDrive3D，将 affordance 与几何联合纳入 world-action 建模，面向自动驾驶轨迹规划。
- 明确指出并处理“密集几何不区分动作相关性”的问题，转而显式预测可行驶区域与碰撞关键区域。
- 采用 VLM 骨干捕捉场景语义和驾驶上下文，用于驾驶 affordance 预测。
- 同时从 RGB world-model latent 预测未来几何，使策略获得驾驶相关线索及其空间结构。
- 在 NAVSIM 基准上取得作者所述的最优性能（91.3 PDMS、89.9 EPDMS），用以说明联合建模未来 affordance 与几何对轨迹规划的有效性。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败情形、对 VLM 骨干或特定数据分布的依赖、计算开销、消融实验细节、跨数据集泛化能力，也未提供与基线方法的逐项比较细节。

### 阅读优先级
高。理由：该论文聚焦自动驾驶 world-action 建模中“动作相关区域与几何联合预测”这一明确问题，并在 NAVSIM 上报告了具体量化指标（PDMS、EPDMS），对关注自动驾驶世界模型、轨迹规划与空间理解交叉方向的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

World-action models have recently improved autonomous driving by jointly learning future scene prediction and trajectory generation. Most existing approaches model the future primarily through RGB appearance, and recent works have begun to incorporate geometric prediction to improve spatial understanding. However, dense geometry describes the spatial layout of the entire scene without indicating which parts are most relevant to the ego vehicle's action. For driving, the model must also identify and anticipate where it can safely move and which regions may pose collision risks. Jointly modeling action-relevant regions and future geometry can provide the policy with both driving-relevant cues and their corresponding spatial structure. We therefore propose AffordDrive3D, an affordance- and geometry-aware world-action model that jointly learns future action-relevant regions and spatial structure. In order to capture the scene semantics and driving context needed for driving affordance prediction, we build AffordDrive3D on a VLM backbone to forecast drivable areas and collision-critical regions that directly affect ego motion, while predicting future geometry from RGB world-model latents. On NAVSIM, AffordDrive3D achieves state-of-the-art performance with 91.3 PDMS and 89.9 EPDMS, demonstrating the effectiveness of jointly modeling future affordances and geometry for trajectory planning.

</details>

#### 2026-10-08 - Refine Connections, Close the Gap: A Reliable Enhancement Framework for Driving Scene Topology

**Authors:** Xiaoqi Wang, Dingyi Zhaung, David Paz, Wenbin He, Yucai Bai, Peng Zhou, Rui Zhang, Jinhua Zhao, Liu Ren
**Links:** [abs](https://arxiv.org/abs/2610.11058) - [pdf](https://arxiv.org/pdf/2610.11058)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, driving scene

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Refine Connections, Close the Gap: A Reliable Enhancement Framework for Driving Scene Topology
- 作者：Xiaoqi Wang, Dingyi Zhaung, David Paz, Wenbin He, Yucai Bai, Peng Zhou, Rui Zhang, Jinhua Zhao, Liu Ren
- 出版日期：2026-10-08T01:15:14Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.11058 ；PDF https://arxiv.org/pdf/2610.11058

### 一句话总结
论文提出 TopoEnhance，将驾驶场景拓扑增强形式化为基于去噪的重建过程，以修正不可靠连接、弥合现有方法与理论上限之间的差距，并提升面向决策的离散拓扑图可靠性。

### 研究问题
论文关注自动驾驶中场景拓扑理解，即车道与交通元素之间连通性的建模。摘要指出，现有方法虽能较好检测单个地图元素，但其连通性推理往往未达到理论潜力，相对于给定底层检测所能达到的理论上限存在明显性能差距；同时，传递给下游任务的、可供决策使用的拓扑图常常不可靠。现有方法通常通过对连续拓扑分数做阈值化来导出连通性，但这些分数未必反映真实逻辑连通可能性，导致误报或漏连。此外，现有基准主要评估连续指标，而忽视了决策所需的离散连通性评估。

### 核心思路/方法
论文提出名为 TopoEnhance 的拓扑增强框架，目标是释放现有方法的潜在能力并提高面向决策拓扑的可靠性。其核心方法是将拓扑增强建模为一种基于去噪的重建过程：模型从随机损坏的真实拓扑图中学习恢复结构一致性。通过这一形式化方式，模型能够解决逻辑不一致并纠正不可靠连接，从而生成稳健的离散拓扑图，并使其接近理论最大性能。摘要称该框架灵活且与来源无关，可在无需重新训练的情况下适用于多种先进基线。

### 主要贡献
- 提出 TopoEnhance，一个面向驾驶场景拓扑的增强框架，旨在弥合现有方法与理论上限之间的差距。
- 将拓扑增强形式化为基于去噪的重建过程，使模型从随机损坏的真实图中学习恢复结构一致性，以修正逻辑不一致和不可靠连接。
- 针对现有基准偏重连续指标、忽视离散连通性的问题，引入适配的 Topology Jaccard Similarity（TJS）指标来衡量离散连通性。
- 摘要称，在多种基线上，TopoEnhance 能持续提升连续拓扑指标（TOP score）和以 TJS 衡量的离散连通性；作为灵活、来源无关的框架，无需重新训练即可在多种先进基线上带来显著增益。

### 局限性
摘要未提供足够信息说明方法的具体计算开销、对不同噪声类型或损坏比例的敏感性、TJS 指标的完整定义与适用范围、实验数据集与基线细节，以及失败案例或边界条件。摘要也未提供足够信息说明该方法在真实部署场景中的延迟、泛化性和安全性验证情况。

### 阅读优先级
高。理由：该论文直接针对自动驾驶场景拓扑中“检测尚可但连通性推理不可靠”的关键瓶颈，且提出面向决策的离散拓扑评估指标 TJS，并声称无需重训练即可增强多种先进基线；若摘要所述成立，对路径规划与运动控制相关的下游任务具有较强潜在价值。但由于摘要未给出实验细节与部署验证，实际影响仍需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

In autonomous driving, understanding scene topology - the connectivity between lanes and traffic elements - is critical for safe path planning and motion control. While current methods excel at detecting individual map elements, their connectivity reasoning often falls short of its theoretical potential, leaving a significant performance gap relative to the theoretical upper-bound achievable given the underlying detections. Furthermore, the decision-ready topology graphs passed to downstream tasks often remain unreliable. Current approaches typically derive connectivity by thresholding continuous topology scores; however, these scores often fail to reflect the true logical likelihood of connectivity, resulting in false positives or missing connections. Existing benchmarks further overlook this issue by primarily evaluating continuous metrics, rather than assessing the discrete connectivity required for decision-making. To bridge these gaps, we propose TopoEnhance, a novel topology enhancement framework designed to unlock the latent potential of existing methods and improve the reliability of decision-ready topology. We formulate topology enhancement as a denoising-based reconstruction process, where the model learns to recover structural consistency from stochastically corrupted ground-truth graphs. This formulation enables the model to resolve logical inconsistencies and rectify unreliable connections, producing robust discrete topology graphs that closely approach theoretical maximum performance. Extensive experiments across different baselines show that TopoEnhance consistently improves both continuous topology metrics (TOP score), and discrete connectivity measured by our adapted Topology Jaccard Similarity (TJS) metric. As a flexible, source-agnostic framework, TopoEnhance delivers substantial gains across diverse state-of-the-art baselines without requiring retraining.

</details>

#### 2026-10-07 - Factorized Tactile Representation and Control for Sim-to-Real Manipulation

**Authors:** Siqi Shang, Bianca Aumann, Tye Brady, Joshua Migdal, Taskin Padir
**Links:** [abs](https://arxiv.org/abs/2610.10510) - [pdf](https://arxiv.org/pdf/2610.10510)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Factorized Tactile Representation and Control for Sim-to-Real Manipulation
- 作者：Siqi Shang, Bianca Aumann, Tye Brady, Joshua Migdal, Taskin Padir
- 出版日期：2026-10-07T17:51:52Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.10510 ；PDF https://arxiv.org/pdf/2610.10510

### 一句话总结
该论文提出一种将触觉响应分解为接触几何、力分布与时间接触变化并分别编码和随机化的表征与控制框架，用于提升触觉仿真到真实操作的迁移可靠性。

### 研究问题
摘要指出，触觉 sim-to-real 学习需要弥合仿真接触与特定设备传感器响应之间的差距，同时保留控制所需的信息。论文关注的问题是如何在仿真到真实的触觉操作中，建立可迁移且对控制有用的触觉表征，并能独立评估不同触觉表征的效用与迁移可靠性。

### 核心思路/方法
论文提出“factorized tactile representation and control framework”，将法向力与接触斑块映射为可从传感器读数恢复的有效接触响应。该响应被分离为三部分：接触几何、力分布和时间接触变化，并针对不同表征进行特定编码与随机化。控制方面使用 Tactile Gated Policy，在控制过程中分别保留这些表征，并可在所有掩码配置下运行而无需重新训练。评估包括响应重建、空间对齐、力调节以及仿真和真实世界中的富接触对抗性 peg insertion。摘要称，该方法实现了小于 1 mm 的接触定位、在未见几何上的 1.69 N 力跟踪误差，以及相比未分解响应在真实世界对抗性 peg insertion 上 35% 的提升；不同触觉表征对不同交互有不同益处。

### 主要贡献
- 提出一种分解式触觉表征与控制框架，将有效接触响应分离为接触几何、力分布和时间接触变化。
- 设计 Tactile Gated Policy，在控制中分别保留这些表征，并支持所有掩码配置而无需重新训练。
- 通过响应重建、空间对齐、力调节和富接触对抗性 peg insertion，在仿真与真实世界中评估方法，使不同触觉表征的效用与迁移可靠性可被独立评估。
- 报告了具体结果：小于 1 mm 接触定位、1.69 N 力跟踪误差、真实世界对抗性 peg insertion 相比未分解响应提升 35%。

### 局限性
摘要未提供足够信息。摘要未说明方法在更广泛任务、不同传感器硬件、极端接触条件或计算成本方面的表现，也未提供失败案例、消融实验细节或与更多基线方法的完整比较。

### 阅读优先级
高。理由：该论文直接面向触觉 sim-to-real 操作中的表征迁移与控制问题，提出分解式表征和无需重训练的掩码策略，并在仿真与真实世界中报告了定位、力跟踪和富接触插入任务的具体结果；对关注机器人触觉学习、仿真到真实迁移和富接触操作的研究者有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Tactile sim-to-real learning must bridge simulated contact and device-specific sensor responses while preserving information needed for control. We propose a factorized tactile representation and control framework that maps normal force and contact patch to an effective contact response recoverable from sensor readings. The response is separated into contact geometry, force distribution, and temporal contact change, with representation-specific encoding and randomization. A Tactile Gated Policy preserves these representations separately through control and operates over all mask configurations without retraining. We evaluate the approach through response reconstruction, spatial alignment, force regulation, and contact-rich adversarial peg insertion in simulation and the real world, enabling the utility and transfer reliability of different tactile representations to be assessed independently. The approach achieves <1 mm contact localization, 1.69 N force-tracking error on unseen geometries, and a 35% improvement in real-world adversarial peg insertion over the unfactorized response, with different tactile representations benefiting different interactions.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
