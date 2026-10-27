# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：62
- 分类分布：
  - Neural Scene Representations & Rendering: 20
  - 3D Reconstruction & Multi-view Geometry: 15
  - Embodied / Robotics / AR Applications: 13
  - Geometry Foundation Models: 8
  - Dynamic / 4D Reconstruction: 6
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“前馈重建 + 测试时几何纠正”正在成为几何基础模型的新范式。**
   - VGGT 不确定性探针（2610.35806）指出前馈模型不报告位姿不确定性，但冻结特征中隐含失败信号；PosePlaner（2610.34845）进一步主张前馈模型把对应、几何、位姿“纠缠”在单次前向中，缺乏测试时用几何证据纠错的接口，因此引入基于 flow matching 的位姿精化器。两者共同反映：社区开始把前馈大模型视为“可被外部几何约束校正的模块”，而非端到端黑箱。
   - 配套的是对前馈流程的“事后几何推理”补强：Learning Scene Coordinate Reconstruction via PGO（2610.35501）用位姿图优化约束 ACE-Zero 的漂移；SG-Splat（2610.35361）在位姿不确定下解耦几何与高斯属性、并加入 flow-guided 位姿精化与可微 BA。

2. **4D/动态重建从“显式基元堆叠”转向“隐式先验 + 自适应时间参数化”。**
   - FL4N（2610.35854）明确抛弃显式 4D 高斯，改用“预训练静态隐式先验 + 动态残差”的前馈隐式 4D 表示，直指时序不一致与渲染伪影。
   - GaussianSpline（2610.35224）用逐高斯自适应非均匀 Bézier 样条替代全局形变/固定阶多项式，按区域分配时间容量；DimFlow（2610.34952）用网格-专家分支双向交互学习时空兼容特征。三者共同点：**不再用统一全局形变场，而是追求空间与时间上的局部自适应与平滑性约束（如 G¹ 连续性）**。

3. **生成先验与重建的耦合从“串联”走向“双向闭环/联合去噪”。**
   - GenSfM（2610.35522）批评“重建+生成”简单串联导致误差级联，改为在共享自注意力下联合去噪形状潜变量与逐视图位姿潜变量。
   - DUET4D（2610.35002）提出“自校正耦合引导”：用当前 4D 高斯表示反向引导生成先验，再用保真重采样把生成监督提升回高斯空间，抑制冗余基元与漂浮伪影。
   - 这标志生成模型在重建管线中的角色，从“补全缺失视角的后处理”变为“与表示共同迭代的监督源”。

4. **3DGS 正快速下沉为机器人与具身智能的数据基础设施。**
   - Robot-Aligned 3DGS（2610.35626）用 3DGS 重建真实工作空间并渲染机器人对齐的腕部相机观测，为 VLA 策略生成视觉-动作监督。
   - Zero-HLM（2610.35075）用 Gaussian-guided agentic real-to-sim 对齐视觉与物理场景；SceneAgent（2610.34745）把 3DGS/摄影测量/LiDAR/4D 视频统一转为可交互仿真环境；AuRA（2610.34452）自动化采集数字孪生数据。
   - 该簇的共同痛点是：**真实数据采集昂贵、数字孪生物理就绪难**，而 3DGS 被当作“视觉逼真但需物理化”的中间表示。

5. **评测与鲁棒性研究开始与表示方法同步推进，而非附属。**
   - PhysLadder（2610.34527）构建层级式 Sim-Real 匹配基准，揭示接触丰富操作中成功率随交互层级急剧下降（L3 为 0%）；VGGT 探针论文自建 HardMatch 基准；LP 数据集（2610.35018）为假肢视角深度估计建立首个系统基准。这表明社区在承认“方法进步需要可诊断的失败基准”。

#### 技术路线观察

**几何基础模型方向**
- 侧重从“更强前馈预测”转向“可诊断、可纠正”。VGGT 探针关注不确定性的可读出性（线性探针 ROC-AUC 93.5% vs 原生置信度 79.7%），PosePlaner 关注测试时用成对平面几何做条件生成式精化，二者形成“检测失败—纠正失败”的互补。
- 与经典 SfM 的关系被重新审视：PosePlaner 明确“复兴对应与位姿的经典耦合”，PGO 论文把全局多视图一致性约束重新引入学习式流程，说明纯前馈路线正在吸收经典几何优化的结构先验。

