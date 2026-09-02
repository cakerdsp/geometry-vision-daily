# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：41
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 13
  - Neural Scene Representations & Rendering: 11
  - Embodied / Robotics / AR Applications: 9
  - Geometry Foundation Models: 5
  - Dynamic / 4D Reconstruction: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

## 今日科研趋势综合分析（arXiv 滚动窗口）


### 今日主要趋势

#### 1. “前馈/训练-free/摊销”思路向 3D 与 4D 重建全面渗透，效率成为核心战场

多篇论文不约而同地避开逐场景优化（per-scene optimization），转向更高效的重建范式：

- **VCAR**（2608.30870）提出**完全无需训练**的 3DGS 分割方案，通过可见性加权多视角投票 + 球面螺旋采样补全视点，绕开特征蒸馏的逐场景训练开销；
- **Amortized Anchor Refinement**（2608.30218）将前馈预测与短时固定预算优化结合，用于可部署的连续时间 4D 重建，使重建能够在消费级 GPU 和 XR 头显上落地；
- **GeoRay**（2608.29680）展示了前馈式三维基础模型向**卫星 RPC 相机**场景的迁移——这是前馈重建从透视场景走向非中心相机模型的重要信号；
- **Lapis**（2608.30129）用**单步扩散**替代多步去噪，配合线性注意力将推理延迟在高分辨率下降低 7-10 倍。

**本质变化**：从“先优化再用”转向“先预测再微调（甚至不微调）”，效率正从加分项变成基本要求。

#### 2. 3DGS 从“重建几何”迈向“物体级结构化与交互”，可编辑性成为新的焦点

3DGS 不再只追求重建精度，而是开始关注**物体级粒度**、**可编辑性**和**交互性**：

- **ObjectSplat**（2608.30423）“先分解再重建”——将实例与背景分别用 mesh splatting 重建后合成，实现物体级编辑并提升 F-score 超过 5%；
- **Lucida**（2608.30821）面向机器人和具身 AI，将杂乱室内场景解析为“独立、可编辑、按观测排列”的物体资产；
- **CapFrame**（2608.30342）提出 TIVG 新任务，通过语言指令控制 3DGS 场景中的相机位姿——这本质上是让 3DGS 场景具备“可操纵”的语言接口；
- **ARAP Deformation of Gaussian Radiance Fields**（2608.29538）关注高斯辐射场的用户交互变形，解决几何编辑与辐射场渲染不一致导致的伪影。

**本质变化**：3DGS 正从“观看用表示”转型为“操纵用表示”，结构化和交互能力正在成为研究高地。

#### 3. 动态场景重建走向“锚点化/结构化”建模，放弃对单个高斯原语的长期跟踪

两篇动态/4D 重建论文给出了高度一致的技术判断：

- **ATGS**（2608.30184）明确指出“用单个高斯基元显式跟踪长期复杂运动本质上是不可靠的”，转而将高斯组织在**时间条件锚点**周围，用时间窗口策略激活相关锚点；
- **SMG**（2608.31023）提出语义运动图（Semantic Motion Graph），将高斯运动建模为**低秩语义运动**，由 SMG 节点驱动，并利用语义一致性缓解遮挡和复杂运动下的不确定性。

**本质变化**：动态场景建模的核心路径从“直接追踪三维点/高斯”转向“先建立结构（锚点/图），再用该结构驱动运动”，这显著降低了长程运动建模的不稳定性。

#### 4. 可靠性评估从“单一指标”走向“细粒度审计”，鲁棒性和校准成为独立研究方向

多篇论文不满于用单一误差指标评价系统，而是区分“失败模式”的差异：

- **Monocular SLAM under Corruptions**（2608.30690）将“显式跟踪失败”与“持续漂移”分离评估，发现学习型跟踪器倾向于将灾难性丢失转化为持续性漂移，并检验合成退化与真实条件能否得出相同工程结论；
- **Confidence Calibration Audit**（2608.29705）系统审计七个前馈式重建模型的置信度，发现不确定性在非训练条件下系统性偏低（中位数偏差 2.4 倍），且模型越自信偏差越大——这提示“置信度”本身是一个需要校准的输出维度；
- **When 3DGS Recovers Real Surfaces**（2608.30054）从数学上划定了 3DGS 恢复真实表面的**可辨识性窗口**——角向容量受限时表面一致解受偏好，反之则可能在相同图像下产生“广告牌式”错误几何。

**本质变化**：对重建/感知系统的评测，正从“报一个 AUROC/PSNR”走向“区分失败类型、审计不确定性质量、界定理论边界”，可靠性本身正在成为一门学问。

#### 5. 生成式 AI 带来新型安全问题，主动防御进入“完全重建”时代

- **APT**（2608.30656）指出现有主动篡改定位均假设“拼接”（SP）设定——合成区域叠加在原始背景上，嵌入信号得以保留。但真实世界的扩散模型修复（inpainting）属于**完全重建**（FR）设定：整张图像都经过去噪，背景信号被破坏，传统框架全部失效。APT 通过在潜在空间嵌入锚点对齐的向量信号，在 FR 设定下首次实现了 0.92 的 FR IoU。

**本质变化**：扩散模型的普及正在系统性瓦解基于“局部篡改”假设的取证方案，安全技术必须从“假设局部修改”转向“假设全图重建”。


### 技术路线观察

| 方向 | 论文 | 技术侧重点 | 共性趋势 |
|------|------|-----------|---------|
| **Geometry Foundation Models**（几何基础模型） | OptiGeo（2608.29881）、GeoRay（2608.29680）、Confidence Audit（2608.29705） | 前馈重建正从“透视相机”走向“非中心RPC相机”（卫星）；光学挑战场景被视为**基础模型训练中的局部失效模式**而非独立任务；置信度被当作需要校准的输出维度 | 基础模型的**能力边界**（传感器偏差、基准模糊、置信度失真）成为研究重点；“哪里失效”比“平均表现多好”更重要 |
| **3D Reconstruction & Multi-view Geometry** | Lucida（2608.30821）、MCamera SLAM鲁棒性（2608.30690）、Lapis（2608.30129）、GeoRay、SMG | 重建的对象从“场景点云/网格”升级为**可编辑物体资产**；SLAM评测从单一轨迹误差走向失败/漂移二分；深度估计引入生成式单步扩散 | 端到端可微性与生成式先验的引入；目标从“重建得准”转向“重建得可用、可推理” |
| **Dynamic / 4D Reconstruction** | ATGS（2608.30184）、SMG（2608.31023）、Amortized Anchor Refinement（2608.30218） | 一致采用**锚点/图结构驱动高斯运动**；前馈+短优化替代纯逐场景优化；拓扑保持（持久同调）用于高斯剪枝 | 运动建模从“逐原语跟踪”转向“结构化驱动”；部署效率（XR头显、消费级GPU）纳入设计目标 |
| **Neural Scene Representations & Rendering** | VCAR（2608.30870）、ObjectSplat（2608.30423）、ARAP Deformation（2608.29538）、CapFrame（2608.30342）、ATGS | 3DGS分割走向训练-free；网格保真度与物体级可编辑性挂钩；变形需保持辐射场一致性；语言指令控制相机位姿 | 3DGS 正从“重建工具”变成“可交互、可编辑、可语言控制的场景表示”；同时出现数学层面（可辨识性）的反思 |
| **Embodied / Robotics / AR Applications** | HDR色调映射（2608.30400）、数字孪生触诊（2608.29396）、MILO 3D HOI（2608.27407）、Lucida | 低层视觉（色调映射、深度估计）与下游

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-02T12:33:02-04:00
**Total number of papers:** 49
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

### 2026-09

#### 2026-09-01 - Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison

