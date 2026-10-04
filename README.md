# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：90
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 28
  - Neural Scene Representations & Rendering: 27
  - Embodied / Robotics / AR Applications: 24
  - Geometry Foundation Models: 6
  - Dynamic / 4D Reconstruction: 5
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“基础模型 + 少量/零微调”正在向动态、遮挡、消歧等硬场景迁移。**
   多篇论文不再从头训练专用模型，而是把已有基础模型扩展到其原本不擅长的场景：
   - Dyna3 把静态深度基础模型 DA3 扩展到 4D 动态重建，且完全训练无关；
   - MVDG 基于 3D 基础模型 VGGT 做多视角消歧，替代成对分类器；
   - Latent-Foresight 针对 VFM 特征空间“两阶段解耦”问题，改为端到端学习可预测的潜在表示；
   - CROSS 在视觉语言模型上叠加免训练的几何算子库，而非重新训练模型。
   这说明社区正从“造更大的基础模型”转向“如何把基础模型接到具体空间/动力学任务上”。

2. **多模态物理属性重建开始从“外观”扩展到触觉、热觉与光照。**
   - TouchTherm 构建视觉—触觉—热觉多模态数字孪生，强调微观表面结构与瞬态温度；
   - EvenSplat 把曝光与光照从几何/颜色中分离，引入相机响应网络与局部曝光补偿；
   - Affine-Aligned Atlas 处理视频中全局运动对规范高斯表示的干扰。
   与之呼应的是，重建目标正从“看起来对”走向“物理可用”，即面向仿真、触觉渲染、光照稳定的资产。

3. **“重建即中间产物、服务于下游任务”的趋势明显。**
   重建不再以视觉指标为终点，而是明确对齐机器人抓取、导航、手术评估、仿真训练等任务：
   - GenCOPE 直接面向机器人抓取的合成到真实位姿估计；
   - GlassGuard 面向机器人导航，把“自由空间污染”作为与覆盖率并列的成功指标；
   - LiteReality-Agent 面向仿真就绪的铰接式室内场景；
   - EIDA 面向 real-to-sim-to-real 导航迁移；
   - 手术技能评估论文用 RGB-D 与语义分解服务显微外科培训。
   这类工作普遍带有“任务级指标 + 几何/物理约束”的双重取向。

4. **几何对应与一致性仍是核心方法论抓手。**
   多篇论文用显式几何约束来稳定生成或重建：
   - World Observer 从共享全景源 warp，建立 actor 与 observer 的几何对应；
   - MEGA 用“先分割、后建网格”加掩码引导神经表面重建，追求对象级水密网格；
   - DecomVoxel 用 3D 原生先验加原位去噪优化，抑制空间漂移；
   - MVDG 用 3D 感知多视角特征做单次编解码消歧。
   这反映出：在生成式先验变强之后，几何一致性反而是更稀缺、更值得投入的约束。

5. **诊断与评测类工作开始和模型设计更紧密耦合。**
   - GIFTBench 把图像伪造定位的泛化诊断做成多轴基准，并把基准反过来当作训练资源；
   - 空间推理论文先把失败拆成四类错误，再据此设计 CROSS；
   - 单光子 LiDAR 论文指出“波形拟合准确不等于几何正确”，并用状态感知路由约束神经场。
   这是一种更健康的趋势：先定位失败模式，再设计针对性机制，而非单纯刷榜。

#### 技术路线观察

- **几何基础模型方向**：MVDG 是今天最典型的代表，沿着 VGGT 这类 3D 基础模型做多视角消歧，核心是把 O(n²) 成对推理压缩为单次多视角编解码。Dyna3 则从深度基础模型切入，利用跨视图特征在最佳匹配搜索下隐含的运动判别信号。二者共同点是：不再假设基础模型的注意力天然具备匹配或运动能力，而是显式构造证据来激活这些能力。

- **3D/4D 重建方向**：DecomVoxel、MEGA、LiteReality-Agent、单光子 LiDAR 重建、UAV 摄影测量参数研究构成一条从“生成先验”到“工程精度”的谱系。DecomVoxel 与 MEGA 关注重遮挡与对象级水密性；LiteReality-Agent 把重建表述为可执行代码的迭代编辑；单光子 LiDAR 强调混合回波下的状态判定；UAV 论文则提醒处理参数会带来从 16 mm 到 303 mm 的巨大精度差异。四者共同说明：重建质量的上限不仅取决于表征，也取决于证据路由、验证与流程配置。

- **神经场景表示方向**：EvenSplat 与 Affine-Aligned Atlas 都在修补 3DGS 类表示的假设漏洞——前者假设光照是场景属性，后者假设规范高斯能对齐所有帧。TouchTherm 进一步把表示从视觉扩展到触觉与热觉。路线侧重从“更快更真”转向“更可分解、更物理一致”。

- **机器人/AR 应用方向**：World Observer、GlassGuard、FlashDexRetarget、GenCOPE、EIDA、水下可穿戴机器人、手术技能评估共同显示，应用侧正在反向定义研究问题。World Observer 解决世界模型的对象持久性，GlassGuard 解决玻璃导致的碰撞边界缺失与自由空间污染，FlashDexRetarget 解决跨本体灵巧数据生成的成功率与效率，EIDA 解决执行接口层面的动力学差异。

- **交叉信号**：AR/机器人应用与三维重建的边界在变模糊。LiteReality-Agent、GenCOPE、GlassGuard 都同时挂在重建与具身应用之下，说明“仿真就绪”“任务可用”正在成为重建工作的默认评价维度。

#### 值得优先阅读的论文

1. **World Observer（2610.02162）**
   理由：它提出了一个清晰且重要的问题——世界模型在 actor 离开视野后如何保持对象状态，并给出“actor-observer 解耦 + 共享全景源 warp”的具体机制。对世界模型、具身智能、AR 持久化都有关联，适合作为今日趋势的入口。

2. **MVDG（2610.01098）**
   理由：它直接处理 3D 基础模型落地时最现实的障碍之一——doppelganger 消歧，并把 O(n²) 成对推理改为多视角单次推理。对做 SfM、视觉定位、大规模重建的读者优先级最高。

3. **Latent-Foresight（2610.01942）**
   理由：它直指当前 VFM + 世界模型的两阶段流水线缺陷，提出端到端联合学习潜在分词器与流式动态模型。若关注世界模型的表示学习，这是今天方法论上最有辨识度的一篇。

4. **Dyna3（2610.01286）**
   理由：训练无关地把静态深度基础模型扩展到 4D 动态场景，且 VLM 引导 SAM 3 做实例级分割的思路可复用性强。对动态重建与基础模型适配两条线都有参考价值。

5. **DecomVoxel（2610.01914）**
   理由：它同时触及 3D 原生先验、原位去噪优化与重遮挡分解重建，且提供代码。对关注生成先验与几何一致性平衡的读者，是今天最值得精读的重建论文之一。

#### 可能的研究机会

- **世界模型中的“观察者”机制与对象持久性**：World Observer 只给出初步框架。可跟进的问题包括：observer 数量如何随场景规模扩展、observer 之间如何避免冗余、对象重入时的状态一致性如何定量评估。可与 Dyna3 的动态点云解耦、Latent-Foresight 的可预测表示结合。

- **基础模型适配中的“证据路由”**：单光子 LiDAR 论文的状态感知路由、CROSS 的错误类型诊断、MVDG 的伪成对训练都指向同一类思路——先判定证据质量，再决定约束方式。可探索把这种路由机制泛化到深度基础模型、3DGS 与多视角消歧中。

- **物理属性重建与仿真就绪资产**：TouchTherm 的触觉—热觉、EvenSplat 的光照分解、L

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-02T13:51:38-04:00
**Total number of papers:** 90
**Number of papers added in the latest update:** 28
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

### 2026-10

#### 2026-10-01 - MVDG: Efficient Multi-view 3D Disambiguation on Unconstrained Real-World Images

**Authors:** Hanyuan Xiao, Gonglin Chen, Haolin Xiong, Wenbin Teng, Haiwei Chen, Yajie Zhao
**Links:** [abs](https://arxiv.org/abs/2610.01098) - [pdf](https://arxiv.org/pdf/2610.01098)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, structure from motion, SfM, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MVDG: Efficient Multi-view 3D Disambiguation on Unconstrained Real-World Images
- 作者：Hanyuan Xiao, Gonglin Chen, Haolin Xiong, Wenbin Teng, Haiwei Chen, Yajie Zhao
- 出版日期：2026-10-01T05:41:05Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.01098) / [PDF](https://arxiv.org/pdf/2610.01098)

### 一句话总结
MVDG 是一个基于 3D 基础模型 VGGT 的可扩展多视角消歧框架，通过单次编解码多视角图像减少对成对比较的依赖，在保持相近成对精度的同时提升 SfM 精度与推理速度。

### 研究问题
论文关注的是“doppelgangers”问题：不同但视觉上相似的 3D 表面之间会产生虚假匹配，这是大规模、真实场景下 3D 重建与视觉定位的基础性障碍。既有方法多用成对分类器缓解该问题，但摘要指出这种设计限制了多视角上下文推理，并给下游 SfM 带来 O(n^2) 推理复杂度。

### 核心思路/方法
- 提出 MVDG，一个可扩展的多视角消歧框架，构建在 3D 基础模型 VGGT 之上，可对任意数量的多视角图像进行联合推理。
- 通过引入 3D 感知的多视角特征，在单次前向过程中编码和解码视图，从而减少对成对比较的依赖。
- 摘要提到直接对 VGGT 进行多视角微调在噪声监督下可能不稳定；受 Doppelgangers 中标签歧义启发，作者从 AerialMegaDepth 构建伪成对训练集，并发现采样子集上的微调能带来稳定优化和对留出场景的较强泛化。
- 由于完整 SfM 评估即使使用 GLOMAP 等更快流程仍昂贵，作者处理伪成对数据集以进行高效验证，并推导常规 SfM 指标与该伪成对测试分类精度之间的预测关系。

### 主要贡献
- 提出 MVDG 多视角 3D 消歧框架，减少对成对分类设计的依赖，并支持任意数量多视角图像的联合推理。
- 针对 VGGT 多视角微调在噪声监督下的不稳定问题，构建基于 AerialMegaDepth 的伪成对训练集，并展示采样子集微调可实现稳定优化与对留出场景的泛化。
- 提出一种高效验证方式：处理伪成对数据集，并推导常规 SfM 指标与伪成对测试分类精度之间的预测关系，以规避昂贵完整 SfM 评估。
- 摘要声称实验表明该方法在保持可比成对精度的同时，相较基线提升了 SfM 精度与推理速度。

### 局限性
- 摘要未提供足够信息说明 MVDG 在何种具体场景、数据集规模或硬件条件下失效或性能下降。
- 摘要未提供足够信息说明伪成对训练集与真实成对监督之间的差距及其对最终性能的影响。
- 摘要未提供足够信息说明推导出的 SfM 指标与伪成对分类精度之间预测关系的适用范围与误差边界。
- 摘要未提供足够信息说明方法对 VGGT 基础模型的依赖程度，以及替换基础模型后的泛化表现。
- 摘要未提供足够信息给出完整实验设置、基线细节、定量结果与消融研究。

### 阅读优先级
中。理由：该工作针对真实场景 3D 重建与视觉定位中的多视角消歧问题，提出基于 3D 基础模型的可扩展框架，并涉及训练稳定性与高效评估，主题与 Geometry Foundation Models 和 3D Reconstruction & Multi-view Geometry 相关。但当前仅有摘要与元数据，缺少具体实验细节、定量结果和与基线的完整对比，因此适合作为方向性了解或后续精读候选，而非仅凭摘要即可高置信度判断其实际影响。

</details>

<details>
<summary>Abstract</summary>

Illusory matches between distinct yet visually similar 3D surfaces--doppelgangers--remain a fundamental obstacle for large-scale, in-the-wild 3D reconstruction and visual localization. Prior work mitigates this issue with pairwise classifiers, but this design limits multi-view contextual reasoning and incurs O(n^2) inference complexity for downstream structure-from-motion (SfM). We present MVDG, a scalable multi-view disambiguation framework built on the 3D foundation model VGGT, which jointly reasons over an arbitrary number of multiview images. By incorporating 3D-aware multi-view features, our method reduces dependence on pairwise comparisons by encoding and decoding views in a single pass. We further observe that direct multi-view fine-tuning of VGGT can be unstable under noisy supervision; motivated by label ambiguity in Doppelgangers, we construct a pseudo-pairwise training set from AerialMegaDepth and show that fine-tuning on sampled subsets yields stable optimization and strong generalization to held-out scenes. Finally, because full SfM evaluation (even with faster pipelines such as GLOMAP) remains expensive, we process a pseudo-pairwise dataset for efficient validation; we derive a predictive relationship between regular SfM metrics and the classification accuracy on this pseudo-pairwise test. Experiments show that our method achieves comparable pairwise accuracy while improving both SfM accuracy and inference speed over baselines.

</details>

#### 2026-10-01 - VASC: Value-Aware Sparse Attention with Cross-Layer Memory for Efficient 3D Reconstruction

**Authors:** Junyi Wu, Fanqing Kong, Leyang Chen, Shaoqiu Zhang, Yulun Zhang
**Links:** [abs](https://arxiv.org/abs/2610.01013) - [pdf](https://arxiv.org/pdf/2610.01013)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, scene reconstruction, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VASC: Value-Aware Sparse Attention with Cross-Layer Memory for Efficient 3D Reconstruction
- 作者：Junyi Wu, Fanqing Kong, Leyang Chen, Shaoqiu Zhang, Yulun Zhang
- 出版日期：2026-10-01T03:57:47Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.01013 ；PDF https://arxiv.org/pdf/2610.01013

### 一句话总结
VASC 面向 VGGT 等前馈式 3D 视觉模型，提出免训练的稀疏注意力方法，通过“值感知块选择”与“执行感知跨层记忆”在固定计算预算下减少冗余注意力，从而在 7Scenes 与 NeuralRGB-D 上改善位姿估计和重建质量，并相较稠密 VGGT 实现最高约 2.29 倍推理加速。

### 研究问题
前馈式 3D 视觉模型（如 VGGT）将相机估计与稠密场景重建统一在单次前向中，但其二次复杂度的全局注意力在长图像序列上代价高昂。现有稀疏方法可能偏向被高度关注但“值”上冗余的区域，从而未能有效保留真正有区分度的内容。论文即针对这一效率与信息选择问题展开。

### 核心思路/方法
论文提出 VASC，一种免训练的稀疏注意力方法，核心由两部分组成：
1. 值感知块选择：将池化后的 query-key 相关性与邻近 value 对比度结合，用于减少冗余，同时保留与 query 相关且具有区分性的内容。
2. 执行感知跨层记忆：跟踪跨层尚未被服务到的需求，并根据实际执行情况更新该状态，使先前未被充分覆盖的块也能在固定计算预算下参与竞争。

### 主要贡献
- 提出 VASC，一种免训练的稀疏注意力方法，结合值感知块选择与执行感知跨层记忆。
- 设计值感知块选择机制，融合池化 query-key 相关性与邻近 value 对比，以降低冗余并保留 query 相关且具区分性的内容。
- 设计跨层记忆机制，跟踪并更新跨层未服务需求，使先前未被充分服务的块在固定计算预算下仍可竞争。
- 在 7Scenes 和 NeuralRGB-D 上，结合 VGGT 与 π³ 的实验显示，相较 FasterVGGT 在位姿估计与重建质量上有改进，并相较稠密 VGGT 实现最高 2.29 倍推理加速。代码已公开。

### 局限性
摘要未提供足够信息。论文未在给定摘要中说明方法在更长序列、不同模型规模或更广泛数据集上的表现，也未给出失败案例、计算预算设置细节或与更多稀疏基线方法的系统比较。

### 阅读优先级
中。理由：该工作针对前馈式 3D 视觉模型中的全局注意力效率瓶颈，提出免训练稀疏注意力与跨层记忆机制，问题定位清晰，且报告了位姿估计、重建质量与推理加速方面的结果；但其方法细节、实验广度与局限性在摘要中披露有限，是否具有广泛适用性需进一步阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D vision models such as VGGT have achieved remarkable progress, unifying camera estimation and dense scene reconstruction in a single pass. However, their quadratic global attention makes long image sequences expensive, while existing sparse methods may favor highly attended yet value-redundant regions. To address these limitations, we introduce VASC, a training-free sparse attention method combining value-aware block selection and execution-aware cross-layer memory. Our value-aware block selection integrates pooled query--key relevance with neighboring value contrast, reducing redundancy while preserving query-relevant and distinctive content. Cross-layer memory tracks unserved demand across layers and updates this state according to actual execution, enabling previously underserved blocks to compete under a fixed computation budget. Experiments on 7Scenes and NeuralRGB-D with VGGT and $π^3$ demonstrate improved pose estimation and reconstruction quality compared with FasterVGGT, together with up to $2.29\times$ faster inference than dense VGGT. Code is available at https://github.com/kosakayamahoo-design/VASC.

</details>

### 2026-09

#### 2026-09-29 - Pow3R-SLAM: Real-Time RGB-D SLAM with 3D Reconstruction Priors

**Authors:** Christopher Kolios, Ishaan Mehta, Sasa Janjic, Yeganeh Bahoo, Sajad Saeedi
**Links:** [abs](https://arxiv.org/abs/2609.38054) - [pdf](https://arxiv.org/pdf/2609.38054)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** MASt3R, pointmap, 3D reconstruction, simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Pow3R-SLAM: Real-Time RGB-D SLAM with 3D Reconstruction Priors
- 作者：Christopher Kolios, Ishaan Mehta, Sasa Janjic, Yeganeh Bahoo, Sajad Saeedi
- 出版日期：2026-09-29T17:22:24Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要链接 https://arxiv.org/abs/2609.38054 ；PDF 链接 https://arxiv.org/pdf/2609.38054 ；项目网页 https://ChrisKolios.github.io/Pow3R-SLAM

### 一句话总结
Pow3R-SLAM 是一个实时 RGB-D SLAM 系统，将深度作为双视角 3D 重建网络的先验而非直接融合的几何信息，从而在跟踪精度、运行速度和建图密度上相较 MASt3R-SLAM 与 ORB-SLAM3 取得改进。

### 研究问题
传统 RGB-D SLAM 系统在深度图像稀疏时表现不佳。论文旨在利用可用的深度信息改善点图（pointmap）的条件数，并从双视角光度、深度和内参数据中推断空白区域的深度，从而提升实时 RGB-D SLAM 的跟踪与建图性能。

### 核心思路/方法
Pow3R-SLAM 受 MASt3R-SLAM 启发，后者使用双视角 3D 重建先验进行单目 SLAM。本文将深度作为网络预测的先验，而不是作为用于融合的几何信息。Pow3R 利用可用深度获得条件更好的点图，同时从双视角光度、深度和内参数据推断空白区域的深度。此外还引入了一种混合变体。

### 主要贡献
- 提出 Pow3R-SLAM，一个实时 RGB-D SLAM 系统，使用 Pow3R 进行跟踪与建图。
- 将深度作为网络预测的先验而非融合几何，以应对深度图像稀疏问题。
- 在 TUM、7-Scenes 和 Replica 的 24 条序列上按 MASt3R-SLAM 协议评估：运行时间快 1.6 倍，平均轨迹误差低 15%，未缩放误差低 3.1 倍，地图更稠密，Chamfer 距离低 30%。
- 引入混合变体，运行速度比 MASt3R-SLAM 快 2.1 倍，达到 25.3 FPS，同时保持改进的跟踪与建图精度。
- 在 RGB-D 模式下与 ORB-SLAM3 比较，Pow3R-SLAM 在 TUM、7-Scenes 和 ETH3D-SLAM 上更准确，并完成全部 TUM 序列。
- 项目网页已提供，代码将在接收后开源。

### 局限性
- 摘要明确提到 Pow3R-SLAM 在一小部分自相似场景（self-similar scenes）上可能表现困难。
- 摘要未提供足够信息说明具体失败原因、失败程度或适用边界。
- 摘要未提供足够信息说明混合变体的具体实现细节。
- 摘要未提供足够信息说明网络架构、训练细节、硬件平台或实时性测试环境。

### 阅读优先级
高。理由：该论文提出将深度作为双视角 3D 重建先验用于实时 RGB-D SLAM，在多个基准上相对 MASt3R-SLAM 和 ORB-SLAM3 报告了明确的精度与速度改进，且涉及 Geometry Foundation Models 与 3D Reconstruction & Multi-view Geometry 方向，若关注 RGB-D SLAM、3D 重建先验或实时建图，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We present Pow3R-SLAM, a real-time RGB-D simultaneous localization and mapping (SLAM) system that uses Pow3R for tracking and mapping. Inspired by MASt3R-SLAM, a recent work on monocular SLAM using two-view 3D reconstruction priors, we extend the work to incorporate depth as a prior on the network's prediction, rather than as geometry to fuse. Where traditional RGB-D SLAM systems struggle with sparsity in the depth images, Pow3R utilizes the available depth to give a better-conditioned pointmap, while inferring the depths in empty regions from the two-view photometric, depth, and intrinsic data. Evaluated against MASt3R-SLAM following its protocol on 24 sequences from TUM, 7-Scenes, and Replica, Pow3R-SLAM runs 1.6x faster in wall time, has 15% lower mean trajectory error, a 3.1x lower unscaled error, and produces denser maps, with a 30% lower Chamfer distance. We also introduce a hybrid variant that runs 2.1x faster than MASt3R-SLAM at 25.3 frames per second (FPS), while maintaining improved tracking and mapping accuracy. Against ORB-SLAM3 in RGB-D mode, Pow3R-SLAM is more accurate on TUM, 7-Scenes, and ETH3D-SLAM, and completes every TUM sequence. While Pow3R-SLAM can struggle on a small set of self-similar scenes, its overall performance shows that adding depth as a prior for two-view 3D reconstruction SLAM can be beneficial. A project webpage is available at: https://ChrisKolios.github.io/Pow3R-SLAM , and code will be made open-source upon acceptance.

</details>

#### 2026-09-29 - PhysWAM: Physically Consistent World Action Model for Autonomous Driving

**Authors:** Dhruv Parikh, Fengcheng Yu, Quankai Gao, Jiawei Yang, Junjie Ye, Maulik Bhatt, Thang Vu, Charles Ochoa, Rowan McAllister, Igor Vasiljevic, Rajgopal Kannan, Viktor Prasanna, Vitor Guizilini, Yue Wang
**Links:** [abs](https://arxiv.org/abs/2609.37970) - [pdf](https://arxiv.org/pdf/2609.37970)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth prediction, metric depth, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PhysWAM: Physically Consistent World Action Model for Autonomous Driving
- 作者：Dhruv Parikh, Fengcheng Yu, Quankai Gao, Jiawei Yang, Junjie Ye, Maulik Bhatt, Thang Vu, Charles Ochoa, Rowan McAllister, Igor Vasiljevic, Rajgopal Kannan, Viktor Prasanna, Vitor Guizilini, Yue Wang
- 出版日期：2026-09-29T16:38:13Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.37970 ；PDF https://arxiv.org/pdf/2609.37970

### 一句话总结
PhysWAM 是一个在单一 flow-matching transformer 中联合去噪多视角视频、度量深度与自车运动的自动驾驶世界-动作模型，并通过耦合点投影（CPP）几何约束提升世界与动作预测的物理一致性。

### 研究问题
世界-动作模型（WAMs）虽然能联合预测场景演化与智能体动作，但仅靠联合生成并不必然对两类预测施加共享的几何约束；本文关注如何让世界生成与动作生成在测得场景几何上保持一致，并改善自动驾驶规划。

### 核心思路/方法
- 统一建模：在单一 flow-matching transformer 中共同去噪多视角视频、度量深度和自车运动。
- 几何约束 CPP（Coupled Point Projection）：将生成的深度反投影为 3D 点，使用生成的自车运动 $\mathrm{SE}(3)$ 进行变换，并最小化其与使用记录自车运动变换后的 LiDAR 点之间的距离。
- 监督方式：该几何约束与标准 flow-matching 目标一起，联合监督生成的深度与运动，以促进与测量场景的物理一致性。
- 推理阶段：轨迹选择仅依赖简单的无标签共识规则，不使用学习到的打分器或模拟器反馈。

### 主要贡献
- 提出 PhysWAM，一个用于自动驾驶、在单一 flow-matching transformer 中协同去噪多视角视频、度量深度与自车运动的统一世界-动作模型。
- 提出耦合点投影（CPP）几何约束，通过将生成深度反投影、用生成自车运动变换并与记录自车运动变换后的 LiDAR 点对齐，联合监督深度与运动以增强物理一致性。
- 在 NAVSIM v1 与 v2 规划、零样本闭环迁移、未来视频与度量深度预测上评估 PhysWAM；尽管轨迹选择过程简单，仍取得较强规划性能，并能零样本迁移到未见驾驶环境，同时生成准确的度量深度与时间一致的视频，CPP 也改善了规划与深度预测。
- 结果表明，场景深度与自车运动之间的几何关系为在简单统一模型中耦合世界与动作生成提供了直接途径。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性、模型规模或训练数据规模。
- 摘要未提供足够信息说明在极端场景、长尾分布或传感器配置变化下的鲁棒性。
- 摘要未提供足够信息说明 CPP 对 LiDAR 点云质量、标定误差或缺失深度监督的敏感性。
- 摘要未提供足够信息说明与更复杂轨迹选择或闭环反馈方法相比的具体差距与失败案例。

### 阅读优先级
中。理由：该论文聚焦世界-动作模型的几何一致性，提出可插拔的 CPP 约束，并在 NAVSIM 与零样本迁移等多项任务上报告了收益；主题与自动驾驶、具身智能和几何基础模型相关，但摘要未给出实验规模、效率与失败模式等关键细节，是否高优先级取决于读者对世界模型或几何约束规划的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

World-action models (WAMs) jointly predict how a scene will evolve and how an agent should act, however joint generation alone does not necessarily impose a shared geometric constraint on these predictions. We present PhysWAM, a unified world-action model for autonomous driving that co-denoises multiview video, metric depth, and ego motion within a single flow-matching transformer. To ground world and action generation in measured scene geometry, we introduce Coupled Point Projection (CPP) that unprojects the generated depth into 3D points, transforms them using the generated $\mathrm{SE}(3)$ ego motion, and minimizes their distance to LiDAR points transformed using the recorded ego motion. This geometric constraint promotes physical consistency with the measured scene by jointly supervising generated depth and motion alongside their standard flow-matching objectives. At inference, trajectory selection relies only on a simple label-free consensus rule, with no learned scorer or simulator feedback. We evaluate PhysWAM across NAVSIM v1 and v2 planning, zero-shot closed-loop transfer, and future video and metric-depth prediction. Despite PhysWAM's simple selection procedure, it achieves strong planning performance and transfers zero-shot to unseen driving environments. It also generates accurate metric depth and temporally coherent video, with CPP improving both planning and depth prediction. Together, these results demonstrate that the geometric relationship between scene depth and ego motion provides a direct way to couple world and action generation within a simple unified model.

</details>

#### 2026-09-28 - Many Eyes, One World: Feed-Forward 3D Reconstruction from Mixed Cameras

**Authors:** Qiaoge Li, Yifan Zhan, Haijun Yang, Haiyang Liu, Yiyi Cai, Chenchi Luo
**Links:** [abs](https://arxiv.org/abs/2609.35658) - [pdf](https://arxiv.org/pdf/2609.35658)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Many Eyes, One World: Feed-Forward 3D Reconstruction from Mixed Cameras
- 作者：Qiaoge Li, Yifan Zhan, Haijun Yang, Haiyang Liu, Yiyi Cai, Chenchi Luo
- 出版日期：2026-09-28T17:21:52Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.35658) | [PDF](https://arxiv.org/pdf/2609.35658)

### 一句话总结
MEOW 是一个前馈式 3D 重建系统，能在不提供标定、畸变参数、相机类型标签或位姿的情况下，从混合透视、鱼眼和全景图像的 N 视图元组中单次前向重建度量点图与相机位姿。

### 研究问题
真实世界采集具有异构性：同一重建任务中可能同时存在透视、鱼眼和 360° 全景图像，但大多数前馈 3D 重建模型假设输入为透视图像且表示统一。摘要指出，近期处理多种相机类型的模型要么需要告知每个视图的相机类型，要么一次只重建一对图像；尚无单次方法能从图像本身重建包含完整全景图的混合相机元组。

### 核心思路/方法
- 设计哲学：将异构相机重建视为数据适配问题，而非架构重新设计。
- 保留透视预训练骨干网络，通过程序化数据引擎学习异构相机。
- 数据引擎将每个场景渲染在连续的相机模型流形上，提供精确光线和深度，并为每个相机采样的训练元组认证共视性。
- 仅用合成元组训练，零样本迁移到真实采集。

### 主要贡献
- 提出 MEOW，一个前馈系统，可从单个 N 视图混合相机元组（透视、鱼眼、完整全景）中一次前向联合重建度量点图和相机位姿，且不提供标定、畸变参数、相机类型标签或位姿。
- 提出以数据适配为核心的设计思路，保留透视预训练骨干，依靠程序化数据引擎学习异构相机。
- 摘要报告了零样本迁移结果：在异构 2D3DS 元组上达到 79.9 mAA@30，而 Wid3R 在已知每个视图相机类型时为 53.8；在激光扫描混合相机基准上，每个四视图混合元组配准达到 79.4 AUC@30。
- 将发布数据引擎、基准和完整评估流程。

### 局限性
- 摘要未提供足够信息说明方法在真实场景中的失败模式、计算成本、对极端相机模型的泛化边界或消融实验细节。
- 摘要未提供足够信息说明训练数据规模、合成与真实域差距的具体影响。
- 摘要未提供足够信息说明基准的完整构成与评估协议细节。

### 阅读优先级
高。理由：该工作针对混合相机前馈 3D 重建这一明确且具挑战性的问题，声称在单次前向中处理包含全景图的异构元组，并报告了相对基线的显著指标提升；同时涉及数据引擎、基准与评估流程的发布，对 3D 重建与多视图几何方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Real-world capture is heterogeneous: perspective, fisheye, and $360^\circ$ panoramic images can coexist within a single reconstruction task, yet most feed-forward 3D reconstruction models assume perspective imagery and a uniform input representation. Recent models handling several camera types are either informed of the camera type for each view or reconstruct one image pair at a time. No single-pass method reconstructs mixed-camera tuples containing full panoramas from images alone. We present MEOW, a feed-forward system that jointly reconstructs metric pointmaps and camera poses from one N-view tuple mixing perspective, fisheye and full-panorama images, in a single forward pass from images alone: no calibration, distortion parameters, camera-type labels or poses are supplied for any view. Our guiding design philosophy is to treat heterogeneous-camera reconstruction as a data-adaptation problem rather than an architectural redesign. MEOW retains a perspective-pretrained backbone and learns heterogeneous cameras entirely from a procedural data engine, which renders each scene across a continuous manifold of camera models with exact rays and depth, and certifies covisibility for every camera-sampled training tuple. Trained on synthetic tuples only, MEOW transfers zero-shot to real captures: on heterogeneous 2D3DS tuples it achieves 79.9 mAA@30 against 53.8 for Wid3R given the camera type of every view; on our laser-scanned mixed-camera benchmark it registers every four-view mixed tuple with 79.4 AUC@30. The data engine, benchmark, and complete evaluation pipeline will be released.

</details>

#### 2026-09-28 - ReSS: Residual-Restoring Sparse Attention for 3D Vision Transformers

**Authors:** Yongsung Kim, Jaehoon Lee, Minjun Park, Wooseok Song, Hun Hwangbo, Sungroh Yoon
**Links:** [abs](https://arxiv.org/abs/2609.35593) - [pdf](https://arxiv.org/pdf/2609.35593)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReSS: Residual-Restoring Sparse Attention for 3D Vision Transformers
- 作者：Yongsung Kim, Jaehoon Lee, Minjun Park, Wooseok Song, Hun Hwangbo, Sungroh Yoon
- 出版日期：2026-09-28T16:43:55Z
- 分类：primary: Geometry Foundation Models；secondary: 未提供
- 链接：摘要页 https://arxiv.org/abs/2609.35593 ；PDF https://arxiv.org/pdf/2609.35593 ；代码 https://github.com/libary753/ReSS

### 一句话总结
ReSS 将 3D 视觉 Transformer 中的注意力块稀疏选择，从“保留高注意力概率块”改为“最小化稀疏化在残差流中造成的漂移”，以在相同稀疏度下更好地保持稠密性能。

### 研究问题
3D 视觉 Transformer（如 VGGT）在多视图图像上单次前向预测相机位姿和场景几何，但其对所有拼接视图 token 的全局注意力会随视图数量增长而主导计算。已有的 SparseVGGT 和 HeSS 在块级别稀疏化注意力，并都保留高注意力概率的块。然而论文观察到：注意力概率并不能很好预测移除某个块后模型行为的实际变化，这种不匹配正是稀疏度提高时性能崩溃的原因。

### 核心思路/方法
论文提出 ReSS（ReSidual-ReStoring Sparse Attention），将块选择问题重新表述为：不再最大化保留的注意力质量，而是最小化稀疏化在残差流中留下的漂移。具体引入一个漂移分数（drift score），量化每个块对残差的偏移程度；由于一个被丢弃集合的漂移取决于贡献向量的方向而非仅其幅度，论文进一步采用迭代式残差恢复程序，从整体上细化丢弃集合。

### 主要贡献
- 指出注意力概率与实际移除块后模型行为变化之间存在不匹配，并说明该不匹配是稀疏度增加时性能崩溃的原因。
- 提出 ReSS，将块选择从最大化保留注意力质量转为最小化残差流漂移，并引入漂移分数与迭代残差恢复程序。
- 在三个骨干网络和五个数据集上，ReSS 在匹配稀疏度下比先前方法更好地保持稠密性能。
- 提供两项支持“漂移是决定稀疏化代价的量”的结果：最大化漂移会比随机选择更快降低性能；以实际漂移而非稀疏度作图时，所有方法大致落在一个曲线上。
- 代码已公开。

### 局限性
摘要未提供足够信息。摘要未说明具体骨干网络、数据集名称、计算开销细节、不同稀疏度范围、失败案例或方法适用边界。

### 阅读优先级
高。理由：该论文针对 3D 视觉 Transformer 全局注意力随视图数增长的计算瓶颈，提出与既有“高注意力概率保留”不同的稀疏化准则，并且摘要给出跨三个骨干、五个数据集的对比结果以及支持核心论点的额外证据，同时公开代码；对关注 3D 视觉 Transformer、几何基础模型和注意力稀疏化的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D vision transformers such as VGGT predict camera poses and scene geometry from multi-view images in a single forward pass, but their global attention over all concatenated view tokens dominates computation as the number of views grows. To reduce this cost, SparseVGGT and HeSS sparsify attention at the block level, and both retain blocks with high attention probability. However, we observe that attention probability poorly predicts how much the model's behavior actually changes when a block is removed, and we show that this mismatch is why performance collapses as sparsity increases. In this paper, we propose ReSS (ReSidual-ReStoring Sparse Attention), which recasts block selection from a problem of maximizing the retained attention mass to one of minimizing the drift that sparsification leaves in the residual stream. We introduce a drift score that quantifies how much each block shifts the residual, and, since the drift of a drop set depends on the directions of the contribution vectors rather than on their magnitudes alone, an iterative residual restoration procedure that refines the drop set as a whole. Across three backbones and five datasets, ReSS preserves dense performance better than prior methods at matched sparsity. Two further results support drift as the quantity that governs the cost of sparsification: maximizing drift degrades performance faster than random selection, and plotted against realized drift instead of sparsity, all methods fall approximately onto a single curve. Code is available at https://github.com/libary753/ReSS.

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-01 - Dyna3: VLM-Guided Training-Free 4D Reconstruction via Depth Foundation Models

**Authors:** Xinhao Xiang, Weiyang Li, Zhijie Zheng, Abhijeet Rastogi, Jiawei Zhang
**Links:** [abs](https://arxiv.org/abs/2610.01286) - [pdf](https://arxiv.org/pdf/2610.01286)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 4D reconstruction, dynamic scene reconstruction, scene reconstruction, pose estimation, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dyna3: VLM-Guided Training-Free 4D Reconstruction via Depth Foundation Models
- 作者：Xinhao Xiang, Weiyang Li, Zhijie Zheng, Abhijeet Rastogi, Jiawei Zhang
- 出版日期：2026-10-01T08:24:21Z
- 分类：Dynamic / 4D Reconstruction（次要分类：3D Reconstruction & Multi-view Geometry）
- 链接：摘要页 https://arxiv.org/abs/2610.01286 ；PDF https://arxiv.org/pdf/2610.01286

### 一句话总结
Dyna3 是一个无需微调的训练无关框架，将原本面向静态场景的深度基础模型 DA3 扩展到 4D 动态场景重建，并通过 VLM 引导 SAM 3 实现实例级动态物体分割。

### 研究问题
现有深度基础模型（如 Depth Anything 3，DA3）虽然在多视图深度估计上表现突出，但假设场景是静态 3D 的，因此在真实动态环境中适用性受限。已有训练无关的 4D 方法（如 Easi3R、VGGT4D）依赖经过对应关系训练的主干网络，其注意力机制编码了跨帧匹配信息，而 DA3 这类纯深度模型不具备这一性质。因此问题在于：如何在不进行微调的前提下，把纯深度的基础模型用于动态 4D 重建。

### 核心思路/方法
- 关键观察：DA3 的跨视图特征虽然只针对深度一致性训练，但在结合跨帧最佳匹配特征搜索后，隐含地编码了可区分运动的信号——静态表面能在全局找到一致匹配，动态物体则不能。
- 采用视觉语言模型（VLM）自动生成场景特定的语义提示，用于 SAM 3，实现精确的实例级分割，从而区分“哪些物体在动”与“存在哪些物体”。
- 重建时将场景解耦为跨帧对齐的静态背景与逐帧动态点云两部分。

### 主要贡献
- 提出 Dyna3，一个无需任何微调、训练无关的框架，将 DA3 扩展到 4D 动态场景重建。
- 揭示并利用了 DA3 跨视图特征中隐含的运动判别信号，通过跨帧最佳匹配特征搜索加以利用。
- 引入 VLM 生成场景特定语义提示驱动 SAM 3，实现实例级分割，区分运动物体与静态存在物体。
- 在四个数据集上的实验表明：在动态物体分割上以 +5.5pp J-Mean 超过当前最优 VGGT4D；姿态估计最高提速 13 倍，4D 重建提速 3 倍，内存降低 4 至 8 倍；有望支持更密集的时间采样。

### 局限性
摘要未提供足够信息。摘要未说明方法在何种场景下会失效、对 VLM 或 SAM 3 错误的敏感性、所依赖的假设边界，也未给出具体数据集名称、失败案例分析或计算资源下限等细节。

### 阅读优先级
高。理由：该工作针对深度基础模型无法处理动态场景这一明确痛点，提出无需微调的 4D 重建方案，并在摘要中给出了相对当前最优方法的定量提升（分割 +5.5pp、姿态最高 13 倍加速、重建 3 倍加速、内存降低 4 至 8 倍），同时结合了 VLM 与 SAM 3 的语义引导思路，对动态/4D 重建及多视图几何方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent depth foundation models like Depth Anything 3 (DA3) achieve remarkable multi-view depth estimation but assume static 3D scenes, limiting their applicability to real-world dynamic environments. Existing training-free 4D methods like Easi3R and VGGT4D rely on correspondence-trained backbones whose attention encodes cross-frame matching, a property absent in depth-only models like DA3. We present Dyna3, a training-free framework that extends DA3 for 4D dynamic scene reconstruction without any fine-tuning. Our key insight is that DA3's cross-view features, though trained only for depth consistency, implicitly encode motion-discriminative signals when combined with best-match feature search across frames. Its static surfaces find consistent matches globally, while dynamic objects cannot. We further adopt vision-language models (VLM) to automatically generate scene-specific semantic prompts for SAM 3, enabling precise instance-level segmentation that distinguishes which objects move from what objects exist. For reconstruction, we decouple the scene into a cross-frame aligned static background and per-frame dynamic point clouds. Experiments on four datasets demonstrate that Dyna3 surpasses correspondence-trained methods with +5.5pp J-Mean over state-of-the-art VGGT4D on dynamic object segmentation, while achieving up to 13x faster pose estimation and 3x faster 4D reconstruction with 4 to 8x lower memory. Dyna3 could therefore enable much denser temporal sampling that prior methods cannot support.

</details>

### 2026-09

#### 2026-09-29 - Eulerian Motion Reconstruction for Water Scenery

**Authors:** Chuhan Chen, Yen-Chi Cheng, Ayush Saraf, Rajvi Shah, Tuotuo Li, Johannes Kopf, Chen Gao, Hung-Yu Tseng, Deva Ramanan, Matthew O'Toole, Changil Kim
**Links:** [abs](https://arxiv.org/abs/2609.38622) - [pdf](https://arxiv.org/pdf/2609.38622)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic reconstruction, motion reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Eulerian Motion Reconstruction for Water Scenery
- 作者：Chuhan Chen, Yen-Chi Cheng, Ayush Saraf, Rajvi Shah, Tuotuo Li, Johannes Kopf, Chen Gao, Hung-Yu Tseng, Deva Ramanan, Matthew O'Toole, Changil Kim
- 出版日期：2026-09-29T22:23:35Z
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2609.38622 ；PDF：https://arxiv.org/pdf/2609.38622

### 一句话总结
该论文提出一种从单段非循环 2D 自然水景视频出发，重建可循环播放、可从新视角交互渲染的 4D 动态水景的方法，其核心是将运动表示为静态 3D 欧拉运动场并加入非周期残差项。

### 研究问题
论文关注水景（water scenery）的动态重建与动画化。作者指出，先前工作多从 2D 视频纹理角度处理该任务，目标是生成循环播放的视频；而本文希望从 3D 视角解决该问题：在仅有单段非循环 2D 源视频的条件下，重建一个可循环的 4D 动态表示，并支持从新视角进行交互式渲染。需要应对的挑战包括真实场景中存在的非周期性与随机动态。

### 核心思路/方法
- 将运动表示为 3D 静态 **欧拉运动场（Eulerian motion field）**。
- 该运动场对“规范高斯泼溅（canonical Gaussian splats）”进行平流（advect），这些高斯点在固定时间周期内循环重生（cyclically reborn at fixed time periods）。
- 训练监督信号来自渲染损失（supervised using rendering losses）。
- 为建模真实场景中的非周期与随机动态，在静态欧拉运动场之外额外引入一个**非周期、随时间变化的残差项（non-periodic, time-varying residual term）**，用于捕捉偏离静态欧拉运动场的部分。

### 主要贡献
- 将水景动态重建任务从 2D 视频纹理视角推进到 3D/4D 视角，目标是生成可循环的 4D 动态重建，而非仅生成循环视频。
- 提出以静态 3D 欧拉运动场驱动循环重生的高斯泼溅的表示方式，并用渲染损失进行监督。
- 通过引入非周期时变残差项，尝试建模真实水景中的非周期与随机动态。
- 摘要声称在定量与定性上均优于先前工作，可实现更逼真的水景动画。

### 局限性
摘要未提供足够信息。论文摘要未说明方法的具体失败情形、对特定水景类型或拍摄条件的依赖、计算开销、重建精度上限或非周期残差项的适用范围等局限。

### 阅读优先级
中。理由：该工作属于动态/4D 重建方向，问题设定（单段非循环 2D 视频输入、循环 4D 重建、新视角交互渲染）具有明确的研究价值，且结合了欧拉运动场、高斯泼溅与残差建模等要素。但仅凭摘要无法判断其技术细节、实验充分性与实际效果边界；若读者关注水景动画、4D 重建或高斯泼溅动态表示，可优先精读，否则可作为中优先级跟踪。

</details>

<details>
<summary>Abstract</summary>

Reconstructing and animating water scenery from nature produces compelling and immersive visual experiences. Previous work examined this task from the perspective of 2D video textures, with the goal of creating a looping video. In our work, we tackle the problem from a 3D perspective, creating a looping 4D dynamic reconstruction which can be interactively rendered from novel viewpoints from a single non-looping 2D source video. We represent motion as a 3D static \textit{Eulerian} motion field that advects canonical Gaussian splats that are cyclically reborn at fixed time periods, supervised using rendering losses. To model non-periodic and stochastic dynamics present in real-world scenes, we add a non-periodic, time-varying residual term to capture deviations from the static Eulerian motion field. We show quantitatively and qualitatively that our framework enables photorealistic animation of water scenes better than prior art.

</details>

#### 2026-09-29 - Gaussian Stippling: Efficient Sorting-Free 3D Gaussian Rendering through Hybrid Sampling and Spatiotemporal Reconstruction

**Authors:** Zijian Huang, Suiliang Mai, Chuankun Zheng, Yuan Meng, Yuchi Huo
**Links:** [abs](https://arxiv.org/abs/2609.38488) - [pdf](https://arxiv.org/pdf/2609.38488)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** spatiotemporal reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Stippling: Efficient Sorting-Free 3D Gaussian Rendering through Hybrid Sampling and Spatiotemporal Reconstruction
- 作者：Zijian Huang, Suiliang Mai, Chuankun Zheng, Yuan Meng, Yuchi Huo
- 出版日期：2026-09-29T20:15:59Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.38488 ；PDF https://arxiv.org/pdf/2609.38488

### 一句话总结
论文提出“Gaussian Stippling”，将连续 3D 高斯泼溅转换为离散可见性采样，以实现无需深度排序的顺序无关渲染，并通过混合采样策略与轻量时空重建网络抑制稀疏随机采样带来的噪声。

### 研究问题
传统 3D Gaussian Splatting（3DGS）需要深度排序和有序 alpha 混合来正确渲染相互重叠的高斯基元，这带来了排序相关的开销与顺序依赖问题。随机透明度虽然可以用离散随机可见性样本替代分数 alpha 贡献，从而实现无需排序的渲染，但在低采样数下会产生显著的空间和时间噪声。论文关注的核心问题是：如何在直接使用未修改 3DGS 资产的前提下，实现高效、顺序无关的渲染，并从稀疏随机样本中恢复高质量图像。

### 核心思路/方法
论文将连续高斯 splats 转换为离散可见性样本的过程称为 Gaussian Stippling，并基于此提出一种高效的顺序无关渲染与重建框架，直接作用于未修改的 3DGS 资产。

方法层面主要包括两部分：
1. 自适应整合基于基元（primitive-based）和基于片段（fragment-based）的 stippling，利用二者在不同渲染情形下的互补优势，以显著提升渲染吞吐量。
2. 引入轻量级的 Gaussian-aware 时空重建网络，从稀疏随机样本中恢复高质量图像。该网络利用每个 stipple 保留的高斯属性，在空间和时间维度上聚合结构化的随机线索，从而有效抑制 stippling 噪声。

### 主要贡献
- 提出 Gaussian Stippling 这一概念，将连续高斯 splats 转换为离散可见性样本，以支持无需排序的顺序无关渲染。
- 提出一种直接作用于未修改 3DGS 资产的高效顺序无关渲染与重建框架。
- 设计自适应混合的 primitive-based 与 fragment-based stippling 策略，以利用二者互补优势提升渲染吞吐量。
- 引入轻量级 Gaussian-aware 时空重建网络，利用每个 stipple 保留的高斯属性，在空间和时间上聚合随机线索以抑制噪声。
- 摘要称，混合 Gaussian stippling 方法配合在多样场景上训练的时空重建网络，可泛化到未见场景，并在移动设备上实现交互式、时间稳定且视觉合理的渲染，无需重新训练或预处理。
- 摘要还称，在场景特定训练并适当扩展采样与网络容量后，方法在视觉质量上进一步优于基线，为质量优先的应用提供高保真配置。

### 局限性
- 摘要未提供足够信息说明方法在极端低采样率、复杂遮挡或高动态场景下的具体失效情况。
- 摘要未提供足够信息说明其移动端性能的具体指标、延迟、功耗或内存占用。
- 摘要未提供足够信息说明与基线比较的完整实验设置、数据集、评价指标和数值结果。
- 摘要未提供足够信息说明场景特定训练的成本、所需训练数据规模以及泛化能力的边界。
- 摘要未提供足够信息说明该方法是否依赖特定 3DGS 变体或对高斯属性有哪些假设。

### 阅读优先级
高。理由：该论文针对 3DGS 中排序与有序 alpha 混合这一关键效率瓶颈，提出无需排序的渲染思路，并同时覆盖稀疏采样去噪、移动端交互渲染与场景泛化等实用性目标；若关注 3DGS 渲染加速、顺序无关渲染或时空重建，摘要显示其具有较强的问题针对性和潜在应用价值。

</details>

<details>
<summary>Abstract</summary>

Conventional 3D Gaussian Splatting (3DGS) requires depth sorting and ordered alpha blending to correctly render overlapping Gaussian primitives. Stochastic transparency enables sorting-free rendering by replacing fractional alpha contributions with discrete stochastic visibility samples, but produces substantial spatial and temporal noise at low sample counts. We refer to this conversion from continuous Gaussian splats to discrete visibility samples as \textit{Gaussian Stippling}. Based on this, we present an efficient order-independent rendering and reconstruction framework that operates directly on unmodified 3DGS assets. Our method adaptively integrates primitive-based and fragment-based stippling, leveraging their complementary strengths across different rendering regimes to significantly improve rendering throughput. To recover high-quality images from sparse stochastic samples, we further introduce a lightweight Gaussian-aware spatiotemporal reconstruction network. By exploiting the Gaussian attributes retained by each stipple, the network aggregates structured stochastic clues across both space and time, effectively suppressing stippling noise. Experiments show that our hybrid Gaussian stippling method, coupled with a spatiotemporal reconstruction network trained on diverse scenes, generalizes to unseen scenes and enables interactive, temporally stable, and visually plausible rendering on mobile devices without retraining or preprocessing. With scene-specific training and appropriately scaled sampling and network capacity, our method further outperforms the baselines in visual quality, offering a high-fidelity configuration for quality-prioritized applications.

</details>

#### 2026-09-29 - ORMA: Optimization-based Monocular 4D Reconstruction of Articulated Animals

**Authors:** Xuyi Hu, Francesco Palandra, Shangzhe Wu, Daniel Cremers, Riccardo Marin, Silvia Zuffi
**Links:** [abs](https://arxiv.org/abs/2609.37986) - [pdf](https://arxiv.org/pdf/2609.37986)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, shape reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ORMA: Optimization-based Monocular 4D Reconstruction of Articulated Animals
- 作者：Xuyi Hu, Francesco Palandra, Shangzhe Wu, Daniel Cremers, Riccardo Marin, Silvia Zuffi
- 出版日期：2026-09-29T16:49:01Z
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2609.37986 ；PDF：https://arxiv.org/pdf/2609.37986

### 一句话总结
ORMA 是一个无需训练的单目视频四足动物 4D 重建框架，通过将关节运动与形状解耦，并借助生成式 3D 先验与优化过程，提升对分布外物种的几何重建准确性和全局一致的运动恢复。

### 研究问题
从单目视频中恢复动物的关节式 4D 表示仍然困难，主要原因包括四足动物形态多样性大，以及缺乏动物 4D 监督数据。现有基于学习的方法通常处理单张图像，并依赖合成数据或模型拟合的 3D 监督，这继承了强参数化先验的限制，降低了对分布外物种的泛化能力。当应用于分布外动物时，这类方法往往能恢复看似合理的姿态，但由于底层形状模型无法忠实表示观察到的实例，几何重建不准确。

### 核心思路/方法
ORMA 是一个无需训练的重建框架，核心是解耦关节运动与形状：
- 使用预测姿态作为优化参考；
- 利用生成式 3D 先验进行准确形状重建；
- 给定参考图像，重建动物几何，并将其配准到参数化模型 SMAL+，得到适应观察实例的关节式形状；
- 结合逐帧关节姿态估计与全局一致的相机姿态，在共享世界坐标系中恢复动物运动；
- 使用自监督 DINO 对应关系和时序一致性进一步优化重建。

### 主要贡献
- 提出 ORMA：无需训练的单目动物 4D 重建框架，将关节与形状解耦，并利用生成式 3D 先验提升形状重建。
- 通过参考图像重建几何并配准到 SMAL+，获得适应具体实例的关节式形状。
- 结合逐帧关节姿态与全局一致相机姿态，在共享世界坐标系中恢复动物运动。
- 利用自监督 DINO 对应和时序一致性进行进一步优化。
- 提出 PAW4D：一个合成多物种基准，包含真实 3D 几何和相机运动，用于定量评估。
- 在 PAW4D、PFERD 和挑战性野外视频上的实验表明，ORMA 提升了重建精度，并在多种四足物种中恢复全局一致的运动。

### 局限性
摘要未提供足够信息。摘要未说明方法对特定物种、遮挡、快速运动、视频长度、计算成本或失败案例的具体限制。

### 阅读优先级
高。理由：该论文针对单目动物 4D 重建中的泛化与几何准确性问题，提出无需训练框架并引入新基准 PAW4D；若关注动态 / 4D 重建、动物建模、生成式先验与优化结合等方向，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering articulated 4D representations of animals from monocular videos remains challenging due to the large diversity of quadruped morphologies and lack of animal 4D supervision data. Existing learning-based reconstruction methods operate on individual images and rely on synthetic or model-fitted 3D supervision, which inherits the constraints of strong parametric priors and limits generalization to out-of-distribution species. When applied to out-of-distribution animals, they often recover a plausible pose while producing inaccurate geometry because the underlying shape model cannot faithfully represent the observed instance. We present ORMA, a training-free reconstruction framework that decouples articulation from shape, using the predicted pose as reference for optimization while leveraging generative 3D priors for accurate shape reconstruction. Given a reference image, we reconstruct the animal geometry and register it to the parametric model SMAL+, yielding an articulated shape adapted to the observed instance. We then combine per-frame articulated pose estimates with globally consistent camera poses to recover animal motion in a shared world coordinate frame, and further refine the reconstruction using self-supervised DINO correspondences and temporal consistency. To enable quantitative evaluation, we introduce PAW4D, a synthetic multi-species benchmark with ground-truth 3D geometry and camera motion. Experiments on PAW4D, PFERD, and challenging in-the-wild videos demonstrate that ORMA improves reconstruction accuracy while recovering globally consistend animal motion across diverse quadruped species.

</details>

#### 2026-09-28 - RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts

**Authors:** Jin Hyun Kim, Min Young Kim, Soohwan Song, Daekyum Kim
**Links:** [abs](https://arxiv.org/abs/2609.35311) - [pdf](https://arxiv.org/pdf/2609.35311)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, 4D Gaussian, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts
- 作者：Jin Hyun Kim, Min Young Kim, Soohwan Song, Daekyum Kim
- 出版日期：2026-09-28T14:46:58Z
- 分类：Dynamic / 4D Reconstruction；次要分类：Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.35311 ；PDF https://arxiv.org/pdf/2609.35311

### 一句话总结
RoGSW4RLD 以前馈式两阶段框架，将多相机机器人世界模型产生的视频预测提升为统一的、可随时间查询的度量 4D 高斯场。

### 研究问题
动作条件视频世界模型能够从多相机预测未来机器人交互，但其输出仍是彼此分离的视频集合，而非可在不同视角和时间上查询的共享度量场景。现有 4D 重建方法虽然可用于空间化这些预测，但独立重建并合并各相机流无法保证跨视角一致性；当移动的机器人搭载相机与固定外部视角混合时，这一问题尤为严重。摘要未提供更多关于问题定义边界或适用范围的细节。

### 核心思路/方法
- 提出 RoGSW4RLD，一个前馈框架，将同步多相机 rollout 提升为统一的、可随时间查询的度量 4D 高斯场。
- 不学习单独的几何转移模型，而是直接重建现有世界模型生成的视觉未来。
- 核心为两阶段架构：
  - 阶段 1：融合跨视角证据与机器人特定的铰接几何和运动学，联合形成度量 4D 场。
  - 阶段 2：细化场的几何与外观，同时严格保持初始时间位移。

### 主要贡献
- 提出面向机器人世界模型 rollout 的前馈式 4D 高斯提升框架，将多相机视频预测统一为可跨视角与时间查询的度量 4D 表示。
- 设计两阶段架构，在阶段 1 融合跨视角证据与机器人铰接几何/运动学，在阶段 2 细化几何与外观并保持时间位移。
- 在 256 个留出的 DROID episode 上评估，相比逐相机重建加校准合并，新视角 PSNR 提升 2.15 dB，深度 AbsRel 降低 47%，机器人位移误差降低 61%。
- 在动作条件 Cosmos 3 rollout 上同样获得稳健增益，表明预测的视频未来可被转化为一致、可空间查询的 4D 度量表示。
- 摘要未提供足够信息说明其具体网络结构、训练损失、数据预处理细节或计算成本。

### 局限性
- 摘要未提供足够信息说明方法在极端视角变化、遮挡、动态物体复杂性或长时序下的表现。
- 摘要未提供足够信息说明对世界模型预测误差的敏感性与鲁棒性。
- 摘要未提供足够信息说明评测是否覆盖真实机器人闭环控制或仅限离线指标。
- 摘要未提供足够信息说明计算资源、推理速度与实时性。
- 摘要未提供足够信息说明与其他 4D 重建方法的全面对比范围。

### 阅读优先级
高。理由：该工作直接针对机器人世界模型输出难以跨视角、跨时间统一查询的问题，提出前馈 4D 高斯提升与两阶段融合思路，并在摘要中给出明确的定量提升；主题同时涉及动态/4D 重建、神经场景表示与机器人/具身应用，属于交叉热点，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Action-conditioned video world models predict future robot interactions from multiple cameras, yet their outputs remain disparate video collections rather than a shared metric scene queryable across viewpoints and time. While existing 4D reconstruction methods offer a path to spatialize these predictions, independently reconstructing and merging each camera stream fails to enforce cross-view consistency. This limitation is particularly detrimental when combining moving robot-mounted cameras with fixed external views. To address this, we introduce RoGSW4RLD, a feed-forward framework that lifts synchronized multi-camera rollouts into a unified, time-queryable metric 4D Gaussian field. Rather than learning a separate geometric transition model, RoGSW4RLD directly reconstructs the visual future generated by existing world models. Its core innovation is a two-stage architecture: Stage 1 jointly forms the metric 4D field by fusing cross-view evidence with robot-specific articulated geometry and kinematics, while Stage 2 refines the field's geometry and appearance while strictly preserving the initial temporal displacements. Evaluated on 256 held-out DROID episodes, RoGSW4RLD significantly outperforms camera-wise reconstruction with calibrated merging, improving novel-view PSNR by 2.15 dB, reducing depth AbsRel by 47%, and lowering robot displacement error by 61%. These robust gains extend to action-conditioned Cosmos 3 rollouts, demonstrating that predicted video futures can be successfully translated into consistent, spatially queryable 4D metric representations.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-01 - DecomVoxel: Harnessing 3D-Native Priors with Guided In-situ Denoising Optimization for Decompositional Scene Reconstruction

**Authors:** Junfeng Ni, Zirui Zhou, Yixin Chen, Yu Liu, Nan Jiang, Zhifei Yang, Song-Chun Zhu, Siyuan Huang
**Links:** [abs](https://arxiv.org/abs/2610.01914) - [pdf](https://arxiv.org/pdf/2610.01914)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DecomVoxel: Harnessing 3D-Native Priors with Guided In-situ Denoising Optimization for Decompositional Scene Reconstruction
- 作者：Junfeng Ni, Zirui Zhou, Yixin Chen, Yu Liu, Nan Jiang, Zhifei Yang, Song-Chun Zhu, Siyuan Huang
- 出版日期：2026-10-01T15:54:23Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要链接：https://arxiv.org/abs/2610.01914 ；PDF：https://arxiv.org/pdf/2610.01914 ；代码：https://github.com/DecomVoxel/DecomVoxel

### 一句话总结
DecomVoxel 将物体补全表述为一种引导式的原位去噪优化，把 3D 原生先验与神经场景重建结合，以提升重遮挡下分解式场景重建的质量。

### 研究问题
论文关注分解式场景重建，即同时重建高质量物体与背景。摘要指出，现有方法在严重遮挡条件下仍难以达到理想质量。生成式先验被视为潜在解决方案，但存在两类问题：基于 2D 图像的先验由于缺乏 3D 感知，常出现多视角不一致；3D 原生先验虽具有更强的结构归纳偏置，却容易在复杂场景中导致空间漂移和错位。

### 核心思路/方法
论文提出 DecomVoxel，将物体补全建模为“引导式原位去噪优化”（guided in-situ denoising optimization），用于连接 3D 原生先验与神经场景重建。方法层面，摘要提到两项关键设计：
1. 重新表述的基于 epsilon 的蒸馏损失（reformulated epsilon-based distillation loss），用于确保稳定的潜在细化；
2. 自适应空间引导（adaptive spatial guidance），利用已占据锚点与空置锚点并结合时间退火，以抑制生成式幻觉并缓解空间漂移。

### 主要贡献
- 提出 DecomVoxel，面向分解式场景重建，将物体补全表述为引导式原位去噪优化，以桥接 3D 原生先验与神经场景重建。
- 引入重新表述的基于 epsilon 的蒸馏损失，以保障稳定的潜在细化。
- 设计自适应空间引导，结合已占据/空置锚点与时间退火，用于抑制生成式幻觉和缓解空间漂移。
- 在 Replica 与 ScanNet++ 上报告实验，称 DecomVoxel 显著优于当前最优方法，同时忠实保留原始空间布局、结构保真度与风格一致的纹理；并称其可输出具有干净拓扑、几何与外观的高质量带纹理网格。

### 局限性
摘要未提供足够信息。摘要未给出失败案例、适用边界、计算开销、对特定数据集或先验模型的依赖程度，也未说明方法在何种场景下可能失效。

### 阅读优先级
高。理由：该论文聚焦 3D 重建与多视角几何中的分解式场景重建问题，明确针对重遮挡、2D 先验多视角不一致与 3D 原生先验空间漂移等关键矛盾，并提出具体方法设计与公开代码；若关注生成式先验与神经场景重建结合、遮挡下物体补全或高质量网格重建，该工作具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Decompositional scene reconstruction aims to reconstruct high-quality objects and background, yet existing methods still struggle with the level of quality under heavy occlusions. While generative priors offer a potential solution, 2D image-based priors often suffer from multi-view inconsistency due to a lack of 3D awareness. Conversely, 3D-native priors provide stronger structural inductive biases but frequently lead to spatial drift and misalignment within complex scenes. To address these issues, we propose DecomVoxel, formulating object completion as a guided in-situ denoising optimization that bridges 3D-native priors with neural scene reconstruction. Our framework introduces a reformulated epsilon-based distillation loss to ensure stable latent refinement, alongside adaptive spatial guidance that utilizes occupied and vacant anchors with temporal annealing to suppress generative hallucinations and mitigate spatial drift. Experiments on Replica and ScanNet++ show that DecomVoxel significantly outperforms state-of-the-art methods while faithfully preserving the original spatial layout, structural fidelity, and style-consistent texture. Our method pushes the boundary of decompositional reconstruction by delivering high-quality textured meshes with clean topology, geometry, and appearance, providing a robust solution for the decompositional reconstruction of complex real-world scenes. Code is available at https://github.com/DecomVoxel/DecomVoxel.

</details>

#### 2026-10-01 - Towards Physical Underwater Robotic Assistance for Scuba Diver Movement in Confined Spaces

**Authors:** Demetrious T. Kutzke, Junaed Sattar
**Links:** [abs](https://arxiv.org/abs/2610.01906) - [pdf](https://arxiv.org/pdf/2610.01906)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Towards Physical Underwater Robotic Assistance for Scuba Diver Movement in Confined Spaces
- 作者：Demetrious T. Kutzke, Junaed Sattar
- 出版日期：2026-10-01T15:50:23Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类信息
- 链接：[摘要](https://arxiv.org/abs/2610.01906) / [PDF](https://arxiv.org/pdf/2610.01906)

### 一句话总结
论文提出并初步验证了一种可穿戴水下机器人 RADMCS，通过推进器驱动的方向引导与触觉反馈，帮助潜水员在受限空间中与海底结构保持固定距离。

### 研究问题
水肺潜水员通常被训练控制深度以避免快速上升或下降带来的严重伤害，如气体栓塞和气压伤。但许多水下任务还需要横向控制，即与珊瑚礁、水下钻探仪器或未爆炸弹药等海底结构保持距离。论文关注的核心问题是：如何通过可穿戴机器人系统，为潜水员提供方向性物理辅助，以帮助其在受限空间中维持与海底结构的距离。

### 核心思路/方法
论文提出 RADMCS（Robotic Assisted Diver Movement in Confined Spaces），一种可穿戴机器人方案，其特点是通过推进器驱动提供方向引导，而不是像已有推进辅助外骨骼那样提供推进助力。该系统利用单目深度估计等感知技术，并结合潜水推进器的力反馈，向潜水员提供触觉反馈，从而辅助其与海底结构保持固定距离。系统体积小、结构紧凑，被定位为一个可扩展的基础平台，未来可加入更复杂的控制与导航行为。

### 主要贡献
- 提出一种面向水肺潜水员的可穿戴机器人方案，通过推进器驱动提供方向引导，区别于既往的推进辅助外骨骼。
- 引入 RADMCS 系统，利用单目深度估计和潜水推进器力反馈，为潜水员提供触觉反馈，以辅助维持与海底结构的距离。
- 报告了 IRB 水下研究结果，涉及八名人类水肺潜水员参与者，包括封闭水域游泳设施和海洋环境中的阈值敏感性测试、封闭水域中的距离保持实验，以及海洋中的形态、适配和功能测试。
- 结果表明，相对较低的推力值（最大值的 10%）即可利用机器人引导的物理感受来引导人类运动方向。

### 局限性
- 论文的长期目标或更复杂控制与导航行为的可行性，摘要仅将其描述为“可扩展的基础平台”，未提供具体验证结果。
- 除“八名人类水肺潜水员参与者”和实验场景类型外，摘要未提供参与者人口统计信息、实验样本量细节、统计分析方法或具体性能指标。
- 摘要未提供单目深度估计的具体精度、触觉反馈的量化效果、不同环境下的对比数据或失败案例。
- 摘要未提供系统的续航、成本、鲁棒性或安全性评估。
- 摘要未提供与已有推进辅助外骨骼的定量比较。
- 摘要未提供代码、数据集或硬件设计的开放获取信息。
> 摘要未提供足够信息，以上局限中涉及未提及内容的条目均无法从摘要中进一步确认。

### 阅读优先级
中。理由：该论文提出了一个具有明确应用场景的水下可穿戴机器人系统，并包含 IRB 人体水下实验，涉及八名潜水员，主题具有一定新颖性和实践意义。但摘要未给出具体性能指标、统计结果或与已有方法的定量对比，且主分类为 3D Reconstruction & Multi-view Geometry，与水下机器人辅助这一主题的常规归类存在差异。若读者关注水下人机交互、可穿戴机器人和潜水辅助技术，该论文值得阅读；若需要详细的实验数据和系统评估，则需查阅全文。

</details>

<details>
<summary>Abstract</summary>

Scuba divers are taught to control their depth to avoid rapid ascents and descents, which could result in serious injuries such as gas embolisms and barotrauma. However, many underwater tasks necessitate lateral control, maintaining distance between subsea structures such as coral reefs, submerged drilling instrumentation, or unexploded ordnance. In this work, we discuss a first-of-its-kind wearable robotic solution providing thruster-actuated directional guidance to a diver, as distinct from prior propulsive-assistance exoskeletons. We introduce ``Robotic Assisted Diver Movement in Confined Spaces'' (RADMCS), a wearable robot that assists divers in maintaining a fixed distance from subsea structures by leveraging perception techniques in monocular depth estimation and force-feedback from submersible thrusters to provide haptic feedback. Its small and compact form factor creates a foundational platform that could be expanded to include more sophisticated control and navigation behaviors. We present results from Institutional Review Board (IRB) in-water studies with eight human scuba diver participants on threshold sensitivity tests in both a closed-water swimming facility and ocean environments; distance-maintaining experiments in a closed-water facility; and form, fit, and function testing in the ocean. We demonstrate that relatively low thrust values (10 percent of maximum) allow robotic direction of a human's movement using the physical sensation of the robot's guidance.

</details>

#### 2026-10-01 - LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction

**Authors:** Zhening Huang, Yueyan Li, Johnathan Chiu, Xiaoyang Lyu, Matt Zhou, Yuxin Yao, Joan Lasenby, Shangzhe Wu
**Links:** [abs](https://arxiv.org/abs/2610.01863) - [pdf](https://arxiv.org/pdf/2610.01863)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, scene reconstruction, embodied AI, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction
- 作者：Zhening Huang, Yueyan Li, Johnathan Chiu, Xiaoyang Lyu, Matt Zhou, Yuxin Yao, Joan Lasenby, Shangzhe Wu
- 出版日期：2026-10-01T15:25:35Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.01863；PDF https://arxiv.org/pdf/2610.01863；代码 https://github.com/LiteReality/LiteReality-Agent/

### 一句话总结
LiteReality-Agent 将 RGB-D 室内场景的三维重建建模为一个“编码问题”，通过编码智能体调用专用工具、迭代编辑可执行的 Python 脚本 Room.py，生成具有铰接结构、可直接用于仿真的室内三维数字孪生。

### 研究问题
如何从 RGB-D 扫描中重建真实室内环境，使其成为真实感强、具有铰接结构、且可直接用于仿真的三维场景。摘要指出，该工作面向真实到仿真（real-to-sim）的需求，并强调与近期前沿模型（如 Astra 和 Fable）的生成结果相比，需要在几何精度、视觉真实感和仿真兼容性上取得更好表现。

### 核心思路/方法
- 将三维重建表述为编码问题：由一个编码智能体使用专用工具收集证据，并迭代编辑一个 Python 脚本 Room.py。
- 执行 Room.py 可生成房间的三维数字孪生。
- 开发了稳健的 observe-edit-verify（观察—编辑—验证）框架，在重建全过程中支持证据收集、测量、验证、布局优化、仿真就绪和质量控制。
- 系统定位为一个编排框架：随着智能体能力提升，可为未来智能体提供专用工具、结构化工作流和稳健的验证机制，以提升重建质量与可靠性。

### 主要贡献
- 提出 LiteReality-Agent，一个面向可交互三维室内场景重建的智能体系统，可从 RGB-D 扫描生成真实、铰接、仿真就绪的三维场景。
- 将三维重建形式化为编码问题，并围绕可执行的 Room.py 脚本构建智能体工作流。
- 设计 observe-edit-verify 框架，覆盖证据收集、测量、验证、布局优化、仿真就绪与质量控制。
- 摘要声称其重建结果在几何精度、视觉真实感和仿真兼容性上优于近期前沿模型 Astra 与 Fable。
- 将系统定位为稳健 real-to-sim 系统的实用且重要的构建模块，并公开源代码与数据采集应用。

### 局限性
- 摘要未提供足够信息说明系统在何种扫描条件、场景类型或硬件配置下会失效。
- 摘要未提供足够信息说明其定量实验结果、评测指标、数据集规模和基线对比细节。
- 摘要未提供足够信息说明 observe-edit-verify 框架各模块的具体实现与计算开销。
- 摘要未提供足够信息说明对智能体能力（如编码模型能力）的依赖程度及其失败模式。
- 摘要未提供足够信息说明“仿真就绪”的具体判定标准与下游具身 AI 任务验证情况。

### 阅读优先级
高。理由：该论文处于三维重建与具身/机器人应用的交叉方向，提出将重建转化为智能体编码任务的新范式，并声称在几何精度、视觉真实感和仿真兼容性上优于前沿模型；同时公开代码与数据采集应用，对 real-to-sim、具身 AI 和三维场景重建研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

We present LiteReality-Agent, an agentic system for reconstructing real indoor environments as realistic, articulated, and simulation-ready 3D scenes from RGB-D scans. At its core, LiteReality-Agent formulates 3D reconstruction as a coding problem, in which a coding agent gathers evidence using specialised tools and iteratively edits a Python script, Room.py, which can be executed to produce a 3D digital twin of the room. With this formulation, we develop a robust observe-edit-verify harness that supports evidence gathering, measurement, verification, layout optimisation, simulation readiness, and quality control throughout the reconstruction process. LiteReality-Agent produces high-quality reconstructions suitable for simulation and downstream embodied AI tasks. Furthermore, as agent capabilities continue to improve rapidly, the system introduced by LiteReality-Agent remains a strong orchestration framework for future agents: it equips them with specialised tools, structured workflows, and robust verification mechanisms that substantially improve reconstruction quality and reliability. We demonstrate that LiteReality-Agent produces reconstructions that are more geometrically accurate, visually realistic, and simulation-compatible than those generated by recent frontier models, such as Astra and Fable. We therefore view LiteReality-Agent as a practical and important building block for robust real-to-sim systems. Both the source code and the data-capture application are publicly available. Code:https://github.com/LiteReality/LiteReality-Agent/

</details>

#### 2026-10-01 - GenCOPE: Syn2Real Generalized Category-Level Object Pose Estimation for Robotic Picking

**Authors:** Jian Liu, Wei Sun, Zhenqi Dai, Hui Yang, Jian Xiao, Nicu Sebe, Na Zhao
**Links:** [abs](https://arxiv.org/abs/2610.01758) - [pdf](https://arxiv.org/pdf/2610.01758)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, manipulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GenCOPE: Syn2Real Generalized Category-Level Object Pose Estimation for Robotic Picking
- 作者：Jian Liu, Wei Sun, Zhenqi Dai, Hui Yang, Jian Xiao, Nicu Sebe, Na Zhao
- 出版日期：2026-10-01T14:20:38Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：abstract_url: https://arxiv.org/abs/2610.01758；pdf_url: https://arxiv.org/pdf/2610.01758；项目页: https://paperreview99.github.io/GenCOPE/

### 一句话总结
GenCOPE 面向机器人抓取场景，提出仅用合成数据训练、直接泛化到真实世界的类别级物体位姿估计方法，通过域不变表示学习与 2D-3D 交叉一致性学习缓解合成到真实的域差距。

### 研究问题
现有类别级物体姿态估计（COPE）虽然能泛化到类内未知物体，但在面对新物体类别时仍需耗费人力重新采集真实世界训练数据，限制了实际应用中的可扩展性。本文关注的问题是：能否实现合成到真实（Syn2Real）的广义 COPE，即模型只在渲染合成数据上训练，却能直接泛化到真实世界部署。核心挑战在于合成数据与真实数据之间存在显著域差距，尤其是纹理外观方面。

### 核心思路/方法
- 目标：通过学习域不变表示，捕捉同一类别内物体的语义共性，从而提升域泛化能力。
- 约束设计：引入 2D 和 3D 语义一致性约束，降低特征编码器对域特定特征的敏感性。
- 位姿回归框架：提出端到端的位姿回归框架，执行 2D-3D 交叉一致性学习，并利用密集跨模态融合进一步精炼位姿估计。
- 架构取向：考虑到真实机器人部署对简洁性和有效性的要求，模型仅依赖全局特征，形成高度轻量且高效的架构。
- 评测：在 REAL275 和 Wild6D 基准以及真实机器人操作场景上进行实验，展示其 Syn2Real 泛化性能。

### 主要贡献
- 提出面向 Syn2Real 广义类别级物体位姿估计的 GenCOPE 方法，目标是仅用合成数据训练并泛化到真实世界。
- 引入 2D 和 3D 语义一致性约束，以学习域不变表示并降低编码器对域特定特征的敏感性。
- 提出端到端位姿回归框架，结合 2D-3D 交叉一致性学习与密集跨模态融合来精炼位姿估计。
- 设计仅依赖全局特征的轻量高效架构，以适应真实机器人部署需求。
- 在 REAL275、Wild6D 及真实机器人操作场景中展示 Syn2Real 泛化性能，并发布代码与演示。

### 局限性
摘要未提供足够信息。摘要未说明方法在极端域差距、未见类别范围、计算资源需求、失败案例或真实机器人部署中的具体限制。

### 阅读优先级
高。理由：该论文聚焦机器人抓取中的类别级位姿估计，并针对实际应用中真实数据采集成本高的问题提出 Syn2Real 泛化方案；同时涉及域不变表示、2D-3D 跨模态一致性和轻量部署，主题与机器人 3D 场景理解及具身应用高度相关。若关注机器人抓取、Sim2Real/Syn2Real 泛化或类别级位姿估计，该文具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

Category-level object pose estimation (COPE), capable of generalizing to intra-class unknown objects, has become a core technique for robotic 3D scene understanding. However, existing COPE methods still require labor-intensive recollection of real-world training data for novel object categories, which limits their scalability in practical applications. This paper aims to achieve synthetic-to-real (Syn2Real) generalized COPE, where a model is trained solely on rendered synthetic data and directly generalized to real-world deployments. The central challenge lies in the significant domain gap between synthetic and real-world data, particularly in texture appearance. To address this, we aim to enhance domain generalization by learning domain-invariant representations that capture semantic commonalities among objects within the same category. We introduce 2D and 3D semantic consistency constraints to reduce the sensitivity of feature encoders to domain-specific features. In addition, we propose an end-to-end pose regression framework that performs 2D-3D cross consistency learning, leveraging dense cross-modality fusion to further refine pose estimation. Since simplicity and effectiveness are essential for real-world robotic deployment, our model operates exclusively on global features, yielding a highly lightweight and efficient architecture. Extensive experiments on the REAL275 and Wild6D benchmarks, as well as real-world robotic manipulation scenes, show superior Syn2Real generalization performance of our paradigm. Code and demos are released at https://paperreview99.github.io/GenCOPE/.

</details>

#### 2026-10-01 - MEGA: Object-Level Mesh Extraction from 3D Gaussian Splatting via Spatial Visual Distillation

**Authors:** Liwei Liao, Yingkui Zhang, Qianqian Tong, Ronggang Wang
**Links:** [abs](https://arxiv.org/abs/2610.01707) - [pdf](https://arxiv.org/pdf/2610.01707)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** mesh reconstruction, surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MEGA: Object-Level Mesh Extraction from 3D Gaussian Splatting via Spatial Visual Distillation
- 作者：Liwei Liao, Yingkui Zhang, Qianqian Tong, Ronggang Wang
- 出版日期：2026-10-01T13:52:12Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.01707 ；https://arxiv.org/pdf/2610.01707

### 一句话总结
MEGA 提出一种“先分割、后建网格”的框架，通过空间视觉蒸馏（SVD）与掩码引导的神经表面重建模块，从复杂 3DGS 场景中提取对象级、水密（watertight）的网格。

### 研究问题
从 3D Gaussian Splatting（3DGS）中提取网格，旨在为 3D 高斯赋予准确几何结构，实现显式且精确的 3D 占用表示。但现有方法主要聚焦场景级网格提取，无法表示对象级占用，且常导致非水密表面。因此，论文关注的问题是如何从复杂 3DGS 场景中提取对象级、水密的网格。

### 核心思路/方法
论文提出 MEGA（Mesh Extraction from GAussians），是一个“segment-then-mesh”（先分割、后建网格）框架，用于从复杂 3DGS 场景中提取对象级、水密网格。其核心包括：
- 空间视觉蒸馏（Spatial Visual Distillation, SVD）：将 3DGS 模型视为教师模型，采样多样相机位姿，并渲染每个已分割对象对应的视图；这些观测随后通过光度监督用于训练网格重建模型。
- 掩码引导的神经表面重建模块：与 SVD 共同构成方法核心，用于从上述观测中重建对象级网格。

### 主要贡献
- 提出 MEGA，一个面向复杂 3DGS 场景的“segment-then-mesh”框架，用于提取对象级、水密网格。
- 引入空间视觉蒸馏（SVD），将 3DGS 作为教师模型，通过采样相机位姿并渲染分割对象视图，以光度监督方式训练网格重建模型。
- 结合掩码引导的神经表面重建模块，实现对对象级占用的恢复。
- 根据摘要，在多个广泛使用基准上的大量实验表明，MEGA 在恢复准确的对象级 3D 占用方面达到 state-of-the-art 性能。
- 摘要称 MEGA 通过结合高质量对象级网格（用于几何占用）与 3DGS 表示（用于照片级真实感渲染），支持复杂物理交互。

### 局限性
- 摘要未提供足够信息说明方法在计算开销、训练时间、内存占用方面的限制。
- 摘要未提供足够信息说明其对分割质量、相机采样策略或复杂场景类型的依赖与失败情形。
- 摘要未提供足够信息说明实验基准、评价指标、对比方法及消融实验的具体细节。
- 摘要未提供足够信息说明“复杂物理交互”的具体实现方式、验证场景与定量结果。

### 阅读优先级
高。理由：该论文聚焦 3DGS 到对象级水密网格提取这一明确且重要的问题，提出“segment-then-mesh”框架与空间视觉蒸馏思路，并声称在对象级 3D 占用上达到 state-of-the-art；若研究兴趣涉及 3D 重建、神经场景表示、3DGS 几何提取或对象级占用，值得优先阅读。但需注意，当前仅基于摘要，具体实验细节与局限需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Mesh extraction from 3D Gaussian Splatting (3DGS) aims to endow 3D Gaussians with accurate geometric structures, enabling explicit and precise 3D occupancy. However, existing methods primarily focus on scene-level mesh extraction, making them unable to represent object-level occupancy and often resulting in non-watertight surfaces. To overcome these limitations, we propose \textbf{MEGA} (\underline{M}esh \underline{E}xtraction from \underline{GA}ussians), a ``segment-then-mesh'' framework for extracting object-level, watertight meshes from complex 3DGS scenes. At the core of MEGA are \textbf{Spatial Visual Distillation (SVD)} and a mask-guided neural surface reconstruction module. SVD treats the 3DGS model as a teacher, sampling diverse camera poses and rendering the corresponding views of each segmented object. These observations are then used to train a mesh reconstruction model through photometric supervision. Extensive experiments on several widely used benchmarks demonstrate that MEGA achieves state-of-the-art performance in recovering accurate object-level 3D occupancy. Moreover, MEGA enables complex physical interactions by combining high-quality object-level meshes for geometric occupancy with 3DGS representations for photorealistic rendering.

</details>

#### 2026-10-01 - The Impact of Processing Parameters on High-Accuracy Measurements in UAV Photogrammetry

**Authors:** Paweł Ćwiąkała, Edyta Puniach, Elżbieta Pastucha, Wojciech Gruszczyński
**Links:** [abs](https://arxiv.org/abs/2610.01438) - [pdf](https://arxiv.org/pdf/2610.01438)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** photogrammetry, camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：The Impact of Processing Parameters on High-Accuracy Measurements in UAV Photogrammetry
- 作者：Paweł Ćwiąkała, Edyta Puniach, Elżbieta Pastucha, Wojciech Gruszczyński
- 出版日期：2026-10-01T10:34:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.01438) / [PDF](https://arxiv.org/pdf/2610.01438)

### 一句话总结
该研究通过 768 种处理变体的全因子实验，系统评估了 Bundle Block Adjustment 参数设置对 UAV 摄影测量 3D 精度及变形指标确定精度的影响。

### 研究问题
UAV 摄影测量被越来越多地用于滑坡、采矿、微地形变化等需要高精度的场景。虽然采集策略已被广泛研究，但处理流程——尤其是 Bundle Block Adjustment 参数设置——对最终精度的影响仍缺乏充分探索。本研究针对这一空白，考察处理参数如何影响最终 3D 精度以及位移、倾斜变化和水平应变确定的精度。

### 核心思路/方法
- 采用系统性、全因子评估方法，对 768 种处理变体进行测试。
- 数据基础为 1.5 年内、在 220 公顷研究区采集的十组 UAV 数据集。
- 分析了八个关键参数。
- 评估处理流程优化对位移、倾斜变化和水平应变确定精度的影响。
- 将优化配置与作者此前使用的基线配置进行对比。

### 主要贡献
- 揭示了最终 3D 精度存在显著变异性：最佳变体 RMSE 为 16 mm，最弱变体达到 303 mm。
- 识别出最具影响力的因素：地面控制点数量、附加相机标定校正的应用，以及使用 Post-Processing Kinematic GNSS 方法确定相机投影中心坐标。
- 在变形指标方面，随机位移误差保持稳定（RMSE 约 6–7 mm）；系统误差在所有轴上降低超过一半，垂直中位绝对误差从 14 mm 降至 7 mm（优化配置相较基线）。
- 据摘要所述，这是首个大规模、面向实践的处理参数选择对摄影测量产品和变形指标确定精度影响的评估，并为构建更稳健、可重复的高精度 UAV 摄影测量工作流提供可操作指导。

### 局限性
- 摘要未提供足够信息说明研究区具体地形、气候或地表覆盖条件对结论外推性的限制。
- 摘要未提供足够信息说明 768 种变体是否存在参数交互效应的详细统计显著性分析。
- 摘要未提供足够信息说明除 RMSE、中位绝对误差外的其他精度评价指标或验证方式。
- 摘要未提供足够信息说明该方法在非 220 公顷研究区、非 1.5 年数据跨度场景下的泛化能力。

### 阅读优先级
高。理由：该研究直接针对 UAV 摄影测量高精度应用中处理参数选择这一实践痛点，实验规模大（768 种变体、十组数据集、1.5 年跨度），量化了最佳与最差配置间的巨大精度差异（16 mm vs 303 mm），并给出可操作的工作流优化方向，对从事高精度变形监测、3D 重建和摄影测量流程设计的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Unmanned aerial vehicle (UAV) photogrammetry is increasingly used in applications requiring high accuracy, such as determining ground surface changes caused by landslides, mining, or microrelief transformation. While acquisition strategies have been widely studied, the influence of the processing workflow-particularly Bundle Block Adjustment parameter settings-remains insufficiently explored. This study addresses this gap through a systematic, full-factorial evaluation of 768 processing variants applied to ten UAV datasets collected over 1.5 years in a 220 ha study area. Eight key parameters were analysed. The results show substantial variability in final 3D accuracy: the best performing variant achieved a root mean square error (RMSE) of 16 mm, whereas the weakest reached 303 mm. The most influential factors were the number of ground control points, the application of additional camera calibration corrections, and the use of the Post-Processing Kinematic GNSS method for determining camera projection center coordinates. The study also evaluates how workflow optimization affects the accuracy of displacement, tilt changes, and horizontal strain determination. While random displacement errors remained stable (RMSE of ~6-7 mm), systematic errors were significantly reduced by over half in all axes, with vertical median absolute error decreasing from 14 mm to 7 mm in the optimized configuration compared to the baseline previously used by the authors. This study provides the first large-scale, practice-oriented assessment of how processing parameter selection shapes the accuracy of both photogrammetric products and deformation indices determination. The results offer actionable guidance for developing more robust and repeatable UAV photogrammetry workflows tailored to high-precision monitoring.

</details>

#### 2026-10-01 - Resolving Mixed Single-Photon LiDAR Returns for Foreground-View and Hidden Scene Reconstruction

**Authors:** Ziting Wen, Runrong Deng, Zili Zhang, Haitao Zheng, Yuecong Xu, Xiaoqiang Ren, Guodong Shi, Kemi Ding
**Links:** [abs](https://arxiv.org/abs/2610.01206) - [pdf](https://arxiv.org/pdf/2610.01206)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, scene representation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Resolving Mixed Single-Photon LiDAR Returns for Foreground-View and Hidden Scene Reconstruction
- 作者：Ziting Wen, Runrong Deng, Zili Zhang, Haitao Zheng, Yuecong Xu, Xiaoqiang Ren, Guodong Shi, Kemi Ding
- 出版日期：2026-10-01T07:15:54Z
- 分类：3D Reconstruction & Multi-view Geometry（无二级分类）
- 链接：摘要页 https://arxiv.org/abs/2610.01206 ；PDF https://arxiv.org/pdf/2610.01206

### 一句话总结
提出一种状态感知框架，从被部分透射遮挡物混合的单光子 LiDAR 直方图中同时重建前景视图与被遮挡场景，并配套一个真实配对遮挡数据集。

### 研究问题
部分透射屏幕与防护罩在机器人巡检中十分常见，会使 LiDAR 同时接收到前景材料和其后场景的混合回波。传统基于峰值的 LiDAR 通常会丢弃较弱的隐藏回波；单光子 LiDAR 虽能记录保留衰减与重叠回波的时间分辨直方图，但现有瞬态重建方法通常只对测得波形拟合单一场景表示。在遮挡下，较弱或距离较近的前景—隐藏回波可能形成宽峰或微弱肩部；而这类波形同样可被“位移的单表面”或“较厚密度分布”解释，因此准确的瞬态拟合并不必然意味着几何正确。

### 核心思路/方法
- 面向被遮挡的单光子直方图，提出状态感知（state-aware）框架，用于前景视图与隐藏场景重建。
- 对每条光线估计局部回波证据，将回波状态判定为：无可可靠表面证据、单回波证据、双回波三类。
- 推断出的回波状态用于路由监督一个双头神经场（two-head neural field）：所有光线都约束波形重建，而可靠锚点提供几何定位。
- 同时引入一个真实配对单光子 LiDAR 遮挡数据集，在同一固定位姿下采集遮挡与干净（无遮挡）数据。

### 主要贡献
- 提出状态感知框架，从被遮挡单光子直方图中进行前景视图与隐藏场景重建。
- 通过逐光线回波证据估计（无可靠表面/单回波/双回波）来路由双头神经场的监督，以缓解“波形拟合正确但几何错误”的歧义。
- 引入真实配对单光子 LiDAR 遮挡数据集（固定位姿下的遮挡与干净采集）。
- 在真实数据集上的实验表明，相比基线方法，隐藏场景深度与点云精度有所提升；结果说明单光子分层重建是穿过部分透射遮挡物进行 3D 感知的可行路径。

### 局限性
- 摘要未提供足够信息说明方法的失效场景、适用遮挡物类型范围、对极端弱回波或强噪声的鲁棒性边界。
- 摘要未提供足够信息说明数据集的规模、场景多样性、采集设备与标注细节。
- 摘要未提供足够信息说明与基线方法的定量对比数值、评价指标定义及消融实验情况。
- 摘要未提供足够信息说明计算开销、实时性与可扩展性。

### 阅读优先级
高。理由：该工作针对“部分透射遮挡下的混合单光子回波”这一具有明确实际动机的问题，提出了状态感知与双头神经场相结合的重建思路，并配套真实配对数据集；对单光子 LiDAR、遮挡场景重建与 3D 感知方向的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Partially transmissive screens and protective covers are common in robotic inspection, but they create mixed LiDAR returns from both the foreground material and the scene behind it. Conventional peak-based LiDAR usually discards weak hidden returns, while single-photon LiDAR records time-resolved histograms that preserve attenuated and overlapping echoes. However, existing transient reconstruction methods typically fit a single scene representation to the measured waveform. Under occlusion, weak or nearby foreground--hidden echoes can form a broad peak or subtle shoulder. Because such waveforms can also be explained by a displaced single surface or a thick density distribution, accurate transient fitting does not necessarily imply correct geometry. We propose a state-aware framework for foreground-view and hidden scene reconstruction from occluded single-photon histograms. For each ray, we estimate local echo evidence, identifying no reliable surface evidence, single-return evidence, or two returns. The inferred echo state routes supervision for a two-head neural field: all rays constrain waveform reconstruction, while reliable anchors provide geometry localization. We also introduce a real paired single-photon LiDAR occlusion dataset with occluded and clean captures at fixed poses. Experiments on a real dataset show improved hidden scene depth and point-cloud accuracy over baselines. Our results demonstrate single-photon layered reconstruction as a practical route for 3D perception through partially transmissive occluders.

</details>

#### 2026-10-01 - Semantic RGB--Depth Based Surgical Skill Assessment in Microscopic Stereo Videos

**Authors:** Jecia Z. Y. Mao, Sue M. Cho, Francis X. Creighton, Deepa Galaiya, Russell H. Taylor, Manish Sahu
**Links:** [abs](https://arxiv.org/abs/2610.01205) - [pdf](https://arxiv.org/pdf/2610.01205)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** monocular depth, stereo depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Semantic RGB--Depth Based Surgical Skill Assessment in Microscopic Stereo Videos
- 作者：Jecia Z. Y. Mao, Sue M. Cho, Francis X. Creighton, Deepa Galaiya, Russell H. Taylor, Manish Sahu
- 出版日期：2026-10-01T07:15:49Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.01205

### 一句话总结
本文提出一种语义 RGB-Depth 框架，利用显微镜立体视频中的深度信息与语义分解的 RGB 流，通过分层注意力架构进行手术技能等级分类。

### 研究问题
显微外科技术技能的客观评估对基于能力的培训和质量保证至关重要，但现有基于视频的方法主要依赖 RGB 图像，忽略了器械—解剖结构交互的 3D 空间关系。虽然立体手术显微镜可提供互补的深度信息，但传统立体匹配算法在高放大成像条件下会产生稀疏且不可靠的深度估计，限制了其在自动化技能评估中的应用。

### 核心思路/方法
提出语义 RGB-Depth 手术技能评估框架。采用基于回归的深度融合方法，将稀疏的度量立体深度与密集的单目深度估计相结合，生成手术场景的密集几何表示。该表示与语义分解的 RGB 流（对应单个手术器械和周围解剖结构）相集成。使用分层注意力架构联合编码这些流，以捕捉不同培训水平外科医生在器械使用和器械—解剖结构交互方面的判别性模式。

### 主要贡献
- 提出语义 RGB-Depth 框架，将稀疏立体深度与密集单目深度融合为密集几何表示，用于显微立体视频的手术技能评估。
- 将几何表示与语义分解的器械及解剖结构 RGB 流结合，并通过分层注意力架构联合编码。
- 在 33 例离体经口显微喉部手术（6 名外科医生，包括主治医师和住院医师）上采用留一外科医生交叉验证进行评估：所提语义 RGB-Depth 模型的技能等级分类 F1 为 0.938，而语义 RGB 为 0.696，语义深度为 0.929。
- 学习的空间、时间和语义注意力模式可支持对模型关注区域、视频片段和语义流进行定性检查。

### 局限性
摘要未提供足够信息（如计算成本、实时性、跨机构泛化能力、深度估计误差的详细分析等均未提及）。

### 阅读优先级
高。理由：该工作针对显微外科技能评估中 RGB 方法忽略 3D 空间关系的问题，提出了明确的语义 RGB-Depth 融合方案，并在摘要中报告了相对语义 RGB 的显著 F1 提升（0.938 对 0.696），主题与 3D 重建及多视角几何分类相关，且涉及医学图像与技能评估交叉方向，具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Objective assessment of microsurgical technical skill is essential for competency-based training and quality assurance, yet existing video-based approaches predominantly rely on RGB images and therefore overlook the 3D spatial relationships that characterize instrument-anatomy interactions. Although stereo operating microscopes provide complementary depth information, conventional stereo matching algorithms can produce sparse and unreliable depth estimates under high-magnification imaging conditions, limiting their use for automated skill assessment. This work presents a semantic RGB-Depth framework for surgical skill assessment from microscopic stereo videos. A regression-based depth fusion method combines sparse metric stereo depth with dense monocular depth estimates to generate a dense geometric representation of the surgical scene. This representation is integrated with semantically decomposed RGB streams corresponding to individual surgical instruments and surrounding anatomy. A hierarchical attention architecture jointly encodes these streams to capture discriminative patterns of instrument use and instrument-anatomy interaction across surgeons at different training levels. The framework was evaluated on 33 ex vivo transoral microlaryngeal procedures performed by six surgeons, comprising attending surgeons and surgical residents, using leave-one-surgeon-out cross-validation. The proposed semantic RGB-Depth model achieved an F1 score of 0.938 for skill-level classification, compared with 0.696 for semantic RGB and 0.929 for semantic depth. These results suggest that geometric information can improve automated surgical skill assessment from microscopic stereo videos. The learned spatial, temporal, and semantic attention patterns also support qualitative examination of the scene regions, video segments, and semantic streams emphasized by the model.

</details>

#### 2026-10-01 - quARtet Marker: A 3D-Printable Multi-Tag Fiducial for Robust Near-Frontal Pose Estimation

**Authors:** Araki Wakiuchi, Hikaru Sasaki, Takamitsu Matsubara
**Links:** [abs](https://arxiv.org/abs/2610.01072) - [pdf](https://arxiv.org/pdf/2610.01072)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：quARtet Marker: A 3D-Printable Multi-Tag Fiducial for Robust Near-Frontal Pose Estimation
- 作者：Araki Wakiuchi, Hikaru Sasaki, Takamitsu Matsubara
- 出版日期：2026-10-01T05:13:15Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类；次要分类未提供）
- 链接：摘要页 https://arxiv.org/abs/2610.01072 ；PDF https://arxiv.org/pdf/2610.01072

### 一句话总结
提出一种可3D打印的多标签基准物 quARtet marker，通过在紧凑足迹内倾斜布置四个 AprilTag，使标记正面朝向相机时各标签仍处于非正面视角，从而提升近正面位姿估计的稳健性，并在三种布局间权衡位姿估计一致性与抓取性。

### 研究问题
实验室器具操作中，透明或反射物体的识别与定位较困难。编码平面基准标记是实用的改造方案：易于打印，且标记面保持平整、可抓取。然而单个平面标签在近正面视角下最不可靠，因为透视线索消失。非平面几何结构可恢复这些线索，但会侵入平行夹爪必须接触的平整表面。因此核心问题是：如何在不破坏可抓取平整面的前提下，改善近正面视角下的位姿估计可靠性。

### 核心思路/方法
核心思路是在一个紧凑足迹内倾斜多个标签，使标记即使正对相机，每个标签也被以非正面角度观测。

具体方法：
- 提出 quARtet marker，一种可3D打印的基准物，体现上述思路。
- 其四个倾斜 AprilTag 的所有被检测角点进入同一次 Perspective-n-Point（PnP）求解。
- 使用一套共享配置同时定义制造几何与检测器模型。
- 由于倾斜会占用平坦面积，提出三种布局，在位姿估计一致性与可抓取性之间权衡。

### 主要贡献
- 提出 quARtet marker 这一可3D打印的多标签基准物设计，通过倾斜多标签在近正面视角下保留透视线索。
- 采用统一 PnP 求解融合四个倾斜 AprilTag 的全部检测角点，并以共享配置连接制造几何与检测器模型。
- 提出三种布局，明确权衡位姿估计一致性与抓取性。
- 实验结果显示：在机器人参考系、同一装置、固定相机实验中，三种布局将平均正面朝向误差从单个平面标签的 2.18 度降至 0.24–0.47 度，均方根位置误差从 1.50 mm 降至 0.17–0.20 mm。
- 机器人搭载相机的位姿保持测试在闭环视觉反馈下确认了这种分离。
- 在相同条件下的摆落试验中，带平整接触条的两种布局约保留 2 mm 的抓取内滑动，而无平整条布局滑动约 100 mm。
- 在测试条件下支持一条规则：位姿估计一致性优先时选无平整条布局，标记面必须保持可抓取时选带平整条布局。

### 局限性
- 摘要未提供足够信息说明实验的具体硬件配置、相机型号、标记尺寸、工作距离范围等细节。
- 摘要未提供足够信息说明三种布局的完整几何参数与设计差异的量化描述。
- 摘要未提供足够信息说明透明或反射物体的实际实验结果；摘要仅提及这类物体是动机背景。
- 摘要未提供足够信息说明摆落试验的具体条件、次数与统计方差。
- 摘要未提供足够信息说明与其他非平面基准或替代方案的对比。
- 摘要未提供足够信息说明该方法是否适用于其他类型标签或更广泛的视角范围。

### 阅读优先级
中。理由：该工作针对近正面位姿估计这一明确痛点提出可3D打印的实用设计，并给出位姿误差与抓取滑动的定量结果及布局选择规则，对机器人操作与视觉基准设计有参考价值；但摘要未提供足够信息说明完整实验细节、消融与对比，若需深入评估方法泛化性与设计参数影响，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation of labware is difficult when transparent or reflective objects must be identified and localized. Coded planar fiducials are a practical retrofit: easy to print, they leave the marked face flat and graspable. Yet a single planar tag is least reliable in near-frontal views, where perspective cues fade. Non-planar geometries restore those cues but intrude on the flat face that a parallel-jaw gripper must contact. Our idea is to tilt multiple tags within one compact footprint, so that each tag is seen at a non-frontal angle even when the marker faces the camera. We propose the quARtet marker, a 3D-printable fiducial embodying this idea: all detected corners of its four tilted AprilTags enter one Perspective-n-Point solve, and a shared configuration defines the fabricated geometry and the detector model. Because tilting consumes flat area, its three layouts trade pose-estimation consistency against graspability. In robot-referenced, same-setup fixed-camera experiments, all three layouts reduced the mean frontal orientation error from 2.18 degree for a single planar tag to 0.24-0.47 degree and the root-mean-square position error from 1.50 to 0.17-0.20 mm. A robot-mounted-camera pose-hold test confirmed this separation under closed-loop visual feedback. In swing-down trials under identical conditions, the two layouts with flat contact strips retained the object with about 2 mm of in-grasp slip, whereas the layout without flat strips slipped by roughly 100 mm. For the tested conditions, the results support a rule: the layout without flat strips when pose-estimation consistency dominates, a layout with flat strips when the marked face must remain graspable.

</details>

#### 2026-10-01 - HierGF: Hierarchical Gaussian Fields via Geometry-perception Message Passing for Sparse-view 3D Reconstruction

**Authors:** Bi'an Du, Zhimin Zhang, Daizong Liu, Baoquan Chen, Wei Hu
**Links:** [abs](https://arxiv.org/abs/2610.01056) - [pdf](https://arxiv.org/pdf/2610.01056)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, AR, augmented reality, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HierGF: Hierarchical Gaussian Fields via Geometry-perception Message Passing for Sparse-view 3D Reconstruction
- 作者：Bi'an Du, Zhimin Zhang, Daizong Liu, Baoquan Chen, Wei Hu
- 出版日期：2026-10-01T04:50:55Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.01056 ；PDF https://arxiv.org/pdf/2610.01056

### 一句话总结
论文提出 HierGF（分层高斯场），从分层几何感知视角处理稀疏视角 3D 重建，通过将粗 3D 几何信息与额外 2D 生成先验转化为结构化伪监督，以缓解多视角一致性不足与欠采样区域结构缺失问题。摘要未提供足够信息说明其具体实验表现。

### 研究问题
论文关注稀疏视角 3D 重建这一多媒体应用场景，包括 AR/VR 内容创建、文化遗产数字化和部分机器人应用；这些场景中可能只有少量随机采集的视角可用。稀疏视角包含的 3D 信息有限，带来两个主要挑战：
1. 可用于匹配的图像过少，难以建立多视角一致性；
2. 视角覆盖不足导致欠采样区域信息缺乏，造成物体结构缺失。

摘要还指出，现有方法大多依赖有限的重投影误差和正则项，容易过拟合到单一视角，并出现跨视角外观不一致；在几何欠采样区域，它们常依赖启发式密度控制，缺乏可靠引导，往往导致模糊和结构空洞。

### 核心思路/方法
论文提出 Hierarchical Gaussian Fields（HierGF），从分层几何感知视角重新审视稀疏视角重建，目标是把有限观测转化为可靠的自生成监督，超越固定先验和启发式密度控制。

具体而言：
- 通过两阶段几何感知骨干网络，将粗 3D 几何信息和额外 2D 生成先验转化为结构化伪监督，从而在极少量输入视角下增强多视角一致性。
- 引入可学习置信度网络，引导梯度朝向跨视角一致的内容。
- 引入几何一致致密化模块，以改善多视角对齐和欠采样区域的重建。

摘要未提供足够信息说明该方法的网络结构细节、训练流程、损失函数形式或具体实现参数。

### 主要贡献
- 提出 HierGF，从分层几何感知角度处理稀疏视角 3D 重建问题。
- 将粗 3D 几何信息与额外 2D 生成先验转化为结构化伪监督，以增强极少输入视角下的多视角一致性。
- 引入可学习置信度网络，引导梯度朝向跨视角一致内容。
- 引入几何一致致密化模块，改善多视角对齐与欠采样区域重建。

摘要未提供足够信息说明其与现有方法的具体量化对比、消融实验结论或应用验证范围。

### 局限性
摘要未提供足够信息说明论文的局限性。摘要中未报告失败案例、计算开销、对先验质量的依赖程度、适用场景边界或实验未覆盖情况。

### 阅读优先级
中。理由：该论文聚焦稀疏视角 3D 重建这一明确且常见的问题，并提出分层几何感知、结构化伪监督、可学习置信度网络和几何一致致密化等思路；若读者关注 3D Reconstruction & Multi-view Geometry 或 AR/VR、机器人相关三维重建，具有潜在参考价值。但摘要未提供实验设置、量化结果、与基线对比和局限性信息，因此无法仅凭元数据和摘要判断其实际效果与稳健性，优先级不宜直接定为高。

</details>

<details>
<summary>Abstract</summary>

Sparse view 3D reconstruction is an important and common scenario in multimedia applications, such as augmented reality/virtual reality (AR/VR) content creation, cultural heritage digitization, and certain robotic applications, where only a limited number of randomly captured views may be available. However, sparse views contain only limited 3D information, posing two major challenges:1) too few images are available for matching, making it difficult to build multi-view consistency; 2) insufficient view coverage leads to a lack of information in under-sampled regions, resulting in missing parts of object structure. Existing methods mostly still rely on limited reprojection errors and regularization terms, which are prone to overfitting to a single view and inconsistent appearances across views. In geometrically under-sampled regions, they often rely on heuristic density control, lacking reliable guidance and often resulting in blurring and structural holes.To address these issues, this paper proposes Hierarchical Gaussian Fields (HierGF), which revisits sparse-view reconstruction from a hierarchical geometry-perception perspective and converts limited observations into reliable self-generated supervision beyond fixed priors and heuristic density control. In particular, we transform coarse 3D geometric information and additional 2D generative priors into structured pseudo-supervision through a two-stage geometry-perception backbone network, thereby enhancing multi-view consistency with very few input views. In addition, we introduce a learnable confidence network to guide gradients toward cross-view consistent content, and a geometrically consistent densification module to improve the reconstruction of multi-view alignment and under-sampled regions.

</details>

### 2026-09

#### 2026-09-30 - Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation

**Authors:** Sanya Verma, Luca Cilio, Velissarios Christodoulou
**Links:** [abs](https://arxiv.org/abs/2610.00731) - [pdf](https://arxiv.org/pdf/2610.00731)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation
- 作者：Sanya Verma, Luca Cilio, Velissarios Christodoulou
- 出版日期：2026-09-30T21:22:08Z
- 分类：3D Reconstruction & Multi-view Geometry（次要分类：未提供）
- 链接：[摘要](https://arxiv.org/abs/2610.00731) / [PDF](https://arxiv.org/pdf/2610.00731)

### 一句话总结
论文通过在同一双臂机器人单元上构建“定制重建”与“默认开源重建”两套仿真环境并进行对照实验，发现提高重建质量（视觉保真度、物理参数定制、度量尺度）能显著提升仿真评分与真实评分的相关性，并缩小 sim-to-real 差距。

### 研究问题
仿真评估在机器人策略评测中越来越常用于替代或补充真实评估，其价值取决于仿真结果能否紧密跟随真实机器人的表现。论文要检验：一种结合度量尺度物体几何、自定义物理参数与场景重建的流程，相比默认开源方案，是否能减少仿真与真实机器人评分之间的不一致。

### 核心思路/方法
- 构建同一个双臂机器人单元的两个仿真版本：
  - **定制重建（authored reconstruction）**：使用估计度量尺度下的物体几何、投影纹理、自定义物理参数，以及自研场景 splat。
  - **默认重建（default reconstruction）**：采用开源方案，即基于生成式单图网格、引擎默认物理和 Gaussian-splat 场景。
- 两种重建使用相同的物体照片与场景视频。
- 两个策略各运行五个任务，形成十个“任务—策略”对（称为 cells）。
- 每个 cell 在每种重建下运行二十次，其余设置保持不变。
- 两种重建均以同一批真实试验为评分基准，由第三方评估者打分。
- 比较指标为十个 cell 均值下仿真与真实评分之间的 Pearson 相关系数，以及平均分数误差。

### 主要贡献
- 报告了定制重建与默认重建在仿真—真实评分一致性上的量化对比：
  - Pearson 相关系数：定制重建 r = 0.90，默认重建 r = 0.51。
  - 平均分数误差：定制重建 6.97 个百分点，默认重建 17.54 个百分点，减少 10.56 个百分点。
- 结论表明：通过更高视觉保真度、自定义物理和度量尺度提升环境重建质量，可使仿真更贴近真实世界，缩小 sim-to-real 差距。
- 释放了测试框架、逐次试验评分、所有报告运行的配置，以及两种重建的资产与场景。

### 局限性
- 实验仅基于一个双臂机器人单元，摘要未提供跨更多机器人平台或场景的验证信息。
- 仅涉及两个策略、五个任务、十个 cell，摘要未提供更大规模任务或策略多样性的信息。
- 真实评分仅由第三方评估者给出，摘要未提供评分者数量、一致性或评分协议细节。
- 摘要未提供物理参数的具体设定方式、度量尺度估计误差、纹理与 splat 质量指标的细节。
- 摘要未提供计算成本、重建耗时或可扩展性分析。
- 摘要未提供统计显著性检验或置信区间信息。
- 摘要未提供基线开源方案的具体名称与版本信息。
- 摘要未提供失败案例或两套重建在哪些任务上差异最大的分析。

### 阅读优先级
**中**。理由：该论文聚焦 real-to-sim 评估中的重建质量对 sim-to-real 一致性的影响，问题明确、对照设计清晰，并报告了相关系数与平均误差的量化结果，对从事机器人仿真评估与 3D 重建应用的研究者有直接参考价值。但实验规模限于单一机器人单元、两个策略与五个任务，且摘要未提供统计显著性与更广泛的泛化验证，因此优先度定为中等而非高；若读者关注 sim-to-real 评估协议或重建资产对策略评分的影响，则可优先阅读。

</details>

<details>
<summary>Abstract</summary>

Simulated evaluation is increasingly used alongside real-world evaluation of robot policies because it is cheaper and easier to repeat; however, its value depends on how closely its outcomes track the real robot's. We test whether our reconstruction pipeline, combining metrically scaled object geometry, authored physical parameters and scene reconstruction, reduces disagreement between simulated and real robot scores relative to a default open-source recipe. We constructed two simulated versions of one bimanual robot cell: an authored reconstruction, using object geometry at estimated metric scale, projected textures, authored physics and our own scene splat; and a baseline, referred to as the default reconstruction, using the open-source recipe of a generative single-image mesh, engine-default physics and a Gaussian-splat scene. Both reconstructions use the same object photographs and scene video. Two policies ran five tasks each, giving ten task-policy pairs, which we call cells; each cell was run twenty times in each reconstruction with all other settings held fixed. Both reconstructions were scored against the same real trials, graded by a third-party evaluator. Pearson correlation between the ten simulated and real cell means is r = 0.90 for the authored reconstruction and 0.51 for the default. Mean score error is 6.97 percentage points for the authored reconstruction and 17.54 for the default, a reduction of 10.56 percentage points. These results show that improving the quality of the environment reconstruction through higher visual fidelity, authored physics and metric scale makes the simulation more faithful to the real world and narrows the sim-to-real gap. We release the harness, the per-trial scores, every reported run's configuration, and the assets and scenes of both reconstructions.

</details>

#### 2026-09-30 - Centralized Multi-UAV Exploration and 3D Reconstruction Using Single-UAV Planners

**Authors:** João Félix Mendes, Meysam Basiri, Rodrigo Ventura
**Links:** [abs](https://arxiv.org/abs/2609.40208) - [pdf](https://arxiv.org/pdf/2609.40208)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Centralized Multi-UAV Exploration and 3D Reconstruction Using Single-UAV Planners
- 作者：João Félix Mendes, Meysam Basiri, Rodrigo Ventura
- 出版日期：2026-09-30T17:19:03Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.40208) / [PDF](https://arxiv.org/pdf/2609.40208)

### 一句话总结
提出一个集中式多无人机探索框架，通过共享全局 TSDF 地图和集中规划，使现有单无人机采样规划器能够直接用于多无人机协同探索与三维重建。

### 研究问题
将单无人机探索方法扩展到多无人机团队，虽然有望提升覆盖速度和鲁棒性，但会引入一致建图、安全导航和部署策略等挑战。论文关注的核心问题是：如何在不改动单无人机采样规划器核心采样逻辑的前提下，将其扩展到多无人机协同探索场景。

### 核心思路/方法
论文提出一个集中式多无人机探索框架，允许多架无人机在共享的全局截断符号距离场（TSDF）地图上进行协同探索，并由中心节点进行规划。方法基于 voxblox 库，改造其建图流程以支持多无人机深度测量数据的实时融合到统一 TSDF 表示中。系统还集成无人机间避碰与机器人自过滤机制，以保证安全导航并避免将其他无人机重建为静态障碍物。

在评估方面，框架在仿真中使用四种基于采样的探索规划器：RH-NBVP、KRH-NBVP、AEP 和 KAEP。这些规划器的核心采样逻辑被保留，仅做系统层面的多无人机适配。实验在多种环境以及两种部署配置下进行：Joint Start（JS，无人机初始化在相近位置）和 Separated Start（SS，无人机初始化在不同位置）。

### 主要贡献
- 提出一个集中式多无人机探索框架，可复用现有单无人机采样规划器，仅需系统层面适配。
- 基于 voxblox 改造建图流程，实现多无人机深度测量向共享全局 TSDF 的实时融合。
- 集成无人机间避碰和机器人自过滤机制，保障安全导航并防止其他无人机被误重建为障碍物。
- 在仿真中对比四种采样规划器与两种部署配置，发现 SS 部署在所有规划器下均实现更快的探索和更好的覆盖率。

### 局限性
摘要未提供足够信息。摘要未提供关于计算开销、通信带宽需求、集中式架构在更大规模无人机团队中的可扩展性、真实飞行实验验证、以及具体定量指标（如探索时间、覆盖率数值）的详细信息。

### 阅读优先级
高。理由：该工作直接面向多无人机协同探索与三维重建中的部署策略、建图融合和安全导航问题，并系统评估了部署方式对探索性能的影响，对多无人机自主探索方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Extending single Unmanned Aerial Vehicles (UAVs) exploration methods to multi-UAV teams can improve coverage speed and robustness, but introduces challenges such as consistent mapping, safe navigation, and deployment strategy. In this work, we present a centralized multi-UAV exploration framework that enables the use of existing single-UAV sampling-based planners in a multi-UAV setting. The proposed architecture allows multiple UAVs to collaboratively explore unknown environments using a shared global Truncated Signed Distance Field (TSDF) map and centralized planning. Building on the voxblox library, we adapt its mapping pipeline to support real-time fusion of depth measurements from multiple UAVs into a common TSDF representation. In addition, inter-UAV collision avoidance and robot self-filtering mechanisms are integrated into the system to ensure safe navigation and prevent reconstruction of other UAVs as static obstacles. The framework is evaluated in simulation using four sampling-based exploration planners - RH-NBVP, KRH-NBVP, AEP, and KAEP - whose core sampling logic is preserved, with only system-level adaptations for multi-UAV operation. Experiments are conducted across multiple environments and under two deployment configurations: Joint Start (JS), where UAVs are initialized in close proximity, and Separated Start (SS), where UAVs are initialized in distinct locations. Results show that SS deployments consistently achieve faster exploration and improved coverage across all planners, highlighting the importance of the deployment strategy in multi-UAV exploration performance.

</details>

#### 2026-09-30 - Reconstructing the Dynamic World: A Representation-Centric View of 4D Scene Reconstruction

**Authors:** Ziren Gong, Guo Chen, Yongjia Li, Yihua Shao, Fabio Tosi, Stefano Mattoccia, Matteo Poggi, Hao Tang, Fei Ma, Shuyan Li, Ziyang Yan, Nicu Sebe, Ling Shao, Jianfei Cai, Qi Tian, Ming-Hsuan Yang
**Links:** [abs](https://arxiv.org/abs/2609.39960) - [pdf](https://arxiv.org/pdf/2609.39960)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reconstructing the Dynamic World: A Representation-Centric View of 4D Scene Reconstruction
- 作者：Ziren Gong, Guo Chen, Yongjia Li, Yihua Shao, Fabio Tosi, Stefano Mattoccia, Matteo Poggi, Hao Tang, Fei Ma, Shuyan Li, Ziyang Yan, Nicu Sebe, Ling Shao, Jianfei Cai, Qi Tian, Ming-Hsuan Yang
- 出版日期：2026-09-30T15:29:43Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.39960 ；PDF https://arxiv.org/pdf/2609.39960

### 一句话总结
本文以“场景表示”为中心，对 4D 场景重建中的现有方法进行统一梳理，围绕场景表示、时间建模策略、重建流程和优化目标建立分析框架，并总结数据集、评价指标、实验实践局限与开放挑战。

### 研究问题
摘要指出，4D 场景重建旨在从视觉观测中恢复动态环境不断演化的几何、外观和运动。尽管神经场景表示已有显著进展，动态场景重建仍面临非刚性运动、遮挡、时间不一致性，以及重建保真度与计算效率之间的权衡等挑战。近期 Neural Radiance Fields（NeRF）与 3D Gaussian Splatting（3DGS）相关工作提出了多种动态场景表示与重建方法，但这些方法之间的关系、底层设计选择与评价协议仍然较为分散。

### 核心思路/方法
论文提出一个关于 4D 场景重建的统一视角，按照以下维度组织现有方法：
- 场景表示
- 时间建模策略
- 重建流程
- 优化目标

通过该框架，论文考察不同设计选择如何影响几何保真度、外观一致性、运动表示和计算效率。论文还整合常用数据集与评价指标，识别当前实验实践中的局限，并讨论复杂动态真实世界环境重建中的开放挑战。摘要强调，该工作将方法发展与 underlying assumptions 和评价证据相连接，为理解现有方法和识别未来研究方向提供结构化基础。作者还提供了一个持续更新的相关论文与资源集合：https://github.com/ZiyangYan/Awesome-4D-Scene-Reconstruction 。

### 主要贡献
- 提出一个以表示为中心的 4D 场景重建统一视角，将现有方法围绕场景表示、时间建模、重建流程和优化目标进行组织。
- 在该框架下分析不同设计选择对几何保真度、外观一致性、运动表示和计算效率的影响。
- 整合常用数据集和评价指标。
- 指出现有实验实践中的局限。
- 讨论复杂、动态真实世界环境重建中的开放挑战。
- 提供持续更新的相关论文与资源集合链接。

### 局限性
摘要未提供足够信息说明本文方法在具体实验中的定量局限、失败案例或适用范围边界。基于摘要只能看出，本文是一篇综述/统一框架类工作，而非提出单一新重建模型；其局限性、覆盖范围是否完整、分类框架是否覆盖所有方法、以及评价协议建议的具体可操作程度，摘要均未提供足够信息。

### 阅读优先级
中。理由：该论文是 4D 场景重建领域的综述与统一框架梳理，适合希望快速建立该方向方法分类、设计维度、数据集与评价指标全貌的读者；如果读者关注具体新模型、新损失函数或实验性能突破，摘要显示本文重点在组织与分析已有工作，而非提出单一新方法。因此对领域入门和方向定位有较高参考价值，但对追求具体算法创新的读者优先级为中等。

</details>

<details>
<summary>Abstract</summary>

4D scene reconstruction aims to recover the evolving geometry, appearance, and motion of dynamic environments from visual observations. Despite substantial progress in neural scene representations, reconstructing dynamic scenes remains challenging due to non-rigid motion, occlusions, temporal inconsistencies, and the trade-offs between reconstruction fidelity and computational efficiency. Recent advances in Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have introduced diverse approaches to representing and reconstructing dynamic scenes, yet their relationships, underlying design choices, and evaluation protocols remain fragmented. In this paper, we present a unified perspective on 4D scene reconstruction, organizing existing methods around their scene representations, temporal modeling strategies, reconstruction pipelines, and optimization objectives. Through this framework, we examine how different design choices affect geometric fidelity, appearance consistency, motion representation, and computational efficiency. We further consolidate commonly used datasets and evaluation metrics, identify limitations in current experimental practices, and discuss open challenges in reconstructing complex, dynamic real-world environments. By connecting methodological developments with their underlying assumptions and evaluation evidence, this work provides a structured foundation for understanding existing approaches and identifying future research directions. An evolving collection of relevant papers and resources is available at https://github.com/ZiyangYan/Awesome-4D-Scene-Reconstruction.

</details>

#### 2026-09-30 - Magnetic based In-situ Self 3D Pose Estimation for a Modular Soft Tendon-Driven Continuum Robot via IMU-Fusion

**Authors:** Zheng Cao, Guo Ning Sue, Xiangyun Bu, David Quinn, Junzhe Hu, Carmel Majidi
**Links:** [abs](https://arxiv.org/abs/2609.39950) - [pdf](https://arxiv.org/pdf/2609.39950)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Magnetic based In-situ Self 3D Pose Estimation for a Modular Soft Tendon-Driven Continuum Robot via IMU-Fusion
- 作者：Zheng Cao, Guo Ning Sue, Xiangyun Bu, David Quinn, Junzhe Hu, Carmel Majidi
- 出版日期：2026-09-30T15:24:19Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.39950

### 一句话总结
本文提出一种将惯性测量单元（IMU）与主动磁场相结合的嵌入式位姿感知框架，用于在不依赖外部相机的情况下估计模块化软体腱驱动连续体机器人的构型，并通过闭环控制实验进行验证。

### 研究问题
连续体机器人因其固有柔顺性和适应复杂环境的能力，适合进行轻柔操作；但其连续可变形结构使得精确的构型估计十分困难，尤其是在外部视觉系统不可用或受遮挡时。论文关注的核心问题是：如何在不依赖外部相机的条件下，实现连续体机器人实时、准确的位姿/构型估计，以支撑实时反馈与闭环控制。

### 核心思路/方法
- 构建嵌入式位姿感知框架，融合 IMU 与主动磁场，实现不依赖外部相机的机器人构型估计。
- 将 IMU 的角度测量与磁场参考进行融合，以改善局部姿态估计，并减少运行过程中累积的姿态误差。
- 该位姿感知方案更新速率为 16.7 Hz，支持实时反馈。
- 通过闭环控制进行实验验证：利用估计的机器人构型，在与物体交互过程中将末端执行器维持在期望位置。

### 主要贡献
- 提出一种基于 IMU 与主动磁场融合的嵌入式位姿感知框架，用于连续体机器人构型估计，无需外部相机。
- 通过融合 IMU 角测量与磁场参考，改善局部姿态估计并降低姿态误差累积。
- 实现 16.7 Hz 的更新速率，支持实时反馈。
- 通过闭环控制实验验证系统：使用估计构型在与物体交互时保持末端执行器处于期望位置，展示了分布式磁-惯性传感在连续体机器人实时位姿估计与闭环控制中的潜力。

### 局限性
- 论文仅基于摘要信息，未提供关于估计精度、误差量级、鲁棒性、可扩展性、磁场干扰影响、IMU 漂移特性等定量结果或对比实验的细节，摘要未提供足够信息。
- 摘要提及实验验证为闭环控制中保持末端执行器在期望位置，但未说明任务复杂度、环境条件、机器人自由度或模块数量的适用范围，摘要未提供足够信息。
- 摘要未提供该方法与其他位姿估计方法（如纯视觉、纯 IMU 或其他传感融合方案）的对比，摘要未提供足够信息。
- 摘要未提供系统在外部磁场变化、动态运动或长期运行下的性能表现，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对连续体机器人在无外部视觉条件下的实时位姿估计与闭环控制这一关键难题，提出磁-惯性融合的嵌入式方案，并给出可实时运行的更新速率与闭环控制验证，与软体机器人、连续体机器人感知与控制、多传感器融合方向高度相关。若读者关注无相机位姿估计、磁传感或软体机器人闭环控制，该论文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Continuum robots are well suited for gentle manipulation because of their inherent compliance and ability to adapt to complex environments. However, their continuously deformable structure makes accurate configuration estimation challenging, particularly when external vision systems are unavailable or obstructed. In this work, we present an embedded pose sensing framework that combines inertial measurement units (IMUs) and active magnetic fields to estimate the robot configuration without relying on external cameras. The angular measurements from the IMU and magnetic-field references are fused to improve local orientation estimation and reduce accumulated orientation error during operation. This pose sensing scheme achieves an update rate of 16.7~Hz, allowing real-time feedback. The proposed system is experimentally validated through closed-loop control, where the estimated robot configuration is used to maintain the end-effector at a desired position while interacting with an object. These results demonstrate the potential of distributed magnetic--inertial sensing for real-time pose estimation and closed-loop control of continuum robots.

</details>

#### 2026-09-30 - Introduction to Computer Vision

**Authors:** Stan Birchfield
**Links:** [abs](https://arxiv.org/abs/2609.39627) - [pdf](https://arxiv.org/pdf/2609.39627)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** structure from motion, camera calibration

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Introduction to Computer Vision
- 作者：Stan Birchfield
- 出版日期：2026-09-30T12:36:34Z
- 分类：primary_category: 3D Reconstruction & Multi-view Geometry；secondary_categories: 未提供
- 链接：abstract_url: https://arxiv.org/abs/2609.39627；pdf_url: https://arxiv.org/pdf/2609.39627

### 一句话总结
这是一本以“代码优先”为理念的计算机视觉入门书籍，覆盖经典 2D 图像处理、经典 3D 视觉与深度学习，共 44 个短章节，并强调用 Python/NumPy 或 PyTorch 实现并与 OpenCV/PyTorch 库函数进行数值对照。

### 研究问题
摘要未提供足够信息说明本书所针对的具体研究问题。从摘要表述看，其目标不是提出新的算法或实验结论，而是面向学生与实践者，提供一个自包含的、可理解计算机视觉算法及其 Python 实现的参考材料。

### 核心思路/方法
- 采用“代码优先”的引入方式，覆盖三大板块：经典 2D 图像处理、经典 3D 视觉、深度学习。
- 全书组织为 44 个短章节，分为三个部分，每个主题从第一性原理构建。
- 具体主题包括：
  - 图像算术与形态学；
  - 卷积、金字塔与频域滤波；
  - 特征检测、光流与立体视觉；
  - 投影几何、相机标定与运动恢复结构；
  - 现代深度学习的完整脉络：从单个神经元到卷积网络、反向传播、经典架构、迁移学习、目标检测、语义分割与实例分割，最后涉及混合精度与并行训练等工程考虑。
- 每种技术都直接用 Python 和 NumPy 或 PyTorch 实现，并与相应的 OpenCV 或 PyTorch 库函数进行数值检查，使读者不仅看到数学，还能看到其在真实与合成数据上的具体行为。
- 材料借助 AI 辅助从免费在线课程笔记中提炼，将大量工作代码压缩为简洁的数学阐述，同时保留经过验证、可复现的结果。

### 主要贡献
- 提供了一本自包含的计算机视觉参考书，面向希望理解计算机视觉算法及其 Python 实现的学生和实践者。
- 以代码优先和数值对照的方式连接数学原理与具体实现行为。
- 内容跨度较广，从经典 2D 图像处理、3D 视觉到现代深度学习，并涵盖目标检测、语义/实例分割及部分工程实践主题。
- 以 44 个短章节、三部分的结构组织，便于按主题逐步学习。
- 强调保留可复现的验证结果，并借助 AI 辅助从公开在线课程笔记中提炼内容。

### 局限性
- 摘要未提供足够信息说明本书在实验规模、数据集覆盖、方法对比或定量评测方面的具体表现。
- 摘要未提供足够信息说明本书是否包含习题、教学配套、代码仓库维护方式或读者预备知识要求。
- 摘要未提供足够信息说明“AI 辅助提炼”的具体流程、验证标准或可能带来的内容偏差。
- 摘要未提供足够信息说明本书与同类教材或课程之间的差异性与覆盖率边界。
- 摘要未提供足够信息说明混合精度、并行训练等工程主题的展开深度。

### 阅读优先级
中。  
理由：如果读者需要一本以 Python 实现为主线、从经典视觉到深度学习且强调数值对照的入门参考书，本书的定位较清晰，具有一定阅读价值；但摘要未提供具体实验、评测或教学配套信息，且书籍主题覆盖面广，是否适合深入某一方向仍需进一步查看目录与正文。因此综合判断为中等优先级。

</details>

<details>
<summary>Abstract</summary>

This book presents a code-first introduction to computer vision, spanning classical 2D image processing, classical 3D vision, and deep learning. Organized as 44 short chapters across three parts, the book builds each topic from first principles: image arithmetic and morphology; convolution, pyramids, and frequency-domain filtering; feature detection, optical flow, and stereo; projective geometry, camera calibration, and structure from motion; and the full arc of modern deep learning, from a single neuron through convolutional networks, backpropagation, classic architectures, transfer learning, object detection, and semantic and instance segmentation, concluding with engineering considerations like mixed-precision and parallel training. Every technique is implemented directly in Python and NumPy or PyTorch and checked numerically against the corresponding OpenCV or PyTorch library function, so readers see not just the mathematics but its concrete behavior on real and synthetic data. The material was distilled with AI assistance from freely available online course notes, condensing extensive working code into concise mathematical exposition while preserving verified, reproducible results throughout. It is intended as a self-contained reference for students and practitioners who want to understand computer vision algorithms and their Python implementations.

</details>

#### 2026-09-30 - MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM

**Authors:** Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer, Holger Voos, Jose Luis Sanchez-Lopez
**Links:** [abs](https://arxiv.org/abs/2609.39596) - [pdf](https://arxiv.org/pdf/2609.39596)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM
- 作者：Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer, Holger Voos, Jose Luis Sanchez-Salopez
- 出版日期：2026-09-30T12:19:04Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2609.39596 ；PDF https://arxiv.org/pdf/2609.39596

### 一句话总结
MVP-SLAM 是一种面向室内建筑工地的在线视觉惯性 SLAM 系统，利用两台相对朝向的鱼眼相机，将地图中检测到的墙体与设计阶段楼层平面图匹配，并通过漂移感知策略在线持续校正轨迹与定位。

### 研究问题
室内建筑工地是视觉 SLAM 的高难度场景：光照变化、重复且低纹理的结构容易导致系统在长轨迹上产生漂移；但墙体等结构元素在这些条件下仍具有可区分性。建筑按设计阶段的楼层平面图施工，尽管实际建成现场可能与设计存在差异，平面图仍可提供度量参考，用于将系统定位在建筑中并校正漂移。现有方法中，一类通常离线使用平面图校正已构建的轨迹，另一类在线校正则往往依赖深度传感器，因此需要一种仅依靠相机、在线完成校正的方法。

### 核心思路/方法
- 系统形式：面向室内建筑工地的在线视觉惯性 SLAM。
- 传感器配置：两台相对朝向的鱼眼相机。
- 校正依据：将系统中地图检测到的墙体与楼层平面图进行匹配。
- 校正策略：通过漂移感知策略（drift-aware policy）从相机单独完成漂移校正。
- 集成方式：采用多阶段集成，将每一对匹配结果逐步转化为持久性校正，使轨迹在被构建的过程中持续保持校正，并定位在平面图内。

### 主要贡献
- 提出 MVP-SLAM，一种在线视觉惯性 SLAM 系统，仅依靠两台相对朝向的鱼眼相机，通过将地图中检测的墙体与楼层平面图匹配来校正漂移。
- 引入漂移感知策略进行墙体—平面图匹配，并通过多阶段集成将匹配对增量转化为持久校正，使轨迹在构建过程中持续保持校正与平面图内定位。
- 在 Hilti-Trimble SLAM Challenge 2026 的多层建筑工地场景中验证：在 Localization 任务中 22 支队伍排名第 2（平均 RMSE 0.29 m），在 SLAM 任务中 62 支队伍排名第 5（0.24 m）；在两个任务中均为“在线运行、集成平面图并定位其中”这一条件下的最高排名队伍。

### 局限性
摘要未提供足够信息。摘要未提及系统在无平面图、平面图与建成现场差异过大、非建筑工地场景或计算资源受限条件下的表现，也未提供失败案例、运行时间或实时性指标等细节。

### 阅读优先级
高。理由：该工作针对室内建筑工地 SLAM 中长轨迹漂移与平面图先验利用这一明确问题，提出仅依赖鱼眼相机的在线校正方案，并在公开挑战赛多任务中获得较靠前排名且在同条件队伍中排名最高，对关注视觉惯性 SLAM、平面图先验、多相机系统与建筑机器人/工地定位的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Indoor building construction sites are demanding environments for visual SLAM, where variable lighting and repetitive, low-textured structures make the system drift over long trajectories, though structural elements such as walls remain distinguishable despite these conditions. These buildings are constructed according to their as-planned floor plans, available from the design phase, and although the actual as-built site can differ from this design, floor plans still provide a metric reference, both to localize the system in the building and to correct drift. Existing methods often use the floor plan to correct an already-built trajectory offline, and those that instead correct it online typically rely on depth sensors. We instead present MVP-SLAM, an online visual-inertial SLAM on two opposite-facing fisheye cameras that corrects drift from cameras alone by matching walls detected in its map to the floor plan, through a drift-aware policy. A multi-stage integration then turns each matched pair incrementally into a persistent correction, so the trajectory stays corrected and localized within the floor plan as it is built. MVP-SLAM was validated on the multi-floor construction sites of the Hilti-Trimble SLAM Challenge 2026, ranking 2nd of 22 teams in the Localization task (0.29 m mean RMSE) and 5th of 62 teams in the SLAM task (0.24 m), the top-ranked one in both tasks among those that operate online, integrate the floor plan, and localize within it.

</details>

#### 2026-09-30 - Emergent Multi-View Geometry Through Self-Distillation

**Authors:** David Nordström, Thibaut Loiseau, Vincent Lepetit, Michael Felsberg, Guillaume Bourmaud, Fredrik Kahl
**Links:** [abs](https://arxiv.org/abs/2609.39227) - [pdf](https://arxiv.org/pdf/2609.39227)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Emergent Multi-View Geometry Through Self-Distillation
- 作者：David Nordström, Thibaut Loiseau, Vincent Lepetit, Michael Felsberg, Guillaume Bourmaud, Fredrik Kahl
- 出版日期：2026-09-30T08:02:42Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.39227) / [PDF](https://arxiv.org/pdf/2609.39227)

### 一句话总结
论文提出名为 Poincar3 的自监督方法，通过自蒸馏而非 RGB 重建从多视角学习表征，从而在无显式 3D 监督下自发获得多视角几何能力。

### 研究问题
论文关注视觉表征学习中的问题：大多数方法基于单张图像，而利用多视角的方法通常依赖 RGB 重建，这会把几何信息与外观信息纠缠在一起。论文试图在不使用 RGB 重建、也不依赖显式 3D 监督的情况下，从多视角数据中学习能够编码几何信息的表征。

### 核心思路/方法
论文提出 Poincar3，一种自监督方法，通过自蒸馏从多视角学习表征，而不是进行 RGB 重建。方法结合了掩码 patch 级别蒸馏与图像级别蒸馏，并使用一个能够观察额外视角的 teacher，从而支持从零开始训练，且不需要显式 3D 监督。摘要还提到使用轻量级 Poincaré adapter，发现所学特征能比现有自监督表征更准确地编码相机运动。

### 主要贡献
- 提出 Poincar3，一种通过自蒸馏而非 RGB 重建从多视角学习表征的自监督方法。
- 将掩码 patch 蒸馏与图像级蒸馏结合，并使用观察额外视角的 teacher，实现无需显式 3D 监督的从零训练。
- 在对应估计、相机位姿估计和 3D 重建任务上，Poincar3 优于此前的单视角与多视角自监督方法，如 DINOv3、MuM 和 Muskie。
- 通过轻量级 Poincaré adapter 发现，所学特征比现有自监督表征更准确地编码相机运动。

### 局限性
摘要未提供足够信息。论文摘要未说明具体实验设置、数据集、计算成本、失败案例或方法适用范围等细节，因此无法基于给定内容判断其局限性。

### 阅读优先级
高。理由：该论文提出了一条区别于 RGB 重建的多视角自监督表征学习路线，且摘要明确声称在对应估计、相机位姿估计和 3D 重建上优于 DINOv3、MuM、Muskie 等已有方法；同时涉及“自发涌现多视角几何”这一具有理论启发的主题，适合关注多视角几何、3D 重建与自监督表征学习的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Over a century ago, Henri Poincaré argued that a motionless observer cannot acquire the notion of space. Yet, most visual representation learning methods operate on individual images, while those that leverage multiple views rely on RGB reconstruction, entangling geometry with appearance. We propose Poincar3, a self-supervised method that learns representations from multiple views through self-distillation instead of RGB reconstruction. We combine masked patch and image-level distillation with a teacher that observes additional views, enabling training from scratch without explicit 3D supervision. Poincar3 outperforms both previous single and multi-view self-supervised approaches such as DINOv3, MuM, and Muskie on correspondence estimation, camera pose estimation, and 3D reconstruction. Using a lightweight Poincaré adapter, we also find that our learned features encode camera motion more accurately than existing self-supervised representations.

</details>

#### 2026-09-30 - Decoupling Spherical Reasoning from Dense Prediction for 360 Depth Estimation

**Authors:** Zhijie Shen, Chunyu Lin, Shuai Zheng, Feng Li, Runmin Cong, Huihui Bai, Yao Zhao
**Links:** [abs](https://arxiv.org/abs/2609.38856) - [pdf](https://arxiv.org/pdf/2609.38856)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Decoupling Spherical Reasoning from Dense Prediction for 360 Depth Estimation
- 作者：Zhijie Shen, Chunyu Lin, Shuai Zheng, Feng Li, Runmin Cong, Huihui Bai, Yao Zhao
- 出版日期：2026-09-30T03:14:24Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.38856

### 一句话总结
该论文提出将全景深度估计中的球面上下文建模与 ERP 稠密预测解耦，通过 Fibonacci Spherical Graph 作为中间推理空间，并用 Spherical Context Conditioning 模块将球面表示回注到 ERP 特征中以指导像素对齐的深度预测。

### 研究问题
ERP（等距柱状投影）广泛用于全景深度估计，但其空间变化的畸变使得几何一致的特征建模十分困难。论文关注的核心问题是：如何在原生球面空间中进行上下文建模，同时避免 ERP 投影畸变带来的影响，并完成稠密 ERP 深度预测。

### 核心思路/方法
论文的核心思路是将“球面空间中的上下文建模”与“ERP 上的稠密预测”解耦。具体方法包括：
1. 提出 Fibonacci Spherical Graph（FSG）作为中间推理空间，将 ERP 特征提升到球面上近似均匀分布的 Fibonacci 节点上，并通过互补的球面邻域捕获局部与长程依赖。该球面离散化使图节点在球面上近似均匀分布，从而减少关系建模中高度拉伸区域的过度表示；同时在紧凑的 Fibonacci 节点集合上操作，避免了在全 ERP 分辨率上构建和处理图的计算负担。
2. 提出 Spherical Context Conditioning（SCC）模块，将增强后的球面表示自适应地调制稠密 ERP 特征，使球面上下文能够引导像素对齐的深度预测，从而连接球面推理与稠密预测两个环节。

### 主要贡献
1. 重新审视全景深度估计，将原生球面空间中的上下文建模与稠密 ERP 预测解耦。
2. 提出 Fibonacci Spherical Graph（FSG）作为中间推理空间，在近似均匀分布的球面节点上捕获局部与长程依赖，并降低高度拉伸区域的过度表示与全分辨率图计算负担。
3. 提出 Spherical Context Conditioning（SCC）模块，用增强的球面表示自适应调制稠密 ERP 特征，桥接球面推理与稠密预测。
4. 在三个基准上开展实验，结果表明所提方法在深度精度上持续优于现有方法。

### 局限性
摘要未提供足够信息。摘要仅说明在三个基准上取得了更优的深度精度，未提及具体实验设置、失败案例、方法假设的适用范围、计算开销的定量结果或潜在限制。

### 阅读优先级
高。理由：该论文针对全景深度估计中 ERP 畸变导致几何一致特征建模困难这一关键问题，提出了明确且具结构性的解耦思路（球面图推理 + 球面上下文调制），并声称在三个基准上持续优于现有方法；对于关注 360 深度估计、球面表示学习或 ERP 畸变建模的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

The equirectangular projection (ERP) is widely used for panoramic depth estimation, but its spatially varying distortion makes geometry-consistent feature modeling challenging. We revisit panoramic depth estimation by decoupling contextual modeling in native spherical space from dense ERP prediction. To this end, we propose a Fibonacci Spherical Graph (FSG) as an intermediate reasoning space to lift ERP features onto quasi-uniform Fibonacci nodes on the sphere and capture local and long-range dependencies through complementary spherical neighborhoods. The resulting spherical discretization distributes graph nodes approximately uniformly over the spherical surface, reducing the over-representation of highly stretched regions during relational modeling. Operating on a compact set of Fibonacci nodes also avoids the computational burden of constructing and processing a graph at full ERP resolution. To bridge spherical reasoning and dense prediction, we propose a Spherical Context Conditioning (SCC) module that adaptively modulates dense ERP features with the enhanced spherical representation, allowing spherical context to guide pixel-aligned depth prediction. Extensive experiments on three benchmarks demonstrate that the proposed method consistently achieves superior depth accuracy over existing approaches.

</details>

#### 2026-09-30 - Agentic Relative Camera Pose Estimation via Learned Ranking and Verification

**Authors:** Zhining Gu, Shangjie Du, Weimin Qiu, Carl Olsson, Ping Liu, Meng Tang
**Links:** [abs](https://arxiv.org/abs/2609.38755) - [pdf](https://arxiv.org/pdf/2609.38755)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Agentic Relative Camera Pose Estimation via Learned Ranking and Verification
- 作者：Zhining Gu, Shangjie Du, Weimin Qiu, Carl Olsson, Ping Liu, Meng Tang
- 出版日期：2026-09-30T01:42:00Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2609.38755) / [PDF](https://arxiv.org/pdf/2609.38755)

### 一句话总结
论文提出 PoseAgent，一个通过可学习的排序与验证机制动态调度多个相机位姿估计器的 agentic 框架，以应对不同图像对上的多样化挑战。

### 研究问题
相机位姿估计已有多种方法（基于对应关系的方法、端到端位姿回归、近期 3D 几何基础模型），但作者观察到没有任何单一估计器能在宽基线、缺乏纹理、外观变化、遮挡等多样挑战下都最优；进一步分析显示，不同估计器在不同基准和个别图像对上表现差异显著，且具有互补优势。因此问题是如何针对给定图像对动态选择最合适的估计器。

### 核心思路/方法
PoseAgent 是一个 agentic 框架，包含以下流程：
1. **Profiling agent**：对输入图像对提取与位姿估计相关的外观、语义和几何特征（例如场景类型）。
2. **Learned ranking agent**：基于图像对画像，预测多个位姿估计器的相对能力排名。
3. **执行与验证**：执行排名最高的估计器，由 **learned verification agent** 评估其预测位姿的误差。
4. **回退策略**：若验证失败，PoseAgent 自适应地调用排名较低的估计器，直到某个候选被接受或达到执行预算。
论文还强调其验证网络在预测位姿误差方面比先前模型更准确。

### 主要贡献
- 提出 PoseAgent，一个通过可学习排序与验证动态编排位姿估计器的 agentic 框架。
- 在 ARKitScenes、MegaDepth、ScanNet++、RealEstate10K 上，相比各自最强的单一估计器，AUC@5 degree 提升最高达 4.2%。
- 在 ARKitScenes 上，PoseAgent 也优于基于 VLM 的 agent（包括使用相同验证器和回退策略的 VLM 排序器）。
- 其验证网络在位姿误差预测上比先前模型更准确。

### 局限性
摘要未提供足够信息（未提及计算开销、执行预算的具体设定、对 profiling agent 特征提取错误的敏感性、在未测试数据集上的泛化性等）。

### 阅读优先级
中。理由：该工作针对多估计器互补性与动态调度这一实际问题，提出了结合学习排序与验证的 agentic 框架，并在多个基准上取得一致提升，对 3D 重建与多视图几何方向有一定参考价值；但摘要未披露方法细节与局限，需阅读全文才能判断其通用性与实用性。

</details>

<details>
<summary>Abstract</summary>

A wide range of approaches have been developed for camera pose estimation, including correspondence-based methods, end-to-end pose regression, and recent 3D geometric foundation models. Our key observation is that no single estimator is optimal for diverse challenges, such as wide baselines, lack of texture, appearance changes, and occlusions. Further analysis reveals substantial performance variation across both benchmarks and individual image pairs, with different estimators exhibiting complementary strengths. We introduce PoseAgent, an agentic framework for relative camera pose estimation that dynamically orchestrates pose estimators through learnable ranking and verification. Given an image pair, a profiling agent first extracts appearance, semantic, and geometric features relevant to pose estimation, e.g., scene type. A learned ranking agent then predicts the relative competence of multiple pose estimators given the image-pair profile. The top-ranked estimator is executed, and its predicted pose is assessed by a learned verification agent that estimates the corresponding pose error. When verification fails, PoseAgent adaptively invokes lower-ranked estimators until a candidate is accepted or the execution budget is reached. For pose verification, our verification network predicts pose errors more accurately than prior models. For pose estimation, PoseAgent improves AUC@5 degree up to 4.2% over the strongest standalone estimator on each of ARKitScenes, MegaDepth, ScanNet++, and RealEstate10K. On ARKitScenes, PoseAgent also outperforms VLM-based agents, which include a VLM ranker with the same verifier and fallback policy. These results demonstrate the effectiveness of our learned ranking and verification.

</details>

#### 2026-09-30 - Matisse: Evidence-Space Reasoning for Active 3D Reconstruction

**Authors:** Xihang Yu, Kaichen Zhou, Lorenzo Shaikewitz, Clément Jambon, Xiao Zhan, Rajat Talak, Luca Carlone
**Links:** [abs](https://arxiv.org/abs/2609.38746) - [pdf](https://arxiv.org/pdf/2609.38746)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Matisse: Evidence-Space Reasoning for Active 3D Reconstruction
- 作者：Xihang Yu, Kaichen Zhou, Lorenzo Shaikewitz, Clément Jambon, Xiao Zhan, Rajat Talak, Luca Carlone
- 出版日期：2026-09-30T01:30:32Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.38746 ；PDF https://arxiv.org/pdf/2609.38746

### 一句话总结
Matisse 是一个无需训练的框架，利用预训练生成式 3D 模型提供的证据空间，将主动重建与关键帧选择统一起来，以在有限计算预算下提升部分视图三维重建效果。

### 研究问题
论文关注的问题是：在有限计算预算下，3D 重建系统如何从部分视图中获取并保留有用信息，从而理解场景几何。摘要指出，现有主动视图获取方法通常只在已观测或已实例化几何上估计不确定性，因此难以推理未见结构；而长时程重建方法又常常保留冗余观测。

### 核心思路/方法
Matisse 的核心是“证据空间推理”，并强调是无需训练（training-free）的框架。它借助预训练生成式 3D 模型提供的证据，统一主动重建与关键帧选择。

具体而言，Matisse 从与 3D 潜在 token 相关的交叉注意力证据中估计 Evidential Uncertainty，并推导出 Evidential Information Gain，用于指导视图获取和关键帧选择。该信息增益基于后验熵的期望减少量。为支持多物体场景，方法采用遮挡感知、物体平衡的聚合方式；同时通过中间潜在变量传播不确定性，以避免在规划阶段进行完整重建。

### 主要贡献
- 提出 Matisse，一个无需训练的框架，将主动重建与关键帧选择统一在由预训练生成式 3D 模型提供的证据空间中。
- 提出基于交叉注意力证据的 Evidential Uncertainty，并推导 Evidential Information Gain，以指导下一次视图获取与关键帧选择。
- 支持多物体场景，通过遮挡感知、物体平衡的聚合处理，并通过中间潜在变量传播不确定性以避免规划时完整重建。
- 摘要报告的结果显示：在 GSO30、YCB-V 和 Replica 上，相比各数据集最佳基线，Chamfer distance 分别降低 12.7%、3.8% 和 9.2%；在 GSO30 上，相同重建后端下相比最佳主动重建基线取得 1.50× 端到端加速；在 GSO30 长时程重建的关键帧选择实验中，相比 Stream3D，使用 14% 的输入视图达到可比的 Chamfer distance。

### 局限性
摘要未提供足够信息关于该方法的局限性。未提供的信息包括：失败场景、对预训练生成式 3D 模型质量的依赖程度、计算资源具体需求、不同数据集上的泛化边界、实时性限制、训练-free 设定下的具体约束等。

### 阅读优先级
高。理由：该论文聚焦主动 3D 重建与关键帧选择，提出无需训练的统一框架，并在多个数据集上报告了 Chamfer distance 降低和端到端加速，同时涉及长时程重建中的视图效率提升；对 3D 重建、主动感知和多视图几何方向具有直接相关性。

</details>

<details>
<summary>Abstract</summary>

How can a 3D reconstruction system acquire and retain useful information to understand the geometry of a scene from partial views under a limited computation budget? Existing active view acquisition methods typically estimate uncertainty over observed or instantiated geometry, limiting their ability to reason about unseen structure, while long-horizon reconstruction methods often retain redundant observations. We introduce Matisse, a training-free framework that unifies active reconstruction and keyframe selection by leveraging evidence provided by a pretrained generative 3D model. Matisse estimates Evidential Uncertainty from cross-attention evidence associated with 3D latent tokens and derives an Evidential Information Gain to guide both view acquisition and keyframe selection based on the expected reduction in posterior entropy. Matisse supports multi-object scenes through occlusion-aware, object-balanced aggregation and propagates uncertainty through intermediate latents to avoid full reconstruction during planning. Matisse reduces Chamfer distance by 12.7%, 3.8%, and 9.2% on GSO30, YCB-V, and Replica, respectively, relative to the best baseline on each dataset, and achieves a $1.50\times$ end-to-end speedup over the best active reconstruction baseline on GSO30 with the same reconstruction backend. In the GSO30 keyframe selection experiment for long-horizon reconstruction, Matisse achieves comparable Chamfer distance using 14% of the input views compared with Stream3D.

</details>

#### 2026-09-29 - HIGS: Hierarchical Implicit Grids for Joint Geometric and Semantic Scene Understanding

**Authors:** Hanwen Cao, Wenqiang Wu, Kuang-Ting Tu, Mathias Otnes, Jeffrey Delmerico, Rui Wang, Yulun Tian, Nikolay Atanasov
**Links:** [abs](https://arxiv.org/abs/2609.38620) - [pdf](https://arxiv.org/pdf/2609.38620)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, geometric reconstruction, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HIGS: Hierarchical Implicit Grids for Joint Geometric and Semantic Scene Understanding
- 作者：Hanwen Cao, Wenqiang Wu, Kuang-Ting Tu, Mathias Otnes, Jeffrey Delmerico, Rui Wang, Yulun Tian, Nikolay Atanasov
- 出版日期：2026-09-29T22:22:49Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.38620) / [PDF](https://arxiv.org/pdf/2609.38620)

### 一句话总结
该论文提出分层隐式网格 HIGS，通过多分辨率子图、统一的几何与语义查询解码机制，以及隐式特征空间内的对齐融合，面向大规模场景的联合几何与语义理解。

### 研究问题
论文指出两个主要挑战：
1. 现有神经隐式表示多聚焦几何重建，缺乏语义信息，难以支持高层空间理解与任务规划。
2. 随着环境规模和复杂度增加，神经表示在后端优化中难以保持计算效率。

因此，论文旨在同时解决几何与语义联合表示问题，以及大规模场景下的计算与内存效率问题。

### 核心思路/方法
- 提出分层神经场，利用多分辨率子图实现高效、可扩展的隐式表示。
- 使用统一的查询与解码机制，同时支持几何特征和语义特征。
- 可学习的地图特征通过查询和解码过程转换为输出，用于训练和推理。
- 面向大规模表示，将场景分解为重叠子图，并在每个局部子图内进行分层优化，从而实现可扩展计算。
- 设计特征编码器预测初始分层网格特征，以减少从零开始优化子图特征所需时间。
- 为校正子图之间的估计漂移，在隐式特征空间内完成对齐与融合，避免解码最终输出，从而显著加速。
- 在该高效分层表示基础上，将几何特征和视觉-语言潜在特征嵌入地图，并在 Signed Distance Field (SDF) 构建和开放词汇物体定位上展示。

### 主要贡献
- 提出 HIGS，一种面向联合几何与语义场景理解的分层隐式网格表示。
- 引入多分辨率子图与局部子图内分层优化，以支持大规模场景的可扩展计算。
- 设计统一查询与解码机制，使同一框架支持几何和语义特征输出。
- 通过特征编码器预测初始分层网格特征，减少子图特征从头优化时间。
- 在隐式特征空间内对齐并融合子图，避免解码最终输出以实现加速。
- 将几何特征与视觉-语言潜在特征嵌入地图，并展示于 SDF 构建和开放词汇物体定位。
- 摘要声称该方法显著提升计算与内存效率，保持较高估计精度，并在大规模真实世界基准上赋予机器人空间感知能力。

### 局限性
- 摘要未提供足够信息说明具体实验数据集、评价指标、对比方法和定量结果。
- 摘要未提供足够信息说明方法在不同传感器模态、动态场景或极端规模下的适用性。
- 摘要未提供足够信息说明开放词汇物体定位的具体精度、失败案例或语义标签体系。
- 摘要未提供足够信息说明子图重叠策略、分层优化超参数、内存占用和运行时间的详细数值。
- 摘要未提供足够信息说明与现有方法的完整优缺点比较。

### 阅读优先级
中。理由：该论文主题覆盖 3D 重建、隐式表示、语义理解与机器人应用，若关注大规模神经隐式建图、几何与语义联合表示或开放词汇物体定位，具有较高相关性；但摘要未给出实验细节和定量验证，是否值得深入阅读需结合全文实验部分判断。

</details>

<details>
<summary>Abstract</summary>

Neural implicit representations have had a significant impact on scene reconstruction by enabling robots to build continuous, differentiable, and high-fidelity 3D maps. Most existing works focus on geometric reconstruction and lack semantic information for high-level spatial understanding and task planning. Also, as the scale and complexity of the environment increase, neural representations face the challenge of maintaining computational efficiency in back-end optimization. To resolve these two challenges, we introduce a hierarchical neural field that leverages multiresolution submaps to achieve an efficient and scalable implicit representation, and a unified query and decoding mechanism to support both geometric and semantic features. More specifically, the learnable map features can be converted to the output with the query and decoding process for both training and inference. For large-scale representation, we decompose a scene into overlapping submaps and do hierarchical optimization within each local submap, thus enabling scalable computation. To further improve efficiency, we design feature encoders that predict initial hierarchical grid features to substantially reduce the time needed to optimize the submap features from scratch. To correct estimation drift among submaps, we align and fuse them entirely within the implicit feature space, leading to substantial acceleration by avoiding the need to decode the final output. Building upon this efficient hierarchical representation, we embed both geometric features and vision-language latent features into the map, and demonstrate it on both Signed Distance Field (SDF) construction and open-vocabulary object grounding. Our approach significantly improves computation and memory efficiency, maintains high estimation accuracy, and endows the robot with spatial awareness on large-scale real-world benchmarks.

</details>

#### 2026-09-29 - All Roads Lead to Rome: Flow-driven Multi-Anchor Exploration for Open-Environment Active 3D Mapping

**Authors:** Yang Li, Aming Wu, Zihao Zhang, Ziju Han, Sijia Zhang, Yahong Han
**Links:** [abs](https://arxiv.org/abs/2609.36889) - [pdf](https://arxiv.org/pdf/2609.36889)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D mapping, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：All Roads Lead to Rome: Flow-driven Multi-Anchor Exploration for Open-Environment Active 3D Mapping
- 作者：Yang Li, Aming Wu, Zihao Zhang, Ziju Han, Sijia Zhang, Yahong Han
- 出版日期：2026-09-29T07:20:32Z
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.36889 ；https://arxiv.org/pdf/2609.36889

### 一句话总结
该论文针对开放环境主动三维建图中的长时程探索问题，将长程目标预测重构为基于条件流匹配的多模态锚点生成，以缓解单点确定性预测在部分可观测下易产生脆弱决策的问题。

### 研究问题
论文关注开放环境主动三维建图任务，目标是面向未知场景完成长时程且尽量最短轨迹的探索与重建。由于未知环境信息有限，建立在闭集假设上的方法（即假设测试环境与训练中见过的环境相似）难以令人满意地泛化。现有主动建图方法通常先预测一个粗略的远距离目标，再将其转换为可执行路径，但这一阶段常被建模为单点预测。在部分可观测条件下，同一局部观测可能对应多个合理的探索方向，因此确定性预测容易产生脆弱决策，并在未知场景中性能退化。论文实验进一步验证，这是其泛化能力较弱的关键因素之一。

### 核心思路/方法
论文将长时程目标预测重构为使用条件流匹配的条件多模态锚点生成。具体而言，不是预测单一目标，而是从当前建图状态中学习粗略探索锚点的条件分布。这些锚点首先通过障碍物感知规划转换为可执行的候选路径。随后，论文采用探索模式聚类来压缩几何上相似的轨迹并减少候选冗余。最后，使用分层选择模块选择最有前景的模式，并在该模式内对路径重新排序，从而产生最终可执行轨迹。

### 主要贡献
- 指出现有主动建图方法中单点预测远距离目标在部分可观测下容易产生脆弱决策，并认为这是泛化能力较弱的关键因素之一。
- 提出将长时程目标预测重构为使用条件流匹配的条件多模态锚点生成，学习当前建图状态下的探索锚点条件分布。
- 设计由障碍物感知规划、探索模式聚类和分层选择模块组成的流程，将多锚点转换为压缩后的候选路径并选出最终可执行轨迹。
- 摘要声称实验表明该方法提升了开放环境中的泛化能力和重建效率。

### 局限性
摘要未提供足够信息说明具体实验设置、数据集、基线方法、定量指标、计算开销、失败案例或方法在何种条件下可能失效。摘要未提供足够信息说明条件流匹配的训练细节、锚点数量选择、聚类与分层选择模块的具体实现及其消融结果。

### 阅读优先级
高。理由：该论文聚焦开放环境主动三维建图这一具身智能相关方向，问题定义明确，方法将条件流匹配引入长时程探索目标的多模态预测，并配套路径生成、聚类与分层选择流程，与3D重建、机器人及具身应用分类高度相关；若读者关注主动建图、开放环境泛化或长时程探索决策，该论文具有较高阅读价值。

</details>

<details>
<summary>Abstract</summary>

To advance the development of embodied intelligence, Open-Environment Active 3D Mapping has attracted increasing attention, aiming to perform a long-horizon and shortest trajectory exploration for reconstructing unseen scenarios. Since only limited information about unseen environments is available, methods built on the closed-set assumption, i.e., assuming that the test environments are similar to those seen during training, cannot generalize satisfactorily. In existing active mapping methods, long-horizon exploration is often guided by predicting a coarse long-range goal and then converting it into an executable path. However, this stage is usually formulated as single-point prediction. Under partial observability, the same local observation may correspond to multiple plausible exploration directions, making such deterministic prediction prone to brittle decisions and degraded performance in unseen scenarios. Our experiments further verify that this is a key factor underlying their weak generalization. To address this issue, we reformulate long-horizon target prediction as conditional multimodal anchor generation using Conditional Flow Matching.Instead of predicting a single goal, our method learns a conditional distribution over coarse exploration anchors from the current mapping state. These anchors are first converted into executable candidate paths through obstacle-aware planning. We then apply exploration-mode clustering to compress geometrically similar trajectories and reduce candidate redundancy. Finally, a hierarchical selection module selects the most promising mode and reranks paths within it to produce the final executable trajectory. Experiments show that our method improves generalization and reconstruction efficiency in open environments.

</details>

#### 2026-09-29 - Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM

**Authors:** Minseo Kim, Yina Kim, Jinhwa Hwang, Alex Junho Lee
**Links:** [abs](https://arxiv.org/abs/2609.36753) - [pdf](https://arxiv.org/pdf/2609.36753)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, robot navigation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM
- 作者：Minseo Kim, Yina Kim, Jinhwa Hwang, Alex Junho Lee
- 出版日期：2026-09-29T05:25:12Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.36753 ；PDF https://arxiv.org/pdf/2609.36753

### 一句话总结
针对长隧道、管道等轴向均匀走廊中 LiDAR 里程计沿特征贫弱方向漂移的结构性退化问题，论文提出一种与退化轴正交的横截面几何描述子 DeCOD，通过匹配管道接缝、结构环等横截面地标来约束纵向漂移，同时不约束绕公共轴的旋转。

### 研究问题
论文关注的是自主机器人导航中 LiDAR SLAM 的定位与建图问题。在长隧道和管道等轴向均匀走廊环境中，LiDAR 里程计存在结构性退化：沿特征贫弱的行进方向无法被约束，导致漂移。摘要明确指出，这种结构性退化无法仅靠局部扫描匹配解决。因此，研究问题是如何在几何退化条件下引入额外约束，抑制沿走廊轴向的纵向漂移。

### 核心思路/方法
论文提出 Degeneracy-orthogonal Contour Offset Descriptor（DeCOD），一种面向横截面地标的结构对齐几何描述子。其基本观察是：横截面边界，例如管道接缝和结构环，能够提供沿退化轴的度量约束；但由于这些横截面轮廓往往近乎相同，区分单个地标需要捕捉细微的表面变化。

方法要点包括：
- 描述子参数化方式：对估计的边界轮廓建模，使用带符号法向偏差作为描述内容。
- 匹配机制：显式解决朝向歧义，并通过畸变估计解耦一阶轮廓误差。
- 因子构建：匹配到的地标产生几何因子，在位姿图优化中约束横截面位置一致性与走廊轴向对齐，从而修正纵向漂移。
- 约束保留：该方法刻意不约束绕公共轴的旋转，即绕走廊轴的自由度仍保持不受约束。

### 主要贡献
- 提出 DeCOD，一种针对横截面地标的、与退化方向正交的结构对齐几何描述子。
- 利用横截面边界作为沿退化轴的度量约束来源，以应对局部扫描匹配无法解决的结构性退化。
- 通过描述子参数化与匹配机制处理近同轮廓的区分问题，包括朝向歧义与一阶轮廓误差。
- 将匹配地标转化为位姿图优化中的几何因子，修正纵向漂移并保持绕公共轴旋转不受约束。
- 摘要称在公开基准和现场实验中，DeCOD 相较标准 3D 描述子取得更稳健的地标检索，并能在不同里程计前端上稳定轨迹，在几何退化下可靠约束纵向漂移。

### 局限性
摘要未提供足够信息说明以下方面：具体实验平台、传感器配置、数据集名称与规模、对比方法细节、计算开销、实时性、失败场景、对非管道或非隧道环境的泛化能力、对横截面地标缺失或稀疏情况的鲁棒性，以及描述子对噪声和畸变的定量敏感度。摘要仅给出总体实验结论，未提供消融研究或误差指标的细节。

### 阅读优先级
中。理由：该论文针对 LiDAR SLAM 在长隧道、管道等退化环境中的纵向漂移问题，问题定义清晰，方法思路具有针对性，且摘要声称在公开基准与现场实验中验证了跨里程计前端的稳定性。但摘要未提供量化结果、数据集细节和失败条件，是否具有广泛适用性仍需阅读正文确认。若读者关注退化环境 SLAM、LiDAR 里程计约束或横截面地标匹配，优先级可调高；若仅泛读 SLAM 进展，可按中优先级处理。

</details>

<details>
<summary>Abstract</summary>

Autonomous robot navigation relies on simultaneous localization and mapping (SLAM) to estimate motion and maintain an accurate pose within an environment. However, in axially uniform corridors such as long tunnels and pipelines, LiDAR odometry is fundamentally limited by unconstrained drift along the feature-weak travel direction. This structural degeneracy cannot be resolved by local scan matching alone. To address this challenge, we propose the Degeneracy-orthogonal Contour Offset Descriptor (DeCOD), a structure-aligned geometric descriptor for cross-sectional landmarks. Cross-sectional boundaries, such as pipe joints and structural rings, provide metric constraints along this degenerate axis, but distinguishing individual landmarks requires capturing subtle surface variations across nearly identical profiles. The descriptor parameterizes signed normal deviation from estimated boundary contours, and matching explicitly resolves heading ambiguity and decouples first-order contour errors by distortion estimation. Matched landmarks yield geometric factors that enforce agreement in cross-section position and corridor axis alignment during pose-graph optimization, correcting longitudinal drift while leaving rotation about the common axis unconstrained. On a public benchmark and in field experiments, DeCOD achieves robust landmark retrieval over standard 3D descriptors and successfully stabilizes trajectories across different odometry frontends, reliably constraining longitudinal drift under geometric degeneracy.

</details>

#### 2026-09-29 - Distilling Privileged Control Barrier Functions into RGB-Only Safety Filters for Dynamic Visual Navigation

**Authors:** Seungyeon Yoo, Gawon Lee, Seungwoo Jung, Inkyu Jang, H. Jin Kim
**Links:** [abs](https://arxiv.org/abs/2609.36520) - [pdf](https://arxiv.org/pdf/2609.36520)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 3D reconstruction, scene reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Distilling Privileged Control Barrier Functions into RGB-Only Safety Filters for Dynamic Visual Navigation
- 作者：Seungyeon Yoo, Gawon Lee, Seungwoo Jung, Inkyu Jang, H. Jin Kim
- 出版日期：2026-09-29T02:12:33Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.36520) / [PDF](https://arxiv.org/pdf/2609.36520)

### 一句话总结
提出一种教师—学生视觉蒸馏框架，将使用特权状态信息的 CBF 教师安全行为迁移到仅依赖 RGB 历史、机器人速度和名义控制动作的学生安全滤波器中，以提升动态视觉导航的安全性。

### 研究问题
仅依赖 RGB 的端到端视觉导航策略在真实动态环境中仍容易发生碰撞，因此需要专门的安全层。现有视觉 CBF 方法虽尝试从 RGB 观测提供安全性，但通常依赖实时渲染或显式场景重建，且主要面向静态场景，限制了其在机载部署中的实用性。论文关注的核心问题是：如何在不进行显式三维重建或在线渲染的前提下，为动态环境中的 RGB 视觉导航提供有效的安全滤波。

### 核心思路/方法
论文提出教师—学生视觉蒸馏框架：
- 教师：使用真实机器人状态和障碍物状态作为特权信息，在 real-to-sim 动态 Gaussian Splatting 环境中构建 CBF 安全约束。
- 学生：直接将短 RGB 历史、机器人速度和名义控制动作映射为安全动作，部署时仅需 RGB 观测和机器人速度，不需要显式三维重建或在线渲染。
- 为缩小教师与学生之间的信息差距，教师仅从学生 RGB 历史中可观测到的障碍物构建安全约束。
- 教师还考虑障碍物速度不确定性，以提升对运动变化的鲁棒性。
- 通过动作增强让学生接触多样化的安全与不安全名义动作，从而更好地捕捉安全边界。

### 主要贡献
- 提出一种教师—学生视觉蒸馏框架，将特权 CBF 教师的安全行为迁移到仅 RGB 的学生安全滤波器。
- 教师基于 real-to-sim 动态 Gaussian Splatting 环境，并仅利用学生 RGB 历史中可观测的障碍物构建安全约束，以减小教师—学生信息差距。
- 教师在安全约束中考虑障碍物速度不确定性，并通过动作增强提升学生对安全边界的捕捉能力。
- 部署阶段学生仅需 RGB 观测和机器人速度，无需显式三维重建或在线渲染。
- 摘要称实验表明该方法优于视觉 CBF 基线，并提升了基于 RGB 的导航策略在动态障碍物运动下的安全性。

### 局限性
摘要未提供足够信息说明以下方面：具体实验设置、数据集与评测指标、真实世界部署验证范围、计算开销与实时性数据、失败案例、对不同传感器噪声或光照条件的鲁棒性、教师—学生信息差距的定量分析，以及方法在更复杂动态场景中的泛化能力。此外，论文分类虽包含 3D Reconstruction 与 Neural Scene Representations & Rendering，但摘要未详细说明 Gaussian Splatting 环境构建与训练的具体技术细节。

### 阅读优先级
高。理由：该论文针对 RGB-only 动态视觉导航中的安全滤波问题，结合 CBF、教师—学生蒸馏和 Gaussian Splatting 环境，问题定位明确且具有机载部署导向；若读者关注视觉导航安全、CBF 安全层、 privileged learning 或动态场景中的 sim-to-real 迁移，该论文具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

RGB-only end-to-end visual navigation policies remain vulnerable to collisions in real-world dynamic environments, motivating a dedicated safety layer. Existing visual Control Barrier Function (CBF) approaches seek to provide safety from RGB observations, but often rely on real-time rendering or explicit scene reconstruction and are primarily designed for static scenes, limiting their practicality for onboard deployment. We propose a teacher-student visual distillation framework that transfers the safety behavior of a privileged CBF teacher to an RGB-only student filter for dynamic environments. The student maps a short RGB history, robot velocity, and a nominal control action directly to a safe action, while the teacher uses ground-truth robot and obstacle states in a real-to-sim dynamic Gaussian Splatting environment. To reduce the teacher-student information gap, the teacher constructs safety constraints only from obstacles observable within the student's RGB history. It also accounts for obstacle-velocity uncertainty to improve robustness to motion variations, while action augmentation exposes the student to diverse safe and unsafe nominal actions to better capture the safety boundary. At deployment, the student requires only RGB observations and robot velocity, without explicit 3D reconstruction or online rendering. Experiments show that the proposed method outperforms visual CBF baselines and improves the safety of RGB-based navigation policies under dynamic obstacle motion. Project page: https://syeon-yoo.github.io/distill-cbf-site/.

</details>

#### 2026-09-28 - VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction

**Authors:** Conghan Yue, Yuanjie Chen, Yue Han, Ya Gao, Yunyan Xiao, WeiYao Zhang, Zhineng Chen
**Links:** [abs](https://arxiv.org/abs/2609.35134) - [pdf](https://arxiv.org/pdf/2609.35134)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction
- 作者：Conghan Yue, Yuanjie Chen, Yue Han, Ya Gao, Yunyan Xiao, WeiYao Zhang, Zhineng Chen
- 出版日期：2026-09-28T13:25:37Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.35134 ；PDF https://arxiv.org/pdf/2609.35134 ；代码 https://github.com/Hammour-steak/VideoPhysEdit

### 一句话总结
VideoPhysEdit 提出一种免训练流程，通过刚体物理场景重建显式进行物理推理，以生成物理反事实视频编辑结果，并配套构建基准与评价指标。

### 研究问题
论文关注“物理反事实视频编辑”（PCVE）：给定源视频、一个物理编辑及其执行帧，生成描绘编辑后运动与交互结果的视频。既有视频编辑方法多关注阴影、遮挡等视觉后果，而对编辑引发的后续运动与交互等物理后果探索不足。PCVE 的难点在于需要理解场景物理、推断物理干预引起的下游运动与交互，同时缺乏成对的事实/反事实数据和专门评价指标。

### 核心思路/方法
论文提出 VideoPhysEdit，一个面向刚体场景的免训练 PCVE 流程。其核心是通过一种新的物理场景重建方法使物理推理显式化：重建出的场景能够在仿真下复现观察到的运动与交互，从而支持将物理编辑作为干预施加，并利用产生的轨迹引导反事实视频生成。论文还构建了 PCVE-RigidBench 合成基准，包含成对的源视频与反事实目标视频以及物理真值，并提出 Physical Edit Score 指标。

### 主要贡献
- 形式化定义了物理反事实视频编辑（PCVE）任务。
- 提出免训练流程 VideoPhysEdit，通过刚体物理场景重建实现显式物理推理，并用仿真轨迹引导反事实视频生成。
- 构建 PCVE-RigidBench 合成基准，提供成对源视频、反事实目标视频与物理真值。
- 提出 Physical Edit Score 评价指标。
- 实验显示 VideoPhysEdit 在物理编辑准确率上显著高于开源方法与商业模型，同时保持有竞争力的视觉保真度，其 Physical Edit Score 为 0.376，是对比方法中唯一为正的分数；真实视频定性比较显示其适用于真实场景，并比对比方法更好地描绘编辑引发的下游运动与交互。

### 局限性
摘要未提供足够信息说明方法在非刚体场景、复杂真实场景泛化能力、计算成本、失败案例或基准多样性方面的具体局限；仅可从摘要推断其方法面向刚体场景，且基准为合成基准，但摘要未给出进一步局限讨论。

### 阅读优先级
高。理由：论文提出新的任务定义 PCVE，并同时给出方法、合成基准与评价指标，属于问题设定与方法/评测配套的工作；且摘要声称在物理编辑准确率上显著优于开源与商业方法，并报告唯一正值的 Physical Edit Score，对视频编辑、物理推理、3D 重建与多视图几何交叉方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Video editing has advanced substantially in recent years, with methods increasingly accounting for the visual consequences of edits, such as changes to shadows and occlusions. However, the physical consequences of edits, including changes to subsequent motion and interactions, remain less explored. We formulate this problem as physical counterfactual video editing (PCVE), which aims to generate a counterfactual video depicting the resulting motion and interactions given a source video, a physical edit, and its execution frame. PCVE is challenging because it requires understanding scene physics and inferring the downstream motion and interactions induced by a physical intervention, while paired factual and counterfactual data and dedicated evaluation metrics are lacking. We introduce VideoPhysEdit, a new training-free pipeline for PCVE in rigid-body scenes. It makes physical reasoning explicit through a novel physical scene reconstruction method that recovers a scene reproducing the observed motion and interactions under simulation, enabling the pipeline to apply physical edits as interventions and use the resulting trajectories to guide counterfactual video generation. We further construct PCVE-RigidBench, a synthetic benchmark with paired source and counterfactual target videos and physical ground truth, and introduce the Physical Edit Score. VideoPhysEdit achieves substantially higher physical edit accuracy than open-source methods and commercial models while maintaining competitive visual fidelity. Its Physical Edit Score is 0.376, the only positive score among the compared methods. Qualitative comparisons on real videos further show that VideoPhysEdit applies to real-world scenes and better depicts the downstream motion and interactions induced by the edits than the compared methods. Code: https://github.com/Hammour-steak/VideoPhysEdit

</details>

#### 2026-09-28 - LEGAU: Learning Semantic Gaussian Priors for Scalable Category-level Pose Estimation

**Authors:** Hongli Xu, Zhaowei Lu, Junwen Huang, Jiaqi Hu, Peter KT Yu, Benjamin Busam, Federico Tombari, Slobodan ilic
**Links:** [abs](https://arxiv.org/abs/2609.35046) - [pdf](https://arxiv.org/pdf/2609.35046)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LEGAU: Learning Semantic Gaussian Priors for Scalable Category-level Pose Estimation
- 作者：Hongli Xu, Zhaowei Lu, Junwen Huang, Jiaqi Hu, Peter KT Yu, Benjamin Busam, Federico Tombari, Slobodan ilic
- 出版日期：2026-09-28T12:42:19Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.35046 ；PDF https://arxiv.org/pdf/2609.35046

### 一句话总结
LEGAU 通过联合预测 NOCS 对应、物体位姿与尺寸、以及规范化语义高斯场，将高斯场作为类别条件下的结构先验参与多模态特征融合，从而提升类别级 6D 位姿估计的可扩展性。

### 研究问题
单张 RGB-D 观测下的类别级 6D 位姿估计本质上是欠约束问题：需要在部分可见几何的基础上，结合物体的规范化结构才能确定稳定位姿。摘要指出，该任务需要同时解释局部可见几何与全局规范结构，因此如何有效耦合形状表征与位姿推理是关键问题。

### 核心思路/方法
LEGAU 是一个统一框架，同时预测三部分输出：NOCS 对应、物体位姿与尺寸、以及规范语义高斯场。其核心设计不是把重建当作独立的辅助任务，而是将高斯场作为“类别条件下的结构先验”，参与多模态特征融合，并为局部位姿推理提供全局引导。方法以类别文本嵌入为条件，通过基于 transformer 的融合模块处理 RGB-D 观测，整合视觉、几何与类别级线索，最终解码出 NOCS 图、位姿与尺寸信息以及基于高斯的物体表征。

### 主要贡献
- 提出统一框架 LEGAU，联合学习规范对应、物体形状与位姿对齐。
- 将语义高斯场作为类别条件结构先验，融入多模态特征融合并引导局部位姿推理，而非作为分离的辅助重建任务。
- 在合成与真实世界基准上验证了该耦合位姿-形状公式在单模型多类别设定下的性能，摘要称在 SOPE 上最高提升 22%，并具有竞争力的真实数据迁移表现。

### 局限性
摘要未提供足够信息。摘要未说明具体失败场景、计算开销、对类别文本嵌入质量的依赖、真实数据迁移的具体限制或消融分析的细节。

### 阅读优先级
中。理由：该论文关注类别级 6D 位姿估计中形状先验与位姿推理的耦合，属于 3D 重建与多视图几何方向，且摘要报告了较明显的性能提升；但摘要未提供足够实验细节与局限说明，是否值得深入精读需结合全文的实验设计、基线对比与真实场景泛化能力进一步判断。

</details>

<details>
<summary>Abstract</summary>

Category-level 6D pose estimation from a single RGB-D observation is inherently under-constrained, since partial visible geometry must be interpreted together with a canonical object structure before a stable pose can be determined. We present LEGAU, a unified framework that jointly predicts NOCS correspondence, object pose and size, and a canonical Semantic Gaussian Field. Rather than treating reconstruction as a detached auxiliary task, LEGAU uses the Gaussian field as a category-conditioned structural prior that participates in multimodal feature fusion and provides global guidance for local pose reasoning. Conditioned on a categorical text embedding, LEGAU processes RGB-D observations through a transformer-based fusion module that integrates visual, geometric, and category-level cues, decoding the NOCS map, pose and size information and the Gaussian-based object representation. Extensive experiments on synthetic and real-world benchmarks show that this coupled pose-shape formulation achieves strong performance in a single-model multi-category setting, with up to 22\% on SOPE and competitive transfer to real-world data. These results highlight the benefit of jointly learning canonical correspondence, object shape, and pose alignment within a unified representation.

</details>

#### 2026-09-28 - Functional Hand Type Prior for 3D Hand Pose Estimation and Action Recognition from Egocentric View Monocular Videos

**Authors:** Wonseok Roh, Seung Hyun Lee, Won Jeong Ryoo, Jakyung Lee, Gyeongrok Oh, Sooyeon Hwang, Hyung-gun Chi, Sangpil Kim
**Links:** [abs](https://arxiv.org/abs/2609.34149) - [pdf](https://arxiv.org/pdf/2609.34149)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Functional Hand Type Prior for 3D Hand Pose Estimation and Action Recognition from Egocentric View Monocular Videos
- 作者：Wonseok Roh, Seung Hyun Lee, Won Jeong Ryoo, Jakyung Lee, Gyeongrok Oh, Sooyeon Hwang, Hyung-gun Chi, Sangpil Kim
- 出版日期：2026-09-28T02:29:40Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类；次要分类摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2609.34149) / [PDF](https://arxiv.org/pdf/2609.34149)

### 一句话总结
论文提出以“功能性手部类型”作为先验，通过估计三维手部姿态、物体类别与手部类型，并聚合长时段逐帧知识，提升第一视角单目视频中的动作识别性能。

### 研究问题
当前第一视角动作识别方法在感知动态手部运动时，往往仅依赖几何或物理信息，难以充分理解真实场景中的细粒度交互。论文希望解决如何利用手部功能配置与物体之间的关联，来增强对连续手部交互的解释能力。

### 核心思路/方法
论文从功能视角引入一种实用的手部类型分类体系，并基于该体系对现有数据集进行逐帧手部类型标注。随后提出一个考虑手部类型语义细节作为先验的手部动作识别框架，以增强网络对动作序列中连续手部交互的理解。

整体流程包含三个主要模块：
1. **Feature Extraction**：特征提取。
2. **Egocentric Knowledge Module**：利用短时线索估计三维手部姿态、物体类别和手部类型。
3. **Egocentric Action Module**：在更长时间范围内聚合逐帧知识，包括手部类型的文本嵌入。

### 主要贡献
- 从功能视角提出一种实用的手部类型分类体系，并用于现有数据集的逐帧手部类型标注。
- 提出一种新的手部动作识别框架，将手部类型的语义细节作为先验纳入建模。
- 设计包含特征提取、第一视角知识模块和第一视角动作模块的整体流程，其中动作模块聚合逐帧知识及手部类型文本嵌入，以增强对连续手部交互的理解。
- 在大规模基准 FPHA 和 H2O 上的广泛实验表明，模型优于当前最先进方法，展示出更优性能。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法的具体失败场景、计算开销、对标注质量的依赖程度、跨数据集泛化限制或消融实验细节。

### 阅读优先级
中。理由：论文聚焦第一视角单目视频中的三维手部姿态估计与动作识别，并提出“功能性手部类型先验”这一较有辨识度的建模思路，且声称在 FPHA 和 H2O 上优于现有方法；但摘要未提供足够实验细节、方法限制与可复现信息，是否值得深入阅读需结合全文中的实验设置、消融与泛化分析进一步判断。

</details>

<details>
<summary>Abstract</summary>

Current methods for egocentric view action recognition often face challenges in perceiving dynamic hand movements relying solely on geometrical or physical information. In this work, we effectively address this problem by gaining insights into the correlation between functional hand configurations and objects, which improves the detailed interpretation of real-world scenarios. To this end, we introduce a practical taxonomy of hand types based on the functioning perspective and utilize it for per-frame hand type labeling on existing datasets. We also propose a novel hand action recognition framework considering semantic details of the hand type as prior. This approach boosts the network's understanding of the continuous hand interaction throughout the action sequence. Our whole pipeline consists of three main modules: (1) Feature Extraction, (2) Egocentric Knowledge Module, which estimates 3D hand pose, object category, and hand type leveraging short-term cues, and (2) Egocentric Action Module, which aggregates per-frame knowledge, including text embeddings of hand type, over a longer time. In our extensive experiments with large-scale benchmarks, FPHA and H2O, our model outperforms current state-of-the-art methods, demonstrating its superior performance.

</details>

#### 2026-09-27 - EpiTransfer: Sparse, Training-Free Long-Range Depth Estimation from Temporal Monocular Aerial Frames

**Authors:** Diksha Aggarwal, Rutvik Dagadkhair, Sanjana Srivastava, Bradley Denby, Kevin Kochersberger
**Links:** [abs](https://arxiv.org/abs/2609.33939) - [pdf](https://arxiv.org/pdf/2609.33939)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EpiTransfer: Sparse, Training-Free Long-Range Depth Estimation from Temporal Monocular Aerial Frames
- 作者：Diksha Aggarwal, Rutvik Dagadkhair, Sanjana Srivastava, Bradley Denby, Kevin Kochersberger
- 出版日期：2026-09-27T21:30:23Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.33939

### 一句话总结
本文提出一种无需训练、基于对极转移（epipolar transfer）的深度估计方法，仅用两帧单目图像和相机位姿估计，通过合成虚拟立体对将时间对应转化为立体三角化任务，在无人机与室内场景中表现优于未针对该域训练的现成学习基线。

### 研究问题
可靠的三维空间理解对自主导航、避障和场景重建至关重要。现有学习型深度估计方法在分布内精度高，但对新视角和新高度泛化能力差。论文希望在无需训练数据的条件下，利用稀疏单目航拍时序帧实现长距离深度估计。

### 核心思路/方法
- 采用几何推导的、无需训练（training-free）的深度估计方法。
- 输入仅为两张单目图像和相机位姿估计。
- 利用相机运动合成一个基线可自由选择的虚拟立体对。
- 将时序对应问题转化为立体三角化任务。
- 该方法旨在缓解直接双视图三角化固有的几何退化问题。
- 验证场景包括户外无人机飞行（最大约 90 m 范围）和室内 OptiTrack 环境，并以 LiDAR 真值作为参考。

### 主要贡献
- 提出一种几何推导、无需训练、稀疏的长距离深度估计方法，仅依赖两帧单目图像与相机位姿。
- 通过合成虚拟立体对，将时序对应转化为立体三角化，以缓解直接双视图三角化的几何退化。
- 在户外无人机飞行与室内 OptiTrack 环境中使用 LiDAR 真值验证，室内达到 AbsRel 0.092、δ<1.25 为 0.940。
- 与直接三角化（AbsRel 0.073）精度相当，但在更具挑战性的场景中保留有效深度的比例更大。
- 显著优于未针对该域训练或微调的现成学习基线 ZoeDepth（AbsRel 0.225）和 Depth Anything V2（AbsRel 0.570），且无需训练数据。

### 局限性
- 摘要仅给出室内 AbsRel 与 δ<1.25 指标，户外场景的量化结果摘要未提供足够信息。
- 摘要未提供方法对相机位姿估计误差的敏感性分析，摘要未提供足够信息。
- 摘要未提供不同基线选择策略的具体影响，摘要未提供足够信息。
- 摘要未提供计算效率或实时性数据，摘要未提供足够信息。
- 摘要未提供与直接三角化相比在哪些具体挑战场景下有效深度比例更大的细节，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文聚焦无需训练、仅依赖两帧单目航拍图像与相机位姿的长距离深度估计，问题设定明确，且提供了与 LiDAR 真值及多个现成学习基线的定量对比；对三维重建、多视图几何和空中自主导航方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Reliable 3D spatial understanding is essential for autonomous navigation, obstacle avoidance, and scene reconstruction. While state-of-the-art learned depth estimation techniques achieve high accuracy in-distribution, they often generalize poorly to novel viewpoints and altitudes. This paper presents a geometrically derived, training-free depth estimation method using epipolar transfer with only two monocular images and camera pose estimates. By leveraging camera motion to synthesize a virtual stereo pair with a freely chosen baseline, our approach transforms temporal correspondence into a stereo triangulation task while mitigating geometric degeneracies inherent to direct two-view triangulation. Validated across outdoor drone flights (to a maximum range of approximately 90\,m) and indoor OptiTrack environments against LiDAR ground truth, the method achieves an indoor AbsRel of 0.092 and $δ< 1.25$ of 0.940, comparable to direct triangulation (AbsRel 0.073) while retaining valid depth over a larger fraction of challenging scenes, and substantially outperforms off-the-shelf learning-based baselines such as ZoeDepth (AbsRel 0.225) and Depth Anything V2 (AbsRel 0.570), which are not trained or fine-tuned for this domain, with no training data required.

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-01 - EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation

**Authors:** Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang
**Links:** [abs](https://arxiv.org/abs/2610.01876) - [pdf](https://arxiv.org/pdf/2610.01876)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation
- 作者：Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang
- 出版日期：2026-10-01T15:32:49Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.01876) / [PDF](https://arxiv.org/pdf/2610.01876)

### 一句话总结
EvenSplat 通过耦合图像空间的光照分解与高斯所携带的光照场，并引入相机响应网络与局部曝光补偿模块，以在曝光和光照变化下改进 3D Gaussian Splatting 的重建效果。

### 研究问题
论文关注的是在曝光变化和光照不均匀条件下的多视角重建问题。摘要指出，同一表面在均匀光照下从不同角度看起来几乎一致，但在不均匀光照下则不然；视角之间存在曝光变化、单张图像内部存在光照变化、局部强光源还会造成亮暗并存的区域。3D Gaussian Splatting 等方法会把这类光照伪影当作场景本身属性，从而把采集相关的光照与几何、颜色纠缠在一起。

### 核心思路/方法
EvenSplat 的核心是将采集相关的光照影响与场景本身的几何和颜色分离。具体而言，该方法耦合了图像空间的光照分解与由高斯携带的光照场，使二维视图和三维视图共享同一套对光照的解释；同时使用相机响应网络和局部曝光补偿模块来吸收训练图像之间残留的全局与局部差异。

### 主要贡献
- 提出 EvenSplat 框架，用于在曝光和光照变化下进行高斯泼溅重建。
- 将图像空间光照分解与高斯携带的光照场进行耦合，使 2D 与 3D 视图共享对光照的解释。
- 引入相机响应网络和局部曝光补偿模块，处理跨训练图像的全局与残余差异。
- 摘要称在多个数据集及多种不均匀光照形式（跨视角曝光、空间光照变化、高对比度光照）上，在真实采集和模拟基准中总体优于当前先进方法，尤其在高对比度光照下表现突出。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败场景、计算开销、对极端或未知光照条件的泛化能力、对特定数据假设的依赖，以及消融实验细节等。

### 阅读优先级
高。理由是论文针对 3D Gaussian Splatting 在曝光和光照变化下将光照伪影与场景属性纠缠的问题提出分离思路，且摘要声称在多种不均匀光照和多个基准上总体优于现有方法，尤其在高对比度光照下表现突出；该主题与神经场景表示与渲染方向直接相关。

</details>

<details>
<summary>Abstract</summary>

A surface photographed under even light presents nearly the same appearance from every angle; the same surface under uneven light does not. Exposure changes between views, illumination varies within a single image, and locally strong light sources leave one region bright and its neighbor in shadow. Multi-view reconstruction methods such as 3D Gaussian Splatting treat these lighting artifacts as if they were properties of the scene, entangling capture-specific illumination with the geometry and color they recover. We present EvenSplat, a framework that separates the two. EvenSplat couples an image-space illumination decomposition with an illumination field carried by the Gaussians, so that the same explanation of the lighting is shared between the two-dimensional and three-dimensional views of the scene; a camera-response network and a local exposure-compensation module absorb the global and residual differences that remain across training images. Through extensive experiments across multiple datasets and diverse forms of uneven illumination (cross-view exposure, spatial illumination variation, and high-contrast lighting) on both real-world captured and simulated benchmarks, EvenSplat generally outperforms state-of-the-art methods, particularly under high-contrast illumination.

</details>

#### 2026-10-01 - Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation

**Authors:** Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai
**Links:** [abs](https://arxiv.org/abs/2610.01114) - [pdf](https://arxiv.org/pdf/2610.01114)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation
- 作者：Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai
- 出版日期：2026-10-01T05:52:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.01114 ；PDF https://arxiv.org/pdf/2610.01114

### 一句话总结
本文提出一种仿射对齐图集（affine-aligned atlas）下的规范高斯表示，通过帧级仿射变换先吸收全局运动，再构建规范高斯，以缓解大相机运动视频中规范表示与各帧失配的问题。

### 研究问题
现有基于高斯的视频表示通常将视频分解为规范高斯（canonical Gaussians）与时间形变（temporal deformation）。但当视频包含较大全局运动（如相机移动）时，规范表示可能与单帧图像发生错位，从而加重时间形变模型的负担。论文关注的核心问题是：如何减少规范表示与目标帧之间的差距，尤其在全局运动较大的视频序列中提升重建质量。

### 核心思路/方法
论文提出“仿射图集规范高斯表示”：在一个更大的仿射对齐图集空间中构建规范高斯。具体而言，先对每一帧应用仿射变换以吸收全局运动，然后再进行规范高斯构建，从而缩小规范表示与目标帧之间的差距。作者强调，该方法只修改规范构建阶段，因此可以集成到已有的基于规范高斯的方法中，且额外参数开销可忽略。

### 主要贡献
- 提出一种仿射对齐图集空间中的规范高斯表示，用于视频表示中的规范高斯构建。
- 通过帧级仿射变换在构建规范高斯前吸收全局运动，缓解规范表示与单帧之间的错位问题。
- 方法仅修改规范构建阶段，可集成到现有基于规范高斯的方法中，且额外参数成本可忽略。
- 实验显示，该方法尤其在相机运动较大的序列上提升了重建质量。

### 局限性
摘要未提供足够信息。摘要中未说明具体实验数据集、评价指标、与哪些基线方法比较、仿射变换如何估计、是否处理非全局运动或复杂动态场景、计算开销的具体数值、失败案例或方法适用边界。上述内容均需参考原文进一步确认。

### 阅读优先级
中。理由：该工作针对基于高斯的视频表示中“大全局运动导致规范表示失配”这一明确问题，提出阶段局部修改且易于集成的方案，对关注高斯泼溅、视频表示与神经场景表示的研究者有参考价值；但摘要未提供实验设置、量化结果和实现细节，且论文分类为神经场景表示与渲染，是否具有广泛跨领域影响需进一步阅读原文判断。

</details>

<details>
<summary>Abstract</summary>

Gaussian splatting has recently emerged as an efficient representation for images and videos due to its explicit structure and fast rendering capability. Existing Gaussian-based video representations often decompose a video into canonical Gaussians and temporal deformation. However, when a video contains large global motion such as camera movement, the canonical representation may become misaligned with individual frames, increasing the burden on the temporal deformation model. In this paper, we propose an affine-atlas canonical Gaussian representation, which constructs canonical Gaussians in a larger affine-aligned atlas space. Frame-wise affine transforms absorb global motion before canonical Gaussian construction, reducing the gap between the canonical representation and target frames. Since the proposed method only modifies the canonical construction stage, it can be integrated into existing canonical-Gaussian-based methods with negligible additional parameter cost. Experiments show that our method improves reconstruction quality especially for sequences with large camera motion.

</details>

### 2026-09

#### 2026-09-30 - TRACE: Privacy-Preserving Next-Best-View Selection over Distributed 3D Gaussian-Splat Maps

**Authors:** Amirhossein Mollaei Khass, Athanasios Cosse, Qiyu Sun, Nader Motee
**Links:** [abs](https://arxiv.org/abs/2610.00822) - [pdf](https://arxiv.org/pdf/2610.00822)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TRACE: Privacy-Preserving Next-Best-View Selection over Distributed 3D Gaussian-Splat Maps
- 作者：Amirhossein Mollaei Khass, Athanasios Cosse, Qiyu Sun, Nader Motee
- 出版日期：2026-09-30T23:32:16Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.00822 ，PDF：https://arxiv.org/pdf/2610.00822

### 一句话总结
在多个机器人各自维护私有 3D Gaussian Splatting 地图的场景下，TRACE 通过只交换与视图选择相关的两类射线聚合量，在不共享 splats 的前提下近似复现集中式的 next-best-view 选择。

### 研究问题
多个机器人各自构建并私有保存自己的 3D Gaussian Splatting 地图时，如何进行 next-best-view 选择。单个机器人候选视图的期望信息增益（EIG）由所有机器人地图共同决定，因为其他机器人的 splats 会遮挡它自己的 splats、也会在其后方发光，因此 EIG 需要针对合并后的地图评估。但没有任何一个机器人拥有这个合并地图，问题在于如何在不共享地图的情况下完成这一评估。

### 核心思路/方法
论文指出，地图之间的耦合只通过两个射线量传导：某个 splat 前方的透射率（transmittance）和其后的辐射亮度（radiance），而这两者都是沿射线命中点的求和。因此它们可以按机器人分解：每个机器人沿候选视图的射线，在自己的地图上按深度分箱（depth bins）对这两个量求和，并把和及其相对位姿的导数发送出去。规划视图的机器人据此恢复出自己的 EIG 及其在 SO(3) 上的梯度。用于 EIG 通信的这两个量称为 Transmittance and Radiance Aggregates，协议因此命名为 TRACE。机器人不共享 splats，且消息大小不随地图规模增长。

### 主要贡献
- 提出 TRACE 协议，使各机器人无需共享私有 3D Gaussian Splatting 地图，即可协同进行 next-best-view 选择。
- 证明 EIG 的跨地图耦合可通过透射率与辐射亮度两类射线聚合量分解，并由各机器人按深度分箱在本地计算后通信。
- 给出的通信内容仅为聚合量及其位姿导数，且消息大小不随地图规模增长。
- 证明在某一 splat 之后的深度分箱未混合两个机器人的命中点时，重建是精确的，并给出否则的误差上界。
- 在 Habitat-Sim 中进行了超过 100 次 next-best-view 决策，TRACE 在 83.3% 的情况下选出的朝向与集中式结果相差在 15 度以内，其视图达到集中式 EIG 的 97.9%。

### 局限性
- 精确重建有一个前提条件：某一 splat 之后的深度分箱不能混合来自两个机器人的命中点；摘要仅说明在此条件下精确、否则给出误差上界，未说明该条件在实际场景中出现的频率或影响程度。
- 摘要未提供足够信息说明实验中的机器人数量、地图规模、通信开销实测、不同场景类型或与更多基线方法的对比。
- 摘要未提供足够信息说明透射率与辐射亮度聚合量通信的隐私强度分析（例如是否可能反推出地图信息）。
- 摘要未提供足够信息说明深度分箱的具体划分方式及其对精度与通信量的影响。

### 阅读优先级
中。理由：该工作面向多机器人分布式 3D Gaussian Splatting 地图下的隐私保护 next-best-view 选择，问题设定明确、方法有理论分解与误差界，并给出量化实验指标；但摘要未提供足够信息以判断隐私保障强度、实际通信开销和多场景泛化性，适合对分布式神经渲染、隐私保护多机器人规划感兴趣的读者进一步阅读。

</details>

<details>
<summary>Abstract</summary>

Share the light, not the map. We study next-best-view selection for a team of robots, each of which builds its own 3D Gaussian Splatting map and keeps it private. A robot picks the view with the largest expected information gain (EIG) about the splats along its own path. This gain depends on the other maps. Their splats occlude its own and shine behind them, so the gain has to be evaluated against the pooled map. No robot has this map. We show that the coupling passes through only two ray quantities, the transmittance in front of a splat and the radiance behind it, and that both are sums over the hits of the ray. Hence, they decompose across the robots, and each robot sums them over depth bins in its own map, along the rays of a candidate view, and sends the sums with their pose derivatives. The robot planning the view turns them into its EIG and gradient on SO(3). Transmittance and Radiance Aggregates, communicated for the EIG, give the protocol its name: TRACE. No robot shares its splats, and the message size does not grow with a map. We prove that the reconstruction is exact unless a depth bin behind a splat mixes hits of two robots, and we bound the error otherwise. Over 100 next-best-view decisions in Habitat-Sim, TRACE picks a heading within 15 degrees of the centralized one in 83.3% of the cases, and its views reach 97.9% of the centralized EIG.

</details>

#### 2026-09-30 - What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting

**Authors:** Rezvan Joshaghani, Steven Cutchin
**Links:** [abs](https://arxiv.org/abs/2610.00749) - [pdf](https://arxiv.org/pdf/2610.00749)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting
- 作者：Rezvan Joshaghani, Steven Cutchin
- 出版日期：2026-09-30T21:41:52Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.00749

### 一句话总结
该研究通过分离亮度与色度通道监督来训练 3DGS 模型，发现标准 3DGS 的几何形成强烈由亮度主导但并非完全排他，且色度外观可在空间支持形成后重新拟合恢复。

### 研究问题
标准 3D Gaussian Splatting (3DGS) 从 RGB 监督中联合学习几何与外观，难以分离亮度和色度对学习表示的贡献。论文试图回答：亮度和色度分别如何影响 3DGS 的几何学习和重建质量？

### 核心思路/方法
- 在不同通道监督下训练模型（亮度单独、色度单独、RGB 等），并冻结非外观参数（位置、尺度、旋转、不透明度）。
- 使用相同的求解器重新估计外观，然后比较留出重建（held-out reconstruction）结果。
- 在 11 个基准场景上，每个场景进行 4 次独立运行。
- 比较高阶球谐函数对亮度和色度重建质量的贡献差异。
- 通过删除色度后重新拟合，测试在冻结几何上恢复色度外观的能力。
- 对比仅色度监督与仅亮度监督产生的几何质量差距，并分析密化（densification）对差距的解释程度。

### 主要贡献
- 量化了仅亮度监督学习的几何与 RGB 训练几何在留出重建上的平均差距仅为 0.085 dB。
- 发现从训练模型删除色度后，足够表达力的求解器可在冻结几何上重新拟合色度至原始质量或略好。
- 揭示高阶球谐函数对亮度的重建质量贡献远大于对色度的贡献（平均 PSNR 提升 1.44 dB vs 0.19 dB），尽管在镜面表面上色调仍随视角变化。
- 证明几何形成阶段亮度优势更大，仅色度监督产生的几何在相同外观求解后比仅亮度监督差 3.9–5.5 dB，密化可解释部分差距。
- 总体结论：标准 3DGS 的几何形成强烈由亮度主导但非亮度排他，大部分色度外观可在空间支持形成后恢复。

### 局限性
摘要未提供足够信息。论文摘要未提及方法的适用场景限制、失败案例、计算成本分析或对非基准数据集的泛化能力。

### 阅读优先级
高。该研究直接挑战 3DGS 中几何与外观联合学习的常见假设，通过受控实验分离亮度与色度贡献，对理解 3DGS 表示学习机制有重要价值，且结论可能影响后续外观建模和压缩策略的设计。

</details>

<details>
<summary>Abstract</summary>

Standard 3D Gaussian Splatting (3DGS) learns geometry and appearance jointly from RGB supervision, making it difficult to isolate how luminance and chroma contribute to the learned representation. We study this by training models under different channel supervision, freezing their non-appearance parameters (position, scale, rotation, and opacity), and re-estimating appearance with the same solver before comparing held-out reconstruction. Across eleven benchmark scenes with four independent runs each, geometry learned from luminance alone supports held-out reconstruction 0.085 dB below RGB-trained geometry on average. If chroma is deleted from a trained model, a sufficiently expressive solver can re-fit it on the frozen geometry to the original quality or slightly better. Higher-order spherical harmonics contribute much more reconstruction quality to luminance than to chroma, improving PSNR by 1.44 dB versus 0.19 dB on average, although on mirror-like surfaces hue does still change with viewpoint. The luminance advantage is even larger when geometry is being formed. Chroma-only supervision produces geometry 3.9-5.5 dB worse than luminance-only supervision after the same appearance solve; densification explains part of this gap. Overall, geometry formation in standard 3DGS is strongly luminance-dominated but not luminance-exclusive, and much of the chromatic appearance can be recovered after spatial support has formed.

</details>

#### 2026-09-30 - Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems

**Authors:** Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li
**Links:** [abs](https://arxiv.org/abs/2610.00618) - [pdf](https://arxiv.org/pdf/2610.00618)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems
- 作者：Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li
- 出版日期：2026-09-30T19:19:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.00618

### 一句话总结
论文提出用有限窗 DFT 的精确 Dirichlet 核替代 3D Gaussian splatting 中的高斯足迹，以实现波相干成像逆问题的可微渲染，并配合专用求解器 DSFW 完成优化。

### 研究问题
波相干成像（如太赫兹层析、合成孔径声学、毫米波雷达）通过傅里叶处理有限长信号成像，其点扩散函数是 Dirichlet 核（复值、振荡、周期），而不是高斯。论文指出，将 3D Gaussian splatting 直接移植到相干感知中会因构造而失败：高斯 splat 丢弃了旁瓣能量（占总能量的 10-20%）以及控制反射体之间相干干涉的相位。

### 核心思路/方法
核心思想是用有限窗 DFT 的物理精确 Dirichlet 核替换可学习的高斯足迹，并由携带面积、法线和材质信息的 surfel 进行调制，使渲染基元匹配测量物理而非近似它。优化方面提出专用求解器 Dirichlet Sliding Frank-Wolfe（DSFW），结合变量投影、残差对偶证书、由证书驱动的低效用 surfel 硬替换，以及周期性低分辨率耦合 Levenberg-Marquardt 校正，以应对破坏通用一阶优化器的崎岖损失景观。Dirichlet 核具有 O(1) 闭式求值，使前向模型在保持端到端可微的同时，与 FFT 真值匹配到机器精度。

### 主要贡献
- 指出将 3D Gaussian splatting 移植到相干感知中因丢弃旁瓣能量和相位而失败。
- 提出以有限窗 DFT 的精确 Dirichlet 核作为渲染基元，并由 surfel 调制，使渲染匹配测量物理。
- 提出专用求解器 DSFW，结合变量投影、残差对偶证书、证书驱动的硬替换和周期性低分辨率耦合 Levenberg-Marquardt 校正。
- Dirichlet 核支持 O(1) 闭式求值，前向模型与 FFT 真值匹配到机器精度且端到端可微。
- 在密集太赫兹重建中，以 0.018 bin RMSE 恢复反射体中心，比波形级自动微分快 10-50 倍，而 Gaussian splats 失败。

### 局限性
摘要未提供足够信息（未给出方法的适用边界、失败情形、计算开销上限、对其他波段的泛化实验或消融细节）。

### 阅读优先级
高。理由：论文针对波相干成像逆问题提出与测量物理精确匹配的可微渲染基元及专用求解器，并在太赫兹重建上给出定量结果与速度对比，对神经场景表示与渲染、可微逆问题方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Wave-based coherent imaging, including terahertz tomography, synthetic-aperture acoustics, and millimeter-wave radar, forms images by Fourier-processing finite-length signals, with an exact point spread function that is not Gaussian but a Dirichlet kernel: complex-valued, oscillatory, and periodic. However, transplanting 3D Gaussian splatting to coherent sensing fails by construction; Gaussian splats discard the sidelobe energy (10-20% of the total) and the phase that governs coherent interference between reflectors. Our key idea is to replace the learned Gaussian footprint with the physically exact Dirichlet kernel of the finite-window DFT, modulated by a surfel that carries area, normal, and material, so that the rendering primitive matches the measurement physics instead of approximating it. We pair this primitive with a specialized solver, Dirichlet Sliding Frank-Wolfe (DSFW), that combines variable projection, residual dual certificates, and certificate-driven hard replacement of low-utility surfels, with periodic low-resolution coupled Levenberg-Marquardt correction, navigating the rugged loss landscape that breaks generic first-order optimizers. The Dirichlet kernel admits an O(1) closed-form evaluation, so the forward model matches FFT ground truth to machine precision while remaining differentiable end-to-end. On dense terahertz reconstruction, our method recovers reflector centers to 0.018 bin RMSE, 10-50x faster than waveform-level automatic differentiation, where Gaussian splats fail.

</details>

#### 2026-09-30 - DyRAD: Radar Novel View Synthesis for Dynamic Driving Scenes

**Authors:** Merav Keidar, Tomer Borreda, Rajalakshmi Nandakumar, Or Litany
**Links:** [abs](https://arxiv.org/abs/2609.39841) - [pdf](https://arxiv.org/pdf/2609.39841)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, novel view synthesis, view synthesis, scene representation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DyRAD: Radar Novel View Synthesis for Dynamic Driving Scenes
- 作者：Merav Keidar, Tomer Borreda, Rajalakshmi Nandakumar, Or Litany
- 出版日期：2026-09-30T14:35:37Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.39841) / [PDF](https://arxiv.org/pdf/2609.39841)

### 一句话总结
DyRAD 通过将静态背景反射体与运动追踪的动态点反射体分离建模，并借助固定解析点扩散函数渲染完整的距离-方位-多普勒张量，从而实现动态驾驶场景下的雷达新视角合成。

### 研究问题
论文关注的是：如何从已记录的传感器数据中重建动态驾驶场景，并合成原始轨迹之外的观测，以支持自动驾驶系统的闭环评估。摘要指出，现有雷达新视角合成方法存在两方面不足：一是处理动态场景的方法仅重建距离-方位张量，未能利用雷达通过多普勒直接测量径向速度的能力；二是渲染多普勒的方法假设场景是静态的。此外，由于雷达处理会将每个反射扩散到多个 bin 中，现有表示会把这种扩散吸收进场景几何，导致视点移动时渲染不正确。

### 核心思路/方法
DyRAD 使用静态背景反射体和运动追踪的动态点反射体来建模动态驾驶场景，并渲染完整的距离-方位-多普勒张量。反射体速度由目标轨迹推导，并投影到视线方向上，使多普勒既作为渲染输出，也作为这些轨迹的监督信号。关键设计是：通过一个由雷达信号处理链推导出的固定解析点扩散函数来渲染反射体，避免传感器引起的扩散被固化到场景表示中。摘要还指出，这种分离还支持零样本传感器配置迁移，使同一重建场景无需重新拟合即可在不同雷达规格下渲染。

### 主要贡献
- 提出 DyRAD，用静态背景反射体与运动追踪的动态点反射体建模动态驾驶场景，并渲染完整的距离-方位-多普勒张量。
- 将反射体速度从目标轨迹推导并投影到视线方向，使多普勒同时作为渲染输出和轨迹监督。
- 使用源自雷达信号处理链的固定解析点扩散函数渲染反射体，避免把传感器扩散烘焙进场景表示。
- 实现零样本传感器配置迁移，使同一重建场景可渲染到不同雷达规格下。
- 在 RADIal、Boreas 和一个合成基准上评估，覆盖原始路径位姿以及此前工作未测试的偏移视点；在 RADIal 上，DyRAD 在 90.7% 的参考检测目标中恢复了雷达检测，而最强基线为 26.9%。

### 局限性
摘要未提供足够信息说明计算开销、实时性、对目标跟踪质量的依赖程度、失败案例，以及在真实世界复杂场景中的泛化边界。摘要未提供足够信息说明各数据集上的完整定量结果、消融实验细节和传感器配置迁移的具体评测设置。

### 阅读优先级
高。理由：该论文针对雷达新视角合成中动态场景与多普勒利用不足的核心矛盾，提出明确的分解建模与解析点扩散函数方案，并报告了相对最强基线的显著提升；同时涉及零样本传感器配置迁移这一对自动驾驶仿真与闭环评估有潜在价值的能力。摘要信息密度高，问题定位清晰，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic driving scenes from recorded sensor data supports closed-loop evaluation of autonomous driving systems by synthesizing observations beyond the original trajectory. Unlike cameras and LiDAR, radar measures radial velocity directly through Doppler. Yet existing radar novel-view synthesis fails to exploit this capability: methods addressing dynamic scenes reconstruct only range-azimuth tensors, while methods that render Doppler assume static scenes. Moreover, because radar processing spreads each reflection across multiple bins, existing representations absorb this spread into scene geometry, causing it to render incorrectly when the viewpoint moves. We present DyRAD, which models dynamic driving scenes using static background reflectors and motion-tracked dynamic point reflectors to render complete range-azimuth-Doppler (RAD) tensors. Reflector velocities are derived from object tracks and projected onto the line of sight, making Doppler both a rendered output and supervision for those tracks. Crucially, we render reflectors through a fixed analytic point-spread function (PSF) derived from the radar's signal-processing chain, preventing sensor-induced spread from being baked into the scene representation. Beyond improving scene reconstruction, this separation also enables zero-shot sensor-configuration transfer, allowing the same reconstructed scene to be rendered under different radar specifications without refitting. We evaluate DyRAD on RADIal, Boreas, and a synthetic benchmark across both on-path poses and displaced viewpoints untested by prior work. On RADIal, DyRAD recovers radar detections in 90.7% of reference-detected objects, compared with 26.9% for the strongest baseline.

</details>

#### 2026-09-30 - EffGS: Efficient and High-Fidelity Gaussian Splatting

**Authors:** Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan
**Links:** [abs](https://arxiv.org/abs/2609.39553) - [pdf](https://arxiv.org/pdf/2609.39553)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EffGS: Efficient and High-Fidelity Gaussian Splatting
- 作者：Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan
- 出版日期：2026-09-30T11:52:18Z
- 分类：Neural Scene Representations & Rendering（主分类）；次级分类摘要未提供
- 链接：[摘要](https://arxiv.org/abs/2609.39553) | [PDF](https://arxiv.org/pdf/2609.39553)

### 一句话总结
EffGS 提出一种面向有界与大规模场景的通用 3D Gaussian Splatting 加速框架，通过频率感知引导、局部化密度控制和自适应基元尺度调制，在保持甚至提升重建质量的同时改善训练与渲染效率。

### 研究问题
3D Gaussian Splatting（3DGS）虽能实现实时新视角合成，但现有通用加速方法在扩展到更复杂、大规模场景时会出现严重的渲染质量下降。论文旨在解决这一问题：在复杂大规模场景中同时提升训练与渲染效率，并保持与原始 3DGS 相当或更好的重建质量。

### 核心思路/方法
EffGS 结合了三个组件：
1. **频率感知引导**：重要性评分机制将逐像素重建误差与随训练调度的 Difference-of-Gaussians（高斯差分）掩码结合，提供阶段依赖的空间引导。
2. **局部化密度控制**：将稠密化与剪枝限制在采样视图中具有有效投影覆盖范围的 Gaussian 上。
3. **自适应基元尺度调制**：可学习的逐 Gaussian 尺度调制在优化过程中调整有效基元范围，同时保留 Compact Box 光栅化规则。

### 主要贡献
- 提出 EffGS，一个更通用的加速框架，在有界和大规模场景中提升训练与渲染效率，并保持与原始 3DGS 相当或更好的重建质量。
- 设计重要性评分机制，融合逐像素重建误差与训练调度的 DoG 掩码，实现阶段依赖的空间引导。
- 提出局部化稠密化与剪枝策略，将密度修改限制于在采样视图中具有有效投影覆盖范围的 Gaussian。
- 引入可学习的逐 Gaussian 尺度调制，在保留 Compact Box 光栅化规则的前提下调整有效基元范围。
- 在有界与大规模场景数据集上进行了实验，并开展组件消融与匹配基元预算对比，支持框架有效性（具体数值结果摘要未提供足够信息）。

### 局限性
摘要未提供足够信息。摘要仅说明实验覆盖有界与大规模场景数据集，并提及组件消融与匹配基元预算对比，但未给出具体失败案例、适用边界、计算开销细节或未覆盖的场景类型。论文本身可能存在的局限需查阅全文，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对 3DGS 在大规模复杂场景中加速时质量下降的关键问题，提出包含三个明确技术组件的通用框架，且摘要声称在重建质量、训练时间与基元数量之间取得良好平衡，并辅以消融与匹配基元预算对比；对关注 3DGS 加速、大规模场景重建与实时渲染的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables real-time novel view synthesis, but existing general-purpose acceleration methods suffer severe rendering quality degradation when extended to more complex, large-scale scenes. To address this issue, we propose EffGS, a more general acceleration framework that improves training and rendering efficiency while maintaining reconstruction quality comparable to or better than vanilla 3DGS across bounded and large-scale scenes. EffGS combines frequency-aware guidance, localized density control, and adaptive primitive scale modulation. First, an importance scoring mechanism combines pixel-wise reconstruction errors with a difference-of-Gaussians mask scheduled over training to provide stage-dependent spatial guidance. Second, localized densification and pruning restricts density modifications to Gaussians with valid projected footprints in the sampled views. Third, learnable per-Gaussian scale modulation adjusts effective primitive extent during optimization while retaining the Compact Box rasterization rule. Extensive experiments on bounded and large-scale scene datasets demonstrate a favorable balance between reconstruction quality, training time, and primitive count. Component ablations and matched-primitive-budget comparisons further support the effectiveness of the framework.

</details>

#### 2026-09-30 - Lens Flare Removal and Reconstruction

**Authors:** Tarun Yenamandra, Jonathon Luiten, Daniel Cremers, Nathan Matsuda
**Links:** [abs](https://arxiv.org/abs/2609.39527) - [pdf](https://arxiv.org/pdf/2609.39527)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3DGS, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lens Flare Removal and Reconstruction
- 作者：Tarun Yenamandra, Jonathon Luiten, Daniel Cremers, Nathan Matsuda
- 出版日期：2026-09-30T11:27:28Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.39527；PDF https://arxiv.org/pdf/2609.39527

### 一句话总结
论文同时研究大范围镜头光晕的去除与可重建表示：一方面构建新数据集并微调扩散模型去除大幅光晕，另一方面提出利用光晕关于相机主点对称性的表示模型，并与 3D 高斯泼溅联合优化，实现光晕与场景的分解、编辑与跨视图迁移。

### 研究问题
摘要指出，图像中的镜头光晕会显著降低 3D 场景重建等下游任务的结果质量，因为光晕属于相机成像系统的属性，而非被建模场景本身的一部分。已有方法主要处理围绕光源的小型光晕，对填满整幅图像的大范围光晕仍存在困难。此外，光晕在媒体中仍是常用的艺术工具，但如何在多视图间一致地表示与重建镜头光晕尚未被探索。

### 核心思路/方法
- 面向大范围光晕去除：构建一个结合公开真实数据与程序化生成流程的新数据集，并在该数据集上微调基于扩散的模型，用于去除复杂、大范围的镜头光晕。
- 面向光晕重建与分解：提出一种光晕表示模型，利用镜头光晕关于相机主点的对称性；提出计算流程，将该光晕模型与高斯泼溅模型（3DGS）联合优化，从而借助前述光晕去除模型把 3D 场景分解为镜头光晕与场景本身。
- 由于重建的光晕是显式且可重新渲染的，因此可被编辑，并迁移到新图像和新 3D 场景中。

### 主要贡献
- 编译了用于大范围光晕去除的新数据集，结合公开真实世界数据与程序化生成流程。
- 在大范围光晕去除任务上微调扩散模型。
- 提出利用光晕关于相机主点对称性的光晕表示模型。
- 提出联合优化光晕模型与 3DGS 的计算流程，实现 3D 场景中光晕与场景的分解。
- 使重建光晕具备显式、可重渲染、可编辑、可迁移到新图像与新 3D 场景的特性。
- 评估方面：在既有基准和面向大型反射光晕的新基准上评估去除效果，直接量化光晕/场景分解，并展示该流程对自动光源定位误差具有鲁棒性。

### 局限性
摘要未提供足够信息。摘要未说明方法的具体失败情形、计算开销、数据集规模与覆盖范围、对非对称或非典型光晕的适用性，也未提供与更多基线方法的完整比较细节。

### 阅读优先级
中。理由：该工作同时涉及光晕去除与神经场景表示/渲染中的光晕重建与分解，并引入新数据集、扩散模型微调、光晕表示与 3DGS 联合优化，主题较有新意且与 3D 场景重建下游任务相关；但摘要未提供充分实验细节与定量结果，若关注具体性能、可复现性或方法对比，需要进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

The presence of lens flares in images can significantly reduce the quality of downstream application results for tasks such as 3D scene reconstruction. This is because lens flares are a property of the camera imaging system, and not a part of the underlying scene being modeled. There are previous methods that tackle the removal of small flares focused around a light source. However, existing methods struggle with large flares, such as those that fill the entire image. In this work, we compile a novel dataset for large-flare removal, combining publicly available real-world data with a procedural generation pipeline. We fine-tune a diffusion-based model on our dataset to remove complex, large lens flares. On the other hand, lens flares remain effective artistic tools, widely used in the media. While there are ways to simulate 2D flares, representing and reconstructing lens flares consistently across multiple views has not yet been explored. To achieve this, we introduce a flare representation model that leverages the symmetry of lens flares about the camera's principal point. We propose a computational pipeline to jointly optimize this flare model and a Gaussian splatting model (3DGS). This enables the decomposition of a 3D scene into lens flares and the scene itself, using our flare-removal model. Because the reconstructed flare is explicit and re-renderable, it can be edited and transferred to novel images and new 3D scenes. We evaluate removal on an established benchmark and a new one for large reflective flares, quantify the flare/scene decomposition directly, and show that the pipeline is robust to errors in automatic light-source localization.

</details>

#### 2026-09-30 - UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting

**Authors:** Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han
**Links:** [abs](https://arxiv.org/abs/2609.39089) - [pdf](https://arxiv.org/pdf/2609.39089)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting
- 作者：Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han
- 出版日期：2026-09-30T06:27:05Z
- 分类：主分类为 Neural Scene Representations & Rendering；无次级分类
- 链接：摘要页 https://arxiv.org/abs/2609.39089 ；PDF https://arxiv.org/pdf/2609.39089

### 一句话总结
UGOD 为稀疏视角 3D Gaussian Splatting 引入视图相关的不确定性估计，并用该不确定性在渲染时调节高斯不透明度、在训练时执行软 dropout，以抑制不可靠高斯的错误贡献。

### 研究问题
稀疏视角下，有限的观测使许多高斯基元约束不足，但它们在 alpha 混合中仍会被累积贡献，导致过拟合；由于缺乏不确定性估计，渲染器无法区分不可靠基元与约束良好的基元，错误贡献会污染新视角合成结果。

### 核心思路/方法
- 为每个高斯估计一个视图相关的不确定性分数。
- 使用一个轻量不确定性头，以高斯属性和视角方向为条件预测该分数。
- 该分数驱动可微分的不透明度调制机制，在合成前衰减高不确定性基元。
- 训练时引入分离的软 dropout 分支，应用由不确定性控制的连续保留掩码，减少模型对约束较差高斯的依赖，从而缓解过拟合。
- 关键设计是分离不确定性分数，防止该随机正则化器的梯度偏置或破坏不确定性预测。

### 主要贡献
- 提出 UGOD，一个不确定性引导的稀疏视角 3D Gaussian Splatting 框架。
- 设计视图相关的不确定性估计，并用于渲染时的不透明度调制。
- 设计基于不确定性的分离软 dropout 训练正则化机制。
- 在 Mip-NeRF 360 和 LLFF 上，摘要称 UGOD 改善了稀疏视角新视角合成，并产生比对比方法更紧凑的高斯表示。

### 局限性
摘要未提供足够信息。摘要未说明具体实验设置、对比方法细节、失败场景、计算开销、超参数敏感性或与其他不确定性建模方法的系统比较。

### 阅读优先级
中。理由：该工作针对稀疏视角 3D Gaussian Splatting 的过拟合与不可靠基元贡献问题，提出不确定性引导的渲染与正则化机制，问题明确且方法路径较清晰；但摘要仅给出总体结论，未提供充分实验细节与局限性信息。若关注稀疏视角重建、高斯泼溅或不确定性建模，可优先阅读。

</details>

<details>
<summary>Abstract</summary>

Sparse-view 3D Gaussian Splatting is prone to overfitting because limited observations leave many Gaussian primitives weakly constrained, yet their contributions are still accumulated through alpha blending. Without uncertainty estimation, the renderer cannot distinguish unreliable primitives from well-constrained ones, allowing their erroneous contributions to corrupt novel-view synthesis. We introduce UGOD, an uncertainty-guided framework that estimates a view-dependent uncertainty score for each Gaussian and uses it to regulate its rendering contribution. A lightweight uncertainty head conditioned on Gaussian attributes and viewing direction predicts this score, which then drives a differentiable opacity-modulation mechanism that attenuates high-uncertainty primitives before compositing. During training, a detached soft-dropout branch applies an uncertainty-controlled continuous keep mask to discourage the model from relying on poorly constrained Gaussians and thereby reduce overfitting. Crucially, detaching the uncertainty score prevents gradients from this stochastic regulariser from biasing or collapsing the uncertainty prediction. Experiments on Mip-NeRF~360 and LLFF show that UGOD improves sparse-view novel-view synthesis while producing more compact Gaussian representations than the compared methods. These results demonstrate that Gaussian uncertainty provides an effective rendering-time control for sparse-view reconstruction.

</details>

#### 2026-09-29 - TSGL: Teacher-Student Graph Learning for 3DGS Compression

**Authors:** Matin Bani Saedi, Matthew Kyan, Gene Cheung
**Links:** [abs](https://arxiv.org/abs/2609.38635) - [pdf](https://arxiv.org/pdf/2609.38635)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TSGL: Teacher-Student Graph Learning for 3DGS Compression
- 作者：Matin Bani Saedi, Matthew Kyan, Gene Cheung
- 出版日期：2026-09-29T22:52:06Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要 https://arxiv.org/abs/2609.38635 ；PDF https://arxiv.org/pdf/2609.38635

### 一句话总结
提出 TSGL，一种基于教师—学生图学习的 3DGS 压缩方法，可在已训练模型上直接压缩，无需重训练或访问训练图像，实现 27x–33x 压缩且 PSNR 损失小于 0.6 dB。

### 研究问题
3D Gaussian Splatting（3DGS）包含数以百万计的高斯基元，每个基元带有丰富属性，导致文件体积庞大。论文关注的问题是如何在不对 3DGS 进行重训练、且无法访问训练图像的前提下，实现高压缩率并尽量保持渲染质量。

### 核心思路/方法
- 面向每个高斯基元块，使用解码后的位置和 DC 球谐（SH）系数作为预测因子。
- 通过教师—学生模型学习一个信号相关的几何图 G，用于编码相邻高斯之间的成对相似性。
- 在得到图 G 后，对剩余属性执行图傅里叶变换（GFT），使信号能量主要投影到低频系数，从而获得紧凑表示。
- 方法直接作用于已训练模型，不需要 3DGS 重训练，也不需要访问训练图像。

### 主要贡献
- 提出 TSGL，一种结合教师—学生图学习的 3DGS 压缩方法。
- 在无需重训练和无需训练图像的后训练压缩设定下，利用位置与 DC SH 系数学习几何图，并通过 GFT 压缩其余属性。
- 在三个标准基准上达到 27x 至 33x 压缩，PSNR 损失小于 0.6 dB，并在压缩体积和渲染质量上优于近期后训练压缩方法。

### 局限性
- 摘要未提供足够信息说明具体数据集名称、实验设置细节、消融实验、计算开销、编码解码时间或对不同 3DGS 变体的泛化能力。
- 摘要未提供足够信息说明教师—学生模型的具体结构、训练目标、图构建的计算复杂度及超参数敏感性。
- 摘要未提供足够信息说明方法在极端压缩率或其他场景类型下的表现。

### 阅读优先级
高。理由：该论文针对 3DGS 文件体积大的核心问题，提出无需重训练和训练图像的后训练压缩方案，并在摘要中报告了较高压缩率与较小 PSNR 损失，且声称优于近期后训练压缩方法，对 3DGS 压缩与神经场景表示方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) is a popular representation for novel view synthesis. However, 3DGS contains millions of Gaussian primitives, each with rich attributes, resulting in large file sizes. We propose a novel 3DGS compression method based on Teacher-Student Graph Learning (TSGL) that operates directly on a trained model, without 3DGS retraining or access to training images. Specifically, for each block of Gaussian primitives, using decoded positions and DC spherical harmonic (SH) coefficients as predictors, we learn a signal-dependent geometry graph G encoding the pairwise similarities between neighbouring Gaussians via a teacher-student model. Given G, we perform Graph Fourier Transform (GFT) on the remaining attributes, so that signal energies are predominantly projected into the low-frequency coefficients for compact representation. On three standard benchmarks, the method reaches 27x to 33x compression with less than 0.6 dB of PSNR loss, improving on recent post-training compression methods in both size and rendering quality.

</details>

#### 2026-09-29 - StereoGaussians: Feed-Forward 3D Gaussian Splatting from Stereo Images

**Authors:** Boyuan Tian, Huangying Zhan, Zhan Li, Shin-Fang Chng, Hanwen Yang, Zirui Wang, Yi Xu
**Links:** [abs](https://arxiv.org/abs/2609.38592) - [pdf](https://arxiv.org/pdf/2609.38592)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** stereo depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：StereoGaussians: Feed-Forward 3D Gaussian Splatting from Stereo Images
- 作者：Boyuan Tian, Huangying Zhan, Zhan Li, Shin-Fang Chng, Hanwen Yang, Zirui Wang, Yi Xu
- 出版日期：2026-09-29T21:51:37Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.38592 ；PDF https://arxiv.org/pdf/2609.38592

### 一句话总结
StereoGaussians 从单个已标定的立体图像对出发，前馈预测度量尺度的 3D Gaussian Splatting 表示，并支持输入视角之外附近视角的外推渲染。

### 研究问题
前馈式 3D Gaussian Splatting 虽然无需逐场景优化即可完成重建，但在实际立体相机应用中，需要在输入视角之外进行附近视角的外推。摘要指出：立体深度只能锚定可见表面，而要渲染新暴露区域，还需要学习外观信息以及额外的场景容量。因此问题是如何在单对立体输入下，同时利用立体网络的几何锚定能力与额外容量，来生成可外推的度量 3DGS 表示。

### 核心思路/方法
摘要给出的方法要点包括：
- 从单个已标定的立体图像对预测度量 3DGS 表示。
- 复用冻结的预训练立体网络的中间表示来预测 Gaussian 属性。
- 使用已标定的视差（calibrated disparity）作为几何锚定。
- 引入第二层 Gaussian 层（second Gaussian layer）和扩展的图像画布（expanded image canvas），为去遮挡内容和视场外内容提供容量。
- 训练数据方面，从经过质量过滤的 3DGS teacher 构建 SceneSplat-Stereo，将立体输入与附近目标视角配对，覆盖 803 个训练场景。

### 主要贡献
- 提出 StereoGaussians，能够从单个已标定立体图像对前馈预测度量 3DGS 表示。
- 设计上复用冻结预训练立体网络的中间表示，并以标定视差锚定几何。
- 通过第二 Gaussian 层与扩展图像画布提升对去遮挡及视场外内容的建模容量。
- 构建 SceneSplat-Stereo 训练数据集，包含 803 个训练场景，配对立体输入与附近目标视角。
- 在未见过的真实与照片级真实感立体基准上，相较强视角合成基线取得提升；消融研究支持主要设计选择。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、计算开销、对立体标定误差的敏感度、泛化边界或消融实验的具体局限说明。

### 阅读优先级
中。理由：该工作针对前馈 3DGS 的立体输入与外推渲染问题，提出明确的技术组合（冻结立体网络特征、视差锚定、双层 Gaussian 与扩展画布）和大规模训练集构建；若关注前馈式 3DGS、立体视觉或新视角外推，值得阅读。但摘要未提供量化结果、与基线的具体差距、运行效率及失败案例，是否能支撑实际应用需阅读正文进一步判断。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) enables reconstruction without per- scene optimisation, but practical stereo-camera applications require nearby-view extrapolation beyond the input views. Stereo depth anchors visible surfaces, yet rendering newly exposed regions also requires learned appearance and additional scene capacity. We introduce StereoGaussians, which predicts a metric 3DGS representation from a single calibrated stereo pair. It reuses intermediate repre- sentations from frozen pretrained stereo networks to predict Gaussian attributes, while calibrated disparity anchors the geometry. A second Gaussian layer and an expanded image canvas provide capacity for disoccluded and outside-field-of- view content. For training, we construct SceneSplat-Stereo from quality-filtered 3DGS teachers, pairing stereo inputs with nearby target views across 803 training scenes. Experiments on unseen real and photorealistic stereo benchmarks demon- strate improvements over strong view-synthesis baselines, while ablation studies support our main design choices.

</details>

#### 2026-09-29 - PneuTac: Tactile Manipulation with Soft Pneumatic Robots via Unified MPM-Gaussian Splatting Simulation

**Authors:** Shaohong Zhong, Marco Pontin, Joe Watson, Perla Maiolino, Ingmar Posner
**Links:** [abs](https://arxiv.org/abs/2609.38418) - [pdf](https://arxiv.org/pdf/2609.38418)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PneuTac: Tactile Manipulation with Soft Pneumatic Robots via Unified MPM-Gaussian Splatting Simulation
- 作者：Shaohong Zhong, Marco Pontin, Joe Watson, Perla Maiolino, Ingmar Posner
- 出版日期：2026-09-29T19:12:12Z
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（次）
- 链接：摘要页 https://arxiv.org/abs/2609.38418 ；PDF https://arxiv.org/pdf/2609.38418

### 一句话总结
PneuTac 提出一个统一框架，用物质点法（MPM）建模软气动机器人与可变形触觉膜动力学，用 3D 高斯泼溅（3DGS）渲染，并通过视觉式真实到仿真建模与代理模型训练，实现软体机器人触觉反馈操作。

### 研究问题
软体机器人和触觉传感器在精细操作中有潜力：软气动机器人依靠柔顺性实现安全接触，视觉式触觉传感器提供高分辨率触觉感知。但用柔顺机器人学习触觉操作面临瓶颈——缺乏高效仿真。现有仿真器通常将二者孤立建模，且存在较大标定差距，难以高效克服。

### 核心思路/方法
作者提出 PneuTac，一个面向软气动机器人触觉反馈操作的统一框架。方法要点包括：
- 使用物质点法（MPM）建模软体机器人动力学以及可变形触觉膜；
- 使用 3D 高斯泼溅（3DGS）进行渲染；
- 通过一种简单的基于视觉的方法完成真实到仿真（real-to-sim）建模；
- 随后训练动作网络与感知网络，以代理模型实现高效仿真；
- 用该框架驱动一条触觉引导流程，在仿真中收集示教数据。

### 主要贡献
摘要中明确给出的贡献包括：
- 提出 PneuTac 统一框架，将软气动机器人动力学、可变形触觉膜与渲染统一建模；
- 采用简单视觉式方法做真实到仿真建模，并训练动作与感知网络形成高效仿真代理模型；
- 利用该框架驱动触觉引导流程，在仿真中采集示教；
- 在定制气动软指（带触觉感知尖端）及额外跨设备评估上开展实验，表明 PneuTac 能较准确建模带触觉传感器的软体机器人；
- 在三个真实世界富接触柔顺操作任务上，用仿真增强示教训练的策略优于仅用相同真实数据训练的基线。

### 局限性
摘要未提供足够信息。摘要未给出失败案例、仿真与真实之间的残余差距量化、任务种类与规模上限、跨设备泛化边界、计算开销或实时性等具体局限。

### 阅读优先级
中。理由：该工作处于软体机器人、触觉操作与神经渲染/仿真的交叉点，且主分类为神经场景表示与渲染、次分类含具身/机器人应用，方法组合（MPM + 3DGS + real-to-sim + 代理模型）对相关方向有参考价值；但摘要未提供实验细节、量化指标与局限，若需判断其可复现性与实际性能，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Soft robots and tactile sensors have demonstrated great potential in delicate manipulation tasks. Soft pneumatic robots enable safe contact through compliance, and vision-based tactile sensors offer high-resolution touch perception. However, learning tactile manipulation with compliant robots has been challenging, bottlenecked by the lack of efficient simulation. Existing simulators typically model them in isolation, and exhibit large calibration gaps that are difficult to overcome efficiently. We present PneuTac, a unified framework for tactile-feedback manipulation with soft pneumatic robots. We leverage the material point method (MPM) for modelling the dynamics of the soft robot and the deformable tactile membrane, and 3D Gaussian splatting (3DGS) for rendering. Real-to-sim modelling is done with a simple vision-based method, to then train action and perception networks for efficient simulation with surrogate models. We use the framework to drive a tactile-guided pipeline to collect demonstrations in simulation. Through experiments on a custom-designed pneumatic soft finger with a tactile sensing tip, together with additional cross-device evaluations, we show that PneuTac is capable of accurately modelling soft robots with tactile sensors, and that policies trained with simulation-augmented demonstrations outperform baselines trained on the same real data on three real-world contact-rich compliant manipulation tasks, making it a practical framework for tactile manipulation on compliant hardware.

</details>

#### 2026-09-29 - Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering

**Authors:** Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, Wonjun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
**Links:** [abs](https://arxiv.org/abs/2609.38177) - [pdf](https://arxiv.org/pdf/2609.38177)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering
- 作者：Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, Wonjun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
- 出版日期：2026-09-29T17:59:52Z
- 分类：Neural Scene Representations & Rendering（主分类）；次要分类摘要未提供
- 链接：https://arxiv.org/abs/2609.38177 ；PDF：https://arxiv.org/pdf/2609.38177

### 一句话总结
受人类粗略构建 3D 场景布局的空间推理方式启发，论文提出 Imagine3D-LLM，让多模态大语言模型先“想象”出一个紧凑的 3D 高斯表示，再基于该表示作答，从而提升多视角图像上的空间推理与 3D 理解能力。

### 研究问题
从多视角图像推理 3D 世界对多模态大语言模型（MLLMs）仍是基础性挑战。现代 MLLMs 虽能有效处理单图输入，但难以跨视角整合证据形成连贯的 3D 理解。已有工作尝试通过增强细粒度像素级跨视角对应，或融合 3D 几何基础模型的特征来注入 3D 感知，但与人类推理之间仍存在显著差距。

### 核心思路/方法
论文重新审视人类空间推理：人类并不依赖细粒度几何线索，而是先跨视角粗略识别共同物体、推断视角之间的相对几何关系，再组装出场景的粗略 3D 布局。受此启发，Imagine3D-LLM 学习组装类似的紧凑 3D 表示，并以该表示为条件进行回答。具体做法是：在图像 token 之后追加一小组可学习的 summary token，将其解码为紧凑的 3D Gaussian Splatting 表示，并用光度重建损失进行监督，同时与标准的下一 token 预测目标联合训练。值得注意的是，虽然只有 summary token 接受直接重建监督，但该目标也在 LLM 底层图像特征中诱导出更强的跨帧对应，表明学习重建会把 3D 感知信号传播到整个模型。

### 主要贡献
- 提出 Imagine3D-LLM，一种先“想象”紧凑 3D 表示再作答的 MLLM 框架，其设计灵感来自人类空间推理过程。
- 通过在图像 token 后追加可学习 summary token，并将其解码为紧凑 3D Gaussian Splatting 表示，以光度重建损失与下一 token 预测目标联合训练。
- 发现仅对 summary token 施加直接重建监督，也能在 LLM 底层图像特征中诱导更强的跨帧对应，说明重建学习可将 3D 感知信号传播至整个模型。
- 摘要称 Imagine3D-LLM 在多个空间推理与 3D 理解基准上持续优于先前方法，提示“想象场景”可能比被告知像素级几何更有效。

### 局限性
- 摘要未提供足够信息说明具体实验设置、基准名称、数据集规模与对比方法细节。
- 摘要未提供足够信息说明模型参数量、训练成本、推理开销或效率表现。
- 摘要未提供足够信息说明失败案例、对特定场景类型（如动态场景、大视角变化）的适用性限制。
- 摘要未提供足够信息说明 3D Gaussian Splatting 表示的紧凑程度、重建质量上限及其对下游任务的影响边界。

### 阅读优先级
高。理由：该工作针对 MLLMs 多视角 3D 理解这一基础挑战，提出与人类空间推理对齐的“先想象 3D 表示再作答”范式，方法上与 3D Gaussian Splatting、可学习 summary token 和联合训练目标结合，且摘要声称在多个基准上持续超越先前方法，并观察到重建监督可反向增强底层图像特征的跨帧对应，具有较强的方法启发性和潜在影响力。

</details>

<details>
<summary>Abstract</summary>

Reasoning about the 3D world from multi-view images remains a fundamental challenge for Multimodal Large Language Models (MLLMs). While modern MLLMs handle single-image inputs effectively, they struggle to integrate evidence across viewpoints into a coherent 3D understanding. A growing body of work attempts to close this gap by injecting 3D awareness into MLLMs, either by boosting fine-grained pixel-level cross-view correspondence or by fusing features from 3D geometry foundation models, yet a substantial gap to human reasoning persists. In this work, we revisit human spatial reasoning, which suggests that rather than relying on fine-grained geometry cues, humans roughly identify common objects across views, infer the relative geometry between viewpoints, and assemble a coarse 3D layout of the scene. Inspired by this process, we introduce Imagine3D-LLM, an MLLM that learns to assemble a similar compact 3D representation of the scene and conditions its answer on this representation. Concretely, we append a small set of learnable summary tokens after the image tokens, decode them into a compact 3D Gaussian Splatting representation supervised by a photometric reconstruction loss, and train jointly with the standard next-token prediction objective. Notably, although only the summary tokens receive direct reconstruction supervision, this objective also induces stronger cross-frame correspondence within the LLM's underlying image features, suggesting that learning to reconstruct propagates 3D-aware signals throughout the model. As a result, Imagine3D-LLM consistently outperforms prior approaches across multiple spatial reasoning and 3D understanding benchmarks, suggesting that imagining the scene can be more effective than being told its pixel-wise geometry.

</details>

#### 2026-09-29 - EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior

**Authors:** Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari
**Links:** [abs](https://arxiv.org/abs/2609.37874) - [pdf](https://arxiv.org/pdf/2609.37874)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior
- 作者：Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari
- 出版日期：2026-09-29T15:49:22Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.37874

### 一句话总结
EndoPrior-GS 通过从帧中提取的视觉启发式信息与估计深度图构建联合纹理先验，用于改进动态内窥镜场景下 3D 高斯泼溅的几何初始化与训练过程。

### 研究问题
动态内窥镜重建是机器人手术和计算机辅助干预的基础，但 3D 高斯泼溅（3DGS）在可变形术中环境中的应用受到虚假几何和光照变化的限制。论文旨在解决 3DGS 在内窥镜动态重建中因这些因素导致的性能约束。

### 核心思路/方法
方法提出一种新流程，显式耦合从帧中提取的视觉启发式信息与估计深度图。具体地，从工具过滤后的有效组织掩码、非镜面反射的光度过滤器以及解剖结构显著性中导出联合纹理先验，形成概率图，用于指导基元初始化及后续密度控制。该先验进一步通过一个纹理感知项扩展到时间域，在训练中动态加权成对基元的贡献。

### 主要贡献
- 提出 EndoPrior-GS 流程，显式耦合帧提取的视觉启发式与估计深度图。
- 构建联合纹理先验，来源包括工具过滤的有效组织掩码、非镜面光度过滤和解剖结构显著性，并用于指导基元初始化与密度控制。
- 将先验扩展到时间域，通过纹理感知项动态加权训练中的成对基元贡献。
- 在 EndoNeRF 和 SCARED 基准数据集上进行实验，结果显示 Flow Error 相比代表性方法分别降低 27.7% 和 25.8%，同时保持有竞争力的渲染质量和实时渲染速度。

### 局限性
摘要未提供足够信息。（摘要未说明方法的失效场景、对特定数据或硬件条件的依赖、先验提取的误差影响、计算开销细节或泛化性限制。）

### 阅读优先级
中。理由：论文针对动态内窥镜重建中 3DGS 的几何与光照问题提出明确的先验引导方案，并在两个基准数据集上报告了 Flow Error 的显著降低，同时声称保持实时速度，对相关方向有参考价值；但摘要未提供方法细节、消融实验或局限性的充分信息，是否具有广泛适用性需进一步阅读正文确认。

</details>

<details>
<summary>Abstract</summary>

Dynamic endoscopic reconstruction is fundamental to robotic surgery and computer-assisted interventions. While 3D Gaussian Splatting (3DGS) realises real-time rendering, its application to deformable intraoperative environments remains constrained by spurious geometry and varying illuminations. To address these limitations, we introduce EndoPrior-GS, a novel pipeline that explicitly couples frame-extracted vision heuristics and estimated depth maps. EndoPrior-GS derives a joint texture prior from a tool-filtered valid tissue mask, a non-specular photometric filter, and anatomical structural salience, yielding a probability map that guides primitive initialisation and subsequent density control. The prior is further extended to the temporal domain through a texture-aware term that dynamically weighs pairwise primitive contributions during training. We conduct extensive experiments on benchmark datasets EndoNeRF and SCARED, and the obtained results show that our method EndoPrior-GS reduces Flow Error by 27.7% and 25.8% over the representative approaches while preserving competitive rendering quality and real-time rendering speed. Our project website is available at https://jiaqi-huang-77.github.io/EndoPrior-GS/.

</details>

#### 2026-09-29 - WINGS: Reference-Free Gaussian Splatting Inpainting with 3D-Native Generative Priors

**Authors:** Noé Lallouet, Michael Fischer, Elie Michel
**Links:** [abs](https://arxiv.org/abs/2609.37816) - [pdf](https://arxiv.org/pdf/2609.37816)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WINGS: Reference-Free Gaussian Splatting Inpainting with 3D-Native Generative Priors
- 作者：Noé Lallouet, Michael Fischer, Elie Michel
- 出版日期：2026-09-29T15:27:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.37816) / [PDF](https://arxiv.org/pdf/2609.37816)

### 一句话总结
提出一种无需参考视图、直接在 3D 原生生成先验表示空间中完成 3D Gaussian Splatting 场景修复的方法，以避免多视图不一致问题并加快速度。

### 研究问题
3D Gaussian Splatting 场景的修复（inpainting）是 3D 编辑中的关键挑战，需要在 3D 空间的掩码区域内生成合理内容。已有方法依赖 2D 扩散模型生成一个或多个修复后的参考视图，因此易受多视图不一致和优化时间过长问题的影响。

### 核心思路/方法
论文提出一种无参考（reference-free）的 Gaussian Splatting 修复方法，完全在 3D 中操作。方法利用大型预训练 3D 先验的嵌入空间，并结合一个结构补全网络，将信息输入生成先验，以重建缺失区域的几何与外观。由于内容生成完全在 3D 中进行，方法避免了协调多张修复参考图像之间不一致性的需要，并且比相关基于 2D 的方法更快。

### 主要贡献
- 提出一种无参考的 Gaussian Splatting 修复方法，原生地在 3D 中操作。
- 利用预训练大型 3D 先验的嵌入空间，并结合结构补全网络与生成先验重建缺失区域的几何和外观。
- 避免多视图不一致问题，并相比相关 2D 方法更快。
- 通过大量实验和用户研究，在定性与定量上展示了方法有效性。
- 据作者所知，这是首个在学习到的 3D 原生生成先验表示空间中运行、且不依赖修复参考视图的 Gaussian Splatting 修复方法。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、适用场景限制、计算资源需求或与基线方法的详细对比限制。

### 阅读优先级
高。理由：该工作针对 3D Gaussian Splatting 修复中的多视图不一致与优化耗时问题，提出 3D 原生、无参考的方法，并声称是首个在学习到的 3D 原生生成先验表示空间中运行的 Gaussian Splatting 修复方法，主题与神经场景表示和渲染方向高度相关。

</details>

<details>
<summary>Abstract</summary>

Inpainting 3D Gaussian Splatting scenes, a key challenge in 3D editing, requires generating plausible content within a masked region of 3D space. Prior approaches rely on 2D diffusion models to produce one or several inpainted reference views, making them susceptible to challenges associated with multi-view inconsistency and lengthy optimization times. Departing from these approaches, we introduce a reference-free Gaussian splatting inpainting method operating natively in 3D. Our method leverages the embedding space of a large, pre-trained 3D prior, combined with a structure completion network to feed a generative prior which reconstructs the missing region's geometry and appearance. Performing content generation entirely in 3D, it avoids the need to reconcile inconsistencies of multiple inpainted reference images, and is faster than related 2D-based methods. We demonstrate the effectiveness of our method qualitatively and quantitatively, through extensive experiments and a user study. To the best of our knowledge, this work is the first Gaussian splatting inpainting method to operate in the learned representation space of a 3D-native generative prior without relying on inpainted reference views.

</details>

#### 2026-09-29 - NRF-GS: Neural Residual Fields for Expressive and Compact Gaussian Splatting

**Authors:** Pratik Singh Bisht, Andreas Kolb
**Links:** [abs](https://arxiv.org/abs/2609.37115) - [pdf](https://arxiv.org/pdf/2609.37115)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NRF-GS: Neural Residual Fields for Expressive and Compact Gaussian Splatting
- 作者：Pratik Singh Bisht, Andreas Kolb
- 出版日期：2026-09-29T09:27:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.37115

### 一句话总结
论文提出 NRF-GS，用共享的全局神经残差场替代每个 splat 的球谐基，以增强视角相关反射的表达能力，从而在减少高斯数量最多 50% 的同时保持或提升渲染质量。

### 研究问题
作者重新审视 3D Gaussian Splatting（3DGS）中的外观建模，认为视角相关反射表达能力有限是表示冗余的关键驱动因素。标准 3DGS 使用低阶球谐（SH），限制了 splat 建模高频方向性效果的能力，通常需要通过增加 splat 数量来补偿。

### 核心思路/方法
NRF-GS 是一种混合表示：它用共享的神经残差场替代每个 splat 的 SH 基。每个高斯编码一组紧凑的外观特征和一个朗伯基础颜色；一个轻量的全局场景级 MLP 以视角方向、距离和每个 splat 的特征为条件，预测视角相关残差。该形式通过结合每个 splat 的漫反射表示与共享的全局高频细节函数，增强方向性反射建模，并实现跨 splat 的参数共享。其关键洞见是：准确捕捉高频方向性反射（尤其是镜面区域）后，GS 表示变得更具表达力，从而减少对几何冗余 splat 的需求。

### 主要贡献
- 揭示 3DGS 中视角相关反射表达能力不足是表示冗余的关键原因。
- 提出 NRF-GS，用共享的全局场景级 MLP 神经残差场替代每个 splat 的 SH 基，实现表达力与参数共享的提升。
- 在减少最多 50% 高斯数量的情况下，取得可比或更好的渲染质量，并明显改善镜面和高频细节。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对 3DGS 的外观建模与表示冗余提出明确改进，且声称可在减少高斯数量的同时保持或提升质量，对关注高效神经渲染与 3DGS 改进的研究者有参考价值；但摘要未提供实验设置、数据集、定量指标和局限讨论等细节，需进一步阅读全文才能判断其实际效果与适用范围。

</details>

<details>
<summary>Abstract</summary>

We revisit the role of appearance modeling in 3D Gaussian Splatting (3DGS) and show that limited expressiveness in view-dependent reflectance is a key driver of representation redundancy. In standard 3DGS, low-order spherical harmonics (SH) are used, restricting the splats' ability to model high-frequency directional effects, which is typically compensated by increasing the number of splats. We propose \emph{NRF-GS: Neural Residual Fields for Gaussian Splatting}, a hybrid representation that replaces per-splat SH-bases with a shared neural residual field. Each Gaussian encodes a compact set of appearance features and a lambertian base color, while a lightweight \emph{global scene-level MLP} predicts view-dependent residuals conditioned on viewing direction, distance, and per-splat features. This formulation enhances directional reflectance modeling by combining diffuse per-splat reflectance representations with a shared global function for high-frequency details, enabling both higher expressiveness and parameter sharing across splats. Our key insight is that by accurately capturing high-frequency directional reflectance, especially in specular regions, the GS-representation becomes more expressive, reducing the need for geometrically redundant splats. As a result, NRF-GS achieves comparable or better rendering quality while reducing the number of Gaussians by up to 50\%, and produces visibly improved specular and high-frequency details.

</details>

#### 2026-09-29 - DRHeC: Differentiable Rendering for Hand-Eye Calibration with RGB-Based Gradients

**Authors:** Xiaotian Zhang, Yusheng Wang, Naoya Kagawa, Noritaka Takamura, Keiji Okuhara, Hiroyasu Baba, Jun Ota
**Links:** [abs](https://arxiv.org/abs/2609.36779) - [pdf](https://arxiv.org/pdf/2609.36779)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** differentiable rendering, rendering, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DRHeC: Differentiable Rendering for Hand-Eye Calibration with RGB-Based Gradients
- 作者：Xiaotian Zhang, Yusheng Wang, Naoya Kagawa, Noritaka Takamura, Keiji Okuhara, Hiroyasu Baba, Jun Ota
- 出版日期：2026-09-29T05:50:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.36779) / [PDF](https://arxiv.org/pdf/2609.36779)

### 一句话总结
本文提出一种基于 RGB 的可微渲染手眼标定框架 DRHeC，通过引入颜色与掩码几何特征提升标定精度与优化稳定性，并配合掩码引导的图像到图像翻译方法保持颜色与几何一致性。

### 研究问题
手眼标定对精密操作至关重要。传统方法依赖标记物，精度受标记物精度与可观测性影响；无标记方法（如基于学习的方法）使用深度神经网络直接从图像提取关键点或特征，可单图计算手眼变换且无需物理标记。近期基于可微渲染的手眼标定方法利用物理模型渲染二值掩码并与观测比较，实现标定阶段无需基准标记且优化可解释。然而，现有可微渲染方法使用二值掩码会丢失内部轮廓细节，降低精度，并可能面临优化不稳定与局部极小值问题。

### 核心思路/方法
- 提出一种基于 RGB 的新型可微渲染框架，通过融合颜色与掩码几何特征，提供更丰富的几何与外观线索，从而提升标定精度与优化稳定性。
- 提出一种掩码引导的图像到图像翻译方法，确保翻译过程中显式保持颜色与几何一致性。
- 通过仿真与真实世界实验验证方法的精度与鲁棒性，并与现有可微渲染方法进行对比。

### 主要贡献
- 提出 RGB -based 可微渲染手眼标定框架，弥补二值掩码丢失内部轮廓细节的不足。
- 引入颜色与掩码几何特征以改善标定精度和优化稳定性。
- 提出掩码引导的图像到图像翻译方法以保持颜色与几何一致性。
- 在仿真和真实世界实验中验证方法的精度与鲁棒性，并报告相比现有可微渲染手眼标定方法 EasyHeC 的改进：在 UR5e 真实世界实验中抓取成功率达 88.9%，插入成功率达 57.4%，分别高出 46.3 和 48.1 个百分点。

### 局限性
摘要未提供足够信息。摘要未提及方法的具体失败场景、计算开销、对特定硬件或环境的依赖、超参数敏感性等潜在局限。

### 阅读优先级
高。理由：该论文针对手眼标定中可微渲染方法的已知问题（二值掩码信息丢失、优化不稳定与局部极小值）提出明确改进，并在真实机器人实验中报告了相对 SOTA 方法的大幅性能提升，对机器人操作、可微渲染与无标记标定方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate hand-eye calibration is crucial for precision manipulation. Traditional methods rely on markers, with their precision dependent on marker accuracy and observability. In contrast, markerless methods, such as learning-based approaches, use deep neural networks to directly extract keypoints or features from images, enabling the computation of hand-eye transformation with a single image and without the need for physical markers. Recently, differentiable rendering-based methods for hand-eye calibration have leveraged physical models to render binary masks and compare them with observations, enabling hand-eye calibration without fiducial markers in the calibration stage and providing interpretable optimization. While the state-of-the-art differentiable rendering methods achieve remarkable accuracy, the use of binary masks can result in the loss of internal profile details, reducing precision. Additionally, these methods can also suffer from unstable optimization and local minima. In this study, we propose a novel RGB-based differentiable rendering framework that provides richer geometric and appearance cues by incorporating color and mask geometric features, thereby improving calibration accuracy and optimization stability. Additionally, we propose a mask-guided image-to-image translation method to ensure explicit preservation of color and geometric consistency throughout the translation. Our approach is validated through both simulation and real-world experiments, with results demonstrating strong accuracy and robustness and clear improvements over existing differentiable rendering methods. Our method achieves a grasping success rate of 88.9% and insertion success rate of 57.4% on the UR5e real-world experiment, outperforming the state-of-the-art differentiable rendering hand-eye calibration method EasyHeC by 46.3 and 48.1 percentage points, respectively.

</details>

#### 2026-09-28 - GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space

**Authors:** Kerui Ren, Tao Lu, Linning Xu, Changjian Jiang, Mu Huang, Chunhua Shen, Mulin Yu, Bo Dai
**Links:** [abs](https://arxiv.org/abs/2609.35734) - [pdf](https://arxiv.org/pdf/2609.35734)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space
- 作者：Kerui Ren, Tao Lu, Linning Xu, Changjian Jiang, Mu Huang, Chunhua Shen, Mulin Yu, Bo Dai
- 出版日期：2026-09-28T17:51:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2609.35734) / [PDF](https://arxiv.org/pdf/2609.35734)

### 一句话总结
GeoVerse 在预训练 3D 基础模型的几何隐空间中融合视频生成模型的外观先验，并通过全局空间记忆实现跨视角一致的新视角合成。

### 研究问题
从稀疏图像进行新视角合成时，需要同时满足两个目标：对已观测区域进行忠实重建，以及对未见内容进行合理补全，并在不同视角之间保持世界一致性。摘要指出，现有基于几何的方法能保留已观测场景结构，但往往难以补全未见区域；视频生成模型虽提供丰富外观先验，但在顺序生成视角时会累积不一致性。

### 核心思路/方法
- 在预训练 3D 基础模型的几何隐空间中执行生成，而非直接在图像空间生成。
- 从 Wan2.2 VACE 提取多层级特征，并通过 ControlNet 风格的适配器注入几何隐扩散模型，以引入视频学习到的外观先验来增强结构补全。
- 引入全局空间记忆，持续聚合已观测与已合成内容，并将目标对齐的引导重新投影，使后续预测锚定到共享场景表示，从而增强跨视角一致性。

### 主要贡献
- 提出 GeoVerse 框架，将视频生成模型的外观先验注入几何隐空间扩散模型，以兼顾几何结构与未见区域补全。
- 设计 ControlNet 风格适配器，实现 Wan2.2 VACE 多层级特征向几何隐扩散模型的注入。
- 提出全局空间记忆机制，通过重投影目标对齐引导来维持跨视角的世界一致性。
- 摘要报告了在多个数据集上的实验：相比 GLD，在 DL3DV 上 PSNR 高 2.23 dB，在 Mip-NeRF360 上 ATE 低 32.4%。

### 局限性
- 摘要未提供足够信息说明方法的具体失败情形或适用边界。
- 摘要未提供足够信息说明对计算资源、训练数据规模或推理速度的要求。
- 摘要未提供足够信息说明全局空间记忆在长序列或大范围场景中的扩展性。
- 摘要未提供足够信息说明各数据集上除 PSNR 与 ATE 外的其他指标表现。

### 阅读优先级
高。理由：该论文聚焦稀疏视角新视角合成中的世界一致性与未见区域补全这一核心难题，方法上结合 3D 基础模型几何隐空间、视频生成先验与空间记忆机制，且摘要给出了相对基线 GLD 的明确量化提升，适合关注神经场景表示与渲染方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observed scene structure but often struggle to complete unseen regions, whereas video generative models offer rich appearance priors but accumulate inconsistencies during sequential view generation. We propose GeoVerse, a framework that synthesizes world-consistent novel views by performing generation within the geometric latent space of a pretrained 3D foundation model and injecting appearance priors from a video generative model. Specifically, GeoVerse extracts multilevel features from Wan2.2 VACE and injects them into the geometric latent diffusion model via a ControlNet-style adapter, incorporating video-learned appearance priors to enhance structural completion. To enforce cross-view coherence, a global spatial memory continuously aggregates observed and synthesized content, reprojecting target-aligned guidance to anchor subsequent predictions to a shared scene representation. Extensive experiments across diverse datasets demonstrate improved visual quality and geometric consistency, with a 2.23 dB higher PSNR on DL3DV and 32.4% lower ATE on Mip-NeRF360 compared to GLD.

</details>

#### 2026-09-28 - CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism

**Authors:** R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti
**Links:** [abs](https://arxiv.org/abs/2609.35619) - [pdf](https://arxiv.org/pdf/2609.35619)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism
- 作者：R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti
- 出版日期：2026-09-28T16:57:15Z
- 分类：Neural Scene Representations & Rendering（主分类）；副分类摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2609.35619) ｜ [PDF](https://arxiv.org/pdf/2609.35619)

### 一句话总结
论文提出 CollisionSplatting——一种直接作用于标准 3D Gaussian Splatting 场景、可调保守度的 GPU 加速概率式距离度量，用于将碰撞感知代价与图像条件奖励统一到运动规划中。

### 研究问题
将稠密视觉信息整合进运动规划仍然困难：几何规划器依赖丢弃视觉丰富度的抽象场景表示，而学习型视觉模型往往缺乏几何可解释性与计算效率。论文试图在保留 3DGS 场景视觉丰富度的同时，实现具备几何可解释性和高效率的碰撞感知规划。

### 核心思路/方法
- 提出 CollisionSplatting：一种简单、模块化、GPU 加速、受概率启发且保守度可调的距离度量，直接运行在标准 3DGS 场景上。
- 与学习到的图像条件奖励函数结合后，该度量通过将碰撞感知代价与图像空间目标统一起来，支持几何与视觉的联合规划。
- 将该度量分别集成进 GPU 加速的 Model Predictive Path Integral（MPPI）与 Rapidly-Exploring Random Tree（RRT）规划器中。
- 在真实世界的视觉引导导航与操作任务中展示了该度量的有效性，并强调 3DGS 可作为丰富感知与实时运动规划之间的实用桥梁。

### 主要贡献
- 提出直接作用于标准 3DGS 场景的、可调保守度的概率式距离度量 CollisionSplatting。
- 实现碰撞感知代价与图像条件目标的统一，从而支持几何与视觉联合规划。
- 将该度量集成到 GPU 加速的 MPPI 与 RRT 规划器中。
- 在碰撞分类性能上与代表性基线持平或更优，同时碰撞检测吞吐显著更高、VRAM 占用显著更低（具体数值摘要未提供足够信息）。
- 在真实世界视觉引导导航与操作任务中验证了该度量的有效性。

### 局限性
摘要未提供足够信息。摘要未提及具体实验设置、对比基线的细节、失败案例、度量保守度调节的代价、方法对 3DGS 重建质量的依赖程度，以及真实世界任务的具体规模与评价指标。

### 阅读优先级
中。理由：该工作面向 3DGS 与运动规划交叉方向，提出的是模块化度量并集成到两种主流规划器中，且报告了吞吐与显存方面的优势，对关注神经场景表示用于机器人规划的研究者有参考价值；但摘要未给出定量结果细节与消融信息，是否构成关键突破需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

Incorporating dense visual information into motion planning remains challenging, as geometric planners rely on abstracted scene representations that discard visual richness, while learned visual models often lack geometric interpretability and computational efficiency. This paper introduces CollisionSplatting, a simple, modular, GPU-accelerated, probability-inspired distance metric with tunable conservatism that operates directly on standard 3D Gaussian Splatting (3DGS) scenes. When combined with learned image-conditioned reward functions, this metric enables joint geometric and visual planning by unifying collision-aware costs with image-space objectives. We integrate the metric into GPU-accelerated Model Predictive Path Integral (MPPI) and Rapidly-Exploring Random Tree (RRT) planners, and show on-par or better collision-classification performance compared to representative baselines while achieving substantially higher collision-checking throughput and significantly lower VRAM usage. Finally, we demonstrate the effectiveness of our metric in real-world vision-guided navigation and manipulation tasks, highlighting 3DGS as a practical bridge between rich perception and real-time motion planning.

</details>

#### 2026-09-28 - Less Is More: Genetic Frame Selection for Efficient Novel View Synthesis

**Authors:** Diego E. Farchione, Ramzi Idoughi, Alberto Jaspe-Villanueva, Peter Wonka
**Links:** [abs](https://arxiv.org/abs/2609.35573) - [pdf](https://arxiv.org/pdf/2609.35573)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, scene reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Less Is More: Genetic Frame Selection for Efficient Novel View Synthesis
- 作者：Diego E. Farchione, Ramzi Idoughi, Alberto Jaspe-Villanueva, Peter Wonka
- 出版日期：2026-09-28T16:33:50Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2609.35573 ；PDF https://arxiv.org/pdf/2609.35573

### 一句话总结
提出一种无需渲染的视图选择器，从已拍摄序列中挑选固定数量且信息量最大的输入帧，用于高效的新视角合成，并声称在多个数据集和输入预算下优于几何与重建感知的基线方法。

### 研究问题
前馈式新视角合成可从多张输入图像中单次前向重建场景，但更多视图不一定带来更好性能：冗余或选择不佳的帧会增加计算成本，甚至可能降低重建质量。论文关注的核心问题是：在已捕获的序列中，如何为指定目标视角选取一个固定大小的、对重建最具信息量的输入子集。

### 核心思路/方法
- 提出一种**无需渲染的视图选择器**，对候选帧从三个互补标准进行打分：
  1. **目标视图覆盖度**：以已观测帧作为目标视角的替代进行度量；
  2. **与已选视图的冗余度**；
  3. **图像清晰度**。
- 使用一个轻量级打分网络，在推理时无需渲染、重建或逐场景优化即可选出信息量最大的帧。
- 训练选择器时，通过**蒸馏一个昂贵的离线搜索过程**：用遗传算法在训练场景上直接优化重建性能，找出高质量子集；选择器仅从几何和图像级特征中学习复现这些选择。
- 摘要称该方法在六类数据集和多种输入预算下，持续优于几何类和重建感知的视图选择基线，选择成本显著低于基于重建的替代方案；精心选择的子集甚至可超过使用完整输入序列的前馈重建。
- 学习到的选择器可泛化到多种重建范式（前馈、3D Gaussian Splatting、NeRF）、目标物体重建，以及目标视角来自独立采集过程的跨捕获设定。

### 主要贡献
- 提出一种无需渲染的视图选择方法，通过目标覆盖度、冗余度和清晰度三项标准选择固定大小输入子集。
- 使用遗传算法离线搜索高质量子集，并蒸馏到轻量级打分网络，使其在推理时无需渲染或逐场景优化。
- 在六个数据集和多种输入预算上，声称优于几何和重建感知的视图选择基线，且选择成本显著更低。
- 表明精心选择的子集可优于完整输入序列的前馈重建。
- 验证学习到的选择器可泛化到前馈、3D Gaussian Splatting 和 NeRF 等多种重建范式，以及目标物体重建和跨捕获设定。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、对特定场景类型或数据分布的敏感性分析、遗传算法离线搜索的计算开销细节、打分网络规模与推理延迟的具体数值，也未说明选择器在极端输入预算或严重遮挡、动态场景等条件下的表现。

### 阅读优先级
高。理由：该论文聚焦新视角合成中“输入视图选择”这一效率与质量的关键问题，提出无需渲染的选择器并结合遗传算法蒸馏，且声称在多种数据集、重建范式和跨捕获设定下均有优势；若关注高效三维重建、神经渲染或视图选择，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Feed-forward novel view synthesis reconstructs a scene from many input images in a single forward pass, yet more views do not necessarily improve performance: redundant or poorly chosen frames increase computational cost and may degrade reconstruction quality. We address the problem of selecting, from an already captured sequence, a fixed-size subset of input views that is most informative for reconstructing specified target viewpoints. We propose a render-free view selector that scores candidate frames based on three complementary criteria: target-view coverage, measured against observed frames that stand in for the targets, redundancy with previously selected views, and image sharpness. A lightweight scoring network then selects the most informative frames without rendering, reconstruction, or per-scene optimization at inference time. To train the selector, we distill an expensive offline search procedure in which a genetic algorithm identifies high-quality subsets by directly optimizing reconstruction performance on training scenes. The selector learns to reproduce these choices from geometric and image-level features alone. Across six datasets and multiple input budgets, our method consistently outperforms both geometric and reconstruction-aware view-selection baselines while incurring significantly lower selection costs than reconstruction-based alternatives. Moreover, carefully selected subsets can outperform feed-forward reconstruction from the full input sequence. The learned selector generalizes across diverse reconstruction paradigms (feed-forward, 3D Gaussian Splatting, and NeRF), to object-targeted reconstruction and to a cross-capture setting in which the target views come from a separate acquisition pass. More broadly, our results indicate that explicitly reasoning about target relevance and inter-view redundancy is a fundamental factor in efficient scene reconstruction.

</details>

#### 2026-09-28 - EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation

**Authors:** Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im
**Links:** [abs](https://arxiv.org/abs/2609.34853) - [pdf](https://arxiv.org/pdf/2609.34853)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation
- 作者：Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im
- 出版日期：2026-09-28T10:46:23Z
- 分类：Neural Scene Representations & Rendering（主类）；Embodied / Robotics / AR Applications（次类）
- 链接：[摘要](https://arxiv.org/abs/2609.34853) / [PDF](https://arxiv.org/pdf/2609.34853)

### 一句话总结
EviSplat 提出在 3D Gaussian Splatting 中保留每个观测的独立特征作为“证据”，等到文本查询到来时再根据查询动态聚合，从而避免查询前多视图信息合并造成的线索损失。

### 研究问题
开放词汇三维场景理解希望无需固定类别词表，就能根据自由文本查询定位与分割对象。已有方法多基于 3D Gaussian Splatting，并在查询未知之前，将多视图观测（如单视图的掩码裁剪）整合为语言特征或紧凑对象描述符。但摘要指出，同一对象的不同视角观测信息量并不相等：有的包含与特定查询相关的线索，有的则提供不完整甚至误导性的证据。查询前的提前整合，可能抑制后续查询真正依赖的线索。

### 核心思路/方法
EviSplat 的核心是“保留个体观测特征，直到文本查询时刻再使用”。具体而言：
- 将个体观测特征保留在类别无关的三维实例中，这些实例可表示对象、对象部件或背景区域。
- 为每个 Gaussian 学习一个分布，描述其观测支持哪些视觉外观。
- 给定文本查询后，先对每个实例使用其最相关的观测进行打分。
- 再为每个 Gaussian 计算分数，方式是结合实例级相关性与局部支持的证据，并按该 Gaussian 被观测的频率与明确程度进行加权。
- 由此，不同查询可以从同一份保留证据中调用不同的视觉线索。

### 主要贡献
- 提出 EviSplat，在开放词汇三维分割中保留多视图个体观测特征作为证据，而不是在查询前将其合并为单一语言特征或对象描述符。
- 将证据保留在类别无关的三维实例中，并学习每个 Gaussian 的外观支持分布。
- 设计查询时打分机制：先按实例最相关观测评分，再融合实例级相关性与局部证据，并按观测频率与明确程度加权。
- 摘要称在多种数据集和评估协议上取得 state-of-the-art 性能，支持“将多视图证据保留到查询时并按查询聚合”的有效性。

### 局限性
摘要未提供足够信息。摘要未给出具体失败情形、计算开销、内存占用、对 Gaussian 数量或视图数量的敏感性、在极端遮挡或观测不足条件下的表现，也未说明“观测频率与明确程度”加权方式可能带来的偏差。相关实验细节与消融结果需查阅原文。

### 阅读优先级
高。理由：该工作针对开放词汇三维场景理解中“查询前多视图信息整合”的关键问题提出明确替代思路，问题动机具体，方法与 3D Gaussian Splatting 紧密相关，且摘要声称在多样数据集与评估协议上达到 state-of-the-art；对三维场景表示、开放词汇分割及具身/机器人应用方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Open-vocabulary 3D scene understanding enables object localization and segmentation from free-form text queries without a fixed category vocabulary. Many recent methods build on 3D Gaussian Splatting and consolidate multi-view observations, such as masked crops from individual views, into language features or compact object descriptors before the query is known. However, observations of the same object vary across viewpoints and are not equally informative: some reveal cues relevant to a particular query, whereas others provide incomplete or misleading evidence. Pre-query consolidation can therefore suppress cues on which a later query depends. We introduce EviSplat, which preserves individual observation features as evidence for later text queries. EviSplat retains individual observation features within class-agnostic 3D instances that represent objects, object parts, or background regions. It also learns, for each Gaussian, a distribution describing which visual appearances its observations support. Given a text query, EviSplat scores each instance using its most relevant observations. It then computes a score for each Gaussian by combining instance-level relevance with locally supported evidence, weighted by how often and how unambiguously that Gaussian was observed. Different queries can thus draw on different visual cues from the same preserved evidence. Experiments across diverse datasets and evaluation protocols demonstrate state-of-the-art performance, supporting the benefit of preserving multi-view evidence until query time and aggregating it according to the query.

</details>

#### 2026-09-28 - SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering

**Authors:** Jingqian Sun, Yichao Tang
**Links:** [abs](https://arxiv.org/abs/2609.34733) - [pdf](https://arxiv.org/pdf/2609.34733)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural rendering, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering
- 作者：Jingqian Sun, Yichao Tang
- 出版日期：2026-09-28T09:31:12Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.34733 ；PDF：https://arxiv.org/pdf/2609.34733

### 一句话总结
SurgGMF 提出一种全因果高斯运动预测框架，通过从历史高斯运动场预测未来高斯的位置、尺度和旋转残差，并结合“全因果末帧渲染协议”避免目标帧信息泄漏，从而把手术场景神经渲染从回顾式重建推进到预测式建模。

### 研究问题
动态手术场景建模对机器人感知、仿真和决策支持很重要。现有神经渲染方法虽能高效重建和渲染可变形手术场景，但主要聚焦于已观测帧的重建，而不是预测未来场景状态。论文要解决的核心问题是：如何在避免目标泄漏的前提下，实现面向未来手术场景渲染的因果高斯运动预测。

### 核心思路/方法
- 不直接预测未来 RGB 图像，而是从历史高斯运动场中预测未来高斯运动状态，具体表示为位置、尺度、旋转残差（X/S/R）。
- 引入 full-causal-last rendering protocol（全因果末帧渲染协议）：渲染未来高斯状态时不访问目标帧高斯属性，同时保留因果外观传播，以防止目标泄漏。
- 在 12 个 EndoNeRF 和 StereoMIS 视频切片上评估，使用神经时间学习器与经典动力学基线，并在统一预测协议下比较。
- 分析精度与效率的权衡：在当前实现下，TKAN 精度最高，而 GRU 和 LSTM 在模块级延迟方面更具优势。

### 主要贡献
- 提出 SurgGMF，一个用于预见性手术场景渲染的全因果高斯运动预测框架。
- 将预测目标从未来 RGB 图像转为未来高斯运动状态（位置、尺度、旋转残差）。
- 引入 full-causal-last 渲染协议，以避免目标帧高斯属性泄漏，同时保持因果外观传播。
- 在 12 个 EndoNeRF 和 StereoMIS 视频切片上，使用神经时间学习器和经典动力学基线进行统一预测协议下的评估。
- 结果显示，学习到的高斯运动预测在渲染空间上持续优于经典动力学基线，说明其收益超过手工状态外推。
- 延迟分析揭示了精度—效率权衡，并指出 TKAN、GRU、LSTM 在当前实现下的不同表现。
- 论文将结果定位为可复现的因果高斯运动预测框架，推动手术高斯表示从回顾式重建走向预测式场景建模。

### 局限性
摘要未提供足够信息。摘要未说明具体失败案例、数据规模限制、泛化到其他手术类型或设备的能力、临床部署可行性，也未给出完整计算成本、推理速度数值、超参数敏感性或与其他预测范式的全面对比。

### 阅读优先级
高。理由：该论文聚焦手术场景神经渲染中的未来状态预测，问题设定明确，且提出全因果渲染协议以避免目标泄漏；同时包含多数据集评估、神经时间学习器与经典动力学基线对比，以及精度—效率权衡分析，对关注动态手术场景建模、高斯表示和预测式渲染的研究者有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic surgical scene modeling is essential for robotic perception, simulation, and decision support. Although existing neural rendering methods enable efficient reconstruction and rendering of deformable surgical scenes, they remain primarily focused on observed-frame reconstruction rather than forecasting future scene states. To this end, we present SurgGMF, a fully causal Gaussian motion forecasting framework for anticipatory surgical scene rendering. Rather than predicting future RGB images directly, SurgGMF forecasts future Gaussian motion states represented by position, scale, and rotation residuals (X/S/R) from historical Gaussian motion fields. To prevent target leakage, we introduce a full-causal-last rendering protocol, where future Gaussian states are rendered without accessing target-frame Gaussian attributes while preserving causal appearance propagation. We evaluate SurgGMF on 12 EndoNeRF and StereoMIS video slices using neural temporal learners and classical dynamics baselines under a unified forecasting protocol. Learned Gaussian motion forecasting consistently outperforms classical dynamics baselines in render space, demonstrating gains beyond hand-crafted state extrapolation. Latency analysis further reveals an accuracy--efficiency trade-off: under the current implementations, TKAN achieves the highest accuracy, whereas GRU and LSTM provide more favorable module-level latency profiles. These results establish SurgGMF as a reproducible framework for causal Gaussian motion forecasting and advance surgical Gaussian representations from retrospective reconstruction toward predictive scene modeling.

</details>

#### 2026-09-28 - GenNVS: Geometry-enhanced Novel View Synthesis via Disentangled 3D Prior

**Authors:** Yajiao Xiong, Youyu Luan, Xiaoyu Zhou, Yongtao Wang
**Links:** [abs](https://arxiv.org/abs/2609.34579) - [pdf](https://arxiv.org/pdf/2609.34579)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GenNVS: Geometry-enhanced Novel View Synthesis via Disentangled 3D Prior
- 作者：Yajiao Xiong, Youyu Luan, Xiaoyu Zhou, Yongtao Wang
- 出版日期：2026-09-28T08:23:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接：https://arxiv.org/abs/2609.34579 ；PDF 链接：https://arxiv.org/pdf/2609.34579

### 一句话总结
GenNVS 通过解耦前景与背景的 3D 先验，并将其对齐为统一 3D 场景来条件化视频扩散模型，从而提升单图新视角合成中的几何结构保持与空间一致性。

### 研究问题
论文关注单图像新视角合成任务。摘要指出，该任务的核心困难在于底层 3D 几何高度模糊。尽管近期基于扩散的方法能产生看似合理的结果，但它们往往难以保持前景对象的几何结构和空间连贯性。

### 核心思路/方法
GenNVS 的核心是“通过解耦 3D 先验实现几何增强的新视角合成”。具体而言：
- 使用 3D Gaussian Splatting 分别建模前景对象和背景；
- 通过由粗到细的几何优化过程将二者对齐，形成统一的 3D 场景；
- 用该场景条件化一个视频扩散模型；
- 提出 Dual-Stream Masking 机制，联合利用渲染的有效性掩码和几何感知变形来引导合成。

### 主要贡献
- 提出 GenNVS 框架，用于几何增强的新视角合成，核心在于解耦的 3D 先验。
- 采用 3D Gaussian Splatting 分别表示前景对象与背景，并通过由粗到细的几何优化对齐成统一 3D 场景。
- 提出 Dual-Stream Masking 机制，以渲染有效性掩码和几何感知变形共同条件化视频扩散模型。
- 摘要称实验结果显示，GenNVS 在视觉质量和几何精度上优于近期方法，并自然支持灵活的场景编辑。

### 局限性
摘要未提供足够信息。未说明方法的具体失败场景、计算开销、对输入图像或场景类型的假设、评估数据集与指标细节，也未给出消融实验或用户研究等信息。

### 阅读优先级
高。理由：该论文聚焦单图新视角合成中关键的几何模糊与空间一致性问题，提出解耦 3D 先验、3D Gaussian Splatting 与视频扩散模型结合的具体框架，并声称在视觉质量和几何精度上优于近期方法，同时支持场景编辑；这些信息对神经场景表示与渲染方向具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Single-image novel view synthesis remains challenging because the underlying 3D geometry is highly ambiguous. Recent diffusion-based approaches produce plausible results, but they often struggle to preserve the geometric structure and spatial coherence of foreground objects. We present GenNVS, a framework for geometry-enhanced novel view synthesis via a disentangled 3D prior. Specifically, GenNVS models foreground objects and the background with 3D Gaussian Splatting and aligns them through a coarse-to-fine geometric optimization process to form a unified 3D scene. This scene conditions a video diffusion model through the proposed Dual-Stream Masking mechanism, which guides synthesis by jointly exploiting rendered validity masks and geometry-aware warping. Experimental results show that GenNVS performs favorably against recent methods in both visual quality and geometric accuracy, while naturally supporting flexible scene editing.

</details>

#### 2026-09-28 - Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting

**Authors:** Yulong Cheng, Youneng Bao, Junfeng Zhou, Mu Li, Jie Wen
**Links:** [abs](https://arxiv.org/abs/2609.34367) - [pdf](https://arxiv.org/pdf/2609.34367)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, splatting, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting
- 作者：Yulong Cheng, Youneng Bao, Junfeng Zhou, Mu Li, Jie Wen
- 出版日期：2026-09-28T05:44:08Z
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（次）
- 链接：[摘要](https://arxiv.org/abs/2609.34367) / [PDF](https://arxiv.org/pdf/2609.34367)

### 一句话总结
论文提出 OIC-GS，一种基于分层 HEALPix 基元网格表示的全向高斯泼溅编解码器，通过球面率失真目标自适应决定基元分配并移除低收益基元，在单个比特流下同时支持全球、视口相关与渐进解码。

### 研究问题
学习图像编解码器（LICs）重建质量高，但解码速度不足以支撑沉浸式 VR；高斯泼溅（GS）编解码器渲染更快，但在重建质量上仍落后，且通常在决定基元分配时未考虑每个基元的编码代价。论文旨在解决全向 GS 编解码中重建质量、解码效率与基元分配之间的问题。

### 核心思路/方法
- 引入 OIC-GS，一种采用分层 HEALPix 基元网格表示的全向 GS 编解码器。
- 高斯基元锚定在预定义球面位置上，从而消除显式坐标编码。
- 更细层级对更粗祖先进行细化，自然支持粗到细重建和分层传输。
- 预定义网格支持高效视口解码，仅选择与视图相关的基元。
- 引入针对量化基元的轻量熵模型，并在球面率失真目标下优化编解码器。
- 当量化后不透明度变为零时，自动移除率失真收益不足的基元，使 OIC-GS 无需固定基元预算即可自适应调整基元密度和细节层级。
- 单个比特流支持全球、视口相关和渐进解码。

### 主要贡献
- 提出 OIC-GS 全向 GS 编解码器与新的分层 HEALPix 基元网格表示。
- 通过预定义球面锚点消除显式坐标编码，并支持粗到细重建、分层传输与视口相关解码。
- 引入轻量熵模型，并在球面率失真目标下优化，使基元可根据率失真收益自动移除，避免固定基元预算。
- 单个比特流支持全球、视口相关和渐进三种解码方式。
- 摘要报告：首个视口仅解码 52% 比特流即达到最终质量，渲染速度为 1,270 FPS；在 100 图像全向基准上，OIC-GS 优于所有被评估的 GS 编解码器，相比 GaussianImage++ 将 WS-PSNR BD-rate 降低 49.6%，相比使用学习熵模型的 SGI 降低 68.6%。

### 局限性
- 除摘要给出的结果外，论文的具体实验设置、数据集细节、消融实验、复杂度与内存开销等均未提供足够信息。
- 熵模型、率失真优化与基元移除策略的具体实现细节未提供足够信息。
- 与其他方法对比的完整评测范围、指标定义与统计方式未提供足够信息。
- 摘要未提供足够信息说明该方法在真实 VR 系统或不同硬件条件下的部署表现。
- 摘要未提供足够信息说明其在不同场景类型、分辨率或比特率下的泛化能力。

### 阅读优先级
高。理由：该论文直接针对全向 GS 编解码中重建质量、解码速度与基元分配代价之间的核心矛盾，提出分层 HEALPix 表示与率失真自适应基元选择，并报告了显著的 BD-rate 降低和视口解码效率，属于神经场景表示与渲染方向中较有实际价值的工作。

</details>

<details>
<summary>Abstract</summary>

Learned image codecs (LICs) achieve high reconstruction quality, but their decoding speed is often insufficient for immersive virtual reality (VR). Gaussian splatting (GS) codecs render much faster, yet still lag in reconstruction quality and typically decide primitive allocation without considering the coding cost of each primitive. We introduce OIC-GS, an omnidirectional GS codec with a new hierarchical HEALPix primitive grid representation. Gaussian primitives are anchored at predefined spherical locations, eliminating explicit coordinate coding. Finer levels refine their coarser ancestors, naturally supporting coarse-to-fine reconstruction and layered transmission. The predefined grid also enables efficient viewport decoding by selecting only view-relevant primitives. We further introduce a lightweight entropy model for quantized primitives and optimize the codec under a spherical rate-distortion objective. Primitives with insufficient rate-distortion benefit are automatically removed when their quantized opacity becomes zero, allowing OIC-GS to adapt both primitive density and level of detail without a fixed primitive budget. A single bitstream supports full-sphere, viewport-dependent, and progressive decoding. The first viewport reaches final quality after decoding only 52% of the bitstream, and is then rendered at 1,270 FPS. On a 100-image omnidirectional benchmark, OIC-GS outperforms all evaluated GS codecs, reducing WS-PSNR BD-rate by 49.6% over GaussianImage++ and 68.6% over SGI, which uses a learned entropy model.

</details>

#### 2026-09-28 - AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting

**Authors:** Amirhossein Mollaei Khass, Nader Motee
**Links:** [abs](https://arxiv.org/abs/2609.34176) - [pdf](https://arxiv.org/pdf/2609.34176)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting
- 作者：Amirhossein Mollaei Khass, Nader Motee
- 出版日期：2026-09-28T02:53:40Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.34176

### 一句话总结
AGILE-GS 将“寻找信息最多的位置”与“在候选池中选择相机”分离，通过优化一个不一定可达的虚拟锚点姿态来引导候选视角评分，从而在无需渲染全部候选的情况下快速选出下一个最佳视角。

### 研究问题
辐射场重建需要大量视角，且视角的布置位置与数量同样重要。针对 3D Gaussian Splatting 的下一个最佳视角（NBV）选择，现有方法通常需要对候选池中的每个候选逐一评分再保留一个，搜索信息与选择相机混在一起，导致选择延迟高。论文要解决的问题是：如何在不渲染全部候选、也不对整个候选池计算 Fisher 信息的前提下，高效选出一个高质量的下一视角。

### 核心思路/方法
方法的核心是把信息搜索与相机选择拆成两个可分离的问题：

1. **锚点优化**：在 SE(3) 上用黎曼梯度上升优化一个虚拟锚点姿态，目标是期望信息增益。该锚点不需要可达，也不必存在于候选池中，它只用于标示模型最不确定的位置。
2. **候选评分与筛选**：候选视角依据锚点的观察几何进行评分，再通过一个贪心的 ridge-leverage 步骤把候选池蒸馏成一个小的、非冗余的候选短名单，此过程不渲染任何候选。
3. **两种使用方式**：
   - **AGILE-GS**：直接取短名单上的第一个视角作为下一视角，因此不对任何候选计算 Fisher 信息。
   - **AGILE-GS+**：对短名单中每个视角计算 Fisher 信息增益并选最优，使昂贵评估只在一小部分视角上运行，而非整个候选池。

### 主要贡献
- 提出将 NBV 选择中的信息搜索与相机选择分离的框架，并引入可不可达的虚拟锚点来标记模型最不确定的位置。
- 提出锚点引导的候选评分与贪心 ridge-leverage 筛选机制，在不渲染任何候选的情况下将候选池压缩为非冗余短名单。
- 提供两种变体：AGILE-GS 不计算任何候选的 Fisher 信息；AGILE-GS+ 仅对短名单计算 Fisher 信息。
- 摘要声称在标准基准和闭环具身采集场景中，两种变体均匹配或超过现有基线，同时将选择延迟降低一到两个数量级。

### 局限性
摘要未提供足够信息。摘要中未说明锚点优化是否依赖特定场景假设、短名单大小如何确定、在什么条件下 Fisher 信息评估不可省略、失败案例或具体延迟数值与基准名称等实验细节。

### 阅读优先级
中。理由：论文针对 3DGS 主动视角选择中的效率瓶颈提出了结构清晰的两段式分离方案，并声称延迟降低一到两个数量级，对关注主动重建、NBV 选择与 3DGS 效率的研究者有潜在参考价值；但摘要未提供具体实验设置、基准名称与定量结果，且该工作尚未经过摘要之外的信息验证，是否值得精读需结合全文实验与自身方向判断。

</details>

<details>
<summary>Abstract</summary>

Radiance fields need hundreds of views, and their placement matters as much as their number. Next-best-view (NBV) selection for 3D Gaussian Splatting (3DGS) usually scores every candidate in the pool and keeps one. Searching for information and choosing a camera, however, are separable problems. We present AGILE-GS, an anchor-guided NBV method that separates the two. A virtual anchor pose is optimized on SE(3) by Riemannian gradient ascent on expected information gain. It need not be reachable or in the pool; it marks where the model is most uncertain. Candidates are scored against the anchor's viewing geometry, and a greedy ridge-leverage step distills the pool into a small, non-redundant shortlist without rendering any candidate. The shortlist can be used in two ways. AGILE-GS takes the first view on it as the next view, so no Fisher information is computed for any candidate. AGILE-GS+ computes the Fisher information gain of each shortlisted view and picks the best, so the expensive evaluation runs on a handful of views rather than the whole pool. On standard benchmarks and in closed-loop embodied acquisition, both match or exceed existing baselines while cutting selection latency by one to two orders of magnitude.

</details>

#### 2026-09-27 - Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors

**Authors:** Ge Gao, Siyue Teng, Chanqgi Wang, Fan Zhang, Nantheera Anantrasirichai, Jui Chiu Chiang, Wen-Hsiao Peng, David Bull
**Links:** [abs](https://arxiv.org/abs/2609.33969) - [pdf](https://arxiv.org/pdf/2609.33969)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic 3D, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors
- 作者：Ge Gao, Siyue Teng, Chanqgi Wang, Fan Zhang, Nantheera Anantrasirichai, Jui Chiu Chiang, Wen-Hsiao Peng, David Bull
- 出版日期：2026-09-27T22:14:31Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2609.33969 ；PDF 链接 https://arxiv.org/pdf/2609.33969

### 一句话总结
论文提出 SAGA，一种基于稀疏 4D anchors 与 3D Gaussian Splatting 的体积视频编解码方法，通过层次化 anchor、坐标型 INR 解码与固定大小记忆槽的熵上下文建模，压缩动态 3D 场景并在摘要报告的实验中对 GIFStream 取得显著 BD-rate 降低。

### 研究问题
沉浸式视频通信需要既照片级真实、渲染高效又紧凑的动态场景表示。动态 3D Gaussian Splatting 虽具潜力，但因 primitives 密集且存在时空冗余而难以压缩。现有基于 anchor 的方法虽能以稀疏 scaffold 共享几何与外观来提升紧凑性，但通常依赖对单一 canonical scaffold 做变形，并且每个 primitive 仅独立地以其关联 anchor 为条件，这限制了处理非局部动态与去遮挡的能力，也未能充分利用 anchor 之间的相关性，尤其在运动或纹理密集区域。

### 核心思路/方法
论文提出 SAGA，作为建立在稀疏 anchor 辅助 Gaussian splatting 表示之上的体积视频编解码器。其核心包括：
- 使用层次化组织的稀疏 4D anchors 表示动态 3D 场景；
- 通过基于坐标的 INR 解码器，从 anchor 间插值生成精细 anchors 与 Gaussian primitives，从而在时空结构间实现紧凑的参数共享；
- 针对非结构化 anchors 之间的长程依赖，引入固定大小 memory slots，并采用 orthogonality-informed updates，用于准确的熵上下文建模。

### 主要贡献
- 提出 SAGA 体积视频编解码框架，基于稀疏 anchor 辅助的 Gaussian splatting 表示。
- 采用层次化稀疏 4D anchors 与坐标型 INR 解码器，通过 anchor 间插值生成精细 anchors 和 Gaussian primitives，实现跨时空结构的紧凑参数共享。
- 引入固定大小 memory slots 与 orthogonality-informed updates，以建模非结构化 anchors 间的长程依赖并服务于熵上下文建模。
- 实验显示 SAGA 对 GIFStream 取得强率失真性能，在 Neu3D 和 MPEG MIV 上分别实现 80.39% 与 83.94% 的 PSNR BD-rate 降低。

### 局限性
摘要未提供足够信息说明方法的失败场景、计算开销、解码复杂度、泛化边界或与更多基线方法的完整对比。摘要仅报告了相对 GIFStream 的 PSNR BD-rate 结果，未提供其他评价指标、数据集细节、消融实验细节或运行时信息，因此这些方面的局限性无法从给定材料判断。

### 阅读优先级
高。理由：该论文聚焦动态 3D Gaussian Splatting 压缩这一沉浸式视频通信中的关键问题，所提方法结合稀疏 4D anchors、INR 插值与 memory-based 熵建模，且摘要报告了在 Neu3D 和 MPEG MIV 上相对 GIFStream 的大幅 BD-rate 降低，对神经场景表示、体积视频压缩与渲染效率方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Immersive video communication requires photorealistic, render-efficient, and compact dynamic scene representations. 3D Gaussian Splatting (3DGS) offers a promising representation, but dynamic 3DGS remains difficult to compress due to dense primitives and spatiotemporal redundancy. Anchor-based formulations improve compactness with sparse scaffolds that share geometry and appearance across primitives. However, existing designs often rely on deforming a single canonical scaffold and condition each primitive on its associated anchor in isolation, limiting their ability to handle non-local dynamics and disocclusion while under-exploiting inter-anchor correlations, particularly in motion- or texture-dense regions. To address these limitations, we propose SAGA, a volumetric video codec built upon Sparse Anchor-assisted GAussian splatting representations. SAGA represents dynamic 3D scenes using hierarchically organized sparse 4D anchors, where coordinate-based INR decoders generate fine anchors and Gaussian primitives from inter-anchor interpolations, enabling compact parameter sharing across spatiotemporal structures. For long-range dependencies among unstructured anchors, we further introduce fixed-size memory slots with orthogonality-informed updates for accurate entropy-context modeling. Experiments show that SAGA achieves strong rate-distortion performance against GIFStream, with PSNR BD-rate reductions of 80.39% and 83.94% on Neu3D and MPEG MIV, respectively.

</details>

#### 2026-09-27 - Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation

**Authors:** Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang
**Links:** [abs](https://arxiv.org/abs/2609.33872) - [pdf](https://arxiv.org/pdf/2609.33872)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation
- 作者：Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang
- 出版日期：2026-09-27T19:48:57Z
- 分类：Neural Scene Representations & Rendering（主分类）；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.33872 ；PDF https://arxiv.org/pdf/2609.33872 ；项目网站 https://robot-gst.github.io

### 一句话总结
Robot-GST 提出一种几何感知的时空行为表示与评估框架，通过 3D Gaussian Splatting 与 SAM3D 构建高斯-SAM 机器人环境进行真机到仿真的策略验证，在动作执行前先仿真评估候选动作序列，以提升长时程操作部署的可靠性。

### 研究问题
机器人操作策略日益依赖视觉语言模型进行端到端决策，但可靠部署仍面临挑战：许多策略缺乏显式机制来预测任务结果，也缺乏评估生成动作能否达成期望最终状态的能力，导致长时程操作中执行误差不断累积。论文试图解决如何在真实执行前对策略生成的动作进行可行性与最终状态评估的问题。

### 核心思路/方法
- 构建几何感知的时空行为表示与评估框架 Robot-GST。
- 基于 RGB-D 观测，利用 3D Gaussian Splatting 与 SAM3D 构建高保真机器人环境，形成 Gaussian-SAM 机器人环境，用于真机到仿真的策略验证，实现“先仿真评估、再执行”。
- 将视觉观测与语言指令结合，借助大型视觉语言模型进行时空推理以支持长时程任务规划。
- 为衔接高层规划与真实执行，引入高斯感知的最终状态估计，通过几何采样与基于状态的轨迹规划实现。
- 在执行前，将候选动作序列放入 Gaussian-SAM 环境中仿真与评估，以过滤不可行的行为。

### 主要贡献
- 提出 Robot-GST 框架，将几何感知的时空行为表示与评估引入机器人操作策略部署流程。
- 构建基于 3D Gaussian Splatting 与 SAM3D 的 Gaussian-SAM 机器人环境，支持从 RGB-D 观测生成高保真仿真环境，实现先评估后执行。
- 引入高斯感知的最终状态估计与基于状态的轨迹规划，连接高层视觉语言规划与真实执行。
- 在涉及刚性、软性和可变形物体的代表性操作任务（包括方块放置、玩具打包、鸭子重排）上进行验证，表明几何感知的时空推理与状态感知执行可提升不同物体类别下的操作可靠性。
- 结果表明，将几何感知重建与高质量渲染和仿真结合，为评估机器人操作行为提供了可扩展的途径。

### 局限性
- 摘要未提供足够信息说明方法在何种硬件平台、实时性、计算开销或大规模场景下的表现。
- 摘要未提供足够信息说明该方法在失败案例、极端物体类别或复杂动态环境中的边界条件。
- 摘要未提供足够信息说明与现有基线方法的定量对比结果及具体评价指标。
- 摘要未提供足够信息说明 Gaussian-SAM 环境构建精度对最终策略执行效果的影响程度。

### 阅读优先级
中。理由：该论文聚焦机器人操作策略的可靠部署与“先仿真评估再执行”的评估框架，结合 3D Gaussian Splatting、SAM3D 与视觉语言模型，主题具有明确的应用价值与交叉性；但摘要仅给出方法概览和任务类别，未提供定量结果、基线对比与实现细节，因此对需要深入评估方法有效性或复现实验的读者而言，需进一步阅读全文才能判断其贡献强度。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation policies are advancing rapidly with increasing reliance on vision-language models for end-to-end decision making. However, reliable deployment remains challenging because many policies lack explicit mechanisms for predicting task outcomes and evaluating whether generated actions will achieve desired final states, causing execution errors to accumulate during long-horizon manipulation. We present Robot-GST, a geometry-aware spatio-temporal behaviour representation and evaluation framework that constructs a Gaussian-SAM robotic environment for real-to-sim policy verification and improves the reliability of real-world manipulation deployment. Our approach constructs a high-fidelity robotic environment from RGB-D observations using 3D Gaussian Splatting and SAM3D, enabling ``simulation and evaluation before acting''. It integrates visual observations and language instructions with spatio-temporal reasoning for long-horizon task planning using large vision-language models. To bridge high-level planning and real-world execution, we introduce Gaussian-aware final-state estimation through geometric sampling and state-based trajectory planning. Before execution, candidate action sequences are simulated and evaluated in the Gaussian-SAM environment to filter infeasible behaviours. We validate our approach on representative manipulation tasks involving rigid, soft, and deformable objects, including cube placing, toy packing, and duck rearrangement, demonstrating that geometry-aware spatio-temporal reasoning and state-aware execution improve manipulation reliability across different object categories. Our results suggest that combining geometry-aware reconstruction with high-quality rendering and simulation provides a scalable approach for evaluating robotic manipulation behaviours. Website: https://robot-gst.github.io

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-01 - World Observer: Joint Actor-Observer Generation for Persistent World Modeling

**Authors:** Hyunwook Choi, Dahyun Chung, Hyunsung Kim, Siyoon Jin, Jinhyeok Choi, Junyoung Seo, Seungryong Kim
**Links:** [abs](https://arxiv.org/abs/2610.02162) - [pdf](https://arxiv.org/pdf/2610.02162)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：World Observer: Joint Actor-Observer Generation for Persistent World Modeling
- 作者：Hyunwook Choi, Dahyun Chung, Hyunsung Kim, Siyoon Jin, Jinhyeok Choi, Junyoung Seo, Seungryong Kim
- 出版日期：2026-10-01T17:53:20Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类摘要未提供足够信息
- 链接：摘要链接 https://arxiv.org/abs/2610.02162 ；PDF 链接 https://arxiv.org/pdf/2610.02162

### 一句话总结
World Observer 通过将“观察”与“行动”解耦，联合生成以智能体为中心的 actor 视角与一个或多个全景 observer，以缓解视频世界模型在物体离开 actor 视野后丢失其演化状态的问题。

### 研究问题
论文关注视频世界模型中的持续世界建模问题：现有视频世界模型通常以 actor 为中心来模拟环境随动作的演化，但一旦物体离开 actor 的当前视野，模型就失去对该物体演化的直接证据，导致物体重新进入视野时难以保持其状态与动态。核心问题是：世界模型如何持续观察 actor 当前视野之外的区域？

### 核心思路/方法
- 将观察与行动解耦：不再仅生成 actor 视角，而是联合生成一个以智能体为中心的 perspective actor，以及一个或多个观察选定世界区域的全景 observer。
- 通过 observer 保持离视野物体的视觉演化：离开 actor 视野的物体仍可在 observer 中持续演化，从而在其重新进入 actor 视野时反映更新后的状态。
- 几何对应：从共享的全景源进行 warp，以显式建立 actor 与 observer 之间的几何对应关系。
- Observer Sink：引入高分辨率透视参考，用于在物体重新进入视野时恢复精细外观。
- 灵活放置与控制：由于 observer 与 actor 解耦，observer 可自由放置在场景中、扩展到多个位置以扩大覆盖范围，并可由控制信号驱动以引导视野外的演化。
- 评估方式：提出 world-space metrics 以及覆盖真实与合成场景的 benchmark，用于评估视野外演化。

### 主要贡献
- 提出 World Observer，一种联合 actor-observer 生成框架，用于持续世界建模，使离开 actor 视野的物体仍能被持续观察并保持演化。
- 通过共享全景源 warp 建立 actor 与 observer 的显式几何对应，并引入 Observer Sink 高分辨率透视参考来恢复重新进入时的精细外观。
- 将 observer 与 actor 解耦，使其可自由放置、多位置扩展，并可由控制信号驱动以引导视野外演化。
- 引入用于评估视野外演化的 world-space metrics 和覆盖真实与合成场景的 benchmark。
- 摘要声称 World Observer 在显著改善视野外动态的同时，在视觉保真度、相机控制和 3D  adherence 方面仍具竞争力。

### 局限性
摘要未提供足够信息。论文摘要未说明具体失败场景、计算成本、对 observer 数量或放置方式的依赖、benchmark 规模、真实场景与合成场景的具体构成，也未给出与基线方法的详细定量比较。

### 阅读优先级
高。理由：该论文针对视频世界模型中一个明确且重要的问题，即 actor 离开视野后物体状态与动态难以保持，并提出了解耦 actor 与 observer 的框架、配套评估指标与 benchmark。对于关注 embodied / robotics / AR 应用、视频世界模型、持续世界建模与视野外演化生成的研究者，具有较高相关性和潜在参考价值。

</details>

<details>
<summary>Abstract</summary>

How can a world model continuously observe regions beyond the actor's current view? Video world models simulate how an environment evolves from an agent's actions, yet remain actor-centric. Once an object leaves the actor's view, they lose direct evidence of its evolution, often failing to preserve its state and dynamics upon re-entry. To address this, we introduce World Observer, which decouples observing from acting by jointly generating a perspective actor for the agent-centric view with one or more panoramic observers that watch selected world regions. This allows objects that leave the actor's view to remain visually evolving in an observer, so their updated states are reflected when they re-enter. We ground the actor and observers by warping from a shared panoramic source for explicit geometric correspondence, and introduce an Observer Sink of high-resolution perspective references to restore fine appearance upon re-entry. Since the observers are decoupled from the actor, they can be placed freely across the scene, extended to multiple locations for broader coverage, and driven by control signals to steer out-of-view evolution. To evaluate out-of-view evolution, we further introduce world-space metrics and a benchmark spanning real and synthetic scenes. World Observer substantially improves out-of-view dynamics while remaining competitive in visual fidelity, camera control, and 3D adherence.

</details>

#### 2026-10-01 - GlassGuard: Verified Glass Plane Mapping for Robot Navigation

**Authors:** Hanwen Guo, Zhengzhi Lin, Yusen Xie, Ji Zhang
**Links:** [abs](https://arxiv.org/abs/2610.02110) - [pdf](https://arxiv.org/pdf/2610.02110)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GlassGuard: Verified Glass Plane Mapping for Robot Navigation
- 作者：Hanwen Guo, Zhengzhi Lin, Yusen Xie, Ji Zhang
- 出版日期：2026-10-01T17:31:23Z
- 分类：Embodied / Robotics / AR Applications（无二级分类信息）
- 链接：[摘要](https://arxiv.org/abs/2610.02110) | [PDF](https://arxiv.org/pdf/2610.02110)

### 一句话总结
GlassGuard 是一个面向机器人导航的玻璃平面重建框架，利用视觉与 LiDAR 的互补证据恢复建筑玻璃平面，并在“玻璃覆盖率”与“自由空间污染”两个维度上同时优化。

### 研究问题
透明和镜面表面对基于 LiDAR 的 SLAM 与导航构成严重挑战：激光回波可能穿过玻璃，导致碰撞边界在地图中缺失。已有工作尝试重建缺失表面，但不准确的障碍物放置可能引发相反方向的失败，即污染可通行的自由空间。因此论文将玻璃重建视为一个双重需求问题：既要覆盖玻璃，又要避免自由空间被错误占据。

### 核心思路/方法
- 提出 GlassGuard，一个面向导航的框架，从互补的视觉与 LiDAR 证据中重建平面建筑玻璃。
- 将“成功”定义为同时考虑玻璃覆盖率与自由空间污染，并将这一原则贯穿提案验证与全局地图构建。
- 方法流程：基础视觉模型提供玻璃实例掩码；结构化 3D 线索生成度量平面假设；无深度的 2D 投影几何检查其朝向；随后进入统一的全局地图。

### 主要贡献
- 明确提出玻璃重建中的双重需求：既不能漏掉玻璃碰撞边界，也不能因此污染自由空间。
- 提出结合视觉实例掩码、结构化 3D 线索与无需深度的 2D 投影几何验证的玻璃平面重建流程。
- 在九个建筑尺度场景中评估，覆盖多样玻璃结构、空间尺度与光照条件，包含超过一小时、2.1 km 的真实机器人行进。
- 全景版本达到 85% 的总玻璃覆盖率；在相同针孔输入下达到 82% 总覆盖率（对比基线最高 61%），同时每帧假体素数减少 5–17 倍。
- 定性示例表明，结合导航规划器时，重建平面能够阻断穿过玻璃的路径，同时保留可通行路线。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、计算开销、不同玻璃类型（如曲面玻璃、多层玻璃）的适用边界，也未给出基线的具体名称与完整实验设置。

### 阅读优先级
高。理由：论文针对 LiDAR 导航中玻璃导致的碰撞边界缺失这一实际痛点，且同时关注漏检与自由空间污染的双重指标；提供了建筑尺度真实机器人数据上的覆盖率与假体素对比结果，对机器人导航、SLAM 与建图方向的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Transparent and specular surfaces pose a serious challenge to LiDAR-based SLAM and navigation because laser returns may pass through glass, leaving collision boundaries absent from the map. Prior work attempts to reconstruct the missing surfaces, but inaccurate obstacle placement can create the opposite failure: contamination of traversable free space. Recognizing this dual requirement, we present GlassGuard, a navigation-oriented framework for reconstructing planar architectural glass from complementary visual and LiDAR evidence. We formulate success in terms of both glass coverage and free-space contamination and apply this principle throughout proposal verification and global map construction. A foundation vision model provides glass-instance masks, structural 3D cues generate metric plane hypotheses, and depth-free 2D projective geometry checks their orientations before they enter a consolidated global map. We evaluate GlassGuard in nine building-scale scenes spanning diverse glass structures, spatial scales, and lighting conditions, with more than one hour and 2.1 km of real-world robot traversal. GlassGuard achieves 85% of total glass coverage for its panoramic version. Under identical pinhole inputs, GlassGuard achieves 82% total coverage, compared with at most 61% for the evaluated baselines, while producing 5-17x fewer false voxels per frame. Qualitative examples with a navigation planner illustrate the reconstructed planes blocking paths through glass while leaving traversable routes open. The project page is available at https://glassguardproject.github.io/.

</details>

#### 2026-10-01 - From Reasoning Failures to Composable Video Spatial Intelligence

**Authors:** Pengzhan Sun, Junbin Xiao, Ramanathan Rajaraman, Shiu-hong Kao, Angela Yao
**Links:** [abs](https://arxiv.org/abs/2610.01999) - [pdf](https://arxiv.org/pdf/2610.01999)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Reasoning Failures to Composable Video Spatial Intelligence
- 作者：Pengzhan Sun, Junbin Xiao, Ramanathan Rajaraman, Shiu-hong Kao, Angela Yao
- 出版日期：2026-10-01T16:31:19Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.01999 ；PDF https://arxiv.org/pdf/2610.01999

### 一句话总结
论文通过统一模式与坐标约定对比预测和真实空间上下文，将视频空间推理失败拆解为四类可诊断错误，并提出免训练的 CROSS 几何算子与空间技能库来显式处理空间约定，从而在多个基准上提升视觉语言模型的空间推理表现。

### 研究问题
论文关注的问题是：现有的空间推理基准虽然评估视觉语言模型在多种任务上的表现，但任务级分数无法揭示成功或失败背后的底层能力差异。作者认为每个任务都需要恢复空间证据、表示几何并进行推理，因此需要将空间推理能力解耦，诊断具体错误来源，并在此基础上修复系统性推理失败。

### 核心思路/方法
论文将空间推理拆解为若干底层能力：恢复空间证据、表示几何、以及在其上进行推理。作者通过在一个共享模式和坐标契约下比较预测的空间上下文与真实空间上下文，对失败进行诊断。该比较揭示出四类反复出现的错误来源：感知不准确、空间上下文信息缺失、选择错误的测量方式、以及参考系错误或位置与方向跟踪错误。

基于这一诊断，作者提出 CROSS，一个免训练的类型化几何算子与空间技能库。该库在可用证据上运行，以支持可靠的视频空间推理。CROSS 可以为非编程视觉语言模型提供经过验证的上下文，或为 SpatialClaw 智能体提供可调用的技能。论文在五个基准上评估 CROSS，摘要提到其在 ReVSI 上将平均分从 55.9% 提升至 60.2%，并将 DSI-Bench 上的 SpatialClaw 结果从 62.8% 提升至 66.3%。作者据此说明，显式处理空间约定可以在不额外训练的情况下修复系统性推理失败。

### 主要贡献
- 提出一种诊断视角：通过共享模式和坐标契约，对比预测与真实空间上下文，将视频空间推理失败归因于四类可复现错误来源。
- 提出 CROSS：一个免训练的、可组合的类型化几何算子与空间技能库，用于在可用证据上支持可靠的视频空间推理。
- 展示 CROSS 的两种使用方式：为非编程视觉语言模型提供经过验证的上下文，或为 SpatialClaw 智能体提供可调用技能。
- 在五个基准上进行评估，并报告在 ReVSI 和 DSI-Bench 上的具体提升，证明显式处理空间约定可修复系统性推理失败且无需额外训练。

### 局限性
摘要未提供足够信息说明 CROSS 的具体实现细节、算子覆盖范围、计算开销、失败案例、基准之外的泛化能力，以及四类错误来源之间的相互影响。摘要也未提供五个基准的完整名称与全部结果，仅报告了 ReVSI 和 DSI-Bench 上的部分数值。此外，摘要未说明该方法的适用边界或对输入证据质量的依赖程度。

### 阅读优先级
高。理由：论文针对视频空间推理中任务级评分无法解释失败原因的问题，提出可诊断的错误分类和免训练的可组合几何算子库，并在多个基准上报告一致提升。对于关注视觉语言模型空间推理、具身智能、机器人及 AR 应用的研究者而言，该工作提供了从失败诊断到可复用技能修复的明确路径，且不依赖额外训练，具有较强的实用性和可扩展性。

</details>

<details>
<summary>Abstract</summary>

Spatial reasoning benchmarks evaluate vision-language models across diverse tasks, but task-level scores do not reveal which underlying capabilities account for success or failure. Each task requires recovering spatial evidence, representing geometry, and reasoning over it. We disentangle these capabilities by comparing predicted and ground-truth spatial context under a shared schema and coordinate contract. This comparison reveals four recurring sources of error: inaccurate perception, missing information in the spatial context, selection of the wrong measurement, and errors in reference frames or in tracking position and orientation. Guided by this diagnosis, we develop CROSS, a training-free library of typed geometric operators and spatial skills that function over available evidence to support reliable video spatial reasoning. The resulting library supplies verified context to non-coding VLMs or callable skills to a SpatialClaw agent. We evaluate \methodname{} on five benchmarks. \methodname{} raises the average score from 55.9\% to 60.2\% on ReVSI and improves the SpatialClaw result from 62.8\% to 66.3\% on DSI-Bench. These gains demonstrate that explicit handling of spatial conventions can repair systematic reasoning failures without additional training.

</details>

#### 2026-10-01 - TouchTherm: Building Multimodal Digital Twins of Objects for Tactile and Thermal Rendering

**Authors:** Yitao Zhang, Hong Ying, Haoran Guo, Xiaoying Zhou, Guanyu Chen, Chenxi Xiao
**Links:** [abs](https://arxiv.org/abs/2610.01943) - [pdf](https://arxiv.org/pdf/2610.01943)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** rendering, VR, virtual reality, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TouchTherm: Building Multimodal Digital Twins of Objects for Tactile and Thermal Rendering
- 作者：Yitao Zhang, Hong Ying, Haoran Guo, Xiaoying Zhou, Guanyu Chen, Chenxi Xiao
- 出版日期：2026-10-01T16:10:08Z
- 分类：primary_category: Embodied / Robotics / AR Applications；secondary_categories: Neural Scene Representations & Rendering
- 链接：abstract_url: https://arxiv.org/abs/2610.01943；pdf_url: https://arxiv.org/pdf/2610.01943

### 一句话总结
TouchTherm 提出一个从真实物体构建可用于仿真的视觉—触觉—热觉多模态数字孪生资产的框架，以同时支持光学触觉渲染和随时间变化的温度反馈。

### 研究问题
机器人仿真和虚拟现实不仅需要物体的视觉几何与外观，还需要能够反映触觉与热觉交互的物理线索。现有 3D 数据集和重建方法主要表示物体尺度的几何与视觉外观，忽视了用于高保真触觉渲染的微观表面结构，以及用于温度感知交互的瞬态温度动态。因此，论文关注如何从真实物体构建同时具备视觉、触觉和热觉信息的仿真就绪资产。

### 核心思路/方法
论文提出 TouchTherm 框架，用于从真实世界物体构建仿真就绪的视觉—触觉—热觉物体资产。

在视觉与触觉重建方面，方法结合结构光扫描与从光度立体获得的多视角法线图。法线图被配准到扫描几何上，并转换到切线空间，以恢复用于光学触觉渲染的局部微观高度场；粗网格则用于碰撞检测。

在热觉重建方面，方法在受控加热后捕获自然冷却过程的同步多视角红外视频，并重建物理正则化的动态热场。

### 主要贡献
- 提出 TouchTherm 框架，从真实物体构建仿真就绪的视觉—触觉—热觉物体资产。
- 在视觉与触觉重建中，结合结构光扫描和光度立体的多视角法线图，将法线图配准到扫描几何并转换到切线空间，以恢复局部微观高度场，同时使用粗网格进行碰撞检测。
- 在热觉重建中，捕获受控加热后自然冷却的同步多视角红外视频，并重建物理正则化的动态热场。
- 在 20 个物体上的实验表明，重建的微观高度场保留主要表面结构，并恢复粗几何之外更高频的细节；热场在 30 秒和 45 秒时的留出表面温度 MAE 分别为 0.465 摄氏度和 0.592 摄氏度。
- 生成的触觉资产支持从触觉观测进行合成到真实的物体识别；基于手套的 VR 系统展示了空间和时间上变化的温度反馈。

### 局限性
摘要未提供足够信息。摘要未说明该方法在更广泛物体类别、复杂材质、不同环境条件或实时性能方面的限制，也未提供失败案例或与其他方法的完整定量比较。

### 阅读优先级
中。理由：该论文面向机器人仿真与 VR 中的多模态数字孪生，结合视觉、触觉和热觉重建，任务方向明确，并给出了 20 个物体上的热场 MAE 与触觉识别、VR 温度反馈演示；但摘要未提供足够信息来判断其方法细节、泛化能力、实时性和完整实验对比，因此对需要多模态物体资产或触觉/热觉仿真的读者具有一定价值，但优先级不宜直接判为最高。

</details>

<details>
<summary>Abstract</summary>

Robotic simulation and virtual reality increasingly require object assets that capture not only visual geometry but also the physical cues underlying tactile and thermal interaction. Existing 3D datasets and reconstruction methods primarily represent object-scale geometry and visual appearance, overlooking microscale surface structure for high-fidelity haptic rendering and transient temperature dynamics for temperature-aware interaction. We present TouchTherm, a framework for constructing simulation-ready visuo-tactile-thermal object assets from real-world objects. For visual and tactile reconstruction, we combine structured-light scanning with multiview normal maps obtained from photometric stereo. The normal maps are registered to the scanned geometry and transformed into tangent space to recover local micro-height fields for optical tactile rendering, while the coarse mesh handles collision detection. For thermal reconstruction, we capture synchronized multiview infrared videos of natural cooling following controlled heating and reconstruct a physics-regularized dynamic thermal field. Experiments on 20 objects show that the reconstructed micro-height fields preserve dominant surface structures and recover higher-frequency details beyond the coarse geometry, while the thermal fields achieve held-out surface-temperature MAEs of 0.465 degrees C and 0.592 degrees C at 30 s and 45 s, respectively. The resulting tactile assets support synthetic-to-real object recognition from tactile observations, while a glove-based VR system demonstrates spatially and temporally varying thermal feedback. These results highlight the potential of TouchTherm for multimodal sensory simulation and temperature-aware virtual interaction.

</details>

#### 2026-10-01 - Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models

**Authors:** Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis
**Links:** [abs](https://arxiv.org/abs/2610.01942) - [pdf](https://arxiv.org/pdf/2610.01942)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models
- 作者：Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis
- 出版日期：2026-10-01T16:09:34Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.01942) / [PDF](https://arxiv.org/pdf/2610.01942)

### 一句话总结
提出 Latent-Foresight，一个端到端联合学习潜在分词器与基于流的生成式动态模型的框架，显式塑造具备时间可预测性的潜在表示，以替代传统两阶段流水线。

### 研究问题
论文关注场景未来演化的预测这一世界建模的基础能力。现有工作虽已表明在视觉基础模型（VFM）的特征空间中操作可得到语义丰富的表示，但存在解耦问题：两阶段流水线先用固定降维（如 PCA）或独立训练的自编码器压缩 VFM 特征，再在冻结的潜在空间上训练单独的预测器；而直接在原始 VFM 特征上施加预测器的方法，也无法保证潜在空间是为可预测动态而组织的。

### 核心思路/方法
提出 Latent-Foresight 端到端框架，联合学习一个潜在分词器（latent tokenizer）和一个基于流的生成式动态模型，从而显式地将表示塑造成支持时间可预测性的形式。为实现稳定的联合优化，作者引入若干关键设计选择，以防止潜在坍塌（latent collapse），并使重建目标与生成目标对齐。

### 主要贡献
- 提出端到端框架 Latent-Foresight，联合学习潜在分词器与基于流的生成式动态模型，显式塑造可预测的潜在表示。
- 引入防止潜在坍塌、对齐重建与生成目标的关键设计，以支持稳定的联合优化。
- 据摘要所述，实验表明该方法学到的时间一致潜在表示更优，在多个未来场景理解任务和预测时间范围上持续优于两阶段基线，同时消除了分离的训练阶段（包括在高分辨率适配时）。
- 提供了实现代码与模型权重。

### 局限性
摘要未提供足够信息。例如未给出具体任务、数据集、评价指标、计算开销、失败案例或设计选择的具体细节，均无法从摘要判断。

### 阅读优先级
中。理由：该工作针对潜在世界模型表示学习与动态预测解耦这一明确问题，提出端到端方案且声称在多项任务上持续优于两阶段基线，思路有参考价值；但摘要未提供实验细节与定量结果，若关注世界模型或具身/机器人方向的表示学习，可进一步阅读原文验证；若仅需概览，可暂缓。

</details>

<details>
<summary>Abstract</summary>

Predicting the future evolution of a scene is a fundamental capability for world modeling. Recent work has shown that operating in the feature space of Vision Foundation Models (VFMs) yields semantically rich representations that support diverse future scene understanding tasks. However, existing approaches rely on two-stage pipelines, where VFM features are first compressed using fixed dimensionality reduction (e.g., PCA) or independently trained autoencoders, and a separate predictor is trained on top of the resulting frozen latent space. This decoupling between representation learning and temporal prediction, as well as approaches that apply predictors directly on raw VFM features, provides no guarantee that the latent space is structured for predictable dynamics. In this work, we propose Latent-Foresight, an end-to-end framework that jointly learns a latent tokenizer and a flow-based generative dynamics model, explicitly shaping the representation to support temporal predictability. To enable stable joint optimization, we introduce several key design choices that prevent latent collapse and align reconstruction with generative objectives. Extensive experiments show that our approach learns more temporally coherent latent representations and consistently outperforms two-stage baselines across multiple future scene understanding tasks and prediction horizons, while eliminating separate training stages, including during high-resolution adaptation. We provide the implementation code and model weights at https://github.com/Sta8is/Latent-Foresight

</details>

#### 2026-10-01 - FlashDexRetarget: Accelerating Dexterous Manipulation Data Generation through Multi-Motion Retargeting

**Authors:** Kyungmin Lee, Sibeen Kim, Dongyoon Hwang, Yoonsang Oh, Donghu Kim, Youngdo Lee, I Made Aswin Nahrendra, Jaegul Choo, Hojoon Lee
**Links:** [abs](https://arxiv.org/abs/2610.01849) - [pdf](https://arxiv.org/pdf/2610.01849)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FlashDexRetarget: Accelerating Dexterous Manipulation Data Generation through Multi-Motion Retargeting
- 作者：Kyungmin Lee, Sibeen Kim, Dongyoon Hwang, Yoonsang Oh, Donghu Kim, Youngdo Lee, I Made Aswin Nahrendra, Jaegul Choo, Hojoon Lee
- 出版日期：2026-10-01T15:15:42Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.01849

### 一句话总结
FlashDexRetarget 是一个基于强化学习的灵巧操作运动重定向框架，旨在提高人-物演示向机器人本体迁移的成功率与训练效率。

### 研究问题
人类手-物演示可作为可复用的灵巧机器人操作数据来源，但跨本体迁移需要物理可行的重定向。现有基于物理的方法在重定向成功率与特定运动的训练效率方面存在局限，或两者兼有。论文旨在解决高成功率与高效率难以兼顾的问题。

### 核心思路/方法
- 提出 FlashDexRetarget，一个基于 RL 的灵巧运动重定向框架。
- 为便于学习演示交互，结合物体点云观测、手-物距离特征、未来轨迹编码，并配合互补奖励来监督物体运动与参考手-物关系。
- 为加速学习，采用分离的左手和右手 actor-critic 网络，并将 off-policy 算法 FlashSAC 适配到灵巧运动跟踪任务。
- 在涵盖单物体与双物体交互的 50 个运动基准上进行评估；并在 200、500、1000 个运动规模下测试扩展性。

### 主要贡献
- 提出 FlashDexRetarget，用于高成功率、高效的灵巧运动重定向。
- 在 50 运动基准上达到 90% 成功率，约为所评估的基于采样基线的 2.5 倍，同时训练计算量比所评估的基于 RL 的基线最多少 100 倍。
- 在 XHand 与 Sharpa Wave Hand 上评估显示一致增益，并通过组件级消融考察各设计选择的贡献。
- 在 200、500、1000 运动规模下验证方法在大规模下仍保持稳定，并随训练集增长更高效地产生成功重定向运动。
- 使用真实世界采集演示的定性回放结果展示框架对录制人类操作的适用性。

### 局限性
- 摘要未提供足够信息关于失败案例、未覆盖的运动类型或具体计算资源规模。
- 摘要未提供足够信息关于真实机器人部署的定量结果与安全性评估。
- 摘要未提供足够信息关于方法对演示质量、物体类别或传感器噪声的敏感性分析。
- 摘要未提供足够信息关于与更多近期方法的完整对比范围。

### 阅读优先级
高。理由：该工作直接针对灵巧操作数据生成中的成功率与训练效率瓶颈，报告了显著的量化提升与大规模扩展验证，且涉及多本体一致性与真实演示回放，对具身智能与机器人操作数据生成方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Human hand-object demonstrations offer a reusable source of dexterous robot manipulation data, but transferring them across embodiments requires physically feasible retargeting. Existing physics-based approaches face limitations in retargeting success, motion-specific training efficiency, or both. To address these limitations, we introduce FlashDexRetarget, an RL-based framework for high-success, efficient dexterous motion retargeting. To make the demonstrated interaction easier to learn, we combine object point-cloud observations, hand-object distance features, and future trajectory encodings with complementary rewards that supervise object motion and reference hand-object relationships. To further accelerate learning, we employ separate left- and right-hand actor critic networks and adapt the off-policy algorithm, FlashSAC to dexterous motion tracking. On a benchmark of 50 motions spanning single-object and two-object interactions, FlashDexRetarget achieves a 90% success rate, approximately 2.5x that of the evaluated sampling-based baselines, while requiring up to 100x less training compute than the evaluated RL-based baselines. Evaluations on both XHand and Sharpa Wave Hand show consistent gains, and component-wise ablations examine the contributions of our design choices. Beyond the 50-motion benchmark, experiments with 200, 500, and 1,000 motions demonstrate that our method remains stable at larger scales and produces successful retargeted motions more efficiently as the training set grows. Qualitative replay results using real-world-captured demonstrations further illustrate the applicability of our framework to recorded human manipulation. Videos and code are available at https://davian-robotics.github.io/FlashDexRetarget/

</details>

#### 2026-10-01 - GIFTBench: Diagnosing Generalization in Image Forgery Localization and Informing Model Design

**Authors:** Baoke Dou, Ziye Wang, Hao Wang, Guoqing Cai, Wende Tan, Chenyang Si, Liucheng Guo, Yueming Lyu
**Links:** [abs](https://arxiv.org/abs/2610.01778) - [pdf](https://arxiv.org/pdf/2610.01778)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GIFTBench: Diagnosing Generalization in Image Forgery Localization and Informing Model Design
- 作者：Baoke Dou, Ziye Wang, Hao Wang, Guoqing Cai, Wende Tan, Chenyang Si, Liucheng Guo, Yueming Lyu
- 出版日期：2026-10-01T14:31:20Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次要分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.01778 ；PDF https://arxiv.org/pdf/2610.01778 ；数据集展示页 https://giftbench-preview.doudoudouya337.chatgpt.site

### 一句话总结
论文提出多轴图像伪造定位基准 GIFTBench，用于诊断模型在多种分布变化下的泛化能力，并基于诊断结果设计改进框架 ForenScope，同时将基准作为训练资源以提升跨域定位表现。

### 研究问题
现有图像伪造定位（IFL）评测基准常覆盖有限的篡改条件，或在跨数据集评测中混合多个因素，导致聚合性能无法完整反映模型在分布变化下的定位泛化能力。论文关注如何更可靠地评估 IFL 模型在多种变化条件下的泛化表现，并将诊断结果用于指导模型设计。

### 核心思路/方法
论文提出 GIFTBench，一个包含 115,013 张篡改图像、具有像素级标注的多轴基准，覆盖篡改来源、语义目标、编辑操作和组合复杂度四个维度，并支持轴特定迁移分析与在十二个外部数据集上的评测。基于该基准的诊断研究揭示了三类现象：跨来源迁移存在不对称性、失败以召回为主导、以及在语义/操作/组合变化下退化程度异质。除评测外，GIFTBench 的规模与多样性提供了比传统 IFL 数据集更广的训练分布，用于训练代表性定位器可提升对外部数据集的聚合迁移表现。受诊断发现指导，论文进一步提出 ForenScope，一个结合分类适配表示、多深度多尺度空间特征、学习式层融合以及选择性粗尺度条件化的检测与定位框架。

### 主要贡献
1. 提出 GIFTBench，一个覆盖多个篡改维度、包含 115,013 张像素级标注篡改图像的多轴 IFL 基准，支持轴特定迁移分析和十二个外部数据集评测。
2. 通过诊断研究揭示 IFL 泛化中的关键失败模式：跨来源迁移不对称、召回主导的失败、以及在不同语义/操作/组合变化下的异质退化。
3. 证明 GIFTBench 不仅可作为评测工具，也可作为有效训练资源：在其上训练代表性定位器能一致提升对外部数据集的聚合迁移表现。
4. 基于诊断发现提出 ForenScope 框架，融合分类适配表示、多深度多尺度空间特征、学习式层融合和选择性粗尺度条件化，在提升跨数据集定位的同时保留图像级检测能力。

### 局限性
摘要未提供足够信息。摘要中未说明 GIFTBench 的构建成本、标注一致性、潜在偏差、覆盖盲区，也未给出 ForenScope 的具体计算开销、失败案例或与现有方法的完整定量对比。论文所述“十二个外部数据集”的具体名称与评测协议细节，摘要未提供足够信息。分类标注为 Embodied / Robotics / AR Applications 与图像伪造定位主题之间的关系，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作同时涉及基准构建、泛化诊断和模型设计，对图像伪造定位与跨域泛化评测方向有直接参考价值；但摘要未提供具体实验数值、对比方法细节和局限性讨论，若需判断其相对现有基准的实际优势，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Reliable evaluation of image forgery localization (IFL) requires assessing models under diverse distribution changes, yet existing benchmarks often cover limited manipulation conditions or entangle multiple factors in cross-dataset evaluation. Consequently, aggregate performance provides an incomplete view of localization generalization. We introduce GIFTBench, a multi-axis benchmark of 115,013 manipulated images with pixel-level annotations spanning manipulation source, semantic target, editing operation, and composition complexity. GIFTBench supports axis-specific transfer analysis and evaluation on twelve external datasets. Its diagnostic studies reveal asymmetric cross-source transfer, recall-dominated failures, and heterogeneous degradation across semantic, operational, and compositional changes. Beyond diagnosis, the scale and diversity of GIFTBench provide a substantially broader training distribution than conventional IFL datasets. Training representative localizers on GIFTBench consistently improves their aggregate transfer to external datasets, showing that the benchmark serves not only as an evaluation tool but also as an effective training resource for cross-domain localization. Guided by the diagnostic findings, we further develop ForenScope, a detection and localization framework combining classification-adapted representations with multi-depth, multi-scale spatial features, learned layer fusion, and selective coarse-scale conditioning. Experiments show improved cross-dataset localization while retaining image-level detection capability. The GIFTBench dataset showcase page is available at https://giftbench-preview.doudoudouya337.chatgpt.site.

</details>

#### 2026-10-01 - EIDA: Execution-Interface Dynamics Adaptation for Real-to-Sim-to-Real Robot Navigation

**Authors:** Yiwei Qian, Shanze Wang, Qingyuan Hu, Xinming Zhang, Wei Zhang
**Links:** [abs](https://arxiv.org/abs/2610.01219) - [pdf](https://arxiv.org/pdf/2610.01219)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EIDA: Execution-Interface Dynamics Adaptation for Real-to-Sim-to-Real Robot Navigation
- 作者：Yiwei Qian, Shanze Wang, Qingyuan Hu, Xinming Zhang, Wei Zhang
- 出版日期：2026-10-01T07:24:32Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.01219 ；PDF：https://arxiv.org/pdf/2610.01219

### 一句话总结
EIDA 通过用目标平台执行数据拟合“执行接口”层面的动力学响应，并在轻量 GPU 并行仿真器中使用这些拟合模型，以改善真实到仿真再到真实的机器人导航迁移。

### 研究问题
仿真到机器人迁移可能失败，因为速度指令产生的运动与反馈不同于策略训练时建模的情况。论文关注的问题是如何在不重建执行器动力学的情况下，适配这种执行接口层面的差异，从而提升导航策略的迁移效果。

### 核心思路/方法
EIDA 不重建执行器动力学，而是从目标平台执行数据中拟合速度指令对应的响应。具体包括：一个模型预测机体坐标系下的位姿增量，用于更新仿真器几何；另一个单独模型预测策略所观察到的速度反馈；策略输入中包含一小段速度反馈历史。拟合后的模型被用于一个轻量级 GPU 并行仿真器中。

### 主要贡献
- 提出执行接口动力学适配方法 EIDA，用目标平台执行数据拟合速度指令响应，而不重建执行器动力学。
- 分别建模机体坐标系位姿增量以更新仿真器几何，以及策略面对的速度反馈预测，并将速度反馈短历史加入策略输入。
- 在 Jackal 和 Go2 完整验证集上，拟合模型相对仿真器预定义运动模型降低了位置和偏航预测误差。
- 在 100 个基准导航环境中、于独立物理仿真器评估时，EIDA 在有和没有全局引导的情况下均取得相比对比学习策略最高的成功率和导航分数。
- 反馈消融进一步支持匹配策略面对的速度估计的必要性。
- 在物理 Unitree Go2 上，EIDA 在全部 20 次静态场景试验中无碰撞到达目标，而基线为 20 次中 4 次。

### 局限性
摘要未提供足够信息。摘要未说明方法在动态场景、不同平台泛化、计算开销、失败案例或更广泛真实环境中的表现与限制。

### 阅读优先级
高。理由：论文直接针对 real-to-sim-to-real 机器人导航中的执行接口动力学适配问题，并同时给出仿真基准与物理机器人验证结果，且摘要报告了较明显的迁移性能提升，对机器人导航与仿真迁移方向具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Simulation-to-robot transfer can fail when velocity commands produce motion and feedback that differ from those modeled during policy training. We present execution-interface dynamics adaptation (EIDA), which fits these responses from target-platform execution data without reconstructing actuator dynamics. A model of body-frame pose increments updates simulator geometry, while a separate model predicts the velocity feedback observed by the policy; a short history of velocity feedback is included in the policy input. The fitted models are used within a lightweight GPU-parallel simulator. On the full Jackal and Go2 validation sets, the fitted models reduced position and yaw prediction errors relative to the simulator's predefined motion model. Across 100 benchmark navigation environments evaluated in a separate physics-based simulator, EIDA achieved the highest success rate and navigation score among the compared learned policies, both with and without global guidance. Feedback ablations further supported the need to match policy-facing velocity estimates. On a physical Unitree Go2, EIDA reached the goal without collision in all 20 static-scene trials, compared with 4 of 20 for the baseline. These results show that execution-interface adaptation can improve navigation transfer without detailed actuator simulation.

</details>

### 2026-09

#### 2026-09-30 - Harnessing Vision-Language Models for Perceptual Quality Assessment and Autonomous Content Adjustment in Augmented Reality

**Authors:** Elias Rotondo, Lin Duan, Yanming Xiu, Sangjun Eom, Conrad Li, Maria Gorlatova
**Links:** [abs](https://arxiv.org/abs/2610.00677) - [pdf](https://arxiv.org/pdf/2610.00677)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Harnessing Vision-Language Models for Perceptual Quality Assessment and Autonomous Content Adjustment in Augmented Reality
- 作者：Elias Rotondo, Lin Duan, Yanming Xiu, Sangjun Eom, Conrad Li, Maria Gorlatova
- 出版日期：2026-09-30T20:13:50Z
- 分类：主分类为 Embodied / Robotics / AR Applications；未提供次级分类
- 链接：[摘要](https://arxiv.org/abs/2610.00677)｜[PDF](https://arxiv.org/pdf/2610.00677)

### 一句话总结
论文提出一个基于视觉语言模型（VLM）的增强现实（AR）内容自动评估与调整框架，并构建 RateAR 基准，验证 VLM 质量预测与人类主观判断的相关性，进而实现自动化 AR 内容调整。

### 研究问题
AR 头戴显示设备面临场景几何受限、空间抖动和时间不稳定等问题，影响终端用户的沉浸感与舒适度。用户研究是 AR 视觉质量评估的标准方法，但其成本高、可扩展性下降且灵活性不足，成为迭代应用设计中的瓶颈。因此，论文关注如何用自动化方法评估和预测用户感知的 AR 场景视觉保真度，并进一步自动调整 AR 内容。

### 核心思路/方法
论文提出一个基于视觉语言模型的自动化 AR 内容评估与优化框架，用于评估和预测用户感知的 AR 场景视觉保真度。首先构建 RateAR 基准，包含在多样场景和环境条件下采集的 AR 图像与视频，并在对象放置、尺度、阴影一致性等感知因素上具有良好到优秀的可靠性（ICC(2,5) >= .90）。随后在 RateAR 上评估十一个商业 VLM，考察其质量预测与人类主观判断的相关性。论文还进行了消融研究，比较不同提示策略，指出上下文提示（contextual prompting）相比其他策略能更好地与人类评分对齐，同时平衡引入的复杂度线索。基于上述发现，论文构建了自动化 AR 内容调整系统，并开展了 21 名参与者参与的用户研究。

### 主要贡献
- 提出 RateAR 基准，涵盖多样场景与环境条件下的 AR 图像和视频，并针对对象放置、尺度、阴影一致性等感知因素报告了良好到优秀的可靠性（ICC(2,5) >= .90）。
- 在 RateAR 上评估十一个商业 VLM，结果表明基于 VLM 的质量预测与人类主观判断强相关，Spearman 秩相关最高达 0.8695。
- 通过消融研究显示，与其他提示策略相比，上下文提示在更好对齐人类评分的同时平衡了引入的复杂度线索。
- 构建自动化 AR 内容调整系统，并通过 21 名参与者的用户研究验证效果，超过 90% 的参与者认为系统改善了虚拟内容的放置和尺寸一致性。

### 局限性
摘要未提供足够信息。摘要未说明 RateAR 的规模、场景覆盖范围的具体边界、十一个商业 VLM 的具体名称、消融实验中各提示策略的详细设置、自动化调整系统的技术细节、用户研究的完整实验设计与统计细节，以及该方法在更广泛 AR 设备或任务上的泛化能力。上述内容均无法仅凭摘要确定。

### 阅读优先级
中。理由：该论文聚焦 AR 视觉质量评估与自动内容调整，将 VLM 用于感知质量预测并构建基准和用户研究，对 AR 应用、人机交互和视觉语言模型评估方向有参考价值；但摘要未提供足够信息说明具体方法细节、基准规模和系统实现，若读者关注可复现实验或具体技术方案，需要进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Advancements in augmented reality (AR) continue to foster innovative solutions, facilitating novel methodologies within educational systems, healthcare delivery, and risk-mitigation protocols. However, optimizing for end-user immersion and comfort remains challenging, as AR head-mounted displays contend with constrained scene geometry, spatial jitter, and temporal instability. User studies are the standard AR evaluation method for visual quality, but their cost, diminishing scalability, and inflexibility pose bottlenecks during iterative application design. To address this problem, we present an automated framework for AR content evaluation and refinement, built on vision-language models (VLMs), to evaluate and predict the visual fidelity of AR scenes as perceived by users. First, we introduce RateAR, a benchmark of AR images and videos collected across diverse scenes and environmental conditions, with good-to-excellent reliability (ICC(2,5) >= .90) across perceptual factors, including object placement, scale, and shadow consistency. Subsequently, we evaluate eleven commercial VLMs on the crafted benchmark. Results support that VLM-based quality predictions strongly correlate with human subjective judgments, achieving Spearman's rank-order correlations of up to 0.8695. An ablation study further suggests that, compared to other prompting strategies, our contextual prompting yields better alignment with human ratings while balancing introduced complexity cues. Building on these findings, we construct an automated AR content adjustment system and conduct a 21-participant user study. More than 90% of participants found that the system improved placement and size coherence of virtual content.

</details>

#### 2026-09-30 - KilometerVision: A New Frontier for Large-Scale Spatial Intelligence in VLMs

**Authors:** Aravindh Mahendran, Michael King, Matthew Koichi Grimes, Antoine Yang, Tyler Zhu, Joseph Heyward, Tengda Han, Shiry Ginosar, Chen Sun, Dima Damen, Simon Osindero, Noah Snavely, Simon Lynen, João Carreira, Viorica Pătrăucean
**Links:** [abs](https://arxiv.org/abs/2609.39588) - [pdf](https://arxiv.org/pdf/2609.39588)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KilometerVision: A New Frontier for Large-Scale Spatial Intelligence in VLMs
- 作者：Aravindh Mahendran, Michael King, Matthew Koichi Grimes, Antoine Yang, Tyler Zhu, Joseph Heyward, Tengda Han, Shiry Ginosar, Chen Sun, Dima Damen, Simon Osindero, Noah Snavely, Simon Lynen, João Carreira, Viorica Pătrăucean
- 出版日期：2026-09-30T12:14:26Z
- 分类：Embodied / Robotics / AR Applications（二级分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2609.39588 ；PDF https://arxiv.org/pdf/2609.39588 ；基准页面 https://perception-test-challenge.github.io/kilometervision.html

### 一句话总结
论文提出首个面向视觉语言模型（VLM）的大范围空间智能基准 KilometerVision，用真实视频探测最远约 1 公里的地理布局理解能力，并发现当前模型主要依赖二维视觉识别与文本匹配，而非真正的路径积分或几何测绘图式空间推理。

### 研究问题
如何在视觉语言模型上评估大规模空间智能，即模型能否从真实世界视频中理解地理布局，覆盖最远约 1 公里的距离尺度。论文进一步追问：当前 VLM 处理空间信息时，是否采用类似人类的层级化空间认知方式，还是以其他机制替代复杂空间推理。

### 核心思路/方法
- 构建并公开首个从真实世界视频出发、探测最远约 1 公里距离的地理布局理解基准。
- 借鉴认知科学文献，将评估对齐到人类空间意识的层级阶段：以地标进行锚定（anchoring via landmarks）、通过路线连接地标（connecting them through routes）、并整合为全局心理地图（integrating into global mental maps）。
- 在此基准上对当前 AI 模型开展大量实验，以观察其空间信息处理方式。

### 主要贡献
- 将 VLM 的大规模空间智能研究推向新前沿，提出 KilometerVision 基准。
- 提供首个基于真实视频、探测最远约 1 公里地理布局理解的基准。
- 提出与人类空间意识层级阶段对齐的评估框架：地标锚定、路线连接、全局心理地图整合。
- 通过实验揭示当前 AI 模型处理空间信息时的根本性分歧：VLM 几乎完全依赖二维视觉识别和文本匹配来绕过复杂空间推理，而不是使用真正的路径积分或形成几何测绘图式知识。
- 基准已公开。

### 局限性
- 论文仅提供摘要，具体实验设置、模型清单、数据集规模、评价指标、定量结果与消融分析等细节：摘要未提供足够信息。
- 基准所覆盖的距离上限约为 1 公里，更远尺度是否适用：摘要未提供足够信息。
- “主要依赖二维视觉识别和文本匹配”的结论所依据的具体证据与统计：摘要未提供足够信息。
- 与认知科学层级阶段的对应关系如何操作化、是否存在简化：摘要未提供足够信息。

### 阅读优先级
高。理由：该工作提出面向 VLM 大规模空间智能的新基准，并给出对当前模型空间推理机制的关键负面发现（依赖二维识别与文本匹配而非路径积分/测绘图式知识），对具身智能、机器人、AR 及 VLM 空间理解方向具有直接参考价值；同时基准公开，便于后续复现与对比。

</details>

<details>
<summary>Abstract</summary>

We push the frontier of large-scale spatial intelligence in Vision-Language Models (VLMs) and introduce the first benchmark that probes geographical layout understanding from real-world videos, spanning up to 1km distances. Inspired by the cognitive science literature, we evaluate models against the hierarchical stages of human spatial awareness: anchoring via landmarks, connecting them through routes, and integrating these into global mental maps. Extensive experiments reveal a fundamental divergence in how current AI models process spatial information. Instead of utilising true path integration or forming geometric survey knowledge, we find that VLMs rely almost entirely on 2D visual recognition and text-matching to bypass complex spatial reasoning. The benchmark is publicly available at https://perception-test-challenge.github.io/kilometervision.html.

</details>

#### 2026-09-30 - OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion

**Authors:** Ziheng Xu, Yueyuan Chen, Xinyuan He, Guoxing Liu, Yuanshuo Tan, Huiming Pan, Bin He, Shuo Jiang, Peter B. Shull
**Links:** [abs](https://arxiv.org/abs/2609.39017) - [pdf](https://arxiv.org/pdf/2609.39017)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OccluDex: Hierarchical 3D Visuo-Tactile Representation Learning for Egocentric Dexterous Manipulation under Self-Occlusion
- 作者：Ziheng Xu, Yueyuan Chen, Xinyuan He, Guoxing Liu, Yuanshuo Tan, Huiming Pan, Bin He, Shuo Jiang, Peter B. Shull
- 出版日期：2026-09-30T05:22:28Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.39017

### 一句话总结
OccluDex 提出一种分层 3D 视触觉表征学习框架，通过融合全局几何结构与局部接触信息，以应对第一人称灵巧操作中手部自遮挡带来的状态估计与泛化难题。

### 研究问题
在基于第一人称（egocentric）感知的灵巧操作中，正在操作的手会频繁遮挡与任务相关的物体表面和接触区域，导致可用于状态估计的视觉证据减少。这使得鲁棒的闭环控制以及对未见物体几何形状的泛化变得尤为困难。论文要解决的核心问题是：在手与物体交互并发生动态自遮挡的条件下，如何实现稳健的灵巧操作。

### 核心思路/方法
- 提出 OccluDex，一个分层的 3D 视触觉表征学习框架，将全局几何结构与局部接触信息相结合，用于动态自遮挡下的鲁棒操作。
- 采用多尺度掩码自编码（multi-scale masked autoencoding），逐步编码不完整的 3D 几何。
- 通过跨模态注意力（cross-modal attention），将触觉接触 token 与高层几何特征进行融合。
- 编码器先在同步的人类视触觉演示数据上进行预训练，之后作为冻结的感知骨干网络迁移至下游强化学习。
- 评估任务包括：水龙头旋转任务（需将手柄顺时针旋转一整圈）和桌面物体重定向任务（需将桌面物体翻转 180 度且不倾倒）。

### 主要贡献
- 提出 OccluDex 分层 3D 视触觉表征学习框架，整合全局几何结构与局部接触信息以应对动态自遮挡。
- 采用多尺度掩码自编码逐步编码部分 3D 几何，并通过跨模态注意力融合触觉接触 token 与高层几何特征。
- 编码器从同步的人类视触觉演示中预训练，并作为冻结感知骨干迁移到下游强化学习。
- 在仿真实验中，对未见物体的准确率比最强 SOTA 基线高 12.6%，对已见物体高 8.3%。
- 使用 Shadow Hand 进行物理实验，展示了对未见物理物体的零样本 sim-to-real 泛化能力。
- 摘要指出该结果有望使类人第一人称物体操作在已见和未见物体上均可行，即使操作机器手遮挡了视觉。

### 局限性
- 摘要未提供足够信息说明方法在更多任务类型或更大规模物体集合上的泛化表现。
- 摘要未提供足够信息说明预训练数据的具体规模、多样性及其对下游性能的影响。
- 摘要未提供足够信息说明失败案例、鲁棒性边界或对触觉传感器差异的敏感性。
- 摘要未提供足够信息说明计算成本、推理延迟或实时性表现。
- 摘要未提供足够信息说明与基线对比的完整实验设置或消融实验细节。

### 阅读优先级
高。理由：该论文针对第一人称灵巧操作中的自遮挡这一核心痛点，提出视触觉融合的分层表征学习方法，并结合预训练与强化学习，涉及仿真与真实 Shadow Hand 实验，报告了对未见/已见物体的准确率提升以及零样本 sim-to-real 泛化，问题重要且方法路径具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Reliable dexterous manipulation requires continuous estimation of object geometry and hand-object contact throughout interaction. With egocentric sensing, however, the manipulating hand frequently occludes task-relevant object surfaces and contact regions, reducing the visual evidence available for state estimation and thereby making robust closed-loop control and generalization to unseen object geometries particularly challenging. To address this, we present OccluDex, a hierarchical 3D visuo-tactile representation learning framework that integrates global geometric structure with local contact information for robust manipulation under dynamic self-occlusion during hand-object interaction. OccluDex adopts multi-scale masked autoencoding to progressively encode partial 3D geometry and fuses tactile contact tokens with high-level geometric features through cross-modal attention. The encoder is pretrained from synchronized human visuo-tactile demonstrations and transferred as a frozen perceptual backbone for downstream reinforcement learning. We evaluate OccluDex on a faucet rotation task, requiring one full clockwise handle revolution, and a tabletop object reorientation task, requiring a 180-degree tabletop object reorientation without toppling. In simulation experiments, OccluDex demonstrated 12.6% higher accuracy for unseen objects and 8.3% higher accuracy for previously seen objects than the strongest state-of-the-art baseline models. Physical experiments were further performed with a Shadow Hand to demonstrate successful zero-shot sim-to-real generalization on unseen physical objects. This results could enable humanoid egocentric object manipulation for seen and unseen objects even when the manipulating robotic hand occludes vision.

</details>

#### 2026-09-29 - FORM: Robot Manipulation through Direct Material Law Identification

**Authors:** Stepan Tretiakov, Ruihan Zhao, Cheng-Hsi Hsiao, Xingjian Li, Adam Thorpe, Hassan Iqbal, Sandeep Chinchali, Ufuk Topcu, Krishna Kumar
**Links:** [abs](https://arxiv.org/abs/2609.38105) - [pdf](https://arxiv.org/pdf/2609.38105)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FORM: Robot Manipulation through Direct Material Law Identification
- 作者：Stepan Tretiakov, Ruihan Zhao, Cheng-Hsi Hsiao, Xingjian Li, Adam Thorpe, Hassan Iqbal, Sandeep Chinchali, Ufuk Topcu, Krishna Kumar
- 出版日期：2026-09-29T17:46:40Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2609.38105) | [PDF](https://arxiv.org/pdf/2609.38105)

### 一句话总结
FORM 通过单次机器人交互，将观测到的材料运动与接触力转化为关于材料参数的线性方程，快速辨识材料属性并直接复用该模型规划新动作与新几何下的操作。

### 研究问题
机器人面对未知可变形材料时，缺乏其物理属性以及在外力与运动下响应方式的先验知识，因此需要快速在线辨识材料属性，才能实现可靠操作。论文关注的问题是：能否从单次机器人交互中快速辨识材料属性，并将恢复出的模型复用于新的动作和几何条件下的操作规划。

### 核心思路/方法
- 使用弱形式动量平衡，将观测到的材料运动与接触力转换为关于未知材料参数的线性方程。
- 这些方程采用与前向模拟器相同的物质点法（Material Point Method）离散方式组装，因此辨识问题退化为线性最小二乘求解。
- 求解结果可直接用于预测，无需重新拟合或格式转换。
- 在仿真和硬件上验证，覆盖四类材料与四类操作任务：弹性杆插入、弹性球杆高尔夫推杆、弹塑性塑形、目标体积倾倒。
- 在每类任务中，从单次交互辨识出的模型被复用于规划新运动或操作不同几何。

### 主要贡献
- 提出 FORM（From Observed Response to Material laws），实现从单次机器人交互辨识材料属性。
- 将辨识问题转化为线性最小二乘求解，使辨识时间从迭代基线的约 10–25 分钟降至 2–5 秒。
- 在四类材料上保持对新运动、初始条件和几何的竞争性精度。
- 在仿真与硬件上展示四类操作任务，并复用单次交互辨识的模型规划新动作或新几何操作。
- 报告了具体精度指标：弹性属性估计误差在 3.4% 以内，弹塑性属性在 2% 以内，面团塑形 IoU 为 72.4–77.8%，在 60–160 mL 目标体积下平均倾倒误差为 3.8 mL。

### 局限性
摘要未提供足够信息。（摘要未说明方法在未覆盖材料类别、极端几何变化、接触噪声或硬件条件变化下的表现，也未提供失败案例或计算资源需求的详细信息。）

### 阅读优先级
高。理由：该工作针对机器人操作未知可变形材料的关键在线辨识问题，提出将辨识转为线性最小二乘的明确技术路线，并同时给出仿真与硬件验证、四类任务及量化指标，方法快速且可复用，对可变形物体操作与材料属性辨识方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

When interacting with an unfamiliar deformable material, a robot lacks prior knowledge of its physical properties and how it will respond to applied forces and motion. Rapid online identification is therefore essential for reliable manipulation. We present FORM (From Observed Response to Material laws), which identifies material properties from a single robot interaction and reuses the recovered model to plan manipulation under new actions and geometries. We use weak-form momentum balance to convert observed material motion and contact forces into linear equations in the unknown material parameters. These equations are assembled using the same material point method discretization as the forward simulator, so identification reduces to linear least-squares solves whose solutions can be used directly for prediction without refitting or conversion. Across four material classes, FORM reduces identification time from roughly 10--25 minutes for iterative baselines to 2--5 seconds, while maintaining competitive accuracy on new motions, initial conditions, and geometries. We demonstrate our approach in simulation and on hardware across four manipulation tasks: elastic rod insertion, golf putting with an elastic club, elastoplastic shaping, and target-volume pouring. In each task, the model identified from a single interaction is reused to plan new motions or manipulate a different geometry. FORM estimates elastic properties within 3.4% and elastoplastic properties within 2%, achieves 72.4--77.8% IoU in dough shaping, and keeps mean pouring error at 3.8 mL across target volumes of 60--160 mL.

</details>

#### 2026-09-29 - Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy

**Authors:** Huan Rong, Chao Yin, Anouar Imel, Yijie Xia, Tinghuai Ma
**Links:** [abs](https://arxiv.org/abs/2609.38016) - [pdf](https://arxiv.org/pdf/2609.38016)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy
- 作者：Huan Rong, Chao Yin, Anouar Imel, Yijie Xia, Tinghuai Ma
- 出版日期：2026-09-29T17:01:29Z
- 分类：Embodied / Robotics / AR Applications（二级分类：摘要未提供足够信息）
- 链接：[摘要](https://arxiv.org/abs/2609.38016) / [PDF](https://arxiv.org/pdf/2609.38016)

### 一句话总结
本文提出 Brain-SAD——一个受大脑启发的安全自动驾驶控制框架，通过动态“恐惧”信号在线生成约束，并在常规交互策略与紧急碰撞防御策略之间进行双策略决策。

### 研究问题
现有约束强化学习（Constrained RL）方法在安全自动驾驶中缺乏约束的动态性：原始-对偶/软约束方法的动作代价通常是静态的状态到代价映射，硬约束方法的安全动作投影依赖于由离线示范估计的固定可行域边界。这种静态约束使约束与训练场景紧密耦合，导致策略因状态级动作代价不当和静态投影边界而难以应对不同的交互场景。

### 核心思路/方法
Brain-SAD 以“恐惧反应”为核心机制：通过感知当前车辆交互场景生成动态恐惧信号，据此刻画长期策略（用于常规交互）或短期策略（用于紧急碰撞防御）的双策略决策。恐惧反应被构造为动态恐惧约束，分别对应两种形式——与动作影响直接耦合的整体恐惧代价，以及由不同风险邻居推导出的动态可行域边界；二者反过来服务于在线策略优化。

### 主要贡献
- 提出 Brain-SAD，一个受大脑启发的安全自动驾驶控制框架，具备面向恐惧的动态约束。
- 感知当前车-交互场景后生成动态恐惧信号，在线决定采用常规交互的长期策略或紧急碰撞防御的短期策略。
- 在两种策略中，将恐惧反应分别构造为与动作影响耦合的整体恐惧代价，以及由不同风险邻居导出的动态可行域边界，用于在线策略优化。
- 实验结果显示 Brain-SAD 优于现有方法，在更短的任务完成与碰撞恢复时间内取得更高成功率，并在复杂度波动的连续交叉口中表现出更强的可靠性。

### 局限性
- 摘要未提供足够信息说明具体实验平台、数据集、基线方法与评价指标细节。
- 摘要未提供足够信息说明“恐惧信号”的具体建模方式、参数设置及其计算开销。
- 摘要未提供足够信息说明该方法在真实车辆或仅仿真环境中的验证情况。
- 摘要未提供足够信息说明双策略切换的稳定性与失效条件。

### 阅读优先级
中。理由：该工作针对约束强化学习中约束静态化这一具体不足提出动态恐惧约束与双策略框架，问题定位明确，且有实验对比结果支撑；但摘要未披露实验设置、实现细节与真实场景验证情况，需进一步阅读原文才能判断方法可复现性与实际适用边界。

</details>

<details>
<summary>Abstract</summary>

Constrained Reinforcement Learning has recently gained increasing attention in the field of Safe Autonomous Driving, where the general mechanism is to maximize the expected reward while keeping the overall action risk bounded. In this way, the safety issues arising in AD can be mitigated through constrained actions. However, existing Constrained RL methods still lack dynamics on the imposed constraints. For instance, the action cost adopted by the existing Primal-Dual/soft-constrained methods is often defined as static state-to-cost mapping, and the safe-action projection in hard-constrained methods relies on the static projection with the fixed feasible region boundary estimated from offline demonstrations. The above drawback tightly couples the imposed constraints to the training scenarios, leaving the AD policy hard to handle different interaction scenarios, due to the improper state-level action-cost and the static projection boundary. Consequently, in this paper, we propose Brain-SAD, a brain-inspired safe autonomous driving control framework with dynamic fear-oriented constraints. By perceiving the current vehicle-interaction scene, Brain-SAD generates dynamic fear signal as fear reaction to online decide long-term policy for regular interaction or short-term policy for urgent-collision defense. In such two policy, the above fear-reaction will be constructed as the dynamic fear constraints, respectively reflecting the overall fear cost directly coupled with action-impact, and the dynamic fear boundary of the feasible region derived from different risky neighbors, both of which will in turn serve for the online policy optimization. Experimental results show that Brain-SAD outperforms existing methods, achieving higher success rate in shorter task-completion and collision-recovery time, and exhibits stronger reliability across continuous intersections of fluctuating complexity.

</details>

#### 2026-09-29 - Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding

**Authors:** Jiayu Ying, Qijian Tian, Ruijie Xu, Xinnan Zhu, Daoguo Dong, Jiachen Xu, Xin Tan
**Links:** [abs](https://arxiv.org/abs/2609.37655) - [pdf](https://arxiv.org/pdf/2609.37655)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding
- 作者：Jiayu Ying, Qijian Tian, Ruijie Xu, Xinnan Zhu, Daoguo Dong, Jiachen Xu, Xin Tan
- 出版日期：2026-09-29T14:17:49Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2609.37655 ；PDF https://arxiv.org/pdf/2609.37655

### 一句话总结
Exemplar2VQA 是一个以示例为驱动、通过多智能体编码在仿真环境中快速合成大规模空间问答数据的可扩展框架，用以缓解 MLLM 空间智能训练数据稀缺的问题。

### 研究问题
多模态大语言模型（MLLM）在空间智能上的推进受限于复杂、可扩展的 3D 问答（QA）数据稀缺。人工标注成本高，而直接用 LLM 合成 QA 对往往因其在空间与几何计算上的固有不足而失败。

### 核心思路/方法
提出 Exemplar2VQA，一个可扩展的、示例驱动的 VQA 生成框架，通过多智能体编码在仿真环境中快速合成大规模空间 QA 对。其核心做法是：为协作的智能体配备精心设计的几何工具库，以确定性代码执行的方式绕开 LLM 在空间推理上的缺陷。框架具有通用性：以多样化的、以静态物体为中心的空间查询模板作为示例，可无缝、自主地将其扩展为大规模、高保真的合成数据集。

### 主要贡献
- 提出 Exemplar2VQA 框架，通过多智能体编码与几何工具库的确定性代码执行，规避 LLM 空间推理缺陷，实现大规模空间 QA 对合成。
- 框架具备通用性，可将多样化的静态物体中心空间查询模板作为示例，自主扩展为大规模高保真合成数据集。
- 仅使用 Exemplar2VQA 生成的合成室内数据微调 Qwen2.5-VL（3B/7B），在多个不同基准上取得显著性能提升。
- 效果不限于域内室内数据集，还能稳健扩展到室外和混合场景基准；作者据此提出 Exemplar2VQA 是弥合具身 AI 中 sim-to-real 差距的可扩展范式。
- 代码已公开于 https://github.com/yingjiayu12/Exemplar2VQA 。

### 局限性
- 摘要未提供足够信息说明具体实验设置、基准名称、评测指标与提升幅度。
- 摘要未提供足够信息说明几何工具库的具体构成、多智能体协作机制细节及模板设计方式。
- 摘要未提供足够信息说明合成数据的规模、质量评估方式与潜在失败案例。
- 摘要未提供足够信息说明方法在更广泛任务类型或真实数据上的泛化边界与成本开销。

### 阅读优先级
高。理由是：该工作针对具身 AI 与 MLLM 空间智能中的关键数据瓶颈，提出可扩展的自动化数据生成范式，并报告了跨室内、室外与混合场景基准的性能提升，属于数据生成与空间推理交叉方向的重要进展；同时代码开源，便于复现与后续研究。

</details>

<details>
<summary>Abstract</summary>

Advancing spatial intelligence in Multimodal Large Language Models (MLLMs) is bottlenecked by the scarcity of complex, scalable 3D question-answer (QA) data. While manual annotation is labor-intensive, directly utilizing LLMs to synthesize these QA pairs often fails due to their inherent deficiencies in spatial and geometric computation. We introduce Exemplar2VQA, a scalable exemplar-driven visual question answering generation framework that rapidly synthesizes large-scale spatial QA pairs in simulated environments via multi-agent coding. By equipping collaborative agents with a meticulously designed library of geometric utilities, Exemplar2VQA bypasses LLMs' spatial reasoning flaws through deterministic code execution. Crucially, the framework exhibits remarkable versatility: taking diverse static object-centric spatial query templates as exemplars, it seamlessly and autonomously scales them into massive, high-fidelity synthetic datasets. Fine-tuning Qwen2.5-VL (3B/7B) exclusively on Exemplar2VQA-generated synthetic indoor data yields significant performance improvements across various diverse benchmarks. Furthermore, its effectiveness is not limited to in-domain indoor datasets but also robustly extends to outdoor and mixed-scene benchmarks. These results establish Exemplar2VQA as a scalable and powerful paradigm for bridging the sim-to-real gap in Embodied AI. Our code is at https://github.com/yingjiayu12/Exemplar2VQA

</details>

#### 2026-09-29 - VidAct: Learning Manipulation from In-the-Wild Videos with Object-Centric 3D Awareness

**Authors:** Hang Li, Mingxin Zhang, Zihan Wu, Yang Tian, Dong Chen, Fengyi Shen, Yuan Meng, Xiangtong Yao, Heng Zhang, Ziyuan Liu, Zhenshan Bing, Alois Knoll
**Links:** [abs](https://arxiv.org/abs/2609.36870) - [pdf](https://arxiv.org/pdf/2609.36870)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VidAct: Learning Manipulation from In-the-Wild Videos with Object-Centric 3D Awareness
- 作者：Hang Li, Mingxin Zhang, Zihan Wu, Yang Tian, Dong Chen, Fengyi Shen, Yuan Meng, Xiangtong Yao, Heng Zhang, Ziyuan Liu, Zhenshan Bing, Alois Knoll
- 出版日期：2026-09-29T07:08:36Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2609.36870，PDF https://arxiv.org/pdf/2609.36870

### 一句话总结
VidAct 提出一种从每个任务单目视频中学习以物体为中心、具备 3D 感知的机器人操作策略的视频到机器人框架，并支持零样本真实世界部署。

### 研究问题
论文关注从视频演示中学习机器人操作的问题。摘要指出，现有基于重建的方法通常依赖受限的相机视角或人到机器人的重定向，且重建出的轨迹难以适应新的物体配置而不扭曲轨迹形状；另一个关键局限是所得策略往往缺乏精确的物体级 3D 几何感知，限制了物体 grounding 和物体形状感知，而这对精确操作至关重要。

### 核心思路/方法
VidAct 是一个高效的 video-to-robot 框架，能够从每个任务单目视频中学习以物体为中心、3D 感知的操作策略，并实现零样本真实世界部署。其方法包含三个关键组件：
1. 从任意演示视频中重建物体网格与运动，并将运动在静态物体坐标系中规范化，从而避免特定本体的重定向，并能适应多样相机视角。
2. 采用残差轨迹迁移，将重建运动适配到新的物体配置，同时保持其运动形状。
3. 作为关键策略学习组件，VidAct 在每一帧预测由仿真提供的特权完整物体点云作为辅助任务，同时保留仅 RGB 部署，从而对物体位姿和 3D 几何提供密集的以物体为中心的监督。

### 主要贡献
摘要声明的主要贡献包括：
- 提出 VidAct，一个从每个任务单目视频中学习以物体为中心、3D 感知操作策略的高效 video-to-robot 框架，并支持零样本真实世界部署。
- 通过重建物体网格与运动，并在静态物体坐标系中规范化运动，避免 embodiment-specific retargeting，同时适应多样相机视角。
- 提出残差轨迹迁移，用于将重建运动适配到新物体配置并保持运动形状。
- 在策略学习中引入逐帧完整物体点云预测作为辅助任务，在仅 RGB 部署条件下提供对物体位姿和 3D 几何的密集物体中心监督。
- 在人类、机器人、生成和互联网视频上的实验表明广泛的视频适用性和零样本部署；逐帧完整物体 3D 监督提升了策略泛化与 sim-to-real 成功率，残差轨迹迁移实现了可靠的轨迹适配并更好地保持形状。

### 局限性
摘要未提供足够信息说明方法的明确局限性。摘要仅报告了实验覆盖人类、机器人、生成和互联网视频，以及零样本部署和 sim-to-real 成功等结果，但未给出失败案例、适用边界、计算成本或对特定条件的依赖等细节。

### 阅读优先级
高。理由：该论文聚焦从野外视频学习机器人操作，并同时处理相机视角、轨迹适配和物体级 3D 感知等摘要中明确指出的关键问题；其提出的物体中心 3D 监督、残差轨迹迁移和零样本真实世界部署在具身智能与机器人操作方向具有较强相关性，且摘要报告了多类型视频上的实验验证。

</details>

<details>
<summary>Abstract</summary>

Video demonstrations offer a scalable alternative to costly robot data for learning manipulation, yet existing reconstruction-based approaches often rely on constrained camera viewpoints or human-to-robot retargeting, while the reconstructed trajectories are difficult to adapt to new objects configurations without distorting the trajectory shape. Another key limitation is that the resulting policies often lack precise object-level 3D geometry awareness, limiting object grounding and object shape awareness critical for precise manipulation. To bridge these gaps, we propose VidAct, an efficient video-to-robot framework that learns object-centric, 3D-aware manipulation policies from a single monocular video per task and enables zero-shot real-world deployment. VidAct consists of three key components. First, VidAct reconstructs object meshes and motion from arbitrary demo videos and canonicalizes the motion in the static object frame, avoiding embodiment-specific retargeting and accommodating diverse camera viewpoints. Second, VidAct employ residual trajectory transfer for adapting the reconstructed motion to novel object configurations while preserving its motion shape. Finally, as the key policy-learning component, VidAct predicts simulation-provided privileged complete-object point clouds at each frame as an auxiliary task while retaining RGB-only deployment, providing dense object-centric supervision over both object pose and 3D geometry. Experiments on human, robot, generated, and internet videos demonstrate broad video applicability and zero-shot deployment. Per-frame complete-object 3D supervision improves policy generalization and sim-to-real success, while residual trajectory transfer enables reliable trajectory adaptation with better shape preservation.

</details>

#### 2026-09-29 - Foundation-Model-Guided Topology-Aware Semantic Risk Fields for Manipulation

**Authors:** Giung Lee, Weihang Guo, Lydia E. Kavraki
**Links:** [abs](https://arxiv.org/abs/2609.36640) - [pdf](https://arxiv.org/pdf/2609.36640)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Foundation-Model-Guided Topology-Aware Semantic Risk Fields for Manipulation
- 作者：Giung Lee, Weihang Guo, Lydia E. Kavraki
- 出版日期：2026-09-29T03:46:07Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2609.36640 ；PDF https://arxiv.org/pdf/2609.36640

### 一句话总结
提出一种由基础模型引导、具备拓扑感知能力的语义风险场，将被操作物体与场景物体之间的语义风险转化为可用于下游运动规划的稠密三维代价表示，从而在满足几何约束的同时降低语义暴露。

### 研究问题
日常环境中的机器人运动规划不仅要满足硬性几何约束，还需要考虑依赖上下文的语义风险。论文关注的问题是如何把语义风险纳入操作规划，使安全不再局限于避碰，而是在存在障碍物（包括完整与部分屏障）的情况下仍能保持拓扑感知的语义风险规避。

### 核心思路/方法
- 对每一个“被操作物体 / 场景物体”配对，使用基础模型提供六个方向性风险权重以及该配对特有的空间衰减尺度。
- 将这些先验与体素化的三维场景几何结合，使用拓扑感知屏蔽（topology-aware shielding）与测地空间衰减（geodesic spatial decay）进行融合。
- 通过 GPU 并行后端批量计算物体级距离与风险，构建稠密三维风险场。
- 该风险场作为模块化代价，供下游运动规划使用。

### 主要贡献
- 提出基础模型引导、拓扑感知的语义风险场，将操作安全从单纯避碰扩展到语义风险层面。
- 设计结合方向性风险权重、配对特定空间衰减、拓扑感知屏蔽与测地衰减的场构造方法。
- 实现 GPU 并行后端以批量计算物体级距离与风险，构建稠密三维场，并作为模块化代价接入运动规划。
- 在完整与部分屏障条件下评估屏蔽行为，并将三维工作空间表示与逐像素语义先验基线进行比较。
- 在三个家庭仿真场景中，相同几何约束下，使用该风险场优化的轨迹比仅考虑碰撞的轨迹具有更低的语义暴露；同时评估了支撑流程的计算实用性与可靠性。

### 局限性
- 摘要未提供足够信息说明真实机器人实验情况，评估仅限于三个家庭仿真场景。
- 摘要未提供足够信息说明基础模型的具体类型、风险权重的获取方式及其可靠性验证细节。
- 摘要未提供足够信息说明与逐像素语义先验基线比较的定量指标与完整结果。
- 摘要未提供足够信息说明拓扑感知屏蔽在更复杂拓扑环境下的适用边界与失效条件。
- 摘要未提供足够信息说明计算性能的具体数值、实时性水平及硬件依赖程度。

### 阅读优先级
高。理由：该工作将基础模型先验、拓扑感知与语义风险场结合，并接入下游运动规划，问题定位清晰且对操作安全有直接意义；摘要同时给出仿真验证与计算实用性评估，适合关注机器人操作规划、语义安全与基础模型具身应用的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Robot motion planning in everyday environments must satisfy hard geometric constraints while accounting for context-dependent semantic risk. We present a foundation-model-guided, topology-aware semantic risk field that extends manipulation safety beyond collision avoidance. For each manipulated-object/scene-object pair, a foundation model provides six directional risk weights and a pair-specific spatial decay scale. The method combines these priors with voxelized 3D scene geometry using topology-aware shielding and geodesic spatial decay. A GPU-parallel backend batches object-level distance and risk computations to construct a dense 3D field that serves as a modular cost for downstream motion planning. We evaluate the field's shielding behavior under full and partial barriers and compare its 3D workspace representation with a pixel-wise semantic-prior baseline. Across three household simulation scenarios, trajectories optimized with the proposed field have lower semantic exposure than collision-only trajectories under the same geometric constraints. We also evaluate the computational practicality and reliability of the supporting pipeline. Together, these results support the proposed field as a practical topology-aware semantic cost representation for manipulation planning beyond collision avoidance.

</details>

#### 2026-09-28 - ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning

**Authors:** Ke Fang, Yupu Yao, Lu Cheng
**Links:** [abs](https://arxiv.org/abs/2609.36333) - [pdf](https://arxiv.org/pdf/2609.36333)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning
- 作者：Ke Fang, Yupu Yao, Lu Cheng
- 出版日期：2026-09-28T22:09:55Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：[摘要](https://arxiv.org/abs/2609.36333) ｜ [PDF](https://arxiv.org/pdf/2609.36333) ｜ 代码：https://anonymous.4open.science/r/atlas-world-model-72C4/

### 一句话总结
ATLAS 提出一种训练目标，在将编码器表示变换到规划器所用潜空间时，同时保留成对关系几何（relational geometry）并校准全局潜分布，以提升世界模型规划的可靠性，尤其在更新颖（higher-novelty）的评估子集上增益更大。

### 研究问题
- 潜世界模型（latent world models）依赖表示几何进行规划，但仅正则化潜边际（latent marginal）无法决定用于动作选择的状态到状态关系。
- 摘要指出：这可能导致与规划相关的新颖性结构（planning-relevant novelty structure）在表示被变换为规划器最终使用的潜变量时被削弱。
- 因此核心问题是：如何在变换过程中保留规划所依赖的关系结构，同时保持全局潜分布的校准。

### 核心思路/方法
- 提出训练目标 ATLAS（Aligned Transport of Latent Structure）。
- 它显式保留关系几何，同时校准全局潜分布。
- 具体做法：
  - 从信息量较高的编码器表示中提取归一化的成对结构（normalized pairwise structure），并将其传输到规划潜空间；
  - 使用 Wasserstein 嵌入匹配（WEMReg），通过一维 Wasserstein-2 传输来校准潜边际分布。
- 分析层面：摘要称关系保留与边际校准构成非冗余约束，并将有限候选规划稳定性与关系失真、潜尺度不匹配、预测误差联系起来。
- 实现层面：ATLAS 实例化于 LeWM 中。

### 主要贡献
- 提出 ATLAS 训练目标，在潜表示变换中同时保留成对关系结构并校准边际分布。
- 给出分析：关系保留与边际校准提供非冗余约束，并将有限候选规划稳定性与关系失真、潜尺度不匹配、预测误差关联。
- 在 LeWM 中实例化 ATLAS，并在 PushT、TwoRoom、OGBench-Cube 上、在较低与较高新颖性评估子集上均提升平均目标达成成功率；其中在较高新颖性的 TwoRoom 片段上增益最大。
- 表示与 rollout 诊断显示：规划潜空间中与新颖性相关的结构更强、边际校准更好、多步预测误差更低。
- 结论强调：保留与规划相关的潜几何是可靠世界模型规划的重要要素。代码已（匿名）提供。

### 局限性
- 摘要未提供足够信息说明方法的计算开销或可扩展性边界。
- 摘要未提供足够信息说明在更广泛任务、真实机器人场景或不同世界模型骨干上的泛化性。
- 摘要未提供足够信息说明超参数敏感性、消融细节及失败案例。
- 摘要未提供足够信息说明与哪些具体基线方法的完整对比结果。
- 摘要未提供足够信息说明次分类归属与完整实验设置细节。

### 阅读优先级
- 高。
- 理由：该工作直面潜世界模型规划中“仅正则化边际不足”的关键表示几何问题，提出明确可操作的目标并在多个基准与新颖性子集上报告增益，且摘要给出与规划稳定性相关的分析框架；对具身智能、机器人规划与世界模型表示学习方向的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Latent world models rely on representation geometry for planning, yet regularizing the latent marginal alone does not determine the state-to-state relationships used for action selection. We show that this can cause planning-relevant novelty structure to be weakened as representations are transformed into the final latent used by the planner. We introduce Aligned Transport of Latent Structure (ATLAS), a training objective that explicitly preserves relational geometry while calibrating the global latent distribution. ATLAS transfers normalized pairwise structure from an informative encoder representation to the planning latent and uses Wasserstein embedding matching (WEMReg) to calibrate its marginal through one-dimensional Wasserstein-2 transport. Our analysis shows that relational preservation and marginal calibration impose non-redundant constraints, and connects finite-candidate planning stability to relational distortion, latent-scale mismatch, and prediction error. Instantiated in LeWM, ATLAS improves mean goal-reaching success across PushT, TwoRoom, and OGBench-Cube on both lower- and higher-novelty evaluation subsets, with the largest gain on higher-novelty TwoRoom episodes. Representation and rollout diagnostics further show stronger novelty-related structure in the planning latent, improved marginal calibration, and lower multi-step prediction error. Together, these results highlight preservation of planning-relevant latent geometry as an important ingredient for reliable world-model planning. Code is available at https://anonymous.4open.science/r/atlas-world-model-72C4/.

</details>

#### 2026-09-28 - Terrain-Aware Autonomous Planetary Exploration for Exteroceptive-Proprioceptive Mapping with Quadruped Scouts

**Authors:** Alberto Sanchez-Delgado, João Carlos Virgolino Soares, Victor Barasuol, Claudio Semini
**Links:** [abs](https://arxiv.org/abs/2609.35493) - [pdf](https://arxiv.org/pdf/2609.35493)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Terrain-Aware Autonomous Planetary Exploration for Exteroceptive-Proprioceptive Mapping with Quadruped Scouts
- 作者：Alberto Sanchez-Delgado, João Carlos Virgolino Soares, Victor Barasuol, Claudio Semini
- 出版日期：2026-09-28T16:01:24Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2609.35493) / [PDF](https://arxiv.org/pdf/2609.35493)

### 一句话总结
该论文提出一种面向四足侦察机器人的地形感知自主探索框架，在外星类似月球环境中融合外部感知与本体感知建图，用于规划兼顾碰撞规避与地形交互成本的自主探索与导航。

### 研究问题
论文关注的是自主行星探索场景下，机器人如何在未知、崎岖地形中导航，同时评估风险、可通行性与能量代价。四足侦察机器人适合此类任务，因为其能穿越不规则表面并在运动过程中收集与移动性相关的信息。因此，核心问题是如何将外部感知的几何信息与本体感知的地形交互信息结合，支持自主探索与后续导航。

### 核心思路/方法
论文提出一个地形感知探索框架，结合外部感知与本体感知建图，面向类似月球环境中的四足机器人。具体而言：
- 机载 RGB-D 相机构建以机器人为中心的高程图，估计几何可通行性，并推导用于自主规划的导航代价。
- 本体感知测量提供交互感知的地形线索，补充基于几何的评估。
- 局部地图被增量配准到全局多层表示中，探索模块利用该表示在未探索的兴趣区域中选择目标。
- 自主导航系统利用可用的地图与代价层，引导碰撞感知的运动到达目标。

### 主要贡献
- 提出融合外部感知与本体感知的 terrain-aware 探索框架，用于四足机器人在月球类似环境中的自主探索。
- 构建机器人中心高程图，估计几何可通行性并推导导航代价，同时利用本体感知提供交互感知地形线索。
- 将局部地图增量配准为全局多层表示，并用于在未探索兴趣区域中选择探索目标。
- 在 NVIDIA Isaac Sim 中进行仿真，展示自主探索、地图扩展以及地形几何与机器人—地形交互之间的空间关联。
- 使用该信息进行后续导航时，平均运输成本（Cost of Transport, CoT）低于初始探索阶段。

### 局限性
摘要未提供足够信息说明以下方面：真实世界实验验证情况、不同地形或环境条件下的泛化能力、与已有方法的定量对比、计算资源与实时性表现、失败案例或方法适用边界。因此，无法仅根据摘要评估这些潜在局限。

### 阅读优先级
高。理由：该论文聚焦四足机器人在行星探索中的自主探索与地形感知建图，明确结合外部感知与本体感知，并涉及多层地图、可通行性代价与运输成本等关键机器人自主导航问题；摘要给出了较完整的方法框架与仿真验证结果，对相关方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous planetary exploration requires robots to navigate unknown, uneven terrain while assessing risk, traversability, and energetic cost. Quadruped scouts are well suited for this task because they can traverse irregular surfaces and gather mobility-relevant information during locomotion. This paper presents a terrain-aware exploration framework that combines exteroceptive and proprioceptive mapping for a quadruped robot in lunar-like environments. An onboard RGB-D camera builds robot-centered elevation maps, estimates geometric traversability, and derives navigation costs for autonomous planning. In parallel, proprioceptive measurements provide interaction-aware terrain cues that complement geometry-based assessment. Local maps are incrementally registered into a global multi-layer representation, which is used by an exploration module to select targets in unexplored regions of interest. The targets are reached by an autonomous navigation system that guides collision-aware motion using the available map and cost layers. Simulation results on NVIDIA Isaac Sim show autonomous exploration, map expansion, and spatial association between terrain geometry and robot-terrain interaction. Subsequent navigation using this information exhibits lower average Cost of Transport (CoT) than initial exploration.

</details>

#### 2026-09-28 - DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library

**Authors:** Youhui Wang, Yunzhu Li, Li Fei-Fei, Jiajun Wu, Huang Huang
**Links:** [abs](https://arxiv.org/abs/2609.35318) - [pdf](https://arxiv.org/pdf/2609.35318)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library
- 作者：Youhui Wang, Yunzhu Li, Li Fei-Fei, Jiajun Wu, Huang Huang
- 出版日期：2026-09-28T14:49:06Z
- 分类：Embodied / Robotics / AR Applications（主要分类；次要分类未提供）
- 链接：[摘要](https://arxiv.org/abs/2609.35318) / [PDF](https://arxiv.org/pdf/2609.35318)

### 一句话总结
DexAgent 是一个智能体式的 Human2Sim2Robot 框架，可将单段第一视角人类视频与任务提示转化为物理合理的机器人轨迹，并通过自进化工具库与验证反馈机制支持多样化物体和长时程任务。

### 研究问题
现有的人类到仿真再到机器人（Human2Sim2Robot）流水线依赖预定义流程，难以适应多样化的物体属性和交互方式，尤其是涉及铰接物体和可变形物体的情形。论文旨在解决：如何从单段第一视角人类视频出发，自动生成物理合理、可迁移至真实机器人的灵巧操作轨迹，并应对不同物体属性与长时程任务。

### 核心思路/方法
DexAgent 是一个智能体式框架，输入为单段第一视角人类视频和任务提示，输出为可用于策略训练的、物理合理的机器人轨迹。框架包含四个阶段：
1. 人类视频的语义理解；
2. 基于物体属性的仿真重建；
3. 机器人轨迹优化；
4. 机器人数据生成。

在每个阶段，DexAgent 会根据任务与物体属性，从工具库中选择合适技能，或在需要时开发新技能。属性特定的验证器评估各阶段结果是否满足物理有效性与任务特定要求，并给出反馈用于细化，从而防止错误在工作流中传播。在最后阶段，DexAgent 在仿真中改变物体与机器人状态，从单段人类视频生成多样化机器人轨迹，并对渲染观测进行重纹理化以促进仿真到真实的迁移。新开发的技能与验证器会保留在工具库中，使框架具备自进化能力，可积累可复用能力；随着处理更多人类视频，处理时间会减少。

### 主要贡献
- 提出 DexAgent，一个智能体式 Human2Sim2Robot 框架，将单段第一视角人类视频与任务提示转化为物理合理的机器人轨迹，用于策略训练。
- 设计四阶段流程，并通过属性特定验证器提供反馈与细化，防止错误传播，从而适应多样化物体属性与长时程任务。
- 引入自进化工具库：新技能与验证器可被保留复用，使框架随处理视频增多而减少处理时间。
- 在最后阶段通过变化仿真中的物体与机器人状态生成多样化轨迹，并通过重纹理化渲染观测促进仿真到真实迁移。
- 在十一个真实世界任务中，使用 DexAgent 生成数据训练的策略成功率比竞争基线高 3.5 倍。

### 局限性
摘要未提供足够信息。摘要未提供关于失败案例、计算开销、对特定物体类别或任务类型的适用边界、真实机器人实验设置细节、基线具体构成、验证器设计细节及其可能失效情形等信息。

### 阅读优先级
高。理由：该工作针对灵巧操作中 Human2Sim2Robot 流水线的自适应与可扩展性问题，提出智能体式框架与自进化工具库，并报告了在十一个真实世界任务上相对基线 3.5 倍的成功率提升，主题与具身智能、机器人操作及仿真到真实迁移高度相关，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Human videos offer a scalable source of demonstrations for dexterous robot manipulation. However, existing human-to-simulation-to-robot (Human2Sim2Robot) pipelines rely on predefined procedures that struggle to accommodate diverse object properties and interactions, particularly those involving articulated and deformable objects. We introduce DexAgent, an agentic Human2Sim2Robot framework that converts a single egocentric human video and a task prompt into physically grounded robot trajectories for policy training. It operates through four stages: semantic understanding of human videos, property-based simulation reconstruction, robot trajectory optimization, and robot data generation. At each stage, DexAgent adapts its approach to the task and object properties by selecting suitable skills from its tool library or developing new ones when needed. Property-specific verifiers assess stage outcomes for physical validity and task-specific requirements and provide feedback for refinement, preventing error propagation through the workflow. This adaptive, verification-guided process allows DexAgent to process diverse objects and long-horizon tasks. In the final stage, DexAgent varies object and robot states in simulation to generate diverse robot trajectories from a single human video, then retextures the rendered observations to facilitate sim-to-real transfer. Newly developed skills and verifiers are retained in its tool library, making it self-evolving to accumulate reusable capabilities. This reduces processing time as DexAgent encounters more human videos. Across eleven real-world tasks, policies trained with DexAgent-generated data achieve a 3.5x higher success rate than competing baselines. Project website: https://dexagent123.github.io/.

</details>

#### 2026-09-28 - MarsLab: A Martian Rover Simulator for Planetary Rover Autonomous Navigation

**Authors:** Hoyun Kim, Beomsu Kim, Giseop Kim
**Links:** [abs](https://arxiv.org/abs/2609.34702) - [pdf](https://arxiv.org/pdf/2609.34702)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** simultaneous localization and mapping, SLAM, robotics, mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MarsLab: A Martian Rover Simulator for Planetary Rover Autonomous Navigation
- 作者：Hoyun Kim, Beomsu Kim, Giseop Kim
- 出版日期：2026-09-28T09:18:28Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类为 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2609.34702 ；PDF https://arxiv.org/pdf/2609.34702 ；项目页 https://kimhoyun-robotair.github.io/MarsLab/

### 一句话总结
MarsLab 是一个开源、原生支持 ROS2 的火星车仿真器，基于 NVIDIA Isaac Sim 构建，用于在可配置地形、光照和大气尘埃条件下开发与评测自主导航算法。

### 研究问题
未来火星任务需要火星车在非结构化地形、光照变化、大气尘埃和通信受限条件下具备自主能力。仿真是在部署前研究这些条件的实用手段，但现有与火星相关的资源在范围上各不相同，包括面向任务的仿真器、固定模拟数据集、任务特定环境和开放机器人接口。论文试图在这一背景下提供一个统一、可配置的火星车自主导航仿真平台。

### 核心思路/方法
MarsLab 将源自 HiRISE 的地形与程序化生成地形相结合，并提供可定制的岩石、陨石坑、太阳光照和大气尘埃设置；在 NVIDIA Isaac Sim 中运行一个毅力号级别的火星车模型。运行时通过标准 ROS2 话题发布 RGB、深度、RGB-D 点云、LiDAR、IMU、轮式里程计和 Ground Truth（GT）位姿数据。论文用 SLAM 基准测试演示 MarsLab，覆盖不同传感模态、尘埃水平、场景几何和路线长度；并用 Visual Place Recognition（VPR）基准测试，在光照和尘埃变化下对重复的火星基地穿越进行评测。

### 主要贡献
- 提出 MarsLab：一个开源、ROS2 原生的火星车仿真器，面向自主与导航算法开发。
- 将 HiRISE 派生地形与程序化地形结合，并提供岩石、陨石坑、太阳光照和大气尘埃的可定制设置。
- 在 NVIDIA Isaac Sim 中运行毅力号级火星车模型。
- 通过标准 ROS2 话题发布多种传感与状态数据：RGB、深度、RGB-D 点云、LiDAR、IMU、轮式里程计和 GT 位姿。
- 展示了两类基准测试：跨传感模态、尘埃水平、场景几何和路线长度的 SLAM 基准；以及光照和尘埃变化下重复火星基地穿越的 VPR 基准。
- 结果表明，受控场景变化和共享 GT 轨迹可用于在同一仿真器内比较轨迹级估计与图像级地点识别。

### 局限性
摘要未提供足够信息。摘要未说明仿真到现实的差距、计算资源需求、地形或尘埃模型的真实度验证、基准测试的绝对性能结论、与其他仿真器的定量比较，以及是否支持多火星车或更广泛任务场景等细节。

### 阅读优先级
高。理由：该工作直接面向行星火星车自主导航，提供开源、ROS2 原生且集成 Isaac Sim 的仿真环境，并同时给出 SLAM 与 VPR 基准，对从事行星机器人、自主导航、SLAM 和视觉地点识别的研究者有较强相关性；且论文明确提供项目页，便于进一步获取资源。

</details>

<details>
<summary>Abstract</summary>

Future Mars missions will require rover autonomy that can operate across unstructured terrain, changing illumination, atmospheric dust, and limited communication. Simulation is a practical way to study these conditions before deployment, but existing Mars-relevant resources differ in scope, including mission-oriented simulators, fixed analog datasets, task-specific environments, and open robotics interfaces. In this context, we present MarsLab, an open-source, ROS2-native Mars rover simulator for autonomy and navigation algorithm development. MarsLab combines HiRISE-derived and procedural terrain with customizable rock, crater, solar-illumination, and atmospheric-dust settings, and runs a Perseverance-class rover model in NVIDIA Isaac Sim. The runtime publishes RGB, depth, RGB-D point clouds, LiDAR, IMU, wheel odometry, and Ground Truth (GT) pose data through standard ROS2 topics. We demonstrate MarsLab with Simultaneous Localization and Mapping (SLAM) benchmarks across sensing modalities, dust levels, scene geometry, and route length, and with Visual Place Recognition (VPR) benchmarks over repeated Mars Base traversals under illumination and dust changes. The results illustrate how controlled scene variation and shared GT trajectories can be used to compare trajectory-level estimation and image-level place recognition within the same simulator. Our Project Page: https://kimhoyun-robotair.github.io/MarsLab/.

</details>

#### 2026-09-28 - When the Score Becomes the Target: Rethinking Metric Validity in Autonomous Driving

**Authors:** Morui Zhu, Deyuan Qu, Qi Chen, Kentaro Oguchi, Qing Yang
**Links:** [abs](https://arxiv.org/abs/2609.34440) - [pdf](https://arxiv.org/pdf/2609.34440)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：When the Score Becomes the Target: Rethinking Metric Validity in Autonomous Driving
- 作者：Morui Zhu, Deyuan Qu, Qi Chen, Kentaro Oguchi, Qing Yang
- 出版日期：2026-09-28T06:59:37Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.34440

### 一句话总结
论文质疑当自动驾驶评测分数本身成为优化目标时，分数提升是否仍能可靠反映驾驶行为改进，并指出需要同时审查评分过程测量什么以及被优化行为如何被执行。

### 研究问题
驾驶基准分数不仅用于评测，也越来越被当作优化目标。论文提出的核心问题是：一旦分数本身被优化，分数增益是否仍然是驾驶改进的可靠证据。具体关注评分过程如何响应驾驶行为变化，以及这些增益在重复执行和重新规划下是否持续。

### 核心思路/方法
论文将评分过程分解为执行、测量、子分数映射和聚合四个环节。通过受控干预，观察那些在请求运动与执行运动之间被省略、阈值化或衰减的行为区分，是否会带来显著行为变化却只得到很小的分数响应。进一步通过闭环比较，检验当执行接口变化时优化增益是否会发生反转，从而说明增益依赖于请求如何被执行并作为反馈返回。

### 主要贡献
- 提出并检验“分数成为优化目标后，分数增益是否仍可靠”这一问题。
- 将评分过程拆解为执行、测量、子分数映射与聚合，用于分析分数对行为变化的响应机制。
- 通过受控干预揭示行为变化与分数响应之间的脱节，并指出这种脱节源于行为区分在请求与执行之间被省略、阈值化或衰减。
- 通过闭环比较说明优化增益可能在执行接口改变时反转，强调增益的迁移依赖于执行与反馈方式。
- 结论是：在优化条件下讨论度量有效性，需要同时考察评分过程测量什么，以及被优化行为如何被执行。

### 局限性
摘要未提供足够信息说明具体实验平台、数据集、评估指标、干预设计的细节、统计显著性、样本规模以及所涉及的自动驾驶任务范围。摘要也未提供足够信息说明该方法是否在真实车辆或仅仿真环境中验证，以及其结论对其他驾驶基准或评分体系的泛化程度。

### 阅读优先级
中。理由：论文关注自动驾驶基准分数作为优化目标时的度量有效性问题，问题意识明确且具有方法反思价值；但摘要未提供具体实验细节、平台和量化结果，因此对需要直接复用实验结论或工程落地的读者，优先级取决于其是否关心评测方法论与闭环优化可靠性。

</details>

<details>
<summary>Abstract</summary>

Driving benchmark scores are increasingly used not only for evaluation but also as optimization targets. This raises a fundamental question: do score gains remain reliable evidence of driving improvement once the score itself is optimized? We address this question by examining how the scoring process responds to changes in driving behavior and whether the resulting gains persist under repeated execution and replanning. We decompose the process into execution, measurement, subscore mapping, and aggregation. Controlled interventions reveal substantial behavioral changes that receive little score response because distinctions are omitted, thresholded, or attenuated between requested and executed motion. Closed-loop comparisons further show that optimization gains can reverse when the execution interface changes, demonstrating their dependence on how requests are executed and returned as feedback. Together, these findings connect the behavioral distinctions preserved by a metric to the conditions under which its gains transfer. Metric validity under optimization therefore requires examining both what the scoring process measures and how the optimized behavior is executed.

</details>

#### 2026-09-28 - UMR: Universal Manipulation Representation

**Authors:** Song Liu, Linyi Li, Yanshun Zhao, Rxuan Li, Xinrui Xu, Yi Ju, Yahui Deng, Senge Zhang, Guoyu Liu, Yixuan Li, Wuyang Zhang, Yao Li, Congcong Zhu, Jingrun Chen
**Links:** [abs](https://arxiv.org/abs/2609.34256) - [pdf](https://arxiv.org/pdf/2609.34256)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UMR: Universal Manipulation Representation
- 作者：Song Liu, Linyi Li, Yanshun Zhao, Rxuan Li, Xinrui Xu, Yi Ju, Yahui Deng, Senge Zhang, Guoyu Liu, Yixuan Li, Wuyang Zhang, Yao Li, Congcong Zhu, Jingrun Chen
- 出版日期：2026-09-28T04:01:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接 https://arxiv.org/abs/2609.34256 ；PDF 链接 https://arxiv.org/pdf/2609.34256 ；项目页面 https://umr-wepvla.github.io/

### 一句话总结
论文提出统一操作表示 UMR，将操作动作分解为世界坐标系下的物体运动（World Flow）与相对当前位姿的末端执行器运动（Ego Trajectory），并实例化为 0.5B 参数的 WEPVLA 策略，实现从人类演示到异构机器人的零样本技能迁移。

### 研究问题
现有策略依赖特定本体的动作空间，导致跨本体演示难以大规模利用，并限制了向新本体和空间变化的迁移。论文试图解决如何在统一动作表示下，使通用具身操作能够跨本体内在泛化并易于扩展。

### 核心思路/方法
UMR 将操作分解为两个功能不同但几何关联的部分：本体无关的 World Flow，描述世界坐标系中任务相关物体运动；Ego Trajectory，表示相对于当前位姿的末端执行器运动。两者通过 \(SE(3)\) 共轭耦合。作者将 UMR 实例化为 WEPVLA，一个 0.5B 参数的紧凑策略，通过双流 Point Action Adapter 和统一 Point Action Expert 在统一几何动作空间中学习。为提升数据效率，提出 Data-Efficient Strategy（DES），通过阶段感知点云编辑丰富物体配置，同时保留演示的接触几何。

### 主要贡献
- 提出统一操作表示 UMR，用于跨本体、可扩展的通用操作动作表示。
- 将 UMR 实例化为 WEPVLA，一个 0.5B 参数策略，采用双流 Point Action Adapter 与统一 Point Action Expert，并通过 \(SE(3)\) 共轭耦合 World Flow 与 Ego Trajectory。
- 提出数据高效策略 DES，通过阶段感知点云编辑多样化物体配置并保留演示接触几何。
- 摘要报告：仿真中 WEPVLA 在 LIBERO 上平均成功率 97.5%，在 10 任务 RLBench 上为 85.7%；真实实验中，仅用人类演示加 DES 增强训练单个策略，每任务约 10 分钟人类演示且无机器人演示，在六种评估设置下平均成功率 91.7%，对比 HumanEgo 为 60.8%。

### 局限性
摘要未提供足够信息。未说明失败案例、跨本体类型范围、真实实验任务数量与具体设置、DES 的适用边界、计算成本、安全性或长期自主性等细节。

### 阅读优先级
高。理由：该论文聚焦具身操作中跨本体统一动作表示这一核心问题，提出明确的两组件分解与可实例化策略，并报告了仿真与真实实验的成功率及零样本迁移结果；若关注 VLA、跨本体迁移或人类演示规模化利用，该工作具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

General-purpose embodied manipulation hinges on a unified action representation that generalizes across embodiments and scales readily. Yet existing policies rely on embodiment-specific action spaces, making cross-embodiment demonstrations difficult to leverage at scale and limiting transfer to new embodiments and spatial variations. To this end, we introduce Universal Manipulation Representation (UMR), a unified action representation that enables zero-shot skill transfer from human demonstrations to heterogeneous robots. UMR decomposes manipulation into two functionally distinct yet geometrically linked components: embodiment-agnostic World Flow, which describes task-relevant object motion in the world frame, and Ego Trajectory, which represents end-effector motion relative to the current pose. We instantiate UMR as World--Ego Point VLA (WEPVLA), a compact 0.5B-parameter policy that learns in the unified geometric action space through a dual-stream Point Action Adapter and a unified Point Action Expert, with an $SE(3)$ conjugation coupling the two components. To improve data efficiency, we complement UMR with a Data-Efficient Strategy (DES) that diversifies object configurations through stage-aware point-cloud editing while preserving demonstrated contact geometry. In simulation, WEPVLA achieves average success rates of 97.5\% on LIBERO and 85.7\% on the 10-task RLBench benchmark. In real-world experiments, a single policy trained on human demonstrations augmented by DES transfers zero-shot to diverse deployment conditions. With about 10 minutes of collected human demonstrations per task and no robot demonstrations, it achieves 91.7\% average success across six evaluation settings, compared with 60.8\% for HumanEgo. Code and additional materials are available at https://umr-wepvla.github.io/.

</details>

#### 2026-09-27 - 3D Point Tracking with State Space Models

**Authors:** Masahiro Ogawa, Qi An, Atsushi Yamashita
**Links:** [abs](https://arxiv.org/abs/2609.34035) - [pdf](https://arxiv.org/pdf/2609.34035)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, 4D reconstruction, robot navigation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D Point Tracking with State Space Models
- 作者：Masahiro Ogawa, Qi An, Atsushi Yamashita
- 出版日期：2026-09-27T23:56:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.34035) / [PDF](https://arxiv.org/pdf/2609.34035)

### 一句话总结
该论文提出一种无位姿、单目、可在单张消费级 GPU 上运行的度量级 3D 点追踪方法，通过冻结的 2D 光流与单目度量深度前端，仅用紧凑状态空间模型学习难以提供的深度残差。

### 研究问题
论文关注动态场景中任意点的度量级 3D 追踪，即输出以绝对米为单位、而非未知尺度下的 3D 位置。作者指出这类能力对 3D/4D 重建、机器人导航和自动驾驶至关重要，因为这些场景的决策依据是米而非像素。目标是在无位姿、单目、单张消费级 GPU 的预算下，实现绝对度量准确的 3D 点追踪。

### 核心思路/方法
方法基于一个观察：一旦某点的 2D 图像轨迹固定，决定其度量精度的量就是沿该像素射线的深度。因此作者不采用端到端学习追踪，而是组合两个冻结前端：用于 2D 对应的稠密光流，以及用于第三维的单目度量深度网络；只学习它们无法提供的残差，即由紧凑状态空间模型（Mamba-3）在 DINOv3 外观特征条件下精化的深度。选择状态空间模型而非最强 3D 追踪器所用的 Transformer，是为了在单 GPU 预算下可行：状态空间模型以固定大小循环状态汇总轨迹，内存开销随帧数恒定，而注意力机制需要随帧数线性增长的键值缓存。在 TAPVid-3D minival 基准上，最佳配置在相同评估条件下取得最高绝对度量精度（平均度量 Average Jaccard 为 0.256），超过强前馈追踪器；论文还包含一项伴随分析，用各竞争者自己的评估器复现，解释为何若干已发表追踪器在该预算下损失大部分精度。

### 主要贡献
- 提出一种无位姿、单目、单张消费级 GPU 的度量级 3D 点追踪方法。
- 观察到 2D 轨迹固定后，度量精度由沿像素射线的深度决定，并据此组合冻结的稠密光流与单目度量深度前端，仅学习深度残差。
- 使用紧凑状态空间模型（Mamba-3）并在 DINOv3 外观特征条件下精化深度，以获得随帧数恒定的内存开销。
- 在 TAPVid-3D minival 上，最佳配置取得相同条件下最高绝对度量精度，平均度量 Average Jaccard 为 0.256。
- 提供伴随分析，用各竞争者自己的评估器解释为何若干已发表追踪器在该预算下损失大部分精度。

### 局限性
摘要未提供足够信息。摘要未提供关于方法失败案例、泛化能力、计算开销具体数值、不同数据集表现、消融实验细节或实际部署限制的充分信息。

### 阅读优先级
高。理由：该论文针对度量级 3D 点追踪这一对机器人、自动驾驶和 3D/4D 重建重要的任务，提出在单张消费级 GPU、无位姿、单目预算下的方案，并在 TAPVid-3D minival 上报告了相同条件下最高的绝对度量精度；其冻结前端加状态空间模型的设计思路和伴随分析也具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Tracking any point of a dynamic scene in metric 3D - in absolute meters, not up to an unknown scale - underpins 3D and 4D reconstruction, robot navigation, and autonomous driving, where decisions are made in meters, not pixels. Our objective is a 3D point tracker accurate in those absolute terms and operating within a single commodity GPU, pose-free, monocular budget. Our method rests on one observation: once a point's 2D image trajectory is fixed, the quantity that governs its metric accuracy is the depth along its pixel ray. Rather than learning tracking end-to-end, we therefore compose two frozen front-ends - dense optical flow for 2D correspondence and a monocular metric-depth network for the third dimension - and learn only the residual they cannot supply: that depth, refined by a compact state space model (Mamba-3) conditioned on appearance features (DINOv3). A state space model rather than the transformers the strongest 3D trackers adopt is what makes a single-GPU budget attainable: it summarises a track in a fixed-size recurrent state whose memory cost is constant in the number of frames, whereas attention requires a key-value cache that grows linearly with them. On the TAPVid-3D minival benchmark our best configuration attains the highest absolute metric accuracy among methods evaluated under identical conditions (mean metric Average Jaccard, 0.256), exceeding strong feed-forward trackers, while a companion analysis, reproduced with each competitor's own evaluator, explains why several published trackers lose most of their accuracy under this budget.

</details>

#### 2026-09-27 - DexTaG: Tactile-as-Guidance in Reinforcement Learning for Dexterous Manipulation

**Authors:** Han Yang, Yian Wang, Yunlong Song, Zhenjia Xu, Chuang Gan
**Links:** [abs](https://arxiv.org/abs/2609.33882) - [pdf](https://arxiv.org/pdf/2609.33882)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DexTaG: Tactile-as-Guidance in Reinforcement Learning for Dexterous Manipulation
- 作者：Han Yang, Yian Wang, Yunlong Song, Zhenjia Xu, Chuang Gan
- 出版日期：2026-09-27T19:56:41Z
- 分类：Embodied / Robotics / AR Applications
- 链接：abstract_url: https://arxiv.org/abs/2609.33882；pdf_url: https://arxiv.org/pdf/2609.33882

### 一句话总结
DexTaG 提出一种以触觉信号为引导的强化学习框架，利用手套采集的人类接触模式指导灵巧手操作策略学习，并通过统一重定向器与蒸馏学生控制器提升效率与真实世界部署能力。

### 研究问题
基于手套的动作捕捉虽可规模化采集灵巧手演示数据，但由于人手与机器人手之间的运动学差异，记录的人类动作无法直接迁移到机器人上，尤其在涉及手内重定向的富接触工具使用任务中更为困难。已有工作通过强化学习或轨迹优化在仿真中弥合差距，但难以保留人类接触模式，常导致不自然操作和不稳定的功能性抓取；同时这些方法通常为每条参考轨迹单独训练策略或求解优化，效率较低。

### 核心思路/方法
DexTaG 是一个触觉引导的强化学习框架，用于灵巧操作。训练过程中，由手套采集的触觉信号引导策略搜索朝向测量到的人类接触模式，从而减少接触监督对精确参考几何的依赖。为提升效率，方法对同一物体的所有训练轨迹联合训练一个可泛化的重定向器；该重定向器进一步蒸馏为一个无触觉的学生控制器，并以目标物体轨迹为条件，用于真实世界部署。

### 主要贡献
- 提出使用触觉信号作为强化学习中的引导，使策略搜索趋向人类接触模式，降低对精确参考几何进行接触监督的依赖。
- 针对同一物体的所有训练轨迹联合训练一个可泛化的重定向器，而非为每条参考轨迹单独训练策略或求解优化，以提升效率。
- 将重定向器蒸馏为无触觉的学生控制器，并以目标物体轨迹为条件，面向真实世界部署。
- 在 marker-pen 和 hammer 操作任务上，DexTaG 学到自然、富接触的行为，而基于距离的接触启发式基线无法学到这些行为；方法能泛化到同一物体与任务的留出轨迹，并在 OakInk2 上优于单轨迹基线。

### 局限性
摘要未提供足够信息说明方法的失败案例、对触觉手套数据质量或标定的敏感性、真实世界部署的具体限制、计算成本细节，以及在更多物体类别或更复杂任务上的泛化边界。摘要也未提供足够信息说明学生控制器在真实世界中的定量表现与安全性评估。

### 阅读优先级
高。理由：该论文聚焦于灵巧手操作中人类演示到机器人迁移的关键难题，提出触觉引导强化学习与统一重定向器及无触觉蒸馏部署路径，问题重要且方法具有明确的新意；摘要已报告在具体工具使用任务上优于基线，适合关注机器人学习、灵巧操作和触觉引导策略的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Glove-based motion capture is emerging as a scalable approach to collecting dexterous-hand demonstration data. However, due to the kinematic gap between the human and robot hand, the recorded human motions cannot be executed directly on the robot, especially for contact-rich tool-use tasks involving in-hand reorientation. Prior work bridges this gap in simulation through reinforcement learning (RL) or trajectory optimization, but the human contact pattern is hard to preserve under such formulations, often producing unnatural manipulation and unstable functional grasps. These methods also train a separate policy or solve a separate optimization for each reference trajectory, which is inefficient. To solve these problems, we propose DexTaG, a tactile-guided RL framework for dexterous manipulation. During training, tactile signals captured by the glove guide policy search toward the measured human contact pattern, reducing reliance on precise reference geometry for contact supervision. To improve efficiency, we train a single generalizable retargeter jointly on all training trajectories of the same object. The retargeter is further distilled into a tactile-free student controller conditioned on the target object trajectory for real-world deployment. On marker-pen and hammer manipulation tasks, DexTaG learns natural, contact-rich behaviors that baselines with distance-based contact heuristics fail to learn, generalizes to held-out trajectories of the same object and task, and outperforms single-trajectory baselines on OakInk2.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
