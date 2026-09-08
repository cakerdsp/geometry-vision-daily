# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：35
- 分类分布：
  - Neural Scene Representations & Rendering: 13
  - Embodied / Robotics / AR Applications: 11
  - 3D Reconstruction & Multi-view Geometry: 7
  - Geometry Foundation Models: 2
  - Dynamic / 4D Reconstruction: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**1. 3D 基础模型与生成模型开始“跨界互融”，内部表征被重新挖掘利用。**
多条工作不再将 3D 重建/生成视为终端任务，而是将 3D 基础模型（如 VGGT）的内部表征视作可复用的“资产”。Z3D（2609.04174）直接尝试从 3DFM 内部表征中解码隐藏表面，并通过潜在扩散合成新视角深度；WorldSculpt（2609.05416）则展示了如何将单物体生成先验迁移到数百物体的大规模场景；SPAR3S（2609.03931）与 OctWorld（2609.03919）也都在探索如何在无 3D 真值监督条件下，利用可微渲染与稀疏表征构建“从多视图图像到可生成 3D 场景”的新范式。这反映了从“炼丹式重建”向“表征即知识、知识可生成”方向演进的苗头。

**2. “长程一致性”与“在线可扩展性”成为重建与生成的双重瓶颈与主战场。**
长视频在线重建在 Scal3R（2609.04201）中被明确诊断为“局部深度稳定、全局位姿崩溃”，进而以多参考相对位姿查询解决长距离漂移；视频生成侧，OctWorld（2609.03919）与 CamTrol++（2609.03639）分别从“持久化 3D 记忆”与“相机步长分解”两个不同角度应对长距离/大视角变化下的空间一致性崩溃。两者殊途同归，均指向同一个核心问题：跨越时间与空间的全局几何记忆如何紧凑、稳定地维护与更新。

**3. 高斯泼溅从“重建利器”走向“可编辑、可加速、可结构化的工程系统”。**
3DGS 相关论文密集出现且分工明确：底层优化稳定性（TruncGradGS，分段截断梯度解决梯度消失）、栅格化工程加速（TileGS，瓦片内深度分箱重排）、上层编辑能力（球谐重参数化实现调色板级颜色/亮度编辑）、大规模结构感知表面重建（STARS-GS，结构感知场景划分与自适应正则化）。这表明 3DGS 正从“能否重建”全面转向“能否用好”：追求加速、稳定、可编辑、可扩展至大规模场景。

**4. 机器人操控领域出现“规模祛魅”与“特征可解释性回归”的并行思潮。**
MINERVA（2609.03715）以 0.54M 参数在 LIBERO 上达到 95.1% 成功率，直接挑战当前 VLA 模型的“大即是好”预设，为模型容量与任务复杂度匹配提出实证基线。GIFT（2609.04193）则从另一角度指出视觉预训练特征与动作控制之间存在“动作充分性差距”，主张通过几何、姿态、目标区域等显式结构监督来引导中间特征。二者都在质疑盲目堆规模的路线，一个在做减法（最小容量），一个在加结构（几何/语义约束）。此外，3D 形态扰动（2609.03657）还展示了用 3DGS 形态参数空间正则化来提升下游机器人策略性能，进一步说明 3D 表征研究正在与操控学习深度绑定。

**5. 语义场景理解与具身/AR 应用走向“混合管线”，强调先验知识与实际几何的融合。**
ReRoom（2609.03596）将虚拟房间代理与真实空间对齐，实现原位家居布局设计并将室内设计准则技能化；语义建图的混合管线（2609.03891）将外部标定相机、单应投影、对象检测/追踪与本体驱动的动态更新结合；焊缝识别（2609.03970）将语义分割、摄影测量与机器人后处理流程打通，作为高精度测量前的预定位阶段。三维视觉正加速进入行业细分场景，以“视觉粗定位 + 先验知识校正 + 机器人/AR执行”的模式落地。


#### 技术路线观察

- **几何基础模型（Geometry Foundation Models）**：目前主要回答“如何用”（Z3D 挖掘 VGGT 内部表征），而非“如何训”。核心矛盾在于现有 3DFM 是否已蕴含足以支持零样本新视角推理的通用 3D 知识，以及如何以轻量解码（潜在扩散）将其释放。
- **3D/4D 重建（传统几何路线）**：Scal3R 与 BA 扩展（2609.04026）都偏向“在经典框架内做结构创新”——前者将冻结骨干+轻量 token 注入引入 SLAM/在线重建，后者以类相机实体建模高阶几何关系并保持稀疏结构。保守但扎实，在可解释性和工程稳定性上占优。
- **神经场景表示与渲染（NeRF/3DGS 衍生）**：最大特点是分化明显且内部自迭代极快。可归纳为四条支线：(a) 编辑能力（P-CORE、PointGT、调色板重参数化）；(b) 工程加速（TileGS）；(c) 优化稳定性（TruncGradGS）；(d) 大规模扩展与结构感知（STARS-GS）。其中 P-CORE 与 PointGT 两篇同作者/同团队论文均聚焦基于点表示的几何+纹理编辑，显示出“可编辑性正在成为表示学习的核心评价维度”之迹象。
- **视频生成与 3D 记忆**：OctWorld 与 CamTrol++ 都试图以“扩散模型 + 几何约束”回答长程一致性；区别在于前者维护显式的、可扩展的八叉树 TSDF 记忆，后者则利用小步自回归与无配准变形在推理层面寻求稳定。两者均不修改或极少修改扩散主干，强调推理时/外围模块增益。
- **机器人/AR 应用（Embodied/Robotics）**：出现了明显的“反思”与“混合”特征。反思在于 MINERVA 对 VLA 参数规模与基准任务复杂度匹配的怀疑与量化；混合在于系统级方案（如本体语义建图、焊缝识别管线、GIFT在线操作蒸馏框架、WorldSculpt 的场景网格输出）越来越多地从头到尾贯通感知、几何、语义与执行环节。

总体而言，几何基础模型与扩散生成之间正在形成围绕“表征复用”合流的主干；纯几何与神经渲染两条路径并行演进，前者稳、后者快；机器人侧则呈现明显的“效率优先”转向。


#### 值得优先阅读的论文

**1. OctWorld（2609.03919）—— 理解“3D 记忆”在长程生成中的角色**
将显式稀疏八叉树 + TSDF 融合引入扩散模型作为持久 3D 记忆，是当前“生成式世界模型必须维护几何一致性”趋势下非常具象、可借鉴的系统性方案。阅读优先级最高，因其跨越了视频生成、3D重建与记忆机制三个交叉领域。

**2. Scal3R（2609.04201）—— 在线重建长程漂移问题的一份“诊断书 + 药方”**
其对失败模式的归因（局部深度稳定、全局位姿崩溃）奠定了设计合理性的基础，而“冻结骨干 + ~1% 可学习 token 查询多参考位姿 + 在线位姿图优化”的方案极简且训练成本低（单 GPU 8 小时），在工程与科研之间取得良好平衡。

**3. STARS-GS（2609.03447）—— 大规模 3DGS 表面重建的“组织与编排”**
从场景划分、邻域组织到自适应正则化三个层面系统解决大规模航拍重建问题，是 3DGS 从“室内物体级”迈向“城市级地理空间”的代表性工作，对工程落地有直接参考价值。

**4. MINERVA（2609.03715）—— 对 VLA 膨胀潮流的冷静审视**
0.54M 参数在 LIBERO 上逼近 π0.5（7700 倍参数）的水平，并给出容量崩溃阈值（~0.25M 以下）与饱和点（~1M），极可能倒逼后续 VLA/操控策略论文重新审视基线设置与基准设计的质量，建议作为回应性

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-07T13:44:33-04:00
**Total number of papers:** 35
**Number of papers added in the latest update:** 2
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

#### 2026-09-03 - Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations

**Authors:** Denis M. Akola, David F. Fouhey
**Links:** [abs](https://arxiv.org/abs/2609.04174) - [pdf](https://arxiv.org/pdf/2609.04174)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations
- 作者：Denis M. Akola, David F. Fouhey
- 出版日期：2026-09-03（arXiv 发布时间）
- 分类：Geometry Foundation Models（几何基础模型）
- 链接：https://arxiv.org/abs/2609.04174

### 一句话总结
本文提出 Z3D 方法，利用 3D 基础模型（如 VGGT）的内部场景表征，通过潜在扩散在未见视角上合成真实的新颖深度图，实现零样本深度预测。

### 研究问题
3D 基础模型内部学习到的场景表征，是否包含可用于推断新视角下三维结构（尤其是隐藏表面）的通用知识？如何有效地从这些表征中解码出新视角的深度信息？

### 核心思路/方法
1. **假设验证**：作者假设 3D 基础模型在解决三维重建任务时，必须学习包含大量通用三维场景知识的内部表征，因此这些表征可能蕴含可解码的隐藏表面信息。
2. **先验验证**：首先证明可以从 3DFM 内部表征中解码出隐藏表面（即模型表征并非仅用于已知视角）。
3. **方法 Z3D**：在 3DFM 表征上执行潜在扩散（latent diffusion），以此估计未见视角下的点图（pointmaps），进而得到新颖视图的深度图。
4. **零样本能力**：该方法无需针对特定数据集进行训练，可直接在多个数据集上为新视角生成合理的深度预测。

### 主要贡献
- 首次研究从 3D 基础模型内部表征解码隐藏表面的可行性，并给出正面证据。
- 提出 Z3D 方法，将潜在扩散应用于 3DFM 表征，实现未见视角的深度估计。
- 实验表明 Z3D 能在多个数据集上为新视角预测真实合理的深度图，展示跨数据集的零样本泛化能力。

### 局限性
摘要未提供足够信息。具体局限（如对遮挡严重场景、复杂拓扑、计算成本、定量精度上限等）均未在摘要中明确说明，无法评估。

### 阅读优先级
**中**  
理由：该工作针对 3D 基础模型内部表征的可重用性进行探索，思想新颖且具有一定启发性，适合关注三维视觉与几何基础模型交叉方向的读者。但目前仅摘要显示初步可行性，未给出定量评测细节或应用场景深度，若追求具体方法实现或严格对比结论，需进一步阅读全文。对于非相关方向读者优先级可降低。

</details>

<details>
<summary>Abstract</summary>

3D Foundation Models (3DFMs) such as VGGT have recently pushed the boundaries of 3D vision by predicting rich unified representations with feed-foward transformers. The scene representations learned by these models enable strong performance on multiple 3D vision tasks. In this paper, we investigate using their internal representations to infer 3D in the scene from new views. Our hypothesis is that in order to solve the task of 3D reconstruction, these models need to learn a representation that includes a large amount of general knowledge about 3D scenes. After showing that it is possible to decode hidden surfaces from internal 3DFM representations, we propose a method, Z3D, that estimates pointmaps in unseen views by doing latent diffusion on 3DFM representation. We show that Z3D can predict realistic depth maps for new views across multiple datasets.

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

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-04 - CrossDepth: Geometry-Constrained Attention for Generalizable Multi-View Surround Depth Estimation

**Authors:** Samer Abualhanud, Max Mehltretter
**Links:** [abs](https://arxiv.org/abs/2609.05397) - [pdf](https://arxiv.org/pdf/2609.05397)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CrossDepth: Geometry-Constrained Attention for Generalizable Multi-View Surround Depth Estimation
- 作者：Samer Abualhanud, Max Mehltretter
- 出版日期：2026-09-04
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.05397

### 一句话总结
CrossDepth 提出一种基于几何约束注意力的多视角环视深度估计方法，通过相机感知射线嵌入与跨图像注意力提升深度精度与跨图像一致性，并在 DDAD 和 nuScenes 上优于现有自监督方法。

### 研究问题
在多视角环视相机系统中，相邻图像重叠极小，导致大多数像素的深度需要依赖单目外观线索推断；然而这些线索在不同图像间可能表现不一致（受相机内参差异和每张图像感受野有限影响），从而造成跨图像深度估计不一致。

### 核心思路/方法
- 针对相机内参差异：在特征上引入逐像素的相机感知射线嵌入，让网络适应相机相关的外观线索变化。
- 针对感受野有限：通过几何约束的跨图像注意力机制，将每个像素的上下文扩展到自身图像之外，仅关注由标定系统导出的几何合理区域。
- 训练方式：全自监督，基于光度一致性（photometric consistency）进行训练。

### 主要贡献
- 提出相机感知射线嵌入，以缓解不同相机内参导致的单目线索解释差异。
- 设计几何约束的跨图像注意力，在标定约束下扩展像素上下文，提升跨图像深度一致性。
- 在 DDAD 和 nuScenes 上的域内与跨域评估中，整体深度精度和跨图像一致性均优于现有自监督方法。
- 代码已公开。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法面向自动驾驶环视深度估计，提出可泛化的跨图像一致性改进思路，属于应用导向的增量创新；但摘要未给出具体数值比较或消融细节，适用性与改进幅度需进一步阅读原文验证。若您关注多视角几何或自监督深度估计方向，可考虑优先阅读。

</details>

<details>
<summary>Abstract</summary>

Reliable 3D understanding of the surrounding environment is a core requirement for autonomous driving. Multi-view surround camera rigs provide broad scene coverage, but the spatially adjacent images typically overlap only minimally. Consequently, the depth of most pixels must be inferred from monocular appearance cues. These cues can appear differently across images and may therefore be interpreted differently by the depth estimation model. We target two main sources of cross-image inconsistency: differences in camera intrinsics and the limited receptive field of each image. We address the former by conditioning the features on per-pixel camera-aware ray embeddings, enabling the network to account for camera-dependent variations in monocular cues. We address the latter by extending each pixel's context beyond its own image through cross-image attention constrained to geometrically plausible regions, derived from the calibrated rig setup. The model is trained in a fully self-supervised manner based on photometric consistency. Evaluations on DDAD and nuScenes show improved overall depth accuracy and cross-image depth consistency over state-of-the-art self-supervised methods under in-domain and cross-domain evaluation. Code is available at https://abualhanud.github.io/CrossDepthPage/.

</details>

#### 2026-09-03 - Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction

**Authors:** Chin-Yang Lin, Yang-Che Sun, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu
**Links:** [abs](https://arxiv.org/abs/2609.04201) - [pdf](https://arxiv.org/pdf/2609.04201)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction
- 作者：Chin-Yang Lin, Yang-Che Sun, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Wei-Chi Chiu, Yu-Lun Liu
- 出版日期：2026-09-03T17:59:53Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.04201

### 一句话总结
Scal3R 提出一种基于多参考相对位姿查询的在线 3D 重建方法，通过轻量可学习 token 与冻结骨干网络的非对称注意力注入，配合在线位姿图优化，显著抑制长视频场景下的累积漂移。

### 研究问题
在线 3D 重建模型在长视频上表现不佳，原因是将位姿回归到固定的首帧锚点会导致外推远超训练分布，微小漂移逐渐累积并放大为严重的几何崩溃。

### 核心思路/方法
- 观察到逐帧深度在重建失败时仍保持稳定，即骨干网络的局部几何完好，只有全局位姿头崩溃，基于这一解耦现象进行设计。
- 将在线重建重构为多参考相对位姿查询：使用约占总参数 1% 的轻量可学习 token，通过非对称注意力注入到完全冻结的骨干网络中，查询相对多个历史关键帧的位姿。
- 引入在线位姿图优化系统，结合回环检测（loop closure）以抑制长距离漂移。

### 主要贡献
- 揭示在线重建中局部几何（深度）与全局位姿解耦的失败模式，并据此设计新方法。
- 提出 Scal3R，利用冻结骨干+轻量 token 进行多参考相对位姿查询，训练效率高（单 GPU 8 小时收敛）。
- 在 KITTI 上将平均 ATE（绝对轨迹误差）较在线基线降低超过 60%。
- 在 Virtual KITTI、Sintel、TUM-Dynamic、ScanNet 和 7-Scenes 上达到最先进性能。

### 局限性
摘要未提供足够信息，无法确知方法在极端退化场景（如严重遮挡、纹理缺失）下的表现、对回环检测失败的敏感性、内存/推理速度开销、以及不同数据集间的泛化边界等细节。

### 阅读优先级
**高**。理由：该工作针对在线 3D 重建中长期存在的长视频漂移问题提供了新的问题洞察（几何-位姿解耦），方法设计轻量且训练高效，在多个基准上取得显著提升，兼具理论动机与实际应用价值。摘要信息完整，适合快速阅读以了解核心思想；若需复现或深入比较，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Online 3D reconstruction models perform poorly on long videos. This happens because regressing poses relative to a fixed first-frame anchor forces extrapolation far beyond the training distribution. Small drifts accumulate and amplify into significant geometric collapse. However, we observe that per-frame depth remains stable throughout this failure. The backbone's local geometry remains intact; only the global pose head breaks down. Motivated by this decoupling, we introduce Scal3R. This approach reformulates online reconstruction as multi-reference relative pose querying. We use lightweight learnable tokens, which make up about ~1% of the parameters, and inject them into a completely frozen backbone via asymmetric attention. This setup queries poses relative to multiple past keyframes. An online pose-graph optimization system with loop closure suppresses long-range drift. Scal3R reaches convergence in 8 hours on a single GPU. It reduces the average ATE by over 60% on KITTI compared to the online baseline. It also achieves state-of-the-art performance across Virtual KITTI, Sintel, TUM-Dynamic, ScanNet, and 7-Scenes. Project page: https://linjohnss.github.io/scal3r/

</details>

#### 2026-09-03 - Stable and Scalable Bundle Adjustment of Holistic 3D Structures

**Authors:** Shaohui Liu, Rémi Pautrat, Daniel Barath, Richard Hartley, Viktor Larsson, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2609.04026) - [pdf](https://arxiv.org/pdf/2609.04026)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stable and Scalable Bundle Adjustment of Holistic 3D Structures
- 作者：Shaohui Liu, Rémi Pautrat, Daniel Barath, Richard Hartley, Viktor Larsson, Marc Pollefeys
- 出版日期：2026-09-03T16:08:03Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.04026

### 一句话总结
本文提出一个统一框架，将束调整从稀疏点/线扩展至包含高阶几何关系（如共面、平行）的整体3D结构，并通过将组约束建模为类相机实体、以2D重投影误差表达，从而在保持传统点BA稀疏性和数值稳定性的同时，提升3D结构丰富度与几何精度。

### 研究问题
如何将束调整从仅优化稀疏点（及线）扩展为联合优化高阶几何关系（如共面性、平行性、线框结构），同时避免计算成本显著增加和数值稳定性下降的问题。

### 核心思路/方法
- 引入分类法：将具有直接2D测量的可扩展几何特征（点、线）与编码高阶关系的“组”区分开，并证明“组”可在BA框架中建模为类相机实体。
- 通过2D重投影测量同时表达组约束和跨特征关联（点-线关联），构造组诱导与跨特征的重投影误差。
- 在Schur消元下保持经典点BA的稀疏结构，避免直接3D正则化导致的病态条件和稳定性劣化。

### 主要贡献
- 提出统一框架，可联合优化几何特征与高阶关系，并保持经典BA的稀疏结构。
- 从理论上说明高阶关系组可被建模为类相机实体。
- 通过组与跨特征的重投影误差公式化，避免直接3D正则化带来的稳定性问题。
- 实验证明运行时间与经典点BA相当，同时生成显著更丰富的3D结构并提升几何精度。

### 局限性
摘要未提供足够信息来具体说明方法的局限（如对特定场景的退化情况、合成/真实数据上的失败案例、超参数敏感性等）。

### 阅读优先级
**高**
理由：该工作直接将经典束调整扩展至整体3D结构联合优化，且宣称在运行时间与经典BA相当的前提下提升结果丰富度与精度，对于多视角几何和3D重建方向的研究者具有重要参考价值；摘要提供的方法思路较完整，适合进一步精读原文验证实验细节。

</details>

<details>
<summary>Abstract</summary>

Bundle Adjustment (BA) is a cornerstone of 3D computer vision and has benefited from decades of advances in sparse optimization and numerical methods. It was originally developed for jointly optimizing camera intrinsics, poses and sparse 3D points. While extensions incorporate lines and other primitives, integrating richer geometric structures such as parallelism, coplanarity, or wireframes often introduces significantly increased computational cost and reduced numerical stability. In this paper, we propose a unified framework that extends bundle adjustment to jointly optimize geometric features and higher-order relations. We first introduce a taxonomy that distinguishes scalable geometric features with direct 2D measurements (e.g., points and lines), from groups encoding higher-order relations (e.g., coplanarity, parallelism, etc.), where we show that groups can be modeled as camera-like entities within the bundle adjustment framework. Building on this formulation, we propose that both group constraints and cross-feature relations (i.e., point-line associations) can be expressed through 2D reprojection measurements. By formulating group-induced and cross-feature reprojection errors, we preserve the sparsity structure of classical point-based BA under Schur elimination, while avoiding direct 3D regularization that degrades the conditioning and stability. Experiments on both real-world and synthetic datasets demonstrate runtime performance comparable to classical point-only bundle adjustment, while producing significantly richer 3D structures and improved geometric accuracy.

</details>

#### 2026-09-03 - Automated Weld Seam Recognition and 3D Mapping for Robotic Post Processing Using Photogrammetry and Semantic Segmentation

**Authors:** Augustin Raju, Abilash Madavath, Chandra Yuvesh Aubeeluck, Nicolas Pyschny, Felix Hackelöer, Florian Zwanzig
**Links:** [abs](https://arxiv.org/abs/2609.03970) - [pdf](https://arxiv.org/pdf/2609.03970)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** photogrammetry, 3D mapping, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Automated Weld Seam Recognition and 3D Mapping for Robotic Post Processing Using Photogrammetry and Semantic Segmentation
- 作者：Augustin Raju, Abilash Madavath, Chandra Yuvesh Aubeeluck, Nicolas Pyschny, Felix Hackelöer, Florian Zwanzig
- 出版日期：2026-09-03T15:07:52Z
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.03970

### 一句话总结
本文提出一种基于多视角图像语义分割与摄影测量的实验性视觉管线，用于焊缝的粗略定位与三维映射，作为高精度测量前的预定位阶段，以减少机器人在后处理任务中的扫描工作量与数据量。

### 研究问题
如何在大尺寸工件场景下，通过低成本、高效的视觉方法快速近似定位焊缝，且无需使用激光扫描仪或结构光传感器进行全表面高精度扫描，从而为机器人后处理（如打磨、精整、检测）提供引导。

### 核心思路/方法
1. 从多个视角拍摄工件图像。
2. 使用语义分割模型从图像中识别焊缝区域。
3. 利用摄影测量技术对工件进行三维重建。
4. 将图像中识别到的焊缝像素投影到重建的三维模型上，实现焊缝在三维空间中的映射与粗略定位。

该管线作为高精度测量前的预筛阶段，旨在缩小后续精确扫描的感兴趣区域。

### 主要贡献
- 提出一种面向机器人后处理的焊缝识别与三维映射的实验性视觉管线。
- 结合语义分割与摄影测量，实现对焊缝的近似空间定位，避免了高精度传感器全表面扫描带来的时间与数据开销。
- 强调该方案作为高精度测量前预阶段的实用性，可提升整体数据采集效率。

### 局限性
摘要未提供足够信息，包括：具体实验对象规模、焊缝分割精度、三维映射误差、与激光扫描的定量对比、计算耗时、场景光照或遮挡条件等细节均未在摘要中说明。摘要明确指出该方法是“experimental”且目标是“approximate localization”，且需在高精度测量前使用，具体精度性能数据无法从摘要获取。

### 阅读优先级
**中**
理由：论文聚焦于机器人后处理中的焊缝预定位，结合了语义分割与摄影测量，思路有一定工程应用价值。但摘要表明其为“experimental”的预定位阶段，且未给出定量性能结果，属于一种辅助性管线而非核心精度突破，适合对机器人视觉引导、三维重建与分割结合应用感兴趣的读者快速浏览。若追求高精度方法或详细对比实验，则优先级可下调。

</details>

<details>
<summary>Abstract</summary>

Accurate identification of weld seam geometries is essential for automated robotic post processing operations such as grinding, finishing, and inspection. For large workpieces, complete surface scanning using high precision laser scanners or structured light sensors can be time consuming and often generates substantial amount of data that are not relevant. This paper presents an experimental vision based pipeline for the approximate localization of weld seams. This serves as a preliminary stage before high precision measurement. The proposed approach aims to reduce the overall scanning effort and data acquisition efficiency. The proposed method includes capturing images of the workpiece from multiple viewpoints, identifying weld seams from the images using semantic segmentation, reconstructing the workpiece using photogrammetry, and projection of identified weld seams into the reconstructed model.

</details>

#### 2026-09-03 - OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping

**Authors:** Zelong Lv, Sicheng Xu, Jianfeng Xiang, Ruicheng Wang, Yue Dong, Yu Deng, Guangzhong Sun, Jiaolong Yang
**Links:** [abs](https://arxiv.org/abs/2609.03919) - [pdf](https://arxiv.org/pdf/2609.03919)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D mapping, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping
- 作者：Zelong Lv, Sicheng Xu, Jianfeng Xiang, Ruicheng Wang, Yue Dong, Yu Deng, Guangzhong Sun, Jiaolong Yang
- 出版日期：2026-09-03
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.03919

### 一句话总结
OctWorld 提出一种基于八叉树3D记忆（OctMap）的视频扩散框架，从单张图像沿用户指定相机轨迹生成长距离、空间一致且可探索的高保真场景视频。

### 研究问题
如何解决长距离视频生成中——即当相机路径延伸、视角覆盖广泛且重新访问已生成区域时——保持全局空间一致性的挑战。

### 核心思路/方法
- 提出 OctMap：一种可扩展、空间自适应的3D记忆模块，渐进地将生成的视觉观测及其对应的深度图融合进全局表示。
- OctMap 在动态稀疏八叉树中执行 TSDF 融合，空间分辨率根据图像证据自适应变化，从而在不同场景尺度下保持几何和外观细节，同时维持较低内存开销。
- 框架整体为自回归式视频扩散模型：以单张图像为起点，沿用户指定轨迹迭代生成内容，并借助持久化3D记忆维持跨帧一致。

### 主要贡献
- 提出 OctWorld，一个具备持久3D记忆的长距离、世界一致视频生成框架。
- 设计 OctMap——基于稀疏八叉树与 TSDF 融合的可扩展3D记忆，兼顾自适应分辨率与内存效率。
- 实验表明 OctWorld 在现有基准及长距离生成挑战性设置上优于先前方法，并验证 OctMap 相比基于点云缓存和固定分辨率 TSDF 体素表示的显著优势。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
- 理由：论文针对视频生成中长距离空间一致性的核心难题，提出结构新颖的八叉树+TSDF融合3D记忆方案，且研究发表于2026年，方法具有明显创新性。适合关注生成式3D场景、世界模型及视频扩散模型的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

We present OctWorld, a video diffusion framework with persistent 3D memory for generating explorable, world-consistent, and high-fidelity visual scenes. Given a single image, OctWorld performs stable autoregressive world generation along user-specified camera trajectories. We focus on long-range generation, characterized by extended camera paths and wide viewpoint coverage, where preserving spatial consistency is particularly challenging when previously generated regions are revisited. To address this problem, we introduce OctMap, an extensible and spatially adaptive 3D memory that progressively fuses generated visual observations and their corresponding depth maps into a global representation. OctMap employs TSDF fusion within a dynamic sparse octree whose spatial resolution adapts to image evidence. This design preserves geometric and appearance details across diverse scene scales while maintaining low memory overhead. Experiments demonstrate that OctWorld generates long-range, spatially consistent videos and outperforms prior methods on both existing benchmarks and challenging long-range generation settings. OctMap also provides clear advantages over point-based caches and fixed-resolution TSDF volumes. Project page: https://maxtirerror.github.io/octworldpage/

</details>

#### 2026-09-03 - STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction

**Authors:** Bocheng Li, Wenjuan Zhang, Jie Pan. Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang
**Links:** [abs](https://arxiv.org/abs/2609.03447) - [pdf](https://arxiv.org/pdf/2609.03447)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, photogrammetry, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction
- 作者：Bocheng Li, Wenjuan Zhang, Jie Pan, Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang
- 出版日期：2026-09-03
- 分类：3D Reconstruction & Multi-view Geometry（次要：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2609.03447

### 一句话总结
本文提出STARS-GS，一种结构感知正则化的3D高斯泼溅框架，通过改进场景划分、邻域高斯组织与自适应表面正则化，显著提升大规模航拍影像的3D表面重建精度。

### 研究问题
如何解决大规模复杂场景下基于3D高斯泼溅的表面重建存在三大挑战：（1）场景划分可能切断连续结构；（2）几何约束仅关注单个高斯而忽略其局部组织；（3）统一正则化难以适应异质几何结构。

### 核心思路/方法
- 结构感知场景划分策略：在划分时尽量保持连续场景结构，并通过边界细化减少跨区域几何不一致与拼接伪影。
- 邻域感知高斯组织：将几何约束从单个图元扩展到邻域组织，促使高斯更好地贴合局部表面几何。
- 自适应表面正则化：根据局部几何特征动态调整正则化强度，在结构化区域保持几何一致性，在非结构化区域保留合理变异。

### 主要贡献
- 提出STARS-GS框架，综合解决场景划分、高斯邻域组织与自适应正则化三方面问题。
- 在大规模航拍摄影测量基准上，平均F1分数从次优方法的0.640提升至0.698，相对提升约9.1%，验证了几何精度与表面完整性的有效改进。

### 局限性
摘要未提供足够信息。摘要仅提及实验在公开基准上验证优于现有高斯类方法，但未说明计算开销、内存消耗、对超参数敏感性、极端场景（如强遮挡/弱纹理区域）表现等潜在限制。

### 阅读优先级
**高**。该工作聚焦于当前热门的3D高斯泼溅技术在大规模航拍表面重建中的实际落地问题，提出了三项针对性改进且有效果量化提升（F1相对提高9.1%），对从事遥感三维重建、城市建模及神经渲染相关研究的读者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Large-scale 3D surface reconstruction from aerial imagery is fundamental to geospatial mapping and urban modeling. Recent advances in 3D Gaussian Splatting (3DGS) have demonstrated considerable potential for this task. However, existing methods still face three major challenges in large and complex scenes: scene partitioning may split continuous scene elements across independently optimized sub-regions; geometric constraints mainly focus on the attributes of individual Gaussians while overlooking their local organization; and uniform regularization struggles to accommodate heterogeneous geometric structures. To address these issues, we propose STARS-GS, a structure-aware 3DGS framework for large-scale surface reconstruction. First, we introduce a structure-aware scene partitioning strategy that better preserves continuous scene structures during partitioning and reduces cross-region geometric inconsistencies and stitching artifacts through boundary refinement. Second, we develop neighborhood-aware Gaussian organization that extends geometric constraints from individual primitives to their neighborhood organization, encouraging Gaussians to better conform to local surface geometry. Third, we introduce adaptive surface regularization that adjusts the regularization strength according to local geometric characteristics, promoting geometric consistency in structured regions while preserving plausible variations in unstructured regions. Extensive experiments on large-scale aerial photogrammetry benchmarks demonstrate that STARS-GS consistently outperforms the evaluated Gaussian-based methods in surface reconstruction. It increases the average F1-score from 0.640 for the second-best method to 0.698, corresponding to a relative improvement of approximately 9.1\%, demonstrating effective improvements in geometric accuracy and surface completeness.

</details>

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

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-03 - Sparse auto-regressive modeling for scene generation from multi-view images

**Authors:** Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud
**Links:** [abs](https://arxiv.org/abs/2609.03931) - [pdf](https://arxiv.org/pdf/2609.03931)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sparse auto-regressive modeling for scene generation from multi-view images
- 作者：Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03931

### 一句话总结
本文提出 SPAR3S，一种基于稀疏体素对齐的 3D 隐空间自回归生成模型，仅需多视图图像即可在无 3D 真值监督条件下完成条件场景补全与生成。

### 研究问题
如何从稀疏、无约束的多视图图像中生成完整 3D 场景，在无需大规模 3D 真值标注的前提下，兼顾超越可见内容的推理能力与计算可行性。

### 核心思路/方法
- 构建紧凑、稀疏的体素对齐 3D 隐空间，仅表示被占据的体素，避免高维密集表示的计算开销。
- 通过可微分的 3D Gaussian Splatting 与光度监督，直接从多视图图像学习该稀疏隐空间，无需 3D 真值。
- 将场景补全转化为在体素网格上预测缺失隐式令牌（latent tokens）及其空间位置（occupancy）的任务。
- 训练掩码自回归 Transformer，联合建模体素占据状态与隐式令牌数值，以实现高效且空间一致的未见区域生成。

### 主要贡献
- 提出一种无需 3D 真值监督的稀疏 3D 隐生成模型（SPAR3S），用于条件场景补全。
- 设计了由多视图图像经光度监督学习的稀疏体素对齐隐空间表征。
- 采用掩码自回归 Transformer 联合建模占据与隐特征，实现结构化场景生成。
- 在合成室内场景中取得优于现有工作的新视角合成质量，并在 RealEstate10k 上验证了真实世界数据的泛化性。

### 局限性
摘要未提供足够信息，未明确提及方法的具体失败案例、计算资源需求、对输入视图数量/分布的敏感性，或扩展至更大规模场景时的潜在瓶颈。

### 阅读优先级
高。理由：该工作聚焦 3D 场景补全这一核心挑战，提出无需 3D 真值监督的稀疏隐空间自回归方案，兼顾效率与生成质量，相关技术路线（Gaussian Splatting + 自回归 Transformer）具有较强创新性与应用潜力，适合场景生成与神经渲染方向研究者优先关注。

</details>

<details>
<summary>Abstract</summary>

Generating complete 3D scenes from sparse, unconstrained views is a fundamental challenge in 3D vision which requires reasoning beyond observed content while remaining computationally tractable. Existing feed-forward reconstruction methods are inherently limited to content visible in the input images, while 3D generative modeling is hindered by the high computational cost of dense volumetric representations and the scarcity of large-scale 3D supervision. We introduce SPAR3S, a sparse voxel-aligned 3D latent generative model for conditional scene completion without requiring ground-truth 3D data for supervision. Our key insight is to formulate 3D scene generation in a structured, compact, voxel-aligned 3D latent space where only occupied voxels are represented. We learn this sparse latent space directly from multi-view images using photometric supervision via differentiable 3D Gaussian Splatting. Given a partial set of observed voxels encoded from sparse input views, scene completion reduces to predicting the missing latent tokens and their spatial support within the voxel grid. To this end, we train a masked autoregressive transformer that jointly models voxel occupancy and latent token values, enabling efficient and spatially consistent generation of unseen regions. We demonstrate the effectiveness of our method on synthetic indoor scenes, achieving higher novel-view quality than prior work. We further validate its generalization on RealEstate10k, highlighting its applicability to real-world data.

</details>

#### 2026-09-03 - Reparametrizing 3D Gaussian Splatting for Real-Time Palette-based Color and Luminance Editing

**Authors:** Cheng-Kang Ted Chao, Yotam Gingold
**Links:** [abs](https://arxiv.org/abs/2609.03897) - [pdf](https://arxiv.org/pdf/2609.03897)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reparametrizing 3D Gaussian Splatting for Real-Time Palette-based Color and Luminance Editing
- 作者：Cheng-Kang Ted Chao, Yotam Gingold
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03897

### 一句话总结
本文提出一种对预训练3D高斯泼溅（3DGS）模型重新参数化球谐系数的方法，实现基于调色板的实时颜色与亮度独立编辑，并支持像素级颜色约束。

### 研究问题
如何在预训练3DGS表示上实现实时的、具备独立颜色（色调/饱和度）与亮度控制的调色板级交互式编辑，并克服先前基于图元空间（primitive-space）方法因alpha混合导致的编辑区域溢出问题。

### 核心思路/方法
- 对预训练vanilla 3DGS的球谐函数进行重新参数化，使其编码与视角相关的调色板权重，而非从零训练新表示。
- 通过基于图像空间稀疏性的损失函数，同时求解调色板权重和调色板颜色。
- 亮度编辑通过沿无彩色轴（achromatic axis）的逐像素权重偏移实现，等效于逐像素的调色板感知亮度编辑。
- 采用迭代重加权最小二乘（IRLS）与阻尼块坐标下降（damped block-coordinate descent）实现快速求解（数十毫秒）。
- 编辑结果可高效烘焙回vanilla 3DGS，保持标准查看器兼容性。

### 主要贡献
- 实现比先前基于调色板的3DGS方法更稀疏、更局部化的颜色编辑。
- 首次为3DGS提供每个调色板颜色的独立亮度控制。
- 支持视角一致的像素级颜色约束，这是先前3DGS方法不具备的能力。
- 编辑过程可实时运行，且与标准3DGS渲染管线兼容。

### 局限性
摘要称该方法较先前方法实现了更稀疏和更局部的编辑，但未提供定量比较数据、用户研究结果或对场景规模/复杂度的限制说明。亦未提及可能的伪影类型、处理失败场景或对预训练模型质量的依赖程度。摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向3DGS交互编辑这一细分应用方向，方法创新（重新参数化球谐、视角空间亮度编辑）有一定新颖性，但受众限于从事3D编辑/渲染交互的研究者；若读者关注实时3D编辑或调色板方法，则值得细读，否则非核心领域可暂缓。

</details>

<details>
<summary>Abstract</summary>

Professional color editing requires precise control over both color (hue and saturation) and lightness, ideally through separate, independent controls. We present a real-time interactive color editing framework for 3D Gaussian Splatting that supports palette-based recoloring, per-palette tone curves for color-aware luminance adjustment, and pixel-level color constraints. Rather than training a new representation from scratch, we reparameterize the spherical harmonics of a pretrained vanilla 3DGS to encode view-dependent palette weights. We simultaneously solve for weights and palette colors via a loss based on image-space sparsity. Luminance editing is realized as a per-pixel weight shift along the achromatic axis, which we show is equivalent to a per-pixel palette-aware luminance edit. This view-space formulation addresses a core limitation of prior primitive-space methods, where alpha-blending breaks per-Gaussian sparsity and causes edits to bleed into unintended regions. Our edits run in tens of milliseconds via an iteratively reweighted least squares and damped block-coordinate descent that couples tone curves and palette shifts under view-space sparsity. Our representation can be efficiently baked back into a vanilla 3DGS, preserving compatibility with standard viewers. We demonstrate sparser, more localized edits than prior palette-based 3DGS methods, while enabling independent luminance control per palette color and view-consistent pixel-level constraints, capabilities previously unavailable for 3DGS.

</details>

#### 2026-09-03 - Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations

**Authors:** Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu
**Links:** [abs](https://arxiv.org/abs/2609.03657) - [pdf](https://arxiv.org/pdf/2609.03657)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, robotics, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations
- 作者：Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu
- 出版日期：2026-09-03T10:54:49Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03657

### 一句话总结

本文提出一种无需优化的3D形态扰动正则化方法，利用3D高斯泼溅的形态参数空间操作，提升稀疏视角下3D场景重建的质量和几何先验学习，并显著改善下游机器人操控策略的性能。

### 研究问题

NeRF和3DGS等3D场景表示在稀疏视角设置下存在严重伪影；现有的生成式3D伪影修复器依赖成对的受损/干净渲染数据，且需要针对不同视角配置进行昂贵的逐场景重建；而2D图像增强虽有即时正则化效果，但缺乏能保持跨视角空间一致性的显式3D等效方法。本文旨在回答：如何设计一种无需优化、能保持空间一致性的3D表示正则化方法，以支持3D感知训练？

### 核心思路/方法

 核心是提出3D形态扰动（3D Morphological Perturbations），将其作为无需优化的正则化器。具体地，利用显式3DGS表示，将每个高斯视为类似于2D像素的基本构建单元，并在其形态参数空间（尺度、旋转、剪枝）上施加扰动。该方法从数据集整理过程中消除了逐场景的3DGS优化循环，使模型能学习比稀疏视角基线更强的几何先验。

### 主要贡献

1. 提出一种无需优化的3D形态扰动正则化方法，显式作用于3DGS的形态参数空间，能够保持空间一致性。
2. 该方法避免了数据集构建中昂贵的逐场景3DGS重建/优化过程。
3. 在轻量视频扩散测试环境中验证，该方法相比稀疏视角基线有助于学到更强的几何先验。
4. 扩展到140亿参数的视频模型（经ControlNet），在保持视觉保真度的同时，相对最先进的图像到图像3D伪影修复器，将平均深度误差降低12.5%。
5. 在下游机器人操控策略中，在4项操纵任务中的3项上将成功率提升最多8.0%。

### 局限性

摘要未提供足够信息。具体而言，本文未明确讨论所提出方法的局限性，如对3DGS表示类型的依赖程度、扰动幅度选择的敏感性、在不同场景类型上的泛化边界，或计算开销的具体细节等。

### 阅读优先级

**高**。理由：该工作针对稀疏视角3D重建这一重要难题，提出一种简洁、无需优化的正则化方案，直接规避了昂贵的数据集构建流程；同时在大规模视频模型和下游机器人任务上展示了显著的定量改进，具有较强的方法普适性与应用价值。且论文归属神经场景表示与渲染方向，发表于2026年，新颖性较突出。

</details>

<details>
<summary>Abstract</summary>

3D scene representations like NeRF and 3D Gaussian Splatting (3DGS) suffer severe artifacts in sparse-view settings. Recent generative 3D artifact fixers attempt to address this, but rely on paired corrupted and clean renders requiring costly, per-scene reconstructions across varying view configurations. While 2D image augmentations act as instant regularizers, no explicit equivalents exist for 3D representations to preserve spatial consistency across views, an essential property for 3D-aware training. We propose 3D Morphological Perturbations as an optimization-free regularizer that preserves spatial consistency. Leveraging explicit 3DGS, we treat each Gaussian as a fundamental building block - analogous to a 2D pixel - and apply perturbations across its morphological parameter space via scale, rotation, and pruning. Our method eliminates per-scene 3DGS optimization loops from dataset curation while enabling models to learn stronger geometric priors than sparse-view baselines in diagnostic ablations conducted on a lightweight video diffusion sandbox. Scaled to a 14B-parameter video model via ControlNet, our approach maintains visual fidelity while reducing mean depth error by 12.5% over state-of-the-art image-to-image 3D artifact refiners, ultimately boosting downstream robotics policy success rates by up to 8.0% across 3 of 4 manipulation tasks.

</details>

#### 2026-09-03 - Stabilizing Camera-Controlled Novel View Synthesis at Inference Time

**Authors:** Prajwal Singh, Arjun Badola, Seema Kumari, Hajime Nagahara, Shanmuganathan Raman
**Links:** [abs](https://arxiv.org/abs/2609.03639) - [pdf](https://arxiv.org/pdf/2609.03639)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stabilizing Camera-Controlled Novel View Synthesis at Inference Time
- 作者：Prajwal Singh, Arjun Badola, Seema Kumari, Hajime Nagahara, Shanmuganathan Raman
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03639

### 一句话总结
本文提出一种无需训练、仅在推理阶段通过将相机运动分解为小自回归步长来稳定单图新视角合成的方法（CamTrol++），显著提升了大视角运动与长时程生成下的时间与几何一致性。

### 研究问题
如何在不重训练或修改扩散模型主干的情况下，提高基于预训练视频扩散模型的、无训练相机控制新视角合成在大相机运动和长生成长度下的稳定性？

### 核心思路/方法
- 核心发现：稳定性的主要来源很简单——将相机运动分解为小的自回归步骤，可限制每步几何畸变并减少误差累积。
- 通过受控相机步长研究，发现性能在小步长下保持稳定，当每步运动接近18°–20°时性能明显下降。
- 进一步评估了几何约束的空间注意力与低频外观锚定作为辅助改进，并结合高效的无配准（registration-free）变形流水线。
- 全程无需训练，也不修改扩散模型主干。

### 主要贡献
- 揭示了影响无训练相机控制新视图合成稳定性的关键因素是相机运动步长分解。
- 提出CamTrol++方法，在RealEstate10K和MegaScene数据集上提升时间与几何一致性、下游3D重建质量和生成效率，超越无训练基线。
- 方法在56帧生成及深度数据受到较大破坏时仍保持有效。

### 局限性
摘要未提供足够信息。具体而言，文中未提及方法在哪些场景下可能失效、是否有计算开销增加或潜在的内存限制，也未给出与其他可训练方法的完整对比结果。

### 阅读优先级
**高**。理由：该工作针对无训练相机控制新视图合成的稳定性问题，给出了简单有效的推理策略，不依赖额外训练，实用性较强；同时在大视角、长时程和深度退化条件下验证了效果，对相关研究方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Training-free, camera-controlled novel view synthesis from a single image using pre-trained video diffusion models often becomes unstable under large camera motion and long generation horizons. Existing approaches commonly combine several inference-time components, making it unclear which design choices are most important for stability. We show that the main source of stability is simple. Decomposing camera motion into small autoregressive steps limits per-step geometric distortion and reduces error accumulation. A controlled camera-step study shows that performance remains stable for small motions and degrades more strongly as the per-step motion approaches $18$-$20^\circ$. We further evaluate geometry-constrained spatial attention and low-frequency appearance anchoring as supporting refinements, together with an efficient registration-free warping pipeline. Across RealEstate10K and MegaScene, CamTrol++ improves temporal and geometric consistency, downstream 3D reconstruction quality, and generation efficiency over training-free baselines. The method remains effective for 56-frame generation and under substantial controlled depth corruption. These results show that careful control of camera motion at inference time can substantially improve the stability of camera-controlled novel view synthesis without retraining or modifying the diffusion backbone.

</details>

#### 2026-09-03 - TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization

**Authors:** Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala
**Links:** [abs](https://arxiv.org/abs/2609.03613) - [pdf](https://arxiv.org/pdf/2609.03613)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization
- 作者：Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03613

### 一句话总结
TileGS 通过对高斯溅射栅格化过程进行瓦片内的深度局部重排，将每个长瓦片范围切分为更短的深度局部子范围并逐层前向光栅化，从而在保持与基线数值一致的前提下实现渲染加速。

### 研究问题
标准 3D Gaussian Splatting (3DGS) 栅格化需要遍历全局排序的瓦片流，导致每个瓦片对应的范围过长、几何属性传输开销大，限制了实时渲染效率。本文旨在通过瓦片内的局部重排机制减少栅格化遍历开销，同时维持输出质量。

### 核心思路/方法
- 提出 **TileGS**，对每个瓦片的高斯分布按深度进行局部重组织，将一个长范围瓦片拆分为一组更短的深度局部范围。
- 栅格化时按**前到后顺序**处理这些深度局部范围，实现更紧凑的遍历。
- 在粗排序不足以与基线合成结果对齐之处，引入**选择性修复**机制以保持合成质量。
- 设置了默认的 **No-GW（No Geometry-Write）** 变体，避免写出几何属性以降低内存压力。

### 主要贡献
- 提出一种瓦片局部深度分箱的 3DGS 栅格化重组方案，提升光栅化内核速度。
- 在 9 场景基准及桌面/笔记本 Ada GPU 上验证：RTX 4090 上实现平均 **1.44x** 栅格内核加速，端到端帧加速为 RTX 4090 上 **1.069x**、RTX 1000 Ada 上 **1.094x**（对比 gsplat）。
- 输出质量与 gsplat 匹配至数值噪声级别（|ΔPSNR|、|ΔSSIM|、|ΔLPIPS| 均 < 0.001）。
- 通过 Nsight Compute 全量分析，论证加速来源于**有效栅格遍历量减少**，而非字节量减少、合并改善、占用率提升或分歧降低；并定位几何属性为剩余内存压力主因（占光栅总流量 85.8%、超额扇区 88.6%）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作聚焦于 3DGS 栅格化的工程优化层面，对渲染效率有明确量化提升，且通过详细 profiling 分析提供了机理性的解释；适合从事实时神经渲染、3DGS 系统优化的研究者关注。但摘要未披露方法在不同纹理/场景复杂度下的泛化性、修复策略的具体代价以及是否适用于大规模场景等细节，故优先级不设为最高。

</details>

<details>
<summary>Abstract</summary>

Real-time 3D Gaussian Splatting (3DGS) achieves high rendering quality, but standard rasterization still traverses a globally sorted tile stream that creates long per-tile ranges and heavy geometry-attribute traffic. We present TileGS, a tile-local reorganization of Gaussian splatting. TileGS turns each long tile range into a sequence of shorter depth-local ranges, rasterizes those ranges in front-to-back order, and applies selective repair where coarse ordering is insufficient to match baseline compositing. Across a 9-scene benchmark on desktop and laptop Ada GPUs, our default No-GW (No Geometry-Write) variant delivers a mean 1.44x raster-kernel speedup on RTX 4090 and mean end-to-end frame speedups of 1.069x on RTX 4090 and 1.094x on RTX 1000 Ada over gsplat--a widely used optimized open-source 3DGS implementation--while matching the gsplat output up to numerical noise (|Delta PSNR| < 0.001 dB, |Delta SSIM| < 0.001, |Delta LPIPS| < 0.001). Full-suite RTX 4090 Nsight Compute profiling reveals TileGS is faster despite lower SM throughput, lower active-warp occupancy, and higher DRAM traffic, while total SASS thread instructions fall by 1.26x. Source-attributed profiling confirms that geometry attributes dominate the remaining memory pressure (85.8% of total raster traffic and 88.6% of excess sectors). Together, these counters support the interpretation that TileGS improves raster performance by reducing effective raster traversal work, rather than by reducing byte volume, improving coalescing, increasing occupancy, or directly reducing measured warp divergence.

</details>

#### 2026-09-03 - TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates

**Authors:** Theo Morales, Nhat-Quynh Le-Pham, Robin Atkins, Binh-Son Hua
**Links:** [abs](https://arxiv.org/abs/2609.03534) - [pdf](https://arxiv.org/pdf/2609.03534)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, Gaussian primitive, novel view synthesis, view synthesis, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates
- 作者：Theo Morales, Nhat-Quynh Le-Pham, Robin Atkins, Binh-Son Hua
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03534

### 一句话总结
该论文提出一种基于分段截断梯度的优化方法，以缓解3D高斯泼溅中的梯度消失问题，从而提升场景重建质量与优化稳定性。

### 研究问题
3D高斯泼溅在从视觉输入学习高斯原语时，优化过程易受梯度消失现象影响——离高斯原语较远的像素其梯度幅值过小，难以有效影响原语属性，导致场景重建次优。

### 核心思路/方法
提出使用分段截断梯度（piecewise truncated gradient）公式替代经典梯度更新，通过截断梯度机制增强远距离像素对高斯原语属性的梯度信号，从而改善训练稳定性，并提升对不同初始化方式的鲁棒性。

### 主要贡献
- 提出针对梯度消失问题的分段截断梯度方法，显著改进3D高斯泼溅的优化过程。
- 在随机初始化与COLMAP初始化下均能一致提升重建性能，且可泛化至静态与动态高斯泼溅场景。
- 指出现有动态场景基准的局限性，并引入基于合成3D场景的新动态高斯泼溅基准数据集。

### 局限性
摘要未提供足够信息来详细分析局限性，包括方法在特定场景下的潜在不足、计算开销、或与现有技术对比的失败案例均未说明。

### 阅读优先级
**高**。理由：该方法针对3D高斯泼溅中常见的梯度消失问题，提出简单且具通用性的改进方案，同时兼顾静态与动态场景，并附带新基准数据集，兼顾理论与应用价值，适合关注神经场景表示与渲染的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has become a de facto scene representation for novel view synthesis, yet robustly learning 3D Gaussian primitives from visual input remains challenging. Standard optimization relies on gradient-based updates, but a common issue is the gradient vanishing phenomenon: a pixel far from a Gaussian primitive often has diminishing gradient magnitudes to influence primitive attributes, resulting in suboptimal scene reconstruction. In this paper, we propose a method to address gradient vanishing with a piecewise truncated gradient formulation that improves the optimization stability and robustness to initializations. We show that our method consistently improves 3D Gaussian Splatting with random and COLMAP initializations while being generalizable across static and dynamic Gaussian Splatting. As a by-product, we also examine the limitations of current benchmarks for dynamic scenes, and introduce a novel dataset for benchmarking dynamic Gaussian Splatting using synthetic 3D scenes. We demonstrate the effectiveness of our method in both static and dynamic settings for the public benchmarks and our proposed dataset.

</details>

#### 2026-09-03 - P-CORE: Self-Supervised Surface Consistency for Point-Based Neural Editing

**Authors:** Yanshu Zhang, Shichong Peng, Mehran Aghabozorgi, Alireza Moazeni, Ke Li
**Links:** [abs](https://arxiv.org/abs/2609.03349) - [pdf](https://arxiv.org/pdf/2609.03349)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, NeRF, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：P-CORE: Self-Supervised Surface Consistency for Point-Based Neural Editing
- 作者：Yanshu Zhang, Shichong Peng, Mehran Aghabozorgi, Alireza Moazeni, Ke Li
- 出版日期：2026-09-03T04:12:39Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03349

### 一句话总结
本文提出一种自监督方法P-CORE，通过保证点云变形前后表面预测的一致性，提升基于点的神经表示在大变形自由编辑下的鲁棒性，减少空洞与不连续伪影。

### 研究问题
基于点的神经表示在无固定连接的情况下能自由编辑形状，但大变形时容易产生表面空洞与不连续。如何在不依赖变形后真实多视图图像的前提下，提升点表示方法对大形变的适应能力。

### 核心思路/方法
- 核心思想：生成随机变形，并约束“变形后点云预测的表面”等于“原始点云预测表面施加相同变形”的结果，从而在自监督信号下维持表面一致性。
- 实现载体：采用基于注意力的点表示（attention-based point representations），区别于基于splatting的点表示——前者使用点间的学习插值核，而后者在每个点周围使用固定高斯核。
- 该学习插值核能够适应大变形，而无需增删点。

### 主要贡献
- 提出新颖的自监督表面一致性约束，使点基神经表示无需变形真实图像即可适应大变形。
- 将方法集成到注意力式点表示中，利用可学习插值核替代高斯核，提升变形鲁棒性。
- 在合成编辑基准（Neural Editor、Objaverse）上，零样本编辑性能优于现有基于点的方法，显著减少伪影。
- 在DTU和Mip-NeRF 360数据集上的定性实验表明其在真实场景中的有效性。

### 局限性
摘要未提供足够信息（未提及计算开销、极端变形情况、失败案例、对训练数据规模的要求或与其他非点基表示方法的比较）。

### 阅读优先级
**中**
理由：该方法针对点基神经编辑在大变形下的鲁棒性问题，提出新颖的自监督一致性约束，具有明确技术动机和较好实验验证，适用于从事神经渲染与形状编辑方向的研究者。但摘要中缺乏方法细节与定量对比的完整描述，且未披露运行效率等信息，非核心方向读者可不优先精读。

</details>

<details>
<summary>Abstract</summary>

Advances in neural rendering have enabled high-fidelity multi-view reconstruction of 3D scenes. However, free-form non-rigid shape editing remains a significant challenge. Point-based neural representations are highly desirable for multi-view reconstruction because they lack fixed connectivity, which does not constrain the learned surface topology to that of the initialization. Yet this same property causes point-based representations to struggle with holes and surface discontinuities under large deformations. To address this, we propose a novel self-supervised method to enable point-based representations to adapt to large deformations without requiring ground truth multi-view images of deformed geometry. The key idea is to generate random deformations and to ensure consistency in the predicted surface before and after deformation. In particular, the surface prediction from the deformed point cloud should be the same as the deformation applied to the surface prediction from the original point cloud. We incorporate our approach into attention-based point representations, which differ from splatting-based point representations in their use of a learned interpolation kernel between points as opposed to a Gaussian kernel around each point. This learned interpolation kernel can learn to adapt to large deformations, without requiring addition or removal of points. We show that our framework significantly enhances its robustness to large deformations. Experiments on synthetic geometry editing benchmarks (Neural Editor, Objaverse) demonstrate that our approach outperforms existing point-based methods in zero-shot editing and significantly reduces artifacts. Furthermore, qualitative results on the DTU and Mip-NeRF 360 datasets demonstrate our method's effectiveness on real-world scenes.

</details>

#### 2026-09-03 - PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations

**Authors:** Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li
**Links:** [abs](https://arxiv.org/abs/2609.03341) - [pdf](https://arxiv.org/pdf/2609.03341)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations
- 作者：Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03341

### 一句话总结
PointGT 提出了一种基于点的3D表示方法，使得对象几何形状与外观纹理能够同时进行编辑，并保持高渲染质量。

### 研究问题
如何在基于点的神经表示中，实现几何形变与高分辨率纹理编辑的兼容与同步操作，克服现有体积表示（如3D高斯溅射）难以同时支持几何与纹理编辑的局限。

### 核心思路/方法
PointGT 将适合几何形变的点基表示与一种学习得到的 UV 映射技术相结合：点基表示支撑几何变形，而UV映射支持高分辨率纹理编辑，从而实现两者的统一编辑框架。

### 主要贡献
- 提出 PointGT，一种支持同时编辑几何与外观的点基3D表示方法。
- 方法兼顾几何形变能力与高分辨率纹理编辑能力，据摘要所述，其精细编辑在渲染质量上表现良好。

### 局限性
摘要未提供足够信息（如对复杂场景的可扩展性、编辑操作的限制或计算开销等均未提及）。

### 阅读优先级
**中**。理由：该工作面向3D表示的可编辑性这一活跃方向，思路具有一定创新性，但摘要未提供定量实验对比或性能数据，实际效果与局限性需要进一步阅读正文判断。

</details>

<details>
<summary>Abstract</summary>

We present PointGT, a point-based 3D representation that enables simultaneous editing of object geometry and appearance. Existing reconstruction and view synthesis techniques produce volumetric 3D representations that are high-quality and photorealistic, but are difficult to edit. In particular, recent efforts to enable texture editing for 3D Gaussian Splatting representations are not compatible with geometry edits and deformations. Our method combines a point-based representation that is well-suited for geometry deformations with a learned UV mapping technique that enables high-resolution texture editing. We show that PointGT enables fine-grained editing of both geometry and texture in point-based neural representations with high rendering quality.

</details>

#### 2026-09-03 - Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training

**Authors:** Yixiong Yang, Sisheng Zhang, Qingsong Yan, Shaohuai Shi, Qiang Wang
**Links:** [abs](https://arxiv.org/abs/2609.03334) - [pdf](https://arxiv.org/pdf/2609.03334)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training
- 作者：Yixiong Yang, Sisheng Zhang, Qingsong Yan, Shaohuai Shi, Qiang Wang
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03334

### 一句话总结
本文提出一种基于拉普拉斯图像分解与由粗到细频率分阶段训练的3D高斯泼溅（3DGS）训练方案，通过归档低频高斯场、仅优化高频残差来减少训练中的活跃高斯数量，从而加速训练并保持重建质量。

### 研究问题
3DGS训练中的关键瓶颈是高斯原语（Gaussian primitives）的持续增长，导致优化成本上升和收敛变慢，尤其在高分辨率场景下更为严重。本文旨在通过减少训练过程中的活跃高斯数量来降低优化开销、加速训练。

### 核心思路/方法
本文提出“Laplacian Frequency Hierarchies”方案，结合拉普拉斯图像分解与由粗到细、按频率分阶段的训练过程。具体为：
1. 先拟合较低频率结构；
2. 将对应的低频高斯场归档（archive）；
3. 后续高斯场仅针对高频残差进行优化，无需承担全部原语负担；
4. 在推理阶段通过图像域内的拉普拉斯风格重建，将各渲染分量合成最终图像。

该方案为插件式（plug-and-play）设计，与现有3DGS加速方法正交，可结合Taming-3DGS、FastGS等强基座使用。

### 主要贡献
- 提出一种简单高效的3DGS训练方案，减少训练中活跃高斯数量，降低优化开销并加速训练。
- 设计插件式、与既有3DGS加速方法正交的方案，可与Taming-3DGS和FastGS直接结合。
- 实验显示在1K设置下分别获得1.73x和1.21x的平均加速，在4K设置下分别获得1.74x和1.33x的平均加速；在更具挑战性场景和高分辨率下收益更明显，同时保持有竞争力的重建质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对3DGS训练效率瓶颈提出了新颖且即插即用的训练方案，可直接与多个主流加速方法结合并获得显著加速（最高1.74x），且在高分辨率下优势更明显，对神经场景表示与渲染方向具有实际应用价值。摘要中已明确给出定量加速效果，适合该领域研究者快速了解最新加速思路。

（注：论文出版日期标注为2026年，摘要中未提供额外说明，请读者自行核实该日期合理性。）

</details>

<details>
<summary>Abstract</summary>

A key bottleneck in 3D Gaussian Splatting training is the continual growth of Gaussian primitives, which increases optimization cost and slows convergence, especially at high resolutions. We propose Laplacian Frequency Hierarchies, a simple yet efficient 3DGS scheme that combines Laplacian image decomposition with coarse-to-fine, frequency-staged training. After fitting lower-frequency structure, we archive the corresponding Gaussian field so that subsequent fields can optimize higher-frequency residuals without carrying the full primitive burden, and we compose the rendered components in the image domain via a Laplacian-style reconstruction at inference time. This design reduces the number of active Gaussians during training, thereby lowering optimization overhead and accelerating training. The proposed scheme is plug-and-play and orthogonal to prior 3DGS accelerations: it can be directly combined with strong backbones such as Taming-3DGS and FastGS to improve training speed with competitive reconstruction quality. It achieves average speedups of 1.73x and 1.21x at 1K setting, and 1.74x and 1.33x at 4K setting on Taming-3DGS and FastGS, with larger gains on more challenging scenes and increasingly pronounced benefits at higher resolutions.

</details>

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

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-04 - WorldSculpt: Generating Compositional Worlds from Grounded Videos

**Authors:** Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
**Links:** [abs](https://arxiv.org/abs/2609.05416) - [pdf](https://arxiv.org/pdf/2609.05416)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3DGS, robotics, AR, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WorldSculpt: Generating Compositional Worlds from Grounded Videos
- 作者：Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
- 出版日期：2026-09-04
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.05416

### 一句话总结
本文提出WorldSculpt方法，通过将强单物体3D生成先验扩展为多视角条件路径，仅用单物体数据微调即可生成包含数百个物体、严重遮挡场景的组合式3D网格表示。

### 研究问题
如何从多视角视频中生成由数百个独立物体网格组成的、处于共享世界坐标系下的组合式3D场景表示，尤其是在密集遮挡、单个视角仅能观测到部分几何的复杂场景下准确重建每个物体的完整形状。

### 核心思路/方法
采用"将强单物体3D生成先验适配到多视角观测"的范式：以Pixal3D为基础，扩展多视角条件路径，使模型在生成每个物体时能利用多个带位姿的观测信息进行grounding。关键设计是，模型仅在规范空间的单物体数据上微调，无需场景级训练即可泛化到包含严重遮挡的大规模场景。

### 主要贡献
- 提出WorldSculpt范式，证明复杂数百物体场景可通过适配单物体生成先验实现组合式生成，无需场景级训练。
- 引入UE-MeshyScene基准：包含密集杂乱场景、数百物体、逐物体标注和真值网格，用于评估此类任务。
- 在单物体、受控多物体及UE-MeshyScene上均优于先前方法，且场景越复杂、遮挡越严重，性能优势越明显。
- 展示将现有3DGS世界（如Marble、HY-World 2.0）转换为组合式网格场景的适用性。

### 局限性
摘要未提供足够信息，无法得知方法在实时性、内存开销、物体数量上限、泛化到未见场景类型等方面的局限。

### 阅读优先级
**高**
理由：该工作针对"密集遮挡场景的组合式3D生成"这一具挑战且具实际应用价值的问题，提出无需场景级训练的可扩展范式，并配套新基准，适合从事三维重建、生成模型及具身智能/AR应用的研究者关注。

</details>

<details>
<summary>Abstract</summary>

We study the problem of generating a compositional 3D representation of a cluttered scene containing hundreds of objects. The goal is to represent the scene as a collection of individual object meshes placed in a shared world frame, as required by downstream applications such as gaming, AR/VR, simulation, and robotics. This task is challenging in densely cluttered scenes, where objects heavily occlude one another and each view reveals only a fraction of their geometry. Geometry-based approaches typically reconstruct the scene as a single representation and leave incomplete geometry in occluded regions, while existing compositional methods with generative priors are largely limited to relatively simple scenes. We show that complex scenes with hundreds of objects can instead be generated compositionally by adapting a strong single-object 3D generative prior to multi-view observations. We instantiate this paradigm with Pixal3D, extending it with a multi-view conditioning pathway that grounds object generation in multiple posed observations. Although the model is finetuned entirely on single objects in canonical space, it generalizes to large scenes with severe occlusion without any scene-level training, demonstrating the feasibility and scalability of this paradigm. We further introduce UE-MeshyScene, a photorealistic benchmark of densely cluttered scenes with hundreds of objects, per-object annotations, and ground-truth meshes. Across single-object, controlled multi-object, and UE-MeshyScene evaluations, our method consistently outperforms prior approaches, with larger gains as scene complexity and occlusion increase. Finally, we demonstrate broader applicability by converting generated 3DGS worlds, such as Marble and HY-World 2.0, into compositional mesh scenes.

</details>

#### 2026-09-03 - GIFT: Guided Intermediate Feature Training via Action-Oriented Structural Supervision for Robotic Manipulation

**Authors:** Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Chaoyue Li, Qichao Zhang, Haoran Li, Zhongpu Xia, Ya-Qin Zhang, Shuicheng Yan, Dongbin Zhao
**Links:** [abs](https://arxiv.org/abs/2609.04193) - [pdf](https://arxiv.org/pdf/2609.04193)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GIFT: Guided Intermediate Feature Training via Action-Oriented Structural Supervision for Robotic Manipulation
- 作者：Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Chaoyue Li, Qichao Zhang, Haoran Li, Zhongpu Xia, Ya-Qin Zhang, Shuicheng Yan, Dongbin Zhao
- 出版日期：2026-09-03
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.04193

### 一句话总结
本文提出GIFT框架，通过几何对齐、姿态预测与目标区域重建等结构监督来引导机器人操作的中间特征学习，弥补视觉丰富性与控制效用之间的“动作充分性差距”，并在多个操作任务上显著提升性能。

### 研究问题
机器人视觉语言预训练和世界模型提供的视觉特征虽丰富，但其原生的动作/视觉预测目标可能遗漏关键物理与任务结构，并保留与控制无关的视觉冗余。作者研究能否通过引导中间特征保留三种控制相关结构——几何（运动可行性）、姿态（指令相关实体）、目标（任务相关区域中的指令接地）——来弥合这一“动作充分性差距”。

### 核心思路/方法
提出GIFT（Guided Intermediate Feature Training）框架，一个架构灵活的中间特征学习方法。该方法将上述三种结构转化为训练时约束：
1. 几何对齐（geometry alignment）
2. 姿态预测（affordance prediction）
3. 目标区域重建（goal-region reconstruction）

GIFT被实例化到三种模型中：Vision-Language-Action（VLA）策略、直接动作世界动作模型（WAM）和逆动力学WAM，同时保留各模型原有的动作生成方式。

### 主要贡献
1. 提出动作充分性差距概念，指出视觉特征与控制效用之间的失配问题。
2. 提出GIFT框架，首次以显式结构监督（几何、姿态、目标区域）引导中间特征学习，跨模型架构适用。
3. 在LIBERO-Plus零样本迁移中，GIFT-VLA、GIFT-WAM-Fast、GIFT-WAM-IDM分别达到79.6%、72.6%、87.8%，较基线高出4.6、12.6、5.2个百分点。
4. 在RoboCasa上，三个变体分别达到61.4%、83.6%、82.3%，较对应基线高出12.6、9.0、8.4个百分点。
5. 尤其在与铰接物体任务及高精度真实操作中，在未见视觉与空间扰动下取得显著提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对机器人操作中视觉-控制失配的核心问题，提出了一种不改变模型动作生成方式的轻量特征引导训练方法，且在多种模型架构和任务基准上均获得一致且显著提升。对从事视觉语言动作模型、世界模型与机器人操纵控制的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-language pre-training and predictive world modeling provide robot policies with rich semantic and dynamic visual features, but their native action and visual-prediction objectives may omit critical physical and task structure while retaining control-irrelevant visual redundancy. We call this mismatch between visual richness and control utility the action-sufficiency gap. We investigate whether this gap can be bridged by guiding intermediate features to preserve three control-relevant structure in robotic manipulation: geometry governing motion feasibility, affordance encoding instruction-relevant entities, and goals grounding instructions in task-relevant regions. To this end, we present GIFT (Guided Intermediate Feature Training), an architecture-flexible framework for learning intermediate features that translates these structures into training-time constraints through geometry alignment, affordance prediction, and goal-region reconstruction. We instantiate GIFT in a Vision-Language-Action (VLA) policy, a direct-action World-Action Model (WAM), and an inverse-dynamics WAM while retaining each model's action formulation. Under zero-shot transfer to LIBERO-Plus, GIFT-VLA, GIFT-WAM-Fast, and GIFT-WAM-IDM outperform StarVLA-OFT, Fast-WAM, and Fast-WAM-IDM by 4.6, 12.6, and 5.2 points, reaching 79.6%, 72.6%, and 87.8%, respectively. On RoboCasa, the three GIFT variants reach 61.4%, 83.6%, and 82.3%, outperforming their counterparts by 12.6, 9.0, and 8.4 points, respectively. Together, these results establish learning functionally structured intermediate features as a reusable principle across model-specific action formulations, with especially large gains on articulated-object tasks and high-precision real-world manipulation under unseen visual and spatial perturbations. Project page: https://openphoenix-team.github.io/GIFT-pages.

</details>

#### 2026-09-03 - A hybrid pipeline for dynamic ontology-based semantic mapping

**Authors:** Konstantinos Dimitropoulos, Ioannis Hatzilygeroudis
**Links:** [abs](https://arxiv.org/abs/2609.03891) - [pdf](https://arxiv.org/pdf/2609.03891)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, mapping, localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A hybrid pipeline for dynamic ontology-based semantic mapping
- 作者：Konstantinos Dimitropoulos, Ioannis Hatzilygeroudis
- 出版日期：2026-09-03
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.03891) | [PDF](https://arxiv.org/pdf/2609.03891)

### 一句话总结
本文提出了一种混合语义映射流程，结合外部标定摄像头、单应投影、对象检测与持续追踪，以及本体驱动的动态语义更新，构建机器人的动态语义世界模型。

### 研究问题
如何构建一个能够动态更新、具备上下文理解能力的机器人语义地图，并有效整合本体等先验知识以提升语义映射质量。

### 核心思路/方法
- 采用外部标定摄像头，通过单应投影完成几何映射与定位。
- 结合**对象检测**和**持续对象追踪**，获取实时感知数据。
- 使用**本体驱动**的语义更新机制，持续维护对象实例、空间属性和语义关系。
- 引入**线性回归模型**，对真实世界坐标的估计值进行校正。
- 选择本体作为知识表示形式，因其层级结构、语义表达能力及对动态世界建模的支持。

### 主要贡献
- 提出一个将几何映射、感知、追踪与本体语义更新相结合的混合语义映射流程。
- 引入本体驱动的动态更新，使语义模型可随实时数据持续调整。
- 使用回归模型校正坐标估计，提升映射精度。
- 展示了本体作为动态语义知识表示在机器人语义映射中的适用性。

### 局限性
摘要未提供足够信息。摘要中未提及实验设置、数据集、定量结果或对比基线，因此无法评估系统性能、适用范围及潜在限制。

### 阅读优先级
**中**

理由：该工作聚焦机器人语义映射，属于领域内较活跃方向，但摘要仅描述系统架构而未提供实验证据和定量评估。对于关注语义映射流程设计的读者有价值；若需评估方法有效性或复现对比，则需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Semantic mapping plays a crucial role in the ability of a robot to interact with objects, operate and navigate a complex environment. The most common pipeline for semantic mapping consists of geometric mapping and localization (SLAM), perception, semantic fusion and semantic representation. However, more recent works also integrate a form of prior knowledge in their application, most notably knowledge graphs or semantic scene graphs, to improve contextual understanding of the environment. In this paper, we present a hybrid pipeline for semantic mapping. Our system incorporates an external calibrated camera using homography projection for geometric mapping and localization, combined with object detection, persistent object tracking and ontology driven semantic updates to build a dynamic semantic world model. Linear regression models are also used for correction of the estimated values of real world coordinates. The system continuously updates object instances, spatial properties and semantic relations based on real time sensory data. Ontologies are selected as form of knowledge representation due to their hierarchical structure, semantic expressiveness and support for dynamic world modelling.

</details>

#### 2026-09-03 - MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?

**Authors:** Kohei Sendai, Tatsuya Matsushima, Yusuke Iwasawa
**Links:** [abs](https://arxiv.org/abs/2609.03715) - [pdf](https://arxiv.org/pdf/2609.03715)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?
- 作者：Kohei Sendai, Tatsuya Matsushima, Yusuke Iwasawa
- 出版日期：2026-09-03
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.03715

### 一句话总结
作者提出极小型视觉运动策略MINERVA（0.54M参数），在LIBERO基准上达到95.1%平均成功率，仅比使用7700倍参数的LeRobot π0.5低2.4个百分点，揭示该基准对模型容量的实际需求远低于当前主流超大模型。

### 研究问题
LIBERO操作基准实际需要的最小模型容量是多少？当前数十亿参数的VLA模型是否对该基准过度参数化？

### 核心思路/方法
- 设计MINERVA策略族（刻意紧凑的视觉运动策略），从0.25M到1M参数范围内扫描，衡量任务特定容量下限。
- 进行广泛的架构、训练和推理扫描，评估各因素（如action-chunk长度、视觉容量、流匹配vs直接L1回归）对性能的影响。
- 使用任务ID置换探针测试指令条件化是否只是记忆任务映射。
- 在LIBERO标准四套件（2000次rollout）、LIBERO-90（89个任务）和LIBERO-Plus扰动场景下评估。

### 主要贡献
- 首次实证估计LIBERO基准的任务特定容量下限：~0.25M以下性能崩溃，~1M处饱和。
- 0.54M参数策略达到95.1%平均成功率，与7,700倍参数的π0.5差距仅2.4点。
- 揭示action-chunk长度和视觉容量是唯二影响超出训练种子波动（±1点）的因素；流匹配相比L1回归无优势，且回归GPU速度快达3.8倍。
- 任务ID置换探针表明标准LIBERO指令条件化主要是在选择已记忆任务。
- 0.54M策略在笔记本电脑CPU上每chunk重规划仅5–9 ms，比SmolVLA快113倍、比π0.5快1,400倍。

### 局限性
- LIBERO-Plus扰动下性能降至46–56%，对光度扰动鲁棒性近乎为零，说明所测出的容量下限仅在标准LIBERO分布内成立，泛化性受限。
- 摘要未提供关于模型在真实机器人上部署的结果、训练数据规模、具体架构细节（如视觉编码器类型）等信息。
- 摘要未提及对更大规模模型蒸馏或容量自适应设计的实现方案。
- 摘要未提供其他基线（除LeRobot π0.5和SmolVLA外）的对比细节。

### 阅读优先级
**高**  
理由：该研究质疑当前VLA模型规模的必要性，提供LIBERO基准首个容量下限实证，结果极具实用价值（CPU实时推理、千倍参数压缩），对机器人策略设计和模型蒸馏方向有直接参考意义，且实验规模充分（多套件、多场景、多次seeds），结论可信度较高。

</details>

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models with billions of parameters now dominate the LIBERO manipulation benchmark, but the model capacity actually required by the benchmark remains unclear. We introduce MINERVA (MINimal Efficient Robotic Vision-Action policy), a family of deliberately compact visuomotor policies designed to measure this task-specific capacity floor. A 0.54M-parameter policy achieves 95.1% average success over 2,000 rollouts on the four standard LIBERO suites, only 2.4 points below the reported LeRobot $π_{0.5}$ result despite using 7,700$\times$ fewer parameters. Performance saturates near 1M parameters and collapses below 0.25M. Across broad architectural, training, and inference sweeps, only action-chunk length and vision capacity consistently exceed a $\pm$1-point training-seed band. Flow matching provides no detectable advantage over direct L1 regression across three seeds, while regression is up to 3.8$\times$ faster on GPU. A task-ID permutation probe shows that standard LIBERO instruction conditioning primarily selects among memorized tasks: changing only the task-ID mapping reduces success to near chance. The same recipe achieves 94.6% success across 89 LIBERO-90 tasks, while LIBERO-Plus perturbations reduce performance to 46--56%, with near-zero robustness to photometric shifts. The 0.54M policy replans every control step in 5--9 ms per chunk on a laptop CPU, 113$\times$ faster than SmolVLA and 1,400$\times$ faster than $π_{0.5}$, without a GPU. These results establish a first empirical estimate of LIBERO's task-specific capacity floor and motivate capacity-aware design and distillation for deployment-efficient robot policies.

</details>

#### 2026-09-03 - ReRoom: Blending Virtual and Physical Contexts for In Situ Room Planning in Mixed Reality

**Authors:** Hongliang Yang, Yanjing Xu, Anhang Zhang, Hui Ye, Pengfei Xu
**Links:** [abs](https://arxiv.org/abs/2609.03596) - [pdf](https://arxiv.org/pdf/2609.03596)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, VR, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReRoom: Blending Virtual and Physical Contexts for In Situ Room Planning in Mixed Reality
- 作者：Hongliang Yang, Yanjing Xu, Anhang Zhang, Hui Ye, Pengfei Xu
- 出版日期：2026年9月3日
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.03596

### 一句话总结
ReRoom 是一个混合现实系统，通过将虚拟房间代理与真实房间空间对齐，支持用户在物理环境中进行原位房间布局设计、评估与迭代。

### 研究问题
真实家庭空间规划本质上是一个原位创作过程，但现有方法要么将布局编辑与物理房间分离，要么对在真实空间中原位评估和细化整体房间布局方案的支持有限。ReRoom 旨在解决如何在混合现实中实现高质量、可交互的原位房间布局规划问题。

### 核心思路/方法
ReRoom 提出了一种混合现实原位布局编辑系统，其核心思路包括：
1. 通过一个与目标房间空间对齐的虚拟房间代理，呈现共享布局状态，使交互和布局生成始终锚定在物理环境上下文中。
2. 用户可通过直接操作或语言输入来细化当前布局提案，系统保留用户已接受的摆放结果，使每次生成的更新都能延续同一个不断演进的设计过程。
3. 采用一种技能引导的布局智能体，该智能体将综合既有室内设计指南提炼出的三条原则，转化为可操作的房间布局设计技能，并基于扫描房间的归一化表示和可复用的几何检查来落地这些原则。

### 主要贡献
- 提出 ReRoom 混合现实系统，支持在真实房间环境中进行原位布局创作与迭代。
- 设计了一种技能引导的布局智能体，将室内设计指导原则形式化并用于真实房间布局生成。
- 实验表明 ReRoom 能针对非矩形房间生成高质量布局，且其原位工作流相比等效的离站 VR 工作流能改善房间规划体验。
- 论文接受后将公开代码。

### 局限性
摘要未提供足够信息，未明确提及系统在特定场景下的失败案例、交互复杂度上限、用户学习成本或计算资源需求等局限性。

### 阅读优先级
**中**。理由：本论文结合混合现实交互与自动化布局生成，聚焦原位房间规划这一具体场景，对开展 MR 交互设计、室内布局生成或人机协同设计研究的读者具有参考价值；评价实验仅提到“优于离站 VR”，未给出具体量化指标摘要，因此若不在相关方向的读者可暂缓精读。

</details>

<details>
<summary>Abstract</summary>

Planning a real domestic space is an in situ authoring process: users evaluate candidate layouts at true scale, refine their intent, and carry accepted decisions into later iterations. Existing approaches either separate layout editing from the physical room or provide limited support for evaluating and refining whole-room proposals in situ. We present ReRoom, a mixed-reality system for in situ room-layout authoring. ReRoom presents a shared layout state through a virtual room proxy spatially registered to the target room, allowing interaction and layout generation to remain grounded in the physical context. Users refine the current proposal through direct manipulation or language and preserve accepted placements, allowing each generated update to continue the same evolving design. To balance layout quality with generation efficiency, ReRoom uses a skill-guided layout agent whose room-layout design skill operationalizes three principles that we formulate by synthesizing established interior-design guidance for real-room layout generation. The skill grounds these principles in a normalized representation of the scanned room and reusable geometric checks. Evaluations show that ReRoom produces high-quality layouts for non-rectangular rooms, while its in situ workflow improves the room-planning experience over an otherwise equivalent off-site VR workflow. Code will be released upon acceptance of the paper.

</details>

#### 2026-09-02 - Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports

**Authors:** Yuqiao Xu, Erman Ayday
**Links:** [abs](https://arxiv.org/abs/2609.03055) - [pdf](https://arxiv.org/pdf/2609.03055)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot perception

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports
- 作者：Yuqiao Xu, Erman Ayday
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.03055

### 一句话总结
本文提出任务限定感知导出框架TFPD，通过系统性评估发现机器人在隐私风险与任务效用之间不存在单一的“少看即安全”规律，不同表示方式在任务表现相同的情况下隐私泄露程度差异巨大。

### 研究问题
家庭机器人在将原始感知数据保留本地、仅导出结构化表示给下游规划器/云服务/日志/学习管道时，这些任务限定的感知导出仍可能通过语义、几何、空间结构及任务目标泄露家庭隐私；核心研究问题是如何系统衡量并缓解“任务限定”导出中的残余隐私风险，并检验更抽象或更少的感知信息是否必然带来更安全的隐私保护。

### 核心思路/方法
提出 Task-Functional Perception Distillation (TFPD) 框架，将丰富的感知保留在本地，同时对下游导出按照任务效用、直接暴露程度、和多种残余推断风险进行多维度刻画。实验采用120个AI2-THOR场景，划分场景不相交的训练/验证/测试集，使用冻结的攻击者选择和表示感知的留出攻击，评估导航、碰撞检测和目标目标执行三个任务。此外用ProcTHOR数据集进行复现，检验结论的稳健性。

### 主要贡献
- 揭示“字段移除或更强抽象不产生普遍性隐私排序”的现象，即减少感知信息并不自动带来更高隐私安全。
- 多个导航导出在任务表现完全一致（成功率为1.000，平均路径比为0.898）时，表示级链接性可在0.532至0.970之间大幅波动，隐私性能不能由任务效用推断。
- 将显式目标标签替换为目标区域使目标类别macro-F1从1.000降至0.077，同时保持任务成功率达0.995，验证了目标层面的隐私与效用可分离性。
- 几何粗化可使物体类别macro-F1从0.704降至0.556，但伴随可测的碰撞效用代价。
- ProcTHOR复现保持了任务等价性与隐私不等价性的核心发现，但改变了归一化与拓扑导出的相对排序，提示隐私评定需针对完整公开表示做任务特定、多风险评价。

### 局限性
摘要中未提供足够的局限性信息，例如计算开销、真实物理机器人场景验证、更广任务类型覆盖或对攻击者能力更细粒度的假设等均未提及。

### 阅读优先级
**中**。理由：该研究面向具身机器人感知导出的隐私评估，问题重要且方法框架（TFPD）具有参考价值，实验规模（120个场景）有限，但结论具备启发意义；若关注机器人隐私或具身AI安全方向，值得阅读；若属于其他方向，可暂缓。

</details>

<details>
<summary>Abstract</summary>

Domestic robots rely on rich perception to operate in private homes, but privacy risk persists even when raw sensor data remain local. Structured representations exported to downstream planners, cloud services, logs, or learning pipelines can still reveal household information through semantics, geometry, spatial structure, and task targets. We introduce Task-Functional Perception Distillation (TFPD), a task-scoped representation-export framework that keeps rich perception local and profiles downstream exports according to task utility, direct exposure, and multiple residual inference risks. Using 120 AI2-THOR scenes with scene-disjoint train/validation/test splits, frozen attacker selection, and representation-aware held-out attacks, we evaluate navigation, collision checking, and object-goal execution. Three navigation exports achieve identical success (1.000) and mean path ratio (0.898), yet representation-level linkability ranges from 0.532 to 0.970. Replacing an explicit target label with a target region reduces target-category macro-F1 from 1.000 to 0.077 while preserving success at 0.995, while geometric coarsening reduces object-category macro-F1 from 0.704 to 0.556 at a measurable collision-utility cost. A ProcTHOR replication preserves the navigation task-equivalence/privacy-inequivalence finding while changing the relative ordering of normalized and topological exports. These results show that neither field removal nor stronger abstraction induces a universal privacy ordering and motivate task-specific, multi-risk evaluation of the complete public representation.

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
