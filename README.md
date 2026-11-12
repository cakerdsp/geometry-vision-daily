# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：43
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 15
  - Embodied / Robotics / AR Applications: 14
  - Neural Scene Representations & Rendering: 10
  - Dynamic / 4D Reconstruction: 2
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **高斯泼溅（Gaussian Splatting）正在从“新视角合成”走向“任务特定化 + 系统化”**
   本批论文中 GS 相关研究占据主导，且明显脱离了单纯追求 PSNR 的阶段，转向具体问题约束：野外照片外观不一致（FastWild-GS）、低光照 RAW 噪声（RetinexGS）、反射去除（RF3DGS）、表面重建的深度正则化（DepthGS）、码率约束下的容量—精度分配（CP-GS）、曲线基元表示（Spaghetti Splatting）。这说明 GS 正在成为“可定制的场景表示底座”，而非单一算法。

2. **前馈三维重建基础模型开始补“可用性”短板：异构相机、交互纠错、与 SLAM/语义结合**
   Camera3R 解决透视预训练模型对非透视/异构相机模型的泛化；Click3R 直面“前馈模型输出不可撤回”的问题，引入稀疏点击做交互式几何校正；V3DSAM 与 GEMOR-GS 则把前馈几何估计/3DGS 地图嵌入 SLAM 系统，补上回环验证、实例建图、在线重定位等系统级能力。趋势是从“重建精度竞赛”转向“可部署、可纠正、可重入”。

3. **物理先验与传感器特性的显式建模成为提升鲁棒性的主流手段**
   RF3DGS 用多视角最小亮度光度先验 + 几何先验构造无反射伪标签；RetinexGS 将颜色分解为视角无关基色与调制场，并用 DNG 噪声元数据加权损失；DepthGS 从理论上推导深度差异与重建误差上界并据此设计自适应正则；Dark Matters/EquivFlow 指出对数类 HDR 编码在冻结 VAE 潜空间中造成暗部色度坍缩，并提出曝光等变编码。共性是：不再依赖“更大模型/更多数据”，而是把成像物理与传感器元数据显式注入优化目标。

4. **“预测效用 vs 决策效用”的区分开始进入机器人与具身智能的表示学习**
   From Prediction to Action 明确提出“能准确预测形变的表示未必最适合选动作”，并在 DLO 平面单抓取控制中比较真值参数、估计参数、学习到的交互历史三类物理上下文；CIALLO 则主张仅靠动作重建不能保证跨具身共享表示，转而对齐动作、视觉变化与语言到“短时程行为意图”空间；AutoVLA-D 发现离散轨迹作为直接输出较弱、但作为连续轨迹的条件更有效。这是一条值得注意的方法论转向：表示的评价标准从“重建/预测误差”转向“下游决策收益”。

5. **世界模型与生成式先验正在与几何/控制结构耦合**
   QCC-WM 用商式因果构造把高维观测压缩为可递归预测的宏状态，并用共享参考商度量约束宏层预测与视觉生成的一致性；Plant Orbiter 用视频扩散生成环绕相机视角再交给 3DGS，实现单图植物重建与文本生成；AutoVLA-D 让离散几何条件先于连续轨迹生成。生成模型不再只是“渲染器”，而是被用作几何/状态空间的约束来源。

#### 技术路线观察

- **几何基础模型方向**：核心矛盾是“大规模透视数据预训练的强先验”与“真实部署中相机模型任意、未知、异构”之间的错配。Camera3R 走参数高效适配（低秩、0.5% 额外参数、不足一天训练），V3DSAM 走“冻结骨干 + 外部语义/几何验证”的组合路线（VGGT-SLAM 2.0 + SAM3，不访问骨干内部特征）。两条路线都刻意避免重训大模型，说明该方向当前的工程重心是复用而非重造。

- **3D/4D 重建方向**：呈现“理论化”与“交互化”两个新支点。DepthGS 是少见的从深度差异推导重建误差上界、再据此设计单视图/多视图自适应正则的工作，属于把经验 trick 换成可解释设计；Click3R 则承认前馈模型必然失败，转而设计人机协同的纠错接口与专门暴露失败模式的基准。二者共同暗示：重建质量的下一个增量可能来自“可证明的正则”与“可纠正的交互”，而非单纯扩大模型。

- **神经场景表示方向**：GS 的技术分化非常清晰——(a) 外观解耦（FastWild-GS 的 128 维 Photo Token + 六参数逐通道变换替代球谐；RetinexGS 的基色/调制场分解）；(b) 资源受限下的表示设计（CP-GS 在共享码率约束下联合优化高斯容量与属性精度，并做分层失真感知量化）；(c) 基元泛化（Spaghetti Splatting 用折线卷积逼近连续曲线，声称是 3DGS 的严格超集）。其中 FastWild-GS 把外观变换同时施加于致密化/剪枝评分渲染，是一个值得注意的“避免把外观差异误算为几何误差”的工程细节。

- **机器人/AR 应用方向**：SLAM 与具身操作两条线都在强化“系统级闭环”。GEMOR-GS 的关键设计是离线标定 LiDAR-相机外参并在全流程复用，再交替优化关键帧位姿与高斯参数，并支持跟踪丢失后的在线重定位；V3DSAM 用像素级双向重投影 + 物体级 3D 空间对应做双尺度回环验证，并以类别约束的 3D 连通性分配全局实例 ID、不做帧间 ID 传播。具身侧则更关注表示的可迁移性与决策价值（CIALLO 的具身嵌入校准、GPF 的几何—指针—流分离）。

- **一个横向观察**：多篇论文都在处理“跨域/跨条件一致性”——跨照片外观（FastWild-GS）、跨视角反射（RF3DGS）、跨相机模型（Camera3R）、跨具身（CIALLO）、宏状态与视觉生成之间（QCC-WM）。一致性约束的具体形式（Token、伪标签、低秩适配、共享参考商度量）差异很大，但问题结构高度相似，存在方法迁移空间。

#### 值得优先阅读的论文

1. **DepthGS（2611.13628）**：本批中少有的给出理论关系与误差上界、并据此推导正则化设计的工作。若关注“GS 表面重建为什么有效/如何原则性设计”，这是最值得读全文的一篇，重点验证其推导假设（单视图/多视图上界）与实际实验的对应程度。

2. **Camera3R（2611.13453）**：几何基础模型适配异构相机是明确的部署瓶颈，且该方法声称参数与训练成本极低、并保留透视输入上的原始性能。优先读以确认低秩适配注入的位置、相机模型参数化方式与训练数据构成（摘要未给出）。

3. **FastWild-GS（2611.13808）**：8.8 分钟/场景、PhotoTourism 上最低 LPIPS，是“野外 GS 效率”这条线的强基线候选；其“外观变换同时用于致密化/剪枝评分”的设计对其他 GS 变体有直接借鉴价值。

4. **From Prediction to Action（2611.14274）**：提出并实证“预测效用 ≠ 决策效用”，且 GPF 仅几何变体相对 DLO 专用扩散策略误差降 32.8%、参数少 18.7 倍、推理快约 193 倍。这一对比如果成立，对具身表示学习的评价范式影响较大，值得读全文核对实验设置与公平性。

5. **CIALLO（2611.13732）**：跨具身共享意图表示 + 仅用 ≤10 秒新机器人录制、只更新具身嵌入即可适配，是“数据高效跨具身迁移”的代表性设定。优先读以确认八具身预训练数据规模、意图空间定义与冻结编解码器后策略学习的实际表现。

（Click3R 与 RF3DGS 可列为次优先：前者的问题定义与基准构建有独立价值，后者的多视角光度

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-11T15:11:26-05:00
**Total number of papers:** 43
**Number of papers added in the latest update:** 14
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

#### 2026-11-10 - Camera3R: Feed-Forward 3D Reconstruction from Heterogeneous Camera Models

