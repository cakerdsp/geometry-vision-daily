# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：60
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 18
  - Neural Scene Representations & Rendering: 16
  - Embodied / Robotics / AR Applications: 15
  - Geometry Foundation Models: 7
  - Dynamic / 4D Reconstruction: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **前馈三维重建从"一次性预测"走向"可交互、可适配、可纠正"**
   Click3R、3R-Adapter、HIST3R 三篇论文共同指向同一痛点：前馈重建模型输出不可撤回、在长尾/长时序场景中失效。三者分别从交互式稀疏对应注入（Click3R）、参数高效微调恢复跨视图关系（3R-Adapter）、利用历史状态校正循环更新方向与幅度（HIST3R）给出不同层面的补救方案。这说明该方向的研究重心正从"提升单次前馈精度"转向"如何让已有前馈模型在部署中可控、可修"。

2. **几何基础模型与语义基础模型的"外部耦合"成为 SLAM/建图新范式**
   V3DSAM 将 VGGT-SLAM 2.0 的几何估计与 SAM3 的开放词汇语义观测组合，在不访问骨干内部特征的前提下做回环验证与实例建图；DPGS-SLAM 将扩散修复先验与 3DGS 建图结合并引入"来源标签"区分生成与观测支持的高斯基元。二者都体现"不重训大模型、在系统层做组合与约束"的工程化路线。

3. **高斯泼溅（3DGS）向"基元泛化"与"系统效率"两端延伸**
   Spaghetti Splatting 把 3DGS 的"核函数+基元"配方推广到曲线型基元，并指出点可视为零长度曲线、该方法构成 3DGS 的严格超集；UltraVoxelGS 用体素优先的前馈高斯预测适配超声稀疏切片；Mitigating SM-Level Load Imbalance 则从 GPU 调度层面解决 3DGS 渲染的 SM 级负载失衡。三者分别代表表示层、领域适配层、系统层的不同推进方向。

4. **评测与基准意识显著增强，且开始面向专业场景与能力维度**
   GeoMind 针对具身操作中的空间推理与空间记忆构建 54 个任务变体，明确批评现有基准用强视觉线索绕过空间推理、用静态场景回避空间记忆；Forensic evaluation framework 面向犯罪现场重建提出结构化取证评估框架并以 EFM3D 为案例；Click3R 也专门构建暴露前馈失败模式的挑战性基准。基准正从"刷点"转向"暴露失败模式"和"专业可用性"。

5. **机器人/具身方向从"感知对齐"扩展到"空间理解、条件表示与优化闭环"**
   UniOMA 用 Gromov–Wasserstein 正则促进力/触觉等模态的结构对齐；AutoVLA-D 提出离散轨迹-几何条件（TrajCond）作为连续轨迹预测的上游条件；OASIS 把底层 MPC 的优化结果反馈给高层子目标策略；GeoMind 则直接评测空间推理与记忆。共同点是：不再只做端到端映射，而是显式引入结构、约束或优化反馈。

#### 技术路线观察

- **几何基础模型方向**：V3DSAM 代表"几何基础模型 + 语义基础模型 + 系统级验证"的组合路线，强调不依赖骨干内部特征、不依赖帧间 ID 传播，走的是可解释、可插拔的工程路线；3R-Adapter 则从模型内部关系注意力结构入手，把适配形式化为"域偏移下的对应恢复"，属于 PEFT 层面的结构性适配。两者一外一内，构成几何基础模型落地长尾场景的两条互补路径。
- **3D/4D 重建方向**：Click3R（交互纠正）、HIST3R（流式状态更新校正）、3R-Adapter（长尾适配）显示重建研究正从"精度竞赛"转向"可靠性工程"——失败检测、人类修正、状态漂移控制成为核心议题。GRAM/MORE/ART 则仍在经典多视图几何内部做理论收敛（把两视图优化与旋转平均合并为单阶段、把仅旋转几何推广到多视图），属于传统几何路线的稳健推进。
- **神经场景表示方向**：Spaghetti Splatting 是表示层面的"基元扩展"，UltraVoxelGS 是"领域适配 + 前馈化"（用体素支撑解耦表示规模与帧数、用渲染时外观自适应处理视角依赖），GPU 调度论文是"系统层优化"。三者共同说明 3DGS 生态已分化出表示、领域、系统三个相对独立但互相依赖的研究层次。
- **机器人/AR 应用方向**：UniOMA 关注多模态结构对齐（含力/触觉等少探索模态），AutoVLA-D 关注 VLA 规划中的条件表示设计，OASIS 关注学习策略与模型预测控制的优化闭环，GeoMind 关注能力评测，Feel My Focus 关注交互式数字孪生的响应性优先设计。整体呈现"从感知到决策、从离线到在线、从单一模态到结构约束"的扩散态势，但各论文之间方法差异较大，尚未形成统一技术栈。
- **横向对比**：SLAM 类工作（V3DSAM、DPGS-SLAM、S²D-FVO、BCVS）普遍强调"不重训、可在线、系统级约束"；重建类工作（Click3R、HIST3R、3R-Adapter）更关注"如何修正已有前馈模型"；表示类工作（Spaghetti、UltraVoxelGS、GPU 调度）更关注表示能力与运行效率。三类工作的评价指标和部署假设差异明显，跨类迁移需要谨慎。

#### 值得优先阅读的论文

1. **Click3R（2611.12875）**：提出"交互式几何校正"这一明确的新问题设定，并配套构建暴露失败模式的基准。对关注前馈重建可靠性、人机协同修正的研究者优先级最高。
2. **HIST3R（2611.12011）**：方向—幅度分解给出了分析 CUT3R 类循环状态更新的统一视角，并指出已有无训练扩展只能控幅度不能控方向，这一诊断本身具有较高复用价值。
3. **V3DSAM（2611.12452）**：展示了"几何基础模型 + 开放词汇语义 + 双尺度回环验证 + 几何锚定实例建图"的完整系统组合，是理解基础模型时代 SLAM 系统设计取舍的良好样本。
4. **Spaghetti Splatting（2611.12716）**：把 3DGS 的卷积平滑配方推广到曲线基元并论证其为 3DGS 严格超集，理论动机清晰，对表示层研究有直接启发。
5. **GeoMind（2611.12175）**：明确指出现有具身基准的两个结构性缺陷（强视觉线索绕过推理、静态场景回避记忆），并给出 54 个任务变体的系统化设计，对做具身评测的研究者有较高参考价值。

（备选：若更关注机器人控制闭环，可将 OASIS 替换 GeoMind；若更关注领域适配，可将 UltraVoxelGS 替换 Spaghetti Splatting。）

#### 可能的研究机会

- **交互式校正与参数高效适配的结合**：Click3R 用稀疏点击注入几何约束，3R-Adapter 用 PEFT 恢复关系结构。二者能否组合——即用少量用户点击驱动关系结构的定向重连，而非仅做推理时约束注入——是一个自然的空白。
- **流式重建中的"可修正状态"设计**：HIST3R 用历史校正更新方向与幅度，但仍是训练-free 的启发式。若能结合 Click3R 式的人类反馈或 V3DSAM 式的语义-几何验证来判定"哪些更新不可靠"，可能形成更鲁棒的流式状态管理机制。
- **生成先验与观测证据的显式分离**：DPGS-SLAM 的"来源标签"提供了一种区分生成内容与观测支持内容的机制。这一思路可推广到其他使用扩散先验补全的建图/重建系统，形成"证据等级"感知的场景表示。
- **曲线/线状基元在细结构场景的应用验证**：Spaghetti Splatting 在表示层支持曲线基元

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-11T15:11:26-05:00
**Total number of papers:** 59
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

#### 2026-11-05 - Georeferenced Cross-View 3D Reconstruction from Ground and Satellite Images

