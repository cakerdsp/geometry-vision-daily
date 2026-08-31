# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：29
- 分类分布：
  - Embodied / Robotics / AR Applications: 10
  - 3D Reconstruction & Multi-view Geometry: 10
  - Neural Scene Representations & Rendering: 4
  - Geometry Foundation Models: 4
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **3D 高斯泼溅（3DGS）生态进入“工程化”与“实用化”阶段**  
   本批论文中 3DGS 相关的工作不再停留在基础重建质量上，而是围绕部署痛点展开：压缩（KISS-GS，85x–319x 体积缩减）、瞬态干扰物过滤（Per-View Gaussian Predictions 的免训练方案）、多物体移除（CoGeo-GS）、水下跨场景评测（Gaussian Splatting Underwater）、多智能体 SLAM（CGS-SLAM）。这表明 3DGS 正从“能做重建”转向“如何好用、快用、稳用”。

2. **几何基础模型（VGGT、LRM、Depth Pro 等）成为跨任务“底座”**  
   本批论文中，VGGT 被用于玻璃表面检测（Glass Surface Detection）与多智能体 SLAM 子图对齐（CGS-SLAM）；LRM 被用于单图人-物交互重建（MILO）；Depth Pro 被用于单目尺度恢复（CGS-SLAM）。单图/少图几何推理的统一模型正在渗透重建、检测与机器人任务，且与 3DGS 深度耦合。

3. **世界模型与机器人策略的“三维化”与“结构化”**  
   4DGS-WAM 用 4DGS 显式分离动态对象与静态背景，只预测动态部分；GaussianDream++ 将世界状态/预测令牌直接插入 VLA 骨干；UCAG-P 以相机中心几何动作空间统一异构具身数据；Instruct-to-Act 将 VLM 规划与世界模型控制器解耦。机器人学习正从 2D 视觉/隐空间预测转向显式 3D/4D 结构化世界建模。

4. **“数据级/训练级”优化日益受重视，与“模型级”创新并行**  
   出现一批不修改网络架构、在数据或训练层面创新以提高泛化或精度的思路：几何驱动的主轴对齐旋转表示（A Geometry-Driven…Pose Estimation）、自监督模糊关键点检测的两阶段几何预训练（SSMB）、前馈 3DGS 中免训练的干扰物过滤、运动模糊图像不需要去模糊的自监督检测。说明在架构创新之外，数据表征与训练范式本身已成为值得投入的方向。

5. **AI for Science/特定场景的评测类工作增多**  
   本批出现多篇为特定应用场景做系统性评测的论文：实验室物体全息可视化四种重建方法对比（Comparative Evaluation of 3D Reconstruction）、水下不同浊度/光照条件 3DGS 跨场景对照（Gaussian Splatting Underwater）、实验室机器人神经重建跨平台基准（Cross-Platform Benchmark）。这类工作为领域提供了稀缺的“可控变量比较”证据，是方法社区与领域应用之间的桥梁。


#### 技术路线观察

- **几何基础模型路线（VGGT 系）**：玻璃检测（蒸馏 VGGT 3D 先验）与 CGS-SLAM（VGGT 做视图对齐）都采用“大模型提供几何先验，下游任务做适配/精化”的范式。特点是快速获得较稳的几何，但受限于大模型的内部表征质量。

- **前馈 3DGS + 后处理工程化路线**：Per-View Gaussian Predictions（免训练过滤）与 KISS-GS（剪枝 + 图像化编码）都强调“与训练解耦”，以前馈 3DGS 输出为输入做纯后处理，可移植性强，但依赖前馈模型本身的逐视角分组与表征质量。CoGeo-GS 则走向“训练中集成语义标签 + 几何补全”的路线，比纯后处理更系统，但优化代价更大。

- **逐场景优化 3DGS/4DGS 路线**：水下评测（5 种 3DGS 系统对照）、4DGS-WAM（动态/静态分解的未来预测）与 SLAM（CGS-SLAM）都在优化阶段做文章。水下工作的关键发现是“方法表现取决于采集设置，而非架构”，说明数据获取协议本身是不可忽视的变量。

- **机器人/具身智能路线的“双通道”化解耦**：Instruct-to-Act 将 VLM 规划与世界模型控制器解耦；GaussianDream++ 将世界建模头在训练时使用、推理时裁剪；UCAG-P 在动作表征层面统一形态。三类工作的共同点是“在训练时最大化几何/语义监督，在部署时精简路径”，体现对实时性与可控性的双重追求。

- **经典几何问题的新解法**：GPS 无人机轨迹标定相机（参数化 ML 估计）、运动模糊下的自监督关键点（几何预训练 + 模糊感知训练）、图像到点云配准（深度引导投影对齐）——这些工作不追求推翻旧问题，而是在原有问题上引入更精确的建模（偏差参数、物理主轴、结构化深度引导）。


#### 值得优先阅读的论文

1. **SpatialCrafter: Single Image World Modeling with Generative 3D Proxies**  
   单图→可探索 3D 场景是游戏/VR/具身智能的公认难题。本文的两阶段分解（全局代理生成 + 外观细化）、PaSS Flow 与 Generative Deferred Refiner 的设计，直接回应了视频扩散模型在几何一致性上的痛点，并配套 115K 场景数据集，方法论与资源价值兼备。

2. **KISS-GS: 3D Gaussian Splatting Compression Kept Simple**  
   压缩是 3DGS 落地的硬门槛。其“模块化、训练解耦、图像化编码、解码通用”四位一体的设计，是对当前集成式压缩系统的一次简化，且给出 85x–319x 可复现的率失真收益。对想快速获得可部署压缩方案的读者最有直接帮助。

3. **Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS**  
   提出一种极简而巧妙的机制——利用逐视角分组预测，通过排除自身高斯渲染同一视角来暴露不一致内容。全程无需重训练，适用于多个前馈模型，且公开验证了不损害干净场景质量。工程借鉴价值高。

4. **GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation**  
   将 3D 世界建模以“令牌”形式嵌入 VLA 骨干，训练时使用专用头解码，推理时裁剪全部辅助部件。这是“世界模型+语言动作策略”落地为轻量实现的代表性探索，兼顾几何监督与部署成本，对机器人学习方向有较强的启示性。

5. **Gaussian Splatting Underwater: A Controlled Cross-Regime Study**  
   少见的水下 3DGS 受控对比：统一位姿、初始化、预算与评估器，结论（方法效果由采集设置决定而非架构；恢复预处理 + vanilla 3DGS 在工业场景几何上胜出）对任何“在退化环境中做重建”的研究者都有参考价值，且发布评测代码。


#### 可能的研究机会

- **“免训练后处理”与“架构内优化”的混合范式**：KISS-GS 与 Per-View 过滤都证明后处理可带来大收益；CoGeo-GS 证明训练内集成语义更系统。三者结合——前馈重建 + 免训练初滤 + 轻量微调/编码——可能是一条低门槛、高收益的 3DGS 落地路径。

- **几何基础模型与 3DGS 的“正交化”结合**：VGGT/LRM 被用于检测（玻璃）、配准（CGS-SLAM）、重建（MILO），但均为“先提取几何先验，后续任务精化”的顺序使用。将几何基础模型的增量更新与 3DGS 增量训练做在线协同（如流式场景更新）仍是空白。

- **水下/退化条件下的 3DGS 训练策略**：水下评测指出光照几何与采集设置比架构更重要。可跟进的空白：在“不均匀光照 + 介质散射 + 前馈单目先验”的组合下设计训练数据增强或不确定性感知损失；或将“恢复预处理”与

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-28T18:16:42-04:00
**Total number of papers:** 29
**Number of papers added in the latest update:** 15
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

### 2026-08

#### 2026-08-27 - CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction

