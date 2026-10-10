# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：93
- 分类分布：
  - Neural Scene Representations & Rendering: 32
  - Embodied / Robotics / AR Applications: 27
  - 3D Reconstruction & Multi-view Geometry: 17
  - Geometry Foundation Models: 12
  - Dynamic / 4D Reconstruction: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **几何基础模型（VGGT 系）成为跨任务公共骨干，正从“特征提供者”转向“计算基础设施”。**
   - `PointVGGT` 直接把 VGGT 当作多视图 RGB-D 配准的计算骨干，提出“先基础、后精化”范式，试图绕开“先成对、后全局”的传统流程。
   - `CoCam4D` 用 VGGT 前馈网络生成带不确定性估计的 3D 高斯场景表示，服务纯相机协同感知。
   - `FreeInpaint` 扩展 3D 基础模型处理带掩码多视图输入，同时保留其恢复位姿与几何的原生能力。
   - 三者共同点：基础模型的输出被当作**可复用的几何先验**，下游任务做的是结构化改造（配准精化、不确定性建模、掩码注意力），而非重训几何网络。

2. **“世界模型”分化为两条清晰路线：预测式潜空间建模（面向控制）与生成式动态化（面向渲染）。**
   - 面向控制：`PLaW-VLA` 在预训练预测导向表征空间中建模任务相关未来状态，强调“预测什么表征”和“如何条件化动作生成”，并报告 RoboTwin Hard Horizon III +11.8pp、零样本 LIBERO-Plus +1.77pp。
   - 面向渲染：`OuroWorld` 将静态 3DGS 场景转为可无缝循环的 3D cinemagraph，用 VLM 推断动态、再用傅里叶级数变形场从构造上保证循环性。
   - 二者共享“世界演化可被建模”的信念，但目标函数、评价方式和失败模式完全不同，短期内不太可能收敛到同一技术栈。

3. **3DGS 正从“重建/渲染表示”扩展为“多用途资产层”，出现水印、外观适配、规划、局部视图复用等外围技术。**
   - `FlyMark` 把水印直接写入 3DGS 已发布参数，免训练、免学习解码器。
   - `PAM-ToD` 冻结预训练 3DGS 参数，只学颜色修正以适配不同时段。
   - `2DGS-Planner` 不把单个高斯基元当障碍物，而是通过栅格化读取规划相关几何。
   - `LVS` 用相对位姿引导的 RGB-D 图像复用替代邻近视角重复渲染。
   - 这说明 3DGS 生态开始出现“表示不变、用途分层”的工程化倾向。

4. **机器人/具身方向明显在补“长尾与鲁棒性”短板：不成功交互、间歇感知、退化环境、同构机器人辨识。**
   - `DreamTrue` 针对机器人数据集中不成功交互覆盖不足，提出反事实后训练。
   - `ALONE` 研究感知间歇条件下的导航，用贝叶斯空间信念在“必要时才看”。
   - `GLIO2` 针对退化环境下扫描到地图前端的漂移与不可恢复误差，改为扫描到多扫描的紧耦合联合优化。
   - `Distributed Relative Localization` 解决同构机器人外观相似导致的数据关联困难。
   - 这些论文的问题意识高度一致：**默认理想条件下的方法已较成熟，真正的瓶颈转移到非理想条件。**

5. **真实感与仿真资产的“贴合现实”诉求上升，评测基准与资产生成同步推进。**
   - `LIVIN` 基于 30 个真实“有人居住”住宅数字孪生，保留实际物品摆放与空间约束，用于评测 3D 检测、重建、导航与移动操作。
   - `USDCraft` 用 LLM 写可执行程序，从部分几何证据生成可直接载入 Isaac Sim 的铰接式 USD 资产。
   - 两者都指向同一个缺口：**仿真里“能跑”不等于“像真实家庭/真实物体那样能跑”。**

#### 技术路线观察

**几何基础模型方向**
- 主流做法是“复用大模型骨干 + 任务特定结构化改造”。`PointVGGT` 用基础模型直接恢复度量一致全局位姿，再用精化阶段处理尺度歧义；`CoCam4D` 在此之上显式建模不确定性，并把高斯图元压缩到 35 字节以适配 C-V2X。
- 一个值得注意的分歧是：`PointVGGT` 强调零样本、免训练；`CoCam4D` 则引入贝叶斯框架和紧凑通信表示。前者偏“能力验证”，后者偏“系统落地”。

**3D/4D 重建方向**
- `Slot3R` 和 `FreeInpaint` 代表两种改造思路：前者是免训练、集合关联式记忆改造，主张“位置决定地址，不决定是否融合”；后者是前馈框架扩展，处理无位姿、带掩码输入。
- 两者都触及一个共同难题：**如何在不完美输入（掩码、邻近指针、跨视角不一致）下保留互补证据，而不是过早平均。**
- `OuroWorld` 的 Inconsistency-Robust Periodic 4DGS 也处理类似问题，但目标从重建转向动态化。

**神经场景表示方向**
- 3DGS 相关论文呈现明显的“分层”特征：底层是表示本体（`OuroWorld`、`PAM-ToD`、`FlyMark`），中层是渲染策略（`LVS`），上层是任务接口（`2DGS-Planner`）。
- `Neural Caching of Prefiltered Radiance` 属于更传统的渲染优化路线，面向镜面光照的神经辐射缓存，与 3DGS 生态关联较弱，但同样在解决“实时 + 质量”的权衡。

**机器人/AR 应用方向**
- 方法侧重点从“感知更多”转向“感知更聪明”：`ALONE` 主动决定何时看，`DreamTrue` 主动构造反事实交互，`Distributed Relative Localization` 融合 UWB 解决匿名辨识。
- 系统侧强调分布式、紧耦合、边缘部署：`GLIO2` 的 GPU 并行前端、`Distributed Relative Localization` 的仅机载 UWB 交换。
- AR 相关（`DreamTrue` 分类含 AR Applications）更多体现为对世界模型的物理合理性与动作忠实度的要求，而非直接的头显交互研究。

#### 值得优先阅读的论文

1. **PLaW-VLA** — 若关注具身策略与世界模型的结合，这是今日最直接回答“预测什么未来表征、如何条件化动作”的论文，且有量化对比（RoboTwin、LIBERO-Plus）。优先读它有助于判断预测式潜空间建模是否值得跟进。

2. **DreamTrue** — 反事实后训练是处理机器人数据长尾（不成功交互）的一个具体机制，且配套了人类标注视频数据集。对做机器人世界模型、数据增广或奖励建模的人都高度相关。

3. **PointVGGT** — “foundation-then-refinement”范式如果成立，可能改变多视图配准的默认流程。建议重点看它如何在无成对估计下解决尺度模糊，以及精化阶段的具体设计。

4. **Slot3R** — 免训练改造 Point3R、保持骨干冻结、在 7Scenes 报告 Acc 降低 57.1%–63.1%，这类“小改动大收益”的工作通常复现价值高，适合作为流式 3D 重建的切入点。

5. **LIVIN** — 若关心仿真到现实的评测缺口，这是今日唯一给出完整基准设计的论文。它的 human-in-the-loop 构建流程和四任务设定，可作为后续资产生成或导航研究的评测底座。

#### 可能的研究机会

- **把“预测式世界模型”和“生成式动态化”接起来。** `PLaW-VLA` 在潜空间预测任务相关未来状态，`OuroWorld` 在像素/高斯空间生成动态。能否用 OuroWorld 式的 4D 表示作为 PLaW-VLA 的预测目标，或反过来用 PLaW-VLA 的表征选择原则约束 OuroWorld 的动态多样性

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-10T13:20:03-04:00
**Total number of papers:** 93
**Number of papers added in the latest update:** 33
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

#### 2026-10-07 - Hardware-aware Calibrated Clustered Attention for Efficient Visual Geometric Transformers

