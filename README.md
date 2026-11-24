# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：82
- 分类分布：
  - Embodied / Robotics / AR Applications: 26
  - 3D Reconstruction & Multi-view Geometry: 21
  - Neural Scene Representations & Rendering: 21
  - Dynamic / 4D Reconstruction: 7
  - Geometry Foundation Models: 7
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“几何先验 + 基础模型”从拼接走向协同设计。** Plan4D 把 Depth Anything 3 与视频生成器 LongCat-Video 做模型缝合并加 DPT 头预测场景流；TuringPAI-VL 用多尺度潜查询把几何、跨视角、时序监督并入视觉 Transformer；DfD-GS 用具物理含义的散焦线索校正单目深度先验的尺度偏差。三者共同显示：几何基础模型不再只是下游重建的预处理深度源，而是与生成、语言、物理线索在训练或架构层面耦合。

2. **稠密注意力/非凸优化被“结构化稀疏与凸化”替代，效率成为重建方法的一等目标。** SGAR 用可学习关键选择替代跨视图稠密注意力，缓解视图数二次增长；FirstCross 用体素网格上的短序列凸问题替代超过一小时的逐场景非凸神经优化，并以 running-max 透射率构造紧凸闭包；SCCV-6D 以全稀疏多视角 RGB-D 单次前向替代多阶段流水线；AGE-Capture 用轻量在线状态与异步事件驱动采集减少跨区飞行与等待。方向一致性很强：结构先验（SfM 匹配、首穿越、可渲染性）被用来削减计算，而非用更大模型硬解。

3. **前馈重建开始追求“部署后稳健性”，而非只在训练分辨率下好看。** PaveSplat 指出解析表面对齐协方差在深度坐标系病态时无法校正 surfel 朝向，导致高分辨率重渲染出现空洞，用恒等初始化的四元数残差修正；AGSR 揭示 3DGS 投影协方差对细尺度结构的带宽衰减，以推理时协方差收缩做插件式超分；Depth Pro 2 明确把指标精度、边界锐利、时序一致与运行时间放在同一 Pareto 前沿上报告。评价维度正从单一 PSNR/精度转向“跨分辨率、跨帧、跨部署条件”的稳健性。

4. **动态/4D 与可规划的生成式世界模型成为独立细分方向。** Plan4D 把未来预测从“视频好看”推进到“稠密 4D 几何 + 文本动作可规划”，同时输出深度、相机、点云、场景流；Depth Pro 2 则从数据侧解决视频度量的时序一致性。两者分别覆盖 4D 生成的语义—几何联合与单目视频度量的时序稳定，构成同一动态重建议题的上下半程。

5. **领域专用 3D 应用明显向“可信度量化”和“数据/任务规模化”两端延伸。** 可信侧：Domain-Aware Conformal Prediction 揭示合成校准的保形位姿估计在真实图像上出现静默失效，改用外观翻译后的合成图像校准以保留几何标签；SpatialScout-V2 用 mean IoU、阈值命中率、覆盖率评估 VLM 主动建图。规模化侧：AgenticTask 以智能体扩增 RoboCasa 任务实例，PAD 以策略感知影响力估值筛选自动驾驶演示。三维视觉的评价对象正从“几何误差”扩展到“不确定性是否可信”和“数据是否对策略有用”。

6. **显式表示（高斯/网格）与物理成像模型深度结合，跨出图形学进入科学成像。** CryoGaussian 用高斯泼溅拟合冷冻电镜颗粒图像，经 CTF 调制的正交线积分可微光栅化，并以共享潜变量建模组成与构象异质性；MODL 在水密三角网格上联合优化几何与视角相关外观，强调网格内在质量而非仅新视角合成；MergeableRF 利用光传输线性性设计 merge-aware 训练使外观网络参数可合并。显式表示正从“实时渲染工具”变为“可解释、可合并、可对接成像物理的重建载体”。


#### 技术路线观察

**几何基础模型方向。** SGAR 代表“把经典 SfM 的匹配稀疏性注入前馈 Transformer 注意力”的路线，核心是可学习的关键选择模块预测跨视图 3D 邻近性，属于对现有前馈模型可微调通用的效率改造。TuringPAI 代表相反方向的“把几何监督压进通用视觉-语言骨干”，以 0.65B 端侧规模、HybridViT-MLQ 与多尺度潜查询换取空间理解。Aspect 上二者形成对照：一个做稀疏化以扩展视角规模，一个做统一化以服务下游动作，但都认同几何能力应内生于基础模型而非外挂。

**3D/4D 重建方向。** 可细分为三条支线。其一，度量与稳健：Depth Pro 2 用单网络统一图像/视频、原生分辨率预测，直接以 Pareto 前沿定义进展，回避了“多帧换一致性、单帧换锐利”的旧权衡；DfD-GS 走物理线索路线，用全聚焦—散焦图像对的散焦强度估计度量视差再对齐单目先验，属于小数据、强先验的稳健化思路。其二，效率与规模：SGAR、FirstCross、SCCV-6D 分别从注意力稀疏、凸化、全稀疏单次估计三个角度压低成本，且都强调“毫米级/大规模/工业部署”类现实约束。其三，主动采集与闭环：AGE-Capture 把重建前沿视角作为残余价值度量并据此自主终止，SpatialScout-V2 把主动建图搬到真实住宅并用 VLM 做视角选择，两者共同把重建从“给定图像求几何”推向“决定看哪里”。

**神经场景表示与渲染方向。** 高斯泼溅仍是主线，但关注点从“更快更好看”转向表示的可修正性与可组合性：PaveSplat 修正 surfel 朝向以抗分辨率变化，AGSR 在推理时收缩协方差并做多孔径融合，MergeableRF 让分基光外观网络参数可合并以支持重光照，CryoGaussian 把高斯搬到冷冻电镜并引入 CTF 调制光栅化。MODL 则提示网格路线并未退场——其卖点是水密性、曲率自适应重网格化与网格内在质量，这可能在高斯难以直接交付的资产管线中保有位置。

**机器人/AR 应用方向。** 呈现“感知—决策—数据”三层并行。感知层：SCCV-6D 面向料箱抓取的整体稀疏 6D 位姿，MORSEPose 用位姿—尺寸包络替代网格/表面距离监督做类别级位姿，Domain-Aware Conformal Prediction 为航天器位姿给出带覆盖保证的不确定性集合。决策层：SpatialScout-V2 检验 VLM 的主动探索与物体定位，AGE-Capture 检验无人机的自主采集终止。数据层：AgenticTask 用生成/执行双智能体扩增仿真任务，PAD 用策略梯度与影响力近似为驾驶演示定价，Driver Gaze Target Identification 则把注视估计与全景场景理解结合输出对象级目标。总体看，应用侧的方法论贡献越来越偏向“基准、评估协议与数据估值”，而非单一模型精度。

**跨方向的共同技术倾向。** 一是用可解释的结构先验（几何匹配、光传输线性、首穿越、散焦物理）约束学习问题；二是把“不确定性/可信度”显式建模（保形预测、不确定性引导聚合、覆盖率指标）；三是强调推理时或部署后的行为（插件式超分、高分辨率重渲染、端侧算力、自主终止）。这三点比单纯“更大模型”更能概括本批论文的走向。


#### 值得优先阅读的论文

1. **Depth Pro 2（2611.26603）**——优先理由：它正面处理单目度量深度中长期存在的“时序一致性 vs 边界锐利”权衡，并以单一网络统一图像与视频、原生分辨率输出，还给出精度/锐利/一致性/运行时的 Pareto 前沿模型族。对任何做视频深度、4D 重建或度量几何的工作，它既是基线也是评价框架的候选。

2. **SGAR（2611.26493）**——

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-20T16:04:06-05:00
**Total number of papers:** 67
**Number of papers added in the latest update:** 25
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

### 2026-11

#### 2026-11-19 - SGAR: Feed-Forward 3D Reconstruction via Sparse Geometry-Guided Attention

