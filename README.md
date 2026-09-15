# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：21
- 分类分布：
  - Neural Scene Representations & Rendering: 7
  - Embodied / Robotics / AR Applications: 6
  - 3D Reconstruction & Multi-view Geometry: 5
  - Geometry Foundation Models: 2
  - Dynamic / 4D Reconstruction: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **从“新视角合成”走向“物理量渲染”：雷达、全息、雾天介质成为新前沿**
   今日多篇论文不再满足于 RGB 意义上的“看起来对”，而是要求渲染器输出可被下游物理系统直接使用的量。`3DPS` 直接从雷达方程立体角形式推导可微点渲染，输出复数相量而非功率幅度；`CVQPG` 把 2D 高斯基元替换为二次相位函数，直接调制全息波前；`Tri-DehazeGS` 把场景与参与介质显式解耦，用独立三平面场建模散射介质。三者共同指向一个趋势：**神经渲染器正在从“图像逼真”转向“物理保真”**，且介质、相位、材质被显式建模而非交给不透明隐特征。

2. **3DGS 生态进入“精细化治理”阶段：剪枝、不确定性认证、跨表示蒸馏、重定位耦合**
   3DGS 不再只是“如何建得更快更好”，而是围绕其工程与可信度缺陷做系统性补丁。`LinearMask-GS` 聚焦学习掩码剪枝中 Gumbel-Sigmoid 导致的早熟双峰分布，改线性增量激活；`VSCP` 关注 3DGS 渲染的视图级覆盖保证，把新视角合成当作结构化回归做共形预测；`RouteBridge` 处理 NeRF 与 3DGS 之间“全局固定教师会传播局部误差”的问题，按光线做可靠性路由；`RIDE` 则把 render–match–PnP 重定位的稀疏度量深度与视频深度先验结合，让 3DGS 地图反过来服务稠密深度。这类工作数量最多，说明**3DGS 正从表示创新期转入可靠性与可部署性补课期**。

3. **几何基础模型与图像匹配的边界正在消融，但“零样本匹配”本身仍未解决**
   `RoMa-$Ω$` 直接追问“前馈 3D 模型到底知道多少图像匹配”，通过三种场景（patch 特征零样本匹配、3D 点预测直接匹配、在其表征上训练完整匹配器）进行分析，并以 VGGT-$Ω$ 替换 DINO 骨干。`SAMV-DUSt3R` 则把 SAM2 2D 掩码注入 MV-DUSt3R，做实例级场景解耦。`Learning Global Camera Poses from Noisy View-Graphs` 用置换等变边条件 GNN 从带噪相对位姿回归全局外参，无需真值监督。这些工作共同反映：**几何基础模型正在吸收匹配与解耦能力，但“零样本深层特征直接做匹配”表现不佳，仍需要在其表征之上训练任务头**，这本身是一个被实验明确化的空白。

4. **动态/4D 重建向长时程突破，前馈模型开始处理数百帧**
   `Point4D` 明确针对现有 4D 方法“至多几十帧”的窗口限制，用基于 3D 查询的运动解码器解耦轨迹预测与图像平面可见性，预测的 3D 端点可在下一时间块直接重新查询，无需重投影或匹配。这代表 **4D 重建的竞赛焦点从“短窗口精度”转向“长时程稳定跟踪”**，且“跨帧复用视觉描述符优于仅用源 patch”是一个可复用的设计结论。

5. **具身与机器人应用层开始整合“感知—仿真—控制—运维”全链路，而非单点算法**
   `HROS`/Argos 把四足巡检组织为机器人运行时、自主技能、认知智能体运行时、交互运维平面，并用共享上下文连接物理状态与推理；`SyncWorld` 用“视觉校准片段”在上下文里指定动作-视觉映射，使世界模型成为零样本模拟器；`Grounding Generated Video Plans` 用生成 HOI 视频提供运动参考、在仿真中 grounding 超过 1500 个视频；`RealSimLoop` 在降阶神经子空间做可微仿真，用视觉反馈在线校正材料参数。**机器人方向今日的关键词是“闭环”与“校准”**——动作不是像素空间的通用语言，视觉校准、可靠性路由、安全门控都是为了让闭环可控。

#### 技术路线观察

- **几何基础模型**：`RoMa-$Ω$` 和 `Learning Global Camera Poses` 代表两条不同路线。前者是“表征复用”——把前馈重建模型（VGGT）的内部表征迁移到匹配器；后者是“端到端学习全局 SfM”——用图神经网络直接回归全局外参，训练信号仅为相对位姿一致性。`SAMV-DUSt3R` 则走“注入式”路线，把 2D 基础模型（SAM2）的掩码作为条件信号注入重建网络。三者的共同点是不再迷信单一基础模型的零样本能力，而是**显式地在其上做条件化、路由或重训练**。

- **3D/4D 重建**：`Point4D` 是今日唯一明确的长时程 4D 工作，技术核心是“查询解耦”——3D 端点跨块直接重查询，绕过重投影与匹配，这对长视频中的漂移控制有直接价值。`Field Converter` 则代表体育/转播场景的世界坐标人体姿态，用相机与球场几何初始化根节点、再预测时序残差，其“几何初始化+残差精修”的范式与 `Point4D` 的“查询+重查询”形成有趣对照：都是用几何或查询提供稳定锚点，再让网络学习修正量。

- **神经场景表示**：分化最明显。雷达（`3DPS`）走物理方程推导路线，强调复值与材质；全息（`CVQPG`）走波前调制路线，强调频域保留；雾天（`Tri-DehazeGS`）走场景-介质解耦路线，强调梯度重平衡；3DGS 压缩（`LinearMask-GS`）与可靠性（`VSCP`）走工程治理路线；跨表示（`RouteBridge`）走按光线路由路线。**没有单一主导技术路线，而是按输出物理量、介质假设和可靠性需求分层演化**。

- **机器人/AR 应用**：`HROS`、`SyncWorld`、`Grounding Generated Video Plans`、`RealSimLoop` 共同显示，应用层论文的贡献越来越难用单一算法指标衡量，而是以系统能力（闭环可追踪、零样本迁移、参考运动可扩展、在线自适应）来主张价值。`GoDeep` 则代表另一条线：用语言空间做 3D 开放词汇理解，把 VLM 当“翻译器”而非特征提取器，强调离散文本带来的可解释性。

#### 值得优先阅读的论文

1. **`3DPS` (3D Point Splatting for mmWave Radar NVS, 2609.11894)**
   优先理由：它是今日唯一明确“首个”定位的工作，且技术推导路径清晰（从雷达方程立体角形式直接推导可微点渲染器），复数输出使同一优化场景可通过 FFT 流水线产出 ADC、CRP、RA 多种格式，避免了按格式重训练。对雷达感知、物理渲染、复值神经表示三个方向都有交叉参考价值。建议重点验证其“单卡约 3 分钟/场景”是否在摘要之外有完整实验支撑。

2. **`Point4D` (Long-range 4D Motion Reconstruction, 2609.09145)**
   优先理由：直接针对 4D 重建公认的短窗口瓶颈，提出 3D 查询解耦与跨块重查询机制，且在 200 帧以上长视频追踪基准上取得领先。其“视觉描述符从任意可见帧提取优于仅用源 patch”的结论具有可迁移性，适合做长视频动态重建的基线或改进起点。

3. **`RoMa-$Ω$` (What Feed-Forward 3D Models Know About Image Matching, 2609.09507)**
   优先理由：它不是单纯提出一个匹配器，而是系统回答了“前馈

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-11T12:26:17-04:00
**Total number of papers:** 21
**Number of papers added in the latest update:** 8
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

#### 2026-09-10 - SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views

