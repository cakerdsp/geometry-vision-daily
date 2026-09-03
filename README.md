# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：44
- 分类分布：
  - Neural Scene Representations & Rendering: 13
  - Embodied / Robotics / AR Applications: 11
  - 3D Reconstruction & Multi-view Geometry: 11
  - Dynamic / 4D Reconstruction: 6
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**1. 重建与生成的深度融合：从"串联桥接"走向"端到端统一"**
这是一个相当明确的信号。RoGe（2609.02847）直接移除了重建与生成之间的显式3D中间表示（如渲染图像、点图或3DGS），改为在隐式几何特征上进行端到端联合训练；InceptionGS（2609.02747）则采用"生成式自举"的迭代策略，在重建与生成之间动态权衡，解决非结构化视角采样下的区域缺失问题；DualDiff3D（2609.01516）通过双扩散先验分别约束结构与外观，避免单一网络中的属性冲突。此外，LightBridge（2609.02543）虽面向重打光，但其"前馈生成式框架 + 无需逐场景优化"的思路也高度吻合这一趋势。四篇论文共同指向一个方向：**生成模型的先验能力正在被更深层地嵌入3D重建管线，而非作为后处理或外部修复器**。

**2. 大规模、前馈式、免优化的场景级方法成为目标**
传统的"逐场景优化"范式正在被多篇论文挑战。LightBridge明确提出前馈式单次前向重打光，彻底摆脱逐场景优化；On-the-Fly3R（2609.00923）以零训练的方式将前馈3R模型扩展到5000+张UAV影像的在线重建；SA-WAM（2609.02531）将预训练视频扩散模型改造为3D感知的世界动作模型；RESELF（2609.01276）则利用预训练几何基础模型的适配完成第一视角场景重建与人体运动恢复。这些工作体现了**对大规模预训练模型的复用与适配**越来越成为主流，其背后的驱动力是对泛化能力、数据效率和实时性的追求。

**3. 动态4D表示进入"工程化"与"时间演化建模"阶段**
4D重建方向呈现两条并行路线：一条是存储与效率优化——CC-4DGS（2609.02184）通过计算变形场替换大型哈希表、压缩点云属性，将存储降至20-30MB/场景，同时保持渲染质量；EvoGS（2609.00994）则聚焦建模本身，将变形视为时间演化过程，通过持久化状态、历史外推与自适应校正增强对大幅度运动的鲁棒性。另一条是语言/语义注入——Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations（2609.02664）发现查询改写能显著提升4D高斯中的语言引导时空分割（时间准确率60.92%→92.21%）。**4D高斯泼溅正从"能重建"走向"高效重建、稳健重建、可交互理解"。**

**4. 评价体系与基准建设：从"方法论创新"到"可复现性与可部署性"**
MeshSplatBench（2609.01306）引入统一基准，系统评估三角形神经渲染从原生优化到Unity游戏引擎部署的完整管线，并复核了资产的拓扑健壮性；TAPVid-MV（2609.01899）构建了首个跨多视角、运动相机下的3D点跟踪基准，覆盖284个序列、109,769条轨迹，并发现现有方法在该任务上远未解决。值得注意的还有**取证领域**的两篇工作——从图像取证到文本中心图像取证，均依赖基准/挑战赛驱动。这一趋势反映：**社区正通过标准化评估隔离各环节误差来源（如几何错误 vs. 对应错误；引擎适配 vs. 表示简化），并以可复现性作为可靠进步的前提。**

**5. 单一模态向几何-语义-动作-物理的多模态统一感知演进**
SA-WAM将RGB、深度与动作在单扩散骨干中联合预测；RESELF联合恢复场景几何与穿戴者身体运动；MS-MEM（2609.02493）将主动视点选择、推动与抓取统一在不确定性感知的建图框架中；从第一视角的"Seeing the World and the Self"标题即可读出其统一意图。这类工作正在打破传统计算机视觉各子领域（重建、运动估计、抓取、SLAM）的边界，构建**以几何为锚点、多模态感知协同的闭环系统**。

---

#### 技术路线观察

| 方向 | 代表论文 | 技术侧重点 | 关键趋势判断 |
|------|---------|------------|-------------|
| **几何基础模型** | Gekko (2609.01530)、单目深度估计综述 (2609.01172) | 自监督共视性代理信号；判别式与生成式双范式梳理 | 从"预训练+微调"走向"从原始视频直接自监督训练"；相对改进作为监督信号的想法很新颖 |
| **3D重建 (静态)** | On-the-Fly3R、深度图引导BA (2609.01089) | 无训练在线扩展；无对应关系配准 | 解决"大规模+无约束输入"工程痛点，而非追求架构创新 |
| **3DGS/神经渲染** | RoGe、DualDiff3D、LightBridge、MeshSplatBench | 端到端统一重建-生成；双扩散先验；前馈重打光；跨引擎部署评估 | 从"优化表示"转向"训练可泛化模型"；对可部署性的关注显著提升 |
| **动态/4D重建** | EvoGS、CC-4DGS、查询改写×4DGS | 时间状态模型；计算变形场+属性压缩；语言查询重构 | 效率与鲁棒性是核心矛盾；**语言查询优化作为低成本高收益的切入点值得注意** |
| **机器人/AR/具身** | SA-WAM、MS-MEM、RESELF、MONORIGAMI、TAPVid-MV、取证系列 | 多模态统一世界模型；不确定性驱动动作选择；场景+身体联合重建；软体驱动硬件 | 从"感知"走向"感知-决策-行动"闭环；几何信息以轻量方式注入预训练模型成为重要手段 |

**整体判断**：几何基础模型的重要性持续上升，一方面体现为Gekko、RESELF对其的直接适配与改造，另一方面体现在SA-WAM中"可复用冻结VAE"的工程智慧。3D重建与神经场景表示的核心竞争点从"表示精度"转向"泛化与效率"。4D重建进入工程优化与语言交互的时代。机器人方向则成为视觉几何技术最活跃的验证场与集成端。

---

#### 值得优先阅读的论文

1. **RoGe (2609.02847)** — 摘要即明确提供了问题定义、方法与消融结论，思路清晰、比较完整。它代表"重建-生成融合"这一最活跃趋势的最激进形态（完全移除显式中间表示），对其他相关工作具有方法论启示。建议第一优先。

2. **Gekko (2609.01530)** — "将跨视图重建误差相对MAE的改进作为共视性代理"提出了一个非常优雅且可迁移的想法，零样本对应、位姿估计与点图回归上全面优于CroCo且提升显著。对自监督3D预训练感兴趣者必读。

3. **SA-WAM (2609.02531)** — 首次在单扩散骨干中实现RGB+深度+动作联合预测，是机器人方向的关键进展。值得注意的是其"非线性编码适配冻结VAE"的技术细节，无需3D微调即可注入几何信息，实现成本低、提升显著，极具借鉴价值。

4. **EvoGS (2609.00994)** — 提出将动态高斯变形建模为时间演化过程，直接针对现有方法在大幅/突变运动下鲁棒性不足的通病，思路明确且与当前4D渲染发展路径高度契合。

5. **TAPVid-MV (2609.01899)** — 作为首个多视角3D点跟踪基准，其结论"几何恢复是主要瓶颈、多视角跟踪器未稳定优于单目"将对未来点跟踪与重建方法的设计产生直接影响。对基准建设或点跟踪方向感兴趣的读者应优先了解，以规避错误方向。

---

#### 可能的研究机会

- **重建与生成融合的"反馈闭环"机制**：RoGe证明了联合训练中生成目标反向塑造几何条件的可行性，但反馈路径的具体

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-03T12:25:05-04:00
**Total number of papers:** 44
**Number of papers added in the latest update:** 11
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
<summary>AI 简析</summary>

### Metadata
- 标题：Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison  
- 作者：Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit  
- 出版日期：2026-09-01  
- 分类：Geometry Foundation Models  
- 链接：https://arxiv.org/abs/2609.01530

### 一句话总结
本文提出Gekko，一种将跨视图补全与掩码自编码的误差差异作为共视性代理信号、从而为所有掩码区域提供双目监督的自监督预训练方法。

### 研究问题
跨视图补全自监督预训练方法在重建非共视区域时参考视图提供信息不足，导致这些区域实质上退化为单目训练信号；如何将这一局限转化为有用的双向（双目）监督信号。

### 核心思路/方法
- 观察：跨视图重建误差相对于掩码自编码误差的相对改进程度可作为共视性的自监督代理——改进大表示共视区域，改进小表示非共视区域。
- 设计：Gekko网络从零开始联合训练三个任务：跨视图补全、掩码自编码，以及逐像素预测上述相对误差改进。
- 通过该相对改进预测，为所有掩码区域提供额外的双目信号，无需任何真值3D标注。
- 支持直接从原始视频训练，采用基于步长的课程学习，免去先前方法的复杂3D预处理。

### 主要贡献
- 提出Gekko框架，将跨视图补全的局限性转为可用的共视性代理信号，并引入额外的双目监督。
- 在零样本对应估计、相对位姿估计和点图回归上一致优于CroCo；在最严格相对位姿阈值下精度提升高达6倍，ETH3D端点误差降低22%。
- Gekko学习的额外通道本身即成为强共视性检测器；冻结特征优于同规模或更大规模的已发布跨视图骨干网络。
- 可从原始视频训练，匹配基于精选数据训练的模型，同时去除繁琐的3D预处理。

### 局限性
摘要未提供足够信息：未讨论方法在何种场景下失效、计算开销、对训练数据规模/多样性的依赖、与更大规模模型的比较细节等局限性均未提及。