**Authors:** Aoxiang Fan, Maria Pilligua, Corentin Dumery, Oliver Heinimann, Pascal Fua
**Links:** [abs](https://arxiv.org/abs/2611.26493) - [pdf](https://arxiv.org/pdf/2611.26493)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward reconstruction, feed-forward 3D reconstruction, 3D reconstruction, structure from motion

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SGAR: Feed-Forward 3D Reconstruction via Sparse Geometry-Guided Attention
- 作者：Aoxiang Fan, Maria Pilligua, Corentin Dumery, Oliver Heinimann, Pascal Fua
- 出版日期：2026-11-19T17:46:57Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.26493) | [PDF](https://arxiv.org/pdf/2611.26493)

### 一句话总结
SGAR 用可学习的稀疏几何相似度引导注意力替代前馈三维重建中的稠密全局注意力，以降低多视图扩展时的二次计算成本。

### 研究问题
现有前馈三维重建模型采用稠密注意力，将所有视图的图像块（patch）两两关联；其计算成本随视图数量呈二次增长，难以应用于更大规模的重建场景。论文试图回答：这些稠密注意力计算是否大部分并不必要。

### 核心思路/方法
作者从经典 structure-from-motion 视角提出：三维结构来源于二维中几何匹配的区域。基于此，SGAR 让每个 patch token 只关注来自其他视图的一小部分 patch token；这些被选中的 token 由轻量级可学习的关键选择模块决定，该模块被训练用于预测跨视图 token 的三维邻近性。由此，稠密全局注意力被替换为更高效的、几何相似度引导的稀疏注意力。SGAR 被描述为一种通用方法，可通过微调应用于不同的前馈模型。

### 主要贡献
- 提出 SGAR，用几何相似度引导的稀疏注意力替代稠密全局注意力，以缓解视图数量增加带来的二次成本。
- 设计轻量级可学习关键选择模块，用于预测跨视图 token 的三维邻近性，从而筛选每个 patch token 需关注的少量其他视图 token。
- 将 SGAR 定位为可微调应用于不同前馈模型的通用方法。
- 摘要称：实验中 SGAR 在现有稠密与稀疏方法中最快，并在稀疏方法中最准确；在 1,000 个视图时相比稠密注意力最高快 12 倍，且在现有稀疏方法失败的情况下保持稳定位姿精度，并在相同时间预算下重建更完整几何。

### 局限性
摘要未提供足够信息说明方法的具体适用边界、失败情形或精度—效率权衡的详细限制。例如：关键选择模块的误选影响、在何种视图规模或场景类型下性能下降、微调所需数据与计算开销等，摘要均未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对前馈三维重建中稠密注意力随视图数二次增长的关键扩展性问题，提出通用性较强的稀疏注意力替换方案，并在摘要中给出速度、位姿精度与几何完整性的对比结论；对多视图三维重建与高效注意力设计方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward models have been very successful in 3D reconstruction with ad hoc attention designs that relate all view patches densely. However, the cost of this dense global attention grows quadratically with the number of views, preventing the model from applying to larger-scale reconstruction settings. In this paper, we argue that most dense attention computations are unnecessary from a classical structure-from-motion perspective: 3D structures stem from geometrically matching regions in 2D. We bring this principle to learning-based feed-forward reconstruction with our Sparse Geometric Attention Reconstruction (SGAR) method. In SGAR, each patch token attends to only a small set of patch tokens from other views, chosen by a lightweight learned key selection module trained to predict cross-view 3D proximity of tokens. Thus, dense global attention is replaced by much more efficient geometric-similarity-guided sparse attention. SGAR is a general method that can be applied to different feed-forward models by fine-tuning. In our experiments, we show that SGAR is the fastest among both state-of-the-art dense and sparse methods and the most accurate sparse one. It runs up to 12-times faster than dense attention at 1,000 views with stable pose accuracy where existing sparse methods fail, and shows the best performance in reconstructing more complete geometries on the same time budget.

</details>

#### 2026-11-19 - Multi-View Transformer with Geometry-Guided Multi-Modal ControlNet for 3D Virtual Try-On

**Authors:** Sarthak Batra, Armin Mustafa, Adrian Hilton
**Links:** [abs](https://arxiv.org/abs/2611.25979) - [pdf](https://arxiv.org/pdf/2611.25979)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** multi-view transformer, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-View Transformer with Geometry-Guided Multi-Modal ControlNet for 3D Virtual Try-On
- 作者：Sarthak Batra, Armin Mustafa, Adrian Hilton
- 出版日期：2026-11-19T12:03:04Z
- 分类：主分类 Geometry Foundation Models；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.25979；PDF https://arxiv.org/pdf/2611.25979

### 一句话总结
论文提出 GS-VTON-MVT 三阶段框架，用多视角 Transformer、几何引导多模态 ControlNet 与姿态自适应注意力，改善 3D Gaussian Splatting 人体虚拟试穿中跨视角一致性问题。

### 研究问题
对 3D Gaussian Splatting（3DGS）捕获的人体进行编辑、使其穿上新 garment 时，每个渲染视角需要对同一 garment 细节保持一致。现有 3D 虚拟试穿（VTON）流程主要独立编辑训练视角，并用人工选择的参考视角、固定注意力混合权重等手工启发式规则融合；这些不一致会进入 3D 表示，并在新视角中表现为纹理漂移、印花模糊和几何不合理。论文要解决的是如何在 3DGS 试穿中实现跨视角一致的编辑。

### 核心思路/方法
论文提出 GS-VTON-MVT，一个结合隐式与显式 3D 推理的三阶段框架：
1. 多视角修复 Transformer：对一组训练视角联合编辑，使用完整的跨视角自注意力，使跨视角对应关系被学习而非人为施加。
2. 几何引导多模态 ControlNet：以 garment 图像以及从当前 3DGS 状态渲染出的深度和表面法线为条件，引导扩散编辑器，在视觉证据最弱处提供显式结构。
3. 姿态自适应 persona-aware 注意力：用基于相机姿态邻近度推导的权重，替代当前视角与参考视角特征之间的固定混合权重。

### 主要贡献
- 提出 GS-VTON-MVT 三阶段框架，用于一致的 3DGS 虚拟试穿。
- 用带完整跨视角自注意力的多视角修复 Transformer 联合编辑训练视角，使跨视角对应关系可学习。
- 引入几何引导多模态 ControlNet，将 garment 图像与当前 3DGS 渲染的深度、表面法线共同作为扩散编辑条件。
- 用姿态自适应 persona-aware 注意力替代固定混合权重。
- 在 3D-VTONBench 基准上，相比通用 3D 编辑器和既有 3D 试穿方法，在 FID、KID、基于 LPIPS 的跨视角一致性和用户偏好上有所提升。

### 局限性
摘要未提供足够信息。摘要未给出计算开销、推理速度、对训练视角数量或质量的敏感性、失败案例、用户研究规模与统计细节，也未说明各模块的消融实验结果。

### 阅读优先级
中。理由：该论文针对 3DGS 虚拟试穿中的跨视角一致性提出明确的三阶段方法，并在摘要中报告了基准指标与用户偏好提升；但摘要未提供实验细节、消融和局限性信息。是否优先精读取决于读者对 3D 虚拟试穿、多视角扩散编辑或几何引导 ControlNet 的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Editing a 3D Gaussian Splatting (3DGS) capture of a person so that they wear a new garment requires every rendered view to agree on the same garment details. Existing 3D virtual try-on (VTON) pipelines, however, edit training views largely independently and fuse them with hand-designed heuristics such as manually chosen reference views and fixed attention-blending weights. The resulting inconsistencies are baked into the 3D representation and surface as texture drift, blurred prints, and implausible geometry in novel views. We present GS-VTON-MVT, a three-stage framework that combines implicit and explicit 3D reasoning for consistent 3DGS try-on. (i) A multi-view inpainting transformer jointly edits a set of training views with full cross-view self-attention, so that cross-view correspondence is learned rather than imposed. (ii) A geometry-guided multi-modal ControlNet conditions the diffusion editor on the garment image together with depth and surface normals rendered from the current 3DGS state, supplying explicit structure where visual evidence is weakest. (iii) A pose-adaptive persona-aware attention replaces the fixed blending weight between current-view and reference-view features with weights derived from camera-pose proximity. On the 3D-VTONBench benchmark, GS-VTON-MVT improves FID, KID, LPIPS-based cross-view consistency, and user preference over general-purpose 3D editors and prior 3D try-on methods.

</details>

#### 2026-11-18 - What Do Learned 3D Models Add to Localization from Posed References?

**Authors:** Jaehyun Kim, Wonseok Kang, Jeongmin Lee, Tae-Wan Kim
**Links:** [abs](https://arxiv.org/abs/2611.23697) - [pdf](https://arxiv.org/pdf/2611.23697)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, point map, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：What Do Learned 3D Models Add to Localization from Posed References?
- 作者：Jaehyun Kim, Wonseok Kang, Jeongmin Lee, Tae-Wan Kim
- 出版日期：2026-11-18T01:41:16Z
- 分类：Geometry Foundation Models
- 链接：摘要页 https://arxiv.org/abs/2611.23697 ；PDF https://arxiv.org/pdf/2611.23697

### 一句话总结
论文系统比较了学习式 3D 模型与几何估计方法在“基于少量带位姿参考图像进行查询定位”任务中的表现差异、增益来源与失败阶段。

### 研究问题
论文关注：在仅使用少量带位姿参考图像、不构建 3D 点图的定位设定下，学习式 3D 模型的相机位姿预测相对于基于同一组参考图像的几何估计究竟带来了什么增量；这些模型的增益在何种参考预算、参考选择和检索条件下成立；以及失败出现在哪些环节。

### 核心思路/方法
- 在八个学习式 3D 模型及其变体、五个测试集上进行比较。
- 改变参考图像预算，交换位姿分量，并对模型所看到的参考图像进行干预。
- 在细粒度位姿误差阈值下，比较几何估计与学习式模型的定位精度。
- 使用共享接受门控，考察几何估计单独使用或作为回退方案的效果。
- 分析学习式平移幅度的增益与参考选择之间的关系。
- 在检索返回其他地点参考图像时，分析模型失败的不同阶段。
- 通过受控测试考察稳健对齐、附近参考对齐、位姿条件模型输入掩码等干预的影响。

### 主要贡献
- 在多个学习式 3D 模型、变体和测试集上，系统比较学习式相机预测与几何估计在少参考定位中的表现。
- 指出在 Cambridge 和 NAVER B1 上，细粒度位姿误差阈值下，使用一个额外参考的几何估计显著优于所有模型使用两个参考的结果，并且无论单独使用还是作为共享接受门控后的回退方案，都不显著更差。
- 指出在相同三个参考下，更准确的方法取决于场景。
- 揭示学习式平移幅度的增益依赖参考选择：在 12-Scenes 上使用所选分散参考对时，八个模型中有七个得到改善；但使用排名最高的两个检索参考时，五个受测模型均未改善。
- 在 NAVER Gangnam Station 的跨地点检索参考条件下，指出模型会在不同阶段失败；稳健对齐可使 Pi3X 和 MapAnything 与按需增加参考的差距缩小到 3.3 个百分点以内。
- 在受控测试中，基于附近参考进行对齐可较大程度恢复 VGGT、Pi3X 和 MapAnything，但不能恢复 Depth Anything 3；位姿条件 Pi3X 仅在对远位姿进行掩码并将其排除出输入位姿归一化时才能恢复。

### 局限性
- 摘要未提供足够信息说明各测试集的具体构成、评价指标定义和统计显著性检验细节。
- 摘要未提供足够信息说明八个学习式 3D 模型的具体名称与完整变体设置。
- 摘要未提供足够信息说明“共享接受门控”的具体设计与阈值。
- 摘要未提供足够信息说明失败阶段的具体分类标准和定量分布。
- 摘要未提供足够信息说明计算成本、推理效率或实际部署相关限制。

### 阅读优先级
中。理由：论文问题聚焦且比较设计较系统，适合关注少参考定位、学习式 3D 模型可靠性及几何估计基线的研究者阅读；但摘要未给出完整实验细节和模型清单，是否高优先级取决于读者对“学习式 3D 模型相对几何估计的增量价值”这一具体问题的兴趣。

</details>

<details>
<summary>Abstract</summary>

Localizing a query from a few posed reference images avoids building a 3D point map. We ask what the camera predictions of learned 3D models add to geometric estimation from the same references, and where failures arise. Across eight learned models and variants and five test sets, we compare reference budgets, swap pose components, and intervene on the references a model sees. At fine pose-error thresholds, geometric estimation with one additional reference is significantly more accurate than every model on two references on Cambridge and NAVER B1 and never significantly worse, alone or as a fallback behind a shared acceptance gate; with the same three references, the more accurate approach depends on the scene. The gain from the learned translation magnitude depends on reference selection: it improves seven of the eight models on 12-Scenes with the spread-out pairs we select, but none of the five we test with the two top-ranked retrieved references. Where retrieval also returns references from other locations, at NAVER Gangnam Station, models fail at different stages. A robust alignment brings Pi3X and MapAnything within 3.3 pp of adding references as needed. In controlled tests, aligning on the nearby references largely restores VGGT, Pi3X and MapAnything but not Depth Anything 3, and pose-conditioned Pi3X recovers only if the far poses are masked and left out of its input-pose normalization.

</details>

#### 2026-11-17 - Layer-Matched Sparse Attention for Low-Redundancy 3D Reconstruction

**Authors:** Sammam Mahdi, Fariha Binta Salim, K. M. Jubair Sami, Rakin Bin Rabbani
**Links:** [abs](https://arxiv.org/abs/2611.23554) - [pdf](https://arxiv.org/pdf/2611.23554)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Layer-Matched Sparse Attention for Low-Redundancy 3D Reconstruction
- 作者：Sammam Mahdi, Fariha Binta Salim, K. M. Jubair Sami, Rakin Bin Rabbani
- 出版日期：2026-11-17T22:01:43Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.23554 ；PDF https://arxiv.org/pdf/2611.23554

### 一句话总结
针对 VGGT 全局注意力随视角数二次增长的问题，论文指出现有免训练稀疏加速器在低冗余视角下损失位姿精度，并提出按层区分“扩散层”与“匹配层”的分层稀疏注意力（LMSA），在低冗余场景中更接近稠密注意力。

### 研究问题
VGGT 能从无位姿图像一次性重建相机与几何，但其全局注意力随视角数二次增长。已有免训练稀疏加速器在冗余视频上表现良好，但当视角间共享几何很少时，位姿精度下降。论文将这一损失归因于两类跨视角信息难以被统一稀疏近似同时保留：扩散层聚合分布式上下文，匹配层依赖查询特定、注意力质量很小的交互。

### 核心思路/方法
- 用逐层统计量衡量“均值 token”遗漏的 log-mass，并以无行依赖的代理指标（logit 方差）为每层选择估计器。
- 扩散层：采用共享的、重要性采样的 hub keys，并用 log 权重使 softmax 分子与分母无偏。
- 匹配层：保持精确计算；摘要称测试过的所有激进稀疏化都会损失精度。
- 在同等成本下，所选层优于测试的四种 shifted windows。

### 主要贡献
- 揭示统一稀疏近似在低冗余视角下失效的原因，并区分扩散层与匹配层的不同稀疏需求。
- 提出可逐层选择估计器的 LMSA 方法，兼顾扩散层的无偏稀疏近似与匹配层的精确计算。
- 在 13 个未见低冗余场景、32 视角下，LMSA 与稠密注意力 AUC@5 差距为 1.4，对比 AVGGT 的 10.3 与 SAF3R 的 4.5；与同期 GPA-VGGT 差异不显著，且仅其对 AVGGT 的增益通过两项场景级检验。
- 100 视角时保持 AUC@5 差距 1.9，且聚合器运行速度快 2.0 倍。
- 将该统计量事后用于选择 GPA-VGGT 保护的层，以增加 5% FLOPs 换来 1.2 AUC@5 提升；未调参用于 π³ 时优于 AVGGT，但距稠密精度仍更远。

### 局限性
摘要未提供足够信息。可确认的边界包括：匹配层未采用稀疏化；在 π³ 上仍未达到稠密精度；与 GPA-VGGT 的差异不显著，且仅对 AVGGT 的增益通过两项场景级检验。其他实验细节、数据集构成与计算开销的完整分析，摘要未提供足够信息。

### 阅读优先级
中。理由：论文聚焦 3D 重建基础模型中全局注意力的免训练加速，问题明确且有低冗余场景的定量对比；但摘要仅给出有限指标与部分显著性结论，未展开实验设置与实现细节，适合关注 VGGT 类模型效率与稀疏注意力的读者进一步阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

VGGT reconstructs cameras and geometry from unposed images in one pass, but its global attention grows quadratically with the number of views. Training-free accelerators thin this attention and work well on redundant video, but lose pose accuracy when views share little geometry. This paper traces these losses to two kinds of cross-view information that a uniform sparse approximation can fail to preserve together: diffuse layers aggregate distributed context, whereas matching layers depend on query-specific interactions that carry little attention mass. A per-layer statistic measures the log-mass missed by a mean token. Its row-free proxy is the logit variance, and it selects the estimator for each layer. Diffuse layers use shared, importance-sampled hub keys, with log-weights that make the softmax numerator and denominator unbiased. Matching layers stay exact: every aggressive thinning tested cost accuracy. At equal cost, the selected layers outperform the four shifted windows tested. On 13 unseen low-redundancy scenes with 32 views, LMSA stays within 1.4 AUC@5 of dense attention, compared with 10.3 for AVGGT and 4.5 for SAF3R; its difference from contemporaneous GPA-VGGT is not significant, and only its gains over AVGGT pass both scene-level tests. With 100 views, it stays within 1.9 AUC@5 while its aggregator runs $2.0\times$ faster. Used post hoc to choose the layers GPA-VGGT protects, the statistic improves it by 1.2 AUC@5 for 5% more FLOPs. Applied untuned to $π^3$, it beats AVGGT but remains further from dense accuracy.

</details>

#### 2026-11-17 - Refin3R: Geometry-Guided Refinement for Feed-Forward 3D Reconstruction

**Authors:** Jongmin Lee, Jaeyeong Kim, Seungryong Kim
**Links:** [abs](https://arxiv.org/abs/2611.23051) - [pdf](https://arxiv.org/pdf/2611.23051)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** point map, feed-forward 3D reconstruction, 3D reconstruction, structure from motion, SfM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Refin3R: Geometry-Guided Refinement for Feed-Forward 3D Reconstruction
- 作者：Jongmin Lee, Jaeyeong Kim, Seungryong Kim
- 出版日期：2026-11-17T16:46:34Z
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（次分类）
- 链接：[摘要](https://arxiv.org/abs/2611.23051) | [PDF](https://arxiv.org/pdf/2611.23051)

### 一句话总结
Refin3R 利用 Structure-from-Motion（SfM）点对前馈式点图预测进行几何引导的细化，通过 2D 与 3D 双分支双向交互，生成稠密且准确的点图。

### 研究问题
前馈式 3D 重建模型能在单次前向中从多张图像预测稠密点图，但缺乏显式几何约束时，预测往往跨视图不一致且缺乏细粒度精度。已有方法虽引入相机位姿或深度等几何先验，但仅将其作为辅助输入、逐视图独立处理，或只在先验可用处细化几何，未能充分利用几何信息。

### 核心思路/方法
- 以 SfM 点为几何引导，在图像网格上传播 SfM 几何，对前馈点图进行细化。
- 采用双分支架构：
  - 2D 分支借助几何感知的骨干特征，将 SfM 几何扩展到其覆盖范围之外；
  - 3D 分支对所有视图的 SfM 点进行推理，捕捉图像网格本身无法表示的多视图结构。
- 两个分支双向交换信息，联合细化每个视图，输出稠密且准确的点图。

### 主要贡献
- 提出 Refin3R，用 SfM 点细化前馈点图，并将 SfM 几何在图像网格上传播。
- 设计 2D/3D 双分支架构，分别负责扩展 SfM 几何覆盖范围与建模多视图结构，并通过双向信息交换联合细化各视图。
- 据摘要，在 ScanNet++、ETH3D、Tanks & Temples 以及域外的人体与手术场景上，点图精度一致优于前馈式和几何引导方法，且运行速度快于最强的几何引导基线。

### 局限性
- 摘要未提供足够信息说明方法对 SfM 点质量或覆盖度的依赖程度及失效情形。
- 摘要未提供足够信息说明各数据集上的具体量化指标、运行时间数值与消融实验结果。
- 摘要未提供足够信息说明双分支的具体网络结构、训练策略与实现细节。
- 摘要未提供足够信息说明在极端稀疏视角或 SfM 失败场景下的表现。

### 阅读优先级
中。理由：该工作针对前馈式 3D 重建的跨视图一致性与精度问题，提出以 SfM 点为几何引导的双分支细化框架，并在多个数据集及域外场景报告了精度与速度优势，对多视图几何与 3D 重建方向有参考价值；但摘要未给出量化结果与实现细节，需阅读全文才能评估其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models predict dense point maps from multiple images in a single pass. Without explicit geometric constraints, however, their predictions are often inconsistent across views and lack fine-grained precision. Recent methods incorporate geometric priors such as camera pose or depth, but use them merely as auxiliary inputs, process each view independently, or refine the geometry only where the priors are available. We present Refin3R, which refines feed-forward point maps with Structure-from-Motion (SfM) points, propagating SfM geometry over the image grid. In its dual-branch architecture, a 2D branch extends SfM geometry beyond its coverage using geometry-aware backbone features, while a 3D branch reasons over the SfM points of all views, capturing multi-view structure that the image grid alone cannot represent. The two branches exchange information bidirectionally to jointly refine each view, yielding dense and accurate point maps. Across ScanNet++, ETH3D, Tanks\&Temples, and out-of-domain human and surgical scenes, Refin3R consistently outperforms feed-forward and geometry-guided methods in point map accuracy while running faster than the strongest geometry-guided baseline.

</details>

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-19 - Plan4D: Generative Plannable 4D Worlds

**Authors:** Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
**Links:** [abs](https://arxiv.org/abs/2611.26516) - [pdf](https://arxiv.org/pdf/2611.26516)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D, scene flow, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Plan4D: Generative Plannable 4D Worlds
- 作者：Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
- 出版日期：2026-11-19T17:59:02Z
- 分类：主分类为 Dynamic / 4D Reconstruction；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.26516 ；PDF https://arxiv.org/pdf/2611.26516 ；项目页 https://fogradio.github.io/plan4d-project

### 一句话总结
Plan4D 提出一种生成式可规划的 4D 世界模型，旨在根据观测场景上下文与文本指定动作，联合预测未来 RGB 视频及稠密 4D 几何（深度、相机、点云和场景流）。

### 研究问题
摘要指出，现有面向未来预测的世界模型大多优先追求生成视频的美学质量，但缺乏显式 4D 建模，导致物理基础较弱、跨时间几何一致性有限。论文关注的问题是：如何构建一个可规划的生成式 4D 世界模型，在给定场景上下文和文本动作的条件下，同时预测未来视频与稠密 4D 几何，并支持复杂、长时程、细粒度动作的规划与生成。

### 核心思路/方法
由于带有配对动作和稠密 4D 标注的训练数据本身稀缺，Plan4D 利用基础视频生成器与 3D 重建器的互补先验。具体而言，论文提出一种“模型缝合”（model-stitching）架构：将 Depth Anything 3 与 LongCat-Video 耦合，并增加一个辅助 DPT 头用于场景流预测。该模型用于在动态 3D 场景中规划并生成复杂、长时程、细粒度动作，同时提升生成未来视频的视觉保真度与几何精度。

### 主要贡献
- 提出 Plan4D，面向生成式可规划 4D 世界模型，联合预测未来 RGB 视频与稠密 4D 几何，包括深度、相机、点云和场景流。
- 针对配对动作与稠密 4D 标注数据稀缺的问题，提出利用基础视频生成器与 3D 重建器互补先验的模型缝合架构。
- 将 Depth Anything 3 与 LongCat-Video 耦合，并引入辅助 DPT 头进行场景流预测。
- 摘要称在合成与真实世界数据集上的广泛实验表明，Plan4D 在环境反应的生成式 4D 建模上达到最先进性能，并显著提升生成未来视频的视觉保真度与几何精度。

### 局限性
- 摘要未提供足够信息说明模型的具体失败模式或适用范围限制。
- 摘要未提供足够信息说明对训练数据规模、数据域差异或标注质量的敏感程度。
- 摘要未提供足够信息说明推理效率、计算成本或实时性表现。
- 摘要未提供足够信息说明“模型缝合”架构中各基础模型的误差传播或相互依赖问题。
- 摘要未提供足够信息说明长时程生成中的误差累积程度及定量评估细节。

### 阅读优先级
中。理由：该论文聚焦生成式 4D 世界建模、视频生成与 3D 重建先验结合，以及文本动作条件下的 4D 几何预测，主题与动态/4D 重建方向直接相关；摘要给出了明确的问题动机、方法框架和性能主张。但摘要未提供实验细节、定量结果、失败案例与效率信息，是否高优先级阅读需结合读者对生成式世界模型、视频生成与 4D 几何联合建模的具体兴趣；若关注该方向，可优先阅读原文实验部分。

</details>

<details>
<summary>Abstract</summary>

Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit 4D modeling. In this paper, we introduce plan4d, a possible next milestone towards building a generative plannable 4D world model that predicts future RGB videos together with dense 4D geometry, including depth, cameras, point clouds, and scene flow from an observed scene context and text-specified actions. Since training data with paired actions and dense 4D annotations is inherently scarce, plan4d leverages the complementary priors of foundational video generators and 3D reconstructors. Specifically, we propose a model-stitching architecture that couples Depth Anything 3 with LongCat-Video and augments it with an auxiliary DPT head for scene-flow prediction. The resulting model allows us to plan and generate complex, long-horizon, and fine-grained actions in a dynamic 3D scenes, while substantially improving both visual fidelity and geometric accuracy of the generated future videos. Extensive experiments on both synthetic and real-world datasets demonstrate that plan4d achieves state-of-the-art performance in generative 4D modeling of environmental reactions. Project Page: https://fogradio.github.io/plan4d-project

</details>

#### 2026-11-18 - Freeforward4d: Annotation-free feed-forward 4d reconstruction of driving scenes

**Authors:** Luosong Guo, Xiang Yang, Chaoyang Li, Ao Gao, Jiangming Shi, Yanyun Qu, Zhizhong Zhang, Jingyu Gong, Yuan Xie
**Links:** [abs](https://arxiv.org/abs/2611.24007) - [pdf](https://arxiv.org/pdf/2611.24007)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, 4D reconstruction, monocular depth, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Freeforward4d: Annotation-free feed-forward 4d reconstruction of driving scenes
- 作者：Luosong Guo, Xiang Yang, Chaoyang Li, Ao Gao, Jiangming Shi, Yanyun Qu, Zhizhong Zhang, Jingyu Gong, Yuan Xie
- 出版日期：2026-11-18T07:58:19Z
- 分类：主分类为 Dynamic / 4D Reconstruction；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.24007 ；PDF https://arxiv.org/pdf/2611.24007

### 一句话总结
FreeForward4D 提出一种仅依赖 RGB 视频、无需数据集相机/ LiDAR 深度/3D 框标注的前馈 4D 驾驶场景重建方法，通过将预训练视觉模型的多视角与单目预测校准到统一度量坐标系，替代数据集标注。

### 研究问题
现有前馈 4D 重建方法多依赖数据集提供的相机参数、LiDAR 深度或 3D 框标注，难以应用于无标注驾驶视频。虽然预训练视觉模型可从 RGB 单独预测相机、深度和物体轨迹，但这些预测的几何彼此不一致：多视角预测以短窗口形式出现且尺度与帧独立，单目深度仅在单图像内为度量尺度。论文要解决的是：如何在不使用数据集标注的情况下，协调这些不一致的几何先验，实现可渲染的前馈 4D 驾驶场景重建。

### 核心思路/方法
论文的关键思路是：一旦将上述先验调和到单一度量坐标系中，它们便可替代数据集标注用于前馈 4D 重建。具体而言，FreeForward4D 将重叠的预测窗口相对单目度量深度进行校准，并在时间上配准到同一坐标系。在该几何基础上，2D 轨迹跨相机在 3D 中进行关联，物体通过分层运动建模运动，该运动结合共享物体速度与局部高斯修正，从而使训练和推理仅使用 RGB 视频。

### 主要贡献
- 提出 FreeForward4D，一种无需标注的前馈 4D 驾驶场景重建框架，训练和推理仅使用 RGB 视频。
- 通过将重叠预测窗口相对单目度量深度校准并跨时间配准到统一坐标系，协调预训练视觉模型的多视角与单目几何先验。
- 在该几何上实现跨相机 2D 轨迹在 3D 中的关联，并采用结合共享物体速度与局部高斯修正的分层运动表示。
- 在 Waymo 上达到 27.66 dB PSNR 和 0.836 SSIM，并在无尺度对齐情况下恢复度量尺度的相机与深度；在全图 PSNR 上超过依赖数据集标注的 STORM、SLARM-F、UFO、DGGT 和 StreetForward，并在 8 秒窗口上取得最佳 RGB 保真度。仅 RGB 微调可进一步适配 nuScenes 和 Argoverse 2。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算开销、对预训练视觉模型质量的敏感度、在极端场景或更长窗口下的表现，以及定量比较的完整实验设置与统计细节。摘要也未提供足够信息说明 nuScenes 与 Argoverse 2 上的具体适配结果数值。

### 阅读优先级
中。理由：该论文针对无标注前馈 4D 驾驶场景重建提出明确的几何调和思路，并在 Waymo 上给出定量结果与对多个依赖标注方法的比较，主题与动态/4D 重建及驾驶仿真相关；但摘要未提供足够信息评估其泛化性、失败模式与实验细节，是否优先精读取决于读者对无标注 4D 重建和预训练视觉先验协调问题的兴趣。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 4D reconstruction enables efficient creation of renderable driving scenes for autonomous driving simulation. However, most existing methods rely heavily on dataset-provided cameras, LiDAR depth, or 3D box annotations, limiting their applicability to unannotated driving videos. Pretrained visual models can predict cameras, depth, and object tracks from RGB alone, but their geometry is mutually inconsistent: multi-view predictions come in short windows with independent scales and frames, while monocular depth is metric only per image. Our key insight is that, once reconciled into a single metric frame, these priors can replace dataset annotations for feed-forward 4D reconstruction. We present \textbf{FreeForward4D}, which calibrates overlapping prediction windows against monocular metric depth and registers them into one frame across time. On this geometry, 2D tracks are associated across cameras in 3D, and objects move through hierarchical motion that combines a shared object velocity with local Gaussian corrections, so that both training and inference use only RGB videos. On Waymo, FreeForward4D achieves 27.66 dB PSNR and 0.836 SSIM while recovering metric-scale cameras and depth without scale alignment. It surpasses STORM, SLARM-F, UFO, DGGT, and StreetForward, which rely on dataset annotations, in full-image PSNR and attains the best RGB fidelity on 8-second windows. RGB-only fine-tuning further adapts the framework to nuScenes and Argoverse 2. Code will be released.

</details>

#### 2026-11-18 - TRoPE: Topology-aware Relative Positional Encoding for 4D Generation

**Authors:** Chengzhuo Gui, Zhenglin Zhou, Fan Ma, Zongxin Yang, Yi Yang
**Links:** [abs](https://arxiv.org/abs/2611.23933) - [pdf](https://arxiv.org/pdf/2611.23933)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D, video-to-4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRoPE: Topology-aware Relative Positional Encoding for 4D Generation
- 作者：Chengzhuo Gui, Zhenglin Zhou, Fan Ma, Zongxin Yang, Yi Yang
- 出版日期：2026-11-18T06:23:09Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要页 https://arxiv.org/abs/2611.23933 ；PDF https://arxiv.org/pdf/2611.23933

### 一句话总结
论文针对视频到4D网格生成中的“粘连伪影”（sticking artifacts），提出拓扑感知的相对位置编码 TRoPE，并配套尾风险目标与专用基准 MeshSticking-4D，以抑制空间邻近但结构远离的顶点发生错误同步运动。

### 研究问题
摘要指出，视频到4D网格生成在从单目视频恢复动态3D几何与运动方面已有显著进展，但常用前馈方法仍易出现粘连伪影：测地距离远的顶点在空间上靠近时会错误地一起运动。作者将其归因于“跨部件运动泄漏”：当运动解码未能区分空间邻近性与网格连通性时，空间上接近但结构上远离的顶点可能检索到相似的运动信息。论文旨在让网格连通性在顶点查询与网格支持的运动源之间的交互中显式化，并更好地刻画和量化该失败模式。

### 核心思路/方法
- 提出 TRoPE（Topology-aware Relative Positional Encoding），一种拓扑感知的相对位置编码，使网格连通性在顶点查询与网格支持的运动源交互中显式表达。
- 从图拉普拉斯（graph Laplacian）导出谱特征，并基于多尺度扩散特征之间的距离构建成对拓扑关系。
- 利用上述拓扑关系，通过旋转相位（rotary phases）调制顶点—锚点注意力（vertex–anchor attention）。
- 引入逐顶点尾风险目标（vertex-wise tail-risk objective），强调持续高误差顶点，以显式抑制粘连伪影。
- 提出 MeshSticking-4D，一个专门针对该失败模式的基准，用于更好地刻画和量化粘连问题。

### 主要贡献
- 识别并归因视频到4D网格生成中的粘连伪影为跨部件运动泄漏，即运动解码未区分空间邻近与网格连通性。
- 提出 TRoPE，将网格拓扑关系通过谱特征与多尺度扩散特征构建，并以旋转相位调制顶点—锚点注意力。
- 引入逐顶点尾风险目标，针对持续高误差顶点抑制粘连伪影。
- 提出专用基准 MeshSticking-4D，用于刻画和量化该失败模式。
- 摘要报告：在 MeshSticking-4D 上，相比基线，最差顶点误差降低39.4%，分离失败率从49.35%降至34.90%；在 Motion-80 与 Motion324-Subset 上尾误差更低；迁移到 Mesh4D 表明可跨骨干适用。

### 局限性
- 摘要未提供足够信息说明方法在不同骨干、不同数据分布或实时性方面的具体限制。
- 摘要未提供足够信息说明 MeshSticking-4D 的构建细节、规模与覆盖范围。
- 摘要未提供足够信息说明尾风险目标与其他损失项的相对权重、训练成本或超参数敏感性。
- 摘要未提供足够信息说明在非网格表示或更复杂拓扑场景下的适用性。

### 阅读优先级
中。理由：论文聚焦视频到4D网格生成中明确的失败模式（粘连伪影），提出拓扑感知位置编码与专用基准，并给出最差顶点误差与分离失败率的量化改善，对动态/4D重建与网格运动学习方向有直接参考价值；但摘要未展开方法细节、基准构成与跨骨干实验设置，需阅读全文才能判断其泛化性与实际代价。

</details>

<details>
<summary>Abstract</summary>

Video-to-4D mesh generation has made substantial progress in recovering dynamic 3D geometry and motion from monocular videos. However, commonly used feed-forward approaches remain prone to sticking artifacts, where geodesically distant vertices move together incorrectly when they become spatially close. We attribute this failure to cross-part motion leakage: spatially nearby yet structurally distant vertices may retrieve similar motion information when motion decoding fails to distinguish spatial proximity from mesh connectivity. To address this issue, we introduce TRoPE, a topology-aware relative positional encoding that makes mesh connectivity explicit in the interaction between vertex queries and mesh-supported motion sources. TRoPE derives spectral features from the graph Laplacian and constructs pairwise topological relations from distances between multi-scale diffusion features, using these relations to modulate vertex--anchor attention through rotary phases. We further introduce a vertex-wise tail-risk objective that emphasizes persistently high-error vertices to explicitly suppress sticking artifacts. To better characterize and quantify these failures, we introduce MeshSticking-4D, a dedicated benchmark for this failure mode. Experiments on MeshSticking-4D show that TRoPE suppresses sticking artifacts while improving overall motion accuracy. Compared with the baseline, it reduces the worst-vertex error by 39.4% and lowers the separation failure rate from 49.35% to 34.90%. Additional evaluations on Motion-80 and Motion324-Subset show lower tail errors on diverse objects, while transfer to Mesh4D demonstrates applicability across backbones.

</details>

#### 2026-11-17 - ARG-Avatar: Animation-Rendering Guidance for Efficient Feedforward Avatar Reconstruction

**Authors:** Jianjin Xu, Soham Dasgupta, Fernando De la Torre
**Links:** [abs](https://arxiv.org/abs/2611.22207) - [pdf](https://arxiv.org/pdf/2611.22207)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** avatar reconstruction, rendering, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ARG-Avatar: Animation-Rendering Guidance for Efficient Feedforward Avatar Reconstruction
- 作者：Jianjin Xu, Soham Dasgupta, Fernando De la Torre
- 出版日期：2026-11-17T04:45:07Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.22207) ｜ [PDF](https://arxiv.org/pdf/2611.22207)

### 一句话总结
提出一种仅含 68M 可训练参数的高效前馈虚拟人重建框架 ARG-Avatar，利用动画与渲染提供的几何对应关系引导注意力，以更少参数、数据和算力取得 SOTA 重建质量。

### 研究问题
从图像重建可动画的 3D 人体虚拟人对游戏和增强现实等应用很重要。前馈方法把推理时间缩短到数秒，但近期方法严重依赖扩大模型容量、训练数据和计算量。作者追问：这种规模化是否必要？摘要将问题定位为在保持前馈效率的同时，避免依赖大规模扩展来获得高质量重建。

### 核心思路/方法
核心洞察是：3D 动画和渲染本身已提供强几何对应关系，而现有方法大多试图从数据中学习这些关系。基于此，作者设计了两项组件：
- Foreground Avatar Coordinate RoPE attention（FACRoPE）注意力机制；
- Intermediate Token Rendering（ITR）流程。

二者用于引导 avatar tokens 关注其对应的 patches，从而在前馈框架中利用动画-渲染引导实现高效重建。模型仅有 68M 可训练参数。

### 主要贡献
- 提出 ARG-Avatar，一个仅含 68M 可训练参数的高效前馈虚拟人重建框架，并达到 SOTA 重建质量。
- 提出 FACRoPE 注意力和 ITR 流程，利用动画与渲染提供的几何对应关系引导 token 与 patch 的对应注意力。
- 在多个数据集上验证：当使用两张或更多输入图像时，ARG-Avatar 持续优于先前方法。
- 与 LHM++ 相比：可训练参数约少 9 倍，训练序列约少 4.8 倍，训练计算约少 14 倍，运行速度快 6 倍；在分布外 NeuMan 基准上 PSNR 提升 2.7 dB。

### 局限性
- 摘要仅说明“使用两张或更多输入图像”时持续优于先前方法，未提供单张输入图像场景的表现，具体限制未说明。
- 摘要未提供失败案例、泛化边界、对特定数据分布的依赖等细节。
- 摘要未提供训练数据规模、模型结构细节及消融实验的具体设置。
- 其他潜在局限：摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直接挑战“前馈虚拟人重建必须依赖大规模扩展”的假设，以 68M 参数取得 SOTA，并给出相对 LHM++ 的参数、数据、算力、速度和 PSNR 多项定量对比；同时涉及 FACRoPE 与 ITR 两个可复用设计，对动态/4D 重建与高效前馈方法研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing animatable 3D human avatars from images is important for applications such as gaming and augmented reality. Feedforward methods make avatar reconstruction accessible by reducing inference time to a few seconds, but recent approaches rely heavily on scaling model capacity, training data, and computation. We ask whether such scaling is necessary. To this end, we introduce ARG-Avatar, an efficient feedforward framework with only 68M trainable parameters that achieves SOTA reconstruction quality. Our key insight is that 3D animation and rendering already provide strong geometric correspondences that existing methods largely attempt to learn from data. In light of this, we design the Foreground Avatar Coordinate RoPE attention (FACRoPE) and Intermediate Token Rendering (ITR) pipeline to guide avatar tokens to attend to their corresponding patches. Experiments across multiple datasets show that ARG-Avatar consistently outperforms prior methods when using two or more input images. Compared with LHM++, ARG-Avatar uses approximately 9$\times$ fewer trainable parameters, 4.8$\times$ fewer training sequences, and 14$\times$ less training compute, while running 6$\times$ faster and achieving a 2.7 dB PSNR improvement on the out-of-distribution NeuMan benchmark.

</details>

#### 2026-11-17 - VTT: Reading Vehicle Size and Powertrain Type from Motion Trajectory Across Unseen Car Models

**Authors:** Yuhang Wang, Yuechen Guo, Jingxin Yang, Chuheng Wei, Suyang Chen, Abdulaziz Alhuraish, Yiyi Wang, Mingyang Ban, Jingran Sun, Hao Zhou
**Links:** [abs](https://arxiv.org/abs/2611.22109) - [pdf](https://arxiv.org/pdf/2611.22109)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion trajectory, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VTT: Reading Vehicle Size and Powertrain Type from Motion Trajectory Across Unseen Car Models
- 作者：Yuhang Wang, Yuechen Guo, Jingxin Yang, Chuheng Wei, Suyang Chen, Abdulaziz Alhuraish, Yiyi Wang, Mingyang Ban, Jingran Sun, Hao Zhou
- 出版日期：2026-11-17T02:49:01Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要页 https://arxiv.org/abs/2611.22109 ；PDF https://arxiv.org/pdf/2611.22109

### 一句话总结
论文提出 VTT 数据集与基准，用于在未见过的车型上从运动轨迹和 CAN 信号识别车辆尺寸类别与动力类型，并比较序列模型、统计特征及大语言模型提出的物理特征。

### 研究问题
如何从车辆运动与控制器局域网（CAN）信号中识别车辆尺寸和动力类型，并在未见过的车型和未见过的驾驶员条件下评估跨车型泛化能力；同时比较不同输入特征与序列架构在该任务上的表现。

### 核心思路/方法
构建包含 9,062 次行驶、约 3,950 小时、1,431 辆车和 174 个车型的数据集，提供基于 footprint 的三类尺寸标签和动力类型标签，并设置未见车型与未见驾驶员的评估。使用 60 秒窗口，比较四种序列架构、统计特征以及由大语言模型提出的物理特征。训练中采用辅助物理目标、数据增强和任务特定加权。

### 主要贡献
- 提出面向跨未见车型车辆属性识别的 VTT 数据集与基准，包含尺寸类别和动力类型标签。
- 在 60 秒窗口下系统比较四种序列架构、统计特征和大语言模型提出的物理特征。
- 通过辅助物理目标、数据增强和任务特定加权，将纯电与燃油车辆识别的 drive-level macro-F1 提升至 92.6–93.0%，尺寸分类从 62.9% 提升至 67.1%。
- 在额外 4,061 名驾驶员的公开日志上验证：全输入模型对 88 个车型中的 86 个正确识别动力类型；尺寸准确率为 63.2%，接近内部车辆级结果 63.5%。
- 物理特征分析将动力类型识别与减速行为关联，将尺寸识别与转向响应关联。

### 局限性
- 尺寸分类准确率仍明显低于动力类型识别，跨车型尺寸泛化能力有限。
- 摘要指出尺寸类别边界附近存在错误，且更长观测带来的增益有限。
- 摘要强调标签分辨率和训练车队覆盖对跨车型泛化的重要性，但未提供更细粒度的失败案例分析。
- 关于四种序列架构的具体名称、各自性能差异、数据增强与任务加权的详细消融结果，摘要未提供足够信息。
- 公开日志的具体来源、数据分布及与内部数据集的差异，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作涉及车辆轨迹属性识别与跨车型泛化基准，包含数据集、评估协议和多类特征比较，对交通分析、仿真和轨迹数据增强有潜在参考价值；但摘要显示尺寸分类性能仍有限，且部分实验细节未给出，是否优先精读取决于读者对跨车型泛化或 CAN/运动信号建模的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Vehicle size and powertrain information can enrich trajectory data for traffic analysis and simulation. We present VTT, a dataset and benchmark for identifying these attributes from motion and controller area network (CAN) signals across unseen car models. The dataset contains 9,062 drives, about 3,950 h, from 1,431 vehicles and 174 car models. It provides three footprint-based size classes, powertrain labels, and evaluation on unseen car models and unseen drivers. Using 60-s windows, we compare four sequence architectures, statistical features and physical features proposed by large language models. Training with auxiliary physical targets, data augmentation and task-specific weighting raises drive-level macro-F1 to 92.6-93.0% for battery-electric versus combustion vehicles and from 62.9% to 67.1% for size classification. On public logs from 4,061 additional drivers, the full-input model identifies powertrain correctly for 86 of 88 car models; size accuracy is 63.2%, close to the internal vehicle-level result of 63.5%. Physical-feature analysis links powertrain recognition to deceleration behaviour and size recognition to steering response. Errors near size-class boundaries and limited gains from longer observations highlight the importance of label resolution and training-fleet coverage for cross-model generalisation.

</details>

#### 2026-11-17 - CueSplat: Learning to Schedule Sparse Deformation for Dynamic Gaussian Splatting on Edge Devices

**Authors:** Qingyuan Tang, He Zhu, Shixuan Sun, Anbang Wu, Jingwen Leng, Minyi Guo, Yu Feng
**Links:** [abs](https://arxiv.org/abs/2611.22095) - [pdf](https://arxiv.org/pdf/2611.22095)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CueSplat: Learning to Schedule Sparse Deformation for Dynamic Gaussian Splatting on Edge Devices
- 作者：Qingyuan Tang, He Zhu, Shixuan Sun, Anbang Wu, Jingwen Leng, Minyi Guo, Yu Feng
- 出版日期：2026-11-17T02:24:13Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.22095) / [PDF](https://arxiv.org/pdf/2611.22095)

### 一句话总结
CueSplat 是一种训练后框架，通过轻量学习路由器按预算稀疏选择需精确形变更新的高斯，并复用邻近帧选择结果、以漂移信号触发全形变重建历史，从而在边缘设备上加速 4D 高斯泼溅渲染。

### 研究问题
基于形变的 4D 高斯泼溅需要逐帧对所有高斯评估形变网络，这在边缘设备上计算开销很大；而高斯轨迹往往具有局部可预测性，但预测可靠性会随高斯和时间变化。论文试图在保持预训练主干冻结及高斯集合不变的前提下，减少逐帧精确形变评估的计算量。

### 核心思路/方法
- 利用高斯轨迹的局部时间规律性，从近期历史预测高斯属性。
- 使用轻量学习路由器，在离线校准的场景特定预算内选择需要精确形变更新的高斯；选择时考虑预测可靠性与渲染贡献。
- 选择的索引在邻近帧间复用，以降低路由开销；被选中的高斯在每一帧仍获得精确更新。
- 使用漂移信号调度连续三帧全形变，以重建预测历史并控制累积预测误差。
- 方法为训练后框架，保持预训练主干冻结并保留其高斯集合。

### 主要贡献
- 提出 CueSplat 训练后框架，在冻结预训练主干和保留高斯集合的条件下调度稀疏形变。
- 结合历史预测、轻量学习路由器、场景特定离线校准预算、邻近帧索引复用与漂移触发的全形变重建。
- 在四种主流 4DGS 算法上评估，Jetson AGX Orin 和 Orin NX 上分别最高获得 \(6.74\times\) 和 \(8.15\times\) 加速，数据集平均 PSNR 最多下降 \(0.16\) dB。

### 局限性
- 摘要未提供足够信息说明方法在更广泛场景、不同预算设置或极端动态下的泛化表现。
- 摘要未提供足够信息说明连续三帧全形变策略的额外开销细节及其对总体加速的影响。
- 摘要未提供足够信息说明学习路由器的训练数据、离线校准流程与超参数敏感性。
- 摘要未提供足够信息说明除 PSNR 外的其他质量指标、内存占用或能耗表现。

### 阅读优先级
中。理由：论文聚焦边缘设备上的 4DGS 推理加速，问题明确且报告了较大加速与较小 PSNR 下降；但摘要未给出方法细节、完整实验设置与多指标评估，是否高优先级取决于读者对边缘部署和 4D 动态重建加速的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Deformation-based 4D Gaussian splatting (4DGS) enables dynamic scene rendering. However, evaluating deformation networks for all Gaussians at every frame is compute-intensive on edge devices. We find that Gaussian trajectories are often locally predictable, yet prediction reliability varies across Gaussians and time. Thus, we propose CueSplat, a post-training framework that exploits local temporal regularity while keeping the pretrained backbone frozen and retaining its Gaussian set. Specifically, CueSplat predicts Gaussian attributes from recent history and uses a lightweight learned router to select exact deformation updates within a scene-specific budget calibrated offline. Selection accounts for prediction reliability and rendering contribution. Selected indices are reused across nearby frames to reduce routing overhead, while selected Gaussians still receive exact updates each frame. To control accumulated prediction error, we use drift signals to schedule three consecutive full-deformation frames that rebuild the prediction history. Evaluated across four mainstream 4DGS algorithms, CueSplat achieves up to $6.74\times$ and $8.15\times$ speedups on Jetson AGX Orin and Orin NX, respectively, with a negligible quality drop (at most $0.16$ dB in dataset-average PSNR).

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-19 - Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth

**Authors:** Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, Amaël Delaunoy, Stephan R. Richter, Vladlen Koltun
**Links:** [abs](https://arxiv.org/abs/2611.26603) - [pdf](https://arxiv.org/pdf/2611.26603)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth
- 作者：Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, Amaël Delaunoy, Stephan R. Richter, Vladlen Koltun
- 出版日期：2026-11-19T18:55:41Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.26603 ；PDF https://arxiv.org/pdf/2611.26603 ；代码与权重 https://apple-aiml-research.github.io/ml-depth-pro-2/

### 一句话总结
Depth Pro 2 提出一种单一可扩展网络，同时处理图像与视频，并在原生分辨率下预测稠密度量深度，试图同时兼顾度量精度、边界锐利性与时序一致性。

### 研究问题
论文关注单目稠密度量深度估计，尤其是图像与视频在全分辨率下的深度预测。作者指出既有方法通常存在权衡：多帧方法更偏向时序一致性，单帧方法更偏向边界锐利性，因此难以同时获得时序一致与边界锐利的结果。论文要解决的问题是在保持度量准确的同时，同时实现锐利边界和时序一致。

### 核心思路/方法
根据摘要，方法核心是训练一个单一、可扩展的网络，统一处理图像和视频，并直接在原生分辨率下预测深度图。其出发点是分析既有单目深度方法的“时序一致性 vs 边界锐利性”权衡，并通过统一网络设计来克服该权衡，使输出同时具备度量准确、锐利和时序一致。摘要未提供足够信息说明具体网络结构、训练数据、损失函数或视频帧融合机制。

### 主要贡献
- 提出 Depth Pro 2，用于图像和视频的全分辨率稠密度量深度估计。
- 通过单一可扩展网络同时处理图像与视频，声称可同时获得度量准确、边界锐利和时序一致的深度图。
- 摘要称其在度量精度、锐利性和时序一致性三个维度上均优于先前工作。
- 发布一组模型，并在度量精度、锐利性、时序一致性和运行时间方面定义新的 Pareto 前沿。
- 公开发布代码与权重。

### 局限性
摘要未提供足够信息说明局限性；未提供具体实验设置、数据集、评价指标数值、失败案例或计算资源需求等细节。仅从摘要可知其贡献声明依赖作者报告，外部复现与边界条件需参考论文正文，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对单目视频/图像度量深度中“锐利性与时序一致性”的核心权衡，且涉及全分辨率、统一图像视频网络、Pareto 前沿模型族与代码权重发布；对 3D 重建、视频深度和实际部署相关方向具有较高参考价值。但具体方法细节与实验可信度需阅读正文进一步确认。

</details>

<details>
<summary>Abstract</summary>

We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness. To overcome this trade-off, we train a single, scalable network that processes both images and video and predicts depth maps at native resolution. Depth Pro 2 produces depth maps that are metrically accurate, sharp, and temporally consistent all at once, outperforming prior work in all of these dimensions. We release a family of models that define a new Pareto frontier in terms of metric accuracy, sharpness, temporal consistency, and runtime. We release code and weights at https://apple-aiml-research.github.io/ml-depth-pro-2/

</details>

#### 2026-11-19 - FirstCross: Convex Single-Photon 3D Reconstruction from Sparse Views

**Authors:** Chi-Wei Lee, Cheng-Han Chiang, Yi-Chun Chang, An-Kai Chen, Po-Chih Kuo
**Links:** [abs](https://arxiv.org/abs/2611.26321) - [pdf](https://arxiv.org/pdf/2611.26321)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, NeRF, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FirstCross: Convex Single-Photon 3D Reconstruction from Sparse Views
- 作者：Chi-Wei Lee, Cheng-Han Chiang, Yi-Chun Chang, An-Kai Chen, Po-Chih Kuo
- 出版日期：2026-11-19T16:05:47Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2611.26321) / [PDF](https://arxiv.org/pdf/2611.26321)

### 一句话总结
论文提出 FirstCross，一种无需神经网络、在体素网格上求解短序列凸问题的稀疏视角单光子 3D 重建方法，声称在深度误差、光子通量和重建速度上优于 Transientangelo 等神经方法。

### 研究问题
稀疏视角、极少光子条件下的单光子激光雷达 3D 重建。摘要指出，Transientangelo 等领先神经方法需要超过一小时的非凸逐场景优化，并且随光子通量下降精度会退化。论文试图解决这一非凸优化耗时与低光子通量下精度退化的问题。

### 核心思路/方法
FirstCross 是 network-free 方法，在体素网格上求解短序列凸问题。其核心观察是：对实心物体，给定信号率和背景率时，一条射线的 Poisson 似然仅通过“首次穿越点”（射线首次进入物体的位置）依赖场景。论文将该似然分解为两个可处理项：

1. 第一项惩罚位于已探测光子之前的表面，并具有紧凸闭包，即用运行最大值透射率替代 NeRF 乘积透射率的体渲染。
2. 第二项处理无法由任何表面解释的光子；在假设每个已探测表面点之后物体足够厚时，该项具有凸上界。

### 主要贡献
- 提出 FirstCross，一种无需神经网络的凸优化式单光子 3D 重建框架，避免 Transientangelo 式超过一小时的非凸逐场景优化。
- 基于“首次穿越”分解 Poisson 似然，构造两个可处理的凸项，其中第一项对应运行最大值透射率的体渲染，第二项在厚物体假设下具有凸上界。
- 摘要给出的对比结果包括：在 Transientangelo 自身真实数据协议下，FirstCross 在所有测试场景、视角数量和通量水平上深度误差更低；在 3 视角且光子数比协议最低通量还少 100 倍时，其平均物体深度误差仍低于使用全部光子的 Transientangelo 的一半；给定其探测表面点时，最佳经典融合在跨通量水平上的误差为三视角 FirstCross 的 1.3 至 1.8 倍；在真实房间尺度采集且仅用 1% 光子时，TransientNeRF 误差为 FirstCross 的 2.8 至 7.7 倍。
- 摘要声称可将少视角单光子扫描仪曝光降至 1%，并在单 GPU 上约一分钟重建物体。

### 局限性
- 方法假设对象为实心物体，并依赖“首次穿越”与每个已探测表面点之后物体足够厚的假设；摘要未提供这些假设在非实心、薄结构或复杂遮挡场景下的适用性信息。
- 摘要未提供网络-free 凸求解器的具体实现细节、运行时间随体素分辨率的变化、内存需求或超参数敏感性。
- 摘要未提供定量结果的完整实验设置、数据集规模、统计显著性、失败案例或与更多基线方法的比较。
- 摘要提及“best classical fusion”和 TransientNeRF 的对比，但未说明融合方法细节与 TransientNeRF 的具体配置。
- 摘要未提供代码、数据或复现实验的可用性信息。
- 摘要未提供足够信息说明该方法在非房间尺度、大场景或极端低光子条件下的泛化能力。

### 阅读优先级
中。理由：论文针对稀疏视角单光子重建中非凸优化耗时和低通量精度退化的问题，提出具有明确数学动机的凸分解方法，并以运行最大值透射率替代 NeRF 乘积透射率，问题定位和方法思路较清晰；摘要报告的对比结果覆盖多个场景、视角数和通量水平，并给出速度与曝光降低的声称。但摘要未提供实现细节、假设适用范围和完整实验设置，且部分强结论需依赖正文验证。若关注单光子 3D 重建、稀疏视角重建或凸优化替代神经优化的方向，建议优先阅读正文；若仅需了解领域概况，可保持中等优先级。

</details>

<details>
<summary>Abstract</summary>

Single-photon lidar records the arrival time of each returning photon, enabling 3D reconstruction from few views and scarce photons. However, leading neural methods such as Transientangelo require over an hour of non-convex per-scene optimization, and their accuracy degrades as photon flux decreases. We propose FirstCross, a network-free approach that instead solves a short sequence of convex problems on a voxel grid. For a solid object, the Poisson likelihood of a ray with given signal and background rates depends on the scene solely through its first crossing, the point where the ray first enters the object. Decomposing this likelihood yields two tractable terms. The first penalizes surfaces in front of detected photons and admits a tight convex closure, namely volume rendering with a running-maximum transmittance in place of NeRF's product transmittance. The second accounts for photons that no surface explains and admits a convex upper bound once the object is assumed to be thick behind each detected surface point. Compared with Transientangelo under its own real-data protocol, FirstCross achieves lower depth error across every test scene, view count, and flux level. With three views and 100 times fewer photons than at the protocol's lowest flux, our mean object depth error stays under half of Transientangelo's with all photons. Given our detected surface points, the best classical fusion has 1.3 to 1.8 times our three-view error across flux levels. On real room-scale captures with 1% of their photons, TransientNeRF has 2.8 to 7.7 times our error. FirstCross lets few-view single-photon scanners cut exposure to 1% and reconstruct an object in about a minute on one GPU.

</details>

#### 2026-11-19 - DfD-GS: Defocus Image Prior for Metric-Scale Single-View Depth Estimation and View Synthesis

**Authors:** Shiori Ueda, Rinto Yagawa, Hideo Saito, Shohei Mori
**Links:** [abs](https://arxiv.org/abs/2611.26072) - [pdf](https://arxiv.org/pdf/2611.26072)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** metric depth, depth estimation, monocular depth, novel view synthesis, view synthesis, scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DfD-GS: Defocus Image Prior for Metric-Scale Single-View Depth Estimation and View Synthesis
- 作者：Shiori Ueda, Rinto Yagawa, Hideo Saito, Shohei Mori
- 出版日期：2026-11-19T13:14:56Z
- 分类：主分类：3D Reconstruction & Multi-view Geometry；次分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.26072 ；PDF https://arxiv.org/pdf/2611.26072

### 一句话总结
DfD-GS 利用全聚焦—散焦图像对中的散焦模糊作为物理度量深度线索，预测度量尺度的单视图 3D Gaussian 场景表示，并用于遮挡感知的新视角合成。

### 研究问题
从单视角观测中恢复度量尺度几何本质上是不适定的，这限制了新视角合成的可靠性。现有方法依赖学习的单目深度先验，这类先验能提供较强的结构估计，但可能存在尺度歧义和对数据集的依赖偏差。论文关注的问题是：能否利用散焦这一物理度量线索，把单目深度先验对齐并细化到度量尺度，从而提升单视图度量深度估计和新视角合成的稳定性。

### 核心思路/方法
论文提出前馈框架 DfD-GS，输入为单视图的全聚焦—散焦图像对，输出度量尺度的 3D Gaussian 场景表示。核心思路是把散焦模糊作为物理度量深度线索。方法首先从全聚焦—散焦图像对及对应的散焦强度中估计基于散焦的度量视差图；然后用该估计对单目深度先验进行对齐和细化，使其达到度量尺度；随后预测可见与隐藏的 3D Gaussians，用于遮挡感知的新视角合成。

### 主要贡献
- 提出 DfD-GS，一个从单视图全聚焦—散焦图像对预测度量尺度 3D Gaussian 场景表示的前馈框架。
- 将散焦模糊作为物理度量深度线索，用于对齐和细化单目深度先验到度量尺度。
- 预测可见与隐藏 3D Gaussians，以支持遮挡感知的新视角合成。
- 在由 Booster 和 Middlebury 构造的合成散焦数据集上，摘要称 DfD-GS 在度量深度估计和新视角合成上优于单图像基线。
- 在 WildRGB-D 上，摘要称 DfD-GS 取得更低的 AbsRel 和 LPIPS，但深度 RMSE 高于单图像基线。
- 摘要称额外分析显示 DfD-GS 在视场变化下保持更稳定的度量尺度；真实数据集定性结果 shows 在光学散焦下恢复主要场景结构。

### 局限性
- 摘要未提供足够信息说明方法对散焦强度估计误差、图像对配准误差或全聚焦图像质量的敏感性。
- 摘要未提供足够信息说明在真实场景中对复杂遮挡、非朗伯表面、深度不连续或运动模糊的处理能力。
- 摘要未提供足够信息说明计算开销、推理速度、训练数据规模及泛化到不同相机/视场条件的定量范围。
- 摘要提到 WildRGB-D 上深度 RMSE 高于单图像基线，但未提供足够信息解释原因及适用边界。
- 摘要未提供足够信息说明合成散焦数据与真实散焦数据之间域差异的影响。

### 阅读优先级
中。理由：论文问题明确，即单视图度量尺度深度与新视角合成，方法思路利用散焦物理线索对齐单目先验，具有一定新颖性和交叉价值；摘要给出了合成与真实数据的部分结果，但同时存在 RMSE 指标劣于基线的混合结论。是否高优先级取决于读者对散焦线索、3D Gaussian 单视图重建及度量尺度估计的具体兴趣；仅据摘要信息，定为中较为稳妥。

</details>

<details>
<summary>Abstract</summary>

Recovering metric-scale geometry from observations at a single viewpoint remains fundamentally ill-posed, limiting the reliability of novel view synthesis. Recent methods rely on learned monocular depth priors, which provide strong structural estimates but can suffer from scale ambiguity and dataset-dependent biases. We propose DfD-GS, a feed-forward framework that predicts a metric-scale 3D Gaussian scene representation from a single-view all-in-focus--defocused image pair. The key idea is to exploit defocus blur as a physical metric depth cue. DfD-GS first estimates a defocus-based metric disparity map from the all-in-focus--defocused image pair and the corresponding defocus strength. This estimate is used to align and refine a monocular depth prior to metric scale. Visible and hidden 3D Gaussians are then predicted for occlusion-aware novel view synthesis. Experiments on synthetic-defocus datasets constructed from Booster and Middlebury show that DfD-GS outperforms single-image baselines in metric depth estimation and novel view synthesis. On WildRGB-D, DfD-GS achieves lower AbsRel and LPIPS but higher depth RMSE than the single-image baselines. Additional analyses show that DfD-GS maintains a more stable metric scale under field-of-view changes. Qualitative results on a real dataset show recovery of the main scene structure under optical defocus.

</details>

#### 2026-11-19 - Domain-Aware Conformal Prediction for Trustworthy Spacecraft Pose Estimation under Sim-to-Real Shift

**Authors:** Nidhal Eddine Chenni, Arunkumar Rathinam, Djamila Aouada
**Links:** [abs](https://arxiv.org/abs/2611.26065) - [pdf](https://arxiv.org/pdf/2611.26065)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Domain-Aware Conformal Prediction for Trustworthy Spacecraft Pose Estimation under Sim-to-Real Shift
- 作者：Nidhal Eddine Chenni, Arunkumar Rathinam, Djamila Aouada
- 出版日期：2026-11-19T13:08:51Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次级分类
- 链接：[摘要](https://arxiv.org/abs/2611.26065)｜[PDF](https://arxiv.org/pdf/2611.26065)

### 一句话总结
针对航天器位姿估计中“合成图像校准、真实图像测试”的分布偏移问题，作者提出在翻译为真实外观的合成图像上进行保形预测校准，以恢复覆盖率保证并显著减少“静默失败”。

### 研究问题
自主交会与近距操作不仅需要准确的航天器目标位姿估计，还需要可靠地判断该估计何时可信。保形预测可通过给出以指定概率包含真实位姿的位姿不确定性集合来提供形式化保证，但该保证假设校准数据与测试数据同分布。在轨道感知场景中，这一假设不成立：带标签的校准图像仅来自合成渲染，而实际操作图像是真实的。论文要解决的问题是：在合成到真实的分布偏移下，保形位姿估计的覆盖率保证会失效，且部分失效是“静默”的，即预测位姿集合看似有效却排除了真实位姿。

### 核心思路/方法
论文在 SPEED+ 数据集上展示：仅用合成图像校准的保形位姿估计在真实图像上会失去覆盖率保证，且许多失败是静默失败。为解决该问题，作者改为在“被翻译为真实图像外观”的合成图像上进行校准。其依据是：外观翻译改变图像外观但保留几何结构，因此合成位姿标签仍然有效，且不需要任何带标签的真实图像。摘要提到使用两种翻译模型进行实验。

### 主要贡献
- 在 SPEED+ 数据集上揭示：合成图像校准的保形位姿估计在真实图像上会失去覆盖率保证，且失败中许多为静默失败，即预测集合看似有效却排除真实位姿。
- 提出在翻译为真实外观的合成图像上进行校准，利用“外观改变、几何保留”使合成位姿标签继续有效，从而无需带标签真实图像。
- 实验表明：使用两种翻译模型时，该校准方式在误覆盖水平 0.1 及以上恢复了高于指定水平的覆盖率，并将静默失败从最多 43.5% 的测试图像降低到最多 3.3%，使保形位姿估计更接近空间中的可信部署。

### 局限性
- 摘要仅报告了 SPEED+ 数据集上的结果，未说明在其他数据集或更广泛场景中的泛化性；摘要未提供足够信息。
- 摘要未给出两种翻译模型的具体名称、结构或训练细节；摘要未提供足够信息。
- 摘要未说明误覆盖水平低于 0.1 时的覆盖率表现；摘要未提供足够信息。
- 摘要未提供计算开销、实时性或在轨部署约束的评估；摘要未提供足够信息。
- 摘要未提供静默失败的具体判定方式及剩余 3.3% 失败的成因分析；摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦航天器位姿估计在合成到真实偏移下的可信不确定性量化，问题定义清晰，且摘要给出了覆盖率恢复与静默失败显著下降的量化结果；若关注保形预测、域偏移下的可信感知或空间自主操作，具有直接参考价值。但摘要未提供方法细节、翻译模型信息及跨数据集验证，需阅读全文才能判断其通用性与部署可行性。

</details>

<details>
<summary>Abstract</summary>

Autonomous rendezvous and proximity operations require not only an accurate estimate of the pose of the target spacecraft, but also a reliable indication of when this estimate can be trusted. Conformal prediction provides such an indication with a formal guarantee, by producing pose uncertainty sets that contain the true pose with a specified probability. Such a guarantee, however, assumes that calibration and test data follow the same distribution, an assumption that is violated in orbital perception, where labelled calibration images are available only from synthetic renderings while operational images are real. In this work, we show on the SPEED+ dataset that conformal pose estimation calibrated on synthetic images loses its coverage guarantee on real images, and that many of the resulting failures are silent: the predicted pose set appears valid but excludes the true pose. To address this, we calibrate on synthetic images translated to the appearance of real images. Since translation alters appearance while preserving geometry, the synthetic pose labels remain valid and no labelled real images are required. Experiments with two translation models show that this calibration restores coverage above the specified level for miscoverage levels of 0.1 and above, and reduces silent failures from up to 43.5% to at most 3.3% of the test images, bringing conformal pose estimation a step closer to trustworthy deployment in space.

</details>

#### 2026-11-19 - AGE-Capture: Autonomous, General, and Efficient UAV Capture for High-Fidelity Scene Reconstruction

**Authors:** Xiaofeng Jin, Ningbo Bu, Matteo Frosi, Yiran Guo, Weilun Ren, Matteo Matteucci
**Links:** [abs](https://arxiv.org/abs/2611.26048) - [pdf](https://arxiv.org/pdf/2611.26048)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AGE-Capture: Autonomous, General, and Efficient UAV Capture for High-Fidelity Scene Reconstruction
- 作者：Xiaofeng Jin, Ningbo Bu, Matteo Frosi, Yiran Guo, Weilun Ren, Matteo Matteucci
- 出版日期：2026-11-19T12:55:48Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.26048 ；PDF https://arxiv.org/pdf/2611.26048

### 一句话总结
提出面向真实无人机的自主、传感器自适应且高效主动采集框架 AGE-Capture，以轻量在线状态和重建前沿视角驱动候选视角评估、任务进度判断与自主终止，从而在有限飞行资源下提升高保真场景重建效率。

### 研究问题
论文关注无人机高保真场景重建中的主动采集问题：系统不仅需要识别有价值的视角，还必须在不同传感配置和有限飞行资源下自主获取信息量丰富的观测，并判断任务是否完成。摘要明确指出，该问题超出单纯“识别有价值视角”的范围。

### 核心思路/方法
AGE-Capture 是一个面向真实无人机的自主、传感器自适应、高效主动采集框架。其核心包括：
- 基于可渲染性构建轻量在线状态，用于评估候选视角的效用、评估任务进度并指导飞行执行；
- 将几何探索与重建观测解耦，并建立统一的相机射线接口，使不同距离传感器与 RGB 相机模型共享同一套重建驱动的采集流程；
- 使用“重建前沿视角”表征残余采集价值，用于区域筛选和自主终止；
- 采用动态感知的分层规划，并结合异步事件驱动采集，以减少不必要的跨区域运动、等待规划的时间和重复观测。

### 主要贡献
- 提出 AGE-Capture 自主主动采集框架，面向真实无人机的高保真场景重建。
- 通过轻量在线状态统一支持候选视角效用评估、任务进度评估与飞行执行指导。
- 通过解耦几何探索与重建观测、建立统一相机射线接口，实现不同传感器配置共享重建驱动采集流程。
- 引入重建前沿视角用于区域筛选和自主终止，并结合动态感知分层规划与异步事件驱动采集提升效率。
- 摘要报告：在十个室内外仿真场景中，平均 PSNR 比在线基线高 3.30–3.53 dB，平均仅使用共同任务时间预算的 58.2%；平均峰值 GPU 显存占用比相同基线低 91.0%–93.3%；不同传感器配置实验验证共享采集流程的适应性，九个真实场景飞行进一步展示实际计算与运动约束下的机载闭环运行。

### 局限性
摘要未提供足够信息说明方法的具体失效条件、真实场景定量重建精度、传感器配置种类与数量、计算平台细节、飞行安全边界及与更多离线方法的比较。摘要仅报告了仿真中的 PSNR 与资源指标以及真实场景的机载闭环运行展示，未提供真实场景的完整定量结果和局限性讨论。

### 阅读优先级
中。理由：该论文聚焦无人机主动采集与三维重建的交叉问题，强调传感器自适应、自主终止和机载效率，摘要给出的仿真增益与资源降低幅度较明确，且包含真实场景飞行验证；但摘要未提供真实场景定量精度、失败案例和详细实验设置，若研究兴趣集中在主动重建、无人机自主采集或在线三维重建，值得进一步阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

High-fidelity scene reconstruction with an unmanned aerial vehicle (UAV) requires more than identifying valuable viewpoints: the system must autonomously acquire informative observations and determine task completion under different sensing configurations and limited flight resources. We present AGE-Capture, an autonomous, sensor-adaptive, and efficient active-capture framework for real UAVs. Building on renderability, the framework uses a lightweight online state to evaluate the utility of candidate views, assess task progress, and guide flight execution. By decoupling geometric exploration from reconstruction observations and establishing a unified camera-ray interface, the framework allows different range sensors and RGB camera models to share a reconstruction-driven acquisition pipeline. Reconstruction-frontier viewpoints characterize residual acquisition value for region screening and autonomous termination; dynamics-aware hierarchical planning combined with asynchronous event-driven capture reduces unnecessary inter-region motion, time spent waiting for plans, and repeated observations. Across ten indoor and outdoor simulation scenes, AGE-Capture achieves a mean peak signal-to-noise ratio (PSNR) $3.30$--$3.53\,\mathrm{dB}$ higher than that of the online baselines while using $58.2\%$ of the common mission-time budget on average. Its mean peak GPU memory usage is $91.0\%$--$93.3\%$ lower than that of the same baselines. Experiments with different sensor configurations validate the adaptability of the shared acquisition pipeline, while flights in nine real-world scenes further demonstrate onboard closed-loop operation under practical computational and motion constraints.

</details>

#### 2026-11-19 - SCCV-6D: Sparse Canonical Coordinate Voting for Holistic Multi-View RGB-D 6D Pose Estimation in Robotic Bin Picking

**Authors:** Nico Leuze, Samed Dogan, Maximilian Hoh, Henry Schaub, Alfred Schöttl
**Links:** [abs](https://arxiv.org/abs/2611.25819) - [pdf](https://arxiv.org/pdf/2611.25819)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SCCV-6D: Sparse Canonical Coordinate Voting for Holistic Multi-View RGB-D 6D Pose Estimation in Robotic Bin Picking
- 作者：Nico Leuze, Samed Dogan, Maximilian Hoh, Henry Schaub, Alfred Schöttl
- 出版日期：2026-11-19T09:38:24Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.25819) / [PDF](https://arxiv.org/pdf/2611.25819)

### 一句话总结
论文提出一种全稀疏的多视角 RGB-D 6D 位姿估计器 SCCV-6D，面向机器人料箱抓取场景，以稀疏方式在一次前向过程中同时完成多目标检测与位姿恢复，并在摘要报告的 IPD、MV-YCB 与 ROBI 上给出精度与速度结果。

### 研究问题
工业料箱抓取要求位姿估计在杂乱、部分遮挡以及零件反光、无纹理的条件下保持准确。论文指出多数近期 6D 位姿方法采用多阶段流程，精度高但内存与运行时间难以满足实际工业部署约束；而整体式流程通过不加区分的下采样或降低分辨率控制成本。论文关注的问题是：如何在保持整体式单次估计的低成本特性的同时，实现高分辨率、多目标、多视角 RGB-D 的 6D 位姿估计，并避免耗时的后处理阶段。

### 核心思路/方法
- **整体稀疏多视角 RGB-D 估计**：SCCV-6D 被描述为完全稀疏的多视角 RGB-D 估计器，以毫米级精度重建 3D 空间。
- **分阶段热图背景剪枝**：通过分阶段热图机制剪除背景。
- **高分辨率多目标预测**：在最高分辨率下同时预测任意数量目标的类别、平移偏移与旋转。
- **旋转的规范坐标投票**：将旋转表述为规范坐标投票；点以关联置信度为其规范物体坐标投票，从而支持闭式位姿恢复，并采用对称性感知的加权 Procrustes 求解。
- **减少后处理**：结合由偏移投票诱导的簇内点恢复，移除耗时的后处理阶段。
- **注意力门控蒸馏**：复用热图表述中的任务监督注意力先验，形成新的注意力门控蒸馏目标，对教师—学生特征对齐进行重加权。
- **摘要报告的结果**：在 IPD 测试划分上报告 0.826 AP、每场景 1.13 s，并称显著快于领先条目；在 MV-YCB 上达到 96.1 ADD-S，在 ROBI 的密集料箱上仍具竞争力。

### 主要贡献
- 提出面向机器人料箱抓取的整体式、完全稀疏的多视角 RGB-D 6D 位姿估计方法 SCCV-6D。
- 将旋转建模为带置信度的规范坐标投票，并配合对称性感知加权 Procrustes 求解实现闭式位姿恢复。
- 通过偏移投票诱导簇内点恢复，减少传统流程中的后处理阶段。
- 提出注意力门控蒸馏目标，利用热图表述中的任务监督注意力先验重加权师生特征对齐。
- 在摘要给出的基准上报告了精度与速度结果，包括 IPD 上 0.826 AP / 1.13 s 每场景、MV-YCB 上 96.1 ADD-S，以及在 ROBI 密集料箱上的竞争力。

### 局限性
- 摘要未提供足够信息说明方法在极端遮挡、强反光或不同传感器条件下的失效边界。
- 摘要未提供足够信息说明 IPD、MV-YCB、ROBI 之外的泛化实验或跨数据集验证。
- 摘要未提供足够信息给出内存占用、能耗或嵌入式部署实测数据；仅提到运行时间与“稀疏”设计。
- 摘要未提供足够信息说明注意力门控蒸馏所依赖的教师模型来源、训练成本与超参数敏感性。
- 摘要未提供足够信息说明与多阶段基线在同等硬件与实现条件下的完整公平比较细节。

### 阅读优先级
**高**。理由：论文直接针对工业料箱抓取中精度—效率—部署约束的冲突，提出整体稀疏多视角方案，并在摘要中给出明确的 AP、ADD-S 与每场景时间指标；对关注 6D 位姿估计、多视角 RGB-D、机器人抓取以及减少后处理流程的研究与工程读者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Industrial bin picking requires pose estimates that are accurate under clutter, partial occlusion, and the reflective, texture-less nature of manufactured parts. Most recent approaches to 6D pose estimation follow multi-stage pipelines. These achieve high accuracy, but incur memory and runtime footprints that do not cope with the operational constraints of many real-world industrial deployments. Holistic pipelines estimate poses in a single pass, with cost controlled through indiscriminate subsampling or lowered resolution. Continuing this line, we present SCCV-6D, a fully sparse multi-view RGB-D estimator. We reconstruct the 3D space at millimeter precision, prune background via a staged heatmap mechanism, and predict class, translation offset and rotation at highest resolution for an arbitrary number of objects simultaneously. Rotation is formulated as canonical coordinate voting. Points vote for their canonical object coordinates with an associated confidence, enabling closed-form pose recovery with a symmetry-aware weighted Procrustes solve. Along an in-cluster point recovery induced by offset votes, this removes time-consuming post-processing stages. We reuse the task-supervised attention priors from the heatmap formulation for a novel attention-gated distillation objective that reweights teacher-student feature alignment. On the IPD test split we report competitive 0.826 AP at 1.13 s per scene, significantly faster than the leading entries. On MV-YCB our approach reaches 96.1 ADD-S, and remains competitive even on the densely packed bins of ROBI.

</details>

#### 2026-11-19 - Mesh-Free Keypoint Learning for Category-Level 6D Object Pose Estimation

**Authors:** Junghoon Seo, Hakjin Lee, Jaehoon Sim
**Links:** [abs](https://arxiv.org/abs/2611.25513) - [pdf](https://arxiv.org/pdf/2611.25513)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mesh-Free Keypoint Learning for Category-Level 6D Object Pose Estimation
- 作者：Junghoon Seo, Hakjin Lee, Jaehoon Sim
- 出版日期：2026-11-19T05:03:40Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.25513 ；PDF https://arxiv.org/pdf/2611.25513

### 一句话总结
论文提出 MORSEPose，利用标准位姿与度量尺寸标注直接构造“位姿—尺寸包络”作为重建监督目标，用于无网格的类别级 6D 物体位姿估计，并在 REAL275 与 HouseCat6D 上验证其与基于表面的监督效果接近。

### 研究问题
类别级 6D 位姿估计需要将未见实例的部分 RGB-D 观测关联到类别共享的规范坐标系。现有做法常通过物体感知重建帮助自适应关键点保留可见表面几何，而重建目标通常依据观测点到已配准实例表面的距离来选择观测点。论文关注如何在不依赖该表面距离选择方式的情况下构造可跨相机帧与度量尺度一致的重建监督目标。

### 核心思路/方法
MORSEPose 的核心是从标准位姿和度量尺寸标注直接推导监督支撑区域：将观测 3D 点映射到归一化物体坐标，并保留落在带容差的“位姿—尺寸包络”内的点。该构造在不同相机帧和度量尺度下保持一致；当标注范围包住物体表面时，该包络会保守地包含传统表面距离选择器的支撑集。方法将该目标与多级 RGB-D 特征、自适应关键点和可学习的类别上下文相结合。

### 主要贡献
- 提出 MORSEPose，用标准位姿与度量尺寸标注直接构造重建监督目标，避免依赖基于配准实例表面距离的点选择。
- 给出该“位姿—尺寸包络”的构造，并说明其在跨相机帧和度量尺度上一致；在标注范围包住物体表面时，该包络保守包含常规表面距离选择器的支撑集。
- 将该目标与多级 RGB-D 特征、自适应关键点及可学习类别上下文集成。
- 在 REAL275 和 HouseCat6D 上报告：包络监督在点级和任务级均与基于表面的监督接近，在边界扰动和视角变化下保持稳定，并支持具有竞争力的类别级位姿精度。

### 局限性
摘要未提供足够信息说明计算开销、对标注尺寸误差的敏感程度、在更广泛数据集或类别上的泛化表现，以及失败情形与消融细节。

### 阅读优先级
中。理由：论文针对类别级 6D 位姿估计中的监督目标构造提出较清晰的替代方案，并在两个基准上给出与表面监督接近的结论；但摘要未提供充分的实验细节与局限性信息，适合作为相关方向的方法参考而非必须优先精读。

</details>

<details>
<summary>Abstract</summary>

Category-level 6D pose estimation relates partial RGB-D observations of unseen instances to a canonical frame shared across a category. Object-aware reconstruction helps adaptive keypoints retain the geometry of the visible surface. Common reconstruction targets select observed points by their distance to a registered instance surface. We present MORSEPose, which derives this support directly from standard pose and metric-size annotations. We map observed 3D points to normalized object coordinates and retain those inside a tolerancedilated pose-and-size envelope. This construction is consistent across camera frames and metric scales. When the annotated extent bounds the object surface, the envelope conservatively contains the support of a conventional surface-distance selector. We integrate this target with multi-level RGB-D features, adaptive keypoints, and learnable category context. Experiments on REAL275 and HouseCat6D show that the envelope closely matches surface-based supervision at both point and task levels, remains stable under boundary perturbations and viewpoint changes, and supports competitive category-level pose accuracy across benchmarks.

</details>

#### 2026-11-18 - Infer3D: Inverse Generative Modeling Enables Robust 3D Reconstruction

**Authors:** Amani Kiruga, Mark Hamilton, Joshua B. Tenenbaum, William T. Freeman, Vincent Sitzmann, Yilun Du, Ayush Tewari
**Links:** [abs](https://arxiv.org/abs/2611.25061) - [pdf](https://arxiv.org/pdf/2611.25061)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Infer3D: Inverse Generative Modeling Enables Robust 3D Reconstruction
- 作者：Amani Kiruga, Mark Hamilton, Joshua B. Tenenbaum, William T. Freeman, Vincent Sitzmann, Yilun Du, Ayush Tewari
- 出版日期：2026-11-18T19:07:33Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.25061 ；PDF https://arxiv.org/pdf/2611.25061

### 一句话总结
论文提出 Infer3D，一种逆向生成建模框架，通过恢复生成模型的潜变量并耦合冻结的 3D 提升网络，提升单目 3D 重建在分布外场景下的鲁棒性。

### 研究问题
现有主流 3D 重建神经网络通常采用摊销式、前馈推理，速度快但在训练中未见的分布外（OOD）场景条件下性能会退化。论文关注：如何借鉴人类视觉的生成式推断特性，提升单目 3D 重建对 OOD 视角和场景条件的泛化能力。

### 核心思路/方法
- 受认知科学中“自上而下生成式推断”启发，将 3D 重建表述为逆向生成建模：优化生成模型的潜变量，使其最好地匹配单目输入。
- 为防止退化的平坦输出，将生成式图像先验与一个冻结的 3D 提升网络耦合，把优化空间约束到有效且多视角一致的 3D 流形上。
- 引入自适应推理策略：对模糊的 OOD 样本分配更多测试时计算，同时高效路由分布内输入。

### 主要贡献
- 提出 Infer3D 逆向生成建模框架，用于单目 3D 重建。
- 通过冻结 3D 提升网络约束优化空间，避免退化平坦输出并保持多视角一致性。
- 在多种受控合成与真实任务中，摘要称其 OOD 重建精度优于在同等或更大数据集上训练的前馈网络。
- 提出自适应推理策略，按输入难度分配测试时计算。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集规模、评价指标数值、计算开销、失败案例或对生成模型与 3D 提升网络依赖程度的细节。

### 阅读优先级
高。理由：该工作直接针对 3D 重建中前馈模型 OOD 泛化差的痛点，方法路线结合生成式先验、测试时优化与自适应计算，且作者团队在该方向具有较高相关性；但需注意摘要未提供定量实验细节，阅读时应重点核查实验设置与比较公平性。

</details>

<details>
<summary>Abstract</summary>

Humans can understand the 3D structure of scenes even from highly unfamiliar or extreme viewpoints. Cognitive science suggests this generalization stems from a top-down generative inference strategy. In contrast, state-of-the-art 3D reconstruction neural networks typically rely on amortized, feedforward inference. While fast, this pattern-matching approach degrades when faced with out-of-distribution (OOD) scene conditions unseen during training. Inspired by the generative nature of human vision, we propose Infer3D, an inverse generative modeling framework that recovers the latent variables of a generative model to best match the monocular input. To prevent degenerate flat outputs, we couple the generative image prior with a frozen 3D lifting network that constrains the optimization space to a valid, multi-view-consistent 3D manifold. Across a variety of controlled synthetic and real-world tasks, Infer3D demonstrates superior OOD reconstruction accuracy compared to feedforward networks trained on equal or larger datasets. Furthermore, mirroring how human perception requires more time to process confusing stimuli, we introduce an adaptive inference strategy that expends more test-time compute on ambiguous OOD examples while efficiently routing in-distribution inputs. Project website: https://amanikiruga.github.io/infer3d-site/

</details>

#### 2026-11-18 - Beyond Appearance: Evidence-Guided Programmatic 3D Scene Reconstruction with Agentic Lighting Reasoning

**Authors:** Zeting Luo, Yifan Li, Shuai Yang
**Links:** [abs](https://arxiv.org/abs/2611.24565) - [pdf](https://arxiv.org/pdf/2611.24565)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, differentiable rendering, relighting, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Appearance: Evidence-Guided Programmatic 3D Scene Reconstruction with Agentic Lighting Reasoning
- 作者：Zeting Luo, Yifan Li, Shuai Yang
- 出版日期：2026-11-18T15:01:21Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Neural Scene Representations & Rendering
- 链接：摘要 https://arxiv.org/abs/2611.24565 ；PDF https://arxiv.org/pdf/2611.24565

### 一句话总结
论文提出 LightHarness，一个基于 VLM 的智能体框架，将显式光照推理引入迭代式图像到代码的 3D 场景重建，以超越仅依赖外观相似性的重建方式。

### 研究问题
现有图像到代码的 3D 场景重建方法主要依赖外观相似性，摘要指出这种相似性对区分几何、材质和光照中的错误提供的指导有限。光照通过与几何和材质的交互影响明暗、投射阴影和反射，因此仅凭外观难以可靠定位并修正这些错误。

### 核心思路/方法
- 提出 LightHarness，一个基于 VLM 的智能体框架，把显式光照推理纳入迭代场景重建。
- 利用几何、本征和光照三类互补线索，联合细化场景结构与外观。
- 提出 Lighting Reasoning Memory，用于维护光源假设，并在迭代中记录支持证据和修订历史。
- 借助上述机制推理部分可见与不可见光源，并以证据引导的验证来指导后续修订。
- 框架通过关于几何、材质和光照的连贯推理重建显式场景，摘要称无需额外训练或可微渲染。

### 主要贡献
- 将显式光照推理引入图像到代码的 3D 场景重建，针对仅依赖外观相似性的局限。
- 提出 Lighting Reasoning Memory，维护光源假设、证据与修订历史，支持对部分可见和不可见光源的推理。
- 通过几何、本征与光照线索的联合细化，并在无额外训练或可微渲染的条件下重建显式场景。
- 摘要称大量实验显示，在挑战性阴影和复杂光照下具有更优的图像到代码重建精度，并支持下游场景编辑、物体插入和多用途重光照。

### 局限性
- 摘要未提供足够信息说明方法的具体实现细节、网络结构、超参数与计算开销。
- 摘要未提供足够信息说明实验数据集、评价指标、对比基线及定量结果的具体数值。
- 摘要未提供足够信息说明失败情形、适用范围边界与消融实验结论。
- 摘要未提供足够信息说明“无需额外训练或可微渲染”的具体验证方式与代价。

### 阅读优先级
高。理由：该论文聚焦图像到代码 3D 场景重建中超越外观相似性的光照与材质、几何联合推理，问题定位明确；摘要声称在挑战性阴影与复杂光照下取得更优精度，并覆盖场景编辑、物体插入和重光照等下游任务，与 3D 重建及神经场景表示与渲染方向相关，值得优先阅读以核实方法细节与实验证据。

</details>

<details>
<summary>Abstract</summary>

Image-to-code methods for 3D scene reconstruction produce executable code that generates editable digital content and supports visual simulation. However, existing methods primarily rely on appearance similarity, which provides limited guidance for distinguishing errors in geometry, materials, and illumination. Light shapes scene appearance through its interactions with geometry and materials, influencing shading, cast shadows, and reflections. We therefore present LightHarness, a VLM-based agentic framework that incorporates explicit lighting reasoning into iterative scene reconstruction. To be specific, we leverage complementary geometric, intrinsic, and illumination cues to jointly refine scene structure and appearance, and propose Lighting Reasoning Memory to maintain light-source hypotheses, which supports evidence, and revision history throughout iterations. Together, they support reasoning about partially visible and unseen sources, with evidence-guided verification directing subsequent revisions. Our framework reconstructs explicit scenes through coherent reasoning about geometry, materials, and illumination without additional training or differentiable rendering. Extensive experiments demonstrate superior image-to-code reconstruction accuracy under challenging shadows and complex illumination, further supporting downstream scene editing, object insertion, and versatile relighting.

</details>

#### 2026-11-18 - Homeward: No Place Like the Training View

**Authors:** Mingyang Lyu, Yinqian Sun, Gongce Cao, Guobin Shen, Yuhao Zhang, Lu Jia, Chenfei Yan, Qian Zhang, Pin Lyu, Chen Gao, Bo Wang
**Links:** [abs](https://arxiv.org/abs/2611.24455) - [pdf](https://arxiv.org/pdf/2611.24455)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** depth prediction, pose estimation, camera calibration, view synthesis, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Homeward: No Place Like the Training View
- 作者：Mingyang Lyu, Yinqian Sun, Gongce Cao, Guobin Shen, Yuhao Zhang, Lu Jia, Chenfei Yan, Qian Zhang, Pin Lyu, Chen Gao, Bo Wang
- 出版日期：2026-11-18T14:01:38Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.24455 ；PDF https://arxiv.org/pdf/2611.24455

### 一句话总结
Homeward 是一种免训练、即插即用的观测适配器，把部署相机拍摄的未标定图像规范化回训练视角，使冻结的 VLA 策略在相机被碰动、重装或更换后仍能保持任务成功率。

### 研究问题
视觉-语言-动作（VLA）策略隐含假设第三人称相机固定在数据采集时的位姿。部署时相机一旦被碰动、重新安装或更换，即使任务和机器人本身没有变化，任务成功率也会急剧下降。论文要解决的是：在冻结 VLA 策略、不重新训练的前提下，如何把未标定部署相机的观测转换为训练视角。

### 核心思路/方法
论文从仿真中的一个闭环诊断悖论出发：用理想几何把受扰动视角重渲染回训练相机，能恢复大部分性能；但若用现成的前馈 3D 基础模型替代几何，策略表现反而可能比不校正更差。性能退化集中在细长、有关节的机械臂上，前馈深度预测会把机械臂撕裂和打散，而机械臂的精确 3D 状态其实可由机器人运动学直接已知。Homeward 利用这种不对称性：从实时 RGB 帧和单张训练视角参考图中估计未知量（相机参数和静态场景深度），而直接从运动学模型渲染已知量（运动中的机器人连杆）。方法无需场景微调，也无需部署相机标定。

### 主要贡献
- 提出 Homeward：免训练、即插即用的观测适配器，将未标定部署相机观测规范化回训练视角，适用于冻结 VLA 策略。
- 揭示并利用“未知与已知”的不对称性：未知的相机参数与静态场景深度由 RGB 帧和训练视角参考图估计，已知的机器人连杆由运动学模型直接渲染。
- 在约 30 万个闭环回合、4 个冻结 VLA 上评估；在 LIBERO-Plus 全部 1,599 个相机变体上，将 OpenVLA-OFT、π_{0.5}、π_0、OpenVLA 的成功率分别从 62.5%、76.5%、68.0%、3.6% 提升到 77.6%、95.1%、91.2%、26.4%。
- 无需场景微调或部署相机标定，可扩展到 6-DoF 随机放置、焦距变化；配合逐步位姿估计，还能处理回合内连续相机漂移；在 LIBERO-Plus 上，4 个策略中有 3 个达到或超过经过标定、场景训练过的视角合成基线。

### 局限性
摘要未提供足够信息说明方法在真实机器人部署中的表现、计算开销、对训练视角参考图质量的依赖程度、极端相机变化下的失效条件，以及除文中所述设置外的泛化边界。摘要未提供足够信息。

### 阅读优先级
中。理由：论文针对 VLA 部署中相机位姿扰动这一实际问题，提出免训练、即插即用的适配器，并在大规模闭环评估和多个冻结策略上报告了显著提升，对机器人学习与 3D 视角规范化交叉方向有参考价值；但摘要未提供真实机器人验证、计算成本和失效分析等关键细节，是否高优先级取决于读者对 VLA 部署鲁棒性或训练视角规范化问题的具体关注程度。

</details>

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precipitously even though the underlying task and robot remain unchanged. We present Homeward, a training-free, plug-and-play observation adapter that canonicalizes observations from an uncalibrated deployment camera back into the training view for frozen VLA policies. Our design stems from a closed-loop diagnostic paradox in simulation: while re-rendering perturbed views into the training camera with oracle geometry recovers much of the lost performance, substituting an off-the-shelf feed-forward 3D foundation model can leave the policy worse off than applying no correction at all. This degradation concentrates on the thin, articulated robot arm, which feed-forward depth prediction tears and scatters - yet the arm's exact 3D state is already known from robot kinematics. Homeward exploits this asymmetry: it estimates what is unknown - camera parameters and static scene depth - from the live RGB frame and a single training-view reference, and renders what is known - the moving robot links - directly from the kinematic model. Evaluated across $\sim$300,000 closed-loop episodes spanning four frozen VLAs, Homeward boosts success across all 1,599 camera variants of LIBERO-Plus from 62.5%, 76.5%, 68.0%, and 3.6% to 77.6%, 95.1%, 91.2%, and 26.4% for OpenVLA-OFT, $π_{0.5}$, $π_0$, and OpenVLA, respectively. Without any scene fine-tuning or deployment camera calibration, Homeward extends to 6-DoF random placements, focal-length changes, and, with per-step pose estimation, continuous intra-episode camera drift, while matching or surpassing a calibrated, scene-trained view-synthesis baseline on three of four policies on LIBERO-Plus.

</details>

#### 2026-11-18 - RAPID: Reconstruction Accelerated by Polarization-Informed Depth for 2D Gaussian Splatting

**Authors:** Daisong Ouyang, Linlin Xia, Liangkun Yan, Song Gu, Shedong Zhao, Xin Dai, Yi Zheng
**Links:** [abs](https://arxiv.org/abs/2611.24404) - [pdf](https://arxiv.org/pdf/2611.24404)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** mesh reconstruction, surface reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RAPID: Reconstruction Accelerated by Polarization-Informed Depth for 2D Gaussian Splatting
- 作者：Daisong Ouyang, Linlin Xia, Liangkun Yan, Song Gu, Shedong Zhao, Xin Dai, Yi Zheng
- 出版日期：2026-11-18T13:35:43Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.24404 ；PDF https://arxiv.org/pdf/2611.24404

### 一句话总结
RAPID 提出一种以几何为先、利用多视角偏振线索恢复稠密表面先验的框架，用于加速 2D Gaussian Splatting 的多视角三维表面重建。

### 研究问题
论文关注从多视角图像进行高效且准确的三维表面重建这一 Gaussian splatting 中的基础挑战。摘要指出，现有许多方法依赖稀疏几何初始化与迭代致密化，导致较大的优化开销，并且难以在渲染质量与几何精度之间取得平衡，尤其在反射区域和弱纹理区域。

### 核心思路/方法
RAPID 是一个“geometry-first”框架，利用多视角偏振线索恢复稠密表面先验。具体而言，方法使用稀疏几何锚点将表面法线整合进深度图，随后跨视角融合这些深度图；再通过曲率自适应采样与有向 Gaussian 初始化支持高效优化。整体目标是加速从偏振多视角输入出发的 Gaussian 优化过程。

### 主要贡献
- 提出 RAPID，一个几何优先的框架，使用多视角偏振线索恢复稠密表面先验，以应对稀疏几何初始化与迭代致密化带来的优化开销和几何/渲染平衡问题。
- 设计将表面法线通过稀疏几何锚点整合进深度图并进行跨视角融合的流程。
- 引入曲率自适应采样与有向 Gaussian 初始化以支持高效优化。
- 在 PISR 数据集上的实验显示，相较 PhyGaP 约获得 \(5\times\) 加速：平均优化时间从约 21 分钟降至 4 分钟，同时保持有竞争力的新视角合成质量与网格重建精度。

### 局限性
摘要未提供足够信息。摘要未给出方法在非偏振输入、不同数据集规模、极端反射或弱纹理条件失败情形、内存开销、超参数敏感性等方面的具体分析；也未提供除 PISR 数据集和 PhyGaP 对比之外的完整实验细节。

### 阅读优先级
中。理由：该工作与 2D Gaussian Splatting、多视角几何重建和偏振先验驱动的优化加速直接相关，摘要报告了明确的约 \(5\times\) 优化加速和可比的渲染/网格精度，具备较强的工程与方向参考价值；但摘要信息有限，尚未展示更广泛数据集、消融和失败案例分析，是否高优先级取决于读者对偏振辅助高斯重建与优化效率的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Efficient and accurate 3D surface reconstruction from multi-view images remains a fundamental challenge in Gaussian splatting. Many existing methods rely on sparse geometric initialization and iterative densification, resulting in substantial optimization overhead and difficulties in balancing rendering quality and geometric accuracy, particularly in reflective and weakly textured regions. To address these limitations, we propose RAPID, a geometry-first framework that uses multiview polarization cues to recover dense surface priors. We integrate surface normals into depth maps using sparse geometric anchors. These depth maps are then fused across views. Curvature-adaptive sampling and oriented Gaussian initialization then support efficient optimization. Experiments on the PISR dataset demonstrate an approximately \(5\times\) speedup over PhyGaP, which is a state-of-the-art Gaussian-based reconstruction method. RAPID reduces the average optimization time from approximately 21 minutes (PhyGaP) to 4 minutes while maintaining competitive novel-view synthesis quality and mesh reconstruction accuracy. These results demonstrate the effectiveness of RAPID in accelerating Gaussian optimization from polarimetric multi-view inputs.

</details>

#### 2026-11-18 - Object Pose: The Link between Weak Perspective, Paraperspective, and Full Perspective

**Authors:** Radu Horaud, Fadi Dornaika, Bart Lamiroy, Stephane Christy
**Links:** [abs](https://arxiv.org/abs/2611.24095) - [pdf](https://arxiv.org/pdf/2611.24095)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Object Pose: The Link between Weak Perspective, Paraperspective, and Full Perspective
- 作者：Radu Horaud, Fadi Dornaika, Bart Lamiroy, Stephane Christy
- 出版日期：2026-11-18T09:19:56Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.24095) | [PDF](https://arxiv.org/pdf/2611.24095)

### 一句话总结
本文对 DeMenthon 与 Davis 提出的迭代位姿估计方法给出代数推导，指出其属于在零阶（弱透视）或一阶（仿射透视/paraperspective）近似透视相机模型的一类方法，并提出迭代 paraperspective 位姿计算方法。

### 研究问题
论文关注如何从 3-D 到 2-D 点对应关系确定 3-D 物体相对于相机的位姿，并重点分析 DeMenthon 与 Davis 方法在弱透视与透视相机模型之间的联系，以及不同透视近似阶数下迭代位姿计算方法的性质。

### 核心思路/方法
- 对 DeMenthon 与 Davis 的方法给出代数推导。
- 将该方法归入更大的一类方法：透视相机模型在零阶（弱透视）或一阶（paraperspective）进行近似。
- 详细描述一种迭代 paraperspective 位姿计算方法，分别针对非共面与共面物体点。
- 分析这些方法的收敛性。
- 引入一种简单方式处理旋转矩阵相关的正交约束。
- 分析对相机标定误差的敏感性，并定义在相机标定不精确情况下的最优实验设置。
- 将该方法与非线性优化方法的结果进行比较。

### 主要贡献
- 给出 DeMenthon 与 Davis 方法的代数推导。
- 揭示弱透视、paraperspective 与全透视位姿估计之间的联系。
- 提出并详细描述迭代 paraperspective 位姿计算方法，覆盖非共面与共面点情形。
- 分析收敛性，并得出迭代 paraperspective 方法比迭代弱透视方法具有更好的收敛性质的结论。
- 引入处理旋转矩阵正交约束的简单方式。
- 分析相机标定误差敏感性，并给出相对于不精确相机标定的最优实验设置。
- 与非线性优化方法进行比较。

### 局限性
摘要未提供足够信息说明计算复杂度、实时性、在真实噪声数据上的广泛实验规模、失败情形或具体精度指标；也未提供与非线性优化方法比较的详细实验设置和数值结果。

### 阅读优先级
中。理由：该论文聚焦位姿估计中透视近似模型之间的理论联系与迭代方法收敛性，对 3D 重建与多视图几何中相机位姿估计方法分析有参考价值；但摘要未给出具体应用场景、代码或大规模实验细节，是否优先阅读取决于读者对弱透视/paraperspective 位姿估计理论及相机标定误差分析的兴趣。

</details>

<details>
<summary>Abstract</summary>

Recently, DeMenthon and Davis [4,5] proposed a method for determining the pose of a 3-D object with respect to a camera from 3-D to 2-D point correspondences. The method consists of iteratively improving the pose computed with a weak perspective camera model to converge, at the limit, to a pose estimation computed with a perspective camera model. In this paper we give an algebraic derivation of DeMenthon and Davis' method and we show that it belongs to a larger class of methods where the perspective camera model is approximated either at zero order (weak perspective) or first order (paraperspective). We describe in detail an iterative paraperspective pose computation method for both non coplanar and coplanar object points. We analyse the convergence of these methods and we conclude that the iterative paraperspective method (proposed in this paper) has better convergence properties than the iterative weak perspective method. We introduce a simple way of taking into account the orthogonality constraint associated with the rotation matrix. We analyse the sensitivity to camera calibration errors and we define the optimal experimental setup with respect to imprecise camera calibration. We compare the results obtained with this method and with a non-linear optimization method.

</details>

#### 2026-11-17 - mmTherm: Absolute 3D Human Pose Estimation from Low-Resolution Thermal Images and mmWave Radar

**Authors:** Zhaoxin Chang, Badii Jouaber, Daqing Zhang
**Links:** [abs](https://arxiv.org/abs/2611.23477) - [pdf](https://arxiv.org/pdf/2611.23477)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：mmTherm: Absolute 3D Human Pose Estimation from Low-Resolution Thermal Images and mmWave Radar
- 作者：Zhaoxin Chang, Badii Jouaber, Daqing Zhang
- 出版日期：2026-11-17T20:30:24Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.23477 ；PDF https://arxiv.org/pdf/2611.23477

### 一句话总结
mmTherm 是一个融合低分辨率热成像与毫米波雷达的轻量框架，用热成像提供的身体结构与关节方向信息配合雷达测距信息，实现绝对 3D 人体姿态与全局定位。

### 研究问题
论文要解决的是绝对 3D 人体姿态估计问题，即同时恢复人体姿态和其在 3D 空间中的全局位置。摘要指出，毫米波雷达可提供距离和方向测量且具有隐私保护优势，但其点云稀疏，使 HPE 约束不足；低分辨率热成像可补充身体方向和结构观测。摘要还报告，一个较强的特征级融合基线在泛化到未见受试者时会丢失较多定位和 HPE 优势，其径向定位甚至不如仅用雷达的基线。

### 核心思路/方法
mmTherm 是一个轻量框架，显式利用热成像与毫米波雷达在几何属性上的互补性：将从热图像估计的身体结构和关节方向，与来自雷达的距离信息结合，用于定位人体并重建其 3D 姿态。摘要强调该设计由“特征级融合基线跨受试者泛化不足”的评估结果驱动。

### 主要贡献
- 指出强特征级融合基线在未见受试者上泛化时，定位与 HPE 优势明显下降，径向定位不如雷达单模态基线。
- 提出轻量框架 mmTherm，显式结合热成像的身体结构/关节方向与雷达距离信息，用于绝对 3D 人体姿态估计。
- 在 OctoNet 上报告：相对最强对应基线，跨用户绝对关节误差降低 33%，根定位误差降低 38%，同时参数显著更少、推理计算量更低。

### 局限性
- 摘要未提供足够信息说明具体网络结构、融合模块细节和训练策略。
- 摘要未提供足够信息说明数据集规模、受试者数量、热成像分辨率设置和雷达配置。
- 摘要未提供足够信息说明延迟、能耗、实时性及失败案例。
- 摘要未提供足够信息说明除 OctoNet 外的泛化验证和与其他模态方法的完整对比。

### 阅读优先级
中。理由：论文聚焦隐私保护条件下的绝对 3D 人体姿态估计，问题定义清晰，且摘要给出了明确的跨用户误差下降指标与轻量化优势；但当前仅有摘要信息，实验细节、方法细节和泛化范围有限，适合作为相关方向跟踪阅读，优先级不宜定为高。

</details>

<details>
<summary>Abstract</summary>

Absolute 3D human pose estimation (HPE) aims to recover both a person's body pose and their global position in 3D space. Privacy-preserving millimeter-wave (mmWave) radar provides distance and direction measurement capabilities, but its sparse point clouds make HPE under-constrained. Low-resolution thermal imaging can provide complementary observations of body direction and structure. However, our evaluation shows that a strong feature-level fusion baseline loses much of its localization and HPE advantage when generalizing to unseen subjects, with radial localization becoming less accurate than a radar-only baseline. Motivated by this finding, we introduce mmTherm, a lightweight framework that explicitly incorporates the complementary geometric properties of thermal imaging and mmWave radar. It combines body structure and joint directions estimated from thermal images with range information from radar to localize the body and reconstruct its 3D pose. Experiments on OctoNet show that mmTherm reduces cross-user absolute joint error by 33% and root localization error by 38% relative to the strongest corresponding baselines, while requiring substantially fewer parameters and less computation at inference.

</details>

#### 2026-11-17 - TRIDENT: Efficient Triple-Task Learning of Dehazing, Depth, and Uncertainty Estimation for Underwater 3-D Robot Visual Perception

**Authors:** Geonmo Yang, Younggun Cho
**Links:** [abs](https://arxiv.org/abs/2611.22224) - [pdf](https://arxiv.org/pdf/2611.22224)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRIDENT: Efficient Triple-Task Learning of Dehazing, Depth, and Uncertainty Estimation for Underwater 3-D Robot Visual Perception
- 作者：Geonmo Yang, Younggun Cho
- 出版日期：2026-11-17T05:08:06Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.22224 ；PDF https://arxiv.org/pdf/2611.22224 ；补充材料 https://sites.google.com/view/underwater-trident/home

### 一句话总结
论文提出 TRIDENT，一种面向水下 3-D 机器人视觉感知的快速轻量三任务联合学习模型，同时处理图像增强、深度估计与不确定性估计，并通过共享主干和三个并行解码器提升特征共享效率。

### 研究问题
水下视觉系统受光传播影响，常出现纹理模糊和颜色对比度低的问题，这会显著降低稳定机器人操作所需的感知能力。论文关注水下 3-D 视觉系统中的多维视觉任务，具体包括图像增强、深度估计和不确定性估计，并希望在同时完成三项任务的同时保持模型在内存占用和推理时间上的效率。

### 核心思路/方法
TRIDENT 采用一个主干结构与三个并行解码器，以实现高效的特征共享；模型被设计为快速且轻量的形式。摘要还指出，该模型被设计为可训练以表达复杂参数化。论文将图像增强、深度估计与不确定性估计作为联合学习任务，并报告该方法在特征匹配中表现出鲁棒性，且可从 2-D 视觉任务平滑扩展到 3-D 视觉任务。

### 主要贡献
- 提出面向水下 3-D 机器人视觉感知的 TRIDENT 模型，联合处理图像增强、深度估计和不确定性估计三项任务。
- 采用一个主干加三个并行解码器的结构，实现高效特征共享，并以快速、轻量为设计目标。
- 在多个标准数据集上的实验评估中，摘要声称 TRIDENT 在图像增强和深度估计上显著优于现有方法。
- 尽管执行三项任务，摘要声称该模型在内存大小和推理时间上均比其他方法更高效。
- 联合学习方法在特征匹配中展现出鲁棒性，并从 2-D 视觉任务扩展到 3-D 视觉任务。

### 局限性
- 摘要未提供足够信息说明具体使用了哪些标准数据集、数据规模及采集条件。
- 摘要未提供足够信息说明训练细节、损失函数设计、复杂参数化的具体形式及超参数设置。
- 摘要未提供足够信息给出内存大小、推理时间和精度指标的具体数值。
- 摘要未提供足够信息说明不确定性估计的定量评估方式与结果。
- 摘要未提供足够信息说明特征匹配鲁棒性的实验设置、对比方法与失败情形。
- 摘要未提供足够信息讨论模型在真实水下机器人平台上的部署验证与实时性边界。

### 阅读优先级
中。理由：该论文面向水下机器人 3-D 视觉感知，将去雾、深度与不确定性估计统一到一个轻量三任务模型中，问题设定和应用方向明确；摘要声称在图像增强、深度估计及效率上优于现有方法，并涉及 2-D 到 3-D 任务扩展与特征匹配鲁棒性。但摘要未给出具体数据集、指标数值和实验细节，是否值得深入阅读需结合全文实验与机器人部署验证进一步判断。

</details>

<details>
<summary>Abstract</summary>

Underwater visual systems often suffer from blurry textures and low color contrast due to the inevitable light propagation. These issues can significantly degrade the perception of stable robotic operations. In this paper, we introduce a novel learning-based sensing system that tackles the multidimensional vision tasks in underwater; concretely, we deal with image enhancement, depth estimation, and uncertainty for 3-D visual systems. Also, we propose a TRIDENT model in a fast and lightweight manner; TRIDENT consists of three parallelized decoders and one backbone structure for efficient feature sharing. In addition, it is designed to be trained to express complex parameterization. In experimental evaluation on several standard datasets, we demonstrate that TRIDENT significantly outperforms other existing methods on image enhancement and depth estimation. Despite performing three tasks, our model has better efficiency than the others for both memory size and inference time. Finally, our joint learning approach demonstrates robustness in feature matching and seamlessly extends from 2-D to 3-D vision tasks. Supplements are available at https://sites.google.com/view/underwater-trident/home

</details>

#### 2026-11-17 - Joint-ID: Transformer-based Joint Image Enhancement and Depth Estimation for Underwater Environments

**Authors:** Geonmo Yang, Gilhwan Kang, Juhui Lee, Younggun Cho
**Links:** [abs](https://arxiv.org/abs/2611.22212) - [pdf](https://arxiv.org/pdf/2611.22212)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, feature matching, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Joint-ID: Transformer-based Joint Image Enhancement and Depth Estimation for Underwater Environments
- 作者：Geonmo Yang, Gilhwan Kang, Juhui Lee, Younggun Cho
- 出版日期：2026-11-17T04:49:09Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次级分类
- 链接：摘要页 https://arxiv.org/abs/2611.22212 ；PDF https://arxiv.org/pdf/2611.22212 ；补充材料 https://sites.google.com/view/joint-id/home

### 一句话总结
提出基于 Transformer 的 Joint-ID 网络，从原始水下图像中联合学习图像增强与深度估计，以提升水下视觉感知质量并服务于水下机器人相关视觉任务。

### 研究问题
水下成像受散射、吸收和湍流等因素影响，导致图像质量下降、可见度受限；论文希望同时改善水下图像质量并获取深度信息，以支持水下环境中的视觉感知。

### 核心思路/方法
- 采用联合学习思路，将图像增强与深度估计放在同一框架中处理，输入为原始水下图像。
- 提出 Transformer 神经网络 Joint-ID，目标是获得高感知质量的图像与深度信息。
- 构建多模态目标函数，针对无效深度、清晰度不足以及由颜色和局部纹理导致的图像退化进行约束。
- 设计端到端训练流程，在共享的层次化特征空间中实现联合恢复与深度估计。
- 提出一个包含多种失真和场景深度的合成数据集，用于多任务学习。
- 在合成数据集、标准数据集以及具有不同光谱和严重浑浊的真实水下图像上评估 Joint-ID；并展示其在特征匹配和显著性检测方面的能力，面向视觉引导的水下机器人应用。

### 主要贡献
- 提出 Joint-ID，一种基于 Transformer 的水下图像增强与深度估计联合学习方法，可从原始水下图像获取高感知质量图像和深度信息。
- 提出面向无效深度、清晰度不足以及颜色与局部纹理退化的多模态目标函数。
- 设计共享层次化特征空间中的端到端联合恢复与深度估计训练流程。
- 提出包含多种失真与场景深度的合成数据集，用于多任务学习。
- 在合成、标准及真实水下图像上评估方法有效性，并展示其用于特征匹配和显著性检测的潜力。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、计算开销、实时性、泛化边界或定量局限；仅提到真实水下图像具有不同光谱和严重浑浊，但未说明方法在这些条件下的具体限制。

### 阅读优先级
中。理由：论文主题聚焦水下图像增强与深度估计的联合学习，并涉及 Transformer、多任务目标函数、合成数据集和水下机器人视觉应用；若关注水下视觉感知或多任务学习，具有相关性。但摘要未提供具体定量结果、对比方法细节和局限性信息，是否精读需结合对这些方向的具体兴趣再判断。

</details>

<details>
<summary>Abstract</summary>

Underwater imaging is a challenging task due to factors such as scattering, absorption, and turbulence, which degrade image quality and limit visibility. In this paper, we propose a novel approach for enhancing underwater images that leverages the benefits of joint learning for simultaneous image enhancement and depth estimation. We introduce Joint-ID, a transformer-based neural network that can obtain high-perceptual image quality and depth information from raw underwater images. Our approach formulates a multi-modal objective function that addresses invalid depth, lack of sharpness, and image degradation based on color and local texture. We design an end-to-end training pipeline that enables joint restoration and depth estimation in a shared hierarchical feature space. Additionally, we propose a synthetic dataset with various distortions and scene depths for multi-task learning. We evaluate Joint-ID on synthetic and standard datasets, as well as real underwater images with diverse spectra and harsh turbidity, demonstrating its effectiveness for underwater image enhancement and depth estimation. Furthermore, we demonstrate the ability of Joint-ID to perform feature matching and saliency detection for visually guided underwater robots. Our proposed method has the potential to improve the visual perception of underwater environments and benefit applications such as oceanography and underwater robotics. Supplements are available at: https://sites.google.com/view/joint-id/home

</details>

#### 2026-11-17 - HandRSI: Recursive Self-Improvement for Hand Pose Estimation

**Authors:** Zhekai Wang, Luqing Luo, Wenhao Yao, Junjie Lu, Huanan Zhu, Feifei Gao, Yuhua Jiang
**Links:** [abs](https://arxiv.org/abs/2611.22164) - [pdf](https://arxiv.org/pdf/2611.22164)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HandRSI: Recursive Self-Improvement for Hand Pose Estimation
- 作者：Zhekai Wang, Luqing Luo, Wenhao Yao, Junjie Lu, Huanan Zhu, Feifei Gao, Yuhua Jiang
- 出版日期：2026-11-17T03:55:44Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.22164) / [PDF](https://arxiv.org/pdf/2611.22164)

### 一句话总结
HandRSI 提出一种递归自我改进框架，将手部姿态估计器的“推理执行框架（harness）自动优化”与“基于该框架的选择性蒸馏”交替迭代，从而减少边界漏检、遮挡误置与抖动。

### 研究问题
摘要指出，第一人称 3D 手部姿态估计器仍存在三类失败：图像边界处漏检手部、遮挡手部定位错误以及抖动。这类失败通常依赖手写推理后处理与微调来修正，而这两个步骤相互依赖，却又被分开调优。论文关注如何把二者纳入统一、可递归改进的流程中。

### 核心思路/方法
- 系统由视频估计器与可执行的推理 harness 组成。
- 每一轮中，coding agents 改进 harness；只有在该改动于留出数据上提升全部十项基准指标的复合表现、且没有显著降低任一指标时，才被接受。
- 被接受的 harness 通过选择性蒸馏指导估计器：在无真值帧上监督手部存在性与时序一致性，在真值帧上监督姿态。
- 由于更新后的估计器可能改变哪些推理改进仍然有效，harness 会在新估计器上重新验证，形成递归自我改进闭环。
- 在精度—速度前沿上使用 hypervolume 选择，得到 Lite、Medium、Heavy 三种系统，运行速度为 20.7 至 41.1 FPS。

### 主要贡献
- 提出 HandRSI 递归自我改进框架，耦合推理 harness 优化与估计器选择性蒸馏。
- 以统一的十指标复合准则和“不得显著回退任一指标”的约束接受 harness 改动，并在更新后的估计器上重新验证。
- 从 ACE-Ego-Hand 模型出发，五轮迭代在 HOT3D 上降低 MPJPE-p 35%、在 ARCTIC 上降低 11%，并将抖动约减半。
- 在 HOT3D 上，HandRSI 的 MPJPE-p 比在同一真值上微调的 ACE-Ego-Hand 低 16%。
- 在统一协议下，于两个基准的全部十项指标上优于九种复跑的已发表方法。
- 公开代码、评估器、harnesses 与权重。

### 局限性
- 摘要未提供足够信息说明计算成本、迭代轮数上限、coding agents 的具体配置与失败案例。
- 摘要未提供足够信息说明各基准数据规模、训练/留出划分细节及统计显著性检验方式。
- 摘要未提供足够信息说明方法在其他手部数据集、不同传感器或非第一人称场景中的泛化表现。
- 摘要未提供足够信息说明 harness 改动空间、接受准则中“显著回退”的具体阈值，以及超参数敏感性。

### 阅读优先级
高。理由：该工作直接针对第一人称 3D 手部姿态估计中的边界、遮挡与抖动问题，给出可递归自我改进的系统级方案，并在两个基准的十项指标上报告了相对强基线与其他方法的比较，同时公开代码与权重；对关注手部姿态估计、推理时自适应与自动优化推理流程的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Egocentric 3D hand pose estimators still miss hands at the image border, misplace occluded hands and jitter. Such failures are usually fixed by hand-written inference refinements and by fine-tuning, two interdependent steps that are tuned separately. We present HandRSI, a recursive self-improvement framework for a hand pose system that consists of a video estimator and its executable inference harness. In each round, coding agents refine the harness, and a change is accepted only if it improves a composite of all ten benchmark metrics on held-out data without significantly regressing any of them. The accepted harness then guides the estimator through selective distillation, which supervises hand presence and temporal consistency on frames without ground truth, while ground truth supervises pose. Since the updated estimator may change which refinements remain useful, the harness is re-validated on it. Starting from the released ACE-Ego-Hand model, five rounds reduce MPJPE-p by 35% on HOT3D and 11% on ARCTIC and roughly halve jitter. On HOT3D, HandRSI's MPJPE-p is 16% lower than that of ACE-Ego-Hand fine-tuned on the same ground truth. Under a unified protocol, it outperforms nine re-run published methods on all ten metrics of both benchmarks. Hypervolume selection on the accuracy-speed front yields Lite, Medium and Heavy systems running at 20.7 to 41.1 FPS. This report gives the full method, every stage of every round and the complete protocol. Code, evaluator, harnesses and weights are public.

</details>

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-19 - CryoGaussian: Heterogeneous Cryo-EM Reconstruction Made Explicit with Gaussian Splatting

**Authors:** Ziwen Wang, Jiajun Fan, Chaoran Cheng, Ruihan Guo, Yanru Qu, Juexiao Zhou, Ge Liu
**Links:** [abs](https://arxiv.org/abs/2611.26128) - [pdf](https://arxiv.org/pdf/2611.26128)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CryoGaussian: Heterogeneous Cryo-EM Reconstruction Made Explicit with Gaussian Splatting
- 作者：Ziwen Wang, Jiajun Fan, Chaoran Cheng, Ruihan Guo, Yanru Qu, Juexiao Zhou, Ge Liu
- 出版日期：2026-11-19T13:51:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.26128) / [PDF](https://arxiv.org/pdf/2611.26128)

### 一句话总结
CryoGaussian 将显式高斯密度表示与可微光栅化结合，用于单颗粒冷冻电镜的异质性重构，在摘要报告的 CryoBench 与实验数据上展示了重构组成型和构象型异质性的能力。

### 研究问题
单颗粒冷冻电镜从带噪颗粒图像中解析大分子结构，但稀有、瞬态的组成状态以及细微、连续的构象变化难以被解析。论文针对异质性冷冻电镜重构问题提出方法。

### 核心思路/方法
- 使用高斯泼溅（Gaussian splatting）构建显式高斯密度表示，直接拟合颗粒图像。
- 通过可微光栅化器渲染正交线积分，并由对比度传递函数（CTF）调制。
- 高斯初始化为随机，数量由估计的分子密度空间支撑决定，最小尺寸受颗粒图像 Nyquist 频率约束。
- 学习颗粒图像潜变量与逐高斯潜变量，联合调制每个高斯的基础位置、振幅和尺度，以捕捉颗粒图像间的组成与构象变化。
- 在推断出的潜变量条件下拟合高斯，重构各结构状态。
- 针对加性冷冻电镜投影优化光栅化器，摘要称训练时间减少 12.8–28.0 倍。

### 主要贡献
- 提出 CryoGaussian，一种面向异质性冷冻电镜重构的高斯泼溅方法，使用显式高斯密度表示并通过可微光栅化直接拟合颗粒图像。
- 在 CryoBench 上，摘要称其在组成型异质性和构象型异质性两方面均取得 state-of-the-art 重构精度。
- 在实验数据上，摘要称解析了 50S 核糖体亚基的一种稀有组成状态（class C4，占颗粒 1.3%），其中 rRNA helix 68 对接且中央突起缺失；并解析了前催化剪接体 SF3b 与解旋酶亚复合体的连续构象运动。
- 针对加性冷冻电镜投影优化光栅化器，摘要报告训练时间减少 12.8–28.0 倍。

### 局限性
- 摘要未提供足够信息说明方法在不同信噪比、颗粒数量、初始化敏感性或失败情形下的表现。
- 摘要未提供足够信息说明与基线方法的完整定量对比细节、消融实验设置及统计显著性。
- 摘要未提供足够信息说明显式高斯表示对分辨率上限、内存/计算开销以及潜变量可解释性的限制。
- 摘要未提供足够信息说明实验数据中稀有状态解析的验证方式与潜在伪影风险。

### 阅读优先级
中。理由：论文主题涉及冷冻电镜异质性重构与高斯泼溅表示，摘要给出了明确的方法框架、基准表现和实验数据应用；但仅凭摘要无法判断定量细节、鲁棒性与局限性，适合作为相关方向的方法跟踪阅读，优先级不宜直接定为高。

</details>

<details>
<summary>Abstract</summary>

Single-particle cryo-electron microscopy (cryo-EM) determines macromolecular structures from noisy particle images. However, rare, transient compositional states and subtle, continuous conformational variation are difficult to resolve. We present CryoGaussian, a Gaussian splatting method for heterogeneous cryo-EM reconstruction that fits an explicit Gaussian density representation directly to the particle images through a differentiable rasterizer rendering orthographic line integrals modulated by the contrast transfer function. The Gaussians are initialized randomly, with their number derived from the estimated spatial support of the molecular density and their minimum size bounded by the Nyquist frequency of the particle images. To capture the compositional and conformational variation across particle images, we learn particle-image and per-Gaussian latents that jointly modulate the base position, amplitude, and scale of each Gaussian. Each structural state is then reconstructed by fitting the Gaussians conditioned on its inferred latent. On CryoBench, CryoGaussian achieves state-of-the-art reconstruction accuracy for both compositional and conformational heterogeneity. On experimental data, it resolves a rare compositional state of the 50S ribosomal subunit (class C4, 1.3% of particles) with rRNA helix 68 docked in the absence of the central protuberance, and continuous conformational motion of the SF3b and helicase subcomplexes of the pre-catalytic spliceosome. We further optimize the rasterizer for additive cryo-EM projection, reducing training time by 12.8-28.0$\times$.

</details>

#### 2026-11-19 - PaveSplat: Resolution-Robust Feed-Forward Gaussian Splatting with Residually Corrected Surface-Aligned Covariances

**Authors:** Janghun Kim, Hyun-Cheol Kim, Eunbin An, Myeonghun Oh, Hyon-Gon Choo
**Links:** [abs](https://arxiv.org/abs/2611.26045) - [pdf](https://arxiv.org/pdf/2611.26045)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PaveSplat: Resolution-Robust Feed-Forward Gaussian Splatting with Residually Corrected Surface-Aligned Covariances
- 作者：Janghun Kim, Hyun-Cheol Kim, Eunbin An, Myeonghun Oh, Hyon-Gon Choo
- 出版日期：2026-11-19T12:55:04Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.26045) / [PDF](https://arxiv.org/pdf/2611.26045)

### 一句话总结
PaveSplat 在解析的表面对齐协方差上引入一个初始化为恒等变换的学习残差（单位四元数），用于校正 surfel 朝向；由此让前馈高斯泼溅在更高显示分辨率下重渲染时保持表面覆盖。

### 研究问题
像素对齐的前馈高斯泼溅在单次前向中，从少量图像为每个像素预测一个图元；其渲染质量取决于这些图元覆盖表面的程度。近期基于 surfel 的方法根据预测深度解析计算表面对齐协方差，但当由深度导出的坐标系病态（ill-posed）时，该协方差无法校正 surfel 朝向，导致 surfel 对表面的覆盖较松散。在训练分辨率下，每个 surfel 的最小一像素足迹可以掩盖这些间隙；但同一预测在更高分辨率下重渲染时，这些间隙会表现为空洞。论文要解决的是：如何在没有重新运行网络的情况下，让前馈预测在更高显示分辨率下重渲染时仍保持稳健的表面覆盖。

### 核心思路/方法
- 保留解析协方差作为初始化，使其各轴与表面切向对齐。
- 在此基础上加入一个以恒等变换初始化的单位四元数残差，用于重新定向 surfel；该残差只在能够改善渲染时才起作用，从而把被解析坐标系错误瞄准的 surfel 重新转回表面。
- 方法属于前馈单次预测路线（pixel-aligned feed-forward Gaussian splatting），不依赖逐场景优化；摘要未提供训练损失、网络结构、数据规模等更多实现细节。

### 主要贡献
- 提出 PaveSplat，一种在解析表面对齐协方差上叠加学习残差的前馈高斯泼溅方法，目标是在不同渲染分辨率下保持 surfel 对可见表面的铺覆。
- 在 RealEstate10K 上，于 1x–8x 各尺度中，在“每像素单高斯”方法组内取得最佳 PSNR、SSIM 和 LPIPS；摘要指出原生分辨率下增益较小，收益主要体现在同一预测被重渲染到更高显示分辨率且不重新运行网络时。
- 在零样本 DL3DV 上，于该组内各尺度均领先 PSNR，并在 SSIM/LPIPS 上排名第一或第二。
- 覆盖空洞分析显示，在高分辨率重渲染下，未覆盖像素少于两个基线方法。

### 局限性
- 摘要仅报告 RealEstate10K 与零样本 DL3DV 的结果，未说明其他数据集、场景类型或极端条件下的表现；摘要未提供足够信息。
- 摘要未提供网络结构、训练配置、推理开销、参数量或运行时间等细节；摘要未提供足够信息。
- 摘要未给出与完整基线集合的全面比较，也未讨论失败案例；摘要未提供足够信息。
- 摘要提到原生分辨率增益较小，说明方法的主要收益限于高分辨率重渲染场景；对其他使用场景的适用性，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对前馈高斯泼溅中“训练分辨率下被掩盖、高分辨率重渲染时暴露”的表面覆盖空洞问题，提出轻量残差校正，并在两个数据集的多尺度评测与覆盖分析上给出结果，问题定义清晰且有实际意义；但摘要未提供实现细节、计算开销与更广泛场景验证，是否值得深入阅读取决于读者对前馈高斯泼溅、分辨率鲁棒渲染及 surfel 表示的兴趣。

</details>

<details>
<summary>Abstract</summary>

We present PaveSplat, a feed-forward Gaussian splatting method that adds a learned residual to the analytic surface-aligned covariance, keeping surfels paving the visible surface across rendering resolutions. Pixel-aligned feed-forward Gaussian splatting predicts one primitive per pixel from a few images in a single pass, and its rendering quality depends on how well these primitives cover the surface. Recent surfel-based methods compute the surface-aligned covariance analytically from predicted depth. However, this covariance has no way to correct the surfel orientation where the depth-derived frame is ill-posed. The surfels then cover the surface loosely; at the training resolution each surfel's one-pixel minimum footprint covers the gaps, but they show up as holes when the same prediction is re-rendered at a higher resolution. To address this, we keep the analytic covariance as an initialization, with its axes aligned to the surface tangents, and add an identity-initialized unit-quaternion residual that reorients a surfel only where this improves rendering, turning surfels that the analytic frame mis-aims back onto the surface. On RealEstate10K, PaveSplat achieves the best PSNR, SSIM, and LPIPS among single-Gaussian-per-pixel methods at every scale (1x-8x). The native-resolution gain is small; the benefit appears when the same prediction is rendered at higher display resolutions without re-running the network. On zero-shot DL3DV, it leads PSNR within this group at every scale and ranks first or second on SSIM/LPIPS. A coverage-hole analysis shows fewer uncovered pixels than both baselines under high-resolution re-rendering.

</details>

#### 2026-11-19 - AGSR: Aperture-Guided Super-Resolution for Gaussian Splatting

**Authors:** Ayman Alkhateeb, Hadi Amirpour, Christian Timmerer
**Links:** [abs](https://arxiv.org/abs/2611.25934) - [pdf](https://arxiv.org/pdf/2611.25934)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AGSR: Aperture-Guided Super-Resolution for Gaussian Splatting
- 作者：Ayman Alkhateeb, Hadi Amirpour, Christian Timmerer
- 出版日期：2026-11-19T11:20:23Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.25934) | [PDF](https://arxiv.org/pdf/2611.25934)

### 一句话总结
AGSR 是一种轻量级推理时框架，通过收缩 3DGS 投影协方差、生成多孔径渲染并用不确定性引导的特征聚合融合，实现面向预训练 3DGS 模型的超分辨率增强。

### 研究问题
3D Gaussian Splatting 支持实时新视角合成，但其高斯光栅化会因每个基元的投影协方差而衰减细粒度场景结构。论文关注：在有限高斯足迹造成有效带宽限制的情况下，如何在不重训 3DGS 的前提下恢复被衰减的结构线索并实现超分辨率。

### 核心思路/方法
论文指出，在推理时收缩投影协方差可缓解有限高斯足迹带来的有效带宽限制，并由此提出多孔径渲染框架。AGSR 逐步融合多孔径渲染结果，采用不确定性引导的特征聚合，并利用透射率和深度线索进行几何条件约束。该方法作为预训练 3DGS 模型的插件式增强模块运行。

### 主要贡献
- 揭示高斯光栅化中投影协方差对细尺度结构的衰减效应，并提出推理时协方差收缩以暴露带宽敏感的结构线索。
- 提出 AGSR：轻量级推理时超分辨率框架，融合多孔径渲染、不确定性引导特征聚合与透射率/深度几何条件。
- AGSR 可作为预训练 3DGS 模型的插件式增强，无需重训底层表示。
- 在 Mip-NeRF 360 基准上，AGSR 优于轻量级图像空间超分辨率基线；且底层高斯表示越退化，增益越明显。
- 在保持实时性能的同时，参数量最多为 139k。

### 局限性
摘要未提供足够信息说明其在不同场景类型、极端退化条件或更广泛数据集上的泛化表现；摘要未提供足够信息说明推理开销的具体分解、与完整重训方法的对比，以及协方差收缩策略的参数敏感性。摘要仅报告 Mip-NeRF 360 基准上的结果，其他实验细节摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对 3DGS 推理时增强这一实用方向，方法轻量且插件化，摘要给出了明确的问题动机与基准结论；但摘要未展开关键实现细节与更广泛验证，适合关注 3DGS 超分辨率与实时渲染增强的读者进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel view synthesis, but Gaussian rasterization attenuates fine-scale scene structure through the projected covariance of each primitive. We show that contracting these projected covariances at inference time can mitigate the effective bandwidth limitation induced by finite Gaussian footprints, motivating a multi-aperture rendering framework for super-resolution. Based on this insight, we propose AGSR (Aperture-Guided Super-Resolution), a lightweight inference-time framework that progressively fuses multi-aperture renderings using uncertainty-guided feature aggregation and geometric conditioning from transmittance and depth cues. AGSR operates as a plug-in enhancement for pre-trained 3DGS models. Experiments on the Mip-NeRF 360 benchmark show that AGSR outperforms lightweight image-space super-resolution baselines, with gains increasing as the underlying Gaussian representation deteriorates. The results provide evidence that covariance contraction exposes bandwidth-sensitive structural cues attenuated by native Gaussian rasterization. AGSR achieves these improvements while maintaining real-time performance with up to 139k parameters.

</details>

#### 2026-11-19 - Multi-View Relighting with Mergeable Radiance Fields

**Authors:** Yinan Wang, Rohan Kadkol, Hyunjin Yoo, Jean-François Lalonde, James J. Clark
**Links:** [abs](https://arxiv.org/abs/2611.25523) - [pdf](https://arxiv.org/pdf/2611.25523)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, relighting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-View Relighting with Mergeable Radiance Fields
- 作者：Yinan Wang, Rohan Kadkol, Hyunjin Yoo, Jean-François Lalonde, James J. Clark
- 出版日期：2026-11-19T05:25:36Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.25523) | [PDF](https://arxiv.org/pdf/2611.25523)

### 一句话总结
论文提出 MergeableRF，通过合并不同基光下训练的辐射场外观网络参数，实现多视角重光照，并支持 NeRF 与 3DGS。

### 研究问题
如何在已知基光条件下，利用多视角图像直接合并辐射场参数来完成重光照。摘要指出，虽然光传输具有线性性，但直接合并独立训练的辐射场参数并不能得到对应的图像组合，因此需要解决参数合并与图像组合不一致的问题。

### 核心思路/方法
- 场景由共享几何和每个基光独立的外观网络表示。
- 各外观网络从相同初始化开始，并引入 merge-aware training，使参数组合能够复现对应图像的加权组合。
- 给定目标 HDR 环境图，计算其基光系数，并用这些系数将外观网络合并为单一重光照模型。
- 方法不依赖材质估计、额外重光照网络或目标特定优化；相比图像空间混合，每个视角只需一次渲染。
- 支持 Neural Radiance Fields（NeRF）和 3D Gaussian Splatting（3DGS）。

### 主要贡献
- 提出 MergeableRF，一种通过模型参数合并实现辐射场重光照的方法。
- 设计共享几何、分基光外观网络与 merge-aware training，使参数组合对应图像组合。
- 方法可同时支持 NeRF 与 3DGS，且无需材质估计、额外重光照网络或目标特定优化。
- 摘要称在合成 Neural Gaffer 物体和真实 OLATverse 采集上，重光照质量与使用相同多光照观测训练的方法具有竞争力。

### 局限性
- 摘要未提供足够信息说明方法对基光数量、基光选择或环境图分解误差的敏感性。
- 摘要未提供足够信息说明训练成本、推理效率的具体量化结果。
- 摘要未提供足够信息说明在复杂材质、非朗伯表面或大场景中的泛化表现。
- 摘要未提供足够信息说明与基线方法的完整定量对比和失败案例分析。

### 阅读优先级
中。理由：该论文关注多视角重光照与辐射场参数合并，问题定义清晰，且同时支持 NeRF 与 3DGS，具有一定方法参考价值；但当前仅有摘要信息，实验细节、定量结果和局限性尚未充分展开，适合作为相关方向的中优先级阅读。

</details>

<details>
<summary>Abstract</summary>

We propose MergeableRF, a method for radiance field relighting through model parameter merging. Given multi-view images of a scene under known basis lights, our goal is to relight the scene by directly combining the parameters of radiance fields trained under these lights. This is motivated by the linearity of light transport: the image under a mixture of lights is the same weighted combination of the images under each light. However, combining the parameters of independently trained radiance fields does not produce the corresponding combination of images. To address this, we represent a scene with shared geometry and a separate appearance network for each basis light. We start these networks from the same initialization and introduce merge-aware training, which teaches their parameter combinations to reproduce the corresponding combinations of images. Given a target HDR environment map, we compute its basis-light coefficients and use them to merge the appearance networks into a single relit model. Our method supports both Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS), without material estimation, additional relighting networks, or target-specific optimization. Unlike image-space blending, it requires only one rendering pass per viewpoint. Experiments on synthetic Neural Gaffer objects and real OLATverse captures demonstrate relighting quality competitive with methods trained on the same multi-light observations.

</details>

#### 2026-11-19 - Watertight Mesh Optimization of Textured Objects

**Authors:** Nathaniel Burgdorfer, Philippos Mordohai
**Links:** [abs](https://arxiv.org/abs/2611.25414) - [pdf](https://arxiv.org/pdf/2611.25414)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** geometric reconstruction, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Watertight Mesh Optimization of Textured Objects
- 作者：Nathaniel Burgdorfer, Philippos Mordohai
- 出版日期：2026-11-19T02:53:08Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2611.25414

### 一句话总结
论文提出 MODL 框架，直接在水密三角形网格上联合优化几何与视角相关外观，以兼顾新视角合成、几何精度和网格内在质量。

### 研究问题
从图像重建高质量 3D 资产时，现有方法往往擅长某一目标而牺牲另一目标，并且经常忽视重建表面的内在质量。论文关注如何统一照片级渲染、几何重建与实用 3D 资产生成。

### 核心思路/方法
MODL 直接在水密三角形网格上联合优化几何和视角相关外观。方法结合拉普拉斯预条件优化以实现平滑的顶点更新，并使用曲率自适应重网格化来保留细节和形状良好的三角形。三角形网格在多视图归一化互相关约束下优化，且不使用分割、几何监督或 alpha 混合。

### 主要贡献
- 提出 MODL，一个直接在水密三角形网格上联合优化几何与视角相关外观的框架。
- 结合拉普拉斯预条件优化与曲率自适应重网格化，以平滑更新顶点并保留细节与良好三角形形状。
- 在多视图归一化互相关约束下优化网格，不依赖分割、几何监督或 alpha 混合。
- 在物体重建数据集上的评估表明，MODL 在新视角合成上具有竞争力，同时生成几何准确且网格内在质量更优的模型。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集名称、定量指标、运行时间、内存开销、失败案例或与其他方法的详细对比结果。

### 阅读优先级
中。理由：论文主题与神经场景表示、网格优化和 3D 资产重建直接相关，摘要明确提出了联合优化几何与外观、水密网格、无分割与无几何监督等特点，具有方法参考价值；但摘要未提供实验细节与定量结果，需阅读全文后才能判断其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

When reconstructing high-quality 3D assets from images, existing approaches often excel at one objective while compromising another, and frequently overlook the intrinsic quality of the reconstructed surfaces. We present MODL, a framework that jointly optimizes geometry and view-dependent appearance directly on a watertight triangle mesh. Our approach combines Laplacian-preconditioned optimization for smooth vertex updates with curvature-adaptive remeshing to preserve fine details and well-shaped triangles. The triangle mesh is optimized subject to multi-view normalized cross-correlation constraints, but without segmentation, geometric supervision or alpha-blending. Evaluations on object reconstruction datasets demonstrate that MODL achieves competitive novel-view synthesis while producing geometrically accurate models with superior intrinsic mesh quality. Our results highlight the potential of direct mesh optimization to unify photorealistic rendering, geometric reconstruction, and practical 3D asset creation.

</details>

#### 2026-11-19 - VideoRNG: Relightable Neural Gaussians from Generative Video Models

**Authors:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi, Zahra Montazeri, Miloš Hašan
**Links:** [abs](https://arxiv.org/abs/2611.25338) - [pdf](https://arxiv.org/pdf/2611.25338)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VideoRNG: Relightable Neural Gaussians from Generative Video Models
- 作者：Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi, Zahra Montazeri, Miloš Hašan
- 出版日期：2026-11-19T01:25:30Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.25338 ；PDF https://arxiv.org/pdf/2611.25338

### 一句话总结
VideoRNG 提出一种两阶段方法，借助生成视频模型与大规模重建模型，从文本或单张图像生成可重打光、可交互渲染的神经高斯 3D 资产，且无需预设网格或解析材质模型。

### 研究问题
论文针对的问题是：传统表面网格与紧凑的基于物理材质难以表达外观依赖精细几何或复杂光传输的物体；现有高斯泼溅生成器通常将固定光照烘焙进外观，导致生成资产难以重打光。摘要指出，生成真实感 3D 资产仍受经典表示限制。

### 核心思路/方法
- 两阶段生成流程：第一阶段，从预训练视频扩散骨干微调得到的视频生成器，在已知姿态、相机和光照下生成结构化的 RGBA 转台序列。
- 第二阶段，由预训练视频扩散骨干初始化前馈大规模重建模型，将选定转台帧的视频 VAE 潜帧直接映射为带学习神经外观特征的数百万各向异性高斯。
- 表示与渲染：通过共享方向解码器与随机高斯光线追踪器，将所提出的“光线追踪可重打光神经高斯”（rtRNG）表示转换为新视角与新光照下的辐射。
- 训练与效率：引入深度锚定外观训练，以在学习几何的同时保留高频外观；通过前景 token 选择与成本感知分布式采样，使百万级高斯重建变得可行。

### 主要贡献
- 提出 VideoRNG，一种从文本提示或单张图像生成完整、可重打光 3D 资产的两阶段方法，不预设网格或解析材质模型。
- 提出 rtRNG 表示，结合神经高斯、学习神经外观特征、共享方向解码器与随机高斯光线追踪器，支持新视角和新光照下的辐射生成。
- 引入深度锚定外观训练，以兼顾几何学习与高频外观保留。
- 通过前景 token 选择与成本感知分布式采样，提升百万级高斯重建的可行性。
- 摘要称可生成毛皮、羽毛、蜘蛛网等复杂资产，并支持交互式渲染、重打光与场景集成。

### 局限性
摘要未提供足够信息说明局限性、失败案例、定量评估、数据集规模、计算成本或与基线方法的完整对比。摘要仅提到方法面向百万级高斯重建的效率问题，但未给出具体限制或适用范围。

### 阅读优先级
中。理由：论文主题属于神经场景表示与渲染，且涉及生成式视频模型、可重打光神经高斯和大规模重建，问题定位与方法组合具有明确研究价值；但当前仅提供摘要，缺少实验细节、定量结果与局限性说明，是否值得优先精读需结合后续正文信息判断。

</details>

<details>
<summary>Abstract</summary>

Generating realistic 3D assets remains constrained by classical representations: surface meshes and compact physically based materials struggle to express objects whose appearance arises from fine geometry or complex light transport, while existing Gaussian-splatting generators typically bake fixed illumination into appearance. We introduce VideoRNG, a two-stage method that generates complete, relightable 3D assets from a text prompt or a single image without prescribing a mesh or analytic material model. A video generator fine-tuned from a pretrained video diffusion backbone first produces a structured RGBA turntable sequence under a known pose, camera, and illumination. A feed-forward large reconstruction model initialized from a pretrained video diffusion backbone then maps the video-VAE latent frames of selected turntable frames directly to millions of anisotropic Gaussians with learned neural appearance features. A shared directional decoder and stochastic Gaussian ray tracer turn this representation, which we call ray-traced Relightable Neural Gaussians (rtRNG), into radiance under novel viewpoints and illumination. To preserve high-frequency appearance while learning geometry, we introduce depth-anchored appearance training, and we make million-Gaussian reconstruction practical through foreground token selection and cost-aware distributed sampling. VideoRNG generates complex assets such as fur, feathers, and spider webs that can be interactively rendered, relit, and integrated into scenes.

</details>

#### 2026-11-18 - Multi-Band Galaxy Novel-View Synthesis with Radiative Gaussian Fields

**Authors:** Yuzhe Wu, Jialin Zhu, Doğa Yılmaz, Daisuke Kawata, He Wang
**Links:** [abs](https://arxiv.org/abs/2611.24723) - [pdf](https://arxiv.org/pdf/2611.24723)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-Band Galaxy Novel-View Synthesis with Radiative Gaussian Fields
- 作者：Yuzhe Wu, Jialin Zhu, Doğa Yılmaz, Daisuke Kawata, He Wang
- 出版日期：2026-11-18T16:41:49Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.24723) / [PDF](https://arxiv.org/pdf/2611.24723)

### 一句话总结
论文提出面向星系多波段观测数据的新视角合成方法 GalaxyGS，在 Gaussian Splatting 框架中引入物理启发的能量辐射与光传播建模，以提升合成精度与物理保真度。

### 研究问题
现有 Gaussian Splatting 主要在 RGB 数据上取得成功，而星系观测数据具有多波段信号、大量天体、跨波段复杂相互作用以及高度非均匀介质中的光传播等特点。摘要指出，这类底层物理过程给模型表示与优化带来很大挑战，且现有研究尚未对此进行探讨。论文关注的核心问题是：如何为星系多波段观测构建具备物理意义表示能力的新视角合成方法。

### 核心思路/方法
论文提出一种物理启发的 Gaussian Splatting 方法 GalaxyGS。根据摘要，该方法包含具有物理意义的组件，用于同时刻画不同天体的能量发射机制以及天体之间的光传播过程。其目标不是简单套用 RGB 场景中的 GS，而是针对星系多波段观测中的能量发射与异质介质光传播进行建模。摘要未提供足够信息说明具体网络结构、物理公式、训练损失或优化细节。

### 主要贡献
- 提出面向星系多波段观测的新视角合成工具 GalaxyGS，将 Gaussian Splatting 扩展到该任务。
- 在方法中引入物理意义组件，以刻画不同天体的能量发射机制和天体间的光传播。
- 指出星系多波段数据相较 RGB 数据在模型表示与优化上的特殊挑战，并将其作为方法设计动机。
- 由于缺乏可直接比较的基线方法，摘要称采用多种可能的替代方法进行广泛比较，并在多个数据集与指标上表明 GalaxyGS 在准确性和物理保真度方面更优。摘要未提供足够信息说明具体数据集、指标数值和对比方法列表。

### 局限性
摘要未提供足够信息说明方法的具体假设、失败场景、计算开销、对真实观测噪声的鲁棒性以及物理建模的适用范围。由于没有可直接比较的基线方法，摘要虽称采用多种替代方案进行比较，但未给出这些替代方案的具体构成与实验设置，因此其比较的完备性无法仅凭摘要判断。摘要未提供足够信息说明定量结果、消融实验和泛化能力。

### 阅读优先级
中。理由：该论文将 Gaussian Splatting 从常规 RGB 新视角合成拓展到星系多波段观测，并强调物理启发的能量发射与光传播建模，主题与 Neural Scene Representations & Rendering 分类高度相关，对关注科学数据渲染、物理保真新视角合成或多波段场景表示的读者有潜在价值。但摘要未给出具体实验数值、基线细节和实现信息，是否值得深入阅读需进一步查看正文实验与物理建模细节。

</details>

<details>
<summary>Abstract</summary>

We propose a novel view synthesis tool for galaxies based on Gaussian Splatting (GS). Unlike RGB data, where GS has achieved success, galaxy observations consist of multi-band signals from a massive number of bodies, contain complex patterns of cross-band interactions, and capture light propagation in highly heterogeneous media. As a result, the underlying physical process poses great challenges in model representation and optimization, which have not been investigated in existing research. To this end, we propose a physically inspired Gaussian Splatting method, GalaxyGS, which is equipped with physically meaningful components that capture both the energy emission mechanism of different astronomical bodies and the light propagation between them. In the absence of directly comparable baseline methods, we adopt a wide range of possible alternative approaches. Comparisons conclusively demonstrate that GalaxyGS is better in accuracy and physical fidelity across datasets and metrics.

</details>

#### 2026-11-18 - Gaussian Primitive Fusion for Any-Resolution Multimodal Images

**Authors:** Baoshuo Cai, Xinrui Jiang, Bing Cao
**Links:** [abs](https://arxiv.org/abs/2611.24164) - [pdf](https://arxiv.org/pdf/2611.24164)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian primitive

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Primitive Fusion for Any-Resolution Multimodal Images
- 作者：Baoshuo Cai, Xinrui Jiang, Bing Cao
- 出版日期：2026-11-18T10:06:21Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.24164 ；PDF https://arxiv.org/pdf/2611.24164

### 一句话总结
论文提出高斯图元融合（GPF），将异构分辨率的多模态图像融合改为在共享连续高斯空间中直接拟合各模态原生分辨率观测，并在最细原生分辨率上渲染融合结果，避免先重采样再融合带来的伪影。

### 研究问题
多模态图像融合需要整合不同模态的互补信息。现有方法通常在共同离散网格上估计模态贡献；当源模态原生分辨率不同时，构建该网格往往需要重采样，可能引入伪影并影响后续融合决策。论文关注的核心问题是：如何在不先把源图像转换到共同分辨率的前提下，实现异构分辨率多模态图像的有效融合。

### 核心思路/方法
GPF 将异构分辨率融合重新表述为共享连续高斯空间中的问题。方法不先将源图像转换为共同分辨率，而是用共享的高斯几何和模态特定的内容表示，直接拟合各源图像原生分辨率的观测，并在所得连续表示中学习模态贡献。优化完成后，融合表示在最细原生分辨率上渲染，而不对源图像进行重采样。

### 主要贡献
- 提出 GPF，将异构分辨率多模态融合放到共享连续高斯空间中处理。
- 使用共享高斯几何与模态特定内容表示直接拟合原生分辨率观测，并在连续表示中学习模态贡献。
- 融合表示在最细原生分辨率上渲染，避免对源图像重采样。
- 摘要称在异构分辨率输入下，GPF 相比“先重采样再融合”流程产生更清晰的目标轮廓和更精细的纹理，模糊与块状伪影更少。
- 摘要称在多个红外-可见光基准上，相较配备插值或超分辨率前端的先进融合方法取得最佳定量结果。

### 局限性
摘要未提供足够信息说明计算复杂度、训练与优化开销、对高斯表示初始化或超参数的敏感性、不同模态配准误差的影响、除红外-可见光之外任务的泛化性，以及具体实验设置和消融细节。摘要亦未提供足够信息说明“最细原生分辨率”渲染在极端分辨率差异下的表现边界。

### 阅读优先级
中。理由：论文针对异构分辨率多模态融合中的重采样伪影问题提出较清晰的连续表示思路，并与红外-可见光融合基准上的先进方法进行比较；但摘要未给出方法实现细节、失败条件和消融证据。若关注多模态融合、任意分辨率处理或神经场景表示与渲染交叉方向，可优先阅读；否则可作为中等优先级跟踪。

</details>

<details>
<summary>Abstract</summary>

Multimodal image fusion integrates complementary observations from different modalities into a unified representation. Existing methods typically estimate modality contributions on a common discrete grid. When source modalities have different native resolutions, constructing such a grid generally involves resampling, which may introduce artifacts and affect subsequent fusion decisions. To address this problem, we propose Gaussian Primitive Fusion (GPF), which reformulates heterogeneous-resolution fusion in a shared continuous Gaussian space. Instead of first converting source images to a common resolution, GPF directly fits their native-resolution observations with shared Gaussian geometry and modality-specific content representations, and learns modality contributions within the resulting continuous representation. Once optimized, the fused representation is rendered at the finest native resolution without resampling the sources. With heterogeneous-resolution inputs, GPF produces clearer target contours and finer textures, with less blurring and blocking artifacts than resample-then-fuse pipelines. Quantitatively, it achieves the best results on multiple infrared-visible benchmarks against state-of-the-art fusion methods equipped with interpolation or super-resolution frontends.

</details>

#### 2026-11-18 - Facet-SLAM: Real-Time Triangle Splatting SLAM

**Authors:** Edward Beng Wai Tan, Siew-Kei Lam
**Links:** [abs](https://arxiv.org/abs/2611.23935) - [pdf](https://arxiv.org/pdf/2611.23935)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Facet-SLAM: Real-Time Triangle Splatting SLAM
- 作者：Edward Beng Wai Tan, Siew-Kei Lam
- 出版日期：2026-11-18T06:23:49Z
- 分类：Neural Scene Representations & Rendering（主分类）；3D Reconstruction & Multi-view Geometry（次分类）
- 链接：[摘要](https://arxiv.org/abs/2611.23935) / [PDF](https://arxiv.org/pdf/2611.23935)

### 一句话总结
Facet-SLAM 是首个面向 RGB-D 相机的实时三角形 splatting SLAM 系统，通过将“跟踪”与“建图”的职责分离，使跟踪摆脱缓慢的光度方法，在保持渲染质量的同时提升表面精度并大幅提速。

### 研究问题
摘要指出两个层面的问题：
1. **表示层面的问题**：基于 3D Gaussian splatting 的稠密 SLAM 虽能逼真渲染，但表面几何质量差，且获得 mesh（网格）需要额外的提取或融合阶段；三角形 splatting 的顶点可直接三角化为连通 mesh，从而避免这一问题。
2. **SLAM 系统层面的问题**：已有的三角形 splatting SLAM 依赖光度跟踪（photometric tracking），速度过慢，无法在传感器速率下完成定位。论文要解决的问题是：如何在三角形 splatting 表示上实现实时定位与建图。

### 核心思路/方法
- **采用几何配准的动机与障碍**：快速几何配准是光度跟踪的自然替代，但摘要指出它单独不够用；原因是 mapper 的优化会把三角形从已观测表面上移开，使其成为不可靠的配准目标。
- **职责分离**：将跟踪器与建图器的角色分开。
  - **Tracker**：由融合深度设定每个三角形的质心（centroid），并用 GICP 将帧配准到这些质心。
  - **Mapper**：通过变量替换（change of variables），把更新限制为非平移更新（non-translating updates），避免三角形被优化推离观测表面。
- **实时性目标**：面向 RGB-D 相机实现实时运行。

### 主要贡献
摘要明确给出的贡献包括：
1. 提出 Facet-SLAM，称其为首个面向 RGB-D 相机的实时三角形 splatting SLAM 系统。
2. 提出跟踪与建图职责分离的设计：tracker 用融合深度设定三角形质心并以 GICP 配准；mapper 通过变量替换限制为非平移更新。
3. 性能与精度结果（摘要所述）：
   - 桌面 GPU 上约 100 FPS，取得有竞争力的跟踪精度；
   - 在 Jetson AGX Orin 上以传感器速率运行；
   - 相比光度方法提速超过 20 倍，渲染质量相当，并提升表面精度；
   - 在 Replica 上，Delaunay mesh 的 chamfer distance 从 1.55 cm 降至 0.86 cm。
4. 承诺开源实现（GitHub 链接见摘要）。

### 局限性
- 摘要未提供足够信息说明方法在哪些场景下会失败，也未说明其对深度质量、动态场景或大尺度场景的适应性。
- 摘要未提供足够信息说明与光度方法对比之外的基线比较细节、数据集规模与评测协议。
- 摘要未提供足够信息说明变量替换约束对建图表达能力的潜在限制，以及长期运行下的漂移表现。
- 摘要未提供足够信息说明内存占用、Jetson 上的具体帧率数值及精度数值。

### 阅读优先级
**高**。理由：论文针对三角形 splatting SLAM 的实时性瓶颈给出明确的结构性方案（跟踪/建图职责分离与非平移更新约束），并报告了显著的提速与表面精度提升（chamfer distance 1.55→0.86 cm），且承诺开源；对关注实时稠密 SLAM、可网格化场景表示与几何配准跟踪的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Dense SLAM systems based on 3D Gaussian splatting build maps that render photorealistically, but their surface geometry is poor, and obtaining a mesh requires extraction or fusion stages. Triangle splatting avoids this with surface primitives whose vertices can be triangulated directly into a connected mesh, yet SLAM with this representation has so far relied on photometric tracking, which is too slow for localization at sensor rate. We present Facet-SLAM, the first real-time triangle splatting SLAM system for RGB-D cameras. Fast geometric registration is the natural alternative, but it is not sufficient alone, since the mapper's optimization displaces triangles from the observed surface and makes them unreliable registration targets. We therefore separate the two roles: the tracker sets each triangle's centroid from fused depth and registers frames to these centroids by GICP, while the mapper is restricted to non-translating updates via a change of variables. Our system achieves competitive tracking accuracy at around 100 FPS on a desktop GPU and runs at sensor rate on a Jetson AGX Orin. Compared with the photometric approach, it is over 20 times faster, matches rendering quality, and improves surface accuracy, reducing the chamfer distance of the Delaunay mesh on Replica from 1.55 to 0.86 cm. We will release the implementation at https://github.com/edward62740/Facet-SLAM.

</details>

#### 2026-11-18 - A Hierarchical Onboard Vision-Language-Navigation Framework for Aerial Robots in Complex Environments

**Authors:** Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Zhaoqi Wang, Yuxin Fan, Wenjun Li, Kenghou Hoi, Zhichao Han, Xin Zhou, Fei Gao
**Links:** [abs](https://arxiv.org/abs/2611.23930) - [pdf](https://arxiv.org/pdf/2611.23930)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, AR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Hierarchical Onboard Vision-Language-Navigation Framework for Aerial Robots in Complex Environments
- 作者：Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Zhaoqi Wang, Yuxin Fan, Wenjun Li, Kenghou Hoi, Zhichao Han, Xin Zhou, Fei Gao
- 出版日期：2026-11-18T06:21:08Z
- 分类：主分类为 Neural Scene Representations & Rendering；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.23930 ；PDF https://arxiv.org/pdf/2611.23930 ；项目页 https://wyz000.github.io/VLN-AR/

### 一句话总结
该论文提出面向复杂环境下空中机器人的分层视觉—语言—导航框架 VLN-AR，通过解耦多模态推理与底层控制、自动化 3DGS 数据生成、三阶段训练、轻量认知代理和板载优化，在资源受限 UAV 平台上兼顾长程导航性能与计算效率。

### 研究问题
摘要指出，UAV 期望在严格板载约束下实现语义推理、智能决策和长程导航；现有基础模型驱动方法仍受限于 3D 数据可得性、轨迹可行性、长程推理以及复杂环境中的计算效率等问题。论文旨在弥合这些差距。

### 核心思路/方法
- 提出分层 VLN 框架 VLN-AR，将多模态推理与底层控制解耦，进行 3D 位姿命令和导航意图的结构化预测，并转化为动态可行动作。
- 引入基于 3D Gaussian Splatting（3DGS）的全自动流程，生成可扩展、照片级真实的 UAV 导航数据，以缓解数据稀缺和域差距。
- 采用渐进式三阶段训练策略，增强 grounding、场景推理和复杂导航能力。
- 使用轻量认知代理，通过记忆感知的任务分解提升长程推理。
- 设计板载优化技术，包括 token 稀疏化和模型轻量化，摘要称实现 7.1x–9.4x 加速，同时在资源受限 UAV 平台上保持较高导航性能。

### 主要贡献
- 提出面向空中机器人的分层 VLN 框架 VLN-AR，解耦多模态推理与底层控制。
- 提出基于 3DGS 的全自动可扩展真实感 UAV 导航数据生成流程。
- 提出渐进式三阶段训练策略与记忆感知任务分解的轻量认知代理。
- 给出板载 token 稀疏化和模型轻量化优化，并报告加速效果。
- 摘要称在仿真和真实 UAV 导航中相较现有方法有显著提升；具体实验设置与指标摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法在极端环境、不同 UAV 平台或真实部署中的失败模式与适用范围。
- 摘要未提供足够信息说明 3DGS 数据生成流程的保真度评估、数据规模及域差距量化结果。
- 摘要未提供足够信息说明三阶段训练各阶段的具体设计、消融实验和对比基线细节。
- 摘要未提供足够信息说明 7.1x–9.4x 加速对应的硬件平台、模型规模、精度损失边界及端到端延迟。
- 摘要未提供足够信息说明真实世界实验规模、任务类型、成功率和安全性评估。

### 阅读优先级
高。理由：该论文聚焦 UAV 板载视觉—语言—导航这一具身智能与空中机器人交叉方向，同时覆盖数据生成、分层控制、长程推理和板载效率等关键瓶颈；摘要给出的 3DGS 数据流程与 7.1x–9.4x 加速指标具有较强工程与系统参考价值。但具体实验细节需查阅全文后判断。

</details>

<details>
<summary>Abstract</summary>

Unmanned Aerial Vehicles (UAVs) are expected to achieve semantic reasoning, intelligent decision-making, and long-horizon navigation under strict onboard constraints. While recent foundation-model-driven approaches have shown promising progress toward this goal, existing methods remain limited by challenges in 3D data availability, trajectory feasibility, long-horizon reasoning, and computational efficiency in complex environments. To bridge these gaps, we propose VLN-AR, a hierarchical vision-language-navigation (VLN) framework for aerial robots. VLN-AR decouples multimodal reasoning and low-level control, enabling structured prediction of 3D pose commands and navigation intentions that are translated into dynamically feasible actions. To mitigate data scarcity and domain gaps, we introduce a fully automated 3D Gaussian Splatting (3DGS)-based pipeline to generate scalable photorealistic UAV navigation data. A progressive three-stage training strategy further enhances grounding, scene reasoning, and complex navigation. In addition, a lightweight cognitive agent improves long-horizon reasoning via memory-aware task decomposition. Finally, we design onboard optimization techniques, including token sparsification and model lightweighting, achieving 7.1x-9.4x speedup while maintaining high navigation performance on resource-limited UAV platforms. Experiments show great improvements over existing methods in both simulation and real-world UAV navigation. Project website: https://wyz000.github.io/VLN-AR/

</details>

#### 2026-11-18 - Improving While Deployed: Learning Proactive End-to-End Driving from Imperfect Human Takeover Data

**Authors:** Yangang Ren, Di Zeng, Jun Li, Zirui Li, Chengjiang Zhang, Xiaoqing Ye, Ji Tao, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2611.23719) - [pdf](https://arxiv.org/pdf/2611.23719)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Improving While Deployed: Learning Proactive End-to-End Driving from Imperfect Human Takeover Data
- 作者：Yangang Ren, Di Zeng, Jun Li, Zirui Li, Chengjiang Zhang, Xiaoqing Ye, Ji Tao, Chen Lv
- 出版日期：2026-11-18T02:21:40Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.23719 ；PDF https://arxiv.org/pdf/2611.23719

### 一句话总结
该文提出一种离线后训练框架，将部署后收集的不完美人类接管数据转化为主动式监督信号，用于更新端到端驾驶模型，且不改变其推理架构。

### 研究问题
论文关注的问题是：端到端驾驶模型部署到车辆后，会持续遇到困难场景并产生包含模型输出与人类行为的人类接管数据；但人类干预往往并不完美，可能介入过晚或不必要地介入，因此直接模仿这些数据会强化迟滞反应或抑制原本合理的驾驶动作。论文要解决的是如何利用这类不完美接管数据进行有效更新，而不是简单模仿。

### 核心思路/方法
论文提出离线后训练框架，主要包含以下步骤：
1. 通过对已部署模型的规划进行增强，并将记录到的人类纠正动作在时间上提前，构建多样化的候选轨迹。
2. 训练一个场景条件轨迹评分器，利用专家演示和来自接管日志的非配对偏好信号对候选轨迹进行排序。
3. 使用该评分器，在接管前场景中选择性替换训练目标为得分更高的候选，同时在正常驾驶场景中保留原始目标。
4. 将得到的目标蒸馏进驾驶模型，且不改变其推理架构。

### 主要贡献
1. 提出一种离线后训练框架，将不完美的人类接管数据转化为主动式监督。
2. 通过候选轨迹构建与场景条件轨迹评分器，结合专家演示和接管日志中的非配对偏好信号进行候选排序。
3. 在选择训练目标时，对接管前场景进行选择性替换，并在正常场景保留原始目标，最终蒸馏到原推理架构中。
4. 在基于真实场景并以4D Gaussian splatting重建的闭环评估中，该方法取得最高总体成功率，优于已部署模型、直接模仿学习和轨迹后优化。

### 局限性
论文摘要未提供足够信息说明计算开销、候选轨迹构建的覆盖范围、评分器偏差、对真实车队日志规模与分布的要求，以及闭环评估的具体场景数量与统计细节。摘要未提供足够信息说明该方法在更广泛真实部署条件下的泛化性与安全性边界。

### 阅读优先级
中。理由：该论文聚焦部署后利用真实接管日志进行端到端驾驶模型更新，问题设定具有实际意义，方法与闭环评估结果在摘要中有明确概括；但其主要贡献与分类标签“Neural Scene Representations & Rendering”之间的关系、以及实验细节和局限性均需阅读全文进一步确认。

</details>

<details>
<summary>Abstract</summary>

Once deployed on vehicles, end-to-end driving models continuously encounter challenging scenarios, generating valuable human takeover data that capture both model outputs and human behaviors. However, human interventions are often imperfect, as drivers may intervene too late or unnecessarily. Consequently, direct imitation can reinforce late responses or discourage otherwise appropriate maneuvers. To address this challenge, we propose an offline post-training framework that transforms imperfect takeover data into proactive supervision. We first construct diverse trajectory candidates by augmenting the plans of the deployed model and shifting recorded human corrective maneuvers earlier in time. We then train a scene-conditioned trajectory scorer to rank these candidates using expert demonstrations and unpaired preference signals from takeover logs. Using this scorer, we selectively replace pre-takeover training targets with higher-scoring candidates while retaining the original targets in normal driving scenarios. Finally, we distill the resulting targets into the driving model without changing its inference architecture. In closed-loop evaluations using real-world scenarios reconstructed with 4D Gaussian splatting, our method achieves the highest overall success rate, outperforming the deployed model, direct imitation learning and trajectory post-optimization. These results highlight a practical path toward efficient updates of deployed driving models using existing fleet logs.

</details>

#### 2026-11-18 - EyeDiT: Anatomy-Grounded Multi-Modal Eye Generation and Simulation

**Authors:** Yonghan Lee, Zachary Willms, Kun Liu, Pushkar Anand, Ali Behrooz, Dmitri Model, Dinesh Manocha, Yatong An
**Links:** [abs](https://arxiv.org/abs/2611.23670) - [pdf](https://arxiv.org/pdf/2611.23670)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, AR, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EyeDiT: Anatomy-Grounded Multi-Modal Eye Generation and Simulation
- 作者：Yonghan Lee, Zachary Willms, Kun Liu, Pushkar Anand, Ali Behrooz, Dmitri Model, Dinesh Manocha, Yatong An
- 出版日期：2026-11-18T00:51:40Z
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（次）
- 链接：摘要页 https://arxiv.org/abs/2611.23670 ；PDF https://arxiv.org/pdf/2611.23670 ；项目页 https://lyhan12.github.io/eyedit

### 一句话总结
EyeDiT 是一个以眼部解剖结构为基础、多模态的 3D 眼睛生成与仿真模型，利用 OCT、带解剖标注的点云和近眼图像训练，可控制瞳孔、受试者身份与视角，并提升眼动追踪的仿真到真实迁移效果。

### 研究问题
现有合成眼睛数据生成器主要面向图像，缺乏高质量的眼部 3D 解剖底层表示，因此控制能力主要限于注视方向，且不提供解剖标签。这限制了合成眼数据在 AR/VR 眼动追踪快速开发中的价值。论文旨在解决如何在生成与仿真中引入解剖结构，并实现对瞳孔、受试者身份和视角的控制。

### 核心思路/方法
论文提出 EyeDiT，训练数据包括 OCT、带解剖标注的解剖点云和近眼图像。流程分两步：首先训练多模态解剖变分自编码器（Multi-Modal Anatomy VAE），从所有输入模态中编码出具有解剖感知的潜在表示；然后训练 Eye Latent DiT，以光轴、瞳孔位置与半径、受试者身份为条件生成潜在样本。结合用于新视角仿真的高斯解码器，模型支持对瞳孔、受试者身份和视点进行控制以合成数据。

### 主要贡献
- 提出以解剖结构为基础的多模态 3D 眼睛生成与仿真模型 EyeDiT，弥补现有生成器缺乏 3D 解剖底层表示和解剖标签的不足。
- 设计多模态解剖 VAE 与 Eye Latent DiT 的两阶段框架，实现以光轴、瞳孔位置与半径、受试者身份为条件的潜在生成。
- 结合高斯解码器支持新视角仿真，使数据合成可控制瞳孔、受试者身份和视点。
- 在新视角合成上优于此前眼睛图像合成模型（单视角 PSNR 24.9 dB 对 21.8 dB）。
- 用其合成数据训练公开眼动追踪网络时，仿真到真实差距小于其他生成器数据（注视误差 3.5° 对 8.4°），接近真实数据训练的网络；与真实数据结合后进一步提升眼动追踪性能（2.3° 对 2.6°）。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法的具体失败情形、计算开销、对特定设备或数据采集条件的依赖，也未说明在更广泛受试者群体或真实 AR/VR 场景中的泛化边界。

### 阅读优先级
高。理由：该工作直接针对合成眼数据的解剖缺失问题，涉及多模态生成、3D 神经表示与 AR/VR 眼动追踪应用；摘要给出了明确的新视角合成和仿真到真实迁移的量化改进，且与主分类“神经场景表示与渲染”和次分类“AR 应用”高度相关，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Synthetic eye data are critical for rapid development of eye tracking (ET) in AR/VR applications. However, existing synthetic eye generators are largely image-centric and lack a high-quality underlying 3D anatomy of the eye, which limits their control mainly to the gaze and provides no anatomical labels. To address this problem, we propose EyeDiT, an anatomy-grounded, multi-modal 3D eye generation and simulation model trained with optical coherence tomography (OCT), labeled anatomy point clouds and near-eye images. Our pipeline first trains a Multi-Modal Anatomy Variational Autoencoder (VAE), which encodes an anatomy-aware latent representation from all input modalities. Then, our Eye Latent DiT is trained to generate latent samples conditioned on the optical axis, the pupil position and radius, and the subject identity. Together with Gaussian decoders for novel-view simulation, our model enables control over the pupil, subject identity and viewpoint for data synthesis. We show that our model outperforms previous eye image synthesis models in novel-view synthesis (24.9 against 21.8 dB PSNR from a single view), and that a public ET neural network trained on our synthetic data shows a smaller sim-to-real gap than when trained on data from other generators (3.5$^\circ$ vs. 8.4$^\circ$ gaze error), approaches a network trained on real data, and further improves ET performance when combined with real data (2.3$^\circ$ vs. 2.6$^\circ$). More information is available on the project page: https://lyhan12.github.io/eyedit

</details>

#### 2026-11-17 - NIRJALA: Draining the Sea out of Gaussian Splatting with Three-Path Optics and Reversible Physics

**Authors:** Latchan Chhetri, Aman Kumar
**Links:** [abs](https://arxiv.org/abs/2611.23450) - [pdf](https://arxiv.org/pdf/2611.23450)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NIRJALA: Draining the Sea out of Gaussian Splatting with Three-Path Optics and Reversible Physics
- 作者：Latchan Chhetri, Aman Kumar
- 出版日期：2026-11-17T19:53:32Z
- 分类：Neural Scene Representations & Rendering（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2611.23450) / [PDF](https://arxiv.org/pdf/2611.23450)

### 一句话总结
NIRJALA 是一个面向水下场景的 3D Gaussian Splatting 框架，通过引入距离饱和的前向散射项与可逆物理锚定，联合恢复无水外观与几何，缓解传统“按指数透射率做除法”导致的反演增益无界问题。

### 研究问题
论文指出，水下图像中每个像素混合了衰减后的场景辐射、后向散射光以及前向散射的场景光，且同一组像素可由多种“场景—水体”组合解释，存在病态性。多数面向水下场景的高斯泼溅方法只建模前两种效应，并通过除以随距离指数衰减的透射率来“去除水体”，导致反演增益（inversion gain）无界增长。因此，如何在建模三路光学效应的同时，保证反演稳定并联合恢复无水外观与几何，是本文关注的问题。

### 核心思路/方法
- **TRIVENI（三路图像形成模型）**：在直接透射与后向散射之外，加入“距离饱和的前向散射项”，并声称证明该设计使反演增益在任意距离下保持有界，同时给出估计的后向散射与衰减误差向恢复颜色传播的界。
- **PRATIBIMBA（可逆物理锚）**：将灵活的神经水体模型与一个十参数物理模型双向绑定，使场景内容不能“藏”在水体模型中。
- **SAMARASA（物理约束目标集合）**：汇集物理信息目标，其中包括按距离分箱的颜色先验。
- **SAJALA 评测套件**：为在有真值条件下评估去水效果，构建了 30 个场景的 Blender Cycles 路径追踪套件，提供无水图像、深度、法线，并在受控水色与浊度下生成。

### 主要贡献
1. 提出 NIRJALA 框架，联合恢复水下场景的无水外观与几何。
2. 提出三路图像形成模型 TRIVENI，加入距离饱和前向散射项，并论证反演增益有界及误差传播界。
3. 提出可逆物理锚 PRATIBIMBA，双向约束神经水体模型与十参数物理模型。
4. 提出包含距离分箱颜色先验的物理约束目标集合 SAMARASA。
5. 构建 30 场景路径追踪评测套件 SAJALA，并提供无水图像、深度与法线真值。
6. 报告在 SAJALA 上相对最强基线将 PSNR 从 24.34 提升至 24.76 dB、深度 AbsRel 从 0.109 降至 0.091；在真实 SeaThru-NeRF 场景上将 LPIPS 从 0.194 降至 0.175，并以 44 FPS 渲染。
7. 讨论水下外观指标与几何指标不一致的现象及评估局限。

### 局限性
- 摘要提及“讨论评估的局限”，但未具体说明局限内容；该部分信息摘要未提供足够信息。
- 未提供方法在不同水体类型、极端浊度或非受控真实场景下的泛化验证细节；摘要未提供足够信息。
- 未提供十参数物理模型的具体参数含义、神经水体模型结构、训练设置与消融实验细节；摘要未提供足够信息。
- 未提供 SAJALA 与真实场景之间的域差距分析细节；摘要未提供足够信息。
- 未提供计算开销、内存占用及与基线在效率上的系统比较（除 44 FPS 外）；摘要未提供足够信息。

### 阅读优先级
**中**。理由：论文针对水下高斯泼溅中“指数透射率除法导致反演不稳定”的问题提出了明确的三路光学建模与可逆物理约束，并给出有界性与误差传播的理论论证，同时构建了带真值的路径追踪评测套件；对水下场景重建、物理引导神经渲染方向的研究者有直接参考价值。但摘要未展开关键实现细节、消融与跨域验证，且性能提升幅度（PSNR +0.42 dB）相对有限，需阅读全文后才能判断方法的稳健性与通用性。

</details>

<details>
<summary>Abstract</summary>

Water does not just tint an underwater photograph; it rewrites it. Each pixel mixes attenuated scene radiance, backscattered light, and scene light scattered forward on its way to the camera, and many combinations of scene and water explain the same pixels. Most Gaussian-splatting methods for underwater scenes model only the first two effects and remove the water by dividing by a transmission that decays exponentially with range, so their inversion gain grows without bound. We present NIRJALA (Sanskrit for "without water"), a 3D Gaussian Splatting framework that recovers water-free appearance and geometry together. TRIVENI, a three-path image formation model, adds a range-saturating forward-scattering term to direct transmission and backscatter; we prove that this keeps the inversion gain bounded at every range and bound how errors in the estimated backscatter and attenuation propagate into the recovered colours. PRATIBIMBA, a reversible physics anchor, ties a flexible neural water model to a ten-parameter physical model in both directions, so scene content cannot hide inside the water. SAMARASA collects the physics-informed objectives, including a range-binned colour prior. To score water removal against ground truth, we built SAJALA ("with water"), a 30-scene suite path-traced in Blender Cycles with water-free images, depth, and normals under controlled water colour and turbidity. On SAJALA, NIRJALA raises PSNR from 24.34 to 24.76 dB and lowers depth AbsRel from 0.109 to 0.091 against the strongest baseline; on real SeaThru-NeRF scenes it lowers LPIPS from 0.194 to 0.175 while rendering at 44 FPS. We also discuss where appearance metrics and geometry disagree underwater, and the limits of our evaluation.

</details>

#### 2026-11-17 - OCLDA-GS: Object-Centric Local Deformation-Aware Gaussian Streaming

**Authors:** Ashim Dahal, Nikesh Subedi, Rabab Abdelfattah, Nick Rahimi
**Links:** [abs](https://arxiv.org/abs/2611.23416) - [pdf](https://arxiv.org/pdf/2611.23416)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OCLDA-GS: Object-Centric Local Deformation-Aware Gaussian Streaming
- 作者：Ashim Dahal, Nikesh Subedi, Rabab Abdelfattah, Nick Rahimi
- 出版日期：2026-11-17T19:19:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.23416) | [PDF](https://arxiv.org/pdf/2611.23416)

### 一句话总结
提出一种以对象为中心的流式 3D 高斯框架，通过对象与运动感知的锚点重分配、对象内邻域限制及逐锚点局部形变校正，改善动态场景流式重建中的对象运动表达与边界一致性。

### 研究问题
现有时间与存储高效的流式 3DGS 方法依赖选择部分锚点高斯并进行邻域插值，但摘要指出这类方法可能忽略对象特定运动，并在对象边界附近引入不一致性。论文关注如何在流式重建中更好地处理大幅运动对象、精确对象边界以及小尺度局部形变。

### 核心思路/方法
OCLDA-GS 是一个以对象为中心的流式框架。其方法包括：
1. 动态重分配对象与运动感知的高斯锚点，为发生大幅运动的对象提供锚点高斯支持；
2. 将高斯邻域限制在对象组内，以获得更精确的对象边界；
3. 估计对象级刚性变换（摘要举例为手部运动），并利用这些估计学习逐锚点的局部形变校正，以处理小形变（摘要举例为衬衫褶皱）。

### 主要贡献
- 提出对象中心的流式 3DGS 框架 OCLDA-GS，针对对象特定运动与对象边界不一致问题进行设计。
- 引入对象与运动感知的锚点重分配机制，并限制对象组内的高斯邻域。
- 结合对象级刚性变换估计与逐锚点局部形变校正。
- 在三个动态多视角视频数据集上进行实验。摘要报告：在匹配细化预算下，相比 Instant Gaussian Stream (IGS)，PSNR 在 N3DV 提升 0.169 dB、Meeting Room 提升 0.202 dB、Google Immersive 提升 +0.199；细化时间步之间的平均 PSNR 下降在 N3DV 和 Meeting Room 分别降低 9.2% 和 13.8%。

### 局限性
摘要未提供足够信息说明方法的具体计算开销、存储需求、实时性、对对象分割或对象级刚性变换估计误差的敏感性，以及失败场景或消融实验细节。摘要未提供足够信息说明三个数据集的完整名称与实验设置细节。

### 阅读优先级
中。理由：该论文聚焦流式动态 3DGS 中对象运动与边界一致性问题，给出了明确的定量改进；但摘要仅提供有限实验信息，且发表于未来日期，是否值得优先精读需结合完整论文中的方法细节、效率分析和实验充分性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Streaming 3D Gaussian Splatting (3DGS) allows for online reconstruction of dynamic scenes from multi-view videos for Free Viewpoint Video (FVV). Current time and storage efficient methods rely on selecting a subset of anchor Gaussians and neighborhood interpolation for fast streamable 3DGS. However, these methods can overlook object-specific motion and introduce inconsistencies near object boundaries. We propose OCLDA-GS, an object-centric streaming framework that dynamically reallocates object and motion-aware Gaussian anchors to allocate anchor Gaussian support for objects undergoing large motion while at the same time, restricting the gaussian neighborhood within object groups for more precise object boundaries. Furthermore, it estimates object-wise rigid transformations (e.g. a hand moving) and leverages these estimates to learn per-anchor local deformation correction for small deformations (e.g. wrinkles on a shirt). Then, we conduct experiments on three dynamic multi-view video datasets and demonstrate improvements over the previous baselines alongside improved quality between refinement timesteps. Under matched refinement budgets, our method improves PSNR over Instant Gaussian Stream (IGS) by 0.169 dB on N3DV, 0.202 dB on Meeting Room and +0.199 on Google Immersive, while reducing the mean PSNR drop between refinement timesteps by 9.2% and 13.8% in N3DV and Meeting Room, respectively.

</details>

#### 2026-11-17 - ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting

**Authors:** Chuanzhi Xu, Boyu Wei, Chengkun Yue, Xuanhua Yin, Yiyang Li, Haodong Chen, Qiang Qu, Weidong Cai
**Links:** [abs](https://arxiv.org/abs/2611.23054) - [pdf](https://arxiv.org/pdf/2611.23054)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting
- 作者：Chuanzhi Xu, Boyu Wei, Chengkun Yue, Xuanhua Yin, Yiyang Li, Haodong Chen, Qiang Qu, Weidong Cai
- 出版日期：2026-11-17T16:47:43Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.23054) / [PDF](https://arxiv.org/pdf/2611.23054)

### 一句话总结
ReTouchGS 是面向预训练 3D Gaussian Splatting 模型的免参考美学色彩增强与参考引导色彩迁移框架，通过预测场景级 LUT 并结合轻量网络实现无需渲染的解析式颜色更新。

### 研究问题
现有 3DGS 色彩迁移与交互编辑方法依赖参考图像和用户指定颜色调整；而在许多应用中，用户只需要自动的美学色彩增强，使场景在视觉上更吸引人，同时保持跨视角的颜色与色调一致。摘要指出，如何对预训练 3DGS 模型进行免参考的美学色彩增强，并兼顾参考引导的色彩迁移，是本文关注的问题。

### 核心思路/方法
- 面向预训练 3DGS 模型，提出免参考美学色彩增强：从模型及其关联相机参数预测场景级颜色查找表（LUT）。
- 支持参考引导色彩迁移：使用同一场景的一个编辑视图及其对应原始渲染，拟合场景级 LUT。
- 使用共享的 blend-aware 色彩细化网络（仅 44.7K 参数）对解析式颜色更新进行细化，实现无需渲染的颜色映射。
- 方法保持几何不变，并可在数秒内输出标准 3DGS 资产。
- 设计 ReTouch3D 基准，用于评估跨视角的美学色彩增强与参考引导色彩迁移。

### 主要贡献
- 据摘要所述，提出首个面向预训练 3DGS 模型的免参考美学色彩增强框架。
- 提出场景级 LUT 预测与基于单编辑视图的参考引导 LUT 拟合路径，统一支持美学增强与参考引导迁移。
- 设计仅 44.7K 参数的共享 blend-aware 色彩细化网络，实现无需渲染的解析式颜色更新。
- 构建 ReTouch3D 基准以支持跨视角评估。
- 摘要称实验在美学色彩增强与参考引导色彩迁移上表现出高色彩准确度，并对未见场景具有较强泛化能力。

### 局限性
摘要未提供足够信息。摘要未给出具体失败情形、适用范围限制、计算开销细节或对不同 3DGS 变体的适用性分析；相关局限需以论文正文为准。

### 阅读优先级
中。理由：该工作聚焦 3DGS 的免参考美学色彩增强与轻量免渲染颜色更新，问题定位清晰，且提供基准与跨视角一致性诉求；但摘要未展开定量结果、对比基线细节与失败案例分析，是否值得优先精读取决于读者对 3DGS 颜色编辑、LUT 风格迁移或轻量后处理方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic scene reconstruction. Existing 3DGS color transfer and interactive editing methods are guided by reference images and user-specified color adjustments. However, in many applications, users simply want aesthetically guided color enhancement that automatically makes the scene more visually appealing while maintaining consistent colors and tones across viewpoints. We present ReTouchGS, to our knowledge the first framework for reference-free aesthetic color enhancement of pretrained 3DGS models. It predicts a scene-level color lookup table (LUT) from the model and its associated camera parameters. ReTouchGS also supports reference-guided color transfer by fitting a scene-level LUT using one edited view of the same scene and its corresponding original render. A shared blend-aware color refinement network with only 44.7K parameters refines an analytic color update to realize either color mapping without rendering. It preserves geometry and delivers standard 3DGS assets in seconds. We also design the ReTouch3D benchmark to support the evaluation of aesthetic color enhancement and reference-guided color transfer across viewpoints. Experiments demonstrate high color accuracy and strong generalization to unseen scenes in both aesthetic color enhancement and reference-guided color transfer.

</details>

#### 2026-11-17 - DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting

**Authors:** Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang
**Links:** [abs](https://arxiv.org/abs/2611.22805) - [pdf](https://arxiv.org/pdf/2611.22805)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting
- 作者：Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang
- 出版日期：2026-11-17T14:00:20Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.22805 ；PDF https://arxiv.org/pdf/2611.22805

### 一句话总结
DOOM-GS 是针对大规模动态 Gaussian Splatting 的首个外存（out-of-core）优化方法，通过面向时空图元的内存管理策略与面向海量图元的快速学习方法，在 GPU 显存不足时仍支持城市级动态场景重建。

### 研究问题
传统 Gaussian Splatting 采用 in-core 训练，假设 GPU 显存足以容纳全部图元；当图元数量超过显存容量（如大规模环境）时该假设失效。已有外存训练研究仅限静态场景，而动态 GS 图元在空间和时间上移动，破坏了现有外存研究的常见假设，在内存管理与训练上带来新挑战。摘要未提供足够信息说明具体破坏的假设细节与训练困难的具体形式。

### 核心思路/方法
- 提出 DOOM-GS，首个专门面向大规模动态 GS 的外存优化方法。
- 设计新的内存管理策略，针对时空图元优化缓存。
- 提出面向大量图元的快速学习方法。
- 由于缺乏合适的大规模动态 GS 数据集，构建并贡献了一个新数据集用于评估。
- 因无直接可比方法，适配若干密切 related 方法进行对比。
- 摘要未提供足够信息说明缓存策略的具体机制、快速学习方法的算法细节与实现方式。

### 主要贡献
- 首次将外存优化扩展到动态 Gaussian Splatting，填补静态外存研究未覆盖的动态场景空白。
- 提出面向时空图元的内存管理策略与面向海量图元的快速学习方法。
- 贡献一个用于大规模动态 GS 评估的新数据集（摘要未提供足够信息说明数据集规模、采集方式与场景类型）。
- 通过广泛评估验证有效性，宣称可在中等硬件上高质量重建城市级动态场景，为后续研究与应用提供基础工具。
- 摘要未提供足够信息说明具体定量指标、对比结果与消融实验结论。

### 局限性
- 摘要未提供足够信息说明方法的具体计算开销、内存换入换出代价与实时性表现。
- 摘要未提供足够信息说明对硬件配置的具体要求与“中等硬件”的界定。
- 摘要未提供足够信息说明新数据集的覆盖范围与多样性，以及适配对比方法的公平性细节。
- 摘要未提供足够信息说明方法在极端规模或高度动态场景下的失效条件。
- 摘要未提供足够信息说明代码、数据是否公开。

### 阅读优先级
中。理由：该论文针对大规模动态 GS 的显存瓶颈提出首个外存优化方案，并附带新数据集与对比评估，问题定位清晰、应用指向明确（城市级动态场景）；但摘要未给出定量结果、方法细节与开源信息，是否值得深入阅读需结合正文实验与实现细节进一步判断。

</details>

<details>
<summary>Abstract</summary>

Traditional Gaussian Splatting (GS) methods use in-core training, i.e. assuming that GPU memory is large enough to accommodate all the primitives. This assumption breaks down when the primitives exceed the capacity of GPU memory, e.g. GS on large environments. Recent out-of-core training research starts to address this issue, but is limited to static scenes. Unlike static GS, dynamic GS primitives move in space and time, breaking common assumptions held in existing out-of-core research and impose new challenges in memory management and training. To this end, we propose Dynamic Out-of-core Optimization for Massive Gaussian Splatting (DOOM-GS), the first out-of-core optimization method designed specifically for massive-scale dynamic GS. DOOM-GS is equipped with novel memory management strategies that optimize caching for spatio-temporal primitives, and a fast learning method for large numbers of primitives. Due to the lack of suitable datasets for large-scale dynamic GS, we also contribute a new dataset for evaluation. Since there are no directly comparable methods, we adapt several closely related methods for comparison. Through extensive evaluation, we demonstrate the effectiveness of DOOM-GS which now makes it possible to reconstruct city-scale dynamic scenes with high quality on moderate hardware, serving as a foundational tool for diverse future research and applications.

</details>

#### 2026-11-17 - Cross3DGS: Unified Vulkan-Based 3D Gaussian Splatting Training from Workstations to Mobile Devices

**Authors:** Hiroyuki Sato, Yusuke Takimoto
**Links:** [abs](https://arxiv.org/abs/2611.22240) - [pdf](https://arxiv.org/pdf/2611.22240)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cross3DGS: Unified Vulkan-Based 3D Gaussian Splatting Training from Workstations to Mobile Devices
- 作者：Hiroyuki Sato, Yusuke Takimoto
- 出版日期：2026-11-17T05:39:40Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2611.22240

### 一句话总结
提出基于 Vulkan 的跨厂商、跨平台 3D Gaussian Splatting 训练器 Cross3DGS，通过按设备选择执行调度，使同一套优化器在从工作站到手机的多类 GPU 上完成标准质量训练。

### 研究问题
现有 3DGS 训练通常依赖 CUDA 工作站；要在拍摄设备或其配套手机、笔记本上训练，仅移植 kernel 不够，因为 GPU 与驱动在并行特性、内存限制和命令提交上存在差异，这些差异决定训练调度能否正确执行并返回正确更新。如何在跨厂商、跨平台环境下保持同一优化器并正确执行训练，是论文关注的问题。

### 核心思路/方法
Cross3DGS 是一个跨厂商、跨平台的 Vulkan 训练器，保留一个优化器，并按设备分两步选择执行调度：先依据设备限制、工作负载规模和观察到的驱动失败，用规则排除已知不能正确运行的调度；再按固定偏好顺序从剩余可行调度中选择一个。论文以标准质量训练（30k 次更新、一百万个 Gaussian）为统一配置。

### 主要贡献
- 提出 Cross3DGS，一个基于 Vulkan 的跨厂商、跨平台 3DGS 训练器，采用单一优化器与按设备调度选择机制。
- 在摘要所述测量配置中，覆盖 NVIDIA、Intel、Arm、Qualcomm、AMD 和 Apple GPU，包括 Android 设备和 iPhone，均完成标准质量训练；而现有可移植训练器 VkSplat 和 Brush 在部分移动 GPU 上无法运行。
- 在工作站 11 个场景上平均，Cross3DGS 质量高于 VkSplat，训练时间无显著差异；Brush 在相近质量下训练时间约为其三倍。
- Cross3DGS 的最终质量在不同设备间几乎一致。
- 提供一个移动应用，可在设备上完成从手持采集到可查看模型的整个流程。

### 局限性
摘要未提供足够信息说明具体设备型号、完整实验设置、各平台训练时间数值、内存占用、功耗与热限制、规则覆盖范围及失败调度的具体类型；也未提供移动端训练规模、模型质量评价指标细节和与更多基线方法的比较。摘要未提供足够信息评估方法在未测量 GPU/驱动上的泛化能力。

### 阅读优先级
中。理由：论文主题涉及 3DGS 训练的跨厂商与移动端部署，若关注 Vulkan 可移植训练、端侧 3DGS 应用或跨 GPU 调度，具有较高相关性；但摘要仅给出方法框架和部分结果概述，缺少详细实验与实现信息，是否需要优先精读取决于对端侧训练和跨平台部署的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Scenes captured with handheld and wearable cameras are still shipped to a CUDA workstation for 3D Gaussian Splatting (3DGS) training. Training on the device that captured them, or on its companion phone or laptop, requires more than translating kernels: GPUs and drivers differ in parallel features, memory limits, and command submission, and these differences decide whether a training schedule executes and returns the correct update. We present Cross3DGS, a cross-vendor, cross-platform Vulkan trainer that keeps one optimizer and chooses its execution schedule per device in two steps: rules on device limits, workload size, and observed driver failures exclude the schedules known not to run correctly, and a fixed preference order selects one of the remaining feasible schedules. The same core completes standard-quality training (30k updates, one million Gaussians) on every configuration we measured, spanning NVIDIA, Intel, Arm, Qualcomm, AMD, and Apple GPUs and including Android devices and an iPhone, whereas the existing portable trainers VkSplat and Brush do not run on some of the mobile GPUs. Averaged over 11 scenes on a workstation, Cross3DGS has higher quality than VkSplat with no significant difference in training time, and Brush reports about three times the training time at comparable quality. The final quality of Cross3DGS is nearly identical across devices. A mobile application turns a handheld capture into a viewable model entirely on the device.

</details>

#### 2026-11-17 - CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure

**Authors:** Qi Shao, Zhihao Cao, Shuhao Zhai, Taoyu Wu, Zhuoxiao Li, Anh Nguyen, Long Hu, Xianzhi Li, Hong Liang, Baoru Huang, Liang Li
**Links:** [abs](https://arxiv.org/abs/2611.22235) - [pdf](https://arxiv.org/pdf/2611.22235)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure
- 作者：Qi Shao, Zhihao Cao, Shuhao Zhai, Taoyu Wu, Zhuoxiao Li, Anh Nguyen, Long Hu, Xianzhi Li, Hong Liang, Baoru Huang, Liang Li
- 出版日期：2026-11-17T05:37:15Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.22235) / [PDF](https://arxiv.org/pdf/2611.22235)

### 一句话总结
提出首个面向全景相机的多智能体高斯泼溅 SLAM 框架 CoSphere-SLAM，通过球面回环闭合与方向性全局优化应对任意朝向重叠、对称房间误回环、单目尺度漂移和短基线深度噪声问题。

### 研究问题
论文聚焦多智能体全景相机协作的密集建图与 SLAM，具体问题包括：
- 全景智能体可在任意 3D 朝向下观测到重叠场景，不同于仅能在相似朝向下共享视图的针孔智能体；但搜索全旋转会产生跨不同对称房间、彼此一致的虚假回环闭合。
- 连续单目尺度漂移会在重访表面处使刚性合并的地图发生分裂。
- 短基线下的深度噪声会扭曲回环的平移方向。

### 核心思路/方法
- **球面回环闭合**：在 $\mathrm{SO}(3)$ 上通过快速傅里叶相关对齐球面特征，以支持任意朝向；并通过全局 $\mathrm{Sim}(3)$ 共识拒绝对称虚假回环。
- **方向性全局优化**：基于回环构建逐关键帧 $\mathrm{Sim}(3)$ 位姿图，采用对数尺度正则化修正尺度漂移，并将光流平移方向与基于深度的平移幅值分离。
- **全向高斯融合**：利用每个高斯所属关键帧的相似度变换高斯，并在其最大射线响应处渲染高斯，以联合细化位姿与地图。

### 主要贡献
- 提出 CoSphere-SLAM，摘要称其为首个面向全景相机的多智能体高斯泼溅 SLAM 框架。
- 设计球面回环闭合机制，在 $\mathrm{SO}(3)$ 上通过快速傅里叶相关对齐球面特征，并利用全局 $\mathrm{Sim}(3)$ 共识拒绝对称虚假回环。
- 提出方向性全局优化，以逐关键帧 $\mathrm{Sim}(3)$ 位姿图和对数尺度正则化修正尺度漂移，并分离光流平移方向与深度平移幅值。
- 提出全向高斯融合，将高斯按关键帧相似度变换并在最大射线响应处渲染，以联合细化位姿和地图。
- 摘要称在室内与跨会话多智能体全景基准上，于单智能体和多智能体方法中取得 state-of-the-art 的轨迹精度与渲染质量。

### 局限性
- 具体实验数据集规模、基线方法清单、定量指标数值和消融实验细节：摘要未提供足够信息。
- 方法在极端尺度漂移、严重深度噪声或高度复杂对称环境下的失败模式与鲁棒性边界：摘要未提供足够信息。
- 计算开销、实时性、通信带宽和地图存储需求：摘要未提供足够信息。
- 对全景相机标定误差、不同全景传感器型号的敏感性：摘要未提供足够信息。
- 代码与数据是否公开、项目网站以外的复现细节：摘要未提供足够信息。

### 阅读优先级
**中**。理由：该论文面向多智能体全景高斯泼溅 SLAM，问题定义清晰，球面回环、$\mathrm{Sim}(3)$ 共识与方向性全局优化具有一定方法新意，且摘要声称取得 state-of-the-art 轨迹与渲染结果；但摘要未给出实验规模、基线、定量结果和失败案例分析，是否值得深入阅读需结合全文实验与可复现性进一步判断。若关注全景 SLAM、多智能体协作建图或高斯泼溅 SLAM，可优先查阅实验部分。

</details>

<details>
<summary>Abstract</summary>

Dense collaborative mapping is essential for search and rescue, building inspection, and warehouse automation, where panoramic cameras capture the entire surroundings in a single frame. Unlike pinhole agents that share views only at similar headings, panoramic agents observe overlapping scenes at any 3D orientation, yet searching full rotations also produces mutually consistent false loop closures across distinct symmetric rooms. Moreover, continuous monocular scale drift splits rigidly merged maps at revisited surfaces, while depth noise at short baselines distorts loop translation directions. To address these challenges, we propose CoSphere-SLAM, the first multi-agent Gaussian splatting SLAM framework for panoramic cameras, whose spherical loop closure aligns spherical features over $\mathrm{SO}(3)$ via fast Fourier correlation across arbitrary orientations and rejects symmetric false closures through global $\mathrm{Sim}(3)$ consensus. Building on these closures, directional global optimization solves a per-keyframe $\mathrm{Sim}(3)$ pose graph with log-scale regularization to correct scale drift while separating optical-flow translation directions from depth-based magnitudes. Finally, omnidirectional Gaussian fusion transforms each Gaussian with its keyframe similarity and renders Gaussians at their maximum ray response to jointly refine poses and maps. Experiments on indoor and cross-session multi-agent panoramic benchmarks demonstrate that CoSphere-SLAM achieves state-of-the-art trajectory accuracy and rendering quality among single-agent and multi-agent methods. Project website: https://cosphere-slam.github.io.

</details>

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-19 - SpatialScout-V2: Can VLM Agents Actively Explore Real-World 3D Scenes and Localize Objects?

**Authors:** Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Xu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li, Yunfang Wu
**Links:** [abs](https://arxiv.org/abs/2611.26177) - [pdf](https://arxiv.org/pdf/2611.26177)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization, simulation, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialScout-V2: Can VLM Agents Actively Explore Real-World 3D Scenes and Localize Objects?
- 作者：Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Xu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li, Yunfang Wu
- 出版日期：2026-11-19T14:28:18Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无副分类信息
- 链接：[摘要](https://arxiv.org/abs/2611.26177) / [PDF](https://arxiv.org/pdf/2611.26177)

### 一句话总结
论文提出 SpatialScout-V2，将主动建图任务从仿真扩展到真实住宅场景，构建包含 100 个家庭、3,171 个目标物体（29 类）的 Realsee3D 基准，并评估七个前沿视觉语言模型（VLM）在固定交互预算下主动选择视角、整合 RGB 观测并定位物体中心的能力，结果显示现有模型在真实场景中的定位精度与完整性仍面临显著挑战。

### 研究问题
摘要指出，空间智能要求智能体获取视觉证据，并将部分观测整合为连贯的三维表示。论文关注的问题是：VLM 智能体能否在真实世界 3D 场景中主动探索并定位物体；具体而言，在给定固定目标清单和固定交互预算的条件下，智能体能否自主选择已记录的视点与观察方向，整合校准后的 RGB 观测，并迭代估计与修正物体中心，从而构建准确且完整的物体中心地图。

### 核心思路/方法
根据摘要，SpatialScout-V2 在 SpatialScout 的主动建图任务基础上，引入三项推进：（1）真实视觉观测；（2）保留原始场景内容；（3）对已记录视角进行交互式探索。基准由 Realsee3D 中 100 个家庭构建，覆盖 29 类、3,171 个目标物体。任务设定为：给定固定目标清单，智能体在固定交互预算内自主选择已记录的视点和观察方向，整合校准后的 RGB 观测，并迭代估计与修正物体中心。评估指标包括平均 IoU、IoU 阈值命中率和目标覆盖率，用于衡量物体中心地图的定位精度与完整性。摘要还提到评估了七个前沿 VLM。

### 主要贡献
摘要明确给出的贡献包括：
1. 提出 SpatialScout-V2，将主动建图任务从仿真扩展到真实住宅场景，引入真实视觉观测、保留原始场景内容并支持对记录视角的交互式探索。
2. 基于 Realsee3D 的 100 个家庭构建基准，覆盖 29 类、共 3,171 个目标物体。
3. 在固定交互预算下评估七个前沿 VLM 的主动探索与物体中心定位能力，并采用平均 IoU、IoU 阈值命中率和目标覆盖率进行评估。
4. 实验发现六个模型的全目标平均 IoU 低于 20%，最佳模型 Claude Opus 5.5 仅达到 22.52%，超过 IoU 0.5 的目标仅占 18.36%；分析还表明，提交覆盖广可能与定位精度有限并存，目标遗漏会进一步降低总体得分。

### 局限性
摘要未提供足够信息说明方法的具体实现细节、基准构建流程、交互预算的具体数值、七個 VLM 的完整名单与逐模型结果、失败原因的系统分析，以及该基准在场景多样性、标注质量或任务泛化方面的限制。因此，无法仅依据摘要对这些方面作出判断。

### 阅读优先级
中。理由：该论文聚焦 VLM 智能体在真实 3D 场景中的主动探索与物体定位，问题设定清晰，且摘要给出了明确的基准规模与关键量化结果，对具身智能、3D 场景理解与 VLM 评测方向具有参考价值；但摘要未提供方法细节与完整实验分析，是否值得深入阅读需结合全文的方法创新程度与实验充分性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires agents to acquire visual evidence and integrate partial observations into coherent three-dimensional representations. We introduce SpatialScout-V2, which extends SpatialScout's active mapping task from simulation to real residential scenes through three advances: real visual observations, preservation of original scene content, and interactive exploration of recorded views. Built from 100 homes in Realsee3D, the benchmark covers 3,171 target objects across 29 categories. Given a fixed target inventory, agents autonomously select recorded viewpoints and viewing directions, integrate calibrated RGB observations, and iteratively estimate and revise object centers within a fixed interaction budget. We evaluate the localization accuracy and completeness of object-center maps using mean IoU, IoU-threshold hit rates, and target coverage. Evaluating seven frontier vision-language models (VLMs), we find that six achieve an all-target mean IoU below 20\%. Even the best-performing model, Claude Opus 5.5, reaches only 22.52\%, with just 18.36\% of targets exceeding an IoU of 0.5. Further analysis shows that broad submission coverage can coexist with limited localization accuracy, while target omissions further reduce overall scores. These results highlight substantial challenges in constructing accurate and complete object-center maps through active exploration of real scenes.

</details>

#### 2026-11-19 - Agentic Scaling of Embodied Tasks in Simulation for Synthetic Data Collection and Policy Evaluation

**Authors:** Kang Wang, Xiaolei Zhou, Xiaoyu Wu, Zhendong Wang
**Links:** [abs](https://arxiv.org/abs/2611.26046) - [pdf](https://arxiv.org/pdf/2611.26046)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Agentic Scaling of Embodied Tasks in Simulation for Synthetic Data Collection and Policy Evaluation
- 作者：Kang Wang, Xiaolei Zhou, Xiaoyu Wu, Zhendong Wang
- 出版日期：2026-11-19T12:55:12Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.26046 ；PDF https://arxiv.org/pdf/2611.26046

### 一句话总结
论文提出基于智能体的框架 AgenticTask，在仿真中按人类意图扩展现有具身任务集合，并用同一套任务表示支持任务构建与执行评估。

### 研究问题
扩展具身交互数据需要大量可用任务，但逐个指定并验证任务实例成本很高。论文关注如何在仿真中低成本地扩展任务集合，并同时支持任务执行与策略评估。

### 核心思路/方法
- 提出 AgenticTask 框架，用统一表示把交互需求与物体及部件绑定、场景与机器人配置、初始条件、完成标准关联起来。
- 任务生成智能体复用交互结构生成受支持的变体，并依据验证反馈修正不兼容配置。
- 任务执行智能体复用相同绑定与几何记录，选择机器人支持的技能，并按原始任务标准检查完成情况。
- 在 RoboCasa 上构建 AgenticTask 集合，并报告构建吞吐、物理检查通过率和执行完成情况。

### 主要贡献
- 提出以智能体为核心的任务集合扩展框架，强调人类意图下的任务变体生成与验证修正。
- 给出连接任务构建与执行的统一任务表示，使生成与评估共享绑定和几何信息。
- 在 RoboCasa 上构建 AgenticTask 集合：从 20,323 次构建尝试中保存 16,450 个任务实例，吞吐为每小时 166.97 个保存实例，62.26% 的构建尝试通过配置的物理检查。
- 执行智能体完成约 38% 的评估任务，成功案例覆盖物体放置、关节物体操作和顺序排列。
- 诊断分析指出构建可靠性、动作选择、任务—机器人兼容性和运行时集成是后续改进重点。

### 局限性
- 执行智能体仅完成约 38% 的评估任务，执行成功率有限。
- 构建尝试的物理检查通过率为 62.26%，构建可靠性仍有提升空间。
- 摘要仅给出诊断分析指出的改进方向，未提供各失败类型的具体分布与消融实验细节。
- 摘要未提供足够信息说明任务集合的规模上限、任务多样性度量、与基线方法的定量对比以及真实机器人迁移效果。
- 摘要未提供足够信息说明计算资源、运行时间成本构成和策略评估的具体协议。

### 阅读优先级
中。理由：论文聚焦具身任务合成数据采集与策略评估中的任务扩展问题，报告了较具体的构建吞吐、通过率和执行成功率，并明确指出失败与改进方向；但摘要未给出与基线方法的对比和更细的实验分析，适合关注仿真任务生成、智能体化数据采集与策略评估的研究者按需阅读。

</details>

<details>
<summary>Abstract</summary>

Scaling embodied interaction data requires a broad collection of usable tasks, yet specifying and validating each task instance remains costly. We present AgenticTask, an agent-based framework that expands existing task collections under human intent. Its central representation links interaction requirements to object and part bindings, scene and robot configurations, initial conditions, and completion criteria. A task-generation agent reuses interaction structure to construct supported variations and revises incompatible configurations using validation feedback. A task-execution agent uses the same bindings and geometric records to select robot-supported skills and check completion against the original task criteria. On RoboCasa, the framework builds the AgenticTask collection, saving 16,450 task instances from 20,323 construction attempts at a throughput of 166.97 saved instances per elapsed hour, with 62.26% of construction attempts passing the configured physical checks. The execution agent completes approximately 38% of evaluated tasks, with successful cases spanning object placement, articulated manipulation, and sequential arrangement. Diagnostic analysis identifies improvement priorities in construction reliability, action selection, task-robot compatibility, and runtime integration. Together, these results demonstrate task-collection expansion with measured construction productivity and concrete execution evidence, providing a foundation for subsequent interaction-data collection for embodied AI.

</details>

#### 2026-11-19 - Driver Gaze Target Identification via Gaze Estimation and Structured Driving Scene Understanding

**Authors:** Xinze Cao, Ke Wang, Deyong Guan, Yuanquan Li, Ke Zhang
**Links:** [abs](https://arxiv.org/abs/2611.25771) - [pdf](https://arxiv.org/pdf/2611.25771)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** driving scene, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Driver Gaze Target Identification via Gaze Estimation and Structured Driving Scene Understanding
- 作者：Xinze Cao, Ke Wang, Deyong Guan, Yuanquan Li, Ke Zhang
- 出版日期：2026-11-19T09:09:04Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次要分类信息
- 链接：[摘要](https://arxiv.org/abs/2611.25771)｜[PDF](https://arxiv.org/pdf/2611.25771)

### 一句话总结
论文提出一个由四部分组成的模块化框架，从车内驾驶员图像与前方道路图像中识别对象级或区域级的注视目标，并在实验室实验和 LBW 数据集上报告了 Top-1 识别精度。

### 研究问题
驾驶员注视区域分类和连续注意力定位所能提供的信息有限，无法说明被注视场景目标的身份；论文旨在解决从同步的车内驾驶员图像与前方视角道路图像中识别对象级或区域级注视目标的问题。

### 核心思路/方法
框架包含四个组件：
1. **MFGaze**：结合以掩码自编码器（MAE）预训练的 Vision Transformer，并通过特征级线性调制（FiLM）引入头部姿态条件。
2. **全景场景理解**：构建结构化的候选集。
3. **多项式岭回归**：通过个体化校准将注视特征映射到二维场景图像坐标。
4. **熵驱动目标推断**：自适应融合边界距离几何与类别级语义先验。
实验评估使用三个公开注视数据集、一项使用 Cityscapes 道路场景与自采集注视数据的实验室测试，以及 Look Both Ways（LBW）数据集。

### 主要贡献
- 提出面向驾驶员注视目标识别的模块化框架，输出对象级或区域级目标，而非仅注视区域或连续坐标。
- 设计 MFGaze，将 MAE 预训练的 ViT 与 FiLM 头部姿态条件结合。
- 将全景场景理解、个体化校准的多项式岭回归与熵驱动目标推断整合为完整流程。
- 摘要报告：完整框架在实验室实验中总体 Top-1 注视目标识别精度为 96.27%；经序列特定校准后，在 LBW 上任务相关对象 Top-1 精度为 79.92%，道路类别为 85.58%。
- MFGaze 在 MPIIFaceGaze、ETH-XGaze、Gaze360 上的平均角度误差分别为 4.06°、4.23°、10.52°，摘要称其为对比方法中最低，并表现出较强的跨数据集泛化能力；敏感性分析显示超参数扰动下性能稳定。

### 局限性
摘要未提供足够信息说明以下方面：框架在真实车载部署条件下的性能、计算开销与实时性、失败案例、候选集构建错误的影响、不同驾驶员或场景分布下的泛化边界，以及与更多基线方法的完整比较细节。摘要仅报告了实验室实验与 LBW 上的部分 Top-1 精度，未提供其他数据集上的端到端目标识别结果。

### 阅读优先级
**中**。理由：论文聚焦驾驶员注视目标识别这一明确任务，方法模块化且摘要给出了多数据集评估与量化结果；但摘要未提供足够信息判断其实际部署可行性、计算成本与局限，适合作为该方向的候选文献进一步阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Identifying a driver's gaze target provides object-level information for visual attention monitoring in intelligent vehicles. Gaze-zone classification and continuous attention localization provide limited information about the identity of the attended scene target. This paper proposes a modular framework that identifies object- or region-level gaze targets from synchronized in-cabin driver images and forward-view road images. The framework comprises four components: MFGaze, which combines a Vision Transformer pretrained with a masked autoencoder (MAE) and head-pose conditioning through feature-wise linear modulation (FiLM); panoptic scene understanding, which constructs a structured candidate set; polynomial ridge regression, which maps gaze features to 2D scene-image coordinates through individualized calibration; and entropy-driven target inference, which adaptively fuses boundary-distance geometry with class-level semantic priors. Experiments evaluate the framework using three public gaze datasets, a laboratory test using Cityscapes road scenes and self-collected gaze data, and the Look Both Ways (LBW) dataset. The complete framework achieves an overall Top-1 gaze target identification accuracy of 96.27% in the laboratory experiment. After sequence-specific calibration, it achieves Top-1 accuracies of 79.92% for task-relevant objects and 85.58% for the road class on LBW. MFGaze achieves the lowest mean angular errors among the compared methods, with 4.06$^\circ$, 4.23$^\circ$, and 10.52$^\circ$ on MPIIFaceGaze, ETH-XGaze, and Gaze360, respectively, and demonstrates strong cross-dataset generalization. Sensitivity analyses show stable performance under hyperparameter perturbations. These results support the framework as a source of object-level gaze information for driver monitoring.

</details>

#### 2026-11-19 - PAD: Policy-Aware Data Valuation for Autonomous Driving

**Authors:** Chengkai Xu, Yicheng Guo, Jiaqi Liu, Yiming Cui, Shiyu Fang, Peng Hang, Hao Zhang, Jian Sun
**Links:** [abs](https://arxiv.org/abs/2611.25604) - [pdf](https://arxiv.org/pdf/2611.25604)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PAD: Policy-Aware Data Valuation for Autonomous Driving
- 作者：Chengkai Xu, Yicheng Guo, Jiaqi Liu, Yiming Cui, Shiyu Fang, Peng Hang, Hao Zhang, Jian Sun
- 出版日期：2026-11-19T06:53:22Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2611.25604)｜[PDF](https://arxiv.org/pdf/2611.25604)

### 一句话总结
论文提出面向目标驾驶策略的“策略感知数据估值”框架 PAD，为每条候选演示分配与其对下游策略效用相关的价值，并用策略特定筛选替代不加区分的数据累积。

### 研究问题
端到端自动驾驶依赖扩大训练演示规模，但数据增长并不保证策略按比例提升；同一条演示对某个规划器可能有益，对另一个规划器可能冗余甚至有害。现有数据筛选方法通常从样本内在属性或训练相关代理指标推断数据价值，未直接衡量下游策略效用。论文要解决的问题是：如何按目标驾驶策略评估候选演示的效用，并据此进行数据筛选。

### 核心思路/方法
PAD 为每个候选演示分配一个针对目标驾驶策略的效用值。其方法组合了场景级校准反馈、投影后的策略梯度，以及对局部训练几何的正则化近似，从而产生可扩展的、基于影响（influence-based）的策略相关数值。论文还通过受控的整组移除研究检验这些数值的方向保真性，并通过跨规划器分析考察同一候选池在不同规划器家族下是否产生显著不同的排序。

### 主要贡献
- 提出 PAD 框架，将数据估值从样本内在属性或训练代理指标转向目标驾驶策略的下游效用。
- 给出结合场景级校准反馈、投影策略梯度与局部训练几何正则化近似的可扩展影响估值方法。
- 通过受控整组移除研究验证估值的方向保真性；通过跨规划器分析表明同一候选池在不同规划器家族下会诱导明显不同的数据排序。
- 在 DiffusionDrive 上，PAD 相比仅使用真实数据训练，在 NavTest 上提升 EPDMS 3.5 点，在 NavHard 上提升 5.0 点。
- 在基于扩散、回归和流匹配的规划器上，策略特定筛选一致优于仅真实数据训练和全池训练，同时显著减少场景级性能回退。

### 局限性
摘要未提供足够信息说明计算开销、候选池规模、估值稳定性边界、跨数据集泛化能力以及除 EPDMS 与场景级回退外的其他评价指标表现。摘要也未提供足够信息说明整组移除研究的具体设计、基线细节和统计显著性。

### 阅读优先级
高。理由：该论文直接针对自动驾驶数据扩展中“数据更多不一定策略更好”的关键问题，提出策略感知的数据估值与筛选方法，并在多种规划器家族上报告一致收益和场景级回退减少；对端到端自动驾驶的数据策展与高效扩展具有较强相关性。但摘要未给出方法实现与实验细节，精读时可重点核查估值可扩展性、基线公平性与跨规划器结论的稳健性。

</details>

<details>
<summary>Abstract</summary>

End-to-end autonomous driving increasingly depends on scaling training demonstrations, yet data growth does not guarantee proportional gains. However, additional data do not guarantee better policies: a demonstration that benefits one planner may be redundant or harmful to another. Existing curation methods typically infer data value from intrinsic sample properties or training-dependent proxies that do not measure downstream policy utility. To address this, we introduce \textbf{Policy-Aware Data Valuation (PAD)}, a framework that assigns each candidate demonstration a utility specific to the target driving policy. PAD combines scene-level calibration feedback with projected policy gradients and a regularized approximation of local training geometry, producing scalable influence-based values for the policy. A controlled group-removal study establishes the directional fidelity of these values, while cross-planner analysis shows that the same candidate pool induces markedly different rankings across planner families. On DiffusionDrive, PAD improves EPDMS over real-only training by $3.5$ points on NavTest and $5.0$ points on NavHard. Policy-specific curation consistently outperforms real-only and full-pool training across diffusion-, regression-, and flow-matching-based planners while substantially reducing scene-level regressions. These results establish policy-aware data valuation as a basis for replacing indiscriminate data accumulation with targeted policy improvement, enabling more efficient and reliable scaling of autonomous-driving systems.

</details>

#### 2026-11-19 - TuringPAI: A Foundation for On-Device Physical AI

**Authors:** Qiman Wu, Hanlin Chen, Yuhua Wei, Mingyuan Wang, Shaman Tang, Minghao Li, Rui Xin, Xingye Liu, Zhichao Yang, Yiqi Yu, Hongyan Pei, Xiaowen Tian, YingYing Liu, Shiwen Liu, Jiahui Hu, Yizhao Wang, Yuheng Zhang, Anhua Liu, Yue He, Shuang Su, Da Zhu, Hua Zhou, Pengfei Diao, Haojie Yang, Weichao Huang, Hang Zhang, Honggou Yang, Xianming Liu
**Links:** [abs](https://arxiv.org/abs/2611.25474) - [pdf](https://arxiv.org/pdf/2611.25474)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TuringPAI: A Foundation for On-Device Physical AI
- 作者：Qiman Wu, Hanlin Chen, Yuhua Wei, Mingyuan Wang, Shaman Tang, Minghao Li, Rui Xin, Xingye Liu, Zhichao Yang, Yiqi Yu, Hongyan Pei, Xiaowen Tian, YingYing Liu, Shiwen Liu, Jiahui Hu, Yizhao Wang, Yuheng Zhang, Anhua Liu, Yue He, Shuang Su, Da Zhu, Hua Zhou, Pengfei Diao, Haojie Yang, Weichao Huang, Hang Zhang, Honggou Yang, Xianming Liu
- 出版日期：2026-11-19T04:01:34Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.25474) / [PDF](https://arxiv.org/pdf/2611.25474)

### 一句话总结
TuringPAI 提出一套面向端侧物理 AI 的模型家族，以共享视觉-语言基础模型 TuringPAI-VL 为初始化，分别派生自动驾驶模型 TuringPAI-Drive 与机器人操作模型 TuringPAI-Embodied，并在车载算力约束下报告了感知、轨迹生成与操作成功率方面的结果。

### 研究问题
论文关注在有限车载算力条件下，物理 AI 模型需要理解空间关系与动态环境，并将观测转化为动作。具体而言，需要解决如何构建一个既能进行通用视觉-语言理解、又能为自动驾驶和机器人操作等下游视觉-语言-动作任务提供共享初始化的端侧基础模型。

### 核心思路/方法
- 提出 TuringPAI 模型家族，包括 TuringPAI-VL（共享视觉-语言理解）、TuringPAI-Drive（自动驾驶）和 TuringPAI-Embodied（机器人操作）。
- TuringPAI-VL 为 0.65B 模型，基于 HybridViT-MLQ 构建，将卷积局部聚合与 Transformer 全局建模相结合。
- 使用 Multi-scale Latent Queries（MLQ）在同一视觉 Transformer 内整合空间特征与观测历史，为语言模型提供紧凑、结构化的接口。
- 训练结合通用视觉-语言数据与几何、跨视角、时序监督。
- TuringPAI-VL 为两个下游 VLA 模型提供共享初始化；TuringPAI-Drive 使用 MLQ 接口；TuringPAI-Embodied 面向机器人操作。

### 主要贡献
- 提出面向端侧物理 AI 的 TuringPAI 模型家族，覆盖视觉-语言理解、自动驾驶与机器人操作三类任务。
- TuringPAI-VL 在支持通用多模态理解的同时，在定量几何感知上相较 Qwen2-VL-2B 有所提升，并为两个下游 VLA 模型提供共享初始化。
- 在自动驾驶方面，TuringPAI-Drive 使用 MLQ 接口时，所有评估的 ADE/FDE 指标与全 token HybridViT 基线相差在 1.2% 以内，并在内部仿真评估中取得可比的总分；在单颗 NVIDIA Orin-X SoC 上使用 XPeng Native Runtime（XNRT）时，车载运行可 12 Hz 生成轨迹。
- 在机器人操作方面，TuringPAI-Embodied 在四个 LIBERO 套件上平均成功率达到 96.8%。
- 结果表明，在实际端侧约束下，驾驶与机器人操作可以共享视觉-语言基础。

### 局限性
- 摘要未提供足够信息说明模型参数量之外的规模细节、训练数据规模与具体数据组成。
- 摘要未提供足够信息说明 TuringPAI-Drive 的实车路测结果；仅提到车载运行轨迹生成频率与内部仿真评估。
- 摘要未提供足够信息说明 LIBERO 四个套件的具体任务设置、评估协议与统计方差。
- 摘要未提供足够信息说明与更多外部基线在驾驶与机器人操作任务上的全面对比。
- 摘要未提供足够信息说明失败案例、鲁棒性边界与端侧部署的功耗/延迟全貌。

### 阅读优先级
中。理由：论文提出面向端侧物理 AI 的统一模型家族，并给出自动驾驶轨迹生成频率、ADE/FDE 相对基线差距与 LIBERO 成功率等具体结果，对具身智能与端侧部署方向有参考价值；但摘要未提供训练数据规模、实车验证细节与更全面的基线对比，需阅读全文才能判断方法通用性与实验严谨性。

</details>

<details>
<summary>Abstract</summary>

Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute. We present TuringPAI, a family of models for on-device Physical AI comprising TuringPAI-VL for shared vision-language understanding, TuringPAI-Drive for autonomous driving, and TuringPAI-Embodied for robotic manipulation. TuringPAI-VL is a 0.65B model built on HybridViT-MLQ, which combines convolutional local aggregation with Transformer-based global modeling. Multi-scale Latent Queries integrate spatial features and observation history within the same visual Transformer, providing a compact, structured interface to the language model. Training combines general vision-language data with geometric, cross-view, and temporal supervision. TuringPAI-VL supports general multimodal understanding and improves quantitative geometric perception over Qwen2-VL-2B, while providing a shared initialization for the two downstream VLA models. For autonomous driving, TuringPAI-Drive maintains all evaluated ADE/FDE metrics within 1.2\% of a full-token HybridViT baseline using the MLQ interface and achieves comparable aggregate scores in an in-house simulation evaluation. Using XPeng Native Runtime (XNRT) on a single NVIDIA Orin-X SoC, TuringPAI-Drive generates trajectories at 12\,Hz in on-vehicle operation. For robotic manipulation, TuringPAI-Embodied achieves a 96.8\% average success rate across the four LIBERO suites. These results demonstrate a shared vision-language foundation for driving and robotic manipulation under practical on-device constraints.

</details>

#### 2026-11-19 - A Unified Framework for Image Manipulation Localization Under Multi-Type Weak Supervision

**Authors:** Songlin Li, Hui Ma, Zhiqing Guo, Dan Ma, Gaobo Yang, Xin Liao
**Links:** [abs](https://arxiv.org/abs/2611.25371) - [pdf](https://arxiv.org/pdf/2611.25371)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Unified Framework for Image Manipulation Localization Under Multi-Type Weak Supervision
- 作者：Songlin Li, Hui Ma, Zhiqing Guo, Dan Ma, Gaobo Yang, Xin Liao
- 出版日期：2026-11-19T02:08:21Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.25371) / [PDF](https://arxiv.org/pdf/2611.25371)

### 一句话总结
论文提出 UniIML 师生框架，将多种弱标注映射为统一表示以引导 SAM 生成候选掩码，并通过 Ordinal Safe Consensus（OSC）筛选与排序候选、构建软伪标签和像素级监督权重，从而在单一模型中统一利用多类型弱监督进行图像篡改定位。

### 研究问题
现有弱监督图像篡改定位（IML）方法通常依赖针对特定标注类型的训练策略，导致不同标注难以在单一模型中联合使用，限制了可用训练数据的规模，并制约进一步进展。论文旨在解决多类型弱标注下的统一训练与定位问题。

### 核心思路/方法
- 提出 UniIML 师生框架，将多样弱标注映射为统一表示，用于引导 Segment Anything Model（SAM）生成多个候选掩码。
- 指出 SAM 面向通用分割，对篡改痕迹敏感度有限，仅依赖其预测质量分数难以可靠选出最佳候选。
- 引入 Ordinal Safe Consensus（OSC）：先利用统一表示中可信弱标注约束过滤候选；再分别按与弱标注的一致性、SAM 预测质量分数、跨视图稳定性对剩余候选排序并聚合，形成初始选择。
- OSC 通过逐一省略某一评价准则重复排序与选择，以评估评价标准变化对候选选择的影响；将被最频繁选中的候选作为最终掩码，并用其相对选择频率量化选择稳定性。
- 基于所选候选的预测概率构建软伪标签，并依据选择稳定性、候选间像素级一致性和预测确定性估计像素级监督权重。
- 学生模型在弱标注定义区域接受直接监督，在其他区域通过可靠性加权蒸馏从软伪标签学习，实现跨弱标注类型的统一训练。

### 主要贡献
- 提出 UniIML 师生框架，将多种弱标注映射为统一表示，以支持单一模型联合使用多类型弱监督。
- 提出 Ordinal Safe Consensus（OSC），结合弱标注约束、SAM 质量分数与跨视图稳定性进行候选筛选、排序与稳定性量化。
- 基于选择稳定性、候选一致性和预测确定性构建软伪标签与像素级监督权重，实现可靠性加权蒸馏。
- 摘要称实验表明 UniIML 相比当前先进 IML 方法取得更优的平均性能。

### 局限性
- 摘要未提供足够信息说明具体数据集、实验设置、消融实验细节及各类弱标注下的分项性能。
- 摘要未提供足够信息说明计算开销、对 SAM 的依赖程度及失败案例分析。
- 摘要未提供足够信息说明方法在真实场景或跨域条件下的泛化表现。

### 阅读优先级
中。理由：论文聚焦多类型弱监督下的统一图像篡改定位框架，问题定义和方法组合（统一表示、SAM 候选生成、OSC 共识选择、软伪标签蒸馏）较清晰；但摘要未给出实验细节与分项结果，且分类标注为 Embodied / Robotics / AR Applications，与 IML 主题的归类关系需进一步核实。若关注弱监督定位或 SAM 适配应用，可优先阅读；若仅需结论性性能对比，则摘要信息不足。

</details>

<details>
<summary>Abstract</summary>

Existing weakly supervised image manipulation localization (IML) methods typically rely on annotation-specific training strategies, hindering the joint use of diverse annotations within a single model. This limits the scale of usable training data and constrains further progress. We propose UniIML, a teacher-student framework that maps diverse weak annotations into a unified representation to guide the Segment Anything Model (SAM) in generating multiple candidate masks. However, SAM is designed for general-purpose segmentation and has limited sensitivity to manipulation traces; its predicted quality scores alone may therefore fail to reliably identify the candidate that best delineates the manipulated region. We introduce Ordinal Safe Consensus (OSC), which first filters candidates using trusted weak-annotation constraints encoded in the unified representation. It then ranks the remaining candidates separately by consistency with weak annotations, SAM-predicted quality scores, and cross-view stability, aggregating these rankings for an initial selection. To assess how changes in the evaluation criteria affect candidate selection, OSC repeats ranking and selection while omitting one criterion at a time. The most frequently selected candidate is adopted as the final mask, and its relative selection frequency quantifies selection stability. We construct soft pseudo-labels from the selected candidate's predicted probabilities and estimate pixel-level supervision weights based on selection stability, pixel-level agreement among candidates, and predictive certainty. The student receives direct supervision in regions defined by weak annotations and learns from soft pseudo-labels elsewhere through reliability-weighted distillation, enabling unified training across weak annotation types. Experiments show that UniIML achieves superior average performance compared with state-of-the-art IML methods.

</details>

#### 2026-11-18 - Accord: Universal Online Metric Localization and Dense Mapping from one Camera and an IMU

**Authors:** Jaafar Mahmoud, Arthur Movsesyan, Cuong Huynh, Mikhail Iumanov, Sergey Zagoruyko, Sergey Kolyubin
**Links:** [abs](https://arxiv.org/abs/2611.25279) - [pdf](https://arxiv.org/pdf/2611.25279)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth prediction, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Accord: Universal Online Metric Localization and Dense Mapping from one Camera and an IMU
- 作者：Jaafar Mahmoud, Arthur Movsesyan, Cuong Huynh, Mikhail Iumanov, Sergey Zagoruyko, Sergey Kolyubin
- 出版日期：2026-11-18T23:16:39Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次分类信息
- 链接：摘要页 https://arxiv.org/abs/2611.25279 ；PDF https://arxiv.org/pdf/2611.25279

### 一句话总结
Accord 提出一种从单相机加 IMU 在线构建稠密度量地图的方法，通过 VIO 提供度量位姿与锚点、深度基础模型预测关键帧窗口深度，并利用多视角双向稠密深度一致性校正单图尺度误差，最终以因子图融合子图。

### 研究问题
从单相机和 IMU 构建稠密度量地图具有挑战性：视觉惯性里程计（VIO）能提供度量运动但几何稀疏，前馈深度模型能预测稠密结构但不能保证度量尺度。论文旨在解决如何在保持度量尺度的前提下，在线获得准确的稠密度量地图。

### 核心思路/方法
- 使用 VIO 滤波器发布度量位姿。
- 以这些位姿为条件，深度基础模型对短关键帧窗口预测深度。
- 将每个关键帧窗口锚定到由滤波器位姿三角化得到的度量 3D 点。
- 利用共视图像之间的双向稠密深度一致性（即多视角一致性 Accord）估计并校正每张图像的尺度误差，同时保留锚点建立的度量尺度。
- 引入上下文关键帧以改进深度预测。
- 将得到的子图在因子图中融合。

### 主要贡献
- 提出 Accord，从任意相机加 IMU 在线构建稠密度量地图，核心是多视角一致性约束下的尺度校正。
- 在五个公开相机-IMU 配置和一个新的 Phone-rig/GoPro 数据集上评估单一建图配置；无需按数据集或配置调参，且每张地图仅用 Accord 自身轨迹对齐，在每个平台上取得 5 cm 平均 F-score 的最佳或次佳结果。
- 开源方法及 Phone-rig 数据集，以惠及研究社区。

### 局限性
摘要未提供足够信息（例如计算开销、实时性指标、失败场景、对 VIO 质量的敏感性等均未在摘要中说明）。

### 阅读优先级
高。理由：该工作直接针对单相机加 IMU 的在线稠密度量建图这一机器人/AR 关键问题，强调无需按数据集调参的通用配置，并提供开源代码与数据集；若关注视觉惯性 SLAM、稠密建图或深度基础模型与几何一致性融合，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Dense metric mapping from a single camera and IMU remains challenging: visual-inertial odometry (VIO) provides metric motion but sparse geometry, whereas feed-forward depth models predict dense structure without ensuring metric scale. We present Accord, which constructs an accurate online dense metric map from any camera with an IMU. A VIO filter publishes metric poses, a depth foundation model conditioned on them predicts depth for short keyframe windows, and a factor graph fuses the resulting submaps. Recent work has explored several approaches to this problem. What is essential is the multi-view agreement (Accord), which is considered in SLAM as a source of geometric self-consistency. Accord anchors each keyframe window to metric 3D points triangulated from the filter poses, then exploits bidirectional dense depth agreement between co-visible images to estimate and correct per-image scale errors while preserving the metric scale established by the anchors. Context keyframes further improve depth prediction, and the resulting submaps are fused in a factor graph. We evaluate a single mapping configuration across five public camera-IMU setups and a new Phone-rig/GoPro dataset. With nothing tuned per dataset/setup and every map aligned only by Accord's own trajectory, Accord achieves consistently best/second-best mean F-score at 5 cm on every platform. Accord is open-source along with the phone-rig dataset for the benefit of the research community

</details>

#### 2026-11-18 - Mapping the Wind to Find the Source: Online Physics-Informed Gas Source Localization with Mobile Robots

**Authors:** Wanting Jin, Thomas Wiedemann, Han Fan, Achim Lilienthal, Alcherio Martinoli
**Links:** [abs](https://arxiv.org/abs/2611.25067) - [pdf](https://arxiv.org/pdf/2611.25067)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mapping the Wind to Find the Source: Online Physics-Informed Gas Source Localization with Mobile Robots
- 作者：Wanting Jin, Thomas Wiedemann, Han Fan, Achim Lilienthal, Alcherio Martinoli
- 出版日期：2026-11-18T19:11:06Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.25067 ；PDF https://arxiv.org/pdf/2611.25067

### 一句话总结
论文提出一种轻量级、物理信息驱动的概率框架，使移动机器人在空间变化的室内气流中在线重建风场，并据此推断气体源位置、规划信息性路径以加快定位。

### 研究问题
移动机器人气体源定位（GSL）面临风速与气体测量在空间上稀疏、带噪声、且可能受机器人运动影响的问题；室内气流随空间显著变化，而详细环境布局、边界条件或预先计算的风场往往不可用；同时危险源要求尽快定位，穷举式探索不现实。论文聚焦于在此类条件下如何高效、稳健地实现气体源定位。

### 核心思路/方法
- 机器人在导航过程中持续采集风与气体测量，并在线重建空间变化的气流场。
- 估计出的风场驱动一个前向扩散模型，对每个候选源位置预测气体分布模式。
- 将预测的气体模式与实测气体模式比较，以更新源位置的概率信念。
- 由于风场是增量重建的，框架还考虑风场估计在空间上的非均匀可靠性及其对源估计的影响。
- 得到的信念图用于信息性路径规划，引导机器人前往信息量更高的区域。

### 主要贡献
- 提出一种轻量级、物理信息驱动的概率框架，用于空间变化室内气流下的高效 GSL。
- 在线重建空间变化风场，并将其与候选源的气体扩散预测耦合，形成源位置概率信念更新。
- 明确考虑风场估计的空间非均匀可靠性对源估计的影响。
- 将信念图与信息性路径规划结合，以引导机器人高效探索。
- 摘要称通过高保真仿真对各个组件及其完整系统集成进行综合评估，并通过真实室内实验评估系统在真实传感、运动与气流条件下的性能；结果显示引入轻量物理知识显著提升空间复杂气流下的定位稳健性并实现更高效探索。

### 局限性
- 摘要未提供足够信息说明方法在更大规模、更多源或动态源场景下的适用性。
- 摘要未提供足够信息说明在线风场重建所需测量量、时间开销或计算资源的具体限制。
- 摘要未提供足够信息给出仿真与真实实验的定量指标、成功率、定位误差或对比基线细节。
- 摘要未提供足够信息说明对传感器配置、机器人运动模式或室内气流条件的依赖程度与失效边界。
- 摘要未提供足够信息说明“轻量级”的具体定义及与非物理方法的计算成本对比。

### 阅读优先级
高。理由：该论文面向危险源快速定位这一高时效任务，问题定义清晰，方法将在线风场重建、物理扩散预测、概率信念更新与信息性路径规划整合为完整系统，且摘要明确包含仿真与真实室内实验评估；对移动机器人气体源定位、物理信息驱动感知与主动探索方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Gas Source Localization (GSL) with mobile robots is challenging because wind and gas measurements are spatially sparse, noisy, and potentially affected by robot motion. Indoor airflow can vary substantially across space, while detailed environmental layouts, boundary conditions, or precomputed airflow fields are often unavailable. Moreover, hazardous sources must be localized as quickly as possible, making exhaustive exploration impractical. This paper presents a lightweight physics-informed probabilistic framework for efficient GSL under spatially varying indoor airflow. As the robot navigates, it continuously collects wind and gas measurements and reconstructs the spatially varying airflow field online. The estimated wind field drives a forward dispersion model that predicts the gas pattern for each candidate source location. These predictions are compared with the measured gas pattern to update a probabilistic belief over the source location. As the wind field is reconstructed incrementally, the framework also accounts for the spatially non-uniform reliability of wind field estimation and its influence on the source estimation. The resulting belief map is then used for informative path planning to guide the robot toward informative regions. High-fidelity simulations provide a comprehensive evaluation of the individual components and their integrations within the complete system, while physical indoor experiments assess the system performance under realistic sensing, motion, and airflow conditions. The results demonstrate that incorporating lightweight physical knowledge significantly improves localization robustness under spatially complex airflow and enables more efficient exploration.

</details>

#### 2026-11-18 - $Z$-sight: Unifying Vision-Language-Action and Latent World Modeling

**Authors:** Junjie Ye, Yiqi Zhao, Muchen Xu, Celina Shiyu Wang, Hao Dong, Ruohai Ge, Rong Xue, Benjamin J Kolligs, Aditya Dutt, Sasanka Nagavalli, Nassim A. Samad, Gaurav S. Sukhatme, Jyotirmoy V. Deshmukh, Yue Wang, Yuliang Guo
**Links:** [abs](https://arxiv.org/abs/2611.24940) - [pdf](https://arxiv.org/pdf/2611.24940)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：$Z$-sight: Unifying Vision-Language-Action and Latent World Modeling
- 作者：Junjie Ye, Yiqi Zhao, Muchen Xu, Celina Shiyu Wang, Hao Dong, Ruohai Ge, Rong Xue, Benjamin J Kolligs, Aditya Dutt, Sasanka Nagavalli, Nassim A. Samad, Gaurav S. Sukhatme, Jyotirmoy V. Deshmukh, Yue Wang, Yuliang Guo
- 出版日期：2026-11-18T18:59:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.24940) / [PDF](https://arxiv.org/pdf/2611.24940)

### 一句话总结
$Z$-sight 是一个统一视觉-语言-动作（VLA）与生成式潜在世界建模的机器人基础模型，直接在 VLM 的视觉 token 空间中预测未来，并与动作联合去噪，从而避免视频生成和外部编码器的高昂成本。

### 研究问题
论文针对现有世界动作模型（WAMs）依赖视频生成器、计算成本高，而近期潜在空间策略虽避免像素生成，却通过特征对齐或冻结目标编码器将未来预测与 VLM 原生特征空间解耦的问题，提出如何在不进行像素重建、不依赖外部编码器的前提下，将未来预测与动作生成统一在 VLM 自身的视觉 token 空间中。

### 核心思路/方法
$Z$-sight 在 VLM 感知当前观测的同一视觉 token 空间中直接预测未来。模型以 mixture-of-transformers 结构将前瞻专家（foresight expert）和连续动作专家与 VLM 耦合，推理时联合去噪未来空间 token 与动作，无需像素重建或外部编码器。训练数据包括人类视频和机器人轨迹。

### 主要贡献
- 提出统一 VLA 与生成式潜在世界建模的机器人基础模型 $Z$-sight。
- 在 VLM 原生视觉 token 空间中进行未来预测，避免视频生成器开销及与外部编码器的解耦。
- 通过 mixture-of-transformers 联合去噪未来空间 token 与动作。
- 摘要报告：SIMPLE 上成功率 81.9%（较最强基线 +9.6 点），六个 Unitree G1 任务平均 73.3%（+20.0 点），每 chunk 耗时 110 ms，并在桌面基准上保持竞争力。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、泛化边界、训练数据规模与多样性细节、消融实验、安全性或实机部署限制等。

### 阅读优先级
高。理由：该工作直接针对 VLA 与世界模型耦合中的成本与特征空间解耦问题，提出无需像素重建和外部编码器的统一方案，并给出明确的成功率提升与推理时延数据，对具身智能与机器人基础模型方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically align intermediate features or rely on frozen target encoders, decoupling future prediction from the VLM's native feature space. $Z$-sight instead predicts the future directly in the visual token space in which its VLM perceives the present. Coupling a foresight expert and a continuous action expert with the VLM in a mixture-of-transformers, $Z$-sight jointly denoises future spatial tokens and actions at inference without pixel reconstruction or external encoders. Trained on human video and robot trajectories, $Z$-sight achieves 81.9% success on SIMPLE (+9.6 points over the strongest baseline) and 73.3% across six Unitree G1 tasks (+20.0 points) at 110 ms per chunk, while remaining competitive on tabletop benchmarks.

</details>

#### 2026-11-18 - Render the Robot, Generate the World: One Video World Model Across Embodiments

**Authors:** Yash Jangir, Karan Mirakhor, Renos Zabounidis, Muhammad Zubair Irshad, Sergey Zakharov, Yonatan Bisk, Homanga Bharadhwaj
**Links:** [abs](https://arxiv.org/abs/2611.24925) - [pdf](https://arxiv.org/pdf/2611.24925)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Render the Robot, Generate the World: One Video World Model Across Embodiments
- 作者：Yash Jangir, Karan Mirakhor, Renos Zabounidis, Muhammad Zubair Irshad, Sergey Zakharov, Yonatan Bisk, Homanga Bharadhwaj
- 出版日期：2026-11-18T18:52:28Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.24925 ；PDF https://arxiv.org/pdf/2611.24925 ；项目页 https://doppelwm.github.io/

### 一句话总结
论文提出 Doppel，一种以“相机对齐的未来身体构型渲染”与数值动作轨迹为条件的、跨具身的视频世界模型，让模型从显式给定预期运动中解放出来，专注于预测物体运动与环境交互变化。

### 研究问题
预测智能体动作后果需要同时建模身体运动与环境响应。现有视频世界模型多从数值动作中同时学习二者，但摘要指出几何与运动学已能指定预期运动；如何避免模型重复学习身体运动、并让不同具身与动作空间共享同一视觉接口，是论文关注的问题。此外，训练机器人数据常缺少相机外参，如何对齐渲染轨迹与记录观测也是需要处理的问题。

### 核心思路/方法
- 提出 Doppel：以相机对齐的未来身体构型渲染为条件，并结合数值动作轨迹，构建具身无关的视频世界模型。
- 通过显式提供预期运动，使模型可聚焦于预测物体运动与交互驱动的环境变化。
- 利用渲染运动作为跨不同具身和动作空间的共同视觉接口。
- 针对无相机外参的机器人数据集，恢复相机位姿并将渲染轨迹与记录观测对齐。
- 联合训练一个共享视频骨干与条件适配器，覆盖八个数据集、八种机器人与人类具身，约 600 小时视频，且不使用具身标签。

### 主要贡献
- 提出以渲染未来身体构型为条件的具身无关视频世界模型 Doppel。
- 给出跨具身共享视觉接口的设计，并联合训练共享视频骨干与条件适配器。
- 在三个机械臂数据集上，Doppel 在留出轨迹上相比仅动作基线提升 PSNR 1.00 dB，在分布外评估下提升 1.20 dB，并预测更一致的物体运动。
- 在全部八种具身上训练（Doppel-8）相比三个机器人模型（Doppel-3），在六个评估集中的四个上提升了机器人预测表现。
- 摘要提到为无相机外参的机器人数据恢复相机位姿并对齐渲染轨迹。

### 局限性
- 摘要仅给出 PSNR 与部分评估集对比，未提供完整实验设置、基线细节、失败案例或计算成本。
- 摘要未说明方法在真实机器人闭环控制中的表现。
- 摘要未提供模型规模、训练资源、推理速度等信息。
- 摘要未提供跨具身泛化的系统消融或负结果分析。
- 以上未提及内容均属于“摘要未提供足够信息”。

### 阅读优先级
中。理由：论文主题与具身智能、视频世界模型和跨具身学习直接相关，且给出了明确的定量提升与多具身训练设置，具备参考价值；但摘要篇幅有限，实验细节、局限与真实部署表现未充分展开，是否精读需结合对“渲染条件视频世界模型”方向的兴趣再判断。

</details>

<details>
<summary>Abstract</summary>

Predicting the consequences of an agent's actions requires modeling both the body's motion and the environment's response. Most video world models attempt to learn both from numerical actions, even though geometry and kinematics already specify the intended motion. We introduce Doppel, an embodiment-agnostic video world model conditioned on camera-aligned renderings of future body configurations and numerical action trajectories. By explicitly providing the intended motion, Doppel can focus on predicting object motion and interaction-driven changes in the environment. Rendered motion also provides a common visual interface across different embodiments and action spaces. To train on robot datasets without camera extrinsics, we recover camera poses and align rendered trajectories with recorded observations. We jointly train a single shared video backbone and conditioning adapter on eight datasets spanning eight robot and human embodiments, from single- and bimanual robot arms to a dexterous humanoid and human hands and bodies, using about 600 hours of video without embodiment labels. Across three robot-arm datasets, Doppel improves PSNR over action-only baselines by 1.00 dB on held-out trajectories and 1.20 dB under out-of-distribution evaluation, while predicting more consistent object motion. Training on all eight embodiments (Doppel-8) improves robot predictions over the three-robot model (Doppel-3) on four of six evaluation sets. Project page: https://doppelwm.github.io/.

</details>

#### 2026-11-18 - Improving Zero-shot 3D Semantic Mapping in Offroad with Geometric Priors

**Authors:** Eerik Alamikkotervo, Risto Ojala
**Links:** [abs](https://arxiv.org/abs/2611.24696) - [pdf](https://arxiv.org/pdf/2611.24696)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D mapping, robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Improving Zero-shot 3D Semantic Mapping in Offroad with Geometric Priors
- 作者：Eerik Alamikkotervo, Risto Ojala
- 出版日期：2026-11-18T16:23:05Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.24696) / [PDF](https://arxiv.org/pdf/2611.24696)

### 一句话总结
该论文提出为每个语义类别拟合球度-高程分布作为几何先验，并将其与视觉基础模型的预测融合，以改善越野非结构化环境中的零样本 3D 语义建图。

### 研究问题
摘要指出，当前的视觉基础模型能在结构化场景中较准确地完成零样本语义预测，但在自然（越野）环境中性能会受损。另一方面，3D 点云在视觉基础模型失效的场景中包含有助于区分语义的信息。论文关注的问题是：如何利用点云中的几何信息来弥补视觉基础模型在越野环境零样本 3D 语义建图中的不足。

### 核心思路/方法
论文为每个语义类别拟合一个“球度-高程”分布，作为几何锚点。在拟合过程中，只使用视觉基础模型预测置信度最高的点，以得到高质量的几何先验分布。随后，将该几何先验与视觉基础模型的预测融合，生成最终的语义建图结果。

### 主要贡献
- 提出以球度-高程分布作为每个语义类别的几何先验，并将其用于零样本 3D 语义建图。
- 采用“仅保留视觉基础模型高置信预测点”的策略来拟合几何先验分布。
- 将几何先验与视觉基础模型预测融合，形成最终语义建图。
- 在 RELLIS-3D 数据集上，相比 SAM3 基线，mIoU 提升 +6.3、准确率提升 +8.9；在 WildScenes 数据集上，mIoU 提升 +1.7、准确率提升 +2.1。

### 局限性
摘要未提供足够信息。摘要未说明方法对视觉基础模型置信度阈值的敏感性、几何先验在其他数据集或传感器配置下的泛化能力、计算开销，也未提供失败案例分析；此外，论文提到源代码将在录用后公开，当前的可复现性状态在摘要中未进一步说明。

### 阅读优先级
中。理由：该工作面向越野环境下零样本 3D 语义建图这一具体问题，方法思路清晰，且有明确的量化提升；但摘要未提供实验设置细节、消融分析或泛化性验证信息，是否值得深入阅读需结合对越野机器人语义建图或几何先验融合方向的兴趣进一步判断。

</details>

<details>
<summary>Abstract</summary>

Semantic 3D mapping is a powerful representation that enables platform agnostic mobile robot navigation in challenging offroad conditions. Current vision foundation models can accurately predict semantics zero-shot on structured scenes but performance is compromised in natural environments. On the other hand, 3D point clouds encode valuable information for discriminating semantics in scenarios where vision foundation models fail. In this work, we propose fitting a sphericity-elevation distribution for each semantic class to act as geometric anchor. Only the points with the most confident vision foundation model predictions are considered when fitting to produce high quality geometric prior distributions. The geometric prior is fused with the vision foundation model prediction to produce the final semantic mapping. The proposed prior improves SAM3 baseline by +6.3 in mIoU and +8.9 in accuracy on the RELLIS-3D dataset, and by +1.7 in mIoU and +2.1 in accuracy on the WildScenes dataset. The source code will be made public upon paper acceptance.

</details>

#### 2026-11-18 - ShoWorld: Shape-Faithful Multi-Hypothesis Occupancy World Model

**Authors:** Zhiqiang Yan, Guangfa Wang, Yuan Wu, Jian Yang, Gim Hee Lee
**Links:** [abs](https://arxiv.org/abs/2611.24457) - [pdf](https://arxiv.org/pdf/2611.24457)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ShoWorld: Shape-Faithful Multi-Hypothesis Occupancy World Model
- 作者：Zhiqiang Yan, Guangfa Wang, Yuan Wu, Jian Yang, Gim Hee Lee
- 出版日期：2026-11-18T14:02:31Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.24457) / [PDF](https://arxiv.org/pdf/2611.24457)

### 一句话总结
ShoWorld 通过将运动预测与形状表示解耦，用多假设轨迹建模运动不确定性、用子体素点表示保持物体形状，从而提升占用世界模型对未来运动物体的预测质量。

### 研究问题
论文针对占用世界模型在预测运动物体时的两个问题：
1. **运动不确定性**：单一轨迹可能把多个合理未来平均成一条不合理的路径。
2. **形状失真**：即使运动预测正确，反复体素化也会侵蚀或膨胀物体形状。

### 核心思路/方法
ShoWorld 将运动与形状分开建模：
- **运动预测器**：以场景布局、邻近智能体和未来自车轨迹为条件，预测概率化轨迹；每个假设被渲染为占用，并按概率融合，以保留多种未来可能性。
- **形状组件**：从局部几何预测带占用概率和偏移量的子体素点；这些点随物体刚性运动，体素占用由“至少一个占用点落入该体素”的概率决定，以减少运动中的形状失真。
- 摘要提到在 Occ3D-nuScenes 上取得 state-of-the-art，并给出在真值占用与自车轨迹条件下 mIoU/IoU 及动态类别上的提升数值。

### 主要贡献
- 提出运动与形状分离表示的占用世界模型 ShoWorld。
- 用概率化多假设轨迹缓解单一轨迹平均化导致的未来不合理问题。
- 用子体素点及占用概率建模物体形状，降低运动过程中的形状失真。
- 在 Occ3D-nuScenes 上报告 state-of-the-art 结果，并给出整体与动态类别的 mIoU/IoU 提升。

### 局限性
摘要未提供足够信息。摘要未说明模型的计算开销、实时性、对传感器输入的具体依赖、失败场景、消融实验细节，也未说明在无真值占用与自车轨迹条件下的性能表现。

### 阅读优先级
**中**。理由：论文聚焦占用世界模型中运动不确定性与形状失真两个明确问题，方法思路清晰，并报告了 Occ3D-nuScenes 上的定量提升；但摘要未提供足够信息判断其泛化性、效率与实际部署价值，适合关注占用预测或世界模型的读者进一步阅读全文验证。

</details>

<details>
<summary>Abstract</summary>

Occupancy world models struggle to forecast moving objects due to motion uncertainty and shape distortion. A single trajectory can average plausible futures into an implausible path, and repeated re-voxelization can erode or inflate object shape even under correct motion. We introduce ShoWorld to address these challenges through separate motion and shape representations. The motion forecaster predicts probabilistic trajectories conditioned on scene layout, nearby agents and the future ego trajectory. Each hypothesis is rendered into occupancy and fused according to its probability to retain alternative futures. The shape component predicts sub-voxel points with occupancy probabilities and offsets from local geometry. These points move rigidly with the object, and voxel occupancy follows the probability that at least one occupied point falls within it. This representation reduces shape distortion under motion. ShoWorld achieves state-of-the-art results on Occ3D-nuScenes. With ground-truth occupancy and ego trajectory, it improves mIoU and IoU by 6.56 and 9.16 points overall and by 6.06 and 5.53 points on dynamic classes.

</details>

#### 2026-11-18 - StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model

**Authors:** Chuang Wang, Rui Nie, Jie Song, Junyuan Gao, Jiahe Song, Haitao Zhou, Boyu Zhu, Xing Li, Jiang Wu, Conghui He, Qian Yu, Weijia Li
**Links:** [abs](https://arxiv.org/abs/2611.24408) - [pdf](https://arxiv.org/pdf/2611.24408)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model
- 作者：Chuang Wang, Rui Nie, Jie Song, Junyuan Gao, Jiahe Song, Haitao Zhou, Boyu Zhu, Xing Li, Jiang Wu, Conghui He, Qian Yu, Weijia Li
- 出版日期：2026-11-18T13:37:51Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.24408 ，PDF 链接 https://arxiv.org/pdf/2611.24408

### 一句话总结
论文提出 StrideWorld 基准，用“先于被评测运动固定”的参考来评估交互式视频世界模型的场景刚性与动作一致性，以避免现有基准中参考吸收场景形变和节奏变化的问题。

### 研究问题
交互式视频世界模型需要根据用户命令探索生成场景，这要求相机移动时场景保持 3D 结构，并且每个动作保持稳定效果。现有基准大多使用与被测视频相拟合的参考，例如从视频自身帧重建的场景，或与命令路径对齐但尺度自由的相机轨迹；这类参考可能吸收逐渐发生的场景形变以及节奏和路线长度变化，使相关错误未被检测到。

### 核心思路/方法
StrideWorld 的参考在它们所评判的运动之前就已固定。具体而言：
- 场景刚性依据起始视图的真值几何来评估；
- 动作一致性依据每个动作的“stride”来评估，即一条命令对应的相机运动；
- stride 在模型最初几步上测量，再用于检验后续步骤，因此每个模型只与自己的步长比较；
- 测量方法在具有已知相机运动的渲染视频上进行了验证，并且评分与人类判断一致。

### 主要贡献
- 提出 StrideWorld 基准，针对交互式视频世界模型评估场景刚性与动作一致性，并采用先于被评判运动固定的参考。
- 设计基于起始视图真值几何的场景刚性评估，以及基于每个动作 stride 的动作一致性评估。
- 在已知相机运动的渲染视频上验证测量，并报告评分与人类判断一致。
- 在来自 140 个起始视图、由若干开放模型生成的视频上进行评测，报告场景形变、单动作节奏、组合路线中的停滞与终点偏差等现象，并公开代码、数据和排行榜。

### 局限性
- 摘要未提供足够信息说明基准所覆盖的具体任务类型、场景类别和数据规模细节。
- 摘要未提供足够信息说明“人类判断一致”的具体评估协议、样本量和一致性指标。
- 摘要未提供足够信息说明除摘要所述模型外的泛化能力，以及基准对闭源模型或真实视频的适用性。
- 摘要未提供足够信息说明微调实验的完整设置与适用范围，仅提到在两个模型上用少量渲染片段微调可消除多数中途停滞。

### 阅读优先级
中。理由：该论文聚焦交互式视频世界模型的评测基准，问题定义清晰，且涉及场景刚性与动作一致性这两个对具身、机器人和 AR 应用重要的维度；但摘要未提供足够实验细节和完整方法描述，若研究兴趣不在视频世界模型评测或具身交互生成，优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action to keep a stable effect. Existing benchmarks mostly evaluate these properties against references fitted to the video under test, either a scene reconstructed from its own frames or a camera trajectory aligned to the command path with a free scale. Such references can absorb gradual scene deformation and changes in pace and route length, so these errors can pass undetected. We therefore introduce StrideWorld, a benchmark whose references are fixed before the motion they judge. It evaluates scene rigidity against the ground-truth geometry of the start view, and action consistency against the stride of each action, the camera motion of one command. The stride is measured on the model's first steps and then used to test the steps that follow, so each model is judged only against its own steps. Its measurements are validated on rendered videos with known camera motion, and its scores agree with human judgments. Across \nvideos{} videos generated by \nmodels{} open models from $140$ start views, all models but one deform their scenes as the camera moves, with offsets up to $7.3$ times those of a rigid rendering along the same camera path. Most models keep a steady pace when a single action is held. Along composed routes, several models often stall, and most completed routes end away from the positions predicted by each model's own strides. Only the two models that scale commands by the estimated scene depth bring most routes close to these positions. Fine-tuning two models on a few rendered clips removes most of their mid-route stalls. Code, data, and a leaderboard are publicly available at https://github.com/chuangwang123/strideworld.

</details>

#### 2026-11-18 - ProbeShare: Probing a Few, Sharing Across Many for Fast World-Model Planning

**Authors:** Zejian Kang, Xiantao Lin, Zekai Chen, Boyang Shen, Mingyu Ma, Shengwen Zheng, Chengtai Guo, Xiangru Huang
**Links:** [abs](https://arxiv.org/abs/2611.24229) - [pdf](https://arxiv.org/pdf/2611.24229)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ProbeShare: Probing a Few, Sharing Across Many for Fast World-Model Planning
- 作者：Zejian Kang, Xiantao Lin, Zekai Chen, Boyang Shen, Mingyu Ma, Shengwen Zheng, Chengtai Guo, Xiangru Huang
- 出版日期：2026-11-18T11:05:38Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2611.24229) / [PDF](https://arxiv.org/pdf/2611.24229)

### 一句话总结
ProbeShare 利用同一规划步内候选动作共享观测历史与动作到特征映射的观察，用少量代表性探针重建大量候选的特征网格，从而加速基于冻结联合嵌入世界模型的视觉规划。

### 研究问题
论文关注使用冻结联合嵌入世界模型进行视觉规划时的计算冗余问题：标准 CEM 规划器会将每个候选动作序列独立通过十亿参数预测器进行推演，即使邻近动作引起的场景变化相似。这种冗余计算随候选种群规模和搜索轮数增长，拖慢闭环重规划。论文要解决的是：如何在保持候选评估与规划效果的同时，减少大量候选独立推演带来的计算开销。

### 核心思路/方法
- 关键观察：在一个规划步内，候选动作共享同一观测历史，因此也共享一个共同的动作到特征映射。
- 方法核心：ProbeShare 用少量代表性探针测量局部响应，并通过场景条件化、几何感知的加权方式重建每个候选的特征网格。
- 动态补充探针：当有希望的候选移动到已有探针覆盖范围之外时，ProbeShare 会评估一个新的探针，以重新为附近候选打分。
- 应用场景：面向机器人到达与物体操作等任务，在图像目标条件下评估候选动作序列，然后执行。

### 主要贡献
- 识别并利用规划步内候选之间共享动作到特征映射的结构性冗余。
- 提出 ProbeShare，通过少量探针加场景条件化、几何感知加权重建候选特征网格，减少逐候选独立推演。
- 设计探针覆盖不足时的补充评估机制，用于对附近候选重新打分。
- 摘要报告在四个 RoboCasa 任务上，相比密集 RoboJEPA 实现 43.8–128.9 倍加速，相比竞争基线至少 14.2 倍加速；在匹配时间比较中取得更高的平均目标进展。

### 局限性
- 摘要未提供足够信息说明方法在不同世界模型架构或非 RoboCasa 任务上的泛化性。
- 摘要未提供足够信息说明探针数量、覆盖策略和几何感知加权的具体实现细节及其敏感性。
- 摘要未提供足够信息说明加速效果与规划成功率之间的完整权衡，仅报告了匹配时间下的平均目标进展。
- 摘要未提供足够信息说明失败案例、安全性或真实机器人部署情况。

### 阅读优先级
高。理由：该论文直接针对世界模型规划中候选独立推演的计算瓶颈，问题定义清晰，方法思路具有结构性优化特征，且摘要给出了明确的加速倍数与任务级效果；对世界模型规划、机器人操作和闭环重规划效率相关方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Visual planning with a frozen joint-embedding world model supports robotic reaching and object manipulation by evaluating candidate action sequences against an image goal before execution. Standard cross-entropy method (CEM) planners roll out every candidate independently through a billion-parameter predictor, even when nearby actions induce similar scene changes. This redundant computation grows with population size and search rounds, slowing closed-loop replanning. We observe that candidates within a planning step share an observation history and thus a common action-to-feature map. Based on this insight, we propose ProbeShare, which measures local responses with a few representative probes and reconstructs each candidate's feature grid through scene-conditioned, geometry-aware weighting. When promising candidates move beyond existing probe coverage, ProbeShare evaluates a new probe to rescore nearby candidates. Across four RoboCasa tasks, ProbeShare accelerates episode planning by 43.8--128.9 times over dense RoboJEPA and at least $14.2\times$ over competitive baselines, with greater mean goal progress in a matched-time comparison.

</details>

#### 2026-11-18 - LaST1.0: A Unified Latent World-Action Model with Control-Centric SpatioTemporal Reasoning

**Authors:** Hao Chen, Xuheng Zhang, Zhuangzhe Wu, Jiaming Liu, Shaobo Zhang, Jialin Gao, Zhonghao Yan, Di Wu, Sixiang Chen, Peng Jia, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng
**Links:** [abs](https://arxiv.org/abs/2611.23974) - [pdf](https://arxiv.org/pdf/2611.23974)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LaST1.0: A Unified Latent World-Action Model with Control-Centric SpatioTemporal Reasoning
- 作者：Hao Chen, Xuheng Zhang, Zhuangzhe Wu, Jiaming Liu, Shaobo Zhang, Jialin Gao, Zhonghao Yan, Di Wu, Sixiang Chen, Peng Jia, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng
- 出版日期：2026-11-18T07:13:27Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.23974 ；PDF https://arxiv.org/pdf/2611.23974

### 一句话总结
LaST1.0 将机器人操作中的世界建模重构为潜空间中的“以控制为中心的未来预测”，并通过统一潜 World-Action 模型与 LaST-Attention 提升精细操作的成功率与泛化能力。

### 研究问题
论文关注 World-Action Models 中“面向重建”的未来视频建模方式：这类方法会把大量模型容量分配给与控制无关的外观细节。作者要解决的问题是，如何把世界建模从“观测完整的视频未来”转向更贴近控制需求的未来预测，从而更好地支撑机器人操作的鲁棒控制与精细操作。

### 核心思路/方法
- 将操作任务中的世界建模重新表述为潜空间中的以控制为中心的未来预测。
- 不预测观测完整的视频未来，而是预测由未来腕部视角导出的紧凑、几何感知的潜目标，把监督重点放在机器人—物体交互的演化上。
- 重新审视统一架构的视觉输入接口与注意力机制：
  - 采用无视觉编码器设计，配合轻量 patch embedder，将细粒度视觉线索直接暴露给骨干网络。
  - 提出 LaST-Attention，用于跨模态的结构化时空交互。

### 主要贡献
- 提出 LaST1.0，一个统一的潜 World-Action 模型，将世界建模重构为以控制为中心的潜空间未来预测。
- 设计基于未来腕部视角的紧凑、几何感知潜目标，使监督聚焦于精细操作所需的机器人—物体交互。
- 采用无视觉编码器加轻量 patch embedder 的视觉输入接口，并引入 LaST-Attention 以支持跨模态结构化时空交互。
- 摘要称在两种机器人 embodiment、五个挑战性操作任务和三个仿真基准（RLBench、LIBERO、LIBERO-Plus）上取得 state-of-the-art 成功率，并能泛化到新场景；具体实验数值与消融细节摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法在真实机器人平台上的表现；实验描述集中在仿真基准与任务评估。
- 摘要未提供足够信息说明计算开销、推理延迟、模型规模或训练成本。
- 摘要未提供足够信息说明失败案例、对腕部视角质量的依赖程度以及跨 embodiment 的详细迁移机制。
- 摘要未提供足够信息给出具体指标数值、对比基线清单与消融实验结果。

### 阅读优先级
高。理由：该论文直接针对 World-Action Models 中“重建导向”与“控制导向”之间的核心权衡，提出潜空间世界建模与结构化时空注意力机制，且摘要声称在多个机器人操作基准上取得 state-of-the-art；对具身智能、机器人操作与世界模型方向具有较强相关性。但需注意，当前判断仅基于摘要与元数据，具体实验强度与可复现性需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

World-Action Models couple action learning with future prediction, enabling robotic policies to capture environmental dynamics for robust control. However, prevailing methods take a reconstruction-oriented approach to model future videos, allocating substantial capacity to appearance details that are incidental to control. In this work, we reformulate world modeling for manipulation as control-centric future prediction in latent space, and present LaST1.0, a unified latent World-Action Model. Rather than modeling an observation-complete video future, LaST1.0 predicts compact, geometry-aware latent targets derived from future wrist views, focusing the supervision on the evolving robot-object interactions required for fine-grained manipulation. To better support this control-centric paradigm, LaST1.0 revisits the visual input interface and attention mechanism of its unified architecture. It adopts a vision-encoder-free design with a lightweight patch embedder, exposing fine-grained visual cues directly to the backbone, and introduces LaST-Attention for structured spatiotemporal interactions across modalities. Evaluations across two robot embodiments, five challenging manipulation tasks, and three simulation benchmarks---RLBench, LIBERO, and LIBERO-Plus---demonstrate that LaST1.0 achieves state-of-the-art success rates and generalizes to novel scenarios. These results demonstrate the effectiveness of control-centric latent world modeling for robust manipulation.

</details>

#### 2026-11-18 - GTI: Grounding Task Intent Throughout Long-Horizon VLA Manipulation

**Authors:** Tianqi Gong, Haochen Niu, Yusheng Zhao, Lantao Zhang, Haoyu Liu, Rendong Ying, Peilin Liu
**Links:** [abs](https://arxiv.org/abs/2611.23926) - [pdf](https://arxiv.org/pdf/2611.23926)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GTI: Grounding Task Intent Throughout Long-Horizon VLA Manipulation
- 作者：Tianqi Gong, Haochen Niu, Yusheng Zhao, Lantao Zhang, Haoyu Liu, Rendong Ying, Peilin Liu
- 出版日期：2026-11-18T06:17:14Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.23926 ；PDF https://arxiv.org/pdf/2611.23926

### 一句话总结
GTI 通过在当前观测与执行历史中定位活动子任务及其执行阶段，并用阶段相关的视觉目标与局部语言指令共同条件化 VLA，以在长时序机器人操作中持续保持全局任务意图。

### 研究问题
VLA 模型能够根据视觉观测、语言和机器人状态生成局部动作，但长时序操作要求全局任务意图始终与当前可执行上下文保持一致。论文关注的问题是：如何在多阶段长时序执行中持续定位当前活动子任务及其执行阶段，使模型不仅知道“现在做什么”，也知道“当前阶段应达到什么状态”，并在执行发生持续偏差时恢复意图一致的执行上下文。

### 核心思路/方法
GTI（Grounding Task Intent）使用当前观测和执行历史来定位当前活动子任务及其执行阶段。对于同一个局部子任务，GTI 生成两种依赖阶段的视觉目标：交互/接触状态和局部完成状态。局部语言指令与相应的阶段特定视觉目标共同条件化 VLA，从而同时指定当前要执行的动作以及当前阶段应达到的状态。执行过程中，GTI 通过异常监控和局部恢复机制，在出现持续偏差后通过回滚、重新观测和阶段重新评估来重建与意图一致的执行上下文。

### 主要贡献
- 提出 GTI，将任务意图定位到当前活动子任务及其执行阶段，而不是仅依赖局部动作生成。
- 为同一局部子任务引入阶段相关的两类视觉目标（交互/接触状态与局部完成状态），并与局部语言指令联合条件化 VLA。
- 引入异常监控与局部恢复流程，通过回滚、重新观测和阶段重新评估支持部署时的持续偏差恢复。
- 在 RoboCasa365、VLA-Arena Horizon-Long 和真实 PiPER 任务上进行评估。摘要报告：在已见复合 RoboCasa365 任务上，GR00T 相对匹配的 Global-FT 基线在 ID/OOD 下成功率从 14.6%/12.1% 提升至 31.8%/20.4%；在 VLA-Arena 上，GTI+π_{0.5} 总体成功率为 47.6%，对比适配的 ForeAct 基线 45.2%，在更难的 L1/L2 任务上分别提升 5.2/6.0 个百分点；在三个真实机器人任务实验中，平均全任务成功率从 21.7% 提升至 59.2%。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体实现细节、计算开销、失败案例、异常监控阈值设定、恢复机制的触发条件细节，也未提供超出上述评估范围的外部验证或更全面的消融结果。

### 阅读优先级
高。理由：该论文直接针对长时序 VLA 操作中的任务意图保持与阶段定位问题，且摘要给出了多个基准和真实机器人任务上的定量提升；对于关注具身智能、机器人长时序操作和 VLA 执行鲁棒性的读者具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models generate local actions from visual observations, language, and robot state, but long-horizon manipulation requires the global task intent to remain grounded in the currently executable context. We propose GTI (Grounding Task Intent), which uses the current observation and execution history to localize the active subtask and its execution phase. For the same local subtask, GTI generates two phase-dependent visual targets: an interaction/contact state and a local completion state. The local language instruction and the corresponding phase-specific visual target jointly condition the VLA, specifying both what to do now and what state should be reached at the current phase. During execution, anomaly monitoring and local recovery re-establish an intent-consistent execution context through rollback, re-observation, and phase re-evaluation after persistent deviation. We evaluate GTI on RoboCasa365, VLA-Arena Horizon-Long, and real-world PiPER tasks. Relative to matched Global-FT baselines, GR00T success on seen composite RoboCasa365 tasks increases from 14.6%/12.1% to 31.8%/20.4% under ID/OOD evaluation. On VLA-Arena, GTI+$π_{0.5}$ reaches 47.6% overall success versus 45.2% for an adapted ForeAct baseline, with gains of 5.2/6.0 percentage points on the harder L1/L2 tasks. In the three real-robot task experiments, mean full-task success increases from 21.7% to 59.2%. The results indicate that persistent semantic intent localization and phase-conditioned visual grounding improve multi-stage execution, while failure-triggered local recovery provides additional deployment-time support.

</details>

#### 2026-11-17 - Code World Model 2.0: Towards Infinite Controllable Video Generation

**Authors:** Ruoyu Wang, Hao Zhong, Yanming Yang, Jiahao Tian, Lin Liu, Biao Gong, Guoshan Lu, Yiding Tian, Chunhua Shen, Zhenzhong Lan, Chi Zhang
**Links:** [abs](https://arxiv.org/abs/2611.22925) - [pdf](https://arxiv.org/pdf/2611.22925)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Code World Model 2.0: Towards Infinite Controllable Video Generation
- 作者：Ruoyu Wang, Hao Zhong, Yanming Yang, Jiahao Tian, Lin Liu, Biao Gong, Guoshan Lu, Yiding Tian, Chunhua Shen, Zhenzhong Lan, Chi Zhang
- 出版日期：2026-11-17T15:23:57Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供
- 链接：[摘要](https://arxiv.org/abs/2611.22925) / [PDF](https://arxiv.org/pdf/2611.22925)

### 一句话总结
论文提出 Invoker-Render：以结构代理、外观参考和语言为共享条件接口，将双向创作模型与因果四步流式模型配对，并通过 Progressive Forcing 缓解步压缩与自回归漂移，面向可控视频生成与实时交互流式渲染。

### 研究问题
摘要指出视觉代理将显式世界状态模拟与真实感视频合成解耦，为离线片段创作和实时交互流式生成提供可控接口。但实际渲染器面临两个挑战：
1. 上游代理的粒度差异大，从粗粒度布局到精细关节几何，取决于交互方式；
2. 流式推理需要在少量因果步骤内运行，并且在自生成历史中不累积漂移。

### 核心思路/方法
- 提出 Invoker-Render，配对双向创作模型与因果四步流式模型，二者共享一个条件接口，该接口覆盖结构代理、外观参考和语言。
- 在约 200 小时对齐的多粒度语料上训练，使模型在提供精细几何约束时遵循约束，在粗粒度代理下合成合理的局部运动，从而支持运行时选择输入细节。
- 提出 Progressive Forcing（ProForcing），用于连接双向创作与实时流式生成，避免步压缩与 rollout 漂移叠加。其训练过程包括：先训练因果预测器，再用训练视频得到的历史将其蒸馏为四步渲染器；随后训练转向连续自生成 rollout。
- 使用流水线化服务栈支持高效流式推理。

### 主要贡献
- 提出共享条件接口下的双向创作模型与因果四步流式模型组合 Invoker-Render。
- 构建约 200 小时对齐的多粒度训练语料，并支持不同代理家族、粒度与相机路径的控制。
- 提出 Progressive Forcing（ProForcing），用于桥接双向创作与实时流式生成并缓解压缩与漂移问题。
- 摘要报告实验显示：相较近期流式基线有一致增益；支持稳定的 30 分钟赛车 rollout，并保持场景与主体外观。
- 提供流水线化服务栈以支持高效流式推理。

### 局限性
- 摘要未提供足够信息说明模型的具体失败模式、定量指标细节、对比基线清单与消融实验规模。
- 摘要未提供足够信息说明 30 分钟 rollout 的评测协议、漂移度量方式及计算资源开销。
- 摘要未提供足够信息说明多粒度语料的具体构成、标注方式与数据偏置。
- 摘要未提供足够信息说明方法在非赛车场景或更广泛开放域中的泛化边界。

### 阅读优先级
中。理由：论文聚焦可控视频生成与世界模型式渲染，涉及实时流式、长时 rollout 稳定性和多粒度代理控制，问题定义清晰且方法要素明确；但摘要未给出定量结果细节与充分实验协议，是否高优先级取决于读者对流式可控视频生成、实时渲染或具身/AR 应用方向的直接兴趣。

</details>

<details>
<summary>Abstract</summary>

Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming. Yet a practical renderer must address two challenges. Upstream proxies vary from coarse layouts to fine articulated geometry depending on the interaction, and streaming inference must operate in a few causal steps without accumulating drift across self-generated history. We present Invoker-Render, pairing a bidirectional creation model with a causal four-step streaming model under a shared conditioning interface over structural proxies, an appearance reference, and language. Trained on an aligned approximately 200-hour multi-granularity corpus, Invoker-Render honors fine geometric constraints when supplied while synthesizing plausible local motion under coarse proxies, enabling runtime selection of input detail. To bridge bidirectional creation and real-time streaming without compounding step compression and rollout drift, we introduce Progressive Forcing (ProForcing). ProForcing first trains a causal predictor and distills it into a four-step renderer using histories derived from training videos. Training then shifts to continuous self-generated rollouts. A pipelined serving stack supports efficient streaming inference. Experiments show versatile control across proxy families, granularities, and camera paths, consistent gains over recent streaming baselines, and stable 30-minute racing rollouts that preserve scene and subject appearance.

</details>

#### 2026-11-17 - Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, Chao Ma
**Links:** [abs](https://arxiv.org/abs/2611.22880) - [pdf](https://arxiv.org/pdf/2611.22880)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, driving scene, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving
- 作者：Guoqing Wang, Pin Tang, Xiangxuan Ren, Chao Ma
- 出版日期：2026-11-17T14:53:49Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.22880 ；PDF https://arxiv.org/pdf/2611.22880

### 一句话总结
论文提出 AgentWorld，一种以交通参与者（agent）为中心的 VLA 世界模型，用离散 agent token 同时进行场景推理与轨迹规划，以避免像素级未来帧生成中大量与驾驶无关的视觉细节带来的瓶颈。

### 研究问题
现有将 VLA 模型与世界建模结合的端到端自动驾驶方法，多在像素级生成未来帧，并产生大量稠密视觉 token。摘要指出，这类生成结果虽然视觉上看似合理，但保留了许多与驾驶无关的外观细节，只有小部分 token 直接编码与规划相关的因素，例如 agent 几何、运动动态和交互，从而形成显著性能瓶颈。由此引出问题：世界 VLA 模型应基于何种世界状态进行推理，以支持超越像素级预测的规划。

### 核心思路/方法
论文主张面向规划的世界建模应聚焦于紧凑、结构化的、以 agent 为中心的潜在状态，用来捕捉驾驶场景中物体随时间的交互。据此提出 AgentWorld：使用离散 agent token 联合进行推理和轨迹规划；每个 token 动态绑定到周围某个 agent，并关联该对象的状态，包括语义身份、3D 几何、运动与交互上下文。摘要称 AgentWorld 通过三个关键过程学习这些 token：显式几何 grounding、面向推理的监督微调，以及面向 agent 的强化学习。

### 主要贡献
- 提出以 agent 为中心的 VLA 世界模型 AgentWorld，用离散 agent token 同时服务推理与轨迹规划。
- 明确指出现有像素级世界 VLA 模型中稠密视觉 token 与规划相关性不足的问题，并主张以紧凑结构化的 agent-centric latent state 作为规划导向的世界建模对象。
- 设计三类学习过程：显式几何 grounding、推理导向监督微调、agent 导向强化学习。
- 摘要称在多样驾驶场景下的开环与闭环实验表明，AgentWorld 提升规划能力、充分利用视觉证据与 agent 动态，并产生可解释的 agent-centric 世界状态。具体实验设置与数值结果摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明开环与闭环实验的具体数据集、评价指标、基线对比和定量结果。
- 摘要未提供足够信息说明三类训练过程的具体实现细节、计算开销或 token 数量等设计参数。
- 摘要未提供足够信息说明方法在失败场景、长尾场景或真实部署条件下的表现与限制。
- 摘要未提供足够信息说明与像素级世界 VLA 方法在同等条件下的系统性消融结果。

### 阅读优先级
中。理由：论文主题与端到端自动驾驶中的 VLA、世界模型和规划相关，且提出以 agent 为中心的表征思路，具有明确的问题意识和潜在参考价值；但当前仅有标题、作者与摘要，缺少实验细节、定量结果和实现信息，是否值得深入复现或引用需待全文确认。

</details>

<details>
<summary>Abstract</summary>

Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible, they preserve many driving-irrelevant appearance details, i.e., only a small portion of the tokens directly encode critical planning-relevant factors, such as agent geometry, motion dynamics, and interactions. This introduces a significant performance bottleneck. An important question thus arises: what world state should a world VLA model reason over to support planning beyond pixel-level prediction? We argue that planning-oriented world modeling should focus on a compact and structured agent-centric latent state that captures the interactions between objects in the driving scene over time. As such, we introduce AgentWorld, an agent-centric VLA world model that uses discrete agent tokens jointly for reasoning and trajectory planning. Each token is dynamically grounded to a surrounding agent associated with its object's state, such as semantic identity, 3D geometry, motion, and interaction context. AgentWorld learns these tokens through three key processes: explicit geometric grounding, reasoning-oriented supervised fine-tuning, and agent-oriented reinforcement learning. Extensive open-loop and closed-loop experiments under diverse driving scenarios show that AgentWorld enhances planning capabilities, fully exploits visual evidence and agent dynamics, and yields interpretable agent-centric world states.

</details>

#### 2026-11-17 - Network-Exposed Configuration Attacks on LLM-Controlled Social Robots

**Authors:** Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung, Quang Dan Le, Hong Qing Yu
**Links:** [abs](https://arxiv.org/abs/2611.22761) - [pdf](https://arxiv.org/pdf/2611.22761)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Network-Exposed Configuration Attacks on LLM-Controlled Social Robots
- 作者：Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung, Quang Dan Le, Hong Qing Yu
- 出版日期：2026-11-17T13:27:57Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.22761 ；PDF https://arxiv.org/pdf/2611.22761

### 一句话总结
论文研究针对 LLM 控制社交机器人 Reachy Mini Lite 的网络暴露配置攻击，发现攻击者可通过管理接口在无对话输入的情况下替换人格设置和云端 LLM 系统提示，并在物理硬件上产生可观察行为变化。

### 研究问题
论文关注具身机器人中 LLM 带来的安全依赖问题：除推理层之外，网络暴露的配置层是否可被未认证攻击者利用，从而绕过对话式提示注入的防护，改变机器人的人格设置与云端 LLM 系统提示。摘要还关注此类弱点在公开仓库中的复现情况，以及开发者网络假设与消费级具身 AI 安全之间的部署差距。

### 核心思路/方法
- 以 Pollen Robotics Reachy Mini Lite 为对象，研究网络暴露的配置攻击路径。
- 对比两类攻击面：一是 11 次、覆盖 5 个类别的提示注入尝试（摘要称均被抵抗）；二是配置层攻击路径（摘要称两条路径均在物理硬件上产生可观察行为变化）。
- 展示本地和网络邻近访问方式，并将弱点映射到 CWE-306（关键功能缺少认证）和 CWE-1327（绑定到不受限 IP 地址），报告 CVSS v3.1 分数为 6.5（中危）。
- 指出配置端点可在无 CORS 预检情况下接受跨源请求（CWE-352；6.5 中危），且持久记忆存储未执行其声明的限制。
- 对 59 个公开仓库进行源码审查，统计缺失认证的出现情况。

### 主要贡献
- 揭示 LLM 控制社交机器人在配置层的网络暴露攻击：无需对抗性对话输入即可替换人格设置和云端 LLM 系统提示。
- 在物理硬件上观察到配置层攻击导致的行为变化，并与提示注入被抵抗的结果形成对比。
- 给出弱点映射与风险评分：CWE-306、CWE-1327、CWE-352，CVSS v3.1 均为 6.5（中危）。
- 通过 59 个公开仓库的源码审查，报告缺失认证在 11 个可源码验证的真实应用中有 10 个存在，计入一个框架默认案例后为 11/11；摘要明确限定这表示样本仓库中的复现，而非商业产品中的普遍性。
- 提出开发者导向的网络假设与消费级具身 AI 安全之间存在部署差距，并指出潜在后果包括通过机上摄像头和麦克风进行监视，以及对附近用户实施社会工程。
- 摘要称提供概念验证代码、证据和调查，链接为 https://bit.ly/reachypi。

### 局限性
- 摘要未提供足够信息说明实验环境、样本规模、测试协议和统计细节。
- 摘要未提供足够信息说明提示注入 11 次尝试的具体类别内容与判定标准。
- 摘要未提供足够信息说明配置层两条攻击路径的具体技术细节与独立复现条件。
- 摘要未提供足够信息说明 59 个公开仓库的筛选标准、应用类型分布及审查方法。
- 摘要明确将仓库审查结论限定为样本内复现，不能外推为商业产品中的普遍性。
- 摘要未提供足够信息说明缓解措施的有效性评估。

### 阅读优先级
中。理由：论文聚焦 LLM 控制具身机器人的配置层安全，问题具体且涉及物理硬件行为变化，并给出 CWE 映射、CVSS 评分和公开仓库审查，对具身 AI 与机器人安全读者有参考价值；但摘要未提供实验细节和缓解评估，且仓库结论被作者明确限定为样本内复现，因此优先级定为中而非高。

</details>

<details>
<summary>Abstract</summary>

Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings and the cloud LLM's system prompt through a management interface, without adversarial conversational input. Eleven prompt-injection attempts across five categories were reported as resisted, whereas both configuration-layer attack paths produced observable behavioural changes on physical hardware. We demonstrate local and network-adjacent access, mapping the weakness to CWE-306 (Missing Authentication for a Critical Function) and CWE-1327 (Binding to an Unrestricted IP Address), with a reported CVSS v3.1 score of 6.5 (Medium). A configuration endpoint also accepts cross-origin requests without a CORS preflight (CWE-352; 6.5 Medium), while the persistent-memory sink stores content without enforcing its stated restrictions. A source review of 59 public repositories identifies missing authentication in 10 of 11 source-verifiable genuine applications, or 11 of 11 including a framework-default case. These findings indicate recurrence within the sampled repositories, not prevalence in commercial products. We characterise a deployment gap between developer-oriented network assumptions and consumer-facing embodied AI security: inference-layer refusal cannot prevent unauthorised changes to model instructions. Potential consequences include surveillance through onboard cameras and microphones and social engineering of nearby users. Proof-of-concept code, evidence and the survey are available at https://bit.ly/reachypi.

</details>

#### 2026-11-17 - CascadeJEPA: Enhancing 3D Geometric Representations via Spatially Coupled Cascaded Prediction

**Authors:** Kailai Zhou, Ziqi Chen, Xiaoning Xu, Yuefeng Wu, Zixuan Fu, Zijun Lin, Zhihao Li, Youwei Pang, Xiaoqi Zhao, Xun Cao, Bihan Wen
**Links:** [abs](https://arxiv.org/abs/2611.22686) - [pdf](https://arxiv.org/pdf/2611.22686)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CascadeJEPA: Enhancing 3D Geometric Representations via Spatially Coupled Cascaded Prediction
- 作者：Kailai Zhou, Ziqi Chen, Xiaoning Xu, Yuefeng Wu, Zixuan Fu, Zijun Lin, Zhihao Li, Youwei Pang, Xiaoqi Zhao, Xun Cao, Bihan Wen
- 出版日期：2026-11-17T12:36:05Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.22686 ；PDF https://arxiv.org/pdf/2611.22686

### 一句话总结
针对 I-JEPA 在预训练中语义识别提升但 3D 几何表示退化的问题，论文提出 CascadeJEPA，通过全网格上下文编码与预测阶段间的交叉注意力增强 patch 级交互，在基本保留原架构的同时改善 3D 几何任务表现并维持语义识别性能。

### 研究问题
论文指出，对 I-JEPA 的分析发现语义学习与几何学习之间存在逐渐扩大的差距：预训练中语义识别改善的同时，3D 几何表示却在退化。作者假设，这一现象部分源于在不完整空间上下文下预测高度抽象的潜在表示，使模型更偏向语义规律而非细粒度几何信息。因此，核心问题是：如何在不大幅改动 I-JEPA 架构的前提下，缓解语义与几何表示之间的失衡。

### 核心思路/方法
论文提出 CascadeJEPA，一个“空间耦合的级联预测”框架。其关键设计包括：全网格上下文编码（full-grid context encoding），以及预测阶段之间的交叉注意力（cross-attention between prediction stages），以促进更丰富的 patch 级交互。摘要强调该方法在较大程度上保留了原始 I-JEPA 架构。

### 主要贡献
- 识别并分析了 I-JEPA 中语义识别提升与 3D 几何表示退化之间的不一致现象。
- 提出 CascadeJEPA，通过全网格上下文编码和阶段间交叉注意力增强 patch 级交互，同时基本保留 I-JEPA 架构。
- 摘要称在多个 3D 几何任务上相较 I-JEPA 取得显著提升，并保持较强的语义识别性能；优势还延伸到未来特征预测和世界模型规划。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集、评价指标和定量结果。
- 摘要未提供足够信息说明计算开销、训练成本或架构改动带来的效率影响。
- 摘要未提供足够信息说明方法在不同骨干网络或不同预训练规模下的泛化性。
- 摘要未提供足够信息说明“全网格上下文编码”和“阶段间交叉注意力”的详细实现与消融结果。

### 阅读优先级
中。理由：论文聚焦 JEPA 类视觉表示学习中语义与 3D 几何表示的平衡问题，问题定位清晰，且与具身/机器人/AR 应用分类相关；但当前仅有摘要信息，缺少实验细节与定量证据，适合作为相关方向的可跟踪工作进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) have emerged as a promising paradigm for predictive visual representation learning. However, our analysis of I-JEPA reveals a growing discrepancy between semantic and geometric learning: improved semantic recognition during pretraining is accompanied by degraded 3D geometric representations. We hypothesize that this partly stems from predicting highly abstract latent representations with incomplete spatial context, favoring semantic regularities over fine-grained geometric information. To address this issue, we introduce CascadeJEPA, a spatially coupled cascaded prediction framework that promotes richer patch-level interactions through full-grid context encoding and cross-attention between prediction stages, while largely preserving the original I-JEPA architecture. Extensive experiments demonstrate substantial improvements over I-JEPA across multiple 3D geometric tasks while maintaining strong semantic recognition performance. Furthermore, its advantages extend to future feature forecasting and world model planning, highlighting the potential of enhanced geometric representations to support predictive world modeling.

</details>

#### 2026-11-17 - InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation

**Authors:** Chen Zhao, Zipeng Ye, Shifeng Bao, Yihan Lin, Haitao Shen, Yining Luo, Yuchen Xie, Jing Zhang
**Links:** [abs](https://arxiv.org/abs/2611.22584) - [pdf](https://arxiv.org/pdf/2611.22584)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation
- 作者：Chen Zhao, Zipeng Ye, Shifeng Bao, Yihan Lin, Haitao Shen, Yining Luo, Yuchen Xie, Jing Zhang
- 出版日期：2026-11-17T11:07:45Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供
- 链接：[摘要](https://arxiv.org/abs/2611.22584)｜[PDF](https://arxiv.org/pdf/2611.22584)｜[项目页](https://lingwupro.github.io/InteractVLA/)

### 一句话总结
InteractVLA 通过双向几何接口，把预训练的流式 VLA 策略转化为可由视觉语言智能体进行几何引导与结果检查的可控工具，以缓解策略调用失败时的无效重试或人工接管问题。

### 研究问题
现有智能体式操作（agentic manipulation）系统把预训练的 VLA 策略当作不透明的、仅接受语言指令的基元：当策略在不熟悉指令或场景扰动下调用失败时，智能体无法引导其行为，只能无效重试或付出高昂代价进行人工接管。论文旨在解决“预训练 VLA 策略缺乏可引导性与可检查性”这一问题。

### 核心思路/方法
论文提出 InteractVLA 框架，通过一个与视觉语言智能体之间的双向几何接口，使预训练的流式（flow-based）VLA 成为几何上可引导、可检查的工具，包含两个方向：

- **前向：测试时几何引导（test-time geometric guidance）**。将智能体指定的末端执行器目标，经由可微的“指令到位姿”映射，通过动作专家转换为输入梯度；“软时间目标对齐（soft-time target alignment）”把到达时间视为潜在的执行索引，以匹配目标位姿，同时不扭曲策略原有的接近运动。
- **反向：动作信息驱动的智能体式精修（action-informed agentic refinement）**。将生成的动作块与标定后的相机重投影暴露给智能体，使其能够诊断空间偏差、为后续 VLA 调用修正目标，或在已引导轨迹之上局部调整运动片段。

摘要还指出，让 VLA 变得可控不仅提升了在线智能体式工具使用，还解锁了有效的递归自我改进（RSI）。

### 主要贡献
- 提出 InteractVLA，将预训练流式 VLA 从“不透明、仅语言”的基元转变为具备几何可引导性与可检查性的交互式工具。
- 设计双向几何接口：前向实现测试时几何引导与软时间目标对齐；反向实现基于动作块与相机重投影的智能体式诊断与精修。
- 摘要报告达到当前最优性能：LIBERO-Plus 99.4%、RoboDojo 48.62%、RoboCasa365 89.4%。
- 摘要声称该可控性可解锁有效的递归自我改进（RSI）。

### 局限性
- 摘要未提供足够信息说明实验设置、基线对比、消融实验与失败案例分析。
- 摘要未提供足够信息说明方法在不同 VLA 架构、任务类型或真实机器人平台上的泛化能力。
- 摘要未提供足够信息说明计算开销、推理时延以及“输入梯度”引导的稳定性与安全性。
- 摘要未提供足够信息说明 RSI 的具体机制、收益来源及其潜在风险。
- 摘要未提供足够信息说明“标定后的相机重投影”对相机标定误差的敏感程度。

### 阅读优先级
**高**。理由：论文直指智能体式机器人操作中 VLA 策略不可引导、不可检查的关键瓶颈，提出的双向几何接口思路具有方法层面的新颖性；摘要给出的三个基准指标（LIBERO-Plus、RoboDojo、RoboCasa365）覆盖面较广且数值较高，并涉及 RSI 这一值得关注的议题。但需注意，上述判断仅基于摘要，实验细节与结论可靠性需阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Existing agentic manipulation systems treat pretrained vision-language-action (VLA) policies as opaque, language-only primitives: when a policy call fails under unfamiliar instructions or scene perturbations, the agent cannot steer its behavior and is forced into futile retries or costly manual takeover. We present InteractVLA, a framework that turns pretrained flow-based VLAs into geometrically steerable and inspectable tools through a bidirectional geometric interface with vision-language agents. In the forward direction, test-time geometric guidance translates an agent-specified end-effector target into input gradients through the action expert via a differentiable command-to-pose mapping, while soft-time target alignment treats arrival time as a latent execution index to match the target pose without distorting the policy's approach motion. In the reverse direction, action-informed agentic refinement exposes generated action chunks and calibrated camera reprojections back to the agent, allowing it to diagnose spatial discrepancies, revise targets for subsequent VLA calls, or locally adjust motion segments on top of the guided trajectory. Making the VLA controllable not only boosts online agentic tool use, but also unlocks effective recursive self-improvement (RSI), achieving state-of-the-art performance of 99.4\% on LIBERO-Plus, 48.62\% on RoboDojo, and 89.4\% on RoboCasa365. Project page: https://lingwupro.github.io/InteractVLA/.

</details>

#### 2026-11-17 - Inertial Video World Models

**Authors:** Yuan Gao, Fan Xu, Yu Guo, Yuxu Lu, Zhengru Fang, Hao Wu, Xiaomeng Huang
**Links:** [abs](https://arxiv.org/abs/2611.22314) - [pdf](https://arxiv.org/pdf/2611.22314)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Inertial Video World Models
- 作者：Yuan Gao, Fan Xu, Yu Guo, Yuxu Lu, Zhengru Fang, Hao Wu, Xiaomeng Huang
- 出版日期：2026-11-17T07:09:41Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供。
- 链接：摘要页 https://arxiv.org/abs/2611.22314 ；PDF https://arxiv.org/pdf/2611.22314 ；代码 https://github.com/YuanGao-YG/InertialWorld

### 一句话总结
论文提出 InertialWorld，将“惯性”作为自回归视频世界模型的结构性先验，通过 Inertial Memory 跨时间携带场景证据而非每步重建，以缓解自回归推演中的误差累积和动力学不稳定问题。

### 研究问题
论文关注现有视频世界模型缺乏显式的惯性状态演化机制，导致运动与结构的连续性只能隐含在视频预测中；在自回归推演过程中，反复重建会累积误差并使预测动力学不稳定。

### 核心思路/方法
核心是将惯性引入为自回归预测的结构性先验：已有场景证据跨时间被携带，而不是在每一步重新构建。关键组件为 Inertial Memory，它将记忆从被动的预测上下文转变为演化的视频状态，包含两种互补视图：
- 稠密欧拉网格：保留与场景对齐的证据；
- 持久拉格朗日载体：将局部内容绑定到学习到的规范坐标。

每一步中，模型根据动作条件运动传输载体内容，由传输后的载体和稠密网格预测完整的下一视频状态，并使用学习到的门控将传输内容与新预测内容组合进记忆，供下一步使用。

### 主要贡献
- 提出 InertialWorld，将惯性作为自回归视频世界模型的结构性先验，使场景证据跨时间携带而非逐步重建。
- 设计 Inertial Memory，以稠密欧拉网格和持久拉格朗日载体两种互补视图表示演化的视频状态。
- 给出基于动作条件运动传输载体、预测下一视频状态并用学习门控融合传输内容与新预测内容的逐步更新机制。
- 摘要称在机器人操作、3D 游戏仿真和开放世界导航等多个领域进行了广泛实验，并在自回归预测性能上优于强视频世界模型基线；具体实验设置与数值结果摘要未提供足够信息。

### 局限性
摘要未提供足够信息来评估局限性，例如计算开销、长期推演稳定性边界、失败场景、对各领域的泛化限制以及基线对比的详细实验条件等，均未在摘要中说明。

### 阅读优先级
中。理由：论文主题与具身智能、机器人操作和视频世界模型的自回归稳定性直接相关，方法思路清晰且提供代码链接；但摘要未给出具体实验数值、消融结果和局限分析，是否值得优先精读需结合全文实验部分进一步判断。

</details>

<details>
<summary>Abstract</summary>

The physical world has inertia: it evolves from what already exists rather than being recreated at every instant. However, many existing video world models lack an explicit mechanism for inertial state evolution, leaving the continuity of motion and structure implicit in video prediction. During autoregressive rollouts, repeated reconstruction can accumulate errors and destabilize the predicted dynamics. To address this limitation, we introduce InertialWorld, an Inertial Video World Model that makes inertia a structural prior for autoregressive prediction: existing scene evidence is carried across time rather than reconstructed at every step. Central to this formulation is Inertial Memory, which turns memory from passive predictive context into an evolving video state with two complementary views: a dense Eulerian grid preserves scene-aligned evidence, while persistent Lagrangian carriers bind local content to learned canonical coordinates. At each step, the model transports the carrier content according to action-conditioned motion, predicts the complete next video state from the transported carriers and dense grid, and uses a learned gate to combine transported and newly predicted content into the memory for the next step. Extensive experiments across multiple domains, including robot manipulation, 3D game simulation, and open-world navigation, demonstrate that InertialWorld achieves competitive autoregressive prediction performance against strong video world model baselines. Codes link: https://github.com/YuanGao-YG/InertialWorld

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