**Authors:** Langxu Zhao, Zuan Gu, Yingdan Zhang, Pengfei Zhao, Tianhan Gao
**Links:** [abs](https://arxiv.org/abs/2609.11279) - [pdf](https://arxiv.org/pdf/2609.11279)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** DUSt3R, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views
- 作者：Langxu Zhao, Zuan Gu, Yingdan Zhang, Pengfei Zhao, Tianhan Gao
- 出版日期：2026-09-10T09:12:48Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.11279 ；PDF https://arxiv.org/pdf/2609.11279

### 一句话总结
该论文提出端到端模型 SAMV-DUSt3R，将 SAM2 的 2D 掩码注入 MV-DUSt3R 重建流程，以在稀疏多视角下实现以实例为中心的三维场景解耦，并报告了重建精度与参考视图选择方面的提升。

### 研究问题
从三维场景中解耦物体（实例级分离）的需求日益增长，论文关注在稀疏多视角条件下实现实例级的三维场景解耦与重建。摘要指出其目标是在不依赖多阶段流水线的情况下完成物体级解耦，并同时提升形状精度与重建稳定性。

### 核心思路/方法
- 提出端到端模型 SAMV-DUSt3R，将 SAM2 的二维掩码注入到 MV-DUSt3R 的重建过程中。
- 设计 Cross Flow Mask Block，利用这些掩码引导网络朝向目标实例，从而联合提升形状精度并实现物体级解耦，且无需多阶段流水线。
- 为保证重建稳定性，引入轻量级 Spatial RankGNN 来选择最优参考视图，摘要给出选择准确率为 73.5%。

### 主要贡献
- 提出将 SAM2 二维掩码注入 MV-DUSt3R 重建的端到端方法，实现以实例为中心的三维场景解耦，避免多阶段流水线。
- 通过 Cross Flow Mask Block 引导网络关注目标实例，联合改善形状精度并实现物体级解耦。
- 引入轻量级 Spatial RankGNN 进行最优参考视图选择，报告选择准确率为 73.5%。
- 摘要称大量实验表明，与最先进基线相比，该方法在多种指标上平均重建精度提升 11%，并展现出较强的实例解耦能力，对驾驶、机器人、AR/VR 和遗产数字化具有明显益处。

### 局限性
- 摘要未提供足够信息说明实验数据集、评价指标细节、对比基线的具体配置以及消融实验设置。
- 摘要未提供足够信息说明方法在不同稀疏视角数量、遮挡、动态场景或类别分布下的失效条件与适用范围。
- 摘要未提供足够信息说明 Spatial RankGNN 选择错误时对重建结果的影响程度，以及 Cross Flow Mask Block 对 SAM2 掩码质量的依赖与鲁棒性。
- 摘要未提供足够信息说明计算开销、推理速度、模型规模与训练数据需求。

### 阅读优先级
高。理由：该论文聚焦稀疏多视角下的实例级三维场景解耦，提出端到端注入 2D 掩码与参考视图选择的组合方案，并在摘要中报告了明确的重建精度提升与选择准确率；主题同时关联几何基础模型与具身/机器人/AR 应用，对三维重建与实例解耦方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

With the rising demand to decouple objects from 3D scenes, we propose SAMV-DUSt3R, an end-to-end model that injects SAM2 2D masks into MV-DUSt3R reconstruction. A Cross Flow Mask Block uses these masks to steer the network toward the target instance, jointly improving shape accuracy and achieving object-level disentanglement without multi-stage pipelines. To ensure reconstruction stability, a lightweight Spatial RankGNN selects the optimal reference view with a selection accuracy of 73.5\%. Extensive experiments demonstrate that our method boosts average reconstruction precision by 11\% across various metrics compared to state-of-the-art baselines. These results reveal a strong instance-disentanglement capability and clear benefits for driving, robotics, AR/VR, and heritage digitisation.

</details>

#### 2026-09-08 - RoMa-$Ω$: What Feed-Forward 3D Models Know About Image Matching

**Authors:** David Nordström, Xinyue Zhang, Thibaut Loiseau, Vincent Lepetit, Fredrik Kahl
**Links:** [abs](https://arxiv.org/abs/2609.09507) - [pdf](https://arxiv.org/pdf/2609.09507)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, MASt3R, feed-forward reconstruction, image matching

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoMa-$Ω$: What Feed-Forward 3D Models Know About Image Matching
- 作者：David Nordström, Xinyue Zhang, Thibaut Loiseau, Vincent Lepetit, Fredrik Kahl
- 出版日期：2026-09-08T22:50:46Z
- 分类：Geometry Foundation Models（主）；3D Reconstruction & Multi-view Geometry（次）
- 链接：[摘要页](https://arxiv.org/abs/2609.09507)｜[PDF](https://arxiv.org/pdf/2609.09507)

### 一句话总结
该工作系统分析了前馈式三维重建模型在图像匹配任务中的表征能力，并基于分析结论用 VGGT-$Ω$ 替换 RoMa v2 的 DINO 骨干，得到在多个基准上超越当前先进匹配器的 RoMa-$Ω$。

### 研究问题
匹配器（如 RoMa，其鲁棒性常被归因于冻结的 DINO 特征）与前馈式重建模型（如 VGGT，在大规模数据上训练以回归稠密三维点图与相机位姿）之间的界限因 MASt3R、VGGT-$Ω$ 等引入匹配损失而日益模糊。作者据此提出核心问题：前馈式三维模型究竟“知道”多少关于图像匹配的信息？

### 核心思路/方法
论文通过三种场景来分析前馈式三维模型在匹配方面的能力：
1. patch 特征的零样本匹配；
2. 三维点预测的直接匹配；
3. 在学习到的表征之上训练完整匹配器。

基于上述分析结论，作者以 VGGT-$Ω$ 替换 RoMa v2 的 DINO 骨干，重新训练得到模型 RoMa-$Ω$。

### 主要贡献
- 给出对前馈式三维重建模型匹配能力的系统分析，覆盖零样本 patch 特征匹配、三维点预测直接匹配、以及在其表征上训练完整匹配器三种场景。
- 发现：前馈式重建模型在零样本匹配（尤其在较深层）表现不佳，但其表征对线性探测与完整匹配流程具有很强的可用性。
- 发现：即使不经过任何训练，其原始预测单独即可实现有竞争力的匹配，但仅在中等视角变化与模态差异条件下成立。
- 基于这些洞察重训 RoMa v2（替换骨干为 VGGT-$Ω$），所得 RoMa-$Ω$ 在广泛基准上超越当前先进匹配器，例如在 WxBS 上相较 RoMa v2 提升 +8.1 mAA。

### 局限性
- 摘要仅指出未训练的原始预测实现有竞争力匹配“仅在中等视角变化与模态差异下成立”，暗示其在更大视角变化或更大模态差异下的适用性受限。
- 具体的实验基准范围、失败案例、计算开销与训练成本等细节，摘要未提供足够信息。
- 分析所覆盖的前馈式三维模型种类、VGGT-$Ω$ 的具体结构与训练配置等，摘要未提供足够信息。

### 阅读优先级
中。理由：选题位于匹配与前馈式三维重建的交叉前沿，对理解“三维基础模型表征是否可用于匹配”这一开放问题有直接价值，且提出的 RoMa-$Ω$ 报告了明确的基准提升（如 WxBS +8.1 mAA）；但摘要未给出具体基准列表、消融与失败情形的细节，是否与自身研究方向强相关需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

Learned image matching has experienced significant progress in recent years, culminating in robust and accurate matchers such as RoMa, whose robustness is often attributed to its use of frozen DINO features. In a parallel development, feed-forward reconstruction models, such as VGGT, have been trained on ever-growing datasets to accurately regress dense 3D point maps and camera poses. The distinction between matchers and feed-forward reconstruction models has become increasingly blurred with the introduction of matching losses in models such as MASt3R and VGGT-$Ω$. This raises a natural question: what do feed-forward 3D models know about image matching? In this work, we answer this question by analyzing three scenarios: (i) zero-shot matching of patch features, (ii) direct matching of 3D point predictions, and (iii) training a full matcher on top of the learned representations. We find that, despite performing poorly in zero-shot matching, especially in later layers, feed-forward reconstruction models provide strong representations for linear probing and full matching pipelines. We further show that, even without any training, their raw predictions alone enable competitive matching, albeit only under moderate viewpoint changes and modality gaps. Based on these insights, we retrain RoMa v2 by replacing its DINO backbone with VGGT-$Ω$. Our resulting model, \ours, outperforms state-of-the-art matchers on a wide range of benchmarks, e.g. +8.1 mAA compared to RoMa v2 on WxBS.

</details>

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-08 - Point4D: Long-range 4D Motion Reconstruction

**Authors:** Minsik Jeon, Jay Karhade, Deva Ramanan, Shubham Tulsiani
**Links:** [abs](https://arxiv.org/abs/2609.09145) - [pdf](https://arxiv.org/pdf/2609.09145)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, motion reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Point4D: Long-range 4D Motion Reconstruction
- 作者：Minsik Jeon, Jay Karhade, Deva Ramanan, Shubham Tulsiani
- 出版日期：2026-09-08
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2609.09145

### 一句话总结
Point4D 提出了一种前馈式4D重建模型，能够对数百帧的长视频序列进行稠密的逐点3D轨迹推断，突破了现有方法仅能处理几十帧短窗口的限制。

### 研究问题
如何实现长视频序列（多百帧级别）的稠密4D运动重建，克服现有4D方法受限于短输入窗口（至多几十帧）的瓶颈。

### 核心思路/方法
- 核心创新是一种灵活的基于3D查询的运动解码器，将轨迹预测与图像平面可见性解耦。
- 预测得到的3D端点可以在下一个时间块中直接被重新查询，无需重新投影或特征匹配。
- 在提取视觉描述符时，不限于源patch，而是从任意可见该点的帧中提取并复用描述符，实验证明该方法优于仅依赖源patch的方案。

### 主要贡献
- 提出Point4D，一种面向长视频的前馈式4D重建模型，可处理跨数百帧的序列。
- 提出基于3D查询的运动解码器，实现轨迹预测与可见性解耦。
- 证明跨帧复用视觉描述符的有效性。
- 在多个跨度超过200帧的长视频追踪基准上达到最先进性能，显著优于此前的前馈4D方法。

### 局限性
摘要未提供足够信息。摘要中未讨论模型的计算复杂度、推理时间、对遮挡或快速运动场景的鲁棒性等潜在局限。

### 阅读优先级
**高**。理由：该工作直接解决了4D重建中长序列处理的公认瓶颈，提出了简洁而创新的解码机制，在多个长视频基准上取得领先结果，对动态场景理解和视频追踪方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

We introduce Point4D, a feed-forward model for 4D reconstruction of long-range video sequences. Point4D is able to reliably infer dense per-point 3D trajectories across multi-hundred-frame videos, unlike existing 4D methods that are limited to short input windows of at most a few dozen frames. A key innovation that enables this is our flexible 3D query-based motion decoder that decouples trajectory prediction from image-plane visibility. The predicted 3D endpoints are then directly re-queried in the next chunk without re-projection or matching. Furthermore, we show that extracting and reusing a visual descriptor from an arbitrary frame where the point is visible leads to better performance than relying solely on the source patch. Overall, Point4D achieves state-of-the-art performance across diverse long-video tracking benchmarks spanning over 200 frames and largely outperforms previous feed-forward 4D method. Project page: https://point-4d.github.io

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-10 - Visual-SLAM for the detection of hidden tomatoes in greenhouses by Hierarchical Localization and GLOMAPfor robotized harvesting

**Authors:** Fernando Cañadas-Aránega, José C. Moreno, José L. Blanco-Claraco, Francisco Rodríguez
**Links:** [abs](https://arxiv.org/abs/2609.11766) - [pdf](https://arxiv.org/pdf/2609.11766)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** structure from motion, SLAM, visual SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visual-SLAM for the detection of hidden tomatoes in greenhouses by Hierarchical Localization and GLOMAPfor robotized harvesting
- 作者：Fernando Cañadas-Aránega, José C. Moreno, José L. Blanco-Claraco, Francisco Rodríguez
- 出版日期：2026-09-10T16:19:36Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.11766 ；PDF https://arxiv.org/pdf/2609.11766

### 一句话总结
该工作提出一种面向温室番茄作物建图的低成本单目 Visual-SLAM 系统，结合 Hierarchical Localization 与基于 Structure-From-Motion 的 GLOMAP，实现对被遮挡番茄的识别与三维重建。

### 研究问题
温室内部先进的作物监测是研究中心的重点目标之一。传统上常使用 LiDAR 或立体相机等高性能传感器，但成本往往较高。论文关注的是：能否用成本显著更低的单目相机 Visual-SLAM 系统，面向农业应用（如温室番茄作物建图）完成检测与建图任务，尤其是识别被遮挡、经典视觉技术难以访问的番茄。

### 核心思路/方法
论文提出使用单目相机的 Visual-SLAM 系统，针对农业应用（温室番茄作物建图）定制。测试在 Agroconnect 实验温室的真实番茄串上进行。开发了一个 ROS 2 Humble 节点，运行在机器人上以采集作物图像，随后存储用于离线处理。为生成温室作物的三维建图模型，将基于 Structure-From-Motion 的 GLOMAP 建图器与 Hierarchical Localization 工具箱集成。系统采用基于由粗到细策略的分层定位范式：先进行全局检索以生成位置假设，再在识别出的候选区域内结合局部特征。

### 主要贡献
- 提出一种使用单目相机的 Visual-SLAM 系统，相比 LiDAR 或立体相机等方案成本显著更低，并面向农业应用定制。
- 将基于 Structure-From-Motion 的 GLOMAP 建图器与 Hierarchical Localization 工具箱集成，用于生成温室作物的三维建图模型。
- 采用由粗到细的分层定位范式：先全局检索生成位置假设，再在候选区域内结合局部特征。
- 开发 ROS 2 Humble 节点用于机器人端图像采集与离线处理。
- 结果显示能够正确识别番茄簇，并正确表征被经典视觉技术遮挡且不可访问的番茄。
- 重建的三维模型通过人工真值测量（果实大小、质心位置和朝向）进行了验证，确认了所提低成本单目流程的几何精度。

### 局限性
- 摘要未提供足够信息说明系统在更多温室场景、不同作物或更大规模环境中的泛化能力。
- 摘要未提供足够信息说明实时性能、计算资源消耗或在线运行能力。
- 摘要未提供足够信息说明与 LiDAR 或立体相机方案在精度、鲁棒性上的系统对比。
- 摘要未提供足够信息说明对光照变化、遮挡程度差异、相机运动等干扰因素的鲁棒性。
- 摘要未提供足够信息说明数据集规模、测试样本数量及统计显著性。
- 摘要仅提到该初始建图是未来更高级算法分析生长模式、优化农业管理的基础，因此面向机器人化采收的完整闭环能力在摘要中未提供足够信息。

### 阅读优先级
中。理由：该论文主题明确，聚焦低成本单目 Visual-SLAM 在温室番茄检测与三维重建中的应用，并涉及 Hierarchical Localization 与 GLOMAP 的集成，对农业机器人、三维重建和视觉定位方向有一定参考价值。但摘要未提供足够信息说明实验规模、实时性、泛化性和与高成本传感器的系统对比，若读者关注机器人化采收的完整系统或大规模验证，需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Advanced crop monitoring inside greenhouses is becoming one of the primary objectives of research centers. High-performance sensors, such as LiDAR or stereo cameras, have traditionally been employed for this purpose, though these often have a high cost. This work proposes a Visual-SLAM system using a monocular camera, which is significantly more cost-effective and specifically tailored for agricultural applications, such as mapping tomato crops in a greenhouse. Tests were carried out on a real tomato bunch, located in the Agroconnect experimental greenhouse. A ROS 2 Humble node was developed to run on the robot in order to capture images of these crops, which were then stored for offline processing. To generate a 3D mapped model for the crop in the greenhouse, the GLOMAP mapper, based on Structure-From-Motion, was integrated with the Hierarchical Localization toolbox. This initial mapping is a foundation for future, more advanced algorithms to analyze growth patterns, and optimize agricultural management. The system leverages a hierarchical localization paradigm based on a coarse-to-fine strategy: it first performs global retrieval to generate location hypotheses, then combines local features within the identified candidate regions. The results show a correct identification of the tomato cluster, correctly characterising the tomato that is occluded and inaccessible by classical vision technologies. The reconstructed 3D model was further validated against manual ground-truth measurements of fruit size, centroid position, and orientation, confirming the geometric accuracy of the proposed low-cost monocular pipeline.

</details>

#### 2026-09-10 - RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting

**Authors:** Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen
**Links:** [abs](https://arxiv.org/abs/2609.11079) - [pdf](https://arxiv.org/pdf/2609.11079)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, depth estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, robot perception, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting
- 作者：Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen
- 出版日期：2026-09-10T04:36:58Z
- 分类：3D Reconstruction & Multi-view Geometry（主类别）；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次类别）
- 链接：摘要页 https://arxiv.org/abs/2609.11079 ；PDF https://arxiv.org/pdf/2609.11079

### 一句话总结
RIDE 利用 render–match–PnP 重定位中获得的稀疏度量深度观测，结合预训练视频深度模型的几何先验，从机器人 RGB 流中估计稠密度量深度。

### 研究问题
论文关注的是：render–match–PnP 重定位虽能建立查询图像像素与 3D 地图点之间的对应关系以恢复相机位姿，但其支持稠密深度估计的潜力常被忽视。RIDE 旨在利用这类几何信息，在给定度量尺度的 3D Gaussian Splatting（3DGS）模型条件下，从机器人 RGB 流中估计稠密度量深度。

### 核心思路/方法
- 以度量尺度的 3DGS 模型为基础，利用 PnP-RANSAC 内点对应关系导出稀疏度量深度观测。
- 将这些稀疏度量深度观测与预训练视频深度模型的几何先验相结合。
- 针对观测不均匀和间歇性的问题，引入全局与局部深度校正以及时间记忆机制。
- 在度量尺度初始化后，支持在短观测间隔内继续进行深度估计。
- 在公开 RGB-D 视频上训练，并在机器人序列上不做微调进行评估。

### 主要贡献
- 提出 RIDE，将重定位几何信息用于稠密度量深度估计。
- 结合 PnP-RANSAC 内点对应得到的稀疏度量深度与预训练视频深度模型的几何先验。
- 通过全局/局部深度校正与时间记忆，应对不均匀、间歇的稀疏观测，并支持短观测间隔下的深度估计。
- 实验显示，相比仅做尺度校准，RIDE 在深度精度和时间一致性上有所提升，表明定位几何可同时支持位姿恢复与稠密机器人感知。

### 局限性
摘要未提供足够信息。摘要未给出具体实验平台、序列数量、失败情形、计算开销、实时性、对 3DGS 模型质量或重定位成功率的依赖程度等细节。

### 阅读优先级
中。理由：该工作位于 3D 重建、神经场景表示与机器人/AR 应用的交叉点，核心思路明确，且强调无需微调即可在机器人序列上评估；但摘要未提供充分的实验细节与对比设置，是否值得精读取决于读者对重定位辅助稠密深度估计、3DGS 机器人感知这一具体方向的关注程度。

</details>

<details>
<summary>Abstract</summary>

Render--match--PnP relocalization establishes correspondences between query image pixels and 3D map points for camera pose recovery, but their potential to support dense depth estimation is often overlooked. To exploit this geometric information, we present RIDE, which estimates dense metric depth from a robot's RGB stream. Given a metrically scaled 3D Gaussian Splatting (3DGS) model, RIDE combines sparse metric depth observations derived from PnP-RANSAC inlier correspondences with the geometric prior of a pretrained video-depth model. To handle uneven and intermittent observations, it integrates global and local depth correction with temporal memory, supporting depth estimation through short observation gaps after metric scale initialization. Trained on public RGB-D videos, RIDE is evaluated on robot sequences without fine tuning. Experiments show improved depth accuracy and temporal consistency over scale-only calibration, demonstrating how localization geometry can support both pose recovery and dense robot perception.

</details>

#### 2026-09-09 - GRADE: Single-Frame Generative Radar Depth Estimation Under Visual Degradation

**Authors:** Bin Zhao, Patrick Chiou, Nakul Garg
**Links:** [abs](https://arxiv.org/abs/2609.10756) - [pdf](https://arxiv.org/pdf/2609.10756)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GRADE: Single-Frame Generative Radar Depth Estimation Under Visual Degradation
- 作者：Bin Zhao, Patrick Chiou, Nakul Garg
- 出版日期：2026-09-09T18:57:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.10756

### 一句话总结
GRADE 将预训练生成先验与单帧雷达几何相融合，在烟雾、雾气和黑暗等视觉退化条件下实现高保真度量深度估计。

### 研究问题
在烟雾、雾气和黑暗等条件下，光学传感器无法穿透空气中的颗粒物，导致密集 3D 深度感知失效。毫米波雷达在这些条件下仍可使用并能准确测距，但其小孔径限制了角分辨率。论文旨在解决：如何在视觉退化条件下，利用单帧雷达几何与生成先验估计高保真度量深度。

### 核心思路/方法
GRADE 首先将原始 4D 雷达频谱映射为粗略的度量深度。随后，一个潜在扩散骨干网络在恢复结构细节的同时，将每个去噪步骤都条件化在该深度估计上。一个像素空间适配器在有可用信息时利用残余相机线索，并在清晰、烟雾退化和遮挡输入上进行训练，使得随着能见度下降，整体输出趋近于雷达条件化路径。

### 主要贡献
- 提出 GRADE，将预训练生成先验锚定在单帧雷达几何中，用于估计高保真度量深度。
- 设计了两阶段方法：先将原始 4D 雷达频谱映射为粗略度量深度，再通过潜在扩散骨干网络恢复结构细节并条件化每一去噪步骤。
- 引入像素空间适配器，利用残余相机线索，并在清晰、烟雾退化和遮挡输入上训练，使输出随能见度下降趋近雷达条件化路径。
- 在 12 栋建筑约 95K 帧（含真实烟雾）上训练与评估，清晰场景 MAE 为 0.303 m，烟雾下为 0.313 m，优于现有基线。
- 代码与数据集已公开。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对视觉退化条件下的深度感知这一明确难题，结合雷达与生成先验，给出了具体量化结果，且涉及 3D 重建与多视角几何方向，摘要信息显示其方法路径与评估结果较为完整，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Dense 3D depth perception fails under smoke, fog, and darkness because optical sensors cannot penetrate airborne particulates. mmWave radar remains usable and measures range accurately under these conditions, but its small aperture limits angular resolution. We present GRADE, which grounds a pretrained generative prior in single-frame radar geometry to estimate high-fidelity metric depth. GRADE first maps raw 4D radar spectra to coarse metric depth. A latent diffusion backbone then recovers structural detail while conditioning every denoising step on this estimate. A pixel-space adapter uses residual camera cues when available and is trained across clear, smoke-degraded, and occluded inputs so the full output approaches the radar-conditioned path as visibility degrades. Trained and evaluated on ~95K frames across 12 buildings with real smoke, GRADE achieves an MAE of 0.303 m in clear scenes and 0.313 m under smoke, outperforming existing baselines. Code and datasets are available at https://phi-lab-rice.github.io/GRADE.

</details>

#### 2026-09-09 - Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts

**Authors:** Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte
**Links:** [abs](https://arxiv.org/abs/2609.10498) - [pdf](https://arxiv.org/pdf/2609.10498)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts
- 作者：Simon Khan, Laurent Gajny, Jennyfer Lecompte, Sébastien Laporte
- 出版日期：2026-09-09T17:35:16Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.10498) / [PDF](https://arxiv.org/pdf/2609.10498)

### 一句话总结
该论文提出 Field Converter，通过相机与球场几何初始化球员根节点，并利用时序残差修正，实现从已标定足球转播中估计共享世界坐标系下的 3D 球员姿态。

### 研究问题
从单目体育转播中恢复 3D 人体姿态时，难点不仅在于相对自身身体的姿态重建，还在于需要将球员定位到共享的度量世界坐标系中。论文聚焦于从已标定的足球转播视频中进行世界坐标下的 3D 球员姿态估计。

### 核心思路/方法
- 使用相机和球场几何信息，通过射线-地面相交来初始化球员根节点。
- 在几何初始化基础上，预测时序残差修正。
- 残差预测使用姿态、图像、相机和几何线索。
- 在匹配不重叠的评估序列上，比较了不同时序骨干：逐帧 MLP、TCN 和 Transformer。

### 主要贡献
- 提出 Field Converter，一个几何初始化与时序残差修正结合的世界坐标 3D 球员姿态估计框架。
- 利用相机和球场几何进行根节点初始化，并通过时序残差修正降低根节点误差。
- 报告中，几何单独使根误差为 49cm，逐帧 MLP 降至 14cm，TCN 降至 10cm，Transformer 达到可比的 11cm；世界空间 MPJPE 达到 13.2cm。
- 消融显示，残差预测明显优于直接全局根节点回归；时序上下文比具体时序骨干更重要。
- 失败分析指出，空中动作是基于地面几何初始化的主要局限。

### 局限性
- 摘要明确指出失败分析发现空中动作是基于地面几何初始化的主要限制。
- 除空中动作外，其他局限性摘要未提供足够信息。
- 实验细节、数据集规模、跨场景泛化能力、计算成本等信息摘要未提供足够信息。

### 阅读优先级
中。理由：该论文针对足球转播中的世界坐标 3D 人体姿态估计，问题设定明确，且给出了根误差、MPJPE 和消融结论；如果关注体育视频分析、单目 3D 人体姿态或几何初始化方法，具有参考价值。但摘要未提供完整实验设置、数据规模和更广泛的泛化分析，是否高优先级取决于读者对足球转播场景的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Recovering 3D human pose from monocular sports broadcasts remains challenging when players must be localized in a shared metric world coordinate system rather than only reconstructed relative to their own body. We introduce Field Converter, a geometry-initialized temporal residual framework for world-grounded 3D player pose estimation from calibrated soccer broadcasts. Our method first uses camera and pitch geometry to initialize the player root through ray-ground intersection, then predicts a temporal residual correction from pose, image, camera, and geometric cues. On match-disjoint evaluation sequences, residual refinement reduces root error from 49cm with geometry alone to 14cm with a frame-wise MLP and 10cm with a TCN, while a Transformer achieves a comparable 11cm. The resulting world-space MPJPE reaches 13.2cm, and ablations show that residual prediction clearly outperforms direct global-root regression while temporal context matters more than the specific temporal backbone. Failure analysis further identifies airborne motion as the main limitation of the ground-based geometric initialization.

</details>

#### 2026-09-08 - Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion

**Authors:** Fadi Khatib, Meirav Galun, Ronen Basri
**Links:** [abs](https://arxiv.org/abs/2609.09491) - [pdf](https://arxiv.org/pdf/2609.09491)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, structure from motion, camera pose estimation, pose estimation, bundle adjustment, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion
- 作者：Fadi Khatib, Meirav Galun, Ronen Basri
- 出版日期：2026-09-08T22:14:03Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.09491

### 一句话总结
本文提出了一种基于可学习视图图聚合的深度全局 Structure-from-Motion 框架，用置换等变、边条件图神经网络从带噪相对位姿回归全局一致的相机外参。

### 研究问题
相机位姿估计是三维重建与视图合成流程中的关键步骤。论文关注如何从带噪声的视图图（view-graph）中学习全局相机位姿，以提升结构从运动（Structure from Motion）中位姿估计的精度、鲁棒性和效率。

### 核心思路/方法
方法核心是学习视图图聚合的深度、全局 Structure-from-Motion 框架：
- 使用置换等变、边条件图神经网络；
- 输入为带噪声的成对相对位姿；
- 输出为全局一致的相机外参；
- 训练不依赖真值监督，仅使用相对位姿一致性目标；
- 后续接三维点三角化和鲁棒 bundle adjustment。

### 主要贡献
- 提出基于学习视图图聚合的深度全局 Structure-from-Motion 框架。
- 设计置换等变、边条件图神经网络，从带噪相对位姿输出全局一致的相机外参。
- 无需真值监督，仅依赖相对位姿一致性目标进行训练。
- 方法高效、可扩展到超过一千张图像，并且对图密度鲁棒。
- 在 MegaDepth、1DSfM、Strecha 和 BlendedMVS 上评估，显示在旋转和平移精度上优于以深度轨迹为中心的方法，同时在许多场景中注册更多图像；与最先进的经典流程相比具有竞争力且速度更快。

### 局限性
摘要未提供足够信息。摘要未说明方法在何种场景或数据条件下会失败，未给出计算复杂度、内存占用、超参数敏感性、对极端噪声或异常值的具体限制，也未提供与经典流程比较的完整实验细节。

### 阅读优先级
高。理由：该论文直接面向三维重建与多视图几何中的核心问题，提出结合图神经网络与全局 Structure-from-Motion 的方法，并声称在多个标准数据集上取得精度、鲁棒性和速度优势；若研究兴趣涉及 SfM、相机位姿估计或图神经网络在三维视觉中的应用，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera pose estimation is a key step in 3D reconstruction and view-synthesis pipelines. We present a deep, global Structure-from-Motion framework based on learned view-graph aggregation. Our method employs a permutation-equivariant, edge-conditioned graph neural network that takes noisy pairwise relative poses as input and outputs globally consistent camera extrinsics. The network is trained without ground-truth supervision, relying solely on a relative-pose consistency objective. This is followed by 3D point triangulation and robust bundle adjustment. Our approach is efficient, scalable to more than a thousand images, and robust to graph density. We evaluate our method on MegaDepth, 1DSfM, Strecha, and BlendedMVS. These experiments demonstrate that our method achieves superior rotation and translation accuracy compared to deep track-centric methods while registering more images across many scenes, and competitive results compared to state-of-the-art classical pipelines, while being much faster.

</details>

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-10 - 3D Point Splatting for mmWave Radar Novel View Synthesis

**Authors:** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar
**Links:** [abs](https://arxiv.org/abs/2609.11894) - [pdf](https://arxiv.org/pdf/2609.11894)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D Point Splatting for mmWave Radar Novel View Synthesis
- 作者：Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar
- 出版日期：2026-09-10T17:52:17Z
- 分类：Neural Scene Representations & Rendering（主分类）；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2609.11894 ；PDF https://arxiv.org/pdf/2609.11894

### 一句话总结
论文提出 3DPS——首个面向毫米波雷达的可微点渲染器，直接从雷达方程立体角形式推导，以复数相位输出实现与格式无关的新视角合成，在保持物理保真度的同时将训练时间压缩到单卡约 3 分钟/场景。

### 研究问题
毫米波雷达新视角合成（NVS）需要一个同时满足三个性质的渲染器：物理忠实、复数值、多视角可优化。摘要指出此前没有方法能同时具备这三点：
- 可微蒙特卡洛（MC）光线追踪器直接实现雷达前向模型，具有显式材质建模和复数输出，但无法扩展到 NVS 所需的多视角优化规模；
- 从光学 NVS 移植的 NeRF、哈希网格和 3D 高斯训练快，但丢弃了相位，并以不透明的学习特征替代显式材质建模，因此只限于功率域的距离-方位（RA）幅度。

### 核心思路/方法
- 从雷达方程的标准立体角形式直接推导出可微点渲染器 3DPS。
- 每个有向 3D 点携带 ITU-R P.2040 材质模型，并以闭式求值。
- 将得到的复数相量通过预计算的点扩散函数（PSF）splat 到距离单元中。
- 复数输出使渲染器与下游输出格式无关：同一个优化后的场景可通过标准 FFT 流水线产出 ADC、复数距离剖面（CRP）和 RA 输出，无需针对每种格式重新训练。

### 主要贡献
- 提出 3DPS，据摘要所述为首个面向雷达的可微点渲染器。
- 从雷达方程立体角形式直接推导，赋予渲染器物理忠实性。
- 通过 ITU-R P.2040 材质模型与闭式复数相量计算，兼顾显式材质建模与复数输出。
- 借助复数输出实现格式无关性，一套优化场景即可支持 ADC、CRP、RA 多种输出。
- 在六个户外 ColoRadar 场景上，持出 RA 图像达到 0.587 的平均皮尔逊相关，为三个光学 NVS 基线（RadarSplat、Radar Fields、DART）的 1.7 倍至 5.2 倍；单张 RTX 4090 上每场景训练约 3 分钟。

### 局限性
- 摘要未提供足够信息说明方法在非户外场景、其他雷达频段或不同硬件条件下的泛化表现。
- 摘要未提供足够信息说明 3DPS 在 ADC、CRP 输出上的定量评估结果，仅给出 RA 图像的皮尔逊相关指标。
- 摘要未提供足够信息说明与 MC 光线追踪器在物理保真度上的直接定量对比。
- 摘要未提供足够信息说明多视角优化中视角数量、稀疏度或场景规模对性能的影响。
- 摘要未提供足够信息说明 0.587 平均皮尔逊相关的方差、逐场景分布或失败案例。
- 摘要未提供足够信息说明材质模型参数是否可学习、初始化方式或对 ITU-R P.2040 假设的敏感性。

### 阅读优先级
中。理由：雷达 NVS 属于相对专门的方向，但该工作提出的“物理忠实 + 复数 + 多视角可训练”三性合一问题定位清晰，且报告了显著的相对基线提升与极短训练时间；若关注可微渲染、雷达感知或 NeRF/3D 高斯之外的非光学传感器 NVS，则值得优先阅读。由于摘要未给出代码、完整实验设置与 ADC/CRP 定量结果，是否精读可待正文确认。

</details>

<details>
<summary>Abstract</summary>

Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-view optimization NVS demands. Optical-NVS ports of NeRF, hash grids, and 3D Gaussians train fast but discard phase and replace explicit material modeling with opaque learned features, restricting them to power-only range-azimuth (RA) magnitudes. We propose 3D Point Splatting (3DPS), the first differentiable point renderer for radar, derived directly from the standard solid-angle form of the radar equation. Each oriented 3D point carries an ITU-R P.2040 material model, evaluated in closed form, with the resulting complex phasor splatted into range bins through a precomputed point spread function (PSF). The complex-valued output makes the renderer product-agnostic. The same optimized scene yields analog-to-digital converter (ADC), complex range profile (CRP), and RA outputs through standard fast Fourier transform (FFT) pipelines without retraining for each format. On six outdoor ColoRadar scenes, 3DPS reaches 0.587 mean Pearson correlation on held-out RA images. This is between 1.7x and 5.2x the three optical-NVS baselines (RadarSplat, Radar Fields, DART). Training takes approximately 3 minutes per scene on a single RTX 4090.

</details>

#### 2026-09-10 - Hologram Representation via Quadratic Phase Gaussian Splatting

**Authors:** Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu
**Links:** [abs](https://arxiv.org/abs/2609.11434) - [pdf](https://arxiv.org/pdf/2609.11434)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hologram Representation via Quadratic Phase Gaussian Splatting
- 作者：Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu
- 出版日期：2026-09-10T12:06:11Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.11434) / [PDF](https://arxiv.org/pdf/2609.11434)

### 一句话总结
该论文提出复数域二次相位高斯（CVQPG），用可学习的二维二次相位函数替代 2D Gaussian Splatting 中的标准二维高斯表示，以提升全息重建的视觉质量。

### 研究问题
如何改进全息图表示方法，使其在重建质量上优于现有先进方法，同时保持参数高效。摘要指出，作者希望验证“调制基元的波前”是否是一种有效且轻量的全息表示增强方式。

### 核心思路/方法
- 提出 Complex-Valued Quadratic Phase Gaussian (CVQPG)。
- 将 2D Gaussian Splatting 中使用的标准二维高斯表示替换为二维二次相位函数。
- 引入额外可学习参数，用于控制这些基元的曲率。
- 通过等参数数量评估，比较该方法与现有先进方法在全息重建中的表现。
- 进行频域分析，观察自然图像中高频与中高频段的保留情况。

### 主要贡献
- 提出 CVQPG，一种新的全息图表示方法，核心是用二维二次相位函数替代标准二维高斯基元。
- 在等参数数量评估中，表明调制基元波前可作为全息表示的有效且轻量增强。
- 在全息重建视觉质量上平均超过现有先进方法：RGB 提升 +0.19 dB，灰度提升 +0.33 dB。
- 频域分析显示，CVQPG 成功保留了自然图像的中高频段。

### 局限性
摘要未提供足够信息。未说明计算开销、训练时间、数据集规模、泛化能力、硬件依赖性、失败案例或与其他表示方法的全面比较。等参数数量评估之外的其他实验设置也未在摘要中给出。

### 阅读优先级
中。理由：该工作与神经场景表示、Gaussian Splatting 和全息显示相关，提出的二次相位基元替代思路较直接，且摘要给出了明确的定量提升和频域分析；但摘要未披露数据集、实现细节和完整实验设置，是否具有广泛适用性需阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

We introduce Complex-Valued Quadratic Phase Gaussian (CVQPG), a novel hologram representation method that replaces standard 2D Gaussian representations used in 2D Gaussian Splatting with 2D quadratic phase functions. CVQPG incorporates additional learnable parameters to control the curvature of these bases. We evaluate our approach against state-of-the-art methods, exceeding the visual quality by +0.19 dB (RGB) and +0.33 dB (grayscale) on average in holographic reconstructions. Specifically, our equal parameter count evaluations show that modulating the primitive's wavefront is an effective and lightweight enhancement for hologram representations. In addition, our frequency domain analysis illustrates that CVQPG has successfully preserved the mid-to-high frequency band of natural images.

</details>

#### 2026-09-10 - Tri-DehazeGS: Scene--Medium Decoupled Gaussian Splatting with Transmittance-Aware Optimization

**Authors:** Kui Jiang, Yang Gu, Jiacheng Liu, Shiyu Liu, Youyu Chen, Hui Liu
**Links:** [abs](https://arxiv.org/abs/2609.11223) - [pdf](https://arxiv.org/pdf/2609.11223)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tri-DehazeGS: Scene--Medium Decoupled Gaussian Splatting with Transmittance-Aware Optimization
- 作者：Kui Jiang, Yang Gu, Jiacheng Liu, Shiyu Liu, Youyu Chen, Hui Liu
- 出版日期：2026-09-10T08:24:16Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.11223

### 一句话总结
Tri-DehazeGS 提出一种场景—介质解耦的高斯泼溅框架，用独立视图共享三平面场建模参与介质，并通过透射率梯度补偿优化低透射区域，以改善雾天多视角图像下的干净新视角重建。

### 研究问题
从有雾多视角图像中恢复干净三维场景具有挑战性，因为雾会衰减场景辐射并引入大气散射。现有散射感知高斯泼溅方法虽引入物理雾模型，但常在图像空间施加退化，或把介质相关变量绑定到高斯基元上，导致干净场景辐射与大气效应相互纠缠；同时低透射率区域对高斯优化提供的监督较弱，使远处或浓雾区域重建不足。

### 核心思路/方法
论文认为雾下干净重建需要同时实现场景—介质解耦与透射率感知的优化重平衡。为此提出 Tri-DehazeGS：
- 用高斯基元表示干净场景；
- 用独立的视图共享三平面场建模参与介质；
- 通过物理散射模型合成有雾观测。
此外引入 Medium-Decoupled Transmittance Gradient Compensation（MD-TGC），在介质冻结后补偿被雾抑制的梯度，且不改变前向渲染。

### 主要贡献
- 提出 Tri-DehazeGS，一个场景—介质解耦的高斯泼溅框架，将干净场景与参与介质分别表示并依据物理散射模型组合。
- 引入 MD-TGC，在介质冻结后补偿雾抑制的梯度，以重平衡低透射率区域的优化。
- 在真实与合成雾基准上实验显示，Tri-DehazeGS 改善了干净新视角重建，并提供代码链接。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算开销、对极端天气或动态场景的适用性，也未给出定量指标、消融细节或与基线方法的完整对比。

### 阅读优先级
高。理由：该论文针对雾天三维重建中场景与介质纠缠、低透射率区域监督不足两个明确问题，提出解耦表示与梯度补偿机制，属于神经场景表示与渲染方向中物理模型与高斯泼溅结合的前沿工作，且提供代码，便于复现与后续研究。

</details>

<details>
<summary>Abstract</summary>

Recovering clean 3D scenes from hazy multi-view images is challenging because haze attenuates scene radiance and introduces atmospheric scattering. Recent scattering-aware Gaussian Splatting methods introduce physical haze models into reconstruction, but they often apply degradation in image space or bind medium-related variables to Gaussian primitives, which can entangle clean scene radiance with atmospheric effects. Moreover, low-transmittance regions provide weakened supervision for Gaussian optimization, causing distant or dense-haze areas to be under-reconstructed. We argue that clean reconstruction under haze requires both scene--medium disentanglement and transmittance-aware optimization rebalancing. To this end, we propose Tri-DehazeGS, a scene--medium decoupled Gaussian Splatting framework. It represents the clean scene with Gaussian primitives, models the participating medium using an independent view-shared tri-plane field, and composes hazy observations through a physical scattering model. We further introduce Medium-Decoupled Transmittance Gradient Compensation (MD-TGC), which compensates haze-suppressed gradients after medium freezing without altering forward rendering. Experiments on real and synthetic haze benchmarks show that Tri-DehazeGS improves clean novel-view reconstruction. Code is available at https://github.com/aptx46/Tri-DehazeGS.

</details>

#### 2026-09-09 - View-Structured Conformal Prediction for 3D Gaussian Splatting

**Authors:** Junzheng Chu, Bin Pan, Zhenwei Shi
**Links:** [abs](https://arxiv.org/abs/2609.10307) - [pdf](https://arxiv.org/pdf/2609.10307)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：View-Structured Conformal Prediction for 3D Gaussian Splatting
- 作者：Junzheng Chu, Bin Pan, Zhenwei Shi
- 出版日期：2026-09-09T15:16:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.10307 ；PDF https://arxiv.org/pdf/2609.10307

### 一句话总结
论文提出视图结构化的共形预测方法 VSCP，将新视图合成的 RGB 预测框覆盖率问题建模为结构化回归，通过把预校准尺度分解为空间形状与可迁移的视图难度因子，在跨场景迁移下实现有限样本有效的视图级覆盖率保证。

### 研究问题
3D Gaussian Splatting 能实时渲染新视图，但仅给出不确定性热图并不能证明渲染视图满足特定预测覆盖率。论文要求：以至少 \(1-\alpha\) 的概率，RGB 预测框覆盖新视图中至少 \(1-\beta\) 比例的像素。摘要指出，按像素汇总校准在 90% 目标下像素级边际覆盖可达 89.9%，但视图事件覆盖率仅 61.4%，说明需要视图级有效的校准方法。

### 核心思路/方法
论文将新视图合成视为结构化回归，并提出 View-Structured Conformal Prediction（VSCP）。方法把预校准尺度拆分为两部分：来自渲染器的空间形状，以及可迁移的视图难度因子，后者用于预测该形状所需的最小视图级乘数。随后在视图上使用留出分位数（View-CP），即使在迁移到新场景时也能提供有限样本有效性。同一分解还使分析精确化：一致性分数是 oracle 视图难度与预测视图难度的比值，超额宽度可分解为测试侧项和校准侧项。

### 主要贡献
- 提出 VSCP，将新视图合成建模为结构化回归，并给出视图级覆盖的共形预测框架。
- 通过空间形状与可迁移视图难度因子的分解，结合视图上的留出分位数，实现跨新场景迁移时的有限样本有效性。
- 给出精确分析：一致性分数为 oracle 与预测视图难度之比，超额宽度分解为测试侧与校准侧两项。
- 在 13 个真实场景中，View-CP 达到 91.7–92.0% 视图事件覆盖率，而像素汇总校准仅 61.4%（90% 目标下）。
- 在匹配覆盖率下，VSCP 相对常数尺度将宽度减少 22.1%，并以每场景单模型、每次查询四次光栅化匹配十模型集成 21.0% 的宽度缩减；相对最接近的单模型基线 3DGS-U 提升 4.7 个点（\(p=0.0225\)）。
- 视图预测器可从有界源族迁移到全部九个无界 Mip-NeRF 360 场景；完整尺度在全部九个场景上相对常数尺度节省 20.7% 宽度，在不同稠密化骨干下仍保持 18.3% 节省，并在 RTX 4090 上以 216–280 FPS 运行。

### 局限性
摘要未提供足够信息说明方法在更广泛数据集、不同 \(\alpha\) 与 \(\beta\) 组合、极端场景或计算资源受限条件下的表现；摘要未提供足够信息说明其失败情形或与更多基线方法的全面比较。摘要未提供足够信息说明理论假设的完整边界与潜在违反条件。

### 阅读优先级
高。理由：该论文针对 3DGS 新视图合成中的不确定性认证问题提出视图级共形预测方法，直接回应像素级校准与视图级覆盖之间的差距；摘要给出了明确的覆盖率目标、跨场景迁移结果、宽度缩减、与基线比较、运行速度以及不同骨干下的表现，问题重要且结果信息量较大，适合优先阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) renders novel views in real time, but an uncertainty heatmap does not certify that a rendered view meets a certain prediction coverage. We treat novel-view synthesis as structured regression and ask that, with probability at least $1-α$, RGB prediction boxes cover at least a $1-β$ fraction of pixels in a new view. We propose View-Structured Conformal Prediction (VSCP). It splits the pre-calibration scale into a spatial shape from the renderer and a transferable view-difficulty factor, which predicts the smallest view-wise multiplier that shape needs. A held-out quantile over views (View-CP) then gives finite-sample validity even when transferring to new scenes. The same factorization makes the analysis exact: a conformity score is the ratio of oracle to predicted view difficulty, and excess width separates into a test-side and a calibration-side term. Across 13 real scenes, pixel-pooled calibration reaches 89.9\% marginal pixel coverage but only 61.4\% view-event coverage at a 90\% target, while View-CP reaches 91.7--92.0\%. At matched coverage VSCP cuts width by 22.1\% against a constant scale, and matches a ten-model ensemble's 21.0\% reduction using only one model per scene and four rather than ten rasterization passes per query. VSCP also improves on the closest single-model baseline, the 3DGS-U field, by 4.7 points ($p=0.0225$). The view predictor transfers from bounded source families to all nine unbounded Mip-NeRF~360 scenes. There the full scale beats the constant scale with 20.7\% width saving on all nine scenes. It also keeps an 18.3\% saving under a different densification backbone and runs at 216--280 FPS on an RTX~4090.

</details>

#### 2026-09-09 - LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting

**Authors:** Donghun Ryu, Minhyeok Lee
**Links:** [abs](https://arxiv.org/abs/2609.10095) - [pdf](https://arxiv.org/pdf/2609.10095)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting
- 作者：Donghun Ryu, Minhyeok Lee
- 出版日期：2026-09-09T12:19:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.10095) / [PDF](https://arxiv.org/pdf/2609.10095)

### 一句话总结
论文指出已有学习掩码剪枝方法因 Gumbel-Sigmoid 激活过陡而在掩码训练窗口内过早形成双峰分布、破坏重要性排序，提出用线性增量激活替代，使掩码保持中间置信区间并形成稳定单峰分布，从而实现更紧凑的 3D Gaussian Splatting。

### 研究问题
3D Gaussian Splatting（3DGS）虽支持实时新视角合成，但通过自适应致密化会产生数百万个基元，带来显著存储开销。已有学习掩码剪枝方法（如 LP-3DGS）为每个 Gaussian 分配可学习掩码以识别并剪除冗余基元，但论文识别出该范式的局限：Gumbel-Sigmoid 激活的陡峭斜率会在较短的掩码训练窗口内把掩码值推向极端，此时重要性排序尚未稳定，从而产生尖锐的双峰分布，导致排序无法再被可靠恢复。

### 核心思路/方法
提出 LinearMask-GS，用线性增量激活（linear increment activation）替代 Gumbel-Sigmoid。该激活在整个掩码训练过程中将掩码值保持在“中等置信度”区间，产生稳定、单峰的掩码分布，使掩码排序能够跟踪重要性。

### 主要贡献
- 识别并指出现有学习掩码剪枝（Gumbel-Sigmoid 范式）的关键局限：掩码训练窗口内过早双峰化，重要性排序不稳定。
- 提出 LinearMask-GS，以线性增量激活替代 Gumbel-Sigmoid，获得稳定单峰掩码分布。
- 在 Mip-NeRF 360 上，相比 3DGS 实现 3.6 倍、相比 LP-3DGS 实现 1.6 倍的 Gaussian 数量缩减，同时保持或提升渲染质量。
- 在户外场景实现 1.6 倍缩减（从 2.18M 到 1.36M），并在 PSNR（+0.38 dB）、SSIM（+0.025）、LPIPS（-0.029）上有明显提升。

### 局限性
摘要未提供足够信息。摘要中未说明方法在室内场景、其他数据集或不同压缩率下的表现，也未讨论线性增量激活是否需要额外的超参数调优、训练成本变化或与其他剪枝范式的兼容性。

### 阅读优先级
中。理由：论文针对 3DGS 存储开销这一明确痛点，指出现有掩码剪枝范式的具体机制缺陷并提出简洁替代方案，报告了压缩率与渲染质量指标，主题与 Neural Scene Representations & Rendering 直接相关且思路清晰；但摘要仅覆盖 Mip-NeRF 360 与户外场景的有限结果，未提供方法细节、消融或更广泛验证，因此对需要深入方法评估的读者优先级为中等。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel view synthesis but produces millions of primitives through adaptive densification, leading to significant storage overhead. Learned-mask pruning methods such as LP-3DGS address this by assigning each Gaussian a learnable mask to identify and prune redundant primitives. However, we identify a limitation of this paradigm: the steep slope of the Gumbel-Sigmoid activation drives mask values to the extremes within the short mask-training window, before the importance ranking has stabilized, producing a sharply bimodal distribution from which that ranking can no longer be reliably recovered. We propose LinearMask-GS, which replaces Gumbel-Sigmoid with a linear increment activation that keeps mask values in a mid-confidence regime throughout mask training, producing a stable, unimodal mask distribution whose ranking tracks importance. On Mip-NeRF 360, our method achieves 3.6x and 1.6x Gaussian reductions over 3DGS and LP-3DGS, respectively, while maintaining or improving rendering quality. For outdoor scenes, it yields a 1.6x reduction (from 2.18M to 1.36M) with notable gains in PSNR (+0.38 dB), SSIM (+0.025), and LPIPS (-0.029).

</details>

#### 2026-09-09 - RealSimLoop: Online Real-to-Sim Adaptation via Differentiable Reduced-Order Simulation with Vision Feedback

**Authors:** Zhihao Cen, Chuhua Xian, Hailin Sun, Yuliang Liufu, Zhen Zhang, Xiangyu Chu, Hongmin Cai, Yunbo Zhang, Guoxin Fang
**Links:** [abs](https://arxiv.org/abs/2609.09828) - [pdf](https://arxiv.org/pdf/2609.09828)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, differentiable rendering, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RealSimLoop: Online Real-to-Sim Adaptation via Differentiable Reduced-Order Simulation with Vision Feedback
- 作者：Zhihao Cen, Chuhua Xian, Hailin Sun, Yuliang Liufu, Zhen Zhang, Xiangyu Chu, Hongmin Cai, Yunbo Zhang, Guoxin Fang
- 出版日期：2026-09-09T07:33:40Z
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2609.09828 ；PDF https://arxiv.org/pdf/2609.09828

### 一句话总结
RealSimLoop 提出一种以视觉为物理反馈、在降阶神经子空间内做可微仿真的在线 real-to-sim 自适应框架，旨在准实时地细化材料刚度等物理参数并跟踪时变材料属性。

### 研究问题
论文关注的是：对可变形物体的真实观测往往稀疏或仅限表面，而下游任务需要内部形变、应力场、交互力等隐藏物理量；基于物理的仿真虽可恢复这些量，但在线 real-to-sim 自适应面临三大困难——全空间优化代价高昂、反馈有限、材料属性随时间变化。摘要未提供足够信息说明这些困难在具体场景中的量化表现。

### 核心思路/方法
- 在降阶神经子空间中执行可微仿真，以大幅加速优化循环，从而实现准实时性能。
- 将高效动力学模型与可微渲染耦合，使梯度可直接反向传播，并利用高保真像素数据细化材料刚度等物理参数。
- 采用滑动窗口目标函数，实现稳健的在线自适应，使系统能够跟踪时变材料属性，并弥合由模型降阶或未建模动力学带来的 real-to-sim 差距。

### 主要贡献
- 提出 RealSimLoop，一个以视觉数据作为物理反馈的可微在线 real-to-sim 自适应框架。
- 通过在降阶神经子空间内进行可微仿真，实现准实时的优化性能。
- 将高效动力学模型与可微渲染结合，支持直接梯度回传，以像素数据细化物理参数。
- 通过滑动窗口目标函数支持在线自适应，以跟踪时变材料属性并缩小 real-to-sim 差距。
- 摘要称大量实验表明该方法优于传统离线方法，并验证了其在下游应用中的通用性，包括外力预测、三维应力场重建与新视角合成。具体实验设置、对比指标和数值结果摘要未提供足够信息。

### 局限性
摘要未提供足够信息说明方法的具体局限，例如降阶子空间的近似误差边界、对训练数据或视觉观测条件的依赖、计算资源需求、失败情形以及实验覆盖范围等均未在摘要中展开。

### 阅读优先级
中。理由：该工作面向可变形物体在线 real-to-sim 自适应，结合可微降阶仿真、可微渲染与视觉反馈，问题设定和下游应用（外力预测、应力场重建、新视角合成）具有明确交叉价值；但摘要未给出实验细节、定量结果与局限讨论，是否值得优先精读需进一步查看正文与实验部分后再判断。

</details>

<details>
<summary>Abstract</summary>

Real-world observations of deformable objects are often sparse or surface-level, while downstream tasks require hidden physical quantities such as internal deformation, stress fields, and interaction forces. Physics-based simulation can recover these quantities, but online real-to-sim adaptation remains challenging due to costly full-space optimization, limited feedback, and time-varying material properties. To address these challenges, we propose RealSimLoop, a differentiable framework for online real-to-sim adaptation using vision data as physical feedback. Our approach achieves quasi-real-time performance by executing differentiable simulation within a reduced-order neural subspace, drastically accelerating the optimization loop. We couple this efficient dynamics model with differentiable rendering, enabling direct gradient backpropagation that leverages high-fidelity pixel data to refine physical parameters such as material stiffness. Furthermore, by employing a sliding-window objective function, RealSimLoop enables robust online adaptation, allowing the system to track time-varying material properties and effectively bridge the real-to-sim gap arising from model reduction or unmodeled dynamics. Extensive experiments demonstrate that our method outperforms conventional offline methods, and we validate the framework's versatility in downstream applications, including external force prediction and 3D stress field reconstruction with novel view synthesis.

</details>

#### 2026-09-09 - RouteBridge: Reliability-Routed Bidirectional Distillation Between Neural Radiance Fields and 3D Gaussian Splatting

**Authors:** YuanHang Wang, Xin Cao
**Links:** [abs](https://arxiv.org/abs/2609.09606) - [pdf](https://arxiv.org/pdf/2609.09606)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RouteBridge: Reliability-Routed Bidirectional Distillation Between Neural Radiance Fields and 3D Gaussian Splatting
- 作者：YuanHang Wang, Xin Cao
- 出版日期：2026-09-09T02:00:17Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.09606) / [PDF](https://arxiv.org/pdf/2609.09606)

### 一句话总结
RouteBridge 提出一种按光线自适应选择教师方向的双向蒸馏框架，在 NeRF 与 3DGS 之间进行可靠监督路由或弃权，以缓解全局固定教师带来的局部重建误差传播。

### 研究问题
NeRF 与 3DGS 具有互补的归纳偏置，但现有跨表示蒸馏通常将某一种表示固定为整个场景的教师。摘要指出，全局固定的教师会传播局部重建误差。因此，论文关注的核心问题是：如何避免单一固定教师方向带来的误差传播，并在两种表示之间实现更可靠的跨表示监督。

### 核心思路/方法
- 提出 RouteBridge，一个双向蒸馏框架，为每条光线选择教学方向。
- 可靠性估计器结合光度残差与表示特定的几何证据。
- 路由监督有三种可能：从 NeRF 到 3DGS、从 3DGS 到 NeRF，或弃权。
- 使用与渲染器无关的接口传递颜色、不透明度和归一化深度。
- 该接口不依赖共享特征或点对应关系。

### 主要贡献
- 提出按光线进行可靠性路由的双向蒸馏框架，而不是全局固定教师。
- 设计可靠性估计器，融合光度残差与表示特定的几何证据，用于选择监督方向或弃权。
- 提供渲染器无关的接口，传递颜色、不透明度和归一化深度，无需共享特征或点对应。
- 在 mip-NeRF 360 上，NeRF 与 3DGS 导出分别达到 28.56 dB 和 28.77 dB；3DGS 导出相比 3DGS 提升 1.56 dB，相比 NeRF-GS 提升 0.45 dB，并将 LPIPS 降至 0.207。
- 在静态三视图 DTU 上达到 21.12 dB。
- 消融表明，自适应路由和几何光线目标都对改进有贡献。

### 局限性
摘要未提供足够信息。摘要未说明失败场景、对特定数据集的依赖、计算开销、超参数敏感性、对动态场景的适用性，也未提供与更多基线方法的完整比较。

### 阅读优先级
高。理由：该论文针对 NeRF 与 3DGS 跨表示蒸馏中固定教师导致误差传播的问题提出双向路由方案，问题明确，方法具有针对性，且在 mip-NeRF 360 和 DTU 上给出了定量结果与消融支持；如果关注神经场景表示、跨表示蒸馏或 3DGS 与 NeRF 结合，优先级较高。

</details>

<details>
<summary>Abstract</summary>

Neural radiance fields (NeRFs) and 3D Gaussian Splatting (3DGS) encode a scene with complementary inductive biases, but existing cross-representation distillation typically fixes one representation as teacher for the entire scene. A globally fixed teacher can propagate local reconstruction errors. We present RouteBridge, a bidirectional framework that selects the teaching direction for each ray. Its reliability estimator combines photometric residuals with representation-specific geometric evidence and routes supervision from NeRF to 3DGS, from 3DGS to NeRF, or abstains. A renderer-independent interface transfers color, opacity, and normalized depth without shared features or point correspondence. On mip-NeRF 360, the NeRF and 3DGS exports reach 28.56 and 28.77 dB, respectively. The 3DGS export improves over 3DGS by 1.56 dB and over NeRF-GS by 0.45 dB while reducing LPIPS to 0.207. On static three-view DTU, RouteBridge obtains 21.12 dB. Ablations show that both adaptive routing and geometric ray targets contribute to the improvement.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

#### 2026-09-10 - Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection

**Authors:** Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie, Gang Liu, Hongjie Yan, Wei Zhou
**Links:** [abs](https://arxiv.org/abs/2609.11225) - [pdf](https://arxiv.org/pdf/2609.11225)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** stereo depth, robot navigation, mapping, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- 作者：Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie, Gang Liu, Hongjie Yan, Wei Zhou
- 出版日期：2026-09-10T08:25:46Z
- 分类：Embodied / Robotics / AR Applications（主要分类）；次要分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.11225 ；PDF https://arxiv.org/pdf/2609.11225

### 一句话总结
论文提出统一的具身智能体运行时 HROS 及其住宅小区巡检实现 Argos，将四足机器人导航、感知、认知推理、语音交互与安全约束下的自演化整合为可追踪的闭环巡检系统。

### 研究问题
自主物业巡检不仅需要稳健的机器人导航，还需要在可追踪的运行闭环中连接异构传感、可复用的自主能力、多模态场景理解、人机交互与企业响应。现有四足巡检系统常通过任务专用接口集成这些功能，导致上下文协调、知识复用和受控适应变得困难。

### 核心思路/方法
- 提出 Harness Robotic OS（HROS），一个统一的具身智能体运行时；Argos 是其面向住宅小区巡检的具体实现。
- HROS 将系统组织为机器人运行时、具身自主技能、认知智能体运行时、交互与运维平面。
- 通过共享上下文连接物理状态与智能体推理。
- 支持流式 ASR/TTS 的语音任务交互。
- 采用分层的工作记忆、情景记忆与语义记忆来保存运行知识。
- 设计安全门控的自演化闭环，将执行轨迹转化为带版本的候选更新，不允许无约束的在线修改。
- Argos 原型集成 Vbot 四足机器人、Fast-LIO2 定位与建图、Hobot-Stereo 深度感知、PCT-Planner 全局规划、EGO-Planner 局部运动生成，以及 OpenClaw 编排的 Qwen3-VL 巡检分析。

### 主要贡献
- 提出统一的具身智能体运行时 HROS，用于闭环四足巡检，缓解任务专用接口带来的上下文协调与知识复用困难。
- 给出 Argos 实现，将机器人运行时、自主技能、认知推理、语音交互和安全门控自演化组织为分层系统。
- 在住宅物业环境中验证部署的导航与巡检闭环，报告了 100% 航点可达率、户外定位误差低于 10 cm、局部障碍响应延迟低于 200 ms、代表性危险检测率 85–95%、告警投递与结构化报告生成成功率 99%。
- 摘要称 HROS 为记忆增强、语音感知且可持续改进的具身巡检智能体提供可扩展软件基础。

### 局限性
- 论文仅提供摘要，未提供关于实验规模、场景数量、基线对比、消融研究、失败案例和统计显著性的细节；这些信息摘要未提供足够信息。
- 危险检测率 85–95% 的具体类别、测试条件与误报情况，摘要未提供足够信息。
- 自演化闭环的版本管理机制、安全门控具体策略及其长期有效性，摘要未提供足够信息。
- 系统在住宅小区之外的泛化能力、不同机器人平台的可移植性，摘要未提供足够信息。
- 真实部署中的成本、维护、隐私与法规问题，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文聚焦具身智能体运行时与四足机器人闭环巡检的系统集成，涉及导航、感知、认知记忆、语音交互与安全自演化等完整链路，并给出可量化的部署指标；对具身智能系统落地、机器人操作系统架构和物业巡检应用有直接参考价值。但需注意仅凭摘要无法评估实验严谨性与泛化性，建议获取全文后重点核查实验细节与自演化机制。

</details>

<details>
<summary>Abstract</summary>

Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

</details>

#### 2026-09-09 - Grounding Generated Video Plans in Simulation Towards Versatile Dexterous Controllers

**Authors:** Tianyue Wu, Boyuan An, Shuqi Zhao, Heyu Guo, Wanli Xing, Yi Ma, Kaifeng Zhang, Ruihai Wu, Masayoshi Tomizuka
**Links:** [abs](https://arxiv.org/abs/2609.10050) - [pdf](https://arxiv.org/pdf/2609.10050)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Grounding Generated Video Plans in Simulation Towards Versatile Dexterous Controllers
- 作者：Tianyue Wu, Boyuan An, Shuqi Zhao, Heyu Guo, Wanli Xing, Yi Ma, Kaifeng Zhang, Ruihai Wu, Masayoshi Tomizuka
- 出版日期：2026-09-09T11:26:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.10050) / [PDF](https://arxiv.org/pdf/2609.10050)

### 一句话总结
将生成的手-物交互视频作为运动参考，通过仿真中的 HOI grounding 训练多物体、多轨迹的灵巧操作跟踪器，并在部署时由视频模型生成运动计划交由该跟踪器执行。

### 研究问题
生成式 HOI 视频能提供可控的操作运动提议，而基于仿真的 HOI 跟踪可把运动学参考转化为可行的底层控制，但其可扩展性受限于缺乏可靠的参考运动。论文要解决的是如何高效、可扩展地获取可靠参考运动，并把生成视频中的运动计划真正落地到仿真与真实控制中。

### 核心思路/方法
论文将生成视频与基于仿真的 HOI grounding 结合：训练阶段，用生成视频提供多样化的运动参考，学习一个多物体、多轨迹的 HOI 跟踪器；部署阶段，由视频模型产生运动计划，再由学到的跟踪器执行。为支持可扩展的参考生成，作者提出通过 HOI 重建、以最小人工干预生成参考数据的方法，并在仿真中成功 grounding 了超过 1,500 个生成视频。

### 主要贡献
- 提出结合生成视频与仿真 HOI grounding 的框架，用于学习多物体、多轨迹的 HOI 跟踪器。
- 提出以最小人工干预、通过 HOI 重建实现可扩展参考生成的方法。
- 在仿真中成功 grounding 超过 1,500 个生成视频，并在基于仿真的训练中取得比基线高出 25 个百分点以上的成功率。
- 在真实世界闭环实验中实现多样化抓取，包括功能性抓取、非抓取式操作以及抓取后物体位姿跟踪。

### 局限性
摘要未提供足够信息。例如未说明真实世界实验的具体任务范围、成功率、失败模式、泛化边界，也未给出仿真与真实环境之间的差距分析、计算成本或数据规模上限等细节。

### 阅读优先级
高。理由：论文聚焦生成视频到仿真 grounding 再到真实灵巧控制的完整链路，并报告了仿真训练中超过基线 25 个百分点以上的成功率提升以及真实闭环中的多类操作能力；若关注具身智能、灵巧操作、视频生成驱动机器人控制等方向，该工作与核心问题直接相关。

</details>

<details>
<summary>Abstract</summary>

Generated hand-object interaction (HOI) videos provide a controllable way to propose manipulation motions. Simulation-based HOI tracking can translate such kinematic references into feasible low-level control, but its scalability is limited by the lack of reliable reference motions. We therefore combine generated videos with simulation-based HOI grounding: during training, generated videos provide diverse motion references for learning a multi-object, multi-trajectory HOI tracker, and at deployment, the video model produces motion plans that are executed by the learned tracker. In particular, we propose a method that enables scalable reference generation by HOI reconstruction with minimal manual intervention and successfully grounds more than 1,500 generated videos in simulation, achieving success rates over 25 percentage points higher than those of baselines during simulation-based training. In real-world closed-loop experiments, it achieves diverse grasps, including functional grasps, non-prehensile manipulation, and post-grasp object-pose tracking. Videos and code are available at https://boyuan-an.github.io/GALATEA/.

</details>

#### 2026-09-08 - Agentic AI-enabled Semantic Commissioning of a Cognitive Digital Twin for Reconfigurable Manufacturing

**Authors:** Yangyang Liu, Xun Xu, Jan Polzer
**Links:** [abs](https://arxiv.org/abs/2609.09503) - [pdf](https://arxiv.org/pdf/2609.09503)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** geometric reconstruction, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Agentic AI-enabled Semantic Commissioning of a Cognitive Digital Twin for Reconfigurable Manufacturing
- 作者：Yangyang Liu, Xun Xu, Jan Polzer
- 出版日期：2026-09-08T22:34:38Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.09503 ；PDF https://arxiv.org/pdf/2609.09503

### 一句话总结
论文提出一种基于智能体与 AI 驱动的自动化工作流，用于认知数字孪生的端到端调试与语义化部署，以应对可重构制造中快速定制化部署的难题。

### 研究问题
可重构制造中，认知数字孪生的快速定制化部署是一大挑战。传统数字孪生构建方法主要关注几何重建，往往忽视自主推理所需的深层语义集成与功能互操作性。

### 核心思路/方法
论文提出一种基于智能体、由 AI 驱动的工作流，用于自动化端到端认知数字孪生调试。系统以 LangGraph 作为多智能体编排引擎，实现双路径合成：
- 语义路径：使用检索增强生成（RAG）从非结构化文档中抽取技术规格；
- 功能路径：使用模型上下文协议（MCP）自主发现并绑定实时工业遥测数据。

### 主要贡献
- 提出面向认知数字孪生自动调试的智能体化、AI 驱动工作流。
- 采用 LangGraph 作为多智能体编排引擎，实现语义路径与功能路径的双路径合成。
- 语义路径利用 RAG 从非结构化文档中抽取技术规格。
- 功能路径利用 MCP 自主发现并绑定实时工业遥测数据。
- 在机器人加工单元中进行实验验证：感知平均精度（mAP）达到 97.2%，部署周期从数周缩短至平均 2 小时，体现从手动脚本向自主编排的范式转变。

### 局限性
摘要未提供足够信息。摘要未说明该方法的适用边界、失败情形、对特定工业协议或文档质量的依赖、实验样本规模、可扩展性或与其他方法的对比局限。

### 阅读优先级
高。理由：该论文聚焦可重构制造与认知数字孪生的自动化部署，问题明确且具有工程价值；摘要给出的验证结果（mAP 97.2%、部署周期从数周降至平均 2 小时）量化显著，并涉及 LangGraph、RAG、MCP 等当前受关注的技术组合。若读者关注具身智能、机器人制造、数字孪生或智能体编排，该论文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Rapid bespoke commissioning of the Cognitive Digital Twin (CDT) is a major challenge in reconfigurable manufacturing. Traditional digital twin (DT) construction methods primarily focus on geometric reconstruction, often neglecting the deep semantic integration and functional interoperability necessary for autonomous reasoning. This paper proposes an agent-based, AI-driven workflow to automate end-to-end CDT debugging. The system utilises LangGraph as a multi-agent orchestration engine to achieve dual-path synthesis: the semantic path extracts technical specifications from unstructured documents using Retrieval Augmented Generation (RAG), while the functional path autonomously discovers and binds to real-time industrial telemetry data using Model Context Protocol (MCP). Experimental validation in a robotic machining cell demonstrates that the system achieves a mean average accuracy (mAP) of 97.2% in perception and reduces the deployment cycle from several weeks to an average of 2 hours, marking a paradigm shift from manual scripting to autonomous orchestration.

</details>

#### 2026-09-08 - SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators

**Authors:** Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang, Junyi Cao, Haoyu Zhen, Yilun Du, Chuang Gan
**Links:** [abs](https://arxiv.org/abs/2609.09155) - [pdf](https://arxiv.org/pdf/2609.09155)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, mapping, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators
- 作者：Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang, Junyi Cao, Haoyu Zhen, Yilun Du, Chuang Gan
- 出版日期：2026-09-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.09155

### 一句话总结
SyncWorld 提出一种利用“视觉校准片段”在上下文中指定动作-视觉映射的动作条件世界模型，无需额外训练即可作为零样本模拟器，在未见环境中预测动作结果并支持测试时策略改进。

### 研究问题
如何使世界模型作为机器人策略回环中的想象环境时，在未见环境（不同视觉环境、相机视角、机器人位置或形态）下实现细粒度、可靠且零样本的动作模拟？核心障碍在于动作并非像素空间的通用语言——相同数值动作在不同设置下的视觉表现不一致，导致混合训练监督冲突和泛化脆弱。

### 核心思路/方法
- 引入 SyncWorld，一种动作条件世界模型，作为跨未见环境的零样本模拟器。
- 利用“视觉校准片段”（visual calibration episode，包含成对的帧与动作，展示所有可控自由度）在上下文中指定特定设置的“动作-视觉映射”（Action–Visual Mapping）。
- 在训练时加入视觉校准上下文，使模型学会通过视觉证据解释动作；当显式校准不可用时，模型可利用交互历史进行推断。
- 该方法无需任何额外训练即可在推理时利用模拟出的 rollout 进行测试时策略改进。

### 主要贡献
- 提出 SyncWorld，首次将动作条件世界模型构建为零样本模拟器，可在未见环境中直接应用。
- 提出利用视觉校准片段在上下文中编码设置相关的动作-视觉映射，解决跨环境动作语义不一致问题。
- 训练策略使模型既能利用显式校准上下文，也能在缺乏校准时依赖交互历史。
- 实验表明 SyncWorld 能准确模拟未见设置中的动作结果，并可在无需训练的情况下实现测试时策略提升。

### 局限性
摘要未提供足够信息。摘要仅提及实验证明其模拟准确性与策略改进能力，但未给出具体实验设置、基线对比、失败案例或对校准片段长度与质量的敏感性分析等细节。

### 阅读优先级
**高**。理由：该工作针对世界模型在机器人策略-回环应用中因动作跨环境泛化差而难以扩展的关键瓶颈，提出新颖的零样本模拟器框架，解决了机器人领域普遍存在的动作非通用语言问题；方法上利用上下文校准而非重训练，具有实用价值，且显示可用于测试时策略改进，对 Embodied AI 与机器人学习方向研究者有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment. We introduce SyncWorld, an action-conditioned world model that serves as a zero-shot simulator across unseen environments without any additional training. SyncWorld leverages a visual calibration episode---paired frames and actions that showcase all the controllable degrees of freedom---to specify the setup-specific Action--Visual Mapping in context. Training with visual calibration contexts teaches the model to interpret actions through visual evidence and to leverage interaction history when explicit calibration is unavailable. Experiments show that SyncWorld can accurately simulate action outcomes in previously unseen settings, and that its capability of simulating rollouts enables test-time policy improvement without training.

</details>

#### 2026-09-08 - GoDeep: Annotation-Free Open-Vocabulary 3D Scene Understanding via Language-Space Lifting

**Authors:** Thodoris Betsas, Anastasios Doulamis, Andreas Georgopoulos
**Links:** [abs](https://arxiv.org/abs/2609.09082) - [pdf](https://arxiv.org/pdf/2609.09082)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GoDeep: Annotation-Free Open-Vocabulary 3D Scene Understanding via Language-Space Lifting
- 作者：Thodoris Betsas, Anastasios Doulamis, Andreas Georgopoulos
- 出版日期：2026-09-08T17:31:51Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.09082

### 一句话总结
GoDeep 提出一种无需 2D-3D 标注、也无需 3D 训练语料库或专用 3D 编码器的开放词汇 3D 场景理解方法，通过将视觉-语言模型仅用作“翻译器”，直接在纯语言嵌入空间中完成实体级描述的地面化、投影与聚合。

### 研究问题
如何在不依赖 3D 训练语料、专用 3D 编码器及任何 2D-3D 标注的前提下，实现开放词汇的 3D 语义分割，并克服 CLIP 嵌入在组合任务上存在的“词袋”式表现（即无法有效区分物体的存在与缺失，且对词汇外物体定位能力弱）？

### 核心思路/方法
- 将视觉-语言模型（如 CLIP）仅作为翻译器，而非 3D 特征提取器：对每张带位姿的图像生成结构化、实体级别的自然语言描述。
- 将这些描述进行地面化（grounding）、投影（projection）与聚合（aggregation），直接在通用的、仅含语言的嵌入空间中完成 3D 场景理解，不训练 3D 编码器，也不需要 3D 训练语料库。
- 所有表示均为离散文本，因此点级预测具有可解释性。
- 提出一种启发式加权聚合策略作为概念验证，该策略偏好“精确但非频繁”的观测，并利用 GoDeep 的可解释性以强化对更细粒度元素的定位。

### 主要贡献
- 提出一种无需标注、无需 3D 训练语料库/编码器的开放词汇 3D 分割管线，利用语言空间提升实现。
- 在 ScanNet++ 上，与使用 ScanNet 训练的强大无标注基线方法表现相当。
- 在含 5 栋建筑的文化遗产基准上，原始分数偏向 CLIP 变体，但一次系统性词汇修正即可逆转排名；该效应在另一类不同对象上通过独立的第二次修正得到验证，表明语言空间嵌入比 CLIP 嵌入更忠实地追踪物理内容。
- 在 ScanNet++ 上对真正的词汇外（OOV）对象展现出更强的“存在”与“缺失”区分能力，且无需任何 2D-3D 标注即可定位这些 OOV 对象。
- 因所有表示均为离散文本，预测在点级别可解释。

### 局限性
摘要未提供足够信息。摘要中未明确讨论方法的显式局限性（如计算开销、对描述质量的依赖、在更大规模场景上的扩展性、失败模式等），也未报告定量实验配置细节。

### 阅读优先级
**中**。理由：该方法在方法论上有明显创新（将 VLM 纯作翻译器、在语言空间中完成 3D 理解），并展示了在词汇外对象定位和可解释性上的优势，对于开放词汇 3D 感知方向有参考价值。但其发表于 2026 年，归档时间较早（预印本），且摘要未提供充分的实验对比与定量细节，需要读者自行谨慎评估其可复现性与实际效果强度，故给出中等优先级。

</details>

<details>
<summary>Abstract</summary>

Open vocabulary 3D semantic segmentation methods typically lift CLIP features into 3D. This embeds points in a joint vision-language space known to behave like a bag-of-words on compositional tasks. Furthermore, even annotation free variants often require a large 3D training corpus and a dedicated 3D encoder per domain. Instead we use a vision-language model purely as a translator. It produces structured, entity-level descriptions of each posed image. These descriptions are grounded, projected, and aggregated directly in a general-purpose, language-only embedding space, with no 3D training corpus or encoder required. On ScanNet++, our pipeline is competitive with strong annotation free baselines trained on ScanNet. On a 5-building cultural heritage benchmark, raw scores initially favor a CLIP-based variant, but a single systematic vocabulary correction reverses this ranking. An effect confirmed by a second, independent correction on a different class, indicating that language-space embeddings track physical content more faithfully. This fidelity extends to genuinely out-of-vocabulary (OOV) objects on ScanNet++ proving that language-space embeddings separate presence from absence objects far more sharply than CLIP-based embeddings do. GoDeep also localize these OOV objects within the scene, all without any 2D-3D annotation. Because every representation remains discrete text, predictions are also explainable at the point level. Finally, exploiting both a heuristic weighting, that favors precise over merely frequent observations and GoDeep's explainability property, we propose an aggregation strategy, as a proof of concept, that favors finer elements localization.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