**Authors:** Ruxiao Duan, Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari, Alex Wong
**Links:** [abs](https://arxiv.org/abs/2611.13453) - [pdf](https://arxiv.org/pdf/2611.13453)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Camera3R: Feed-Forward 3D Reconstruction from Heterogeneous Camera Models
- 作者：Ruxiao Duan, Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari, Alex Wong
- 出版日期：2026-11-10T01:56:04Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.13453 ；PDF https://arxiv.org/pdf/2611.13453 ；代码 https://github.com/android-xr/camera3r

### 一句话总结
Camera3R 提出一种低秩适配（LoRA 类）框架，以极少新增参数和较短训练时间，将基于透视图像预训练的前馈三维重建网络扩展到任意非透视/异构相机模型，同时保持其在透视输入上的原始性能。

### 研究问题
现有前馈三维重建（3R）基础模型多在大规模透视数据集上训练，虽在透视图像上表现良好，但难以泛化到非透视图像，限制了其在相机模型任意、未知甚至异构场景中的部署。论文关注：如何在尽量少重训练的前提下，让已具备透视重建能力的基础模型适配其他相机模型。

### 核心思路/方法
论文提出 Camera3R，一个低秩适配框架，用于高效地把透视预训练的 3R 网络扩展到其他相机模型。摘要称其目标是以最小重训练复用现有重建模型能力；实验部分声称仅需 0.5% 额外参数、少于一天训练，即可将基础 3R 模型适配到非透视相机，并完全保留其在透视输入上的原始性能。具体低秩适配的模块位置、相机模型参数化方式、训练数据构成等细节，摘要未提供足够信息。

### 主要贡献
- 提出 Camera3R 低秩适配框架，用于将透视预训练的前馈 3R 网络扩展到任意其他相机模型。
- 强调以极少新增参数（0.5%）和较短训练时间（少于一天）完成适配。
- 声称在适配非透视相机的同时，完全保留模型在透视输入上的原始性能。
- 提供开源代码链接。

### 局限性
- 摘要未提供足够信息说明适配所覆盖的具体相机模型类型、数量与范围。
- 摘要未提供足够信息说明“任意其他相机模型”的验证实验设置、数据集与定量指标。
- 摘要未提供足够信息说明低秩适配的具体注入位置、秩取值及消融实验。
- 摘要未提供足够信息说明训练资源的具体配置与“少于一天”的硬件条件。
- 摘要未提供足够信息说明在极端或分布外相机模型上的失败模式与鲁棒性边界。

### 阅读优先级
中。理由：该工作针对前馈 3R 基础模型的相机模型泛化问题，提出低参数、短训练的适配思路，问题定位清晰且具工程实用价值；但摘要仅给出总体声明，缺少实验设置、对比基线与定量细节，需阅读全文才能判断其泛化范围与可靠性。对关注三维重建基础模型适配与异构相机部署的读者优先级可上调至高；对一般读者为中。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction (3R) from unconstrained multi-view images has recently emerged as a prominent research direction in 3D computer vision. Various foundational reconstruction models have been proposed with different architectures and reconstruction paradigms. Despite being trained on large-scale perspective datasets with substantial computational resources, these models generally struggle to generalize to non-perspective images. This limitation hinders their deployment in applications involving arbitrary, unknown, and potentially heterogeneous camera models. To build on the capabilities of existing reconstruction models with minimal retraining, we propose Camera3R, a low-rank adaptation framework that efficiently extends perspective-pretrained 3R networks to any other camera models. Extensive experiments demonstrate that, with only 0.5% additional parameters and less than a day of training, Camera3R adapts a foundational 3D reconstruction model to non-perspective cameras while fully preserving its original performance on perspective inputs. Code is available at https://github.com/android-xr/camera3r.

</details>

#### 2026-11-09 - V3DSAM: Semantic-Geometric Loop Verification and Geometry-Anchored Persistent Instance Mapping for Feed-Forward Dense SLAM

**Authors:** Maolin Ye, Dongqing Zhao, Linyang Li, Shuai Xue, Yuan Liu, Yiyuan Wang, Wen Li
**Links:** [abs](https://arxiv.org/abs/2611.12452) - [pdf](https://arxiv.org/pdf/2611.12452)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, SLAM, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：V3DSAM: Semantic-Geometric Loop Verification and Geometry-Anchored Persistent Instance Mapping for Feed-Forward Dense SLAM
- 作者：Maolin Ye, Dongqing Zhao, Linyang Li, Shuai Xue, Yuan Liu, Yiyuan Wang, Wen Li
- 出版日期：2026-11-09T14:07:07Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.12452 ；PDF https://arxiv.org/pdf/2611.12452

### 一句话总结
V3DSAM 是一个开放词汇语义稠密 SLAM 系统，通过语义-几何双尺度回环验证与几何锚定的持久实例建图，提升长序列前馈稠密 SLAM 中跨视角关联的可靠性。

### 研究问题
论文针对长序列前馈稠密 SLAM 中跨视角关联不可靠的问题。摘要指出，系统需要在场景级和物体级建立物理对应关系；同时，现有方法可能依赖骨干网络内部特征与帧间时序 ID 传播，而论文希望降低这种依赖。

### 核心思路/方法
- 系统将 VGGT-SLAM 2.0 的前馈几何估计与 SAM3 的开放词汇语义观测相结合。
- 提出语义-几何双尺度回环验证：利用像素级双向重投影和物体级 3D 空间对应来识别错误回环，且不访问骨干网络内部特征。
- 提出几何锚定的持久实例建图：在优化后的全局坐标系中，通过类别约束的 3D 连通性定义物理实例，并在不进行帧间身份传播的情况下分配全局 ID。

### 主要贡献
- 提出 V3DSAM 开放词汇语义稠密 SLAM 系统，在场景级与物体级建立物理对应。
- 提出语义-几何双尺度回环验证，用于拒绝错误回环，且不依赖骨干内部特征。
- 提出几何锚定的持久实例建图，通过全局坐标系中的类别约束 3D 连通性定义实例并分配全局 ID，不依赖帧间身份传播。
- 摘要报告：在 TUM RGB-D 评估中，该验证器拒绝了全部四个错误回环候选；在长序列 ScanNet 实验中，实例身份一致性有所提升。
- 摘要总结认为，V3DSAM 降低了长时跨视角关联对骨干内部特征和时序 ID 传播的依赖。

### 局限性
摘要未提供足够信息说明计算开销、实时性、对不同骨干或数据集的泛化能力、失败案例，以及定量指标的完整细节。摘要仅报告了 TUM RGB-D 中四个错误回环候选被全部拒绝，以及 ScanNet 长序列实验中的实例身份一致性提升，未给出更全面的实验设置与消融细节。摘要未提供足够信息。

### 阅读优先级
中。理由：论文主题涉及前馈稠密 SLAM、开放词汇语义、回环验证与持久实例建图，和几何基础模型及机器人/AR 应用相关；摘要给出了明确的方法要点和初步评估结论。但摘要篇幅有限，未提供完整实验细节与性能指标，是否精读可结合对前馈稠密 SLAM 或开放词汇实例建图的兴趣再决定。

</details>

<details>
<summary>Abstract</summary>

To address unreliable cross-view association in long-sequence feed-forward dense SLAM, this letter presents V3DSAM, an open-vocabulary semantic dense SLAM system that establishes physical correspondences at both the scene and object levels. The system combines feed-forward geometric estimates from VGGT-SLAM 2.0 with open-vocabulary semantic observations from SAM3. We introduce semantic-geometric dual-scale loop verification, which identifies false loop closures using pixel-level bidirectional reprojection and object-level 3D spatial correspondences, without accessing backbone-internal features. We further propose geometry-anchored persistent instance mapping, which defines physical instances through class-constrained 3D connectivity in an optimized global coordinate system and assigns global IDs without inter-frame identity propagation. The proposed verifier rejects all four false loop candidates in our TUM RGB-D evaluation, while long-sequence ScanNet experiments show improved instance identity consistency. Thus, V3DSAM reduces dependence on internal backbone features and temporal ID propagation for robust long-term cross-view association.

</details>

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-10 - Dark Matters: VAE-Aware HDR Encoding for SDR-to-HDR Video Reconstruction

**Authors:** Donghoon Cha, Bomseok Park, Hansl von Kwon, Ku DoHyung, Hanwool Sul
**Links:** [abs](https://arxiv.org/abs/2611.13504) - [pdf](https://arxiv.org/pdf/2611.13504)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dark Matters: VAE-Aware HDR Encoding for SDR-to-HDR Video Reconstruction
- 作者：Donghoon Cha, Bomseok Park, Hansl von Kwon, Ku DoHyung, Hanwool Sul
- 出版日期：2026-11-10T03:16:31Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.13504) / [PDF](https://arxiv.org/pdf/2611.13504)

### 一句话总结
论文指出现有对数类 HDR 编码会在冻结 VAE 的潜在表示中造成暗部色度坍缩，并提出一种可逆、曝光等变的编码 EquivFlow，在不修改 VAE 的前提下改善 SDR-to-HDR 视频重建的色度保真度。

### 研究问题
SDR-to-HDR 重建是一个不适定问题，需要恢复被裁剪的高光、被压暗的阴影以及量化伪影，同时保持原始内容。潜在扩散模型虽能提供生成先验来恢复缺失细节，但其效果受制于 HDR 信号如何通过预训练 VAE。作者发现，常见的对数类编码会在生成前压制低亮度色度差异，导致冻结 VAE 潜在空间中的“暗侧坍缩”。

### 核心思路/方法
提出 EquivFlow：一种紧凑、可逆的曝光等变编码，将曝光变化映射为加性偏移，同时保留与尺度无关的色度分量，并且不修改 VAE。该编码被集成到 SDR-to-HDR 视频扩散流程中。摘要还提到在预训练图像与视频 VAE 上进行了编码层面测试，观察其曝光结构与深暗色度传输在测试宿主中的表现。

### 主要贡献
- 揭示常见对数类 HDR 编码在冻结 VAE 潜在空间中导致低亮度色度差异被压制、出现暗侧坍缩的问题。
- 提出 EquivFlow 编码，使曝光变化表现为加性偏移，并保留尺度无关的色度分量，且无需修改 VAE。
- 在测试的预训练图像和视频 VAE 上验证其曝光结构与深暗色度传输特性。
- 将 EquivFlow 集成到 SDR-to-HDR 视频扩散中，在测试设置下报告一致的色度保真度增益，同时保持有竞争力的重建保真度。

### 局限性
摘要未提供足够信息说明定量实验规模、对比基线细节、失败案例、计算开销，以及 EquivFlow 在其他编码器或更广泛 HDR 内容上的泛化边界。

### 阅读优先级
中：问题定位具体且有洞察（VAE 输入编码导致暗部色度坍缩），方法轻量且不修改 VAE，对 SDR-to-HDR 与扩散先验结合的研究有参考价值；但摘要未给出充分实验细节，需阅读全文确认增益幅度与适用范围。

</details>

<details>
<summary>Abstract</summary>

SDR-to-HDR reconstruction is an ill-posed problem in which clipped highlights, crushed shadows, and quantization artifacts must be recovered while preserving the original content. Latent diffusion models provide powerful generative priors for restoring missing detail, but their effectiveness is constrained by how HDR signals pass through the pretrained VAE. We find that common log-like encodings suppress low-luminance chromatic differences before generation, producing a dark-side collapse in the frozen-VAE latent. We introduce EquivFlow, a compact, invertible exposure-equivariant encoding that maps exposure changes to additive shifts while retaining a scale-independent chromatic component, without modifying the VAE. Encoding-level tests across pretrained image and video VAEs show that its exposure structure and deep-dark chroma transport persist across the tested hosts. Integrated into SDR-to-HDR video diffusion, EquivFlow delivers consistent chromatic-fidelity gains across the tested settings while retaining competitive reconstruction fidelity.

</details>

#### 2026-11-08 - Kinematic Total-Body PET Video Reconstruction via Hierarchical List-Mode EM and Validation-Adaptive Space-Time Regularisation

**Authors:** Andrew J. Reader, Gary J. R. Cook, Paul K. Marsden, Sarah-May Gould, Alexander Hammers, Simon R. Cherry
**Links:** [abs](https://arxiv.org/abs/2611.11052) - [pdf](https://arxiv.org/pdf/2611.11052)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Kinematic Total-Body PET Video Reconstruction via Hierarchical List-Mode EM and Validation-Adaptive Space-Time Regularisation
- 作者：Andrew J. Reader, Gary J. R. Cook, Paul K. Marsden, Sarah-May Gould, Alexander Hammers, Simon R. Cherry
- 出版日期：2026-11-08T01:09:17Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.11052) / [PDF](https://arxiv.org/pdf/2611.11052)

### 一句话总结
论文提出“运动学PET（Kinematic PET）”成像任务，并给出一种面向全身PET视频重建的层级列表模式EM与验证自适应时空正则化方法，用于在不门控条件下观察早期示踪剂输运和快速多器官运动。

### 研究问题
摘要指出，研究关注的是无需门控即可可视化早期放射性示踪剂递送和快速多器官运动的PET成像任务。为实现这一目标，需要在约33 ms（约30帧/秒）的超短帧条件下进行全身PET视频重建，并应对超短帧带来的噪声放大问题。

### 核心思路/方法
方法采用33 ms帧，并以3D EM TOF列表模式重建作为初始化，随后循环执行两阶段更新：
1. 层级EM（HEM）更新：使用多个时间池化层级，将帧特定的EM校正与来自更高计数时间块的校正结合，以减缓超短帧的噪声放大。
2. 验证自适应时空（VAST）正则化更新：对每帧中的每个3D目标图像块，在空间和时间邻近区域采样源图像块，选择与相邻两帧对应图像块均值最匹配的候选，未改变的图像块也可作为候选。
此外，可选的时间块求和校正以初始EM时间求和为参考，用于减少空间细节损失。

### 主要贡献
- 提出“运动学PET”作为聚焦早期示踪剂递送和快速多器官运动、无需门控可视化的成像任务。
- 提出结合HEM与VAST的全身PET视频重建方法，用于33 ms超短帧的列表模式重建。
- 在动态数字体模中评估HEM+VAST，并在Siemens Biograph Vision Quadra采集的人体FDG数据（注射后28–58 s）上展示。
- 摘要报告：在背景空间变异系数为10%时，最快体模团注的时间半高全宽为151 ms（HEM+VAST），真实值为86 ms；视频帧率FDG图像显示血管与器官细节、示踪剂团注通过及呼吸相关多器官运动。
- 指出运动学PET可作为传统动态PET的补充，支持图像衍生生理生物标志物开发和定量重建中的运动估计。

### 局限性
- 摘要仅报告了体模中快速团注时间半高全宽的对比（151 ms vs 真实值86 ms），未提供更全面的定量评估细节。
- 摘要未提供与既有4D PET重建方法在相同33 ms帧时长和匹配噪声水平下的对比结果；作者明确将此类比较列为未来工作。
- 摘要未提供人体FDG数据的定量评价指标、统计检验或读者研究信息。
- 摘要未提供计算复杂度、重建耗时、参数敏感性或更大规模临床验证的信息。
- 摘要未提供VAST中空间/时间邻域采样范围、候选数量等实现细节的完整参数信息。

### 阅读优先级
中。理由：该论文面向全身PET超短帧视频重建，问题明确，方法组合（HEM+VAST）和33 ms帧设置具有方法学参考价值；但摘要显示当前验证主要包括动态数字体模和有限人体FDG数据展示，且与已有4D PET方法的系统比较尚列为未来工作。若读者关注动态/4D PET重建、超短帧噪声抑制或时空正则化，优先级可提高；若关注成熟临床验证或完整实验基准，则需等待全文进一步信息。

</details>

<details>
<summary>Abstract</summary>

Kinematic PET is introduced as an imaging task focused on visualisation of early radiotracer delivery and rapid multi-organ motion without gating. The proposed kinematic video reconstruction method uses 33-ms frames (~30 frames per second), initialised with 3D expectation maximisation (EM) time of flight (TOF) list-mode reconstruction, followed by cycles of a 2-stage update. These 2 stages are i) a hierarchical EM (HEM) update using multiple temporal pooling levels, and ii) a validation-adaptive space-time (VAST) regularisation update. HEM combines frame-specific EM corrections with corrections estimated from higher-count temporal blocks, slowing noise amplification for the ultrashort frames. VAST mixes each 3D target patch in a frame with source patches sampled nearby in space and time. It selects the candidate that best matches the mean of the corresponding patches in the two adjacent frames, with the unchanged patch also eligible. Optional temporal block sum correction uses the initial EM temporal sum as a reference to reduce loss of spatial detail. HEM+VAST was evaluated with a dynamic digital phantom, and demonstrated on human FDG data acquired on a Siemens Biograph Vision Quadra (28 - 58 s post-injection). At a background spatial coefficient of variation of 10%, the temporal full width at half maximum of the fastest phantom bolus was 151 ms with HEM+VAST, compared with 86 ms for the ground truth. The video frame rate FDG images reveal vascular and organ detail, radiotracer bolus passage and respiration-related multi-organ motion. Kinematic PET could complement conventional dynamic PET by supporting the development of image-derived physiological biomarkers and motion estimation for quantitative reconstruction. Future work should compare HEM+VAST with prior 4D PET reconstruction methods at the same 33-ms frame duration and matched noise levels.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-10 - CJRR-Net: A Candidate-Joint Reprojection Ranking for Future-View Selection in Human Pose Estimation

**Authors:** Huiting Xi, Marsha Mariya Kappan, Eduardo Benitez Sandoval, Francisco Cruz
**Links:** [abs](https://arxiv.org/abs/2611.13700) - [pdf](https://arxiv.org/pdf/2611.13700)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CJRR-Net: A Candidate-Joint Reprojection Ranking for Future-View Selection in Human Pose Estimation
- 作者：Huiting Xi, Marsha Mariya Kappan, Eduardo Benitez Sandoval, Francisco Cruz
- 出版日期：2026-11-10T07:46:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.13700) / [PDF](https://arxiv.org/pdf/2611.13700)

### 一句话总结
论文提出 CJRR-Net，在 MPI-INF-3DHP 的八个标定相机中为未来视角选择任务构建候选视角特定几何特征，并在所选视角上取得低于共享输入 MLP 与适配版 PoseErrNet 的 2D MPJPE。

### 研究问题
多相机系统用于表演记录、体育与人体运动分析时，选择信息量高的视角对可靠的人体姿态估计很重要。论文关注的问题是：在八个已标定相机的固定设置下，如何为未来视角选择出更有利于人体姿态估计的相机视角。摘要将任务表述为“future-view selection”，但对该任务的时间定义与设定细节未作进一步说明。

### 核心思路/方法
CJRR-Net（Candidate-Joint Reprojection Ranking Network）将以下几类信息结合：
- 当前视角的姿态观测；
- 相机配置；
- 候选视角特定几何特征：通过将估计的 3D 姿态及其不确定性重投影到每个候选视角获得。

模型据此在 MPI-INF-3DHP 的八个标定相机之间进行未来视角选择。摘要还提到使用 blender rollout 展示重复的相机选择过程。

### 主要贡献
- 提出 CJRR-Net，用于八相机标定设置下的未来视角选择。
- 将当前视角姿态观测、相机配置与候选视角特定的重投影几何特征结合，用于候选视角排序/选择。
- 在所选视角的 2D MPJPE 上报告 105.18 像素，低于共享输入 MLP 的 114.64 像素与适配 PoseErrNet 的 117.56 像素。
- 在摘要列出的每个评估遮挡组中，取得所列策略中最低的平均误差。
- 通过 blender rollout 展示重复相机选择。
- 摘要结论支持：在所评估的固定八相机设置中，候选视角特定几何对单视角选择具有作用。

### 局限性
- 摘要仅给出 MPI-INF-3DHP 上八个标定相机的固定设置，未说明该设置之外的泛化能力；其他相机数量、布局或数据集上的表现摘要未提供足够信息。
- 摘要给出 2D MPJPE 数值，但未提供完整实验协议、训练细节、消融实验、统计显著性等；这些内容摘要未提供足够信息。
- “future-view selection”的具体时间定义、预测时域与在线/离线设定，摘要未提供足够信息。
- 遮挡组评估的分组标准与具体结果明细，摘要未提供足够信息。
- blender rollout 的具体用途、指标与结果细节，摘要未提供足够信息。
- 与共享输入 MLP、适配 PoseErrNet 的公平性设置与实现细节，摘要未提供足够信息。

### 阅读优先级
中。理由：论文主题集中在多相机人体姿态估计中的视角选择，且摘要给出了明确的对比数值与遮挡组结论，适合关注多视角几何与视角选择的研究者进一步阅读；但摘要未提供实验细节、泛化验证与任务时间定义，是否高优先级取决于读者对固定八相机设置下候选几何特征的兴趣。

</details>

<details>
<summary>Abstract</summary>

Multi-camera systems support performance recording, sports and human-movement analysis, where selecting an informative viewpoint is important for reliable human pose estimation. We propose the Candidate-Joint Reprojection Ranking Network (CJRR-Net) for future-view selection among eight calibrated cameras in MPI-INF-3DHP. The model combines current-view pose observations, camera configuration, and candidate-specific geometric features obtained by reprojecting the estimated 3D pose and its uncertainty into each candidate view. CJRR-Net achieves a selected-view 2D mean per-joint position error (MPJPE) of 105.18 pixels, compared with 114.64 pixels for the shared-input MLP and 117.56 pixels for adapted PoseErrNet. It also achieves the lowest mean error among the listed policies in each evaluated occlusion group. A blender rollout illustrates repeated camera selection. These findings support candidate-specific geometry for single-view selection in the evaluated fixed eight-camera setting.

</details>

#### 2026-11-10 - DepthGS: Depth-Guided Gaussian Splatting with Adaptive Regularization for High-Quality Surface Reconstruction

**Authors:** Xiao Ren, Yu Liu, Ning An, Jian Cheng, Xin Qiao, You-Fu Li, He Kong
**Links:** [abs](https://arxiv.org/abs/2611.13628) - [pdf](https://arxiv.org/pdf/2611.13628)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DepthGS: Depth-Guided Gaussian Splatting with Adaptive Regularization for High-Quality Surface Reconstruction
- 作者：Xiao Ren, Yu Liu, Ning An, Jian Cheng, Xin Qiao, You-Fu Li, He Kong
- 出版日期：2026-11-10T06:16:16Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；副分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.13628 ；PDF https://arxiv.org/pdf/2611.13628

### 一句话总结
DepthGS 是一个深度引导的 3D Gaussian Splatting 框架，通过理论分析深度差异与重建误差的关系，设计了单视图与多视图的自适应正则化策略，用于高质量表面重建。

### 研究问题
论文指出，3DGS 已从新视角合成扩展到表面重建，但深度信息与重建误差之间的关系尚未被充分探索，这限制了几何优化策略的原则性设计。因此，论文关注如何基于深度差异与重建误差的理论关系，设计更有依据的几何正则化方法，以提升表面重建质量。

### 核心思路/方法
论文提出 DepthGS，一个深度引导的高斯泼溅框架。其核心是从理论上推导单视图和多视图设置下深度差异与重建误差之间的关系，并建立相应的重建误差上界。基于该分析，论文设计了两类自适应正则化策略：
1. 单视图优化：提出深度差异引导的自适应法向正则化策略，利用由局部深度差异计算出的几何可靠性权重来调制法向约束强度。
2. 多视图优化：引入跨视图深度一致性正则化策略，促进相邻视图深度图与“将当前视图深度预测变换到相邻视图所得的深度预测”之间的一致性。

### 主要贡献
- 推导了单视图和多视图设置下深度差异与重建误差的理论关系，并严格建立相应的重建误差上界。
- 基于上述理论分析，设计了单视图下的深度差异引导自适应法向正则化策略。
- 提出了多视图下的跨视图深度一致性正则化策略。
- 摘要称在 DTU、Mip-NeRF360 和 Tanks and Temples 上的实验表明，DepthGS 在表面重建和新视角合成两方面均取得有竞争力的性能。

### 局限性
摘要未提供足够信息。摘要未给出具体实验指标、计算开销、对深度输入质量或来源的依赖程度、失败案例，也未说明理论假设在实际场景中的适用边界。

### 阅读优先级
中。理由：论文将深度差异与重建误差的理论关系同自适应正则化设计直接关联，问题动机和方法结构较清晰，且涉及表面重建与新视角合成两个任务；但摘要未提供定量结果和实现细节，是否值得深入阅读需结合具体实验数据与复现条件进一步判断。

</details>

<details>
<summary>Abstract</summary>

Recently, 3D Gaussian Splatting (3DGS) has emerged as an efficient representation for novel view synthesis, offering fast differentiable rendering and high visual fidelity, and has increasingly been extended to surface reconstruction. However, the relationship between depth information and reconstruction error remains insufficiently explored, limiting the principled design of geometric optimization strategies. To fill the above gap, we propose DepthGS, a depth-guided Gaussian splatting framework. We derive theoretical relations between depth discrepancies and reconstruction error under single-view and multi-view settings, and rigorously establish corresponding upper bounds on reconstruction error. The above analysis informs the design of adaptive regularization strategies in both single-view and multi-view optimization. More specifically, for single-view optimization, we propose a depth-difference-guided adaptive normal regularization strategy that modulates the normal constraint strength using a geometric reliability weight computed from local depth differences. For multi-view optimization, we introduce a cross-view depth consistency regularization strategy that promotes consistency between neighboring-view depth maps and the corresponding depth predictions obtained by transforming the current view's depth predictions into those neighboring views. Extensive experiments on DTU, Mip-NeRF360, and Tanks and Temples demonstrate that DepthGS achieves competitive performance in both surface reconstruction and novel view synthesis.

</details>

#### 2026-11-10 - Lightweight Deep Learning Framework for Astrocyte-Centric 3D Reconstruction across Normal and Stress-associated Ultrastructural States

**Authors:** Bowen Deng, Gwang-Jin Jeong, Seulgi Noh, Ji Young Mun, Na Young Kim
**Links:** [abs](https://arxiv.org/abs/2611.13581) - [pdf](https://arxiv.org/pdf/2611.13581)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lightweight Deep Learning Framework for Astrocyte-Centric 3D Reconstruction across Normal and Stress-associated Ultrastructural States
- 作者：Bowen Deng, Gwang-Jin Jeong, Seulgi Noh, Ji Young Mun, Na Young Kim
- 出版日期：2026-11-10T04:54:30Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次分类
- 链接：摘要页 https://arxiv.org/abs/2611.13581 ；PDF https://arxiv.org/pdf/2611.13581

### 一句话总结
论文提出轻量级框架 AstroSeg-vEM，用于在体积电子显微镜（vEM）图像中实现以星形胶质细胞为中心的分割、三维重建与定量形态分析，并在正常与形态学定义的应激相关星形胶质细胞超微结构状态数据上报告了较高分割精度与消费级硬件上的高效重建能力。

### 研究问题
星形胶质细胞形态与其支持和调控神经回路功能的能力密切相关，但从 vEM 数据重建其形态仍然劳动密集且计算资源消耗大，尽管 vEM 具有高空间分辨率，这阻碍了其更广泛采用与可扩展性。论文关注的问题是：如何在高分辨率、各向异性的 vEM 数据上，以较轻量的计算方式实现保持形态的星形胶质细胞分割、三维重建与定量形态分析，并适用于下游校对工作流。

### 核心思路/方法
AstroSeg-vEM 是一个轻量级、以星形胶质细胞为中心的框架，包含形态保持的星形胶质细胞分割、三维重建和定量形态分析。方法上将基于 transformer 的二维分割与专门的后处理方法结合，直接在高分辨率 EM 切片上运行，适合各向异性 vEM 数据和下游校对流程，并保留原始 EM 数据的完整面内分辨率。摘要提到在四个小鼠海马数据集上评估，这些数据集代表正常和形态学定义的应激相关星形胶质细胞超微结构状态；在留出测试集上平均 Dice 和加权 Dice 分别为 0.92 和 0.95。其轻量架构支持在消费级硬件上进行高效、高保真重建。

### 主要贡献
- 提出 AstroSeg-vEM：一个轻量级、以星形胶质细胞为中心的 vEM 框架，用于分割、三维重建和定量形态分析。
- 方法设计结合 transformer 二维分割与专门后处理，直接处理高分辨率 EM 切片，适配各向异性 vEM 数据与校对工作流，并保留完整面内分辨率。
- 在四个小鼠海马数据集（涵盖正常与形态学定义的应激相关星形胶质细胞超微结构状态）上展示稳健性能与泛化能力，留出测试集平均 Dice 0.92、加权 Dice 0.95。
- 轻量架构支持消费级硬件上的高效高保真重建，面向大规模星形胶质细胞超微结构分析和未来星形胶质细胞—神经元相互作用研究提供可扩展、可及的平台。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、对不同成像条件或物种的泛化边界、计算资源与运行时间的具体量化、标注依赖程度、后处理参数敏感性，以及三维重建质量的独立评价指标。摘要也未提供足够信息说明与其它方法的系统性对比结果。上述内容均无法仅依据摘要判断。

### 阅读优先级
中。理由：该工作面向 vEM 中星形胶质细胞的三维重建与形态分析，问题明确且应用价值清晰，摘要给出了留出测试集上的 Dice 指标和轻量化、消费级硬件可用的定位；但摘要未提供与现有方法的对比、详细实验设置和三维重建质量的独立验证信息。若读者关注轻量级 vEM 分割重建、星形胶质细胞形态定量或应激相关超微结构状态分析，优先级可提高；否则可作为方法参考类论文阅读。

</details>

<details>
<summary>Abstract</summary>

The morphology of astrocytes is closely associated with their ability to support and modulate neural circuit functions; however, its reconstruction from volume electron microscopy (vEM) data remains labor-intensive and computationally resource-intensive, placing substantial barriers on its broader adoption and scalability despite the high spatial resolution of vEM. We present AstroSeg-vEM, a lightweight, astrocyte-centric framework for morphology-preserving astrocyte segmentation, 3D reconstruction, and quantitative morphological analysis in vEM images. AstroSeg-vEM combines transformer-based 2D segmentation with dedicated post-processing methods and operates directly on high-resolution EM sections, making it well suited to anisotropic vEM data and downstream proofreading workflows while preserving the full in-plane resolution of the original EM data. Across four mouse hippocampal datasets representing normal and morphologically defined stress-associated astrocyte ultrastructural states, AstroSeg-vEM demonstrates robust performance and generalization, achieving average Dice and weighted Dice values of 0.92 and 0.95, respectively, on a held-out test dataset. Its lightweight architecture enables efficient, high-fidelity reconstruction on consumer-grade hardware, providing a scalable and accessible platform for large-scale astrocyte ultrastructure analysis and future astrocyte-neuron interaction studies.

</details>

#### 2026-11-10 - GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM

**Authors:** Yuchen Yang, Ming Ding, Xinyu Wu, Hesheng Wang
**Links:** [abs](https://arxiv.org/abs/2611.13528) - [pdf](https://arxiv.org/pdf/2611.13528)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** SLAM, visual SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, differentiable rendering, rendering, splatting, robot perception, mapping, localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM
- 作者：Yuchen Yang, Ming Ding, Xinyu Wu, Hesheng Wang
- 出版日期：2026-11-10T03:51:43Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.13528)｜[PDF](https://arxiv.org/pdf/2611.13528)

### 一句话总结
GEMOR-GS 通过离线标定并复用 LiDAR-相机外参、交替优化关键帧位姿与高斯参数、并在跟踪丢失后利用 3DGS 地图进行在线重定位，提升 LiDAR-惯性-视觉 SLAM 中高斯地图的几何精度、外观保真度与可重新进入能力。

### 研究问题
论文关注 LiDAR-惯性-视觉 SLAM 系统在连续运行中对真实感且度量一致的世界表示的需求。摘要指出，3D Gaussian splatting 可提供显式、可渲染、可查询的场景模型，但需要使高斯地图几何准确、全局精炼并支持重新进入。具体问题包括：如何改进 3DGS 地图的几何与外观；如何在跟踪丢失后从 3DGS 地图恢复位姿；以及外参质量与重定位表现之间的关系。

### 核心思路/方法
- **外参离线标定与复用**：首先在专用标定片段上，通过直接法对齐离线估计 LiDAR-相机外参，并在后续所有在线和离线过程中复用该外参。
- **关键帧位姿与高斯参数交替优化**：在校准后的几何下，利用带门控的可微渲染与 LiDAR 投影目标，交替精炼关键帧位姿和高斯参数。
- **全局重建**：从精炼后的关键帧模式重建最终全局重建，并解除所有在线约束。
- **在线重定位**：在跟踪丢失后，通过 XFeat bypass map、RANSAC-PnP 粗定位以及 Gaussian RGB-D warp refinement，从 3DGS 地图中恢复位姿。

### 主要贡献
- 提出 GEMOR-GS，使高斯地图几何准确、全局精炼且可重新进入，面向机器人感知与决策。
- 设计离线 LiDAR-相机外参标定并在在线/离线流程中复用的机制。
- 采用带门控可微渲染与 LiDAR 投影目标，交替优化关键帧位姿与高斯参数，并进行全局重建。
- 提供基于 3DGS 地图的在线重定位流程，包括 XFeat bypass map、RANSAC-PnP 粗定位与 Gaussian RGB-D warp refinement。
- 摘要报告：在一个自采集序列和五个公开序列上，离线重建相对在线地图在所有配对关键帧上提升 14.3–19.9 dB，PSNR 较 Gaussian-LIC2 提升约 9 dB，保留集重定位成功率为 86–100%，并与外参质量相关。

### 局限性
- 摘要未提供足够信息说明方法在动态场景、极端光照或大规模环境中的表现。
- 摘要未提供足够信息说明计算开销、实时性、内存占用或在线运行效率。
- 摘要未提供足够信息说明外参标定失败或外参退化时重定位性能的具体下降程度与鲁棒性边界。
- 摘要未提供足够信息说明五个公开序列的具体名称、场景类型与评测协议细节。
- 摘要未提供足够信息说明与更多基线方法的全面对比结果。

### 阅读优先级
**中**。理由：该论文与 3DGS SLAM、LiDAR-惯性-视觉融合、地图全局精炼和重定位直接相关，摘要给出了较明确的性能提升数字；但摘要未提供实验细节、实时性与鲁棒性信息，是否高优先级取决于读者对 3DGS SLAM 全局建图与在线重定位方向的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Photorealistic and metrically consistent world representations are a primary requirement for LiDAR--inertial--visual SLAM systems that serve robots over continuous operation. 3D Gaussian splatting makes such representations attainable by supplying an explicit, renderable, and queryable scene model. We present GEMOR-GS (Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM) to make the Gaussian map geometrically accurate, globally refined, and re-enterable, providing a better appearance for robot perception and decision-making. To improve the 3DGS map, the LiDAR--camera extrinsic is first estimated offline by direct-method alignment over dedicated calibration segments and reused by all following online and offline processes. Under the calibrated geometry, keyframe poses and Gaussian parameters are refined alternately under a gated differentiable-rendering and LiDAR--projection objective. The final global reconstruction is then rebuilt from the refined keyframe schema with all online constraints lifted. For the robot SLAM lifecycle, the method recovers the pose from the 3DGS map after tracking loss through an XFeat bypass map, RANSAC-PnP coarse localization, and Gaussian RGB-D warp refinement. Experiments on one self-collected and five public sequences quantify each element: the offline reconstruction wins all paired keyframes against the online map by 14.3--19.9 dB, improves PSNR by approximately 9 dB over Gaussian-LIC2, and achieves 86--100% held-out relocalization success tied to extrinsic quality. The results show that GEMOR-GS improves the geometric accuracy, appearance fidelity, and re-enterability of the 3DGS map, serving as a dependable robot world model for SLAM and downstream tasks.

</details>

#### 2026-11-09 - Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks

**Authors:** Hao Gu, Jin Yao, Zezhou Cheng
**Links:** [abs](https://arxiv.org/abs/2611.12875) - [pdf](https://arxiv.org/pdf/2611.12875)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, geometric reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks
- 作者：Hao Gu, Jin Yao, Zezhou Cheng
- 出版日期：2026-11-09T18:58:02Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.12875 ；PDF https://arxiv.org/pdf/2611.12875

### 一句话总结
Click3R 提出一种交互式几何校正框架：在给定图像对和少量用户提供的跨视图点对应后，通过轻量级点对应适配器向 3D 重建网络注入几何约束，从而修正前馈式重建模型难以更改的预测错误。

### 研究问题
现有前馈式大规模 3D 重建模型只输出单一且不可撤回的预测；当模型失败时，缺少纠正机制。论文关注如何利用稀疏的人类对应点击，对这类前馈模型的几何重建结果进行交互式校正，并应对重复纹理、对称结构、大视角变化或无纹理区域等困难场景。

### 核心思路/方法
给定一对图像以及用户提供的一小组跨视图点对应，Click3R 通过轻量级点对应适配器将几何约束注入 3D 重建网络，使模型能够缓解上述挑战场景中的歧义。为评估交互式重建，论文还构建了一个专门用于暴露现有前馈式 3D 重建方法失败模式的挑战性基准。

### 主要贡献
- 提出 Click3R，一种利用稀疏人类对应点击对前馈式 3D 重建模型进行交互式几何校正的框架。
- 设计轻量级点对应适配器，将用户提供的跨视图对应作为几何约束注入重建网络。
- 构建一个具有挑战性的交互式重建基准，用于暴露现有前馈式方法的失败模式。
- 实验表明，仅需一次对应点击即可降低重建误差，并在标准基准和所构建基准上均有性能提升。

### 局限性
摘要未提供足够信息。摘要未说明适配器的具体结构、训练或推理成本、对点击质量的敏感程度、基准规模与评价指标细节，也未讨论失败案例或适用范围限制。

### 阅读优先级
中。理由：该工作针对前馈式 3D 重建缺乏纠错机制的问题，提出稀疏交互校正思路，问题定义清晰且具有实用性；但摘要仅给出总体效果结论，未提供方法细节与充分实验信息，是否值得优先精读取决于读者对交互式 3D 重建或人机协同几何校正的兴趣。

</details>

<details>
<summary>Abstract</summary>

Despite impressive progress, existing feed-forward large 3D reconstruction models produce a single, irrevocable prediction. When these models fail, there is no mechanism to correct their mistakes. To address this limitation, we introduce Click3R, a framework for interactive geometric correction of feed-forward models using sparse human correspondence clicks. Given an image pair and a small set of cross-view point correspondences provided by a user, Click3R injects geometric constraints into the 3D reconstruction networks through a lightweight point correspondence adapter, enabling the model to resolve ambiguities in challenging scenarios such as repetitive textures, symmetric structures, large viewpoint changes, or textureless regions. To evaluate interactive reconstruction, we curate a challenging benchmark specifically designed to expose failure modes of existing feed-forward 3D reconstruction methods. Experiments show that Click3R reduces reconstruction error with as few as a single correspondence click, improving performance on both standard and our curated benchmarks. Our results highlight that sparse human interaction provides an effective and practical mechanism for correcting geometric reconstruction errors.

</details>

#### 2026-11-09 - A forensic evaluation framework for egocentric foundation models: an EFM3D case study for crime scene reconstruction

**Authors:** Davidson Chisom Onwubiko, Shahana Bano, Carlos Francisco Moreno-García
**Links:** [abs](https://arxiv.org/abs/2611.12259) - [pdf](https://arxiv.org/pdf/2611.12259)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A forensic evaluation framework for egocentric foundation models: an EFM3D case study for crime scene reconstruction
- 作者：Davidson Chisom Onwubiko, Shahana Bano, Carlos Francisco Moreno-García
- 出版日期：2026-11-09T11:49:04Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.12259) / [PDF](https://arxiv.org/pdf/2611.12259)

### 一句话总结
本文提出了一个用于评估第一视角基础模型在犯罪现场重建中的取证评估框架，并以 EFM3D 为案例在四个模拟室内犯罪场景上进行了评估，结果显示该模型更适合场景上下文记录与复核，而非高保真取证采集。

### 研究问题
基础模型越来越多地将几何、语义与空间上下文结合用于三维场景理解，但其是否适用于法医犯罪现场重建仍不明确。本文关注的是：如何构建一个结构化的取证评估框架，并据此判断第一视角基础模型（以 EFM3D 为例）在犯罪现场重建中的实际适用性。

### 核心思路/方法
- 构建了一个结构化的取证评估框架，用于评估第一视角基础模型，并将其应用于 EFM3D。
- 在罗伯特戈登大学 East Lodge House 法医培训设施中，使用 Meta Project Aria Gen 1 录制了四个模拟室内犯罪场景。
- 该框架从四个方面进行评估：房间尺度的重建、语义场景理解、计算性能，以及取证适用性。
- 由于缺少参考网格与专家标注的三维真值，统计结果被作为描述性输出，而非几何或检测精度的度量。

### 主要贡献
- 提出了一个可复现的、面向专业取证场景的第一视角基础模型评估框架。
- 以 EFM3D 为案例给出了实证评估结果：
  - 四个场景生成的网格平均为 12,668±2,430 个顶点、24,838±4,903 个面。
  - 记录了 39,529 条语义预测，覆盖 21--24 个类别，平均置信度为 0.40。
  - 最终推理每个场景处理 1,388±203 个片段，速度为 0.69±0.01 样本/秒，每次录制约需 50.77±6.12 分钟。
  - 七项标准的能力画像显示，该模型在房间几何、家具定位、场景上下文和空间关系方面的支持较强，对细尺度法医证据的支持较弱。
- 结论上，将 EFM3D 定位为上下文记录与场景复核的补充工具，而非高保真取证采集的替代方案。

### 局限性
- 摘要明确指出，缺少参考网格与专家标注的三维真值，因此相关统计仅为描述性输出，不能作为几何或检测精度的度量。
- 实验基于四个模拟室内犯罪场景，场景数量有限。
- 摘要未提供足够信息说明真实犯罪现场的泛化能力、不同设备或环境条件下的表现，以及语义预测的具体准确性评估。
- 摘要未提供足够信息说明框架中七项标准的具体定义与评分方式。
- 摘要未提供足够信息说明与其他基础模型或重建方法的对比结果。

### 阅读优先级
中。理由：本文的核心价值在于提出了一个面向取证场景的第一视角基础模型评估框架，并给出了 EFM3D 的案例数据与能力画像，对关注三维重建、第一视角感知与法医应用交叉方向的研究者有参考意义；但摘要显示其评估缺乏几何与检测真值，结论以描述性统计和能力画像为主，且实验规模有限，因此不属于必须优先精读的论文。

</details>

<details>
<summary>Abstract</summary>

Foundation models increasingly combine geometry, semantics, and spatial context for three-dimensional scene understanding, but their suitability for forensic crime scene reconstruction remains unclear. This study presents a structured forensic evaluation framework for egocentric foundation models and demonstrates it using the Egocentric Foundation Model for 3D (EFM3D). Four simulated indoor crime scenes were recorded with Meta Project Aria Gen~1 at Robert Gordon University's East Lodge House forensic training facility. The framework evaluates room-scale reconstruction, semantic scene understanding, computational performance, and forensic suitability. Across the four scenes, EFM3D generated meshes averaging $12{,}668\pm2{,}430$ vertices and $24{,}838\pm4{,}903$ faces, with 39,529 recorded semantic predictions spanning 21--24 categories at a mean confidence of 0.40. Because reference meshes and expert-labelled 3D ground truth were unavailable, these statistics are treated as descriptive outputs rather than measures of geometric or detection accuracy. Final inference runs processed $1{,}388\pm203$ snippets per scene at $0.69\pm0.01$ samples/s and required $50.77\pm6.12$ minutes per recording. A seven-criterion capability profile indicated stronger support for room geometry, furniture localisation, scene context, and spatial relationships than for fine-scale forensic evidence. The results position EFM3D as a complementary tool for contextual documentation and scene review rather than a replacement for high-fidelity forensic capture. The framework provides a reproducible basis for evaluating future egocentric foundation models in specialised forensic settings.

</details>

#### 2026-11-09 - DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing

**Authors:** Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta, Xin He
**Links:** [abs](https://arxiv.org/abs/2611.12038) - [pdf](https://arxiv.org/pdf/2611.12038)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** metric depth, scene reconstruction, simultaneous localization and mapping, SLAM, visual SLAM, camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing
- 作者：Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta, Xin He
- 出版日期：2026-11-09T08:15:55Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.12038 ；PDF https://arxiv.org/pdf/2611.12038

### 一句话总结
DPGS-SLAM 是一个面向含动态物体环境的单目 RGB SLAM 框架，通过异步扩散补全被遮挡静态背景，并用“来源标签”区分生成与观测支持的高斯基元，以减轻动态观测对跟踪与建图的影响。

### 研究问题
摘要指出，动态观测会污染视觉 SLAM 的相机跟踪与场景重建；现有 3DGS-SLAM 系统在动态物体违反其静态场景假设时可能不稳定。直接排除动态观测虽可降低影响，但可能导致被遮挡的静态背景缺失或约束不足。论文旨在解决这一矛盾：既要抑制动态区域对跟踪与建图的干扰，又要为观测不足的静态背景提供临时表示。

### 核心思路/方法
- 框架定位：单目 RGB SLAM，面向动态环境中的稠密建图，结合 3D Gaussian Splatting。
- 动态区域识别：通过光流运动发现，并利用 SAM2 进行时序一致的掩码传播。
- 背景补全：对选定关键帧，使用微调的扩散修复模型在遮挡区域生成合理的背景外观；随后用 Metric3D v2 从补全图像预测度量深度，以初始化“临时”高斯基元。
- 来源感知映射：为高斯基元添加来源标签，区分“生成基元”与“观测支持基元”；生成内容不参与相机位姿估计和观测地图优化。
- 遮挡解除处理：当先前被遮挡背景变为可见时，移除符合条件的生成基元，并由真实 RGB 观测与预测深度独立初始化观测支持基元。
- 实验概述：在 TUM RGB-D 上平均 ATE RMSE 为 1.2 cm，在 BONN RGB-D 上为 2.7 cm；在 StaDy4D 上仅用单目 RGB 输入，平均 PSNR 相比 WildGS-SLAM 提升 4.60 dB。

### 主要贡献
- 提出 DPGS-SLAM 单目 RGB SLAM 框架，支持对观测不足静态背景的临时表示。
- 引入异步扩散背景补全与来源感知高斯映射相结合的机制。
- 使用光流运动发现与 SAM2 时序一致掩码传播识别动态区域。
- 通过来源标签将生成内容排除在相机位姿估计与观测地图优化之外，并在背景变为可见时用真实观测独立初始化观测支持基元。
- 摘要报告了在 TUM RGB-D、BONN RGB-D 和 StaDy4D 上的竞争性跟踪与建图结果。

### 局限性
摘要未提供足够信息说明计算开销、实时性、扩散补全失败情形、对掩码/光流质量的敏感性、在更广泛数据集上的泛化性，以及生成基元与观测支持基元切换策略的详细失败模式。摘要未提供足够信息。

### 阅读优先级
高。理由：该论文直接针对 3DGS-SLAM 在动态场景中的静态假设失稳问题，提出“扩散补全 + 来源感知”的明确机制，并给出跟踪与渲染的定量结果；对动态视觉 SLAM、神经场景表示与稠密建图方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Dynamic observations can contaminate camera tracking and scene reconstruction in visual SLAM (simultaneous localization and mapping). Although 3DGS (3D Gaussian splatting) enables efficient dense mapping, existing 3DGS-SLAM systems may exhibit instability when dynamic objects violate their underlying static-scene assumption. Excluding dynamic observations can reduce their influence on tracking and mapping, but may leave occluded static backgrounds missing or weakly constrained. Our proposed DPGS-SLAM is a monocular RGB SLAM framework that supports provisional representations of insufficiently observed static backgrounds through asynchronous diffusion-based background completion and provenance-aware Gaussian mapping. Dynamic regions are identified through optical-flow-based motion discovery and temporally consistent mask propagation by SAM2 (segment anything model 2). For selected keyframes, a fine-tuned diffusion inpainting model generates plausible background appearance in occluded regions, while Metric3D v2 predicts metric depth from the completed images to initialize provisional Gaussian primitives. Provenance labels distinguish generated primitives from observation-supported primitives, excluding generated content from camera-pose estimation and observed-map optimization. When previously occluded backgrounds become visible, eligible generated primitives are removed, and observation-supported primitives are independently initialized from real RGB observations and predicted depth. Experimental results demonstrated competitive camera tracking, with average ATE RMSE values of 1.2 cm on TUM RGB-D and 2.7 cm on BONN RGB-D. On StaDy4D, DPGS-SLAM improved average PSNR by 4.60 dB over WildGS-SLAM using only monocular RGB input.

</details>

#### 2026-11-09 - HIST3R: Decomposing and Rectifying State Updates with History for Streaming 3D Reconstruction

**Authors:** Kenneth Yang, Yu-Chiang Frank Wang
**Links:** [abs](https://arxiv.org/abs/2611.12011) - [pdf](https://arxiv.org/pdf/2611.12011)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, camera pose estimation, pose estimation, depth estimation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HIST3R: Decomposing and Rectifying State Updates with History for Streaming 3D Reconstruction
- 作者：Kenneth Yang, Yu-Chiang Frank Wang
- 出版日期：2026-11-09T07:50:03Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.12011 ；PDF https://arxiv.org/pdf/2611.12011

### 一句话总结
HIST3R 是一个无需训练的流式 3D 重建框架，在 CUT3R 基础上利用历史状态同时校正循环状态更新的方向和幅度，以缓解长时序几何漂移。

### 研究问题
流式 3D 重建若用循环状态，可在有限内存下理解长视频场景，但每个新帧都会更新紧凑的场景记忆，后续预测均依赖该记忆。不可靠的更新会覆盖历史上下文，并累积成长时序几何漂移。摘要指出，现有 CUT3R 的无训练扩展只做幅度控制：能削弱不可靠更新，却不能修正其方向。

### 核心思路/方法
论文通过“方向—幅度”分解分析 CUT3R 式循环更新：幅度决定更新增益，即观测写入状态的强度；方向编码几何意图，即更新把状态推向何处。该分解统一了 CUT3R 及其变体，并揭示现有无训练扩展仅控制幅度。HIST3R 基于 CUT3R，是一个无需训练的框架，用历史同时控制这两个分量：利用局部一致的历史状态校正更新方向；根据当前观测与其历史之间的视觉差异调制更新幅度，抑制冗余更新并保留互补证据。

### 主要贡献
- 提出方向—幅度分解，用于分析 CUT3R 式循环状态更新，并指出已有无训练扩展仅进行幅度控制、无法校正方向。
- 提出无需训练的 HIST3R，利用历史状态同时校正更新方向与调制更新幅度。
- 摘要称在相机位姿估计、3D 重建和视频深度估计上持续提升长时序性能，同时保持 CUT3R 的内存占用和推理速度。
- 摘要报告：1000 帧输入时，相对最强对比方法，ScanNet 上 ATE 降低 23.87%，TUM-Dynamics 上降低 33.65%；500 帧时，相对最强 CUT3R 类变体，7-Scenes 上重建精度中位数提升 56.52%，NRGBD 上提升 33.96%。

### 局限性
摘要未提供足够信息说明局限性，例如失败场景、对历史质量或视觉差异度量的敏感性、计算开销细节及泛化边界等，均未在摘要中展开。摘要也未提供具体实验设置、数据集划分和消融细节。

### 阅读优先级
高。理由：该工作针对流式 3D 重建中循环状态更新的长时序漂移问题，提出清晰的分解视角和无需训练的改进方案，且摘要报告了多任务、多数据集上的量化提升；对关注流式重建、状态记忆更新和 CUT3R 系列方法的研究者有直接相关性。是否适合精读仍需结合全文实验细节判断，摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Streaming 3D reconstruction with recurrent states enables long-video scene understanding under bounded memory, but turns reconstruction into a state-evolution problem: each incoming frame updates a compact scene memory on which all subsequent predictions depend, so unreliable updates overwrite historical context and accumulate into long-horizon geometric drift. We analyze CUT3R-style recurrent updates through a direction--magnitude decomposition, in which the magnitude sets the update gain, i.e., how strongly an observation is written into the state, and the direction encodes the geometric intent, i.e., where the update drives the state. This decomposition provides a unified view of CUT3R and its variants, revealing that existing training-free extensions perform magnitude-only control: they can attenuate an unreliable update but cannot correct its direction. We propose HIST3R, a training-free framework built on CUT3R that controls both components using history. HIST3R rectifies the update direction using locally consistent historical states, and modulates the update magnitude according to the visual discrepancy between the current observation and its history, suppressing redundant updates while preserving complementary evidence. Across camera pose estimation, 3D reconstruction, and video depth estimation, HIST3R consistently improves long-horizon performance while retaining the memory footprint and inference speed of CUT3R. With 1000 input frames, it reduces ATE by 23.87% on ScanNet and 33.65% on TUM-Dynamics relative to the strongest competing method; with 500 frames, it improves median reconstruction accuracy over the strongest CUT3R-based variant by 56.52% on 7-Scenes and 33.96% on NRGBD.

</details>

#### 2026-11-09 - 3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model

**Authors:** Zixiang Ai, Zhenyu Cui, Xu Zou, Jiahuan Zhou
**Links:** [abs](https://arxiv.org/abs/2611.11964) - [pdf](https://arxiv.org/pdf/2611.11964)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model
- 作者：Zixiang Ai, Zhenyu Cui, Xu Zou, Jiahuan Zhou
- 出版日期：2026-11-09T06:33:18Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.11964 ；PDF https://arxiv.org/pdf/2611.11964

### 一句话总结
针对前馈三维重建模型在长尾场景下出现的跨视图对应失效问题，论文将其归因于“关系注意力结构坍塌”，并提出参数高效微调范式 3R-Adapter，通过可变形检索、关系重连与一致性精炼来恢复跨视图关系结构。

### 研究问题
前馈三维重建模型在大规模预训练下泛化较强，但在低光照重建、人体—场景联合重建、测试时适应等长尾场景中表现不佳。作者观察到关系注意力结构坍塌，表现为跨视图对应失败，并将其视为上述局限的主要原因。现有参数高效微调方法主要做通道级特征调整，缺乏显式适配关系结构的机制，因此无法解决对应失败问题。

### 核心思路/方法
论文将三维重建模型的适配形式化为域偏移下的对应关系恢复问题，提出 3R-Adapter，包含三个组件：
1. **Deformable Retrieval（可变形检索）**：面向任务自适应地检索关系候选；
2. **Relational Rewiring（关系重连）**：重建跨视图关系结构；
3. **Consistency Refinement（一致性精炼）**：将重连后的关系注入稳定预测中。

整体定位为面向长尾三维重建场景的参数高效微调范式，强调轻量、高效的适配。

### 主要贡献
- 指出关系注意力结构坍塌（表现为跨视图对应失败）是前馈三维重建模型在长尾场景中受限的主要原因。
- 将三维重建模型的适配问题表述为域偏移下的对应关系恢复问题。
- 提出 3R-Adapter 参数高效微调范式，由可变形检索、关系重连、一致性精炼三部分组成，显式适配关系结构而非仅做通道级特征调整。
- 摘要称在低光照重建、人体—场景联合重建和测试时适应上进行了大量实验，相比现有 PEFT 方法显著提升鲁棒性，同时保持高效轻量适配；并已开源代码。

### 局限性
- 摘要未提供足够信息说明具体数据集、基线配置、评价指标和数值结果。
- 摘要未提供足够信息说明各组件在不同任务上的消融贡献与相对增益。
- 摘要未提供足够信息说明计算开销、参数量、训练成本等“轻量高效”的量化证据。
- 摘要未提供足够信息说明方法在其他长尾场景或更广泛域偏移下的适用边界与失败情形。

### 阅读优先级
**中**。理由：论文聚焦三维重建模型的长尾适配与跨视图对应恢复，问题定位清晰，方法由三个明确组件构成，并覆盖低光照、人体—场景联合重建和测试时适应三类场景，对关注参数高效微调与三维重建鲁棒性的读者有参考价值；但当前仅有摘要与元数据，缺少实验细节与量化结果，需阅读全文后才能判断其实际效果与通用性。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D reconstruction models have demonstrated strong generalization under large-scale pre-training, yet they struggle in long-tail scenarios such as low-light reconstruction, joint human-scene reconstruction, and test-time adaptation. We observe relational attention structure collapse, manifested as the failure of cross-view correspondences, as a primary cause of these limitations. While adaptation offers a practical way to bridge this gap, existing parameter-efficient fine-tuning (PEFT) approaches mainly perform channel-wise feature adjustment and lack mechanisms to explicitly adapt relational structures, leaving correspondence failures unresolved. In this work, we formulate adaptation of 3D reconstruction models as a problem of correspondence recovery under domain shift and propose 3R-Adapter, a PEFT paradigm for long-tail 3D reconstruction scenarios. Our method consists of three components: Deformable Retrieval for task-adaptive relation candidate retrieval, Relational Rewiring for reconstructing cross-view relational structures, and Consistency Refinement for injecting the rewired relations into stable predictions. Extensive experiments on low-light reconstruction, joint human-scene reconstruction, and test-time adaptation demonstrate that our approach significantly improves robustness over existing PEFT methods while maintaining efficient lightweight adaptation. Our code is released at https://github.com/PKU-OV3-LAB/3R-Adapter.

</details>

#### 2026-11-09 - Scale-Consistent Monocular Fisheye Visual Odometry via Spherical Bundle Adjustment-Guided Unsupervised Depth Learning

**Authors:** Wanhui Luo, Hongbo Zhao, Yi Zhou, Qijun Chen, Yiming Nie, Rui Fan
**Links:** [abs](https://arxiv.org/abs/2611.11934) - [pdf](https://arxiv.org/pdf/2611.11934)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, bundle adjustment, depth estimation, view synthesis, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Scale-Consistent Monocular Fisheye Visual Odometry via Spherical Bundle Adjustment-Guided Unsupervised Depth Learning
- 作者：Wanhui Luo, Hongbo Zhao, Yi Zhou, Qijun Chen, Yiming Nie, Rui Fan
- 出版日期：2026-11-09T06:06:13Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.11934) / [PDF](https://arxiv.org/pdf/2611.11934)

### 一句话总结
该论文提出 S²D-FVO，一个将球面光束法平差（SBA）引导的无监督深度学习与单目鱼眼视觉里程计相结合的框架，旨在提升长轨迹下的尺度一致性与深度估计精度。

### 研究问题
单目鱼眼视觉里程计因宽视场和单目配置简单而具有吸引力，但长轨迹中的尺度漂移仍是主要挑战。无监督深度学习可缓解该问题，然而鱼眼图像的显著畸变给准确深度估计带来困难。论文关注如何在鱼眼畸变条件下改善尺度一致性和深度估计精度。

### 核心思路/方法
论文提出 S²D-FVO 框架，核心包括：
- 指出像素重投影残差不能均匀反映视线方向间的角度偏差，且标量角度重投影残差的一阶线性化对某一切线方向上的扰动不敏感。
- SBA 采用由球面对数映射导出的切空间角度重投影残差，该残差在两个切线方向上均保留敏感性，且其范数等于对应的标量角度残差。
- 在 SBA 中进一步引入基于中值深度的尺度正则项以约束重建尺度。
- 在无监督深度学习中，用 SBA 替代位姿估计网络，为视图合成提供更可靠的相对位姿；反过来，训练良好的深度估计网络为 SBA 提供尺度参考，提升尺度一致性并允许细化单个三维路标位置。

### 主要贡献
- 提出 S²D-FVO 单目鱼眼 VO 框架，将 SBA 引导的无监督深度学习集成其中，以改善尺度一致性和深度估计精度。
- 设计基于球面对数映射的切空间角度重投影残差，使残差在两个切线方向上均保持敏感性，且范数与标量角度残差一致。
- 在 SBA 中引入中值深度尺度正则项约束重建尺度。
- 用 SBA 替代无监督深度学习中的位姿估计网络，并形成深度网络与 SBA 之间的尺度参考交互。
- 摘要称在多个公开数据集及两个新采集的大规模数据集上进行了实验，结果表明该框架在深度和轨迹估计精度上优于代表性现有方法，且适用于不同相机模型。

### 局限性
- 摘要未提供足够信息说明计算复杂度、实时性表现。
- 摘要未提供足够信息说明对极端畸变、动态场景或低纹理环境的鲁棒性。
- 摘要未提供足够信息说明新采集数据集的具体规模、场景类型和采集条件。
- 摘要未提供足够信息说明各模块的消融实验细节及失败案例。

### 阅读优先级
中。理由：该论文聚焦鱼眼单目 VO 的尺度漂移与畸变下深度估计问题，方法上涉及 SBA 残差设计与无监督深度学习的耦合，对 3D 重建与多视图几何方向有参考价值；但摘要未给出定量结果和实时性信息，是否优先精读取决于读者对鱼眼 VO 或无监督深度估计的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

The wide field of view of fisheye cameras and the simplicity of a monocular setup make monocular fisheye visual odometry (VO) attractive for robotic localization and mapping. Nevertheless, scale drift remains a major challenge over long trajectories. Unsupervised depth learning can help to mitigate this issue, but the pronounced distortion of fisheye images poses challenges for accurate depth estimation. This article presents S$^2$D-FVO, a monocular fisheye VO framework integrating spherical bundle adjustment (SBA)-guided unsupervised depth learning to improve scale consistency and depth estimation accuracy. Given that pixel reprojection residuals do not uniformly reflect angular deviations between viewing rays and that the first-order linearization of a scalar angular reprojection residual is insensitive to perturbations along one tangent direction, SBA employs tangent-space angular reprojection residuals derived from the spherical logarithmic map. These residuals retain sensitivity along both tangent directions, with their norms equal to the corresponding scalar angular residuals. A median depth-based scale regularization term is further integrated into SBA to constrain the reconstruction scale. Building on these formulations, SBA replaces the pose estimation network during unsupervised depth learning, providing more reliable relative poses for view synthesis. In turn, depth estimates from the well-trained depth estimation network provide scale references for SBA, improving scale consistency while allowing individual 3-D landmark positions to be refined. Extensive experiments conducted on multiple public datasets, as well as two newly collected large-scale datasets, demonstrate that the proposed framework outperforms representative existing approaches in both depth and trajectory estimation accuracy and is applicable to different camera models.

</details>

#### 2026-11-09 - Budget-aware Correspondence-driven View Selection for Real-time 3D Perception of Mobile Robots

**Authors:** Vaishnav Ramesh, Jacob Carter, Shivali J. Patel, Sanjeev J. Koppal, Md Jahidul Islam
**Links:** [abs](https://arxiv.org/abs/2611.11809) - [pdf](https://arxiv.org/pdf/2611.11809)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, structure from motion, SfM, camera pose estimation, pose estimation, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Budget-aware Correspondence-driven View Selection for Real-time 3D Perception of Mobile Robots
- 作者：Vaishnav Ramesh, Jacob Carter, Shivali J. Patel, Sanjeev J. Koppal, Md Jahidul Islam
- 出版日期：2026-11-09T03:13:15Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.11809) / [PDF](https://arxiv.org/pdf/2611.11809)

### 一句话总结
该论文提出 BCVS（budget-aware correspondence-driven view sampling），一种无需相机位姿、基于对应关系打分的视角选择算法，用于在用户给定预算下在线过滤冗余图像，以支持移动机器人的实时 3D 感知。

### 研究问题
面向自主机器人与智能交通的真实部署中，长且冗余的图像序列会妨碍下游处理；论文关注如何在给定预算下高效选择视角，同时避免依赖完整 SfM 流程或相机位姿估计，并保持几何稳定性所需的视图重叠与重建质量。

### 核心思路/方法
BCVS 是一种无位姿（pose-free）的视角选择算法：
- 采用纯对应关系（correspondence-based）打分策略，优先选择视图新颖性，同时保持足够重叠以维持几何稳定性；
- 给定用户指定预算，迭代选择最具区分度的帧并抑制近重复帧，生成紧凑子集；
- 目标是在保持连通性的同时最小化重建损失；
- 摘要称其在 CPU 上可达 22+ FPS，支持移动机器人的在线过滤。

### 主要贡献
- 提出 BCVS：不依赖完整 SfM 管线或相机位姿估计的预算感知视角采样方法；
- 在基准实验中，BCVS 在紧预算下优于 CPU 友好的基线方法，并随预算扩大保持竞争力；
- 通过大型航空与海洋机器人数据的现场试验验证其实用性与可扩展性：冗余降低最多 16%，同时维持稳健的 SfM 配准与高质量 3D 重建。

### 局限性
摘要未提供足够信息。摘要未给出具体基准数据集名称、对比基线细节、失败场景、计算资源具体配置、冗余降低指标的完整定义，以及方法在极端低预算或高动态场景下的表现。

### 阅读优先级
中。理由：该工作与移动机器人实时 3D 感知、视角选择及减少冗余图像序列直接相关，且强调 CPU 实时性与无位姿设计，具有工程实用价值；但摘要未提供充分实验细节与失败场景分析，需阅读全文进一步判断其通用性与可复现性。

</details>

<details>
<summary>Abstract</summary>

3D visual perception and scene reconstruction are critical for autonomous robots and intelligent transportation, yet real-world deployments often generate long, redundant image sequences that hinder downstream processing. This report investigates BCVS (budget-aware correspondence-driven view sampling), a pose-free view selection algorithm that offers 22+ FPS on a CPU, enabling online filtering for efficient 3D perception by mobile robots. Unlike existing approaches that rely on full structure-from-motion (SfM) pipelines or camera pose estimation, BCVS employs a purely correspondence-based scoring strategy that prioritizes view novelty while maintaining sufficient overlap for geometric stability. Given a user-specified budget, BCVS iteratively selects the most distinct frames and suppresses near-duplicates, producing compact subsets that preserve connectivity and minimize reconstruction loss. Extensive experiments on benchmark show that BCVS outperforms CPU-friendly baselines at tight budgets and remains competitive as budgets scale. Field trials with large aerial and marine robotics data further validate its practicality and scalability: BCVS reduces redundancy up to 16% while sustaining robust SfM registration and high-quality 3D reconstructions.

</details>

#### 2026-11-09 - Towards Rotation-Only Imaging Geometry: Multi-View Pose Estimation

**Authors:** Xinrui Li, Qi Cai, Yuanxin Wu
**Links:** [abs](https://arxiv.org/abs/2611.11770) - [pdf](https://arxiv.org/pdf/2611.11770)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Rotation-Only Imaging Geometry: Multi-View Pose Estimation
- 作者：Xinrui Li, Qi Cai, Yuanxin Wu
- 出版日期：2026-11-09T02:22:33Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次级分类
- 链接：[摘要](https://arxiv.org/abs/2611.11770) / [PDF](https://arxiv.org/pdf/2611.11770)

### 一句话总结
论文提出 GRAM 方法，直接从初始相对旋转和内点匹配中估计全局旋转，并进一步提出 MORE 与 ART，用于多视图仅旋转的全局旋转优化和全局平移恢复。

### 研究问题
全球结构从运动（global SfM）通常在单个图像对上细化相对位姿，再通过旋转平均估计全局旋转。作者指出，成对细化在旋转初始化过程中没有显式地将特征级约束与多视图一致性结合起来。因此，论文关注如何更直接地利用初始相对旋转和内点匹配来估计全局旋转，以及如何将仅旋转的成像几何扩展到多视图。

### 核心思路/方法
- 提出 GRAM（Global Rotations from Aggregated Matches）：通过最小化逐边的仅旋转代数残差，直接从初始相对旋转和内点匹配估计全局旋转，将两视图相对位姿优化和旋转平均替换为单一阶段。
- 进一步将仅旋转成像几何扩展到多视图，提出 MORE（Multi-view Optimization with Rotation-only Reprojection Error），用于非线性全局旋转细化。
- 提出 ART（Analytical Rotation-guided Translation）：从 LiGT（Linear Global Translation）约束推导局部尺度的三视图平移，并使用加权最小二乘恢复全局平移。

### 主要贡献
- 将两视图相对位姿优化与旋转平均合并为一个阶段，提出直接由初始相对旋转和内点匹配估计全局旋转的 GRAM。
- 将仅旋转成像几何扩展到多视图，并提出用于非线性全局旋转细化的 MORE。
- 提出 ART，从 LiGT 约束推导局部尺度三视图平移，并通过加权最小二乘恢复全局平移。
- 摘要称合成与真实世界实验展示了所提方法的精度、鲁棒性和效率；具体实验设置与数值结果摘要未提供足够信息。

### 局限性
摘要未提供足够信息，因此无法基于摘要确定具体局限性，例如方法对退化配置、噪声或尺度处理的敏感性，以及实验覆盖范围和失败情形等。

### 阅读优先级
中。理由：该论文面向 global SfM 中旋转初始化与多视图一致性结合的问题，提出将相对位姿优化与旋转平均合并的方法，问题定位清晰；但摘要未给出具体实验数值、对比基线细节和失败情形，是否值得优先精读需结合全文实验结果进一步判断。

</details>

<details>
<summary>Abstract</summary>

Global structure-from-motion (SfM) commonly refines relative poses on individual image pairs and then estimates global rotations by rotation averaging. Pairwise refinement does not explicitly combine feature-level constraints with multi-view consistency during rotation initialization. We introduce Global Rotations from Aggregated Matches (GRAM), which estimates global rotations directly from initial relative rotations and inlier matches by minimizing edge-wise rotation-only algebraic residuals. GRAM replaces two-view relative-pose optimization and rotation averaging with a single stage. We further extend rotation- only imaging geometry to multiple views and develop Multi-view Optimization with Rotation-only Reprojection Error (MORE) for nonlinear global rotation refinement. Analytical Rotation-guided Translation (ART) derives locally scaled triplet translations from Linear Global Translation (LiGT) constraints and recovers global translations using weighted least squares. Synthetic and real-world experiments demonstrate the accuracy, robustness, and efficiency of the proposed methods.

</details>

#### 2026-11-09 - LangDepth: Vision-Language Scene Priors for Semantic Binning and Cross-Domain Monocular Depth Estimation

**Authors:** Reyhaneh Ahani Manghotay, Jie Liang
**Links:** [abs](https://arxiv.org/abs/2611.11763) - [pdf](https://arxiv.org/pdf/2611.11763)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LangDepth: Vision-Language Scene Priors for Semantic Binning and Cross-Domain Monocular Depth Estimation
- 作者：Reyhaneh Ahani Manghotay, Jie Liang
- 出版日期：2026-11-09T02:04:23Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.11763 ；PDF https://arxiv.org/pdf/2611.11763

### 一句话总结
LangDepth（SemanticBins）利用冻结 CLIP 编码器与可学习场景/几何概念键生成紧凑场景描述子，经场景先验模块（SPM）给出场景条件化的度量深度区间锚点，并与 DINOv2-L 稠密特征及逐像素分配网络（PPAN）和置信门融合，实现跨域单目深度估计。

### 研究问题
单目度量深度对场景级尺度敏感：室内房间与室外驾驶场景的深度范围差异很大，但多数深度解码器仅从视觉特征中隐式推断这种全局结构。论文追问：场景级语义结构能否作为上游先验，在稠密预测之前塑造度量输出空间。

### 核心思路/方法
- 用冻结 CLIP 编码器和可学习的、面向场景与几何的概念键库，将图像特征转换为紧凑场景描述子，无需逐图像文本或外部 captioner。
- 场景先验模块（SPM）将该描述子映射为场景条件化的度量深度区间，在稠密解码前提供全局范围锚点。
- 并行使用 DINOv2-L 骨干与轻量 FPN 提取稠密视觉特征，并由逐像素分配网络（PPAN）将像素分配到场景规定的 bin 结构。
- 置信门融合稠密视觉估计与 SPM 先验。
- 在 NYU Depth V2 与 KITTI 上联合训练，采用适度的监督深度预算，不使用网络规模深度监督或伪标签深度数据。

### 主要贡献
- 提出以场景条件化输出空间为核心的单目深度架构，将场景级语义结构作为上游先验而非仅靠视觉特征隐式推断全局尺度。
- 设计无需逐图像文本/外部 captioner 的场景描述子构建方式，并通过 SPM 提供场景条件化度量深度区间锚点。
- 结合 DINOv2-L/FPN 稠密特征、PPAN 像素分配与置信门融合，形成统一框架。
- 摘要报告单一模型在 NYU 上 delta_1 = 0.960、KITTI 0.960、DIODE indoor 0.887、iBims-1 0.946、SUN RGB-D 0.861；并报告 SPM 预测紧凑室内范围与更宽 KITTI 范围、门在室外场景偏向 SPM、扰动路由场景上下文导致 KITTI 与 iBims-1 大幅下降等可解释性观察。

### 局限性
摘要未提供足够信息（未说明失败案例、计算开销、对场景分类错误的敏感性边界、训练数据规模细节及跨域泛化的系统限制等）。

### 阅读优先级
高。理由：摘要明确给出跨多个室内/室外数据集的单一模型精度指标与可解释性分析，且方法核心“场景条件化输出空间”对跨域单目度量深度具有直接研究价值；但需注意仅依据摘要，实验细节与局限性未展开。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation has advanced through large-scale pretraining and strong visual backbones, yet metric depth remains sensitive to scene-level scale. Indoor rooms and outdoor driving scenes occupy very different depth ranges, but most depth decoders infer this global structure implicitly from visual features. We ask whether scene-level semantic structure can instead act as an upstream prior that shapes the metric output space before dense prediction. We present LangDepth (SemanticBins), a monocular depth architecture that couples strong visual features with a scene-conditioned output space. A frozen CLIP encoder and a learnable bank of scene- and geometry-oriented concept keys convert image features into a compact scene descriptor, without requiring per-image text or an external captioner. A Scene Prior Module (SPM) maps this descriptor to a scene-conditioned metric depth interval, providing a global range anchor before dense decoding. In parallel, a DINOv2-L backbone with a lightweight FPN extracts dense visual features, and a Per-Pixel Assignment Network (PPAN) assigns pixels to the scene-prescribed bin structure. A confidence gate fuses the dense visual estimate with the SPM prior. We train LangDepth jointly on NYU Depth V2 and KITTI under a modest supervised depth budget, without web-scale depth supervision or pseudo-labelled depth data. A single model achieves delta_1 = 0.960 on NYU, 0.960 on KITTI, 0.887 on DIODE indoor, 0.946 on iBims-1, and 0.861 on SUN RGB-D. Beyond aggregate accuracy, the SPM predicts compact indoor ranges and much wider outdoor KITTI ranges, the gate becomes SPM-dominant on outdoor scenes, and perturbing the routed scene context causes large drops on KITTI and iBims-1. These results support scene-conditioned output spaces as a practical and interpretable mechanism for cross-domain monocular depth estimation.

</details>

#### 2026-11-08 - Martine: Benchmarking Multi-View 3D Surface Reconstruction Across Viewpoint Coverage, Resolution, and Lighting

**Authors:** Robin Bruneau, Baptiste Brument, Frederic Giraud, Bastian Sigrist, Sascha Jecklin, Philipp Fürnstahl, Bjoern Menze, Lilian Calvet
**Links:** [abs](https://arxiv.org/abs/2611.11602) - [pdf](https://arxiv.org/pdf/2611.11602)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** multi-view stereo, surface reconstruction, photogrammetry, camera calibration, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Martine: Benchmarking Multi-View 3D Surface Reconstruction Across Viewpoint Coverage, Resolution, and Lighting
- 作者：Robin Bruneau, Baptiste Brument, Frederic Giraud, Bastian Sigrist, Sascha Jecklin, Philipp Fürnstahl, Bjoern Menze, Lilian Calvet
- 出版日期：2026-11-08T20:32:04Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Neural Scene Representations & Rendering
- 链接：[Abstract](https://arxiv.org/abs/2611.11602) / [PDF](https://arxiv.org/pdf/2611.11602)

### 一句话总结
论文提出 Martine，一个面向受控多视角 3D 物体表面重建的基准，覆盖视角分布、分辨率与光照条件，并提供精确 3D 真值和量化对齐信息，以支持按采集条件与物体属性分析重建误差。

### 研究问题
摘要指出，多视角 3D 表面重建的基准评测存在困难：重建精度同时取决于重建范式、物体属性和采集条件；现有基准常限制视角覆盖、分辨率或光照，可能使比较偏向适合特定设置的方法；部分基准缺乏准确 3D 真值或量化的图像到几何对齐，限制其用于度量表面评估。Martine 旨在解决受控条件下跨采集条件的表面重建基准评测问题。

### 核心思路/方法
Martine 是一个受控 3D 物体表面重建基准。其数据包含 28 个物体，涵盖透明材料和精细结构；以 9568 x 6376 像素、84 个视角在球冠范围采集，并覆盖单光源和多光源两种条件。基准提供与物体无关的相机标定、准确 3D 真值扫描、在测试图像上量化的标定与图像到几何精度，以及用于按材料属性、可见性、曲率和精细结构分析误差的 3D 属性掩码。摘要还说明其实验覆盖摄影测量、经典多视角立体、神经隐式表面、基于 Gaussian-splatting 的重建以及多视角光度立体，并支持对参考数据精度进行显式控制的采集条件感知评估。

### 主要贡献
- 提出 Martine 基准，用于受控多视角 3D 物体表面重建评测，覆盖视角分布、分辨率和光照条件。
- 构建包含 28 个物体（含透明材料和精细结构）的数据集，采集分辨率为 9568 x 6376，84 个视角分布于球冠范围，并包含单光源与多光源条件。
- 提供与物体无关的相机标定、准确 3D 真值扫描，以及在测试图像上量化的标定和图像到几何精度。
- 提供 3D 属性掩码，支持按材料属性、可见性、曲率和精细结构分析重建误差。
- 实验覆盖多种重建范式，并报告可在评估可见表面上分辨亚毫米级重建差异，最佳观测 Chamfer 距离为 0.058 mm。

### 局限性
摘要未提供足够信息说明该基准在物体类别覆盖范围、采集成本、泛化到非受控场景的能力、不同重建范式的计算资源需求等方面的局限；也未提供足够信息说明其评测协议在不同任务间的可迁移性。

### 阅读优先级
高。理由：该论文直接面向多视角 3D 表面重建的基准评测问题，明确针对现有基准在视角覆盖、分辨率、光照、3D 真值和图像到几何对齐方面的不足；摘要显示其数据规模、采集条件和评测维度较完整，并覆盖多类重建方法，对关注 3D 重建评测严谨性和受控采集条件影响的研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Controlled acquisition setups are widely used for high-accuracy multi-view 3D surface reconstruction, as they allow sensor configuration, image resolution, viewpoint distribution, and illumination to be specified. Yet benchmarking remains difficult, since reconstruction accuracy depends jointly on the reconstruction paradigm, object properties, and acquisition regime. Existing benchmarks often restrict viewpoint coverage, resolution, or illumination, which can bias comparisons towards methods suited to the chosen setting. Others lack accurate 3D ground truth or quantified image-to-geometry alignment, limiting their use for metric surface evaluation. We introduce Martine, a benchmark for controlled 3D object surface reconstruction. Martine comprises 28 objects, including transparent materials and fine structures, captured at 9568 x 6376 pixels from 84 views over a spherical cap under both single-light and multi-light regimes. It provides object-independent camera calibration, accurate 3D ground-truth scans, calibration and image-to-geometry accuracy quantified on test images, and 3D property masks for analysing errors by material properties, visibility, curvature and fine structures. Experiments across photogrammetry, classical multi-view stereo, neural implicit surfaces, Gaussian-splatting-based reconstruction, and multi-view photometric stereo show that Martine enables regime-aware evaluation with explicit control over reference-data accuracy. The benchmark resolves sub-millimetric reconstruction differences, with a best observed Chamfer distance of 0.058 mm over the evaluated visible surface.

</details>

#### 2026-11-08 - TransArt3D: From Two States to Articulated 3D Reconstruction with Video Transition Priors

**Authors:** Chenhao Guan, Liying Yang, Xinxing Yu, Hao Mo, Tianshun Han, Renjun Gao, Yanyan Liang
**Links:** [abs](https://arxiv.org/abs/2611.11304) - [pdf](https://arxiv.org/pdf/2611.11304)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, robotics, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TransArt3D: From Two States to Articulated 3D Reconstruction with Video Transition Priors
- 作者：Chenhao Guan, Liying Yang, Xinxing Yu, Hao Mo, Tianshun Han, Renjun Gao, Yanyan Liang
- 出版日期：2026-11-08T11:03:36Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.11304 ；PDF https://arxiv.org/pdf/2611.11304

### 一句话总结
TransArt3D 是一个基于优化的框架，利用视频扩散模型隐含的“状态间运动先验”，从两张端点图像重建带关节的 3D 资产，并显式恢复部件结构与关节运动学。

### 研究问题
从少量图像重建可交互的带关节 3D 资产对机器人与仿真很重要，但问题高度欠约束。现有基于优化的方法在静态 3D 先验下独立评估每个状态，导致逐状态重建误差泄漏到运动部件与关节估计中，形成虚假运动。视频扩散模型能捕捉物体在状态间的运动，但这种信息仅以 2D 方式隐含存在。论文要解决的是：如何把这种视频过渡先验转化为显式的部件结构与关节运动学，从而在仅给定两个端点状态时稳定地重建带关节 3D 资产。

### 核心思路/方法
- 输入为两个端点图像，目标是重建带关节的 3D 资产及其部件与关节参数。
- 首先用“过渡耦合的 3D 一致性”提升端点之间生成的帧：将静态 3D 先验跨帧联合应用，以稳定不变区域，并初始化部件与关节。
- 随后采用 rectified-flow 运动学细化：让视频先验监督整个过渡上的 3D 运动场，同时通过部件分配与共享关节在优化全程约束该运动场，避免逐状态误差进入关节估计。
- 最后使用运动感知的规范外观融合：利用恢复的关节关系将两张端点图像映射到同一规范表面，从而为仅由一个状态显露的区域贴图。

### 主要贡献
- 提出 TransArt3D，一个基于优化的框架，将视频过渡先验转化为显式的部件结构与关节运动学，用于从两个端点图像重建带关节 3D 资产。
- 引入过渡耦合的 3D 一致性，将静态 3D 先验跨帧联合应用，以稳定不变区域并初始化部件与关节。
- 引入 rectified-flow 运动学细化，使视频先验监督 3D 运动场，并通过部件分配与共享关节约束优化。
- 引入运动感知的规范外观融合，将两个端点图像映射到同一规范表面，补全仅单状态可见区域的纹理。
- 摘要称在 PartNet-Mobility 上，TransArt3D 在几何与关节精度上优于使用相同两个端点的方法，并在带关节状态几何、关节定位与外观上超过使用六个观测状态的方法。

### 局限性
- 摘要未提供足够信息说明方法对端点图像质量、视角变化或物体类别的具体敏感性与失败情形。
- 摘要未提供足够信息说明计算开销、优化时间或对视频扩散模型生成质量的依赖程度。
- 摘要未提供足够信息说明在 PartNet-Mobility 之外的泛化能力。
- 摘要未提供足够信息说明关节类型、部件数量或拓扑复杂度的适用范围。
- 摘要未提供足够信息说明与使用更多观测状态方法比较时的具体实验设置与公平性细节。

### 阅读优先级
中。理由：论文问题定义清晰，针对“两个端点图像重建带关节 3D 资产”这一欠约束任务提出将视频过渡先验显式化的思路，且摘要给出了在 PartNet-Mobility 上的比较结论；但摘要未提供足够信息判断方法细节、失败模式与泛化性。若关注机器人/仿真中的可交互资产生成、视频先验用于 3D 重建或关节物体建模，优先级可上调；否则建议先阅读摘要与实验部分再决定。

</details>

<details>
<summary>Abstract</summary>

Reconstructing interactable articulated assets from a few images is key to robotics and simulation, yet highly underconstrained. Existing optimization-based methods fit an articulated asset under a static 3D prior that scores each state independently, so per-state reconstruction errors leak into the estimated moving part and joint as false motion. Video diffusion models capture how objects move between states, but only implicitly in 2D. To this end, we present TransArt3D, an optimization-based framework that reconstructs an articulated 3D asset from two endpoint images by translating this video transition prior into explicit part structure and joint kinematics. It first lifts frames generated between the endpoints with a transition-coupled 3D consensus that applies the static 3D prior jointly across frames, stabilizing unchanging regions and initializing the parts and joint. A rectified-flow kinematic refinement then lets the video prior supervise a 3D motion field over the whole transition, while part assignment and a shared joint constrain the field throughout optimization, keeping per-state errors out of the articulation. Finally, a motion-aware canonical appearance fusion uses the recovered articulation to map both endpoint images onto one canonical surface, texturing regions that only one state reveals. On PartNet-Mobility, TransArt3D outperforms methods given the same two endpoints in geometry and joint accuracy, and surpasses methods given six observed states in articulated-state geometry, joint localization and appearance.

</details>

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-10 - A Lightweight Differentiable Method for Real-Time Skin Rendering and Digitization

**Authors:** Mario Marquez-Balduque, Carlos Rodriguez-Pardo, Jorge Lopez-Moreno
**Links:** [abs](https://arxiv.org/abs/2611.14451) - [pdf](https://arxiv.org/pdf/2611.14451)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Lightweight Differentiable Method for Real-Time Skin Rendering and Digitization
- 作者：Mario Marquez-Balduque, Carlos Rodriguez-Pardo, Jorge Lopez-Moreno
- 出版日期：2026-11-10T18:20:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2611.14451

### 一句话总结
该论文提出一种轻量级可微屏幕空间次表面散射框架，直接估计适用于实时渲染管线的皮肤散射参数，并通过单光单视角采集实现皮肤外观数字化。

### 研究问题
传统皮肤逆渲染通常依赖离线路径追踪来估计物理属性，但这些属性无法直接映射到游戏引擎等交互应用中使用的近似着色器。论文试图弥合离线逆渲染与实时渲染管线之间的差距，直接估计面向实时渲染的次表面散射参数。

### 核心思路/方法
论文引入可微屏幕空间次表面散射（SSSS）框架，能够联合优化空间变化的基础纹理和散射距离。为考虑皮肤厚度的局部变化，方法在不同面部区域分别估计这些参数，并生成可用于生产运行时引擎的混合 profile map。采集方面采用低成本、单光源、单视角的设置，以提升外观获取的可及性和实用性。优化由掩码损失函数驱动，聚焦于次表面散射效应占主导的区域。

### 主要贡献
- 提出可微屏幕空间次表面散射框架，支持基础纹理与散射距离的联合优化。
- 针对面部不同区域估计散射参数，生成可直接用于实时引擎的混合 profile map。
- 设计低成本单光单视角采集流程，面向实际外观获取。
- 使用覆盖 Monk Skin Tone Scale 的 45 人真实数据集进行验证，并补充合成数据、多光源设置和倾斜视角配置的实验。
- 结果表明方法能从轻量输入中有效恢复散射参数，并生成与标准实时着色器直接兼容的真实感皮肤外观。

### 局限性
摘要未提供足够信息。摘要未说明方法在极端光照、不同设备或更广泛人群上的泛化能力，也未给出计算开销、实时性能数值或失败案例的具体信息。

### 阅读优先级
中。理由：该工作面向实时皮肤渲染与轻量采集，问题定义清晰，且与实时渲染管线直接对接，对图形学与皮肤渲染方向有实用价值；但摘要未提供定量性能、对比基线细节和局限性分析，需阅读全文后才能判断其技术深度与泛化性。

</details>

<details>
<summary>Abstract</summary>

Inverse rendering for skin typically relies on offline path tracing to estimate physical properties, which fail to map directly to the approximate shaders utilized in interactive applications, such as game engines. We bridge this gap by directly estimating subsurface scattering parameters tailored for real-time rendering pipelines. We introduce a differentiable Screen-Space Subsurface Scattering (SSSS) framework that enables the joint optimization of spatially varying base textures and scattering distances. To account for local variations in skin thickness, we estimate these parameters across distinct facial regions, generating a blended profile map ready for production runtime engines. Our pipeline utilizes a low-cost, single-light, single-view capture setup designed for accessible and practical appearance acquisition. Optimization is driven by a masked loss function targeting regions where subsurface scattering effects are dominant. We validate our approach on a real-world dataset of $45$ individuals across the Monk Skin Tone Scale, ensuring demographic generalization. Furthermore, we complement this evaluation with synthetic data, a multi-light setup validating our single-light assumption, and a tilted-view configuration confirming angular consistency. Results demonstrate that our method effectively recovers scattering parameters from lightweight inputs, yielding realistic skin appearance directly compatible with standard real-time shaders.

</details>

#### 2026-11-10 - FastWild-GS: Minutes-Scale In-the-Wild Gaussian Splatting via Compact Per-Image Appearance Adaptation

**Authors:** Donghun Ryu, Seokhyun Kim, Minhyeok Lee
**Links:** [abs](https://arxiv.org/abs/2611.13808) - [pdf](https://arxiv.org/pdf/2611.13808)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FastWild-GS: Minutes-Scale In-the-Wild Gaussian Splatting via Compact Per-Image Appearance Adaptation
- 作者：Donghun Ryu, Seokhyun Kim, Minhyeok Lee
- 出版日期：2026-11-10T09:39:33Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.13808) | [PDF](https://arxiv.org/pdf/2611.13808)

### 一句话总结
FastWild-GS 用紧凑的每图像外观建模（128 维 Photo Appearance Token 加六参数逐通道变换，并由小型 MLP 预测高斯颜色）来处理野外照片间的曝光、光照与瞬态物体差异，在 PhotoTourism 上每场景训练 8.8 分钟，并在所比较方法中取得最低 LPIPS。

### 研究问题
野外（in-the-wild）场景的互联网照片在曝光、光照和瞬态物体（如路人）上存在差异，因此单一组高斯颜色无法解释全部照片；近期的野外高斯 Splatting 方法大多需要每场景数小时的优化。论文关注的是如何在保持重建质量的同时，显著缩短这种野外场景的优化时间。

### 核心思路/方法
- 为每张照片引入一个 128 维的 Photo Appearance Token，以及一个应用于渲染图像的逐通道变换（scale 与 offset），共六个参数。
- 用一个小型 MLP 结合该 Token 与每个高斯自身的 feature，预测每个高斯的颜色，替代球谐函数颜色表示。
- 在用于致密化与剪枝评分的高斯渲染结果上，同样施加该变换，从而避免把照片之间的外观差异误算为重建误差。

### 主要贡献
- 提出 FastWild-GS，一种分钟级（minutes-scale）的野外高斯 Splatting 方法，通过紧凑的每图像外观自适应建模照片间的曝光、光照与瞬态差异。
- 将外观变换一致地用于渲染与致密化、剪枝评分，以减少外观差异被误判为重建误差。
- 在 PhotoTourism 上每场景训练 8.8 分钟，在所比较方法中 LPIPS 最低，比 LPIPS 次优的 AsymGS 快 23 倍。
- 在 NeRF-OSR 上每场景 9.7 分钟，在所比较方法中取得最佳平均 PSNR、SSIM 和 LPIPS。

### 局限性
摘要未提供足够信息。摘要未说明方法在极端外观变化、动态物体密集场景下的表现，也未给出内存占用、参数量开销或失败案例等细节。

### 阅读优先级
中。理由：论文聚焦野外高斯 Splatting 的训练效率，报告了明确的加速比（相对 AsymGS 快 23 倍）与多项指标优势，对关注三维重建/新视角合成效率的读者有参考价值；但摘要未提供消融、局限与实现细节，需阅读全文才能判断方法稳健性与适用范围。

</details>

<details>
<summary>Abstract</summary>

Internet photos of a scene differ in exposure, illumination and transient objects such as passers-by, so one set of Gaussian colours cannot explain all photos (the in-the-wild setting). Recent in-the-wild Gaussian Splatting methods mostly report hours of per-scene optimization. We present FastWild-GS, which describes each photo by a 128-dimensional Photo Appearance Token and a per-channel transform, a scale and an offset applied to the rendered image (six parameters); a small MLP predicts the colour of each Gaussian from this token and a per-Gaussian feature, replacing the spherical-harmonics colour. The same transform is applied to the renders that score Gaussians for densification and pruning, so appearance differences between photos are not counted as reconstruction error. On PhotoTourism, FastWild-GS trains in 8.8 minutes per scene with the lowest LPIPS among the compared methods, 23x faster than AsymGS, the next best in LPIPS. On NeRF-OSR, it has the best average PSNR, SSIM and LPIPS among the compared methods in 9.7 minutes per scene.

</details>

#### 2026-11-10 - Marrying Capacity and Precision for Efficient 2D Gaussian Image Representation

**Authors:** Lin Dong, Qi Ming, Liuqian Wang, Wentao Chao, Yufei Gao, Chengming Liu, Lei Shi
**Links:** [abs](https://arxiv.org/abs/2611.13784) - [pdf](https://arxiv.org/pdf/2611.13784)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Marrying Capacity and Precision for Efficient 2D Gaussian Image Representation
- 作者：Lin Dong, Qi Ming, Liuqian Wang, Wentao Chao, Yufei Gao, Chengming Liu, Lei Shi
- 出版日期：2026-11-10T09:21:35Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.13784) / [PDF](https://arxiv.org/pdf/2611.13784)

### 一句话总结
提出 CP-GS，在统一码率约束下联合优化 2D 高斯表示的数量（容量）与参数精度，以提升有限预算下的率失真性能。

### 研究问题
2D 高斯表示在有限预算下的率失真性能，关键取决于高斯容量与参数精度如何分配；现有方法通常分别优化这两类资源，忽略了内容相关的高斯容量需求和不同参数对量化的敏感度差异。

### 核心思路/方法
CP-GS 是一个容量—精度耦合的高斯泼溅框架，面向预算感知的 2D 高斯图像表示，在共享码率约束下联合优化容量分配与属性精度。方法包括三部分：
1. 构建内容自适应高斯表示，将固定的高斯预算从冗余区域动态重新分配到表示需求更高的区域；
2. 引入分层失真感知表示量化，通过高效的基于渲染的校准，在不同高斯属性间分配精度，并在异构属性组内进一步细化；
3. 联合优化高斯容量与属性精度：构造不同高斯数量与精度配置的候选表示，依据解码失真与实际序列化大小选择工作点。

### 主要贡献
- 提出容量与精度耦合的 2D 高斯图像表示框架 CP-GS，在共享码率约束下联合优化容量分配与属性精度。
- 设计内容自适应的高斯预算重分配机制，以应对内容相关的高斯容量需求。
- 引入分层失真感知量化与基于渲染的校准，处理异构量化敏感度。
- 通过候选表示选择实现容量与精度的联合工作点优化。
- 在 DIV2K 和 Kodak 上，于多种预算下相较代表性 2D 高斯与隐式神经表示取得更好的率失真性能，同时保持固定总体表示预算与较低优化成本。

### 局限性
- 摘要未提供足够信息说明方法在不同图像内容类型或极端低预算下的具体表现。
- 摘要未提供足够信息说明计算复杂度、优化时间或校准开销的定量细节。
- 摘要未提供足够信息说明候选表示构造与选择过程的具体规模及对整体成本的影响。
- 摘要未提供足够信息说明方法在 DIV2K 和 Kodak 之外数据集上的泛化能力。

### 阅读优先级
中。理由：该论文聚焦 2D 高斯图像表示中的码率—失真优化，问题定义清晰，联合容量与精度的思路对相关方向有参考价值；但摘要未提供足够信息展示更细粒度的实验设置与局限性，是否优先精读取决于读者对高斯表示压缩与预算分配的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

2D Gaussian representations provide an explicit and efficient way to represent images, but their rate-distortion performance under limited budgets depends critically on how Gaussian capacity and parameter precision are allocated. Existing methods typically optimize these two resources separately, overlooking content-dependent capacity demands and heterogeneous quantization sensitivity. We present CP-GS, a capacity-precision coupled Gaussian splatting framework for budget-aware 2D Gaussian image representation that jointly optimizes capacity allocation and attribute precision under a shared rate constraint. CP-GS first constructs a content-adaptive Gaussian representation by dynamically reallocating a fixed Gaussian budget from redundant regions to areas with higher representation demand. It then introduces hierarchical distortion-aware representation quantization, using efficient rendering-based calibration to allocate precision across Gaussian attributes and further refine it within heterogeneous attribute groups. Finally, it jointly optimizes Gaussian capacity and attribute precision by constructing candidate representations with different Gaussian counts and precision configurations and selecting operating points according to decoded distortion and actual serialized size. Experiments on DIV2K and Kodak show that CP-GS achieves improved rate-distortion performance over representative 2D Gaussian and implicit neural representations across a range of budgets, while maintaining a fixed overall representation budget and low optimization cost. These results demonstrate the benefit of jointly optimizing spatial capacity and parameter precision for compact Gaussian image representation.

</details>

#### 2026-11-10 - RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors

**Authors:** Qiang Wen, Guotao Meng, Junhong Ruan, Hongyu Liu, Chenyang Lei, Qifeng Chen
**Links:** [abs](https://arxiv.org/abs/2611.13772) - [pdf](https://arxiv.org/pdf/2611.13772)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors
- 作者：Qiang Wen, Guotao Meng, Junhong Ruan, Hongyu Liu, Chenyang Lei, Qifeng Chen
- 出版日期：2026-11-10T09:11:01Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.13772)｜[PDF](https://arxiv.org/pdf/2611.13772)

### 一句话总结
该论文提出 RF3DGS，利用多视角光度先验与几何先验构建“无反射”伪标签，并在 3D Gaussian Splatting 框架下实现 3D 反射去除，同时建立了基于 Unity 的 3D 反射去除基准。

### 研究问题
论文关注 3D 反射去除问题，目标是在需要高保真可视化的应用（如博物馆展览）中去除反射影响。作者指出，将“同一 3D 点在多视角图像中的最小像素强度与无反射信息强相关”这一光度先验推广到多视角 3D Gaussian Splatting 并非易事，这是论文要解决的核心难点。

### 核心思路/方法
- 利用广泛采用的光度先验：同一 3D 点对应的多视角图像中，最小像素强度与无反射信息强相关。
- 首先使用几何先验优化一个基础 3DGS 模型，为每个视角估计粗略的无反射深度图。
- 基于这些深度图和光度先验，通过 3D warping 从辅助视角聚合无反射信息，为参考视角构建干净的透射伪标签。
- 该伪标签作为自监督信号用于优化。
- 引入 Adaptive Twin Rendering (ATR) 损失，在利用伪标签的同时保留原始含反射图像中的高频细节。
- 将上述内部 3D 自先验与 ATR 损失融合，形成 RF3DGS 方法。

### 主要贡献
- 提出 RF3DGS，一种用于反射去除的 Reflection-Free 3D Gaussian Splatting 新方法。
- 设计了一条将光度先验推广到多视角 3DGS 的流程：几何先验估计深度图、3D warping 构建无反射伪标签、自监督优化。
- 提出 Adaptive Twin Rendering (ATR) 损失，用于协同利用伪标签并保留原始图像高频细节。
- 摘要声称在合成和真实场景中均展现出 state-of-the-art 的反射去除性能。
- 建立了首个基于 Unity 渲染引擎的 3D 反射去除基准，用于严格定量评估。

### 局限性
- 摘要未提供足够信息说明方法对深度图估计误差、视角覆盖不足或光度先验失效场景的鲁棒性。
- 摘要未提供足够信息说明计算开销、训练时间、参数量等效率相关指标。
- 摘要未提供足够信息说明真实场景实验的具体设置、评价指标和数据规模。
- 摘要未提供足够信息说明基准的具体构成、场景数量和评测协议细节。
- 摘要未提供足够信息说明与哪些具体方法进行了对比以及定量结果。

### 阅读优先级
中。理由：该论文聚焦 3D Gaussian Splatting 中的 3D 反射去除，问题定义清晰，方法围绕光度先验、几何先验、3D warping 伪标签和 ATR 损失展开，并声称建立首个 Unity 渲染的 3D 反射去除基准；对神经渲染、3D 重建和反射去除方向的研究者有直接相关性。但摘要未给出具体实验数值、对比方法和效率信息，是否需要优先精读取决于读者对 3D 反射去除基准与方法细节的兴趣。

</details>

<details>
<summary>Abstract</summary>

3D reflection removal is crucial in applications demanding high-fidelity visualization, such as museum exhibitions. In this work, we propose Reflection-Free 3D Gaussian Splatting (RF3DGS), a novel method for superior reflection removal. RF3DGS exclusively leverages a widely-adopted photometric prior for reflection removal: that the minimum pixel intensity across multi-view images corresponding to the same 3D point strongly correlates with reflection-free information. However, generalizing this principle to a 3D Gaussian Splatting within a multi-view context is non-trivial. To address this, RF3DGS first optimizes a vanilla 3DGS model using a geometric prior to estimate a coarse, reflection-free depth map for each view. Leveraging these depth maps and photometric prior, a 3D warping process aggregates reflection-free information from auxiliary views to construct a clean transmission pseudo-label for a given reference view. This pseudo-label provides a robust self-supervised signal for optimization. We further introduce an Adaptive Twin Rendering (ATR) loss to synergistically utilize this pseudo-label while preserving high-frequency details from the original, reflection-degraded images. By adeptly fusing these internal 3D self-priors with the ATR loss, RF3DGS demonstrates state-of-the-art reflection removal performance across both synthetic and real-world scenarios. Furthermore, we establish the first 3D reflection removal benchmark, based on the Unity rendering engine, for rigorous quantitative evaluation.

</details>

#### 2026-11-09 - RetinexGS: Retinex-Inspired Gaussian Splatting for Low-Light RAW Reconstruction

**Authors:** Yulang Fei, Huaiyuan Weng, Chul Min Yeum
**Links:** [abs](https://arxiv.org/abs/2611.13280) - [pdf](https://arxiv.org/pdf/2611.13280)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RetinexGS: Retinex-Inspired Gaussian Splatting for Low-Light RAW Reconstruction
- 作者：Yulang Fei, Huaiyuan Weng, Chul Min Yeum
- 出版日期：2026-11-09T21:44:31Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.13280 ；PDF https://arxiv.org/pdf/2611.13280

### 一句话总结
RetinexGS 是一个 RAW 域 3D Gaussian Splatting 框架，结合 Retinex 启发的表观建模与传感器噪声信息优化，用于低光照新视角合成。

### 研究问题
标准 3D Gaussian Splatting 流程在严重欠曝图像上表现不稳定，暗区会出现颜色不稳定、漂浮伪影和不完整重建。论文关注低光照观测中的噪声问题，并利用 RAW 图像保留线性传感器测量与噪声元数据的特性，进行噪声感知重建。

### 核心思路/方法
- 在 RAW 域构建 3DGS 框架，结合 Retinex 启发的表观建模与传感器信息驱动的优化。
- 将每个高斯的颜色分解为与视角无关的基础颜色，以及共享的、依赖位置和视角的调制场，并对两个分量分别正则化，以约束从噪声观测中的表观学习。
- 使用 DNG 噪声元数据对重建损失加权，以处理信号相关噪声。
- 采用失真感知渲染，避免对 RAW 目标进行空间重采样。
- 针对暗区稀疏几何，引入深度引导初始化。

### 主要贡献
- 提出 RetinexGS，一个面向低光照新视角合成的 RAW 域 3DGS 框架。
- 引入 Retinex 启发的颜色分解与分量正则化，以应对噪声观测下的表观学习。
- 利用 DNG 噪声元数据加权重建损失，并结合失真感知渲染与深度引导初始化。
- 在三个公开 RawNeRF 场景和两个自采集低光照 RAW 场景上评估；所有方法在各场景使用相同 RAW 输入训练时，RetinexGS 在五个场景的平均 sRGB PSNR 上分别比 LE3D 和 RawNeRF 高 2.18 dB 和 2.71 dB，并支持实时新视角渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：论文针对低光照 RAW 重建与 3DGS 结合的问题，方法要点和定量结果在摘要中较明确，且涉及实时渲染；但摘要未提供失败案例、计算开销细节或更广泛场景验证，是否优先精读取决于对低光照神经渲染方向的关注程度。

</details>

<details>
<summary>Abstract</summary>

Standard 3D Gaussian Splatting (3DGS) pipelines struggle with severely underexposed images, producing unstable colors, floating artifacts, and incomplete reconstructions in dark regions. To better account for noise in these low-light observations, RAW images offer a natural basis for noise-aware reconstruction by preserving linear sensor measurements and providing access to noise metadata. We present RetinexGS, a RAW-domain 3DGS framework that combines Retinex-inspired appearance modeling with sensor-informed optimization for low-light novel-view synthesis. We factorize each Gaussian's color into a view-independent base color and a shared, position- and view-dependent modulation field, regularizing the two components separately to constrain appearance learning from noisy observations. We use DNG noise metadata to weight the reconstruction loss for signal-dependent noise, while distortion-aware rendering avoids spatially resampling RAW targets. To address sparse geometry in dark regions, we introduce depth-guided initialization. We evaluate RetinexGS on three public RawNeRF scenes and two custom-captured low-light RAW scenes. With all methods trained on the same RAW inputs for each scene, RetinexGS outperforms LE3D and RawNeRF in mean sRGB PSNR by 2.18 dB and 2.71 dB respectively, across the five scenes, while supporting real-time novel-view rendering.

</details>

#### 2026-11-09 - Plant Orbiter: 3D Plant Reconstruction and Generation with Video Diffusion Orbit Cameras and 3D Gaussian Splatting

**Authors:** Zane K. J. Hartley, Yong En Kok, Lewis A. G. Stuart, Andrew P. French, Michael P. Pound
**Links:** [abs](https://arxiv.org/abs/2611.12739) - [pdf](https://arxiv.org/pdf/2611.12739)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Plant Orbiter: 3D Plant Reconstruction and Generation with Video Diffusion Orbit Cameras and 3D Gaussian Splatting
- 作者：Zane K. J. Hartley, Yong En Kok, Lewis A. G. Stuart, Andrew P. French, Michael P. Pound
- 出版日期：2026-11-09T17:22:19Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.12739) / [PDF](https://arxiv.org/pdf/2611.12739)

### 一句话总结
Plant Orbiter 利用视频扩散生成环绕相机视角，并结合 3D Gaussian Splatting，从单张图像重建植物三维高斯表示，并可由文本提示生成三维植物模型。

### 研究问题
现代数字表型分析管线需要高通量、精确获取植物的三维形态性状，但植物形态复杂、结构纤细且存在遮挡，使得从二维向三维管线过渡时，高通量获取植物数字三维“双胞胎”仍然是显著挑战。

### 核心思路/方法
论文提出 Plant Orbiter，将视频扩散用于生成高质量的植物环绕相机视角，再结合 3D Gaussian Splatting，从单张图像生成植物的三维高斯表示。摘要还提到将该方法与二维扩散模型结合，从文本提示生成三维植物模型。

### 主要贡献
- 提出 Plant Orbiter，一种从单张图像生成植物三维高斯表示的流程。
- 在植物形态重建上，摘要称其相较其他先进方法更准确，对所有基线取得最高 3D F-score。
- 摘要称该方法更易于对齐、相机布置成本更低，因而更适合高通量管线。
- 与二维扩散模型结合后，摘要称其在文本提示生成三维植物模型方面取得最先进结果。

### 局限性
摘要未提供足够信息。摘要未给出数据集规模、评价指标细节、基线列表、计算成本、对特定植物类型的适用范围或失败案例分析。

### 阅读优先级
中。理由：该工作面向植物三维重建与生成，结合视频扩散和 3D Gaussian Splatting，若关注数字表型、三维植物建模或单图三维生成，具有相关性；但摘要未提供实验细节和定量结果的具体数值，需阅读全文才能判断方法可靠性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Modern digital phenotyping pipelines require the precise measurement of a range of 3D morphological plant traits. The accurate, high throughput acquisition of these traits helps breeders and researchers accelerate the development of new varieties, techniques and products. Recent advances in 3D technologies have enabled a rapid transition from 2D to 3D pipelines, but high throughput acquisition of digital 3D twins of plants remains a significant challenge due to complex morphology, thin structures and occlusions. In this paper we present Plant Orbiter, a new approach to generating 3D plants that leverages recent advances in video diffusion to produce high quality 3D Gaussian Splats of plants from a single image. We show that our method more accurately recreates plant morphology than other state-of-the-art methods, achieving the highest 3D F-score against all baselines, while being more practical for high throughput pipelines due to easier alignment and reduced cost of camera placement. Combined with a 2D diffusion model, we show that our method also achieves state-of-the-art results in the generation of 3D plant models from a text prompt.

</details>

#### 2026-11-09 - Spaghetti Splatting: Differentiating Curvilinear Dirac Masses via Convolution

**Authors:** George Shramko, Shrisudhan Govindarajan, Rudy Lam, Yizheng Xie, Daniel Rebain, David B. Lindell, Andrea Tagliasacchi
**Links:** [abs](https://arxiv.org/abs/2611.12716) - [pdf](https://arxiv.org/pdf/2611.12716)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spaghetti Splatting: Differentiating Curvilinear Dirac Masses via Convolution
- 作者：George Shramko, Shrisudhan Govindarajan, Rudy Lam, Yizheng Xie, Daniel Rebain, David B. Lindell, Andrea Tagliasacchi
- 出版日期：2026-11-09T17:04:26Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.12716) / [PDF](https://arxiv.org/pdf/2611.12716)

### 一句话总结
论文提出 Spaghetti Splatting，用折线近似曲线基元，并通过卷积将曲线上的 Dirac 质量平滑化后进行体渲染，从而支持从图像学习曲线型几何表示。

### 研究问题
生产系统中的 3D 几何常由点、线、三角形等基元表示，但这类基元本质上是定义在无穷小位置上的 Dirac 质量，直接通过体渲染从图像中学习具有挑战性。已有方法如 EWA splatting、Poisson reconstruction 和 3D Gaussian Splatting 通过低通核卷积 Dirac 质量来解决该问题，其中点和三角形已被较多研究，而曲线型基元在该框架下的学习仍待探索。

### 核心思路/方法
论文研究“核函数 + 基元”这一卷积平滑配方在曲线型基元上的推广。具体而言，用折线近似曲线，并构造折线的卷积使其收敛到连续曲线的卷积；对每个线段进行体渲染，使相连线段在关节处合成时不会重复计数。为加速训练和推理，论文对每个线段线性化相机投影，并且该方法可容纳高斯核之外的核函数，例如 Beta 核。由于点可视为长度为零的曲线，该表示是 3D Gaussian Splatting 的严格超集。

### 主要贡献
- 提出 Spaghetti Splatting，将卷积平滑 Dirac 质量的思路扩展到曲线型基元。
- 使用折线近似曲线，并设计线段体渲染方式，使连接线段在关节处合成时不重复计数。
- 对每个线段线性化相机投影以支持快速训练和推理，并兼容非高斯核（如 Beta 核）。
- 指出点是零长度曲线，因此该表示严格包含 3D Gaussian Splatting。
- 摘要称其在一般场景上与当前先进方法相比仍具竞争力，在线状几何上优于专用方法，原生支持抗锯齿，并能产生可直接用于物理仿真的长连接线段。

### 局限性
摘要未提供足够信息说明该方法的具体失效场景、计算开销、对复杂拓扑曲线的处理能力、训练数据需求或定量实验细节。摘要也未提供足够信息说明折线近似误差、关节合成策略的数值稳定性以及线性化相机投影带来的近似误差范围。

### 阅读优先级
中。理由：该论文关注曲线型基元的体渲染与可微学习，属于神经场景表示与渲染方向，且声称是 3D Gaussian Splatting 的严格超集并支持非高斯核与抗锯齿；但摘要未给出定量结果和实现细节，是否值得优先精读取决于读者对曲线基元、splatting 表示或物理仿真可用几何的兴趣。

</details>

<details>
<summary>Abstract</summary>

In production systems, 3D geometry is represented by primitives such as points, lines, and triangles, as rendering hardware is optimized to generate images from them very efficiently. Learning such primitives from images by volume rendering is challenging, as they are Dirac masses defined at infinitesimal locations in space. EWA splatting, Poisson reconstruction, and 3D Gaussian Splatting overcome this by convolving Dirac masses with a low-frequency kernel, a recipe that generalizes along two axes: the kernel and the primitive. As points and triangles have already received significant attention, we investigate this recipe for curvilinear primitives, and introduce Spaghetti Splatting. We approximate curves by polylines whose convolution converges to that of the continuous curve, and volume render each segment so that connected segments composite without overcounting at their joints. For fast training and inference, we linearize the camera projection per segment, which also accommodates kernels beyond Gaussians, such as Beta kernels. As a point is a curve of zero length, our representation is a strict superset of 3D Gaussian Splatting. It remains competitive with the state-of-the-art on general scenes, outperforms methods specialized to line-like geometry, natively supports anti-aliasing, and produces long connected strands that are directly amenable to physics simulation.

</details>

#### 2026-11-09 - Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs

**Authors:** Junha Ryu, Hoi-Jun Yoo
**Links:** [abs](https://arxiv.org/abs/2611.12319) - [pdf](https://arxiv.org/pdf/2611.12319)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs
- 作者：Junha Ryu, Hoi-Jun Yoo
- 出版日期：2026-11-09T12:41:30Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.12319) / [PDF](https://arxiv.org/pdf/2611.12319)

### 一句话总结
该论文针对 GPU 上 3D Gaussian Splatting 渲染中由屏幕瓦片负载不均导致的 SM 级负载失衡与长执行尾问题，提出一种无需重训练、无需专用硬件的软件定义 GPU 调度方法，以缓解执行尾并加速 alpha blending。

### 研究问题
论文指出，现有 GPU 上 3DGS 的优化要么依赖需要重训练的算法改动，要么依赖缺乏灵活性、难以适配不断演进的 3DGS 变体的专用加速器。作者识别出 GPU 端 3DGS 渲染中的一个基础性低效问题：屏幕瓦片间工作量不均导致严重的 SM 级负载失衡，形成长执行尾——少数 SM 处理计算密集的瓦片，而多数 SM 空闲，在大规模城市场景中尤为明显。

### 核心思路/方法
论文提出一种软件定义的 GPU 调度方法，用于缓解上述执行尾，且不修改原始 alpha blending 公式：
- 使用 persistent kernel 优先调度重负载瓦片（heavy tiles first）；
- 对离群瓦片（outlier tiles）选择性地跨多个 CTA 分块（chunking）处理；
- 采用轻量的逐帧策略，利用渲染管线中已有的瓦片统计数据决定何时分块、分块程度多少；
- 不依赖重训练或专用硬件，可与现有优化正交组合，适用于多种 3DGS 变体。

### 主要贡献
- 识别并刻画了 GPU 端 3DGS 渲染中由屏幕瓦片工作量不均引起的 SM 级负载失衡与执行尾问题。
- 提出基于 persistent kernel 的软件定义调度方案：重瓦片优先调度 + 离群瓦片跨 CTA 分块，并配合基于已有瓦片统计的逐帧轻量策略。
- 方法无需重训练、无需专用硬件，可与现有优化正交叠加，并保留原始 alpha blending 公式。
- 摘要报告：在大规模城市场景中，按场景平均，alpha blending 最高加速 2.93x；在其最不均衡的帧上最高加速 5.6x。

### 局限性
摘要未提供足够信息。例如：具体实验平台与 GPU 型号、对比基线细节、测试场景与数据集规模、分块策略的开销与适用边界、对非城市场景或不同 3DGS 变体的实测效果等，均未在摘要中说明。

### 阅读优先级
低。理由：该工作聚焦 GPU 渲染调度与系统级性能优化，属于较专门的工程优化方向；若读者关注 3DGS 的渲染效率、GPU 负载均衡或实时渲染系统实现，则相关性较高，但摘要未提供足够信息判断其通用性与实验严谨性，建议按需查阅全文。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic, real-time rendering on commodity GPUs and is increasingly adopted in generative world models and autonomous driving simulators. However, existing optimizations rely on algorithmic changes that often require retraining, or on specialized accelerators that lack flexibility across evolving 3DGS variants. In this paper, we identify a fundamental inefficiency in GPU-based 3DGS rendering: severe SM-level load imbalance caused by uneven workloads across screen tiles. This imbalance creates a long execution tail, leaving most SMs idle while a few process computationally intensive tiles, particularly in large-scale urban scenes. To address this, we present a software-defined GPU scheduling approach that mitigates the execution tail. Our approach uses a persistent kernel to schedule heavy tiles first and selectively chunks outlier tiles across multiple CTAs. A lightweight per-frame policy determines when and how much to chunk using tile statistics already available in the rendering pipeline. Our approach requires neither retraining nor specialized hardware and can be applied orthogonally to existing optimizations across diverse 3DGS variants. Averaged per scene, it accelerates alpha blending by up to 2.93x on a large-scale urban scene, and by up to 5.6x on its most imbalanced frames, while retaining the original alpha blending formulation.

</details>

#### 2026-11-09 - UltraVoxelGS: Voxel-First Feed-Forward Gaussian Splatting for 3D Ultrasound Reconstruction

**Authors:** Yue Wang, Haoxin Chen, Xiaoqing Guo
**Links:** [abs](https://arxiv.org/abs/2611.11951) - [pdf](https://arxiv.org/pdf/2611.11951)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, scene representation, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UltraVoxelGS: Voxel-First Feed-Forward Gaussian Splatting for 3D Ultrasound Reconstruction
- 作者：Yue Wang, Haoxin Chen, Xiaoqing Guo
- 出版日期：2026-11-09T06:16:49Z（按 arXiv 元数据）
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.11951) / [PDF](https://arxiv.org/pdf/2611.11951)

### 一句话总结
UltraVoxelGS 是一种“体素优先”的前馈式高斯泼溅 3D 超声重建方法：直接从带位姿的超声图像预测完整高斯场景表示，绕过逐场景优化，从而在约 10 秒内完成重建并提升渲染的物理一致性。

### 研究问题
论文摘要指出，既有 3D 超声重建方法受限于逐场景优化瓶颈，无法在线使用，通常需要离线处理。若将自然图像中常见的前馈高斯预测直接迁移到超声场景，会面临两个问题：
1. 超声切片之间最多只有一维交集，不满足现有前馈高斯方法所假设的密集重叠；
2. 由于声学传播与衰减，超声外观具有视角依赖性，不满足光度一致性假设。

因此，核心问题是：如何在超声切片重叠稀疏、外观不一致的条件下，实现快速且物理忠实的前馈 3D 重建与渲染。

### 核心思路/方法
- **前馈预测整体高斯场景**：从带位姿的超声图像直接预测完整高斯场景表示，避免逐场景优化。
- **前馈体素到高斯通道**：将所有带位姿切片提升到固定大小的体素支撑中，再直接预测高斯参数，从而将表示规模与输入帧数解耦。
- **超声感知的外观渲染策略**：在训练中将反射与累积衰减进行分解，并利用空间相邻切片之间的外观连续性，在渲染时进行高效的“渲染时外观自适应”（Render-time Appearance Adaptation）。

### 主要贡献
1. 提出 UltraVoxelGS，摘要称其首次同时实现快速重建和物理忠实渲染，为 2D 超声扫描过程中的实时空间反馈提供可能。
2. 设计前馈体素到高斯预测路径，绕过逐场景优化瓶颈，并将表示规模与输入数量解耦。
3. 针对超声的视角依赖外观，提出分解反射与累积衰减的训练策略，以及利用相邻切片外观连续性的渲染时外观自适应。
4. 在真实与模拟数据集上，摘要报告其 PSNR/SSIM 优于逐场景优化基线，同时将推理时间从 10–20 分钟缩短到约 10 秒（超过 35 倍加速），并可扩展到超过 1,000 帧的序列。

### 局限性
- 摘要未提供足够信息说明方法在极端稀疏视角、不同超声设备或噪声条件下的鲁棒性。
- 摘要未提供足够信息说明“超过 1,000 帧”扩展实验的具体设置与资源消耗。
- 摘要未提供足够信息说明失败案例、计算内存需求或临床部署限制。

### 阅读优先级
**高**。理由：该论文直接针对 3D 超声重建中“离线逐场景优化”的关键瓶颈，提出前馈式高斯泼溅方案，并在摘要中报告了显著加速与 PSNR/SSIM 提升；若关注实时/在线超声空间反馈、前馈神经渲染或高斯泼溅在医学超声中的应用，具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

We present UltraVoxelGS, a 3D ultrasound reconstruction method that achieves both fast reconstruction and physically faithful rendering for the first time, bringing live spatial feedback during 2D ultrasound scanning within reach. This is made possible by a feed-forward design that predicts a complete Gaussian scene representation from posed ultrasound images directly, entirely bypassing the per-scene optimization bottleneck that has confined prior methods to offline use. Realising such feed-forward prediction in this setting is non-trivial: unlike natural images, ultrasound slices share at most one-dimensional intersections and exhibit view-dependent appearance due to acoustic propagation and attenuation, violating the dense overlap and photometric consistency assumed by existing feed-forward Gaussian methods. Hence, to achieve fast reconstruction, we introduce a feed-forward voxel-to-Gaussian pass that decouples representation size from input count by lifting all posed slices into a fixed-size voxel support and predicting Gaussian parameters directly. For faithful rendering, we propose ultrasound-aware appearance rendering strategy factorize reflection from cumulative attenuation during training and exploit appearance continuity among spatially adjacent slices for efficient Render-time Appearance Adaptation. On both real-world and simulated datasets, UltraVoxelGS achieves best PSNR/SSIM compared with per-scene optimization baselines while reducing inference from 10-20 minutes to approximately 10 seconds (over 35 times faster) and scales to sequences exceeding 1,000 frames. Code is available at https://github.com/YuebyYue/UltraVoxelGS-camera-ready.

</details>

#### 2026-11-08 - FastGRT: Accelerating Training of 3D Gaussian Ray Tracing

**Authors:** Meet Banthia, Xiaoteng Liu, Hexu Zhao, Aurojit Panda, Jinyang Li
**Links:** [abs](https://arxiv.org/abs/2611.11586) - [pdf](https://arxiv.org/pdf/2611.11586)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FastGRT: Accelerating Training of 3D Gaussian Ray Tracing
- 作者：Meet Banthia, Xiaoteng Liu, Hexu Zhao, Aurojit Panda, Jinyang Li
- 出版日期：2026-11-08T20:00:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.11586) / [PDF](https://arxiv.org/pdf/2611.11586)

### 一句话总结
FastGRT 通过重构 GPU 上高斯光线追踪的计算组织方式，在不改变原始渲染公式的前提下显著加速 GRT 的训练。

### 研究问题
基于高斯的光线追踪（GRT）能实现基于光栅化的 3D Gaussian Splatting 难以达到的渲染能力，但其训练成本远高于 3DGS。论文聚焦于：光线追踪在 GPU 上的执行方式中，有相当一部分训练开销源于计算的组织方式，而非算法本身。

### 核心思路/方法
- 将光线遍历（ray traversal）与混合（blending）解耦，以改善计算组织；
- 在前向传播中完成的工作可在反向传播中复用；
- 引入快速梯度累积（fast gradient accumulation）优化；
- 采用混合 BVH 更新策略（hybrid BVH update strategy）以缓解训练管线中的其他主要瓶颈；
- 基于 Vulkan 实现，作者称其为首个同时支持训练与渲染的 Vulkan 版 GRT 实现。

### 主要贡献
- 指出 GRT 训练开销的重要来源是 GPU 上的计算组织方式；
- 提出 FastGRT，通过解耦遍历与混合、复用前向计算结果，并配合梯度累积与 BVH 更新优化来加速训练；
- 给出首个支持训练和渲染的 Vulkan 版 GRT 实现；
- 与 3DGRT 相比，训练时间提升 1.9× 至 4.97×，同时保持原始渲染公式不变；
- 代码开源。

### 局限性
- 摘要未提供足够信息说明实验所用的数据集、场景规模或硬件配置；
- 摘要未提供足够信息说明加速比在不同场景或分辨率下的波动原因；
- 摘要未提供足够信息说明混合 BVH 更新策略的具体触发条件与开销；
- 摘要未提供足够信息说明与 3DGS 训练成本的绝对差距；
- 摘要未提供足够信息说明 Vulkan 实现相对其他图形 API 实现的通用性与可移植性限制。

### 阅读优先级
中。理由：该工作针对 3D 高斯光线追踪训练效率这一明确瓶颈，提出了可复用的计算组织优化与工程实现，并报告了较大加速比且开源；但摘要未披露实验细节与适用边界，若关注训练加速的系统实现可优先阅读，若关注渲染质量或新表示则信息有限。

</details>

<details>
<summary>Abstract</summary>

Ray Tracing enables rendering capabilities that are difficult to achieve with rasterization-based approaches such as 3D Gaussian Splatting (3DGS). However, the training cost of Gaussian-based ray tracing (GRT) is much higher than that of 3DGS. In this paper, we study how ray tracing using Gaussians executes on GPUs and show that a considerable fraction of the training cost arises from how the computation is organized. We develop FastGRT, which decouples ray traversal from blending and reuses work done in the forward pass for the backward pass. FastGRT further incorporates optimizations such as fast gradient accumulation and a hybrid BVH update strategy to tackle other major bottlenecks in the training pipeline. We implement FastGRT in Vulkan. To the best of our knowledge, it is the first Vulkan-based GRT implementation that supports both training and rendering. Compared to 3DGRT, FastGRT improves training time by 1.9$\times$ to 4.97$\times$, while preserving the original rendering formulation. Our code is open source.

</details>

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-10 - From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation

**Authors:** Chengxiao Dong, Alessio Caporali, Hongyu Lan, Gianluca Palli
**Links:** [abs](https://arxiv.org/abs/2611.14274) - [pdf](https://arxiv.org/pdf/2611.14274)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation
- 作者：Chengxiao Dong, Alessio Caporali, Hongyu Lan, Gianluca Palli
- 出版日期：2026-11-10T16:17:48Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.14274) | [PDF](https://arxiv.org/pdf/2611.14274)

### 一句话总结
论文区分“预测效用”与“决策效用”，在平面单抓取 DLO 形状控制中比较不同物理上下文表示对前向预测与执行控制的不同价值。

### 研究问题
论文关注：能够准确预测可变形物体响应的表示，未必最有利于选择操作动作。作者在平面单抓取可变形线性物体（DLO）形状控制任务中，研究预测效用与决策效用之间的区别，并比较不同物理上下文表示分别对前向预测和实际控制的作用。

### 核心思路/方法
- 提出 Geometry-Pointer-Flow（GPF）作为共同决策主干，将抓取位置选择与以抓取为条件的运动生成分离。
- 使用仅几何变体与 DLO 专用扩散策略比较，报告一步执行形状误差降低 32.8%，参数量少 18.7 倍，推理约快 193 倍。
- 在 GPF 主干上比较三类物理上下文表示：真实参数、估计参数、学习到的交互历史表示。
- 分别评估这些表示在前向预测与执行控制中的表现。
- 所有策略仅在仿真中训练，并迁移到实体机器人，无真实世界训练或微调。

### 主要贡献
- 明确指出并实证研究可变形物体操作中“预测效用”与“决策效用”的区分。
- 提出 Geometry-Pointer-Flow（GPF）决策主干，并给出仅几何变体在误差、参数量与推理速度上的对比结果。
- 发现物理上下文表示在预测与控制中的排序不一致：预测上真实参数优于仅几何，估计参数略优于交互历史；控制上估计参数无可检测的一步控制增益，而历史条件 GPF 相对仅几何 GPF 降低执行误差 9.9%（470 次配对仿真试验）。
- 闭环中交互历史在仿真中提升严格阈值达成率，并在硬件上取得最强零样本性能。
- 结论主张物理上下文应按其支持的决策来评估，而非仅看预测精度。

### 局限性
- 任务范围限于平面单抓取 DLO 形状控制，摘要未提供对其他变形物体或更复杂操作任务的泛化信息。
- 摘要未提供硬件实验的具体规模、评价指标细节与统计显著性信息。
- 摘要未提供真实参数、估计参数与交互历史表示的具体实现细节。
- 摘要未提供失败案例分析或方法在更强动态扰动下的表现。
- 代码尚未发布，摘要仅说明接收后发布。

### 阅读优先级
高。理由：论文直接挑战“预测精度等同决策价值”的常见假设，并给出预测与控制排序不一致的实证结果；同时报告了显著的计算效率优势与仿真到真实零样本迁移结果，对可变形物体操作与表征学习方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

A representation that accurately predicts a deformable object's response is not necessarily the one most useful for choosing manipulation actions. We study this distinction between predictive utility and decision utility in planar single-grasp shape control of Deformable Linear Objects (DLOs). As a common decision backbone, we introduce Geometry-Pointer-Flow (GPF), a geometry-grounded policy that separates grasp-location selection from grasp-conditioned motion generation. Its geometry-only variant reduces one-step executed shape error by 32.8% relative to a DLO-specific diffusion policy, while using 18.7 times fewer parameters and achieving approximately 193 times faster inference. On this backbone, we compare physical context represented by ground-truth parameters, estimated parameters, and learned interaction-history representations, for both forward prediction and executed control. For prediction, ground-truth physical parameters reduce next-shape error by 15.8% over geometry alone, and estimated parameters are slightly more predictive than interaction history. This ordering does not carry over to control: estimated parameters provide no detectable one-step control gain, whereas history-conditioned GPF reduces executed error by 9.9% relative to geometry-only GPF across 470 paired simulation trials. In closed loop, interaction history improves strict-threshold attainment in simulation and yields the strongest zero-shot performance on hardware. All policies are trained exclusively in simulation and transferred to the physical robot without real-world training or fine-tuning. These results show that physical context should be evaluated by the decisions it supports rather than by predictive accuracy alone. Code will be released upon acceptance.

</details>

#### 2026-11-10 - CIALLO: Learning Shared Intent Representations for Cross-Embodiment Manipulation

**Authors:** Choo Sin Wai, Dake Zhong, Jingye Zhang, Zhifang Liu, Siyao Xiao, Zirong Ding, Yuhong Zhang, Kangjie Chen, Dongbin Zhang, Guorui Song, Guocun Wang, Peng Jiao, Haoqian Wang
**Links:** [abs](https://arxiv.org/abs/2611.13732) - [pdf](https://arxiv.org/pdf/2611.13732)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CIALLO: Learning Shared Intent Representations for Cross-Embodiment Manipulation
- 作者：Choo Sin Wai, Dake Zhong, Jingye Zhang, Zhifang Liu, Siyao Xiao, Zirong Ding, Yuhong Zhang, Kangjie Chen, Dongbin Zhang, Guorui Song, Guocun Wang, Peng Jiao, Haoqian Wang
- 出版日期：2026-11-10T08:35:27Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.13732 ；PDF https://arxiv.org/pdf/2611.13732

### 一句话总结
CIALLO 提出一种动作编解码器，将动作、视觉变化与语言对齐到短时程行为意图的共享空间，并通过“具身校准与任务学习分离”的方式实现跨形态机器人操作知识迁移。

### 研究问题
机器人演示中包含可复用的操作知识，但跨具身迁移需要能够桥接不同控制接口差异的表示。论文指出，仅靠动作重建不能保证不同机器人上的相似行为共享同一表示，因此核心问题是：如何学习一种共享的行为意图表示，使其既能跨机器人复用，又能映射回各自的具体动作。

### 核心思路/方法
- 提出 CIALLO，一种动作编解码器，在短时程行为意图的共享空间中对齐动作、视觉变化和以观测为基础的语言。
- 使用以具身为条件的解码器，将共享意图映射回机器人特定的动作，从而让同一表示支持不同控制接口。
- 在八个具身上预训练后，CIALLO 可通过一段最长 10 秒的新机器人录制数据，仅更新具身嵌入来适配新机器人。
- 校准后的编解码器保持冻结，由策略从观测和指令中学习预测意图。
- 以 Qwen3.5-4B 实例化该策略，形成 Qwen-CIALLO；摘要称其骨干在策略微调前无需大规模机器人动作预训练。

### 主要贡献
- 提出将动作、视觉变化与语言对齐到共享短时程行为意图空间的动作编解码器 CIALLO，用于跨具身操作。
- 设计具身条件解码与轻量具身校准流程：预训练覆盖八个具身，新机器人仅需不超过 10 秒录制并只更新具身嵌入。
- 将共享编解码器与策略学习解耦：编解码器冻结，策略学习从观测和指令预测意图。
- 实验报告称，在每任务 20 个演示下，Qwen-CIALLO 在真实 SO-101 与单臂 Piper 机器人上平均成功率为 76.7%，高于全量微调 π0 的 70.0%。
- 仿真中额外微调动作解码器后，在 LIBERO 上达到 97.3%，在 RoboTwin 2.0 上达到 52.7%；LIBERO 策略在不再微调情况下于 LIBERO-Plus 达到 80.8%。

### 局限性
- 摘要未提供足够信息说明八个预训练具身的具体构成、数据规模与多样性。
- 摘要未提供足够信息说明真实机器人实验的任务数量、评测协议、方差或失败模式分析。
- 摘要未提供足够信息说明“仅更新具身嵌入”的校准在何种条件下失效，或对录制数据质量的敏感性。
- 摘要未提供足够信息说明与更多基线方法的系统对比，除 π0 外的比较对象未提及。
- 摘要未提供足够信息说明计算成本、推理延迟与模型规模对实际部署的影响。
- 摘要未提供足够信息说明仿真中额外微调动作解码器与真实实验中冻结解码器之间的性能差异来源。

### 阅读优先级
高。理由：该论文直接针对跨具身操作中的共享表示与控制接口迁移问题，提出“具身校准与任务学习分离”的明确技术路线，并给出真实机器人与仿真基准上的量化结果；若关注跨具身机器人学习、动作表示学习或轻量适配新机器人，该摘要信息具有较高参考价值。但需注意，摘要未提供实验细节与消融分析，深入判断仍需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Robot demonstrations contain reusable manipulation knowledge, but transferring this knowledge across embodiments requires representations that bridge differences in control interfaces. Action reconstruction alone does not ensure that similar behaviors across robots share a representation. To address this gap, we introduce CIALLO, an action codec that aligns actions, visual changes, and observation-grounded language in a shared space of short-horizon behavioral intent. An embodiment-conditioned decoder maps this intent back to robot-specific actions, allowing a shared representation to support different control interfaces. After pretraining on eight embodiments, CIALLO adapts to a new robot from one recording of at most 10 seconds by updating only its embodiment embeddings. The calibrated codec then remains frozen while a policy learns to predict intent from observations and instructions. We instantiate this policy with Qwen3.5-4B to form Qwen-CIALLO, whose backbone requires no large-scale robot-action pretraining before policy finetuning. With 20 demonstrations per task, Qwen-CIALLO achieves 76.7\% average success across real SO-101 and single-arm Piper robots, compared with 70.0\% for fully finetuned $π_0$. In simulation, we additionally finetune the action decoder, achieving 97.3\% success on LIBERO and 52.7\% on RoboTwin 2.0. The LIBERO policy also achieves 80.8\% on LIBERO-Plus without further finetuning. Together, these results support a shared action codec as a transferable control interface that separates embodiment calibration from task learning.

</details>

#### 2026-11-10 - PUMA: Probability-Constrained Sequential Interaction for Forensic Localization

**Authors:** Zhouli Yu, Mengyuan Zhou
**Links:** [abs](https://arxiv.org/abs/2611.13621) - [pdf](https://arxiv.org/pdf/2611.13621)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PUMA: Probability-Constrained Sequential Interaction for Forensic Localization
- 作者：Zhouli Yu, Mengyuan Zhou
- 出版日期：2026-11-10T06:03:20Z
- 分类：主分类 Embodied / Robotics / AR Applications；无次级分类
- 链接：[摘要](https://arxiv.org/abs/2611.13621) / [PDF](https://arxiv.org/pdf/2611.13621)

### 一句话总结
PUMA 通过空间约束的非平衡最优传输与基于共享位置接口的逐位置凸选择，显式保留匹配质量失配信息并自适应决定跨分支顺序交互，用于图像篡改定位。

### 研究问题
摘要指出，图像篡改定位需要同时利用语义结构与对噪声敏感的法证证据；但空间对应关系、匹配质量以及交互顺序三者的影响常被混在一起。现有语义—法证融合方法虽能提供互补表示，却未能在空间对应过程中显式保留质量失配信息，也未自适应选择信息在各分支间的传播顺序。论文即针对这两个未显式处理的问题展开。

### 核心思路/方法
- 提出 PUMA（Probability-constrained Unbalanced Matching and Aggregation），将空间约束的非平衡最优传输与两种顺序算子之间的逐位置凸选择相结合，二者通过共享位置接口连接。
- 在归一化之前保留带符号的传输质量残差（signed transport-mass residuals）。
- 构造行随机的跨分支算子与噪声分支内算子。
- 通过门控残差路径更新噪声特征。

### 主要贡献
- 明确将空间对应、匹配质量与交互顺序的影响分开处理，提出在空间对应中保留质量失配信息的机制。
- 引入基于共享位置接口的自适应顺序交互选择。
- 摘要称 PUMA 在四个测试集上取得较强定位结果，其中 COVERAGE 与 NIST16 上的分数超过其对比列表中代表性方法的已发表结果。
- 摘要称实验支持局部匹配状态与自适应顺序交互对跨源定位及若干后处理条件的有效性。

### 局限性
- 摘要未提供足够信息说明四个测试集的具体构成、对比方法清单、评价指标细节及消融实验设置。
- 摘要未提供足够信息说明“若干后处理条件”具体指哪些条件及其影响程度。
- 摘要未提供足够信息说明方法在何种失败场景或噪声条件下可能退化。
- 摘要未提供足够信息说明计算开销、参数量或推理效率。
- 主分类为 Embodied / Robotics / AR Applications，与图像篡改定位主题的对应关系摘要未提供足够信息。

### 阅读优先级
中。理由：论文针对语义—法证融合中匹配质量保留与交互顺序自适应这两个较具体的问题，并报告了在 COVERAGE 与 NIST16 上超过部分已发表方法的结果，对图像篡改定位方向有参考价值；但摘要未给出实验细节、对比方法清单与效率信息，且分类标签与主题存在不一致，需阅读全文后才能判断其方法有效性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Image manipulation localization must jointly exploit semantic structure and noise-sensitive forensic evidence. However, the effects of spatial correspondence, matching quality, and interaction order are often conflated. Existing semantic-forensic fusion methods provide complementary representations, but do not explicitly preserve quality-mismatch information during spatial correspondence or adaptively select the order in which information is propagated across branches. We propose PUMA (Probability-constrained Unbalanced Matching and Aggregation), which combines spatially constrained unbalanced optimal transport with position-wise convex selection between two sequential operators through a shared positional interface. Before normalization, PUMA retains signed transport-mass residuals, constructs row-stochastic cross-branch and within-noise-branch operators, and updates noise features through a gated residual path. PUMA achieves strong localization results on four test sets, with scores on COVERAGE and NIST16 exceeding the published results of the representative methods listed in our comparison. The experiments support the utility of local matching states and adaptive sequential interaction for cross-source localization and several post-processing conditions.

</details>

#### 2026-11-09 - AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA

**Authors:** Yuguang Yang, Zhewen Tan, Canyu Chen, Linlin Yang, Cheng Chi, Chunyang Liu, Kehua Sheng, Jinyu Yang, Baochang Zhan, Bo Zhang, Yan Wang, Xianbin Cao
**Links:** [abs](https://arxiv.org/abs/2611.12382) - [pdf](https://arxiv.org/pdf/2611.12382)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA
- 作者：Yuguang Yang, Zhewen Tan, Canyu Chen, Linlin Yang, Cheng Chi, Chunyang Liu, Kehua Sheng, Jinyu Yang, Baochang Zhan, Bo Zhang, Yan Wang, Xianbin Cao
- 出版日期：2026-11-09T13:20:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.12382 ；PDF https://arxiv.org/pdf/2611.12382 ；代码 https://github.com/ShivaTeam/AutoVLA-D

### 一句话总结
论文提出 TrajCond（一种离散的轨迹—几何条件）与 AutoVLA-D 方法，在连续轨迹预测前以两阶段训练学习该条件，并同时自回归生成离散与数值轨迹；实验显示离散轨迹作为直接输出较弱，但作为 TrajCond 能稳定提升最终连续轨迹预测。

### 研究问题
自回归 VLA 规划通常把连续轨迹作为最终输出，而驾驶指令往往描述动作而非自车状态，这削弱了对最终连续轨迹的直接条件约束。论文要解决的是：如何为 VLA 规划引入更有效的条件表示，以改善最终连续轨迹预测。

### 核心思路/方法
- 提出 TrajCond：为 VLA 规划引入一种离散的轨迹—几何条件。
- 将 TrajCond 表示为 1D-Brohan 差分动作轨迹，并在最终连续轨迹预测之前，用两阶段训练框架学习它。
- 方法同时自回归生成离散轨迹与数值轨迹，因此命名为 AutoVLA-D（Double）。
- 评测覆盖闭环与开环驾驶基准：NAVSIM navtest、nuScenes、NeuroNCAP。

### 主要贡献
- 指出并针对“驾驶指令描述动作而非自车状态、削弱连续轨迹直接条件化”的缺口，提出离散轨迹—几何条件 TrajCond。
- 给出 AutoVLA-D 方法：以两阶段训练学习 TrajCond，并在最终连续轨迹预测前使用，同时自回归生成离散与数值轨迹。
- 实验结论：离散轨迹作为直接输出较弱，但作为 TrajCond 更有效，能在闭环与开环驾驶基准上一致提升最终连续轨迹预测。
- 公开代码链接。

### 局限性
- 摘要未提供足够信息说明两阶段训练的具体阶段划分、损失设计与训练细节。
- 摘要未提供足够信息说明各基准上的具体指标数值、对比基线完整列表与消融实验细节。
- 摘要未提供足够信息说明 1D-Brohan 差分动作轨迹的具体定义、离散化方式与参数设置。
- 摘要未提供足够信息说明方法在失败情形、计算开销或泛化边界方面的分析。

### 阅读优先级
高。理由：论文直接针对 VLA 规划中“动作指令与连续轨迹条件化不匹配”的关键问题，提出可复用的离散轨迹—几何条件，并在 NAVSIM navtest、nuScenes、NeuroNCAP 的闭环与开环基准上报告一致提升，且提供代码；对自动驾驶 VLA 规划与轨迹条件化方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous trajectory. We address this gap with TrajCond, which introduces a discrete trajectory-geometric condition for VLA planning. Specifically, we represent TrajCond as a 1D-Brohan differential action trajectory and learn it with a two-stage training framework before final continuous trajectory prediction. With the simultaneous autoregressive generation of discrete and numeric trajectories, we name our method AutoVLA-D (Double). Experiments on NAVSIM navtest, nuScenes, and NeuroNCAP show that discrete trajectories are weaker as direct outputs but more effective as TrajCond, consistently improving final continuous trajectory prediction across closed-loop and open-loop driving benchmarks. Code is available at https://github.com/ShivaTeam/AutoVLA-D.

</details>

#### 2026-11-09 - QCC-WM: Linking Macro-State Dynamics and Visual Generation via Quotient Causal Construction

**Authors:** Zhizhong Fu, Wei Zhou, Zhaoyang Jiang, Yudong Lin, Songlun Li, Zhi Li, Feifan Chen, Gaoming Li, Xiaorong Ding, Yifan Chen
**Links:** [abs](https://arxiv.org/abs/2611.12353) - [pdf](https://arxiv.org/pdf/2611.12353)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：QCC-WM: Linking Macro-State Dynamics and Visual Generation via Quotient Causal Construction
- 作者：Zhizhong Fu, Wei Zhou, Zhaoyang Jiang, Yudong Lin, Songlun Li, Zhi Li, Feifan Chen, Gaoming Li, Xiaorong Ding, Yifan Chen
- 出版日期：2026-11-09T13:05:16Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.12353 ；PDF https://arxiv.org/pdf/2611.12353

### 一句话总结
QCC-WM 提出一种基于商式因果构造的视觉世界模型，通过动作响应构建宏状态并进行递归预测，同时用共享参考商度量约束宏层预测与生成视觉变化的一致性。

### 研究问题
论文关注动作条件世界建模中的关键挑战：如何从高维观测中构造支持动作条件下递归预测的宏状态，并保持其预测演化与生成观测中的视觉变化一致。摘要指出，需要同时处理宏变量构造、递归动作条件预测，以及宏层预测与视觉生成之间的一致性约束。

### 核心思路/方法
QCC-WM 使用动作响应引导宏变量构造，以支持递归的动作条件预测。方法引入共享参考商度量，用来约束预测状态与观测变化之间的一致性，使宏层预测能够为未来视觉生成提供结构化约束。具体而言，模型利用平移和旋转动作及其预测响应，通过因果抽象将局部视觉特征聚合为具有空间对应关系的宏节点，并在共享参考度量下递归预测节点内容与运动。宏层预测用于指导未来观测生成，预测运动用于传输历史外观信息；随后，将生成观测与宏层目标之间的节点级误差映射回对应空间区域进行校正，以提升视觉生成与宏层预测之间的一致性。

### 主要贡献
- 提出 QCC-WM，一种基于 Quotient-based Causal Construction 的视觉世界模型。
- 使用动作响应引导宏变量构造，支持递归的动作条件预测。
- 引入共享参考商度量，约束预测状态与观测变化之间的一致性。
- 通过因果抽象将局部视觉特征聚合为具有空间对应关系的宏节点，并递归预测节点内容与运动。
- 利用宏层预测指导未来观测生成，并通过预测运动传输历史外观信息。
- 将节点级误差映射回空间区域进行校正，以改善视觉生成与宏层预测的一致性。
- 在 US-VLA 数据集上报告：四步预测 ROI-MSE 为 0.01861；与各预测 horizon 的最佳基线相比，四步预测以及八步、十六步递归外推的 LPIPS 分别降低 48.59%、41.68%、30.23%。
- 消融与机制分析表明：运动引导的参考传输主要改善像素重建；节点级误差反馈进一步改善感知质量以及生成观测与宏层预测之间的一致性。

### 局限性
- 摘要仅报告了 US-VLA 数据集上的结果，未说明在其他数据集或真实场景中的泛化表现；摘要未提供足够信息。
- 摘要未提供模型参数量、训练成本、推理速度或计算资源需求；摘要未提供足够信息。
- 摘要未说明失败案例、误差上界或方法在复杂动作组合下的稳定性；摘要未提供足够信息。
- 摘要未提供与更多类型世界模型或生成框架的系统比较细节；摘要未提供足够信息。
- 摘要未说明宏节点数量、因果抽象的具体实现细节及其对超参数的敏感性；摘要未提供足够信息。

### 阅读优先级
中。理由：该论文与动作条件视觉世界模型、宏状态动力学和视觉生成一致性直接相关，摘要给出了明确的问题设定、方法框架和定量结果；但摘要未提供充分的实验细节、跨数据集验证和计算成本信息，是否精读应结合读者对 Embodied / Robotics / AR Applications 中世界模型与视觉生成交叉方向的兴趣决定。

</details>

<details>
<summary>Abstract</summary>

A key challenge in action-conditioned world modeling is to construct macro-states from high-dimensional observations that support recursive prediction under actions, while keeping their predicted evolution consistent with visual changes in generated observations. We propose QCC-WM, a visual world model based on Quotient-based Causal Construction. QCC-WM uses action responses to guide macro-variable construction for recursive action-conditioned prediction. A shared reference quotient measurement constrains the consistency between predicted states and observed changes, allowing macro-level predictions to provide structured constraints for future visual generation. Using translational and rotational actions and their predicted responses, the model aggregates local visual features into macro-nodes with spatial correspondence through causal abstraction, and recursively predicts node content and motion under a shared reference measurement. Macro-level predictions guide future observation generation, while predicted motion transports historical appearance information. Node-level errors between generated observations and macro-level targets are then mapped back to the corresponding spatial regions for correction, improving consistency between visual generation and macro-level predictions. On the US-VLA dataset, QCC-WM achieves an ROI-MSE of 0.01861 for four-step prediction. Compared with the best baseline at each prediction horizon, it reduces LPIPS by 48.59%, 41.68%, and 30.23% for four-step prediction and eight- and sixteen-step recursive extrapolation, respectively. Ablation studies and mechanism analyses show that motion-guided reference transport mainly improves pixel reconstruction, while node-level error feedback further improves perceptual quality and consistency between generated observations and macro-level predictions.

</details>

#### 2026-11-09 - UniOMA: Unified Optimal-Transport Multi-Modal Structural Alignment for Robot Perception

**Authors:** Xinrui Zu, Mark Hoogendoorn, Kevin Sebastian Luck, Shujian Yu
**Links:** [abs](https://arxiv.org/abs/2611.12351) - [pdf](https://arxiv.org/pdf/2611.12351)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot perception

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniOMA: Unified Optimal-Transport Multi-Modal Structural Alignment for Robot Perception
- 作者：Xinrui Zu, Mark Hoogendoorn, Kevin Sebastian Luck, Shujian Yu
- 出版日期：2026-11-09T13:04:20Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：abstract_url: https://arxiv.org/abs/2611.12351；pdf_url: https://arxiv.org/pdf/2611.12351

### 一句话总结
该论文提出 UniOMA，用基于 Gromov–Wasserstein 距离的几何感知正则项增强对比学习，以实现机器人感知中跨模态的结构对齐。

### 研究问题
机器人学习需要可泛化且对齐良好的多模态表示。摘要指出，已有方法虽尝试通过建模条件依赖或高阶统计依赖来对齐模态，但没有显式考虑跨模态的结构一致性；同时，力与触觉等模态的数据常具有不同样本密度。

### 核心思路/方法
论文在现有对比损失基础上加入几何感知的 Gromov–Wasserstein（GW）距离正则化：为每个模态编码模态内几何结构，并通过动态学习的 GW barycenter 减小跨模态结构差异，从而在实例级对比对齐之外促进结构一致性。该最优传输对齐策略被用于机器人感知任务，涉及力与触觉等较少探索的模态；摘要还称该 GW 正则项可无缝集成到大多数类 InfoNCE 目标中。

### 主要贡献
- 提出 UniOMA 多模态对齐方法，将 GW 距离正则项与对比损失结合，显式促进跨模态结构一致性。
- 利用动态学习的 GW barycenter 编码模态内几何并缩小跨模态结构差异。
- 将该对齐策略应用于机器人感知中力、触觉等模态，关注不同样本密度情形。
- 在五个机器人基准上报告了结构对齐和下游性能相对现有多模态对比基线的改进，任务包括机器人与环境状态预测。
- 指出该 GW 正则项可集成到大多数类 InfoNCE 目标中。

### 局限性
摘要未提供足够信息说明计算开销、GW barycenter 学习的稳定性、五个基准的具体构成、参与者或硬件条件、失败案例及相对基线的完整定量细节；也未提供足够信息说明该方法在摘要所述模态之外的适用边界。

### 阅读优先级
中。理由：摘要显示该工作面向机器人多模态结构对齐，并提出可插件式正则项，且声称在五个基准上改进下游性能；但当前仅有摘要与元数据，缺少实验细节与定量结果，是否值得优先精读需结合全文实验与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Achieving generalizable and well-aligned multimodal representations remains a core challenge in robot learning. While recent approaches have attempted to align modalities by modeling conditional or higher-order statistical dependencies, they do not explicitly consider the structural coherence across modalities. In this work, we propose a novel multimodal alignment method that augments existing contrastive losses with a geometry-aware Gromov--Wasserstein (GW) distance-based regularization. To this end, we encode intra-modal geometry for each modality and reduce cross-modal structural discrepancies through a dynamically learned GW barycenter, thereby encouraging structural consistency in addition to instance-level contrastive alignment. We apply this optimal-transport-based alignment strategy to robot perception tasks involving underexplored modalities such as force and tactile signals, where modality data often exhibit varying sample densities. Extensive experiments on five robotic benchmarks show that our method improves structural alignment and downstream performance over state-of-the-art multimodal contrastive baselines across a wide range of downstream tasks, including robot and environment state prediction. Moreover, our GW-based regularization can be seamlessly integrated into most InfoNCE-like objectives.

</details>

#### 2026-11-09 - GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation

**Authors:** Jinghe Wang, Xinrui Cao, Duo Wu, Chenghao Gu, Yong Zhong, Linjia Kang, Tianyi Xiong, Zhi Wang
**Links:** [abs](https://arxiv.org/abs/2611.12175) - [pdf](https://arxiv.org/pdf/2611.12175)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation
- 作者：Jinghe Wang, Xinrui Cao, Duo Wu, Chenghao Gu, Yong Zhong, Linjia Kang, Tianyi Xiong, Zhi Wang
- 出版日期：2026-11-09T10:28:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.12175 ；PDF https://arxiv.org/pdf/2611.12175 ；代码/基准 https://github.com/Notfound-JH/GEOMIND-benchmark.git

### 一句话总结
论文提出 GeoMind，一个面向桌面操作任务的结构化空间理解基准，围绕空间推理与空间记忆构建 54 个评估任务变体，并指出多种具身智能体在空间理解上的持续弱点。

### 研究问题
论文关注开放世界环境下机器人操作所需的稳健空间理解能力，具体包括两类能力：一是在复杂布局中识别目标的空间推理能力；二是在交互中持续演化场景下进行适应的空间记忆能力。作者指出，现有具身基准存在两个不足：一是常引入强视觉线索，从而绕过空间推理；二是聚焦静态场景，难以揭示智能体的空间记忆能力。因此，如何系统评估结构化空间理解成为研究问题。

### 核心思路/方法
论文提出 GeoMind 基准，以桌面操作任务为载体，系统评估结构化空间理解。GeoMind 包含 54 个评估任务变体，围绕空间推理和空间记忆组织。论文还提出一个可扩展流水线，用于自动生成和标注任务实例，并确保目标经过验证且交互可执行。论文对多种具身智能体进行了广泛评估，发现它们在空间理解上存在一致弱点：空间变化后难以保持对物体身份的跟踪，以及难以将关系或几何约束转化为可执行动作。

### 主要贡献
- 提出 GeoMind，一个面向机器人操作中结构化空间理解的系统基准，包含 54 个评估任务变体，覆盖空间推理与空间记忆。
- 提出可扩展的任务实例自动生成与标注流水线，强调目标验证与交互可执行性。
- 对多种具身智能体进行评估，揭示其在空间理解上的一致弱点，尤其是空间变化后的身份跟踪困难，以及关系/几何约束到可执行动作的转化困难。
- 公开发布 GeoMind 基准（代码链接已给出）。

### 局限性
- 论文摘要仅给出基准规模，即 54 个评估任务变体；未提供任务具体分布、难度分层、场景数量、数据规模等细节。
- 摘要未提供所评估具身智能体的具体名称、数量、模型类型或实验设置。
- 摘要未提供量化评估结果、指标定义或对比基线细节。
- 摘要未说明自动生成与标注流水线的具体技术实现、验证方式或可扩展性度量。
- 摘要未讨论基准本身的局限，例如仿真与真实场景差距、任务覆盖范围等；“摘要未提供足够信息”。

### 阅读优先级
中。理由：该论文与具身智能、机器人操作和空间理解评估直接相关，且明确指出现有基准在空间推理与空间记忆评估上的缺口，并公开基准，对相关方向有参考价值。但摘要未提供具体实验设置、量化结果和基准细节，是否值得深入阅读取决于读者对空间理解评测基准或桌面操作任务的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation has advanced rapidly in mapping visual observations and language instructions to actions. However, reliable manipulation in open-world environments requires robust spatial understanding: the ability to identify targets in complex layouts (spatial reasoning) and adapt to scenes that continuously evolve through interaction (spatial memory). Yet existing embodied benchmarks fall short in evaluating spatial understanding: they often introduce strong visual cues that bypass spatial reasoning, and focus on static scenes that offer little insight into an agent's capacity for spatial memory. To address this gap, we introduce GeoMind, a systematic benchmark for structured spatial understanding through tabletop manipulation. GeoMind comprises 54 evaluated task variants organized around spatial reasoning and spatial memory. It also incorporates a scalable pipeline that automates the generation and annotation of task instances with verified targets and executable interactions. Extensive evaluations across diverse embodied agents reveal their consistent weaknesses in spatial understanding. Our findings highlight that these agents struggle to track identities after spatial changes and convert relational or geometric constraints into executable actions. We release the GeoMind benchmark at https://github.com/Notfound-JH/GEOMIND-benchmark.git.

</details>

#### 2026-11-09 - OASIS: Optimization-Aware Subgoal Inference with Safety Constraints for Autonomous Mobile Robot Navigation

**Authors:** Arian Hajizadeh, Javad Pourrafi Arabani, Negar Shenavar, Sana Bashiri, Seyed Majid Esmailzadeh
**Links:** [abs](https://arxiv.org/abs/2611.11996) - [pdf](https://arxiv.org/pdf/2611.11996)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OASIS: Optimization-Aware Subgoal Inference with Safety Constraints for Autonomous Mobile Robot Navigation
- 作者：Arian Hajizadeh, Javad Pourrafi Arabani, Negar Shenavar, Sana Bashiri, Seyed Majid Esmailzadeh
- 出版日期：2026-11-09T07:25:13Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.11996 ；PDF https://arxiv.org/pdf/2611.11996

### 一句话总结
OASIS 是一个分层移动机器人导航框架：高层策略用强化学习生成局部子目标，低层用带运动约束、几何避碰约束和高阶控制屏障函数约束的非线性模型预测控制跟踪子目标，并把每次子目标区间内的控制器优化结果反馈给下一次策略决策，以缓解“几何上合理但控制上不可行”的子目标问题。

### 研究问题
动态环境中的移动机器人导航需要同时满足三方面要求：朝目标推进、遵守运动限制、避开周围障碍。已有的“学习子目标 + 模型预测控制”方案中，子目标策略能够引导模型预测控制超越其局部预测时域，但摘要指出一个关键问题：几何上合适的子目标不一定能对应一个可成功求解的控制问题。论文要解决的问题即如何让子目标生成考虑底层控制优化的实际可行性，而不仅是几何位置。

### 核心思路/方法
论文提出 OASIS 分层导航框架，主要由以下部分构成：

- **高层子目标生成**：用基于 Soft Actor–Critic 训练的强化学习策略生成局部子目标。
- **低层跟踪控制**：由非线性模型预测控制器跟踪子目标，约束包括运动限制、几何碰撞避免约束，以及嵌入的高阶控制屏障函数约束。
- **优化状态反馈**：将每个子目标区间内控制器优化的结果进行汇总，并在策略下一次决策时提供给策略，且不需要额外的优化调用。也就是说，子目标策略在生成下一子目标时能够“感知”上一段子目标对应的优化结果。
- **评估设置**：在五个包含静态和移动障碍物的导航场景中评估，覆盖密集交互和感知不确定性；对比对象包括分层控制变体和直接目标控制变体；并做了三个训练种子的匹配比较，以及与“除缺少优化状态输入外其余相同的层级结构”的对比。

### 主要贡献
- 提出 OASIS 分层导航框架，将控制器优化结果纳入强化学习子目标生成，使子目标推断具有优化感知能力，且反馈机制不引入额外优化调用。
- 在低层非线性模型预测控制中同时考虑运动限制、几何碰撞避免约束以及高阶控制屏障函数约束，用于支持安全约束下的子目标跟踪。
- 在五个含静态与移动障碍物的导航场景（含密集交互与感知不确定性）中进行评估，报告 OASIS 获得最高的总体导航成功率。
- 通过三个训练种子的匹配比较，报告相对于“仅缺少优化状态输入、其余相同”的层级结构具有一致的成功率优势。
- 在选定策略比较中报告主要优化失败更少，同时平均控制器时间相近。

### 局限性
- 摘要未提供足够信息说明所对比各方法的具体实现细节、基线命名与参数配置。
- 摘要未提供足够信息说明五个导航场景的具体环境定义、障碍物密度指标与感知不确定性建模方式。
- 摘要未提供足够信息给出成功率、优化失败次数和控制器时间的具体数值，仅给出相对比较结论。
- 摘要未提供足够信息说明高阶控制屏障函数的具体形式、约束参数以及安全性的理论保证。
- 摘要未提供足够信息说明方法在真实机器人平台上的验证情况，评估似乎限于所述五个导航场景。
- 摘要未提供足够信息说明计算开销的完整分解、训练成本以及对不同控制器或策略骨干的泛化性。

### 阅读优先级
**中**。理由：该论文关注“学习子目标与底层优化可行性脱节”这一在分层导航中较实际的问题，并提出把控制器优化结果反馈给子目标策略的轻量机制，且包含多场景、多种子与消融式匹配比较，对分层导航与安全约束控制方向有参考价值。但摘要未给出具体性能数值、安全性理论保证和实机验证信息，若读者重点关注定量结果或真实部署，需要进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Navigation in dynamic environments requires mobile robots to make progress toward their goals while respecting motion limits and avoiding surrounding obstacles. Learned subgoal policies can guide model predictive control beyond its local prediction horizon, but a geometrically suitable subgoal does not necessarily lead to a successfully solved control problem. This paper proposes OASIS, a hierarchical navigation framework that incorporates recent optimization outcomes into reinforcement learning-based subgoal generation. A high-level policy trained using Soft Actor--Critic generates local subgoals, while a nonlinear model predictive controller tracks them subject to motion limits, geometric collision-avoidance constraints, and embedded high-order control barrier function constraints. The outcomes of controller optimizations over each subgoal interval are summarized and provided to the policy at its next decision, without requiring additional optimization calls. The framework is evaluated in five navigation scenarios with static and moving obstacles, including dense interactions and sensing uncertainty. Comparisons with hierarchical and direct-goal control variants show that OASIS achieves the highest aggregate navigation success. Matched comparisons across three training seeds further show a consistent success advantage over the otherwise identical hierarchy without optimization-status input. The selected-policy comparison also shows fewer primary optimization failures with similar mean controller time.

</details>

#### 2026-11-08 - Feel My Focus: Gaze-Triggered Digital Twin Creation for Remote Collaboration

**Authors:** Shih-Yu Ma, Suibi Che-Chuan Weng, Ming-Yuan Pai, Tom Yeh, Ellen Yi-Luen Do
**Links:** [abs](https://arxiv.org/abs/2611.11640) - [pdf](https://arxiv.org/pdf/2611.11640)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mixed reality, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Feel My Focus: Gaze-Triggered Digital Twin Creation for Remote Collaboration
- 作者：Shih-Yu Ma, Suibi Che-Chuan Weng, Ming-Yuan Pai, Tom Yeh, Ellen Yi-Luen Do
- 出版日期：2026-11-08T21:47:21Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.11640 ；PDF https://arxiv.org/pdf/2611.11640

### 一句话总结
论文提出“Feel My Focus”这一注视触发的混合现实演示系统，将持续视觉注意作为生成动作，在远程协作中快速创建并共享轻量级 3D 数字孪生。

### 研究问题
远程协作中如何让远端伙伴快速获得并就地讨论物理对象的三维表示；以及如何把注视从“指向/引用”工具转变为触发数字孪生生成的主动作。摘要还关注此类注视触发生成系统在真实协作场景中的设计权衡、失败模式与用户控制问题。

### 核心思路/方法
系统将“持续注视”视为生成性动作：当用户注视某个物理对象时，触发单图像采集、注意力引导的分割以及单次（one-shot）3D 重建，使远端伙伴能够就地查看并讨论该对象。系统集成注视追踪眼镜、模块化分割与重建服务，以及用于运行时流式传输与交互的 MR 客户端。设计上优先考虑响应性与体验连续性，而非光度保真度。摘要报告了公开演示中的观察，并讨论设计权衡、失败模式与用户控制考虑。

### 主要贡献
- 提出将持续视觉注意作为生成动作的注视触发数字孪生创建方式，区别于仅把注视用作参考指针的系统。
- 构建了面向远程协作的轻量级 3D 数字孪生快速创建与共享演示系统，集成注视追踪眼镜、模块化分割/重建服务与 MR 客户端。
- 明确以响应性和体验连续性为优先的设计取向，而非追求光度保真度。
- 基于公开演示报告设计权衡、失败模式与用户控制方面的观察。

### 局限性
- 摘要未提供足够信息说明定量实验结果、用户研究规模或统计评估。
- 摘要未提供足够信息说明重建精度、延迟、分割质量等具体性能指标。
- 摘要未提供足够信息说明失败模式的具体类型与发生条件。
- 摘要未提供足够信息说明用户控制机制的具体设计细节。
- 摘要未提供足够信息说明系统在不同对象、光照或协作场景下的泛化能力。

### 阅读优先级
中。理由：该工作涉及注视交互、MR 远程协作与轻量级 3D 数字孪生生成，问题定位和设计取向清晰，适合关注人机交互与 AR/MR 协作系统的读者；但摘要仅报告公开演示观察，未给出定量实验或详细评估信息，若需要严谨性能对比或用户研究证据，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

We present Feel My Focus, a gaze-triggered mixed reality (MR) demonstration that enables rapid creation and sharing of lightweight 3D digital twins during remote collaboration. Unlike systems that use gaze primarily as a referential pointer, Feel My Focus treats sustained visual attention as a generative action: a fixation on a physical object initiates single-image capture, attention-guided segmentation, and one-shot 3D reconstruction, allowing a remote partner to inspect and discuss the object in situ. The system integrates gaze-tracking glasses, modular segmentation and reconstruction services, and an MR client for runtime streaming and interaction. This design prioritizes responsiveness and experiential continuity over photometric fidelity. We report observations from a public demonstration, highlighting design trade-offs, failure modes, and user control considerations for deploying gaze-triggered generative systems in real-world collaborative settings.

</details>

#### 2026-11-08 - ScanDreamer: A Map-Grounded World Model for Quadrotor Navigation

**Authors:** Yunyi Gao, Yixing Shi, Yize Liu, Hai-Duong Tran, Nhat-Hoang P. Nguyen, Shuai Wang, Yi Deng, Shengming Liu, Sim Kuan Goh, Duc-Thinh Pham, Sameer Alam
**Links:** [abs](https://arxiv.org/abs/2611.11605) - [pdf](https://arxiv.org/pdf/2611.11605)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ScanDreamer: A Map-Grounded World Model for Quadrotor Navigation
- 作者：Yunyi Gao, Yixing Shi, Yize Liu, Hai-Duong Tran, Nhat-Hoang P. Nguyen, Shuai Wang, Yi Deng, Shengming Liu, Sim Kuan Goh, Duc-Thinh Pham, Sameer Alam
- 出版日期：2026-11-08T20:33:43Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.11605 ；PDF https://arxiv.org/pdf/2611.11605

### 一句话总结
ScanDreamer 是一种以在线二维扫描记忆地图为条件的世界模型导航方法，用于前视深度相机四旋翼在未知杂乱环境中的避障导航，并在摘要报告的 Isaac Sim 评测中显著优于 AirDreamer。

### 研究问题
四旋翼在建筑与隧道巡检等场景中，需要依靠前向深度相机在未知杂乱环境中导航；有限的视场会限制场景理解与避障能力。近期基于世界模型的智能体（如 AirDreamer）通过想象经验学习导航，但摘要指出其仍存在数据需求大、缺乏显式几何记忆以及对相机可观测范围缺乏感知的问题。

### 核心思路/方法
- 利用深度图像与飞行器位姿构建在线二维扫描记忆地图（scan-memory map）。
- 世界模型、actor 与 critic 均以该地图为条件；地图还用于定义测地进度奖励（geodesic progress reward）。
- 引入前向锥惩罚（forward-cone penalty），抑制相机视线方向之外的水平运动。
- 在想象（imagination）过程中，在冻结地图上传播四旋翼位姿，并从地图几何中导出进度与撞墙接触信号。

### 主要贡献
- 提出 ScanDreamer：将显式在线扫描记忆地图与基于地图的世界模型想象相结合的四旋翼导航方法。
- 将地图同时用于策略/价值条件化、进度奖励定义以及想象阶段的几何信号推导。
- 增加前向锥惩罚，使运动与相机可观测方向保持一致。
- 摘要报告的训练预算为 80 万环境步（单 GPU 5.5 小时）；在 NVIDIA Isaac Sim 上跨未见布局与参数范围评测 1560 个回合、三个随机种子：成功率为 96.3 ± 0.3%、碰撞率为 3.6 ± 0.3%，而同在线交互预算下 AirDreamer 为 59.6 ± 3.0% 成功率与 28.8 ± 2.8% 碰撞率；移除前向锥惩罚后碰撞率升至 9.9 ± 3.1%。
- 摘要称结果表明显式地图记忆、地图 grounded 想象与感知感知运动的结合可显著提升导航性能与数据效率，并提供源代码链接。

### 局限性
- 摘要未提供足够信息说明方法在真实飞行器、真实传感器噪声与真实环境中的验证情况。
- 摘要未提供足够信息说明二维扫描记忆地图在三维复杂结构（如多层建筑、复杂隧道）中的表达上限与失效情形。
- 摘要未提供足够信息说明对不同相机视场、位姿估计误差、地图分辨率等参数的敏感性。
- 摘要未提供足够信息说明与更多基线方法的系统比较及消融实验的完整细节。
- 摘要未提供足够信息说明计算/内存开销随地图规模增长的扩展性。

### 阅读优先级
高。理由：摘要给出了明确的问题动机、方法要点、训练预算与多随机种子评测指标，并与同类世界模型方法进行了同交互预算对比，还报告了关键组件（前向锥惩罚）的消融结果；对四旋翼导航、世界模型与感知感知运动方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Quadrotors inspecting buildings and tunnels must navigate unknown clutter with a forward-facing depth camera whose limited field of view constrains scene understanding and collision-avoiding navigation. Recent world-model agents learn navigation through imagined experience (e.g., AirDreamer), but remain data-intensive and often lack explicit geometric memory and awareness of what the camera can observe. We propose ScanDreamer, a map-grounded world model that constructs an online 2D scan-memory map from depth images and vehicle pose. Our world model, actor, and critic are conditioned on this map, which also defines a geodesic progress reward. Moreover, a forward-cone penalty discourages horizontal motion outside the camera's viewing direction. During imagination, ScanDreamer propagates the quadrotor pose over a frozen map and derives progress and wall-contact signals from the mapped geometry. We train ScanDreamer for 0.8 million environment steps (5.5 h on one GPU) and evaluate it in NVIDIA Isaac Sim over 1560 episodes spanning unseen layouts and parameter ranges. Across three seeds (mean $\pm$ SD), ScanDreamer achieves 96.3 $\pm$ 0.3% success with 3.6 $\pm$ 0.3% collision, compared with 59.6 $\pm$ 3.0% success and 28.8 $\pm$ 2.8% collision for AirDreamer at the same online-interaction budget. Removing the forward-cone penalty increases collisions to 9.9 $\pm$ 3.1%. These results show that combining explicit map memory, map-grounded imagination, and perception-aware motion substantially improves navigation performance and data efficiency. The source code is available at https://github.com/WANGSHUAIzzzz/ScanDreamer.

</details>

#### 2026-11-08 - How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding

**Authors:** Gengyuan Zhang, Xiao Han, Shijie Zhou, Abdullah Koukash, Jingpei Wu, Jindong Gu, Yuqicheng Zhu, Nassir Navab, Volker Tresp, Ghazal Ghazaei
**Links:** [abs](https://arxiv.org/abs/2611.11437) - [pdf](https://arxiv.org/pdf/2611.11437)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding
- 作者：Gengyuan Zhang, Xiao Han, Shijie Zhou, Abdullah Koukash, Jingpei Wu, Jindong Gu, Yuqicheng Zhu, Nassir Navab, Volker Tresp, Ghazal Ghazaei
- 出版日期：2026-11-08T15:00:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.11437) / [PDF](https://arxiv.org/pdf/2611.11437)

### 一句话总结
论文提出两阶段评估框架，先以 SurgKnowBench 诊断通用多模态大模型在手术场景理解上的能力边界，再以 SurgAgentGym 检验通用智能体能否通过工具介导的证据使用在推理阶段提升手术理解。

### 研究问题
摘要指出，由于手术数据稀缺且评估协议碎片化，对通用多模态大语言模型（MLLMs）在手术场景理解方面的评估仍然有限。论文关注：当前预训练模型已具备怎样的手术理解能力、边界在哪里；以及在不额外进行手术训练的前提下，通用 MLLM 智能体能否通过工具使用在推理时改善手术场景理解。

### 核心思路/方法
论文采用两阶段评估框架：
1. **Stage I — SurgKnowBench**：一个诊断性基准，统一整合跨不同手术流程和任务的公开手术数据集，并评估闭源与开源 MLLMs，以刻画预训练手术能力的边界。
2. **Stage II — SurgAgentGym**：受外科训练中“脚手架式”教学启发，构建一个智能体环境，让通用 MLLM 智能体在手术任务中使用对 SurgWiki 的有界知识搜索和通用视觉定位，从而评估通用智能体能否在推理阶段通过工具介导的证据使用提升手术理解，而无需额外手术训练。

### 主要贡献
- 提出两阶段评估框架，用于手术场景理解下的通用模型与智能体评测。
- 构建 SurgKnowBench，统一公开手术数据集并跨流程、跨任务评估 MLLMs，揭示当前模型保留部分视觉先验，但在关系理解、流程理解和工作流评估方面仍然薄弱。
- 构建 SurgAgentGym，提供智能体化评测环境，验证通用智能体可通过有界知识搜索与通用视觉定位在推理阶段使用证据。
- 实验结果显示，智能体推理主要缩小了感知密集型任务的差距，而细粒度定位和专家式评估仍是持续瓶颈；据此提出面向智能体化手术理解的未来研究方向。

### 局限性
- 论文实验的具体数据集规模、模型清单、评价指标数值等细节：摘要未提供足够信息。
- SurgWiki 的构建方式与知识范围：摘要未提供足够信息。
- “有界知识搜索”的具体约束机制：摘要未提供足够信息。
- 智能体推理提升幅度的定量结果：摘要未提供足够信息。
- 是否涉及真实临床场景验证或安全性分析：摘要未提供足够信息。

### 阅读优先级
**中**。理由：该论文聚焦通用多模态大模型与智能体在手术场景理解中的评测与推理阶段增强，属于 Embodied / Robotics / AR Applications 方向，问题定义清晰且提出两阶段评测框架；但摘要未给出具体实验规模与定量细节，若研究兴趣不在手术场景理解、多模态智能体评测或医疗具身应用，优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Evaluating general-purpose multimodal large language models (MLLMs) for surgical scene understanding remains limited due to scarce surgical data and fragmented evaluation protocols. We address these challenges through a two-stage evaluation framework for surgical scene understanding. In Stage I, we introduce SurgKnowBench, a diagnostic benchmark that harmonizes public surgical datasets across procedures and tasks and evaluates proprietary and open-source MLLMs to map the boundary of pretrained surgical competence. SurgKnowBench reveals that current models retain partial visual priors but remain weak on relational and procedural understanding and workflow assessment. Building on this failure frontier and motivated by the scaffolded nature of surgical training, we introduce SurgAgentGym, an agentic environment where general-purpose MLLM agents can use bounded knowledge search over SurgWiki and general-purpose visual grounding for surgical tasks. SurgAgentGym evaluates whether generalist agents can improve surgical understanding at inference time through tool-mediated evidence use, without additional surgical training. Our results show that agentic inference narrows the gap mainly for perception-heavy tasks, while fine-grained localization and expert-style assessment remain persistent bottlenecks. This opens a path toward future studies of agentic surgical understanding.

</details>

#### 2026-11-08 - DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight

**Authors:** Zhongxi Chen, Yi Yang, Xinyi Chen, Mingzhe Ye, Yaping Li, Zhihong Liu, Congsheng Xu, Haonan Wang, Zhijie Deng
**Links:** [abs](https://arxiv.org/abs/2611.11166) - [pdf](https://arxiv.org/pdf/2611.11166)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight
- 作者：Zhongxi Chen, Yi Yang, Xinyi Chen, Mingzhe Ye, Yaping Li, Zhihong Liu, Congsheng Xu, Haonan Wang, Zhijie Deng
- 出版日期：2026-11-08T06:14:36Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.11166 ；PDF https://arxiv.org/pdf/2611.11166 ；项目页 https://dexforesight.github.io/

### 一句话总结
DexForesight 通过将动作条件下的空间世界模型隐式注入灵巧操作策略的潜在空间，使策略在部署时无需深度输入或显式未来预测即可获得空间预见能力。

### 研究问题
灵巧操作需要对周围场景和机器人手部具备丰富的空间预见能力。现有 world-action 模型通常通过显式的未来预测来获取这类预测知识，论文关注的是如何以隐式方式获得空间预见，并避免部署阶段依赖显式未来预测或深度输入。

### 核心思路/方法
- 训练阶段：从离线场景深度、运动学手部几何和演示轨迹中学习一个动作条件下的空间世界模型。
- 世界模型预测两类目标：3D 手部点运动和视觉特征变化，用以捕捉关节式手部动力学以及演示动作下的场景变化，包括被相机遮挡的手指运动。
- 策略对齐：冻结世界模型，将策略查询与世界模型的预测性世界查询对齐，把学到的空间动力学转移到策略潜在表示中，并用其条件化动作生成。
- 部署阶段：仅保留策略，策略以 RGB 观测、语言和机器人状态为输入，不需要深度输入，也不进行显式未来预测。

### 主要贡献
- 提出 DexForesight 框架，以隐式方式将空间预见注入灵巧策略潜在空间，而非依赖显式未来预测。
- 构建动作条件下的空间世界模型，联合建模 3D 手部点运动与视觉特征变化，并覆盖被遮挡手指的运动。
- 通过冻结世界模型并对齐策略查询与世界查询，实现空间动力学知识向策略的迁移。
- 摘要报告：在 11 个 DexJoCo 仿真任务上，将基础策略总体成功率从 49.4% 提升至 60.5%；在三个真实机器人灵巧操作任务上达到 58.3% 成功率，最强基线为 50.0%。

### 局限性
- 摘要未提供足够信息说明世界模型训练数据规模、离线数据覆盖范围及其对分布外场景的泛化表现。
- 摘要未提供足够信息说明真实机器人实验的任务细节、基线设置、评估样本量与统计显著性。
- 摘要未提供足够信息说明方法对深度数据质量、手部运动学模型准确性或相机遮挡程度的敏感性。
- 摘要未提供足够信息说明训练与部署的计算开销、推理延迟及实时性表现。
- 摘要未提供足够信息说明失败案例类型及方法在更长时序或更复杂接触任务中的表现。

### 阅读优先级
中。理由：论文聚焦灵巧操作中的空间预见与策略学习，给出了仿真与真实机器人成功率对比，问题和方法描述较清晰；但摘要未展开实验细节、基线构成与局限性分析，若关注灵巧操作或世界模型与策略结合方向，可作为中优先级阅读并进一步查看原文实验部分。

</details>

<details>
<summary>Abstract</summary>

Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand. Existing world-action models often acquire such predictive knowledge through explicit future prediction. We introduce DexForesight, a framework that learns spatial foresight implicitly by injecting dynamics-aware world representations into the latent space of a dexterous policy. During training, DexForesight learns an action-conditioned spatial world model from offline scene depth, kinematic hand geometry, and demonstration trajectories. The world model predicts 3D hand-point motion and visual feature changes, capturing both articulated hand dynamics and scene changes under demonstrated actions, including the motion of fingers occluded from the cameras. We then freeze the world model and align policy queries with its predictive world queries, transferring the learned spatial dynamics into policy latents and using them to condition action generation. At deployment, only the policy is retained, operating on RGB observations, language, and robot state without depth input or explicit future prediction. On 11 DexJoCo simulation tasks, DexForesight improves the overall success rate of the base policy from 49.4% to 60.5%. On three real-robot dexterous manipulation tasks, DexForesight achieves 58.3% success, compared with 50.0% for the strongest baseline.Project page https://dexforesight.github.io/

</details>

#### 2026-11-08 - MOSU2: Long-range Navigation System with Multi-modal Scene Understanding

**Authors:** Jing Liang, Zhenyu Hou, Senthurbavan Kirubaharan, Md Safwan Mondal, Ashok Gudivada, Xuesu Xiao, Dinesh Manocha
**Links:** [abs](https://arxiv.org/abs/2611.11148) - [pdf](https://arxiv.org/pdf/2611.11148)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MOSU2: Long-range Navigation System with Multi-modal Scene Understanding
- 作者：Jing Liang, Zhenyu Hou, Senthurbavan Kirubaharan, Md Safwan Mondal, Ashok Gudivada, Xuesu Xiao, Dinesh Manocha
- 出版日期：2026-11-08T05:41:39Z
- 分类：Embodied / Robotics / AR Applications（次要分类：摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2611.11148) / [PDF](https://arxiv.org/pdf/2611.11148)

### 一句话总结
MOSU2 是一个面向公共户外长距离导航的两阶段轨迹选择系统，通过第一阶段情境推理判断何时需要补充证据，仅在交互未解决时触发第二阶段检索几何与动态信息，从而在实时性与决策正确性之间取得平衡。

### 研究问题
机器人在公共户外空间长距离行进时，不仅要避障，还需保持在适合自身机动性的地形上，并判断何时前进、让行或绕行行人、骑行者、车辆、交通信号及临时限制。这类决策的正确性常取决于场景如何演化（如驶近的车是否在减速、骑行者是否会横穿路径）。视觉语言模型（VLM）能解读此类线索，但其推理所基于的图像缺乏度量几何与运动信息；而每一步都提供这些证据对实时导航而言过慢，手工设计的触发条件又无法覆盖户外情境的开放性多样性。

### 核心思路/方法
- **两阶段轨迹选择**：第一阶段进行情境推理，判断何时需要额外证据以及需要检索什么；仅当某一交互仍未解决时，第一阶段才触发第二阶段。
- **第二阶段证据检索与对齐**：检索几何与动态信息，并将其与场景上下文对齐，以做出导航决策。
- **整体流程**：沿用 MOSU 的思路，从基于 GPS 的路线规划出发，通过多模态可通行性分析过滤候选轨迹，再选择一条轨迹驱动机器人移动。
- **真实世界实验场景**：停止手势、施工现场、人行横道，以及与车辆、骑行者、行人共享的道路。

### 主要贡献
- 提出 MOSU2 长距离导航系统，采用两阶段轨迹选择机制，由第一阶段的情境推理自适应地决定是否触发第二阶段的几何与动态证据检索。
- 在真实世界实验中，相较其单图像前身 MOSU，平均导航成功率从 61.8% 提升至 94.2%，条件检测准确率从 72.2% 提升至 91.4%，代价是约 2.2 倍的平均决策延迟。
- 摘要提及项目网站，但未提供更多贡献细节。

### 局限性
- 摘要未提供足够信息说明系统在更大规模、更多样化环境中的泛化能力。
- 摘要未提供足够信息说明 2.2 倍决策延迟在具体硬件平台与实时性要求下是否可接受。
- 摘要未提供足够信息说明两阶段触发机制的误触发/漏触发情况及其对失败案例的影响。
- 摘要未提供足够信息说明实验规模、路线长度、试次数量与基线设置等细节。
- 摘要未提供足够信息说明对 VLM 的依赖程度、模型类型及推理开销。

### 阅读优先级
中。理由：该工作针对户外长距离导航中“何时调用昂贵多模态证据”的实际问题，给出了两阶段自适应触发思路，并在真实世界场景中报告了较明显的成功率与条件检测提升，对具身导航与机器人户外部署有参考价值；但摘要未披露实验规模、硬件与失败模式等关键细节，需阅读全文才能判断其可复现性与泛化性。

</details>

<details>
<summary>Abstract</summary>

Robots that travel long distances through public outdoor spaces must do more than avoid obstacles: they must remain on terrain suited to their mobility and decide when to proceed, yield, or detour around pedestrians, cyclists, vehicles, traffic signals, and temporary restrictions. These decisions are difficult because their correctness often depends on how a scene evolves, such as whether an approaching car is slowing or a cyclist will cross the robot's path. Vision-language models (VLMs) can interpret such cues, but they reason over images that lack metric geometry and motion. Supplying this evidence at every step is too slow for real-time navigation, and hand-crafted triggers cannot anticipate the open-ended variety of outdoor situations. We present MOSU2, a long-range navigation system with two-stage trajectory selection, in which first-stage contextual reasoning determines when additional evidence is needed and what to retrieve. Only when an interaction remains unresolved does the first stage trigger the second stage to retrieve geometric and dynamic information and align it with scene context to make navigation decisions. Building on MOSU, MOSU2 follows routes from GPS-based route planning and filters candidate trajectories through multi-modal traversability analysis before selecting a trajectory to move the robot. In real-world experiments spanning stop gestures, construction sites, crosswalks, and roads shared with vehicles, cyclists, and pedestrians, MOSU2 raises mean navigation success from 61.8% to 94.2% and condition-detection accuracy from 72.2% to 91.4% over its single-image predecessor, at about 2.2 times its mean decision latency. Project website: https://jinggm.github.io/mosu2/

</details>

#### 2026-11-08 - ObjectWorld: Scaling Object-Centric World Models with A Large-Scale 3D Full-Object Flow Dataset

**Authors:** Haonan Chen, Sicheng Isabella Lu, Haitian Li, Jiajin Wu, Hexiang Wei, Jiawei Zhang, Xin Fei, Yiwen Hou, Chenrui Tie, Chongkai Gao, Sheng Wang, Lin Shao
**Links:** [abs](https://arxiv.org/abs/2611.11085) - [pdf](https://arxiv.org/pdf/2611.11085)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ObjectWorld: Scaling Object-Centric World Models with A Large-Scale 3D Full-Object Flow Dataset
- 作者：Haonan Chen, Sicheng Isabella Lu, Haitian Li, Jiajin Wu, Hexiang Wei, Jiawei Zhang, Xin Fei, Yiwen Hou, Chenrui Tie, Chongkai Gao, Sheng Wang, Lin Shao
- 出版日期：2026-11-08T02:55:15Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.11085 ；PDF https://arxiv.org/pdf/2611.11085

### 一句话总结
论文提出一种覆盖目标物体完整表面（含遮挡区域）的“3D full-object flow”物体中心运动表示，并构建大规模数据集与可扩展标注流程，用于训练以图像和任务描述为输入、预测完整物体几何上稠密流的世界模型。

### 研究问题
如何为可扩展的机器人操作学习一个既能在规模上获得监督、又能对下游控制保持可操作性的中间运动表示；以及如何缓解完整 3D 物体运动的大规模监督数据稀缺问题。摘要指出，从大规模视觉数据进行生成式世界建模是有前景的路径，但需要合适的中间表示与规模化监督。

### 核心思路/方法
- 提出“3D full-object flow”：一种物体中心运动表示，为目标物体完整表面上的点分配稠密 3D 轨迹，包括被遮挡区域。
- 将可见表面的 object flow 扩展到完整物体几何，使完整物体运动显式化，并统一适用于刚性与可变形物体。
- 构建 1210 小时 full-object flow 数据集，整合多样真实世界视频与物理仿真；提供可扩展标注流程，从真实观测中恢复完整物体运动，并给出用于系统评估标注质量的质量指标。
- 训练一个世界模型：输入图像与任务描述，在重建的物体几何上预测稠密 full-object flow。

### 主要贡献
- 提出 3D full-object flow 这一物体中心、覆盖完整表面（含遮挡）的稠密 3D 运动表示，并声称统一适用于刚性与可变形物体。
- 发布 1210 小时 full-object flow 数据集，整合真实视频与物理仿真，并提供可扩展标注流程与标注质量指标。
- 训练以图像和任务描述为输入、预测稠密 full-object flow 的世界模型；摘要报告实验显示可靠的标注质量、可随数据扩展的流预测，以及在新场景和机器人本体上的有效下游操作。

### 局限性
- 摘要未提供足够信息说明具体实验设置、基线对比、失败案例与定量指标细节。
- 摘要未提供足够信息说明标注流程的具体技术细节、质量指标定义及标注误差范围。
- 摘要未提供足够信息说明方法在真实机器人部署中的实时性、泛化边界与安全性。
- 摘要未提供足够信息说明数据集覆盖的物体类别、场景分布与仿真到真实的差距程度。

### 阅读优先级
高。理由：论文同时提出新的物体中心完整 3D 运动表示、大规模数据集与标注流程，并面向机器人操作的下游控制；摘要明确给出数据规模（1210 小时）与跨新场景、跨机器人本体的实验结论，属于该方向中信息密度较高的系统级工作。但需注意当前仅有摘要与元数据，具体实验细节需查阅原文。

</details>

<details>
<summary>Abstract</summary>

Generative world modeling from large-scale visual data offers a promising path toward scalable robot manipulation. This calls for an intermediate representation that can be supervised at scale and remains actionable for downstream control. We propose 3D full-object flow, an object-centric motion representation that assigns dense 3D trajectories to points across the complete surface of a target object, including its occluded regions. By extending visible-surface object flow to the full object geometry, this representation makes complete object motion explicit and applies uniformly to both rigid and deformable objects. To realize the potential of this representation at scale, we introduce a 1210-hour full-object flow dataset that addresses the scarcity of large-scale supervision for complete 3D object motion. The dataset integrates diverse real-world videos and physical simulations, with a scalable annotation pipeline for recovering full-object motion from real-world observations and quality metrics for systematically assessing annotation quality. We then train a world model that takes an image and a task description as input and predicts dense full-object flow over the reconstructed object geometry. Experiments show reliable annotation quality, data-scalable flow prediction, and effective downstream manipulation across novel scenes and robot embodiments. Project website with additional results and videos: https://nus-lins-lab.github.io/ObjectWorld/.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