**3D/4D 重建方向**
- 静态重建侧：CVTSplat（2610.35347）探索自适应质心 Voronoi 剖分，强调单元规则性带来的 GPU 效率（构建快 5–10 倍）；这代表“表示离散化结构本身”仍是效率与质量的竞争点。
- 4D 重建侧：分成两条路线——(a) 前馈隐式路线（FL4N）；(b) 优化式高斯路线（GaussianSpline、DimFlow、DUET4D），但共同追求局部自适应时间建模与生成先验约束。
- 稀疏视角 4D 是明确的高欠约束场景，DUET4D 的“自校正耦合”是对“生成伪观测时间不一致 + 直接吸收导致漂浮物”这两个具体失效模式的针对性设计。

**神经场景表示方向**
- 3DGS 的改进从“渲染质量”扩展到“任务适配”：人体高斯泼溅（2610.35152）用局部熵复杂度先验约束高斯放置密度，解决复杂几何/纹理区域模糊；RIDE-Splat（2610.34632）处理挡风玻璃反射这一违反世界空间一致性的真实采集问题，用“场景透射 + 单张相机附着有符号反射图”分解，无需掩码或预训练网络。
- 表示与应用的边界模糊：3DGS 同时出现在重建、编辑（VidEdit3D，2610.35756）、机器人数据生成、仿真构建中。

**机器人/AR 应用方向**
- 技术侧重点从“策略学习算法”转向“数据管线与仿真就绪度”：Zero-HLM 的运动-环境协同适应、SceneAgent 的模拟器视觉检查与修复、AuRA 的执行感知抓取选择，都是在解决“如何低成本获得物理可信的交互数据”。
- 评测侧出现 Sim-Real 匹配设计（PhysLadder 共享任务定义与成功标准，16 个任务中 10 个在仿真与真实的成功计数完全一致），这为“仿真结论能否外推”提供了更严格的证据框架。
- 3D 编辑与视频扩散的结合（VidEdit3D）显示视频扩散模型的时空先验正被用于跨视角一致性约束，与 4D 重建中的生成先验使用形成方法上的呼应。

#### 值得优先阅读的论文

1. **PosePlaner（2610.34845）**
   理由：它提出了一个可插拔的通用机制——把位姿精化视为以粗匹配为条件的生成问题，并声称可在两视角数据上训练后用于 n 视角流式估计器的周期精化。如果成立，这是对前馈位姿预测器生态的“通用补丁”，影响面最广。

2. **GenSfM（2610.35522）**
   理由：直接挑战“重建与生成串联”的常见做法，用共享自注意力的联合去噪替代级联，并配套紧凑 3D 原生 UV-volume tokenization 以控制序列规模。这是生成式重建路线中方法论最完整的一篇。

3. **Does VGGT Know What It Does Not Know?（2610.35806）**
   理由：提供可操作的失败检测信号（线性探针）与自建困难基准，且验证了向 PhotoTourism、ScanNet-1500 的免重训迁移。对任何使用 VGGT 类模型做下游系统的人都直接相关。

4. **FL4N（2610.35854）**
   理由：作为“首个前馈隐式 4D NVS”，其“静态

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-27T13:58:35-04:00
**Total number of papers:** 62
**Number of papers added in the latest update:** 31
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

## Dynamic / 4D Reconstruction

### 2026-10

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
论文评估了仅依赖 Insta360 X5/X6 内置 1 kHz IMU 为双鱼眼 360 相机 SfM 恢复度量尺度的可行性，并与智能手机 ARKit/ARCore 位姿提供的尺度进行对比。

### 研究问题
消费级 360 度相机的双鱼眼视频经 SfM 只能恢复至相似变换，缺少度量尺度。现有流程依赖同期采集的智能手机 ARKit 或 ARCore 位姿提供尺度。本文关注：能否用相机内置 IMU 构成自包含的度量尺度来源，以及其精度与智能手机尺度相比如何。

### 核心思路/方法
- 对 Insta360 X5 与 X6 的内置 IMU（1 kHz）进行传感器表征，包括噪声密度、相机-IMU 同步、加速度计尺度因子、偏置稳定性。
- 从数据中估计相机-IMU 旋转与帧时间。
- 在整段测量的 SfM 位姿上，通过线性视觉-惯性对齐恢复尺度。
- 标准形式将重力与加速度计偏置设为整段共享，会产生尺度高估；改为对每个连续片段独立估计后平均，可去除该偏差。
- 摘要还提到对窗口构造的消融，以及与单目度量深度网络的比较。