**Authors:** Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen, Aurélien Chateigner
**Links:** [abs](https://arxiv.org/abs/2608.26868) - [pdf](https://arxiv.org/pdf/2608.26868)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** VGGT, SLAM, monocular depth, Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction
- 作者：Jean-Daniel de Ambrogi, Aline Chetouani, Vincent Nguyen, Aurélien Chateigner
- 出版日期：2026-08-27
- 分类：几何基础模型（Geometry Foundation Models）；次要分类：3D重建与多视角几何、神经场景表示与渲染
- 链接：https://arxiv.org/abs/2608.26868

### 一句话总结
CGS-SLAM提出了一种基于3D高斯泼溅（3DGS）的混合式去中心化/中心化多智能体SLAM系统，仅使用RGB和惯性数据即可实现多智能体的协同场景重建与子图对齐。

### 研究问题
如何在不依赖RGB-D传感器（如消费级智能手机不可用）的条件下，利用3DGS实现多智能体协同SLAM，并兼顾低通信开销与高质量的重建和跟踪。

### 核心思路/方法
每个智能体使用惯性数据作为运动先验进行本地跟踪，借助度量单目深度估计器（Depth Pro）重建带尺度的地图；智能体之间共享关键帧编码，并在空间重叠区域进行动态关键帧选择以增强子图对齐；随后，中心服务器使用视图对齐模型（VGGT）对各子图进行全局对齐，形成混合式去中心化/中心化架构，从而在大范围GNSS拒止环境中保持低通信成本并完成全局重建。

### 主要贡献
1. 提出了首个（或少数）支持仅RGB+惯性输入的多智能体3DGS SLAM系统。
2. 设计了混合式去中心化/中心化通信机制，在映射过程中保持低通信开销。
3. 引入动态关键帧选择策略以提升子图对齐质量。
4. 实验表明在多个数据集上跟踪性能具有竞争力，渲染质量优于现有方法，且子图对齐准确。

### 局限性
摘要未提供足够信息。摘要仅提及实验效果（跟踪、渲染、对齐），未说明失败场景、传感器要求、实时性、计算资源消耗或对智能体数量扩展性的具体讨论。

### 阅读优先级
**中**。理由：该工作面向多智能体协同SLAM与3DGS结合，属于较为新颖且应用价值较高的方向，但摘要中未给出具体数值结果与详细方法框架，适合对协同重建感兴趣的研究者进一步阅读全文；若读者主要关注单智能体3DGS SLAM或实时部署，则本文优先级一般。

</details>

<details>
<summary>Abstract</summary>

Recent advances in SLAM have leveraged 3DGS for photorealistic reconstruction and novel view synthesis. However, most methods rely on RGB-D input, which is unavailable on consumer-grade smartphones, and few integrate 3DGS within a collaborative framework. Therefore, we present CGS-SLAM, a hybrid decentralized/centralized system enabling multi-agent 3DGS SLAM using only RGB and inertial data. Each agent performs local tracking with inertial data as a motion prior and reconstructs a scaled map using a metric monocular depth estimator (Depth Pro). Keyframe encodings are shared among agents, enabling dynamic keyframing in regions of spatial overlaps with other agents, enhancing submap alignment. Afterwards, a central server aligns submaps using VGGT as a view alignment model. This bidirectional communication keeps communication cost low during mapping and global reconstruction in difficult GNSS-denied environments. Experiments on multiple datasets demonstrate competitive tracking performance, improved rendering quality over state-of-the-art methods, and accurate submap alignment.

</details>

#### 2026-08-27 - Glass Surface Detection Grounded in 3D Visual Geometry

**Authors:** Yiwei Lu, Ke Xu, Tao Yan, Xiaojun Chang, Radu Timofte, Rynson W. H. Lau
**Links:** [abs](https://arxiv.org/abs/2608.26752) - [pdf](https://arxiv.org/pdf/2608.26752)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** visual geometry grounded transformer, VGGT, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Glass Surface Detection Grounded in 3D Visual Geometry
- 作者：Yiwei Lu, Ke Xu, Tao Yan, Xiaojun Chang, Radu Timofte, Rynson W. H. Lau
- 出版日期：2026-08-27
- 分类：Geometry Foundation Models（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.26752

### 一句话总结
该论文提出将玻璃表面检测从2D外观线索转向基于3D视觉几何建模的方法，通过蒸馏3D先验并设计专用检测头，在七个基准上取得最优性能。

### 研究问题
如何利用3D视觉几何显式建模玻璃表面的物理存在，以解决传统2D外观方法在几何模糊场景中对透明、反光玻璃检测失效的问题。

### 核心思路/方法
1. **范式转变**：将GSD问题从2D外观驱动转为3D几何驱动。
2. **3D先验蒸馏**：从视觉几何grounded transformer（VGGT）中蒸馏丰富的3D先验，生成玻璃感知的3D表示。
3. **多任务学习**：设计新型玻璃检测头，包含两个核心模块：
   - **频率自注意力模块（FSAM）**：识别玻璃特有的光谱特征，用于玻璃表面定位。
   - **几何接地模块（GeGB）**：选择性将2D特征接地到3D几何中，用于玻璃表面分割。

### 主要贡献
1. 提出将玻璃表面检测重新定义为3D几何grounded问题，而非纯2D外观任务。
2. 设计了包含FSAM和GeGB的新颖检测头，结合频率特征与3D几何信息。
3. 在七个标准GSD基准上达到最先进性能，并验证了对视频/多模态数据的泛化能力。
4. 展示了对玻璃场景重建质量的显著提升。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法的计算开销、对3D几何质量（如深度估计误差）的依赖程度，或在高度动态/极端光照场景下的失效边界；实验细节（如具体消融、运行时间）也未给出。

### 阅读优先级
**高**
理由：该工作提出了一种解决玻璃检测难题的新范式（3D几何grounded），而非仅方法改进；涵盖了从模型设计、多任务学习到下游重建应用的完整链条，且指标全面（七个基准+泛化测试）。对从事透明物体感知、3D视觉或机器人场景理解的读者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Glass surface detection (GSD) is critical for scene understanding and reconstruction, and yet remains challenging due to the transparency and reflectivity of glass surfaces. Existing GSD methods typically rely on 2D appearance cues, which may fail in geometrically ambiguous scenes. In this paper, we propose a paradigm shift: grounding GSD in 3D visual geometry to explicitly model the physical existence of glass surfaces. Our method first distills rich 3D priors from the visual geometry grounded transformer (VGGT) and generates glass-aware 3D representations. It then exploits multi-tasking learning with a novel glass detection head, consisting of two core modules: a Frequency Self-Attention Module (FSAM) that identifies glass-specific spectral features for glass surface localization, and a Geometry Grounding Block (GeGB) that selectively grounds 2D features in 3D geometry for glass surface segmentation. Extensive experiments demonstrate that our method achieves state-of-the-art performance across seven standard GSD benchmarks, generalizes well to video/multi-modal data, and substantially improves reconstruction in glass scenes. Code is available in https://github.com/YT3DVision/VGGT_GLASS.

</details>

#### 2026-08-26 - GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation

**Authors:** Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He, Lei Yang, Haifang Qing, Si Liu, Ding Zhao, Ping Luo, Haibao Yu
**Links:** [abs](https://arxiv.org/abs/2608.25659) - [pdf](https://arxiv.org/pdf/2608.25659)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation
- 作者：Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He, Lei Yang, Haifang Qing, Si Liu, Ding Zhao, Ping Luo, Haibao Yu
- 出版日期：2026-08-26
- 分类：Geometry Foundation Models（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：https://arxiv.org/abs/2608.25659

### 一句话总结
GaussianDream++ 通过在 VLA 骨干网络中直接插入世界状态令牌和世界预测令牌，并以训练阶段专用的世界表示头解码为共享高斯原语的当前/未来三维表达，实现了高效、轻量且鲁棒的机器人操作世界建模。

### 研究问题
如何在视觉-语言-动作（VLA）策略中，以高效的方式引入具备度量三维结构与短期物理演化预测能力的监督信号，从而提升语言条件下的机器人操作性能，同时避免在线高斯解码或推理阶段的高昂部署成本。

### 核心思路/方法
- 在 VLA 骨干网络中直接插入**World State Tokens（世界状态令牌）**和**World Prediction Tokens（世界预测令牌）**，使世界建模信息与策略主干深度融合。
- 引入**训练专用**的 World Representation Head，将上述令牌解码为共享高斯原语下的**当前世界**与**未来预测**的耦合表示。
- 通过**静态-动态因子分解**，保留场景的持久结构，并将残差运动聚焦于交互相关区域。
- **推理时裁剪**：模型头部、渲染器、辅助目标及 VGGT/TGE 路径全部移除，仅保留 20 个世界令牌，无需在线高斯解码或 rollout，实现高效闭环控制。

### 主要贡献
- 提出 GaussianDream++ 方法，作为 GaussianDream 的紧凑、策略原生扩展，将世界状态与预测令牌无缝融入 VLA 骨干。
- 实现训练期三维监督（当前重建 + 未来预测），在不增加推理负担的前提下增强策略的几何与动态感知能力。
- 在 LIBERO 上达到 **98.6%**、LIBERO-Plus 上达到 **87.8%** 的成功率，在相机与场景布局移位下表现明显提升。
- 真实机器人实验中，相较于复现的 π₀.₅，平均成功率从 **29.2%** 提升至 **52.5%**，同时保持高效的闭环控制。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法在机器人操作与三维视觉交叉领域提出了在 VLA 策略内高效引入三维世界建模的新思路，并展示了在仿真与真实机器人上的显著性能提升；同时推理阶段极为轻量，具备明确的工程实用价值，对从事机器人学习、三维表示学习及具身智能的研究者具有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies have advanced language-conditioned robotic manipulation, yet action-imitation objectives provide only weak supervision for metric 3D structure and short-horizon physical evolution. Geometry-enhanced policies mainly improve current-scene grounding, whereas predictive policies often model future dynamics in RGB or latent spaces and may incur substantial deployment cost. GaussianDream demonstrates that training-time current Gaussian reconstruction and future Gaussian prediction provide effective 3D supervision, but its dense VGGT/TGE-based prefix jointly carries state, dynamics, and action-conditioning information. We present \textbf{\methodname}, a compact, policy-native extension that inserts \textbf{World State Tokens} and \textbf{World Prediction Tokens} directly into the VLA backbone. A training-only \textbf{World Representation Head} decodes these tokens into a Current World and coupled Future Prediction over shared Gaussian primitives, while static--dynamic factorization preserves persistent structure and focuses residual motion on interaction-relevant regions. At inference, the head, renderer, auxiliary objectives, and VGGT/TGE pathway are removed, leaving only 20 world tokens without online Gaussian decoding or rollout. \method achieves \textbf{98.6\%} on LIBERO and \textbf{87.8\%} on LIBERO-Plus, with clear gains under Camera and Layout shifts. Real-robot experiments further improve average success from 29.2\% to 52.5\% over reproduced $π_{0.5}$ while maintaining efficient closed-loop control.

</details>

#### 2026-08-25 - GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models

**Authors:** Zijian Zhang, Yuqing Jiang, Weitao Zhou, Minglei Li, Jinhao Zhang, Yao Mu, Xiaofan Li, Hao Zhao, Haibao Yu
**Links:** [abs](https://arxiv.org/abs/2608.24714) - [pdf](https://arxiv.org/pdf/2608.24714)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models
- 作者：Zijian Zhang, Yuqing Jiang, Weitao Zhou, Minglei Li, Jinhao Zhang, Yao Mu, Xiaofan Li, Hao Zhao, Haibao Yu
- 出版日期：2026-08-25
- 分类：几何基础模型（Geometry Foundation Models）
- 链接：https://arxiv.org/abs/2608.24714

### 一句话总结
GaussianWAM 通过将 3D 高斯场中的几何与语义监督蒸馏进世界-动作模型（WAM）的训练表示中，在不改变推理架构的前提下显著提升了机器人操作任务的性能。

### 研究问题
世界-动作模型（WAM）在联合学习未来视觉预测和动作生成时，其视频潜在表示主要针对视觉预测优化，未被显式地鼓励保持跨视角几何结构以及空间局部化、与物体相关的语义信息。本文旨在解决这一问题，探索如何在训练阶段为 WAM 表示注入几何与语义监督，而不增加部署时的计算负担。

### 核心思路/方法
GaussianWAM 是一个训练时的表示增强框架，其核心流程为：
1. 利用同步多视角观测，由冻结的几何基础模型和视觉基础模型提供深度、相机参数和稠密语义特征；
2. 将这些异构信号绑定到共享的 3D 高斯原语（Gaussian primitives）上，并渲染出空间对齐的语义、深度和覆盖目标；
3. 将渲染目标蒸馏到 WAM 的当前观测表示中；
4. 训练结束后，所有教师模型、高斯组件和辅助预测头均被移除，保留原始 WAM 推理路径，不增加额外模块或前向计算。

### 主要贡献
- 提出 GaussianWAM，一种训练时表示增强框架，通过 3D 高斯场组织几何与语义监督，并蒸馏到 WAM 表示中；
- 展示了将异构教师信号在空间上统一组织的优势：在 LIBERO-Plus 上，FastWAM 从 52.05% 提升至 71.29%，Cosmos Policy 从 71.52% 提升至 77.30%；
- 消融结果显示，直接 CLIP 和 VGGT 蒸馏建立了 FastWAM 的强基线 69.37%，而高斯场统一进一步将其提升至 71.29%，验证了空间组织异构教师信号的有效性；
- GaussianWAM 在标准 LIBERO 上也提升了性能，并在 RoboTwin 和真实世界操作上呈现正迁移趋势；
- 方法不影响部署架构，训练后额外组件全部移除。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的计算开销、训练时间成本、对多视角数据质量/数量要求的敏感性、失败模式或更广泛泛化性的边界条件。

### 阅读优先级
**高**。理由：该方法在多个基准（LIBERO-Plus、LIBERO、RoboTwin、真实世界操作）上均获得显著性能提升，且设计上不改变部署架构，具备实际应用价值；同时其核心思路——利用 3D 高斯场组织异构教师信号进行训练时蒸馏——具有一定新颖性，对 WAM 和机器人操作研究方向具有参考意义。

</details>

<details>
<summary>Abstract</summary>

World-Action Models (WAMs) jointly learn future visual prediction and action generation, using video dynamics as a representation-learning signal for robotic manipulation. However, their video latents are primarily optimized for visual prediction and are not explicitly encouraged to preserve cross-view geometric structure or spatially localized, object-relevant semantics. We propose \textbf{GaussianWAM}, a training-time representation-enhancement framework that organizes geometric and semantic supervision through a 3D Gaussian field. Given synchronized multi-view observations, frozen geometry and vision foundation models provide depth, camera parameters, and dense semantic features. GaussianWAM binds these heterogeneous signals to shared Gaussian primitives and renders spatially aligned semantic, depth, and coverage targets, which are distilled into the current-observation representations of the WAM. All teacher models, Gaussian components, and auxiliary prediction heads are removed after training, leaving the original WAM inference path without additional modules or forward computation. On LIBERO-Plus, GaussianWAM improves FastWAM from 52.05\% to 71.29\% and Cosmos Policy from 71.52\% to 77.30\%. Direct CLIP and VGGT distillation already establishes a strong FastWAM baseline of 69.37\%, while Gaussian-field unification further improves it to 71.29\%, supporting the benefit of spatially organizing heterogeneous teacher signals. GaussianWAM also improves performance on standard LIBERO and shows positive transfer trends on RoboTwin and real-world manipulation. These results suggest that training-time Gaussian distillation provides a practical way to inject geometry- and semantics-related supervision into WAM representations without changing their deployment architecture.

</details>

## Dynamic / 4D Reconstruction

### 2026-08

#### 2026-08-26 - 4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting

**Authors:** Yueen Ma, Zenglin Xu, Irwin King
**Links:** [abs](https://arxiv.org/abs/2608.25956) - [pdf](https://arxiv.org/pdf/2608.25956)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting
- 作者：Yueen Ma, Zenglin Xu, Irwin King
- 出版日期：2026-08-26
- 分类：Dynamic / 4D Reconstruction（次要分类：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.25956

### 一句话总结
本文提出一个基于4D高斯泼溅的对象中心世界动作模型（4DGS-WAM），通过分离动态对象与静态背景，实现仅预测动态物体变化而复用已观察静态内容的未来状态外推。

### 研究问题
现有世界动作模型（WAMs）基于2D视觉数据，缺乏显式的对象级空间结构，且反复处理冗余背景内容；而点云虽能表示3D空间，但在跨视角对齐和累积上存在困难，如何构建一个兼具显式空间结构与高效未来预测的世界动作模型是本文要解决的问题。

### 核心思路/方法
- 使用显式4D高斯泼溅（4DGS）表示，将场景中的动态对象与静态背景分别建模。
- 对于动态对象：采用策略模型预测未来的执行者动作，世界模型预测这些对象所对应高斯泼溅的变换。
- 对于静态背景：由于在过去的帧中大部分已被观察，无需在未来状态中重新生成，可直接复用。
- 该设计将2D观测提升为持久化的4D表示，使未来预测只需专注于动态对象演化，形成对象中心的世界动作模型。

### 主要贡献
- 提出4DGS-WAM，一个对象中心的世界动作模型，基于4D高斯泼溅显式建模动态与静态场景分量。
- 通过复用已观察的静态背景，避免对未来状态中冗余背景的重复生成，从而将计算资源集中于动态对象演化。
- 在KITTI-MOT数据集上进行了短时程预测与过去重建的实验评估。

### 局限性
摘要未提供足够信息——实验具体指标、与基线方法的量化比较、推理效率、动态对象数量限制或场景复杂度适用性均未在摘要中说明。

### 阅读优先级
**中**。理由：该工作将对象中心思想与4DGS结合，方法上有一定创新性，且静态背景复用的思路对未来预测类任务具有参考价值；但摘要中未见对比实验细节和量化结果，实际性能仍需阅读全文确认。适合关注4D重建、世界模型或动作预测方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Current world action models (WAMs) typically operate on 2D visual data. These models can achieve exceptional visual quality, but they lack explicit spatial structure for individual objects and repeatedly process redundant background content. Although point clouds can represent the world in 3D space, they can be difficult to align and accumulate across viewpoints. In this paper, we leverage an explicit 4D Gaussian Splatting (4DGS) representation that separately models dynamic objects and the static background of a scene. For dynamic objects, we use a policy model to predict future actor actions and a world model to predict transformations of their observed Gaussian splats. The static background need not be regenerated for future states, as much of it has already been observed in past frames. This forms an object-centric world action model, which we name 4DGS-WAM. It lifts 2D observations into a persistent 4D representation so that previously observed static content can be reused during future prediction. Future-state extrapolation can then focus on modeling the evolution of dynamic objects. Experiments on KITTI-MOT evaluate short-horizon prediction and past reconstruction.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-08

#### 2026-08-27 - Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects

**Authors:** Brian De La Cruz, Aaron Y. Zhao, Maitrey Gramopadhye, Sawyer J. Lazar, Xianming Tan, Daniel Szafir, David S. Lawrence
**Links:** [abs](https://arxiv.org/abs/2608.27301) - [pdf](https://arxiv.org/pdf/2608.27301)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, photogrammetry, NeRF, neural radiance field, radiance field, Gaussian Splatting, radiance, splatting, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects
- 作者：Brian De La Cruz, Aaron Y. Zhao, Maitrey Gramopadhye, Sawyer J. Lazar, Xianming Tan, Daniel Szafir, David S. Lawrence
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.27301

### 一句话总结
该研究对比了摄影测量、NeRF、高斯溅射与LiDAR四种3D重建方法在生成实验室物品全息模型上的保真度，发现NeRF方法在透明、反光、低纹理物体上表现最优。

### 研究问题
当前的3D重建方法是否足以支持在教育场景中创建真实感强的实验室物品全息表示？四种主流重建方法（摄影测量、NeRF、高斯溅射、LiDAR）在形状、颜色、纹理和视觉缺陷等维度上的保真度如何？

### 核心思路/方法
- 选取常见实验室物品作为重建对象，分别用四种方法（摄影测量、NeRF、高斯溅射、LiDAR）生成全息模型。
- 采用重复测量设计（repeated-measures design），由研究生对生成的模型在形状、颜色、纹理和视觉缺陷四个维度进行主观评估。
- 比较不同方法在不同物体类型（特别是透明、反光、低纹理物体）上的表现差异。

### 主要贡献
- 系统比较了四种主流3D重建方法在教育全息影像场景中的适用性，填补了该应用领域的评估空白。
- 发现NeRF方法在不同物体上均能产生最稳定高保真的表示，尤其擅长处理其他方法难以捕获的透明、反光或低纹理物体。
- 揭示了形状和颜色通常比纹理重建得更成功，指出纹理是教育全息模型中的难点。
- 展示了面向AR/MR教育环境创建沉浸式学习对象的可行工作流程，支持实验前准备、空间推理和学生参与等教育目标。

### 局限性
摘要未提供足够信息。例如，未提及样本数量、评估者人数、统计分析方法、各方法的计算成本或重建时间、以及任何定量误差指标，也未说明LiDAR方法在具体物体上的失败模式细节。

### 阅读优先级
**中**  
理由：该研究对教育技术/AR/MR内容开发者和3D重建算法应用者有一定参考价值，比较了多种主流方法的实际效果，但属于应用性评估而非算法创新，方法细节有限（具体协议、指标不全），对于纯算法研究者或追求方法突破的读者优先级偏低。若您关注沉浸式教育或全息显示应用，可读性较高。

</details>

<details>
<summary>Abstract</summary>

In this study, we examined whether current 3D reconstruction methods can support the creation of realistic holographic representations of laboratory objects for educational use. In this regard, we compared four approaches: photogrammetry, a neural radiance field (NeRF)-based method, Gaussian splatting, and LiDAR. These methods were used to generate holographic models of common laboratory items and their fidelity was evaluated by graduate students. Participants assessed the models for shape, color, texture, and visual defects using a repeated-measures design. Across objects, the NeRF-based method produced the most consistently high-fidelity representations, particularly for transparent, reflective, or low-texture items that were difficult to capture with other approaches. Shape and color were generally reproduced more successfully than texture, suggesting that some visual properties remain more challenging to represent accurately in educational holograms. Beyond identifying the strengths and limitations of each reconstruction method, the study demonstrates a practical workflow for creating immersive learning objects that may support pre-laboratory preparation, spatial reasoning, and student engagement in AR/MR-based educational environments. These findings offer design-relevant insights for educators and researchers developing immersive digital learning experiences.

</details>

#### 2026-08-27 - SSMB: Self-Supervised Local Feature Detection under Motion Blur

**Authors:** Zhenjun Zhao, Fabio Bellavia, Wenting Wang, Fan Zhu, Jiajun Wu, Suryansh Kumar, Mingqiang Wei, Haoang Li, Javier Civera
**Links:** [abs](https://arxiv.org/abs/2608.27181) - [pdf](https://arxiv.org/pdf/2608.27181)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** image matching, pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SSMB: Self-Supervised Local Feature Detection under Motion Blur
- 作者：Zhenjun Zhao, Fabio Bellavia, Wenting Wang, Fan Zhu, Jiajun Wu, Suryansh Kumar, Mingqiang Wei, Haoang Li, Javier Civera
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.27181

### 一句话总结
SSMB 提出了一种无需去模糊、无需手工检测器或外部伪标签的自监督关键点检测方法，专门针对运动模糊图像，通过局部判别增强模块和两阶段训练实现模糊不变的特征检测。

### 研究问题
运动模糊会扭曲局部图像结构，降低关键点定位的可重复性；现有方法要么依赖计算昂贵的“先去模糊再检测”流程（可能引入伪影），要么在清晰图上回归手工关键点的位置（受限于手工检测器的假设），缺乏真正针对模糊可重复性的自监督方案。

### 核心思路/方法
- 整体框架：去模糊无关的自监督关键点检测器，不依赖手工检测器或外部伪标签。
- 关键模块：Local Discriminability Enhancement (LDE) 模块，用于在全局特征混合后恢复细粒度的局部判别能力。
- 两阶段训练：
  1. 几何预训练：在合成形状上通过渲染几何引导，引导出空间上具有判别性的关键点检测，无需外部检测器。
  2. 模糊感知训练：在真实清晰-模糊图像对上进行，通过多组件自监督目标（跨域一致性、几何对齐、空间覆盖）学习模糊不变检测。

### 主要贡献
- 提出首个无需去模糊、无需手工检测器和外部伪标签的自监督模糊图像关键点检测方法。
- 引入局部判别增强模块，解决全局特征混合后局部判别力不足的问题。
- 提出两阶段自监督训练策略，结合合成几何预训练和真实模糊对训练。
- 在关键点检测、图像匹配、相对姿态估计和运动模糊下的视觉定位等任务上，达到稀疏关键点检测器的新 SOTA，一致优于监督和自监督基线。

### 局限性
摘要未提供足够信息。例如，未提及方法在极端模糊、高噪声或实时性方面的具体限制，也未给出失败场景或计算开销的讨论。

### 阅读优先级
高。理由：该研究针对运动模糊下关键点检测这一长期难题，提出了一种全新的自监督方案，避免去模糊流程和手工先验，并且在多个下游任务上超越现有基线。对于从事三维重建、视觉定位、SLAM 等相关方向的研究者，该方法具有较高的参考价值。尽管摘要未给出实验细节，但整体贡献和技术路线具备较强的创新性和实用性。

</details>

<details>
<summary>Abstract</summary>

Keypoint detection under motion blur remains a significant challenge, as blur distorts local image structure and degrades the repeatability of feature localization. Existing approaches either rely on computationally expensive deblur-then-detect pipelines that may introduce restoration artifacts, or learn to regress the image positions of handcrafted keypoints extracted on sharp images, which reflects the assumptions of the handcrafted detector rather than what is truly repeatable under blur. We present SSMB, a deblur-free, self-supervised keypoint detector for motion-blurred images that requires neither handcrafted detectors nor external pseudo-labels. SSMB introduces the Local Discriminability Enhancement (LDE) module, which restores fine-grained local discriminability after global feature mixing. Training is performed in two stages. First, geometric pretraining on synthetic shapes bootstraps spatially discriminative keypoint detection without any external detector, just from the rendered geometry. Second, blur-aware training on real sharp-blur image pairs learns blur-invariant detection through a multi-component self-supervised objective that enforces cross-domain consistency, geometric alignment, and spatial coverage. Extensive evaluations on keypoint detection, image matching, relative pose estimation, and visual localization under motion blur demonstrate that SSMB establishes a new state-of-the-art among sparse keypoint detectors, consistently outperforming both supervised and self-supervised baselines across all tasks. Code, models, and datasets will be publicly available upon paper acceptance.

</details>

#### 2026-08-27 - A Geometry-Driven, Framework-Agnostic Optimization for Object Pose Estimation

**Authors:** Wei Chen, Tao Zhen, Zhongchen Shi, Jing Zhang, Liang Xie, Erwei Yin
**Links:** [abs](https://arxiv.org/abs/2608.26859) - [pdf](https://arxiv.org/pdf/2608.26859)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Geometry-Driven, Framework-Agnostic Optimization for Object Pose Estimation
- 作者：Wei Chen, Tao Zhen, Zhongchen Shi, Jing Zhang, Liang Xie, Erwei Yin
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.26859

### 一句话总结
本文提出一种基于物体主惯性轴对齐的几何驱动、数据集层面的姿态表示优化方法，在不修改网络结构的前提下提升物体姿态估计精度。

### 研究问题
如何在不依赖网络架构创新的情况下，从数据层面提升物体姿态估计的精度与鲁棒性，同时解决对称物体的旋转标签歧义问题。

### 核心思路/方法
- 提出一种新的、物理上合理的旋转表示：通过主惯性轴对齐，将物体的坐标系与其固有的几何轴（由惯性属性推导）对齐。
- 该优化完全在数据集层面进行，不涉及任何网络架构修改，具有框架无关性（Framework-Agnostic），可作为即插即用模块。
- 利用主轴的“能量最小化”特性增强表示稳定性，并对对称物体的旋转歧义在数据层面进行显式的规范化处理，从根源消除训练时的标签混淆。

### 主要贡献
1. 提出几何驱动的数据级优化方法，替代传统的模型中心式改进思路。
2. 引入基于主惯性轴的旋转表示，具备内在稳定性，对噪声和遮挡更鲁棒。
3. 在数据层面显式解决对称物体的旋转歧义问题，消除标签混淆。
4. 方法框架无关，无需修改现有网络即可应用，兼容类别级和实例级模型。
5. 大量实验表明在保持基线网络完整性的前提下，精度获得一致且显著的提升。

### 局限性
摘要未提供足够信息以评估方法的局限性，例如计算开销、对非刚性物体或极端几何形状的适用性、实验数据集的具体规模与范围均未在摘要中说明。

### 阅读优先级
**中**  
理由：该方法属于数据-centric优化方向，思路新颖且有实用价值（框架无关、即插即用），适合姿态估计领域研究者关注；但摘要未给出具体实验数值和对比基线细节，无法判断其性能提升的实际幅度与适用范围，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

Current object pose estimation research remains predominantly model-centric, focusing on architectural innovations and post-processing refinements. This paper introduces a data-centric optimization by proposing a novel, physically grounded rotation representation through principal axes alignment. Our method aligns the object's coordinate system with its inherent geometric axes, derived from inertial properties, yielding three key advantages: Inherent Stability-leveraging the energy-minimizing property of principal axes provides a robust representation that is less sensitive to noise and occlusions; Symmetry-Aware Canonicalization-explicitly resolving rotational ambiguities for symmetric objects at the data level, which fundamentally eliminates label confusion during network training; and Framework Agnosticism-the optimization is applied purely at the dataset level, ensuring plug-and-play compatibility with existing networks without any architectural modification. We validate the framework across diverse category-level and instance-level models. Extensive experiments demonstrate consistent and significant accuracy improvements, while preserving the integrity of the baseline network. This work establishes a new, geometry-driven direction for enhancing pose estimation, circumventing the need for complex network redesign.

</details>

#### 2026-08-27 - DPA-I2P: Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration in Autonomous Driving

**Authors:** Wenxin Zhang, Hang Li, Zhiwei Xu, Qiankun Dong, Gang Wang, Tao Li
**Links:** [abs](https://arxiv.org/abs/2608.26589) - [pdf](https://arxiv.org/pdf/2608.26589)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, camera pose estimation, pose estimation, autonomous driving, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DPA-I2P: Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration in Autonomous Driving
- 作者：Wenxin Zhang, Hang Li, Zhiwei Xu, Qiankun Dong, Gang Wang, Tao Li
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26589

### 一句话总结
本文提出一种深度引导的投影对齐方法DPA-I2P，利用结构化的深度与视觉信息增强图像与点云之间的跨模态对应学习，从而提升自动驾驶场景中相机位姿估计的精度。

### 研究问题
如何解决图像与稀疏LiDAR点云之间因模态差异导致的跨模态对应学习困难，以提高图像到点云配准的准确性和鲁棒性。

### 核心思路/方法
提出DPA-I2P框架，包含三个关键设计：1）Ray-Conditioned Metric Depth Encoding（RMDE），以几何感知方式编码深度信息；2）Projection-Consistent Vision Lifting（PVL），以结构化方式利用视觉线索；3）Cross-Modal Query Pruning（CQP），在早期精细化阶段抑制不可靠的查询以提升匹配稳定性。整体方法在端到端框架中学习跨模态对齐。

### 主要贡献
1. 提出DPA-I2P，一种新颖的深度引导投影对齐方法用于图像到点云配准。
2. 设计RMDE和PVL模块，以几何感知方式而非朴素拼接方式融合深度与视觉特征。
3. 引入CQP机制，在精细化早期过滤不稳定查询，提高匹配稳定性。
4. 在KITTI和nuScenes数据集上验证有效性：KITTI上相较于最强隐式基线，RTE降低45.0%，RRE降低55.6%；nuScenes上也优于所评估的基线，显示出较好的跨场景迁移能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对自动驾驶中重要的图像-点云配准任务，提出了系统性的方法改进（深度引导+投影对齐+查询剪枝），并在两个主流数据集（KITTI、nuScenes）上取得显著精度提升（尤其KITTI上RTE/RRE大幅降低），同时验证了跨场景迁移性。对从事多模态配准、自动驾驶定位或3D视觉的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Image-to-Point Cloud Registration aims to estimate the camera pose of a given image within a 3D scene point cloud, which is a fundamental task in autonomous driving and large-scale outdoor localization. Recent implicit correspondence learning methods have improved registration performance by learning cross-modal alignment in an end-to-end framework, leading to more accurate camera pose estimation. However, due to the inherent modality discrepancy between images and sparse LiDAR point clouds, reliable cross-modal correspondence learning remains challenging. To address this issue, we propose Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration (DPA-I2P). Unlike naive depth or feature concatenation, Ray-Conditioned Metric Depth Encoding (RMDE) and Projection-Consistent Vision Lifting (PVL) exploit depth and visual cues in a structured, geometry-aware manner. In addition, Cross-Modal Query Pruning (CQP) suppresses unreliable queries during early refinement to improve matching stability. Experiments on KITTI and nuScenes demonstrate the effectiveness of the proposed method. On KITTI, DPA-I2P reduces RTE and RRE by 45.0% and 55.6% over the strongest implicit baseline, respectively. On nuScenes, DPA-I2P also improves registration accuracy over the evaluated baselines, suggesting better transferability to different driving scenes.

</details>

#### 2026-08-27 - Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones

**Authors:** R. Yang, Y. Bar-Shalom, H. A. J. Huang
**Links:** [abs](https://arxiv.org/abs/2608.26548) - [pdf](https://arxiv.org/pdf/2608.26548)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Camera Calibration Using Inaccurate and Asynchronous Discrete GPS Trajectory from Drones
- 作者：R. Yang, Y. Bar-Shalom, H. A. J. Huang
- 出版日期：2026-08-27
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.26548

### 一句话总结
本文提出了一种利用无人机GPS轨迹进行静止相机标定的方法，通过参数估计同时处理GPS高度偏差、时间偏移以及相机姿态角偏差，并使用迭代最小二乘最大似然估计器实现对非同步离散轨迹的标定。

### 研究问题
如何利用无人机GPS记录的运动轨迹作为地面真值来标定静止相机的朝向角（偏航、俯仰、滚转），同时克服GPS高度不准（含未知偏差）、GPS与相机间时间不同步（存在未知时间偏移）、以及GPS轨迹时间离散需要精确插值这三个挑战。

### 核心思路/方法
- 将标定问题建模为参数估计问题，待估计向量包含GPS高度偏差、时间偏移以及相机的偏航、俯仰、滚转偏差。
- 针对非同步、时间离散的GPS轨迹，开发了一种基于迭代最小二乘算法的专用最大似然估计器。
- 通过仿真实验验证算法性能，并推荐了一种能够获得良好标定精度的无人机飞行轨迹。
- 标定精度以残余偏差相对于测量误差标准差的比例衡量，结果显示可达测量误差标准差的14%。

### 主要贡献
- 将GPS高度偏差和时间偏移纳入参数估计框架，与相机姿态角偏差联合估计，解决了两个主要挑战。
- 提出了适用于非同步时间离散GPS轨迹的迭代最小二乘最大似然估计器。
- 给出了能够实现高标定精度的推荐无人机轨迹。
- 仿真结果表明估计结果满足Cramér-Rao下界（CRLB），归一化估计误差平方在统计上可接受。

### 局限性
- 摘要未提供真实实验（如物理实验）数据与结果，仅提及仿真测试。
- 摘要未能提供算法在不同轨迹类型、噪声水平或极端场景下的鲁棒性分析细节。
- 摘要未涉及该方法对相机内参或其他相机参数（如焦距、畸变）的标定能力。
- 摘要未讨论方法在实时应用中的计算复杂度或运行时间。
- 摘要未提供失败模式或适用条件的明确边界（如GPS精度要求、无人机飞行速度限制等）。

### 阅读优先级
**中**  
理由：该论文聚焦于相机标定与无人机GPS轨迹结合的特定问题，方法上采用经典参数估计框架（最大似然 + 迭代最小二乘），对从事相机标定或无人机视觉定位的研究者有一定参考价值。然而，摘要以仿真验证为主，缺少真实实验对比及应用场景的讨论，阅读价值更多在于方法设计思路而非普适性结论。因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

This paper considers a stationary camera calibration problem, which estimates the camera orientation angles yaw, pitch and roll, using a drone trajectory recorded by a GPS. There are three challenges in using a GPS trajectory as ground truth for camera calibration. One, the altitude of GPS data is inaccurate with an unknown bias. Two, the GPS receiver and camera are not time synchronized, and there is an unknown time offset between the two systems. Three, the GPS trajectory is time-discrete and accurate interpolation is needed. This is actually an estimation problem since velocity is also needed. To address the first two challenges, we formulate the problem as a parameter estimation problem to estimate a vector consisting of the GPS altitude bias and time offset in addition to the camera yaw, pitch and roll biases. We then develop a special maximum likelihood estimator using the Iterated Least Squares algorithm which can work with a non-synchronized time-discrete GPS trajectory for the third challenge. Since the camera measurement errors are usually small, this requires a high calibration accuracy so that the residual bias error following the calibration should not be significant compared to the measurement error standard deviation. The calibration accuracy depends highly on the drone trajectory. This paper also recommends an appropriate drone trajectory which can yield a good calibration accuracy, namely, 14\% of the measurement error standard deviation. Simulation tests are conducted to demonstrate the algorithm performance. The estimation results meet the Cramer-Rao Lower Bound (CRLB) since the Normalized Estimation Error Squared w.r.t.\ the CRLB is statistically acceptable.

</details>

#### 2026-08-26 - Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots

**Authors:** Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier
**Links:** [abs](https://arxiv.org/abs/2608.26383) - [pdf](https://arxiv.org/pdf/2608.26383)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** feed-forward reconstruction, 3D reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, view synthesis, rendering, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots
- 作者：Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier
- 出版日期：2026-08-26
- 分类：3D Reconstruction & Multi-view Geometry（主）；Neural Scene Representations & Rendering（次）
- 链接：https://arxiv.org/abs/2608.26383

### 一句话总结
本文系统评测了NeRF与3D Gaussian Splatting在多种GPU平台上的训练/渲染性能，并对比了Meta SAM3D单图重建的速度与精度差距，指出实验室机器人应采用“轻量前馈重建维持实时闭环 + 重型神经重建按需调度”的分层方案。

### 研究问题
神经3D重建方法在真实实验室机器人常用的各类计算平台（从单板计算机到服务器级节点）上，能否满足物理控制回路所需的实时性？尤其是NeRF与3D Gaussian Splatting的训练和渲染效率，以及SAM3D这类前馈方法相比逐场景优化的延迟与保真度差距有多大？

### 核心思路/方法
- 构建跨平台的系统化基准测试，覆盖从单板计算机到服务器级GPU的多种计算设备。
- 在同一基准轴上评估两类方法：逐场景优化的NeRF和3D Gaussian Splatting（训练+渲染），以及Meta的SAM3D单图像重建。
- 对比这些方法的渲染质量、GPU开销、训练/推理延迟，并考察其在机器人控制回路实时性约束下的可行性。

### 主要贡献
- 首次系统性地在不同计算平台上基准测试神经3D重建方法，覆盖实验室机器人实际可能用到的设备层级。
- 定量分析显示：Gaussian Splatting渲染质量优于NeRF，但GPU成本更高；板载计算无法以交互速率完成完整逐场景优化。
- 对SAM3D的初步评估表明其可在数秒内生成合理的物体几何，但细节不一致可能影响下游操纵任务。
- 基于实验结论提出分层处理管线建议：轻量前馈重建支撑实时感知跟踪，重型神经重建在合适计算资源上选择性调度。

### 局限性
- 摘要未提供数据集规模、测试场景数量、具体设备型号及量化性能数值（如FPS、PSNR、延迟毫秒数等）等实验细节。
- 摘要未说明SAM3D评估的具体任务设置、精度度量方式以及其“细节不匹配”的具体表现类型。
- 摘要未提供基准测试的重复次数、统计显著性检验或误差分析，也未说明各方法在不同平台上的资源消耗（如显存占用）。

### 阅读优先级
**高**  
理由：该工作填补了神经3D重建在机器人实时应用场景中跨平台性能评估的空白，结论直接指向实际部署策略（分层管线），对从事具身智能、实验室自动化或实时3D视觉的读者有明确参考价值。尽管摘要缺少定量细节，但研究问题与结论的工程导向性强，适合优先阅读以获取系统性认知。

</details>

<details>
<summary>Abstract</summary>

Autonomous robots performing laboratory tasks depend on 3D reconstruction pipelines that can turn raw camera streams into actionable object representations within the latency budget of a physical control loop. Neural 3D reconstruction methods have demonstrated high-quality view synthesis, but their real-time viability across the compute platforms on which laboratory robots actually run remains poorly characterized. In this work, we present a systematic compute-platform benchmark of neural 3D reconstruction methods, evaluating NeRF and 3D Gaussian Splatting training and rendering on GPU-enabled computing devices ranging from single-board computers to server-class nodes, and place Meta's SAM3D single-image reconstruction on the same axes to quantify its latency and fidelity gap relative to per-scene optimization. Our results show that Gaussian Splatting yields higher rendering quality than NeRF at greater GPU cost, and that onboard compute is insufficient for full per-scene optimization at interactive rates. Our preliminary assessment on SAM3D indicates that it delivers plausible object geometry within seconds, but with detail mismatches that can compromise downstream manipulation. Together, these findings motivate tiered pipelines in which lightweight feed-forward reconstruction sustains the real-time perception-and-tracking loop for laboratory robots, while heavier neural reconstruction is scheduled selectively on suitable compute.

</details>

#### 2026-08-26 - Gaussian Splatting Underwater: A Controlled Cross-Regime Study

**Authors:** Olaya Álvarez-Tuñón, Stella Graßhof
**Links:** [abs](https://arxiv.org/abs/2608.25483) - [pdf](https://arxiv.org/pdf/2608.25483)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, structure from motion, Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Splatting Underwater: A Controlled Cross-Regime Study
- 作者：Olaya Álvarez-Tuñón, Stella Graßhof
- 出版日期：2026-08-26
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.25483

### 一句话总结
本文在受控协议下系统比较了五种高斯泼溅方法在水下不同浊度、光照和色彩衰减条件下的重建性能，发现方法效果主要由数据采集设置而非算法架构决定。

### 研究问题
高斯泼溅（Gaussian splatting）方法在水下不同环境条件（浊度、光照损失、颜色衰减）下的表现如何？不同方法各自的优劣势与局限性是什么？

### 核心思路/方法
- 使用多个公开水下数据集，覆盖不同浊度、光照衰减和色彩衰减程度，并加入一个工业巡检场景。
- 选取五个具有公开代码的高斯泼溅系统，在统一协议下运行：共享位姿、初始化、预算和评估器。
- 通过控制变量比较各方法在几何与光度上的表现，分析环境因素对方法相对性能的影响。

### 主要贡献
- 提供了高斯泼溅在水下多环境条件下的系统化跨场景对比研究。
- 发现方法性能更多依赖采集设置（如水质、光照几何）而非网络架构。
- 揭示了水清晰度对上游运动恢复结构（SfM）的强约束（清晰水注册率99.5%，12 NTU时降至0.0%）。
- 指出光照几何决定介质建模是否有用：随相机移动的人工光下，不考虑介质的泼溅法优于两种介质感知方法。
- 在工业巡检场景中，基准的光度领先者在几何上落败，而恢复预处理（restoration pre-pass）+ vanilla 3DGS 在几何上胜出；且该差异在已有报告得分中不可见。
- 发布场景构建、逐次运行配置和评估代码。

### 局限性
摘要未提供足够信息（未详细说明各方法的具体实现差异、评估指标细节、数据集规模、计算开销等）。

### 阅读优先级
**高**  
理由：该研究针对水下三维重建这一重要且难度高的场景，对高斯泼溅方法进行了严格受控的跨条件基准，结论具有较强实际指导意义（如设置对性能的决定性影响），并对现有方法在非常规环境下的适用性提出质疑，适合关注三维重建、水下视觉及高斯泼溅的读者。

</details>

<details>
<summary>Abstract</summary>

The underwater environment is challenging for 3D reconstruction, because particles suspended in the water scatter and diffuse light, turbidity varies, absorption depends on wavelength, and illumination is rarely uniform. Methods based on Gaussian splatting have generally been developed for conditions that allow good image quality, and have primarily been tested on relatively shallow water. This paper examines how well Gaussian splatting performs across publicly available underwater datasets representing different degrees of turbidity, loss of illumination, and colour attenuation, together with an industrial survey. Five systems with public code are run under one protocol, with shared poses, initialisation, budget, and evaluator, to establish their relative advantages, disadvantages, and limitations. What these methods can do turns out to depend more on the setup than on the architecture. Water clarity binds upstream of rendering, since structure-from-motion registers 99.5 \% of frames in clear water and 0.0 \% at 12 NTU. Illumination geometry decides whether a medium model helps at all: under an artificial light that moves with the camera, medium-blind splatting beats both medium-aware systems. On the survey the benchmark's photometric leader comes last, beaten on geometry by a restoration pre-pass in front of vanilla 3DGS---and none of it is visible in the scores the field reports. Scene builds, per-run configurations, and evaluation code are released at https://github.com/olayasturias/uw3dgs

</details>

#### 2026-08-26 - PIVOT: A Multi-Trajectory Dataset and Testbed for Pose, Intrinsics, and Novel Viewpoint Evaluation in Real-World 3D Reconstruction

**Authors:** Mary Raymond
**Links:** [abs](https://arxiv.org/abs/2608.25401) - [pdf](https://arxiv.org/pdf/2608.25401)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, camera calibration, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PIVOT: A Multi-Trajectory Dataset and Testbed for Pose, Intrinsics, and Novel Viewpoint Evaluation in Real-World 3D Reconstruction
- 作者：Mary Raymond
- 出版日期：2026-08-26T06:02:32Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：[摘要](https://arxiv.org/abs/2608.25401) | [PDF](https://arxiv.org/pdf/2608.25401)

### 一句话总结
PIVOT是一个多轨迹真实场景数据集与评测平台，用于独立评估相机位姿、内参和训练/测试轨迹差异对NeRF和3DGS等新视角合成方法性能的影响。

### 研究问题
现有新视角合成方法的评测通常在比实际机器人/无人机/自动驾驶场景更“干净”的条件下进行（如重建友好的轨迹、优化过的位姿和内参、从训练轨迹中采样的测试视图），这些假设可能掩盖方法在实测位姿、可复用标定和结构不同的相机轨迹下的真实表现。PIVOT旨在建立一个能独立研究这些因素的基准。

### 核心思路/方法
- 构建一个多轨迹数据集：对每个场景使用多种不同的相机轨迹进行采集，并同时保留传感器测量得到的位姿（实测位姿）和COLMAP优化后的位姿，以及标定和优化后的相机内参。
- 定义三类基准测试族：
  1. 已见轨迹 vs. 未见轨迹的新视角泛化能力；
  2. 实测位姿 vs. 优化位姿的敏感性；
  3. 标定内参 vs. 优化内参的敏感性。
- 引入一种“定向位姿空间Chamfer距离”，用于量化训练位姿对评测轨迹的覆盖程度。
- PIVOT v1包含5个真实场景（由DJI Mini 4 Pro采集），并提供开放的处理流程和基于Nerfstudio的评测工具链。

### 主要贡献
- 提出了PIVOT数据集与评测平台，明确将位姿、内参和轨迹结构作为独立评测变量，填补现有基准的空白。
- 定义了三个针对性的基准评测族，分别用于评估轨迹泛化、位姿敏感性和内参敏感性。
- 提出了定向位姿空间Chamfer距离这一新度量，用于描述训练位姿对评测轨迹的覆盖质量。
- 提供了包含5个真实场景的开源数据集和完整工具链（基于Nerfstudio）。
- 基准结果显示：已表示轨迹上的留出视图与未见轨迹之间存在一致的质量差距，且方法对位姿来源和相机内参存在显著敏感性。

### 局限性
摘要未提供足够信息。摘要中未涉及数据规模细节（如每个场景的轨迹数量、帧数）、计算资源需求、对方法性能差距的量化数值、以及是否有失败案例或场景类型限制（如动态物体、光照变化等）等内容，这些无法从摘要中确认。

### 阅读优先级
**高**。理由：
1. 该工作直接针对新视角合成评测中常见的“理想化假设”问题，对NeRF/3DGS领域的实践者有较强的现实指导意义。
2. 提出的三类基准评测族和新的覆盖度量具有方法论价值，适合从事三维重建、位姿估计和视角合成研究的读者。
3. 提供开源数据和工具链，具备直接复现和扩展应用的潜力。
4. 结果揭示的“轨迹未见时质量下降”和“位姿/内参敏感”等问题，对系统部署（如机器人、无人机）具有实际参考意义。

</details>

<details>
<summary>Abstract</summary>

Neural radiance fields (NeRFs), 3D Gaussian Splatting (3DGS), and related novel-view synthesis methods are commonly evaluated under capture and reconstruction conditions cleaner than those encountered by robots, drones, and autonomous systems. Benchmarks often rely on reconstruction-friendly trajectories, optimized camera poses and intrinsics, and held-out views sampled from trajectories represented during training. These assumptions can obscure performance with measured poses, reusable camera calibration, and structurally different camera paths. We introduce PIVOT (Pose, Intrinsics and Viewpoint Oriented Testbed), a multi-trajectory dataset, processing pipeline, and evaluation framework for independently studying these factors. PIVOT captures each scene using diverse camera trajectories and retains, where available, both sensor-derived measured poses and COLMAP-optimized poses, together with calibrated and optimized camera intrinsics. It defines three benchmark families: (1) seen versus unseen trajectory novel-view generalization, (2) measured versus optimized pose sensitivity, and (3) calibrated versus optimized intrinsics sensitivity. We also introduce a directed pose-space Chamfer distance to quantify how well training poses cover an evaluation trajectory. PIVOT v1 contains five real-world scenes captured with a DJI Mini 4 Pro and provides an open processing and Nerfstudio-based evaluation toolchain. Benchmark results show a consistent quality gap between held-out views on represented trajectories and unseen trajectories, as well as substantial sensitivity to pose source and camera intrinsics.

</details>

#### 2026-08-25 - Markerless Pose Estimation for Resistance Training Technique Assessment

**Authors:** Joseph Turner, Jeff Clark, Nawid Keshtmand
**Links:** [abs](https://arxiv.org/abs/2608.24384) - [pdf](https://arxiv.org/pdf/2608.24384)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Markerless Pose Estimation for Resistance Training Technique Assessment
- 作者：Joseph Turner, Jeff Clark, Nawid Keshtmand
- 出版日期：2026-08-25
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.24384

### 一句话总结
本文提出一种基于BlazePose的无标记姿态估计框架，从普通视频中提取关节角度轨迹，用于抗阻力训练（深蹲、卧推、硬拉）的技术评估，并以深蹲为主要案例验证其可行性。

### 研究问题
如何在无实验室设备、无物理标记点的条件下，利用普通视频实现对抗阻力训练动作的量化技术评估，以替代实验室-based运动分析的高门槛方案。

### 核心思路/方法
- 采用BlazePose模型从深蹲、卧推、硬拉视频中提取解剖学关键点。
- 将关键点转换为关节角度轨迹，以深蹲作为主要案例研究。
- 使用均方根误差（RMSE）将每次重复的轨迹与定义的参考重复进行对比评估。
- 通过轨迹对比实现重复间定量比较及组内技术变异性识别。

### 主要贡献
- 提出一个可直接从普通视频评估抗阻力训练技术的无标记姿态估计框架。
- 证明该框架能够恢复深蹲和硬拉有意义的运动学模式，实现重复间定量比较和技术变异性检测。
- 表明无标记姿态估计可在实验室外环境支持可访问的生物力学评估。

### 局限性
- 性能强烈依赖摄像机视角和视觉遮挡，非矢状面视角会扭曲二维关节角度估计。
- 摘要未提供更多详细信息（如模型精度指标、数据集规模、与其他方法对比等），故无法进一步展开；摘要未提供足够信息。

### 阅读优先级
**中**  
理由：研究面向运动训练中防损伤的实际应用，方法创新性一般（基于现成BlazePose），但结果受视角限制明显，且摘要未披露验证细节和对比实验，适用于关注运动分析、姿态估计应用的读者，学术突破性有限。

</details>

<details>
<summary>Abstract</summary>

Resistance training can be a high risk activity, and safe form is essential to avoiding injury. Laboratory-based movement analysis provides quantitive technique assessment, yet is not easily accessible. Markerless pose estimation infers body landmarks from images or video without physical markers and could offer a feasible alternative for technique assessment. We present a pose estimation framework to evaluate resistance-training technique from ordinary video footage. Using BlazePose, anatomical landmarks were extracted from squat, bench press, and deadlift videos and converted into joint-angle trajectories, with the squat serving as the primary case study. Trajectories were assessed against a defined reference repetition using root mean square error (RMSE). Results show that the framework recovers meaningful kinematic patterns for the squat and deadlift, enabling quantitative comparison between repetitions and identification of technique variability within a set. Performance depended strongly on camera orientation and visual occlusion, with non-sagittal views distorting 2D joint-angle estimates. The findings demonstrate that markerless pose estimation can support accessible biomechanical assessment outside laboratory environments.

</details>

#### 2026-08-25 - ExMesh++: From Multi-View Images to Relightable UV-PBR Mesh Assets via Topology-Adaptive Reconstruction and Decomposition

**Authors:** Chuanjin Fan, Lifan Wu, Wenjie Chang, Hanzhi Chang, Wenfei Yang, Tianzhu Zhang
**Links:** [abs](https://arxiv.org/abs/2608.24109) - [pdf](https://arxiv.org/pdf/2608.24109)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** multi-view reconstruction, surface reconstruction, inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ExMesh++: From Multi-View Images to Relightable UV-PBR Mesh Assets via Topology-Adaptive Reconstruction and Decomposition
- 作者：Chuanjin Fan, Lifan Wu, Wenjie Chang, Hanzhi Chang, Wenfei Yang, Tianzhu Zhang
- 出版日期：2026-08-25T06:16:03Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.24109

### 一句话总结
ExMesh++提出了一种分阶段框架，从多视角图像直接重建可重打光的UV-PBR网格资产，通过拓扑自适应优化和稳定的网格-UV载体实现几何、材质与光照的联合优化。

### 研究问题
如何从多视角图像重建不仅包含表面几何、还具备良好拓扑、有效UV参数化和显式PBR材质贴图的可编辑、可重打光的网格资产，同时缓解逆渲染中几何、材质与光照相互补偿导致的分解模糊问题。

### 核心思路/方法
- 采用分阶段（staged）框架，而非端到端联合优化。
- 第一阶段：自适应顶点分裂与合并，显式细化网格几何和拓扑，并在拓扑变化过程中保持UV一致性。
- 第二阶段：固定已得到的网格-UV载体，在UV空间中优化PBR贴图并联合优化环境光照。
- 在稳定载体基础上，通过次级光线追踪建模单次弹射的漫反射间接光照，并共享UV-PBR材质。

### 主要贡献
- 提出ExMesh++分阶段框架，能够从多视角图像重建可直接使用的可重打光UV-PBR网格资产。
- 通过自适应顶点分裂/合并实现拓扑优化，同时保持UV一致性。
- 在固定网格-UV载体上解耦优化PBR材质与光照，减少分解歧义。
- 引入基于次级光线追踪的单次弹射漫反射间接光照建模。
- 实验表明重建几何精度具有竞争力、重打光性能强，且导出资产可直接用于标准DCC工作流。

### 局限性
摘要未提供足够信息（未提及具体失败案例、方法在特定场景下的限制或量化误差分析）。

### 阅读优先级
**中**。理由：该工作面向可编辑、可重打光的PBR网格资产重建，属于三维重建与渲染的交叉方向，对关注工业级DCC工作流可用性的研究者有参考价值；但摘要未给出具体实验数值或对比基线细节，创新性主要体现在分阶段框架设计，若不属于该细分方向，优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

Multi-view reconstruction extends beyond surface recovery to editable and relightable mesh assets. Such assets require well-formed topology, valid UV parameterization, and explicit PBR material maps. Existing surface reconstruction approaches optimize implicit fields, Gaussian primitives, or other intermediate representations. Converting them into such assets often requires surface extraction and texture baking. Inverse-rendering methods estimate materials and illumination, yet these components often remain tied to neural fields or point-based primitives rather than the final mesh. Joint optimization of geometry, materials, and lighting may also allow these variables to compensate for one another, leading to ambiguous decomposition. To address these limitations, we present ExMesh++, a staged framework for reconstructing relightable UV-PBR mesh assets from multi-view images. The first stage refines explicit mesh geometry and topology through adaptive vertex splitting and merging, while maintaining UV consistency as the topology changes. The second stage fixes the resulting mesh-UV carrier and optimizes UV-space PBR maps together with environment lighting. Building on this stable carrier, ExMesh++ models one-bounce diffuse indirect illumination through secondary-ray tracing with shared UV-PBR materials. Experiments demonstrate competitive geometry accuracy, strong relighting performance, and direct usability of the exported assets in standard DCC workflows.

</details>

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-27 - Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS

**Authors:** Kangmin Seo, Jae-Pil Heo
**Links:** [abs](https://arxiv.org/abs/2608.26951) - [pdf](https://arxiv.org/pdf/2608.26951)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS
- 作者：Kangmin Seo, Jae-Pil Heo
- 出版日期：2026-08-27
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.26951

### 一句话总结
本文提出一种无需训练的过滤流程，利用前馈3D高斯泼溅中的逐视角高斯预测结构，自动剔除与多数输入视角不一致的瞬态干扰物，从而提升新视角渲染质量。

### 研究问题
在面向随意拍摄的多视角前馈3D高斯重建中，如何在不重新训练或无场景特定优化的前提下，消除仅出现在部分视角中的瞬态物体（干扰物），避免其在合成新视角时产生模糊、重复或漂浮伪影。

### 核心思路/方法
- 利用前馈3DGS的逐视角预测结构：对每个输入视角，排除其关联的高斯，并用剩余表示渲染同一相机视角，以暴露与其他输入不一致的内容。
- 通过特征相似度形成候选区域，再用渲染验证筛选候选：仅保留那些在移除后能降低其他输入视角重建误差的候选区域。
- 整个流程基于单一冻结预测，无需重训练或场景特定优化。

### 主要贡献
- 提出一种训练无关的干扰物过滤流程，直接作用于前馈3DGS的逐视角高斯预测。
- 在三个重建模型和两个干扰物基准上，验证了该方法在不同输入视角数量下均能持续改善新视角质量。
- 在干净场景下，对四个模型的评估显示原始重建结果基本得以保留，即过滤不会显著损害无干扰场景质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对前馈3DGS实际应用中常见的瞬态干扰物问题，提出了一种无需重新训练、即插即用的过滤方案，具有较高的实用价值；方法简洁且已在多个模型和基准上验证，适合关注3D重建、新视角合成及无训练后处理策略的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting reconstructs an explicit Gaussian representation from multiple input images in one network execution, making 3D reconstruction increasingly accessible for casual captures. However, such captures frequently contain transient objects that appear in only a subset of the views. Such content can be encoded into the per-view Gaussians associated with the inputs that observe it and remain in the combined representation despite being observed by no other input. As a result, it may produce blurred, duplicated, or floating artifacts in novel views. We introduce a training-free filtering procedure that exploits this per-view prediction structure. For each input, we exclude its associated Gaussians and render the same camera using the remaining representation, revealing content that is inconsistent with the other inputs. Feature similarity forms candidate regions, and rendering-based verification retains only candidates whose removal reduces reconstruction error in the other input views. The procedure operates on a single frozen prediction without retraining or scene-specific optimization. Across three reconstruction models and two distractor benchmarks, it consistently improves novel-view quality with varying numbers of input views. On clean scenes, evaluations across four models show that the original reconstructions are largely preserved.

</details>

#### 2026-08-27 - KISS-GS: 3D Gaussian Splatting Compression Kept Simple

**Authors:** Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann, Adrian Szatmari, Paul Schlack, Florian Barthel, Peter Eisert, Anna Hilsmann
**Links:** [abs](https://arxiv.org/abs/2608.26948) - [pdf](https://arxiv.org/pdf/2608.26948)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KISS-GS: 3D Gaussian Splatting Compression Kept Simple
- 作者：Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann, Adrian Szatmari, Paul Schlack, Florian Barthel, Peter Eisert, Anna Hilsmann
- 出版日期：2026-08-27T10:49:42Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.26948

### 一句话总结
KISS-GS 提出一种模块化、与训练解耦的 3D Gaussian Splatting 压缩管线，通过剪枝压缩、图像化格式编码及可选微调，实现 85x 到 319x 的场景体积缩减，并保持解码简单通用。

### 研究问题
如何设计一个模块化、透明且高效的 3DGS 压缩方法，在显著缩小场景文件大小的同时，保持各组件可独立复用、解码简单，并实现优于紧密集成方法的率失真性能。

### 核心思路/方法
- 完全解耦压缩与训练：对 vanilla 3DGS 重建的场景直接进行后处理压缩。
- 第一步：通过结合最先进的剪枝方案（compaction），实现 15.7x 的缩减。
- 第二步：将压缩后的高斯编码为基于图像的格式，便于简单、通用的解码（如 web 原生图像格式）。
- 提出 SOG-XT 格式，作为 Self-Organizing Gaussians 的扩展，包含两个主要创新：
  1. 自组织 2D 码本（Self-organizing 2D Codebooks）
  2. 并行代表分配平滑（PRAS）：利用四元数与尺度参数化的对称性，生成更利于编码的 2D 属性网格
- 可选步骤：编码感知的微调（encoding-aware fine-tuning），额外带来 2.2x 缩减。
- 整体管线模块化，各阶段可独立替换或结合未来进展。

### 主要贡献
- 提出 KISS-GS：一个原理简单、模块化的 3DGS 压缩管线，完全将压缩与训练解耦。
- 提出 SOG-XT 格式，包含自组织 2D 码本和 PRAS 两个新组件，用于生成更可编码的二维属性表示。
- 在标准 3DGS 基准上，实现 85x 至 319x 的总场景体积缩减率，超越紧密集成的方法，并在真实场景中设定新基准。
- 解码仅依赖 web 原生图像格式，保证通用性与简单性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作面向 3DGS 部署中的实际痛点（文件体积过大），提出了一套简单解耦、效果显著且可复用的压缩方案，在率失真性能上超越现有紧密集成方法，且代码公开。对于从事 3D 场景重建、压缩和实时渲染的研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Scene reconstruction with 3D Gaussian Splatting (3DGS) has become common, however deployment remains painful as the uncompressed file sizes can be massive. Current 3DGS compression systems combine multiple strategies for file size reduction, which can obscure where gains come from and limit component reuse across training pipelines. To make the gains more transparent, we propose KISS-GS, a modular compression pipeline named after the principle of keeping things simple, designed to decouple compression entirely from training. Given a 3DGS scene reconstructed with vanilla 3DGS, we are able to reduce it through compaction by 15.7x using a combination of state-of-the-art pruning schemes. Then we encode it into an image-based format designed for simple, ubiquitous decoding. With the SOG-XT format, we propose a novel extension to Self-Organizing Gaussians with two main contributions: (i) Self-organizing 2D Codebooks and (ii) Parallel Representative Assignment Smoothing (PRAS), which leverages the symmetry of quaternion and scale parameterizations to produce 2D attribute grids more amenable to encoding. This encoding reduces scene size by 6.6x. We show that optional encoding-aware fine-tuning yields a further 2.2x. Across standard 3DGS benchmarks, our simple and modular approach thus achieves a total of 85x to 319x reductions in the size of the scene over uncompressed vanilla 3DGS, setting new benchmarks for real-world scenes and surpassing tightly integrated methods in rate-distortion. Decoding relies solely on web-native image formats, and the modular design makes each stage easy to combine with future advances in reconstruction and compaction. Code and project page: https://fraunhoferhhi.github.io/KISS-GS/

</details>

#### 2026-08-27 - CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes

**Authors:** Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang
**Links:** [abs](https://arxiv.org/abs/2608.26656) - [pdf](https://arxiv.org/pdf/2608.26656)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** monocular depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes
- 作者：Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang
- 出版日期：2026-08-27
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.26656

### 一句话总结
CoGeo-GS提出一种概念驱动且几何感知的3D场景多物体移除框架，通过语义标签与几何补全管线，在单次优化中实现高质量多物体去除。

### 研究问题
如何在3D场景中高效且稳定地移除多个目标物体，同时保持几何与多视角一致性，避免现有3DGS方法在多物体场景下因遮挡、语义纠缠导致的重复优化和几何不稳定问题。

### 核心思路/方法
- 概念驱动的语义标签分配：为高斯点赋予概念感知的语义标签，支持灵活的目标物体选择，并减少前景物体与背景结构间的干扰，可在单次优化阶段完成多物体移除。
- 几何感知补全管线：融合单目深度先验、扩散模型细化以及边界对齐混合，恢复被移除区域的合理几何结构。
- 几何正则化细化策略：进一步稳定重建过程并保持多视角一致性。

### 主要贡献
- 提出CoGeo-GS，一个面向3D场景可控制多物体移除的概念驱动框架。
- 设计语义标签机制，实现在单一优化阶段内灵活选择多个目标并降低语义纠缠。
- 引入几何感知补全管线与几何正则化策略，提升移除区域的重建质量与多视角一致性。
- 实验表明CoGeo-GS在视觉质量与重建保真度上优于现有方法。

### 局限性
摘要未提供足够信息，无法得知该方法在极端遮挡、物体尺度差异、语义标签边界模糊、计算成本或实时性方面的具体局限。

### 阅读优先级
**高**
理由：该工作针对3DGS多物体场景编辑的痛点提出系统解决方案，结合语义标签与几何补全，属于神经场景表示与渲染方向的热点研究问题，且实验结果显示优于现有方法，对相关领域的研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Multi-object removal in 3D scenes is challenging due to severe occlusions, semantic entanglement, and the difficulty of maintaining geometric and multi-view consistency. Existing 3D Gaussian Splatting (3DGS) methods perform well for single-object editing but scale poorly to multi-object scenarios, often requiring repetitive optimization and yielding unstable geometry in removed regions. We propose CoGeo-GS, a concept-driven framework for controllable multi-object removal in 3D scenes. CoGeo-GS assigns concept-aware semantic tags to Gaussians, enabling flexible object selection and reducing interference between foreground objects and background structures within a single optimization stage. To recover plausible geometry, we introduce a geometry-aware completion pipeline that combines monocular depth priors with diffusion-based refinement and boundary-aligned blending. A geometry-regularized refinement strategy further stabilizes reconstruction and preserves multi-view consistency. Experiments demonstrate that CoGeo-GS outperforms existing methods in visual quality and reconstruction fidelity.

</details>

#### 2026-08-26 - PAGS: Autofocusing Photoacoustic Tomography via Speed-of-Sound-Adaptive Gaussian Splatting

**Authors:** Jiarui Ge, Jintao Ma, Bangxu Fan, Jinyan Zhang, Xiaokang Yang, Shuai Na, Xiaoyun Yuan
**Links:** [abs](https://arxiv.org/abs/2608.25472) - [pdf](https://arxiv.org/pdf/2608.25472)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PAGS: Autofocusing Photoacoustic Tomography via Speed-of-Sound-Adaptive Gaussian Splatting
- 作者：Jiarui Ge, Jintao Ma, Bangxu Fan, Jinyan Zhang, Xiaokang Yang, Shuai Na, Xiaoyun Yuan
- 出版日期：2026-08-26
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.25472

### 一句话总结
本文提出一种基于高斯溅射与声速自适应场联合优化的可微框架PAGS，用于在不依赖标定声速先验的情况下，对光声计算断层成像（PACT）中的声速异质性导致的失焦伪影进行盲自动对焦。

### 研究问题
PACT成像中，未知的声速（SoS）异质性会改变声波飞行时间，导致在假设均匀声速进行重建时出现失焦伪影。现有方法要么依赖标定的声学先验，要么优化稠密的物理介质模型，在三维场景下计算代价高且难以扩展。因此，需要一种无需先验、可扩展且高效的盲对焦重建方法。

### 核心思路/方法
- 用稀疏高斯光声（PA）源表示初始压力场，替代显式的介质恢复。
- 引入由球谐函数参数化的紧凑各向异性路径平均声速（ASoS）场，作为潜传播场，直接控制源到换能器的到达时间对齐。
- 通过解析高斯声学投影，将源表示高效映射为换能器信号。
- 构建闭环信号域优化：从测量数据中联合更新高斯PA源参数与ASoS场，全程无需标定SoS先验。

### 主要贡献
- 提出PAGS，一个用于PACT盲自动对焦的可微框架，统一了源表示与声速场估计。
- 用紧凑的球谐参数化ASoS场替代显式稠密介质模型，降低三维扩展难度与计算开销。
- 解析高斯声学投影带来计算效率优势。
- 在模拟与物理体模实验上验证了异质声学介质下的重建清晰度提升、稀疏视图采样下的稳健性，以及计算上的收益。

### 局限性
摘要未提供足够信息。论文未明确讨论对极端声速异质性、真实组织非均匀性的泛化边界、可扩展性的具体量化指标，也未提及对噪声或数据缺失的具体鲁棒性分析。

### 阅读优先级
**中**  
理由：该方法将高斯溅射引入光声断层成像，新颖性较高，且无需声速先验和稠密介质建模，对计算成像方向有一定参考价值。但属于专业性强的交叉领域，且摘要未提供与其他SOTA方法的定量对比，影响快速判断其相对优势的紧迫性。若关注无先验声速校正或可微成像，建议阅读；否则可暂缓。

</details>

<details>
<summary>Abstract</summary>

Photoacoustic computed tomography (PACT) combines optical absorption contrast with acoustic detection for high-resolution deep-tissue imaging. A persistent challenge is that unknown speed-of-sound (SoS) heterogeneity changes acoustic time-of-flight, causing defocusing artifacts when reconstruction assumes a uniform SoS. Existing SoS-adaptive methods either rely on calibrated acoustic priors or optimize dense physical medium models, which becomes expensive and difficult to scale in 3D. We propose PAGS, a differentiable framework for blind autofocusing PACT via speed-of-sound-adaptive Gaussian splatting. PAGS represents the initial pressure field with sparse Gaussian photoacoustic (PA) sources and replaces explicit medium recovery with a compact anisotropic path-averaged SoS (ASoS) field parameterized by spherical harmonic probes. This latent propagation field directly controls source-to-transducer arrival-time alignment, while an analytic Gaussian acoustic projection maps the source representation to transducer signals efficiently. The resulting closed-loop signal-domain optimization jointly updates the Gaussian PA source parameters and the ASoS field from measured data, without calibrated SoS priors. Experiments on simulated and physical phantom data demonstrate improved reconstruction sharpness under heterogeneous acoustic media, robustness to sparse-view sampling, and computational benefits from the analytic Gaussian projection.

</details>

## Embodied / Robotics / AR Applications

### 2026-08

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

#### 2026-08-27 - SpatialCrafter: Single Image World Modeling with Generative 3D Proxies

**Authors:** Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan
**Links:** [abs](https://arxiv.org/abs/2608.27073) - [pdf](https://arxiv.org/pdf/2608.27073)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, virtual reality, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialCrafter: Single Image World Modeling with Generative 3D Proxies
- 作者：Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan
- 出版日期：2026-08-27T12:58:37Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.27073

### 一句话总结
SpatialCrafter 提出一种两阶段图像到三维场景生成框架，通过引入全局三维代理（3D Proxy）结合视频扩散模型，实现高保真、几何一致且抗长时间漂移的可探索场景生成。

### 研究问题
如何基于单张图像生成可自由探索的 3D 场景，同时克服现有视频扩散模型在稀疏点云或 2D 全景条件下产生的随机幻觉、长时间漂移和三维一致性不足的问题。

### 核心思路/方法
- 将生成过程分解为全局代理生成（Global Proxy Generation）与外观细化（Appearance Refinement）两个阶段。
- 提出 Point-anchored Sparse Structure (PaSS) Flow 模块，用于预测空间对齐且几何一致的 3D 代理。
- 将视频扩散模型重新定位为 Generative Deferred Refiner，在代理定义的场景几何上合成高频逼真细节。
- 引入 Parallel Geometry Injection 和 Proxy-Aware Corruption 训练策略，提升对代理瑕疵的鲁棒性，同时不干扰预训练生成流形。
- 新建了一个包含 115K 场景的大规模混合数据集，用于图像到场景生成任务训练。

### 主要贡献
- 提出两阶段图像到场景生成框架，引入全局 3D 代理以改善一致性和漂移问题。
- 设计 PaSS Flow 模块，用于生成几何一致的 3D 代理。
- 提出两种训练策略（Parallel Geometry Injection 与 Proxy-Aware Corruption），有效集成代理与预训练 VDM。
- 构建并公开首个用于图像到场景生成的混合数据集（115K 场景）。
- 在合成与真实数据集上，SpatialCrafter 在快速相机运动和极端视角变化下优于现有方法，且保持鲁棒性和一致性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该研究针对图像到 3D 场景生成中的关键难题（3D 一致性、长时间漂移）提出了系统性两阶段解决方案，并配套公开新数据集，对机器人、VR/AR 和游戏等领域有潜在应用价值；实验覆盖合成及真实场景，评估维度较全面，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Explorable image-to-scene generation is essential for applications in gaming, robotics, and virtual reality. Existing methods based on video diffusion model (VDM) commonly rely on incomplete conditioning signals such as sparse point clouds or 2D panoramas, leading to stochastic hallucinations, long-term drifts and suboptimal 3D consistency. We present SpatialCrafter, a novel two-stage framework that addresses these issues by introducing a global 3D proxy for high-fidelity image-to-scene generation. Specifically, we decompose the generation process into global proxy generation and appearance refinement. For proxy generation, we propose a Point-anchored Sparse Structure~(PaSS) Flow module that predicts a spatially aligned and geometrically consistent 3D proxy. For appearance refinement, we re-frame the VDM as a Generative Deferred Refiner which synthesizes high-frequency photorealistic details upon proxy-defined scene geometry. To better integrate the proxy with the pre-trained VDM, we introduce Parallel Geometry Injection and Proxy-Aware Corruption training strategies, which improve robustness to proxy artifacts without disrupting the pretrained generative manifold. Furthermore, as no suitable dataset exists for this explorable scene generation task, we construct a new large-scale dataset of 115K scenes. To the best of our knowledge, it is the first hybrid dataset for image-to-scene generation. Extensive experiments on both synthetic and real-world datasets show that SpatialCrafter outperforms state-of-the-art methods, mitigates long-term drift, and remains robust and consistent under rapid camera motion and extreme viewpoint changes. Code, models, and the newly constructed dataset will be publicly released. See more at https://fangchuan.github.io/SpatialCrafter/.

</details>

#### 2026-08-27 - Contact-Aided Factor-Graph Localization for Underwater Sampling

**Authors:** Michele Grimaldi, Yosaku Maeda, Hitoshi Kakami, Ignacio Carlucho, Yvan R. Petillot, Tomoya Inoue
**Links:** [abs](https://arxiv.org/abs/2608.26932) - [pdf](https://arxiv.org/pdf/2608.26932)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Contact-Aided Factor-Graph Localization for Underwater Sampling
- 作者：Michele Grimaldi、Yosaku Maeda、Hitoshi Kakami、Ignacio Carlucho、Yvan R. Petillot、Tomoya Inoue
- 出版日期：2026-08-27
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26932

### 一句话总结
本文提出一种在退化水下环境中利用机械臂接触事件作为几何约束的因子图定位框架，以降低水下采样任务的轨迹漂移并提升重访精度。

### 研究问题
自主水下机器人在近距离海底采样时，由于低空下视相机面对平坦无纹理海底而产生尺度模糊和横向退化，传统惯性-DVL融合缺乏结构漂移校正机制，如何实现鲁棒的状态估计是一个关键挑战。

### 核心思路/方法
- 将基于吸盘的机械臂接触事件建模为高置信度因子，融入平滑式因子图定位框架，形成隐式回环闭合，无需依赖外观场景识别。
- 紧密融合自适应视觉里程计、学习式目标检测和机载传感器。
- 视觉里程计相对位姿因子与地标方位-距离因子根据内点统计进行不确定性缩放，避免弱视觉帧破坏估计稳定性。
- 系统可在运动过程中完全在线初始化。

### 主要贡献
- 提出接触辅助的因子图定位框架，将物理交互作为信息性几何约束引入定位。
- 通过接触事件实现无需外观识别的隐式回环闭合。
- 设计了基于内点统计的不确定性缩放机制，增强视觉退化条件下的鲁棒性。
- 实验验证在罐体、港口及仿真环境中，接触约束显著降低轨迹漂移并提升目标重访精度，优于滤波式导航和无接触图优化方案。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作针对水下退化环境的定位问题提出新颖的接触辅助因子图方法，robotics定位方向研究者有一定参考价值；但实验为摘要级概述，缺少定量细节，且领域相对专门化，综合优先级定为中。

</details>

<details>
<summary>Abstract</summary>

Accurate state estimation for autonomous underwater vehicles performing close-range seafloor sampling remains challenging. In low-altitude operation, down-looking cameras over featureless planar seabeds produce scale ambiguity, lateral degeneracy, and inconsistent feature tracking. Meanwhile, inertial-Doppler Velocity Log (DVL) fusion alone provides no mechanism for structural drift correction. We propose a Contact-Aided Factor-Graph Localization framework that treats physical interaction as an informative geometric constraint within a smoothing-based localization formulation. The method tightly fuses suction-based manipulator contact events with adaptive visual odometry, learned object detections, and on-board sensors. Visual odometry relative-pose factors and landmark bearing-range factors are uncertainty-scaled according to inlier statistics to prevent visually weak frames from destabilizing the estimator, while contact events are modeled as high-confidence factors that induce implicit loop closures without appearance-based place recognition. Furthermore, the system can fully initialize online during motion. Experimental evaluation in tanks, harbor, and simulation environments demonstrates that contact-induced constraints significantly reduce trajectory drift and improve object revisit accuracy compared to filtering-based navigation and contact-free graph formulations. These results highlight the role of embodied physical interaction as a localization primitive in perception-degraded underwater environments

</details>

#### 2026-08-27 - Decoupling Planning and Control for Instructable Agents

**Authors:** Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr
**Links:** [abs](https://arxiv.org/abs/2608.26788) - [pdf](https://arxiv.org/pdf/2608.26788)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Decoupling Planning and Control for Instructable Agents
- 作者：Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr
- 出版日期：2026-08-27T08:17:58Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26788

### 一句话总结
本文提出Instruct-to-Act系统，将VLM的高层规划能力与世界模型控制器的快速低层控制能力解耦结合，使控制器能根据语言指令在陌生环境中高频自主行动。

### 研究问题
如何将预训练视觉语言模型（VLM）的高层规划能力与世界模型控制器的快速控制能力结合，以解决VLM难以生成可靠低延迟动作序列、而世界模型控制器缺乏开放任务引导的问题。

### 核心思路/方法
- 系统架构：Instruct-to-Act，VLM规划器生成稀疏、高延迟的高层文本指令，训练好的世界模型控制器以高频方式根据这些指令自主行动。
- 控制器训练：将控制器策略回放片段用合成指令重新标注，并在现有奖励最大化与世界建模目标之外，联合优化行为克隆目标，使控制器具备语言可引导性。
- 评估设计：在七个具身环境（含三个多智能体环境）中进行测试，VLM规划器通过语言协调，训练后的控制器作为执行器。

### 主要贡献
1. 提出解耦规划与控制的Instruct-to-Act框架，兼顾VLM的开放任务理解与控制器的高速执行。
2. 通过合成指令重标注+联合行为克隆训练，使现有世界模型控制器具备语言引导能力。
3. 在匹配观测与动作空间条件下，解耦方法一致优于仅控制器和直接VLM生成动作的变体。
4. 支持直接替换不同预训练VLM规划器而无需微调，且在七个任务中六个任务上保持与强基线（视觉-语言-动作模型、多智能体RL）竞争力。

### 局限性
摘要未提供足够信息，未提及计算资源需求、部署延迟具体数值、失败案例分析、对不同环境泛化能力差异的深入讨论，以及与其他方法在剩余一个任务上对比结果不佳的具体原因。

### 阅读优先级
**高**。理由：该工作提出了一种新颖且通用的架构解耦思路（VLM规划+世界模型控制），在多个环境包括多智能体场景中验证有效，且具有即插即用VLM规划器的实际价值；研究问题切中当前VLM具身应用的核心瓶颈（规划与控制冲突），对相关领域研究者有较强参考意义。

</details>

<details>
<summary>Abstract</summary>

Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model controller to act autonomously at high frequency when conditioned on sparse, higher-latency, and high-level text instructions generated by a VLM planner. To train controllers to be language-instructable, we relabel segments of controller policy rollouts with synthetic instructions and jointly optimize a behavior-cloning objective along with existing reward-maximizing and world-modeling objectives. We evaluate our proposed approach across seven embodied environments, including three multi-agent environments where VLM planners coordinate through language while trained controllers serve as their actuators. Under matched observation and action spaces, our decoupled approach consistently outperforms controller-only and direct VLM action-generation variants, preserves fast control, and lets us swap in different pretrained VLM planners without fine-tuning, while remaining competitive with strong vision-language-action and multi-agent RL baselines on six of seven tasks.

</details>

#### 2026-08-26 - Gating Before Commitment: Anticipating Intent Divergence to Prevent Post-Interaction Decision Failures in Autonomous Driving

**Authors:** Cong Xu, Ravi Sankar
**Links:** [abs](https://arxiv.org/abs/2608.26074) - [pdf](https://arxiv.org/pdf/2608.26074)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gating Before Commitment: Anticipating Intent Divergence to Prevent Post-Interaction Decision Failures in Autonomous Driving
- 作者：Cong Xu, Ravi Sankar
- 出版日期：2026-08-26
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26074

### 一句话总结
本文提出一种在自动驾驶规划提交前进行“意图分歧门控”的决策层，通过在结构化描述符上计算平滑的意图-几何分歧分数，对计划进行提前拦截，从而防止交互后决策失败。

### 研究问题
自动驾驶中车辆交互时的意图误读会导致反复出现的规划失败，本文研究如何在计划承诺之前预判意图分歧并采取门控干预，以避免事后决策失效。

### 核心思路/方法
- 设计一个决策层，包含语言引导的意图模块，读取结构化描述符并计算平滑的意图-几何分歧得分。
- 在规划走廊包络（corridor envelope）之前设置门控机制，在计划提交前拦截有问题的规划动作。
- 在冻结、公开的实现下，对重放的越野偏离和四个碰撞片段进行测试。
- 通过初步校准和预注册重设计（将不确定性视为弃权）来减少误触发。
- 通过两个消融实验评估模型贡献：对比完整得分与其他规则（如未否决规则和几何规则）的检测性能。

### 主要贡献
- 提出并验证了“门控在承诺之前”的决策机制，是所测试中唯一能修复计划的层。
- 主案例中，门控在漂移开始后72 ms触发，但在走廊出口前161 ms触发，并在全部十次重放中保持轨迹在走廊内。
- 预注册重设计将首次校准中每5.9分钟出现9次误触发的情况降至每分钟0.341次。
- 消融实验表明：完整得分在四个（部署资格条件）或三个（未否决规则）失败案例中检测最快；几何规则在域内轨道上同等误报率下检测数量增加三倍以上。
- 证据支持门控机制本身有效，模型的具体作用既包括在失败案例上最快检测，也包括对几何规则提供不确定性否决。

### 局限性
- 摘要未明确列出实验环境的具体规模、真实路测条件或泛化性评估，因此缺乏对更广泛驾驶场景的验证信息。
- 摘要未提供关于计算开销、实时性要求或集成到完整自动驾驶系统的具体细节。
- 摘要未描述误触发减少的具体机制参数（除了“不确定性作为弃权”）及其在更复杂交互中的适用性，摘要未提供足够信息。
- 未披露数据集的规模和多样性、基线方法对比的完整范围等信息，摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该文聚焦于自动驾驶交互决策中的意图分歧检测与门控机制，问题具体且方法有一定创新性，但摘要中实验规模、对比基线和泛化细节有限，对非专门从事自动驾驶决策层的研究者参考价值相对有限。对于从事机器人规划、人机交互和可解释决策系统的读者而言，其门控思路与不确定性处理方式具有参考意义。

</details>

<details>
<summary>Abstract</summary>

Intent misinterpretation during vehicle interactions causes recurring planning failures. We study a decision layer in which a language-guided intent module reads structured descriptors, computes a smoothed intent-geometry divergence score, and gates the planned maneuver before commitment, upstream of a corridor envelope. On a replayed off-road departure and four crash clips under a frozen, disclosed implementation, gating is the only layer that repairs the plan: on the main case it fires 72 ms after the drift onset but 161 ms before the corridor exit, keeping the trajectory in the corridor in all ten replays. The first calibration draws nine false triggers in 5.9 minutes, each from scoring uncertainty as half a conflict; a preregistered redesign treating uncertainty as abstention cuts this to 0.341 per minute. Two ablations bound the model's contribution: the full score detects fastest on four of five failures under the deployed eligibility, three of five against the unvetoed rule (000871 by one cycle; 000228 by a pre-onset fire on an uncertain stretch that five clips cannot classify as signal or coincidence; dropping the confidence term costs two detections), while on in-domain tracks at equal false positives the geometric rule more than triples its detection. The evidence supports the gating mechanism; the model's demonstrated roles are the fastest detection on these failures and an uncertainty veto on the geometric rule.

</details>

#### 2026-08-26 - One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation

**Authors:** Xiaomi Embodied Intelligence Team, University of Macau, :, Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang
**Links:** [abs](https://arxiv.org/abs/2608.26058) - [pdf](https://arxiv.org/pdf/2608.26058)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation
- 作者：小米具身智能团队，澳门大学，Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang
- 出版日期：2026-08-26
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.26058

### 一句话总结
UCAG-P提出了一种以相机为中心的几何统一动作表示方法，将异构具身操作数据对齐到共享几何空间，使单个视觉-语言-动作（VLA）策略能在多种机器人形态上训练并实现跨形态泛化。

### 研究问题
异构具身数据的固有差异（不同的机器人形态、相机配置和底层动作空间）严重限制了通用VLA策略的规模化训练，现有方法通常依赖显式动作重定向、人-机器人视频合成或数据集专属适配分支，难以实现统一策略的联合学习。

### 核心思路/方法
- 提出**相机中心统一动作公式（UCAG-P）**，将异构具身数据集在结构上对齐到一个共享的几何动作空间。
- 不再将机器人专属指令作为共享策略目标，而是通过**图像坐标和相机坐标系中的可观测锚点运动**来表示操作，将机械臂、人形机器人和人手视为统一动作模式的不同具体形态。
- 设计**几何条件动作翻译器（geometry-conditioned action translator）**，将预测的运动与目标形态的运动学结合，生成可执行控制指令。
- 采用**解耦架构**，使共享VLA策略学习可迁移的操作几何，同时保留形态专属的可控性。

### 主要贡献
- 提出一种新的相机中心统一动作公式，从结构上解决异构具身数据的对齐问题，无需显式动作重定向或数据集专属分支。
- 构建解耦的预训练架构，在共享策略学习与形态专属控制之间取得平衡。
- 在**4.03K小时机器人/仿真数据与2.34K小时人类演示数据**上进行训练。
- 单一检查点无需基准专属微调即达到：LIBERO 98.3%、RoboTwin Easy/Hard 88.7%/89.2%、LIBERO-Plus零样本 82.0%、RoboCasa GR-1 62.0%。

### 局限性
摘要未提供足够信息，例如方法在未见过的极端形态或复杂动态场景下的表现、几何翻译器的计算开销、以及不同相机配置下的鲁棒性等均未提及。

### 阅读优先级
**高**。理由是：该工作针对VLA策略规模化训练中的核心瓶颈（异构数据对齐）提出了新颖的统一动作几何公式，训练数据规模大（累计超过6K小时），并在多个基准上取得了无需微调的高性能，同时包含零样本泛化评测，对具身智能和机器人操作领域具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Scaling generalist vision-language-action (VLA) policies is severely bottlenecked by the inherent heterogeneity of embodied data, which spans diverse robot morphologies, camera configurations, and low-level action spaces. Existing paradigms typically address this mismatch through explicit action retargeting, human-to-robot video synthesis, or dataset-specific adaptation branches, fundamentally hindering the joint learning of a unified policy. We introduce UCAG-P, a camera-centric unified action formulation that structurally aligns heterogeneous embodied datasets into a shared geometric action space. Rather than treating robot-specific commands as the shared policy target, UCAG-P represents manipulation through camera-observable anchor motion in image and camera-frame coordinates, treating robot arms, humanoids, and human hands as different embodiments of a common action schema. A geometry-conditioned action translator combines predicted motion with target-embodiment kinematics to produce executable controls. The resulting decoupled architecture allows a shared VLA policy to learn transferable manipulation geometry while retaining embodiment-specific controllability. UCAG-P is trained on 4.03K hours of robot and simulation data and 2.34K hours of human demonstrations. A single checkpoint reaches 98.3% on LIBERO, 88.7% and 89.2% on RoboTwin Easy and Hard, 82.0% zero-shot on LIBERO-Plus, and 62.0% on RoboCasa GR-1, without benchmark-specific fine-tuning.

</details>

#### 2026-08-25 - Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training

**Authors:** Wenxuan Shen, Dongna Jin, Dongping Chen
**Links:** [abs](https://arxiv.org/abs/2608.24680) - [pdf](https://arxiv.org/pdf/2608.24680)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training
- 作者：Wenxuan Shen, Dongna Jin, Dongping Chen
- 出版日期：2026-08-25
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.24680

### 一句话总结
本文提出Game2World引擎和GameCleaner模型，用于从真实游戏视频中自动去除UI覆盖层，从而将海量互联网游戏视频转化为高质量的世界模型训练数据。

### 研究问题
原始游戏视频中，游戏世界与屏幕空间界面（UI/HUD）混杂在一起，引入了游戏特定的偏差和无关动态，阻碍了视频世界模型的训练效果。因此，如何自动、高效地从真实游戏视频中去除UI元素，同时保留场景内容与时间动态，是一个关键挑战。

### 核心思路/方法
- 提出**GameUI-Taxonomy**，形式化定义了游戏UI的类别体系。
- 构建全栈框架**G2WEngine**，能够从真实游戏视频中自动提取可复用的UI资产，并在干净画面上合成时间上连贯的UI叠加层，用于生成成对训练数据。
- 基于该引擎构建**Game2World**数据集，包含96K合成成对视频（带精确重建目标）和来自303款游戏的1,079条真实世界视频片段，用于真实场景评估。
- 提出**GameCleaner**，一种无需掩码的游戏UI去除模型，结合多模态语义理解与视频编辑能力，直接识别并去除多种HUD元素，同时保留底层场景内容与时间动态。

### 主要贡献
- 提出形式化的GameUI-Taxonomy和全栈G2WEngine框架。
- 构建大规模Game2World数据集及包含5,132个已验证UI元素的资产库（覆盖21个类别，来自1,010个代表性游戏帧）。
- 提出无需掩码的UI去除模型GameCleaner，并证明其在合成和真实视频上的有效性。
- 实验显示，基于去除UI后视频训练的世界模型，VideoReward比基于带UI视频训练的模型提升6.83%；GameCleaner在合成视频上平均AAR达到95.36，比最强的时序掩码基线提升57.3%，在真实视频上达到80.05的AAR，且背景保持率达99.8%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对世界模型训练数据预处理这一关键问题，提出了完整的数据工程框架和模型，并展示了显著的量化收益；数据集和代码即将开源，对游戏视频理解和世界模型领域研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Video games provide a scalable source of training data for video world models, offering diverse environments, complex interactions, and abundant in-the-wild gameplay videos. However, raw gameplay footage entangles the game world with screen-space interfaces, introducing game-specific biases and irrelevant dynamics that hinder world-model training. To address this problem, we introduce GameUI-Taxonomy and G2WEngine, a full-stack framework that formalizes gameplay UI grounding and removal. G2WEngine automatically extracts reusable UI assets from real gameplay videos and synthesizes temporally coherent UI overlays on clean footage. Using this engine, we construct Game2World, comprising 96K synthetic paired videos with precise reconstruction targets and 1,079 in-the-wild clips from 303 games for realistic evaluation. Its asset library contains 5,132 verified UI elements across 21 taxonomy categories, collected from 1,010 representative gameplay frames. Based on Game2World, we propose GameCleaner, a mask-free gameplay UI removal model that combines multimodal semantic understanding with video editing capabilities. Unlike mask-based methods, GameCleaner directly identifies and removes diverse HUD elements while preserving the underlying scene content and temporal dynamics. In a controlled pilot, world models trained on UI-free gameplay improve overall VideoReward by 6.83% over those trained on UI-overlaid data. On UI-removal evaluation, GameCleaner achieves an average AAR of 95.36 on synthetic videos, outperforming the strongest temporal mask baseline by 57.3%, and obtains the best in-the-wild AAR of 80.05 with 99.8 background preservation. These results demonstrate the scalable potential of transforming Internet gameplay videos into high-quality world-model training data. Code, dataset, and model will be available at https://github.com/Dongping-Chen/Game2World.

</details>

#### 2026-08-25 - VizAnchor: Decoding Manipulation Intent from Tampering Visualizations via Dual-Anchor Reasoning

**Authors:** Xiaotian Zhang, Huayuan Ye, Haiyang Zhang, Chenhui Li, Changbo Wang, Sicheng Song
**Links:** [abs](https://arxiv.org/abs/2608.24535) - [pdf](https://arxiv.org/pdf/2608.24535)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VizAnchor: Decoding Manipulation Intent from Tampering Visualizations via Dual-Anchor Reasoning
- 作者：Xiaotian Zhang, Huayuan Ye, Haiyang Zhang, Chenhui Li, Changbo Wang, Sicheng Song
- 出版日期：2026-08-25
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.24535

### 一句话总结
VizAnchor是一个基于双锚点（语义锚与空间锚）和VLM推理的框架，用于理解可视化图表中的操纵行为，包括定位篡改区域、还原原始信息并推断误导意图。

### 研究问题
现有方法只能定位被篡改的区域或恢复隐藏信息，无法解释可视化是如何被操纵的，以及这些改动为何会误导观众。本文旨在解决这一空白，实现从篡改可视化中解码操纵意图。

### 核心思路/方法
VizAnchor分为两个阶段：
1. **双锚点构建**：构建语义锚点以恢复真实的图表信息，构建空间锚点以定位被篡改的区域。
2. **三智能体推理**：
   - **误导者定位智能体**：通过分析四面板视觉提示，预测误导性信息；
   - **图表叙事重建智能体**：以原始图表和篡改图表为输入，分别重建其视觉叙事；
   - **意图推断智能体**：整合视觉证据与误导者信息，推断误导意图。

此外，作者构建了两个数据集，分别用于篡改定位和误导意图推断。

### 主要贡献
- 提出VizAnchor框架，首次将篡改可视化的理解从“定位/恢复”推进到“意图解码”层面；
- 设计双锚点证据构建机制，结合VLM推理进行多层次分析；
- 构建用于篡改定位和误导意图推断的数据集；
- 实验表明VizAnchor能准确定位篡改区域，并对操纵方式、误导者和误导意图产生可信的解释。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作聚焦数据可视化安全与误导性图表理解，属于交叉方向，方法上采用了VLM+多智能体框架，有一定新颖性。但摘要中未给出定量实验细节或与现有方法的对比结果，且分类为Embodied/Robotics/AR方向，与可视化安全略显错位，建议对可视化和AI安全交叉领域感兴趣的读者优先关注。

</details>

<details>
<summary>Abstract</summary>

Data visualizations are widely used for communicating information, but they are also vulnerable to intentional manipulations that induce misleading interpretations. Existing methods focus on locating tampered regions or recovering hidden information, without explaining how the visualization has been manipulated or why the resulting changes may mislead viewers. We propose \textbf{VizAnchor}, a framework for visualization manipulation understanding through dual-anchor evidence construction and VLM-based reasoning. In the first stage, VizAnchor constructs a semantic anchor to recover authentic chart information and a spatial anchor to localize tampered regions. In the second stage, three specialized agents decode the manipulation. The misleader grounding agent analyzes a four-panel visual prompt to predict the misleader information. The chart narrative reconstruction agent takes the original and tampered charts as inputs and reconstructs their respective visual narratives. Finally, the intent inferring agent integrates the visual evidence and misleader information to infer the misleading intent. We further construct a dataset for tampering localization and a dataset for misleading intent inferring. Evaluation shows that VizAnchor accurately localizes manipulations and produces faithful explanations of their manipulation, misleaders, and misleading intents.

</details>

#### 2026-08-25 - NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation

**Authors:** Yumeng He, Yichen Song, Xiaotian Yang, Weijia Zhang, Zanwei Zhou, Junru Gong, Xiaokang Yang, Yunbo Wang
**Links:** [abs](https://arxiv.org/abs/2608.24212) - [pdf](https://arxiv.org/pdf/2608.24212)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, embodied AI, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation
- 作者：Yumeng He, Yichen Song, Xiaotian Yang, Weijia Zhang, Zanwei Zhou, Junru Gong, Xiaokang Yang, Yunbo Wang
- 出版日期：2026-08-25
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.24212

### 一句话总结
NeoWorld-Pro 提出一种将单目图像重建为可交互3D场景的程序化编程框架，利用多模态大语言模型生成场景程序，并通过物理引擎闭环迭代优化，实现对物体几何、关节和物理属性的可验证重建。

### 研究问题
如何将单张RGB图像转换为具备物理合理性、场景级交互性和精确空间关系的仿真就绪3D场景，以克服现有图像到URDF方法缺乏物理支撑和交互能力的问题。

### 核心思路/方法
- 将单目场景重建重新定义为“程序化编程”任务：使用多模态大语言模型（MLLM）的零样本推理与代码合成能力，将一张RGB图像转换为可执行程序，程序中指定物体几何、关节结构和物理属性。
- 引入“物理在环”（physics-in-the-loop）迭代机制：生成程序后在物理引擎中执行并验证，根据执行结果不断修正程序，确保关节运动合理、物体组合与交互有效、空间关系准确。

### 主要贡献
- 提出针对单目图像重建的交互式场景编程框架，将重建问题转化为程序生成与验证问题。
- 设计了物理在环的迭代优化机制，使生成场景具备物理合理性和可交互性。
- 实验表明方法优于开环方法和先前单目重建方法，并可支持复杂下游任务（如稳定堆叠和精细操作）。

### 局限性
摘要未提供足够信息，包括对失败案例的讨论、对计算开销或运行效率的分析、以及对不同场景类型（如动态场景或极端光照）的适用性评估。摘要也未提及与现有重建方法在定量指标上的具体对比数值。

### 阅读优先级
**高**  
理由：该工作直接面向具身智能对高质量仿真资产的需求，提出结合MLLM代码生成与物理闭环验证的新范式，创新性强且实验表明能支撑堆叠、精细操作等关键下游任务，对Embodied AI和仿真领域具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

The advancement of Embodied AI necessitates high-quality simulation assets that faithfully mirror the real world. However, transforming raw visual observations into simulation-ready scenes remains challenging due to the lack of physical grounding and scene-level interactivity in current image-to-URDF methods. We propose NeoWorld-Pro, a framework that reformulates monocular scene reconstruction as procedural programming for interactive 3D environments. Leveraging the zero-shot reasoning and code synthesis capabilities of MLLMs, NeoWorld-Pro converts a single RGB image into executable programs specifying object geometry, articulation, and physical properties. A physics-in-the-loop mechanism then iteratively refines the generated programs by validating their execution in a physics engine, enforcing physically plausible articulations, valid object compositions and interactions, and accurate spatial relationships. Experiments show that NeoWorld-Pro outperforms open-loop and prior monocular reconstruction methods, while enabling complex downstream tasks such as stable stacking and fine-grained manipulation.

</details>

#### 2026-08-25 - SceneReGen: Generative Reconstruction of 3D Scenes from a Single Image

**Authors:** Zefan Tian, Yuteng Ye, Yiheng Zhang, Yuhang Yang, Xueqiang Lv, Shizhou Zhang, Le Liu, Di Xu
**Links:** [abs](https://arxiv.org/abs/2608.23930) - [pdf](https://arxiv.org/pdf/2608.23930)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, embodied AI, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SceneReGen: Generative Reconstruction of 3D Scenes from a Single Image
- 作者：Zefan Tian, Yuteng Ye, Yiheng Zhang, Yuhang Yang, Xueqiang Lv, Shizhou Zhang, Le Liu, Di Xu
- 出版日期：2026-08-25
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.23930

### 一句话总结
SceneReGen 提出一种生成式重建框架，将单图像三维场景重建转化为在共享观测对齐场景坐标系中生成并装配完整物体资产，通过选择性位姿分解弥补物体生成与场景重建间的表征差距。

### 研究问题
如何从单张图像进行三维场景重建，在补全部分被遮挡物体的同时，将其连贯地放置于共享的、与观测对齐的场景坐标系中。核心难点在于物体级生成先验的输出是居中、尺度归一化的物体坐标系表达，与场景级重建所需的观测对齐场景坐标系存在表征差距。

### 核心思路/方法
- 将场景重建重新定义为“完整物体资产的生成与装配”问题，所有资产统一在共享的观测对齐场景坐标系中表达。
- 通过选择性位姿分解（selective pose factorization）处理生成-重建差距：物体的观测朝向直接编码在生成网格中，而平移和尺度则从实例级与全局场景证据中估计。
- 网络结构包括：几何编码器（从场景图像和实例掩码提取密集线索）、可学习的形状查询（条件化预训练的基于 DiT 的三维生成器，生成保持观测朝向的完整网格）、以及位置查询（融合物体与场景特征，用于在共享坐标系中装配物体）。

### 主要贡献
- 提出 SceneReGen 框架，弥合物体级生成先验与场景级重建之间的表征差距。
- 设计选择性位姿分解策略，将朝向编码于生成网格中，平移和尺度通过实例与全局证据估计。
- 在 3D-FUTURE 评估子集上，场景级 CD、场景级 F-Score 和三维边界框 IoU 均取得最优，物体级 CD 并列最优，物体级 F-Score 排名第二。
- 在自动驾驶与具身智能场景中的定性结果展示了面向资产生成的重建方法在室内家具之外的潜力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单图像三维场景重建中的表征差距问题提出了新的生成式框架，在标准数据集上取得了多项最优指标，且应用场景涉及自动驾驶与具身智能等热门领域，方法新颖且评估结果明确，值得细读。

</details>

<details>
<summary>Abstract</summary>

Single-image 3D scene reconstruction must complete partially observed objects and place them coherently in a shared observation-aligned scene frame. Object-level generative priors offer strong completion ability, but their centered, scale-normalized outputs are typically expressed in an object frame, creating a fundamental representation gap between object generation and scene reconstruction. We introduce SceneReGen, a generative reconstruction framework that reinterprets scene reconstruction as the generation and assembly of complete object assets in a shared observation-aligned scene frame. SceneReGen addresses the generation-reconstruction gap through selective pose factorization: each object's observed orientation is encoded directly in the generated mesh, while translation and scale are estimated from instance-level and global scene evidence. Given a scene image and instance masks, a geometry encoder extracts dense cues; learnable shape queries condition a pretrained DiT-based 3D generator to produce complete meshes in their observed orientations, while position queries fuse object and scene features to assemble them in the shared frame. On the 3D-FUTURE evaluation subset, SceneReGen achieves the best scene-level CD, scene-level F-Score, and 3D bounding-box IoU among the evaluated methods, ties the best object-level CD, and ranks second in object-level F-Score. Qualitative outputs in autonomous-driving and embodied-AI scenes further illustrate the potential of asset-centric reconstruction beyond indoor furniture.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