**Authors:** David G. Shatwell, Mubarak Shah
**Links:** [abs](https://arxiv.org/abs/2611.07575) - [pdf](https://arxiv.org/pdf/2611.07575)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Georeferenced Cross-View 3D Reconstruction from Ground and Satellite Images
- 作者：David G. Shatwell, Mubarak Shah
- 出版日期：2026-11-05T07:26:29Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.07575) | [PDF](https://arxiv.org/pdf/2611.07575)

### 一句话总结
论文提出 X-VGGT，一个前馈式跨视角几何 Transformer，联合处理地面图像与带地理参考的卫星图像，同时预测地面相机位姿、稠密 3D 点图以及场景级变换参数，从而将局部重建对齐到卫星平面，实现地面图像的地理配准。

### 研究问题
从地面图像进行地理参考 3D 重建，不仅需要恢复局部场景几何，还需要把每个相机中心和 3D 点定位到地理坐标系中。摘要指出，现有跨视角地理定位方法只能估计单个地面相机的 GPS 坐标，不能重建稠密 3D 几何；而近期的前馈多视图 3D 重建模型只在局部坐标系中预测点图和相机位姿。因此，如何将跨视角地理定位与稠密 3D 重建统一起来，是本文关注的问题。

### 核心思路/方法
论文提出 X-VGGT，一种前馈式跨视角几何 Transformer。其核心是联合处理一组地面级图像和一张带地理参考的卫星图像，并预测三类输出：
1. 地面视角相机位姿；
2. 稠密 3D 点图；
3. 一个场景级变换，该变换由重力、尺度、偏航角和 translation 参数化。

该变换用于将局部重建投影到卫星平面，从而完成所有地面图像与带地理参考卫星图像的地理配准。论文还提出了针对这一联合任务的评估协议。

### 主要贡献
- 提出 X-VGGT，将地面图像与卫星图像联合处理，统一跨视角地理定位与稠密 3D 重建任务。
- 在输出中同时预测地面相机位姿、稠密 3D 点图，以及由重力、尺度、偏航角和 translation 参数化的场景级变换，用于将局部重建投影到卫星平面并实现地理配准。
- 提出针对该联合任务的评估协议。
- 摘要称，在多个跨视角数据集上，X-VGGT 能产生准确的地理参考重建，并优于先前的跨视角地理定位和多视图 3D 重建模型。

### 局限性
摘要未提供足够信息。例如具体数据集名称、实验设置、定量指标、失败案例、计算开销、对卫星图像质量或地面图像覆盖范围的敏感性等，均未在摘要中说明。

### 阅读优先级
高。理由：该论文直接针对跨视角地理定位与前馈多视图 3D 重建之间的任务缺口，提出联合建模方法和评估协议；摘要明确声称在多个跨视角数据集上优于现有两类方法，问题定义和方法输出均较清晰，适合关注 3D 重建、多视图几何与跨视角地理定位交叉方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Georeferenced 3D reconstruction from ground images requires recovering not only the local scene geometry, but also localizing every camera center and 3D point in a geographic coordinate frame. Existing cross-view geo-localization methods are able to estimate the GPS coordinate of a single ground camera, but do not reconstruct dense 3D geometry, while recent feed-forward multi-view 3D reconstruction models predict point maps and camera poses only in a local coordinate frame. We introduce X-VGGT, a feed-forward cross-view geometry transformer that unifies these tasks by jointly processing a set of ground-level images and a georeferenced satellite image to predict ground-view camera poses, dense 3D point maps, and a scene-level transform parameterized by gravity, scale, yaw and translation. This transform projects the local reconstruction into the satellite plane, resulting in the geo-registration of all ground images with the georeferenced satellite image. We further propose an evaluation protocol for this joint task and show that, across multiple cross-view datasets, X-VGGT produces accurate georeferenced reconstructions and outperforms prior cross-view geo-localization and multi-view 3D reconstruction models.

</details>

#### 2026-11-05 - MetricTrail: Revisiting the Power of Metric Depth and Local Optimization for Long-Sequence Streaming 3D Reconstruction

**Authors:** Jingnan Gao, Jiahui Huang, Sven Elflein, Jianhao Zheng, Bingxin Ke, Xiaokang Yang, Yichao Yan, Laura Leal-Taixé, Qunjie Zhou, Jiawei Ren, Shengyu Huang
**Links:** [abs](https://arxiv.org/abs/2611.07555) - [pdf](https://arxiv.org/pdf/2611.07555)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** metric depth, 3D reconstruction, dense reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MetricTrail: Revisiting the Power of Metric Depth and Local Optimization for Long-Sequence Streaming 3D Reconstruction
- 作者：Jingnan Gao, Jiahui Huang, Sven Elflein, Jianhao Zheng, Bingxin Ke, Xiaokang Yang, Yichao Yan, Laura Leal-Taixé, Qunjie Zhou, Jiawei Ren, Shengyu Huang
- 出版日期：2026-11-05T07:02:32Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.07555 ；PDF https://arxiv.org/pdf/2611.07555

### 一句话总结
MetricTrail 是一个面向长单目视频的流式系统，通过引入单图像度量深度改进 DPVO 式稀疏局部估计器，并结合冻结 DINOv3 表示的学习适配器提升对应估计，从而实现相机运动估计与稠密重建。

### 研究问题
论文关注从长单目视频中进行准确的相机运动估计与稠密重建。为在长序列上保持推理效率，作者重新审视 DPVO 的稀疏局部估计器，试图在不重新训练对应网络、不扩大优化窗口的前提下提升轨迹精度，并改善对应估计与系统模块的可替换性。

### 核心思路/方法
- 沿用 DPVO 的稀疏局部估计器以保持长序列推理效率。
- 利用单图像度量深度初始化 patch 深度，并在优化过程中将其作为软约束，从而提升轨迹精度；摘要强调无需重新训练对应网络或扩大优化窗口。
- 通过学习的适配器，将冻结的 DINOv3 表示用于增强匹配特征与循环上下文，以改进对应估计。
- 对应估计器与适配器在多样的短片段上训练，不进行额外的长序列训练。
- 模块化设计使深度提供者可以独立升级，并支持提供相机内参与标定立体观测而无需重新训练。

### 主要贡献
- 提出 MetricTrail 流式系统，用于长单目视频的相机运动估计与稠密重建。
- 表明单图像度量深度可显著提升 DPVO 式稀疏局部估计器的轨迹精度，且无需重新训练对应网络或扩大优化窗口。
- 引入基于冻结 DINOv3 表示的学习适配器以增强匹配特征和循环上下文。
- 系统设计具备模块化特性：深度提供者可独立升级，并支持输入相机内参与标定立体观测而无需重训练。
- 摘要报告在仅 RGB 协议下，于 KITTI、Oxford Spires 和 VBR 上取得所评估方法中最低的平均轨迹误差；将估计位姿与单图像深度预测配对后，在室内外基准上产生较强稠密重建，并对野外视频产生连贯重建。
- 摘要报告在提供内参时，系统处理 KITTI-02 达到 12.70 FPS，峰值 GPU 内存 3.21 GB。

### 局限性
- 摘要未提供足够信息说明方法在极端长序列、剧烈运动、低纹理或动态场景下的具体表现。
- 摘要未提供足够信息说明对单图像度量深度预测质量的依赖程度及失败模式。
- 摘要未提供足够信息给出完整实验设置、对比方法细节、消融实验规模与训练数据规模。
- 摘要未提供足够信息说明稠密重建的定量指标细节与实时性在不同硬件上的泛化表现。
- 摘要未提供足够信息讨论标定立体观测与提供内参场景下的系统开销与精度变化。

### 阅读优先级
中。理由：论文聚焦长序列流式单目 3D 重建，结合度量深度、局部优化与冻结视觉基础模型适配器，问题明确且摘要给出多基准轨迹误差与效率数据；但摘要未展开实验细节与局限性，适合作为相关方向的重点跟踪论文，而非仅凭摘要即可完全评估其方法细节的必读高优先级。

</details>

<details>
<summary>Abstract</summary>

We present MetricTrail, a streaming system for accurate camera motion estimation and dense reconstruction from long monocular videos. To keep inference efficient over long sequences, we revisit DPVO's sparse local estimator. We find that single-image metric depth substantially improves its trajectory accuracy, without retraining the correspondence network or enlarging the optimization window. Metric predictions initialize patch depths and remain as soft constraints during optimization. We further improve correspondence estimation through learned adapters that augment matching features and recurrent context with frozen DINOv3 representations. The correspondence estimator and adapters are trained on diverse short clips without additional long-sequence training. This modular design also allows the depth provider to be independently upgraded and supports supplied camera intrinsics and calibrated stereo observations without retraining. Under the reported RGB-only protocols, MetricTrail achieves the lowest average trajectory error among evaluated methods on KITTI, Oxford Spires, and VBR. Pairing the estimated poses with single-image depth predictions also produces strong dense reconstruction on indoor and outdoor benchmarks and coherent reconstructions of in-the-wild videos. With supplied intrinsics, the system processes KITTI-02 at 12.70 FPS with 3.21 GB peak GPU memory.

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

#### 2026-11-05 - SM4RT: Cascaded Feed-forward Model for 4D Reconstruction

**Authors:** Pang-Chi Lo, Jhao-Syun Lai, Tsung-Wei Ke
**Links:** [abs](https://arxiv.org/abs/2611.08436) - [pdf](https://arxiv.org/pdf/2611.08436)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** geometric reasoning, 4D reconstruction, dynamic scene reconstruction, scene reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SM4RT: Cascaded Feed-forward Model for 4D Reconstruction
- 作者：Pang-Chi Lo, Jhao-Syun Lai, Tsung-Wei Ke
- 出版日期：2026-11-05T18:28:38Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.08436) | [PDF](https://arxiv.org/pdf/2611.08436)

### 一句话总结
SM4RT 是一个多任务级联前馈模型，先重建 3D 几何，再基于预测结构估计运动，用于从 RGB 视频进行动态场景重建。

### 研究问题
现有前馈方法通常将几何重建与运动估计分开处理，且往往在单一坐标系中预测运动，需要额外应对相机运动带来的歧义；同时真实世界的运动标注稀疏。论文旨在解决动态场景中几何与运动联合重建的上述问题。

### 核心思路/方法
SM4RT 采用级联方式依次完成两项任务：先重建 3D 几何，再以预测出的结构为基础引导运动估计。模型将每个像素的 3D 运动表达在其对应的相机坐标系中，以降低相机运动引起的歧义。针对运动标签稀疏问题，引入弱监督损失，利用另一时间步的已标注点位置约束未标注点的运动。模型为多任务前馈架构。

### 主要贡献
- 提出级联前馈框架 SM4RT，将几何重建与运动估计顺序结合，而非分开处理。
- 在对应相机坐标系中表达逐像素 3D 运动，以缓解相机运动带来的歧义。
- 引入弱监督损失，利用另一时间步的标注点位置正则化未标注点运动，应对真实运动标签稀疏问题。
- 在 Kubric、Waymo、Point Odyssey 三个动态场景数据集上评估运动估计，据摘要称在多数指标上优于先前基线；并在五个动态场景数据集上评估几何重建，据摘要称达到与 state-of-the-art 方法有竞争力的表现。
- 摘要指出该统一框架表明级联结合几何重建与运动估计不仅避免性能权衡，还能通过改善几何推理增强运动估计。

### 局限性
- 摘要未提供足够信息说明具体网络结构、参数量、训练细节与推理效率。
- 摘要未提供足够信息说明弱监督损失的具体形式与权重设置。
- 摘要未提供足够信息说明各数据集上的具体数值结果、对比基线细节及失败案例。
- 摘要未提供足够信息说明方法在非动态场景、极端相机运动或标注极少条件下的表现。

### 阅读优先级
中。理由：论文主题属于动态/4D 重建中的几何与运动联合估计，级联前馈与相机坐标系运动表达的思路具有一定方法参考价值；但摘要仅给出高层描述与有限实验结论，未提供足够细节判断其实际效果与可复现性，适合在需要了解该方向新框架时进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

We introduce SM4RT, a multi-task cascade feed-forward model for dynamic scene reconstruction from RGB videos. While existing feed-forward approaches typically address geometry reconstruction and motion estimation separately--and often predict motions in a single coordinate frame that must account for camera movement--SM4RT solves these tasks sequentially by first reconstructing 3D geometry and then bootstrapping motion estimation from the predicted structure. By expressing each pixel's 3D motion in its corresponding camera frame, SM4RT reduces ambiguity arising from camera motion. To address the sparsity of real-world motion labels, SM4RT further incorporates a weakly supervised loss that regularizes unlabeled point motions using labeled point positions at the other time step. We evaluate motion estimation on three dynamic-scene datasets--Kubric, Waymo, and Point Odyssey--and SM4RT achieves the best performance on most metrics compared with prior baselines. We additionally benchmark geometry reconstruction on five dynamic scene datasets and show that SM4RT achieves competitive performance with state-of-the-art methods. Overall, our unified framework demonstrates that combining geometry reconstruction and motion estimation in a cascade not only avoids performance trade-offs but also enhances motion estimation through improved geometric reasoning.

</details>

#### 2026-11-05 - InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image

**Authors:** Chanho Kim, Muhammad Salman Ali, Kyeonghwan Gwak, Muhammad Shaheryar, Incheol Park, Jeongwan On, Seungryul Baek
**Links:** [abs](https://arxiv.org/abs/2611.08330) - [pdf](https://arxiv.org/pdf/2611.08330)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** avatar reconstruction, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image
- 作者：Chanho Kim, Muhammad Salman Ali, Kyeonghwan Gwak, Muhammad Shaheryar, Incheol Park, Jeongwan On, Seungryul Baek
- 出版日期：2026-11-05T17:21:08Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.08330 ；PDF https://arxiv.org/pdf/2611.08330

### 一句话总结
InstantHand 提出一种前馈框架，利用现成的 MANO、相机与掩码估计，从单张图像直接构建可动画的 3D Gaussian 手部 avatar，无需测试时优化，并针对轮廓监督不足与外观颜色漂移提出两项正则/迁移策略。

### 研究问题
论文关注从单张图像重建可动画手部 avatar 的问题。摘要指出，现有手部 avatar 重建通常依赖多视角采集或逐受试者优化，限制了可扩展性。本文试图在无需测试时优化的前提下，以单图输入构建可动画的 3D Gaussian 手部 avatar。摘要还指出两个具体问题：图像平均损失对 alpha 泄漏监督不足，导致细手指轮廓变厚；从图像特征回归的颜色即使在观测区域也可能漂向学习到的先验。

### 核心思路/方法
- 采用前馈框架，从单张图像构建可动画的 3D Gaussian 手部 avatar。
- 使用现成的 MANO、相机和掩码估计作为输入条件，不进行测试时优化。
- 提出 Soft Alpha Band 正则器，将监督集中在轮廓边界，以缓解图像平均损失对 alpha 泄漏监督不足、细手指轮廓变厚的问题。
- 提出 Reliability-gated Appearance Transfer：根据每个 Gaussian 的渲染贡献迁移源颜色，以保留观测外观；同时以全局源身份为条件，用学习到的先验补全未观测区域，以缓解颜色向先验漂移的问题。
- 摘要报告构建 avatar 用时 2.84 秒，渲染速度 161 FPS。

### 主要贡献
- 提出 InstantHand：一种从单张图像前馈构建可动画 3D Gaussian 手部 avatar 的框架，无需测试时优化，依赖现成 MANO、相机和掩码估计。
- 提出 Soft Alpha Band regularizer，针对轮廓边界集中监督，以改善 alpha 泄漏导致的细手指轮廓变厚问题。
- 提出 Reliability-gated Appearance Transfer，按 Gaussian 渲染贡献迁移源颜色以保留观测外观，并用全局源身份条件化的先验补全未观测区域。
- 摘要称其在 InterHand2.6M 上匹配逐受试者优化基线，在 HanCo 的零样本评估中保持竞争力，并给出 2.84 秒构建与 161 FPS 渲染的效率指标。

### 局限性
- 摘要未提供足够信息说明方法在遮挡、极端姿态、手部与物体交互或低质量输入条件下的具体表现。
- 摘要未提供足够信息说明对 MANO、相机和掩码估计质量的敏感程度及失败案例。
- 摘要未提供足够信息说明 Soft Alpha Band 正则器与 Reliability-gated Appearance Transfer 的消融细节和定量增益。
- 摘要未提供足够信息说明在 InterHand2.6M 与 HanCo 上的完整评估协议、指标定义及零样本评估的具体设置。
- 摘要未提供足够信息说明方法对非手部区域、背景或全身场景的适用性。

### 阅读优先级
中。理由：该论文聚焦单图前馈手部 avatar 重建，问题定义清晰，且给出构建时间与渲染帧率等效率指标，对动态/4D 重建与神经场景表示渲染方向有参考价值；但摘要未提供充分实验细节与消融结果，是否值得优先精读需结合全文的实验完整性与与自身研究方向的相关性判断。

</details>

<details>
<summary>Abstract</summary>

Hand avatar reconstruction typically relies on multi-view capture or per-subject optimization, limiting its scalability. We introduce InstantHand, a feed-forward framework that constructs an animatable 3D Gaussian hand avatar from a single image using off-the-shelf MANO, camera, and mask estimates, without test-time optimization. Image-averaged losses provide insufficient supervision for alpha leakage, which thickens thin finger contours. To address this issue, we propose a Soft Alpha Band regularizer that concentrates supervision on silhouette boundaries. Furthermore, colors regressed from image features can drift toward a learned prior even in observed regions. Our Reliability-gated Appearance Transfer preserves observed appearance by transferring source colors according to each Gaussian's rendering contribution, while completing unobserved regions using the learned prior conditioned on global source identity. InstantHand constructs an avatar in 2.84 seconds and renders at 161 FPS, matching per-subject-optimized baselines on InterHand2.6M and remaining competitive in zero-shot evaluation on HanCo.

</details>

#### 2026-11-05 - XM4D: 4D Reconstruction through Certifiable Geometric Optimization

**Authors:** Haoyu Han, Jack Benarroch Jedlicki, Jiahui Lei, Heng Yang
**Links:** [abs](https://arxiv.org/abs/2611.07902) - [pdf](https://arxiv.org/pdf/2611.07902)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** depth prediction, 4D reconstruction, non-rigid reconstruction, dynamic Gaussian, bundle adjustment, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：XM4D: 4D Reconstruction through Certifiable Geometric Optimization
- 作者：Haoyu Han, Jack Benarroch Jedlicki, Jiahui Lei, Heng Yang
- 出版日期：2026-11-05T12:20:52Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.07902 ；PDF https://arxiv.org/pdf/2611.07902

### 一句话总结
XM4D 将 4D 重建中的相机运动估计与非刚性形变估计分离，分别建模为可验证全局最优性的结构化 QCQP 并求解，再用所得几何初始化动态高斯泼溅进行光度细化。

### 研究问题
论文关注准确的 4D 重建问题：联合估计相机运动、场景几何与非刚性形变属于高度非凸优化，难以保证全局最优性。摘要指出，如何在保证精度与效率的同时获得可验证的全局最优性，是该方法要解决的核心问题。

### 核心思路/方法
- 总体框架：将相机运动估计与非刚性形变估计分离，两个阶段都形式化为结构化二次约束二次规划（QCQP），并给出半定规划（SDP）松弛与可验证的全局最优性证书。
- 相机运动估计：利用基础深度预测模型将静态点轨迹提升到 3D，构建同时估计相机位姿、深度尺度与静态路标的缩放式 bundle adjustment 问题；通过解析消去平移与路标，将问题约化为关于缩放旋转的 QCQP。
- 非刚性重建：使用嵌入式形变图（EDG）表示动态运动，并说明其跟踪、刚性与时序正则目标同样可约化为仅含旋转的 QCQP。
- 求解方式：两个问题均采用 SDP 松弛，并使用基于黎曼优化的 GPU 加速 Burer–Monteiro 求解器高效求解。
- 后续细化：恢复的几何用于初始化动态高斯泼溅，以进行光度细化。

### 主要贡献
- 提出 XM4D 框架，以可证明全局最优的几何优化为基础实现 4D 重建。
- 通过分离相机运动与非刚性形变，将两个阶段分别转化为结构化 QCQP，并提供 SDP 松弛与可验证的全局最优性证书。
- 在相机运动阶段，通过解析消去平移与路标，把缩放式 bundle adjustment 约化为缩放旋转上的 QCQP。
- 在非刚性阶段，基于 EDG 将跟踪、刚性与时序正则目标约化为仅含旋转的 QCQP。
- 使用 GPU 加速的 Burer–Monteiro 黎曼优化求解器处理 SDP 松弛，并以恢复几何初始化动态高斯泼溅进行光度细化。
- 摘要称在七个基准上进行了广泛实验，展示了静态与动态场景中的准确相机运动估计、可扩展到数千帧的高效优化，以及当前最优的新视角渲染质量。

### 局限性
- 摘要未提供足够信息说明失败情形、对基础深度预测模型误差的敏感性、SDP 松弛在何种条件下保证紧致性，以及计算开销的具体量级。
- 摘要未提供足够信息说明七个基准的具体构成、评测协议、与基线方法的定量对比细节及消融实验结果。
- 摘要未提供足够信息说明方法对极端非刚性运动、遮挡、弱纹理或大规模场景的适用边界。

### 阅读优先级
高。理由：摘要明确针对 4D 重建中非凸优化与全局最优性保证这一核心难题，提出可验证最优性的 QCQP/SDP 建模路线，并覆盖相机运动、非刚性形变与动态高斯泼溅细化；若关注动态/4D 重建与神经场景表示，该论文的问题设定和方法框架具有较高阅读价值。但需注意，摘要未给出定量实验细节，阅读全文时应重点核查全局最优性证书的实际适用条件与实验支撑。

</details>

<details>
<summary>Abstract</summary>

Accurate 4D reconstruction remains challenging: jointly estimating camera motion, scene geometry, and non-rigid deformation entails highly nonconvex optimization, making global optimality difficult to guarantee. We present XM4D, a framework for accurate and efficient 4D reconstruction built upon certifiably globally optimal geometric optimization. By separating the estimation of camera motion from non-rigid deformation, we formulate both stages as structured quadratically constrained quadratic programs (QCQP) that admit semidefinite programming (SDP) relaxations and verifiable global optimality certificates. For camera motion estimation, we lift static point tracks into 3D using foundational depth prediction models and formulate a scaled bundle adjustment problem that jointly estimates camera poses, depth scales, and static landmarks. By analytically eliminating translations and landmarks, we reduce the problem to a QCQP over scaled rotations. For non-rigid reconstruction, we represent dynamic motion using an embedded deformation graph (EDG) and show that its tracking, rigidity, and temporal regularization objectives similarly reduce to a rotation-only QCQP. Both problems admit SDP relaxations that we solve efficiently with a GPU-accelerated Burer-Monteiro solver based on Riemannian optimization. The recovered geometry further initializes dynamic Gaussian splatting for photometric refinement. Extensive experiments across seven benchmarks demonstrate accurate camera motion estimation on both static and dynamic scenes, efficient optimization that scales to thousands of frames, and state-of-the-art novel-view rendering quality.

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

#### 2026-11-05 - PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation

**Authors:** Chuanxin Song, Peixi Peng
**Links:** [abs](https://arxiv.org/abs/2611.07873) - [pdf](https://arxiv.org/pdf/2611.07873)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** motion trajectories, depth estimation, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation
- 作者：Chuanxin Song, Peixi Peng
- 出版日期：2026-11-05T11:47:33Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2611.07873；PDF https://arxiv.org/pdf/2611.07873

### 一句话总结
论文提出全景视频深度估计数据集 PanoCARLA 与端到端框架 PVDepth，通过球面感知噪声初始化与立方体贴图校正时序建模，缓解 ERP 全景视频中几何畸变和非线性时序动态带来的迁移困难。

### 研究问题
全景视频深度估计对虚拟现实和世界模型等应用重要，但领域进展受两个障碍制约：一是大规模训练数据稀缺；二是等距柱状投影（ERP）特有的时空挑战，使透视视频深度模型难以直接迁移。论文关注的核心问题是：如何让源自透视视频的深度模型适应 ERP 全景视频中的几何畸变与非线性的时序动态。

### 核心思路/方法
论文首先构建 PanoCARLA，一个大规模合成 RGB-D 全景视频数据集，具有自然运动轨迹和类无人机漫游视角。在此基础上提出 PVDepth，一个从透视视频深度模型改造而来的端到端框架。针对 ERP 特有的几何畸变及其导致的非线性时序动态，论文引入两个核心机制：
1. Progressive Sphere-aware Noise Initialization：将噪声分布从平面退火到球面，引导模型适应非均匀的信息密度；
2. Cube-rectified Temporal Modeling：引入辅助的立方体贴图时序分支，用于校正 ERP 域中的非线性时序动态。

### 主要贡献
- 提出 PanoCARLA 大规模合成 RGB-D 全景视频数据集，包含自然运动轨迹与类无人机漫游视角。
- 提出 PVDepth 端到端框架，将透视视频深度模型适配到全景视频深度估计。
- 设计 Progressive Sphere-aware Noise Initialization，以平面到球面的噪声分布退火应对 ERP 非均匀信息密度。
- 设计 Cube-rectified Temporal Modeling，借助辅助立方体贴图时序分支校正 ERP 域非线性时序动态。
- 摘要称大量实验显示 PVDepth 性能更优，能生成几何准确且时序一致的深度序列；代码和数据将公开。

### 局限性
- 摘要未提供足够信息说明 PanoCARLA 的规模、采集细节、场景多样性与标注质量。
- 摘要未提供足够信息说明实验设置、对比方法、评价指标与具体定量结果。
- 摘要未提供足够信息说明两个核心机制的计算开销、实时性或在真实全景视频上的泛化表现。
- 摘要未提供足够信息说明方法对非合成数据、不同 ERP 分辨率或极端运动场景的适用边界。

### 阅读优先级
高。理由：该论文同时针对数据稀缺与 ERP 时空适配两个明确瓶颈，提出数据集与端到端方法，并给出两个针对性机制；若关注全景视频深度估计、VR 或世界模型相关三维感知，摘要显示其问题设定与贡献较为直接相关。但具体实验证据与数据规模需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Panoramic video depth estimation is pivotal for applications such as Virtual Reality and World Models. However, advancements in this field are impeded by two primary obstacles: the scarcity of large-scale training data and the unique spatiotemporal challenges of Equirectangular Projection (ERP), which hinder the direct transfer of perspective models. In this paper, we first present PanoCARLA, a large-scale synthetic RGB-D panoramic video dataset, featuring natural motion trajectories and drone-like roaming perspectives. Building on this foundation, we propose PVDepth, an end-to-end framework adapted from perspective video depth models. To tackle ERP-specific geometric distortions and consequent non-linear temporal dynamics, we introduce two core mechanisms: (1) A Progressive Sphere-aware Noise Initialization strategy that anneals the noise distribution from planar to spherical, guiding the model to adapt to non-uniform information density; and (2) A Cube-rectified Temporal Modeling module that incorporates an auxiliary cubemap temporal branch to rectify non-linear temporal dynamics in the ERP domain. Extensive experiments demonstrate that PVDepth achieves superior performance, generating geometrically accurate and temporally consistent depth sequences. Code and data will be released at https:// github.com/ChuanxinSong/PVDepth.

</details>

#### 2026-11-05 - STAG-Net: Structure-Aware Attention over Landmark Groups for Lightweight Head Pose Estimation

**Authors:** Asiri Gawesha Lindamulage, Sanka Mohottala, Dharshana Kasthurirathna, Nuwan Kodagoda
**Links:** [abs](https://arxiv.org/abs/2611.07828) - [pdf](https://arxiv.org/pdf/2611.07828)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：STAG-Net: Structure-Aware Attention over Landmark Groups for Lightweight Head Pose Estimation
- 作者：Asiri Gawesha Lindamulage, Sanka Mohottala, Dharshana Kasthurirathna, Nuwan Kodagoda
- 出版日期：2026-11-05T11:09:34Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.07828 ；PDF https://arxiv.org/pdf/2611.07828

### 一句话总结
STAG-Net 是一种基于面部关键点组的结构感知注意力轻量头部姿态估计方法，摘要声称其在多个跨数据集和 subject independent 设置下取得对比方法中最低的平均绝对误差，同时显著降低参数量、FLOPs 与训练/推理成本。

### 研究问题
摘要指出，头部姿态估计对人机交互和驾驶员监控很重要，但许多基于图像的方法对资源受限部署而言成本仍然过高。论文关注如何在轻量化条件下，利用面部关键点进行头部姿态估计，并兼顾精度与训练、推理效率。

### 核心思路/方法
摘要给出的方法要点包括：
- 从面部关键点估计头部姿态；
- 使用 movement aware selection、空间聚类、紧凑 DeepSet 编码器、自注意力以及全局几何描述符；
- 在关键点组上施加结构感知注意力；
- 分别使用 FaceMesh 和 Face Alignment Network 关键点构建变体；
- 在 300W-LP、AFLW2000 和 BIWI 上，采用跨数据集和 subject independent 协议评估。

### 主要贡献
摘要中明确列出的贡献包括：
- 提出 STAG-Net，用于轻量头部姿态估计，并给出 FaceMesh 与 FAN 两种关键点变体；
- 在所有评估设置中，取得对比的基于关键点方法里最低的平均绝对误差；
- 在 BIWI 有效检测帧上，FAN 变体在跨数据集评估中达到 \(3.51^\circ\)，在 subject independent 评估中达到 \(2.39^\circ\)，为所有对比方法中最低总体误差；
- 回归器仅使用 0.012 至 0.043 百万参数和 24.1 至 83.6 千 FLOPs，摘要称 FLOPs 比 FSA-Net 少约三个数量级；
- 包含关键点提取与回归的 FaceMesh 流程在 Tesla T4 GPU 上达到 322.9 FPS，摘要称为最快被测图像基线 164.5 FPS 的近两倍，并在 CPU 上达到 111.0 FPS；
- 按数据集大小归一化后，训练样本处理速度比 FSA-Net 快七至八倍，比 HopeNet 和 TokenHPE 快一百倍以上，完整训练在 28 分钟内完成。

### 局限性
摘要未提供足够信息说明方法在极端姿态、遮挡、关键点检测失败场景下的鲁棒性，也未给出失败案例分析、跨域泛化边界或与更多非关键点方法的系统性比较细节。摘要未提供足够信息说明统计显著性、误差方差、模型鲁棒性消融的完整结果，以及不同硬件条件下的能耗或内存占用。摘要未提供足够信息说明训练数据规模、超参数敏感性及实际部署限制。

### 阅读优先级
中。理由：论文主题聚焦轻量头部姿态估计，摘要给出了较明确的精度、参数量、FLOPs、FPS 和训练时间对比，适合关注高效视觉模型与关键点姿态估计的读者；但摘要未展开方法细节和局限性分析，是否精读需结合对结构感知注意力、DeepSet 编码及跨数据集评估设计的兴趣。

</details>

<details>
<summary>Abstract</summary>

Head pose estimation is important for human computer interaction and driver monitoring, but many image based methods remain too costly for resource constrained deployment. We propose STAG-Net, a structure-aware attention over landmark groups for lightweight head Pose estimation that estimates head pose from facial landmarks using movement aware selection, spatial clustering, compact DeepSet encoders, self attention, and a global geometry descriptor. We develop variants using FaceMesh and Face Alignment Network landmarks and evaluate them under cross dataset and subject independent protocols on 300W-LP, AFLW2000, and BIWI. STAG-Net achieves the lowest mean absolute error among all compared landmark based methods in every evaluated setting. On BIWI frames with valid detections, the FAN variant also records the lowest overall error among all compared methods, reaching $3.51^\circ$ under cross dataset evaluation and $2.39^\circ$ under subject independent evaluation. The regressors use only 0.012 to 0.043 million parameters and 24.1 to 83.6 thousand FLOPs, about three orders of magnitude fewer FLOPs than FSA-Net. Despite including landmark extraction and regression, the FaceMesh pipeline reaches 322.9 frames per second on a Tesla T4 GPU, nearly twice the 164.5 frames per second of the fastest measured image based baseline, and 111.0 frames per second on CPU. After normalization by dataset size, STAG-Net processes training samples seven to eight times faster than FSA-Net and more than one hundred times faster than HopeNet and TokenHPE, while complete training finishes within 28 minutes. These results show that STAG-Net combines leading landmark based accuracy with substantially lower training and inference cost.

</details>

#### 2026-11-05 - Real-Time Event-Based LED Tracking and Pose Estimation with PWM-Encoded Markers

**Authors:** Junkai Niu, Sheng Zhong, Delei Kong, Xin Wang, Kaizhen Sun, Yusen Zhang, Mingzhen Gan, Yi Zhou
**Links:** [abs](https://arxiv.org/abs/2611.07630) - [pdf](https://arxiv.org/pdf/2611.07630)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-Time Event-Based LED Tracking and Pose Estimation with PWM-Encoded Markers
- 作者：Junkai Niu, Sheng Zhong, Delei Kong, Xin Wang, Kaizhen Sun, Yusen Zhang, Mingzhen Gan, Yi Zhou
- 出版日期：2026-11-05T08:16:07Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；无次要分类
- 链接：摘要页 https://arxiv.org/abs/2611.07630 ；PDF https://arxiv.org/pdf/2611.07630

### 一句话总结
论文提出一种基于事件相机的实时框架，通过脉冲宽度调制（PWM）编码的 LED 标记实现 LED 跟踪与六自由度相对位姿估计。

### 研究问题
论文关注在快速运动、运动模糊和高动态范围（HDR）光照条件下，如何利用事件相机对 LED 标记进行实时跟踪并估计 6-DoF 相对位姿。摘要指出需要解决多 LED 的身份关联、快速运动下的像素级跟踪以及实时度量位姿估计问题。

### 核心思路/方法
- 利用事件相机像素异步响应亮度变化、具备微秒级时间分辨率的特性，捕获 LED 的高频闪烁模式。
- 多个 LED 共享同一闪烁频率，并通过不同 PWM 占空比编码各自身份，以降低频率资源需求和计算成本。
- 采用双速率异步跟踪框架：低速率进行 LED 检测，高速率利用原始事件更新，从而在快速运动下保持 LED 身份关联和像素级跟踪。
- 根据 LED 身份与位置建立 2D-3D 对应关系，实现实时度量 6-DoF 相对位姿估计。

### 主要贡献
- 提出基于 PWM 编码 LED 标记的事件相机实时 LED 跟踪与 6-DoF 相对位姿估计框架。
- 设计多 LED 共享闪烁频率、以不同占空比区分身份的编码方式，减少频率资源需求和计算开销。
- 提出双速率异步跟踪框架，结合低速率检测与高速率原始事件更新，提升快速运动下的身份关联与跟踪稳定性。
- 在自采集数据集上进行广泛评估，摘要称其在大运动流和图像平面 LED 瞬态重叠下具有鲁棒性。
- 构建由四旋翼和麦轮移动机器人组成的协同机器人平台，在时变 HDR 光照下通过悬停和目标跟随实验展示闭环无人机引导潜力，并在 NVIDIA Jetson Orin NX 上板载部署。
- 摘要称将公开数据集和实现以促进后续研究。

### 局限性
- 摘要未提供足够信息说明方法在极端遮挡、LED 完全重叠或非 HDR 场景下的具体表现。
- 摘要未提供足够信息说明自采集数据集的规模、标注方式、对比基线及定量误差指标。
- 摘要未提供足够信息说明计算资源消耗、实时性具体帧率或延迟数据。
- 摘要未提供足够信息说明 PWM 占空比编码在 LED 数量增加时的可扩展性上限。
- 摘要未提供足够信息说明户外强光、远距离或低信噪比条件下的失效边界。

### 阅读优先级
中。理由：论文面向事件相机、LED 标记跟踪与实时 6-DoF 位姿估计，属于 3D 重建与多视图几何相关方向，且包含机器人平台闭环实验与板载部署信息；但摘要未给出定量实验细节和与现有方法的对比结果，是否具有显著性能优势需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Event cameras are neuromorphic vision sensors with pixels that independently and asynchronously respond to brightness changes at microsecond resolution, supporting state estimation under rapid motion, motion blur, and high dynamic range (HDR) illumination. This also enables capture of high-frequency blinking patterns from light-emitting diodes (LEDs). Based on this, we propose a real-time event-based framework for LED tracking and six-degree-of-freedom (6-DoF) relative pose estimation using pulse-width modulation (PWM)-encoded LED markers. Multiple LEDs share a common blinking frequency and encode identities through distinct PWM duty cycles, reducing frequency-resource requirements and computational cost. Our dual-rate asynchronous tracking framework combines low-rate LED detection with high-rate raw-event updates, maintaining robust LED identity association and accurate pixel-level tracking under rapid motion. LED identities and positions establish reliable 2D-3D correspondences for real-time metric 6-DoF relative pose estimation. Extensive evaluations on a self-collected dataset demonstrate robustness under large motion flow and transient image-plane LED overlap. Furthermore, we develop a coordinated robotic platform comprising a quadrotor and a Mecanum-wheeled mobile robot, demonstrating the proposed framework's potential for closed-loop drone guidance through hovering and target-following experiments under time-varying HDR illumination, with onboard deployment on an NVIDIA Jetson Orin NX. The dataset and implementation will be released to facilitate further research.

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

#### 2026-11-05 - MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation

**Authors:** Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri, Georgios Pavlakos, Roberto Martín-Martín
**Links:** [abs](https://arxiv.org/abs/2611.08372) - [pdf](https://arxiv.org/pdf/2611.08372)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting, manipulation, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation
- 作者：Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri, Georgios Pavlakos, Roberto Martín-Martín
- 出版日期：2026-11-05T17:50:35Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.08372) | [PDF](https://arxiv.org/pdf/2611.08372)

### 一句话总结
MOMASPLAT 提出一种面向移动操作（MoMa）的动态新视角示范增强框架，通过分别重建静态场景与被操作物体，并从未见过的机器人基座位姿合成包含动态交互的完整操作轨迹示范。

### 研究问题
摘要指出，通过模仿学习训练的视觉运动策略对相机视角变化高度敏感。在移动操作中，由于导航不确定性、定位漂移和环境约束，机器人很少能在与示范采集时完全相同的基座位姿下执行操作。已有的新视角合成增强方法假设场景是静态的，因此无法在接触后交互阶段重新渲染被操作物体，导致示范中最关键的部分未被增强。论文要解决的核心问题是：如何为移动操作生成包含动态物体交互的新视角示范，从而提升策略对未见基座位姿的鲁棒性。

### 核心思路/方法
摘要给出的关键洞察是：标准 MoMa 数据采集过程天然提供了重建静态场景与被操作物体所需的多视角观测。MOMASPLAT 将 3D Gaussian Splatting、前馈 3D 基础模型与基于运动学的动作重定向相结合，分别重建场景和被操作物体，从新视角渲染二者，并生成几何一致的合成示范及相应的变换后动作。该方法强调合成的是完整操作轨迹，包括动态物体交互阶段。

### 主要贡献
- 提出 MOMASPLAT，一个面向移动操作的新视角示范增强框架，能够从未见过的机器人基座位姿合成完整操作轨迹，并覆盖动态物体交互。
- 利用标准 MoMa 数据采集天然提供的多视角观测，分别重建静态场景与被操作物体。
- 结合 3D Gaussian Splatting、前馈 3D 基础模型和基于运动学的动作重定向，生成几何一致的合成示范与变换后的动作。
- 在五个真实世界移动操作任务（涉及刚性与铰接物体、跨三个场景）上评估，并在仿真中对照真值验证合成示范的保真度。
- 摘要报告：显著提升对未见基座位姿的鲁棒性，平均成功率超过最强基线两倍以上，并在所有基线均失败的大基座位移情况下仍保持非平凡成功率，同时减少对大规模真实世界数据采集的需求。

### 局限性
- 摘要未提供足够信息说明方法在非刚性物体、透明/反光物体或严重遮挡条件下的表现。
- 摘要未提供足够信息说明多视角重建对采集数据覆盖度、标定精度或计算开销的具体要求与限制。
- 摘要未提供足够信息说明真实世界评估的样本规模、统计显著性或失败模式分析。
- 摘要未提供足够信息说明动作重定向在接触丰富或高精度操作任务中的误差边界。

### 阅读优先级
中。理由：该工作针对移动操作中视角鲁棒性与动态新视角示范增强这一明确问题，方法组合（3D Gaussian Splatting、3D 基础模型、动作重定向）与真实世界任务评估在摘要中已有清晰概述，对具身智能与机器人视觉运动策略方向具有相关性；但摘要未提供实验细节、定量表格与局限性讨论，是否值得深入阅读需结合全文的实验严谨性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Visuomotor policies trained through imitation learning are highly sensitive to changes in camera viewpoint. This is particularly problematic for mobile manipulation (MoMa), where robots rarely execute manipulation from the exact same base pose used during demonstration collection due to navigation uncertainty, localization drift, and environmental constraints. Recent approaches use novel-view synthesis (NVS) to augment demonstrations with unseen viewpoints, but they assume static scenes and therefore fail to re-render the manipulated object during the post-contact interaction phase, leaving the most critical parts of the demonstration unaugmented. We present MOMASPLAT, a novel-view demonstration augmentation framework for mobile manipulation that synthesizes full manipulation trajectories from unseen robot base poses, including dynamic object interactions. Our key insight is that standard MoMa data collection naturally provides the multiview observations needed to reconstruct both the static scene and the manipulated object in 3D. MOMASPLAT combines 3D Gaussian Splatting, feed-forward 3D foundation models, and kinematics-based action retargeting to separately reconstruct the scene and manipulated object, render them from novel viewpoints, and generate geometrically consistent synthetic demonstrations paired with transformed actions. We evaluate MOMASPLAT on five real-world mobile manipulation tasks involving both rigid and articulated objects across three scenes, and validate the fidelity of its synthesized demonstrations against ground truth in simulation. MOMASPLAT substantially improves robustness to unseen base poses, more than doubling the average success rate of the strongest baseline and maintaining non-trivial success at large base displacements where all baselines fail, while reducing the need for largescale real-world data collection.

</details>

#### 2026-11-05 - 4D Point Splatting for mmWave Radar Micro-Doppler Differentiable Rendering

**Authors:** Adnan Armouti, Guanyue Qian, Rajalakshmi Nandakumar
**Links:** [abs](https://arxiv.org/abs/2611.08342) - [pdf](https://arxiv.org/pdf/2611.08342)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：4D Point Splatting for mmWave Radar Micro-Doppler Differentiable Rendering
- 作者：Adnan Armouti, Guanyue Qian, Rajalakshmi Nandakumar
- 出版日期：2026-11-05T17:27:29Z
- 分类：Neural Scene Representations & Rendering（主分类）；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.08342 ；PDF https://arxiv.org/pdf/2611.08342

### 一句话总结
提出 4DPS——一种基于物理的可微渲染器，将显式运动场景拟合到真实毫米波雷达采集，渲染原始复数回波，以缩小雷达人体感知数据的 sim2real 差距。

### 研究问题
毫米波雷达可借微多普勒感知步态、手势、活动、姿态与生命体征，但雷达数据集规模远落后于视觉与语言数据；暴力采集无法弥合差距，而现有合成方法（仅前向模拟器、学习式生成器、静态场景逆渲染器）无法拟合真实运动人体采集，存在 sim2real 差距。

### 核心思路/方法
- 用同步相机初始化房间与人体，将场景表示为带朝向的点，每点携带材质、法线与速度。
- 将每个点 splat 到距离（range）与多普勒（Doppler）bin 中，输出真实雷达记录的原始复数回波。
- 对渲染数据施加与真实数据相同的信号处理，从而获得任意表示，用于训练任意 SOTA 下游模型。
- 使用自定义 CUDA 核实现序列级拟合。

### 主要贡献
- 提出 4DPS，一种拟合真实运动场景采集的物理可微毫米波雷达渲染器。
- 在 HuPR 的 235 条序列与 RT-Pose 的 100 条序列上完成拟合，重建达到 SOTA：距离-方位中位相关 0.940 / 0.830，距离-多普勒 0.829 / 0.695，微多普勒 0.988 / 0.966。
- 渲染数据在下游 sim2real 差距上达到 SOTA：RT-Pose 上用渲染数据训练的姿态模型在真实数据上达 21.9 cm MPJPE（真实训练 16.7 cm，RF-Genesis 基线 127.6 cm），且渲染训练与真实训练模型学到近乎相同的特征。
- 单张 H100 上拟合一条序列耗时 5.7 分钟（HuPR）/ 12.9 分钟（RT-Pose），首次使毫米波雷达的数据集级逆渲染成为可能。
- 摘要称可支持任意以人为中心的下游任务的合成数据生成，以及用于数据增强的场景编辑。

### 局限性
- 摘要未提供足够信息说明方法在无同步相机的纯雷达场景、不同雷达硬件泛化或极端遮挡/多人场景下的表现。
- 摘要未提供足够信息说明渲染与真实训练之间 21.9 cm 与 16.7 cm 差距的具体来源与改进空间。
- 摘要未提供足够信息说明 5.7/12.9 分钟拟合耗时的可扩展性边界（如更大数据集或更多序列并行时的开销）。
- 摘要未提供足够信息给出定量实验之外的失败案例或误差分析。

### 阅读优先级
高。理由：该工作针对雷达人体感知数据稀缺与 sim2real 差距这一关键瓶颈，给出可微逆渲染方案，并在两个不同雷达数据集上报告重建与下游姿态估计的 SOTA 定量结果，且具备数据集级可行性；对神经场景表示、雷达感知与合成数据生成方向均有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Millimeter-wave radar resolves the micrometer displacements of a moving body as micro-Doppler, enabling gait, gesture, activity, pose and vital-sign sensing. Each task relies on a downstream model trained on real data, yet radar datasets lag orders of magnitude behind vision and language. Brute-force collection will not close that gap, and existing synthesis methods (forward-only simulators, learned generators and static-scene inverse renderers) cannot fit a real capture of a moving body, leaving a sim2real gap. We present 4D Point Splatting (4DPS), a physics-based differentiable renderer that fits an explicit moving scene to a real capture. Using the synchronized camera to initialize the room and body, we represent the scene as oriented points carrying material, normal and velocity, and splat each point into range and Doppler bins. Our output is the raw complex return a real radar records, so we apply the same signal processing on the rendered data to obtain any representation for training any SOTA downstream model. We fit 235 sequences on HuPR and 100 on RT-Pose, two datasets with different radars. Our reconstructions set the state of the art, with median correlations of 0.940 and 0.830 on range-azimuth, 0.829 and 0.695 on range-Doppler, and 0.988 and 0.966 on micro-Doppler. Our renders also set the state of the art in downstream sim2real gap. On RT-Pose, a pose model trained on them reaches 21.9 cm MPJPE on real data, against 16.7 cm for real training and 127.6 cm for the RF-Genesis baseline, where both the rendered- and real-trained models learn nearly the same features. Our custom CUDA kernels fit a sequence in 5.7 minutes on HuPR and 12.9 on RT-Pose on one H100, making dataset-scale inverse rendering of mmWave radar possible for the first time. This work can enable synthetic data generation for any human-centered downstream task and model, and scene editing for data augmentation.

</details>

#### 2026-11-05 - Hierarchical Incremental Beta Splatting for Online Reconstruction

**Authors:** Linus Franke
**Links:** [abs](https://arxiv.org/abs/2611.08288) - [pdf](https://arxiv.org/pdf/2611.08288)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Hierarchical Incremental Beta Splatting for Online Reconstruction
- 作者：Linus Franke
- 出版日期：2026-11-05T16:52:46Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2611.08288

### 一句话总结
该论文提出 HIBS（分层增量 Beta Splatting），将 beta 核引入在线 3D 重建，通过可调形状参数与置信度感知初始化、误差驱动重定位及 LOD 合并，在 Mip-NeRF 360 的 on-the-fly 协议下提升 PSNR 并缩短优化时间。

### 研究问题
在线 3D Gaussian Splatting 在采集过程中重建场景：每个关键帧只生成一次基元，并且仅对其进行数十次迭代优化，因此难以修正较差的初始化或补足缺失细节；同时高斯本身偏“软”，需要大量重叠才能表现实心表面。

### 核心思路/方法
- 将 beta 核引入增量重建，其形状参数可在“软的高斯状剖面”和“平顶、接近不透明的 surfel”之间插值，作为几何置信度的调节手段。
- 置信度感知生成：利用几何可观测性和多视图深度一致性来初始化不透明度与形状；几何可验证处生成实心基元，不可验证处生成软且可修正的基元。
- 在线致密化中的误差驱动重定位：将陈旧基元回收至光度误差热点。
- 有界 beta 核支撑带来精确 tile 剔除和更快光栅化；闭式、保形合并公式提供 LOD 层次，用于快速优化与实时渲染。

### 主要贡献
- 提出 HIBS，将 beta 核用于增量式在线重建，并以形状参数表达几何置信度。
- 提出置信度感知的基元生成策略，结合几何可观测性与多视图深度一致性初始化不透明度和形状。
- 引入误差驱动重定位进行在线致密化，回收陈旧基元。
- 利用有界支撑实现精确 tile 剔除与更快光栅化，并给出保形合并的 LOD 层次。
- 在 Mip-NeRF 360 的 on-the-fly 协议下，PSNR 最高提升 0.8 dB，优化时间最多减少 40%。

### 局限性
摘要未提供足够信息（未说明失败场景、适用范围限制、对特定数据集的依赖或计算/内存开销等）。

### 阅读优先级
中。理由：该工作聚焦在线增量重建中初始化与细节修正的关键痛点，方法组合（beta 核、置信度感知生成、重定位、LOD）较完整，并给出定量提升；但摘要仅报告单一数据集协议下的结果，且作者与实验规模信息有限，是否具有广泛适用性需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

Online 3D Gaussian Splatting reconstructs a scene during capture: each keyframe spawns primitives once and refines them for only a few dozen iterations, leaving little chance to fix poor initialization or missing detail. Gaussians are also inherently soft, needing many overlaps for solid surfaces. We present Hierarchical Incremental Beta Splatting (HIBS), which brings beta kernels to incremental reconstruction. Their shape parameter interpolates between a soft, Gaussian-like profile and a flat-topped, near-opaque surfel, acting as a confidence dial for geometry. Our confidence-aware spawning uses geometric observability and multi-view depth agreement to initialize both opacity and shape, producing solid primitives where geometry is verifiable and soft, correctable primitives where it is not. As online densification, error-driven relocation recycles stale primitives into photometric-error hotspots. Bounded beta kernel support enables exact tile culling and faster rasterization, and a closed-form, shape-preserving merging formulation provides a level-of-detail (LOD) hierarchy for fast optimization and real-time rendering. On Mip-NeRF 360 in the on-the-fly protocol, HIBS improves PSNR by up to 0.8 dB while reducing optimization time by up to 40%. Project page: https://linus-franke.com/hibs/

</details>

#### 2026-11-05 - Perception Over Geometry: Rethinking Gaussian Allocation in Mesh-based Splatting

**Authors:** Yuting Wang, Yang Zhao, Shanding Diao, Penglin Wang, Yuan Chen, Wei Jia, Ronggang Wang
**Links:** [abs](https://arxiv.org/abs/2611.07979) - [pdf](https://arxiv.org/pdf/2611.07979)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Perception Over Geometry: Rethinking Gaussian Allocation in Mesh-based Splatting
- 作者：Yuting Wang, Yang Zhao, Shanding Diao, Penglin Wang, Yuan Chen, Wei Jia, Ronggang Wang
- 出版日期：2026-11-05T13:09:42Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.07979 ；PDF https://arxiv.org/pdf/2611.07979

### 一句话总结
论文提出 P-MGS，将外观建模与几何控制分离，按感知复杂度而非网格面密度分配高斯，以较少高斯实现较优新视角合成并支持连贯的网格编辑。

### 研究问题
现有基于网格的 3D Gaussian Splatting 方法通常为每个三角面分配固定数量的高斯，但外观重建所需的表示能力取决于局部外观复杂度，而非仅由网格细分密度决定。摘要指出这一做法存在表示分配与外观需求不匹配的问题。

### 核心思路/方法
P-MGS 的核心是分离外观建模与几何控制。具体包括：引入感知复杂度引导的分配策略，根据多视角观测估计的表面外观需求来分配高斯；高斯在优化时不受网格约束，之后通过事后绑定与原始网格关联，从而在保留网格拓扑的同时维持自适应细化能力；在网格编辑时，采用局部仿射变形传递，在网格变形下更新高斯中心与协方差，减少错位与漂浮伪影。

### 主要贡献
摘要声称的贡献包括：提出按感知复杂度分配高斯的策略；通过无网格约束优化加事后绑定，兼顾重建灵活性与网格拓扑保留；设计面向网格编辑的局部仿射变形传递以更新高斯参数；实验层面摘要称在新视角合成平均质量上更优、使用更少高斯，并获得连贯的网格编辑效果。具体实验设置、数据集与定量指标摘要未提供足够信息。

### 局限性
摘要未提供足够信息。可确认的边界是：摘要未给出失败案例、计算开销、绑定误差或编辑类型覆盖范围的细节；亦未说明感知复杂度估计的具体实现与消融结果。

### 阅读优先级
中。理由：该论文针对基于网格的 3DGS 中“固定每面高斯分配”这一明确问题，提出分配策略与编辑传递方法，主题与神经场景表示及渲染直接相关；但摘要未提供定量实验细节与实现信息，是否值得优先精读取决于读者对网格编辑与高斯分配策略的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic novel-view synthesis but lacks explicit topology for geometric editing. Existing mesh-based methods enable geometric manipulation by associating Gaussians with triangular mesh faces, typically assigning a fixed number of Gaussians to each face. However, the representation capacity required for appearance reconstruction depends on local appearance complexity rather than merely on mesh tessellation density. To address these limitations, we propose P-MGS, a framework that separates appearance modeling from geometric control to achieve high quality rendering, compact representation, and flexible mesh editing. P-MGS introduces a perceptual complexity guided allocation strategy that distributes Gaussians according to surface appearance demand estimated from multiview observations. To preserve reconstruction flexibility, Gaussians are optimized without mesh constraints and subsequently associated with the original mesh through post hoc binding, retaining adaptive refinement while preserving mesh topology. During mesh editing, local affine deformation transfer updates Gaussian centers and covariances under mesh deformation, reducing misalignment and floating artifacts. Experiments demonstrate superior average novel view synthesis quality with fewer Gaussians and coherent mesh editing.

</details>

#### 2026-11-05 - AffineGS: Unlocking Accurate Geometry in 3DGS via Spatially Varying Affine Rectification

**Authors:** Tze Ho Elden Tse, Jizong Peng, Richard Chen, Angela Yao
**Links:** [abs](https://arxiv.org/abs/2611.07709) - [pdf](https://arxiv.org/pdf/2611.07709)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** metric depth, monocular depth, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AffineGS: Unlocking Accurate Geometry in 3DGS via Spatially Varying Affine Rectification
- 作者：Tze Ho Elden Tse, Jizong Peng, Richard Chen, Angela Yao
- 出版日期：2026-11-05T09:27:56Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.07709 ；PDF https://arxiv.org/pdf/2611.07709

### 一句话总结
论文指出单目深度网络存在随区域变化的“分段线性”失真，使 3DGS 中常用的全局尺度—平移对齐失效，因此提出空间变化的仿射校正与法向感知正则，以在保持高斯泼溅照片级质量的同时提升几何精度。

### 研究问题
3D Gaussian Splatting（3DGS）在新视角合成上视觉质量突出，但几何精度落后于其视觉质量。现有深度引导方法通常用单目深度先验正则化优化，并采用一个全局的 scale-and-shift 对齐；作者认为这一假设存在根本缺陷：现代单目深度网络系统性地表现出区域相关、分段线性的失真，而全局对齐会因强制单一变换而扭曲场景几何。

### 核心思路/方法
针对上述问题，论文提出：
1. **空间变化的仿射校正模型**：将单目视差校正为一致的度量深度，使用区域平滑、边缘感知的场来建模空间变化的仿射关系，而不是全局统一变换。
2. **法向感知正则器**：利用空间梯度，将校正后的视差与 3DGS 的深度和法向耦合起来。
3. 方法定位为**无需传感器（sensor-free）**，在多种实验设置下同时追求高斯泼溅的强光度质量与更高的几何精度。

### 主要贡献
- 发现并指出单目深度网络存在区域相关、分段线性失真的现象，说明标准全局对齐策略会扭曲场景几何。
- 提出空间变化的仿射校正模型，用区域平滑且边缘感知的场将单目视差校正为一致的度量深度。
- 推导法向感知正则器，以空间梯度耦合校正视差与 3DGS 的深度、法向。
- 摘要声称：在多种实验设置下，该无传感器方法在保持高斯泼溅强光度质量的同时显著提升几何精度，并优于当前聚焦几何的最先进方法。

### 局限性
- 摘要未提供足够信息说明方法对哪些场景类型、数据集规模或退化条件不适用。
- 摘要未提供足够信息说明空间变化仿射场的具体参数化、优化开销或实时性影响。
- 摘要未提供足够信息给出定量指标、对比基线细节与消融实验规模。
- 摘要未提供足够信息说明“区域平滑、边缘感知”假设在强非仿射失真或深度先验严重错误时的失效边界。

### 阅读优先级
**高**。理由：该工作直接挑战 3DGS 深度引导中广泛使用的全局对齐假设，问题定位清晰；若摘要所述“区域相关分段线性失真”成立，则对基于单目深度先验的 3DGS 几何优化具有方法层面的普遍意义，且摘要声称在几何精度上优于聚焦几何的最先进方法，值得优先阅读以核验其假设、正则设计与实验证据。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has become the leading approach for photorealistic novel view synthesis, yet its geometric accuracy lags behind its visual quality. Existing depth-guided methods attempt to resolve this by regularizing the optimization with monocular depth priors, typically using a single global scale-and-shift alignment. Crucially, we discover a fundamental flaw in this assumption: modern monocular depth networks systematically exhibit region-dependent, piecewise-linear distortions. This discovery invalidates standard global alignment strategies, which warp scene geometry by enforcing a single transform. To address this, we introduce a spatially varying affine rectification model that corrects monocular disparity into consistent metric depth using regionally smooth, edge-aware fields. We further derive a normal-aware regularizer that uses spatial gradients to couple the rectified disparity with 3DGS depth and normals. Across diverse experimental settings, our sensor-free method shows strong photometric quality of Gaussian Splatting while substantially improving geometric accuracy and outperforming state-of-the art geometry-focused methods.

</details>

#### 2026-11-05 - Integrating Learned Priors through Prior-Space Reparameterization for Physically Based Inverse Rendering

**Authors:** Hun Hwangbo, Minjun Park, Yongsung Kim, Wooseok Song, Jungmin Ko, Junghyun Hwang, Sungroh Yoon
**Links:** [abs](https://arxiv.org/abs/2611.07573) - [pdf](https://arxiv.org/pdf/2611.07573)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Integrating Learned Priors through Prior-Space Reparameterization for Physically Based Inverse Rendering
- 作者：Hun Hwangbo, Minjun Park, Yongsung Kim, Wooseok Song, Jungmin Ko, Junghyun Hwang, Sungroh Yoon
- 出版日期：2026-11-05T07:20:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.07573) / [PDF](https://arxiv.org/pdf/2611.07573)

### 一句话总结
论文提出一种基于先验空间的材质重参数化方法，将学习到的材质预测作为先验来约束优化空间，同时保持纯光度目标不变，从而改善物理逆渲染中的材质分解与重光照效果。

### 研究问题
物理逆渲染需要从外观中分解材质与光照，但该问题本身具有歧义性。现有方法多通过辅助正则损失引入学习到的材质先验，这会改变优化目标，并需要平衡先验影响与光度拟合。论文关注的是：如何在不改变目标函数的情况下，有效利用学习到的材质先验来约束逆渲染优化。

### 核心思路/方法
论文提出一种先验引导的材质重参数化方法，利用预测特征之间的关系限制优化空间，而不改变优化目标。具体做法包括：将多视角材质预测融合到网格上，并在得到的先验特征空间中构造 permutohedral lattice；使具有相似预测的表面点共享材质变量，并将这些变量与几何、光照一起在纯光度目标下联合优化。摘要还提到，该重参数化会汇聚带噪声的光度梯度，使采样视角间的更新更一致，从而支持缩短联合优化时间。

### 主要贡献
- 提出一种先验引导的材质重参数化方法，通过限制优化空间引入学习先验，同时保持目标函数不变。
- 使用多视角材质预测融合、先验特征空间中的 permutohedral lattice 以及相似预测表面点共享材质变量的机制。
- 在两个学习预测器、三个合成基准和 Stanford-ORB 上进行实验，报告改善材质分解与重光照。
- 在 Synthetic4Relight 和 TensoIR-Synthetic 上，相比评估中最强的基于网格的基线，重光照 PSNR 提升 1.5-2.5 dB。
- 在受控比较中，优于使用相同先验的正则损失方法。
- 展示了该重参数化可汇聚噪声光度梯度，使采样视角间更新更一致，并支持不足一分钟的缩短联合优化计划，同时在 TensoIR-Synthetic 上保持高于所有评估基线的重光照质量。

### 局限性
摘要未提供足够信息说明方法在非合成数据上的泛化能力、对材质预测器质量的敏感性、计算开销的完整分析，以及失败案例或局限条件。摘要未提供足够信息说明更多实验细节与消融范围。

### 阅读优先级
高。理由：论文直接针对物理逆渲染中“如何引入学习先验而不改变优化目标”的关键问题，提出明确的重参数化机制，并在摘要中报告了重光照 PSNR 提升、优于同先验正则损失以及缩短优化时间的结果；对神经场景表示与渲染、逆渲染和材质分解方向具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Physically based inverse rendering decomposes appearance into materials and illumination, an ambiguous problem for which learned material predictions provide useful prior information. Most existing methods incorporate these cues through auxiliary regularization losses, which alter the optimization objective and require balancing their influence against photometric fitting. We propose a prior-guided material reparameterization that uses the predicted feature relationships to restrict the optimization space while leaving the objective unchanged. We fuse multi-view material predictions onto a mesh and construct a permutohedral lattice in the resulting prior feature space. Surface points with similar predictions share material variables, which are optimized jointly with geometry and illumination using a purely photometric objective. Experiments with two learned predictors on three synthetic benchmarks and Stanford-ORB demonstrate improved material decomposition and relighting. Our method improves relighting PSNR by 1.5-2.5 dB over the strongest evaluated mesh-based baseline on Synthetic4Relight and TensoIR-Synthetic, and outperforms a regularization loss using the same prior in controlled comparisons. We further show that our reparameterization pools noisy photometric gradients, producing updates that are more consistent across sampled views. This consistency enables a shortened joint optimization schedule that takes less than a minute while retaining relighting quality above all evaluated baselines on TensoIR-Synthetic.

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
- 作者：Arian Hajizadeha, Javad Pourrafia, Negar Shenavara, Sana Bashiria, Seyed Majid Esmailzadeh
- 出版日期：2026-11-09T07:25:13Z
- 分类：主分类 Embodied / Robotics / AR Applications；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.11996 ；PDF https://arxiv.org/pdf/2611.11996

### 一句话总结
OASIS 是一个分层导航框架：高层策略在生成局部子目标时，把上一个子目标区间内控制器的优化结果作为反馈输入，并在底层用带运动限制、几何避碰与高阶控制障碍函数约束的非线性模型预测控制跟踪子目标。

### 研究问题
动态环境中的移动机器人导航需要兼顾目标推进、运动限制与障碍规避。学习到的子目标策略可以帮助模型预测控制突破局部预测时域，但摘要明确指出：几何上合适的子目标不一定能带来成功求解的控制问题。因此问题在于，如何让子目标生成考虑底层控制器优化是否可行/成功，而不仅仅是几何合理性。

### 核心思路/方法
- 采用分层结构：高层策略用 Soft Actor–Critic 训练，生成局部子目标；底层使用非线性模型预测控制跟踪子目标。
- 底层控制约束包括：运动限制、几何碰撞避免约束，以及嵌入的高阶控制障碍函数约束。
- 将每个子目标区间内控制器优化的结果进行汇总，并在策略下一次决策时提供给策略，且不需要额外的优化调用。
- 摘要未提供足够信息说明“优化结果”的具体汇总方式、状态表示、网络结构、训练细节与参数设置。

### 主要贡献
- 提出 OASIS：将近期优化结果纳入基于强化学习的子目标生成，形成优化感知的分层导航框架。
- 在五个包含静态与移动障碍的导航场景中评估，场景涉及密集交互与感知不确定性。
- 与分层控制变体和直接目标控制变体比较，摘要称 OASIS 取得最高的总体导航成功率。
- 在三个训练种子的匹配比较中，相对于除缺少优化状态输入外其余相同的分层结构，摘要称其具有一致的成功率优势。
- 所选策略比较显示，在平均控制器时间相近的情况下，主要优化失败更少。

### 局限性
- 摘要未提供足够信息说明实验规模、具体场景定义、成功率数值、失败率数值、控制器时间数值与统计显著性检验。
- 摘要未提供足够信息说明优化状态汇总的具体设计、消融完整性与计算开销的详细分析。
- 摘要未提供足够信息说明真实机器人实验；评估仅从摘要看为五个导航场景。
- 摘要未提供足够信息说明方法在更高维系统、不同机器人模型或不同底层控制器上的泛化能力。

### 阅读优先级
中。理由：该摘要聚焦于“子目标生成需考虑底层优化可行性”这一明确问题，并给出分层强化学习与带安全约束的非线性模型预测控制结合的设计，以及多场景与多种子比较结果；但摘要未给出具体数值与实现细节，是否值得深入阅读取决于读者对优化感知子目标、控制障碍函数约束和移动机器人导航交叉方向的兴趣。

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

#### 2026-11-05 - TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

**Authors:** Yijiong Lin, Wenhao He, Toby Jack, Max Yang, Haoran Li, Nathan F. Lepora
**Links:** [abs](https://arxiv.org/abs/2611.07881) - [pdf](https://arxiv.org/pdf/2611.07881)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation
- 作者：Yijiong Lin, Wenhao He, Toby Jack, Max Yang, Haoran Li, Nathan F. Lepora
- 出版日期：2026-11-05T12:01:12Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.07881 ；PDF https://arxiv.org/pdf/2611.07881

### 一句话总结
TactileLab 是一个基于 IsaacLab 的可扩展多模态触觉仿真框架，用基于光流的“模拟触觉流”替代高计算成本的软体/可变形仿真来表征接触剪切，并结合真到仿触觉翻译与新的数据采集方法，实现从仿真训练到真实双臂与灵巧手内操作部署的端到端 sim-to-real 流程。

### 研究问题
论文关注接触丰富操作中的触觉仿真问题：高保真地模拟触觉传感中的剪切通常依赖可变形或软体仿真，计算开销大，难以扩展到大规模强化学习。因此需要一种可扩展、能高效表征剪切相关接触动力学的触觉仿真方式，并解决仿真触觉与真实触觉之间的迁移问题，以支持真实机器人上的灵巧操作部署。

### 核心思路/方法
- 构建于 IsaacLab 之上的可扩展多模态触觉仿真框架 TactileLab。
- 提出“模拟触觉流”（simulated tactile flow）：不依赖软体物理建模剪切变形，而使用刚体仿真高效估计接触界面的稠密切向运动，生成编码剪切相关接触动力学的触觉流场。
- 该流场与接触深度场提供的几何特征互补，形成多模态触觉表征。
- 提出一种新的策略架构，用于联合处理长时程本体感知信号与丰富触觉观测。
- 为促进 sim-to-real 部署，提出真到仿触觉翻译方法，将真实触觉图像流映射为模拟触觉流与深度场，并提出新的触觉数据采集方法，在不同触觉传感器设计上进行验证。
- 使用该流程在包含双臂与灵巧手内操作的任务上展示真实世界部署。

### 主要贡献
- 提出 TactileLab：基于 IsaacLab 的可扩展多模态触觉仿真框架，聚焦剪切敏感触觉。
- 提出基于光流的模拟触觉流表征，以刚体仿真高效估计接触界面稠密切向运动，避免依赖高成本软体/可变形仿真来建模剪切。
- 将触觉流场与接触深度场结合，形成互补的触觉观测。
- 提出联合处理长时程本体感知与丰富触觉观测的新策略架构。
- 提出真到仿触觉翻译方法，将真实触觉图像流映射为模拟触觉流和深度场，并配合新的触觉数据采集方法，在多种触觉传感器设计上验证。
- 在多种接触丰富任务中，使用模拟触觉流训练的策略表现出可扩展的高效学习，并出现接触感知行为；在真实世界双臂与灵巧手内操作任务上完成部署。
- 整体上提供面向可扩展触觉策略学习的端到端 sim-to-real 框架，支持异构触觉机器人系统上的剪切敏感操作。

### 局限性
摘要未提供足够信息。摘要未给出具体任务清单、成功率、训练规模、仿真与真实实验的定量对比、失败案例、传感器型号与数量、计算开销数据，也未说明方法在超出已验证传感器设计与任务范围外的适用性限制。

### 阅读优先级
中。理由：该论文聚焦触觉仿真中的剪切表征与 sim-to-real 迁移，对接触丰富操作、触觉强化学习和灵巧操作方向具有明确相关性；其“用刚体仿真估计触觉流替代软体仿真”的思路和真到仿触觉翻译具有一定方法新颖性。但仅凭摘要无法判断定量效果、可复现性与跨传感器泛化程度，建议在需要评估触觉仿真效率或灵巧操作 sim-to-real 方案时阅读全文进一步核实。

</details>

<details>
<summary>Abstract</summary>

Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable multimodal tactile simulation framework built on IsaacLab, with a particular focus on a new optical-flow-based tactile representation termed \textit{simulated tactile flow}. Instead of relying on soft-body physics to model shear deformation, TactileLab uses rigid-body simulation to efficiently estimate dense tangential motion at the contact interface, producing tactile flow fields that encode shear-relevant contact dynamics. This flow field complements geometric features from a contact depth field. We further introduce a novel policy architecture for jointly processing long-horizon proprioceptive signals and rich tactile observations. Across multiple contact-rich tasks, policies trained using simulated tactile flow learn efficiently at scale and exhibit emergent contact-aware behaviours. To facilitate sim-to-real policy deployment, we then propose a novel real-to-sim tactile translation method that maps real tactile image streams to simulated tactile flow and depth fields, together with a new tactile data collection method, and validate it across diverse tactile sensor designs. Using this pipeline, we demonstrate real-world deployment on tasks encompassing dual-arm and dexterous in-hand manipulation. Overall, TactileLab provides an end-to-end sim-to-real framework for scalable tactile policy learning, enabling diverse shear-sensitive manipulation across heterogeneous tactile robotic systems.

</details>

#### 2026-11-04 - Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation

**Authors:** Weiduo Yuan, Ze Yuan, Sihan Liu, Jionghao Wang, Liang Heng, Zhenyu Zhao, Yue Wang
**Links:** [abs](https://arxiv.org/abs/2611.07229) - [pdf](https://arxiv.org/pdf/2611.07229)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation
- 作者：Weiduo Yuan, Ze Yuan, Sihan Liu, Jionghao Wang, Liang Heng, Zhenyu Zhao, Yue Wang
- 出版日期：2026-11-04T23:34:19Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.07229) / [PDF](https://arxiv.org/pdf/2611.07229)

### 一句话总结
提出 Spatial-UMI-Dream，一个基于 605 小时 RGB-D UMI 数据、经两阶段训练以联合预测未来 RGB、鱼眼对齐度量深度与动作的 5B 空间 World Action Model，并配套构建 RoboTwin-UMI 基准以评估 UMI 策略在环境与机器人本体变化下的泛化性。

### 研究问题
UMI 虽支持与特定机器人无关的可扩展演示采集，但其移动的近距夹爪相机使相机运动与物体运动相互纠缠，缺乏稳定外部视角；精确操作所需的度量几何信息仅隐含在 RGB 中。此外，评估 UMI 策略需要检验其“机器人无关演示采集”能否转化为跨机器人本体的策略泛化，以及对环境变化的鲁棒性。

### 核心思路/方法
- 构建 5B 规模的 Spatial-UMI-Dream（WAM），在 605 小时 RGB-D UMI 数据上预训练。
- 采用两阶段训练：先进行 world-only 适配，再进行 world-action 联合学习。
- 联合预测未来 RGB、鱼眼对齐的度量深度与动作；通过立体视觉推导的深度，在统一的双夹爪 RGB-D 表示中显式表达场景尺度与空间关系。
- 提出 RoboTwin-UMI：基于 RoboTwin 的二十任务仿真基准，使用 UMI 腕部安装鱼眼观测，可在不额外微调的情况下，分别及联合控制环境与本体变化进行评估。

### 主要贡献
- 提出融合度量几何与 RGB-D 表示的空间 World Action Model，以显式空间尺度缓解 UMI 视角下几何信息隐含的问题。
- 构建 RoboTwin-UMI 二十任务仿真基准，支持在环境变化、本体变化及二者联合条件下对 UMI 策略进行受控、可重复评估。
- 在 RoboTwin-UMI 上报告：域内成功率 79.10%，本体与环境联合偏移下 72.15%，分别超过最强评估基线 4.65 与 10.30 个百分点；在本体迁移下表现出评估策略中最小的成功率下降。
- 匹配预训练消融显示：仅 RGB 预训练相较 RGB-D 预训练使域内成功率下降 5.75 个百分点。
- 在六个真实世界任务上平均成功率达 85.0%，超过最强基线 24.2 个百分点。

### 局限性
- 摘要未提供足够信息说明模型参数量 5B 带来的计算成本、推理延迟或训练资源需求。
- 摘要未提供足够信息说明 RoboTwin-UMI 基准的任务多样性细节、仿真到现实差距及评测协议细节。
- 摘要未提供足够信息说明六个真实世界任务的具体设置、基线列表与统计显著性。
- 摘要未提供足够信息说明方法在非 UMI 采集设置或其他传感模态下的适用性。
- 摘要未提供足够信息说明失败案例、安全性或长期运行稳定性。

### 阅读优先级
高。理由：该工作同时涉及 UMI 操作中的度量几何建模、World Action Model 的大规模预训练与跨本体/环境泛化评测基准，摘要给出了明确的量化收益与消融结果，对具身操作与世界模型方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

The Universal Manipulation Interface (UMI) enables scalable demonstration collection independently of a specific robot. However, its moving, close-range gripper cameras entangle camera and object motion without a stable external view, leaving the metric geometry needed for precise manipulation implicit in RGB. We introduce Spatial-UMI-Dream, a 5B spatial World Action Model (WAM) pretrained on 605 hours of RGB-D UMI data through two-stage training -- world-only adaptation followed by joint world-action learning -- to jointly predict future RGB, fisheye-aligned metric depth, and actions. Stereo-derived depth makes scene scale and spatial relationships explicit within a unified dual-gripper RGB-D representation. Furthermore, evaluating UMI policies requires testing whether UMI's robot-independent demonstration collection translates into policy generalization across robot embodiments, alongside robustness to environmental changes. We introduce RoboTwin-UMI, a twenty-task simulation benchmark built on RoboTwin with UMI wrist-mounted fisheye observations, enabling controlled, repeatable evaluation of UMI policies under environment and embodiment changes separately and jointly without additional fine-tuning. On RoboTwin-UMI, Spatial-UMI-Dream achieves 79.10% in-domain success and 72.15% under combined embodiment and environment shifts, exceeding the strongest evaluated baseline in each setting by 4.65 and 10.30 percentage points, respectively. It also exhibits the smallest success-rate drop under embodiment transfer among the evaluated policies. In a matched pretraining ablation, RGB-only pretraining leads to a 5.75-percentage-point decrease in in-domain success compared with RGB-D pretraining. Across six real-world tasks, Spatial-UMI-Dream achieves 85.0% average success, exceeding the strongest baseline by 24.2 percentage points. Project page: https://weiduoyuan.com/spatial-umi-dream/

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