### 主要贡献
- 提出并评估一种不依赖手机 AR 位姿、仅用相机内置 IMU 的自包含度量尺度方案。
- 给出该 IMU 的表征结果与相机-IMU 对齐方法。
- 发现并处理标准整段共享重力/偏置形式带来的约 3.4% 平均尺度高估，通过分段独立估计并平均消除偏差。
- 在九组与 LiDAR 共装的测量中，惯性尺度相对 LiDAR 的平均绝对误差为 0.74%，智能手机尺度为 1.94%；在打印基准标记上两者均在目标 1% 不确定度内一致。
- 在公开基准三十条参考轨迹（缩放至 1/40、1、40）上，尺度恢复平均误差 -0.07%，标准差 1.28%。
- 在五十组仅以智能手机为参考的生产测量中，两种尺度一致性的标准差为 2.6%，惯性尺度平均低 0.9%；差异不依赖窗口构造，随智能手机锚点范围增大而增大，且无法归因于任一参考。
- 补充了窗口构造消融和与单目度量深度网络的比较。

### 局限性
- 摘要未提供足够信息说明 IMU 表征的具体数值、测试环境条件及传感器长期稳定性细节。
- 摘要未提供足够信息说明公开基准的名称、序列内容及 1/40、1、40 缩放的具体构造方式。
- 摘要未提供足够信息说明五十组生产测量的采集条件、场景类型及智能手机锚点范围的具体定义。
- 摘要未提供足够信息说明与单目度量深度网络比较的具体网络、数据集与结果数值。
- 摘要仅指出两种尺度差异“无法归因于任一参考”，未提供足够信息确定误差来源。

### 阅读优先级
中。理由：该工作针对 360 相机 SfM 的度量尺度这一明确工程问题，给出了自包含 IMU 方案及多组与 LiDAR、基准标记、公开基准和手机参考的对比，对相关 3D 重建流程有直接参考价值；但摘要未展开具体实现细节与失败条件，是否高优先阅读取决于读者对 Insta360 生态或视觉-惯性尺度估计的具体需求。

</details>

<details>
<summary>Abstract</summary>

Structure-from-motion (SfM) from the dual-fisheye video of a consumer 360-degree camera recovers geometry only up to a similarity transform; in the pipeline considered here, metric scale is obtained from smartphone ARKit or ARCore poses captured alongside the camera. This paper evaluates a self-contained alternative: the IMU embedded in the Insta360 X5 and X6, recorded at 1 kHz. The sensor is characterised (noise density, camera-IMU synchronisation, accelerometer scale factor, bias stability), the camera-IMU rotation and frame timing are estimated from the data, and the scale is recovered by a linear visual-inertial alignment over the SfM poses of a whole survey. The standard formulation, with gravity and accelerometer bias shared across the survey, overestimates the scale by 3.4% on average; estimating each contiguous segment independently and averaging removes the bias. On nine surveys with a co-mounted LiDAR scanner the inertial scale deviates from the LiDAR by 0.74% in mean absolute error, against 1.94% for the smartphone scale; on printed fiducial markers both agree within the 1% uncertainty of the target. On the reference trajectories of thirty sequences of a public benchmark, brought to scales of 1/40, 1 and 40, the estimator recovers the metric scale with a mean error of -0.07% and a standard deviation of 1.28%. On fifty production surveys where the smartphone is the only reference, the two scales agree to a standard deviation of 2.6%, the inertial scale being 0.9% lower on average; the difference does not depend on window construction, grows with the extent of the smartphone anchor, and cannot be attributed to either reference. An ablation over window construction and a comparison with monocular metric-depth networks complete the study.

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

## Neural Scene Representations & Rendering

### 2026-10

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

#### 2026-10-21 - TerraTransfer++: Demonstration-Free End-to-End Planner

