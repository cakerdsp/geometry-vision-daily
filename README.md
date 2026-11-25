# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：80
- 分类分布：
  - Embodied / Robotics / AR Applications: 24
  - Neural Scene Representations & Rendering: 22
  - 3D Reconstruction & Multi-view Geometry: 19
  - Dynamic / 4D Reconstruction: 8
  - Geometry Foundation Models: 7
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“隐式表示可被剪枝/路由”成为神经渲染的效率主线。**
   多篇论文不再把 token、高斯或特征当作不可约的整体，而是引入显式的重要性/可见性判据在推理前做选择。Tokens as Locality-Preserving Anchors 用轻量路由器按目标视角只保留固定预算的源 token，使渲染成本与源图像数量解耦；LMnOP 指出高剪枝率下“单独冗余、组合关键”的高斯会被 leave-one-out 误删，改用 leave-many-out 重要性；HoloSplat 则在服务端对 token 做不透明度引导剪枝与 PCA 降维以适配带宽。共同点是：**效率优化的对象从“像素/图元”上移到“token 或特征”，并且越来越依赖对表示冗余结构的建模**，而非单纯压缩网络。

2. **前馈重建正在从“受控采集”走向“野外鲁棒”。**
   WildAnySplat 直面瞬态遮挡、光照变化与相机 ISP 造成的多视角不一致，用学生-教师框架、瞬态掩码与双边网格恢复规范表示；HoloSplat 与 ViDiHand2 则分别处理真实采集中的带宽约束与未见相机泛化。方向变化在于：**前馈方法的评价标准正从“在干净基准上更快”转向“在真实退化输入下仍然一致”**，鲁棒性设计（掩码、外观归一化、几何约束求解）开始成为前馈管线的一等公民，而不是后处理补丁。

3. **几何先验与生成先验正在双向耦合，而非单向“生成辅助几何”。**
   BridgeMVS 明确批评现有混合方法只单向利用单目线索，改为 mono-to-cost 与 cost-to-mono 的双向动态融合；ViDiHand2 把视频扩散模型的“外观深度回归”重构为基于 MANO 度量结构的几何约束求解；LatentParse 则把 CLIP/DINOv3/VGGT 的潜特征解析成显式空间证据再喂给 VLM。趋势是：**显式几何（度量、多视图一致性）与学习型先验（扩散、基础模型特征）互为约束项**，而不是一个当输入、一个当输出。

4. **世界模型与主动感知开始强调“目标/查询驱动的稀疏化”。**
   ROAM-GS 用持久目标加选择性视角，只在变长前缀的端点采集，解决多房间场景下短视 next-best-view 与密集建图的两难；DexLatentWorld 从点云演示学连续潜在动作，把统一潜动作空间直接作为 MPC 搜索空间，绕开昂贵的动作标签；One Latent World 让同一空间潜表示被异构 LiDAR 直接射线解码。共同点是：**不再追求“更密地建模一切”，而是建模“该看哪里/该查哪条射线”**，把采样与观测的决策纳入模型本身。

5. **基准与失效分析成为独立且必要的研究产出。**
   EgoDepth-Bench 用 37 个环境、94 万级同步样本与毫米级几何校验构建第一视角度量深度基准，并报告微调后 AbsRel 从 0.708 降到 0.091；Confidently Lost 揭示 MASt3R-SLAM 在光子饥饿下“静默失败”——纯噪声帧对给出 0.936 的跨视图自一致性，暗序列中超过 95% 被接受的对应违反真值对极几何；Place-Revisit Consistency 用重访一致性发现 KITTI 参考位姿局部不一致，平移差异中位数达 6.60 m。趋势是：**社区开始系统性地质疑“高置信度统计量=正确几何”这一假设**，评估方法本身成为被审视对象。

#### 技术路线观察

- **几何基础模型方向**：LatentParse 走“免训练解析”路线，不动 VLM 权重，用工具化探测把三种编码器的潜特征转成文本证据；Confidently Lost 则从反面检验学习型双视图几何的可靠性，指出高自一致性可能在无结构输入下被伪造；EgoDepth-Bench 提供的是评测与监督基础设施。三者共同显示该方向的重心正从“再训一个更大的几何模型”转向“如何可靠地读取和信任已有模型的几何输出”。

- **3D/4D 重建方向**：BridgeMVS 在级联 MVS 框架内做多阶段双向融合，属于传统多视图几何与单目先验的深度耦合；ROAM-GS 是免训练的主动采集策略，强调视角预算分配而非网络结构；Place-Revisit Consistency 与 Screening for nonrigidity 分别从数据基准与 SfM 诊断角度处理“重建结果可信吗”的问题。该方向呈现“**精度提升**（BridgeMVS）与“**采集/验证策略**”（ROAM-GS、两项诊断工作）并行推进的格局。

- **神经场景表示与渲染方向**：这一支最集中。Tokens as Locality-Preserving Anchors 与 LMnOP 分别从注意力路由和高斯剪枝两端压缩成本；NNS-GS 把散射建模从局部特征扩展到光空间到视图空间的非局部贡献，并配合渐进式训练分离漫反射/散射/镜面成分；WildAnySplat 把前馈 3DGS 推向野外；GSDet 则反向把高斯泼溅用作检测的表示形式，用 3D 高斯替代锚框/查询。技术侧重点明显从“表示能力”转向“**表示的可寻址性与可裁剪性**”。

- **机器人/AR 应用方向**：Real2Worlds2Real 用智能体编排工具构建数字孪生并扩展为数字变体，属于 Real2Sim2Real 的规模化尝试；DexLatentWorld 与 One Latent World 都在构建“可被控制/可被异构传感器查询”的潜空间世界模型；MakeSense 针对退化感知下的负融合问题，用私有流加共享瓶颈 token 保留传感器特异证据；Tri-DNO 以噪声优化替代重训练来改善手物接触；ViDiHand2 为从第一视角视频学习操作提供度量手部运动。该方向的共性是：**瓶颈不在生成质量，而在数据成本、具身迁移与传感器可靠性**，因此方法多为“复用预训练模型+轻量适配/优化”。

#### 值得优先阅读的论文

1. **Confidently Lost**（2611.30173）
   优先级最高。它给出的失效模式（纯噪声输入下跨视图自一致性仍达 0.936、超过 95% 被接受对应违反真值对极几何）对任何使用学习型双视图几何做 SLAM/重建的工作都是直接警示，且提出了无需真值的区分手段，方法学价值高于单点性能提升。

2. **Tokens as Locality-Preserving Anchors**（2611.31156）
   把源 token 当作保持局部性的空间锚点并用路由器按视角选固定预算，是“渲染成本与源视图数解耦”的清晰技术路线；其以解码器注意力作监督、用非最大抑制降冗余、一次排序服务多预算的设计，具备较强的可迁移性。

3. **LMnOP**（2611.30102）
   对 leave-one-out 重要性在高剪枝率下失效的诊断很具体，且给出随机移除下像素颜色均值/方差的闭式近似、无需采样，属于“问题指出+可计算方案”都较完整的工作，对 3DGS 部署侧压缩有直接参考价值。

4. **BridgeMVS**（2611.30787）
   双向动态融合的动机（现有混合方法单向利用单目线索）陈述清楚，级联多阶段框架中每阶段做 mono-to-cost 与 cost-to-mono 更新，是几何与先验耦合的代表性工程路线，且有代码链接便于复现核验。

5. **WildAnySplat**（2611.31023）
   若关注前馈 3DGS 的野外落地，这篇最直接：学生-教师监督、逐视角瞬态掩码、双边网格颜色变换三个组件分别对应不一致性的不同来源，混合数据策略（真实配对+合成增强+伪干净标签）也值得细看其配比与消

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-25T17:30:37-05:00
**Total number of papers:** 102
**Number of papers added in the latest update:** 45
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

#### 2026-11-24 - FocusAnchor: Zero-Shot Metric Depth by Anchoring a Depth Foundation Prior to Focus Cues