**Authors:** Weitian Wang, Shubham Rai, Cecilia De La Parra, Akash Kumar
**Links:** [abs](https://arxiv.org/abs/2610.09274) - [pdf](https://arxiv.org/pdf/2610.09274)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** visual geometry grounded transformer, VGGT, scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hardware-aware Calibrated Clustered Attention for Efficient Visual Geometric Transformers
- 作者：Weitian Wang, Shubham Rai, Cecilia De La Parra, Akash Kumar
- 出版日期：2026-10-07T01:13:49Z
- 分类：Primary: Geometry Foundation Models；Secondary: 未提供
- 链接：摘要页 https://arxiv.org/abs/2610.09274 ；PDF https://arxiv.org/pdf/2610.09274

### 一句话总结
论文提出硬件友好的分块聚类注意力（BC attention），并配合哈希超平面校准与基于阈值的误差补偿，在 GPU 上加速 VGGT 的全局注意力层与整体骨干网络，同时将精度损失控制在较低水平。

### 研究问题
Visual Geometry Grounded Transformer（VGGT）能一次性联合推断相机位姿、深度和稠密几何等关键 3D 属性，但这种联合推断机制需要处理极长序列的全局注意力层，从而造成显著的延迟瓶颈。论文关注的问题是如何在保持可接受精度损失的前提下，加速 VGGT 中这类长序列全局注意力。

### 核心思路/方法
论文提出 blockwise clustered attention（BC attention）来加速 VGGT 的全局注意力层。其关键做法是将聚类限制在硬件友好的邻域块内，从而降低查询聚类的计算开销，并减少片上与片外内存之间昂贵的数据移动，使其能够扩展到长序列并在 GPU 上带来实际延迟改善。此外，论文引入哈希超平面校准方法和基于阈值的误差补偿方法，以高效降低聚类误差，因为聚类误差被认为是当前聚类注意力机制的瓶颈。

### 主要贡献
- 提出 blockwise clustered attention（BC attention），通过将聚类限制在硬件友好的邻域块内，降低查询聚类开销并减少片上/片外内存间的数据移动。
- 使 BC attention 能够扩展到长序列，并在 GPU 上实现实际延迟改进。
- 引入哈希超平面校准方法与基于阈值的误差补偿方法，以高效降低聚类误差。
- 在 GPU 实验中，校准后的 BC attention 对大场景的全局注意力层实现 2.10–2.63× 加速，对整体骨干实现 1.77–2.35× 加速，精度损失可忽略（1%）。
- 在较小性能损失（< 5%）下，校准后的 BC attention 进一步在全局注意力层实现 2.26–2.87× 延迟改进，在骨干实现 1.90–2.55× 改进。

### 局限性
摘要未提供足够信息。摘要未说明所测试的具体 GPU 型号、数据集、基线细节、聚类数量、块大小等实现参数，也未提供精度损失之外的其他失败案例或适用范围限制。

### 阅读优先级
高。理由：该论文针对 VGGT 联合 3D 推断中的长序列全局注意力延迟瓶颈，提出硬件感知的注意力加速方法，并给出明确的 GPU 延迟与精度损失数据；若关注视觉几何 Transformer 的推理效率、长序列注意力或硬件友好优化，摘要显示其具有直接相关性。

</details>

<details>
<summary>Abstract</summary>

The Visual Geometry Grounded Transformer (VGGT) marks a significant leap forward in 3D scene reconstruction, as it is the first model that directly infers all key 3D attributes (camera poses, depths, and dense geometry) jointly in one pass. However, this joint inference mechanism requires global attention layers with extremely long sequences that causes a significant latency bottleneck. In this paper, we propose blockwise clustered attention (BC attention) to accelerate the global attention layers in VGGT. By limiting the clustering within HW-friendly neighborhood blocks, BC attention reduces the computation overhead of query clustering as well as the costly data movement between on- and off-chip memory. This enables BC attention to scale to long sequences and deliver practical latency improvements on GPUs. Moreover, we introduce a hashing hyperplane calibration method and a threshold-based error compensation method to reduce clustering errors efficiently, which is a bottleneck in the current clustered attention mechanism. Overall, our experiments on GPU demonstrate that calibrated BC attention accelerates the global attention layers by 2.10-2.63$\times$ and the whole backbone by 1.77-2.35$\times$ with negligible loss (1%) for large scenes. With a small performance loss (< 5%), calibrated BC attention further achieves a 2.26-2.87$\times$ latency improvement on the global attention layers and a 1.90-2.55$\times$ improvement on the backbone.

</details>

#### 2026-10-06 - DepthWorld: 3D World Model for Robot Manipulation

**Authors:** Jai Bardhan, Josef Sivic, Vladimir Petrik
**Links:** [abs](https://arxiv.org/abs/2610.08780) - [pdf](https://arxiv.org/pdf/2610.08780)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** geometric reasoning, metric depth, stereo depth, robotics, manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DepthWorld: 3D World Model for Robot Manipulation
- 作者：Jai Bardhan, Josef Sivic, Vladimir Petrik
- 出版日期：2026-10-06T17:59:00Z
- 分类：Geometry Foundation Models（主类）；Embodied / Robotics / AR Applications（次类）
- 链接：https://arxiv.org/abs/2610.08780 ；PDF：https://arxiv.org/pdf/2610.08780

### 一句话总结
论文提出用于机器人操作的 3D 世界模型 DepthWorld，通过构建校准的 3D 数据集 DROID-3D，并训练同时预测多视角 RGB 与深度的扩散世界模型，以缓解现有基于 RGB 的视频世界模型缺乏一致 3D 几何的问题。

### 研究问题
摘要指出，世界模型可作为传统机器人模拟器的数据驱动替代方案，用于策略评估、改进和规划；但这些用途都依赖可信的 3D 几何。当前基于视频的世界模型仅用 RGB 训练，生成的 rollout 虽然逐帧看起来正确，却不能组合成一致的 3D 世界。因此，论文关注两个方面的缺口：机器人操作领域的大规模 3D 监督，以及能够吸收这些监督而不破坏强预训练视频先验的架构。

### 核心思路/方法
论文包含数据集构建与模型训练两部分：

1. **校准流程与 DROID-3D**：提出一种校准流程，将学习到的立体深度与联合因子图结合，汇集来自同一物理机器人的所有 episode，以恢复该机器人共享的运动学参数以及每个场景的外参。将该流程应用于 DROID 数据集后，得到 DROID-3D，这是一个校准的 3D 数据集，提供密集度量深度和重新校准的多视角外参；摘要称在 90% 的 episode 上，外部相机达到小于 0.7 px 的重投影误差。

2. **DepthWorld 模型**：基于 Stable Video Diffusion 训练世界模型 DepthWorld，通过空间 latent tiling 联合预测多视角 RGB 和深度，同时保持预训练 VAE 不变。摘要强调，在相同训练预算下，深度监督使 RGB 预测本身相比仅 RGB 的相同基线提升 +1.48 dB PSNR，同时产生可用于下游几何推理的准确度量深度。

### 主要贡献
- 提出一种校准流程，结合学习到的立体深度与联合因子图，汇集同一物理机器人的所有 episode，恢复共享运动学参数和逐场景外参。
- 构建 DROID-3D：在 DROID 数据集上应用上述流程得到的校准 3D 数据集，提供密集度量深度和重新校准的多视角外参，并报告外部相机在 90% episode 上低于 0.7 px 重投影误差。
- 提出 DepthWorld：基于 Stable Video Diffusion 的世界模型，通过空间 latent tiling 联合预测多视角 RGB 与深度，并保持预训练 VAE 不变。
- 报告深度监督在相同训练预算下将 RGB 预测相对仅 RGB 基线提升 +1.48 dB PSNR，同时产出准确度量深度以支持下游几何推理。

### 局限性
摘要未提供足够信息说明以下方面：数据集规模、机器人平台种类、校准流程对失败案例或不同相机配置的鲁棒性、DepthWorld 在真实机器人操作任务中的策略评估/规划效果、推理速度与计算成本、泛化到 DROID 之外数据的能力、以及深度预测误差的定量指标。摘要也未提供消融实验细节、基线选择范围和训练数据具体规模。

### 阅读优先级
高。理由：论文同时涉及机器人操作中的 3D 世界模型、大规模 3D 监督数据集构建与视频扩散模型架构改造，问题定义明确，且摘要给出了可量化的改进结果；对关注几何基础模型、具身智能、机器人策略评估与规划的研究者有直接相关性。

</details>

<details>
<summary>Abstract</summary>

World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look correct frame-by-frame but do not compose into a consistent 3D world. Closing this gap requires progress on two fronts: large-scale 3D supervision for manipulation, and an architecture that can absorb it without disturbing strong pretrained video priors. We introduce a calibration pipeline that combines learned stereo depth with a joint factor graph, pooling all episodes collected from the same physical robot to recover its shared kinematic parameters alongside per-scene extrinsics. Applied to the DROID dataset, this yields DROID-3D, a calibrated 3D dataset providing dense metric depth and recalibrated multi-view extrinsics (achieving <0.7 px reprojection error on 90% of episodes for external cameras). We then train DepthWorld, a Stable Video Diffusion-based world model that jointly predicts multi-view RGB and depth via spatial latent tiling, leaving the pretrained Variational Autoencoder (VAE) unchanged. Depth supervision improves RGB prediction itself by +1.48 dB PSNR over an identical RGB-only baseline at equal training budget, while simultaneously yielding accurate metric depth for downstream geometric reasoning.

</details>

#### 2026-10-06 - M3SunAgent: Monocular 3D Spatial Understanding Agent for Metric Depth Estimation and 3D Visual Grounding

**Authors:** Jinsong Zhang, Kejun Wu, Ming Zhu, Renjie Qiao, Chengtao Cai, Zhengguo Li
**Links:** [abs](https://arxiv.org/abs/2610.07982) - [pdf](https://arxiv.org/pdf/2610.07982)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：M3SunAgent: Monocular 3D Spatial Understanding Agent for Metric Depth Estimation and 3D Visual Grounding
- 作者：Jinsong Zhang, Kejun Wu, Ming Zhu, Renjie Qiao, Chengtao Cai, Zhengguo Li
- 出版日期：2026-10-06T08:45:25Z
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（次分类）
- 链接：[摘要](https://arxiv.org/abs/2610.07982) / [PDF](https://arxiv.org/pdf/2610.07982)

### 一句话总结
本文提出统一的单目 3D 空间理解智能体 M3SunAgent，以 LLM 作为任务规划器协调多种工具，将实例级度量深度估计与单目 3D 视觉定位整合到同一框架中，并构建了对应的评测基准 M3SI。

### 研究问题
单目度量深度估计与 3D 视觉定位被视为单目 3D 空间理解（M3Sun）的两个互补基石，可为具身智能系统提供基础 3D 空间信息。但摘要指出，这两类互补任务通常由分离的框架分别完成，导致空间信息获取不灵活、不对齐，难以满足具身智能系统的需求。

### 核心思路/方法
- 提出统一的单目 3D 空间理解智能体 M3SunAgent，利用大语言模型（LLM）作为任务规划器进行空间视觉编程，灵活生成结构化程序并协调调用工具。
- 面向实例级度量深度估计：M3SunAgent 调用目标检测工具定位目标，使用深度估计工具在选定点上估计深度，并将这些预测聚合为实例级深度估计。
- 面向单目 3D 视觉定位：M3SunAgent 使用视觉语言模型（VLM）工具定位目标并输出基础空间属性，再结合反投影工具与维度提升工具预测其 3D 边界框。
- 构建 M3Sun Instance（M3SI）数据集，包含 2,910 个样本，用于评测。

### 主要贡献
- 提出统一的 M3SunAgent，以 LLM 作为任务规划器协调工具，缓解两个互补任务由分离框架处理所带来的空间信息不灵活与不对齐问题。
- 给出针对实例级度量深度估计与单目 3D 视觉定位的工具调用与程序化流程设计。
- 构建 M3SI 基准数据集，包含 2,910 个样本。
- 实验结果显示：在实例级单目度量深度估计评测中，M3SunAgent 在所有对比模型中表现最佳，52.61% 的预测实例深度误差低于 0.25（δ < 0.25）；在单目 3D 视觉定位评测中，取得 41.73% 的 3D mIoU，超过当时最优的 MonoVLM 模型 3.62%。

### 局限性
摘要未提供足够信息。摘要未说明 M3SunAgent 的具体失败情形、计算开销、对工具质量的依赖程度、M3SI 数据集的构成细节与泛化性验证等，因此无法基于现有信息分析其局限性。

### 阅读优先级
高。理由：该论文将单目度量深度估计与 3D 视觉定位统一到一个 LLM 驱动的智能体框架中，并给出定量提升与新建基准，对关注具身智能、单目 3D 空间理解、LLM 工具编排与视觉编程的研究方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular metric depth estimation and 3D visual grounding represent the two complementary cornerstones of monocular 3D spatial understanding (M3Sun), from which the fundamental 3D spatial information required by M3Sun can be acquired. However, these complementary tasks are generally conducted by separate frameworks, which pose challenges of inflexible and unaligned spatial information access for embodied intelligence systems. In this paper, we propose a unified agent for monocular 3D spatial understanding (M3SunAgent) that leverages a large language model (LLM) as a task planner for spatial visual programming, which flexibly generate structured programs and coordinate tools. For instance-level metric depth estimation task, M3SunAgent invokes an object detector tool to locate the target, estimates depth at selected points with a depth estimation tool, and aggregates these predictions into an instance-level depth estimate. We also construct the M3Sun Instance (M3SI) dataset, a benchmark with 2,910 samples for evaluation. For monocular 3D visual grounding task, M3SunAgent uses a vision-language model (VLM) tool to locate the target and output basic spatial attributes, then combines back-projection tool with a dimension-lifting tool to predict its 3D bounding box. Experimental results demonstrate the superior performance of M3SunAgent. Specifically, in evaluations of instance-level monocular metric depth estimation, M3SunAgent achieves the best performance among all compared models, 52.61% of predicted instances are distributed below depth error 0.25 ($δ< 0.25$). In evaluations of monocular 3D visual grounding, M3SunAgent demonstrates overall competitive performance than vision and VLM models, reaching a 3D mean intersection over union (mIoU) of 41.73% and exceeding the state-of-the-art MonoVLM model by 3.62%.

</details>

#### 2026-10-06 - Revar3r: gauge-aware perturbation uncertainty for feed-forward 3d reconstruction

**Authors:** Sammam Mahdi, Fariha Binta Salim, Rakin Bin Rabbani, Aniqua Nusrat Zereen
**Links:** [abs](https://arxiv.org/abs/2610.07883) - [pdf](https://arxiv.org/pdf/2610.07883)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** VGGT, MASt3R, feed-forward 3D reconstruction, 3D reconstruction, novel view synthesis, view synthesis, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Revar3r: gauge-aware perturbation uncertainty for feed-forward 3d reconstruction
- 作者：Sammam Mahdi, Fariha Binta Salim, Rakin Bin Rabbani, Aniqua Nusrat Zereen
- 出版日期：2026-10-06T07:29:54Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry、Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.07883 ；PDF https://arxiv.org/pdf/2610.07883

### 一句话总结
ReVar3R 针对前馈 3D 重建中的无训练扰动不确定性，提出在计算逐点方差前先把预测稳健配准到统一相似变换框架，以消除由对称性/规范（gauge）引起的伪不确定性，并在多个骨干与数据集上评估其对 AUSE 等指标的影响。

### 研究问题
论文关注前馈 3D 重建中“无训练扰动不确定性”的缺陷：当输出包含未被观察到的对称性时，多次运行之间的变化可能反映对称性（输出帧的旋转/规范差异），而不是真实误差。对于 point maps，摘要指出会导出一个闭式、与误差无关的方差项，该项随场景范围增长并可能淹没所需信号。因此问题是如何在不重训练、不修改冻结模型的前提下，获得更可靠的不确定性估计。

### 核心思路/方法
- 核心观察：一个正确重建的远距离点，即使冻结的 3D 模型处理等价输入，也可能因输出帧发生微小旋转而显得不确定。
- 诊断：对 point maps 推导出闭式、与误差无关的方差项，随场景范围增长，并预测其具有 $\|x_p\|^2$ 特征；模拟复现该效应，30 个真实 VGGT view-sets 均表现出该预测特征。
- 方法：ReVar3R 在计算逐点方差前，将预测稳健配准到共同相似框架；无需重训练或修改冻结模型。
- 可选步骤：使用留出划分进行校准与融合。
- 评估：在 VGGT、π3、MASt3R 三个骨干与六个数据集上，使用同一估计器比较 AUSE 与内置置信度，并分阶段评估无标签核心、无标签等权融合、留出权重融合以及加入内置信号后的表现；同时与训练过的 evidence head 比较。

### 主要贡献
- 指出无训练扰动不确定性在存在未观察对称性时可能测量的是规范/对称性变化而非误差。
- 对 point maps 推导并验证一个与误差无关、随场景范围增长的方差项，具有 $\|x_p\|^2$ 特征。
- 提出 ReVar3R：一种 gauge-aware 的稳健相似框架配准方法，用于计算逐点方差，无需重训练或修改冻结模型。
- 在 VGGT、π3、MASt3R 与六个数据集上评估，报告同一估计器在 18 个条件中的 15 个将 AUSE 降至内置置信度以下。
- 分阶段评估结果：无标签核心 11/18 胜，无标签等权融合 12/18，留出权重 14/18，加入内置信号 15/18。
- 与训练过的 evidence head 形成权衡：后者在幅度校准更好且在其训练域领先，而 ReVar3R 可跨骨干迁移而无需适配。
- 其排序改进点过滤，但不能检测稳定的系统偏差、不能帮助新视角合成、也不能跨域迁移校准。

### 局限性
- 摘要明确说明：不能检测稳定的系统偏差。
- 摘要明确说明：不 aid novel-view synthesis（不能帮助新视角合成）。
- 摘要明确说明：不能跨域迁移校准。
- 与训练过的 evidence head 相比，后者在幅度校准上更好并在其训练域领先。
- 其他潜在局限、实验细节、失败案例、计算开销、超参数敏感性等：摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接挑战前馈 3D 重建中无训练不确定性估计的一个基础问题（gauge/对称性导致伪方差），给出可诊断的闭式项与无需重训练的配准方法，并在多个主流骨干与数据集上报告了较系统的 AUSE 对比和分阶段增益；对关注 3D 基础模型不确定性、点图置信度与点过滤的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

A correctly reconstructed distant point appears uncertain even when a frozen 3D model processes equivalent inputs because its output frame rotates fractionally. This exposes a weakness of trainingfree perturbation uncertainty: when outputs contain an unobserved symmetry, run-to-run variation potentially reflects symmetry rather than error. Existing alternatives have trade-offs: built-in confidence is outperformed in most evaluated conditions, while trained evidential heads require modelspecific supervision. For point maps, this research derives a closed-form, error-independent variance term that grows with scene extent and potentially overwhelms the desired signal. Simulation reproduces the effect; all 30 real VGGT view-sets tested exhibit its predicted $\|x_p\|^2$ signature. ReVar3R robustly registers predictions to a common similarity frame before computing per-point variance, without retraining or modifying the frozen model. Optional calibration and fusion use a held-out split. Across VGGT, π3, and MASt3R on six datasets, the same estimator on every backbone lowers AUSE below built-in confidence in 15 of 18 conditions. The staged evaluation yields 11 of 18 wins for the label-free core, 12/18 for label-free equal-weight fusion, 14/18 with held-out weights, and 15/18 when the built-in signal is included. Against a trained evidential head, the result is a trade-off: the head calibrates magnitude better and leads in its training domain, whereas ReVar3R transfers across backbones without adaptation. Its ranking improves point filtering, but it does not detect stable systematic bias, aid novel-view synthesis, or transfer calibration across domains.

</details>

#### 2026-10-05 - VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges

**Authors:** Sungjae Choi, Hanna Bae, Sunghyun Baek, Junmo Kim
**Links:** [abs](https://arxiv.org/abs/2610.06594) - [pdf](https://arxiv.org/pdf/2610.06594)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges
- 作者：Sungjae Choi, Hanna Bae, Sunghyun Baek, Junmo Kim
- 出版日期：2026-10-05T16:07:04Z
- 分类：Geometry Foundation Models
- 链接：[摘要](https://arxiv.org/abs/2610.06594) / [PDF](https://arxiv.org/pdf/2610.06594)

### 一句话总结
VGGT-Bridge 通过在分块对齐框架中引入跨越远距离分块的长程“跳边”约束，在不重新训练的前提下缓解逐帧误差沿序列累积造成的漂移，并在多个里程计数据集上降低 ATE。

### 研究问题
前馈式视觉几何 Transformer（如 VGGT）能从图像集合中一次性重建稠密 3D 结构，但其注意力复杂度为二次型，难以扩展到数千帧的长序列。分块对齐框架通过将长序列切分为有重叠的分块，并把各分块局部重建拼接成位姿图来应对该问题；然而，现有方法只连接序列上相邻的分块，导致逐帧的小误差沿链条累积成大规模漂移。

### 核心思路/方法
论文提出 VGGT-Bridge，在相邻分块的顺序边之外，增加长程跳边，直接约束非相邻分块，且无需重新训练。具体做法是：在稀疏采样的粗分块上运行 VGGT，让每个粗分块把相距较远的细分块桥接成单一直接约束。作者还将 VGGT 的首帧尺度偏置转化为漂移校正：以反向顺序输入选定的粗分块；并采用一种回路感知策略，使该反向操作与已有的回路闭合保持兼容。

### 主要贡献
- 提出 VGGT-Bridge，用长程跳边突破仅依赖顺序相邻分块的位姿图结构，直接约束非相邻分块，且不需要重新训练。
- 通过稀疏粗分块运行 VGGT，将远距离细分块桥接为直接约束。
- 将 VGGT 的首帧尺度偏置转化为漂移校正，并通过回路感知策略保持与已有回路闭合的兼容性。
- 在 KITTI Odometry、Virtual KITTI 和 Waymo Open 上，相较于 SwiftVGGT 基线分别降低 ATE 28.3%、18.8% 和 10.0%，在所有分块对齐方法中取得最佳性能。

### 局限性
摘要未提供足够信息。摘要未说明方法对粗分块采样策略的敏感性、反向输入带来的额外计算或工程代价、在不同序列长度或不同重叠比例下的表现，也未提供失败案例或与所有已有方法的完整对比细节。

### 阅读优先级
高。理由：该工作针对前馈视觉几何模型在长序列重建中的可扩展性与漂移累积问题，提出无需重训练的长程约束机制，并在多个自动驾驶里程计数据集上报告了明确且一致的 ATE 改进，属于“Geometry Foundation Models”方向中兼顾方法简洁性与实证效果的研究，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward visual geometry transformers such as VGGT reconstruct dense 3D structure from images in a single forward pass, simplifying multi-view 3D reconstruction. However, their quadratic attention complexity makes them difficult to scale to long sequences with thousands of frames. Chunk-and-align frameworks address this by splitting a long sequence into overlapping chunks and stitching their local reconstructions into a pose graph. Yet existing methods connect only sequentially adjacent chunks, so small per-frame errors accumulate along the chain into large-scale drift. To move beyond sequential edges, we propose VGGT-Bridge, which adds long-range skip edges that directly constrain non-adjacent chunks without retraining. By running VGGT on sparsely sampled coarse chunks, each coarse chunk bridges distant fine chunks into a single direct constraint. We further turn VGGT's first-frame scale bias into a drift correction by feeding selected coarse chunks in reverse, and a loop-aware policy keeps this reversal compatible with existing loop closures. VGGT-Bridge reduces ATE by 28.3% on KITTI Odometry, 18.8% on Virtual KITTI, and 10.0% on Waymo Open over the SwiftVGGT baseline, achieving the best performance among all chunk-and-align methods.

</details>

#### 2026-10-05 - MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs

**Authors:** Yun Jiang, Bo Zheng, Yingying Zhang, Xueming Xiao, Tao Hu, Hutao Cui, Zhiguo Meng, Ke Gao, Yang Gao, Meibao Yao
**Links:** [abs](https://arxiv.org/abs/2610.07110) - [pdf](https://arxiv.org/pdf/2610.07110)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, 3D reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs
- 作者：Yun Jiang, Bo Zheng, Yingying Zhang, Xueming Xiao, Tao Hu, Hutao Cui, Zhiguo Meng, Ke Gao, Yang Gao, Meibao Yao
- 出版日期：2026-10-05T15:46:50Z
- 分类：Geometry Foundation Models（主）；Neural Scene Representations & Rendering（次）
- 链接：https://arxiv.org/abs/2610.07110 ；PDF: https://arxiv.org/pdf/2610.07110

### 一句话总结
MoonGS 是首个面向月球场景的前馈式 3D 高斯泼溅框架，仅用两张输入图像即可单次前向预测像素对齐的高斯基元，在稀疏、弱纹理的月球数据上实现无需逐场景优化的高质量新视角渲染。

### 研究问题
从稀疏的巡视器图像中进行高质量月球地形三维重建，对自主月球探测至关重要，但面临三个挑战：视点重叠不足、表面纹理弱、数据量有限。摘要指出该问题在现有条件下仍具挑战性，MoonGS 正是针对这些困难提出。

### 核心思路/方法
- 任务设定：仅输入两张图像，单次前向预测像素对齐的高斯基元，直接渲染逼真的新视角，无需任何逐场景优化。
- 骨干设计：采用可适配的骨干结构，无缝集成先进视觉基础模型以提取鲁棒的深度特征。
- 语义先验：以两种方式引入语义先验——将语义线索与视觉特征融合以精化高斯参数估计；采用语义排序损失对背景深度进行正则化。
- 稀疏观测增强：采用熵引导的启发式重采样策略，以可忽略的开销选择最具信息量的远距离视点来扩充稀疏观测。
- 评测：在 LuSNAR 基准与自建合成弱纹理数据集 MoonBlender 上验证，并展示可有效利用包括 VGGT 在内的先进骨干以显著提升性能；在嫦娥任务影像上做定性评估。

### 主要贡献
- 提出 MoonGS，摘要称为首个面向月球场景的前馈式 3D 高斯泼溅框架，仅凭两张图像即可实现无需逐场景优化的逼真新视角渲染。
- 设计可适配骨干以集成先进视觉基础模型，提取鲁棒深度特征。
- 以融合语义线索精化高斯参数、并以语义排序损失正则化背景深度两种方式引入语义先验。
- 提出熵引导的启发式重采样策略，以极低开销选取信息量最大的远距离视点来增强稀疏观测。
- 实验显示在 LuSNAR 基准与 MoonBlender 数据集上超越前馈式 NeRF/3DGS 基线：PSNR +4.9 dB、SSIM +0.29、LPIPS 降低 40%，并保持亚秒级推理；同时验证框架可有效利用包括 VGGT 在内的先进骨干提升性能，并在嫦娥任务影像上取得对比方法中最佳的视觉质量，表明对真实月球数据的鲁棒性。
- 摘要声明源代码与数据集已公开于 https://github.com/InRobots/MoonBlender 。

### 局限性
- 摘要未提供足够信息说明方法在何种失败场景下失效，或对极端光照、更大规模场景、更多输入图像时的表现。
- 摘要未提供足够信息说明计算资源、显存占用、训练数据规模与训练时长等细节。
- 摘要未提供足够信息说明定量实验的具体基准划分、对比方法清单与消融实验细节。
- 摘要未提供足够信息说明在真实嫦娥影像上是否仅做定性评估、是否存在定量真实数据结果。
- 摘要未提供足够信息说明“亚秒级推理”所对应的硬件平台与输入分辨率。

### 阅读优先级
高。理由：该工作针对月球探测这一明确且困难的应用场景，提出前馈式 3DGS 新框架，报告了相对前馈式 NeRF/3DGS 基线的显著定量提升（PSNR +4.9 dB、SSIM +0.29、LPIPS 降低 40%）并保持亚秒级推理，同时涉及视觉基础模型集成、语义先验与稀疏观测增强等可迁移方法要素，且声明代码与数据集公开，对三维重建、机器人感知与行星探测交叉方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

High-quality 3D reconstruction of lunar terrain from sparse rover images is indispensable for autonomous lunar exploration, but remains challenging because viewpoint overlap is insufficient, surface textures are weak, and data volume is limited. We propose MoonGS, the first feed-forward 3D Gaussian Splatting framework tailored to lunar scenes. Given only two input images, MoonGS predicts pixel-aligned Gaussian primitives in a single forward pass and renders photorealistic novel views without any per-scene optimization. MoonGS (i) adopts an adaptable backbone design that seamlessly integrates advanced vision foundation models to extract robust depth features; (ii) integrates semantic priors in two manners: merging semantic cues with visual features to refine Gaussian parameter estimation, and adopting a semantic ranking loss that regularizes background depth; and (iii) employs an entropy-guided heuristic resampling strategy to augment sparse observations by selecting the most informative distant viewpoints with negligible overhead. Experiments on the LuSNAR benchmark and our synthetic weak-texture MoonBlender dataset show that MoonGS surpasses state-of-the-art feed-forward NeRF/3DGS baselines by +4.9 dB PSNR, +0.29 SSIM, and 40\% lower LPIPS while maintaining sub-second inference. Furthermore, we validate the broad applicability of our framework by demonstrating that it effectively leverages state-of-the-art backbones, including VGGT, to significantly boost performance. Qualitative evaluations on Chang'e mission imagery also show the best visual quality among compared methods, indicating robustness on real lunar data. The source code and dataset are publicly available at https://github.com/InRobots/MoonBlender.

</details>

#### 2026-10-04 - Deep Prior Learning for Embodied Perception

**Authors:** Yimou Wu, Jiaxin Guo, Yun-hui Liu, Zheng Li
**Links:** [abs](https://arxiv.org/abs/2610.05531) - [pdf](https://arxiv.org/pdf/2610.05531)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Deep Prior Learning for Embodied Perception
- 作者：Yimou Wu, Jiaxin Guo, Yun-hui Liu, Zheng Li
- 出版日期：2026-10-04T20:53:38Z
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2610.05531

### 一句话总结
论文提出基于 VGGT 的 VPGGT 框架，通过先验残差连接与 Metric Global Attention，在具身感知中更有效地利用带噪相机位姿、内参和深度先验，以缓解先验稀释并恢复物理尺度。

### 研究问题
具身系统需要超越单纯图像的几何感知。现有前馈 3D 模型虽引入相机位姿、内参和深度等几何先验，但处理带噪位姿、保持准确先验以及恢复物理尺度，并不仅仅是直接接受这些输入即可解决。论文关注的核心问题之一是“先验稀释”：预测结果反而不如所提供的位姿先验准确。

### 核心思路/方法
论文提出 Vision-Prior Geometry Grounded Transformer（VPGGT），这是一个基于 VGGT 的框架，并在 OmniVGGT 基础上扩展，用于先验感知的具身感知。方法包括：
- 从真实轨迹出发构造受传感器启发的位姿扰动，用于训练；扰动仅针对相机位姿，提供的相机内参和深度不额外加噪。
- 引入无参数的 prior residual connection（PRC），以缓解 prior dilution。
- 引入 Metric Global Attention，使全局尺度 token 条件化于可用的位姿尺度和深度尺度，并为几何输出预测共享的度量缩放因子。

### 主要贡献
- 提出 VPGGT，一个基于 VGGT 并扩展 OmniVGGT 的先验感知具身感知框架。
- 构造面向相机位姿的传感器启发式扰动训练设定。
- 提出无参数 prior residual connection，用于缓解预测精度低于输入位姿先验的先验稀释问题。
- 提出 Metric Global Attention，用于预测共享度量缩放因子并恢复物理尺度。
- 在四个数据集上的实验表明，当所有视角提供相机先验时，在精确位姿和受扰动位姿下，PRC 相比匹配训练基线提升了平移方向准确率和联合位姿 AUC。

### 局限性
摘要未提供足够信息说明方法在更多模态、更复杂噪声类型或真实部署场景中的表现。摘要未提供足够信息说明推理效率、计算开销、失败案例以及与其他基线方法的完整比较细节。摘要未提供足够信息说明四个数据集的具体构成、评价协议和消融实验完整结果。

### 阅读优先级
中。理由：论文主题集中在具身感知、几何先验利用和前馈 3D 模型扩展，对关注 VGGT/OmniVGGT、位姿先验鲁棒性和度量尺度恢复的研究者具有直接相关性；但摘要仅给出方法框架与部分实验结论，未提供完整实验细节和外部验证信息，因此不适合作为仅凭摘要即可深入复现或全面评估的优先阅读材料。

</details>

<details>
<summary>Abstract</summary>

Embodied systems need geometric perception that exploits available observations beyond images alone. Recent feed-forward 3D models incorporate geometric priors, including camera poses, intrinsics, and depth. However, handling noisy poses, preserving accurate priors, and recovering physical scale require more than simply accepting these inputs. We introduce \emph{Vision-Prior Geometry Grounded Transformer} (VPGGT), a VGGT-based framework that extends OmniVGGT for prior-aware embodied perception. We formulate sensor-motivated pose corruptions from ground-truth trajectories for training and introduce a parameter-free \emph{prior residual connection} (PRC) to mitigate \emph{prior dilution}, where predictions are less accurate than their supplied pose priors. Our noise formulation targets camera poses; supplied intrinsics and depth receive no additional corruption. We further introduce \emph{Metric Global Attention}, which conditions a global scale token on available pose and depth scales and predicts a shared metric scaling factor for the geometric outputs. Experiments across four datasets show that \emph{PRC} improves translation-direction accuracy and joint pose AUC over a matched training baseline when camera priors are provided for all views, under both exact and corrupted poses. These results support explicit prior access during refinement as a useful addition to feature-level conditioning.

</details>

## Dynamic / 4D Reconstruction

### 2026-10

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

#### 2026-10-07 - DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video

**Authors:** Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang
**Links:** [abs](https://arxiv.org/abs/2610.09720) - [pdf](https://arxiv.org/pdf/2610.09720)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic reconstruction, dynamic 4D, 4D Gaussian, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video
- 作者：Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang
- 出版日期：2026-10-07T09:15:02Z
- 分类：Dynamic / 4D Reconstruction（主）；Neural Scene Representations & Rendering（次）
- 链接：https://arxiv.org/abs/2610.09720 ；PDF: https://arxiv.org/pdf/2610.09720

### 一句话总结
DynStream 面向长时、无位姿视频流，提出在局部时间窗内重建并增量对齐融合的在线 4D 高斯框架，以同时实现连续处理与高保真渲染。

### 研究问题
从长时、无位姿的流式视频中在线重建动态 4D 场景，需要同时满足连续处理与照片级真实感渲染。摘要指出，现有方法难以同时做到这两点：前馈高斯方法受限于离线处理，而在线的点云方法又难以保持稠密几何和高保真渲染。

### 核心思路/方法
- 输入为连续视频流，在局部时间窗内进行场景重建。
- 将这些局部重建增量式地对齐并融合为全局一致的场景。
- 支持在线 4D 重建，且无需逐场景优化。
- 通过联合强制跨窗口几何一致性与对时变场景内容建模，支持长视频流上的高效重建与照片级渲染。

### 主要贡献
- 提出 DynStream，一个从长时、无位姿视频进行流式 4D 高斯重建的框架。
- 通过局部时间窗重建 + 增量对齐融合，实现在线 4D 重建，避免逐场景优化。
- 联合跨窗口几何一致性与时变场景建模，兼顾效率与高保真渲染。
- 摘要称实验表明其可从长视频流实现高保真在线动态重建与渲染，并在多种动态室内外场景上取得 state-of-the-art 性能。

### 局限性
- 具体的失败场景、边界条件、计算开销、内存占用、实时性指标等：摘要未提供足够信息。
- 摘要仅提及“多种动态室内与室外场景”，未给出数据集名称、评测指标或对比基线细节：摘要未提供足够信息。
- 摘要未说明对无位姿输入的位姿估计误差、长时漂移等问题的具体处理效果与限制：摘要未提供足够信息。

### 阅读优先级
高。理由：该论文聚焦长时无位姿视频的在线 4D 重建这一兼具连续处理与高保真渲染的挑战性问题，且摘要声称在动态室内外场景上达到 state-of-the-art，与动态/4D 重建及神经场景表示与渲染方向高度相关；但若关注具体实验设置与工程可行性，需进一步查阅原文，因为摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Online reconstruction of dynamic 4D scenes from long, unposed streaming videos requires both continuous processing and photorealistic rendering, which existing methods struggle to achieve simultaneously. Existing feed-forward Gaussian methods are restricted to offline processing, whereas online point-cloud approaches struggle to maintain dense geometry and high-fidelity rendering. We present DynStream, a framework for streaming 4D Gaussian reconstruction from long, unposed videos. Given a continuous video stream, DynStream reconstructs the scene within local temporal windows and incrementally aligns and fuses these local reconstructions into a globally consistent scene, enabling online 4D reconstruction without per-scene optimization. By jointly enforcing cross-window geometric consistency and modeling time-varying scene content, DynStream supports efficient reconstruction and photorealistic rendering over extended video streams. Experiments demonstrate that DynStream enables high-fidelity online dynamic reconstruction and rendering from long video streams, achieving state-of-the-art performance across diverse dynamic indoor and outdoor scenes.

</details>

#### 2026-10-04 - DynaMesh: Dynamic 3D Texture Generation

**Authors:** Raj Hansini, Guan Chen, Rana Hanocka, Itai Lang
**Links:** [abs](https://arxiv.org/abs/2610.05529) - [pdf](https://arxiv.org/pdf/2610.05529)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D, video-to-4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DynaMesh: Dynamic 3D Texture Generation
- 作者：Raj Hansini, Guan Chen, Rana Hanocka, Itai Lang
- 出版日期：2026-10-04T20:52:25Z
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2610.05529

### 一句话总结
DynaMesh 提出一种在保持三维网格几何不变的前提下，根据文本提示生成随时间演变的动态纹理/外观效果的方法。

### 研究问题
论文关注如何在三维网格上生成“传播式”的视觉动态效果。已有动态三维内容生成工作主要关注几何与位置的运动会改变而外观保持不变；而纹理生成方法则把外观作为固定表面属性绘制到形状上，而非一个演变过程。两者都没有处理视觉效果在三维物体上传播的问题。摘要指出，直接用“视频模型 + 逐帧图像到三维生成”的自然路线会因后者没有时间概念，导致序列闪烁、丢失效果细节，并且每一视频帧都产生不同网格。

### 核心思路/方法
方法以无纹理形状和描述效果的文本提示为输入，输出几何不变、纹理逐帧变化的单一网格。具体做法是：先以网格渲染图和文本提示为条件驱动视频模型，得到参考视频；再对视频运行一个冻结的图像到三维生成器，但做了两处改动：一是每帧的条件在时间窗口上进行混合，二是针对每个形状拟合低秩适配器以恢复丢失的细节。网格在整个序列中只编码一次，因此几何按构造保持恒定，最终输出为单一网格加上每一帧的纹理。

### 主要贡献
- 提出 DynaMesh，一种面向三维网格的动态纹理生成方法，在几何不变的情况下产生随时间演变的外观。
- 针对视频到三维逐帧生成导致的闪烁、细节丢失和网格不一致问题，提出时间窗口条件混合与逐形状低秩适配器两项改动。
- 通过只编码一次网格，使几何恒定成为构造性保证，输出为单一网格与逐帧纹理。
- 摘要称其在多种物体和效果上显著优于近期 video-to-4D 与纹理化方法，并能将时间效果泛化到训练中未见过的不同形状。

### 局限性
摘要未提供足够信息。（论文未在摘要中明确讨论失败情形、计算开销、对提示或视频模型的依赖限制，以及泛化能力的边界等。）

### 阅读优先级
中。理由：该工作处于动态三维内容生成与三维纹理生成的交叉点，问题定义清晰，方法思路具有针对性；但摘要未给出定量结果、实验设置与局限分析，若读者关注动态纹理或 video-to-4D 方向，可优先阅读原文以核实实验细节与泛化表现。

</details>

<details>
<summary>Abstract</summary>

We present DynaMesh, a dynamic texture generation method for 3D meshes. Given a textureless shape and a text prompt describing an effect, our method produces an appearance that evolves while the object's geometry remains unchanged. Previous works on dynamic 3D content generation have focused on motion, where an object's geometry and position change while keeping its appearance the same. Methods on texture generation sit on the other side of the problem, painting appearance onto a shape as a fixed surface property and not as an evolving process. Neither addresses a visual effect that propagates on a 3D object. A natural route consists of two generators: a video model that shows the effect from a single view, and an image-to-3D generator that lifts each frame to 3D. However, the latter has no notion of time, so running it per video frame produces a sequence that flickers, loses effect details, and yields a different mesh at every video frame. Our method addresses these failures by conditioning a video model on a render of the mesh and the prompt to obtain a reference video, then running a frozen image-to-3D generator on the video with two changes. The conditioning of each frame is blended over a temporal window, and low-rank adapters are fit per shape to restore the lost details. The mesh is encoded once for the whole sequence, so geometry is constant by construction, and the output is a single mesh with a texture per frame. Applied to various objects and effects, DynaMesh substantially improves over recent video-to-4D and texturing methods, and can generalize its temporal effect to different shapes never seen during training. Our project page is at https://threedle.github.io/dynamesh/.

</details>

#### 2026-10-04 - Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting

**Authors:** Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu
**Links:** [abs](https://arxiv.org/abs/2610.05289) - [pdf](https://arxiv.org/pdf/2610.05289)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting
- 作者：Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu
- 出版日期：2026-10-04T15:07:47Z
- 分类：主分类为 Dynamic / 4D Reconstruction；次分类为 Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2610.05289；PDF 链接 https://arxiv.org/pdf/2610.05289；代码链接 https://xiaobiaodu.github.io/mobile-4dgs-project/

### 一句话总结
Mobile-4DGS 提出一个面向移动端的统一轻量框架，用于静态与动态高斯表示的实时渲染，通过压缩外观、精简高斯基元以及显式紧凑 4D 表示来降低存储与逐帧计算开销。

### 研究问题
论文关注的问题是：尽管 3D Gaussian Splatting（3DGS）在新视角合成上表现突出，但将静态和动态高斯表示部署到资源受限的移动设备上仍然困难，主要原因包括存储负担重、高斯基元冗余以及逐帧计算代价高。

### 核心思路/方法
论文提出 Mobile-4DGS，一个统一的轻量框架，目标是在移动平台上实现高保真实时的静态与动态高斯渲染。方法层面包括：
- 紧凑外观建模：引入 Monte Carlo Specular Energy Aggregator，将高阶辐射残差压缩到一阶 Spherical Harmonics（SH）；并结合 Attribute-Conditioned SH Enhancement 模块，其预测偏移在推理前预先烘焙。
- 基元精简：提出 Multi-View Alpha-Based Densification and Pruning 策略，在保持多视角一致性的同时抑制冗余高斯基元。
- 动态场景表示：构建紧凑显式 4D 表示，包括二阶高斯运动、可学习时间支撑以及二值静态-动态划分，从而无需运行时变形网络即可进行连续时间建模。
- 播放效率优化：基于静态-动态划分，提出 Depth-Order Certificate，选择性复用此前已提交的深度顺序，以减少播放过程中的重投影、排序、合并与索引缓冲区更新。

### 主要贡献
- 提出统一的轻量框架 Mobile-4DGS，面向移动端静态与动态高斯实时渲染。
- 引入 Monte Carlo Specular Energy Aggregator 与 Attribute-Conditioned SH Enhancement，用于压缩外观表示，并将预测偏移预烘焙以降低推理开销。
- 提出 Multi-View Alpha-Based Densification and Pruning，减少冗余高斯基元并维持多视角一致性。
- 构建紧凑显式 4D 表示，通过二阶高斯运动、可学习时间支撑和二值静态-动态划分，实现无需运行时变形网络的连续时间建模。
- 提出 Depth-Order Certificate，复用已提交深度顺序，以减少动态播放中的重投影、排序、合并与索引缓冲区更新。
- 摘要称在静态与动态场景上的大量实验表明，Mobile-4DGS 显著降低存储和渲染开销，同时保持有竞争力的视觉质量，并支持移动设备上的实时 3D 与 4D 高斯 Splatting。

### 局限性
摘要未提供足够信息。摘要未给出具体实验平台、移动设备型号、帧率、存储压缩比例、视觉质量指标、失败案例或方法适用范围等细节，因此无法基于摘要判断其局限性。

### 阅读优先级
高。理由：该论文聚焦 3DGS 在移动端部署中的存储、冗余基元和逐帧计算瓶颈，并同时覆盖静态与动态高斯表示，属于动态/4D 重建与神经场景表示渲染交叉方向；若关注移动端实时高斯渲染、4D 表示压缩或高效动态场景建模，该工作具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable performance in novel view synthesis, yet deploying both static and dynamic Gaussian representations on resource-constrained mobile devices remains challenging due to heavy storage, redundant primitives, and costly per-frame computation. We present Mobile-4DGS, a unified lightweight framework for high-fidelity real-time static and dynamic Gaussian rendering on mobile platforms. For compact appearance modeling, we introduce a Monte Carlo Specular Energy Aggregator that compresses high-order radiance residuals into the first-order Spherical Harmonics (SH), together with an Attribute-Conditioned SH Enhancement module whose predicted offsets are pre-baked before inference. We further propose a Multi-View Alpha-Based Densification and Pruning strategy to suppress redundant primitives while maintaining multi-view consistency. For dynamic scenes, we develop a compact explicit 4D representation by constructing second-order Gaussian motion, learnable temporal support, and a binary static-dynamic partition, enabling continuous-time modeling without runtime deformation networks. Based on this partition, a Depth-Order Certificate selectively reuses previously committed depth orders to reduce re-projection, sorting, merging, and index-buffer updates during playback. Extensive experiments on static and dynamic scenes demonstrate that Mobile-4DGS substantially reduces storage and rendering overhead while maintaining competitive visual quality, enabling real-time 3D and 4D Gaussian Splatting on mobile devices. \textcolor{magenta}{\href{https://xiaobiaodu.github.io/mobile-4dgs-project/}{Code has been released: https://xiaobiaodu.github.io/mobile-4dgs-project/}}.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

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

#### 2026-10-07 - WAPR: A Foundation Model for Wide-Angle Refinement in Unseen Object Pose Estimation

**Authors:** Yulin Wang, Mengting Hu, Hongli Li, Jianghao Zhou, Chen Luo
**Links:** [abs](https://arxiv.org/abs/2610.09535) - [pdf](https://arxiv.org/pdf/2610.09535)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WAPR: A Foundation Model for Wide-Angle Refinement in Unseen Object Pose Estimation
- 作者：Yulin Wang, Mengting Hu, Hongli Li, Jianghao Zhou, Chen Luo
- 出版日期：2026-10-07T06:38:15Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.09535

### 一句话总结
WAPR 是一个面向未见物体的零样本宽角度位姿精化基础模型，可在候选位姿旋转偏差高达 90 度的情况下进行精化，并兼顾快速推理与旋转对称物体的宽角度训练。

### 研究问题
现实应用要求 6D 位姿估计准确、快速，并能扩展到未见物体。论文关注的核心问题是：在未见物体位姿估计中，如何对存在较大旋转偏差（最高 90 度）的候选位姿进行宽角度精化，同时保持较快推理速度，并处理旋转对称物体的训练问题。

### 核心思路/方法
- 提出 WAPR，一个零样本宽角度位姿精化模型，用于精化旋转偏差最高 90 度的候选位姿。
- 每个检测到的物体实例仅使用少至 12 个候选位姿，支持每帧 1 秒内的快速推理，位姿估计吞吐量最高可达每秒 25 个检测物体实例。
- 针对旋转对称物体的宽角度训练，使用旋转对称先验，在损失计算前将对称等价的位姿目标规范化。
- 构建 SA6D 大规模 6D 训练数据集，包含上述先验；该数据集对 944 个 GSO 扫描获取 KASAL 辅助的旋转对称先验，并通过几何和纹理增强扩展为约 5 万个增强物体实例和约 200 万张渲染 RGB-D 图像。
- 引入角度平衡损失，通过降低无信息大误差样本的影响，稳定不同角度范围的学习。
- 在七个 BOP 核心数据集上进行实验，表明 WAPR 在快速和无约束推理设置下的未见物体 6D 位姿定位与检测中达到当前最优性能。

### 主要贡献
- 提出 WAPR 零样本宽角度位姿精化模型，支持高达 90 度旋转偏差的候选位姿精化。
- 实现快速推理：每帧 1 秒内，吞吐量最高达每秒 25 个检测物体实例，且每个物体实例仅需少至 12 个候选位姿。
- 利用旋转对称先验规范化对称等价位姿目标，以支持旋转对称物体的宽角度训练。
- 构建 SA6D 大规模 6D 训练数据集，包含约 5 万个增强物体实例和约 200 万张渲染 RGB-D 图像。
- 提出角度平衡损失，提升不同角度范围学习的稳定性。
- 在七个 BOP 核心数据集上取得未见物体 6D 位姿定位与检测的当前最优性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：论文针对未见物体 6D 位姿估计中的宽角度精化、快速推理和旋转对称训练问题提出完整方法，并构建大规模数据集，且在七个 BOP 核心数据集上报告当前最优性能；若关注 6D 位姿估计、零样本泛化或机器人视觉，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-world applications require 6D pose estimation to be accurate, fast, and scalable to unseen objects. This paper introduces WAPR, a zero-shot wide-angle pose refinement model that refines candidate poses with rotational deviations up to 90 degrees. With as few as 12 candidate poses per detected object instance, WAPR supports fast inference within 1 s per frame and reaches a pose-estimation throughput of up to 25 detected object instances per second. To support wide-angle training for rotationally symmetric objects, WAPR uses rotational symmetry priors to canonicalize symmetry-equivalent pose targets before loss computation. We further construct SA6D, a large-scale 6D training dataset with such priors. SA6D obtains KASAL-assisted rotational symmetry priors for 944 GSO scans and expands them through geometry and texture augmentation into about 50K augmented object instances and about 2M rendered RGB-D images. In addition, an angle-balanced loss stabilizes learning across different angular ranges by reducing the influence of uninformative large-error cases. Experiments on seven BOP core datasets show that WAPR achieves state-of-the-art performance in unseen-object 6D pose localization and detection under both fast and unconstrained inference settings. Project page: https://github.com/WangYuLin-SEU/WAPR.

</details>

#### 2026-10-07 - ActiveLang: Active Open-Vocabulary 3D Mapping with Semantic-Uncertainty-Guided Exploration

**Authors:** Liyan Chen, Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh, Philippos Mordohai
**Links:** [abs](https://arxiv.org/abs/2610.09518) - [pdf](https://arxiv.org/pdf/2610.09518)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D mapping, mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ActiveLang: Active Open-Vocabulary 3D Mapping with Semantic-Uncertainty-Guided Exploration
- 作者：Liyan Chen, Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh, Philippos Mordohai
- 出版日期：2026-10-07T06:15:39Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.09518) / [PDF](https://arxiv.org/pdf/2610.09518)

### 一句话总结
ActiveLang 是一个面向开放词汇 3D 建图的主动探索系统，通过语义不确定性引导视角选择，在紧凑的双高斯表示上在线适配语言特征，从而以更少观测和更低计算成本构建带语言标注的 3D 地图。

### 研究问题
机器人在协助人类完成多样任务时，需要同时理解周围环境的几何与语义信息。并且，机器人常在不熟悉的环境中工作、承担新任务，无法事先知道相关概念。这促使研究者构建带语言标注的 3D 地图，以支持开放词汇场景理解与人机交互。论文关注的核心问题是：如何让机器人主动探索场景，从而更高效地建立这类语言标注的 3D 地图。

### 核心思路/方法
论文提出 ActiveLang，一个用于主动开放词汇 3D 建图的自主系统，其探索由语义不确定性引导。方法上，ActiveLang 在紧凑的双高斯表示上进行在线语言特征适配，以适度的内存开销联合重建场景几何、外观与开放词汇语义。其规划器负责高效选择信息量高的视角，从而用更少观测和更低计算成本完成有效建图。

### 主要贡献
- 提出 ActiveLang，一个主动开放词汇 3D 建图系统，采用语义不确定性引导的探索策略。
- 在紧凑的双高斯表示上执行在线语言特征适配，联合重建几何、外观与开放词汇语义，且内存开销适中。
- 设计规划器以高效选择信息量高的视角，减少所需观测次数并降低计算成本。
- 在 Replica 与 ScanNet++ 上的实验表明，其 2D 与 3D 开放词汇分割相较在线和离线基线均有显著提升，说明主动探索场景能更高效地构建语言标注 3D 地图。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败场景、对特定数据集或传感器配置的依赖、计算资源上限、实时性约束，也未给出定量指标、消融实验细节或与基线的完整比较设置。

### 阅读优先级
中。理由：该论文面向开放词汇 3D 建图与主动探索的结合，属于 3D 重建、机器人/具身智能交叉方向，问题设定清晰且具有实际应用背景；摘要声称在 Replica 与 ScanNet++ 上取得显著提升。但摘要未提供具体方法细节、定量结果与局限性讨论，是否值得深入阅读取决于读者对主动建图、开放词汇语义或双高斯表示的关注程度。

</details>

<details>
<summary>Abstract</summary>

As robots increasingly assist humans with diverse tasks, they need both geometric and semantic understanding of their surroundings. Moreover, robots often operate in unfamiliar environments and take on new tasks without knowing the relevant concepts ahead of time. This motivates language-annotated 3D maps that support open-vocabulary scene understanding and human-robot interaction. We introduce ActiveLang, an autonomous system for active open-vocabulary 3D mapping with semantic-uncertainty-guided exploration. ActiveLang performs online language-feature adaptation on a compact dual-Gaussian representation to jointly reconstruct scene geometry, appearance, and open-vocabulary semantics with modest memory overhead. Its planner efficiently selects informative viewpoints, enabling effective mapping with fewer observations and lower computational cost. Experiments on Replica and ScanNet++ demonstrate substantial improvements in 2D and 3D open-vocabulary segmentation over both online and offline baselines, highlighting that actively exploring scenes builds language-annotated 3D maps more efficiently.

</details>

#### 2026-10-07 - Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning

**Authors:** Hanqiu Li Cai, Chema Garabito
**Links:** [abs](https://arxiv.org/abs/2610.09450) - [pdf](https://arxiv.org/pdf/2610.09450)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning
- 作者：Hanqiu Li Cai, Chema Garabito
- 出版日期：2026-10-07T05:07:09Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.09450 ；PDF: https://arxiv.org/pdf/2610.09450

### 一句话总结
论文从零预训练 3B 参数像素空间文本到图像 Transformer（Iris-3B），并将预训练潜空间模型 FLUX.2 Klein 4B 转换到像素空间，随后在深度估计与图像复原/超分任务上微调对比，发现像素空间生成先验并未带来显著下游提升，但 Iris-3B 本身可扩展到 3B 参数并在 1024² 文到图质量上可与潜空间模型竞争。

### 研究问题
论文要检验一个说法：像素空间扩散模型避免了潜空间模型中 VAE 的有损压缩，因此在细粒度细节重要的下游任务上可能具有优势。作者沿两条通往像素空间骨干的路线进行测试：从零预训练像素空间模型，以及将预训练潜空间模型转换为像素空间模型，并在单目深度估计和图像复原/超分任务上微调比较。

### 核心思路/方法
- 方法上包含两条路线：一是从零预训练 Iris-3B，一个 3B 参数像素空间文本到图像 Transformer，采用 \(256\to512\to1024\) 课程训练，并先在 \(256^2\) 上对预测目标和表示对齐进行消融，以决定扩展什么。
- 二是将一个预训练潜空间模型 FLUX.2 Klein base 4B 转换为像素空间。
- 对两个模型家族都微调用于单目深度估计和图像复原/超分。
- 对深度任务使用一个匹配的直接回归配方进行微调比较。
- 在 \(4\times\) DIV2K 复原任务上比较像素模型与潜空间 FLUX.2 Klein 微调版本。

### 主要贡献
- 预训练并发布了 Iris-3B 的权重和训练代码，表明使用 PixelDiT 的像素 Transformer（PiT）头进行像素空间预训练可扩展到 3B 参数。
- 展示 Iris-3B 在 \(1024^2\) 下、官方评估器下于 OneIG 上匹配 Qwen-Image 的文到图质量，即像素空间模型能达到与潜空间模型竞争的生成质量。
- 系统地测试并报告了一个负面结果：在单目深度估计和图像复原/超分任务上，使用像素空间生成先验没有显著提升；Iris-3B 在深度上与潜空间 FLUX.2 Klein 持平，转换后的像素 FLUX.2 Klein 落后；在 \(4\times\) DIV2K 复原上，两个像素模型都没有超过潜空间 FLUX.2 Klein 微调版本，转换版本略落后。
- 记录了相关配方、失败模式和这一负面结果背后仍存在的混淆因素。

### 局限性
- 摘要未提供足够信息说明数据集规模、训练计算量、评估指标数值结果、转换方法细节、消融实验具体结论、失败模式的具体内容以及混淆因素的具体列表。
- 摘要明确报告的是一个负面结果：像素空间生成先验在下游深度估计和图像复原/超分任务上未带来显著改善。
- 摘要未提供足够信息说明该结论是否可推广到其他下游任务、其他模型规模或其他像素空间架构。
- 摘要未提供足够信息说明 Iris-3B 与潜空间模型在文到图质量上的比较细节，仅提到在 OneIG 上匹配 Qwen-Image。

### 阅读优先级
中。理由：论文的核心发现是一个有价值的负面结果，挑战了“像素空间模型因避免 VAE 损失而在细粒度下游任务上更优”的直觉假设，并且发布了 3B 像素空间模型的权重与训练代码，对像素空间生成和下游微调研究有参考价值。但其主要实验集中在深度估计和图像复原/超分两个任务上，且摘要表明像素空间先验未带来优势，若读者关注的是像素空间生成模型本身的可扩展性或文到图质量，则仍有较高参考意义；若仅关注下游任务性能提升，则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Pixel-space diffusion models avoid the lossy VAE of latent models, which suggests an advantage on downstream tasks where fine-grained detail matters. We test this claim along both routes to a pixel-space backbone. We pretrain Iris-3B, a 3B-parameter pixel-space text-to-image transformer, from scratch through a $256\to512\to1024$ curriculum, after first ablating the prediction target and representation alignment at $256^2$ to decide what to scale. We also convert a pretrained latent model, FLUX.2 Klein base 4B, to pixel space. We fine-tune both families for monocular depth estimation and for image restoration/super-resolution. We find no significant improvement from using a pixel-space generative prior. Fine-tuned for depth with one matched direct-regression recipe, Iris-3B is level with the latent FLUX.2 Klein and the converted pixel FLUX.2 Klein falls behind it, and on $4\times$ DIV2K restoration neither pixel model beats a latent FLUX.2 Klein fine-tune, the converted one trailing it slightly. We document the recipes, the failure modes and the remaining confounds behind this negative result. Nevertheless, Iris-3B shows that pixel-space pretraining with the pixel-transformer (PiT) head of PixelDiT scales to 3B parameters and to text-to-image quality competitive with latent models, matching Qwen-Image on OneIG under the official evaluators at $1024^2$. We release its weights and training code in the hope that they help pave the way for further work on pixel-space generation.

</details>

#### 2026-10-06 - StyleFields: Multi-Scale AdaIN-Modulated Implicit SDFs for Coarse-to-Fine 3D Shape Reconstruction and Editing

**Authors:** Ehsan Garaaghaji, Nicolas Talabot, Pascal Fua, Doruk Oner
**Links:** [abs](https://arxiv.org/abs/2610.09200) - [pdf](https://arxiv.org/pdf/2610.09200)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, shape reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StyleFields: Multi-Scale AdaIN-Modulated Implicit SDFs for Coarse-to-Fine 3D Shape Reconstruction and Editing
- 作者：Ehsan Garaaghaji, Nicolas Talabot, Pascal Fua, Doruk Oner
- 出版日期：2026-10-06T22:51:51Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：abstract_url: https://arxiv.org/abs/2610.09200；pdf_url: https://arxiv.org/pdf/2610.09200

### 一句话总结
StyleFields 提出一种基于 DeepSDF 的隐式 SDF 架构，通过多层级 AdaIN 注入潜变量并配合由粗到细的监督与网络深度增长，实现高保真 3D 重建以及粗结构与细细节的可控几何风格混合。

### 研究问题
论文关注高保真 3D 重建中的可控几何风格混合问题：希望把一个物体的粗结构（coarse structure）与另一个物体的细尺度细节（fine-scale details）结合起来。摘要指出其目标是在不使用部件标签（part labels）或对抗训练（adversarial training）的情况下实现内容-风格解耦（content-style decoupling），并进一步将重建用于性能驱动的设计编辑。

### 核心思路/方法
- 基础架构：基于 DeepSDF 的隐式 SDF 架构。
- 核心机制：深度感知调制（depth-aware modulation），不是使用单一全局编码，而是在解码器多个深度层级通过多级 Adaptive Instance Normalization（AdaIN）注入潜变量。
- 训练策略：使用由粗到细（coarse-to-fine）的调度，监督匹配的辅助头（auxiliary heads），同时逐渐增加网络深度。
- 解耦方式：通过上述设计，使早期层对齐全局形状、后期层对齐高频细节，从而实现内容-风格解耦。
- 编辑应用：在学习到的 surrogate drag predictor 作为可微目标下，对重建的汽车进行优化；通过冻结互补的潜变量流（freezing the complementary latent stream），实现全局形态或表面细节的有针对性编辑。

### 主要贡献
- 提出 StyleFields，一种 DeepSDF 基础的隐式 SDF 架构，用于高保真 3D 重建并支持可控的几何风格混合。
- 提出深度感知的多级 AdaIN 潜变量注入方式，结合由粗到细监督和网络深度渐增，实现无需部件标签或对抗训练的内容-风格解耦。
- 摘要声称其可获得忠实重建、有说服力的跨实例混合（cross-instance hybrids），并在注入深度和监督粒度的消融中取得一致增益。
- 展示一个汽车空气动力学应用：以学习到的 surrogate drag predictor 作为可微目标，对重建汽车进行优化，从而实现全局形态或表面细节的定向编辑。

### 局限性
- 摘要未提供足够信息说明方法在大规模、开放类别或复杂拓扑数据上的泛化能力。
- 摘要未提供足够信息说明计算成本、训练时间、参数量或推理效率。
- 摘要未提供足够信息说明定量指标、数据集、基线比较或消融实验的具体数值。
- 摘要未提供足够信息说明 surrogate drag predictor 的精度、适用范围及其对优化结果可靠性的影响。
- 摘要未提供足够信息说明跨实例混合在语义合理性、几何合法性或失败案例方面的表现。

### 阅读优先级
高。理由：该论文聚焦隐式 3D 重建、内容-风格解耦和可控几何编辑，并将重建与空气动力学性能优化连接起来，主题同时涉及 3D 重建与下游性能驱动设计；摘要明确给出方法核心机制、消融增益和实际应用，具有较强的方法与应用参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce StyleFields, a DeepSDF-based architecture for high-fidelity 3D reconstruction that enables controllable geometric style mixing: the coarse structure of one object can be combined with the fine-scale details of another. The core idea is depth-aware modulation: instead of a single global code, we inject latents via multi-level Adaptive Instance Normalization at several decoder depths, and supervise matching auxiliary heads with a coarse-to-fine schedule while gradually growing network depth. This aligns early layers with global shape and later layers with high-frequency detail, achieving content-style decoupling without part labels or adversarial training. StyleFields delivers faithful reconstructions, convincing cross-instance hybrids, and consistent gains in ablations over injection depth and supervision granularity. We further demonstrate a practical application in automotive aerodynamics: a learned surrogate drag predictor serves as a differentiable objective to optimize reconstructed cars, allowing targeted edits of global form or surface details by freezing the complementary latent stream. StyleFields offers a simple, effective recipe for controllable implicit reconstruction and downstream performance-driven design.

</details>

#### 2026-10-06 - Digital Twin-Driven Real2Sim2Real: Simulator-Conditioned Generation via Paired Driving-Scene Reconstruction

**Authors:** Hojun Lim, Hyeongseok Jeon, Donghyun Kim, Soonyoung Jung, Heecheol Yoo
**Links:** [abs](https://arxiv.org/abs/2610.08339) - [pdf](https://arxiv.org/pdf/2610.08339)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, autonomous driving, driving scene, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Digital Twin-Driven Real2Sim2Real: Simulator-Conditioned Generation via Paired Driving-Scene Reconstruction
- 作者：Hojun Lim, Hyeongseok Jeon, Donghyun Kim, Soonyoung Jung, Heecheol Yoo
- 出版日期：2026-10-06T13:36:50Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.08339 ；PDF https://arxiv.org/pdf/2610.08339

### 一句话总结
论文提出数字孪生驱动的 Real2Sim2Real 流程 DT-R2S2R：先在带地理坐标的数字孪生中重建真实驾驶片段以对齐模拟器渲染，再以此条件化扩散模型，从而在无目标区域真实图像参与训练的情况下，为新的目标区域合成带免费标注的逼真驾驶数据。

### 研究问题
基于相机的自动驾驶 3D 感知依赖大规模带标注数据集，而将系统部署到新的目标区域通常需要重新采集与标注数据。现有生成式增广方法存在根本取舍：标签条件方法要消耗它本意替代的标注，模拟器条件方法虽提供免费标注，却缺乏对特定真实环境的视觉接地。论文因此研究：数字孪生驱动的 Real2Sim2Real 流程能在多大程度上替代目标区域的真实数据。

### 核心思路/方法
论文构建 DT-R2S2R 流程。第一步为 DT-R2S：在带地理参照的数字孪生（DT）中重建已录制的驾驶片段。第二步为 DT-S2R：以几何对齐的模拟器渲染为条件，训练扩散模型，形成以数字孪生为接地的 Sim2Real 模型。该模型可在数字孪生覆盖范围内的已重建场景以及新模拟器场景中，依据低成本且带地理参照的模拟器数据合成逼真驾驶图像。生成数据的有效性在多种 3D 检测器上验证。

### 主要贡献
- 提出数字孪生驱动的 Real2Sim2Real 流程 DT-R2S2R，用带地理参照的数字孪生重建真实驾驶片段，以几何对齐的模拟器渲染条件化扩散模型。
- 得到数字孪生接地的 Sim2Real 模型 DT-S2R，可依据低成本、带地理参照的模拟器数据，在数字孪生覆盖范围内的已重建场景和新模拟器场景中合成逼真驾驶图像。
- 在多种 3D 检测器上验证生成数据有效性；其中 DETR3D 在不使用目标图像训练检测器的情况下，达到目标区域真实数据 oracle 所获 mAP 的 93.18%。
- 表明与既有目标区域外真实数据进行简单协同训练可超过该 oracle，说明在数字孪生可用区域，DT-R2S2R 可显著降低人工现场采集与标注成本，为扩展 3D 感知提供实用基础。

### 局限性
- 方法适用范围受“数字孪生覆盖范围”和“数字孪生可用区域”限制；摘要未提供足够信息说明覆盖范围之外或缺乏数字孪生的区域表现如何。
- 摘要未提供足够信息说明数字孪生重建的精度要求、重建误差对下游生成与检测的影响。
- 摘要未提供足够信息说明扩散模型训练细节、数据规模、计算成本与推理开销。
- 摘要未提供足够信息说明所验证的 3D 检测器完整清单、数据集构成以及除 DETR3D 外各检测器的具体指标。
- 摘要未提供足够信息说明协同训练设置中“目标区域外真实数据”的来源、数量与配比敏感性。

### 阅读优先级
高。理由：该工作直接针对自动驾驶 3D 感知中跨区域部署的数据采集与标注成本问题，提出数字孪生接地的 Real2Sim2Real 生成式增广方案，并给出接近目标区域真实数据 oracle 的量化结果（DETR3D 达 93.18% mAP），且协同训练可超过 oracle，对数据高效 3D 感知与仿真到现实迁移方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera-based 3D perception for autonomous driving relies heavily on large annotated datasets, and deploying such a system to a new target region typically requires data collection and annotation. Generative augmentation has been proposed to reduce this cost, but existing approaches face a fundamental trade-off: label-conditioned methods consume the very annotations they aim to replace, while simulator-conditioned methods offer free annotations but lack visual grounding to specific real environments. This work investigates the extent to which a digital-twin-driven Real2Sim2Real pipeline (DT-R2S2R) can substitute for target-region real data. By reconstructing recorded driving clips inside a georeferenced digital twin (DT-R2S), we condition a diffusion model on geometrically aligned simulator renderings, establishing a digital twin-grounded Sim2Real model (DT-S2R). As a result, DT-S2R synthesizes photorealistic driving images given low-cost yet georeferenced simulator data across both reconstructed and novel simulator scenes within digital-twin coverage. The efficacy of generated data is verified on diverse 3D detectors. DETR3D, especially, reports 93.18% of mAP obtained by a target-region real-data oracle, without employing target images for detector training. Furthermore, simple co-training with existing out-of-target real data outperforms the oracle. Thus, DT-R2S2R can substantially reduce the cost of manual on-site data collection and annotation in digital twin-available districts, providing a practical foundation for scaling 3D perception.

</details>

#### 2026-10-06 - Image-Space Refraction Correction for Underwater 3D Reconstruction: Warping Flat-Port Views into Pinhole Perspective

**Authors:** Chelim Lim, Tobias Fischer, Emilio Olivastri, Beverley Gorry, Michael Milford, Alejandro Fontan
**Links:** [abs](https://arxiv.org/abs/2610.07788) - [pdf](https://arxiv.org/pdf/2610.07788)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, SfM, SLAM, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Image-Space Refraction Correction for Underwater 3D Reconstruction: Warping Flat-Port Views into Pinhole Perspective
- 作者：Chelim Lim, Tobias Fischer, Emilio Olivastri, Beverley Gorry, Michael Milford, Alejandro Fontan
- 出版日期：2026-10-06T05:33:46Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.07788) / [PDF](https://arxiv.org/pdf/2610.07788)

### 一句话总结
提出一种在图像空间进行的基于物理的水下折射校正方法，将平面端口平口相机视图变形为针孔透视，以消除重建中的碗状畸变。

### 研究问题
消费级相机广泛应用于水下探索与珊瑚礁、海底栖息地测绘，但平口外壳界面处的折射会导致重建场景和相机轨迹出现碗状变形，损害测绘与导航所需的度量精度。论文旨在在重建之前移除主要的折射畸变。

### 核心思路/方法
在图像空间引入基于物理的折射校正，将平面端口视图变形为针孔透视。该方法与下游任务无关，校正后的图像可直接作为现有重建和 SLAM 算法的输入。通过光线追踪仿真刻画折射畸变，并在两个具有不同场景结构的真实水下数据集上验证校正效果。

### 主要贡献
- 提出图像空间的、基于物理的折射校正方法，将平口视图变形为针孔透视。
- 方法对下游任务无关，校正图像可直接供现有重建与 SLAM 算法使用。
- 通过光线追踪仿真刻画折射畸变，并在两个真实水下数据集上验证。
- 与常规及折射式 Structure-from-Motion（SfM）相比，方法在去除重建变形的同时注册更多帧并保持较低重投影误差。
- 校正可泛化到多种重建与 VSLAM 后端，显示对下游视觉流程的广泛适用性。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体计算复杂度、对极端水下条件或不同相机参数的泛化边界、失败案例，也未提供定量实验指标的详细数值。

### 阅读优先级
高。理由：论文针对水下 3D 重建中由平口折射引起的系统性几何畸变这一实际问题，提出与下游算法解耦的图像空间校正方案，并在真实数据集上验证且声称可泛化到多种重建与 VSLAM 后端，对水下视觉测绘与导航流程具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Consumer-grade cameras in flat-port housings are widely used for underwater exploration and mapping of coral reefs and seafloor habitats due to their low cost and accessibility. However, refraction at flat-port interfaces causes bowl-shaped deformation in reconstructed scenes and camera trajectories, compromising the metric accuracy required for mapping and navigation. To remove the dominant refractive distortion before reconstruction, we introduce a physics-based refraction correction in image space. Our method is downstream-agnostic: the refraction-corrected images can be directly used as input to existing reconstruction and SLAM algorithms. We characterize the refractive distortion through ray-tracing simulations and validate our correction on two real underwater datasets with differing scene structures. Compared with conventional and refractive Structure-from-Motion (SfM), our approach removes reconstruction deformation while registering more frames and maintaining low reprojection error. The correction further generalizes across diverse reconstruction and VSLAM backends, demonstrating its broad applicability to downstream vision pipelines.

</details>

#### 2026-10-05 - SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation

**Authors:** Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin
**Links:** [abs](https://arxiv.org/abs/2610.07472) - [pdf](https://arxiv.org/pdf/2610.07472)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, pose estimation, Gaussian Splatting, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation
- 作者：Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin
- 出版日期：2026-10-05T22:38:27Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.07472 ；PDF https://arxiv.org/pdf/2610.07472

### 一句话总结
SURGE 是一个面向水下 ROV 的相机-声呐融合框架，通过在因子图中联合估计轨迹与目标位置，并将恢复出的度量位姿用于声呐高斯泼溅，从而在真实水下 RGB-声呐数据上改善定位一致性并得到更紧凑、原生度量的重建结果。

### 研究问题
水下 ROV 在洞穴、沉船和水下基础设施等环境中执行探索与巡检任务时，需要准确的三维环境理解，这依赖可靠的载体定位和度量场景重建。然而水下外部定位常常不可用，小型 ROV 主要依赖自身感知。光学视觉能提供丰富视觉与几何信息，但存在尺度模糊和轨迹漂移；二维成像声呐能提供度量距离，却缺少完整三维几何。现有水下重建方法通常分别处理这些限制，或假设传感器位姿已知，导致定位与重建相互割裂。论文要解决的问题是如何在外部定位不可用的情况下，将视觉与声学观测结合，实现定位与重建的联合估计。

### 核心思路/方法
SURGE 是一个相机-声呐框架，其核心是在因子图中整合视觉观测和声学观测，联合估计 ROV 轨迹与目标位置。在获得恢复出的度量位姿后，方法使用这些位姿进行声呐高斯泼溅，从而完成重建。摘要没有提供因子图的具体节点、因子形式、优化细节、图像门控机制的具体实现，也没有提供网络结构、损失函数或训练策略等细节。

### 主要贡献
- 提出 SURGE，一个相机-声呐融合框架，将视觉与声学观测在因子图中结合，联合估计 ROV 轨迹和目标位置。
- 利用恢复出的度量位姿驱动声呐高斯泼溅，将定位与重建连接起来。
- 在真实水下 RGB-声呐观测上进行实验，摘要称 SURGE 相比传统基于视觉的位姿估计显著提升了定位一致性，并相比 RGB 高斯泼溅基线产生更紧凑、原生度量的重建。
- 摘要未提供足够信息说明消融实验、定量指标、数据集规模或与更多基线的系统比较。

### 局限性
摘要未提供足够信息说明方法的具体适用边界、失败场景、计算代价、实时性、对传感器标定误差的敏感性、不同水质或浑浊度下的表现，以及定量评价指标的完整情况。摘要仅提到实验在真实水下 RGB-声呐观测上进行，未说明实验环境数量、目标类型、轨迹长度或重建精度数值。

### 阅读优先级
高。理由：该论文位于 3D 重建与多视图几何、神经场景表示与渲染、以及水下机器人应用的交叉方向，直接针对水下 ROV 在无外部定位条件下定位与重建割裂的问题，提出相机-声呐因子图联合估计与声呐高斯泼溅结合的方案，问题定义清晰且应用场景明确。若关注水下感知、多模态融合定位建图或声呐神经渲染，该论文具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Remotely operated vehicles (ROVs) are widely used to explore and inspect underwater environments such as caves, shipwrecks, and submerged infrastructure. These missions require accurate 3D understanding of the surrounding environment, which depends on both reliable vehicle localization and metric scene reconstruction. However, external positioning is often unavailable underwater, requiring small ROVs to rely primarily on onboard perception. Optic vision provides rich visual and geometric information but suffers from scale ambi- guity and trajectory drift, whereas 2D imaging sonar provides metric range but incomplete 3D geometry. Existing underwater reconstruction approaches typically address these limitations separately or assume known sensor poses, leaving localization and reconstruction disconnected. We present SURGE, a camera sonar framework that jointly estimates the ROV trajectory and target location by integrating visual and acoustic observations within a factor graph, then uses the recovered metric poses for sonar Gaussian splatting. Experiments on real underwater RGB sonar observations show that SURGE substantially improves localization consistency over conventional vision based pose estimation and produces a more compact, natively metric reconstruction than RGB Gaussian splatting baselines.

</details>

#### 2026-10-05 - Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models

**Authors:** Zhimin Shao, Xijun Liu, Zhaoliang Zhang, Yutao Tang, Abhay Yadav, Rama Chellappa, Cheng Peng
**Links:** [abs](https://arxiv.org/abs/2610.06813) - [pdf](https://arxiv.org/pdf/2610.06813)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models
- 作者：Zhimin Shao, Xijun Liu, Zhaoliang Zhang, Yutao Tang, Abhay Yadav, Rama Chellappa, Cheng Peng
- 出版日期：2026-10-05T17:55:06Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要链接 https://arxiv.org/abs/2610.06813；PDF 链接 https://arxiv.org/pdf/2610.06813

### 一句话总结
论文提出 Masked Geometric Encoder（MGE），通过在训练中从全局注意力中策略性丢弃帧 token 并向预训练的全上下文教师模型蒸馏，学习在不完整跨视角上下文下更鲁棒的几何表示，并配套提出 Anchor-Guided Adaptive token merging 以提升推理效率。

### 研究问题
- 现有 3D 基础模型依赖全对全全局注意力，导致二次复杂度并限制长序列推理。
- 无约束的跨视角交互可能传播来自遮挡视图或“视觉相似但几何距离较远”视图的不可靠证据。
- 因此需要在不完整跨视角上下文条件下，学习更鲁棒的几何表示，同时兼顾标准基准性能与推理效率。

### 核心思路/方法
- 提出 Masked Geometric Encoder（MGE），在训练时策略性地从全局注意力中丢弃 frame tokens。
- 通过从预训练的全上下文教师模型进行蒸馏，使模型学习内在更丰富的逐帧表示，并提供足够的中间监督以避免性能退化。
- 在推理阶段，提出 Anchor-Guided Adaptive token merging 技术：保留具有代表性的 anchor frames，同时联合合并其余视图中的冗余 token。
- 目标是在保持较高重建质量的同时实现推理加速，尤其在有限视图设置下。

### 主要贡献
- 提出 MGE，在遮挡和“doppelganger views”场景下带来更强性能，同时在标准基准上保持高性能。
- 表明更丰富的逐帧表示可提升推理阶段 token 减少的有效性。
- 提出 Anchor-Guided Adaptive token merging 技术，以保留代表性 anchor frames 并合并冗余 tokens。
- 与其他高效推理方法相比，在实现推理加速的同时持续保持更高的重建质量，尤其在有限视图设置下。

### 局限性
- 摘要未提供足够信息说明具体实验数据集、评价指标、计算开销细节、失败案例或方法适用范围。
- 摘要未提供足够信息说明 MGE 丢弃 frame tokens 的具体策略、教师模型结构、蒸馏损失细节及 token merging 的完整算法流程。
- 摘要未提供足够信息说明在哪些条件下性能可能下降，或是否对特定场景、视图数量、硬件条件存在限制。

### 阅读优先级
高。理由：该论文针对 3D 基础模型中的全局注意力复杂度与跨视角不可靠证据传播问题提出明确方法，并同时关注遮挡、doppelganger views、标准基准和有限视图下的推理效率与重建质量，问题重要且方法方向清晰，适合关注 3D 重建、多视图几何与高效推理的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent progress in 3D foundation models has enabled rapid 3D reconstruction and camera calibration by leveraging learned 3D priors from vast amount of spatial data. However, the all-to-all global attention design leads to quadratic complexity and limits long-sequence inference; unconstrained cross-view interactions also can propagate unreliable evidence from occluded or visually similar but geometrically distant views. In this paper, We introduce a Masked Geometric Encoder (MGE), which promotes the learning of robust geometric representations under incomplete cross-view context. During training, MGE strategically drops frame tokens from global attention and distills from a pretrained full-context teacher model. This allows the model to learn an intrinsically richer per-frame representation while providing sufficient intermediate supervision to avoid performance degradation. Through extensive experiments, we show that MGE leads to much stronger performance under occlusion and doppelganger views while retaining high performance on standard benchmarks. Such a richer frame representation also leads to more effective token reduction during inference. To this end, we develop a novel Anchor-Guided Adaptive token merging technique that preserves representative anchor frames while jointly merging redundant tokens from the remaining views. Compared to other efficient inference approaches, we can achieve inference speedup while consistently maintaining higher reconstruction quality, particularly in limited-view settings.

</details>

#### 2026-10-05 - FrontVeg V2: A Training-Free Software Framework for Foreground-Aware Zero-Shot Plant Trait Segmentation in High-Resolution Images of Trellised Crops

**Authors:** Abdoul Djalil Ousseini Hamza, Herearii Metuarea, Corentin Lothod{é}, Morgane Roth, Jacem Ben Hamden, Eric Duch{ê}ne, Lionel Ley, David Alletru, David Rousseau
**Links:** [abs](https://arxiv.org/abs/2610.06575) - [pdf](https://arxiv.org/pdf/2610.06575)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FrontVeg V2: A Training-Free Software Framework for Foreground-Aware Zero-Shot Plant Trait Segmentation in High-Resolution Images of Trellised Crops
- 作者：Abdoul Djalil Ousseini Hamza, Herearii Metuarea, Corentin Lothod{é}, Morgane Roth, Jacem Ben Hamden, Eric Duch{ê}ne, Lionel Ley, David Alletru, David Rousseau
- 出版日期：2026-10-05T15:53:57Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.06575 ；PDF https://arxiv.org/pdf/2610.06575

### 一句话总结
FrontVeg V2 是一个开源、免训练的软件框架，用于在棚架作物高分辨率图像中实现前景感知的零样本植物性状分割。

### 研究问题
论文针对棚架作物高分辨率图像中的植物性状分割问题，尤其是邻近植被行造成的干扰。摘要指出，该框架旨在分割植物器官和病害症状，同时减少由邻近植被行引发的检测。摘要未提供足够信息说明具体作物种类、病害类型或评估数据集细节。

### 核心思路/方法
FrontVeg V2 采用免训练、零样本的分割流程，包含以下组成部分：
- 单目深度估计；
- 使用 Valley-Aware Depth Thresholding 进行自动前景提取；
- 分块零样本分割；
- Graph-Based Mask Assembly；
- 几何感知融合。

当前实现集成了 Depth Anything V2（DAV2）与 SAM3，并支持命令行批处理和 Napari 图形界面两种使用方式。摘要未提供足够信息说明各模块的具体算法细节、参数设置或处理流程。

### 主要贡献
- 提出 FrontVeg V2，一个开源、免训练的前景感知零样本植物性状分割软件框架。
- 将单目深度估计、前景提取、分块零样本分割、掩码组装与几何感知融合组合为统一流程。
- 支持在无需任务特定模型重训练的情况下，用于多作物、多性状的数字表型分析。
- 当前实现集成 DAV2 与 SAM3，并提供命令行批处理与 Napari 图形界面。
- 摘要未提供足够信息说明定量实验结果、精度指标或与基线方法的比较。

### 局限性
- 摘要未提供足够信息说明该框架在何种数据集、作物种类或病害症状上进行了验证。
- 摘要未提供足够信息说明分割精度、鲁棒性、运行效率或失败案例。
- 摘要未提供足够信息说明 Valley-Aware Depth Thresholding、Graph-Based Mask Assembly 和几何感知融合的具体实现限制。
- 摘要未提供足够信息说明对 Depth Anything V2 和 SAM3 的依赖是否带来计算资源或泛化性方面的约束。
- 摘要未提供足够信息说明与监督学习方法或其他零样本方法的对比结果。

### 阅读优先级
中。理由：该论文提出的是面向高分辨率棚架作物图像、免训练且零样本的分割框架，并整合了深度估计与基础分割模型，主题与植物表型、零样本分割和农业视觉相关。但摘要未提供定量实验、数据集和对比结果，无法仅凭摘要判断其实际性能与创新程度；若关注农业视觉、零样本分割或数字表型工具，可列为中等优先级阅读。

</details>

<details>
<summary>Abstract</summary>

FrontVeg V2 is an open-source, training-free software framework for foregroundaware zero-shot segmentation of plant traits in high-resolution images of trellised crops. The pipeline combines monocular depth estimation, automatic foreground extraction using Valley-Aware Depth Thresholding, tiled zero-shot segmentation, Graph-Based Mask Assembly, and geometry-aware fusion. This design enables plant organs and disease symptoms to be segmented while reducing detections arising from neighboring vegetation rows. The current implementation integrates Depth Anything V2 (DAV2) and SAM3 and can be used through both command-line batch processing and a Napari graphical interface. FrontVeg V2 provides a reusable framework for multi-crop, multi-trait digital phenotyping without task-specific model retraining.

</details>

#### 2026-10-05 - Structural Foundations of Nonlinear Systems with Unknown Inputs: The UID-Induced Normal Form and Minimal-Sensing Structure-from-Motion

**Authors:** Agostino Martinelli
**Links:** [abs](https://arxiv.org/abs/2610.05939) - [pdf](https://arxiv.org/pdf/2610.05939)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Structural Foundations of Nonlinear Systems with Unknown Inputs: The UID-Induced Normal Form and Minimal-Sensing Structure-from-Motion
- 作者：Agostino Martinelli
- 出版日期：2026-10-05T07:56:38Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.05939) / [PDF](https://arxiv.org/pdf/2610.05939)

### 一句话总结
本文提出非线性未知输入系统的首个通用结构性状态估计方案（UID 诱导标准型），统一解决了未知输入的解耦与重构问题，并以一种仅需三个点特征与单轴陀螺仪的最小 Structure-from-Motion 配置验证了其可行性。

### 研究问题
论文关注由未知输入驱动的非线性系统的状态估计问题，试图在不对未知输入施加任何模型或随机假设的前提下，从结构层面处理未知输入对可观测动态的影响，即如何将未知输入信息分解、解耦并重建，并探索该框架在最小传感配置下的 Structure-from-Motion 应用。

### 核心思路/方法
- 基于非线性未知输入可观测性理论，证明任意此类系统都存在一个结构等价的表示，称为 UID 诱导标准型（UID-induced normal form）。
- 该表示将未知输入携带的信息分解为两个互补部分：与可观测动态在结构上解耦的未知输入方向，以及完全表示影响可观测动态的未知输入信息的可观测量。
- 由此在不需要任何未知输入模型或随机假设的条件下，统一给出未知输入解耦与未知输入重构的结构性方案。
- 将该框架应用于一种此前未被探索的最小 Structure-from-Motion 配置：仅使用三个点特征和单个单轴陀螺仪进行递归状态估计，可恢复三维结构与相机运动，但存在一个未知的全局尺度因子。

### 主要贡献
- 建立了首个针对未知输入驱动非线性系统的通用结构性状态估计解。
- 提出 UID 诱导标准型，将未知输入信息分解为结构性解耦方向与可观测表示量，统一了未知输入解耦与重构，且不依赖未知输入的模型或随机假设。
- 展示了一个此前未被探索的最小 Structure-from-Motion 配置，说明仅用三个点特征和单轴陀螺仪即可进行递归状态估计并恢复结构、相机运动（至多相差未知全局尺度）。
- 在真实世界数据上的实验验证了该框架，并证明了该最小传感配置的可行性。

### 局限性
- 摘要仅提及恢复三维结构与相机运动“至多相差一个未知全局尺度因子”，尺度不确定性未被消除。
- 摘要未说明计算复杂度、收敛性保证、对噪声或异常值的鲁棒性，也未给出与现有方法的定量对比——摘要未提供足够信息。
- 摘要未说明实验所用真实数据的规模、场景类型及评价指标——摘要未提供足够信息。
- 摘要未说明该标准型在更一般系统上的构造条件或适用范围限制——摘要未提供足够信息。

### 阅读优先级
高。理由：论文声称首次给出未知输入非线性系统状态估计的通用结构性解，并提出最小传感 Structure-from-Motion 配置，主题与 3D 重建及多视图几何直接相关；但具体适用边界与实验细节需阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

This paper establishes the first general structural solution to the problem of state estimation for nonlinear systems driven by unknown inputs. Building upon nonlinear unknown-input observability theory, we show that every such system admits a structurally equivalent representation, referred to as the UID-induced normal form. The proposed representation decomposes the information carried by the unknown inputs into two complementary components: unknown-input directions that are structurally decoupled from the observable dynamics and observable quantities that completely represent the unknown-input information affecting the observable dynamics. As a consequence, the UID-induced normal form provides a unified structural solution to unknown-input decoupling and unknown-input reconstruction, without requiring any model or stochastic assumption on the unknown inputs. The practical significance of the proposed framework is demonstrated through a previously unexplored minimal Structure-from-Motion configuration. The proposed representation enables recursive state estimation from only three point features and a single-axis gyroscope, allowing the recovery of the three-dimensional structure and camera motion up to an unknown global scale factor. Experiments on real-world data validate the proposed framework and demonstrate the feasibility of this minimal sensing configuration.

</details>

#### 2026-10-05 - Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM

**Authors:** Junhyun Nam, Wonse Jo
**Links:** [abs](https://arxiv.org/abs/2610.05757) - [pdf](https://arxiv.org/pdf/2610.05757)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM
- 作者：Junhyun Nam, Wonse Jo
- 出版日期：2026-10-05T04:06:38Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要链接 https://arxiv.org/abs/2610.05757 ；PDF 链接 https://arxiv.org/pdf/2610.05757

### 一句话总结
论文提出 Hybrid DeepSEE（HDS），一种人在回路（HITL）的神经符号框架，用于在视觉 SLAM 中主动预判漂移，并借助 LLM 将人类定性上下文转化为可解释的符号约束，以提升可靠性。

### 研究问题
视觉 SLAM 中的数据驱动模型虽然具备预测能力，但其“黑盒”特性在分布外（OOD）环境中常常产生物理上不一致的输出，从而影响漂移预判的可靠性。

### 核心思路/方法
HDS 将神经漂移风险估计与符号约束推理相结合。具体而言，框架使用一个大型语言模型（LLM）作为推理桥梁，把定性的、来自人类上下文的输入转化为可解释的符号约束，从而在神经预测基础上引入符号层面的推理与约束。

### 主要贡献
- 提出 Hybrid DeepSEE（HDS），一种人在回路（HITL）的神经符号框架，面向视觉 SLAM 的主动漂移预判。
- 将神经漂移风险估计与符号约束推理相集成，以应对数据驱动模型在 OOD 环境中输出物理不一致的问题。
- 使用 LLM 作为推理桥梁，把定性的人类上下文翻译为可解释的符号约束。
- 在该架构基础上，提出一个更强的漂移预判框架，旨在提升视觉 SLAM 的可靠性与一致性。

### 局限性
摘要未提供足够信息。包括具体的实验设置、数据集、评价指标、定量结果、与基线方法的对比、LLM 的具体使用方式与失败案例、HITL 的交互负担、符号约束的覆盖范围与可扩展性，以及实时性等，摘要均未提供足够信息。

### 阅读优先级
中。理由是：该论文聚焦视觉 SLAM 漂移预判中的可靠性、可解释性与 OOD 问题，并将神经符号方法与人在回路、LLM 推理桥接相结合，主题具有一定交叉创新性；但摘要未给出实验验证与量化结果，难以仅凭摘要判断其实际效果与相对优势。

</details>

<details>
<summary>Abstract</summary>

This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drift risk estimation with symbolic constraint reasoning. By utilizing a Large Language Model (LLM) as a reasoning bridge, the framework translates qualitative human context into interpretable symbolic constraints. Building upon this architecture, we propose a superior drift anticipation framework that ensures enhanced reliability and consistency in Visual SLAM

</details>

#### 2026-10-04 - F$^2$ SLAM: Turning Feed-Forward Geometry into Persistent Factors for SLAM

**Authors:** Zhisong Xu, Fan Zhu, Jiawei Qian, Ziyu Chen, Zhenjun Zhao, Javier Civera
**Links:** [abs](https://arxiv.org/abs/2610.05207) - [pdf](https://arxiv.org/pdf/2610.05207)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, bundle adjustment, dense reconstruction, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：F$^2$ SLAM: Turning Feed-Forward Geometry into Persistent Factors for SLAM
- 作者：Zhisong Xu, Fan Zhu, Jiawei Qian, Ziyu Chen, Zhenjun Zhao, Javier Civera
- 出版日期：2026-10-04T13:24:27Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类；未提供二级分类）
- 链接：[摘要](https://arxiv.org/abs/2610.05207) / [PDF](https://arxiv.org/pdf/2610.05207)

### 一句话总结
该论文提出 F$^2$SLAM，将前馈三维模型提供的多视图几何直接转化为持久稠密因子图中的优化原生“目标-权重”测量，从而在统一的稠密光束法平差中联合约束位姿、逆深度与可选相机内参。

### 研究问题
前馈三维模型能提供较强的多视图几何先验，而在线 SLAM 主要依赖局部测量，在长序列上会累积漂移。现有结合二者的尝试通常把前馈预测当作外部几何状态，在在线估计完成后再进行对齐或融合，这导致更广泛的多视图证据被排除在优化 SLAM 状态的优化器之外。

### 核心思路/方法
- 不将前馈几何作为事后对齐或融合的外部状态，而是直接转换为优化原生的目标-权重测量，并附着在持久稠密因子图上。
- 采用双频流结构：高频流维持局部跟踪约束与图连通性；低频流利用更宽的多视图上下文，在状态一致性检查后有选择地刷新已有测量。
- 两条流通过单一稠密光束法平差共同约束同一组位姿、逆深度以及可选的相机内参。

### 主要贡献
- 提出把前馈几何转化为持久优化因子/测量的 SLAM 框架，使多视图证据进入优化器内部，而非停留在事后融合层面。
- 设计高频局部跟踪与低频多视图上下文刷新相结合的双频机制，并引入状态一致性检查以选择性更新测量。
- 在统一稠密光束法平差中同时约束位姿、逆深度和可选内参，覆盖标定与未标定设置。
- 摘要称在多个基准上展示出稳定的轨迹估计与改进的稠密重建；在 Replica 数据集未标定配置下，将平均 ATE RMSE 从最强前馈基线的 0.030 m 降至 0.002 m。

### 局限性
- 摘要未提供足够信息说明方法的具体计算开销、实时性、高频流与低频流的具体频率设置。
- 摘要未提供足够信息说明状态一致性检查的具体判据与失败情形。
- 摘要未提供足够信息说明除 Replica 外其他基准的详细结果、消融实验及与更多 SLAM 方法的完整对比。
- 摘要未提供足够信息说明在极端场景（如快速运动、弱纹理、动态环境）下的表现与鲁棒性。

### 阅读优先级
高。理由：该论文针对前馈几何与在线 SLAM 结合方式提出“直接转为优化原生持久因子”的明确新思路，并报告了未标定设置下显著的 ATE RMSE 改进；若关注多视图几何先验与 SLAM 优化器的深度耦合、稠密重建或标定/未标定统一优化，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D models provide strong multi-view geometric priors, while on- line simultaneous localization and mapping (SLAM) relies mainly on local mea- surements and can accumulate drift over long sequences. Existing attempts to combine the two typically treat feed-forward predictions as an external geomet- ric state that is aligned or fused with the online estimate after the fact, which keeps broader multi-view evidence outside the optimizer that refines the SLAM state. We present F2SLAM, which instead converts feed-forward geometry di- rectly into optimization-native target-weight measurements attached to a persis- tent dense factor graph. A high-frequency stream maintains local tracking con- straints and graph connectivity, while a low-frequency stream uses wider multi- view context to selectively refresh existing measurements after a state-consistency check. Both streams constrain the same poses, inverse depths, and optional cam- era intrinsics through a single dense bundle adjustment. Experiments on multiple benchmarks demonstrate consistently strong trajectory estimation and improved dense reconstruction in both calibrated and uncalibrated settings. Notably, the uncalibrated configuration reduces the average ATE RMSE from 0.030 m for the strongest feed-forward baseline to 0.002 m on the Replica dataset.

</details>

#### 2026-10-04 - SPACE-CLIPv2: Decoding Local Geometry from Frozen CLIP for Monocular Depth Estimation

**Authors:** Hyun Song, Taewan Cho, Kangmin Kim, Andrew Jaeyong Choi
**Links:** [abs](https://arxiv.org/abs/2610.05029) - [pdf](https://arxiv.org/pdf/2610.05029)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SPACE-CLIPv2: Decoding Local Geometry from Frozen CLIP for Monocular Depth Estimation
- 作者：Hyun Song, Taewan Cho, Kangmin Kim, Andrew Jaeyong Choi
- 出版日期：2026-10-04T07:50:10Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.05029 ；PDF：https://arxiv.org/pdf/2610.05029

### 一句话总结
SPACE-CLIPv2 在冻结 CLIP 主干上，通过固定局部邻域 token 聚合与门控残差、token 空间高通分支，改进单目深度估计中的局部几何解码。

### 研究问题
论文关注：CLIP 等视觉-语言基础模型虽具强语义表示，但其 patch token 并非直接为稠密度量几何优化；SPACE-CLIP 已表明冻结 CLIP 特征可通过层组特征融合支持单目深度估计，但仍未解决“相邻 CLIP token 应如何组合以恢复精细局部结构”的问题。

### 核心思路/方法
提出 SPACE-CLIPv2，一种冻结主干深度解码器，在 CLIP token 空间聚合固定局部邻域。具体而言：在选定的解码器阶段，模型采样固定 token stencil，预测聚合权重，并通过门控残差更新注入响应；此外，token 空间高通分支用于保留浅层局部对比。论文还比较固定采样与学习偏移采样，并在 NYU Depth V2 上相对匹配的 SPACE-CLIP 基线改进；五种子实验一致偏向固定采样而非学习偏移采样。零样本 iBims-1 评估进一步改善边界和平面几何指标。

### 主要贡献
- 提出 SPACE-CLIPv2：在冻结 CLIP 特征上通过固定局部邻域 token 聚合来解码局部几何的深度解码器。
- 在选定解码器阶段引入固定 token stencil、预测聚合权重和门控残差更新机制。
- 引入 token 空间高通分支以保留浅层局部对比。
- 在 NYU Depth V2 上相对匹配 SPACE-CLIP 基线取得改进，并通过五种子实验支持固定采样优于学习偏移采样。
- 在零样本 iBims-1 评估中改善边界与平面几何指标。

### 局限性
摘要未提供足够信息。未提供关于模型规模、计算开销、失败场景、固定 stencil 设计选择依据、学习偏移采样劣势原因、其他数据集泛化表现等细节。

### 阅读优先级
中。理由：该工作聚焦冻结 CLIP 特征用于单目深度估计中的局部 token 聚合问题，问题定义清晰，且给出 NYU Depth V2 与零样本 iBims-1 上的摘要级结果；但摘要未展开方法细节、消融规模与完整实验设置，若研究兴趣直接涉及 CLIP 几何解码或单目深度估计，可优先阅读，否则可作为中等优先级参考。

</details>

<details>
<summary>Abstract</summary>

Vision-language foundation models such as CLIP provide strong semantic representations, but their patch tokens are not directly optimized for dense metric geometry. SPACE-CLIP showed that frozen CLIP features can support monocular depth estimation through layer-group feature fusion, yet it leaves open how neighboring CLIP tokens should be combined to recover fine local structure. We present SPACE-CLIPv2, a frozen-backbone depth decoder that aggregates fixed local neighborhoods in CLIP token space. At selected decoder stages, the model samples a fixed token stencil, predicts aggregation weights, and injects the resulting response through a gated residual update. A token-space high-pass branch further preserves shallow local contrast. On NYU Depth V2, SPACE-CLIPv2 improves over a matched SPACE-CLIP baseline, while five-seed experiments consistently favor fixed over learned-offset sampling. Zero-shot iBims-1 evaluation further improves boundary and planar-geometry measures. These results support constrained local token aggregation as a practical mechanism for decoding geometry from frozen CLIP representations.

</details>

## Neural Scene Representations & Rendering

### 2026-10

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

#### 2026-10-07 - Gaussian Density Splatting Network

**Authors:** Miao Shang, Yabin Wang, Xiaopeng Hong
**Links:** [abs](https://arxiv.org/abs/2610.10396) - [pdf](https://arxiv.org/pdf/2610.10396)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Density Splatting Network
- 作者：Miao Shang, Yabin Wang, Xiaopeng Hong
- 出版日期：2026-10-07T16:48:58Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.10396) / [PDF](https://arxiv.org/pdf/2610.10396)

### 一句话总结
GDSNet 将人群计数从传统的网格化密度图预测，转变为连续 2D 高斯基元的叠加表示，并通过控制点拟合与可微高斯泼溅实现端到端训练。

### 研究问题
摘要指出，传统人群计数方法依赖基于网格的密度图，对空间分辨率较为敏感。论文试图用连续的高斯基元表示来替代这种网格化表示，以缓解分辨率敏感问题并提升计数性能。

### 核心思路/方法
- 将人群表示为一组连续 2D 高斯基元的叠加，而非网格化的密度图。
- 提出基于控制点的拟合机制：分配一组控制点来定义局部区域，从这些区域汇聚特征，用于回归每个高斯基元的参数。
- 改造可微高斯泼溅框架以适配计数任务：每个基元由几何参数和一个标量密度质量参数化。
- 通过可微渲染密度图的空间匹配进行端到端训练，同时提供局部密度监督和全局计数优化。

### 主要贡献
- 提出 GDSNet，一种基于连续 2D 高斯基元叠加的人群计数新方法。
- 引入基于控制点的拟合机制，用于结构化预测高斯参数。
- 将可微高斯泼溅框架适配到计数任务，实现密度图空间匹配下的端到端训练，并同时支持局部密度监督与全局计数优化。
- 在四个标准基准上进行了广泛评估，摘要称 GDSNet 持续优于当前最优方法。

### 局限性
- 摘要未提供足够信息说明具体实验设置、基准名称、评价指标细节及消融实验情况。
- 摘要未提供足够信息说明方法在极端密集场景、遮挡严重场景或跨域泛化方面的表现。
- 摘要未提供足够信息说明控制点数量选择、高斯基元数量设定及计算开销等实现细节。
- 摘要未提供足够信息说明与现有方法相比的具体性能提升幅度。

### 阅读优先级
高。理由：该论文提出了一种区别于传统网格密度图的人群计数表示方式，结合了控制点拟合与可微高斯泼溅，属于表示形式上的创新；且摘要声称在四个标准基准上持续超越当前最优方法，对人群计数和神经场景表示交叉方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

This paper proposes a novel crowd counting approach, the Gaussian Density Splatting Network (GDSNet). Unlike methods that rely on conventional, grid-based density maps and are sensitive to spatial resolution, GDSNet represents a crowd as a superposition of continuous 2D Gaussian primitives. Our approach is built upon two key contributions. First, we introduce a control-point-based fitting mechanism to structure the prediction of the Gaussian parameters. We design a method to allocate a set of control points that define local regions, from which features are pooled to regress each primitive's parameters. Second, we adapt a differentiable Gaussian Splatting framework to the counting task by parameterizing each primitive with geometric parameters and a scalar density mass. This formulation allows the network to be trained end-to-end via spatial matching of differentiably rendered density maps, naturally providing both local density supervision and global count optimization. Extensive evaluations on four standard benchmarks show GDSNet consistently outperforms the state of the art.

</details>

#### 2026-10-07 - NeRFifyMesh: Optimizing Neural Radiance Fields from Textured Meshes for Robotics Scene Building

**Authors:** Nillan Nimal, Mahboubeh Asadi, Sajad Saeedi
**Links:** [abs](https://arxiv.org/abs/2610.10387) - [pdf](https://arxiv.org/pdf/2610.10387)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** NeRF, radiance field, scene representation, rendering, radiance, robotics, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NeRFifyMesh: Optimizing Neural Radiance Fields from Textured Meshes for Robotics Scene Building
- 作者：Nillan Nimal, Mahboubeh Asadi, Sajad Saeedi
- 出版日期：2026-10-07T16:45:16Z
- 分类：主分类为 Neural Scene Representations & Rendering；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.10387) / [PDF](https://arxiv.org/pdf/2610.10387)

### 一句话总结
该论文提出一种将已有带纹理网格模型转换为 NeRF 表示的新流程，通过采样网格几何与纹理人工生成基于点的真值辐射场，以避免基于相机的采样或多视角渲染。

### 研究问题
在机器人领域，场景表示对环境理解与交互至关重要。NeRF 及其变体作为新颖表示推动了相关研究。在语义建图与仿真等应用中，机器人研究者希望使用多个 NeRF 模型来构建场景，每个模型代表一个物体。尽管已有大量 3D 网格模型数据集，但仍迫切需要工具将这些资产转换为 NeRF 模型，以支持快速算法开发与测试。摘要未提供足够信息说明现有转换方法的具体不足或量化瓶颈。

### 核心思路/方法
论文提出一种新流程，用于将现有网格模型转换为 NeRF 表示。其核心是：通过采样网格几何和纹理，人工生成基于点的真值辐射场。该方法避免了为训练 NeRF 模型而进行基于相机的采样，或渲染原始网格的多视角图像。摘要未提供足够信息说明采样策略、网络结构、训练细节或优化方式。

### 主要贡献
- 提出一种将已有带纹理网格模型转换为 NeRF 表示的新流程。
- 通过采样网格几何与纹理人工生成基于点的真值辐射场，从而避免基于相机的采样或多视角渲染来训练 NeRF。
- 广泛基准测试表明，该方法可取得与基线相当的渲染质量。
- 展示了该表示的应用：构建统一 NeRF 场景，并使用提取的几何进行碰撞仿真。

### 局限性
摘要未提供足够信息说明方法的计算开销、对网格质量或纹理质量的依赖、泛化能力、失败案例、与基线对比的具体指标、碰撞仿真的精度或实时性等局限。摘要仅提到渲染质量与基线相当，未说明是否在全部指标上占优或存在明显不足。

### 阅读优先级
中。理由：该工作面向机器人场景构建，提出将已有网格资产转换为 NeRF 的流程，并涉及统一场景构建与碰撞仿真，对机器人仿真与语义建图方向有潜在应用价值。但摘要未提供具体方法细节、定量对比与局限信息，若读者关注 NeRF 资产转换或机器人场景表示，可优先阅读；若仅关注通用 NeRF 渲染性能，则优先级一般。

</details>

<details>
<summary>Abstract</summary>

In robotics, scene representation plays a pivotal role in understanding and interacting with the environment. The advent of Neural Radiance Fields (NeRF) and its variants, as a novel representation, has opened a new frontier of research. In applications such as semantic mapping and simulation, roboticists aim to build scenes using multiple NeRF models, each representing an object. While extensive datasets of 3D mesh models already exist, there is an urgent need to develop tools to convert these assets to NeRF models for rapid algorithm development and testing. This paper presents a new pipeline for converting existing mesh models to NeRF representations by artificially generating a ground truth point-based radiance field through sampling mesh geometry and texture. This approach alleviates the need for camera-based sampling or rendering multi-view images of the original mesh to train the NeRF model. Extensive benchmarking demonstrates that our method yields comparable rendering quality to the baselines. Additionally, the application of this representation is shown by constructing unified NeRF scenes and performing collision simulations with extracted geometry.

</details>

#### 2026-10-07 - DeltaSplat: Iterative Gaussian Refinement for Pose-Free Feed-Forward 3D Gaussian Splatting

**Authors:** Chanung Park, Seunghyeon Song, Joo Chan Lee, Eunbyung Park, Jong Hwan Ko
**Links:** [abs](https://arxiv.org/abs/2610.09853) - [pdf](https://arxiv.org/pdf/2610.09853)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** camera calibration, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DeltaSplat: Iterative Gaussian Refinement for Pose-Free Feed-Forward 3D Gaussian Splatting
- 作者：Chanung Park, Seunghyeon Song, Joo Chan Lee, Eunbyung Park, Jong Hwan Ko
- 出版日期：2026-10-07T11:11:22Z
- 分类：primary: Neural Scene Representations & Rendering；secondary: 未提供
- 链接：摘要页 https://arxiv.org/abs/2610.09853；PDF https://arxiv.org/pdf/2610.09853

### 一句话总结
DeltaSplat 提出一种轻量级高斯精修模块，通过迭代渲染与残差预测，纠正无位姿前馈 3DGS 中由相机估计误差传播导致的高斯几何与光度偏差。

### 研究问题
无位姿前馈 3D Gaussian Splatting 虽能摆脱相机标定与逐场景优化，但相机估计误差会传播到预测的高斯上，并加剧单次前馈预测的几何与光度不准确问题。论文要解决的核心问题是如何修正这些误差。

### 核心思路/方法
- 引入 DeltaSplat，一个面向无位姿前馈 3DGS 的轻量级高斯精修模块。
- 在输入上下文视角上迭代渲染当前高斯，并根据渲染残差预测每个高斯的更新量。
- 针对仅用 2D 残差无法充分确定 3D 修正的问题，方法以逐像素 Plücker 射线和渲染深度作为软几何先验来条件化每次更新。
- 使用双分支卷积混合器高效编码输入，并通过逐属性头将融合特征解码为位置、不透明度和颜色更新。
- 该模块仅给骨干网络增加约 2.2% 参数，推理时仍保持完全前馈。

### 主要贡献
- 提出 DeltaSplat 轻量级高斯精修模块，用于纠正无位姿前馈 3DGS 的误差传播。
- 设计迭代渲染—残差预测—逐高斯更新机制，并引入 Plücker 射线与渲染深度作为软几何先验，以缓解 2D 残差对 3D 修正欠定的问题。
- 在 DL3DV 上，无位姿设置达到 26.64 dB PSNR，比其最先进骨干提升 1.75 dB，并超过部分使用真值相机的基线；在 6–24 视图和所有相机模式下均保持一致增益。

### 局限性
摘要未提供足够信息。摘要未说明方法在更广泛数据集、极端稀疏视图、动态场景、不同骨干泛化性、计算时延或失败案例等方面的表现。

### 阅读优先级
高。理由：该论文直接针对无位姿前馈 3DGS 的关键误差传播问题，提出的精修模块参数开销小且保持前馈推理，并在摘要中报告了明确的定量提升与跨视图、跨相机模式的稳定性，主题与神经场景表示和渲染方向高度相关。

</details>

<details>
<summary>Abstract</summary>

Pose-free feed-forward 3D Gaussian Splatting (3DGS) reconstructs a scene from sparse, unposed images in a single network pass, removing the need for camera calibration and per-scene optimization. However, camera estimation errors propagate into the predicted Gaussians and compound the geometric and photometric inaccuracies of single-pass prediction. To correct these errors, we introduce DeltaSplat, a lightweight Gaussian refinement module for pose-free feed-forward 3DGS. It iteratively renders the current Gaussians at the input context views and predicts per-Gaussian updates from the resulting residuals. A 2D residual alone, however, underdetermines the 3D correction. DeltaSplat therefore conditions each update on per-pixel Plücker rays and rendered depth as a soft geometric prior. A dual-branch convolutional mixer efficiently encodes these inputs, and per-attribute heads decode the fused features into position, opacity, and color updates. The module adds only ~2.2% parameters to the backbone and remains fully feed-forward at inference. On DL3DV, DeltaSplat reaches 26.64 dB PSNR in the pose-free setting, improving its state-of-the-art backbone by 1.75 dB and surpassing even baselines supplied with ground-truth cameras; consistent gains hold across 6-24 views and all camera regimes.

</details>

#### 2026-10-07 - TileSkipper: Region-Adaptive Tile Pruning for 3D Gaussian Splatting

**Authors:** Jingxing Li, Yongjae Lee, Deliang Fan, Abhay Kumar Yadav, Cheng Peng, Rama Chellappa
**Links:** [abs](https://arxiv.org/abs/2610.09343) - [pdf](https://arxiv.org/pdf/2610.09343)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TileSkipper: Region-Adaptive Tile Pruning for 3D Gaussian Splatting
- 作者：Jingxing Li, Yongjae Lee, Deliang Fan, Abhay Kumar Yadav, Cheng Peng, Rama Chellappa
- 出版日期：2026-10-07T03:01:51Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.09343 ；PDF：https://arxiv.org/pdf/2610.09343

### 一句话总结
TileSkipper 面向冻结的 3D Gaussian Splatting 检查点，通过校准为每个 Gaussian 分配静态 cutoff 策略，在 Tile 枚举中跳过低贡献区域，从而在不更新参数、不增加 kernel、不做逐帧策略推断的前提下实现区域自适应的 Tile 剪枝与渲染加速。

### 研究问题
Tiled 3D Gaussian Splatting 光栅化器在枚举 Tile 时通常对所有场景内容使用统一的全局贡献 cutoff，但不同内容对支持截断的敏感程度并不相同。论文试图解决：如何在不改变模型参数、不引入额外 kernel 的情况下，为不同 Gaussian 区域分配更合适的 cutoff，以减少 Tile 枚举中的候选配对开销，同时控制渲染质量损失。

### 核心思路/方法
TileSkipper 为冻结检查点选择静态的 per-Gaussian cutoff 策略。其校准渲染过程会测量候选配对节省量，并估计一个孤立移除的失真代理，该代理考虑前向透射率和背景颜色。方法在 64 个 Gaussian 分组之间分配 cutoff，并且只在互不重叠的选择视图上完成完整渲染后才接受策略。导出的策略每个 Gaussian 使用一个字节，不需要参数更新、额外 kernel 或逐帧策略推断。

### 主要贡献
- 提出 TileSkipper，一种针对 Tiled 3D Gaussian Splatting 的区域自适应 Tile 剪枝方法，通过静态 per-Gaussian cutoff 策略跳过低贡献 Tile 枚举。
- 使用校准渲染测量候选配对节省量与孤立移除失真代理，并将该代理与前向透射率和背景颜色关联。
- 在 64 个 Gaussian 分组间分配 cutoff，并通过互不重叠选择视图上的完整渲染来筛选策略。
- 导出的策略空间开销为每个 Gaussian 一字节，且不涉及参数更新、额外 kernel 或逐帧策略推断。
- 在 Mip-NeRF 360、Tanks & Temples 和 Deep Blending 的 13 个场景上，固定策略 AccuTile sweep 取得数据集宏平均加速：标准分辨率 $1.088\times$，3840 像素宽 $1.238\times$，平均 PSNR 变化分别为 $-0.007/-0.023$ dB。
- 与现有 opacity-aware bounds 的六种集成带来 $1.009\times$--$1.121\times$ 的纯编译器加速；对来自 $3σ$ 光栅化器的四个移植版本，分别归因于先前的精确边界转换与本文的增量收益。
- 匹配质量消融显示，相较场景全局校准有适度收益，与 per-Gaussian 控制持平；与 AdaGScale 的独立比较则依赖具体情景。

### 局限性
摘要未提供足够信息来说明 TileSkipper 在更多数据集、更多分辨率、不同硬件或不同光栅化器实现下的泛化表现。摘要未提供足够信息来说明校准成本、选择视图数量、策略过拟合风险以及对动态场景或非冻结检查点的适用性。摘要未提供足够信息来完整解释与 AdaGScale 比较中“regime-dependent”的具体条件与结论边界。

### 阅读优先级
中。理由：该论文聚焦 3D Gaussian Splatting 渲染效率优化，问题明确，方法具有工程可部署特征（每 Gaussian 一字节、无参数更新、无额外 kernel、无逐帧推断），并给出多数据集加速与 PSNR 变化数据；但摘要未展开校准成本、泛化细节和部分对比条件，若关注 3DGS 加速与系统集成，值得阅读；若仅关注新场景表示建模或训练方法，则优先级相对较低。

</details>

<details>
<summary>Abstract</summary>

Tiled 3D Gaussian Splatting rasterizers often use one scene-wide contribution cutoff for tile enumeration, although content differs in its sensitivity to support truncation. TileSkipper selects a static per-Gaussian cutoff policy for a frozen checkpoint. Calibration renders measure candidate pair savings and an isolated-removal distortion proxy that accounts for front transmittance and background color. The method allocates cutoffs across 64 Gaussian groups and accepts policies only after complete renders on disjoint selection views. The exported policy uses one byte per Gaussian, with no parameter updates, additional kernel, or per-frame policy inference. Across 13 scenes from Mip-NeRF 360, Tanks & Temples, and Deep Blending, a fixed-policy AccuTile sweep gives dataset-macro speedups of $1.088\times$ at standard resolution and $1.238\times$ at 3840 pixels wide, with $-0.007/-0.023$ dB mean PSNR change. Six integrations with existing opacity-aware bounds yield $1.009\times$--$1.121\times$ compiler-only speedups. For four ports from $3σ$ rasterizers, we separately attribute the prior exact-bound transition and our incremental gain. Matched-quality ablations show modest gains over scene-global calibration and parity with per-Gaussian control; the standalone comparison with AdaGScale is regime-dependent.

</details>

#### 2026-10-06 - RDGSplat: Render-Dedicated Geometry for Novel View Synthesis

**Authors:** Zhijie Zheng, Xinhao Xiang, Jiawei Zhang
**Links:** [abs](https://arxiv.org/abs/2610.09173) - [pdf](https://arxiv.org/pdf/2610.09173)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RDGSplat: Render-Dedicated Geometry for Novel View Synthesis
- 作者：Zhijie Zheng, Xinhao Xiang, Jiawei Zhang
- 出版日期：2026-10-06T22:18:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.09173) / [PDF](https://arxiv.org/pdf/2610.09173)

### 一句话总结
RDGSplat 在冻结的 3D 基础模型上额外解码出一套专用于渲染的几何表示，从而在不破坏原有度量预测的前提下提升新视角合成质量。

### 研究问题
论文指出，3D 基础模型通过在已有重建表示上挂接高斯头来实现高效新视角合成，但其渲染出的视角质量与模型恢复出的几何不匹配。原因在于：该几何是在度量目标下估计的，从未以“渲染效果”为标准进行评分。近期方法通过更新主干权重来缓解该问题，但这会丢弃模型原本用于度量预测的能力，并且每换一个新主干都需要重复训练。

### 核心思路/方法
- 提出 RDGSplat 框架，从冻结的 3D 基础模型中解码出第二套专用于渲染的几何，同时保持其度量预测不变。
- **Render-Dedicated Geometry Decoding**：复制预训练解码器，并仅在光度监督下优化这些副本。
- **Target-Pose Conditioned Adapter**：重新构造这些解码器所读取的表示，使其以目标相机位姿而非目标图像为条件。

### 主要贡献
- 提出在冻结主干下为渲染专门解码几何的框架，避免更新主干权重。
- 设计 Render-Dedicated Geometry Decoding，通过复制并光度监督优化解码器副本。
- 引入 Target-Pose Conditioned Adapter，将解码器读取的表示改写为以目标相机位姿为条件。
- 在四个基准、三个前馈主干上验证了新视角合成的提升，且所有预训练权重保持冻结。摘要给出的具体结果为：在 RE10K 上，WM2.0 从 20.918 dB 提升至 24.266 dB，新增训练参数 205.5 M，对应冻结的 1.4 B 主干；同一模型预测的深度和位姿保持不变。

### 局限性
- 摘要未提供足够信息说明方法在非前馈式主干、动态场景或更大规模数据集上的表现。
- 摘要未提供足够信息说明额外解码器与适配器带来的推理开销或显存代价。
- 摘要未提供足够信息说明光度监督之外是否需要其他正则或约束。
- 摘要未提供足够信息说明失败案例或对目标位姿分布外情况的鲁棒性。

### 阅读优先级
高。理由：该工作针对“冻结 3D 基础模型下渲染质量与度量几何解耦”这一明确问题，提出了保持预训练权重不变的轻量适配方案，并给出了跨三个主干、四个基准的实验结果；若关注基础模型复用、新视角合成或几何与渲染目标冲突，具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

3D foundation models enable efficient novel view synthesis by carrying a Gaussian head on the representation they already use for reconstruction. However, the views they render fall short of the geometry they recover, because that geometry is estimated under a metric objective and never scored on how it renders. Recent methods alleviate this by updating the backbone weights, but they thereby discard the metric predictions the model was built for and must be repeated for every new backbone. To this end, we propose RDGSplat, a framework that decodes a second geometry dedicated to rendering from a frozen 3D foundation model, leaving its metric predictions intact. In particular, we devise Render-Dedicated Geometry Decoding, which duplicates the pretrained decoders and optimizes the duplicates under photometric supervision alone. Then, a Target-Pose Conditioned Adapter is introduced to reformulate the representation those decoders read, conditioned on the target camera pose rather than the target image. Extensive experiments show that RDGSplat improves novel view synthesis across three feed-forward backbones on four benchmarks, with every pretrained weight frozen. On RE10K, it raises WM2.0 from 20.918 to 24.266\,dB while training 205.5\,M added parameters against a frozen 1.4\,B backbone, and the depth and pose the same model predicts are unchanged.

</details>

#### 2026-10-06 - SPLATIFY: Reproduce, Discover, Innovate! From Papers and Ideas to Trainable 3DGS Code

**Authors:** Seemandhar Jain, Keshav Gupta, Manmohan Chandraker
**Links:** [abs](https://arxiv.org/abs/2610.09116) - [pdf](https://arxiv.org/pdf/2610.09116)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SPLATIFY: Reproduce, Discover, Innovate! From Papers and Ideas to Trainable 3DGS Code
- 作者：Seemandhar Jain, Keshav Gupta, Manmohan Chandraker
- 出版日期：2026-10-06T21:06:33Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.09116

### 一句话总结
SPLATIFY 是一个多智能体框架，旨在将 3D Gaussian Splatting（3DGS）论文自动转化为基于 gsplat 的可训练代码，并在无公开代码的论文上达到专家实现水平，同时支持组合式改进与跨学科方法发现。

### 研究问题
3DGS 研究快速增长，在已有工作上继续推进前，往往需要投入大量精力重新复现论文。通用论文到代码的方法以及前沿模型在此场景下均会失败，因此需要一种针对 3DGS 论文的自动化、可训练代码生成方案。

### 核心思路/方法
SPLATIFY 是一个多智能体框架，将 3DGS 论文转换为基于 gsplat 的可训练实现，包含五项创新：
1. 针对 gsplat 的上下文无关文法，建立在模块化方法模板之上，并为损失、致密化、渲染和优化提供扩展点，通过构造约束生成代码以满足 gsplat 的架构不变量。
2. 用于忠实复现的架构要素：fork 感知的引用恢复，以函数级粒度检索组件级代码；按拓扑依赖顺序进行 Graph-of-Thought 合成；从 20 多个已验证实现中进行 RAG 引导的上下文示例选择；以及结合 PSNR 引导的重新生成、高斯级结构检查和 VLM 驱动补丁的视觉反馈。
3. 知识驱动的组合式改进：自主发现弱点，并组合互补的正则化器、损失和致密化策略，以改进原始结果。
4. 跨学科方法发现：智能体从 3DGS 文献之外检索物理先验，并将其与渲染知识组合，为此前未处理的场景类型生成方法。
5. SPLATIFY-Bench：覆盖 30 篇多样化 3DGS 论文的评估框架。

### 主要贡献
- 提出 SPLATIFY 多智能体框架，将 3DGS 论文转化为可训练的 gsplat 实现。
- 通过五项创新（文法约束、忠实复现架构、组合式改进、跨学科发现、SPLATIFY-Bench）支撑论文到代码的转化、复现与创新。
- 在无公开代码的论文上，SPLATIFY 达到专家实现水平，并将开发时间从数周缩短到数分钟。
- 通过组合式发现，PSNR 最高提升 2.4 dB。
- 展示了完全由 SPLATIFY 合成的新方法，用于体积星云渲染及其他科学领域。

### 局限性
摘要未提供足够信息（未说明失败案例、计算开销、对非 gsplat 后端的适用性、评估局限或人工干预程度等）。

### 阅读优先级
高。理由：该工作直面 3DGS 研究中论文复现成本高的痛点，提出多智能体自动生成可训练代码的框架，并包含基准、组合式改进和跨学科发现，对 3DGS 及论文到代码自动化方向均具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

The rapid growth of 3D Gaussian Splatting (3DGS) research demands significant effort to reimplement papers before building on them. We introduce SPLATIFY, a multi-agent framework that converts 3DGS papers into trainable gsplat-based implementations, where generic paper-to-code methods and frontier models fail. SPLATIFY achieves this through five innovations: (1) A context-free grammar for gsplat over a modular method template with extension points for losses, densification, rendering, and optimization, constraining synthesis so generated code satisfies gsplat's architectural invariants by construction. (2) Architectural elements for faithful reproduction: fork-aware citation recovery retrieving component-level code at function-level granularity, Graph-of-Thought synthesis in topological dependency order, RAG-guided in-context example selection from over 20 verified implementations, and visual feedback combining PSNR-guided regeneration, Gaussian-level structural checks, and VLM-driven patching. (3) Knowledge-driven compositional improvement that autonomously finds weaknesses and composes complementary regularizers, losses, and densification strategies to improve upon original results. (4) Interdisciplinary method discovery where agents retrieve physical priors from outside the 3DGS literature and compose them with rendering knowledge to produce methods for previously unaddressed scene types. (5) SPLATIFY-Bench, an evaluation framework across 30 diverse 3DGS papers. On papers without public code, SPLATIFY matches expert implementations while reducing development time from weeks to minutes, and through compositional discovery further improves PSNR by up to 2.4 dB. We additionally demonstrate novel methods for volumetric nebula rendering and other scientific domains, synthesized entirely by SPLATIFY.

</details>

#### 2026-10-06 - Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error

**Authors:** Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González
**Links:** [abs](https://arxiv.org/abs/2610.08756) - [pdf](https://arxiv.org/pdf/2610.08756)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Transfer Error
- 作者：Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González
- 出版日期：2026-10-06T17:47:47Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.08756) | [PDF](https://arxiv.org/pdf/2610.08756)

### 一句话总结
提出一种面向 3D Gaussian Splatting 的后训练语义提升方法，通过跨视角累积目标/非目标证据并按可见性加权，再用双阈值过滤高斯，从而将 2D 检测器、语义提升与表示间标签迁移三类误差分离开来。

### 研究问题
3D Gaussian Splatting 中的同一个高斯会被多个视角观测，但不同视角对其类别的判断并不总是一致：有些视角下该高斯被遮挡，检测器在不同视角下的置信度也不同。此外，真值以带标注的网格形式给出，因为两次训练运行不会产生相同的高斯。因此论文关注如何在多视角不一致、遮挡与置信度差异下进行语义提升，并区分误差来源。

### 核心思路/方法
- 提出一种后训练（post-training）语义提升方法，每次处理一个目标类别。
- 同时累积“目标”和“非目标”证据，并按每个高斯在每个视角中的可见性进行加权。
- 高斯过滤使用两个阈值：主阈值 β 选取高置信度种子，较低的阈值 γβ 用于补充其周围的连通分量。
- 评估时将标签从高斯迁移到既可见又有标注的网格顶点。
- 该设计可分离三类误差来源：2D 检测器、语义提升、以及两种表示之间的标签迁移。
- 阈值与迁移算子基于七个 Replica 验证场景选择，并在十个留出的 ScanNet++ 场景上以对所有场景和类别相同的取值进行评估。

### 主要贡献
- 提出一种跨视角融合、按可见性加权的后训练语义提升方法，一次处理一个目标类别。
- 采用双阈值策略（β 与 γβ）过滤高斯，兼顾高置信种子与周围连通分量。
- 通过将标签从高斯迁移到可见且标注的网格顶点，实现对三类误差来源的分离分析。
- 与逐视角阈值化证据的先前版本相比，该方法在测试 mIoU 上提升 0.24，并使两个数据集的所有类别和场景可共用一个单一阈值。
- 误差分析显示，剩余误差主要来自检测器。

### 局限性
- 摘要未提供足够信息说明方法对更多类别、更复杂场景或不同类型检测器的泛化能力。
- 摘要未提供足够信息说明双阈值 β 与 γβ 的具体取值、敏感性或调参成本。
- 摘要未提供足够信息说明在遮挡严重或视角一致性极差情况下的具体失败模式。
- 摘要未提供足够信息说明训练时间、推理开销或计算资源需求。
- 摘要未提供足够信息说明与更多现有语义提升方法的全面对比。

### 阅读优先级
中。理由：该工作聚焦 3D Gaussian Splatting 的语义提升与误差分解，问题定义清晰，且给出跨数据集的量化结果（验证集 mIoU 0.93/0.65，测试集 0.80/0.54），对关注 3D 语义表示与误差分析的研究者有参考价值；但摘要未展示与广泛基线方法的系统对比，也未提供方法细节与开源信息，因此优先级为中等。

</details>

<details>
<summary>Abstract</summary>

The same Gaussian of a 3D Gaussian Splatting model is seen from many views, and these views do not always agree on the class it belongs to. The Gaussian may be occluded in some of them, and the confidence of the detector is not the same from one view to another. The ground truth, on the other hand, is given as an annotated mesh, because two training runs do not produce the same Gaussians. In this work, we propose a post-training lifting method that works with one target class at a time and combines the information coming from all the views. Target and non-target evidence are accumulated simultaneously, weighted by the visibility of each Gaussian in each view. After that, the Gaussians are filtered with two thresholds: a main threshold $β$ selects the high-confidence seeds, and a lower one $γβ$ adds the connected components around them. For the evaluation, the labels are transferred from the Gaussians to the mesh vertices that are both visible and annotated. With this design, we can separate three sources of error: the 2D detector, the lifting and the transfer between representations. The thresholds and the transfer operator are chosen on seven Replica validation scenes, and the method is evaluated on ten held-out ScanNet++ scenes with the same values for every scene and class. The mean mIoU on the validation scenes was 0.93 with masks from the dataset annotations and 0.65 with YOLO masks, and on the ScanNet++ test scenes it was 0.80 and 0.54. Compared with thresholding the evidence per view, as a previous version of the method did, the fraction improves the test mIoU by 0.24 and makes it possible to use a single threshold for all the classes and scenes of both datasets. Finally, the error analysis shows that most of the remaining error comes from the detector.

</details>

#### 2026-10-06 - DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given

**Authors:** Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee
**Links:** [abs](https://arxiv.org/abs/2610.07958) - [pdf](https://arxiv.org/pdf/2610.07958)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given
- 作者：Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee
- 出版日期：2026-10-06T08:29:41Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.07958) | [PDF](https://arxiv.org/pdf/2610.07958)

### 一句话总结
DensiTok 是一个可插拔模块，通过在低维隐空间中补全前馈 3DGS 模型内部几何 token，使冻结骨干网络在稀疏视角输入下表现出“看到更多视角”的效果。

### 研究问题
前馈 3D Gaussian Splatting（3DGS）通过单次前向传播重建场景，但其质量在输入图像数量减少时会急剧下降。摘要指出，瓶颈位于重建头之前：从少量无位姿视角出发，模型内部表示中缺乏未观测区域的证据，导致空洞、浮点和模糊。常见做法是用图像或视频生成器合成额外视角像素再重新编码，但这种方式成本高，且本身不具备 3D 一致性。

### 核心思路/方法
- 不合成额外图像像素，而是“加密证据本身”，即直接对内部几何 token 进行致密化。
- DensiTok 作为预训练前馈 3DGS 模型的插件模块，保持骨干网络和重建头冻结。
- 将几何 token 压缩到紧凑隐空间，在相机几何条件下以单步 flow-matching 补全未观测视角的隐变量，再解码回 token 供原重建头使用。
- 由于在低维隐空间完成补全，不需要图像合成，也不需要额外编码器前向传播。
- 同一模块设计可集成到不同的预训练预测器中。

### 主要贡献
- 提出 DensiTok，一种直接致密化前馈 3DGS 内部几何 token 的插件模块。
- 通过隐空间补全而非像素合成来提供未观测区域证据，避免额外图像生成与重新编码开销。
- 在保持各骨干网络及其重建头冻结的情况下，可集成到不同预训练预测器中。
- 摘要称在三个预训练骨干和两个基准上，DensiTok 一致改善稀疏视角重建，并缩小了与密集视角重建的差距。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算开销细节、对相机位姿质量的依赖程度、隐空间补全的误差上界，以及在不同数据集或极端稀疏条件下的泛化表现。实验细节、消融结果和定量指标均未在摘要中给出。

### 阅读优先级
中。理由：该工作针对前馈 3DGS 在稀疏视角下的关键瓶颈提出模块化、免图像合成的隐空间补全思路，且声称跨多个骨干和基准一致有效，具有较强的问题针对性和方法普适性；但摘要未给出实验细节、定量结果与失败案例分析，需进一步阅读正文才能判断其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) reconstructs a scene in a single forward pass, replacing per-scene optimization with a network trained across many scenes. Its quality, however, degrades sharply as the number of input images drops. The bottleneck is upstream of the reconstruction heads: from a few unposed views, the internal representation they read carries no evidence for unobserved regions, leaving holes, floaters, and blur. The common remedy supplies that evidence as pixels, synthesizing extra views with an image or video generator and re-encoding them, which is costly and not 3D-consistent by construction. We instead densify the evidence itself. We present DensiTok, a plug-in module for pretrained feed-forward 3DGS models that densifies their internal geometry tokens directly, making a frozen backbone behave as though it had observed many more views than it was given. DensiTok compresses those tokens into a compact latent space, completes the latents of the unobserved viewpoints in a single flow-matching step conditioned on camera geometry, and decodes them back into tokens that the original reconstruction heads. The same module design can be integrated into different pretrained predictors while keeping each backbone and its reconstruction heads frozen. Completion in a low-dimensional latent space requires no image synthesis or additional encoder passes. Across three pretrained backbones and two benchmarks, DensiTok consistently improves sparse-view reconstruction and recovers much of the gap to dense-view reconstruction.

</details>

#### 2026-10-06 - Efficient Gaussian Splatting Sequence Compression with Standard Video Codecs

**Authors:** Qi Yang, Shuting Xia, Le Yang, Geert Van Der Auwera, Zhu Li
**Links:** [abs](https://arxiv.org/abs/2610.07795) - [pdf](https://arxiv.org/pdf/2610.07795)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Efficient Gaussian Splatting Sequence Compression with Standard Video Codecs
- 作者：Qi Yang, Shuting Xia, Le Yang, Geert Van Der Auwera, Zhu Li
- 出版日期：2026-10-06T05:43:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2610.07795 ；PDF 链接 https://arxiv.org/pdf/2610.07795 ；代码 https://github.com/Qi-Yangsjtu/GSCV

### 一句话总结
论文提出 GSCV，一种利用标准视频编解码器压缩高斯泼溅（GS）序列的方法，通过 Inter-PLAS 增强 GS 图像在 I 帧与 P 帧之间的帧间相关性，并采用高比特深度 GS 图像的新流程提升可压缩性与质量上限。

### 研究问题
论文关注 GS 序列压缩问题。摘要指出，现有基于视频的 GS 序列压缩依赖 Parallel Linear Assignment Sorting（PLAS）和被跟踪的基元信息，将 GS 转换为平滑的 2D 视频；但在大多数实际应用中，被跟踪信息并不可用。缺少该信息时，直接使用原始 PLAS 会因其随机性导致生成图像的帧间相关性较弱，从而影响视频编解码器的帧间压缩性能。

### 核心思路/方法
论文提出的方法名为 GSCV，用于 GS 序列压缩，并利用视频编解码器。针对原始 PLAS 在缺少被跟踪信息时帧间相关性弱的问题，GSCV 引入了一种简单而高效的 Inter-PLAS 方法，使 GS 在 I 帧和 P 帧之间生成更接近的图像，从而显著增强视频编解码器的帧间性能。此外，GSCV 基于最先进的视频编解码器实现了一个新流程，处理高比特深度 GS 图像，从而在提供更高质量上限的同时实现更高的可压缩性。

### 主要贡献
- 提出 GSCV，一种利用标准视频编解码器进行 GS 序列压缩的有效方法。
- 提出 Inter-PLAS，用于在 I 帧与 P 帧之间生成更接近的 GS 图像，提升视频编解码器的帧间性能。
- 实现基于最先进视频编解码器与高比特深度 GS 图像的新流程，提升可压缩性并提供更高质量上限。
- 实验结果表明，GSCV 在 GS 序列压缩方面相较 MPEG 视频锚点和基于点云的锚点有明显提升。
- 公开代码链接。

### 局限性
摘要未提供足够信息说明 GSCV 的具体计算开销、实时性、对不同 GS 表示或数据集的泛化能力，以及与更多基线方法的完整对比细节。摘要未提供足够信息说明 Inter-PLAS 的具体实现细节和参数敏感性。摘要未提供足够信息说明高比特深度流程对兼容性和部署成本的影响。

### 阅读优先级
中。理由：该论文聚焦 GS 序列压缩与标准视频编解码器结合，问题明确，且摘要声称相较 MPEG 视频和点云锚点有性能提升，并公开代码，对 GS 压缩、视频编码和神经场景表示方向的研究者有参考价值。但用户未提供额外兴趣方向，且摘要未展开实验细节，因此优先级定为中而非高。

</details>

<details>
<summary>Abstract</summary>

This paper presents a novel effective Gaussian Splatting (GS) sequence Compression method that utilizes the Video codec (GSCV). Existing video-based GS sequence compression relies on the Parallel Linear Assignment Sorting (PLAS) and tracked primitive information to convert GS into smooth 2D videos. However, tracked information is not available for most practical applications, and without it, using the vanilla PLAS can generate images exhibiting weak inter-frame correlation, due to its stochastic nature. GSCV incorporates a simple yet efficient Inter-PLAS method to produce close images between the I- and P-frames of GS, enhancing the inter-frame performance of video codec greatly. GSCV also realizes a new pipeline based on the state-of-the-art video codecs with high bit-depth GS images, achieving higher compressibility while simultaneously providing a higher quality upper bound. Experimental results show that the proposed GSCV exhibits obviously improved performance over MPEG video and point cloud-based anchors in GS sequence compression. The code is available at https://github.com/Qi-Yangsjtu/GSCV.

</details>

#### 2026-10-06 - OntoPlan: An Ontology-Grounded Scene Representation and Agentic Framework for Scalable Robot Task Planning

**Authors:** Hyeongwoo Nam, Woongje Cho, Juwon Kim, Jongeun Choi
**Links:** [abs](https://arxiv.org/abs/2610.07649) - [pdf](https://arxiv.org/pdf/2610.07649)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OntoPlan: An Ontology-Grounded Scene Representation and Agentic Framework for Scalable Robot Task Planning
- 作者：Hyeongwoo Nam, Woongje Cho, Juwon Kim, Jongeun Choi
- 出版日期：2026-10-06T02:45:03Z
- 分类：Neural Scene Representations & Rendering（主分类；未提供次级分类）
- 链接：摘要页 https://arxiv.org/abs/2610.07649 ；PDF https://arxiv.org/pdf/2610.07649 ；代码 https://github.com/namhyeongwoo/OntoPlan

### 一句话总结
论文提出本体驱动的场景表示与智能体框架 OntoPlan，用共享符号词汇表达对象、空间、关系和状态，并选择性检索任务相关信息，以提升大环境下长程机器人任务规划的成功率并显著降低 token 开销。

### 研究问题
基于大语言模型（LLM）的机器人任务规划在开放式指令跟随上具有潜力，但在大环境中的长程任务上表现退化。具体问题包括：以文本向 LLM 传递空间信息时，模型可能无法捕捉空间上下文，且 token 成本随环境规模增长；直接用 LLM 生成动作序列也难以满足当前世界状态与动作前置条件。

### 核心思路/方法
论文从两方面回应上述问题：
1. **本体驱动的场景表示**：将对象、空间、关系与状态对齐到共享的符号词汇中，以支持空间推理与任务规划。
2. **OntoPlan 智能体框架**：解释指令、选择性检索与任务相关的信息、形式化目标与约束，并生成可执行计划。

### 主要贡献
- 提出本体驱动的场景表示，将对象、空间、关系和状态统一到共享符号词汇，用于空间推理和任务规划。
- 提出 OntoPlan 智能体框架，可解释指令、选择性检索任务相关信息、形式化目标与约束并产出可执行计划。
- 在覆盖五种室内环境、三种场景尺度的 150 个通用任务上，OntoPlan 平均任务成功率为 0.89，最强基线为 0.27；平均每任务总 token 为 18.1k，约为最高效基线的 1/5.6。
- 随着场景尺度增大，上述优势持续存在，而先前方法在成功率上下降更剧烈、token 成本仍远更高。
- OntoPlan 对模糊或不可行指令能通过追问或报告信息不足来恰当响应，而非强行给出无效计划。

### 局限性
- 摘要未提供足够信息说明实验的具体任务类型、环境构建方式、基线方法与评价细节。
- 摘要未提供足够信息说明本体构建成本、泛化边界、真实机器人部署情况或失败案例分析。
- 摘要未提供足够信息说明推理延迟、计算资源需求及不同 LLM 后端的影响。

### 阅读优先级
高。理由：该工作同时针对 LLM 机器人任务规划中的空间上下文丢失、世界状态与动作前置条件满足、以及环境规模扩大带来的 token 成本问题，给出了本体驱动场景表示与智能体框架；摘要报告了在 150 个任务、五种室内环境和三种场景尺度上的显著成功率与 token 效率优势，且涉及模糊/不可行指令处理，属于可扩展机器人任务规划方向的重要进展。

</details>

<details>
<summary>Abstract</summary>

Large language model (LLM)-based robot task planning is promising for open-ended instruction following, but degrades on long-horizon tasks in large environments. When spatial information is conveyed to the LLM through text, the model can fail to capture spatial context, and token cost grows with environment size. Generating action sequences directly with an LLM also makes it difficult to satisfy the current world state and action preconditions. We address this with an ontology-grounded scene representation that aligns objects, spaces, relations, and states in a shared symbolic vocabulary for spatial reasoning and task planning, and with OntoPlan, an agentic framework that interprets instructions, selectively retrieves task-relevant information, formalizes goals and constraints, and produces executable plans. Across 150 general tasks spanning five indoor environments and three scene scales, OntoPlan achieves 0.89 average task success, compared with 0.27 for the strongest baseline, while using 18.1k total tokens per task on average, about 5.6$\times$ fewer than the most efficient baseline. These advantages persist as scene scale increases, whereas prior methods degrade more sharply in success and remain far more costly in tokens. OntoPlan also responds appropriately to ambiguous or infeasible instructions by asking follow-up questions or reporting insufficient information rather than committing to invalid plans. Code available at https://github.com/namhyeongwoo/OntoPlan.

</details>

#### 2026-10-06 - OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception

**Authors:** Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam
**Links:** [abs](https://arxiv.org/abs/2610.07569) - [pdf](https://arxiv.org/pdf/2610.07569)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D mapping, Gaussian Splatting, 3D Gaussian Splatting, splatting, robotics, robot perception, mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception
- 作者：Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam
- 出版日期：2026-10-06T00:58:30Z
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（次）
- 链接：[摘要](https://arxiv.org/abs/2610.07569) | [PDF](https://arxiv.org/pdf/2610.07569) | [项目页](https://csiro-robotics.github.io/OpenSplatGraph)

### 一句话总结
OpenSplatGraph 提出一个统一框架，从基于高斯泼溅的在线开放词汇语义地图中直接构建持久的 3D 场景图，以同时支持语言引导的目标定位与结构化关系推理。

### 研究问题
论文针对机器人感知中的一个割裂问题：基于 3D Gaussian Splatting 的稠密语义建图虽能提供高保真几何与高效的开放词汇感知，但其语义通常表示为非结构化特征场，限制了以对象为中心的推理；而 3D 场景图虽能显式建模对象及其关系以支持结构化推理，但通常基于稀疏几何表示构建，未能充分利用稠密语义地图的信息。因此，核心问题是如何将稠密开放词汇语义建图与结构化对象中心表示紧密结合。

### 核心思路/方法
- 提出统一框架 OpenSplatGraph，从在线高斯式开放词汇语义地图中直接构建持久的 3D 场景图。
- 在稠密语义地图上引入“可靠性感知语义场”（reliability-aware semantic field），维护轻量级观测统计，用于置信度感知、查询条件化的对象提取。
- 将提取的对象实例关联到持久图节点，使对象属性与关系能够跨观测与查询增量更新。
- 通过紧密耦合稠密语义建图与持久对象中心表示，在保持高斯建图几何保真度的同时，支持语言引导的目标定位和结构化关系推理。

### 主要贡献
- 提出从稠密高斯开放词汇语义地图直接构建持久 3D 场景图的统一框架。
- 设计可靠性感知语义场与置信度感知、查询条件化的对象提取机制。
- 实现对象属性与关系随观测和查询进行增量更新的持久图节点关联。
- 据摘要所述，在标准 3D 场景理解基准和真实机器人实验中，该方法在在线开放词汇感知与下游机器人任务上取得了有竞争力的表现。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集规模、对比基线、评价指标及定量结果。
- 摘要未提供足够信息说明方法的计算开销、实时性、可扩展性或失败情形。
- 摘要未提供足够信息说明可靠性感知语义场的具体实现细节与超参数。
- 摘要未提供足够信息说明在真实机器人实验中的任务类型与具体表现。

### 阅读优先级
高。理由：该工作位于神经场景表示与机器人/具身智能的交叉点，直指稠密开放词汇建图与结构化场景图之间的关键衔接问题；若关注开放词汇机器人感知、3D 场景图或高斯泼溅建图，该文的问题设定与“可靠性感知 + 持久图节点”思路具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Dense 3D mapping with semantic understanding is essential for robotic perception in complex environments. Recent 3D Gaussian Splatting-based mapping approaches enable high-fidelity geometry and efficient open-vocabulary perception, but typically represent semantics as unstructured feature fields that limit object-centric reasoning. In contrast, 3D scene graphs explicitly model objects and their relationships for structured reasoning, but are commonly constructed from sparse geometric representations that do not fully exploit dense semantic maps. In this work, we present OpenSplatGraph, a unified framework that constructs persistent 3D scene graphs directly from an online Gaussian-based open-vocabulary semantic map. The proposed framework augments the dense semantic map with a reliability-aware semantic field that maintains lightweight observation statistics for confidence-aware, query-conditioned object extraction. Extracted object instances are associated with persistent graph nodes, allowing object attributes and relationships to be incrementally updated across observations and queries. By tightly coupling dense semantic mapping with persistent object-centric representations, our framework supports both language-guided object grounding and structured relational reasoning while preserving the geometric fidelity of Gaussian-based mapping. Comprehensive evaluations on standard 3D scene understanding benchmarks and real-world robotic experiments demonstrate that OpenSplatGraph achieves competitive performance for online open-vocabulary perception and downstream robotic tasks. Project page: https://csiro-robotics.github.io/OpenSplatGraph.

</details>

#### 2026-10-06 - AIMS: Anchor-Integrated Multi-View Synthesis for Scalable Novel View Rendering

**Authors:** JooHyun Park, HanYoung Jang, HyeongYeop Kang
**Links:** [abs](https://arxiv.org/abs/2610.07566) - [pdf](https://arxiv.org/pdf/2610.07566)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AIMS: Anchor-Integrated Multi-View Synthesis for Scalable Novel View Rendering
- 作者：JooHyun Park, HanYoung Jang, HyeongYeop Kang
- 出版日期：2026-10-06T00:54:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.07566) / [PDF](https://arxiv.org/pdf/2610.07566)

### 一句话总结
AIMS 通过“锚点视图 + 邻近观测融合”的解耦式设计，在保持下游全局合成视图预算固定的前提下利用更多输入观测，从而提升前馈新视角合成的可扩展性。

### 研究问题
前馈式新视角合成方法能从带位姿的多视角输入中获得较强泛化能力，但扩展到大规模输入视图集合时存在困难：
- 基于 Transformer 的方法联合处理所有输入视图 token，随视图数量增长，计算和内存开销迅速增加；
- 简单的视图子采样虽然降低开销，但会丢弃可能有用的观测信息。

因此，核心问题是如何在视图数量增长时，既控制全局合成模型的处理成本，又不浪费额外观测信息。

### 核心思路/方法
AIMS 提出一种可扩展框架，将“可用观测数量”与“全局合成模型处理的视图数量”解耦。具体包括：
- 使用最远点采样（farthest point sampling）选择一组固定数量、空间上分散的锚点视图；
- 将每个锚点附近的观测分组；
- 使用轻量级可学习整合器（learnable integrator）将各组观测信息融合为增强后的锚点表示；
- 这样额外观测可以参与合成，但下游全局视图预算保持固定。

### 主要贡献
- 提出 AIMS 框架，将输入观测规模与全局合成模型处理的视图数量解耦，以提升前馈新视角合成的可扩展性。
- 采用最远点采样选择空间分布的锚点视图，并用轻量级可学习整合器融合邻近观测，使额外观测信息可被利用而不增加全局视图预算。
- 在 RealEstate10K 和 ScanNet 上进行评估，展示了相对于 Transformer 类和高斯类基线在质量—效率权衡上的优势。
- 报告结果：两个数据集上 PSNR 分别为 29.41 dB 和 17.73 dB，渲染平均每视图 7.24 ms。

### 局限性
- 摘要未提供足够信息说明方法在不同规模输入视图集合下的具体扩展边界。
- 摘要未提供足够信息说明锚点数量、分组策略或整合器设计对性能的敏感性分析。
- 摘要未提供足够信息说明在更复杂场景、动态场景或极端视角变化下的表现。
- 摘要未提供足够信息说明与基线相比在内存占用、训练成本或推理总吞吐方面的完整细节。
- 摘要未提供足够信息说明失败案例或该方法不适用的情况。

### 阅读优先级
高。该论文关注前馈新视角合成中的可扩展性问题，提出的“锚点 + 邻近观测融合”思路明确针对 Transformer 类方法随视图数增长的计算/内存瓶颈，且摘要给出了具体数据集、PSNR 和渲染时间指标，对关注新视角合成、神经场景表示与渲染效率的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward novel view synthesis methods achieve strong generalization from posed multi-view inputs, but scaling them to large input view sets remains challenging. Transformer-based approaches that jointly process all input-view tokens incur rapidly increasing computation and memory as the number of views grows, while simple view subsampling discards potentially useful observations. We introduce Anchor-Integrated Multi-View Synthesis (AIMS), a scalable framework that decouples the number of available observations from the number of views processed by the global synthesis model. AIMS selects a fixed set of spatially distributed anchor views using farthest point sampling, groups nearby observations around each anchor, and uses a lightweight learnable integrator to fuse their information into enriched anchor representations. This allows additional observations to contribute to synthesis while keeping the downstream global view budget fixed. Evaluations on RealEstate10K and ScanNet demonstrate a favorable quality--efficiency trade-off against transformer-based and Gaussian-based baselines. AIMS achieves 29.41 dB and 17.73 dB PSNR on the two datasets, respectively, with rendering averaging 7.24 ms per view.

</details>

#### 2026-10-05 - Learnable Spectral Activations

**Authors:** Tamir Shor, Or Litany, Alex Bronstein
**Links:** [abs](https://arxiv.org/abs/2610.07419) - [pdf](https://arxiv.org/pdf/2610.07419)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural radiance field, radiance field, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learnable Spectral Activations
- 作者：Tamir Shor, Or Litany, Alex Bronstein
- 出版日期：2026-10-05T21:29:04Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.07419 ；PDF: https://arxiv.org/pdf/2610.07419

### 一句话总结
论文提出可学习谱激活（LSA），用残差截断傅里叶级数替代固定神经元级非线性，在不扩大渐近函数类的前提下改变表示分解方式，以改善隐式神经表示的重建质量。

### 研究问题
隐式神经表示（INRs）的表示能力受输入编码和激活函数所诱导的谱结构影响。现有方法主要通过坐标编码或周期性非线性来改变网络可用的频率，但摘要指出“频率可及性并非唯一瓶颈”：对于具有局部结构或空间变化结构的信号，网络还需要有效地将频率组合成多谐波内部响应。因此，问题在于如何让网络更有效地进行频率组合与谱塑形，而不仅仅是提供更多频率。

### 核心思路/方法
- 提出可学习谱激活（LSA），将固定的神经元级非线性替换为残差截断傅里叶级数。
- 该傅里叶级数的谐波振幅在训练过程中学习得到。
- LSA 不扩大渐近函数类，而是改变表示的分解方式：线性权重负责选择特征，激活系数负责控制谱塑形，二者由不同的梯度分别更新。
- 在固定预激活的前提下，激活输出对系数是仿射的，因此谱调优成为一个更直接的子问题，而不是与特征选择纠缠在一起。
- 摘要提到经验上这种分解使更多目标信号能量集中在神经正切核（NTK）的前导特征模中，与优化行为改善一致。
- 在音频、图像、神经辐射场和神经声学场任务上，LSA 提升了重建质量。

### 主要贡献
- 提出 LSA，用可学习的残差截断傅里叶级数作为神经元级激活，学习谐波振幅以进行谱塑形。
- 强调该方法的机制不是扩展渐近函数类，而是改变表示分解，使谱调优与特征选择通过分离的梯度解耦。
- 给出经验观察：该分解使目标信号能量更集中于 NTK 前导特征模，与优化行为改善一致。
- 在音频、图像、神经辐射场和神经声学场任务上报告了重建质量提升。

### 局限性
摘要未提供足够信息。摘要未说明计算开销、参数增加、训练稳定性、与具体基线方法的详细比较、消融实验、失败场景或适用范围限制。

### 阅读优先级
中。理由：论文主题属于隐式神经表示与神经场景表示中的激活/谱结构设计，问题定位明确，方法思路具有结构性意义，并覆盖音频、图像、NeRF 和神经声学场多类任务；但摘要未提供充分的实验细节、定量结果和局限分析，是否值得优先精读取决于读者对 INR 激活函数设计或谱分解优化的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Implicit neural representations (INRs) are shaped by the spectral structure induced by their input encodings and activation functions. Existing methods improve fitting primarily by modifying which frequencies are available to the network, through coordinate encodings or periodic nonlinearities. However, frequency access is not the only bottleneck: signals with localized or spatially varying structure require the network to efficiently compose frequencies into multi-harmonic internal responses. We introduce learnable spectral activations (LSA), which replace fixed neuron-level nonlinearities with a residual truncated Fourier series whose harmonic amplitudes are learned during training. LSA does not expand the asymptotic function class. Instead, it changes the factorization of the representation: linear weights select features while activation coefficients control spectral shaping, and the two are updated by separate gradients. Because the activation output is affine in the coefficients given fixed pre-activations, spectral tuning becomes a more direct subproblem compared to architectures where it is entangled with feature selection. Empirically, this factorization concentrates more target-signal energy in the leading eigenmodes of the neural tangent kernel, consistent with improved optimization behavior. Across audio, image, neural radiance field, and neural acoustic field tasks, LSA also improves reconstruction quality.

</details>

#### 2026-10-05 - Real-time Rendering of Pre-integrated Neural Emitters

**Authors:** Arno Coomans, Floor Verhoeven, Edoardo A. Dominici, Markus Steinberger
**Links:** [abs](https://arxiv.org/abs/2610.06762) - [pdf](https://arxiv.org/pdf/2610.06762)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-time Rendering of Pre-integrated Neural Emitters
- 作者：Arno Coomans, Floor Verhoeven, Edoardo A. Dominici, Markus Steinberger
- 出版日期：2026-10-05T17:35:36Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.06762) / [PDF](https://arxiv.org/pdf/2610.06762)

### 一句话总结
论文提出 Neural Emission Fields（NEF），通过在发光体周围空间预计算光照，消除运行时积分，从而实时渲染复杂发光体的无噪声无遮挡直接光照。

### 研究问题
论文关注实时渲染中复杂发光体的直接光照瓶颈，具体包括具有遮挡外壳、高多边形发光网格、空间变化发光或可变形组件的发光体。现有实时方案要么依赖简化解析表示，要么回退到运行时采样：解析方法受限于简单发光体几何，纯采样估计器需要高采样预算才能无噪声，代理表示仍需在运行时对发光体周围出射辐射度进行积分。

### 核心思路/方法
论文提出 Neural Emission Fields（NEF），该表示通过在发光体周围体积中预计算光照来消除运行时积分。该神经场由位置、法线、视线方向和材质参数参数化。采用双头漫反射/光泽架构，每个着色点只需一次网络评估即可得到无噪声、无遮挡的直接光照。由于训练在发光体局部坐标系中进行，训练后的 NEF 可作为可移植光照资产，在刚性变换下跨场景复用。内部互反射、自遮挡、空间变化发光和形变均被吸收到学习到的表示中，且不增加运行时成本。

### 主要贡献
- 提出 Neural Emission Fields（NEF），一种在发光体周围空间预计算光照的表示，消除运行时积分。
- NEF 由位置、法线、视线方向和材质参数参数化，并采用双头漫反射/光泽架构。
- 每个着色点仅需一次网络评估即可获得无噪声、无遮挡的直接光照。
- 由于在发光体局部坐标系中训练，NEF 可作为可移植光照资产，在刚性变换下跨场景复用。
- 内部互反射、自遮挡、空间变化发光和形变被吸收进学习表示，且不增加运行时成本。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对实时渲染中复杂发光体直接光照的明确瓶颈，提出预计算神经场以消除运行时积分，并强调可移植光照资产与零额外运行时成本，问题定位和方法思路较清晰；但摘要未提供实验细节、性能数据、对比结果或局限性信息，因此难以仅凭摘要判断其实际效果与适用范围。

</details>

<details>
<summary>Abstract</summary>

Direct illumination from non-trivial emitters with occluding housing, high-polygon emissive meshes, spatially varying emission, or deformable assemblies is a persistent bottleneck in real-time rendering. Current real-time solutions either rely on simplified analytical representations or fall back to runtime sampling. Analytical methods are restricted to simple emitter geometry, pure sampling-based estimators need high sampling budgets to be noise-free, and proxy representations still require runtime integration over outgoing radiance around the emitter. We present Neural Emission Fields (NEF), a representation that eliminates runtime integration by precomputing the illumination in the volume around the emitter. This neural field is parameterized by position, normal, view direction, and material parameters. Using a two-headed diffuse/glossy architecture, it yields noise-free unoccluded direct illumination from a single network evaluation per shading point. Because training is performed in the emitter's local frame, a trained NEF acts as a portable lighting asset reusable across scenes under rigid transforms. Internal interreflections, self-occlusion, spatially varying emission, and deformations are absorbed into the learned representation at zero additional runtime cost.

</details>

#### 2026-10-05 - GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting

**Authors:** Boaz Keren-Gil, James Gain, Patrick Marais
**Links:** [abs](https://arxiv.org/abs/2610.06688) - [pdf](https://arxiv.org/pdf/2610.06688)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting
- 作者：Boaz Keren-Gil, James Gain, Patrick Marais
- 出版日期：2026-10-05T16:52:37Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.06688 ；PDF：https://arxiv.org/pdf/2610.06688

### 一句话总结
GS-Pool 面向同一空间两次独立 3DGS 重建之间的对象级变化检测，通过将 SAM2 掩码提升到高斯、引入跨访问摄影载体并结合几何、颜色与蒸馏 DINOv3 特征，输出发生变化的对象及其掩码。

### 研究问题
工厂、博物馆和测量场景会在相隔数月后拍摄同一空间，需要判断哪些对象发生了变化。当每次访问都用 3D Gaussian Splatting（3DGS）重建后，直接比较两个重建结果无法回答该问题：训练具有随机性，因此未变化空间的两次重建不会重合；并且第二次访问通常只是快速重扫描，照片数量远少于第一次。论文要解决的是在这种独立重建、且第二次扫描照片更少的情况下，如何进行对象级变化检测。

### 核心思路/方法
- 输入为同一空间两次独立重建得到的高斯场，目标是返回每次访问中发生变化的对象及其掩码。
- 将每次访问照片的 SAM2 掩码提升到渲染这些照片的高斯上，并合并为一个对象池，使每个决策在 3D 中按对象只做一次。
- 引入“摄影载体”：将每个输入重建的 3DGS 训练损失作用于另一访问的照片，并反向传播到渲染每个像素的高斯上。
- 将该载体与 GS-Diff 的几何项和颜色项，以及蒸馏的 DINOv3 特征相结合。
- 将这些证据与两次访问中都存在的对象证据进行比较，从而为每个场景设定变化阈值。
- 每个变化对象以一组高斯的形式返回，并附带其决策依据，供检查者在 3D 中复核。

### 主要贡献
- 提出 GS-Pool，用于两个独立重建的 3D 高斯场之间进行对象级变化检测并输出变化对象掩码。
- 设计基于 SAM2 掩码提升与对象池的 3D 对象级决策机制。
- 提出跨访问照片训练损失反向传播得到的“摄影载体”，并与 GS-Diff 几何/颜色项及蒸馏 DINOv3 特征融合。
- 通过比较两次访问共有对象的证据，为每个场景设定变化阈值。
- 在 PASLCD 上达到 mIoU/F1 为 0.751/0.846，相较最强先前方法 GS-Diff 的 0.644/0.758 提升 17%/12%；mIoU 相比 O-SCD、PlenoCI、MV-3DCD 分别高 36%、40%、57%；在 CL-Splats 上达到 0.855 mIoU，比 MV-3DCD 高 33%。

### 局限性
摘要未提供足够信息。摘要未说明方法在训练随机性、第二次扫描照片数量极少、对象池构建错误或阈值设定失败等情况下的失败模式，也未提供计算成本、实时性、跨场景泛化、标注依赖或消融实验细节。

### 阅读优先级
高。该论文直接针对 3DGS 重建之间对象级变化检测这一具体任务，提出明确的跨访问证据融合方案，并在摘要中给出与 GS-Diff 等方法的定量对比；若关注 3D 场景变化检测、3DGS 下游理解或对象级 3D 比较，该文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Factories, museums and surveyors photograph the same space months apart and need to know which objects changed. When each visit is reconstructed with 3D Gaussian Splatting (3DGS), a direct comparison of the two reconstructions does not answer this. Training is stochastic, so two reconstructions of an unchanged space never coincide, and the second visit is often a quick re-scan with far fewer photographs. We propose GS-Pool, which takes two independently reconstructed Gaussian fields of the same space and returns the changed objects in each, together with their masks. SAM2 masks of each visit's photographs are lifted onto the Gaussians that render them and merged into an object pool, so every decision is taken once per object in 3D. We introduce a photographic carrier, the 3DGS training loss of each input reconstruction against the other visit's photographs, backpropagated to the Gaussians that rendered each pixel. We combine it with GS-Diff's geometry and colour terms and our distilled DINOv3 features. This evidence is compared with that of the objects present in both visits, which sets a change threshold for each scene. On PASLCD, GS-Pool reaches mIoU/F1 scores of 0.751/0.846 against 0.644/0.758 for GS-Diff, the strongest prior method, a gain of 17%/12%. Its mIoU is also 36%, 40% and 57% above that of O-SCD, PlenoCI and MV-3DCD, and it reaches 0.855 mIoU on CL-Splats, 33% above MV-3DCD. Each changed object is returned as a set of Gaussians with the evidence behind its decision, which an inspector can review in 3D.

</details>

#### 2026-10-05 - MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks

**Authors:** Eunji Kim, Gahyeon Kim, Gianella Cravioto, Dong-hun Lee, Chaewon Moon, Chae-yeong Song, Sang-hyo Park
**Links:** [abs](https://arxiv.org/abs/2610.06472) - [pdf](https://arxiv.org/pdf/2610.06472)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks
- 作者：Eunji Kim, Gahyeon Kim, Gianella Cravioto, Dong-hun Lee, Chaewon Moon, Chae-yeong Song, Sang-hyo Park
- 出版日期：2026-10-05T15:02:47Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.06472；PDF: https://arxiv.org/pdf/2610.06472

### 一句话总结
MaRO-GS 是一个面向目标物体的 3D 高斯泼溅框架，可直接从带物体掩码的多视角图像优化目标物体高斯，并在多视角掩码不一致时保持鲁棒。

### 研究问题
论文关注 Gaussian Splatting 中的准确 3D 物体重建问题。现有物体级 3DGS 方法在只需要目标物体时仍重建整个场景，而不是直接优化目标物体，带来较大计算开销；同时，它们依赖 2D 分割掩码将高斯与物体关联，但掩码在多视角之间往往不一致。这种不一致会破坏高斯优化，产生错误监督的高斯，从而降低物体重建保真度。

### 核心思路/方法
论文提出 MaRO-GS，一个 3DGS 框架，直接从带物体掩码的多视角图像中优化目标物体高斯，并对不一致监督保持鲁棒。为提供可靠监督，方法使用 mask-reliability view filtering 排除不可靠视角；通过 object-supported Gaussian density control 抑制与目标物体无关的高斯并防止背景密集化；同时使用 Silhouette-aligned Object Loss 维持面向物体的优化。

### 主要贡献
- 提出 MaRO-GS，直接优化目标物体高斯，而非重建整个场景。
- 针对多视角掩码不一致问题，引入 mask-reliability view filtering 以排除不可靠视角。
- 引入 object-supported Gaussian density control，抑制目标物体无关高斯并防止背景密集化。
- 引入 Silhouette-aligned Object Loss，维持物体聚焦优化。
- 摘要称在多种数据集上的实验表明，该方法提升了 PSNR、分割准确率和计算效率，并在小物体 LERF-Mask 数据集上取得最大 2.05 dB 的 PSNR 增益。

### 局限性
摘要未提供足够信息。未提供关于失败案例、方法适用范围、对掩码质量下限的要求、计算资源需求、具体数据集组成或消融实验细节等信息。

### 阅读优先级
高。该论文聚焦 3DGS 物体级重建中的关键问题：多视角掩码不一致与计算开销，并给出针对性方法设计；若关注 3D 高斯泼溅、物体级重建或鲁棒分割监督，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

We address the challenge of accurate 3D object reconstruction from multi-view images in Gaussian Splatting. Existing object-level 3DGS methods reconstruct the entire scene rather than directly optimizing the target object, even when only the target object is needed, which incurs substantial computational overhead. They also rely on 2D segmentation masks to associate Gaussians with objects, but these masks are often inconsistent across views. Such inconsistencies corrupt Gaussian optimization and produce incorrectly supervised Gaussians that degrade object reconstruction fidelity. To overcome these limitations, we propose MaRO-GS, a 3DGS framework that directly optimizes target-object Gaussians from object-masked multi-view images and remains robust to inconsistent supervision. For reliable supervision, mask-reliability view filtering excludes unreliable views. Object-supported Gaussian density control suppresses Gaussians irrelevant to the target object and prevents background densification, while Silhouette-aligned Object Loss maintains object-focused optimization. Extensive experiments across diverse datasets demonstrate that MaRO-GS improves PSNR, segmentation accuracy, and computational efficiency, with the largest PSNR gain of 2.05 dB on the small-object LERF-Mask dataset.

</details>

#### 2026-10-05 - Controllable and Photorealistic Pedestrian Risky Motion Generation for End-to-End Driving Safety Evaluation

**Authors:** Siyuan Liu, Miao Li, Haibao Yu, Haohong Lin, Qing Zhou, Bingbing Nie, Ding Zhao
**Links:** [abs](https://arxiv.org/abs/2610.06171) - [pdf](https://arxiv.org/pdf/2610.06171)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Controllable and Photorealistic Pedestrian Risky Motion Generation for End-to-End Driving Safety Evaluation
- 作者：Siyuan Liu, Miao Li, Haibao Yu, Haohong Lin, Qing Zhou, Bingbing Nie, Ding Zhao
- 出版日期：2026-10-05T11:43:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.06171

### 一句话总结
ControlPed 结合轨迹级冲突合成与 3D 高斯泼溅（3DGS），生成具有照片级真实感和运动可控性的行人类安全关键场景，用于端到端自动驾驶安全评估。

### 研究问题
在罕见且安全关键的车辆-行人交互场景下评估端到端自动驾驶，需要传感器级、照片级真实的场景。然而，基于轨迹的场景生成器无法合成原始视觉观测，而基于视频的方法又缺乏可控性。论文聚焦于如何同时兼顾视觉真实感与运动可控性，生成用于安全评估的高危行人运动场景。

### 核心思路/方法
论文提出 ControlPed 框架，将轨迹级冲突合成与 3D 高斯泼溅（3DGS）相结合。其构建于 HazardPed 数据集之上，该数据集包含来自 10,352 个交通视频的 422 条冲突轨迹、HD 地图以及 857 条标注的 3D 人体运动。方法流程为：首先生成冲突轨迹；随后通过文本条件化的运动扩散模型将这些轨迹提升为 3D 人体运动序列；最后使用可动画的 3DGS 化身渲染多视角传感器观测。

### 主要贡献
- 提出 ControlPed 框架，结合轨迹级冲突合成与 3DGS，生成照片级真实、运动可控的安全关键行人场景，以弥补轨迹生成器无法合成视觉观测、视频方法缺乏可控性的空白。
- 基于 HazardPed 数据集（10,352 个交通视频、422 条冲突轨迹、HD 地图、857 条标注 3D 人体运动）构建方法流程。
- 在 88 个渲染的照片级真实场景中进行安全评估，发现七个领先端到端驾驶模型性能严重下降，平均 HDScore 从 88.8 骤降至 47.4，暴露了在危险行人行为下的主要失效模式。
- 将发布数据集与测试基准，以促进车辆-行人交互的安全评估。

### 局限性
摘要未提供足够信息。摘要仅提及方法框架、数据来源、评估结果与发布计划，未说明方法本身的技术限制、计算成本、泛化边界、失败案例或评估覆盖范围的不足。

### 阅读优先级
高。理由：该工作直接针对端到端自动驾驶安全评估中的关键痛点（罕见安全场景的传感器级生成与可控性），并给出了七个领先模型性能显著下降的量化证据，对自动驾驶安全评测、场景生成与 3DGS 应用方向具有较高参考价值，且承诺发布数据集与基准。

</details>

<details>
<summary>Abstract</summary>

Evaluating end-to-end autonomous driving under rare, safety-critical vehicle-pedestrian interactions requires photorealistic, sensor-level scenarios. However, trajectory-based scenario generators cannot synthesize raw visual observations, whereas video-based approaches lack controllability. To bridge this gap, we present ControlPed, a novel framework that combines trajectory-level conflict synthesis with 3D Gaussian Splatting (3DGS) to generate photorealistic, motion-controllable safety-critical scenarios. Built upon HazardPed, a dataset derived from 10,352 traffic videos comprising 422 conflict trajectories, HD maps, and 857 annotated 3D human motions, ControlPed first generates conflict trajectories, lifts them into 3D human motion sequences via text-conditioned motion diffusion, and finally renders multi-view sensor observations using animatable 3DGS avatars. Safety evaluation in 88 rendered photorealistic scenarios reveals that seven leading end-to-end driving models suffer a severe performance drop, with their mean HDScore plunging from 88.8 to 47.4, exposing major failure modes under dangerous pedestrian behaviors. The dataset and testing benchmarks will be released to facilitate safety assessment of vehicle-pedestrian interactions.

</details>

#### 2026-10-05 - Casual Flash Lighting for Gaussian Splat Inverse Rendering

**Authors:** Jiamin Xu, Dongheng Wei, Jiarong Zhao, Qi Wang, James Tompkin, Weiwei Xu, Gang Xu
**Links:** [abs](https://arxiv.org/abs/2610.06035) - [pdf](https://arxiv.org/pdf/2610.06035)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Casual Flash Lighting for Gaussian Splat Inverse Rendering
- 作者：Jiamin Xu, Dongheng Wei, Jiarong Zhao, Qi Wang, James Tompkin, Weiwei Xu, Gang Xu
- 出版日期：2026-10-05T09:34:05Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.06035（PDF：https://arxiv.org/pdf/2610.06035）

### 一句话总结
本文提出一种结合日常室内拍摄中静态光照与闪光灯（开/关）图像的高斯泼溅逆渲染方法，通过 GS 锚定的漫反射场避免闪光残差在视角间被 alpha 混合漂移吸收，从而改进材质分解与重光照。

### 研究问题
- 从照片中恢复几何、材质和光照在仅有静态光照时高度病态（ambiguous）。
- 主动光照方案可降低歧义，但需要暗室或专用硬件。
- 如何利用日常室内拍摄中同时存在的静态光照与闪光光照（开或关、各自独立视角）来缓解逆渲染的歧义，是本文关注的问题。

### 核心思路/方法
- 协同利用 casual indoor capture 中的静态光照与闪光光照（flash on/off），两者来自独立视角。
- 闪光残差用于约束反照率（albedo）和 BRDF；静态光照则捕捉闪光遗漏的掠射角高光（grazing-angle specular highlights）。
- 以 2DGS 重建为框架。
- 关键贡献是 GS-anchored diffuse field：在光栅化的 2DGS 深度处查询一个哈希编码 MLP。
- 由于该场仅依赖世界位置，它在 3D 中具有视角一致性（view consistent），可使闪光残差驱动材质分解，而不被跨视角的 alpha-blending drift 吸收。
- 同时以延迟着色（deferred shading）渲染静态光照，使其也能监督材质分解。

### 主要贡献
- 提出结合静态与闪光光照的日常室内捕获逆渲染方案，避免主动光照对暗室或专用硬件的需求。
- 提出 GS-anchored diffuse field：哈希编码 MLP 在 2DGS 深度处查询，仅依赖世界位置，保证 3D 视角一致性，防止闪光残差被 alpha 混合漂移吸收。
- 使用延迟着色渲染静态光照，使其参与材质分解监督。
- 在五个合成场景和三个真实室内场景上，该方法在漫反射颜色、反照率与粗糙度材质参数上优于六个近期基线；在重光照任务中，PSNR 相比次优基线提升 4.17 dB。

### 局限性
- 摘要未提供足够信息说明方法的失败场景、硬件依赖、计算成本或对拍摄条件的限制。
- 摘要未提供足够信息说明合成与真实场景的具体规模、评价协议细节及基线选择依据。
- 摘要未提供足够信息说明 GS-anchored diffuse field 在极端视角或复杂材质下的表现边界。

### 阅读优先级
高。理由：该工作针对逆渲染中光照歧义这一核心问题，提出结合日常闪光与静态光照的实用采集方案，并在材质分解与重光照指标上给出明确的量化提升（PSNR +4.17 dB），对神经渲染、逆渲染与材质估计方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering geometry, materials, and lighting from photographs is highly ambiguous when only static illumination is available. Active-lighting setups reduce the ambiguity but require dark rooms or specialized hardware. Instead, we synergize both static and flash lighting from casual indoor capture, with the flash on or off, each from independent viewpoints. The flash residual constrains albedo and the BRDF, while static lighting captures grazing-angle specular highlights that flash misses. With a 2DGS reconstruction framing, our key contribution is a GS-anchored diffuse field: a hash-encoded MLP is queried at the rasterized 2DGS depth. As it depends only on world position, it is view consistent in 3D and allows the flash residual to drive material decomposition instead of being absorbed by alpha-blending drift across views. At the same time, we render static lighting with deferred shading such that it can also supervise material decomposition. On five synthetic and three real indoor scenes, our method outperforms six recent baselines on diffuse color, albedo and roughness material parameters, and in relighting where PSNR improves by 4.17 dB over the next-best baseline.

</details>

#### 2026-10-04 - SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering

**Authors:** Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger
**Links:** [abs](https://arxiv.org/abs/2610.05576) - [pdf](https://arxiv.org/pdf/2610.05576)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering
- 作者：Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger
- 出版日期：2026-10-04T22:25:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.05576 ；https://arxiv.org/pdf/2610.05576

### 一句话总结
针对基于 3D Gaussian Splatting 的随机顺序无关透明渲染中输出噪声明显的问题，从表示与图像合成两个层面降低高频噪声，以提升随机渲染的收敛速度与图像质量。

### 研究问题
随机顺序无关透明渲染可高效、优雅地渲染如 3D Gaussian Splatting 之类的基元辐射场，但由于输出中存在固有的可见噪声，实际应用仍不理想。论文旨在最小化高频噪声，并从表示与图像合成层面处理噪声来源。

### 核心思路/方法
论文提出一种系统性方法来最小化高频噪声，分别从表示层面和图像合成层面处理噪声来源。在随机渲染过程中，采用基于历史的空间重采样方案大幅加速图像收敛，并使用时间重要性重采样保证相机运动下的连贯性。在训练过程中，使用颜色正则化器隐式降低 3DGS 模型沿视光线的方差。基于这些特性，其优化的 Vulkan 渲染器在低采样数和高采样数下都能有效缓解输出噪声。

### 主要贡献
- 提出从表示和图像合成层面最小化高频噪声的系统性方法。
- 在随机渲染中引入基于历史的空间重采样方案，显著加速图像收敛。
- 引入时间重要性重采样，以在相机运动下保持连贯性。
- 在训练中使用颜色正则化器，隐式降低 3DGS 模型沿视光线的方差。
- 实现基于 Vulkan 的优化渲染器，在每像素 1 采样时相较此前随机方法取得约 13 dB 的 PSNR 提升，并快速收敛到排序 3DGS，平均 L1 误差小于 $10^{-4}$。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直接针对 3D Gaussian Splatting 随机渲染中的关键实际瓶颈——输出噪声与收敛速度，并报告了显著的 PSNR 提升和低 L1 误差；若关注 3DGS 渲染、顺序无关透明或随机渲染质量优化，该论文具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Stochastic order-independent transparency enables efficient and elegant rendering of primitive-based radiance fields like 3D Gaussian Splatting models, but remains impractical due to the inherent visible noise in the output. We propose a principled approach to minimize high-frequency noise, addressing its sources at the representation and image synthesis level. During stochastic rendering, our history-based spatial resampling scheme drastically accelerates image convergence, while temporal importance resampling ensures coherence under camera movement. During training, a color regularizer implicitly reduces the variance along view rays in the 3DGS models. With these properties, our optimized, Vulkan-based renderer effectively mitigates output noise at low and high sample counts, achieving a substantial 13~dB PSNR increase in quality over previous stochastic methods at 1 sample per pixel and quickly converging to sorted 3DGS with an average L1 error of less than $10^{-4}$.

</details>

#### 2026-10-04 - Universal Test-Time Training

**Authors:** Zefan Cai, Qinzhe Hu, Ziqiao Ma, Hao Tan, Junjie Hu
**Links:** [abs](https://arxiv.org/abs/2610.05484) - [pdf](https://arxiv.org/pdf/2610.05484)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Universal Test-Time Training
- 作者：Zefan Cai, Qinzhe Hu, Ziqiao Ma, Hao Tan, Junjie Hu
- 出版日期：2026-10-04T19:43:36Z
- 分类：Neural Scene Representations & Rendering（主分类）；次要分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.05484 ；PDF https://arxiv.org/pdf/2610.05484

### 一句话总结
论文提出 uTTT，将所有层原本各自私有的快速权重记忆改为所有层共享的单一记忆，使记忆在时间与深度两个维度上递归，并在语言建模与新视角合成任务上验证其效果。

### 研究问题
现有 Test-Time Training（TTT）架构把上下文压缩为在线更新的快速权重，并作为记忆被查询。但这些设计让记忆对每一层保持私有：记忆只在时间上递归，深度仅用于索引 L 个彼此独立的记忆。论文质疑“记忆归属是否必须绑定到深度”，并研究共享记忆能否带来更好的效果。

### 核心思路/方法
论文提出 Universal Test-Time Training（uTTT）：所有层读写同一份共享记忆，同时保留各层特有的骨干参数。这样共享记忆在时间与深度两个维度上递归，递归单位分别是 chunk 和 layer——某个 chunk 中深层写入的内容，可以被下一个 chunk 的浅层读取。

论文给出两种实例化：
- uTTT-MoE：每个 token head 被路由到由所有层共享的专家池中的少数专家。
- uTTT-Dense：在每个层都应用完整的共享记忆，不进行路由。

### 主要贡献
- 提出 uTTT，将 TTT 中的记忆所有权从“按深度私有”改为“所有层共享一份记忆”。
- 使记忆在时间与深度两个维度上递归，以 chunk 和 layer 为递归单位。
- 给出两种具体实现：uTTT-MoE 与 uTTT-Dense。
- 在语言建模中，uTTT-MoE 在 124M 和 760M 规模达到 15.5 与 27.9 RULER 准确率，在相同状态与活跃计算量下分别比层私有对应方法高 2.6 与 2.1 分，为所测试的有界状态模型中最高，且每 token 损失匹配或优于全注意力。
- 在新视角合成中，在固定每层计算量下共享记忆，路由模型在 view-23 物体 PSNR 上提升 0.92 dB，稠密模型提升 0.76 dB。

### 局限性
摘要未提供足够信息。摘要未说明计算开销、内存占用、训练稳定性、模型规模上限、任务范围之外的泛化性、实现细节或失败案例等局限。

### 阅读优先级
中。理由：该论文针对 TTT 记忆机制提出明确且可检验的结构性改动，并在语言建模与新视角合成两类任务上给出定量增益；但摘要仅覆盖核心方法与主要结果，若读者关注 TTT、快速权重记忆或跨层共享机制，值得进一步阅读全文以确认细节与适用边界。

</details>

<details>
<summary>Abstract</summary>

Recent Test-Time Training (TTT) architectures compress context into fast weights that are updated online and queried as memory. Existing TTT designs keep this memory private to each layer: it recurs only over time, and depth merely indexes L separate memories. We argue that memory ownership need not be tied to depth, and introduce Universal Test-Time Training (uTTT), in which all layers read and write one shared memory while retaining layer-specific backbone parameters. The shared memory thus recurs over two dimensions, time and depth, with chunks and layers as their units: a write by a deep layer in one chunk can be read by a shallow layer in the next. We instantiate this idea as uTTT-MoE and uTTT-Dense. uTTT-MoE routes each token head to a few experts in a pool shared by all layers; uTTT-Dense applies the whole shared memory at every layer without routing. In language modeling, uTTT-MoE reaches 15.5 and 27.9 RULER accuracy at 124M and 760M, 2.6 and 2.1 points above its layer-private counterpart at equal state and active compute, the highest among tested bounded-state models, with per-token loss matching or beating full attention. In novel view synthesis, sharing at fixed per-layer compute gains 0.92 dB in view-23 object PSNR in routed models and 0.76 dB in dense models.

</details>

#### 2026-10-03 - NAMVIS: Next-Scale Autoregressive Multi-View Image Synthesis

**Authors:** Ramil Khafizov, Ilya Statsenko, Ruslan Rakhimov, Artem Komarichev, Peter Wonka, Evgeny Burnaev
**Links:** [abs](https://arxiv.org/abs/2610.04722) - [pdf](https://arxiv.org/pdf/2610.04722)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NAMVIS: Next-Scale Autoregressive Multi-View Image Synthesis
- 作者：Ramil Khafizov, Ilya Statsenko, Ruslan Rakhimov, Artem Komarichev, Peter Wonka, Evgeny Burnaev
- 出版日期：2026-10-03T19:22:02Z
- 分类：Neural Scene Representations & Rendering（主分类）；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.04722 ；PDF https://arxiv.org/pdf/2610.04722 ；项目页 https://corl-team.github.io/namvis/

### 一句话总结
NAMVIS 将稀疏视角多视角图像合成从扩散式迭代去噪改写为“几何条件下的下一尺度自回归”，在 Objaverse、GSO、OmniObject3D 上以更高指标和 3 倍以上加速优于所评估的扩散基线。

### 研究问题
稀疏视角新视角合成是 3D 内容生成的核心问题。摘要指出，基于扩散的方法受限于迭代去噪，导致多视角生成在推理阶段代价高昂。

### 核心思路/方法
- 提出 NAMVIS，一个“无扩散”框架，将多视角图像合成重新表述为几何条件下的“下一尺度自回归”。
- 不通过重复去噪生成目标视角，而是用少量由粗到细的尺度步骤预测离散视觉 token；在每个尺度内以及各目标视角之间并行采样所有 token。
- 提出 Multi-scale Projective Pose Encoding，在每个分辨率上把源相机与目标相机的变换注入目标视角自注意力以及源到目标的交叉注意力，从而将生成过程锚定到显式相机几何。
- 结合全局条件与稠密的几何感知交叉注意力，使模型在保持源视角外观的同时维持目标视角一致性。

### 主要贡献
- 提出无扩散的几何条件下一尺度自回归多视角合成框架 NAMVIS。
- 提出 Multi-scale Projective Pose Encoding，用于在多个分辨率上注入源与目标相机变换。
- 通过全局条件与稠密几何感知交叉注意力的结合，兼顾源视角外观保持与目标视角一致性。
- 在 Objaverse、GSO、OmniObject3D 上，在 PSNR、SSIM、LPIPS 指标上优于所评估的扩散基线，并在相同评估设置下比所评估的扩散基线快 3 倍以上。

### 局限性
摘要未提供足够信息。摘要中仅给出正向结论与速度对比，未提及失败情形、适用边界（如视角数量、物体类型、场景尺度等）、计算资源需求或误差分析。

### 阅读优先级
高。理由：该论文针对稀疏视角多视角合成中扩散推理昂贵的明确痛点，给出非扩散的下一尺度自回归替代方案，并在多个数据集与三项指标上报告优于所评估扩散基线、且推理速度提升 3 倍以上；若关注 3D 内容生成与多视角合成的效率与质量权衡，属于值得优先阅读的工作。

</details>

<details>
<summary>Abstract</summary>

Sparse-view novel view synthesis is a central problem in 3D content creation, but diffusion-based approaches remain limited by iterative denoising, making multi-view generation expensive at inference time. We introduce NAMVIS, a diffusion-free framework that reformulates multi-view image synthesis as geometry-conditioned next-scale autoregression. Instead of generating target views through repeated denoising, NAMVIS predicts discrete visual tokens through a small number of coarse-to-fine scale steps, while sampling all tokens within each scale and across target views in parallel. To anchor this generation process to explicit camera geometry, we propose Multi-scale Projective Pose Encoding, which injects source and target camera transformations into both target-view self-attention and source-to-target cross-attention at every resolution. NAMVIS further combines global conditioning with dense geometry-aware cross-attention, enabling the model to preserve source-view appearance while maintaining target-view consistency. Across Objaverse, GSO, and OmniObject3D, NAMVIS outperforms diffusion-based baselines in PSNR, SSIM, and LPIPS, while running over 3 times faster than the evaluated diffusion baselines under the same evaluation setting. These results suggest that geometry-conditioned next-scale autoregression is a promising and efficient alternative to diffusion for sparse-view multi-view synthesis. Additional qualitative results, videos, and resources are available at https://corl-team.github.io/namvis/

</details>

## Embodied / Robotics / AR Applications

### 2026-10

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

#### 2026-10-07 - Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving

**Authors:** Xingtai Gui, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan, Jianbing Shen
**Links:** [abs](https://arxiv.org/abs/2610.10390) - [pdf](https://arxiv.org/pdf/2610.10390)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric foundation model, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving
- 作者：Xingtai Gui, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan, Jianbing Shen
- 出版日期：2026-10-07T16:47:17Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接：https://arxiv.org/abs/2610.10390；PDF链接：https://arxiv.org/pdf/2610.10390

### 一句话总结
论文提出 GeoCoTDrive，一种显式几何思维链框架，试图通过在 2D 语义推理中引入定位后的 3D 几何先验，缓解现有 VLA 自动驾驶模型中动作所需的精确 3D 几何线索与 2D 语义空间推理之间的不匹配问题。

### 研究问题
现有 Vision-language-action（VLA）模型在自动驾驶中面临一个根本性不匹配：驾驶动作需要精确的 3D 几何线索，而视觉-语言理解与推理主要发生在 2D 语义空间中。论文关注如何让 VLA 模型在面向规划决策时有效利用显式几何信息。

### 核心思路/方法
论文提出 GeoCoTDrive，一个显式几何思维链框架，以规划为导向来 grounding 几何信息。其核心范式是“先以 2D 思考，再以专用 3D 先验驾驶”：
1. 首先 grounding 与决策关键线索对应的 2D 区域；
2. 然后在已 grounding 的区域内，从几何基础模型中采样特征，检索局部化的 3D 先验；
3. 将这些局部几何特征交错加入自回归上下文，以支持轨迹生成。

为监督该过程，论文引入 planning-relevant grounding，即一种新的区域级 grounding 任务，聚焦直接影响自车规划决策的局部空间线索，并构建 PlanningGrounding 数据集，以赋予 VLA 面向规划的 grounding 能力。

### 主要贡献
- 提出 GeoCoTDrive，一个显式几何思维链框架，将几何 grounding 以规划为导向融入 VLA 自动驾驶。
- 提出“先以 2D 思考，再以专用 3D 先验驾驶”的范式，先把 2D 决策关键区域 grounding，再从几何基础模型中检索局部 3D 先验并交错进自回归上下文。
- 引入 planning-relevant grounding 这一新的区域级 grounding 任务，聚焦直接影响自车规划决策的局部空间线索。
- 构建 PlanningGrounding 数据集，用于赋予 VLA 面向规划的 grounding 能力。
- 摘要称在多个端到端自动驾驶基准上的实验表明，GeoCoTDrive 持续提升安全关键规划性能，证明显式几何思维链过程对基于 VLA 的规划有效。

### 局限性
摘要未提供足够信息。论文未在给定摘要中说明方法的具体失败场景、计算开销、对几何基础模型质量的依赖程度、数据集规模与标注细节、是否引入额外推理延迟，也未提供实验设置、对比基线、评价指标和消融研究的细节。因此无法基于摘要判断其泛化性、实时性与实际部署限制。

### 阅读优先级
高。理由：该论文聚焦 VLA 自动驾驶中 2D 语义推理与 3D 几何动作需求之间的核心不匹配，提出显式几何思维链、planning-relevant grounding 任务和 PlanningGrounding 数据集，问题定义清晰且方法方向具有针对性；若关注端到端自动驾驶、VLA 规划或几何 grounding，该论文具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving. However, existing VLA models still suffer from a fundamental mismatch: driving actions require precise 3D geometric cues, while visual-language understanding and reasoning are largely conducted in a 2D semantic space. In this paper, we propose GeoCoTDrive, an explicit geometric chain-of-thought framework that grounds geometry in a planning-oriented manner. GeoCoTDrive follows a think with 2D first, drive with dedicated 3D priors paradigm. It first grounds 2D regions corresponding to decision-critical cues, and then retrieves localized 3D priors by sampling features from a geometric foundation model within the grounded regions. These localized geometric features are interleaved into the autoregressive context to support the trajectory generation. To supervise this process, we introduce planning-relevant grounding, a new region-level grounding task that focuses on local spatial cues directly affecting ego planning decisions, and construct the PlanningGrounding dataset to endow VLAs with planning-oriented grounding capability. Experiments across multiple end-to-end autonomous driving benchmarks show that GeoCoTDrive consistently improves safety-critical planning performance, demonstrating the effectiveness of the explicit geometric chain-of-thought process for VLA-based planning.

</details>

#### 2026-10-07 - Towards Accurate End-Effector Localization for UMI-Style Robotic Manipulation Teaching

**Authors:** Junjie Zhang, Deteng Zhang, Zhisong Xu, Bo Sun, Liuyang Li, Yihong Tian, Jie Yin
**Links:** [abs](https://arxiv.org/abs/2610.09857) - [pdf](https://arxiv.org/pdf/2610.09857)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, manipulation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Accurate End-Effector Localization for UMI-Style Robotic Manipulation Teaching
- 作者：Junjie Zhang, Deteng Zhang, Zhisong Xu, Bo Sun, Liuyang Li, Yihong Tian, Jie Yin
- 出版日期：2026-10-07T11:14:14Z
- 分类：Embodied / Robotics / AR Applications（secondary_categories 未提供）
- 链接：摘要页 https://arxiv.org/abs/2610.09857 ；PDF https://arxiv.org/pdf/2610.09857

### 一句话总结
针对 UMI 风格机器人示教中末端执行器定位精度与时间完整性的评测缺口，论文提出真实与仿真结合的定位数据集 MILD，并提出融合鱼眼视觉惯性估计与序列局部 AprilTag 几何的 AprilVINS，在统一协议下报告了毫米级 TCP 相对 APE RMSE。

### 研究问题
论文关注机器人示教学习中的末端执行器定位问题：在近距离操作与相机遮挡情形下，需要准确且时间上完整的末端执行器定位。摘要指出，现有 SLAM 基准偏重导航运动，而操作数据集更偏重策略学习而非定位评测，因此缺少针对该类任务的诊断式评测框架。

### 核心思路/方法
- 构建 MILD（Manipulation-Interface Localization Dataset）：包含真实世界与仿真序列。真实子集提供来自 Insta360 X5 与 Insight9 的 86 条传感器序列，覆盖 15 个重复桌面任务，并包含标定资产与每次执行的机器人末端执行器参考轨迹；仿真的 MILD-Sim 在 Isaac Sim 中扩展任务覆盖，用于受控的操作重放研究。
- 在带仪器的真实录制上对视觉惯性系统与基准辅助（fiducial-aided）系统进行基准测试，比较 TCP 相对轨迹误差与时间覆盖情况。
- 提出 AprilVINS：结合鱼眼视觉惯性估计与序列局部 AprilTag 几何，用于无需预先测量的基准地图的标记增强示教工作空间；方法区分“先验准入”与“联合优化状态的受保护导出”。
- 在 Insta360 AprilTag4 录制上，在统一协议、序列特定配置下，报告 AprilVINS(full) 达到毫米级 SE(3) 对齐的 TCP 相对 APE RMSE，具有高时间完成度，且报告误差低于所测试路线在各自协议下的结果；不带标签因子的鱼眼 VIO 仍处于厘米级。
- 通过消融实验区分精度与可导出性，并用 MILD-Sim 重放研究提供任务特定的容差参考，以帮助解释误差量级。

### 主要贡献
- 提出 MILD：一个面向操作界面定位的真实与仿真数据集，包含真实传感器序列、标定资产与末端执行器参考轨迹，并提供仿真重放子集 MILD-Sim。
- 在真实录制上对视觉惯性及基准辅助系统进行基准测试，揭示即使同一名义任务下，TCP 相对轨迹误差与时间覆盖率仍存在较大差异。
- 提出 AprilVINS，将鱼眼视觉惯性估计与序列局部 AprilTag 几何结合，并给出先验准入与受保护导出的分离设计。
- 报告 AprilVINS(full) 在指定录制与统一协议下达到毫米级 TCP 相对 APE RMSE，而不带标签因子的鱼眼 VIO 为厘米级；并通过消融与仿真重放研究提供误差解释参考。
- 摘要称代码、数据集与评测清单将在接收后发布。

### 局限性
- 摘要未提供足够信息说明真实子集中的具体任务类型、传感器同步与标定流程细节、基准测试所采用的全部对比方法及其配置。
- 摘要未提供足够信息说明 AprilVINS 在非 AprilTag 环境、无鱼眼相机或严重遮挡等条件下的表现。
- 摘要未提供足够信息说明 MILD-Sim 与真实子集之间的域差距、仿真重放研究的规模及统计显著性。
- 摘要未提供足够信息说明“序列特定配置”是否引入调参偏差，以及各对比路线在各自协议下的公平性细节。
- 摘要未提供足够信息说明代码、数据集与评测清单的实际可获取性（仅称接收后发布）。
- 摘要未提供足够信息说明毫米级误差在不同任务、不同操作速度或不同遮挡程度下的稳定性。

### 阅读优先级
中。理由：该论文针对 UMI 风格机器人示教中的定位评测缺口，提出数据集与定位方法，并报告毫米级与厘米级的对比结果，对具身操作、示教学习与视觉惯性定位交叉方向有参考价值；但摘要未给出完整实验细节、对比配置与开源现状，且部分结论依赖“序列特定配置”和“各自协议”下的比较，需阅读全文进一步判断方法泛化性与评测公平性。

</details>

<details>
<summary>Abstract</summary>

Robot demonstration learning requires accurate and temporally complete end-effector localization during close-range manipulation and camera occlusion. Existing SLAM benchmarks emphasize navigation motions, whereas manipulation datasets prioritize policy learning over localization evaluation. We introduce MILD, a Manipulation-Interface Localization Dataset with real-world and simulation sequences. The real-world subset provides 86 sensor sequences from Insta360 X5 and Insight9 across 15 repeated tabletop tasks, calibration assets, and a per-execution robot end-effector reference trajectory. The simulation subset, MILD-Sim, extends task coverage in Isaac Sim for controlled manipulation-replay studies. Benchmarking visual-inertial and fiducial-aided systems on instrumented real-world recordings reveals large differences in both TCP-relative trajectory error and temporal coverage, even under the same nominal task. To support marker-augmented teaching workspaces without a pre-surveyed fiducial map, we present AprilVINS, which combines fisheye visual-inertial estimation with sequence-local AprilTag geometry and separates prior admission from guarded export of the jointly optimized state. On Insta360 AprilTag4 recordings, AprilVINS(full) under a unified protocol with sequence-specific profiles reaches millimeter-level SE(3)-aligned TCP-relative APE RMSE with high time completion and lower reported error than the tested routes under their respective protocols, whereas fisheye VIO without tag factors remains at centimeter scale. Ablations separate accuracy from exportability, and a MILD-Sim replay study provides task-specific tolerance references for interpreting those error magnitudes. Together, MILD and AprilVINS provide a diagnostic benchmarking framework for UMI-style demonstration collection. Code, datasets, and evaluation manifests will be released upon acceptance.

</details>

#### 2026-10-07 - Not All Uncertainty Matters: Simulation-in-the-Loop Fast-Slow Reasoning for Decision-Critical Autonomous Driving System

**Authors:** Jiayi Chen, Shuai Wang, Guangxu Zhu, Derrick Wing Kwan Ng, Chengzhong Xu, Kaibin Huang
**Links:** [abs](https://arxiv.org/abs/2610.09520) - [pdf](https://arxiv.org/pdf/2610.09520)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Not All Uncertainty Matters: Simulation-in-the-Loop Fast-Slow Reasoning for Decision-Critical Autonomous Driving System
- 作者：Jiayi Chen, Shuai Wang, Guangxu Zhu, Derrick Wing Kwan Ng, Chengzhong Xu, Kaibin Huang
- 出版日期：2026-10-07T06:15:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.09520 ；PDF https://arxiv.org/pdf/2610.09520

### 一句话总结
提出 SIGMA，一个将规划器嵌入不确定性评估的仿真在环快慢协同框架，并引入期望规划增益（EPG）来判断何时调用云端推理，以提升自动驾驶决策的规划效果与效率。

### 研究问题
大型视觉语言模型（VLM）具备强大的开放世界感知与推理能力，可用于自动驾驶，但其高计算成本与推理延迟使持续云端使用不现实。这催生了快慢协同：高效的端上模块负责实时感知与控制，云端模型仅在需要时提供高层推理。核心挑战在于判断云端推理何时应影响时间敏感的驾驶决策。现有方法多依赖感知不确定性、启发式触发或资源驱动策略，而没有评估“解决某个不确定性是否会改善规划”。摘要未提供足够信息说明现有方法在具体场景中的失效程度或量化对比细节。

### 核心思路/方法
SIGMA 是一个面向任务的快慢协同仿真在环框架。它将规划器嵌入不确定性评估中，评估在语义与几何不确定性下，合理的场景实现如何影响可行轨迹与规划代价。基于这些结果，SIGMA 估计解决不确定性所带来的规划代价期望降低量。论文进一步提出期望规划增益（EPG），作为决策级指标，用于云端调用、云端引导集成，以及在截止时间与资源约束下的请求优先级排序。摘要未提供足够信息说明 SIGMA 的具体网络结构、仿真采样机制、EPG 的计算公式及其阈值设定。

### 主要贡献
- 提出 SIGMA：将规划器纳入不确定性评估的仿真在环快慢协同框架，使云端推理是否介入取决于其对规划的实际改善潜力。
- 提出期望规划增益（EPG）：一个决策级指标，用于云端调用、云端引导集成与请求优先级排序，并考虑截止时间与资源约束。
- 在 CARLA 实验中显示，SIGMA 能减少不必要的云端交互，同时改善规划、效率与导航成功率；在静态与动态障碍场景中均有验证。
- 相较固定周期协同，SIGMA 在动态场景中减少不必要云端交互 50%，导航成功率提升超过 6%，完成时间最多缩短 26.2%。

### 局限性
摘要未提供足够信息说明 SIGMA 的失败案例、对仿真环境与真实世界差距的敏感性、EPG 指标在不同 VLM 或不同端上算力配置下的泛化能力，以及实验是否覆盖更复杂或更长期的安全关键场景。摘要也未提供消融实验、对比基线细节、计算开销的绝对值与统计显著性等信息。

### 阅读优先级
高。理由：该论文聚焦自动驾驶中 VLM 云端推理的调用时机这一关键且实用的问题，提出以规划代价降低为核心的决策级指标 EPG，并提供 CARLA 实验中的量化收益（云端交互减少 50%、导航成功率提升超 6%、完成时间最多降低 26.2%），对快慢协同、不确定性评估与具身智能决策方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Large vision-language models (VLMs) provide powerful open-world perception and reasoning for autonomous driving, but their high computational cost and inference latency make continuous cloud-side use impractical. This motivates fast--slow collaboration, where efficient onboard modules handle real-time perception and control while cloud models provide high-level reasoning only when needed. The key challenge is deciding when cloud reasoning should influence time-critical driving decisions. Existing methods often rely on perception uncertainty, heuristic triggers, or resource-driven policies, without assessing whether resolving an uncertainty will improve planning. We propose \textbf{SIGMA}, a simulation-in-the-loop framework for task-oriented fast--slow collaboration. SIGMA embeds the planner into uncertainty assessment and evaluates how plausible scene realizations under semantic and geometric uncertainty affect feasible trajectories and planning cost. Based on these outcomes, it estimates the expected reduction in planning cost from resolving uncertainty. We further introduce expected planning gain (EPG), a decision-level metric for cloud invocation, cloud-guidance integration, and request prioritization under deadline and resource constraints. Experiments in CARLA show that SIGMA reduces unnecessary cloud interactions while improving planning, efficiency, and navigation success in static and dynamic obstacle scenarios. Compared with fixed-period collaboration, SIGMA reduces unnecessary cloud interactions by 50\%, improves navigation success by more than 6\%, and cuts finish time by up to 26.2\% in dynamic scenarios.

</details>

#### 2026-10-07 - ClimbLab: MATLAB Simulation Platform for Legged Climbing Robotics

**Authors:** Kentaro Uno, Warley F. R. Ribeiro, Yusuke Koizumi, Keigo Haji, Koki Kurihara, William Jones, Kazuya Yoshida
**Links:** [abs](https://arxiv.org/abs/2610.09315) - [pdf](https://arxiv.org/pdf/2610.09315)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ClimbLab: MATLAB Simulation Platform for Legged Climbing Robotics
- 作者：Kentaro Uno, Warley F. R. Ribeiro, Yusuke Koizumi, Keigo Haji, Koki Kurihara, William Jones, Kazuya Yoshida
- 出版日期：2026-10-07T02:15:00Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.09315

### 一句话总结
本文提出了一个面向足式攀爬机器人的开源 MATLAB 仿真与分析平台，支持将任意带浮动基座的肢式机器人系统建模为多体系统，并在可配置环境中进行行走与攀爬仿真。

### 研究问题
论文关注足式攀爬机器人研究中的仿真需求：如何为任意肢式机器人系统（以浮动基座多体形式建模）提供在任意环境中行走与攀爬的仿真能力，并支持对攀爬具有关键影响的环境参数与地形进行配置。摘要未提供足够信息说明其具体针对的现存仿真平台缺陷或尚未解决的科学问题。

### 核心思路/方法
- 构建一个开源的 MATLAB 仿真与分析平台，面向足式攀爬机器人。
- 支持将任意肢式机器人系统设计为带浮动基座的多体系统，并仿真其在任意环境中的行走与攀爬。
- 主要可变环境参数包括：倾角（inclination）、重力（gravity）、地面刚度（ground stiffness）。
- 可将任意点云安装为地形图（terrain map）。
- 仿真器采用刚体动力学引擎（rigid body dynamics engine）。
- 论文首先描述仿真器结构、计算流程，然后给出代表性仿真示例：四足机器人假设抓附于墙面（gripping on the wall）或在陡坡上攀爬（climbing on the steep slope）。

### 主要贡献
- 提出并开源了一个专门面向足式攀爬机器人的 MATLAB 仿真与分析平台 ClimbLab。
- 提供了支持任意肢式机器人（浮动基座多体）在任意环境中行走与攀爬的仿真能力。
- 提供了关键环境参数的可配置性（倾角、重力、地面刚度）以及基于任意点云的地形图导入。
- 给出了仿真器结构、计算流程的说明，并展示了四足机器人在墙面抓附与陡坡攀爬的代表性仿真示例。

### 局限性
- 摘要未提供足够信息说明该仿真平台与现有平台的定量对比或验证结果。
- 摘要未提供足够信息说明仿真精度、计算效率、规模上限等性能指标。
- 摘要未提供足够信息说明是否包含真实机器人实验验证，或仿真到现实的迁移评估。
- 摘要未提供足够信息说明平台对非 MATLAB 用户、其他机器人形态或非攀爬任务的适用性限制。

### 阅读优先级
中。理由：该工作面向足式攀爬机器人仿真平台，对从事攀爬机器人建模、仿真与控制的研究者有直接参考价值，且开源平台本身具有工具属性；但摘要仅覆盖平台结构与两个示例场景，未提供与现有平台的对比、实验验证或性能数据，因此对一般读者的即时吸引力有限。

</details>

<details>
<summary>Abstract</summary>

This paper presents an open-sourced MATLAB simulation and analysis platform dedicated to legged climbing robots. This simulator enables the design of any limbed robotic system as an articulated multi-body with a floating base and simulates it walking and climbing in an arbitrary environment. The main variable environmental parameters are inclination, gravity, and ground stiffness, and any point cloud can be installed as the terrain map. Furthermore, the simulator employs a rigid body dynamics engine. This paper first describes the simulator structure, and the computational flow and next presents the representative simulation examples where quadrupedal robots assumed gripping on the wall or climbing on the steep slope.

</details>

#### 2026-10-07 - Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation

**Authors:** Tzu-Yu Chuang, Ching-Hsiang Chang, Yi-Hsiu Lee, Yi-Ting Chen, Min Sun, YuanFu Yang
**Links:** [abs](https://arxiv.org/abs/2610.09309) - [pdf](https://arxiv.org/pdf/2610.09309)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation
- 作者：Tzu-Yu Chuang, Ching-Hsiang Chang, Yi-Hsiu Lee, Yi-Ting Chen, Min Sun, YuanFu Yang
- 出版日期：2026-10-07T02:07:21Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.09309 ；https://arxiv.org/pdf/2610.09309

### 一句话总结
论文提出 Entity-Level Goal Readout，将 3D trace world model 的预测转化为可直接执行的 SE(3) 终端目标，并通过共享 Pose-Native Executor 实现闭环机器人操作。

### 研究问题
生成式 world model 能预测操作场景如何朝任务目标演化，但这些未来预测并不直接给出控制所需的紧凑任务变量。若只用未来预测作为监督，终端目标准确率并非显式学习目标，即使具备几何恢复能力也可能不足。论文关注如何把预测到执行的接口作为显式学习组件，而非控制流程中的附带后处理。

### 核心思路/方法
方法名为 Entity-Level Goal Readout，是一个学习到的 prediction-to-execution 接口，使可执行终端目标成为 3D trace world model 的显式输出。它结合 object-centric pose prediction 与基于观测深度的 translation grounding，产生紧凑的 SE(3) 目标。共享的 Pose-Native Executor 使用该固定目标和在线物体位姿反馈进行闭环控制，且无需重新运行 world model。

### 主要贡献
- 提出 Entity-Level Goal Readout，把可执行终端目标显式建模为 3D trace world model 的输出。
- 将 object-centric pose prediction 与基于观测深度的 translation grounding 结合，生成 SE(3) 紧凑目标。
- 使用共享 Pose-Native Executor，在固定目标和在线物体位姿反馈下进行闭环控制，无需重跑 world model。
- 在五个操作任务上达到 79.69% 平均成功率；目标诊断直接测量终端目标准确率，并通过受控 translation perturbations 描述目标误差下执行性能如何退化。
- 在 Franka 机械臂上零样本部署：nominal StackCube 成功率 73.33%，有 distractors 时 66.67%，PickPlate 中目标在策略训练期间未见时成功率 75.00%。

### 局限性
摘要未提供足够信息。摘要未说明五个操作任务的具体构成、失败模式、计算成本、泛化边界、真实部署的完整条件，也未提供与基线方法的详细对比或消融实验细节。

### 阅读优先级
高。理由：论文聚焦 world model 预测与机器人可执行控制之间的接口问题，提出显式学习的 prediction-to-execution 组件，并报告了多个操作任务与真实 Franka 机械臂零样本部署结果；若关注具身智能、机器人操作和 world model 规划，该工作与核心问题直接相关。

</details>

<details>
<summary>Abstract</summary>

Generative world models provide rich predictions of how manipulation scenes may evolve toward task objectives, yet those futures do not directly expose the compact task variables required by control. When training supervises future prediction alone, terminal goal accuracy is not an explicit learning objective, even when geometric recovery is available. We present Entity-Level Goal Readout, a learned prediction-to-execution interface that makes the executable terminal goal an explicit output of a 3D trace world model. It combines object-centric pose prediction with translation grounded in observed depth to produce a compact goal in SE(3). A shared Pose-Native Executor consumes this fixed goal with online object-pose feedback for closed-loop control without rerunning the world model. Across five manipulation tasks, the pipeline achieves a mean success rate of 79.69%. Goal diagnostics directly measure terminal goal accuracy, while controlled translation perturbations characterize how execution degrades under goal error. Zero-shot deployment on a Franka arm achieves 73.33% success on nominal StackCube, 66.67% with distractors, and 75.00% on PickPlate with a target unseen during policy training. These results support treating the prediction-to-execution interface as an explicit learned component of world-model planning rather than incidental post-processing in the control pipeline itself. Project page: https://claire0730.github.io/executable-goals/

</details>

#### 2026-10-06 - TopoCurve: Geometry-Aware Topology Reasoning via Bézier Curves in Autonomous Driving

**Authors:** Mihai Bogdan Deaconu, Laura Dioşan
**Links:** [abs](https://arxiv.org/abs/2610.09118) - [pdf](https://arxiv.org/pdf/2610.09118)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reasoning, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TopoCurve: Geometry-Aware Topology Reasoning via Bézier Curves in Autonomous Driving
- 作者：Mihai Bogdan Deaconu, Laura Dioşan
- 出版日期：2026-10-06T21:07:51Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.09118 ，PDF https://arxiv.org/pdf/2610.09118

### 一句话总结
TopoCurve 用端点固定的三次贝塞尔曲线统一建模车道几何，并把曲线几何贯穿到注意力与拓扑监督中，在 OpenLane-V2 上以纯端到端相机方案取得新的最优结果。

### 研究问题
论文关注自动驾驶中的拓扑推理任务：从多视角图像中联合检测 3D 车道与交通元素，并推断它们之间的结构连通性。作者指出现有方法存在以下问题：
- 将车道建模为离散折线，缺乏平滑性与解析切线方向，也缺少用于注意力的全局空间支撑；
- 提供的是稀疏的拓扑监督。

### 核心思路/方法
论文提出一种以结构化参数化车道表示为基础的几何驱动架构，核心做法包括：
- 将车道建模为端点固定的三次贝塞尔曲线，从而获得连续几何、精确端点以及解析定义的方向性；
- 在整个流程中复用这一共享曲线几何；
- 使用多尺度傅里叶特征编码端点距离与切线对齐，并注入拓扑头；
- 以采样曲线点作为几何对齐的参考，用于跨越整条车道的可变形交叉注意力；
- 采用并行的曲线锚定注意力分支，为“一对多”拓扑监督提供多样预测。

这些组件被描述为一个紧耦合级联：表示支撑几何推理，几何推理引导特征聚合，并支撑更密集的监督。

### 主要贡献
- 提出 TopoCurve，一种基于结构化参数化车道表示（端点固定三次贝塞尔曲线）的 3D 拓扑推理几何驱动架构。
- 利用共享曲线几何实现连续几何、精确端点与解析方向性，并将其用于拓扑头编码、可变形交叉注意力的几何对齐参考以及一对多拓扑监督。
- 在 OpenLane-V2 基准上，无任何后处理取得 50.6 OLS，作者称其在纯端到端相机方法中建立新的最优结果；在端点检测上以 56.8 对 52.6 的 DET_p 超过所有现有方法。

### 局限性
- 摘要未提供足够信息说明方法的失败场景、对特定数据分布或传感器配置的依赖，以及贝塞尔曲线表示的适用边界。
- 摘要未提供足够信息说明计算开销、推理速度、参数量或训练成本。
- 摘要未提供足够信息说明消融实验的具体设置与各组件贡献的量化结果。
- 摘要未提供足够信息说明除 OpenLane-V2 外的泛化性验证。

### 阅读优先级
高。理由：该工作针对拓扑推理中的车道表示与监督稀疏问题提出结构性改进，在 OpenLane-V2 上报告了端到端相机方法的最优 OLS 与端点检测提升；如果读者关注自动驾驶拓扑推理、车道几何表示或可变形注意力与结构化先验结合，具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Topology reasoning jointly detects 3D lanes and traffic elements from multi-view images and infers their structural connectivity. Current methods model lanes as discrete polylines, lacking smoothness, analytical tangent directions, and global spatial support for attention, while providing sparse topology supervision. We propose TopoCurve, a geometry-driven architecture for 3D topology reasoning grounded in a structured parametric lane representation. Lanes are modeled as endpoint-fixed cubic Bézier curves, enabling continuous geometry with exact endpoints and analytically defined directionality. We exploit this shared curve geometry across the entire pipeline. Endpoint distance and tangent alignment are encoded with multi-scale Fourier features and injected into the topology head. Sampled curve points serve as geometry-aligned references for deformable cross-attention spanning the full lane. Parallel curve-anchored attention branches provide diverse predictions for one-to-many topology supervision. These components form a tightly coupled cascade where representation enables geometric reasoning, guides feature aggregation, and supports denser supervision. TopoCurve achieves 50.6 OLS on the OpenLane-V2 benchmark without any post-processing, establishing a new state-of-the-art among end-to-end camera-only methods, and outperforms all existing approaches on endpoint detection (56.8 vs. 52.6 on DET_p).

</details>

#### 2026-10-06 - Demo: Closed-Loop Sionna-Isaac Sim Co-Simulation Framework for Wireless-Aware Robot Navigation over ROS 2

**Authors:** Yi Shen Lim, Seungeun Oh, Jihong Park
**Links:** [abs](https://arxiv.org/abs/2610.08618) - [pdf](https://arxiv.org/pdf/2610.08618)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Demo: Closed-Loop Sionna-Isaac Sim Co-Simulation Framework for Wireless-Aware Robot Navigation over ROS 2
- 作者：Yi Shen Lim, Seungeun Oh, Jihong Park
- 出版日期：2026-10-06T16:17:51Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.08618) / [PDF](https://arxiv.org/pdf/2610.08618)

### 一句话总结
该论文演示了一个基于 ROS 2 的 NVIDIA Isaac Sim 与 NVIDIA Sionna 实时闭环联合仿真框架，用于无线感知的机器人导航。

### 研究问题
当机器人将控制回路卸载到网络时，接收机随机器人移动，链路质量取决于机器人所在位置。要仿真这一场景，需要同时具备物理引擎和站点特定的传播模型。据作者所知，尚无模拟器原生统一两者，已有的两者耦合仅局限于离线分析。

### 核心思路/方法
提出一个实时联合仿真框架，通过 ROS 2 耦合 NVIDIA Isaac Sim 与 NVIDIA Sionna，闭合两者之间的感知-行动-通信（PAC）回路。Sionna 在 Isaac Sim 所仿真的精确几何环境上进行基站到机器人信道的射线追踪，而非随机建模，并将信道状态实时反馈到控制回路。射线追踪在 GPU 上运行，覆盖图刷新约 16ms（约 60 Hz），足以支持实时控制。为展示框架实用性，在基于 OpenStreetMap（OSM）的 SUTD 校园数字孪生中，使用两台 Nova Carter 机器人实现了一个无线感知导航应用。

### 主要贡献
- 提出并演示了一个基于 ROS 2 的实时闭环联合仿真框架，耦合 NVIDIA Isaac Sim 与 NVIDIA Sionna，闭合感知-行动-通信（PAC）回路。
- 使用 Sionna 在 Isaac Sim 的精确几何上进行基站到机器人的信道射线追踪，并实时反馈信道状态到控制回路。
- 展示了 GPU 射线追踪使覆盖图刷新约 16ms（约 60 Hz），满足实时控制需求。
- 在 OSM 派生的 SUTD 校园孪生中用两台 Nova Carter 机器人实现无线感知导航应用：闭环规划器在仅比最短路径基线增加 7.4% 遍历时间的情况下消除了通信中断，而最短路径基线在其 81.2 s 运行中有 7.9 s 处于断连状态。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作属于演示（Demo）性质，聚焦于联合仿真框架的构建与一个具体导航应用展示，对从事机器人仿真、无线感知导航或 ROS 2 集成的读者有直接参考价值；但摘要未提供更广泛的实验对比、可扩展性或通用性验证信息，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

A robot that offloads its control loop to the network carries the receiver with it, so link quality is decided by where it goes. Simulating this requires both a physics engine and a site-specific propagation model at once; to our knowledge no simulator natively unifies both, with existing couplings of the two limited to offline analyses. We demonstrate a real-time co-simulation framework coupling NVIDIA Isaac Sim and NVIDIA Sionna over ROS 2 that closes the perception-action-communication (PAC) loop between them. Sionna ray-traces the base-station-to-robot channel over the exact geometry Isaac Sim simulates on, rather than modeling it stochastically, and feeds channel states back into the control loop in real time. Ray-traced on GPU, the coverage map is refreshed in ~16ms (~60 Hz), fast enough for real-time control. To showcase the framework's utility, we implement a wireless-aware navigation application in an OpenStreetMap(OSM)-derived SUTD campus twin with two Nova Carter robots: the closed-loop planner eliminates communication outage at only +7.4% traversal time over the shortest-path baseline (which spends 7.9 s of its 81.2 s run disconnected).

</details>

#### 2026-10-06 - WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses

**Authors:** Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen, Dung D. Le, Ngo Anh Vien, H. Nguyen-Xuan
**Links:** [abs](https://arxiv.org/abs/2610.08526) - [pdf](https://arxiv.org/pdf/2610.08526)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses
- 作者：Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen, Dung D. Le, Ngo Anh Vien, H. Nguyen-Xuan
- 出版日期：2026-10-06T15:21:14Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：abs: https://arxiv.org/abs/2610.08526 ；pdf: https://arxiv.org/pdf/2610.08526

### 一句话总结
论文提出 WareFly-VLA——一个面向智能仓库中语言引导无人机人员搜索、定位与跟踪的真实感 VLA 框架与数据集，并基于四个开源 VLA 架构建立统一基准，结果显示仓库中的语言条件空中控制仍远未解决。

### 研究问题
- 视觉-语言-动作（VLA）模型在机器人操作与地面移动导航中已取得显著成果，但智能仓库中无人机的语言条件控制仍基本未被探索。
- 主要障碍在于缺乏同时提供连续底层飞行动作、细粒度自然语言目标描述以及真实工业环境的基准。
- 因此需要构建相应的数据集与评测协议，以检验现有 VLA 模型能否胜任仓库场景下的语言引导空中任务。

### 核心思路/方法
- 构建 WareFly-VLA：一个真实感 UAV VLA 框架与数据集，用于仓库环境中语言引导的人员搜索、定位与跟踪。
- 数据在 NVIDIA Isaac Sim 中采集，包含 507 段人工遥操作飞行回合与 8,504 个高分辨率 RGB 转换样本；每个样本配有人工撰写的目标工人外观描述以及同步的四自由度控制指令。
- 覆盖两类空中任务：目标接近（target approach）与人员跟随（person following），并设置遮挡、远距离搜索、高度变化与杂乱环境等条件。
- 建立统一基准，纳入四个开源 VLA 架构（SmolVLA、GR00T N1.7、pi_0、OpenVLA），在无泄漏的回合级协议下、于两种控制频率进行评测。
- 数据集同时提供同步的视频、语言、动作、位姿与难度标注，以支持世界模型研究。

### 主要贡献
- 提出并发布 WareFly-VLA 框架与数据集，填补智能仓库中语言条件无人机控制基准的空白。
- 提供 507 段人工遥操作飞行回合与 8,504 个高分辨率 RGB 转换，每项均配有人工外观描述与四自由度同步控制指令。
- 覆盖目标接近与人员跟随两类任务，并包含遮挡、远距离搜索、高度变化与杂乱等挑战条件。
- 建立四个开源 VLA 架构在两种控制频率、无泄漏回合级协议下的统一基准。
- 给出关键实证发现：严格泛化设置下性能大幅下降；连续动作建模持续优于离散动作 token 化；单帧下仅前向通道可靠可学；当前基础模型接口从地面与类人形态向空中平台迁移效果差。
- 发布数据集、基线方法与评测协议，以支持智能仓库中的语言接地空中自主研究。

### 局限性
- 摘要未提供足够信息说明真实世界部署验证情况；数据均在 NVIDIA Isaac Sim 中采集。
- 摘要未提供足够信息说明数据集规模相对于任务复杂度的充分性讨论。
- 摘要未提供足够信息说明各基线模型的具体失败模式细节与定量数值。
- 摘要未提供足够信息说明四自由度控制指令的具体维度构成与动作空间定义。
- 摘要未提供足够信息说明难度标注的具体分级标准与标注一致性。
- 摘要未提供足够信息说明除前向通道外其他通道不可靠学习的原因分析。

### 阅读优先级
高。理由：该工作同时提供新数据集、统一基准与明确的反直觉实证结论（如连续动作优于离散 token 化、基础模型跨形态迁移差、单帧仅前向通道可学），对 VLA 与空中具身智能交叉方向具有直接参考价值；摘要所述内容足以支撑将其列为重点跟踪对象。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved impressive results in robotic manipulation and ground-mobile navigation, yet language-conditioned control of unmanned aerial vehicles (UAVs) in smart warehouses remains largely unexplored, hindered by the lack of benchmarks that jointly provide continuous low-level flight actions, fine-grained natural-language target descriptions, and realistic industrial environments. This paper introduces WareFly-VLA, a photorealistic UAV VLA framework and dataset for language-guided human search, localization, and tracking in warehouse environments. It contains 507 human-teleoperated flight episodes and 8,504 high-resolution RGB transitions collected in NVIDIA Isaac Sim, each paired with a human-written appearance description of the target worker and a synchronized four-degree-of-freedom control command. Two aerial tasks are covered: target approach and person following, under occlusion, long-range search, altitude variation, and clutter. A unified benchmark of four open-source VLA architectures (SmolVLA, GR00T N1.7, pi_0 and OpenVLA) is established under a leakage-free episode-level protocol at two control rates. The results show that language-conditioned aerial control in warehouses is far from solved: performance drops substantially under strict generalization settings, continuous action modeling consistently outperforms discrete action tokenization, only the forward channel is reliably learnable from a single frame, and current foundation-model interfaces transfer poorly from ground and humanoid embodiments to aerial platforms. The synchronized video, language, action, pose, and difficulty annotations further support world-model research. The dataset, baselines, and evaluation protocol are released to support language-grounded aerial autonomy in smart warehouses.

</details>

#### 2026-10-06 - Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization

**Authors:** Xuekang Zhu, Kaiwen Feng, Ruifeng Wang, Xiwen Wang, Xiaochen Ma, Bo Du, Changjiang Jiang, Chenfan Qu, Songyu Ye, Xia Du, Wentao Feng, Jian Liu, Ji-Zhe Zhou
**Links:** [abs](https://arxiv.org/abs/2610.07916) - [pdf](https://arxiv.org/pdf/2610.07916)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization
- 作者：Xuekang Zhu, Kaiwen Feng, Ruifeng Wang, Xiwen Wang, Xiaochen Ma, Bo Du, Changjiang Jiang, Chenfan Qu, Songyu Ye, Xia Du, Wentao Feng, Jian Liu, Ji-Zhe Zhou
- 出版日期：2026-10-06T07:58:40Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次要分类信息
- 链接：摘要页 https://arxiv.org/abs/2610.07916；PDF https://arxiv.org/pdf/2610.07916

### 一句话总结
该论文将图像篡改定位（IML）重新解释为以伪影为隐变量的概率问题，指出现有模型对伪影的隐式建模不足，并提出通过成对编辑关系进行特征解耦的两阶段学习范式 PAL 与 SL，同时构建了 EditGroup-45K 数据集。

### 研究问题
论文关注图像篡改定位任务。作者首先揭示伪影的潜在性质，将 IML 从常规的全监督学习重新表述为隐变量问题：$P(y|x)=\int P(y|z)\,P(z|x)\,dz$，其中 $z$ 表示伪影。基于这一解释，作者指出现有 IML 模型不足的原因在于它们采用隐式的伪影建模策略，并强调以显式方式建模 $z$ 的必要性。

### 核心思路/方法
由于没有伪影的直接标签，作者认为特征解耦是进行显式建模最合适的方案。为此，论文提出一个两阶段学习范式，包含 Pairwise Artifacts Learning (PAL) 与 Standard Localization (SL) 两个阶段，分别通过编辑关系估计 $P(z|x)$ 与 $P(y|z)$。为支持这种基于编辑关系的学习，作者构建了 EditGroup-45K，一个以源图像为锚、组织为编辑组以构造配对的数据集。摘要提到进行了大量实验。

### 主要贡献
- 揭示伪影的潜在性质，将 IML 重新解释为隐变量问题 $P(y|x)=\int P(y|z)\,P(z|x)\,dz$。
- 指出现有 IML 模型不足的原因是其隐式伪影建模策略，并强调显式建模 $z$ 的必要性。
- 提出两阶段学习范式 PAL 与 SL，通过编辑关系分别估计 $P(z|x)$ 和 $P(y|z)$。
- 构建 EditGroup-45K 数据集，采用源图像锚定并组织为编辑组以支持配对构造。
- 摘要称实验表明 PAL 范式在多种 IML 架构上带来一致提升，且经验分析验证 PAL 确实通过特征解耦显式捕获了伪影。

### 局限性
摘要未提供足够信息说明该方法的具体失败情形、计算开销、对特定编辑类型的敏感性、数据集覆盖范围之外的泛化能力，也未给出具体实验设置、评价指标细节与消融结果；此外，论文被归入 Embodied / Robotics / AR Applications 分类，但摘要未说明该分类与 IML 任务之间的具体关联。

### 阅读优先级
中。理由：该论文对 IML 提出了较清晰的问题重构（隐变量视角）与显式的解耦学习方案，并配套提出数据集，若关注图像篡改定位、特征解耦或数据集构建，具有一定参考价值；但摘要未提供足够的实验细节与量化结果，且分类标签与任务主题之间的关联不明确，因此优先级不宜直接判为高。

</details>

<details>
<summary>Abstract</summary>

Image Manipulation Localization (IML) is commonly formulated as a fully supervised learning task that estimates the optimal manipulation mask $y$ for a given image $x$. In this work, we first reveal the latent nature of artifacts and thus reinterpret IML as a latent-variable problem, $P(y|x)=\int P(y|z)\,P(z|x)\,dz$, where $z$ denotes the artifacts. Following this interpretation, we pinpoint the cause for the current IML models' insufficiency as their implicit artifacts modeling strategy, highlighting the necessity of modeling $z$ in an explicit manner. Without direct labels, feature disentanglement is the most appropriate solution for this explicit modeling. Accordingly, we propose a two-stage learning paradigm with the Pairwise Artifacts Learning (PAL) and Standard Localization (SL) phases to estimate $P(z|x)$ and $P(y|z)$ via edit relations. To support our edit-relation-based learning, we further curate EditGroup-45K, a source-anchored dataset organized into edit groups for pair construction. Extensive experiments show that our PAL paradigm yields consistent improvements across diverse IML architectures, and empirical analyses further verify that PAL does capture artifacts explicitly through feature disentanglement. Code and dataset are available at https://github.com/venus-guangjian/PAL

</details>

#### 2026-10-06 - CoRE: Learning Collaboration-Role Experts for Decentralized Collaborative Manipulation with One Policy

**Authors:** Yanan Zhou, Zhaoyan Qian, Zihao Li, Mingyuan Ba, Ranpeng Qiu, Weiming Zhi
**Links:** [abs](https://arxiv.org/abs/2610.07752) - [pdf](https://arxiv.org/pdf/2610.07752)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoRE: Learning Collaboration-Role Experts for Decentralized Collaborative Manipulation with One Policy
- 作者：Yanan Zhou, Zhaoyan Qian, Zihao Li, Mingyuan Ba, Ranpeng Qiu, Weiming Zhi
- 出版日期：2026-10-06T04:49:11Z
- 分类：Embodied / Robotics / AR Applications（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2610.07752) / [PDF](https://arxiv.org/pdf/2610.07752) / [项目页](https://aus.bot/research/core/)

### 一句话总结
CoRE 面向“单策略、去中心化”的协作操作设定，通过从多任务多机器人演示中学习“协作角色专家”，让每个机器人在共享参数下仅凭局部视觉与本体感知采取互补动作。

### 研究问题
论文研究的是**单策略去中心化协作**：每个机器人执行同一个策略，输入仅为自身的视觉观测和本体感知，不使用任务提示、身份标签或机器人间通信。核心挑战在于：在共享参数的前提下学习出互补的团队行为，并使每个机器人能基于**局部观测**选择恰当的动作。

### 核心思路/方法
- 从**汇总的多任务、多机器人演示**中学习“协作角色专家”（Collaboration-Role Experts）。
- 使用**融合的外观与几何信息**作为局部交互证据。
- 采用**查询条件化的交叉注意力专家**，提供可适应的预测路径；由**局部路由器**在每个动作块（action-chunk）位置上对各专家进行组合。
- 训练阶段引入**动作—专家对齐损失**：在固定输入下，以相对强制路由预测误差对比演示来监督专家选择，且**无需角色标签**。

### 主要贡献
- 提出 CoRE 方法，在无任务提示、无身份标签、无机器人间通信的单策略去中心化设定下学习互补协作行为。
- 设计基于外观与几何融合的局部交互证据、查询条件化交叉注意力专家与局部路由器组合机制。
- 提出无需角色标签的动作—专家对齐损失，用相对强制路由预测误差监督专家选择。
- 摘要称：在仿真基准中，CoRE 在所评估的去中心化方法中取得最高平均性能；物理实验显示其在多种操作任务中有效协作，并对伙伴延迟和减速具有鲁棒性。

### 局限性
- 具体仿真基准名称、任务数量、对比方法清单及量化指标：摘要未提供足够信息。
- 物理实验的平台、任务细节、评价指标与样本规模：摘要未提供足够信息。
- 方法对更复杂场景（如更多机器人、更高维感知、不同通信约束变体）的泛化能力：摘要未提供足够信息。
- 训练所需演示数据的规模、采集成本与对演示质量的敏感性：摘要未提供足够信息。
- 与集中式或带通信方法的性能差距分析：摘要未提供足够信息。

### 阅读优先级
**中**
理由：该论文聚焦去中心化单策略协作操作，且声称在仿真中取得所评估去中心化方法中的最高平均性能，并有物理实验验证，对具身智能与多机器人协作方向具有参考价值；但摘要未给出具体基准、指标与实验细节，无法仅凭摘要判断其性能优势幅度与方法边界，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

Collaborative manipulation requires robots to perform complementary actions as interactions unfold. We study single-policy decentralized collaboration: every robot runs the same policy from its visual observations and proprioception, without task prompts, identity labels, or inter-robot messages. The challenge is to learn complementary team behaviors within shared parameters and select appropriate actions from each robot's local observations. We introduce CoRE, which learns Collaboration-Role Experts from pooled multi-task, multi-robot demonstrations. Fused appearance and geometry provide local interaction evidence. Query-conditioned cross-attention experts provide adaptable prediction paths, which a local router combines at each action-chunk position. During training, an action-expert alignment loss supervises expert selection using relative forced-route prediction errors against demonstrations under fixed inputs, without role labels. Across simulation benchmarks, CoRE achieves the highest average performance among evaluated decentralized methods. Physical experiments demonstrate effective collaboration across diverse manipulation tasks and robustness to partner delays and slowdowns. Project page: https://aus.bot/research/core/.

</details>

#### 2026-10-05 - GeoWM: Efficient Direct World Modeling in Explicit Geometry

**Authors:** Mehrdad Noori, Guile Wu, Sam Hosseini, Dongfeng Bai
**Links:** [abs](https://arxiv.org/abs/2610.07381) - [pdf](https://arxiv.org/pdf/2610.07381)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometry foundation model, robotics, manipulation, autonomous driving, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoWM: Efficient Direct World Modeling in Explicit Geometry
- 作者：Mehrdad Noori, Guile Wu, Sam Hosseini, Dongfeng Bai
- 出版日期：2026-10-05T20:52:18Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.07381 ；PDF https://arxiv.org/pdf/2610.07381

### 一句话总结
GeoWM 是一种直接在显式几何空间中进行世界建模的方法，通过几何基础模型构建几何历史并借助流匹配 transformer，直接预测指定未来时刻的场景几何，从而避免递归 rollout 带来的误差累积与计算开销。

### 研究问题
论文关注 3D 场景几何及其随时间演化的建模问题，指出这一能力对自动驾驶和机器人领域至关重要。现有常见范式是使用世界模型预测未来图像或环境的潜在表示，再从这些预测中恢复几何。摘要指出该范式存在两点不足：一是没有显式建模几何结构，二是通常依赖递归 rollout 来达到更长的预测时域，导致误差累积与计算成本上升。

### 核心思路/方法
GeoWM 的核心是“直接”在显式几何上预测未来场景几何，而非递归 rollout，也不经过“先预测图像或潜表示、再恢复几何”的间接路径。其关键设计包括：
- 利用几何基础模型将观测到的 RGB 帧转换为“几何历史”；
- 以该几何历史作为条件，输入一个流匹配 transformer，预测指定未来时域的场景几何；
- 使用轻量级相机运动预测器估计未来视角；
- 将观测到的几何投影到预测视角中，作为未来几何预测的有效几何先验。

### 主要贡献
- 提出 GeoWM，一种几何世界模型，可直接预测指定未来时域的场景几何，无需递归 rollout。
- 借助几何基础模型构建几何历史，并以此条件化流匹配 transformer 进行未来几何预测。
- 展示轻量级相机运动预测器可准确估计未来视角，且将观测几何投影到预测视角可为未来几何预测提供有效几何先验。
- 在覆盖城市驾驶、空中飞行和动态操作的四个数据集上进行实验，摘要称 GeoWM 在深度、相机位姿和 3D 场景几何预测上优于所评估的世界模型，同时在更长预测时域下显著降低推理时间。

### 局限性
- 摘要未提供足够信息说明方法在极端场景、不同传感器配置或分布外数据上的表现。
- 摘要未提供足够信息说明各数据集的具体规模、评价指标细节及消融实验的完整结果。
- 摘要未提供足够信息说明几何基础模型与流匹配 transformer 的具体架构、训练成本及超参数敏感性。
- 摘要未提供足够信息说明相机运动预测器的适用范围与失效条件。

### 阅读优先级
高。理由：该论文针对世界模型中递归 rollout 导致误差累积和长时域推理成本高这一明确痛点，提出直接在显式几何空间预测未来场景几何的替代范式，并声称在四类数据集上同时提升深度、位姿与 3D 几何预测表现、降低长时域推理时间。对自动驾驶、机器人和具身智能中需要几何一致长时预测的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Modeling 3D scene geometry and its evolution over time is essential for autonomous driving and robotics. A common paradigm is to use world models to predict future images or latent representations of the environment and subsequently recover geometry from these predictions. However, this paradigm does not explicitly model geometric structure and typically relies on recursive rollouts to reach longer prediction horizons, leading to error accumulation and increasing computational cost. To address these limitations, we present GeoWM, a geometry world model that directly forecasts future scene geometry at specified future horizons without recursive rollout. The key idea is to leverage a geometry foundation model to transform observed RGB frames into a geometric history, which conditions a flow-matching transformer to predict the scene geometry at a specified future horizon. We further show that a lightweight camera-motion predictor can accurately estimate the future viewpoint, and that projecting the observed geometry into the predicted viewpoint provides an effective geometric prior for future geometry forecasting. Extensive experiments on four datasets spanning urban driving, aerial flight, and dynamic manipulation demonstrate that GeoWM outperforms the evaluated world models in forecasting depth, camera pose, and 3D scene geometry, while substantially reducing inference time at longer horizons.

</details>

#### 2026-10-05 - AIM: Adaptive Interaction Modeling Networks for Real-to-Sim Soft-Body Simulation

**Authors:** Tiancheng Yang, Dingshuo Chen, Tianle Chen, Zhaocheng Liu, Qiang Liu
**Links:** [abs](https://arxiv.org/abs/2610.07116) - [pdf](https://arxiv.org/pdf/2610.07116)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AIM: Adaptive Interaction Modeling Networks for Real-to-Sim Soft-Body Simulation
- 作者：Tiancheng Yang, Dingshuo Chen, Tianle Chen, Zhaocheng Liu, Qiang Liu
- 出版日期：2026-10-05T16:52:23Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[abstract_url](https://arxiv.org/abs/2610.07116) / [pdf_url](https://arxiv.org/pdf/2610.07116)

### 一句话总结
AIM 将真实到仿真的软体仿真建模为局部—全局交互问题，通过自适应粒子关系建模与几何条件化的全局通信，提升可变形物体在外力交互下的形变预测精度与长时程稳定性。

### 研究问题
可变形物体操作（如叠衣物、处理食物）要求机器人同时控制物体形状变化与运动。预测式软体仿真可通过预判外力交互下的形变来支持这类任务，但存在两个问题：
1. 基于空间邻域的关系建模可能错误表达形变依赖，引入局部误差，并在连续预测中不断累积；
2. 针对单个场景拟合的模型，难以适应物体几何形状与操作条件的变化。

### 核心思路/方法
AIM 将 real-to-sim 软体仿真视为局部—全局交互建模问题，主要包含：
- 利用运动历史与几何信息，在当前空间邻居与保留连接（retained connections）之上自适应地调整粒子关系；
- 使用几何条件化的全局通信，协调物体整体层面的响应；
- 采用统一运动学控制点接口，表示不同的操作配置；
- 使用多步自回归监督，让模型在自己的预测轨迹上进行训练。

### 主要贡献
- 提出 AIM 框架，将 real-to-sim 软体仿真形式化为局部—全局交互建模问题。
- 通过运动历史与几何自适应的粒子关系建模，以及几何条件化的全局通信，缓解局部邻域建模误差及其累积问题。
- 设计统一运动学控制点接口与多步自回归监督，以适配不同操作配置并提升长时程预测能力。
- 在 PhysTwin 与 PGND 上的实验显示：相对 PhysTwin，未来预测跟踪误差降低 20.0%；相对 PGND，在六类物体上的平均长时程粒子误差降低 22.8%。
- 支持跨动作、跨物体实例与跨场景迁移，包括从机器人交互到人类操作的零样本迁移，且无需目标域动力学拟合。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作面向机器人可变形物体操作中的 real-to-sim 软体仿真核心难题，提出了局部—全局交互建模的统一框架，并报告了明确的误差下降与跨动作、跨实例、跨场景乃至零样本迁移能力；对具身智能、机器人操作与仿真学习方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Deformable-object manipulation is essential for robotic tasks such as folding laundry and handling food, where robots must control shape changes as well as object motion. Predictive soft-body simulation supports these tasks by anticipating deformation under external interactions. However, spatial neighborhoods can misrepresent deformation dependencies, introducing local errors that accumulate over successive predictions. Models fitted to individual scenes must also accommodate changes in object geometry and manipulation conditions. In this work, we propose AIM, an Adaptive Interaction Modeling framework that treats real-to-sim soft-body simulation as a local-global interaction modeling problem. AIM uses motion history and geometry to adapt particle relations over current spatial neighbors and retained connections, while geometry-conditioned global communication coordinates object-wide responses. A unified kinematic control-point interface represents different manipulation configurations, and multi-step autoregressive supervision trains the model on its own predicted trajectories. Experiments on PhysTwin and PGND demonstrate improved motion accuracy and visual fidelity, with a 20.0% reduction in future-prediction tracking error relative to PhysTwin and a 22.8% reduction in mean long-horizon particle error across six object categories relative to PGND. The framework further supports transfer across actions, object instances, and scenes, including zero-shot transfer from robot interactions to human manipulation without target-domain dynamics fitting.

</details>

#### 2026-10-04 - RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation

**Authors:** Huapeng Li, Fuxiang Feng, Jinqiu Fan, Shuo Yang, Fengjiao Chen, Xuezhi Cao, Ran Song, Wei Zhang
**Links:** [abs](https://arxiv.org/abs/2610.05414) - [pdf](https://arxiv.org/pdf/2610.05414)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation
- 作者：Huapeng Li, Fuxiang Feng, Jinqiu Fan, Shuo Yang, Fengjiao Chen, Xuezhi Cao, Ran Song, Wei Zhang
- 出版日期：2026-10-04T17:55:26Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.05414 ；PDF https://arxiv.org/pdf/2610.05414 ；项目页 https://mxxq-stack.github.io/rmmbench-project/

### 一句话总结
RMMBench 是一个面向机器人移动操作的评测基准，通过统一框架整合高层与低层具身任务，构建 70 个“导航—操作”任务场景，用于更细粒度地评估 VLM 在连续空间长时程任务中的具身能力。

### 研究问题
尽管视觉语言模型（VLMs）提升了机器人的环境理解与任务推理能力，但如何全面评估 VLMs 在机器人导航与操作中的集成效果仍是问题。摘要指出，当前基准缺乏评估多样化机器人任务的综合方法，评估指标也相对有限，难以全面、细粒度地衡量 VLMs 的具身能力。

### 核心思路/方法
论文提出 RMMBench，要求机器人理解语言指令并在连续空间中执行长时程任务。该基准将高层和低层具身任务无缝集成到统一框架中，构建了一个“导航—操作”任务套件，包含 70 个规范任务场景，覆盖从局部操作到长时程复合导航的任务范围。

### 主要贡献
- 提出 RMMBench，一个面向机器人移动操作的综合评测基准。
- 将高层与低层具身任务整合进统一框架。
- 构建包含 70 个规范任务场景的“导航—操作”任务套件，覆盖从局部操作到长时程复合导航。
- 通过该基准评估发现，领先 VLMs 在执行移动操作任务时仍面临空间定位方面的重大挑战，并凸显在长时程交互中增强机器人空间感知能力的必要性。

### 局限性
摘要未提供足够信息。摘要未说明基准的具体实验设置、对比方法数量、评测指标细节、任务成功判定方式、仿真或真实环境配置，也未说明其局限性或失败案例。

### 阅读优先级
高。理由：该论文聚焦 VLM 与机器人移动操作评测，提出统一的高层/低层任务框架和 70 个任务场景，并给出对当前领先 VLMs 在空间定位与长时程交互方面的关键发现；对具身智能、机器人导航与操作、VLM 机器人集成评测方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Although the advancement of vision-language models (VLMs) has endowed robots with enhanced environmental understanding and task reasoning, a comprehensive evaluation methodology is important to advance the integration of VLMs in robotic navigation and manipulation. However, current benchmarks lack a comprehensive method to evaluate diverse robotic tasks, and evaluation metrics remain relatively constrained, making it difficult to assess the embodied capabilities of VLMs in a thorough and fine-grained manner. To address this issue, we propose RMMBench, an evaluation benchmark that requires robots to understand language instructions and perform long-horizon tasks in continuous spaces. RMMBench seamlessly integrates high- and low-level embodied tasks into a unified framework, constructing a "navigation-manipulation" task suite comprising 70 canonical task scenarios that range from localized manipulation to long-horizon composite navigation. The results reveal that leading VLMs still face major challenges in spatial localization when performing mobile manipulation tasks, and also highlight the necessity of enhancing the spatial perception capability of robots during long-horizon interactions. RMMBench can be accessed at https://mxxq-stack.github.io/rmmbench-project/

</details>

#### 2026-10-04 - Reflection-Robust 6DoF Object Tracking with Light Fields

**Authors:** Nikolai Goncharov, Donald G. Dansereau
**Links:** [abs](https://arxiv.org/abs/2610.04883) - [pdf](https://arxiv.org/pdf/2610.04883)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reflection-Robust 6DoF Object Tracking with Light Fields
- 作者：Nikolai Goncharov, Donald G. Dansereau
- 出版日期：2026-10-04T02:45:31Z
- 分类：Embodied / Robotics / AR Applications（主要分类；次要分类摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2610.04883) | [PDF](https://arxiv.org/pdf/2610.04883)

### 一句话总结
该论文提出一种基于光场的抗反射 6DoF 刚体目标跟踪方法，将反射造成的视角相关外观变化从干扰转化为位姿线索，并在自建光场跟踪数据集与两段实拍光场序列上验证，是唯一在高反射条件下保持精度的对比方法。

### 研究问题
现有 6DoF 刚体目标跟踪器普遍假设目标外观在序列中保持稳定，但这一假设在反射表面上不成立——反射表面的外观会随其映照的环境而变化。论文要解决的核心问题是：如何在存在视角相关反射外观的情况下，仍然稳健地跟踪运动刚体目标的 6DoF 位姿。

### 核心思路/方法
- 利用光场信息，将反射这一“表面麻烦”重新解释为位姿线索。
- 逐帧流程：
  1. 在抗反射条件下鲁棒地恢复深度，并反投影为点云，进而估计表面法线；
  2. 将目标的视角相关外观分解为漫反射反照率与其所反射的环境贴图，得到一个可重光照的表面光场；
  3. 从粗略初始化出发，用恢复出的环境贴图进行重光照，并在光度损失上优化位姿。
- 关键机制：由于运动目标会映照出场景中的新部分，环境贴图随序列推进不断被填充，使该光度信号随时间变得更锐利、更有利。

### 主要贡献
- 提出一种光场基础、抗反射的 6DoF 跟踪器，把视角相关反射外观显式建模为漫反射反照率与环境贴图的分解，并用于位姿优化。
- 提出一种随序列推进而自我增强的机制：运动目标不断映照新场景区域，使环境贴图逐步补全、跟踪信号逐步锐化。
- 构建了一个新的光场跟踪数据集：从机器人操作基准重新渲染，包含四个受控反射率水平，并为每一水平配以模拟深度，用以复现消费级 RGB-D 传感器在光亮表面上的失效模式。
- 额外在两段实拍光场序列上进行评估。
- 实验结论：在漫反射目标上，该方法落后于最强基线；但在完全反射目标上，它是唯一保持精度的方案，而所有基线均出现性能退化。

### 局限性
- 摘要明确承认在漫反射目标上弱于最强基线，说明方法并非在所有外观条件下占优。
- 摘要未提供足够信息：具体基线方法名称、各数据集上的量化指标数值、消融实验、运行时间与实时性、对光场采集硬件与标定的依赖程度、失败案例与边界条件。
- 摘要未提供足够信息：四个受控反射率水平的具体设定，以及模拟深度的具体失效建模方式。
- 摘要未提供足够信息：方法对非刚性形变、遮挡、快速运动等更一般场景的适用性。

### 阅读优先级
高。理由：该论文针对 6DoF 跟踪中长期被假设忽略的反射外观问题提出明确的新建模思路（可重光照表面光场 + 环境贴图随时间补全），并配套了带受控反射率与模拟深度失效的新基准数据集；摘要给出的结论对比鲜明（漫反射略逊、全反射唯一不退化），对机器人操作、自动驾驶与 AR 相关跟踪研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Tracking the 6DoF pose of a moving rigid object is fundamental to robotics and autonomous driving, but existing trackers assume that object appearance is stable across a sequence, an assumption that breaks down on reflective surfaces whose appearance changes as they mirror the environment. We introduce a light field based reflection-robust 6DoF tracker that turns this apparent nuisance into a pose cue. Per frame, our method recovers depth robustly against reflections, back-projects it into a point cloud, and estimates surface normals. It then decomposes the object's view-dependent appearance into a diffuse albedo and the environment map it reflects, resulting in a relightable surface light field. Starting from a coarse initialization, we relight it by the recovered environment map and optimize the pose on the photometric loss. Because a moving object mirrors new parts of the scene, the environment map fills in as the sequence proceeds, sharpening this signal over time. To evaluate this approach, we introduce a light field tracking dataset re-rendered from a robotic manipulation benchmark at four controlled reflectivity levels, each paired with simulated depth that reproduces how consumer RGB-D sensors fail on shiny surfaces. Additionally, we evaluate on two captured light field sequences. Our method trails the strongest baselines on diffuse objects and is the only one that holds its accuracy on fully reflective objects, where every baseline degrades.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
