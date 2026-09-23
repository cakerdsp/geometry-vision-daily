# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：73
- 分类分布：
  - Embodied / Robotics / AR Applications: 27
  - Neural Scene Representations & Rendering: 21
  - 3D Reconstruction & Multi-view Geometry: 15
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **前馈式几何基础模型从“能不能做”转向“可靠性与效率”**  
   本批论文中，VGGT-Prime（2609.23733）从架构冗余角度加速视觉几何 Transformer；When Wider Views Fail（2609.24839）系统压力测试前馈重建在大视角跨度下的失效模式；Revisiting Multi-View Stereo（2609.24850）则把 MVS 重构成序列到序列并显式注入相机先验。三者共同表明：几何基础模型的研究重心正从精度竞赛转向**可部署性、效率与分布外鲁棒性**。

2. **不确定性建模开始贯穿 SLAM 与建图全流程**  
   BayesianGS-SLAM（2609.24140）将颜色与深度预测不确定性同时用于建图、位姿优化和关键帧选择；When Wider Views Fail（2609.24839）关注模型在分布偏移下的不可靠几何；D-JEPA（2609.24749）指出预测精度与决策成功之间的“决策局部预测差距”。这反映出一个趋势：**不确定性不再只是后处理工具，而是被显式纳入优化目标和决策接口**。

3. **物理约束与力反馈成为具身操作的核心接口**  
   Opt2VLA（2609.23968）在 VLA 与控制接口中显式引入连续接触力指令；Imagine-RL（2609.24033）用视觉-力矩潜世界模型预测未来接触后果；InsertAnything（2609.24511）依赖三维指尖力反馈实现精密插入；FinsSim（2609.23943）则构建标定的推进器-水动力学模型。这些工作共同指向：**接触丰富任务中，纯几何/视觉目标已不够，力与动力学反馈正在被提升为一等公民**。

4. **世界模型从“预测未来”走向“辅助决策与探索”**  
   D-JEPA（2609.24749）学习决策对齐的潜在世界模型；WOLF（2609.23656）用循环世界模型预测 LiDAR 局部占据与可见性以生成预测前沿；NeuIDO（2609.24313）将世界建模形式化为神经算子学习。三者分别从**决策对齐、主动探索、物理内化**三条路径推进世界模型，说明该方向正在从生成式预测转向决策与感知的闭环服务。

5. **4D/动态神经表示向多模态与语义自适应演进**  
   Dynamic Thermal Gaussians（2609.24531）首次联合建模动态 RGB-热成像；SAMIRA（2609.24158）按面部语义区域分别建模运动与光照响应；两者均反对全局耦合的统一响应模型。这表明 4D 重建的下一阶段竞争点在于**模态一致性与语义粒度**，而非单纯提升单模态渲染保真度。

#### 技术路线观察

- **几何基础模型**：VGGT-Prime 关注架构冗余与计算自适应，When Wider Views Fail 关注分布偏移下的失效边界，Revisiting MVS 关注已知相机参数下如何注入相机先验。三者侧重点不同，但共同默认前馈模型已成为主流基线，问题已转向效率、鲁棒性和几何先验的显式利用。
- **3D/4D 重建**：Revisiting MVS 和 VGGT-Prime 代表前馈重建路线；Dynamic Thermal Gaussians 和 SAMIRA 代表基于高斯的动态/可重光照重建路线；OpenFlyScan 则把重建质量预测与主动补采结合，代表**重建即服务**的系统化路线。CMambaDepth 用 Channel Mamba 与混合注意力处理自监督单目深度，属于效率与跨尺度建模路线。
- **神经场景表示与渲染**：BayesianGS-SLAM 把概率不确定性引入 3DGS SLAM；Dynamic Thermal Gaussians 把热模态锚定到共享几何基底；SAMIRA 把光照响应按语义解耦。三者共同趋势是**表示不再追求单一统一模型，而是按模态、语义或不确定性分解**。
- **机器人/AR 应用**：Opt2VLA、Imagine-RL、InsertAnything 分别从力接口、世界模型增强评论家、仿真到现实强化学习三条路线解决接触密集操作；WOLF 和 FinsSim 分别面向无人机探索与水下机器人仿真。整体看，应用层论文越来越强调**训练与部署的一致性**（仿真到现实、潜空间到真实执行），而非仅追求仿真指标。

#### 值得优先阅读的论文

1. **When Wider Views Fail（2609.24839）**  
   理由：这是本批中少见的系统性失效分析工作，直接挑战前馈重建“越宽越好”的隐含假设。对任何计划部署前馈几何模型的研究者，理解其失效边界比追求新 SOTA 更紧迫。

2. **BayesianGS-SLAM（2609.24140）**  
   理由：把不确定性同时用于建图、跟踪和关键帧选择，是 3DGS SLAM 中较完整的概率化尝试。其“预测不确定性复用”思路可能迁移到其他神经渲染优化管线。

3. **D-JEPA（2609.24749）**  
   理由：明确指出“预测准确不等于决策正确”这一被广泛忽视的问题，并提出决策对齐的潜在世界模型。对具身智能和世界模型方向的研究者，这是一个值得跟进的框架性视角。

4. **Revisiting Multi-View Stereo（2609.24850）**  
   理由：在已知相机参数下重新审视 MVS，把传统 MVS 与前馈模型桥接，序列到序列的表述和光线图嵌入可能成为后续 MVS 工作的新基线。

5. **Opt2VLA（2609.23968）**  
   理由：在人形机器人全身操作中显式引入连续力指令，直面接触后视觉不可靠的问题。若关注 VLA 与力控结合，这是本批中最具接口设计参考价值的工作。

#### 可能的研究机会

- **不确定性驱动的主动重建与探索**：BayesianGS-SLAM 的不确定性估计与 OpenFlyScan 的质量引导补采、WOLF 的预测前沿可以组合。即：用 SLAM/重建的不确定性直接驱动下一最佳视角或补采航带，形成感知-决策闭环。
- **决策对齐的世界模型与力反馈结合**：D-JEPA 的决策对齐机制若与 Imagine-RL 的视觉-力矩潜世界模型结合，可能产生既能预测接触后果、又能按决策成功性排序候选动作的力感知世界模型。
- **前馈重建的效率-鲁棒性联合优化**：VGGT-Prime 的架构冗余削减与 When Wider Views Fail 揭示的视角跨度失效可以联合研究：是否存在既计算自适应、又对视角分布偏移鲁棒的注意力分配策略。
- **多模态 4D 重建中的语义自适应分解**：Dynamic Thermal Gaussians 的共享几何基底与 SAMIRA 的语义自适应响应可以结合，探索热-可见光-光照-运动四类响应按语义区域解耦的通用 4D 表示。
- **水下/特种场景的 Sim-to-Real 与几何基础模型结合**：FinsSim 提供了水下仿真与标定动力学，Range-Aided SLAM 提供了高精度航向下初始化。两者结合可能催生水下几何基础模型的评测与迁移研究。

#### 风险和不确定性

- 本分析仅基于论文摘要与已有简析，未阅读全文。VGGT-Prime 的具体路由器设计、加速比与精度损失；When Wider Views Fail 的具体模型、数据集与定量退化曲线；D-JEPA 的算子细节与实验规模；Opt2VLA 的力指令表示与控制器接口——均需全文验证。
- Dynamic Thermal Gaussians 的“首个动态 RGB-热重建框架”与“新基准数据集”声明需核对全文与数据可用性；SAMIRA 的语义自适应模块在极端表情或光照下的表现需实验验证。
- Range-Aided SLAM 与 OpenFlyScan 的实机/实飞结果、FinsSim 的 Sim-to-Real 定量迁移效果，摘要未给出完整指标，结论应保守。
- 本批论文时间集中在 2026-09-20 至 2026-09-21，样本量有限，所归纳趋势可能受

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-23T12:54:32-04:00
**Total number of papers:** 73
**Number of papers added in the latest update:** 20
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

#### 2026-09-21 - SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation

**Authors:** Jiangshan Gong, Yuqun Wu, Qiqian Fu, Yao Xiao, Chuhang Zou, Shenlong Wang, Derek Hoiem
**Links:** [abs](https://arxiv.org/abs/2609.25490) - [pdf](https://arxiv.org/pdf/2609.25490)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, 3D reconstruction, robotics

<details>
<summary>Abstract</summary>

Consistent multi-view object segmentation is critical for 3D perception and robotics, yet remains challenging under severe viewpoint and occlusion changes. Existing methods typically perform 3D instance segmentation on point clouds or rely on offline 2D mask-matching pipelines. However, 3D instance segmentation is limited by scarce 3D annotations, while offline 2D matching suffers from object identity ambiguity across frames. To leverage strong 2D and 3D priors jointly, we propose SAM-V (Geometry-Aware Segment Anything for Multi-View Instance Segmentation). Instead of combining the two priors through post-hoc matching, SAM-V directly integrates features from a feed-forward geometry model (VGGT) into a 2D segmentation foundation model (SAM), trained end-to-end for cross-view instance prediction. SAM-V introduces a prompt-fusion mechanism that enriches sparse SAM prompt tokens with view-specific camera tokens and local VGGT features, making the prompt representation both view-aware and spatially grounded, together with a mask decoder that attends to dense 2D and 3D features. By conditioning the mask decoding directly on multi-view geometry, SAM-V produces consistent multi-view segmentation of a prompted object in a single forward pass without offline mask matching or explicit 3D reconstruction. On the IGGT 3D tracking benchmark, where consistent instance identity across frames directly determines performance, SAM-V improves overall IoU by 5 points and frame-level recall by 12 points on the ScanNet++ split over the state-of-the-art multi-view instance segmentation baseline and leads on all metrics in the zero-shot ScanNet split. Our code and pretrained models are available at https://github.com/gong208/SAM-V.git.

</details>

#### 2026-09-21 - When Wider Views Fail: Stress-Testing Feed-Forward 3D Reconstruction

**Authors:** Daisy Li, Kyle Gao, Quanyun Wu, Hanna Chomko, John S. Zelek, Jonathan Li
**Links:** [abs](https://arxiv.org/abs/2609.24839) - [pdf](https://arxiv.org/pdf/2609.24839)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward reconstruction, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：When Wider Views Fail: Stress-Testing Feed-Forward 3D Reconstruction
- 作者：Daisy Li, Kyle Gao, Quanyun Wu, Hanna Chomko, John S. Zelek, Jonathan Li
- 出版日期：2026-09-21T16:20:14Z
- 分类：主类 Geometry Foundation Models；次类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.24839) / [PDF](https://arxiv.org/pdf/2609.24839)

### 一句话总结
论文通过控制输入图像的视角跨度、保持输入数量不变，压力测试前馈式三维重建模型在视角分布偏移下的失效模式。

### 研究问题
前馈式三维重建模型能从稀疏图像高效估计几何，但其预训练特性使其可能在训练数据之外的分布偏移下变得脆弱。论文关注的问题是：在非受限成像场景中，这类模型何时可能不可靠；具体而言，视角变化作为一种受控的分布偏移，会如何影响前馈式重建模型的表现。

### 核心思路/方法
论文将视角变化设计为一种受控的分布偏移：在保持输入图像预算固定的情况下，改变稀疏输入图像的角跨度。作者在多个前馈式重建模型上进行观察，分析随着视角跨度增加时模型表现的变化。

### 主要贡献
- 将视角变化作为受控分布偏移，用于压力测试前馈式三维重建模型。
- 在多个前馈式重建模型上观察到：随着视角跨度增大，性能出现显著退化。
- 指出大视角跨度不仅导致表面覆盖不完整，还会产生不被观测图像支持的几何。
- 表明视角变化会引发超出传统“重建不完整”范畴的失效模式，并强调需要在挑战模型所学几何先验的分布偏移下评估预训练前馈模型。

### 局限性
摘要未提供足够信息说明具体使用了哪些模型、数据集、评价指标、实验数量或定量结果；也未提供关于失败模式的具体可视化、误差来源拆解或改进方法的细节。因此，无法基于给定摘要判断方法的适用范围边界、计算成本或与其他压力测试设置的比较。

### 阅读优先级
高。理由：该论文聚焦前馈式三维重建模型在分布偏移下的可靠性问题，主题与 Geometry Foundation Models 和 3D Reconstruction & Multi-view Geometry 直接相关；其“固定输入预算、改变视角跨度”的压力测试设定清晰，且指出大视角跨度会带来不完全覆盖与不被观测支持的几何，这对评估和部署此类模型具有重要警示意义。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models enable efficient geometry estimation from sparse images, but their pretrained nature can make them vulnerable to distribution shifts beyond their training data. Identifying these failure modes is important for understanding when such models can be reliably deployed in unconstrained imaging settings. We investigate viewpoint variation as a controlled distribution shift by varying the angular span of sparse image inputs while keeping the input budget fixed. Across multiple feed-forward reconstruction models, we observe substantial degradation as viewpoint span increases, with wide spans producing both incomplete surface coverage and geometry unsupported by the observed imagery. These results reveal that viewpoint variation can induce failure modes beyond conventional reconstruction incompleteness, highlighting the need to evaluate pretrained feed-forward models under distribution shifts that challenge their learned geometric priors.

</details>

#### 2026-09-20 - VGGT-Prime: Compute-Adaptive Mixture-of-Heads for Efficient Visual Geometry Transformers

**Authors:** Abteen Arab, Guile Wu, Chengjie Huang, Dongfeng Bai
**Links:** [abs](https://arxiv.org/abs/2609.23733) - [pdf](https://arxiv.org/pdf/2609.23733)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** visual geometry grounded transformer, VGGT, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VGGT-Prime: Compute-Adaptive Mixture-of-Heads for Efficient Visual Geometry Transformers
- 作者：Abteen Arab, Guile Wu, Chengjie Huang, Dongfeng Bai
- 出版日期：2026-09-20T16:22:15Z
- 分类：Geometry Foundation Models（二级分类：摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2609.23733) / [PDF](https://arxiv.org/pdf/2609.23733)

### 一句话总结
VGGT-Prime 从架构冗余的角度出发，通过轻量路由器为每个全局注意力头动态分配不同计算模式，在保持重建质量的同时显著加速视觉几何 Transformer。

### 研究问题
前馈式视觉几何模型（如 VGGT）能够从多视角图像直接进行三维重建，但其全局注意力机制导致计算量随输入视角数量呈二次方增长，长序列输入时延迟显著。现有加速工作主要集中于通过 token 合并或 key/value 稀疏化来减少 **token 冗余**，本文则转向研究视觉几何 Transformer 中的 **架构冗余** 问题。

### 核心思路/方法
- 论文指出 VGGT 全局注意力层中的多头注意力模块存在显著的架构冗余，只有一部分注意力头携带关键几何信息。
- 基于这一观察，提出 VGGT-Prime，一种 **计算自适应混合头（compute-adaptive mixture-of-heads）** 模型。
- 核心做法：使用轻量路由器估计每个全局注意力头所需的计算水平，然后将各注意力头动态分配到不同的计算模式，从而消除冗余、加速推理，同时维持有竞争力的重建质量。

### 主要贡献
- 从架构冗余（而非 token 冗余）的新视角解决视觉几何 Transformer 的效率瓶颈。
- 提出 VGGT-Prime，通过轻量路由器驱动的计算自适应混合头机制实现加速。
- 在多个数据集上的实验表明，VGGT-Prime 相比 VGGT 可实现 **8× 推理加速**，同时在相机位姿、深度和点云预测上保持有竞争力的性能。
- 进一步表明该方法与现有加速方法（如 token 合并）互补，结合后相对 VGGT 可提升推理速度最高达 **14×**。

### 局限性
- 摘要未提供足够信息说明其在不同规模数据集或极端视角数量下的具体泛化表现。
- 摘要未提供足够信息说明路由器的训练开销、额外参数引入量或端到端训练成本。
- 摘要未提供足够信息说明方法在低计算模式下的精度损失边界或失效场景。
- 摘要未提供足够信息说明其与 token 合并结合时的具体实现细节与兼容性约束。

### 阅读优先级
**高**。该工作针对视觉几何基础模型中全局注意力二次复杂度这一核心瓶颈，提出了与主流 token 冗余路线不同的架构冗余视角，且报告了 8×–14× 的显著加速与竞争性精度，对 3D 重建、多视角几何与高效 Transformer 方向均有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward visual geometry models such as the Visual Geometry Grounded Transformer (VGGT) have recently enabled direct 3D reconstruction from multi-view images. Despite their promising performance, these models scale quadratically with the number of input views due to their global attention mechanism, resulting in substantial latency for long sequence inputs. There have been some recent efforts to accelerate VGGT, but they primarily focus on reducing \emph{token redundancy} through token merging or key/value sparsification. Our work resolves this bottleneck from a different perspective by investigating \emph{architectural redundancy} in visual geometry transformers. We show that the multi-head attention modules in VGGT's global-attention layers contain substantial architectural redundancy, with only a subset of heads carrying critical geometric information. In light of this observation, we propose VGGT-Prime, a compute-adaptive mixture-of-heads model that resolves this redundancy to accelerate visual geometry transformers while maintaining competitive reconstruction quality. The key idea of VGGT-Prime is to estimate the appropriate computation level for each global-attention head using a lightweight router and then dynamically assign each head to different computation modes. Extensive experiments on multiple datasets demonstrate that VGGT-Prime can achieve an {$8\times$} inference speedup over VGGT while maintaining competitive performance on camera pose, depth, and point-cloud predictions. We further show that VGGT-Prime is complementary to existing acceleration methods, such as token merging, further improving inference speed by up to $14{\times}$ over VGGT. An overview of our work is available on our \href{https://vggt-prime.github.io}{project page}.

</details>

#### 2026-09-17 - GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction

**Authors:** Enpeng Li, Yunzhou Zhang, Zhiyao Zhang, Dexuan Lyu, Chenyu Wang, Chiyuan Cui, Cheng Cheng
**Links:** [abs](https://arxiv.org/abs/2609.20012) - [pdf](https://arxiv.org/pdf/2609.20012)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward reconstruction, feed-forward 3D reconstruction, 3D reconstruction, SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction
- 作者：Enpeng Li, Yunzhou Zhang, Zhiyao Zhang, Dexuan Lyu, Chenyu Wang, Chiyuan Cui, Cheng Cheng
- 出版日期：2026-09-17T10:21:52Z
- 分类：Geometry Foundation Models（主类）；3D Reconstruction & Multi-view Geometry（次类）
- 链接：[摘要](https://arxiv.org/abs/2609.20012) | [PDF](https://arxiv.org/pdf/2609.20012)

### 一句话总结
本文提出 GRF-Recon，一个面向长单目序列的馈送式 3D 重建统一框架，通过粗到细轨迹对齐、几何先验注入与混合权重稀疏射线场优化，在保持可扩展性的同时提升全局一致性与轨迹精度。

### 研究问题
摘要指出，馈送式 3D 重建虽能高效建模，但在扩展到大规模单目场景时面临三重约束：GPU 显存占用过大、局部几何退化、长期轨迹漂移。现有基于分块（chunk-based）的优化策略几何约束有限，难以在长轨迹上维持全局一致性。

### 核心思路/方法
- 构建粗到细的轨迹对齐流程，并辅以轻量级几何先验注入。
- 通过 LoRA 适配将单目几何线索蒸馏进馈送式主干，在保持推理效率的同时提升精细结构上的深度精度。
- 提出混合权重稀疏射线场优化，利用高频几何特征引导局部点云精化，并施加一致的帧间射线约束；与既有分块方法相比，建立强跨帧几何耦合且保持可扩展性。
- 采用带联合射线误差优化的高效轨迹拼接策略，显式减少累积漂移。

### 主要贡献
- 提出面向长单目序列的稳定、可扩展馈送式 3D 重建统一框架。
- 将单目几何先验以 LoRA 方式蒸馏进馈送式主干，兼顾精细结构深度精度与推理效率。
- 设计混合权重稀疏射线场优化，实现跨帧几何耦合下的局部点云精化。
- 提出联合射线误差优化的轨迹拼接策略以抑制长期漂移。
- 摘要称实验表明其轨迹精度可与代表性 SLAM 系统竞争，并在大规模场景中保持全局一致的 3D 重建。

### 局限性
- 摘要未提供足够信息说明具体实验数据集、评测指标数值、与 SLAM 系统对比的详细结果。
- 摘要未提供足够信息说明方法的计算开销、实时性、显存占用的量化结果。
- 摘要未提供足够信息说明在极端场景（如剧烈运动、弱纹理、动态物体）下的表现。
- 摘要未提供足够信息说明 LoRA 适配、射线场优化中各超参数的影响与消融结果。

### 阅读优先级
中。理由：该工作针对长序列馈送式重建的显存、局部几何与轨迹漂移等明确痛点，方法组合（几何先验蒸馏 + 稀疏射线场 + 轨迹拼接）具有一定新意，且主类为 Geometry Foundation Models，与 3D 重建方向相关度高；但摘要未给出量化实验细节与开源信息，若关注具体性能提升幅度或工程落地，需进一步阅读全文验证。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction provides an efficient paradigm for scene modeling from image sequences. Scaling these models to large monocular scenarios are constrained by excessive GPU memory footprint, degraded local geometry, and long-term trajectory drift. Existing chunk-based optimization strategies provide limited geometric constraints and fail to maintain global consistency over extended trajectories. We present a unified framework for stable and scalable feed-forward 3D reconstruction from long monocular sequences. Our approach builds on coarse-to-fine trajectory alignment augmented by lightweight geometric prior injection. Distilling monocular geometric cues into the feed-forward backbone via LoRA adaptation improves depth accuracy on fine structures while preserving inference efficiency. We introduce a hybrid-weight sparse ray-field optimization that leverages high-frequency geometric features to guide local point-cloud refinement and enforce consistent inter-frame ray constraints. Unlike prior chunk-based methods, this establishes strong cross-frame geometric coupling while maintaining scalability. Finally, an efficient trajectory stitching strategy with joint ray-error optimization explicitly reduces accumulated drift. Extensive experiments show that our approach achieves competitive trajectory accuracy compared with representative SLAM systems, while maintaining globally consistent 3D reconstruction in large-scale scenarios.

</details>

#### 2026-09-17 - VGGT-GS SLAM: Uncalibrated Monocular Gaussian Splatting SLAM with Feed-Forward Priors

**Authors:** Yuhang Han, Hao Wang, Jiaxi Cao, Xingyu Liu
**Links:** [abs](https://arxiv.org/abs/2609.19628) - [pdf](https://arxiv.org/pdf/2609.19628)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** VGGT, SLAM, bundle adjustment, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VGGT-GS SLAM: Uncalibrated Monocular Gaussian Splatting SLAM with Feed-Forward Priors
- 作者：Yuhang Han, Hao Wang, Jiaxi Cao, Xingyu Liu
- 出版日期：2026-09-17T03:18:23Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry、Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.19628) / [PDF](https://arxiv.org/pdf/2609.19628)

### 一句话总结
论文提出 VGGT-GS SLAM，一个面向未标定单目视频的 3D Gaussian Splatting SLAM 系统，借助前馈 VGGT 位姿与深度先验，联合优化相机参数、位姿与三维高斯地图。

### 研究问题
摘要指出，该工作针对的是**未标定视频（uncalibrated videos）**下的单目 3D Gaussian Splatting SLAM 问题。其关注点包括：在缺少标定信息的情况下进行定位与建图，并在未标定设置下提升定位精度与渲染质量。摘要未提供足够信息说明其具体应对的失败模式、评价指标细节或与既有方法的定量差距。

### 核心思路/方法
- 以**前馈 VGGT 位姿与深度先验**作为起点。
- 执行**子图可微 bundle adjustment**，联合精化相机位姿与 3D Gaussian 地图。
- 通过**解析标定雅可比**优化子图共享的内参以及径向—切向畸变。
- 引入 **Gaussian-native alignment（GNA）**，用于序列子图之间以相机为锚的尺度精化，并用于回环候选的验证，以提升全局一致性。

### 主要贡献
- 提出 VGGT-GS SLAM，一个面向未标定视频的单目 3D Gaussian Splatting SLAM 系统。
- 将前馈 VGGT 位姿与深度先验引入子图可微 bundle adjustment，联合优化相机位姿与 3D Gaussian 地图。
- 通过解析标定雅可比在优化中处理子图共享内参与径向—切向畸变。
- 提出 Gaussian-native alignment（GNA），用于子图间相机锚定尺度精化与回环候选验证。
- 摘要称在标准室内基准上，未标定设置下定位精度与渲染质量有一致提升，并称其为未标定 Gaussian SLAM 的强基线。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算开销、对 VGGT 先验质量的依赖程度、评测数据集名称与规模、消融实验细节、与基线方法的定量比较结果，以及是否适用于室外或大规模场景。上述内容均无法仅凭给定摘要判断。

### 阅读优先级
**中**。理由：该论文处于几何基础模型、三维重建与神经场景表示/渲染的交叉点，主题明确，方法要素（前馈先验、可微 BA、解析标定、GNA）具有参考价值；但当前仅有摘要，缺少实验数据、基线对比与消融细节，是否值得优先精读取决于读者对未标定单目 Gaussian SLAM 或 VGGT 先验应用的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

We present VGGT-GS SLAM, a monocular 3D Gaussian Splatting SLAM system designed for uncalibrated videos. Starting from feed-forward VGGT pose and depth priors, our system performs submap differentiable bundle adjustment that jointly refines camera poses and a 3D Gaussian map, while optimizing submap-shared intrinsics and radial--tangential distortion through analytic calibration Jacobians. To improve global consistency, we introduce Gaussian-native alignment (GNA) for camera-anchored scale refinement between sequential submaps and verification of loop-closure candidates. Extensive experiments on standard indoor benchmarks show consistent improvements in localization accuracy and strong rendering quality under uncalibrated settings, establishing a strong baseline for uncalibrated Gaussian SLAM.

</details>

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-21 - Dynamic Thermal Gaussians: Multimodal 4D Gaussian Splatting

**Authors:** Rongfeng Lu, Lifeng Lin, Xiaobao Wei, Quan Chen, Ming Lu, Yitian Xue, Yaoqi Sun, Yuhan Gao, Anke Xue, Chenggang Yan
**Links:** [abs](https://arxiv.org/abs/2609.24531) - [pdf](https://arxiv.org/pdf/2609.24531)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, spatiotemporal reconstruction, dynamic scene representation, 4D Gaussian, Gaussian Splatting, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dynamic Thermal Gaussians: Multimodal 4D Gaussian Splatting
- 作者：Rongfeng Lu, Lifeng Lin, Xiaobao Wei, Quan Chen, Ming Lu, Yitian Xue, Yaoqi Sun, Yuhan Gao, Anke Xue, Chenggang Yan
- 出版日期：2026-09-21T13:03:17Z
- 分类：Dynamic / 4D Reconstruction（主类）；Neural Scene Representations & Rendering（次类）
- 链接：摘要页 https://arxiv.org/abs/2609.24531 ；PDF https://arxiv.org/pdf/2609.24531 ；代码与数据集 https://github.com/LinLif1869/DTG

### 一句话总结
该论文提出首个面向复杂场景的动态 RGB-热成像重建框架，将颜色与热模态锚定到共享几何基底上，实现随时间变化的外观与温度的高保真时空重建。

### 研究问题
热成像在军事及更广泛的热分析应用中具有重要作用。现有 3D 热重建工作已将温度分析从 2D 扩展到 3D 空间，但多数假设温度分布是静态的，忽略了真实环境中热传递的时间动态性。论文要解决的问题是：如何对复杂场景中随时间变化的 RGB 外观、热观测与场景几何进行联合建模与重建。

### 核心思路/方法
- 提出首个面向复杂场景的动态 RGB-热重建框架，联合建模随时间变化的 RGB 外观、热观测与场景几何。
- 引入多模态动态场景表示，将颜色模态与热模态锚定到一个共享几何基底上，以保证二者在时空形变下的一致性。
- 设计多模态嵌入，以增强每个模态的运动表达能力。
- 提出多模态路由机制：保留一组统一的共享多模态高斯作为几何骨干，同时自适应地生成模态特定的高斯，以增强各模态在细节丰富区域的表示能力。
- 贡献一个新的基准数据集，包含高频温度变化，用于促进 4D 重建评估。
- 摘要称大量实验表明该方法在外观与温度两方面均实现了高保真时空重建。

### 主要贡献
- 提出首个面向复杂场景的动态 RGB-热重建框架，弥补现有工作忽略热传递时间动态性的不足。
- 提出多模态动态场景表示，将颜色与热模态锚定于共享几何基底，确保时空形变下的一致性。
- 设计多模态嵌入以增强各模态运动表达能力，并提出多模态路由机制，在共享多模态高斯几何骨干基础上自适应生成模态特定高斯。
- 贡献一个具有高频温度变化的新基准数据集，用于 4D 重建评估。
- 公开代码与数据集。

### 局限性
摘要未提供足够信息。摘要未提及方法的具体失效场景、计算开销、对特定传感器或数据条件的依赖，也未给出定量结果或与基线方法的对比细节，因此无法基于摘要判断其局限性。

### 阅读优先级
中。理由：该工作属于动态/4D 重建与多模态神经场景表示交叉方向，提出首个动态 RGB-热重建框架并附带新数据集，对热成像 3D/4D 分析相关研究者有参考价值；但摘要未提供定量实验证据与具体实现细节，若研究兴趣不涉及热成像或多模态动态重建，优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Thermography plays a vital role in military and broader thermal analysis applications. Recent progress in 3D thermal reconstruction has extended temperature analysis from 2D to 3D space, yet most existing works assume static temperature distributions, neglecting the temporal dynamics of heat transfer in real-world environments. To address this limitation, we propose the first dynamic RGB-Thermal reconstruction framework for complex scenes. Our method jointly models RGB appearance, thermal observations, and scene geometry as they change over time. Specifically, we introduce a multimodal dynamic scene representation that anchors both the color and thermal modalities to a shared geometric substrate, ensuring their consistency under spatiotemporal deformations. We further design multimodal embeddings to enhance the motion expressiveness for each modality, and propose a multimodal routing mechanism that retains a unified set of shared multimodal Gaussians as the geometric backbone while adaptively spawning modality-specific Gaussians to strengthen the representational capacity in detail-rich regions of each individual modality. In addition, we contribute a novel benchmark dataset featuring high-frequency temperature variations to facilitate the evaluation of 4D reconstruction. Extensive experiments demonstrate that our method achieves high-fidelity spatiotemporal reconstruction of both appearance and temperature. Our code and dataset are available at: https://github.com/LinLif1869/DTG.

</details>

#### 2026-09-21 - Relightable 3D Avatar Reconstruction with Semantic-Adaptive Motion-Illumination Responses

**Authors:** Jiankuo Zhao, Xiangyu Zhu, Jijie Li, Baiqin Wang, Shukai Chen, Zhen Lei
**Links:** [abs](https://arxiv.org/abs/2609.24158) - [pdf](https://arxiv.org/pdf/2609.24158)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** avatar reconstruction, relighting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Relightable 3D Avatar Reconstruction with Semantic-Adaptive Motion-Illumination Responses
- 作者：Jiankuo Zhao, Xiangyu Zhu, Jijie Li, Baiqin Wang, Shukai Chen, Zhen Lei
- 出版日期：2026-09-21T06:18:27Z
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2609.24158

### 一句话总结
SAMIRA 是一个基于 3D 高斯表示的头部化身重建框架，通过按面部语义区域分别建模运动响应和光照响应，提升单目视频重建中的表情动画精度与重光照真实感。

### 研究问题
从单目视频重建富有表现力且可重光照的 3D 头部化身仍具挑战，因为需要同时精确建模非刚性面部运动与依赖光照的外观。现有高斯化身方法通常采用全局耦合表示，即所有高斯基元共享统一的运动或光照响应模型；这种统一建模忽略了不同面部语义区域各自不同的运动模式和材质/反射特性，从而限制了细粒度动画精度并降低了重光照合理性。

### 核心思路/方法
论文提出 SAMIRA，一个用于语义自适应运动-光照响应建模的 3D 高斯化身框架，包含两个模块：

1. **语义自适应运动响应模块**：将当前帧到参考帧的网格位移光栅化到拓扑一致的 UV 空间，并利用面部语义将位移特征路由到各个语义专属的调制器中，从而在粗粒度网格绑定之外预测局部化的高斯几何残差。

2. **语义自适应光照响应模块**：为每个面部区域学习紧凑的漫反射与镜面反射响应因子，使不同区域的高斯能够针对新环境光照调整其光照响应。这些响应因子被纳入延迟物理基于着色（deferred physically based shading）中，以轻量方式近似语义相关的光照效果。

### 主要贡献
- 提出 SAMIRA 框架，面向 3D 高斯化身实现语义自适应的运动-光照响应建模。
- 设计语义自适应运动响应模块，通过 UV 空间位移光栅化与语义专属调制器预测局部高斯几何残差，以突破统一运动模型的限制。
- 设计语义自适应光照响应模块，为各面部区域学习漫反射/镜面反射响应因子，并融入延迟物理基于着色，以实现语义相关光照效果的轻量近似。
- 在自重现、跨重现和重光照任务上的实验表明，SAMIRA 在细粒度表情重建和重光照真实感方面优于现有方法（具体实验细节摘要未提供足够信息）。

### 局限性
摘要未提供足够信息。摘要未提及方法的失败案例、计算开销、对特定数据或条件的依赖、泛化边界等具体局限。

### 阅读优先级
中。理由：该论文聚焦单目视频的可重光照 3D 头部化身重建，针对现有高斯方法“全局耦合表示”的明确问题提出语义自适应运动与光照响应建模，思路清晰且模块化；但摘要未给出定量结果、数据集规模或与基线方法的详细对比，且论文分类为动态/4D 重建，若研究兴趣集中在可重光照化身、高斯表示或语义区域建模，则相关性较高；若关注通用 3D 重建或静态场景，则优先级相对一般。

</details>

<details>
<summary>Abstract</summary>

Reconstructing expressive and relightable 3D head avatars from monocular videos remains challenging in computer vision, as it requires accurate modeling of both non-rigid facial motion and illumination-dependent appearance. Existing Gaussian avatar methods commonly rely on globally coupled representations, in which Gaussian primitives share a unified motion or illumination response model. Such uniform modeling neglects the distinct motion patterns and material/reflectance properties of different facial semantic regions, thereby limiting fine-grained animation accuracy and reducing relighting plausibility. To address this limitation, we propose SAMIRA, a 3D Gaussian avatar framework for semantic-adaptive motion-illumination response modeling. For motion response modeling, the Semantic-Adaptive Motion Response module rasterizes current-to-reference mesh displacements into a topology-consistent UV space and leverages facial semantics to route displacement features through semantic-specific modulators, predicting localized Gaussian geometric residuals beyond coarse mesh binding. For illumination response modeling, the Semantic-Adaptive Illumination Response module learns compact diffuse and specular response factors for each facial region, allowing Gaussians in different regions to adapt their illumination responses to novel environment lighting. These response factors are incorporated into deferred physically based shading, providing a lightweight approximation of semantic-dependent illumination effects. Extensive experiments on self-reenactment, cross-reenactment, and relighting demonstrate that SAMIRA improves both fine-grained expression reconstruction and relighting realism over existing methods.

</details>

#### 2026-09-20 - GARO: Geometry-Aware Redundancy Optimization for Real-Time and High-Fidelity Dynamic Gaussian Splatting

**Authors:** Huiwen Xue, Kaixing Zhao, Zuheng Ming, Tingcheng Li
**Links:** [abs](https://arxiv.org/abs/2609.23509) - [pdf](https://arxiv.org/pdf/2609.23509)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic Gaussian, scene reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GARO: Geometry-Aware Redundancy Optimization for Real-Time and High-Fidelity Dynamic Gaussian Splatting
- 作者：Huiwen Xue, Kaixing Zhao, Zuheng Ming, Tingcheng Li
- 出版日期：2026-09-20T09:52:43Z
- 分类：Dynamic / 4D Reconstruction（主分类）；Neural Scene Representations & Rendering（次分类）
- 链接：摘要页 https://arxiv.org/abs/2609.23509 ；PDF https://arxiv.org/pdf/2609.23509

### 一句话总结
GARO 面向动态高斯泼溅中冗余高斯过多导致的内存与渲染效率问题，提出一个几何感知的冗余度量框架，在自适应密度控制阶段剪除冗余点，以在保持 PSNR 稳定的同时实现 2 倍渲染加速。

### 研究问题
动态场景重建中的新视角合成对虚拟现实等应用十分重要，高渲染速度是其中的关键需求。现有可变形高斯泼溅方法虽能实现高保真动态场景建模，但由于存在大量冗余高斯，在内存占用和渲染效率方面仍受限制。论文即针对动态高斯表示中的冗余问题展开研究。

### 核心思路/方法
GARO 被定位为一个统一的冗余度量框架，嵌入传统动态场景重建流程的自适应密度控制阶段。其流程为两步筛选：
1. 先通过“优化活跃度评估策略”选出低梯度候选点；
2. 再通过“低曲率分析”评估几何复杂度，进一步过滤并剪除冗余点。
最终目标是得到紧凑且具有表现力的高斯表示。

### 主要贡献
- 提出 GARO——一个用于动态场景重建自适应密度控制阶段的统一冗余度量框架。
- 设计了先低梯度候选筛选、后低曲率几何复杂度评估的两阶段冗余点剪除机制。
- 在合成与真实数据集上的大量实验表明，GARO 在质量与速度之间取得稳健权衡：PSNR 保持稳定，渲染速度提升 2 倍。

### 局限性
摘要未提供足够信息。摘要中未给出具体数据集名称、对比基线、内存占用量化结果、失败案例或方法适用范围等细节。

### 阅读优先级
高。理由：该论文针对动态高斯泼溅中冗余高斯导致的内存与效率瓶颈提出通用的冗余度量框架，属于动态/4D 重建与神经场景表示方向的实时渲染效率问题；摘要给出了明确的机制描述与“PSNR 稳定、渲染速度 2 倍”的量化结论，对关注动态高斯压缩、实时渲染与虚拟现实应用的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis is a key task for dynamic scene reconstruction, where high rendering speed is essential for applications such as virtual reality. Existing deformable Gaussian Splatting methods achieve high-fidelity dynamic scene modeling, but still face limitations in memory usage and rendering efficiency due to the large number of redundant Gaussians. To address these challenges, we propose Geometry-Aware Redundancy Optimization (GARO), a unified redundancy measurement framework in the adaptive density control stage of the traditional dynamic scene reconstruction pipeline. This framework first selects low-gradient candidates using an optimization activity assessment strategy, and then evaluates geometric complexity through low curvature analysis to further filter and prune redundant points, resulting in a compact and expressive Gaussian representation. Extensive experiments on synthetic and real-world datasets demonstrate that GARO achieves robust trade-offs between quality and speed, with PSNR remaining stable and rendering speed improved by 2x, validating the efficiency and effectiveness of GARO.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-22 - GTR: Gated Token Recurrence for Efficient Dense Prediction

**Authors:** Zhe Feng, Longfei Liu, Wei Liu, Kai Chen, Jiangjiang Kong, Wei Zhou, Yifeng Qian, Dexiong Chen, Xuanlong Yu, Xi Shen
**Links:** [abs](https://arxiv.org/abs/2609.26590) - [pdf](https://arxiv.org/pdf/2609.26590)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, depth estimation, monocular depth

<details>
<summary>Abstract</summary>

Self-attention-based vision backbones perform well on dense prediction, but the quadratic computational cost of global softmax attention limits their efficiency as image resolution increases. We introduce Gated Token Recurrence (GTR), a softmax-free recurrent vision backbone that combines gated linear attention, alternating spatial scan directions, and spatially enhanced SwiGLU blocks. GTR is distilled from a detection-specialized DINOv3 teacher using only final-layer patch-token alignment through a linear projection and squared $\ell_2$ loss, without masked-token prediction or intermediate-layer supervision. With Objects365 detector pre-training, GTR-L achieves 58.9 box AP on COCO \texttt{val2017} with 1.908\,ms median batch-one latency under compiled FP16 execution on an RTX~4090. The same backbone also transfers to instance segmentation, pose estimation, oriented detection, semantic segmentation, and monocular depth estimation. In an isolated kernel benchmark, our specialized chunkwise CUDA operator is $4.0\times$ faster than FLA v0.5.0 at 1.6K tokens on RTX~4090. TensorRT deployment on DRIVE AGX Thor achieves 2.282--8.769\,ms median batch-one latency across the evaluated models. These results show that recurrent token mixing can provide an efficient alternative to global softmax attention for high-resolution dense prediction and edge deployment.Project page: https://intellindust-ai-lab.github.io/projects/GTR/

</details>

#### 2026-09-22 - Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation

**Authors:** John Church, Vazghen Nikolian
**Links:** [abs](https://arxiv.org/abs/2609.26561) - [pdf](https://arxiv.org/pdf/2609.26561)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

We present an improvement on previous spacecraft pose estimation architectures that results in the lowest published mean rotation errors we know of on the SPEED+ lightbox and sunlamp test sets for a known, non-cooperative spacecraft. By using a previously established heatmap-based pose estimation architecture and adapting a large self-supervised ViT foundation model (DINOv3) in place of the smaller convolutional and ViT encoders of previous work, we show that pose estimation accuracy improves from 300M to 840M parameters with no saturation yet observed. We also evaluate our 840M model on a Jetson Orin NX 16GB, measuring single-pass network inference at 133.8 ms per crop with a board draw of 32.0 W. These measurements demonstrate embedded inference feasibility on a processor family with orbital flight heritage. Our resulting model outperforms previous models across lightbox and sunlamp domains while training only on synthetic data. Our best model, using DINOv3 840M adapted with LoRA as the encoder (rank 64, three-seed ensemble with four-rotation test-time augmentation), results in $1.56^\circ$ mean rotation error on sunlamp and $1.17^\circ$ on lightbox, compared to the previous best mean rotation errors we know of on these test sets, $2.66^\circ$ and $1.75^\circ$ by EagerNet.

</details>

#### 2026-09-22 - ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards

**Authors:** Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci
**Links:** [abs](https://arxiv.org/abs/2609.26315) - [pdf](https://arxiv.org/pdf/2609.26315)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** SLAM, monocular depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

Orchard robots need maps that preserve small but semantically important structures such as trunks, trellises, and fruit. 3D Gaussian Splatting (3DGS) SLAM achieves high photometric fidelity. However, its optimization remains appearance-driven, and transferring image semantics to 3D points is unreliable for thin structures, whose pixels may receive depth from background surfaces. We present ArborSplat, an online semantic 3DGS SLAM system that tracks with LiDAR odometry and optimizes semantics directly on the Gaussian map, constrained by class-specific height bands above a ground plane fitted to each keyframe's stereo point cloud, and fuses multi-view evidence into a semantic point cloud online while rejecting labels inconsistent with the local ground surface or with monocular depth. Class-constrained refinement reserves Gaussian capacity for underrepresented structures and, under reduced budgets, increases training-view accuracy on tree classes. We evaluate the approach on apple and pear orchards during dormancy, flowering, and harvesting. On full routes, it keeps ATE below 0.5 m on all 12 traversals. On shared 301-frame segments, it exceeds SGS-SLAM and GS3LAM by 0.23 to 0.50 training-view and 0.15 to 0.36 held-out mIoU while running 1.7 to 7.5 times faster, whereas SemGauss-SLAM runs out of GPU memory on all six.

</details>

#### 2026-09-22 - LiFR v2: Completion-Augmented Event Propagation for High-Rate Dense Prediction

**Authors:** Tao Wan, Xiaoshan Wu, Yifei Yu, Bo Wang, Xiaoyang Lyu, Muxin Liu, Aoxuan Pan, Zhongrui Wang, Xiaojuan Qi
**Links:** [abs](https://arxiv.org/abs/2609.25803) - [pdf](https://arxiv.org/pdf/2609.25803)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>Abstract</summary>

High-rate dense perception in dynamic environments is limited by the low update rate of RGB cameras, as rapid scene changes can occur between frames. Event cameras offer temporally dense but spatially sparse measurements, complementary to spatially dense RGB observations. Direct fusion cannot fully exploit this complementarity, while event-guided propagation fails on newly appearing or disoccluded regions without valid RGB support. We present LiFR v2, a unified propagation-completion-memory framework for causal anytime and streaming dense prediction from an RGB keyframe and events. LiFR v2 introduces an Event-Guided Completion Module (EGCM) to recover task-relevant representations where propagation is unsupported, and a History Retrieval Module (HRM) to reuse completed representations across successive queries. The framework supports semantic segmentation, monocular depth estimation, and multi-task dense prediction, and we further introduce SHF-Emerge to evaluate rapid object emergence and disocclusion. LiFR v2 achieves 74.37% mIoU on DSEC and 56.13% on SHF-Emerge, improving LiFR-Seg by 1.85 percentage points on the latter, while reducing SHF-Emerge depth RMSE from 1.564 m to 1.118 m over the propagation baseline. It also exceeds 100 FPS for both segmentation and depth, demonstrating accurate and efficient high-rate perception beyond RGB frame rates.

</details>

#### 2026-09-22 - Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning

**Authors:** Dingkang Yang, Yizhou Liu, Wendong Cheng, Zizhi Chen, Shunli Wang, Yang Liu, Hongsheng Li, Lihua Zhang
**Links:** [abs](https://arxiv.org/abs/2609.25741) - [pdf](https://arxiv.org/pdf/2609.25741)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, geometric reconstruction, rendering, simulation

<details>
<summary>Abstract</summary>

Generative models have advanced image-conditioned 3D content creation, yet generating controllable and executable 3D scenes from a single image remains challenging. Existing 3D generative approaches can synthesize visually plausible objects and scenes, but their spatial layout estimation is coupled with specific asset generators. They struggle to jointly model object semantics, metric geometry, and scene-level spatial relationships, which are essential for interactive editing, physical simulation, and embodied applications. We propose Fysiverse-3D-Vision, a unified vision-language-geometry framework for generative 3D scene reconstruction and executable asset construction from a single image. We establish a shared representation where spatial reasoning and geometric reconstruction mutually enhance each other, allowing object layouts to be inferred beyond the constraints of individual asset generators. Our model integrates textual supervision, semantic visual cues, and geometric representations within a unified Transformer to capture scene context, metric geometry, and object-level interactions. An object-conditioned layout module performs cross-attention between target object representations and global geometric features to predict object translation, rotation, and scale. Training progressively learns geometry-language alignment, introduces layout reasoning while preserving reconstruction capability, and refines physical consistency through collision-aware optimization. By separating spatial layout reasoning from asset synthesis, Fysiverse-3D-Vision provides an adaptable interface for interactive scene editing, object-level manipulations, and executable 3D content generation. Experiments demonstrate that our framework achieves superior geometric consistency, layout estimation, rendering quality, and physical property understanding compared with existing approaches.

</details>

#### 2026-09-22 - Point Diffusion Mamba: Unified Diffusion-State-Space Modeling for Single-View 3D Reconstruction under Data Scarcity

**Authors:** Wei Zhou, Xinzhe Shi, Xingxing Hao, Xing Hao, Kang Li, Jinye Peng, Ying He
**Links:** [abs](https://arxiv.org/abs/2609.25538) - [pdf](https://arxiv.org/pdf/2609.25538)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, point cloud reconstruction

<details>
<summary>Abstract</summary>

While single-view 3D reconstruction has seen significant progress, extrapolating complex 3D structures from inherently ambiguous 2D observations remains fundamentally ill-posed, particularly in the critically underexplored data-scarce regime. To address this challenge, we propose Point Diffusion Mamba (PDM), a method that integrates the generative power of diffusion models with the efficiency of state-space model for single-view 3D reconstruction under data-scarce conditions. Specifically, PDM employs a lightweight reconstruction module tailored to handle unordered point-cloud inputs effectively. By combining a Local Geometric Aggregation module with Mamba blocks, our approach jointly models global geometric structures and local details. In 3D reconstruction, each point in the initial noisy input requires a precise prediction, yet the high-level features extracted by the Mamba module capture only abstract semantic information from sparse points. To bridge this gap, we introduce the Hierarchical Feature Integration Network, which fuses high-level semantic and local geometric features for each point, overcoming the limitations of token-based point-cloud reconstruction. Furthermore, we propose a Dynamic Weighted Sampling strategy that adaptively unifies 3D generation with single-view reconstruction by leveraging generative priors to enhance reconstruction quality. Experimental results on the ShapeNet and Pix3D benchmarks demonstrate that PDM outperforms state-of-the-art methods, providing an effective solution for 3D reconstruction under data-scarce settings. Code is available at: https://github.com/NWUzhouwei/PDM.

</details>

#### 2026-09-21 - SE(3) Neural Potential Fields for 6-DoF Trajectory Planning Directly from Images Without Explicit 3D Reconstruction

**Authors:** Jeffrey Eiyike, Masoud Ataei, Elvis Gyaase, Vikas Dhiman
**Links:** [abs](https://arxiv.org/abs/2609.24864) - [pdf](https://arxiv.org/pdf/2609.24864)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, dense reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SE(3) Neural Potential Fields for 6-DoF Trajectory Planning Directly from Images Without Explicit 3D Reconstruction
- 作者：Jeffrey Eiyike, Masoud Ataei, Elvis Gyaase, Vikas Dhiman
- 出版日期：2026-09-21T16:35:57Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2609.24864 ；PDF https://arxiv.org/pdf/2609.24864

### 一句话总结
论文提出一种直接从带位姿 RGB 图像学习的 SE(3) 神经势场，用导航函数（自由空间中到抓取位姿的测地距离）作监督，以绕开经典人工势场的局部停滞与贴障下降问题，实现无显式 3D 重建的 6-DoF 无碰撞轨迹规划。

### 研究问题
在杂乱场景中到达一个 6-DoF 抓取位姿需要无碰撞轨迹。传统做法是先重建 3D 场景再在重建中规划，代价是精度与计算开销。直接从图像学习势场可去掉这一依赖，但会继承人工势场的经典缺陷：当吸引梯度与排斥梯度相互抵消时，下降方向会贴着障碍物掠过而非绕行，并可能停在目标之前无法到达。

### 核心思路/方法
- 学习对象：SE(3) 神经势场，从带位姿的 RGB 图像学习。
- 监督信号：导航函数，即在训练时从同一批图像中恢复的自由空间内到抓取位姿的测地距离。
- 目的：通过该监督消除两类失败模式（梯度抵消导致的贴障下降，以及在目标前停滞）。
- 部署：在 UR10 上执行，针对两个桌面场景，从被障碍阻塞的起始位姿出发。

### 主要贡献
- 提出用导航函数监督的 SE(3) 神经势场，直接从图像学习，不需显式 3D 重建。
- 在两个桌面场景、UR10 上从被障碍阻塞的起点执行：该势场从每个起点都能收敛到抓取位姿 3 cm 以内，且执行的每条路径相对真值几何均为无碰撞；作为对比，仅用图像监督时分别为 25% 和 0%。
- 平均间隙从不足 1 cm 提升到 8.6–8.8 cm；机械臂连杆接触占已执行构型的比例从 20.6–50.4% 降到 2.7–5.5%。
- 两个场景上的实际抓取成功率分别为 90.0% 和 40.0%；剩余失败归因于笛卡尔执行器的拒绝，而非势场本身。
- 规划耗时约 2 s，对比在同样图像的重建上跑 RRT* 的 67–133 s；不过在统一的离线测试框架下两者相当，部署中的差距来自对稠密重建做碰撞检查的开销，而非规划器本身的复杂度。

### 局限性
- 摘要仅报告了两个桌面场景的实验，未给出更广泛场景或泛化能力的证据；摘要未提供足够信息说明在其他环境下的表现。
- 第二个场景的抓取成功率仅 40.0%，摘要将其归因于笛卡尔执行器的拒绝，但未提供该执行器失败的具体机制或改进方案；摘要未提供足够信息。
- 规划时间优势被作者限定为部署条件所致：在统一离线框架下与 RRT* 相当，说明优势并非来自规划器复杂度本身；摘要未提供足够信息说明该部署开销差异在更一般设置下是否保持。
- 训练依赖从图像恢复的自由空间测地距离作为监督，其恢复质量对结果的影响在摘要中未量化；摘要未提供足够信息。
- 未提及推理时是否需要真值几何进行碰撞检查之外的计算，也未提及对不同机械臂或相机的迁移能力；摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对“从图像直接做 6-DoF 规划、不做显式 3D 重建”这一明确问题，并给出较具体的量化对比（收敛精度、间隙、连杆接触比例、抓取成功率与规划耗时），对图像驱动规划与势场方法方向有参考价值；但摘要只覆盖两个桌面场景，且作者自己指出时间优势在统一框架下并不成立，因此其结论的普适性有待正文验证，适合作为方法参考而非必读结论性文献。

</details>

<details>
<summary>Abstract</summary>

Reaching a 6-DoF grasp pose in clutter requires a collision-free trajectory, conventionally obtained by reconstructing the scene in 3D and planning inside that reconstruction, at the cost of its accuracy and compute. Potential fields learned directly from images remove that dependency but inherit the classical weakness of artificial potential fields: where attractive and repulsive gradients cancel, the descent grazes the obstacle instead of going around it, and can stall short of the goal. We present an SE(3) neural potential field learned from posed RGB images and supervised with a navigation function, the geodesic distance to the grasp through free space recovered from those same images during training, which removes both failures. On two tabletop scenes, from obstacle-blocked starts executed on a UR10, the field converges within 3 cm of the grasp from every start and every path it executes is collision-free against the ground-truth geometry, against 25% and 0% under image supervision alone; mean clearance rises from under a centimeter to 8.6-8.8 cm and arm-link contacts fall from 20.6-50.4% to 2.7-5.5% of executed configurations. Executed grasp success is 90.0% and 40.0% on the two scenes, the residual failures being refusals of the Cartesian executor rather than of the field. Planning takes about 2 s against 67-133 s for RRT* on a reconstruction of the same images, though under a common offline harness the two are comparable: the deployed margin is the cost of collision-checking a dense reconstruction, not planner complexity.

</details>

#### 2026-09-21 - Revisiting Multi-View Stereo: A Sequence-to-Sequence Formulation

**Authors:** Aoxiang Fan, Corentin Dumery, Nicolas Talabot, Pascal Fua
**Links:** [abs](https://arxiv.org/abs/2609.24850) - [pdf](https://arxiv.org/pdf/2609.24850)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** multi-view stereo, MVS, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Revisiting Multi-View Stereo: A Sequence-to-Sequence Formulation
- 作者：Aoxiang Fan, Corentin Dumery, Nicolas Talabot, Pascal Fua
- 出版日期：2026-09-21T16:28:26Z
- 分类：3D Reconstruction & Multi-view Geometry（主类别）；次类别：未提供
- 链接：摘要页 https://arxiv.org/abs/2609.24850；PDF https://arxiv.org/pdf/2609.24850

### 一句话总结
该论文针对已知相机参数的多视图立体（MVS）问题，将传统 MVS 从“序列到单视图深度”的映射重新表述为“序列到序列”的联合几何预测，并通过可注入相机先验的全局 Transformer 架构提升重建表现。

### 研究问题
论文关注的是：在已知相机参数条件下，从多视图图像计算准确几何结构。摘要指出，近期前馈（FF）模型虽然可以联合估计三维几何与相机参数，但即使提供真值相机参数，也常因重建歧义导致几何畸变。因此，作者重新审视已知相机参数下的 MVS 问题，试图在传统 MVS 与前馈方法之间建立桥梁。

### 核心思路/方法
论文的核心思路是将 MVS 不再视为仅对单个参考视图预测深度的“序列到一”映射，而是类似前馈模型的“序列到序列”任务，对所有输入视图联合预测几何。

方法上，作者提出一种基于全局 Transformer 的架构，包含两个显式利用相机诱导先验的组件：
1. 光线图嵌入（ray-map embeddings）：将相机参数注入图像块 token，使 Transformer 具备相机感知能力；
2. 统一的全局代价体（unified global cost volume）：替代传统逐视图代价体，用于联合捕获所有视图中的三维结构。

### 主要贡献
- 将已知相机参数下的 MVS 重新表述为序列到序列任务，对所有输入视图联合预测几何。
- 提出一种全局 Transformer 架构，并设计两个显式利用相机先验的组件：光线图嵌入与统一全局代价体。
- 摘要称在多个公开基准上进行了大量实验，方法达到 state-of-the-art 性能，超过 MVS 与前馈重建基线。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法的具体失败情形、计算开销、对相机参数误差的敏感性、训练数据规模或泛化边界等局限。

### 阅读优先级
高。理由：该论文直接回应 MVS 与前馈重建方法之间的关键差异，提出序列到序列重构与相机感知 Transformer 设计，并在摘要中声称在多个公开基准上超过 MVS 和 FF 基线；若关注已知相机参数下的三维重建、多视图几何或前馈式重建架构，该工作具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Computing accurate geometry from multi-view images is a fundamental problem in computer vision. Recent feed-forward (FF) models jointly estimate 3D geometry and camera parameters, but they typically suffer from geometry distortion caused by reconstruction ambiguity, even when ground-truth camera parameters are supplied. In this paper, we study the multi-view stereo (MVS) problem with known camera parameters and propose a novel approach that bridges conventional MVS and FF methods. Rather than casting MVS as a sequence-to-one mapping that predicts depth only for a single reference view, we reformulate it as a sequence-to-sequence task, akin to FF models, that jointly predicts geometry for all input views. We introduce a global transformer-based architecture with two components that explicitly exploit camera-induced priors: ray-map embeddings that inject camera parameters into image patch tokens, making the transformer camera-aware, and a unified global cost volume that replaces conventional per-view cost volumes to jointly capture 3D structure across all views. Extensive experiments on multiple public benchmarks show our approach achieves state-of-the-art performance, surpassing both MVS and FF reconstruction baselines.

</details>

#### 2026-09-21 - Range-Aided SLAM Initialization Exploiting Accurate Heading Information

**Authors:** Isabel Lougheed, James Richard Forbes
**Links:** [abs](https://arxiv.org/abs/2609.24846) - [pdf](https://arxiv.org/pdf/2609.24846)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Range-Aided SLAM Initialization Exploiting Accurate Heading Information
- 作者：Isabel Lougheed, James Richard Forbes
- 出版日期：2026-09-21T16:24:26Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：abstract_url: https://arxiv.org/abs/2609.24846；pdf_url: https://arxiv.org/pdf/2609.24846

### 一句话总结
本文提出一种面向距离辅助 SLAM（RA-SLAM）的两步初始化方法，在已知高精度航向信息的条件下，先借助 GTRS 求解应答器相对 AUV 的位置，再通过线性最小二乘估计应答器与 AUV 的位置，从而为一般非线性 RA-SLAM 问题提供可靠初始化。

### 研究问题
一般 SLAM 问题具有可分离结构：在机器人航向已知时，地标与机器人位置可线性求解。本文关注的是拥有高精度航向信息的场景，例如自主水下航行器（AUV）导航，并利用这一条件求解距离应答器与机器人的位置。其目标是为距离辅助 SLAM 提供有效的初始化方法。

### 核心思路/方法
方法包含两个步骤：
1. 给定非线性距离测量，使用广义信赖域子问题（GTRS）求解应答器相对于 AUV 的位置。
2. 利用相对应答器位置与已知的 AUV 航向，通过求解线性最小二乘问题估计应答器与 AUV 的位置。

这些应答器与 AUV 位置估计，结合高精度航向信息，为一般非线性 RA-SLAM 问题提供可靠初始化。论文在真实 AUV 数据集上测试了该方法，该数据集同时提供长基线（LBL）距离测量与惯性导航系统（INS）提供的高精度航向信息。

### 主要贡献
- 提出一种利用高精度航向信息的 RA-SLAM 初始化方法。
- 将初始化拆分为两步：先以 GTRS 求解应答器相对位置，再以线性最小二乘估计应答器与 AUV 位置。
- 所得到的应答器与 AUV 位置估计结合高精度航向，可为一般非线性 RA-SLAM 提供可靠初始化。
- 在真实 AUV 数据集上验证了该方法，该数据集包含 LBL 距离测量与 INS 高精度航向信息。

### 局限性
摘要未提供足够信息说明方法的计算复杂度、对航向精度下降的敏感性、对测距噪声或异常值的鲁棒性、与其它初始化方法的定量对比，以及失败情形或适用边界。摘要也未提供足够信息说明在更广泛场景（非 AUV 或航向精度不足）中的泛化能力。

### 阅读优先级
中。理由：该工作面向 RA-SLAM 初始化，问题定义清晰，且利用 AUV 场景中常见的高精度航向信息构造两步求解流程，并在真实 AUV 数据集上测试；对水下导航、距离辅助 SLAM 初始化及相关最小二乘求解感兴趣的读者具有参考价值。但摘要未给出与现有方法的定量比较或详细实验指标，因此不适合仅凭摘要判定为最高优先级。

</details>

<details>
<summary>Abstract</summary>

This paper presents a novel initialization method for range-aided simultaneous localization and mapping (RA-SLAM). The general SLAM problem has a well-known separable structure where landmark and robot positions can be solved for in a linear fashion given known robot headings. This paper considers the case where highly accurate heading information is available, which is typical of autonomous underwater vehicle (AUV) navigation, to solve for the range transponder and robot positions. The proposed approach consists of two steps. First, using a generalized trust region subproblem (GTRS), the positions of the transponders relative to the AUV are solved for given the nonlinear range measurements. Second, the relative transponder positions and the known heading of the AUV are used to estimate the transponder and AUV positions by solving a linear least-squares problem. These transponder and AUV position estimates, combined with the highly accurate heading information, provide a reliable initialization method for the general nonlinear RA-SLAM problem. The effectiveness of the proposed approach is tested on a real-world AUV dataset where long baseline (LBL) range measurements are provided in concert with highly accurate heading information provided by an inertial navigation system (INS).

</details>

#### 2026-09-21 - CMAMBADEPTH: Self-supervised Monocular Depth Estimation with Channel Mamba and Hybrid Attention

**Authors:** Xuezhi Xiang, Jiayao Liu, Heqi Xiang, Yuqi Hu, Yiming Chen, Shanjun Zhang
**Links:** [abs](https://arxiv.org/abs/2609.24494) - [pdf](https://arxiv.org/pdf/2609.24494)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CMAMBADEPTH: Self-supervised Monocular Depth Estimation with Channel Mamba and Hybrid Attention
- 作者：Xuezhi Xiang, Jiayao Liu, Heqi Xiang, Yuqi Hu, Yiming Chen, Shanjun Zhang
- 出版日期：2026-09-21T12:31:24Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.24494

### 一句话总结
该论文提出 CMambaDepth，一个基于通道选择性状态传播的自监督单目深度估计框架，通过双向/单向 Channel Mamba 与混合注意力模块来解决跨尺度信息交互低效及局部-全局空间建模难以平衡的问题。

### 研究问题
现有自监督单目深度估计方法普遍存在两个瓶颈：
1. 跨尺度信息交互效率低下；
2. 难以平衡局部与全局空间建模。

### 核心思路/方法
论文提出 CMambaDepth 自监督框架，核心设计包含三个组件：
1. **双向 Channel Mamba（Bi-CMamba）**：对齐编码器跨尺度特征，并在有序尺度组之间实现双向信息交换。
2. **单向 Channel Mamba（Uni-CMamba）**：逐步聚合解码器特征，并通过组选择机制保留细粒度尺度组以供后续融合。
3. **混合注意力模块（HAM）**：结合大核局部上下文与 Manhattan 自注意力，实现互补的空间建模。

论文还给出了实验结果：在 KITTI 上达到 AbsRel 0.094、RMSE 4.156；在 DDAD 上 AbsRel 0.140；在 NYUv2 零样本跨数据集泛化测试中 AbsRel 0.232，比基线 RA-Depth 提升 7.2%。

### 主要贡献
1. 提出 CMambaDepth 自监督框架，通过通道选择性状态传播实现高效多尺度特征融合和细粒度上下文建模。
2. 设计 Bi-CMamba 用于编码器跨尺度特征对齐与尺度组间双向信息交换。
3. 设计 Uni-CMamba 用于解码器特征逐步聚合，并通过组选择机制保留细粒度尺度组。
4. 引入 HAM，将大核局部上下文与 Manhattan 自注意力结合以互补空间建模。
5. 在 KITTI、DDAD 及 NYUv2 零样本跨数据集测试上取得有竞争力的结果。

### 局限性
- 摘要未提供足够信息说明方法的具体计算开销、参数量或推理速度。
- 摘要未提供足够信息说明在更广泛数据集或不同场景条件下的表现。
- 摘要未提供足够信息说明各模块的消融实验细节及其各自贡献的量化分析。
- 摘要未提供足够信息说明失败案例或方法适用范围的具体限制。

### 阅读优先级
**中**。理由：该论文针对自监督单目深度估计中的跨尺度交互与局部-全局建模平衡问题提出明确方法，并在 KITTI、DDAD、NYUv2 上报告了量化结果，主题与 3D Reconstruction & Multi-view Geometry 分类直接相关，对关注单目深度估计、Mamba 结构或自监督学习的读者有参考价值；但摘要未提供足够信息展示方法细节深度、消融充分性与实际部署开销，因此不宜定为最高优先级。

</details>

<details>
<summary>Abstract</summary>

Accurate monocular depth estimation serves as a core enabler for single camera scene understanding. However, existing self-supervised monocular depth estimation methods generally suffer from the bottleneck of inefficient cross-scale information interaction and difficulty in balancing local and global spatial modeling. In this paper, we propose CMambaDepth, a self-supervised framework that achieves efficient multi-scale feature fusion and fine-grained contextual modeling via channel-wise selective state propagation. Specifically, Bidirectional Channel Mamba (Bi-CMamba) aligns encoder features across scales and enables bidirectional information exchange among ordered scale groups. Unidirectional Channel Mamba (Uni-CMamba) progressively aggregates decoder features and retains fine-grained scale groups through a group selection mechanism for subsequent fusion. Furthermore, a Hybrid Attention Module (HAM) is introduced to combine large-kernel local context and Manhattan self-attention for complementary spatial modeling. Experimental results demonstrate that our method achieves highly competitive performance. Specifically, our model achieves an AbsRel of 0.094 and an RMSE of 4.156 on KITTI, and an AbsRel of 0.140 on DDAD. In the zero-shot cross-dataset generalization test on NYUv2, it attains an AbsRel of 0.232, outperforming the baseline RA-Depth by 7.2%.

</details>

#### 2026-09-21 - STA-TFM: Spatio-Temporal Aggregation Across Views TransForMer for Pose Estimation

**Authors:** Mena Kamel, Natalie Won, Amrut Sarangi, Sven Jager, Albert Pla Planas
**Links:** [abs](https://arxiv.org/abs/2609.24482) - [pdf](https://arxiv.org/pdf/2609.24482)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：STA-TFM: Spatio-Temporal Aggregation Across Views TransForMer for Pose Estimation
- 作者：Mena Kamel, Natalie Won, Amrut Sarangi, Sven Jager, Albert Pla Planas
- 出版日期：2026-09-21T12:22:35Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.24482) / [PDF](https://arxiv.org/pdf/2609.24482)

### 一句话总结
STA-TFM 是一种基于 Transformer 的多视角 3D 人体姿态估计架构，通过融合单视角时空特征与跨视角信息，并辅以可控的多视角数据生成流程，在多个数据集上优于现有的无需相机参数的多视角方法。

### 研究问题
单目 3D 人体姿态估计（HPE）仍受深度歧义、遮挡和时序一致性需求等问题困扰。多视角方法虽然精度优于单目方法，但通常需要复杂的搭建。论文旨在提出一种多视角姿态估计方法，在提升精度的同时避免复杂设置，并缓解训练数据稀缺问题。

### 核心思路/方法
- 采用基于 Transformer 的架构，结合空间与时间信息进行多视角姿态估计。
- 利用 DSTformer 作为单目特征提取器，在每个视角内捕获长距离姿态依赖关系。
- 使用融合 Transformer 跨视角聚合信息，生成连贯的 3D 估计。
- 针对训练数据稀缺，提出数据生成流程，可将任意现有 3D 姿态数据集转换为参数可控的多视角设置。
- 方法可处理噪声及缺失的 2D 输入。

### 主要贡献
- 提出 STA-TFM，一种结合空间与时间信息的多视角姿态估计 Transformer 架构。
- 引入融合 Transformer 跨视角聚合信息，并复用 DSTformer 捕获单视角长距离依赖。
- 提出可控参数的多视角数据生成流程，以缓解训练数据稀缺。
- 实验表明在多个数据集上优于现有的无需相机参数的多视角方法：在 DHP19 上 MPJPE 和 MPJVE 分别降低 50.9% 和 49.5%；在 HAA4D 上分别降低 6.7% 和 7.7%；在 TotalCapture 上 MPJPE 降低 15.2%。
- 方法能处理噪声和缺失的 2D 输入，具备在医疗监测、运动评估和沉浸式技术中部署的潜力。

### 局限性
- 摘要未提供足够信息说明方法在具体实验设置、数据集规模、计算成本或实时性方面的限制。
- 摘要未提供足够信息说明数据生成流程的具体假设或其对真实多视角数据的泛化能力。
- 摘要未提供足够信息说明方法在相机参数可用时的相对表现，或与其他需要相机参数的方法的详细对比。
- 摘要未提供足够信息说明在极端遮挡或严重噪声条件下的失败案例。

### 阅读优先级
高。理由：该论文针对 3D 人体姿态估计中的深度歧义、遮挡和时序一致性等核心问题，提出结合时空与跨视角信息的 Transformer 架构，并在多个数据集上报告了显著的误差降低，同时提供了代码、检查点和数据链接，对多视角几何与 3D 重建方向具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular 3D human pose estimation (HPE) remains challenging due to depth ambiguity, occlu- sions, and the need for temporal consistency. While multi-view methods provide superior accuracy over monocular approaches, they often require complex setups. We introduce STA-TFM, a transformer-based architecture that combines spatial and temporal information for multi-view pose estimation. The approach leverages DSTformer, a monocular feature extractor, to capture long-range pose dependencies within each view. A fusion transformer then aggregates information across views to produce coherent 3D estimates. To address training data scarcity, we use a data generation pipeline that transforms any existing 3D pose dataset into multi-view setups with controllable parameters. Experiments on various datasets demonstrate that STA-TFM outperforms existing camera-parameter-free multi-view methods. STA-TFM achieves 50.9% and 49.5% reductions in mean per joint position error (MPJPE) and mean per joint velocity error (MPJVE) on the DHP19 dataset. Furthermore, it achieves 6.7% and 7.7% respective reductions on HAA4D, and a 15.2% MPJPE reduction on TotalCapture. STA-TFM handles noisy and missing 2D inputs, supporting potential deployment in healthcare monitoring, athletic assessment, and immersive technologies. Code, training checkpoints, and data are available at https://zenodo.org/records/22832620.

</details>

#### 2026-09-20 - Learning-Based 3D Reconstruction of Power Networks from Aerial Point Clouds

**Authors:** Rishabh Jain, Anuja Saini, Vishal Jain
**Links:** [abs](https://arxiv.org/abs/2609.23915) - [pdf](https://arxiv.org/pdf/2609.23915)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning-Based 3D Reconstruction of Power Networks from Aerial Point Clouds
- 作者：Rishabh Jain, Anuja Saini, Vishal Jain
- 出版日期：2026-09-20T22:43:42Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.23915) / [PDF](https://arxiv.org/pdf/2609.23915)

### 一句话总结
该论文提出一个端到端框架，从大规模航空 LiDAR 点云中重建架空电力网络拓扑，并提取跨档级物理元数据。

### 研究问题
如何从大规模航空 LiDAR 点云中重建架空电力设施网络拓扑，并提取跨档级物理元数据。摘要指出，启发式连通规则在密集、杂乱场景或导线部分观测下容易失效，因此需要更稳健的方法。

### 核心思路/方法
论文方法包括三个主要部分：
1. **语义分割**：使用改进的 KPConv 模型对输入点云进行语义分割，通过调整数据采样和损失函数，强化对杆塔和导线类别的关注。
2. **网络拓扑推断**：分两阶段进行：
   - 对杆塔类点进行聚类获得杆塔实例，并使用几何准则验证候选，包括通过 PCA 估计的高度和垂直度；
   - 对候选杆塔对，结合启发式方法和轻量级 ResNet 分类器，在杆塔与导线点分布的二维俯视投影上判断是否存在物理导线跨档。
3. **属性计算**：对每条验证后的导线，计算电力基础设施几何属性，包括端点导线高度、地面高程、与弧垂相关的最低点特征、导线排列和导线宽度。

### 主要贡献
- 提出端到端的航空 LiDAR 电力网络拓扑重建与跨档级物理元数据提取框架。
- 使用改进 KPConv 语义分割，并通过采样与损失调整强化杆塔和导线类别。
- 通过显式分类候选跨档，缓解密集、杂乱场景和导线部分观测下启发式连通规则的常见失效模式。
- 在多个真实航空 LiDAR 数据集上评估，报告端点高度达到分米级精度，拓扑重建召回率相对启发式最近邻基线约提升 9%，在复杂布局中提升更大。
- 为每条验证导线计算端点导线高度、地面高程、弧垂相关最低点特征、导线排列和导线宽度等属性。

### 局限性
摘要未提供足够信息说明方法在极端天气、不同 LiDAR 密度、不同电压等级或大规模计算效率方面的表现；也未提供具体失败案例、超参数敏感性或泛化能力边界。摘要未提供足够信息说明实验数据规模、标注成本、类别不平衡处理细节及与更多基线方法的全面比较。

### 阅读优先级
中。理由：该论文聚焦航空 LiDAR 点云中的电力网络 3D 重建与拓扑推断，方法组合明确，包含语义分割、几何验证和基于 ResNet 的跨档分类，并报告了分米级高度精度和约 9% 的召回率相对提升。若读者关注点云语义分割、基础设施重建或拓扑推断，具有参考价值；但摘要未提供足够信息展示完整实验细节、局限性和泛化边界，因此优先级不宜直接定为高。

</details>

<details>
<summary>Abstract</summary>

This paper presents an end-to-end framework for reconstructing overhead power utility network topology and extracting span-level physical metadata from large-scale aerial LiDAR. The pipeline begins with semantic segmentation of the input point cloud using an improved KPConv-based model, in which data sampling and loss functions are adapted to emphasize pole and conductor (wire) classes. Network topology inference then proceeds in two stages: (i) pole instances are obtained by clustering pole-class points and validating candidates using geometric criteria, including height and verticality estimated via PCA, and (ii) candidate pole pairs are evaluated using a heuristic method and a lightweight ResNet-based classifier on 2D top-view projections of pole and wire point distributions to determine whether a physical conductor span exists. By explicitly classifying candidate spans, the approach mitigates common failure modes of heuristic connectivity rules in dense or cluttered scenes and under partial wire observation. For each validated wire, attributes regarding utility infrastructure geometry are computed, including endpoint conductor heights, ground elevation, sag-related lowest-point features, conductor arrangement, and wire width. Evaluation on multiple real-world aerial LiDAR datasets demonstrates decimeter-level endpoint height accuracy and approximately 9% relative improvement in recall for topology reconstruction compared to heuristic nearest-neighbor baselines, with larger gains in complex layouts.

</details>

#### 2026-09-20 - Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction

**Authors:** Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi
**Links:** [abs](https://arxiv.org/abs/2609.23796) - [pdf](https://arxiv.org/pdf/2609.23796)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** monocular geometry, scene reconstruction

<details>
<summary>Abstract</summary>

Single-image 3D object generation can now produce high-fidelity assets, yet accurately placing them into a coherent scene layout remains an open challenge. A central difficulty lies in how object layout is represented. Holistic methods absorb placement into a scene-level generation process, sacrificing object-level detail. Compositional methods preserve object fidelity by decoupling geometry from layout, but typically parameterize layout as sparse, unbounded pose variables that are difficult to learn and generalize poorly under scarce scene-level supervision. We present Mira-Scene, a compositional 3D scene reconstruction framework that replaces sparse pose regression with dense, bounded correspondence recovery. At its core is the Canonical Coordinate Map (CCM), a pixel-aligned field that maps each visible object pixel to a surface coordinate in the object's bounded canonical space. When paired with a scene-space Point Cloud Map (PCM) from monocular geometry estimation, CCM induces dense canonical-to-scene correspondences from which object transformations are recovered through robust geometric alignment. Because CCM operates in bounded canonical space, it provides a stable prediction target that can be trained from scalable object-level 3D data without requiring scene-level layout annotations. Mira-Scene further introduces a multimodal diffusion transformer that jointly generates object geometry and CCMs, using modality-specific expert streams with shared attention and positional encoding to promote geometry-layout consistency. Experiments on indoor, outdoor, synthetic, and in-the-wild scenes show that Mira-Scene substantially outperforms strong baselines in layout accuracy, achieving relative gains of 39.8% in 3D-IoU and 16.5% in 2D-IoU over SAM3D, using limited open-source training data.

</details>

#### 2026-09-20 - Elevator-VIGS: Separating Elevator Motion from Robot Motion in Visual-Inertial Gaussian Splatting SLAM

**Authors:** Rui Zhou, Zihan Zhu, Wei Zhang, Zizhou Luo, Norbert Haala, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2609.23491) - [pdf](https://arxiv.org/pdf/2609.23491)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** SLAM, bundle adjustment, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Elevator-VIGS: Separating Elevator Motion from Robot Motion in Visual-Inertial Gaussian Splatting SLAM
- 作者：Rui Zhou, Zihan Zhu, Wei Zhang, Zizhou Luo, Norbert Haala, Marc Pollefeys
- 出版日期：2026-09-20T09:26:55Z
- 分类：3D Reconstruction & Multi-view Geometry（主）；Neural Scene Representations & Rendering（次）
- 链接：摘要页 https://arxiv.org/abs/2609.23491 ；PDF https://arxiv.org/pdf/2609.23491 ；项目页 https://ruizhou-cn.github.io/elevator-vigs/

### 一句话总结
提出 Elevator-VIGS，一种视觉-惯性 3D 高斯泼溅 SLAM 系统，通过在电梯坐标系中估计机器人位姿、并将电梯相对世界的运动建模为逐关键帧的运输状态，从而在电梯运行过程中保持跟踪与建图。

### 研究问题
在运动电梯内部，相机与 IMU 的观测存在冲突：相机只看到机器人相对电梯的运动，而 IMU 感知到该运动叠加电梯相对世界的运动。现有视觉-惯性估计器难以处理这一冲突——若视觉主导，估计器只跟踪机器人在电梯内的运动而漏掉电梯上升；若冲突持续存在，估计器会发散。因此论文要解决的是：如何在乘坐电梯的过程中实现不丢失、不发散的视觉-惯性 SLAM 跟踪与建图。

### 核心思路/方法
论文观察到冲突源于将两种观测强行纳入单一坐标系。其做法是：在电梯坐标系中估计机器人位姿，并将电梯相对世界的运动作为逐关键帧的“运输状态”（transport state）——即电梯的上升与垂直速度——纳入稠密的视觉-惯性 bundle adjustment 中。系统使用视觉-语言模型与深度网络以零样本（zero-shot）方式检测电梯乘坐过程，并在出发与到达时刻对运输状态施加约束。

### 主要贡献
- 提出 Elevator-VIGS，可在电梯乘坐过程中持续进行跟踪与建图的视觉-惯性 3D 高斯泼溅 SLAM 系统。
- 提出将机器人位姿置于电梯坐标系、将电梯运动作为逐关键帧运输状态（上升与垂直速度）纳入稠密视觉-惯性 bundle adjustment 的建模方式。
- 利用视觉-语言模型和深度网络实现零样本电梯乘坐检测，并在出发与到达处约束运输状态。
- 采集了真实世界与仿真的电梯序列；在这些序列上取得领先的跟踪与渲染性能，并在四个无电梯的公开基准上保持 VIGS-SLAM 的领先性能。

### 局限性
摘要未提供足够信息。摘要中未给出方法的失败情形、计算开销、对电梯类型或环境的适用范围、零样本检测的准确率、以及真实与仿真实验的具体规模与定量指标等。

### 阅读优先级
中。理由：该工作面向视觉-惯性 SLAM 中一个具体且实际被忽视的场景（移动电梯内的传感器冲突），并给出了清晰的建模思路与系统实现，对从事 SLAM、视觉-惯性里程计与高斯泼溅建图的研究者有直接参考价值；但其创新集中在特定场景的处理机制上，若研究兴趣不涉及视觉-惯性融合或动态平台建图，相关性有限。摘要未提供足够信息来判断其定量提升幅度，因此暂不列为高优先级。

</details>

<details>
<summary>Abstract</summary>

We present Elevator-VIGS, a visual-inertial 3D Gaussian Splatting SLAM system that keeps tracking and mapping through elevator rides. Inside a moving elevator, the two sensors are in conflict. The camera sees only the robot's motion relative to the elevator, while the IMU senses that motion plus the elevator's motion relative to the world. This conflict is challenging for existing visual-inertial estimators. If vision dominates, the estimator tracks only the robot's motion within the elevator and misses the elevator's rise, and if the conflict remains, the estimator diverges. We observe that the conflict comes from forcing both observations into a single coordinate frame. We instead estimate the robot's pose in the elevator's coordinate frame, and the elevator's motion relative to the world as a per-keyframe transport state, the elevator's rise and vertical velocity, within dense visual-inertial bundle adjustment. Elevator-VIGS detects rides zero-shot with a vision-language model and a depth network, and constrains the transport state at the departure and the arrival. We record real-world and simulated elevator sequences. On these sequences, Elevator-VIGS achieves state-of-the-art tracking and rendering performance. On four elevator-free public benchmarks it keeps the state-of-the-art performance of VIGS-SLAM. Project page: https://ruizhou-cn.github.io/elevator-vigs/.

</details>

#### 2026-09-17 - Underwater Visual Target Tracking with Target-Specific Depth Estimation and Adaptive Model-Fusion Predictive Control

**Authors:** Yuheng Zhou, Haiyang Cheng, Yanqi Feng, Pangkit Fong, Mei Xuan Lee, Marcus Gee, Chongrong Fang, Jianping He
**Links:** [abs](https://arxiv.org/abs/2609.20731) - [pdf](https://arxiv.org/pdf/2609.20731)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Underwater Visual Target Tracking with Target-Specific Depth Estimation and Adaptive Model-Fusion Predictive Control
- 作者：Yuheng Zhou, Haiyang Cheng, Yanqi Feng, Pangkit Fong, Mei Xuan Lee, Marcus Gee, Chongrong Fang, Jianping He
- 出版日期：2026-09-17T17:22:01Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2609.20731 ，PDF https://arxiv.org/pdf/2609.20731

### 一句话总结
面向自主水下航行器（AUV），该论文提出一种立体视觉伺服框架，通过目标特定的深度估计与卡尔曼滤波获得稳定三维相对状态，并用自适应模型融合预测控制实现实时平移控制。

### 研究问题
摘要指出，基于视觉的水下目标跟踪面临两个主要挑战：深度测量不可靠，以及目标运动未知。论文即针对这两点，为 AUV 构建水下视觉目标跟踪方案。

### 核心思路/方法
论文方法的要点（均来自摘要）如下：

- 总体框架：为 AUV 提出立体视觉伺服（stereo visual-servoing）框架。
- 感知端：
  - 通过目标特定的深度提取（target-specific depth extraction）和卡尔曼滤波，从立体图像得到稳定的三维相对状态。
  - 利用颜色、视差和时间线索构建目标深度掩码（target-depth mask），以选出可靠的目标像素。
  - 对得到的深度测量和检测到的图像中心分别进行滤波。
- 控制端：
  - 将偏航调节（yaw regulation）与平移控制解耦，从而避免计算开销大的耦合多自由度优化，使实时平移 MPC 成为可能。
  - 平移控制器采用自适应模型融合预测控制，融合恒速（constant-velocity）与零速（zero-velocity）两种目标模型，以适应不同目标运动模式。
  - 依据历史预测误差更新模型权重。
  - 在满足执行机构、跟随距离和视场（field-of-view）约束的条件下计算平移控制指令。
- 验证方式：通过仿真和真实世界实验验证框架有效性，并声称性能优于已有框架。

### 主要贡献
- 提出面向 AUV 的立体视觉伺服跟踪框架。
- 感知上提出目标特定的深度提取方法，结合颜色/视差/时间线索构造目标深度掩码，并对深度与图像中心分别滤波，以缓解水下深度测量不可靠问题。
- 控制上通过偏航与平移解耦，避免昂贵的耦合多自由度优化，实现实时平移 MPC。
- 提出自适应模型融合预测控制，以恒速与零速目标模型的加权融合适应未知目标运动，并由历史预测误差在线更新权重。
- 在控制中显式考虑执行机构、跟随距离与视场约束。
- 通过仿真与真实实验验证，并报告相较现有框架更优的表现。

### 局限性
摘要未提供足够信息。摘要中未给出实验平台细节、数据集或场景规模、对比方法的具体名称与指标数值、失败案例、计算资源与实时性量化结果，也未说明该方法在何种条件下会失效或适用边界。

### 阅读优先级
中。理由：该论文聚焦水下视觉目标跟踪中“深度不可靠 + 目标运动未知”的实际问题，将目标特定深度提取与自适应模型融合 MPC 结合，问题设定清晰、模块划分明确，对水下机器人感知与控制交叉方向有参考价值；但摘要层面未提供量化结果与实验细节，是否值得精读需进一步阅读正文确认其方法新颖度与验证充分性。

</details>

<details>
<summary>Abstract</summary>

Vision-based underwater target tracking is challenged by unreliable depth measurements and unknown target motion. This paper proposes a stereo visual-servoing framework for an autonomous underwater vehicle (AUV). For perception, the framework derives a stable 3D relative state from stereo images through target-specific depth extraction and Kalman filtering. It constructs a target-depth mask from color, disparity, and temporal cues to select reliable target pixels, and then filters the resulting depth measurement and detected image center separately. For control, the framework decouples yaw regulation from translational control, avoiding computationally expensive coupled multi-DOF optimization and enabling real-time translational MPC. The translational controller employs adaptive model-fusion predictive control, combining constant-velocity and zero-velocity target models to accommodate different target-motion patterns. It updates the model weights using historical prediction errors and computes translational commands subject to actuation, following-distance, and field-of-view constraints. Through simulations and real-world experiments, we validate the effectiveness of the proposed framework and show it has better performance than existing frameworks.

</details>

#### 2026-09-17 - Semantic SLAM in Precision Agriculture using Bayesian Inference

**Authors:** Ruben Beumer, Sander Doodeman, René van de Molengraft, Duarte Antunes
**Links:** [abs](https://arxiv.org/abs/2609.20604) - [pdf](https://arxiv.org/pdf/2609.20604)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Semantic SLAM in Precision Agriculture using Bayesian Inference
- 作者：Ruben Beumer, Sander Doodeman, René van de Molengraft, Duarte Antunes
- 出版日期：2026-09-17T15:51:05Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.20604 ；PDF https://arxiv.org/pdf/2609.20604

### 一句话总结
该论文提出一个面向精准农业自主机器人的实时语义世界建模框架，将基于贝叶斯推断的物体及其语义属性概率建图与基于 g²o 的图优化 SLAM 结合，并在仿真与室内人工植物场地实验中用 Spot 机器人验证了实时建图能力。

### 研究问题
如何在精准农业场景中，使自主机器人在不完全依赖 GPS 的情况下，实现准确的建图与定位，同时利用植物类型、大小、健康等语义信息边执行任务边完成自身定位与建图。

### 核心思路/方法
- 构建实时语义世界建模框架，面向精准农业自主机器人。
- 对物体及其语义属性进行概率建图，并通过贝叶斯推断进行更新。
- 与基于图优化的 SLAM 方法结合，具体采用 g²o 这一通用图优化框架实现。
- 该集成使系统在准确建图与定位的同时，不必完全依赖 GPS。
- 利用植物类型、大小、健康等语义信息，支持机器人在作物田中边执行任务边建图与定位。
- 通过 Gazebo 仿真和室内人工植物场地物理实验验证，使用 Boston Dynamics 的机器狗 Spot。
- 训练 YOLOv8n 目标检测模型，从深度相机观测中提取物体和语义数据。

### 主要贡献
- 提出面向精准农业的实时语义世界建模框架，融合概率语义建图与图优化 SLAM。
- 将贝叶斯推断用于物体及其语义属性的更新，并集成 g²o 图优化实现 SLAM。
- 通过仿真与物理实验验证系统可成功实时建图至少 400 株植物。
- 使用 YOLOv8n 从深度相机观测中提取物体与语义数据，支撑语义 SLAM 流程。

### 局限性
- 摘要未提供足够信息说明该方法在真实农田、不同光照与天气条件下的表现。
- 摘要未提供足够信息说明其定位精度、建图精度、实时性指标或与基线方法的定量对比。
- 摘要未提供足够信息说明贝叶斯推断的具体模型形式、计算开销或失败案例。
- 摘要未提供足够信息说明 400 株植物上限之外的可扩展性。
- 摘要未提供足够信息说明 YOLOv8n 检测误差对 SLAM 与语义建图的影响。

### 阅读优先级
中。理由：该论文主题位于语义 SLAM、机器人与精准农业的交叉点，方法组合（贝叶斯推断 + g²o 图优化 + YOLOv8n）和实验平台（Spot、Gazebo、室内人工植物场地）对相关方向有参考价值；但摘要未给出定量结果、精度指标与真实农田验证细节，若需评估实际性能或复现实验，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

This paper presents a real-time semantic world modeling framework specialized for precision agriculture using autonomous robots. The framework combines probabilistic mapping of objects and their semantic attributes, updated through Bayesian inference, with a graph-based Simultaneous Localization and Mapping (SLAM) approach implemented using $g^2o$, a general framework for graph optimization. This integration enables accurate mapping and localization without relying solely on GPS. By leveraging semantic information such as plant type, size, and health, the robot can perform tasks while mapping and localizing itself within a field of crops. The proposed framework was validated through Gazebo simulations and physical experiments on an indoor field with artificial plants using Boston Dynamics' robot dog Spot. A YOLOv8n object detection model was trained to extract object and semantic data from depth camera observations. These simulations and experiments demonstrate that the system can successfully perform real-time mapping of up to at least 400 plants.

</details>

#### 2026-09-17 - RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

**Authors:** Marina Orozco González, Luis Merino
**Links:** [abs](https://arxiv.org/abs/2609.20589) - [pdf](https://arxiv.org/pdf/2609.20589)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, SLAM, visual SLAM, Gaussian Splatting, rendering, radiance, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RawSLAM: Online HDR Gaussian SLAM from Linear Radiance
- 作者：Marina Orozco González, Luis Merino
- 出版日期：2026-09-17T15:41:32Z
- 分类：3D Reconstruction & Multi-view Geometry（主）；Neural Scene Representations & Rendering（次）
- 链接：[摘要页](https://arxiv.org/abs/2609.20589) / [PDF](https://arxiv.org/pdf/2609.20589)

### 一句话总结
论文提出 RawSLAM，据摘要称是首个直接在单次曝光 16 位线性 HDR 图像上进行跟踪与建图的在线高斯 SLAM 框架。

### 研究问题
现有稠密视觉 SLAM 系统几乎只依赖 8 位色调映射后的 LDR 输入，在极端光照下阴影与高光会导致跟踪漂移和建图崩溃；而已有的 raw/HDR 重建流程严格离线，依赖 Structure-from-Motion 预处理，不适用于大帧间运动。

### 核心思路/方法
方法由三个核心组件构成：
1. 架构无关的 HDR 高斯泼溅模块，采用无 MLP 的对数参数化高斯颜色特征；
2. Reinhard 范围压缩的光度目标函数；
3. 结构引导的空间梯度加权。
三者结合使该方法在轨迹与重建精度上优于对 MonoGS 的直接 HDR 适配，并能以线性场景辐射度原生渲染以供后渲染处理。同一形式无需修改即可运行于标准 8 位输入。

### 主要贡献
- 据摘要称，提出首个在线高斯 SLAM 框架，直接在单次曝光 16 位线性 HDR 图像上跟踪与建图。
- 提出三个核心组件：架构无关 HDR 高斯泼溅模块（无 MLP 对数颜色参数化）、Reinhard 范围压缩光度目标、结构引导空间梯度加权。
- 在轨迹与重建精度上优于对 MonoGS 的直接 HDR 适配，并在标准 8 位输入上约为 MonoGS 基线误差的一半。
- HDR 高斯模块可无缝迁移至 SplaTAM、Gaussian SLAM 和 DROID-W，消除这些系统在挑战性光照序列上的全部跟踪失败。
- 引入 RawSLAM 数据集：10 个真实室内序列，含 16 位 RAW 图像、对齐深度、IMU 测量与外部 OptiTrack 位姿。代码与数据集将公开。

### 局限性
- 摘要未提供足够信息说明方法的计算开销、实时性能指标或帧率。
- 摘要未提供足够信息说明数据集规模之外的多样性、场景类型或与其他数据集的跨域泛化表现。
- 摘要未提供足够信息说明在 8 位输入上误差减半的具体实验设定与对比细节。
- 摘要未提供足够信息说明结构引导空间梯度加权的具体实现细节与消融结果。
- 摘要未提供足够信息说明代码与数据集的具体公开时间。

### 阅读优先级
高。理由：该工作针对极端光照下 SLAM 鲁棒性这一明确痛点，提出在线 HDR 高斯 SLAM，并声称在多个现有系统上消除跟踪失败，同时配套发布 16 位 RAW 室内数据集，对 3D 重建、神经渲染与 SLAM 交叉方向具有潜在参考价值。

</details>

<details>
<summary>Abstract</summary>

Current dense visual SLAM systems rely almost exclusively on 8-bit tonemapped Low Dynamic Range (LDR) inputs, limiting their robustness in extreme lighting where shadows and highlights trigger tracking drift and mapping collapse. Conversely, existing raw and High Dynamic Range (HDR) reconstruction pipelines operate strictly offline. They depend on Structure-from-Motion preprocessing and are not suited for large inter-frame motion. We present, to the best of our knowledge, the first online Gaussian SLAM framework that tracks and maps directly on single-exposure 16-bit linear HDR imagery. Our method rests on three core components: an architecture-agnostic HDR Gaussian Splatting module featuring an MLP-free logarithmic parameterization of Gaussian color features; a Reinhard range-compressed photometric objective; and structure-guided spatial gradient weighting. Combined, these components allow our approach to outperform a direct HDR adaptation of MonoGS in both trajectory and reconstruction accuracy, while rendering natively in linear scene radiance for post-rendering processing. The same formulation runs unchanged on standard 8-bit inputs, roughly halving the MonoGS baseline error. Furthermore, our HDR Gaussian module transfers seamlessly to SplaTAM, Gaussian SLAM, and DROID-W, eliminating all tracking failures these systems suffer on challenging illumination sequences. To enable this research, we introduce RawSLAM: a dataset of 10 real-world indoor sequences featuring 16-bit RAW imagery, aligned depth, IMU measurements, and external OptiTrack poses. Code and dataset will be made publicly available soon.

</details>

#### 2026-09-17 - SLAMSqueezeBench: Comparing SLAM Systems under Resource Constraints

**Authors:** Mohamed Hefny, Karthik Dantu, Steven Y. Ko
**Links:** [abs](https://arxiv.org/abs/2609.19533) - [pdf](https://arxiv.org/pdf/2609.19533)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, Gaussian Splatting, splatting, manipulation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SLAMSqueezeBench: Comparing SLAM Systems under Resource Constraints
- 作者：Mohamed Hefny, Karthik Dantu, Steven Y. Ko
- 出版日期：2026-09-17T00:59:01Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.19533 ；PDF https://arxiv.org/pdf/2609.19533

### 一句话总结
论文提出 SLAMSqueezeBench，一个在边缘硬件上对 SLAM 系统施加计算与内存资源约束，并模拟有限缓冲下相机丢帧的测试框架，用于比较九种 SLAM 系统。

### 研究问题
SLAM 通常是自主机器人上运行的服务之一，用于辅助规划、操作等任务，这些任务都运行在边缘硬件上并受到严重资源约束。但大多数 SLAM 系统是在隔离环境中构建和测试的，其性能报告仿佛它是系统上唯一运行的任务。作者观察到，现有基准缺乏在真实资源约束下比较 SLAM 系统的通用机制。

### 核心思路/方法
作者开发了 SLAMSqueezeBench，该框架允许在边缘硬件的真实工作负载下测试 SLAM 系统。其做法是在执行期间对 SLAM 系统可用的计算和内存资源施加约束。它还模拟真实的相机帧采集过程，当有限缓冲区满时会发生丢帧。作者使用 SLAMSqueezeBench 比较了九种 SLAM 系统，涵盖经典系统、基于学习的系统以及用于高斯泼溅的方法。

### 主要贡献
- 指出并针对现有基准缺乏在真实资源约束下比较 SLAM 系统的通用机制这一问题。
- 提出 SLAMSqueezeBench 框架，可在边缘硬件上以真实工作负载测试 SLAM 系统。
- 该框架通过对执行期间的可用计算和内存资源施加约束，并模拟有限缓冲满时丢帧的真实相机帧采集。
- 使用该框架比较了九种 SLAM 系统，涵盖经典系统、基于学习系统和高斯泼溅方法。
- 作者表示该测试框架将在论文发表后供社区使用。

### 局限性
摘要未提供足够信息说明具体资源约束的设置、边缘硬件平台、九种系统的具体名称、评价指标、实验结论、框架开销或适用范围限制。摘要未提供足够信息说明该框架是否覆盖其他资源类型或更广泛机器人任务场景。

### 阅读优先级
中。理由：该工作针对 SLAM 评测中资源约束这一实际且常被忽视的问题，并提出可比较多类 SLAM 系统的框架，对边缘机器人、SLAM 评测和具身应用研究者有参考价值；但摘要未给出具体实验设置、指标和结论，是否具有强实证说服力需阅读全文后才能判断。

</details>

<details>
<summary>Abstract</summary>

Simultaneous localization and mapping (SLAM) is one of the services running on an autonomous robot. It is typically run to assist other tasks such as planning, manipulation, etc. All these tasks are run on edge hardware and are subject to severe resource constraints. However, most SLAM systems are built and tested in isolation, and their performance is reported as if they are the only task running on a system. We observe that existing benchmarks lack a common mechanism for comparing SLAM systems under realistic resource constraints. To address this limitation, we have developed SLAMSqueezeBench, a framework that allows testing of SLAM systems under realistic workloads on edge hardware. It does so by imposing constraints on compute and memory resources available for the SLAM system during execution. It also simulates realistic camera frame acquisition with frame drops when a finite buffer is full. Using SLAMSqueezeBench, we compare nine SLAM systems spanning classical systems, learning-based systems, and approaches for Gaussian splatting. Our testing framework will be available for use by the community upon publication.

</details>

#### 2026-09-17 - AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend

**Authors:** Hengyi Wang, Lourdes Agapito
**Links:** [abs](https://arxiv.org/abs/2609.19518) - [pdf](https://arxiv.org/pdf/2609.19518)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend
- 作者：Hengyi Wang, Lourdes Agapito
- 出版日期：2026-09-17T00:11:16Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供足够信息
- 链接：abstract_url: https://arxiv.org/abs/2609.19518；pdf_url: https://arxiv.org/pdf/2609.19518

### 一句话总结
AMB3R-SLAM 是一个可在单块消费级 GPU 上实时运行的单目 SLAM 系统，通过轻量前端与分层后端实现万帧级、公里级轨迹重建，并能自然处理动态场景，还可扩展至双目、RGB-D 与 LiDAR 输入。

### 研究问题
论文关注的是实时单目 SLAM 在超长序列、公里级轨迹和 10k 帧规模下的重建与跟踪问题，同时试图避免依赖静态世界假设的 bundle adjustment，从而处理复杂动态场景。

### 核心思路/方法
方法由轻量前端和分层后端组成：前端用于低延迟在线跟踪；后端按局部、中层和全局层级逐步施加一致性约束。该系统避免使用依赖静态世界假设的 bundle adjustment，因此可自然应对复杂动态场景。作者还说明该方法可扩展到利用双目、RGB-D 和 LiDAR 作为额外输入。

### 主要贡献
- 提出 AMB3R-SLAM，一个能在单块消费级 GPU 上实时运行、在 10k 帧上重建公里级轨迹的单目 SLAM 系统。
- 设计轻量前端与分层后端结合的结构，后端逐步强制局部、中层与全局一致性。
- 避免依赖静态世界假设的 bundle adjustment，使系统可直接处理复杂动态场景。
- 展示方法可扩展至双目、RGB-D 和 LiDAR 额外输入。
- 在 9 个数据集上取得较强的相机跟踪性能，并在 VBR 与 Oxford Spires 上将先前最先进方法的绝对轨迹误差降低超过 70%；加入 LiDAR 输入后，在 KITTI 与 VBR 上将 ATE 进一步降至亚米级。

### 局限性
摘要未提供足够信息。论文未在摘要中说明失败场景、计算资源具体配置、实时性指标细节、各数据集上的完整定量结果或方法对额外输入的依赖程度等局限。

### 阅读优先级
高。理由：该工作面向公里级、万帧规模的实时单目 SLAM，提出分层后端并规避静态世界假设，且在多个数据集上报告了显著 ATE 降低；主题属于 3D 重建与多视图几何中的核心问题，具有较强的方法与系统参考价值。

</details>

<details>
<summary>Abstract</summary>

We present AMB3R-SLAM, a real-time monocular SLAM system capable of reconstructing kilometer-scale trajectories over 10k frames on a single consumer-grade GPU. Our model couples a lightweight front-end for low-latency online tracking with a hierarchical backend that progressively enforces local, mid-level, and global consistency. By avoiding bundle adjustment that relies on the static world assumption, our system naturally handles complex dynamic scenes out of the box. Furthermore, we demonstrate that our method can be extended to leverage stereo, RGB-D, and LiDAR as additional inputs. AMB3R-SLAM achieves strong camera tracking performance across 9 datasets, reducing the absolute trajectory error (ATE) of previous state-of-the-art methods on VBR and Oxford Spires by over 70%. With additional LiDAR input, our model further reduces ATE to sub-meter level on KITTI and VBR datasets.

</details>

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-22 - φ-RIE: From Photorealistic Reconstruction to Interactive Environments

**Authors:** Runyi Yang, Deheng Zhang, Xiaoye Wang, Kanzhi Wu, Lei Sun, Ajad Chhatkuli, Kunyu Peng, Luc Van Gool, Danda Pani Paudel
**Links:** [abs](https://arxiv.org/abs/2609.26795) - [pdf](https://arxiv.org/pdf/2609.26795)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, manipulation, simulation

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) can reconstruct a captured scene photorealistically, but the resulting representation does not by itself support physical interaction. Robot simulation instead requires object-level change, \textit{i.e.}, objects must move independently, make contact, and reveal previously occluded surroundings. This gap arises because object appearance may remain entangled with the background, while hidden object geometry and occluded background content may be unobserved. To address this challenge, we present φ-RIE, a Gaussian-native pipeline that converts selected objects into movable simulator assets while preserving the remaining reconstruction. Our key observation is that asset construction and source removal should be coupled, \textit{i.e.}, one object identity should define the movable asset and the scene content to remove and complete. Accordingly, Scene Observation supplies shared evidence to Coupled Scene Construction, which creates registered assets and completed background Gaussians for simulator-driven rendering in an Interactive Environment. This coupling preserves unedited Gaussians while aligning visual and physical state. On 50 ScanNet++ scenes, evidence-based selection and registration retry increase matched F1 at 20\,mm from 0.336 to 0.383 at fixed retention. Further tests demonstrate asset executability, manipulation gains over a single-generator baseline, and the visual cost of conversion. Together, these results demonstrate that \name\ enables interactive scene conversion.

</details>

#### 2026-09-22 - Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models

**Authors:** Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan
**Links:** [abs](https://arxiv.org/abs/2609.26007) - [pdf](https://arxiv.org/pdf/2609.26007)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation, world model

<details>
<summary>Abstract</summary>

Monocular drone navigation requires reaching a goal in an unseen environment from a single forward-facing camera, which offers few cues for depth and scale. World models address this by modelling how observations evolve under actions, but they are built to be executed: the prediction is produced at deployment and fed back into action generation at every control step. We argue that what a policy needs from a world model is not the prediction but the representation required to produce it: in flight the executed action explains almost all of the change between observations, so prediction reduces to reprojecting a static scene under a known displacement. We therefore introduce skytopia, a policy built on an action-conditioned latent world model, and the 3D Gaussian Splatting platform on which it is trained. A forward objective predicts the representation of the next observation from the intended motion, and an inverse objective recovers that motion from the predicted transition. Because the prediction never reaches action generation, the predictor is discarded and one policy serves point-goal, image-goal, and goal-free navigation. Simulation experiments show that skytopia outperforms every baseline under all three specifications, attaining 57.8%, 66.0%, and 49.0% success rate, while discarding the predictor removes 59.4% of the inference cost. The same policy is subsequently deployed on a physical drone without fine-tuning and reaches goals in indoor, open outdoor, and woodland environments.

</details>

#### 2026-09-22 - GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration

**Authors:** Karim Slimani, Catherine Achard, Eric Marchand, Brahim Tamadazte
**Links:** [abs](https://arxiv.org/abs/2609.25966) - [pdf](https://arxiv.org/pdf/2609.25966)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dense correspondence, rendering, splatting

<details>
<summary>Abstract</summary>

This paper introduces GRIP, a pose-conditioned refinement framework for pixel-to-point matching and 2D to 3D registration. Given an initial coarse pose estimate, GRIP addresses the structural mismatch between grid based image descriptors and unordered point cloud descriptors by softly rendering learned 3D point features onto the image grid through Gaussian feature splatting. The rendered point derived feature map is then fused with image features by a pixel aligned transformer, enabling visual semantic and geometric cues to interact in a shared 2D representation. The refined features are decoded and propagated to finer resolutions for dense correspondence estimation and final pose refinement. Experiments on RGB D Scenes V2 and 7 Scenes demonstrate state of the art inlier ratio and competitive registration recall, with stronger performance under stricter evaluation thresholds.

</details>

#### 2026-09-22 - NaCR: Visual Localization via NeRF-aided Camera Ray Regression

**Authors:** Yesheng Zhang, Xiang Dai, Xu Zhao, Chongyang Zhang
**Links:** [abs](https://arxiv.org/abs/2609.25907) - [pdf](https://arxiv.org/pdf/2609.25907)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** NeRF, novel view synthesis, view synthesis, rendering, radiance, mapping, localization, virtual reality

<details>
<summary>Abstract</summary>

Visual localization (VL) is a fundamental technology for vision applications such as virtual reality. Recently, a novel VL paradigm, Camera Ray Regression (CRR), has emerged, which maps 2D image patches to 3D camera rays, but its accuracy is limited. To improve CRR accuracy, we notice a compelling duality: the inverse of this mapping is inherently performed by the novel view synthesis model, \ie, Neural Radiance Fields (NeRF). While NeRF renders image patches from camera rays via differentiable ray marching, CRR predicts the rays from image patches. Motivated by this complementary relationship, we propose NeRF-aided Camera Ray Regression (NaCR), a unified framework that seamlessly bridges NeRF and CRR at the ray level. First, NaCR incorporates three simple yet effective enhancements into the CRR baseline. Second, leveraging a pre-trained NeRF, NaCR augments the training data by synthesizing novel views tailored for efficient, patch-level consumption. Finally, exploiting the differentiability of NeRF, NaCR forms a closed-loop supervision pipeline where photometric rendering errors are back-propagated to optimize the predicted camera rays. To ensure stable convergence within the highly non-convex image space, we introduce a two-stage training curriculum. Extensive experiments across indoor and outdoor benchmarks demonstrate that NaCR achieves competitive accuracy. Comprehensive ablation studies validate the efficacy of each proposed component.

</details>

#### 2026-09-22 - Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking

**Authors:** Edward Beng Wai Tan, Siew-Kei Lam
**Links:** [abs](https://arxiv.org/abs/2609.25746) - [pdf](https://arxiv.org/pdf/2609.25746)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

ICP-based 3D Gaussian Splatting (3DGS) SLAM tracks in real time by registering incoming frames against map Gaussians, using each primitive's covariance for both rendering and registration. These two uses place conflicting demands on one covariance. The mapper shapes it to minimize photometric error, often flattening it against surfaces, while robust registration typically benefits from measurement uncertainty. We propose a dual-covariance parameterization. Each Gaussian keeps a single mean but holds two covariances: a rendering covariance optimized by the mapper, and a tracking covariance derived from an RGB-D sensor noise model. We further use the tracking covariances as Gaussian anchors for image corners, providing constraints in directions where depth geometry is weak. We evaluate on TUM RGB-D, ScanNet, Replica, and two outdoor sequences recorded with a RealSense D435i on wheeled and handheld platforms. We achieve robust tracking performance across multiple scenes and reduced odometry drift, while tracking at $\sim$ 60 FPS.

</details>

#### 2026-09-22 - Ultra-fast Neural Inference for Stochastic Gaussian Splatting Denoising

**Authors:** Chenxiao Hu, Hao Zhang, Yanchen Zhang, Meng Gai, Guoping Wang, Sheng Li
**Links:** [abs](https://arxiv.org/abs/2609.25604) - [pdf](https://arxiv.org/pdf/2609.25604)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Stochastic rendering eliminates the sorting and alpha blending process in Gaussian splatting, at the cost of introducing spatial noise. Formulating temporal denoising over the pixel stream shared by view-consistent stochastic splatting renderers, we propose a temporal neural denoiser validated on stochastic 2D Gaussian Splatting rendering, combining dual-path exponential moving average accumulation, per-pixel learned trust prediction for history validation, a fixed anisotropic spatial filter and a variance-gated composition with stabilization. The denoiser suppresses the noise, achieving temporally stable, visually compelling outputs during free camera navigation, all while retaining the sort-free, blend-free rasterization performance. The combined pipeline retains a PSNR gap to sorted alpha-blending renderers, but the denoiser's overhead stays below the time saved by removing sorting and blending.

</details>

#### 2026-09-21 - OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones

**Authors:** Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao
**Links:** [abs](https://arxiv.org/abs/2609.24253) - [pdf](https://arxiv.org/pdf/2609.24253)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones
- 作者：Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao
- 出版日期：2026-09-21T08:17:56Z
- 分类：主分类为 Neural Scene Representations & Rendering；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.24253；PDF https://arxiv.org/pdf/2609.24253

### 一句话总结
OpenFlyScan 是一个面向消费级无人机的质量引导航拍重建系统，通过预测 3DGS 区域重建质量并规划补采航带，以移动应用执行补采，从而降低大规模城市资产构建的成本与返工。

### 研究问题
摘要指出，3DGS 虽能为大规模具身仿真提供高保真场景，但构建大规模城市资产仍受制于昂贵设备和延迟的质量反馈。预设的航测方案可能导致复杂表面观测不足，缺陷往往在重建完成后才被发现，进而需要返场重飞和重复处理。因此，问题在于：如何在使用消费级无人机、不增加机载硬件的条件下，提前预测重建质量差区域，并针对性地补采数据以改善重建结果。

### 核心思路/方法
摘要给出的方法包含三个组成部分：
1. **GS 质量模型**：从 GS 渲染误差中学习，用于预测区域性的重建质量。
2. **重采规划器（reacquisition planner）**：基于质量预测，生成互补的补采航带（complementary reacquisition strips）。
3. **定制移动应用**：执行补采航带，并支持自动化倾斜摄影（automated oblique surveys）与数据传输，且不需要在无人机上搭载额外硬件。

整体流程将采集、针对性补采与重建整合在一起，形成质量引导的闭环。

### 主要贡献
- 提出 OpenFlyScan，一个面向消费级无人机的质量引导航拍重建系统，集成 GS 质量模型、重采规划器和定制移动应用。
- 质量模型可从 GS 渲染误差中学习并预测区域重建质量，摘要称其在真实航拍场景中能有效识别可能重建不佳的区域。
- 规划器可基于质量预测生成互补补采航带，并通过移动应用执行，无需额外机载硬件。
- 在 Expo West 现场实验中，针对性补采使额外视角下的 PSNR 提升 10.95 dB。
- 摘要称代码与模型将在 https://openflyscan.github.io/ 公开。

### 局限性
- 摘要未提供足够信息说明质量模型的泛化能力、训练数据规模与场景覆盖范围。
- 摘要未提供足够信息说明重采规划器的计算开销、实时性或对飞行安全的考虑。
- 摘要未提供足够信息说明除 Expo West 外其他真实场景的定量结果。
- 摘要未提供足够信息说明系统对无人机型号、传感器或飞行环境的依赖与限制。
- 摘要未提供足够信息说明与现有航测或重建方法的完整对比。
- 摘要未提供足够信息说明移动应用的具体平台、数据传输方式与自动化倾斜摄影的实现细节。

### 阅读优先级
**中**。理由：该工作面向消费级无人机的大规模城市 3DGS 重建，提出质量预测加针对性补采的闭环系统，并给出了 PSNR 提升 10.95 dB 的现场实验结果，对航拍重建、3DGS 数据采集和具身仿真资产构建方向有参考价值。但摘要篇幅有限，未披露方法细节、泛化性与对比实验，是否值得深入阅读取决于读者对质量引导采集或消费级无人机航测系统的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) provides high-fidelity scenes for large-scale embodied simulation, but constructing large-scale urban assets remains constrained by expensive equipment and delayed quality feedback. Preset surveys can leave complex surfaces insufficiently observed, with defects discovered only after reconstruction, requiring return visits and repeated processing. We present OpenFlyScan, a quality-guided aerial reconstruction system for consumer drones that integrates a GS quality model, a reacquisition planner, and a custom-designed mobile app. The model learns from GS rendering errors to predict regional reconstruction quality. Based on these predictions, the planner then generates complementary reacquisition strips to be executed through the app, which also supports automated oblique surveys and data transfer without additional hardware on board. Across real aerial scenes, the model effectively identifies regions that are likely to be poorly reconstructed. In the Expo West field experiment, targeted reacquisition improves PSNR at additional views by 10.95 dB. With consumer drones, OpenFlyScan integrates capture, targeted reacquisition, and reconstruction to support rapid, low-cost urban asset creation. Code and models will be made publicly available at https://openflyscan.github.io/.

</details>

#### 2026-09-21 - BayesianGS-SLAM: Uncertainty-Aware Neural Rendering SLAM via Probabilistic Formulation

**Authors:** Kyeongsu Kang, Seongbo Ha, Sibaek Lee, Hyeonwoo Yu
**Links:** [abs](https://arxiv.org/abs/2609.24140) - [pdf](https://arxiv.org/pdf/2609.24140)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, neural rendering, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BayesianGS-SLAM: Uncertainty-Aware Neural Rendering SLAM via Probabilistic Formulation
- 作者：Kyeongsu Kang, Seongbo Ha, Sibaek Lee, Hyeonwoo Yu
- 出版日期：2026-09-21T05:48:17Z
- 分类：Primary: Neural Scene Representations & Rendering；Secondary: 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2609.24140 ；PDF https://arxiv.org/pdf/2609.24140

### 一句话总结
该论文提出 BayesianGS-SLAM，一种基于 3D Gaussian Splatting 的不确定性感知 SLAM 框架，通过估计并复用颜色与深度的预测不确定性，将不确定性同时用于建图、跟踪和关键帧选择。

### 研究问题
论文关注的问题是：基于神经渲染的 SLAM 依赖渲染得到的 RGB-D 残差进行相机跟踪和地图优化，但这些预测的可靠性会因传感器噪声、观测覆盖有限以及地图表示不完整而发生显著变化。若缺乏显式可靠性估计，不可靠残差可能损害位姿优化，而当前地图已能很好解释的帧又可能触发冗余的建图更新。

### 核心思路/方法
论文提出 BayesianGS-SLAM，在 3D Gaussian Splatting SLAM 框架中估计建图过程中的预测颜色不确定性和深度不确定性，并在整个 SLAM 流程中一致地复用该不确定性。其可处理概率公式结合了两类不确定性成分：传感器噪声不确定性，以及由不透明度引发、并通过渲染过程传播的地图表示不确定性。由此得到的预测不确定性被用于三个方面：增强建图、通过鲁棒位姿目标归一化跟踪残差、以及使用基于预测惊讶度的关键帧准则评估新进入帧。与主要考虑颜色不确定性或仅在建图阶段使用不确定性的已有不确定性感知神经渲染 SLAM 方法不同，该框架同时估计颜色和深度的预测不确定性，并将其整合进建图、跟踪和关键帧选择。

### 主要贡献
- 提出 BayesianGS-SLAM，一个不确定性感知的 3D Gaussian Splatting SLAM 框架，估计建图过程中的预测颜色和深度不确定性，并在 SLAM 流程中一致复用。
- 给出可处理的概率公式，将传感器噪声不确定性成分与不透明度引发的地图表示不确定性成分结合，并通过渲染过程传播。
- 将预测不确定性用于增强建图、通过鲁棒位姿目标归一化跟踪残差，以及基于预测惊讶度的关键帧选择。
- 在真实世界 RGB-D 数据集上的评估显示，与现有不确定性感知 SLAM 方法相比，深度不确定性-误差排序有显著改善；所提出的关键帧选择策略减少了所选关键帧数量和建图调用次数，同时保持有竞争力的跟踪和渲染性能。

### 局限性
- 摘要未提供足够信息说明方法在更大规模场景、不同传感器类型或极端噪声条件下的泛化能力。
- 摘要未提供足够信息说明计算开销、实时性以及不确定性估计本身带来的额外成本。
- 摘要未提供足够信息说明与更多非不确定性感知 SLAM 基线方法的全面比较结果。
- 摘要未提供足够信息说明失败案例、消融实验细节以及各不确定性成分的具体贡献。

### 阅读优先级
中。理由：该论文主题位于神经渲染 SLAM、3D Gaussian Splatting 与不确定性建模的交叉点，问题定义清晰，且声称在深度不确定性排序和关键帧效率上有改进。但摘要未提供足够信息展示完整实验细节、计算代价和泛化性，因此对需要深入评估方法实用性的读者而言，优先级为中等；若研究兴趣集中在不确定性感知 SLAM 或 3DGS SLAM，则可优先阅读。

</details>

<details>
<summary>Abstract</summary>

Neural-rendering-based SLAM relies on rendered RGB-D residuals for camera tracking and map optimization, but the reliability of these predictions can vary substantially because of sensor noise, limited observation coverage, and incomplete map representations. Without an explicit reliability estimate, unreliable residuals may adversely affect pose optimization, while frames already well explained by the current map may trigger redundant mapping updates. In this paper, we present BayesianGS-SLAM, an uncertainty-aware 3D Gaussian Splatting SLAM framework that estimates predictive color and depth uncertainty during mapping and consistently reuses it across the SLAM pipeline. Our tractable probabilistic formulation combines a sensor-noise uncertainty component with an opacity-induced map-representation component propagated through the rendering process. The resulting predictive uncertainty is used to augment mapping, normalize tracking residuals through a robust pose objective, and evaluate incoming frames using a predictive-surprise-based keyframe criterion. Unlike prior uncertainty-aware neural-rendering SLAM methods that primarily consider color uncertainty or use uncertainty only during mapping, our framework estimates predictive uncertainty for both color and depth and integrates it into mapping, tracking, and keyframe selection. Evaluations on real-world RGB-D datasets demonstrate substantially improved depth uncertainty-error ranking compared with existing uncertainty-aware SLAM methods. Moreover, the proposed keyframe-selection strategy reduces the number of selected keyframes and mapping calls while maintaining competitive tracking and rendering performance.

</details>

#### 2026-09-20 - GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting

**Authors:** Hongfei Zhu, Haochen Deng, Sitao Zhang, Ling Zhou
**Links:** [abs](https://arxiv.org/abs/2609.23436) - [pdf](https://arxiv.org/pdf/2609.23436)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting
- 作者：Hongfei Zhu, Haochen Deng, Sitao Zhang, Ling Zhou
- 出版日期：2026-09-20T08:13:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.23436 ；PDF：https://arxiv.org/pdf/2609.23436

### 一句话总结
该论文提出一种交替优化框架，利用预训练图像扩散模型生成几何一致的伪视角，并通过主动伪视角选择与多重约束机制，提升稀疏视角下 3D Gaussian Splatting 的新视角合成质量。

### 研究问题
从稀疏观测进行新视角合成存在严重的欠约束问题。3D Gaussian Splatting 虽能实现实时渲染，但在少视角训练时会产生漂浮物、几何破碎和背景发白等问题。论文关注的是：如何为稀疏视角 3DGS 训练提供额外且可靠的监督信号，以缓解这些退化现象。

### 核心思路/方法
论文提出一个交替优化框架，使用预训练图像扩散模型为 3DGS 生成几何一致的伪视角，作为额外监督。生成过程受到以下约束：深度条件 ControlNet、IP-Adapter 风格迁移、LoRA 场景适配以及 img2img 结构锚定。

核心组件是 Generative Active Pseudo-view Selection（GAPS），用于在选择目标视角时平衡重建信息量与生成可靠性。其退火调度策略从训练早期的保守插值逐渐转向后期的探索性外推，以逐步覆盖未观测区域。此外，方法采用双准则准入门和不确定性加权损失来拒绝不可靠生成，并使用密度自适应 DropGaussian 减少复杂场景中的过拟合。

### 主要贡献
- 提出交替优化框架，利用预训练扩散模型为稀疏视角 3DGS 生成额外伪视角监督。
- 提出 GAPS（Generative Active Pseudo-view Selection），通过退火调度在保守插值与探索性外推之间切换，以覆盖未观测区域。
- 引入双准则准入门与不确定性加权损失，以过滤不可靠生成。
- 引入密度自适应 DropGaussian，以缓解复杂场景的过拟合。
- 在 LLFF 的 3/6/9 视角设置上，相较 vanilla 3DGS 平均 PSNR 分别提升 0.40/0.89/0.70 dB；在 Mip-NeRF 360 的 12/24 视角设置上提升 1.18/0.80 dB；所有设置中 SSIM 提升、LPIPS 下降。
- 消融实验表明主动选择与密度自适应正则化均为必要；仅在完整方法下，无界 360 度场景中的 LPIPS 才能低于无伪视角基线。

### 局限性
摘要未提供足够信息。摘要中未说明方法的计算开销、生成模型推理成本、对更极端稀疏视角的适用性、不同扩散模型选择的影响，也未给出失败案例或对伪视角质量的直接定量评估。因此无法基于摘要判断其局限。

### 阅读优先级
高。理由：该论文针对稀疏视角 3DGS 的欠约束这一明确且重要的问题，提出了较完整的生成式伪视角监督框架，并在两个常用数据集上报告了多视角设置的一致增益，且包含消融验证关键组件必要性。对于关注 3DGS、稀疏视角新视角合成、扩散先验与主动数据选择交叉方向的研究者，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis from sparse observations is severely under-constrained. Although 3D Gaussian Splatting (3DGS) enables real-time rendering, it produces floaters, broken geometry, and washed-out backgrounds when trained with few views. We propose an alternating optimization framework that uses a pre-trained image diffusion model to generate geometrically consistent pseudo-views for additional 3DGS supervision. Generation is constrained by depth-conditioned ControlNet, IP-Adapter style transfer, LoRA scene adaptation, and img2img structural anchoring. We introduce Generative Active Pseudo-view Selection (GAPS) to balance reconstruction informativeness and generative reliability when choosing target views. Its annealing schedule shifts from conservative interpolation early in training to exploratory extrapolation later, gradually covering unobserved regions. A dual-criterion admission gate and uncertainty-weighted losses reject unreliable generations, while density-adaptive DropGaussian reduces overfitting in complex scenes. On LLFF with 3/6/9 views, our method improves average PSNR over vanilla 3DGS by 0.40/0.89/0.70 dB. On Mip-NeRF 360 with 12/24 views, the gains are 1.18/0.80 dB. SSIM improves and LPIPS decreases in every setting. Ablations show that active selection and density-adaptive regularization are both necessary; only the full method reduces LPIPS below the no-pseudo-view baseline on unbounded 360-degree scenes.

</details>

#### 2026-09-20 - LiteTex-GS: Fast and Lightweight Texturing for Gaussian Splatting

**Authors:** Zhiwei Li, Yijia Guo, Yishi Lu, Liwen Hu, Hong Rao, Shengbo Chen, Lei Ma
**Links:** [abs](https://arxiv.org/abs/2609.23380) - [pdf](https://arxiv.org/pdf/2609.23380)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LiteTex-GS: Fast and Lightweight Texturing for Gaussian Splatting
- 作者：Zhiwei Li, Yijia Guo, Yishi Lu, Liwen Hu, Hong Rao, Shengbo Chen, Lei Ma
- 出版日期：2026-09-20T06:00:47Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.23380 ；PDF: https://arxiv.org/pdf/2609.23380

### 一句话总结
LiteTex-GS 提出一种快速轻量的高斯泼溅纹理化框架，通过紧凑初始化、渐进式纹理分辨率分配、贡献与面积感知剪枝以及分辨率感知更新规则，缓解纹理化高斯方法在细节表现与计算效率之间的矛盾。

### 研究问题
高斯泼溅能够实现实时新视角合成，但其几何与外观表示紧密耦合，往往需要大量基元来复现高频纹理细节，导致显著的内存与优化成本。近期带纹理的 2D 高斯方法通过为高斯基元附加纹理图来缓解该限制，但离散高斯与连续 2D 网格之间存在结构差异，需要复杂参数化，带来严重计算开销，从而损害高斯泼溅原有的效率。因此，如何在精细纹理与计算敏捷性之间取得平衡仍未解决。

### 核心思路/方法
- 初始化一种极其紧凑的表示，为每个高斯分配最小的局部纹理。
- 仅对重建误差显著的基元逐步分配更高分辨率纹理。
- 引入贡献与面积感知的剪枝策略，剔除低效用高斯，以保持精简的几何骨架。
- 设计分辨率感知更新规则，缓解纹理上采样造成的梯度稀释问题，保持快速稳定收敛。

### 主要贡献
- 提出 LiteTex-GS，一种面向高斯泼溅的快速、轻量纹理化框架。
- 通过紧凑初始化与按重建误差渐进分配更高分辨率纹理，减少不必要的纹理参数。
- 提出贡献与面积感知剪枝策略，去除低效用高斯。
- 提出分辨率感知更新规则，以缓解纹理上采样导致的梯度稀释。
- 在标准新视角合成基准上的大量实验表明，与现有纹理化高斯基线相比，该方法在使用显著更少参数和更少训练时间的同时，达到有竞争力或更优的渲染质量。

### 局限性
摘要未提供足够信息。摘要未说明具体数据集、评价指标、消融实验细节、失败场景、计算资源需求或与其他非纹理化高斯方法的全面比较，因此无法基于摘要判断其局限性。

### 阅读优先级
高。理由：该论文针对高斯泼溅中纹理化效率与细节平衡这一明确痛点，提出轻量化纹理框架，并声称在标准新视角合成基准上以更少参数和更少训练时间取得有竞争力或更优的渲染质量，对神经场景表示与实时渲染方向具有较高相关性和潜在实用价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has enabled real-time novel view synthesis, but its tightly coupled geometry and appearance representation often require a large number of primitives to reproduce high-frequency texture details, leading to substantial memory and optimization costs. Recent textured 2D Gaussian methods alleviate this limitation by attaching texture maps to Gaussian primitives. However, bridging the fundamental structural gap between discrete Gaussians and continuous 2D grids requires complex parameterizations that introduce severe computational overhead. This overhead fundamentally compromises the original efficiency of Gaussian Splatting, making the balance between detailed texturing and computational agility an unresolved challenge. To address these challenges, we propose LiteTex-GS, a fast and lightweight texturing framework for Gaussian Splatting. Our method initializes an extremely compact representation, assigning minimal local texture to each Gaussian and progressively allocates higher resolution only to primitives with significant reconstruction errors. To maintain a streamlined geometric scaffold, we introduce a contribution- and area-aware pruning strategy that eliminates low-utility Gaussians. Furthermore, to mitigate the gradient dilution caused by texture upsampling, we design a resolution-aware update rule that preserves rapid and stable convergence. Extensive experiments on standard novel view synthesis benchmarks demonstrate that our method achieves competitive or superior rendering quality while using substantially fewer parameters and less training time than existing textured Gaussian baselines.

</details>

#### 2026-09-19 - GrapeSplat: Geometry-Grounded Reconstruction via Amalgamated Pose-Free Encoding for Feed-Forward 3D Gaussian Splatting

**Authors:** Si-Yu Lu, Yung-Yao Chen, Yi Jan Chen, Shang-Lin Li, Ching-Chan Liao, Wen-Huang Cheng
**Links:** [abs](https://arxiv.org/abs/2609.23182) - [pdf](https://arxiv.org/pdf/2609.23182)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GrapeSplat: Geometry-Grounded Reconstruction via Amalgamated Pose-Free Encoding for Feed-Forward 3D Gaussian Splatting
- 作者：Si-Yu Lu, Yung-Yao Chen, Yi Jan Chen, Shang-Lin Li, Ching-Chan Liao, Wen-Huang Cheng
- 出版日期：2026-09-19T19:11:37Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.23182) / [PDF](https://arxiv.org/pdf/2609.23182) / [代码与权重](https://github.com/VAISR/GrapeSplat)

### 一句话总结
GrapeSplat 通过将多视角线索融合为体素对齐的场景表示，并从学习到的稀疏网格直接解码 3D 高斯，实现无需姿态、无需逐场景优化的前馈式可渲染场景重建。

### 研究问题
摘要指出，现有的前馈式 3D Gaussian Splatting 虽已能从无姿态、未标定图像重建可渲染场景，但存在两个问题：
1. 多数模型仅以光度一致性作为监督，且逐像素预测高斯，导致全局结构脆弱；
2. 高斯基元数量与图像分辨率和视角数量绑定。

因此，论文关注如何在前馈框架下增强全局结构、解除高斯基元数量对分辨率和视角数的依赖，并避免逐场景优化或后处理。

### 核心思路/方法
GrapeSplat 将多视角线索融合为体素对齐的场景表示，并直接从学习到的网格解码高斯，无需逐场景优化或后处理。具体包含：
- **Atlas Encoder**：将所有视角提升为以预测 3D 点为锚点的逐像素几何与外观特征；
- **PEACH-Vox**：通过平滑的逐轴映射及其精确闭式逆映射，将无界场景压缩到有界稀疏网格；
- **Sparse Decoder**：使用稀疏卷积整合网格，并将整个场景解码为每个被占据单元对应多个高斯。

该融合表示利用稀疏体素占用：高斯数量随被占据单元变化，并在视角覆盖场景时趋于饱和，而网格分辨率决定其上限。GrapeSplat 在单次前向传播中将无姿态图像转化为可渲染的高斯场景。训练使用 8 视角序列上的 2D 和 3D 监督，可在室内和无界场景中从 4 到 64 视角进行零样本泛化。

### 主要贡献
- 提出 GrapeSplat，一种无需姿态、无需逐场景优化或后处理的前馈式 3D Gaussian Splatting 方法。
- 设计 Atlas Encoder，将多视角提升为锚定于预测 3D 点的逐像素几何与外观特征。
- 提出 PEACH-Vox，将无界场景通过平滑逐轴映射压缩到有界稀疏网格，并提供精确闭式逆映射。
- 采用 Sparse Decoder，通过稀疏卷积整合网格并解码为每个被占据单元多个高斯，使高斯数量与图像分辨率和视角数解耦。
- 在 8 视角序列上以 2D 和 3D 监督训练后，实现从 4 到 64 视角在室内与无界场景中的零样本泛化。
- 公开代码与训练权重链接。

### 局限性
- 摘要未提供足够信息说明方法在极端视角、动态场景、透明或反光物体等困难条件下的表现。
- 摘要未提供足够信息说明训练数据规模、具体数据集名称及定量指标。
- 摘要未提供足够信息说明计算开销、推理速度或显存占用。
- 摘要未提供足够信息说明与现有方法的详细对比结果。
- 摘要未提供足够信息说明失败案例或鲁棒性边界。

### 阅读优先级
**高**。理由：该论文聚焦无姿态前馈式 3D Gaussian Splatting 的结构化表示问题，提出体素对齐的融合表示与稀疏解码思路，直击逐像素预测导致全局结构脆弱、基元数量与分辨率和视角数绑定的痛点；且摘要明确给出从 4 到 64 视角的零样本泛化声明，并公开代码与权重，便于复现与验证。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting now reconstructs renderable scenes from unposed, uncalibrated images. Yet, most models supervise only photometric consistency and predict Gaussians pixel by pixel, which leaves global structure fragile and ties primitive count to image resolution and view count. To this end, GrapeSplat amalgamates multi-view cues into a voxel-aligned scene representation and decodes Gaussians directly from the learned grid, requiring no per-scene optimization or post-processing. An Atlas Encoder lifts all views into pixel-wise geometry-and-appearance features anchored at predicted 3D points. PEACH-Vox compands the unbounded scene into a bounded sparse grid through a smooth per-axis map with an exact closed-form inverse. The Sparse Decoder then consolidates the grid with sparse convolutions and decodes the full scene as multiple Gaussians per occupied cell. This amalgamated representation exploits sparse voxel occupancy, where the Gaussian count follows the occupied cells and saturates as views cover the scene, while grid resolution sets its ceiling. GrapeSplat turns unposed images into a renderable Gaussian scene in a single forward pass. Trained with 2D and 3D supervision on 8-view sequences, it generalizes zero-shot from 4 to 64 views across indoor and unbounded scenes. Code and trained weights are available at https://github.com/VAISR/GrapeSplat

</details>

#### 2026-09-17 - SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos

**Authors:** Peiyu Liu, Dingxi Zhang, Federico Tombari, Marc Pollefeys, Christina Tsalicoglou, Daniel Barath
**Links:** [abs](https://arxiv.org/abs/2609.20818) - [pdf](https://arxiv.org/pdf/2609.20818)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic Gaussian, Gaussian Splatting, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos
- 作者：Peiyu Liu, Dingxi Zhang, Federico Tombari, Marc Pollefeys, Christina Tsalicoglou, Daniel Barath
- 出版日期：2026-09-17T17:59:41Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.20818

### 一句话总结
本文针对飞溅液体难以重建的问题，构建了真实多视角飞溅液体基准数据集，并提出 SplashSplat——一种“仅在观测可约束处施加物理结构”的表示方法，在真实与合成基准上优于现有动态高斯泼溅方法，且训练成本更低。

### 研究问题
飞溅液体存在时间极短：液片会撕裂成液丝与液滴，外观具有视角依赖性且几乎无纹理，且几乎没有能持久追踪的特征。因此，重建研究此前主要集中于烟雾、合成液体或缓慢形变的表面。据作者所述，目前尚不存在同步多视角的飞溅液体数据集，真实飞溅液体的重建缺乏数据与有效方法。

### 核心思路/方法
方法建立在单一原则之上：仅在观测能够约束的地方施加物理结构。具体包括：
- 由掩码融合得到的逐帧液体 SDF 提供几何；
- 在相邻 SDF 之间进行水平集传输，得到粗略速度场；
- 沿该流场推进拉格朗日载体（Lagrangian carriers），每个新观测对其进行修正，并在覆盖丢失处重新播种；
- 最终解码为局部高斯，用于可微渲染。

### 主要贡献
1. 提出据作者所知尚不存在的同步多视角飞溅液体基准：20 个真实场景，从连贯水流到剧烈飞溅，由七台同步标定的 4K 相机以 60 fps 采集，并提供人工精修的各视角液体与容器掩码以及固定评测划分。
2. 提出 SplashSplat 方法，基于上述“仅在可约束处施加物理结构”的原则，结合掩码融合 SDF、水平集传输、拉格朗日载体推进与局部高斯解码。
3. 在真实采集数据与合成基准上，SplashSplat 优于当前最先进的动态高斯泼溅方法，运动在物理上更合理且训练成本更低。同一表示还支持无需重新优化的时间插值与风格迁移。

### 局限性
摘要未提供足够信息。摘要中未说明方法的失败情形、适用边界、对掩码精度的依赖程度、计算与内存开销的具体限制，或基准数据集本身的覆盖不足等局限。

### 阅读优先级
高。理由：该工作同时贡献了此前缺失的真实飞溅液体多视角基准数据集与对应重建方法，问题设定（极短时、无纹理、视角依赖、难以追踪的液体）具有明显挑战性与新颖性，且声称在真实与合成基准上均优于现有动态高斯泼溅方法并降低训练成本，对动态场景重建、神经渲染与流体相关视觉研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

A splash lives for a fraction of a second: sheets tear into ligaments and droplets, appearance is view-dependent and nearly textureless, and little persists long enough to track. Reconstruction research has consequently focused on smoke, synthetic liquids, or gently deforming surfaces. To our knowledge, no synchronized multi-view dataset of splashing liquids exists. We therefore introduce a benchmark of 20 real scenes, from coherent streams to violent splashes, captured by seven synchronized, calibrated 4K cameras at 60 fps, with manually refined per-view liquid and container masks and fixed evaluation splits. We further present SplashSplat, built on a single principle: impose physical structure only where the observations can constrain it. Per-frame liquid SDFs fused from the masks provide the geometry, level-set transport between consecutive SDFs yields a coarse velocity field, and Lagrangian carriers advected along this flow, corrected against each new observation and reseeded where coverage is lost, decode local Gaussians for differentiable rendering. SplashSplat outperforms state-of-the-art dynamic Gaussian splatting methods on our real captures and on a synthetic benchmark, with physically more plausible motion and a lower training cost. The same representation supports temporal interpolation and style transfer without re-optimization.

</details>

#### 2026-09-17 - PhGS: Post-Hoc Pruning and Refinement of Single-View Feed-Forward 3D Gaussian Reconstructions

**Authors:** Rinto Yagawa, Han Cheng, Dieter Schmalstieg, Hideo Saito, Shohei Mori
**Links:** [abs](https://arxiv.org/abs/2609.20623) - [pdf](https://arxiv.org/pdf/2609.20623)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PhGS: Post-Hoc Pruning and Refinement of Single-View Feed-Forward 3D Gaussian Reconstructions
- 作者：Rinto Yagawa, Han Cheng, Dieter Schmalstieg, Hideo Saito, Shohei Mori
- 出版日期：2026-09-17T16:07:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.20623) / [PDF](https://arxiv.org/pdf/2609.20623)

### 一句话总结
针对单视图前馈 3DGS 生成中因每条相机射线预测固定数量高斯而导致的空间冗余，提出一种骨干无关的后处理压缩流程：冻结基模型，通过重要性分数剪枝与轻量循环精修模块迭代恢复图像质量。

### 研究问题
单视图前馈 3D Gaussian Splatting（3DGS）生成方法会在每条相机射线上预测固定数量的高斯，从而引入严重的空间冗余。现有的大多数压缩（compaction）策略面向多视图设置，依赖跨视图一致性，因而与单图像模型不兼容。论文要解决的核心问题是：在不重新训练基础前馈网络的前提下，如何压缩单视图前馈 3DGS 生成的冗余高斯表示。

### 核心思路/方法
论文的关键思路是保持基础模型冻结，对生成的高斯施加后处理剪枝与循环精修，而非重新训练前馈网络直接输出紧凑表示。具体地，提出一个骨干无关的压缩流程，包含两个耦合组件：
1. 基于重要性分数的剪枝机制；
2. 可训练的轻量循环精修模块，用于迭代更新存活下来的基元（primitives）以恢复图像质量。
此外，方法支持在推理时灵活设定保留比例（keep ratios）以适应不同应用需求。

### 主要贡献
- 提出骨干无关（backbone-agnostic）的单视图前馈 3DGS 压缩流程。
- 将基于重要性分数的剪枝与可训练轻量循环精修模块相结合，在压缩后迭代恢复图像质量。
- 无需重新训练基础前馈网络，可无缝集成现有基线方法。
- 在保持新视图渲染保真度的同时实现较高的内存缩减。
- 支持推理时灵活的保留比例设置。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集、基线对比对象及定量指标。
- 摘要未提供足够信息说明重要性分数的具体定义与剪枝细节。
- 摘要未提供足够信息说明精修模块的架构、训练代价与推理开销。
- 摘要未提供足够信息说明保留比例的可调范围及其对质量与内存的定量影响。
- 摘要未提供足够信息说明方法在何种失败情形或边界条件下表现受限。

### 阅读优先级
中。理由：该工作面向单视图前馈 3DGS 的冗余压缩这一具体且实际的问题，提出冻结基模型 + 后处理剪枝与精修的思路，具备与现有基线解耦、推理时可调保留比例等实用特性；但摘要未给出定量结果与实验细节，是否在保真度与压缩率上具有显著优势尚无法从摘要判断，因此对关注 3DGS 压缩与单视图重建方向的读者具有中等参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent single-view feed-forward 3D Gaussian Splatting (3DGS) generation predicts a fixed number of Gaussians per camera ray, introducing severe spatial redundancy. Most existing compaction strategies target multi-view setups to exploit cross-view consistency and are incompatible with single-image models. Instead of retraining the base feed-forward network to directly output compact representations, our insight is to keep the base models frozen and apply post-hoc pruning and recurrent refinement to the generated Gaussians. Consequently, we propose a backbone-agnostic compaction pipeline for single-view feed-forward 3DGS that couples an importance-score-based pruning mechanism with a trainable, lightweight recurrent refinement module, which iteratively updates the surviving primitives to restore image quality. Our results demonstrate seamless integration with existing baselines while preserving novel-view rendering fidelity and achieving high memory reduction. Furthermore, our method supports flexible inference-time keep ratios for application needs.

</details>

#### 2026-09-17 - CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding

**Authors:** Zhikun Zhou, Kunyu Peng, Runyi Yang, Junhao Cai, Di Wen, Ruiping Liu, Danda Pani Paudel, Yi Zhou, Luc Van Gool, Kailun Yang
**Links:** [abs](https://arxiv.org/abs/2609.20586) - [pdf](https://arxiv.org/pdf/2609.20586)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding
- 作者：Zhikun Zhou, Kunyu Peng, Runyi Yang, Junhao Cai, Di Wen, Ruiping Liu, Danda Pani Paudel, Yi Zhou, Luc Van Gool, Kailun Yang
- 出版日期：2026-09-17T15:39:25Z
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（次）
- 链接：[摘要](https://arxiv.org/abs/2609.20586) / [PDF](https://arxiv.org/pdf/2609.20586)

### 一句话总结
CoRef-GS 面向多机器人协同场景，提出在独立重建并融合后的高斯地图上完成"指代式"语义定位与视角关系推理的框架，并配套发布双四足机器人基准 CoQuad-Ref。

### 研究问题
具身机器人的指代式场景理解需要从指定视角对以物体为中心和以关系为中心的语言查询进行定位。单个智能体的局部语义高斯地图可以支持这种定位，但在协同场景下，地图由各智能体独立重建后再对齐融合，此时被指代的目标或作为上下文参照的地标可能来自其他智能体的观测，而空间关系仍需从发起查询的机器人视角来解释。论文将该问题形式化为"融合地图上的协同指代高斯定位"，并指出其需要满足三个条件：几何可对齐性、实例级语义可比性、以及视角条件化的关系推理。现有语言感知高斯方法多聚焦单地图查询，而高斯配准方法仅优化几何或光度对齐，不保留面向语言定位的语义兼容性。

### 核心思路/方法
CoRef-GS 包含三个环节：首先构建局部开放词汇、实例感知的高斯地图；随后通过跨智能体对齐模块，以几何与语义一致性对部分重叠的地图进行对齐；最后使用视角条件化的掩码关系图（view-conditioned mask relation graph）完成查询定位。论文同时提出 CoQuad-Ref，一个覆盖真实世界与仿真室内场景的双四足机器人基准。

### 主要贡献
- 提出协同指代高斯定位问题设定：在独立重建并对齐融合的地图上，处理可能跨智能体来源的目标与地标，同时保持查询机器人的视角关系解释。
- 提出 CoRef-GS 框架，包含开放词汇实例感知局部高斯地图构建、几何与语义一致性驱动的跨智能体对齐模块，以及视角条件化掩码关系图的查询定位。
- 提出 CoQuad-Ref 双四足机器人基准，覆盖真实与仿真室内场景。
- 实验报告：仿真场景中旋转误差从粗初始化后的 2.58° 降至细化后的 0.15°；真实世界指代 mIoU 相比 ReferSplat 从 52.6% 提升至 68.8%。
- 承诺公开基准与源代码（https://github.com/ruojiruoli17/CoRef-GS.git）。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败情形、对重叠程度的敏感性、计算开销、智能体数量上限，也未给出仿真场景指代精度等其他指标，亦未说明基准的规模与数据构成细节。

### 阅读优先级
高。理由：该工作同时涉及多智能体协同、语言指代定位与高斯泼溅交叉方向，提出新问题设定、新方法、新基准并给出量化改进；但判断是否与自身研究直接相关，仍需摘要未提供的实验设置与数据细节。

</details>

<details>
<summary>Abstract</summary>

Referring scene understanding for embodied robots requires grounding object- and relation-centric language queries from a designated viewpoint. While a local semantic Gaussian map can support such grounding within one agent's observations, cooperative settings require this ability to remain effective after independently reconstructed maps are aligned and fused. In this setting, the referred target or its contextual landmark may come from another agent's observations, while spatial relations must still be interpreted from the querying robot's viewpoint. We formulate this problem as cooperative referring Gaussian grounding over fused maps, which requires geometric alignability, instance-level semantic comparability, and view-conditioned relation reasoning. Existing language-aware Gaussian methods mainly focus on single-map querying, whereas Gaussian registration methods optimize geometric or photometric alignment without preserving language-grounding-oriented semantic compatibility. We propose CoRef-GS, a cooperative referring Gaussian splatting framework. CoRef-GS constructs local open-vocabulary instance-aware Gaussian maps, then aligns partially overlapping maps with a cross-agent alignment module by geometric and semantic consistency, and grounds queries using a view-conditioned mask relation graph. We further introduce CoQuad-Ref, a dual-quadruped benchmark spanning both real-world and simulated indoor scenes. Experiments show that, on simulated scenes, CoRef-GS reduces the rotation error from 2.58° after coarse initialization to 0.15° after refinement, and improves real-world referring mIoU over ReferSplat from 52.6% to 68.8%. The established benchmark and source code will be publicly released at https://github.com/ruojiruoli17/CoRef-GS.git.

</details>

#### 2026-09-17 - EliGSiR: Continual RGB-D Mapping with Gaussian Splatting under Bounded Compute

**Authors:** Björn Ellensohn, Elmar Rueckert, Christian Rauch
**Links:** [abs](https://arxiv.org/abs/2609.20348) - [pdf](https://arxiv.org/pdf/2609.20348)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EliGSiR: Continual RGB-D Mapping with Gaussian Splatting under Bounded Compute
- 作者：Björn Ellensohn, Elmar Rueckert, Christian Rauch
- 出版日期：2026-09-17T13:12:49Z
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：[摘要](https://arxiv.org/abs/2609.20348) / [PDF](https://arxiv.org/pdf/2609.20348)

### 一句话总结
EliGSiR 是一个面向在线 RGB-D 连续建图的持续高斯泼溅映射器，通过视图调度、自适应监督分辨率和定向几何增长，在有限算力预算下持续更新并保留已重建区域。

### 研究问题
传统 3D Gaussian Splatting 假设观测集合封闭且优化流程较长；而连续 RGB-D 建图要求新观测在线到达，同时必须保留此前已重建的区域，因此需要解决如何在计算预算受限且地图持续演化的条件下分配优化资源的问题。

### 核心思路/方法
论文提出 EliGSiR（Evidence-guided Load-adaptive Incremental Gaussian Splatting with Image Replay），一种持续高斯映射器，控制随重建演化而变化的优化预算使用方式，包含三个机制：
- Map-Guided View Scheduling：过滤冗余的 incoming views，并根据地图当前状态重新考虑保留的视图；
- Load-Adaptive Fidelity：根据当前建图负载调整监督分辨率，而非遵循固定分辨率计划；
- Targeted Geometry Growth：将深度监督与高斯创建分离，仅在重复 RGB-D 观测表明结构缺失或错位处增加几何容量。
这些机制在建图活跃期间共同自适应决定优化哪些视图、使用多少图像细节以及在哪里扩展表示。

### 主要贡献
- 提出 EliGSiR 持续高斯映射框架，面向在线到达观测与已重建区域保留的需求，在有限算力预算下自适应使用优化资源。
- 设计 Map-Guided View Scheduling、Load-Adaptive Fidelity 与 Targeted Geometry Growth 三项机制，分别控制视图优化选择、监督细节程度和几何容量增长位置。
- 在 Replica、TUM RGB-D、ScanNet++ 以及真实 RGB-D 传感器序列上进行评估，同时考虑最终重建结果与采集过程中的地图状态。
- 在 TUM RGB-D fr3/long_office_household 上，使用与受控基线相同的地面真值建图位姿时达到 21.52 dB，而 SplaTAM 为 19.42 dB；在跟踪位姿比较中，使用实时 ORB-SLAM3 位姿的 EliGSiR 在 155.5 s 内达到 23.02 dB，而 CaRtGS 使用其原生跟踪器在 230.9 s 内为 20.10 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对连续 RGB-D 建图中的在线观测、有限算力与地图保留问题，提出可操作的自适应优化机制，并在多个数据集与真实传感器序列上给出定量对比，对神经场景表示与机器人/AR 应用方向均有参考价值。

</details>

<details>
<summary>Abstract</summary>

Conventional 3D Gaussian Splatting assumes a closed set of observations and long optimization schedules. Continual RGB-D mapping in contrast poses the problem that new observations arrive online, while previously reconstructed regions must be preserved. We present EliGSiR (Evidence-guided Load-adaptive Incremental Gaussian Splatting with Image Replay), a continual Gaussian mapper that controls how the available optimization budget is used as the reconstruction evolves. Map-Guided View Scheduling filters redundant incoming views and reconsiders retained views according to the current state of the map. Load-Adaptive Fidelity adjusts supervision resolution to the current mapping load instead of following a fixed resolution schedule. Targeted Geometry Growth separates depth supervision from Gaussian creation and adds geometric capacity only where repeated RGB-D observations indicate missing or misplaced structure. Together, these mechanisms adapt which views are optimized, how much image detail is used, and where the representation grows while mapping remains active. We evaluate EliGSiR on Replica, TUM RGB-D, ScanNet++, and real RGB-D sensor sequences, considering both the final reconstruction and the map available throughout acquisition. On TUM RGB-D fr3/long_office_household, EliGSiR reaches 21.52 dB with the same ground-truth mapping poses used by the controlled baselines, compared with 19.42 dB for SplaTAM. In the tracked-pose comparison, EliGSiR with live ORB-SLAM3 poses reaches 23.02 dB in 155.5 s, compared with 20.10 dB in 230.9 s for CaRtGS using its native tracker. We further evaluate reconstruction throughout acquisition and show how EliGSiR adaptive view scheduling, supervision fidelity, and geometry growth improve the use of the available mapping budget.

</details>

#### 2026-09-17 - GS-PI: An Optimization-Decoupled Appearance Decomposition Approach for Generating PBR Gaussian Assets

**Authors:** Jieting Xu, Rengan Xie, Zijian Huang, Zehui Jin, Rui Wang, Yuchi Huo
**Links:** [abs](https://arxiv.org/abs/2609.19907) - [pdf](https://arxiv.org/pdf/2609.19907)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, inverse rendering, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-PI: An Optimization-Decoupled Appearance Decomposition Approach for Generating PBR Gaussian Assets
- 作者：Jieting Xu, Rengan Xie, Zijian Huang, Zehui Jin, Rui Wang, Yuchi Huo
- 出版日期：2026-09-17T08:51:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.19907) / [PDF](https://arxiv.org/pdf/2609.19907)

### 一句话总结
GS-PI 提出一种优化解耦的框架，将 PBR 材质生成建模为 3D 点云上以几何为条件的扩散过程，从而把 Gaussian Splatting 模型转换为可重新光照的 PBR-GS 资产。

### 研究问题
Gaussian Splatting 在新视角合成上表现优异，但其编码的是“烘焙”后的辐射度，光照与几何紧密耦合，难以无缝接入基于物理的渲染（PBR）管线。现有逆渲染方法尝试通过联合优化解耦材质，但常因目标相互竞争而出现严重歧义与残留光照伪影。

### 核心思路/方法
论文将 PBR 材质生成重新表述为 3D 点云上以几何为条件的扩散过程，直接在 3D 域中操作，从而天然保证多视角一致性，规避 2D 扩散方法面临的像素对应问题。方法引入多尺度跨视角条件机制，整合三类互补信息：全局语义先验、以源视角为锚定的光度线索、以及绝对空间学习视角方向条件信号。整体流程为：从预训练 Gaussian 模型中提取点云，通过条件扩散预测 PBR 属性，再经由可微光栅化蒸馏回 Gaussian 表示，最终得到完全可重新光照的 PBR-GS 资产。

### 主要贡献
- 提出优化解耦框架 GS-PI，将 PBR 材质生成建模为几何条件下的 3D 点云扩散过程，避免联合优化中的目标竞争与歧义。
- 直接在 3D 域操作，保证多视角一致性，规避 2D 扩散方法的像素对应难题。
- 设计多尺度跨视角条件机制，融合全局语义先验、源锚定光度线索与绝对空间学习视角方向信号，压缩复杂多视角证据，缓解跨视角投影错位，并防止镜面高光被烘焙进本征颜色。
- 以“学习式扩散 + 短程目标驱动蒸馏”替代逐场景的联合光照/BRDF 优化，且无需代理网格。
- 摘要声称其性能优于近期逆渲染基线。

### 局限性
摘要未提供足够信息。论文摘要未给出具体实验设置、失败案例、计算开销、数据依赖或泛化边界等细节，因此无法基于所给材料判断其局限。

### 阅读优先级
中。理由：该工作针对 Gaussian Splatting 与 PBR 管线衔接的关键痛点，提出优化解耦与 3D 扩散相结合的思路，对神经渲染与逆渲染方向有参考价值；但摘要未提供实验细节与定量结果，且发布时间较新，需阅读全文才能评估其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting (GS) excels at novel-view synthesis but encodes baked-in radiance, tightly entangling illumination with geometry and preventing seamless integration into physically based rendering (PBR) pipelines. Existing inverse-rendering methods attempt to disentangle materials via joint optimization, but often suffer from competing objectives that cause severe ambiguities and residual lighting artifacts. To overcome this, we present GS-PI, a novel optimization-decoupled framework that casts PBR material generation as a geometry-conditioned diffusion process on 3D point clouds. By operating directly in the 3D domain, our method inherently guarantees multi-view consistency, sidestepping the severe pixel correspondence issues that challenge 2D diffusion approaches. We introduce a multi-scale cross-view conditioning mechanism that integrates three complementary components: a global semantic prior, source-anchored photometric cues, and an absolute spatial learned view-direction conditioning signal. This design efficiently compresses complex multi-view evidence, mitigating cross-view projection misalignment and successfully preventing specular highlights from baking into intrinsic colors. By extracting a point cloud from a pre-trained Gaussian model, predicting PBR attributes via conditional diffusion, and distilling them back through differentiable rasterisation, we yield a fully relightable PBR-GS asset. GS-PI outperforms recent inverse-rendering baselines while replacing per-scene joint illumination/BRDF optimization with a learned diffusion pass followed by a short target-driven distillation, without requiring proxy meshes.

</details>

#### 2026-09-17 - Printing the Underdetermined: Materializing Multi-solutionness in Figurative Paintings

**Authors:** Yutao Ming, Teng Xu, Youjia Wang, Yunyang Liu, Fengmin Yang, Fuqiang Zhao, Jingyi Yu, Hua Yang, Yanjun Zhou
**Links:** [abs](https://arxiv.org/abs/2609.19782) - [pdf](https://arxiv.org/pdf/2609.19782)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Printing the Underdetermined: Materializing Multi-solutionness in Figurative Paintings
- 作者：Yutao Ming, Teng Xu, Youjia Wang, Yunyang Liu, Fengmin Yang, Fuqiang Zhao, Jingyi Yu, Hua Yang, Yanjun Zhou
- 出版日期：2026-09-17T06:50:54Z
- 分类：Neural Scene Representations & Rendering（Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2609.19782 ；PDF：https://arxiv.org/pdf/2609.19782

### 一句话总结
论文针对具象绘画被当作单一可恢复三维场景这一常规假设，提出将“多解性”（与单幅绘画相容的多种三维配置）显式保留、重建并通过 DreamPrinting 实体化的工作流程。

### 研究问题
常规做法把具象绘画视为描绘了一个单一可恢复的三维场景：观看者推断深度与遮挡，重建流程试图收敛到一个稳定模型。论文要处理的核心问题是这种“唯一解”假设忽略了多解性。摘要指出多解性来自两方面：
- 未观测内容：背面和被遮挡体积允许多种合理补全；
- 已观测线索：透视、明暗和遮挡仍然对几何约束不足。
当使用视频生成模型在无显式三维约束下合成额外视角时，帧级的小漂移是不可避免的，而非例外。

### 核心思路/方法
- 从一幅绘画中采样多个相机环绕的多视角视频序列。
- 对每个序列用 3D Gaussian Splatting 重建为基于点的 Gaussian 场景表示。
- 在该表示中，密度光晕（density halos）与鬼影（ghosting）被用来暴露未解决的自由度。
- 使用 DreamPrinting 将这些表示制作成物理实体。
- 整体上把多种相容解释作为显式输出，而不是当作残差误差来处理。

### 主要贡献
- 提出并突出“多解性”（multi-solutionness）概念，即与单幅绘画相容的三维配置的非唯一性，并将其保持为可见、可物质化的对象。
- 提出一条工作流程：单幅绘画 → 多个相机环绕多视角视频序列 → 3D Gaussian Splatting → 显式暴露未解自由度的 Gaussian 场景表示 → DreamPrinting 实体化。
- 将多种相容解释视为显式输出而非误差，为具象绘画的空间解读提供一个可在数字与物理形式中检视、比较和讨论的计算框架。

### 局限性
摘要未提供足够信息。摘要中未给出定量实验结果、用户研究、方法失败案例、计算成本、生成视频数量或实体化的具体精度限制等细节。

### 阅读优先级
中。理由：论文提出了一个较有新意的视角（把多解性作为显式输出并实体化），涉及视频生成、3D Gaussian Splatting 与 DreamPrinting 的组合流程，对神经场景表示与渲染、计算艺术/绘画空间解读交叉方向有参考价值；但摘要未提供实验验证细节与定量结论，实际价值需进一步阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

Figurative paintings are often approached as if they depict a single recoverable 3D scene: viewers infer depth and occlusion, and reconstruction pipelines attempt to converge to one stable model. We instead foreground multi-solutionness, the non-uniqueness of 3D configurations compatible with a single painted image, and propose a workflow that keeps this non-uniqueness visible and material. Multi-solutionness arises from two sources: unobserved content, where backsides and occluded volumes admit multiple plausible completions, and observed cues, where perspective, shading, and occlusion still underconstrain geometry. When additional views are synthesized by a video generative model without explicit 3D constraints, small frame-level drifts become inevitable rather than exceptional. Our pipeline samples multiple camera-orbit multi-view video sequences from one painting, reconstructs each sequence with 3D Gaussian Splatting into a point-based Gaussian scene representation where density halos and ghosting expose unresolved degrees of freedom, and fabricates these representations as physical artifacts using DreamPrinting. By treating multiple compatible interpretations as explicit outputs rather than residual error, we provide a computational framework for spatial readings of figurative painting that can be inspected, compared, and discussed in both digital and physical form.

</details>

#### 2026-09-17 - GAPrompt++: Multi-Granular Geometry-Aware Point Cloud Prompt for 3D Vision Model

**Authors:** Zixiang Ai, Zhenyu Cui, Yufei Guo, Wenwen Qiang, Lei Chen, Jiwen Lu, Jiahuan Zhou
**Links:** [abs](https://arxiv.org/abs/2609.19716) - [pdf](https://arxiv.org/pdf/2609.19716)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view stereo, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GAPrompt++: Multi-Granular Geometry-Aware Point Cloud Prompt for 3D Vision Model
- 作者：Zixiang Ai, Zhenyu Cui, Yufei Guo, Wenwen Qiang, Lei Chen, Jiwen Lu, Jiahuan Zhou
- 出版日期：2026-09-17T05:14:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.19716) | [PDF](https://arxiv.org/pdf/2609.19716)

### 一句话总结
GAPrompt++ 提出一种多粒度、几何感知的点云提示（prompting）方法，用于以极低可训练参数代价将预训练 3D 视觉模型高效适配到下游任务，并构建了两个更具挑战性的点云评测基准。

### 研究问题
预训练 3D 视觉模型虽推动了点云分析的发展，但通过全量微调适配下游任务在计算和存储上代价高昂。参数高效微调（PEFT）是潜在的替代方案，然而现有基于提示（prompting）的方法忽略了点云内在的几何结构，具体表现为：既无法同时编码细粒度几何线索与粗粒度结构语义，也无法在模型层级中有效传播这些信息，从而限制了适配能力。

### 核心思路/方法
针对上述问题，论文提出 GAPrompt++，一种多粒度几何感知的提示方法，为高效的 3D 任务适配提供更丰富的几何引导，由三个组件构成：
1. **Point Shift Prompter（点偏移提示器）**：在不同尺度上提取多粒度几何特征，从而在适配过程中实现实例特定的几何调整。
2. **Keypoint Prompter（关键点提示器）**：自适应地生成点级别的提示，以突出局部几何显著性和细粒度结构细节。
3. **Prompt Propagation（提示传播）机制**：将上述多粒度几何线索注入整个特征提取层级，增强捕获关键几何特征的能力。

### 主要贡献
- 提出 GAPrompt++，一种多粒度几何感知的提示方法，为高效 3D 任务适配提供更丰富的几何引导。
- 设计 Point Shift Prompter、Keypoint Prompter 与 Prompt Propagation 三个组件，分别处理多尺度几何调整、点级局部显著性提示与层级信息传播。
- 实验表明，GAPrompt++ 在基于提示的 PEFT 方法中达到 state-of-the-art，并在多个基准上超越全量微调，同时可训练参数少于 2%。
- 针对现有评测数据集趋于饱和的问题，构建了两个分别源自 3D Gaussian Splatting 与 Multi-View Stereo 重建的更具挑战性基准，以提供多样且真实的点云场景，推动未来研究。

### 局限性
- 具体实验设置、数据集名称、对比方法与数值结果：摘要未提供足够信息。
- 两个新基准的规模、标注方式与评价协议：摘要未提供足够信息。
- 方法在具体下游任务（如分类、分割、检测等）上的适用范围：摘要未提供足够信息。
- 少于 2% 可训练参数的具体计算口径与模型规模：摘要未提供足够信息。

### 阅读优先级
高。理由：该工作聚焦 3D 视觉模型的高效适配这一实际问题，同时给出方法（多粒度几何感知提示）与评测资源（两个新基准）两方面贡献；且摘要声称在多个基准上超越全量微调且可训练参数少于 2%，属于值得优先验证的结论性主张。

</details>

<details>
<summary>Abstract</summary>

Pre-trained 3D vision models have substantially advanced point cloud analysis, yet adapting them to downstream tasks via full fine-tuning is computationally expensive and storage-intensive. Parameter-Efficient Fine-Tuning (PEFT) offers a promising alternative by reducing both adaptation cost and storage burden. However, existing prompting-based approaches ignore the intrinsic geometric structures of point clouds, thereby limiting their adaptation capability. This limitation stems from their inability to encode both fine-grained geometric cues and coarse-grained structural semantics, as well as failing to propagate such information effectively through the model hierarchy. To address these challenges, we propose GAPrompt++, a multi-granular geometry-aware prompting method that provides richer geometric guidance for efficient 3D task adaptation. Specifically, we introduce a Point Shift Prompter that extracts multi-granular geometric features across different scales, enabling instance-specific geometric adjustments during adaptation. Next, a Keypoint Prompter adaptively generates point-level prompts to highlight local geometric saliency and fine-grained structural details. Furthermore, a Prompt Propagation mechanism injects these multi-granular geometric cues throughout the feature extraction hierarchy, strengthening the ability to capture essential geometric characteristics. Extensive experiments show that GAPrompt++ achieves state-of-the-art performance among prompting-based PEFT methods and even surpasses full fine-tuning across diverse benchmarks, while requiring less than 2\% trainable parameters. In addition, to address the saturation of existing evaluation datasets, we construct two more challenging benchmarks derived from 3D Gaussian Splatting and Multi-View Stereo reconstruction, offering diverse and realistic point cloud scenarios to promote future research.

</details>

#### 2026-09-16 - ParticleSplat: Self-supervised Object-centric Latent Particle Splatting

**Authors:** Lyuxing He, Daniel Guo, Elizabeth Terveen, Deepak Pathak, David Held, Tal Daniel
**Links:** [abs](https://arxiv.org/abs/2609.19463) - [pdf](https://arxiv.org/pdf/2609.19463)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** geometric reasoning, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ParticleSplat: Self-supervised Object-centric Latent Particle Splatting
- 作者：Lyuxing He, Daniel Guo, Elizabeth Terveen, Deepak Pathak, David Held, Tal Daniel
- 出版日期：2026-09-16T22:05:05Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.19463) | [PDF](https://arxiv.org/pdf/2609.19463)

### 一句话总结
ParticleSplat 将 Deep Latent Particles 的 2D 潜在粒子扩展到 3D 潜在粒子空间，借助前馈 3D 高斯泼溅与视图合成目标，实现自监督的以物体为中心的场景分解。

### 研究问题
DLP 框架虽能以粒子（含位置、尺度、视觉外观等属性）表示图像，但其本质是 2D 的，无法进行显式的 3D 空间与几何推理，而这对于机器人操作等下游任务至关重要。论文旨在解决这一 2D 局限。

### 核心思路/方法
- 利用潜在粒子与 3D 高斯基元之间的结构相似性，构建 3D 潜在粒子空间，并以新颖视图合成目标进行训练。
- 模型将带相机位姿的多视图联合编码到一个共享的 3D 以物体为中心的潜在空间中。
- 随后把粒子转换为与粒子对齐的 3D 高斯，通过其组合重建完整场景。
- 训练方式为自监督。

### 主要贡献
- 提出 ParticleSplat，一种基于前馈 3D 高斯泼溅的自监督、以物体为中心的学习方法，把场景分解为表示语义实体的潜在“粒子”集合。
- 将 DLP 的 2D 粒子表示扩展为 3D 潜在粒子空间，并引入新颖视图合成目标进行训练，使模型具备显式 3D 空间与几何推理能力。
- 在模拟与真实世界数据集上表明，该形式能无监督地学到物体掩码。
- 支持可控的 3D 场景编辑，例如通过在潜在空间中修改粒子来移动物体。
- 表明所学 3D 表示提升了机器人操作任务的下游性能。

### 局限性
- 具体实验设置、数据集名称、评价指标与定量结果：摘要未提供足够信息。
- 物体掩码“无监督学到”的验证方式与精度：摘要未提供足够信息。
- 3D 场景编辑的操作细节与定性/定量表现：摘要未提供足够信息。
- 机器人操作任务的具体类型、提升幅度与对比基线：摘要未提供足够信息。
- 方法的计算开销、训练规模与失效场景：摘要未提供足够信息。

### 阅读优先级
中。理由：该工作处于以物体为中心的表示学习与神经场景表示/渲染的交叉点，将 DLP 扩展到 3D 并结合 3D 高斯泼溅，思路清晰，且宣称具备无监督物体掩码、可控 3D 编辑与机器人操作下游增益等实用价值；但摘要未给出定量证据与实验细节，难以仅凭摘要判断其相对现有方法的具体优势与可靠性。

</details>

<details>
<summary>Abstract</summary>

We present ParticleSplat, a self-supervised object-centric learning method that decomposes scenes into a set of latent ''particles'' representing semantic entities through feedforward 3D Gaussian Splatting. Building on the Deep Latent Particles (DLP) framework, which represents images as a set of particles with attributes such as position, scale, and visual appearance, we address a key limitation of DLP: its inherently 2D nature, which prevents explicit 3D spatial and geometric reasoning that are critical for downstream tasks such as robotic manipulation. Leveraging the structural similarity between latent particles and 3D Gaussian primitives, we introduce a 3D latent particle space trained with a novel view synthesis objective. Our model jointly encodes multiple views with camera poses into a shared 3D object-centric latent space, then transforms particles into particle-aligned 3D Gaussians whose composition reconstructs the full scene. On simulated and real-world datasets, we show that this formulation inherently learns object masks without supervision and supports controllable 3D scene editing, such as moving objects by modifying particles in the latent space. We further establish that the learned 3D representation improves downstream performance on robotic manipulation tasks.

</details>

#### 2026-09-16 - RGS: Reflection-aware Gaussian Splatting via Learning Geometry Continuity for Reflective Objects

**Authors:** Xiaobiao Du, Yida Wang, Cheng Bi, Kun Zhan, Xin Yu
**Links:** [abs](https://arxiv.org/abs/2609.19421) - [pdf](https://arxiv.org/pdf/2609.19421)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RGS: Reflection-aware Gaussian Splatting via Learning Geometry Continuity for Reflective Objects
- 作者：Xiaobiao Du, Yida Wang, Cheng Bi, Kun Zhan, Xin Yu
- 出版日期：2026-09-16T20:55:24Z
- 分类：Neural Scene Representations & Rendering（secondary_categories 未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.19421) / [PDF](https://arxiv.org/pdf/2609.19421)

### 一句话总结
针对现有 3DGS 在反射区域易发生表面塌陷、几何与高光质量差的问题，提出基于物理的延迟渲染框架 RGS，通过几何连续性建模来改善反射物体的新视角合成。

### 研究问题
摘要指出，现有 3D Gaussian Splatting（3DGS）方法在反射区域常出现"表面塌陷"（surface collapse）问题，由此导致几何结构不佳以及低质量的高光（specular）渲染。论文要解决的是：如何准确建模反射区域的高光，并提升此类物体的新视角合成质量。

### 核心思路/方法
- 提出一个基于物理的延迟渲染（physically-based deferred rendering）框架，命名为 Reflection-aware Gaussian Splatting（RGS）。
- 观察到一个强大的 3D 基础模型能够提供强 3D 几何先验，用于促进正确的几何建模。
- 基于此提出跨视角形状一致性正则化（cross-view shape consistency regularization），用大模型先验与跨视角约束来正则化几何表面，从而在反射区域产生更平滑的几何表面并减少几何空洞（geometric hollows）。
- 提出反射感知致密化策略（reflection-aware densification strategy），用于捕捉不同视角间的高光变化，以进一步改善反射区域的渲染结果。

### 主要贡献
- 提出 RGS 这一基于物理的延迟渲染框架，可准确建模高光区域并提升新视角合成性能。
- 利用 3D 基础模型先验与跨视角约束构建跨视角形状一致性正则化，缓解反射区域的表面塌陷/几何空洞，得到更平滑的几何表面。
- 提出反射感知致密化策略，捕捉跨视角高光变化，提升反射物体的渲染质量。
- 摘要称大量实验表明该方法能持续渲染高质量反射物体，并达到 state-of-the-art 性能。

### 局限性
- 具体的定量指标、对比方法与消融实验设置：摘要未提供足够信息。
- 所用 3D 基础模型的具体类型、先验形式及使用方式：摘要未提供足够信息。
- 反射感知致密化策略的具体实现细节与判据：摘要未提供足够信息。
- 方法的计算开销、训练/渲染效率及对非反射或混合场景的适用性：摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对 3DGS 在反射物体上的明确缺陷（表面塌陷与高光质量差）提出针对性方案，属于神经场景表示与渲染方向的直接改进，且摘要声称达到 state-of-the-art；若关注反射物体建模、几何正则化或 3DGS 改进，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has significantly improved the quality of novel view synthesis with explicit Gaussian representation. However, we observed that existing 3D Gaussian Splatting methods (3DGS) often suffer from surface collapse issues on reflective regions, and thus produce inferior geometry and low-quality specular. In this work, we propose a physically-based deferred rendering framework, named Reflection-aware Gaussian Splatting (RGS), that can accurately model specular regions and improve novel view synthesis performance. Specifically, we found that a powerful 3D foundation model can provide a strong 3D geometric prior to foster correct geometric modeling. Based on this, we propose a cross-view shape consistency regularization to regularize the geometry surface with the large model prior and cross-view constraints. In this manner, our RGS can produce smoother geometric surfaces on reflective regions while reducing geometric hollows. To further improve rendering results on reflective regions, we present a reflection-aware densification strategy that is designed to capture specular variations across various views. With this strategy, our RGS is able to render novel views of objects in higher quality. Extensive experiments demonstrate our method consistently renders high-quality reflective objects, achieving state-of-the-art performance.

</details>

#### 2026-09-16 - SemSafe-3DGS: Semantic Risk-Aware Active Navigation in Uncertain 3D Gaussian Splatting Maps

**Authors:** Amirhossein Mollaei Khass, Athanasios Cosse, Nader Motee
**Links:** [abs](https://arxiv.org/abs/2609.19330) - [pdf](https://arxiv.org/pdf/2609.19330)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SemSafe-3DGS: Semantic Risk-Aware Active Navigation in Uncertain 3D Gaussian Splatting Maps
- 作者：Amirhossein Mollaei Khass, Athanasios Cosse, Nader Motee
- 出版日期：2026-09-16T18:56:13Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.19330

### 一句话总结
论文提出一种面向带属性 3D 高斯地图的语义风险感知安全主动感知导航框架，通过类相关风险权重调制碰撞间隙模型，并将语义风险约束与主动感知统一在 CBF-QP 中。

### 研究问题
自主机器人需要在部分观测环境中安全导航，同时获取有助于未来规划的观测。现有安全形式化方法主要围绕几何推理，导致几何相似但语义后果不同的场景元素可能引发相近的控制响应。论文关注如何在不确定的 3D 高斯表示地图中，使导航安全约束能够体现语义差异，并兼顾主动感知以减少地图不确定性。

### 核心思路/方法
论文面向带属性的 3D 高斯地图提出语义风险感知的安全主动感知框架。其核心做法包括：使用类相关风险权重调制 Average Value-at-Risk 碰撞间隙模型，使安全关键的 Gaussian primitives 在复合障碍函数中具有更大影响；将加权后的间隙聚合为控制障碍函数；引入与轨迹相关的主动感知障碍，鼓励获取能够降低机器人预期运动方向上几何地图不确定性的观测。两类目标被集成到统一的 CBF-QP 中，将语义风险感知碰撞避免作为硬约束，同时在信息获取与安全或任务进展冲突时对信息获取进行放松。

### 主要贡献
- 提出面向 attributed 3D Gaussian maps 的语义风险感知安全主动感知导航框架。
- 通过类相关风险权重将语义属性引入 Average Value-at-Risk 碰撞间隙模型，使安全关键 Gaussian primitives 在复合障碍中影响更大。
- 将加权间隙聚合为控制障碍函数，并设计轨迹相关的主动感知障碍以降低预期运动方向上的几何地图不确定性。
- 在统一 CBF-QP 中集成安全硬约束与可放松的信息获取目标。
- 摘要称实验展示了高效安全约束、通过主动感知改善导航、语义相关轨迹适应以及 Ackermann 动力学下的实机执行。

### 局限性
摘要未提供足够信息说明方法的计算复杂度、可扩展性、失败案例或与其他方法的定量对比细节。摘要未提供足够信息说明语义属性与风险权重的获取方式、标注依赖或泛化能力。摘要未提供足够信息说明实验规模、数据集、评价指标及消融实验设置。

### 阅读优先级
高。理由：该论文将语义风险、主动感知、控制障碍函数与 3D 高斯地图导航结合，主题聚焦于不确定环境下的安全自主导航，且摘要明确提到统一 CBF-QP 与实机执行；若关注语义安全、主动感知或 3DGS 机器人应用，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous robots operating in partially observed environments must navigate safely while acquiring observations that improve future planning. Existing safety formulations generally reason primarily about geometry. Consequently, geometrically similar scene elements may induce comparable control responses despite having different semantic consequences. We present a semantic risk aware safe-active perception framework for navigation in attributed 3D Gaussian maps. Semantic attributes modulate an Average Value-at-Risk collision clearance model through class dependent risk weights, allowing safety-critical Gaussian primitives to receive greater influence in the composite barrier. The resulting weighted clearances are aggregated into a control barrier function, while a trajectory-relevant active perception barrier promotes observations that reduce geometric map uncertainty along the robot's anticipated motion. Both objectives are integrated in a unified CBF-QP that enforces semantic risk-aware collision avoidance as a hard constraint while relaxing information acquisition when it conflicts with safety or task progress. Experiments demonstrate efficient safety constraint, improved navigation through active perception, semantic dependent trajectory adaptation, and real-robot execution under Ackermann dynamics.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-22 - Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping

**Authors:** Markus Käppeler, Rohit Mohan, Abhinav Valada
**Links:** [abs](https://arxiv.org/abs/2609.26325) - [pdf](https://arxiv.org/pdf/2609.26325)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping, localization

<details>
<summary>Abstract</summary>

Camera-based 3D object detection and online vectorized HD mapping provide compact scene representations for autonomous driving, but both depend on accurate metric geometry and remain limited by depth ambiguity. Over long-term deployment, observations from repeated traversals can be accumulated into persistent point cloud priors that provide geometric context beyond the current observations. Existing explicit point cloud prior approaches, however, rely on LiDAR-based map construction and therefore require expensive 3D ranging sensors. We propose a framework that constructs a static point cloud prior map from previous camera traversals using Pi3X and augments each point with DINOv3 features. At runtime, a local prior patch is retrieved using global localization, encoded with a sparse voxel backbone, and fused in bird's-eye view (BEV) with lifted multi-view camera features. Task-specific sparse transformer heads then predict 3D objects and vectorized map elements from the fused representation. On Argoverse 2, the vision-based prior improves a strong baseline from 0.287 to 0.299 CDS and from 0.669 to 0.750 vectorized mapping mAP. Ablations show that semantic DINOv3 features are particularly important for vectorized mapping. These results demonstrate that vision-built geometric-semantic priors provide an effective form of long-term scene memory for camera-based perception, improving both tasks without LiDAR for prior-map construction or online inference.

</details>

#### 2026-09-22 - MatchFusion: Explicit-Implicit Instance Matching for Spatio-Temporal Multimodal Autonomous Driving

**Authors:** Xiaoyu Li, Jiajia Fu, Long Shi, Tianyu Du, Ruihang Li, Xian Wu, Lijun Zhao, Yingtao Zhang, Lining Sun, Ruifeng Li
**Links:** [abs](https://arxiv.org/abs/2609.25860) - [pdf](https://arxiv.org/pdf/2609.25860)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

Sparse instance representations provide a compact interface for spatial LiDAR-camera and temporal past-current interaction in multimodal perception and E2EAD. Effective interaction requires reliable instance correspondences despite geometric discrepancies and heterogeneous semantic representations. Attention-based methods exploit contextual semantics but often require specialized representation alignment, increasing computational overhead. In contrast, association based on structured object states is efficient and interpretable but lacks contextual evidence to resolve ambiguous matches. To combine these complementary strengths, we propose MatchFusion, a learnable instance matching and fusion module for spatio-temporal multimodal autonomous driving. MatchFusion initializes pairwise affinities using geometric similarity and category consistency, then selectively refines structurally plausible associations using instance embeddings. The resulting soft matchmap guides a common residual aggregation operator for adaptive information exchange. This unified matching-fusion formulation supports spatial LiDAR-camera and temporal past-current interaction, using multi-view image-plane geometry and motion-compensated BEV geometry as the respective structural priors. Experiments on nuScenes demonstrate consistent perception gains across diverse front-end configurations. Compared with a prior instance-centric fusion method, the MatchFusion-equipped system achieves higher perception accuracy while reducing FLOPs by 55.3% and GPU memory usage by 39.3%, with the matching-fusion module accounting for only 3.7% of total perception latency. Integrating temporal MatchFusion into SparseDrive further improves perception within an E2E framework without additional supervision. These results establish explicit-implicit matching as an effective and efficient mechanism for spatio-temporal instance interaction.

</details>

#### 2026-09-22 - Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes

**Authors:** Yuling Xi, Haokai Zhang, Muzhi Zhu, Hao Zhong, Zongze Du, Hengyu Zhao, Chenchen Jing, Yufei Yin, Bin Qin, Yongjie Yang, Zhenbo Luo, Hao Chen, Chunhua Shen
**Links:** [abs](https://arxiv.org/abs/2609.25841) - [pdf](https://arxiv.org/pdf/2609.25841)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D mapping, embodied AI, manipulation, mapping

<details>
<summary>Abstract</summary>

Metric reasoning is a critical and challenging task for Vision Language Models (VLMs), playing a pivotal role in embodied AI tasks such as robotic manipulation and autonomous navigation. However, current spatial reasoning remains bottlenecked by rigid pixel-level supervision; such localized optimization often compromises general multimodal intelligence, triggering performance degradation or catastrophic forgetting of broad reasoning capabilities. To address these limitations, we introduce Metric-Bench, a focused benchmark designed to guide metric-spatial reasoning using contextual information. By incorporating in-image reference objects with known physical dimensions, Metric-Bench guides models to implicitly learn the 2D-to-3D mapping without camera intrinsics. We further present MetricReasoner, a task-adapted reinforcement fine-tuning recipe for reference-grounded metric reasoning, using structured prompts and verifiable numerical rewards. Extensive experiments on Metric-Bench demonstrate that our approach significantly enhances spatial metric understanding, outperforming existing and even larger proprietary models by 43.1\%, while improving downstream embodied performance over a spatial-specialized counterpart by 30.4\% on RoboSpatial overall accuracy and 9.3\% on ERQA, and additionally delivering consistent gains on general benchmarks (15.9\% on V$\star$Bench, 88.9\% on BLINK), indicating that the proposed adaptation does not necessarily compromise general VLM capabilities.

</details>

#### 2026-09-22 - PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation

**Authors:** Yu Zheng, Qiyu Feng, Yixin Wu, Baoquan Yang, Yixuan Zhou, Bingyang Hu, Kemeng Huang, Guansheng Yang, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2609.25653) - [pdf](https://arxiv.org/pdf/2609.25653)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, manipulation, simulation

<details>
<summary>Abstract</summary>

Large-scale manipulation demonstrations are essential for learning robust visuomotor policies, yet real-world data collection is expensive and difficult to scale. Simulation offers a promising alternative, but physical and visual discrepancies can limit the transferability of synthetic data, particularly for manipulation with soft grippers. We present PhyVisGen, a physically and visually high-fidelity framework for scalable robotic manipulation data generation. On the physical side, PhyVisGen introduces an arm-gripper coupling method based on the Incremental Potential Contact (IPC), enabling high-fidelity soft contact throughout complete manipulation trajectories. On the visual side, it combines real-scene reconstruction with real-time path tracing to generate visually realistic observations while preserving captured scene appearance. Quantitative evaluations demonstrate the physical and visual fidelity of PhyVisGen. Policies trained exclusively on synthetic manipulation demonstrations achieve 65-95% success across five real-robot tasks, without real-robot demonstration data or policy fine-tuning.

</details>

#### 2026-09-22 - Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation

**Authors:** Sunyu Wang, Jean Oh, Nancy S. Pollard
**Links:** [abs](https://arxiv.org/abs/2609.25619) - [pdf](https://arxiv.org/pdf/2609.25619)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

This work investigates how to enable general multi-finger robotic hands to perform the complete tool manipulation process, which entails picking up a tool, loading it into a suitable pose, and then wielding it. Inspired by human tool manipulation and mechanical design principles, we model the hand and the tool as a unified hand-object mechanism (HOM) composed of sub-assemblies. Specifically, we define a HOM as consisting of the hand, the object, and the generalized contact frames, allowing the HOM's motions to be expressed with the same set of Cartesian-space relative contact velocities, irrespective of the hand's kinematics and geometry. Then, we define a HOM's sub-assemblies as relative contact velocity and contact force constraints between fingers. Building on these definitions, we developed a lightweight and physically interpretable motion planning and contact estimation framework using least squares and a complementary filter. We evaluated our framework in simulation by teleoperating five different robotic hands. The results show that our framework enabled all five hands to execute the complete tool manipulation process, achieving dexterous behaviors even from identical, simple reference trajectories. Furthermore, the results showcase our framework's adaptability to different hands, tools, and tasks, enabled by its kinematic and geometric foundation.

</details>

#### 2026-09-21 - JAMB: Joint Action-Motion Diffusion for Bimanual Manipulation

**Authors:** Chuyang Xiao, Peilin Meng, David Held
**Links:** [abs](https://arxiv.org/abs/2609.25322) - [pdf](https://arxiv.org/pdf/2609.25322)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Coordinated bimanual manipulation is challenging because the motion of either arm can alter the shared 3D scene and thereby affect the other arm. Yet most diffusion policies generate actions without explicitly modeling these future geometric consequences, while predictive variants typically use future state only as auxiliary supervision or fixed conditioning. We address this limitation by proposing JAMB, a diffusion policy that jointly denoises bimanual actions and future 3D point tracks. By allowing action and track hypotheses to evolve together within a shared Transformer, each can inform and refine the other throughout denoising. We further ground multimodal representations in a shared spatiotemporal coordinate system to facilitate geometry-aware interaction during joint denoising. We evaluate JAMB on diverse bimanual manipulation tasks in RoboTwin 2.0 and on a real-world robot, comparing it with action-only policies and alternative future-prediction approaches spanning different state representations and learning objectives. Across 16 simulation tasks, JAMB achieves an average success rate of 83.4%, outperforming the strongest baseline by 23.9 percentage points. On three real-world tasks, it outperforms the action-only and auxiliary geometry prediction methods by 50.0 and 21.2 percentage points, respectively. Beyond these performance gains, JAMB shows stronger generalization to cluttered scenes and out-of-distribution backgrounds than the evaluated baselines. Together, these results demonstrate the effectiveness of our joint action-motion modeling framework for coordinated bimanual manipulation. Our project website is available at https://jam-bimanual.github.io/

</details>

#### 2026-09-21 - Disparity Estimation of Planar Reflective Surfaces Using Specular Reflections From a Single Light Source

**Authors:** Katja Kossira, Frank Sippel, Jürgen Seiler, André Kaup
**Links:** [abs](https://arxiv.org/abs/2609.24756) - [pdf](https://arxiv.org/pdf/2609.24756)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Disparity Estimation of Planar Reflective Surfaces Using Specular Reflections From a Single Light Source
- 作者：Katja Kossira, Frank Sippel, Jürgen Seiler, André Kaup
- 出版日期：2026-09-21T15:26:17Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2609.24756 ；PDF https://arxiv.org/pdf/2609.24756

### 一句话总结
针对单光源照明的平面无纹理表面，论文提出 SRDE 算法，利用镜面反射区域、光源和相机位置信息估计视差，并可与现有神经视差估计流程结合以提升性能。

### 研究问题
在多相机成像与相机阵列广泛应用的场景（如自动驾驶、机器人控制、虚拟现实）中，物体与环境的准确视差图对可靠运行至关重要。尽管神经网络已有进展，平坦且无纹理物体的视差估计仍然困难。论文聚焦一个受限场景：平面、无纹理表面由单个固定光源照明，物体表面出现一个主导的镜面反射。在此条件下，可靠的几何与光度线索缺失，镜面反射还常导致误预测，尤其是依赖纹理信息进行对应像素匹配的传统方法。

### 核心思路/方法
论文提出名为 Specular Reflection Disparity Estimation（SRDE）的新算法，专门针对平面无纹理物体与单光源照明的受限场景。与传统立体匹配方法不同，SRDE 忽略纹理，转而利用镜面反射的几何属性，纳入反射区域的位置信息、光源信息以及相机配置信息来估计视差。此外，论文将 SRDE 集成到现有神经视差估计流程中，选择性地替换镜面区域的预测结果，而不修改主干模型。

### 主要贡献
- 提出 SRDE 算法，面向平面无纹理物体与单光源照明的受限场景进行视差估计。
- 不同于依赖纹理的传统立体匹配方法，SRDE 忽略纹理，利用镜面反射的几何属性，结合反射区域、光源和相机设置的位置信息。
- 摘要称 SRDE 在合成图像上显著优于现有方法，端点误差（End Point Error）改善超过 52%。
- 摘要称进一步测试表明在真实数据上也具有更优性能。
- 将 SRDE 集成到现有神经视差估计流程中，通过选择性替换镜面区域预测、不修改主干模型，实现额外性能增益且无需重新训练网络。

### 局限性
- 摘要未提供足够信息说明 SRDE 在非平面、有纹理或非单光源场景下的适用性。
- 摘要未提供足够信息说明真实世界实验的具体设置、数据集、评价指标细节与定量结果。
- 摘要未提供足够信息说明 SRDE 对光源标定、相机标定或反射区域检测误差的鲁棒性。
- 摘要未提供足够信息说明与神经视差估计流程集成时的具体替换策略、阈值或失败案例。
- 摘要未提供足够信息说明计算复杂度、实时性或实际部署开销。

### 阅读优先级
中。理由：该论文针对的是较受限但明确的场景（平面无纹理表面、单光源、主导镜面反射），并声称在合成与真实数据上均优于现有方法，同时提出可与现有神经视差估计流程即插即用式结合的策略，这对多相机成像、机器人、AR/VR 等应用具有潜在参考价值。但由于摘要未给出具体实验设置、定量对比细节与鲁棒性分析，是否值得深入阅读取决于读者是否关注镜面反射、无纹理表面视差估计或神经视差估计流程的后处理增强。

</details>

<details>
<summary>Abstract</summary>

Multi-camera imaging and camera arrays have become ubiquitous in many applications, such as autonomous driving, robot control, or virtual reality, and accurate disparity maps of objects and their environment are essential for reliable operation. Despite recent advances in neural networks, correctly estimating the disparity of flat and textureless objects remains challenging. In particular, we consider a scenario defined by flat, textureless surfaces illuminated by a single fixed light source, resulting in one dominant specular reflection visible on the object surface. Under these conditions, reliable geometric and photometric cues are missing, and the specular reflection often causes mispredictions, especially when using conventional methods that rely on texture information to match corresponding pixels. To address this issue, the novel Specular Reflection Disparity Estimation SRDE algorithm is introduced, which is specifically designed for the constrained scenario of planar, textureless objects and single-source illumination. Unlike conventional stereo matching methods, SRDE ignores texture and instead leverages the geometric properties of specular reflections by incorporating the position information of the reflective region, the light source, and the camera setup. We show that SRDE outperforms existing methods by a notable margin, achieving more than a 52% improvement in End Point Error on synthetic images. Further tests demonstrate superior performance on real-world data. Furthermore, we integrate SRDE into existing neural disparity estimation pipelines by selectively replacing predictions in specular regions without modifying the backbone model. This hybrid strategy enables additional performance gains without requiring network retraining.

</details>

#### 2026-09-21 - D-JEPA: A Decision-Aligned Latent World Model

**Authors:** Shuaijun Liu, Chengyu Wu, Qifu Wen, Feiyang You, Chenglong Zhang, Shuyang Hao, Xi Lin, Ningxin Su
**Links:** [abs](https://arxiv.org/abs/2609.24749) - [pdf](https://arxiv.org/pdf/2609.24749)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, autonomous driving, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：D-JEPA: A Decision-Aligned Latent World Model
- 作者：Shuaijun Liu, Chengyu Wu, Qifu Wen, Feiyang You, Chenglong Zhang, Shuyang Hao, Xi Lin, Ningxin Su
- 出版日期：2026-09-21T15:17:32Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2609.24749 ；PDF https://arxiv.org/pdf/2609.24749

### 一句话总结
D-JEPA 是一种“决策对齐”的潜在世界模型，针对潜在预测精度与实际执行结果不一致的问题，学习候选未来之间与决策相关的关系，并通过 JEPA 兼容的未来表征实现基于潜在距离的规划。

### 研究问题
潜在世界模型可以预测动作的后果，但摘要指出：预测准确并不保证潜在距离能反映哪个候选动作会成功执行。作者将这一现象定义为“决策局部预测差距”（decision-local prediction gap）：在少数竞争执行资格的未来候选中，一个被预测更接近目标的候选，其真实执行结果可能反而差于另一个可选方案。因此，核心问题是：如何让潜在世界模型中的预测几何与真实决策结果对齐，而不是仅追求预测精度。

### 核心思路/方法
- 提出 D-JEPA，一个决策对齐的潜在世界模型，从已执行结果中学习候选未来之间与决策相关的关系。
- 使用一个有界、置换等变（permutation-equivariant）的算子，联合推理“目标相对预测特征”和“序数证据”（ordinal evidence），在动作选择最关键的部位精炼预训练得到的预测几何。
- 通过受限的预测器适配（restricted predictor adaptation）和共享序数接口（shared ordinal interface），将这种对齐扩展到互补的预测几何上。
- 进一步将学习到的决策结构落实到 JEPA 兼容的未来表征中，从而可通过原生的潜在距离规划进行部署。

### 主要贡献
- 识别并形式化了“决策局部预测差距”：预测更接近目标不等于真实执行更优。
- 提出 D-JEPA，通过从执行结果中学习决策相关的关系结构，使潜在世界模型与动作选择对齐。
- 设计了有界、置换等变的联合推理算子，以及受限预测器适配和共享序数接口，用于精炼和扩展预测几何。
- 将决策结构嵌入 JEPA 兼容表征，支持原生潜在距离规划。
- 摘要报告了多类评估中的动作选择改进，包括 PushT 上 87.89% 成功率、RoboTwin 上平均提升 15.04 个百分点、物理机器人任务上提升 17 个百分点。

### 局限性
- 摘要未提供足够信息说明方法的失败案例、适用边界或未覆盖的任务类型。
- 摘要未提供足够信息说明计算开销、训练成本或推理效率。
- 摘要未提供足够信息说明与基线方法的完整对比设置、消融实验细节或统计显著性。
- 摘要未提供足够信息说明真实机器人实验的具体平台、任务数量和评估协议。
- 摘要未提供足够信息说明该方法对预训练模型质量、数据规模或领域迁移的依赖程度。

### 阅读优先级
高。理由：该论文聚焦具身智能与机器人控制中“世界模型预测精度”与“实际决策效果”不一致的关键问题，提出决策对齐的潜在世界模型，并报告了 PushT、RoboTwin、物理机器人和自动驾驶等多场景改进；若关注世界模型、JEPA、机器人策略选择或潜在规划，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Latent world models predict the consequences of actions, but accurate prediction does not guarantee that latent distance reflects which candidate will execute successfully. We identify a decision-local prediction gap: among the few futures competing for execution, a candidate predicted closer to the goal can produce a worse realized outcome than an available alternative. We introduce D-JEPA, a decision-aligned latent world model that learns decision-relevant relations among candidate futures from executed outcomes. A bounded, permutation-equivariant operator jointly reasons over goal-relative predictive features and ordinal evidence, refining pretrained predictive geometry where action choices are most consequential. Restricted predictor adaptation and a shared ordinal interface extend this alignment across complementary predictive geometries. D-JEPA further realizes the learned decision structure in JEPA-compatible future representations, enabling deployment through native latent-distance planning. Evaluations across latent control, manipulation, pretrained action-producing models, physical robots and autonomous driving demonstrate improved action selection, including 87.89% success on PushT, a 15.04-point average gain on RoboTwin, and a 17-point gain on physical robot tasks. These results establish decision-relevant relational structure as a direct bridge between predictive world modeling and effective control.

</details>

#### 2026-09-21 - InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality

**Authors:** Zhenghua Ma, Xinpan Meng, Zeyu Liu, Muyuan Ma, Hengdi Zhang, Houcheng Li, Long Cheng
**Links:** [abs](https://arxiv.org/abs/2609.24511) - [pdf](https://arxiv.org/pdf/2609.24511)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality
- 作者：Zhenghua Ma, Xinpan Meng, Zeyu Liu, Muyuan Ma, Hengdi Zhang, Houcheng Li, Long Cheng
- 出版日期：2026-09-21T12:51:29Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.24511

### 一句话总结
该论文提出一个完全在仿真中训练的强化学习框架，仅依靠目标位姿与紧凑的三维指尖力反馈，实现可直接部署到真实世界的接触密集精密插入操作，并在跨间隙、跨几何与多项真实任务中展现泛化能力。

### 研究问题
接触密集的精密插入是机器人装配中的关键操作技能。由于间隙很小，插入对位姿对齐误差高度敏感，容易发生碰撞与卡阻；而零件在几何形状与间隙上的差异又进一步阻碍策略的复用。论文关注的核心问题是：能否完全在仿真中训练插入策略，无需真实演示或策略微调即可直接部署，并在多种孔几何与间隙条件下保持成功与泛化。

### 核心思路/方法
论文提出一个强化学习框架，完全在仿真中训练插入策略，并直接部署到真实机器人，无需真实世界演示或策略微调。方法要点包括：
- 将目标位姿与紧凑的三维指尖力反馈结合，使策略能够在估计孔位存在误差时搜索对齐并修正运动。
- 使用解耦的门控奖励（decoupled gated reward）协调对齐与插入两个阶段。
- 通过力信号平滑（force-signal smoothing）与状态无关的标准差（state-independent standard deviations）稳定学习过程。
上述要点均来自摘要，摘要未提供网络结构、仿真环境细节、训练规模、奖励具体形式等更多信息。

### 主要贡献
- 提出一个完全在仿真中训练、可直接部署的接触密集精密插入强化学习框架，无需真实世界演示或策略微调。
- 策略在真实世界多种孔几何上完成插入，最小标称间隙为 0.02 mm，并在孔位误差下提升成功率、降低峰值接触力。
- 通过跨间隙与跨几何评估，验证了策略的泛化能力。
- 在 ManipulationNet 的 peg-in-hole 基准测试中，于其 Human-in-the-Loop 协议下取得首个满分 20/20，且插入运动完全自主。
- 仅在仿真六边形插入任务上训练得到的单一策略，在八个未见过的真实世界插入任务上取得 95.0% 的总体成功率。
- 项目网站提供开源仿真与真实机器人实验脚本、资产及训练检查点。

### 局限性
摘要未提供足够信息说明以下方面：方法的失败案例与边界条件、对特定传感器或力反馈精度的依赖程度、仿真到现实差距的具体影响、计算与训练成本、策略在其他操作任务上的适用性，以及与非强化学习或含真实微调方法的系统对比。摘要中提到的 0.02 mm 为最小标称间隙，跨间隙与跨几何评估的具体范围与任务数量除“八个未见真实任务”外亦未提供足够信息。

### 阅读优先级
高。理由：该工作直接针对机器人装配中接触密集精密插入这一高难度问题，提出无需真实演示与微调、从仿真直接部署的框架，并给出 0.02 mm 最小标称间隙、跨几何跨间隙泛化、ManipulationNet 基准首个 20/20 满分以及单一策略在八个未见真实任务上 95.0% 成功率等具体结果；同时提供开源脚本、资产与检查点，对具身操作、装配自动化与仿真到现实迁移方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Contact-rich precision insertion is a key manipulation skill in robotic assembly. Tight clearances make insertion more sensitive to alignment errors and prone to collisions and jamming, while variations in geometry and clearance across parts further complicate policy reuse. We present a reinforcement learning framework that trains insertion policies entirely in simulation for direct deployment without real-world demonstrations or policy fine-tuning. By combining target poses with compact three-dimensional fingertip force feedback, the policy learns to search for alignment and correct its motion despite errors in the estimated hole position. A decoupled gated reward coordinates alignment and insertion. Force-signal smoothing and state-independent standard deviations stabilize the learning process. The resulting policies perform real-world insertion across multiple hole geometries with a minimum nominal clearance of 0.02 mm and improve success while reducing peak contact forces under hole-position errors. Cross-clearance and cross-geometry evaluations further confirm policy generalization. The system achieved the first perfect score of 20/20 on ManipulationNet's peg-in-hole benchmark under its Human-in-the-Loop protocol, with fully autonomous insertion motions. A single policy trained only on a simulated hexagonal insertion task achieved an overall success rate of 95.0% across eight unseen real-world insertion tasks. These results show that learning entirely in simulation can yield precision insertion skills that can be deployed directly and reused across real-world tasks. The project website (https://mzhsoul.github.io/InsertAnything/) provides open-source simulation and real-robot experiment scripts, assets, and trained checkpoints.

</details>

#### 2026-09-21 - NeuIDO: Neural Intrinsic Dynamics Operator for Physics-Informed 4D World Models

**Authors:** Jiajing Lin, Xin Zhang, Jianhua Sun
**Links:** [abs](https://arxiv.org/abs/2609.24313) - [pdf](https://arxiv.org/pdf/2609.24313)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NeuIDO: Neural Intrinsic Dynamics Operator for Physics-Informed 4D World Models
- 作者：Jiajing Lin, Xin Zhang, Jianhua Sun
- 出版日期：2026-09-21T09:12:47Z
- 分类：Embodied / Robotics / AR Applications（主要分类；次要分类未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.24313) | [PDF](https://arxiv.org/pdf/2609.24313)

### 一句话总结
NeuIDO 将世界建模表述为神经算子学习问题，通过两阶段训练从视觉观测中学习统一的“内在动力学”表示，从而推进物理信息 4D 生成向世界模型演进。

### 研究问题
论文关注的核心问题是：现有的物理信息 4D 生成范式依赖人工设定的动力学假设，而非从数据中内化世界动力学，因此与“真正的世界模型”之间仍存在差距。如何让模型从视觉观测中自行学习世界动力学，成为需要解决的缺口。

### 核心思路/方法
- 将世界建模形式化为**神经算子学习问题**。
- 提出**两阶段训练策略**，学习从视觉观测分布到内在动力学分布的、具有泛化能力的映射。
- 基于该“观测—动力学”映射，NeuIDO 支持：
  - 直接从视频进行**零样本动力学推断**；
  - 通过**少样本适配**进一步对齐复杂的真实世界动力学。
- 目标是学习一个统一的**内在动力学表示**，而非依赖人工施加的动力学假设。

### 主要贡献
- 提出 NeuIDO 这一新的世界动力学建模框架，从视觉观测中学习统一的 intrinsic dynamics representation。
- 将世界建模转化为神经算子学习问题，并设计两阶段训练策略以获得可泛化的观测—动力学映射。
- 实现零样本视频动力学推断，并可通过少样本适配对齐复杂真实动力学。
- 摘要称大量实验表明，NeuIDO 能有效将不同视觉观测背后的内在动力学统一到共享表示中，并在新场景中快速推断动力学。

### 局限性
摘要未提供足够信息。具体局限、失败场景、实验设置细节、数据集与定量指标等均未在给定摘要中说明。

### 阅读优先级
**中**。理由：该论文主题处于物理信息 4D 生成、世界模型与具身智能的交叉点，问题定位明确，方法思路（神经算子 + 两阶段训练 + 零样本/少样本动力学推断）具有潜在参考价值；但当前仅提供摘要，缺少实验细节、对比结果与局限讨论，尚不足以判断其实际效果与适用边界。若研究方向涉及世界模型、4D 生成或物理信息学习，可优先关注。

</details>

<details>
<summary>Abstract</summary>

World models aim to capture environmental dynamics and predict future trajectories, showing growing potential for embodied intelligence. Physics-informed 4D generation integrates physical simulation to predict 3D object interactions, offering a promising pathway toward world models. However, this paradigm relies on manually imposed dynamical assumptions rather than internalizing world dynamics, and thus still leaves a gap toward a true world model. To bridge this gap, we propose NeuIDO, a novel world dynamics modeling framework that learns a unified intrinsic dynamics representation from visual observations, advancing physics-informed 4D generation toward a world model. Specifically, we formulate world modeling as a neural operator learning problem and introduce a two-stage training strategy to learn a generalizable mapping from the visual observation distribution to the intrinsic dynamics distribution. Building on this observation-dynamics mapping, NeuIDO enables zero-shot dynamics inference directly from videos and can be further aligned with complex real-world dynamics via few-shot adaptation. Extensive experiments demonstrate that NeuIDO effectively unifies the intrinsic dynamics underlying diverse visual observations into a shared representation and rapidly infers dynamics in novel scenes.

</details>

#### 2026-09-21 - Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning

**Authors:** Kejia Hu, Wentong Zhai, Bo Zhao, Shuai Liang
**Links:** [abs](https://arxiv.org/abs/2609.24033) - [pdf](https://arxiv.org/pdf/2609.24033)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning
- 作者：Kejia Hu, Wentong Zhai, Bo Zhao, Shuai Liang
- 出版日期：2026-09-21T02:59:08Z
- 分类：Embodied / Robotics / AR Applications（secondary_categories 未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.24033) / [PDF](https://arxiv.org/pdf/2609.24033)

### 一句话总结
Imagine-RL 在冻结的 VLA 策略上引入动作条件下的视觉-力矩未来想象，并通过带残差置信先验的交叉注意力改进动作评论家，从而在少量真实机器人 RL 轨迹下提升接触密集操作的成功率。

### 研究问题
摘要指出，接触密集操作中的可靠动作评估不能只看当前观测，还需要考虑未来的视觉与接触后果。现有噪声空间强化学习方法虽然能高效地引导冻结的 VLA 策略，但其评论家大多忽略了这些未来后果，因此动作评估不够可靠。

### 核心思路/方法
- 在噪声空间 VLA 后训练中加入“动作条件下的视觉-力矩想象”。
- 对每个候选动作块，使用冻结的视觉-力矩潜世界模型（VTLWM）自回归预测紧凑的未来表示，而不进行像素重建。
- 设计交叉注意力机制：由当前图像-状态-动作查询，去关注观测历史和预测未来。
- 利用上一窗口的预测残差作为 token 级置信先验，抑制不可靠的未来 token。
- 评论家结合当前证据与预测后果来更好地评估候选动作并监督 actor；VLA 与 VTLWM 均保持冻结。

### 主要贡献
- 提出 Imagine-RL，将动作条件下的视觉-力矩想象引入噪声空间 VLA 后训练，以增强评论家对候选动作的评估。
- 引入基于预测残差的 token 级置信先验，用于抑制不可靠的未来 token。
- 在四个真实机器人任务、每任务 50 次评估试验中，仅使用 100 条 RL 轨迹，平均成功率相较 DSRL 提升 23.6%，相较 VLA 基线提升 60%。
- 方法保持 VLA 与 VTLWM 冻结，仅在噪声空间进行强化学习后训练。

### 局限性
- 摘要未提供足够信息说明方法在不同机器人平台、不同任务类型或更复杂接触场景中的泛化能力。
- 摘要未提供足够信息说明 VTLWM 的训练数据、预训练细节或其对想象质量的依赖程度。
- 摘要未提供足够信息说明置信先验机制在预测残差异常或世界模型失准时的鲁棒性。
- 摘要未提供足够信息说明计算开销、推理时延或真实机器人部署成本。
- 摘要未提供足够信息说明与更多基线方法的完整对比、消融实验或失败案例分析。

### 阅读优先级
高。理由：该论文聚焦 VLA 强化学习后训练与接触密集操作，提出结合世界模型想象、交叉注意力和残差置信的评论家改进方案，并在真实机器人任务上报告了相对 DSRL 与 VLA 基线的显著成功率提升；若关注机器人操作、VLA 后训练或世界模型辅助 RL，该工作具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences. Existing noise-space reinforcement learning efficiently steers a frozen Vision-Language-Action (VLA) policy, but its critics largely ignore these consequences. We present Imagine-RL, which augments noise-space VLA post-training with action-conditioned visual-torque imagination. For each candidate action chunk, a frozen visual-torque latent world model (VTLWM) autoregressively predicts compact future representations without pixel reconstruction. A current image-state-action query attends to observed histories and predicted futures, while previous-window prediction residuals provide token-wise confidence priors that suppress unreliable future tokens. By combining current evidence with predicted consequences, the action critic better evaluates candidate actions and supervises the actor, while the VLA and VTLWM remain frozen. Across four real-robot tasks with 50 evaluation trials per task, Imagine-RL uses only 100 RL trajectories and improves the average success rate by (23.6%) over DSRL and by (60%) over VLA baselines.

</details>

#### 2026-09-21 - Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation

**Authors:** Fukang Liu, Yipu Chen, Jaehwi Jang, Danfei Xu, Zsolt Kira, Ye Zhao
**Links:** [abs](https://arxiv.org/abs/2609.23968) - [pdf](https://arxiv.org/pdf/2609.23968)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation
- 作者：Fukang Liu, Yipu Chen, Jaehwi Jang, Danfei Xu, Zsolt Kira, Ye Zhao
- 出版日期：2026-09-21T00:41:02Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供（摘要未提供足够信息）
- 链接：摘要链接 https://arxiv.org/abs/2609.23968 ；PDF 链接 https://arxiv.org/pdf/2609.23968

### 一句话总结
Opt2VLA 是一个面向人形机器人全身操作、在 VLA 与控制接口中显式引入连续接触力指令的力感知视觉-语言-动作框架。

### 研究问题
现有 VLA 模型在语义规划与视觉运动控制方面已有进展，但现有人形系统主要以几何运动目标表示动作，依赖以运动跟踪为主的全身控制器，对交互力的显式推理与控制有限。在接触丰富任务中，几何相似的运动可能因任务情境不同而需要不同的力模式，且接触后视觉观测可能变得不可靠，因此需要显式的力调节能力。

### 核心思路/方法
- 提出 Opt2VLA，一个力感知 VLA 框架，在 VLA 到控制的接口中引入显式力指令，用于人形机器人全身操作。
- 使用单个多任务 VLA 策略，同时预测几何运动目标与连续接触力参考。
- 这些输出由任务特定的、基于强化学习（RL）的全身控制器进行跟踪。
- 为提供可扩展且具有物理依据的监督，通过带显式力参考的全身轨迹优化（TO）生成动力学可行且接触一致的训练数据。

### 主要贡献
- 提出在 VLA 与控制接口中显式引入力命令的力感知 VLA 框架。
- 单个多任务 VLA 策略联合预测几何运动目标与连续接触力参考。
- 利用带显式力参考的全身轨迹优化，生成动力学可行且接触一致的训练数据，以提供可扩展、物理依据的监督。
- 在三个接触丰富的人形任务上进行评估，显示显式力条件相比仅运动控制能实现更准确、更一致的力调节；来自 TO 的物理依据力矩监督进一步提升了力跟踪精度与稳定性。
- 闭环评估展示了在仿真与硬件上具备语言条件化的力调制能力。

### 局限性
摘要未提供足够信息（未给出具体任务设置、评价指标数值、硬件平台细节、失败案例或适用范围限制等）。

### 阅读优先级
高。理由：该论文聚焦接触丰富场景下力感知 VLA 与人形全身操作，问题定位明确，方法上同时涉及多任务 VLA、力参考预测、RL 全身控制与轨迹优化监督，并声称在仿真与硬件上完成闭环验证；对关注人形机器人操作、VLA 与力控制结合的研究具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise regulation of interaction forces. While recent vision-language-action (VLA) models have shown promise for semantic planning and visuomotor control, existing humanoid systems primarily represent actions through geometric motion goals and rely on whole-body controllers focused on motion tracking, with limited explicit reasoning or control of interaction forces. This limitation is particularly relevant in contact-rich tasks, where geometrically similar motions may require different force regimes depending on the task context and where visual observations may become unreliable after contact. In this work, we present Opt2VLA, a force-aware VLA framework that introduces explicit force commands at the VLA-to-control interface for humanoid whole-body manipulation. A single multi-task VLA policy jointly predicts both geometric motion goals and continuous contact-force references, which are tracked by task-specific reinforcement learning (RL)-based whole-body controllers. To provide scalable and physically grounded supervision, we generate dynamically feasible and contact-consistent training data via whole-body trajectory optimization (TO) with explicit force references. We evaluate Opt2VLA on three contact-rich humanoid tasks and show that explicit force conditioning enables more accurate and consistent force regulation than motion-only control, while physically grounded torque supervision from TO further improves force tracking accuracy and stability. Closed-loop evaluations further demonstrate language-conditioned force modulation with Opt2VLA in simulation and on humanoid hardware.

</details>

#### 2026-09-20 - FinsSim: A Reality-Aligned Integrated Simulation Platform for Underwater Robot Learning

**Authors:** Yu Zhang, Yuanmingqing Song, Xiangyun Rao, Pangkit Fong, Kunhao Zhang, Chongrong Fang, Jianping He
**Links:** [abs](https://arxiv.org/abs/2609.23943) - [pdf](https://arxiv.org/pdf/2609.23943)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FinsSim: A Reality-Aligned Integrated Simulation Platform for Underwater Robot Learning
- 作者：Yu Zhang, Yuanmingqing Song, Xiangyun Rao, Pangkit Fong, Kunhao Zhang, Chongrong Fang, Jianping He
- 出版日期：2026-09-20T23:38:56Z
- 分类：Embodied / Robotics / AR Applications（二级分类：未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.23943) / [PDF](https://arxiv.org/pdf/2609.23943)

### 一句话总结
FinsSim 是一个面向水下机器人 Sim-to-Real 学习的、与现实对齐的一体化仿真平台，通过高保真仿真、统一学习接口、多传感器融合定位以及标定的推进器-水动力学模型，构建完整的仿真到现实迁移流程。

### 研究问题
水下机器人学习依赖仿真器，而这类仿真器需要同时具备高保真水动力学、便捷的学习接口以及可信的现实迁移能力。论文旨在弥合理论研究与实际应用之间的差距，解决水下机器人 Sim-to-Real 迁移中的关键问题。

### 核心思路/方法
- 构建高保真仿真，并提供可选后端以适配多样化需求。
- 提供标准控制基线以及统一的机器人学习工作流，方便水下机器人研究。
- 为实现可靠的 Sim-to-Real 迁移，采用多传感器融合方案，提供低成本且精确的定位。
- 实现经过标定的推进器-水动力学模型，以及带约束的力/力矩分配算法（constrained wrench allocation）。
- 通过 ROS 2 将上述模块桥接，形成完整的 Sim-to-Real 迁移流程。

### 主要贡献
- 提出 FinsSim，一个面向 Sim-to-Real 水下机器人学习的、与现实对齐的一体化仿真平台。
- 集成高保真仿真（可选后端）、标准控制基线与统一学习工作流。
- 引入多传感器融合定位、标定推进器-水动力学模型和约束力分配算法，以支持可靠的现实迁移。
- 通过匹配的仿真与实验，展示在该框架下可实现水下机器人控制策略可靠的 Sim-to-Real 迁移。
- 通过消融研究验证各模块可从不同方面应对水下 Sim-to-Real 的关键问题。

### 局限性
- 摘要未提供足够信息说明所使用仿真后端的种类与具体性能差异。
- 摘要未提供足够信息说明多传感器融合方案的具体传感器配置、定位精度指标与成本细节。
- 摘要未提供足够信息说明实验的具体场景、机器人平台、任务类型与定量评估结果。
- 摘要未提供足够信息说明消融研究的具体设计、对比对象与结论细节。
- 摘要未提供足够信息说明该平台在更复杂水下环境或不同机器人本体上的泛化能力。

### 阅读优先级
高。理由：该论文聚焦水下机器人 Sim-to-Real 学习这一具体且具有挑战性的方向，提出了一体化仿真平台，并声称通过匹配的仿真与实验验证了控制策略的可靠迁移，同时包含消融研究，问题定位与贡献陈述较为明确，对水下机器人学习与仿真平台研究具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Underwater robot learning relies on simulators that integrate high-fidelity hydrodynamics, convenient learning interfaces, and a credible transition to real scenarios. In this work, we present FinsSim, a reality-aligned integrated simulation platform for Sim-to-Real underwater robot learning. FinsSim first constructs high-fidelity simulation with selectable backends to adapt to diverse requirements. To facilitate underwater robot research, it further offers standard control baselines, alongside with unified robot learning workflows. For reliable Sim-to-Real transfer, FinsSim adopts a multi-sensor fusion scheme to provide low-cost yet precise localization. Moreover, it implements calibrated thruster-hydrodynamics models and a constrained wrench allocation algorithm. Bridging these modules by ROS~2, FinsSim establishes a complete Sim-to-Real transfer pipeline. Through matched simulations and experiments, it is demonstrated that reliable Sim-to-Real transfer of underwater robot control policies can be achieved with the FinsSim framework. Separate ablation studies also validate that the modules of FinsSim can address the pivotal issues of underwater Sim-to-Real from different aspects. Overall, this work aims to bridge the gap between theoretical research and practical applications, ultimately driving advancements in the field of underwater robotics.

</details>

#### 2026-09-20 - WOLF: World Model Guided LiDAR Exploration with Predictive Frontiers

**Authors:** Yuyang Tian, Penghui Yang, Pengyuan Wu, Haoran Yang, Chenhui Li, Pengfei Han, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li
**Links:** [abs](https://arxiv.org/abs/2609.23656) - [pdf](https://arxiv.org/pdf/2609.23656)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WOLF: World Model Guided LiDAR Exploration with Predictive Frontiers
- 作者：Yuyang Tian, Penghui Yang, Pengyuan Wu, Haoran Yang, Chenhui Li, Pengfei Han, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li
- 出版日期：2026-09-20T14:09:26Z
- 分类：Embodied / Robotics / AR Applications（secondary_categories 未提供）
- 链接：摘要页 https://arxiv.org/abs/2609.23656 ；PDF https://arxiv.org/pdf/2609.23656

### 一句话总结
WOLF 提出一种由世界模型引导的 LiDAR 无人机自主探索框架，通过预测未来观测并生成“预测前沿”来辅助视角选择与轨迹生成。

### 研究问题
基于 LiDAR 的无人机探索需要不断决定下一步观测位置。摘要指出，仅依赖已测量地图做决策，对被遮挡区域之后的空间延续缺乏预见性，可能遗漏潜在有信息量的方向。因此核心问题是：如何利用对未来观测的预测，提升自主探索的前瞻性与效率。

### 核心思路/方法
- 训练阶段：使用循环世界模型从探索轨迹中学习观测动态，循环记忆保留跨连续视角理解部分观测所需的空间上下文。
- 预测阶段：在探索过程中，模型结合观测历史与候选运动，预测局部占据情况与可见性。
- 预测前沿生成：通过置信度、分支一致性和观测质量对预测进行对齐与融合，识别有潜力的区域，形成“预测前沿”。
- 决策与更新：预测前沿与已测量的前沿共同用于几何视角选择和轨迹生成；新的扫描结果会更新后续预测。

### 主要贡献
- 提出 WOLF，一种世界模型引导的 LiDAR 探索框架，用未来观测预测增强自主探索。
- 设计循环世界模型，从探索轨迹学习观测动态，并借助循环记忆保留空间上下文。
- 提出预测前沿生成机制，融合置信度、分支一致性与观测质量来识别有前景区域。
- 将预测前沿与已测量前沿结合，用于指导几何视角选择与轨迹生成，并支持新扫描更新预测。
- 在仿真中报告：在 Garage 中相对于 EPIC，在可比覆盖率下平均终端时间减少 10.9%；在 Tunnel 中平均覆盖率从 42.12% 提升至 98.35%。真实世界实验展示了学习模型在物理飞行中进行在线推理的机载部署。

### 局限性
- 摘要未提供足够信息说明方法在更广泛场景、传感器配置或不同环境类型下的泛化能力。
- 摘要未提供足够信息说明真实世界实验的具体规模、评价指标、成功率或与基线方法的完整对比。
- 摘要未提供足够信息说明世界模型预测失败时的鲁棒性、计算资源需求和机载推理的实时性能细节。
- 摘要未提供足够信息说明“可比覆盖率”的具体定义及统计显著性。

### 阅读优先级
高。理由：该论文聚焦 LiDAR 无人机自主探索中的前瞻性决策问题，提出世界模型与预测前沿结合的明确方法路径，并给出仿真定量结果与真实世界机载部署证据；对具身智能、机器人自主探索和 UAV 导航方向具有直接相关性。

</details>

<details>
<summary>Abstract</summary>

LiDAR-based unmanned aerial vehicle (UAV) exploration builds maps by continually selecting where to observe next. However, decisions based on the measured map provide limited foresight into spatial continuations behind occlusions, leaving potentially informative directions unrecognized. We present WOLF, a world-model-guided framework that predicts future observations to enhance autonomous exploration. In the training stage, a recurrent world model learns observation dynamics from exploration trajectories, with recurrent memory retaining the spatial context needed to interpret partial observations across successive views. Building on this context, the model combines observation history with candidate motions during exploration to predict local occupancy and visibility. To guide further sensing, a predictive frontier generation mechanism then aligns and fuses these predictions using confidence, branch agreement, and observation quality to identify promising regions. The resulting predictive frontiers join measured ones to guide geometric viewpoint selection and trajectory generation, while new scans update subsequent predictions. In simulations, our method reduces mean terminal time by 10.9% relative to EPIC in Garage at comparable coverage and increases mean coverage from 42.12% to 98.35% in Tunnel. Real-world experiments further demonstrate onboard deployment of the learned model for online inference during physical flight.

</details>

#### 2026-09-20 - STRIDER: Stepping-Enabled Multi-Gait Hierarchical 3D Loco-Manipulation Framework for Humanoid Robots

**Authors:** Yuanzhuo Li, Wen Zhao, Zhe Yong, Xiang Meng, Gang Han, Hengle Ren, Xiaoyang Zheng, Zhen Wang, Yijie Guo
**Links:** [abs](https://arxiv.org/abs/2609.23483) - [pdf](https://arxiv.org/pdf/2609.23483)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：STRIDER: Stepping-Enabled Multi-Gait Hierarchical 3D Loco-Manipulation Framework for Humanoid Robots
- 作者：Yuanzhuo Li, Wen Zhao, Zhe Yong, Xiang Meng, Gang Han, Hengle Ren, Xiaoyang Zheng, Zhen Wang, Yijie Guo
- 出版日期：2026-09-20T09:17:11Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接 https://arxiv.org/abs/2609.23483 ；PDF 链接 https://arxiv.org/pdf/2609.23483

### 一句话总结
STRIDER 是一个面向人形机器人的分层多步态 3D loco-manipulation 框架，通过结合地形感知的 3D 踏步逻辑、AMP 自然行走、笛卡尔上半身控制，并提出 LD-PPO 蒸馏算法，将行走与踏步专家融合为统一的学生策略，以提升落脚点跟踪、姿态跟踪和多步态移动操作能力。

### 研究问题
论文指出人形机器人 loco-manipulation 存在两个突出限制：
1. 使用连续速度命令的控制器无法精确调节单个落脚点，而专门的落脚点跟踪模块又难以与全身操作集成。
2. 标准的基于动作的模仿蒸馏主要迁移专家动作，没有显式促进异构技能之间的共享表示。
因此，论文关注如何桥接这些差距，实现可精确落脚点控制、可融合多种步态专家并支持全身操作的人形机器人框架。

### 核心思路/方法
论文提出 STRIDER，一个分层多步态框架，核心组成包括：
- 地形感知的 3D 踏步逻辑；
- 基于 Adversarial Motion Priors（AMP）的自然行走；
- 笛卡尔上半身控制；
- 踏步专家在支撑脚坐标系中选择可行落脚点，并生成考虑离地间隙的摆动轨迹；
- 提出 Latent Distillation Proximal Policy Optimization（LD-PPO），一种带有 teacher-conditioned latent alignment 的蒸馏算法，用于将不同的行走和踏步专家融合为一个可执行的学生策略；
- LD-PPO 联合优化 on-policy reinforcement learning、基于 DAgger 的动作重建和 latent alignment，从而在迁移专家动作的同时鼓励跨异构模式共享技能表示。

### 主要贡献
- 提出 STRIDER 分层多步态人形机器人 3D loco-manipulation 框架，整合地形感知 3D 踏步、AMP 自然行走和笛卡尔上半身控制。
- 设计踏步专家，在支撑脚坐标系中选择可行落脚点并生成 clearance-aware 摆动轨迹。
- 提出 LD-PPO 蒸馏算法，通过 teacher-conditioned latent alignment 联合优化 on-policy RL、DAgger 动作重建和 latent alignment，将行走与踏步专家融合为统一学生策略。
- 在 TianGong Omni 人形机器人上进行仿真和真实机器人评估，表明 LD-PPO 在落脚点跟踪和姿态跟踪精度上优于 vanilla distillation-PPO。
- 在硬件部署中实现多步态 loco-manipulation，并具备准确的落脚点和末端执行器跟踪。

### 局限性
摘要未提供足够信息。摘要未说明具体实验规模、失败案例、泛化边界、计算成本、真实环境复杂度、安全性或与其他基线方法的完整对比细节，因此无法基于摘要进一步判断其局限性。

### 阅读优先级
高。理由：该论文聚焦人形机器人 loco-manipulation、精确落脚点控制、多步态专家融合和蒸馏策略学习，属于 embodied / robotics 中较核心且具挑战性的方向；同时摘要明确提到仿真与真实机器人部署验证，并声称在跟踪精度上优于 vanilla distillation-PPO，具有较高的方法参考价值和工程落地相关性。

</details>

<details>
<summary>Abstract</summary>

Humanoid loco-manipulation faces two prominent limitations: controllers using continuous velocity commands cannot precisely regulate individual footholds, while specialized foothold-tracking modules are difficult to integrate with whole-body manipulation. Furthermore, standard action-based imitation distillation primarily transfers expert actions, without explicitly encouraging a shared representation of heterogeneous skills. This paper introduces STRIDER, a hierarchical multi-gait framework to bridge these gaps. The framework integrates terrain-aware 3D stepping logic, Adversarial Motion Priors (AMP)-based natural walking, and Cartesian upper-body control: its stepping expert selects feasible footholds in the stance-foot frame and generates clearance-aware swing trajectories. To fuse distinct walking and stepping experts into one executable student policy, we propose Latent Distillation Proximal Policy Optimization (LD-PPO), a distillation algorithm augmented with teacher-conditioned latent alignment. By jointly optimizing on-policy reinforcement learning, DAgger-based action reconstruction, and latent alignment, LD-PPO transfers expert actions while encouraging a shared skill representation across heterogeneous modes. Simulation and real-robot evaluations on the TianGong Omni humanoid show that LD-PPO outperforms vanilla distillation-PPO in foothold-tracking and posture-tracking accuracy. Deployed on hardware, STRIDER realizes multi-gait loco-manipulation with accurate foothold and end-effector tracking.

</details>

#### 2026-09-20 - HEARTH: An Object-Centric RGB-Thermal-3D Dataset for Temperature-Aware Robot Manipulation

**Authors:** Yuning Su, Borui Li, Yonghao Shi, Bofei Liu, Xing-Dong Yang
**Links:** [abs](https://arxiv.org/abs/2609.23418) - [pdf](https://arxiv.org/pdf/2609.23418)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** camera calibration, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HEARTH: An Object-Centric RGB-Thermal-3D Dataset for Temperature-Aware Robot Manipulation
- 作者：Yuning Su, Borui Li, Yonghao Shi, Bofei Liu, Xing-Dong Yang
- 出版日期：2026-09-20T07:21:32Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.23418

### 一句话总结
该论文提出了一个以物体为中心的 RGB-热成像-3D 数据集 HEARTH，用于让机器人策略在操作中感知并利用物体的温度信息。

### 研究问题
语言引导的机器人操作可能依赖可见外观无法揭示的物理属性，温度就是其中之一。然而，现有的机器人学习物体数据集很少将测量到的温度与物体的外观和几何形状关联起来。论文旨在解决温度感知在机器人操作数据集与策略学习中的缺失问题。

### 核心思路/方法
论文构建了 HEARTH 数据集，包含来自 18 个日常类别的 90 个物理物体，共 145 个采集到的物体状态。其处理流程通过相机标定和位姿迁移，将表面温度映射到重建网格上。数据集包含原始温度测量、相机参数、RGB 纹理网格以及用于仿真的热纹理。基于这些资产，作者构建了三个源自 LIBERO 的任务，并采集了 1,200 条演示用于微调预训练的视觉-语言-动作（VLA）模型 π_{0.5}。消融研究显示，向 VLA 添加热观测后，温度依赖的物体选择任务成功率从仅 RGB 基线的 35.0% 提升到 75.0%。

### 主要贡献
- 提出 HEARTH 数据集：一个以物体为中心的 RGB-热成像-3D 数据集，涵盖 90 个物体、18 个类别、145 个物体状态。
- 提供将表面温度映射到重建网格的流程，并包含原始温度测量、相机参数、RGB 纹理网格和热纹理。
- 基于该数据集构建三个 LIBERO 衍生任务，并采集 1,200 条演示用于微调预训练 VLA 模型 π_{0.5}。
- 通过消融研究证明加入热观测可显著提升温度依赖物体选择任务的成功率（35.0% → 75.0%）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：论文同时提出了新的多模态数据集和面向机器人操作的温度感知策略验证，且消融结果显示了热观测带来的显著性能提升，对具身智能、机器人学习和多模态感知方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Language-guided manipulation can depend on physical properties that visible appearance does not reveal. Temperature is one such property, but object datasets for robot learning rarely associate measured temperatures with object appearance and geometry. We present HEARTH, an object-centric RGB-thermal-3D dataset of 90 physical objects from 18 everyday categories, comprising 145 captured object states. Our pipeline maps apparent surface temperatures onto reconstructed meshes through camera calibration and pose transfer. The dataset includes raw temperature measurements, camera parameters, RGB-textured meshes, and thermal textures for simulation. We use these assets to construct three LIBERO-derived tasks and collect 1,200 demonstrations for fine-tuning a pretrained vision-language-action (VLA) model, $π_{0.5}$. In an ablation study, adding thermal observations to the VLA increases success on temperature-dependent object-selection tasks from 35.0% for the RGB-only baseline to 75.0%. These results demonstrate the utility of HEARTH for training robot policies to follow temperature-related instructions.

</details>

#### 2026-09-20 - Manipulation Feasible Navigation Among Movable Obstacles with Discrete Contact Pushing

**Authors:** Shaohu Wang, Aiguo Song, Yulong Yuan, Zhongyu Sun, Tianyuan Miao, Qinjie Ji
**Links:** [abs](https://arxiv.org/abs/2609.23312) - [pdf](https://arxiv.org/pdf/2609.23312)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Manipulation Feasible Navigation Among Movable Obstacles with Discrete Contact Pushing
- 作者：Shaohu Wang, Aiguo Song, Yulong Yuan, Zhongyu Sun, Tianyuan Miao, Qinjie Ji
- 出版日期：2026-09-20T02:59:49Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.23312) / [PDF](https://arxiv.org/pdf/2609.23312)

### 一句话总结
提出一种面向移动操作机器人的分层可移动障碍物导航（NAMO）框架，通过结合高层重定位规划、LLM 辅助推断操作依赖以及离散接触推挤执行，实现对大体积不可抓取障碍物的可行导航与操作。

### 研究问题
在存在大型可移动障碍物的环境中，仅绕行导航可能效率低下甚至不可行。若要与障碍物交互，则需要同时推理导航收益、可行放置位置以及可执行的操作方式。论文旨在解决移动操作机器人在此类环境中的导航与操作联合可行性问题。

### 核心思路/方法
论文提出一个分层 NAMO 框架：
- 高层规划器从参考路径中识别关键阻塞障碍物，搜索同时满足几何约束、操作约束和下游导航约束的重定位方案。
- 当直接重定位受到其他可移动物体阻碍时，选择性调用 LLM 推断辅助操作依赖关系，再由确定性几何规划进行验证。
- 在执行层面，为箱形障碍物表面定义离散接触模式，根据位置和姿态误差在线选择接触面与区域，通过接触切换实现直线推、侧推和角推。
- 使用循环强化学习策略协调移动底座与机械臂，在持续推挤过程中跟踪工具中心点（TCP）目标并保持末端执行器可达性。

### 主要贡献
- 提出面向移动操作机器人的分层 NAMO 框架，联合考虑几何、操作与下游导航约束。
- 引入 LLM 选择性推断辅助操作依赖，并通过确定性几何规划验证。
- 定义箱形障碍物表面的离散接触模式，支持直线、侧面和角部推挤的在线接触切换。
- 使用循环强化学习策略协调移动底座与机械臂，维持持续推挤中的 TCP 跟踪与末端可达性。
- 通过仿真和真实机器人实验展示在绕行、单/多障碍物重定位及依赖约束场景中的可行导航-操作，验证框架对大型不可抓取障碍物的交互式导航能力。

### 局限性
摘要未提供足够信息。摘要中未说明方法在非箱形障碍物、复杂动态环境、计算实时性或失败案例方面的表现，也未提供定量对比结果、消融实验细节或 LLM 调用频率与可靠性分析。

### 阅读优先级
中。理由：该论文聚焦移动操作与可移动障碍物导航这一具身智能中的实际难题，方法结合分层规划、LLM 辅助推理、离散接触推挤与强化学习，具有一定新颖性和工程集成价值；但摘要未给出定量实验结果与详细对比，是否显著优于现有方法尚不明确。若关注机器人导航、移动操作或 NAMO 方向，可优先阅读；若仅关注通用视觉或 AR 应用，相关性可能有限。

</details>

<details>
<summary>Abstract</summary>

In environments with large movable obstacles, detour-only navigation can be inefficient or even infeasible, while obstacle interaction requires reasoning about navigation benefit, feasible placement, and executable manipulation. We present a hierarchical navigation among movable obstacles (NAMO) framework for mobile manipulators. At the high level, the planner identifies key blocking obstacles from reference paths and searches for relocation plans that jointly satisfy geometric, manipulation, and downstream navigation constraints. When direct relocation is hindered by other movable objects, a large language model (LLM) is selectively invoked to infer auxiliary manipulation dependencies, which are then verified by deterministic geometric planning. To execute the resulting relocation goals, we define discrete contact modes on the surfaces of box-shaped obstacles and select contact faces and regions online based on position and orientation errors, enabling straight, side, and corner pushing through contact switching. A recurrent reinforcement-learning policy coordinates the mobile base and manipulator to track tool center point (TCP) targets while preserving end-effector reachability during sustained pushing. Simulation and real-robot experiments demonstrate feasible navigation-manipulation in detour, single- and multi-obstacle relocation, and dependency-constrained scenarios, validating the framework for interactive navigation with large non-graspable obstacles. The open-source project is available at https://cloudytosunny.github.io/NAMO_DCPushing/.

</details>

#### 2026-09-17 - DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation

**Authors:** Yan Qin, Yue Chen, Wenwei Lin, Shujia Liu, Chuqiao Lyu, Kailun Su, Chenze Yu, Ping Luo, Wenbo Ding, Tianxing Chen, Renjing Xu
**Links:** [abs](https://arxiv.org/abs/2609.20649) - [pdf](https://arxiv.org/pdf/2609.20649)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation
- 作者：Yan Qin, Yue Chen, Wenwei Lin, Shujia Liu, Chuqiao Lyu, Kailun Su, Chenze Yu, Ping Luo, Wenbo Ding, Tianxing Chen, Renjing Xu
- 出版日期：2026-09-17T16:28:34Z
- 分类：Embodied / Robotics / AR Applications（一级分类；二级分类未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.20649) ｜ [PDF](https://arxiv.org/pdf/2609.20649)

### 一句话总结
DexTouch-WM 是一种动作条件化的世界模型，利用可扩展的人类触摸数据与共享触觉传感布局，联合预测未来 RGB 观测与双侧触觉动态，以缓解真实机器人触觉交互数据难以规模化的问题。

### 研究问题
学习接触丰富的灵巧操作预测模型需要密集的触觉交互数据，但这类数据在真实机器人上采集成本高、难以扩展，并且与具体本体（embodiment）的传感器绑定。论文试图解决：如何利用可扩展的人类触摸数据来监督机器人触觉世界模型的学习。

### 核心思路/方法
- 核心洞察：当触觉观测与动作空间被“兼容化”后，人类与机器人操作共享可迁移的接触动态。
- 硬件与数据对齐：在人类手与灵巧机器人手上部署具有共享传感布局的柔性压阻阵列；并将人类运动重定向到机器人动作空间。
- 模型结构：DexTouch-WM 将预训练视频专家与轻量触觉专家耦合，使用解剖学感知的触觉 token（anatomy-aware tactile tokens）和对齐的动作条件。
- 训练与预测目标：以人类交互监督同一个用于真实机器人预测的动态模型，联合预测未来 RGB 观测与双侧触觉动态。
- 缩放实验设计：固定 5 小时真实机器人监督，将人类交互从 0 小时增至 100 小时，在人类与机器人任务集不相交的条件下评估留出的机器人域视觉、几何与接触预测。

### 主要贡献
- 提出 DexTouch-WM：一种动作条件化、可同时预测未来 RGB 观测与双侧触觉动态的世界模型。
- 通过共享触觉传感布局与人类动作重定向，构建人类触摸监督机器人触觉世界模型的可迁移路径。
- 在固定真实机器人监督量的设置下，验证增加人类交互时长（0 到 100 小时）可显著提升留出的机器人域视觉、几何与接触预测表现。
- 将世界模型进一步评估为策略评估的替代环境，以及用于真实机器人策略学习的合成轨迹生成器，表明可扩展人类交互是学习灵巧机器人世界模型的补充数据轴。

### 局限性
- 摘要未提供足够信息说明真实机器人实验的具体平台、任务种类、评估指标细节、人类与机器人任务集不相交的具体范围。
- 摘要未提供足够信息说明模型计算开销、推理速度、实时性表现。
- 摘要未提供足够信息说明触觉传感布局的具体设计、重定向方法的误差或失败案例。
- 摘要未提供足够信息说明在策略评估与合成轨迹生成上的定量结果与局限性。

### 阅读优先级
高。理由：该工作提出利用人类触摸数据监督机器人触觉世界模型的新数据轴，涉及人机触觉传感对齐、动作条件世界模型、虚实/人机迁移与策略学习等关键问题，且设置了从 0 到 100 小时人类交互的缩放实验，对接触丰富灵巧操作与触觉世界模型方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Learning predictive models of contact-rich dexterous manipulation requires dense tactile interaction, but such data are costly to scale on real robots and remain tied to embodiment-specific sensors. We introduce DexTouch-WM, an action-conditioned world model that learns from scalable human touch to jointly predict future RGB observations and bilateral tactile dynamics. Our insight is that human and robot manipulation share transferable contact dynamics when their tactile observations and action spaces are made compatible. We deploy flexible piezoresistive arrays with a shared sensing layout on both human and dexterous robot hands, and retarget human motion into the robot action space so that human interaction can supervise the same dynamics model used for real-robot prediction. DexTouch-WM couples a pretrained video expert with a lightweight tactile expert using anatomy-aware tactile tokens and aligned action conditioning. In human-to-robot scaling experiments, we keep five hours of real-robot supervision fixed while increasing human interaction from 0 to 100 hours, and observe substantial improvements in held-out robot-domain visual, geometric, and contact prediction despite disjoint human and robot task sets. Beyond prediction, we evaluate the world models as surrogate environments for policy evaluation and as generators of synthetic trajectories for real-robot policy learning, showing that scalable human interaction provides a complementary data axis for learning dexterous robot world models.

</details>

#### 2026-09-17 - AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations

**Authors:** Soham Patil, Om Sanjay Gunjal, Sourabh Bhosale, Arhan Chavare, Ramandeep Singh Hora, Spandan Roy
**Links:** [abs](https://arxiv.org/abs/2609.20107) - [pdf](https://arxiv.org/pdf/2609.20107)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations
- 作者：Soham Patil, Om Sanjay Gunjal, Sourabh Bhosale, Arhan Chavare, Ramandeep Singh Hora, Spandan Roy
- 出版日期：2026-09-17T12:07:28Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.20107) / [PDF](https://arxiv.org/pdf/2609.20107)

### 一句话总结
AnyViewDex 提出一种非对称训练流程，通过在仿真训练中引入多视角对比对齐与特权 3D 几何监督，使多指灵巧操作策略在部署时仅依赖未标定单目 RGB 与本体感知即可实现视角不变的零样本抓取。

### 研究问题
多指灵巧操作的视觉运动策略对相机视角变化高度敏感。为实现视角不变性，近期方法多依赖 RGB-D 或点云等显式 3D 模态，但这会带来硬件依赖、标定要求以及真实部署中对传感器噪声的脆弱性。论文试图解决的问题是：能否在不依赖测试时显式 3D 传感的条件下实现视角不变控制。

### 核心思路/方法
论文提出 AnyViewDex，一种非对称训练流程，将多视角对比对齐与特权 3D 几何监督相结合。具体而言，在仿真训练阶段回归绝对 3D 物体坐标，以此作为辅助目标，提供几何 grounding 信号，缓解全局池化对比嵌入的空间坍缩问题。部署阶段，策略仅使用未标定单目 RGB 和本体感知，进行零样本操作，不依赖测试时深度。方法在强化学习和学生-教师蒸馏两种设定下进行了验证。

### 主要贡献
- 证明无需测试时显式 3D 传感即可实现视角不变控制，方法是在仿真训练中将几何知识编码进视觉表示。
- 提出非对称训练流程，结合多视角对比对齐与特权 3D 几何监督。
- 通过回归绝对 3D 物体坐标作为辅助目标，缓解全局池化对比嵌入的空间坍缩。
- 在 xArm7 与 16-DoF LEAP Hand 硬件评估中，跨八种未见物体和六个未标定视角达到 76.7% 抓取成功率（480 次试验；所有消融条件共 2,400 次）。
- 表明几何 grounded 的单目策略可零样本迁移，无需测试时深度。

### 局限性
- 摘要未提供足够信息说明方法在更大规模物体类别、更复杂操作任务（如非抓取类灵巧操作）上的泛化能力。
- 摘要未提供足够信息说明对极端光照、遮挡、动态场景或传感器噪声的鲁棒性。
- 摘要未提供足够信息说明仿真到现实迁移中特权 3D 监督所需数据的具体获取成本与可扩展性。
- 摘要未提供足够信息说明与依赖 RGB-D 或点云的方法在同等条件下的详细对比结果。
- 摘要未提供足够信息说明失败案例的具体模式与原因分析。

### 阅读优先级
高。理由：该论文针对灵巧操作中视角不变性这一关键问题，提出不依赖测试时 3D 传感的单目 RGB 方案，并在真实硬件上进行了较大规模评估（480 次试验、多物体多视角），对具身智能与机器人操作方向具有较强参考价值；同时摘要给出了明确的方法机制与量化结果，值得进一步阅读全文以了解实验细节与局限。

</details>

<details>
<summary>Abstract</summary>

Visuomotor policies for multi-fingered dexterous manipulation are highly sensitive to camera viewpoint shifts. To achieve view invariance, recent methods increasingly rely on explicit 3D modalities like RGB-D or point clouds, which can introduce hardware dependencies, calibration requirements, and vulnerability to sensor noise during real-world deployment. In this work, we show that view-invariant control can be achieved without explicit test-time 3D sensing by encoding geometric knowledge into the visual representation during simulation. We present AnyViewDex, an asymmetric training pipeline that combines multi-view contrastive alignment with privileged 3D geometric supervision. By regressing absolute 3D object coordinates during simulated training, this auxiliary objective provides a geometric grounding signal that mitigates the spatial collapse of the globally pooled contrastive embedding. At deployment, the policy operates zero-shot using only uncalibrated monocular RGB and proprioception. We validate this approach across both reinforcement learning and student-teacher distillation. In hardware evaluation on an xArm7 with a 16-DoF LEAP Hand, AnyViewDex reaches 76.7% grasping success across eight unseen objects and six uncalibrated viewpoints (480 trials; 2,400 across all ablation conditions), indicating that geometrically grounded monocular policies transfer zero-shot without test-time depth. Project Page: https://anyviewdex.github.io/

</details>

#### 2026-09-17 - Feeling Terrain Before Crossing: World Models for Off-Road Navigation

**Authors:** E-In Son, Dong-Wook Kim, Ji-Hoon Hwang, Kangsun Lee, Jisung Bae, Jung-Taak Kim, Seung-Woo Seo
**Links:** [abs](https://arxiv.org/abs/2609.19863) - [pdf](https://arxiv.org/pdf/2609.19863)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Feeling Terrain Before Crossing: World Models for Off-Road Navigation
- 作者：E-In Son, Dong-Wook Kim, Ji-Hoon Hwang, Kangsun Lee, Jisung Bae, Jung-Taak Kim, Seung-Woo Seo
- 出版日期：2026-09-17T08:19:06Z
- 分类：Embodied / Robotics / AR Applications（主分类；二级分类摘要未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.19863) / [PDF](https://arxiv.org/pdf/2609.19863)

### 一句话总结
论文提出 Feel-WM，这是首个引入本体感觉（proprioception）条件的越野导航世界模型，在预测相机所见场景的同时预测机器人未来将“感受到”的物理状态与失败风险，从而在非结构化地形上实现更优的前瞻规划。

### 研究问题
导航世界模型通过“预见”来规划：预测各候选动作序列产生的未来并选择最优者，而非直接将观测映射为动作。但论文指出，城市环境中预测场景已足以作为决策代理，而越野导航的关键在于机器人—地形的交互，因此预测不能只覆盖相机将看到什么，还必须覆盖机器人将感受到什么。现有以场景为中心的模型无法预测机器人在规划轨迹上会打滑、倾斜或震动的程度。如何让世界模型在越野场景中同时预测视觉未来与物理未来，是本文要解决的问题。

### 核心思路/方法
- 以本体感觉作为输入条件：摘要指出本体感觉直接捕捉上述动力学，作为输入时可改进对物理未来的预测。
- Feel-WM 同时预测两类未来：机器人将感受到的物理未来（以未来本体感觉状态和失败风险的形式表示），以及相机将看到的场景。
- 无人工标签学习：未来本体感觉状态与失败风险均从机器人自身经验中学习，无需人工标注。
- 规划器设计：规划器将物理未来与场景一并展开（roll out），并在一个可分离的评分中权衡预测失败风险与目标相似度，而非将二者混为一谈。

### 主要贡献
- 提出 Feel-WM，被描述为首个以本体感觉为条件、在预测相机所见之外还预测机器人所感的越野导航世界模型。
- 给出物理未来的具体表征形式：未来本体感觉状态 + 失败风险，二者均从机器人自身经验学习、无需人工标签。
- 提出可分离评分机制，将预测失败风险与目标相似度分开加权。
- 在真实越野数据与仿真中验证：在开环规划与闭环崎岖地形导航上，Feel-WM 优于仅视觉的导航世界模型，且覆盖轮式与足式平台。
- 部署验证：在 Husky 上于山地小径进行车载规划，提前预测粗糙地面并绕行，完成了端到端策略失败的路线。

### 局限性
摘要未提供足够信息。可确认的边界是：论文仅报告了在真实越野数据、仿真以及 Husky 山地小径部署上的结果，未在摘要中说明具体地形类型范围、失败案例、计算开销、跨平台迁移的泛化边界或与更多基线方法的对比细节。

### 阅读优先级
中。理由：选题处于具身智能与越野机器人导航的交叉点，“以本体感觉为条件预测物理未来”的思路对世界模型与机器人规划方向的研究者有明确参考价值，且包含真实平台部署验证；但摘要未给出定量结果、方法细节与消融信息，若研究兴趣不涉及越野导航、世界模型或机器人—地形交互，优先级可下调。

</details>

<details>
<summary>Abstract</summary>

Navigation world models plan by foresight, predicting the future that each candidate action sequence produces and selecting the best, rather than mapping observations to actions directly. Unlike urban settings where a predicted scene is a sufficient proxy, off-road navigation hinges on the robot--terrain interaction, so the prediction must cover not only what the camera will see but what the robot will feel. However, existing scene-focused models do not predict how much the robot will slip, tilt or shake along a planned trajectory. Proprioception captures these dynamics directly and, when used as input, improves the prediction of the physical future. We present Feel-WM, the first off-road navigation world model that conditions on proprioception and predicts what the robot will feel alongside what the camera will see. The physical future takes the form of a future proprioceptive state and a failure risk, both learned from the robot's own experience without human labels. The planner rolls out the physical future alongside the scene and weighs the predicted failure risk against goal similarity in a separable score. Experiments on real off-road data and in simulation demonstrate that Feel-WM outperforms visual-only navigation world models in open-loop planning and closed-loop rough-terrain navigation across wheeled and legged platforms. Deployed on a Husky on mountain trails, Feel-WM plans onboard, predicts rough ground ahead and steers around it, completing courses that an end-to-end policy fails.

</details>

#### 2026-09-17 - SnapPhysics: A Physics-Aware Scene Graph from a Single View for Interactive Mixed Reality Scenes

**Authors:** Suji Kang, Seok-Young Kim, Young Bin Kim, Taewook Ha, Dieter Schmalstieg, Shohei Mori, Woontack Woo
**Links:** [abs](https://arxiv.org/abs/2609.19815) - [pdf](https://arxiv.org/pdf/2609.19815)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SnapPhysics: A Physics-Aware Scene Graph from a Single View for Interactive Mixed Reality Scenes
- 作者：Suji Kang, Seok-Young Kim, Young Bin Kim, Taewook Ha, Dieter Schmalstieg, Shohei Mori, Woontack Woo
- 出版日期：2026-09-17T07:26:56Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.19815 ；PDF https://arxiv.org/pdf/2609.19815 ；项目页 https://snapphysics-ismar2026.github.io/

### 一句话总结
SnapPhysics 是一个无需训练、从单张图像重建三维物体并估计质量、摩擦和重心等物理属性的框架，通过物理感知场景图结合实例级三维重建与空间对齐，为混合现实提供物理上连贯的交互。

### 研究问题
在混合现实（MR）中，物理上连贯的交互不仅依赖几何，也依赖质量、摩擦、重心等物理属性。现有方法存在两类局限：一是通过分析视频中的物体动态来推断这些属性，计算代价高；二是对单张图像查询视觉语言模型（VLM），缺乏几何基础与物体间关系。论文旨在解决单视图下物理属性估计的上述问题。

### 核心思路/方法
SnapPhysics 是一个无需训练的框架，从单张图像重建三维物体并估计其物理属性（质量、摩擦、重心）。方法将实例级三维重建与空间对齐，与一个物理感知场景图相结合；该场景图编码物体间关系和每个物体的度量几何，作为结构化上下文，用于基于 VLM 的物理属性推理。由此弥补 VLM 单图查询缺乏几何基础与物体间关系的不足，并避免基于视频动态推断的高计算成本。摘要称其无需人工参数调优即可支持物理交互式 MR 体验。

### 主要贡献
- 提出 SnapPhysics，一个无需训练、从单张图像重建三维物体并估计质量、摩擦、重心等物理属性的框架。
- 结合实例级三维重建与空间对齐，以及编码物体间关系和逐物体度量几何的物理感知场景图，作为 VLM 属性推理的结构化上下文。
- 在 3D-FRONT 上，场景级 F-Score 相比最佳基于学习的方法提升 18.6%。
- 在具有真实质量标注的真实采集场景中，相比纯 VLM 估计，平均绝对对数差误差（mALDE）最多降低 20.5%，对数尺度相关性（\(r^2_{\mathrm{ls}}\)）最多提升 19.6%。
- 使物理交互式 MR 体验无需人工参数调优。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败情形、对特定场景或物体类别的依赖、重建精度上限、推理耗时、对 VLM 的依赖程度及泛化能力等局限。

### 阅读优先级
高。理由：该工作面向 MR 中物理属性估计这一关键问题，提出无需训练的单视图框架，并在 3D-FRONT 与真实采集场景上给出明确的定量提升；同时涉及三维重建、场景图与 VLM 推理的结合，对具身/机器人与 AR 应用方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We propose SnapPhysics, a training-free framework that reconstructs 3D objects and estimates their physical properties such as mass, friction, and center of gravity from a single image. For physically coherent interactions in mixed reality (MR), such properties are as important as geometry. Prior approaches infer them by analyzing object dynamics in video, which is computationally costly, or by querying vision-language models (VLMs) on single images, which lacks geometric grounding and inter-object relationships. We address these limitations by combining instance-level 3D reconstruction and spatial alignment with a physics-aware scene graph that encodes these relationships and per-object metric geometry as structured context for VLM-based property reasoning. Experiments on 3D-FRONT show that SnapPhysics improves scene-level F-Score by 18.6% over the best learning-based method, and on real captured scenes with ground-truth mass, it reduces the mean absolute log difference error (mALDE) by up to 20.5% and improves log-scale correlation ($r^2_{\mathrm{ls}}$) by up to 19.6% over VLM-only estimation. SnapPhysics enables physically interactive MR experiences without manual parameter tuning. Project page: https://snapphysics-ismar2026.github.io/.

</details>

#### 2026-09-17 - VAST: V2X/Dynamic Map-Aware Autonomous Driving Systems Validation Toolchain

**Authors:** Shunsuke Ito, Takuya Azumi
**Links:** [abs](https://arxiv.org/abs/2609.19681) - [pdf](https://arxiv.org/pdf/2609.19681)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VAST: V2X/Dynamic Map-Aware Autonomous Driving Systems Validation Toolchain
- 作者：Shunsuke Ito, Takuya Azumi
- 出版日期：2026-09-17T04:25:47Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无副分类
- 链接：摘要链接 https://arxiv.org/abs/2609.19681 ；PDF 链接 https://arxiv.org/pdf/2609.19681

### 一句话总结
VAST 是一个面向 V2X 与动态地图的自动驾驶系统级验证工具链，通过集成 Scenic、Scenario Simulator v2、AWSIM、Autoware 和 SIM-LDM 解决互操作性问题，并在遮挡交叉口等场景中量化了边界案例发现效率与动态地图可用性带来的安全收益。

### 研究问题
论文关注 IoT-to-Edge-to-Cloud 连续体中的协同自动驾驶系统级验证问题。该验证需要覆盖车辆、基础设施传感器、边缘侧动态地图服务和车载自动驾驶栈，因此面临跨组件互操作与联合仿真的挑战。摘要指出 VAST 不提出新的搜索算法，而是针对以下互操作性问题：Lanelet2 到 Scenic 的映射、通过 SS2 进行基于 ROS 2 的联合仿真、动态地图对象注入 Autoware，以及 TTC、PET、碰撞、超时和性能测量的收集。

### 核心思路/方法
VAST 的核心思路是构建一个 V2X/动态地图感知的验证工具链，将 Scenic、Scenario Simulator v2、AWSIM、Autoware 和 SIM-LDM 连接起来，以实现系统级联合仿真与验证。其方法重点不在搜索算法创新，而在互操作性工程，包括：
- Lanelet2 到 Scenic 的映射；
- 基于 ROS 2 通过 SS2 实现联合仿真；
- 将动态地图对象注入 Autoware；
- 收集 TTC、PET、碰撞、超时和性能测量。

摘要中报告了在遮挡交叉口场景下的评估：Lanelet2 兼容的约束采样将边界案例发现率从 40.0% 提升到 80.0%，并将每个已发现边界案例的平均时间从 259.7 秒降低到 110.4 秒。在相同生成场景分布下，动态地图可用性将碰撞率从 78.0% 降低到 40.0%，并将非碰撞结果从 22.0% 增加到 60.0%，同时 TTC/PET 出现统计显著变化。此外，在 1 至 16 个 NPC 的吞吐量研究中，采样时间保持在 0.1 秒以下，而 AWSIM/Autoware 执行与重启开销主导了运行时间。

### 主要贡献
- 提出 VAST 工具链，连接 Scenic、Scenario Simulator v2、AWSIM、Autoware 和 SIM-LDM，用于 V2X/动态地图感知的自动驾驶系统级验证。
- 解决多项互操作性问题，包括 Lanelet2-to-Scenic 映射、基于 ROS 2 的联合仿真、动态地图对象注入 Autoware，以及 TTC/PET/碰撞/超时/性能测量收集。
- 在遮挡交叉口场景中展示约束采样可提升边界案例发现率并缩短发现时间。
- 展示动态地图可用性可降低碰撞率并增加非碰撞结果，且 TTC/PET 变化具有统计显著性。
- 通过 1-16 个 NPC 的吞吐量研究，指出采样开销较低，而 AWSIM/Autoware 执行与重启开销是运行时主要瓶颈。
- 将 VAST 定位为协同自动驾驶 CPS 的实用验证基础设施。

### 局限性
摘要未提供足够信息说明 VAST 在遮挡交叉口之外的场景泛化能力、所依赖工具链的版本兼容性边界、动态地图注入的完整性与实时性约束、统计显著性的具体检验方法与效应量、以及真实世界部署验证情况。摘要也未提供关于失败案例、超时判定的具体阈值、性能测量的详细定义与可复现性配置的信息。此外，摘要明确 VAST 不引入新的搜索算法，因此其贡献主要限于互操作性与验证基础设施层面，搜索策略本身的创新性未在摘要中体现。

### 阅读优先级
中。理由：该论文针对协同自动驾驶系统级验证中的工具链互操作问题，提供了具体的集成方案与量化结果，对从事 V2X、动态地图、自动驾驶仿真验证和 CPS 系统测试的研究者与工程师有直接参考价值。但摘要表明其不提出新的搜索算法，核心贡献偏工程集成与验证基础设施，若读者关注算法创新或理论突破，优先级可能降低；若关注可落地的验证工具链与实验指标，则值得阅读。

</details>

<details>
<summary>Abstract</summary>

Cooperative autonomous driving in the IoT-to-Edge-to-Cloud continuum requires system-level validation across vehicles, infrastructure sensors, edge-side Dynamic Map services, and in-vehicle autonomous-driving stacks. This paper presents VAST, a V2X/Dynamic Map-aware validation toolchain that connects Scenic, Scenario Simulator v2, AWSIM, Autoware, and SIM-LDM. VAST does not introduce a new search algorithm; instead, it addresses interoperability challenges, including Lanelet2-to-Scenic mapping, ROS 2-based co-simulation through SS2, Dynamic Map object injection into Autoware, and collection of TTC, PET, collision, timeout, and performance measurements. In occluded-intersection scenarios, Lanelet2-compatible constrained sampling increases the edge-case discovery rate from 40.0% to 80.0% and reduces the average time per discovered edge case from 259.7 s to 110.4 s. Under the same generated scenario distribution, Dynamic Map availability reduces the collision rate from 78.0% to 40.0% and increases non-collision outcomes from 22.0% to 60.0%, with statistically significant TTC/PET shifts. A throughput study with 1-16 NPCs shows that sampling remains below 0.1 s, whereas AWSIM/Autoware execution and restart overhead dominate runtime. These results position VAST as a practical validation infrastructure for cooperative autonomous-driving CPSs.

</details>

#### 2026-09-17 - VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control

**Authors:** Zhongbo Zhang, Jiayi Jin, Yifan Wang, Zaibin Zhang, Haiwen Diao, Lijun Wang, Huchuan Lu
**Links:** [abs](https://arxiv.org/abs/2609.19554) - [pdf](https://arxiv.org/pdf/2609.19554)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control
- 作者：Zhongbo Zhang, Jiayi Jin, Yifan Wang, Zaibin Zhang, Haiwen Diao, Lijun Wang, Huchuan Lu
- 出版日期：2026-09-17T01:24:51Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.19554 ；PDF https://arxiv.org/pdf/2609.19554

### 一句话总结
论文提出 VA-Bench，用于评估通用多模态大模型在“观察—推理—行动—修正”闭环中的具身空间智能，覆盖仅 RGB 演示、主动选择视角与度量笛卡尔指令执行，并报告当前模型在长时程任务上的显著不足。

### 研究问题
论文关注的是：在不完整观测下，模型是否能够识别并主动获取缺失证据，将其解释到共同的空间参照系中，并据此采取行动。空间智能不仅是描述物体位置，还需要完成完整的 observe-reason-act-revise 闭环。VA-Bench 旨在检验通用 MLLM 能否把视觉演示与主动获取的证据转化为成功的具身行动。

### 核心思路/方法
VA-Bench 要求通用 MLLM 从仅 RGB 的演示中学习程序性上下文，主动选择相机视角，发出度量笛卡尔命令，并根据执行反馈修正命令。模型不获得特权物体位姿、oracle 轨迹或学习到的动作头。一个固定的、与模型无关的控制器只执行模型指定的目标。VA-Bench 包含 14 个基础任务族（11 个单臂和 3 个双臂）、7 个留出的几何/布局变体，以及一条长时程五物体组合赛道。评估在每项基础任务相同的 20 个经物理验证的种子上，对 12 个主要模型条件进行三次独立运行，报告终端成功率、九项轨迹级行为诊断和子任务进度。

### 主要贡献
- 提出 VA-Bench，用于评估完整 observe-reason-act-revise 闭环中的具身空间智能。
- 设计涵盖仅 RGB 演示、主动相机视角选择、度量笛卡尔命令发布与基于执行反馈修正的评测流程。
- 构建包含 14 个基础任务族、7 个留出几何/布局变体以及长时程五物体组合赛道的任务体系。
- 在 12 个主要模型条件、三次独立运行和每项基础任务 20 个物理验证种子上进行系统评估，并报告终端成功率、九项轨迹级行为诊断与子任务进度。
- 实验发现：最佳模型在标注运行中目标定位得分为 100.0%，空间关系得分为 78.9%，但三次运行宏平均任务成功率仅为 53.93±3.17%；主动相机控制显著优于被动多视角观察，一组匹配比较中成功率从 27.86% 升至 57.50%；留出几何迁移可使任务成功率下降超过 30 个百分点；没有任何模型完成严格的长时程回合，尽管取得了可观的子任务进展。

### 局限性
摘要未提供足够信息说明 VA-Bench 在真实机器人平台上的部署范围、任务种类之外的可扩展性、计算成本、模型规模影响、失败模式的具体归因，以及除已报告指标外的其他评测维度。摘要也未提供关于数据集规模、标注成本、仿真与真实环境比例、控制器具体实现细节和统计显著性的充分信息。

### 阅读优先级
高。理由：该论文直接针对具身空间智能与通用 MLLM 的闭环行动能力，提出了包含主动感知、度量控制和反馈修正的基准，并给出多个定量发现，如主动相机控制带来显著提升、留出几何迁移导致大幅下降、长时程任务无人完成。这些结果对具身智能、机器人学习和多模态模型评测具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires more than describing object locations. Under incomplete observation, models must identify and acquire missing evidence, interpret it in a common spatial frame, and act on it. We introduce VA-Bench to evaluate the complete observe-reason-act-revise loop. General-purpose MLLMs learn procedural context from RGB-only demonstrations, actively select camera viewpoints, issue metric Cartesian commands, and revise them from execution feedback. Models receive no privileged object poses, oracle trajectories, or learned action heads. A fixed model-agnostic controller executes only model-specified targets. VA-Bench contains 14 base task families (11 single-arm and three dual-arm), seven held-out geometry/layout variants, and a long-horizon five-object composition track. We evaluate 12 primary model conditions in three independent runs over the same 20 physically verified seeds per base task, reporting terminal success, nine trajectory-level behavioral diagnostics, and subtask progress. First, the best-performing model scores 100.0% on target localization and 78.9% on spatial relations in the annotated run. Its three-run macro-average task success is only 53.93+/-3.17%. Second, active camera control significantly improves task success over passive multi-view observation. In one matched comparison, success rises from 27.86% to 57.50%. Third, held-out geometric transfer can reduce task success by over 30 percentage points. No model completes a strict long-horizon episode, despite substantial partial progress. VA-Bench thus tests whether general-purpose MLLMs can turn visual demonstrations and actively acquired evidence into successful embodied action.

</details>

#### 2026-09-17 - AURORA: A Natural Language-Driven Agentic Framework for Understanding, Reasoning, and Orchestrating Reliable Air-Ground Co-Simulation

**Authors:** Keshu Wu, Hao Zhang, Rui Gan, Xiangbo Gao, Xiaopeng Li, Zhengzhong Tu, Yang Zhou
**Links:** [abs](https://arxiv.org/abs/2609.19527) - [pdf](https://arxiv.org/pdf/2609.19527)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AURORA: A Natural Language-Driven Agentic Framework for Understanding, Reasoning, and Orchestrating Reliable Air-Ground Co-Simulation
- 作者：Keshu Wu, Hao Zhang, Rui Gan, Xiangbo Gao, Xiaopeng Li, Zhengzhong Tu, Yang Zhou
- 出版日期：2026-09-17T00:41:46Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.19527 ；PDF https://arxiv.org/pdf/2609.19527

### 一句话总结
AURORA 将自然语言驱动的空地协同仿真场景生成建模为“编译与验证”过程，通过显式中间表示与运行时验证、局部修复，提升生成场景对用户所要求交互关系的忠实实现能力。

### 研究问题
空地交通研究日益依赖协同仿真，但场景构建劳动密集且难以验证。论文指出的关键问题是：生成场景可能成功执行，却未能实现用户所要求的空间、时间、通信或行为关系。因此，研究问题可概括为：如何从自然语言出发，生成不仅可执行、而且忠实实现所请求交互关系的可靠空地协同仿真场景。

### 核心思路/方法
论文提出 AURORA，一个自然语言驱动的智能体框架，将空地场景生成视为带有验证的编译过程。其核心是 Air-Ground Scenario Graph（AGSG），一种带类型的中间表示，显式连接智能体、空中任务、事件、通信链路、成功条件及其跨域依赖关系。该共享表示支持统一工作流中的多项能力：基于仿真器的解析、道路—空域联合落地、时间规划、执行前可行性检查、基于轨迹的运行时验证、失败定位，以及有界修复。论文还引入 AURORA-Bench，用于评估生成场景不仅是否执行，而且是否忠实实现所请求的交互。

### 主要贡献
- 提出 AURORA 框架，将自然语言驱动的空地协同仿真场景生成形式化为“编译并验证”的过程。
- 提出 Air-Ground Scenario Graph（AGSG）作为带类型的中间表示，显式建模智能体、空中任务、事件、通信链路、成功条件及跨域依赖。
- 基于 AGSG 构建统一工作流，涵盖解析、联合落地、时间规划、执行前可行性检查、运行时验证、失败定位与有界修复。
- 引入 AURORA-Bench，用于评估生成场景是否忠实实现所请求交互，而不仅是是否可执行。
- 实验显示：结构化执行显著提升可靠性；运行时验证能暴露基于完成度评估所忽略的“静默失败”；局部修复可在不重新生成整个场景的情况下解决许多违规。

### 局限性
摘要未提供足够信息说明具体实验设置、基线对比、语言模型范围、AURORA-Bench 的规模与指标细节、有界修复的失败案例与适用范围、计算开销、可扩展性或真实系统部署限制。以上方面均需依据论文全文进一步确认。

### 阅读优先级
高。理由：该论文聚焦自然语言驱动的可靠协同仿真生成，提出显式中间表示与运行时验证机制，并给出基准 AURORA-Bench；对关注具身/机器人/AR 应用、空地交通仿真、语言驱动场景生成与可验证智能体工作流的研究者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Air-ground transportation research increasingly relies on co-simulation, yet constructing scenarios remains labor-intensive and difficult to validate. More importantly, a generated scenario may execute successfully while failing to realize the spatial, temporal, communication, or behavioral relationships requested by the user. This paper presents AURORA, a natural-language-driven agentic framework that treats air-ground scenario generation as a process of compilation with verification. Central to AURORA is the Air-Ground Scenario Graph (AGSG), a typed intermediate representation that explicitly connects agents, aerial missions, events, communication links, success conditions, and their cross-domain dependencies. This shared representation enables simulator-grounded parsing, joint road-airspace grounding, temporal planning, pre-execution feasibility checking, trace-based runtime verification, failure localization, and bounded repair within a unified workflow. We further introduce AURORA-Bench to evaluate not only whether generated scenarios execute, but whether they faithfully realize the requested interactions. Experiments across multiple language models show that structured execution substantially improves reliability, while runtime verification exposes silent failures that completion-based evaluation overlooks. Localized repair further resolves many violations without regenerating the entire scenario. The results show that reliable scenario generation requires verifying realized behavior, not merely executable code, and demonstrate the value of explicit intermediate representations for verifiable and repairable language-driven co-simulation.

</details>

#### 2026-09-16 - WZPlanner: Safe End-to-End Path Planning for Autonomous Driving in Work Zones

**Authors:** Nishad Sahu, Changzhong Qian, Guangzhou Cai, Shounak Sural, Ragunathan, Rajkumar
**Links:** [abs](https://arxiv.org/abs/2609.19393) - [pdf](https://arxiv.org/pdf/2609.19393)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WZPlanner: Safe End-to-End Path Planning for Autonomous Driving in Work Zones
- 作者：Nishad Sahu, Changzhong Qian, Guangzhou Cai, Shounak Sural, Ragunathan, Rajkumar
- 出版日期：2026-09-16T20:22:51Z
- 分类：Embodied / Robotics / AR Applications（主要分类，二级分类未提供）
- 链接：摘要页 https://arxiv.org/abs/2609.19393 ；PDF https://arxiv.org/pdf/2609.19393 ；代码与数据集 https://github.com/Nishad-Sahu/WZPlanner

### 一句话总结
论文面向施工区（Work Zone）中车道几何被临时交通管制改变、且可能不在车载地图中的场景，提出数据集 WorkZonePlan、半自动数据生成流程 WAVE 以及联合预测车道边界、施工区边界与行驶轨迹的 BoundaryFormer（BF/BF++），并在闭环 CARLA 评估路线上报告了优于 SimLingo 与 TransFuser++ 的 Driving Score。

### 研究问题
施工区通过临时交通控制和封路改变车道几何，这些变化可能不存在于车载地图中，给自动驾驶车辆的感知与规划带来挑战。同时，具有结构化几何监督的公开数据集稀缺，限制了模型的泛化能力。论文关注的核心问题是：如何在缺乏地图先验、且几何结构被临时改变的施工区中，实现更安全的端到端路径规划。

### 核心思路/方法
论文从数据与模型两方面入手：

1. **数据集 WorkZonePlan**：包含 149K+ 合成样本和 5K+ 真实世界多模态样本，带有车道边界、施工区边界和行驶轨迹选项的 3D 标注；并提供 76 个闭环 CARLA 场景，在三种天气条件下回放，生成 228 条 Bench2Drive 格式的评估路线。
2. **数据生成流程 WAVE**（Work-zone-focused AV data generation in Virtual and rEal Environments）：用于创建该数据集的半自动化流程。
3. **模型 BoundaryFormer（BF）**：基于 transformer，联合预测车道边界多项式、施工区边界多项式和行驶轨迹；边界预测使用 slot attention。
4. **消融发现与 BF++**：消融表明，使用边界 slot 特征的独立轨迹解码器相比仅用 slot attention 的方法能显著改善轨迹预测。基于此，BF++ 提供 Camera 和 Camera+LiDAR 两种变体，并引入度量地平面编码、带类型的边界/轨迹查询、长程点锚点、图像空间曲线细化，以及保守的门控 LiDAR 融合。
5. **评估结果**：在评估冻结时四个模型共有的 211 条路线上，BF++-Camera 与 BF++-Camera+LiDAR 的 Driving Score 分别为 63.0 和 64.4，对比 SimLingo 的 59.3 和 TransFuser++ 的 26.1。BF++ 参数量比 SimLingo 小 40 倍，比 TransFuser++ 小 10 倍以上，同时 Driving Score 更高。

### 主要贡献
- 提出面向施工区的多模态数据集 WorkZonePlan，覆盖合成与真实样本，并提供车道边界、施工区边界、行驶轨迹选项的 3D 标注，以及闭环 CARLA 评估场景与 Bench2Drive 格式评估路线。
- 提出半自动化数据生成流程 WAVE，用于在虚拟与真实环境中构建该数据集。
- 提出 BoundaryFormer（BF），以 transformer 联合预测车道边界多项式、施工区边界多项式和行驶轨迹，并采用 slot attention 进行边界预测。
- 通过消融识别出使用边界 slot 特征的独立轨迹解码器对轨迹预测的关键作用，并据此发展出 BF++，集成度量地平面编码、带类型查询、长程点锚点、图像空间曲线细化与保守门控 LiDAR 融合。
- 在共同评估路线上报告 BF++ 以显著更小的模型规模取得高于 SimLingo 与 TransFuser++ 的 Driving Score，支持“联合预测车道边界、施工区边界与行驶轨迹”作为施工区安全自动驾驶的有前景方向。

### 局限性
- 摘要未提供足够信息说明真实世界样本的采集地区、传感器配置、标注质量控制或数据分布偏差。
- 摘要未提供足够信息说明 WAVE 流程的自动化程度边界、人工介入比例及其可扩展性。
- 摘要未提供足够信息说明 BF++ 各组件（如门控 LiDAR 融合、图像空间曲线细化）的独立消融结果。
- 摘要未提供足够信息说明失败案例、安全边界、极端天气或极端施工区布局下的表现。
- 摘要未提供足够信息说明与更多基线方法的对比，以及评估冻结所依据的具体标准。
- 摘要未提供足够信息说明模型的计算延迟、实时性与车载部署可行性。

### 阅读优先级
**高**。理由：该工作同时覆盖数据集、数据生成流程与端到端规划模型，且针对施工区这一地图先验易失效的安全关键场景；摘要给出了明确的闭环评估指标与模型规模对比，并以显著更小的参数量取得更高 Driving Score，对自动驾驶感知与规划交叉方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Work zones alter lane geometry through temporary traffic controls and closures that may be absent from on-board maps, challenging autonomous vehicle (AV) perception and planning. Generalization is also limited by scarce public datasets with structured geometric supervision. We present WorkZonePlan, a dataset comprising 149K+ synthetic and 5K+ real-world multimodal samples with 3D annotations for lane boundaries, work zone boundaries, and driving trajectory options. It also provides 76 closed-loop CARLA scenarios replayed under three weather conditions, yielding 228 Bench2Drive-format evaluation routes. We introduce WAVE (Work-zone-focused AV data generation in Virtual and rEal Environments), a semi-automated pipeline for creating the dataset, and BoundaryFormer (BF), a transformer-based model that jointly predicts lane and work zone boundary polynomials and driving trajectories. BF uses slot attention for boundary prediction. Ablations show that a separate trajectory decoder using boundary slot features substantially improves trajectory prediction over a slot-attention-only approach. Building on this finding, BF++ offers Camera and Camera+LiDAR variants with metric ground-plane encoding, typed boundary/trajectory queries, long-range point anchors, image-space curve refinement, and conservative gated LiDAR fusion. On the 211 routes common to all four models at the evaluation freeze, BF++-Camera and BF++-Camera+LiDAR achieve Driving Scores of 63.0 and 64.4, respectively, compared with 59.3 for SimLingo and 26.1 for TransFuser++ (TF++). BF++ is 40 times smaller than SimLingo and more than 10 times smaller than TF++, while achieving higher Driving Scores. These results support jointly predicting lane boundaries, work zone boundaries, and driving trajectories as a promising direction toward safer AV operation in work zones. Code and dataset: https://github.com/Nishad-Sahu/WZPlanner.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
