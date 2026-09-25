# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：64
- 分类分布：
  - Embodied / Robotics / AR Applications: 24
  - 3D Reconstruction & Multi-view Geometry: 17
  - Neural Scene Representations & Rendering: 15
  - Geometry Foundation Models: 4
  - Dynamic / 4D Reconstruction: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **视觉语言模型从“语义描述”转向“空间/几何落地”，成为具身智能感知的核心组件。**
   多篇论文围绕 VLM 在机器人场景中的几何短板展开：`VLMs Can Describe, But Not Measure` 明确指出 VLM 语义强、度量弱，提出“VLM 标注 + 深度 grounding”的模块化物体中心表示；`AnchorReasoning` 用视觉 grounded 思维链把决策关键元素与轨迹规划连接；`Spatial and Semantic Reasoning for LLM-Driven Robot Navigation via MCP` 通过 MCP 标准化工具把占据栅格转成 LLM 可用的度量/位姿感知图像。共同信号是：单纯调用 VLM 不够，需要显式的空间表示层或数据监督把语义与几何对齐。

2. **几何基础模型（前馈深度/点云先验）正在被“缝合”进 SLAM、检测与地图构建等经典几何管线。**
   `DAVIO` 用 Depth Anything 3 同时做单目惯性 SLAM 的启动与建图，解决传统 VIO 等视差启动、只保留稀疏路标的问题；`Leveraging Vision-Based Point Cloud Map Priors` 用 Pi3X + DINOv3 从历史相机轨迹构建点云先验，替代昂贵的 LiDAR 建图；`Vision Foundation Models with Synthetic-Only Training` 用 DINOv3 替换小编码器提升航天器位姿估计。趋势是前馈几何模型不再只做离线预测，而是作为先验/初始化嵌入在线系统。

3. **3D 高斯表示从“照片级重建”走向“可交互、可解耦、可物理驱动”。**
   `φ-RIE` 把 3DGS 场景中选定物体转为可移动仿真资产并补全被遮挡背景，目标是机器人仿真中的物体级交互；`GaussPDE` 在不重训练的前提下把 PDE 动力学注入预训练 3DGS，通过图拉普拉斯演化修改球谐直流系数；`InfiNoVA` 用时变 3D 高斯把多相机演示重建成密集新视角用于 VLA 策略增强；`ArborSplat` 则把语义直接优化到高斯地图上。共同方向是 3DGS 从静态可视化走向可编辑、可仿真、可驱动的场景表示。

4. **语义/运动先验从“二值剔除”转向“连续调制”，以保留对应密度。**
   `KYS-SLAM` 明确反对现有语义/动态 SLAM 的二元特征拒绝，改为把语义、全景、运动先验融合为连续对应代价；`ArborSplat` 用类别特定高度带约束和标签一致性拒绝来提升细薄结构语义可靠性。两者都反映同一思路：上下文证据是分级量，不是排他性准则。

5. **多模态融合继续向“物理一致性”和“鲁棒性补偿”深入，而非简单拼接。**
   `Reflection-Aware Reasoning` 用相机 + 2D 雷达在 BEV 空间推断反射阶数与反射面，再用物理引导射线追踪定位 NLOS 行人；`Wave-Robust Passive AUV Localization` 用 IMU 对波浪引起的 6-DOF 阵列扰动做协方差去扭曲后再做 MUSIC DOA；`From LiDAR Maps to Visual Localization` 把 LiDAR 地图渲染成带 2D-3D 来源的准图像，让相机与地图共享视觉特征匹配器。这些工作都在处理模态间/物理扰动带来的系统性偏差。

#### 技术路线观察

- **几何基础模型方向**：`DAVIO`、`Leveraging Vision-Based Point Cloud Map Priors`、`Vision Foundation Models with Synthetic-Only Training` 代表了“用大规模前馈模型提供几何/语义先验”的路线。区别在于：DAVIO 把深度模型嵌入 VIO 滤波器的启动与建图闭环；点云先验论文把 Pi3X 当建图器、DINOv3 当语义增强；航天器位姿论文则是把 DINOv3 当编码器替换。共同点是基础模型仍需要下游几何约束（IMU 预积分、BEV 融合、热力图架构）来恢复度量尺度与重力。

- **3D/4D 重建方向**：`RawHDRV` 处理单曝光 Raw 视频的 HDR 重建，属于 4D/动态重建中的成像前端问题，利用 Bayer 通道曝光特性而非交替曝光；`GTR` 从效率角度切入密集预测骨干，用门控线性注意力替代 softmax 注意力，服务于高分辨率 3D 感知。两者分别从“输入动态范围”和“骨干效率”两个侧面支撑 3D/4D 重建的可扩展性。

- **神经场景表示方向**：`RoomLight` 提出 2.5D 室内光照先验，把 VAE 潜空间解码为 HDR radiance 与深度并参数化为面光源，纠正远场环境贴图假设；`GaussPDE` 在高斯基元上做 PDE 演化；`φ-RIE` 做高斯场景的物体解耦与背景补全；`InfiNoVA` 用时变高斯做视角增强；`ArborSplat` 做语义高斯 SLAM。整体看，神经场景表示正从“重建保真度”转向“物理先验正确性、可编辑性、语义可靠性、下游任务可用性”。

- **机器人/AR 应用方向**：`AnchorReasoning` 关注长尾自动驾驶的 VG-CoT 监督；`VLMs Can Describe, But Not Measure` 关注桌面操作中的物体中心表示；`KYS-SLAM`、`From LiDAR Maps to Visual Localization`、`ArborSplat` 关注定位与建图；`BladeMaster` 关注可变形物体切割仿真；`Spatial and Semantic Reasoning for LLM-Driven Robot Navigation via MCP` 关注 LLM 与 ROS 的标准化接口；`Skytopia` 关注单目无人机导航的潜在世界模型；`Wave-Robust Passive AUV Localization` 和 `Reflection-Aware Reasoning` 关注水下/非视距等极端感知条件。应用侧的共同瓶颈是：语义可用但几何不可靠，或几何可靠但语义/交互不可用。

#### 值得优先阅读的论文

1. **`DAVIO: Dense Monocular-Inertial SLAM with Feed-Forward Initialization and Pose-Conditioned Mapping`**
   理由：它把前馈多视角深度模型与经典 VIO 滤波器做了较完整的闭环设计——五图像窗口无特征线性系统启动、缓冲重放、位姿条件化深度、沿视线残差尺度校正、保重力子图。对同时关心几何基础模型和 SLAM 的读者，这是今天最系统的一篇。

2. **`AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios`**
   理由：416k 帧、395k 决策关键元素、VG-CoT 分层监督、课程式微调、物体尺寸感知 grounding 指标，规模和任务定义都较完整。它直接回应“VLM 在驾驶中缺少视觉证据与推理/规划连接”的监督缺口，是自动驾驶 VLM 方向值得优先读的数据集类工作。

3. **`φ-RIE: From Photorealistic Reconstruction to Interactive Environments`**
   理由：把 3DGS 重建转成可交互仿真资产，核心洞察“资产构建与源移除应耦合、同一物体身份定义可移动资产与需补全内容”具有方法启发性。对机器人仿真、具身智能、3DGS 编辑交叉方向价值高。

4. **`KYS-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM`**
   理由：它把“上下文不合理性”从二值剔除重构为连续对应代价，模块化扩展 ORB-SLAM3 且不改几何后端，思路清晰、工程可复用性强。对语义/动态 SLAM 的读者，这是今天最值得细读的方法论转变。

