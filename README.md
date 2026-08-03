# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：47
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 17
  - Embodied / Robotics / AR Applications: 14
  - Neural Scene Representations & Rendering: 11
  - Dynamic / 4D Reconstruction: 3
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**1. 4D 重建与动态场景表示进入"效率 + 可控性"并重阶段**
今日多篇论文（AdaAnchor4D、S-Avatar、TSOG、4DHumanDiff、SpiD）围绕动态场景/动态人体展开。技术重心已从早期"能否重建"转向"如何高效重建、压缩存储、并可控驱动"。TSOG 直接针对 4DGS 文件体积（>90% 压缩率），SpiD 和 S-Avatar 都强调单图头部虚拟形象驱动且消除外部追踪依赖，4DHumanDiff 则追求端到端直接生成 4DGS 资产，避免中间视频步骤。这一趋势表明，**动态场景重建正从研究原型走向可部署资产管线**。

**2. 语言/语义信息开始成为几何任务的外部引导信号**
CapDepth 和 ByDeWay-V2 分别将详细长文本描述和显式空间谓词注入单目深度估计与多模态大模型空间推理。JEPADepth 则引入自监督掩码预测表示学习（I-JEPA 风格）增强光度基线。这类工作突破了纯几何/光度的自监督范式，借助预训练视觉基础模型（DINOv3、VGGT）或语言模型的先验知识来解决传统歧义问题（非朗伯表面、恶劣天气、物体幻觉）。

**3. 高斯泼溅（3DGS）成为场景重建与质量评估的共同底座**
StructureGS 在 3DGS 中引入结构感知约束重建铰接物体；Genie Sim PanoWorld 用前馈全景重建器将生成视频直接提升为 3D 高斯场景；SpatialQ 则专门做 3DGS 场景质量评估。3DGS 已从渲染表示工具演化为**贯穿生成、重建、评估、存储全链路的公共基础格式**。

**4. 世界模型与仿真平台寻求"连续物理时间"和"信号级保真"**
ODEWorld 用 ODE 参数化连续潜伏速度场，突破离散时间预测局限，支持任意时间分辨率预测和反向预测；mmRadarTwin 构建信号级（而非路径级/渲染级）的毫米波雷达数字孪生平台，实现测量与仿真的同域比较。两者都指向**对物理世界更本质的建模粒度**——时间上连续、信号上可校准，而非仅追求视觉逼真。

**5. SLAM/SfM 与生成式重建路径走向互补融合**
VidMap 将 SLAM 的时序约束与 SfM 的全局优化结合，解决未校准长视频度量重建；Genie Sim PanoWorld 则从生成侧出发，用轨迹可控的全景视频作为重建桥梁。这两者体现了重建研究的两条并行路线：**经典几何管线强化、生成模型几何化**。

---

#### 技术路线观察

| 方向 | 代表论文 | 技术侧重点 |
|------|----------|------------|
| **几何基础模型** | JigShape、SpatialQ | 用基准测试和评估任务反向推动基础模型能力边界认知；强调视觉-几何联合推理和跨视图一致性，而非单纯提高重建精度 |
| **3D/4D 重建（多视图几何）** | VidMap、Convolutional Neural Shading、Endo-NeRF++ | 回归几何精度与鲁棒性：卷积着色器替代单点着色、不确定性引导采样、SLAM+SfM 混合管线；核心诉求是暗区/无纹理/动态遮挡下的稳定性 |
| **神经场景表示与渲染** | TSOG、S-Avatar、SpiD、StructureGS、4DHumanDiff、AdaAnchor4D | 3DGS 变体主导：锚点条件聚合、双轴解耦、结构感知约束、扩散引导生成；共性是从"纯渲染质量"转向"可编辑性 + 可驱动性 + 压缩效率" |
| **机器人 / AR 应用** | ODEWorld、mmRadarTwin、Write-Safe Flow Field Mapping、Genie Sim PanoWorld | 面向物理交互与闭环部署：连续时间预测、信号级仿真校准、写安全分数门控地图更新、可漫游场景生成；重点关注"感知-地图-决策"的闭环可靠性而非单一模块精度 |

值得注意的交叉点：**SpatialQ 将质量评估引入 3DGS 场景理解**，这是今日列表中唯一聚焦"评估"的论文，反映了 3DGS 生态正在形成独立的测评研究分支。而 **JEPADepth 和 CapDepth 都从不同角度引入额外监督信号（表示空间预测/语言描述）**，暗示自监督几何任务正在从纯光度约束向多模态/自监督表示学习过渡。

---

#### 值得优先阅读的论文

1. **VidMap**（2607.27194）
   - 理由：直接处理 SLAM 与 SfM 的长期矛盾，融合时序约束与全局优化，对未校准任意长视频的度量重建提出了系统级方案。作者来自 ETH（Pollefeys 组），方法框架具有示范性，对机器人导航和场景理解的数据规模化有直接意义。

2. **Convolutional Neural Shading**（2607.28132）
   - 理由：直击神经渲染中"单点几何信息不足"的核心瓶颈，用卷积着色器捕捉邻域信息，解决暗区和无纹理区域的几何重建——这是当前 NeRF/3DGS 方法普遍存在的痛点，值得精读实现细节。

3. **TSOG**（2607.28049）
   - 理由：4DGS 的文件体积问题是实际部署的最大障碍之一（当前格式动辄数 GB）。>90% 压缩率且 PSNR 损失极小，如果真实有效，将是 4D 内容存储和传输的标准候选方案。需要重点验证其在不同 4DGS 表示上的通用性声明。

4. **AdaAnchor4D**（2607.28320）
   - 理由：单目无人机视频的 4D 重建具有明确应用价值（城市级动态场景），且当前动态高斯方法在"时空异构"场景中普遍存在重影问题。其锚点条件化特征聚合思路新颖，对场景的局部动态建模有借鉴意义。

5. **SpiD**（2607.28032）
   - 理由：解决了现有高斯头部虚拟形象方法的"公平性"问题——外部追踪延迟不计入推理时间。其"计算轴 + 特征轴"双解耦的设计哲学对任何实时可驱动 3D 表示都有参考价值。

---

#### 可能的研究机会

- **3DGS 质量评估的标准化**：SpatialQ 是这一方向的早期探索，但 3DGS 场景质量缺乏公认基准、指标体系和跨视图一致性度量方法。可跟进：建立包含不同重建质量/不同场景类型的大规模 3DGS 质量评测数据集，或将无参考质量评估扩展到 4DGS。

- **语言引导的几何任务深化**：CapDepth 和 ByDeWay-V2 分别展示了长描述和空间谓词的价值，但语言信息目前只用于引导单目深度估计和 MLLM 推理。可探索：将详细语言描述用于 3D 重建质量反馈、动态场景编辑（"移动左侧红色物体"）、或铰接物体部件语义标注（对 StructureGS 的结构约束提供更丰富的先验）。

- **数字孪生与重建的闭环校准**：mmRadarTwin 提供了信号级仿真平台，但仅用于毫米波雷达验证。可将类似"共享接口 + 路径归因"设计扩展到 3DGS/NeRF 的渲染管线，实现虚拟场景与真实重建的同域比较，用于诊断重建误差来源——目前重建误差分析主要靠人为观察。

- **世界模型的连续时间与稀疏观测结合**：ODEWorld 支持任意时间分辨率预测，但输入观测仍为规则离散帧。可组合：将连续时间预测与稀疏/不规则观测（如机器人事件相机、随机采样视频帧）结合，增强真实部署灵活性。

- **语义通信的内容自适应压缩**：机器人语义通信 demo（2607.28256）展示了 VQ-VAE 令牌压缩，但如果结合 TSOG 的空间有序结构，或

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-03T11:13:58-04:00
**Total number of papers:** 36
**Number of papers added in the latest update:** 1
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

### 2026-07

#### 2026-07-30 - JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles

