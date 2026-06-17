# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：46
- 分类分布：
  - Neural Scene Representations & Rendering: 16
  - 3D Reconstruction & Multi-view Geometry: 14
  - Embodied / Robotics / AR Applications: 12
  - Dynamic / 4D Reconstruction: 2
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

好的，这是基于您提供的论文列表生成的今日科研趋势综合分析。

#### 今日主要趋势

1.  **高斯泼溅（Gaussian Splatting）从渲染工具向核心架构范式的演进**：3D高斯泼溅（3DGS）已不再仅仅是一种新颖的渲染技术。本日论文显示，它正被系统性地改造为一种通用的、可学习的连续场景表示基元，深入渗透到多个子领域。**AIGS-Net**和**GLFS**将其应用于低光照增强中的光照场建模，**GSPan**将其用于遥感图像融合中的连续残差细节表示，**MoonSplat**和**GASE**则将其作为在线重建和自动化仿真环境构建的核心。这与“点”表示的传统用法不同，这些工作强调高斯元的“场”属性和可优化性，预示着一个“高斯元+Task-x”的研究范式正在形成。

2.  **从“感知”到“预测”的世界模型，强调几何一致性与解耦**：世界模型的研究重心正在从过去的2D视频预测，转向具有几何意义的3D/4D动态预测。**FR3D**明确将场景3D演化与智能体自运动解耦，旨在实现未来动态3D重建。**OmniDrive**和**Qwen-RobotWorld**则聚焦于驾驶或机器人场景，利用大语言模型（LLM）或大规模数据，生成受控的未来视觉轨迹。这些工作的共同核心是追求预测结果在3D空间中的物理一致性和可控性，而非仅仅2D视觉上的“像”。

3.  **机器人学习的数据瓶颈催生“自动化数据工厂”**：解决机器人学习中“数据匮乏”和“Sim-to-Real Gap”问题的方案，正从简单的物理仿真，转向高度自动化的、结合3D重建与生成式模型的“数据工厂”。**AnnotateAnything**为仅有几何的3D资产自动生成语义和物理标注；**GASE**通过全景相机快速扫描并自动重建高保真仿真场景；**R2RDreamer**则直接在真实演示数据上通过3D编辑和2D视频补全进行数据增强。这标志着机器人领域正在构建从“原始数据采集”到“高质量、可泛化训练数据”的端到端自动化流水线。

4.  **几何先验与语义/生成模型深度耦合**：论文普遍认识到，纯数据驱动的神经网络缺乏物理规则和3D几何常识。因此，将显式或隐式的几何先验融入到以视觉Transformer（ViT）、扩散模型或大语言模型（LLM）为代表的现代生成式架构中，成为一个显著趋势。例如，**GLFS**将高斯光场物理先验注入ViT的自注意力机制，**GAM**直接利用预训练几何基础模型（GFM）作为机器人的统一感知和动作骨干，**BRDFusion**则将物理渲染（PBR）与生成式模型结合以取长补短。

5.  **特定应用场景下的轻量化与鲁棒性追求**：除了通用方法，针对特定场景的极致优化也成为亮点。**SPARK**专为自动驾驶赛车的低延迟需求设计，利用固定几何先验实现高效高性能；**RICH-SLAM**针对雷达数据的稀疏性和噪声，设计了专用的增量建图和粒子滤波方案，以提升鲁棒性。这些工作表明，在追求通用能力的同时，针对边缘设备、恶劣环境等特定约束的高效、鲁棒解决方案同样重要。

---

#### 技术路线观察

| 方向 | 技术侧重点 | 代表性论文 |
| :--- | :--- | :--- |
| **几何基础模型 (GFM)** | 将深度学习模型（如ViT）显式设计为几何推理的统一骨干，强调几何先验的直接利用，而非从图像特征中隐式学习。 | **GAM** (直接复用于策略学习)、**GLFS** (物理先验注入Transformer) |
| **3D/4D 重建** | 从静态场景重建转向动态未来预测；从全局SfM/NeRF转向局部、在线、流式处理（3DGS）；强调解耦（自运动vs世界运动）和几何一致性。 | **FR3D** (未来动态预测)、**MoonSplat** (在线单目GS+Sim(3)优化)、**RICH-SLAM** (雷达SLAM) |
| **神经场景表示** | 高斯泼溅(3DGS)成为主流，其应用从渲染扩展到作为核心可学习的连续“场”（如光照场、残差细节场），并与特定任务（如图像增强、全色锐化）的物理模型结合。 | **AIGS-Net**、**GSPan**、**Edit3DGS** |
| **机器人/AR应用** | 核心是解决数据生成和Sim-to-Real Gap。技术路线包括：**1) 自动化标注与重建**；**2) 基于真实数据的数据增强**；**3) 利用LLM/生成模型构建世界模型用于策略预训练或规划**。 | **AnnotateAnything**、**GASE**、**R2RDreamer**、**TerraTransfer**、**Qwen-RobotWorld** |

---

#### 值得优先阅读的论文

1.  **《MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization》**
    - **理由**：这篇文章是3DGS在线重建方向的标杆性工作。它直击现有在线GS方法的两个痛点（相机追踪不稳定、大场景效率低），并提出了一个优雅且有效的解决方案（Sim(3)全局优化 + 体素化GS + 颜色残差学习）。其性能达到SOTA且具备实时性，对机器人导航、AR等应用具有很高的直接参考价值。

2.  **《Geometric Action Model for Robot Policy Learning》**
    - **理由**：这篇文章代表了一个极具潜力的研究新方向：直接复用无处不在的几何基础模型（如DINOv2）作为机器人策略的“操作系统”。它通过最小的架构修改，将强大的3D几何先验注入到语言条件策略中，实验证明了其优越性。这对于理解“视觉基础模型如何赋能具身智能”具有启发性。

3.  **《Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation》**
    - **理由**：这是一份大规模、系统性的技术报告，代表了“LLM+视频生成世界模型”在具身智能领域的最新前沿。它提出了一个统一的问题设定（语言条件未来轨迹预测）和相关的知识库（EWK），并在多个基准上取得了领先结果。阅读此文有助于把握该领域的最新“游戏规则”和性能天花板。

4.  **《FR3D: Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion》**
    - **理由**：该工作开创性地提出了“未来动态3D重建”这一任务，并解决了长期存在的自运动-世界运动混淆问题。其核心思想（解耦、持久3D表示）对于构建更具物理一致性的世界模型至关重要。它连接了动态3D重建和预测这两个重要领域，前瞻性很强。

5.  **《R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies》**
    - **理由**：这篇文章解决了机器人学习中的一个实际且重要的问题——空间泛化。它提出了一种“先编辑3D，再补全2D”的巧妙数据增强流水线，完美避开了Sim-to-Real Gap，且生成的增强数据直接适用于主流的2D RGB策略，实用价值高。其两阶段思路（轻量3D编辑 + 2D视频补全）具有很强的工程范式和推广潜力。

---

#### 可能的研究机会

1.  **“高斯元+X”的通用任务建模框架**：AIGS-Net、GSPan等成功将GS用于特定任务（光照、遥感）。一个开放的方向是：能否设计一个通用的、与任务无关的“高斯元表示核心”，只需更换解码头和损失函数，就能应用于图像增强、超分、去噪、深度估计等多种低级视觉任务？这类似于将UNet或ViT作为骨干，但骨干本身是可学习的“光场/几何场”。

2.  **在线/流式4D高斯泼溅的未来预测**：FR3D融合了GS

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-17T12:02:08-04:00
**Total number of papers:** 46
**Number of papers added in the latest update:** 16
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

### 2026-06

#### 2026-06-15 - SurroundNEXO: Ego-Centric Metric Bridging for Spatially Consistent Geometry in Autonomous Driving