5. **`RoomLight: A 2.5D Illumination

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-25T13:08:13-04:00
**Total number of papers:** 82
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

#### 2026-09-24 - FounRef: Robust, Structure-Preserving, and Fast Metric Refinement of Frozen Monocular Foundation Priors with Sparse Anchors

**Authors:** Dan Halperin, Mirko Mählisch
**Links:** [abs](https://arxiv.org/abs/2609.29224) - [pdf](https://arxiv.org/pdf/2609.29224)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** depth prediction, metric depth

<details>
<summary>Abstract</summary>

Dense metric depth from cameras is essential to real-world 3D applications, yet achieving accuracy, faithful surface geometry, and fast inference simultaneously remains challenging. Monocular foundation models provide rich, transferable geometric priors but lack reliable metric scale, while depth-completion networks recover metric depth at the cost of geometric fidelity, cross-domain robustness, or speed. We present FounRef, a training-free method that aligns a frozen monocular foundation prior with sparse metric anchors to produce dense metric depth. FounRef is modular by design: its depth prior, anchor source, and refinement solver can each be replaced independently. We instantiate FounRef with MoGe-2 and LiDAR anchors. FounRef validates each anchor against the prior's dense depth prediction, rejecting inconsistencies caused by cross-sensor misalignment that geometry-only filters cannot detect. It then applies global and local metric corrections through a structure-preserving solver, retaining the prior's fine-grained geometry. FounRef requires no task-specific training and operates out of the box across unfamiliar cameras and scenes. On out-of-domain data, it delivers up to 24% lower depth error, 92% lower surface-normal noise, and almost 15x faster inference than DMD3C, a state-of-the-art depth-completion network. By decoupling metric alignment from geometry prediction, FounRef provides an accurate, geometrically faithful, and efficient approach to dense metric depth that can directly benefit from future advances in foundation models and metric sensors.

</details>

#### 2026-09-23 - Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces

**Authors:** Andrew Bond, Ege Erdem Özlü, Tuna Çimen, Ilkin Umut Melanlioglu, Tolga Birdal, Erkut Erdem, Aykut Erdem
**Links:** [abs](https://arxiv.org/abs/2609.27988) - [pdf](https://arxiv.org/pdf/2609.27988)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces
- 作者：Andrew Bond, Ege Erdem Özlü, Tuna Çimen, Ilkin Umut Melanlioglu, Tolga Birdal, Erkut Erdem, Aykut Erdem
- 出版日期：2026-09-23T12:17:02Z
- 分类：Geometry Foundation Models（主要类别）；次要类别未提供
- 链接：摘要链接 https://arxiv.org/abs/2609.27988 ；PDF 链接 https://arxiv.org/pdf/2609.27988 ；项目页 https://cyberiada.github.io/TaskInducedViTs/

### 一句话总结
论文指出 Vision Transformer 特征空间中常用的欧氏距离或余弦相似度隐含“各方向同等重要”的假设，转而用任务诱导的拉回度量刻画特征空间几何，并提出可学习低秩近似的 Spectral Pullback Network 及用于 token 剪枝的重要性头。

### 研究问题
- ViT 特征空间上的方法通常依赖欧氏距离或余弦相似度，默认所有方向同等有意义，但摘要指出没有理由相信真实任务几何具有该性质。
- 任务敏感的特征空间几何由拉回度量 \(g(F) = J(F)^\top J(F)\) 给出，其中 \(J\) 是解码器输出相对于特征的雅可比矩阵，解码器输出被送入任务特定距离。
- 在现代规模下存储完整 \(g\) 不可行；对于深度图等稠密输出，连构造 \(J\) 都不切实际。
- 因此核心问题是：能否学习该度量的低秩近似，以及这种低秩近似是否可学是否取决于模型—解码器组合。

### 核心思路/方法
- 使用任务敏感的拉回度量 \(g(F) = J(F)^\top J(F)\) 描述 ViT 特征空间的真实任务几何。
- 提出一种无矩阵诊断量 \(\kappa_{cap}(r)\)，可用少量雅可比向量积计算，用于判断低秩近似是否可学，并刻画其依赖于模型—解码器对。
- 对可处理的模型—解码器对，提出 Spectral Pullback Network（SPN），通过随机幂迭代学习度量的低秩版本。
- 将 SPN 蒸馏为一个约 310K 参数的重要性头，直接从特征预测 token 重要性。
- 当雅可比谱过于分散、不适合低秩近似时，摘要提出让解码器输入特征通过 VAE 瓶颈以恢复可处理性。
- 在 DPT、DINOv2、CLIP、VGGT 骨干上，用 \(\kappa_{cap}(r)\) 预测哪些学习度量架构可行。
- 几何 token 剪枝在 DPT 深度任务、剪枝比例 0.5 下，将基于 ToMe 的 token 选择带来的额外深度误差降低 25%，且不微调 ViT。

### 主要贡献
- 指出现有 ViT 特征空间方法默认欧氏或余弦几何的假设问题，并引入任务诱导的拉回度量作为任务敏感几何描述。
- 提出可计算少量雅可比向量积的无矩阵诊断 \(\kappa_{cap}(r)\)，用于判断低秩度量近似是否可学，并说明其取决于模型—解码器对。
- 提出 Spectral Pullback Network（SPN），用随机幂迭代学习低秩度量，并蒸馏为约 310K 参数的重要性头。
- 在多个骨干上验证 \(\kappa_{cap}(r)\) 对学习度量架构可行性的预测作用。
- 报告重要性头在 DINOv2 CLS 上达到 Spearman \(\rho = 0.998\)，并在 DPT 深度任务上以几何 token 剪枝降低 ToMe 式 token 选择的额外深度误差 25%。

### 局限性
- 摘要未提供足够信息说明方法在非视觉任务、其他模态或更广泛数据集上的泛化能力。
- 摘要未提供足够信息说明 \(\kappa_{cap}(r)\) 的计算成本、超参数敏感性或失败边界。
- 摘要未提供足够信息说明 VAE 瓶颈恢复可处理性的具体代价、精度损失或适用范围。
- 摘要未提供足够信息说明重要性头在 CLS 之外的 token 类型、不同剪枝比例或不同任务上的表现。
- 摘要未提供足够信息说明是否与微调方法、其他 token 剪枝方法进行了全面对比。
- 摘要未提供足够信息说明低秩近似与完整度量之间的理论误差界。

### 阅读优先级
高。理由：论文直接针对 ViT 特征空间几何这一基础假设，提出可诊断低秩可学性的 \(\kappa_{cap}(r)\)、可学习度量的 SPN 与轻量重要性头，并在 DPT、DINOv2、CLIP、VGGT 上给出验证和深度任务剪枝提升；对关注 ViT 特征几何、token 剪枝与任务感知表示的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Methods operating on Vision Transformer (ViT) feature spaces typically rely on Euclidean distance or cosine similarity. This assumes that every direction is equally meaningful, but there is no reason to believe the true task geometry has this property. The task-sensitive geometry of the feature space is given by the pullback metric $g(F) = J(F)^\top J(F)$, where $J$ is the Jacobian of the decoder's output fed to a task-specific distance, with respect to the features. Storing the full $g$ is infeasible at modern scales, and for dense outputs such as depth maps even forming $J$ is impractical. We show that whether a low-rank approximation of this metric can be learned depends on the model-decoder pair, and we characterize this with a matrix-free diagnostic $κ_{cap}(r)$ computable with a low number of Jacobian-vector products. For tractable pairs, we develop the Spectral Pullback Network (SPN), which learns a low-rank version of the metric from randomized power iteration, and we distill it into a $310$K-parameter importance head that predicts token importance directly from the features. When the Jacobian spectrum is too spread out for a low-rank approximation, passing the decoder's input features through a VAE bottleneck can restore tractability. Across DPT, DINOv2, CLIP, and VGGT backbones, $κ_{cap}(r)$ predicts which learned-metric architectures are viable. The importance head reaches Spearman $ρ= 0.998$ on DINOv2 CLS, and our geometric token pruning reduces the additional depth error of ToMe-based token selection by $25\%$ on DPT depth at prune ratio $0.5$, without fine-tuning the ViT. Project page: https://cyberiada.github.io/TaskInducedViTs/

</details>

#### 2026-09-21 - SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation

**Authors:** Jiangshan Gong, Yuqun Wu, Qiqian Fu, Yao Xiao, Chuhang Zou, Shenlong Wang, Derek Hoiem
**Links:** [abs](https://arxiv.org/abs/2609.25490) - [pdf](https://arxiv.org/pdf/2609.25490)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, 3D reconstruction, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation
- 作者：Jiangshan Gong, Yuqun Wu, Qiqian Fu, Yao Xiao, Chuhang Zou, Shenlong Wang, Derek Hoiem
- 出版日期：2026-09-21T23:39:19Z
- 分类：主分类 Geometry Foundation Models；副分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2609.25490 ；PDF https://arxiv.org/pdf/2609.25490

### 一句话总结
SAM-V 将前馈几何模型 VGGT 的特征直接融入 2D 分割基础模型 SAM，端到端训练实现单次前向传播的多视角一致实例分割，无需离线掩码匹配或显式 3D 重建。

### 研究问题
多视角物体分割在剧烈视角变化与遮挡下仍具挑战。现有做法主要有两条路线：一是直接在点云上做 3D 实例分割，但受限于稀缺的 3D 标注；二是依赖离线的 2D 掩码匹配流程，但跨帧存在物体身份歧义问题。论文关注的核心问题是：如何联合利用强 2D 先验与强 3D 先验，避免后处理匹配带来的身份不一致。

### 核心思路/方法
- 不以事后匹配的方式结合 2D 与 3D 先验，而是将前馈几何模型（VGGT）的特征直接集成进 2D 分割基础模型（SAM），针对跨视角实例预测进行端到端训练。
- 提出提示融合机制（prompt-fusion）：用视角相关的相机 token 与局部 VGGT 特征增强稀疏的 SAM 提示 token，使提示表示既具备视角感知能力，又具备空间接地能力。
- 配套设计掩码解码器（mask decoder），同时关注稠密的 2D 与 3D 特征。
- 通过将掩码解码直接条件化于多视角几何，在单次前向传播中即可对被提示物体产生一致的多视角分割，无需离线掩码匹配或显式 3D 重建。

### 主要贡献
- 提出 SAM-V，将几何基础模型特征与 2D 分割基础模型端到端融合，用于多视角实例分割。
- 提出提示融合机制，使 SAM 的稀疏提示 token 同时具备视角感知与空间接地特性。
- 设计可同时关注稠密 2D 与 3D 特征的掩码解码器，直接以多视角几何为条件生成一致的跨视角分割。
- 在 IGGT 3D 跟踪基准上，于 ScanNet++ 划分中相比最先进的多视角实例分割基线，整体 IoU 提升 5 点、帧级召回提升 12 点；并在零样本 ScanNet 划分的所有指标上领先。
- 代码与预训练模型已公开。

### 局限性
摘要未提供足够信息（未提及失败情形、计算开销、对 VGGT 或 SAM 的依赖风险、标注需求或泛化边界等具体限制）。

### 阅读优先级
中。理由：该工作面向多视角一致实例分割，思路（将几何基础模型特征注入 2D 分割基础模型、避免离线匹配与显式重建）与几何基础模型方向直接相关，且报告了较明显的基准提升并开源代码；但摘要未给出方法细节与局限性的充分信息。是否优先精读，取决于读者对多视角分割、3D 跟踪或几何与 2D 基础模型融合的具体兴趣，摘要未提供额外兴趣方向。

</details>

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

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-24 - Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures

**Authors:** Abhiram Maddukuri, Georgios Pavlakos
**Links:** [abs](https://arxiv.org/abs/2609.30187) - [pdf](https://arxiv.org/pdf/2609.30187)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion reconstruction, embodied AI

<details>
<summary>Abstract</summary>

Ego-Exo4D is a large-scale dataset providing synchronized egocentric and multi-view exocentric video, a rich resource for skill learning and assessment, procedural activity understanding, and embodied AI. However, the dataset ships with only sparse 3D human pose annotations, and reconstructing dense human motion from its multi-view captures is nontrivial. To this end, we present Ego-Exo4D-HM, a large-scale dataset of 4D human motion reconstructions for Ego-Exo4D's captures, and release the accompanying reconstruction pipeline. The code, dataset, and documentation can be found at https://abhiram824.github.io/egoexo4d_human_meshes.

</details>

#### 2026-09-24 - ADATEX4D: adaptive texture capacity allocation for 4D gaussian splatting

**Authors:** De Jiang, Peiqiang Wang, Kehong Yuan, Shaohua Ma
**Links:** [abs](https://arxiv.org/abs/2609.29963) - [pdf](https://arxiv.org/pdf/2609.29963)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Textured Gaussians improve local appearance capacity, but assigning the same texture resolution to every primitive wastes storage on low-detail or weakly visible regions. We introduce AdaTex4D, an adaptive texture-capacity module for deformation-based 4D Gaussian Splatting. Each Gaussian carries packed RGBA triplanes whose two axes grow independently according to visibility normalized screen-space gradients and deformed local scales. Experiments on N3DV and PanopticSports show that AdaTex4D reduces texture storage by more than half while preserving reconstruction quality. Under fixed memory budgets, adaptive allocation also improves quality over uniform texture assignment and reduces overall model and peak memory. These results show that dynamic, anisotropic texture allocation provides a more efficient way to distribute local appearance capacity in 4D Gaussian representations.

</details>

#### 2026-09-24 - SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting

**Authors:** Nitya Nanvani, Andras Palffy, Holger Caesar
**Links:** [abs](https://arxiv.org/abs/2609.29836) - [pdf](https://arxiv.org/pdf/2609.29836)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

While 2D Vision Foundation Models offer a pathway to automate 3D semantic pseudo-labelling, translating these priors into robust 3D representations typically requires complex heuristics or multi-model ensembles. We introduce SplatLabel, an automated pipeline that leverages a 4D Gaussian representation to extract LiDAR segmentation with predictive confidence, as well as semantic occupancy grids at arbitrary voxel resolutions. At its core, SplatLabel handles dynamic environments through an explicit temporal manifold that models the trajectories and lifespans of individual 3D primitives. This allows the system to accurately track moving actors and strictly define when objects appear and disappear, completely eliminating the need for pre-annotated 3D bounding boxes. To robustly support this dynamic tracking, the representation is grounded by structural and semantic priors: we guide scene geometry in unobserved regions by integrating 360-degree LiDAR via virtual depth maps, and rather than relying on domain-specific prompt engineering, we directly distill continuous soft probabilities from 2D models to inherently resolve semantic ambiguities over time and space. Finally, to accurately reflect the real-world trade-off between precision and recall, we reframe pseudo-label evaluation as a selective classification task using a generalized risk-recall metric. Experiments on SemanticKITTI demonstrate that SplatLabel consistently outperforms state-of-the-art baselines across multiple recall levels, establishing a highly robust framework for both 3D LiDAR segmentation and occupancy prediction.

</details>

#### 2026-09-23 - High Dynamic Range Video Reconstruction from Single-Exposure Raw Sequences

**Authors:** Tao Zhang, Peixian Su, Xingyu Gao, Yunhao Zou, Yu Lu, Zunjie Zhu, Bolun Zheng, Ying Fu, Chenggang Yan
**Links:** [abs](https://arxiv.org/abs/2609.27274) - [pdf](https://arxiv.org/pdf/2609.27274)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：High Dynamic Range Video Reconstruction from Single-Exposure Raw Sequences
- 作者：Tao Zhang, Peixian Su, Xingyu Gao, Yunhao Zou, Yu Lu, Zunjie Zhu, Bolun Zheng, Ying Fu, Chenggang Yan
- 出版日期：2026-09-23T03:01:47Z
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2609.27274

### 一句话总结
该论文提出 RawHDRV，一个面向单曝光 Raw 视频的端到端 HDR 重建框架，通过利用 Bayer 数据的线性响应与通道特性，在无需交替曝光或额外硬件的情况下缓解高光裁剪与暗部细节丢失问题。

### 研究问题
传统图像传感器动态范围有限，导致拍摄的低动态范围视频常出现高光裁剪和暗部细节丢失。现有交替曝光 HDR 方法会牺牲帧率并面临运动对齐困难，难以适用于真实拍摄场景。因此，如何从单曝光视频序列中高质量重建 HDR 视频是一个具有挑战性的问题。

### 核心思路/方法
论文提出 RawHDRV 端到端框架，核心在于利用 Bayer 数据的线性响应和通道特定特性：
- 采用通道分解的时间对齐与融合策略，分别处理 Bayer 各通道以利用其不同曝光特性，并结合曝光感知加权融合。
- 引入曝光互补性掩码引导的恢复模块，利用帧间曝光冗余自适应融合可靠信息并抑制饱和伪影。
- 提出掩码引导的颜色损失，结合归一化误差约束与梯度平滑以增强高光恢复。
- 同时构建了一个大规模移动端 Raw-HDR 视频数据集，并带有逐帧 HDR 标注。

### 主要贡献
- 提出 RawHDRV，一个面向单曝光 Raw 视频 HDR 重建的端到端框架。
- 设计通道分解时间对齐与融合策略及曝光感知加权融合。
- 引入曝光互补性掩码引导的恢复模块和掩码引导颜色损失。
- 构建带逐帧 HDR 标注的大规模移动端 Raw-HDR 视频数据集。
- 实验表明该方法在所有指标上达到当前最优，在极端曝光条件下具有更优的空间质量和时间稳定性。

### 局限性
摘要未提供足够信息。摘要中未说明方法的具体失败场景、计算开销、对特定硬件的依赖程度、数据集规模与多样性的详细限制，也未提及在非移动端设备或其他传感器上的泛化能力。

### 阅读优先级
中。理由：该工作针对单曝光 Raw 视频 HDR 重建这一具有实际价值的问题，提出了结合 Bayer 通道特性与掩码引导的完整框架，并构建了新数据集，且声称在所有指标上达到最优。但摘要未提供足够的实验细节、量化结果和局限性讨论，若读者关注 HDR 视频重建、Raw 域处理或动态场景重建，可作为相关方向的重要参考；若仅需泛读，则可暂列为中等优先级。

</details>

<details>
<summary>Abstract</summary>

Due to the limited dynamic range of conventional image sensors, captured low dynamic range (LDR) video often suffers from highlight clipping and shadow detail loss, making high-quality high dynamic range (HDR) reconstruction from single-exposure sequences highly challenging without alternating exposures or extra hardware. Alternating-exposure HDR methods sacrifice frame rate and struggle with motion alignment, making them impractical for real-world capture. To address this, we propose RawHDRV, an end-to-end framework for single-exposure Raw video HDR reconstruction, that fundamentally exploits the linear response and channel-specific characteristics of Bayer data. Specifically, it features a channel-decomposition temporal alignment and fusion strategy that processes Bayer channels separately to exploit their distinct exposure characteristics, together with exposure-aware weighted fusion. It further incorporates an exposure complementarity mask-guided restoration module that leverages inter-frame exposure redundancy to adaptively fuse reliable information and suppress saturation artifacts, and introduces a mask-guided color loss that combines normalized error constraints with gradient smoothing to enhance highlight recovery. Furthermore, we construct a large-scale mobile Raw-HDR video dataset with per-frame HDR annotations. Experiments show that our method achieves the state-of-the-art results in all metrics, demonstrating superior spatial quality and temporal stability under extreme exposure conditions. The code is available at https://github.com/supeixian/RawHDRV.

</details>

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

#### 2026-09-24 - Anatomy-Aligned Surface Field Learning for Myocardial Reconstruction from Sparse Short-Axis Cine MRI

**Authors:** Xiaohan Yuan, Xuan Yang, Qingya Li, Yangang Wang, Lei Li
**Links:** [abs](https://arxiv.org/abs/2609.29825) - [pdf](https://arxiv.org/pdf/2609.29825)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction, simulation

<details>
<summary>Abstract</summary>

Patient-specific 4D myocardial reconstruction from cine MRI supports quantitative functional assessment, regional motion analysis, and simulation-based modeling. However, routinely acquired short-axis (SAX) cine MRI is sparsely sampled along the through-plane direction, making dense and anatomically consistent surface reconstruction challenging. In this study, we propose an anatomy-aligned surface learning framework that parameterizes the epicardial and endocardial surfaces on a shared circumferential-longitudinal UV domain. This formulation converts irregular 3D reconstruction into structured coordinate-field completion with explicit correspondence across subjects and cardiac phases. Sparse SAX contours are encoded as UV observation fields, coverage-aware sampling improves robustness to incomplete slice coverage, and topology- and distortion-aware learning preserves circumferential continuity and local surface quality. Experiments on three public cine MRI datasets showed that the proposed method consistently outperformed representative mesh-based and implicit reconstruction approaches, achieving overall Chamfer distances of $2.887$~mm on ACDC, $2.641$~mm on M\&Ms, and $2.810$~mm on M\&Ms-2. The reconstructed sequences also preserved ventricular function, with end-diastolic volume and ejection fraction errors of $3.3$~mL and $1.1 \%$, respectively. These results demonstrate that anatomy-aligned UV learning provides an accurate, efficient, and correspondence-aware representation for sparse cine MRI reconstruction and myocardial modeling. The source code will be available at https://github.com/yuan-xiaohan/SAX2MyoSurf.

</details>

#### 2026-09-24 - Markerless Multi-Modal Autonomous Robotic Inspection of Large Space Structures

**Authors:** Juan De Dios Alfaro, Arturo Ríos, David Rodríguez-Martínez, Carlos Pérez-del-Pulgar
**Links:** [abs](https://arxiv.org/abs/2609.29644) - [pdf](https://arxiv.org/pdf/2609.29644)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, geometric reconstruction, rendering

<details>
<summary>Abstract</summary>

Future orbital infrastructures, such as deployable antennas, solar farms, and large orbital platforms will require autonomous inspection systems able to operate with limited prior knowledge and without cooperative markers. Current on-orbit servicing approaches often rely on predefined trajectories, standard interfaces, fiducial markers or accurate target models, which limits scalability for large, heterogeneous or partially unknown structures. This paper presents a markerless autonomous robotic inspection pipeline in which 3D reconstruction is used as an inspection-support representation. The system integrates a Kinova Gen2 manipulator with an end-effector-mounted multimodal sensor head composed of an RGB-D camera, a thermal camera and a 2D LiDAR. The pipeline estimates an approximate inspection volume, generates viewpoints, plans collision-free motions with MoveIt, and synchronously records RGB-D images, thermal data, and robot poses in ROS2. Candidate reconstruction methods were evaluated to select a practical method for this pipeline, with Nerfacto used for geometric reconstruction and Thermal-Nerfacto used to demonstrate thermal-aware rendering for inspection. Validation in a Gazebo-based simulator and preliminary laboratory tests reveal that the proposed system can autonomously acquire spatially coherent inspection data and produce reconstructions suitable for visual and geometric assessment, representing a step towards inspection of large non-cooperative space structures.

</details>

#### 2026-09-24 - WildHSR: Metric Feed-Forward 4D People-Scene Reconstruction from a 3D Foundation Model

**Authors:** Jerrin Bright, John Zelek
**Links:** [abs](https://arxiv.org/abs/2609.29106) - [pdf](https://arxiv.org/pdf/2609.29106)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction

<details>
<summary>Abstract</summary>

3D foundation models recover video cameras and geometry in one forward pass, but some of the strongest are up to scale. Joint people-scene reconstruction then requires two missing outputs: metric scale and persistent person identity. We ask whether one up-to-scale foundation representation can support both through lightweight adaptation. Exact metric labels are scarce, but unlabeled in-the-wild video is abundant. We use people in curated web video to initialise the solution: a posed metric body and 2D keypoints give an approximate, closed-form scale pseudo-label. These pseudo-labels pretrain a Scale Readout, which is then fine-tuned together with a lightweight adapter using exact metric supervision from standard real-video training splits. At inference the head predicts metric scale from foundation-model tokens, without the ruler or its teachers. For person identity, we probe the pretrained foundation model alone and find evidence that its intermediate query-key features encode person correspondence across frames. In most evaluated moving-person clips, a mid-layer token prefers that person over the vacated location and other people. A tiny projection reads this correspondence; together with metric pelvis motion and proposal confidence, it drives dustbin-aware Sinkhorn association of per-frame bodies. WildHSR combines both readouts to reconstruct metric cameras, scene and people from monocular video. Each window is predicted feed-forward; analytic association and Sim(3) composition connect windows. On EMDB-2, WildHSR is the first feed-forward method in the published comparison to beat the best optimization-based WA-MPJPE and RTE while leading feed-forward methods on all three world-frame metrics. On RICH, it leads feed-forward people-and-scene methods on WA-MPJPE and W-MPJPE. The complete pipeline runs at 10.1 fps on one GPU.

</details>

#### 2026-09-23 - PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting

**Authors:** Sungjae Choi, Seunghee Koh, Junmo Kim
**Links:** [abs](https://arxiv.org/abs/2609.28645) - [pdf](https://arxiv.org/pdf/2609.28645)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, monocular depth, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

Recent advancements in 3D Gaussian Splatting (3DGS) have extended its capabilities to multi-scale segmentation. Existing methods reconstruct a scene with Gaussian primitives and learn multi-scale segmentation features separately, which leaves the geometry unaware of semantic structure and the feature learning dependent on incomplete mask supervision. To address these limitations, we present PePESeg3D, a novel framework that injects perception priors into a multi-scale 3D Gaussian segmentation pipeline. To fully exploit perception priors, we integrate them not only into contrastive feature learning but also into the upstream geometry reconstruction. Specifically, PePE Reconstruction incorporates monocular depth and mask constraints to ensure semantically coherent object structures. Building on this aligned geometry, PePE Contrastive Learning leverages dense depth-color cues and view-consistent centroid supervision to compensate for the incompleteness of multi-scale masks obtained from a 2D foundation model. Extensive experiments on the SPIn-NeRF, LERF-Mask, and NVOS benchmarks demonstrate that PePESeg3D achieves state-of-the-art performance in both multi-scale segmentation and scene reconstruction, highlighting the importance of integrating perception priors into both geometry optimization and feature learning for accurate multi-scale 3D segmentation. Our code is available at https://github.com/BeCow5X5/PePESeg3D.

</details>

#### 2026-09-23 - Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM

**Authors:** Preeti Chatterjee, Jin Lu, Jin Sun, Suchendra M. Bhandarkar
**Links:** [abs](https://arxiv.org/abs/2609.27509) - [pdf](https://arxiv.org/pdf/2609.27509)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, bundle adjustment, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM
- 作者：Preeti Chatterjee, Jin Lu, Jin Sun, Suchendra M. Bhandarkar
- 出版日期：2026-09-23T08:07:47Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.27509 ；PDF https://arxiv.org/pdf/2609.27509

### 一句话总结
KYS-SLAM 将语义、全景与运动先验转化为连续的特征匹配代价，用“惩罚而非剔除”的方式替代二值特征拒绝，作为 ORB-SLAM3 的模块化扩展以缓解立体视觉 SLAM 的数据关联退化与轨迹漂移。

### 研究问题
基于局部描述子的立体视觉 SLAM 面临三类问题：语义歧义、实例级混淆以及独立运动物体。这些问题都会破坏数据关联，并累积为轨迹漂移。

现有语义与动态 SLAM 方法通过二值特征剔除来应对，但作者认为这会以牺牲对应密度为代价来抑制离群点。论文主张“上下文不合理性”更适合表达为分级量，而不是排他性准则。

### 核心思路/方法
- 将 KYS-SLAM 定位为 ORB-SLAM3 的模块化扩展，用连续的对应调制替代特征剔除。
- 核心做法是把上下文证据重新表述为“对应代价”，应用于特征匹配阶段，并保持几何后端不变。
- 每个关键点被赋予语义、全景和运动先验，并通过分层兼容性公式融合。
- 融合中，语义类别与实例身份用于约束结构合理性；零样本运动分数用于降低位于独立运动物体上的特征权重。
- 该运动分数来自一个免训练模块：将深度感知的自运动模型拟合到背景光流，并通过自校准、覆盖感知的阈值对全景片段进行分类，从而只惩罚具有充分运动证据的片段，静态结构不被惩罚。
- 设计动机是：惩罚对应关系而不是丢弃它们，可以保留光束法平差所依赖的几何支撑集合。

### 主要贡献
- 提出 KYS-SLAM，将上下文证据从排除准则重构为对应代价，用于特征匹配。
- 引入分层语义—全景—运动先验融合，对关键点进行连续兼容性调制。
- 提出免训练、自校准、覆盖感知的动态片段判定方式，仅惩罚有足够运动证据的片段。
- 在固定配置、不按序列或数据集重新调参的条件下，报告了跨域结果：在 21 条立体序列上，室外 KITTI 的逐序列 ATE RMSE 降低 17.4%，室内 EuRoC 降低 27.7%，且无回退；在 KITTI Tracking 动态子集上降低 6.6%；在 Virtual KITTI 2 上降低 17.8%，最高达 31.2%。跨域涵盖室外驾驶、室内飞行和合成图像，并使用同一组常数。

### 局限性
- 摘要未提供足够信息说明方法对极端动态场景、低纹理场景或实时性开销的具体表现。
- 摘要未提供足够信息说明零样本运动分数模块的失败模式与阈值敏感性。
- 摘要未提供足够信息说明与更多基线方法的完整对比细节。
- 摘要未提供足够信息说明代码、数据集划分与完整实现配置。

### 阅读优先级
高。理由：该论文直接针对语义/动态 SLAM 中“剔除特征导致对应密度下降”的关键矛盾，提出连续对应代价这一较具方法学新意的重构思路；同时给出跨室外、室内与合成域的定量结果，且强调单一固定配置无回退，对视觉 SLAM、动态环境建图与语义几何融合方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier suppression. We contend that contextual implausibility is better expressed as a graded quantity than an exclusion criterion. We present Know-Your-Scene (KYS)-SLAM, a modular extension of ORB-SLAM3 that supplants feature rejection with continuous correspondence modulation. The contribution is the reframing of contextual evidence as correspondence cost, applied within feature matching and leaving the geometric backend unmodified. Each keypoint is augmented with semantic, panoptic, and motion priors fused through a hierarchical compatibility formulation, in which semantic class and instance identity enforce structural plausibility while a zero-shot motion score down-weights features on independently moving objects. That score comes from a training-free module fitting a depth-aware ego-motion model to background optical flow and classifying panoptic segments via self-calibrating, coverage-aware thresholds, so only segments with sufficient motion evidence are penalized and static structure is left unpenalized. Penalizing correspondences rather than discarding them preserves the geometric support bundle adjustment depends on. Under one fixed configuration, no coefficient retuned per sequence or dataset, KYS-SLAM reduces per-sequence ATE RMSE by 17.4% on outdoor KITTI and 27.7% on indoor EuRoC across 21 stereo sequences with no regressions, and by 6.6% on dynamic subsets of KITTI Tracking and 17.8%, up to 31.2%, on Virtual KITTI 2 -- cross-domain transfer across outdoor driving, indoor flight, and synthetic imagery under one set of constants.

</details>

#### 2026-09-23 - From LiDAR Maps to Visual Localization: Unified Visual Association for Robust Point-Line-Plane Pose Estimation

**Authors:** Wentao Zhao, Zikun Chen, Yihe Niu, Haoyu Chen, Jingchuan Wang
**Links:** [abs](https://arxiv.org/abs/2609.27363) - [pdf](https://arxiv.org/pdf/2609.27363)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From LiDAR Maps to Visual Localization: Unified Visual Association for Robust Point-Line-Plane Pose Estimation
- 作者：Wentao Zhao, Zikun Chen, Yihe Niu, Haoyu Chen, Jingchuan Wang
- 出版日期：2026-09-23T05:05:05Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.27363 ；PDF https://arxiv.org/pdf/2609.27363

### 一句话总结
该论文提出一种统一视觉关联的定位框架，将已有 LiDAR 地图渲染为带 2D-3D 来源信息的准图像，使相机观测与地图渲染视图可共享视觉特征与匹配器，从而实现全局定位与连续 6-DoF 位姿跟踪。

### 研究问题
论文关注的是：在已有 LiDAR 地图作为持久几何先验的条件下，如何实现相机定位。其核心挑战在于相机图像与点云地图之间存在显著的模态差异。摘要指出，该问题面向长期机器人导航，需要在严重光照变化和动态遮挡等条件下保持定位能力。

### 核心思路/方法
论文提出一个统一定位框架，使 LiDAR 地图变得“视觉可寻址”，而不是依赖专门的图像-LiDAR 对应模型。具体做法是：将地图几何与反射率渲染为 LiDAR 衍生的准图像，并保留显式的 2D-3D 来源关系，从而让相机观测和渲染地图视图能够共享成熟的视觉特征与匹配器，用于全局定位和连续位姿跟踪。

在对应关系上，通过这一共同视觉接口建立点和线对应；同时，利用保留的来源信息恢复度量 LiDAR 几何以及线支持的平面约束，用于位姿估计。

为提升在模糊关联和弱几何条件下的鲁棒性，论文进一步引入一种分布感知、可观测性互补的优化策略。该策略不是把匹配歧义压缩为单一置信度，而是将候选关联分布传播为方向性位姿信息不确定性，并根据可靠结构因子对当前弱位姿方向的互补能力，选择性增强这些结构因子。

### 主要贡献
- 提出统一视觉关联框架，将 LiDAR 地图渲染为带 2D-3D 来源的准图像，使相机图像与地图视图可共享视觉特征和匹配器。
- 通过共同视觉接口建立点、线对应，并利用来源信息恢复度量 LiDAR 几何和线支持的平面约束，用于位姿估计。
- 提出分布感知、可观测性互补的优化策略，将候选关联分布传播为方向性位姿信息不确定性，并选择性增强能互补弱位姿方向的可靠结构因子。
- 摘要称在 EuRoC MAV 基准和自采集真实世界序列上，仅使用预建 LiDAR 地图作为持久先验，实现了准确的全局定位和鲁棒的连续 6-DoF 跟踪，包括严重光照变化和动态遮挡条件下。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算开销、对地图质量或环境结构的依赖程度，也未提供与基线方法的定量对比细节、消融实验细节以及自采集序列的规模与条件。上述内容均需以论文正文为准。

### 阅读优先级
高。理由：该论文直接针对 LiDAR 地图与视觉定位之间的模态差异问题，提出统一视觉关联和点-线-平面位姿估计框架，并涉及全局定位、连续 6-DoF 跟踪以及严重光照和动态遮挡下的鲁棒性；同时发表在 3D Reconstruction & Multi-view Geometry 与机器人/AR 相关分类下，对视觉定位、机器人导航和多模态地图复用方向具有较高潜在参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera localization in a prior LiDAR map provides a persistent geometric reference for long-term robotic navigation, yet remains challenging because of the substantial modality gap between camera images and point-cloud maps. We present a unified localization framework that makes the LiDAR map visually addressable rather than relying on a dedicated image-LiDAR correspondence model. Map geometry and reflectivity are rendered into LiDAR-derived quasi-images with explicit 2D-3D provenance, enabling camera observations and rendered map views to share mature visual features and matchers for both global localization and continuous pose tracking. Point and line correspondences are established through this common visual interface, while the retained provenance recovers metric LiDAR geometry and line-supported planar constraints for pose estimation. To improve robustness under ambiguous associations and weak geometry, we further introduce a distribution-aware, observability-complementary optimization strategy. Instead of reducing matching ambiguity to a scalar confidence, candidate association distributions are propagated into directional pose-information uncertainty, and reliable structural factors are selectively reinforced according to their ability to complement the currently weak pose directions. Experiments on the EuRoC MAV benchmark and self-collected real-world sequences demonstrate accurate global localization and robust continuous 6-DoF tracking using only a pre-built LiDAR map as the persistent prior, including under severe illumination variations and dynamic occlusions.

</details>

#### 2026-09-22 - GTR: Gated Token Recurrence for Efficient Dense Prediction

**Authors:** Zhe Feng, Longfei Liu, Wei Liu, Kai Chen, Jiangang Kong, Wei Zhou, Yifeng Qian, Dexiong Chen, Xuanlong Yu, Xi Shen
**Links:** [abs](https://arxiv.org/abs/2609.26590) - [pdf](https://arxiv.org/pdf/2609.26590)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GTR: Gated Token Recurrence for Efficient Dense Prediction
- 作者：Zhe Feng, Longfei Liu, Wei Liu, Kai Chen, Jiangang Kong, Wei Zhou, Yifeng Qian, Dexiong Chen, Xuanlong Yu, Xi Shen
- 出版日期：2026-09-22T15:34:20Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2609.26590) / [PDF](https://arxiv.org/pdf/2609.26590)

### 一句话总结
论文提出 GTR——一种无需 softmax、基于门控线性注意力与交替空间扫描方向的循环视觉骨干，用于在高分辨率密集预测中替代全局 softmax 注意力，并报告了在 COCO 检测与多任务迁移上的精度及延迟结果。

### 研究问题
基于自注意力的视觉骨干在密集预测任务上表现良好，但全局 softmax 注意力的二次计算成本随图像分辨率增大而限制其效率。论文关注的问题是：能否用循环式的 token 混合机制，作为全局 softmax 注意力的高效替代方案，服务于高分辨率密集预测与边缘部署。

### 核心思路/方法
- 提出 Gated Token Recurrence（GTR），一种 softmax-free 的循环视觉骨干。
- 方法组合了三个要素：门控线性注意力、交替空间扫描方向、以及空间增强的 SwiGLU 模块。
- 训练上采用蒸馏策略：从一个面向检测专门化的 DINOv3 教师模型中蒸馏，仅使用最终层 patch-token 对齐，通过线性投影和平方 ℓ2 损失实现；不使用 masked-token prediction，也不使用中间层监督。
- 使用 Objects365 检测器预训练。
- 实现层面提供了专门的 chunkwise CUDA 算子，并涉及编译 FP16 执行与 TensorRT 部署。

### 主要贡献
- 提出 GTR 这一无需 softmax 的循环视觉骨干，将门控线性注意力、交替空间扫描方向与空间增强 SwiGLU 结合，用于高效密集预测。
- 给出一种简化的蒸馏方案：仅依赖最终层 patch-token 对齐（线性投影 + 平方 ℓ2 损失），无需 masked-token prediction 与中间层监督。
- 在 Objects365 检测器预训练后，GTR-L 在 COCO val2017 上达到 58.9 box AP，并在 RTX 4090 编译 FP16 执行下报告 1.908 ms 的 batch-one 中位延迟。
- 同一骨干可迁移至实例分割、姿态估计、旋转检测、语义分割与单目深度估计。
- 在 RTX 4090、1.6K tokens 的孤立 kernel 基准中，专用 chunkwise CUDA 算子比 FLA v0.5.0 快 4.0 倍。
- 在 DRIVE AGX Thor 上的 TensorRT 部署中，所评估模型达到 2.282–8.769 ms 的 batch-one 中位延迟。

### 局限性
- 摘要未提供足够信息说明各迁移任务的具体精度表现、对比基线设置、数据集规模与训练细节。
- 摘要未提供足够信息说明 GTR 在不同分辨率、不同硬件或不同 token 长度下的完整效率曲线与 scaling 行为。
- 摘要未提供足够信息说明蒸馏方案与 masked-token prediction 或中间层监督方案的消融对比。
- 摘要未提供足够信息说明方法在非检测类密集预测任务上是否同样需要 Objects365 检测器预训练。
- 摘要未提供足够信息说明与全局 softmax 注意力骨干在同等精度下的系统性效率对比。
- 主分类标注为 3D Reconstruction & Multi-view Geometry，但摘要未提供足够信息说明该工作与三维重建或多视图几何的直接关联。

### 阅读优先级
中。理由：论文主题（高效密集预测骨干、softmax-free 循环 token 混合、边缘部署延迟）具有明确的工程与应用价值，且摘要给出了具体 AP 与延迟数字，便于快速判断相关性；但摘要未涉及具体任务精度细节、消融与完整实验设置，若关注三维重建或多视图几何方向，则需进一步确认其相关性。

</details>

<details>
<summary>Abstract</summary>

Self-attention-based vision backbones perform well on dense prediction, but the quadratic computational cost of global softmax attention limits their efficiency as image resolution increases. We introduce Gated Token Recurrence (GTR), a softmax-free recurrent vision backbone that combines gated linear attention, alternating spatial scan directions, and spatially enhanced SwiGLU blocks. GTR is distilled from a detection-specialized DINOv3 teacher using only final-layer patch-token alignment through a linear projection and squared $\ell_2$ loss, without masked-token prediction or intermediate-layer supervision. With Objects365 detector pre-training, GTR-L achieves 58.9 box AP on COCO \texttt{val2017} with 1.908\,ms median batch-one latency under compiled FP16 execution on an RTX~4090. The same backbone also transfers to instance segmentation, pose estimation, oriented detection, semantic segmentation, and monocular depth estimation. In an isolated kernel benchmark, our specialized chunkwise CUDA operator is $4.0\times$ faster than FLA v0.5.0 at 1.6K tokens on RTX~4090. TensorRT deployment on DRIVE AGX Thor achieves 2.282--8.769\,ms median batch-one latency across the evaluated models. These results show that recurrent token mixing can provide an efficient alternative to global softmax attention for high-resolution dense prediction and edge deployment. Project page: https://intellindust-ai-lab.github.io/projects/GTR/

</details>

#### 2026-09-22 - Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation

**Authors:** John Church, Vazghen Nikolian
**Links:** [abs](https://arxiv.org/abs/2609.26561) - [pdf](https://arxiv.org/pdf/2609.26561)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation
- 作者：John Church, Vazghen Nikolian
- 出版日期：2026-09-22T15:13:44Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2609.26561 ；PDF https://arxiv.org/pdf/2609.26561

### 一句话总结
该工作用大规模自监督 ViT 基础模型（DINOv3）替换此前较小的卷积/ViT 编码器，在仅用合成数据训练的条件下提升了已知非合作航天器的单目位姿估计精度，并给出面向嵌入式推理的实测结果。

### 研究问题
如何在已知、非合作航天器的单目位姿估计任务中，进一步提升旋转误差精度，同时保持仅使用合成数据训练，并验证大模型在具备在轨飞行历史的处理器族上的嵌入式推理可行性。

### 核心思路/方法
- 沿用此前已建立的基于热力图的位姿估计架构。
- 将此前工作中较小的卷积编码器和 ViT 编码器替换为大型自监督 ViT 基础模型 DINOv3，并进行适配。
- 模型规模从 300M 扩展到 840M 参数，且作者称尚未观察到饱和。
- 最佳模型配置：以 LoRA 适配的 DINOv3 840M 作为编码器（rank 64），采用三随机种子集成与四旋转测试时增强。
- 在 Jetson Orin NX 16GB 上评估 840M 模型，测量单次网络前向推理时间与整板功耗。

### 主要贡献
- 报告了作者所知在 SPEED+ lightbox 和 sunlamp 测试集上、针对已知非合作航天器的最低平均旋转误差。
- 显示从 300M 到 840M 参数扩展带来位姿估计精度提升，且尚未观察到饱和。
- 给出嵌入式推理实测：840M 模型在 Jetson Orin NX 16GB 上单次裁剪推理 133.8 ms，整板功耗 32.0 W，表明在具有在轨飞行历史的处理器族上具备嵌入式推理可行性。
- 仅用合成数据训练，在 lightbox 与 sunlamp 两个域上均优于此前模型。
- 具体结果：最佳模型在 sunlamp 上平均旋转误差 1.56°，在 lightbox 上 1.17°；对比此前已知最佳 EagerNet 的 2.66° 与 1.75°。

### 局限性
- 摘要未提供足够信息说明合成训练数据的具体来源、规模与生成方式。
- 摘要未提供足够信息说明模型在真实在轨数据或其他非 SPEED+ 数据集上的泛化表现。
- 摘要未提供足够信息说明功耗与推理时间之外的其他嵌入式资源占用（如内存）细节。
- 摘要未提供足够信息说明消融实验、失败案例或位姿估计中的平移误差表现。
- 仅报告旋转误差指标，摘要未提供足够信息说明完整六自由度位姿的评估情况。

### 阅读优先级
高。理由：该论文直接针对航天器单目位姿估计这一明确任务，报告了在公开测试集上相对此前最佳结果的显著旋转误差改进，同时覆盖“基础模型适配”与“嵌入式推理可行性”两个关键维度，且仅用合成数据训练，对航天视觉与资源受限部署方向具有较强参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards
- 作者：Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci
- 出版日期：2026-09-22T12:25:10Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.26315 ；PDF https://arxiv.org/pdf/2609.26315

### 一句话总结
ArborSplat 是一个面向果园场景的在线语义 3D Gaussian Splatting SLAM 系统，通过 LiDAR 里程计跟踪并在高斯地图上直接优化语义，以改善树干、棚架和果实等细小结构的语义建图效果。

### 研究问题
论文关注果园机器人建图需求：需要保留树干、棚架和果实等体积小但语义重要的结构。现有 3D Gaussian Splatting SLAM 虽然具有高光度保真度，但其优化仍以外观驱动为主；将图像语义迁移到 3D 点对细薄结构不可靠，因为这些结构的像素可能从背景表面获得深度。因此，问题在于如何在线构建兼具几何、外观与可靠语义的果园 3DGS 地图。

### 核心思路/方法
摘要给出的核心方法包括：
- 使用 LiDAR 里程计进行跟踪。
- 在高斯地图上直接优化语义。
- 使用类别特定的高度带约束，该高度带基于每个关键帧立体点云拟合出的地平面。
- 在线融合多视角证据为语义点云。
- 拒绝与局部地表面或单目深度不一致的标签。
- 采用类别约束细化，为代表性不足的结构保留高斯容量；在降低预算时，提高树木类别的训练视角准确率。

### 主要贡献
- 提出 ArborSplat，一个面向果园的在线语义 3DGS SLAM 系统，结合 LiDAR 里程计跟踪与高斯地图上的直接语义优化。
- 引入基于每个关键帧立体点云拟合地平面的类别特定高度带约束。
- 在线融合多视角语义证据为语义点云，并拒绝与局部地表面或单目深度不一致的标签。
- 通过类别约束细化为代表性不足结构保留高斯容量，并在降低预算下提升树木类别的训练视角准确率。
- 在苹果园和梨园的休眠期、开花期和采收期进行评估；完整路线上 12 次遍历的 ATE 均低于 0.5 m；在共享 301 帧片段上，相比 SGS-SLAM 和 GS3LAM 提升训练视角与留出集 mIoU，并运行更快；SemGauss-SLAM 在全部六个片段上出现 GPU 内存不足。

### 局限性
摘要未提供足够信息说明该方法的具体失败场景、适用范围限制、计算资源需求细节、对 LiDAR 或立体相机的依赖程度，以及在不同果园环境中的泛化边界。摘要仅提到 SemGauss-SLAM 在全部六个共享片段上 GPU 内存不足，但未说明 ArborSplat 自身是否存在类似内存或实时性限制。其他潜在局限摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对果园语义 SLAM 与 3DGS 结合中的细薄结构语义不可靠问题，提出在线语义优化、地平面高度带约束和多视角融合等具体机制，并包含跨物候期与多果园的定量比较；对农业机器人、语义建图和 3DGS SLAM 交叉方向具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：LiFR v2: Completion-Augmented Event Propagation for High-Rate Dense Prediction
- 作者：Tao Wan, Xiaoshan Wu, Yifei Yu, Bo Wang, Xiaoyang Lyu, Muxin Liu, Aoxuan Pan, Zhongrui Wang, Xiaojuan Qi
- 出版日期：2026-09-22T07:36:01Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类）；次要分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.25803 ；PDF https://arxiv.org/pdf/2609.25803

### 一句话总结
LiFR v2 提出了一个统一的“传播—补全—记忆”框架，从 RGB 关键帧与事件流进行因果式任意时刻与流式稠密预测，以缓解 RGB 低更新率与事件空间稀疏性带来的互补性利用不足问题。

### 研究问题
动态环境中的高帧率稠密感知受限于 RGB 相机的低更新率，因为帧间可能发生快速场景变化。事件相机提供时间上稠密但空间稀疏的测量，与空间稠密的 RGB 观测互补。然而，直接融合无法充分利用这种互补性；而事件引导的传播在无有效 RGB 支持的新出现区域或被遮挡后再出现（disocclusion）区域会失败。

### 核心思路/方法
论文提出的 LiFR v2 是一个统一的传播—补全—记忆框架，用于从一张 RGB 关键帧和事件流进行因果式任意时刻与流式稠密预测。具体包含两个模块：
- Event-Guided Completion Module (EGCM)：在传播不受支持的区域恢复任务相关表示。
- History Retrieval Module (HRM)：在连续查询之间复用已补全的表示。

该框架支持语义分割、单目深度估计与多任务稠密预测。论文还引入 SHF-Emerge 用于评估快速物体出现与去遮挡情况。

### 主要贡献
- 提出 LiFR v2，一个用于从 RGB 关键帧与事件进行因果式任意时刻及流式稠密预测的统一传播—补全—记忆框架。
- 引入 Event-Guided Completion Module (EGCM)，在传播不受支持处恢复任务相关表示。
- 引入 History Retrieval Module (HRM)，在连续查询间复用已补全表示。
- 框架支持语义分割、单目深度估计与多任务稠密预测。
- 提出 SHF-Emerge，用于评估快速物体出现与去遮挡。
- 在 DSEC 上达到 74.37% mIoU；在 SHF-Emerge 上达到 56.13% mIoU，相比 LiFR-Seg 提升 1.85 个百分点；在 SHF-Emerge 上将深度 RMSE 从传播基线的 1.564 m 降至 1.118 m。
- 分割与深度均超过 100 FPS，展示了超出 RGB 帧率的准确且高效的高帧率感知。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的具体失败情形、对特定数据集或硬件条件的依赖、计算资源需求、长期流式场景下的误差累积、事件噪声或传感器失配等潜在限制；也未提供 SHF-Emerge 的构建细节与统计特性。

### 阅读优先级
高。理由：该工作针对高帧率稠密感知中 RGB 低更新率与事件空间稀疏性的核心矛盾，提出明确的模块化解决方案，并在语义分割、单目深度估计与多任务稠密预测上报告了定量结果与超过 100 FPS 的效率指标；同时提出了新的评估设置 SHF-Emerge 以针对物体快速出现与去遮挡，这些内容对事件相机与稠密预测交叉方向具有直接参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning
- 作者：Dingkang Yang, Yizhou Liu, Wendong Cheng, Zizhi Chen, Shunli Wang, Yang Liu, Hongsheng Li, Lihua Zhang
- 出版日期：2026-09-22T06:22:31Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.25741) | [PDF](https://arxiv.org/pdf/2609.25741)

### 一句话总结
提出统一的视觉-语言-几何框架 Fysiverse-3D-Vision，从单张图像出发进行生成式 3D 场景重建，并将其空间布局推理与资产生成分离，以支持可执行 3D 内容的生成。

### 研究问题
从单张图像生成可控且可执行的 3D 场景仍具挑战性。现有 3D 生成方法虽能合成视觉上合理的物体与场景，但其空间布局估计与特定资产生成器相耦合，难以联合建模物体语义、度量几何与场景级空间关系——而这些对于交互式编辑、物理仿真和具身应用至关重要。

### 核心思路/方法
- 构建统一的视觉-语言-几何框架，用于单张图像的生成式 3D 场景重建与可执行资产构建。
- 建立共享表示，使空间推理与几何重建相互增强，从而让物体布局推断摆脱单个资产生成器的约束。
- 在统一 Transformer 中整合文本监督、语义视觉线索与几何表示，以捕捉场景上下文、度量几何和物体级交互。
- 设计物体条件布局模块，在目标物体表示与全局几何特征之间执行交叉注意力，预测物体的平移、旋转与尺度。
- 采用渐进式训练：先学习几何-语言对齐，再在保持重建能力的前提下引入布局推理，最后通过碰撞感知优化提升物理一致性。
- 通过将空间布局推理与资产合成分离，提供可适配接口，用于交互式场景编辑、物体级操作和可执行 3D 内容生成。

### 主要贡献
- 提出 Fysiverse-3D-Vision 框架，从单张图像生成 3D 场景，并解耦空间布局推理与资产合成。
- 通过共享表示与统一 Transformer 联合建模语义、度量几何与场景级空间关系，使布局推断不再受限于特定资产生成器。
- 引入物体条件布局模块与交叉注意力机制，显式预测物体的平移、旋转和尺度。
- 设计渐进式训练策略与碰撞感知优化，以提升物理一致性并保留重建能力。
- 提供面向交互式编辑与可执行 3D 内容生成的适配接口。

### 局限性
摘要仅声称在几何一致性、布局估计、渲染质量和物理属性理解方面优于现有方法，未给出具体实验设置、数据集、评价指标、失败案例或计算成本等信息。因此这些方面的局限性“摘要未提供足够信息”。

### 阅读优先级
中。理由：该工作聚焦单图到可执行 3D 场景的生成与布局解耦，问题设定与接口设计对 3D 重建、场景生成和具身应用方向有参考价值；但摘要未提供定量结果、数据集和实现细节，是否值得深入精读需结合正文实验与代码/补充材料进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Point Diffusion Mamba: Unified Diffusion-State-Space Modeling for Single-View 3D Reconstruction under Data Scarcity
- 作者：Wei Zhou, Xinzhe Shi, Xingxing Hao, Xing Hao, Kang Li, Jinye Peng, Ying He
- 出版日期：2026-09-22T01:11:24Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：abstract_url: https://arxiv.org/abs/2609.25538；pdf_url: https://arxiv.org/pdf/2609.25538；代码：https://github.com/NWUzhouwei/PDM

### 一句话总结
提出 Point Diffusion Mamba（PDM），将扩散模型的生成能力与状态空间模型的效率结合，用于数据稀缺条件下的单视图 3D 重建。

### 研究问题
单视图 3D 重建虽已有显著进展，但从本质上具有歧义的 2D 观测中推断复杂 3D 结构仍是根本性的不适定问题，在数据稀缺情形下尤为突出且研究不足。论文聚焦于数据稀缺条件下的单视图 3D 重建。

### 核心思路/方法
- 将扩散模型的生成能力与状态空间模型的效率相结合，形成面向数据稀缺单视图 3D 重建的方法 PDM。
- 采用轻量级重建模块处理无序点云输入。
- 结合 Local Geometric Aggregation 模块与 Mamba blocks，联合建模全局几何结构与局部细节。
- 针对 Mamba 模块提取的高层特征仅包含稀疏点的抽象语义信息、而重建中初始噪声输入的每个点都需要精确预测这一差距，引入 Hierarchical Feature Integration Network，将高层语义特征与局部几何特征逐点融合，以克服基于 token 的点云重建的局限。
- 提出 Dynamic Weighted Sampling 策略，利用生成先验自适应地统一 3D 生成与单视图重建，以提升重建质量。

### 主要贡献
- 提出 PDM，将扩散模型与状态空间模型统一用于数据稀缺条件下的单视图 3D 重建。
- 设计轻量级重建模块，并通过 Local Geometric Aggregation 与 Mamba blocks 联合建模全局几何结构和局部细节。
- 提出 Hierarchical Feature Integration Network，逐点融合高层语义与局部几何特征。
- 提出 Dynamic Weighted Sampling 策略，自适应统一 3D 生成与单视图重建。
- 在 ShapeNet 和 Pix3D 基准上实验，摘要称其优于现有最先进方法（具体指标与对比细节摘要未提供足够信息）。

### 局限性
- 摘要未提供足够信息说明方法的具体失败情形或适用边界。
- 摘要未提供足够信息说明数据稀缺的具体定义、数据规模范围及对数据稀缺程度的敏感性。
- 摘要未提供足够信息说明计算开销、推理速度或模型参数量等效率细节（虽提及状态空间模型的效率，但无定量说明）。
- 摘要未提供足够信息说明在 ShapeNet 和 Pix3D 上的具体评价指标、数值结果及消融实验细节。
- 摘要未提供足够信息说明 Dynamic Weighted Sampling 的具体实现方式与超参数敏感性。

### 阅读优先级
高。理由：该论文聚焦数据稀缺条件下的单视图 3D 重建这一研究不足且具有实际意义的问题，方法上融合扩散模型与状态空间模型（Mamba）并涉及点云重建、层次特征融合与动态加权采样等设计；同时提供公开代码，便于复现与进一步验证。但需注意，摘要未提供足够信息说明具体实验细节与定量结果，阅读全文时需重点核查实验设置与消融分析。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction
- 作者：Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi
- 出版日期：2026-09-20T18:36:29Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类）；摘要未提供足够信息说明次要分类
- 链接：摘要页 https://arxiv.org/abs/2609.23796 ；PDF https://arxiv.org/pdf/2609.23796

### 一句话总结
Mira-Scene 提出用像素对齐、有界的 Canonical Coordinate Map 替代稀疏位姿回归，从单图恢复密集对应关系以推断物体变换，并通过多模态扩散 Transformer 联合生成物体几何与 CCM，从而在无需场景级布局标注的情况下提升生成式 3D 场景重建的布局精度。

### 研究问题
单图 3D 物体生成已能产出高保真资产，但如何准确地把这些物体放入一个连贯的场景布局仍是未解决的挑战。核心困难在于物体布局的表示方式：
- 整体式方法把放置过程吸收进场景级生成，牺牲物体级细节；
- 组合式方法通过解耦几何与布局来保持物体保真度，但通常把布局参数化为稀疏、无界的位姿变量，难以学习，并且在场景级监督稀缺时泛化差。

### 核心思路/方法
- 用密集、有界的对应关系恢复，替代稀疏位姿回归。
- 核心是 Canonical Coordinate Map（CCM）：一个像素对齐的场，将每个可见物体像素映射到该物体有界规范空间中的表面坐标。
- 将 CCM 与来自单目几何估计的场景空间 Point Cloud Map（PCM）配对，诱导出密集的规范空间到场景空间的对应关系，再通过鲁棒几何对齐恢复物体变换。
- 由于 CCM 在有界规范空间中运作，它提供了稳定的预测目标，可从可扩展的物体级 3D 数据训练，无需场景级布局标注。
- 进一步引入多模态扩散 Transformer，联合生成物体几何与 CCM；使用模态特定的专家流，并共享注意力与位置编码，以促进几何—布局一致性。

### 主要贡献
- 提出 Mira-Scene，一个组合式 3D 场景重建框架，将布局表示从稀疏位姿回归转为密集、有界的对应关系恢复。
- 提出 Canonical Coordinate Map（CCM），作为像素对齐的有界规范空间场，并说明其与场景空间 Point Cloud Map 配对后可诱导密集对应关系以恢复物体变换。
- 提出可联合生成物体几何与 CCM 的多模态扩散 Transformer，采用模态特定专家流、共享注意力和位置编码来促进几何—布局一致性。
- 摘要报告在室内、室外、合成和自然场景（in-the-wild）实验中，布局精度显著优于强基线；相对 SAM3D，3D-IoU 提升 39.8%，2D-IoU 提升 16.5%，且使用有限的开源训练数据。

### 局限性
- 摘要未提供足够信息说明方法的失败案例、适用边界或具体限制条件。
- 摘要未提供足够信息说明对单目几何估计、物体级训练数据分布或计算成本的依赖程度。
- 摘要未提供足够信息说明“有限开源训练数据”的具体规模、基线设置细节及消融结果。

### 阅读优先级
高。理由：该论文针对单图生成式 3D 场景重建中“物体保真度与场景布局难以兼得”的关键矛盾，提出以有界像素对齐对应关系替代稀疏位姿回归，并给出 3D-IoU 与 2D-IoU 的量化提升；若关注组合式场景重建、布局表示学习或生成式 3D 资产放置，该工作具有直接相关性。

</details>

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

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-24 - Towards Practical Compression of 3D Gaussian Splatting

**Authors:** Pengpeng Yu, Yueru Chen, Fei Song, Tai Qin, Qi Zhang, Jing Wang, Yulan Guo
**Links:** [abs](https://arxiv.org/abs/2609.30245) - [pdf](https://arxiv.org/pdf/2609.30245)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D representations, increasing the complexity of training and coding. Meanwhile, floating-point context inference can introduce numerical inconsistencies across platforms, causing entropy-decoding failures. To address these practical challenges, we propose COSA-GS, which constructs context without spatial aggregation through anchor-wise causal factorization. Specifically, we use geometry context derived from each anchor's coordinates to model a compact learnable anchor latent. The anchor latent is then fused with the geometry context to form an anchor context for attribute coding. The resulting context model features a simple architecture composed solely of linear transformations and activations. We train COSA-GS using rate--distortion optimization with adaptive Gaussian pruning. Further, we develop quantization-aware training and integer inference for the context model to achieve bit-exact consistency of entropy-decoded symbols across platforms. Experiments demonstrate that COSA-GS achieves state-of-the-art compression performance while retaining fast and consistent cross-platform decoding, providing a simple yet effective framework for practical 3DGS compression. Code is available at https://github.com/pengpeng-yu/COSA-GS.

</details>

#### 2026-09-24 - M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis

**Authors:** Yang Zhou, Jiuhong Xiao, Shizhao Ye, Long Quang, Carlos Nieto-Granda, Giuseppe Loianno
**Links:** [abs](https://arxiv.org/abs/2609.30056) - [pdf](https://arxiv.org/pdf/2609.30056)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Robotic novel view synthesis (NVS) must recover both visual appearance and metric 3D structure, yet most generative NVS methods rely only on images, overlooking LiDAR, a complementary sensor common on robotic platforms. We present M3GD, a Camera--LiDAR multimodal representation for generative NVS that composes independently pretrained 2D image and 3D point-cloud foundation models without separately pretraining a cross-modal translator. We show that, after camera projection, frozen LiDAR and image features exhibit substantial shared spatial structure, providing a natural cross-modal representation. M3GD conditions generation on LiDAR through this structure: it combines explicit geometry statistics with learned point-cloud descriptors into view-aligned packets on the image-latent grid, injected through a lightweight residual adapter into a multi-view flow-matching generator whose latent space, decoders, and training objective remain intact. On the GrandTour dataset, M3GD improves target-view RGB and depth synthesis over an image-only version of the same backbone. Ablations show that the gains come from pixel-aligned LiDAR content and that target-view LiDAR acts as a geometric query linking the requested view to source observations. Deployment on a ground robot demonstrates practical real-world operation, with a configurable quality--cost trade-off controlled by the number of Euler integration steps.

</details>

#### 2026-09-24 - OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning

**Authors:** Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai
**Links:** [abs](https://arxiv.org/abs/2609.29985) - [pdf](https://arxiv.org/pdf/2609.29985)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Underwater 3D reconstruction is critical for marine exploration, ecological monitoring, and subsea infrastructure inspection, yet remains challenging at large scale due to light attenuation, scattering, and limited capture coverage. While 3D Gaussian Splatting (3DGS) enables high-quality real-time rendering, its application to large underwater scenes is constrained by high memory consumption and inefficient optimization over extensive areas. We propose OceanXL, a fast and scalable 3DGS-based framework for large-scale underwater reconstruction. OceanXL adopts a divide-and-conquer strategy, partitioning scenes into spatially coherent blocks to enable efficient optimization while preserving global geometric consistency. We further introduce an adaptive pruning scheme tailored to underwater conditions that removes redundant primitives, producing compact representations without sacrificing visual fidelity. Together, these components improve training efficiency and rendering performance for large scenes. We also introduce a large-scale underwater dataset covering diverse marine environments. Experiments on five large-scale scenes demonstrate favorable scalability, compactness, and efficiency--quality trade-offs over large-scene baselines. Controlled comparisons on the small-scale SeaThru-NeRF dataset further show competitive reconstruction quality with substantially smaller model sizes than underwater-specific methods.

</details>

#### 2026-09-24 - Shadow Reduction in Ultrasound Imaging Using Differentiable Simulation and Radiance Field Decomposition

**Authors:** Valentin Bacher, Pak Hei Yeung, Bernhard Kainz, Madeleine K. Wyburd, Nicola K. Dinsdale, Michael Gray, Ana I. L. Namburete
**Links:** [abs](https://arxiv.org/abs/2609.29373) - [pdf](https://arxiv.org/pdf/2609.29373)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, rendering, radiance, simulation

<details>
<summary>Abstract</summary>

Acoustic shadows from bone and other highly attenuating tissues obscure clinically important structures in ultrasound. In fetal brain imaging, skull-induced artefacts disproportionately degrade the hemisphere closer to the transducer (proximal), limiting symmetric assessment of the two hemispheres. Existing correction methods require raw scanner data, impose restrictive assumptions on tissue properties, or rely on generative models that may hallucinate anatomy. We present RFlash, a physics-informed post-processing method that decomposes beamformed ultrasound images into explicit attenuation and scatter-intensity maps using a differentiable radiance-field formulation of image formation. Attenuation-adaptive re-rendering then removes the dependence of the signal at each depth on the intervening tissue, equivalent to virtually advancing the transducer into the tissue. Across 1,261 3D fetal brain volumes, 143 real 2D curvilinear abdominal scans, and 1,200 simulated 2D linear-probe liver scans, RFlash reduces shadow-related intensity differences more effectively than classical Hughes-Duck attenuation correction. For a gestational-age model trained on the distal hemisphere (further from the transducer) and applied to the proximal hemisphere, prediction error decreases by 5.1 days (40%) relative to the original images. The estimated attenuation maps also yield shadow-confidence maps that improve random-forest bone-shadow segmentation over the image alone and receive greater SHAP importance than an existing neural confidence-map baseline, suggesting greater physical consistency. RFlash requires neither hardware modification nor access to raw scanner data and supports 2D and 3D acquisitions with linear and curvilinear probes, making it widely applicable allowing clinicians to use our method on their already acquired scanners and images.

</details>

#### 2026-09-24 - Only What Was Seen: Observation-Gram Compaction of View-Dependent Appearance in 3D Gaussian Splatting

**Authors:** Krzysztof Pietroszek
**Links:** [abs](https://arxiv.org/abs/2609.28997) - [pdf](https://arxiv.org/pdf/2609.28997)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Most of the memory of a 3D Gaussian Splatting model holds spherical-harmonic colour coefficients, yet each Gaussian is seen only from the narrow cone of directions of the training cameras. We turn this into a distortion metric that other compressors can adopt: a per-Gaussian observation Gram matrix, accumulated from viewing directions and blending weights, is the exact first-order map from coefficient changes to squared image error and needs only the model and the camera poses. Under it, degree reduction becomes a closed-form projection that generalises truncation, degree allocation a Lagrangian rate-distortion problem, and vector quantisation the matrix-weighted Lloyd algorithm, of which Compressed3D's quantiser is the scalar case. Swapped into Compressed3D with everything else unchanged, the metric raises PSNR by +0.49 dB before fine-tuning, with SSIM and LPIPS following, and at matched rate still gains +0.32 dB without a single training image. A training-free stack built on the metric alone is 15% smaller than the image-free GSICO at equal quality on Mip-NeRF 360.

</details>

#### 2026-09-24 - PlenoCI: Plenoptic CharacterIstics for View Dependence Aware Change Classification

**Authors:** Jason Lai, Chamuditha Jayanga Galappaththige, Niko Suenderhauf, Dimity Miller, Donald G. Dansereau
**Links:** [abs](https://arxiv.org/abs/2609.28930) - [pdf](https://arxiv.org/pdf/2609.28930)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting

<details>
<summary>Abstract</summary>

Radiance field representations such as 3D Gaussian Splatting (3DGS) natively encode complex visual phenomena such as occlusions and view dependence, but they are inherently underconstrained. Independently optimized reconstructions converge to different primitive configurations, even in unchanged regions. We introduce Plenoptic CharacterIstics (PlenoCI), a novel feature built from the plenoptic field these representations approximate. PlenoCI directly captures rich visual behaviors while ignoring Lambertian textures. By deriving closed-form analytic plenoptic derivatives from a 3DGS representation, we efficiently detect these 5D structures. Our approach is robust to underconstrained representations by construction, reporting two orders of magnitude fewer false positives between independent reconstructions of unchanged scenes than concurrent work. We demonstrate PlenoCI's utility on change classification. First, we detect changes with an instance-aware 3DGS pipeline, achieving state-of-the-art results on CL-Splats with a 25.7% mIoU gain over the strongest competitor, while remaining competitive on the more challenging PASLCD benchmark. Leveraging PlenoCI, we classify changes as geometric or appearance-based with a balanced accuracy of 0.735, comparable to the best performing baseline. We believe plenoptic derivatives and PlenoCI open new directions for view dependence aware understanding in visually complex environments. Code and data are available at https://js0n-lai.github.io/plenoci.

</details>

#### 2026-09-23 - RoomLight: A 2.5D Illumination Prior for Indoor Environments

**Authors:** Andreea Ardelean, Bernhard Egger
**Links:** [abs](https://arxiv.org/abs/2609.28300) - [pdf](https://arxiv.org/pdf/2609.28300)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, differentiable rendering, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoomLight: A 2.5D Illumination Prior for Indoor Environments
- 作者：Andreea Ardelean, Bernhard Egger
- 出版日期：2026-09-23T15:46:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.28300 ；PDF: https://arxiv.org/pdf/2609.28300 ；项目页：https://andreead-a.github.io/RoomLight

### 一句话总结
该论文提出 RoomLight，一种基于真实室内全景图及其估计深度训练的 2.5D 空间感知光照先验，用于改进室内逆渲染中的光照恢复。

### 研究问题
逆渲染等不适定逆问题需要先验来约束解空间。现有学习式光照先验多依赖“远距离光照假设”，即把光照表示为远场环境贴图。这种表示难以适用于室内场景，因为室内光照会由于有限距离发光体、可见性变化和视差而在空间上高度变化，单一环境贴图难以近似。

### 核心思路/方法
论文提出一种空间感知的光照先验，训练数据为真实世界室内全景图及其估计深度。该方法使用变分自编码器学习一个紧凑、可优化的潜空间，解码得到 HDR radiance 和深度，并将结果参数化为面光源发射器，从而可直接集成到标准可微渲染管线中。通过联合建模 radiance 与深度，该先验捕捉室内光照的空间结构，而不是把光源视为无限远。摘要称该设计在学习先验的合理性保证与下游优化所需梯度流之间建立联系，并支持空间变化的光照建模。

### 主要贡献
- 提出 RoomLight，一种面向室内环境的空间感知光照先验。
- 使用真实世界室内全景图及其估计深度进行训练。
- 采用 VAE 学习紧凑、可优化的潜空间，并解码为 HDR radiance 与深度。
- 将解码结果参数化为面光源发射器，可直接接入标准可微渲染管线。
- 通过联合建模 radiance 与深度，捕捉室内光照的空间结构，而非假设光源在无限远处。
- 摘要称该方法相比现有方法能实现空间变化光照建模，并获得更高保真度的室内光照恢复。

### 局限性
摘要未提供足够信息。未提供关于失败案例、计算成本、对深度估计误差的敏感性、泛化范围外场景能力、与具体基线方法比较细节等限制信息。

### 阅读优先级
中。理由：该工作聚焦室内逆渲染中的光照先验，针对远场环境贴图假设的不足提出 2.5D 空间感知建模，并强调可接入可微渲染管线，对神经渲染、逆渲染和室内光照建模方向具有相关性。但由于摘要未给出定量结果、基线细节与局限分析，是否值得优先精读取决于读者对室内光照先验与可微渲染结合的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Ill-posed inverse problems require priors to constrain the solution space toward plausible outcomes. In inverse rendering, learned priors modeling the distribution of natural illumination improve the recovery of scene properties. However, existing models rely on the distant-illumination assumption, representing lighting as a far-field environment map. This limits their applicability to indoor scenes, where illumination is highly spatially varying due to finite-distance emitters, visibility changes, and parallax, all of which are poorly approximated by a single environment map. To address this, we introduce a spatially-aware illumination prior trained on real-world indoor panoramas and their estimated depth. Our variational autoencoder model learns a compact, optimizable latent space that decodes into HDR radiance and depth, parameterizing an area light emitter for direct integration into standard differentiable rendering pipelines. This design bridges the plausibility guarantees of a learned prior with the gradient flow required for downstream optimization. Crucially, by jointly modeling radiance and depth, our prior captures the spatial structure of indoor illumination, instead of treating the light sources as infinitely distant. We demonstrate that this formulation enables spatially-varying illumination modeling and achieves higher-fidelity recovery of indoor lighting compared to existing approaches. Project page: https://andreead-a.github.io/RoomLight

</details>

#### 2026-09-23 - InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies

**Authors:** Sai Puneeth Reddy Gottam, Elmar Rueckert, Vedant Dave
**Links:** [abs](https://arxiv.org/abs/2609.27734) - [pdf](https://arxiv.org/pdf/2609.27734)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, scene representation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies
- 作者：Sai Puneeth Reddy Gottam, Elmar Rueckert, Vedant Dave
- 出版日期：2026-09-23T11:47:58Z
- 分类：Neural Scene Representations & Rendering（二级分类：摘要未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.27734) | [PDF](https://arxiv.org/pdf/2609.27734)

### 一句话总结
InfiNoVA 通过将多相机演示重建为时变 3D 高斯表示并渲染新视角观测，为 VLA 策略提供密集且几何一致的视角增强，从而提升其在未见视角下的操作成功率。

### 研究问题
视觉-语言-动作（VLA）策略往往强依赖训练时所见相机视角，导致在未见视角下部署时性能显著下降。从足够多样的物理视角采集演示成本高昂，且对视角空间的覆盖仍然稀疏。

### 核心思路/方法
- 将同步多相机演示转换为密集、几何一致的训练视角分布。
- 把每条操作轨迹重建为时变 3D 高斯表示。
- 从采样的相机位姿渲染新观测，同时保留原始状态-动作对应关系。
- 该显式场景表示旨在提升帧级保真度与时间一致性，并减少生成式新视角合成中出现的任务关键幻觉。

### 主要贡献
- 提出 InfiNoVA 数据增强框架，用于将同步多相机演示转化为密集的几何一致训练视角。
- 在四个真实世界操作任务中，使用 InfiNoVA 训练的策略在未见随机视角下平均成功率比 VISTA 基线增强和未增强策略高 5.4 倍。
- 相比直接在全部五个物理相机视角上训练，InfiNoVA 成功率再高 1.7 倍。
- 结果表明，密集且几何 grounded 的视角增强可在不修改底层策略架构的情况下提升机器人策略的相机鲁棒性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直面 VLA 策略在视角泛化上的关键痛点，提出了不改变策略架构的数据增强方案，并报告了在真实世界任务中相对多个基线的显著提升；问题重要、方法思路清晰、结果量化明确，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies often rely strongly on the camera viewpoints seen during training, causing substantial performance degradation when deployed from unseen perspectives. Collecting demonstrations from sufficiently diverse physical viewpoints is expensive and still provides only sparse coverage of the viewpoint space. We introduce InfiNoVA, a data-augmentation framework that converts synchronized multi-camera demonstrations into a dense distribution of geometrically consistent training views. InfiNoVA reconstructs each manipulation trajectory as a time-varying 3D Gaussian representation and renders novel observations from sampled camera poses while preserving the original state-action correspondence. This explicit scene representation improves frame-level fidelity and temporal consistency while reducing task-critical hallucinations observed in generative novel-view synthesis. Across four real-world manipulation tasks, policies trained with InfiNoVA achieve 5.4x higher average success under unseen randomized viewpoints than both VISTA-based augmentation and the unaugmented policy. InfiNoVA further achieves 1.7x higher success than training directly on all five physical camera views. These results show that dense, geometrically grounded viewpoint augmentation provides a practical route toward camera-robust robot policies without modifying the underlying policy architecture.

</details>

#### 2026-09-23 - GaussPDE: Graph-Based Partial Differential Equation-Driven Rendering for 3D Gaussian Splatting

**Authors:** Haoyuan Yue, Fengyuan Ye, Ziyin Li
**Links:** [abs](https://arxiv.org/abs/2609.27264) - [pdf](https://arxiv.org/pdf/2609.27264)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussPDE: Graph-Based Partial Differential Equation-Driven Rendering for 3D Gaussian Splatting
- 作者：Haoyuan Yue, Fengyuan Ye, Ziyin Li
- 出版日期：2026-09-23T02:48:35Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.27264) | [PDF](https://arxiv.org/pdf/2609.27264)

### 一句话总结
GaussPDE 在预训练 3D 高斯场景上直接构建高斯图并演化偏微分方程，通过修改球谐直流颜色系数实现稳定、可控且空间连贯的动态渲染，无需网格提取、体素化或重训练。

### 研究问题
如何在不进行网格提取、体素化或重训练的前提下，将物理结构化的偏微分方程动力学注入预训练的 3D 高斯场景，从而实现稳定、可控且空间连贯的动态可视化。摘要指出，PDE 渲染不仅需要准确的外观，还需要可靠的离散计算域。

### 核心思路/方法
- 在 3DGS 重建阶段引入相机感知正则化，抑制相机附近的浮动体和过大的基元，以避免它们造成不稳定的图拓扑。
- 使用协方差感知距离以及不透明度、外观和边界感知电导，构建活跃高斯图。
- 在高斯基元上直接进行质量加权的图拉普拉斯 PDE 演化。
- 将演化中的标量 PDE 状态耦合回渲染：修改球谐直流颜色系数，同时保持几何、不透明度和视角相关渲染行为。

### 主要贡献
- 提出 GaussPDE 框架，将物理结构化的 PDE 动力学注入预训练 3D 高斯场景，且无需网格提取、体素化或重训练。
- 指出 PDE 渲染依赖可靠的离散计算域，并通过相机感知正则化改善图拓扑稳定性。
- 构建基于协方差感知距离与多属性电导的活跃高斯图，实现质量加权图拉普拉斯 PDE 演化。
- 通过修改球谐直流颜色系数将 PDE 状态耦合到渲染，同时保持几何、不透明度和视角相关渲染行为。
- 在真实与合成场景上的实验显示，相较基线方法，GaussPDE 产生稳定、可控、空间连贯的动态可视化，并减少跨边界泄漏。

### 局限性
摘要未提供足够信息。摘要未说明方法的计算开销、对复杂拓扑或大幅形变的适用性、对超参数的敏感性、具体失败案例，也未提供定量指标细节。

### 阅读优先级
中。理由：该工作面向 3D Gaussian Splatting 与 PDE 驱动渲染的交叉方向，提出无需网格提取、体素化或重训练的动态渲染思路，并强调图拓扑稳定性与跨边界泄漏改善，对神经场景表示与渲染方向的研究者具有参考价值；但摘要未提供定量结果、计算成本与失败案例分析，实际价值需进一步阅读全文验证。

</details>

<details>
<summary>Abstract</summary>

We present GaussPDE, a framework that injects physically structured partial differential equation (PDE) dynamics into pretrained 3D Gaussian scenes without mesh extraction, voxelization, or retraining. Our key observation is that PDE rendering requires not only accurate appearance, but also a reliable discrete computational domain. We therefore first introduce camera-aware regularization during 3DGS reconstruction to suppress camera-near floaters and oversized primitives that would create unstable graph topology. We then construct an active Gaussian graph using covariance-aware distances and opacity, appearance, and boundary-aware conductance, enabling mass-weighted graph Laplacian PDE evolution directly over Gaussian primitives. The evolving scalar PDE state is coupled back to rendering by modifying the direct-current spherical harmonic color coefficients while preserving geometry, opacity, and view-dependent rendering behavior. Experiments on real and synthetic scenes show that GaussPDE produces stable, controllable, and spatially coherent dynamic visualizations, with reduced cross-boundary leakage compared with baselines.

</details>

#### 2026-09-22 - φ-RIE: From Photorealistic Reconstruction to Interactive Environments

**Authors:** Runyi Yang, Deheng Zhang, Xiaoye Wang, Kanzhi Wu, Lei Sun, Ajad Chhatkuli, Kunyu Peng, Luc Van Gool, Danda Pani Paudel
**Links:** [abs](https://arxiv.org/abs/2609.26795) - [pdf](https://arxiv.org/pdf/2609.26795)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：φ-RIE: From Photorealistic Reconstruction to Interactive Environments
- 作者：Runyi Yang, Deheng Zhang, Xiaoye Wang, Kanzhi Wu, Lei Sun, Ajad Chhatkuli, Kunyu Peng, Luc Van Gool, Danda Pani Paudel
- 出版日期：2026-09-22T17:59:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.26795) | [PDF](https://arxiv.org/pdf/2609.26795)

### 一句话总结
φ-RIE 是一个基于高斯表示的原生流水线，将 3DGS 重建场景中选定的物体转化为可移动的仿真资产，同时保留并补全其余重建内容，从而把照片级重建转变成可交互环境。

### 研究问题
3D Gaussian Splatting 虽能对捕获场景进行照片级重建，但其表示本身不支持物理交互。机器人仿真需要物体级别的变化，即物体能够独立移动、发生接触，并揭示此前被遮挡的周围环境。摘要指出该差距源于两点：物体外观可能与背景纠缠；隐藏的物体几何与被遮挡的背景内容可能未被观测到。

### 核心思路/方法
核心观察是：资产生成与源移除应当耦合，即同一个物体身份既定义可移动资产，也定义需要移除并补全的场景内容。φ-RIE 据此构建了一个 Gaussian-native 流水线：Scene Observation 为 Coupled Scene Construction 提供共享证据；后者创建已配准的资产，并生成补全后的背景高斯，用于 Interactive Environment 中由仿真器驱动的渲染。这种耦合在保持未编辑高斯不变的同时，对齐视觉状态与物理状态。

### 主要贡献
- 提出 φ-RIE，一个将选定物体转化为可移动仿真资产、同时保留其余重建内容的 Gaussian-native 流水线。
- 提出资产构建与源移除耦合的关键思路，由同一物体身份统一定义可移动资产及需移除和补全的场景内容。
- 通过 Scene Observation 与 Coupled Scene Construction 的共享证据，生成配准资产与补全背景高斯，支持交互环境中的仿真器驱动渲染。
- 在 50 个 ScanNet++ 场景上，基于证据的选择与配准重试在固定保留率下将 20 mm 的匹配 F1 从 0.336 提升至 0.383。
- 进一步的测试展示了资产可执行性、相较单一生成器基线的操作增益，以及转换的视觉代价。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败情形、适用场景边界、计算开销、对未观测区域补全质量的定量限制，也未给出关于泛化能力或依赖条件的明确局限陈述。

### 阅读优先级
中。理由：该工作面向 3DGS 与机器人仿真的交叉问题，提出从照片级重建到交互环境的转换框架，并给出 ScanNet++ 上的定量结果与额外测试，对神经场景表示、可交互场景构建和仿真资产生成方向有参考价值；但摘要未提供额外兴趣方向，且局限性与方法细节有限，是否高优先阅读取决于读者对 3DGS 物理交互与机器人仿真的具体需求。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models
- 作者：Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan
- 出版日期：2026-09-22T11:08:50Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.26007) / [PDF](https://arxiv.org/pdf/2609.26007)

### 一句话总结
论文提出 Skytopia：一种仅依赖前向单目相机、基于动作条件潜在世界模型的无人机导航策略，其核心主张是策略从世界模型中需要的是“能产生预测的表示”而非预测本身，因此在部署时丢弃预测器以降低推理成本，并统一支持点目标、图像目标与无目标导航。

### 研究问题
单目无人机导航要求在未见环境中，仅凭单个前向相机的输入到达目标，但这类输入对深度与尺度提供的线索很少。世界模型通过建模“观测如何在动作下演化”来应对该问题，但摘要指出这类方法通常是为部署执行而设计的：预测在部署时产生，并在每个控制步被反馈进行动生成。论文质疑这一范式的必要性，并试图回答：策略究竟需要世界模型的预测，还是产生该预测所需的表示？

### 核心思路/方法
- **核心论点**：在飞行中，已执行的动作几乎解释了观测之间的全部变化，因此预测可归约为“在已知位移下对静态场景的重投影”，策略真正需要的是支撑该预测的表示，而非预测结果本身。
- **方法构成**：提出 Skytopia，一个建立在动作条件潜在世界模型之上的策略；同时提出用于训练该策略的 3D Gaussian Splatting 平台。
- **双目标训练**：前向目标从意图运动预测下一观测的表示；逆向目标从预测的转移中恢复该运动。
- **部署设计**：由于预测不会进入动作生成环节，预测器在部署时被丢弃，从而降低推理开销；同一个策略可服务点目标、图像目标和无目标三种导航设定。
- **验证方式（摘要层面）**：仿真实验中在三类设定下均优于所有基线，成功率分别为 57.8%、66.0%、49.0%；丢弃预测器可去除 59.4% 的推理成本；同一策略随后在未微调的情况下部署到实体无人机，并在室内、开阔室外和林地环境中到达目标。

### 主要贡献
- 提出对世界模型在策略中作用的新观点：策略需要的是“用于产生预测的表示”，而非部署时的预测输出。
- 构建 Skytopia 策略，结合动作条件潜在世界模型与 3D Gaussian Splatting 训练平台，采用前向-逆向双目标学习。
- 在部署阶段丢弃预测器，实现 59.4% 的推理成本削减，同时不将预测反馈至动作生成。
- 用同一个策略统一支持点目标、图像目标与无目标三种导航规范。
- 仿真结果显示在三种设定下均超越所有基线；并在实体无人机上零微调部署，覆盖室内、开阔室外与林地环境。

### 局限性
摘要未提供足够信息。摘要未给出基线方法的具体构成、实验环境数量与规模、失败案例、实体部署的定量指标、3D Gaussian Splatting 平台的具体假设与依赖，也未讨论策略在动态场景、极端光照或相机标定误差下的表现与限制。

### 阅读优先级
高。理由：论文提出的“丢弃预测器、仅保留表示”的论点直接挑战世界模型在具身控制中的常见部署范式，并给出仿真成功率与推理成本削减的量化结果，还宣称在实体无人机上零微调跨室内外与林地部署。主题同时落在神经场景表示与具身/机器人导航的交叉点，对单目无人机导航与世界模型效率研究方向具有较强参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration
- 作者：Karim Slimani, Catherine Achard, Eric Marchand, Brahim Tamadazte
- 出版日期：2026-09-22T10:22:32Z
- 分类：主分类为 Neural Scene Representations & Rendering；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.25966 ；PDF https://arxiv.org/pdf/2609.25966

### 一句话总结
GRIP 提出一种基于位姿条件的细化框架，通过高斯特征泼溅将学习到的三维点特征柔和渲染到图像网格，并与图像特征在像素对齐的 Transformer 中融合，以改善像素到点匹配和 2D 到 3D 配准。

### 研究问题
论文关注图像到点云配准中的像素到点匹配与 2D 到 3D 配准问题。摘要指出其核心挑战在于基于网格的图像描述子与无序点云描述子之间存在结构不匹配。GRIP 在给定初始粗略位姿估计的条件下，试图缓解这种跨模态结构差异，并进一步细化配准结果。

### 核心思路/方法
- 输入设定：给定初始粗略位姿估计。
- 跨模态桥接：通过高斯特征泼溅，将学习到的三维点特征柔和渲染到图像网格上，得到由点云派生的特征图。
- 特征融合：将渲染得到的点云派生特征图与图像特征通过像素对齐的 Transformer 进行融合，使视觉语义线索和几何线索在共享的二维表示中交互。
- 解码与传播：对细化后的特征进行解码，并传播到更细分辨率，用于密集对应估计和最终位姿细化。
- 输出目标：像素到点匹配以及最终的 2D 到 3D 配准位姿细化。

### 主要贡献
- 提出 GRIP，一个位姿条件下的细化框架，用于像素到点匹配和 2D 到 3D 配准。
- 使用高斯特征泼溅作为跨模态桥梁，将无序点云特征渲染到图像网格，以缓解图像网格描述子与无序点云描述子之间的结构不匹配。
- 通过像素对齐 Transformer 融合渲染的点云派生特征图与图像特征，在共享二维表示中实现视觉语义与几何线索的交互。
- 将细化特征解码并传播到更细分辨率，用于密集对应估计和最终位姿细化。
- 在 RGB-D Scenes V2 和 7 Scenes 上报告了 state-of-the-art 的 inlier ratio 和具有竞争力的 registration recall，并在更严格评估阈值下表现更强。

### 局限性
- 摘要未提供足够信息说明方法对初始粗略位姿估计质量的敏感程度或失败情形。
- 摘要未提供足够信息说明计算开销、实时性、内存占用或高斯泼溅与 Transformer 融合带来的复杂度。
- 摘要未提供足够信息说明在 RGB-D Scenes V2 和 7 Scenes 之外的泛化能力。
- 摘要未提供足够信息说明消融实验、各模块具体贡献或超参数影响。
- 摘要未提供足够信息说明是否依赖特定传感器、标定质量或训练数据规模。
- 摘要未提供足够信息说明与基线方法在具体指标数值上的差距。

### 阅读优先级
中。理由：该论文主题属于图像到点云配准与神经场景表示/渲染的交叉方向，核心方法将高斯特征泼溅用于跨模态特征对齐，并声称在 inlier ratio 和严格阈值下表现较强，对相关领域读者有参考价值。但摘要未提供具体实验数值、消融细节、计算成本或失败案例分析，且兴趣方向未额外指定，因此不适合无条件列为高优先级；若读者关注 2D-3D 配准、跨模态特征融合或高斯泼溅应用，可提升为高优先级。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：NaCR: Visual Localization via NeRF-aided Camera Ray Regression
- 作者：Yesheng Zhang, Xiang Dai, Xu Zhao, Chongyang Zhang
- 出版日期：2026-09-22T09:13:21Z
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2609.25907 ；PDF https://arxiv.org/pdf/2609.25907

### 一句话总结
论文提出 NaCR，将 NeRF 与相机光线回归（CRR）在光线层级统一起来，通过增强 CRR 基线、利用预训练 NeRF 合成新视角数据、以及将渲染光度误差反传以优化预测光线，并用两阶段训练课程保证收敛，以提升视觉定位精度。

### 研究问题
视觉定位（Visual Localization, VL）是虚拟现实等视觉应用的基础技术。近年出现的“相机光线回归”（Camera Ray Regression, CRR）范式将 2D 图像块映射到 3D 相机光线，但其精度有限。论文要解决的问题是如何提升 CRR 的定位精度。

### 核心思路/方法
作者观察到一种互补的对偶关系：CRR 从图像块预测光线，而 NeRF 的新视角合成恰恰执行该映射的逆过程——通过可微的光线步进从相机光线渲染图像块。基于这一互补关系，论文提出 NaCR（NeRF-aided Camera Ray Regression），一个在光线层级无缝连接 NeRF 与 CRR 的统一框架，具体包含三部分：
1. 在 CRR 基线上引入三项简单而有效的增强；
2. 利用预训练 NeRF 合成新视角，为高效的图像块级消费定制增强训练数据；
3. 利用 NeRF 的可微性，构建闭环监督流程，将光度渲染误差反向传播以优化预测的相机光线。
此外，为在高度非凸的图像空间中保证稳定收敛，论文引入两阶段训练课程。

### 主要贡献
- 提出 NaCR，一个在光线层级统一 NeRF 与 CRR 的框架，利用二者的对偶互补关系提升视觉定位精度。
- 在 CRR 基线中加入三项简单有效的增强。
- 利用预训练 NeRF 合成面向图像块级消费的新视角数据以增强训练。
- 构建基于 NeRF 可微性的闭环监督流程，用光度渲染误差反传优化预测光线。
- 引入两阶段训练课程以保证在高非凸图像空间中的稳定收敛。
- 在室内与室外基准上进行大量实验，表明 NaCR 取得有竞争力的精度；消融研究验证了各组件的有效性。

### 局限性
摘要仅说明在室内外基准上取得“有竞争力的精度”，未给出具体精度数值、对比方法、实验设置与失败案例；三项 CRR 增强的具体内容、两阶段训练课程的细节、以及闭环监督的收敛性分析均未提供。摘要未提供足够信息说明方法的适用范围限制、对预训练 NeRF 质量的依赖程度以及在真实场景中的泛化表现。

### 阅读优先级
**中**。理由：论文主题属于神经场景表示与渲染、视觉定位的交叉方向，将 NeRF 的可微渲染用于监督相机光线回归的思路具有一定新颖性，且涉及 VR/机器人/AR 等应用场景，对该方向读者有参考价值。但摘要仅给出方法框架与结论性表述，缺少定量结果与实现细节，无法从摘要判断其相对现有方法的实际提升幅度，因此优先级定为中而非高；若读者专攻视觉定位或 NeRF 应用，可适当上调关注度。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking
- 作者：Edward Beng Wai Tan, Siew-Kei Lam
- 出版日期：2026-09-22T06:35:43Z
- 分类：Neural Scene Representations & Rendering（主类）；3D Reconstruction & Multi-view Geometry（次类）
- 链接：摘要页 https://arxiv.org/abs/2609.25746 ；PDF https://arxiv.org/pdf/2609.25746

### 一句话总结
该论文提出双协方差参数化的 3D 高斯泼溅 SLAM，让渲染与配准分别使用不同的协方差，以缓解同一协方差在两类任务中的需求冲突，并提升实时跟踪鲁棒性。

### 研究问题
在基于 ICP 的 3D Gaussian Splatting SLAM 中，传入帧需要与地图高斯进行配准，而每个高斯的协方差同时被用于渲染和配准。摘要指出，这两种用途对协方差的要求相互冲突：建图器为最小化光度误差会将其压平贴向表面，而鲁棒配准通常更受益于测量不确定性。论文要解决的核心问题即是如何在同一高斯表达中消解这一冲突，从而兼顾渲染优化与鲁棒跟踪。

### 核心思路/方法
论文提出一种“双协方差”参数化：每个高斯保留单一均值，但持有两个协方差——一个是由建图器优化的渲染协方差，另一个是由 RGB-D 传感器噪声模型导出的跟踪协方差。此外，作者将跟踪协方差用作图像角点的高斯锚点，为深度几何较弱的方向提供约束。方法面向实时跟踪，摘要称其跟踪速度约为 60 FPS。

### 主要贡献
- 提出双协方差参数化，将渲染协方差与跟踪协方差解耦，使同一高斯可同时服务渲染优化与配准需求。
- 引入由 RGB-D 传感器噪声模型导出的跟踪协方差，用于配准而非渲染。
- 将跟踪协方差作为图像角点的高斯锚点，在深度几何较弱的方向上补充约束。
- 在 TUM RGB-D、ScanNet、Replica 以及两段由 RealSense D435i 在轮式和手持平台录制的户外序列上进行评估。
- 摘要报告了跨多个场景的鲁棒跟踪性能和降低的里程计漂移，并保持约 60 FPS 的跟踪速度。

### 局限性
- 摘要未提供足够信息说明双协方差相比单协方差在计算或内存上的额外开销。
- 摘要未提供足够信息说明具体指标数值、各数据集上的逐项结果或消融实验。
- 摘要未提供足够信息说明退化场景、动态场景或极端光照条件下的失败模式。
- 摘要未提供足够信息说明跟踪协方差所依赖的 RGB-D 噪声模型的具体形式与参数来源。
- 摘要未提供足够信息说明与现有 3DGS SLAM 方法的详细对比结论。
- 摘要未提供足够信息说明该方法的适用传感器范围是否仅限 RGB-D。

### 阅读优先级
中。理由：论文针对 3DGS SLAM 中渲染与配准共用协方差的明确冲突提出解耦方案，问题表述清晰，且报告了约 60 FPS 的实时性与跨多数据集评估，对关注 3DGS SLAM、实时跟踪和 RGB-D 里程计的研究者具有参考价值。但摘要未给出具体定量结果、对比方法和消融细节，是否真正带来显著且稳健的改进需进一步阅读正文验证，因此不直接列为高优先级。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Ultra-fast Neural Inference for Stochastic Gaussian Splatting Denoising
- 作者：Chenxiao Hu, Hao Zhang, Yanchen Zhang, Meng Gai, Guoping Wang, Sheng Li
- 出版日期：2026-09-22T02:51:29Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.25604 ；https://arxiv.org/pdf/2609.25604

### 一句话总结
该论文针对随机高斯泼溅渲染中因去除排序与 alpha 混合而引入的空间噪声，提出了一种时序神经去噪器，以在保持无排序、无混合光栅化性能的同时获得时间稳定且视觉可用的输出。

### 研究问题
随机渲染消除了高斯泼溅中的排序和 alpha 混合过程，但代价是引入空间噪声。论文关注的问题是：如何对视图一致的随机泼溅渲染器共享的像素流进行时序去噪，从而在自由相机导航时抑制噪声并获得时间稳定、视觉上令人满意的输出，同时不牺牲无排序、无混合光栅化带来的性能优势。

### 核心思路/方法
论文将时序去噪建模在视图一致的随机泼溅渲染器共享的像素流上，并在随机 2D 高斯泼溅渲染上验证所提出的时序神经去噪器。该方法组合了以下组件：
- 双路径指数移动平均累积；
- 逐像素学习到的信任预测，用于历史验证；
- 固定的各向异性空间滤波器；
- 带稳定化的方差门控合成。

### 主要贡献
- 提出了一种面向随机高斯泼溅渲染的时序神经去噪器，用于处理随机渲染引入的空间噪声。
- 在随机 2D 高斯泼溅渲染上验证了该去噪器。
- 方法结合了双路径指数移动平均累积、逐像素学习信任预测、固定各向异性空间滤波以及方差门控合成与稳定化。
- 去噪器能够在自由相机导航期间抑制噪声，产生时间稳定、视觉上 compelling 的输出，同时保留无排序、无混合光栅化性能。
- 组合流水线相对于排序 alpha 混合渲染器仍保留 PSNR 差距，但去噪器的开销低于移除排序和混合所节省的时间。

### 局限性
- 组合流水线相对于排序 alpha 混合渲染器仍存在 PSNR 差距。
- 摘要未提供足够信息说明具体实验数据集、评价指标数值、消融实验细节、不同场景下的泛化能力以及失败案例。
- 摘要未提供足够信息说明该方法是否适用于随机 2D 高斯泼溅之外的其它随机泼溅渲染设置。
- 摘要未提供足够信息说明训练成本、推理硬件条件以及实时性能的具体量化结果。

### 阅读优先级
中。理由：该工作针对随机高斯泼溅渲染去噪这一具体问题，提出了包含历史验证、空间滤波和方差门控合成的时序神经去噪方案，并强调去噪开销低于去除排序与混合节省的时间，具有明确的系统性能取向。但摘要未给出具体实验数据、对比细节和泛化范围，若读者关注随机高斯泼溅渲染、无排序无混合光栅化或时序神经去噪，则值得进一步阅读；若仅关注成熟高斯泼溅管线的通用改进，则优先级相对有限。

</details>

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

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-24 - Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage

**Authors:** Yuncong Yang, Jinlong Li, Yulong Xue, Feng Wu, Chunwen Zhang, Lei Qiao, Xuyang Wang
**Links:** [abs](https://arxiv.org/abs/2609.30214) - [pdf](https://arxiv.org/pdf/2609.30214)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>Abstract</summary>

We present Underwater C$^{3}$-JEPA (cross-view, control-conditioned, context-extended), an object-centric multi-view predictive world model for near-field heavy-load underwater ROV salvage. Without contact sensors, it predicts in latent space how the task-object state evolves through contact interaction and under the hydrodynamic lag of the vehicle, from synchronized multi-view RGB observations and vehicle control signals. C$^{3}$-JEPA encodes multi-camera observations into task-object and context tokens, fuses cross-camera evidence through held-out-view attention, and directly predicts future states conditioned on control. Weak binding anchors the target and gripper at low annotation cost, while SIGReg sharpens the geometric representation. Experiments show that the learned representation transfers substantially more task-relevant information to downstream probes than a reconstruction-free latent baseline, while keeping the predictor lightweight. The resulting predictive interface supports model-predictive-control (MPC) candidate evaluation and imagined-rollout behavior-agent training. Validation on real underwater video shows the same architecture recovering a withheld camera's object state and staying ahead of persistence, so the recipe transfers beyond simulation.

</details>

#### 2026-09-24 - S2Planner: Multi-Scale Semantic Planner for End-to-End Autonomous Driving

**Authors:** Zhaowei Lu, Liguo Zhou, Yujie Guo, Lei Yu, Alois Knoll
**Links:** [abs](https://arxiv.org/abs/2609.29813) - [pdf](https://arxiv.org/pdf/2609.29813)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

We present S2Planner, a trajectory planner that combines three front-facing cameras with ego-motion history and the current driving command. A fine-tuned DINOv3 backbone and a Spatial Tuning Adapter produce multi-scale image features; a coarse-to-fine decoder then uses trajectory self-attention and camera-projected cross-attention to refine candidate waypoints. The contribution is the integration of ego-conditioned trajectory initialization with iterative, geometry-guided sampling of multi-scale image features, rather than a new visual backbone or attention operator. On the NAVSIM v1 non-reactive evaluation, the previously reported navtest run obtained 88.03 PDMS. Because that run was selected using navtest performance, this number is exploratory and cannot be interpreted as an unbiased test estimate. Validation-selected evaluation on unexposed data, repeated runs, and computational measurements are needed to establish generalization and efficiency.

</details>

#### 2026-09-24 - Frame-to-Panorama Localization and Context-Aware Sampling for Scene-Specific Ship Detection in a Smart Marina Testbed

**Authors:** Ignat Romanov, Andreas Hadjipieris, Neofytos Dimitriou
**Links:** [abs](https://arxiv.org/abs/2609.29447) - [pdf](https://arxiv.org/pdf/2609.29447)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, digital twin

<details>
<summary>Abstract</summary>

Smart maritime infrastructures provide continuous access to heterogeneous sensing streams, enabling repeated experimentation, digital-twin development, and AI-based maritime services. However, sensing hardware alone is not sufficient for scene-specific model development: historical video streams must also be spatially indexed, contextualized, and reduced to informative subsets for annotation. This paper presents a frame-to-panorama localization and context-aware sampling pipeline for ship detection in historical PTZ maritime video lacking reliable pan, tilt, and zoom metadata. The main contribution is an end-to-end data-curation approach that recovers camera-view information from historical PTZ video and combines it with environmental context and visual diversity to construct compact, scene-specific training sets. Specifically, frames are localized on a reference panorama using SuperPoint and LightGlue, enriched with weather and solar-state metadata, and selected through diversity sampling to preserve variation across camera view and environmental conditions. A second context-aware stage targets under-represented distant-vessel cases near the horizon using tile-level visual embeddings and Gaussian Mixture Model clustering. Applied within the CMMI MDigi-I Smart Marina testbed, the proposed pipeline reduces 40,718 candidate frames to 220 images for annotation, corresponding to a 99.5% reduction. A YOLO26-m detector fine-tuned on this subset achieves a mean AP50 of 94.78% $\pm$ 0.51% and a mean AP50-95 of 75.10% $\pm$ 1.73% under sequence-grouped five-fold cross-validation. These results demonstrate that highly redundant infrastructure video streams can be transformed into compact, spatially and contextually diverse training sets for scene-specific detector adaptation while substantially reducing annotation effort.

</details>

#### 2026-09-24 - Assessing the Impact of Fleet Size on Crowdsourced Mapping Using a Dissimilarity Measure

**Authors:** Marie-Ngoïe Badibanga Kalenda, Philippe Bonnifait, Marie-Anne Mittet
**Links:** [abs](https://arxiv.org/abs/2609.29198) - [pdf](https://arxiv.org/pdf/2609.29198)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping, localization, simulation

<details>
<summary>Abstract</summary>

Accurate digital maps are essential for Advanced Driver Assistance Systems (ADAS) or Autonomous Driving (AD), providing critical information such as road geometry, traffic signs and speed limits required by safety functions including Intelligent Speed Assistance (ISA). Maintaining these map layers using traditional surveying methods is costly and difficult to scale. Crowdsourced approaches based on fleets provide a promising alternative for continuously validating and updating map information. However, the relationship between the number of contributing vehicles and the quality of the resulting map remains poorly understood. To address this gap, this paper presents a simulation-based framework for evaluating crowdsourced traffic sign maintenance using a dissimilarity measure called GOSPAM (Generalized Optimal SubPattern Assignment for Maps), which combines localization errors with detection performance by accounting for False Positives (FP) and False Negatives (FN). The proposed system models multivehicle observations with representative sensor noise, detection errors, and semantic recognition uncertainties. Observations from multiple vehicles are aggregated using spatial clustering and semantic filtering to estimate traffic sign locations. Using simulated trajectories generated from data carried out by an experimental vehicle in an area containing ground-truth traffic signs, we assess the influence of fleet size on the performance of crowdsourced mapping. The number of vehicles ranges from 5 to 50, and performance is analyzed using standard evaluation metrics which are compared to the GOSPAM . The results show that GOSPAM can be used to effectively assess the quality of crowdsourced mapping, such as the contributions made by the first vehicles or the improvements made by numerous vehicles.

</details>

#### 2026-09-24 - Representation World Model: Learning States, Transition and Executable Plans in Representation

**Authors:** Yijun Yuan, Weicheng Zheng, Weibang Wang, Minghui Qin, Chang Sun, Junhao Huang, Kenan Li, Anmin Liu, Yicheng Yao, Hang Zhao
**Links:** [abs](https://arxiv.org/abs/2609.29171) - [pdf](https://arxiv.org/pdf/2609.29171)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>Abstract</summary>

We propose the Representation World Model (RWM), which learns states, transitions, and executable plans directly in representation space. Unlike existing world models that typically learn latent representations together with explicit dynamics models and perform planning through search, optimization, or policy-based prediction, RWM directly incorporates planning into the learned representation geometry. RWM learns the representation geometry by applying inverse-dynamics supervision locally along latent paths constructed from endpoint representations, requiring these paths to preserve task-relevant state and transition information. At inference, planning is performed by directly constructing a latent path between the current and goal representations, with inverse dynamics used to recover the corresponding actions, without recursive rollouts or action-space search. Experiments on continuous-control benchmarks demonstrate the effectiveness of RWM for direct planning, while results on robotic manipulation further show its potential to extend to more complex embodied control tasks. These results suggest that planning directly in representation space provides a promising alternative to conventional world-model planning.

</details>

#### 2026-09-24 - ReVNM: Learning-Based Visual Navigation from a Remote Camera

**Authors:** Michikuni Eguchi, Kohei Honda, Masafumi Endo, Yasuhiro Yoshimura, Ryo Yonetani
**Links:** [abs](https://arxiv.org/abs/2609.28976) - [pdf](https://arxiv.org/pdf/2609.28976)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, localization, simulation

<details>
<summary>Abstract</summary>

Visual Navigation Models (VNMs) enable robots to navigate from egocentric visual observations without geometric localization and planning, but long-range navigation still requires pre-built maps. This paper presents the Remote Visual Navigation Model (ReVNM), which uses a single remote surveillance camera to serve as both an observation source and an implicit environmental map for visual navigation. While the use of remote cameras could eliminate the need for pre-built maps as well as onboard vision processing, their limited field of view instead of egocentric observations makes it hard to achieve collision-free navigation. The lack of existing data with diverse remote viewpoints, which are crucial for training robust VNMs, further complicates the challenge. In this work, we propose a learning-by-synthesis approach to address this two-fold challenge. Our ReVNM extends a state-of-the-art VNM architecture with an exocentric-to-egocentric (exo2ego) module that predicts an egocentric depth observation from remote-camera observations. This helps the VNM to plan a path while considering obstacles in front of the robot. Trained only on randomly generated worlds with diverse obstacle layouts and camera viewpoints, ReVNM can generalize well to real robot navigation without additional fine-tuning. Experiments in both simulation and real-world environments confirmed the effectiveness of the proposed approach.

</details>

#### 2026-09-23 - AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios

**Authors:** Zhipeng Bao, Wenjie Zhao, Tianle Zhu, Haohua Que, Chence Yang, Geng Yuan, Qianwen Li
**Links:** [abs](https://arxiv.org/abs/2609.28366) - [pdf](https://arxiv.org/pdf/2609.28366)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios
- 作者：Zhipeng Bao, Wenjie Zhao, Tianle Zhu, Haohua Que, Chence Yang, Geng Yuan, Qianwen Li
- 出版日期：2026-09-23T16:38:06Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2609.28366) / [PDF](https://arxiv.org/pdf/2609.28366)

### 一句话总结
论文提出 AnchorReasoning——一个面向长尾自动驾驶、基于 WOD-E2E 构建的视觉 grounded 推理数据集，通过 VG-CoT 监督与课程式微调，将决策关键视觉证据与推理及轨迹规划相连接。

### 研究问题
视觉语言模型（VLMs）在长尾自动驾驶中具有潜力，但现有驾驶数据集对“将决策关键的视觉证据与推理和规划相连接”所提供的监督有限。论文针对这一监督不足的问题展开研究。

### 核心思路/方法
- 构建 AnchorReasoning 数据集，基于 WOD-E2E，包含 416,119 个标注帧和 395,379 个决策关键元素，覆盖 4 个大类、19 个细粒度类型。
- 每帧组织为视觉 grounded 的思维链（VG-CoT），连接：决策关键元素的识别与定位、元素属性与含义、驾驶动作依据，以及动作与轨迹规划。
- 提出课程式监督微调策略，逐步学习上述分层能力。
- 提出一个物体尺寸感知的 grounding 指标，用于评估定位质量。
- 在八种通用、具身智能和自动驾驶专用骨干模型上进行实验。

### 主要贡献
- 提出 AnchorReasoning 数据集，为长尾自动驾驶提供视觉 grounded 的推理监督，规模为 416,119 帧、395,379 个决策关键元素，含 4 大类 19 细类。
- 提出 VG-CoT 标注组织方式，将元素识别定位、属性含义、动作依据与轨迹规划串联为一条推理链。
- 提出课程式监督微调策略与物体尺寸感知的 grounding 评估指标。
- 实验显示 VG-CoT 监督提升了 grounded 推理与轨迹预测：5-s ADE 和 FDE 分别下降 7.84 和 11.86，RFS Frame 和 Cluster 分别提升 1.66 和 1.70；同时平均减少 18.5 个推理 token，每帧推理延迟降低 0.32 秒。

### 局限性
- 摘要未提供足够信息说明数据集的具体采集条件、标注质量控制与一致性验证方式。
- 摘要未提供足够信息说明实验的完整设置、基线对比细节与消融研究。
- 摘要未提供足够信息说明该方法在真实闭环驾驶或安全关键场景中的验证情况。
- 摘要未提供足够信息说明物体尺寸感知 grounding 指标的具体定义与计算方式。
- 摘要未提供足够信息说明课程式微调各阶段的具体划分与超参数。

### 阅读优先级
高。理由：该工作同时涉及数据集构建、视觉 grounded 思维链监督、课程式微调与自动驾驶轨迹预测评测，且给出了明确的量化收益（ADE/FDE 下降、效率提升），对长尾自动驾驶与 VLM 推理规划交叉方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-language models (VLMs) offer a promising approach to long-tail autonomous driving, but existing driving datasets provide limited supervision for connecting decision-critical visual evidence with reasoning and planning. We introduce AnchorReasoning, a visually grounded reasoning dataset built on WOD-E2E, containing 416,119 annotated frames and 395,379 decision-critical elements across four major categories and 19 fine-grained types. Each frame is organized as a visually grounded chain-of-thought (VG-CoT) that links decision-critical element identification and localization, element attributes and implications, driving-action rationale, and action and trajectory planning. We further develop a curriculum supervised fine-tuning strategy that progressively learns these hierarchical capabilities, together with an object-size-aware grounding metric for evaluating localization quality. Experiments across eight general-purpose, embodied-AI, and AV-specific backbones show that VG-CoT supervision improves grounded reasoning and trajectory prediction. Across models, 5-s ADE and FDE decrease by 7.84 and 11.86, while RFS Frame and Cluster improve by 1.66 and 1.70. These gains are achieved with 18.5 fewer reasoning tokens and 0.32 s/frame lower inference latency on average, demonstrating the value of visually grounded, decision-focused supervision for VLM reasoning and planning in long-tail autonomous driving.

</details>

#### 2026-09-23 - VLMs Can Describe, But Not Measure: Object-Centric Scene Understanding for Robotic Manipulation

**Authors:** Enrico Saccon, Tommaso Faraci, Iñigo De La Ossa Zarzuelo, Luigi Palopoli, Marco Roveri, Matteo Saveriano
**Links:** [abs](https://arxiv.org/abs/2609.28184) - [pdf](https://arxiv.org/pdf/2609.28184)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth estimation, manipulation, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VLMs Can Describe, But Not Measure: Object-Centric Scene Understanding for Robotic Manipulation
- 作者：Enrico Saccon, Tommaso Faraci, Iñigo De La Ossa Zarzuelo, Luigi Palopoli, Marco Roveri, Matteo Saveriano
- 出版日期：2026-09-23T14:26:22Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2609.28184 ；PDF https://arxiv.org/pdf/2609.28184

### 一句话总结
论文提出一种由 VLM 驱动、模块化的物体级场景理解框架，通过将单次 RGB-D 观测分割为物体区域、由 VLM 标注并结合深度信息，构建与任务无关的物体中心表示，从而在保留语义能力的同时改善定位与深度估计。

### 研究问题
面向未见过环境中的机器人操作，系统既需要语义理解，也需要可靠的度量（几何）信息。摘要指出，视觉-语言模型（VLM）具备较强的语义能力，但其几何估计不够可靠。因此，论文关注如何在机器人场景理解中同时获得可靠的语义与度量信息。

### 核心思路/方法
论文提出的方法是一个 VLM 驱动、模块化的感知框架，使用现成（off-the-shelf）方法完成场景理解。具体流程为：从单次 RGB-D 观测出发，将场景分割为物体级区域；由 VLM 对这些区域进行标注；再利用深度信息进行 grounding（落地/对齐），从而构建一个与任务无关的物体中心表示。该表示还被集成到任务规划框架中，用于机器人执行。

### 主要贡献
- 提出一种模块化的、由 VLM 驱动的物体中心场景理解感知框架，基于现成方法构建。
- 从单次 RGB-D 观测生成物体级区域分割，并由 VLM 标注，再用深度信息进行 grounding，形成任务无关的物体中心表示。
- 在 151 个桌面场景上进行实验，摘要称该分解方法在保持较强语义性能的同时，相较直接 VLM 推理显著改善了定位与深度估计。
- 将该表示与任务规划框架集成，用于机器人执行。

### 局限性
摘要未提供足够信息。摘要未说明具体失败案例、适用场景边界、对特定 VLM 或分割方法的依赖程度、计算开销、真实机器人实验的规模与条件，也未给出定量指标细节与消融分析。

### 阅读优先级
中。理由：该论文聚焦 VLM 在机器人操作中的语义与几何度量分工问题，并提出模块化、物体中心的表示方法，且包含桌面场景实验与任务规划集成，对具身智能与机器人感知方向有参考价值；但摘要未提供足够的实验细节、对比方法与真实机器人验证信息，是否值得深入阅读需结合全文的定量结果与实验设置进一步判断。

</details>

<details>
<summary>Abstract</summary>

Robotic operation in previously unseen environments requires both semantic understanding and reliable metric information. While vision--language models (VLMs) provide strong semantic capabilities, their geometric estimates remain less reliable. In this paper, we propose a VLM-driven, modular perception framework for scene understanding using off-the-shelf approaches. Starting from a single RGB-D observation, the scene is segmented into object-level regions, annotated by a VLM, and grounded with depth information to construct a task-independent object-centric representation. Experiments on 151 tabletop scenes show that the proposed decomposition preserves strong semantic performance while substantially improving localization and depth estimation over direct VLM inference. The resulting representation is also integrated with a task-planning framework for robotic execution.

</details>

#### 2026-09-23 - Wave-Robust Passive AUV Localization Using FP-MUSIC

**Authors:** Usama Saqib, Ola Rønning, Andrzej Wąsowski
**Links:** [abs](https://arxiv.org/abs/2609.27712) - [pdf](https://arxiv.org/pdf/2609.27712)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wave-Robust Passive AUV Localization Using FP-MUSIC
- 作者：Usama Saqib, Ola Rønning, Andrzej Wąsowski
- 出版日期：2026-09-23T11:29:56Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.27712

### 一句话总结
针对水面波浪引起的水听器阵列六自由度扰动问题，提出利用 IMU 测量对快拍协方差进行去扭曲的定点迭代 MUSIC 算法（FP-MUSIC），以实现接收端被动的 AUV 三维定位与空间建图。

### 研究问题
在无预部署海底应答器、也无法直接访问载体自身传感器的条件下，如何对自主水下航行器（AUV）进行定位。核心困难在于：水面波浪运动带来六自由度扰动，会使阵列在相邻快拍之间发生旋转，从而降低传统子空间处理的性能。

### 核心思路/方法
- 系统构成：单个浮动水面浮标，配备水听器阵列与惯性测量单元（IMU），实现接收端被动的三维定位与空间建图。
- 核心算法 FP-MUSIC：一种定点迭代的 MUSIC 算法，利用 IMU 测量在到达方向估计之前对快拍协方差进行“去扭曲”（de-warp）。
- 距离与前后向分辨：采用子空间投影的宽带匹配滤波器解算信标距离，并利用功率不对称性进行独立的前后向识别。

### 主要贡献
- 提出接收端被动的三维定位与空间建图系统方案，仅依赖单个配备水听器阵列和 IMU 的水面浮标。
- 提出 FP-MUSIC，利用 IMU 测量在 DOA 估计前对快拍协方差去扭曲，以应对波浪引起的阵列旋转。
- 采用子空间投影宽带匹配滤波器解算信标距离，并用功率不对称性实现独立的前后向识别。
- 在多种模拟海况下评估：FP-MUSIC 相比未补偿方法显著降低定位误差，并在波浪扰动下维持稳健的三维跟踪与载体姿态估计；中等海况下，2 米信标间隔的准确率从约 45% 提升至 75%。

### 局限性
摘要未提供足够信息。摘要仅在模拟海况下给出评估结果，未提供实际海试、真实环境验证、计算复杂度、实时性、不同阵列构型或不同海况上界的表现等信息。

### 阅读优先级
中。理由：该工作面向水下被动定位中波浪扰动导致子空间处理退化的具体问题，方法思路（IMU 辅助协方差去扭曲 + 定点迭代 MUSIC）较为明确，且给出了量化的性能提升；但摘要仅覆盖模拟评估，缺乏实海况验证等关键信息，是否具备工程落地价值需进一步阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

Localizing an autonomous underwater vehicle without pre-deployed seabed transponders, or direct access to onboard vehicle sensors remains a core challenge. We present a receiver-passive 3-D localization and spatial mapping system utilizing a single floating surface buoy equipped with a hydrophone array and an inertial measurement unit (IMU). The central difficulty is that surface wave motion induces six-degree-of-freedom (6-DOF) perturbations that rotate the array between snapshots, degrading conventional subspace processing. We resolve this by introducing a fixed-point iterative MUltiple SIgnal Classification algorithm (FP-MUSIC) that uses IMU measurements to de-warp snapshot covariances prior to direction-of-arrival estimation. Furthermore, we employ a subspace-projected wideband matched filter to resolve beacon ranges and use power asymmetry for independent front-back identification. Evaluations across simulated sea states demonstrate that FP-MUSIC substantially reduces localization error relative to uncompensated methods and sustains robust 3-D tracking and vehicle orientation estimation under wave-induced motion. At moderate sea state, FP-MUSIC increases the 2-m beacon-separation accuracy from approximately 45% to 75%.

</details>

#### 2026-09-23 - DAVIO: Dense Monocular-Inertial SLAM with Feed-Forward Initialization and Pose-Conditioned Mapping

**Authors:** Jaafar Mahmoud, Arthur Movsesyan, Mikhail Iumanov, Sergey Kolyubin
**Links:** [abs](https://arxiv.org/abs/2609.27702) - [pdf](https://arxiv.org/pdf/2609.27702)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DAVIO: Dense Monocular-Inertial SLAM with Feed-Forward Initialization and Pose-Conditioned Mapping
- 作者：Jaafar Mahmoud, Arthur Movsesyan, Mikhail Iumanov, Sergey Kolyubin
- 出版日期：2026-09-23T11:21:38Z
- 分类：Embodied / Robotics / AR Applications（主）；3D Reconstruction & Multi-view Geometry（次）
- 链接：摘要页 https://arxiv.org/abs/2609.27702 ；PDF https://arxiv.org/pdf/2609.27702

### 一句话总结
DAVIO 利用单一多视角深度模型 Depth Anything 3，同时承担单目惯性 SLAM 的启动初始化与建图，实现具备真实尺度与重力约束的实时稠密 SLAM。

### 研究问题
仅用相机与 IMU 进行度量尺度定位与稠密建图时，传统视觉-惯性滤波器必须等待足够的视差才能启动，并且只能保留稀疏路标；而前馈几何模型虽然能从少量图像预测稠密结构，却无法提供度量尺度与重力方向。论文试图融合两类方法的优势，解决启动慢、定位误差与建图稠密度/精度之间的矛盾。

### 核心思路/方法
- 使用单一多视角深度模型 Depth Anything 3 同时服务于启动阶段与建图阶段。
- 启动阶段：由五张图像窗口与预积分 IMU 测量构成一个无特征（feature-free）线性系统，通过带鲁棒性与条件数检查的求解，经缓冲重放（buffered replay）引导 VIO 滤波器完成初始化。
- 跟踪阶段：用滤波器的度量位姿对深度模型进行条件化（conditioning）。
- 残差尺度仅沿视线方向进行校正，以保持度量相机基线不变。
- 使用保持重力的子图（gravity-preserving submap graph）并结合带漂移门控的重访机制对地图进行精化。
- 论文声明发布 DAVIO 代码，定位为实时稠密度量 SLAM 系统。

### 主要贡献
- 提出用单一前馈多视角深度模型同时完成启动初始化与稠密建图的 SLAM 框架。
- 设计无特征、带条件数检查的线性启动方案，借助 IMU 预积分实现更早启动并获得度量尺度与重力信息。
- 提出位姿条件化建图与仅沿视线方向的尺度校正策略，在保持相机基线的同时修正残差尺度。
- 引入保持重力的子图图结构与漂移门控重访进行地图精化。
- 在 EuRoC 上相较 SOTA 前馈建图方法启动更早、定位误差更低、建图更准确（在相同位姿条件下）；在建筑尺度的 ORI 序列上，在相同里程计下达到或优于 SOTA 建图方法，且在将 GT 位姿替换为真实里程计时性能下降更小。
- 向社区开源代码。

### 局限性
- 具体运行时间、帧率、内存占用等实时性指标：摘要未提供足够信息。
- 除 EuRoC 与 ORI 之外的数据集或场景泛化能力：摘要未提供足够信息。
- 深度模型预测偏差对系统的影响分析：摘要未提供足够信息。
- 与更多类型基线（如非前馈方法、其他 VIO/SLAM 系统）的定量对比细节：摘要未提供足够信息。
- 消融实验与各模块贡献的定量结果：摘要未提供足够信息。

### 阅读优先级
中。理由：该工作面向单目+IMU 的稠密度量 SLAM，将前馈深度模型与 VIO 滤波器结合，选题在机器人与 AR 应用方向具有明确价值，且涉及启动初始化、尺度校正与建图精化等实际工程问题。但由于仅提供摘要，无法判断实验规模、实时性指标与开源代码质量，是否值得精读取决于读者对单目惯性稠密 SLAM 或前馈几何先验融合方向的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

A camera and an IMU are the minimal sensor setup for metric localization and dense mapping, yet classical visual--inertial filters must wait for parallax before they start and then retain only sparse landmarks. Feed-forward geometry models, in contrast, predict dense structure from a few images but provide neither metric scale nor gravity. We present DAVIO, which uses a single multi-view depth model, Depth Anything~3, for both start-up and mapping. At start-up, a five-image window and preintegrated IMU measurements form a feature-free linear system. Its robust, conditioning-checked solution bootstraps a VIO filter through buffered replay. During tracking, the filter's metric poses condition the depth model. Residual scale is corrected only along viewing rays, which preserves the metric camera baselines, and a gravity-preserving submap graph with drift-gated revisits refines the map. On EuRoC, DAVIO starts markedly earlier, reduces the localization error, and maps more accurately than SOTA feed-forward mappers given identical poses. On building-scale ORI sequences, DAVIO is on bar or better than SOTA mappers on the same odometry, and degrades far less when GT poses are replaced by real odometry. We release the code of DAVIO, a real-time dense metric SLAM system, to the community.

</details>

#### 2026-09-23 - Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization

**Authors:** Byeonggyu Park, Mingu Jeon, Seong-Woo Kim
**Links:** [abs](https://arxiv.org/abs/2609.27346) - [pdf](https://arxiv.org/pdf/2609.27346)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization
- 作者：Byeonggyu Park, Mingu Jeon, Seong-Woo Kim
- 出版日期：2026-09-23T04:33:01Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.27346 ；PDF: https://arxiv.org/pdf/2609.27346

### 一句话总结
该论文提出一个反射感知框架，用于在自车运动条件下融合前视相机图像与 2D 雷达点云，通过推断反射阶数和反射面分布并借助物理引导射线追踪重建反射路径，从而定位处于非视距（NLOS）状态的行人。

### 研究问题
如何在外来自车动态的户外场景中，可靠地定位非视距（NLOS）行人。摘要指出，这一问题对城市自动驾驶安全至关重要，但在自车运动环境下极具挑战，因为自车运动会使雷达多径传播变得复杂且噪声严重。

### 核心思路/方法
- 面向户外测试场场景中移动自车的 NLOS 行人定位，提出反射感知框架。
- 融合前视相机图像和 2D 雷达点云。
- 在鸟瞰图（bird’s-eye-view）空间中推断反射阶数和反射面分布。
- 使用物理引导的射线追踪重建失真的反射路径，并据此定位被遮挡行人。
- 在自车动态条件下的户外测试场场景中进行验证。

### 主要贡献
- 提出一个面向移动自车 NLOS 行人定位的反射感知框架。
- 将前视相机图像与 2D 雷达点云融合，并在鸟瞰图空间推断反射阶数和反射面分布。
- 引入物理引导射线追踪以重建失真反射路径并定位隐藏行人。
- 在户外测试场场景中、自车动态条件下验证框架有效性。摘要声称结果证明了该框架在移动自车 NLOS 行人定位中的有效性。

### 局限性
- 摘要未提供足够信息说明具体实验规模、数据集组成、评价指标和定量结果。
- 摘要未提供足够信息说明框架在不同场景、天气、光照、交通密度或传感器配置下的泛化能力。
- 摘要未提供足够信息说明失败案例、计算开销、实时性、对雷达噪声或多径复杂度的鲁棒性边界。
- 摘要未提供足够信息说明与已有方法的对比情况。
- 摘要未提供足够信息说明“户外测试场场景”的具体范围及其对真实城市开放道路的代表性。

### 阅读优先级
中。理由：该论文关注自动驾驶中 NLOS 行人定位这一安全相关且具有挑战性的问题，方法上结合多模态感知、鸟瞰图推理和物理引导射线追踪，具有一定技术针对性；但根据摘要，验证局限于户外测试场场景，且摘要未给出定量结果、对比和泛化性信息。因此对 NLOS 感知、雷达多径利用或自动驾驶行人安全方向的研究者优先级较高，对一般读者则为中等。

</details>

<details>
<summary>Abstract</summary>

Reliable localization of non-line-of-sight (NLOS) pedestrians is critical for safe urban autonomous driving, yet it remains highly challenging in ego-dynamic outdoor environments, where ego-vehicle motion makes radar multipath propagation complex and noisy. In this paper, we present a reflection-aware framework for NLOS pedestrian localization with a moving ego-vehicle in outdoor testbed scenarios. Our framework fuses front-view camera images and 2D radar point clouds to infer reflection orders and reflective surface distributions in bird's-eye-view space. It then uses physics-guided ray tracing to reconstruct distorted reflection paths and localize the hidden pedestrian. We validate the framework in outdoor testbed scenarios under ego-dynamic conditions. The results demonstrate the effectiveness of the proposed framework for NLOS pedestrian localization with a moving ego-vehicle.

</details>

#### 2026-09-23 - BladeMaster: Real-Time Robotic Cutting Simulation with Online-Generated Persistent Discontinuities

**Authors:** Zhanyu Yang, Yunuo Chen, Yanjia Huang, Joseph Masterjohn, Yin Yang, Chenfanfu Jiang
**Links:** [abs](https://arxiv.org/abs/2609.27342) - [pdf](https://arxiv.org/pdf/2609.27342)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BladeMaster: Real-Time Robotic Cutting Simulation with Online-Generated Persistent Discontinuities
- 作者：Zhanyu Yang, Yunuo Chen, Yanjia Huang, Joseph Masterjohn, Yin Yang, Chenfanfu Jiang
- 出版日期：2026-09-23T04:29:39Z
- 分类：Embodied / Robotics / AR Applications（二级分类：未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.27342) / [PDF](https://arxiv.org/pdf/2609.27342)

### 一句话总结
BladeMaster 是一个基于全拉格朗日物质点法（TLMPM）的 GPU 加速切割仿真框架，通过在物质点上在线生成持久侧标签来编码切割历史，从而在无需预设切割面或复制粒子的情况下实现实时机器人切割仿真。

### 研究问题
可变形物体的切割会同时改变其形状与拓扑结构，这给机器人操作中的精确仿真带来挑战。仿真器需要：
- 在切割发展过程中跟踪切割工具；
- 在工具撤出后保留产生的间断（不连续性）；
- 使新暴露的表面能够与工具以及彼此之间发生交互。

而现有方法通常预先指定切割面，或将材料分离与辅助几何场耦合，难以满足上述需求。

### 核心思路/方法
- 基于**全拉格朗日物质点法（TLMPM）**，并利用 **GPU 加速**。
- 核心思想：将切割历史**直接编码在物质点上**，通过由刀片几何形状**在线生成**的持久侧标签（persistent side labels）实现。
- 这些标签控制**粒子-网格耦合**：在完整材料内部保持连通性，同时在工具撤出后阻止切割面之间的虚假耦合。
- 该形式支持**渐进切割与相交切割**，无需预定义切割面，也无需复制粒子。
- 通过**材料-材料接触**，切割面可以重新接触并相互滑动而不会重新连接。
- 通过**工具-材料双向耦合**，材料反作用力能够影响工具运动。

### 主要贡献
- 提出 BladeMaster，一个基于 TLMPM 的 GPU 加速切割框架。
- 通过在线生成的持久侧标签将切割历史编码于物质点，控制粒子-网格耦合以保留切割间断。
- 支持渐进切割与相交切割，无需预设切割面或粒子复制。
- 支持切割面重新接触与滑动而不重新连接，并支持工具与材料的双向耦合。
- 实验展示了工具驱动切割后的操作，并在代表性任务上实现**快于实时**的性能。

### 局限性
- 摘要未提供足够信息（未说明方法的适用边界、失败情形、精度与稳定性限制、对比基线的具体范围等）。
- 摘要未提供足够信息（未给出实验任务的具体类型、规模、硬件配置及性能指标的量化细节）。
- 摘要未提供足够信息（未说明该方法对特定材料模型、本构或参数选择的依赖与敏感性）。

### 阅读优先级
**高**。理由：该工作直面机器人切割仿真中拓扑变化、间断保留与实时性等核心难题，提出的在线生成持久标签思路具有方法层面的新颖性，且声称达到快于实时的性能，对机器人操作与可变形体仿真方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Cutting changes both the shape and topology of deformable objects, making accurate simulation challenging for robotic manipulation. A simulator must track the cutting tool as a cut develops, preserve the resulting discontinuities after tool withdrawal, and enable newly exposed surfaces to interact with the tool and with each other. Existing formulations often prescribe cut surfaces in advance or couple material separation to auxiliary geometric fields. We introduce BladeMaster, a GPU-accelerated cutting framework based on the total Lagrangian material point method (TLMPM). Our key idea is to encode the cutting history directly on material points through persistent side labels generated online from the blade geometry. These labels govern particle-grid coupling, preserving connectivity within intact material while preventing spurious coupling across cut faces after tool withdrawal. Our formulation supports progressive and intersecting cuts without predefined cut surfaces or particle duplication. Material-material contact enables cut surfaces to recontact and slide against each other without reconnecting, while two-way tool-material coupling allows material reaction forces to influence tool motion. Experiments demonstrate tool-driven cutting followed by manipulation, with faster-than-real-time performance on representative tasks.

</details>

#### 2026-09-23 - Spatial and Semantic Reasoning for LLM-Driven Robot Navigation via MCP

**Authors:** Jungsoo Lee, Jaegyun Park, Wansoo Kim
**Links:** [abs](https://arxiv.org/abs/2609.27340) - [pdf](https://arxiv.org/pdf/2609.27340)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatial and Semantic Reasoning for LLM-Driven Robot Navigation via MCP
- 作者：Jungsoo Lee, Jaegyun Park, Wansoo Kim
- 出版日期：2026-09-23T04:29:01Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.27340 ；PDF https://arxiv.org/pdf/2609.27340

### 一句话总结
该论文提出一种非侵入式框架，通过面向导航的表示层并经 MCP 标准化工具，将 LLM 推理与 ROS 导航连接起来，使 LLM 能够利用度量/位姿感知图像与语义路点标注完成地图构建及空间、语义导航目标选择。

### 研究问题
论文指出现有 LLM 与 ROS 导航集成存在两个缺口：一是占据栅格等导航数据为原始几何消息，LLM 难以直接将其用作空间或语义上下文；二是添加 LLM 驱动能力通常需要自定义封装或机器人专用接口，限制了跨系统复用。

### 核心思路/方法
提出一个非侵入式框架，连接 LLM 推理与基于 ROS 的导航。框架包含面向导航的表示层，并通过 Model Context Protocol（MCP）暴露为标准化、可复用工具，使任何 MCP 兼容的 LLM 无需机器人专用封装即可访问。具体模块包括：视觉地图模块将占据栅格转换为度量、位姿感知图像以供目标推理；语义标注模块记录带有机器人位姿的路点级观测。评估任务为自主建图、基于空间推理的导航、基于语义推理的导航。

### 主要贡献
- 提出一种非侵入式框架，在不修改现有 ROS 导航栈的情况下，将 LLM 推理与 ROS 导航连接。
- 设计导航导向表示层：视觉地图模块把占据栅格转为度量、位姿感知图像；语义标注模块记录带位姿的路点级观测。
- 通过 MCP 将上述能力暴露为标准化、可复用工具，使任意 MCP 兼容 LLM 无需机器人专用封装即可使用。
- 在模拟室内环境中评估三类任务，报告所评估的 LLM 后端利用这些表示达到超过 97% 的地图覆盖率，并能根据自然语言指令选择空间或语义导航目标。

### 局限性
摘要未提供足够信息。摘要未说明模拟环境的规模与多样性、所评估的具体 LLM 后端、与基线方法的对比、失败案例、真实机器人验证情况，以及 MCP 工具在跨系统复用方面的实际测试范围。

### 阅读优先级
中。理由：该工作聚焦 LLM 与 ROS 导航集成中的表示与接口复用问题，提出 MCP 标准化工具与非侵入式框架，并报告了超过 97% 地图覆盖率及空间/语义目标选择结果；但摘要仅给出模拟室内环境下的有限任务评估，未提供与基线的对比细节、真实机器人验证和跨系统复用测试信息。对关注 LLM 机器人导航、ROS 集成或 MCP 工具化的读者具有参考价值，但若需判断其泛化性与实际部署效果，摘要信息尚不充分。

</details>

<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used as natural-language interfaces for robotic systems, yet their integration with Robot Operating System (ROS)-based navigation remains limited by two gaps. First, navigation data such as occupancy grids are represented as raw geometric messages that are difficult for LLMs to use directly as spatial or semantic context. Second, adding LLM-driven capabilities often requires custom wrappers or robot-specific interfaces, limiting reuse across systems. To address these challenges, we propose a non-invasive framework that connects LLM reasoning with ROS-based navigation through a navigation-oriented representation layer, exposed through the Model Context Protocol (MCP) as standardized, reusable tools so that any MCP-compatible LLM can access them without robot-specific wrappers. The visual map modules transform occupancy grids into metric, pose-aware images for goal reasoning, while the semantic annotation modules record waypoint-level observations with robot poses. We evaluate the framework on three tasks: autonomous mapping, spatial reasoning-based navigation, and semantic reasoning-based navigation. The results show that the evaluated LLM backends use these representations to achieve over 97% map coverage and select spatial or semantic navigation targets from natural-language instructions in a simulated indoor environment. This demonstrates representation-mediated LLM navigation without modifying the existing ROS navigation stack.

</details>

#### 2026-09-22 - Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping

**Authors:** Markus Käppeler, Rohit Mohan, Abhinav Valada
**Links:** [abs](https://arxiv.org/abs/2609.26325) - [pdf](https://arxiv.org/pdf/2609.26325)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping
- 作者：Markus Käppeler, Rohit Mohan, Abhinav Valada
- 出版日期：2026-09-22T12:36:48Z
- 分类：Embodied / Robotics / AR Applications（主要分类；二级分类摘要未提供）
- 链接：摘要页 https://arxiv.org/abs/2609.26325 ；PDF https://arxiv.org/pdf/2609.26325

### 一句话总结
论文提出一个无需 LiDAR 构建先验地图的框架：利用视觉方法从历史相机轨迹构建带语义特征的静态点云先验地图，并在运行时将其与多视角相机特征在 BEV 空间融合，以提升基于相机的 3D 目标检测与在线矢量化 HD 地图构建。

### 研究问题
基于相机的 3D 目标检测和在线矢量化 HD 地图构建能提供紧凑的场景表示，但二者都依赖准确的度量几何，并受深度歧义限制。长期部署中，重复轨迹的观测可累积为持久的点云先验，提供超出当前观测的几何上下文；然而现有显式点云先验方法依赖 LiDAR 建图，需要昂贵的 3D 测距传感器。论文关注的问题是：能否仅用视觉构建点云先验，并用于提升上述两个相机感知任务？

### 核心思路/方法
- 使用 Pi3X 从既往相机轨迹构建静态点云先验地图，并为每个点附加 DINOv3 特征。
- 运行时通过全局定位检索局部先验块，用稀疏体素骨干网络编码，并在鸟瞰图（BEV）中与提升后的多视角相机特征融合。
- 融合表示输入任务特定的稀疏 Transformer 头，分别预测 3D 目标和矢量化地图元素。

### 主要贡献
- 提出一个使用视觉构建几何-语义点云先验的框架，先验地图构建与在线推理均不需要 LiDAR。
- 在 Argoverse 2 上，视觉先验将强基线从 0.287 提升至 0.299 CDS，并将矢量化地图构建 mAP 从 0.669 提升至 0.750。
- 消融实验显示，语义 DINOv3 特征对矢量化地图构建尤其重要。
- 结果表明，视觉构建的几何-语义先验可作为长期场景记忆，改善两个相机感知任务。

### 局限性
- 除 Argoverse 2 外，是否在其他数据集或场景下有效，摘要未提供足够信息。
- 框架对全局定位、Pi3X 建图质量、DINOv3 特征质量的具体依赖程度与失效条件，摘要未提供足够信息。
- 与 LiDAR 先验方法相比的性能差距、计算与存储开销、长期部署中的更新机制，摘要未提供足够信息。
- 摘要未提供足够信息说明 3D 目标检测与矢量化地图构建两侧收益差异的具体原因。

### 阅读优先级
中。理由：该工作针对相机感知中深度歧义与 LiDAR 依赖问题，提出用视觉构建点云先验并同时服务两个重要任务，在 Argoverse 2 上有明确指标提升，且消融指出语义特征对地图构建重要；但摘要未提供跨数据集验证、计算开销和与 LiDAR 先验的对比等关键细节，是否具有广泛通用性尚不明确。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MatchFusion: Explicit-Implicit Instance Matching for Spatio-Temporal Multimodal Autonomous Driving
- 作者：Xiaoyu Li, Jiajia Fu, Long Shi, Tianyu Du, Ruihang Li, Xian Wu, Lijun Zhao, Yingtao Zhang, Lining Sun, Ruifeng Li
- 出版日期：2026-09-22T08:24:12Z
- 分类：Embodied / Robotics / AR Applications
- 链接：abs: https://arxiv.org/abs/2609.25860 ；pdf: https://arxiv.org/pdf/2609.25860

### 一句话总结
MatchFusion 提出一种可学习的“显式—隐式”实例匹配与融合模块，用几何相似度与类别一致性初始化实例关联，再借助实例嵌入选择性细化，从而统一支持空间 LiDAR-相机与时间过去-当前交互，并在 nuScenes 上同时提升感知精度、降低计算与显存开销。

### 研究问题
论文关注多模态感知与端到端自动驾驶（E2EAD）中的稀疏实例表示交互问题：在空间 LiDAR-相机融合以及时间过去-当前交互中，由于几何差异和异构语义表示，可靠实例对应关系难以建立。摘要指出，已有路线存在两难：基于注意力的方法可利用上下文语义，但常需专门表示对齐，计算开销增加；基于结构化目标状态的关联方法高效且可解释，却缺乏上下文证据以解决歧义匹配。因此，核心问题是如何在保持高效与可解释的同时，获得足够的上下文信息来完成可靠实例匹配与融合。

### 核心思路/方法
摘要给出的方法要点如下：
- 提出 MatchFusion，一个面向时空多模态自动驾驶的可学习实例匹配与融合模块。
- 匹配初始化：使用几何相似度和类别一致性初始化成对亲和度。
- 选择性细化：对结构上合理的关联，使用实例嵌入进行选择性细化，以补充上下文证据。
- 融合机制：由得到的软匹配图（soft matchmap）引导一个通用的残差聚合算子，实现自适应信息交换。
- 统一形式：该“匹配—融合”统一 formulation 同时支持空间 LiDAR-相机交互与时间过去-当前交互，分别使用多视图图像平面几何和运动补偿 BEV 几何作为结构先验。
- 端到端集成：将时间 MatchFusion 集成进 SparseDrive，可在 E2E 框架内提升感知，且无需额外监督。

### 主要贡献
- 提出显式—隐式结合的实例匹配与融合模块 MatchFusion，用于时空多模态自动驾驶中的稀疏实例交互。
- 将几何相似度、类别一致性等结构化先验与实例嵌入的上下文细化结合，以缓解歧义匹配问题。
- 用统一的匹配—融合形式覆盖空间 LiDAR-相机与时间过去-当前两类交互，并分别采用多视图图像平面几何与运动补偿 BEV 几何作为结构先验。
- 在 nuScenes 上验证：在不同前端配置下取得一致的感知增益。
- 与先前以实例为中心的融合方法相比，MatchFusion 系统在更高感知精度的同时，FLOPs 降低 55.3%，GPU 显存使用降低 39.3%，匹配—融合模块仅占总感知延迟的 3.7%。
- 将时间 MatchFusion 集成到 SparseDrive 中，可在 E2E 框架内进一步提升感知，且无需额外监督。

### 局限性
摘要未提供足够信息。摘要未说明失败场景、对特定数据集或前端配置的依赖程度、匹配错误的影响、可扩展性边界、训练数据需求、超参数敏感性、实时性在更广泛硬件或平台上的表现，也未提供定量结果之外的定性失败案例分析。

### 阅读优先级
高。理由：该工作直接针对多模态自动驾驶中稀疏实例时空交互的关键问题，且摘要报告了在 nuScenes 上精度提升的同时显著降低 FLOPs 和 GPU 显存，并将模块集成到 E2E 框架 SparseDrive 中；对关注多模态感知、端到端自动驾驶、实例级融合与效率优化方向的研究者具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes
- 作者：Yuling Xi, Haokai Zhang, Muzhi Zhu, Hao Zhong, Zongze Du, Hengyu Zhao, Chenchen Jing, Yufei Yin, Bin Qin, Yongjie Yang, Zhenbo Luo, Hao Chen, Chunhua Shen
- 出版日期：2026-09-22T08:09:21Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.25841；PDF https://arxiv.org/pdf/2609.25841

### 一句话总结
论文提出面向室内场景的 Metric-Bench 基准与 MetricReasoner 微调方案，利用图像内已知物理尺寸的参考物体，引导 VLM 在不依赖相机内参的情况下进行上下文空间度量推理，并报告了多项基准上的性能提升。

### 研究问题
视觉语言模型（VLM）的度量推理对具身智能任务（如机器人操作、自主导航）至关重要，但当前空间推理受限于僵化的像素级监督；这种局部化优化可能损害通用多模态智能，导致性能下降或对广泛推理能力的灾难性遗忘。

### 核心思路/方法
- 构建 Metric-Bench：一个聚焦的基准，通过引入图像内具有已知物理尺寸的参考物体，利用上下文信息引导度量空间推理，使模型隐式学习 2D 到 3D 的映射，且不依赖相机内参。
- 提出 MetricReasoner：一种面向参考物 grounded 度量推理的任务适配强化微调方案，使用结构化提示和可验证的数值奖励。

### 主要贡献
- 提出 Metric-Bench，用于指导基于上下文信息的度量空间推理。
- 提出 MetricReasoner 强化微调方法，用于参考物 grounded 的度量推理。
- 在 Metric-Bench 上，方法显著增强空间度量理解，超过现有模型甚至更大的专有模型 43.1%。
- 下游具身性能相比空间专用对照模型，在 RoboSpatial 总体准确率上提升 30.4%，在 ERQA 上提升 9.3%。
- 在通用基准上也有持续增益：V$\star$Bench 提升 15.9%，BLINK 提升 88.9%，表明该适配不一定损害通用 VLM 能力。

### 局限性
- 论文摘要未提供足够信息说明基准的规模、数据来源、标注方式或场景多样性。
- 摘要未提供足够信息说明实验设置、对比基线细节、消融实验或失败案例。
- 摘要未提供足够信息说明方法在不同 VLM 架构、训练成本或真实机器人部署中的适用性与限制。
- 摘要未提供足够信息说明数值奖励的具体设计、结构化提示的具体形式及可验证性的边界。

### 阅读优先级
高。理由：该论文聚焦具身 AI 中关键的度量空间推理问题，同时提出基准与微调方法，并在摘要中报告了在空间、具身及通用基准上的多项显著提升；对关注 VLM 空间推理、机器人操作与自主导航的研究者有较强相关性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation
- 作者：Yu Zheng, Qiyu Feng, Yixin Wu, Baoquan Yang, Yixuan Zhou, Bingyang Hu, Kemeng Huang, Guansheng Yang, Hesheng Wang
- 出版日期：2026-09-22T04:03:34Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.25653 （PDF: https://arxiv.org/pdf/2609.25653）

### 一句话总结
PhyVisGen 是一个兼顾物理与视觉高保真的机器人操作数据生成框架，用仿真数据训练的策略在五个真实机器人任务上达到 65–95% 成功率，且无需真实演示数据或策略微调。

### 研究问题
大规模操作演示数据对学习鲁棒的视觉运动策略至关重要，但真实世界数据采集成本高、难以规模化。仿真虽有潜力，但物理与视觉差异会限制合成数据的迁移性，尤其是在使用软体夹爪的操作场景中。

### 核心思路/方法
论文从物理与视觉两方面构建高保真数据生成框架：
- 物理侧：提出基于增量势接触（IPC）的机械臂—夹爪耦合方法，使完整操作轨迹中保持高保真软体接触。
- 视觉侧：结合真实场景重建与实时路径追踪，在保留所采集场景外观的同时生成视觉逼真的观测。

### 主要贡献
- 提出 PhyVisGen 框架，面向可扩展的机器人操作数据生成，兼具物理与视觉高保真。
- 引入基于 IPC 的机械臂—夹爪耦合方法，支持完整操作轨迹中的高保真软接触。
- 结合真实场景重建与实时路径追踪，生成保留场景外观的视觉逼真观测。
- 定量评估验证了框架的物理与视觉保真度。
- 仅用合成操作演示训练的策略在五个真实机器人任务上取得 65–95% 成功率，无需真实机器人演示数据或策略微调。

### 局限性
摘要未提供足够信息。摘要未说明方法的计算开销、IPC 耦合在更复杂接触场景下的适用边界、视觉重建对场景采集条件的要求、五个任务的具体类型与难度，以及失败案例或成功率波动的来源；也未提供与基线方法的对比细节。

### 阅读优先级
高。理由：该工作直接针对机器人操作数据规模化中的核心瓶颈（仿真到真实的物理与视觉差距），并给出无需真实演示与微调即可在真实任务上取得 65–95% 成功率的验证结果，对具身智能与机器人学习方向具有较强参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation
- 作者：Sunyu Wang, Jean Oh, Nancy S. Pollard
- 出版日期：2026-09-22T03:25:32Z
- 分类：Embodied / Robotics / AR Applications（主要分类；次要分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2609.25619 ；PDF https://arxiv.org/pdf/2609.25619

### 一句话总结
该论文将手与工具建模为统一的“手-物体机构”（HOM），以相对接触速度约束来描述其运动，并提出一种轻量、物理可解释的运动规划与接触估计框架，使多指机器人手完成从抓取工具、装载到合适位姿再到挥舞工具的完整操作流程。

### 研究问题
如何让通用多指机器人手执行完整的工具操作过程，即拾取工具、将工具装载到合适位姿、然后挥舞工具。摘要指出，该工作关注的是完整流程，而不仅是其中某一环节。

### 核心思路/方法
- 受人类工具操作与机械设计原理启发，将手和工具建模为统一的“手-物体机构”（HOM），其由子装配体组成。
- 将 HOM 定义为由手、物体和广义接触坐标系构成，使 HOM 的运动可以用同一组笛卡尔空间相对接触速度表示，不依赖于手的运动学与几何结构。
- 将 HOM 的子装配体定义为手指之间的相对接触速度与接触力约束。
- 基于上述定义，开发了一个轻量且物理可解释的运动规划与接触估计框架，使用最小二乘法与互补滤波器。
- 评估方式为在仿真中遥操作五种不同的机器人手。

### 主要贡献
- 提出以相对接触速度统一表达手-工具机构运动的形式化定义，强调其不依赖具体手的运动学与几何。
- 提出将 HOM 分解为子装配体，并以手指间相对接触速度与接触力约束来定义子装配体。
- 提出基于最小二乘与互补滤波器的轻量、物理可解释的运动规划与接触估计框架。
- 实验结果显示，该框架使五种不同的手都能执行完整工具操作流程，并能从相同、简单的参考轨迹产生灵巧行为。
- 结果还展示了该框架对不同手、工具与任务具有一定适应性，其基础在于运动学与几何层面的建模。

### 局限性
- 摘要仅说明评估在仿真中通过遥操作五种机器人手完成，未提供真实机器人实验信息。
- 摘要未提供足够信息说明该方法在接触估计精度、规划鲁棒性、泛化边界、失败案例或计算开销方面的具体局限。
- 摘要未提供足够信息说明所测试工具、任务的具体范围以及“灵巧行为”的量化评价标准。
- 摘要未提供足够信息说明最小二乘与互补滤波器框架在不同噪声、不确定性或复杂接触条件下的表现。

### 阅读优先级
中。理由：该工作聚焦多指机器人手完整工具操作流程，并提出统一的手-物体机构表示与轻量规划/接触估计框架，对机器人操作与具身智能方向具有潜在参考价值；但摘要未提供真实机器人验证细节与定量局限信息，是否需要优先精读取决于读者对仿真验证、统一接触速度建模或工具操作规划的具体兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：JAMB: Joint Action-Motion Diffusion for Bimanual Manipulation
- 作者：Chuyang Xiao, Peilin Meng, David Held
- 出版日期：2026-09-21T19:11:38Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次要分类信息
- 链接：摘要页 https://arxiv.org/abs/2609.25322 ；PDF https://arxiv.org/pdf/2609.25322 ；项目网站 https://jam-bimanual.github.io/

### 一句话总结
JAMB 提出一种联合去噪双臂动作与未来 3D 点轨迹的扩散策略，通过共享 Transformer 让动作假设与运动假设在去噪过程中相互修正，以提升协调双臂操作的性能与泛化能力。

### 研究问题
双臂协调操作具有挑战性，因为任一机械臂的运动都会改变共享的 3D 场景，从而影响另一条臂。然而，多数扩散策略在生成动作时并未显式建模这种未来几何后果；而带预测的变体通常仅将未来状态用作辅助监督或固定条件。论文旨在解决如何在动作生成过程中显式、交互式地建模未来几何变化，以支持协调双臂操作。

### 核心思路/方法
- 提出 JAMB，一种扩散策略，联合去噪双臂动作与未来 3D 点轨迹。
- 在共享 Transformer 内让动作假设与轨迹假设共同演化，使二者在去噪全过程中互相提供信息并相互精炼。
- 将多模态表示统一锚定在共享时空坐标系中，以促进联合去噪过程中的几何感知交互。
- 在 RoboTwin 2.0 的多种双臂操作任务以及真实世界机器人上进行评估，并与仅动作策略及不同状态表示、学习目标的替代未来预测方法进行比较。

### 主要贡献
- 提出联合动作-运动建模框架 JAMB，将双臂动作与未来 3D 点轨迹在同一扩散过程中联合去噪，而非仅将未来状态作为辅助监督或固定条件。
- 通过共享 Transformer 和共享时空坐标系，实现动作与未来运动假设之间的几何感知交互与相互精炼。
- 在 16 个仿真任务上达到平均 83.4% 成功率，比最强基线高 23.9 个百分点。
- 在三个真实世界任务上，分别比仅动作方法和辅助几何预测方法高 50.0 和 21.2 个百分点。
- 在杂乱场景和分布外背景上表现出比所评估基线更强的泛化能力。

### 局限性
- 摘要未提供足够信息说明方法的计算开销、实时性、推理速度或部署成本。
- 摘要未提供足够信息说明真实世界实验的具体任务设置、机器人平台、传感器配置与评估规模。
- 摘要未提供足够信息说明失败案例、安全边界、对感知噪声或标定误差的敏感性。
- 摘要未提供足够信息说明 3D 点轨迹的获取方式、是否依赖外部跟踪或特定表示，以及其泛化到更复杂任务或更多臂系统的能力。
- 摘要未提供足够信息说明与基线在模型规模、训练数据量或计算预算上是否严格对齐。

### 阅读优先级
高。理由：该论文针对双臂协调操作中“动作生成未显式建模未来几何后果”的关键问题，提出联合去噪动作与未来 3D 点轨迹的框架，并在仿真与真实机器人上报告了显著性能提升和更强泛化能力；主题属于具身智能与机器人操作的前沿方向，且提供了项目网站，适合优先阅读。

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