**Authors:** Shawn Li, Wei Yang, Jike Zhong, Jiate Li, Jiawei Yang, You Qin, Ryan Rossi, Franck Dernoncourt, Roger Zimmermann, Yue Wang, Zhengzhong Tu, Vicente Ordonez, Mohit Bansal, Yue Zhao
**Links:** [abs](https://arxiv.org/abs/2607.27670) - [pdf](https://arxiv.org/pdf/2607.27670)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** geometric reasoning

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles
- 作者：Shawn Li, Wei Yang, Jike Zhong, Jiate Li, Jiawei Yang, You Qin, Ryan Rossi, Franck Dernoncourt, Roger Zimmermann, Yue Wang, Zhengzhong Tu, Vicente Ordonez, Mohit Bansal, Yue Zhao
- 出版日期：2026-07-30T04:34:27Z
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2607.27670

### 一句话总结
本文提出一个基于榫卯拼图的全新基准JigShape，用于评估视觉语言模型（VLMs）的视觉-几何推理能力，发现在更高密度拼图中所有模型均出现性能崩塌的“缩放悬崖”现象。

### 研究问题
现有拼图基准采用矩形切割，在纹理重复区域会产生模糊的ground truth，无法有效衡量VLM的几何推理能力。本文旨在通过引入具有强局部兼容性约束的榫卯咬合拼图，评估VLM在视觉内容与几何约束联合推理上的真实表现，并探索其在不同规模拼图下的能力边界。

### 核心思路/方法
构建JigShape基准，使用“榫+槽”（tab-and-blank）互锁拼图片段，使几何约束提供强局部兼容性要求，与视觉内容结合后产生无歧义的ground truth。基准包含95K个实例，覆盖4×4至16×16四种网格密度。评估方法包括：对前沿VLM进行零样本测试，以及对模型进行监督微调（SFT）后测试，观察不同网格规模下的性能变化。

### 主要贡献
1. 提出JigShape基准，通过榫卯互锁设计解决了传统矩形拼图ground truth模糊的问题，提供无歧义的几何-视觉联合推理评估。
2. 建立包含95K实例、四种网格密度的大规模评测集，系统评估VLM的视觉几何推理能力。
3. 揭示零样本VLM在几何推理上的显著短板：仅GPT-5.5在4×4上超过随机基线，其余模型均处于随机水平。
4. 发现“缩放悬崖”现象：监督微调在4×4上可达到>97%准确率，但所有模型在更大网格（8×8、12×12）上性能急剧下降，表明现有架构无法在拼图数量增加时维持一致的约束满足能力。

### 局限性
摘要未提供足够信息。摘要仅提及性能下降现象（“scaling cliff”）及其对架构能力的暗示，但未明确讨论基准本身的局限性（如可能的偏差、计算成本、泛化范围等）。此外，摘要未提供关于实验设置的具体细节、模型部署方式或误差分析的深入讨论。

### 阅读优先级
**高**
理由：该论文针对VLM几何推理这一关键短板，提出了设计新颖的基准（榫卯拼图），并揭示了系统的“缩放悬崖”现象，这对当前VLM能力边界评估和未来架构改进具有重要参考价值。尽管摘要中未给出完整实验细节，但问题定义清晰，发现的现象具有跨模型的一般性，适合计算机视觉与多模态推理方向的研究者重点关注。

</details>

<details>
<summary>Abstract</summary>

Jigsaw puzzle solving requires jointly reasoning about visual content and geometric constraints, yet existing benchmarks use rectangular cuts that create ambiguous ground truth in texture-repeated regions. We introduce \textit{\ours{}}, a benchmark with tab-and-blank interlocking pieces where geometric constraints provide strong local compatibility requirements that, combined with visual content, yield unambiguous ground truth. Across 95K instances at four grid densities (4$\times$4 to 16$\times$16), we find that \textbf{zero-shot VLMs largely lack geometric reasoning}: only one of five frontier models (GPT-5.5) exceeds random baseline on 4$\times$4 puzzles, while all others perform at chance level. While supervised fine-tuning achieves $>$97\% on 4$\times$4, \textbf{all models collapse on larger grids}: GPT-5.5 drops from 70\% to near-random on 8$\times$8, and even fine-tuned models fall below 5\% on 12$\times$12. This ``scaling cliff'' suggests current architectures cannot maintain consistent constraint satisfaction as the number of pieces increases. \ours{} establishes scalable geometric reasoning as an open challenge for vision-language models.

</details>

#### 2026-07-29 - SpatialQ: Understanding 3D Gaussian Splatting Scene Quality via Visual-based MLLM

**Authors:** Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao
**Links:** [abs](https://arxiv.org/abs/2607.26595) - [pdf](https://arxiv.org/pdf/2607.26595)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** VGGT, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialQ: 基于视觉多模态大语言模型的3D高斯泼溅场景质量理解
- 作者：Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao
- 出版日期：2026-07-29（需注意该日期可能与实际发布时间存在偏差，系原文提供）
- 分类：Geometry Foundation Models（主分类）；Neural Scene Representations & Rendering（次分类）
- 链接：[摘要页](https://arxiv.org/abs/2607.26595) | [PDF](https://arxiv.org/pdf/2607.26595)

### 一句话总结
本文提出SpatialQ，一个针对3D高斯泼溅（3DGS）场景质量评估的多模态框架，通过融合多视图几何特征与视觉大语言模型，解决了传统2D质量指标难以捕捉空间结构和跨视图一致性的问题。

### 研究问题
如何对3D高斯泼溅重建的3D场景进行可靠的质量评估，使其不仅能衡量渲染视图的感知保真度，还能反映空间结构、跨视图一致性等场景级因素。

### 核心思路/方法
1. **3D感知质量表示学习**：基于VGGT编码器增加专用质量预测头，将多视图图像编码为视图特定特征并聚合，捕捉跨视图一致性。同时通过联合建模深度和点云结构信息，融入几何线索，学习超越外观特征的结构感知质量表示。
2. **基于多模态大语言模型的推理机制**：将原始图像、深度图、点云渲染图和相机参数共同输入Qwen模型（一种多模态大语言模型），实现有依据的多模态质量推理。

### 主要贡献
- 提出首个专门针对3DGS场景的多模态质量评估框架，整合3D感知质量表示与多模态大语言模型推理。
- 引入结构感知的质量学习策略，融合深度和点云几何信息，弥补传统2D质量指标在空间结构方面的不足。
- 构建了基于Qwen的多模态推理机制，将视觉与几何数据联合输入，增强对3D场景质量的解释能力。

### 局限性
- 摘要未提供实验具体结果，无法定量评估方法性能（如与其他IQA或MLLM方法的对比结果）。
- 摘要未讨论模型的计算复杂度、推理速度或对多视图数量依赖性的分析。
- 未提及是否在多种3DGS渲染场景（如大规模场景、稀疏视图等）下验证鲁棒性。

### 阅读优先级：中
**理由**：该工作针对3DGS场景质量评估这一新兴且实用的方向，方法设计合理（结合几何线索与MLLM）。但由于摘要未提供关键性能数据（如准确率、与主流方法的对比），且发布日期标注为2026年（可能存疑），建议在获取完整实验细节或验证有效性后再决定是否深入阅读。对于从事3D场景重建与质量评估研究的读者，优先级可适度提高。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as an effective representation for novel view synthesis and 3D scene reconstruction, creating an increasing demand for reliable quality assessment. Unlike conventional image quality assessment (IQA), the quality of a 3DGS scene depends not only on the perceptual fidelity of rendered views, but also on scene-level factors such as spatial structure and cross-view consistency. Existing IQA methods are limited by their reliance on 2D perceptual cues, whereas general multimodal large language models (MLLMs) are not designed for stable quality regression and may produce unreliable judgments. To address these limitations, a multimodal quality assessment framework is developed for 3DGS scene understanding. First, a 3D-aware quality representation learning framework is introduced by augmenting a VGGT-based encoder with a dedicated quality head. Multi-view images are encoded into view-specific features and aggregated to capture cross-view consistency, while geometric cues are incorporated through joint modeling of depth and point-cloud-related structural information, enabling the learning of structure-aware quality representations beyond appearance-driven features. Second, a grounded multimodal reasoning mechanism is constructed by jointly feeding original images, depth maps, point cloud renderings, and camera parameters into a Qwen-based MLLM.

</details>

## Dynamic / 4D Reconstruction

### 2026-07

#### 2026-07-31 - OASIS: Occlusion-aware Single-image Hand Avatar Reconstruction via 3D Gaussian Splatting

**Authors:** Zhisheng Han, Shiyao Wu, Jiayan Qiu, Yakun Ju, Lu Liu, Le Zhang, Pengfei Feng, Huiyu Zhou, Zheheng Jiang
**Links:** [abs](https://arxiv.org/abs/2607.29633) - [pdf](https://arxiv.org/pdf/2607.29633)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** avatar reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Single-image 3D hand avatar reconstruction is fundamentally ill-posed and particularly challenging due to limited visual evidence under severe self-occlusion and the complex pose-dependent deformation of highly articulated hands. Existing methods predominantly rely on implicit NeRF-style representations, whose volumetric fitting is computationally expensive and often struggles to preserve fine-grained hand details. In this work, we present OASIS, a tailored 3D Gaussian Splatting framework for single-image hand avatar reconstruction. To faithfully encode sparse image-specific appearance cues in single-view reconstruction, we construct geometry-aligned visual evidence tokens by explicitly aligning input image observations with 3D hand geometry and context-adaptively tokenizing the resulting visual evidence. Since severe self-occlusion makes the reliability of image evidence inherently visibility-dependent, we introduce a visibility-conditioned point-image attention to reliably transfer visual evidence to geometric tokens, yielding occlusion-aware Gaussian features for faithful and robust reconstruction. To further capture non-rigid deformation of articulated hands, we introduce a Feature-on-Mesh representation to enable Gaussian deformation to be guided by local surface stretching. Under this framework, we adopt a one-shot adaptation scheme that learns a shared hand prior from multi-identity training data and then fits it to a target image for target-specific reconstruction. Extensive experiments show that OASIS outperforms existing baselines in both visual fidelity and efficiency across challenging poses and in-the-wild scenarios, and further demonstrates strong versatility in downstream applications such as text-to-avatar generation and texture editing.

</details>

#### 2026-07-30 - AdaAnchor4D: Anchor-Conditioned Spatiotemporal Feature Aggregation for Monocular UAV 4D Reconstruction

**Authors:** Peiyi Xu, Junpeng Zhang, Guanbin Li, Ronghua Shang, Mingtao Feng, Le Dong, Weisheng Dong, Guangming Shi, Jie Feng
**Links:** [abs](https://arxiv.org/abs/2607.28320) - [pdf](https://arxiv.org/pdf/2607.28320)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic scene reconstruction, dynamic reconstruction, dynamic Gaussian, scene reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AdaAnchor4D: Anchor-Conditioned Spatiotemporal Feature Aggregation for Monocular UAV 4D Reconstruction
- 作者：Peiyi Xu, Junpeng Zhang, Guanbin Li, Ronghua Shang, Mingtao Feng, Le Dong, Weisheng Dong, Guangming Shi, Jie Feng
- 出版日期：2026-07-30
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.28320

### 一句话总结
本文提出AdaAnchor4D，一种面向单目无人机视频动态场景重建的自适应锚点变形框架，通过锚点条件化的时空特征聚合提升复杂城市动态场景的渲染质量并保持实时性能。

### 研究问题
单目无人机视频中的复杂城市场景具有显著的时空异构性，不同区域遵循不同时间活动模式，且部分动态区域的运动状态随时间演变。现有基于分解共享时空特征场的动态高斯方法采用固定平面特征组合机制，难以适应此类异构局部动态，导致重影伪影和动态细节模糊。

### 核心思路/方法
- **Anchor-Conditioned Feature Aggregation (ACFA)**：利用锚点特有的聚合嵌入和时间信息，自适应聚合共享时空特征，使不同局部单元获得匹配自身局部状态和时间状态的动态表示。
- **Decoupled Local Geometry Deformation (DLGD)**：将锚点状态变形与局部高斯几何变形解耦。
- **Density-Adaptive Coordinate Warping (DACW)**：根据轴向上的锚点分布重新参数化特征查询坐标，缓解非均匀几何采样与均匀网格参数化之间的不匹配。

### 主要贡献
- 提出AdaAnchor4D，一种针对单目无人机动态场景重建的自适应锚点变形框架。
- 设计ACFA机制，实现锚点条件化的自适应时空特征聚合，适应场景异构局部动态。
- 提出DLGD与DACW，分别解耦几何变形并缓解采样与参数化不匹配问题。
- 在UAV-Arc4D、VisDrone和UAVDT数据集上实验表明，AdaAnchor4D在保持实时渲染性能的同时，相比代表性动态高斯方法取得了更高的渲染质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目无人机动态场景重建中时空异构性这一具体挑战，提出了三项机制创新（ACFA、DLGD、DACW），并在多个UAV基准上验证了渲染质量提升和实时性保留。结合所属动态/4D重建及神经场景渲染领域，对从事动态场景建模、无人机视觉和实时神经渲染研究的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular UAV videos provide valuable observations for dynamic reconstruction of complex urban scenes. However, such scenes exhibit pronounced spatiotemporal heterogeneity: different regions follow distinct temporal activity patterns, while the motion states of some dynamic regions may further evolve over time. Although dynamic Gaussian methods based on decomposed shared spatiotemporal feature fields have achieved efficient and accurate reconstruction in object-centric or relatively compact scenes, their commonly adopted fixed plane-wise feature combination mechanisms are less suited to the heterogeneous local dynamics of UAV scenes, often leading to ghosting artifacts and blurred dynamic details. To address this challenge, we propose AdaAnchor4D, an adaptive anchor deformation framework for monocular UAV dynamic scene reconstruction. At its core, Anchor-Conditioned Feature Aggregation (ACFA) adaptively aggregates shared spatiotemporal features using anchor-specific aggregation embeddings and temporal information, allowing different local units to obtain dynamic representations tailored to their local and temporal states. Decoupled Local Geometry Deformation (DLGD) separates anchor-state deformation from local Gaussian geometry deformation, while Density-Adaptive Coordinate Warping (DACW) reparameterizes feature-query coordinates according to the axis-wise anchor distributions, alleviating the mismatch between non-uniform geometric sampling and uniform grid parameterization. Experiments on UAV-Arc4D, VisDrone, and UAVDT show that AdaAnchor4D achieves higher rendering quality than representative dynamic Gaussian methods while maintaining real-time rendering performance. The code will be made publicly available.

</details>

#### 2026-07-30 - S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image

**Authors:** Hail Song, Seokhwan Yang, Jiwon Yang, Woojin Cho, Woontack Woo
**Links:** [abs](https://arxiv.org/abs/2607.28164) - [pdf](https://arxiv.org/pdf/2607.28164)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** dynamic 3D, avatar reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, AR, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image
- 作者：Hail Song, Seokhwan Yang, Jiwon Yang, Woojin Cho, Woontack Woo
- 出版日期：2026-07-30
- 分类：Dynamic / 4D Reconstruction；子分类：Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.28164

### 一句话总结
S-Avatar 提出一种从单张图像生成逼真 3D 头部虚拟形象的方法，通过扩散引导的 3D 高斯生成和 FLAME 参数模型驱动，实现动态渲染与新视角、表情下的高一致性。

### 研究问题
如何从单张图像重建头部 3D 虚拟形象，并解决现有方法在未见视角下 3D 一致性不足的问题，同时支持实时动态驱动。

### 核心思路/方法
采用三阶段流程：
1. 利用基于扩散的高斯生成模块，从单张图像直接合成高分辨率 3D 高斯溅射（3DGS）。
2. 将参数化头部模型 FLAME 与生成的 3DGS 对齐，通过优化其参数和空间变换实现匹配。
3. 构建绑定模板（binding template），编码初始高斯溅射与 FLAME 之间的空间关系，从而将 3DGS 适配至 FLAME 的变化，实现实时动态形变与渲染。

### 主要贡献
- 提出扩散引导的单图 3DGS 生成模块，结合 FLAME 控制实现高质量头部虚拟形象构建。
- 引入绑定模板策略，使 3DGS 能适应 FLAME 参数变化，支持实时动态渲染。
- 公开数据集上的评估显示，该方法在新视角和表情生成任务上优于现有最先进方法，具备更高真实感和一致性。
- 为 VR/AR 等应用提供了高效且易访问的虚拟形象创建途径。

### 局限性
摘要未提供足够信息，未详细说明方法在极端姿态、遮挡、非正面光照或训练数据依赖等方面的潜在限制，也未给出定量误差或失败案例分析。

### 阅读优先级
**高**  
理由：论文聚焦单图头部虚拟形象重建这一热门且具有实际应用价值的方向，结合扩散模型与 3DGS，方法新颖且宣称优于现有技术，并支持实时动态渲染，适合关注 3D 重建、神经渲染及 VR/AR 应用的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

We propose S-Avatar, a novel method for generating photorealistic 3D head avatars from a single image using a diffusion-guided 3D model generation module and strategies for animating 3D Gaussian Splatting (3DGS). While single-image head avatar reconstruction is crucial for lifelike Virtual Reality (VR) applications, existing approaches often struggle to preserve 3D consistency under unseen viewpoints. S-Avatar addresses this limitation through a three-stage pipeline. First, a high-resolution 3DGS is synthesized directly from a single image using a diffusion-based Gaussian splat generation module. Next, the parametric head model FLAME is aligned with the generated 3DGS by optimizing its parameters and spatial transformations. Finally, to adapt the 3DGS to FLAME variations, we construct a binding template that encodes the spatial relationship between the initial splats and FLAME. The dynamic 3D head avatar can then be rendered in real time by deforming the 3DGS with the binding template. By combining diffusion-guided canonical 3DGS generation with FLAME-based control, our method achieves efficient and accurate reconstruction with enhanced 3D consistency. Evaluations on public datasets demonstrate that S-Avatar outperforms state-of-the-art methods in novel-view and expression generation, achieving superior realism and consistency. Consequently, our approach represents a significant advance in accessible avatar creation, applicable to a wide range of VR/AR applications. The project page is available at https://github.com/hailsong/savatar.

</details>

#### 2026-07-28 - SplatStream: Fine Granular Scalable Gaussian Splatting for Adaptive 3D Scene Streaming

**Authors:** Muhammad Talha, William Gordon, Sajid Umair, Zhu Li, Anique Akhtar, Joel Jung
**Links:** [abs](https://arxiv.org/abs/2607.25971) - [pdf](https://arxiv.org/pdf/2607.25971)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, dynamic Gaussian, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatStream: Fine Granular Scalable Gaussian Splatting for Adaptive 3D Scene Streaming
- 作者：Muhammad Talha, William Gordon, Sajid Umair, Zhu Li, Anique Akhtar, Joel Jung
- 出版日期：2026-07-28
- 分类：Dynamic / 4D Reconstruction（主分类）；Neural Scene Representations & Rendering（副分类）
- 链接：摘要：https://arxiv.org/abs/2607.25971 ；PDF：https://arxiv.org/pdf/2607.25971

### 一句话总结
提出一个名为 SplatStream 的细粒度可伸缩高斯泼溅框架，用于动态3D场景的适应性流传输，通过质量/分辨率分层、层间预测编码、B帧时域扩展及体积-不透明度重要性度量，实现低延迟、带宽自适应的流媒体传输。

### 研究问题
动态3D高斯泼溅（GS）表征尺寸大、帧间冗余高，导致其在适应性流传输场景下（如带宽波动环境）面临显著挑战。

### 核心思路/方法
1. **空间可伸缩性**：将GS场景分解为质量层和分辨率层，引入层间预测编码实现可伸缩性。
2. **时域可伸缩性**：引入B帧以提供时域质量可伸缩性。
3. **预测机制**：使用轻量级基于跨层Transformer的预测器，用于跨层和时域预测。
4. **重要性分组**：基于体积-不透明度度量对高斯原语进行细粒度打包，优先传输视觉重要性高的原语，实现渐进式细化。
5. **流传输适配**：将可伸缩GS比特流映射为兼容MPEG-DASH的子表示结构，支持细粒度自适应、低延迟传输。

### 主要贡献
1. 提出一种细粒度可伸缩的高斯泼溅框架，支持动态3D场景的适应性流传输。
2. 引入跨层预测编码和B帧机制，实现空间与时域的可伸缩性。
3. 利用体积-不透明度重要性度量进行高斯原语分组与优先传输，提升渐进式反馈质量。
4. 将可伸缩比特流与MPEG-DASH流媒体标准对接，实现在带宽波动下的低延迟自适应传输。

### 局限性
摘要未提供足够信息。该部分需阅读全文后分析。

### 阅读优先级
**高**。理由：该工作针对动态高斯泼溅在流传输中的核心难点——表征冗余与带宽适配——提出了完整的可伸缩方案，并涉及层间预测、Transformer、MPEG-DASH标准对接等多个技术点，对NeRF/3D GS领域及多媒体流传输研究均有参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (GS) enables high quality real-time rendering for immersive media, but its large representation size and frame-wise redundancy create significant challenges for adaptive streaming. This paper presents SplatStream, a fine granular scalable Gaussian splatting framework for dynamic 3D scene delivery. The proposed method decompose the GS scenes into quality and resolution layers, and introduces inter-layer predictive coding to achieve scalability. For temporal direction, B-frames are introduced to have temporal quality scalability. A lightweight cross-layer transformer based predictor is utilized for both cross layer and temporal predictions. In addition, a volume-opacity based importance measure is used for fine-grained Gaussian packetization, allowing visually important primitives to be transmitted earlier for progressive refinement. Finally, the scalable GS bitstream is mapped to an MPEG-DASH compatible sub-representation structure, enabling fine granular adaptive, low-latency delivery of dynamic Gaussian splatting content under bandwidth-varying conditions.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-07

#### 2026-07-30 - Beyond Visual Ambiguity: Guiding Robust Monocular Depth Estimation in Challenging Scenarios via Detailed Long Captions

**Authors:** Junrui Zhang, Jiaqi Li, Yiran Wang, Liao Shen, Zhiguo Cao
**Links:** [abs](https://arxiv.org/abs/2607.28285) - [pdf](https://arxiv.org/pdf/2607.28285)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond Visual Ambiguity: Guiding Robust Monocular Depth Estimation in Challenging Scenarios via Detailed Long Captions
- 作者：Junrui Zhang, Jiaqi Li, Yiran Wang, Liao Shen, Zhiguo Cao
- 出版日期：2026-07-30T14:32:02Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.28285

### 一句话总结
本文提出CapDepth框架，利用详细长文本描述作为语言引导，以缓解单目深度估计在非朗伯表面和恶劣天气等挑战场景中的视觉歧义问题。

### 研究问题
单目深度估计（MDE）在非朗伯表面和恶劣天气条件下，由于单张图像信息有限导致视觉歧义，现有方法通常孤立地通过图像修复或增强处理这些场景，鲁棒性提升有限。基于此，本文研究如何借助语言模态的详细长描述能力，有效引导深度估计模型应对这些挑战场景。

### 核心思路/方法
本文提出CapDepth框架，核心包括三个设计：
1. **详细长描述输入模板**：显式编码多个原子句子之间的丰富空间关系，为模型提供更全面的场景信息。
2. **动态描述编码器**：通过渐进式掩码注意力机制，从长描述中提取细粒度的、与深度相关的文本特征。
3. **文本自适应解码器**：利用稳定的自适应层归一化，用文本特征引导增强的深度解码过程。

### 主要贡献
- 提出CapDepth框架，首次将详细长描述系统地用于引导单目深度估计，缓解挑战场景中的视觉歧义。
- 设计详细长描述输入模板、动态描述编码器和文本自适应解码器三个组件，分别解决先前语言集成MDE方法中文本信息有限、全局文本特征粗糙、深度解码阶段语言引导不足的问题。
- 在实验中，CapDepth在非朗伯表面场景深度误差降低25.0%，恶劣天气条件下降低22.0%，优于现有最先进方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目深度估计中具有实际挑战性的场景（非朗伯表面、恶劣天气）提出了创新性的语言引导框架，报告的性能提升幅度较大（误差降低超过20%），且研究问题明确、方法设计有针对性，对视觉-语言模型与深度估计交叉方向具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation (MDE) faces challenges with non-Lambertian surfaces and adverse weather conditions due to the visual ambiguities inherent in single-image limited information. Existing works address them in isolation via image inpainting or augmentation, yielding limited robustness gains. Language, as a powerful complementary modality to vision, is demonstrated to enhance the visual perception capabilities of vision-language models (VLMs) via detailed long captions. However, prior language-integrated MDE methods fail to fully harness this potential due to short text input with limited information, coarse global text feature learning, and limited language guidance during depth decoding. To address these limitations, we propose CapDepth, a novel framework for robust MDE that leverages guidance from detailed long captions to alleviate visual ambiguities in both challenging scenarios. First, we design a detailed long caption input template that explicitly conveys rich spatial relationships among multiple atom sentences. Second, a dynamic caption encoder is introduced to extract fine-grained depth-relevant text features via progressive masked attention. Finally, we propose a text-adaptive decoder that guides enhanced depth decoding with text features via stable adaptive layer normalization. Extensive experiments validate the efficacy of CapDepth, which outperforms state-of-the-art methods, achieving depth error reductions of 25.0% on non-Lambertian surfaces and 22.0% under adverse weather conditions.

</details>

#### 2026-07-30 - Convolutional Neural Shading for High-Quality 3D Reconstruction from Multi-View Images

**Authors:** Juheon Hwang, Taewan Kim, Heeseok Oh, Jiwoo Kang
**Links:** [abs](https://arxiv.org/abs/2607.28132) - [pdf](https://arxiv.org/pdf/2607.28132)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, differentiable rendering, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Convolutional Neural Shading for High-Quality 3D Reconstruction from Multi-View Images
- 作者：Juheon Hwang, Taewan Kim, Heeseok Oh, Jiwoo Kang
- 出版日期：2026-07-30
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.28132

### 一句话总结
本文提出一种名为卷积神经着色（CNS）的新管线，通过引入卷积神经着色器和细粒度位移网络，从多视图图像重建更高质量的3D形状。

### 研究问题
如何克服现有神经可微渲染方法中仅使用单点几何信息（如表面位置和法线）导致的局部几何细节缺失问题，特别是在暗区和无纹理区域，以及图像边界处的表面不规则性。

### 核心思路/方法
- 采用**卷积神经着色器（convolutional neural shader）**替代单点着色模型，利用卷积操作捕捉表面邻域信息，从而在暗区和无纹理区域也能捕获几何变化，提升几何预测精度。
- 引入**细粒度位移网络（fine-detail displacement network）**，利用表面几何的空间信息，在渲染坐标中关联相邻值以学习精细位移细节，从而缓解图像边界处的表面不规则问题。

### 主要贡献
- 提出一种新的CNS管线，将卷积神经着色用于多视图3D重建，有效克服单点信息局限。
- 设计细粒度位移网络，改善图像边界处的表面质量。
- 实验表明，与当前最先进方法相比，重建形状和渲染图像质量均有显著提升。

### 局限性
摘要未提供足够信息；摘要中未提及方法在极端几何、大规模场景、计算开销、训练时间或泛化性等方面的潜在限制。

### 阅读优先级
**高**。理由：该工作针对神经辐射场/神经渲染在几何细节重建中的核心瓶颈提出新思路，且实验显示质量提升显著，属于近期多视图重建与神经渲染方向的前沿方法，适合该领域研究者跟进。

</details>

<details>
<summary>Abstract</summary>

We propose a convolutional neural shading (CNS), a novel pipeline to reconstruct high-quality 3D shapes from multi-view images. Several recent studies have used neural radiance fields and other neural differentiable rendering methods to understand 3D geometry. However, these approaches rely on single-point geometric information, such as positions and normals of the surface, leading to a lack of detailed local geometry. Our approach addresses the inherent limitations of single-point information by leveraging a neural shader to capture variations even in dark and textureless regions with a convolutional neural shader, resulting in far more accurate geometry predictions. Additionally, our method mitigates surface irregularities at image boundaries by introducing a fine-detail displacement network, which utilizes spatial information of surface geometry and learns fine displacement details by correlating neighboring values in the rendering coordinates. Through extensive experiments, our proposed method has demonstrated significant quality improvements in the reconstructed shapes and rendered images over current state-of-the-art methods.

</details>

#### 2026-07-30 - Endo-NeRF++: Uncertainty-Aware Neural Rendering with Multi-Resolution Hash Encoding for Dynamic Surgical Scene Reconstruction

**Authors:** Gousia Habib, Laura Ruotsalainen
**Links:** [abs](https://arxiv.org/abs/2607.27825) - [pdf](https://arxiv.org/pdf/2607.27825)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, NeRF, neural rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Endo-NeRF++: Uncertainty-Aware Neural Rendering with Multi-Resolution Hash Encoding for Dynamic Surgical Scene Reconstruction
- 作者：Gousia Habib, Laura Ruotsalainen
- 出版日期：2026-07-30
- 分类：3D Reconstruction & Multi-view Geometry（次要分类：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2607.27825

### 一句话总结
Endo-NeRF++是一种面向动态手术场景的神经渲染框架，通过多分辨率哈希编码、时空特征融合与不确定性引导的自适应采样，在变形内镜场景中提升了重建精度和时间一致性。

### 研究问题
如何在存在组织变形、遮挡、镜面反射和受限视角的动态手术场景中，实现高精度且时间连贯的神经渲染重建。

### 核心思路/方法
在EndoNeRF基础上扩展，引入三项关键机制：
1. 多分辨率哈希网格编码，同时捕捉粗粒度和细粒度的解剖细节；
2. 时间特征融合，在组织变形和手术工具遮挡期间维持稳定的重建；
3. 不确定性引导的自适应采样，将更多采样点分配到不确定性高的区域，从而提升渲染质量和几何连贯性。

### 主要贡献
- 提出Endo-NeRF++框架，将不确定性估计引入动态手术场景的神经渲染；
- 结合多分辨率哈希编码和时序特征融合，有效处理形变与遮挡；
- 不确定性驱动的自适应采样机制，在机器人手术视频序列上较EndoNeRF基线取得显著提升：PSNR最高提升1.22 dB（4.3%），SSIM最高提升5.3%，LPIPS最高降低55.1%。

### 局限性
摘要未提供足够信息，无法获知该方法在计算开销、泛化能力、不同手术类型或更长视频序列上的表现，也未提及与除EndoNeRF外其他方法的比较或失败案例。

### 阅读优先级
**中**  
理由：该工作针对手术场景重建这一特定领域，方法上有明确创新（不确定性引导采样+多分辨率哈希编码），并与基线取得了可观提升，适合关注神经渲染或医学影像重建的读者；但摘要未提供实验设置细节和更广泛对比，普适性和方法局限尚不明朗，可不作为紧急必读。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic surgical scenes is crucial for robot-assisted minimally invasive surgery; however, it continues to be difficult because of tissue deformation, occlusions, specular reflections, and restricted viewpoints. In this study, we introduce Endo-NeRF++, a neural rendering framework that accounts for uncertainty in the reconstruction of dynamic surgical scenes. Expanding on EndoNeRF, the suggested approach incorporates multi-resolution hash-grid encoding, temporal feature merging, and uncertainty-informed adaptive sampling to enhance reconstruction accuracy and temporal coherence in deformable endoscopic scenes.The multi-resolution hash-grid representation within the framework effectively captures both coarse and fine anatomical details, while temporal feature blending ensures stable reconstruction during tissue deformation and surgical tool occlusions. Additionally, uncertainty-driven adaptive sampling assigns more samples to uncertain areas to enhance rendering quality and geometric coherence. Experiments on robotic surgical video sequences demonstrate that the proposed uncertainty-guided adaptive sampling improves PSNR by up to 1.22\,dB (4.3\%), increases SSIM by up to 5.3\%, and reduces LPIPS by up to 55.1\% compared with the EndoNeRF baseline.

</details>

#### 2026-07-30 - EgoGVAE: Ego-body Mesh Reconstruction via Guided Variational Autoencoder

**Authors:** Jaehun Jung, Wonjun Kim
**Links:** [abs](https://arxiv.org/abs/2607.27755) - [pdf](https://arxiv.org/pdf/2607.27755)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** mesh reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoGVAE: Ego-body Mesh Reconstruction via Guided Variational Autoencoder
- 作者：Jaehun Jung, Wonjun Kim
- 出版日期：2026-07-30
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.27755

### 一句话总结
本文提出一种基于引导变分自编码器的单步推理方法，仅利用头部姿态即可快速重建全身网格，推理速度比扩散式方法快50倍以上。

### 研究问题
如何仅从头部姿态（单一关节轨迹）恢复未观察到的全身姿态与网格，同时避免扩散模型迭代过程带来的高计算成本和时间开销。

### 核心思路/方法
- 构建一个以全身姿态为输入的引导网络（变分自编码器），学习全身姿态的潜在分布。
- 设计一个头到运动的网络（head-to-motion network），使其学习到的潜在分布与引导网络的分布对齐。
- 推理时从头姿态采样的“引导分布”潜在特征可直接解码为自然的全身姿态，仅需单步采样即可完成重建，无需迭代。

### 主要贡献
- 提出一种简洁新颖的引导变分自编码器框架，利用潜在空间对齐实现高效全身网格重建。
- 相比扩散式方法，推理速度提升超过50倍（单步采样）。
- 在基准数据集上验证了该方法在ego-body网格重建任务中的有效性和性能提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法在保证全套姿重建质量的同时，将推理速度提升至扩散模型的50倍以上，对头戴设备/智能眼镜等实时应用具有重要意义；且方法简洁，潜在空间对齐思路具有可扩展性，适合关注高效人体重建与生成模型的读者。

</details>

<details>
<summary>Abstract</summary>

We address the problem of recovering the full-body mesh from only the head pose. This task has become essential for various applications based on head-mounted devices or smart glasses. The challenge of this task lies in estimating the pose information of unobserved body parts based solely on a single joint (i.e., head) trajectory. Several studies have begun to adopt head-conditioned generative models, however, such previous methods are costly and time-consuming due to the diffusion-based iterative process. As an alternative, we propose a simple yet novel method that leverages the latent space of the guidance network, which is designed as a variational autoencoder taking full-body poses as inputs. By enforcing latent distributions of this guidance network and our head-to-motion network to be similar, latent features sampled from the 'guided' distribution, i.e., distribution learned in our head-to-motion network, can be reliably decoded for natural representations of full-body poses even only with the head pose. One important advantage of the proposed method is that one-step sampling scheme achieves remarkably fast inference (more than 50 times faster) compared to diffusion-based approaches. Experimental results on benchmark datasets show that the proposed method efficiently improves the performance of ego-body mesh reconstruction.

</details>

#### 2026-07-29 - VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion

**Authors:** Zador Pataki, Paul-Edouard Sarlin, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2607.27194) - [pdf](https://arxiv.org/pdf/2607.27194)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** image matching, structure from motion, SfM, simultaneous localization and mapping, SLAM, monocular depth, camera calibration, mapping, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion
- 作者：Zador Pataki, Paul-Edouard Sarlin, Marc Pollefeys
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2607.27194

### 一句话总结
本文提出VidMap系统，通过融合SLAM的时序约束与离线SfM的全局优化能力，实现了任意未校准长视频的度量重建。

### 研究问题
现有视频位姿恢复方法存在局限：SLAM依赖初始化、对瞬态故障敏感且需已知相机校准；SfM忽略图像顺序，在视觉对称和极端运动场景下鲁棒性不足。因此，该文致力于解决如何结合两种方法的优势，实现鲁棒且准确的视频度量重建。

### 核心思路/方法
- 结合SLAM的强时序约束与SfM的全局优化灵活性，将时间顺序作为闭环检测的关键信息。
- 利用近期宽基线密集图像匹配的进展提升匹配质量。
- 使用度量单目深度先验增强全局优化过程。

### 主要贡献
- 提出一种新系统，融合SLAM时序约束与离线SfM全局优化，支持未校准视频的度量重建。
- 将时序信息作为闭环检测的“一等公民”，提升可靠性。
- 在包含极端运动和视觉对称的多样困难数据集上，比现有经典/学习的SLAM和SfM方法（无论是否已知校准）更鲁棒、更准确。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该文针对视频重建领域SLAM与SfM的矛盾提出融合方案，技术思路清晰且实验验证鲁棒性优势，适合对3D重建、视觉SLAM或机器人导航感兴趣的读者；但摘要未提及具体性能指标与消融实验细节，需进一步阅读正文判断方法可复现性和实际效果。

</details>

<details>
<summary>Abstract</summary>

Accurately recovering the camera's calibration and metric poses for any unconstrained video would unlock large-scale training data for navigation and scene understanding. The dominant approaches to this problem are severely limited: Simultaneous Localization and Mapping (SLAM) is sensitive to initialization and transient failures due to its causal, incremental nature; it is often over-optimized for real-time operation and generally requires known camera calibration; while Structure-from-Motion (SfM) typically forgoes any image ordering, enabling optimal initialization and global optimization, but lacks robustness to visual symmetries and extreme motions. To bridge this gap, we introduce a system that combines the strong sequential constraints of SLAM with the flexibility and global optimization of offline SfM, enabling the metric reconstruction of arbitrary, long, uncalibrated videos. This system leverages recent advances in wide-baseline dense image matching, treats temporal ordering as a first-class citizen for reliable loop closure, and augments global optimization with metric monocular depth priors. As a result, thorough evaluations on diverse, challenging datasets that exhibit extreme motion and visual symmetries reveal that our approach is significantly more robust and accurate than both state-of-the-art SLAM and SfM, classical or learned, with given or unknown camera calibration. The code is publicly available at https://github.com/cvg/vidmap.

</details>

#### 2026-07-29 - Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for Decision-Critical Applications

**Authors:** Piyush Jain, Kousik Dasgupta, Rajarshi Roy, Subarna Tripathi
**Links:** [abs](https://arxiv.org/abs/2607.27145) - [pdf](https://arxiv.org/pdf/2607.27145)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, monocular depth, embodied AI, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for Decision-Critical Applications
- 作者：Piyush Jain, Kousik Dasgupta, Rajarshi Roy, Subarna Tripathi
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry; Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.27145

### 一句话总结
本文提出ByDeWay-V2框架，通过向多模态大语言模型（MLLM）的提示中注入显式的空间关系谓词和深度线索，在无需训练的情况下提升了空间推理的准确性和可审计性，尤其适合资源受限的实时决策场景。

### 研究问题
多模态大语言模型在关键决策应用（如机器人、具身AI）中，其空间判断不透明且存在细粒度空间理解不足和物体幻觉问题；现有方法（如ByDeWay的LDP）在处理同一几何平面内物体间的投影和拓扑空间关系时表现不足。

### 核心思路/方法
- 采用开放词汇物体检测器（YOLO-World-L）计算图像中检测到的物体之间的成对几何关系。
- 将这些关系转化为人类可读的结构化空间谓词（如“left of”、“inside”等），并将其与深度线索（来自单目深度估计）一起注入MLLM的提示中。
- 整个流程无需训练，将3D场景深度与2D空间语义桥接，同时提供可审计的证据以支持下游决策。

### 主要贡献
1. 提出了ByDeWay-V2框架，通过显式空间关系谓词增强MLLM的空间推理能力，同时保持可解释性。
2. 在VSR和BLINK空间推理子集上，该框架显著提升了多个MLLM的性能：例如在BLINK空间子集上，对于Qwen2.5-VL，相对于LDP方法F1分数相对提升46%；将BLIP-Base在VSR上的近乎随机性能恢复至F1=0.53。
3. 提供轻量级配置（在CPU上仅需40个token上下文预算），证明了框架在资源受限实时决策场景中的适用性。

### 局限性
摘要未提供足够信息（如具体失败案例、对其他任务或更大模型的影响、深度估计误差的影响等）。

### 阅读优先级
中
- 理由：该工作专注于视觉空间推理这一具体方向，并提出了实用的轻量级改进方法（无需训练）。对于从事具身AI、机器人及可解释AI的研究者有一定参考价值，但对于广义的计算机视觉或语言模型研究者，其方法限定性较强。

</details>

<details>
<summary>Abstract</summary>

As Multimodal Large Language Models (MLLMs) are increasingly deployed in decision-critical pipelines such as robotics, embodied AI, and safety monitoring, the opacity of their spatial judgments limits operator trust and auditability. MLLMs demonstrate strong reasoning but often struggle with fine-grained spatial understanding and object hallucination. Prior work, ByDeWay, introduced Layered-Depth-Based Prompting (LDP), a training-free framework that mitigates hallucinations by structuring prompts using monocular depth estimation. However, coarse depth layering falls short in resolving object-to-object spatial relationships within the same geometric plane, such as projective ("left of", "above") and topological ("inside", "touching") relations. We propose ByDeWay-V2, which integrates explicit spatial relational context alongside depth cues, expressed as human-readable predicates that serve as auditable evidence for downstream decision support. Using an open-vocabulary object detector (YOLO-World-L), our framework computes pairwise geometric relations between detected objects and injects them as structured spatial predicates into the MLLM prompt, bridging 3D scene depth and 2D spatial semantics without any training. We evaluate ByDeWay-V2 on the Visual Spatial Reasoning (VSR) and BLINK benchmarks across multiple MLLMs, with hallucination grounding assessed via POPE. On the BLINK spatial subset, ByDeWay-V2 achieves a 46 percent relative F1 improvement over LDP for Qwen2.5-VL, and recovers BLIP-Base's spatial reasoning on VSR from near-random performance to a competitive F1 of 0.53. Our lightest configuration operates under a strict 40-token context budget on CPU, showing the framework's suitability for resource-constrained, real-time decision-support settings.

</details>

#### 2026-07-29 - JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation

**Authors:** Ionuţ Grigore, Călin-Adrian Popa
**Links:** [abs](https://arxiv.org/abs/2607.26600) - [pdf](https://arxiv.org/pdf/2607.26600)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation
- 作者：Ionuţ Grigore, Călin-Adrian Popa
- 出版日期：2026-07-29
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2607.26600

### 一句话总结
JEPADepth 提出一种自监督单目深度估计方法，在标准光度损失基础上，引入基于I-JEPA的掩码预测表示学习损失，以提升模型性能，且在推理时不增加额外开销。

### 研究问题
如何通过引入掩码预测表示学习来增强自监督单目深度估计中基于光度重建损失的训练效果，同时不改变推理时的模型结构。

### 核心思路/方法
1. 在标准光度重建流程上，增加一个基于预训练DINOv3 Vision Transformer编码器的掩码预测损失（JEPA目标）。
2. 该损失在表示空间中计算：一个预测器根据可见上下文区域的嵌入，推断被掩码的目标区域嵌入；目标编码器和预测器仅在训练阶段使用，推理时丢弃。
3. 整体框架在KITTI上训练，与同一DINOv3光度基线对比，性能有提升。

### 主要贡献
摘要未提供足够信息以提取独立贡献列表。从摘要可推断：提出了一种结合I-JEPA的掩码预测损失与光度损失的深度估计框架，在三个公开基准（KITTI、Make3D、Cityscapes）上取得有竞争力的结果，尤其在零样本迁移场景下达到最佳或接近最佳性能。

### 局限性
摘要未提供关于局限性、失败案例或计算成本等信息，因此无法进行分析。

### 阅读优先级
中  
理由：该方法在自监督深度估计领域表现出竞争力，零样本迁移性能突出，但创新点主要是将现有I-JEPA损失嫁接到光度框架上，且实验细节未深入给出。如关注自监督表示学习与深度估计结合，可阅读；若需理论突破或详尽实验分析，优先级较低。

</details>

<details>
<summary>Abstract</summary>

Self-supervised monocular depth estimation typically relies on photometric reconstruction losses that couple depth, pose, and appearance assumptions. In this paper, we propose JEPADepth, a self-supervised monocular depth framework that incorporates a complementary training objective inspired by Image Joint-Embedding Predictive Architectures (I-JEPA) for self-supervised depth learning. Our method augments a standard photometric pipeline with a masked prediction loss computed in the representation space of a pretrained DINOv3 Vision Transformer encoder. A predictor infers target-region embeddings from visible context-region embeddings under structured masking, and is discarded along with the target encoder at inference time, adding no deployment cost. On KITTI, adding the JEPA objective consistently improves performance over the same DINOv3-based photometric baseline, without changing the inference-time architecture. Compared to prior monocular self-supervised methods, JEPADepth is competitive with state-of-the-art transformer-based approaches and outperforms strong CNN-based baselines on the standard benchmark. In zero-shot transfer (trained on KITTI and evaluated without fine-tuning), JEPADepth achieves the best or near-best performance among the compared methods on both Make3D and Cityscapes across multiple metrics.

</details>

#### 2026-07-28 - HOME: Robust Hough-space Matching Method for Structured and Textureless Videos

**Authors:** Masaki Satoh
**Links:** [abs](https://arxiv.org/abs/2607.25389) - [pdf](https://arxiv.org/pdf/2607.25389)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, pose estimation, feature matching, robotics, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HOME: Robust Hough-space Matching Method for Structured and Textureless Videos  
- 作者：Masaki Satoh  
- 出版日期：2026-07-28  
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications  
- 链接：摘要：https://arxiv.org/abs/2607.25389 ；PDF：https://arxiv.org/pdf/2607.25389  

### 一句话总结
提出一种基于霍夫空间的超轻量、免训练特征匹配框架HOME，通过将图像中的全局线性结构映射为稳定局部极值，将复杂线条匹配简化为高效的一维点匹配，在结构化和无纹理场景中实现鲁棒且快速的单应性估计。

### 研究问题
如何在计算资源有限的边缘设备上，针对结构化环境（强线性结构）或无纹理表面，实现高效、鲁棒的视觉特征匹配，从而解决现有基于点特征（如ORB）在这些场景中频繁失败、而基于线条的SLAM方法计算量过大的瓶颈问题。

### 核心思路/方法
1. **霍夫空间变换**：将输入图像转换到霍夫空间，把全局线性结构映射为稳定的局部极值，并将这些极值作为关键点。  
2. **一维点匹配**：将复杂的线条匹配问题重构成高效的一维点匹配任务。  
3. **一维径向描述子**：设计具有数学保证的旋转和平移不变性的描述子，无需显式估计方向，降低计算开销。  
4. **验证方式**：以单应性估计作为概念验证，评估匹配精度和效率。

### 主要贡献
- 提出HOME框架，首次将线条匹配通过霍夫空间转换为轻量级的一维点匹配，避免了传统线条提取与描述的昂贵计算。  
- 数学上保证了一维径向描述子的旋转和平移不变性，无需方向估计步骤。  
- 实验表明：在基于点特征方法失败的结构化/无纹理场景中，HOME仍能实现鲁棒配准，且运行速度远快于现有基于线条的方法。

### 局限性
- 摘要仅说明本文聚焦于单应性估计作为概念验证，未提供全3D位姿估计的实验细节。  
- 摘要未提供任何关于算法实时性定量数据、与其他方法的具体速度对比数值、以及在更多场景下的鲁棒性测试结果。  
- 摘要明确提及“将稳健匹配引擎扩展到全3D位姿估计仍是未来方向”，表明当前工作尚未覆盖3D位姿估计。  

### 阅读优先级
**高**  
理由：该方法针对边缘计算中的实时匹配瓶颈提出新颖且轻量的思路，在结构化和无纹理场景中具有显著优势。尽管当前验证限于2D单应性估计，但其基础框架对机器人、AR等实时应用具有潜在价值，适合对轻量化特征匹配感兴趣的研究者。

</details>

<details>
<summary>Abstract</summary>

Visual front-ends for robotic localization typically rely on point-based features such as Oriented FAST and Rotated BRIEF (ORB), which frequently fail in structured environments dominated by strong linear structures or textureless surfaces. While line-based Simultaneous Localization and Mapping (SLAM) systems mitigate this by utilizing line segments, conventional line extraction and description algorithms are computationally prohibitive for real-time edge robotics. To address this fundamental bottleneck, we propose HOME (Hough-space One-dimensional Matching of Extrema), an ultra-lightweight, training-free feature matching framework. HOME transforms images into Hough space, mapping global linear structures to stable local extrema, which serve as keypoints, thereby reformulating complex line matching into highly efficient one-dimensional point matching. The proposed 1D radial descriptor mathematically guarantees rotational and translational invariance without the overhead of explicit orientation estimation. As a proof of concept to validate the matching accuracy and efficiency of HOME, this paper focuses on homography estimation. Extensive evaluations demonstrate that HOME achieves robust registration in challenging scenarios where point-based methods fail, operating at a much faster speed than existing line-based methods. Extending this robust matching engine to full 3D pose estimation remains a highly promising future direction.

</details>

#### 2026-07-28 - WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing

**Authors:** Prathyush Sajith, Emadeldeen Hamdan, Ahmet Enis Cetin
**Links:** [abs](https://arxiv.org/abs/2607.25234) - [pdf](https://arxiv.org/pdf/2607.25234)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, stereo depth, robotics, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing
- 作者：Prathyush Sajith, Emadeldeen Hamdan, Ahmet Enis Cetin
- 出版日期：2026-07-28
- 分类：3D Reconstruction & Multi-view Geometry（主要），Embodied / Robotics / AR Applications（次要）
- 链接：摘要：https://arxiv.org/abs/2607.25234；PDF：https://arxiv.org/pdf/2607.25234

### 一句话总结
本文提出用数据无关的Walsh-Hadamard token mixer替代立体深度估计Transformer中的全局自注意力，在对数线性复杂度下保持精度，并引入混合对数视差损失以提升远距离物体估计性能。

### 研究问题
立体深度估计算法（用于驾驶、机器人和增强现实）需在高分辨率下快速运行，而基于Transformer的立体匹配器中，全局自注意力的计算复杂度随像素数平方增长，成为推理延迟的主要瓶颈。

### 核心思路/方法
1. 将立体Transformer中的联合自注意力阶段替换为数据无关的Walsh-Hadamard token mixer，该混频器在变换域以对数线性成本全局混合token，而保留数据相关的交叉注意力用于左右视图对应。
2. 引入混合对数视差损失函数，对代表远距离物体的小视差像素赋予更高权重，以提升远处物体估计精度且不增加额外计算开销。

### 主要贡献
- 提出Walsh-Hadamard token mixer替代全局自注意力，在合成驾驶数据上将模型计算量降低2.46倍，单图像推理延迟降低2.65倍，且端点误差与注意力基线持平。
- 通过复杂度分析揭示该方法优势受序列长度与通道宽度比值主导，解释了其在高分辨率立体匹配中的适用性及在分类Transformer中的不适用性，并在非立体长序列基准上验证了这种token-通道缩放规律。
- 引入混合对数视差损失，在不增加计算开销的前提下减少远距离物体的误差。

### 局限性
摘要未提供足够信息。摘要未讨论模型在真实驾驶/机器人数据上的鲁棒性、泛化能力、硬件部署细节，也未对比其他高效注意力变体或提供消融实验的量化误差率。

### 阅读优先级
高  
理由：该工作直接针对立体深度估计的实时性核心瓶颈，提供了理论清晰（复杂度分析）、实验验证（计算和延迟大幅下降，精度持平）且实用（损失函数提升远距离物体性能）的解决方案，对高分辨率实时应用场景具有显著参考价值。

</details>

<details>
<summary>Abstract</summary>

Stereo depth estimation for driving, robotics and augmented reality must run at high resolution under tight latency budgets, yet in transformer-based matchers the global self-attention that aggregates scene context grows quadratically with the number of pixels and comes to dominate runtime. We show that the joint self-attention stage of a stereo transformer, whose role is to spread context across both views, can be replaced by a data-independent Walsh-Hadamard token mixer that mixes tokens globally in the transform domain at log-linear cost, while the data-dependent cross-attention that performs left-right correspondence is retained. On synthetic driving data the mixer matches the attention baseline in end-point error while reducing model compute by a factor of 2.46 and single-image inference latency by a factor of 2.65. A complexity analysis shows the benefit is governed by the ratio of sequence length to channel width, which explains why high-resolution stereo matching is a particularly favorable setting and why classification transformers are not; we confirm this token-to-channel scaling on non-stereo long-sequence benchmarks. Furthermore, we introduce a hybrid log-disparity loss function designed to up-weight small-disparity pixels corresponding to long-range objects. This approach reduces the error on distant objects without incurring any additional computational overhead.

</details>

## Neural Scene Representations & Rendering

### 2026-07

#### 2026-07-30 - TSOG: A Format For Temporally And Spatially Ordered Gaussians

**Authors:** Shady Gmira, Evangelos Alexiou, Emmanouil Potetsianakis, Emmanuel Thomas
**Links:** [abs](https://arxiv.org/abs/2607.28049) - [pdf](https://arxiv.org/pdf/2607.28049)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TSOG: A Format For Temporally And Spatially Ordered Gaussians
- 作者：Shady Gmira, Evangelos Alexiou, Emmanouil Potetsianakis, Emmanuel Thomas
- 出版日期：2026-07-30T11:28:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.28049

### 一句话总结
提出了一种名为TSOG的4D高斯泼溅高效表示格式，通过时间域扩展的空间有序高斯框架，实现超过90%的文件体积缩减且质量损失极小。

### 研究问题
如何高效表示、存储和传输动态场景的4D高斯泼溅（4DGS）内容，以解决现有4DGS表示中文件体积过大的问题。

### 核心思路/方法
- 在空间有序高斯（SOG）框架基础上引入**时间线属性**，并对几何与外观属性进行**时间参数化**，从而将SOG扩展到时间域。
- 与SOG一致，TSOG是一种有损格式，为每个高斯分配唯一索引，并将属性值编码为与索引对齐的图像数据。
- 该格式是**模型无关**、**可扩展**的，兼容离散和连续两种4DGS表示。
- 评估采用PLYs序列作为基础基线、FreeTimeGS作为最先进的4DGS表示基线进行对比。

### 主要贡献
- 提出TSOG格式，首次将空间有序高斯框架系统性地扩展到时间域。
- 实现文件体积缩减超过90%，同时PSNR差异仅为-0.42至+0.85 dB，显示以极小质量代价换取显著存储节省。
- 格式设计具备模型无关性和扩展性，适用于不同4DGS表示类型，为下一代4D内容的表示、存储和传输提供了可行方案。

### 局限性
摘要未提供足够信息——关于计算开销、编码解码效率、对极端动态场景的鲁棒性、以及其他质量指标（如SSIM或LPIPS）方面的表现，摘要未提及。

### 阅读优先级
**高**
理由：该工作针对4DGS文件体积极大的痛点，提出了通用且兼容性强的压缩表示格式，节省超过90%的存储空间且质量损失小，对动态场景内容的高效存储和传输具有直接且重要的应用价值，适合关注神经渲染、3D/4D内容压缩的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

We propose Temporally and Spatially Ordered Gaussians (TSOG), a format for efficient representation of 4D Gaussian Splatting (4DGS) content. TSOG extends the Spatially Ordered Gaussians (SOG) framework to the temporal domain by introducing a timeline attribute and temporal parameterization of geometry and appearance attributes. Similar to SOG, TSOG is a lossy format that assigns each Gaussian a unique index and encodes attribute values as index-aligned image data. TSOG is model-agnostic, extensible, and compatible with both discrete and continuous 4DGS representations. Evaluation using a PLYs sequence and FreeTimeGS as baselines, serving as simplistic and state-of-the-art 4DGS representations respectively, shows file size reductions exceeding 90%, with PSNR differences ranging between -0.42 and +0.85 dB. These results demonstrate substantial file size savings with minimal quality degradation, enabling efficient representation, storage, and delivery of dynamic scenes for next-generation 4D content.

</details>

#### 2026-07-30 - Split and Drive: Dual-Axis Disentanglement for Real-Time Gaussian Head Avatars

**Authors:** MD Wahiduzzaman Khan, Mingshan Jia, Xiaolin Zhang, En Yu, Kaska Musial-Gabrys
**Links:** [abs](https://arxiv.org/abs/2607.28032) - [pdf](https://arxiv.org/pdf/2607.28032)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Split and Drive: Dual-Axis Disentanglement for Real-Time Gaussian Head Avatars
- 作者：MD Wahiduzzaman Khan, Mingshan Jia, Xiaolin Zhang, En Yu, Kaska Musial-Gabrys
- 出版日期：2026-07-30
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：https://arxiv.org/abs/2607.28032

### 一句话总结
提出一个基于双轴解耦的单图高斯头部虚拟形象框架 SpiD，通过内化逐帧驱动和分解面部特征分支，在包含完整驱动流程的情况下实现了最快推理速度。

### 研究问题
如何从单张图像生成照片级真实感、可动画化的头部虚拟形象，同时消除推理阶段对外部跟踪管线的依赖，并解决统一表示中不同几何面部区域相互纠缠导致的表达力与渲染保真度受限问题。

### 核心思路/方法
提出“双轴解耦”（Dual-Axis Disentanglement）设计：
1. **计算轴（Compute Axis）**：将逐帧驱动过程内化为模型自身计算的一部分，从而在推理时不再依赖外部跟踪管线。
2. **特征轴（Feature Axis）**：将头部虚拟形象分解为三个专用高斯分支，每个分支分别建模一个几何上不同的面部区域（具体区域划分摘要未详细说明）。

### 主要贡献
- 提出 SpiD 框架，首次在单图高斯头部虚拟形象中同时实现计算轴与特征轴的双重解耦。
- 消除推理阶段的外部跟踪依赖，使得实测推理速度包含完整驱动流程，更贴近真实应用场景。
- 在多个对比实验中，性能持续优于现有最先进方法，并且是所比较方法中推理速度最快的。

### 局限性
- 摘要未提供三个高斯分支具体对应的面部区域划分细节。
- 摘要未提及方法在极端表情、遮挡、非正面视角或不同光照条件下的表现。
- 摘要未提供定量实验数据（如具体 FPS、PSNR/SSIM 数值）或与其他方法的详细性能差距。
- 摘要未说明训练所需数据规模、计算资源要求及泛化能力测试情况。

### 阅读优先级
**中**
理由：该工作针对单图头部虚拟形象生成的实时性瓶颈，提出了具有实用价值的双轴解耦架构，且强调包含完整驱动管道的推理速度优势，对数字人合成与实时渲染领域有一定参考意义。然而，摘要中缺乏具体实验数据（如量化指标、可视化结果），且未提供实现细节与消融分析，难以直接评估其技术效果的显著程度，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Creating photorealistic animatable head avatars from a single image remains a fundamental challenge in digital human synthesis. While recent 3D Gaussian Splatting methods have achieved promising results, they rely on external tracking pipelines whose latency is excluded from inference measurements. Furthermore, they adopt unified representations that entangle geometrically distinct facial regions, limiting both expressiveness and rendering fidelity. We propose SpiD (Split and Drive), a single-image Gaussian head avatar framework built on two disentanglement axes. The compute axis internalizes per-frame driving, eliminating external tracking dependency at inference. The feature axis decomposes the avatar into three specialized Gaussian branches, each modeling a geometrically distinct facial domain. Extensive experiments demonstrate consistently strong performance against state-of-the-art methods while achieving the fastest inference speed among all compared methods on a single GPU with the complete driving pipeline included.

</details>

#### 2026-07-30 - 4DHumanDiff: Direct Text-to-4DGS Generation for Consistent 360-Degree Dynamic Humans

**Authors:** Renlong Wu, Haoran Chen, Yuxiang Wei, Xiaowei Jin, Wangmeng Zuo, Hui Li
**Links:** [abs](https://arxiv.org/abs/2607.27634) - [pdf](https://arxiv.org/pdf/2607.27634)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, scene reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4DHumanDiff: Direct Text-to-4DGS Generation for Consistent 360-Degree Dynamic Humans
- 作者：Renlong Wu, Haoran Chen, Yuxiang Wei, Xiaowei Jin, Wangmeng Zuo, Hui Li
- 出版日期：2026-07-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.27634 ；PDF: https://arxiv.org/pdf/2607.27634

### 一句话总结
本文提出4DHumanDiff，一个直接从文本提示端到端生成由4D高斯泼溅（4DGS）表示的动态人体模型的扩散框架，可在约一分钟内生成360度一致动态人体，推理时间较现有方法降低10倍以上。

### 研究问题
现有文本生成动态人体资产的方法通常先合成单目或多视角视频，再拟合4D表示，该流程成本高且容易出现几何不完整或视角不一致的渲染结果。本文旨在解决如何在文本提示下直接、高效、一致地生成完整360度动态人体资产的问题。

### 核心思路/方法
- 直接建模结构化的4D表示空间，端到端生成4DGS动态人体，避免视频预生成和逐场景重建。
- 采用3D U-Net骨干网络并引入时间注意力机制，实现运动感知的生成。
- 构建大规模text-to-4DGS数据集（60,000个高质量文本-4DGS对）。
- 引入2D正则化提升渲染质量，并提出免训练的4D插值方法增强运动平滑性。

### 主要贡献
- 提出首个直接从文本生成4DGS动态人体的扩散框架，免去视频中间步骤和逐场景重建。
- 构建60,000对的大规模text-to-4DGS训练数据集。
- 通过2D正则化和免训练4D插值，提升渲染质量与运动平滑度。
- 实验显示所提方法能在一分钟内生成一致的360度动态人体，获得更好的时间一致性和多视角一致性，并将推理时间降低10倍以上。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法直接针对文本到动态3D资产生成这一热点方向，绕开了传统多阶段流程，在效率（10倍以上提速）和一致性（360度、时间与多视角）上均有明显提升，并附带大规模数据集，对神经场景表示、内容生成和渲染领域的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Generating high-quality 360-degree dynamic human assets from text prompts is challenging. Existing methods usually synthesize monocular or multi-view videos first and then fit a 4D representation, which is expensive and often causes incomplete geometry or view-inconsistent renderings. We present 4DHumanDiff, a diffusion framework that directly generates dynamic humans represented by 4D Gaussian Splatting (4DGS) from text prompts. By modeling the structured 4D representation space end-to-end, 4DHumanDiff avoids video pre-generation and per-scene reconstruction, making it better suited for view-consistent and temporally coherent asset generation. The model uses a 3D U-Net backbone with temporal attention for motion-aware generation. We further construct a large-scale text-to-4DGS dataset with 60,000 high-quality pairs, and introduce 2D regularization and training-free 4D interpolation to improve rendering quality and motion smoothness. Experiments show that 4DHumanDiff generates consistent 360-degree dynamic humans within one minute, achieves better temporal and multi-view consistency, and reduces inference time by more than 10x.

</details>

#### 2026-07-29 - StructureGS: Structure-aware Gaussian Splatting for Articulated Object Reconstruction

**Authors:** Gahye Lee, Gyoonseo Kim, Wonjong Jang, Jooeun Son, Seungyong Lee
**Links:** [abs](https://arxiv.org/abs/2607.26889) - [pdf](https://arxiv.org/pdf/2607.26889)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StructureGS: Structure-aware Gaussian Splatting for Articulated Object Reconstruction
- 作者：Gahye Lee, Gyoonseo Kim, Wonjong Jang, Jooeun Son, Seungyong Lee
- 出版日期：2026-07-29
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：摘要页: https://arxiv.org/abs/2607.26889 ; PDF: https://arxiv.org/pdf/2607.26889

### 一句话总结
本文提出StructureGS，一种将结构感知约束（如空间一致性和结构连通性）集成到3D高斯溅射框架中的方法，用于重建具有清晰部件几何与边界的铰接物体。

### 研究问题
如何解决铰接物体（含多个可动部件）重建中由于几何、外观和运动参数相互纠缠，导致部件分解模糊、边界不清和几何伪影的问题。

### 核心思路/方法
- 基础框架：基于3D Gaussian Splatting进行铰接物体重建。
- 关键创新：引入结构化导向信息，具体利用物体部件的有向包围盒来施加两类结构约束：
  - 空间一致性：约束每个部件的几何在其指定区域内保持紧凑且空间连贯。
  - 结构连通性：强制相邻部件之间保持物理上合理的接触关系。
- 实现手段：通过结构感知损失函数，将显式结构约束注入优化过程。

### 主要贡献
1. 提出了StructureGS，一个集成了结构感知导向的铰接物体重建框架，有效改善了部件分解质量。
2. 设计了基于有向包围盒的空间一致性和结构连通性约束，为优化提供显式结构先验。
3. 实验表明，该方法在铰接物体重建任务上达到了最先进性能，生成了部件几何清晰的高质量结果。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**

理由：本文方法专注于铰接物体的3D重建这一具体问题，利用结构先验改进部件分解。对于从事神经渲染、物体重建或机器人操作等领域的读者，该方法结合了经典几何约束与现代场景表示，具有参考价值。但如果读者主要关注通用场景渲染或无铰接结构的静态重建，则相关性较低。摘要未提供消融实验或失败案例等细节，因此初步判断为中等优先级。

</details>

<details>
<summary>Abstract</summary>

Reconstructing articulated objects with multiple movable parts is essential for understanding object structure and enabling physical interaction. However, this reconstruction task poses significant challenges due to the entanglement of geometry, appearance, and motion parameters during optimization. Existing methods rely primarily on photometric supervision, which commonly fails to disentangle these interdependent components, resulting in poor part decomposition with blurred boundaries and geometric artifacts. To address this limitation, we introduce StructureGS, a reconstruction framework for articulated objects that integrates structure-aware guidance into 3D Gaussian Splatting. Our approach leverages oriented bounding boxes of object parts to enforce two key structural properties: spatial coherence, which constrains each part's geometry to remain compact and spatially coherent within its designated region, and structural connectivity, which enforces physically plausible contact relationships between adjacent parts. These properties are realized through structure-aware losses that inject explicit structural constraints into the optimization process. Extensive experiments demonstrate that our method achieves state-of-the-art performance in articulated object reconstruction, producing high-quality results with well-defined part geometries.

</details>

#### 2026-07-29 - 3DGBGS: 3D Granular Ball Gaussian Splatting for Compact Novel View Synthesis

**Authors:** Meng Yang, Shuyin Xia, Dawei Dai, YiWang
**Links:** [abs](https://arxiv.org/abs/2607.26578) - [pdf](https://arxiv.org/pdf/2607.26578)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** SfM, Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3DGBGS: 3D Granular Ball Gaussian Splatting for Compact Novel View Synthesis
- 作者：Meng Yang, Shuyin Xia, Dawei Dai, YiWang
- 出版日期：2026-07-29
- 分类：Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2607.26578，PDF: https://arxiv.org/pdf/2607.26578

### 一句话总结
3DGBGS 是一种基于颗粒球（Granular Ball）思想的紧凑型3D高斯溅射框架，通过自适应划分点云并初始化锚点，在减少模型存储的同时保持新视角合成质量。

### 研究问题
现有基于锚点的3D高斯溅射方法通常使用固定体素化从稀疏SfM点云构建锚点，无法充分适应空间非均匀点分布，导致锚点数量、模型紧凑性和渲染质量之间存在权衡。该研究旨在解决这一问题。

### 核心思路/方法
提出3DGBGS框架，核心步骤包括：
- **自适应颗粒球划分**：将SfM点云自适应划分为3D颗粒球，大球紧凑表示平滑冗余区域，小球保留复杂几何和局部细节。
- **颗粒球锚点初始化（GBAI）**：利用颗粒球中心初始化紧凑锚点位置。
- **颗粒球尺度先验（GBSP）**：利用颗粒球半径提供局部尺度先验，用于高斯生成。

### 主要贡献
基于摘要，主要贡献包括：
- 提出了结合颗粒球计算（GBC）与锚点型3DGS的紧凑框架。
- 通过GBAI和GBSP模块，实现自适应、紧凑的锚点初始化与尺度指导。
- 在四个基准数据集上，平均减少初始锚点37.1%、最终锚点10.0%，模型存储降低9.8%，同时保持可比的渲染质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。
理由：该方法针对3DGS模型紧凑性提出了新颖的颗粒球自适应策略，实验改进了锚点数量与存储效率，适合对3D场景渲染紧凑性有兴趣的读者。但未与更多最新方法对比或讨论实时性等关键细节，优先级中等。

</details>

<details>
<summary>Abstract</summary>

Three-dimensional Gaussian Splatting (3DGS) enables high-quality real-time novel-view synthesis through explicit Gaussian primitives and differentiable rasterization. 3DGS and Granular Ball Computing (GBC), proposed in 2019, share a natural compatibility in adaptive representation. The efficiency of 3DGS partly stems from a coarse-to-fine and on-demand refinement process that draws on the generation principle of GBC. This connection motivates us to further introduce adaptive granular ball organization into anchor-based 3DGS. Existing anchor-based methods typically construct anchors from sparse SfM point clouds through fixed voxelization, which cannot adequately adapt to spatially non-uniform point distributions and leads to a trade-off among anchor count, model compactness, and rendering quality. To address this issue, we propose 3DGBGS (3D Granular Ball Gaussian Splatting), a compact anchor-based framework for novel-view synthesis. 3DGBGS adaptively partitions SfM point clouds into 3D granular balls, using larger balls to compactly represent smooth and redundant regions and smaller balls to preserve complex geometry and local details. Based on this representation, Granular Ball Anchor Initialization (GBAI) uses granular ball centers to initialize compact anchor positions, while the Granular Ball Scale Prior (GBSP) exploits granular ball radii to provide local scale priors for Gaussian generation. Experiments on four benchmarks show that 3DGBGS reduces initial and final anchors by 37.1% and 10.0%, respectively, and model storage by 9.8% on average, while maintaining comparable rendering quality.

</details>

#### 2026-07-29 - AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting

**Authors:** ByungHyun Kim, Jinwoo Jeon, Woontack Woo
**Links:** [abs](https://arxiv.org/abs/2607.26525) - [pdf](https://arxiv.org/pdf/2607.26525)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting
- 作者：ByungHyun Kim, Jinwoo Jeon, Woontack Woo
- 出版日期：2026-07-29T06:43:17Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.26525

### 一句话总结
AtlasLC 是一种无需原始源数据、无需训练、直接对已发布的物体级3D高斯泼溅资产进行快速压缩的管线，通过局部竞争剪枝和确定性地图打包技术，在减少压缩时间的同时维持可比的几何与感知质量。

### 研究问题
现有3DGS压缩方法主要针对场景级捕获设计，依赖繁重的布局生成或激进的全域剪枝，不适用于语义集中的前景物体；在XR实际管线中，物体级资产需要反复打包、传输、解码和实例化，因此现有方法在资产准备成本、编解码兼容性、解码延迟以及深度和轮廓线索保留方面表现不佳。本文旨在解决如何针对物体级3DGS实现快速、编解码器就绪且部署友好的压缩。

### 核心思路/方法
AtlasLC 结合了局部竞争剪枝与确定性地图打包，直接操作已发布的3DGS资产（无需原始图像、相机位姿或逐资产优化）。具体地：
- **局部竞争剪枝**：在保持物体前景整体支撑的前提下，去除冗余高斯点。
- **单次排序条件传输**：作为轻量级、单遍的共享坐标骨干，连接剪枝与打包阶段，避免映射/重映射瓶颈。
- **确定性地图打包**：无需额外布局生成，直接打包高斯点，减少预处理时间。

### 主要贡献
1. 提出一种无需源数据、无需训练的直接压缩管线，适用于已发布的物体级3DGS资产。
2. 将地图准备时间降低最高25倍，端到端压缩时间降低最高5倍。
3. 在相似压缩尺寸下，比特数比紧凑结构化基线减少约6%~8%，同时保持可比的感知和几何质量。
4. 提供更优的部署感知平衡：兼顾有效载荷、解码延迟、运行时FPS和3D几何保真度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作直接针对XR实际部署中的物体级3DGS资产压缩瓶颈，提出了无需原始数据、无需训练的快速方案，且显著降低压缩时间和比特率。对于关注3DGS在XR/移动设备落地或编解码器优化的研究者与工程师，具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic novel-view synthesis with real-time rendering, but deploying compressed object-centric 3DGS in XR requires more than image-space rate-distortion. In practical XR asset pipelines, reusable objects are repeatedly packaged, transmitted, decoded, and instantiated, making asset-preparation cost, codec compatibility, decoding latency, and preservation of depth and silhouette cues first-class concerns. Existing 3DGS compression methods are largely developed for scene-scale captures and often rely on heavy layout generation or aggressive global pruning, assumptions that transfer poorly to semantically concentrated foreground objects. We present AtlasLC, a source-free, training-free compression pipeline for object-centric 3DGS that operates directly on released Gaussian assets, without original images, camera poses, or per-asset optimization. AtlasLC couples local-competition pruning with deterministic atlas packing to remove the mapping/remapping bottleneck while preserving object-wide foreground support; a lightweight single-pass sort-based conditional transport is used as a shared coordinate backbone for these stages. Across the evaluated assets, AtlasLC reduces atlas-preparation time by up to a factor of 25 and end-to-end compression time by up to a factor of 5, while offering a favorable deployment-aware balance of payload, decode latency, runtime FPS, and 3D geometry relative to the evaluated compressed baselines. Relative to similarly compact structured baselines, it uses about 6 to 8 percent fewer bits while maintaining comparable perceptual and geometric quality. These results show that object-centric 3DGS compression should be optimized for a deployment-aware operating point enabling scalable XR asset libraries.

</details>

#### 2026-07-28 - CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting

**Authors:** Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin
**Links:** [abs](https://arxiv.org/abs/2607.25569) - [pdf](https://arxiv.org/pdf/2607.25569)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting
- 作者：Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin
- 出版日期：2026-07-28
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2607.25569

### 一句话总结
CORF-GS提出一种基于耦合光学-射频3D高斯泼溅的实时无线辐射场重建框架，通过光学引导和联合优化实现高效在线信道建模。

### 研究问题
现有无线辐射场重建方法依赖预采集观测数据和离线优化，无法提供实时信道知识，如何实现基于序贯输入数据的实时无线信道重建。

### 核心思路/方法
1. 构建光学与射频的统一高斯表征：共享几何结构，分别学习模态特定的外观属性。
2. 光学引导高斯采样：在新关键帧到达时，利用高分辨率光学图像为重建不足区域补充高斯点。
3. 耦合光学-射频联合优化：针对光与无线电波对物体表面响应的波长失配问题，同时优化共享高斯，使其适应光学结构和射频功率分布，避免被动适应冻结的光学几何。

### 主要贡献
- 提出首个基于3DGS的实时无线辐射场重建框架CORF-GS。
- 设计光学引导采样与耦合优化策略，解决跨模态信源感知差异。
- 仿真结果表明CORF-GS在RF频谱合成质量上达到最先进水平，重建时间相比现有方法减少6.4倍。

### 局限性
摘要未提供足够信息：未报告方法在真实场景、动态环境或不同频段下的性能表现，亦未分析计算资源需求或模型可扩展性。

### 阅读优先级
**高**
理由：该工作首次将在线、实时特性引入无线辐射场重建领域，且提出耦合光学-射频联合优化方案解决跨模态感知差异问题，性能提升显著（重建时间降低6.4倍），对动态无线信道建模有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent advances in 3D Gaussian Splatting (3DGS)-based wireless radiance field (WRF) reconstruction provide an efficient solution for wireless channel modeling. However, existing WRF reconstruction methods rely on pre-collected observations and offline optimization, and thus struggle to provide real-time channel knowledge. To bridge this gap, we propose CORF-GS, a real-time WRF reconstruction framework that processes sequential optical and radio frequency (RF) keyframes. Specifically, CORF-GS constructs a unified Gaussian representation for optical and RF with shared geometry and modality-specific appearance, allowing high-resolution optical images to provide structural priors for WRF reconstruction. When a new keyframe arrives, CORF-GS first employs optical-guided Gaussian sampling to densify the WRF in under-represented regions. Since light and radio waves may respond differently to the same object surfaces due to wavelength mismatch, relying solely on optical guidance may neglect RF-informative areas. Therefore, CORF-GS performs coupled optical-RF optimization to jointly refine the shared Gaussians. Compared with the existing two-stage training pipelines, this prevents WRF from passively adapting to a frozen optical geometry and encourages the shared Gaussians to adapt to both optical structures and RF power distributions. Simulations show that CORF-GS achieves state-of-the-art RF spectrum synthesis quality and reduces the reconstruction time by $6.4\times$ compared with existing WRF methods.

</details>

#### 2026-07-28 - PanoLess: Environment Reconstruction from Partial Reflective Views

**Authors:** Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan
**Links:** [abs](https://arxiv.org/abs/2607.25362) - [pdf](https://arxiv.org/pdf/2607.25362)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, inverse rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PanoLess: Environment Reconstruction from Partial Reflective Views
- 作者：Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan
- 出版日期：2026-07-28
- 分类：Neural Scene Representations & Rendering
- 链接：摘要地址 https://arxiv.org/abs/2607.25362，PDF地址 https://arxiv.org/pdf/2607.25362

### 一句话总结
PanoLess 提出一种基于高斯溅射的框架，仅通过反射表面（如玻璃）的部分视角图像，就能重构出完整的环境照明图，并输出环境支持区域的可见性图。

### 研究问题
如何在仅从反射表面一侧获取的局部视角图像中，重建出具有几何一致性的周围环境照明图（远场 illumination map），以克服传统方法需要 360 度全覆盖数据的限制。

### 核心思路/方法
1. 使用表面对齐的 2D 高斯溅射与延迟着色技术，从部分反射视图中恢复精确的逐像素法线及反射线索。
2. 将这些线索融合到一个神经立方体贴图表示中，用以编码环境照明信息。
3. 额外生成一个可见性图，显式标记环境中的哪些区域得到了部分反射观测的支持。

### 主要贡献
- 提出可在仅利用反射表面一侧图像的情况下重建环境照明的新框架。
- 与需要全 360 度覆盖的现有逆渲染和反射感知高斯溅射方法不同，本方法能够在局部视图输入下实现一致、有物理依据的照明估计。
- 在自建合成基准和公开数据集上超越反射感知基线，并展示出对真实世界反射捕获数据的泛化能力。

### 局限性
摘要未提供足够信息，未提及该方法在特定复杂场景（如非朗伯反射表面、强遮挡或动态环境）下的表现或限制，也未讨论重建计算开销或对输入图像质量的要求。

### 阅读优先级
高。该工作针对部分反射视图这一实用场景提出新的解决方案，在技术路径（高斯溅射+神经立方体贴图）和任务设定上均有新意，且展示了较好的实验结果和泛化性，适合关注环境重建、反射感知渲染的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Reflections from shiny objects and glass facades naturally extend the field of view of a camera, capturing the surrounding environment without the need to pan the camera or acquire a full panorama. We propose PanoLess, a Gaussian-splat-based framework that reconstructs the surrounding environment as a distant illumination map from images captured on only one side of a reflective surface. PanoLess leverages surface-aligned 2D Gaussian splats with deferred shading to recover accurate per-pixel normals and reflection cues, which are fused into a neural cubemap representation of the environment. In addition, PanoLess produces a visibility map that explicitly denotes which regions of the environment are supported by the partial reflective observations. Unlike existing inverse-rendering and reflection-aware Gaussian-splatting approaches, which typically require full 360-degree coverage and struggle under incomplete views, PanoLess enables consistent, physically grounded illumination estimation from partial-view input. We show that PanoLess achieves high-fidelity and geometrically consistent environment reconstruction, outperforming reflection-aware baselines on a new custom synthetic benchmark and publicly available datasets, and demonstrating generalization to real-world reflective captures.

</details>

#### 2026-07-28 - SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation

**Authors:** Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang
**Links:** [abs](https://arxiv.org/abs/2607.25219) - [pdf](https://arxiv.org/pdf/2607.25219)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation
- 作者：Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang
- 出版日期：2026-07-28T02:51:24Z
- 分类：Neural Scene Representations & Rendering（主要），Embodied / Robotics / AR Applications（次要）
- 链接：摘要：https://arxiv.org/abs/2607.25219，PDF：https://arxiv.org/pdf/2607.25219

### 一句话总结
提出一个基于3D高斯泼溅（3DGS）的社交导航仿真平台SONG，结合大语言模型驱动行人轨迹和全身运动合成，并提供基准数据集SONG-Bench与多维评估指标，用于支持视觉感知的社交导航研究。

### 研究问题
现有社交导航仿真平台缺乏视觉观测、移动人物化身或真实感外观与行人行为，无法支持基于视觉的社交导航研究。本文旨在构建一个高保真、可真实模拟视觉感知环境的仿真平台。

### 核心思路/方法
- 采用3D高斯泼溅（3DGS）对场景和人物化身进行真实感表示。
- 使用大语言模型生成语义合理的行人移动轨迹。
- 通过轨迹驱动的全身运动生成器合成连续、自然的肢体运动。
- 构建SONG-Bench，按难度分层的评估任务序列。
- 提出涵盖有效性、安全性、社会合规性的多维评估指标集。

### 主要贡献
1. 提出SONG平台，首个利用3DGS实现场景和人物高保真表示的社交导航仿真平台。
2. 构建SONG-Bench，提供分层难度的评估任务与多维评价指标。
3. 系统评估表明：基于视觉的社交导航远未解决；安全性缺陷先于社交礼节问题；真实世界数据比模型规模更重要。
4. 验证了在平台生成数据上微调可有效提升真实环境下的成功率。

### 局限性
摘要未提供足够信息。例如未说明平台的可扩展性、计算开销、跨场景泛化能力或对人类行为多样性的覆盖程度。

### 阅读优先级
高  
理由：该平台直接针对视觉社交导航模拟的空白，采用3DGS+大语言模型的新技术组合，提供了系统评估与真实场景迁移验证，对从事仿真、机器人导航与具身智能的研究者有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Social navigation has progressed from simplified 2D environments toward a more general vision-based setting, in which a robot needs to achieve socially compliant behavior purely from onboard visual observations. Yet supporting simulation platforms have not kept pace: existing options either lack visual observations, lack moving human avatars, or fall short of real-world fidelity in appearance and pedestrian behavior, offering limited support for advancing vision-based social navigation. We introduce SONG, a SOcial Navigation platform powered by 3D Gaussian splatting (3DGS). It leverages 3DGS for both scene and avatar representations, drives pedestrians using semantically grounded trajectories generated by a large language model, and synthesizes their full-body motion with a trajectory-conditioned generator to produce continuous, natural movement. On top of the platform, we curate SONG-Bench, a set of evaluation episodes stratified by difficulty, and propose a multi-dimensional metric suite covering effectiveness, safety, and social compliance. A systematic evaluation of representative navigation baselines reveals three findings: (a) vision-based social navigation is far from solved; (b) a critical safety deficit precedes social etiquette; (c) real-world data matters more than model scale. Crucially, we demonstrate that fine-tuning on our curated data effectively improves the success rate in real-world environments. We hope our platform provides a faithful and rigorous testbed for the next generation of vision-based social navigation research.

</details>

## Embodied / Robotics / AR Applications

### 2026-07

#### 2026-07-30 - When Robots Exchange Meaning: A Demo of Goal-Oriented Semantic Communications for Collaborative Robotics

**Authors:** Peizheng Li, Xinyi Lin, Sajida Gufran, Adnan Aijaz
**Links:** [abs](https://arxiv.org/abs/2607.28256) - [pdf](https://arxiv.org/pdf/2607.28256)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D mapping, embodied AI, robotics, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：When Robots Exchange Meaning: A Demo of Goal-Oriented Semantic Communications for Collaborative Robotics
- 作者：Peizheng Li, Xinyi Lin, Sajida Gufran, Adnan Aijaz
- 出版日期：2026-07-30
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.28256

### 一句话总结
本文演示了一个面向协作机器人的机器人-边缘语义通信测试平台，通过VQ-VAE令牌传输实现RGB图像的42.67倍压缩，并重建为语义地图以支撑任务级机器人应用。

### 研究问题
在面向6G的任务导向型协作机器人场景中，通信质量应体现于任务执行与环境理解，而非仅以数据包传递来衡量；本文旨在构建一个从语义视觉传输到对象级地图交互的完整演示平台。

### 核心思路/方法
- 搭建机器人-边缘语义通信测试平台，包括机器人端视觉压缩、边缘端语义建图以及基于浏览器的任务交互界面。
- 机器人端配备RGB-D传感器与LiDAR，运行ROS 2；边缘节点使用Jetson Orin进行重建、RTAB-Map建图、语义对象处理及可视化。
- 具体实现：机器人端通过ONNX Runtime编码器将RGB帧编码为VQ-VAE令牌，边缘端使用PyTorch解码器重建图像。
- 320×240图像被表示为80×60令牌网格，打包负载为5400字节，相较模型输入RGB字节实现42.67倍压缩。
- 重建后的视觉流与深度、位姿和3D建图信息关联，生成语义地图供下游机器人应用使用。

### 主要贡献
- 构建了完整的机器人-边缘语义通信演示路径，覆盖从语义视觉传输到对象级地图交互。
- 提供了一个结合语义通信、具身AI与物理AI的实用测试平台，用于未来任务感知6G网络研究。
- 给出了初步的压缩效率验证（42.67倍缩减）以及实际演示视频链接。

### 局限性
摘要未提供足够信息，具体包括：未说明VQ-VAE训练数据集与训练细节，未报告重建图像质量指标（如PSNR/SSIM）或语义建图精度评估结果，也未讨论不同网络条件或任务场景下的系统性性能对比。

### 阅读优先级
**中**。理由：该文为演示论文，侧重于系统集成与概念验证，而非深度方法创新或完整实验评估。对于关注语义通信与机器人结合的研究者有一定参考价值，但如需深入了解性能与算法细节，摘要提供的信息有限，建议结合视频或其他扩展材料阅读。

</details>

<details>
<summary>Abstract</summary>

Collaborative robotics is a representative task-oriented 6G use-case, where communication quality should be reflected in mission execution, environment understanding, and closed-loop operation rather than packet delivery alone. This demo paper presents a robot-edge semantic communication (SemCom) testbed integrating robot-side visual compression, edge-side semantic mapping, and dashboard-based mission interaction. A mobile robot equipped with RGB-D sensing and LiDAR runs ROS 2, while a Jetson Orin edge node performs reconstruction, RTAB-Map mapping, semantic object handling, and browserbased visualization. As an initial proof of concept, RGB frames are encoded on the robot into VQ-VAE tokens using an ONNX Runtime encoder and reconstructed on the edge using a PyTorch decoder. A 320 X 240 image is represented by an 80 X 60 token grid with a packed payload of 5400 bytes, corresponding to a 42.67X reduction relative to model-input RGB bytes. The reconstructed visual stream is further associated with depth, pose, and 3D mapping information to generate a semantic map for downstream robotic applications. The demo exposes the full path from semantic visual transport to object-level map interaction, and provides a practical platform for future task-aware 6G networking studies at the intersection of SemCom, embodied AI, and physical AI-enabled robotics. A video of the demo is available at https://tinyurl.com/Tos09

</details>

#### 2026-07-30 - mmRadarTwin: A Measurement-Calibrated Signal-Level Digital Twin Platform for Indoor mmWave Radar

**Authors:** Jianyi Zhou, Chenghao Zhang, Yanli Li, Dong Yuan
**Links:** [abs](https://arxiv.org/abs/2607.28108) - [pdf](https://arxiv.org/pdf/2607.28108)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：mmRadarTwin: A Measurement-Calibrated Signal-Level Digital Twin Platform for Indoor mmWave Radar
- 作者：Jianyi Zhou, Chenghao Zhang, Yanli Li, Dong Yuan
- 出版日期：2026-07-30
- 分类：Embodied / Robotics / AR Applications（具身/机器人/AR应用）
- 链接：https://arxiv.org/abs/2607.28108

### 一句话总结
mmRadarTwin是一个面向室内毫米波雷达的、信号级且带路径归因的数字孪生平台，通过共享接收通道和距离-角度处理接口将真实雷达测量与虚幻引擎场景仿真连接，实现同域比较与诊断。

### 研究问题
室内毫米波雷达感知难以复现，因为测量的距离-角度响应受场景几何、材料响应、多径、硬件约定和信号处理等多种因素影响；现有光线追踪和数字孪生工具多暴露渲染、信道或路径级量，而雷达感知需要能在与真实FMCW测量相同域中处理和比较的复杂信号产品。

### 核心思路/方法
- 构建信号级、路径归因的数字孪生平台，包含两条分支：真实雷达测量分支 与 虚幻引擎场景仿真分支，二者通过共享的接收通道和距离-角度处理接口对接。
- 仿真器输出复数多通道接收网格，并导出每条路径的贡献记录，标识模拟返回的参与者（actor）、材料标签、传播事件和输出bin支持。
- 在办公室部署中使用商用单站毫米波雷达和移动场景采集硬件进行评估。

### 主要贡献
- 提出mmRadarTwin平台，实现信号级（非路径级或渲染级）的室内毫米波雷达数字孪生仿真。
- 建立测量与仿真共享的接收通道和距离-角度处理接口，支持同域比较。
- 提供每路径贡献记录，可识别参与者、材料、传播事件及输出位置，便于诊断仿真与实测差异。
- 在真实办公环境、154个测量位姿、22个雷达位置上进行评估，召回率70.8%，展示了实用的系统工作流。

### 局限性
摘要未提供足够信息，但根据摘要可明确：作者并不声称实现完整的雷达图重建或跨房间泛化；平台当前性能受限于弱/缺失路径支持、响应偏移、不支持锚点及缺失物理机制导致的残差。其他实验细节（如精度、运行时间、各类型残差的具体量化等）摘要未提供。

### 阅读优先级
**中**

理由：该工作提供了一个可工作的信号级室内毫米波雷达数字孪生平台，且已通过真实测量验证（70.8%召回率），对从事毫米波雷达仿真或室内感知的研究者有一定参考价值。但根据摘要，作者明确表示未实现完整重建或跨房间泛化，且未展示对下游任务的提升效果；若读者关注高精度重建或通用泛化，本工作的实用性可能有限。因此建议按需阅读，不必优先。

</details>

<details>
<summary>Abstract</summary>

Indoor mmWave radar perception is difficult to reproduce because measured range-angle responses depend on scene geometry, material response, multipath, hardware conventions, and signal processing. Existing ray-tracing and digital-twin tools often expose rendering, channel, or path-level quantities, while radar sensing requires complex signal products that can be processed and compared in the same domain as real FMCW measurements. We present mmRadarTwin, a signal-level and path-attributed digital-twin platform for indoor mmWave radar. mmRadarTwin links a real radar measurement branch with an Unreal Engine scene-simulation branch through a shared receive-channel and range-angle processing interface. The simulator writes complex multi-channel receive grids and exports per-path contribution records that identify the actor, material tag, propagation event, and output-bin support of each simulated return. We evaluate mmRadarTwin in an office deployment using a commodity monostatic mmWave radar and mobile scene-capture hardware. Across 154 measured poses spanning 22 radar locations, the current physics-only path-basis simulator recalls 70.8% of measurement-active geometry-supported response regions in the central usable field of view while exposing residuals caused by weak or missing path support, shifted responses, unsupported anchors, and missing physical mechanisms. Rather than claiming complete radar-map reconstruction or cross-room generalization, mmRadarTwin establishes a practical systems workflow for constructing, comparing, and diagnosing indoor radar digital twins.

</details>

#### 2026-07-30 - ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow

**Authors:** Dongxiu Liu, Haoyi Niu, Peng Cheng, Yuan Gao, Xirui Kang, Sangli Teng, Koushil Sreenath, Xianyuan Zhan
**Links:** [abs](https://arxiv.org/abs/2607.27924) - [pdf](https://arxiv.org/pdf/2607.27924)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow
- 作者：Dongxiu Liu, Haoyi Niu, Peng Cheng, Yuan Gao, Xirui Kang, Sangli Teng, Koushil Sreenath, Xianyuan Zhan
- 出版日期：2026-07-30T09:37:30Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.27924

### 一句话总结
ODEWorld 是一种基于物理时间连续流的潜空间世界模型，通过 ODE 参数化连续动力学，支持任意时间分辨率预测、反向预测并缓解表征坍缩问题。

### 研究问题
现有世界建模方法主要局限于离散时间预测，难以高效捕捉物理世界中空间与时间的连续动态特性。作者试图构建一个连续时间潜变量世界模型，以更自然地建模物理世界动态。

### 核心思路/方法
- 提出 Physical-Time Flow（PT-Flow）：在结构化表示空间中学习一个连续的潜速度场，并用常微分方程（ODE）参数化时序数据的底层动态。
- 未来预测被重构为在压缩潜空间中对 ODE 进行时间积分。
- 基于 PT-Flow 构建 ODEWorld，提取时变特征，并在动力学表示空间和潜速度场上施加 ODE 约束，以解决潜世界模型中的表征坍缩问题。
- 由于模型本质连续，支持任意时间分辨率预测和反向预测。

### 主要贡献
- 提出 PT-Flow 连续潜动力学学习方法，并用 ODE 参数化物理时间动态。
- 构建 ODEWorld 连续时间潜世界模型，兼具效率与通用性，并解决潜世界模型长期存在的表征坍缩问题。
- 在长时程预测后仍能实现高质量图像重建。
- 支持任意时间分辨率预测与反向预测，突破了离散时间模型的能力边界。
- 可提供丰富的规划导向信息，促进下游策略学习。
- 实验表明 ODEWorld 在视频生成和机器人控制任务中均表现出色，兼顾规划导向的动力学抽象与视觉真实感。

### 局限性
摘要未提供足够信息。摘要中未明确讨论该方法的潜在局限性，例如计算开销、ODE 求解器的数值稳定性、对高维复杂场景的扩展性、训练数据需求等均未提及。

### 阅读优先级
**高**
理由：该工作提出了一个新颖的连续时间潜世界模型范式，直接挑战主流离散时间世界模型，且研究目标跨足视频生成与机器人控制，在具身智能和连续动力学建模方向具有较高的学术价值与潜在应用前景。摘要中实验覆盖两类任务且宣称性能优越，值得关注。

</details>

<details>
<summary>Abstract</summary>

In the physical world we inhabit, space and time are fundamentally continuous. However, existing machine learning paradigms for world modeling are largely confined to discrete-time prediction, thereby exhibiting significant inefficiency in capturing the dynamics of physical world. We introduce Physical-Time Flow (\textbf{PT-Flow}), a novel approach that learns a continuous latent velocity field operating in physical time. Crucially, the underlying dynamics of sequential data are parameterized by an ordinary differential equation (ODE) embedded in a well-structured representation space. Under this paradigm, the prediction of future can be recast as temporal integration via an ODE solver in the compressed latent space. Building upon PT-Flow, we construct \textbf{ODEWorld}, a continuous-time latent world model that is both efficient and versatile. By extracting time-variant features and enforcing ODE properties on both the dynamical representation space and the latent velocity field, ODEWorld effectively addresses the long-standing representation collapse issue in latent world model literature. This also enables high-quality image reconstruction even after long-horizon prediction. Moreover, its continuous nature allows for arbitrary temporal resolution and even backward prediction, which is impossible for most discrete-time models. Lastly, ODEWorld can provide rich planning-oriented information to facilitate downstream policy learning. Comprehensive experiments demonstrate that ODEWorld successfully reconciles planning-conducive dynamics abstraction with visual realism, excelling in both video generation and robotic control. \href{https://dstate.github.io/odeworld_website/}{Project Website}.

</details>

#### 2026-07-30 - Write-Safe Flow Field Mapping under Ambiguous Onboard Sensing and Localization Drift

**Authors:** Linhao Jin, Qimin Feng, Peter Gunnarson, Qiang Zhong
**Links:** [abs](https://arxiv.org/abs/2607.27713) - [pdf](https://arxiv.org/pdf/2607.27713)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Write-Safe Flow Field Mapping under Ambiguous Onboard Sensing and Localization Drift
- 作者：Linhao Jin, Qimin Feng, Peter Gunnarson, Qiang Zhong
- 出版日期：2026-07-30
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.27713

### 一句话总结
本文提出一种地图参考感知的保守融合框架，通过预测“写安全分数”来抑制移动机器人流场建图中因观测模糊和定位漂移导致的鬼影结构污染。

### 研究问题
移动机器人在依赖机载感知推断局部流场结构时，局部估计虽然局部看似合理，但直接写入全局地图可能不安全——相似的流场结构会产生模糊观测，而定位漂移会导致预测块被写入错误位置，重复的错误配准更新会积累成持久的鬼影结构。论文针对这一失效模式，研究如何在模糊感知和定位漂移下安全地进行流场地图写入。

### 核心思路/方法
提出一种地图参考感知的保守融合框架：
- 模型预测局部速度块（velocity patch）以及一个学习得到的写安全分数（write-safety score）。
- 该分数会持续衰减不确定的地图更新，同时在没有可靠地图参考时允许初始化。
- 通过这种门控机制，避免将不可靠的局部估计写入全局地图，从而减少鬼影污染。

### 主要贡献
- 提出地图参考感知的保守融合框架，引入学习式写安全分数。
- 在合成射流和横流环境中，该方法相比无门控融合将平均鬼影污染减少42%。
- 在真实推力器尾流数据上的零样本硬件回放中，鬼影污染减少39%，同时保留81%的地图覆盖率。
- 实验结果表明，在模糊感知和定位漂移条件下，安全地图写入对流场建图至关重要。

### 局限性
摘要未提供足够信息，未提及方法在复杂真实环境下的泛化能力、计算开销、对安全分数阈值的敏感性，或与现有方法的定量对比细节。

### 阅读优先级
**中**。理由：该工作针对移动机器人流场建图中的实际失效模式（感知模糊与定位漂移导致的鬼影污染），提出了有明确创新点的保守融合框架，且实验验证了有效性。但其主要面向流场建图这一特定下游任务，若读者关注机器人建图安全性或流场感知，则有较高参考价值；否则可作为一般性感知-建图融合问题的参考。

</details>

<details>
<summary>Abstract</summary>

Mobile robots can infer local flow structure from onboard sensing, but a locally plausible estimate is not always safe to write into a global map. Similar flow structures may produce ambiguous observations, while localization drift causes predicted patches to be written at incorrect locations. Repeated misregistered updates then accumulate into persistent ghost structures. We address this failure mode with a map-reference-aware conservative fusion framework. The model predicts a local velocity patch and a learned write-safety score that continuously attenuates uncertain map updates while permitting initialization when no reliable map reference is available. Across synthetic jet and crossflow environments, the proposed method reduces average ghost contamination by 42% relative to ungated fusion. A zero-shot hardware replay using real pressure and optical-flow measurements from a thruster wake further reduces ghost contamination by 39% while retaining 81% map coverage. These results show that safe map writing is critical for flow mapping under ambiguous sensing and localization drift.

</details>

#### 2026-07-29 - Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation

**Authors:** Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, Maoqing Yao
**Links:** [abs](https://arxiv.org/abs/2607.26646) - [pdf](https://arxiv.org/pdf/2607.26646)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation  
- 作者：Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, Maoqing Yao  
- 出版日期：2026-07-29  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2607.26646  

### 一句话总结  
该论文提出一个两阶段的前馈流水线，仅从单张360°全景图生成高质量、可自由探索的室内3D场景，无需逐场景优化或多视角输入，支持零样本泛化。

### 研究问题  
如何从单张360°全景图重建高质量、可自由导航的3D场景，同时解决现有方法缺乏度量轨迹控制、在大范围相机运动下处理大面积遮挡困难以及需要高端多GPU服务器的问题。

### 核心思路/方法  
- **第一阶段：全景视频生成**  
  - 使用NavMesh规划的SE(3)漫游轨迹，通过密集几何扭曲条件注入潜在视频扩散模型。  
  - 采用长-短轨迹混合训练和基于快捷模型的自一致性目标，在无无分类器引导的四步去噪中生成高保真全景视频。  
- **第二阶段：3D重建**  
  - 利用前馈式全景重建器将生成的视频提升为高保真3D高斯场景，支持实时自由视角漫游，可直接作为具身AI模拟资产。

### 主要贡献  
1. 提出一种两阶段流水线，将生成与重建通过显式、轨迹可控的全景视频桥接。  
2. 引入NavMesh规划轨迹注入、长短轨迹混合训练和基于快捷模型的自一致性目标，实现高效高质量视频生成。  
3. 在生成全景视频和下游3D重建任务上均优于几何条件基线，且零样本泛化到未见室内场景。

### 局限性  
摘要未提供足够信息。

### 阅读优先级  
**高**  
理由：该工作解决了具身AI中的关键问题（从单全景图到可导航3D场景的生成），方法创新性强（两阶段桥接生成与重建、快捷模型加速推理），实验证明性能优越且具备零样本泛化能力，对室内3D场景理解和模拟领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We address the problem of reconstructing a high-fidelity, freely navigable 3D scene from a single $360^\circ$ panorama, without per-scene optimization or multi-view capture. Existing methods either lack metric trajectory control, which hinders reliable downstream 3D reconstruction, or struggle with large disocclusions under long-range camera motion while requiring high-end multi-GPU servers.We present Genie Sim PanoWorld, a two-stage feed-forward pipeline that bridges generation and reconstruction via an explicit, trajectory-controllable panoramic video. A NavMesh-planned $\mathrm{SE}(3)$ roaming trajectory is injected into a latent video diffusion model through dense geometry-warped conditioning; long--short trajectory mixed training and a self-consistency objective based on shortcut models together yield high-fidelity video in four CFG-free denoising steps. A feed-forward panoramic reconstructor then lifts the generated video into a high-fidelity 3D Gaussian scene that supports real-time, free-viewpoint roaming and can be directly used as a simulation-ready asset for embodied AI applications. Experiments show that Genie Sim PanoWorld outperforms geometry-conditioned baselines in both panoramic video generation and downstream 3D reconstruction, while generalizing zero-shot to unseen indoor scenes.

</details>

#### 2026-07-28 - Spline-Based Boundary Representations for Sparse View Reconstruction and Simulation Using Isogeometric Analysis

**Authors:** Davor Dobrota, Vsevolod Skorokhodov, Chenghao Xu, Olga Fink, Malcolm Mielle
**Links:** [abs](https://arxiv.org/abs/2607.26234) - [pdf](https://arxiv.org/pdf/2607.26234)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spline-Based Boundary Representations for Sparse View Reconstruction and Simulation Using Isogeometric Analysis
- 作者：Davor Dobrota, Vsevolod Skorokhodov, Chenghao Xu, Olga Fink, Malcolm Mielle
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26234

### 一句话总结
本文提出FORGE-SIM方法，通过优化B样条边界表示，直接从稀疏RGB图像重建紧凑、光滑、水密的几何模型，并同步支持计算机辅助设计和数值仿真。

### 研究问题
如何从稀疏视角的RGB图像直接重建出既适合可视化、又满足数值仿真（如热仿真、模态分析）要求的显式、水密、光滑的几何模型，以消除计算机视觉与数值分析之间的表示鸿沟。

### 核心思路/方法
1. **直接优化样条表示**：不依赖传统网格或隐式表面，而是将多片B样条边界表示作为可优化参数，从稀疏图像中直接回归出几何。
2. **仿真兼容性设计**：重建的几何自动满足水密性和光滑性，原生兼容计算机辅助设计和等几何分析流程。
3. **场投影策略**：将观测得到的场（如热状态、语义信息）以相同样条基函数投影到重建模型上，使模型可直接用于仿真。

### 主要贡献
- 提出了FORGE-SIM，一种无需人工干预、从稀疏RGB图像直接重建多片B样条边界表示的方法。
- 重建的几何紧凑、光滑、水密，同时兼容设计软件与仿真工作流。
- 实现了将观测场（热、语义等）映射到同一样条基上，支持即时仿真应用。
- 模型质量足以支撑热仿真与模态分析，统一了图像重建与仿真建模的优化框架。

### 局限性
摘要未提供足够信息，无法得知具体性能指标、对比方法、失败案例或计算开销等局限性。

### 阅读优先级
**高**  
理由：该方法解决了计算机视觉与数值仿真之间的长期表示不兼容问题，对于数字孪生、仿真驱动设计等跨领域应用有重要启发意义。摘要提供的技术路径清晰、创新点明确，且实验（热仿真、模态分析）初步验证了可行性。建议优先阅读以评估方法细节。

</details>

<details>
<summary>Abstract</summary>

Image-based reconstruction aims to recover three-dimensional geometry from images. Recent advances have enabled the recovery of visually detailed models, yet their representations are not well-suited for numerical simulation. Simulation frameworks typically require explicit, watertight, and smooth geometries to ensure numerical robustness and accuracy, properties that surfaces extracted from image-based reconstructions lack. We propose FORGE-SIM, a method to directly reconstruct a multi-patch B-spline boundary representation from sparse posed RGB images without manual intervention. By optimizing the spline representation itself, our approach produces compact, smooth, and watertight geometries that are natively compatible with both Computer Aided Design and simulation workflows. Additionally, we introduce a strategy to project observation-derived fields, such as a thermal state and semantic information, onto the reconstructed models in the same spline basis, enabling immediate use in simulation. We demonstrate that the obtained models are of sufficiently high quality to enable thermal simulation and modal analysis. By unifying image-based reconstruction and simulation-ready modeling within a single optimization framework, this work removes a long-standing barrier between computer vision and numerical analysis. We anticipate that it will enable new workflows for simulation-driven design, inspection, and digital twin applications.

</details>

#### 2026-07-28 - BG-REAL: A Public Real-Data Anchored Benchmark for Background Manipulation Detection and Localization

**Authors:** Bugra Alperen Uluirmak, Rifat Kurban
**Links:** [abs](https://arxiv.org/abs/2607.26232) - [pdf](https://arxiv.org/pdf/2607.26232)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BG-REAL: A Public Real-Data Anchored Benchmark for Background Manipulation Detection and Localization
- 作者：Bugra Alperen Uluirmak, Rifat Kurban
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2607.26232，PDF: https://arxiv.org/pdf/2607.26232

### 一句话总结
本文提出BG-REAL，一个专注于背景操作检测与定位的公开真实数据锚定基准测试包，包含7000个处理样本、六种编辑类型，并揭示了现有基线模型因重编码伪影而产生的高误报率问题。

### 研究问题
背景操作是一种实用但定义不够清晰的图像取证场景：操纵证据可能位于显著性前景物体之外，而许多现有评估强调以物体为中心的复制-移动、拼接或通用合成编辑。因此，需要针对背景操作检测与定位的专用基准。

### 核心思路/方法
构建基于Open Images V7实例分割源的真实数据锚定基准测试包BG-REAL。包含7000个样本（6000个公共数据锚定样本+1000个合成对照样本），覆盖六种编辑家族、匹配的真实对照、源组划分、掩码与泄露质量保证、599条人工辅助质量控制行。采用匹配真实对照诊断方法，评估三种完整外部基线（TruFor、MVSS-Net、HiFi-Net）在固定阈值下的误报率。

### 主要贡献
1. 提出了首个公开的、基于真实数据锚定的背景操作检测与定位基准BG-REAL。
2. 提供了完整的构建流程、评估协议、可直接使用的图表和复现文档。
3. 通过匹配真实对照诊断，发现基线模型存在重编码伪影导致的共同捷径风险（误报率0.57至1.00），而非某一特定模型的问题。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。
理由：该工作专注于图像取证中一个特定且实用的子问题——背景操作，并提供了真实的基准数据集和诊断结果，对从事图像篡改检测、特别是背景相关研究的学者有直接参考价值。但论文尚未提出新的检测算法，且摘要未展示在背景操作场景下的具体性能提升，因此优先级适中。

</details>

<details>
<summary>Abstract</summary>

Background manipulation is a practical but under-specified image-forensics setting: the manipulated evidence can sit outside the salient foreground object, while many evaluations emphasize object-centric copy-move, splicing, or generic synthetic edits. We introduce BG-REAL, a public real-data anchored benchmark package for background manipulation detection and localization. The current release is built from Open Images V7 instance-segmentation sources and contains 7,000 processed samples over 1,200 source groups, including 6,000 public-data anchored samples and 1,000 synthetic control samples. BG-REAL covers six edit families, matched authentic controls, source-group splits, mask and leakage QA, 599 human-assisted quality-control rows, three completed external baselines (TruFor, MVSS-Net, and HiFi-Net), and five-seed model evaluation. Beyond aggregate accuracy, we use matched-authentic-control diagnostics to measure how often baselines misclassify re-encoded authentic images as manipulated at a threshold fixed on held-out validation data; false-positive rates range from 0.57 (TruFor, the lowest) to 1.00 (several weak or mask-informed baselines), indicating that re-encoding artifacts are a shared shortcut risk across baselines rather than a problem specific to any one model. The release provides the construction pipeline, evaluation protocol, paper-ready figures, and reproduction documentation. We frame BG-REAL as a background-manipulation-focused complement to general image-manipulation-localization benchmarks, not as a fully real-only or general-purpose benchmark.

</details>

#### 2026-07-28 - DVPSFormer: Efficient Online Depth-aware Video Panoptic Segmentation for Autonomous Driving

**Authors:** Yung-Hsu Yang, Luigi Piccinelli, Siyuan Li, Mattia Segu, Lei Ke, Martin Danelljan, Yuqian Fu, Zuria Bauer, Fisher Yu, Hermann Blum, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2607.26165) - [pdf](https://arxiv.org/pdf/2607.26165)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, rendering, autonomous driving, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DVPSFormer: Efficient Online Depth-aware Video Panoptic Segmentation for Autonomous Driving
- 作者：Yung-Hsu Yang, Luigi Piccinelli, Siyuan Li, Mattia Segu, Lei Ke, Martin Danelljan, Yuqian Fu, Zuria Bauer, Fisher Yu, Hermann Blum, Marc Pollefeys
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2607.26165；PDF：https://arxiv.org/pdf/2607.26165

### 一句话总结
提出一种面向自动驾驶的高效在线深度感知视频全景分割架构DVPSFormer，通过显式场景离散化和在线多数投票机制，在降低延迟的同时在Cityscapes-DVPS和SemKITTI-DVPS基准上达到新SOTA。

### 研究问题
现有深度感知视频全景分割（DVPS）方法依赖多阶段流水线或离线跟踪，计算成本高且不适合实时决策，无法满足自动驾驶对在线、高效4D场景理解的需求。

### 核心思路/方法
1. **显式场景离散化（ESD）**：利用分割查询（segmentation queries）表示前景和背景区域，配合离散到连续（D2C）深度头在单次前向中解码度量深度，紧密耦合语义与几何学习，减少延迟。
2. **在线多数投票机制（OMV）**：利用时间一致性在实例跟踪过程中对分类结果进行修正，提升稳定性。
3. 整体架构为统一在线设计，无需多阶段或离线步骤。

### 主要贡献
- 提出DVPSFormer，首个高效在线的统一架构用于深度感知视频全景分割。
- 设计ESD机制，实现语义与深度学习的紧耦合，显著降低延迟。
- 提出OMV机制，利用时间一致性提升跟踪中的分类效果。
- 在Cityscapes-DVPS和SemKITTI-DVPS基准上取得新SOTA结果。

### 局限性
摘要未提供足够信息，未提及计算资源要求、在极端驾驶场景下的表现、或对标注数据的依赖等具体局限性。

### 阅读优先级
**高**。理由：该论文针对自动驾驶中实时4D场景理解的迫切需求，提出了兼具效率和性能的在线解决方案，并在多个基准上刷新SOTA，方法新颖（ESD和OMV），且提供开源代码和模型，对从事环境感知、机器人导航的从业者和研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Safe autonomous navigation requires a holistic understanding of dynamic environments, necessitating the simultaneous estimation of metric depth, semantic segmentation, and instance trajectories. While depth-aware video panoptic segmentation (DVPS) unifies these tasks, existing approaches often rely on computationally expensive, multi-stage pipelines or offline tracking, rendering them unsuitable for real-time decision-making. To address this, we propose DVPSFormer, a unified online architecture designed for efficient 4D scene understanding. Central to our approach is explicit scene discretization (ESD), a novel mechanism that leverages segmentation queries to represent foreground and background regions, enabling a discrete-to-continuous (D2C) depth head to decode metric depth in a single pass. This tightly couples semantic and geometric learning while significantly reducing latency. Furthermore, we propose an online majority voting (OMV) mechanism that exploits temporal consistency to refine classification during instance tracking. DVPSFormer establishes a new state-of-the-art on the Cityscapes-DVPS and SemKITTI-DVPS benchmarks, offering a streamlined solution for online robotic perception. Code and models are available at https://royyang0714.github.io/DVPSFormer.

</details>

#### 2026-07-28 - S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information

**Authors:** Kaneyoshi Hiratsuka, Benjamin Yen, Ryosuke Kojima
**Links:** [abs](https://arxiv.org/abs/2607.26047) - [pdf](https://arxiv.org/pdf/2607.26047)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information
- 作者：Kaneyoshi Hiratsuka, Benjamin Yen, Ryosuke Kojima
- 出版日期：2026-07-28T17:56:07Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26047

### 一句话总结
本文提出一个将听觉空间信息与视觉特征融合的多模态模仿学习框架S2A2，用于机器人操作任务中的声源定位与识别，并通过仿真和真实机器人实验验证其有效性。

### 研究问题
如何在机器人模仿学习操作任务中，有效利用物体位置、材质及接触/运动引起的声学信息，实现主动声源定位与识别，并完成声学感知驱动的操作目标。

### 核心思路/方法
1. 设计一系列新的“声学感知操作任务”，要求机器人依赖听觉线索（如声音位置、音色）来确定操作目标。
2. 提出多模态模仿学习框架S2A2（Spatial-Spectral Audio Action），该框架将视觉特征与声学空间信息（空间+谱）整合，用于声学感知操作任务。
3. 将ACT、Diffusion Policy、VQ-BeT和π₀等策略集成到S2A2框架中，并通过仿真实验和真实机器人实验进行评估。

### 主要贡献
- 引入了一组新的声学感知操作任务，用于模仿学习，强调机器人通过听觉线索进行主动探索。
- 提出了S2A2框架，该框架能够将视觉特征与声学空间-谱信息进行多模态融合。
- 仿真实验表明，所提方法在同时需要位置和音色信息的任务中效果最佳。
- 真实机器人实验验证了所提任务和框架在真实世界操作中的可行性。

### 局限性
摘要未提供足够信息，无法明确列出本文实验的量化局限性（如失败案例、计算资源需求或任务泛化能力等）。

### 阅读优先级
**中**  
理由：该工作创新性地将听觉空间信息引入机器人操作中的模仿学习，解决了传统方法忽视声音线索的问题，对于多模态机器人学习领域有参考价值。但由于未详细说明方法具体结构、基线对比差异或实验量化结果，目前仅适用于概念验证和领域入门阅读，尚需后续完整论文评估细节。

</details>

<details>
<summary>Abstract</summary>

Acoustic information provides rich cues about object location, material properties, and changes caused by contact or motion. This paper introduces a new set of acoustic-aware manipulation tasks for imitation learning, in which robots must use auditory cues to determine manipulation targets. These tasks require sound source localization and identification for active exploration in robotic manipulation. Also, we propose a multimodal imitation learning framework, Spatial-Spectral Audio Action (S2A2), that integrates visual features with acoustic spatial and acoustic signal information for the acoustic-aware manipulation tasks. We implemented S2A2 models that integrates policies such as ACT, Diffusion Policy, VQ-BeT, and $π_0$, into our framework. Simulation experiments showed that the proposed method is the most effective for tasks requiring both position and timbre. Furthermore, real-robot experiments confirm the applicability of the proposed tasks and framework to real-world manipulation.

</details>

#### 2026-07-28 - Wonder: Video World Model Done Better

**Authors:** Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei
**Links:** [abs](https://arxiv.org/abs/2607.26037) - [pdf](https://arxiv.org/pdf/2607.26037)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Wonder: Video World Model Done Better
- 作者：Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei
- 出版日期：2026-07-28T17:45:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.26037

### 一句话总结
本文提出一个名为Wonder的通用的视频世界模型，支持实时、可控制摄像头的交互式世界探索，用户可通过移动摄像头在长时程中导航并发现新区域。

### 研究问题
如何构建一个通用的视频世界模型，使其能够实时响应摄像头控制指令，在保持长期连贯性的同时支持用户交互式探索（如移动摄像头、发现和重访区域）。

### 核心思路/方法
1. **摄像头控制**：引入密集坐标场的摄像头条件化方法，通过渲染提供空间对齐的运动和方向线索，使模型直接将摄像头运动视为视觉证据。
2. **记忆机制**：提出高效的基于稀疏注意力的记忆机制，在推理时选择性地关注少量相关上下文标记，不受实际上下文长度限制，实现快速精确的记忆检索。
3. **训练策略**：开发了多种技术来纠正自强制样式的蒸馏流程，提升学生模型对控制信号的遵从性，同时保持教师模型的多样化生成模式和长期记忆能力。

### 主要贡献
- 提出了一个支持实时、长时程、摄像头可控交互的视频世界模型Wonder。
- 设计了基于密集坐标场的摄像头条件化方法和稀疏注意力记忆机制。
- 改进了蒸馏训练流程，平衡了控制信号响应、生成多样性及长期记忆保持。
- 模型能以16 FPS合成多样化的分钟级视频，在长卷中保持连贯的几何、外观和动态。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法涉及视频生成、世界模型、交互控制与长期记忆等前沿交叉领域，且声称实现了实时长时程的可控探索，对机器人仿真、AR/VR及具身智能应用具有潜在重要影响。

</details>

<details>
<summary>Abstract</summary>

We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy. We introduce a novel camera conditioning with a dense coordinate field whose renderings provide spatially aligned motion and orientation cues, allowing the model to interpret camera motion directly as visual evidence. To support fast and precise memory retrieval over a growing generation context, we propose an efficient sparse attention-based memory mechanism, enabling the model to selectively attend to a small set of relevant context tokens at inference time, regardless of actual context length. We further develop several techniques to rectify the self-forcing-style distillation pipeline, improving the student model's ability to respect control signals, as well as maintaining diverse generation modes and long-term memory from the teacher. Together, these components enable Wonder to synthesize diverse, minute-scale videos at 16 FPS while preserving coherent geometry, appearance, and dynamics across long rollouts. Beyond image-to-video generation, Wonder naturally supports video-conditioned generation, allowing existing dynamic scenes to be re-shot in real time.

</details>

#### 2026-07-28 - HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone

**Authors:** Simple AI, :, Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, Yushen Zuo, Ke Rui, Minglei Li, Jinhao Zhang, Zhikang Pan, Xiang Wang, Haoran Jia, Huan Du, Zicheng Zeng, Jun Ma, Guiyu Qin, Di Zhang, Xiaofei Li
**Links:** [abs](https://arxiv.org/abs/2607.25895) - [pdf](https://arxiv.org/pdf/2607.25895)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone
- 作者：Simple AI, :, Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, Yushen Zuo, Ke Rui, Minglei Li, Jinhao Zhang, Zhikang Pan, Xiang Wang, Haoran Jia, Huan Du, Zicheng Zeng, Jun Ma, Guiyu Qin, Di Zhang, Xiaofei Li
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：arxiv.org/abs/2607.25895

### 一句话总结
本文提出HiFi-UMI数据生产系统，通过提升无机器人UMI数据的采集保真度，使得仅用该数据微调的策略能直接部署到真实机器人上，无需任何后训练阶段的真实机器人数据。

### 研究问题
机器人操作策略学习受限于同时具备高保真度和可扩展性的数据匮乏问题：真实遥操作数据精准但成本高、难以规模化；无机器人UMI数据容易采集但保真度低，通常只能用于预训练，仍需少量真实机器人数据作为后训练的“锚点”。本文核心问题是：能否仅通过提高无机器人UMI数据的保真度，完全去除后训练中的真实机器人数据环节。

### 核心思路/方法
本文从四个维度协同设计了一套便携式UMI数据生产系统（HiFi-UMI）以提升数据保真度：
1. **轨迹精度**：采用头戴式离线立体惯性SLAM。
2. **夹爪间相对姿态**：使用原生而非重建的相对姿态估计。
3. **同步性**：利用共享微秒级GPIO触发信号。
4. **视野**：每只手配备两个广角相机，覆盖约200度视野。
该系统在无外部定位基础设施下，可实现3毫米工作空间局部末端执行器精度。基于此系统采集的高保真数据，策略后训练阶段完全使用HiFi-UMI演示数据，无需任何真实机器人轨迹。

### 主要贡献
1. 提出HiFi-UMI数据生产系统，通过提升无机器人UMI数据的保真度，实现了零机器人后训练：仅用HiFi-UMI演示数据微调的策略可直接在真实机器人上部署，并在三个不同架构（视觉-语言-动作族与世界-动作模型族）的基线上，与评估场景内采集的遥操作基线相比，成功率差异仅为-2.5、+3.1和-0.6个百分点。
2. 最强策略在精密插入任务上达到85%成功率，尽管HiFi-UMI轨迹未在该评估场景采集。
3. 在相同语料库上预训练4000小时，将十个未见任务的动作误差降低41%，并使基于StarVLA-QwenPI的真实机器人成功率再提升18.1个百分点。
4. 开源HiFi-UMI-2K数据集：2000小时微秒同步、超宽视角演示数据，每条数据均通过仿真回放自动重建与验证。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：本文针对机器人操作学习的数据瓶颈，提出了一种系统性的数据生产方案，在不依赖昂贵真实机器人数据的情况下实现了高性能策略学习，并提供了大规模开源数据集，对具身智能领域的研究有重要参考价值。实验覆盖多种主流策略架构并报告了量化成功率和动作误差，结果详实。

</details>

<details>
<summary>Abstract</summary>

Learning deployable manipulation policies is bottlenecked by the scarcity of data that is both high-fidelity and scalable. Real-robot teleoperation is accurate but costly to scale; robot-free UMI capture scales readily, and current practice uses the resulting data mainly for pre-training, adding a small real-robot "anchor" at post-training. We ask whether raising the fidelity of robot-free UMI data, rather than shrinking the real-robot fraction, can remove that anchor. We present HiFi-UMI, a portable UMI data-production system co-designed for trajectory accuracy, inter-gripper relative pose, synchronization, and field of view: head-mounted offline stereo-inertial SLAM, native rather than reconstructed relative pose, a shared microsecond GPIO trigger, and two wide-angle cameras per hand covering ~200 degrees. It reaches 3 mm workspace-local end-effector accuracy without external tracking infrastructure. Using this corpus, we demonstrate zero-robot post-training: a policy post-trained solely on HiFi-UMI demonstrations deploys directly on a real robot and matches in-domain teleoperation across three backbones spanning the vision-language-action and world-action-model families, with success-rate differences of -2.5, +3.1, and -0.6 percentage points on StarVLA-QwenPI, OpenPI-pi_0.5, and LingBot-VA; the strongest policy reaches 85% on a precision insertion task, even though the teleoperation baseline is collected in the evaluation scene and no HiFi-UMI trajectory is. Pre-training on 4,000 hours from the same corpus lowers action error on ten unseen tasks by 41% and, on StarVLA-QwenPI, raises real-robot success by a further 18.1 percentage points. We open-source HiFi-UMI-2K, 2,000 hours of microsecond-synchronized, ultra-wide-FoV demonstrations, each automatically reconstructed and validated through simulation replay, as a large-scale, high-fidelity resource for the robot-learning community.

</details>

#### 2026-07-28 - Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control

**Authors:** Jiaxin Bai, Jiaxuan Xiong
**Links:** [abs](https://arxiv.org/abs/2607.25337) - [pdf](https://arxiv.org/pdf/2607.25337)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control
- 作者：Jiaxin Bai, Jiaxuan Xiong
- 出版日期：2026-07-28
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2607.25337

### 一句话总结
本文提出Temporal-Distance JEPA，通过从离线轨迹中挖掘有向时间距离成本来训练JEPA世界模型，使潜在模型预测控制的表现优于现有方法。

### 研究问题
如何让JEPA世界模型规划器在离线演示日志中获取真正的进度成本，而非依赖潜空间欧氏距离这种非设计用于规划的信号，从而缩小训练与规划之间的差距。

### 核心思路/方法
1. 保留LeWM的编码器-预测器主干，并从无奖励轨迹中挖掘有向时间成本。
2. 使用同轨迹步序作为正样本，跨轨迹对作为启发性负样本，并加入滚动一致性项匹配规划器视野。
3. 挖掘得到的监督同时作为规划成本和表示信号：拓扑进度时直接部署成本，接触几何主导时通过改进表示提升欧氏规划。

### 主要贡献
1. 提出Temporal-Distance JEPA，能自主从离线轨迹中提取时间进度结构用于规划。
2. 在锁评估下，部署挖掘成本使Two-Room成功率达到100.0%（LeWM为97.4%），共享欧氏规划使OGB-Cube提升14.2分，并改善Push-T。
3. 与LeWM和RC-aux基线对比，在多个环境上匹配或超过两者表现。
4. 消融实验验证了有向头、跨轨迹负样本和滚动一致性各自的贡献。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。该工作针对具体规划场景（JEPA世界模型控制）有明确改进，但需要读者熟悉JEPA和潜在模型预测控制背景，且未提供局限性细节，适合相关方向研究者快速了解方案。

</details>

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space rather than reconstructing pixels, making them a natural backbone for latent model predictive control from offline demonstration logs. JEPA-style training optimizes short-horizon latent prediction, whereas planning requires a multi-step ranking of imagined futures by goal progress. Prior JEPA planners often inherit that ranking from embedding geometry, typically latent Euclidean distance, which arises as a byproduct of representation learning rather than as a progress cost mined from the logs. We propose Temporal-Distance-JEPA, which retains the LeWM encoder--predictor backbone and mines a directed temporal cost from reward-free trajectories: same-trajectory step order supplies positive targets, cross-trajectory pairs act as heuristic negatives, and a rollout-consistency term matches the planner horizon. The mined supervision serves two roles: as the deployed planning cost when progress is topological, and as a representation signal that improves Euclidean planning when contact geometry dominates. Under locked evaluation, deploying the mined cost raises Two-Room success to 100.0% versus LeWM's 97.4%, while shared Euclidean planning on the same temporally trained checkpoint raises OGB-Cube by 14.2 points over LeWM and improves Push-T. Against LeWM and the concurrent RC-aux baseline under locked evaluation, Temporal-Distance-JEPA matches or exceeds both methods on every environment. Ablations show that the directed head, cross-trajectory negatives, and rollout consistency each contribute. Temporal-Distance-JEPA narrows the train--plan gap for JEPA world-model planners by discovering temporal progress structure in offline logs and co-designing cost form with plan-time deployment. Code is available at https://github.com/HKBU-KnowComp/Temporal-Distance-JEPA.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
