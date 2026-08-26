# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：39
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 13
  - Embodied / Robotics / AR Applications: 9
  - Neural Scene Representations & Rendering: 9
  - Dynamic / 4D Reconstruction: 7
  - Geometry Foundation Models: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

## 今日科研趋势综合分析报告

> 覆盖时间窗口：2026-08-24 至 25 | 论文总数：17 篇


### 一、今日主要趋势

#### 趋势 1：世界模型从"像素预测"向"几何/语义状态预测"转型

这是今日最显著的趋势信号。两篇独立工作 **GeoWAM**（自动驾驶领域）和 **GaussianWAM**（机器人操作领域）同时挑战了世界动作模型（WAM）在像素空间学习场景动态的既有范式，提出将预测目标从图像转向显式几何表征——GeoWAM 直接预测未来点云，GaussianWAM 则通过 3D 高斯场将几何与语义监督蒸馏进模型表示。两者互不引用、几乎同期发布，指向一个正在形成的领域共识：**像素作为状态空间对几何与运动建模是间接且低效的**，"几何即状态"可能成为下一代世界模型的核心理念。

#### 趋势 2：单目/稀疏输入下的场景生成式重建加速兴起

**SceneReGen** 将单图像三维场景重建重新定义为"完整物体资产的生成与装配"；**NeoWorld-Pro** 则用多模态大语言模型将单目图像转化为可交互场景程序。两者互补地展示了同一趋势的两个侧面：一是**几何驱动的生成式补全**（SceneReGen），利用物体级生成先验弥补观测缺失；二是**基于物理验证的程序化场景编程**（NeoWorld-Pro），把重建问题转化为可执行代码的生成与验证。结合 **FixAnything** 对稀疏视角渲染伪影的通用修复，可以看出领域正在从"重建观测到的"转向"生成观测不到的"。

#### 趋势 3：3D 高斯泼溅成为跨表征、跨媒体、跨任务的"粘合剂"

今日多篇论文以 3DGS 为核心或关联组件，但侧重点各异：**GaussianWAM** 将异构语义/几何信号绑定到共享高斯原语进行蒸馏；**SeeU** 在高斯空间中注入语义进行条件化精化以解决稀疏视角欠约束问题；**AquaFlow** 与 **NemoSplat** 分别将单目流式重建和前馈 4D 重建扩展到水下场景；**LagrangeGS** 将动态 3DGS 建模为非保守拉格朗日系统；**ExMesh++** 则试图将重建结果导出为可编辑的 UV-PBR 网格资产。这一分布表明 3DGS 已从"新视角渲染方法"演变为一个**基础设施层**——不同子领域正在围绕它解决各自的核心痛点（几何一致性、物理一致性、场景可编辑性、媒体退化鲁棒性）。

#### 趋势 4：输入数据层面的"预处理革命"——解决杂乱信号与真实世界数据

**Game2World Engine** 直面游戏视频中 UI 覆盖层对世界模型训练的干扰，通过自动化 UI 提取与合成构建干净的成对训练数据；**Spotter** 通过语义分割与多视立体将街景全景转化为紧凑的地理参考数据库；**SiZeUp** 利用单目深度先验与有序深度损失直接从航拍影像估计建筑高度。这些工作共同指向一个趋势：**重建与生成模型的下限由训练数据质量决定，而数据质量的核心瓶颈正从"采集"转向"范式化清洗与结构化提取"**。

#### 趋势 5：模型效率与轻量化微调成为通用诉求

**FixAnything** 仅通过二进制掩码与轻量微调即复用预训练视频生成模型完成多表示渲染修复；**NemoSplat** 以前馈方式实现无需逐场景优化的 4D 水下重建；**SiZeUp** 通过降维参数化将重建速度提升 23–52 倍；**LagrangeGS** 通过近似速度-海森矩阵为单位矩阵绕开大规模求逆计算瓶颈。这些工作展示了从"每场景逐优化"走向"前馈/轻量适配"的范式迁移，契合边缘设备与实时应用需求。


### 二、技术路线观察

| 技术路线 | 代表性论文 | 核心表征/监督信号 | 关键瓶颈 |
|---------|-----------|------------------|----------|
| **几何基础模型** | GaussianWAM | 深度 + 相机参数 + 稠密语义特征绑定高斯原语 | 如何在训练后移除教师模型不掉点 |
| **世界模型（驾驶/机器人）** | GeoWAM, GaussianWAM, Game2World | 点云（GeoWAM）vs 像素+高斯场蒸馏（GaussianWAM）vs 清洗后游戏视频（Game2World） | 几何监督如何与动作生成协调统一 |
| **前馈 3D/4D 重建** | NemoSplat, AquaFlow, SeeU | 显式高斯/点云 + 物理媒体模型 | 动态场景解耦、媒体退化补偿 |
| **物理感知动态建模** | LagrangeGS | 非保守拉格朗日系统 + 局部刚体正则 | 大规模粒子计算效率 |
| **生成式场景重建** | SceneReGen, NeoWorld-Pro | 物体先验 + 场景坐标装配（SceneReGen）；MLLM 代码生成 + 物理在环验证（NeoWorld-Pro） | 物体生成本位坐标与场景坐标之间的表征差距 |
| **渲染修复/编辑** | FixAnything, ExMesh++, Object-Uni | 视频生成先验 + 二进制掩码锚定；分阶段网格-UV-材质解耦 | 3D 一致性维持、分解歧义 |
| **定位与导航应用** | Spotter | 建筑立面语义分割 + 多视立体 + 级联检索 | GPS 退化环境的实时性要求 |
| **特定领域适配** | Misanthrope, 姿态评估框架 | 隐私感知关键点检测（自蒸馏）；BlazePose 运动学分析 | 任务特定性与泛化能力的权衡 |

**侧重点对比：**
- **视觉表征重心**从"像素/图像空间"向"几何空间（点云、深度、高斯）"迁移，且语义信息（而非仅几何）正成为第三极监督信号。
- **实现范式**从"每场景优化"向"前馈推理 + 轻量微调"转变，但具体路径分化：有的复用视频生成先验（FixAnything），有的用基础模型前馈预测（NemoSplat），有的用 MLLM 代码生成（NeoWorld-Pro）。
- **场景覆盖**从室内/郊外数字建模（Object-Uni、SceneReGen）扩展到水下（AquaFlow、NemoSplat）、城市 GPS 退化（Spotter）、运动健身（姿态评估）等真实应用场景。
- **一致性保障手段**呈现多元化：FixAnything 用相机位姿精度做 DPO 奖励信号，LagrangeGS 用拉格朗日力学约束保证时间可逆性，SeeU 用熵感知跨视角聚合恢复欠约束区域，ExMesh++ 用分阶段优化减轻分解歧义。


### 三、值得优先阅读的论文

#### 1. GaussianWAM（arXiv:2608.24714）⭐ 最优先
**理由**：与 GeoWAM 构成今日最重要的"合流"信号——两篇独立工作同时挑战世界模型像素空间范式。GaussianWAM 的技术路线（异构教师信号 → 3D 高斯场统一组织 → 训练时蒸馏、推理时零开销）具有高度可迁移性，且对机器人操作这一热门方向直接适用。理解它可同时把握世界模型演进与 3DGS 基础设施化两大趋势的交汇点。

#### 2. GeoWAM（arXiv:2608.23486）⭐ 最优先
**理由**：将世界模型预训练目标从"未来图像"切换为"未来点云"，是一个简洁而深刻的问题重构。自动驾驶场景动作执行空间本身就是三维的，这一改动直击像素表征的本质缺陷。开闭环实验对比结果值得细读，它可能预示 WAM 领域的重要转向。

#### 3. SceneReGen（arXiv:2608.23930）⭐ 高
**理由**：选择性位姿分解（朝向编码在生成网格中，平移与尺度从场景证据估计）是一个精巧的设计洞察，直面物体级生成与场景级重建之间的

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-08-26T09:14:29-04:00
**Total number of papers:** 39
**Number of papers added in the latest update:** 7
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

#### 2026-08-24 - NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction

**Authors:** Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu, Hanwen Zhang, Huajian Huang, Sai-Kit Yeung
**Links:** [abs](https://arxiv.org/abs/2608.22888) - [pdf](https://arxiv.org/pdf/2608.22888)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, 4D Gaussian, Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction
- 作者：Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu, Hanwen Zhang, Huajian Huang, Sai-Kit Yeung
- 出版日期：2026-08-24
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.22888

### 一句话总结
NemoSplat 是首个面向水下动态场景的前馈式 4D 高斯泼溅框架，通过媒体感知和时间解耦设计，直接从无标定海洋视频中实现高保真重建与跟踪。

### 研究问题
如何在存在光散射、运动干扰和动态物体的非受控水下环境中，实现稳健、高保真的 4D 动态场景重建。

### 核心思路/方法
- 利用前馈式视觉基础模型提供相机位姿与稠密深度估计。
- 提出 **Promptable Dynamic Disentangler**：融合学习到的动态概率和可选语义文本先验，采用置信度感知策略，隔离大规模瞬态动态实体。
- 设计 **Media-Aware Gaussian Predictor**：联合估计 3D 高斯固有属性与物理媒体参数，在单次前向传播中恢复纯净场景外观。
- 构建含大规模动态元素的水下数据集，用于训练与评估。

### 主要贡献
- 提出 NemoSplat，首个面向媒体感知动态重建的前馈 4D 高斯泼溅框架，可直接处理无标定海洋视频。
- 设计 Promptable Dynamic Disentangler，实现鲁棒的瞬态实体分离。
- 提出 Media-Aware Gaussian Predictor，在重建中显式建模媒体干扰。
- 引入大规模水下动态数据集，并证明 NemoSplat 在跟踪精度与渲染质量上达到当前最优水平。

### 局限性
摘要未提供足够信息。摘要未提及方法对极端浑浊水体、计算开销、实时性、泛化到其他水下环境或数据集的局限性分析。

### 阅读优先级
**高**。理由：该工作将 4D 高斯泼溅扩展到水下非受控场景，提出新的媒体感知预测器与动态解耦机制，并自建大规模数据集，对动态重建和水下视觉领域均有显著推进意义；且摘要明确报告了 SOTA 跟踪与渲染结果，实验支持较充分。

</details>

<details>
<summary>Abstract</summary>

Reconstructing photorealistic scenes in unconstrained underwater environments remains challenging due to severe media-induced light scattering and unpredictable dynamic objects. Recent feed-forward visual foundation models have demonstrated remarkable capabilities in generalized novel view synthesis and tracking. However, when directly applied to aquatic videos, optical attenuation and motion interference fatally corrupt their feature aggregation, leading to severe tracking and reconstruction failures. To overcome these limitations, we present NemoSplat, the first feed-forward 4D Gaussian Splatting framework tailored for media-aware dynamic reconstruction directly from uncalibrated marine videos. Beyond providing robust estimations of camera poses and dense scene depth, we devise a Promptable Dynamic Disentangler that utilizes a confidence-aware fusion strategy of learned dynamic probabilities and optional semantic text priors, effectively isolating massive transient entities. Furthermore, to counteract visual degradation, a Media-Aware Gaussian Predictor is formulated to jointly estimate intrinsic 3D Gaussian attributes alongside physical media parameters, rendering pristine scene appearance in a single forward pass. Additionally, we introduce a large-scale underwater dataset with massive dynamic elements to facilitate training and evaluation. Extensive experiments on our dataset demonstrate that NemoSplat achieves state-of-the-art tracking accuracy and high-fidelity rendering. Homepage: https://nemosplat.hkustvgd.com

</details>

#### 2026-08-24 - LagrangeGS: Non-Conservative Lagrangian System on Dynamic 3D Gaussian Splatting

**Authors:** Shogo Sato, Takuhiro Kaneko, Shoichiro Takeda, Tomoyasu Shimada, Riku Inoue, Kazuhiko Murasaki, Ryuichi Tanida
**Links:** [abs](https://arxiv.org/abs/2608.22773) - [pdf](https://arxiv.org/pdf/2608.22773)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LagrangeGS: Non-Conservative Lagrangian System on Dynamic 3D Gaussian Splatting
- 作者：Shogo Sato, Takuhiro Kaneko, Shoichiro Takeda, Tomoyasu Shimada, Riku Inoue, Kazuhiko Murasaki, Ryuichi Tanida
- 出版日期：2026-08-24T03:51:21Z
- 分类：Dynamic / 4D Reconstruction（主）；Neural Scene Representations & Rendering（次）
- 链接：https://arxiv.org/abs/2608.22773

### 一句话总结
作者提出 LagrangeGS，将动态 3D 高斯溅射建模为非保守拉格朗日系统，从而在无需重新训练的情况下实现稳定的长期外推、一致的时间反转和反事实物理编辑。

### 研究问题
现有物理感知的动态 3DGS 扩展方法虽然可以显式预测速度场以改善外推，但仅将向量场拟合到视觉形变上，未满足拉格朗日力学约束，导致三大问题：(i) 物理不一致的轨迹；(ii) 缺乏时间可逆性；(iii) 长期外推时出现几何坍塌。

### 核心思路/方法
- 将动态 3DGS 建模为非保守拉格朗日系统，从原理上解决物理不一致轨迹问题。
- 针对直接应用通用 LNN 需对数百万高斯粒子进行大尺度速度-海森矩阵求逆的计算瓶颈，将速度-海森矩阵近似为单位矩阵，使粒子动力学解耦，从而降低计算复杂度。
- 为恢复时间可逆性，将非保守力显式限制为与时间无关，使后向积分保持一致。
- 为应对长期外推中的几何坍塌，引入局部刚体对齐来正则化粒子轨迹。

### 主要贡献
- 提出 LagrangeGS，首次将动态 3DGS 表述为非保守拉格朗日系统。
- 通过近似速度-海森矩阵为单位矩阵，解决大规模粒子计算瓶颈。
- 通过限制非保守力的时间无关性，实现一致的时间反向积分。
- 引入局部刚体对齐正则化，解决长期外推几何坍塌问题。
- 在动态场景基准上验证了无需重训练的稳定长期外推、一致时间反转和基于物理的反事实编辑能力。

### 局限性
摘要未提供足够信息（摘要仅描述方法有效性与能力，未提及具体限制或失败场景，如对复杂场景的鲁棒性、计算开销具体量化、近似为单位矩阵带来的精度损失等）。

### 阅读优先级
**高**。理由：该工作直接针对动态 3DGS 中物理一致性、时间可逆性和长期稳定性三个核心痛点，提出了统一的拉格朗日力学框架，并给出可扩展的工程近似方案，对 4D 重建和物理编辑方向具有较强方法论参考价值；且来自工业界研究团队，实验覆盖基准较广，实用性倾向明显。

</details>

<details>
<summary>Abstract</summary>

Dynamic 3D Gaussian Splatting (3DGS) achieves photorealistic reconstruction of time-varying scenes, and recent physics-aware extensions improve extrapolation by explicitly predicting velocity fields. However, these extensions merely fit vector fields to visual deformations without satisfying Lagrangian mechanics, leading to three major issues: (i) physically inconsistent trajectories, (ii) lack of time-reversibility, and (iii) geometric collapse during long-term extrapolation. In this paper, we propose LagrangeGS, which formulates dynamic 3DGS as a non-conservative Lagrangian system. While this Lagrangian formulation fundamentally solves (i), a direct application of general LNNs to dynamic 3DGS requires a large velocity-Hessian inversion for millions of Gaussian particles. To overcome this computational bottleneck, we approximate the velocity-Hessian as an identity matrix, decoupling particle dynamics for computational tractability. For (ii), we restrict the non-conservative forces to be explicitly time independent, enabling consistent backward integration. Finally, to address (iii), we introduce local rigid alignment that regularizes particle trajectories. Extensive evaluations on dynamic scene benchmarks demonstrate that LagrangeGS enables stable long-term extrapolation, consistent time reversal, and counterfactual physics-based editing without retraining.

</details>

#### 2026-08-23 - M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression

**Authors:** Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang
**Links:** [abs](https://arxiv.org/abs/2608.22465) - [pdf](https://arxiv.org/pdf/2608.22465)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, 4D Gaussian, Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：M³ISR：用于3D/4D高斯泼溅与前馈压缩的多模态多视角基准
- 作者：Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang
- 出版日期：2026-08-23
- 分类：Dynamic / 4D Reconstruction（主要）；Neural Scene Representations & Rendering（次要）
- 链接：https://arxiv.org/abs/2608.22465

### 一句话总结
本文提出了一个受控合成的多模态多视角基准M³ISR，用于系统评估3D/4D高斯泼溅的重建、压缩和流式传输性能。

### 研究问题
现有动态多视角视频基准虽提供真实拍摄内容，但难以分离相机几何、表示效率和时域冗余等因素对高斯泼溅方法的影响，缺乏一个能对3DGS/4DGS重建、压缩与流式传输进行受控评估的基准。

### 核心思路/方法
构建包含25个场景（来自5个室内外场景组）、两种相机/运动配置、6路同步1080p视角的合成基准，提供RGB、相机参数、深度、语义/实例分割和静态-动态掩码等密集真值标注。采用共享中心相机设计以隔离视角变化因素，并设计五个互补赛道：3DGS合成、4DGS合成、4DGS流式传输、3DGS压缩、4DGS压缩。同时定义3DGS/4DGS前馈压缩任务，提供参考率-失真公式和初步基线评估。

### 主要贡献
1. 提出M³ISR——一个专门为3D/4D高斯泼溅设计的受控合成基准，包含丰富的多模态标注。
2. 设计共享中心相机配置，可隔离视角变化并实现新视角合成和表示效率的受控评估。
3. 组织五个互补评估赛道，覆盖重建、流式传输和压缩三大任务方向。
4. 定义3DGS/4DGS前馈压缩任务，并提供参考率-失真公式和基线评估。

### 局限性
摘要未提供足够信息。摘要仅提及初步基线评估显示流式方法在训练/重建成本上显著高于离线动态重建基线，以及静态重建质量差异小但存储差异大，但未明确说明基准自身的覆盖范围限制（如合成场景与真实场景的域差距、场景规模上限等）。

### 阅读优先级
**中**。理由：该工作提供了一个结构化的受控基准，对从事3D/4DGS压缩和流式传输研究的读者有较高参考价值；但作为基准论文，不涉及新算法突破，对非该细分领域的读者参考价值有限。摘要显示了基准设计和初步基线结果，但缺乏更深入的方法论细节。

</details>

<details>
<summary>Abstract</summary>

High-fidelity free-viewpoint video (FVV) and interactive rendering increasingly rely on explicit Gaussian representations, yet practical deployment remains constrained by representation size, dynamic updates, and computational cost. Existing multi-view video benchmarks provide valuable real-captured content, but they make it difficult to isolate the effects of controlled camera geometry, representation efficiency, and temporal redundancy. We introduce M$^3$ISR, a controlled synthetic benchmark for 3D and 4D Gaussian Splatting (3DGS/4DGS). The benchmark contains 25 scenes from five indoor and outdoor scene groups, two camera/motion configurations, six synchronized 1080p views, and dense ground-truth annotations including RGB, camera parameters, depth, semantic and instance segmentation, and static--dynamic masks. The shared-center camera design intentionally isolates angular view variation and enables controlled evaluation of novel-view synthesis and representation efficiency. We organize M$^3$ISR into five complementary tracks covering 3DGS synthesis, 4DGS synthesis, 4DGS streaming, 3DGS compression, and 4DGS compression. Representative baseline results show small differences in static reconstruction quality but substantial differences in representation storage, while the evaluated streaming methods exhibit substantially higher reported training or reconstruction cost than the corresponding offline dynamic reconstruction baselines. We further define feedforward compression tasks for 3DGS and 4DGS and provide reference rate--distortion formulations and preliminary baseline evaluations. The benchmark is intended as a controlled and complementary testbed for systematic study of Gaussian-based FVV reconstruction, compression, and streaming.

</details>

#### 2026-08-22 - Learning Implicit Constitutive Laws for Dynamic 3D Gaussian Splatting from Monocular Videos

**Authors:** Xiaoyang Liu, Kai Han
**Links:** [abs](https://arxiv.org/abs/2608.22102) - [pdf](https://arxiv.org/pdf/2608.22102)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Implicit Constitutive Laws for Dynamic 3D Gaussian Splatting from Monocular Videos
- 作者：Xiaoyang Liu, Kai Han
- 出版日期：2026-08-22T20:47:17Z
- 分类：Dynamic / 4D Reconstruction（次要分类：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.22102

### 一句话总结
本文提出GCA框架，通过隐式本构规律学习与多模态对齐模块，从单目视频中驱动3D高斯表示的可变形物体动态重建，显著优于现有方法。

### 研究问题
如何从单目动态视频中学习可变形物体的隐式物理本构规律，以避免现有隐式方法在噪声监督下的局部最优问题和显式方法依赖预定义本构方程、在单目设定下不稳定的问题。

### 核心思路/方法
- 整体框架：GCA（Gaussian Constitutive Alignment），以静态多视角扫描作为几何初始化，仅从单一固定视角的动态视频学习内在物理动态。
- 关键模块一：Rank-based Depth-Geometric Anchors（RDGA）——通过尺度不变的基于秩的深度对齐，从单目动态观测建立鲁棒的几何约束，减少对不可靠像素级颜色监督的依赖。
- 关键模块二：Constitutive Prior Regularizer（CPR）——将经典本构模型作为可微软先验集成，在保持隐式建模灵活性的同时正则化优化过程，即使真实材料不在假设集合中也能工作。
- 统一机制：基于LoRA的适应性调整将两个模块统一在框架内。

### 主要贡献
- 提出GCA框架，实现从单目视频学习隐式本构规律并驱动3D高斯动态重建。
- 设计RDGA模块，通过秩基深度几何锚定克服单目监督中的颜色噪声问题。
- 设计CPR模块，将经典本构模型作为可微先验，提升物理可解释性与优化稳定性。
- 实验验证：在合成、真实到仿真及真实世界数据集上优于现有方法，在合成基准上比最强基线Chamfer Distance降低48%。

### 局限性
摘要未提供足够信息。摘要中未明确讨论方法的失败案例、计算开销、对初始化质量的具体依赖程度、真实世界数据上的详细误差范围或对其他场景（如多物体交互、极端形变）的适用性限制。

### 阅读优先级
**高**。理由：该工作针对动态3D高斯重建中单目监督这一关键痛点，提出新颖的隐式本构学习框架，并报告了显著的定量提升（Chamfer Distance降低48%），同时涵盖合成、真实到仿真和真实世界多类评估，对从事动态重建、物理仿真与神经渲染交叉方向的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We present GCA (Gaussian Constitutive Alignment), a framework for learning implicit constitutive laws from monocular dynamic video of deformable objects represented by 3D Gaussians. Given a static multi-view scan for geometric initialization, our method learns intrinsic physical dynamics solely from a single fixed-viewpoint video of the moving object. Existing implicit methods often suffer from local minima under noisy supervision and lack physical interpretability, while explicit approaches rely on predefined constitutive equations, limiting generalizability and becoming unstable in monocular settings. To address these challenges, our framework unifies LoRA-based adaptation with two key alignment modules. First, we propose Rank-based Depth-Geometric Anchors (RDGA) to establish robust geometric constraints from monocular dynamic observations via scale-invariant rank-based depth alignment, reducing the reliance on unreliable pixel-level color supervision. Second, a Constitutive Prior Regularizer (CPR) integrates classical constitutive models as soft differentiable priors, regularizing the optimization while preserving the flexibility of implicit modeling---even when the actual material is absent from the hypotheses. Extensive experiments on synthetic, real-to-sim, and real-world datasets demonstrate that GCA outperforms existing methods, achieving 48% lower Chamfer Distance than the strongest baseline on synthetic benchmarks while remaining robust under monocular supervision.

</details>

#### 2026-08-20 - Gallileo-4D: Frozen Backbone Ensemble for Dynamic 4D Reconstruction

**Authors:** Nicolò Savioli
**Links:** [abs](https://arxiv.org/abs/2608.19743) - [pdf](https://arxiv.org/pdf/2608.19743)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, dynamic 4D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gallileo-4D: Frozen Backbone Ensemble for Dynamic 4D Reconstruction
- 作者：Nicolò Savioli
- 出版日期：2026-08-20
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2608.19743

### 一句话总结
本文提出了一种零训练成本的冻结骨干网络集成方法，在PhysAI动态4D重建挑战赛中取得第三名，通过推理时融合三种解码配置，比冻结基线提升+0.041 APD。

### 研究问题
如何在预训练4D骨干网络微调效果不佳的情况下，通过不更新梯度（零训练）的方式提升动态4D重建性能。研究发现基准测试中仅25%的评估数据与训练数据分布一致，导致微调反而损害预训练特征在剩余75%数据上的表现。

### 核心思路/方法
- 冻结预训练4D骨干网络，不进行任何梯度更新
- 在推理阶段融合三种解码配置：时间步长-3、水平翻转测试时增强、密集步长-1
- 使用凸权重对三种解码结果进行加权融合
- 该集成方法在冻结基线上获得+0.041 APD提升，超过了所有13种微调配置的效果

### 主要贡献
- 提出一种零训练成本的推理时集成策略，在动态4D重建挑战赛中获得第三名（27个队伍中，最终APD为0.58356）
- 揭示了一个反直觉现象：在训练数据分布与评估数据分布不一致的基准下，微调反而会损害模型在大部分评估数据上的性能
- 证明了冻结骨干+推理时集成的有效性，且训练成本为零

### 局限性
摘要未提供足够信息：未提及方法在非该基准场景下的泛化能力、计算资源消耗、推理时间等具体细节；也未说明参与挑战赛的其他候选方法细节。

### 阅读优先级
**中**。理由：该方法思路简洁且实用，揭示了分布不匹配下微调失效的重要现象，对4D重建和迁移学习领域有一定启发意义。但摘要未提供方法细节和消融实验，适用性有限，适合对推理时集成或该挑战赛感兴趣的读者快速浏览。

</details>

<details>
<summary>Abstract</summary>

We describe our entry to the PhysAI Dynamic 4D Reconstruction Challenge, which placed third of 27 teams at 0.58356 APD on the final leaderboard, without a single gradient update. This was not the plan: of thirteen fine-tuning configurations of a pre-trained 4D backbone, twelve degraded the challenge score, and eleven of those twelve improved local validation at the same time. We trace this inversion to the structure of the benchmark: only 25% of the evaluation set belongs to the data variant released for training, so updates that fit the available data damage the pre-trained features the remaining 75% relies on. Our system therefore freezes the backbone and spends its budget at inference time, fusing three decoding configurations -- temporal stride-3, horizontal-flip test-time augmentation, and dense stride-1 -- under a convex weighting. The ensemble recovers +0.041 APD over the frozen baseline, more than any training run achieved, at zero training cost.

</details>

#### 2026-08-20 - S$^2$GS: Structured Sparse Gaussian Streaming for Efficient Free-Viewpoint Video Reconstruction on Edge-IoT Devices

**Authors:** Yiwei Li, Jiannong Cao, Weixun Gao, Rui Cao, Songye Zhu, Yinfeng Cao, Mingjin Zhang
**Links:** [abs](https://arxiv.org/abs/2608.19639) - [pdf](https://arxiv.org/pdf/2608.19639)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** video reconstruction, rendering, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：S$^2$GS: Structured Sparse Gaussian Streaming for Efficient Free-Viewpoint Video Reconstruction on Edge-IoT Devices
- 作者：Yiwei Li, Jiannong Cao, Weixun Gao, Rui Cao, Songye Zhu, Yinfeng Cao, Mingjin Zhang
- 出版日期：2026-08-20T05:12:53Z
- 分类：Dynamic / 4D Reconstruction（动态/4D重建）
- 链接：https://arxiv.org/abs/2608.19639

### 一句话总结
本文提出S$^2$GS框架，通过结构感知的时空稀疏性选择性更新高斯残差，在边缘物联网设备上实现高效且低存储的自由视角视频流式重建。

### 研究问题
现有自由视角视频（FVV）流式重建方法在资源受限的边缘物联网设备上面临每帧优化时间长、存储占用大的问题，难以部署。

### 核心思路/方法
- **空间域**：采用流式八叉树（streaming octree）层级组织高斯残差，捕获空间相关性以指导残差更新。
- **时间域**：设计结构化门控机制，包含层级特征传播（HFP）和Gumbel-Sigmoid采样，将层级动态线索转化为可微优化下的稀疏残差更新决策。
- **多级离散方案**：提供对残差更新的细粒度控制，同时保留复杂动态细节。
- 整体框架在消费者GPU、工业边缘IoT设备和物理远程呈现测试平台上验证。

### 主要贡献
- 提出S$^2$GS框架，利用结构感知的时间稀疏性实现高效FVV流式重建，兼顾视觉保真度。
- 设计空间八叉树与时间门控机制相结合的残差更新策略。
- 在RTX 4090上相比QUEEN，每帧优化时间降低59%、存储成本降低85%。
- 在Jetson AGX Orin上实现60+ FPS的最高渲染吞吐量和最低能耗，展示资源受限系统的部署潜力。

### 局限性
摘要未提供足够信息，无法说明该方法的潜在局限性（如特定场景退化、极端动态下的表现、八叉树内存开销等）。

### 阅读优先级
**高**。理由：该工作针对边缘IoT设备上的FVV流式重建这一实际问题，提出了兼顾效率与质量的新颖稀疏化框架，且提供了跨多种硬件平台的量化对比结果（如59%时间降低、85%存储降低、60+ FPS），对动态重建与边缘计算交叉领域的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Streaming reconstruction of Free-Viewpoint Videos (FVVs) supports immersive Internet of Things (IoT) services, such as telepresence and digital twin visualization. Existing methods suffer from high per-frame optimization time and large storage footprints, limiting deployment on resource-constrained Edge-IoT devices. To address these challenges, we propose Structured Sparse Gaussian Streaming (S$^2$GS), an FVV reconstruction framework that exploits structure-aware temporal sparsity to selectively update Gaussian residuals, enabling efficient streaming without compromising visual fidelity. In the spatial domain, a streaming octree hierarchically organizes Gaussian residuals, capturing spatial correlations that guide residual updates. In the temporal domain, a structured gating mechanism, comprising hierarchical feature propagation (HFP) and Gumbel-Sigmoid sampling, converts hierarchical dynamic cues into sparse residual update decisions under differentiable optimization. A multi-level discrete scheme is further adopted to provide fine-grained control over residual updates while preserving intricate dynamic details. Extensive experiments across consumer GPUs, industrial edge IoT devices, and a physical telepresence testbed demonstrate that S$^2$GS consistently reduces per-frame optimization time and storage footprint while maintaining competitive visual quality. Compared with QUEEN, S$^2$GS reduces per-frame optimization time by 59% and storage costs by 85% on an RTX 4090 GPU. On the Jetson AGX Orin, S$^2$GS delivers the highest rendering throughput (60+ FPS) and the lowest energy consumption among the evaluated methods, demonstrating its potential for deployment in resource-constrained systems.

</details>

#### 2026-08-20 - Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models

**Authors:** Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh
**Links:** [abs](https://arxiv.org/abs/2608.19556) - [pdf](https://arxiv.org/pdf/2608.19556)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, scene flow, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models
- 作者：Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh
- 出版日期：2026-08-20
- 分类：Dynamic / 4D Reconstruction（次要分类：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.19556

### 一句话总结
Stream4D 提出用前馈式 4D 重建奖励替代静态 3D 重建批评器，为流式自回归扩散视频模型提供显式场景动态建模，从而改善长时程视频生成中的几何漂移与运动退化问题。

### 研究问题
流式自回归扩散视频模型在长时程生成中，因训练目标仅优化局部帧预测，导致世界几何与动态不一致，出现累积几何漂移和运动趋于静态或非自然的问题。已有双向方法依赖 3D 高斯泼溅重建的奖励信号，但单一刚性 3D 重建无法建模动态场景，会误将真实物体运动视为重建误差，且该批评器在自回归设置下可能被“冻结视频”这一捷径所利用。

### 核心思路/方法
- 用前馈式 4D 重建奖励替换静态 3D 重建批评器，显式建模场景动态，使连贯运动获得高一致性奖励。
- 增加一个运动先验项，奖励自然的场景流幅度，同时惩罚抖动和非刚性伪影，以引导运动幅度与质量。
- 将上述两项与一个轻量级感知锚点（perceptual anchor）组合成最终训练配方。

### 主要贡献
- 提出 Stream4D 方法，将静态 3D 批评器替换为前馈式 4D 重建奖励，解决静态重建对动态场景的误导。
- 引入运动先验，显式奖励自然场景流幅度并抑制抖动与非刚性伪影。
- 在多种自回归视频骨干网络和不同生成时长下，Stream4D 提升了 4D 重建质量、更有效地保持运动，并获得更高的人类对齐偏好。

### 局限性
摘要未提供足够信息，未明确提及具体的失败案例、计算开销、训练稳定性或对特定场景类型的限制。

### 阅读优先级
**高**。理由：该工作针对流式自回归视频生成中的核心动态一致性问题提出新训练奖励方案，结合 4D 重建与运动先验，方法新颖且适用于多种骨干网络，实验宣称在多项指标上取得改进，对视频生成与 4D 重建交叉领域有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Streaming autoregressive diffusion models enable real-time, long-horizon video generation, but their training objectives optimize local frame prediction rather than the geometry and dynamics of a coherent world: long rollouts accumulate geometric drift and degrade into static or unnatural motion. Recent bidirectional approaches address this problem using rewards signals built upon 3D Gaussian-Splatting reconstruction. However, a single rigid 3d reconstruction cannot model a dynamic scene, so this critic penalizes genuine object motion as reconstruction error and is maximized by freezing the video. This shortcut is especially detrimental in the AR setting, where each chunk can propagate an already-static configuration. In this work, we propose Stream4D, which replaces the static critic with a feed-forward 4D reconstruction reward that explicitly models scene dynamics, allowing coherent motion to receive high consistency rewards. To further guide motion magnitude and quality, we add a motion prior that rewards natural scene-flow magnitude while penalizing jitter and non-rigid artifacts. Our final recipe combines these two terms with a lightweight perceptual anchor. Across various autoregressive video backbones and various generation horizons, Stream4D improves 4D reconstruction quality, preserves motion more effectively, and achieves higher human-aligned preference. Project page: https://banyuanhao.github.io/Stream4D/

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-08

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

#### 2026-08-24 - Spotter: Efficient Urban Visual Localization via Geo-Referenced Facade Landmarks in GPS-Degraded Environments

**Authors:** Antoni Valls, Jordi Sanchez-Riera
**Links:** [abs](https://arxiv.org/abs/2608.23290) - [pdf](https://arxiv.org/pdf/2608.23290)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** multi-view stereo, stereo depth, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spotter: Efficient Urban Visual Localization via Geo-Referenced Facade Landmarks in GPS-Degraded Environments
- 作者：Antoni Valls, Jordi Sanchez-Riera
- 出版日期：2026-08-24
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2608.23290

### 一句话总结
Spotter 是一种利用建筑立面作为地理参考的实时视觉定位框架，在 GPS 信号不佳的城市环境中通过离线构建紧凑度量数据库和在线级联检索+几何验证实现精确全局定位，并在巴塞罗那的穿戴设备数据集上验证了其超越里程计基线、接近 SOTA 地图匹配方法且帧率更高的性能。

### 研究问题
在稠密城市环境中，GPS 信号因多径传播常出现退化，导致传统视觉里程计随运行时间产生漂移，而地图匹配方法既依赖可靠的 GPS 先验又计算量过大，难以在边缘设备上实时运行。因此，如何在不依赖 GPS 的前提下实现鲁棒、实时的全局视觉定位是本文要解决的核心问题。

### 核心思路/方法
- **离线阶段**：处理 Google Street View 全景图，通过语义分割提取建筑立面，并将多视图立体深度与制图数据配对，构建一个紧凑的度量数据库，为立面提供全局地理参考。
- **在线阶段**：查询图像通过级联检索（cascaded retrieval）与几何验证流水线进行匹配，恢复精细的全局相机位姿。
- **融合能力**：系统保留在 GPS 信号可用时融合 GPS 的能力。

### 主要贡献
1. 提出 Spotter —— 一种以建筑立面作为全局地理参考的视觉定位框架，可在 GPS 退化环境中实现实时定位。
2. 设计离线建库流程，将街景全景、语义分割、多视图深度与制图数据整合为紧凑度量数据库。
3. 提出级联检索+几何验证的在线匹配流水线，实现高效且精细的全局定位。
4. 构建了一个在巴塞罗那多个街区、使用穿戴式智能眼镜采集的行人序列新数据集，并在此基准上展示了超越里程计基线、定位精度接近 SOTA 地图方法且帧率显著更高的结果。

### 局限性
摘要未提供足够信息。具体未提及方法在非立面区域、光照/遮挡变化、极端天气、大规模数据库扩展性、对街景更新频率的依赖性以及失败模式等局限性；亦未提供与其他方法在精度/速度上的具体数值差距。

### 阅读优先级
**中**。理由：该工作面向城市视觉定位的实际应用痛点（GPS 退化、实时性），方法组合（语义分割+街景+级联检索）有一定工程价值，并提供了新数据集。但主要创新点在于系统集成与工程化，而非全新的理论方法；若读者关注边缘实时视觉定位或穿戴设备定位应用，可优先阅读，若更关注理论突破则优先级可降低。

</details>

<details>
<summary>Abstract</summary>

Accurate visual localization on robotic and wearable platforms remains challenging in dense urban environments. Existing methodologies typically rely on GPS for absolute positioning, yet GPS signals frequently degrade in urban canyons due to multipath propagation. Consequently, standard solutions like visual odometry suffer from unmitigated drift over time, while map-matching techniques struggle to acquire the reliable GPS priors they need, on top of being too computationally heavy for real-time edge execution. To address these limitations, we propose Spotter, a robuts and real-time visual localization framework that uses building facades as a reliable source of global geo-reference, while retaining the capability to integrate GPS signals when available. In an offline stage, Spotter processes Google Street View panoramas by semantically segmenting facades and pairing multi-view stereo depth with cartographic data to build a compact metric database. At runtime, query images are matched via a cascaded retrieval and geometric verification pipeline to recover fine-grained global camera localization. We benchmark Spotter on a newly collected dataset of pedestrian sequences acquired with wearable smart glasses across several districts of Barcelona. Experimental results show that Spotter outperforms odometry-based baselines and achieves localization accuracy comparable to state-of-the-art map-based methods while operating at significantly higher frame rates.

</details>

#### 2026-08-24 - Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation

**Authors:** YiHsuan Tsai
**Links:** [abs](https://arxiv.org/abs/2608.23206) - [pdf](https://arxiv.org/pdf/2608.23206)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, multi-view reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation
- 作者：YiHsuan Tsai
- 出版日期：2026-08-24
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.23206

### 一句话总结
本文提出将球面占用率分布（ray-wise occupancy profiles）作为多视图3D重建与生成任务的统一中间表示，并通过判别式解码器与生成式扩散管道验证其有效性与不确定性表达能力。

### 研究问题
如何设计一种紧凑、可学习且具有不确定性感知能力的中间表示，以统一支持从图像进行多视图3D重建（判别式）与3D生成（生成式）任务。

### 核心思路/方法
- 从多视图3D高斯重建中蒸馏出球面占用率分布 P(r) = T(r) o(r)，作为逐射线占用概率剖面。
- 判别式路径：训练一个逐射线解码器，将全局视角平均特征与射线特定图像证据通过FiLM条件注入到剖面预测头中。
- 生成式路径：构建基于剖面VAE与潜空间扩散模型的生成管道，支持无条件采样与图像条件下的多解重建，并通过classifier-free guidance调节解的多样性。
- 分析了预测剖面的形态学特性，包括后处理功率锐化与学习锐化目标，揭示L1逐射线损失族中的单调宽度-峰值权衡关系，并据此重新定义形态学门控。
- 在DTU真实场景上进行验证，确认管道可迁移至非合成输入。

### 主要贡献
- 提出球面占用率剖面作为多视图重建与生成的统一中间表示。
- 判别式解码器在独立测试集上达到归一化中位深度误差0.035（基于Google Scanned Objects 999对象子集训练）。
- 生成式管道支持无条件采样与图像条件多解重建，且解的离散程度可量化、可通过引导强度调节。
- 揭示预测剖面形态（宽度-峰值）的单调权衡前沿，并提出改进的形态学门控定义。
- 在DTU真实照片上验证了跨域迁移能力。

### 局限性
摘要未提供足够信息：未提及训练/测试数据的具体划分细节、计算资源需求、失败案例、对极端视角或遮挡的鲁棒性分析，以及与其他现有方法在标准基准上的定量对比结果。

### 阅读优先级
**中**。理由：该工作提出了一个新颖的统一表示框架，兼具判别与生成能力，并包含形态学分析，对多视图重建与生成交叉领域有参考价值；但摘要中缺乏与SOTA方法的直接对比和更广泛的数据集验证，实际影响力需结合全文评估。若你重点关注统一表示或不确定性建模，可提高优先级。

</details>

<details>
<summary>Abstract</summary>

We study spherical occupancy profiles-the ray-wise occupancy probability profiles P(r) = T(r) o(r) distilled from multi-view 3D Gaussian reconstructions-as a unified intermediate representation for both discriminative and generative 3D reconstruction from images. On a 999-object subset of Google Scanned Objects with 48 turntable views each, we train (i) a discriminative per-ray decoder that injects global view-averaged and ray-specific image evidence into a FiLM-conditioned profile head, reaching median soft depth error 0.035 (normalized) on an independent 90-object test split, and (ii) a generative pipeline built on a profile VAE and a latent diffusion model, which supports unconditional sampling that matches the reconstruction manifold and image-conditioned multi-solution reconstruction whose per-object solution spread is quantifiable and tunable via classifier-free guidance. We further analyze the morphology of predicted profiles: post-hoc power sharpening and a learned sharpening target both recover ground-truth profile width without degrading depth, exposing a monotonic width-peak frontier in the L1-per-ray loss family and motivating a principled redefinition of morphology gates. Real-photo validation on two DTU scenes confirms the pipeline transfers to non-synthetic input. Our results suggest that ray-wise occupancy profiles offer a compact, learned, and uncertainty-aware interface between multi-view reconstruction and generative priors.

</details>

#### 2026-08-24 - Misanthrope: A Privacy-Preserving Keypoint Detector

**Authors:** Francesco Vultaggio, Predrag Djindjic, Markus Gerke, Sebastian Tschiatschek, Phillipp Fanta-Jende
**Links:** [abs](https://arxiv.org/abs/2608.23012) - [pdf](https://arxiv.org/pdf/2608.23012)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** image matching, structure from motion, SfM, simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Misanthrope: A Privacy-Preserving Keypoint Detector  
- 作者：Francesco Vultaggio, Predrag Djindjic, Markus Gerke, Sebastian Tschiatschek, Phillipp Fanta-Jende  
- 出版日期：2026-08-24  
- 分类：3D 重建与多视图几何  
- 链接：https://arxiv.org/abs/2608.23012  

### 一句话总结
该工作提出一种通过自蒸馏训练的隐私保护关键点检测器 Misanthrope，其核心思想是从源头避免检测人物身上的关键点，从而在图像匹配任务中缓解基于特征的反演攻击，同时保持甚至提升匹配性能。

### 研究问题
如何在图像匹配流水线中保护场景中的隐私敏感内容（尤其是人物），而不牺牲匹配精度？现有方法多采用事后混淆（post-hoc obfuscation），该工作试图在特征检测源头规避隐私泄露。

### 核心思路/方法
- 设计一种新颖的关键点检测器 Misanthrope，通过自蒸馏（self-distillation）训练，使模型学习不检测人物身体上的关键点。
- 此举旨在从源头减少可被反演攻击利用的特征，从而替代传统的事后隐私保护手段。
- 验证思路：先展示传统特征检测管道的反演图像可被用于检测和重新识别场景中的人物，再证明 Misanthrope 能缓解此类攻击。

### 主要贡献
- 提出 Misanthrope，一种隐私保护的关键点检测器，从源头规避人物敏感内容。
- 通过反演攻击实验，证明传统检测器存在人物识别风险，而 Misanthrope 能有效缓解。
- 在匹配性能上与现有最优方法持平，并在含人物干扰的场景（如摄影旅游、野外里程计）中超越现有方法。
- 在 Image Matching Challenge 2021 Phototourism 测试集上，Misanthrope 在 9 个场景中有 7 个达到最佳稀疏特征提取性能。
- 开源模型与评估脚本。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作为隐私保护与视觉几何任务的交叉方向，提出了一种无需事后处理的源头式隐私防护策略，并在标准基准上达到领先性能，对 SLAM、视觉定位等领域具有直接借鉴价值；同时代码开源，便于复现和扩展。

</details>

<details>
<summary>Abstract</summary>

Image matching is a core component of applications such as Simultaneous Localization and Mapping (SLAM), Visual Localization, and Structure from Motion (SfM). However, the local image features central to this task are vulnerable to inversion attacks, which enable adversaries to reconstruct privacy-sensitive scene content from local features. These attacks pose a particular threat in distributed computing scenarios where the pre-computed features leave edge devices to be processed by remote servers. In this work, we introduce Misanthrope, a novel privacy-preserving keypoint detector trained through self-distillation to avoid detecting keypoints on people---a predominant source of privacy-sensitive content in most localization scenarios---thus mitigating inversion attacks at the source rather than through post-hoc obfuscation. We demonstrate how inverted images from traditional feature detection pipelines can be used to detect and re-identify people in the scene, while Misanthrope is able to mitigate these attacks. Furthermore, Misanthrope maintains image matching performance on par with the state of the art and even surpasses it in challenging settings where people act as distractors, such as phototourism and in-the-wild odometry. On the Image Matching Challenge 2021 Phototourism test set, Misanthrope is the top-performing sparse feature extractor in 7 out of 9 scenes. We make our model and its evaluation script available here: https://github.com/fratopa/misanthrope

</details>

#### 2026-08-24 - AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction

**Authors:** Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu
**Links:** [abs](https://arxiv.org/abs/2608.22906) - [pdf](https://arxiv.org/pdf/2608.22906)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** pointmap, scene reconstruction, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, scene representation, rendering, splatting, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction
- 作者：Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu
- 出版日期：2026-08-24
- 分类：3D Reconstruction & Multi-view Geometry；次级分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.22906

### 一句话总结
AquaFlow 提出面向水下场景的单目高斯溅射流式重建框架，通过鲁棒位姿估计与物理启发式场景表示，显著提升水下跟踪与渲染质量。

### 研究问题
如何将单目 3DGS 流式重建方法推广至水下场景，克服由光衰减和散射引起的视觉退化，以实现高保真的水下逐步重建。

### 核心思路/方法
- 在大规模水下数据上微调 3D 视觉基础模型，以获取鲁棒的位姿和点图估计。
- 提出介质引导的增量式高斯初始化策略，服务于流式建图。
- 设计流式兼容的混合场景表示：将结构化的、距离条件化的神经高斯与物理启发式光学模型相结合，补偿水下成像效应，实现准确重建。

### 主要贡献
- 提出 AquaFlow，首个针对水下场景的单目高斯溅射流式重建框架。
- 引入介质引导的高斯初始化与流式兼容的混合神经场景表示，应对水下视觉退化。
- 在包含 62 条多样化水下轨迹（覆盖公开基准与网络野生视频）的综合数据集上，达到最先进的跟踪与渲染性能：平均定位误差降低 13.2%，PSNR 较 WaterSplat-SLAM 提升 4.74 dB。

### 局限性
摘要未提供足够信息（如计算开销、对极端水质/光照条件的鲁棒性边界、泛化到特定水下环境的能力等均未提及）。

### 阅读优先级
**高**。理由：该工作针对水下场景这一具有明确应用价值但视觉退化严重的领域，在 3DGS 流式重建这一热门方向上提出完整解决方案，且提供了大规模评测与显著性能提升，对从事水下视觉、SLAM 或神经渲染的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent monocular 3D Gaussian Splatting (3DGS) streaming reconstruction methods have achieved impressive performance by balancing reconstruction quality and efficiency. However, extending these frameworks to underwater scenes remains challenging due to severe visual degradation, such as light attenuation and scattering, which degrades camera pose tracking and distorts scene geometry. To address these challenges, we propose AquaFlow, a monocular Gaussian Splatting streaming reconstruction framework for efficient and high-fidelity underwater reconstruction. Specifically, AquaFlow fine-tunes a 3D vision foundation model on large-scale underwater data for robust pose and pointmap estimation, and introduces a medium-guided incremental Gaussian initialization strategy for streaming mapping. Furthermore, we develop a streaming-compatible hybrid scene representation that integrates structured, distance-conditioned neural Gaussians with a physics-inspired optical model to compensate for underwater image formation effects, enabling accurate scene reconstruction. We evaluate AquaFlow on a comprehensive dataset of 62 diverse underwater trajectories, collected from both public benchmarks and in-the-wild web videos across various scales. Extensive experiments demonstrate that AquaFlow achieves state-of-the-art tracking and rendering performance, reducing average localization error by 13.2% and improving PSNR by 4.74 dB compared to WaterSplat-SLAM.

</details>

#### 2026-08-24 - SiZeUp: Fast 3D Proxy from Aerial Images via Depth Ordinal Loss

**Authors:** Wenjun Zhou, Yunshan Li, Qiaoyu Zhu, Weidan Xiong, Hao Zhang, Daniel Cohen-Or, Hui Huang
**Links:** [abs](https://arxiv.org/abs/2608.22821) - [pdf](https://arxiv.org/pdf/2608.22821)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, monocular depth, point cloud reconstruction, feature matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SiZeUp: Fast 3D Proxy from Aerial Images via Depth Ordinal Loss
- 作者：Wenjun Zhou, Yunshan Li, Qiaoyu Zhu, Weidan Xiong, Hao Zhang, Daniel Cohen-Or, Hui Huang
- 出版日期：2026-08-24T05:37:34Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.22821

### 一句话总结
SiZeUp 提出一种从倾斜航空影像快速构建大规模 3D 城市代理模型的方法，通过高度-足迹表示和有序深度一致性损失实现高效稳健的高度估计，相比现有流程提速 23–52 倍。

### 研究问题
如何从校准的倾斜航拍影像中快速且可扩展地构建大规模 3D 城市代理模型，同时避免依赖显式特征匹配或稠密点云重建。

### 核心思路/方法
- 采用“高度-足迹”表示，将建筑抽象问题降维为低维优化（足迹挤出单一高度参数）。
- 引入有序深度一致性损失：通过可微渲染器将参数化建筑代理映射为多视角深度图像，强制代理渲染结果与单目深度模型预测的相对深度排序一致。
- 损失基于相对深度而非度量深度，规避单目尺度模糊问题，提供跨视角更可靠的监督信号。
- 结合高效的动态视角选择策略，进一步提升速度。

### 主要贡献
- 提出一种快速、可扩展的 3D 城市代理构建方法，无需稠密点云或显式特征匹配。
- 设计基于有序深度的一致性损失，在相对深度空间监督优化，增强跨视角稳定性。
- 相比最先进的代理重建管线，实现 23–52 倍速度提升，同时保持代理级覆盖率和体积一致性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。该方法在大规模城市 3D 建模的效率和鲁棒性上具有明显优势，且引入了新颖的有序深度损失，适合对重建效率或城市规模建模感兴趣的读者；但对于不关注代理建模或无需处理尺度不确定性的读者，相关性相对有限。

</details>

<details>
<summary>Abstract</summary>

We present SiZeUp, a fast and scalable approach for constructing large-scale 3D urban proxy models directly from calibrated oblique aerial imagery. Our method adopts a height-from-footprint representation, reducing 3D building abstraction to a low-dimensional optimization problem in which building footprints are extruded by a single height parameter. To enable efficient and robust height estimation, we introduce an ordinal depth consistency loss that enforces agreement between the relative depth ordering of rendered proxies and depth priors predicted by a monocular depth model. This is realized through a differentiable renderer that maps parametric building proxies into multi-view depth images, allowing gradients to be propagated from depth supervision to building heights. Our ordinal formulation produces stable optimization in practice and avoids explicit feature matching or dense point cloud reconstruction. Rather than relying on metric depth, which can be unreliable under monocular scale ambiguity, our ordinal depth consistency loss operates on relative depths, providing a more reliable signal across views. Combined with an efficient dynamic view selection, our approach achieves a 23-52$\times$ speedup over state-of-the-art proxy reconstruction pipelines while maintaining comparable proxy-level coverage and volume consistency, making it well suited for large-scale urban modeling tasks.

</details>

#### 2026-08-23 - DECO: Depth-Guided Co-Visibility Reasoning for Low-Altitude UAV Visual Localization

**Authors:** Yibin Ye, Xichao Teng, Shuo Chen, Xiaokai Song, Dongdong Guan, Qifeng Yu, Zhang Li
**Links:** [abs](https://arxiv.org/abs/2608.22289) - [pdf](https://arxiv.org/pdf/2608.22289)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, monocular depth, feature matching, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DECO: Depth-Guided Co-Visibility Reasoning for Low-Altitude UAV Visual Localization
- 作者：Yibin Ye, Xichao Teng, Shuo Chen, Xiaokai Song, Dongdong Guan, Qifeng Yu, Zhang Li
- 出版日期：2026-08-23
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.22289

### 一句话总结
DECO 提出了一种利用单目深度先验来推理无人机图像与正射参考图之间共同可见区域的方法，从而提升低空无人机在 GNSS 拒止环境下的视觉定位精度。

### 研究问题
低空无人机视觉定位中，正射参考图主要记录俯视表面（如屋顶、地面），而垂直结构（如立面、墙体）被压缩或缺失，导致低空图像中大量显著关键点在参考图中没有有效对应，产生冗余匹配和位姿估计不准确。

### 核心思路/方法
- 使用单目深度先验推断局部表面几何，估计无人机图像与参考图之间的共同可见区域。
- 提出“几何-显著性耦合共同可见性评分”（Geometry-Saliency Coupled Co-visibility Score），联合考虑几何共同可见性与检测器显著性，对关键点进行排序。
- 保留既视觉显著又几何共同可见的关键点，用于改进特征匹配和 PnP 位姿求解。

### 主要贡献
- 提出 DECO，一个深度引导的共同可见性推理框架，用于低空无人机视觉定位。
- 引入几何-显著性耦合的共同可见性评分，改善关键点选择。
- 实验表明 DECO 在不同深度模型、特征检测器和匹配器下均能提升定位性能。
- 代码将开源（https://github.com/UAV-AVL/DECO）。

### 局限性
摘要未提供足够信息，包括未提及具体实验数据集、与哪些基线方法比较、不同深度模型/检测器/匹配器组合下的具体性能差距、计算开销或实时性分析等。

### 阅读优先级
**高**

理由：该工作针对低空无人机视觉定位中的实际痛点（正射参考图缺失垂直结构导致匹配退化），提出了新颖的深度引导共同可见性推理方法，具有明确的工程应用价值，且模块化设计可适配多种现有深度模型和匹配器，对相关方向研究者有较强参考意义。

### 阅读优先级
**高**

理由：该方法面向GNSS拒止环境下无人机视觉定位这一实用场景，创新性地引入深度先验解决正射图与低空视角间的几何域差异问题，且框架与不同组件（深度模型、检测器、匹配器）兼容，具备较强通用性和实用潜力，适合该方向研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Unmanned aerial vehicles (UAVs) increasingly require robust visual localization in GNSS-denied environments. A common solution estimates UAV poses by matching keypoints between UAV images and geo-tagged orthographic reference maps derived from satellite or aerial imagery, followed by Perspective-\(n\)-Point (PnP) pose solving. However, such reference maps mainly record top-down surfaces such as roofs and ground planes, while vertical structures such as facades and walls are often compressed or missing. Consequently, many visually distinctive keypoints in low-altitude UAV images have no valid counterparts in the reference map, leading to redundant matches and inaccurate pose estimation. To address this issue, we propose DECO, a DEpth-guided CO-visibility reasoning framework for low-altitude UAV visual localization. DECO uses monocular depth priors to infer local surface geometry and estimate co-visible regions between UAV images and the reference map. Based on this prior, a Geometry-Saliency Coupled Co-visibility Score is introduced to jointly consider geometric co-visibility and detector saliency for keypoint ranking. In this way, DECO retains keypoints that are both visually distinctive and geometrically co-visible, improving feature matching and PnP-based pose estimation. Extensive experiments demonstrate that DECO achieves superior localization performance and can be integrated with different depth models, feature detectors, and matchers. The source code will be available at https://github.com/UAV-AVL/DECO.

</details>

#### 2026-08-22 - Robust Global Structure-from-Motion via View Graph Pruning

**Authors:** Jiamin Xu, Lixing Yao, Weichen Dai, Renshu Gu, Zunjie Zhu, Weiwei Xu, Gang Xu
**Links:** [abs](https://arxiv.org/abs/2608.22054) - [pdf](https://arxiv.org/pdf/2608.22054)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, SfM, neural rendering, novel view synthesis, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robust Global Structure-from-Motion via View Graph Pruning
- 作者：Jiamin Xu, Lixing Yao, Weichen Dai, Renshu Gu, Zunjie Zhu, Weiwei Xu, Gang Xu
- 出版日期：2026-08-22T17:40:47Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.22054

### 一句话总结
本文提出一种基于子图引导的视图图剪枝框架，通过先在各子图内执行全局SfM获得可靠位姿，再剔除跨子图的不一致边，从而提升全局运动恢复结构方法在视觉模糊等挑战性条件下的鲁棒性。

### 研究问题
全局SfM方法性能高度敏感于视图图中由视觉模糊匹配导致的错误边，这些错误边会引发相机位姿注册错误和重建伪影。因此，研究问题是如何在全局SfM框架下识别并移除视图图中的不可靠连接。

### 核心思路/方法
核心思路是利用可靠子图的内部一致性来识别并移除不可靠连接。具体方法分为三步：
1. 将视图图划分为局部一致的子图，并在每个子图内执行全局SfM以获得可靠相机位姿；
2. 跨子图应用基于RANSAC的边剪枝，剔除不一致的边；
3. 在精化后的视图图上执行全局SfM。

### 主要贡献
- 提出一种子图引导的视图图剪枝框架，用于提升全局SfM的鲁棒性；
- 在模糊、序列化、无序图像数据集上验证了方法在挑战条件下对全局SfM鲁棒性的改进；
- 通过神经渲染进一步评估，表明改进后的相机估计能够提升新视角合成的质量。

### 局限性
摘要未提供足够信息：未详细说明方法在极端模糊或大规模数据上的具体性能边界，也未讨论计算开销、失败案例或方法的适用范围限制。

### 阅读优先级
**高**。理由：该工作针对全局SfM的已知脆弱性问题（视觉模糊导致的错误匹配）提出了一种结构化的剪枝框架，且实验结果覆盖了多种挑战性数据，并额外通过神经渲染验证了下游应用收益，对三维重建与多视角几何方向的研究和实践均有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Structure-from-Motion (SfM) aims to estimate camera poses and reconstruct 3D structures from a collection of unordered images. Compared with incremental SfM, global SfM achieves better scalability by jointly estimating camera poses based on a view graph constructed from pairwise correspondences. However, its performance is highly sensitive to erroneous edges caused by visually ambiguous matches, which may lead to incorrect camera registration and reconstruction artifacts. In this work, we propose a subgraph-guided view graph pruning framework for robust global SfM. Our key idea is to exploit the internal consistency of reliable subgraphs to identify and remove unreliable connections. Specifically, we first partition the view graph into locally consistent subgraphs and perform global SfM within each subgraph to obtain reliable camera poses. We then apply RANSAC-based edge pruning across subgraphs to remove inconsistent edges, and finally perform global SfM on the refined view graph. Extensive experiments on ambiguous, sequential, and unordered image datasets demonstrate that our method improves the robustness of global SfM under challenging conditions. Further evaluation with neural rendering shows that the improved camera estimation leads to higher-quality novel view synthesis results.

</details>

#### 2026-08-22 - ORBIT++: Benchmarking SfM in the Wild with 360° Video

**Authors:** Sara Sabour, Linyi Jin, Richard Tucker, Amir Hertz, Marcus Brubaker, Saurabh Saxena, Junhwa Hur, Andrea Tagliasacchi, Deqing Sun, David J. Fleet, Richard Szeliski, Noah Snavely
**Links:** [abs](https://arxiv.org/abs/2608.22039) - [pdf](https://arxiv.org/pdf/2608.22039)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, SfM, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ORBIT++: Benchmarking SfM in the Wild with 360° Video
- 作者：Sara Sabour, Linyi Jin, Richard Tucker, Amir Hertz, Marcus Brubaker, Saurabh Saxena, Junhwa Hur, Andrea Tagliasacchi, Deqing Sun, David J. Fleet, Richard Szeliski, Noah Snavely
- 出版日期：2026-08-22
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.22039

### 一句话总结
本文提出了一个基于360°全景视频构建的、用于评估相机位姿估计的新基准ORBIT，该基准包含复杂真实场景且具备可靠的轨迹真值。

### 研究问题
现有SfM（运动恢复结构）方法在复杂视频（如挑战性相机运动、动态场景）中经常失效，而领域内缺乏针对这些困难场景的可靠真值基准，难以衡量实际进展并定位待改进环节。

### 核心思路/方法
关键洞察是利用在线全景360°视频作为数据源：全景视频提供更丰富的视觉上下文以跟踪相机运动，即使部分视图受模糊、运动或动态物体影响。具体流程为：先在全景视频中跟踪完整相机运动，再裁剪并重投影所选部分，生成透视视角片段，最终构成名为ORBIT的基准。

### 主要贡献
- 提出了ORBIT：一个用于评估相机位姿估计的新基准，基于360°视频构建，包含困难真实场景且具备可靠轨迹真值。
- 实验表明COLMAP以及近期基于优化的和前馈式SfM方法在本基准上难以准确估计相机位姿。
- 为研究者提供一个有价值的测试平台，用于在真实挑战性SfM问题上衡量实质进展。

### 局限性
摘要未提供足够信息：未说明基准的规模（如片段数量）、评估指标的具体细节、与其他基准的定量对比，以及构建过程中的潜在偏差或失败模式。

### 阅读优先级
**高**  
理由：该工作针对SfM领域缺乏困难场景真值基准的关键空白，提出创新性数据来源（360°视频），并直接验证了现有主流及前沿方法在该基准上的不足，对评估和改进相机位姿估计方法具有直接参考价值，适合3D视觉研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Structure-from-Motion (SfM) is a cornerstone of 3D perception, yet current methods often fail when applied to complex videos involving challenging camera motions or dynamic scenes. Compounding the problem, the field lacks reliable ground-truth benchmarks for such difficult scenarios, making it hard to gauge real-world progress or to pinpoint where improvements are most needed. To address this gap, we introduce a new benchmark for evaluating camera pose estimation. Our key insight is to leverage online panoramic 360° video as a source of data from which to construct challenging clips, while still enabling robust ground-truth trajectory recovery. The panoramic nature of these videos provides richer visual context for tracking camera motion, even when parts of the view are affected by blur, motion, or dynamic objects. After tracking camera motion across full 360° videos, we crop and reproject selected portions to generate perspective-view clips that serve as our benchmark, called ORBIT. Experiments show that COLMAP, as well as recent optimization-based and feed-forward SfM methods struggle to accurately estimate camera poses on our benchmark. Hence, ORBIT provides a valuable testbed where researchers can meaningfully measure progress on truly challenging, real-world SfM problems.

</details>

#### 2026-08-20 - HandMvNet: Real-Time 3D Hand Pose Estimation Using Multi-View Cross-Attention Fusion

**Authors:** Muhammad Asad Ali, Nadia Robertini, Didier Stricker
**Links:** [abs](https://arxiv.org/abs/2608.20093) - [pdf](https://arxiv.org/pdf/2608.20093)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HandMvNet: Real-Time 3D Hand Pose Estimation Using Multi-View Cross-Attention Fusion
- 作者：Muhammad Asad Ali, Nadia Robertini, Didier Stricker
- 出版日期：2026-08-20T14:24:35Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.20093

### 一句话总结
HandMvNet 是一种基于多视图交叉注意力融合的实时 3D 手部姿态与形状估计方法，在无需相机参数输入的情况下，实现了比单目方法更准确、比现有多视图方法更快的推理。

### 研究问题
如何从多视图相机图像中实时、准确地估计 3D 手部姿态和形状，同时克服单目方法中的尺度-深度模糊问题，并减少对相机参数的依赖。

### 核心思路/方法
采用多视图注意力融合机制，从多个视角图像中有效整合特征，以学习一致的绝对手部姿态和形状。与先前需要输入相机参数的多视图方法不同，该方法无需相机参数即可学习 3D 几何，从而简化输入并降低推理开销，实现实时性能。

### 主要贡献
- 提出 HandMvNet，据摘要所述为最早的多视图实时 3D 手部姿态与形状估计方法之一。
- 通过多视图注意力融合机制，获得比单目方法更一致的绝对手部姿态和形状。
- 消除了多视图方法对相机参数输入的需求。
- 相比现有方法，显著降低推理时间并保持竞争力的结果。
- 在公开数据集上的定性和定量评估中，在相同设置下优于先前方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法针对多视图 3D 手部姿态估计的实时性问题提出了新方案，兼具无需相机参数和低推理延迟的特点，对相关领域的研究者和工程应用具有较高参考价值。不过由于摘要未披露网络结构细节和实验基准的具体内容，阅读时应结合论文正文验证其声称的性能。

</details>

<details>
<summary>Abstract</summary>

In this work, we present HandMvNet, one of the first real-time method designed to estimate 3D hand motion and shape from multi-view camera images. Unlike previous monocular approaches, which suffer from scale-depth ambiguities, our method ensures consistent and accurate absolute hand poses and shapes. This is achieved through a multi-view attention-fusion mechanism that effectively integrates features from multiple viewpoints. In contrast to previous multi-view methods, our approach eliminates the need for camera parameters as input to learn 3D geometry. HandMvNet also achieves a substantial reduction in inference time while delivering competitive results compared to the state-of-the-art methods, making it suitable for real-time applications. Evaluated on publicly available datasets, HandMvNet qualitatively and quantitatively outperforms previous methods under identical settings. Code is available at github.com/pyxploiter/handmvnet.

</details>

#### 2026-08-20 - Gravity-aware partially calibrated absolute pose estimation from affine- or rotation-covariant features

**Authors:** Marcus Valtonen Örnhag, Alberto Jaenal, Stefan Adalbjörnsson
**Links:** [abs](https://arxiv.org/abs/2608.20056) - [pdf](https://arxiv.org/pdf/2608.20056)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gravity-aware partially calibrated absolute pose estimation from affine- or rotation-covariant features
- 作者：Marcus Valtonen Örnhag, Alberto Jaenal, Stefan Adalbjörnsson
- 出版日期：2026-08-20
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.20056

### 一句话总结
本文利用IMU提供的重力向量与特征描述符蕴含的局部几何信息，提出两种新的高效求解器，用于联合估计绝对位姿与焦距的部分标定绝对位姿估计问题。

### 研究问题
如何利用IMU重力先验和特征诱导的局部几何信息，以更少的对应点数量和更低计算成本，实现对绝对位姿与焦距的联合估计，从而在部分标定场景下提升定位精度与效率。

### 核心思路/方法
- 从IMU数据获取重力向量，并结合特征描述符（如SIFT）中嵌入的局部几何信息，
- 推导出新的约束条件，用于联合估计绝对位姿和焦距。
- 基于这些约束构建两个求解器：
  - UP1PfAC：仅需单个仿射对应（affine correspondence）即可求解；
  - UP2PfORI：需要两个旋转协变特征（rotation-covariant features）。
- 与传统需要四个点对应的半标定绝对位姿方法相比，本文方法所需样本更少、计算成本更低，便于集成到现代RANSAC类鲁棒估计框架中。

### 主要贡献
- 首次将特征诱导的局部几何信息应用于部分标定绝对位姿估计，填补了该方向的研究空白；
- 推导了结合重力向量与特征局部几何的新约束，并据此设计两个高效求解器（UP1PfAC和UP2PfORI）；
- 在公开大规模数据集上验证了方法在定位精度和速度上的有效性，相较于现有最优方法表现出色，同时能准确估计焦距。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作针对部分标定绝对位姿估计提出了更高效的求解器（最少仅需1个仿射对应或2个旋转协变特征），显著减少了传统方法所需的对应点数量，并利用IMU的普及性，方法适用性广。摘要明确表明在两个大规模公开数据集上进行了验证且效果优于现有方法，且结果涉及实际应用常用的RANSAC框架，对视觉定位、SLAM、XR等领域具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Inertial measurement units (IMUs) are now standard in most consumer devices, such as smartphones, drones, and extended reality (XR) headsets. By fusing visual and inertial data, localization systems gain significantly in speed and robustness compared to vision-only or IMU-only approaches. However, traditional pose estimation methods fail to utilize the local geometric information embedded in feature descriptors like SIFT. Recent work has proved the advantages of leveraging this information for relative and absolute pose estimation, but its application to partially calibrated absolute pose estimation remains unexplored. In this paper, we derive novel constraints for joint estimation of absolute pose and focal length, making use of a gravity vector obtained from IMU data and the feature-induced local geometry, which we use to construct two efficient solvers: UP1PfAC, that operates given a single affine correspondence and UP2PfORI, which requires two orientation-covariant features. Unlike traditional, semi-calibrated absolute pose methods requiring four point correspondences, our solvers benefit from fewer samples and lower computational cost, simplifying robust estimation in modern RANSAC-like frameworks. We evaluate the proposed solvers against the state-of-the-art on large-scale public datasets and demonstrate that our method achieves fast and accurate localization and focal length estimation.

</details>

#### 2026-08-20 - Point-Based 3D Reconstruction from Sparse Views under Known Illumination

**Authors:** Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad, Markus Worchel, J. Andreas Bærentzen, Thomas B. Moeslund
**Links:** [abs](https://arxiv.org/abs/2608.20000) - [pdf](https://arxiv.org/pdf/2608.20000)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Point-Based 3D Reconstruction from Sparse Views under Known Illumination（已知光照下基于点的稀疏视角三维重建）
- 作者：Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad, Markus Worchel, J. Andreas Bærentzen, Thomas B. Moeslund
- 出版日期：2026-08-20T13:15:27Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：https://arxiv.org/abs/2608.20000

### 一句话总结
本文提出一种基于不透光beta surfel的可微点渲染方法，在已知光照条件下利用物理光传输约束实现稀疏视角下的紧凑三维重建，以平均仅267个surfel即可超越现有基于点的基线方法。

### 研究问题
如何在已知光照的稀疏视角条件下，以更少的图元数量实现高精度的基于点的三维表面重建？现有方法（如神经隐式表面或密集点云/高斯溅射）通常需要大量图元，本文试图探索一种更紧凑的表示方案。

### 核心思路/方法
- 采用基于**不透明beta surfel**的可微点渲染框架，以椭圆/圆盘状图元表示表面。
- 设计了一种**显式伴随光传输（adjoint light transport）**公式，用于计算surfel几何和外观参数的梯度。
- 通过将**基于物理的光传输**纳入优化过程，使重建受到光照物理约束的引导，从而在直接光照受控场景中提升表面恢复精度。

### 主要贡献
- 提出了一种仅依赖少量图元（平均267个surfel）即可完成高质量重建的点基方法。
- 在5个合成物体、10个视角的重建实验中，取得了所有评估基线中**最低的平均对称Chamfer距离**。
- 相较于最强点基基线，**平均Chamfer距离相对降低28.5%**，且所用图元数减少约161个（约为基线数量的极小比例）。
- 定向Chamfer指标显示，该方法在**精度**上表现更优，在**完整性**上与相关点基方法竞争力相当。

### 局限性
摘要未提供足够信息。具体包括：未提及方法在真实场景或非受控光照下的表现、对光照估计误差的鲁棒性、计算开销、训练时间，以及与其他非点基方法（如神经隐式表面）的详细对比数据。此外，实验仅涉及合成物体，未见真实数据验证。

### 阅读优先级
**高**。理由：本文在稀疏视角重建领域提出了一个在效率和精度上均有显著改进的紧凑点基解决方案，实验结果显示图元数量大幅减少且误差显著降低，对关注点云/表面重建、可微渲染和光传输建模的研究者具有直接参考价值。其方法思路（物理约束+紧凑表示）也可能对相关下游任务有启发意义。

</details>

<details>
<summary>Abstract</summary>

Sparse view 3D reconstruction is commonly addressed with neural implicit surfaces or dense point-based representations such as Gaussian splatting. Surface-aware splatting methods improve extracted geometry through oriented primitives and regularization, while RadiosityGS incorporates differentiable light transport through a radiosity inspired finite-element surfel formulation. We propose a differentiable point rendering method based on opacity-bearing beta surfels. An opacity explicit adjoint light transport formulation provides gradients for surfel geometry and appearance parameters, allowing physically based light transport to constrain reconstruction. Across five synthetic objects reconstructed from ten posed views, our method achieves the lowest mean symmetric Chamfer distance among the evaluated baselines and reduces mean Chamfer distance by 28.5% relative to the strongest point-based baseline while using only 267 surfels on average, approximately ~161 fewer primitives. Directional Chamfer results further show improved accuracy and competitive completion relative to related point-based methods. These results show that, in the controlled direct illumination setting, compact beta surfels combined with transport-based optimization can recover surfaces without relying on the tens to hundreds of thousands of primitives used by the evaluated baselines.

</details>

## Neural Scene Representations & Rendering

### 2026-08

#### 2026-08-24 - FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors

**Authors:** Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan
**Links:** [abs](https://arxiv.org/abs/2608.23549) - [pdf](https://arxiv.org/pdf/2608.23549)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** structure from motion, NeRF, Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors
- 作者：Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan
- 出版日期：2026-08-24
- 分类：Neural Scene Representations & Rendering（神经场景表示与渲染）
- 链接：https://arxiv.org/abs/2608.23549

### 一句话总结
FixAnything是一个统一的渲染修复模型，通过最小化改动和轻量微调复用预训练视频生成模型，以视频到视频转换的方式修复多种3D表示（如3DGS、NeRF、网格、点云）中的渲染伪影，并利用相机位姿精度作为奖励信号进行直接偏好优化（DPO）以保持3D一致性。

### 研究问题
如何在输入视图稀疏或目标视图偏离输入时，用一种通用方法修复来自不同3D场景表示（如Gaussian Splatting、NeRF、网格、点云）的渲染伪影，同时保证输出具有3D一致性并支持下游重建？现有方法针对单一表示定制，需要自定义架构或大量重训练。

### 核心思路/方法
1. **视频生成模型复用**：将预训练视频生成模型改造为视频到视频转换模型（video-to-video translation），利用其隐式多视图先验。关键洞察是即使带噪声的渲染序列也保留了相机运动和粗略场景结构，因此可将清理视为视频翻译任务。
2. **二进制掩码控制**：引入表示“干净像素”的二进制掩码，使模型锚定高质量输入（如训练视图）并仅精炼其余区域，从而控制保留哪些场景结构。
3. **直接偏好优化（DPO）**：使用从运动恢复结构（SfM）获得的相机位姿精度作为奖励信号，对模型进行直接偏好优化，鼓励生成支持下游重建的3D一致渲染结果。
4. **统一框架**：单个通用模型（FixAnything）可通过轻量微调适配多种3D表示，无需针对每种表示设计专用架构，且未来更强的视频模型可直接替换无需架构重设计。

### 主要贡献
- 提出FixAnything，第一个单一模型即可修复多种3D表示渲染伪影的通用框架（实验覆盖四种不同3D表示）。
- 揭示噪声渲染序列保留相机运动与粗略结构的关键洞察，将渲染精炼重新定义为视频到视频翻译问题。
- 引入二进制掩码机制控制保留区域，以及基于相机位姿精度的DPO奖励信号来保证3D一致性。
- 证明一个通用视频先验可以替代多个专用精炼管线，且框架简单，便于未来直接采用更强视频模型。

### 局限性
摘要未提供足够信息，例如：未说明在何种最差情况下（如极端稀疏视图或完全无干净像素）性能如何；未讨论计算资源、微调数据规模要求；未提及模型对视频生成模型先验失败的鲁棒性；未提供定量对比指标或具体伪影类型的失败案例。

### 阅读优先级
**中**。理由：该方法具有较高的通用性和实用性（跨4种表示、轻量微调、易于扩展），但摘要未给出具体定量结果或与现有方法的详细对比细节，属于概念验证型工作；对于从事渲染修复、3D表示学习或视频先验应用的读者有参考价值，但对于Tier-1顶会论文而言，其现实效果和局限性有待原论文进一步验证。

</details>

<details>
<summary>Abstract</summary>

Rendering views using 3D scene representations such as Gaussian Splatting (3DGS), Neural Radiance Fields (NeRF), meshes, or even point clouds produces artifacts when input views are sparse or target views lie far from the input. Recent work mitigates these artifacts using diffusion-based generative priors, but is specialized to individual representations and require custom architectures or extensive retraining. We present FixAnything, a single model for fixing a wide range of rendering artifacts. It does so by repurposing a pretrained video generative model, leveraging its implicit multi-view priors with only minimal modification and lightweight finetuning. Our key insight is that even noisily-rendered sequences preserve camera motion and coarse scene structure, allowing cleanup to be formulated as video-to-video translation. To control what scene structure should be preserved, we introduce a binary mask denoting the clean pixels, enabling the model to anchor its output to high-quality inputs (e.g. training views) while refining the rest. To encourage FixAnything to produce 3D-consistent renderings that support downstream reconstruction, we use camera pose accuracy (recovered via structure-from-motion) as a reward signal for direct preference optimization (DPO). Across four distinct 3D representations, FixAnything consistently improves rendering quality with lightweight finetuning, demonstrating that a single generalist video prior can replace multiple specialist refinement pipelines. The simplicity of the framework enables immediate adoption of stronger future video models without architectural redesign.

</details>

#### 2026-08-24 - Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers

**Authors:** Federico Stella, Fei Jiang, Zhongshi Jiang, Zohar Barzelay, Emanuel Garbin, Amin Jourabloo, Liuhao Ge
**Links:** [abs](https://arxiv.org/abs/2608.23410) - [pdf](https://arxiv.org/pdf/2608.23410)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers
- 作者：Federico Stella, Fei Jiang, Zhongshi Jiang, Zohar Barzelay, Emanuel Garbin, Amin Jourabloo, Liuhao Ge
- 出版日期：2026-08-24
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.23410

### 一句话总结
本文提出一种基于“下一尺度”自回归范式的人脸新视角合成方法，在单次前向传播中生成多视角、高分辨率且跨视角一致的人脸照片级真实图像。

### 研究问题
如何在多人脸、多目标摄像机场景下，实现高空间分辨率、保身份与细节且几何一致的照片级新视角合成。

### 核心思路/方法
- 基于下一尺度（next-scale）自回归范式，将其扩展用于以人为中心的新视角合成，支持更高分辨率、多视角输出及更强的跨视角一致性。
- 在多样化身份与外观的合成人脸数据集上训练。
- 与扩散模型不同，无需2D预训练；利用下一尺度架构，可从较低分辨率的通用预训练中获益，仅在最后训练阶段使用全尺寸任务特定图像。
- 该方法可用更少的任务特定训练数据收敛，从而能够使用更小但更真实的训练集。
- 可同时合成多个新视角以提高视角间一致性，并可与现有的基于Transformer的像素对齐3D高斯提升模型耦合，生成准确且逼真的人脸3D模型。

### 主要贡献
- 将下一尺度自回归范式适配于人类中心的多视角、高分辨率新视图合成。
- 证明该范式无需2D预训练，且能利用低分辨率通用预训练，减少任务特定数据需求。
- 实证显示在人类主体上，下一尺度自回归在感知保真度和跨视角一致性上取得收益，可作为多输出人类视图合成的可扩展骨干。
- 可与3D高斯提升模型耦合，实现人脸照片级3D重建。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作在视角合成这一活跃领域提出了一种有潜力的替代扩散模型的范式，并展示了多视角一致性与数据效率方面的优势；但摘要未提供定量对比基准、运行资源要求或明确的失败案例，对需要严格评估方法性能的读者，需阅读全文后再决定价值。

</details>

<details>
<summary>Abstract</summary>

Photorealistic novel view synthesis of people remains challenging at high spatial resolutions and across multiple target cameras, where preserving identity, fine appearance details, and geometric coherence is critical. We build on the next-scale autoregressive paradigm and adapt it for human-centric view synthesis by enabling higher image resolutions, multi-view outputs and stronger cross-view consistency in a single forward pass. We train on a synthetic dataset of human faces spanning diverse identities and apparel. Contrary to diffusion models, this paradigm does not need 2D pre-training and, thanks to its next-scale architecture, it benefits from lower-resolution, general-purpose pre-trainings, with the full-sized purpose-specific images being used only in the last training stages. This enables our architecture to converge with a smaller amount of purpose-specific training data, allowing us to use a smaller but more realistic training dataset. The resulting model produces sharp and realistic views, with the option to synthesize multiple novel viewpoints simultaneously for improved agreement across views. Empirically, we observe gains in perceptual fidelity and cross-view coherence on human subjects, demonstrating that next-scale autoregression is an effective backbone for scalable, multi-output human view synthesis. We also couple our pipeline with an existing transformer-based model for pixel-aligned 3D gaussian lifting from multi-view facial inputs, resulting in accurate and photorealistic 3D models of human faces.

</details>

#### 2026-08-24 - Neighbor-Aware View Synthesis for Restoring Missing Views in Light-Field Camera Arrays

**Authors:** Sakshi Goel, Ayush Goyal, K S Venkatesh, Koteswar Rao Jerripothula
**Links:** [abs](https://arxiv.org/abs/2608.23175) - [pdf](https://arxiv.org/pdf/2608.23175)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** depth estimation, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Neighbor-Aware View Synthesis for Restoring Missing Views in Light-Field Camera Arrays
- 作者：Sakshi Goel, Ayush Goyal, K S Venkatesh, Koteswar Rao Jerripothula
- 出版日期：2026-08-24T12:23:27Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.23175

### 一句话总结
本文提出一种基于条件生成对抗网络（cGAN）的生成式框架，利用相邻相机的子孔径图像和位置编码映射来恢复光场相机阵列中缺失的视图。

### 研究问题
光场相机阵列中因硬件故障导致部分相机失效，从而产生缺失的子孔径图像并降低重建质量。本文研究如何从精心选择的相邻相机信息中合成缺失视图，且保证几何一致性。

### 核心思路/方法
该框架首先从相邻相机中筛选出一组对目标视图恢复最有用的子集图像，然后将这些图像与一个位置编码映射（同时指示已选相机位置和期望目标视图位置）一起输入条件生成对抗网络（cGAN），由生成器合成缺失视角。网络通过对抗训练学习生成在几何上一致且光度上准确的视图重建。

### 主要贡献
- 提出一种新颖的生成式框架，专门用于光场相机阵列中缺陷/缺失视图的恢复。
- 利用邻居感知的相机子集选择策略与位置编码结合，提升视图合成的几何一致性。
- 在合成和真实光场数据集上验证了方法在定量和定性上均优于视图插值基线方法，提供容错的光场采集解决方案。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法在极端缺失数、实时性要求、计算开销或处理遮挡/复杂场景等方面的局限。

### 阅读优先级
**中**。理由：该工作针对光场相机硬件故障的视图恢复问题，方法设计有明确应用价值，并且提供了与基线比较的实验结果。但摘要中未给出关键实验数值细节，且该主题属于较专门的应用方向，若你并非从事光场成像或视图合成相关研究，优先级可适当降低。

</details>

<details>
<summary>Abstract</summary>

In light-field (LF) imaging systems, dense spatial sampling from a camera array enables powerful post-capture capabilities such as refocusing and depth estimation. However, real-world LF capture is often affected by hardware malfunctions, where one or more cameras in the array fail, leading to missing sub-aperture images and degraded reconstruction quality. This paper addresses the problem of defective or missing view restoration in light-field camera arrays. We propose a novel generative framework that synthesizes the absent views by exploiting information from a carefully selected subset of neighboring cameras. These selected images, along with a positional encoding map indicating both their locations and the desired target view, are fed into a conditional Generative Adversarial Network (cGAN) trained to generate the missing viewpoint in a geometrically consistent manner. Extensive experiments on synthetic and real-world LF datasets demonstrate that our method produces visually plausible and photometrically accurate reconstructions, outperforming baselines for view interpolation both quantitatively and qualitatively. The proposed framework thus offers a robust and efficient solution for fault-tolerant light-field image acquisition.

</details>

#### 2026-08-24 - Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation

**Authors:** Mining Tan, Yinuo Wang, Ziqi Zhou, Weize Quan, Sifei Li, Jingdong Chen, DanDan Zheng, Libin Wang, Weiming Dong
**Links:** [abs](https://arxiv.org/abs/2608.22757) - [pdf](https://arxiv.org/pdf/2608.22757)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation
- 作者：Mining Tan, Yinuo Wang, Ziqi Zhou, Weize Quan, Sifei Li, Jingdong Chen, DanDan Zheng, Libin Wang, Weiming Dong
- 出版日期：2026-08-24
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.22757

### 一句话总结
本文提出Object-Uni，一个统一模型，将物体姿态作为显式几何变量，同时实现物体级空间感知（姿态感知、空间推理）与可控生成（姿态条件生成、新视角合成）。

### 研究问题
现有统一理解-生成模型虽然能用自然语言描述物体，但无法精确表征连续物体姿态，也难以在目标视角下生成几何一致的图像。因此，本文旨在解决物体实例空间状态的理解与操控问题。

### 核心思路/方法
- 将物体级空间智能统一为一个问题，涵盖姿态感知、空间推理、姿态条件生成和物体级新视角合成。
- 将物体姿态视为理解与生成共享的显式几何变量，而非仅作预测标签或控制信号。
- 提出基于视角的方向抽象方法，将方向映射为结构化视角描述，同时保留连续几何监督。
- 构建物体级空间基准数据集UniSpatial-80K。
- 训练统一模型时采用物体标记锚定的姿态锚点（object-token-grounded pose anchor），将每个实例与其姿态状态关联。

### 主要贡献
- 提出Object-Uni统一模型，首次在统一框架中同时处理物体级空间理解与可控生成。
- 提出视角基的方向抽象方法，使姿态可被多模态大语言模型使用，同时保持连续几何监督。
- 构建UniSpatial-80K物体级空间基准。
- 实验表明模型显著提升物体级姿态理解与姿态可控生成能力，推动统一模型从“描述物体”走向“操控空间状态”。

### 局限性
摘要未提供足够信息（未提及失败案例、数据规模细节、计算资源、泛化边界或对比基线等具体局限）。

### 阅读优先级
**高**。理由：本文面向统一理解-生成模型中的物体级空间姿态操控这一前沿问题，提出统一的建模框架、新的姿态表征方法和专用基准，兼具方法论创新与数据贡献，对多模态大模型与3D视觉交叉领域的研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Unified models for visual understanding and generation have made rapid progress, yet they still lack the ability to understand and manipulate the spatial states of object instances. Existing models can describe objects in natural language, but they struggle to precisely represent continuous object poses and generate geometrically consistent images under target viewpoints. To mitigate this, we propose \emph{Object-Uni}, a unified model for object-centric spatial understanding and controllable generation. Specifically, we formulate object-centric spatial intelligence as a unified problem connecting pose perception, spatial reasoning, pose-conditioned generation, and object-centric novel view synthesis. We treat object pose as an explicit geometric variable shared by understanding and generation, rather than merely a prediction label or control signal. To make pose usable by multimodal large language models, we propose a viewpoint-based orientation abstraction that maps orientation into structured viewpoint descriptions while preserving continuous geometric supervision. We further construct an object-centric spatial benchmark (UniSpatial-80K) and train a unified model with an object-token-grounded pose anchor to associate each instance with its pose state. Experiments show that our model improves object-level pose understanding and pose-controllable generation, moving unified models from describing objects toward manipulating spatial states.

</details>

#### 2026-08-24 - Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization

**Authors:** Zeyang Bai, Yunpeng Wang, Yunbiao Wang, Jun Xiao
**Links:** [abs](https://arxiv.org/abs/2608.22740) - [pdf](https://arxiv.org/pdf/2608.22740)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization
- 作者：Zeyang Bai, Yunpeng Wang, Yunbiao Wang, Jun Xiao
- 出版日期：2026-08-24
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.22740

### 一句话总结
本文提出 SeeU 框架，通过将语义信息注入高斯空间（Semantic-in-Gaussian），利用跨视角熵感知模块和条件高斯变换器，提升稀疏视角下的三维重建与渲染质量，在结构完整性和渲染性能上超越现有 SOTA 方法。

### 研究问题
现有可泛化三维高斯泼溅（G-3DGS）框架依赖像素对齐的高斯估计，在部分观测或遮挡区域容易产生不完整表面或结构坍缩，导致稀疏视角下新视角合成质量受限。本文旨在解决如何在稀疏视角下恢复被遮挡或欠约束区域的结构信息，同时保持表面一致性。

### 核心思路/方法
- 提出 SeeU（Seeing the Unseen）框架，核心设计为 “Semantic-in-Gaussian”，即在高斯空间中进行语义条件化精化。
- 引入跨视角熵感知（Cross-view Entropy-Aware, CEA）模块，将多视角语义线索和几何线索聚合为紧凑嵌入。
- 这些嵌入作为条件，指导条件高斯变换器（Conditional Gaussian Transformer）对粗粒度高斯进行残差更新，从而恢复部分观测结构中被欠约束的区域，同时保持表面一致性。

### 主要贡献
- 提出 SeeU 框架，将语义信息引入高斯空间用于条件化精化，弥补像素对齐高斯估计在遮挡和部分观测区域的不足。
- 设计跨视角熵感知模块，有效聚合多视角语义与几何信息。
- 在多个基准上验证有效性，尤其在外推设置下，相比近期 SOTA G-3DGS 方法平均 PSNR 提升 2.44 dB，同时保持高效的前馈推理。

### 局限性
摘要未提及具体局限性，如计算开销、对语义标注的依赖程度、跨数据集泛化边界等，摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该方法针对稀疏视角三维重建中的关键痛点（遮挡与结构不完整），提出新颖的语义-高斯融合机制，且在多个基准上显示明显性能提升，对神经场景表示与渲染方向的研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Generalizable 3D Gaussian Splatting (G-3DGS) has emerged as a promising approach for novel view synthesis undersparse-view settings. However, existing frameworks remain restricted by pixel-aligned Gaussian estimation, whichstruggles in partially observed or occluded regions and often leads to incomplete surfaces or structural collapse. Toaddress these challenges, we propose SeeU (Seeing the Unseen), a novel G-3DGS framework. We frame its core design asSemantic-in-Gaussian: semantic-conditioned refinement in Gaussian space. Specifically, we introduce a Cross-viewEntropy-Aware (CEA) module that aggregates multi-view semantic and geometric cues into compact embeddings. Theseembeddings guide the Conditional Gaussian Transformer, which applies residual updates to coarse Gaussians, helpingrecover under-constrained regions of partially observed structures while preserving surface consistency. Comprehensiveexperiments on multiple benchmarks demonstrate that SeeU consistently improves rendering quality and structuralcompleteness while retaining efficient feed-forward inference. Especially under challenging extrapolation settings,SeeU achieves an average improvement of 2.44 dB in PSNR compared to recent SOTA G-3DGS methods.

</details>

#### 2026-08-23 - Fast and Compact 3D Gaussian Splatting with Polarized Opacity Prior

**Authors:** Zi-Ming Wang, Kai-Wen Duan, Kowei Huang, Akihiro Sugimoto, Shang-Hong Lai
**Links:** [abs](https://arxiv.org/abs/2608.22344) - [pdf](https://arxiv.org/pdf/2608.22344)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fast and Compact 3D Gaussian Splatting with Polarized Opacity Prior
- 作者：Zi-Ming Wang, Kai-Wen Duan, Kowei Huang, Akihiro Sugimoto, Shang-Hong Lai
- 出版日期：2026-08-23
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.22344

### 一句话总结
本文提出一种以极化不透明度先验（POP）为核心的训练框架，通过替代传统的“先稠密化后剪枝”流程，实现了3D高斯泼溅的快速、紧凑训练，在保持重建质量的同时显著减少高斯数量。

### 研究问题
3D高斯泼溅（3DGS）在实时渲染中达到先进质量，但存在“模型膨胀”问题：大量冗余、低不透明度的高斯导致内存占用和训练成本过高。该低效源于标准“稠密化-剪枝”范式——先激进扩展模型，再依赖剪枝实现紧凑。本文旨在构建一种本质紧凑的表示，替代该传统循环。

### 核心思路/方法
本文提出一个高效的训练框架，包含两个协同设计组件：
1. **L2重建损失**：提供与误差成比例的梯度，稳定优化过程。
2. **极化不透明度先验（POP）**：主动管理高斯群体，将信息丰富的高斯基元推向完全不透明，将无信息基元推向透明，从而实现自然剪枝，并通过早期光线终止（Early Ray Termination）加速渲染。

该方法替代了传统的“稠密化-剪枝”循环，从训练开始就构建紧凑表示。

### 主要贡献
- 提出一种新的训练框架，用内在紧凑表示取代传统“稠密化-剪枝”循环，避免模型膨胀。
- 设计极化不透明度先验（POP），主动管理高斯不透明度，实现自然剪枝和渲染加速。
- 在三个公开数据集上的实验表明，该方法在保持相当视觉重建质量的同时，显著减少高斯数量并加速3DGS训练。
- 提供了一个简单有效的路径，实现快速且本质紧凑的3DGS训练。

### 局限性
摘要未提供足够信息。摘要中未提及方法的失败案例、限制条件（如对特定场景或数据集类型的适用边界）、计算开销对比、以及对极端复杂场景的鲁棒性等。实验细节（如具体数据集名称、指标数值）也未给出。

### 阅读优先级
**高**。理由：3DGS是当前神经渲染领域的热点方向，模型膨胀问题直接影响实际部署效率。本文提出替代经典流程的训练框架，方法设计简洁且有公开实验支持（三数据集验证），对从事三维重建、实时渲染或模型压缩研究的读者具有直接参考价值。结合POP和L2损失的协同设计思路可能启发后续改进工作。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves state-of-the-art rendering quality at real-time speeds but suffers from "model bloat" - a large number of redundant, low-opacity Gaussians that inflate memory usage and training costs. This inefficiency stems from the standard "densify-then-prune" paradigm, which expands the model aggressively before relying on pruning to achieve compactness. To mitigate this problem, we present an efficient training framework that builds an intrinsically compact representation, replacing the conventional densify-then-prune cycle. Our method leverages a synergistic design: an L2 reconstruction loss to provide error-proportional gradients that stabilize optimization, and a novel Polarized Opacity Prior (POP) to actively manage the Gaussian population. POP steers informative primitives toward full opacity and uninformative ones toward transparency, enabling natural pruning and accelerating rendering through Early Ray Termination. Experiments on three public datasets demonstrate that our approach consistently achieves accelerated 3DGS training with significantly fewer Gaussians while maintaining comparable visual reconstruction quality. These results show that the proposed framework provides a simple and effective path toward fast and inherently compact 3DGS training.

</details>

#### 2026-08-20 - 4DAnyone: Create Anyone in 4D from a Casual Monocular Video

**Authors:** Yudong Jin, Tao Xie, Qihang Zhang, Zehong Shen, Zhen Xu, Yujun Shen, Hujun Bao, Xiaowei Zhou, Yinghao Xu
**Links:** [abs](https://arxiv.org/abs/2608.20335) - [pdf](https://arxiv.org/pdf/2608.20335)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4DAnyone: Create Anyone in 4D from a Casual Monocular Video
- 作者：Yudong Jin, Tao Xie, Qihang Zhang, Zehong Shen, Zhen Xu, Yujun Shen, Hujun Bao, Xiaowei Zhou, Yinghao Xu
- 出版日期：2026-08-20T17:59:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.20335

### 一句话总结
本文提出4DAnyone框架，通过生成多视角一致的视频并将其提升为4D高斯泼溅，实现从随意单目视频重建4D人体，并解决了视频扩散模型在多视角扩展时的上下文瓶颈问题。

### 研究问题
如何从未标定的单目视频中重建4D人体，尤其是如何解决现有相机控制视频扩散模型在目标视角数量增加（需数十个视角以支撑4DGS重建）时无法保持多视角一致性的问题。

### 核心思路/方法
- 将问题拆解为两个耦合瓶颈：参考上下文方面（所有已生成视角的条件信息呈O(N)增长，削弱跨视角外观指导）和目标上下文方面（分组后不连续的目标视角组之间无法直接交换信息，导致全局结构漂移）。
- 设计**Reference Context Packing (RCP)**：将不断增长的参考视角压缩为固定长度的混合分辨率上下文，将参考上下文复杂度降至O(1)。
- 设计**Target Context Routing (TCR)**：在去噪过程中轮换目标视角的分组方式，高噪声步时跨组共享上下文，低噪声步时稳定细节。
- 使用自研游戏引擎构建MVGameHuman数据集，并与光舞台及野外视频数据集结合进行训练。

### 主要贡献
- 提出4DAnyone框架，实现从随意单目视频到4D人体的重建。
- 识别并形式化了视频扩散模型在多视角生成中的“有界注意力上下文”问题，指出其两个耦合瓶颈。
- 提出RCP和TCR两种互补设计，分别解决参考上下文增长和目标上下文隔离问题。
- 在DNA-Rendering和DyMVHumans上验证方法有效性，在novel-view视频质量和4DGS重建方面均优于此前方法，并展示野外泛化鲁棒性。

### 局限性
摘要未提供足够信息。摘要中未明确讨论方法的失败案例、计算成本、训练数据规模对性能的影响，也未提及在复杂遮挡、极端姿态或户外真实场景下的具体限制。

### 阅读优先级
**高**。理由：该工作在4D人体重建方向提出明确的框架和方法论贡献，针对视频扩散模型的实际瓶颈提出了工程上可行的解决方案，并在公开数据集上取得了显著提升，且附带项目页面和开源代码。对于从事神经渲染、4D重建、人体数字化等方向的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

We present 4DAnyone, a framework for reconstructing 4D humans from an uncalibrated monocular video by generating reconstruction-grade multiview-consistent videos and lifting them into 4D Gaussian Splatting (4DGS). Existing camera-controlled video diffusion models synthesize plausible novel-view videos but fail to maintain consistency when scaled to the tens of target views required for 4DGS reconstruction. We identify this failure as a bounded-attention-context problem: when target views exceed the capacity of a single DiT forward pass, they must be split into groups, exposing two coupled bottlenecks. On the reference-context side, conditioning on all previously generated views grows as $O(N)$, weakening cross-view appearance guidance. On the target-context side, disjoint groups cannot directly exchange information, causing global structural drift. 4DAnyone addresses both bottlenecks with two complementary designs: Reference Context Packing (RCP) compresses growing reference views into a fixed-length mixed-resolution context with $O(1)$ reference-context complexity, while Target Context Routing (TCR) rotates target-view groupings during denoising to share context across groups at high-noise steps and stabilize details at low-noise steps. We further build the MVGameHuman dataset using our in-house game engine and combine it with light-stage and in-the-wild video datasets for training. Experiments on DNA-Rendering and DyMVHumans show that 4DAnyone outperforms prior methods in both novel-view video quality and downstream 4DGS reconstruction, with robust in-the-wild generalization. See our project page for video results and source code: https://4danyone.github.io.

</details>

#### 2026-08-19 - GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting

**Authors:** Yechan Park, HyunJin Kim
**Links:** [abs](https://arxiv.org/abs/2608.19066) - [pdf](https://arxiv.org/pdf/2608.19066)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting
- 作者：Yechan Park, HyunJin Kim
- 出版日期：2026-08-19
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.19066

### 一句话总结
本文提出一种轻量级即插即用模块，利用3D高斯场景表示将观测视角归一化，从而在不重新训练策略的前提下增强冻结的视觉-语言-动作（VLA）策略对视角变化的鲁棒性。

### 研究问题
VLA策略在训练与部署时相机配置不一致（视角偏移）会导致性能显著下降，现有应对方法（大规模微调或生成式数据增强）计算成本高且存在灾难性遗忘风险。本文旨在解决如何在不重训练策略的条件下，高效恢复VLA策略在视角偏移下的性能损失。

### 核心思路/方法
- 将视角偏移重新建模为局部化新视角合成问题。
- 基于“局部性假设”（相机扰动相对于工作空间保持在较小有界范围内），将视角归一化转化为场景无关、策略无关的遮挡补全（disocclusion）任务。
- 实现方式：在冻结的VLA策略前接入一个仅含400万参数的3D高斯canonicalizer模块，该模块负责将观测图像进行视角规范化处理，不修改策略任何权重。

### 主要贡献
- 首次直接将3D高斯新视角合成用于VLA策略的观测空间适配。
- 提出轻量级即插即用框架GS-VLA，无需策略重训练即可提升对视角变化的鲁棒性。
- 在三个正交维度上验证了方法有效性：不同策略架构、未见任务套件、不同扰动尺度。
- 实验表明，该方法能恢复视角偏移下丢失的大部分性能，而无需修改策略权重。

### 局限性
摘要未提供足够信息，包括但不限于：具体实验设置细节、基线对比方法的完整列表、计算资源需求、在真实物理机器人上的验证情况、3D高斯模块的推理延迟或额外开销、对极端视角偏移或非局部性扰动的适应性边界等。

### 阅读优先级
**高**。理由：该论文针对VLA策略部署中实际存在的视角敏感性问题，提出一种轻量且无需重训练的解决方案，实验显示在LIBERO基准上极端情况下可恢复从约10%到接近原始90%的性能损失，具有较强实用价值；且方法新颖（首次将3D高斯渲染用于VLA观测适配），对具身智能领域的研究者和工程师均有参考意义。

</details>

<details>
<summary>Abstract</summary>

This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displacement of the camera mount can reduce the success rate on the LIBERO benchmark from about 90% to about 10% in the worst case. Prior approaches, such as large-scale fine-tuning or generative data augmentation, are computationally expensive and risk catastrophic forgetting. To address this, viewpoint shifts are reformulated as a localized novel-view synthesis problem. Under a Locality assumption, that camera perturbations remain within a small bounded region relative to the workspace, viewpoint normalization reduces to a scene- and policy-independent disocclusion task. Our work implements this idea with a 4M-parameter 3D-Gaussian canonicalizer prepended to a frozen VLA policy. Without modifying policy weights, GS-VLA improves performance across three orthogonal axes: (1) Policy architectures, (2) Unseen task suites, and (3) Perturbation scales. These results show that a lightweight visual module can recover a large fraction of the performance lost under viewpoint shift, without policy retraining.

</details>

#### 2026-08-19 - USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes

**Authors:** Li-Heng Chen, Haokai Pang, Chengye Su, Jiarun Liu, Qifeng Chen, Ziqian Ni, Jianxin Huang, Shi-Sheng Huang, Hongbo Fu, Sheng Yang
**Links:** [abs](https://arxiv.org/abs/2608.19036) - [pdf](https://arxiv.org/pdf/2608.19036)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** dynamic reconstruction, scene representation, rendering, autonomous driving, driving scene, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes
- 作者：Li-Heng Chen, Haokai Pang, Chengye Su, Jiarun Liu, Qifeng Chen, Ziqian Ni, Jianxin Huang, Shi-Sheng Huang, Hongbo Fu, Sheng Yang
- 出版日期：2026-08-19T15:29:06Z
- 分类：Neural Scene Representations & Rendering；次要分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.19036

### 一句话总结
USR-Drive提出一个统一的生成式框架，通过联合去噪3D高斯与3D边界框，在一个共享场景表示中同时恢复动态几何和实例级目标布局，实现动态重建与3D检测的相互增强。

### 研究问题
如何将自动驾驶中的动态场景重建（密集几何）与实例级感知（3D检测）从分离的任务统一为一个共享的生成式框架，使两者相互约束、互补提升，而不是像以往那样将边界框仅作为外部条件或使用解耦模块预测。

### 核心思路/方法
- 将密集3D高斯原语和稀疏3D边界框表示为两个对齐的潜在token流；
- 使用统一的多模态扩散Transformer对二者进行联合去噪；
- 提出统一位置编码（Unified Positional Encoding, UPE），将异构token对齐到共享的度量时空坐标系中；
- 两种模态互为约束：几何为框预测提供密集度量证据，框为几何提供实例级结构先验，减少时序3D几何表示中的歧义并保持空间一致性。

### 主要贡献
- 提出统一的生成式条件框架，仅需带位姿的多视角驾驶视频即可联合恢复动态几何与实例级布局；
- 将3D高斯与3D边界框建模为相互约束的状态变量而非外部条件，区别于以往解耦范式；
- 设计统一位置编码以对齐异构多模态token；
- 在nuScenes和VKitti数据集上，动态重建与3D检测均取得最优结果。

### 局限性
摘要未提供足够信息（未提及失败案例、计算开销、对极端场景的鲁棒性、训练数据需求或与SOTA的量化差距等具体局限）。

### 阅读优先级
**高**
理由：该工作直接针对自动驾驶中“重建-感知”割裂的瓶颈问题，提出统一生成式框架，且同时覆盖动态重建与3D检测两个核心任务，方法设计新颖（联合去噪+统一位置编码），并在两个公开数据集上取得SOTA，对场景表示学习、扩散模型应用和自动驾驶感知方向均有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial representation learning for autonomous driving aims to map raw visual signals into structured 3D scene representations, where object-centric bounding boxes and rendering-oriented 3D primitives (\eg, 3D Gaussians) serve as two distinct yet highly complementary levels for scene understanding. Existing methods typically treat dynamic reconstruction and instance-level perception as separate tasks, despite their shared goal of estimating the underlying 3D world state. As a result, dynamic reconstruction is under-constrained while 3D detection lacks geometric grounding. To address this gap, we propose USR-Drive, a unified conditional generative framework that, given only posed multi-view driving videos, jointly recovers dense dynamic geometry and instance-level object layouts within a shared scene representation. Specifically, USR-Drive represents dense Gaussian primitives and sparse 3D bounding boxes as two aligned latent token streams and jointly denoises them with a unified multi-modal diffusion Transformer. Unlike prior paradigms that use boxes as external conditions or predict them with detached modules, USR-Drive treats them as mutually constrained state variables with a Unified Positional Encoding (UPE) that aligns heterogeneous tokens within a shared metric spatiotemporal coordinate. Via such unified representation and generative framework, the two modalities reinforce each other: geometry supplies dense metric evidence for box prediction, while boxes provide instance-level structural priors that help preserve spatial consistency and reduce ambiguity in sequential 3D geometric representation. Our approach successfully delivers state-of-the-art results for both dynamic reconstruction and 3D detection on the nuScenes and VKitti datasets.

</details>

## Embodied / Robotics / AR Applications

### 2026-08

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

#### 2026-08-24 - GeoWAM: Visual Geometry World Action Models for Autonomous Driving

**Authors:** Yiren Lu, Xin Ye, Jiaming Liu, Philip Jacobson, Jin Yao, Yi-chung Chen, Liam Merino, Dhruva Dixith Kurra, Min Cai, Tom Lampo, Yu Yin, Danhua Guo, Burhan Yaman
**Links:** [abs](https://arxiv.org/abs/2608.23486) - [pdf](https://arxiv.org/pdf/2608.23486)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoWAM: Visual Geometry World Action Models for Autonomous Driving
- 作者：Yiren Lu, Xin Ye, Jiaming Liu, Philip Jacobson, Jin Yao, Yi-chung Chen, Liam Merino, Dhruva Dixith Kurra, Min Cai, Tom Lampo, Yu Yin, Danhua Guo, Burhan Yaman
- 出版日期：2026-08-24
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.23486

### 一句话总结
GeoWAM 提出以未来场景几何（点云）预测替代传统像素级视频预测，作为自动驾驶世界动作模型的预训练目标，从而学习更符合驾驶动作执行空间的场景动态表征。

### 研究问题
现有世界动作模型（WAM）在像素空间学习场景动态，但像素将几何、运动与外观、纹理、光照纠缠在一起，迫使模型从二维观测推断三维变换，这种间接表征不利于驾驶场景的几何与运动建模。研究问题为：能否直接用三维几何（点云）作为状态空间来建模场景演化与驾驶动作？

### 核心思路/方法
- 构建视觉几何世界动作模型（GeoWAM），核心是用点云表示驾驶场景的几何状态。
- 预训练阶段：预测未来场景几何（点云），而非未来图像，使模型表征同时编码空间结构与时间演化。
- 动作预测阶段：设计几何条件化的动作头（geometry-conditioned action head），利用学到的几何动态信息预测未来自车轨迹。
- 评估方式：进行开环与闭环评估，对比基于图像的世界模型方法。

### 主要贡献
1. 提出以未来几何预测作为驾驶世界模型预训练目标的新范式，替代像素空间的视频生成。
2. 引入 GeoWAM 模型架构，将点云作为驾驶动作执行的自然状态空间。
3. 通过开环与闭环实验证明：视觉几何世界建模相比基于图像的方法能产生显著更强的驾驶策略。

### 局限性
摘要未提供足够信息。摘要未提及具体数据规模、评估场景范围、计算资源需求、模型在极端场景下的表现，以及与基线方法的具体量化差距等细节。

### 阅读优先级
**高**

理由：该工作提出将世界动作模型从像素空间转向几何（点云）空间，这是一个具有范式意义的方向转变，且摘要报告了开环与闭环评估中的显著性能提升。对从事自动驾驶决策建模、世界模型、几何深度学习的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics in pixel space by combining a video-generation backbone for future-observation prediction with an action head for ego-trajectory prediction. Pixels, however, provide only an indirect representation of these dynamics: they entangle geometry and motion with appearance, texture, and illumination, forcing the model to infer three-dimensional transformations from two-dimensional observations. We argue that geometry, represented by point clouds, offers a more natural state space for driving because it explicitly captures spatial structure and the rigid and non-rigid transformations that govern scene evolution while directly aligning with the space in which driving actions are executed. Building on this insight, we introduce \textbf{GeoWAM}, a visual geometry world action model for autonomous driving. Rather than predicting future images, GeoWAM is pretrained to forecast future scene geometry, yielding representations that jointly encode spatial structure and temporal evolution. A geometry-conditioned action head then leverages these learned geometric dynamics to predict future ego trajectories. Extensive open-loop and closed-loop evaluations show that visual geometry world modeling yields substantially stronger driving policies than image-based alternatives, establishing future-geometry prediction as an effective pretraining objective for autonomous driving.

</details>

#### 2026-08-23 - DreamMimic: Learning Visuomotor Whole-Body Loco-Manipulation via World Model

**Authors:** Jie Yin, Xingyu Lai
**Links:** [abs](https://arxiv.org/abs/2608.22278) - [pdf](https://arxiv.org/pdf/2608.22278)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DreamMimic: Learning Visuomotor Whole-Body Loco-Manipulation via World Model
- 作者：Jie Yin, Xingyu Lai
- 出版日期：2026-08-23T08:08:39Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.22278

### 一句话总结
DreamMimic 提出一种基于世界模型辅助蒸馏的框架，将特权教师策略蒸馏为基于视觉的类人机器人全身移动操作控制器，并在 OMOMO 和 BEHAVE 基准上超越强视觉基线。

### 研究问题
如何利用世界模型稳定地将特权教师策略蒸馏为基于视觉输入的类人机器人全身移动操作策略，以应对部分可观测性、接触丰富的动力学以及从高维视觉输入学习长期行为带来的挑战。

### 核心思路/方法
- 将 Dreamer 风格的 RSSM 重新用于学习预测性潜在动力学，而非规划，同时作为表示空间和动作条件多步监督信号。
- 向学生策略暴露紧凑的预测特征以减少长期漂移。
- 在标准重建目标之外，增加针对特权状态、接触、物体状态和奖励估计的辅助预测头，以强化与智能体-物体交互及任务进展相关的潜在表示。
- 提出性能条件引导（PCG），一种奖励驱动的自适应蒸馏调度，通过计算教师和学生策略的性能分数来动态平衡引导与探索，避免过早教师退化和过度教师干扰。

### 主要贡献
- 提出 DreamMimic 框架，利用世界模型辅助蒸馏解决基于视觉的类人机器人移动操作策略学习问题。
- 通过辅助预测头（包括特权状态、接触、物体状态和奖励）增强潜在表示对接触丰富交互的适用性。
- 引入性能条件引导（PCG）自适应蒸馏调度机制，改善视觉场景下的训练稳定性。
- 在 OMOMO 和 BEHAVE 上展示了相对于强视觉基线的跟踪式移动操作性能提升，且部署时不向学生暴露在线特权交互状态。

### 局限性
- 摘要未提供关于计算成本、模型规模、训练稳定性、泛化边界或失败案例等具体局限性信息。
- 摘要中提到“定性仿真进一步检验形态和模拟器变化”，但未提供详细实验细节或定量结果。
- 摘要未提供足够信息说明该方法在真实机器人上的部署表现。

### 阅读优先级
**中**

理由：该工作面向类人机器人全身移动操作这一特定且有挑战的方向，方法上结合世界模型蒸馏与自适应引导，具有一定创新性且基准结果优于强基线。但作者仅两位且无机构信息，论文发表于 arXiv（2026年），未提供会议/期刊发表信息，且摘要未给出详细的实验设置与量化对比，验证强度有限。适合关注机器人学习、视觉策略蒸馏和世界模型应用的读者阅读，但优先级不宜过高。

</details>

<details>
<summary>Abstract</summary>

Vision-based whole-body loco-manipulation on humanoid robots is challenging due to partial observability, contact-rich dynamics, and the difficulty of learning long-horizon behaviors from high-dimensional visual inputs. We present \href{https://github.com/DreamMimic/DreamMimic}{DreamMimic}, a framework that distills privileged teacher policies into vision-based humanoid controllers via world-model-assisted distillation. Instead of using a Dreamer-style RSSM for planning, we repurpose it to learn predictive latent dynamics that serve as both a representation space and an action-conditioned multi-step supervision signal, while exposing compact predictive features to the student policy to reduce long-term drift. Beyond standard reconstruction objectives for proprioceptive and visual observations, we add auxiliary prediction heads for privileged state, contact, object state, and reward estimation. These heads provide additional supervision related to agent--object interaction and task progress, encouraging the latent representation to retain signals that are useful for contact-rich loco-manipulation. We further introduce Performance-Conditioned Guidance (PCG), a reward-driven adaptive distillation schedule that computes performance scores for both teacher and student to dynamically balance guidance and exploration. PCG prevents both premature teacher annealing and excessive teacher interference in challenging visual settings. Experiments on OMOMO and BEHAVE show improved tracking-based loco-manipulation performance over strong vision-based baselines, without exposing online privileged interaction states to the student at deployment. Qualitative simulations further examine morphology and simulator changes. These results suggest that world models can provide a useful mechanism for stabilizing visual policy distillation in contact-rich humanoid behaviors.

</details>

#### 2026-08-21 - Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding

**Authors:** Jie Xu, Na Zhao
**Links:** [abs](https://arxiv.org/abs/2608.21136) - [pdf](https://arxiv.org/pdf/2608.21136)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding
- 作者：Jie Xu, Na Zhao
- 出版日期：2026-08-21
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.21136

### 一句话总结
Stream3Dv2 是一个免训练的流式零样本 3D 场景理解框架，通过几何-语义融合机制和流式局部-历史架构，解决实时 RGB-D 输入下的噪声掩码与计算开销问题。

### 研究问题
现有的开放词汇零样本 3D 场景理解方法无法高效处理流式 RGB-D 输入，且对 2D 分割掩码的噪声敏感，限制了其在真实世界场景中的部署。本文旨在解决这两个关键缺陷。

### 核心思路/方法
- 提出 Stream3Dv2，一个新颖的免训练框架，用于鲁棒的流式 3D 感知。
- 通过嵌套的“局部到历史”（nested local-to-historical）架构处理序列数据，捕获多视角一致性，同时避免高计算开销以支持及时响应。
- 引入几何-语义融合机制，显式利用语义引导，将 3D 分割形式化为点-集合合并与划分问题，以解决几何噪声和语义歧义。
- 提出基于流形距离的点云细化策略：使用局部流形图进行点-流形优化，缓解欧氏距离度量导致的边界划分失败；利用几何包围盒动态激活和更新历史实例，实现快速流形-流形细化。

### 主要贡献
- 提出 Stream3Dv2，用于鲁棒流式 3D 感知的免训练框架。
- 设计几何-语义融合机制，解决流式 3D 分割中的几何噪声与语义歧义。
- 提出基于流形距离的点云细化策略，改善边界划分并支持快速历史实例更新。
- 在公开数据集上的实验表明，Stream3Dv2 在基础开放词汇流式 3D 分割和检测任务上持续优于现有基线。
- 与基于 LLM 的智能体集成，支持语言驱动的 3D 场景理解，展示其在开放世界具身智能中的潜力。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的失败案例、对特定场景（如极端噪声或动态遮挡）的鲁棒性边界、运行效率的具体数值（如推理速度或显存占用），也未提及与既有流式方法的计算复杂度对比细节。

### 阅读优先级
**高**。理由：该工作针对流式零样本 3D 理解这一实际部署关键问题提出了免训练的解决方案，技术上融合了几何-语义融合与流形优化，且与 LLM 智能体结合，具备较强的应用前景和扩展价值。摘要中显示出在公开数据集上的一致性能提升，适合关注 3D 感知、开放词汇理解和具身智能的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recently, open-vocabulary zero-shot 3D scene understanding using vision foundation models has emerged as a promising alternative to data-intensive supervised methods. However, deploying these models in real-world scenarios is severely hindered by their inability to efficiently handle streaming RGB-D inputs and their inherent vulnerability to noise 2D segmentation masks. To address these critical limitations, we propose Stream3Dv2, a novel training-free framework designed for robust streaming 3D perception. Stream3Dv2 processes sequential data through an original nested local-to-historical architecture, capturing multi-view consistency while circumventing the high computational overhead so as to support timely responses. At its core, we introduce a comprehensive geometric-semantic fusion mechanism that resolves geometric noise and semantic ambiguity by explicitly utilizing semantic guidance and formulating 3D segmentation as solving point-and-set merging and partitioning problems. Furthermore, we present an innovative manifold-distance-based point cloud refinement strategy. This approach leverages local manifold graphs for point-to-manifold optimization that mitigates the boundary delineation failures caused by Euclidean-distance metrics, and employs geometric bounding boxes to dynamically activate and update historical instances for achieving rapid manifold-to-manifold refinement. Extensive experiments on public datasets demonstrate that Stream3Dv2 consistently outperforms existing baselines in foundational open-vocabulary streaming 3D segmentation and detection. Finally, we show that integrating our framework with an LLM-based agent enables advanced language-driven 3D scene understanding, underscoring its potential for open-world embodied intelligence. Code will be updated at https://github.com/SubmissionsIn/Stream3D.

</details>

#### 2026-08-19 - SceneGTMM: A Conformal Mapping-based Scene-Aware Transferable GNN-Transformer Dual-Graph Interaction Framework for Map Matching

**Authors:** Yongliang Zhang, Feng Song, Ji Chen, Lishuai Guo, Yong Deng, Yue Zheng, Tianyi Liu, Zhixiong Chen, Qixin Zhang
**Links:** [abs](https://arxiv.org/abs/2608.19298) - [pdf](https://arxiv.org/pdf/2608.19298)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SceneGTMM: A Conformal Mapping-based Scene-Aware Transferable GNN-Transformer Dual-Graph Interaction Framework for Map Matching
- 作者：Yongliang Zhang, Feng Song, Ji Chen, Lishuai Guo, Yong Deng, Yue Zheng, Tianyi Liu, Zhixiong Chen, Qixin Zhang
- 出版日期：2026-08-19
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.19298

### 一句话总结
本文提出了一种基于共形映射场景相对策略的GNN-Transformer双图交互框架SceneGTMM，用于实现高精度、可跨区域迁移的地图匹配方法。

### 研究问题
地图匹配技术在噪声鲁棒性、跨区域迁移和可解释性方面存在挑战，现有方法在局部-全局融合、动态路网适应以及对黑盒模型的依赖上存在局限。

### 核心思路/方法
论文提出SceneGTMM框架，包含三个主要技术模块：
1. 基于共形映射的场景相对策略：构建以轨迹为中心的局部坐标系，减少对训练路网的依赖，从而支持跨区域迁移和动态路网更新；
2. GNN-Transformer双图交互架构：GNN建模路网图以捕获局部拓扑约束，Transformer建模轨迹图以捕获全局时序依赖，并通过跨图注意力实现噪声抑制和语义对齐；
3. CRF增强的结构化预测：将Transformer的全局上下文与CRF的拓扑转移约束结合，提升路径连通性和鲁棒性。

### 主要贡献
- 提出共形映射场景相对策略，降低对训练路网的依赖，支持跨区域迁移；
- 设计GNN-Transformer双图交互架构，融合局部拓扑约束与全局时序依赖，并通过跨图注意力实现噪声抑制；
- 引入CRF增强的结构化预测，提升路径连通性和鲁棒性；
- 实验表明该方法在多种源轨迹和不同定位误差条件下均优于基线方法，并通过注意力与相对坐标可视化增强可解释性。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的计算复杂度、实时性能、对极端场景（如严重遮挡或信号丢失）的适应能力，以及在不同道路类型（如城市密集路网与乡村稀疏路网）上的具体表现差异。

### 阅读优先级
**中**
- 理由：该工作面向地图匹配这一具体应用场景，方法新颖性较高（结合共形映射、GNN、Transformer与CRF），并有定量改进数据支撑。但该领域相对垂直，且论文发表于2026年，研究时效性尚需验证；若您的研究方向涉及轨迹数据挖掘、智能交通或自动驾驶路径规划，则值得精读，否则可暂缓。

</details>

<details>
<summary>Abstract</summary>

Map matching is a key technology connecting positioning data with high precision road networks, but it faces challenges in noise robustness, cross regional transfer, and interpretability. To addr ess the limitations of existing methods in local global fusion, dynamic road network adaptation, and reliance on black box mod els, this paper proposes SceneGTMM, a transferable GNN Transformer dual graph interaction map matching framework based on a conformal mapping based scene relative strategy. 1) Conformal mapping based scene relative strategy: constructs trajectory centric local coordinate systems to reduce dependence on the training road network, supporting cross regional transfer and dynamic road network updates; 2) GNN Transformer dual graph interaction architecture: a GNN modeled road graph captures local topological constraints, while a Transformer modeled trajectory graph captures global temporal dependencies, and cross graph attention achieves noise suppression and semantic alignment; 3) CRF enhanced structured prediction: combines the global context of the Transformer with the topological transition constraints of CRF to improve path connectivity and robustness. Experiments show that SceneGTM achieves over 80% accuracy on multi source trajectories with positioning errors of 16 50 meters, representing a 5.3% improvement over HMM. In cross city transfer scenarios, it outperforms MTrajRec, GraphMM, and TMM, and enhances interpretability through attention and relative coordinate visualization. This study provides a new paradigm for high precision, transferable map matching for real time traffic perception and autonomous driving path planning.

</details>

#### 2026-08-19 - LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding

**Authors:** Yumin Lee, Hyoseok Ju, Giseop Kim
**Links:** [abs](https://arxiv.org/abs/2608.19059) - [pdf](https://arxiv.org/pdf/2608.19059)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding
- 作者：Yumin Lee, Hyoseok Ju, Giseop Kim
- 出版日期：2026-08-19
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.19059

### 一句话总结
LT-Mem提出了一种基于易变性感知的时空记忆框架，通过三层记忆结构（Live、Delta、Meta）和波动性调节策略，实现对长期场景中对象跨会话历史的持续理解与推理。

### 研究问题
长期运行的机器人在动态演化环境中面临“时间性失忆”问题：现有系统要么覆盖历史以维持最新地图，要么存储语义快照但缺乏跨会话一致的对象身份，导致无法回答如“绿色椅子在所有会话中出现在哪些位置？”这类需要对象历史信息的问题。

### 核心思路/方法
1. **多会话SLAM骨干**：提供跨会话空间对齐的逐对象观测数据。
2. **推理层（易变性感知策略）**：通过确定性证据评分保持跨会话身份一致性，并基于每个对象的动态特征，在“覆盖（overwrite）”、“保持（hold）”和“多假设（multi-hypothesis）”三种动作中进行选择。
3. **Tri-Memory结构**：包含Live（当前状态）、Delta（变化信息）和Meta（事件历史）三个部分，同时保留当前状态与事件历史，支持纵向对象中心推理。
4. **评估数据集LT-VQA**：包含多会话记录、持久身份标注和时间问答对，用于系统评估。

### 主要贡献
- 提出了LT-Mem，一个将空间对齐的实例级3D感知与易变性条件时间推理相统一的记忆演化框架。
- 设计了Tri-Memory结构，解决了跨会话对象身份一致性与历史信息保留的兼顾问题。
- 引入了LT-VQA数据集和评估套件，包含多会话记录、持久身份标注和时间QA对。
- 实验表明LT-Mem在所有指标上持续优于基线，且消耗的token数量少一个数量级；消融实验确认性能提升来自结构化记忆架构而非LLM容量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接面向机器人长期场景理解中对象历史遗忘这一实际痛点，提出了新颖的三层记忆架构与易变性感知策略，并配套了专门的数据集。其在效率和性能上均有显著优势声明，对持续学习、场景理解及具身智能方向的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Long-term robot operation in evolving environments requires object-level understanding that persists across repeated revisits. Existing systems either overwrite history to maintain an up-to-date map or store semantic snapshots without consistent cross-session object identity, resulting in temporal amnesia: the systematic loss of object history that prevents answering queries such as "Where has the green chair been across all sessions?" We propose LT-Mem, a volatility-aware memory evolution framework that unifies spatially aligned instance-level 3D perception with volatility-conditioned temporal reasoning. First, a multi-session SLAM backbone provides spatially aligned per-object observations across sessions. Second, a reasoning layer governs how object memory evolves: deterministic evidence scoring preserves cross-session identity, and a volatility-aware policy selects among overwrite, hold, and multi-hypothesis actions based on each object's dynamics. Third, the resulting Tri-Memory structure (Live, Delta, Meta) preserves both current states and event histories, enabling longitudinal object-centric reasoning. We further introduce LT-VQA, a dataset and evaluation suite comprising multi-session recordings, persistent identity annotations, and temporal QA pairs. Experiments show that LT-Mem consistently outperforms baselines across all metrics while consuming an order of magnitude fewer tokens, and ablations confirm that gains are driven by the structured memory architecture rather than LLM capacity.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