**Authors:** Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan
**Links:** [abs](https://arxiv.org/abs/2610.30319) - [pdf](https://arxiv.org/pdf/2610.30319)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TerraTransfer++: Demonstration-Free End-to-End Planner
- 作者：Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan
- 出版日期：2026-10-21T18:31:28Z
- 分类：主分类为 Neural Scene Representations & Rendering；无次级分类
- 链接：摘要页 https://arxiv.org/abs/2610.30319 ；PDF https://arxiv.org/pdf/2610.30319

### 一句话总结
论文提出一种不依赖人工专家演示的端到端自动驾驶训练框架：先在向量化仿真器中通过自博弈预训练策略，再将其蒸馏为流匹配轨迹教师，并在冻结视觉主干上训练轻量适配器，得到闭环策略与规划器两个学生模型。

### 研究问题
端到端自动驾驶的标准训练范式成本高昂：模仿学习依赖车队规模驾驶日志，且行为分布对安全关键长尾覆盖稀薄；照片级仿真器中的闭环强化学习受样本效率、逐步渲染成本和大型视觉主干前向计算限制。论文关注能否在不使用人工专家演示、也不依赖日志轨迹监督对齐的情况下，获得具备自然多样行为与高反应性的端到端策略与规划器。

### 核心思路/方法
论文利用向量化仿真器自博弈的效率优势：在每秒数百万 rollout 步的规模下，获得包含碰撞、近失误与恢复等自然多样性的状态分布，并由基础驾驶质量奖励产生高反应性策略。方法分三步：
1. 通过自博弈预训练单一策略；
2. 将其 rollout 蒸馏为同时具备规划能力的流匹配轨迹教师；
3. 在冻结的预训练视觉主干上训练轻量适配器，通过动作 KL 散度、批关系低秩结构损失，以及面向规划器的轨迹匹配损失，复现教师的潜空间。
所有监督目标均回溯到自博弈策略，因此对齐过程从不以日志轨迹为监督；仅需成对的（图像、场景状态）帧数据集，无需整理好的专家演示。由同一自博弈教师得到两个端到端学生：闭环策略与规划器。

### 主要贡献
- 提出无演示的端到端训练路线，避免模仿学习对车队规模驾驶日志与专家演示的依赖，也规避照片级仿真器闭环强化学习的样本效率与渲染成本瓶颈。
- 设计从自博弈策略到流匹配轨迹教师的蒸馏流程，并在冻结视觉主干上以多种损失训练轻量适配器，实现潜空间对齐。
- 从单一自博弈教师产出两个学生模型：闭环策略在照片级 3D Gaussian splatting 闭环基准 HUGSim 上优于所有已发表的基于模仿的端到端方法；规划器在 NAVSIM navhard 上达到 59.4 EPDMS，高于包括 DriveZero-Scale（57.1）在内的所有已发表方法，在 navtest 上达到 95.5 PDMS，且不使用人类演示。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、计算开销、跨场景泛化边界、安全保证或消融实验细节。摘要未提供足够信息说明自博弈奖励设计细节、教师蒸馏的稳定性条件，以及在不同传感器配置或真实部署中的表现。

### 阅读优先级
高。理由：论文直接针对端到端自动驾驶训练成本与专家演示依赖这一核心瓶颈，给出无需人工演示的统一训练框架，并在 HUGSim、NAVSIM navhard 与 navtest 上报告了优于已发表方法的定量结果；若关注端到端规划、自博弈仿真训练或教师-学生蒸馏，该工作具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all existing paradigms: imitation learning requires fleet-scale driving logs whose behavior distribution only thinly covers the safety-critical tail; closed-loop reinforcement learning in a photorealistic simulator, while offering diverse behaviors, is bottlenecked by sample-efficiency, per-step cost of rendering, and a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: at millions of rollout steps per second, one can obtain a state distribution with natural diversity in collisions, near-misses, and recoveries that no driving log contains, and a highly reactive policy emerges from a basic driving-quality reward. Our approach exploits this asymmetry. We pretrain a single policy by self-play, distill its rollouts into a flow-matching trajectory teacher that also plans, and train lightweight adapters on a frozen pretrained vision backbone to reproduce the latent space of either teacher through the action KL divergence, a batch-relational low-rank structural loss, and, for the planner, a trajectory-matching loss. Every target traces back to the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. From this one self-play teacher we obtain two end-to-end students: a closed-loop policy that outperforms every published imitation-based end-to-end method on the photorealistic 3D Gaussian splatting closed-loop benchmark HUGSim, and a planner that reaches 59.4 EPDMS on NAVSIM navhard, above every published method including DriveZero-Scale (57.1), and 95.5 PDMS on navtest, without human demonstrations.

</details>

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

## Embodied / Robotics / AR Applications

### 2026-10

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
- 分类：主分类 Embodied / Robotics / AR Applications；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.29845 ；PDF https://arxiv.org/pdf/2610.29845 ；项目网站 https://rangenav.github.io/

### 一句话总结
RangeNav 提出一个仅 183k 参数、完全用合成数据预训练的 LiDAR range-image 编码器，通过导航对齐的多任务预训练后冻结用于策略学习，并在仿真与真实四足机器人上验证导航表现。

### 研究问题
论文针对密集人群与杂乱场地中移动机器人需要 360° 感知的问题，指出全景 LiDAR 虽能全覆盖，但在稀疏奖励下用强化学习直接学习表示样本效率低，而现有 3D 预训练点云编码器对大规模并行 RL 仿真而言内存开销过大。因此需要一种紧凑、适合并行仿真且能提供有效感知表示的方案。

### 核心思路/方法
- 采用 LiDAR range-image 作为输入形式，构建紧凑编码器（183k 参数），完全在合成数据上预训练。
- 针对 range image 的极端长宽比与方位角接缝，使用各向异性卷积和循环填充。
- 预训练目标为导航对齐的多任务组合：range reconstruction、semantic segmentation 与 bird's-eye-view (BEV) prediction。
- 预训练完成后冻结编码器，用于后续策略学习。

### 主要贡献
- 提出紧凑的 LiDAR range-image 编码器 RangeNav，参数量仅 183k，预训练完全基于合成数据，面向大规模并行 RL 仿真的内存约束。
- 设计适配 range image 极端长宽比与方位角接缝的网络结构（各向异性卷积、循环填充）。
- 提出导航对齐的预训练目标，联合 range reconstruction、semantic segmentation 与 BEV prediction。
- 仿真结果显示，相较仅重建基线，加入语义与 BEV 监督在程序化生成的训练环境和分布外真实感测试环境中分别平均提升成功率 32.03 与 23.73 个百分点。
- 在 Unitree B2-W 四足机器人上进行零样本真实部署，摘要称其在密集人群、低光环境和施工区域中表现稳健，而有限视场深度策略在这些场景中表现困难。

### 局限性
- 摘要未提供足够信息说明预训练数据规模、合成数据来源与多样性。
- 摘要未提供足够信息说明真实世界实验的定量指标、试验次数与统计显著性。
- 摘要未提供足够信息说明与更多基线方法的系统对比。
- 摘要未提供足够信息说明编码器冻结后策略学习的具体算法与训练成本。
- 摘要未提供足够信息说明失败案例与安全性分析。

### 阅读优先级
高。理由：论文聚焦机器人导航中全景 LiDAR 感知与 RL 样本效率/内存瓶颈的实际问题，方法紧凑且给出仿真提升幅度与真实四足机器人零样本部署结果，并承诺开源代码与模型；对具身智能、机器人导航与 LiDAR 表示学习方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous mobile robots operating in dense crowds and cluttered sites require $360^\circ$ perception to react to surrounding hazards. While panoramic LiDAR offers full-surround coverage, learning representations within reinforcement learning (RL) is sample-inefficient under sparse rewards, and existing 3D pretrained point-cloud encoders are too memory-heavy for massively parallel RL simulation. We present RangeNav, a compact (183k parameters) LiDAR range-image encoder pretrained entirely on synthetic data. RangeNav uses anisotropic convolutions and circular padding to handle the extreme aspect ratio and azimuthal seam of range images. We pretrain the network using a navigation-aligned objective combining range reconstruction, semantic segmentation, and bird's-eye-view (BEV) prediction, then freeze it for policy learning. In simulation, adding semantic and BEV supervision increases success rates over a reconstruction-only baseline by an average of 32.03 and 23.73 percentage points (pp) in procedurally generated training and out-of-distribution realistic test environments, respectively. Zero-shot real-world deployments on a Unitree B2-W quadruped demonstrate robust navigation through dense crowds, low-light settings, and construction zones where limited-field-of-view depth policies struggle. Code and models will be open-sourced. Project website: https://rangenav.github.io/.

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