**Authors:** Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit
**Links:** [abs](https://arxiv.org/abs/2609.01530) - [pdf](https://arxiv.org/pdf/2609.01530)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** CroCo, pointmap, pose estimation

<details>
<summary>Abstract</summary>

Self-supervised pre-training via cross-view completion learns strong features for 3D vision from co-visible regions of image pairs. However, the reference view provides little information for reconstructing non-co-visible patches, implicitly yielding a monocular training signal in these regions. We introduce Gekko, which turns this limitation into a useful signal. The relative improvement of the cross-view reconstruction error over a masked-autoencoder error is a self-supervised proxy for co-visibility: large improvements indicate co-visible regions, negligible ones non-co-visible areas. Gekko is a network, trained from scratch, that jointly performs cross-view completion, masked autoencoding, and per-pixel prediction of this relative improvement, providing an additional binocular signal for all masked regions without any ground-truth 3D annotation. Under identical architectures and training data, Gekko consistently outperforms CroCo on zero-shot correspondence estimation, relative pose estimation, and pointmap regression, with up to 6 times higher accuracy at the strictest relative-pose threshold and a 22% drop in end-point error on ETH3D. The extra channel it learns is itself a strong co-visibility detector on unseen scenes, and Gekko's frozen features outperform released cross-view backbones of comparable or larger size. It can also be trained directly from raw videos with a simple stride-based curriculum, removing the cumbersome 3D preprocessing prior methods require while matching models trained on curated data. Code and pre-trained models are publicly available.

</details>

### 2026-08

#### 2026-08-30 - OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes

**Authors:** Muxin Liu, Tianbo Liu, Jing Xia, Xiaoyang Lyu, Xiaoshan Wu, Bo Wang, Peng Dai, Zhongrui Wang, Shaoshuai Shi, Xiaojuan Qi
**Links:** [abs](https://arxiv.org/abs/2608.29881) - [pdf](https://arxiv.org/pdf/2608.29881)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** monocular geometry, depth estimation, monocular depth, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes
- 作者：Muxin Liu, Tianbo Liu, Jing Xia, Xiaoyang Lyu, Xiaoshan Wu, Bo Wang, Peng Dai, Zhongrui Wang, Shaoshuai Shi, Xiaojuan Qi
- 出版日期：2026-08-30
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（副分类）
- 链接：https://arxiv.org/abs/2608.29881

### 一句话总结
OptiGeo 提出一种偏差感知训练框架，利用少量透明目标渲染数据对单目深度估计模型进行局部几何矫正，以高效应对透明、反射等光学挑战场景中的传感器偏差问题。

### 研究问题
如何在透明、反射和高光等光学挑战性场景中，提升单目深度估计模型对真实传感器缺失或偏差数据的鲁棒性，避免对通用几何模型造成过度专门化，同时保持高效的部署规模。

### 核心思路/方法
- 将光学失效问题重新定义为基础模型训练中的局部失效模式，识别出传感器引发的监督偏差是关键瓶颈（模型从有偏的真实深度监督中继承了传感器失效模式）。
- 提出 OptiGeo，一种偏差感知训练框架：利用干净几何教师模型和残差裁剪对齐（residual-trimmed alignment）来修正有偏的真实监督。
- 将透明目标渲染重新定位为“干净光学几何”的紧凑来源，而非大规模领域专用微调数据集；仅用少量渲染数据即可学习透明物体及区域的几何结构，纠正真实传感器难以监督的局部几何失真。
- 模型参数量仅 30M，保持高效性。

### 主要贡献
- 提出传感器监督偏差是光学挑战场景下单目深度估计模型失效的关键瓶颈，并给出新的问题视角。
- 提出 OptiGeo 偏差感知训练框架，结合干净几何教师与残差裁剪对齐，有效修正有偏监督。
- 以少量透明目标渲染数据实现局部几何矫正，避免架构冗余和过度专门化。
- 在透明场景基准上以 30M 参数超越 300M 级单目模型及十亿级多视图基线方法，同时在通用零样本深度和边界锐度上保持竞争力。
- 通过真实世界导航案例验证了作为光学挑战场景中高效感知模块的实用性。

### 局限性
摘要未提供足够信息。未提及 OptiGeo 在非光学挑战场景（如极端光照、动态物体、遮挡严重等）下的表现，也未报告训练渲染数据的具体规模、生成成本或训练时间，以及与其他方法在计算开销上的详细对比。

### 阅读优先级
**高**。理由：该工作针对机器人部署中真实存在的传感器失效问题（透明/反射/高光），提出了一种参数高效（30M）且不依赖大规模特定领域数据的训练框架，在基准上显著超越更大规模模型，具备实际应用价值；同时问题定义新颖（传感器监督偏差），对单目几何领域的研究有启发性。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation has achieved strong open-domain generalization, yet reliable robotic deployment remains difficult in transparent, reflective, and specular environments, where depth sensors often produce missing or biased depth. Existing methods often handle such optical failures with scene-specific preprocessing, auxiliary modules, or post-hoc fine-tuning. While effective in constrained settings, these designs increase architectural redundancy and can over-specialize general geometry models to narrow optical scenarios. We revisit this problem as a localized failure mode within base-model training and identify sensor-induced supervision bias as a key bottleneck: models inherit sensor failure patterns from biased real-depth supervision in optically challenging regions. We then introduce OptiGeo, a bias-aware training framework that rehabilitates biased real supervision using a clean-geometry teacher and residual-trimmed alignment. We redefine transparency-targeted rendering as a compact source of clean optical geometry, rather than a large domain-specific fine-tuning set. With only a small targeted rendering set, OptiGeo learns the geometric structure of transparent objects and regions, correcting local geometry distortions that real sensors cannot reliably supervise. Despite only 30M parameters, OptiGeo outperforms substantially larger 300M-scale monocular models and billion-scale multi-view baselines on transparent-scene benchmarks, while remaining competitive on general zero-shot depth and boundary sharpness. Real-world navigation cases further validate its practicality as an efficient perception module in optically challenging scenes.

</details>

#### 2026-08-30 - A Calibration Audit of Confidence in Feed-Forward 3D Reconstruction

**Authors:** Nanxing Nick Deng, Qing Cheng, Niclas Zeller, Daniel Cremers
**Links:** [abs](https://arxiv.org/abs/2608.29705) - [pdf](https://arxiv.org/pdf/2608.29705)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Calibration Audit of Confidence in Feed-Forward 3D Reconstruction
- 作者：Nanxing Nick Deng, Qing Cheng, Niclas Zeller, Daniel Cremers
- 出版日期：2026-08-30
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：https://arxiv.org/abs/2608.29705

### 一句话总结
本文系统审计了七种前馈式三维重建模型的逐像素置信度，发现其误差排名表现良好，但不确定性幅度在非训练条件下系统性偏低（中位数偏差2.4倍），且无法通过简单重缩放修正场景级校准问题。

### 研究问题
前馈式三维重建模型输出的逐像素置信度虽被下游系统当作可靠性信号使用，但其训练目标是损失权重而非不确定性幅度，因此该置信度是否可用于误差预测从未被定量检验。本文围绕这一问题展开审计。

### 核心思路/方法
- 对七种已发布骨干模型、十三个数据集进行系统审计。
- 从四个维度评估置信度质量：误差排名能力、平均水平的正确性、置信度范围内的稳定性、区间覆盖真实值的程度。
- 发现置信度在排名误差上表现良好，但预测的不确定性幅度过低（中位数偏差2.4倍），且模型越自信偏差越大。
- 通过实验说明该现象在损失达到最优时仍可出现。
- 提出一种每骨干+每数据集仅含两个常数的幂律校正方法，可修正整体幅度而不影响排名。
- 展示了所有重缩放方法都无法修正的“场景级”偏差。

### 主要贡献
- 首次对前馈式三维重建模型的置信度进行系统校准审计。
- 量化了跨模型、跨数据集的置信度偏差（中位数2.4倍）。
- 揭示模型越自信则误差预测偏差越大的现象。
- 展示即使损失达到最优，模型仍可能保持过度自信。
- 提出并公开审计协议、结果及每模型每数据集拟合常数：目标数据集留出时可将中位数偏差从2.4x降至1.35x，用少量标注场景重拟合可进一步达1.12x。

### 局限性
摘要未提供足够信息：未明确提及具体数据集名称、模型架构细节、计算成本、校正方法在不同场景下的适用边界，以及“场景级”偏差的定量描述（仅提及约三分之二的留出场景落在五点区间外）。

### 阅读优先级
**高**  
理由：本文针对一个广泛使用但未被验证的置信度信号进行了严格的跨模型、跨数据集审计，发现系统性的校准问题并提出实用校正方法；其成果对三维重建（尤其是视觉定位、导航等依赖可靠不确定性的任务）具有直接参考价值，且审计协议和拟合常数的公开便于复现与扩展。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models emit a per-pixel confidence that downstream systems read as a reliability signal. It is trained as a loss weight, not as an uncertainty magnitude, and whether it can be used as an error prediction has not been measured. We audit seven released backbones on thirteen datasets and score the confidence on four properties, how well it ranks error, whether its level is right on average, whether it holds across the confidence range, and whether its intervals cover the truth. The confidence ranks error well, but the predicted uncertainty is too low when it is read under conditions that are not exactly those of training. The median case is off by 2.4x across all seven models, and the error prediction is further off the more confident the model is. We show that this phenomenon can appear even though the loss's optimum is reached. A released model resumed under its own loss reaches that optimum on its training data within a few hundred updates and stays overconfident on unseen frames. A power law with two constants per backbone and dataset corrects the overall magnitude of the predicted uncertainty and leaves the ranking untouched. What no rescaling reaches is the scene, which we attribute to the model's missing knowledge of scale across predictions. Every correction we tried is close to right on average and still leaves two thirds of held-out scenes outside a five-point band, because what a scene is missing is a shape rather than a shift. We release the audit protocol, its results, and the fitted constants per model and dataset. Fitted with the target dataset held out, the constants bring the median case from 2.4x off to 1.35x, and a refit on a few labelled scenes of that dataset reaches 1.12x.

</details>

#### 2026-08-27 - CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction

**Authors:** Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen, Aurélien Chateigner
**Links:** [abs](https://arxiv.org/abs/2608.26868) - [pdf](https://arxiv.org/pdf/2608.26868)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** VGGT, SLAM, monocular depth, Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction
- 作者：Jean-Daniel de Ambrogi, Aline Chetouani, Vincent Nguyen, Aurélien Chateigner
- 出版日期：2026-08-27
- 分类：几何基础模型（Geometry Foundation Models）；次要分类：3D重建与多视角几何、神经场景表示与渲染
- 链接：https://arxiv.org/abs/2608.26868

### 一句话总结
CGS-SLAM提出了一种基于3D高斯泼溅（3DGS）的混合式去中心化/中心化多智能体SLAM系统，仅使用RGB和惯性数据即可实现多智能体的协同场景重建与子图对齐。

### 研究问题
如何在不依赖RGB-D传感器（如消费级智能手机不可用）的条件下，利用3DGS实现多智能体协同SLAM，并兼顾低通信开销与高质量的重建和跟踪。

### 核心思路/方法
每个智能体使用惯性数据作为运动先验进行本地跟踪，借助度量单目深度估计器（Depth Pro）重建带尺度的地图；智能体之间共享关键帧编码，并在空间重叠区域进行动态关键帧选择以增强子图对齐；随后，中心服务器使用视图对齐模型（VGGT）对各子图进行全局对齐，形成混合式去中心化/中心化架构，从而在大范围GNSS拒止环境中保持低通信成本并完成全局重建。

### 主要贡献
1. 提出了首个（或少数）支持仅RGB+惯性输入的多智能体3DGS SLAM系统。
2. 设计了混合式去中心化/中心化通信机制，在映射过程中保持低通信开销。
3. 引入动态关键帧选择策略以提升子图对齐质量。
4. 实验表明在多个数据集上跟踪性能具有竞争力，渲染质量优于现有方法，且子图对齐准确。

### 局限性
摘要未提供足够信息。摘要仅提及实验效果（跟踪、渲染、对齐），未说明失败场景、传感器要求、实时性、计算资源消耗或对智能体数量扩展性的具体讨论。

### 阅读优先级
**中**。理由：该工作面向多智能体协同SLAM与3DGS结合，属于较为新颖且应用价值较高的方向，但摘要中未给出具体数值结果与详细方法框架，适合对协同重建感兴趣的研究者进一步阅读全文；若读者主要关注单智能体3DGS SLAM或实时部署，则本文优先级一般。

</details>

<details>
<summary>Abstract</summary>

Recent advances in SLAM have leveraged 3DGS for photorealistic reconstruction and novel view synthesis. However, most methods rely on RGB-D input, which is unavailable on consumer-grade smartphones, and few integrate 3DGS within a collaborative framework. Therefore, we present CGS-SLAM, a hybrid decentralized/centralized system enabling multi-agent 3DGS SLAM using only RGB and inertial data. Each agent performs local tracking with inertial data as a motion prior and reconstructs a scaled map using a metric monocular depth estimator (Depth Pro). Keyframe encodings are shared among agents, enabling dynamic keyframing in regions of spatial overlaps with other agents, enhancing submap alignment. Afterwards, a central server aligns submaps using VGGT as a view alignment model. This bidirectional communication keeps communication cost low during mapping and global reconstruction in difficult GNSS-denied environments. Experiments on multiple datasets demonstrate competitive tracking performance, improved rendering quality over state-of-the-art methods, and accurate submap alignment.

</details>

#### 2026-08-27 - Glass Surface Detection Grounded in 3D Visual Geometry

**Authors:** Yiwei Lu, Ke Xu, Tao Yan, Xiaojun Chang, Radu Timofte, Rynson W. H. Lau
**Links:** [abs](https://arxiv.org/abs/2608.26752) - [pdf](https://arxiv.org/pdf/2608.26752)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** visual geometry grounded transformer, VGGT, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Glass Surface Detection Grounded in 3D Visual Geometry
- 作者：Yiwei Lu, Ke Xu, Tao Yan, Xiaojun Chang, Radu Timofte, Rynson W. H. Lau
- 出版日期：2026-08-27
- 分类：Geometry Foundation Models（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.26752

### 一句话总结
该论文提出将玻璃表面检测从2D外观线索转向基于3D视觉几何建模的方法，通过蒸馏3D先验并设计专用检测头，在七个基准上取得最优性能。

### 研究问题
如何利用3D视觉几何显式建模玻璃表面的物理存在，以解决传统2D外观方法在几何模糊场景中对透明、反光玻璃检测失效的问题。

### 核心思路/方法
1. **范式转变**：将GSD问题从2D外观驱动转为3D几何驱动。
2. **3D先验蒸馏**：从视觉几何grounded transformer（VGGT）中蒸馏丰富的3D先验，生成玻璃感知的3D表示。
3. **多任务学习**：设计新型玻璃检测头，包含两个核心模块：
   - **频率自注意力模块（FSAM）**：识别玻璃特有的光谱特征，用于玻璃表面定位。
   - **几何接地模块（GeGB）**：选择性将2D特征接地到3D几何中，用于玻璃表面分割。

### 主要贡献
1. 提出将玻璃表面检测重新定义为3D几何grounded问题，而非纯2D外观任务。
2. 设计了包含FSAM和GeGB的新颖检测头，结合频率特征与3D几何信息。
3. 在七个标准GSD基准上达到最先进性能，并验证了对视频/多模态数据的泛化能力。
4. 展示了对玻璃场景重建质量的显著提升。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法的计算开销、对3D几何质量（如深度估计误差）的依赖程度，或在高度动态/极端光照场景下的失效边界；实验细节（如具体消融、运行时间）也未给出。

### 阅读优先级
**高**
理由：该工作提出了一种解决玻璃检测难题的新范式（3D几何grounded），而非仅方法改进；涵盖了从模型设计、多任务学习到下游重建应用的完整链条，且指标全面（七个基准+泛化测试）。对从事透明物体感知、3D视觉或机器人场景理解的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Glass surface detection (GSD) is critical for scene understanding and reconstruction, and yet remains challenging due to the transparency and reflectivity of glass surfaces. Existing GSD methods typically rely on 2D appearance cues, which may fail in geometrically ambiguous scenes. In this paper, we propose a paradigm shift: grounding GSD in 3D visual geometry to explicitly model the physical existence of glass surfaces. Our method first distills rich 3D priors from the visual geometry grounded transformer (VGGT) and generates glass-aware 3D representations. It then exploits multi-tasking learning with a novel glass detection head, consisting of two core modules: a Frequency Self-Attention Module (FSAM) that identifies glass-specific spectral features for glass surface localization, and a Geometry Grounding Block (GeGB) that selectively grounds 2D features in 3D geometry for glass surface segmentation. Extensive experiments demonstrate that our method achieves state-of-the-art performance across seven standard GSD benchmarks, generalizes well to video/multi-modal data, and substantially improves reconstruction in glass scenes. Code is available in https://github.com/YT3DVision/VGGT_GLASS.

</details>

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-01 - EvoGS: Modeling Deformation Evolution for Dynamic Gaussian Splatting

**Authors:** Wei Dong, Shahram Shirani, Jun Chen, Han Zhou
**Links:** [abs](https://arxiv.org/abs/2609.00994) - [pdf](https://arxiv.org/pdf/2609.00994)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, dynamic Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

Recent extensions of 3D Gaussian Splatting (3DGS) enable real-time novel view synthesis in dynamic scenes by learning time-conditioned Gaussian deformations. However, existing MLP-based methods typically estimate deformations independently at each timestamp, making them less robust to large or abrupt motions. To address this issue, we propose \textbf{EvoGS}, a 3DGS-based dynamic reconstruction framework that models Gaussian deformation as a temporal evolution process. EvoGS maintains persistent deformation states for each Gaussian, extrapolates future states from historical deformation states, and corrects the predictions with MLP-derived observations. The correction is adaptively weighted using a temporal residual memory and evolution statistics such as deformation velocity and trajectory deviation. To further improve reconstruction quality, EvoGS introduces deformation-aware densification. Clone and split operations are performed along corrected deformation directions, while an uncertainty-aware strategy suppresses densification for Gaussians with unstable deformation histories. Experiments show that EvoGS improves dynamic novel view synthesis quality and achieves competitive performance across benchmarks.

</details>

#### 2026-09-01 - DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments

**Authors:** Ming Liao, Chao Ye, Jianing Fei, Weiyang Lin
**Links:** [abs](https://arxiv.org/abs/2609.00619) - [pdf](https://arxiv.org/pdf/2609.00619)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, scene representation, rendering, simulation

<details>
<summary>Abstract</summary>

In indoor environments, object positions frequently change due to human activities or embodied-agent interactions, causing previously constructed scene graphs to become inconsistent with the current scene. To address this issue, we propose DSG, a dynamic 3D scene graph construction framework that detects object changes and performs spatial relationship reasoning. First, we construct a semantic-aware 3D Gaussian scene representation and develop a dual-view rendering-based object change detection method to enable reliable scene graph node updates. Second, we propose a spatial relationship reasoning method that incorporates multi-granularity visual context, enabling a large language model to identify a richer set of interobject spatial relationships. Furthermore, we introduce DynTHOR, a dynamic indoor scene graph benchmark built on the AI2-THOR simulation platform for evaluating scene graph construction in dynamic environments. Extensive experiments on Dyn-THOR, 3RScan, and real-world scenes demonstrate that DSG consistently outperforms existing methods in both object node construction and spatial relationship reasoning, significantly improving the accuracy of dynamic scene graph construction.

</details>

### 2026-08

#### 2026-08-31 - SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting

**Authors:** Haozheng Yu, Xinyu Yang, Rundong Luo, Jennifer J. Sun, Bharath Hariharan
**Links:** [abs](https://arxiv.org/abs/2608.31023) - [pdf](https://arxiv.org/pdf/2608.31023)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting
- 作者：Haozheng Yu, Xinyu Yang, Rundong Luo, Jennifer J. Sun, Bharath Hariharan
- 出版日期：2026-08-31
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.31023

### 一句话总结
本文提出语义运动图（Semantic Motion Graph, SMG），通过低秩语义运动建模单目动态高斯场景，以缓解无约束区域的过拟合与运动不确定性。

### 研究问题
动态高斯泼溅在单目视频重建中常对训练视角过拟合，在遮挡或复杂运动场景下因缺乏可靠正则化信号而失效。如何在弱约束区域获得可靠的运动建模？

### 核心思路/方法
- 关键洞察：真实场景运动具有语义一致性——空间接近且语义相关的区域往往具有相似动态。
- 构建语义运动图（SMG），将高斯运动建模为低秩语义运动：高斯运动由SMG节点驱动。
- 针对运动不确定性的来源（不可靠的现成先验和优化中弱约束区域），利用可靠图节点引导邻近不可靠节点的运动。

### 主要贡献
- 提出SMG方法，将高斯运动建模为低秩语义运动，利用语义一致性约束动态场景。
- 通过可靠节点引导不可靠节点，解决运动不确定性问题。
- 引入新的多视角数据集（ego-exo采集设置），用于评估现实场景下的动态高斯泼溅。
- 在多个具有挑战性的真实世界基准上达到单目动态高斯泼溅的最新性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目动态场景重建中的过拟合和弱约束问题提出新方法，具有明确的问题动机和创新点（语义驱动低秩运动建模），并附带新数据集，对动态场景建模方向具有较大参考价值。

</details>

<details>
<summary>Abstract</summary>

We study dynamic Gaussian Splatting from monocular videos. While recent advancements in dynamic Gaussian splatting offer a promising foundation for modeling dynamic scenes, they often overfit to the training views and fail under occlusion or complex scene motion due to the lack of reliable regularization signals in under-constrained regions. We propose Semantic Motion Graph (SMG), a novel approach models the Gaussian motion as the low-rank semantic motion. Our key insight is that the real-world scene motion is often structured by semantic coherence: regions that are spatially close and semantically related tend to exhibit consistent dynamics. To leverage this prior, we construct SMG to model structured motion of the scene. The Gaussian motion is driven by the motion of SMG nodes. We further observe that the uncertainty of Gaussian motion arises from both unreliable off-the-shelf priors and weakly constrained regions during optimization. SMG addresses this by using reliable graph nodes to guide the motion of nearby unreliable nodes. To evaluate dynamic Gaussian splatting under challenging real-world scenarios, we introduce a new multiview dataset collected under an ego-exo setup. Extensive experiments demonstrate that SMG achieves state-of-the-art performance on monocular dynamic Gaussian splatting across challenging real-world benchmarks. Project page: https://smg-gaussian.github.io/.

</details>

#### 2026-08-31 - Amortized Anchor Refinement for Deployable Continuous-Time 4D Gaussian Reconstruction

**Authors:** Jingong Chen, Qingwen Zhang, Sanghyeon Jun, Chulwoo Pack, Kyle Gao, Kwanghee Won
**Links:** [abs](https://arxiv.org/abs/2608.30218) - [pdf](https://arxiv.org/pdf/2608.30218)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, scene flow, 4D Gaussian

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Amortized Anchor Refinement for Deployable Continuous-Time 4D Gaussian Reconstruction
- 作者：Jingong Chen, Qingwen Zhang, Sanghyeon Jun, Chulwoo Pack, Kyle Gao, Kwanghee Won
- 出版日期：2026-08-31
- 分类：Dynamic / 4D Reconstruction（次要：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.30218

### 一句话总结
本文提出一种面向可部署连续时间4D重建的“摊销锚点细化”方法，通过冻结骨干网络加短时优化，在固定计算预算下实现高质量重建，并可直接在独立XR头显上播放。

### 研究问题
如何使连续时间4D重建在独立XR头显等部署设备上变得可行，同时避免逐场景优化带来的过高计算成本，并解决前馈预测难以恢复场景细节的问题。

### 核心思路/方法
- 使用**冻结的骨干网络**预测初始高斯表示，获得快速的前馈估计。
- 在此基础上进行**短时、固定预算的优化**，专门化该表示以恢复场景细节。
- 引入**容量下限（capacity floor）**机制，保持表示密度，防止低预算下重建坍缩。
- 在无训练阶段，应用**持久同调约束**修剪不稳定的高斯体，同时保留拓扑持久结构。
- 将修剪后的轨迹直接作为**场景流**输出，用于最终渲染。

### 主要贡献
- 提出摊销锚点细化框架，结合前馈预测与短时优化，兼顾效率与细节恢复。
- 设计容量下限机制，确保低计算预算下不会发生重建坍缩。
- 提出训练无关的持久同调约束策略，用于稳定高斯修剪与结构保持。
- 在Stage-Capture基准上达到24.31±2.22dB，并在单个消费级GPU上完成目标预算内重建，实现XR头显端播放。

### 局限性
摘要未提供足够信息，未涉及方法在不同场景泛化性、处理大规模动态场景的显存需求、与现有全优化方法的性能差距的具体量化对比，以及持久同调约束在极端动态或稀疏视角下的鲁棒性。

### 阅读优先级
**高**
理由：论文面向XR头显等实际部署场景，提出结合前馈与短时优化的新范式，且报告了端到端可用结果（消费级GPU重建、头显播放），对4D重建与实时渲染方向具有较强实用价值。核心方法（摊销细化+拓扑约束）具备一定新颖性，值得深入阅读。

</details>

<details>
<summary>Abstract</summary>

Continuous-time 4D reconstruction remains impractical on standalone XR headsets. Per-scene optimization demands deployment-infeasible compute, and lower budgets cause collapse rather than degrade gradually. Feed-forward prediction is fast, but struggle to recover scene-specific detail. We present Amortized Anchor Refinement, which uses a frozen backbone to predict an initial Gaussian representation and a short optimization to specialize it under a fixed compute budget, with a capacity floor preserving representational density. A training-free stage then applies a persistent-homology constraint to prune unstable Gaussians while preserving topologically persistent structures, and streams the resulting trajectories directly as scene flow. On the Stage-Capture benchmark, Amortized Anchor Refinement achieves 24.31$\pm$2.22dB, while our deployment experiments demonstrate reconstruction within the target budget on a single consumer GPU and playback on a standalone XR headset.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-01 - Seeing the World and the Self from Egocentric Video

**Authors:** Kai Guan, Minchao Jiang, Ruichen WangLi, Wentao Zhu, Lei Zhang
**Links:** [abs](https://arxiv.org/abs/2609.01276) - [pdf](https://arxiv.org/pdf/2609.01276)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** geometry foundation model, scene reconstruction, depth estimation

<details>
<summary>Abstract</summary>

Complete 3D perception from egocentric video requires recovering the surrounding scene and the wearer's full-body motion in a shared metric frame. Existing methods typically address scene reconstruction and motion estimation separately: scene reconstruction methods ignore the wearer, whereas motion estimation methods lack explicit scene geometry and often depend on external trajectories. Joint recovery is challenging because the two tasks exhibit asymmetric visibility and require different prediction paradigms. The largely visible scene supports deterministic geometric regression, whereas the severely occluded body requires generative motion inference. We therefore propose RESELF (REconstructing the Scene and the sELF), a unified framework that couples deterministic metric geometry reconstruction with geometry-conditioned motion generation. RESELF adapts a geometry foundation model pre-trained on large-scale exocentric data to egocentric video using frame-wise scale and relative-pose consistency objectives. The resulting camera trajectory and latent geometric features condition a diffusion model that recovers the wearer's motion. A subsequent closed-loop kinematic feedback stage further refines the camera head while preserving the reconstructed scene geometry. To support training and evaluation, we curate EE4D-JSM from EgoExo4D by aligning egocentric video, sparse metric scene geometry, camera trajectories, and full-body motion annotations. Experiments show that RESELF outperforms state-of-the-art methods designed for the individual tasks across depth estimation, camera tracking, and full-body motion estimation. Code, models, and datasets will be available at https://ka1guan.github.io/RESELF/.

</details>

#### 2026-09-01 - Monocular Depth Estimation from a Single Image: Progress and Opportunities

**Authors:** Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun, Yi-Hua Huang, Ziyi Yang, Peng Dai, Xiaojuan Qi
**Links:** [abs](https://arxiv.org/abs/2609.01172) - [pdf](https://arxiv.org/pdf/2609.01172)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, 3D reconstruction, SLAM, visual SLAM, depth estimation, monocular depth, robotics, robot perception, autonomous driving, augmented reality

<details>
<summary>Abstract</summary>

Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing the problem, distinguishing between relative and metric depth estimation, and highlighting the key challenges that have shaped a decade of research. We then present common problem formulations and introduce the most widely used datasets, covering indoor, outdoor, and synthetic data. Following this, we review major advances prior to the foundation model era, distilling core insights from influential methods that contributed to improvements in accuracy, efficiency, and robustness. The survey then turns to the recent surge of foundation-model-based approaches, categorizing them into discriminative and generative paradigms and emphasizing the critical roles of large-scale pretraining (e.g., DINOv3) and synthetic data. We compare representative models using both quantitative benchmarks and qualitative examples, and discuss natural extensions to video-based depth estimation. Further, to illustrate real-world impact, we highlight the integration of depth estimation into applications such as visual SLAM, content generation, and robot perception. Finally, we outline open challenges and promising research directions as the field advances further into the era of foundation models.

</details>

#### 2026-09-01 - Adaptive Depth-Map-Guided Bundle Adjustment for Correspondence-Free Multi-View Point Cloud Registration

**Authors:** Yiran Zhou, Yingyu Wang, Shoudong Huang, Liang Zhao
**Links:** [abs](https://arxiv.org/abs/2609.01089) - [pdf](https://arxiv.org/pdf/2609.01089)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, bundle adjustment, robotics

<details>
<summary>Abstract</summary>

Robotic processing of irregular steel scrap requires dense 3-D measurement to replace manual visual assessment in hazardous cutting workcells. The reconstructed map is used to estimate piece dimensions, boundary geometry, feasible preheating and cutting regions, and collision-aware torch paths. The reconstruction errors therefore propagate directly to downstream measurement and planning. Existing multi-view registration methods commonly rely on feature extraction and data association to establish correspondences between views. In workcells with smooth metallic surfaces, repeated structures, occlusions, and partial overlaps, however, wrong correspondences may be established, leading to inaccurate pose estimation and distorted reconstruction. This paper presents an adaptive layered depth-map-guided bundle adjustment framework for correspondence-free multi-view point cloud registration. The scene is represented by a global 2.5-D grid, where each cell can adaptively maintain multiple depth hypotheses. Raw depth observations are directly projected into the global map to form depth constraints without explicit feature correspondences. At grid cells where multiple surfaces produce conflicting depths, a softmax-based layer assignment links each observation to compatible depth hypotheses. The resulting nonlinear least-squares formulation jointly refines sensor poses and the layered depth map, with correspondences implicitly induced by the depth-map representation and projection model. Experiments on self-collected industrial datasets show that the proposed method achieves consistently competitive reconstruction accuracy while maintaining robustness and low computational cost in challenging industrial scenarios. We release the open-source code implementation at: https://github.com/YiranZhou-Robotics/ADM-BA.git

</details>

#### 2026-09-01 - On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios

**Authors:** Zhe Shen, Liyuan Lou, Yifei Yu, Guanbo Wang, Quanjian Ji, Xin Wang, Zongqian Zhan
**Links:** [abs](https://arxiv.org/abs/2609.00923) - [pdf](https://arxiv.org/pdf/2609.00923)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, rendering, mapping

<details>
<summary>Abstract</summary>

While feed-forward 3D reconstruction (3R) offers efficient end-to-end modeling, its application in large-scale UAV mapping is hindered by the prohibitive memory cost of Transformer attention. Current scalable streaming 3R methods assume temporally and spatially continuous inputs, rendering them ineffective for the weakly ordered or unordered image streams common in cross-strip UAV operations. To address this, we propose On-the-Fly3R, a training-free, progressive online 3D reconstruction framework for large-scale UAV images that upgrades various 3R backbones for large-scale UAV scenarios. Our method enables reconstruction from unordered inputs via retrieval-guided dynamic subset construction, which adaptively selects spatially relevant images. To further improve the robustness, a validation-rejection-retry mechanism is designed to guarantee global consistency, performing a pre-integration consistency check and automatically rejecting misaligned images and retrying with alternative subset. Finally, inspired by VSLAM, pose graph optimization based on the retrieval loop closure is employed to mitigate camera drift. Evaluations on several UAV benchmarks show that our On-the-Fly3R successfully scales various 3R models to over 5,000 images across square-kilometer UAV scenes, delivering substantially superior accuracy compared to several SOTA streaming 3R methods. Code is available at https://github.com/Sh1nZzz/On_the_Fly3R

</details>

#### 2026-09-01 - Efficient and Robust Absolute Pose Estimation via Gravity-Prior-Driven Transformation Decoupling and Pose Refinement

**Authors:** Hu Cao, Qianyi Yang, Xinyi Li, Jiong Liu, Yinlong Liu, Alois Knoll
**Links:** [abs](https://arxiv.org/abs/2609.00713) - [pdf](https://arxiv.org/pdf/2609.00713)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Estimation of the absolute pose of an object is an essential task for various robotic applications. Recently, incorporating gravity direction as prior information has emerged as a popular approach to simplify absolute pose estimation. However, developing a robust and efficient algorithm to solve this challenging problem remains a difficult question due to large amounts of mismatches. In addition, obtaining an accurate pose solution from selected inlier correspondences with gravity prior is still a research gap. In this paper, we propose a novel transformation strategy that exploits geometric relations derived from the gravity prior. Through transformation decoupling, the original 6 degrees of freedom (DoF) absolute pose estimation problem is simplified into a 4-DoFs problem: 1-DoF for the rotation angle and 3-DoFs for translation, significantly improving the efficiency. For the 1-DoF rotation angle, we apply a one-dimensional global voting algorithm for optimal estimation. Once the optimal rotation is obtained, the mismatched correspondences are preliminarily filtered, and translation estimation, a linear problem, can be easily solved. Furthermore, to obtain accurate pose results, we introduce a novel pose refinement algorithm to enhance the accuracy of both rotation and translation. Extensive experiments on synthetic data and three publicly available real-world datasets (TUM RGB-D, ETH3D, and RobotCar) demonstrate that the proposed method achieves stronger performance compared to existing state-of-the-art (SOTA) approaches. To further validate our method, we integrated it into ORB-SLAM2. The results on the KITTI dataset show it effectively reduces drift and improves trajectory alignment during relocalization. The source code will be released upon acceptance.

</details>

### 2026-08

#### 2026-08-31 - Real-Time Video Anomaly Detection Using YOLO Pose Estimation and CLIP-Based Semantic Scoring

**Authors:** Vanodhya G. Warnasooriya, Amir Hajian, Watchara Ruangsang, Supavadee Aramvith
**Links:** [abs](https://arxiv.org/abs/2608.31074) - [pdf](https://arxiv.org/pdf/2608.31074)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-Time Video Anomaly Detection Using YOLO Pose Estimation and CLIP-Based Semantic Scoring
- 作者：Vanodhya G. Warnasooriya, Amir Hajian, Watchara Ruangsang, Supavadee Aramvith
- 出版日期：2026-08-31
- 分类：3D Reconstruction & Multi-view Geometry（主要类别）；无次要类别
- 链接：https://arxiv.org/abs/2608.31074

### 一句话总结
本文提出一个两阶段轻量级实时视频异常检测框架，利用YOLO v11n-pose提取人体关键点，并通过CLIP对裁剪人物区域与预定义异常行为文本进行语义相似度评分，在保持较高AUROC的同时实现了约51 FPS的端到端吞吐量。

### 研究问题
如何在不依赖光流、独立姿态估计器和基于密度的评分模块的情况下，设计一个轻量且实时的视频异常检测框架，同时维持可接受的检测精度。

### 核心思路/方法
- 第一阶段：使用YOLO v11n-pose在单次前向传播中检测人物并提取17个骨骼关键点。
- 第二阶段：将每个人物裁剪区域通过CLIP ViT-B/32编码，并与预定义的异常行为文本描述计算余弦相似度，以此进行语义评分。
- 整体架构取消了光流、独立姿态估计器和密度评分模块，实现端到端检测。

### 主要贡献
- 提出一个轻量级两阶段框架，简化了传统视频异常检测的复杂流程。
- 在CUHK Avenue、ShanghaiTech Campus以及朱拉隆功大学自建的室内数据集上进行了实验验证。
- 在NVIDIA Titan XP GPU上实现约51 FPS的端到端吞吐量，相比多特征基线获得3.36倍加速。
- 在三个数据集上分别取得89.26%、70.26%和84.13%的帧级AUROC。

### 局限性
摘要未提供足够信息。摘要未说明模型在特定异常类型上的表现差异、失败案例、对光照/遮挡等环境条件的鲁棒性、以及CLIP文本描述设计对结果的影响程度。

### 阅读优先级
**中**。理由：该工作结合了当前主流的人体姿态估计和CLIP语义特征，思路简洁且实时性突出，适合关注高效视频异常检测的读者；但上海科技大学的AUROC仅为70.26%，精度表现一般，且摘要未提供与SOTA的全面对比细节，因此优先级为中等。

</details>

<details>
<summary>Abstract</summary>

We propose a lightweight two-stage framework for real-time video anomaly detection. The first stage employs YOLO v11n-pose to detect persons and extract seventeen skeletal keypoints in a single forward pass. The second stage encodes each cropped person region through CLIP ViT-B/32 and computes cosine similarity against predefined textual descriptions of anomalous behaviors. This architecture eliminates the need for optical flow, standalone pose estimators, and density-based scoring modules. Experiments on CUHK Avenue, ShanghaiTech Campus, and a custom indoor dataset collected at Chulalongkorn University demonstrate an end-to-end throughput of approximately 51 FPS on an NVIDIA Titan XP GPU, a 3.36x speedup over the multi-feature baseline, while maintaining frame-level AUROC values of 89.26%, 70.26%, and 84.13%, respectively.

</details>

#### 2026-08-31 - Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling

**Authors:** Minghan Qin, Yuang Wang, Xiuyu Yang, Yushi Long, Yujian Zhang, Ruihuan Wang, Kai Ye, Yangang Zhang, Hang Li
**Links:** [abs](https://arxiv.org/abs/2608.30821) - [pdf](https://arxiv.org/pdf/2608.30821)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, pose estimation, embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling
- 作者：Minghan Qin, Yuang Wang, Xiuyu Yang, Yushi Long, Yujian Zhang, Ruihuan Wang, Kai Ye, Yangang Zhang, Hang Li
- 出版日期：2026-08-31
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：https://arxiv.org/abs/2608.30821

### 一句话总结
Lucida提出了一种“解析-生成-放置”的可组合真实到仿真场景建模流水线，通过重新分配各步骤的输入要求，使每步仅依赖真实捕获中可靠提供的信息，最终在场景级检测、位姿估计和重建等任务上显著优于现有方法。

### 研究问题
如何在杂乱的真实室内场景捕获中，恢复出“完整、可编辑、按观测排列”的物体资产，以构建可直接用于机器人仿真和具身AI的仿真场景副本——即解决现有“解析-生成-放置”三步管线中每一步都因真实捕获不理想（实例几何不精确、视角遮挡、资产与观测不匹配）而失败的问题。

### 核心思路/方法
Lucida保持“解析-生成-放置”的顺序，但重新分配了各步骤对输入的要求，使每步只消费真实捕获中可靠提供的信息，并将精度需求推迟到管线末端而非在起点强求。具体来说：
- **解析**：将视频解析为场景图，图中节点携带每个实例的多视角证据；
- **生成**：根据每个实例的多视角证据，生成该实例的完整资产；
- **放置**：使用GizmoAct（一个视觉语言模型策略），将放置问题转化为多轮GUI交互，通过闭环地操作物体的gizmo并在自身判断对齐达成时停止，完成资产放置。

### 主要贡献
- 提出Lucida，一种可组合真实到仿真场景建模的新流水线，其核心思想是重新分配各步骤的输入要求，使每一步仅依赖真实捕获中可靠提供的信息；
- 提出GizmoAct，一种基于视觉语言模型的放置策略，将物体放置建模为多轮GUI交互，支持闭环对齐和自主终止；
- 实验结果表明：在场景级3D物体检测上，Lucida在R2S-Scene上相对Boxer的mAP提升69%；在CA-1M上，ADD-SB@0.05从57.8%提升至83.4%；场景重建F-Score从SAM3D的0.794提升至0.924。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对真实到仿真场景建模这一对机器人仿真和具身AI有直接应用价值的任务，提出了一种重新分配各步骤要求的新颖流水线，并在三个任务上均取得了大幅度的性能提升（如mAP提升69%、ADD-SB提升约25个百分点、F-Score从0.794升至0.924），改进效果显著，值得重点关注。

</details>

<details>
<summary>Abstract</summary>

Composable scene modeling aims to recover a real indoor scene as complete, editable object assets arranged as observed, giving robot simulation and embodied AI a simulation-ready replica of the real environment whose objects can be manipulated individually. Existing pipelines decompose the task into three steps---parse the observations into instances, generate an asset for each, and place each asset back---but every step presumes an input that a cluttered capture rarely provides: accurate instance geometry, unoccluded views, and assets that accurately match the observations. We propose Lucida, which keeps this order but redistributes the requirements, so each step consumes only what a real capture reliably provides and precision is reached at the end of the pipeline rather than demanded at its start. Lucida parses the video into a scene graph whose nodes carry per-instance multi-view evidence, generates a complete asset for each instance from its evidence, and places assets with GizmoAct, a VLM policy that casts placement as multi-turn GUI interaction, manipulating the object's gizmo in a closed loop and deciding itself when alignment is reached. Across scene-level 3D object detection, object pose estimation, and scene reconstruction, Lucida improves mAP over Boxer by 69% on R2S-Scene, raises ADD-SB@0.05 from 57.8% to 83.4% on CA-1M, and increases scene F-Score from 0.794 for SAM3D to 0.924.

</details>

#### 2026-08-31 - Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions

**Authors:** Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper
**Links:** [abs](https://arxiv.org/abs/2608.30690) - [pdf](https://arxiv.org/pdf/2608.30690)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions
- 作者：Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper
- 出版日期：2026-08-31
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.30690

### 一句话总结
本文系统比较了单目SLAM系统在合成退化与真实恶劣条件下的表现，发现学习型跟踪器倾向于将灾难性丢失转化为持续漂移，且合成退化的物理保真度直接影响对真实世界系统排序的预测能力。

### 研究问题
合成退化压力测试能否有效替代真实世界恶劣条件，用于单目SLAM的鲁棒性评估？特别是，不同退化类型（图像空间、几何感知、复合）下，经典特征法与学习型跟踪器的失败模式（显式跟踪失败 vs 漂移积累）有何差异？

### 核心思路/方法
- 评估对象：一个经典特征法SLAM系统 + 两个学习型跟踪器。
- 退化类型：图像空间退化、几何感知退化、复合退化，以及与4Seasons真实恶劣条件的对比。
- 评估方式：不将鲁棒性简化为单一轨迹误差，而是区分“显式跟踪失败”与“方法保持运行但积累的漂移”两类行为。
- 核心比较：检验合成退化是否能得出与真实条件相同的工程结论（如系统排序是否一致）。

### 主要贡献
- 提出将“跟踪失败”与“漂移”分离评估单目SLAM鲁棒性的视角。
- 发现学习型跟踪器在退化下主要将灾难性丢失转化为持续性（有时严重）漂移。
- 揭示合成退化的物理保真度影响工程结论：结构化雨和雾代理能保持真实世界中的系统排序，而简单光照代理则不能。
- 提供代码开源：https://github.com/abhaythomas/master_thesis_vslamlab_robustness

### 局限性
摘要未提供足够信息（例如：未说明具体数据集规模、各退化参数设置、量化指标细节、失败/漂移的具体阈值或度量方式，以及经典方法在大幅退化下是否完全失效等）。

### 阅读优先级
**高**。理由：该工作直接挑战合成退化测试的效度假设，对SLAM鲁棒性评估方法论有重要参考价值；且发现学习型系统“以漂移换失败”的行为模式，对选择/开发鲁棒视觉里程计有实际指导意义。

</details>

<details>
<summary>Abstract</summary>

Visual SLAM is commonly evaluated on clean trajectories, although deployment failures are often caused by adverse weather, illumination, blur, and sensor artifacts. Controlled corruptions are attractive because they isolate such factors, but a synthetic stress test is useful only when it leads to the same engineering conclusion as the condition it is intended to approximate. This work examines that question for monocular SLAM. We evaluate a classical feature-based system and two learned trackers under image-space, geometry-aware, and compound corruptions, and compare their behavior with adverse conditions from 4Seasons. Rather than reducing robustness to a single trajectory error, the evaluation separates explicit tracking failure from drift accumulated by methods that remain active. The results show that learned trackers largely replace catastrophic loss with sustained, and sometimes severe, drift. More importantly, the apparent ordering of the learned systems changes with the physical fidelity of the corruption: structured rain and fog proxies preserve the real-world ordering, whereas a simple illumination proxy does not. Code is available at: https://github.com/abhaythomas/master_thesis_vslamlab_robustness.

</details>

#### 2026-08-31 - Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention

**Authors:** Bingde Liu, Wu Ran, Jinglei Zhang, Huanhuan Yuan, Chao Ma
**Links:** [abs](https://arxiv.org/abs/2608.30129) - [pdf](https://arxiv.org/pdf/2608.30129)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention
- 作者：Bingde Liu, Wu Ran, Jinglei Zhang, Huanhuan Yuan, Chao Ma
- 出版日期：2026-08-31
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.30129（PDF: https://arxiv.org/pdf/2608.30129）

### 一句话总结
本文提出Lapis，一种基于线性注意力的像素空间单步扩散生成框架，在保持高精度深度估计的同时大幅降低推理延迟。

### 研究问题
生成式框架在单目深度估计中表现优异，但其标准注意力的O(N²)复杂度和多步去噪过程在扩展到高分辨率图像时计算成本过高。如何在不牺牲结构一致性和细节质量的前提下，实现高效的一步式生成深度估计，是本文要解决的核心问题。

### 核心思路/方法
Lapis采用粗到细的层级设计：
- **Patch-level Consistency Module**：通过整合语义和空间先验来恢复结构的连贯性；
- **Pixel-level Refinement Module**：利用基于跳跃连接的像素对应关系恢复清晰的几何边界；
- **直接x预测策略**：借助流形假设，通过直接预测干净数据流形来减轻单步扩散中的采样噪声。

### 主要贡献
- 提出Lapis框架，将线性注意力与像素空间单步扩散结合，实现高效深度估计；
- 通过粗到细的模块设计，解决了直接应用线性注意力和一步预测导致的结构不一致、细节丢失和噪声问题；
- 在多个基准上达到SOTA精度和边界清晰度，推理延迟相比此前SOTA生成模型在1080P下降低最多7.6倍、在1440P下降低最多10.9倍。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的失败案例、对特定场景（如弱纹理、动态物体）的鲁棒性、训练成本或模型参数量等潜在局限。

### 阅读优先级
**高**。理由：该工作直接针对生成式深度估计的计算瓶颈提出解决方案，在精度和效率上均取得显著改进，且适用于高分辨率场景，对从事深度估计、生成模型及高效注意力机制研究的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

This work presents $\textbf{Lapis}$, a $\textbf{l}$inear-$\textbf{a}$ttention-based $\textbf{pi}$xel-$\textbf{s}$pace generative framework that achieves efficient and high-fidelity depth estimation with one-step diffusion. While generative frameworks have significantly advanced monocular depth estimation with superior detail fidelity, the $\mathcal{O}(N^2)$ complexity of standard attention and the multi-step denoising process introduce prohibitive computational costs when scaling them to high-resolution image applications. Although linear attention and one-step prediction are intuitively viable, directly applying them leads to poor structural consistency, detail loss, and noise. Lapis rectifies these limitations through a coarse-to-fine hierarchy. Specifically, a Patch-level Consistency Module restores structural coherence by integrating semantic and spatial priors. Subsequently, a Pixel-level Refinement Module recovers sharp geometric boundaries via skip-connection-based pixel correspondence. Furthermore, to mitigate sampling noise inherent in one-step diffusion, we leverage the manifold assumption and adopt a direct $\mathbf{x}$-prediction strategy to target the clean data manifold. Extensive evaluations on multiple benchmarks demonstrate that Lapis consistently achieves state-of-the-art (SOTA) accuracy and boundary sharpness across various resolutions, reducing inference latency by up to 7.6$\times$ at 1080P and 10.9$\times$ at 1440P resolution compared to previous SOTA generative models.

</details>

#### 2026-08-30 - GeoRay: Gauge-Aware Feed-Forward Satellite 3D Reconstruction in the Geodetic Frame

**Authors:** Zhe Dong, Wanqing Wu, Yuzhe Sun, Haochen Jiang, Yuchen Ma, Lecheng Ren, Tianzhu Liu, Yanfeng Gu
**Links:** [abs](https://arxiv.org/abs/2608.29680) - [pdf](https://arxiv.org/pdf/2608.29680)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, photogrammetry

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoRay: Gauge-Aware Feed-Forward Satellite 3D Reconstruction in the Geodetic Frame
- 作者：Zhe Dong, Wanqing Wu, Yuzhe Sun, Haochen Jiang, Yuchen Ma, Lecheng Ren, Tianzhu Liu, Yanfeng Gu
- 出版日期：2026-08-30
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.29680

### 一句话总结
GeoRay 提出了一种面向卫星影像的、在大地测量坐标系下直接重建稠密地表高程的前馈三维重建方法，通过射线一致性适配器、显式基准机制和融合策略，仅需24秒即可在一张瓦片上实现绝对MAE为2.99米的重建精度。

### 研究问题
传统前馈三维基础模型针对透视相机场景，而卫星摄影测量需要在非中心有理多项式相机（RPC）模型下，在绝对大地测量坐标系中重建稠密地表高度。该任务面临三个核心挑战：预训练的透视特征沿RPC高度射线不可靠、绝对高程存在低阶基准模糊（可与传感器偏差互换）、以及单目与多视角线索在不同区域各失效。

### 核心思路/方法
- **射线一致性适配器**：使用轻量级适配器使冻结的骨干网络能够沿原生RPC射线进行特征匹配。
- **显式基准机制**：将地表起伏（relief）与绝对高程（level）分离，构造对垂直原点具有等变性的机制，使单一训练模型可同时支持零控制点、单控制点和稀疏控制点推断。
- **标定逆方差融合**：结合单目与多视角两条推理流，按各自置信度加权融合。
- 构建了绝对坐标系下的新基准（Bench），涵盖域内、跨数据集和跨城市三个层级，无需配准或测试参考泄漏即可评估绝对位置精度。

### 主要贡献
- 提出GeoRay，首个面向卫星RPC相机的、在大地测量框架下的前馈稠密高程重建方法。
- 设计射线一致性适配器，使冻结的透视预训练特征可用于非中心RPC射线。
- 提出显式基准机制，解决绝对高程与传感器偏差的低阶互换问题，实现控制点数量可变的统一推断。
- 引入标定逆方差融合策略，结合单目与多视角线索。
- 构建绝对坐标系评估基准；在26个US3D瓦片上达到2.99米绝对MAE（覆盖率91.9%），完备性感知精度较最强合规基线提升46.4个百分点，且在两个迁移场景下保持最优精度。

### 局限性
摘要未提供足够信息，无法获知该方法在极端地形、密集遮挡、大倾角成像或不同分辨率传感器上的表现，也未提及内存占用、失败模式或融合策略在特定区域的退化情况。

### 阅读优先级
**高**  
理由：该工作针对卫星摄影测量这一实际高价值场景，解决了透视预训练模型向非中心RPC相机迁移的适配问题，并提出了绝对高程基准模糊的显式处理机制。实验显示相较最强合规基线有大幅精度提升，且代码与模型将开源，值得关注其技术细节与基准设计。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D foundation models reconstruct perspective scenes in one pass. Satellite photogrammetry needs a different product, one that domain adaptation alone does not deliver: dense surface height in an absolute geodetic frame under non-central rational polynomial cameras (RPCs). Perspective-pretrained features are not reliably observable along RPC height rays, absolute elevation carries a low-order height--datum gauge exchangeable with sensor bias to first order, and monocular and multi-view cues fail in different regions. \method{} treats all three. Lightweight ray-consistent adapters make a frozen backbone matchable along native RPC rays. An explicit datum mechanism separates relief from absolute level and is equivariant to the vertical origin by construction, so one trained model serves zero-, one-, and sparse-control inference. Calibrated inverse-variance fusion combines the two relief streams. \bench{}, our absolute-frame benchmark of eighteen systems across in-domain, cross-dataset, and cross-city tiers, scores absolute placement without registration or test-reference leakage. On 26 held-out US3D tiles, \method{} attains $2.99$\,m absolute MAE at $91.9\%$ coverage, improves completeness-aware accuracy by $46.4$ points over the strongest compliant feed-forward baseline, remains the most accurate such system under both transfer shifts, and runs in $24$\,s model-forward time per tile. Code and models will be released at https://github.com/HIT-SIRS/GeoRay

</details>

#### 2026-08-27 - Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects

**Authors:** Brian De La Cruz, Aaron Y. Zhao, Maitrey Gramopadhye, Sawyer J. Lazar, Xianming Tan, Daniel Szafir, David S. Lawrence
**Links:** [abs](https://arxiv.org/abs/2608.27301) - [pdf](https://arxiv.org/pdf/2608.27301)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, photogrammetry, NeRF, neural radiance field, radiance field, Gaussian Splatting, radiance, splatting, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects
- 作者：Brian De La Cruz, Aaron Y. Zhao, Maitrey Gramopadhye, Sawyer J. Lazar, Xianming Tan, Daniel Szafir, David S. Lawrence
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.27301

### 一句话总结
该研究对比了摄影测量、NeRF、高斯溅射与LiDAR四种3D重建方法在生成实验室物品全息模型上的保真度，发现NeRF方法在透明、反光、低纹理物体上表现最优。

### 研究问题
当前的3D重建方法是否足以支持在教育场景中创建真实感强的实验室物品全息表示？四种主流重建方法（摄影测量、NeRF、高斯溅射、LiDAR）在形状、颜色、纹理和视觉缺陷等维度上的保真度如何？

### 核心思路/方法
- 选取常见实验室物品作为重建对象，分别用四种方法（摄影测量、NeRF、高斯溅射、LiDAR）生成全息模型。
- 采用重复测量设计（repeated-measures design），由研究生对生成的模型在形状、颜色、纹理和视觉缺陷四个维度进行主观评估。
- 比较不同方法在不同物体类型（特别是透明、反光、低纹理物体）上的表现差异。

### 主要贡献
- 系统比较了四种主流3D重建方法在教育全息影像场景中的适用性，填补了该应用领域的评估空白。
- 发现NeRF方法在不同物体上均能产生最稳定高保真的表示，尤其擅长处理其他方法难以捕获的透明、反光或低纹理物体。
- 揭示了形状和颜色通常比纹理重建得更成功，指出纹理是教育全息模型中的难点。
- 展示了面向AR/MR教育环境创建沉浸式学习对象的可行工作流程，支持实验前准备、空间推理和学生参与等教育目标。

### 局限性
摘要未提供足够信息。例如，未提及样本数量、评估者人数、统计分析方法、各方法的计算成本或重建时间、以及任何定量误差指标，也未说明LiDAR方法在具体物体上的失败模式细节。

### 阅读优先级
**中**  
理由：该研究对教育技术/AR/MR内容开发者和3D重建算法应用者有一定参考价值，比较了多种主流方法的实际效果，但属于应用性评估而非算法创新，方法细节有限（具体协议、指标不全），对于纯算法研究者或追求方法突破的读者优先级偏低。若您关注沉浸式教育或全息显示应用，可读性较高。

</details>

<details>
<summary>Abstract</summary>

In this study, we examined whether current 3D reconstruction methods can support the creation of realistic holographic representations of laboratory objects for educational use. In this regard, we compared four approaches: photogrammetry, a neural radiance field (NeRF)-based method, Gaussian splatting, and LiDAR. These methods were used to generate holographic models of common laboratory items and their fidelity was evaluated by graduate students. Participants assessed the models for shape, color, texture, and visual defects using a repeated-measures design. Across objects, the NeRF-based method produced the most consistently high-fidelity representations, particularly for transparent, reflective, or low-texture items that were difficult to capture with other approaches. Shape and color were generally reproduced more successfully than texture, suggesting that some visual properties remain more challenging to represent accurately in educational holograms. Beyond identifying the strengths and limitations of each reconstruction method, the study demonstrates a practical workflow for creating immersive learning objects that may support pre-laboratory preparation, spatial reasoning, and student engagement in AR/MR-based educational environments. These findings offer design-relevant insights for educators and researchers developing immersive digital learning experiences.

</details>

#### 2026-08-27 - SSMB: Self-Supervised Local Feature Detection under Motion Blur

**Authors:** Zhenjun Zhao, Fabio Bellavia, Wenting Wang, Fan Zhu, Jiajun Wu, Suryansh Kumar, Mingqiang Wei, Haoang Li, Javier Civera
**Links:** [abs](https://arxiv.org/abs/2608.27181) - [pdf](https://arxiv.org/pdf/2608.27181)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** image matching, pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SSMB: Self-Supervised Local Feature Detection under Motion Blur
- 作者：Zhenjun Zhao, Fabio Bellavia, Wenting Wang, Fan Zhu, Jiajun Wu, Suryansh Kumar, Mingqiang Wei, Haoang Li, Javier Civera
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.27181

### 一句话总结
SSMB 提出了一种无需去模糊、无需手工检测器或外部伪标签的自监督关键点检测方法，专门针对运动模糊图像，通过局部判别增强模块和两阶段训练实现模糊不变的特征检测。

### 研究问题
运动模糊会扭曲局部图像结构，降低关键点定位的可重复性；现有方法要么依赖计算昂贵的“先去模糊再检测”流程（可能引入伪影），要么在清晰图上回归手工关键点的位置（受限于手工检测器的假设），缺乏真正针对模糊可重复性的自监督方案。

### 核心思路/方法
- 整体框架：去模糊无关的自监督关键点检测器，不依赖手工检测器或外部伪标签。
- 关键模块：Local Discriminability Enhancement (LDE) 模块，用于在全局特征混合后恢复细粒度的局部判别能力。
- 两阶段训练：
  1. 几何预训练：在合成形状上通过渲染几何引导，引导出空间上具有判别性的关键点检测，无需外部检测器。
  2. 模糊感知训练：在真实清晰-模糊图像对上进行，通过多组件自监督目标（跨域一致性、几何对齐、空间覆盖）学习模糊不变检测。

### 主要贡献
- 提出首个无需去模糊、无需手工检测器和外部伪标签的自监督模糊图像关键点检测方法。
- 引入局部判别增强模块，解决全局特征混合后局部判别力不足的问题。
- 提出两阶段自监督训练策略，结合合成几何预训练和真实模糊对训练。
- 在关键点检测、图像匹配、相对姿态估计和运动模糊下的视觉定位等任务上，达到稀疏关键点检测器的新 SOTA，一致优于监督和自监督基线。

### 局限性
摘要未提供足够信息。例如，未提及方法在极端模糊、高噪声或实时性方面的具体限制，也未给出失败场景或计算开销的讨论。

### 阅读优先级
高。理由：该研究针对运动模糊下关键点检测这一长期难题，提出了一种全新的自监督方案，避免去模糊流程和手工先验，并且在多个下游任务上超越现有基线。对于从事三维重建、视觉定位、SLAM 等相关方向的研究者，该方法具有较高的参考价值。尽管摘要未给出实验细节，但整体贡献和技术路线具备较强的创新性和实用性。

</details>

<details>
<summary>Abstract</summary>

Keypoint detection under motion blur remains a significant challenge, as blur distorts local image structure and degrades the repeatability of feature localization. Existing approaches either rely on computationally expensive deblur-then-detect pipelines that may introduce restoration artifacts, or learn to regress the image positions of handcrafted keypoints extracted on sharp images, which reflects the assumptions of the handcrafted detector rather than what is truly repeatable under blur. We present SSMB, a deblur-free, self-supervised keypoint detector for motion-blurred images that requires neither handcrafted detectors nor external pseudo-labels. SSMB introduces the Local Discriminability Enhancement (LDE) module, which restores fine-grained local discriminability after global feature mixing. Training is performed in two stages. First, geometric pretraining on synthetic shapes bootstraps spatially discriminative keypoint detection without any external detector, just from the rendered geometry. Second, blur-aware training on real sharp-blur image pairs learns blur-invariant detection through a multi-component self-supervised objective that enforces cross-domain consistency, geometric alignment, and spatial coverage. Extensive evaluations on keypoint detection, image matching, relative pose estimation, and visual localization under motion blur demonstrate that SSMB establishes a new state-of-the-art among sparse keypoint detectors, consistently outperforming both supervised and self-supervised baselines across all tasks. Code, models, and datasets will be publicly available upon paper acceptance.

</details>

#### 2026-08-27 - A Geometry-Driven, Framework-Agnostic Optimization for Object Pose Estimation

**Authors:** Wei Chen, Tao Zhen, Zhongchen Shi, Jing Zhang, Liang Xie, Erwei Yin
**Links:** [abs](https://arxiv.org/abs/2608.26859) - [pdf](https://arxiv.org/pdf/2608.26859)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Geometry-Driven, Framework-Agnostic Optimization for Object Pose Estimation
- 作者：Wei Chen, Tao Zhen, Zhongchen Shi, Jing Zhang, Liang Xie, Erwei Yin
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.26859

### 一句话总结
本文提出一种基于物体主惯性轴对齐的几何驱动、数据集层面的姿态表示优化方法，在不修改网络结构的前提下提升物体姿态估计精度。

### 研究问题
如何在不依赖网络架构创新的情况下，从数据层面提升物体姿态估计的精度与鲁棒性，同时解决对称物体的旋转标签歧义问题。

### 核心思路/方法
- 提出一种新的、物理上合理的旋转表示：通过主惯性轴对齐，将物体的坐标系与其固有的几何轴（由惯性属性推导）对齐。
- 该优化完全在数据集层面进行，不涉及任何网络架构修改，具有框架无关性（Framework-Agnostic），可作为即插即用模块。
- 利用主轴的“能量最小化”特性增强表示稳定性，并对对称物体的旋转歧义在数据层面进行显式的规范化处理，从根源消除训练时的标签混淆。

### 主要贡献
1. 提出几何驱动的数据级优化方法，替代传统的模型中心式改进思路。
2. 引入基于主惯性轴的旋转表示，具备内在稳定性，对噪声和遮挡更鲁棒。
3. 在数据层面显式解决对称物体的旋转歧义问题，消除标签混淆。
4. 方法框架无关，无需修改现有网络即可应用，兼容类别级和实例级模型。
5. 大量实验表明在保持基线网络完整性的前提下，精度获得一致且显著的提升。

### 局限性
摘要未提供足够信息以评估方法的局限性，例如计算开销、对非刚性物体或极端几何形状的适用性、实验数据集的具体规模与范围均未在摘要中说明。

### 阅读优先级
**中**  
理由：该方法属于数据-centric优化方向，思路新颖且有实用价值（框架无关、即插即用），适合姿态估计领域研究者关注；但摘要未给出具体实验数值和对比基线细节，无法判断其性能提升的实际幅度与适用范围，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Current object pose estimation research remains predominantly model-centric, focusing on architectural innovations and post-processing refinements. This paper introduces a data-centric optimization by proposing a novel, physically grounded rotation representation through principal axes alignment. Our method aligns the object's coordinate system with its inherent geometric axes, derived from inertial properties, yielding three key advantages: Inherent Stability-leveraging the energy-minimizing property of principal axes provides a robust representation that is less sensitive to noise and occlusions; Symmetry-Aware Canonicalization-explicitly resolving rotational ambiguities for symmetric objects at the data level, which fundamentally eliminates label confusion during network training; and Framework Agnosticism-the optimization is applied purely at the dataset level, ensuring plug-and-play compatibility with existing networks without any architectural modification. We validate the framework across diverse category-level and instance-level models. Extensive experiments demonstrate consistent and significant accuracy improvements, while preserving the integrity of the baseline network. This work establishes a new, geometry-driven direction for enhancing pose estimation, circumventing the need for complex network redesign.

</details>

#### 2026-08-27 - DPA-I2P: Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration in Autonomous Driving

**Authors:** Wenxin Zhang, Hang Li, Zhiwei Xu, Qiankun Dong, Gang Wang, Tao Li
**Links:** [abs](https://arxiv.org/abs/2608.26589) - [pdf](https://arxiv.org/pdf/2608.26589)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, camera pose estimation, pose estimation, autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DPA-I2P: Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration in Autonomous Driving
- 作者：Wenxin Zhang, Hang Li, Zhiwei Xu, Qiankun Dong, Gang Wang, Tao Li
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26589

### 一句话总结
本文提出一种深度引导的投影对齐方法DPA-I2P，利用结构化的深度与视觉信息增强图像与点云之间的跨模态对应学习，从而提升自动驾驶场景中相机位姿估计的精度。

### 研究问题
如何解决图像与稀疏LiDAR点云之间因模态差异导致的跨模态对应学习困难，以提高图像到点云配准的准确性和鲁棒性。

### 核心思路/方法
提出DPA-I2P框架，包含三个关键设计：1）Ray-Conditioned Metric Depth Encoding（RMDE），以几何感知方式编码深度信息；2）Projection-Consistent Vision Lifting（PVL），以结构化方式利用视觉线索；3）Cross-Modal Query Pruning（CQP），在早期精细化阶段抑制不可靠的查询以提升匹配稳定性。整体方法在端到端框架中学习跨模态对齐。

### 主要贡献
1. 提出DPA-I2P，一种新颖的深度引导投影对齐方法用于图像到点云配准。
2. 设计RMDE和PVL模块，以几何感知方式而非朴素拼接方式融合深度与视觉特征。
3. 引入CQP机制，在精细化早期过滤不稳定查询，提高匹配稳定性。
4. 在KITTI和nuScenes数据集上验证有效性：KITTI上相较于最强隐式基线，RTE降低45.0%，RRE降低55.6%；nuScenes上也优于所评估的基线，显示出较好的跨场景迁移能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶中重要的图像-点云配准任务，提出了系统性的方法改进（深度引导+投影对齐+查询剪枝），并在两个主流数据集（KITTI、nuScenes）上取得显著精度提升（尤其KITTI上RTE/RRE大幅降低），同时验证了跨场景迁移性。对从事多模态配准、自动驾驶定位或3D视觉的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Image-to-Point Cloud Registration aims to estimate the camera pose of a given image within a 3D scene point cloud, which is a fundamental task in autonomous driving and large-scale outdoor localization. Recent implicit correspondence learning methods have improved registration performance by learning cross-modal alignment in an end-to-end framework, leading to more accurate camera pose estimation. However, due to the inherent modality discrepancy between images and sparse LiDAR point clouds, reliable cross-modal correspondence learning remains challenging. To address this issue, we propose Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration (DPA-I2P). Unlike naive depth or feature concatenation, Ray-Conditioned Metric Depth Encoding (RMDE) and Projection-Consistent Vision Lifting (PVL) exploit depth and visual cues in a structured, geometry-aware manner. In addition, Cross-Modal Query Pruning (CQP) suppresses unreliable queries during early refinement to improve matching stability. Experiments on KITTI and nuScenes demonstrate the effectiveness of the proposed method. On KITTI, DPA-I2P reduces RTE and RRE by 45.0% and 55.6% over the strongest implicit baseline, respectively. On nuScenes, DPA-I2P also improves registration accuracy over the evaluated baselines, suggesting better transferability to different driving scenes.

</details>

#### 2026-08-27 - Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones

**Authors:** R. Yang, Y. Bar-Shalom, H. A. J. Huang
**Links:** [abs](https://arxiv.org/abs/2608.26548) - [pdf](https://arxiv.org/pdf/2608.26548)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones
- 作者：R. Yang, Y. Bar-Shalom, H. A. J. Huang
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.26548

### 一句话总结
本文提出了一种利用无人机GPS轨迹进行静止相机标定的方法，通过参数估计同时处理GPS高度偏差、时间偏移以及相机姿态角偏差，并使用迭代最小二乘最大似然估计器实现对非同步离散轨迹的标定。

### 研究问题
如何利用无人机GPS记录的运动轨迹作为地面真值来标定静止相机的朝向角（偏航、俯仰、滚转），同时克服GPS高度不准（含未知偏差）、GPS与相机间时间不同步（存在未知时间偏移）、以及GPS轨迹时间离散需要精确插值这三个挑战。

### 核心思路/方法
- 将标定问题建模为参数估计问题，待估计向量包含GPS高度偏差、时间偏移以及相机的偏航、俯仰、滚转偏差。
- 针对非同步、时间离散的GPS轨迹，开发了一种基于迭代最小二乘算法的专用最大似然估计器。
- 通过仿真实验验证算法性能，并推荐了一种能够获得良好标定精度的无人机飞行轨迹。
- 标定精度以残余偏差相对于测量误差标准差的比例衡量，结果显示可达测量误差标准差的14%。

### 主要贡献
- 将GPS高度偏差和时间偏移纳入参数估计框架，与相机姿态角偏差联合估计，解决了两个主要挑战。
- 提出了适用于非同步时间离散GPS轨迹的迭代最小二乘最大似然估计器。
- 给出了能够实现高标定精度的推荐无人机轨迹。
- 仿真结果表明估计结果满足Cramér-Rao下界（CRLB），归一化估计误差平方在统计上可接受。

### 局限性
- 摘要未提供真实实验（如物理实验）数据与结果，仅提及仿真测试。
- 摘要未能提供算法在不同轨迹类型、噪声水平或极端场景下的鲁棒性分析细节。
- 摘要未涉及该方法对相机内参或其他相机参数（如焦距、畸变）的标定能力。
- 摘要未讨论方法在实时应用中的计算复杂度或运行时间。
- 摘要未提供失败模式或适用条件的明确边界（如GPS精度要求、无人机飞行速度限制等）。

### 阅读优先级
**中**  
理由：该论文聚焦于相机标定与无人机GPS轨迹结合的特定问题，方法上采用经典参数估计框架（最大似然 + 迭代最小二乘），对从事相机标定或无人机视觉定位的研究者有一定参考价值。然而，摘要以仿真验证为主，缺少真实实验对比及应用场景的讨论，阅读价值更多在于方法设计思路而非普适性结论。因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

This paper considers a stationary camera calibration problem, which estimates the camera orientation angles yaw, pitch and roll, using a drone trajectory recorded by a GPS. There are three challenges in using a GPS trajectory as ground truth for camera calibration. One, the altitude of GPS data is inaccurate with an unknown bias. Two, the GPS receiver and camera are not time synchronized, and there is an unknown time offset between the two systems. Three, the GPS trajectory is time-discrete and accurate interpolation is needed. This is actually an estimation problem since velocity is also needed. To address the first two challenges, we formulate the problem as a parameter estimation problem to estimate a vector consisting of the GPS altitude bias and time offset in addition to the camera yaw, pitch and roll biases. We then develop a special maximum likelihood estimator using the Iterated Least Squares algorithm which can work with a non-synchronized time-discrete GPS trajectory for the third challenge. Since the camera measurement errors are usually small, this requires a high calibration accuracy so that the residual bias error following the calibration should not be significant compared to the measurement error standard deviation. The calibration accuracy depends highly on the drone trajectory. This paper also recommends an appropriate drone trajectory which can yield a good calibration accuracy, namely, 14\% of the measurement error standard deviation. Simulation tests are conducted to demonstrate the algorithm performance. The estimation results meet the Cramer-Rao Lower Bound (CRLB) since the Normalized Estimation Error Squared w.r.t.\ the CRLB is statistically acceptable.

</details>

#### 2026-08-26 - Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots

**Authors:** Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier
**Links:** [abs](https://arxiv.org/abs/2608.26383) - [pdf](https://arxiv.org/pdf/2608.26383)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** feed-forward reconstruction, 3D reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, view synthesis, rendering, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots
- 作者：Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier
- 出版日期：2026-08-26
- 分类：3D Reconstruction & Multi-view Geometry（主）；Neural Scene Representations & Rendering（次）
- 链接：https://arxiv.org/abs/2608.26383

### 一句话总结
本文系统评测了NeRF与3D Gaussian Splatting在多种GPU平台上的训练/渲染性能，并对比了Meta SAM3D单图重建的速度与精度差距，指出实验室机器人应采用“轻量前馈重建维持实时闭环 + 重型神经重建按需调度”的分层方案。

### 研究问题
神经3D重建方法在真实实验室机器人常用的各类计算平台（从单板计算机到服务器级节点）上，能否满足物理控制回路所需的实时性？尤其是NeRF与3D Gaussian Splatting的训练和渲染效率，以及SAM3D这类前馈方法相比逐场景优化的延迟与保真度差距有多大？

### 核心思路/方法
- 构建跨平台的系统化基准测试，覆盖从单板计算机到服务器级GPU的多种计算设备。
- 在同一基准轴上评估两类方法：逐场景优化的NeRF和3D Gaussian Splatting（训练+渲染），以及Meta的SAM3D单图像重建。
- 对比这些方法的渲染质量、GPU开销、训练/推理延迟，并考察其在机器人控制回路实时性约束下的可行性。

### 主要贡献
- 首次系统性地在不同计算平台上基准测试神经3D重建方法，覆盖实验室机器人实际可能用到的设备层级。
- 定量分析显示：Gaussian Splatting渲染质量优于NeRF，但GPU成本更高；板载计算无法以交互速率完成完整逐场景优化。
- 对SAM3D的初步评估表明其可在数秒内生成合理的物体几何，但细节不一致可能影响下游操纵任务。
- 基于实验结论提出分层处理管线建议：轻量前馈重建支撑实时感知跟踪，重型神经重建在合适计算资源上选择性调度。

### 局限性
- 摘要未提供数据集规模、测试场景数量、具体设备型号及量化性能数值（如FPS、PSNR、延迟毫秒数等）等实验细节。
- 摘要未说明SAM3D评估的具体任务设置、精度度量方式以及其“细节不匹配”的具体表现类型。
- 摘要未提供基准测试的重复次数、统计显著性检验或误差分析，也未说明各方法在不同平台上的资源消耗（如显存占用）。

### 阅读优先级
**高**  
理由：该工作填补了神经3D重建在机器人实时应用场景中跨平台性能评估的空白，结论直接指向实际部署策略（分层管线），对从事具身智能、实验室自动化或实时3D视觉的读者有明确参考价值。尽管摘要缺少定量细节，但研究问题与结论的工程导向性强，适合优先阅读以获取系统性认知。

</details>

<details>
<summary>Abstract</summary>

Autonomous robots performing laboratory tasks depend on 3D reconstruction pipelines that can turn raw camera streams into actionable object representations within the latency budget of a physical control loop. Neural 3D reconstruction methods have demonstrated high-quality view synthesis, but their real-time viability across the compute platforms on which laboratory robots actually run remains poorly characterized. In this work, we present a systematic compute-platform benchmark of neural 3D reconstruction methods, evaluating NeRF and 3D Gaussian Splatting training and rendering on GPU-enabled computing devices ranging from single-board computers to server-class nodes, and place Meta's SAM3D single-image reconstruction on the same axes to quantify its latency and fidelity gap relative to per-scene optimization. Our results show that Gaussian Splatting yields higher rendering quality than NeRF at greater GPU cost, and that onboard compute is insufficient for full per-scene optimization at interactive rates. Our preliminary assessment on SAM3D indicates that it delivers plausible object geometry within seconds, but with detail mismatches that can compromise downstream manipulation. Together, these findings motivate tiered pipelines in which lightweight feed-forward reconstruction sustains the real-time perception-and-tracking loop for laboratory robots, while heavier neural reconstruction is scheduled selectively on suitable compute.

</details>

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-01 - DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting

**Authors:** Qian Wang, Yu Wang, Weiqi Li, Xinhua Cheng, Xiandong Meng, Ronggang Wang, Jian Zhang
**Links:** [abs](https://arxiv.org/abs/2609.01516) - [pdf](https://arxiv.org/pdf/2609.01516)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction and novel-view synthesis, scenarios with limited input views often lead to poor reconstruction quality and artifacts in rendered novel views. Recent efforts attempt to utilize powerful diffusion priors, yet they typically process rendered and reference views concatenated along an additional dimension in a single network. These methods overlook an inherent nature that different views should maintain appearance similarity but differ in structure due to view shifts, leading to blur caused by conflicts between the two properties. In this paper, we propose DualDiff, a novel pipeline that leverages dual diffusion priors with a Structure-Appearance Attention (SAA) module to introduce reference guidance for refining low-quality novel views rendered from flawed 3D representations. Specifically, we retain one diffusion branch to focus on extracting structural information from the low-quality novel views, while introducing another branch to ensure appearance consistency with reference views. Furthermore, we present a 3D reconstruction framework named DualDiff3D, which integrates a reliability-enhanced Render-Refine-Optimize (RRO) loop to progressively and robustly incorporate the refined novel views, yielding more accurate 3DGS. Extensive experiments demonstrate that our approach outperforms state-of-the-art methods even in the inference-only setting, with further performance gains achievable through training. Our code and pre-trained weights are available at https://github.com/Akaneqwq/DualDiff3D.

</details>

#### 2026-09-01 - MeshSplatBench: A Unified Benchmark for Triangle-Based Neural Rendering

**Authors:** Kaixuan Zhang, Minxian Li, Mingwu Ren, Xiatian Zhu
**Links:** [abs](https://arxiv.org/abs/2609.01306) - [pdf](https://arxiv.org/pdf/2609.01306)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural rendering, rendering

<details>
<summary>Abstract</summary>

Triangle-based neural rendering bridges neural scene representations and conventional graphics pipelines by optimizing explicit geometric primitives compatible with standard rasterization hardware. However, existing approaches are evaluated almost exclusively within custom research renderers, obscuring their practical deployability in production engines. To bridge this gap, we introduce \textbf{MeshSplatBench}, a unified benchmark that systematically investigates triangle-based neural rendering across the complete pipeline from native optimization to game-engine deployment. MeshSplatBench establishes a standardized evaluation protocol while preserving each method's native optimization semantics, reproducing published results within $0.8\%$ PSNR deviation. Furthermore, we introduce a hierarchical Unity deployment protocol spanning three rendering tiers: native CUDA renderers, method-specific dedicated engine shaders, and standard opaque mesh pipelines, isolating the exact fidelity losses caused by engine adaptation \textit{vs.} representation reduction. Finally, we conduct a topological audit of reconstructed surfaces, demonstrating that explicit connectivity and shared indexing alone are insufficient to guarantee production-ready assets due to prevalent non-manifold structures, fragmented components, and boundary artifacts. Overall, MeshSplatBench demonstrates that rasterizability is merely a primitive-level attribute, whereas graphics readiness requires jthe holistic alignment of representation, topology, and engine compatibility. Source code will be released.

</details>

#### 2026-09-01 - Inverse Rendering for Modeling with Line Primitives

**Authors:** Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel
**Links:** [abs](https://arxiv.org/abs/2609.00625) - [pdf](https://arxiv.org/pdf/2609.00625)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, inverse rendering, rendering, radiance, simulation

<details>
<summary>Abstract</summary>

Faithfully capturing diverse real-world objects with fuzzy, anisotropic structures, such as hair, fur, fibers, and textiles, for efficient real-time visualization remains challenging. Recent radiance field reconstruction methods capture these structures from multi-view images using translucent volumetric primitives such as 3D Gaussians rather than opaque low-dimensional primitives (e.g., triangles, line segments, and polylines), thereby limiting compatibility with standard depth-tested rasterization, reflection modeling, and physical simulation. We present an inverse rendering method for reconstructing fuzzy geometry using explicit line segments, which are rasterized on a subpixel grid for anti-aliasing to reproduce a semi-transparent appearance. While straightforward to render, optimizing numerous line primitives to match target images poses a significant challenge. We address this by introducing a stochastic differentiable rasterizer for line segments that produces informative gradients with respect to vertex positions, attributes, and discrete connectivity. Experiments on synthetic and real-world datasets show that our method outperforms surface-based approaches in capturing fuzzy boundaries and achieves quality comparable to volumetric representations while relying entirely on explicit geometry. The resulting representation integrates seamlessly with standard graphics pipelines, enabling cross-platform rendering, various shading models, and physical simulation.

</details>

### 2026-08

#### 2026-08-31 - VCAR: Training-Free 3DGS Segmentation via View Completeness and Axis-Aware Boundary Refinement

**Authors:** Kun Cao, Di Wang, Haibin Zhu, Haozhi Huang, Xu Wang, Zheng Shi, Guanghua Yang
**Links:** [abs](https://arxiv.org/abs/2608.30870) - [pdf](https://arxiv.org/pdf/2608.30870)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VCAR: Training-Free 3DGS Segmentation via View Completeness and Axis-Aware Boundary Refinement
- 作者：Kun Cao, Di Wang, Haibin Zhu, Haozhi Huang, Xu Wang, Zheng Shi, Guanghua Yang
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30870

### 一句话总结
VCAR 提出一种无需训练的 3D 高斯泼溅（3DGS）分割方法，通过可见性加权多视角投票、球面螺旋采样补全视角以及轴感知边界细化，实现粗到精的精确分割，并显著降低训练开销。

### 研究问题
现有 3DGS 语义分割方法依赖特征蒸馏，导致每个场景需要大量训练开销且分割边界模糊。本文指出边界伪影部分源于视点覆盖不足和各向异性高斯原语的边界溢出，旨在无需训练的情况下提升分割精度和效率。

### 核心思路/方法
VCAR 采用粗到精的两阶段策略：
- **粗阶段**：基于可见性加权的多视角投票方案，快速定位目标物体。
- **细阶段**：根据粗分割结果构建以物体为中心的球体，通过球面螺旋采样（SSS）生成补充视点，在增强视点上进行多视角投票，精确细化目标边界并抑制无关 3D 高斯。
- **轴感知边界细化（ABR）**：将投影后的二维协方差分解为逐轴贡献，识别导致边界泄漏的主轴，仅沿该轴进行定向各向异性压缩，缓解各向异性原语带来的伪影。

### 主要贡献
- 提出无需训练的训练-free 粗到细 3DGS 分割框架，避免逐场景训练开销。
- 设计可见性加权多视角投票和球面螺旋采样以补全视点、精确细化边界。
- 引入轴感知边界细化机制，针对各向异性高斯原语的边界泄漏进行定向修正。
- 在 NVOS 和 LERF 数据集上达到最先进的分割精度和效率（实验细节以论文原文为准）。

### 局限性
摘要未提供足够信息。未提及方法在特定复杂场景（如遮挡严重、物体重叠或大规模场景）下的表现，也未说明内存占用、推理耗时等具体量化指标。

### 阅读优先级
**高**。理由：该工作针对 3DGS 分割中训练开销大和边界模糊的关键痛点，提出无需训练的高效方案，兼具方法创新性与实用价值，且实验验证了其有效性，对关注神经场景表示与渲染的研究者有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

Semantic segmentation in 3D Gaussian Splatting (3DGS) is crucial for advancing 3D scene understanding. Existing methods predominantly rely on feature distillation, which incurs substantial per-scene training overhead and often yields blurred segmentation boundaries. We identify that these boundary artifacts are driven in part by insufficient viewpoint coverage and boundary overflow of anisotropic Gaussian primitives. To address these challenges, we propose VCAR, a training-free coarse-to-fine segmentation strategy based on View Completeness and Axis-aware Boundary Refinement. In the coarse stage, a visibility-based weighted multi-view voting scheme rapidly localizes the target. In the fine stage, an object-centric sphere derived from the coarse result generates supplementary viewpoints via Spherical Spiral Sampling (SSS), allowing multi-view voting on the augmented views to precisely refine object boundaries and suppress irrelevant 3D Gaussians. Moreover, we introduce Axis-aware Boundary Refinement (ABR) to mitigate artifacts from anisotropic primitives. By decomposing the projected 2D covariance into per-axis contributions, ABR identifies the dominant axis responsible for boundary leakage and applies targeted anisotropic compression exclusively along that axis. Extensive experiments on NVOS and LERF demonstrate that VCAR achieves state-of-the-art segmentation accuracy and efficiency without training. Our code is available at https://github.com/DDKK0526/VCAR.

</details>

#### 2026-08-31 - ObjectSplat: Improving Mesh Fidelity and Interactivity for 3D Scenes via Object-Level Mesh Splatting

**Authors:** Minhas Kamal, Hiranya Garbha Kumar, Mahedi Kamal, Balakrishnan Prabhakaran
**Links:** [abs](https://arxiv.org/abs/2608.30423) - [pdf](https://arxiv.org/pdf/2608.30423)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ObjectSplat: Improving Mesh Fidelity and Interactivity for 3D Scenes via Object-Level Mesh Splatting
- 作者：Minhas Kamal, Hiranya Garbha Kumar, Mahedi Kamal, Balakrishnan Prabhakaran
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30423

### 一句话总结
本文提出一种“先分解再重建”的物体级网格溅射方法，将场景中的实例与背景分别重建后合成，以提升网格保真度、新视角合成质量，并支持物体级编辑和交互。

### 研究问题
现有基于溅射（splatting）的3D场景重建方法将整个场景表示为单一整体场，缺乏物体级结构，导致下游编辑和交互不可行；同时，输入扫描中未被直接观察到的区域会被周围纹理污染且无法修正，限制了网格保真度和新视角合成质量。

### 核心思路/方法
采用“分解-再重建”流程：
1. 从每一帧中分割出各个实例（物体）；
2. 将剩余部分视为背景，并进行修复（inpainting）；
3. 使用网格溅射（mesh splatting）独立重建每个实例和背景；
4. 将重建结果组合成单一场景，实现物体级可修改性和交互性。

### 主要贡献
- 提出物体级网格溅射方法，显著提升网格保真度（F-score提升超过5%）；
- 改善新视角合成质量；
- 支持物体级（逐对象）的修改性和交互性；
- 代码将公开。

### 局限性
摘要中未提供关于方法失败场景、性能瓶颈、计算成本或对真实复杂场景的鲁棒性等局限性的具体信息，因此局限性部分摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该方法针对3D场景重建的物体级结构和交互性提出明确改进，且有量化增益（F-score提升>5%），属于领域内的实际工程改进。但摘要未提供具体技术细节（如分割方法、修复策略、基准对比等），且尚未提及实验规模与下游应用验证，故适合对该方向感兴趣的读者快速了解，而非必读的高优先级论文。

</details>

<details>
<summary>Abstract</summary>

Splatting-based algorithms reconstruct photorealistic, real-time-renderable, and mesh-exportable 3D scenes from regular images, but they represent a scene as a single monolithic field. Therefore, the reconstruction has no object-level structure, leaving it infeasible for downstream editing or interaction. Moreover, regions that are never directly observed in the input scans are contaminated by the surrounding texture and left uncorrected, capping both mesh fidelity and novel-view synthesis. We propose a decompose-before-reconstruct approach: we segment the instances out of every frame, consider the remaining as background and inpaint it, reconstruct each instance and the background independently with mesh splatting, and compose them into a single scene. Our method significantly improves mesh fidelity (over a 5\% gain in F-score) and novel-view synthesis, while supporting object-wise modifiability and interactivity. The code will be made publicly available.

</details>

#### 2026-08-31 - CapFrame: Text-Instructed Viewpoint Grounding in 3D Gaussian Scenes via Geometric Pseudo Labels

**Authors:** Jirong Li, Satoshi Ikehata, Shuhei Kurita, Ikuro Sato
**Links:** [abs](https://arxiv.org/abs/2608.30342) - [pdf](https://arxiv.org/pdf/2608.30342)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CapFrame: Text-Instructed Viewpoint Grounding in 3D Gaussian Scenes via Geometric Pseudo Labels
- 作者：Jirong Li, Satoshi Ikehata, Shuhei Kurita, Ikuro Sato
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30342

### 一句话总结
本文提出新任务TIVG（文本指令视角定位）及方法CapFrame，通过将语言指令转换为几何伪标签，在3D高斯场景中优化相机位姿，使渲染画面与文本描述对齐。

### 研究问题
现有语言引导的3D场景方法多聚焦于物体级定位（确定“看什么”），但难以控制单帧画面中的“如何看”（如主体朝向或构图布局）。本文研究如何在3D高斯场景中根据文本指令确定6自由度相机位姿，使渲染出的帧与指令语义一致。

### 核心思路/方法
CapFrame采用“检索-翻译-精炼”（Retrieve-Translate-Refine）流水线：
1. **检索**：从3D高斯场景中检索相关视图，并通过多模态大语言模型（MLLMs）的问题评估（Question-Evaluation）过程对视图排序。
2. **翻译**：将文本指令转换为朝向（orientation）和布局（layout）两类几何伪标签。
3. **精炼**：利用布局损失和朝向损失，在3DGS中进行可微分的相机位姿优化。整体框架为部分可微分。

### 主要贡献
1. 提出新任务TIVG，弥补现有方法在语言引导视角控制方面的空白。
2. 提出CapFrame框架，实现从语言到几何伪标签的转换及位姿优化。
3. 在38个真实场景、135条指令上进行实验，相比启发式视角搜索和改造的轨迹生成基线，CapFrame生成的视角与文本更对齐，经由VLM指标、MLLM评估和用户研究验证。

### 局限性
摘要未提供足够信息（包括失败案例、对复杂指令的鲁棒性、计算开销、对3DGS重建质量的依赖等均未提及）。

### 阅读优先级
**高**。理由：该工作提出新的任务定义（TIVG），且方法新颖（利用几何伪标签连接语言与相机位姿优化），实验规模较大并包含多种评估方式（自动指标+人工评估），对文本驱动的3D场景交互与视图合成方向有明显推进意义。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic real-time novel view synthesis, yet placing a virtual camera to capture a desired frame remains largely manual. Existing language-guided approaches in 3D scenes mainly focus on object-centric grounding, determining what to observe but rarely controlling how it should appear in a single frame, such as subject orientation or frame layout. To address this limitation, we introduce a new task, Text-Instructed Viewpoint Grounding (TIVG), which aims to identify a 6-DoF camera pose in a 3D Gaussian scene whose rendered frame aligns with a text instruction. To solve this task, we propose CapFrame, a partially differentiable framework that converts language into geometric pseudo labels for camera pose optimization. CapFrame follows a Retrieve-Translate-Refine pipeline: it retrieves relevant views and ranks them through a Question-Evaluation process with MLLMs, translates the instruction into orientation and layout pseudo labels, and refines the camera pose via differentiable optimization with layout and orientation losses in 3DGS. Experiments on 38 real-world scenes with 135 instructions indicate that CapFrame produces viewpoints better aligned with texts than heuristic viewpoint search and adapted trajectory generation baselines, validated by VLM metrics, MLLM judges, and user studies. Code is available at: https://github.com/jirongli/CapFrame

</details>

#### 2026-08-31 - ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation

**Authors:** Jiahao Wu, Jie Liang, Die Hu, Jiayu Yang, Kaiqiang Xiong, Xiang Li, Xiaoyun Zheng, Chao Wang, Ronggang Wang
**Links:** [abs](https://arxiv.org/abs/2608.30184) - [pdf](https://arxiv.org/pdf/2608.30184)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** video reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation
- 作者：Jiahao Wu, Jie Liang, Die Hu, Jiayu Yang, Kaiqiang Xiong, Xiang Li, Xiaoyun Zheng, Chao Wang, Ronggang Wang
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30184

### 一句话总结
本文提出一种基于锚定时间高斯溅射（ATGS）的框架，通过时间条件锚点与多级特征设计，提升长序列体积视频重建的时空稳定性与视觉质量。

### 研究问题
现有体积视频重建方法在处理长序列和复杂运动时存在时间不稳定和视觉伪影问题，即如何实现对长度较长、动作复杂的动态场景进行高质量自由视角渲染。

### 核心思路/方法
- 关键洞察：用单个高斯基元显式跟踪长期复杂运动本质上是不可靠的，因此将高斯围绕时间条件锚点组织，以定位其空间和时间支持范围，降低长程运动复杂度。
- 时间窗口策略：仅激活与查询时间相关的锚点，提升可扩展性和时间连贯性。
- 多级锚点特征：使用紧凑的全局特征、局部空间特征和局部时间特征联合约束高斯生成，保障时空稳定性。

### 主要贡献
1. 提出ATGS框架，基于锚定时间高斯溅射实现长序列体积视频重建。
2. 引入时间条件锚点机制，降低长程运动跟踪的复杂性。
3. 设计时间窗口激活策略，兼顾可扩展性与时间一致性。
4. 提出紧凑的多级锚点特征编码，联合约束高斯生成，提高时空稳定性。
5. 实验表明在长序列复杂运动场景下，ATGS consistently优于已有方法。

### 局限性
摘要未提供足够信息。例如，摘要未提及计算开销、实时性、适用范围（如特定场景类型）或失败案例等限制性讨论。

### 阅读优先级
**中**。理由：该方法针对体积视频重建中长序列和复杂运动的痛点，提出了锚点+时间窗口的创新思路，具有一定学术价值；但摘要中未披露足够实验细节（如定量指标、对比基准范围等），难以评估其实际幅度提升，适合对动态场景渲染或高斯溅射方向感兴趣的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Volumetric video enables immersive free viewpoint rendering of dynamic real world scenes, yet existing methods struggle with long sequences and complex motions, often leading to temporal instability and visual artifacts. To address these challenges, we propose \ourname, a Gaussian splatting based framework for volumetric video reconstruction. Our key insight is that explicitly tracking long term complex motion with individual Gaussian primitives is inherently unstable. Instead, we organize Gaussians around time conditioned anchors that localize their spatial and temporal support, thereby reducing long range motion complexity. We further introduce a temporal windowing strategy to activate only anchors relevant to the queried time, which improves scalability and temporal coherence. In addition, to ensure spatial and temporal stability, we design a compact set of multi level anchor features that encode global features, local spatial features, and local temporal features, jointly constraining Gaussian generation. Extensive experiments demonstrate that \ourname \ consistently outperforms prior methods on long sequence volumetric videos with complex motions. Project page: https://github.com/WuJH2001/ATGS.

</details>

#### 2026-08-31 - AI-enabled Low-Cost 3D Maize Ear Morphometry Platform at Breeding Scale

**Authors:** Therin Young, Elijah Rodriguez, Lisa Coffey, Talukder Zaki Jubery, Adarsh Krishnamurthy, Patrick Schnable, Baskar Ganapathysubramanian
**Links:** [abs](https://arxiv.org/abs/2608.30161) - [pdf](https://arxiv.org/pdf/2608.30161)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AI-enabled Low-Cost 3D Maize Ear Morphometry Platform at Breeding Scale（AI驱动的低成本玉米果穗三维形态测量平台，适用于育种规模）
- 作者：Therin Young, Elijah Rodriguez, Lisa Coffey, Talukder Zaki Jubery, Adarsh Krishnamurthy, Patrick Schnable, Baskar Ganapathysubramanian
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30161

### 一句话总结
本文提出并验证了一种基于消费级相机和神经辐射场（NeRF）的低成本玉米果穗三维重建与形态测量流水线，可在育种规模下高效获取果穗长度、体积等几何指标。

### 研究问题
现有高通量表型分析平台因成本高、劳动密集且依赖专用硬件而受限，本文旨在开发一种低成本、易操作且可扩展的三维玉米果穗形态测量方案。

### 核心思路/方法
- 使用消费级数码单反相机在电动转盘和均匀LED照明下拍摄20秒视频，重建果穗密闭三维网格。
- 通过多种子COLMAP流程估计相机位姿，初始化NeRF进行三维重建。
- 利用视频中可见的已知直径圆柱支架，实现自动公制尺寸缩放和几何质量控制。
- 对300个来自玉米自交系多样群体的果穗进行验证，其中250个通过自动化处理和质量控制。
- 将骨架长度与游标卡尺测量值、凸包体积与水置换体积进行比较，评估测量准确性。

### 主要贡献
- 开发并验证了低成本三维果穗表型流水线，硬件成本约607美元。
- 操作时间从约5分钟降至每穗1分钟，下游处理全自动运行。
- 在250个果穗上，骨架长度与卡尺测量高度一致（R²=0.964，RMSE=4.68 mm）；15穗子集的凸包体积与水置换体积一致（R²=0.982，RMSE=5.26 mL）。
- 分析了长度残差与弯曲度的关系，指出残差源于测量定义差异（卡尺测弦长，骨架长度测测地弧长）。
- 为育种规模的三维果穗表型分析提供了可行基础。

### 局限性
摘要未提供足够信息，如：对未通过质量控制（约16.7%）果穗的失败原因分析、平台在不同环境或品种间的泛化性、以及与其他高吞吐量平台的直接成本效益对比均未提及。

### 阅读优先级
**中**。该研究在低成本3D表型方向具有实用价值，且验证结果扎实，适合关注作物表型、农业AI或NeRF应用的读者。但若您不从事相关领域，其创新性主要在于工程集成，而非新的算法或理论突破，优先级相应降低。

</details>

<details>
<summary>Abstract</summary>

Maize ear geometry (length, width, curvature, and volume) is closely tied to yield and grain-filling outcomes, but existing high-throughput phenotyping pipelines remain constrained by the cost, labor, and specialized hardware they require. We developed and validated a low-cost pipeline that reconstructs a watertight 3-D mesh of a maize ear from a single 20-second video captured with a consumer-grade DSLR on a motorized turntable under uniform LED illumination. Camera poses from a multi-seed COLMAP procedure initialize a Neural Radiance Field (NeRF), and a cylindrical holder of known diameter, visible in every frame, provides automatic metric scaling with downstream geometric quality control. Applied to 300 ears spanning a diverse maize inbred panel, 250 (83.3%) passed automated processing and quality control. Skeleton length agreed with manual caliper measurements across all 250 ears (R^2 = 0.964, RMSE = 4.68 mm), and convex-hull volume agreed with water-displacement volume on a 15-ear subset spanning the full size range (R^2 = 0.982, RMSE = 5.26 mL). Residual length error grew with ear curvature, whereas bounding-box height, which records the same straight-line chord as calipers, showed no such trend; the discrepancy therefore originates in the measurement definition, since calipers record the chord while skeleton length traces the geodesic arc. The capture hardware costs approximately 607 USD, and operator involvement fell from roughly five minutes to one minute per ear, with all downstream processing running unattended. The platform provides a foundation for breeding-scale 3-D ear phenotyping.

</details>

#### 2026-08-30 - When 3D Gaussian Splatting Recovers Real Surfaces

**Authors:** Songhe Wang, David Johnathan Miller
**Links:** [abs](https://arxiv.org/abs/2608.30054) - [pdf](https://arxiv.org/pdf/2608.30054)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：When 3D Gaussian Splatting Recovers Real Surfaces
- 作者：Songhe Wang, David Johnathan Miller
- 出版日期：2026-08-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30054

### 一句话总结
本文通过数学框架证明3D高斯溅射（3DGS）在角向容量受限时偏好表面一致的几何重建，而角向容量过高则可能导致错误的不透明广告牌式几何解。

### 研究问题
3D高斯溅射在什么条件下能够恢复真实场景表面，而非仅仅过拟合视角相关的外观？具体而言，几何错位与角向容量如何影响表面一致解与错误几何解之间的可辨识性。

### 核心思路/方法
作者建立了一种基于“首次命中”（first-hit）渲染抽象的数学框架，该框架将几何与外观清晰分离。利用视差效应证明几何错位会将空间纹理强制转化为高频角向信号。在此基础上，推导出一个严格的可辨识窗口：
- 若角向容量有界，表面一致解在数学上更受偏好；
- 若角向容量无限制，相同图像可被不正确的、不透明广告牌几何完美解释。

### 主要贡献
- 提出一个将几何与外观分离的首次命中渲染数学框架；
- 证明几何错位通过视差将空间纹理转化为高频角向信号的机制；
- 建立表面一致解与广告牌几何解之间的严格可辨识条件；
- 通过合成压力测试验证预测：广告牌失败恰在高角向容量处出现；
- 在真实世界数据集中表明标准采集协议下重建在SH高阶时仍保持表面一致，与理论预测吻合。

### 局限性
摘要仅提及合成实验确认了广告牌失败出现在高角向容量处，但未提供实验数据集的具体规模、评价指标、失败临界点的定量数值，也未讨论框架假设（如首次命中抽象）在真实复杂场景（遮挡、透明物体、反射表面等）中的适用边界。摘要未提供足够信息。

### 阅读优先级
**中**。理由：该论文在理论层面为3DGS的几何可辨识性提供了清晰的数学解释，对理解3DGS的失败模式有价值；但由于摘要未提供充分的定量结果、方法实现细节和广泛的实验对比，其实际工程指导意义需阅读全文后评估。适合关注3DGS理论分析的读者阅读。

</details>

<details>
<summary>Abstract</summary>

When does 3D Gaussian Splatting (3DGS) recover the true scene surface rather than just overfitting view-dependent appearance? We answer this by developing a mathematical framework based on a first-hit rendering abstraction that cleanly isolates geometry from appearance. We prove that geometric misalignment forcefully converts spatial textures into high-frequency angular signals via parallax. This establishes a strict identifiability window: if angular capacity is bounded, surface-consistent solutions are mathematically preferred; if unrestricted, the same images can be perfectly explained by an incorrect, opaque billboard geometry. Experiments on synthetic stress tests confirm this prediction, showing billboard failures emerge precisely at high angular capacities. Conversely, in the real-world datasets we evaluate under standard capture protocols, reconstructions remain surface-consistent even at high SH degrees, which is consistent with the prediction that rich spatial texture can push billboard solutions outside the tested angular-capacity range.

</details>

#### 2026-08-30 - As-Rigid-As-Possible Deformation of Gaussian Radiance Fields

**Authors:** Xinhao Tong, Tianjia Shao, Yanlin Weng, Yin Yang, Kun Zhou
**Links:** [abs](https://arxiv.org/abs/2608.29538) - [pdf](https://arxiv.org/pdf/2608.29538)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：As-Rigid-As-Possible Deformation of Gaussian Radiance Fields
- 作者：Xinhao Tong, Tianjia Shao, Yanlin Weng, Yin Yang, Kun Zhou
- 出版日期：2026-08-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.29538

### 一句话总结
本文提出一种交互式方法，通过对3D高斯辐射场进行几何编辑后再优化高斯参数，实现保持辐射场一致性的刚体（ARAP）变形，避免现有3DGS变形框架中常见的伪影。

### 研究问题
如何对3D Gaussian Splatting（3DGS）表示的对象进行变形，同时保持高斯辐射场在变形前后的一致性，从而避免因几何编辑与辐射场渲染不一致而产生的伪影。

### 核心思路/方法
- 首先对高斯体进行几何编辑（几何变形），随后进一步优化高斯参数，确保其光栅化结果与变形后的辐射场一致。
- 设计“径向特征”（radial features）数学描述变形前后的径向差异，并在辐射场中密集采样。
- 提出自适应各向异性空间低通滤波器，防止采样过程中的混叠问题，并适应非均匀采样间隔。
- 最终实现用户可交互的大尺度ARAP辐射场变形。

### 主要贡献
- 提出一种面向高斯辐射场的ARAP变形方法，兼顾几何编辑与辐射场渲染一致性。
- 设计径向特征用于量化变形前后辐射场的差异，并引入自适应各向异性低通滤波解决采样混叠。
- 保持3DGS的高渲染质量与实时效率，同时避免现有3DGS变形方法中常见的伪影。

### 局限性
摘要未提供足够信息。文中未明确讨论方法的计算开销、交互实时性具体指标、适用范围限制或失败案例等局限性细节。

### 阅读优先级
**高**。理由：该工作针对3DGS变形中的核心一致性问题提出新方法，属于当前热门的神经场景表示与渲染方向，方法新颖且有明确的问题动机，适合关注3D编辑与实时渲染的读者阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) models radiance fields as sparsely distributed 3D Gaussians, providing a compelling solution to novel view synthesis at high resolutions and real-time frame rates. However, deforming objects represented by 3D Gaussians remains a challenging task. Existing methods deform a 3DGS object by editing Gaussians geometrically. These approaches ignore the fact that it is the radiance field that rasterizes and renders the final image. The inconsistency between the deformed 3D Gaussians and the desired radiance field inevitably leads to artifacts in the final results. In this paper, we propose an interactive method for as-rigid-as-possible (ARAP) deformation of the Gaussian radiance fields. Specifically, after performing geometric edits on the Gaussians, we further optimize Gaussians to ensure its rasterization yields a similar result as the deformed radiance field. To facilitate this objective, we design radial features to mathematically describe the radial difference before and after the deformation, which are densely sampled across the radiance field. Additionally, we propose an adaptive anisotropic spatial low-pass filter to prevent aliasing issues during sampling and to preserve the field with the varying non-uniform sampling intervals. Users can interactively employ this tool to achieve large-scale ARAP deformations of the radiance field. Since our method maintains the consistency of the Gaussian radiance field before and after deformation, it avoids artifacts that are common in existing 3DGS deformation frameworks. Meanwhile, our method keeps the high quality and efficiency of 3DGS in rendering.

</details>

#### 2026-08-27 - Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS

**Authors:** Kangmin Seo, Jae-Pil Heo
**Links:** [abs](https://arxiv.org/abs/2608.26951) - [pdf](https://arxiv.org/pdf/2608.26951)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS
- 作者：Kangmin Seo, Jae-Pil Heo
- 出版日期：2026-08-27
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.26951

### 一句话总结
本文提出一种无需训练的过滤流程，利用前馈3D高斯泼溅中的逐视角高斯预测结构，自动剔除与多数输入视角不一致的瞬态干扰物，从而提升新视角渲染质量。

### 研究问题
在面向随意拍摄的多视角前馈3D高斯重建中，如何在不重新训练或无场景特定优化的前提下，消除仅出现在部分视角中的瞬态物体（干扰物），避免其在合成新视角时产生模糊、重复或漂浮伪影。

### 核心思路/方法
- 利用前馈3DGS的逐视角预测结构：对每个输入视角，排除其关联的高斯，并用剩余表示渲染同一相机视角，以暴露与其他输入不一致的内容。
- 通过特征相似度形成候选区域，再用渲染验证筛选候选：仅保留那些在移除后能降低其他输入视角重建误差的候选区域。
- 整个流程基于单一冻结预测，无需重训练或场景特定优化。

### 主要贡献
- 提出一种训练无关的干扰物过滤流程，直接作用于前馈3DGS的逐视角高斯预测。
- 在三个重建模型和两个干扰物基准上，验证了该方法在不同输入视角数量下均能持续改善新视角质量。
- 在干净场景下，对四个模型的评估显示原始重建结果基本得以保留，即过滤不会显著损害无干扰场景质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对前馈3DGS实际应用中常见的瞬态干扰物问题，提出了一种无需重新训练、即插即用的过滤方案，具有较高的实用价值；方法简洁且已在多个模型和基准上验证，适合关注3D重建、新视角合成及无训练后处理策略的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting reconstructs an explicit Gaussian representation from multiple input images in one network execution, making 3D reconstruction increasingly accessible for casual captures. However, such captures frequently contain transient objects that appear in only a subset of the views. Such content can be encoded into the per-view Gaussians associated with the inputs that observe it and remain in the combined representation despite being observed by no other input. As a result, it may produce blurred, duplicated, or floating artifacts in novel views. We introduce a training-free filtering procedure that exploits this per-view prediction structure. For each input, we exclude its associated Gaussians and render the same camera using the remaining representation, revealing content that is inconsistent with the other inputs. Feature similarity forms candidate regions, and rendering-based verification retains only candidates whose removal reduces reconstruction error in the other input views. The procedure operates on a single frozen prediction without retraining or scene-specific optimization. Across three reconstruction models and two distractor benchmarks, it consistently improves novel-view quality with varying numbers of input views. On clean scenes, evaluations across four models show that the original reconstructions are largely preserved.

</details>

#### 2026-08-27 - KISS-GS: 3D Gaussian Splatting Compression Kept Simple

**Authors:** Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann, Adrian Szatmari, Paul Schlack, Florian Barthel, Peter Eisert, Anna Hilsmann
**Links:** [abs](https://arxiv.org/abs/2608.26948) - [pdf](https://arxiv.org/pdf/2608.26948)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KISS-GS: 3D Gaussian Splatting Compression Kept Simple
- 作者：Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann, Adrian Szatmari, Paul Schlack, Florian Barthel, Peter Eisert, Anna Hilsmann
- 出版日期：2026-08-27T10:49:42Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.26948

### 一句话总结
KISS-GS 提出一种模块化、与训练解耦的 3D Gaussian Splatting 压缩管线，通过剪枝压缩、图像化格式编码及可选微调，实现 85x 到 319x 的场景体积缩减，并保持解码简单通用。

### 研究问题
如何设计一个模块化、透明且高效的 3DGS 压缩方法，在显著缩小场景文件大小的同时，保持各组件可独立复用、解码简单，并实现优于紧密集成方法的率失真性能。

### 核心思路/方法
- 完全解耦压缩与训练：对 vanilla 3DGS 重建的场景直接进行后处理压缩。
- 第一步：通过结合最先进的剪枝方案（compaction），实现 15.7x 的缩减。
- 第二步：将压缩后的高斯编码为基于图像的格式，便于简单、通用的解码（如 web 原生图像格式）。
- 提出 SOG-XT 格式，作为 Self-Organizing Gaussians 的扩展，包含两个主要创新：
  1. 自组织 2D 码本（Self-organizing 2D Codebooks）
  2. 并行代表分配平滑（PRAS）：利用四元数与尺度参数化的对称性，生成更利于编码的 2D 属性网格
- 可选步骤：编码感知的微调（encoding-aware fine-tuning），额外带来 2.2x 缩减。
- 整体管线模块化，各阶段可独立替换或结合未来进展。

### 主要贡献
- 提出 KISS-GS：一个原理简单、模块化的 3DGS 压缩管线，完全将压缩与训练解耦。
- 提出 SOG-XT 格式，包含自组织 2D 码本和 PRAS 两个新组件，用于生成更可编码的二维属性表示。
- 在标准 3DGS 基准上，实现 85x 至 319x 的总场景体积缩减率，超越紧密集成的方法，并在真实场景中设定新基准。
- 解码仅依赖 web 原生图像格式，保证通用性与简单性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作面向 3DGS 部署中的实际痛点（文件体积过大），提出了一套简单解耦、效果显著且可复用的压缩方案，在率失真性能上超越现有紧密集成方法，且代码公开。对于从事 3D 场景重建、压缩和实时渲染的研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Scene reconstruction with 3D Gaussian Splatting (3DGS) has become common, however deployment remains painful as the uncompressed file sizes can be massive. Current 3DGS compression systems combine multiple strategies for file size reduction, which can obscure where gains come from and limit component reuse across training pipelines. To make the gains more transparent, we propose KISS-GS, a modular compression pipeline named after the principle of keeping things simple, designed to decouple compression entirely from training. Given a 3DGS scene reconstructed with vanilla 3DGS, we are able to reduce it through compaction by 15.7x using a combination of state-of-the-art pruning schemes. Then we encode it into an image-based format designed for simple, ubiquitous decoding. With the SOG-XT format, we propose a novel extension to Self-Organizing Gaussians with two main contributions: (i) Self-organizing 2D Codebooks and (ii) Parallel Representative Assignment Smoothing (PRAS), which leverages the symmetry of quaternion and scale parameterizations to produce 2D attribute grids more amenable to encoding. This encoding reduces scene size by 6.6x. We show that optional encoding-aware fine-tuning yields a further 2.2x. Across standard 3DGS benchmarks, our simple and modular approach thus achieves a total of 85x to 319x reductions in the size of the scene over uncompressed vanilla 3DGS, setting new benchmarks for real-world scenes and surpassing tightly integrated methods in rate-distortion. Decoding relies solely on web-native image formats, and the modular design makes each stage easy to combine with future advances in reconstruction and compaction. Code and project page: https://fraunhoferhhi.github.io/KISS-GS/

</details>

#### 2026-08-27 - CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes

**Authors:** Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang
**Links:** [abs](https://arxiv.org/abs/2608.26656) - [pdf](https://arxiv.org/pdf/2608.26656)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** monocular depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes
- 作者：Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang
- 出版日期：2026-08-27
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.26656

### 一句话总结
CoGeo-GS提出一种概念驱动且几何感知的3D场景多物体移除框架，通过语义标签与几何补全管线，在单次优化中实现高质量多物体去除。

### 研究问题
如何在3D场景中高效且稳定地移除多个目标物体，同时保持几何与多视角一致性，避免现有3DGS方法在多物体场景下因遮挡、语义纠缠导致的重复优化和几何不稳定问题。

### 核心思路/方法
- 概念驱动的语义标签分配：为高斯点赋予概念感知的语义标签，支持灵活的目标物体选择，并减少前景物体与背景结构间的干扰，可在单次优化阶段完成多物体移除。
- 几何感知补全管线：融合单目深度先验、扩散模型细化以及边界对齐混合，恢复被移除区域的合理几何结构。
- 几何正则化细化策略：进一步稳定重建过程并保持多视角一致性。

### 主要贡献
- 提出CoGeo-GS，一个面向3D场景可控制多物体移除的概念驱动框架。
- 设计语义标签机制，实现在单一优化阶段内灵活选择多个目标并降低语义纠缠。
- 引入几何感知补全管线与几何正则化策略，提升移除区域的重建质量与多视角一致性。
- 实验表明CoGeo-GS在视觉质量与重建保真度上优于现有方法。

### 局限性
摘要未提供足够信息，无法得知该方法在极端遮挡、物体尺度差异、语义标签边界模糊、计算成本或实时性方面的具体局限。

### 阅读优先级
**高**
理由：该工作针对3DGS多物体场景编辑的痛点提出系统解决方案，结合语义标签与几何补全，属于神经场景表示与渲染方向的热点研究问题，且实验结果显示优于现有方法，对相关领域的研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Multi-object removal in 3D scenes is challenging due to severe occlusions, semantic entanglement, and the difficulty of maintaining geometric and multi-view consistency. Existing 3D Gaussian Splatting (3DGS) methods perform well for single-object editing but scale poorly to multi-object scenarios, often requiring repetitive optimization and yielding unstable geometry in removed regions. We propose CoGeo-GS, a concept-driven framework for controllable multi-object removal in 3D scenes. CoGeo-GS assigns concept-aware semantic tags to Gaussians, enabling flexible object selection and reducing interference between foreground objects and background structures within a single optimization stage. To recover plausible geometry, we introduce a geometry-aware completion pipeline that combines monocular depth priors with diffusion-based refinement and boundary-aligned blending. A geometry-regularized refinement strategy further stabilizes reconstruction and preserves multi-view consistency. Experiments demonstrate that CoGeo-GS outperforms existing methods in visual quality and reconstruction fidelity.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-01 - One Print, Many Moves: Monolithic Origami-inspired Folding Actuator for Composable Soft Multi-DoF Systems

**Authors:** Jaehyung Jang, Zhenish Zhakypov, Jasmin Elena Palmer, Melissa Klein, Jee-Hwan Ryu, Allison Mariko Okamura
**Links:** [abs](https://arxiv.org/abs/2609.00751) - [pdf](https://arxiv.org/pdf/2609.00751)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, VR, virtual reality

<details>
<summary>Abstract</summary>

Conventional soft robot actuators excel in compliance, but their uncontrolled deformations compromise accuracy and hinder scaling to multi-degree-of-freedom (DoF) systems. We introduce a MONOlithic ORIGAMI-inspired soft folding actuator design (MONORIGAMI) that establishes a design strategy based on spatially programmed stiffness anisotropy to preserve material compliance along desired folding directions while selectively restricting deformation in unwanted directions. The actuator leverages stiffness tiers based on material thickness, patterned in an origami-inspired geometry with facets and creases, converting unconstrained soft deformation into accurate, repeatable, and composable folding motions without additional reinforcements. The design is fully 3D-printable through a single-material, single-print process that requires no assembly. Each actuator serves as a scalable motion primitive, and linking and orienting multiple actuators mechanically programs multi-DoF trajectories. Using the same fundamental module, we demonstrate three 3D-printed soft multi-DoF robotic systems spanning distinct application domains: (1) a compact 4-DoF wearable haptic device for high-fidelity cutaneous feedback in virtual reality (VR), (2) a 3-DoF joystick for kinesthetic feedback in teleoperation, and (3) a modular robotic gripper capable of underwater operation with geometry-encoded grasp trajectories. These systems demonstrate the module's capabilities for compact multi-axis integration, controlled physical interaction, and geometry-programmed operation across different environments. Together, these results show that MONORIGAMI provides a general, composable, accessible, reliable, and scalable platform for high-precision soft multi-DoF robotics, addressing long-standing limitations in both soft actuator design and fabrication.

</details>

### 2026-08

#### 2026-08-31 - IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training

**Authors:** Rongze Tang, Jianjie Fang, Zhaolu Wang, Ziyou Wang, Xvyuan Liu, Haisheng Su, Xin Zhang, Wei Wu, Chen Gao, Yong Li, Zhibo Chen
**Links:** [abs](https://arxiv.org/abs/2609.00161) - [pdf](https://arxiv.org/pdf/2609.00161)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>Abstract</summary>

World models have made remarkable progress in action-conditioned future prediction for embodied agents, yet still struggle to model physically plausible interactions. Existing approaches address this limitation by constraining the generation process with external representations encoding motion, geometry, or semantics. Obtaining these spatiotemporally dense representations typically requires auxiliary estimators or manual annotations, limiting training scalability. We instead revisit the training objective and identify a supervision-allocation mismatch under the globally averaged mean squared error (MSE) denoising objective: prevalent static content dominates the optimization signal, leaving sparse dynamic-object regions critical to interaction generation disproportionately under-supervised. Motivated by this observation, we introduce IMPACT, a scalable Interaction-aware Model training framework with Prior-guided Attention Calibration and Targeting. IMPACT uses cross-attention associated with manipulated-object tokens as an internal spatiotemporal prior for action-conditioned changes. It samples candidate regions from this prior, calibrates them with detached local prediction errors to construct an interaction map, and uses the map to reweight denoising supervision, requiring neither external representations nor inference-time modifications. Extensive experiments on robot-arm and human-hand manipulation, spanning diverse control modalities and DiT backbones, show that IMPACT consistently outperforms the corresponding MSE-trained baselines, improving interaction fidelity, physical plausibility, and visual quality.

</details>

#### 2026-08-31 - APT: Anchor-aligned Perturbations for Tamper Localization in Fully Regenerated Images

**Authors:** Suhyeon Ha, Woo Jae Kim, Joonsung Jeon, Sooel Son, Sung-eui Yoon
**Links:** [abs](https://arxiv.org/abs/2608.30656) - [pdf](https://arxiv.org/pdf/2608.30656)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：APT: Anchor-aligned Perturbations for Tamper Localization in Fully Regenerated Images
- 作者：Suhyeon Ha, Woo Jae Kim, Joonsung Jeon, Sooel Son, Sung-eui Yoon
- 出版日期：2026-08-31
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.30656

### 一句话总结
本文提出APT（锚点对齐扰动）方法，通过在潜在空间嵌入密集向量定位信号，实现对扩散模型完全重建图像中篡改区域的像素级定位，在COCO数据集上达到0.92的FR IoU，显著优于现有基线。

### 研究问题
现有主动篡改定位方法基于拼接（SP）设定，即合成区域叠加在原始背景之上，嵌入信号得以保留。然而真实场景中基于扩散模型的修复（inpainting）属于完全重建（FR）设定——整张图像都经过去噪过程，背景信号被破坏，导致现有框架失效。因此需要针对FR设定设计新的篡改定位方案。

### 核心思路/方法
APT采用半脆弱的潜在空间扰动，在图像分发前嵌入密集的向量级定位信号。具体做法：
- 将每个空间特征向量对齐到固定的锚点方向；
- 修复（inpainting）后，通过合成前景与锚点对齐背景特征之间的对齐差异来定位篡改区域；
- 引入难负样本挖掘（hard negative mining）损失和噪声扰动分支，进一步增强对齐的均匀性。

### 主要贡献
1. 提出APT框架，首次针对扩散模型完全重建（FR）设定下的篡改定位问题；
2. 实现FR IoU 0.92，超过最强基线WAM（0.84），而现有方法在该设定下性能接近随机（AUC 0.5）；
3. 框架可泛化到测试时未知的篡改类型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作切入了一个实际但被忽视的场景（扩散模型完全重建下的篡改检测），给出了明确的量化优势（FR IoU 0.92 vs 0.84），且指出现有方法在该设定下完全失效（AUC 0.5），具有清晰的实践意义和对比价值。

</details>

<details>
<summary>Abstract</summary>

Proactive tamper localization embeds an imperceptible signal into an image prior to distribution, enabling pixel-level manipulation detection. Existing methods assume a spliced (SP) setting, where synthesized regions are composited onto the original background, leaving embedded signals intact. However, real-world diffusion-based inpainting operates in a fully regenerated (FR) setting, where the entire image undergoes denoising, disrupting background signals and rendering existing frameworks ineffective. We propose APT, a semi-fragile latent-space perturbation that embeds a dense, vector-wise localization signal. By aligning each spatial feature vector toward a fixed anchor direction, APT localizes tampering via the alignment disparity between synthesized foreground and anchor-aligned background features after inpainting. The proposed hard negative mining loss and noisy perturbation branch further enforce uniform alignment. Experiments on COCO demonstrate that APT achieves an FR IoU of 0.92, outperforming the strongest baseline (WAM, 0.84), while existing methods collapse to near-random performance (AUC 0.5), establishing APT as a practical forensic framework generalizable across tampering types unknown at test time.

</details>

#### 2026-08-31 - Real-Time Scene-Adaptive Tone Mapping for High-Dynamic Range Object Detection

**Authors:** Gongzhe Li, Linwei Qiu, Peibei Cao, Fengying Xie, Xiangyang Ji, Qilin Sun
**Links:** [abs](https://arxiv.org/abs/2608.30400) - [pdf](https://arxiv.org/pdf/2608.30400)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-Time Scene-Adaptive Tone Mapping for High-Dynamic Range Object Detection
- 作者：Gongzhe Li, Linwei Qiu, Peibei Cao, Fengying Xie, Xiangyang Ji, Qilin Sun
- 出版日期：2026-08-31T07:52:53Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.30400

### 一句话总结
本文提出一种面向高动态范围（HDR）图像目标检测的场景自适应实时色调映射方法，通过端到端优化弥合HDR RAW输入与检测网络所需的LDR sRGB输入之间的差距。

### 研究问题
HDR图像包含丰富的色调与细节信息，对自动驾驶等计算机视觉系统具有潜力，但多数嵌入式神经网络基于低动态范围（LDR）输入训练，在处理高比特深度HDR图像时会因极端动态范围而出现显著性能下降。本文旨在解决该差距问题。

### 核心思路/方法
- 提出一种新颖的色调映射方法，将HDR RAW输入与检测网络所需的LDR sRGB要求相连接，并与下游任务实现端到端联合优化。
- 不依赖传统图像信号处理（ISP）流程，引入神经光度校准（neural photometric calibration）对动态范围进行正则化，并使用缩放不变局部色调映射模型（scaling-invariant local tone mapping model）保留图像细节。
- 架构支持性能迁移微调（performance transfer finetuning），能以最小成本从LDR sRGB图像高效适配至HDR RAW图像。

### 主要贡献
- 提出一种端到端可优化的色调映射方法，兼顾HDR输入与LDR检测网络需求。
- 引入神经光度校准与缩放不变局部色调映射模型，替代传统ISP流程。
- 支持性能迁移微调，降低从LDR到HDR输入的适配成本。
- 在挑战性汽车HDR场景中优于传统色调映射算法及先进AI-ISP方法。
- 在NVIDIA Jetson平台上实现对4K高比特深度HDR输入的实时处理。

### 局限性
摘要未提供足够信息（如对极端动态范围的具体量化表现、模型规模、训练数据细节、在非汽车场景下的泛化能力、微调所需的具体数据量等均未提及）。

### 阅读优先级
**高**

理由：该工作针对自动驾驶等实际应用中HDR图像与现有LDR检测网络不匹配的关键问题，提出端到端可优化的实时色调映射方案，并展示在嵌入式平台（NVIDIA Jetson）上的实时处理能力，兼具算法创新与实际部署价值，对相关领域研究者具有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

High-dynamic-range (HDR) images, with their rich tone and detail reproduction, hold significant potential to enhance computer vision systems, particularly in autonomous driving. However, most neural networks for embedded systems are trained on low-dynamic-range (LDR) inputs and suffer substantial performance degradation when handling high-bit-depth HDR images due to the challenges posed by extreme dynamic ranges. In this paper, we propose a novel tone mapping method that not only bridges the gap between HDR RAW inputs and the LDR sRGB requirements of detection networks but also achieves end-to-end optimization with downstream tasks. Instead of relying on the traditional image signal processing (ISP) pipeline, we introduce neural photometric calibration to regularize dynamic ranges and a scaling-invariant local tone mapping model to preserve image details. In addition, our architecture also supports performance transfer finetuning, enabling efficient adaptation from the LDR sRGB images to the HDR RAW images with minimal cost. The proposed method outperforms traditional tone mapping algorithms and advanced AI-ISP methods in challenging automotive HDR scenes. Moreover, our pipeline achieves real-time processing of 4K high-bit-depth HDR inputs on NVIDIA Jetson platforms.

</details>

#### 2026-08-29 - Toward Trustworthy Robot-Assisted Sliding Palpation for Shallow Vessel Localisation with a Calibrated Digital Twin

**Authors:** Piotr Blaszyk, Wen Fan, Kaizhong Deng, Daniel Elson, Dandan Zhang
**Links:** [abs](https://arxiv.org/abs/2608.29396) - [pdf](https://arxiv.org/pdf/2608.29396)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Toward Trustworthy Robot-Assisted Sliding Palpation for Shallow Vessel Localisation with a Calibrated Digital Twin
- 作者：Piotr Blaszyk, Wen Fan, Kaizhong Deng, Daniel Elson, Dandan Zhang
- 出版日期：2026-08-29
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.29396

### 一句话总结
本文提出一种基于校准数字孪生的机器人辅助滑动触诊框架，通过仿真生成标记触觉序列，训练时空图神经网络实现浅表血管定位，并给出了跨域评估结果。

### 研究问题
如何在不依赖大量真实触觉数据的前提下，可靠定位浅表皮下血管，以实现安全的机器人辅助静脉穿刺和血管感知操作？核心挑战在于真实触觉数据采集成本高、耗时且可能损坏基于视觉的软触觉传感器。

### 核心思路/方法
- 构建一个校准的数字孪生，用于生成带标签的触觉序列，减少对真实数据的依赖。
- 数字孪生建模传感器-血管接触，并通过基于贝叶斯优化的域自适应对真实滑动轨迹进行校准。
- 在滑动方向和接触条件上进行随机化，增强仿真多样性。
- 使用时空图神经网络对仿真生成的标记轨迹进行逐节点血管分类，并通过2D-3D-2D几何投影生成人类可验证的俯视定位图。
- 在四个数据集（Sim、Silicone、Meat）上进行四种训练-测试配置（Sim→Sim、Sim→Silicone、Sim→Meat、Meat→Silicone）的跨域评估。

### 主要贡献
- 提出一种结合校准数字孪生的机器人滑动触诊框架，降低对真实数据的依赖。
- 引入贝叶斯优化域自适应，使数字孪生与真实滑动轨迹对齐，实现模拟到真实的标记对齐（最深接触处平均绝对误差0.50 mm）。
- 实现基于图神经网络的血管分类和可解释的俯视定位图生成。
- 提供跨域评估结果：除Sim→Meat外，预测血管像素距真实血管像素平均距离为1.05–1.31 mm；所有模型平均为1.05–5.49 mm。
- 公开代码、模型权重和数据（GitHub和Zenodo）。

### 局限性
摘要未提供足够信息。摘要仅提及Sim→Meat配置误差较大，归因于更大的域偏移和当前仿真迁移的局限，但未提供其他具体局限性，如模型在更深血管、更复杂组织上的表现、计算成本、实时性等。

### 阅读优先级
**高**。理由：该工作针对机器人辅助医疗操作中的关键问题（血管定位），提出结合数字孪生、域自适应和图神经网络的完整方案，跨域评估设计清晰，数值结果具体，且开放代码与数据，对仿真到真实迁移和触觉感知方向的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Reliable localisation of shallow subsurface vessels is important for safe robot-assisted venous access and vessel-aware manipulation, but collecting diverse tactile data on physical hardware is costly, time-consuming, and can degrade soft vision-based tactile sensors. We present a robot-assisted sliding-palpation framework in which a calibrated digital twin generates labelled tactile sequences, reducing reliance on real-world data. The twin models sensor-vessel contact, is calibrated against real palpation trajectories using Bayesian-optimisation-based domain adaptation, and is randomised over sliding direction and contact conditions. A spatio-temporal graph neural network trained on simulated marker trajectories performs per-node vessel classification and produces a human-verifiable top-view localisation map through 2D-to-3D-to-2D geometric projection. We evaluate three datasets: Sim, Silicone, and Meat, the latter a raw-meat phantom with vessel models at nominal depths of 0 to 30 mm, using four train-to-test configurations: Sim to Sim, Sim to Silicone, Sim to Meat, and Meat to Silicone. The calibrated twin achieves a simulated-to-real marker-alignment mean absolute error of 0.50 mm at deepest contact across four canonical interactions. After reprojection onto a 1 mm top-view grid, predicted vessel pixels lie on average 1.05 to 5.49 mm from the nearest true vessel pixel across the four models, with 1.05 to 1.31 mm for all except Sim to Meat. The larger error for Sim to Meat reflects the greater domain shift and current limit of simulation transfer. These results demonstrate progress toward trustworthy tactile palpation through calibrated simulation, interpretable localisation, and transparent cross-domain evaluation. Code, model weights, and data are publicly available on GitHub and Zenodo.

</details>

#### 2026-08-27 - Reconstructing Humans and Objects in Interaction using Large Reconstruction Models

**Authors:** Agniv Chatterjee, Georgios Pavlakos
**Links:** [abs](https://arxiv.org/abs/2608.27407) - [pdf](https://arxiv.org/pdf/2608.27407)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reconstructing Humans and Objects in Interaction using Large Reconstruction Models
- 作者：Agniv Chatterjee, Georgios Pavlakos
- 出版日期：2026-08-27
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.27407

### 一句话总结
本文提出 MILO 框架，利用大规模重建模型（LRMs）从单张图像中恢复详细的 3D 人-物交互，将重建问题转化为对 LRM 生成网格的分割与拟合。

### 研究问题
如何从单张 RGB 图像中准确重建 3D 人-物交互（3D HOI），克服深度模糊、遮挡和物体形状多样性的挑战。

### 核心思路/方法
- 关键观察：LRMs 能提供保留人-物相对空间排列和邻近线索的强几何骨架。
- 将 3D HOI 重建重新定义为“解释 LRM 网格”的过程，具体步骤为：
  1. 将 LRM 生成的网格分割为人体部分和物体部分；
  2. 对人体部分拟合参数化人体模型；
  3. （可选）若存在物体模板，则将其与物体部分对齐。

### 主要贡献
- 提出 MILO，一种利用 LRM 视觉能力进行单图 3D 人-物交互重建的新框架。
- 将传统基于重投影和接触约束的拟合方式，转变为基于 LRM 几何骨架的解释方式，简化了重建流程。
- 在多个基准和交互场景上取得了优于现有基线方法的重建精度。

### 局限性
摘要未提供足够信息。摘要中未讨论方法在遮挡极端严重、无物体模板可用、运行效率或泛化到未见物体类别时的具体局限。

### 阅读优先级
**中**  
理由：该工作为 3D 人-物交互重建提供了新的思路（借助 LRM），方法有一定创新性，且声称在多个基准上超越基线。但摘要未提供定量实验细节和深入对比，且属于特定应用方向（人-物交互），对于非该领域读者吸引力有限。若你从事 3D 重建或具身智能方向研究，可进一步关注；否则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Estimation of Human-Object Interactions in 3D (3D HOI) is a fundamental problem in 3D computer vision with applications in AR/VR, robotics, and embodied AI. However, reconstructing these interactions in 3D remains challenging due to depth ambiguities, occlusions, and object shape variability. Existing approaches are primarily concerned with reprojection and contact constraints, fitting parametric human models and object templates to 2D images. In this paper, we explore a different avenue. We present MILO, a framework that leverages the visual capabilities of Large Reconstruction Models (LRMs) to recover detailed 3D human-object interactions from a single image. Our key observation is that LRMs provide a powerful geometric scaffold that preserves relative human-object arrangement and proximity cues. This significantly simplifies the reconstruction procedure, reframing the problem as interpreting the LRM mesh: we segment it into human and object components, fit a parametric body model to the human part, and optionally align an object template to the object part (if such a template is available). MILO achieves strong reconstruction accuracy and outperforms existing baselines across multiple benchmarks and interaction scenarios. Our code is available at https://ac5113.github.io/MILO.

</details>

#### 2026-08-27 - SpatialCrafter: Single Image World Modeling with Generative 3D Proxies

**Authors:** Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan
**Links:** [abs](https://arxiv.org/abs/2608.27073) - [pdf](https://arxiv.org/pdf/2608.27073)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, virtual reality, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialCrafter: Single Image World Modeling with Generative 3D Proxies
- 作者：Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan
- 出版日期：2026-08-27T12:58:37Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.27073

### 一句话总结
SpatialCrafter 提出一种两阶段图像到三维场景生成框架，通过引入全局三维代理（3D Proxy）结合视频扩散模型，实现高保真、几何一致且抗长时间漂移的可探索场景生成。

### 研究问题
如何基于单张图像生成可自由探索的 3D 场景，同时克服现有视频扩散模型在稀疏点云或 2D 全景条件下产生的随机幻觉、长时间漂移和三维一致性不足的问题。

### 核心思路/方法
- 将生成过程分解为全局代理生成（Global Proxy Generation）与外观细化（Appearance Refinement）两个阶段。
- 提出 Point-anchored Sparse Structure (PaSS) Flow 模块，用于预测空间对齐且几何一致的 3D 代理。
- 将视频扩散模型重新定位为 Generative Deferred Refiner，在代理定义的场景几何上合成高频逼真细节。
- 引入 Parallel Geometry Injection 和 Proxy-Aware Corruption 训练策略，提升对代理瑕疵的鲁棒性，同时不干扰预训练生成流形。
- 新建了一个包含 115K 场景的大规模混合数据集，用于图像到场景生成任务训练。

### 主要贡献
- 提出两阶段图像到场景生成框架，引入全局 3D 代理以改善一致性和漂移问题。
- 设计 PaSS Flow 模块，用于生成几何一致的 3D 代理。
- 提出两种训练策略（Parallel Geometry Injection 与 Proxy-Aware Corruption），有效集成代理与预训练 VDM。
- 构建并公开首个用于图像到场景生成的混合数据集（115K 场景）。
- 在合成与真实数据集上，SpatialCrafter 在快速相机运动和极端视角变化下优于现有方法，且保持鲁棒性和一致性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该研究针对图像到 3D 场景生成中的关键难题（3D 一致性、长时间漂移）提出了系统性两阶段解决方案，并配套公开新数据集，对机器人、VR/AR 和游戏等领域有潜在应用价值；实验覆盖合成及真实场景，评估维度较全面，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Explorable image-to-scene generation is essential for applications in gaming, robotics, and virtual reality. Existing methods based on video diffusion model (VDM) commonly rely on incomplete conditioning signals such as sparse point clouds or 2D panoramas, leading to stochastic hallucinations, long-term drifts and suboptimal 3D consistency. We present SpatialCrafter, a novel two-stage framework that addresses these issues by introducing a global 3D proxy for high-fidelity image-to-scene generation. Specifically, we decompose the generation process into global proxy generation and appearance refinement. For proxy generation, we propose a Point-anchored Sparse Structure~(PaSS) Flow module that predicts a spatially aligned and geometrically consistent 3D proxy. For appearance refinement, we re-frame the VDM as a Generative Deferred Refiner which synthesizes high-frequency photorealistic details upon proxy-defined scene geometry. To better integrate the proxy with the pre-trained VDM, we introduce Parallel Geometry Injection and Proxy-Aware Corruption training strategies, which improve robustness to proxy artifacts without disrupting the pretrained generative manifold. Furthermore, as no suitable dataset exists for this explorable scene generation task, we construct a new large-scale dataset of 115K scenes. To the best of our knowledge, it is the first hybrid dataset for image-to-scene generation. Extensive experiments on both synthetic and real-world datasets show that SpatialCrafter outperforms state-of-the-art methods, mitigates long-term drift, and remains robust and consistent under rapid camera motion and extreme viewpoint changes. Code, models, and the newly constructed dataset will be publicly released. See more at https://fangchuan.github.io/SpatialCrafter/.

</details>

#### 2026-08-27 - Contact-Aided Factor-Graph Localization for Underwater Sampling

**Authors:** Michele Grimaldi, Yosaku Maeda, Hitoshi Kakami, Ignacio Carlucho, Yvan R. Petillot, Tomoya Inoue
**Links:** [abs](https://arxiv.org/abs/2608.26932) - [pdf](https://arxiv.org/pdf/2608.26932)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Contact-Aided Factor-Graph Localization for Underwater Sampling
- 作者：Michele Grimaldi、Yosaku Maeda、Hitoshi Kakami、Ignacio Carlucho、Yvan R. Petillot、Tomoya Inoue
- 出版日期：2026-08-27
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26932

### 一句话总结
本文提出一种在退化水下环境中利用机械臂接触事件作为几何约束的因子图定位框架，以降低水下采样任务的轨迹漂移并提升重访精度。

### 研究问题
自主水下机器人在近距离海底采样时，由于低空下视相机面对平坦无纹理海底而产生尺度模糊和横向退化，传统惯性-DVL融合缺乏结构漂移校正机制，如何实现鲁棒的状态估计是一个关键挑战。

### 核心思路/方法
- 将基于吸盘的机械臂接触事件建模为高置信度因子，融入平滑式因子图定位框架，形成隐式回环闭合，无需依赖外观场景识别。
- 紧密融合自适应视觉里程计、学习式目标检测和机载传感器。
- 视觉里程计相对位姿因子与地标方位-距离因子根据内点统计进行不确定性缩放，避免弱视觉帧破坏估计稳定性。
- 系统可在运动过程中完全在线初始化。

### 主要贡献
- 提出接触辅助的因子图定位框架，将物理交互作为信息性几何约束引入定位。
- 通过接触事件实现无需外观识别的隐式回环闭合。
- 设计了基于内点统计的不确定性缩放机制，增强视觉退化条件下的鲁棒性。
- 实验验证在罐体、港口及仿真环境中，接触约束显著降低轨迹漂移并提升目标重访精度，优于滤波式导航和无接触图优化方案。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作针对水下退化环境的定位问题提出新颖的接触辅助因子图方法，robotics定位方向研究者有一定参考价值；但实验为摘要级概述，缺少定量细节，且领域相对专门化，综合优先级定为中。

</details>

<details>
<summary>Abstract</summary>

Accurate state estimation for autonomous underwater vehicles performing close-range seafloor sampling remains challenging. In low-altitude operation, down-looking cameras over featureless planar seabeds produce scale ambiguity, lateral degeneracy, and inconsistent feature tracking. Meanwhile, inertial-Doppler Velocity Log (DVL) fusion alone provides no mechanism for structural drift correction. We propose a Contact-Aided Factor-Graph Localization framework that treats physical interaction as an informative geometric constraint within a smoothing-based localization formulation. The method tightly fuses suction-based manipulator contact events with adaptive visual odometry, learned object detections, and on-board sensors. Visual odometry relative-pose factors and landmark bearing-range factors are uncertainty-scaled according to inlier statistics to prevent visually weak frames from destabilizing the estimator, while contact events are modeled as high-confidence factors that induce implicit loop closures without appearance-based place recognition. Furthermore, the system can fully initialize online during motion. Experimental evaluation in tanks, harbor, and simulation environments demonstrates that contact-induced constraints significantly reduce trajectory drift and improve object revisit accuracy compared to filtering-based navigation and contact-free graph formulations. These results highlight the role of embodied physical interaction as a localization primitive in perception-degraded underwater environments

</details>

#### 2026-08-27 - Decoupling Planning and Control for Instructable Agents

**Authors:** Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr
**Links:** [abs](https://arxiv.org/abs/2608.26788) - [pdf](https://arxiv.org/pdf/2608.26788)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Decoupling Planning and Control for Instructable Agents
- 作者：Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr
- 出版日期：2026-08-27T08:17:58Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26788

### 一句话总结
本文提出Instruct-to-Act系统，将VLM的高层规划能力与世界模型控制器的快速低层控制能力解耦结合，使控制器能根据语言指令在陌生环境中高频自主行动。

### 研究问题
如何将预训练视觉语言模型（VLM）的高层规划能力与世界模型控制器的快速控制能力结合，以解决VLM难以生成可靠低延迟动作序列、而世界模型控制器缺乏开放任务引导的问题。

### 核心思路/方法
- 系统架构：Instruct-to-Act，VLM规划器生成稀疏、高延迟的高层文本指令，训练好的世界模型控制器以高频方式根据这些指令自主行动。
- 控制器训练：将控制器策略回放片段用合成指令重新标注，并在现有奖励最大化与世界建模目标之外，联合优化行为克隆目标，使控制器具备语言可引导性。
- 评估设计：在七个具身环境（含三个多智能体环境）中进行测试，VLM规划器通过语言协调，训练后的控制器作为执行器。

### 主要贡献
1. 提出解耦规划与控制的Instruct-to-Act框架，兼顾VLM的开放任务理解与控制器的高速执行。
2. 通过合成指令重标注+联合行为克隆训练，使现有世界模型控制器具备语言引导能力。
3. 在匹配观测与动作空间条件下，解耦方法一致优于仅控制器和直接VLM生成动作的变体。
4. 支持直接替换不同预训练VLM规划器而无需微调，且在七个任务中六个任务上保持与强基线（视觉-语言-动作模型、多智能体RL）竞争力。

### 局限性
摘要未提供足够信息，未提及计算资源需求、部署延迟具体数值、失败案例分析、对不同环境泛化能力差异的深入讨论，以及与其他方法在剩余一个任务上对比结果不佳的具体原因。

### 阅读优先级
**高**。理由：该工作提出了一种新颖且通用的架构解耦思路（VLM规划+世界模型控制），在多个环境包括多智能体场景中验证有效，且具有即插即用VLM规划器的实际价值；研究问题切中当前VLM具身应用的核心瓶颈（规划与控制冲突），对相关领域研究者有较强参考意义。

</details>

<details>
<summary>Abstract</summary>

Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model controller to act autonomously at high frequency when conditioned on sparse, higher-latency, and high-level text instructions generated by a VLM planner. To train controllers to be language-instructable, we relabel segments of controller policy rollouts with synthetic instructions and jointly optimize a behavior-cloning objective along with existing reward-maximizing and world-modeling objectives. We evaluate our proposed approach across seven embodied environments, including three multi-agent environments where VLM planners coordinate through language while trained controllers serve as their actuators. Under matched observation and action spaces, our decoupled approach consistently outperforms controller-only and direct VLM action-generation variants, preserves fast control, and lets us swap in different pretrained VLM planners without fine-tuning, while remaining competitive with strong vision-language-action and multi-agent RL baselines on six of seven tasks.

</details>

#### 2026-08-26 - Gating Before Commitment: Anticipating Intent Divergence to Prevent Post-Interaction Decision Failures in Autonomous Driving

**Authors:** Cong Xu, Ravi Sankar
**Links:** [abs](https://arxiv.org/abs/2608.26074) - [pdf](https://arxiv.org/pdf/2608.26074)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gating Before Commitment: Anticipating Intent Divergence to Prevent Post-Interaction Decision Failures in Autonomous Driving
- 作者：Cong Xu, Ravi Sankar
- 出版日期：2026-08-26
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26074

### 一句话总结
本文提出一种在自动驾驶规划提交前进行“意图分歧门控”的决策层，通过在结构化描述符上计算平滑的意图-几何分歧分数，对计划进行提前拦截，从而防止交互后决策失败。

### 研究问题
自动驾驶中车辆交互时的意图误读会导致反复出现的规划失败，本文研究如何在计划承诺之前预判意图分歧并采取门控干预，以避免事后决策失效。

### 核心思路/方法
- 设计一个决策层，包含语言引导的意图模块，读取结构化描述符并计算平滑的意图-几何分歧得分。
- 在规划走廊包络（corridor envelope）之前设置门控机制，在计划提交前拦截有问题的规划动作。
- 在冻结、公开的实现下，对重放的越野偏离和四个碰撞片段进行测试。
- 通过初步校准和预注册重设计（将不确定性视为弃权）来减少误触发。
- 通过两个消融实验评估模型贡献：对比完整得分与其他规则（如未否决规则和几何规则）的检测性能。

### 主要贡献
- 提出并验证了“门控在承诺之前”的决策机制，是所测试中唯一能修复计划的层。
- 主案例中，门控在漂移开始后72 ms触发，但在走廊出口前161 ms触发，并在全部十次重放中保持轨迹在走廊内。
- 预注册重设计将首次校准中每5.9分钟出现9次误触发的情况降至每分钟0.341次。
- 消融实验表明：完整得分在四个（部署资格条件）或三个（未否决规则）失败案例中检测最快；几何规则在域内轨道上同等误报率下检测数量增加三倍以上。
- 证据支持门控机制本身有效，模型的具体作用既包括在失败案例上最快检测，也包括对几何规则提供不确定性否决。

### 局限性
- 摘要未明确列出实验环境的具体规模、真实路测条件或泛化性评估，因此缺乏对更广泛驾驶场景的验证信息。
- 摘要未提供关于计算开销、实时性要求或集成到完整自动驾驶系统的具体细节。
- 摘要未描述误触发减少的具体机制参数（除了“不确定性作为弃权”）及其在更复杂交互中的适用性，摘要未提供足够信息。
- 未披露数据集的规模和多样性、基线方法对比的完整范围等信息，摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该文聚焦于自动驾驶交互决策中的意图分歧检测与门控机制，问题具体且方法有一定创新性，但摘要中实验规模、对比基线和泛化细节有限，对非专门从事自动驾驶决策层的研究者参考价值相对有限。对于从事机器人规划、人机交互和可解释决策系统的读者而言，其门控思路与不确定性处理方式具有参考意义。

</details>

<details>
<summary>Abstract</summary>

Intent misinterpretation during vehicle interactions causes recurring planning failures. We study a decision layer in which a language-guided intent module reads structured descriptors, computes a smoothed intent-geometry divergence score, and gates the planned maneuver before commitment, upstream of a corridor envelope. On a replayed off-road departure and four crash clips under a frozen, disclosed implementation, gating is the only layer that repairs the plan: on the main case it fires 72 ms after the drift onset but 161 ms before the corridor exit, keeping the trajectory in the corridor in all ten replays. The first calibration draws nine false triggers in 5.9 minutes, each from scoring uncertainty as half a conflict; a preregistered redesign treating uncertainty as abstention cuts this to 0.341 per minute. Two ablations bound the model's contribution: the full score detects fastest on four of five failures under the deployed eligibility, three of five against the unvetoed rule (000871 by one cycle; 000228 by a pre-onset fire on an uncertain stretch that five clips cannot classify as signal or coincidence; dropping the confidence term costs two detections), while on in-domain tracks at equal false positives the geometric rule more than triples its detection. The evidence supports the gating mechanism; the model's demonstrated roles are the fastest detection on these failures and an uncertainty veto on the geometric rule.

</details>

#### 2026-08-26 - One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation

**Authors:** Xiaomi Embodied Intelligence Team, University of Macau, :, Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang
**Links:** [abs](https://arxiv.org/abs/2608.26058) - [pdf](https://arxiv.org/pdf/2608.26058)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation
- 作者：小米具身智能团队，澳门大学，Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang
- 出版日期：2026-08-26
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26058

### 一句话总结
UCAG-P提出了一种以相机为中心的几何统一动作表示方法，将异构具身操作数据对齐到共享几何空间，使单个视觉-语言-动作（VLA）策略能在多种机器人形态上训练并实现跨形态泛化。

### 研究问题
异构具身数据的固有差异（不同的机器人形态、相机配置和底层动作空间）严重限制了通用VLA策略的规模化训练，现有方法通常依赖显式动作重定向、人-机器人视频合成或数据集专属适配分支，难以实现统一策略的联合学习。

### 核心思路/方法
- 提出**相机中心统一动作公式（UCAG-P）**，将异构具身数据集在结构上对齐到一个共享的几何动作空间。
- 不再将机器人专属指令作为共享策略目标，而是通过**图像坐标和相机坐标系中的可观测锚点运动**来表示操作，将机械臂、人形机器人和人手视为统一动作模式的不同具体形态。
- 设计**几何条件动作翻译器（geometry-conditioned action translator）**，将预测的运动与目标形态的运动学结合，生成可执行控制指令。
- 采用**解耦架构**，使共享VLA策略学习可迁移的操作几何，同时保留形态专属的可控性。

### 主要贡献
- 提出一种新的相机中心统一动作公式，从结构上解决异构具身数据的对齐问题，无需显式动作重定向或数据集专属分支。
- 构建解耦的预训练架构，在共享策略学习与形态专属控制之间取得平衡。
- 在**4.03K小时机器人/仿真数据与2.34K小时人类演示数据**上进行训练。
- 单一检查点无需基准专属微调即达到：LIBERO 98.3%、RoboTwin Easy/Hard 88.7%/89.2%、LIBERO-Plus零样本 82.0%、RoboCasa GR-1 62.0%。

### 局限性
摘要未提供足够信息，例如方法在未见过的极端形态或复杂动态场景下的表现、几何翻译器的计算开销、以及不同相机配置下的鲁棒性等均未提及。

### 阅读优先级
**高**。理由是：该工作针对VLA策略规模化训练中的核心瓶颈（异构数据对齐）提出了新颖的统一动作几何公式，训练数据规模大（累计超过6K小时），并在多个基准上取得了无需微调的高性能，同时包含零样本泛化评测，对具身智能和机器人操作领域具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Scaling generalist vision-language-action (VLA) policies is severely bottlenecked by the inherent heterogeneity of embodied data, which spans diverse robot morphologies, camera configurations, and low-level action spaces. Existing paradigms typically address this mismatch through explicit action retargeting, human-to-robot video synthesis, or dataset-specific adaptation branches, fundamentally hindering the joint learning of a unified policy. We introduce UCAG-P, a camera-centric unified action formulation that structurally aligns heterogeneous embodied datasets into a shared geometric action space. Rather than treating robot-specific commands as the shared policy target, UCAG-P represents manipulation through camera-observable anchor motion in image and camera-frame coordinates, treating robot arms, humanoids, and human hands as different embodiments of a common action schema. A geometry-conditioned action translator combines predicted motion with target-embodiment kinematics to produce executable controls. The resulting decoupled architecture allows a shared VLA policy to learn transferable manipulation geometry while retaining embodiment-specific controllability. UCAG-P is trained on 4.03K hours of robot and simulation data and 2.34K hours of human demonstrations. A single checkpoint reaches 98.3% on LIBERO, 88.7% and 89.2% on RoboTwin Easy and Hard, 82.0% zero-shot on LIBERO-Plus, and 62.0% on RoboCasa GR-1, without benchmark-specific fine-tuning.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