**Authors:** Ashkan Ganj, Hang Su, Tian Guo
**Links:** [abs](https://arxiv.org/abs/2611.32970) - [pdf](https://arxiv.org/pdf/2611.32970)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** metric depth

<details>
<summary>Abstract</summary>

Existing depth-from-focus methods can struggle with weak focus cues, new cameras, or fewer focal slices. We present FocusAnchor, a recurrent model that uses focus-volume lookups to refine metric depth and repeatedly aligns a relative depth prior from a frozen foundation model to the current depth estimate. The aligned prior guides subsequent refinement in a feedback loop, carrying metric scale recovered from textured regions into regions where focus cues are weak while preserving scene structure. To support transfer across cameras, we synthesize training stacks with randomized camera parameters and focus distances. However, stack synthesis blurs existing image noise differently across slices, creating artificial depth cues even on textureless surfaces. We add independent per-slice noise to suppress these cues. We also introduce variable-stack training to improve robustness with fewer focal slices and support more practical mobile capture. Compared with FOSSA ViT-B, FocusAnchor reduces AbsRel by 36% on NYU Depth V2 and by 9% on DDFF-12 after fine-tuning. In zero-shot evaluation, FocusAnchor and its variable-stack variant, FocusAnchor-flex, achieve the two lowest AbsRel values on all five benchmarks. On ZEDD test, FocusAnchor achieves 9% lower AbsRel than the best competing method, FOSSA ViT-B, while FocusAnchor-flex achieves lower AbsRel with 40% fewer focal slices on ZEDD validation.

</details>

#### 2026-11-24 - X-3DComposer: Feed-Forward 3D Scene Composition with Any Assets from Any Views

**Authors:** Zidian Qiu, Ancong Wu
**Links:** [abs](https://arxiv.org/abs/2611.32491) - [pdf](https://arxiv.org/pdf/2611.32491)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>Abstract</summary>

Composing an editable 3D scene from images requires an asset for each object and a layout that places the assets. 3D generation and CAD retrieval now supply the assets, but layout still lacks a general solution: scene generation methods couple it with generation, and pose estimators handle one object at a time and need true-size CAD models, depth, or iterative refinement. We present X-3DComposer, a feed-forward model that predicts the layout separately from asset generation. Given one or more images of a scene, the object masks, and an asset for each object from any source, it jointly predicts the rotation, translation, and per-axis scale of all objects in a single forward pass of about one second. The key idea is to treat objects as views: renders of the assets are processed together with the scene images by a multi-view geometry model adapted from VGGT-$Ω$, and each object pose follows in closed form from the cameras predicted for its renders. Camera intrinsics, camera poses, and depth are optional inputs. When the meshes produced by five scene generation methods are kept fixed and only their layout is replaced, the layouts of X-3DComposer are more accurate than the native layouts of these methods. Compared with the stand-alone layout model SceneMaker, it reduces the scene-level Chamfer distance by 52% on IndoorMix, our test set from six indoor datasets, and by 28% on 3D-FUTURE.

</details>

#### 2026-11-24 - MaskedVGGT: Masked Multi-View Transformers Are Scalable 3D Learners

**Authors:** Zichen Zou, Xiaosong Jia, Wen-Ming Chen, Zuxuan Wu, Yu-Gang Jiang
**Links:** [abs](https://arxiv.org/abs/2611.32297) - [pdf](https://arxiv.org/pdf/2611.32297)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, CroCo, multi-view transformer, novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Multi-view feed-forward models show strong scalability, but their reliance on costly geometric annotations limits data scaling. Existing 3D self-supervised approaches reduce this reliance through cross-view completion (e.g., CroCo, MuM, Muskie) or novel-view synthesis (e.g., RayZer, E-RayZer), typically learning image representations and cross-view interactions jointly. We argue that learning single image representations from scratch is unnecessary for 3D pretraining methods, as doing so fails to benefit from the continuing advances in 2D foundation models (e.g., DINO, CLIP, frontier VLMs). We introduce MaskedVGGT, which freezes a strong pretrained 2D encoder and pretrains only an added, randomly initialized multi-view transformer, focusing on learning interactions across views. MaskedVGGT pretrains the multi-view transformer through masked self-distillation without annotations: a student predicts targets at masked locations based on complete anchor views and heavily masked remaining views, while an exponential-moving-average teacher provides prediction targets based on unmasked inputs. In experiments across model sizes up to 1B parameters, MaskedVGGT pretraining followed by fine-tuning outperforms single-stage supervised VGGT-$Ω$ training with the same training data, model architecture, and total number of optimization updates. MaskedVGGT also outperforms E-RayZer, CroCo, MuM, and Muskie, providing evidence for the effectiveness of building multi-view pretraining on strong 2D representations. Finally, extending pretraining with additional unlabeled videos further improves generalization, and the learned representations transfer to diverse downstream tasks. These results demonstrate an effective division of learning: reuse strong image representations from 2D pretraining and learn cross-view interactions from unlabeled multi-view data without relying on geometric annotations.

</details>

#### 2026-11-23 - Parsing Visual Latents for Multimodal Spatial Reasoning

**Authors:** Zhuoying Yang, Yichen Guo, Kathy Jia, Zichang Su, Ayesha Kashif, Nange Hai, Jeffrey Ming Han Li, Zhewen He, Silvio Kempf, Ni Jiachen, Junjie Yang, Muhammad Hamza, Zakaria El Ouahidi, Gabriel Azpitarte, Manling Li, Yi Fang, Shuhong Liu, Mengyu Wang
**Links:** [abs](https://arxiv.org/abs/2611.31021) - [pdf](https://arxiv.org/pdf/2611.31021)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Parsing Visual Latents for Multimodal Spatial Reasoning
- 作者：Zhuoying Yang, Yichen Guo, Kathy Jia, Zichang Su, Ayesha Kashif, Nange Hai, Jeffrey Ming Han Li, Zhewen He, Silvio Kempf, Ni Jiachen, Junjie Yang, Muhammad Hamza, Zakaria El Ouahidi, Gabriel Azpitarte, Manling Li, Yi Fang, Shuhong Liu, Mengyu Wang
- 出版日期：2026-11-23T17:02:00Z
- 分类：主分类 Geometry Foundation Models；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2611.31021) / [PDF](https://arxiv.org/pdf/2611.31021)

### 一句话总结
论文提出免训练的 LatentParse 框架，将 CLIP、DINOv3、VGGT 三种预训练视觉编码器的潜特征解析成显式空间证据文本，连同图像一起提供给 VLM，以提升多视图空间推理表现。

### 研究问题
多视图空间推理需要从 2D 观测推断物体与相机之间的 3D 关系，这依赖跨视图对应和场景几何。视觉语言模型（VLM）无法可靠提取这些信息；而预训练视觉编码器的潜特征本已包含相关信息（CLIP 关联物体与图像区域、DINOv3 跨视图匹配语义、VGGT 编码多视图几何），但以灰度特征图形式直接放入上下文时，VLM 并不能从中受益。论文要解决的问题是：如何让 VLM 有效利用这些潜特征进行空间推理。

### 核心思路/方法
LatentParse 是一个免训练框架，流程如下：
1. 使用一个“分析者 VLM”，借助预定义工具探测三种编码器的特征。这些工具的功能是定位物体、跨视图跟踪物体、测量视图间运动；
2. 将探测结果提炼为简洁的文本报告；
3. 把该文本报告与图像一起提供给目标 VLM，用于回答问题。

方法的核心是将潜特征“解析”为关系证据文本，而不是让 VLM 直接读取特征图，并且整个过程不需要训练。

### 主要贡献
- 提出免训练的 LatentParse 框架，把预训练视觉编码器的潜特征解析为显式空间证据供 VLM 使用。
- 在 MMSI-Bench、MV-RoboBench 和 SPAR-Bench 三个基准上评估，相比仅使用图像的基线，使全部五个 VLM 平均提升 0.7–2.4 个百分点。
- 在 MMSI-Bench 上，将 Qwen3.8-27B 从 34.4% 提升到 39.5%，其中相机相关问题提升最大，达 19.2 个百分点。
- 结论表明：潜特征一旦被解析为关系证据，无需训练即可对空间推理产生作用；论文提供代码链接。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法的具体失效场景、计算开销、对分析者 VLM 能力的依赖程度、各基准上的细分结果或误差来源。

### 阅读优先级
中。理由：该工作针对 VLM 多视图空间推理中的明确痛点，提出免训练、可直接复用的特征解析思路，并在三个基准、五个 VLM 上给出一致的小幅提升，且相机相关问题提升显著，方法与结论对相关方向有参考价值；但摘要中提升幅度总体有限，且缺少对失败情形与开销的说明，需阅读全文进一步判断适用性。

</details>

<details>
<summary>Abstract</summary>

Spatial reasoning across multiple views requires inferring the 3D relations between objects and the camera from 2D observations, which depends on cross-view correspondence and scene geometry that vision-language models (VLMs) do not reliably extract. Pretrained vision encoders already capture this information in their latent features, with CLIP linking objects to image regions, DINOv3 matching semantics across views, and VGGT encoding multi-view geometry. However, VLMs do not benefit from these features when we present them directly in context as grayscale feature images. We therefore propose LatentParse, a training-free framework that parses latent features into explicit spatial evidence for VLMs. In LatentParse, an analyst VLM probes the features of all three encoders with predefined tools that locate objects, track them across views, and measure motion between views. It then distills the results into a concise text report, which is provided together with the images to the VLM to answer the question. We evaluate LatentParse on MMSI-Bench, MV-RoboBench and SPAR-Bench, where it improves all five VLMs over the photo-only baseline by 0.7-2.4 percentage points on average. On MMSI-Bench, it raises Qwen3.8-27B from 34.4% to 39.5%, with the largest improvements of 19.2 percentage points on the camera-related questions. These results suggest that latent features become useful for spatial reasoning once they are parsed into relation evidence, without training. Code is available at https://github.com/Harvard-AI-and-Robotics-Lab/LatentParse.

</details>

#### 2026-11-23 - EgoDepth-Bench: Benchmarking Metric Depth for Egocentric Manipulation

**Authors:** Yuan Gao, Dongchen Wei, Xinyang Lin, Shuhua Cao, Xueliang Guo, Zhuohan Li, Yihao Wang
**Links:** [abs](https://arxiv.org/abs/2611.30734) - [pdf](https://arxiv.org/pdf/2611.30734)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, depth estimation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoDepth-Bench: Benchmarking Metric Depth for Egocentric Manipulation
- 作者：Yuan Gao, Dongchen Wei, Xinyang Lin, Shuhua Cao, Xueliang Guo, Zhuohan Li, Yihao Wang
- 出版日期：2026-11-23T14:12:47Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要 https://arxiv.org/abs/2611.30734 ；PDF https://arxiv.org/pdf/2611.30734

### 一句话总结
论文提出 EgoDepth-Bench，一个面向第一视角操作场景的度量深度基准，包含跨 37 个物理环境采集的 941,233 个同步样本，并用于评估单目、双目与多视角模型的深度精度和预测覆盖情况。

### 研究问题
摘要聚焦于第一视角操作场景中的度量深度估计评测问题：现有模型在该场景下的度量深度精度与预测覆盖（包括手部和物体区域）需要系统评估，同时需要考察模型对未见环境的泛化能力。摘要未提供更具体的问题背景或现有基准缺陷的详细说明。

### 核心思路/方法
- 构建 EgoDepth-Bench 数据集：包含 941,233 个同步样本，覆盖 37 个不同物理环境。
- 每个样本组合六路经过标定的 RGB 视图，以及原生鱼眼视图中的度量深度；该深度由五个主动红外立体模块重建。
- 使用标定球杆验证几何精度，已知球间距上的中位误差为 1.27 mm。
- 提供按环境划分的留出集（environment-held-out splits），用于评估对未见环境的泛化。
- 在单目、双目和多视角模型上同时测量深度精度与预测覆盖，包括手部和物体区域。
- 摘要给出微调示例：在 EgoDepth-Bench 上微调 MapAnything 后，在未见环境上度量 AbsRel 从 0.708 降至 0.091，尺度对齐 AbsRel 从 0.327 降至 0.072。

### 主要贡献
- 提出 EgoDepth-Bench 基准，提供大规模同步 RGB 与度量深度样本，覆盖 37 个物理环境。
- 提供基于主动红外立体模块和标定球杆验证的毫米级几何精度深度数据。
- 设计环境留出划分，支持对未见环境的泛化评估。
- 建立同时衡量深度精度与预测覆盖（含手部和物体）的评测方式，覆盖单目、双目和多视角模型。
- 通过 MapAnything 微调结果展示该基准可作为有效监督并支持严格的度量与相对深度评估。
- 项目页面提供评估代码和交互式 RGB-深度序列。

### 局限性
- 摘要未提供足够信息说明数据集在传感器同步误差、主动红外立体模块在不同材质或光照条件下的失效情况等方面的具体局限。
- 摘要未提供足够信息说明基准在模型类型、场景多样性或任务类型上的覆盖边界。
- 摘要未提供足够信息说明除 MapAnything 外其他模型的完整评测结果与失败模式。
- 摘要未提供足够信息说明数据采集成本、标注质量控制细节或潜在偏差。

### 阅读优先级
高。理由：该论文直接面向第一视角操作场景的度量深度评测，提供大规模同步 RGB-度量深度数据、环境留出泛化评估以及精度与覆盖并重的指标；摘要给出的微调结果显示了显著的 AbsRel 改善，且与 Embodied / Robotics / AR Applications 相关，适合关注第一视角深度估计与机器人操作感知的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

We introduce EgoDepth-Bench, comprising 941,233 synchronized samples collected across 37 distinct physical environments. Each sample combines six calibrated RGB views with metric depth in the native fisheye view, reconstructed from five active-infrared stereo modules. A calibrated ball-bar confirms millimeter-level geometric accuracy, with a median error of 1.27 mm on a known sphere spacing. Environment-held-out splits enable evaluation of generalization to unseen environments. Across monocular, stereo, and multi-view models, the benchmark measures both depth accuracy and prediction coverage, including on hands and objects. Fine-tuning MapAnything on EgoDepth-Bench reduces metric AbsRel from 0.708 to 0.091 and scale-aligned AbsRel from 0.327 to 0.072 on unseen environments. These results demonstrate that EgoDepth-Bench provides effective supervision and enables rigorous evaluation of metric and relative depth estimation in egocentric manipulation. The project page provides the evaluation code and interactive RGB-depth sequences.

</details>

#### 2026-11-23 - Confidently Lost: Silent Failure and Edge Deployment of Dense Visual SLAM under Photon Starvation

**Authors:** Shrikrishna Bhagirath Rajule, Srinath Neelamagam, Aniket Bera
**Links:** [abs](https://arxiv.org/abs/2611.30173) - [pdf](https://arxiv.org/pdf/2611.30173)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** MASt3R, SLAM, visual SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Confidently Lost: Silent Failure and Edge Deployment of Dense Visual SLAM under Photon Starvation
- 作者：Shrikrishna Bhagirath Rajule, Srinath Neelamagam, Aniket Bera
- 出版日期：2026-11-23T07:21:28Z
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.30173) / [PDF](https://arxiv.org/pdf/2611.30173)

### 一句话总结
论文指出，基于学习到的双视图几何的稠密视觉 SLAM 在低照度下会“静默失败”：网络在缺乏场景结构时仍会为两帧生成一致几何，使系统错误地信任高自洽性统计量，并分析了这种机制在边缘设备部署中的表现。

### 研究问题
论文关注低照度（photon starvation）条件下稠密视觉 SLAM 的失效模式：系统并非显式报错，而是在高置信度下静默失败。具体问题包括：网络在仅有噪声、没有真实场景时是否仍给出高跨视图几何自一致性；这种被高估的统计量如何影响关键帧选择与重定位；能否在无真值条件下区分“自信的崩溃”与正常运行；以及该机制在边缘部署中的可复现性。

### 核心思路/方法
- 以 MASt3R-SLAM 为分析对象，考察其网络在低照度下的跨视图几何自一致性统计量。
- 构造两类输入进行对照：9 级量化噪声的两帧（无场景）与真实暗帧对，比较其自一致性数值。
- 分析同一被高估的统计量如何被两个子系统以相反方向的阈值读取，导致关键帧饥饿与重定位几乎接受所有候选。
- 提出在关键帧对基线上读取同一统计量，以在 ETH3D 暗序列上、无真值且无额外计算（样本内）地区分自信崩溃与正常运行。
- 比较低照度适配权重与重新调整两个阈值的效果，并在搭载于腿足机器人的 Jetson AGX Orin 上回放，观察机制特征在四条路线中最暗两条上的复现情况。

### 主要贡献
- 揭示低照度下稠密视觉 SLAM 的静默失败现象：两帧纯量化噪声即可使网络给出 0.936 的跨视图几何自一致性，真实暗帧对为 0.935；网络在缺乏结构时“发明”相同几何并让系统信任该一致性。
- 给出失效后果的量化描述：在暗序列上消耗 1,605 帧、仅输出 7 个关键帧、不拒绝任何因子图边、报告满帧率，而接受对应关系中超过 95% 违反真值对极几何。
- 指出同一膨胀统计量被两个子系统以相反阈值读取，造成关键帧饥饿与重定位过度接受并存的矛盾行为。
- 提出无需真值、无额外计算的样本内判别方式（在关键帧对基线上读取同一统计量），用于分离自信崩溃与正常运行。
- 通过低照度适配权重与阈值重调实验说明：跟踪轨迹可从 1/6 提升到 5/6，但两者都不能得到准确轨迹，因为适配只是从错误几何中撤回置信，而非找到正确几何。
- 在边缘设备部署回放中验证机制特征可在最暗路线上复现，且其表现形式随路线几何与传感器编码变化。

### 局限性
- 摘要仅报告了 ETH3D 暗序列上的样本内结果，未提供跨数据集或样本外验证信息。
- 摘要未提供低照度适配权重与阈值重调实验的完整设置、评价指标细节与统计显著性。
- 摘要未提供边缘部署回放的定量指标、路线数量之外的传感器配置细节及失败率数据。
- 摘要未说明该方法在非暗光常规条件下的表现，也未给出与其他 SLAM 系统的对比实验。
- 摘要未提供足够信息说明所提判别方式在实际在线系统中的阈值选择与鲁棒性。
- 摘要未提供足够信息说明计算开销、实时性及在更多机器人平台上的泛化能力。

### 阅读优先级
高。理由：论文聚焦稠密视觉 SLAM 在低照度下的静默失败这一安全相关失效模式，涉及几何基础模型的可信度、统计量误用与边缘部署，问题定义清晰且具有实践风险；摘要给出的现象与量化描述具体，适合关注 SLAM 鲁棒性、低照度感知与机器人部署的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Dense visual SLAM built on learned two-view geometry is evaluated in good light; in low light it fails silently. Two frames of 9-level quantized noise, no scene at all, give MASt3R-SLAM's network a cross-view geometric self-consistency of 0.936; a real dark frame pair gives 0.935. Starved of structure, the network invents the same geometry for both views and the system trusts the agreement: on a dark sequence it consumes 1,605 frames, emits 7 keyframes, rejects no factor-graph edges and reports full frame rate, while over 95% of the correspondences it accepts violate the ground-truth epipolar geometry. One inflated statistic is read by two subsystems against thresholds in opposite directions, so keyframing starves while relocalization accepts almost every candidate. The same statistic, read at keyframe-pair baselines, separates the confident collapse from working runs on the ETH3D dark sequences without ground truth or extra computation (in-sample). Low-light-adapted weights take tracked trajectories from 1/6 to 5/6, as does retuning two thresholds; neither yields accurate ones, because the adaptation withdraws confidence from wrong geometry rather than finding right geometry. Replayed on a Jetson AGX Orin carried by a legged robot, the mechanism's signature reproduces on the two darkest of four routes, and which of its faces appears varies with route geometry and sensor encoding. The network does not lose confidence in the dark; it manufactures it.

</details>

#### 2026-11-22 - Separating Action Allocation from Image Matching in Visual Token Routing

**Authors:** Chenxi Wang, Bin Wang
**Links:** [abs](https://arxiv.org/abs/2611.29477) - [pdf](https://arxiv.org/pdf/2611.29477)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** image matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Separating Action Allocation from Image Matching in Visual Token Routing
- 作者：Chenxi Wang, Bin Wang
- 出版日期：2026-11-22T13:26:58Z
- 分类：Geometry Foundation Models（主类）；3D Reconstruction & Multi-view Geometry（次类）
- 链接：[摘要](https://arxiv.org/abs/2611.29477) / [PDF](https://arxiv.org/pdf/2611.29477)

### 一句话总结
论文提出将自适应视觉 token 路由中的“动作次数分配”与“图像—动作匹配”两个因素分离开来评估，发现匹配本身有益，但按任务表分配动作频率相对随机配对会造成更大质量损失。

### 研究问题
自适应视觉 token 路由器旨在节省计算，同时保留回答每个问题所需的图像细节。论文关注的问题是：较高的平均得分究竟反映了路由器为单张图像做出了更好的选择，还是仅仅因为在需要高分辨率的任务上更频繁地使用了高分辨率。也就是说，需要区分“图像匹配质量”与“动作频率分配”对最终得分的贡献。

### 核心思路/方法
论文在每个任务内固定动作次数，并将路由器的分配结果与“相同动作和图像的随机配对”进行比较，以此分离匹配效应与动作频率效应。实验涉及等权重的 ChartQA 和 TextVQA，使用 Qwen2.5-VL-3B 与 -7B，并考察外部选择器 CARES 所选择的连续分辨率交换后的影响。此外，在请求带有任务标签时，将任务表与离散路由器进行比较。

### 主要贡献
- 提出一种在任务内固定动作次数、以随机配对为对照的分析方式，用于区分图像匹配与动作分配的影响。
- 报告在等权重 ChartQA 和 TextVQA 上，Qwen2.5-VL-3B 和 -7B 均从匹配中获益，但相对于任务表，其动作频率带来更大损失；7B 上表现为 1.71 分增益与 3.95 分损失。
- 发现交换 CARES 选择的连续分辨率也会降低 7B 的质量。
- 在请求带任务标签时，任务表比离散路由器高 1.92 分，并在 7B 完整请求上平均节省 31.76 ms。

### 局限性
摘要未提供足够信息，无法判断实验覆盖范围、数据集规模、统计显著性、其他模型或任务上的泛化性，以及方法的具体实现细节。

### 阅读优先级
中。理由：该论文关注视觉 token 路由评估中的归因问题，对理解自适应计算与分辨率分配的有效性有参考价值；但摘要仅给出有限任务与模型上的结果，且分类标注与视觉 token 路由主题之间的关联在摘要中未展开，需阅读全文才能判断方法细节与广泛适用性。

</details>

<details>
<summary>Abstract</summary>

Adaptive visual token routers aim to save computation while preserving the image detail needed to answer each question. A higher average score could reflect better choices for individual images or more frequent use of high resolution on tasks that need it. We distinguish the two by keeping action counts fixed within each task and comparing the router's assignments with random pairings of the same actions and images. On equally weighted ChartQA and TextVQA, both Qwen2.5-VL-3B and -7B gain from matching but lose more from their action frequencies relative to a task table, with a 1.71-point gain and a 3.95-point loss on 7B. Exchanging the continuous resolutions chosen by the external selector CARES also lowers quality on 7B. When requests arrive with task labels, the table outscores the discrete router by 1.92 points and saves 31.76 ms per complete 7B request on average.

</details>

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

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-24 - HARI4D: Hand-Articulation Aware 4D Reconstruction of Human-Object Interaction

**Authors:** Semin Kim, Xianghui Xie, Chuqiao Li, Jongyoo Kim, Gerard Pons-Moll
**Links:** [abs](https://arxiv.org/abs/2611.32932) - [pdf](https://arxiv.org/pdf/2611.32932)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, manipulation, VR

<details>
<summary>Abstract</summary>

Reasoning about human-object interaction from RGB cameras is important for gaming, VR environments, and robot learning. Yet 4D reconstruction from a monocular RGB camera is challenging, especially when articulated hands are involved. Prior full-body works neglect hands during reconstruction, causing them to penetrate into, or float from the object. We present HARI4D, a hand-articulation-aware method for reconstructing spatially and temporally consistent 4D human-object interaction from monocular RGB video. We introduce a history-aware object tracker that provides robust and stable tracking. Based on these tracks, we improve the interaction configuration through coarse-to-fine reasoning that follows the order of object manipulation: ReachNet first brings the full body and arms to the object during contact, and TouchNet then finalizes hand articulation according to temporal context and local object geometry. On ARCTIC, unseen in training, our method reduces the object error by 56% and improves hand contact F1 from 0.866 to 0.921 over prior art. Our method recovers accurate full body-object interaction with coherent hand articulations and applies to online videos. Our code and pretrained models will be released.

</details>

#### 2026-11-24 - MemHand: Memory-Enhanced World-Space Hand Motion Reconstruction from Egocentric Videos

**Authors:** Junyi Ma, Zhangshuo Qi, Erhang Zhang, Mingjie Li, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2611.32876) - [pdf](https://arxiv.org/pdf/2611.32876)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion reconstruction, augmented reality

<details>
<summary>Abstract</summary>

Recovering the continuous world-space motion of both hands from egocentric video is essential for applications such as human-to-robot policy transfer and augmented reality. Achieving this goes beyond reconstructing the hands from each individual frame, as the context that a frame needs is often spread over time, especially around occlusions or when a hand moves out of sight. Recent works have explored how to exploit temporal context, yet they mostly draw it from fixed-length windows. Such windows cannot guarantee that every frame has the context required to reconstruct the hands in world space with accurate poses and metric scale. To address this limitation, we introduce MemHand, a memory-enhanced framework for world-space hand motion reconstruction. MemHand maintains two complementary forms of memory. The Short-Term Event Memory keeps the context of the well-observed hand around each occlusion or out-of-sight event and supplies it to frames with weak or missing visual evidence. In addition, since the metric scale holds over the whole recording, the Long-Term Scale Memory retains the most reliable observations across the video as scale anchors within a bounded state. Across benchmarks featuring severe occlusions and frequent out-of-sight intervals, MemHand achieves state-of-the-art accuracy and generalizes well to unseen domains. Benefiting from the synergy of both memories, it cuts W-MPJPE by 57\% on ARCTIC and 70\% on HOT3D relative to StableHand, delivering continuous and metrically accurate world-space hand poses and trajectories. We will release our code and models at the project page: https://irmvlab.github.io/memhand.github.io

</details>

#### 2026-11-24 - PRC4D: Physical Relation-Constrained Persistent 4D Reconstruction

**Authors:** Junho Kim, Hyunyoung Choi, Jiseok Kim, Seongwon Lee
**Links:** [abs](https://arxiv.org/abs/2611.32396) - [pdf](https://arxiv.org/pdf/2611.32396)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>Abstract</summary>

A faithful 4D reconstruction should capture both the shape and motion of objects, even when they disappear from view. Existing methods preserve previously observed geometry and extend motion through occlusion using local spatial and motion associations. However, treating short-term contact or shared motion as sufficient evidence of persistent rigidity can introduce incorrect motion constraints and distort overall reconstruction. To address this limitation, we present PRC4D, a physical relation-constrained framework that identifies reliable rigid relations and uses them to maintain spatial consistency through occlusion. PRC4D combines 3D contact and relative motion consistency with sequence-level verification to distinguish persistent couplings from transient interactions. The resulting graph guides observed-pose refinement and motion propagation from visible to occluded components without altering reconstructed geometry. Experiments on diverse real-world multi-object sequences and controlled occlusion simulations demonstrate improved reconstruction accuracy, reduced relative pose errors, and more consistent object configurations under changing visibility.

</details>

#### 2026-11-24 - ST-SfM: Spatio-Temporal Structure-from-Motion for Initialising 4D Gaussian Splatting

**Authors:** Harshit, Sami Brandt
**Links:** [abs](https://arxiv.org/abs/2611.32231) - [pdf](https://arxiv.org/pdf/2611.32231)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** dynamic 4D, dynamic Gaussian, 4D Gaussian, structure from motion, SfM, Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Dynamic Gaussian splatting is usually initialised either with random points or with a structure-from-motion (SfM) cloud of the first frame. Neither says anything about what moves, where and when. We introduce ST-SfM, a sparse spatio-temporal SfM for synchronised, calibrated multi-camera video that splits the scene into two branches. Static structure is detected once per camera on a temporal-median image, gated for temporal stability and matched along epi-polar lines. Motion is detected as space-time interest points (STIPs) in the video volume, described with HOG3D and matched only between candidates that agree both epipolarly and in time. Union-find tracks that refuse inconsistent merges are triangulated with RANSAC over all view pairs, giving static 3D points and dynamic 4D points (x, y, z, t) with sub-frame times. We use ST-SfM derived sparse 4D cloud to initialise 4D Gaussian splatting. In comparison with random initialisation on N3DV scenes we get improvements in PSNR, SSIM and LPIPS.

</details>

#### 2026-11-24 - MoGe-4D: Efficient, Flexible, and Unified Dense 4D Reconstruction and Tracking

**Authors:** Ruicheng Wang, Linlin Xin, Sicheng Xu, Jianfeng Xiang, Zelong Lv, Yu Deng, Yue Dong, Guangzhong Sun, Tong Zhang, Jiaolong Yang
**Links:** [abs](https://arxiv.org/abs/2611.32198) - [pdf](https://arxiv.org/pdf/2611.32198)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>Abstract</summary>

Reconstructing dynamic scenes from RGB video requires reasoning about both 3D geometry and motion across viewpoints, yet existing methods either split reconstruction and tracking into fragmented pipelines or face prohibitive dense spatiotemporal decoding costs. We introduce MoGe-4D, a feed-forward framework that unifies geometry and motion prediction via ordered queries of paired allocentric and egocentric dynamic point maps. Each query maps source pixels to a target time simultaneously in both camera frames, resolving relative camera pose in closed form while flexibly serving depth, dynamic registration, and dense 3D tracking. For efficient dense querying, MoGe-4D decouples scene modeling from query decoding: a high-capacity context encoder caches coarse global spatiotemporal features once, while a lightweight query encoder rapidly decodes dense point maps at flexible resolutions. Furthermore, as supervising dense 4D queries demands continuous 3D correspondences whose raw trajectory storage is prohibitive, we introduce RigIDTrack, a synthetic data pipeline and dataset that compresses surface dynamics into rigidity-regularized affine bodies, recovering exact arbitrary-frame 3D trajectories with $\sim15\%$ storage overhead over RGB-D video. Across diverse benchmarks, MoGe-4D achieves state-of-the-art dense 3D tracking, matches dedicated 3D foundation models in reconstruction, and runs substantially faster than prior 4D baselines.

</details>

#### 2026-11-23 - Tornado4D: Physics-Guided 4D Gaussian Reconstruction of a Laboratory Tornado from Sparse One-Sided Videos

**Authors:** Yucheng Zhu, Maria J. Molina, Christopher Metzler
**Links:** [abs](https://arxiv.org/abs/2611.31435) - [pdf](https://arxiv.org/pdf/2611.31435)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, 3DGS, novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Characterizing how tornadoes evolve over space and time is critically important for understanding and preparing for these highly destructive weather events. Towards this end, we develop algorithms capable of forming time-resolved 3D reconstructions of laboratory smoke tornadoes from sparse one-sided videos. Even in a controlled environment, reconstruction is severely underconstrained: appearance is view dependent, motion is non-rigid, and the unobserved volume admits many geometries. We present Tornado4D, a physics-guided 4D Gaussian framework capable of reconstructing laboratory tornadoes from sparse, one-sided videos. Tornado4D uses knowledge of the enclosure geometry to introduce rotational airflow field priors that constrain how the 3D structure evolves over time. These rotational priors allow us to reconstruct otherwise unobserved structure. We evaluate reconstruction accuracy by computing novel-view synthesis accuracy on a held out camera view: Tornado4D outperforms frame-by-frame 3DGS and video-based 4DGS by a considerable margin.

</details>

#### 2026-11-23 - HoloSplat: Real-Time Token Streaming for Feed-Forward Human Reconstruction

**Authors:** Chaofan Li, Qihan Ding, Shihan Wang, Zhehao Shen, Boyu Shen, Quanyu Chen, Haoyu Wu, Lan Xu, Xin Lou
**Links:** [abs](https://arxiv.org/abs/2611.31140) - [pdf](https://arxiv.org/pdf/2611.31140)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** human reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HoloSplat: Real-Time Token Streaming for Feed-Forward Human Reconstruction
- 作者：Chaofan Li, Qihan Ding, Shihan Wang, Zhehao Shen, Boyu Shen, Quanyu Chen, Haoyu Wu, Lan Xu, Xin Lou
- 出版日期：2026-11-23T18:11:00Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要页 https://arxiv.org/abs/2611.31140 ；PDF https://arxiv.org/pdf/2611.31140

### 一句话总结
HoloSplat 将前馈人体重建器拆分在高斯头之前，通过服务端 token 压缩与客户端 token 恢复的多码率流式编解码，实现实时、低带宽的人体自由视角体积视频流式传输。

### 研究问题
论文针对人体自由视角视频实时流式传输中的三重约束：每帧需实时重建、需在严格带宽预算内传输、需在轻量客户端 GPU 上解码。摘要指出，现有逐帧优化或前馈推理方法会产生超出实际流式传输上限的大量 3D Gaussian 数据，而激进压缩又会严重降低渲染质量。

### 核心思路/方法
HoloSplat 的核心是把前馈重建器在高斯头之前拆分，构建由服务端 token 压缩和客户端 token 恢复驱动的多码率流式编解码框架：
- 服务端：采用不透明度引导的 token 剪枝、基于 PCA 的降维，以及对 token anchors 的无损几何编码。
- 客户端：将特征重建超网络融合进高斯头，以恢复压缩导致的质量损失。
- 此外提出 Neural Session Calibration（NSC），在预热阶段利用 incoming camera views 在线快速微调高斯头，以解决新相机参数和变化采集条件带来的质量退化，并声称无逐帧开销。

### 主要贡献
- 提出面向人体中心体积视频的实时流式框架 HoloSplat，将前馈重建器拆分在高斯头之前，形成多码率 token 流式编解码。
- 设计服务端 token 压缩流程：不透明度引导 token 剪枝、PCA 降维、token anchors 无损几何编码。
- 设计客户端特征重建超网络并融合进高斯头，以补偿压缩引起的质量损失。
- 引入 Neural Session Calibration（NSC），在预热阶段在线微调高斯头，且无逐帧开销。
- 摘要给出的评估结果包括：四块 RTX 5090 GPU 上、50 Mbit/s 下平均 32.2 FPS；RTX 3050 Ti 笔记本 GPU 上每帧解码为 3D Gaussians 耗时 22.1 ms；相比未压缩 float32 Gaussians 传输数据量减少 22.8 倍；校准解码使 PSNR 提升 1.050 dB。

### 局限性
- 摘要未提供足够信息说明方法在极端带宽、复杂动态场景或不同人体外观条件下的失效情况。
- 摘要未提供足够信息说明 NSC 预热阶段的具体时长、收敛稳定性及对相机视角覆盖的依赖程度。
- 摘要未提供足够信息说明与更多基线方法的全面定量对比、用户研究或端到端延迟分解。
- 摘要未提供足够信息说明训练数据规模、泛化能力及跨数据集表现。
- 摘要未提供足够信息说明服务端计算开销、多路并发流式传输时的扩展性。

### 阅读优先级
中。理由：该论文聚焦人体体积视频实时流式传输这一明确应用问题，方法组合清晰，且摘要给出了帧率、带宽、解码时延、压缩比和 PSNR 等关键指标；但摘要未展开实验细节、基线对比和局限性，是否值得深入阅读取决于读者对动态/4D 重建、前馈人体重建与实时流式编解码方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Live free-viewpoint video streaming of humans enables immersive telepresence and interactive XR applications. However, this requires reconstructing each frame in real time, transmitting the data within strict bandwidth budgets, and decoding it on lightweight client GPUs. Existing approaches, whether relying on per-frame optimization or feed-forward inference, generate massive 3D Gaussian payloads that exceed practical streaming limits, while aggressive compression severely degrades rendering quality. In this work, we present HoloSplat, a real-time streaming framework for human-centric volumetric video. HoloSplat splits a feed-forward reconstructor before its Gaussian head, introducing a multi-rate streaming codec driven by server-side token compression and client-side token restoration. On the server side, we apply opacity-guided token pruning, PCA-based dimensionality reduction, and lossless geometry coding for token anchors. On the client side, a feature reconstruction hypernetwork is fused into the Gaussian head to recover compression-induced quality loss. Furthermore, we introduce Neural Session Calibration (NSC), which rapidly fine-tunes the Gaussian head online using incoming camera views during a warm-up phase. This resolves quality degradation from novel camera parameters and varying capture conditions with zero per-frame overhead. In our evaluations, HoloSplat averages 32.2 FPS on four RTX 5090 GPUs at 50 Mbit/s. It decodes each frame into 3D Gaussians in 22.1 ms on an RTX 3050 Ti laptop GPU, transmitting 22.8$\times$ less data than uncompressed float32 Gaussians, while calibrated decoding improves PSNR by 1.050 dB.

</details>

#### 2026-11-23 - ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild

**Authors:** Yuxi Wang, Yufei Liu, Chengkai Jin, Qingyue Chen, Wenqi Ouyang, Tianyi Wei, Kerui Ren, Siyuan Huang, Zhiqi Shen, Hongsheng Li, Xingang Pan
**Links:** [abs](https://arxiv.org/abs/2611.30597) - [pdf](https://arxiv.org/pdf/2611.30597)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** metric depth, motion reconstruction, depth estimation, manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild
- 作者：Yuxi Wang, Yufei Liu, Chengkai Jin, Qingyue Chen, Wenqi Ouyang, Tianyi Wei, Kerui Ren, Siyuan Huang, Zhiqi Shen, Hongsheng Li, Xingang Pan
- 出版日期：2026-11-23T12:33:36Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要页 https://arxiv.org/abs/2611.30597 ；PDF https://arxiv.org/pdf/2611.30597

### 一句话总结
ViDiHand2 将基于视频扩散模型（VDM）的手部深度估计从直接回归改为几何约束求解，并结合手部几何先验与置信度门控融合，以在野外人手视频中重建度量 3D 手部运动。

### 研究问题
摘要指出，从第一人称人类视频学习机器人操作需要准确的度量 3D 手部运动。现有方法利用预训练视频扩散模型先验从全帧视频直接恢复被遮挡的手，但其基于外观的深度回归对未见相机泛化较差。因此，论文关注的是：如何提升 VDM 框架下野外 3D 手部度量深度与运动重建的跨相机泛化能力，并增强遮挡与图像截断情形的鲁棒性。

### 核心思路/方法
- 将 VDM 基于手部深度估计的“直接回归”重构为“细粒度几何约束求解”，提出 **Fine-Grained Geometric Lifting** 与 **Clip-Level Ray Fitting**，通过强制像素对齐的 2D 关节与 MANO 手部度量结构之间的几何一致性来恢复度量深度，并利用片段内的时间观测。
- 由于几何 lifting 依赖 2D 关节，为提升遮挡和图像截断下的鲁棒性，提出 **Confidence-Gated Fusion**，根据定位置信度自适应融合几何 lifting 关节与 MANO 预测。
- 增强 VDM 主干以更好捕捉时空表示，并输出后续步骤依赖的逐帧 2D 关节与 MANO 预测。
- 摘要给出的效率信息为运行速度 57 FPS。

### 主要贡献
- 提出 ViDiHand2，一个几何驱动的框架，把 VDM 手部深度估计从直接回归转化为细粒度几何约束求解。
- 引入 Fine-Grained Geometric Lifting 与 Clip-Level Ray Fitting，以像素对齐 2D 关节和 MANO 度量结构的一致性恢复度量深度，并聚合片段级时间观测。
- 引入 Confidence-Gated Fusion，按定位置信度自适应融合几何 lifting 关节与 MANO 预测，以应对遮挡与图像截断。
- 增强 VDM 主干以提升时空表示，并产出逐帧 2D 关节与 MANO 预测。
- 摘要称在七个公开数据集上持续优于 18 个基线；与各指标最佳基线相比，野外绝对关节误差降低 42%，检测失败减少 8.82 倍，运行速度 57 FPS。

### 局限性
- 摘要未提供足够信息说明方法在何种相机、遮挡程度或运动模式下会失效。
- 摘要未提供足够信息说明七个公开数据集的具体构成、评测协议与误差指标定义。
- 摘要未提供足够信息说明 18 个基线的具体名单与对比细节。
- 摘要未提供足够信息说明 57 FPS 对应的硬件环境、输入分辨率或推理设置。
- 摘要未提供足够信息说明 Fine-Grained Geometric Lifting、Clip-Level Ray Fitting 与 Confidence-Gated Fusion 的消融结果。
- 摘要未提供足够信息说明增强 VDM 主干的网络结构改动与训练数据规模。

### 阅读优先级
中。理由：论文主题属于动态/4D 重建与手部运动重建，摘要明确给出几何约束求解、置信度融合和 VDM 主干增强三项方法要点，并报告了较显著的野外汇总指标与 57 FPS 效率；但摘要未给出数据集构成、评测协议、消融与硬件条件等细节。若读者关注野外度量 3D 手部重建、VDM 先验与几何先验结合，建议优先阅读方法和实验部分；若仅需一般性了解，摘要已覆盖核心主张。

</details>

<details>
<summary>Abstract</summary>

Learning robot manipulation from egocentric human videos requires accurate metric 3D hand motion. Recent methods leverage pretrained video diffusion model (VDM) priors to recover occluded hands directly from full-frame videos, but their appearance-based depth regression generalizes poorly to unseen cameras. In this work, we propose ViDiHand2, a geometry-driven framework that reformulates VDM-based hand depth estimation from direct regression into fine-grained geometric constraint solving. Specifically, we introduce Fine-Grained Geometric Lifting and Clip-Level Ray Fitting, which recover metric depth by enforcing geometric consistency between pixel-aligned 2D joints and the metric structure of MANO hands, while leveraging temporal observations across the clip. Since the lifting relies on these 2D joints, to improve robustness under occlusion and image truncation, we further develop Confidence-Gated Fusion to adaptively combine geometrically lifted joints with MANO predictions according to localization confidence. Finally, we enhance the VDM backbone to better capture spatial-temporal representations and produce the per-frame 2D joint and MANO predictions that both steps rely on. Extensive experiments on seven public datasets demonstrate that ViDiHand2 consistently outperforms 18 baselines, reducing in-the-wild absolute joint error by 42% and detection failures by 8.82x compared with the best baseline on each metric, while running at 57 FPS. The code is available at https://github.com/NTUYWANG103/ViDiHand.

</details>

#### 2026-11-23 - Dynamic Gaussian Scene Reconstruction by Integrating Events and Structural Priors

**Authors:** Zihao Yu, Guozhen Liu, Jie Yan, Jialiang Liu, Panlong Tan, Qinglin Sun, Hao Sun
**Links:** [abs](https://arxiv.org/abs/2611.29920) - [pdf](https://arxiv.org/pdf/2611.29920)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic Gaussian, scene reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dynamic Gaussian Scene Reconstruction by Integrating Events and Structural Priors
- 作者：Zihao Yu, Guozhen Liu, Jie Yan, Jialiang Liu, Panlong Tan, Qinglin Sun, Hao Sun
- 出版日期：2026-11-23T02:18:47Z
- 分类：Dynamic / 4D Reconstruction；3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.29920 ；PDF https://arxiv.org/pdf/2611.29920

### 一句话总结
针对基于事件的动态高斯重建在快速运动下依赖的两个易失效假设，提出 ESC-DGR，利用事件观测协同完成支撑补充、可靠运动参考选择与目标时刻残差预测，从而提升动态区域重建质量。

### 研究问题
摘要指出，现有基于事件的动态高斯重建依赖两个假设来支持“支撑增强”和“可靠性估计”：第一，已有高斯能够吸收重建误差；第二，光度优化已充分收敛，因而可用解析方差估计可靠性。两者在快速运动下都可能失效：前者失效时，缺少高斯支撑的区域无法生成致密化候选；后者失效时，运动区域中尚未收敛的高斯可能被排除为运动参考。论文要解决的是在这两类假设不成立时，如何仍获得可靠的支撑补充与运动参考，并改善事件驱动单目动态场景重建。

### 核心思路/方法
论文提出 Event-Structure Collaborative Dynamic Gaussian Reconstruction（ESC-DGR），使用不依赖上述两个条件的事件观测。具体包括：
- 事件首先识别需要额外支撑的变化区域，且仅在渲染深度有效的位置放置支撑；
- 增强表示仍需可靠运动参考，因此利用在线渲染统计与历史事件证据，将位移估计从可靠高斯传播到弱观测邻域；
- 这些参考描述帧间隔时间尺度上的主导运动，目标时刻事件进一步约束活动高斯的有界位置残差；
- 支撑放置、参考选择与残差预测在同一优化运行中作用于同一演化表示。

### 主要贡献
- 提出 ESC-DGR，将事件观测用于动态高斯重建中的支撑放置、运动参考选择与残差预测，并统一在一个优化运行内。
- 针对快速运动下“已有高斯吸收误差”和“光度优化已收敛”两个假设的失效问题，给出不依赖二者的替代方案。
- 在 E-D3DGS 基准的事件驱动单目动态场景重建上，所评估方法中取得最佳重建质量；相对 E-D3DGS，合成与真实场景的动态区域 PSNR（dPSNR）分别提升 1.02 和 1.45 dB。
- 八个合成场景的动态高斯总数减少 8.5%；虽平均帧率相对 E-D3DGS 下降约 21%–25%，但十二个场景渲染均保持高于 80 FPS。

### 局限性
- 摘要仅给出相对 E-D3DGS 的帧率下降比例与绝对帧率下限，未提供与其他方法的完整效率对比或计算开销分解。
- 摘要未提供失败案例、极端运动条件、不同事件传感器设置下的鲁棒性分析。
- 摘要未说明各模块的消融实验细节及各项设计对最终指标的独立贡献。
- 摘要未提供训练时间、显存占用、优化收敛速度等工程层面信息。
- 摘要未提供在 E-D3DGS 之外数据或场景类型上的泛化验证。
- 除 dPSNR 与动态高斯数量外，其他重建质量指标的具体数值摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对事件驱动动态高斯重建中两个明确且可检验的假设失效问题，方法链条完整（支撑放置—参考传播—残差约束），并给出相对基线 E-D3DGS 的定量提升与效率代价；同时涉及动态/4D 重建与神经场景表示，属于核心相关方向。若关注快速运动下的动态重建鲁棒性或事件相机与高斯表示的结合，优先级应设为高；若只关注静态重建或非事件方法，可降为中。

</details>

<details>
<summary>Abstract</summary>

Existing approaches to event-based dynamic Gaussian reconstruction rely on two assumptions for support augmentation and reliability estimation. First, existing Gaussians can absorb reconstruction errors. Second, photometric optimization has converged sufficiently to estimate reliability using analytical variance. Both assumptions can fail under fast motion. When the first fails, regions without Gaussian support cannot generate densification candidates. When the second fails, Gaussians in moving regions where optimization has not converged may be excluded as motion references. We propose Event-Structure Collaborative Dynamic Gaussian Reconstruction (ESC-DGR), using event observations independent of both conditions. Events first identify changes that require additional support, placed only where rendered depth is valid. The augmented representation still needs reliable motion references. Online rendering statistics and historical event evidence therefore propagate displacement estimates from reliable Gaussians to weakly observed neighborhoods. These references describe dominant motion at the frame-interval timescale. Target-time events therefore further condition bounded position residuals for active Gaussians. Support placement, reference selection, and residual prediction thus operate on the same evolving representation within one optimization run. For event-driven monocular dynamic scene reconstruction, our method achieves the best reconstruction quality among the evaluated methods on the E-D3DGS benchmark. Relative to E-D3DGS, dynamic-region PSNR (dPSNR) improves by 1.02 and 1.45 dB on synthetic and real scenes, respectively. The total dynamic Gaussian count across eight synthetic scenes decreases by 8.5%. Although mean frame rate decreases by about 21%-25% relative to E-D3DGS, rendering remains above 80 FPS in all twelve scenes. Code: https://github.com/zh-yu1/ESC-DGR.

</details>

#### 2026-11-22 - Continuous-time 4D Reconstruction via Event-guided Latent Feature Interpolation

**Authors:** Gwangtak Bae, Seunggu Kang, Junho Kim, Eun Sun Lee, Changwoon Choi, Young Min Kim
**Links:** [abs](https://arxiv.org/abs/2611.29838) - [pdf](https://arxiv.org/pdf/2611.29838)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Continuous-time 4D Reconstruction via Event-guided Latent Feature Interpolation
- 作者：Gwangtak Bae, Seunggu Kang, Junho Kim, Eun Sun Lee, Changwoon Choi, Young Min Kim
- 出版日期：2026-11-22T23:43:18Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.29838) / [PDF](https://arxiv.org/pdf/2611.29838)

### 一句话总结
提出一种连续时间 4D 重建方法，在潜特征空间中进行插值，并借助事件相机的微秒级测量作为引导，从而在任意时刻输出 3D 结构与相机位姿。

### 研究问题
现有几何基础模型能把视频序列转换为已配准的点云帧，但无法预测超出观测时间分辨率之外的时刻。事件相机虽能提供微秒级连续证据填补时间间隙，但将事件数据整合进现有基于 RGB 的基础模型仍具挑战性。

### 核心思路/方法
- 将连续时间重建表述为**潜特征空间中的插值**问题，以利用基础模型的几何先验。
- 在图像空间引入**事件损失**作为辅助任务，提供具有物理依据的引导以提升精度。
- 针对配对训练数据缺乏，提出**自监督训练框架**：使用估计几何的伪真值标签，以及由高帧率 RGB 视频生成的模拟事件。

### 主要贡献
- 提出连续时间 4D 重建管线，可在任意时刻提取 3D 结构与相机位姿。
- 以潜空间插值结合事件损失的方式整合事件相机引导与 RGB 基础模型。
- 提出面向配对数据缺失的自监督训练框架。
- 摘要声称：优于对输入 RGB 视频或估计几何做时间插值的基线，可泛化到未见真实场景，并在合成损坏受控实验中于运动模糊与低光条件下保持鲁棒。

### 局限性
- 具体网络结构、损失函数形式与实现细节：摘要未提供足够信息。
- 实验数据集、评价指标与定量结果：摘要未提供足够信息。
- 自监督伪真值与模拟事件的具体生成方式及误差影响：摘要未提供足够信息。
- 对事件相机硬件依赖、实时性、计算开销：摘要未提供足够信息。
- 泛化实验的规模与场景覆盖范围：摘要未提供足够信息。

### 阅读优先级
**中**。理由：选题聚焦连续时间 4D 重建与事件相机引导的结合，问题定义清晰，方法思路（潜空间插值 + 事件辅助损失 + 自监督）具有参考价值；但摘要未给出定量结果与实现细节，是否值得深入精读需结合全文实验部分判断。

</details>

<details>
<summary>Abstract</summary>

Recent geometric foundation models can successfully convert a video sequence into frames of registered point clouds, but cannot predict moments beyond the observed temporal resolution. We propose a continuous-time 4D reconstruction method that extracts 3D structure and camera poses at any time instant, with additional guidance from event-camera measurements. While event cameras provide evidence at microsecond resolution to continuously fill the temporal gap, integrating them into existing RGB-based foundation models remains challenging. We formulate the problem as interpolation in the latent feature space and augment event-based losses in the image space as an auxiliary task to boost accuracy. Operating in the latent space leverages the powerful geometric priors of foundation models, while the event loss provides physically grounded guidance. To effectively address the lack of paired training data, we further propose a self-supervised training framework that uses pseudo-ground-truth labels of estimated geometry and simulated events generated from high-frame-rate RGB videos. Through extensive experiments, we demonstrate that the proposed pipeline outperforms baselines that temporally interpolate either the input RGB videos or the estimated geometry, and that it generalizes to unseen real-world scenarios. Controlled experiments with synthetic corruptions show that it remains robust under motion-blur and low-light conditions.

</details>

#### 2026-11-22 - Ride on Anything: Contact-Coupled Monocular 4D Reconstruction of a Rider and Horse in Camera and World Frames

**Authors:** Zehang Weng, Ci Li
**Links:** [abs](https://arxiv.org/abs/2611.29435) - [pdf](https://arxiv.org/pdf/2611.29435)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Ride on Anything: Contact-Coupled Monocular 4D Reconstruction of a Rider and Horse in Camera and World Frames
- 作者：Zehang Weng, Ci Li
- 出版日期：2026-11-22T12:26:19Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.29435)｜[PDF](https://arxiv.org/pdf/2611.29435)

### 一句话总结
本文提出一种无需训练的测试时耦合方法 RoA，将分别冻结的人体估计器与马体估计器联合优化，以缓解单目视频中骑手悬浮、穿模和相对抖动等问题，并输出相机坐标系下的4D重建与世界坐标系下的重建结果。

### 研究问题
仅使用单目视频重建骑马者与马。如果独立应用人体估计器和马体估计器，两个网格虽能较好贴合各自轮廓，但骑手会悬浮在马旁、穿过马体、沿马背滑动并相对马抖动；这些误差沿相机轴方向，在输入视角下不可见。论文关注的是如何在不重新训练估计器的前提下，使骑手与坐骑在三维空间中保持接触一致。

### 核心思路/方法
- 提出 Ride on Anything（RoA）：一种通用的、无需训练的测试时方法，用于重建骑在动物上的人，并耦合冻结的骑手估计器与坐骑估计器。
- 面向骑马场景具体实例化：使用 SAM 3D Body 与 4DEquine。
- 技术要点包括：
  - 将两个估计器对齐到共同帧索引；
  - 通过一个由马体估计器初始化的像素各向同性相机投影两个对象；
  - 在马体坐标系下定义交互项，联合优化有界修正；
  - 使用基于广义绕数的碰撞项，且该碰撞项对非水密马体网格仍然有效；
  - 利用背景得到的相机旋转与 MoGe-2 得到的视场角，将结果提升到水平世界坐标系。

### 主要贡献
- 提出一种无需训练的测试时耦合框架，用于单目视频中“人骑动物”的4D重建。
- 针对骑马场景，引入共同帧对齐、统一相机投影、马体坐标系交互项及适用于非水密网格的碰撞项，以改善骑手与马体的接触一致性。
- 在骑马片段上报告了量化改善：
  - 骑手骨盆与马背平均距离从 15 cm 降至 1 cm；
  - 座位沿脊柱与横跨脊柱的漂移分别降低 64% 与 89%；
  - 90百分位穿透深度降低 57%；
  - 骑手表面位于马体内部的比例从 12.1% 降至 7.9%；
  - 骑手相对马的加速度降低 94%，马的 jerk 降低 80%；
  - 但骑手轮廓 IoU 从 0.59 降至 0.52。
- 定性上，骑手保持在马背上并与马一起运动。
- 还测试了一个任务外片段（徒步牵马），并分析了失败模式。

### 局限性
- 摘要明确指出，3D 精度的定量评估仍待对骑乘动物进行标定录制。
- 轮廓 IoU 从 0.59 降至 0.52，表明耦合优化可能牺牲部分二维轮廓拟合。
- 摘要仅提到对任务外“徒步牵马”片段进行了测试与失败模式分析，但未给出具体失败模式细节；摘要未提供足够信息。
- 该方法依赖冻结估计器（SAM 3D Body、4DEquine）及 MoGe-2 等组件；其泛化边界与对其他动物或估计器的适用性，摘要未提供足够信息。
- 实验规模、数据集构成、运行时间与计算开销等，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦单目4D重建中的接触耦合与穿模/悬浮问题，问题定义清晰，量化指标具体，且方法无需训练，具有一定实用价值；但摘要显示3D精度仍缺乏标定录制验证，且存在轮廓 IoU 下降与任务外失败模式，适合作为相关方向的方法参考而非确定性结论来源。

</details>

<details>
<summary>Abstract</summary>

We address the reconstruction of a horse and its rider from a single video. When a human estimator and a horse estimator are applied independently, both meshes can fit their silhouettes well while the rider hovers beside or passes through the horse, slides along its back and jitters relative to it. These errors lie along the camera axis and are not visible in the input view. We present Ride on Anything (RoA), a general, training-free methodology for reconstructing a person riding an animal, which couples frozen estimators of the rider and the mount at test time. We instantiate it for horseback riding with SAM 3D Body and 4DEquine. RoA aligns both estimators on a common frame index, projects both subjects through one pixel-isotropic camera initialized from the horse estimator, and jointly optimizes bounded corrections under interaction terms defined in the horse's body frame, including a collision term based on generalized winding numbers that remains valid on the non-watertight horse mesh. The result is lifted to a levelled world frame using the camera rotation from the background and the field of view from MoGe-2. On our riding clips, the raw outputs of the two estimators leave the rider's pelvis 15 cm from the horse's back on average. RoA reduces this seat gap to 1 cm, the drift of the seat along and across the spine by 64% and 89%, the 90th-percentile penetration depth by 57%, and the share of rider surface inside the horse from 12.1% to 7.9%. The motion is markedly smoother (94% lower acceleration of the rider relative to the horse, 80% lower horse jerk), while the rider's silhouette IoU decreases from 0.59 to 0.52. Qualitatively, the rider stays seated on the horse and moves together with it. A quantitative evaluation of 3D accuracy awaits calibrated recordings of ridden animals. We also test a clip outside the task, a horse led on foot, and analyse the failure modes.

</details>

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

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-24 - First-Hit Photoconsistency for Neural Surface Reconstruction

**Authors:** Gabriel Lenain, Edmond Boyer, Jean Ponce
**Links:** [abs](https://arxiv.org/abs/2611.32998) - [pdf](https://arxiv.org/pdf/2611.32998)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Recent neural implicit and Gaussian splatting approaches have achieved impressive results in multi-view surface reconstruction. However, jointly optimizing geometry and appearance introduces ambiguities. A parametric appearance model can compensate for geometric errors, reproducing the input images accurately without an accurate surface. We demonstrate accurate neural implicit surface reconstruction using only multi-view patch photoconsistency with geometry-based visibility, without volumetric rendering or parametric appearance models. For each reference ray, sphere tracing computes the first surface intersection. Its position and normal define a local patch whose photoconsistency is evaluated across visible neighboring views using colors sampled directly from the input images. For efficient sphere tracing, we use a 1-Lipschitz multi-layer perceptron. We use a single photoconsistency loss, without foreground masks or auxiliary geometric regularization. Experiments show that our method achieves the lowest mean Chamfer distance on BlendedMVS (BMVS) among compared methods and matches the geometric accuracy of leading reconstruction methods on DTU.

</details>

#### 2026-11-24 - CityRecast: Suppressing Persistent Artifacts in Generative Satellite 3D Reconstruction

**Authors:** Shuo Cui, Yingyan Hou, Wanxuan Lu, Hongfeng Yu, Daobing Zhang, Xian Sun
**Links:** [abs](https://arxiv.org/abs/2611.32863) - [pdf](https://arxiv.org/pdf/2611.32863)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>Abstract</summary>

Satellite-based 3D reconstruction is limited by sparse observations and changes across acquisition dates. Existing methods use generative priors to recover missing visual detail, but ghosting, streaking, and blur persist in their Gaussian scenes. These artifacts become particularly apparent in low-elevation renderings. We introduce CityRecast to suppress these artifacts through Gaussian scene repair and supervision calibration. To correct the Gaussian distributions that produce these artifacts, we first use multi-angle warm-up to constrain their spatial extent. This reduces the initial ghosting carried into progressive refinement. Surface-guided replacement then continues to repair the Gaussian distribution while preserving existing appearance. To provide more reliable supervision for this process, observation calibration mitigates interference from multi-temporal observations. Joint refinement further reduces conflicts among generated views. Experiments on DFC2019 and IARPA demonstrate reduced artifacts in low-elevation renderings while maintaining satellite-view fidelity. Compared with Skyfall-GS, CityRecast reduces FID-CLIP by 25.3% on DFC2019 and 51.8% on IARPA. MUSIQ increases by 14.54 and 24.95 points, respectively.

</details>

#### 2026-11-24 - DOPER: Deep Object Pose Estimation Revisited

**Authors:** Hugo Hadfield, Alperen Degirmenci, Jonathan Tremblay
**Links:** [abs](https://arxiv.org/abs/2611.32846) - [pdf](https://arxiv.org/pdf/2611.32846)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

We present DOPER, an RGB pose estimation framework that shares a visual backbone across object detection, segmentation, and keypoint prediction to recover the 6D pose of known objects through Perspective-n-Point. Starting from synthetic training, DOPER adapts to real observations using partial supervision while retaining synthetic keypoint labels. Calibrated multi-view observations provide geometric constraints for keypoint supervision. During inference, optional heatmap refinement fits a rigid pose directly to the predicted keypoint distributions, resolving ambiguous correspondences without depth input or a learned pose refiner. Starting from underspecified CAD models, DOPER progressively refines the object representation and pose estimator. Results on SPEED+ and SHIRT further demonstrate effective adaptation to illumination changes and accurate temporal pose estimation. Across the evaluated single-view and multi-view configurations, DOPER achieves state-of-the-art detection AP results on HANDAL, HOPEv2, HOT3D, and T-LESS while using only RGB and running in real time (35 Hz per object model on one GB300). These results demonstrate the effectiveness of jointly learning detection and pose keypoints, with real observations and geometric constraints.

</details>

#### 2026-11-24 - Diving Deeper into Dense Keypoint Localization in Object Pose Estimation

**Authors:** Jiahong Chen, Jinghao Wang, Yueneng Yang, Banglei Guan, Zi Wang, Dewen Hu, Qifeng Yu
**Links:** [abs](https://arxiv.org/abs/2611.32728) - [pdf](https://arxiv.org/pdf/2611.32728)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, localization

<details>
<summary>Abstract</summary>

6D pose estimation of rigid objects is a fundamental and challenging task in computer vision. Recent dense semantic keypoint-based methods employ binary encoding for efficient global keypoint localization, delivering strong performance in object pose estimation. Nevertheless, the discontinuous nature of binary encoding hinders effective training at high resolutions, while its inherent discrete and quantization errors lead to significant localization uncertainty. We propose GHLAPose, a global-to-local framework that synergizes hybrid Gray-binary (HGB) encoding with local-aware refinement (LAR). Specifically, HGB encoding first alleviates discontinuity to achieve accurate initial global keypoint localization. To further address intrinsic encoding errors, the LAR module estimates uncertainty and refines keypoint localization. This synergy enables a precise global-to-local strategy by aggregating global and local features. Extensive experiments on LM, LM-O, YCB-V, and TUD-L datasets demonstrate that GHLAPose surpasses state-of-the-art methods, particularly on fine-grained metrics. On LM-O, it outperforms the second-best method by 1.4% and 1.9% on ADD(-S) 0.02d and 0.05d respectively, and on YCB-V by 1% on ADD(-S) 0.1d. The code will be available at GHLAPose.

</details>

#### 2026-11-24 - RestPose: Canonicalization for Open Object Pose Estimation

**Authors:** Sandeep Inuganti, Weihang Li, Benjamin Busam, Didier Stricker, Jason Rambach
**Links:** [abs](https://arxiv.org/abs/2611.32696) - [pdf](https://arxiv.org/pdf/2611.32696)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

In object pose estimation methods, predicted poses are expressed with respect to a canonical frame, defined by a reference model of that object. In learning-based methods, an arbitrarily chosen modeling convention defines this canonical frame, which is then used to generate the ground-truth pose-annotations for training. Object pose estimation methods are therefore bound to such arbitrary conventions, restricting generalization. In this work, we propose that such a canonical frame can instead be derived for any object, and present RestPose, an approach towards open object pose estimation that does not require reference models or canonical frame conventions during training. From a single input image, we generate an object mesh and canonicalize it through a geometric and physical analysis of the object, then use foundation model-based dense matching to estimate the pose. We choose category-level benchmarks for our experiments, which contain instances across various object categories and enable us to measure the effectiveness of our canonicalization. Across HouseCat6D, NOCS, and Omni6DPose datasets, we improve on the supervised state-of-the-art methods by 18.3 points in absolute metrics and 13.8 points in scale-agnostic metrics, without requiring task-specific training. Code will be published.

</details>

#### 2026-11-24 - AirLeg: A Robust and Accurate Self-Supervised Visual-Inertial-Leg SLAM System

**Authors:** Kuan Xu, Tianxin Hu, Ruofei Bai, Ruimeng Liu, Yuefan Hao, Zeyu Jiang, Zitong Zhan, Shenghai Yuan, Chen Wang, Lihua Xie
**Links:** [abs](https://arxiv.org/abs/2611.32523) - [pdf](https://arxiv.org/pdf/2611.32523)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment, localization, simulation

<details>
<summary>Abstract</summary>

Visual-inertial-leg (VIL) state estimation offers cost-effective localization for legged robots, adding only a camera to the onboard IMU and joint encoders. However, learning-based leg odometry is limited by its supervision: networks trained in simulation suffer from the sim-to-real gap, while real-world labels require costly sensors or inherit the errors of visual estimates. To address this, we present AirLeg, a self-supervised VIL SLAM system in which vision and leg proprioception improve each other from training to deployment. We pre-train the leg odometry network in simulation and adapt it to the robot without ground truth through imperative learning, where multi-sensor bundle adjustment uses the leg odometry to refine the visual map, which in turn supervises the network. During deployment, the fused estimates adapt the network online. To improve both localization and this supervision, a dual-window estimator fuses vision, IMU, and leg odometry, relates loaded feet to the visually reconstructed terrain through a deformation-aware constraint, and weights the constraints by variance component estimation. AirLeg completes all 17 GrandTour sequences with the lowest average error (0.19 m) among 19 methods. On a low-cost quadruped, it achieves the lowest drift (0.6%) with only 0.5 h of unlabeled data, in real time on an embedded computer.

</details>

#### 2026-11-24 - DiffAnchor: Anchor-Space Diffusion for Monocular 3D Hand Pose Estimation

**Authors:** Changlong Jiang, Youci Tang, Haohong Kuang, Hang Xu, Jinghong Zheng, Ran Wang, Zhenghong Yu, Chen Feng, Xiaofeng Yue, Yang Xiao
**Links:** [abs](https://arxiv.org/abs/2611.32513) - [pdf](https://arxiv.org/pdf/2611.32513)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation, localization

<details>
<summary>Abstract</summary>

Accurate and efficient monocular 3D hand pose estimation is an important perception capability for embodied human interaction and dexterous manipulation. Recent diffusion-based methods model pose uncertainty by iteratively denoising 3D joint coordinates. However, directly diffusing the final joints requires the generative process to simultaneously explore plausible poses and recover precise coordinates, often relying on additional denoising steps or multiple hypotheses and consequently increasing inference cost. In this work, we propose DiffAnchor, a few-step anchor-space diffusion framework that diffuses anchors rather than joints. Our key insight is that stochastic exploration does not need to operate directly on the final output. Instead, diffusion searches for informative intermediate anchors that serve as local 3D regressors, while anchor-to-joint offset prediction and weighted aggregation complete precise joint localization. Specifically, fixed context anchors provide stable global references, whereas noisy dynamic anchors are iteratively refined toward informative joint regions. An importance-guided anchor selection and replenishment mechanism further retains useful anchors, removes ineffective ones, and explores insufficiently covered regions. This design reduces the precision burden of the diffusion process and enables accurate prediction using only a few denoising steps and a single hypothesis. Extensive experiments on HO-3D V2, NYU, ICVL, and InterHand2.6M demonstrate state-of-the-art performance on the first three benchmarks and competitive performance on challenging interacting-hand estimation, while maintaining inference efficiency comparable to deterministic regression baselines.

</details>

#### 2026-11-24 - COHERE4D: Training-Free Dense Surface Alignment for Coherent Metric 4D Human-Scene Reconstruction

**Authors:** Zhumei Wang, Shaofei Wang, Xiang An, Mingtao Pei, Siyuan Huang
**Links:** [abs](https://arxiv.org/abs/2611.32482) - [pdf](https://arxiv.org/pdf/2611.32482)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, scene reconstruction

<details>
<summary>Abstract</summary>

Human and scene foundation models offer complementary strengths for monocular 4D reconstruction: human models recover metric-scale body meshes but lack scene grounding, whereas scene models estimate globally consistent 3D geometry and camera motion without reliable metric scale. Crucially, both models reconstruct the same foreground human surface. Yet existing methods do not directly exploit this shared surface: lacking reliable foreground human geometry in scene reconstructions, earlier approaches either resort to sparse contact constraints or learn data-driven alignment modules that generalize poorly to out-of-distribution scenes. We present COHERE4D, a training-free framework that directly registers the human surfaces predicted by independently pretrained human and scene foundation models to reconstruct a coherent, metric 4D world. COHERE4D establishes dense, pixel-aligned 3D correspondences over the visible human surface and employs RANSAC with cross-frame consensus to suppress outliers from occlusion, background contamination, and depth noise. This formulation solves for two complementary geometric quantities: a sequence-level shared scale that calibrates scene geometry and camera motion to metric human size, and per-frame human translations that align camera-space human meshes with the scaled scene geometry to enforce spatial and temporal consistency. Across diverse backbones and benchmarks, COHERE4D substantially outperforms prior methods in human--scene alignment, metric scene and camera pose reconstruction, and global human motion estimation, adding only 4,ms/frame, enabling overall inference at up to 14 FPS.

</details>

#### 2026-11-24 - GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM

**Authors:** Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang
**Links:** [abs](https://arxiv.org/abs/2611.32335) - [pdf](https://arxiv.org/pdf/2611.32335)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** SLAM, pose estimation, geometric reconstruction, Gaussian Splatting, rendering, splatting, mapping

<details>
<summary>Abstract</summary>

Panoramic cameras capture nearly the entire spherical field of view in a single frame. However, the mismatch between this panoramic coverage and the field of view of LiDAR poses a substantial challenge for panoramic Gaussian splatting SLAM that relies on LiDAR depth priors. We introduce GOLD-SLAM, a Gaussian-splatting Omnidirectional LiDAR-Depth SLAM system that combines high-quality rendering with accurate geometric reconstruction. It performs tracking and mapping in the spherical domain and uses tracked visual features in regions without LiDAR coverage to improve pose estimation. To address insufficient coverage of newly observed surfaces and floating artifacts during incremental mapping, we introduce Depth-Aware Map Extension and Pruning (DAEP). To enable broader evaluation, we collect a new dataset, WHOLE, using a UAV platform across Weak-geometry, High-dynamic, Omnidirectional, Low-light, and Easy scenarios. Extensive experiments on public benchmarks and WHOLE demonstrate competitive rendering quality and improved geometric accuracy relative to perspective systems. Compared with existing panoramic baselines, GOLD-SLAM improves mean PSNR by 5.56-9.10 dB and reduces mean Depth-L1 by 71.9-83.9%. To assess deployment feasibility on resource-constrained platforms such as UAVs, we evaluate an embedded configuration of GOLD-SLAM on a Jetson Orin NX (16 GB), demonstrating online operation at the cost of reconstruction quality.

</details>

#### 2026-11-24 - EventSSM: Causal Spatial-State Modelling for Asynchronous Events Event-Depth Estimation

**Authors:** Sadiq O. Macaulay, Dipon Ghosh, Hadfield Simon
**Links:** [abs](https://arxiv.org/abs/2611.31720) - [pdf](https://arxiv.org/pdf/2611.31720)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation

<details>
<summary>Abstract</summary>

Event cameras report asynchronous brightness changes, yet metric-depth supervision is typically available only at sparsely sampled reference timestamps. Aggregating events into frame-like representations simplifies learning but can obscure the fine-grained temporal structure of the original event stream. We introduce EventSSM, a causal spatial-state framework for event-associated metric-depth estimation using a recurrent memory updated by chronological event packets. To bridge asynchronous predictions and frame-time supervision, predicted event depths are geometrically transported using calibrated camera poses and differentiably rendered at reference timestamps. Benchmark evaluations demonstrate improvements over established event-depth methods across multiple depth-error measures. Controlled ablations further examine cross-modal initialization, temporal recurrence, individual state, readout, and supervision components, and packet subdivision. Together, these findings establish EventSSM as an effective framework for causal event-associated metric-depth estimation, combining persistent spatial context with physically timed state retention.

</details>

#### 2026-11-23 - Anchoring VAE Fine-Tuning to Its Latent Diffusion Prior

**Authors:** Rafael Bischof, Dominik Narnhofer, Julius Erbach, Michael Kraus, Konrad Schindler, Bernd Bickel
**Links:** [abs](https://arxiv.org/abs/2611.31651) - [pdf](https://arxiv.org/pdf/2611.31651)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, simulation

<details>
<summary>Abstract</summary>

Pretrained latent diffusion models are effective priors for transfer learning, from geometry estimation to physics simulation. Existing approaches fine-tune the diffusion backbone but freeze the encoder of the VAE to preserve the latent distribution. However, a frozen encoder may miss salient details in non-RGB inputs and is limited to three channels. We introduce Diffusion Prior Anchoring (DPA), a regularizer applied during VAE fine-tuning that uses a score-distillation update to steer latents toward the high-density manifold on which the pretrained diffusion model denoises accurately. We validate DPA across three image and video models (FLUX 3, LTX-Video, Wan2.2) and four tasks: monocular depth estimation, MRI reconstruction, wind-flow simulation, and surface normal estimation, where DPA lowers the prediction error by 7.5% relative to the frozen VAE, 4.9% to decoder-only fine-tuning, and 4.0% to unanchored VAE fine-tuning. Its gain grows the further the target data lies from the RGB training distribution, from 3.3% on monocular depth estimation to 7.2% on complex-valued MRI. DPA also applies to modified VAEs, including pruned and multi-channel variants. With a four-channel VAE that encodes depth and surface normals, it lowers depth estimation error by 9.3%.

</details>

#### 2026-11-23 - InitFree-SfM: When Initialization-Free Bundle Adjustment meets Learned Structure-from-Motion

**Authors:** Simon Weber, Mateo de Mayo, Je Hyeong Hong, Carl Olsson, Daniel Cremers, Ronald Clark
**Links:** [abs](https://arxiv.org/abs/2611.31516) - [pdf](https://arxiv.org/pdf/2611.31516)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, structure from motion, SfM, bundle adjustment

<details>
<summary>Abstract</summary>

Initialization-free bundle adjustment (InitFree BA) aims to jointly recover camera poses and scene structure without requiring an initial global estimate. It is a very challenging problem, especially compared to traditional BA where a good estimation is assumed. While recent methods optimize surrogate Object Space Error (OSE) objectives from random initialization, a low objective value does not necessarily yield an accurate reconstruction, revealing a gap between optimization and reconstruction. We show that existing InitFree BA pipelines struggle to produce accurate 3D reconstructions on modern SfM benchmarks, and demonstrate that incorporating learned metric depth substantially improves their practical feasibility. We introduce InitFree-SfM, a complete initialization-free SfM pipeline combining learned correspondences, metric depth, depth-consistent track construction, and joint metric refinement. Within this framework, we propose a simple depth-augmented OSE (dOSE), which complements the directional constraints of OSE by constraining landmark positions along their viewing rays. Our approach substantially outperforms existing InitFree BA methods and achieves competitive accuracy with established SfM pipelines, including on challenging low-overlap image collections. Importantly, our analysis challenges the prevailing emphasis on surrogate objectives in previous InitFree BA research, revealing that geometric constraints play a central role in accurate reconstruction, while OSE-based optimization provides further improvements.

</details>

#### 2026-11-23 - Go Far, Look Less: Active Multi-Room Reconstruction with Persistent Goals and Selective Views

**Authors:** Jiawei Jiang, Haonan Zhou, Wendi Hu, Jiabei Hu, Yina Xiang, Kaiyue Zhou, Gaoang Wang
**Links:** [abs](https://arxiv.org/abs/2611.30802) - [pdf](https://arxiv.org/pdf/2611.30802)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, surface reconstruction, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Go Far, Look Less: Active Multi-Room Reconstruction with Persistent Goals and Selective Views
- 作者：Jiawei Jiang, Haonan Zhou, Wendi Hu, Jiabei Hu, Yina Xiang, Kaiyue Zhou, Gaoang Wang
- 出版日期：2026-11-23T15:02:53Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.30802) | [PDF](https://arxiv.org/pdf/2611.30802)

### 一句话总结
ROAM-GS 是一个免训练的主动多房间重建框架，通过“持久目标 + 选择性视角”缓解现有主动重建方法在多房间场景中短视评分与高帧率密集建图的缺陷。

### 研究问题
摘要指出，主动 3D 重建需要在稀疏视角预算下恢复完整几何与高保真渲染，但现有多数方法在多房间住宅中显著退化：短视的 next-best-view 评分不会为前往远处房间的移动赋予价值，并会过度优化近处无法消除的残差；而密集建图方法则需要流式处理数千帧才能到达远处房间。论文即针对多房间场景下稀疏视角预算分配与远距离房间覆盖的问题。

### 核心思路/方法
论文提出 ROAM-GS，一个免训练的主动多房间重建框架，将“持久目标”与“选择性视角”结合。每次决策选择一个目标以及通向该目标的变长前缀，仅在端点进行采集。方法使用 Surface Reconstruction Memory 通过投影更新后的缺陷与观察方向来评分位姿。持久目标会以剩余价值为“前往远处房间的移动”计入收益，并在到达后不再可测量地改善目标时释放。摘要称该方法无需逐场景调参。

### 主要贡献
- 提出 ROAM-GS，一个免训练的主动多房间重建框架，耦合持久目标与选择性视角。
- 引入 Surface Reconstruction Memory，用更新后缺陷的投影与观察方向进行位姿评分。
- 持久目标机制为前往远处房间的移动赋予剩余价值，并在目标不再可测量改善时释放。
- 摘要报告：在 HSSD 上将平均覆盖率从 74% 提升到 93%；在 HM3D 上从 47% 提升到 96%（+11.7 dB PSNR）；在保持单房间 Replica 保真度的同时，以约 173 倍更少的视角匹配 90 分钟密集建图。

### 局限性
- 摘要未提供足够信息说明计算开销、运行时间或内存占用。
- 摘要未提供足够信息说明方法在非住宅或多楼层等更复杂场景中的泛化表现。
- 摘要未提供足够信息说明失败案例、对传感器或相机运动假设的依赖。
- 摘要未提供足够信息说明与基线方法的完整定量对比细节与消融实验。

### 阅读优先级
中。理由：论文针对主动多房间 3D 重建中的稀疏视角分配问题，摘要给出了明确的覆盖率与 PSNR 提升，并声称以约 173 倍更少视角匹配密集建图，问题定义与结果指标较具体；但摘要未提供实验设置、基线细节与局限性信息，需阅读全文后才能判断方法可靠性与适用边界。

</details>

<details>
<summary>Abstract</summary>

Active 3D reconstruction aims to allocate a sparse view budget to recover complete geometry and high-fidelity renderings. However, existing methods degrade sharply in multi-room homes: myopic next-best-view scoring gives transit no credit for distant rooms and over-polishes irreducible nearby residuals, whereas dense mappers reach far rooms only by streaming thousands of frames. We propose ROAM-GS, a training-free active multi-room reconstruction framework that couples persistent goals with selective views: each decision selects a goal and a variable-horizon prefix toward it, capturing only at its endpoint. A Surface Reconstruction Memory scores poses by projecting post-update defects and viewing directions. Persistent goals credit transit with their remaining value and are released once arrivals stop measurably improving them. Without per-scene tuning, ROAM-GS achieves state-of-the-art multi-room reconstruction while preserving single-room Replica fidelity, raising mean coverage from 74% to 93% on HSSD and from 47% to 96% (+11.7 dB PSNR) on HM3D, and matching 90-minute dense mapping using $173\times$ fewer views.

</details>

#### 2026-11-23 - BridgeMVS: Bridging Multi-View Stereo and Monodepth via Bidirectional Dynamic Fusion

**Authors:** Jianfei Jiang, Haochen Yu, Qiankun Liu, Rui Yang, Hongyuan Liu, Xianglong Meng, Jiansheng Chen, Huimin Ma
**Links:** [abs](https://arxiv.org/abs/2611.30787) - [pdf](https://arxiv.org/pdf/2611.30787)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, 3D reconstruction, multi-view stereo, MVS, depth estimation, monocular depth, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BridgeMVS: Bridging Multi-View Stereo and Monodepth via Bidirectional Dynamic Fusion
- 作者：Jianfei Jiang, Haochen Yu, Qiankun Liu, Rui Yang, Hongyuan Liu, Xianglong Meng, Jiansheng Chen, Huimin Ma
- 出版日期：2026-11-23T14:49:54Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.30787 ；PDF https://arxiv.org/pdf/2611.30787 ；代码 https://github.com/JianfeiJ/BridgeMVS

### 一句话总结
BridgeMVS 通过双向动态融合（BDF）在级联多阶段 MVS 框架中双向桥接单目深度特征与多视图代价体表示，使 MVS 与单目深度估计相互增强，并在多个基准上取得领先结果。

### 研究问题
摘要指出，MVS 利用显式几何获得度量深度，但在特征匹配不可靠的困难区域表现不佳；MDE 能提供稳健的结构先验，但通常存在尺度模糊。现有混合方法主要以单向方式利用单目线索，对 MDE 与 MVS 之间的相互增强探索不足。论文要解决的问题即：如何在统一框架中充分实现单目深度与多视图几何的双向互补。

### 核心思路/方法
论文提出 BridgeMVS，一个统一的级联多阶段 MVS 框架，通过 Bidirectional Dynamic Fusion（BDF）连接单目深度特征与多视图代价体表示。在每个阶段，BDF 执行动态的 mono-to-cost 与 cost-to-mono 更新：单目结构特征用于引导代价体细化，以提升 MVS 深度估计的鲁棒性；多视图几何证据用于重新校准单目表示，以改善其度量尺度一致性。融合后的单目与多视图表示由粗到细逐阶段传播，并分别受阶段式相对尺度 MDE 监督和度量尺度 MVS 监督约束，使跨分支交互惠及后续高分辨率深度估计。BDF 还被设计为即插即用模块，可集成到现有级联 MVS 框架中。

### 主要贡献
- 指出并针对现有混合方法仅单向利用单目线索、MDE 与 MVS 相互增强不足的问题。
- 提出 BridgeMVS 统一级联多阶段 MVS 框架，核心为双向动态融合 BDF，实现 mono-to-cost 与 cost-to-mono 的动态更新。
- 通过由粗到细的跨阶段传播，以及阶段式相对尺度 MDE 监督与度量尺度 MVS 监督，联合约束两个分支。
- 将 BDF 设计为即插即用模块，便于集成到现有级联 MVS 框架。
- 摘要称在 DTU、Tanks-and-Temples 和 ETH3D 基准上达到 state-of-the-art，同时提升单目深度估计精度；并称在 Tanks-and-Temples Intermediate 与 Advanced 基准均排名第一。

### 局限性
- 摘要未提供足够信息说明 BDF 在各阶段的具体网络结构、融合算子细节与计算开销。
- 摘要未提供足够信息说明训练数据规模、训练策略、推理效率与显存占用。
- 摘要未提供足够信息给出各基准上的具体定量指标、消融实验细节及失败案例。
- 摘要未提供足够信息说明方法在极端弱纹理、重复纹理或透明反射等困难区域的具体表现边界。
- 摘要未提供足够信息说明即插即用模块在不同 MVS 框架上的泛化验证范围。

### 阅读优先级
高。理由：论文直接针对 MVS 与单目深度估计的互补融合这一核心问题，提出双向动态融合与即插即用模块，且摘要声称在 DTU、Tanks-and-Temples、ETH3D 上达到领先并同时提升 MDE 精度，属于 3D 重建与多视图几何方向中方法创新与基准表现均值得关注的工作；但具体实验细节需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Multi-View Stereo (MVS) and Monocular Depth Estimation (MDE) provide complementary cues for dense 3D reconstruction. While MVS leverages explicit geometry for metric depth, it struggles in challenging regions where feature matching is unreliable. Conversely, MDE provides robust structural priors but typically yields scale-ambiguous results. Existing hybrid methods mainly exploit monocular cues in a unidirectional manner, leaving the mutual enhancement between MDE and MVS insufficiently explored. To address this limitation, we propose BridgeMVS, a unified cascaded multi-stage MVS framework that bridges monocular depth features and multi-view cost volume representations through Bidirectional Dynamic Fusion (BDF). At each stage, BDF performs dynamic mono-to-cost and cost-to-mono updates, where monocular structural features guide cost volume refinement for more robust MVS depth estimation, while multi-view geometric evidence recalibrates monocular representations to improve their metric-scale consistency. Furthermore, the fused monocular and multi-view representations are progressively propagated from coarse to fine stages and constrained by stage-wise relative-scale MDE supervision and metric-scale MVS supervision, enabling cross-branch interactions to benefit subsequent high-resolution depth estimation. In addition, BDF is designed as a plug-and-play module that can be conveniently integrated into existing cascaded MVS frameworks. Extensive experiments demonstrate that BridgeMVS achieves state-of-the-art performance on the DTU, Tanks-and-Temples, and ETH3D benchmarks, while simultaneously boosting the accuracy of monocular depth estimation. Notably, BridgeMVS ranks first on both the Tanks-and-Temples Intermediate and Advanced benchmarks. The source code is available at \href{https://github.com/JianfeiJ/BridgeMVS}{https://github.com/JianfeiJ/BridgeMVS}.

</details>

#### 2026-11-23 - Screening for nonrigidity in structure from motion using projected reprojection residuals

**Authors:** Íñigo Cirauqui-Viloria
**Links:** [abs](https://arxiv.org/abs/2611.30769) - [pdf](https://arxiv.org/pdf/2611.30769)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Screening for nonrigidity in structure from motion using projected reprojection residuals
- 作者：Íñigo Cirauqui-Viloria
- 出版日期：2026-11-23T14:41:02Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.30769) / [PDF](https://arxiv.org/pdf/2611.30769)

### 一句话总结
论文提出一种基于投影重投影残差空间与时间排列模式的诊断方法，用于在稀疏 SfM 重建中筛查可能存在的非刚性形变，而不是仅依赖重投影误差的幅值汇总。

### 研究问题
稀疏 Structure from Motion（SfM）通常假设场景是静态的，但实际形变仍可能产生看似合理的重建结果。现有的重投影误差汇总方式会丢弃误差在点与视图之间的排列信息，因此难以发现仅从误差幅值看不出的不一致性。论文关注的问题是如何利用一次已有的 SfM 估计结果，对重建是否受到非刚性形变影响进行筛查。

### 核心思路/方法
论文提出的诊断方法首先去除那些可以由小幅点与相机调整、以及随时间变化的简单空间趋势所解释的残差成分；随后测量剩余残差与固定空间模式和时间模式的对齐程度。该方法只使用一个估计出的 SfM 重建，提供的是筛查证据，而不是物理形变估计。摘要还提到，该方法使用估计相机、3D 点和图像观测进行诊断。

### 主要贡献
- 提出一种利用重投影误差在点与视图之间排列方式的诊断方法，用于筛查 SfM 重建中的非刚性迹象。
- 在四个合成管状族上，该诊断检测到了全部八个带有规定运动的采集，而重投影误差幅值汇总方法仅检测到五或六个。
- 在同一截断值设置下，该诊断在覆盖外观变化和重建流程变化的 20 个重建变体中保留了 19 个正检测，并有 1 次数值弃权。
- 作者强调，重投影误差的排列方式可以揭示其幅值单独会遗漏的不一致性。

### 局限性
- 摘要明确指出，该诊断只提供筛查证据，不是物理形变估计。
- 四个合成族在开发过程中已知，迁移变体复用了其中两个族，说明评估设置存在已知数据范围限制。
- 截断值设置为每个族使用其他三个族中最高的静态分数，因此得分最高的静态采集也会被筛查为阳性。
- 摘要未提供足够信息说明真实场景数据上的验证情况。
- 摘要未提供足够信息说明方法对噪声、外点、相机标定误差等实际因素的鲁棒性。
- 摘要未提供足够信息说明计算复杂度、参数敏感性及更大规模数据集上的表现。

### 阅读优先级
中。理由：该论文针对 SfM 中静态假设与非刚性形变之间的不一致性提出筛查工具，问题具有实际意义，且方法强调利用残差排列信息而非仅看幅值。但摘要显示评估主要基于合成管状族和有限变体，且作者明确将其定位为筛查证据而非形变估计；是否适合直接用于真实复杂场景，需要进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Sparse structure from motion (SfM) assumes a static scene, yet deformation may still yield plausible reconstructions. Reprojection-error summaries discard how errors are arranged across points and views. We propose a diagnostic that first removes residual components explainable by small point and camera adjustments and simple spatial trends that change over time. It then measures alignment with fixed spatial and temporal patterns. The diagnostic uses one estimated SfM reconstruction and provides screening evidence rather than a physical deformation estimate. Across four synthetic tubular families, the diagnostic detected all eight acquisitions with prescribed motion, compared with five or six for summaries of reprojection-error magnitude. Each family's cutoff was the highest static score among the other three families, so the static acquisition with the highest score also screened positive. With the same cutoffs, the diagnostic retained positive detections in 19 of 20 reconstruction variants spanning changes in appearance and reconstruction pipeline, with one numerical abstention. These findings show that the arrangement of reprojection errors across points and views can reveal inconsistencies that their magnitudes alone miss. The four families were known during development, and the transfer variants reused two of them. Within this setting, the diagnostic offers a practical way to flag a plausible reconstruction for closer inspection using only its estimated cameras, 3D points and image observations.

</details>

#### 2026-11-23 - Place-Revisit Consistency Evaluation of Reference Poses

**Authors:** Jianzhu Huai, Yujia Zhang, Grzegorz Jozkow
**Links:** [abs](https://arxiv.org/abs/2611.30741) - [pdf](https://arxiv.org/pdf/2611.30741)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, pose estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Place-Revisit Consistency Evaluation of Reference Poses
- 作者：Jianzhu Huai, Yujia Zhang, Grzegorz Jozkow
- 出版日期：2026-11-23T14:19:47Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[abstract_url](https://arxiv.org/abs/2611.30741) / [pdf_url](https://arxiv.org/pdf/2611.30741)

### 一句话总结
论文提出一种基于“重访地点一致性”的参考位姿评估方法，用于检测移动感知数据集中公开参考轨迹存在的局部不一致问题。

### 研究问题
参考轨迹被广泛用于评估里程计和同步定位与建图（SLAM）系统，但基准参考位姿中的局部不一致可能会使这类评估产生偏差。论文关注的问题是：如何识别并评估参考轨迹中这类局部不一致。

### 核心思路/方法
论文利用“地点重访”作为一致性检验条件：当平台在足够时间间隔后重新访问先前观察过的地点时，参考轨迹所隐含的相对位姿应当与直接从车载传感器估计出的相对位姿一致。作者用激光雷达扫描配准和立体图像位姿估计来实例化这一思路，并将其应用于 KITTI Odometry 和 SNAIL Radar。

### 主要贡献
- 提出一种面向移动感知数据集中参考位姿的“地点重访一致性”评估方法。
- 以激光雷达扫描配准和立体图像位姿估计两种方式实现该一致性检验。
- 在 KITTI Odometry 分析中识别出若干重访区域，公开参考位姿与传感器导出的相对位姿不一致，平移差异中位数最高达 6.60 m。
- 通过代表性点云叠加进一步定位这些差异，支持将地点重访用作基准验证工具。

### 局限性
摘要未提供足够信息。摘要未说明方法对传感器类型、重访检测阈值、时间间隔条件等的敏感性，也未给出 SNAIL Radar 上的具体结果细节或失败案例。

### 阅读优先级
中。理由：该工作与使用 KITTI 等基准评估里程计/SLAM 的研究直接相关，尤其适合关注基准数据质量与评估偏差的读者；但摘要仅给出方法框架和 KITTI 上的部分发现，未提供完整实验细节，需阅读全文后才能判断其普适性与影响范围。

</details>

<details>
<summary>Abstract</summary>

Reference trajectories are widely used to evaluate odometry and simultaneous localization and mapping systems. However, local inconsistencies in benchmark reference poses can bias such evaluations. This paper presents a place-revisit consistency evaluation method for reference poses in mobile sensing datasets. When a platform revisits a previously observed place after a sufficient temporal gap, the relative pose implied by the reference trajectory should agree with relative poses estimated directly from onboard sensors. We instantiate this idea with lidar scan registration and stereo-image pose estimation, and apply it to the KITTI Odometry and SNAIL Radar. The KITTI analysis identifies several revisit regions where the public reference poses disagree with sensor-derived relative poses, with median translation discrepancies up to 6.60 m. Representative point-cloud overlays further localize these discrepancies and support the use of place revisits as a benchmark-validation tool.

</details>

#### 2026-11-22 - A ROS2 based Human-In-The-Loop Framework for UAV Search and Rescue Operations

**Authors:** Anubhav Pandey, Harshit Nagpal, Aditya Agarwal, Tejasvi Alladi, Fei Richard Yu
**Links:** [abs](https://arxiv.org/abs/2611.29507) - [pdf](https://arxiv.org/pdf/2611.29507)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, depth estimation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A ROS2 based Human-In-The-Loop Framework for UAV Search and Rescue Operations
- 作者：Anubhav Pandey, Harshit Nagpal, Aditya Agarwal, Tejasvi Alladi, Fei Richard Yu
- 出版日期：2026-11-22T14:25:55Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.29507) / [PDF](https://arxiv.org/pdf/2611.29507)

### 一句话总结
论文提出一个基于 ROS2 的人在回路（HITL）框架，利用 RGB-D 传感与 YOLOv11 将人的左右方向手势转换为无人机导航指令，面向退化搜救环境强调鲁棒性与实时部署。

### 研究问题
现有无人机自主框架缺乏人类情境意识，限制了其在非结构化搜救（SAR）环境中的实时适应性。同时，ROS1 已弃用，需要迁移到 ROS2，并优先考虑实时通信、可扩展性与长期可维护性。论文关注的是在退化 SAR 环境中实现鲁棒、实时部署，而非理想条件下的峰值精度。

### 核心思路/方法
- 构建基于 ROS2 的人在回路（HITL）框架，将人类方向手势（左/右）翻译为 UAV 导航命令。
- 使用 RGB-Depth（RGB-D）传感与 YOLOv11 进行手势识别。
- 采用深度加权姿态估计与自适应 RGB-D 融合，并建模时间一致性。
- 通过 ROS2 数据分发服务（DDS）实现实时部署。
- 在 Gazebo-PX4 仿真中评估，并在公开 UAV-GESTURE 数据集上对真实人员评估，覆盖清晰空气与 Koschmieder 雾条件。

### 主要贡献
- 提出面向 UAV SAR 的 ROS2 HITL 框架，使无人机可直接响应操作员手势，无需复杂路径规划。
- 在遮挡与变化环境条件下，深度估计达到 89% 置信度（Gazebo-PX4 仿真）。
- 雾天条件下，RGB-D 融合在所有场景与距离上平均比仅 RGB 提供更有信息量的线索，平均提升 46.7%。
- 展示更优的遮挡处理（+15%）、自适应 RGB-D 融合、时间一致性建模，以及端到端延迟低于 50 ms 的实时部署。
- 不重新训练时，框架对真实人员手势读取准确率为 80%；在能见度 10 m 时深度保持 77%，而 RGB 降至 24%；修改后的 YOLOv11 在仿真中达到 91%，在真实数据训练后于留出真实人员上达到 99%。
- 开源 ROS2 实现便于 SAR-UAV 平台从 ROS1 迁移。

### 局限性
- 摘要未提供足够信息说明真实户外 SAR 场景中的完整部署验证。
- 摘要未提供足够信息说明框架在多人、复杂手势或多模态指令下的表现。
- 摘要未提供足够信息说明计算资源需求、功耗与平台载荷限制。
- 摘要未提供足够信息说明除左右方向手势外的手势类别覆盖范围。
- 摘要未提供足够信息说明与完整自主导航或路径规划方法的系统对比。

### 阅读优先级
中。理由：该工作聚焦 ROS2 迁移、HITL 手势控制与退化环境鲁棒性，对 UAV 搜救与人机交互方向有明确参考价值；但摘要未提供完整实验细节与真实场景部署证据，且主分类与 3D 重建相关度有限，适合按需深入阅读。

</details>

<details>
<summary>Abstract</summary>

Existing Unmanned Aerial Vehicle (UAV) autonomy frameworks lack human contextual awareness, limiting real-time adaptability in unstructured Search and Rescue (SAR) environments. To address data availability, we propose a Robot Operating System (ROS2)-based human-in-the-loop (HITL) framework that translates human directional gestures (left/right) into UAV navigation commands using RGB-Depth (RGB-D) sensing and YOLOv11 (You Only Look Once). The deprecation of ROS1 necessitates migrating to ROS2, prioritising real-time communication, scalability, and long-term maintainability. Unlike approaches optimised for peak accuracy under ideal conditions, the proposed system prioritises robustness and real-time deployment in degraded SAR environments. Our system achieves 89% confidence in depth estimation under occlusion and varying environmental conditions in Gazebo-PX4 simulations. In foggy conditions, RGB-D fusion consistently provides more informative cues than RGB alone, with an average improvement of 46.7% across all scenarios and distances. The framework demonstrates superior occlusion handling (+15%), adaptive RGB-D fusion, temporal consistency modelling, and real-time deployment via a ROS2 data distribution service (DDS), with end-to-end latency below 50 ms. We evaluate the modified YOLOv11 and the depth-weighted pose estimation on a held-out simulated test set and on real people from the public UAV-GESTURE dataset, in clear air and in Koschmieder fog. Without retraining, the framework reads the gestures of real people with 80% accuracy, depth keeps 77% at a visibility of 10 m where RGB drops to 24%, and the modified YOLOv11 reaches 91% in simulation and 99% on held-out real people when trained on real data. The open-source ROS2 implementation eases the transition of SAR-UAV platforms from ROS1, enabling UAVs to act directly on operator gestures without complex path planning.

</details>

#### 2026-11-22 - MIMORPHEUS: Rethinking Cross-Modal Supervision for Human Pose Estimation from Radar Signals

**Authors:** Shizhao Zhang, Yanyan Zhang, Deshui Yu, Jun Pan, Guangyou Fang
**Links:** [abs](https://arxiv.org/abs/2611.29341) - [pdf](https://arxiv.org/pdf/2611.29341)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MIMORPHEUS: Rethinking Cross-Modal Supervision for Human Pose Estimation from Radar Signals
- 作者：Shizhao Zhang, Yanyan Zhang, Deshui Yu, Jun Pan, Guangyou Fang
- 出版日期：2026-11-22T09:18:48Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.29341 ；PDF https://arxiv.org/pdf/2611.29341

### 一句话总结
MIMORPHEUS 提出一种基于条件扩散的框架，从 3D 人体姿态生成雷达回波，以缓解雷达-姿态配对数据稀缺问题，并用于雷达数据增强与视觉姿态标注的跨模态利用。

### 研究问题
论文关注穿墙 MIMO 雷达人体姿态估计中的数据瓶颈：构建成对的雷达与姿态数据集耗时耗力，大规模视觉姿态数据集没有对应雷达回波，物理仿真虽可生成合成信号但依赖散射建模专业知识，且可能存在仿真与真实数据之间的差距。

### 核心思路/方法
MIMORPHEUS 通过条件扩散从 3D 人体姿态生成雷达回波。具体包括：
- MIMO-VAE 按回波的信道与快时间采样结构压缩回波；
- SkeleCoder 通过对比对齐学习与回波特征对应的姿态特征；
- 这些姿态特征用于引导 MIMO-VAE 隐空间中的扩散过程；
- VAE 解码器从生成的隐变量重建回波。

训练完成后，生成器可为已记录姿态产生不同回波以增强雷达数据，并为现有视觉数据集中的姿态标注补充雷达模态。

### 主要贡献
- 提出 MIMORPHEUS 框架，利用条件扩散从 3D 人体姿态生成雷达回波。
- 设计 MIMO-VAE 压缩回波，并设计 SkeleCoder 通过对比对齐学习姿态特征。
- 在数据增强实验中，方法在四个雷达姿态估计器上使 MPJPE 降低 6.8%-11.2%。
- 在三个公开姿态数据集上的迁移实验表明，视觉姿态标注可提供有用的雷达训练数据。
- 摘要称代码将在 GitHub 公开。

### 局限性
摘要未提供足够信息说明以下局限：方法对真实雷达数据分布差异的鲁棒性、生成回波与真实回波的定量差距、计算成本、对特定雷达配置或姿态范围的依赖，以及失败场景。摘要仅提到物理仿真可能存在仿真与真实数据差距，但未给出 MIMORPHEUS 自身在此方面的定量评估。

### 阅读优先级
中。理由：该论文针对雷达人体姿态估计中配对数据稀缺这一明确问题，提出跨模态生成与数据增强思路，并报告了 MPJPE 降低和迁移实验结果，具有一定方法参考价值；但摘要未提供更详细的实验设置、对比基线、生成质量评估和局限性分析，需阅读全文后才能判断其泛化性与实用程度。

</details>

<details>
<summary>Abstract</summary>

Deep learning has shown promise for estimating human pose with multiple-input multiple-output (MIMO) radar through walls. Building paired radar and pose datasets demands considerable time and manual effort, while large visual pose datasets provide no corresponding radar echoes. Physical simulation can supply synthetic signals, but requires expertise in scattering models and can leave a gap between simulated and real data. To address this challenge, we introduce MIMORPHEUS, a framework that generates radar echoes from 3D human poses through conditional diffusion. To prepare echo and pose representations, MIMO-VAE compresses the echoes according to their channel and fast time sample structure, while SkeleCoder learns pose features through contrastive alignment with echo features. These pose features then guide diffusion in the MIMO-VAE latent space, and the VAE decoder reconstructs echoes from the generated latents. Once trained, the generator augments radar data by producing different echoes for a recorded pose and supplies the radar modality for pose annotations in existing visual datasets. In data augmentation experiments, our method reduces MPJPE by 6.8%-11.2% across four radar pose estimators. Transfer experiments with three public pose datasets also show that visual pose annotations can supply useful radar training data. Code will be made publicly available on GitHub.

</details>

#### 2026-11-22 - Inclusive Hand Pose Estimation via Topology-Aware Distillation and Progressive Kinematic Reasoning

**Authors:** Kanglei Zhou, Zikai Hao, Liyuan Wang, Xiaohui Liang
**Links:** [abs](https://arxiv.org/abs/2611.29163) - [pdf](https://arxiv.org/pdf/2611.29163)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Inclusive Hand Pose Estimation via Topology-Aware Distillation and Progressive Kinematic Reasoning
- 作者：Kanglei Zhou, Zikai Hao, Liyuan Wang, Xiaohui Liang
- 出版日期：2026-11-22T02:48:32Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.29163) / [PDF](https://arxiv.org/pdf/2611.29163)

### 一句话总结
论文针对手部运动结构中部分关节持续缺失时的姿态估计退化问题，构建了 IncNYU 基准并提出 InsHaPE 框架，通过拓扑感知蒸馏与渐进式运动链推理提升结构不完整条件下的鲁棒性，同时保持完整手部上的性能。

### 研究问题
现有手部姿态估计方法大多假设手部结构完全articulated（具有完整关节结构），当运动结构中的部分组件持续缺失时，预测会变得不稳定或不合理，即使存在可用的部分观测，也可能导致性能下降甚至系统失效。论文旨在研究并缓解这种结构不完整性带来的鲁棒性问题。

### 核心思路/方法
- 构建 IncNYU：一个具有生理约束的基准，通过对完整手部模型进行形态学修改来模拟结构不完整性，并保留完整区域与合成移除区域的参考位置。
- 提出 InsHaPE：一个面向结构不完整性的包容式手部姿态估计框架，目标是在结构缺失时保持鲁棒，同时在标准完整手部上保持性能。
- 基于分层运动学建模，引入两个互补组件：
  1. 拓扑感知蒸馏策略：从完整articulated手部表示中迁移关节级与关系级先验，在结构缺失时提供解剖学一致的初始化。
  2. 渐进式运动学推理模块：沿运动链进行结构化推理，在严重结构变化下实现完整且解剖学一致的姿态估计。
- 实验涉及 NYU/IncNYU，并在 MSRA 上进行外部验证；摘要称其在结构不完整下提升鲁棒性，并在完整手部上保持有竞争力的性能，同时系统级评估显示对需要固定拓扑手部姿态表示的下游应用有鲁棒性收益。

### 主要贡献
- 明确指出并系统研究手部姿态估计中“结构不完整性”这一挑战。
- 构建 IncNYU 基准，用于模拟和评估手部结构不完整条件下的姿态估计。
- 提出 InsHaPE 框架，结合拓扑感知蒸馏与渐进式运动学推理，以在结构缺失下保持解剖学一致性和鲁棒性。
- 在 NYU/IncNYU 与 MSRA 上开展实验，并给出系统级下游应用评估，说明方法在结构不完整条件下的鲁棒性优势。

### 局限性
- 摘要未提供足够信息说明 IncNYU 的具体规模、数据构成与标注细节。
- 摘要未提供足够信息说明各模块的消融实验细节与定量增益。
- 摘要未提供足够信息说明方法在真实结构缺失场景与合成缺失场景之间的差异。
- 摘要未提供足够信息说明计算开销、推理效率或部署约束。
- 摘要未提供足够信息说明失败案例与适用边界。

### 阅读优先级
中。理由：该论文聚焦手部姿态估计在结构不完整条件下的鲁棒性，问题定义清晰，且包含新基准与系统级评估，对关注鲁棒手部姿态估计或下游固定拓扑表示应用的研究者有参考价值；但摘要未给出具体实验细节与定量结果，是否高优先级阅读需结合对 IncNYU 基准和运动学推理方法的兴趣进一步判断。

</details>

<details>
<summary>Abstract</summary>

Hand pose estimation aims to recover the spatial configuration of hand joints from visual observations and serves as a fundamental perception module for downstream systems that rely on complete and topologically consistent hand representations. Most existing methods are developed under the assumption of fully articulated hand structures and tend to produce unstable or implausible predictions when parts of the kinematic structure are persistently absent, resulting in degraded performance or even system failure despite available partial observations. To study this challenge, we construct IncNYU, a physiologically constrained benchmark that simulates structural incompleteness through morphological modification of complete hand models and retains reference locations for both intact and synthetically removed regions. Based on this benchmark, we propose InsHaPE, an Inclusive Hand Pose Estimation framework designed to remain robust under structural incompleteness while preserving performance on standard, fully articulated hands. Built on hierarchical kinematic modeling, InsHaPE introduces two complementary components. First, a topology-aware distillation strategy transfers joint-level and relational priors from fully articulated hand representations, providing anatomically consistent initialization under missing structures. Second, a progressive kinematic reasoning module performs structured inference along the kinematic chain, enabling complete and anatomically consistent pose estimation under severe structural variations. Extensive experiments on NYU/IncNYU, together with external validation on MSRA, demonstrate that InsHaPE improves robustness under structural incompleteness while maintaining competitive performance on complete hands. System-level evaluations further show that InsHaPE improves robustness for downstream applications that require fixed-topology hand pose representations.

</details>

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

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-24 - Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild

**Authors:** Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng
**Links:** [abs](https://arxiv.org/abs/2611.33145) - [pdf](https://arxiv.org/pdf/2611.33145)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, localization

<details>
<summary>Abstract</summary>

Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial reasoning in static images or synthetic indoor environments, where semantic shortcuts often suffice, making it difficult to faithfully evaluate spatial reasoning capabilities in the wild. In light of this, we present Lost on Campus, a benchmark for evaluating ESR in large-scale real-world outdoor 3D environments reconstructed by 3D Gaussian Splatting. Our benchmark introduces a unified reasoning-action evaluation framework that seamlessly integrates diagnostic QA for isolated reasoning with closed-loop interactive navigation for active reasoning under multimodal instructions. To enable fine-grained diagnosis, we evaluate six capability aspects of ESR: action grounding, spatial foresight, metric awareness, goal-directed planning, ego-allocentric localization, and spatio-temporal consistency. Extensive experiments reveal that: (i) Compared to indoor settings, real-world outdoor environments impose substantially higher demands on spatial reasoning, where existing models exhibit poor performance; (ii) VLMs still struggle with fine-grained visual alignment, with failures in spatial foresight and ego-allocentric localization emerging as primary bottlenecks; (iii) Improving multimodal interaction capabilities and long-term spatial reasoning is crucial for advancing embodied intelligence. These findings highlight that faithful evaluation of ESR demands benchmarks tightly coupling perception, reasoning and action within realistic and continuous environments.

</details>

#### 2026-11-24 - AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline

**Authors:** Nicola Leonetti, Federico Stella, Aoxiang Fan, Saqib Javed, Pascal Fua, Luigi Di Stefano
**Links:** [abs](https://arxiv.org/abs/2611.32735) - [pdf](https://arxiv.org/pdf/2611.32735)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Feedforward 3D Gaussian Splatting (3DGS) pipelines reconstruct a scene from images in a single forward pass, representing it as real-time-renderable 3D Gaussians. However, the resulting representations contain far more Gaussians than are needed to render the scene faithfully, especially when there are many input views. This drastically increases memory and storage requirements. Existing pruning methods either require costly re-optimization, which defeats the purpose of a single forward pass, or rely on simple strategies that do not exploit all the available information. We present AnyPrune, a transformer-based, optimization-free pruning module designed to work on top of any feedforward 3DGS pipeline. To remove unnecessary Gaussians, AnyPrune learns and exploits pipeline-specific redundancy patterns through a short single-GPU training on the frozen target feedforward pipeline. AnyPrune achieves better rendering quality than existing optimization-free pruning methods in most settings and generalizes to unseen datasets, as shown through extensive experiments across multiple feedforward pipelines, datasets, and input view counts. It prunes a 1.6M-Gaussian field in about $5\,\mathrm{s}$ on a consumer GPU, faster than every method that merges Gaussians or re-optimizes the field. It can also be combined with the pruning built into feedforward pipelines, pruning further at moderate ratios while preserving or improving rendering quality. Finally, it can even suggest a scene-specific pruning ratio that retains most of the quality.

</details>

#### 2026-11-24 - Completion-Aware Compression for Progressive 3D Gaussian Splatting

**Authors:** Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu
**Links:** [abs](https://arxiv.org/abs/2611.32628) - [pdf](https://arxiv.org/pdf/2611.32628)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables high-quality novel-view rendering, but its large scene representations are costly to transmit. Pruning and compression reduce file sizes, yet progressive delivery also requires usable reconstructions before the full scene arrives. Existing progressive representations provide partial scenes, but level-based updates are limited by predefined coding boundaries. This paper presents a progressive 3DGS codec that balances attribute fidelity with the image benefit of making Gaussians available earlier. Its single compact stream supports partial 3D reconstruction and adds newly decoded Gaussians as more bytes arrive. The stream supports fine-grained updates at arbitrary received-byte budgets, without separate encodings or later attribute refinement. At matched complete-file sizes and received bytes, completion-aware allocation improves 1/8 PSNR over attribute-only allocation by 0.48-1.43 dB. The proposed codec compresses original 3DGS representations by 62-88 times while retaining near-reference Full PSNR. Under the evaluated 50-Mbps delivery model, partial reconstruction becomes available in approximately 0.2 s.

</details>

#### 2026-11-24 - Mind the Band: The Hidden Frequency Variable in Geometric RoPE

**Authors:** Seonghyun Jin, Youngmin Kim, Jong Chul Ye
**Links:** [abs](https://arxiv.org/abs/2611.32171) - [pdf](https://arxiv.org/pdf/2611.32171)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** depth estimation, novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Geometric rotary position encodings (RoPE) incorporate 3D camera geometry into multi-view attention by rotating token features according to viewing rays, depths, and reprojected image coordinates. Each coordinate is rotated across a progression of frequencies--its frequency band--yet existing implementations leave this band to inherited defaults, either retaining standard 2D RoPE's top frequency or letting the frequency span grow exponentially with the attention head dimension. We show that this unstandardized setting can reverse benchmark rankings. In novel view synthesis on RealEstate10K, RayRoPE matches the strongest baseline in the 47M model (144-channel heads), yet trails by 1.2 dB in the 25M model (48-channel heads), and exhibits the same reversal when varying head size alone at fixed model width. Populating a 243x range with four frequencies instead of the 3x default at 48 channels recovers 0.9 dB of that gap. Across view synthesis and two-view depth estimation, overly narrow bands consistently blur correspondence, whereas all three projection-based encodings perform reliably when their top frequency lies within 0.3--3 rotations per 8-pixel patch (10--90 rotations across 256x256 RealEstate10K). At the opposite extreme, overly wide bands degrade RayRoPE through a forward-backward asymmetry: averaging rotations over a predicted depth interval damps high frequencies in the forward pass, yet leaves their gradients with respect to predicted depth undamped. Blocking only those high-frequency depth gradients recovers 90--93% of the lost PSNR, showing that forward smoothing does not guarantee backward stability. Guided by this analysis, we distill practical guidelines--setting bands in image coordinates, populating spans in small heads, and avoiding unconditional same-view damping--and advocate reporting and matching frequency bands in future multi-view benchmarks.

</details>

#### 2026-11-24 - View Management with Gaussian Placement and Opacity Regularization for Online 3DGS

**Authors:** Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim
**Links:** [abs](https://arxiv.org/abs/2611.32025) - [pdf](https://arxiv.org/pdf/2611.32025)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, mapping, localization

<details>
<summary>Abstract</summary>

The realistic rendering of 3D Gaussian Splatting (3DGS) has drawn interest from real-time applications that require maps to be built online. This led to coupling 3DGS with SLAM, providing camera poses and initial Gaussians for the map. However, the map is still optimized with designs inherited from conventional SLAM, which train only on keyframes selected for localization and regularize geometry with uncertain frontend depth. These designs overlook the model complexity of a 3DGS map: with millions of parameters but few views of each region, the map overfits to sparse inputs. Resolving this is challenging, as every view and Gaussian added to the map competes for the same real-time budget. We close this gap from both sides. To add views while keyframes preserve the structure of the map, we progressively admit non-keyframe images as mapping updates complete and allocate the limited updates across different groups of frames according to the supervision each group provides. To control the model complexity of the map, edge-guided initialization places new Gaussians where image detail requires them. To complement the uncertain frontend depth, Self-Referenced Opacity Regularization (SOR) uses accumulated rendering evidence, at no extra rendering cost, to suppress the opacity of Gaussians that persistently contribute in front of a map-derived surface reference. Together, these designs improve both the appearance and the geometry of online maps within the real-time budget.

</details>

#### 2026-11-24 - HiGS: A Hierarchical Architecture for Fast Differentiable 3D Gaussian Splatting

**Authors:** Dawid Pająk, Martin Bisson, Rodolfo Lima, François Trudel
**Links:** [abs](https://arxiv.org/abs/2611.31918) - [pdf](https://arxiv.org/pdf/2611.31918)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) makes one screen tile the cell of partitioning, the cell of rasterization, and the unit of parallel work. Partitioning favors large tiles and rasterization small ones, and with one unit per tile the densest tiles set the frame time. We present Hierarchically Tiled Gaussian Splatting (HiGS), a unified architecture for rendering and reconstruction that gives each role its own granularity: Gaussians are partitioned over coarse macro-tiles, rasterized over the fine render tiles within them, and processed in bounded depth-sorted batches. A dense region issues more batches instead of one longer unit, so frame time follows the work in a view rather than its densest tile. The same batches carry reconstruction: compositing supplies the transmittance and color needed to differentiate each one independently, leaving optimizer memory traffic as the dominant training cost. We fuse the optimizer into the backward pass, halve the parameters and moments it stores and updates directly, and defer appearance updates outside the view. HiGS renders scenes faster than every published method we evaluate, by the widest margin on views with uneven load, and reconstructs them faster and in less memory, at equal image quality and with exact front-to-back alpha compositing.

</details>

#### 2026-11-23 - Collision Rendering: GPU-Accelerated Trajectory Planning on Sparse Voxel Radiance Fields with Risk-Bounded Collision Checking

**Authors:** Byoungkwon Yoon, Han Gyeom Lee, Hojun Lee, Yuseop Sim, Daniel Sungwoo Bae, Martin Byung-Guk Jun
**Links:** [abs](https://arxiv.org/abs/2611.31658) - [pdf](https://arxiv.org/pdf/2611.31658)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, rendering, radiance, robotics

<details>
<summary>Abstract</summary>

Although radiance fields provide detailed scene representations for robotics, they remain underexplored for trajectory planning, without a widely agreed-upon way to translate learned spatial primitives into reliable collision criteria. To bridge this gap, we introduce Collision Rendering, the first trajectory planning framework on sparse voxel radiance fields (SVR), which supports GPU-accelerated, risk-bounded collision checking and a differentiable collision cost. Our key insight is that the structured volumetric density of SVR allows its rendering pipeline to serve as a fast numerical approximator of collision probability. We approximate the robot with collision spheres and place a coinciding spherical camera at each sphere. Under a probabilistic collision model, we derive an upper bound on each sphere's maximum directional collision probability from the camera's rendering pipeline. Evaluating this bound on the GPU yields a modular collision checker that integrates with established sampling-based planners without an auxiliary geometric map or changes to the learned representation. We further compute a collision cost and its gradients from rendered opacities through the same pipeline, extending the framework to trajectory optimization. Experiments demonstrate millisecond collision checking time on a consumer-grade GPU and collision-free trajectories in all queries, outperforming other radiance field-based planners.

</details>

#### 2026-11-23 - InterGS+: Inter-Frame Gaussian Splatting Compression with Geometry-Aware Transformer Prediction and Adaptive Residual Coding

**Authors:** Muhammad Talha, Zhu Li, Joel Jung
**Links:** [abs](https://arxiv.org/abs/2611.31482) - [pdf](https://arxiv.org/pdf/2611.31482)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic 3D, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (3DGS) provides real-time photorealistic rendering, but representing each frame as irregular Gaussian primitives with high-dimensional attributes creates substantial storage and transmission cost. Exploiting temporal redundancy is challenging because Gaussian primitives do not preserve fixed identities across frames. We propose InterGS+, a lightweight post-hoc inter-frame codec that jointly improves temporal prediction and residual representation. Current-frame geometry is coded with G-PCC and reconstructed before prediction, enabling consistent temporal neighborhoods at encoder and decoder. Attributes are predicted using lightweight KNN and bilateral predictors together with a geometry-aware transformer for spherical-harmonic (SH) appearance, with per-Gaussian mode selection. Residual coding is adapted to each attribute: SH innovations are coded in a shared PCA domain using vector quantization with refinement, opacity and scale in activated gamma-companded domains, and rotation as canonicalized quaternion innovations using vector quantization and refinement. On MPEG dynamic sequences, InterGS+ achieves average BD-rate reductions of 45.48% over G-PCC Amd. 1 and 7.78% over InterGS-Lite, with corresponding BD-PSNR gains of 9.98 dB and 1.10 dB. Average decoding complexity is 0.049 ms/Gaussian, demonstrating efficient streamable dynamic 3DGS compression.

</details>

#### 2026-11-23 - Enhancing Sparse-View Gaussian Splatting with Feed-Forward Priors via Spectral Fusion and Distillation

**Authors:** Weikai Lin, Jun Dai, Sheng Zhao, Junjie Zhao, Yuhao Zhu
**Links:** [abs](https://arxiv.org/abs/2611.31428) - [pdf](https://arxiv.org/pdf/2611.31428)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>Abstract</summary>

Gaussian splatting from sparse training views renders high-quality images near training views, but reconstruction quality degrades at distant regions, which are undersampled by the training set. Feed-forward novel view synthesis (NVS) models use strong learned priors to resample the scene from substantially different viewpoints, but they take more than ten times as long to render and produce high-frequency artifacts on out-of-domain scenes. We propose a plug-and-play method that enhances an existing sparse-view Gaussian model with a pretrained feed-forward NVS model. We observe that the two are complementary in the frequency domain: the prior is more accurate at low frequencies, and the Gaussians at high frequencies. The reliability of the prior relative to the Gaussians is inversely proportional to the image frequency, so the optimal fusion weight is a first-order low-pass filter with one parameter that can be fitted. Our key idea is then to intelligently fuse the reliable part of each of the two methods. To remove the slow feed-forward model at render time, we use these fused images as teachers and distill them back into Gaussians, balanced with supervision from input views. Our method improves the quality of various sparse-view Gaussian methods without sacrificing rendering speed, and our analysis works on different prior models. Project page: https://linwk20.github.io/spectral-fusion-gs/

</details>

#### 2026-11-23 - Tokens as Locality-Preserving Anchors: Scalable Novel View Synthesis with Target-Adaptive Token Routing

**Authors:** Sagnik Ghosh, Aswin C. Sankaranarayanan
**Links:** [abs](https://arxiv.org/abs/2611.31156) - [pdf](https://arxiv.org/pdf/2611.31156)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tokens as Locality-Preserving Anchors: Scalable Novel View Synthesis with Target-Adaptive Token Routing
- 作者：Sagnik Ghosh, Aswin C. Sankaranarayanan
- 出版日期：2026-11-23T18:21:37Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.31156 ；PDF https://arxiv.org/pdf/2611.31156

### 一句话总结
论文提出将源图像 token 视为保持局部性的空间锚点，并用轻量路由器按目标视角只选取固定预算的高排名 token 供解码器注意，从而使渲染成本不再随源 token 数增长。

### 研究问题
基于 Transformer 的新视角合成模型不依赖显式 3D 表示，能复现细节和视角相关效果，但其解码器对每一帧都要关注所有源 token，导致渲染随源图像增多而变慢。光栅化可通过剔除视角不可见图元来避免这一问题，但源 token 没有显式位置或范围，无法直接按此方式剔除。

### 核心思路/方法
关键洞察是：源 token 虽然是隐式的，但仍可视为空间锚点，每个 token 编码场景的局部区域，因此对任一视角，解码器的注意力只集中在少数 token 上。方法使用一个轻量路由器，根据源 token 和目标视角预测这些关键 token；解码器只关注排名最高的固定预算 token，使成本不再依赖源 token 总数。路由器以解码器注意力作为监督信号，并使用非最大抑制降低冗余 token 的排名。由于一次排序可服务所有预算，渲染时预算可以动态改变。

### 主要贡献
- 提出将源 token 作为保持局部性的锚点，用于按目标视角路由 token。
- 设计轻量路由器预测需关注的少量 token，使解码器只处理固定预算的 top-ranked token，从而解除渲染成本与源 token 数量的耦合。
- 使用解码器注意力监督路由器，并通过非最大抑制压低冗余 token。
- 摘要报告：在 24 张源图像和“两个视角 worth of tokens”的设置下，模型渲染速度比 LagerNVS 快 6.4 倍，PSNR 仅低 0.68 dB；且一次排名服务所有预算，预算可在渲染时更改。

### 局限性
摘要未提供足够信息来说明方法在更多源图像、不同数据集、不同视角数量下的泛化表现，也未提供路由器训练开销、内存占用、失败案例或与更多基线方法的完整比较。摘要未提供足够信息说明“两个视角 worth of tokens”的具体定义及固定预算的选取范围。

### 阅读优先级
中。理由：论文针对 Transformer 新视角合成的可扩展性瓶颈提出清晰的 token 路由思路，并有明确的加速与质量折中数据；但摘要未给出更广泛实验细节，是否适合精读取决于对高效神经渲染与 token 稀疏化方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Transformer-based view synthesis models render each target viewpoint from the source images, without an explicit 3D representation, which lets them reproduce fine detail and view-dependent effects. However, their decoder attends to every source token for every frame, so rendering slows with each source image. Rasterization avoids this by culling primitives that the viewpoint does not see, but source tokens cannot be culled this way, as they have no explicit position or extent. Our key insight is that source tokens are nonetheless spatial anchors: each encodes a local region of the scene, so the decoder's attention for any viewpoint concentrates on a few of them. A lightweight router predicts these tokens from the source tokens and the viewpoint, and the decoder attends only to a fixed budget of top-ranked tokens, so its cost no longer depends on the number of source tokens. We supervise the router with the decoder's attention, using non-maximum suppression to demote redundant tokens. With 24 source images and two views' worth of tokens, our model renders 6.4 times faster than LagerNVS, at a PSNR only 0.68 dB lower. One ranking serves every budget, so the budget can change at render time.

</details>

#### 2026-11-23 - WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild

**Authors:** Richard Shaw, Arthur Moreau, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero
**Links:** [abs](https://arxiv.org/abs/2611.31023) - [pdf](https://arxiv.org/pdf/2611.31023)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild
- 作者：Richard Shaw, Arthur Moreau, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero
- 出版日期：2026-11-23T17:05:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.31023) / [PDF](https://arxiv.org/pdf/2611.31023)

### 一句话总结
提出 WildAnySplat 前馈式 3D Gaussian Splatting 框架，利用学生-教师学习与瞬态掩码、双边网格等设计，提升从野外多视角图像进行新视角合成的鲁棒性与外观一致性。

### 研究问题
野外多视角图像常因瞬态遮挡物、光照变化和相机 ISP 导致多视角不一致，从而降低现有前馈重建方法的质量。论文旨在解决这一条件下鲁棒新视角合成的问题。

### 核心思路/方法
- 采用学生-教师框架：教师网络处理干净图像，学生网络处理对应的野外输入；教师提供干净监督，引导学生学习一致的规范表示。
- 由于成对的干净与野外数据稀缺，采用混合数据策略：真实配对采集、合成增强，以及由基于优化的重建生成的伪干净标签，以弥合合成与真实数据的域差距。
- 使用 Transformer 架构，并以专用 DPT 头分别预测相机位姿、深度和高斯。
- 额外预测逐视角瞬态掩码，用于重加权光度监督并抑制不可靠高斯。
- 引入双边网格模块建模逐图像颜色变换，以处理跨视角外观变化并恢复规范辐射表示。

### 主要贡献
- 提出面向野外多视角图像的前馈 3D Gaussian Splatting 框架 WildAnySplat。
- 引入学生-教师学习框架，以获得对瞬态变化鲁棒且外观一致的 3D 表示。
- 设计混合数据策略，结合真实配对、合成增强与伪干净标签，缓解配对数据稀缺问题。
- 通过瞬态掩码重加权光度监督，并用双边网格建模逐图像颜色变换。
- 摘要称在具有挑战性的野外基准上，方法提升了对瞬态遮挡和外观变化的鲁棒性，同时保留前馈高斯泼溅的快速推理。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算开销细节、对特定数据类型的依赖程度或定量实验的完整限制。摘要仅提及使用伪干净标签等混合数据策略，但未提供其误差传播或泛化边界的分析。

### 阅读优先级
中。理由：论文聚焦野外前馈 3DGS 的鲁棒重建，问题明确且方法组合具有针对性；但摘要未给出定量结果、基线对比细节和充分局限性说明，是否优先精读取决于读者对野外前馈高斯泼溅与鲁棒新视角合成的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

We present WildAnySplat, a feed-forward 3D Gaussian Splatting framework that enables robust novel-view synthesis from in-the-wild multi-view images. Unlike controlled captures, real-world images often contain multi-view inconsistencies caused by transient occluders, illumination changes, and camera ISP, which degrade the quality of existing feed-forward reconstruction methods. To address this challenge, we introduce a student-teacher framework that learns transient-robust and appearance-consistent 3D representations. A teacher network operates on clean images, while a student processes the corresponding in-the-wild inputs. The teacher provides clean supervision to guide the student toward a consistent canonical representation. Since paired clean and in-the-wild data are scarce, we use a hybrid data strategy, combining real paired captures, synthetic augmentations, and pseudo-clean labels generated from optimization-based reconstructions, bridging the domain gap between synthetic and real-world data. We adopt a transformer architecture with dedicated DPT heads for camera pose, depth, and Gaussian prediction. We additionally predict per-view transient masks to reweight photometric supervision and suppress unreliable Gaussians. To account for cross-view appearance variation, we incorporate a bilateral grid module that models per-image color transformations and enables recovery of a canonical radiance representation. Experiments on challenging in-the-wild benchmarks show that WildAnySplat improves robustness to transient occlusions and appearance variation while retaining the fast inference of feed-forward Gaussian Splatting.

</details>

#### 2026-11-23 - GSDet: Gaussian Splatting for Oriented Object Detection

**Authors:** Zeyu Ding, Jiaqi Zhao, Yong Zhou, Wen-liang Du, Hancheng Zhu, Rui Yao
**Links:** [abs](https://arxiv.org/abs/2611.30602) - [pdf](https://arxiv.org/pdf/2611.30602)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GSDet: Gaussian Splatting for Oriented Object Detection
- 作者：Zeyu Ding, Jiaqi Zhao, Yong Zhou, Wen-liang Du, Hancheng Zhu, Rui Yao
- 出版日期：2026-11-23T12:39:05Z
- 分类：主分类为 Neural Scene Representations & Rendering；无二级分类信息
- 链接：摘要页 https://arxiv.org/abs/2611.30602 ；PDF https://arxiv.org/pdf/2611.30602

### 一句话总结
GSDet 提出将定向目标检测表述为高斯泼溅，在由图像特征构建的 3D 特征空间中以 3D 高斯表示定向目标，再投影为 2D 高斯并转换为定向框。

### 研究问题
摘要指出，现代定向目标检测器依赖预定义的目标候选，例如 CNN 方法中的锚框或 transformer 方法中的查询，这些候选难以有效捕捉空间信息。论文旨在解决这一限制。

### 核心思路/方法
- 将定向目标检测建模为高斯泼溅框架。
- 在由图像特征构建的 3D 特征空间中执行检测，使用 3D 高斯表示定向目标。
- 将 3D 高斯投影到图像平面形成 2D 高斯，再转换为定向框。
- 使用包含 3D 高斯采样的解码器，优化随机初始化 3D 高斯的均值、各向异性协方差和置信度分数。
- 方法具有灵活性，可在推理时进行自适应控制并使用动态数量的高斯。

### 主要贡献
- 提出 GSDet 框架，将定向目标检测表述为高斯泼溅。
- 用 3D 高斯表示定向目标，并通过投影与变换得到定向框，以替代对预定义目标候选的依赖。
- 设计带 3D 高斯采样的解码器，优化高斯的均值、各向异性协方差与置信度分数。
- 支持推理阶段的自适应控制和动态高斯数量。
- 摘要报告在 3 个数据集上的结果：采用自适应控制评估时，DIOR-R 的 AP₅₀ 提升 0.7%，DOTA-v1.0 提升 0.3%，DOTA-v1.5 提升 0.55%，并优于主流检测器。

### 局限性
- 摘要仅给出 AP₅₀ 提升数值，未提供完整实验设置、对比基线细节、消融实验和失败案例分析；摘要未提供足够信息。
- 未说明方法在不同数据集、目标尺度、密集场景或计算开销方面的具体限制；摘要未提供足够信息。
- 未提供推理效率、训练成本、参数敏感性等信息；摘要未提供足够信息。

### 阅读优先级
中。理由：该论文将高斯泼溅引入定向目标检测，问题动机和方法表述较清晰，且摘要报告了三个数据集上的 AP₅₀ 增益；但摘要未提供充分的实验细节与局限性信息，是否值得深入阅读需结合全文的实验严谨性、效率表现和可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Oriented object detection has advanced with the development of convolutional neural networks (CNNs) and transformers. However, modern detectors still rely on predefined object candidates, such as anchors in CNN-based methods or queries in transformer-based methods, which struggle to capture spatial information effectively. To address the limitations, we propose GSDet, a novel framework that formulates oriented object detection as Gaussian splatting. Specifically, our approach performs detection within a 3D feature space constructed from image features, where 3D Gaussians are employed to represent oriented objects. These 3D Gaussians are projected onto the image plane to form 2D Gaussians, which are then transformed into oriented boxes. Furthermore, we optimize the mean, anisotropic covariance, and confidence scores of these randomly initialized 3D Gaussians, using a decoder that incorporates 3D Gaussian sampling. Moreover, our method exhibits flexibility, enabling adaptive control and a dynamic number of Gaussians during inference. Experiments on 3 datasets indicate that GSDet achieves AP$_{50}$ gains of 0.7\% on DIOR-R, 0.3\% on DOTA-v1.0, and 0.55\% on DOTA-v1.5 when evaluated with adaptive control and outperforms mainstream detectors.

</details>

#### 2026-11-23 - NNS-GS: Non-Local Neural Scattering for Relightable Gaussian Splatting

**Authors:** Shiyu Liang, Yang Gao, Lili Wang, Aimin Hao, Beibei Wang
**Links:** [abs](https://arxiv.org/abs/2611.30351) - [pdf](https://arxiv.org/pdf/2611.30351)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NNS-GS: Non-Local Neural Scattering for Relightable Gaussian Splatting
- 作者：Shiyu Liang, Yang Gao, Lili Wang, Aimin Hao, Beibei Wang
- 出版日期：2026-11-23T09:23:15Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.30351 ；PDF https://arxiv.org/pdf/2611.30351

### 一句话总结
提出 NNS-GS，用非局部神经散射模块与几何引导的局部反射模块，从 Gaussian Splatting 表示中学习可重光照的半透明物体，并缓解局部特征散射模型难以刻画次表面散射跨区域影响的问题。

### 研究问题
论文关注半透明物体的可重光照 3D 资产创建。摘要指出，改变某一表面位置的光照会通过次表面散射影响其他位置的外观；而现有基于 Gaussian 的散射模型通常从局部特征预测散射，难以捕捉这种跨位置依赖关系。因此核心问题是：如何在 Gaussian Splatting 框架中学习非局部散射，并同时处理反射、高光和阴影边界等外观成分。

### 核心思路/方法
NNS-GS 将非局部散射学习与几何引导的局部反射结合：
- 散射模块：在光空间中学习“可见表面区域的光照”如何贡献到视图空间中的着色点，并以区域漫反射响应和空间关系为条件。
- 反射模块：提供上述漫反射响应，并利用额外几何引导，以更好地捕捉镜面高光和锐利阴影边界。
- 训练策略：采用基于锚点的渐进式训练，先建立漫反射-散射基座，再引入镜面反射，并对各成分分别监督，以减少成分混合并支持可控的散射外观。

### 主要贡献
- 提出 NNS-GS，将非局部散射学习引入可重光照 Gaussian Splatting，用于半透明物体建模。
- 设计散射模块，在光空间与视图空间之间建立光照贡献关系，并以区域漫反射响应和空间关系为条件。
- 将几何引导的局部反射模块与非局部散射模块结合，以改善镜面高光和阴影边界表现。
- 采用基于锚点的渐进式训练与分成分监督，减少成分混合并支持可控散射外观。
- 摘要报告：在标定点光照下，合成与真实半透明场景的平均 PSNR 分别较现有方法提升 2.47 dB 和 0.81 dB；额外合成比较显示在调整散射衰减时 NNS-GS 更接近参考结果。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算开销、对训练数据或标定点光照的依赖程度、泛化边界，以及真实场景实验的完整设置与评价范围。摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对可重光照半透明物体中的非局部次表面散射问题，问题定义清晰，且摘要给出了定量 PSNR 提升；但摘要未展开实验设置、基线细节、运行成本与局限，是否值得优先精读取决于读者对可重光照 Gaussian Splatting、半透明材质与次表面散射方向的直接兴趣。

</details>

<details>
<summary>Abstract</summary>

Creating relightable 3D assets of translucent objects is challenging because changing the illumination at one surface location can affect the appearance elsewhere through subsurface scattering. Existing Gaussian-based scattering models typically predict scattering from local features, making this dependence difficult to capture. We present Non-Local Neural Scattering for Gaussian Splatting (NNS-GS), which learns non-local scattering together with geometry-guided local reflection. The scattering module learns how illumination from light-visible surface regions in light space contributes to the shading point in view space, conditioned on regional diffuse responses and spatial relationships. The reflection module supplies these diffuse responses and uses additional geometric guidance to better capture specular highlights and sharp shadow boundaries. To reduce component mixing and support controllable scattering appearance, anchor-based progressive training establishes the diffuse-scattering base before introducing specular reflection and supervises the components separately. Under calibrated point lighting, NNS-GS improves mean PSNR over existing methods by 2.47 dB and 0.81 dB on the synthetic and real translucent scenes, respectively. Additional synthetic comparisons further show that NNS-GS better matches the reference when adjusting scattering attenuation.

</details>

#### 2026-11-23 - AdvMTO: Multimodal and Temporal Adversarial Object Attacks via 2D Gaussian Splatting for BEV-Based 3D Object Detection

**Authors:** Zhiyang Cui, Hao Tan, Ruonan Li, Shibin Wu, Junjian Zhang, Hong'an Lin, Zhaoquan Gu
**Links:** [abs](https://arxiv.org/abs/2611.30283) - [pdf](https://arxiv.org/pdf/2611.30283)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AdvMTO: Multimodal and Temporal Adversarial Object Attacks via 2D Gaussian Splatting for BEV-Based 3D Object Detection
- 作者：Zhiyang Cui, Hao Tan, Ruonan Li, Shibin Wu, Junjian Zhang, Hong'an Lin, Zhaoquan Gu
- 出版日期：2026-11-23T08:40:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.30283) | [PDF](https://arxiv.org/pdf/2611.30283)

### 一句话总结
论文提出 AdvMTO，一种基于 2D Gaussian Splatting 的对抗物体攻击框架，通过统一构造当前与历史的多模态观测来抑制 BEV 3D 目标检测器对持续对抗物体的识别。

### 研究问题
BEV 3D 目标检测器面临对抗物体攻击威胁，但现有攻击通常只针对单一模态、只协调当前时间戳的相机与 LiDAR 观测，或主要在相机流中建模时间持续性。由于缺乏对当前与历史观测的统一构造，检测器累积的部分证据未被抑制，从而限制了攻击效果。论文关注如何构造并优化持续性的对抗物体，以更有效地抑制 BEV 检测器的检测。

### 核心思路/方法
- 使用 2D Gaussian Splatting（2DGS）框架构造持续性对抗物体；其有向 surfel 将外观、几何与不透明度编码在单一物体状态中。
- 由该物体状态生成相机图像与扫描线 LiDAR 回波。
- 通过检测器原生处理流程构造当前与历史输入；对融合检测器，在每个原生 LiDAR 源扫描中重新生成回波。
- 针对不同检测器优化有界外观扰动，并对时间相机检测器将梯度传播经过历史 BEV 记忆。
- 对融合检测器，沿局部法线进行有界几何细化，以同时扰动两种传感模态。

### 主要贡献
- 提出基于 2DGS 的对抗物体攻击框架 AdvMTO，统一编码物体的外观、几何与不透明度，并生成相机与 LiDAR 观测。
- 强调通过检测器原生处理构造当前与历史输入，以抑制检测器累积证据。
- 针对时间相机检测器引入经过历史 BEV 记忆的梯度传播；针对融合检测器引入沿局部法线的有界几何细化。
- 在 nuScenes 上对三种 BEV 检测器进行实验，显示对交通锥检测的有效抑制；时间消融进一步表明检测器原生历史建模对攻击构造与优化的重要性。

### 局限性
- 摘要仅提及在 nuScenes 上针对交通锥检测进行实验，未说明对其他物体类别、场景类型或检测器的泛化能力。
- 摘要未提供足够信息说明攻击的物理可实现性、真实世界部署条件或防御鲁棒性评估。
- 摘要未提供足够信息说明计算开销、优化收敛性及超参数敏感性。
- 摘要未提供足够信息说明与更多现有攻击方法的定量对比细节。

### 阅读优先级
中。理由：论文聚焦 BEV 3D 检测的对抗攻击，结合 2DGS、多模态与时间持续性建模，问题定位和方法设计具有针对性；但摘要显示的实验范围较集中于 nuScenes 上的交通锥检测，若读者关注物理攻击可行性、广泛泛化或防御评估，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Adversarial object attacks pose a threat to BEV-based 3D object detectors in autonomous driving. Existing attacks typically target a single modality, coordinate camera and LiDAR observations at the current timestamp, or model temporal persistence mainly in camera streams. Without a unified construction of current and historical observations, attacks can leave part of the detector's accumulated evidence unsuppressed, limiting their effectiveness. In this paper, we propose AdvMTO, a 2D Gaussian Splatting (2DGS) framework for suppressing detection of persistent adversarial objects. Its oriented surfels encode appearance, geometry, and opacity in one object state, from which camera images and scanline LiDAR returns are generated. AdvMTO then constructs current and historical inputs through detector-native processing, regenerating LiDAR returns in each native source sweep for fusion detectors. We optimize bounded appearance perturbations for each detector, propagating gradients through historical BEV memory for temporal camera detectors. For fusion detectors, bounded geometry refinement along local normals further perturbs both sensing modalities. Experiments on nuScenes demonstrate effective suppression of traffic-cone detection across three BEV detectors. Temporal ablations further highlight the importance of detector-native history modeling for both attack construction and optimization.

</details>

#### 2026-11-23 - LMnOP: Pruning 3D Gaussian Splatting via Leave-Many-Out Importance

**Authors:** Sunjae Jeong, Jaeseung Kim, Hyoseok Hwang
**Links:** [abs](https://arxiv.org/abs/2611.30102) - [pdf](https://arxiv.org/pdf/2611.30102)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LMnOP: Pruning 3D Gaussian Splatting via Leave-Many-Out Importance
- 作者：Sunjae Jeong, Jaeseung Kim, Hyoseok Hwang
- 出版日期：2026-11-23T05:59:03Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.30102) / [PDF](https://arxiv.org/pdf/2611.30102)

### 一句话总结
针对 3D Gaussian Splatting 在高剪枝率下“单独冗余但组合后关键”的高斯被误删问题，提出以“留多出”重要性（移除其他随机高斯时某高斯的平均损失增量）指导剪枝的 LMnOP 方法。

### 研究问题
3D Gaussian Splatting 能实时渲染逼真视图，但单场景常需数百万高斯，存储与渲染成本高。剪枝通过保留子集降低成本，常用评分是 leave-one-out 重要性（单独移除某高斯时的损失增量）。但在高剪枝率下会同时移除大量高斯，导致那些“单独看冗余、组合起来却关键”的高斯被错误删去。

### 核心思路/方法
- 提出 LMnOP（Leave-Many-Out Pruning），在“其他高斯也被移除”的情形下估计每个高斯的重要性。
- 该 leave-many-out 重要性定义为：在随机移除其他高斯的同时移除某高斯所带来的平均损失增量。
- 对随机移除下每个像素颜色的精确均值与方差进行闭式（closed form）计算，并据此近似重要性，无需对移除模式采样。
- 用该重要性细化每个高斯的保留概率，最终只进行一次剪枝。

### 主要贡献
- 指出并针对高剪枝率下 leave-one-out 评分失效的问题，提出 leave-many-out 重要性度量。
- 给出随机移除下像素颜色均值与方差的闭式计算，并据此无采样地近似重要性。
- 摘要称：在无需微调的情况下，LMnOP 在三个数据集、90% 与 99% 移除率下的 18 项指标中有 16 项取得最佳结果；在全部 13 个场景上，SSIM 与 LPIPS 均优于 GaussianPOP。

### 局限性
摘要未提供足够信息。摘要未给出方法的具体计算复杂度、显存/运行时开销、超参数敏感性、跨数据集泛化细节、失败场景或与其他基线在全部指标上的逐项对比；也未说明“16/18 指标”中未取胜的两项指标具体是什么。

### 阅读优先级
中。理由：该工作面向 3D Gaussian Splatting 的存储与渲染成本问题，提出区别于 leave-one-out 的剪枝重要性度量，且摘要报告了高剪枝率下的多指标优势与无需微调的特点，对关注 3DGS 压缩/剪枝的读者有直接参考价值；但摘要未提供实现开销、复杂度与完整实验细节，需阅读全文进一步判断其实际适用性。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting renders photorealistic views in real time. However, a single scene often needs millions of Gaussians, so these models are costly to store and render. Pruning reduces this cost by keeping a subset of the Gaussians. A common score is the leave-one-out importance, which is the loss increase when a Gaussian alone is removed. At high pruning ratios, many Gaussians are removed together, so Gaussians that are redundant alone but essential together are lost. We present LMnOP (Leave-Many-Out Pruning), which estimates the importance of each Gaussian under the removal of the other Gaussians. This leave-many-out importance is the average loss increase when a Gaussian is removed while the others are also removed at random. We compute the exact mean and variance of each pixel's color under random removal in closed form, and approximate the importance from them without sampling removal patterns. We refine each Gaussian's probability of remaining with its importance and prune once at the end. Without fine-tuning, LMnOP achieves the best results in 16 of 18 metrics on three datasets at 90% and 99% removal. It improves SSIM and LPIPS over GaussianPOP in all 13 scenes.

</details>

#### 2026-11-23 - Ego2Wrist: Bootstrapping Wrist-View Synthesis from Egocentric Video

**Authors:** Ziyao Zeng, Xiatao Sun, Hao Wang, Ziyu Guo, Youheng Yao, Jingcheng Ni, Shenyuan Gao, Fengyu Yang, Renrui Zhang, Bangya Liu, Daniel Rakita
**Links:** [abs](https://arxiv.org/abs/2611.29850) - [pdf](https://arxiv.org/pdf/2611.29850)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** view synthesis, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Ego2Wrist: Bootstrapping Wrist-View Synthesis from Egocentric Video
- 作者：Ziyao Zeng, Xiatao Sun, Hao Wang, Ziyu Guo, Youheng Yao, Jingcheng Ni, Shenyuan Gao, Fengyu Yang, Renrui Zhang, Bangya Liu, Daniel Rakita
- 出版日期：2026-11-23T00:16:39Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.29850) / [PDF](https://arxiv.org/pdf/2611.29850)

### 一句话总结
Ego2Wrist 从人类头戴式自我中心视频和任务描述中合成同步的手腕视角视频，并借助免真值的一致性指标支持递归自提升。

### 研究问题
手腕相机视角与机器人操作直接相关，但大规模采集人类手腕相机视频受制于繁琐装置及其对自然手部动作的干扰；相比之下，头戴式人类自我中心视频更易扩展。论文试图解决如何从易扩展的自我中心视频生成同步手腕视角的问题。

### 核心思路/方法
论文提出 Ego2Wrist，从人类自我中心视频与任务描述合成同步手腕相机视角，并联合生成三个视角。模型在约 940 小时配对的头部与手腕相机录制数据上训练。为在无真值情况下评估生成的手腕视角，论文提出以手为中心的跨视角一致性指标 HCC，衡量生成手腕视角与输入头部视角中对应手部区域的一致性。HCC 还可用于在野外自我中心视频上筛选生成的手腕视角以继续训练，从而支持递归自提升。

### 主要贡献
- 提出 Ego2Wrist，从自我中心视频和任务描述合成同步手腕视角，并联合生成三个视角。
- 构建并使用约 940 小时配对头部—手腕相机录制进行训练。
- 提出免真值评估指标 HCC；摘要称其模型检查点排序与基于真值的 LPIPS 相当，且人类评估者在 77% 的回答中更偏好 HCC 选出的生成结果。
- 在四个数据集上评估，Ego2Wrist 相比微调的 WorldWander 将 LPIPS 降低 28%，并在 76% 的回答中获得人类偏好。
- 利用 HCC 在野外自我中心视频上进行递归自提升，生成质量在三轮中逐步提升。

### 局限性
摘要未提供足够信息说明失败场景、计算成本、对任务描述质量的敏感性、跨域泛化边界以及“三个视角”的具体构成等细节；相关实验细节亦需以论文正文为准。

### 阅读优先级
高。理由：该工作直面机器人操作数据规模化采集的瓶颈，提出从易获取的自我中心视频生成手腕视角，并给出免真值评估与自提升路径；摘要中报告了多数据集对比、人类偏好和三轮递归提升结果，对自我中心视觉、视角合成与机器人策略训练数据生成方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Wrist cameras provide an action-centric view that is directly relevant to robot manipulation. However, collecting human wrist-camera videos at scale is challenging due to cumbersome setups that can interfere with natural hand movements. In contrast, head-mounted human egocentric videos are much easier to scale. We introduce Ego2Wrist, which synthesizes synchronized wrist-camera views from human egocentric videos and task descriptions. Trained on approximately 940 hours of paired head- and wrist-camera recordings, Ego2Wrist jointly generates three views. To evaluate generated wrist views without ground truth, we propose hand-centric cross-view consistency (HCC), which measures consistency between generated wrist views and corresponding hand regions in the input head view. HCC ranks model checkpoints comparably to ground-truth-based LPIPS, and human evaluators prefer HCC-selected generations in 77% of responses. Evaluated on four datasets, Ego2Wrist outperforms fine-tuned WorldWander, reducing LPIPS by 28% and receiving human preference in 76% of responses. More importantly, HCC facilitates recursive self-improvement on in-the-wild egocentric videos by selecting generated wrist views for further training. Generation quality progressively improves over three rounds. These results demonstrate a scalable approach to generating real-world wrist-view human manipulation videos for robot policy training.

</details>

#### 2026-11-22 - SpectralGS: Spectral Gaussian Splatting for Unsupervised Spectral Super-Resolution

**Authors:** Qiaoying Qu, Bin Pan, Chen Jia, Haiyang Xu, Xia Xu, Zhenwei Shi
**Links:** [abs](https://arxiv.org/abs/2611.29388) - [pdf](https://arxiv.org/pdf/2611.29388)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpectralGS: Spectral Gaussian Splatting for Unsupervised Spectral Super-Resolution
- 作者：Qiaoying Qu, Bin Pan, Chen Jia, Haiyang Xu, Xia Xu, Zhenwei Shi
- 出版日期：2026-11-22T11:02:38Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.29388) / [PDF](https://arxiv.org/pdf/2611.29388)

### 一句话总结
SpectralGS 提出一种基于光谱高斯泼溅的无监督光谱超分辨率框架，通过共享光谱高斯表示与基于光谱响应函数的投影渲染，在无配对高光谱数据条件下从 RGB 图像重建光谱信息。

### 研究问题
论文针对无监督光谱超分辨率任务，即在不使用配对高光谱数据的条件下从 RGB 图像恢复光谱信息。摘要指出，RGB 观测中光谱信息有限，使学习有效的空间—光谱表示具有挑战性，因此需要将结构化的光谱建模与传感器成像过程相结合。

### 核心思路/方法
SpectralGS 由两个组件构成：
1. **共享光谱高斯表示（Shared Spectral Gaussian Representation）**：利用共享光谱与局部空间高斯基元构建连续的空间—光谱表示，并利用高光谱图像的低秩光谱结构。
2. **光谱响应投影渲染（Spectral Response Projection Rendering）**：利用光谱响应函数（SRF）对连续表示进行积分投影，混合生成 RGB 图像；通过渲染 RGB 与观测 RGB 之间的一致性提供训练监督。

整体上，该方法将结构化的连续空间—光谱表示与基于成像响应的渲染相结合，实现无监督光谱重建。

### 主要贡献
- 提出 SpectralGS，一种光谱高斯泼溅框架，集成结构化的连续空间—光谱表示与基于成像响应的渲染，从而支持无监督光谱重建。
- 设计共享光谱高斯表示模块，利用高光谱图像的低秩光谱结构构建连续空间—光谱表示。
- 设计基于 SRF 的投影渲染模块，以渲染 RGB 与观测 RGB 的一致性作为监督信号。
- 摘要称大量实验表明该方法优于当前最先进方法（具体实验设置与结果数值摘要未提供足够信息）。

### 局限性
- 摘要未提供足够信息说明方法在不同传感器、不同场景或不同光谱分辨率下的泛化能力。
- 摘要未提供足够信息说明对 SRF 先验准确性或标定误差的敏感程度。
- 摘要未提供足够信息说明计算开销、训练效率及高斯基元数量等实现细节。
- 摘要未提供足够信息说明定量实验结果、对比数据集与评价指标。
- 摘要未提供足够信息说明失败案例或适用边界。

### 阅读优先级
**中**。理由：该论文将高斯泼溅与光谱响应渲染结合用于无监督光谱超分辨率，问题设定与结构化表示思路具有一定新意，且摘要声称优于现有最先进方法；但摘要未给出具体实验数据、数据集与实现细节，是否值得深入阅读需结合全文实验严谨性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Unsupervised spectral super-resolution aims to recover spectral information from RGB images without paired hyperspectral data. However, the limited spectral information in RGB observations makes learning an effective spatial-spectral representation challenging, requiring the incorporation of structured spectral modeling with sensor imaging. In this paper, we propose SpectralGS, a spectral Gaussian splatting framework comprising two components: Shared Spectral Gaussian Representation and Spectral Response Projection Rendering. The representation module constructs a continuous spatial-spectral representation via shared spectral and local spatial Gaussian primitives, exploiting the low-rank spectral structure of hyperspectral images. The rendering module utilizes the spectral response function (SRF) to apply integral projection to the continuous representation, blending it to generate an RGB image. Consistency between the rendered and observed RGB images provides training supervision. Our main contribution is a Gaussian splatting framework that integrates structured continuous spatial-spectral representation with imaging response-based rendering, enabling unsupervised spectral reconstruction. Extensive experiments demonstrate that our method outperforms current state-of-the-art methods.

</details>

#### 2026-11-22 - RadioWorld: Transferring World Models to Radio-Frequency Radiance Fields

**Authors:** Hu Zhou, Jiazhou Zhou, Shuowen Zhang, Ying-Chang Liang, Liang Liu
**Links:** [abs](https://arxiv.org/abs/2611.29282) - [pdf](https://arxiv.org/pdf/2611.29282)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** radiance field, radiance, scene understanding, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RadioWorld: Transferring World Models to Radio-Frequency Radiance Fields
- 作者：Hu Zhou, Jiazhou Zhou, Shuowen Zhang, Ying-Chang Liang, Liang Liu
- 出版日期：2026-11-22T07:10:47Z
- 分类：Neural Scene Representations & Rendering（次要分类：Embodied / Robotics / AR Applications）
- 链接：[摘要](https://arxiv.org/abs/2611.29282)｜[PDF](https://arxiv.org/pdf/2611.29282)

### 一句话总结
RadioWorld 提出一种将世界模型迁移至射频辐射场的通用框架，仅依据物理场景几何与收发机位置即可合成 RF 辐射场，推理阶段无需任何参考 RF 测量。

### 研究问题
摘要指出，现有神经 RF 场方法存在三项根本局限：
1. 主要依赖逐场景优化，无法泛化到未见场景；
2. 在每个目标场景中需要昂贵的参考 RF 测量；
3. 在参考测量附近之外进行外推时性能严重下降。

论文旨在克服上述局限，实现无需推理时参考 RF 测量的、可泛化到未见场景的 RF 辐射场合成。

### 核心思路/方法
- 提出 RadioWorld：一个将世界模型适配为直接从物理场景几何与收发机位置合成 RF 辐射场的通用框架。
- 采用双流 Mixture-of-Transformers（MoT）架构，耦合两个专用模块：
  - Scene-Understanding Transformer：编码 3D 场景几何与收发机位置，提取环境感知的全局电磁传播特征；
  - Field-Generation Transformer：关注上述特征，并结合局部查询条件合成 RF 辐射场。
- 建立 UrbanRF-Bench：大规模射线追踪基准，覆盖 7 个全球城市、657 个城市场景、32,850 个 RF 辐射场。

### 主要贡献
1. 提出 RadioWorld 框架，将世界模型迁移至 RF 辐射场合成，推理时无需参考 RF 测量。
2. 设计双流 MoT 架构，分离场景理解与场生成两个专用 Transformer 模块。
3. 构建 UrbanRF-Bench 大规模射线追踪基准（657 个城市场景、32,850 个 RF 辐射场、7 个全球城市）。
4. 摘要称大量实验表明 RadioWorld 显著优于专用基线，并能在未见城市任意位置准确合成 RF 场；代码、数据集与检查点将在接收后发布。

### 局限性
- 摘要未提供足够信息说明具体实验设置、基线细节、评价指标与定量结果。
- 摘要未提供足够信息说明模型的计算开销、训练数据需求与推理效率。
- 摘要未提供足够信息说明方法在非城市场景或不同频段下的适用性。
- 摘要未提供足够信息说明失败案例或性能边界。

### 阅读优先级
**高**。理由：该论文针对神经 RF 场泛化性、参考测量依赖与外推退化三个明确痛点提出通用框架，并配套大规模基准 UrbanRF-Bench；主题横跨神经场景表示与 6G 通信感知，若研究兴趣涉及 RF 辐射场、世界模型迁移或无线信道建模，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Electromagnetic (EM) wave propagation in the physical world constitutes a Radio-Frequency (RF) radiance field, providing rich information for 6G communication and sensing. However, existing neural RF field methods suffer from three fundamental limitations: (1) they predominantly rely on per-scene optimization and cannot generalize to unseen scenes; (2) they require costly reference RF measurements in each target scene; and (3) they degrade severely when extrapolating beyond the vicinity of reference measurements. To overcome these limitations, we present RadioWorld, a general framework that adapts a world model to synthesize RF radiance fields directly from physical scene geometry and transceiver locations, without requiring any reference RF measurements at inference. Specifically, RadioWorld couples two specialized modules within a dual-stream Mixture-of-Transformers (MoT) architecture: a Scene-Understanding Transformer that encodes 3D scene geometry and transceiver locations to extract environment-aware global EM propagation features, and a Field-Generation Transformer that attends to these features to synthesize the RF radiance field with the local query conditions. We also establish UrbanRF-Bench, a large-scale ray-traced benchmark spanning 657 urban scenes and 32,850 RF radiance fields across seven global cities. Extensive experiments demonstrate that RadioWorld significantly outperforms specialized baselines and accurately synthesizes RF fields at arbitrary locations in unseen cities. Code, datasets, and checkpoints will be released upon acceptance.

</details>

#### 2026-11-22 - Complementary Geometry in Gaussian Splatting

**Authors:** Mingle Jiang, Jikui Zhou, Chenghan Lyu, Rui Xu, Yunke Wang, Chang Xu
**Links:** [abs](https://arxiv.org/abs/2611.29236) - [pdf](https://arxiv.org/pdf/2611.29236)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Complementary Geometry in Gaussian Splatting
- 作者：Mingle Jiang, Jikui Zhou, Chenghan Lyu, Rui Xu, Yunke Wang, Chang Xu
- 出版日期：2026-11-22T05:17:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.29236) / [PDF](https://arxiv.org/pdf/2611.29236)

### 一句话总结
论文观察到冻结的高斯表示在不同视角下的深度预测存在互补误差，提出 REVEAL 框架，在不修改原表示的前提下选择性融合多视角深度信息以提升新视角几何精度，并发布带真值深度的真实场景基准 RIG。

### 研究问题
Gaussian Splatting 在新视角合成中视觉质量较高，但其渲染几何的准确性仍有挑战：渲染深度是沿每条射线的透明度加权平均，可能并不对应真实场景表面。论文关注如何在不修改原始高斯表示的情况下，提升新视角深度（几何）的准确性。

### 核心思路/方法
- 关键观察：同一冻结高斯表示在不同视角下的深度预测呈现互补误差，因此可利用其他视角的信息改进新视角几何。
- 提出 REVEAL 通用框架：选择性细化新视角深度。
  - 先将源视角的深度预测重投影到目标视角，并通过稳健的多视角一致性进行融合。
  - 再引入学习到的选择机制，基于“深度误差的预期降低量”判断候选深度是否比原始预测更准确。
- 额外提出 RIG：用同步 RGB-D 相机采集的真实世界基准，提供真值深度，用于评估静态与动态重建模型。

### 主要贡献
- 揭示并利用冻结高斯表示中不同视角深度预测的互补误差现象。
- 提出 REVEAL 框架，在不修改原始表示的情况下选择性细化新视角深度。
- 提出真实世界基准 RIG，提供真值深度，支持静态与动态重建模型评估。
- 在 3 个基准、6 个 Gaussian Splatting 骨干上实验，摘要称 REVEAL 一致提升深度精度，同时保持可比的渲染质量。

### 局限性
- 摘要未提供足够信息说明 REVEAL 的计算开销、实时性表现。
- 摘要未提供足够信息说明方法对动态场景、稀疏视角或深度噪声的鲁棒性细节。
- 摘要未提供足够信息说明 RIG 基准的规模、场景类型与采集条件细节。
- 摘要未提供足够信息说明选择机制的具体训练方式与失败案例。

### 阅读优先级
高。理由：论文针对 Gaussian Splatting 几何精度这一明确痛点，提出通用且可与多种骨干结合的后处理框架，并附带真实世界深度基准；若关注新视角合成中的几何质量评估与改进，该工作具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has achieved high visual quality in novel view synthesis, but the accuracy of its rendered geometry remains a challenge. In particular, the rendered depth is computed as an opacity-weighted average along each ray, which may not correspond to the actual scene surface. In this paper, we observe that depth predictions from different views of the same frozen Gaussian representation exhibit complementary errors, allowing us to improve novel-view geometry using information from other views without modifying the original representation. Based on this observation, we propose REVEAL, a general framework that selectively refines novel-view depth using complementary geometric information. Specifically, we first reproject depth predictions from source views to the target view and combine them using robust multi-view consensus. We then introduce a learned selection mechanism to determine whether the candidate depth is more accurate than the original prediction, based on the expected reduction in depth error. In addition, we introduce RIG, a real-world benchmark captured with synchronized RGB-D cameras, which provides ground-truth depth for evaluating both static and dynamic reconstruction models. Experiments on 6 Gaussian Splatting backbones across 3 benchmarks show that REVEAL consistently improves depth accuracy while maintaining comparable rendering quality.

</details>

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

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-24 - ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification

**Authors:** Xingjian Ran, Xiaoye Mo, Sihao Liu, Li Luo, Taiqiang Wu, Ji Zhao, Wenqi Shao, Hongyang Li, Jiaqi Wang, Bo Dai
**Links:** [abs](https://arxiv.org/abs/2611.33143) - [pdf](https://arxiv.org/pdf/2611.33143)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, spatial intelligence

<details>
<summary>Abstract</summary>

Embodied spatial intelligence requires agents to gather information through exploration and interaction, then use it to reason and act. Existing benchmarks insufficiently distinguish correct outcomes from completion of these task requirements. We introduce ROAM-Bench to evaluate these abilities under robot motion and collision constraints. Independent checks use simulation state and episode records to assess outcomes and task requirements, with stronger checks of geometry, coverage, or placement. It comprises 250 manually validated tasks across 11 types in five groups and 27 indoor environments, covering object and room search, counting, geometric judgments, direction reasoning, and relocation. Human evaluators achieve 84% strict task success on 100 sampled tasks, with every correct outcome satisfying the required checks. Across seven frontier vision-language models, we identify two complementary failure modes: correct outcomes with unmet task requirements, and incorrect outcomes despite passing stronger checks. Oracle-input diagnostics show that more complete target observations and calibrated feedback improve final spatial judgments.

</details>

#### 2026-11-24 - Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action

**Authors:** Yueh-Cheng Liu, Snehal Jauhri, Matthias Nießner, Angela Dai
**Links:** [abs](https://arxiv.org/abs/2611.33137) - [pdf](https://arxiv.org/pdf/2611.33137)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, inverse rendering, rendering, embodied AI, manipulation, scene understanding

<details>
<summary>Abstract</summary>

We present Physicl Scenes, a high-quality artist-created and curated dataset of 6,499 3D scenes spanning household rooms, public interiors, and outdoor spaces. The dataset combines detailed geometry, physically based materials, and carefully composed environments with object- and part-level semantic annotations, providing rich, joint supervision for visual and embodied learning. We demonstrate its value as training data across inverse rendering, 3D reconstruction, scene understanding, and mobile manipulation. Across these tasks, training state-of-the-art methods with our scenes improves performance over alternative synthetic datasets. In addition, we introduce a mobile manipulation benchmark, evaluating vision-language-action models performing physical pick and place in diverse 3D scenes with realistic layouts, and using our part annotations to also score where each object is grasped. Our dataset will be released publicly to facilitate research in visual and embodied AI.

</details>

#### 2026-11-24 - Motion Conditioned World Modeling for Embodied Visual Tracking

**Authors:** Jiahao Zhang, Xuan Yao, Junyu Gao, Changsheng Xu
**Links:** [abs](https://arxiv.org/abs/2611.32900) - [pdf](https://arxiv.org/pdf/2611.32900)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world modeling

<details>
<summary>Abstract</summary>

World models support embodied decision-making by predicting future environment states. In embodied visual tracking, uncertain target motion and robot-induced viewpoint changes jointly affect visual observations, making future-state prediction challenging. We propose Motion-Conditioned World Modeling, which incorporates predicted target-motion distributions and robot ego-motion into latent state transitions. A Geometry--Progress module jointly models geometric paths and single-step travel distances through shared motion modes and path-conditioned progress distributions. This formulation captures uncertainty in route selection and motion progress while preserving their dependence. Action-induced coordinate transformations express predicted paths in the next robot frame, providing geometrically grounded conditions for future visual-state prediction. Future visual feature reconstruction supervises the motion predictor through the conditioned transition branch, linking explicit motion representations to subsequent observations. The model is jointly optimized with motion likelihood, feature reconstruction, and expert-action supervision, enabling the tracking policy to combine visual context with predictive motion cues.Experiments on three embodied tracking benchmarks demonstrate improved tracking performance and cross-environment generalization with a lightweight $0.5$B backbone.

</details>

#### 2026-11-24 - Supply Geometry, Learn Execution: Screw Attention for Zero-Shot Policy Transfer in Robot Manipulation

**Authors:** Aly Magassouba
**Links:** [abs](https://arxiv.org/abs/2611.32797) - [pdf](https://arxiv.org/pdf/2611.32797)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

We present the Screw Attention Policy, a geometry-centric manipulation framework that supplies task geometry explicitly and learns only execution. The policy operates on object poses, relative SE(3) transforms, and joint screw axes provided by perception and robot models. The policy requires only 30K learned parameters. Trained entirely in simulation on a single robot arm, the policy generalises to new scene layouts, transfers zero-shot across robot embodiments, and deploys directly on a real robot, without adaptation or fine-tuning. It achieves 96% success on LIBERO, 85.8% under layout changes, 80.2% across five unseen robot arms, and 21 of 24 trials on a real robot. These results suggest that much of what manipulation policies learn at scale is geometric structure that can instead be supplied.

</details>

#### 2026-11-24 - MemAnchorWorld: A Sparse World Model with Horizon-Conditioned Memory Retrieval for Autonomous Driving

**Authors:** Xinyang Jia, Yuqi Zhang, Jiakai Wang, Yahu Yang, Guandong Pan, Chao Tong, Xianglong Liu
**Links:** [abs](https://arxiv.org/abs/2611.32745) - [pdf](https://arxiv.org/pdf/2611.32745)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world model

<details>
<summary>Abstract</summary>

Sparse world models for 4D semantic occupancy forecasting represent scenes with a small set of evolving queries to efficiently predict future geometry and semantics for autonomous driving. However, existing sparse world models face a bottleneck in using historical temporal evidence for long-horizon forecasting. They rely on scene states to carry historical information implicitly, allowing errors to propagate and accumulate across successive forecasting steps and causing geometric and semantic deviations. To address this limitation, we present MemAnchorWorld, a sparse occupancy world model that explicitly retrieves relevant historical geometric and semantic evidence for 4D semantic occupancy forecasting. Inspired by the von Restorff effect, we introduce a forecast-time-conditioned hierarchical dual-path memory-anchor retrieval mechanism. Guided by the effective age and semantic compatibility of historical information, it combines query-level candidate selection with point-level memory-anchor retrieval to provide historical evidence for sparse points at different forecast times. To better use memory anchors and existing features, a point-level residual adapter jointly gated by the task and forecast time separately controls residual corrections to semantics, occupancy confidence, and spatial positions. On Occ3D-nuScenes, MemAnchorWorld achieves an average mIoU of 13.55% and an average IoU of 22.84% across the 1-3 s forecasting horizons, attaining state-of-the-art performance on both metrics.Project page: https://memanchorworld.github.io/

</details>

#### 2026-11-24 - Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation

**Authors:** Itai Mizlish, Boaz Ben-Moshe
**Links:** [abs](https://arxiv.org/abs/2611.32718) - [pdf](https://arxiv.org/pdf/2611.32718)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, robot navigation, mapping

<details>
<summary>Abstract</summary>

A small ground robot can carry one camera and a few watts of compute, but the depth foundation models that could turn that camera into a range sensor are vision transformers sized for GPUs. We bring one to a Raspberry Pi 5 with the Hailo-8L, an accelerator that runs every layer in integer arithmetic, attention included. Quantised for it, Depth Anything V2 loses large parts of the scene, and we measure why: at 449 tokens, 91% of softmax weights fall below one int8 step while carrying 17-33% of the attention mass. Our answer is to distil, not quantise. An attention-free ResNet-34 U-Net student of Depth Anything V2-Large (24.5M parameters) runs at 27.1 FPS on the chip, its int8 output matches its float twin (Pearson 0.99993), and on held-out scenes of its simulated yard it is the most accurate depth network on the chip (AbsRel 0.269 against 0.354-0.530). On 1,000 stereo-verified points of a real outdoor drive it is not resolvably different from the vendor's Depth Anything V2-Small build, while running faster (27.1 vs 21.6 FPS). Ranging obstacles by where they meet the floor needs only the camera height, so mapping, hybrid-A* planning and SLAM run on the Pi's own CPU. In real-time hardware-in-the-loop tests in a Gaussian-splat reconstruction of a real yard, the stack reaches the goal without contact in 7.9$\pm$1.1 of 10 scenes, against 9.2$\pm$0.4 with exact obstacles, and in 7.7$\pm$0.7 on its own pose with simulated wheel odometry (ten seeds each; 8.2$\pm$0.4 with the real Pi and Hailo-8L in the loop, five seeds). The source code, pre-trained models and data are available at https://github.com/itaim18/DANIEL.

</details>

#### 2026-11-24 - GeoVLDrive: Geometry-Grounded Vision-Language Reasoning for Autonomous Driving

**Authors:** JiaHui Huang, Songyan Zhang, Hanbing Li, Hanchao Leng, Kuiyuan Yang, Guang Chen, Hangjun Ye, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2611.32510) - [pdf](https://arxiv.org/pdf/2611.32510)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) planners inherit semantic knowledge from pretrained vision-language models, but their reasoning is rarely grounded in 3D scene structure and its evolution over time. We introduce GeoVLDrive, a geometry-grounded VLA framework for 3D spatiotemporal reasoning and planning. Multi-layer features from a 3D foundation model augment the vision-language backbone through gated cross-attention. A structured latent chain of thought (CoT) organizes future scene geometry, key-agent motion, and meta-actions into ordered, separately supervised latent states. An action expert generates trajectory proposals from these states and multi-layer scene features, and ranks them using scene-grounded, interacting score tokens. We also introduce NAVSIM 3DQA to train and evaluate metric 3D spatial and motion understanding. GeoVLDrive achieves 91.8 PDMS on NAVSIM v1 and 90.9 EPDMS on NAVSIM v2. On NAVSIM 3DQA, the geometry-grounded backbone scores 89.2% overall, 4.6 percentage points above the fine-tuned Qwen3-VL-2B baseline. On LingoQA, the backbone achieves 68.6% Lingo-Judge accuracy.

</details>

#### 2026-11-24 - OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution

**Authors:** Zhilu Zhang, Xiaoyu Liu, Wenxi Liu, Shengfeng He
**Links:** [abs](https://arxiv.org/abs/2611.32473) - [pdf](https://arxiv.org/pdf/2611.32473)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, autonomous driving, world modeling

<details>
<summary>Abstract</summary>

Action-conditioned world models play a vital role in robotics and autonomous driving, yet existing video diffusion models struggle to maintain dynamic object persistence. When the camera turns away and returns, out-of-view moving entities fail to evolve plausibly in latent space, often mutating or vanishing entirely due to bounded perspective views. To resolve this issue, we propose OmniPersist, a unified framework that couples perspective video generation with panoramic evolution within a single-stage diffusion model, without relying on auxiliary models or initial panoramic inputs. To maintain efficiency, we model the panoramic stream at a lower frame rate, bridging both views across space and time via Geometric Anchoring (GeoAnch) for spatial correspondence and Temporal Compensation (TemComp) for temporal aggregation. OmniPersist is agnostic to camera-control architectures, supporting both latent-level and attention-level conditioning. Extensive experiments on a newly constructed dynamic benchmark across image-to-video and video continuation tasks demonstrate consistent gains in visual quality, camera controllability, revisit consistency, and dynamic persistence.

</details>

#### 2026-11-24 - Can You Find the Edit When Nothing Looks Wrong? A Paired Benchmark for Text-Driven Image Manipulation Localization Beyond Semantic Abnormality

**Authors:** Peiyu Zhuang, Jianquan Yang, Zhuoying Cai, Yi Jiang, Yingquan Chen, Xinle Wang, Zeqin Yu, Dongdong Lin, Ruitao Xie, Kaige Li, Xiaochun Cao
**Links:** [abs](https://arxiv.org/abs/2611.32242) - [pdf](https://arxiv.org/pdf/2611.32242)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>Abstract</summary>

Instruction-driven image editing can alter a photograph while keeping the result coherent with the scene. Existing benchmarks lack matched plausible and anomalous edits of the same target, making it difficult to measure how localization performance changes with semantic plausibility. We construct a paired benchmark by generating semantically plausible and anomalous replacements of the same target in each source photograph. Both edits use the same editor, language, and generation settings. We estimate a separate mask for each output and retain pairs with sufficient mask overlap, enabling direct comparison of localization performance under the two semantic conditions. The release contains 47,747 bilingual triplets from 6,500 photographs, spanning four editors, three source domains, and six intended violation types. Across nine public localizers, editor-averaged IoU is lower on plausible edits in 26 of 27 model-dataset comparisons. This gap persists under pixel-change controls and region-size analyses. These findings reveal a semantic-plausibility shortcut: localization often weakens when an edited result looks ordinary. The benchmark provides a controlled setting for measuring this gap and developing localizers that remain effective on plausible edits.

</details>

#### 2026-11-24 - NativeDrive: Native Multimodal Foundations for Autonomous Driving

**Authors:** Zehua Fan, Qi Jiang, Wei Li, Kai Tang, Yue Jiang, Yujian Li, Bailin Li, Feng Gao, Yan Wang, Kun Zhan
**Links:** [abs](https://arxiv.org/abs/2611.32216) - [pdf](https://arxiv.org/pdf/2611.32216)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

Autonomous driving requires semantic understanding and fine-grained scene perception for precise action prediction. Vision-language-action models (VLAs) inherit semantic priors, but low-dimensional action labels provide limited structural supervision. Some studies extend VLAs with visual generation tasks or adopt video-based world-action models (WAMs), but both approaches introduce appearance-reconstruction overhead, which is less relevant to planning. Native multimodal models offer an alternative to unify understanding and generation within one backbone. On this basis, we propose NativeDrive, a native encoder-free multimodal driving framework adapting the unified backbone for policy learning and introduce a dense supervision task tailored to driving. The Native Action Interface reuses the understanding expert's token-prediction interface for the discrete policy and adapts the generation expert for continuous policy. Driving Semantic Editing reuses the generation expert's editing capability for dense scene-structure supervision during training, while inference runs only the selected planning policy. NativeDrive achieves competitive planning performance among unified understanding-and-generation models on NAVSIM v1 and v2, with ablations validating its components' effectiveness. Code will be released.

</details>

#### 2026-11-24 - Instant LiDAR: Feed-Forward Gaussian Reconstruction for LiDAR Simulation

**Authors:** Xin Kang, Jiahui Huang, Jiawei Ren, Sipeng Zhang, Yu Chen, Weihua Zhang, Junjie Lai
**Links:** [abs](https://arxiv.org/abs/2611.32042) - [pdf](https://arxiv.org/pdf/2611.32042)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, simulation

<details>
<summary>Abstract</summary>

LiDAR reconstruction supports closed-loop autonomous driving simulation, but hours of per-scene optimization make large asset libraries costly to build and maintain. We present Instant LiDAR, a feed-forward pipeline that reconstructs multiple LiDAR scans as reusable Gaussian assets in minutes without per-scene optimization. LiDAR measurements provide strong geometric priors, but directly initializing Gaussians from them yields poor reconstruction due to nonuniform sampling and a limited field of view. Sparse returns leave surface gaps, while combining scans expands coverage but introduces redundant primitives. To address these challenges, Instant LiDAR combines measurement-anchored Gaussian prediction, sampling-aware Gaussian scales, and multi-frame consolidation. The predictor refines attributes anchored to recorded returns, while the scales adapt spatial support to LiDAR sampling. Multi-frame consolidation merges overlapping predictions into a compact asset spanning the driving log. Compared with NuRec, Instant LiDAR reconstructs scenes approximately 46 times faster on Physical AI (PAI) and 70 times faster on Waymo. It also achieves comparable downstream 3D detection accuracy on Waymo.

</details>

#### 2026-11-24 - VLG-Drive: Unifying Vision-Language and Geometric Priors for Autonomous Driving

**Authors:** Junge Zhang, Jie Zhu, Yanqi Jia, Xiangyu Xu, Zixun Huang, Wenbin He, Xin Li, Jiachen Li, Liu Ren
**Links:** [abs](https://arxiv.org/abs/2611.31952) - [pdf](https://arxiv.org/pdf/2611.31952)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

A driving planner needs both scene semantics, which vision-language models (VLMs) provide, and spatial structure, which geometric foundation models recover from visual history. We present VLG-Drive, which keeps both models frozen and trains only a fusion interface and a planner from trajectory labels. At each camera-grid cell, the interface fuses the paired VLM and geometry features into one joint token through a geometry-anchored residual, and a command-conditioned planner reads these tokens to predict the ego trajectory. VLG-Drive achieves 31.78 EPDMS on NavHard under perturbed initial states, the highest among the compared methods, and 88.27 PDMS on NavTest from cameras alone. Pointwise fusion outperforms independent VLM and geometry streams on both benchmarks. In closed-loop driving on 420 HUGSIM scenarios, VLG-Drive outperforms all compared planners. These results indicate that a lightweight planner trained on fused features of frozen vision-language and geometric foundation models is an effective alternative to adapting either model for planning.

</details>

#### 2026-11-24 - Gaze World Model

**Authors:** Jiawen Zhang, Houze Yang, Xu Cao, Yifan Shen, Zhongyi Zhou, Steve Wong, Ismini Lourentzou, Inki Kim, James M. Rehg
**Links:** [abs](https://arxiv.org/abs/2611.31836) - [pdf](https://arxiv.org/pdf/2611.31836)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, world model

<details>
<summary>Abstract</summary>

Where a person looks indicates their focus of attention, and how their gaze shifts between targets reveals how that attention responds to a changing scene. Existing gaze target estimation methods largely operate frame by frame and do not model these shifts. Gaze shifts are often driven by dynamic changes in the scene, which is the kind of information world models are designed to encode. This relationship is subtle, however, since an event far across the frame may produce only a slight movement of the person's head or eyes. We therefore introduce the Gaze World Model (GWM), which co-trains latent scene prediction with person-conditioned gaze supervision on a frozen V-JEPA 2.1 encoder; in our ablations, the latent prediction objective improves both shift detection and gaze localization. Given a video clip and the person's head box, GWM estimates gaze locations and detects gaze shifts in the observed clip, and forecasts future gaze and shifts from predicted scene features. To train and evaluate these tasks, we augment VideoAttentionTarget and ChildPlay with event-level gaze-shift annotations. GWM achieves state-of-the-art shift detection on these benchmarks, about 10 points higher in four-class AP than the strongest baseline, while remaining comparable to the strongest image-based models in gaze target estimation, and outperforms the compared baselines on future gaze localization and shift forecasting.

</details>

#### 2026-11-24 - Beyond the Benchmark: Localizing Released Autonomous Driving Models to Real Vehicles

**Authors:** Morui Zhu, Deyuan Qu, Qi Chen, Qing Yang
**Links:** [abs](https://arxiv.org/abs/2611.31814) - [pdf](https://arxiv.org/pdf/2611.31814)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, localization

<details>
<summary>Abstract</summary>

Released autonomous-driving models achieve strong benchmark performance, yet deploying them on a new real vehicle remains challenging. We study this deployment gap and find that released models can remain coupled to assumptions from their source sensing, data, and execution processes even after conventional adaptation. We introduce Released-to-Real (R2R), a deployment-localization methodology that identifies such source-system coupling and corrects only the affected components while preserving the released model. For data and behavior adaptation, we find that the mismatch between trajectory-level optimization and receding-horizon execution enters through the ego state rather than the observation, and introduce Human-Anchored Reinforcement Learning (HA-RL), which corrects it on recorded target driving without the costly rollouts of generative closed-loop reinforcement learning (RL). For physical sensor adaptation, R2R localizes and corrects source-dependent spatial and temporal representations with frozen perception weights, requiring neither target annotations nor retraining. HA-RL improves the closed-loop success rate of a released diffusion-based planner from 82.2% to 95.2%, while sensor adaptation across multiple released detectors and three real sensor rigs improves the vehicle mean average precision (mAP) of a released multi-camera detector from 0.041 to 0.420 on a five-camera target rig. These results provide a practical path for preparing released models before deployment on new real vehicles. Our project page is publicly available at https://released-to-real.github.io.

</details>

#### 2026-11-23 - FabricBench: A Standardized Policy Benchmark for Bimanual Fabric Manipulation with a Contact-Driven Deformable Simulator

**Authors:** Wenkang Hu, Haoran Wang, Liu Liu, Wenchao Huang, Yiji Chen, Mengao Zhao, Xincheng Tang, Zhengjie Shu, Lai Jiang, Wei Li, Zhendong Wang, Zhizhong Su, Huamin Wang, Ruigang Yang
**Links:** [abs](https://arxiv.org/abs/2611.31577) - [pdf](https://arxiv.org/pdf/2611.31577)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Fabric manipulation challenges robot policies with changing geometry, self-occlusion, and contact, yet standardized evaluation remains focused on rigid objects. We introduce FabricBench, a benchmark for bimanual fabric manipulation with six tasks spanning garments, silk, and bags, 10,000 simulation-ready assets, and controlled tests of configuration and appearance generalization. Built on an open-source solver in Newton, our simulator enables stable bimanual grasping, holding, and release through contact forces, without artificial attachment. Redesigned cloth-rigid contact and bidirectional force coupling support interactions among robot arms, fabric, and free rigid objects, allowing a bag to support its contents and transmit their weight to the grippers. In a controlled grasp-hold-release evaluation, our solver succeeds in all 45 trials, compared with none for the tested baseline configurations. Evaluating six representative policies, including vision-language-action models and world action models, reveals substantial remaining challenges: the best policy achieves 77% average success, while no policy exceeds 36% on long-horizon T-shirt folding. Under the most deformed initial T-shirt configurations, success falls to 6-14% across policies, with larger drops than under the evaluated appearance shifts. Zero-shot deployment of $π_{0.5}$ on a real robot largely preserves task difficulty ordering across six tasks (Spearman $ρ=0.94$). These results establish FabricBench as a reproducible testbed for measuring fabric-manipulation capabilities and exposing limitations in configuration generalization. The project website is available at https://fabricbench.github.io/.

</details>

#### 2026-11-23 - Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation

**Authors:** Jinzhong Gu, Jiakai Chen, Xinyi Cao, Yan Shen, Hangke Sui, Shutian Zheng, Xiang Xiao, Haoran Lu, Fan Xu, Lu Shi, Daochen Shi, Ruihua Zhang, Wei Zhan, Masayoshi Tomizuka, Ruihai Wu
**Links:** [abs](https://arxiv.org/abs/2611.31098) - [pdf](https://arxiv.org/pdf/2611.31098)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation
- 作者：Jinzhong Gu, Jiakai Chen, Xinyi Cao, Yan Shen, Hangke Sui, Shutian Zheng, Xiang Xiao, Haoran Lu, Fan Xu, Lu Shi, Daochen Shi, Ruihua Zhang, Wei Zhan, Masayoshi Tomizuka, Ruihai Wu
- 出版日期：2026-11-23T17:39:59Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.31098) / [PDF](https://arxiv.org/pdf/2611.31098)

### 一句话总结
提出 Real2Worlds2Real，一个自改进的智能体框架，把可扩展的仿真世界构建与策略开发结合起来，在有限视觉观测和任务描述下构建真实感数字孪生并扩展为多样化数字变体，进而支撑机器人操作策略学习与真实迁移。

### 研究问题
论文关注机器人操作学习中的数据瓶颈：真实世界交互数据采集成本高。Real2Sim2Real 通过在仿真中学习、并以真实观测为锚定，提供了有希望的路径，但要将该范式扩展到多样任务和物理交互仍然困难。摘要指出，核心问题包括：可扩展的仿真世界构建、跨任务与物理交互的泛化，以及在仿真中开发并 refine 策略后实现真实世界策略迁移。

### 核心思路/方法
- 框架定位：Real2Worlds2Real 是一个“自改进的智能体框架”（self-improving agentic framework），整合可扩展仿真世界构建与策略开发。
- 输入条件：给定有限的视觉观测和任务描述。
- 世界构建：其“工具编排 harness”（tool-orchestration harness）构建忠实的数字孪生（digital twins），并将其扩展为多样化、可物理执行的“数字表亲/数字变体”（digital cousins）。
- 自适应构建：智能体自适应选择工具并回访构建决策，利用视觉反馈和执行反馈来 refine 几何与物理行为。
- 策略开发：在这些世界基础上，智能体编排策略开发，协调数据生成、策略学习和 refine，依据任务需求和仿真 rollout 反馈进行。
- 技能复用：在两个阶段中，智能体把经过验证的流程蒸馏为可复用技能，用于指导后续任务。

### 主要贡献
- 提出 Real2Worlds2Real 自改进智能体框架，将 Real2Sim2Real 的可扩展世界构建与策略开发统一起来。
- 设计工具编排 harness，在有限视觉观测和任务描述下构建数字孪生，并扩展为多样化、可物理执行的数字变体，同时利用视觉与执行反馈 refine 几何和物理行为。
- 让智能体编排数据生成、策略学习与 refine，并依据仿真 rollout 反馈迭代策略开发。
- 引入跨阶段的可复用技能蒸馏与复用机制，以提升后续任务的世界构建效率和长程任务成功率。
- 摘要报告实验显示：世界保真度提升、真实世界策略迁移成功；世界多样性和交互数据量增加带来性能增益；技能复用进一步提升世界构建效率和长程任务成功率。

### 局限性
- 摘要未提供足够信息说明具体实验任务、机器人平台、基线方法、评价指标和定量结果。
- 摘要未提供足够信息说明“有限视觉观测”的具体规模和条件，以及数字孪生/数字变体的保真度如何量化。
- 摘要未提供足够信息说明真实世界策略迁移的成功率、失败模式和安全边界。
- 摘要未提供足够信息说明技能复用的适用范围、跨任务泛化边界以及方法对工具集或仿真器的依赖程度。
- 摘要未提供足够信息说明计算成本、数据生成规模和训练时长。

### 阅读优先级
高。理由：该论文直接针对机器人操作学习中真实数据成本高这一关键瓶颈，提出自改进智能体框架来扩展 Real2Sim2Real 的世界构建与策略开发；摘要明确报告了世界保真度提升、真实世界策略迁移成功、世界多样性与数据量带来增益以及技能复用改善长程任务成功率。若关注机器人操作、仿真到真实迁移、智能体化工具编排和可扩展策略学习，该论文值得优先阅读。但需注意：具体实验设置与定量证据需查阅全文，摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Scaling robot manipulation learning remains challenging due to the high cost of collecting real-world interaction data. Real-to-Sim-to-Real (Real2Sim2Real) offers a promising route by enabling policy learning in simulation grounded in real-world observations, yet scaling this paradigm across diverse tasks and physical interactions remains difficult. We introduce Real2Worlds2Real, a self-improving agentic framework that integrates scalable simulation-world construction with policy development. Given limited visual observations and task descriptions, its tool-orchestration harness constructs faithful digital twins and expands them into diverse, physically executable digital cousins. The agent adaptively selects tools and revisits construction decisions, using visual and execution feedback to refine geometry and physical behavior. Building on these worlds, the agent orchestrates policy development by coordinating data generation, policy learning, and refinement based on task requirements and simulation rollout feedback. Across both stages, the agent distills validated procedures into reusable skills that guide subsequent tasks. Experiments demonstrate improved world fidelity and successful real-world policy transfer, with performance gains from increasing world diversity and interaction-data volume. Skill reuse further improves world-building efficiency and long-horizon task success.

</details>

#### 2026-11-23 - DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation

**Authors:** Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias
**Links:** [abs](https://arxiv.org/abs/2611.30907) - [pdf](https://arxiv.org/pdf/2611.30907)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation
- 作者：Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias
- 出版日期：2026-11-23T16:05:37Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.30907 ；PDF https://arxiv.org/pdf/2611.30907

### 一句话总结
提出一种基于点云观测、从重定向人类操作演示中学习连续潜在动作的 3D 跨具身世界模型，并将该统一潜在动作空间直接用于模型预测控制，实现零样本机器人操作与跨具身迁移。

### 研究问题
论文关注两个问题：一是世界模型通常依赖带动作标签的交互数据，这类数据获取成本高、难以规模化；二是模型往往绑定于训练时的特定具身形态，难以迁移到未见过的机器人形态。摘要还指出，目标是支持零样本操作以及未见夹爪几何形态下的迁移。

### 核心思路/方法
- 从重定向人类操作演示的**点云观测**中直接学习连续动作表示，构建 3D 潜在动作世界模型。
- 使用**对比学习目标**，鼓励不同具身之间运动表示的一致性。
- 形成的统一潜在动作空间直接作为**模型预测控制**的搜索空间。
- 采样的潜在动作作为条件，驱动**基于粒子的未来预测**。
- 从预测的几何运动中恢复可执行的机器人命令，且**不需要具身特定的动作解码器**。

### 主要贡献
- 提出 3D 跨具身潜在动作世界模型 DexLatentWorld，避免依赖昂贵的动作标签交互数据。
- 通过对比目标构建统一潜在动作空间，并直接用于模型预测控制。
- 无需具身特定动作解码器即可从预测几何运动恢复机器人命令，支持向未见具身与未见夹爪几何形态的零样本迁移。
- 摘要报告：任务无关适配后，在 reaching、grasping、placing 上分别达到 90%、92%、60% 成功率，对比 DexWM 报告的 72%、58%、28%。
- 摘要报告：在真实世界中用未见过的灵巧手完成零样本操作，在五项涉及推动、抓取和举升日常物体的任务上，50 次试验取得 86% 成功率。

### 局限性
- 摘要未提供足够信息说明方法的失败案例、适用边界或对点云质量与演示数据分布的敏感性。
- 摘要未提供足够信息说明“任务无关适配”的具体定义、数据需求与计算成本。
- 摘要未提供足够信息说明真实世界 50 次试验的具体任务划分、统计方差与基线对比细节。
- 摘要未提供足够信息说明跨具身迁移的具身数量、形态差异范围及夹爪几何差异程度。

### 阅读优先级
**高**。理由：论文聚焦跨具身世界模型、潜在动作表示与零样本机器人操作，摘要给出了明确的量化结果与真实世界验证，且方法上试图绕开动作标签数据和具身特定解码器，对该方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions. However, they typically rely on action-labelled interaction data that is costly to acquire and difficult to scale. These models are also often tied to the specific embodiment they were trained on, limiting transferability to previously unseen robot morphologies. We introduce a 3D latent-action world model that learns continuous action representations directly from point-cloud observations of retargeted human manipulation demonstrations. A contrastive objective is used to encourage consistent representations of motion across embodiments. The resulting unified latent action space serves directly as the search space for model-predictive control, where sampled latent actions condition particle-based future predictions. Executable robot commands are then recovered from the predicted geometric motion without requiring an embodiment-specific action decoder. Through extensive evaluations, we demonstrate that the learned latent actions exhibit controllable and compositional motion, transfer to unseen robot embodiments, and support zero-shot manipulation with unseen gripper geometries. Following task-agnostic adaptation, our model achieves 90%, 92%, and 60% success on reaching, grasping, and placing, respectively, compared with DexWM's reported 72%, 58%, and 28%. Finally, we demonstrate zero-shot real-world manipulation with an unseen dexterous hand, achieving an 86% success rate across 50 trials on five diverse tasks involving pushing, grasping, and lifting everyday objects. These results highlight the potential of geometry-grounded latent actions as a unified, transferable interface for world-model-based robotic manipulation. Project materials, including demonstration videos and source code, are available at https://vinaymohan0409.github.io/DexLatentWorld/.

</details>

#### 2026-11-23 - Can Multimodal Fusion MakeSense for Embodied Vision in Degraded Sensing?

**Authors:** Cheng-Ru Chou, Shih-Yu Lai, Pei-Lin Chiang, Shou-Po Tsai, Jing-Zhe Huang, Fukuharu Tanaka, Hirozumi Yamaguchi, Bing-Yu Chen, Yu-Lun Liu, Hsun-Ping Hsieh
**Links:** [abs](https://arxiv.org/abs/2611.30836) - [pdf](https://arxiv.org/pdf/2611.30836)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied vision, robotics, autonomous driving, localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Can Multimodal Fusion MakeSense for Embodied Vision in Degraded Sensing?
- 作者：Cheng-Ru Chou, Shih-Yu Lai, Pei-Lin Chiang, Shou-Po Tsai, Jing-Zhe Huang, Fukuharu Tanaka, Hirozumi Yamaguchi, Bing-Yu Chen, Yu-Lun Liu, Hsun-Ping Hsieh
- 出版日期：2026-11-23T15:20:31Z
- 分类：主分类 Embodied / Robotics / AR Applications；次要分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.30836 ；PDF https://arxiv.org/pdf/2611.30836

### 一句话总结
论文提出多模态融合框架 MakeSense，通过在私有流中保留各传感器证据、并以共享瓶颈 token 进行信息整合，缓解退化感知条件下“增加传感器反而增大误差”的负融合问题。

### 研究问题
具身视觉系统依赖互补传感器在条件变化下进行感知与行动；即使模型能够接受任意传感器子集，也可能出现负融合：加入一个传感器会增加预测误差。论文关注在退化观测下，如何减少这种有害的传感器增补效应。

### 核心思路/方法
- 提出 MakeSense 多模态融合框架：在私有流中保留传感器特定证据，并通过共享瓶颈 token 组合信息。
- 训练时配对同一退化观测的完整视图与子集视图，并对“传感器更多但误差更高”的情况施加惩罚。
- 在几何条件允许时，距离读出仅使用测距测量，其余预测使用所有可用输入。
- 通过轻量适配器与按数据集训练，将同一设计用于多个任务场景。

### 主要贡献
- 明确提出并针对“负融合”问题设计融合框架 MakeSense。
- 在五个数据集上进行配对测试，揭示有益与有害的传感器增补。
- 摘要称 MakeSense 在 MM-Fi 上减少负融合；并在 MMAUD 的无人机定位、V2X-Real 的协同 3D 检测、RELI11D 的少样本姿态迁移、Humanoid-Everyday 的命令预测上带来改进。
- 在 Humanoid-Everyday 中，基于冻结核心输出的世界模型在较长测试时域上比线性基线更准确地预测未来融合状态。
- 摘要称该框架支持人类活动、空中系统、机器人与自动驾驶等具身感知场景。

### 局限性
- 摘要未提供足够信息说明五个数据集的具体规模、评测协议、基线细节与统计显著性。
- 摘要未提供足够信息说明负融合的定量定义、惩罚项的具体形式与超参数。
- 摘要未提供足够信息说明各任务改进的具体数值幅度。
- 摘要未提供足够信息说明计算开销、实时性以及在真实部署条件下的表现。
- 摘要未提供足够信息说明方法在传感器严重缺失或极端退化条件下的失效边界。

### 阅读优先级
中。理由：论文主题与具身视觉、多传感器融合和退化感知直接相关，且摘要声称覆盖五类数据集与多种具身场景，具有潜在参考价值；但当前仅有摘要与元数据，缺少实验数值、协议和实现细节，需阅读全文后才能判断其证据强度与可复现性。

</details>

<details>
<summary>Abstract</summary>

Embodied vision systems rely on complementary sensors to perceive and act as conditions change. Even models that accept arbitrary sensor subsets can exhibit negative fusion: adding a sensor increases prediction error. We propose MakeSense, a multimodal fusion framework that preserves sensor-specific evidence in private streams and combines information through shared bottleneck tokens. Training pairs full and subset views of the same degraded observations, penalizing higher error with more sensors. Where geometry permits, the distance readout uses range measurements alone, while the rest of the prediction draws on all available inputs. Paired tests across five datasets reveal helpful and harmful sensor additions. MakeSense reduces negative fusion on MM-Fi. With lightweight adapters and per-dataset training, the same design improves UAV localization on MMAUD, cooperative 3D detection on V2X-Real, few-shot pose transfer to RELI11D, and command prediction on Humanoid-Everyday, where a world model trained on the frozen core's outputs forecasts future fused states more accurately than a linear baseline at longer tested horizons. MakeSense supports embodied sensing across human activity, aerial systems, robotics, and autonomous driving.

</details>

#### 2026-11-23 - Tri-DNO: Trilateral Diffusion Noise Optimization for 3D Human Object Interaction

**Authors:** Paul Hinzer, Niklas Gard, Anna Hilsmann, Peter Eisert
**Links:** [abs](https://arxiv.org/abs/2611.30607) - [pdf](https://arxiv.org/pdf/2611.30607)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** AR, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tri-DNO: Trilateral Diffusion Noise Optimization for 3D Human Object Interaction
- 作者：Paul Hinzer, Niklas Gard, Anna Hilsmann, Peter Eisert
- 出版日期：2026-11-23T12:44:02Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.30607) / [PDF](https://arxiv.org/pdf/2611.30607)

### 一句话总结
Tri-DNO 通过迭代优化预训练多模态 HOI 扩散模型的初始噪声，在不重新训练生成模型的前提下改善手物接触质量并减少穿插。

### 研究问题
论文关注 3D 人-物交互（HOI）生成中的手部抓握真实性问题。摘要指出，即使轻微的几何不一致（如接触不足或物体穿插）也会显著损害真实感；尽管扩散生成模型在 HOI 合成上已有前景，但确保物理上合理的手-物交互仍然具有挑战性。

### 核心思路/方法
Tri-DNO 是一种扩散噪声优化策略，用于从预训练的多模态 HOI 扩散模型中采样。该方法不修改或重新训练生成模型，而是迭代优化扩散生成器的初始噪声，以生成稳固的手-物接触，同时减轻穿插并保持手部位置合理。摘要将其描述为“Trilateral Diffusion Noise Optimization”，但未展开说明“三边”具体指哪三个优化目标或约束。

### 主要贡献
- 提出 Tri-DNO，一种针对预训练多模态 HOI 扩散模型的扩散噪声优化策略，用于改善手-物接触。
- 无需修改或重新训练生成模型，通过优化初始噪声实现更稳固的接触、减轻穿插并保持手部位置合理。
- 在 GRAB 数据集上的实验表明，相比基线在抓握质量上有提升，且摘要称无需额外模型训练，与现有方法相比不增加计算成本。
- 摘要进一步说明该方法可应用于实际媒体制作场景。

### 局限性
- 摘要未提供足够信息说明“三边”优化的具体构成、噪声优化的迭代细节与目标函数。
- 摘要未提供足够信息说明实验的定量指标、对比方法细节、用户研究或媒体制作场景的具体验证方式。
- 摘要未提供足够信息说明方法在 GRAB 之外数据集或更复杂交互场景中的泛化能力。
- 摘要未提供足够信息说明失败案例、计算开销的具体测量方式或对预训练模型质量的依赖程度。

### 阅读优先级
中。理由：该工作针对 HOI 生成中手-物接触物理合理性的明确痛点，提出无需重训练、不增加计算成本的噪声优化思路，问题定义清晰且应用指向 AR/VR 与媒体制作；但摘要未披露方法细节与充分实验信息，是否值得深入阅读取决于读者对扩散采样优化或手-物交互生成的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Generating realistic 3D human object interactions (HOI) is essential for applications, such as augmented or virtual reality (AR/VR) or character animation of interactive entertainment. A particular challenge lies in the faithful generation of hand grasps in human object interaction scenes, where even minor geometric inconsistencies, such as insufficient contact or interpenetration, can significantly compromise realism. While diffusion-based generative models have shown promising results in HOI synthesis, ensuring physically plausible hand-object interactions remains challenging. We present Tri-DNO, a diffusion noise optimization strategy to sample from a pretrained multimodal HOI diffusion model, improving hand-object contact. Rather than modifying or retraining the generative model, our approach iteratively optimizes the initial noise of the diffusion generator, thereby generating firm hand object contact, while mitigating penetration and keeping the hand position realistic. Experiments on the GRAB dataset demonstrate improvements over the baseline in grasp quality without additional model training or increased computational cost compared to existing methods. We further demonstrate the applicability of our approach to practical media production scenarios.

</details>

#### 2026-11-23 - One Latent World for Heterogeneous LiDARs: A Scan Pattern Agnostic 4D World Model via Direct Ray Decoding

**Authors:** Minwoo Jung, Dongjae Lee, DongGuw Lee, Yeong Sang Park, Maurice Fallon, Ayoung Kim
**Links:** [abs](https://arxiv.org/abs/2611.30007) - [pdf](https://arxiv.org/pdf/2611.30007)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Latent World for Heterogeneous LiDARs: A Scan Pattern Agnostic 4D World Model via Direct Ray Decoding
- 作者：Minwoo Jung, Dongjae Lee, DongGuw Lee, Yeong Sang Park, Maurice Fallon, Ayoung Kim
- 出版日期：2026-11-23T04:10:19Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.30007) / [PDF](https://arxiv.org/pdf/2611.30007)

### 一句话总结
论文提出一种与扫描模式无关的 4D LiDAR 世界模型，通过将场景与传感器观测解耦，并用直接射线解码从同一潜表示生成异构 LiDAR 的扫描。

### 研究问题
现有 LiDAR 世界模型通常按训练传感器的扫描模式合成扫描，或从中间 3D 表面/场渲染。前者限制了对其他扫描模式 LiDAR 的迁移，后者可能产生错误深度和虚假回波。论文关注的问题是：能否构建一个不依赖特定扫描模式的 4D LiDAR 世界模型，使同一空间潜表示可被同一安装位置下的异构 LiDAR 直接观测。

### 核心思路/方法
论文提出“扫描模式无关”的 4D LiDAR 世界模型，将场景与传感器观测解耦，使一个空间潜表示可由异构 LiDAR 共享而不需重新生成。其解码器直接从潜表示预测每条射线的命中概率和深度，结合全局场景上下文与在初步深度处检索的局部特征。由于不依赖中间表面或场，论文称这可减少错误深度和虚假回波；每条射线独立解码，因此共享同一射线的 LiDAR 会得到相同回波，从而观测到一致场景。此外，模型使用 diffusion transformer 在潜空间中生成场景，并基于由给定自运动和目标运动 warp 的观测潜表示预测 4D 序列。

### 主要贡献
- 提出扫描模式无关的 4D LiDAR 世界模型，将场景与传感器观测解耦，使同一潜表示可服务异构 LiDAR。
- 设计直接射线解码器，从潜表示直接预测每条射线的命中概率与深度，避免中间表面或场渲染带来的错误深度和虚假回波。
- 使用 diffusion transformer 在潜空间中生成场景并预测 4D 序列。
- 在 KITTI-360 和 nuScenes 上，论文报告生成场景更真实，预测帧间配准误差相对最佳对比世界模型降低约 70%；解码器深度误差比其他世界模型所用渲染低 19% 至 28%；生成扫描有利于若干下游任务。

### 局限性
摘要未提供足够信息。摘要未说明计算开销、实时性、对极端稀疏或特殊扫描模式的泛化边界、失败案例、下游任务的具体范围与指标细节，也未给出消融实验的完整设置。

### 阅读优先级
高。理由：该工作直接针对 LiDAR 世界模型中“扫描模式绑定”和“中间几何渲染误差”两个关键问题，提出潜空间解耦与直接射线解码，并报告了配准误差和深度误差的显著改进；对异构 LiDAR 世界建模、4D 场景预测及相关机器人/自动驾驶应用具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

LiDAR world models generate and predict metric 3D observations in the form of LiDAR scans. They typically synthesize scans following the scan pattern of their training sensor or render them from an intermediate 3D surface or field. However, following one scan pattern limits transfer to LiDARs with other patterns, and rendering from intermediate geometry can cause incorrect depths and false returns. In this paper, we propose a scan pattern agnostic 4D LiDAR world model that decouples the scene from sensor observation, so one spatial latent can be observed by heterogeneous LiDARs at the same mounting position without regeneration. Our decoder predicts the hit probability and depth of each ray directly from the latent, combining global scene context with local features retrieved at a preliminary depth. Without an intermediate surface or field, it reduces incorrect depths and false returns, and as each ray is decoded independently from one latent, LiDARs that share a ray receive the same return and observe one consistent scene. Finally, a diffusion transformer generates scenes in this latent and predicts 4D sequences from observed latents warped by the given ego and object motion. On KITTI-360 and nuScenes, our model generates realistic scenes and reduces the registration error between predicted frames by about 70% relative to the best compared world model. Its decoder yields 19 to 28% lower depth error than the rendering used by other world models, and generated scans benefit several downstream tasks. Our code will be open-sourced. More details are available at https://minwoo0611.github.io/OneLatentWorld.

</details>

#### 2026-11-23 - SAGE-Drive: Benefit-Aware Adaptive Reasoning for Autonomous Driving Planning

**Authors:** Donglei Rong, Wenbin Yao, Congcong Bai, Xi Gao, Qiaoqiao Ren, Sheng Jin, Cheng Xu
**Links:** [abs](https://arxiv.org/abs/2611.29947) - [pdf](https://arxiv.org/pdf/2611.29947)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAGE-Drive: Benefit-Aware Adaptive Reasoning for Autonomous Driving Planning
- 作者：Donglei Rong, Wenbin Yao, Congcong Bai, Xi Gao, Qiaoqiao Ren, Sheng Jin, Cheng Xu
- 出版日期：2026-11-23T03:10:09Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.29947 ；PDF https://arxiv.org/pdf/2611.29947

### 一句话总结
论文提出 SAGE-Drive，用“是否带来规划误差下降”作为监督信号，预测显式推理在不同驾驶场景中的收益，并在给定推理预算下只对预测收益最高的场景启用显式推理。

### 研究问题
显式推理能帮助自动驾驶车辆理解复杂交通交互并支持轨迹规划，但会带来额外计算开销；同时，显式推理对规划准确性的收益随场景变化，因此关键问题是：判断何时启用显式推理更有利。摘要指出，需要解决“确定显式推理何时能提升规划准确性”这一挑战。

### 核心思路/方法
- 构造配对规划结果：对同一场景分别在有、无显式推理条件下规划，以规划误差的下降量衡量“推理收益”，并将其作为监督标签。
- 学习预测推理收益：利用“无推理初始轨迹的几何特征”和“多模态场景信息”预测上述收益。
- 预算约束下的自适应调用：在预定义推理预算下，仅在预测收益最高的场景中调用显式推理。
- 实验规模与设置：在 1,497 个配对驾驶场景上开展实验；测试集上比较了 20% 与 35% 推理预算下的平均位移误差（ADE）。

### 主要贡献
- 提出 SAGE-Drive，一个面向自动驾驶规划的“收益感知”自适应推理框架，核心是在推理预算约束下选择性启用显式推理。
- 将“显式推理带来的规划误差下降”形式化为可监督的推理收益，并验证其可作为推理选择的有效准则。
- 实验显示：在 1,497 个配对场景中，显式推理在 53.5% 的情况下提升规划准确性，在 46.5% 的情况下反而降低准确性，平均收益接近零，说明“是否推理”需要场景自适应判断。
- 在测试集上，20% 推理预算下 SAGE-Drive 的 ADE 为 1.5191 m，优于随机选择的 1.5252 m；35% 预算下 ADE 为 1.5148 m，接近对所有场景都推理的 1.5141 m。

### 局限性
- 摘要仅给出 ADE 指标及部分预算条件下的结果，未提供其他规划指标、安全性指标或计算开销的详细量化信息：摘要未提供足够信息。
- 摘要未说明数据集来源、场景分布、基线方法完整列表及统计显著性：摘要未提供足够信息。
- 摘要未说明“多模态场景信息”的具体构成、模型结构细节及训练/测试划分方式：摘要未提供足够信息。
- 摘要未讨论预测收益误差对推理选择的影响，也未给出失败案例分析：摘要未提供足够信息。
- 论文标注为 2026 年，且分类含 Embodied / Robotics / AR Applications，但摘要未提供真实系统部署或实车验证信息：摘要未提供足够信息。

### 阅读优先级
中。理由：论文聚焦“显式推理是否值得启用”这一具有实际计算成本意义的问题，且摘要给出了明确的配对实验规模与预算条件下的 ADE 对比，适合关注自动驾驶规划效率与自适应推理的研究者阅读；但摘要未提供方法细节、完整基线及安全性/计算开销的充分证据，是否高优先级取决于读者对“推理预算选择”这一具体问题的兴趣。

</details>

<details>
<summary>Abstract</summary>

Explicit reasoning enables autonomous vehicles (AVs) to interpret complex traffic interactions and support trajectory planning, but introduces additional computational demands. Determining when explicit reasoning can improve planning accuracy remains a key challenge, as its benefits vary across driving scenarios. To address this challenge, this study proposes Scene-Adaptive Gating of Explicit Reasoning for Driving (SAGE-Drive), a benefit-aware adaptive reasoning framework for autonomous driving planning. First, paired planning outcomes with and without explicit reasoning are analyzed to measure the reasoning benefit, i.e., the reduction in planning error achieved by explicit reasoning, which serves as the supervision label. SAGE-Drive then learns to predict these benefits using geometric features of the initial trajectory planned without reasoning and multimodal scene information, and invokes explicit reasoning only for the scenarios with the highest predicted benefits under a predefined reasoning budget. Experiments on 1,497 paired driving scenarios reveal that explicit reasoning improves planning accuracy in 53.5% of cases while degrading it in 46.5%, yielding a near-zero average benefit. On the test set, with a 20% reasoning budget, SAGE-Drive achieves an average displacement error (ADE) of 1.5191 m, compared with 1.5252 m for random selection. At a 35% budget, it achieves an ADE of 1.5148 m, close to the 1.5141 m obtained when reasoning is applied to every scenario. These findings establish the predicted reasoning benefit as an effective criterion for reasoning selection, allowing explicit reasoning to be invoked where it improves planning accuracy at a fraction of its computational cost.

</details>

#### 2026-11-22 - ClothCast: Generative Cloth World Modeling under Partial Observability

**Authors:** Yushen Hu, Yilong Song, Zhen Zhou, Apurv Kushwaha, Harshvardhan Chandirasekar, Zhu-Tian Chen
**Links:** [abs](https://arxiv.org/abs/2611.29369) - [pdf](https://arxiv.org/pdf/2611.29369)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ClothCast: Generative Cloth World Modeling under Partial Observability
- 作者：Yushen Hu, Yilong Song, Zhen Zhou, Apurv Kushwaha, Harshvardhan Chandirasekar, Zhu-Tian Chen
- 出版日期：2026-11-22T10:21:24Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.29369) / [PDF](https://arxiv.org/pdf/2611.29369)

### 一句话总结
ClothCast 是一个面向部分可观测布料场景的世界模型：它利用夹爪轨迹提供的运动先验，对可见表面和遮挡层进行预测，并用扩散式点流模型来学习残余形变。

### 研究问题
机器人操作布料时，世界模型需要预测场景在给定动作下如何演化；由于布料形变复杂且存在自遮挡，预测非常困难。论文要解决的是：在不提供布料网格或材质参数、且只有单次 RGB-D 观测的条件下，如何预测布料在计划夹爪轨迹下的时序演化，并处理被遮挡的布料层。

### 核心思路/方法
- **输入**：一次 RGB-D 观测、相机位姿、机器人自身模型、计划的夹爪轨迹；不使用布料网格或材质参数。
- **分层点集提升**：将观测提升为分层点集，其中包含推测的遮挡层。
- **混合刚性先验**：根据夹爪位姿构造混合刚性先验，并让点集随该先验移动；被夹爪持有的布料随夹爪运动，其余形变需要预测。
- **残余运动预测**：用视频扩散点流模型预测残余运动。
- **渲染与补全**：在 4 至 11 秒、10 Hz 的完整 episode 中，将移动后的点渲染为深度，再由几何条件补全模型合成 RGB。
- **释放后处理**：布料释放后，用人工设计的 settling 步骤替代学习到的运动。
- **基准**：发布 ClothCastBench，包含 10,000 个模拟双臂布料操作 episode，每帧都带有真值布料网格（含遮挡层）。

### 主要贡献
- 提出 ClothCast 世界模型，在部分可观测条件下结合夹爪轨迹运动先验与学习到的残余点流来预测布料演化，且不依赖布料网格或材质参数。
- 引入分层点集表达以显式处理推测的遮挡层。
- 发布 ClothCastBench：10,000 个模拟双臂布料操作 episode，逐帧提供含遮挡层的真值布料网格。
- 在 492 个留出 episode 上，序列平均可见表面 Chamfer 距离为 14.0 mm，较最强几何基线 Flex-π（35.6 mm）低 2.5 倍；布料区域 PSNR 较最强布料 PSNR 基线 Cosmos-Predict2.5 高 3.7 dB。
- 在 50 个 episode 的消融子集上，仅使用刚性先验（作用于 ClothCast 学习到的初始几何，并采用相同后处理）已经优于两个具备几何能力的基线，而学习到的残余进一步将误差降低约三分之一。

### 局限性
- 摘要未提供足够信息说明真实机器人实验、真实布料泛化能力及 sim-to-real 表现。
- 摘要未提供足够信息说明推理速度、计算开销与实时性。
- 摘要未提供足够信息说明对相机位姿噪声、夹爪轨迹误差或初始观测质量的敏感性。
- 摘要未提供足够信息说明“推测的遮挡层”的准确性评估与失败模式。
- 摘要未提供足够信息说明释放后的 settling 步骤在复杂布料或动态场景中的适用范围。
- 摘要未提供足够信息说明 ClothCastBench 的布料类型、材质多样性与任务分布细节。

### 阅读优先级
**高**。理由：该工作直接面向机器人布料操作中的部分可观测世界建模难题，方法结合运动先验与生成式点流，且提供了明确的量化对比和大规模带真值网格的基准；对具身操作、布料感知与生成式世界模型方向均有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

World models support robotic manipulation by predicting how the scene evolves under a planned action. For garments this prediction is notoriously difficult: deformations are complex, and self-occlusion leaves much of the cloth unobserved. Planned gripper trajectories provide a useful motion prior because cloth held by a gripper moves with it, while the remaining deformation must be predicted. We introduce ClothCast, a world model that applies this prior to the cloth's points and learns the residual motion. ClothCast takes one RGB-D observation, the camera pose, the robot's own model and the planned gripper trajectories, with no cloth mesh or material parameters. It lifts the observation to a layered point set that includes hypothesized occluded layers, carries the points with a blended rigid prior derived from the gripper poses, and predicts the residual motion with a video-diffusion point-flow model. Over entire 4- to 11-second episodes at 10 Hz, the moved points are rendered into depth, from which a geometry-conditioned completion model synthesizes RGB; after release, a hand-designed settling step replaces the learned motion. We further release ClothCastBench, 10,000 simulated dual-arm cloth-manipulation episodes with the ground-truth cloth mesh, including occluded layers, at every frame. On 492 held-out episodes, ClothCast achieves 2.5x lower sequence-averaged visible-surface Chamfer distance than Flex-π, the strongest baseline in geometry (14.0 mm vs. 35.6 mm), and 3.7 dB higher cloth-region PSNR than Cosmos-Predict2.5, the strongest baseline in cloth PSNR. On a 50-episode ablation subset, the rigid prior alone, applied to ClothCast's learned initial geometry with the same post-processing, already outperforms both geometry-capable baselines, and the learned residual lowers its error by about a third.

</details>

#### 2026-11-22 - SpatialDuet: Bayesian task routing between a metric expert and a geometry expert for spatial intelligence

**Authors:** Duy Tran Thanh
**Links:** [abs](https://arxiv.org/abs/2611.29168) - [pdf](https://arxiv.org/pdf/2611.29168)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialDuet: Bayesian task routing between a metric expert and a geometry expert for spatial intelligence
- 作者：Duy Tran Thanh
- 出版日期：2026-11-22T02:57:30Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.29168) / [PDF](https://arxiv.org/pdf/2611.29168)

### 一句话总结
论文提出 SpatialDuet，将分别擅长不同空间任务的“度量专家”和“几何专家”两个冻结的视觉语言模型（VLM）组合起来，由贝叶斯任务路由器按问题类型为两个专家的输出加权，在不训练任何模型权重的情况下提升小模型的空间推理表现。

### 研究问题
具身助手与可穿戴设备需要三维空间推理，但硬件受限使它们只能使用小型 VLM。摘要指出，小型空间 VLM 因训练方式不同而获得不同能力：在大规模空间问题集上训练的模型擅长估计物体与房间尺寸；带三维几何编码器的模型更擅长相对方向和绝对距离。论文要解决的问题是：与其像已发表方法那样训练单一模型处理所有空间任务，不如构建一个系统，让每个冻结模型只负责其最擅长的任务。

### 核心思路/方法
SpatialDuet 由一个度量专家、一个几何专家和一个贝叶斯任务路由器组成。
- 度量专家：数据驱动的空间 VLM，配有三种免训练模块，即训练对齐采样、度量感知的最小贝叶斯风险解码和按类型进行的度量校准。
- 几何专家：带三维几何编码器的 VLM。
- 贝叶斯任务路由器：对每种问题类型，从带标签的开发问题上估计两个专家各自更可能表现更好的概率；并以该概率为权重融合答案。对于数值答案在对数空间中融合，对于多选答案在选项分布上融合。
整个过程不训练任何模型权重。

### 主要贡献
- 提出 SpatialDuet，将度量专家与几何专家在贝叶斯任务路由器下配对，按问题类型路由，而非训练单一模型覆盖所有空间任务。
- 为度量专家引入三个免训练模块：训练对齐采样、度量感知最小贝叶斯风险解码、按类型度量校准。
- 摘要称在覆盖视频与单图像的四项空间基准上验证了 SpatialDuet；在 VSI-Bench 上比已发表最佳小型 VLM 高 3.17%，在 CV-Bench 上排除一个在 CV-Bench 风格数据上训练的模型后高 1.44%，且未训练任何模型权重。

### 局限性
- 摘要未提供足够信息说明四个空间基准的具体名称与构成、数据集规模、评价指标细节。
- 摘要未提供足够信息说明两个专家模型的具体参数规模、来源与算力开销。
- 摘要未提供足够信息说明路由器的概率估计在开发集之外是否稳健，以及专家均失败时的表现。
- 摘要未提供足够信息说明误差分析、消融实验细节与失败案例。
- 摘要未提供足够信息说明该方法在真实具身或可穿戴设备上的部署与延迟表现。

### 阅读优先级
中。理由：论文关注受限硬件下小 VLM 的组合式空间推理，采用免训练路由融合两个专家，问题设定清晰且报告了基准上的定量收益；但仅凭摘要无法判断专家模型细节、路由稳健性和实际部署开销，适合作为组合式空间推理与免训练模型复用的候选阅读，暂不宜列为高优先级精读。

</details>

<details>
<summary>Abstract</summary>

Embodied assistants and wearable devices need 3D spatial reasoning, and their limited hardware restricts them to small vision-language models (VLMs). Small spatial VLMs acquire different abilities from their training: a model trained on large spatial question sets estimates object and room sizes well, whereas a model with a 3D geometry encoder is better at relative directions and absolute distances. Instead of training a single model for all spatial tasks, as published methods do, we build one system that uses each frozen model for the tasks it handles best. We propose SpatialDuet, which pairs a metric expert with a geometry expert under a Bayesian task router. The metric expert is a data-driven spatial VLM run with three training-free modules: training-aligned sampling, metric-aware minimum Bayes risk decoding and per-type metric calibration. The geometry expert is a VLM with a 3D geometry encoder. For each question type, the router estimates from labelled development questions how likely each expert is to be better, and pools their answers with that probability as weight, in log space for numeric answers and over the option distributions for multiple-choice answers. Extensive experiments on four spatial benchmarks covering video and single images validate SpatialDuet; it outperforms the best published small VLMs by 3.17% on VSI-Bench and, excluding a model trained on CV-Bench-style data, by 1.44% on CV-Bench, without training any model weight.

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