### 阅读优先级
**高**。理由：该方法在3D视觉自监督预训练核心方向上提出新训练信号，并报告了跨多任务的一致性能提升；附带公开代码和模型，便于复现与验证，适合该领域研究者优先阅读。

</details>

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

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-02 - Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations

**Authors:** Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran
**Links:** [abs](https://arxiv.org/abs/2609.02664) - [pdf](https://arxiv.org/pdf/2609.02664)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D Gaussian, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations
- 作者：Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran
- 出版日期：2026-09-02
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02664

### 一句话总结
本文提出一种无需训练的查询改写策略，将冗长叙事性语言查询转化为精简关键词形式，从而显著提升4D高斯表示中复杂物体的时间定位与空间分割性能。

### 研究问题
现有4D高斯表示框架在进行语言引导的动态场景理解时，对冗长、叙事风格且包含噪声上下文信息的查询高度敏感，导致分割性能下降。本文研究查询改写对复杂物体分割的影响，探索如何通过压缩查询中的语言噪声来提升时空分割精度。

### 核心思路/方法
- 借鉴检索增强语言模型与关键词引导的查询重构思想，提出一种**无需训练的再解释策略**。
- 将长描述性查询逐步转化为**简洁的关键词接地形式**，在去除语言噪声的同时保留与物体中心表征相关的语义锚点。
- 在HyperNeRF和Neu3D数据集上进行验证，评估改写后查询对时间定位和空间分割的影响。

### 主要贡献
- 首次系统性研究查询改写对4D高斯表示中复杂物体分割的影响。
- 提出无需微调即可应用的查询重写策略，有效降低查询中的语言噪声。
- 实验显示：平均时间准确率从60.92%提升至92.21%，平均vIoU从20.08%提升至76.94%。
- 消融实验表明，更短、关键词聚焦的查询能带来更稳定的视频特征相似度分布，并与物体中心高斯表征更好对齐。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法无需训练即可带来显著的性能提升（时间准确率提升超30个百分点，vIoU提升近57个百分点），且面向4D动态场景理解这一活跃研究方向，思路简洁、实用性强，值得快速阅读。

</details>

<details>
<summary>Abstract</summary>

Recent 4D Gaussian representation frameworks have demonstrated strong performance in language-guided dynamic scene understanding. However, these methods remain highly sensitive to verbose and narrative-style queries that contain noisy contextual information. In this paper, we investigate the impact of query rewriting for complex object segmentation in 4D Gaussian representations. Inspired by recent findings in retrieval-augmented language models and keyword-guided query reformulation, we propose a training-free reinterpretation strategy that transforms long descriptive queries into concise keyword-grounded forms. Our approach progressively reduces linguistic noise while preserving semantic anchors relevant to object-centric representations. Experiments on HyperNeRF and Neu3D demonstrate that concise rewritten queries significantly improve both temporal localization and spatial segmentation performance. In particular, our method improves average temporal accuracy from 60.92% to 92.21% and average vIoU from 20.08% to 76.94% without any additional fine-tuning. Extensive ablation studies further reveal that shorter, keyword-focused queries consistently yield stable video-feature similarity distributions and better alignment with object-centric Gaussian representations

</details>

#### 2026-09-02 - CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting

**Authors:** Kyungdae Park, Chae Eun Rhee
**Links:** [abs](https://arxiv.org/abs/2609.02184) - [pdf](https://arxiv.org/pdf/2609.02184)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting
- 作者：Kyungdae Park, Chae Eun Rhee
- 出版日期：2026-09-02
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.02184

### 一句话总结
CC-4DGS通过计算变形场与点云属性压缩两项技术，将动态4D高斯溅射的每场景存储量降至20–30 MB，同时保持与现有先进方法相当的渲染质量与实时性能。

### 研究问题
如何减少动态4D高斯溅射方法对大型多分辨率哈希表和高维高斯属性的存储依赖，实现存储高效且可扩展的动态场景表示。

### 核心思路/方法
- 提出**计算变形场（CDF）**：用确定性密集哈希编码和紧凑神经解码器替代大型可学习多分辨率哈希表，动态生成变形特征，将变形存储压缩至每场景1–3 MB。
- 提出**规范点云属性压缩（CCA）**：通过条件自编码、选择性量化与残差码本，压缩高维球谐外观项及辅助高斯属性，实现3–5倍点云数据缩减且质量损失可忽略。
- 两者结合形成统一表示，在保持实时渲染的前提下将总存储降至20–30 MB。

### 主要贡献
- 重新设计动态高斯溅射的变形建模与规范属性存储，提升存储效率。
- 计算变形场将变形存储大幅压缩至1–3 MB/场景。
- 点云属性压缩管线实现3–5倍压缩，且质量损失极小。
- 在N3DV与Technicolor Light Field数据集上，重建精度与Swift4D等先进方法相当，同时显著提升存储效率与运行时内存权衡。

### 局限性
摘要未提供足够信息：未说明方法在处理极长序列、大尺度场景或极端动态时的表现限制；未报告具体GPU内存占用数值、训练时间或对部署硬件的要求；未讨论压缩后在高帧率或高分辨率下的边界情况质量。

### 阅读优先级
**高** — 理由：该工作直击动态4D高斯溅射的存储瓶颈，提出了一种兼具明显压缩收益与质量保持的实际解决方案；实验覆盖两个公开数据集并与强基线对比，结果可信度高；对于从事动态场景表示、神经渲染及高效存储相关研究的人员具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic four-dimensional (4D) Gaussian Splatting has emerged as a powerful explicit representation for high-quality view synthesis, yet existing methods still require tens to hundreds of megabytes per scene due to their heavy reliance on large multi-resolution hash tables and high-dimensional Gaussian attributes. This paper presents CC-4DGS, a storage-efficient and scalable framework that rethinks both deformation modeling and canonical attribute storage. First, we introduce a computational deformation field (CDF) that replaces large multi-resolution learnable hash tables with deterministic dense hash encoding and compact neural decoders, enabling on-the-fly synthesis of deformation features while reducing deformation storage to only 1--3 MB per scene. Second, we propose a compression of canonical point-cloud attributes (CCA) pipeline that compresses high-dimensional spherical harmonic appearance terms and auxiliary Gaussian attributes via conditional autoencoding, selective quantization, and residual codebooks, achieving 3--5$\times$ point-cloud reduction with negligible quality loss. Together, these components yield a unified representation that preserves real-time rendering performance while reducing total storage to 20--30 MB. Extensive experiments across the N3DV and Technicolor Light Field datasets demonstrate that CC-4DGS achieves reconstruction accuracy comparable to state-of-the-art methods such as Swift4D, while offering significantly improved storage efficiency and favorable runtime-memory trade-offs.

</details>

#### 2026-09-01 - EvoGS: Modeling Deformation Evolution for Dynamic Gaussian Splatting

**Authors:** Wei Dong, Shahram Shirani, Jun Chen, Han Zhou
**Links:** [abs](https://arxiv.org/abs/2609.00994) - [pdf](https://arxiv.org/pdf/2609.00994)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, dynamic Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EvoGS: Modeling Deformation Evolution for Dynamic Gaussian Splatting
- 作者：Wei Dong, Shahram Shirani, Jun Chen, Han Zhou
- 出版日期：2026-09-01
- 分类：Dynamic / 4D Reconstruction（次要：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2609.00994

### 一句话总结
EvoGS 将动态 3D 高斯变形建模为时间演化过程，通过持久化状态、历史外推与自适应校正，提升动态场景新视角合成的鲁棒性与质量。

### 研究问题
现有基于 MLP 的动态 3D 高斯泼溅（3DGS）方法在每个时间戳独立估计变形，难以应对大幅度或突变运动；如何利用时间连续性建模变形演化以提升动态重建质量是核心问题。

### 核心思路/方法
- 为每个高斯体维护持久化变形状态，而非逐时刻独立估计。
- 从历史变形状态外推未来状态，再使用 MLP 获得的观测进行校正。
- 校正权重自适应调节，利用时间残差记忆以及变形速度、轨迹偏差等演化统计量。
- 提出变形感知的稠密化策略：沿校正后的变形方向执行克隆与分裂，并用不确定性感知策略抑制变形历史不稳定区域的稠密化。

### 主要贡献
- 提出将动态高斯变形视为时间演化过程的新框架，替代逐时刻独立估计。
- 设计状态外推加 MLP 观测校正的双阶段机制，并引入自适应权重调节。
- 提出变形感知的稠密化方法，利用变形方向与不确定性提高重建质量。
- 实验表明在动态新视角合成任务上质量提升，并在多个基准上取得有竞争力的结果。

### 局限性
摘要未提供足够信息：未提及方法在特定场景（如极端运动、遮挡、实时性）下的限制，也未报告计算开销、内存占用或失败案例等详细局限性。

### 阅读优先级
**高**。理由：该工作直接针对动态 3D 高斯泼溅中变形估计的共性问题（对大幅/突变运动鲁棒性不足），提出新颖的演化建模思路，且引入变形感知稠密化作为辅助改进，方法层面具有较强创新性；适合关注动态/4D 重建与神经渲染的读者优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments
- 作者：Ming Liao, Chao Ye, Jianing Fei, Weiyang Lin
- 出版日期：2026-09-01
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.00619

### 一句话总结
本文提出DSG，一个面向动态室内环境的3D场景图构建框架，通过3D高斯表示中的物体变化检测和基于多粒度视觉上下文的空间关系推理，提升场景图的动态更新与关系识别精度。

### 研究问题
室内环境中物体位置常因人类活动或智能体交互而改变，导致已有场景图与当前场景不一致，本文旨在解决动态环境下3D场景图的准确构建与更新问题。

### 核心思路/方法
1. 构建语义感知的3D高斯场景表示，提出基于双视角渲染的物体变化检测方法，以实现场景图节点的可靠更新。
2. 提出融合多粒度视觉上下文的空间关系推理方法，使大语言模型能识别更丰富的物体间空间关系。
3. 基于AI2-THOR仿真平台构建动态室内场景图基准DynTHOR，用于动态环境下场景图构建的评估。

### 主要贡献
- 提出DSG动态3D场景图构建框架，支持物体变化检测与空间关系推理。
- 设计基于双视角渲染的物体变化检测机制，提升节点更新的可靠性。
- 提出多粒度视觉上下文的空间关系推理方法，增强空间关系识别能力。
- 构建动态场景图基准DynTHOR，并在DynTHOR、3RScan及真实场景中验证方法有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向具身智能与动态场景图构建，方法新颖且包含新基准，适合从事场景理解、具身智能相关研究的人员阅读；但摘要未给出量化性能对比或具体实验设置细节，论文重要程度需结合正文进一步判断。

</details>

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

#### 2026-09-02 - Adapting a Foundation Model for Lunar Surface Height Estimation

**Authors:** Patrick Bauer, Marius Schwinning, Melanie Siegel, Andreas Weinmann, Hichem Snoussi
**Links:** [abs](https://arxiv.org/abs/2609.02448) - [pdf](https://arxiv.org/pdf/2609.02448)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Adapting a Foundation Model for Lunar Surface Height Estimation
- 作者：Patrick Bauer, Marius Schwinning, Melanie Siegel, Andreas Weinmann, Hichem Snoussi
- 出版日期：2026-09-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.02448

### 一句话总结
本文提出对基础模型 Depth Anything V2（DAV2）进行微调，使其能够可靠地估计月球表面的相对高度，为着陆危险地形检测提供辅助信息。

### 研究问题
如何将通用单目相对深度估计基础模型 DAV2 适配到月球表面场景，从而获得准确、可靠的相对高度估计，辅助危险地形定位？

### 核心思路/方法
作者指出已有工作仅将 DAV2 作为零样本基线用于月球 DEM 估计，未针对目标域做适配，因而可能表现不佳。为此，他们提出使用公开的、由立体摄影测量（SPG）生成的月球表面 DEM 数据，对 DAV2 模型进行微调，将其转变为适用于月球表面的相对高度估计器。

### 主要贡献
- 提出一种基于微调 DAV2 的月球表面相对高度估计方法；
- 利用公开 SPG 衍生的月球 DEM 数据进行领域适配；
- 实验表明，与零样本模型相比，微调后的模型在性能上有显著提升，能够作为可靠的月球表面相对高度估计器。

### 局限性
摘要未提供足够信息：未报告具体实验数据集规模、评测指标、定量结果数值、与现有方法的详细对比，以及微调带来的计算成本或潜在的过拟合问题等细节。

### 阅读优先级
**中**。理由：该方法针对未来月球任务的危险地形检测需求，对基础模型进行领域微调，思路直接且结果有提升，具有一定实用价值；但摘要未给出定量实验细节，创新性主要体现在“适配策略”而非新的网络架构，建议对月球感知或深度估计微调感兴趣的研究者可阅读，非核心领域者可暂缓。

</details>

<details>
<summary>Abstract</summary>

Digital elevation models (DEMs) can provide accurate height information, making it invaluable for analyzing the lunar surface. As the European Space Agency (ESA) prepares for future lunar missions that aim to land on the Moon, a precise method for height estimation will be essential for hazardous terrain that could endanger the landing approach. Traditional approaches to generate DEMs from imagery, such as shape from shading (SfS) and stereophotogrammetry (SPG) have been proven highly valuable for this task. However, due to advancements in machine learning, especially computer vision, the focus has shifted towards monocular depth estimation via deep learning. The lunar surface is covered by rocks and craters, and classic hazard detection methods rely solely on 2D image data. Our goal is to address this issue by developing a relative lunar surface height estimator that can provide additional information for hazard localization. In this letter, we present a methodology that builds on the well-known zero-shot relative depth estimation model Depth Anything V2 (DAV2). Other works have been using it as a state-of-the-art comparison for their proposed lunar DEM estimation method, but without adaptations to the target domain. Thus, it may underperform. Therefore, we propose a fine-tuning strategy with publicly available SPG-derived DEM data of the lunar surface. Our results demonstrate a significant improvement in performance compared to the zero-shot model, effectively transforming DAV2 into a reliable relative depth estimator of the lunar surface.

</details>

#### 2026-09-01 - Seeing the World and the Self from Egocentric Video

**Authors:** Kai Guan, Minchao Jiang, Ruichen WangLi, Wentao Zhu, Lei Zhang
**Links:** [abs](https://arxiv.org/abs/2609.01276) - [pdf](https://arxiv.org/pdf/2609.01276)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** geometry foundation model, scene reconstruction, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seeing the World and the Self from Egocentric Video（从第一视角视频中感知世界与自身）
- 作者：Kai Guan, Minchao Jiang, Ruichen WangLi, Wentao Zhu, Lei Zhang
- 出版日期：2026-09-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.01276

### 一句话总结
本文提出统一框架 RESELF，从第一视角视频中联合恢复环绕场景的确定性度量几何与穿戴者的生成式全身运动，并显著优于各单独任务上的现有方法。

### 研究问题
如何从第一视角（自我中心）视频中，在共享度量坐标系下同时重建周围三维场景几何和穿戴者的全身运动？其中场景可见性高适合确定性几何回归，而身体被严重遮挡需要生成式运动推断，两类任务表现出不对称可见性与不同预测范式，联合恢复具有挑战性。

### 核心思路/方法
- 提出 RESELF（REconstructing the Scene and the sELF），统一框架将确定性度量几何重建与几何条件运动生成相结合。
- 将在大规模外部（exocentric）数据上预训练的几何基础模型适配到第一视角视频，采用逐帧尺度和相对位姿一致性目标。
- 利用产生的相机轨迹和潜在几何特征，作为扩散模型的条件来恢复穿戴者运动。
- 引入闭环运动学反馈阶段，在保持重建场景几何的同时进一步优化相机头部位姿。
- 从 EgoExo4D 中整理 EE4D-JSM 数据集，对齐第一视角视频、稀疏度量场景几何、相机轨迹与全身运动标注。

### 主要贡献
1. 提出首个（据摘要推断）统一处理第一视角场景重建与全身运动生成的框架 RESELF，解决两类任务不对称可见性与不同预测范式的问题。
2. 设计将大规模预训练几何基础模型适配到第一视角视频的训练目标（逐帧尺度与相对位姿一致性）。
3. 采用扩散模型进行几何条件化的身体运动生成，并加入闭环运动学反馈精化相机轨迹。
4. 构建 EE4D-JSM 基准数据集。
5. 实验表明 RESELF 在深度估计、相机跟踪和全身运动估计上均超过针对单个任务设计的现有最先进方法。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的失败情形、计算成本、对极端遮挡或复杂场景的鲁棒性等局限，也未提供消融分析或定量对比的具体数据。

### 阅读优先级
**高**。理由：该工作解决第一视角视频中场景重建与全身运动估计相互割裂的问题，提出统一定性几何重建与生成式运动推断的框架，属于 3D 视觉与人体运动分析的交叉热点方向。同时构造了新的数据基准，并在三个子任务上取得优于现有技术的性能，对相关研究者具有较高的参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Monocular Depth Estimation from a Single Image: Progress and Opportunities
- 作者：Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun, Yi-Hua Huang, Ziyi Yang, Peng Dai, Xiaojuan Qi
- 出版日期：2026-09-01T12:48:10Z
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.01172

### 一句话总结
这是一篇关于单目深度估计（MDE）领域的综述论文，系统梳理了从早期学习方法到以基础模型（foundation models）为代表的最新进展，并展望了未来研究方向。

### 研究问题
单目深度估计（从单一图像中估计场景深度）作为计算机视觉的基础挑战，其研究演进路径、核心方法分类、代表性模型对比，以及该领域在基础模型时代面临的开放问题与机遇。

### 核心思路/方法
该综述按时间与范式将领域发展分为几个阶段进行梳理：
- 首先明确问题定义，区分相对深度估计与度量深度估计，指出十年研究中面临的关键挑战；
- 介绍常见的问题形式化方法以及广泛使用的数据集（室内、室外、合成数据）；
- 回顾基础模型时代之前的主要进展，提炼具有影响力的方法在精度、效率与鲁棒性方面带来的核心洞见；
- 聚焦近期基于基础模型的方法，将其划分为判别式（discriminative）与生成式（generative）两大范式，强调大规模预训练（如DINOv3）和合成数据的关键作用；
- 通过定量基准和定性示例比较代表性模型，并讨论向视频深度估计的自然扩展；
- 展示深度估计在视觉SLAM、内容生成、机器人感知等实际应用中的集成；
- 最后指出开放挑战和有前景的研究方向。

### 主要贡献
- 提供单目深度估计领域从早期到基础模型时代的全面综述，涵盖问题定义、数据集、方法演进与应用集成的完整链条；
- 将基础模型时代的方法归类为判别式与生成式两大范式，并指出大规模预训练与合成数据的核心价值；
- 通过定量与定性对比，帮助读者理解代表性模型的差异；
- 讨论深度估计向视频任务的自然延伸及其在视觉SLAM、内容生成、机器人感知等真实场景中的应用；
- 总结开放挑战与未来研究方向，为领域后续发展提供指引。

### 局限性
摘要未提供足够信息：未包含关于具体遗漏的研究方向、方法对比的详细量化结果，或综述所覆盖文献范围的明确边界等局限性说明。

### 阅读优先级
**高**。理由：单目深度估计是计算机视觉核心问题，与3D重建、机器人、自动驾驶、AR等领域直接相关。该综述覆盖了从经典方法到基础模型时代的最新技术进展（含DINOv3等前沿预训练模型），且作者团队来自知名机构，发表于2026年，时效性强，适合希望快速把握该领域全貌与未来趋势的研究者阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Adaptive Depth-Map-Guided Bundle Adjustment for Correspondence-Free Multi-View Point Cloud Registration
- 作者：Yiran Zhou, Yingyu Wang, Shoudong Huang, Liang Zhao
- 出版日期：2026-09-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.01089

### 一句话总结
提出一种自适应的分层深度图引导束调整框架，用于无对应关系的多视角点云配准，以提升工业不规则钢废料场景下的三维重建精度与鲁棒性。

### 研究问题
在具有光滑金属表面、重复结构、遮挡和部分重叠的工业场景中，现有基于特征提取与数据关联的多视角配准方法容易建立错误对应关系，导致位姿估计不准确和重建失真。该文旨在解决这一问题，实现无需显式特征对应的多视角点云配准。

### 核心思路/方法
- 采用全局2.5D栅格表示场景，每个栅格单元可自适应维护多个深度假设。
- 将原始深度观测直接投影到全局地图中形成深度约束，无需显式特征对应。
- 当多个表面在同一栅格产生深度冲突时，通过基于softmax的层分配将每个观测关联到兼容的深度假设。
- 构建非线性最小二乘问题，联合优化传感器位姿与分层深度图；对应关系由深度图表示和投影模型隐式推导。

### 主要贡献
- 提出一种无对应关系的多视角点云配准框架，避免错误特征对应导致的问题。
- 通过自适应分层深度图表示处理多表面深度冲突。
- 在自采集工业数据集上验证，该方法在挑战性工业场景中达到稳定的重建精度，同时保持鲁棒性和低计算开销。
- 公开了开源代码。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法面向工业特种场景（不规则钢废料处理），核心贡献在无对应关系的多视角配准和分层深度图束调整，对从事三维重建、机器人感知相关研究的读者有参考价值；但实验仅基于作者自采集数据，缺少与主流方法的定量对比细节，普适性尚待验证。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios
- 作者：Zhe Shen, Liyuan Lou, Yifei Yu, Guanbo Wang, Quanjian Ji, Xin Wang, Zongqian Zhan
- 出版日期：2026-09-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.00923

### 一句话总结
提出一种无需训练的在线渐进式三维重建框架 On-the-Fly3R，通过检索引导的动态子集构建和验证-拒绝-重试机制，将前馈 3R 模型扩展到大规模无人机无序影像序列上。

### 研究问题
前馈 3D 重建模型在大规模无人机航测场景中面临 Transformer 注意力显存开销过大、以及对弱有序或无序影像流适应性不足的问题，现有可流式 3R 方法依赖时间和空间连续的输入，无法直接用于跨航线无人机作业。

### 核心思路/方法
- 提出 **训练无关的渐进式在线重建框架**，可适配多种现有 3R 骨干网络。
- 通过 **检索引导的动态子集构建** 从无序输入中选择空间相关的影像子集进行重建。
- 设计 **验证-拒绝-重试机制**：进行预集成一致性检查，自动拒绝错位影像并改用替代子集重试，以保证全局一致性。
- 借鉴 VSLAM 思想，基于检索闭环进行 **位姿图优化**，缓解相机漂移。

### 主要贡献
- 提出 On-the-Fly3R，首个面向大规模无人机场景的无需训练的在线三维重建框架，支持无序影像输入。
- 在多个 UAV 基准上将多种 3R 模型扩展到 5000+ 张影像、覆盖平方公里级场景。
- 相比多种 SOTA 流式 3R 方法，重建精度显著更优。
- 开源代码：https://github.com/Sh1nZzz/On_the_Fly3R

### 局限性
摘要未提供足够信息（未讨论时间效率、位姿图优化引入的额外计算开销、具体失败场景或对极端无序输入的上限等）。

### 阅读优先级
**中** — 该工作针对无人机大规模无序影像的三维重建提出了实用框架，对从事 UAV 测绘与在线重建的研究者有参考价值，但若您的兴趣不在此方向，影响力可能有限。框架无需训练便迁移到多种 3R 模型，适配性较强，建议相关方向读者关注。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Efficient and Robust Absolute Pose Estimation via Gravity-Prior-Driven Transformation Decoupling and Pose Refinement
- 作者：Hu Cao, Qianyi Yang, Xinyi Li, Jiong Liu, Yinlong Liu, Alois Knoll
- 出版日期：2026-09-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.00713

### 一句话总结
本文提出一种利用重力先验对绝对位姿估计进行变换解耦的方法，将6自由度问题降为4自由度，并配合全局投票与位姿精化算法，实现了高效且鲁棒的绝对位姿估计。

### 研究问题
如何在存在大量错误匹配的情况下，利用重力方向先验信息，高效且鲁棒地求解物体的绝对位姿（6自由度），并进一步从内点对应关系中获取精确的位姿解。

### 核心思路/方法
- 利用重力先验推导几何关系，通过变换解耦将原始6自由度绝对位姿估计问题简化为4自由度问题：1自由度旋转角 + 3自由度平移。
- 对1自由度旋转角采用一维全局投票算法进行最优估计。
- 获得最优旋转后，初步过滤错误匹配；平移估计退化为线性问题，易于求解。
- 引入一种新的位姿精化算法，同时提升旋转和平移的精度。

### 主要贡献
- 提出基于重力先验的变换解耦策略，将6自由度位姿估计简化为4自由度问题，显著提升效率。
- 设计1自由度旋转角的全局投票估计方法，增强对误匹配的鲁棒性。
- 提出新的位姿精化算法，进一步提升位姿精度。
- 在合成数据和三个公开真实数据集（TUM RGB-D、ETH3D、RobotCar）上验证了优于现有最先进方法的性能。
- 将方法集成到ORB-SLAM2中，在KITTI数据集上确认其能有效减少漂移并改善重定位时的轨迹对齐；代码将在论文接收后开源。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对机器人领域的基础问题（绝对位姿估计），在利用重力先验方面提出了新的变换解耦思路，显著降低问题维度，并在多个真实数据集及SLAM系统集成中验证了有效性。方法新颖且实用性强，对从事位姿估计、视觉SLAM及3D重建相关研究的人员具有较高参考价值。

</details>

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

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-02 - RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation

**Authors:** Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang
**Links:** [abs](https://arxiv.org/abs/2609.02847) - [pdf](https://arxiv.org/pdf/2609.02847)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, novel view synthesis, view synthesis, scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation
- 作者：Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang
- 出版日期：2026-09-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.02847

### 一句话总结
RoGe提出一种端到端统一框架，将前馈隐式场景重建与视频扩散生成模型联合训练，通过射线查询注入几何条件，实现稀疏视角下的新视角合成。

### 研究问题
如何在稀疏输入视图下进行新视角合成，同时兼顾已观测区域的几何准确性（重建）与未观测区域的生成先验（生成），并克服现有混合方法中二者通过显式/有损中间表示桥接而导致的误差传播问题。

### 核心思路/方法
RoGe移除了重建与生成之间的显式3D中间桥梁，具体流程为：
1. 从稀疏输入视图出发，利用前馈重建模型构建隐式场景表示。
2. 用目标相机射线查询该隐式表示，获得逐视角的几何特征。
3. 将这些几何特征直接注入视频扩散模型作为条件，不经过图像渲染或显式3D表示。
4. 重建模型与生成模型端到端联合训练，使生成目标能反向塑造几何条件。

### 主要贡献
- 提出端到端的统一重建与生成框架RoGe，消除了重建与生成之间的显式桥接。
- 利用射线查询得到的隐式几何特征作为扩散模型条件，替代原始重建token或渲染图像。
- 联合训练使生成目标直接作用于几何条件，提升条件质量。
- 在DL3DV数据集上，图像级指标与视频级时序一致性上均优于重建式、生成式及混合式基线。
- 消融实验表明：射线查询的隐式特征优于原始重建token与渲染RGB；联合训练带来额外收益。

### 局限性
摘要未提供足够信息，未说明方法在DL3DV之外的泛化能力、计算开销、对极端稀疏视角或大轨迹的鲁棒性等问题。

### 阅读优先级
**高**

理由：该工作针对新视角合成中重建与生成结合的痛点提出端到端统一方案，方法设计新颖（移除显式3D桥梁、用射线查询注入条件），并在多类基线上取得一致性优势，对神经场景表示与生成模型结合方向具有较强参考价值。但具体实验结果细节（如数值指标、模型复杂度）需进一步查阅全文。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis from sparse inputs requires both geometric grounding from the observed views and generative priors of unobserved regions, motivating recent hybrid methods that combine reconstruction and generation. However, existing methods bridge the two with rendered images or explicit 3D representations such as point maps or 3D Gaussians. Generation is thus conditioned on a lossy and imperfect projection of the scene, inheriting its errors, and reconstruction receives no signal from generation to correct them. We present RoGe, an end-to-end unified reconstruction and generation framework that removes this explicit bridge. It targets roaming within a scene anchored by sparse views: given a few posed images and a camera trajectory, it synthesizes a temporally coherent video along that trajectory. From the sparse input views, RoGe builds an implicit scene representation with a feed-forward reconstruction model, and queries it with target camera rays to obtain per-view geometric features. These features are injected into a video diffusion model as conditioning, without any 3D intermediate. Both modules are trained jointly, so the generation objective directly shapes its own geometric conditioning. We conduct experiments on DL3DV, where RoGe outperforms reconstruction-based, generation-based, and hybrid baselines on image-level metrics and video-level temporal consistency. Ablations confirm that ray-queried implicit features outperform both raw reconstruction tokens and rendered RGB as conditioning, and that joint training brings further gains.

</details>

#### 2026-09-02 - InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling

**Authors:** Tianheng Lu, Guangyu Wang, Ruqi Huang, Lu Fang
**Links:** [abs](https://arxiv.org/abs/2609.02747) - [pdf](https://arxiv.org/pdf/2609.02747)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling
- 作者：Tianheng Lu, Guangyu Wang, Ruqi Huang, Lu Fang
- 出版日期：2026-09-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.02747

### 一句话总结
InceptionGS 通过将重建与生成先验巧妙结合，对大规模场景的高斯泼溅进行引导式自举修复，以应对非结构化视角采样下因部分区域视图稀疏而导致的渲染质量问题。

### 研究问题
在大规模场景数字化中，当采集到的多视角图像分布高度非结构化（大部分区域覆盖良好但局部区域观测不足）时，如何实现所有可能视角下一致且视觉上令人满意的渲染输出。

### 核心思路/方法
- 从初始高斯泼溅（Gaussian Splatting）出发，采用“生成式自举”（Generative Bootstrapping）策略。
- 在重建与生成之间进行巧妙权衡：对因视图稀缺导致的问题区域进行重新思考与修复，同时保持其余区域的重建质量。
- 通过软性引入场景自适应与视角自适应的生成先验（generative priors），实现对缺失观测区域的合理补全。
- 算法流程为迭代式引导修复，而非端到端单一生成或纯重建。

### 主要贡献
- 提出 InceptionGS 框架，首次在统一框架中平衡重建与生成，解决非结构化视角采样下的大规模高斯泼溅痛点。
- 引入场景与视角双自适应的生成先验软融合机制，使修复过程适应不同区域的稀疏程度。
- 在真实大规模场景上验证了方法的优越性与广泛适用性，证明其能处理非结构化影像并提升高保真高斯泼溅质量。
- 补充视频提供更直观的视觉演示效果。

### 局限性
摘要中提到“大规模真实场景”的实验均未在摘要中给出具体数据集、量化对比指标或失败案例细节，因此实验层面的局限性（如计算开销、极端稀疏下的表现上限、先验失效场景等）无法判断——**摘要未提供足够信息**。

### 阅读优先级
**高**，理由：  
- 该工作针对大规模场景重建中“真实且普遍”的视图非均匀覆盖问题，具有明确的实际应用价值。  
- 将生成模型与传统神经渲染结合是当前热点方向，框架设计上有新颖性（软性生成先验引导自举）。  
- 作者团队及发表时间具备一定新鲜度，适用于关注大规模渲染、高斯泼溅或神经场景表示的前沿研究者。

</details>

<details>
<summary>Abstract</summary>

Achieving truly immersive large-scale scene digitization necessitates consistent and visually pleasing rendering across all possible viewing perspectives. However, collecting multi-view images covering every fine detail of a large-scale scene is prohibitive due to scene complexity, capture cost, negligence, or accessibility constraints. As a result, the sampled views tend to be highly unstructured -- the majority of the scene is well covered yet certain regions inevitably lack sufficient observations. Existing reconstruction based methods are vulnerable to view scarcity while generation based approaches suffer from generalization, controllability, and 3D consistency issues. To address this challenge, we propose InceptionGS, which bootstraps Gaussian splatting by subtly balancing reconstruction and generation. Starting from an initial Gaussian splatting, InceptionGS reasonably rethinks and repairs problematic regions caused by view scarcity while preserving the quality elsewhere, by softly incorporating scene- and view-adaptive generative priors. Extensive experiments on real-world large-scale scenes demonstrate the superiority and broad applicability of our approach in handling unstructured imagery and boosting high-fidelity Gaussian splatting. Please refer to the supplementary video for better visual demonstrations.

</details>

#### 2026-09-02 - LightBridge: Feed-Forward Generative Relighting for 3D Gaussian Splatting

**Authors:** Hezhi Cao, Panhao Cheng, huangsheng du, Qibiao Li, Youcheng Cai, Ligang Liu
**Links:** [abs](https://arxiv.org/abs/2609.02543) - [pdf](https://arxiv.org/pdf/2609.02543)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, inverse rendering, relighting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LightBridge: Feed-Forward Generative Relighting for 3D Gaussian Splatting
- 作者：Hezhi Cao, Panhao Cheng, huangsheng du, Qibiao Li, Youcheng Cai, Ligang Liu
- 出版日期：2026-09-02T12:58:24Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.02543

### 一句话总结
LightBridge 提出一种前馈式生成框架，无需逐场景优化即可对完整 3DGS 资产实现单次前向的可控重打光。

### 研究问题
如何在保持 3D Gaussian Splatting (3DGS) 高质量实时渲染优势的同时，实现高效且可控的重打光，避免传统逆向渲染方法的低效和生成式方法所需的逐场景优化阶段。

### 核心思路/方法
1. 构建大规模多光照重打光数据集（Multi-Illumination Relighting Dataset），包含同场景的成对源光照与目标光照观测，以支持前馈训练。
2. 提出 Latent Bridge Relighting Diffusion 模型，将重打光建模为潜空间中的源到目标传输（transport），实现无需迭代扩散采样的一步式 2D 视觉 token 提取。
3. 设计 Gaussian Propagation Transformer，利用点变换器结合稀疏图像到点自注意力与点到图像交叉注意力，将视觉线索高效传播到完整 3DGS，避免对所有图像和高斯 token 进行全注意力计算。

### 主要贡献
- 提出首个面向完整 3DGS 资产的单次前馈可控重打光生成框架。
- 基于数据集的构造和潜空间传输扩散设计，实现无需逐场景优化的一步式重打光预测。
- 提出高斯传播变换器，通过稀疏注意力机制高效地将 2D 线索传播到 3DGS。
- 实验验证了该设计在重打光质量和单次前向预测效率上的竞争力，并将公开代码和数据集。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对 3DGS 重打光这一活跃研究方向提出了无需逐场景优化的前馈式解决方案，在方法设计和效率上具有显著创新性，对生成式神经渲染和场景编辑领域有较强参考价值；且代码与数据集将公开，便于复现和后续研究。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves high-quality, real-time novel view synthesis, but the resulting assets have baked-in illumination and cannot be easily relit. Inverse rendering methods optimize simplified reflectance and illumination models for each scene, limiting efficiency and relighting quality. Recent generative approaches leverage large diffusion models for realistic lighting edits, but applying them to 3DGS typically requires an additional per-scene optimization stage to bake the edited appearance into the representation. We present LightBridge, a feed-forward generative framework for controllable relighting of complete 3DGS assets in a single pass. To enable feed-forward training, we construct a large-scale Multi-Illumination Relighting Dataset with paired source and target observations of the same scenes. Latent Bridge Relighting Diffusion models relighting as source-to-target transport in latent space, enabling one-step extraction of 2D visual tokens without iterative diffusion sampling. A Gaussian Propagation Transformer uses a point transformer with sparse image-to-point self-attention followed by point-to-image cross-attention to efficiently propagate these cues across the complete 3DGS, while avoiding full attention over all image and Gaussian tokens. Experiments validate these designs, demonstrating competitive relighting quality and efficient single-pass prediction of complete relit 3DGS assets without scene-specific optimization. The code and dataset will be made publicly available upon acceptance.

</details>

#### 2026-09-01 - DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting

**Authors:** Qian Wang, Yu Wang, Weiqi Li, Xinhua Cheng, Xiandong Meng, Ronggang Wang, Jian Zhang
**Links:** [abs](https://arxiv.org/abs/2609.01516) - [pdf](https://arxiv.org/pdf/2609.01516)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting
- 作者：Qian Wang, Yu Wang, Weiqi Li, Xinhua Cheng, Xiandong Meng, Ronggang Wang, Jian Zhang
- 出版日期：2026-09-01T16:45:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.01516（摘要页）/ https://arxiv.org/pdf/2609.01516（PDF）

### 一句话总结
本文提出DualDiff3D，通过引入结构-外观双扩散先验及可靠性增强的渲染-细化-优化循环，改善少视图条件下3D高斯泼溅的重建质量和新视角渲染效果。

### 研究问题
在输入视图数量有限的情况下，3D高斯泼溅（3DGS）重建质量差、渲染的新视角存在伪影。现有利用扩散先验的方法通常将渲染视图与参考视图沿额外维度拼接输入单一网络，忽略了不同视图间“外观应相似但结构因视角变化而不同”的固有特性，导致两类属性相互冲突并产生模糊。

### 核心思路/方法
- 提出**DualDiff**管线：利用双扩散先验，其中一个扩散分支专注从低质量新视角中提取结构信息，另一分支确保与参考视图的外观一致性；引入**结构-外观注意力（SAA）模块**实现参考引导，细化从有缺陷的3D表示中渲染出的低质量新视角。
- 提出**DualDiff3D**重建框架：集成**可靠性增强的渲染-细化-优化（RRO）循环**，逐步且鲁棒地将细化后的新视角融入优化过程，从而获得更精确的3DGS模型。

### 主要贡献
- 提出DualDiff双扩散先验管线及SAA模块，分别处理结构信息与外观一致性，避免单一网络中的属性冲突。
- 提出DualDiff3D框架及RRO循环，稳健集成细化新视角以提升3DGS重建精度。
- 实验表明，在仅推理（inference-only）设置下即取得优于现有方法的效果，且通过训练可进一步提升性能。
- 开源代码与预训练权重。

### 局限性
摘要未提供足够信息，无法获取关于方法在极端少视图、复杂场景、计算开销或失败案例等方面的局限性。

### 阅读优先级
**高**。理由：该工作针对3DGS在少视图下的关键缺陷提出双扩散先验与注意力机制，创新性强；且在推理-only设置下即优于现有方法，训练后进一步提升，具备实际应用潜力；代码与权重已开源，便于复现和后续研究。该方向属于3D重建与渲染的热点领域，适合相关研究者优先精读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MeshSplatBench: A Unified Benchmark for Triangle-Based Neural Rendering
- 作者：Kaixuan Zhang, Minxian Li, Mingwu Ren, Xiatian Zhu
- 出版日期：2026-09-01
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.01306

### 一句话总结
MeshSplatBench 是一个统一的基准测试，系统评估基于三角形的神经渲染方法从原生优化到游戏引擎部署全流程的可部署性与保真度。

### 研究问题
现有基于三角形的神经渲染方法几乎仅在定制研究渲染器中评估，其在生产级引擎中的实际可部署性不明确。因此，本文旨在填补这一空白，统一度量该类方法在完整管线（原生优化到游戏引擎）中的真实表现。

### 核心思路/方法
MeshSplatBench 提出并实施三部分方法：1) 建立标准化评估协议，同时保留各方法的原生优化语义，可在0.8% PSNR偏差内复现已发表结果；2) 引入分层Unity部署协议，包含三个渲染层级（原生CUDA渲染器、方法专用的引擎着色器、标准不透明网格管线），以隔离引擎适配与表示简化分别造成的保真度损失；3) 对重建表面进行拓扑审计，检查非流形结构、碎片化组件和边界伪影等影响资产可用性的问题。

### 主要贡献
- 首次提出统一基准 MeshSplatBench，系统化覆盖三角形神经渲染从原生优化到游戏引擎部署的完整管线。
- 建立标准化评估协议，可高保真复现（0.8% PSNR偏差内）现有方法的已发表结果。
- 设计分层Unity部署协议，用于分离不同来源的保真度损失（引擎适配 vs. 表示简化）。
- 通过拓扑审计揭示：仅依赖显式连接与共享索引不足以确保生产级资产质量，仍普遍存在非流形结构、碎片化组件及边界伪影。

### 局限性
摘要未提供足够信息（例如：具体测试方法数量、基准的数据集范围、计算资源开销、对实时性的量化评估等均未在摘要中说明）。

### 阅读优先级
**中**。理由：该工作为领域提供了缺失的统一基准和跨引擎部署评估协议，对需要将神经渲染用于实际图形管线的研究者具有参考价值；但摘要未展示具体的对比结果、定量发现或创新性评估指标，故非同领域内的高优先阅读项。对专注游戏引擎部署或三角形网格渲染的读者，可适当上调优先级。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Inverse Rendering for Modeling with Line Primitives
- 作者：Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel
- 出版日期：2026-09-01
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.00625

### 一句话总结
提出一种基于显式线段图元的逆向渲染方法，在保持与标准图形管线兼容的同时，实现具有模糊、各向异性结构（如毛发、纤维、纺织品）的物体重建与高质量渲染。

### 研究问题
如何利用显式的低维图元（线段）而非体素化图元（如3D高斯），从多视角图像中重建具有半透明、模糊结构外观的真实物体，同时兼容标准图形渲染、反射建模和物理模拟流程。

### 核心思路/方法
- 使用显式线段作为重建图元，并在亚像素网格上进行光栅化以实现抗锯齿，从而再现半透明外观。
- 提出一种针对线段的随机可微光栅化器，能够为顶点位置、属性和离散连通性提供有效梯度，便于优化大量线段图元以匹配目标图像。

### 主要贡献
- 首次将显式线段用于逆向渲染重建模糊几何，避免了体表表示的不兼容问题。
- 设计了针对线段的随机可微光栅化器，解决了在线段图元上优化众多参数的难题。
- 实验证明该方法在捕捉模糊边界上优于基于表面的方法，且质量与体素表示相当，同时完全依赖显式几何。
- 输出表示可无缝集成至标准图形管线，支持跨平台渲染、多种着色模型和物理模拟。

### 局限性
摘要未提供足够信息（包括对线数规模、内存/计算开销、在极端复杂场景下的表现、算法鲁棒性、实时性能指标、以及与特定体素方法定量对比的详细实验设置均未在摘要中说明）。

### 阅读优先级
**中**。理由：该方法在图形学与逆向渲染领域具有创新性，解决了显式几何与体积质量的权衡问题，但论文涉及的表示与优化技术相对专门，若研究兴趣不在模糊几何建模或可微渲染方向，则参考价值有限。

</details>

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

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-02 - From Detection to Localization: A Unified Forensics Framework for Fully Synthetic and Tampered Images

**Authors:** Annalisa Gallina, Marco Fiorucci, Marco Brigo, Federica Battisti, Lamberto Ballan
**Links:** [abs](https://arxiv.org/abs/2609.02640) - [pdf](https://arxiv.org/pdf/2609.02640)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Detection to Localization: A Unified Forensics Framework for Fully Synthetic and Tampered Images
- 作者：Annalisa Gallina, Marco Fiorucci, Marco Brigo, Federica Battisti, Lamberto Ballan
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02640

### 一句话总结
本文提出一个统一的多分类图像取证框架，能同时区分真实、全生成和篡改图像，并通过分割分支实现篡改区域的像素级定位。

### 研究问题
现有图像篡改检测方法通常将问题简化为二分类（真实 vs. 生成），无法区分和定位不同类型的篡改操作，限制了取证能力的细粒度。本文旨在解决这一局限，实现更全面的图像伪造识别与定位。

### 核心思路/方法
- 在已有检测器基础上进行扩展，引入统一的多分类框架（真实 vs. 全生成 vs. 篡改三类）。
- 除图像真实性分类外，框架中加入分割分支，以支持篡改区域的像素级定位。
- 该框架将检测与定位任务整合于同一模型，提升取证效率。

### 主要贡献
- 提出了一个统一的多分类取证框架，突破了传统二分类的局限。
- 结合分类与分割两个任务，实现篡改区域的像素级定位。
- 在分类准确率和定位IoU指标上优于所选的近期基准方法。
- 公开了代码实现。

### 局限性
摘要未提供足够信息：摘要未提及方法的失败案例、计算开销、对特定伪造类型的鲁棒性、数据集构成或实验范围的局限。

### 阅读优先级
**中**。理由：该工作面向多媒体取证中的实用需求，提出统一分类与定位的方案，方法较完整且有基准对比，但属于对现有检测器的改进型扩展，创新幅度有限；若研究领域相近（图像取证、伪造检测/定位），可重点阅读框架设计与分割分支的整合方式。

</details>

<details>
<summary>Abstract</summary>

The rapid advancement of generative models has significantly worsened the problem of manipulated image detection, as these methods are capable of producing highly realistic forgeries, reinforcing the importance of multimedia forensics. Conventional approaches typically frame image manipulation detection as a binary classification task (real vs. generated), which limits the capability to distinguish and localize different forms of manipulation. To address these constraints, this work extends an existing detector by introducing a unified multiclass framework (real vs. fully generated vs. tampered). In addition to classifying image authenticity, the framework incorporates a segmentation branch to enable pixel-level localization of tampered regions. The proposed approach outperforms selected recent benchmarks, offering an efficient solution with improved classification accuracy and higher IoU scores for the localization task. Find the code at https://github.com/anngal01/From-Detection-to-Localization-A-Unified-Forensics-Framework-for-Fully-Synthetic-and-Tampered-Images.

</details>

#### 2026-09-02 - Spatially Aware World Action Model via Geometric Latent Diffusion

**Authors:** Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid
**Links:** [abs](https://arxiv.org/abs/2609.02531) - [pdf](https://arxiv.org/pdf/2609.02531)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth prediction, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatially Aware World Action Model via Geometric Latent Diffusion
- 作者：Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02531

### 一句话总结
本文提出SA-WAM，在预训练视频扩散模型中同时引入深度预测与动作预测，使世界动作模型具备3D空间感知能力，并在仿真与真实机器人基准上取得领先结果。

### 研究问题
现有的世界动作模型（WAMs）仅基于RGB观测进行未来预测与动作生成，未利用3D几何信息，限制了其在机器人策略学习中的空间理解能力。如何在不破坏预训练先验的前提下，将几何信息融入统一的世界模型与动作预测框架是核心问题。

### 核心思路/方法
- 在单一扩散骨干网络中，将预训练视频模型扩展为联合预测动作、RGB和深度图的三模态输出。
- 使用非线性编码将无界深度信号映射到冻结VAE tokenizer所预期的有界输入域，从而无需针对3D进行微调即可复用现有tokenizer，保留预训练的视频与物理先验。

### 主要贡献
- 提出SA-WAM，首个在单扩散骨干中实现RGB、深度与动作联合预测的3D感知世界动作模型。
- 设计非线性深度编码方法，支持冻结tokenizer直接消费几何信息，避免3D专用微调带来的先验损失。
- 在RoboCasa和LIBERO-Plus基准上取得最先进结果，并提升未来状态预测质量。
- 在真实UR5机械臂评估中超越强基线，尤其在随机化环境中增益显著。
- 分析了世界模型预测质量与任务成功率之间的相关性，为WAM性能改进提供依据。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作首次将3D几何信息以轻量方式整合进预训练视频世界模型，同时兼顾动作预测与未来状态预测，在仿真和真实机器人上均验证了有效性；面向具身智能和机器人策略学习方向的研究者具有较高参考价值，且分析预测质量与成功率的关系对后续工作有启发意义。

</details>

<details>
<summary>Abstract</summary>

World Action Models (WAMs) leverage the capabilities of large-scale pretrained video diffusion models to jointly predict future observations and actions, inheriting rich visual and physical priors from internet-scale video. This has made them a promising paradigm for robot policy learning, yet the prevailing models operate exclusively on RGB observations and do not leverage 3D information. To bridge this gap, we introduce a Spatially Aware World Action Model (SA-WAM), which repurposes a pretrained video model for joint action, RGB, and depth prediction, enabling 3D-aware world modeling and action prediction within a single diffusion backbone. We use a nonlinear encoding that maps the unbounded depth signal into the bounded input domain expected by the frozen VAE tokenizer. This allows us to reuse the tokenizer without 3D-specific fine-tuning, incorporating geometric information without sacrificing the pretrained priors. SA-WAM achieves state-of-the-art results on the RoboCasa and LIBERO-Plus benchmarks, while simultaneously improving future-state predictions. Furthermore, SA-WAM outperforms strong baselines in real-world evaluation using a UR5 robotic arm, with strong gains in randomized environments. We analyze the correlation between world model prediction quality and rollout success, providing insights into WAM performance and avenues for its improvement.

</details>

#### 2026-09-02 - MS-MEM: Multi-Skill Manipulation-Enhanced Mapping via Uncertainty- and Disturbance-Aware Action Selection

**Authors:** Yitian Shi, Jesper Mücke, Nils Dengler, Sicong Pan, Rania Rayyes, Maren Bennewitz
**Links:** [abs](https://arxiv.org/abs/2609.02493) - [pdf](https://arxiv.org/pdf/2609.02493)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MS-MEM: Multi-Skill Manipulation-Enhanced Mapping via Uncertainty- and Disturbance-Aware Action Selection
- 作者：Yitian Shi, Jesper Mücke, Nils Dengler, Sicong Pan, Rania Rayyes, Maren Bennewitz
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02493

### 一句话总结
本文提出 MS-MEM，一种结合主动视点选择、物体推动与抓取的多技能操作增强建图框架，通过不确定性感知与扰动约束的统一动作选择，在提高建图精度的同时减少对场景的干扰。

### 研究问题
如何在狭窄、杂乱的空间（如货架）中，通过多技能操作与主动感知的协同，实现高效且低干扰的场景建图与物体定位，以应对严重遮挡和受限可达性的挑战。

### 核心思路/方法
1. 构建场景级度量-语义证据信念估计器，用于不确定性感知建图和环境表示。
2. 引入不确定性感知的抓取表示，基于一种全证据抓取估计器进行学习，同时建模抓取可行性与朝向不确定性。
3. 设计统一的动作选择管线，以共同的信息增益准则评估候选的感知与操作动作（视点选择、推动、抓取）。
4. 针对操作动作，提出附带扰动约束，抑制对场景信念中高置信区域的过度改变，在降低建图不确定性的同时控制场景扰动。

### 主要贡献
1. 提出 MS-MEM 框架，整合主动视点选择、物体推动与抓取三种能力，实现多技能协同的建图增强。
2. 提出基于全证据估计的不确定性感知抓取表示，同时估计抓取可行性与朝向不确定性。
3. 提出统一信息增益驱动的动作选择机制，并设计附带扰动约束，以实现建图精度与场景扰动之间的平衡。
4. 实验表明，相比单技能基准与忽略扰动的无约束基准，MS-MEM 可实现更高建图精度并显著降低场景扰动。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作在机器人建图与操作交叉领域具有一定创新性，统一了多技能动作选择与不确定性/扰动建模；但由于摘要未给出具体实验设置、定量结果与部署细节，且面向较为特定的货架场景任务，适合对主动感知或多技能操作建图感兴趣的读者作为方法参考，而非常规通用视觉或建图研究者必须优先精读的工作。

</details>

<details>
<summary>Abstract</summary>

Accurate scene understanding in confined, cluttered spaces such as shelves is essential for service robots, as many everyday tasks require them to locate and retrieve objects reliably. Yet, it remains challenging due to severe occlusions, restricted accessibility, and the need to avoid excessive scene changes. In this paper, we propose Multi-Skill Manipulation-Enhanced Mapping (MS-MEM), an evidential framework for uncertainty-aware mapping that integrates active viewpoint selection, object pushing, and grasping. MS-MEM combines scene-level metric-semantic evidential belief estimators with an uncertainty-aware grasp representation. This representation is learned using a novel full-evidential grasp estimator that models both grasp affordance and orientation uncertainty. In our framework, candidate perception and manipulation actions are evaluated within a unified action selection pipeline using a common information gain criterion. For manipulation actions, we further introduce a collateral disturbance constraint (CDC) that discourages excessive changes to confident regions of the scene belief. This enables MS-MEM to select actions that effectively reduce map uncertainty while limiting collateral scene changes. Experimental results show that, compared with single-skill and unconstrained baselines that ignore scene disturbance, MS-MEM achieves higher mapping accuracy while substantially reducing scene disturbance, highlighting the synergistic effects of active viewpoint selection, push, and grasp actions.

</details>

#### 2026-09-02 - Evidence-Guided Detection, Localization and Explanation for Text-Centric Image Forensics

**Authors:** Peifeng Liu, Bin Li, Qingsong Zhang, Yangxin Yu, Leqing Chen, Xiaoye Qiu
**Links:** [abs](https://arxiv.org/abs/2609.02097) - [pdf](https://arxiv.org/pdf/2609.02097)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evidence-Guided Detection, Localization and Explanation for Text-Centric Image Forensics（面向文本中心图像取证的证据引导检测、定位与解释）
- 作者：Peifeng Liu, Bin Li, Qingsong Zhang, Yangxin Yu, Leqing Chen, Xiaoye Qiu
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02097

### 一句话总结
本文提出一个“检测器-定位器-推理器”三模块级联的证据引导系统，在 ACM Multimedia 2026 的 GenText-Forensics 挑战赛中以 0.638 分获得第二名，用于文本中心图像的取证检测、篡改区域定位与可解释性报告生成。

### 研究问题
针对 AIGC 技术使文本中心图像篡改变得日益普及所带来的新取证挑战——不仅需要判断图像真伪（检测），还需要空间锚定篡改位置（定位），并基于证据给出可解释的说明（解释）。

### 核心思路/方法
- 构建三级系统：图像级检测器提供全局真实性先验；专用定位器提取篡改区域作为空间定位证据；基于 MLLM 的推理器依据专家取证证据生成结构化取证报告。
- 模块间通过级联证据流连接：检测器门控后续定位与提示过程；定位器将篡改响应转换为定位框；推理器训练融合检测决策与定位证据生成最终报告。
- 关键技术手段：引入迭代困难感知挖掘提升定位质量；采用报告-掩码一致性后处理，使报告定位结果与预测掩码对齐。

### 主要贡献
- 提出证据引导的检测-定位-推理取证系统框架，实现从全局判断到局部定位再到自然语言解释的完整取证链路。
- 设计级联证据流机制，使三个模块协同工作，检测结果门控下游任务，定位证据支撑解释生成。
- 引入迭代困难感知挖掘与报告-掩码一致性后处理，分别提升定位精度与报告与空间证据的一致性。
- 在官方隐藏测试集上取得 0.638 综合分并获得挑战赛第二名，验证系统有效性，并开源代码。

### 局限性
摘要未提供足够信息。摘要仅提及系统性能数据和模块设计，未报告失败案例、计算开销、泛化能力评估、数据集分布特征或与基线方法的详细对比等信息。

### 阅读优先级
**中**。理由：该文是挑战赛解决方案的技术报告，系统设计思路清晰（级联证据引导），对从事图像取证、AIGC 检测或多模态可解释推理方向的研究者有一定参考价值；但由于是竞赛技术方案，本质更偏工程集成而非方法论重大突破，且摘要未给出实验细节和深入分析，泛化学术参考价值有限。

</details>

<details>
<summary>Abstract</summary>

The rapid progress of AIGC has made text-centric image manipulation increasingly accessible, creating new forensic challenges that require not only authenticity detection but also spatial grounding and evidence-based explanation. This paper presents our solution to the GenText-Forensics Challenge at ACM Multimedia 2026. We propose an evidence-guided detector-localizer-reasoner system, where an image-level detector provides a global authenticity prior, a dedicated localizer extracts tampered regions as spatial grounding evidence, and an MLLM-based reasoner generates structured forensic reports grounded in this expert forensic evidence. These modules are connected through a cascaded evidence flow: the detector gates the subsequent localization and prompting process, the localizer converts tamper responses into grounding boxes, and the reasoner is trained to synthesize the detector decision and localized evidence into the final report. As a key part of our method, we introduce iterative difficulty-aware mining to improve localization quality and apply report-mask consistency post-processing to align report grounding with predicted masks. On the official hidden test set, our system achieves a final score of 0.638 and ranks second in the challenge, validating the effectiveness of the proposed evidence-guided system. The code is available at https://github.com/peifengLiu42/ACMMM26-evidence-guided-detector-localizer-reasoner-system.

</details>

#### 2026-09-01 - TAPVid-MV: A Benchmark for Tracking Any Point in 3D Across Multiple Views

**Authors:** Skanda Koppula, Frano Rajic, Abdullah Faiz Ur Rahman, Yi Yang, Ignacio Rocco, Jeet Thakwani, Rishabh Kabra, Andrew Zisserman, Joao Carreira, Siyu Tang, Carl Doersch, Gabriel Brostow
**Links:** [abs](https://arxiv.org/abs/2609.01899) - [pdf](https://arxiv.org/pdf/2609.01899)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, SfM, SLAM, robotics, autonomous driving, AR, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TAPVid-MV: A Benchmark for Tracking Any Point in 3D Across Multiple Views
- 作者：Skanda Koppula, Frano Rajic, Abdullah Faiz Ur Rahman, Yi Yang, Ignacio Rocco, Jeet Thakwani, Rishabh Kabra, Andrew Zisserman, Joao Carreira, Siyu Tang, Carl Doersch, Gabriel Brostow
- 出版日期：2026-09-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.01899

### 一句话总结
本文提出 TAPVid-MV，一个用于跨多个同步、移动相机视角下进行 3D 点跟踪的新基准，并发现现有方法在该任务上表现不佳，几何恢复是主要瓶颈。

### 研究问题
现有点跟踪基准仅针对单视频或静态多相机设置，缺乏对相机运动下、多同步视角中长期 3D 点跟踪的评估；因此需要一个专门的基准来测试和推动该方向的发展。

### 核心思路/方法
- 构建包含 284 个序列、1,142 个标定相机流和 109,769 条点轨迹的基准，覆盖室内外、机器人、人类活动、驾驶及合成程序化场景等 7 个子集。
- 通过数据集特有的辅助模态（如传感器深度、LiDAR、SLAM/SfM 点、人体网格、带姿态物体网格和仿真）获取轨迹，并由人类标注者进行视觉验证。
- 在同一数据集上联合评估重建与点跟踪，以区分几何恢复错误与点对应错误，并对比多视角与单目点跟踪器性能。

### 主要贡献
- 提出首个面向运动多相机设置下长期 3D 点跟踪的基准 TAPVid-MV。
- 提供大规模、经过人工验证的点轨迹标注，覆盖多种室内外场景。
- 通过 30 多个基线评估显示现有方法远未解决该任务，且多视角点跟踪器并未稳定优于单目点跟踪器。
- 通过联合分析指出几何恢复是准确 3D 点跟踪的主要瓶颈。
- 释放的标注还支持单目 2D/3D 点跟踪、未来轨迹预测和 4D 重建等下游任务。

### 局限性
摘要未提供足够信息（未说明基准在特定场景类型上的失败模式、对标注噪声的敏感性、评估指标的具体细节或计算开销等）。

### 阅读优先级
**高**。理由：该工作提出了一个全新且具有明确实际需求（机器人、AR/VR、自动驾驶）的基准，覆盖广泛场景并附有大规模人工验证数据；同时揭示了现有方法在该任务上的明显不足和关键瓶颈（几何恢复），对点跟踪、多视角重建及 3D 感知领域的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Multi-camera systems are increasingly practical for robotics, AR/VR, and autonomous driving because complementary views reduce depth ambiguity and preserve visibility under occlusion. Existing point-tracking benchmarks, however, focus on a single video or static multi-camera rigs. None test long-term 3D point tracking across several synchronized views under camera motion. We introduce TAPVid-MV (Tracking Any Point in Video across Multiple Views), the first benchmark for this setting. It contains a curated set of 284 sequences, 1,142 calibrated camera streams, and 109,769 point tracks across seven subsets spanning indoor and outdoor domains, from robotics and human activity to driving and synthetic procedural scenes. We obtain these trajectories using dataset-specific auxiliary modalities: sensor depth, LiDAR, SLAM and SfM points, human meshes, posed object meshes, and simulation. Every sequence and trajectory is visually verified by human annotators. Across more than 30 baselines, no method comes close to solving the task. Surprisingly, existing multi-view point trackers do not consistently outperform monocular point trackers. By evaluating reconstruction and point tracking on the same datasets, TAPVid-MV helps distinguish errors in recovered geometry from errors in point correspondence. Through this joint analysis, we identify geometry recovery as a major bottleneck for accurate 3D point tracking. Beyond multi-view 3D point tracking, our released annotations support monocular 2D and 3D point tracking, future-trajectory prediction, and 4D reconstruction.

</details>

#### 2026-09-01 - One Print, Many Moves: Monolithic Origami-inspired Folding Actuator for Composable Soft Multi-DoF Systems

**Authors:** Jaehyung Jang, Zhenish Zhakypov, Jasmin Elena Palmer, Melissa Klein, Jee-Hwan Ryu, Allison Mariko Okamura
**Links:** [abs](https://arxiv.org/abs/2609.00751) - [pdf](https://arxiv.org/pdf/2609.00751)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Print, Many Moves: Monolithic Origami-inspired Folding Actuator for Composable Soft Multi-DoF Systems
- 作者：Jaehyung Jang, Zhenish Zhakypov, Jasmin Elena Palmer, Melissa Klein, Jee-Hwan Ryu, Allison Mariko Okamura
- 出版日期：2026-09-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.00751

### 一句话总结
本文提出一种名为MONORIGAMI的单材料、单次3D打印、免装配的折纸启发式软体折叠致动器，通过空间编程的刚度各向异性，在保持柔顺性的同时实现精确、可组合的多自由度运动。

### 研究问题
传统软体机器人致动器虽具有良好的柔顺性，但其不可控变形导致精度不足，且难以扩展至多自由度系统。本文旨在解决如何在保持材料柔顺性的前提下，实现高精度、可扩展的软体多自由度驱动。

### 核心思路/方法
- 提出“空间编程的刚度各向异性”设计策略：沿期望折叠方向保持柔顺性，同时在非期望方向选择性限制变形。
- 基于材料厚度设计“刚度层级”，并按照折纸启发的几何结构（包含折面和折痕）进行图案化排布，从而将无约束的软体变形转化为精确、可重复的折叠运动。
- 整个设计只需单材料、单次3D打印，无需任何装配。
- 每个致动器作为可扩展的运动基元，通过链接和定向多个致动器即可机械编程多自由度轨迹。

### 主要贡献
1. 提出MONORIGAMI致动器设计范式，通过刚度各向异性和折纸几何在软体材料中实现空间编程变形控制。
2. 实现完全单材料、单次打印、免装配的制造流程，无需额外增强结构。
3. 基于同一基础模块展示了三个不同应用领域的3D打印软体多自由度系统：
   - 面向VR高保真皮肤反馈的紧凑型4自由度可穿戴触觉设备；
   - 用于遥操作动觉反馈的3自由度操纵杆；
   - 可水下作业、具有几何编码抓取轨迹的模块化机械爪。
4. 论证了该平台在紧凑多轴集成、受控物理交互和跨环境几何编程操作方面的通用性、可组合性、可访问性、可靠性和可扩展性。

### 局限性
摘要未提供足够信息，文中未明确讨论该致动器在负载能力、寿命、疲劳性能、控制复杂度或制造精度容差等方面的潜在局限性。

### 阅读优先级
**高**

理由：该工作提出了一种全新的软体致动器设计范式，解决了软体机器人向高精度多自由度系统扩展的长期难题，且实现了单次打印免装配的高可制造性。同时，论文在三个截然不同的实际领域（VR触觉、遥操作、水下抓取）中进行了系统级验证，具有较高的科学影响力和工程转化潜力，值得优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training
- 作者：Rongze Tang, Jianjie Fang, Zhaolu Wang, Ziyou Wang, Xvyuan Liu, Haisheng Su, Xin Zhang, Wei Wu, Chen Gao, Yong Li, Zhibo Chen
- 出版日期：2026-08-31
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.00161

### 一句话总结
本文提出IMPACT框架，通过将跨注意力作为内部时空先验来生成交互图并对去噪监督进行加权，从而在不依赖外部表示或推理时改动的情况下提升世界模型在交互生成中的物理合理性与视觉质量。

### 研究问题
世界模型在动作条件下未来预测中难以建模物理上合理的交互；现有方法依赖外部表示（如运动、几何、语义）约束生成，但这些表示获取成本高（需辅助估计器或人工标注），限制了训练的可扩展性。作者指出根本原因在于全局平均MSE去噪目标下存在监督分配失配问题——静态内容主导优化信号，动态交互区域被欠监督。

### 核心思路/方法
IMPACT的核心是识别MSE监督分配失配问题，并提出无需外部表示的解决方案：
1. 使用与操作对象token关联的交叉注意力作为动作条件变化的内部时空先验；
2. 从该先验中采样候选区域，并用分离的局部预测误差对候选区域进行校准，构建“交互图”；
3. 利用交互图对去噪监督进行重新加权，使稀疏的动态交互区域获得更充分的监督。
该方法无需外部表示，也不需要在推理时修改模型。

### 主要贡献
- 识别了全局平均MSE去噪目标下的监督分配失配问题，指出其是限制世界模型交互建模能力的根本原因之一；
- 提出IMPACT训练框架，利用内部交叉注意力先验与局部预测误差构建交互图以重新加权监督，免除了外部表示和人工标注的需求；
- 在机械臂与机械手操作任务上，跨越不同控制模态和DiT骨干网络，一致优于MSE训练的基线，在交互保真度、物理合理性、视觉质量上均有提升。

### 局限性
摘要未提供足够信息以判断该方法在非操作类交互场景、更大规模数据集、长时程预测等方面的泛化性能，也未讨论计算开销或失败案例。

### 阅读优先级
**高**。理由：该工作针对世界模型交互建模这一重要难题提出了无需外部标注的通用训练方案，核心思路（从监督分配失配切入并用内部注意力构建交互图）具有一定新颖性和可扩展性；实验覆盖多个任务与骨干网络，适合关注具身智能、世界模型与扩散模型训练的研究者阅读。

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