**Authors:** Shuai Yuan, Runxi Tang, Yuzhou Ji, Fudong Ge, Hanshi Wang, Yifei Wang, Xianming Zeng, Jianyun Xu, Xingliang Liu, Yanfeng Wang, Zhipeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.16960) - [pdf](https://arxiv.org/pdf/2606.16960)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth prediction, metric depth, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SurroundNEXO: Ego-Centric Metric Bridging for Spatially Consistent Geometry in Autonomous Driving
- 作者：Shuai Yuan, Runxi Tang, Yuzhou Ji, Fudong Ge, Hanshi Wang, Yifei Wang, Xianming Zeng, Jianyun Xu, Xingliang Liu, Yanfeng Wang, Zhipeng Zhang
- 出版日期：2026-06-15T17:00:32Z
- 分类：Geometry Foundation Models (主要); Embodied / Robotics / AR Applications (次要)
- 链接：摘要: https://arxiv.org/abs/2606.16960, PDF: https://arxiv.org/pdf/2606.16960

### 一句话总结
SurroundNEXO通过利用自车视角几何信息（Ego-Ray位置编码）和稀疏LiDAR度量锚点，解决了自动驾驶中多相机低重叠场景下的深度预测与空间一致性问题，相比现有方法在多项指标上取得了显著提升。

### 研究问题
如何在不依赖密集视觉对应的情况下，实现自动驾驶多相机（低重叠环视系统）的可靠度量级深度预测，以提升三维空间一致性？

### 核心思路/方法
1.  **Ego-Ray位置编码**：将图像令牌赋予全局可比较的自车视角方向，奠定跨视图几何推理基础，而非进行早期全局特征融合。
2.  **稀疏度量锚点**：使用稀疏LiDAR测量值作为度量锚点，向深度预测中传播绝对尺度信息。
3.  **渐进式特征交互**：特征交互按照从视图内部建模、到分解的时空推理、再到全局集成的顺序逐步扩展。

### 主要贡献
- 提出了SurroundNEXO，一种面向低重叠多相机系统的度量深度框架，以自车几何替代密集视觉对应。
- 在NuScenes、Waymo、DDAD三个自动驾驶基准上，单视图误差降低33.2%，跨视图一致性提升10.5%，度量重建质量提升25.6%。
- 在极稀疏深度提示下保持鲁棒性，并对未见过的相机布局展现出强大的零样本泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作明确提出并解决了自动驾驶感知域中环视相机低重叠带来的实际难题，并基于摘要报告了在NuScenes、Waymo、DDAD等主流数据集上全面且显著的性能提升，同时方法设计新颖（引入Ego-Ray位置编码和渐进式交互）。对于从事自动驾驶环境感知、多视图几何或度量深度估计的研究者而言，具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Modern autonomous driving depends on accurate metric 3D understanding for perception, reconstruction, and planning, which in turn requires reliable multi-camera depth prediction. However, the outward-facing nature of vehicle-mounted surround-view camera rigs inherently limits visual overlap across views, challenging the correspondence-based assumptions that underpin conventional multi-view geometry. To bridge this gap, we present SurroundNEXO, named after the Spanish word nexo for a geometric link, a low-overlap multi-camera metric depth framework that grounds cross-view reasoning in ego-centric geometry rather than dense visual correspondences. Instead of directly enforcing early global fusion, SurroundNEXO first assigns image tokens globally comparable ego-frame viewing directions through Ego-Ray Positional Encoding, then uses sparse LiDAR measurements as metric anchors to propagate absolute scale cues, and finally expands feature interaction progressively from view-local modeling to decomposed spatio-temporal reasoning and global integration. This design enables metric-scale depth prediction with improved spatial consistency across weakly overlapping cameras. Across low-overlap autonomous driving benchmarks, including NuScenes, Waymo and DDAD, SurroundNEXO reduces single-view error by 33.2%, improves cross-view consistency by 10.5%, and enhances metric reconstruction quality by 25.6% compared with SOTA methods. It further remains robust under extremely sparse depth prompts and exhibits strong zero-shot generalization to unseen camera layouts.

</details>

#### 2026-06-15 - Uncertainty Quality of VGGT: An Analysis on the DTU Benchmark Dataset

**Authors:** Markus Hillemann, Robert Langendörfer, Steven Landgraf, Markus Ulrich
**Links:** [abs](https://arxiv.org/abs/2606.16479) - [pdf](https://arxiv.org/pdf/2606.16479)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** visual geometry grounded transformer, VGGT, DUSt3R, MASt3R, 3D reconstruction, bundle adjustment, photogrammetry, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Uncertainty Quality of VGGT: An Analysis on the DTU Benchmark Dataset
- 作者：Markus Hillemann, Robert Langendörfer, Steven Landgraf, Markus Ulrich
- 出版日期：2026-06-15T09:49:00Z
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（副分类）
- 链接：https://arxiv.org/abs/2606.16479

### 一句话总结
本文分析了VGGT模型在DTU基准数据集上输出的不确定性质量，发现存在一个有效的置信度阈值可用于过滤原始输出，并指出提升不确定性质量对改善VGGT三维重建精度有显著潜力。

### 研究问题
如何评估VGGT模型所预测的不确定性质量？具体包括：是否存在可用的置信度阈值来过滤VGGT的原始输出？不确定性质量的提升能否提高三维重建的准确性？

### 核心思路/方法
基于DTU基准数据集，对VGGT模型输出的不确定性进行定量分析，通过设定置信度阈值对原始输出进行过滤，并评估该过滤操作对三维重建精度的影响。

### 主要贡献
1. 识别出VGGT在DTU数据集上预测不确定性时存在一个有效的置信度阈值，可用于过滤其原始输出。
2. 通过实验证明，提升不确定性质量（例如通过该阈值过滤）有望显著提高VGGT的三维重建精度。

### 局限性
摘要未提供足够信息。具体局限性（如分析仅针对DTU数据集、未讨论其他场景或基线对比等）超出摘要范围。

### 阅读优先级
**高**。理由：VGGT因获得CVPR-2025最佳论文奖而广受关注，本文聚焦于其不确定性质量这一关键但常被忽视的方面，对可靠使用该模型进行三维重建具有重要意义。分析结果可直接指导实际应用中的输出后处理，且发表于2026年（当前时间点之后），属于前沿研究。

</details>

<details>
<summary>Abstract</summary>

Visual Geometry Grounded Transformer (VGGT) has already attracted a great deal of attention in a short period of time, not least due to the Best Paper Award at CVPR-2025. Similar to DUSt3R and MASt3R, VGGT aims to bring about a paradigm shift by replacing established methods like bundle adjustment and feature matching with a simple, unified, feed-forward neural network that predicts camera poses, depth maps, and dense 3D structure directly from multiple images of a scene in a few seconds. A key aspect is its ability to process an arbitrary number of views consistently in a single forward pass without any post-processing or iterative optimization. For photogrammetry, this opens new possibilities for real-time, scalable, and accessible 3D reconstruction. In this context, not only high reconstruction accuracy but also high-quality uncertainty estimates are crucial, as they foster trust and enable robust quality assurance. This paper therefore investigates the quality of VGGT's uncertainty predictions. The analysis identifies an effective confidence threshold for filtering VGGT's raw output and demonstrates that enhancing uncertainty quality holds strong potential for improving the accuracy of its 3D reconstructions.

</details>

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-16 - Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion

**Authors:** Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab, Federico Tombari, Stefano Gasperini
**Links:** [abs](https://arxiv.org/abs/2606.18250) - [pdf](https://arxiv.org/pdf/2606.18250)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** dynamic 3D, 3D reconstruction, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion
- 作者：Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab, Federico Tombari, Stefano Gasperini
- 出版日期：2026-06-16
- 分类：Dynamic / 4D Reconstruction, 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.18250

### 一句话总结
本文提出FR3D，一种将场景3D演化与智能体运动解耦的世界模型，用于从单目观测进行未来动态3D重建，可在2秒后保持几何一致性。

### 研究问题
如何从单目视频预测动态环境的未来演化，同时解决2D视频合成中因自运动与世界运动混淆导致的物体变形或消失等物理不一致性问题，并实现长期几何一致性。

### 核心思路/方法
1. **解耦建模**：显式地将场景的3D演化与智能体轨迹分离，将推断的自我运动作为潜在的动作代理，从而消除自运动与世界运动之间的歧义。
2. **教师-学生蒸馏**：利用现成基础模型的空间“常识”（如深度、尺寸等）进行蒸馏，以增强模型在未见场景上的零样本泛化能力。
3. **持久3D潜在表示**：维护一个持续更新的潜在3D表示，用于预测未来动态场景，而非仅依赖逐帧图像特征。

### 主要贡献
- 提出FR3D，首个实现未来动态3D重建（即使2秒后）并保持几何一致性的世界模型。
- 通过解耦自我运动和场景运动，解决了传统基于图像特征的预测方法中存在的物理不一致问题。
- 引入教师-学生蒸馏策略，利用基础模型的空间知识提升零样本泛化性能。
- 在多个数据集上的实验证明了该方法对未来动态3D重建的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该工作聚焦于动态3D重建与未来预测，方法新颖（解耦自运动与世界运动），对自主智能体相关研究有参考价值。但摘要未提供量化性能数据或与现有方法的具体对比，读者需进一步阅读论文正文以评估实际效果。若研究领域为3D/4D重建或具身智能，则优先级可提升至高。

</details>

<details>
<summary>Abstract</summary>

Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. Unlike prior works that treat the world as a sequence of image-based features, FR3D explicitly decouples the 3D evolution of the scene from the agent's trajectory, treating the inferred ego-motion as a latent proxy for action. This disentanglement resolves the ambiguities between self-motion and world-motion, ensuring geometric consistency into the future. Furthermore, we introduce a teacher-student distillation strategy that leverages the spatial "common sense" of off-the-shelf foundation models, leading to robust zero-shot generalization. Extensive experiments demonstrate FR3D's strong performance for future dynamic 3D reconstruction from monocular observations across multiple datasets, even 2 seconds into the future. Project page: https://fr3d-wm.github.io.

</details>

#### 2026-06-15 - Renderable Partial Representations for Dynamic Gaussian Splatting under Incomplete Delivery

**Authors:** Faruk Alpay, Levent Sarioglu, Yaser Hadri
**Links:** [abs](https://arxiv.org/abs/2606.17212) - [pdf](https://arxiv.org/pdf/2606.17212)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, NeRF, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Renderable Partial Representations for Dynamic Gaussian Splatting under Incomplete Delivery
- 作者：Faruk Alpay, Levent Sarioglu, Yaser Hadri
- 出版日期：2026-06-15
- 分类：动态/4D重建；神经场景表示与渲染
- 链接：摘要: https://arxiv.org/abs/2606.17212, PDF: https://arxiv.org/pdf/2606.17212

### 一句话总结
本文提出一种面向动态高斯泼溅（Dynamic Gaussian Splatting）的渲染可用的部分表示方法，通过优化图像空间中的退化度，使不完整传输状态下的场景仍可直接渲染，并以反事实效用层指导自适应调度。

### 研究问题
在动态高斯压缩中，交互式渲染常面临部分表示：部分时空区域存在、部分缺失，且后期精炼无法影响已显示帧。本文研究如何在网络传输不完整时，使高斯表示状态仍然直接可渲染，并优化其图像空间退化。

### 核心思路/方法
1. 将高斯图元组织成可独立寻址的时空聚类，包含一个基础层和三个精炼层。
2. 训练时采样部分依赖图，在一个GPU批次中渲染多个反事实状态。
3. 优化目标包括：期望失真、尾部失真、时间不一致性、码率和前缀回归。
4. 引入反事实效用层，测量每个完成组在不同接收方上下文中的边际渲染贡献。
5. 具体传输实现基于MTU限制的熵编码块、截止时间感知调度和接收方依赖闭包。

### 主要贡献
1. 提出一种动态高斯表示，其不完整交付状态仍可渲染，且退化在图像空间优化。
2. 建立反事实效用层，定量评估各完成组的渲染贡献，超越了标称精炼层顺序。
3. 实验证明：在多个动态场景（D-NeRF、HyperNeRF）中，精细精炼层的边际效用为负；基于效用的顺序可在匹配字节预算下消除PSNR回归（broom2）或提升PSNR达3.03 dB（chicken）。

### 局限性
摘要未提供足够信息关于方法的计算开销、实时性能、对极端缺失率的鲁棒性或与其他动态高斯压缩方法的系统比较。

### 阅读优先级：高
**理由**：该工作直接针对交互式渲染中动态高斯表示的传输与渲染退化问题，提出反事实效用这一新颖思路，实验验证了标称层顺序的不足并带来显著性能提升（如3.03 dB）。方法紧密结合网络交付的分布视角，为动态场景的实时渲染优化提供重要方向。

</details>

<details>
<summary>Abstract</summary>

Dynamic Gaussian compression is normally optimized for complete files or complete progressive prefixes, but interactive rendering encounters partial representations: some spatiotemporal regions are present, others missing, and late refinements cannot affect the displayed frame. We study dynamic Gaussian representations whose incomplete delivery states remain directly renderable and whose degradation is optimized in image space. Gaussian primitives are organized into independently addressable spatiotemporal clusters with a base level and three refinements; training samples partial dependency graphs, renders many counterfactual states in one GPU batch, and minimizes expected distortion, tail distortion, temporal inconsistency, rate, and prefix regressions. A counterfactual utility layer measures the marginal render contribution of each completion group across valid receiver contexts. The same graph admits a concrete delivery realization with MTU-bounded entropy-coded chunks, deadline-aware scheduling, and receiver-side dependency closure. On held-out views, the finest refinement has negative mean marginal utility in 3/32 D-NeRF bouncingballs, 49/64 HyperNeRF broom2, and 28/64 HyperNeRF chicken clusters; its lower-tail utility is negative in 21/32, 61/64, and 42/64 clusters, respectively. On broom2, render-utility ordering removes both PSNR regressions produced by nominal layer order at matched byte budgets; on chicken, utilities measured on disjoint training cameras improve held-out PSNR by 3.03 dB at the lowest matched budget. These scoped results show why nominal refinement order cannot substitute for render-conditioned utility: the formulation treats network delivery as a distribution over renderable scene states rather than as an external wrapper around a graphics codec.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

#### 2026-06-16 - Neural Tree Reconstruction for the Open Forest Observatory

**Authors:** Marissa Ramirez de Chanlatte, Arjun Rewari, Trevor Darrell, Derek J. N. Young
**Links:** [abs](https://arxiv.org/abs/2606.18153) - [pdf](https://arxiv.org/pdf/2606.18153)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, NeRF, radiance, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Neural Tree Reconstruction for the Open Forest Observatory  
- 作者：Marissa Ramirez de Chanlatte, Arjun Rewari, Trevor Darrell, Derek J. N. Young  
- 出版日期：2026-06-16  
- 分类：3D 重建与多视角几何  
- 链接：摘要：https://arxiv.org/abs/2606.18153；PDF：https://arxiv.org/pdf/2606.18153  

### 一句话总结
本文探索将神经辐射场（NeRF）引入开放森林观测站（OFO）数据集，以提升森林三维地图的重建质量，并指出其对气候应用的重要性。

### 研究问题
如何克服现有基于运动恢复结构（SfM）方法在森林三维重建中产生的伪影、细节缺失及林下可见性受限等问题，从而提升 OFO 数据集的质量。

### 核心思路/方法
利用神经辐射场（NeRF）等先进三维重建技术替代经典 SfM 方法，因其能够产生更高质量、更鲁棒的重建结果，并对稀疏视图和先验知识有更好的支持。

### 主要贡献
- 提出了将 NeRF 整合到 OFO 数据集中的探索性思路。
- 概述了未来支持更先进三维视觉模型的工作方向。
- 强调了高质量三维重建对于林业应用（如再造林优先、野火隐患减少、碳汇监测）的重要性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
低。理由：本文目前仅停留在“探索思路”和“未来工作展望”阶段，未给出具体实验或定量结果，缺乏实质性技术贡献。对于关注成熟方法的读者而言，参考价值有限。

</details>

<details>
<summary>Abstract</summary>

The Open Forest Observatory (OFO) is a collaboration across universities and other partners to make low-cost forest mapping accessible to ecologists, land managers, and the general public. The OFO is building both a database of geospatial forest data as well as open-source methods and tools for forest mapping by uncrewed aerial vehicle. Such data are useful for a variety of climate applications including prioritizing reforestation efforts, informing wildfire hazard reduction, and monitoring carbon sequestration. In the current iteration of the OFO's forest map database, 3D tree maps are created using classical structure-from-motion techniques. This approach is prone to artifacts, lacks detail, and has particular difficulty on the forest floor where the input data (overhead imagery) has limited visibility. These reconstruction errors can potentially propagate to the downstream scientific tasks (e.g. a wildfire simulation.) Advances in 3D reconstruction, including methods like Neural Radiance Fields (NeRF), produce higher quality results that are more robust to sparse views and support data-driven priors. We explore ways to incorporate NeRFs into the OFO dataset, outline future work to support even more state-of-the-art 3D vision models, and describe the importance of high-quality 3D reconstructions for forestry applications.

</details>

#### 2026-06-16 - SPARK: Low Latency Single-Camera 3D Pose Estimation for Autonomous Racing using Keypoints

**Authors:** Dominic Ebner, Markus Lienkamp
**Links:** [abs](https://arxiv.org/abs/2606.17936) - [pdf](https://arxiv.org/pdf/2606.17936)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SPARK: Low Latency Single-Camera 3D Pose Estimation for Autonomous Racing using Keypoints
- 作者：Dominic Ebner, Markus Lienkamp
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要URL: https://arxiv.org/abs/2606.17936；PDF: https://arxiv.org/pdf/2606.17936

### 一句话总结
本文提出SPARK，一种基于关键点检测的单目相机3D位姿估计算法，专为自动驾驶赛车设计，在实现高精度远程检测的同时保持低延迟和低资源消耗。

### 研究问题
如何在自动驾驶赛车场景中，利用单目相机快速、准确地检测其他非合作参与者的3D位姿，以支持安全、无碰撞的轨迹规划，并克服LiDAR方法延迟高、边缘部署困难的问题。

### 核心思路/方法
- 采用YOLO模型进行关键点检测，利用自动驾驶赛车环境中固定的几何结构（如赛车尺寸一致性）来提升检测精度与速度。
- 整体框架为端到端单目3D位姿估计，旨在降低延迟并减少计算资源占用。
- 在真实世界的自动驾驶赛车数据上评估，并与当前最先进的LiDAR和相机检测算法进行对比。

### 主要贡献
- 提出SPARK算法，在远程检测中达到高精度，性能超越现有最先进的单目相机检测算法。
- 实现低延迟和低资源消耗，适合边缘设备部署。
- 公开发布源代码，便于复现与进一步研究。

### 局限性
摘要未提供足够信息（未说明算法在极端光照、遮挡条件下的表现，也未提及多目标场景下的具体性能瓶颈）。

### 阅读优先级
高。理由：本文针对自动驾驶赛车这一实时性要求极高的场景，提出了在精度和延迟上优于现有方法的单目解决方案，且代码开源，对相关领域有直接参考价值和复现潜力。

</details>

<details>
<summary>Abstract</summary>

In autonomous racing, fast detection of other participants' movements is required to plan safe, collision-free trajectories with non-cooperative opponents. LiDAR detection is inherently slower and harder to deploy on edge devices than vision methods, causing delayed detections that limit object tracking performance during high-dynamic maneuvering. Utilizing monocular 3D detection enables an easy-to-deploy, low-latency detection of other participants on the racetrack. We present SPARK, a single-camera pose-estimation algorithm for autonomous racing using keypoint detection. It achieves long-range detection with high accuracy, exceeding the performance of state-of-the-art monocular camera detection algorithms while maintaining lower latency. By employing well-optimized YOLO models and leveraging the fixed geometry in the autonomous racing domain, the algorithm also exhibits low latency and resource usage. We evaluate the performance of our approach on real-world autonomous racing data and compare it to state-of-the-art LiDAR and camera detection algorithms. The source code is available at: https://github.com/TUMFTM/SPARK-camera-det

</details>

#### 2026-06-16 - MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization

**Authors:** Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian
**Links:** [abs](https://arxiv.org/abs/2606.17935) - [pdf](https://arxiv.org/pdf/2606.17935)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization
- 作者：Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2606.17935

### 一句话总结
MoonSplat 提出一种集成全局 Sim(3) 优化的在线体素化 3DGS 框架，实现了单目图像序列下的稳健相机追踪与高效全局闭环，并引入颜色残差学习以加速收敛。

### 研究问题
现存在线 3DGS 方法面临两个关键挑战：因缺乏全局优化导致的相机姿态估计脆弱，以及大规模/长序列场景下的优化效率低下。

### 核心思路/方法
1. 提出在线体素化 3DGS 重建框架，并集成全局 **Sim(3)** 优化（即同时优化尺度、旋转和平移），实现相机追踪与全局闭环对相机姿态和体素化 3DGS 的一致性修正。
2. 引入**颜色残差学习**策略，加速体素化 3DGS 的收敛，并提升渲染质量。

### 主要贡献
1. 提出结合全局 Sim(3) 优化的在线体素化 3DGS 系统，显著提升单目序列下相机姿态估计的稳健性和大场景优化效率。
2. 引入颜色残差学习策略，兼顾优化速度与渲染质量。
3. 在多种室内外数据集上，方法在相机姿态估计精度和渲染质量上达到当前最优（SOTA），并保持实时性。
4. 基于该方法开发并部署了真实的无人机主动重建系统，验证了其实用鲁棒性与泛化性。

### 局限性
摘要未提供足够信息。未提及方法在极端动态场景、遮挡、或计算资源约束下的具体表现，也未讨论可能存在的失败模式或假设限制。

### 阅读优先级
**高**  
理由：该工作直击在线 3DGS 的主要痛点（姿态估计不稳定、大场景效率低），提出了具有理论新颖性的 Sim(3) 全局优化与颜色残差学习；实验涵盖多类数据集，并落地到无人机实际系统，对机器人、AR/VR 等应用有直接启发价值。

</details>

<details>
<summary>Abstract</summary>

Online 3D reconstruction from monocular image sequences is a challenging and ongoing research topic. 3D Gaussian Splatting (3DGS), leveraging its high-quality real-time rendering capability, empowers online 3D reconstruction to represent dense scenes with enhanced expressiveness, and thus holds great promise for a wide range of applications such as robotics and AR/VR. However, existing online 3DGS methods still suffer from some key challenges: fragile camera pose estimation due to the lack of global optimization, and low optimization efficiency in large-scale or long-sequence scenarios. To address these issues, we propose a robust and efficient online voxelized 3DGS reconstruction framework integrated with global $\text{Sim}(3)$ optimization, which enables reliable camera tracking and efficient global loop closure for both camera poses and voxelized 3DGS. To accelerate the convergence of the voxelized 3DGS, we further introduce a color residual learning strategy, which not only boosts optimization speed but also enhances rendering quality. Extensive experiments on diverse indoor and outdoor datasets demonstrate that our method achieves state-of-the-art performance in both camera pose estimation accuracy and rendering quality, while retaining real-time efficiency. Additionally, we develop and deploy a real-world UAV-based active reconstruction system grounded on our proposed method, validating its robustness and generalizability for practical online 3D reconstruction tasks. Our code and data are available at https://github.com/TrickyGo/MoonSplat.

</details>

#### 2026-06-16 - High-Fidelity 3D Geometric Reconstruction of Pelvic Organs from MRI: A Hybrid Deep Learning and Iterative Optimization Approach

**Authors:** Hui Wang, Xiaowei Li, Chenxin Zhang, Yifan Feng, Jianwei Zuo, Yumeng Tang, Xiuli Sun, Jianliu Wang, Bing Xie, Jiajia Luo
**Links:** [abs](https://arxiv.org/abs/2606.17836) - [pdf](https://arxiv.org/pdf/2606.17836)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, geometric reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：High-Fidelity 3D Geometric Reconstruction of Pelvic Organs from MRI: A Hybrid Deep Learning and Iterative Optimization Approach  
- 作者：Hui Wang, Xiaowei Li, Chenxin Zhang, Yifan Feng, Jianwei Zuo, Yumeng Tang, Xiuli Sun, Jianliu Wang, Bing Xie, Jiajia Luo  
- 出版日期：2026-06-16  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：摘要页 https://arxiv.org/abs/2606.17836；PDF https://arxiv.org/pdf/2606.17836  

### 一句话总结  
本文提出一种混合深度学习与迭代优化的框架，用于从 MRI 数据中高保真重建盆腔器官（膀胱、子宫、直肠）的 3D 几何结构，在几何精度与网格质量上优于现有主流方法。

### 研究问题  
现有盆腔器官 3D 重建方法要么聚焦分割，要么侧重下游模型应用，缺乏标准化的高保真几何重建流程，导致劳动密集型且保真度不足。

### 核心思路/方法  
提出混合可变形形状建模框架，包含三个核心组件：  
1. **几何感知多层深度学习架构**：保持盆腔器官的拓扑一致性；  
2. **两阶段摊销优化训练策略**：先捕捉全局形状，后优化局部表面；  
3. **全局协同机制**：训练时迭代优化为深度学习提供监督，推理时深度学习快速预测全局形态，再经迭代优化精修局部表面与网格质量。

### 主要贡献  
- 首个集成深度学习预测与迭代优化的盆腔器官高保真重建框架；  
- 在几何保真度上显著优于主流深度学习重建模型（膀胱、直肠、子宫的 Chamfer Distance 更低，Dice 相似系数更高）；  
- 在保持高计算效率的同时，获得更好的整体体网格质量；  
- 在患者级别，框架在最小元素质量指标（minSICN 和 minSIGE）上超过传统几何后处理算法。

### 局限性  
摘要未提供足够信息。

### 阅读优先级  
**高**  
理由：该研究针对医学图像重建中实际问题（盆腔器官高保真几何重建），提出新的混合框架并取得性能提升，适用于需要高精度 3D 模型的下游分析任务；方法结构清晰，有明确的应用价值，对于从事医学图像处理、3D 重建或盆腔建模的研究者具有参考意义。

</details>

<details>
<summary>Abstract</summary>

Patient-specific 3D reconstruction of pelvic organ geometry from MRI is important for pelvic floor modeling and downstream patient-specific analysis. However, while previous studies have focused primarily on either image segmentation or downstream use of 3D models, the reconstruction of high-fidelity, high-quality geometries remains labor-intensive and poorly standardized. The study introduced a hybrid deformable shape modeling framework that integrates deep learning prediction with iterative optimization for the reconstruction of the bladder, uterus, and rectum. The framework consists of three core components: a geometry-aware multi-level deep learning architecture that preserves topological consistency of pelvic organs; a two-stage amortized optimization training strategy that balances global shape capture and local surface refinement; and a holistic synergy mechanism--where iterative optimization provides supervision for deep learning during the training phase, and during inference, deep learning rapidly predicts the global organ morphology, followed by iterative optimization to refine local surfaces and mesh quality. This framework demonstrated marked superiority in geometric fidelity than current mainstream deep learning-based organ reconstruction models. For individual anatomical structures, the reconstructed 3D geometries for the bladder, rectum, and uterus achieved significantly lower Chamfer Distance values and higher Dice Similarity Coefficient scores. In addition, while maintaining high computational efficiency, the proposed architecture yielded superior overall volumetric mesh quality. At the patient level, the framework achieved higher mean values for the 10 worst elements for both minSICN and minSIGE compared to traditional geometric post-processing algorithms.

</details>

#### 2026-06-16 - RICH-SLAM: Radar SLAM with Incremental and Continuous Hilbert Mapping

**Authors:** Bingbing Zhang, Huan Yin, Yang Xu, Shuo Liu, Shaojie Shen, Fumin Zhang, Wen Xu
**Links:** [abs](https://arxiv.org/abs/2606.17534) - [pdf](https://arxiv.org/pdf/2606.17534)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, pose estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RICH-SLAM: Radar SLAM with Incremental and Continuous Hilbert Mapping
- 作者：Bingbing Zhang, Huan Yin, Yang Xu, Shuo Liu, Shaojie Shen, Fumin Zhang, Wen Xu
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry; Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.17534

### 一句话总结
RICH-SLAM 是一种基于雷达的 SLAM 框架，通过增量希尔伯特空间高斯过程建图和后验加权粒子滤波，实现从稀疏噪声雷达测量中构建连续占用地图并支持不确定性感知规划。

### 研究问题
如何克服雷达测量数据稀疏、噪声大的固有缺陷，以实现密集、连续且一致的 SLAM 地图表示。

### 核心思路/方法
- 后端采用 Rao-Blackwellized 粒子滤波器，粒子滤波用于位姿估计，卡尔曼滤波用于地图更新。
- 提出增量希尔伯特空间降秩高斯过程建图策略（Incremental Hilbert-space reduced-rank Gaussian process mapping），能根据稀疏雷达输入生成连续且感知不确定性的地图表示。
- 引入后验感知的粒子加权方案（posterior-aware particle weighting scheme），利用地图参数的完整后验分布进行更鲁棒的似然评估。

### 主要贡献
1. 提出了 RICH-SLAM，一个为雷达传感器设计的完整 SLAM 框架。
2. 设计了增量希尔伯特空间降秩高斯过程映射方法，实现稀疏输入下的连续与不确定性建模。
3. 提出基于后验分布的粒子加权机制，提升似然估计的鲁棒性。
4. 在自采集数据集和公开 ColoRadar 数据集上验证了该方法能从稀疏雷达测量构建连续占用地图，并支持移动机器人的不确定性感知规划。

### 局限性
摘要未提供足够信息，未明确指出本方法的计算复杂度、实时性限制、对雷达硬件或环境的特定约束。

### 阅读优先级
**中**
理由：该方法针对雷达 SLAM 中稀疏、噪声数据导致的建图连续性难题，提出了基于希尔伯特空间高斯过程的创新解决方案，在理论和新颖性方面有亮点，对从事雷达 SLAM 或不确定性感知建图的研究人员有一定参考价值。但摘要未涉及详细实验对比或性能指标，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Simultaneous localization and mapping using radar sensors has gained increasing attention due to radar's inherent robustness to adverse weather and lighting conditions. However, radar measurements are characteristically sparse and noisy compared to LiDAR and visual data, posing significant challenges in achieving dense, continuous, and consistent map representations. In this paper, we present RICH-SLAM, a radar SLAM framework designed to address these challenges. Our approach features a Rao-Blackwellized particle filter-based back end that employs particle filtering for pose estimation and Kalman filtering for map updates. We propose an incremental Hilbert-space reduced-rank Gaussian process mapping strategy that enables continuous and uncertainty-aware map representations given sparse radar inputs. We further introduce a posterior-aware particle weighting scheme that leverages the full posterior distribution of map parameters for more robust likelihood evaluation. Experiments on self-collected and public ColoRadar datasets show that RICH-SLAM constructs continuous occupancy maps from sparse radar measurements and supports uncertainty-aware planning for mobile robots.

</details>

#### 2026-06-16 - Impact of Hand Impairment and Occlusions on Hand Pose Estimation Accuracy in Augmented Reality Applications

**Authors:** Damian M. Manzone, Mathew Szymanowski, Olga Taran, Shuo Cai, Melissa Marquez-Chin, Tammy Zeng, Hardeep Singh, Cesar Marquez-Chin, José Zariffa
**Links:** [abs](https://arxiv.org/abs/2606.17427) - [pdf](https://arxiv.org/pdf/2606.17427)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, AR, augmented reality, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Impact of Hand Impairment and Occlusions on Hand Pose Estimation Accuracy in Augmented Reality Applications
- 作者：Damian M. Manzone, Mathew Szymanowski, Olga Taran, Shuo Cai, Melissa Marquez-Chin, Tammy Zeng, Hardeep Singh, Cesar Marquez-Chin, José Zariffa
- 出版日期：2026-06-16
- 分类：3D Reconstruction & Multi-view Geometry（主要），Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2606.17427

### 一句话总结
本研究评估了HoloLens 2头戴显示器和多种手部姿态估计算法（WiLoR、HaMeR、WildHands、MediaPipe）在手部受损人群（颈髓损伤患者）与无损伤对照组中，以及与透明和遮挡物体交互时的姿态估计准确性。

### 研究问题
手部损伤和来自真实物体交互的遮挡对增强现实中手部姿态估计准确性的影响，以及AR头戴显示器与现有最先进姿态估计算法的比较。

### 核心思路/方法
- 被试：13名颈髓损伤患者（神经损伤水平C3-C6；ASIA等级A-D）和15名无损伤对照。
- 任务：与透明和不透明物体交互。
- 设备/算法：HoloLens 2 HMD + 4种最先进姿态估计算法（WiLoR, HaMeR, WildHands, MediaPipe）。
- 评估方式：通过多摄像机三角测量生成3D关节位置的真实值，比较预测准确性。

### 主要贡献
1. 首次系统评估手部损伤和物体遮挡对AR HMD及多种姿态估计算法准确性的影响。
2. 发现HoloLens 2和姿态估计算法的预测在受损与无损伤群体间准确性无显著差异，表明这些方法可推广至手部受损人群。
3. 透明物体相比不透明物体提供了微小精度优势（约0.1 mm），WiLoR和HaMeR比HoloLens 2略准确（约2 mm）。
4. 生成的数据库可用于改进针对手部受损人群的姿态估计方法。

### 局限性
摘要未提供足够信息，例如：缺乏具体实验设置（如摄像机数量、光照条件）、不同物体交互类型的详细分析、算法在特定遮挡模式下的表现差异，以及样本量对统计效力的影响等。

### 阅读优先级
高。理由：研究直接针对AR手部康复应用中的核心挑战（手部损伤与遮挡），并提供了主流算法与商业设备（HoloLens 2）的定量比较，对相关领域的研究者和从业者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Mixed reality applications can be designed for hand rehabilitation. Augmented reality (AR) head mounted displays (HMDs) specifically allow for ecologically valid tasks because individuals can see their real environment and interact with real objects while receiving additional cues on the HMD. While these applications rely on accurate hand pose estimation, there is a gap in investigating the influence of hand impairment or occlusion from real-object interactions on pose estimation accuracy. Further, comparisons between AR HMD predictions and state-of-the-art pose estimation methods have not been established. The current study assessed pose estimation accuracy of the HoloLens 2 HMD and state-of-the-art pose estimation algorithms (WiLoR, HaMeR, WildHands, and MediaPipe) while individuals with cervical spinal cord injury (cSCI; n = 13, Neurological Level of Injury: C3-C6; American Spinal Injury Association Impairment Scale: A-D) and 15 uninjured controls interacted with clear and opaque objects. Ground truth estimates of 3D joint positions were generated via triangulation from a multi-camera setup. Pose estimation accuracy did not differ between the cSCI and uninjured control groups suggesting that 3D joint predictions from the HoloLens 2 and pose estimation algorithms can generalize to populations with hand impairment. Further, clear objects provided a small accuracy advantage over opaque objects (0.1 mm) and predictions from both WiLoR and HaMeR were slightly more accurate than the HoloLens 2 (2 mm). Overall, these results suggest that the HoloLens 2 may be viable for hand rehabilitation applications and the dataset generated can be used to refine pose estimation methods for hand-impaired populations.

</details>

#### 2026-06-15 - SGM-SLAM: Scene Graph Matching for Data-Efficient Distributed SLAM

**Authors:** Yewei Huang, Tixiao Shan, Abhinav Rajvanshi, Niluthpol Chowdhury Mithun, Yaxuan Li, Brendan Englot, Han-Pang Chiu
**Links:** [abs](https://arxiv.org/abs/2606.16881) - [pdf](https://arxiv.org/pdf/2606.16881)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SGM-SLAM: Scene Graph Matching for Data-Efficient Distributed SLAM
- 作者：Yewei Huang, Tixiao Shan, Abhinav Rajvanshi, Niluthpol Chowdhury Mithun, Yaxuan Li, Brendan Englot, Han-Pang Chiu
- 出版日期：2026-06-15
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：摘要： https://arxiv.org/abs/2606.16881 ；PDF： https://arxiv.org/pdf/2606.16881

### 一句话总结
提出一种基于场景图匹配的数据高效分布式SLAM框架，通过仅使用对象标签和质心进行匹配，实现多机器人间的协作定位与建图。

### 研究问题
如何高效地在多机器人分布式SLAM系统中，利用场景图匹配识别机器人间的测量约束，同时降低通信和数据交换成本。

### 核心思路/方法
1. 构建场景图：利用融合的RGB-LiDAR点云生成语义分割点云层和离散有界对象层，并辅以估计的机器人轨迹。
2. 场景图匹配：仅使用对象标签和质心（而非传统特征级匹配）进行协作匹配，通过多步数据交换与优化过程最大化通信效率。
3. 框架集成：将场景图匹配作为分布式SLAM的约束机制，支持装备激光雷达、相机和惯性传感器的机器人团队。

### 主要贡献
- 首次提出仅依赖对象标签和质心的场景图匹配方法，用于分布式SLAM中的机器人间约束识别。
- 设计了多步数据交换与优化流程，显著提升通信效率。
- 通过仿真和真实世界（四足机器人）数据集验证了框架在室内外环境中的有效性与高效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。
理由：该工作聚焦分布式SLAM中的数据效率和场景图匹配，属于技术设计完善的应用型研究，但未提供与现有方法的定量对比或极致性能提升证据，适合对多机器人SLAM或语义建图感兴趣的读者参考。

</details>

<details>
<summary>Abstract</summary>

We introduce a data-efficient distributed Simultaneous Localization and Mapping (SLAM) framework designed for a team of robots equipped with LiDAR, cameras, and inertial sensors. Our framework uses scene graph matching to identify inter-robot measurement constraints. Unlike prior approaches that rely on feature-level matching, our framework is the first to perform scene graph matching using only object labels and centroids. Our approach constructs a scene graph by using fused RGB-LiDAR point clouds to generate both a semantically segmented point cloud layer, and a layer of discrete bounded objects, to accompany estimated robot trajectories. Scene graph matching is performed collaboratively through exchanging and matching object data with neighboring robots. To maximize communication efficiency, we utilize a multi-step data exchange and optimization process. We demonstrate the effectiveness and efficiency of our approach using both simulation and real-world datasets collected by legged robots in indoor and outdoor environments.

</details>

#### 2026-06-15 - MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods

**Authors:** Robert Langendörfer, Markus Hillemann, Markus Ulrich
**Links:** [abs](https://arxiv.org/abs/2606.16638) - [pdf](https://arxiv.org/pdf/2606.16638)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** visual geometry grounded transformer, 3D reconstruction, multi-view stereo, structure from motion, camera pose estimation, pose estimation, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods
- 作者：Robert Langendörfer, Markus Hillemann, Markus Ulrich
- 出版日期：2026-06-15T12:26:47Z
- 分类：3D Reconstruction & Multi-view Geometry (主要), Neural Scene Representations & Rendering (次要)
- 链接：摘要链接: https://arxiv.org/abs/2606.16638, PDF链接: https://arxiv.org/pdf/2606.16638

### 一句话总结
本文提出了一个名为MVM-IOD的工业物体中心基准数据集，用于评估3D重建方法，并基于该数据集对当前多种SOTA方法（如SfM、MVS、前馈网络等）进行了实验。

### 研究问题
现有的3D重建和相机位姿估计数据集大多未描绘真实的工业场景，而工业应用中的高成本和时间限制使得该任务极具挑战性。

### 核心思路/方法
1.  **构建数据集 (MVM-IOD)**：通过将工业机器人臂末端执行器上的相机沿半球轨迹系统性地移动，采集典型工业物体的RGB图像、参考相机位姿和参考3D点云。数据集包含9个物体和2种背景选择，共18个场景。
2.  **定义基准评估**：基于该数据集，对多种当前SOTA方法（包括传统方法如Structure from Motion、Multi-View Stereo，以及前馈方法如Visual Geometry Grounded Transformer、π3，还有2D Gaussian Splatting）进行广泛评估，报告基线结果。

### 主要贡献
1.  **引入MVM-IOD数据集**：该数据集专门针对真实工业场景中的3D重建和相机位姿评估，提供参考位姿和点云。
2.  **揭示前馈方法的局限性**：实验表明，数据集中的捕获设置（半球轨迹）为前馈方法生成了分布外图像，导致次优的点云和位姿。
3.  **提出改进路径**：发现通过应用简单的预处理步骤，可以将分布外图像向训练分布偏移，从而改善前馈方法性能，并提示在特定工业应用中应谨慎使用这些方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：论文提出了一个针对特定工业场景的基准数据集（MVM-IOD），并基于该数据集对比了传统与前沿（如前馈网络）3D重建方法，为评估该类方法提供了标准。但数据集的具体细节（如物体种类、数量、场景复杂性）及实验结果的量化指标在摘要中未展示，需要阅读全文才能获得更深入的见解。

</details>

<details>
<summary>Abstract</summary>

3D object reconstruction, and camera pose estimation in industrial applications are challenging tasks, as errors are costly while the computation time is often limited. The complexity of typical industrial objects further complicates these tasks. Most of the existing datasets in this context do not depict realistic industrial scenarios. Therefore, we introduce the Machine Vision Metrology Industrial Object Dataset (MVM-IOD). Images of typical industrial objects are captured systematically, by moving a camera, mounted at the end effector of an industrial robot arm, on a hemisphere around the objects. MVM-IOD contains reference camera poses and reference 3D point clouds, the acquired RGB images of 9 objects and 2 background choices resulting in 18 scenes, which allows evaluation of all image based methods that compute a 3D reconstruction, camera poses, or novel views of a scene. Based on MVM-IOD, we extensively evaluate current SOTA 3D reconstruction and camera pose estimation methods, such as Structure from Motion, Multi-View Stereo, recent feed forward methods (Visual Geometry Grounded Transformer, π3), and 2D Gaussian Splatting and report our findings as a baseline for future research. The experiments show that capture setups like ours generate out-of distribution images for feed forward methods, leading to suboptimal point clouds and camera poses. However, these out-of-distribution images can be shifted closer to the training distribution by applying simple preprocessing steps. Consequently, in certain industrial applications, feed forward methods should be used with caution.

</details>

#### 2026-06-15 - Rotational Symmetry based Object Pose Estimation from Point Clouds in the Absence of Known 3D Models

**Authors:** Weichen Dai, Ruixun Yu, Yangjie Tang, Yifan Du, Yiyang Zhang, Donglei Sun, Hua Zhang
**Links:** [abs](https://arxiv.org/abs/2606.16593) - [pdf](https://arxiv.org/pdf/2606.16593)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rotational Symmetry based Object Pose Estimation from Point Clouds in the Absence of Known 3D Models
- 作者：Weichen Dai, Ruixun Yu, Yangjie Tang, Yifan Du, Yiyang Zhang, Donglei Sun, Hua Zhang
- 出版日期：2026-06-15
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：abstract: https://arxiv.org/abs/2606.16593 ; pdf: https://arxiv.org/pdf/2606.16593

### 一句话总结
提出一种在无已知3D模型情况下，利用物体旋转对称性先验信息，通过迭代优化同时估计点云姿态并细化点云的方法。

### 研究问题
如何在没有已知高质量3D模型（例如因保密限制无法获取）的条件下，仅依据点云数据实现工业物体的姿态估计。

### 核心思路/方法
1. **利用旋转对称性**：将工业物体常见的旋转对称性作为先验信息，替代缺失的3D模型。
2. **迭代优化过程**：姿态估计与点云细化联合进行。
3. **旋转对称约束损失**：
   - 根据当前估计的姿态旋转每个3D点。
   - 利用旋转对称性，通过最近邻搜索为每个点找到多个对应点。
   - 基于这些对应关系计算旋转对称约束损失，用于迭代更新姿态和点云。

### 主要贡献
- 提出一种不依赖已知3D模型，仅靠旋转对称性先验实现点云姿态估计的方法。
- 通过显式将旋转对称性融入优化过程，方法在多种物体类型上表现出鲁棒性和良好的泛化能力。
- 在自建数据集（含四类合成物体和一类真实轮毂）上，性能与依赖已知3D模型的方法相当。

### 局限性
摘要未提供足够信息。例如，未说明方法在非对称物体上的表现、对强噪声或遮挡的处理能力，也未提及计算效率或依赖的具体对称性条件（如仅轴向对称还是多类对称）。

### 阅读优先级
**中**
理由：研究问题（无模型姿态估计）具有实际应用价值，且方法思路清晰（利用旋转对称性+迭代优化）。但需注意其适用场景局限在有旋转对称性的工业零件上，且摘要未提供详细定量对比结果，需阅读全文评估实际效果和泛化性。

</details>

<details>
<summary>Abstract</summary>

Object pose estimation is crucial to many industrial applications, with one example being automated spray painting using a robot. However, confidentiality concerns often limit access to high-quality 3D models, posing a significant challenge for point-cloud-based pose estimation. In such scenarios, rotational symmetry, a readily accessible characteristic of many industrial objects, can provide valuable prior information to facilitate pose estimation.In this paper, we propose a method that leverages the rotational symmetry commonly found in industrial objects to address the challenge caused by the absence of 3D models. The object pose is jointly estimated with point cloud refinement through an iterative optimization process. This optimization relies on a rotational symmetry constraint loss. To construct this loss, each 3D point is rotated according to the currently estimated pose, and multiple correspondences are identified using nearest-neighbor search by exploiting the rotational symmetry property. These correspondences are then used to compute the rotational symmetry constraint loss, which iteratively refines both the pose and the point cloud.By explicitly incorporating rotational symmetry into the optimization process, the proposed method achieves robust pose estimation and generalizes well across diverse object types. The proposed method is evaluated on a dataset specifically created for point clouds without known 3D models, consisting of four categories of synthetic objects and one real wheel hub collected from a production line. Experimental results demonstrate that the proposed method achieves performance comparable to methods that rely on known 3D models.

</details>

#### 2026-06-15 - Instance-Aware Knowledge Distillation for Semi-Supervised Learning of an On-Board Multi-Task Dense Prediction Model for Collision Avoidance System

**Authors:** Gyutae Hwang, Sang Jun Lee
**Links:** [abs](https://arxiv.org/abs/2606.16414) - [pdf](https://arxiv.org/pdf/2606.16414)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, monocular depth, driving scene, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Instance-Aware Knowledge Distillation for Semi-Supervised Learning of an On-Board Multi-Task Dense Prediction Model for Collision Avoidance System
- 作者：Gyutae Hwang, Sang Jun Lee
- 出版日期：2026-06-15T08:51:06Z
- 分类：3D Reconstruction & Multi-view Geometry（主类）；Embodied / Robotics / AR Applications（次类）
- 链接：摘要：https://arxiv.org/abs/2606.16414 | PDF：https://arxiv.org/pdf/2606.16414

### 一句话总结
本文提出一种实例感知知识蒸馏框架，用于半监督学习轻量级多任务密集预测模型，并部署于低算力边缘设备的碰撞避免系统，在目标域（乡村俱乐部数据集）上实现学生模型性能超越大教师模型，计算量大幅降低。

### 研究问题
如何在有限计算资源和标注成本下，为碰撞避免系统训练一个轻量级、多任务密集预测模型，并部署到边缘设备上。

### 核心思路/方法
1. **实例感知知识蒸馏框架**：结合教师模型的域先验和基础模型的实例中心知识，生成伪标签以缓解教师偏差。  
2. **半监督学习**：利用伪标签进行训练，降低对大规模标注数据集的依赖。  
3. **多任务密集预测**：学生模型同时执行前向障碍物检测和单目深度估计。  
4. **系统部署**：将学生模型部署到低算力边缘设备，实时将障碍物空间信息编码为CAN消息，用于自动导引车操作。  
5. **数据集构建与验证**：构建大型乡村俱乐部数据集，并进行实地验证。

### 主要贡献
1. 提出基于实例感知知识蒸馏的半监督学习框架，有效缓解教师偏差。  
2. 学生模型在实例分割任务上超越教师模型，并在单目深度估计中保持性能稳定。  
3. 与教师模型相比，学生模型FLOPs降低22.68倍，参数量减少14.33倍，在低算力边缘设备上达到6.46 FPS。  
4. 构建了大型乡村俱乐部数据集，并完成多任务密集预测碰撞避免系统的实地验证。

### 局限性
摘要未提供足够信息：未提及伪标签生成的具体失败案例、框架对不同数据域（非乡村俱乐部场景）的泛化能力、深度估计性能下降的具体数值、系统在极端场景（如夜间、恶劣天气）下的表现，以及半监督学习所需的未标注数据量等。

### 阅读优先级
**高**  
理由：  
- 提出新颖的实例感知知识蒸馏框架，结合半监督学习，有效解决边缘部署中的算力和标注瓶颈。  
- 实验结果显著（学生模型参数量和FLOPs大幅降低，部分任务性能超越教师），具有实际应用价值。  
- 涉及当前热门方向（多任务密集预测、边缘AI、自动导引车安全），对计算机视觉和机器人交叉领域的研究者有参考意义。

</details>

<details>
<summary>Abstract</summary>

Collision avoidance systems have evolved toward camera-based deep learning approaches for driving scene understanding. However, deployment in edge environments such as country clubs is constrained by limited computational resources and unreliable communication infrastructure. Moreover, constructing large-scale datasets for the target domain involves substantial annotation cost. To address these limitations, we propose an instance-aware knowledge distillation framework for semi-supervised learning. Specifically, we generate pseudo labels that mitigate teacher bias by leveraging domain priors from the teacher and instance-centric knowledge from foundation models. The trained lightweight student is deployed in the proposed collision avoidance system and performs multiple dense prediction tasks in real-time. The system detects frontal obstacles and encodes their spatial information into controller area network messages for automated guided vehicle operation. To achieve this, we construct a large-scale country club dataset and perform field validation of the proposed system. Experimental results demonstrate that the student outperforms the large teacher in instance segmentation while mitigating performance degradation in monocular depth estimation. Compared with the teacher, the student reduces FLOPs by 22.68$\times$ and parameters by 14.33$\times$, achieving 6.46 FPS on a low-cost edge device.

</details>

#### 2026-06-12 - StereoGeo: an end-to-end stereo camera calibration method

**Authors:** Imane Meddour, Andréa Macario Barros, Cédric Gouy-Pailler
**Links:** [abs](https://arxiv.org/abs/2606.14619) - [pdf](https://arxiv.org/pdf/2606.14619)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StereoGeo: an end-to-end stereo camera calibration method
- 作者：Imane Meddour, Andréa Macario Barros, Cédric Gouy-Pailler
- 出版日期：2026-06-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.14619

### 一句话总结
本文提出了一种基于端到端网络的立体相机标定方法StereoGeo，能够同时估计左右相机的焦距、重力方向以及两者之间的相对外参。

### 研究问题
如何设计一种端到端的方法，在无需结构化环境中的标定图案、且不局限于单目或多视角设置的情况下，同时完成立体相机的内参（焦距、重力方向）和外参（相对位姿）标定。

### 核心思路/方法
扩展GeoCalib算法，将深度神经网络的特征提取与可微分优化器相结合，构建一个端到端的网络架构，用于立体相机标定。

### 主要贡献
1. 提出了StereoGeo，首个端到端的立体相机标定网络，同时估计左右相机的焦距、重力方向及相对外参。
2. 在真实世界基准数据集上，该方法在内参标定上达到有竞争力表现，并在立体外参估计上准确度优于现有的单目方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法聚焦于立体相机标定这一专业子领域，解决了现有方法在端到端联合标定上的不足，但论文公开的摘要篇幅有限，缺乏对方法架构细节、实验设置和量化结果的深入描述，适合对该方向有特定需求的读者作为参考。

</details>

<details>
<summary>Abstract</summary>

In this work, we propose StereoGeo, an end-to-end network-based approach for stereo camera calibration. Our method estimates the focal lengths and gravity directions of the left and right cameras, as well as the relative extrinsic transformation relating them. Existing methods often rely on calibration patterns in structured environments or address only a single camera configuration, being limited to either intrinsic or extrinsic estimation, and depending on a multi-view setups. StereoGeo extends the GeoCalib algorithm, integrating deep neural network feature extraction with a differentiable optimizer. Extensive experiments on real-world benchmarks demonstrate that StereoGeo achieves competitive performance for intrinsic calibration and provides accurate stereo extrinsic estimation, outperforming existing methods that are limited to monocular settings. The dataset used in this work is partially publicly available at https://github.com/meddourimane/StereoGeo-dataset.

</details>

#### 2026-06-12 - Scratched Lenses, Shifted Depth: Passive Camera-Side Optical Attacks

**Authors:** Qinlin He, Zeming Zhuang, Yongji Wu, Lan Zhang, Xiaoyong, Yuan
**Links:** [abs](https://arxiv.org/abs/2606.14504) - [pdf](https://arxiv.org/pdf/2606.14504)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Scratched Lenses, Shifted Depth: Passive Camera-Side Optical Attacks
- 作者：Qinlin He, Zeming Zhuang, Yongji Wu, Lan Zhang, Xiaoyong, Yuan
- 出版日期：2026-06-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.14504

### 一句话总结
本文提出一种新型被动摄像端物理对抗攻击：通过在镜头或保护罩上制造微小划痕，当特定视觉条件（如强光源、镜面反射）触发时，划痕会产生结构化的光学伪影，从而扭曲单目深度估计和3D目标检测中的深度信息。

### 研究问题
- 如何利用摄像端物理损伤（如镜头划痕）作为持久的、场景触发的对抗攻击，来误导几何推理（尤其是深度估计）？

### 核心思路/方法
- 将攻击建模为光学空间中的触发条件通道：划痕作为固定但场景触发的光学扰动源。
- 提出SLASH（Scratch-induced Lens Adversarial Streak Hijacking）攻击：利用微小划痕与明亮光源、镜面反射交互产生条纹伪影，扭曲深度线索。
- 在数字和真实世界中评估：分别测试单目深度估计和单目3D目标检测任务；物理实验验证攻击可从数字仿真迁移至真实相机录制结果。

### 主要贡献
- 识别了一种新的对抗攻击表面：看似无害的硬件缺陷（如镜头划痕）可作为潜在、场景触发的对抗机制。
- 提出并验证了SLASH攻击：在固定划痕约束下，单目深度估计的相对误差可达32%。
- 证明了该攻击在物理世界中的可迁移性：真实相机录制结果显示深度偏移超过模型自然预测基线。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该工作揭示了硬件物理损伤作为新攻击面的安全风险，对3D视觉系统鲁棒性研究有启发意义。但方法聚焦于特定物理实现（镜头划痕），且未在摘要中提供防御思路或大规模基准对比，适合对对抗攻击与3D视觉交叉领域感兴趣的研究者，非该领域读者优先级可适度降低。

</details>

<details>
<summary>Abstract</summary>

Physical adversarial attacks on vision systems are typically studied through scene manipulation, such as adversarial patches or projections, where the adversary controls what the camera observes. Camera-side attacks using stickers or auxiliary optics have also been explored, but they treat attacks as image-space perturbations from designed patterns. This misses how physical imperfections interact with scene-dependent lighting and optics. We identify a threat: passive lens-side damage that is persistent yet trigger-conditioned, producing optical artifacts that bias geometric inference under particular visual conditions. We instantiate this threat through Scratch-induced Lens Adversarial Streak Hijacking SLASH, a physical-world attack caused by small scratches on a camera lens or protective cover. Scratches interact with bright light sources and specular reflections to create structured streak artifacts that distort depth cues. Since the perturbation is fixed in the optical path but triggered by the scene, it is both persistent and selective. We formulate the attack in optical space, model the scratch pattern as a trigger-conditioned optical channel, and optimize one fixed configuration across diverse viewing conditions. We evaluate SLASH on monocular depth estimation and monocular 3D object detection in digital and real-world settings. Under the fixed-scratch constraint, directional depth shifts reach up to 32% relative error for monocular depth estimation, with consistent effects on monocular 3D object detection. Physical experiments confirm transfer to real camera recordings, inducing depth shifts above the model's natural prediction baseline. These findings reveal an attack surface where benign-looking hardware imperfections act as latent, scene-triggered adversarial mechanisms, challenging assumptions about physical robustness and motivating defenses for secure vision systems.

</details>

#### 2026-06-12 - MooMIns -- Monocular 3D Reconstruction and Object Pose Estimation from Multiple Instances

**Authors:** Robert Langendörfer, Markus Hillemann, Markus Ulrich
**Links:** [abs](https://arxiv.org/abs/2606.14389) - [pdf](https://arxiv.org/pdf/2606.14389)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, structure from motion, SfM, pose estimation, depth estimation, monocular depth, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MooMIns -- Monocular 3D Reconstruction and Object Pose Estimation from Multiple Instances
- 作者：Robert Langendörfer, Markus Hillemann, Markus Ulrich
- 出版日期：2026-06-12T12:24:50Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.14389

### 一句话总结
提出一种基于高斯溅射（Gaussian-splatting）的框架MooMIns，通过利用单张单目图像中同一物体的多个实例，同时实现3D重建和6D位姿估计。

### 研究问题
如何从单张单目图像中同时进行3D重建和6D物体位姿估计？原始问题本身是不适定的，但工业场景中堆叠物体提供隐式多视图线索，可被利用来解决此问题。

### 核心思路/方法
- 反向高斯溅射：将原始高斯溅射的“从多相机渲染单场景”反转，变为“从单相机渲染多物体实例”。
- 初始化：使用SAM3实例分割掩码和修改后的运动恢复结构（SfM）流水线。
- 几何重建：强调基于图像证据的真正几何重建，而非基于训练数据先验的深度估计，避免产生幻觉。

### 主要贡献
- 提出MooMIns框架，利用单张图像中多个物体实例的隐式多视图几何。
- 在合成与真实堆叠抓取场景下，实现高精度的3D重建和可靠的单实例6D位姿估计。
- 不同于基于学习的单目深度估计，方法避免了训练数据的先验偏差。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中** —— 该方法针对工业堆叠场景中的3D重建与位姿估计，思路新颖，反向利用了高斯溅射，但评估仅提及合成和真实场景，缺乏与主流方法的定量对比细节。对单目重建与位姿估计方向的研究者有一定参考价值。

</details>

<details>
<summary>Abstract</summary>

Simultaneous 3D reconstruction and 6D object pose estimation from a single monocular image is an inherently ill-posed problem. In industrial settings, however, multiple instances of an object are often randomly arranged in bins, implicitly providing several views of the same object within a single image. We show that this implicit multi-view geometry can be exploited to simultaneously reconstruct the object in 3D and estimate the 6D pose of each visible object instance. We present MooMIns, a new Gaussian-splatting-based approach that inverts the original Gaussian splatting formulation: instead of rendering a single scene from multiple cameras, we render multiple object instances from a single camera. Our method is initialized with SAM3 instance segmentation masks and a modified Structure from Motion (SfM) pipeline. In contrast to learned monocular depth estimation, we perform true geometry-based reconstruction from image evidence, avoiding hallucinations caused by training data priors. We evaluate MooMIns on synthetic and real bin-picking scenarios, and demonstrate accurate reconstruction of previously unseen objects as well as reliable pose estimation of individual instance

</details>

#### 2026-06-12 - Pano3D: Unified 3D Reconstruction and Panoptic Segmentation

**Authors:** Victor Barberteguy, Ahmet Iscen, Mathilde Caron, Alireza Fathi, Gül Varol, Cordelia Schmid
**Links:** [abs](https://arxiv.org/abs/2606.14307) - [pdf](https://arxiv.org/pdf/2606.14307)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feedforward reconstruction, 3D reconstruction, dense reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Pano3D: Unified 3D Reconstruction and Panoptic Segmentation
- 作者：Victor Barberteguy, Ahmet Iscen, Mathilde Caron, Alireza Fathi, Gül Varol, Cordelia Schmid
- 出版日期：2026-06-12
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2606.14307) | [PDF](https://arxiv.org/pdf/2606.14307)

### 一句话总结
本文提出一种统一框架，将前馈式3D重建网络与基于集合的掩码解码器结合，实现无需相机参数的3D重建与全景分割联合学习，并在多个数据集上达到最优性能。

### 研究问题
如何使前馈式3D重建神经网络在无需相机参数的情况下，同时具备鲁棒的3D全景分割语义理解能力？

### 核心思路/方法
- 在现有3D重建模型基础上，增加一个基于集合的掩码解码器。
- 联合训练几何损失和语义损失，使几何特征与语义特征相互促进。
- 特征初始化时利用几何信息，然后微调以同时捕获几何与语义。
- 方法适用于在线注意力和全对注意力两种重建骨干网络。

### 主要贡献
1. 首次在统一框架中实现3D重建与3D全景分割的联合学习。
2. 通过共享训练目标，证明了几何与语义损失具有相互促进作用。
3. 在ScanNet、ScanNet200和ScanNet++数据集上取得了3D全景分割的最优结果。
4. 消融实验表明联合训练能为前馈式3D重建网络提供全景分割能力，并实现双向性能提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高
理由：该方法将3D重建与全景分割统一在单框架中，兼具理论创新（特征联合初始化与微调）和实际性能（SOTA结果），且泛化至多种骨干网络，对3D视觉领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D feedforward reconstruction neural networks have achieved remarkable success in dense reconstruction from images without any camera parameters. Yet, equipping these models with robust semantic understanding remains an open problem. Here we introduce an approach that performs 3D reconstruction and 3D panoptic segmentation in a unified framework. We build on existing 3D reconstruction models and augment them with a set-based mask decoder. The approach is jointly trained with a geometric and semantic loss, which are shown to be mutually beneficial. More precisely, the features are initialized from the geometric information and then finetuned to capture jointly geometry and semantics. We demonstrate the generality of our approach by successfully applying our framework both to online and all-to-all attention reconstruction backbones. Our method achieves state-of-the-art performance in 3D panoptic segmentation across ScanNet, ScanNet200, and ScanNet++ datasets. Ablation studies show that such joint training of a unified model equips 3D feedforward reconstruction neural networks with panoptic segmentation and yields mutually beneficial improvements.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-16 - AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement

**Authors:** Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.17998) - [pdf](https://arxiv.org/pdf/2606.17998)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement
- 作者：Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-16
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.17998

### 一句话总结
AIGS-Net是一种超轻量级网络，通过输入自适应的2D高斯点照明场模型，仅用约40个可学习参数即可实现快速、高质量的低光照图像增强。

### 研究问题
现有低光照图像增强方法在光照场建模的表达能力与计算复杂度之间难以平衡，导致细节恢复和色彩保真度不足。

### 核心思路/方法
1. 构建输入自适应的2D高斯点照明场，其高斯基函数的不透明度由输入图像相对亮度统计动态调节，并通过有序Alpha合成渲染空间变化的照明补偿。
2. 引入零参数非线性多尺度上下文编码模块，无需额外卷积权重即可提取低频结构和局部对比度线索。
3. 集成噪声掩膜估计、锁定单通道Gamma映射、跨通道一致性正则化及目标颜色对齐约束，抑制噪声放大和传感器导致的色彩偏差。

### 主要贡献
1. 提出超轻量级AIGS-Net架构，仅需约40个可学习参数。
2. 设计了输入自适应的2D高斯点照明场，实现高效光照建模与补偿。
3. 在LOL和LSRW基准上实现细节恢复与色彩保真度的提升，同时保持极快的推理速度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作专注于低光照图像增强领域的实际效率问题，方法新颖（结合2D高斯点与极轻量设计），且实验结果明确。但摘要未提供与其他方法的定量对比细节或开源信息，其实际可复现性和规模效应尚需进一步评估。若对超轻量级网络或照明场建模感兴趣，则值得一读。

</details>

<details>
<summary>Abstract</summary>

Existing low-light image enhancement methods often face a bottleneck between the representation capacity of illumination-field modeling and computational complexity. To address this issue, this paper proposes an Adaptive Illumination Gaussian Splatting Network (AIGS-Net), an ultra-lightweight architecture for fast low-light enhancement. Unlike conventional static priors, AIGS-Net constructs an input-adaptive 2D Gaussian Splatting illumination field. The opacity of Gaussian basis functions is dynamically modulated by relative luminance statistics of the input image, and spatially varying illumination compensation is rendered through ordered alpha compositing. To guide adaptive illumination compensation efficiently, a zero-parameter nonlinear multiscale contextual encoding module is introduced to extract low-frequency structures and local contrast cues without additional convolutional weights. To suppress noise amplification and sensor-induced color bias, AIGS-Net integrates noise-mask estimation, locked single-channel Gamma mapping, cross-channel consistency regularization, and target color-alignment constraints. Experiments on LOL and LSRW benchmarks show that AIGS-Net improves detail recovery and color fidelity while requiring only approximately 40 learnable parameters, achieving an effective trade-off between enhancement quality and extreme inference efficiency.

</details>

#### 2026-06-16 - Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement

**Authors:** Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, Ying Fang, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.17985) - [pdf](https://arxiv.org/pdf/2606.17985)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement
- 作者：Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, Ying Fang, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-16T14:37:08Z
- 分类：Neural Scene Representations & Rendering
- 链接：论文摘要 https://arxiv.org/abs/2606.17985 | PDF https://arxiv.org/pdf/2606.17985

### 一句话总结
本文提出GLFS，一种将高斯光场飞溅的连续物理光照模型集成到Vision Transformer中，用于无监督低光图像增强的方法。

### 研究问题
现有无监督低光图像增强方法在复杂非均匀光照下容易出现局部曝光失衡和颜色失真，且大多数Vision Transformer缺乏显式建模光照退化物理先验的机制。

### 核心思路/方法
1. 将场景光照表示为各向异性高斯基函数的叠加，实现连续物理光照建模。
2. 在自注意力机制中引入物理引导偏差，自适应推断空间增益场，以实现复杂光照下的准确均匀恢复。
3. 开发颜色矢量角度损失和亮度-边缘损失，分别用于减少增强过程中的色偏和结构退化，保持色调一致性并提高局部细节的结构保真度。

### 主要贡献
1. 提出了GLFS，一种基于高斯光场飞溅的Vision Transformer，将连续物理光照建模引入Transformer架构。
2. 通过物理指导的偏差机制，使自注意力能够自适应地推断空间增益场，改善非均匀光照下的恢复效果。
3. 设计了颜色矢量角度损失和亮度-边缘损失，有效抑制色偏并提升细节结构保真度。
4. 消融研究和定量评估表明，GLFS在光照校正和细节保留方面具有明显优势，达到当前最优性能，并为低光图像增强提供了新的表示范式。

### 局限性
摘要未提供足够信息（例如模型计算复杂度、对极端暗光场景的鲁棒性、是否依赖特定数据集或超参数设置等）。

### 阅读优先级
**高**。
理由：该工作针对低光图像增强中的核心痛点（非均匀光照、颜色失真）提出了物理先验驱动的Transformer结构，并设计了专用损失函数。论文表示达到SOTA性能并提供新表示范式，属于方法创新度较高的文章，对相关领域研究者有较强借鉴意义。

</details>

<details>
<summary>Abstract</summary>

Existing unsupervised low-light image enhancement methods often encounter local exposure imbalance and color distortion under complex non-uniform illumination. In addition, most Vision Transformers lack an explicit mechanism for modeling the physical priors of illumination degradation. To address these limitations, we propose GLFS, a Gaussian light field splatting-based Vision Transformer that integrates continuous physical illumination modeling from Gaussian splatting into the Transformer architecture. In GLFS, scene illumination is represented by a superposition of anisotropic Gaussian basis functions. Physics-guided biases are introduced into self-attention to adaptively infer a spatial gain field, enabling accurate and uniform restoration under complex illumination. To reduce color bias and structural degradation during enhancement, a color-vector angular loss and a luminance-edge loss are further developed. These losses enforce hue consistency and improve the structural fidelity of local details. Extensive ablation studies and quantitative evaluations show that GLFS provides clear advantages in illumination correction and detail preservation. It achieves state-of-the-art performance and offers a new representation paradigm for low-light image enhancement.

</details>

#### 2026-06-16 - GSPan: A Continuous Gaussian Primitive Representation for Arbitrary-Scale Pansharpening

**Authors:** Fangyi Li, Xiaoyuan Yang, Yixiao Li, Zongyang Sui, Kangqing Shen, Gemine Vivone
**Links:** [abs](https://arxiv.org/abs/2606.17722) - [pdf](https://arxiv.org/pdf/2606.17722)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, Gaussian primitive, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GSPan: A Continuous Gaussian Primitive Representation for Arbitrary-Scale Pansharpening
- 作者：Fangyi Li, Xiaoyuan Yang, Yixiao Li, Zongyang Sui, Kangqing Shen, Gemine Vivone
- 出版日期：2026-06-16T09:36:36Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.17722

### 一句话总结
GSPan 提出用连续二维高斯基元表示残差细节，实现任意尺度的全色锐化融合。

### 研究问题
现有全色锐化深度学习方法局限于固定网格预测，无法灵活适应不同缩放比例。

### 核心思路/方法
- 将每个波段上的残差细节建模为连续且可学习的二维高斯基元。
- 设计双流分层交互（DSHI）架构和空间-光谱交互注意力（SSIA）模块，从PAN和MS观测中估计这些基元。
- 将预测的基元渲染为残差细节场，注入上采样后的MS图像。
- 提出尺度解耦非对称推理（SDAI）策略：先以较低分辨率估计基元，再在目标分辨率下渲染融合图像。

### 主要贡献
- 首次将二维高斯泼溅引入全色锐化，实现任意缩放网格上的连续融合。
- 提出双流分层交互与空间-光谱交互注意力机制，用于从互补数据中估计高斯基元。
- 设计尺度解耦推理策略，可降低大场景推理的计算成本。
- 在QuickBird、GaoFen-2、WorldView-3及WorldView-3-4K数据集上实现最先进的融合性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。该工作创新性地用连续表示替代固定网格预测，解决了全色锐化中的尺度适应问题，并支持高效推理，方法论新颖且实验基准覆盖多个卫星数据集。

</details>

<details>
<summary>Abstract</summary>

Pansharpening aims to generate high-resolution multispectral (HRMS) images by fusing low-resolution multispectral (LRMS) and panchromatic (PAN) observations. Most existing deep learning methods treat pansharpening as fixed-grid prediction, which limits scale adaptation. To address this, we propose GSPan, a framework that introduces 2D Gaussian Splatting (GS) into pansharpening. Instead of directly predicting pixels, GSPan represents band-wise residual details as continuous and learnable 2D Gaussian primitives. We design a Dual-Stream Hierarchical Interaction (DSHI) architecture with a Spatial-Spectral Interactive Attention (SSIA) module to estimate these primitives from complementary PAN and MS observations. The predicted primitives are rendered as a residual detail field and injected into the upsampled MS image. This continuous representation allows GSPan to render fused images on arbitrary target sampling grids without scale-specific retraining. It further enables a Scale-Decoupled Asymmetric Inference (SDAI) strategy, which estimates primitives at a reduced resolution and renders the fused image at the target resolution for efficient large-scene pansharpening. Experiments on QuickBird, GaoFen-2, WorldView-3, and WorldView-3-4K datasets show that GSPan delivers state-of-the-art fusion performance. Moreover, SDAI markedly accelerates inference, achieving a favorable trade-off between computational efficiency and fusion quality. Our results demonstrate the potential of continuous Gaussian residual representations as a flexible and scale-decoupled alternative to fixed-grid prediction.

</details>

#### 2026-06-16 - GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments

**Authors:** Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.17520) - [pdf](https://arxiv.org/pdf/2606.17520)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GASE: 基于高斯泼溅的自动化系统用于重建具身仿真环境  
- 作者：Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang  
- 出版日期：2026-06-16T05:00:42Z  
- 分类：Neural Scene Representations & Rendering（主要）；Embodied / Robotics / AR Applications（次要）  
- 链接：摘要 https://arxiv.org/abs/2606.17520 ；PDF https://arxiv.org/pdf/2606.17520  

### 一句话总结  
GASE 是一个基于高斯泼溅的高度自动化系统，利用全景相机阵列快速扫描环境，并采用相机位姿引导的前景提取与高质量修复策略，独立重建前景物体与静态背景，以实现逼真的仿真场景构建，有效缩小 sim-to-real 差距。

### 研究问题  
如何高效、自动化地重建高保真仿真场景，以减小模拟环境与真实环境之间的 sim-to-real 差距，用于机器人具身智能体的策略训练。

### 核心思路/方法  
1. **高效数据采集**：采用全景相机阵列的多视角视频流，实现快速环境扫描。  
2. **前景-背景分离与修复**：引入基于相机位姿的策略，在2D域内鲁棒地跨帧提取前景物体；对背景进行高保真场景修复。  
3. **独立重建与导入**：前景物体与静态背景分别使用3D高斯泼溅等方法独立重建，并无缝导入物理仿真器用于策略训练。

### 主要贡献  
- 提出了一个高度自动化的仿真场景构建系统 GASE，显著简化了现有工作流中的数据采集与前景提取步骤。  
- 在分割精度上超越现有3D高斯方法超过10%，同时实现了最先进的修复质量。  
- 在真实机器人操作与导航任务中，与纯真实世界数据训练的策略相比，性能差距维持在10%以内，验证了系统在弥合 sim-to-real 差距上的有效性。  
- 将开源代码以促进可复现性。

### 局限性  
摘要未提供足够信息。

### 阅读优先级  
**高**  
**理由**：该系统在分割精度和修复质量上取得显著提升（分别超过10%和最先进水平），且在真实机器人部署中保持了较小的性能差距（<10%），直接解决了仿真环境构建的关键瓶颈。对于从事机器人学习、具身智能或神经渲染的研究者具有高参考价值。

</details>

<details>
<summary>Abstract</summary>

Training embodied agents in the real world requires skilled operators and expensive hardware. Simulation environments offer a compelling alternative by enabling large-scale, cost-effective data augmentation. Consequently, rapidly constructing high-fidelity simulation scenes with a minimal sim-to-real gap has become a critical objective in robot learning. While reconstruction-based methods provide superior visual quality, current workflows are hindered by inefficient data acquisition and subpar foreground object extraction. We thus propose GASE, a highly automated system for simulation scene construction. GASE leverages multi-view video streams from panoramic camera arrays to enable rapid environment scanning. To ensure high-quality asset generation, our pipeline introduces a camera-pose-based strategy that robustly extracts objects across frames in the 2D domain, followed by high-fidelity scene inpainting. Foreground objects and the static background are then reconstructed independently and seamlessly imported into physics simulators for policy training. Extensive experiments demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation accuracy by over 10\% while achieving state-of-the-art inpainting quality. Furthermore, real-robot deployments across manipulation and navigation tasks maintains a performance gap of less than 10\% compared to policies trained purely on real-world data. These results confirm that GASE provides an efficient and highly effective solution for bridging the sim-to-real gap. Code will be released.

</details>

#### 2026-06-16 - Edit3DGS: Unified Framework for Dynamic Head Editing via 2D Instruction-Guided Diffusion and 3D Gaussian Splatting

**Authors:** Duy-Dat Tran, Trung-Nghia Le
**Links:** [abs](https://arxiv.org/abs/2606.17432) - [pdf](https://arxiv.org/pdf/2606.17432)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic 3D, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Edit3DGS: Unified Framework for Dynamic Head Editing via 2D Instruction-Guided Diffusion and 3D Gaussian Splatting
- 作者：Duy-Dat Tran, Trung-Nghia Le
- 出版日期：2026-06-16
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.17432

### 一句话总结
Edit3DGS是一个将2D指令引导扩散模型与3D高斯泼溅技术结合的统一框架，用于对动态三维头部进行语义可控、时序连贯的编辑。

### 研究问题
如何实现动态3D头部的高保真编辑，使其既能通过文本指令进行语义控制，又能保持身份、运动动态和时间一致性，同时避免帧间伪影。

### 核心思路/方法
1. 利用文本条件扩散模型对视频中可编辑面部区域进行掩码和修改，支持表情变换、属性修改和外观精修等精细操作。
2. 将编辑后的帧通过3D高斯泼溅聚合为连贯、高保真的动态头像。
3. 引入多视角批量编辑和轻量级修复策略，以恢复跨时间步长丢失的表情，增强时空一致性。

### 主要贡献
- 提出一个统一框架，整合了2D指令驱动的语义控制与3D高斯泼溅的逼真重建。
- 实现了无伪影、时序平滑的动态头部编辑，支持多种编辑操作（表情、属性、外观）。
- 框架可应用于虚拟化身、沉浸式通信、电影制作和交互媒体等场景。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文提出的方法在动态3D头部编辑领域兼具语义可控性与时序一致性，且应用场景广泛；方法整合了当前热门的扩散模型与3D高斯泼溅技术，技术新颖性高。

</details>

<details>
<summary>Abstract</summary>

We present Edit3DGS, a unified framework for dynamic 3D head editing that integrates 2D instruction-guided diffusion with 3D Gaussian splatting. Unlike prior approaches that separately address frame-based edits or static 3D reconstruction, our method couples semantic controllability in the image domain with photorealistic, temporally consistent 3D representations. Given an input video, editable facial regions are masked and modified using a text-conditioned diffusion model to support fine-grained operations such as expression transformation, attribute modification, and appearance refinement. The edited frames are then aggregated through 3D Gaussian splatting to produce a coherent, high-fidelity avatar that preserves both identity and motion dynamics. To enforce consistency, Edit3DGS incorporates multi-view batch editing and lightweight inpainting strategies that recover lost expressions across timesteps. Experimental results demonstrate that our framework enables controllable, artifact-free head editing with smooth temporal transitions, offering practical applications in virtual avatars, immersive communication, film production, and interactive media.

</details>

#### 2026-06-16 - TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations

**Authors:** Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan
**Links:** [abs](https://arxiv.org/abs/2606.17386) - [pdf](https://arxiv.org/pdf/2606.17386)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations
- 作者：Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan
- 出版日期：2026-06-16
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.17386；PDF: https://arxiv.org/pdf/2606.17386

### 一句话总结
本文提出TerraTransfer方法，通过在向量化模拟器中自博弈训练策略，再将其与预训练视觉骨干网络对齐，实现了无需专家示范的端到端驾驶。

### 研究问题
如何在不依赖昂贵的人工标注和专家演示数据的情况下，高效训练端到端自动驾驶策略，并降低训练成本（包括数据收集和闭环强化学习的计算开销）。

### 核心思路/方法
将“学习驾驶”与“学习视觉”解耦：1）在向量化模拟器中进行快速自博弈（self-play）训练，生成包含碰撞、近碰撞和恢复等丰富状态分布的驾驶策略；2）通过动作KL散度和批量关系低秩结构损失，将自博弈策略的潜在空间与预训练视觉骨干网络对齐，仅需配对（图像，场景状态）数据，无需专家轨迹监督。

### 主要贡献
1. 提出利用向量化模拟器的低成本自博弈替代昂贵实车数据采集和闭环图像RL训练。
2. 设计了一种对齐机制，使自博弈学习的驾驶策略能迁移到视觉输入上，无需专家示范。
3. 在基于3D高斯溅射的逼真闭环场景中，端到端策略获得了匹配或超越现有方法的性能。

### 局限性
摘要未提供足够信息，例如：在真实世界或复杂动态场景下的泛化能力、对齐过程的收敛性保证、以及未与大规模实际路测结果的对比。

### 阅读优先级
中。理由：该方法在降低端到端自动驾驶训练成本（无需专家演示）方面提出了新颖的解耦思路，对关注训练效率和数据成本的读者有参考价值；但摘要未提供充分的实验对比和泛化性分析，需进一步阅读全文评估实用性。

</details>

<details>
<summary>Abstract</summary>

End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all stages: collecting and labeling millions of driving frames is costly, and closed-loop RL on images is bottlenecked by the per-step cost of photorealistic rendering plus a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: millions of rollout steps per second, and a state distribution naturally rich in collisions, near-misses, and recoveries that no driving log contains. Our approach exploits this asymmetry by decoupling learning to drive from learning to see. We pretrain a single policy by self-play, then align its latent space with a pretrained vision backbone, through the action KL divergence and a batch-relational low-rank structural loss. The action target comes from the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. On photorealistic 3D Gaussian splatting closed-loop scenarios, the resulting end-to-end policy matches or exceeds prior end-to-end methods.

</details>

#### 2026-06-15 - BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering

**Authors:** Yi-Ruei Liu, Jie-Ying Lee, Zheng-Hui Huang, Yu-Lun Liu, Chih-Hao Lin
**Links:** [abs](https://arxiv.org/abs/2606.17049) - [pdf](https://arxiv.org/pdf/2606.17049)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** inverse rendering, relighting, rendering, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering
- 作者：Yi-Ruei Liu, Jie-Ying Lee, Zheng-Hui Huang, Yu-Lun Liu, Chih-Hao Lin
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering (主)；Embodied / Robotics / AR Applications (次)
- 链接：摘要页 [https://arxiv.org/abs/2606.17049](https://arxiv.org/abs/2606.17049) | PDF [https://arxiv.org/pdf/2606.17049](https://arxiv.org/pdf/2606.17049)

### 一句话总结
BRDFusion 将物理渲染（PBR）与生成式模型融合，实现高质量、可控的城市场景逆向渲染与正向渲染，支持重光照、夜间模拟和动态物体编辑。

### 研究问题
如何解决物理渲染方法在城市场景逆向渲染中存在的重建与渲染伪影，同时克服生成模型一致性和可控性不足的问题，以实现高质量且可控的视频生成。

### 核心思路/方法
提出一个统一框架，结合两种互补模型：
1. **逆向渲染阶段**：使用物理建模恢复显式、一致的场景属性（如材质、光照），并利用生成先验缓解优化歧义。
2. **正向渲染阶段**：物理模型从场景配置提供可控渲染，生成模型负责去噪和修复伪影。二者协同工作，实现高保真视频输出。

### 主要贡献
- 将物理渲染与生成模型有机结合，取长补短。
- 在真实与合成场景中获得了优于基线方法的视频质量。
- 支持新颖视角重光照、夜间模拟、动态物体插入/编辑等高级功能。

### 局限性
摘要未提供关于方法计算开销、对训练数据规模要求、失败案例（如极端光照或复杂几何）等局限性信息。

### 阅读优先级
**中**
理由：该工作解决了城市场景逆向渲染中的实用问题，方法巧妙结合物理与生成范式，但摘要未展示定量实验结果或具体实施细节，且2026年的论文相对较新，需谨慎评估其可比性与可复现性。如果对可编辑渲染或城市仿真感兴趣，则值得深入原文阅读。

</details>

<details>
<summary>Abstract</summary>

Inverse rendering of urban scenes from captured videos enables numerous applications, including content creation and autonomous driving simulation. Physically-based rendering methods follow and control lighting physics, but suffer from reconstruction and rendering artifacts. While generative models produce realistic videos, they offer limited consistency and controllability. We present BRDFusion, a unified framework that combines two complementary models for inverse and forward rendering. Specifically, BRDFusion recovers explicit, consistent scene properties with physical modeling and alleviates optimization ambiguity with generative priors. During forward rendering, the physical model provides controllable rendering from the scene configuration, and the generative model denoises and fixes artifacts. Therefore, our method produces high-quality videos while allowing precise control, outperforming baselines in real and synthetic scenes. Moreover, BRDFusion supports novel-view relighting, night simulation, and dynamic object insertion/editing. Project page: https://shigon255.github.io/brdfusion-page/

</details>

#### 2026-06-15 - Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence

**Authors:** Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu
**Links:** [abs](https://arxiv.org/abs/2606.16566) - [pdf](https://arxiv.org/pdf/2606.16566)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence
- 作者：Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2606.16566; PDF: https://arxiv.org/pdf/2606.16566

### 一句话总结
Local-GS 通过针对SIMT执行边界的瓦片级warp一致性优化，显著加速了3D高斯泼溅的渲染过程。

### 研究问题
如何解决3D高斯泼溅中因高斯原语不规则空间分布导致的GPU利用率低下、warp发散和冗余计算问题，以提升渲染效率。

### 核心思路/方法
提出一种warp一致的渲染范式，将高斯原语组织为与SIMT执行边界对齐的形式，而非依赖场景几何。具体包括三个warp一致的阶段：
1. **提升阶段（hoisting stage）**：在瓦片级别预计算共享参数。
2. **剔除阶段（culling stage）**：丢弃无贡献的warp。
3. **混合阶段（blending stage）**：将逐像素分支替换为统一指令流。

### 主要贡献
- 提出Local-GS，一种通过瓦片级warp一致性加速3DGS的即插即用优化方法。
- 在多个数据集的基准测试中，在不牺牲质量的前提下提升了效率。
- 在所有测试基线上均带来额外性能增益，例如在Deep Blending场景上实现7.76倍加速。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法针对3DGS渲染效率这一具体工程优化问题，提出创新性的warp一致性策略，对于从事神经渲染或GPU优化的研究者具有参考价值，但未涉及算法理论突破，可结合具体场景决定是否深入阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has significantly advanced real-time novel view synthesis by representing scenes as dense collections of anisotropic 3D Gaussian primitives. However, the irregular spatial distribution of Gaussians often leads to poor GPU utilization, as warp divergence and redundant computation degrade rendering performance. To address this, we present Local-GS, a warp-coherent rendering paradigm that, organizes Gaussian primitives with respect to SIMT (Single Instruction, Multiple Threads) execution boundaries rather than scene geometry. Specifically, we propose three warp-coherent stages: a hoisting stage that precomputes shared parameters at tile level, a culling stage that discards warps with no contribution, and a blending stage that replaces per-pixel branching with a uniform instruction stream. Across extensive benchmarks on multiple datasets, Local-GS improves efficiency without compromising quality. As a plug-and-play optimization, it provides additional performance gains to all tested baselines, culminating in a $7.76\times$ speedup on Deep Blending scenes.

</details>

#### 2026-06-15 - RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos

**Authors:** Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li
**Links:** [abs](https://arxiv.org/abs/2606.16278) - [pdf](https://arxiv.org/pdf/2606.16278)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos
- 作者：Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2606.16278

### 一句话总结
提出RealityBridge框架，用于修复和增强可编辑3D高斯泼溅（3DGS）仿真驾驶视频，弥合其与真实世界视频之间的Sim-to-Real差距。

### 研究问题
如何修复可编辑3DGS驾驶仿真视频中存在的渲染伪影、前景资产退化、光照不一致和时序闪烁等Sim-to-Real差距，同时保持结构完整性和资产一致性。

### 核心思路/方法
1. 采用多模态控制输入（渲染视频、前景掩码、边缘图、语义掩码）作为条件。
2. 引入轻量级GateNet模块，实现自适应条件分配到骨干网络各层。
3. 构建针对性训练数据，并采用自回归长视频训练策略。
4. 使用奖励引导的后训练（reward-guided post-training）来提升修复质量、时间稳定性和幻觉抑制。

### 主要贡献
1. 提出首个结构保持且资产感知的Sim-to-Real框架，专用于编辑后的3DGS驾驶视频。
2. 设计多模态控制与自适应条件分配机制（GateNet），有效处理多种伪影和光照问题。
3. 通过自回归长视频训练和奖励引导后训练，显著提升时序一致性和视觉真实性。
4. 在内部和公开驾驶数据集上的实验表明，该方法在伪影去除、光照和谐化及长序列时序一致性上优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。
理由：该工作针对自动驾驶安全关键的稀有场景仿真问题，提出了结合3DGS编辑与视频修复的新框架，方法设计具有创新性（多模态控制+自回归训练+奖励引导），涉及当前热门的3DGS与Sim-to-Real交叉领域，且实验结果明确优于现有方法，对自动驾驶和神经渲染方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Long-tail hazardous scenarios are essential for safety-oriented autonomous driving, yet they are difficult to collect and reproduce at scale. Editable 3D Gaussian Splatting (3DGS) simulation offers a promising alternative by reconstructing real driving scenes and supporting controllable scene editing. However, edited 3DGS-rendered videos still suffer from a significant Sim-to-Real gap, including rendering artifacts, degraded foreground assets, inconsistent illumination, and temporal flickering. Existing restoration and video generation methods are insufficient for this task, as they often fail to jointly repair 3DGS-specific artifacts, improve visual realism, and ensure temporal consistency. To fill this gap, we propose RealityBridge, a structure-preserving and asset-aware Sim-to-Real framework for edited 3DGS driving videos. RealityBridge uses multimodal controls, including rendered videos, foreground masks, edge maps, and semantic masks, together with a lightweight GateNet for adaptive condition allocation across backbone layers. We further construct targeted training data and introduce autoregressive long-video training with reward-guided post-training to improve restoration quality, temporal stability, and hallucination suppression. Extensive experiments on internal and public driving datasets show that RealityBridge outperforms existing methods in artifact removal, illumination harmonization, and long-sequence temporal consistency.

</details>

#### 2026-06-15 - PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation

**Authors:** Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou
**Links:** [abs](https://arxiv.org/abs/2606.16232) - [pdf](https://arxiv.org/pdf/2606.16232)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation  
- 作者：Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou  
- 出版日期：2026-06-15  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2606.16232  

### 一句话总结  
该工作提出PolyMerge方法，将高保真3D高斯泼溅场景模型转换为轻量级凸多面体覆盖表示，在资源受限的无人机上实现可证明安全的实时避障导航。

### 研究问题  
如何压缩大容量、高计算量的3DGS场景模型，使其能在计算资源严重受限的嵌入式平台上实时生成安全轨迹，同时保证碰撞避免的数学可证性。

### 核心思路/方法  
- 将原始3DGS模型中的所有障碍物用一组凸多面体的并集进行可证明的过近似覆盖（即每个多面体完全包含障碍物，且并集不遗漏任何障碍）。  
- 通过调节凸多面体的数量来权衡保守程度（覆盖精度）与计算代价。  
- 与控制障碍函数（CBF）集成，以该多面体覆盖作为约束条件，规划出无碰撞路径。

### 主要贡献  
1. 提出PolyMerge：一种将3DGS场景压缩为可证明覆盖所有障碍的凸多面体表示的方法。  
2. 该方法能灵活控制多面体数量，在安全保守性与计算需求之间做权衡。  
3. 在Crazyflie微型无人机上实现实时轨迹规划与跟踪，在严苛机载计算约束下保证碰撞安全，且速度快于基线方法。  
4. 提供了模拟和硬件实验验证，并公开代码与演示视频。

### 局限性  
摘要未提供足够信息，无法判断具体局限性（如多面体覆盖的保守性程度对路径可行性的影响、是否依赖特定场景结构、3DGS模型精度损失等）。

### 阅读优先级  
高  
理由：该工作直接解决了3DGS在高动态、资源受限机器人（如微型无人机）上应用的瓶颈问题，结合了可证明安全（CBF）与实时性，与神经场景表示在机器人导航中的落地紧密相关，具有明显的实际应用与理论价值。

</details>

<details>
<summary>Abstract</summary>

Obstacle avoidance is essential for safe navigation and motion planning. Recent radiance field reconstruction methods enable object detection and modeling with high fidelity, but remain too memory- and compute-intensive for on-board perception-based path planning. To address these limitations, we propose PolyMerge to convert a large, photorealistic 3D Gaussian Splatting (3DGS) model of a scene into a lightweight representation of convex polytopes whose union provably over-approximates all obstacles in the original 3DGS model. PolyMerge tunes the polytope count to trade off conservativeness and compute cost, and integrates with control barrier functions (CBFs) to plan collision-free paths. We showcase PolyMerge in simulation and hardware experiments on a Crazyflie drone, which uses PolyMerge to compute and follow safe trajectories in real time under severe onboard compute constraints, outperforming baselines in speed while guaranteeing safety. For our code and videos, visit https://athlon76.github.io/PolyMerge-website/.

</details>

#### 2026-06-15 - Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing

**Authors:** Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Kunyang Huang, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.16168) - [pdf](https://arxiv.org/pdf/2606.16168)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing
- 作者：Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Kunyang Huang, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.16168；PDF：https://arxiv.org/pdf/2606.16168

### 一句话总结
本文提出了一种频率感知的隐式高斯泼溅网络（Fi-Gaussian），通过频域解耦和物理散射重归一化机制，提升单张图像去雾的细节恢复效果。

### 研究问题
单张图像去雾任务中，高频细节丢失以及准确的物理散射建模困难。

### 核心思路/方法
1. 采用隐式高斯泼溅（Implicit Gaussian Splatting）在2D特征空间中连续表示清晰图像的潜在分布，替代显式3D点云渲染。
2. 设计频率感知隐式高斯泼溅模块，在频域中解耦低频结构信息和高频纹理信息，并使用复数值权重进行自适应高斯聚合，以恢复精细细节。
3. 引入物理驱动的散射重归一化机制，在隐式高斯先验指导下估计透射图和大气光。

### 主要贡献
1. 提出Fi-Gaussian网络，首次将隐式高斯泼溅应用于单张图像去雾，验证了其在低级视觉任务中的有效性。
2. 通过频率感知解耦和复数值高斯聚合，显著提升高频纹理的恢复质量。
3. 结合物理散射重归一化机制，在多个基准数据集上取得最优定量性能，并生成视觉上更优的去雾结果。

### 局限性
摘要未提供足够信息，例如模型的计算复杂度、对极端雾霾场景的鲁棒性、不同数据集上的具体性能差异、与现有方法的详细对比数值等。

### 阅读优先级
中。理由：该方法在去雾任务中引入了频域感知与隐式高斯泼溅的新颖结合，对关注低级视觉和神经渲染的读者有参考价值，但内容相对专精且发表于2026年，若非直接相关领域，优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Single image dehazing continues to be hindered by the loss of high-frequency details and the difficulty of accurate physical scattering modeling. To address these issues, we propose Fi-Gaussian, a frequency-aware implicit Gaussian splatting network for single image dehazing. Unlike explicit rendering methods that rely on 3D point clouds, our method employs implicit Gaussian splatting to adaptively model the underlying distribution of clear images as a continuous representation in 2D feature space. The core of the network is a frequency-aware implicit Gaussian splatting module, which decouples low-frequency structural information and high-frequency texture information in the frequency domain and then performs adaptive Gaussian aggregation with complex-valued weights to recover fine details. In addition, a physics-driven scattering renormalization mechanism is introduced to estimate the transmission map and atmospheric light under the guidance of implicit Gaussian priors. Extensive experiments on multiple benchmark datasets demonstrate that Fi-Gaussian achieves state-of-the-art quantitative performance and produces visually superior dehazed results, validating the effectiveness of implicit Gaussian splatting for low-level vision tasks.

</details>

#### 2026-06-15 - Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation

**Authors:** Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.16163) - [pdf](https://arxiv.org/pdf/2606.16163)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation
- 作者：Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-15
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：[摘要](https://arxiv.org/abs/2606.16163) | [PDF](https://arxiv.org/pdf/2606.16163)

### 一句话总结
本文提出首个将2D高斯泼溅（2DGS）引入图像去雾领域的零样本框架Dehaze-GaussianImage，通过可演化的各向异性高斯场建模雾图，并以无监督方式实现物理可解释的高效去雾。

### 研究问题
现有单图像去雾方法在像素级优化中存在计算冗余，且隐式神经网络缺乏物理可解释性，导致表示效率与重建保真度难以平衡。本文旨在突破传统像素网格处理范式，提升去雾的表示效率和重建质量。

### 核心思路/方法
- 将雾图建模为连续且动态可演化的各向异性高斯场，取代传统CNN或Transformer的静态网格处理。
- 提出一种新颖的重建-解耦零样本学习策略，将大气散射模型嵌入高斯参数空间，驱动高斯基元在优化过程中自适应地分裂、克隆和剪枝，从而实现传输介质与清晰纹理的几何级解耦。
- 引入显式结构保持约束，抑制传统物理先验常见的伪影。

### 主要贡献
- 首次将2D高斯泼溅引入图像去雾领域，提出零样本去雾框架Dehaze-GaussianImage，打破了像素网格处理范式。
- 提出重建-解耦零样本学习策略，将大气散射模型融入高斯参数空间，实现几何级解耦。
- 实验表明，该方法在完全无监督、参数极少的条件下达到最先进（SOTA）性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该方法在零样本去雾领域提出新颖的高斯表示范式，具有较好的创新性和理论价值；但摘要缺乏定量实验对比细节，也未说明泛化到其他视觉任务或真实场景的挑战，因此属于中等优先级的参考阅读。

</details>

<details>
<summary>Abstract</summary>

Existing single image dehazing methods are often constrained by computational redundancy in pixel-level optimization and the lack of physical interpretability in implicit neural networks. These limitations hinder the balance between representation efficiency and reconstruction fidelity. To address these issues, we propose Dehaze-GaussianImage, the first zero-shot framework that introduces 2D Gaussian Splatting (2DGS) into the image dehazing domain to break the traditional pixel-grid processing paradigm. Distinct from static convolutional neural networks (CNNs) or Transformers, our approach models hazy images as continuous and dynamically evolvable anisotropic Gaussian fields. Specifically, we propose a novel reconstruction-decoupling zero-shot learning strategy that embeds the atmospheric scattering model into the Gaussian parameter space. This strategy drives Gaussian primitives to adaptively split, clone, and prune during optimization, achieving geometric-level decoupling of the transmission medium and clear textures. Furthermore, explicit structure-preserving constraints are introduced to suppress artifacts commonly caused by traditional physical priors. Experimental results demonstrate that the proposed method achieves state-of-the-art (SOTA) performance in a fully unsupervised manner with minimal parameters, highlighting the potential of explicit Gaussian representation for low-level vision tasks.

</details>

#### 2026-06-15 - Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement

**Authors:** Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2606.16159) - [pdf](https://arxiv.org/pdf/2606.16159)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement
- 作者：Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li
- 出版日期：2026-06-15
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.16159

### 一句话总结
提出首个基于显式-隐式联合建模的低光图像增强框架CGS-Retinex，通过连续高斯泼溅估计全局光照分布，并利用隐式神经表示独立建模反射率，以解决低光增强中的颜色失真和结构伪影问题。

### 研究问题
低光图像增强中，现有方法难以在全局平滑光照调整与局部高频细节恢复之间取得平衡，常导致颜色失真和结构伪影。

### 核心思路/方法
1. **连续高斯渲染器**：将图像网格表示为连续参数场，用于估计空间连续的全局光照分布，从而消除离散高斯采样导致的网格伪影。
2. **隐式反射率建模**：引入隐式神经表示独立建模反射率，利用浅层高频特征指导网络准确重建退化纹理细节。
3. **Retinex框架约束**：在Retinex理论框架中，引入物理启发的亮度一致性约束和光照平滑正则化，使显式光照和隐式反射率能保持恰当曝光，并高保真恢复高频结构与颜色。

### 主要贡献
- 首次将连续高斯泼溅与Retinex理论深度结合，建立显式-隐式联合建模的低光增强框架。
- 提出连续高斯渲染器消除离散采样伪影，并通过隐式神经表示独立恢复高频纹理。
- 实验表明该方法能显著抑制暗区噪声和过曝，实现优异的高频结构保真度和颜色恢复。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作为低光图像增强引入了全新的连续物理表示范式（连续高斯泼溅+隐式神经表示），方法具有创新性，且针对颜色失真和结构伪影等核心难题提出了系统性解决方案，适合关注图像增强、神经渲染及Retinex理论的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Low-light image enhancement aims to recover clear images from low-illumination observations and is crucial for high-level downstream vision tasks. However, existing methods frequently encounter color distortion and structural artifacts when balancing global smooth illumination adjustment and local high-frequency detail recovery. To address these issues, we propose CGS-Retinex as the first low-light image enhancement framework based on explicit-implicit joint modeling. Our framework deeply integrates continuous Gaussian splatting with Retinex theory. Specifically, we represent the image grid as a continuous parameter field and propose a continuous Gaussian renderer to estimate the spatially continuous global illumination distribution. This approach fundamentally eliminates grid artifacts caused by discrete Gaussian sampling. Furthermore, we introduce an implicit neural representation to model reflectance independently. We leverage shallow high-frequency features to guide the network in accurately reconstructing degraded texture details. Within the Retinex framework, we incorporate physics-inspired brightness consistency constraints and illumination smoothness regularization to enable explicit illumination and implicit reflectance to maintain proper exposure and achieve high-fidelity recovery of high-frequency structures and colors. Extensive experiments demonstrate that CGS-Retinex significantly suppresses dark-region noise and overexposure while achieving exceptional high-frequency structural fidelity and color restoration by precisely decoupling illumination and texture. This work establishes a novel continuous physical representation paradigm for low-light image enhancement.

</details>

#### 2026-06-14 - TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization

**Authors:** Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu
**Links:** [abs](https://arxiv.org/abs/2606.15924) - [pdf](https://arxiv.org/pdf/2606.15924)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization
- 作者：Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu
- 出版日期：2026-06-14T16:59:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.15924；PDF：https://arxiv.org/pdf/2606.15924

### 一句话总结
TurboGS 是一个通过错误引导的稀疏像素采样和优化来加速 3D 高斯泼溅（3DGS）训练的训练框架，能够在单张 RTX 5090 GPU 上 100 秒内实现与原始 3DGS 相当或更优的新视角渲染质量，训练速度提升高达 10 倍。

### 研究问题
如何在保持高保真渲染质量的前提下，加速 3D 高斯泼溅（3DGS）的训练优化过程，以减少处理冗余像素和牺牲细节的问题。

### 核心思路/方法
TurboGS 基于四个核心组件构建：
1.  **基于块的稀疏像素采样**：利用训练过程中的多视图重建误差，优先处理困难区域（挑战区域），跳过已良好重建的区域，避免冗余梯度计算。
2.  **基于块的结构感知损失与稀疏归一化互相关（NCC）**：提供稀疏但有效的监督信号，以保留精细细节并稳定训练。
3.  **错误驱动的密度控制策略**：动态分配模型容量，移除冗余的高斯原语，控制模型复杂度。
4.  **定制化混合优化器**：结合 Hessian 引导的更新与 Adam 动量衰减，在稀疏监督下稳定并改善收敛。

### 主要贡献
- 提出了 TurboGS，一个基于错误引导稀疏像素采样和优化的 3DGS 加速训练框架。
- 通过四大核心组件（稀疏采样、结构感知损失、密度控制、混合优化器）协同工作，显著减少计算冗余。
- 实验证明，在单张 RTX 5090 GPU 上，TurboGS 能在 100 秒内取得与原始 3DGS 相当或更优的渲染质量，实现高达 10 倍的训练加速。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作直接针对 3DGS 的训练效率瓶颈，提出了一个端到端的加速框架，在保持质量的同时实现了数量级的速度提升（10倍），且发表在 2026 年，具有很强的时效性和实用性，尤其适合关注高效神经渲染和实时应用的读者。

</details>

<details>
<summary>Abstract</summary>

Consumer-level applications require fast optimization of 3D Gaussian Splatting (3DGS) with high-fidelity novel view rendering. However, existing 3DGS acceleration approaches still incur substantial computation on redundant pixels while sacrificing fine details. In this paper, we present TurboGS, an error-guided training framework that accelerates 3DGS by concentrating optimization on perceptually informative pixels. TurboGS is built upon four core components: (1) a tile-wise sparse pixel sampling, which, driven by multi-view reconstruction errors during training, prioritizes challenging regions and skips well-reconstructed ones to avoid redundant gradient computation; (2) a tile-wise structure-aware loss with sparse Normalized Cross-Correlation, which provides sparse yet effective supervision to preserve fine details and stabilize training; (3) an error-driven Gaussian density control strategy, which dynamically allocates model capacity and removes redundant primitives; and (4) a tailored hybrid optimizer that couples Hessian-informed updates with Adam moment damping to stabilize and improve convergence under sparse supervision. Experiments on standard benchmarks demonstrate that TurboGS can deliver on par or superior rendering quality within 100 seconds on a single RTX 5090 GPU card (up to 10x training speedup over vanilla 3DGS).

</details>

#### 2026-06-14 - EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units

**Authors:** Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen
**Links:** [abs](https://arxiv.org/abs/2606.15848) - [pdf](https://arxiv.org/pdf/2606.15848)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units
- 作者：Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen
- 出版日期：2026-06-14
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.15848

### 一句话总结
本文提出EmoZone-Talker框架，通过区域语义控制和面部动作单元（AU），解决音频驱动3DGS说话头在表情控制中的空间纠缠和时间不稳定问题，实现精细、可解释的面部动画。

### 研究问题
如何在高保真音频驱动的3DGS说话头合成中，实现精细、可编辑且时空稳定的面部表情控制，克服语音驱动动态与显式表情信号之间的内在冲突。

### 核心思路/方法
1. 提出 **Synergy Zones with Prioritized Attention Bias (SZ-PAB)**，利用解剖先验约束区域级模态贡献，显式解耦音频和表情信号的贡献。
2. 提出 **Channel-Independent Temporal AU Encoder (CIT-AE)**，对动作单元（AU）的时序动态进行独立通道建模，保证时间一致性。
3. 将上述解耦的区域AU表示集成到3D高斯变形中，实现精确、可解释的面部表情控制。

### 主要贡献
- 将音频驱动面部动画重新构造为跨模态冲突下的结构化时空协调问题。
- 提出SZ-PAB和CIT-AE两种模块，实现显式的空间解耦和时序动态建模。
- 实验表明，该方法在表情可控性、真实感、上脸精确度和时间一致性上均有提升，同时保持高渲染质量和准确唇同步。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对3DGS说话头合成中的关键问题（表情控制的可解释性与时空稳定性），提出了结构化的新框架，实验效果显著，且代码将开源，对领域研究和应用有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has shown strong potential for high-fidelity talking head synthesis. However, enabling fine-grained, interpretable, and editable facial expression control remains fundamentally challenging due to intrinsic conflicts between speech-driven facial dynamics and explicit expression signals. Existing methods rely on implicit multimodal fusion, leading to spatial entanglement and temporal instability. We present EmoZone-Talker, a novel framework that reformulates audio-driven facial animation as a structured spatial-temporal coordination problem under cross-modal conflicts. Our approach introduces an explicit spatial disentanglement and temporal dynamics modeling of facial motion. Specifically, we propose Synergy Zones with Prioritized Attention Bias (SZ-PAB) to explicitly decouple modality contributions via region-wise constraints guided by anatomical priors, and a Channel-Independent Temporal AU Encoder (CIT-AE) to model temporally coherent AU dynamics. By integrating these representations into 3D Gaussian deformation, EmoZone-Talker enables precise and interpretable control over facial expressions. Extensive experiments demonstrate that our method improves expression controllability and realism, with notable gains in upper-face accuracy and temporal coherence, while preserving high rendering quality and accurate lip synchronization. Code will be publicly released to facilitate reproducibility and further research.

</details>

#### 2026-06-14 - SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction

**Authors:** Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao
**Links:** [abs](https://arxiv.org/abs/2606.15659) - [pdf](https://arxiv.org/pdf/2606.15659)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction
- 作者：Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao
- 出版日期：2026-06-14T07:55:57Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.15659

### 一句话总结
本文提出SpatialAvatar-0，一种基于FLAME网格绑定高斯表示的多阶段重建框架，通过前馈生成器和布局保持的逐主体精炼，实现高质量4D头部虚拟形象重建，并在多个基准上取得领先性能。

### 研究问题
如何从单张或少数源肖像出发，高效重建高质量4D头部虚拟形象，并弥合前馈预测器（可泛化）和逐主体精炼器（需大量迭代）两种范式之间的鸿沟。

### 核心思路/方法
1. **共享的FLAME网格绑定高斯表示**：将3D高斯绑定到FLAME网格上，使前馈生成和逐主体精炼共用同一表示，避免表示不兼容。
2. **前馈生成器**：使用参数自由的K源均值池化（parameter-free K-source mean-pool）处理可变数量的输入源，并采用单目时间到多视角空间的两阶段调度策略（monocular-temporal to multi-view-spatial two-phase schedule），防止身份先验在小规模多视图集上坍塌。
3. **布局保持的逐主体精炼**：仅需10K次迭代的精炼流程，冻结FLAME绑定和高斯数量，用三分量抗尖峰正则化（three-component anti-spike regularization）替代传统的自适应稠密化，从而保留前馈阶段的高斯布局。

### 主要贡献
1. 提出了前馈生成与逐主体精炼共享同一FLAME网格绑定高斯表示的框架，首次实现两种范式的端到端兼容。
2. 设计了一种参数自由的K源均值池化机制，支持可变数量的输入源，减少对固定源数训练数据的依赖。
3. 引入10K次迭代的布局保持精炼流程，相比传统300K-600K迭代方法显著降低计算成本，同时提升指标（如超过GeoAvatar +1.3 dB PSNR）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作在4D虚拟形象重建这一活跃方向上提出了统一前馈与精炼的新思路，性能提升显著（PSNR+1.3~1.5 dB），且训练效率提升高达60倍，对AR/VR和数字人领域的实践有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

High-quality 4D head avatars from one or a few source portraits are central to telepresence, AR/VR, and digital-human interaction. 3D Gaussian Splatting (3DGS) has emerged as the dominant representation, with two complementary regimes (generalizable feed-forward predictors and per-subject refiners) maturing in parallel. However, existing feed-forward predictors are trained on a single dataset family with a hard-coded source count, inheriting the corresponding domain bias. Per-subject refiners require 300K--600K iterations and rely on adaptive densification that destroys upstream Gaussian layouts, preventing the two regimes from sharing a representation end-to-end. To bridge both regimes we propose SpatialAvatar-0 on a shared FLAME-mesh-bound Gaussian representation: a feed-forward generator with a parameter-free K-source mean-pool and a monocular-temporal to multi-view-spatial two-phase schedule that anchors against identity-prior collapse onto the smaller multi-view set. We further introduce a 10K-iter layout-preserving per-subject refinement loop that freezes the FLAME-binding and Gaussian count and replaces densification with a three-component anti-spike regularization. On VFHQ/HDTF cross-domain zero-shot we surpass the in-domain leader GAGAvatar by +1.5 dB PSNR despite never training on either test domain, and on the SplattingAvatar monocular benchmark we lead every reported metric, surpassing the 300K-iter GeoAvatar by +1.3 dB PSNR at up to 60x shorter per-subject schedule than common SOTA baselines. Website: https://spatialwalk.github.io/SpatialAvatar-0.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-16 - OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation

**Authors:** Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang
**Links:** [abs](https://arxiv.org/abs/2606.17536) - [pdf](https://arxiv.org/pdf/2606.17536)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation
- 作者：Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang
- 出版日期：2026-06-16T05:25:55Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.17536

### 一句话总结
本文提出名为DRIVE-CHOREO的LLM编排多智能体世界模型，通过统一潜在共压缩机制解决多视角驾驶视频生成中异构控制注入和后处理跨视角融合问题，在nuScenes上取得新SOTA。

### 研究问题
自主驾驶生成式世界模型面临两个未解决冲突：1）异构控制注入——自然语言、高清地图、轨迹、相机位姿等表征空间不兼容；2）后处理跨视角融合——每个相机的潜在编码无法编码全局3D几何。

### 核心思路/方法
核心思想是将可控多视角视频生成重新定义为潜在编排（latent choreography），使用三个Qwen2.5-VL智能体协作：
- **Director**（导演）：将用户意图解析为结构化WorldScript。
- **Cartographer**（制图师）：将WorldScript转化为空间锚定的布局标记。
- **Auditor**（审核员）：提供跨视角反馈作为辅助监督。
三个智能体共同生成一个位置感知的标记序列，该序列通过视图-时间排列与多视角视频共压缩，在3D VAE的卷积感受野中强制实现相机间几何一致性。

### 主要贡献
1. 提出DRIVE-CHOREO方法，将LLM编排与多智能体世界模型结合，统一处理语言、几何和像素的潜在对齐。
2. 在nuScenes数据集上，多视角一致性和BEV mAP达到新SOTA（21.6），FVD为45.7。
3. 纯用合成数据训练的检测器在真实验证集上获得+2.4 NDS提升，验证了下游实用性。

### 局限性
摘要未提供不足够信息：未提及计算开销、对异常场景的鲁棒性、模型在不同天气/光照条件下的泛化能力，以及智能体协作的具体失败案例分析。

### 阅读优先级
**中**。该工作结合LLM与生成式世界模型，在自动驾驶视频生成和多视角一致性问题上有显著改进，但属于较专业的分支领域。若研究方向与多模态视频生成、world model、自动驾驶仿真相关，则阅读优先级可提升。

</details>

<details>
<summary>Abstract</summary>

Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-choreographed multi-agent world model that recasts controllable multi-view video generation as latent choreography. Three Qwen2.5-VL agents - a Director parsing user intent into a structured WorldScript, a Cartographer grounding it into spatially-anchored layout tokens, and an Auditor feeding cross-view critiques back as auxiliary supervision - jointly author a single position-aware token sequence. This sequence is co-compressed with the multi-view video via a view-time permutation that enforces inter-camera geometry within the convolutional receptive field of a 3-D VAE. On nuScenes, DRIVE-CHOREO sets new state-of-the-art multi-view consistency and BEV mAP (21.6) with competitive FVD (45.7); a detector trained purely on our synthetic data gains +2.4 NDS on the real validation split, validating downstream utility.

</details>

#### 2026-06-16 - AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation

**Authors:** Haoran Lu, Mutian Shen, Shuyang Yu, Yu Xiao, Songling Liu, Jianshu Zhang, Shang Wu, Yue Chen, Guo Ye, Jiayi Wang, Zhaoran Wang, Han Liu
**Links:** [abs](https://arxiv.org/abs/2606.17446) - [pdf](https://arxiv.org/pdf/2606.17446)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation
- 作者：Haoran Lu, Mutian Shen, Shuyang Yu, Yu Xiao, Songling Liu, Jianshu Zhang, Shang Wu, Yue Chen, Guo Ye, Jiayi Wang, Zhaoran Wang, Han Liu
- 出版日期：2026-06-16
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.17446

### 一句话总结
AnnotateAnything 是一个通用自动标注框架，能将仅有几何结构的3D资产转换为附带语义、交互和物理操控标签的资产，支持机器人仿真数据收集。

### 研究问题
如何为机器人仿真中的原始3D资产自动生成结构化、多样化且可执行的操控标签（如抓取姿态、灵巧接触点、关节运动路径等），以替代仅依赖几何信息的被动资产。

### 核心思路/方法
构建两条互补的标注流水线：
1. **统一视觉-语言标注流水线**：利用视觉语言推理推断物体语义、交互约束和3D线索，提供人类先验指导以识别有意义的交互区域。
2. **全自动大规模并行物理标注流水线**：在视觉语言先验的基础上，通过候选生成、几何优化和轨迹生成，将先验信息与每个资产的几何及物理约束结合，生成多样化可执行的动作注释。

此外，基于生成的注释构建异步并行仿真数据收集系统，支持多种物体、任务和机器人形态。

### 主要贡献
- 提出了一个通用自动标注框架，将被动3D资产转化为“操控就绪”的资产。
- 设计了两条互补的标注流水线（视觉-语言推理管线 + 物理标注管线），兼顾语义先验和物理可执行性。
- 实验表明，该框架在标注效率、数据收集效率和任务成功率上均优于现有标注和数据生成流水线。
- 支持下游任务如功能区域检测、机器人视觉问答和视觉指令微调。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接面向机器人操作领域的核心瓶颈（3D资产缺乏交互语义标签），提出了通用自动化解决方案，并展现了跨多任务和机器人形态的实用性。摘要明确提供了与现有方法的性能对比，且计划开源代码和基准，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Simulation enables scalable robot data collection, but raw 3D assets provide only geometry, lacking the semantic, interactive, and physical knowledge needed to specify where and how robots should act. In this work, we present AnnotateAnything, a general automatic annotation framework that converts passive 3D assets into manipulation-ready assets with structured, diverse, and executable manipulation labels. AnnotateAnything is built around two complementary pipelines. First, a unified visual-language annotation pipeline using vision-language reasoning to infer object semantics, interaction constraints, and 3D-grounded cues, providing human-prior guidance for identifying meaningful interaction regions. Second, a fully automatic and massively parallel physics annotation pipeline grounds these priors in each asset's geometry and physical constraints through candidate generation, geometry optimization and trajectory generation. This pipeline produces diverse and executable action annotations, including grasp poses, dexterous contacts, articulation waypoints, insertion directions, hanging affordances, and navigation targets. Using the generated annotations, we further build an asynchronous parallel simulation data-collection system across diverse objects, tasks, and robot embodiments. Experiments demonstrate that AnnotateAnything achieves superior annotation efficiency, data-collection efficiency, and task success rates over existing annotation and data-generation pipelines, while also supporting downstream tasks such as affordance detection, robotic VQA, and visual instruction finetuning. We provide project materials on the project page and plan to release the full code, annotations, and benchmark to facilitate future research. Videos, code, demo assets, and annotations are provided in supplementary materials Project page: https://tourmaline-caramel-169490.netlify.app.

</details>

#### 2026-06-15 - Geometric Action Model for Robot Policy Learning

**Authors:** Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
**Links:** [abs](https://arxiv.org/abs/2606.17046) - [pdf](https://arxiv.org/pdf/2606.17046)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric foundation model, manipulation, simulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometric Action Model for Robot Policy Learning  
- 作者：Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong  
- 出版日期：2026-06-15  
- 分类：Embodied / Robotics / AR Applications  
- 链接：[摘要](https://arxiv.org/abs/2606.17046) | [PDF](https://arxiv.org/pdf/2606.17046)  

### 一句话总结  
本文提出**几何动作模型（GAM）**，通过复用预训练几何基础模型（GFM）作为共享骨干，实现语言条件下的机器人操作策略学习，在仿真和真实实验中表现优于现有方法。

### 研究问题  
如何让机器人策略在遵循语言指令时，有效利用3D几何信息处理接触丰富的操作任务，而不依赖传统2D图像或2D衍生潜空间。

### 核心思路/方法  
1. **模型结构**：将预训练的几何基础模型（GFM）在中间层拆分——浅层作为观测编码器，插入因果未来预测器以预测语言、本体感知和动作历史条件下的未来潜在token；深层GFM模块则用于特征传播和动作解码，最终同时输出未来几何和动作。  
2. **设计特点**：通过最小架构修改赋予GFM语言条件化的时序世界建模能力，同时保留其丰富的几何先验。

### 主要贡献  
1. 提出GAM，直接复用GFM作为感知、时序预测和动作解码的统一基座。  
2. 通过拆分GFM并插入因果预测器，实现语言条件化的时序世界建模，无需大幅改动模型结构。  
3. 在多个仿真和真实机器人操作基准上，GAM在精确度、鲁棒性、速度和模型轻量化方面均超越当前基础模型规模的基线方法。

### 局限性  
摘要未提供实验的失败案例、泛化边界或计算资源要求等具体局限性信息。

### 阅读优先级  
**高**  
理由：该工作针对机器人操作中的3D几何建模这一核心难题，提出了创新且高效的轻量化解决方案，实验涵盖仿真和真实场景，结果全面优于基线，对具身智能及机器人学习领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world. Recent vision-language-action models (VLAs) and video world-action models (WAMs) inherit strong semantic or temporal priors from large-scale foundation models, but they still operate primarily on 2D image frames or 2D-derived latent spaces, leaving implicit the 3D geometry required for contact-rich manipulation. We propose the Geometric Action Model (GAM), a language-conditioned manipulation policy that directly repurposes a pretrained geometric foundation model (GFM) as a shared substrate for perception, temporal prediction, and action decoding. GAM splits the GFM at an intermediate layer: the shallow layers serve as an observation encoder, and a causal future predictor inserted at the split layer forecasts future latent tokens conditioned on language, proprioception, and action history. The predicted future tokens are then routed through the remaining GFM blocks for feature propagation and decoding, allowing a single backbone to produce both future geometry and actions. This design equips the GFM with language-conditioned temporal world modeling through minimal architectural modification while preserving its rich geometric priors. Across a broad suite of simulation and real-robot manipulation benchmarks, GAM is more accurate, more robust, faster, and lighter than current foundation-model-scale baselines.

</details>

#### 2026-06-15 - R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies

**Authors:** Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu
**Links:** [abs](https://arxiv.org/abs/2606.17040) - [pdf](https://arxiv.org/pdf/2606.17040)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies
- 作者：Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.17040

### 一句话总结
R2RDreamer 提出一种真实到真实的数据增强框架，通过结合轻量级3D编辑和2D视频补全，在不引入模拟-真实差距的前提下，提升基于RGB的2D操控策略的空间泛化能力。

### 研究问题
如何从少量真实演示中通过数据增强，使基于RGB的2D操控策略（如扩散策略和视觉-语言-动作策略）在目标物体姿态、机器人配置和相机视角发生空间偏移时仍能保持泛化能力？

### 核心思路/方法
R2RDreamer 采用两阶段策略：首先，在共享3D空间中执行轻量级3D增强，包括编辑不完整的物体点云和末端执行器轨迹；然后，利用遮挡感知推理将编辑后的场景投影为带掩码的图像空间控制视频，并通过一个稠密控制的图像到视频模型，补全出时间上连贯的RGB观测。整个过程无需强3D场景解析或完整的几何补全，且直接生成适用于2D RGB策略的数据。

### 主要贡献
1. 提出首个面向2D RGB策略的真实到真实数据增强框架，兼顾3D动作-观测的几何一致性与2D视频空间的可视化完整性。
2. 设计了一种结合轻量级3D编辑、遮挡感知投影和稠密控制视频补全的流水线，避免复杂环境配置和模拟-真实鸿沟。
3. 在空间偏移操控任务上，通过扩散策略和视觉-语言-动作策略验证了该方法能显著提升空间泛化能力，并分别分析了3D编辑、遮挡感知投影和视频补全三个模块的贡献。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作针对2D RGB策略的数据增强问题提出实用方案，结合3D和2D优势，避免模拟-真实差距，且在两种主流策略（扩散策略和视觉-语言-动作策略）上进行了验证，对从事机器人操控、模仿学习及数据增广的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial generalization is critical for imitation-learned manipulation policies, but achieving it typically requires scaling demonstrations across diverse object poses, robot configurations, and camera viewpoints. Data augmentation from a few source demonstrations offers a practical alternative to costly real-world collection. Simulation-based augmentation can create controllable variation, but requires complex environment and object setup and may introduce a sim-to-real gap. Recent real-to-real methods avoid these issues by jointly editing 3D observations and action trajectories from real demonstrations, yet they still rely on strong 3D scene parsing and geometry completion, and often produce observations tailored to 3D pointcloud policies rather than RGB-based 2D policies. We propose R2RDreamer, a real-to-real demonstration augmentation framework that preserves the geometric consistency of 3D action-observation editing while moving visual completion to 2D video space. Specifically, R2RDreamer first performs lightweight 3D augmentation by editing incomplete object pointclouds and end-effector trajectories in a shared 3D frame; it then projects the edited scene into masked image-space control videos with occlusion-aware reasoning and uses a dense-control image-to-video model to complete temporally coherent RGB observations. Experiments on spatially shifted manipulation tasks with both 2D diffusion-style policies and vision-language-action policies show that R2RDreamer improves spatial generalization from limited source demonstrations, with analyses validating the contributions of 3D editing, occlusion-aware projection, and video completion.

</details>

#### 2026-06-15 - Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation

**Authors:** Jie Zhang, Xiaoyue Chen, Anzhe Chen, Deqing Li, Gengze Zhou, Hale Yin, Haoqi Yuan, Haoyang Li, Jiahao Li, Jiazhao Zhang, Jingren Zhou, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Pei Lin, Qihang Peng, Shengming Yin, Tianhe Wu, Tianyi Yan, Xiao Xu, Yan Shu, Yanran Zhang, Ye Wang, Yi Wang, Yilei Chen, Yixian Xu, Yiyang Huang, Yuxiang Chen, Zekai Zhang, Zhendong Wang, Zixing Lei, Zhixuan Liang, Zihao Liu, Zikai Zhou, Chenxu Lv, Xiong-Hui Chen, Chenfei Wu
**Links:** [abs](https://arxiv.org/abs/2606.17030) - [pdf](https://arxiv.org/pdf/2606.17030)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, autonomous driving, mapping, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation
- 作者：Jie Zhang, Xiaoyue Chen, Anzhe Chen, Deqing Li 等
- 出版日期：2026-06-15（arXiv发布）
- 分类：Embodied / Robotics / AR Applications
- 链接：arxiv.org/abs/2606.17030

### 一句话总结
本文提出Qwen-RobotWorld，一个以自然语言为统一接口的语言条件视频世界模型，通过视觉轨迹生成统一涵盖机器人操作、自动驾驶、室内导航和人机迁移等多种具身场景。

### 研究问题
如何构建一个统一的具身世界模型，使其能够以自然语言作为动作接口，准确预测多种具身任务（如机器人操作、自动驾驶等）的未来视觉轨迹，从而支持策略训练、虚拟评估和下游控制。

### 核心思路/方法
- **双流MMDiT与MLLM动作编码**：采用60层双流扩散Transformer架构，将冻结的Qwen2.5-VL语义与视频-VAE潜在特征通过逐层联合注意力耦合。
- **具身世界知识（EWK）**：构建包含860万视频-文本对（超2亿帧）的数据集，覆盖20余种具身形态和500余种动作类别，并配以动作-语言映射。
- **通用+专家渐进式课程训练**：两阶段训练策略，先学习通用视觉先验，再注入具身专业化知识，共享语言接口。

### 主要贡献
- 提出统一、语言条件化的视频世界模型Qwen-RobotWorld，在多个具身基准上取得最优或竞争力强的结果（如EWMBench、DreamGen Bench排名第一；WorldModelBench、PBench超越所有开源模型）。
- 展示了三种有前景的应用：合成数据生成以增强策略训练、可扩展虚拟环境用于策略评估、语言指导的规划信号用于下游机器人控制。
- 在RoboTwin-IF基准上的零样本分析支持强泛化能力和多视角一致性。

### 局限性
摘要未提供足够信息（如模型规模、计算资源、失败案例分析、对特定场景的鲁棒性等）。

### 阅读优先级
**高**  
理由：该工作提出大规模、统一的世界模型，在多个具身基准上取得领先结果，且应用方向明晰（数据增强、虚拟评估、控制信号），对具身AI和机器人领域研究者具有直接参考价值。摘要未提及严重缺陷，整体方法论清晰。

</details>

<details>
<summary>Abstract</summary>

We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge (EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+ embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a two-stage training strategy that first learns general visual priors and then injects embodied specialization under a shared language interface. Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-IF benchmark further support robust generalization and multi-view consistency.

</details>

#### 2026-06-15 - DreamX-World 1.0: A General-Purpose Interactive World Model

**Authors:** DreamX Team, Yancheng Bai, Rui Chen, Xiangxiang Chu, Rujing Dang, Hao Dou, Bingjie Gao, Qiwen Gu, Siyu Hong, Jiachen Lei, Geng Li, Jifan Li, Ruimin Lin, Qingfeng Shi, Bingze Song, Lei Sun, Jing Tang, Ruitian Tian, Jun Wang, Jiahong Wu, Pengfei Zhang, Shen Zhang, Jiashu Zhu
**Links:** [abs](https://arxiv.org/abs/2606.16993) - [pdf](https://arxiv.org/pdf/2606.16993)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DreamX-World 1.0: A General-Purpose Interactive World Model
- 作者：DreamX Team, Yancheng Bai, Rui Chen, Xiangxiang Chu, Rujing Dang, Hao Dou, Bingjie Gao, Qiwen Gu, Siyu Hong, Jiachen Lei, Geng Li, Jifan Li, Ruimin Lin, Qingfeng Shi, Bingze Song, Lei Sun, Jing Tang, Ruitian Tian, Jun Wang, Jiahong Wu, Pengfei Zhang, Shen Zhang, Jiashu Zhu
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.16993

### 一句话总结
DreamX-World 1.0是一个通用的交互式文本/图像到视频世界模型，支持可控的长时序生成，在5秒基础评测中总体得分84.76，优于HY-WorldPlay 1.5和LingBot-World。

### 研究问题
如何构建一个通用、可控、支持长时序交互的世界模型，同时实现相机导航、事件控制、多域生成（逼真、游戏风格、风格化）和高帧率推理。

### 核心思路/方法
1. **数据引擎**：结合相机精确的Unreal Engine渲染、动作丰富的游戏录像和恢复相机几何的真实世界视频。
2. **相机控制**：提出E-PRoPE，一种轻量级投影位置编码变体，在保持PRoPE投影几何的同时进行相机感知注意力。
3. **自回归世界模型**：通过因果强制、DMD风格蒸馏和长序列训练，将双向视频生成器转化为几步自回归世界模型。
4. **记忆条件场景持久性**：通过基于相机几何的检索恢复早期视图，减少跨自回归块的颜色漂移。
5. **事件指令微调**：添加可组合的事件控制；强化学习对齐恢复蒸馏后的相机控制和视觉质量。
6. **高效推理**：混合精度DiT、残差重用、75%剪枝VAE解码和异步流水线并行，在8块RTX 5090上达到16 FPS。

### 主要贡献
- 提出通用交互式世界模型，支持长时序、相机控制和事件指令。
- 引入E-PRoPE编码和记忆条件场景持久性机制，提升长时序生成稳定性。
- 通过训练和推理优化（蒸馏、残差重用、剪枝等）实现16 FPS实时推理。
- 在5秒评测中取得84.76总分，优于对比方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作针对世界模型的可控生成和高效推理有明确技术贡献，适合关注交互式视频生成、世界模型或实时推理的读者；但摘要未列出具体实验设置和基线对比细节，作为应用方向的论文，重要程度中等。

</details>

<details>
<summary>Abstract</summary>

DreamX-World 1.0 is a general-purpose interactive text/image-to-video world model for controllable long-horizon generation. It supports camera navigation, revisits to previously observed regions, and promptable events across photorealistic, game-style, and stylized domains. Our data engine combines camera-accurate Unreal Engine rendering, action-rich gameplay recordings, and real-world videos with recovered camera geometry. For camera control, we introduce E-PRoPE, a lightweight variant of projective positional encoding that retains PRoPE's projective camera geometry while applying camera-aware attention to spatially reduced tokens. We convert a bidirectional video generator into a few-step autoregressive world model using causal forcing, DMD-style distillation, and long-rollout training. Training on self-generated long-horizon contexts exposes the model to its own generated history and reduces the style and color drift that accumulates across autoregressive chunks. Memory-Conditioned Scene Persistence retrieves earlier views through camera-geometry-based retrieval, while residual recycling makes the conditioning path less sensitive to imperfect memory latents. Event Instruction Tuning adds composable event control, and reinforcement learning alignment recovers camera control and visual quality after distillation. With mixed-precision DiT execution, residual reuse, 75\%-pruned VAE decoding, and asynchronous pipeline parallelism, DreamX-World 1.0 reaches up to 16\,FPS on eight RTX\,5090 GPUs. On our 5-second basic evaluation, DreamX-World 1.0 achieves a camera-control score of 73.75 and an overall score of 84.76, outperforming HY-WorldPlay 1.5 and LingBot-World in overall score, which achieve 80.79 and 80.45, respectively.

</details>

#### 2026-06-15 - Latent Space Reinforcement Learning for Inverse Material Estimation in Food Fracture Simulation

**Authors:** Adrian Ramlal, Yuhao Chen, John S. Zelek
**Links:** [abs](https://arxiv.org/abs/2606.16870) - [pdf](https://arxiv.org/pdf/2606.16870)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Latent Space Reinforcement Learning for Inverse Material Estimation in Food Fracture Simulation
- 作者：Adrian Ramlal, Yuhao Chen, John S. Zelek
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.16870

### 一句话总结
本文提出了一个基于潜空间强化学习的框架，通过目标条件策略在不可微的食品断裂模拟器中高效估计材料参数，以橘子剥皮为例，验证了方法的有效性。

### 研究问题
如何从目标断裂行为描述中，反向估计非均匀食品材料（如橘子）的不可微材料参数，并实现任意目标无需重训练的通用逆映射。

### 核心思路/方法
1. 在不可微的连续损伤力学模拟器上，训练一个神经网络代理（使用2000次前向模拟）。
2. 比较CMA-ES（无梯度进化优化器）与PPO（强化学习算法）在原始9维参数空间和两个学习到的4维潜空间上的表现。
3. 训练一个目标条件的PPO策略，学习通用逆映射：给定任意目标剥皮行为描述，该策略可在单次前向传递（约10ms，8次代理评估）中输出材料参数估计。
4. 使用归一化流潜空间与共享代理评估器，并引入热启动扩展（从策略输出初始化CMA-ES细化）进一步提升恢复精度。

### 主要贡献
- 提出了一种基于潜空间强化学习的逆材料估计框架，能在不可微模拟器中高效运行。
- 目标条件PPO策略在模拟器验证中实现0.642的实际恢复率，比原始参数空间提升23%。
- 热启动CMA-ES细化将恢复率提升至0.828（使用540次评估），为食品物理逆向问题提供了实用方案。

### 局限性
摘要未提供足够信息：未讨论方法在非食品场景或不同断裂类型上的泛化性、对噪声或观测误差的鲁棒性、以及计算资源需求等局限性。

### 阅读优先级
高  
理由：该工作将强化学习与潜空间表示结合，解决了食品模拟中不可微逆参数估计的实际问题，方法清晰且有量化性能提升（23%），对机器人、食品科学和计算机视觉领域的交叉研究有参考价值。

</details>

<details>
<summary>Abstract</summary>

Realistic visual simulation of food manipulation requires accurate material parameters, yet these are difficult to measure directly and vary across the heterogeneous regions of a single food item. We address the inverse problem of estimating material parameters from a target description of fracture behavior in a non-differentiable continuum damage mechanics simulator. Using orange peeling as a test case, we train a neural surrogate on 2,000 forward simulations and compare Covariance Matrix Adaptation Evolution Strategy (CMA-ES, a gradient-free evolutionary optimizer) with Proximal Policy Optimization (PPO, a reinforcement learning algorithm) across the original 9-dimensional parameter space and two learned 4-dimensional latent representations. Since different oranges have different material properties, a practical inverse system must handle arbitrary targets without retraining. We train a goal-conditioned PPO policy that learns a general inverse mapping: given any target description of peeling behavior, the policy produces a material parameter estimate in a single forward pass (8 surrogate evaluations, approximately 10ms). Operating in a normalizing flow latent space with a shared surrogate evaluator, the goal-conditioned policy achieves 0.642 actual recovery when validated through the simulator, outperforming the original parameter space by 23%. A warm-start extension that initializes CMA-ES refinement from the policy's output further improves recovery to 0.828 with 540 evaluations. These findings provide a practical framework for inverse food physics and lay groundwork for vision-driven material identification from video observations of food manipulation.

</details>

#### 2026-06-15 - Automated Digital Twin Construction for Highway Scenarios Using LiDAR Point Clouds and OpenStreetMap

**Authors:** Yongqi Zhao, Dong Bi, Paul Kovacevic, Tomislav Mihalj, Martin Schabauer, Johannes Betz, Arno Eichberger
**Links:** [abs](https://arxiv.org/abs/2606.16570) - [pdf](https://arxiv.org/pdf/2606.16570)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Automated Digital Twin Construction for Highway Scenarios Using LiDAR Point Clouds and OpenStreetMap
- 作者：Yongqi Zhao, Dong Bi, Paul Kovacevic, Tomislav Mihalj, Martin Schabauer, Johannes Betz, Arno Eichberger
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.16570

### 一句话总结
提出一种自动化工作流，融合LiDAR点云与OpenStreetMap数据，生成符合ASAM OpenDRIVE标准的高速公路数字孪生地图，减少了手动干预需求。

### 研究问题
如何高效、低成本地从真实传感器数据（LiDAR点云）和开源地图（OSM）中自动构建高速公路场景的标准化道路地图（ASAM OpenDRIVE格式），以支持自动驾驶系统的仿真与验证。

### 核心思路/方法
1. 利用移动测绘LiDAR点云精确提取车道级几何信息，但仅覆盖扫描路径范围。  
2. 结合OpenStreetMap提供的广泛道路网络拓扑，弥补LiDAR在未覆盖区域（如匝道）的几何缺失。  
3. 自动化管道中：从LiDAR测量重建主线路段；从OSM道路图推断匝道几何与拓扑结构，从而完整建模高速公路立交，无需全面传感器覆盖。  
4. 最终生成地理参考的ASAM OpenDRIVE地图。

### 主要贡献
- 提出融合LiDAR精确几何与OSM拓扑的自动化数字孪生构建管道，仅需最小手动干预。  
- 实验证明平均横向均方根误差（RMSE）为0.740米，且生成地图可直接用于主流仿真平台（IPG CarMaker和Esmini）。  
- 提供了开源代码（GitHub仓库）。

### 局限性
摘要未提供足够信息，无法确定具体局限性（如对特定道路类型的适用性、计算效率、大场景扩展性等），需要阅读全文。

### 阅读优先级
- 优先级：中  
- 理由：该工作针对自动驾驶仿真中的地图生成问题，提出实用的传感器融合方案（LiDAR+OSM），结果有定量误差指标和仿真验证，且代码开源。适合对数字孪生、地图自动化构建或自动驾驶仿真感兴趣的读者。但摘要未披露与纯LiDAR方法或纯OSM方法的全面对比，以及局限性细节，故优先级设为中等。

</details>

<details>
<summary>Abstract</summary>

Accurate road environment modeling is fundamental to the simulation and validation of automated driving systems. However, constructing road maps in standardized formats such as ASAM OpenDRIVE from real-world sensor data remains a time-consuming and costly process. Mobile mapping LiDAR captures accurate lane-level geometry but is confined to the driven corridor, while OpenStreetMap (OSM) provides broad road network topology but lacks geometric precision at the lane level. To address this, an automated workflow is proposed to fuse LiDAR point clouds with OSM data to generate georeferenced ASAM OpenDRIVE maps of highway environments, requiring minimal manual intervention. The pipeline reconstructs mainline roads from LiDAR-derived measurements and infers ramp geometry and topology from the OSM road graph, enabling complete highway interchange modeling without full sensor coverage. Experiments demonstrate a mean lateral RMSE of 0.740 m, and the generated maps are directly usable in mainstream simulation platforms including IPG CarMaker and Esmini. These results validate the effectiveness of combining measurement-derived geometry with map-derived topology for automated OpenDRIVE digital twin generation. The project code is available at https://github.com/ftgTUGraz/opendrive-digital-twin-generator

</details>

#### 2026-06-15 - PROSE: Training-Free Egocentric Scene Registration with Vision-Language Models

**Authors:** Zhiang Chen, Nahyuk Lee, Boyang Sun, Taein Kwon, Marc Pollefeys, Zuria Bauer, Sunghwan Hong
**Links:** [abs](https://arxiv.org/abs/2606.16569) - [pdf](https://arxiv.org/pdf/2606.16569)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** AR, digital twin, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PROSE: Training-Free Egocentric Scene Registration with Vision-Language Models
- 作者：Zhiang Chen, Nahyuk Lee, Boyang Sun, Taein Kwon, Marc Pollefeys, Zuria Bauer, Sunghwan Hong
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications (具身智能/机器人/增强现实应用)
- 链接：https://arxiv.org/abs/2606.16569

### 一句话总结
PROSE 是一种无需训练、仅依赖 RGB 视觉语言模型的自我中心场景配准方法，通过将视频序列转化为对象级 3D 场景图并利用 VLM 进行跨扫描匹配，在无需深度传感器或注释的情况下实现优于传统几何和深度学习方法的效果。

### 研究问题
如何仅通过 RGB 图像对两个不同时间拍摄的自我中心室内场景进行鲁棒且可扩展的配准，而无需深度传感器、预训练匹配器或标注的场景图。

### 核心思路/方法
1.  **场景图生成**：利用现成的几何、分割和语言基础模型，将每个 RGB 序列提升为对象级 3D 场景图。
2.  **跨序列匹配**：使用同一个预训练的视觉语言模型（VLM）来匹配两个 RGB 序列中的对象实例。具体通过对象高度作为先验来缩小匹配范围，并通过成对的相同/不同查询来验证匹配提案。
3.  **刚性变换估计**：为每个匹配对象假设一个候选变换，并选择几何一致性最强的变换作为最终结果。整个过程无需添加任何可学习参数，也不需要深度传感器、训练或标注图。

### 主要贡献
- 提出了一种全新的、完全无需训练的RGB-only自我中心场景配准范式，避开了传统方法对稀疏几何或预训练图匹配的依赖。
- 有效利用预训练VLM的跨扫描匹配能力，结合对象高度先验和配对验证查询，使匹配过程变得可靠。
- 在Aria Digital Twin和Aria Everyday Activities基准测试中，该方法在配准精度上优于几何基线和基于学习场景图的方法，且生成的场景图可直接用于下游任务。

### 局限性
摘要未提供足够信息。例如，未讨论该方法对VLM性能的依赖性、在极端遮挡或光照变化下的鲁棒性、计算成本，以及是否在所有场景中都优于基线方法。

### 阅读优先级
高。理由：该工作提出了一种新颖的、轻量级（无训练）的自我中心场景配准方案，直接针对该领域的关键挑战（无深度、无标注、视图模糊）给出了独特的解决路径，并在多个基准上取得了领先性能。对于从事机器人空间记忆、AR系统以及具身智能的研究者具有重要参考价值。即使摘要未提供全部细节，其核心思路的创新性和实用性已经足够突出。

</details>

<details>
<summary>Abstract</summary>

Registering two captures of the same indoor space taken at different times underpins persistent spatial memory for robots and AR systems, yet the realistic version of this task is egocentric and its most scalable form is RGB-only. Head-mounted cameras yield blurry, fast-moving, partially overlapping views from which dense geometry is hard to recover. Classical registration leans on exactly the clean point clouds this setting lacks, while learned scene-graph methods require a pre-built or annotated graph and a trained matcher that we find brittle under egocentric data. We take a different route, using a pretrained vision-language model as the source of both scene understanding and cross-scan matching. Our method, PROSE (Prompted Scene rEgistration), lifts each RGB sequence into an object-level 3D scene graph using off-the-shelf foundation models for geometry, segmentation, and language, then prompts the same VLM to match object instances across the two RGB sequences. To make this matching tractable and reliable, we leverage object heights as a prior and verify each proposed match with a paired same/different query, then solve for the rigid transform by hypothesizing a candidate per matched object and selecting the one with the strongest geometric consensus. PROSE adds no learned parameters and requires no depth sensor, training, or annotated graph. On the egocentric Aria Digital Twin and Aria Everyday Activities benchmarks, it outperforms both geometric and learned scene-graph baselines in registration accuracy, on ground-truth and RGB-reconstructed point clouds alike, and the scene graph it produces transfers directly to downstream tasks.

</details>

#### 2026-06-15 - EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video

**Authors:** Hyunjin Kim, Ri-Zhao Qiu, Guangqi Jiang, Xiaolong Wang
**Links:** [abs](https://arxiv.org/abs/2606.16202) - [pdf](https://arxiv.org/pdf/2606.16202)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video
- 作者：Hyunjin Kim, Ri-Zhao Qiu, Guangqi Jiang, Xiaolong Wang
- 出版日期：2026-06-15
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.16202

### 一句话总结
本文提出EgoPhys框架，能够从第一人称RGB视频中，利用可泛化的先验知识构建可变形物体的物理数字孪生，并支持零样本泛化到未见物体。

### 研究问题
如何仅通过第一人称RGB视频，构建可变形物体（如弹性材料、织物）的物理数字孪生，并实现准确的物理动力学预测与零样本泛化？

### 核心思路/方法
1. **蒸馏逆物理解**：将每个物体的逆物理求解结果蒸馏到紧凑的码本（codebook）中，避免测试时对每个弹簧刚度进行逐点优化。
2. **可泛化先验训练**：利用包含多种可变形物体、场景和操作风格的自我中心交互数据集，训练模型以学习通用先验。
3. **预测密度场**：对未见物体，直接预测密集的弹簧刚度场，实现零样本泛化。
4. **机器人部署验证**：以单个第一人称人类操作视频初始化数字孪生，作为内部世界表征辅助可变形物体规划（在真实xArm6机器人上演示）。

### 主要贡献
- 提出首个能从自我中心RGB视频构建可变形物理数字孪生的框架EgoPhys。
- 通过码本蒸馏与可泛化先验，实现无需测试时优化的零样本泛化。
- 在重建、未来预测和零样本泛化任务上优于基线方法。
- 构建了包含多样化可变形物体、场景和操作风格的自我中心交互数据集。
- 在真实机器人上验证了单次人类操作视频初始化的数字孪生可作为世界模型辅助规划。

### 局限性
摘要未提供足够信息，无法从文本中推断具体局限性。例如，未说明对视频质量、物体种类或光照条件的潜在限制，也未提及计算成本或失败案例。

### 阅读优先级
**高**
理由：该工作将自我中心RGB视频直接用于可变形物体物理建模，结合零样本泛化与机器人规划验证，在具身智能和机器人领域具有明确的应用潜力和创新性。摘要清晰展示了从数据、方法到实际部署的完整链条，对于关注物理仿真、数字孪生或机器人操作的读者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Humans naturally understand object physics through everyday interactions, but faithfully predicting complex deformable dynamics, such as elastic materials and fabrics, remains a major challenge for computer vision and robotics. We present EgoPhys, a framework that constructs deformable physical digital twins from egocentric RGB-only video using generalizable priors. EgoPhys overcomes the limitations of existing methods to enable controllable deformable digital twin generation from egocentric videos by distilling per-object inverse-physics solutions into a compact codebook, enabling prediction of dense spring stiffness fields for unseen objects without per-spring test-time optimization. Trained with generalizable priors from diverse egocentric interactions, EgoPhys outperforms baselines in reconstruction, future prediction, and zero-shot generalization. To support training and evaluation, we curate an egocentric interaction dataset covering diverse deformable objects, scenes, and manipulation styles. We deploy EgoPhys on a real xArm6 robot, demonstrating that a digital twin initialized from a single egocentric human play video can serve as an internal world representation to aid in deformable-object planning, highlighting egocentric RGB observations as a scalable path toward real-to-sim pipelines.

</details>

#### 2026-06-14 - FlashNav: Ultra-Fast Policy Training for Robot Navigation within 20 Seconds

**Authors:** Shanze Wang, Yiwei Qian, Xinming Zhang, Jun Xue, Siwei Cheng, Xianghui Wang, Qingyuan Hu, Xiaoyu Shen, Wei Zhang
**Links:** [abs](https://arxiv.org/abs/2606.15846) - [pdf](https://arxiv.org/pdf/2606.15846)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FlashNav: Ultra-Fast Policy Training for Robot Navigation within 20 Seconds
- 作者：Shanze Wang, Yiwei Qian, Xinming Zhang, Jun Xue, Siwei Cheng, Xianghui Wang, Qingyuan Hu, Xiaoyu Shen, Wei Zhang
- 出版日期：2026-06-14
- 分类：Embodied / Robotics / AR Applications
- 链接：论文摘要 | 论文PDF

### 一句话总结
FlashNav提出一种GPU优先的深度强化学习导航训练框架，将策略训练时间缩短至20秒以内，并能在真实轮式和足式机器人上部署。

### 研究问题
如何大幅降低基于深度强化学习的机器人导航策略的训练时间（从数小时/天缩短至秒级），同时保持策略的可部署性和避障性能。

### 核心思路/方法
核心思路是让仿真环境紧密对齐导航马尔可夫决策过程（MDP），剥离不必要的渲染和高保真物理细节，只保留速度级导航必需组件（占据几何、范围传感、目标条件控制、机器人运动动力学、碰撞处理、终止和重置）。具体实现上，基于批量化位图仿真器和全GPU驻留训练流水线（FastDSAC学习器），完全在GPU上生成大规模并行导航转移样本。

### 主要贡献
1. 提出首个将基于DRL的机器人导航策略训练时间降至秒级的框架，最快部署策略训练时间少于20秒。
2. 通过实验在TurtleBot2和Unitree Go2上展示：在RTX 5090上20秒内达到100%成功率；在多个桌面GPU上训练时间保持在几十秒内。
3. 验证了学得的策略可直接迁移到物理轮式和足式机器人上，在静态和动态室内场景中均有效。

### 局限性
摘要未提供关于方法在复杂动态场景、多障碍物环境或不同传感器配置下的泛化能力；也未提及与其他基线方法的详细对比指标或失败案例。摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作显著降低了机器人导航中深度强化学习的训练时间瓶颈（从小时级到秒级），且进行了真实机器人部署验证，对机器人应用领域具有较强实用价值和启发性。

</details>

<details>
<summary>Abstract</summary>

Deep reinforcement learning has shown strong potential for robot navigation, but its practical deployment is still limited by the long wall-clock cost of policy training. This paper presents FlashNav, a GPU-first framework for ultra-fast range-based robot navigation training. To the best of our knowledge, FlashNav is the first DRL-based robot navigation framework that reaches seconds-level policy training, with the fastest deployable policy trained in less than 20 seconds. The key idea is to align simulation with the navigation MDP: FlashNav preserves the essential components for velocity-level navigation, including occupancy geometry, range sensing, goal-conditioned control, robot motion dynamics, collision handling, termination, and reset, while removing unnecessary rendering and high-fidelity physical details from the training loop. Built on a batched bitmap simulator and a fully GPU-resident training pipeline with our FastDSAC learner, FlashNav generates massive parallel navigation transitions entirely on GPU. Experiments on TurtleBot2 and Unitree Go2 show that FlashNav achieves a 100\% success-rate below 20 seconds on an RTX 5090 and remains within tens of seconds across desktop GPUs. The learned policies further transfer to physical wheeled and legged robots in static and dynamic indoor scenes, demonstrating that DRL-based navigation can be trained at seconds-level speed while preserving deployable obstacle-avoidance behavior.

</details>

#### 2026-06-12 - BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization

**Authors:** Yinqiang Zhang, Liang Lu, Yipeng Pan, Maolin Lei, Yuhan Xie, Zhanteng Xie, Xiaowei Luo, Jia Pan
**Links:** [abs](https://arxiv.org/abs/2606.14237) - [pdf](https://arxiv.org/pdf/2606.14237)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization
- 作者：Yinqiang Zhang, Liang Lu, Yipeng Pan, Maolin Lei, Yuhan Xie, Zhanteng Xie, Xiaowei Luo, Jia Pan
- 出版日期：2026-06-12T08:20:02Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.14237

### 一句话总结
本文提出一种基于LiDAR的室内定位方法BIM-Loc，通过直接集成设计阶段的建筑信息模型（BIM），在实现轨迹估计的同时在线检测真实环境与BIM之间的差异。

### 研究问题
如何在特征稀疏的室内环境中，利用设计阶段的BIM模型实现准确、鲁棒的定位，并在线检测真实观测与BIM之间的不一致性。

### 核心思路/方法
1. **多命中射线投射策略**：高效实现BIM与点云数据的关联，并将3D观测投影到2D纹理空间。
2. **BIM集成因子的姿态图优化框架**：联合优化里程计、序列扫描与BIM结构之间的约束一致性。
3. **分层贝叶斯推理模块**：增量更新连续2D表面表示，用于检测不一致性，实现从像素级到结构级的传播更新。

### 主要贡献
1. 提出一种直接集成BIM的LiDAR定位方法，无需依赖精确的预先地图。
2. 创新性地将定位与BIM-现实差异检测在线融合。
3. 通过模拟与真实实验证明，在定位精度与鲁棒性上显著优于现有基于地图的方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对服务与巡检机器人等实际应用中常见的特征稀疏室内环境，提出一种无需预先精确地图即可利用设计阶段BIM的定位方案，具备很强的实用价值。方法上引入差异感知与在线更新机制，创新性明确，且已在模拟与真实场景中验证性能优势。适用于从事机器人定位、BIM应用或室内导航的研究者。

</details>

<details>
<summary>Abstract</summary>

Accurate and robust localization is a fundamental requirement for service and inspection robots, particularly in feature-sparse indoor environments where traditional systems struggle due to a lack of distinct landmarks. While prior maps can enhance robustness, precise and compact maps capturing real-world details are often unavailable for new or frequently changing environments. This paper presents BIM-Loc, a novel discrepancy-aware LiDAR-based localization method that directly integrates Building Information Models (BIM) from the design phase. BIM-Loc simultaneously estimates trajectories aligned with the BIM coordinate system and identifies discrepancies between real-world observations and the as-designed BIM in an online fashion. Our core contributions include: (1) a novel multi-hit ray casting strategy for efficient BIM-point data association and projection of 3D observations into 2D texture space; (2) a pose graph optimization framework with BIM-integrated factors that enforces consistency among odometry, sequential scans, and BIM structures; and (3) a hierarchical Bayesian inference module that incrementally updates a continuous 2D surface representation for discrepancy detection, propagating updates from the pixel to the structure level. Extensive evaluations in both simulation and real-world applications demonstrate that BIM-Loc significantly outperforms state-of-the-art map-based methods in localization accuracy and robustness.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
